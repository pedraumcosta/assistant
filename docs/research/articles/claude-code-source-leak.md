# Diving into Claude Code's source code

| | |
|---|---|
| Publisher | Engineer's Codex |
| Source | https://read.engineerscodex.com/p/diving-into-claude-codes-source-code |
| Research date | 2026-10-03 |
| Method | First pass only: fetched through a tool that returns a small model's summary of the page, not the raw text. Reported as full coverage, but not read first-hand. |
| Status | Lowest-confidence digest in this folder. Patterns only; no figure may be used. |
| Used for | PLAN §3.4, DESIGN |

## Digest

**Thesis:** An accidentally published npm sourcemap exposed Claude Code's internals, and the leak shows the product's value lies in harness design decisions that apply to any agent.

**Components described:**
- **Per-turn repo context:** git branch, recent commits and CLAUDE.md are reloaded every turn.
- **Prompt caching:** a `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` splits the system prompt into a stable cached front and a dynamic back. Cache-breaking sections are named `DANGEROUS_uncachedSystemPromptSection` so engineers see the cost.
- **Search tools:** dedicated Grep and Glob tools return structured results instead of shell output; an LSP tool gives definitions, references and call hierarchy.
- **Compaction:** five distinct context-compaction strategies (not enumerated in the digest).
- **Hooks:** an event hook system with 25+ events.
- **Sub-agents:** three execution models (fork, teammate, worktree), made cheap by sharing the cached prefix.
- **Memory:** three layers. An always-loaded index of pointers, topic files loaded on demand, and transcripts that are grep-only. Memory is treated as hints to verify; facts derivable from code are not stored; topic file is written first, then the index. A nightly `autoDream` consolidation runs in a restricted forked sub-agent.
- **Permissions:** commands are classified by a side-query to the model ("is this command safe?"), the "critic" pattern, instead of brittle allowlists.
- **Unshipped or internal:** KAIROS, a heartbeat-driven background agent; "Magic Docs", a single-file-restricted sub-agent that keeps a doc updated; anti-distillation decoy tools; binary attestation in Bun's Zig HTTP layer; an "undercover mode".

**Reusable in a prototype:** the stable/dynamic prompt split, structured grep/glob tools, the index-plus-topic-file memory, the safety side-query, and single-file-scoped sub-agents.

## Figures quoted by the article

Author's claims, relayed through a summarising model. Unverified.

- "600,000 lines" of Claude Code internals.
- "44 hidden feature flags and 20+ unshipped features total".
- "25+ event hook system".
- "spawning 5 agents costs barely more than 1".
- Memory index "~150 characters per line".
- `undercover.ts` is 90 lines.
- Capybara: "1M context".
- claw-code: "75,000+ stars and 75,000+ forks".
- Bypass of anti-distillation "within an hour".
- Incident context: Axios 100M weekly downloads; LiteLLM 97M monthly installs; Railway 2M users, 31% of Fortune 500, 52 minutes; Copilot "1.5M+ pull requests".

## Cautions

The article rests on leaked source. The unshipped or internal features it describes (KAIROS, autoDream, Magic Docs, anti-distillation decoys, attestation, undercover mode, model codenames) may not reflect the product. It names five compaction strategies and 25+ hook events without listing them.
