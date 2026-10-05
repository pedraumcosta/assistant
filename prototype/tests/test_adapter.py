"""The adapter's translation and its budget stop, without calling a model."""
import asyncio
import inspect

import pytest

from prototype.runner import prices
from prototype.scaffold import adapter_anthropic as adapter
from prototype.scaffold import listing


def test_schemas_match_the_listings_own_tool_signatures():
    functions = {"bash": listing.tool_bash, "read_file": listing.tool_read_file,
                 "write_file": listing.tool_write_file, "search_replace": listing.tool_search_replace}
    assert set(adapter.SCHEMAS) == set(functions)
    for name, fn in functions.items():
        params = inspect.signature(fn).parameters
        assert set(adapter.SCHEMAS[name]["properties"]) == set(params)
        required = {p for p, v in params.items() if v.default is inspect.Parameter.empty}
        assert set(adapter.SCHEMAS[name]["required"]) == required


def test_translation_of_a_tool_turn():
    blocks = [{"type": "text", "text": "Looking."},
              {"type": "tool_use", "id": "a", "name": "bash", "input": {"cmd": "ls"}},
              {"type": "tool_use", "id": "b", "name": "read_file", "input": {"path": "x"}}]
    system, messages = adapter.to_api([
        {"role": "system", "content": "You are a SWE agent.\n\n"},
        {"role": "user", "content": "task"},
        {"role": "assistant", "content": "Looking.", "tool_calls": [], "_blocks": blocks},
        {"role": "tool", "tool_call_id": "a", "content": "exit=0"},
        {"role": "tool", "tool_call_id": "b", "content": ""},
        {"role": "assistant", "content": "summary"},
    ])
    assert system == "You are a SWE agent.\n\n"
    assert messages == [
        {"role": "user", "content": "task"},
        {"role": "assistant", "content": blocks},
        {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": "a", "content": "exit=0"},
            {"type": "tool_result", "tool_use_id": "b", "content": "(no output)"}]},
        {"role": "assistant", "content": "summary"},
    ]


def test_cost_from_token_counts_and_the_recorded_price():
    usage = {"input_tokens": 1_000_000, "output_tokens": 100_000, "cache_read_input_tokens": 500_000}
    assert prices.cost_usd("claude-sonnet-5-5", usage) == pytest.approx(2.00 + 1.00 + 0.10)
    assert prices.PRICES["claude-sonnet-5-5"]["evidence"] == "E-86"


def test_a_call_that_could_pass_the_budget_is_not_made():
    model = adapter.AnthropicModel("claude-sonnet-5-5", budget_usd=0.05, api_key="not-a-key")
    # The output allowance alone could cost 0.08 USD, so the call must be refused before any request.
    with pytest.raises(adapter.BudgetStop):
        asyncio.run(model.complete([{"role": "system", "content": ""}, {"role": "user", "content": "x"}], []))
    assert model.spent == 0.0
