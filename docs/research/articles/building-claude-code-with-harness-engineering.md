# Building Claude Code with Harness Engineering

| | |
|---|---|
| Author | Fareed Khan |
| Published | 2026-04-06 |
| Source | https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0 |
| Read via | Freedium mirror of the article, downloaded complete on 2026-10-05 |
| Method | Read end to end by a Claude Code sub-agent working from the full downloaded text, with our thesis as the lens. This replaces a first pass on 2026-10-03 that saw only a truncated summary. |
| Status | Digest, not a copy of the article. All figures are the author's claims; none is verified and none may be used as evidence. |
| Used for | PLAN §3.4, DESIGN, prototype design |

## Read confirmation

I read the downloaded full text first-hand, lines 1-9099 (whole file), in seven sequential chunks. The article runs from line 18 to line 9095; the last section, "How to Improve It Further", is lines 9079-9093. Most code listings and transcripts appear two or three times (scrape artefact). No instructions aimed at the reader were found in the text.

## 1. Structure

- **Intro:** revenue claim, "five core components", repo layout (`core.py` plus `s01`-`s23` scripts, `skills/`).
- **What is Harness Engineering?** Four principles: the model is the only decision-maker, tools are the only interface, context is a managed resource, permissions are declarative.
- **How Claude Code Uses Harness Engineering?** Generic loop, tool registry as the only extension point, compaction, pre-execution permissions.
- **Phase 1, Core Agent Loop:** while loop, dispatch map, TodoWrite, sub-agent isolation.
- **Phase 2, Knowledge & Context:** skills, compression, file-based task graph.
- **Phase 3, Async & Multi-Agent:** background tasks, JSONL mailbox teammates, FSM protocol, self-assignment, worktrees.
- **Phase 4, Production Hardening:** streaming, file snapshots/revert, YAML permissions, event bus/hooks, session resume/fork.
- **Phase 5, Async Runtime:** `asyncio.gather` tools, interrupt injection, prompt caching, MCP.
- **Phase 6, Enterprise Upgrades:** Redis mailboxes, worktree lifecycle, all mechanisms combined.
- **How to Improve It Further:** five gaps.

Phase numbering in the prose is off by one throughout (Phase 2 is called "the third phase", and so on).

## 2. Mechanisms as coded

- **Loop:** `agent_loop(messages, dispatch)` is `while True:` → `client.messages.create(..., max_tokens=8000)` → append assistant → `if response.stop_reason != "tool_use": break` → append tool results as a user message. There is no iteration, token or cost cap anywhere.
- **Tool registry:** JSON-schema tool list plus `DISPATCH = {"bash": lambda inp: run_bash(inp["command"]), ...}`. Handlers "accept a dict of inputs, return a string, and never raise exceptions to the loop. Errors are returned as strings, not thrown." `run_read` returns numbered lines capped at `[:50000]`; grep has `timeout=30` and `[:10000]`; bash has `timeout=120` and a substring blocklist `_ALWAYS_BLOCK`.
- **Todo:** `.agent_todo.json`, a list of `{"id","task","status":"pending"}`, with `todo_write/read/update`. The system prompt says "ALWAYS call todo_write first". Status is self-reported by the model.
- **Sub-agent:** `spawn_subagent(prompt) -> str` runs the same loop on a fresh `sub_messages` list and returns only the final text. It is sequential.
- **Skills:** `skills/<name>/SKILL.md` with `name`/`description` front-matter. `discover_skills()` puts one line per skill (`[:100]`) in the system prompt; `load_skill(name)` returns the full body as a tool result.
- **Compaction:** `COMPRESS_THRESHOLD = 40_000 # ~10k tokens estimated` (characters), `KEEP_RECENT = 6`. Older messages are summarised by one LLM call (`text[:20000]`, `max_tokens=2000`). The summary is written to `.agent_memory.md` with `write_text` (overwritten each time) and reloaded at startup. Only text blocks are summarised.
- **Task graph:** `.agent_tasks.json`, tasks `{"id": uuid4().hex[:8], description, status, priority, depends_on, result}`, guarded by `threading.Lock`. `run_task_next()` returns the highest-priority pending task whose dependencies are all `done`. The lock is in-process only, despite the "survives everything" claim.
- **Permissions:** `config/permissions.yaml` with `always_deny`, `always_allow`, `ask_user`, each a list of `{pattern, reason}` regexes. `check_permission(tool_name, input_str, rules) -> tuple[bool, str]` evaluates deny → allow → ask (`input(" Allow? [y/N] ")`), then `# Default: allow if no rule matched`.
- **Hooks:** `EventBus.on(event, handler)` and `emit(event, **payload) -> list`. Events are `session_start`, `pre_tool_use`, `post_tool_use`, `tool_error`, `session_end`. A pre-hook returning `{"block": True}` yields "Blocked by hook". Built-in hooks:
  - a logger appending plain-text lines to `.agent_events.log` (first input value `[:60]`, output length only);
  - a per-tool call counter;
  - a timer flagging calls over 5 seconds.
- **Background tasks:** daemon thread, `timeout=300`, output `[:2000]`, result pushed to a `queue.Queue` and injected as a user message after the turn.
- **Teammates:** `.mailboxes/<name>.jsonl`, lines of `{"from","body"}`. `_receive` reads then truncates the file with no lock; polling is `stop_event.wait(timeout=0.5)`. Each message starts a fresh `sub_messages`, so the "accumulated context" claim is not implemented.
- **FSM protocol:** `AgentState` is IDLE/REQUESTING/WAITING/RESPONDING; `send` refuses while WAITING.
- **Self-assignment:** `claim_next_task(agent_id)` sets `in_progress` and `claimed_by` under the lock. A task becomes `done` when the loop stops, and `failed` only on a Python exception.
- **Worktrees:** `git worktree add -b task/<id> ../.worktree-<id[:8]>`.
  - Only `bash` is redirected, via process-global `os.chdir`; `write`/`read` still go through the normal dispatch.
  - `finally` removes the worktree and runs `branch -D`.
  - `detect_conflicts` intersects `git diff --name-only HEAD <branch>` file sets.
  - `create_worktree_safe` refuses detached HEAD, warns on a dirty tree, and renames the branch on collision.
- **Streaming:** `client.messages.stream` plus `get_final_message()`.
- **Sessions:** `.sessions/<id>.json` holds `{id, created, updated, title, messages}`. `:sessions`, `:resume <id>`, `:fork <id>` (copy with a new id).
- **Parallel tools:** `asyncio.gather(*[_dispatch_one(b) ...])`, with a per-path `asyncio.Lock` for writes.
- **Interrupt:** an `asyncio.Queue` checked before the model call and before tool execution; 30s wait.
- **Caching:** `"cache_control": {"type": "ephemeral"}` on the system block and the last tool. `CacheStats` reads `cache_creation_input_tokens` and `cache_read_input_tokens`, with `saved = int(read * 0.9)`.
- **MCP:** `config/mcp_config.yaml`, stdio only, tools registered as `mcp__<server>__<tool>`, routed by prefix check.
- **Redis mailbox:** `MailboxBackend` with `send`/`receive`/`close`, channel `agent:{name}:inbox`, and an `asyncio.Queue` fallback.

## 3. Verification, evaluation, audit, cost and failure handling

Everything called "verification" is the model choosing to run pytest or mypy inside the loop. Nothing runs after the agent stops.

- Todo: "the model cannot silently skip steps because each step has a status that persists across turns"; "It verified its work."
- Cached system prompt: "Always verify your work. Check outputs before proceeding."
- Review, the only human routing: "the harness compares which files each branch modified and surfaces any overlapping changes for human review before merging"; transcript: "Overlap detected on 1 file - human review required before merging."
- Hooks: "This is how teams add cost tracking, audit logging, custom approval workflows, and integration with external monitoring systems without modifying the agent loop itself." Also: "The event bus makes observability a structural property of the harness rather than something bolted on after the fact."
- Policy: "A pre_tool_use hook that returns {"block": True} can prevent a tool from running — this is how policy enforcement layers cleanly on top of permission governance."
- Permissions: "making safety a structural property rather than a model behavior"; "Security policy lives in configuration, not in code."
- Sessions: "A session that cannot be resumed is a session that cannot be trusted with long tasks."
- Reversibility: "Every write call in Claude Code silently saves the previous file content before overwriting." The snapshot is in memory and one level deep.
- Cost: token counts only, no currency.

Closing section, the five items in full:

- "Parallel Subagent Spawning the current subagent implementation is sequential. Refactoring spawn_subagent to use asyncio.gather would let the lead agent dispatch three explore subagents simultaneously, exactly how Claude Code does it internally, cutting exploration time by the number of parallel agents."
- "Vector Memory Store our long-term memory is a flat markdown file. Replacing it with a lightweight vector store like ChromaDB would let the agent retrieve semantically relevant memories rather than injecting the entire summary every session, keeping context focused as projects grow."
- "Fine-Grained Token Accounting cache stats tracker counts tokens per session but does not break down cost per task or per tool type. Adding a cost ledger that logs spend per operation would let teams identify which tool calls are most expensive and optimise accordingly."
- "Webhook-Based Event Bus event bus fires hooks in-process only. Extending it to forward events to an external HTTP endpoint would enable integration with Slack, Datadog, PagerDuty, or any monitoring system without modifying the agent loop."
- "Evaluation Framework the test suite validates that the harness works correctly but does not measure how well the agent performs on real tasks. Adding an LLM-as-a-judge evaluation layer that scores agent outputs on accuracy, tool efficiency, and plan adherence would turn the repo into a benchmarkable system, not just a working one."

## 4. What the Python prototype should copy

- The loop shape exactly: `while True` → create → append → `stop_reason != "tool_use"` → dispatch → append. Add the iteration and budget cap the article lacks.
- The handler contract `dict -> str`, never raising, with truncated outputs and numbered-line reads.
- `check_permission(tool, input_str, rules) -> (bool, reason)` over YAML tiers in deny → allow → ask order. Invert the default to deny or ask, and log the returned reason.
- `EventBus.on/emit` with the five event names and the `{"block": True}` convention. These names match where a plug-in would attach.
- A JSONL append pattern for the event log, but with structured full payloads. The article's log is lossy text.
- The session JSON shape and fork-by-copy, for replay in evals.
- `CacheStats`-style reading of the `usage` object as the seed of a cost ledger.
- `detect_conflicts`-style `git diff --name-only`, as the basis for a scope check against the change contract.
- A worktree per eval run, with the `write` tool rooted in the worktree (the article does not do this).
- Skip mailboxes, FSM, Redis, self-assignment and compaction for a one-day build.

## 5. Evidence for and against the thesis

**For "the harness is commodity":**
- The author says so directly: "That harness is fully reproducible, and that is exactly what we are going to build."
- Each mechanism is tens of lines; the combined file is "280 lines"; "you can use litellm to swap in any model you like".
- MCP, SKILL.md and hooks are shown as open extension points, which is the plug-in surface the evidence layer needs.

**For "the evidence layer is missing":**
- No acceptance contract, scope, budget, post-stop gate, evidence bundle or risk tier exists anywhere in the article.
- Task completion equals the model stopping.
- The audit log is truncated text; cost is tokens only.
- The author names a cost ledger, external event forwarding and an evaluation framework as the gaps.

**Partial overlaps already present:**
- pre-tool blocking hooks;
- three-tier permission policy as data;
- a file-overlap → human review rule;
- per-session tool-call and cache statistics;
- session persistence.

**Against the thesis:**
- The opening credits the harness, not the model or prompts, for the product's success: "It got there because Anthropic built the right harness around the right model".
- The stated philosophy, "the harness never branches on model output", is the opposite of a deterministic gate.
- The author's proposed evaluation is LLM-as-judge, not deterministic checks.
- Hooks make an evidence layer cheap for harness vendors to add natively, so it is equally reproducible.
- The demo's own flaws (allow-by-default, non-isolated writes, self-reported status) show that "reproducible" here means demo-grade, not production parity.

## 6. Numbers

**Asserted about Claude Code, with no source or measurement:**
- "crossed $1 billion in annualized revenue within six months of launch"
- "Context is actively managed at ~92% window usage" / "approximately 92% context window usage"
- "Claude Code ships with 18 registered tools"
- "spawns three parallel explore subagents"
- "a 92% prompt prefix reuse rate across all internal agent calls"
- "at approximately 10% of the normal token cost"
- "five core components"; "23 Components"

**Constants in the author's code:**
- `max_tokens` 8000 (main), 4000 (teammates), 2000 (summary)
- `COMPRESS_THRESHOLD = 40_000 # ~10k tokens estimated`; `KEEP_RECENT = 6`; `text[:20000]`
- timeouts 120s (bash), 300s (background), 30 (grep); output caps 50,000 / 10,000 / 2000 characters
- polling 0.5 and 1.0; hook timer threshold 5 seconds; interrupt wait 30; mailbox receive timeouts 30.0 and 2.0

**Shown in transcripts the author presents as runs:**
- "44 passed in 2.1s" (repeated), "47 passed in 2.3s", "46 passed in 2.3s (44 original + 2 new ...)"
- "18 messages → 1 summary"; "22 messages → 1 summary"; "(14 msgs)"
- "The subagent ran twenty-five"; "25 files found" / "23 session files" / "(24 files)"
- coverage "71%", "88%", "100%" (124 statements, 42 branches)
- "Total time: 34s vs ~95s sequential"
- "0.4s (vs ~1.2s sequential)"; "0.6s (vs ~2.1s sequential)"; "~1s parallel vs ~3.3s sequential - 3x faster"
- "MISS → 1,847 tokens written"; "saved ~1,662 tokens"; "total saved≈8,310 tokens"; "Cache hit rate: 5/6 calls (83%)"
- "14 built-in + 14 MCP = 28 available"; "s_full.py: 13 tools"
- "8.2s (vs ~9s polling average in Phase 4)"; "23.4s"; "<10ms per message vs ~500ms polling"
- "I created a file is 280 lines"; "77 min read"

No benchmark method is given for any timing, and the transcripts are internally inconsistent (see section 7).

## 7. Speculative or reverse-engineered claims

- The internal names "nO master loop", "compressor wU2" and "h2A async queue"/"h2A steering queue" are attributed to "reverse-engineered Claude Code execution traces", with no citation.
- "It calls TodoWrite. Every time." and "Anthropic observed that ... the model drifts" are unsourced.
- "Claude Code's internal agent coordination uses message passing that is instant, lock-free" is unsourced.
- "Claude Code avoids most of these issues by using file snapshots rather than worktrees" is unsourced.
- The article says the 18-message compaction happened "without paying for 18 turns", but the code's trigger is a character count, not a turn count.

The transcripts look illustrative rather than captured:
- Non-hex task ids such as `g3h4i5j6`.
- Six tests listed as PASSED, followed by "5 passed".
- "[stats] 6 tool calls" over a dict that sums to 5.
- A "45-second test suite" that passes "in 2.1s".
- "Branches preserved for inspection" although the code deletes the branches in `finally`.
- The claim that `read` and `pip freeze` "matched always_allow patterns" when they only fall through to the default allow.
- "The architecture is clean, non-repetitive, and fully tested", which the code shown does not support.
