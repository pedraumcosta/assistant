# The Complete Claude Architect Study Guide

| | |
|---|---|
| Publisher | Data Science Collective (Medium) |
| Source | https://medium.com/data-science-collective/the-complete-claude-architect-study-guide-with-code-and-tutor-prompts-01f524e95c92 |
| Research date | 2026-10-03 |
| Method | First pass only: fetched through a tool that returns a small model's summary of the page, not the raw text. Reported as full coverage, but not read first-hand. |
| Status | Lowest-confidence digest in this folder. Patterns only; no figure may be used. |
| Used for | PLAN §3.4, DESIGN |

## Digest

**Thesis:** A synthesis of the Claude Certified Architect exam guide. Prefer deterministic enforcement over probabilistic prompting when stakes are high, and fix root causes.

**Components described:**
- **Agent loop:** terminate on `stop_reason`, not on text content. Anti-patterns are natural-language "done" detection, arbitrary iteration caps, and treating any text block as completion.
- **Orchestration:** hub-and-spoke coordinator with sub-agents that share no memory; the coordinator must pass context explicitly.
- **Hooks:** PreToolUse hooks block deterministically (the example is a refund threshold); PostToolUse hooks normalise or log.
- **Tool design:** descriptions are the primary selection mechanism, so they should state purpose, inputs, examples, edge cases and boundaries. Keep each agent's tool set small. `tool_choice` can be auto, any, or a forced tool.
- **Errors:** four structured categories (transient, validation, business, permission). Distinguish access failure from a valid empty result. Propagate failure type, attempted action, partial results and alternatives; do not suppress silently or kill the workflow.
- **Configuration:** CLAUDE.md at user, project and directory level; `.claude/rules/` with glob patterns; project versus user `.mcp.json`; commands and skills with `context: fork` and `allowed-tools`.
- **Planning:** plan mode for multi-file or architectural work, direct execution for clear scope.
- **Prompting:** explicit criteria with examples beat "be conservative"; 2-4 few-shot examples; schemas with nullable fields and "unclear"/"other" enums to prevent fabrication.
- **Context:** progressive summarisation loses precision, so keep a never-summarised "case facts" block; put key material at the start to counter lost-in-the-middle.
- **Escalation:** valid triggers are an explicit human request, a policy exception, or repeated failure. Sentiment and model confidence are unreliable triggers.
- **Provenance:** carry claim-to-source mappings through synthesis.

**Reusable:** nearly all of it. The `stop_reason` loop, the error taxonomy, PreToolUse gates and the pinned-facts block are the cheapest to adopt.

## Figures quoted by the article

Author's claims, relayed through a summarising model. Unverified.

- Exam domain weights: 27%, 18%, 20%, 20%, 15%. Pass mark "720/1000".
- "Giving an agent 18 tools degrades selection reliability"; "4–5 tools per agent".
- Few-shot: 2-4 examples.
- Refund gate example: $500.
- Batch API: "50% cost savings", "up to a 24-hour processing window".
- Rules across "50+ directories".

## Cautions

A synthesis of a certification exam guide, not a study of running systems. It calls arbitrary iteration caps and model confidence scores unreliable, which is in tension with other articles that rely on both.
