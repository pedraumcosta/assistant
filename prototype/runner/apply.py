"""Applies a change written in advance to a copy of the repository, on the host.

A change is a directory: the files in it replace or add to the copy, and an
optional `_script.json` may name paths to `delete` and files to `create`.
(Its `bash` entry is for the fake agent, which acts through the shell.)
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

RESERVED = {"_script.json", "meta.json"}


def apply(change_dir: Path, head: Path) -> None:
    script = change_dir / "_script.json"
    todo = json.loads(script.read_text()) if script.is_file() else {}
    for rel in todo.get("delete", []):
        target = head / rel
        shutil.rmtree(target) if target.is_dir() else target.unlink()
    for rel, content in todo.get("create", {}).items():
        (head / rel).parent.mkdir(parents=True, exist_ok=True)
        (head / rel).write_text(content)
    for f in sorted(change_dir.rglob("*")):
        if f.is_file() and f.name not in RESERVED:
            dest = head / f.relative_to(change_dir)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dest)
