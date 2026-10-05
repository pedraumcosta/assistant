"""The dry run: the fake agent through every task, variant and arm. Spends nothing.

    python -m prototype.runner.dryrun [--jobs 4]

It proves the measurement before any money is spent: every correct change
must come out qualified, every wrong or unsafe one must not, and a run
whose provider failed must come out as an error, not as a result.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from prototype.runner import arms, fake, paths, report

BATCH = "dryrun-fake"
CRASH_TASKS = ("o1-bulk-discount", "t1-tax-rounding")


def matrix() -> list[tuple[str, str, str]]:
    out = []
    for task in paths.task_ids():
        agents = [f"fake:{v}" for v in fake.variants(task)] + (["fake:crash"] if task in CRASH_TASKS else [])
        out += [(task, arm, agent) for agent in agents for arm in arms.ARMS]
    return out


def expected(agent: str) -> tuple[str, bool | None]:
    """(status, qualified) a dry run must give for this fake agent."""
    return {"fake:good": ("ok", True), "fake:bad": ("ok", False), "fake:unsafe": ("ok", False),
            "fake:crash": ("error", False)}[agent]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--jobs", type=int, default=4)
    a = p.parse_args()
    shutil.rmtree(paths.RUNS / BATCH, ignore_errors=True)
    ledger = paths.RUNS / BATCH / "ledger.jsonl"    # its own ledger: a dry run is not spend

    def one(job):
        task, arm, agent = job
        r = subprocess.run([sys.executable, "-m", "prototype.runner.run", "--batch", BATCH, "--task", task,
                            "--arm", arm, "--agent", agent, "--ledger", str(ledger)],
                           capture_output=True, text=True, cwd=paths.ROOT.parent)
        return job, r

    jobs = matrix()
    failed = 0
    with ThreadPoolExecutor(a.jobs) as pool:
        for job, r in pool.map(one, jobs):
            if r.returncode != 0:
                failed += 1
                print("RUNNER FAILED", job, r.stderr[-800:])
    print(report.render(BATCH).split("## By run")[0])
    (paths.RUNS / BATCH / "RESULTS.md").write_text(report.render(BATCH))

    wrong = []
    outcomes = {(o["task"], o["arm"], o["author"]["model"]): o for o in report.load(BATCH)}
    for job in jobs:
        o = outcomes.get(job)
        want = expected(job[2])
        got = (o["status"], o["groundtruth"]["qualified"]) if o else None
        if o is None or got[0] != want[0] or (want[0] == "ok" and got[1] is not want[1]):
            wrong.append((job, want, got))
    for w in wrong:
        print("UNEXPECTED", *w)
    print(f"{len(jobs)} runs, {failed} runner failures, {len(wrong)} unexpected outcomes")
    return 1 if failed or wrong else 0


if __name__ == "__main__":
    sys.exit(main())
