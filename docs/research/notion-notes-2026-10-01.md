# Pedro's Notion notes on nine strategy reads, checked against the sources

| | |
|---|---|
| Origin | Pedro's summary of nine articles from his Notion "Machine Learning" database (tag `assistant`), written 2026-10-01 and given to this project on 2026-10-05 |
| What this file is | Each claim in that summary, checked against the source where we could read it |
| Method | Six of the nine sources were located and read in full on 2026-10-05 (one by the main Claude Code session, five by sub-agents). Two had been read earlier through a summarising fetch only. One could not be found. |
| Status | The "Finding" column is what the source text says. Where a claim is marked "not checked", it remains Pedro's note and is not usable as evidence. |
| Used for | PLAN §3.6, ROADMAP §2 |

## Coverage

| # | Source in the notes | Record | How it was read |
|---|---|---|---|
| 1 | Claude Managed Agents (Towards AI) | `articles/claude-managed-agents.md` | Summarising fetch, 2026-10-03 |
| 2 | MinusX, "What makes Claude Code so damn good" | `articles/minusx-decoding-claude-code.md` | Full text |
| 3 | Claude Code source-leak analysis (Engineer's Codex) | `articles/claude-code-source-leak.md` | Summarising fetch, 2026-10-03 |
| 4 | Anthropic harness-engineering playbook (Medium summary) | `articles/anthropic-harness-design-long-running-apps.md` | Full text of Anthropic's primary post, not the Medium summary |
| 5 | Copilot vs "Private AGI" | None | **Not found** (ASSIST-012) |
| 6 | Anthropic, "AI-resistant technical evaluations" | `articles/anthropic-ai-resistant-technical-evaluations.md` | Full text |
| 7 | "Sessions fall apart at hour three" | `articles/claude-code-spec-driven-development-hour-three.md` | Full text |
| 8 | CCA-F Part 4 (long-running harness) | `articles/cca-f-part-4-long-running-agent-harness.md` | Full text |
| 9 | Agent visualization (IAEE) | `articles/real-time-visualization-of-agentic-interactions.md` | Full text |

## Claims and findings

### 1. Claude Managed Agents

| Claim in the notes | Finding |
|---|---|
| Cost figures for a session and for monthly runtime | The figures arrived garbled in the notes. Our earlier record has the article's wording: "$0.08 per session-hour", "roughly $58 per month" for continuous running, and a one-hour Opus session example of "about $0.705 total". These are the author's time-stamped claims, read through a summarising fetch. Not usable. |
| Four primitives; flat delegation only; at most 20 sub-agents | Consistent with our earlier record (agent, environment, session, events; one level of delegation; up to 20 agents per coordinator) |
| Quotes: "The harness is becoming a commodity, and Anthropic is one of the first companies to ship it as such"; "Building a reliable agent loop is not the differentiator. The product is"; "You write the waiter. Anthropic runs the kitchen." | Not checked. The article has not been read from full text. |

### 2. MinusX

| Claim in the notes | Finding |
|---|---|
| One flat message history | Confirmed: "it maintains a flat list of messages" |
| At most one sub-agent branch, no recursive spawning | Partly confirmed. No recursive spawning is firm ("There is a maximum of one branch"). The next paragraph says "the main agent creates clones of itself", plural, so "only one sub-agent" is not clearly stated. |
| "Debuggability >>> complicated hand-tuned multi-agent lang-chain-graph-node mishmash." | Confirmed verbatim |
| About 50% of important LLM calls go to Haiku at 70–80% lower cost | Corrected. The text says "Over 50% of all important LLM calls made by CC are to claude-3-5-haiku". The "70–80%" figure is a separate, general statement about smaller models' prices, not a measured saving. The Haiku calls are auxiliary (large files, web pages, git history, summaries), not the main loop. |
| Token anatomy: ~2.8k system prompt, ~9.4k tool docs, 1–2k CLAUDE.md | Confirmed: "~2800 tokens", "9400 tokens", "another 1000-2000 tokens" |

The article describes Claude Code as of August 2025.

### 3. Claude Code source-leak analysis

| Claim in the notes | Finding |
|---|---|
| Three-layer memory; autoDream; cached and dynamic prompt split; "spawning 5 agents costs barely more than 1" | Consistent with our earlier record, which was a summarising fetch |
| 20+ unshipped flags including KAIROS; anti-distillation defences | Consistent with our earlier record. The article rests on leaked source; unshipped features may not reflect the product. |
| A startup should not plan to win background agents; Anthropic treats the harness as defensible IP | Pedro's inferences, not claims of the article |

### 4. Anthropic harness design

| Claim in the notes | Finding |
|---|---|
| "Context anxiety": Sonnet 4.5 wraps up early near context limits | Confirmed. The post adds that "Opus 4.5 largely removed that behavior on its own". |
| Self-evaluation bias | Confirmed: "agents reliably skew positive when grading their own work" |
| Planner → Generator (negotiates sprint contract) → Evaluator (Playwright as a real user, per-criterion thresholds) | Confirmed |
| `feature_list.json` in JSON because it resists accidental reformatting | Not in this post. See item 8. |
| "Unacceptable to remove or edit tests" as a hard rule | Not in this post |
| Solo agent ships a broken game; harnessed agent ships 16 working features over 10 sprints | Corrected. The planner produced "a 16-feature spec spread across ten sprints". The post does not say all 16 worked. The solo run cost "$9" in "20 min"; the harness run "$200" in "6 hr". |
| "The harness is the product" | Not in this post |

### 5. Copilot vs "Private AGI"

Not found after three searches on its title and phrases. Every point below is Pedro's note only.

- Autonomy decision formula EV = B×p − L×(1−p) − C: agent mode only if the loss L is bounded and the success probability p is high.
- "The hidden dependency is not AGI. It's the scoreboard."
- "Autonomy tax."
- Homogenisation risk, with team-specific style and conventions as a differentiation idea.
- Juniors gain most, "+14–15% support productivity". By the note's own wording this is a customer-support figure, not a coding one.

### 6. Anthropic, AI-resistant technical evaluations

| Claim in the notes | Finding |
|---|---|
| Claude 3.7 beaten by more than 50% of candidates | Corrected; the direction was reversed. "By May 2025, Claude 3.7 Sonnet had already crept up to the point where over 50% of candidates would have been better off delegating to Claude Code entirely." |
| Opus 4 beat most; Opus 4.5 matched the top human casually | Confirmed with caveats. They were different versions of the task (a 4-hour and then a 2-hour limit), and Opus 4.5 needed to be told the achievable score. |
| "Human experts retain an advantage at sufficiently long time horizons" | Corrected wording: "Human experts retain an advantage over current models at sufficiently long time horizons." |
| Method: use the model to find where models fail and design evaluations there | Confirmed. That version "served us well—for several months" before the next model beat it. |

### 7. "Sessions fall apart at hour three"

| Claim in the notes | Finding |
|---|---|
| Four layers with explicit lifetimes (Plan Mode, committed spec, task list, cross-session todos) | Confirmed. The todos path is `.claude/todos.json`. |
| "refusing to ask any one of them to be the others" | Confirmed |
| Interview to spec, then execute in a fresh session | Confirmed |
| Tools fail "not because the tool lacks project management, but because nobody told you which layers it already includes" | Corrected: the subject is sessions. "Your sessions fall apart not because the tool lacks project management, but because nobody told you which layers it already includes." |

### 8. CCA-F Part 4

| Claim in the notes | Finding |
|---|---|
| "The model is not the system. The system is everything that persists between sessions" | Confirmed; it continues ": logs, files, commits, and structured summaries" |
| "Compaction produces summaries, not specifications"; "the problem is the quality of the handoff" | Confirmed |
| "Structural gravity": rigid JSON schemas stop agents rewriting their own requirements | Corrected; the text is weaker. "JSON introduces structural constraints that the model is less likely to violate". No validator, permission or hook is described. |
| 4–5 tools at most per agent | Confirmed: "Limit tools per agent (4–5 max)" |
| Only `stop_reason == "tool_use"` continues the loop; "most failures are in loop control" | Confirmed, with wording: "Most system failures occur in loop control" |

This article is a second-hand summary of an Anthropic engineering post that we have not read (ASSIST-013). It has the same author as item 7.

### 9. Agent visualization

| Claim in the notes | Finding |
|---|---|
| Repo-tree view where brightness shows how recently a file was accessed | Confirmed: "The more recently in the chat a file has been visited, the brighter and bolder the outline". "Heatmap of agent attention" is not the author's wording. |
| Built by tailing `~/.claude/projects/*.jsonl` | Corrected. The path is `~/.claude/projects/<slug>/*.jsonl`. The text says the tool "monitors" the most recent session and does not describe how. |
| Observability without instrumenting the agent | A fair inference; the author does not make the claim. The tool works only with the Claude CLI and the article says nothing about the format's stability. |

## Summary of the check

- Most structural points in the notes hold.
- Seven claims needed correcting, two of them materially: the Claude 3.7 comparison was reversed, and the "16 working features" result was overstated.
- Three quotations attributed to the Anthropic playbook are not in the primary post.
- Everything from item 5, and the three quotations in item 1, remain unchecked.
