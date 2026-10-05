"""What changed between the base and the working copy.

Computed on the host by reading files only. Nothing the agent left behind
is executed here, and symbolic links are recorded, never followed.
"""
from __future__ import annotations

import difflib
import hashlib
import shutil
from pathlib import Path

from prototype.runner.paths import JUNK

_SKIP_DIRS = {"__pycache__", ".pytest_cache"}


def tree(root: Path) -> dict[str, str]:
    """Every file under root, as relative path -> content hash."""
    out = {}
    root = Path(root)
    stack = [root]
    while stack:
        for p in sorted(stack.pop().iterdir()):
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                out[rel] = "symlink:" + str(p.readlink())
            elif p.is_dir():
                if p.name not in _SKIP_DIRS:
                    stack.append(p)
            elif not p.name.endswith(".pyc"):
                out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for rel, digest in sorted(tree(root).items()):
        h.update(f"{rel}\0{digest}\n".encode())
    return h.hexdigest()


def compute(base: Path, work: Path) -> dict[str, list[str]]:
    a, b = tree(base), tree(work)
    return {
        "added": sorted(set(b) - set(a)),
        "modified": sorted(p for p in set(a) & set(b) if a[p] != b[p]),
        "deleted": sorted(set(a) - set(b)),
    }


def _lines(path: Path) -> list[str]:
    if path.is_symlink() or not path.is_file():
        return []
    try:
        return path.read_text().splitlines(keepends=True)
    except UnicodeDecodeError:
        return ["<binary>\n"]


def unified(base: Path, work: Path, change: dict[str, list[str]]) -> str:
    out = []
    for rel in sorted(change["added"] + change["modified"] + change["deleted"]):
        out += difflib.unified_diff(_lines(Path(base) / rel), _lines(Path(work) / rel), f"a/{rel}", f"b/{rel}")
    return "".join(line if line.endswith("\n") else line + "\n" for line in out)


def snapshot(work: Path, dest: Path) -> Path:
    """A copy of the working copy as the change left it, for the checks to read."""
    shutil.copytree(work, dest, symlinks=True, ignore=JUNK)
    return dest
