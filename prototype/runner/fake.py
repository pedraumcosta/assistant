"""A model that costs nothing: it replays a change written in advance.

It speaks the listing's Model protocol, so a dry run exercises the real
loop, the real tools in the real container, and everything after them.
"""
from __future__ import annotations

import json

from prototype.runner.paths import CHANGES

VARIANTS = ("good", "bad", "unsafe")


def variants(task: str) -> list[str]:
    return [v for v in VARIANTS if (CHANGES / task / v).is_dir()]


class FakeModel:
    def __init__(self, task: str, variant: str):
        self.label = f"fake:{variant}"
        self.turn = 0
        self.crash_on = 2 if variant == "crash" else None
        self.steps: list[tuple[str, dict]] = []
        if variant == "crash":
            self.steps = [("read_file", {"path": "README.md"}), ("read_file", {"path": "AGENTS.md"})]
            return
        root = CHANGES / task / variant
        files = sorted(p for p in root.rglob("*") if p.is_file() and p.name != "_script.json")
        script = json.loads((root / "_script.json").read_text()) if (root / "_script.json").is_file() else {}
        self.steps += [("bash", {"cmd": cmd}) for cmd in script.get("bash", [])]
        parents = sorted({p.parent.relative_to(root).as_posix() for p in files} - {"."})
        if parents:
            self.steps.append(("bash", {"cmd": "mkdir -p " + " ".join(parents)}))
        self.steps += [("write_file", {"path": p.relative_to(root).as_posix(), "content": p.read_text()}) for p in files]
        self.steps.append(("bash", {"cmd": "python -m pytest -q 2>&1 | tail -3"}))

    async def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        self.turn += 1
        if self.crash_on == self.turn:
            raise ConnectionError("fake provider failure")
        usage = {"input_tokens": 0, "output_tokens": 0}
        if self.turn <= len(self.steps):
            name, args = self.steps[self.turn - 1]
            return {"role": "assistant", "content": "", "cost": 0.0, "usage": usage,
                    "tool_calls": [{"id": f"fake-{self.turn}", "name": name, "args": args}]}
        return {"role": "assistant", "content": "The change is made.\nCLAIM: done", "cost": 0.0, "usage": usage}
