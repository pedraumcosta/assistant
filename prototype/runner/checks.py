"""Running one check and reading its result as an evidence item.

A check ends in one of three states. `error` means the check itself did
not produce a result we can trust; it is never read as a pass and never
counted as a fail. A check passes only when it exits clean AND reports
the number of tests it is known to contain, all of them passed.
"""
from __future__ import annotations

import time
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

from prototype.runner import sandbox

PYTEST = ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", "/checks",
          "-o", "junit_family=xunit2"]


def _read_junit(path: Path) -> dict | None:
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError):
        return None
    counts = {"total": 0, "failed": 0, "errors": 0, "skipped": 0}
    first = None
    cases = {}      # test id -> passed | failed | errors | skipped
    for case in root.iter("testcase"):
        counts["total"] += 1
        ident = f"{case.get('classname', '')}::{case.get('name', '')}".strip(":")
        cases[ident] = "passed"
        for kind, key in (("failure", "failed"), ("error", "errors"), ("skipped", "skipped")):
            if case.find(kind) is not None:
                counts[key] += 1
                cases[ident] = key
                if first is None and kind != "skipped":
                    first = f"{case.get('classname', '')}::{case.get('name', '')}".strip(":")
    counts["passed"] = counts["total"] - counts["failed"] - counts["errors"] - counts["skipped"]
    counts["first_failure"] = first
    counts["cases"] = cases
    return counts


def pytest_check(name: str, mounts: list[tuple[Path, str, str]], target: str, out_dir: Path,
                 expected_tests: int | None, env: dict[str, str] | None = None,
                 timeout: int = 180, min_tests: int = 1, extra_args: tuple[str, ...] = ()) -> dict:
    """Run pytest on `target` in a fresh container and return an evidence item."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    # A name no earlier run used: a report can only be this run's own, and
    # the host never has a stale view of a file it deleted a moment ago.
    junit = out_dir / f"junit-{uuid.uuid4().hex}.xml"
    result = sandbox.run_once([*mounts, (out_dir, "/out", "rw")],
                              [*PYTEST, *extra_args, f"--junitxml=/out/{junit.name}", target],
                              workdir="/checks", env=env, timeout=timeout)
    (out_dir / "stdout.txt").write_text(result.stdout[-20000:])
    (out_dir / "stderr.txt").write_text(result.stderr[-20000:])
    tests = _read_junit(junit)
    cases = None
    for _ in range(10):     # the mount can show the file a moment after the container wrote it
        if tests is not None or result.timed_out:
            break
        time.sleep(0.3)
        tests = _read_junit(junit)
    if tests is not None:
        cases = tests.pop("cases")
    item = {"check": name, "exit_code": result.code, "duration_s": result.duration_s,
            "expected_tests": expected_tests, "tests": tests, "cases": cases}

    def end(status: str, reason: str) -> dict:
        return {**item, "status": status, "reason": reason}

    if result.timed_out:
        return end("error", f"did not finish in {timeout}s")
    if tests is None:
        return end("error", f"no readable test report (exit code {result.code})")
    if result.code == 0:
        if tests["failed"] or tests["errors"] or tests["skipped"]:
            return end("error", "exit code 0 but the report shows tests that did not pass")
        if tests["total"] < min_tests:
            return end("error", f"exit code 0 but only {tests['total']} tests ran, at least {min_tests} expected")
        if expected_tests is not None and tests["total"] != expected_tests:
            return end("error", f"{tests['total']} tests ran, {expected_tests} expected")
        return end("passed", f"{tests['passed']} of {tests['total']} tests passed")
    if result.code == 1 or (result.code == 2 and tests["errors"]):
        bad = tests["failed"] + tests["errors"]
        return end("failed", f"{bad} of {tests['total']} tests did not pass; first: {tests['first_failure']}")
    return end("error", f"pytest exit code {result.code}")
