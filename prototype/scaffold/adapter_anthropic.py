"""The Anthropic adapter for the listing's `Model` protocol.

The listing cannot call a real model as published (ADR-021): its tool
schemas carry a name only, and its message format is its own. This adapter
supplies the two things that are missing and nothing else:

- a parameter schema for each of the four tools, read off the signatures
  of the listing's own functions. The description stays what the listing
  sends, which is the tool's name;
- the translation between the listing's messages and the Messages API.

It also fills the `cost` field the listing's cost cap reads, from the
provider's token counts and the published price (prices.py).
"""
from __future__ import annotations

import json

import anthropic

from prototype.runner.prices import cost_usd, worst_case_usd

MAX_OUTPUT_TOKENS = 8192

_STR, _INT = {"type": "string"}, {"type": "integer"}
SCHEMAS = {   # the signatures of tool_bash, tool_read_file, tool_write_file, tool_search_replace
    "bash": {"type": "object", "properties": {"cmd": _STR}, "required": ["cmd"]},
    "read_file": {"type": "object", "properties": {"path": _STR, "offset": _INT, "limit": _INT}, "required": ["path"]},
    "write_file": {"type": "object", "properties": {"path": _STR, "content": _STR}, "required": ["path", "content"]},
    "search_replace": {"type": "object", "properties": {"path": _STR, "search": _STR, "replace": _STR},
                       "required": ["path", "search", "replace"]},
}


class BudgetStop(Exception):
    """The next call could take the run past its budget, so it is not made."""


def to_api(messages: list[dict]) -> tuple[str, list[dict]]:
    """The listing's messages as (system, messages) for the Messages API."""
    system, out = "", []
    for m in messages:
        role = m["role"]
        if role == "system":
            system = m["content"]
        elif role == "tool":
            block = {"type": "tool_result", "tool_use_id": m["tool_call_id"], "content": m["content"] or "(no output)"}
            if out and out[-1]["role"] == "user" and isinstance(out[-1]["content"], list):
                out[-1]["content"].append(block)     # results of one turn travel together
            else:
                out.append({"role": "user", "content": [block]})
        elif role == "assistant":
            # What the model sent is returned to it as it was sent.
            out.append({"role": "assistant", "content": m.get("_blocks") or m.get("content") or "(no text)"})
        else:
            out.append({"role": "user", "content": m["content"]})
    return system, out


def _block(b) -> dict:
    if b.type == "text":
        return {"type": "text", "text": b.text}
    if b.type == "tool_use":
        return {"type": "tool_use", "id": b.id, "name": b.name, "input": b.input}
    if b.type == "thinking":
        return {"type": "thinking", "thinking": b.thinking, "signature": b.signature}
    if b.type == "redacted_thinking":
        return {"type": "redacted_thinking", "data": b.data}
    return b.model_dump(exclude_none=True)


class AnthropicModel:
    def __init__(self, model: str, budget_usd: float, api_key: str | None = None):
        self.model = model
        self.label = model
        self.budget = budget_usd
        self.spent = 0.0
        self.client = anthropic.AsyncAnthropic(api_key=api_key, max_retries=3, timeout=300)

    async def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        system, api_messages = to_api(messages)
        # The listing passes no tools when it asks for a summary; the API
        # needs them whenever the history contains tool calls, so they are
        # always declared.
        api_tools = [{"name": name, "description": name, "input_schema": schema} for name, schema in SCHEMAS.items()]
        chars = len(system) + len(json.dumps(api_messages)) + len(json.dumps(api_tools))
        ahead = worst_case_usd(self.model, chars, MAX_OUTPUT_TOKENS)
        if self.spent + ahead > self.budget:
            raise BudgetStop(f"budget: {self.spent:.4f} USD spent, the next call could cost {ahead:.4f}, "
                             f"limit {self.budget:.2f}")
        r = await self.client.messages.create(model=self.model, max_tokens=MAX_OUTPUT_TOKENS, system=system,
                                              messages=api_messages, tools=api_tools)
        usage = {k: getattr(r.usage, k, 0) or 0 for k in
                 ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}
        cost = cost_usd(self.model, usage)
        self.spent += cost
        return {
            "role": "assistant",
            "content": "".join(b.text for b in r.content if b.type == "text"),
            "tool_calls": [{"id": b.id, "name": b.name, "args": b.input} for b in r.content if b.type == "tool_use"],
            "cost": cost,
            "usage": usage,
            "_blocks": [_block(b) for b in r.content],
            "_meta": {"id": r.id, "model": r.model, "stop_reason": r.stop_reason},
        }
