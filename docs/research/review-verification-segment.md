# The AI code review and verification segment

| | |
|---|---|
| Research date | 2026-10-05 |
| Method | Web research by a Claude Code sub-agent from company blogs, docs, pricing pages and press releases. Figures were confirmed in the raw downloaded page, not in a summary. |
| Status | Record as received. Funding and usage figures are the companies' own announcements unless marked otherwise. "How occupied is the space" is the researcher's assessment. |
| Used for | PLAN §3.8, PLAN §2.1 decisions T2 and T3 |

Tags in this file: **[P]** confirmed in the publisher's raw page (downloaded and searched, not a summary); **[P-archive]** read raw from a web-archive capture because the publisher blocked direct download; **[P-summary]** publisher's page seen only through a summarising fetch; **[S]** secondary source or search snippet only.


Tags: **[P]** = read in the named publisher's raw page (curl + grep); **[S]** = secondary source or search snippet only. No figure here rests on a summarising fetch, so [P-summary] is unused. Numbers after a tag point to the numbered "Sources" section, placed before the two closing sections (URL and publication date). "Vendor claim" means the company measured itself.

## Part 1. Funding and scale

| Company | Latest round | Valuation | Lead investors | Published scale figures |
|---|---|---|---|---|
| CodeRabbit | $143M Series C, 2026-08-12 [P1][P2] | $1.5B [P1][P2] | Atomico, Smash Capital (co-leads) [P1] | Vendor claims: revenue up "more than 5x year-over-year"; "more than 2 million code reviews each week"; "more than 17,000 customers" [P1] |
| CodeRabbit (earlier) | $60M Series B, 2025-09-16 [P3]; $16M Series A, 2024-08-13 [P4] | Series B about $550M [S5] | Scale Venture Partners (B) [P3]; CRV (A) [P4] | Vendor claim at Series B: 13 million pull requests reviewed [P3] |
| Greptile | $25M Series A, 2025-09-23 [P6] | Not disclosed by company. TechCrunch reported talks at $30M on a $180M valuation, 2025-07-18, before close [P7] | Benchmark [P6] | Vendor claim: 500M+ lines reviewed and 180,000+ bugs prevented "this month" [P6] |
| Qodo | $70M Series B, 2026-03-30; total $120M [P8] | Not found | Qumra Capital [P8] | Customer names only [S9] |
| Graphite (reviewer first called Diamond) | $52M Series B, 2025-03-17 [P10]; agreement to join Cursor announced 2025-12-19 [P11] | Last valuation $290M [S12]; acquisition price undisclosed [S12] | Accel [P10] | "Diamond" name deprecated 2025-10-08; now "Graphite Agent" [P10] |
| Cursor Bugbot | Part of Cursor; no separate round | n/a | n/a | Vendor claims: resolution rate 78.13% over 50,310 PRs; "hundreds of thousands of PRs per day" [P13] |
| GitHub Copilot code review | Part of GitHub/Microsoft | n/a | n/a | Vendor claims: 60 million reviews; "more than one in five code reviews on GitHub"; actionable feedback in 71% of reviews [P14] |
| Claude Code Review | Part of Anthropic; research preview since 2026-03-09 [P15] | n/a | n/a | Internal Anthropic figures: PRs with substantive comments rose from 16% to 54%; "less than 1% of findings are marked incorrect" [P15] |
| OpenAI Codex code review | Part of OpenAI | n/a | n/a | No usage figure found |
| Macroscope | $30M Series A, 2025-09-17; total $40M [P16][P17] | Not found | Lightspeed [P16] | Not found |
| Baz | $9M seed extension, 2026-06-29; total $17M [P18] | Not found | Battery Ventures, boldstart [P18] | About 100 customers [S19] |
| Ellipsis | $2M seed, 2024-06-19 [P20] | Not found | Y Combinator and angels [P20] | Not found |
| Sourcery | $1.75M seed, 2022 [S21]; nothing newer found | Not found | Forward Partners [S21] | Not found |
| Korbit | $11.3M Series A, 2023 [S22]; a 2026 sale to Boost Security appears in one snippet, unverified [S22] | Not found | Khosla Ventures [S22] | Not found |

Other 2025-2026 raises: Theorem, $6M seed led by Khosla, verifying AI-written code [S23]; Axiom, $200M Series A at $1.6B led by Menlo Ventures, formally verified (Lean) AI output [S24]; CodeAnt AI, $2M seed [S25]; cubic, $800K [S25].

**The "98% / 91%" line.** The original source is Faros AI's "AI Productivity Paradox Report 2025" (2025-07-23; analysis "as of June 2025"): "Developers on teams with high AI adoption complete 21% more tasks and merge 98% more pull requests, but PR review time increases 91%", from telemetry on "over 10,000 developers across 1,255 teams" [P26]. Faros sells engineering analytics, so this is a vendor's observational study, a correlation across teams, and not a review vendor's product claim. The same page reports a 9% increase in bugs per developer and a 154% increase in average PR size [P26]. Third-party blogs repeat it with wrong attributions (LinearB, DORA) [S27]; I did not find it in CodeRabbit's funding release or the Greptile, Qodo or Cursor pages I read. Faros says PR review time rose 91%, which is not the same as developers "spend 91% longer in review".

## Part 2. What the main products do

| | CodeRabbit | Greptile | Qodo | Cursor Bugbot | GitHub Copilot code review | Claude Code Review |
|---|---|---|---|---|---|---|
| (a) When it runs | On the PR; also IDE and CLI before commit; a planning product before work starts [P28][P29] | On the PR; CLI and MCP for local use [P30] | On the PR; "Agentic Toolbox" inside the agent loop [P31] | On the PR, each push by default [P32] | On the PR; also in the IDE [P33] | On the PR; local `/code-review` [P34] |
| (b) Who judges; can it block | LLM, plus 50+ linters and SAST tools run in sandboxes [P35]. Blocks when a check is set to `error` with the request-changes workflow [P36][P37] | LLM. Optional GitHub status check; beta auto-approve after a 5/5 score [P38][P39] | LLM multi-agent review with rules; blocking behaviour not confirmed in the pages read [P31] | LLM. Findings default to `neutral`; a fail-on-unresolved mode exists where available [P32] | LLM. Approvals count toward required reviews only if enabled (public preview); deterministic gating is the separate GitHub Code Quality product (CodeQL, coverage) [P33] | LLM. "The check run always completes with a neutral conclusion so it never blocks merging" [P34] |
| (c) Pre-agreed contract | Partial: "Issue Assessment" checks a PR against linked issues and out-of-scope changes; custom checks in natural language [P36][P40] | Partial: reviews against Jira/Linear issues [P30] | Partial: reads ticket acceptance criteria, reports findings "rather than explicit compliance statuses" [P41] | No (rules files) [P32] | No (instructions) [P33] | No (`REVIEW.md` instructions) [P34] |
| (e) Evidence record | PR comments, check summary, reports, admin audit log [P36][P42] | Comments, analytics [P30] | Comments, governance analytics, audit logs (Enterprise) [P43] | Check run, analytics API [P32] | PR review; audit log [P58] | Check run with machine-readable severity counts [P34] |
| (f) Model-neutral | Reviews any author's code; investor calls it "model-agnostic" [P1] | Reviews any PR; hands fixes to several agents [P30] | BYOK on Enterprise [P43] | Reviews any PR; reviewer is Cursor's | GitHub's "tuned mix of models" [P33] | Reviewer is Anthropic's |
| (g) Deployment | SaaS; self-hosted for Enterprise with 500+ seats [P44] | SaaS; self-host on Enterprise [P45] | SaaS; single-tenant or on-prem/air-gapped on Enterprise [P43] | SaaS | SaaS (github.com) | Managed; own-CI alternative via GitHub Actions [P34] |
| (h) Price | $24/$48/$72 per developer per month billed annually; agent at $0.40 per agent-minute [P46] | $30 per seat per month, 50 credits per seat, extra credits $1 [P45] | Pro Team from $30; $.012 per credit [P43] | "The average Bugbot run costs $1.00-$1.50"; seat fee of $40 removed [P47] | Estimated $0.05 to $1 (Lite) or $0.25 to $5 (Balanced) per review in AI credits, plus Actions minutes [P33] | "Each review averages $15-25" [P34] |

OpenAI Codex code review also runs on the PR, flags "only P0 and P1 issues", and its docs say review rules "don't replace tests, branch protections, or required approvals" [P48].

**(d) Published accuracy.** None of these products publishes a false-pass rate, meaning how often a change it passed later proved wrong. What exists:

- Martian "Code Review Bench" (third party) scores whether review comments matched what developers later changed. Four vendors announced first place on different dates or tracks: CodeRabbit, F1 51.2% and precision 49.2%, 2026-03-03 [P49]; Qodo, F1 64.3% for a research-preview configuration and 47.9% for the production one, 2026-03-15 [P50]; cubic, F1 65.7%, 2026-03-25 [P51]; Greptile, F1 60.8%, precision 76.2%, recall 50.6%, 2026-07-30 [P52]. I did not read Martian's own leaderboard; these are vendor restatements.
- Vendor-run benchmarks: Greptile, 82% catch rate on 50 bugs, with false positives not scored [P53]; Qodo, F1 60.1% on 100 PRs with LLM-injected defects [P54]; Macroscope, 48% detection and 98% precision on 118 bugs [P55].
- Field proxies: Cursor's "resolution rate" (78.13%) is judged by an LLM at merge time; Cursor treats unresolved findings as false positives [P13][P56].

One limit matters for our idea: CodeRabbit's custom checks are decided by an LLM agent and cannot "run your test suite" or "execute arbitrary repository code" [P40].

## Part 3. Vendor audit logs

- **GitHub Copilot.** "You can apply the `actor:Copilot` filter to your enterprise audit log to view agentic activity over the last 180 days" [P57]. "The audit log retains events for the last 180 days" [P58]. So 180 days is confirmed as the general enterprise audit-log retention; GitHub recommends streaming to a SIEM for longer history [P58]. Fields include `action` (for example `pull_request.create`), `actor_is_agent`, `agent_session_id` and `user` [P57]. The log "does not include client session data, such as the prompts a user sends to Copilot locally" [P58].
- **Claude.** The Compliance API gives "programmatic access to their organization's Activity Feed" and, for Enterprise, chats, files, projects and Claude Code sessions [P59]. Claude Code's OpenTelemetry export has events for user prompts, tool results, tool decisions and API requests, and counters for sessions, lines of code, pull requests, commits, cost and tokens; prompt text, tool arguments and tool content are redacted unless specific variables are set [P60]. Retention: not found.
- **Cline.** OpenTelemetry events include `task.tool_used` ("tool_name, success, duration_ms, auto_approved"), `task.terminal_execution` ("success, command_hash, duration_ms") and `task.completed` [P61]. Cline's separate product telemetry "never" includes code, file paths or command arguments [P62].

All three record what the agent did and what it cost. None records whether the resulting change was verified or correct; the nearest fields are tool-call success flags and PR counts.

## Part 4. Closest to our idea

- **CodeRabbit "Agentic Change Management"** (2026-08-12): validation, a "Triage" product that "scores changes according to value, urgency, risk, dependencies, readiness, and reviewer fit, then directs consequential work to human reviewers, routes low-risk changes into automated workflows", and rules that squash-merge low-risk PRs "after required checks and reviews pass" [P1][P63]. It calls the PR "the auditable decision point" [P1]. This is our risk routing, on sale now; Triage rules need the Team plan at $48 [P63][P46].
- **Sonar**: a deterministic quality gate "optimized for agent centric development" enforcing six conditions on new code [P64], and Sonar Vortex, which "injects the right project context and constraints before the first line of code, then verifies every change in real time with SonarQube's algorithmic analysis" [P65]. This is deterministic verification outside the model, limited to static analysis.
- **Baz Planner** (2026-06-29): review moved to the plan before code is written [P18].
- **Faros AI**: "benchmarks from your own merged code" that re-run shipped work under different models and harnesses to cut "cost per verified outcome" (2026-09-21) [P66]. This is per-repository agent measurement without a gate.
- **Open source**: agent-spec, which turns requirements into "Task Contracts" and "mechanically verifies the implementation" (457 stars) [P67]; agents-shipgate, "the deterministic merge gate for AI-generated agent capability changes" (89 stars) [P68]; an in-toto predicate proposal of 2026-09-30 for AI code-generation provenance, including "the machine acceptance contract that gated the artifact (embedded as re-runnable checks...)" and human sign-offs [P69]. Funding: not found.

## Sources

Format: publication date, then URL. "undated" marks living docs and pricing pages, all read 2026-10-05.

1. 2026-08-12 (Business Wire release via Yahoo Finance; businesswire.com blocked): https://finance.yahoo.com/technology/ai/articles/coderabbit-raises-143-million-1-130000002.html
2. 2026-08-12: https://www.coderabbit.ai/newsroom/reuters-coderabbit-valued-at-1-5-billion
3. 2025-09-16: https://www.coderabbit.ai/blog/coderabbit-series-b-60-million-quality-gates-for-code-reviews
4. 2024-08-13: https://www.coderabbit.ai/blog/coderabbit-announces-16m-series-a-funding-led-by-crv
5. 2025-09: https://mlq.ai/news/coderabbit-raises-60-million-series-b-valuation-hits-550-million/
6. 2025-09-23: https://www.greptile.com/blog/series-a
7. 2025-07-18: https://techcrunch.com/2025/07/18/benchmark-in-talks-to-lead-series-a-for-greptile-valuing-ai-code-reviewer-at-180m-sources-say/
8. 2026-03-30: https://techcrunch.com/2026/03/30/qodo-bets-on-code-verification-as-ai-coding-scales-raises-70m/
9. 2026-03-30: https://siliconangle.com/2026/03/30/ai-generated-code-verification-startup-qodo-raises-70m/
10. 2025-03-17: https://graphite.com/blog/series-b-diamond-launch
11. 2025-12-19: https://graphite.com/blog/graphite-joins-cursor
12. 2025-12 (Fortune, citing Axios): https://finance.yahoo.com/news/exclusive-cursor-acquires-code-review-153008616.html
13. 2026-04-08: https://cursor.com/blog/bugbot-learning
14. 2026-03-05: https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/
15. 2026-03-09: https://claude.com/blog/code-review
16. 2025-09-17: https://macroscope.com/blog/introducing-macroscope
17. 2025-09-17: https://www.cnbc.com/2025/09/17/periscopes-beykpour-raises-40-million-for-macroscope-to-track-code.html
18. 2026-06-29: https://baz.ai/resources/news/baz-announces-planner-and-extended-seed-round
19. 2026: https://www.calcalistech.com/ctechnews/article/cl8og4qtn
20. 2024-06-19: https://www.ellipsis.dev/blog/ellipsis-raises-a-2m-seed-round
21. 2022-01-14: https://tech.eu/2022/01/14/working-its-magic-code-refactoring-platform-sourcery-closes-1-75-million-in-seed-funding/
22. 2023-05: https://www.einpresswire.com/article/636642258/korbit-closes-11-3-million-and-launches-ai-mentor-for-software-engineering
23. 2026-01 (page download failed): https://venturebeat.com/security/theorem-wants-to-stop-ai-written-bugs-before-they-ship-and-just-raised-usd6m
24. 2026-03-12: https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/
25. 2025-05-08: https://fintech.global/2025/05/08/ai-code-review-platform-codeant-ai-raises-2m-to-speed-up-software-development/ ; https://startupintros.com/orgs/cubic-ai
26. 2025-07-23: https://www.faros.ai/blog/ai-software-engineering
27. 2026: https://codeant.ai/blogs/best-ai-code-review-tools ; https://www.buildmvpfast.com/blog/best-ai-code-review-tools-anthropic-2026
28. undated: https://docs.coderabbit.ai/llms.txt
29. undated: https://docs.coderabbit.ai/overview/coderabbit-plan.md
30. undated: https://www.greptile.com/docs/llms.txt
31. 2026-08-12 (page modified): https://docs.qodo.ai/code-review/overview ; index https://docs.qodo.ai/llms.txt
32. undated: https://cursor.com/docs/bugbot
33. undated: https://docs.github.com/en/copilot/concepts/agents/code-review
34. undated: https://code.claude.com/docs/en/code-review.md
35. undated: https://docs.coderabbit.ai/tools/index.md
36. undated: https://docs.coderabbit.ai/pr-reviews/pre-merge-checks.md
37. undated: https://docs.coderabbit.ai/pr-reviews/request-changes-workflow.md
38. undated: https://www.greptile.com/docs/code-review/greptile-json-reference.md
39. undated: https://www.greptile.com/docs/code-review/auto-approve-prs.md
40. undated: https://docs.coderabbit.ai/pr-reviews/custom-checks.md
41. 2026-09-24 (page modified): https://docs.qodo.ai/integrations/ticketing-integrations
42. undated: https://docs.coderabbit.ai/management/audit-logs.md
43. undated: https://www.qodo.ai/pricing/
44. undated: https://docs.coderabbit.ai/self-hosted/overview.md
45. undated: https://www.greptile.com/pricing
46. undated: https://www.coderabbit.ai/pricing
47. 2026-05-11: https://cursor.com/blog/may-2026-bugbot-changes
48. undated: https://developers.openai.com/codex/cloud/code-review
49. 2026-03-03: https://www.coderabbit.ai/blog/coderabbit-tops-martian-code-review-benchmark
50. 2026-03-15: https://www.qodo.ai/blog/qodo-ranked-1-ai-code-review-tool-in-martians-code-review-benchmark/
51. 2026-03-25: https://www.cubic.dev/blog/cubic-is-the-best-ai-code-reviewer-on-martian-s-benchmark
52. 2026-07-30: https://www.greptile.com/content-library/greptile-martian-code-review-benchmark
53. undated: https://www.greptile.com/benchmarks
54. 2026-02-04: https://www.qodo.ai/blog/how-we-built-a-real-world-benchmark-for-ai-code-review/
55. undated: https://macroscope.com/content/best-ai-code-review-tools-github-2026
56. 2026-01-15: https://cursor.com/blog/building-bugbot
57. undated: https://docs.github.com/en/copilot/reference/agentic-audit-log-events
58. undated: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs
59. undated: https://platform.claude.com/docs/en/manage-claude/compliance-api.md
60. undated: https://code.claude.com/docs/en/monitoring-usage.md
61. undated: https://docs.cline.bot/enterprise-solutions/monitoring/opentelemetry-events.md
62. undated: https://docs.cline.bot/enterprise-solutions/monitoring/telemetry.md
63. undated: https://docs.coderabbit.ai/triage/rules.md
64. undated: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gate-for-agentic-ai
65. undated: https://www.sonarsource.com/products/sonar-vortex/
66. 2026-09-21: https://www.faros.ai/blog/ai-route-optimization
67. 2026-03-07 (repo created): https://github.com/ZhangHanDong/agent-spec
68. 2026-04-25 (repo created): https://github.com/ThreeMoonsLab/agents-shipgate
69. 2026-09-30: https://github.com/in-toto/attestation/issues/604

## How occupied is the space

**Already sold by funded companies.** Review on the PR (every product above). Risk scoring, routing to humans and auto-merge of low-risk changes (CodeRabbit Triage, Greptile auto-approve, Copilot approvals). Merge blocking (CodeRabbit, Bugbot, GitHub rulesets). Checking a change against a linked ticket and flagging out-of-scope edits (CodeRabbit, Qodo, Greptile). Pre-work planning (CodeRabbit Plan, Baz Planner). Per-repository measurement of agent output and cost (Faros). Deterministic gates for agent code (Sonar).

**Not found as a product.** A machine-checkable contract (scope, acceptance checks, budget) agreed before the agent runs and enforced afterwards. Verification that is deterministic end to end: the leaders' verdicts are LLM judgments, and CodeRabbit's custom checks cannot run the test suite. A signed, portable evidence bundle per change; this exists only as a week-old in-toto proposal. A per-repository false-pass rate for the verifier; vendors publish precision and recall of comments, and four claim first place on the same benchmark.

**Best argument that an incumbent closes the gap within a year.** CodeRabbit has $143M of new capital, a stated position as "the control layer", 17,000 customers, sandboxes that already run 50+ deterministic tools, a planning product that produces the "before" artifact, issue-scope checks and risk routing. Joining these into a contract-then-evidence flow is product work on parts it owns, and its release already mentions "evidence from isolated test environments" [P1]. GitHub is the other candidate: it owns checks, rulesets, the audit log and the agent. The counter-argument is incentive: every funded reviewer sells LLM judgment, and none has published its own false-pass rate.

## Corrections to Pedro's notes

1. "CodeRabbit $1.5B ($25M Series A...)" merges two companies. $1.5B is CodeRabbit's valuation at its $143M Series C of 2026-08-12 [P1][P2]. CodeRabbit's Series A was $16M, led by CRV, on 2024-08-13 [P4]. The $25M Series A is Greptile's, led by Benchmark, on 2025-09-23 [P6].
2. "98% more PRs, 91% longer in review" is not a review vendor's claim. It comes from Faros AI's July 2025 telemetry report, and the 91% is an increase in PR review time [P26].
3. "Review/verification is the hot funded segment" holds: $143M + $70M + $25M = $238M went into CodeRabbit, Qodo and Greptile between 2025-09 and 2026-08 [P1][P8][P6]. The funded products are LLM reviewers moving toward governance, not deterministic verifiers.
4. The "180-day" Copilot figure is correct, as audit-log retention [P58].
5. Vendor audit logs record agent actions and cost; none records whether the change was correct [P57][P60][P61].
