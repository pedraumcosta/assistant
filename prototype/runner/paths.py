"""Where things are, and how a task's base is assembled."""
from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "fixture"
TASKS = ROOT / "tasks"
PROTECTED = ROOT / "protected"      # stands in for the protected branch
GROUNDTRUTH = ROOT / "groundtruth"  # seen by neither the agent nor the gate
CHANGES = ROOT / "changes"
SCAFFOLD = ROOT / "scaffold"
RUNS = ROOT / "runs"

# Never part of a change: caches the tools leave behind.
JUNK = shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc")


def task_ids() -> list[str]:
    return sorted(p.name for p in TASKS.iterdir() if (p / "task.md").is_file())


def task_text(task: str) -> str:
    return (TASKS / task / "task.md").read_text().strip()


def contract(task: str) -> dict:
    return yaml.safe_load((PROTECTED / task / "contract.yaml").read_text())


def contract_hash(task: str) -> str:
    return hashlib.sha256((PROTECTED / task / "contract.yaml").read_bytes()).hexdigest()


def build_base(task: str, dest: Path) -> Path:
    """The repository as the task finds it: the fixture plus the task's overlay."""
    shutil.copytree(FIXTURE, dest, ignore=JUNK)
    overlay = TASKS / task / "overlay"
    if overlay.is_dir():
        shutil.copytree(overlay, dest, dirs_exist_ok=True, ignore=JUNK)
    return dest


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
