"""The batch of slice 5: every task, every arm, several trials, one model.

    python -m prototype.runner.batch --batch arms-sonnet --agent sonnet --trials 5

Runs are sequential and idempotent: a run whose outcome record exists is
skipped, so an interrupted batch is resumed by running the same command
again. The ledger refuses any run that would pass the spend cap, before
the run starts. One failed run does not stop the batch: its status is
`error` in its own record and the batch moves on.
"""
from __future__ import annotations

import argparse
import time
import traceback

from prototype.runner import arms, paths
from prototype.runner.run import run


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    p.add_argument("--agent", required=True)
    p.add_argument("--trials", type=int, default=5)
    p.add_argument("--tasks", nargs="*", default=None, choices=paths.task_ids())
    a = p.parse_args()

    tasks = a.tasks or paths.task_ids()
    todo = [(t, arm, n) for t in tasks for arm in arms.ARMS for n in range(1, a.trials + 1)]
    print(f"batch {a.batch}: {len(todo)} runs ({len(tasks)} tasks x {len(arms.ARMS)} arms x {a.trials} trials)")
    started = time.monotonic()
    done = failed = 0
    for i, (task, arm, trial) in enumerate(todo, 1):
        try:
            o = run(a.batch, task, arm, a.agent, trial)
            done += 1
            g = o["gate"] or {}
            print(f"[{i}/{len(todo)}] {o['run']}: status={o['status']} claim={o['claim']} "
                  f"gate={g.get('verdict')} qualified={o['groundtruth']['qualified']} "
                  f"cost={o['cost_usd']:.4f} ({time.monotonic() - started:.0f}s elapsed)", flush=True)
        except SystemExit as e:     # the ledger refusing is a stop, not a skip
            print(f"[{i}/{len(todo)}] {task}/{arm}/t{trial}: stopped: {e}", flush=True)
            raise
        except Exception:
            failed += 1
            print(f"[{i}/{len(todo)}] {task}/{arm}/t{trial}: runner failure", flush=True)
            traceback.print_exc()
    print(f"batch {a.batch}: {done} runs completed, {failed} runner failures, "
          f"{time.monotonic() - started:.0f}s")


if __name__ == "__main__":
    main()
