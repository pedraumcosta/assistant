from __future__ import annotations
import asyncio, json, pathlib, subprocess
from dataclasses import dataclass, field
from typing import Any, Protocol

# ---- Provider abstraction (Recommendation 2): provider-first fallback ---------
class Model(Protocol):
    async def complete(self, messages: list[dict], tools: list[dict]) -> dict: ...

# ---- Tools (Recommendation 3): bash + 3 file tools --------------------------
def _truncate(s: str, n: int = 25_000) -> str: return s if len(s) <= n else s[:n] + "\n...[truncated]"

def tool_bash(cmd: str) -> str:
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
    return _truncate(f"exit={r.returncode}\nstdout:\n{r.stdout}\nstderr:\n{r.stderr}")

def tool_read_file(path: str, offset: int = 0, limit: int = 2000) -> str:
    lines = pathlib.Path(path).read_text().splitlines()
    return _truncate("\n".join(f"{i+1:4}: {ln}" for i, ln in enumerate(lines[offset:offset+limit])))

def tool_write_file(path: str, content: str) -> str:
    pathlib.Path(path).write_text(content); return f"wrote {len(content)} bytes"

def tool_search_replace(path: str, search: str, replace: str) -> str:
    p = pathlib.Path(path); text = p.read_text()
    if text.count(search) != 1: return f"ERROR: search string occurs {text.count(search)}x; must be unique"
    p.write_text(text.replace(search, replace, 1)); return "OK"

TOOLS = {"bash": tool_bash, "read_file": tool_read_file,
         "write_file": tool_write_file, "search_replace": tool_search_replace}

# ---- Hierarchical Markdown context (Recommendation 6) ----------------------
def discover_context(cwd: pathlib.Path = pathlib.Path.cwd()) -> str:
    parts = []
    for p in reversed([cwd, *cwd.parents]):                    # root-to-leaf
        md = p / "AGENTS.md"
        if md.exists(): parts.append(f"<ctx path='{md}'>\n{md.read_text()}\n</ctx>")
    return "\n".join(parts)

# ---- Middleware pipeline (Recommendation 1) ---------------------------------
@dataclass
class Agent:
    model: Model
    messages: list = field(default_factory=list)
    n_turns: int = 0
    cost: float = 0.0
    max_turns: int = 50
    max_cost: float = 5.00
    compact_at_tokens: int = 120_000

    def _token_estimate(self) -> int:
        return sum(len(json.dumps(m)) for m in self.messages) // 4

    async def _check_limits(self):
        if self.n_turns >= self.max_turns: raise StopIteration(f"max_turns={self.max_turns}")
        if self.cost >= self.max_cost: raise StopIteration(f"max_cost=${self.max_cost:.2f}")

    async def _maybe_compact(self):                              # Recommendation 7
        if self._token_estimate() < self.compact_at_tokens: return
        summary = await self.model.complete(
            self.messages + [{"role": "user",
                "content": "Summarize the conversation. Preserve decisions and unresolved issues."}], tools=[])
        # Preserve system + last 30% of turns verbatim, drop the middle (Gemini pattern)
        keep = max(4, int(len(self.messages) * 0.30))
        self.messages = [self.messages[0], {"role":"assistant","content": summary["content"]}] + self.messages[-keep:]

    async def run(self, task: str) -> str:
        self.messages = [
            {"role": "system", "content": f"You are a SWE agent.\n\n{discover_context()}"},
            {"role": "user", "content": task},
        ]
        tool_schemas = [{"name": n, "description": f.__doc__ or n} for n, f in TOOLS.items()]
        while True:
            await self._check_limits(); await self._maybe_compact()
            resp = await self.model.complete(self.messages, tools=tool_schemas)
            self.n_turns += 1; self.cost += resp.get("cost", 0.0)
            self.messages.append(resp)
            if not resp.get("tool_calls"): return resp.get("content", "")
            for call in resp["tool_calls"]:                      # serial execution
                try: out = TOOLS[call["name"]](**call["args"])
                except Exception as e: out = f"ERROR: {type(e).__name__}: {e}"
                self.messages.append({"role": "tool", "tool_call_id": call["id"], "content": _truncate(str(out))})
