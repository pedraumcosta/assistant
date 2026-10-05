"""The verdict: executable evidence on a change, against its contract.

    python -m prototype.gate.verdict --task T --base DIR --head DIR --out DIR

What it reads: the base, the change, the contract with its hidden checks,
and three numbers about the run (cost, turns, seconds). It never reads the
author's conversation or its claim: a verifier that reads the author's
account of its work inherits the author's mistakes.

The decision order is DESIGN.md 4.1. First match wins. Checks that only
read the change come before checks that run it.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from prototype.runner import change as changes
from prototype.runner import checks, paths, sandbox, unsafe

TOOLS = Path(__file__).resolve().parent / "tools"
ENV = {"PYTHONPATH": "/work", "WORK": "/work"}
ROUTES = {"green": "accepted", "yellow": "review", "red": "person"}

SECRETS = [
    ("an AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("a private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("an API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("a GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("a password or token in code", re.compile(r"(?i)\b(password|passwd|secret|api_key|token)\s*=\s*['\"][^'\"\s]{8,}['\"]")),
]


def key(base_tree: str, head_tree: str, contract_sha: str) -> str:
    """What a verdict is a function of. The same three give the same record."""
    return hashlib.sha256(f"{base_tree}\n{head_tree}\n{contract_sha}".encode()).hexdigest()


# ------------------------------------------------------------ checks that only read

def integrity(base: Path, head: Path, change: dict) -> str | None:
    """Step 2. Was a protected path altered?"""
    for kind in ("added", "modified", "deleted"):
        for path in change[kind]:
            name = path.rsplit("/", 1)[-1]
            if name in unsafe.STRICT_NAMES:
                return f"the pipeline's configuration was changed: {path}"
            if kind == "added":
                continue
            if path.startswith("checks/"):
                return f"a check was changed: {path}"
            if path.startswith("tests/") and unsafe.weakened(base / path, head / path):
                return f"an existing test was removed or changed: {path}"
    return None


def scope(contract: dict, change: dict) -> str | None:
    """Step 6. Did the change stay where the contract allows?"""
    s = contract["scope"]
    for kind in ("added", "modified", "deleted"):
        for path in change[kind]:
            if unsafe.match(path, s.get("deny")):
                return f"{path} must not be changed"
            if kind != "added" and unsafe.match(path, s.get("keep")):
                return f"{path} must be kept as it is"
            if not unsafe.match(path, s.get("allow")):
                return f"{path} is outside the scope of the change"
    return None


def dependencies(head: Path, change: dict) -> str | None:
    """Step 8. Does the change import something that is not there?"""
    local = {p.stem if p.is_file() else p.name for p in head.iterdir()}
    known = set(sys.stdlib_module_names) | local | {"pytest"}
    for path in change["added"] + change["modified"]:
        file = head / path
        if not path.endswith(".py") or file.is_symlink():
            continue
        try:
            tree = ast.parse(file.read_text())
        except (SyntaxError, UnicodeDecodeError):
            continue    # the build check has already spoken
        for node in ast.walk(tree):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else \
                    [node.module] if isinstance(node, ast.ImportFrom) and node.module and not node.level else []
            for name in names:
                if name.split(".")[0] not in known:
                    return f"{path} imports {name}, which is not available"
    return None


def secrets(base: Path, head: Path, change: dict) -> str | None:
    """Step 8. Is there a secret in what was added?"""
    for line in changes.unified(base, head, change).splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            for what, pattern in SECRETS:
                if pattern.search(line):
                    return f"the change adds what looks like {what}"
    return None


# ------------------------------------------------------------ checks that run the change

def build(head: Path, head_tree: str, packages: list[str], out: Path) -> dict:
    """Step 4. Also confirms that the container sees exactly the change being judged."""
    out.mkdir(parents=True, exist_ok=True)
    r = sandbox.run_once([(head, "/work", "ro"), (TOOLS, "/gate", "ro")],
                         ["python", "/gate/build_check.py", head_tree, *packages], workdir="/tmp", timeout=120)
    (out / "stdout.txt").write_text(r.stdout[-20000:])
    item = {"check": "build", "exit_code": r.code, "duration_s": r.duration_s}
    if r.code == 0 and r.stdout.strip().endswith("BUILD-OK"):
        return {**item, "status": "passed", "reason": "parses and imports"}
    if r.code == 1 and r.stdout.strip():
        return {**item, "status": "failed", "reason": r.stdout.strip().splitlines()[-1][:300]}
    if r.code == 3:
        return {**item, "status": "error", "reason": "the container did not see the change to be judged"}
    return {**item, "status": "error", "reason": f"the build check gave no result (exit code {r.code})"}


def adequacy(base: Path, head: Path, author: dict, repo_ids: set[str], required: bool, out: Path) -> dict:
    """Step 7. Do the author's own new tests tell the new code from the old?

    They are run against the original code, where at least one must fail.
    Tests that pass on both prove nothing about the change.
    """
    new = sorted(set(author["cases"]) - repo_ids)
    item = {"check": "test-adequacy", "new_tests": len(new), "duration_s": 0.0}
    if not new:
        if required:
            return {**item, "status": "failed", "reason": "the contract requires tests for the change and none was added"}
        return {**item, "status": "passed", "reason": "no tests were added and none was required"}
    run = checks.pytest_check("test-adequacy", [(base, "/work", "ro"), (head / "tests", "/checks/tests", "ro")],
                              "/checks/tests", out, None, ENV, extra_args=("--continue-on-collection-errors",))
    item["duration_s"] = run["duration_s"]
    if run["cases"] is None or run["exit_code"] not in (0, 1, 2):
        return {**item, "status": "error", "reason": "could not run the new tests against the original code: " + run["reason"]}
    broken_modules = {name for name, state in run["cases"].items() if "::" not in name and state == "errors"}
    failing = [t for t in new
               if run["cases"].get(t) in ("failed", "errors") or t.split("::")[0] in broken_modules]
    item["new_tests_failing_on_original"] = len(failing)
    if failing:
        return {**item, "status": "passed",
                "reason": f"{len(failing)} of {len(new)} new tests fail against the original code"}
    return {**item, "status": "failed",
            "reason": f"all {len(new)} new tests pass against the original code, so they do not test the change"}


# ------------------------------------------------------------------------- the verdict

def decide(task: str, base: Path, head: Path, meta: dict, out: Path) -> dict:
    """Produce the verdict for one change. `meta` is cost_usd, turns, seconds, stop_reason."""
    started = time.monotonic()
    contract = paths.contract(task)
    want = contract["checks"]
    budget = contract["budget"]
    change = changes.compute(base, head)
    evidence: list[dict] = []
    base_tree, head_tree, contract_sha = changes.tree_hash(base), changes.tree_hash(head), paths.contract_hash(task)

    def end(state: str, step: str, reason: str, integrity_violation: bool = False) -> dict:
        tier = contract["risk_tier"]
        return {
            "key": key(base_tree, head_tree, contract_sha),
            "task": task, "contract_sha256": contract_sha, "base_tree": base_tree, "head_tree": head_tree,
            "verdict": state, "step": step, "reason": reason, "integrity_violation": integrity_violation,
            "risk_tier": tier,
            "routed": {"passed": ROUTES[tier], "failed": "author", "error": "requeue"}[state],
            "evidence": [{k: v for k, v in e.items() if k != "cases"} for e in evidence],
            "seconds": round(time.monotonic() - started, 3),
        }

    def static(name: str, reason: str | None) -> bool:
        evidence.append({"check": name, "status": "failed" if reason else "passed",
                         "reason": reason or "nothing found", "duration_s": 0.0})
        return reason is None

    def ran(make) -> dict:
        """Run a check in a container. A check that broke is tried once more (the failure ladder)."""
        item = make()
        if item["status"] == "error":
            item = {**make(), "retried": True}
        evidence.append(item)
        return item

    # 1. The verdict process failed: reached from any step below, through `error`.
    # 2. The contract or a protected path was altered.
    if not static("integrity", why := integrity(base, head, change)):
        return end("failed", "integrity", why, integrity_violation=True)

    # 3. Budget or time exceeded.
    over = None
    if meta.get("stop_reason") == "limit":
        over = "the author stopped at a limit before finishing"
    elif meta.get("cost_usd", 0) > budget["max_cost_usd"]:
        over = f"cost {meta['cost_usd']:.2f} USD is over the budget of {budget['max_cost_usd']:.2f}"
    elif meta.get("seconds", 0) > budget["max_seconds"]:
        over = f"{meta['seconds']:.0f} seconds is over the budget of {budget['max_seconds']}"
    if not static("budget", over):
        return end("failed", "budget", over)

    # 4. The build fails.
    item = ran(lambda: build(head, head_tree, want["build"]["packages"], out / "build"))
    if item["status"] != "passed":
        return end(item["status"], "build", item["reason"])

    # 5. A required test fails, visible or hidden.
    repo_ids: set[str] = set()
    for target in want["repo_tests"]:
        name = f"repo-tests:{target['path']}"
        item = ran(lambda: checks.pytest_check(
            name, [(head, "/work", "ro"), (base / target["path"], f"/checks/{target['path']}", "ro")],
            f"/checks/{target['path']}", out / name.replace(":", "-"), target["tests"], ENV))
        if item["status"] != "passed":
            return end(item["status"], name, item["reason"])
        repo_ids |= set(item["cases"])
    author = None
    if (head / "tests").is_dir():
        author = ran(lambda: checks.pytest_check(
            "author-tests", [(head, "/work", "ro"), (head / "tests", "/checks/tests", "ro")],
            "/checks/tests", out / "author-tests", None, ENV, skips_are="failed"))
        if author["status"] != "passed":
            return end(author["status"], "author-tests", author["reason"])
    hidden = ran(lambda: checks.pytest_check(
        "hidden-tests", [(head, "/work", "ro"), (paths.PROTECTED / task / "hidden", "/checks", "ro")],
        "/checks/test_hidden.py", out / "hidden-tests", want["hidden_tests"], ENV))
    if hidden["status"] != "passed":
        return end(hidden["status"], "hidden-tests", hidden["reason"])

    # 6. The change left its scope.
    if not static("scope", why := scope(contract, change)):
        return end("failed", "scope", why)

    # 7. The author's own new tests pass against the original code.
    if author is not None or want["author_tests_required"]:
        item = ran(lambda: adequacy(base, head, author or {"cases": {}}, repo_ids,
                                    want["author_tests_required"], out / "test-adequacy"))
        if item["status"] != "passed":
            return end(item["status"], "test-adequacy", item["reason"])

    # 8. A new dependency does not exist, or a secret is present.
    if not static("dependency", why := dependencies(head, change)):
        return end("failed", "dependency", why)
    if not static("secrets", why := secrets(base, head, change)):
        return end("failed", "secrets", why)

    # 9. Otherwise.
    return end("passed", "all", "every required check passed")


def feedback(v: dict) -> str:
    """What the author is told when its change is not accepted: the first
    reason, as a pipeline would show it. Nothing about the hidden checks
    beyond the fact that one did not pass."""
    if v["step"] == "hidden-tests":
        return "A hidden acceptance check did not pass. The change does not yet do everything the task asks."
    return f"Check `{v['step']}` did not pass: {v['reason']}"


def markdown(v: dict) -> str:
    rows = "\n".join(f"| {e['check']} | {e['status']} | {e['reason']} | {e.get('duration_s', 0):.1f} |" for e in v["evidence"])
    return (f"# Verdict: {v['verdict']}\n\n"
            f"| | |\n|---|---|\n| Task | `{v['task']}` |\n| Reason | {v['reason']} |\n| Decided at | {v['step']} |\n"
            f"| Integrity violation | {'yes' if v['integrity_violation'] else 'no'} |\n"
            f"| Risk tier | {v['risk_tier']} |\n| Routed to | {v['routed']} |\n"
            f"| Contract | `{v['contract_sha256'][:16]}` |\n| Base | `{v['base_tree'][:16]}` |\n| Head | `{v['head_tree'][:16]}` |\n\n"
            f"## Evidence\n\n| Check | Result | Reason | Seconds |\n|---|---|---|---|\n{rows}\n")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--task", required=True)
    p.add_argument("--base", type=Path, required=True)
    p.add_argument("--head", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    v = decide(a.task, a.base, a.head, {}, a.out)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "verdict.json").write_text(json.dumps(v, indent=2) + "\n")
    (a.out / "verdict.md").write_text(markdown(v))
    print(f"{v['verdict']}: {v['reason']}")
    return {"passed": 0, "failed": 1, "error": 2}[v["verdict"]]      # one status for the pipeline


if __name__ == "__main__":
    sys.exit(main())
