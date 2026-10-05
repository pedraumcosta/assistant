# Research records

Everything we read or looked up for the ASSIST exercise, recorded so the repo stands on its own (`docs/PLAN.md` decision D9). `EVIDENCE.md` is the only file whose figures may be quoted elsewhere; the rest are working records.

## Index

| File | What it is | Confidence |
|---|---|---|
| `EVIDENCE.md` | Ledger of every figure and quotation we rely on, with source, date, URL and verification tag | Curated; rows tagged [S] are unverified |
| `market-landscape.md` | Competitor table, feature taxonomy, where incumbents are strong, candidate gaps, recent market events | Record as received; many [S] figures |
| `limitations-evidence.md` | Independent evidence on productivity, quality, security, cost and technical limits, including the case against entering | Record as received; mixed [P] and [S] |
| `harness-paper.md` | arXiv 2609.00006v1, the Wavestone AI Lab source-code study of eleven coding harnesses | Read end to end from the full text |
| `harness-paper-implications-2026-10-02.md` | Pedro's own analysis of what the harness paper implies, checked claim by claim against the paper and set against our later research | Checked by the main session against the HTML text and the PDF |
| `paper-verification-economics.md` | arXiv 2609.04681, a synthesis proposing Production-Qualified Change, the Verification Tax and an SDLC control plane. Prior art for our framing | Read end to end by the main session |
| `paper-governed-ai-engineering.md` | arXiv 2606.22484, a governance framework with three human-oversight tiers for agent-written code in regulated domains | Read end to end from the full text |
| `articles/` | One record per article, from the brief and from Pedro's Notion notes (table below) | Varies; see table |
| `practitioner-notes.md` | Digest of Pedro's private working notes on AI, software engineering and management | Digest of curated notes; figures not yet traced to primary sources |
| `notion-notes-2026-10-01.md` | Pedro's summary of nine strategy reads from his Notion database, with each claim checked against the source | Checked where the source was read in full; one source not found |
| `web-research-notes-2026-10-01.md` | Pedro's web research notes of 2026-10-01, with an overview of what held, what was corrected and what could not be verified | Overview of the four check files below |
| `check-market-claims.md` | Claim-by-claim check of the competitive snapshot and CFO-case data, including six conflicts with our earlier records | Figures confirmed in raw pages; some publishers blocked |
| `check-harness-and-repo-claims.md` | Claim-by-claim check of harness ideas, repository understanding and pain points | Figures confirmed in raw pages |
| `check-procurement-claims.md` | Check of the enterprise procurement checklist against vendors' official documentation | Quotations confirmed in raw pages |
| `review-verification-segment.md` | Funding, scale and actual behaviour of AI code review and verification products; what vendor audit logs record; the products closest to our idea | Figures confirmed in raw pages; the assessment of how occupied the space is belongs to the researcher |
| `paper-harness-ablation.md` | arXiv 2609.20804, an ablation study of planning, tools and context management across four models | Read end to end from the full text |
| `second-thesis-brownfield.md` | Evaluation of a second thesis, a brownfield / enterprise-legacy specialisation: its evidence read in full, the market, and what it changes in the first thesis | Overview of the four records below; the assessment and recommendation are ours |
| `paper-swe-refactor-bench.md` | arXiv 2608.23564: whole-repository migrations judged in three stages; the best measurement we have of a behaviour-only check passing bad changes | Read end to end from the full text |
| `paper-legacy-modernization-case-study.md` | arXiv 2608.28972: a VB6 to C# migration of twelve features, assessed by hand | Read end to end; one system, internally inconsistent on some figures |
| `brownfield-market.md` | Who sells AI for legacy modernisation, the demand evidence, Osmani's case studies checked at source, and products close to the four practices | Figures confirmed in raw pages; the closing assessment is the researcher's |
| `decision-models-2026-10-02.md` | Pedro's addendum on the Jev decision model: what it is, what held, and where it fits an assistant and our evidence layer | Overview of the two check files below; the product is three weeks old and independent evidence is thin |
| `check-decision-model-product.md` | Claim-by-claim check of what Jev is, its limits, deployment and the measurements cited for it | Figures confirmed in raw pages |
| `check-decision-model-risks.md` | Check of the risk and crowdedness claims, including a full read of arXiv 2609.29769 on shared errors between decision models and LLM judges | Figures confirmed in raw pages; negative findings are weak |

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
| `articles/anthropic-harness-design-long-running-apps.md` | Harness design for long-running application development | Prithvi Rajasekaran, Anthropic | Full text, by the main session |
| `articles/anthropic-ai-resistant-technical-evaluations.md` | Designing AI-resistant technical evaluations | Tristan Hume, Anthropic | Full text, end to end |
| `articles/minusx-decoding-claude-code.md` | What makes Claude Code so damn good | MinusX | Full text, end to end |
| `articles/claude-code-spec-driven-development-hour-three.md` | Claude Code: Spec-Driven Development — Why Your AI Coding Sessions Fall Apart at Hour Three | Rick Hightower | Full text, end to end |
| `articles/cca-f-part-4-long-running-agent-harness.md` | Foundations of CCA-F Exam Part 4: Engineering the Long-Running Agent Harness | Rick Hightower | Full text, end to end |
| `articles/real-time-visualization-of-agentic-interactions.md` | Real-Time Visualization of Agentic Interactions | Daniel Warfield | Full text, end to end |
| `articles/osmani-brownfield-agentic-engineering.md` | Brownfield Agentic Engineering | Addy Osmani | Full text, by the main session |

The article records are digests written for this exercise, not copies of the articles.

## How the research was done

All research was run from one Claude Code session. Reading was delegated to sub-agents, each with a written brief and its own context; the main session worked from their reports and wrote the plan.

Three methods were used, and the difference matters:

- **Summarising fetch.** The page is retrieved by a tool that returns a small model's summary. Fast, but it truncated long articles without saying so. Used for the first pass on 2026-10-03.
- **Full text.** The page is downloaded, converted to text, checked to run through to its final section, and read end to end. Used on 2026-10-05 for the four long articles and the paper.
- **Raw-page verification.** For checking specific claims: the page is downloaded and searched for the exact figure or quotation, so nothing rests on a summary. Used on 2026-10-05 for Pedro's web research notes.

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
| 2026-10-05 | AI-resistant evaluations post | Full text | 48,702 | 17 | 99 s |
| 2026-10-05 | MinusX and visualization articles | Full text | 58,089 | 10 | 137 s |
| 2026-10-05 | "Hour three" and CCA-F Part 4 articles | Full text | 73,446 | 11 | 179 s |
| 2026-10-05 | Governed AI-assisted engineering paper (arXiv 2606.22484) | Full text | 66,401 | 16 | 132 s |
| 2026-10-05 | Harness ablation paper (arXiv 2609.20804) | Full text | 96,939 | 12 | 163 s |
| 2026-10-05 | Check: harness, repository and pain-point claims | Raw-page verification | 110,229 | 27 | 304 s |
| 2026-10-05 | Check: market claims and six conflicts | Raw-page verification | 122,057 | 39 | 347 s |
| 2026-10-05 | Check: procurement checklist | Raw-page verification | 147,894 | 30 | 379 s |
| 2026-10-05 | Review and verification segment | Raw-page research | 219,065 | 68 | 615 s |
| 2026-10-05 | Check: Jev decision model, product claims | Raw-page verification | 148,790 | 34 | 395 s |
| 2026-10-05 | Check: decision-model risks and crowdedness | Raw-page verification | 201,366 | 59 | 502 s |
| 2026-10-05 | SWE Refactor Bench and VB6 case-study papers | Full text | 141,226 | 18 | 311 s |
| 2026-10-05 | Legacy modernisation and brownfield market | Raw-page research | 155,264 | 56 | 570 s |

Anthropic's harness design post and the verification-economics paper were read by the main session itself, so they have no row above.

The harness paper was read twice on 2026-10-05: selected sections by the main session directly from the arXiv full text, then end to end by a sub-agent.

### Other lookups

- **GitHub access model** (2026-10-05). GitHub Docs pages on personal-account repository permissions, organisation repository roles and plan features, to settle where the repo should live. Result in `EVIDENCE.md` rows E-27 to E-29 and PLAN decision D6.
- **Local environment** (2026-10-03 and 2026-10-05). GitHub CLI authentication, git identity, Python version, and whether model API keys were present. No values were read or recorded.

## Leads found but not read

- Anthropic's earlier engineering post on long-running agent harnesses (initializer agent, feature list, context resets), which the CCA-F article summarises and the harness design post builds on (ASSIST-013).
- arXiv 2609.28919 (Accenture, "Harness Tokenomics"), which models token-spend savings from routing coding-agent work with a decision model on an emulated enterprise.
- The primary studies cited by `paper-verification-economics.md` (for example the MIT / NBER study of commits against releases, Stanford SWE-chat, Meta TestGen-LLM, SWE-Marathon). Their figures are second-hand until read.

## Known gaps

- **`market-landscape.md` is partly superseded.** It was written on 2026-10-03 from mixed sources. Where it differs from `check-market-claims.md` (for example Cognition's valuation and the opencode star count), the check file is right.

- **Unverified figures.** Many market figures are [S]. `EVIDENCE.md` lists the verification work still open (ASSIST-004).
- **Three articles read only through a summarising fetch** (ASSIST-005).
- **One article from Pedro's Notion notes could not be found** ("Copilot vs Private AGI"); its points are unchecked (ASSIST-012).
- **Pedro's notes were partly unavailable.** Several shelves were not synced to the machine, including the strategy and product-management material (ASSIST-003).
- **Interested sources.** Much of the problem evidence comes from vendors who sell the fix (Faros, Sonar, Veracode, GitGuardian, GitClear). Independent confirmation exists (METR, Stack Overflow) but is thinner.
- **No primary market-size, revenue or unit-economics data.**
