"""The OpenAI adapter for the listing's `Model` protocol — the evaluator's side.

The same two gaps the Anthropic adapter fills (ADR-021), filled for the
Chat Completions API: parameter schemas for the four tools, read off the
listing's own function signatures, and the translation between the
listing's messages and the API's. Costs come from the provider's token
counts and the published price (prices.py, E-87); a call that could take
the run past its budget is not made.
"""
from __future__ import annotations

import json

import openai

from prototype.runner.prices import cost_usd, worst_case_usd
from prototype.scaffold.adapter_anthropic import SCHEMAS, BudgetStop

MAX_OUTPUT_TOKENS = 8192


def to_api(messages: list[dict]) -> list[dict]:
    """The listing's messages as Chat Completions messages."""
    out = []
    for m in messages:
        role = m["role"]
        if role == "tool":
            out.append({"role": "tool", "tool_call_id": m["tool_call_id"], "content": m["content"] or "(no output)"})
        elif role == "assistant":
            entry: dict = {"role": "assistant", "content": m.get("content") or None}
            calls = m.get("tool_calls") or []
            if calls:
                entry["tool_calls"] = [{"id": c["id"], "type": "function",
                                        "function": {"name": c["name"], "arguments": json.dumps(c["args"])}}
                                       for c in calls]
            out.append(entry)
        else:   # system, user
            out.append({"role": role, "content": m["content"]})
    return out


class OpenAIModel:
    def __init__(self, model: str, budget_usd: float, api_key: str | None = None):
        self.model = model
        self.label = model
        self.budget = budget_usd
        self.spent = 0.0
        self.client = openai.AsyncOpenAI(api_key=api_key, max_retries=3, timeout=300)

    async def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        api_messages = to_api(messages)
        api_tools = [{"type": "function", "function": {"name": name, "description": name, "parameters": schema}}
                     for name, schema in SCHEMAS.items()]
        chars = len(json.dumps(api_messages)) + len(json.dumps(api_tools))
        ahead = worst_case_usd(self.model, chars, MAX_OUTPUT_TOKENS)
        if self.spent + ahead > self.budget:
            raise BudgetStop(f"budget: {self.spent:.4f} USD spent, the next call could cost {ahead:.4f}, "
                             f"limit {self.budget:.2f}")
        r = await self.client.chat.completions.create(model=self.model, max_completion_tokens=MAX_OUTPUT_TOKENS,
                                                      messages=api_messages, tools=api_tools)
        choice = r.choices[0]
        u = r.usage
        cached = getattr(getattr(u, "prompt_tokens_details", None), "cached_tokens", 0) or 0
        usage = {"input_tokens": (u.prompt_tokens or 0) - cached, "output_tokens": u.completion_tokens or 0,
                 "cache_creation_input_tokens": 0, "cache_read_input_tokens": cached}
        cost = cost_usd(self.model, usage)
        self.spent += cost
        calls = []
        for c in (choice.message.tool_calls or []):
            try:
                args = json.loads(c.function.arguments)
            except json.JSONDecodeError:
                args = {"cmd": c.function.arguments} if c.function.name == "bash" else {}
            calls.append({"id": c.id, "name": c.function.name, "args": args})
        return {
            "role": "assistant",
            "content": choice.message.content or "",
            "tool_calls": calls,
            "cost": cost,
            "usage": usage,
            "_meta": {"id": r.id, "model": r.model, "stop_reason": choice.finish_reason},
        }
