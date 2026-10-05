# What makes Claude Code so damn good (and how to recreate that magic in your agent)

| | |
|---|---|
| Author | "vivek", MinusX blog |
| Published | 2025-08-21 |
| Source | https://minusx.ai/blog/decoding-claude-code/ |
| Read on | 2026-10-05, from the publisher's page |
| Method | Read end to end by a Claude Code sub-agent from the complete downloaded text, and checked against Pedro's prior notes on the article. |
| Status | Digest. Describes Claude Code as of August 2025. Figures are the author's, with no method or sample given; none is usable as evidence. |
| Used for | PLAN §3.6; prototype design (single loop, cheaper-model arm) |

## Read record

- **Article:** "What makes Claude Code so damn good (and how to recreate that magic in your agent)!?", MinusX blog, https://minusx.ai/blog/decoding-claude-code/
- **Author and date:** byline "vivek", dated 2025-08-21.
- **Read:** the whole file, all 297 lines. The appendix (system prompt, tool list) is collapsed and not in the file.
- **How the author knows:** traffic interception plus personal use. "Sreejith wrote a logger that intercepts and logs every network request made"; the analysis is "from my extensive use over the last couple of months". No method, sample size or dataset is given for any number. The recommendations are opinion.

## What the article says

Thesis: Claude Code (CC) is good because it is architecturally simple. "Keep Things Simple, Dummy. LLMs are terrible enough to debug and evaluate."

- **One loop.** "Claude Code has just one main thread"; "it maintains a flat list of messages". Hierarchical tasks are handled "by spawning itself as a sub-agent without the ability to spawn more sub-agents", the result being "added to the main message history as a 'tool response'".
- **Small model for auxiliary work.** Haiku is "used to read large files, parse web pages, process git history and summarize long conversations".
- **Prompts.** Long, with heuristics, examples, XML tags (`<system-reminder>`, `<good-example>`) and Markdown sections. "CC sends the entire contents of the claude.md with every user request".
- **Search.** "LLM search >>> RAG based search"; RAG "introduces new (and more importantly, hidden) failure modes".
- **Tools.** High-level tools such as `mcp__ide__getDiagnostics` are "extremely deterministic in what they do".
- **Todo list.** Maintained by the model, against "context rot". The author rejects "Multi-agent handoff + verification (PRD/PM agent -> implementer agent -> QA agent)".

## Check of Pedro's notes

- **One flat message history** — Confirmed: "it maintains a flat list of messages".
- **At most one sub-agent branch, no recursion** — Confirmed, with an ambiguity. "There is a maximum of one branch" and sub-agents lack "the ability to spawn more sub-agents"; but the next paragraph says "the main agent creates clones of itself" (plural). No recursion is firm; "only one sub-agent" is not clearly stated.
- **Quote** — Confirmed verbatim: "Debuggability >>> complicated hand-tuned multi-agent lang-chain-graph-node mishmash."
- **"About 50% ... to Haiku at 70-80% lower cost"** — Corrected. Exact text: "Over 50% of all important LLM calls made by CC are to claude-3-5-haiku." The cost figure is a separate general statement: "The smaller models are 70-80% cheaper than the standard ones (Sonnet 4, GPT-4.1)." It is not a measured saving on CC's bill.
- **Token anatomy** — Confirmed: "The system prompt is ~2800 tokens long, with the Tools taking up a whopping 9400 tokens. The user prompt always contains the claude.md file, which can typically be another 1000-2000 tokens." Note claude.md sits in the user prompt.

## Figures

All are the author's claims; none has a stated method, sample or date range.

- "Over 50% of all important LLM calls made by CC are to claude-3-5-haiku" — presumably counted from intercepted logs; "important" is undefined.
- "70-80% cheaper than the standard ones (Sonnet 4, GPT-4.1)" — asserted price comparison, no source.
- "The system prompt is ~2800 tokens long" — from intercepted prompt; tokenizer not stated.
- "the Tools taking up a whopping 9400 tokens" (repeated in section 3) — same basis.
- "another 1000-2000 tokens" for claude.md — asserted as typical.
- "only makes debugging 10x harder" — rhetorical.
- "maximum of one branch" — observed behaviour.
- "it just looks at 10 lines of the json file" — illustrative.
- "This post is ~2k words long"; "57 min read" (as the byline renders) — page description.
- Chart captions carry no numbers; the charts are not in the text.

## Relevance to our thesis

Supports:

- The leading harness is a single loop with a flat history, so a minimal single-loop Python agent is a defensible agent under test.
- "LLMs are terrible enough to debug and evaluate" supports evaluation as the entry point.
- It names existing plug-in surfaces: claude.md sent with every request, and MCP tools.
- Intercepting network requests worked as a no-cooperation way to observe a vendor harness.

Cuts against:

- The author dismisses "handoff + verification" with a QA agent. Our verifier is deterministic and runs after the agent stops, but buyers sharing this view may hear "verification layer" as added complexity. Position it as checks, not agents.
- Haiku handles auxiliary calls; the main loop is credited to "the new Claude 4 model". Nothing here shows a cheaper model can run the main edit loop, so the cheaper-model arm is not pre-validated.
- "you deviate from the general-model-improvement trajectory" is a warning to anything layered on harnesses.

For the prototype: one file, one loop; log the model per call so cost per accepted change separates main-loop from auxiliary calls.

## Cautions

- **Dated.** Describes Claude Code as of August 2025: "the new Claude 4 model", Sonnet 4, claude-3-5-haiku, GPT-4.1, and a tool list including LS, MultiEdit, TodoWrite. No CC version number is given.
- **Unsupported.** "The difference in Claude Code's performance with and without claude.md is night and day" and "We already know multi-agent handoff is not a good idea" come with no evidence.
- **Promotional.** The author sells MinusX ("We've incorporated most of these into MinusX already"; demo links).
- **Reverse-engineered.** Not an Anthropic account; design intent is inferred from traffic.
