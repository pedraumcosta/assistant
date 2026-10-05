# The published scaffold (Listing 3 of the harness paper)

| | |
|---|---|
| Source | Barbaste, Darrigol, Vu and Wiltberger, "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents", arXiv 2609.00006v1, §16.10, Listing 3 (pages 70 and 71) |
| URL | https://arxiv.org/abs/2609.00006v1 |
| Licence | CC BY 4.0, as stated on the arXiv page (https://creativecommons.org/licenses/by/4.0/) |
| Read | 2026-10-05, from the PDF downloaded from arXiv |
| Used for | The agent under test in the prototype (`PLAN.md` D3, `JOURNAL.md` ADR-003) |

## How this copy was made

The listing was extracted from the PDF as text. The PDF typesets code with spaces between characters and wraps long lines; both were undone by hand. Typographic quotation marks on listing line 37 were restored to plain ones. Nothing else was changed: names, defaults, comments and line numbering are the paper's. The listing's own numbering ends at 82; the paper describes it as "∼90 LoC".

The paper's caption: "A minimum viable harness, ∼90 LoC Python. Illustrative scaffold, not production code."

## The listing

```python
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
```

## What the paper says about it

- "It is not a drop-in library; it is a scaffold to be copied and specialized." (E-59)
- "The scaffold above deliberately omits features for which our corpus shows divergence: sandbox (Recommendations 9–10 are deployment-specific), multi-agent (Recommendation 12 defers it), MCP/Skills (Recommendation 14 is extensibility, not core). Start here, measure [17], add the minimum that your observed failure modes demand."
- Observation 13: it "implements 10 of the 18 recommendations directly", with "no framework dependencies, no RAG, no vector store, no multi-agent orchestration, and no sandbox". The claim that it would match Mini-SWE-Agent's benchmark numbers is offered as a conjecture, "without proof".

## What we observed reading it, before running it

These are our own observations. They are the reasons for the departures recorded in `JOURNAL.md` ADR-021.

1. **It cannot call a real model as published.** The tool schemas carry a name and a description only, and no tool function has a docstring, so the description is the name. Both providers we use need a parameter schema for each tool. The `Model` protocol also implies a message format (`role: system`, `role: tool`, `tool_calls` with `args`) that neither provider's API uses directly. An adapter has to supply both.
2. **Cost is whatever the adapter reports.** The loop adds `resp.get("cost", 0.0)`. An adapter that omits the field leaves the cost cap inactive.
3. **The limits do not stop the loop in the way the code reads.** `_check_limits` raises `StopIteration` inside a coroutine. Python turns that into `RuntimeError: coroutine raised StopIteration`, which we confirmed on Python 3.12.9. A caller must treat that error as "limit reached", or a run that hit its cap looks like a crash.
4. **Every tool acts on the process's own directory and machine.** `tool_bash` runs with `shell=True`, with no working directory, no environment filter and no restriction on paths or network. The file tools accept any path, absolute ones included.
5. **Context discovery reads above the repository.** `discover_context` collects `AGENTS.md` from the working directory and every parent up to the filesystem root, and its default argument is fixed when the module is imported.
6. **There is no notion of "done".** The loop returns the first response that has no tool call. Whether that response claims success is free text.
