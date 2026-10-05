# Pedro's web research notes, checked against the sources

| | |
|---|---|
| Origin | Pedro's web research notes of 2026-10-01, given to this project on 2026-10-05. They cover a competitive snapshot, harness ideas in circulation, developer pain points, data for the CFO case, repository understanding, and an enterprise procurement checklist. |
| What this file is | The overview of the check: what held, what was corrected, and what could not be verified. The detail is in four companion files. |
| Method | Four Claude Code sub-agents checked the claims on 2026-10-05, each told to confirm figures and quotations in the raw downloaded page instead of a summary. One paper cited in the notes was read in full. |
| Status | Many dollar figures were garbled when the notes were handed over; the checks recovered them from the sources. Parts of the notes were written for a different purpose (preparing to discuss building an assistant) and are recorded here only for their factual content. |
| Used for | PLAN §3.8, ROADMAP §2 |

## Where the detail is

| Part of the notes | Record |
|---|---|
| Competitive snapshot, CFO-case data, and six conflicts with our earlier records | `check-market-claims.md` |
| Harness ideas, repository understanding, pain points | `check-harness-and-repo-claims.md` |
| Enterprise procurement checklist | `check-procurement-claims.md` |
| "Review/verification is the hot funded segment" | `review-verification-segment.md` |
| "harness governs performance more than model (arXiv 2609.20804 ablations)" | `paper-harness-ablation.md` |

## The six conflicts with our earlier records

| Topic | The notes said | Finding |
|---|---|---|
| Stack Overflow survey | "2026: 84% use AI, trust 29%" | Our record was right. The 2026 survey is not published. The 2025 figures are 84% using or planning to use AI, 46% distrust against 33% trust. "29%" is a 2025 sub-figure. |
| "98% more PRs, 91% longer in review" | "directionally per DORA" | Our record was right. Faros AI, 2025-07-23. Not in the DORA report. |
| "Verification tax" | Attributed to DORA 2025 | Neither fully right. Not in the DORA 2025 report; used in a DORA insight article dated 2026-03-10, before the paper we had credited (arXiv 2609.04681, September 2026). Who coined it is not established. |
| EU AI Act high-risk obligations | August 2026 | Our record was right. The omnibus entered into force on 2026-07-27 and moved Annex III obligations to 2027-12-02. |
| opencode GitHub stars | ~165k | Our record was closer: 211,831 on 2026-10-05. The notes were right that Aider's last commit was 2026-05-22. |
| Cognition | Round and valuation had moved | The notes were right; our record was stale. Cognition's blog, 2026-09-08: "raised over $2B at a $48B valuation". |

## Corrections to the notes

**Competitive snapshot**
- Anthropic has no separate long-context pricing; its docs say long-context requests are billed at standard pricing.
- Amp is a separate company since December 2025. Its page says "No Amp token fees or limits" with bring-your-own-keys, not "zero markup", and now lists a 20 USD Individual tier.
- No Codex plan is called "Premium"; Pro starts at 100 USD.
- Cursor's page shows Teams at 40 USD per user; no 60 USD tier or "Business" plan was found.
- The TechCrunch article does not say Cursor's margins are negative.
- The "CodeRabbit 1.5B (25M Series A)" line merges two companies: the valuation is CodeRabbit's, the 25M USD Series A is Greptile's.

**Harness ideas**
- The cited paper does not show that the harness governs performance more than the model. Its conclusion is conditional on model, task and budget.
- The OpenAI "Harness engineering" link pointed to a different post. The right one is dated 2026-02-11; the claim itself holds.
- The "Skill issue" post is by Dex Horthy's cofounder.
- The token-reduction figures (98.7% from Anthropic, 99.9% from Cloudflare) measure tool-definition or input tokens, not whole-task cost.
- Simon Willison confirms review as "the natural bottleneck" but writes "I haven't adopted git worktrees yet".
- "Spec-driven dev now shipped by everyone" was not verified beyond Kiro, GitHub Spec Kit and Tessl.

**Repository understanding**
- "Beat everything" is the interviewer's summary, not Boris Cherny's words. His post is confirmed verbatim.
- Cursor's +2.6% retention applies only to codebases of 1,000 or more files; overall it is +0.3%.
- Aider's documentation says "graph ranking algorithm"; "PageRank" appears only in its source code.
- Serena's README now says "over 40 programming languages".

**Pain points**
- Cursor did not roll back its July 2025 pricing; it apologised and offered refunds.
- The Copilot "September cliff" is a cost-management vendor's label for promotional credits ending on 2026-09-01.

**Procurement checklist**
- Cline does not document SCIM.
- Copilot is not SaaS-only: local bring-your-own-key exists and an enterprise version is in public preview.
- Copilot "premium-request budgets" is outdated; Business and Enterprise are billed in AI credits since 2026-06-01.
- `allowedProviders` is a provider allow-list. The model allow-list is `availableModels`.
- "Uncapped" Copilot indemnity could not be verified.

## Confirmed as stated

- The Cursor acquisition, from the SEC filing: closed 2026-08-14, 389,289,254 Class A shares, implied equity value 60.0 billion USD.
- Copilot's move to usage-based AI Credits on 2026-06-01.
- Both METR findings, and all four GitClear figures.
- The Copilot 180-day window for agent activity, and the April 2026 indemnity-filter change.
- The 30-day retention tension: Anthropic's newest models "require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic".
- Claude Code's run-rate of "over $2.5 billion" (Anthropic, 2026-02-12), with enterprise "over half".

## Could not be verified

- The Bloomberg figure of 1 billion USD annualised revenue for Cognition (seen only through a secondary outlet).
- Any 2030 market-size forecast beyond one market-report vendor's 22.06 billion USD. These are forecasts and are not used.
- Augment's revenue.
- Copilot indexing "on default branch", and whether code passes through Cursor's servers for embedding.
- The publication date of the GitClear report.

## What the check found that the notes did not say

1. **The funded reviewers sell model judgment, not deterministic verification.** CodeRabbit's own docs say its custom checks cannot run the test suite. Claude Code's review check "always completes with a neutral conclusion so it never blocks merging".
2. **CodeRabbit is moving toward our position.** Its 2026-08-12 release (143 million USD at a 1.5 billion USD valuation) launched "Agentic Change Management" as "the control layer", with risk scoring, routing to humans and auto-merge of low-risk changes.
3. **Two adjacent products are deterministic or per-repository.** Sonar sells a deterministic quality gate "optimized for agent centric development" and a product that sets constraints before coding and then verifies each change with static analysis. Faros sells benchmarks "from your own merged code" to cut "cost per verified outcome". Neither runs the customer's acceptance checks against a pre-agreed contract.
4. **No vendor publishes a false-pass rate** for its own verdicts. Four vendors each claim first place on the same review benchmark.
5. **No vendor audit log records the outcome of an agent's work.** They record actions and cost.
6. **A frontier lab argues against blocking gates.** OpenAI: "The repository operates with minimal blocking merge gates. … corrections are cheap, and waiting is expensive", followed by "This would be irresponsible in a low-throughput environment."
