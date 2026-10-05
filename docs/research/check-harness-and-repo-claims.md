# Check of harness, repository-understanding and pain-point claims in Pedro's web research notes

| | |
|---|---|
| Notes dated | 2026-10-01 |
| Checked on | 2026-10-05 |
| Method | Each claim checked at the most primary source reachable by a Claude Code sub-agent, with figures and quotations confirmed in the raw page. OpenAI's post was read from a web-archive capture of 2026-09-24. |
| Status | Record as received. |
| Used for | PLAN §3.8; DESIGN (repo understanding) |

Tags in this file: **[P]** confirmed in the publisher's raw page (downloaded and searched, not a summary); **[P-archive]** read raw from a web-archive capture because the publisher blocked direct download; **[P-summary]** publisher's page seen only through a summarising fetch; **[S]** secondary source or search snippet only.


Tags: [P] = read in the publisher's raw page (curl + grep); [P-archive] = publisher's page read raw from a Wayback Machine capture because the live site blocked curl; [S] = secondary only. All quotations are verbatim.

## Section H: harness ideas

### H1. OpenAI "Harness engineering"
**Claim:** Feb 2026; ~1M LOC, zero human-written lines; humans design constraints/verification/feedback loops.
**Finding: Confirmed, with a wrong URL and an important qualification on verification.**

- The URL given is a different post ("Unlocking the Codex harness: how we built the App Server", 4 Feb 2026). The right one is "Harness engineering: leveraging Codex in an agent-first world", by Ryan Lopopolo, 11 Feb 2026: https://openai.com/index/harness-engineering/ . openai.com returns a Cloudflare challenge to curl; text read from Wayback capture 20260924171239. [P-archive]
- Scale: "an internal beta of a software product with 0 lines of manually-written code"; "on the order of a million lines of code"; "roughly 1,500 pull requests"; "3.5 PRs per engineer per day"; team grew from three to seven engineers; "about 1/10th the time" (their own estimate). It is an internal beta with "internal daily users and external alpha testers".
- What humans do: "Humans steer. Agents execute."; the job is "to design environments, specify intent, and build feedback loops"; "We prioritize work, translate user feedback into acceptance criteria, and validate outcomes."
- How correctness is assured (the key passages):
  - "we instruct Codex to review its own changes locally, request additional specific agent reviews both locally and in the cloud, respond to any human or agent given feedback, and iterate in a loop until all agent reviewers are satisfied"
  - "Humans may review pull requests, but aren't required to. Over time, we've pushed almost all review effort towards being handled agent-to-agent."
  - "These constraints are enforced mechanically via custom linters (Codex-generated, of course!) and structural tests."
  - "The repository operates with minimal blocking merge gates. Pull requests are short-lived. Test flakes are often addressed with follow-up runs rather than blocking progress indefinitely. In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive." Then: "This would be irresponsible in a low-throughput environment."
  - Runtime validation: the app is "bootable per git worktree", with Chrome DevTools Protocol and a per-worktree observability stack so Codex can "reproduce bugs, validate fixes, and reason about UI behavior directly".
- Stated limits: "our bottleneck became human QA capacity"; "Our team used to spend every Friday (20% of the week) cleaning up 'AI slop.'"; "should not be assumed to generalize without similar investment"; "What we don't yet know is how architectural coherence evolves over years".
- The tests themselves are agent-written ("every line of code—application logic, tests, CI configuration..."). No defect rate, coverage figure or independent correctness measure is given (only one helper is said to have "100% test coverage"). Vendor interest: OpenAI sells Codex.

### H2. Hindsight "agent harness needs memory"
**Finding: Confirmed as a vendor argument, not an independent finding.**
Title "The Missing Layer in Every Agent Harness", Ben Bartholomew, "Hindsight Team", 4 May 2026. Hindsight is Vectorize's memory product; the page carries "Try Hindsight Cloud ... Long-term memory for your agents, fully managed". Claims: "What almost none of them ship with is memory that learns."; "The remaining gap between 'an agent that is impressive in a single session' and 'an agent that gets better at your work over months' is almost entirely memory."; compaction "is a context-window management trick, not memory"; "Claude Code does not have native long-term memory yet". Conclusion: "Hindsight is designed to be the memory layer any harness can drop in." No measurements. https://hindsight.vectorize.io/blog/2026/05/04/agent-harness-needs-memory [P]

### H3. HumanLayer "skill issue"
**Finding: Partly confirmed (attribution corrected).**
- "Skill Issue: Harness Engineering for Coding Agents", HumanLayer blog, 12 Mar 2026, bylined **Kyle** (Dex Horthy's cofounder), not Dex. Phrases: "it's not a model problem. It's a configuration problem."; "The model is probably fine. It's just a skill issue."; "Avoid the dumb zone."; too many MCP tools push "you into the dumb zone much faster". It says context engineering was "Coined by my cofounder Dex in 12-factor agents". https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents [P]
- 12-factor-agents README: "Factor 3: Own your context window", "Factor 10: Small, Focused Agents" ("3-10, maybe 20 steps max"; "As context grows, LLMs are more likely to get lost or lose focus"). https://github.com/humanlayer/12-factor-agents [P]
- Dex's "Advanced Context Engineering" essay: "keeping utilization in the 40%-60% range". https://github.com/humanlayer/advanced-context-engineering-for-coding-agents [P]
- "Mid-context" dumb zone and Dex's own talk wording: not found in the pages read (talk not checked). HumanLayer sells coding-agent tooling.

### H4. Spec-driven development and backlash
**Finding: Partly confirmed. Criticisms confirmed; "shipped by everyone" not verified.**
- The HN item is the discussion of Böckeler's article (128 points, 32 comments); commenters write "Waterfall anyo[ne]" and "Really, we are doing waterfall, but with AI, now?". [P]
- Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", martinfowler.com, 15 Oct 2025: "like using a sledgehammer to crack a nut" (Kiro turned a small bug into "4 'user stories' with a total of 16 acceptance criteria"); "spec-kit created a LOT of markdown files for me to review... very verbose and tedious to review"; "To be honest, I'd rather review code than all these markdown files."; "False sense of control?"; "Verschlimmbesserung". She does not use the word waterfall in the passages found. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html [P]
- Colin Eberhardt, Scott Logic, "Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?", 26 Nov 2025: "a sea of markdown documents, long agent run-times and unexpected friction"; "2,577 lines of markdown" against "689 lines of code"; "I am a lot more productive without SDD, around ten times faster"; "Spec Kit drags you right back into the past!" One hobby-app trial. https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html [P]
- Vendors confirmed from these sources: AWS Kiro, GitHub Spec Kit, Tessl. Other vendors: not checked.

### H5. Willison on parallel agents
**Finding: Partly confirmed.**
"Embracing the parallel coding agent lifestyle", 5 Oct 2025: "AI-generated code needs to be reviewed, which means the natural bottleneck on all of this is how fast I can review the results."; "I can only focus on reviewing and landing one significant change at a time". But: "I haven't adopted git worktrees yet: if I want to run two agents in isolation against the same repo I do a fresh checkout, often into /tmp." He reports others using worktrees; he does not call them mainstream. The wording "human attention/verification capacity" is the notes' paraphrase (OpenAI's post says "human time and attention"). https://simonwillison.net/2025/Oct/5/parallel-coding-agents/ [P]

### H6. Code mode / MCP code execution
**Finding: Corrected (dates and what the figures measure).**
- Anthropic, "Code execution with MCP", 4 Nov 2025: "This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%." An illustrative example of loading tool definitions on demand, not a benchmark. https://www.anthropic.com/engineering/code-execution-with-mcp [P]
- Cloudflare, "Code Mode: the better way to use MCP", 26 Sep 2025: no percentage figure found. https://blog.cloudflare.com/code-mode/ [P]
- Cloudflare, "Code Mode: give agents an entire API in 1,000 tokens", **20 Feb 2026**: "Code Mode reduces the number of input tokens used by 99.9%. An equivalent MCP server without Code Mode would consume 1.17 million tokens"; two tools, "around 1,000 tokens", API of "over 2,500 endpoints". https://blog.cloudflare.com/code-mode-mcp/ [P]
- Both are reductions in tool-definition/input-context tokens for one large tool surface, not in whole-task cost. Both vendors sell the platform involved.

## Section R: repository understanding

### R1. Boris Cherny on agentic search
**Finding: Confirmed.**
- X post, 1 Feb 2026 (04:56 UTC), reply to @EthanLipnik: "Early versions of Claude Code used RAG + a local vector db, but we found pretty quickly that agentic search generally works better. It is also simpler and doesn't have the same issues around security, privacy, staleness, and reliability." Read from X's syndication JSON (cdn.syndication.twimg.com) for status 2017824286489383315. [P]
- Pragmatic Engineer, "Building Claude Code with Boris Cherny", 4 Mar 2026. Gergely Orosz's summary, not a Cherny quote: "Claude Code's 'agentic search' is really just glob and grep, and it outperformed RAG... Plain glob and grep, driven by the model, beat everything." https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny [P]
- No benchmark numbers in either. Anthropic employee describing Anthropic's product.

### R2. Cursor semantic search
**Finding: Confirmed.**
"Improving agent with semantic search", 6 Nov 2025: "on average 12.5% higher accuracy in answering questions (6.5%–23.5% depending on the model)" on their own "Cursor Context Bench" (offline). Online A/B: "agent code retention increases by 0.3% when semantic search is available. This effect increases to 2.6% on large codebases with 1,000 files or more"; "a 2.2% increase in dissatisfied follow-up user requests when semantic search was not available." Recommendation: "Our agent makes heavy use of grep as well as semantic search, and the combination of these two leads to the best outcomes." Note the overall retention figure is 0.3%. Vendor's own unpublished benchmark. https://cursor.com/blog/semsearch [P]

### R3. Aider repo map
**Finding: Confirmed (PageRank is in the code, not the docs).**
Post of 22 Oct 2023 and current docs: tree-sitter extracts definitions/references; ranking uses "a graph ranking algorithm, computed on a graph where each source file is a node and edges connect files which have dependencies"; budget set "via the --map-tokens switch, which defaults to 1k tokens". Docs add that aider "does expand the repo map significantly at times, especially when no files have been added to the chat". Source `aider/repomap.py` has `map_tokens=1024` and references networkx `pagerank`. https://aider.chat/2023/10/22/repomap.html , https://aider.chat/docs/repomap.html , https://github.com/Aider-AI/aider/blob/main/aider/repomap.py [P]

### R4. Vendor indexing
**Finding: Partly confirmed.**
- Cursor: "Securely indexing large codebases" (27 Jan 2026) confirms Merkle-tree sync against "the server's version", syntactic chunks "converted into the embeddings". Turbopuffer is not named on the Cursor pages read; turbopuffer's own post says "Cursor moved everything to turbopuffer in a few days in November of 2023" and "Cursor never stores plain text code with turbopoffer [sic]". Embeddings are stored server-side; whether code chunks transit Cursor's servers for embedding: not found in pages read. Cursor's current search docs describe only a local "Instant Grep" ("builds and queries its index on your machine"). https://cursor.com/blog/secure-codebase-indexing , https://turbopuffer.com/blog/turbopuffer [P]
- Augment: "When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud." Code leaves the machine. https://docs.augmentcode.com/setup-augment/workspace-indexing [P]
- Copilot: "GitHub indexes the GitHub repositories in your workspace... GitHub builds and updates this index when needed"; for non-GitHub repos "This feature uploads your data to GitHub" and is "disabled by default" for organisations. **"Default branch": not found** in current GitHub or VS Code docs. https://docs.github.com/en/copilot/concepts/context/repository-indexing , https://code.visualstudio.com/docs/copilot/reference/workspace-context [P]

### R5. Serena
**Finding: Corrected (figure out of date).**
README now says "support for over 40 programming languages" via its LSP backend; "30+" not found. Also offers a paid JetBrains plugin backend. https://github.com/oraios/serena [P]

### R6. WorkOS on compaction and caching
**Finding: Confirmed, with nuance.**
"Stop giving your coding agent a million-token context window", Mitch Fultz, 14 Aug 2026: "Compaction also breaks prompt-cache reuse from the inserted summary onward: an unchanged leading system-and-tools prefix may remain reusable, but the retained turns can no longer reuse their previous cached state, because they now follow a different prefix." So partial, not total, cache loss. https://workos.com/blog/coding-agent-context-window-compaction-settings [P]

## Section P: pain points

### P1. GitClear
**Finding: Confirmed, all four; baseline wording is inconsistent.**
"The Maintainability Gap: AI Code Quality in 2026": "623 million analyzed changes from 2023-2026". "code block duplication (+81%), error-masking constructs (+47%), and two-week code churn (+15%)"; "Refactoring line moves are down 70%"; also copy/paste "+41%", cross-file calls "down 35%", legacy maintenance "down 74% vs 2022 levels". Detail: duplication "from 40.3 in 2023 to 73.0 year-to-date in 2026 — an 81% increase over 2023"; moved code "21% in 2022... 13% of changed lines in 2023... 3.8% year-to-date in 2026". Comparison is 2023 vs 2026 year-to-date (chart "Indexed to 2023 = 100"), although one sentence says "vs 2022 levels". No base values are given on the page for +47% and +15% (full PDF is behind an email form). Publication date: not found on page; earliest Wayback capture 10 Jul 2026. GitClear sells code-quality analytics. https://www.gitclear.com/the_ai_code_quality_maintainability_gap [P]

### P2. METR
**Finding: Confirmed.**
- 10 Jul 2025: "we recruited 16 experienced developers from large open-source repositories (averaging 22k+ stars and 1M+ lines of code)"; "246 total" issues; "they take 19% longer to complete issues"; "developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%." [P]
- 24 Feb 2026, "We are Changing our Developer Productivity Experiment Design": "We have data from 57 developers, across 143 repos, and 800+ tasks."; "we believe it is likely that developers are more sped up from AI tools now — in early 2026 — compared to our estimates from early 2025. However, because of the selection effects in our experiment, our data is only very weak evidence for the size of this increase." Raw: returning developers "-18% with a confidence interval between -38% and +9%"; new developers "-4%... between -15% and +9%". Both intervals include zero. Original result restated as "19% longer, with a confidence interval between +2% and +39%". [P]

### P3. Pricing backlashes
**Finding: Partly confirmed; "rollback" corrected.**
- Cursor: 16 Jun 2025 Pro change from request-based to "$20 of included usage"; 4 Jul 2025 post "We missed the mark" offers refunds "between June 16 and July 4". An apology and refunds, not a rollback. https://cursor.com/blog/june-2025-pricing [P]
- Copilot "September cliff": a coinage by CloudZero (cost-management vendor), 26 Aug 2026. GitHub moved all plans to usage-based "GitHub AI Credits" on 1 Jun 2026 (announced 27 Apr 2026) with "promotional included usage for June, July, and August: Copilot Business: $30... Copilot Enterprise: $70". CloudZero: on 1 Sep "Enterprise pools shrink 44% and Business pools shrink 37%" (to 3,900 and 1,900 credits). The shrink percentages are CloudZero's. https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ [P]; https://www.cloudzero.com/blog/github-copilot-enterprise-pricing/ [S]
- Antigravity: The Register, 12 Mar 2026, "Users protest as Google Antigravity price floats upward": credits "$25 for 2,500"; AI Pro users report weekly rather than five-hour refreshes. [S] https://www.theregister.com/software/2026/03/12/users-protest-as-google-antigravity-price-floats-upward/5227776
- Kiro: The Register, 18 Aug 2025: "a wallet-wrecking tragedy"; vibe requests "$0.04 each", spec requests "$0.20 each"; AWS "blames pricing bug". [S] https://www.theregister.com/2025/08/18/aws_updated_kiro_pricing/

## Summary

| Item | Verdict | One line |
|---|---|---|
| H1 | Confirmed (URL corrected) | Million lines, 0 hand-written; correctness rests on agent review, linters, structural tests; human review optional; no quality metric published |
| H2 | Confirmed (vendor) | Memory vendor arguing harnesses need memory; no data |
| H3 | Partly confirmed | "Skill issue" post is by Kyle, not Dex; "mid-context" wording not found |
| H4 | Partly confirmed | Böckeler and Scott Logic quotes confirmed; "everyone ships it" not verified |
| H5 | Partly confirmed | Review is "the natural bottleneck"; Willison himself had not adopted worktrees |
| H6 | Corrected | Anthropic 98.7% (Nov 2025); Cloudflare 99.9% is Feb 2026; tool-definition tokens only |
| R1 | Confirmed | Tweet 1 Feb 2026 verbatim; "beat everything" is Orosz's summary |
| R2 | Confirmed | 12.5% (6.5–23.5%), 2.6% retention on 1,000+ files, 0.3% overall; hybrid recommended |
| R3 | Confirmed | Docs say "graph ranking algorithm"; PageRank and 1024 default in source |
| R4 | Partly confirmed | Merkle and Turbopuffer confirmed; Augment uploads code; Copilot "default branch" not found |
| R5 | Corrected | README says "over 40", not 30+ |
| R6 | Confirmed | Breaks cache "from the inserted summary onward"; prefix may survive |
| P1 | Confirmed | All four figures; baseline 2023; date not on page |
| P2 | Confirmed | 19% longer vs believed 20% faster; 2026 data "only very weak evidence" |
| P3 | Partly confirmed | Cursor apologised/refunded, no rollback; "September cliff" = end of Copilot promo credits 1 Sep 2026 |
