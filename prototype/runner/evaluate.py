"""The slice-6 batch: the evaluator agent over a sample of finished runs.

    python -m prototype.runner.evaluate --batch arms-sonnet            # trial 1 of every task x arm
    python -m prototype.runner.evaluate --batch sizing --runs o1-bulk-discount__bare__sonnet__t1
    python -m prototype.runner.evaluate --batch arms-sonnet --model fake-eval   # plumbing, no spend

The default sample is the first trial of every task-and-arm cell: it
covers every task and every arm once, 33 evaluations, without buying the
whole batch twice. Evaluations are idempotent (a written verdict is not
re-bought) and each is reserved on the ledger before it starts.
"""
from __future__ import annotations

import argparse
import json
import time
import traceback

from prototype.runner import paths
from prototype.runner.evaluator import EVAL_BUDGET_USD, EVAL_MODEL, evaluate_run
from prototype.runner.ledger import Ledger


def sample(batch: str, trial: int = 1) -> list[str]:
    """Trial `trial` of every task x arm cell that has a finished outcome."""
    out = []
    for run_dir in sorted((paths.RUNS / batch).iterdir()):
        if run_dir.name.endswith(f"__t{trial}") and (run_dir / "outcome.json").is_file():
            out.append(run_dir.name)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    p.add_argument("--runs", nargs="*", default=None)
    p.add_argument("--trial", type=int, default=1, help="which trial of each cell the default sample takes")
    p.add_argument("--model", default=EVAL_MODEL)
    a = p.parse_args()

    runs = a.runs or sample(a.batch, a.trial)
    if not runs:
        raise SystemExit(f"no finished runs to evaluate in batch {a.batch!r}")
    print(f"evaluating {len(runs)} runs of batch {a.batch} with {a.model}")
    ledger = Ledger(paths.RUNS / "ledger.jsonl")
    started = time.monotonic()
    failed = 0
    for i, rid in enumerate(runs, 1):
        try:
            if a.model != "fake-eval":
                ledger.reserve(f"eval/{a.batch}/{rid}", EVAL_BUDGET_USD)
            v = evaluate_run(a.batch, rid, a.model)
            if a.model != "fake-eval":
                ledger.settle(f"eval/{a.batch}/{rid}", v["cost_usd"])
            print(f"[{i}/{len(runs)}] {rid}: {v['verdict']} ({v['turns']} turns, {v['cost_usd']:.4f} USD) "
                  f"- {v['reason'][:90]}", flush=True)
        except SystemExit:
            raise   # the ledger refusing is a stop, not a skip
        except Exception:
            failed += 1
            print(f"[{i}/{len(runs)}] {rid}: evaluation failure", flush=True)
            traceback.print_exc()
    print(f"done: {len(runs) - failed} evaluated, {failed} failures, {time.monotonic() - started:.0f}s")


if __name__ == "__main__":
    main()
