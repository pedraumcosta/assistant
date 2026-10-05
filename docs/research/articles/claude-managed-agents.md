# Claude Managed Agents: Stop Building Your Own Agent Loop

| | |
|---|---|
| Publisher | Towards AI |
| Source | https://pub.towardsai.net/claude-managed-agents-stop-building-your-own-agent-loop-anthropic-already-built-it-06525f23c04c |
| Research date | 2026-10-03 |
| Method | First pass only: fetched through a tool that returns a small model's summary of the page, not the raw text. Reported as full coverage, but not read first-hand. |
| Status | Lowest-confidence digest in this folder. Patterns only; no figure may be used. |
| Used for | PLAN §3.4, DESIGN |

## Digest

**Thesis:** Stop writing your own loop, sandbox, persistence and retry logic; Anthropic hosts the harness.

**Components described:**
- **Primitives:** agent (a versioned definition of model, system prompt, tools, MCP servers, skills), environment (sandbox), session (a running instance with persistent filesystem and history), and events (bidirectional messaging).
- **Toolset:** the prebuilt `agent_toolset_20260401` provides bash, file read/write/edit, glob, grep, web search and web fetch.
- **Async pattern:** one webhook triggers a session and returns; a second fires on completion.
- **Credentials:** vaults (`static_bearer`, `mcp_oauth`) keep secrets out of agent definitions and allow rotation.
- **Multi-agent:** a coordinator delegates to pre-created sub-agents in isolated session threads. Depth is one level, and all agents share one container filesystem. Thread events surface on the primary thread for observability.
- **Human-in-the-loop:** confirmation requests for sensitive tool calls; custom tools executed by the application.
- **Context:** oversized tool outputs spill to the filesystem, and the model gets a truncated preview plus a path.
- **Deployment:** a deploy script creates agents and environments once and saves IDs to a manifest; a run script starts per-task sessions.
- **Alternative:** the Claude Agent SDK runs the same loop locally, for private networks or local filesystems.

**Reusable:** the agent/environment/session/event data model, spill-to-file for large outputs, the vault pattern, the confirmation event, and deploy/run separation. It is also the build-versus-buy option for the prototype.

## Figures quoted by the article

Author's claims, relayed through a summarising model. Unverified.

- Pricing (dated May 2026 by the author), input/output per million tokens: Opus 4.7 "$5.00"/"$25.00"; Sonnet 4.6 "$3.00"/"$15.00"; Haiku 4.5 "$1.00"/"$5.00".
- Opus 4.7 tokenizer "up to roughly 35% more tokens for the same input text".
- "$0.08 per session-hour"; "roughly $58 per month" for 24/7.
- "$10 per 1,000 searches".
- "300 requests per minute" on create, "600 requests per minute" on read.
- "a one-hour coding session on an Opus model consuming 50,000 input tokens and 15,000 output tokens costs about $0.705 total, of which the session runtime accounts for $0.08".
- Caching "up to 90% on cache hits"; batch "up to 50% savings".
- Up to 20 unique agents per coordinator; "up to 20 skills total"; one level of delegation depth.
- Tool outputs over 100K tokens spill to file.
- Slack bot is "maybe forty lines of real code".

## Cautions

Pricing, model names and limits are the author's time-stamped claims (dated May 2026 by the author) and must be checked against current vendor documentation before any use. This article argues the opposite of our decision D3: use a hosted loop instead of writing one. It is recorded in the plan as the rejected alternative for the prototype's inner loop.
