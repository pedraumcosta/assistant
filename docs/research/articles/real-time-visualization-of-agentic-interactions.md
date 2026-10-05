# Real-Time Visualization of Agentic Interactions — Intuitively and Exhaustively Explained

| | |
|---|---|
| Author | Daniel Warfield |
| Published | Page dated 2026-08-22 |
| Source | https://medium.com/intuitively-and-exhaustively-explained/real-time-visualization-of-agentic-interactions-intuitively-and-exhaustively-explained-7b8958da837a |
| Read on | 2026-10-05, via a Freedium mirror |
| Method | Read end to end by a Claude Code sub-agent from the complete downloaded text, and checked against Pedro's prior notes on the article. |
| Status | Digest. The article contains no measurements. |
| Used for | PLAN §3.6; ROADMAP open question T5 (attachment points) |

## Read record

- **Article:** "Real-Time Visualization of Agentic Interactions — Intuitively and Exhaustively Explained".
- **Author and date:** Daniel Warfield; the page shows "August 22, 2026". Read through a Freedium mirror of the Medium article.
- **Read:** the whole file, all 163 lines. Images and link targets are not in the text.
- **How the author knows:** he built the tool described (ahar-visualizer, a VSCode extension) and reports its design and his own use. It is a product walkthrough and opinion; there is no measurement or experiment.

## What the article says

Thesis: you cannot improve how an agent navigates a large directory unless you can watch it. "without any ability to observe what 'quickly and consistently understanding' looks like, it's impossible to understand what approaches work well and what approaches don't."

Mechanism:

- "The visualizer looks at two things": the directory open in VS Code, and the Claude CLI transcript.
- "When you run Claude via the Claude CLI, the transcript of the conversation is stored in ~/.claude/projects/<slug>/*.jsonl". The visualizer "looks at the most recent chat session and monitors for reads, writes, edits, and updates to files".
- "The more recently in the chat a file has been visited, the brighter and bolder the outline." Any file visited in the session keeps "a thin orange line"; a new session resets it.

The second half covers the author's Agent Harnesses Standard: "routing files" (HARNESS.md at the root; TOOLS.md, DOCS.md, SRC.md and similar below), nested "sub-harnesses", and "leaf" folders such as skills with a SKILL.md, under "progressive disclosure".

## Check of Pedro's notes

- **"Repo-tree heatmap of agent attention"** — Corrected in wording. The text describes a tree visualization with highlighted nodes; "heatmap" and "attention" are not the author's words. It shows file visits.
- **"Node brightness = file-access recency"** — Confirmed: "The more recently in the chat a file has been visited, the brighter and bolder the outline."
- **"Built by tailing ~/.claude/projects/*.jsonl"** — Corrected. Exact path: "~/.claude/projects/<slug>/*.jsonl". "Tailing" is not in the text; the author says it "monitors" the most recent session and does not describe the implementation.
- **"Observability without instrumenting the agent"** — Not in the text as a claim. It is a fair inference: the tool reads files the CLI already writes and no hooks or agent changes are mentioned.

## Figures

The article contains no measured quantities. Every number present:

- "10 min read" and "August 22, 2026" — page metadata.
- "Agent Harnesses has 6 repositories available" — a GitHub link preview, not an author measurement.
- "two simultaneous sessions in two different repos"; "looks at two things" — descriptive.
- "1.1M articles unlocked" — Freedium mirror chrome, unrelated to the article.
- Versions appear only as placeholders: "ahar-visualizer-X.Y.Z.vsix".

No token counts, timings, accuracy or cost figures are given.

## Relevance to our thesis

- **Transcript files read:** "~/.claude/projects/<slug>/*.jsonl", by default "the most recent session on your computer".
- **Fields read:** not stated. The article says only that it watches for "reads, writes, edits, and updates to files". No JSON field, record type or tool name is given.
- **Stability or documentation of the format:** not addressed. The author says only that the transcript "allows Claude to keep track of the chat context", which describes the CLI's own working state, not a published interface. No version guarantee, no documentation cited.
- **As a no-cooperation attachment point:** the article is an existence proof that a third party can derive live file-level activity for a vendor harness from local transcripts with no change to the agent. That could feed an evidence bundle (files read and edited, access order, scope check against a change contract). Limits in the text:
  - "Currently, the Claude CLI is the only agentic tool this visualizer works with."
  - It runs on the developer's machine; nothing is said about CI or remote runs.
  - It records visits, not correctness: observation, not verification.
  - The transcript is written by the agent's own client, so it is self-reported. Deterministic checks after the agent stops should not depend on it.

Supports our direction: the author builds around existing harnesses rather than a new one, and treats SKILL.md and markdown routing files as the integration unit. He built the tool "to allow me to visualize A/B tests", a sign of demand for per-repo agent evaluation.

Cuts against: tooling layered on harnesses is already being produced as open source ("All of these repos are open source"), so observability alone is unlikely to be a paid differentiator.

For the prototype: treat transcript parsing as an optional, best-effort evidence source with a format check; use hooks or CI as the primary one.

## Cautions

- **Promotional.** The author presents his own tool and standard.
- **Unsupported.** "this scheme is yet to cause confusion" is anecdote from one user. The A/B tests are "an article that I'm currently working on"; no results exist here.
- **Versions.** Dated August 22, 2026; concerns "the Claude CLI" / Claude Code. No CLI version, model name or extension version is stated.
- **Source quality.** Read through an unofficial mirror; images are missing and the install text is inconsistent (".visx" and ".vsix").
