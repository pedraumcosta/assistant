# Research records

Everything we read or looked up for the ASSIST exercise, recorded so the repo stands on its own (`docs/PLAN.md` decision D9). `EVIDENCE.md` is the only file whose figures may be quoted elsewhere; the rest are working records.

## Index

| File | What it is | Confidence |
|---|---|---|
| `EVIDENCE.md` | Ledger of every figure and quotation we rely on, with source, date, URL and verification tag | Curated; rows tagged [S] are unverified |
| `market-landscape.md` | Competitor table, feature taxonomy, where incumbents are strong, candidate gaps, recent market events | Record as received; many [S] figures |
| `limitations-evidence.md` | Independent evidence on productivity, quality, security, cost and technical limits, including the case against entering | Record as received; mixed [P] and [S] |
| `harness-paper.md` | arXiv 2609.00006v1, the Wavestone AI Lab source-code study of eleven coding harnesses | Read end to end from the full text |
| `articles/` | One record per article from the brief (table below) | Varies; see table |
| `practitioner-notes.md` | Digest of Pedro's private working notes on AI, software engineering and management | Digest of curated notes; figures not yet traced to primary sources |

### Articles

| File | Article | Author | How it was read |
|---|---|---|---|
| `articles/building-claude-code-with-harness-engineering.md` | Building Claude Code with Harness Engineering | Fareed Khan | Full text, end to end |
| `articles/building-claude-from-scratch-62-components.md` | Building Claude from Scratch: 62 Components Behind Anthropic's Thinking Engine | Fareed Khan | Full text, end to end |
| `articles/senior-staff-engineer-sub-agent-teams.md` | Building a Senior Staff Engineer with Sub-Agent Teams in Claude Code | Fareed Khan | Full text, end to end |
| `articles/agent-harnesses-with-claude.md` | Agent Harnesses with Claude — Intuitively and Exhaustively Explained | Daniel Warfield | Full text, end to end |
| `articles/claude-code-source-leak.md` | Diving into Claude Code's source code | Engineer's Codex | Summarising fetch only |
| `articles/claude-architect-study-guide.md` | The Complete Claude Architect Study Guide | Data Science Collective | Summarising fetch only |
| `articles/claude-managed-agents.md` | Claude Managed Agents: Stop Building Your Own Agent Loop | Towards AI | Summarising fetch only |

The article records are digests written for this exercise, not copies of the articles.

## How the research was done

All research was run from one Claude Code session. Reading was delegated to sub-agents, each with a written brief and its own context; the main session worked from their reports and wrote the plan.

Two reading methods were used, and the difference matters:

- **Summarising fetch.** The page is retrieved by a tool that returns a small model's summary. Fast, but it truncated long articles without saying so. Used for the first pass on 2026-10-03.
- **Full text.** The page is downloaded, converted to text, checked to run through to its final section, and read end to end. Used on 2026-10-05 for the four long articles and the paper.

### Research passes

Token, tool-call and duration figures are as reported by the Claude Code harness for each sub-agent.

| Date | Pass | Method | Tokens | Tool calls | Duration |
|---|---|---|---|---|---|
| 2026-10-03 | Pedro's AI and LLM notes | Local files | 186,489 | 19 | 113 s |
| 2026-10-03 | Pedro's software engineering notes | Local files | 125,820 | 18 | 111 s |
| 2026-10-03 | Pedro's management notes | Local files | 139,356 | 24 | 145 s |
| 2026-10-03 | Linked articles, first pass | Summarising fetch | 66,945 | 22 | 267 s |
| 2026-10-03 | Market landscape | Web search and fetch | 106,841 | 66 | 236 s |
| 2026-10-03 | Limitations evidence | Web search and fetch | 101,144 | 56 | 224 s |
| 2026-10-05 | Senior Staff Engineer article | Full text | 104,709 | 7 | 78 s |
| 2026-10-05 | Agent Harnesses article | Full text | 113,239 | 7 | 87 s |
| 2026-10-05 | Harness Engineering article | Full text | 199,239 | 9 | 95 s |
| 2026-10-05 | 62 Components article | Full text | 171,700 | 11 | 130 s |
| 2026-10-05 | Harness paper (arXiv 2609.00006v1) | Full text | 194,762 | 17 | 204 s |

The harness paper was read twice on 2026-10-05: selected sections by the main session directly from the arXiv full text, then end to end by a sub-agent.

### Other lookups

- **GitHub access model** (2026-10-05). GitHub Docs pages on personal-account repository permissions, organisation repository roles and plan features, to settle where the repo should live. Result in `EVIDENCE.md` rows E-27 to E-29 and PLAN decision D6.
- **Local environment** (2026-10-03 and 2026-10-05). GitHub CLI authentication, git identity, Python version, and whether model API keys were present. No values were read or recorded.

## Known gaps

- **Unverified figures.** Many market figures are [S]. `EVIDENCE.md` lists the verification work still open (ASSIST-004).
- **Three articles read only through a summarising fetch** (ASSIST-005).
- **Pedro's notes were partly unavailable.** Several shelves were not synced to the machine, including the strategy and product-management material (ASSIST-003).
- **Interested sources.** Much of the problem evidence comes from vendors who sell the fix (Faros, Sonar, Veracode, GitGuardian, GitClear). Independent confirmation exists (METR, Stack Overflow) but is thinner.
- **No primary market-size, revenue or unit-economics data.**
