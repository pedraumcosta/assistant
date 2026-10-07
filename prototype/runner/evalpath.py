"""The evaluation path (DESIGN §4.2, decision T12), shown end to end on one task.

The software under change is itself built on a model: a reminder email is
drafted by a model from a prompt the author's code builds. One run of such
a system proves little, so the verdict is an evaluation — fixed cases, some
hidden from the author, sampled repeatedly, scored by code, and decided as
passed, failed or inconclusive on the whole confidence interval.

    python -m prototype.runner.evalpath author             # the agent rewrites the prompt
    python -m prototype.runner.evalpath evaluate --target base
    python -m prototype.runner.evalpath evaluate --target author

Boundaries, the same as everywhere in the prototype: the author's code runs
only in a container with no network and no key (it builds prompt strings —
a pure function); the model is called from the host by the pipeline; the
hidden cases never enter the author's container; spend is reserved on the
ledger before it happens. Every requirement here is scored by code, so no
model scorer (and no scorer-agreement measurement) was needed; where code
could not score, DESIGN §4.2 requires a measured scorer, which this task
does not exercise.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import math
import re
import shutil
import time
from pathlib import Path

import yaml

from prototype.runner import paths
from prototype.runner.agent import run_agent
from prototype.runner.events import EventLog
from prototype.runner.ledger import Ledger
from prototype.runner.prices import cost_usd
from prototype.runner.sandbox import AgentBox, IMAGE, run_once

ROOT = paths.ROOT / "evalpath"
RUNS = paths.RUNS / "evalpath"

CLAIM = ("\n\nWhen you stop, end your last message with exactly one of these lines: "
         "`CLAIM: done` if the task is complete, or `CLAIM: not done` if it is not.")


def contract() -> dict:
    return yaml.safe_load((ROOT / "contract.yaml").read_text())


def load_cases() -> list[dict]:
    visible = yaml.safe_load((ROOT / "cases" / "visible.yaml").read_text())
    hidden = yaml.safe_load((ROOT / "hidden" / "cases.yaml").read_text())
    out = [{**c, "visible": True} for c in visible] + [{**c, "visible": False} for c in hidden]
    for c in out:        # YAML reads dates as objects; the app takes strings
        c["invoice"] = {k: str(v) for k, v in c["invoice"].items()}
    return out


# ---------------------------------------------------------------- scoring
# Code first, per DESIGN §4.2. Forbidden-claim patterns, not bare words: a
# customer named "Approved Partners Ltd" must be nameable without tripping
# R3 (hidden case h1 exists to hold exactly this line).
_CLAIM_PATTERNS = [
    r"(?:is|was|has been|have been|been)\s+(?:pre-?)?approved",
    r"approved\s+for\s+(?:processing|payment|financing)",
    r"approval\s+(?:has|was|is)",
    r"guarantee[ds]?",
]


def score(draft: str, invoice: dict) -> dict:
    """Each requirement pass-or-fail, by code. A sample passes only if all do."""
    text = draft.strip()
    low = text.lower()
    checks = {
        "R1": invoice["number"] in text,
        "R2": invoice["total"] in text and invoice["currency"].lower() in low,
        "R3": not any(re.search(p, low) for p in _CLAIM_PATTERNS),
        "R4": len(text) <= 400,
        # R5, scorer v2. The v1 scorer demanded the literal words "payment
        # date" and wrongly failed 40 of 40 drafts that asked "could you
        # confirm the date on which you will make the payment?" - the
        # false-fail error source DESIGN 4.2 names, caught by reading the
        # samples. v2 accepts any question that asks about paying and a date.
        "R5": any(("pay" in q and ("date" in q or "when" in q))
                  for q in low.split("?")[:-1]),
    }
    return {"checks": checks, "passed": all(checks.values())}


# ---------------------------------------------------------------- decision
def wilson(passed: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total == 0:
        return 0.0, 1.0
    p = passed / total
    d = 1 + z * z / total
    centre = (p + z * z / (2 * total)) / d
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / d
    return max(0.0, centre - half), min(1.0, centre + half)


def decide(passed: int, total: int, pass_mark: float) -> str:
    low, high = wilson(passed, total)
    if low >= pass_mark:
        return "passed"
    if high < pass_mark:
        return "failed"
    return "inconclusive"


# ---------------------------------------------------------------- the app
def build_prompts(snapshot: Path, cases: list[dict], out: Path) -> dict[str, str]:
    """The author's pure function runs in a container; prompts come out as a file."""
    out.mkdir(parents=True, exist_ok=True)
    (out / "cases.json").write_text(json.dumps([c["invoice"] for c in cases]))
    code = ("import json, sys; sys.path.insert(0, '/work'); "
            "from invoicing_reminder import reminder_prompt; "
            "cases = json.load(open('/out/cases.json')); "
            "json.dump([reminder_prompt(c) for c in cases], open('/out/prompts.json', 'w'))")
    r = run_once([(snapshot, "/work", "ro"), (out, "/out", "rw")],
                 ["python", "-c", code], workdir="/work", timeout=60)
    if r.code != 0:
        raise RuntimeError(f"the author's prompt builder failed in its container: {r.stderr[-800:]}")
    prompts = json.loads((out / "prompts.json").read_text())
    return {c["id"]: p for c, p in zip(cases, prompts)}


class AppModel:
    """The model the application runs on, called by the pipeline on the host."""

    def __init__(self, model: str):
        import anthropic
        from dotenv import dotenv_values
        key = dotenv_values(paths.ROOT.parent / ".env").get("ANTHROPIC_API_KEY")
        self.model = model
        self.client = anthropic.Anthropic(api_key=key, max_retries=3, timeout=120)
        self.spent = 0.0

    def draft(self, prompt: str) -> str:
        # 2000, not a tight cap: the first evaluation round capped output at
        # 300 tokens and silently truncated drafts mid-sentence (some to
        # nothing), which the per-requirement failures exposed. The app's
        # length policy is a requirement (R4), not a token cap.
        r = self.client.messages.create(model=self.model, max_tokens=2000,
                                        messages=[{"role": "user", "content": prompt}])
        usage = {k: getattr(r.usage, k, 0) or 0 for k in
                 ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}
        self.spent += cost_usd(self.model, usage)
        return "".join(b.text for b in r.content if b.type == "text")


# ---------------------------------------------------------------- author
def author() -> None:
    """The agent rewrites the prompt template. It sees the task, the app and
    the visible cases — never the hidden ones."""
    c = contract()
    rdir = RUNS / "author"
    if (rdir / "outcome.json").is_file():
        print("author run already recorded"); return
    if rdir.exists():
        shutil.rmtree(rdir)
    base, work = rdir / "base", rdir / "work"
    base.mkdir(parents=True)
    shutil.copy(ROOT / "app" / "invoicing_reminder.py", base / "invoicing_reminder.py")
    (base / "cases").mkdir()
    shutil.copy(ROOT / "cases" / "visible.yaml", base / "cases" / "visible.yaml")
    shutil.copy(ROOT / "task.md", base / "task.md")
    shutil.copytree(base, work)

    ledger = Ledger(paths.RUNS / "ledger.jsonl")
    ledger.reserve("evalpath/author", c["budget"]["author_usd"])
    from prototype.runner.run import make_model
    model, model_name = make_model("sonnet", "e1-payment-reminder", c["budget"]["author_usd"])
    log = EventLog(rdir / "events.jsonl", run="evalpath-author", task="e1-payment-reminder", model=model_name)
    prompt = (ROOT / "task.md").read_text() + CLAIM
    with AgentBox(work) as box:
        ended = run_agent(model, prompt, box, log, max_turns=20, max_cost=c["budget"]["author_usd"])
    ledger.settle("evalpath/author", ended["cost_usd"])
    snap = rdir / "snapshot"
    shutil.copytree(work, snap)
    (rdir / "outcome.json").write_text(json.dumps(
        {"stop_reason": ended["stop_reason"], "turns": ended["turns"],
         "cost_usd": round(ended["cost_usd"], 6), "final_text": ended["final_text"][-400:]}, indent=2) + "\n")
    print(f"author: {ended['stop_reason']}, {ended['turns']} turns, {ended['cost_usd']:.4f} USD")


# ---------------------------------------------------------------- evaluate
def evaluate(target: str) -> dict:
    c = contract()
    ev = c["evaluation"]
    out = RUNS / f"evaluation-{target}"
    record = out / "verdict.json"
    if record.is_file():
        v = json.loads(record.read_text()); print(json.dumps(v["summary"], indent=2)); return v
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    snapshot = (ROOT / "app") if target == "base" else (RUNS / "author" / "snapshot")

    cases = load_cases()
    prompts = build_prompts(snapshot, cases, out / "prompts")
    ledger = Ledger(paths.RUNS / "ledger.jsonl")
    ledger.reserve(f"evalpath/evaluation-{target}", c["budget"]["evaluation_usd"])
    app = AppModel(ev["app_model"])
    started = time.monotonic()

    samples: list[dict] = []

    def round_of(repeats_from: int, repeats_to: int) -> None:
        for case in cases:
            for rep in range(repeats_from, repeats_to + 1):
                draft = app.draft(prompts[case["id"]])
                s = score(draft, case["invoice"])
                samples.append({"case": case["id"], "visible": case["visible"], "repeat": rep,
                                "passed": s["passed"], "checks": s["checks"], "draft": draft})

    round_of(1, ev["repeats"])
    passed = sum(s["passed"] for s in samples)
    verdict = decide(passed, len(samples), ev["pass_mark"])
    extended = False
    if verdict == "inconclusive" and ev["max_repeats"] > ev["repeats"]:
        extended = True             # the budget buys more samples before a person is asked
        round_of(ev["repeats"] + 1, ev["max_repeats"])
        passed = sum(s["passed"] for s in samples)
        verdict = decide(passed, len(samples), ev["pass_mark"])
    ledger.settle(f"evalpath/evaluation-{target}", app.spent)

    low, high = wilson(passed, len(samples))
    by_req = {r: sum(not s["checks"][r] for s in samples) for r in ("R1", "R2", "R3", "R4", "R5")}
    by_case = {case["id"]: share for case in cases
               if (share := [s["passed"] for s in samples if s["case"] == case["id"]]) is not None}
    summary = {
        "target": target, "verdict": verdict,
        "samples": len(samples), "passed": passed,
        "pass_rate": round(passed / len(samples), 3),
        "interval_95": [round(low, 3), round(high, 3)], "pass_mark": ev["pass_mark"],
        "extended_sampling": extended,
        "failures_by_requirement": by_req,
        "by_case": {k: f"{sum(v)} of {len(v)}" for k, v in by_case.items()},
        "hidden_cases_failed_samples": sum(1 for s in samples if not s["visible"] and not s["passed"]),
        "app_model": ev["app_model"], "cost_usd": round(app.spent, 6),
        "seconds": round(time.monotonic() - started, 1),
    }
    (out / "samples.json").write_text(json.dumps(samples, indent=2) + "\n")
    record.write_text(json.dumps({"summary": summary}, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return {"summary": summary}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("step", choices=["author", "evaluate"])
    p.add_argument("--target", choices=["base", "author"], default="author")
    a = p.parse_args()
    author() if a.step == "author" else evaluate(a.target)


if __name__ == "__main__":
    main()
