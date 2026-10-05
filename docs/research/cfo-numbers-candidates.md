# Candidate figures for the CFO message — all [S], none usable yet

| | |
|---|---|
| Status | **Unverified.** Every row below was gathered through web search summaries on 2026-10-05 and is tagged [S]. Per the working rules (ADR-010, ASSIST-004), no row may appear in CXO-facing text until checked at its raw source and promoted to `EVIDENCE.md` with a [P] tag. |
| Purpose | Fill the gaps identified for the CFO conversation: market size, seat pricing, inference cost structure. The build-vs-buy math needs no external figure: the buy side is the seat prices below, the build side is our own staged probe costs. |

## Market size (TAM context — used only as honesty-tagged context, never as a claim)

Analyst estimates for the AI code assistant / code tools market in 2026 cluster at **8–10 billion USD**, with outliers at 6 and 10.3:

| Figure (2026) | Firm | Verify at |
|---|---|---|
| 9.46 B USD (from 7.65 B in 2025, 23.7% CAGR) | Research and Markets | researchandmarkets.com/reports/6225896 |
| 10.3 B USD | Grand View Research | grandviewresearch.com/industry-analysis/ai-code-assistants-market-report |
| 9.35 B USD | Mordor Intelligence | mordorintelligence.com/industry-reports/artificial-intelligence-code-tools-market |
| 10.12 B USD | Precedence Research | precedenceresearch.com/ai-code-tools-market |

Note for the message: these size the **assistant** market we refuse to enter. The review-and-verification sliver we would enter has no published size we found. Say so rather than derive one.

## Seat pricing (the "buy" column) — verify at the vendors' own pricing pages

| Product | Reported price | Verify at |
|---|---|---|
| GitHub Copilot Business / Enterprise | 19 / 39 USD per seat per month (Enterprise reported cut from 70 to 39 in 2026; usage-based AI Credits added June 2026) | github.com/features/copilot (pricing) |
| Cursor Teams | 32 USD/seat/mo annual (40 monthly); Premium tier 96 annual (120 monthly), June 2026 structure | cursor.com/pricing |
| CodeRabbit Pro | 24 USD/developer/mo annual (30 monthly); Enterprise custom, reported from 15,000 USD/mo for 500+ users | coderabbit.ai/pricing |
| Claude Code / OpenAI assistant tiers | Already verified: 20 and 100 USD tiers (EVIDENCE E-12, E-13) | — |

## Inference cost structure (the "run cost" contrast)

| Claim | Source to verify |
|---|---|
| AI-native products averaged ~45% gross margin in 2025, projected ~52–53% in 2026, against 70–85% for traditional SaaS | cloudzero.com/blog/ai-gross-margin |
| Inference averages ~23% of revenue at scaling-stage AI B2B companies | cloudzero.com/blog/ai-gross-margin (check its primary: likely a survey — cite the survey, not the blog) |
| Bessemer's 2025 benchmarks put the fastest-scaling cohort at ~25% gross margin, "often negative" | Bessemer's published 2025 AI benchmarks (find the original report) |
| "Margins on all of the 'code gen' products are either neutral or negative" | Already verified: EVIDENCE E-17 [P] |

## What was looked for and not found

- A published market size for agent-output **verification/review** tooling specifically.
- Any public build-vs-buy benchmark for this category. Conclusion: compose the comparison from verified seat prices and our own labelled assumptions; do not import a benchmark.
