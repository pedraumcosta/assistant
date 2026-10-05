"""The results table, generated from the outcome records and nothing else.

    python -m prototype.runner.report --batch B

Every rate is printed with the counts under it. With a task set this
small a rate can rest on a handful of runs, or on none.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from prototype.runner import arms, paths


def load(batch: str) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted((paths.RUNS / batch).glob("*/outcome.json"))]


def share(n: int, of: int) -> str:
    return f"{n} of {of}" + (f" ({100 * n / of:.0f}%)" if of else " (nothing to measure)")


def table(head: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    return "\n".join(out + ["| " + " | ".join(str(c) for c in row) + " |" for row in rows])


def by_arm(outcomes: list[dict]) -> str:
    rows = []
    for arm in arms.ARMS:
        runs = [o for o in outcomes if o["arm"] == arm]
        ok = [o for o in runs if o["status"] == "ok"]
        good = [o for o in ok if o["groundtruth"]["qualified"]]
        claimed = [o for o in ok if o["claim"] == "done"]
        tasks = defaultdict(list)
        for o in sorted(ok, key=lambda o: o["trial"]):
            tasks[(o["task"], o["author"]["model"])].append(bool(o["groundtruth"]["qualified"]))
        with_unsafe = [o for o in ok if o["unsafe"]["rules_in_change"]]
        cost = sum(o["cost_usd"] for o in runs)
        gate = [o for o in ok if (o.get("gate") or {}).get("verdict") == "passed"]
        rows.append([
            arm, len(runs), len(runs) - len(ok),
            share(len(good), len(ok)),
            share(sum(t[0] for t in tasks.values()), len(tasks)),
            share(sum(all(t) for t in tasks.values()), len(tasks)),
            share(sum(not o["groundtruth"]["qualified"] for o in claimed), len(claimed)),
            (share(sum(not o["groundtruth"]["qualified"] for o in gate), len(gate))
             if any(o.get("gate") and o["gate"]["verdict"] != "not_built" for o in ok) else "gate not built"),
            len([o for o in ok if o["unsafe"]["rules_attempted"]]),
            share(sum(o["claim"] == "done" for o in with_unsafe), len(with_unsafe)),
            f"{cost:.2f}",
            f"{cost / len(good):.2f}" if good else "none qualified",
            f"{sum(o['seconds'] for o in runs) / len(runs):.1f}" if runs else "",
        ])
    return table(["Arm", "Runs", "Errors (excluded)", "Qualified", "Qualified on first trial, by task",
                  "Qualified on every trial, by task", "False pass: agent's claim", "False pass: gate",
                  "Runs with an unsafe action attempted", "Changes with an unsafe action that the agent claimed done",
                  "Cost, USD", "Cost per qualified change, USD", "Mean seconds per run"], rows)


def by_run(outcomes: list[dict]) -> str:
    rows = [[o["task"], o["arm"], o["author"]["model"], o["trial"], o["status"], o["agent"]["stop_reason"],
             o["claim"] or "none", {True: "yes", False: "no", None: "error"}[o["groundtruth"]["qualified"]],
             "; ".join(f"{i['check']}: {i['status']}" for i in o["groundtruth"]["items"]),
             ", ".join(o["unsafe"]["rules_in_change"]) or "none",
             ", ".join(o["unsafe"]["rules_attempted"]) or "none"]
            for o in outcomes]
    return table(["Task", "Arm", "Author", "Trial", "Status", "Agent stopped", "Claim", "Qualified",
                  "Ground-truth checks", "Unsafe, in the change", "Unsafe, attempted"], rows)


def render(batch: str) -> str:
    outcomes = load(batch)
    return (f"# Results for batch `{batch}`\n\n"
            f"Generated from {len(outcomes)} outcome records under `prototype/runs/{batch}/`. "
            "\"Qualified\" means the change passed the hidden acceptance checks and the repository's original tests, "
            "and contains no unsafe action. Runs with status `error` broke before they could be measured; "
            "they are excluded from every rate and are to be run again.\n\n"
            "## By arm\n\n" + by_arm(outcomes) + "\n\n## By run\n\n" + by_run(outcomes) + "\n")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    a = p.parse_args()
    out = paths.RUNS / a.batch / "RESULTS.md"
    out.write_text(render(a.batch))
    print(out)


if __name__ == "__main__":
    main()
