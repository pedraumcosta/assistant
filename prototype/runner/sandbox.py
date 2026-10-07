"""Containers. Everything the agent wrote, or runs, stays inside one.

Three uses of one image:
- the agent's tools: only the run's working copy is mounted, read-write;
- the verdict and the ground-truth checks: a snapshot of the change,
  read-only, plus the checks, read-only.
None has a network, and none is given an API key.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
import uuid
from dataclasses import dataclass
from pathlib import Path

from prototype.runner.paths import SCAFFOLD

IMAGE = "assist-proto:1"
# The container runs as the invoking host user, not root. On a native Linux
# daemon, root with every capability dropped cannot write to a bind mount the
# host user owns (no CAP_DAC_OVERRIDE), so verdicts ended as `error`: fail
# closed, but nothing judged (ASSIST-024). Matching the host user makes the
# mounts writable exactly where the host user could write, and nothing runs
# as root at all.
CONFINE = ["--network", "none", "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
           "--pids-limit", "256", "--memory", "1g",
           "--user", f"{os.getuid()}:{os.getgid()}"]


class SandboxError(RuntimeError):
    """The container itself failed. Never a result of the change under test."""


class AgentBox:
    """The container the agent's four tools run in, for the length of one run."""

    def __init__(self, work: Path):
        self.work = Path(work).resolve()
        self.name = f"assist-agent-{uuid.uuid4().hex[:12]}"

    def start(self) -> None:
        r = subprocess.run(
            ["docker", "run", "-d", "--rm", "--name", self.name, *CONFINE,
             "-v", f"{self.work}:/work", "-v", f"{SCAFFOLD}:/opt/scaffold:ro",
             "-w", "/work", IMAGE, "sleep", "infinity"],
            capture_output=True, text=True)
        if r.returncode != 0:
            raise SandboxError(f"could not start the agent container: {r.stderr.strip()}")

    def call(self, request: dict, timeout: int = 150) -> dict:
        """Run one tool request through the unedited listing, inside the container."""
        try:
            r = subprocess.run(
                ["docker", "exec", "-i", "-w", "/work", self.name, "python", "/opt/scaffold/tool_entry.py"],
                input=json.dumps(request), capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            raise SandboxError("the tool call did not return") from None
        try:
            return json.loads(r.stdout)
        except json.JSONDecodeError:
            raise SandboxError(f"the tool entry point gave no reply (exit {r.returncode}): {r.stderr[-500:]}") from None

    def stop(self) -> None:
        subprocess.run(["docker", "rm", "-f", self.name], capture_output=True)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc):
        self.stop()


@dataclass
class Exit:
    code: int | None       # None when the container was killed for running too long
    stdout: str
    stderr: str
    duration_s: float
    timed_out: bool


def run_once(mounts: list[tuple[Path, str, str]], command: list[str], workdir: str,
             env: dict[str, str] | None = None, timeout: int = 180) -> Exit:
    """Run one command in a fresh container. mounts are (host path, container path, ro|rw)."""
    name = f"assist-check-{uuid.uuid4().hex[:12]}"
    args = ["docker", "run", "--rm", "--name", name, *CONFINE, "--tmpfs", "/tmp", "-w", workdir]
    for host, inside, mode in mounts:
        args += ["-v", f"{Path(host).resolve()}:{inside}:{mode}"]
    for key, value in (env or {}).items():
        args += ["-e", f"{key}={value}"]
    start = time.monotonic()
    try:
        r = subprocess.run([*args, IMAGE, *command], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        subprocess.run(["docker", "rm", "-f", name], capture_output=True)
        return Exit(None, str(e.stdout or ""), str(e.stderr or ""), round(time.monotonic() - start, 3), True)
    return Exit(r.returncode, r.stdout, r.stderr, round(time.monotonic() - start, 3), False)
