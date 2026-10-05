# Market landscape: AI software-development assistants

| | |
|---|---|
| Research date | 2026-10-03 |
| Method | Web research pass by a Claude Code sub-agent: vendor pricing and documentation pages fetched directly, plus web search for third-party coverage. |
| Status | Record as received. Figures tagged [S] were seen only in search summaries or secondary write-ups and are not verified. Nothing here may be quoted in a CXO document until it has a row in `EVIDENCE.md` tagged [P] or [L]. |
| Used for | PLAN §3.2 (where not to compete), PROPOSAL problem and product sections |

Tags: **[P]** the publisher's own page was fetched on the research date. **[S]** search summary or secondary source only.

### How to read this (source reliability)

- **[P]** = I fetched the vendor's own page today (2026-10-03). These pages are undated; treat them as "as displayed 2026-10-03".
- **[S]** = figure seen only in a search-result summary of third-party coverage. I did not open the primary article; several are low-quality aggregators. **Re-verify any [S] figure before it goes into a CXO document.**
- CNBC and Techzine returned HTTP 403, so the Cursor/SpaceX deal and Meta's coding agent are [S] only.
- The market has changed a lot since mid-2026; several products in your list have been renamed, sold or shut down (noted in the table and section 5).

### 1. Comparison table

| Product (vendor) | Form factor | Models | Published pricing | Deployment | Notable features | Segment | Source |
|---|---|---|---|---|---|---|---|
| GitHub Copilot (Microsoft) | IDE, CLI, cloud agent, PR review | Multi-model; third-party agents (Claude, Codex) inside Copilot | Free; Pro $10 (1,500 AI credits); Pro+ $39 (7,000); Max $100 (20,000); Business $19/seat (1,900); Enterprise $39/seat (3,900) | SaaS | Agent mode, cloud agent, code review, MCP, token-based "AI Credits" since 1 Jun 2026 [S] | All, enterprise default | [P] https://docs.github.com/en/copilot/get-started/plans |
| Claude Code (Anthropic) | CLI, IDE, desktop, web, mobile, Slack, CI | Claude only | Pro $20 ($17 annual); Max from $100; Team $25/seat ($20 annual), Premium $100/seat; Enterprise $20/seat plus usage at API rates | SaaS; third-party cloud providers for CLI/VS Code/JetBrains | Sub-agents, skills, hooks, MCP, auto memory, cloud routines, PR code review, Agent SDK | Pro devs to enterprise | [P] https://claude.com/pricing ; https://code.claude.com/docs/en/overview |
| Codex (OpenAI) | CLI, IDE extension, cloud, desktop, iOS, PR review | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna | Free; Go $8; Plus $20; Pro $100/$200/$500; Business $25/user ($20 annual); Enterprise custom | SaaS; data residency on Enterprise | Slack/GitHub integration, code review, Compliance API audit logs | All | [P] https://learn.chatgpt.com/docs/pricing |
| Cursor (Anysphere, now SpaceX [S]) | IDE, CLI, cloud agents, PR bot (Bugbot) | Frontier models plus Grok, own Composer | Hobby free; Individual $20; Teams $40/user; Enterprise custom | SaaS | Skills, hooks, MCP, cloud agents/automations, usage analytics, audit logs, repo/model/MCP access controls | Pro devs, enterprise | [P] https://cursor.com/pricing |
| Devin / Devin Desktop, formerly Windsurf (Cognition) | Cloud agent, IDE, CLI | OpenAI, Claude, Gemini, SpaceXAI, own SWE-2 | Free; Pro $20; Max $200; Teams $80/mo + $40/dev seat; Enterprise custom | SaaS; VPC on Enterprise | windsurf.com/pricing now redirects to devin.ai | Enterprise, autonomous tasks | [P] https://devin.ai/pricing |
| Antigravity IDE/CLI, Jules (Google) | IDE, CLI, SDK, cloud agent | Gemini, "a variety of agent models" | Free; Google AI Pro/Ultra (prices not on page; $19.99/$99.99/$199.99 [S]); business from $30/seat or pay-as-you-go | SaaS, Google Cloud | Gemini CLI retired for individual accounts 18 Jun 2026 [S] | All, GCP shops | [P] https://antigravity.google/pricing ; [S] https://www.cloudzero.com/blog/google-antigravity-pricing/ |
| Kiro (AWS), replacing Q Developer | IDE, CLI | Claude Sonnet 5, Opus 5, open-weight (DeepSeek, MiniMax, GLM-5, Qwen3 Coder Next) | Free (50 credits); Pro $20 (1,000); Pro+ $40 (2,000); Pro Max $100 (5,000); Power $200 (10,000); overage $0.04/credit | SaaS on AWS | Spec-driven development; Q Developer new sign-ups blocked 15 May 2026, end of support 30 Apr 2027 [S] | AWS shops | [P] https://kiro.dev/pricing/ ; [S] https://enterprisedna.co/resources/news/aws-kiro-replaces-amazon-q-developer-spec-driven-2026/ |
| JetBrains AI / Junie | IDE, CLI | Multi-model; BYOK [S] | AI Free (3 credits); AI Pro $20 (20); AI Ultimate $60 (70); AI Enterprise $60 | SaaS; enterprise on-prem not found | Page dated 22 Jul 2026 | JetBrains users | [P] https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html |
| Amp (Amp Frontier, ex-Sourcegraph) | CLI, IDE | BYOK, or use your own subscriptions | Hobby free (pay-as-you-go); Individual $20; Enterprise custom | SaaS; own runners | Spun out of Sourcegraph Dec 2025 [S]; Cody is enterprise-only [S] | Power users | [P] https://ampcode.com/pricing |
| Replit | Browser IDE, app builder | Not named | Core $20; Pro $100 (10 parallel agents); Enterprise custom | SaaS; single-tenant on Enterprise | Hosting and database bundled | Non-developers, prototyping | [P] https://replit.com/pricing |
| Lovable | App builder | Not found | Plan prices not displayed on page; free tier 5 daily credits; no per-seat charge | SaaS | Plan mode, shared workspace credits | Non-technical builders | [P] https://lovable.dev/pricing |
| Bolt | App builder | Not found | Free (1M tokens/month); Pro $25 (10M); Teams $30/member; Enterprise custom | SaaS | Hosting, SSO/audit logs on Enterprise | Same | [P] https://bolt.new/pricing |
| v0 (Vercel) | App builder | Own model tiers | Free; Plus $30; Business $100; Enterprise custom | SaaS | GitHub sync, design mode | Front-end, product teams | [P] https://v0.app/pricing |
| Cline | IDE extension, CLI, SDK | BYOK, any provider | Open source free; Enterprise custom | Local client, your model endpoint | No inference markup; SSO, RBAC on Enterprise | BYO-model teams | [P] https://cline.bot/pricing |
| OpenHands | Web GUI, CLI, cloud | Model-agnostic, BYOK | Local free (MIT); SaaS free tier; Enterprise custom | Local, SaaS, self-hosted in VPC | At-cost models | Self-hosters | [P] https://www.openhands.dev/pricing |
| opencode | CLI, IDE, desktop | BYOK | Free; Go $10/mo [S] | Local | 209,405 GitHub stars, Sept 2026 [S] | OSS power users | [S] https://www.morphllm.com/comparisons/opencode-vs-cline |
| Aider / Roo Code / Continue | CLI / IDE | BYOK | Free | Local | Aider: no commits since 22 May 2026 [S]. Roo: archived 15 May 2026 [S]. Continue: acquired by Cursor, repo read-only [S] | Declining | [S] https://thenewstack.io/roo-code-cloud-ides-ai-coding/ ; https://www.bodegaone.ai/blog/cursor-acquires-continue-dev |
| Tabnine (now Tricentis) | IDE, CLI, context engine | Not found | Pricing page now redirects to Tricentis contact form; $39 and $59/user [S] | SaaS, VPC, on-prem, air-gapped [S] | Enterprise Context Engine | Regulated enterprise, now testing/SAP | [P redirect] https://www.tabnine.com/pricing/ ; [S] https://finance.yahoo.com/technology/ai/articles/tricentis-acquires-tabnine-further-scale-150000471.html |
| Augment Code | IDE, CLI, cloud | Multi-model | Standard $20/mo; Business $100/mo (usage credit, up to 50 seats); 40% service fee on LLM cost; Enterprise custom | SaaS; multi-region on Enterprise | Context Engine, CMEK, ISO 42001, SIEM | Large codebases | [P] https://www.augmentcode.com/pricing |
| Factory (Droid) | Desktop, CLI, SDK, cloud agents | Frontier and open-weight | Pro $20; Plus $100; Max $200; Teams $60 + $40/seat; Business/Enterprise custom | SaaS; on-prem and data residency on Enterprise | Background agents, "agent-readiness" dashboard | Enterprise | [P] https://factory.com/pricing |
| Qodo | PR bot, IDE | BYOK on Enterprise | Pro Team $30/mo base, $0.012/credit; Enterprise custom | SaaS, single-tenant, on-prem/air-gapped | Agentic code review, rules system | Code review, regulated | [P] https://www.qodo.ai/pricing/ |
| IBM Bob | IDE, agents | Claude, Mistral, Granite; local Nemotron, Poolside Laguna [S] | Not found | SaaS; on-prem, sovereign, air-gapped since 1 Oct 2026 | Vendor claim: 80,000 IBM users, 45% productivity gain [S] | Regulated, mainframe | [P] https://newsroom.ibm.com/2026-10-01-ibm-introduces-self-hosted-deployment-for-ibm-bob-to-help-enterprises-advance-ai-sovereignty-and-governance |
| Others | PR bots, IDE | Varied | CodeRabbit about $24/dev; Greptile $30/seat; GitLab Duo Pro $19/user add-on; Zencoder from $19; Kilo Code Teams $15/user; Mistral Vibe Pro EUR 14.99 (all [S]) | Mistral Devstral self-hostable [S] | — | Niche | [S] https://tech-insider.org/coderabbit-vs-greptile-vs-qodo-2026/ ; https://byteiota.com/mistral-vibe-coding-agent-with-open-weights-and-half-the-cost/ |

### 2. Feature taxonomy

Labels are my judgement from the pricing and docs pages above, not a published classification.

**Table stakes** (present in essentially every serious product):
- Agentic edit-run-test loop, on every plan including Copilot Free.
- MCP support.
- Repo instruction files (AGENTS.md, CLAUDE.md, rules).
- Plan mode; even Lovable prices it.
- IDE plus CLI form factors.
- Background or cloud agents: Copilot, Claude Code, Codex, Cursor, Devin, Factory, Jules.
- PR code review bot: Copilot, Claude Code, Codex, Cursor Bugbot.
- Multi-model choice, on everything except Claude Code and Codex.
- SSO, and zero-training on business data.
- Credit or token metering.

**Emerging** (in the leaders, uneven elsewhere):
- Sub-agents and parallel orchestration (Replit sells "10 parallel agents").
- Skills and plugin marketplaces (Cursor "team marketplace for rules, skills, plugins").
- Hooks.
- Automatic cross-session memory.
- Scheduled or event-triggered agents.
- Slack and mobile entry points.
- Hosting third-party agents inside a platform (GitHub).
- Usage analytics, audit logs, and repo/model/MCP access controls. These are consistently gated to the top enterprise tier.
- Spec-driven development (Kiro's core idea).
- BYO-key in commercial products (JetBrains, Amp, Qodo Enterprise).

**Rare:**
- True air-gapped deployment: IBM Bob, Qodo, Tabnine, and self-hosted open source.
- Local open-weight model support with vendor backing.
- Standalone code-graph or context engine sold separately (Tabnine, Augment).
- "Agent-readiness" assessment (Factory).
- AI code attribution API (Cursor Enterprise).
- Customer-managed encryption keys (Augment).
- Mainframe or legacy-specific tooling (AWS Transform, IBM).

Checkpoints/rewind and sandboxing details were not confirmed on the pages I fetched.

### 3. Where incumbents are structurally strong (do not compete here)

- **Model ownership and subsidy.** Anthropic, OpenAI and Google sell flat subscriptions over their own models. Wrappers pay API rates; Augment publishes its 40% fee on LLM cost. All three now share the same $20 / $100 / $200 ladder.
- **Distribution.** GitHub owns the pull request surface and hosts competitors' agents inside Copilot. Reported Copilot scale is 4.7M paid subscribers as of 28 Jan 2026 [S, https://www.getpanto.ai/blog/github-copilot-statistics]. AWS, Google and Microsoft bundle into cloud commitments.
- **Revenue scale** (all [S], mostly aggregator-reported):
  - Claude Code: $2.5B run-rate in Feb 2026; an $8B figure for May 2026 appears only on aggregators (https://aibusinessweekly.net/p/claude-code-statistics).
  - Cursor: $2B ARR by Feb 2026 (https://getlatka.com/companies/cursor.com).
  - Codex: 5M weekly users in June 2026, per a vendor statement (https://www.gradually.ai/en/codex-statistics/).
- **Market share.** Menlo Ventures put coding at $4B of 2025 departmental AI spend [S, https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/]. The "Anthropic 54% vs OpenAI 21%" split comes from a secondary blog [S, https://valueaddvc.com/blog/openai-vs-anthropic-which-ai-company-is-winning-the-enterprise-in-2026].
- **Feature velocity.** Hooks, skills, sub-agents and cloud agents spread across vendors within months. A general-purpose harness is not defensible.
- **Consolidation of the independent middle.** Continue, Roo, Tabnine, Windsurf, Graphite and Cursor itself have all been absorbed or closed (section 5).

### 4. Candidate underserved segments

**a) Verification and review throughput**
- Evidence: Faros AI telemetry on 22,000 developers (April 2026) reports median time in review up 441.5%, bugs per developer up 54%, incidents per PR up 242.7% [S, https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways ; https://adtmag.com/articles/2026/04/22/more-code-more-bugs.aspx]. Faros sells engineering analytics, so it is an interested party.
- Stack Overflow survey: 84% use or plan to use AI, 46% distrust accuracy, 66% cite "almost right" output [S, https://adtmag.com/blogs/watersworks/2026/01/stack-overflow-survey.aspx]. Coverage labels this both 2025 and 2026; the survey year is unconfirmed.
- Incumbent counter: every major vendor already ships a review bot, Cursor bought Graphite, and Tricentis bought Tabnine for exactly this. It is the most contested "gap".

**b) Air-gapped, sovereign and regulated deployment**
- Evidence: the big-vendor products are SaaS, or VPC at best. IBM cites its own survey that 68% of executives find data residency requirements challenging (IBM Institute for Business Value, June 2026) [P]. That is a vendor claim.
- Tabnine, the best-known air-gapped vendor, has just been folded into a testing company.
- Incumbent counter: IBM shipped air-gapped Bob on 1 Oct 2026. Factory and Qodo offer on-prem. Claude Code runs through third-party clouds. Open-weight models with Cline or OpenHands cost nothing. The gap is narrowing quickly.

**c) Brownfield and legacy modernisation**
- Evidence: DORA's ROI report (11 May 2026) puts AI gains at 35-40% on simple tasks and 10% or less on complex legacy code [P, https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/].
- AWS claims 40M lines of COBOL modernised for Toyota 50% faster (vendor claim) [S, https://aws.amazon.com/blogs/migration-and-modernization/reimagining-mainframe-applications-with-aws-transform-and-claude-code/].
- Incumbent counter: AWS Transform, Anthropic and IBM are all targeting this directly. IBM shares reportedly fell 13% on Anthropic's COBOL announcement of 23 Feb 2026 [S, https://www.artificialintelligence-news.com/news/cobol-modernization-ai-claude-ibm/].

**d) Cost governance and predictability**
- Evidence: Copilot moved to token billing on 1 Jun 2026, with developer backlash [S, https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx].
- A class action over Claude Max caps was filed 15 Jun 2026 in the Northern District of California (reported by BeInCrypto via Yahoo) [P, https://finance.yahoo.com/sectors/technology/articles/anthropic-faces-lawsuit-over-claude-150710669.html].
- Uber reportedly exhausted its annual AI coding budget in four months [S, https://www.forbes.com/sites/janakirammsv/2026/05/26/why-your-engineers-favorite-ai-tools-are-wrecking-your-2026-budget/].
- 53% of Stack Overflow respondents call agent cost a barrier [S].
- Incumbent counter: spend caps, pooled usage and analytics already sit in enterprise tiers. Only a cross-vendor control plane is beyond what incumbents will build themselves.

**e) Vendor-neutral, BYO-model tooling**
- Evidence: opencode's star count; Roo, Continue and Aider leaving a vacuum.
- Incumbent counter: willingness to pay is weak. Cline and opencode are free.

Net: no gap is uncontested. The most defensible combination looks like (b) plus (c) in a specific vertical, where deployment constraints and domain knowledge compound.

### 5. Market events

**Acquisitions and ownership** (all [S] unless marked)
- SpaceX acquired Anysphere (Cursor) for $60B in stock; announced 16 Jun 2026, closed 14 Aug 2026 (https://www.techzine.eu/news/devops/143619/spacex-completes-acquisition-of-cursor/). Cursor's own pricing page listing Grok is consistent with this [P].
- Cursor acquired Continue, announced about 16 Jun 2026, and Graphite in Dec 2025.
- Tricentis acquired Tabnine on 30 Jul 2026. The $500M price comes from a single aggregator and is unverified.
- Cognition bought Windsurf in Jul 2025 and renamed it Devin Desktop on 2 Jun 2026; it is reportedly valued around $25B after a May 2026 raise.
- OpenAI acquired Ona (formerly Gitpod), Astral and Promptfoo. Anthropic acquired Bun (https://aifundingtracker.com/openai-biggest-acquisitions/).

**Shutdowns and replacements**
- Roo Code archived 15 May 2026.
- Gemini CLI retired for individual accounts 18 Jun 2026.
- Amazon Q Developer being replaced by Kiro.
- Amp spun out of Sourcegraph Dec 2025.

**Pricing and limits**
- Copilot AI Credits from 1 Jun 2026; Copilot Max $100 tier added Jul 2026 [S].
- Anthropic's weekly limits were set at +25% from 14 Sep 2026 after a temporary +50%, read by users as a cut [S, https://x.com/AGTPinsights/status/2093745413140492439].
- OpenAI reopened Pro $200 at roughly half the previous usage and added Pro $500 on 29 Sep 2026 [S, https://www.developersdigest.tech/blog/codex-usage-limits-pricing-2026].
- Google cut the top Antigravity tier from $249.99 to $199.99 on 19 May 2026 [S].

**Funding and revenue** (all [S])
- Replit: $9B valuation (Mar 2026), about $525M ARR.
- Lovable: $13.3B valuation (12 Aug 2026).
- OpenHands: $18.8M Series A (Jun 2026). Cline: $32M.
- Anthropic: confidential S-1 reportedly filed 1 Jun 2026.

**New entrant**
- Meta launched a coding agent, "Muse Code", on 5 Aug 2026, per a CNBC headline I could not open.

**Not found:** Cursor and Codex revenue from primary sources; an official Copilot user count for 2026; enterprise pricing for Tabnine or IBM Bob; Lovable plan prices; on-prem options for JetBrains.
