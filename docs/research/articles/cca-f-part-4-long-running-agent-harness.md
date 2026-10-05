# Foundations of CCA-F Exam Part 4: Engineering the Long-Running Agent Harness: From Amnesia to Persistent Autonomy

| | |
|---|---|
| Author | Rick Hightower (published in Towards AI) |
| Published | 2026-05-05 |
| Source | https://pub.towardsai.net/foundations-of-cca-f-exam-part-4-engineering-the-long-running-agent-harness-from-amnesia-to-fc03bfbb0377 |
| Read on | 2026-10-05, via a Freedium mirror |
| Method | Read end to end by a Claude Code sub-agent from the complete downloaded text, and checked against Pedro's prior notes on the article. |
| Status | Digest of a second-hand, exam-preparation summary of an Anthropic engineering post, which we have not read (ASSIST-013). Same author as the "hour three" article, so the two do not corroborate each other. No measured data. |
| Used for | PLAN §3.6; ROADMAP open question T4 |

## Read record

- **Author and date:** Rick Hightower; May 5, 2026. The publication name "Towards AI" appears only in the URL, not in the file.
- **Read:** the whole file, lines 1-559.
- **Basis:** a second-hand summary of an Anthropic engineering post, mapped to exam domains for certification preparation: "Insights synthesized from Anthropic Engineering (Code RL & Claude Code teams) and the official Claude Certified Architect — Foundations Exam Guide." No original data or account of the author's own build. Diagrams it refers to are absent from the text.

## What the article says

**Thesis.** Long-running agent work fails across context windows because state is lost, not because the model reasons badly: "The model is not the system. The system is everything that persists between sessions: logs, files, commits, and structured summaries."

**Why compaction is insufficient.** "Compaction produces summaries, not specifications. It removes the precise steps, acceptance criteria, and dependencies required for execution." Two failure modes follow: the "One-Shot Trap" and "Premature Victory".

**Shift-worker model.** "The problem is not memory. The problem is the quality of the handoff."

**Dual-agent harness** (same model, different initial prompts).

- Initializer Agent, first session only: builds `init.sh`, `claude-progress.txt`, `feature_list.json` "with 200+ granular features marked passes: false", and an initial Git commit.
- Coding Agent, every later session: one feature at a time, leaving "a clean, merge-ready state".

**Persistent artifacts.** `init.sh` standardises start-up; `claude-progress.txt` is "a chronological shift log"; `feature_list.json` "defines all required work as structured tasks"; Git gives rollback. Puppeteer MCP Server results (browser end-to-end tests) are the third artifact said to "survive every context reset".

**Morning routine.** Orient (`pwd`); review history (`claude-progress.txt` + `git log --oneline -20`); read `feature_list.json`; run `init.sh` and baseline tests; then "Verify → Execute → Commit → Handoff".

**Structural gravity.** "JSON introduces structural constraints that the model is less likely to violate. Unlike free-form text, it enforces consistency and prevents the agent from rewriting or skipping requirements."

**Enforcement and verification.** "Prompt instructions alone have a non-zero failure rate"; "Enforcement belongs in tooling and control flow, not in prose." "Agents frequently hallucinate success." "Self-review is biased (use independent verification)".

**Loop and tools.** Only `stop_reason == "tool_use"` continues the loop; any other value exits.

## Check of Pedro's notes

- **Shift-worker model:** Confirmed.
- **Quote "The model is not the system…":** Confirmed; it continues ": logs, files, commits, and structured summaries."
- **Quote "Compaction produces summaries, not specifications":** Confirmed.
- **Loses acceptance criteria and next actions:** Confirmed. "Compaction preserves the general meaning but not the instructions, acceptance criteria, or next actions."
- **"the problem is the quality of the handoff":** Confirmed.
- **"Structural gravity" (rigid JSON schemas stop agents rewriting their own requirements):** Corrected. The term is present, but the claim is hedged and no mechanism is given: "JSON introduces structural constraints that the model is less likely to violate", and "JSON feature list (rigid structure prevents creative rewriting or premature passes: true)". The text says "rigid structure", not "rigid JSON schemas", and describes no validator, permission or hook protecting the file.
- **4-5 tools max per agent:** Confirmed. "Limit tools per agent (4–5 max)".
- **Loop rule:** Confirmed. "Key Rule: Only "tool_use" continues the loop."
- **"most failures are in loop control":** Corrected for wording. The text has "Most system failures occur in loop control" and "Most failures are not in tools or models. They are in a loop control." It also attributes session-reset failures to "a missing state and a missing verification".

## Figures

All asserted; none measured.

- "Domain 1: Agentic Architecture & Orchestration (27%)"; "Domain 2: Tool Design & MCP Integration (18%)"; "Domain 4: Prompt Engineering & Structured Output (20%)"; "Domain 5: Context Management & Reliability (15%)"; "Domain 3 — Claude Code (20%)".
- "feature_list.json with 200+ granular features marked passes: false".
- "git log --oneline -20".
- "Limit tools per agent (4–5 max)".
- "the five battle-tested LLM patterns".
- "two specialized personae"; "two dominant failure modes".
- "three artifacts that survive every context reset".
- "a non-zero failure rate" (no rate given).
- "16 min read"; "Contents 32" sections; biography "30+ coding agents", "Fortune 100".

## Relevance to our thesis

**Supports**

- The diagnosis matches ours: acceptance criteria do not survive compaction, so the contract must be an external structured artifact re-read every session.
- Premature victory and "hallucination of success" are named as dominant failures; the stated remedy is independent end-to-end verification and programmatic gates, not prompts.
- A per-item pass flag (`passes: false` until verified) is a usable shape for acceptance checks: "Completion must be earned through verification, not assumed."

**Cuts against**

- This is the vendor's own reference pattern (feature list with pass flags, progress log, Puppeteer tests, hooks); buyers may conclude the vendor already covers it.
- The verification is genuine outcome checking (baseline tests, browser end-to-end), but the same agent runs it and flips its own `passes` flag. No independent verifier, budget, evidence bundle or risk routing is described.
- The feature list is generated by an initializer session at project start. The article says nothing about where requirements come from for ordinary changes in an existing repository.

**Take for a prototype**

- Contract as JSON in the repository, with per-check status, read as a fixed first step of each session.
- Do not rely on structural gravity. By the article's own rule ("Instructions are not guarantees"), enforce immutability with a pre-tool hook, a hash checked in CI, or storage outside the agent's writable paths.
- Run verification outside the agent's loop and record blind spots ("browser-native modals may not be visible to automation").

## Cautions

- Second-hand and exam-oriented.
- The source is named inconsistently: "Harnessing Long-Running Agents: Engineering the Multi-Context Architecture" in the body, "Effective Harnesses for Long-Running Agents" in the reading list. Read the Anthropic original before relying on details.
- Promotional footer: speaker booking and the author's skill marketplace.
- Same author as the "hour three" article; agreement between the two is not independent corroboration.
