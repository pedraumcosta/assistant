"""Counts the tests each ground-truth check contains, on the task's base.

The count is what lets a check tell "all passed" from "something made
pytest exit clean early". Run again whenever a check file changes:

    python -m prototype.runner.manifest
"""
from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path

from prototype.runner import sandbox
from prototype.runner.paths import GROUNDTRUTH, build_base, task_ids

COLLECT = ["python", "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", "--rootdir", "/checks"]


def count(mounts, target: str) -> int:
    r = sandbox.run_once(mounts, [*COLLECT, target], workdir="/checks", env={"PYTHONPATH": "/work", "WORK": "/work"})
    found = re.search(r"^(\d+) tests? collected", r.stdout, re.MULTILINE)
    if r.code != 0 or not found:
        raise SystemExit(f"could not collect {target}:\n{r.stdout}\n{r.stderr}")
    return int(found.group(1))


def main() -> None:
    for task in task_ids():
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent.parent) as tmp:
            base = build_base(task, Path(tmp) / "base")
            counts = {
                "acceptance_tests": count([(base, "/work", "ro"), (GROUNDTRUTH / task, "/checks", "ro")],
                                          "/checks/test_acceptance.py"),
                "regression_tests": count([(base, "/work", "ro"), (base / "tests", "/checks/tests", "ro")],
                                          "/checks/tests"),
            }
        (GROUNDTRUTH / task / "manifest.json").write_text(json.dumps(counts, indent=2) + "\n")
        print(task, counts)


if __name__ == "__main__":
    main()
