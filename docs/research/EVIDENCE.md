# Evidence ledger

Every figure or quotation that a document in this repo relies on has a row here. The rule from `docs/PLAN.md` §5: no number is invented or estimated, and only rows tagged **[P]** or **[L]** may appear in a CXO-facing document.

| Tag | Meaning |
|---|---|
| [P] | Read on the publisher's own page on the research date |
| [L] | Read in a PDF copy of the published report held in Pedro's files. The PDF is not redistributed in this repo |
| [S] | Seen only in a search summary or secondary write-up. Not verified; must be upgraded to [P] or dropped |

Two cautions apply to every [P] row gathered by a research sub-agent: the page was fetched through a tool that summarises with a small model, so the exact wording of a quotation should be re-read at the source before it is printed in the proposal. Rows E-30 to E-33 were read directly from the source text and do not carry that caution.

"Interest" records whether the source sells a product that benefits from the finding.

## The problem is after generation

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-01 | "roughly half of test-passing SWE-bench Verified PRs … would not be merged into main by repo maintainers"; merge decisions "about 24 percentage points" below grader scores (296 PRs, 4 maintainers, 3 repos) | METR, 2026-03-10 | [P] | Independent | https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/ |
| E-02 | "Tasks involving code specifically have increased 210%" | Faros, AI Engineering Report 2026, 22,000 developers and 4,000 teams | [L] | Vendor (sells measurement) | https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways |
| E-03 | "Bugs per developer are up 54%" | Faros 2026 | [L], also [P] on the blog | Vendor | as E-02 |
| E-04 | "Median review time has increased 5X" (report PDF); "+441.5%" median time in review (blog) | Faros 2026 | [L] and [P] | Vendor | as E-02 |
| E-05 | "31% more PRs are merging without any review" (PDF); "+31.3%" (blog) | Faros 2026 | [L] and [P] | Vendor | as E-02 |
| E-06 | "+242.7% incidents per PR"; "+861% code churn" | Faros 2026 | [L] and [P] | Vendor | as E-02 |
| E-07 | 66% cite "AI solutions that are almost right, but not quite"; 46% distrust accuracy vs 33% who trust it; 84% use or plan to use AI tools; 48,854 respondents | Stack Overflow Developer Survey 2025, July 2025 | [P] | Independent of AI vendors | https://survey.stackoverflow.co/2025/ai |
| E-08 | "only 55% of generation tasks result in secure code"; "No meaningful security gains materialized" | Veracode Spring 2026 GenAI Code Security Update, 2026-03-24 | [P] | Vendor (sells AppSec) | https://www.veracode.com/blog/spring-2026-genai-code-security/ |
| E-09 | An agent deleted a production volume and its backups in 9 seconds; agent's statement: "I violated every principle I was given: I guessed instead of verifying, I ran a destructive action without being asked." | ACS Information Age, 2026-05-05, on the PocketOS incident of 2026-04-25 | [P] | Independent press | https://ia.acs.org.au/article/2026/gone-in-9-seconds--ai-agent-deletes-company-database.html |
| E-10 | 96% don't fully trust AI code to be functionally correct; only 48% always check before committing | Sonar State of Code 2026, Jan 2026 | [S] | Vendor | https://www.sonarsource.com/blog/state-of-code-developer-survey-report-the-current-reality-of-ai-coding/ |
| E-11 | Public frontier models: 80% time horizon "~1.5h [50m-2h40m]" against a 50% horizon of "~12h [5h-61h]" | METR Frontier Risk Report, 2026-05-19 | [P] | Independent | https://metr.org/blog/2026-05-19-frontier-risk-report/ |

## Where not to compete

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-12 | Claude: Pro 20 USD, Max from 100 USD | Anthropic pricing page, as displayed 2026-10-03 | [P] | Vendor | https://claude.com/pricing |
| E-13 | ChatGPT / Codex: Plus 20 USD, Pro 100 / 200 / 500 USD | OpenAI pricing page, as displayed 2026-10-03 | [P] | Vendor | https://learn.chatgpt.com/docs/pricing |
| E-14 | Google AI plans at 19.99 / 99.99 / 199.99 USD | Secondary coverage | [S] | — | https://www.cloudzero.com/blog/google-antigravity-pricing/ |
| E-15 | Copilot moved all plans to token-based "AI Credits" on 2026-06-01; "agentic usage is becoming the default, and it brings significantly higher compute and inference demands" | GitHub blog, 2026-04-27 | [P] | Vendor | https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ |
| E-16 | "Compared to today, this works out to a 17% reduction in weekly limits on Claude Code" | BleepingComputer quoting Anthropic, 2026-08-29 | [P] | Independent press | https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/ |
| E-17 | "Margins on all of the 'code gen' products are either neutral or negative" | TechCrunch, 2025-08-07 | [S] | Independent press | https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/ |
| E-18 | Windsurf, Continue, Tabnine and Roo Code absorbed or closed | Various secondary sources; see `market-landscape.md` §5 | [S] | — | — |
| E-19 | IBM introduced self-hosted, air-gapped deployment for IBM Bob | IBM newsroom, 2026-10-01 | [P] | Vendor | https://newsroom.ibm.com/2026-10-01-ibm-introduces-self-hosted-deployment-for-ibm-bob-to-help-enterprises-advance-ai-sovereignty-and-governance |

## The case against entering

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-20 | "(90%) use AI"; "(30%) currently report little to no trust in the code generated by AI"; nearly 5,000 respondents | DORA, State of AI-assisted Software Development 2025 | [L] | Vendor-run (Google) | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report |
| E-21 | Agent use rose from 31% to "59%" | Stack Overflow blog, 2026-09-30 | [P] | Independent of AI vendors | https://stackoverflow.blog/2026/09/30/getting-ready-for-2026-results-a-look-back-on-developer-survey-findings |
| E-22 | Follow-up to the slowdown study: returning developers "-18% with a confidence interval between -38% and +9%"; METR calls the data unreliable ("30% to 50% of developers told us that they were choosing not to submit some tasks") | METR, 2026-02-24 | [P] | Independent | https://metr.org/blog/2026-02-24-uplift-update/ |
| E-23 | Original study: 16 experienced open-source developers took "19% longer" with AI while estimating they were 20% faster | METR, July 2025, arXiv 2507.09089 | [S] | Independent | https://arxiv.org/abs/2507.09089 |
| E-24 | Adopters "merged roughly 24% more pull requests than they would have otherwise" | Microsoft, arXiv 2607.01418, 2026-07-01 (observational) | [P] | Vendor | https://arxiv.org/abs/2607.01418 |

## Cost and model routing

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-25 | 211 real tasks, 12 repos, judged by a model: Claude Code + GLM-5.2 at 0.92 USD per task (score 0.568); Claude Code + Opus 4.8 at 1.76 USD (0.521); Codex + GPT-5.5 at 2.06 USD (0.466) | Faros, 2026-06-25 | [P] | Vendor | https://www.faros.ai/blog/open-models-vs-frontier-models |
| E-26 | SWE-bench Pro: top entry 89.9%, best open-weight entry 65.1% | benchlm.ai aggregator, 2026-10-02; mostly vendor-reported scores, harnesses differ | [P] on the aggregator | Aggregator | https://benchlm.ai/benchmarks/swe-bench-pro |

## GitHub access model

| ID | Claim, as published | Source and date | Tag | URL |
|---|---|---|---|---|
| E-27 | "In a private repository, repository owners can only grant write access to collaborators. Collaborators can't have read-only access to repositories owned by a personal account." | GitHub Docs, read 2026-10-05 | [P] | https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/permission-levels-for-a-personal-account-repository |
| E-28 | Organisation repositories have five roles; the Read role cannot push | GitHub Docs, read 2026-10-05 | [P] | https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization |
| E-29 | GitHub Free includes unlimited private repositories "with a limited feature set"; protected branches on private repositories are listed under Pro and Team | GitHub Docs, read 2026-10-05 | [P] | https://docs.github.com/en/get-started/learning-about-github/githubs-plans |

## The harness paper

Read directly from the arXiv full text, not through a summarising tool. See `harness-paper.md`.

| ID | Claim, as published | Source | Tag | URL |
|---|---|---|---|---|
| E-30 | "across roughly four million lines of Python, TypeScript, and Rust, no agent runtime imports a general-purpose agentic framework, and none retrieves code with vector embeddings" | Barbaste, Darrigol, Vu, Wiltberger, arXiv 2609.00006v1, abstract | [P] | https://arxiv.org/abs/2609.00006v1 |
| E-31 | Recommendation 1: "Start with a linear while loop; graduate to a middleware pipeline only when orthogonal turn policies emerge." The paper includes "a 90-line minimum-viable-harness scaffold" | as E-30, §16 | [P] | as E-30 |
| E-32 | Omnigent "is not a twelfth harness; it is a bet that the harness has become a commodity component and that the durable value sits one layer up" | as E-30, §14.4 | [P] | as E-30 |
| E-33 | Future work: "Unified evaluation frameworks that assess safety, user experience, cost efficiency, and extensibility alongside correctness, addressing the gap between benchmark performance and production readiness." | as E-30, §17.2 | [P] | as E-30 |

## Not usable as evidence

- Every figure in `articles/`. They are the authors' own claims; several run transcripts are inconsistent with the code shown beside them.
- Every figure in `practitioner-notes.md` until it is traced to its primary source and given a row above.
- Revenue, valuation, market-share and user-count figures in `market-landscape.md` §3 and §5. All are [S], several from low-quality aggregators.

## Open verification work (ASSIST-004)

1. Upgrade or drop E-10, E-14, E-17, E-18 and E-23.
2. Re-read the exact wording of each [P] quotation gathered by a sub-agent before it is printed in the proposal.
3. Decide whether the proposal needs any market-size or revenue figure at all. If it does, it needs a primary source that we do not yet have.
