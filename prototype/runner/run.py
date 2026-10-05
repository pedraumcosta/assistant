"""One run: one task, one arm, one trial, from the base to the outcome record.

    python -m prototype.runner.run --batch B --task T --arm bare --agent fake:good --trial 1

The outcome record is written once. A run whose record exists is not run
again: the same request gives the same record, not a second one.
"""
from __future__ import annotations

import argparse
import json
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

from prototype.runner import arms, change as changes, groundtruth, paths
from prototype.runner.agent import run_agent
from prototype.runner.events import EventLog, read_events
from prototype.runner.fake import FakeModel
from prototype.runner.ledger import Ledger
from prototype.runner.sandbox import AgentBox, SandboxError


MODELS = {"sonnet": "claude-sonnet-5-5"}    # PLAN T22


def make_model(agent: str, task: str, budget_usd: float):
    if agent.startswith("fake:"):
        return FakeModel(task, agent.split(":", 1)[1]), agent
    if agent in MODELS:
        # The key is read here, on the host. It never enters a container.
        from dotenv import dotenv_values
        from prototype.scaffold.adapter_anthropic import AnthropicModel
        key = dotenv_values(paths.ROOT.parent / ".env").get("ANTHROPIC_API_KEY")
        return AnthropicModel(MODELS[agent], budget_usd, api_key=key), MODELS[agent]
    raise SystemExit(f"unknown agent {agent!r}")


def run_id(task: str, arm: str, agent: str, trial: int) -> str:
    return f"{task}__{arm}__{agent.replace(':', '-')}__t{trial}"


def run(batch: str, task: str, arm: str, agent: str, trial: int, ledger_path: Path | None = None) -> dict:
    rid = run_id(task, arm, agent, trial)
    rdir = paths.RUNS / batch / rid
    record = rdir / "outcome.json"
    if record.is_file():
        return json.loads(record.read_text())
    if rdir.exists():
        shutil.rmtree(rdir)     # a run that died before its record: start it clean
    rdir.mkdir(parents=True)

    contract = paths.contract(task)
    budget = contract["budget"]
    ledger = Ledger(ledger_path or paths.RUNS / "ledger.jsonl")
    ledger.reserve(f"{batch}/{rid}", budget["max_cost_usd"])   # refused here if it would pass the cap

    model, model_name = make_model(agent, task, budget["max_cost_usd"])
    scaffold = paths.sha256_file(paths.SCAFFOLD / "listing.py")
    log = EventLog(rdir / "events.jsonl", run=rid, batch=batch, task=task, arm=arm, trial=trial,
                   model=model_name, scaffold_sha256=scaffold[:16], contract_sha256=paths.contract_hash(task)[:16])
    started = time.monotonic()
    base = paths.build_base(task, rdir / "base")
    work = rdir / "work"
    shutil.copytree(base, work)
    log.emit("run_started", base_tree=changes.tree_hash(base), budget=budget)

    cost = 0.0
    try:
        with AgentBox(work) as box:
            ended = run_agent(model, arms.prompt(arm, paths.task_text(task), contract), box, log,
                              max_turns=budget["max_turns"], max_cost=budget["max_cost_usd"])
        cost = ended["cost_usd"]
    except SandboxError as e:
        ended = {"stop_reason": "container_error", "final_text": "", "detail": str(e), "turns": 0, "cost_usd": 0.0}
        log.emit("agent_stopped", **ended)
    finally:
        ledger.settle(f"{batch}/{rid}", cost)
    agent_seconds = round(time.monotonic() - started, 3)

    change = changes.compute(base, work)
    (rdir / "change.json").write_text(json.dumps(change, indent=2) + "\n")
    (rdir / "change.diff").write_text(changes.unified(base, work, change))
    snap = changes.snapshot(work, rdir / "snapshot")
    said = arms.claim(ended["stop_reason"], ended["final_text"])
    log.emit("change_recorded", **{k: len(v) for k, v in change.items()}, head_tree=changes.tree_hash(snap), claim=said)

    # The gate arrives with slice 3. Until then the gated arm differs from
    # the bare arm only in what the agent is told.
    gate = {"verdict": "not_built"} if arm == "gated" else None

    truth = groundtruth.evaluate(task, base, snap, work, change, read_events(rdir / "events.jsonl"), rdir / "groundtruth")
    for item in truth["items"]:
        log.emit("groundtruth_check", **item)

    infra = ended["stop_reason"] in ("provider_error", "container_error") or truth["qualified"] is None
    outcome = {
        "run": rid, "batch": batch, "task": task, "arm": arm, "trial": trial,
        "written": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        # error: the run or its measurement broke. It is neither a pass nor a fail, and is to be run again.
        "status": "error" if infra else "ok",
        "author": {"model": model_name, "scaffold_sha256": scaffold},
        "contract_sha256": paths.contract_hash(task), "risk_tier": contract["risk_tier"],
        "base_tree": changes.tree_hash(base), "head_tree": changes.tree_hash(snap),
        "agent": {k: ended[k] for k in ("stop_reason", "detail", "turns", "cost_usd")} | {"seconds": agent_seconds},
        "change": change,
        "claim": said,
        "gate": gate,
        "groundtruth": {"qualified": truth["qualified"],
                        "items": [{k: i[k] for k in ("check", "status", "reason", "duration_s")} for i in truth["items"]]},
        "unsafe": truth["unsafe"],
        "cost_usd": cost,
        "seconds": round(time.monotonic() - started, 3),
    }
    log.emit("outcome", status=outcome["status"], qualified=truth["qualified"], claim=said,
             unsafe_in_change=truth["unsafe"]["rules_in_change"])
    tmp = record.with_suffix(".tmp")
    tmp.write_text(json.dumps(outcome, indent=2) + "\n")
    tmp.rename(record)
    return outcome


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    p.add_argument("--task", required=True, choices=paths.task_ids())
    p.add_argument("--arm", required=True, choices=arms.ARMS)
    p.add_argument("--agent", required=True)
    p.add_argument("--trial", type=int, default=1)
    p.add_argument("--ledger", type=Path)
    a = p.parse_args()
    o = run(a.batch, a.task, a.arm, a.agent, a.trial, a.ledger)
    print(f"{o['run']}: status={o['status']} claim={o['claim']} qualified={o['groundtruth']['qualified']} "
          f"unsafe={o['unsafe']['rules_in_change']}")


if __name__ == "__main__":
    main()
