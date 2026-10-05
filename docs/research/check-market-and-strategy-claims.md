# Check of claims about market structure and harness strategy

| | |
|---|---|
| Checked on | 2026-10-05 |
| Method | Each claim traced from Pedro's notes to the public source it rests on, then checked at that source by a Claude Code sub-agent, with figures and quotations confirmed in the raw page or paper text. Only public sources are cited. |
| Status | Record as received. |
| Used for | PLAN §3.12; PROPOSAL problem and product sections |

Tags in this file: **[P]** confirmed in the publisher's raw page or the paper's text; **[P-mirror]** raw text confirmed through a web-archive capture or mirror because the publisher blocked direct download; **[S]** secondary source only.

Checked 2026-10-05. Every figure and quotation below was read in raw page text (curl) or in the publisher's PDF unless tagged otherwise. Tags: [P] publisher's raw page or PDF; [P-mirror] raw text via an archive capture or mirror; [S] secondary only.

### M1. Market structure; Thoughtworks Radar Vol 33

**Claim.** The market "bifurcated" into synchronous in-editor "pair" agents and asynchronous cloud "delegate" agents; "Convergence points (Thoughtworks Radar Vol 33): MCP as the universal integration protocol; 'context engineering' replacing 'vibe coding'".

**Finding: Partly confirmed.**

- **MCP.** Vol 33 places Model Context Protocol (MCP) in **Platforms, Trial** (blip 39). The theme "The rise of agents elevated by MCP" says: "In many ways, MCP has become the ultimate integration protocol for powering agents and enabling them to work efficiently and semi-autonomously." The wording is "ultimate", not "universal". The blip also cautions that MCP's rapid evolution "has also introduced architectural gaps", and Vol 33 puts "Naive API-to-MCP conversion" on **Hold**.
- **Context engineering.** **Techniques, Assess** (blip 13) in Vol 33. The theme text: "context engineering has proven critical to optimizing both behavior and resource consumption." (The blip page shows it moved to **Adopt** in April 2026.)
- **Spec-driven development.** **Techniques, Assess** (blip 22): "an emerging approach to AI-assisted coding workflows"; "We may be relearning a bitter lesson — that handcrafting detailed rules for AI ultimately doesn't scale." The antipatterns theme notes "a bias toward heavy up-front specification and big-bang releases."
- **"Replacing vibe coding".** The word "vibe" does not appear in the Vol 33 PDF. The framing comes from a companion Thoughtworks article, "From vibe coding to context engineering: 2025 in software development" (Ken Mugrage, 5 Nov 2025), not from the Radar itself.
- **Pair/delegate split.** Not in Vol 33. The words "pair" and "delegate" as class labels are the notes' own. A published near-equivalent is GitHub's "Agent mode = synchronous" versus "Coding agent = asynchronous" ("an asynchronous teammate that lives in the cloud, takes on issues, and sends you fully tested pull requests"). I found no source for the product-by-product lists or for "bifurcated".

**Citations.** Thoughtworks, *Technology Radar Vol. 33*, Nov 2025, https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/11/tr_technology_radar_vol_33_en.pdf [P]; blip pages https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp , https://www.thoughtworks.com/radar/techniques/context-engineering , https://www.thoughtworks.com/radar/techniques/spec-driven-development [P]. Ken Mugrage, Thoughtworks, 5 Nov 2025, https://www.thoughtworks.com/en-us/insights/blog/machine-learning-and-ai/vibe-coding-context-engineering-2025-software-development [P]. GitHub Blog, 2 Jun 2025, https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/ [P].

### M2. Multi-agent debate

**Claim.** Anthropic: "+90.2% over single-agent Opus ... at ~15× the tokens", not suited to "most coding tasks". Cognition's position and follow-up. Settlement: "fan out reads, single-thread writes".

**Finding: Partly confirmed (one correction; the slogan is the notes').**

- **Anthropic (13 Jun 2025).** "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval." Confirmed.
- **Correction on 15×.** The baseline is chat, not the single agent: "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."
- **Caveat confirmed.** "some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research".
- **Cognition, "Don't Build Multi-Agents"** (Walden Yan, 12 Jun 2025). Two principles: "Share context, and share full agent traces, not just individual messages" and "Actions carry implicit decisions, and conflicting decisions carry bad results". Conclusion: "in 2025, running multiple agents in collaboration only results in fragile systems."
- **Follow-up, "Multi-Agents: What's Actually Working"** (Walden Yan, 22 Apr 2026). Position narrowed, not reversed: "Our original observations still hold today for parallel-writer swarms"; what works is "setups where multiple agents contribute intelligence to a task while writes stay single-threaded." Summary line: "multi-agent systems work best today when writes stay single-threaded and the additional agents contribute intelligence rather than actions." Unstructured swarms are "mostly a distraction"; "The practical shape is map-reduce-and-manage".
- **"fan out reads, single-thread writes"** is in none of the three pages. It is the notes' paraphrase; the closest verbatim is Cognition's "writes stay single-threaded".

**Citations.** Anthropic, https://www.anthropic.com/engineering/multi-agent-research-system [P]. Cognition, https://cognition.com/blog/dont-build-multi-agents [P]; https://cognition.com/blog/multi-agents-working [P].

### M3. Devin's 2025 Performance Review

**Claim.** "PR merge rate 34%→67%"; "security fixes ~20×, migrations 10–14×, test coverage to 80–90%"; fails at ambiguous end-to-end problems and mid-task requirement changes.

**Finding: Confirmed, with scope notes.**

- "67% of its PRs are now merged vs 34% last year". The comparison is this year against last year, share of Devin's PRs merged. No definition or denominator is given.
- 20× is one customer: "Another saw 20x efficiency gain: human developers average 30 minutes per vulnerability, Devin, 1.5 minutes."
- 10× and 14× are two separate customers, not a range: "3-4 hours vs 30-40 for human engineers (10x improvement)" (a bank's ETL files); "14x less time than a human engineer" (Java version migration).
- "Companies' test coverage typically rises from 50-60% to 80-90% when using Devin."
- Weaknesses: "Devin can't independently tackle an ambiguous coding project end-to-end like a senior engineer could, using its own judgement." and "Devin handles clear upfront scoping well, but not mid-task requirement changes. It usually performs worse when you keep telling it more after it starts the task."

All figures are vendor self-reported. **Citation.** The Cognition Team, "Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work", 14 Nov 2025, https://cognition.com/blog/devin-annual-performance-review-2025 [P].

### M4. MIT "95%"

**Claim.** "MIT (2025): 95% of enterprise GenAI pilots with no measurable P&L return — failure is workflow integration, not model quality".

**Finding: Partly confirmed; the claim is looser than the report, and the report is contested.**

- **Primary.** *The GenAI Divide: State of AI in Business 2025*, MIT NANDA; Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari; July 2025; marked "Preliminary Findings". 26 pages.
- **Exact wording.** "Despite $30–40 billion in enterprise investment into GenAI, this report uncovers a surprising result in that 95% of organizations are getting zero return." and "Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with no measurable P&L impact." So "95%" is attached to organizations getting zero return; "no measurable P&L impact" is attached to "the vast majority".
- **Cause.** "This divide does not seem to be driven by model quality or regulation, but seems to be determined by approach." "The primary factor ... is the learning gap, tools that don't learn, integrate poorly, or match workflows." The integration framing is supported.
- **Sample and method.** "a systematic review of over 300 publicly disclosed AI initiatives, structured interviews with representatives from 52 organizations, and survey responses from 153 senior leaders collected across four major industry conferences." Research period January–June 2025. Success is "deployment beyond pilot phase with measurable KPIs. ROI impact measured 6 months post-pilot". The report states its own limits: "These figures are directionally accurate based on individual interviews rather than official company reporting."
- **Discrepancy.** Fortune (18 Aug 2025) reports "150 interviews with leaders, a survey of 350 employees, and an analysis of 300 public AI deployments", which does not match the PDF's 52 and 153.
- **Criticism.** Futuriom (R. Scott Raynovich, 26 Aug 2025): "The 95% figure is presented in one sentence, but the authors offer no detail on where they came up with that number." It quotes Wharton's Kevin Werbach: the only 5% figure is for "custom enterprise AI tools", and "'unsuccessful' explicitly does not mean 'zero returns.'"; "If MIT Project NANDA stands behind the claims, it should release the full supporting data. If not, it should retract the report." The Werbach wording is as quoted by Futuriom [S]; I did not open his original post.
- **Forbes.** Blocked (HTTP 403 live and via web.archive.org). Not read; do not cite it for wording.

**Citations.** Report PDF: MIT's site (nanda.media.mit.edu) does not serve it directly; raw text read from a Wayback capture of https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf [P-mirror]. Fortune, https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ [S for the report]. Futuriom, https://www.futuriom.com/articles/news/why-we-dont-believe-mit-nandas-werid-ai-study/2025/08 [P for the criticism].

### M5. Stack Overflow Developer Survey 2025

**Claim.** "trust in AI accuracy 29%, down from ~40%; more distrust (46%) than trust (33%)".

**Finding: Corrected (mixes two measures).**

Same question both years: "How much do you trust the accuracy of the output from AI tools as part of your development workflow?"

| | 2024 | 2025 |
|---|---|---|
| Highly trust | 2.7% | 3.1% |
| Somewhat trust | 40.3% | 29.6% |
| Neither trust nor distrust | 26.6% | not shown in the 2025 chart |
| Somewhat distrust | 22.5% | 26.1% |
| Highly distrust | 7.9% | 19.6% |
| Publisher's summary | "43% feel good about AI accuracy and 31% are skeptical" | "distrust ... (46%) than trust it (33%)" |
| Responses | 37,302 | 33,244 |

- "29% down from ~40%" is true only for the single option **Somewhat trust** (40.3% to 29.6%). It is not total trust.
- The like-for-like headline is Stack Overflow's own: trust **43% (2024) to 33% (2025)**; distrust **31% to 46%**.
- Do not pair "29%" with "33%" in one sentence as if both were "trust". Also note the 2024 scale had a neutral option the 2025 chart does not display, so the year-on-year comparison is not perfectly clean.

**Citations.** Stack Overflow, *2025 Developer Survey — AI*, https://survey.stackoverflow.co/2025/ai [P]; *2024 Developer Survey — AI*, https://survey.stackoverflow.co/2024/ai [P].

### M6. DORA 2025

**Finding: Confirmed (from Google's announcement; the gated report PDF was not opened).**

- "AI, the great amplifier" is a section heading. Key sentence: "AI doesn't fix a team; it amplifies what's already there. Strong teams use AI to become even better and more efficient. Struggling teams will find that AI only highlights and intensifies their existing problems."
- Instability: "Unlike last year, we observe a positive relationship between AI adoption on both software delivery throughput and product performance. ... However, AI adoption does continue to have a negative relationship with software delivery stability." And: "Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability."
- Basis: "over 100 hours of qualitative data and survey responses from nearly 5,000 technology professionals".

**Citation.** Nathen Harvey and Derek DeBellis, "Announcing the 2025 DORA Report: State of AI-Assisted Software Development", Google Cloud Blog, 23 Sep 2025, https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report [P].

### M7. Veracode 2025 GenAI Code Security Report

**Finding: Partly confirmed; 2.74× is misattributed.**

- **80 tasks, 100+ LLMs: confirmed.** Report PDF: "The complete test set consists of 80 coding tasks: four languages and four CWEs, with five examples of each. We give these 80 coding tasks to over 100 LLMs".
- **45%: confirmed.** "only 55% of generation tasks result in secure code. In other words, in 45% of the tasks the model introduces a known security flaw into the code."
- **Java 72%: confirmed in Veracode's blog, not as a printed figure in the PDF.** Blog: "Java was the riskiest language, with a 72% security failure rate across tasks." (others: "Python: 38%, JavaScript: 43%, C#: 45%"). The PDF's Figure 2 prints mean security pass rates of 61.69%, 57.34%, 55.27% and 28.50% and says performance is similar "with the notable exception of Java".
- **2.74×: not Veracode.** The string "2.74" appears nowhere in the Veracode PDF, landing page or two Veracode blogs. It is from CodeRabbit's *State of AI vs Human Code Generation Report* (470 open-source GitHub pull requests): "Security issues were up to 2.74× higher". Note "up to", and that it is a different study with a different method. CodeRabbit's headline overall figure is "approximately 1.7x more issues".

**Citations.** Veracode, *2025 GenAI Code Security Report* (PDF dated July 2025; landing page now headed "October 2025 Update"), https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ and https://www.veracode.com/wp-content/uploads/2025_GenAI_Code_Security_Report_Final.pdf [P]; Veracode blog, 30 Jul 2025, https://www.veracode.com/blog/genai-code-security-report/ [P]. CodeRabbit (David Loker), 17 Dec 2025, https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report [P].

### M8. Inner versus outer harness

**Finding: Confirmed in the README; original Lopopolo post not located.**

- Quotation is verbatim in the README, attributed "— Ryan Lopopolo, OpenAI": "While alternative coding harnesses may have short-term lift, they will be bitter lessened away. I am bearish on any harness that doesn't come from the lab whose model you are using. You're fighting against post-training."
- Takeaway verbatim: "**The real edge lives in the outer harness, not the inner one.** Inner harness (tool definitions, implementations) is where labs have post-training leverage. Outer harness — orchestration, stacking while loops, injecting domain context — is where builders have alpha."
- **Original source.** The episode's public transcript shows the hosts reading it from a tweet ("I'll show the tweet that started this" ... "here's the quote"). So the origin is a post on X by Lopopolo, but I could not find the post itself. The quotation as published is a transcription of a host reading aloud; "bitter lessened" is probably "bitter-lessoned" in the original. It is not in the Latent Space interview with Lopopolo (7 Apr 2026), and OpenAI's "Harness engineering" article was blocked (403). Cite it as "quoted in ai that works", not as a primary Lopopolo source.

**Citation.** BoundaryML, *ai that works*, "OpenAI tells you not to build your own harness", 5 May 2026, https://github.com/ai-that-works/ai-that-works/tree/main/2026-05-05-openai-tells-you-not-to-build-your-own-harness (README.md and transcript.txt) [P].

### M9. Software-factory design patterns

**Finding: Confirmed.** Folder: `2026-08-25-software-factory-design-patterns`.

- "**Every agentic software factory breaks down into four layers: compute, dev environment, harness, and orchestration.**" The summary line adds "where to buy versus build at each one."
- "**The harness layer has no standard interface yet, and that's not an accident.** Protocols like ACP and AG-UI let a harness talk to a UI, but neither supports hooks, the lifecycle events a control plane needs to react to mid-session. `Claude Code`, `Codex`, and Pi all implement hooks completely differently because each harness makes different tradeoffs."
- "Boundary deliberately doesn't own the harness layer so it can stay swappable between `Claude Code` and `Codex`." and "It should be composition over inheritance".
- The README says "no standard interface **yet**"; keep the "yet". "Keep the harness swappable" as a general rule is the notes' inference from Boundary's stated practice.

**Citation.** BoundaryML, *ai that works*, "Software Factory Design Patterns", 25 Aug 2026, https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-25-software-factory-design-patterns [P].

### M10. SlopCodeBench episode

**Finding: Confirmed, with an internal inconsistency in the source.** Folder: `2026-08-04-slop-code-bench`. All four statements are verbatim:

- "today's frontier models top out around 33% strict pass rate"
- "**Only Sonnet wrote actual Python unit tests.**"
- "**Planning didn't move the needle.**" ("found close to no difference")
- "Fable beat Sonnet on strict pass rate by about 2 percentage points, at roughly 5x the cost."

Caveat: the same README's Key Takeaways say "Sonnet 5 and Fable tied at 33%, GPT-5.5 came in at 14.8%" and in the next sentence "Fable beat Sonnet by about 2 points". "Tied" and "beat by about 2 points" conflict; the README gives no exact pair of figures. These are the hosts' notes on a benchmark by Gabe Orlanski (University of Wisconsin-Madison); the benchmark's own publication was not checked.

**Citation.** BoundaryML, *ai that works*, "SlopCodeBench", 4 Aug 2026, https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-04-slop-code-bench [P].

### M11. Harness-engineering framing

**Finding: Confirmed, with exact wording.** Episode: "Harness Engineering Without the Hype", folder `2026-04-21-harness-engineering-without-the-hype` (recorded live at AI Engineer Miami).

- Episode highlight, unattributed to a named speaker: "The harness is really the operating system around the agent — and the agent is the while true loop." The notes drop "really" and hyphenate "while-true".
- Key takeaway heading, verbatim: "**Evals are the spec that outlives everything else.**" followed by "The code you write today may be irrelevant in six months."

This is the README authors' summary, not a transcript; the repo's transcript file for this episode is effectively empty, so the speaker cannot be confirmed.

**Citation.** BoundaryML, *ai that works*, 21 Apr 2026, https://github.com/ai-that-works/ai-that-works/tree/main/2026-04-21-harness-engineering-without-the-hype [P].

### M12. Kent Beck at Prodacity 2026

**Finding: Confirmed (description wording only).**

- Video exists: "Kent Beck: Software Engineering in the Age of AI | Prodacity 2026", channel Rise8, uploaded 2026-09-29, 3,112 seconds.
- Description bullets, verbatim: "Why Beck calls it the genie, and why plausible code is not working code" and "One-shot versus iterative, and why spec-driven development is waterfall wearing a new coat".
- These are Rise8's billing in the description. Whether Beck says those exact words was not checked (no transcript read). Attribute them to the description, not to Beck as a quotation.
- Talk date: Rise8's announcement gives the event as "August 25–27, 2026, in Nashville, Tennessee"; the description mentions "Day 1" but the exact day of the talk is not stated.

**Citations.** Rise8, YouTube, 29 Sep 2026, https://www.youtube.com/watch?v=F8fBgDCf2Y4 [P]; Rise8 announcement, 1 May 2026, https://www.rise8.us/resources/rise8-announces-prodacity-2026-with-expanded-ai-focus-for-govtech-training [P].

## Summary

| Item | Verdict | One line | Public URL |
|---|---|---|---|
| M1 | Partly confirmed | MCP is Trial, context engineering and spec-driven development are Assess; "ultimate" not "universal"; "vibe coding" and pair/delegate are not in the Radar | https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/11/tr_technology_radar_vol_33_en.pdf |
| M2 | Partly confirmed | 90.2% confirmed; 15× is versus chat, not versus single agent; slogan is the notes' | https://www.anthropic.com/engineering/multi-agent-research-system |
| M3 | Confirmed | 67% vs 34% "last year"; 20×, 10× and 14× are single-customer examples | https://cognition.com/blog/devin-annual-performance-review-2025 |
| M4 | Partly confirmed | "95% of organizations are getting zero return"; 52 interviews, 153 surveyed, 300+ initiatives; contested | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf |
| M5 | Corrected | 29.6% is "Somewhat trust" only; like for like is 43% to 33% trust, 31% to 46% distrust | https://survey.stackoverflow.co/2025/ai |
| M6 | Confirmed | "AI doesn't fix a team; it amplifies what's already there"; negative relationship with delivery stability | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report |
| M7 | Partly confirmed | 80 tasks, 100+ LLMs, 45% confirmed; Java 72% from Veracode blog; 2.74× is CodeRabbit, "up to" | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ |
| M8 | Confirmed | Quote and takeaway verbatim in README; origin is a tweet, not located | https://github.com/ai-that-works/ai-that-works/tree/main/2026-05-05-openai-tells-you-not-to-build-your-own-harness |
| M9 | Confirmed | Four layers and "no standard interface yet" verbatim | https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-25-software-factory-design-patterns |
| M10 | Confirmed | All four statements verbatim; README also says Sonnet 5 and Fable "tied at 33%" | https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-04-slop-code-bench |
| M11 | Confirmed | Both phrases in the 21 Apr 2026 episode README; minor wording difference | https://github.com/ai-that-works/ai-that-works/tree/main/2026-04-21-harness-engineering-without-the-hype |
| M12 | Confirmed | Both phrases are in Rise8's video description; not verified as Beck's spoken words | https://www.youtube.com/watch?v=F8fBgDCf2Y4 |
