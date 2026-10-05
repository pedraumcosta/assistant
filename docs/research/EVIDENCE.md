# Evidence ledger

Every figure or quotation that a document in this repo relies on has a row here. The rule from `docs/PLAN.md` §5: no number is invented or estimated, and only rows tagged **[P]** or **[L]** may appear in a CXO-facing document.

| Tag | Meaning |
|---|---|
| [P] | Read on the publisher's own page on the research date |
| [L] | Read in a PDF copy of the published report held in Pedro's files. The PDF is not redistributed in this repo |
| [S] | Seen only in a search summary or secondary write-up. Not verified; must be upgraded to [P] or dropped |
| [P-archive] | Read raw from a web-archive capture because the publisher blocked direct download |

A caution applies to the [P] rows numbered E-01 to E-29 that were gathered by a research sub-agent: the page was fetched through a tool that summarises with a small model, so the exact wording of a quotation should be re-read at the source before it is printed in the proposal. Rows E-30 to E-37, E-40 to E-45, E-59 to E-61, E-73 and E-74 were read directly from the source text by the main session and do not carry that caution; E-38 and E-39 were checked against the downloaded text. Rows E-17, E-46 to E-58 and E-62 to E-72 were confirmed by sub-agents in the raw downloaded page or the full text.

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
| E-17 | "Margins on all of the 'code gen' products are either neutral or negative. They're absolutely abysmal", said by Nicholas Charriere, founder of Mocha | TechCrunch, 2025-08-07 | [P] | Independent press, quoting a founder | https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/ |
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
| E-59 | The 90-line listing "is not a drop-in library; it is a scaffold to be copied and specialized." It has four tools (bash, read_file, write_file, search_replace), `max_turns = 50`, `max_cost = 5.00`, and compaction at 120,000 estimated tokens | as E-30, §16.10, Listing 3 (read in the PDF) | [P] | as E-30 |
| E-60 | On benchmark scores across harnesses: "These figures are not directly comparable (different underlying models, different evaluation runs, different deployment configurations…) and we do not draw a head-to-head conclusion from them." | as E-30, §13.4 | [P] | as E-30 |
| E-61 | Omnigent's policy plane has "CEL (Common Expression Language), Python, or LLM-classifier evaluators" and is "enforced on foreign harnesses through each vendor's own extension mechanism" | as E-30, §14.4 | [P] | as E-30 |

## Self-evaluation and the rising capability floor

Both sources are the model vendor's own engineering blog. Run figures are single runs reported by the author, not a study.

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-34 | "agents reliably skew positive when grading their own work" | Anthropic, "Harness design for long-running application development", 2026-03-24 | [P] | Vendor | https://www.anthropic.com/engineering/harness-design-long-running-apps |
| E-35 | "the evaluator is still an LLM that is inclined to be generous towards LLM-generated outputs" | as E-34 | [P] | Vendor | as E-34 |
| E-36 | "the evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo." | as E-34 | [P] | Vendor | as E-34 |
| E-37 | Same prompt, one run each: solo agent "20 min", "$9"; full harness "6 hr", "$200"; "The harness was over 20x more expensive". The solo build's central feature did not work; the harness build was playable | as E-34 | [P] | Vendor | as E-34 |
| E-38 | "By May 2025, Claude 3.7 Sonnet had already crept up to the point where over 50% of candidates would have been better off delegating to Claude Code entirely." | Anthropic, "Designing AI-resistant technical evaluations", 2026-01-21 | [P] | Vendor | https://www.anthropic.com/engineering/AI-resistant-technical-evaluations |
| E-39 | "Human experts retain an advantage over current models at sufficiently long time horizons." | as E-38 | [P] | Vendor | as E-38 |

## Published framing we build on

A single-author synthesis with no new measurements. These rows are the paper's own definitions and statements, read directly from its text. The figures it cites from other studies are not in this ledger; they are listed in `paper-verification-economics.md` and are [S] until checked at their sources.

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-40 | "the useful question is no longer how much code an agent can generate, but how much production-qualified value an engineering system can deliver per dollar, per reviewer-hour, and per unit of operational risk" | Bhati, arXiv 2609.04681v1, September 2026 | [P] | Independent author | https://arxiv.org/abs/2609.04681 |
| E-41 | Production-Qualified Change: "A candidate change i receives PQC credit only if it satisfies the organization's relevant qualification vector" | as E-40, §8 | [P] | as E-40 | as E-40 |
| E-42 | Verification Tax: CI, review, security and rework cost over generation cost. "A low Verification Tax can be dangerous if it results from skipping tests or rubber-stamping reviews." | as E-40, §10 | [P] | as E-40 | as E-40 |
| E-43 | "if one model generates the change and another model approves it, what independent evidence remains?" | as E-40, §5 | [P] | as E-40 | as E-40 |
| E-44 | "In agentic pipelines, the verifier itself must be treated as a first-class artifact." | as E-40, §6 | [P] | as E-40 | as E-40 |
| E-45 | "The proposed constructs - PQC, Verification Tax, Agentic Autonomy Budget, and the Control Plane - are not claimed as validated standards. They are hypotheses intended to make future studies comparable." | as E-40, §19 | [P] | as E-40 | as E-40 |

## Competitors and the verification segment

Confirmed in the raw downloaded page on 2026-10-05. Company figures are the companies' own announcements.

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-46 | SpaceX completed the acquisition of Anysphere (Cursor) on 2026-08-14 for 389,289,254 Class A shares, implied equity value 60.0 billion USD | SEC Form 8-K; see `check-market-claims.md` item B1 | [P] | Regulatory filing | see record |
| E-47 | "Cognition has raised over $2B at a $48B valuation"; run-rate revenue "from $492M to almost $900M" since May | Cognition blog, 2026-09-08 | [P] | Vendor | see `check-market-claims.md` item A6 |
| E-48 | "Claude Code's run-rate revenue has grown to over $2.5 billion" | Anthropic, 2026-02-12 | [P] | Vendor | see `check-market-claims.md` item B2 |
| E-49 | CodeRabbit raised a 143 million USD Series C at a 1.5 billion USD valuation and launched "Agentic Change Management" as "the control layer"; claims "more than 17,000 customers" and "more than 2 million code reviews each week" | CodeRabbit release, 2026-08-12 | [P] | Vendor | see `review-verification-segment.md` |
| E-50 | CodeRabbit's custom checks cannot "run your test suite" or "execute arbitrary repository code" | CodeRabbit documentation | [P] | Vendor | see `review-verification-segment.md` |
| E-51 | Claude Code's review check "always completes with a neutral conclusion so it never blocks merging" | Anthropic documentation | [P] | Vendor | see `review-verification-segment.md` |
| E-52 | "Developers on teams with high AI adoption complete 21% more tasks and merge 98% more pull requests, but PR review time increases 91%" | Faros AI, AI Productivity Paradox Report 2025, 2025-07-23 | [P] | Vendor (sells measurement) | https://www.faros.ai/blog/ai-software-engineering |
| E-53 | No vendor audit log examined (GitHub Copilot, Claude Code, Cline, Cursor) records whether an agent's change was verified or accepted; they record actions and cost | Vendors' official documentation, read 2026-10-05 | [P] | Our reading of vendor docs | see `check-procurement-claims.md` |
| E-54 | Anthropic's newest models "require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic" | Anthropic documentation, read 2026-10-05 | [P] | Vendor | https://platform.claude.com/docs/en/manage-claude/api-and-data-retention |
| E-55 | The EU AI omnibus "entered into force on 27 July 2026"; Annex III high-risk obligations moved to 2 December 2027 | European Commission AI Act page | [P] | Regulator | see `check-market-claims.md` item A4 |

## A stated counter-position

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-56 | "Humans may review pull requests, but aren't required to. Over time, we've pushed almost all review effort towards being handled agent-to-agent." | OpenAI, "Harness engineering: leveraging Codex in an agent-first world", 2026-02-11 | [P-archive], capture of 2026-09-24 | Vendor | https://openai.com/index/harness-engineering/ |
| E-57 | "The repository operates with minimal blocking merge gates. … In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive." Followed by: "This would be irresponsible in a low-throughput environment." | as E-56 | [P-archive] | Vendor | as E-56 |
| E-58 | "Harness design is thus a conditional systems problem in which each component should be selected for the target model, task type, and resource budget rather than adopted as a default." | Fan et al., arXiv 2609.20804, 2026-09-17 | [P] | Academic | https://arxiv.org/abs/2609.20804 |

## Decision models

The product is three weeks old. None of these rows concerns judgments about code.

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-62 | Jev: "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE"; "The Services are hosted in the United States"; "64k tokens per request; 32k tokens for `state` plus the longest question" | TypeSafe AI documentation and privacy policy, read 2026-10-05 | [P] | Vendor | https://docs.typesafe.ai/models |
| E-63 | "On Jev's most confident errors, 96.0% of LLM verdicts repeat its answer, against 50.3% under independence." Text rubrics only | Rao and Callison-Burch, arXiv 2609.29769, 2026-09-24 | [P] | Academic | https://arxiv.org/abs/2609.29769 |
| E-64 | "Use a Jev-first cascade to lower cost, and expect little gain in accuracy" | as E-63, Appendix P | [P] | Academic | as E-63 |
| E-65 | Post-hoc calibration: calibration error "0.117" raw, "0.008" with isotonic regression; "a few hundred labeled examples is enough to get most of the benefit". One constructed sentiment dataset | AnthusAI/Jev-Calibration repository | [P] | Independent project | see `check-decision-model-risks.md` item R2 |
| E-66 | "Jev matched the oracle on all 500 repeated decisions." Five frozen agent runs, one reviewer's labels; "not a general ranking of judge accuracy" | LangChain blog | [P] | Vendor of evaluation tooling | see `check-decision-model-product.md` item 4 |

## Brownfield work and the limits of fixed checks

| ID | Claim, as published | Source and date | Tag | Interest | URL |
|---|---|---|---|---|---|
| E-67 | "only 28 of 520 runs ( 5.4% ) pass all three stages, 13 of the 20 tasks receive no accepted solution" | Hong et al., SWE Refactor Bench, arXiv 2608.23564, August 2026 | [P] | Academic | https://arxiv.org/abs/2608.23564 |
| E-68 | Of runs passing every fixed behavioural check: 30 had not migrated ("Stage II gives all 30 full marks; only Stage I stops them"); of the 88 that had, "only 28 survived all six verifiers; the other 60 ( 68.2% ) had a counterexample found against them within the hour" | as E-67 | [P] | Academic | as E-67 |
| E-69 | The completeness audit is a model judge: "Judge and human agree 89.7% of the time ( 140/156, κ=0.795 )". The counterexample search depends on the panel: "retire the two strongest and the remaining four would accept 46 submissions instead of 28" | as E-67 | [P] | Academic | as E-67 |
| E-70 | "a 35–40% productivity gain on simple, greenfield tasks, its impact on complex, legacy brownfield code is often 10% or less" | DORA, ROI of AI-assisted Software Development, v.2026.1, citing Stanford research | [P] | Vendor-run (Google) | https://services.google.com/fh/files/misc/dora-roi-of-ai-assisted-software-development-2026.pdf |
| E-71 | Legacy-Bench: pass rates "from 16.9% to 42.5% across the 12 model-agent combinations"; "In 97% of failures, the agent believes it has solved the task" | Factory, 2026-04-01 | [P] | Vendor (sells a coding agent) | see `brownfield-market.md` Part 2 |
| E-72 | VB6 to C# case study: "the agent scored 70% equivalence across the 331 instructions evaluated", assessed by hand by the system's maintainer; one system, twelve features | Alves, Politowski and Montandon, arXiv 2608.28972, August 2026 | [P] | Academic | https://arxiv.org/abs/2608.28972 |
| E-73 | "When an agent is the one making them pass, don't let that same session be the only author of the tests. Pin the behavior first, in a separate pass or by a person" | Addy Osmani, "Brownfield Agentic Engineering", 2026-09-14 | [P] | Practitioner | https://addyo.substack.com/p/brownfield-agentic-engineering |
| E-74 | "Autonomy should follow blast radius, observability, and recoverability. A model's confidence is a poor guide." | as E-73 | [P] | Practitioner | as E-73 |

## Not usable as evidence

- Every figure in `articles/` that does not have a row above. They are the authors' own claims; several run transcripts are inconsistent with the code shown beside them.
- Every figure in `practitioner-notes.md` until it is traced to its primary source and given a row above.
- Every figure in `paper-verification-economics.md` that it cites from another study, and the "84–97%" velocity figure in `paper-governed-ai-engineering.md`, which is modelled from assumed inputs.
- Every claim in `notion-notes-2026-10-01.md` marked "not checked", including everything from the article that could not be found.
- Revenue, valuation, market-share and user-count figures in `market-landscape.md` §3 and §5. All are [S], several from low-quality aggregators.

## Open verification work (ASSIST-004)

1. Upgrade or drop E-10, E-14 and E-18. E-17 was confirmed on 2026-10-05. E-23 is confirmed in `check-harness-and-repo-claims.md` item P2 and can be upgraded when its row is rewritten with the exact wording.
2. Re-read the exact wording of each [P] quotation gathered by a sub-agent before it is printed in the proposal.
3. Decide whether the proposal needs any market-size or revenue figure at all. If it does, it needs a primary source that we do not yet have.
