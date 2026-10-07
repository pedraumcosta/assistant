"""Published prices, in USD per million tokens. No price is assumed:
each entry cites its row in docs/research/EVIDENCE.md."""
from __future__ import annotations

PRICES = {
    # E-86, read on the publisher's page on 2026-10-05
    "claude-sonnet-5-5": {"input": 2.00, "output": 10.00, "cache_write_5m": 2.50, "cache_read": 0.20, "evidence": "E-86"},
    # E-87, read on the publisher's page on 2026-10-07. OpenAI bills cached
    # input at a discount and has no cache-write charge; the adapter maps its
    # usage fields onto the same keys cost_usd reads.
    "gpt-5.1-2025-11-13": {"input": 1.25, "output": 10.00, "cache_write_5m": 0.00, "cache_read": 0.125, "evidence": "E-87"},
}


def cost_usd(model: str, usage: dict) -> float:
    p = PRICES[model]
    return (usage.get("input_tokens", 0) * p["input"]
            + usage.get("output_tokens", 0) * p["output"]
            + usage.get("cache_creation_input_tokens", 0) * p["cache_write_5m"]
            + usage.get("cache_read_input_tokens", 0) * p["cache_read"]) / 1_000_000


def worst_case_usd(model: str, input_chars: int, max_output_tokens: int) -> float:
    """An upper estimate of one call, made before the call: every 2.5
    characters of the request counted as a token, and the whole output
    allowance used."""
    p = PRICES[model]
    return (input_chars / 2.5 * p["input"] + max_output_tokens * p["output"]) / 1_000_000
