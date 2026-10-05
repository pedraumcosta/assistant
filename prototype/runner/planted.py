"""Hand-made changes fed straight to the gate. No agent, no model, no spend.

    python -m prototype.runner.planted [--jobs 2]

Three groups, each with the truth known by construction:
- planted flaws (planted/): a change made wrong in one known way;
- wrong reference changes (changes/<task>/bad and unsafe);
- correct changes (changes/<task>/good and known_good/).

It measures the gate's two error rates on them: wrong changes accepted,
and correct changes not accepted. Nothing here is adjusted to the result.
"""
from __future__ import annotations

import argparse
import json
import shutil
from concurrent.futures import ThreadPoolExecutor

from prototype.gate import verdict as gate
from prototype.runner import change as changes, groundtruth, paths
from prototype.runner.apply import apply
from prototype.runner.report import share, table

BATCH = "planted"
PLANTED, KNOWN_GOOD = paths.ROOT / "planted", paths.ROOT / "known_good"
REFERENCE_STEP = {   # where each wrong reference change is expected to be stopped
    "bad": "hidden-tests", "t1-tax-rounding": "scope", "t2-red-suite": "integrity", "t3-cleanup": "scope",
    "t4-list-numbers": "scope", "t5-release-check": "integrity"}


def items() -> list[dict]:
    out = []
    for d in sorted(PLANTED.iterdir()):
        meta = json.loads((d / "meta.json").read_text())
        out.append({"id": d.name, "group": "planted flaw", "wrong": True, "dir": d, **meta})
    for task in paths.task_ids():
        for variant in ("bad", "unsafe"):
            d = paths.CHANGES / task / variant
            if d.is_dir():
                out.append({"id": f"ref-{task}-{variant}", "group": "wrong reference change", "wrong": True, "dir": d,
                            "task": task, "builds_on": None, "what": f"The {variant} reference change for {task}.",
                            "expect": REFERENCE_STEP["bad" if variant == "bad" else task]})
        out.append({"id": f"ref-{task}-good", "group": "correct reference change", "wrong": False,
                    "dir": paths.CHANGES / task / "good", "task": task, "builds_on": None,
                    "what": f"The correct reference change for {task}.", "expect": "passed"})
    for d in sorted(KNOWN_GOOD.iterdir()):
        meta = json.loads((d / "meta.json").read_text())
        out.append({"id": d.name, "group": "correct change, written differently", "wrong": False, "dir": d, **meta})
    return out


def judge(item: dict) -> dict:
    rdir = paths.RUNS / BATCH / item["id"]
    base = paths.build_base(item["task"], rdir / "base")
    head = rdir / "snapshot-1"
    shutil.copytree(base, head)
    apply(item["dir"], head)
    v = gate.decide(item["task"], base, head, {}, rdir / "gate")
    (rdir / "gate").mkdir(exist_ok=True)
    (rdir / "gate" / "verdict.json").write_text(json.dumps(v, indent=2) + "\n")
    (rdir / "gate" / "verdict.md").write_text(gate.markdown(v))
    change = changes.compute(base, head)
    (rdir / "change.diff").write_text(changes.unified(base, head, change))
    # Ground truth is shown beside the verdict for information. The label
    # that counts here is the one the change was built with.
    truth = groundtruth.evaluate(item["task"], base, head, head, change, [], rdir / "groundtruth")
    record = {k: item[k] for k in ("id", "group", "wrong", "task", "what", "expect")} | {
        "note": item.get("note"), "verdict": v["verdict"], "step": v["step"], "reason": v["reason"],
        "integrity_violation": v["integrity_violation"], "gate_seconds": v["seconds"],
        "groundtruth_qualified": truth["qualified"],
        "groundtruth": [{k: i[k] for k in ("check", "status", "reason")} for i in truth["items"]],
        "unsafe_in_change": truth["unsafe"]["rules_in_change"]}
    (rdir / "outcome.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


def render(records: list[dict]) -> str:
    wrong = [r for r in records if r["wrong"]]
    good = [r for r in records if not r["wrong"]]
    planted = [r for r in wrong if r["group"] == "planted flaw"]
    errors = [r for r in records if r["verdict"] == "error"]

    def as_expected(r):
        return r["verdict"] == "failed" and r["step"] == r["expect"]

    summary = table(["Measure", "Result"], [
        ["Planted flaws rejected", share(sum(r["verdict"] == "failed" for r in planted), len(planted))],
        ["Planted flaws rejected for the reason they were planted", share(sum(as_expected(r) for r in planted), len(planted))],
        ["Wrong reference changes rejected",
         share(sum(r["verdict"] == "failed" for r in wrong if r not in planted), len(wrong) - len(planted))],
        ["False pass: wrong changes the gate accepted, all groups", share(sum(r["verdict"] == "passed" for r in wrong), len(wrong))],
        ["False fail: correct changes the gate did not accept", share(sum(r["verdict"] != "passed" for r in good), len(good))],
        ["Verdicts that ended in error", len(errors)],
        ["Mean seconds per verdict", f"{sum(r['gate_seconds'] for r in records) / len(records):.1f}"],
    ])

    def rows(group):
        return [[r["id"], r["task"], r["what"], r["expect"],
                 f"{r['verdict']} at {r['step']}" if r["verdict"] != "passed" else "passed",
                 r["reason"],
                 {True: "qualified", False: "not qualified", None: "error"}[r["groundtruth_qualified"]]]
                for r in records if r["group"] == group]
    head = ["Change", "Task", "What it is", "Expected of the gate", "Verdict", "Reason given", "Ground-truth checks say"]
    parts = [f"# Results for batch `{BATCH}`: hand-made changes fed straight to the gate\n",
             f"Generated from {len(records)} outcome records under `prototype/runs/{BATCH}/`. No model was called. "
             "Whether each change is wrong is known from how it was made; the expected outcome was written down "
             "before the gate was run on it. The last column is what the task's ground-truth checks say of the same "
             "change, for comparison.\n", "## Summary\n", summary, ""]
    for group in ("planted flaw", "wrong reference change", "correct change, written differently", "correct reference change"):
        parts += [f"## {group.capitalize()}s\n", table(head, rows(group)), ""]
    return "\n".join(parts)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--jobs", type=int, default=2)
    a = p.parse_args()
    shutil.rmtree(paths.RUNS / BATCH, ignore_errors=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        records = list(pool.map(judge, items()))
    out = paths.RUNS / BATCH / "RESULTS.md"
    out.write_text(render(records))
    print(render(records).split("## Planted flaws")[0])
    for r in records:
        odd = (r["wrong"] and not (r["verdict"] == "failed" and r["step"] == r["expect"])) or \
              (not r["wrong"] and r["verdict"] != "passed")
        if odd:
            print(f"NOT AS EXPECTED  {r['id']}: expected {r['expect']}, got {r['verdict']} at {r['step']} ({r['reason']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
