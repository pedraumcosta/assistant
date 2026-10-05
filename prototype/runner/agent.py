"""Runs the published scaffold, unedited, with its tools inside a container.

listing.py is imported as published. Three things are placed around it
(JOURNAL ADR-021): its tool table and its context discovery are pointed at
the container, where the same unedited functions run; the model is wrapped
so that every response is logged; and its limit signal is read correctly.

The loop stays on the host because the model call needs the network and
the tools must not have it. One run per process: the listing keeps its
tool table in a module global.
"""
from __future__ import annotations

import asyncio
import time

from prototype.runner.events import EventLog
from prototype.runner.sandbox import AgentBox
from prototype.scaffold import listing

TOOL_NAMES = tuple(listing.TOOLS)   # bash, read_file, write_file, search_replace
LOG_CHARS = 4000


class ContainerFailed(BaseException):
    """The container failed, not the tool. A BaseException on purpose: the
    listing turns every Exception from a tool into text for the model, and a
    broken container must stop the run instead of becoming a tool result."""


class LoggedModel:
    def __init__(self, inner, log: EventLog):
        self.inner, self.log = inner, log

    async def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        start = time.monotonic()
        response = await self.inner.complete(messages, tools)
        self.log.emit("model_response", latency_s=round(time.monotonic() - start, 3),
                      content=response.get("content", ""), tool_calls=response.get("tool_calls") or [],
                      usage=response.get("usage"), cost_usd=response.get("cost", 0.0))
        return response


def _in_container(box: AgentBox, log: EventLog, name: str):
    def tool(**args):
        log.emit("tool_call", tool=name, args=args)
        start = time.monotonic()
        try:
            reply = box.call({"op": "tool", "name": name, "args": args})
        except Exception as e:
            log.emit("tool_result", tool=name, ok=False, container_failed=str(e))
            raise ContainerFailed(str(e)) from None
        took = round(time.monotonic() - start, 3)
        if reply["ok"]:
            out = reply["out"]
            log.emit("tool_result", tool=name, ok=True, duration_s=took, chars=len(str(out)), out=str(out)[:LOG_CHARS])
            return out
        log.emit("tool_result", tool=name, ok=False, duration_s=took, error=f"{reply['type']}: {reply['msg']}"[:LOG_CHARS])
        # Raised again under its own name, so the listing reports it to the
        # model exactly as it would have on the host.
        raise type(reply["type"], (Exception,), {})(reply["msg"])
    return tool


def run_agent(model, prompt: str, box: AgentBox, log: EventLog, max_turns: int, max_cost: float) -> dict:
    """One session of the scaffold. Returns how it ended; never raises for the agent's own doing."""
    listing.TOOLS = {name: _in_container(box, log, name) for name in TOOL_NAMES}

    def context(*_args, **_kwargs) -> str:
        reply = box.call({"op": "context"})
        if not reply["ok"]:
            raise ContainerFailed(f"context discovery: {reply}")
        return reply["out"]
    listing.discover_context = context

    agent = listing.Agent(model=LoggedModel(model, log), max_turns=max_turns, max_cost=max_cost)
    end = {"stop_reason": "returned", "final_text": "", "detail": None}
    try:
        end["final_text"] = asyncio.run(agent.run(prompt)) or ""
    except RuntimeError as e:
        # The listing signals a limit with StopIteration, which a coroutine
        # cannot raise: Python hands us this RuntimeError instead.
        if isinstance(e.__cause__, StopIteration):
            end.update(stop_reason="limit", detail=str(e.__cause__))
        else:
            end.update(stop_reason="provider_error", detail=f"{type(e).__name__}: {e}")
    except ContainerFailed as e:
        end.update(stop_reason="container_error", detail=str(e))
    except Exception as e:
        end.update(stop_reason="provider_error", detail=f"{type(e).__name__}: {e}")
    end.update(turns=agent.n_turns, cost_usd=agent.cost)
    log.emit("agent_stopped", **{k: v for k, v in end.items() if k != "final_text"},
             final_text=end["final_text"][:LOG_CHARS])
    return end
