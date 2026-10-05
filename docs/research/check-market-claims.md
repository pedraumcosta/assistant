# Check of market claims in Pedro's web research notes

| | |
|---|---|
| Notes dated | 2026-10-01 |
| Checked on | 2026-10-05 |
| Method | Each claim checked at the most primary source reachable by a Claude Code sub-agent, with figures confirmed in the raw page. Bloomberg, Forbes, OpenAI's site, EUR-Lex and SEC full-text search blocked direct access; affected items are marked. |
| Status | Record as received. Section A resolves six conflicts between the notes and our earlier records. |
| Used for | PLAN §3.8; corrections to `market-landscape.md` and `EVIDENCE.md` |

Tags in this file: **[P]** confirmed in the publisher's raw page (downloaded and searched, not a summary); **[P-archive]** read raw from a web-archive capture because the publisher blocked direct download; **[P-summary]** publisher's page seen only through a summarising fetch; **[S]** secondary source or search snippet only.


Tags: **[P]** confirmed in the publisher's raw page (curl + grep); **[P-summary]** publisher's page seen only via a summarising fetch; **[S]** secondary only. Blocked on every attempt (HTTP 403 or empty body): bloomberg.com, forbes.com, openai.com/index, grandviewresearch.com, EUR-Lex, EDGAR full-text search. No [P-summary] items resulted: every summarising fetch of a blocked page also failed.

## Section A — conflicts with our records

### A1. Stack Overflow Developer Survey
**Claim:** "Stack Overflow 2026: 84% use AI, trust 29% and falling, 66% 'almost right but not quite'; most-experienced trust least."
**Finding: Corrected — our record is right.**
- 2026 results are not published. `survey.stackoverflow.co/2026` and `/2026/ai` return 404; the survey index lists 2025 as the newest year. Stack Overflow's blog, 30 Sept 2026: "We are on the precipice of brand new results from the 2026 Developer Survey." [P]
- 2025 figures [P]: "84% of respondents are using or planning to use AI tools" (note: *using or planning to use*); "More developers actively distrust the accuracy of AI tools (46%) than trust it (33%), and only a fraction (3%) report 'highly trusting' the output." Chart values: Highly trust 3.1%, Somewhat trust 29.6%, Somewhat distrust 26.1%, Highly distrust 19.6%. Frustration "cited by 66% of developers" is "AI solutions that are almost right, but not quite".
- "29%": no 2025 headline trust figure is 29%. Two candidates on the 2025 page: "Somewhat trust 29.6%" (one component of the 33%), or the complex-tasks question ("In 2024, 35% of professional developers already believed that AI tools struggled with complex tasks. This year, that number has dropped to 29%"). Either way it is a 2025 number, not a 2026 trust figure.
- "Most-experienced trust least" is supported for 2025: "lowest 'highly trust' rate (2.6%) and the highest 'highly distrust' rate (20%)".
- Sources: https://survey.stackoverflow.co/2025/ai ; https://stackoverflow.blog/2026/09/30/getting-ready-for-2026-results-a-look-back-on-developer-survey-findings/

### A2. "98% more PRs, 91% longer in review"
**Claim:** "claimed, directionally per DORA".
**Finding: Corrected — our record is right.** The source is Faros AI, "The AI Productivity Paradox Report 2025", published 2025-07-23 [P]: "Developers on teams with high AI adoption complete 21% more tasks and merge 98% more pull requests, but PR review time increases 91%"; "a 9% increase in bugs per developer and a 154% increase in average PR size". The DORA 2025 report PDF contains neither figure. Precision: 91% is an increase in *PR review time*, and the comparison is teams with high AI adoption.
- Source: https://www.faros.ai/blog/ai-software-engineering

### A3. DORA 2025 and "verification tax"
**Claim:** "DORA 2025: throughput up but delivery instability rising; 'verification tax'".
**Finding: Partly confirmed.**
- Throughput/instability is confirmed in the report PDF [P]: "AI adoption now improves software delivery throughput, a key shift from last year. However, it still increases delivery instability."
- "Verification tax" does **not** appear in the 2025 report (0 matches in the full PDF text, whitespace-normalised; nearest wording is "verification and coordination costs").
- Earliest use found is DORA's own later insight article "Balancing AI tensions" (dora.dev; the only date on the page is March 10, 2026) [P]: "The verification tax: Time saved writing is often re-spent auditing … constantly moderated by a hidden verification tax." So the phrase is DORA's, but from 2026 commentary, not the 2025 report.
- Later uses: SoftwareSeni, 18 Aug 2026 (attributes it to DORA) [P]; Bhati, arXiv 2609.04681, lists "Verification Tax" as one of its proposed concepts [P]. A search-result summary says DORA's 2026 ROI report also uses it [S, not opened]. No use earlier than March 2026 was found; original coiner not established.
- Neither side had it fully: the Pedro's attribution to DORA 2025 is wrong for the phrase; our record's Sept 2026 date is not the earliest use.
- Sources: https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf ; https://dora.dev/insights/balancing-ai-tensions/ ; https://arxiv.org/abs/2609.04681

### A4. EU AI Act timing
**Claim:** "GPAI transparency (Aug 2025) + high-risk obligations (Aug 2026)".
**Finding: Corrected — our record is right** (the GPAI half of the note is correct).
- European Commission AI Act page [P]: the AI Omnibus "was adopted on 19 November 2025, a political agreement was reached on 7 May 2026 and entered into force on 27 July 2026." "The rules for high-risk use cases in certain sensitive areas (Annex III) have been extended to 2 December 2027"; systems embedded in regulated products (Annex I) "have an extended transition period until 2 August 2028".
- Same page: "the governance rules and the obligations for GPAI models became applicable on 2 August 2025"; "The transparency rules of the AI Act will come into effect in August 2026." A new prohibition added by the Omnibus applies from December 2026.
- Gibson Dunn alert, 27 May 2026 (pre-adoption) [P]: Annex III "by 2 December 2027", Annex I "by 2 August 2028"; Article 50 "proceeds as scheduled, with a proposed four-month grace period for existing systems under Article 50(2)" (until 2 December 2026).
- The Commission page links the final text as `OJ:L_202601744`; "Regulation (EU) 2026/1744, signed 8 July 2026" and "Council approval 29 June 2026" are [S] only (EUR-Lex returned an empty body).
- Sources: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

### A5. GitHub stars (GitHub REST API, queried 2026-10-05 ~14:45 UTC) [P]
**Claim:** opencode "~165k stars"; Aider "no commits since 2026-05-22".
**Finding: Corrected on stars — our record is closer; Aider date confirmed.**

| Repo (as resolved by the API) | Stars |
|---|---|
| anomalyco/opencode (`sst/opencode` redirects here) | 211,831 |
| opencode-ai/opencode (different project; archived) | 13,787 |
| cline/cline | 69,872 |
| Aider-AI/aider | 49,374 |
| OpenHands/OpenHands (`All-Hands-AI/OpenHands` redirects here) | 90,022 |

Aider's default branch (`main`): latest commit 5dc9490b, committer date 2026-05-22T14:02:20Z, matching the repo's `pushed_at`. The Pedro's date is right.

### A6. Cognition
**Claim:** "round closed >? at ?48B" plus a Bloomberg URL on $1B annualised revenue.
**Finding: Confirmed for Pedro's notes; our record is stale** (though accurate for May).
- Cognition blog, 8 Sept 2026 [P]: "Cognition has raised over $2B at a $48B valuation", "led by Andreessen Horowitz and Accel"; "Since our last round in May, Cognition's run-rate revenue has grown from $492M to almost $900M." TechCrunch, same day [P], says "$2 billion at a $48 billion valuation".
- May round: TechCrunch, 27 May 2026 [P]: "more than $1 billion at a $25 billion pre-money valuation ($26 billion post money)".
- $1B annualised revenue: the Bloomberg article (25 Sept 2026) is paywalled (403). Startup Fortune, 27 Sept 2026 [S], reports Bloomberg as saying Cognition "hit $1 billion in annualized revenue this month". The highest company-stated figure is "almost $900M".
- Windsurf rename confirmed: Cognition blog "Introducing Devin Desktop", 06.02.26: "Devin Desktop - the next generation of Windsurf." [P]
- Sources: https://cognition.com/blog/series-e ; https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/ ; https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/ ; https://cognition.com/blog/introducing-devin-desktop

## Section B — competitive snapshot

### B1. Cursor / SpaceX
**Finding: Confirmed** (pricing partly). SEC Form 8-K, Space Exploration Technologies Corp., date of report August 14, 2026 [P]: merger agreement of June 16, 2026 with Anysphere, Inc.; "on August 14, 2026 (the 'Effective Time'), the Merger became effective"; Cursor shares converted into "an aggregate of 389,289,254 shares of the Company's Class A common stock, based on an implied equity value of Cursor of $60.0 billion". Class A trades as "SPCX" on "The Nasdaq Stock Market LLC" and "Nasdaq Texas, LLC". CNBC, 16 June 2026 [P]: "$60 billion worth of stock"; "Musk merged SpaceX with his AI startup, xAI, earlier this year." The Bloomberg URL is paywalled, not read.
Pricing (cursor.com/pricing, monthly view) [P]: Individual "$20 / mo."; Teams "$40 / user / mo." with a Standard/Premium toggle (Premium price not visible in the static page); Enterprise "Custom" with "Pooled usage". A "$60" tier and the name "Business" were not found.
- https://www.sec.gov/Archives/edgar/data/1181412/000162828026056945/spcx-20260814.htm ; https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html

### B2. Claude Code revenue and pricing
**Finding: Partly confirmed.** Forbes is blocked (403). Primary equivalents: Anthropic, 12 Feb 2026 [P]: "Claude Code's run-rate revenue has grown to over $2.5 billion; this figure has more than doubled since the beginning of 2026" and "enterprise use has grown to represent over half of all Claude Code revenue." Anthropic, 3 Dec 2025 [P]: "In November … it reached $1 billion in run-rate revenue." A more recent Claude Code-specific figure from a primary source: not found (an "$8 billion … by May 2026" figure appeared only in a search summary of low-quality blogs [S]).
Pricing [P]: claude.com/pricing — Team standard seat "$20 Per seat / month if billed annually. $25 if billed monthly"; Enterprise "Seat price + usage at API rates US$20/seat/month, billed annually." Claude Code docs: "around $13 per developer per active day and $150-250 per developer per month". SSO / zero-retention / Bedrock-Vertex not checked.
- https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation ; https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone ; https://claude.com/pricing ; https://code.claude.com/docs/en/costs

### B3. GitHub Copilot
**Finding: Confirmed.** GitHub changelog, 1 June 2026 [P]: "As of June 1, all Copilot plans bill based on GitHub AI Credits consumed." GitHub blog, 27 Apr 2026 [P]: "Business remains $19/user/month, and Enterprise remains $39/user/month." Docs [P]: Business 1,900 and Enterprise 3,900 credits per user per month; "included AI credits are pooled at the billing entity level"; beyond that, "Usage continues at published per-credit rates" if additional usage is allowed; "1 AI credits = $0.01 USD". Individual plans listed: Pro $10, Pro+ $39, Max $100. Caveat: annual Pro/Pro+ subscribers stay on request-based pricing until expiry.
- https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/ ; https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing

### B4. OpenAI Codex
**Finding: Partly confirmed.** OpenAI's announcement page is blocked (403). gHacks, 3 Apr 2026 [S]: pay-as-you-go "Codex-only seats on ChatGPT Business and Enterprise", "effective starting today", and the annual Business seat price cut "from $25 to $20 per seat per month". A search summary of the OpenAI page dates the announcement April 2 and says that from June 24, 2026 new Codex pay-as-you-go seats are no longer available on Business plans [S, unconfirmed]. Current Codex pricing page [P]: Business "$20 / user / month" ("2+ users, billed annually. $25 per user per month when billed monthly"); Pro "From $100 /month" ("Plans at $100, $200, or $500"). No plan named "Premium" was found. "Codex as a platform: build on the open agent harness" is an OpenAI Developers blog post dated Aug 19, 2026 [P].
- https://learn.chatgpt.com/docs/pricing (redirect from developers.openai.com/codex/pricing) ; https://developers.openai.com/blog/codex-as-a-platform ; https://www.ghacks.net/2026/04/03/openai-adds-pay-as-you-go-codex-seats-for-chatgpt-business-and-enterprise-teams/

### B5. Amp, Factory, Cline, Augment
- **Amp — Corrected on ownership; pricing claim looks outdated.** Sourcegraph blog, 2 Dec 2025 [P]: "Sourcegraph and Amp are becoming two separate companies", with the co-founders launching "Amp Inc." — so not "Sourcegraph Amp". ampcode.com/pricing today [P] shows monthly tiers (Hobby Free; Individual "$20 ∕ mo."; Teams; Enterprise) with "Bring your own keys (BYOK)" and "No Amp token fees or limits". The words "zero markup" were not found on the page; that description is [S] only, and the "anti-subscription" framing conflicts with a $20/month tier.
- **Factory — Partly confirmed.** Docs have a "Custom Models (BYOK)" page: "Connect your own API keys" [P]. But Factory also sells subscriptions: Pro $20, Plus $100, Max $200, Teams "$60/mo per team, plus $40/mo per seat" [P].
- **Cline — Confirmed** [P]: open source and free for individuals; enterprise list includes "role-based access control, SSO, OIDC, SCIM provisioning, audit logs, VPC deployments".
- **Augment — Could not verify from primary sources.** Pricing page today [P]: Standard "$20 /month flat, no per-seat charge" (up to 50 seats), Business "$100 /month flat", Enterprise custom. The $20M figure is GetLatka only [S]: "generated $20M in revenue in 2025". The retirement of individual plans and the pivot to "Intent" are [S].
- https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies ; https://ampcode.com/pricing ; https://factory.com/pricing ; https://docs.factory.com/model-independence/byok ; https://cline.bot/pricing ; https://www.augmentcode.com/pricing ; https://getlatka.com/companies/augmentcode.com

### B6. Antigravity / Kiro
**Finding: Partly confirmed.** The Register, 12 Mar 2026 [P]: "Users protest as Google Antigravity price floats upward"; credits "at a cost of $25 for 2,500"; subhead mentions the "$250 per month Ultra plan". The article is about Antigravity; a Jules backlash was not confirmed in it. Kiro pricing [P]: Free 50 credits; Pro $20 (1,000 credits); Pro+ $40; Pro Max $100 (5,000); Power $200; add-on "$0.04/credit" — so $20/$100 are two of five tiers. "Spec overkill" complaints: [S] only (GitHub issues and reviews in search results; not opened).
- https://www.theregister.com/2026/03/12/users_protest_as_google_antigravity/ ; https://kiro.dev/pricing/

### B7. Market size by 2030 (forecasts, not measurements)
**Finding: Partly confirmed.**
- The Business Research Company [P]: "$7.65 billion in 2025", "$22.06 billion in 2030", CAGR 23.6%.
- Grand View Research (403): press-release title in search results reads "AI Code Tools Market Size To Reach $26.03 Billion By 2030" [S].
- MarketsandMarkets [P]: no 2030 figure — "USD 4.3 billion in 2023 to USD 12.6 billion by 2028, at a CAGR of 24.0%".
- A "$17.2 billion by 2030" figure appeared in a search summary, attributed there to MarketsandMarkets, which conflicts with the page above; origin not confirmed [S]. Mordor's forecast runs to 2031; the "$29.96 billion by 2031" figure is [S].
- Honest range for 2030 across these: $22.06B [P] to $26.03B [S], with an unconfirmed $17.2B outlier. The "~22–26B" in the notes matches TBRC and Grand View.
- https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-code-tools-global-market-report ; https://www.marketsandmarkets.com/Market-Reports/ai-code-tools-market-239940941.html

### B8. Margins (TechCrunch, 7 Aug 2025, Marina Temkin)
**Finding: Confirmed — both phrasings are the same quote.** [P]
- "Vibe coders generally, and Windsurf in particular, can have such expensive structures that their gross margins are 'very negative,' one person close to Windsurf told TechCrunch."
- "'Margins on all of the "code gen" products are either neutral or negative. They're absolutely abysmal,' said Nicholas Charriere, founder of Mocha".
- On Cursor the article only says "the same pressure on margins Windsurf faced could be impacting Anysphere"; it does not state Cursor's margins are negative.
- https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/

### B9. Context windows
**Finding: Partly confirmed — the Anthropic pricing caveat is wrong.** [P]
- Anthropic models overview: Fable 5.1, Opus 5.5 and Sonnet 5.5 each "1M tokens" (Haiku 4.5: 200K). Context-windows page: "1M is the default: you don't need a beta header, and long-context requests are billed at standard pricing." Pricing page: "A 900k-token request is billed at the same per-token rate as a 9k-token request." There is no separate long-context price.
- OpenAI: gpt-6-astra, gpt-6.1-sol and gpt-6-luna each "Context window 1.05M" (compare page: 1,050,000).
- Google: model code `gemini-3.1-pro-preview`, "Input token limit 1,048,576" — still labelled Preview. Pricing is tiered: input $2.00, rising to "$4.00, prompts > 200k tokens"; output $12.00, rising to $18.00 above 200k.
- https://platform.claude.com/docs/en/about-claude/models/overview ; https://platform.claude.com/docs/en/build-with-claude/context-windows ; https://developers.openai.com/api/docs/models ; https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview ; https://ai.google.dev/gemini-api/docs/pricing

## Summary

| Item | Verdict | One line |
|---|---|---|
| A1 | Corrected (our record right) | 2026 survey unpublished; 84/66/46/33/3.1 are 2025; "29%" is a 2025 sub-figure |
| A2 | Corrected (our record right) | Faros AI, 23 July 2025; not DORA |
| A3 | Partly confirmed | Instability finding is DORA 2025; "verification tax" is not in that report; earliest found is a DORA article dated March 10, 2026 |
| A4 | Corrected (our record right) | Omnibus in force 27 July 2026; Annex III to 2 Dec 2027, Annex I to 2 Aug 2028 |
| A5 | Corrected (our record closer) | opencode 211,831 stars on 2026-10-05; Aider last commit 2026-05-22 confirmed |
| A6 | Confirmed (the notes right) | Over $2B at $48B, 8 Sept 2026; run-rate "almost $900M"; $1B is Bloomberg via secondary |
| B1 | Confirmed | 8-K: closed 14 Aug 2026, 389,289,254 Class A shares, $60.0B; Teams is $40, no $60 tier found |
| B2 | Partly confirmed | Over $2.5B (Feb 2026), $1B (Nov 2025), enterprise over half; no newer primary figure |
| B3 | Confirmed | $19/$39 unchanged; AI Credits on all plans from 1 June 2026, pooled |
| B4 | Partly confirmed | Business $20 annual; pay-as-you-go launch date secondary only; "Premium" not found (Pro from $100) |
| B5 | Partly confirmed | Amp is a separate company and now has a $20 tier; Augment $20M is GetLatka only |
| B6 | Partly confirmed | Register article confirmed (Antigravity only); Kiro has five tiers |
| B7 | Partly confirmed | 2030 forecasts: $22.06B (TBRC) to $26.03B (Grand View, secondary) |
| B8 | Confirmed | Both phrases verbatim; "abysmal" speaker is Nicholas Charriere of Mocha |
| B9 | Partly confirmed | 1M-class confirmed; Anthropic has no long-context surcharge; Gemini 3.1 Pro is still Preview |
