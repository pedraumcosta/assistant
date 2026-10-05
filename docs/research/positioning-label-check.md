# Check of the label "evidence-driven development"

| | |
|---|---|
| Checked on | 2026-10-05 |
| Method | Web research by a Claude Code sub-agent, with names and quotations confirmed in raw pages. Searching was throttled part-way, so "no owner found" rests on about a dozen searches. Trademark registers could not be queried. |
| Status | Record as received. The verdict section is the researcher's assessment. |
| Used for | PLAN §2.1 T14; PROPOSAL §2.5; JOURNAL ADR-019 |

Tags in this file: **[P]** confirmed in the raw page; **[S]** secondary source or search snippet only.


Research date 2026-10-05. [P] = wording confirmed in the raw page fetched with curl; [S] = search snippet or secondary source only. Blocked pages are named. Absence claims rest on roughly a dozen web searches, not an exhaustive sweep.

## 1. Who uses "evidence-driven / evidence-based" today

**No product, company or book was found that owns "evidence-driven development" as a category or tagline.** What exists:

- **Academic field (strongest prior meaning).** "Evidence-based software engineering" (EBSE) is Kitchenham, Dybå and Jørgensen's ICSE 2004 paper (pp. 273-281), which proposed importing the evidence-based-medicine research approach (systematic reviews) into software engineering; it later won an ACM SIGSOFT most-influential-paper award. [S] https://dl.acm.org/doi/10.5555/998675.999432 (ACM blocked the raw fetch; details from search snippets).
- **Derek Jones's book** "Evidence-based Software Engineering: based on the publicly available data" — "discusses what is currently known about software engineering, based on an analysis of all the publicly available data". [P] http://www.knosof.co.uk/ESEUR/ . Release date of 8 Nov 2020 is [S] https://shape-of-code.com/2020/11/08/evidence-based-software-engineering-book-released/
  Both mean *empirical research about software practice*, not *accepting a change on test evidence*. A reader with a research background will hear this first.
- **Lean/product sense.** A SlideShare deck titled "Evidence driven development - a lean methodology to product development" exists (hypothesis/experiment sense). [S] https://www.slideshare.net/slideshow/evidence-driven-development-a-lean-methodology-to-product-development/101210694 (raw fetch blocked by a client challenge; author and date not confirmed).
- **AI-coding-agent context, 2026 — small, unowned, but converging on the idea:**
  - GitHub topic `evidence-driven`: "30 public repositories matching this topic"; top entry GanyuanRan/Aegis (1.3k stars), "Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked", whose README says "Proof before 'done'. Completion claims ship with fresh verification evidence". It uses the *tag*, not the phrase "evidence-driven development". [P] https://github.com/topics/evidence-driven , https://github.com/GanyuanRan/Aegis
  - doulos76/evidence-driven-engineering: "A lightweight evidence-first engineering judgment framework (Agent Skill) for AI coding agents"; 0 stars. [P] https://github.com/doulos76/evidence-driven-engineering
  - Papers use the *vocabulary* without the label: Agentic Agile-V (Christopher Koch, arXiv, 19 May 2026): "Agent output is not accepted because it is plausible; it is accepted because it satisfies evidence appropriate to its risk level", with an "Evidence Bundle". [P] https://arxiv.org/abs/2605.20456 . Protocol-Driven Development (Jun He, Deying Yu, 13 May 2026): an implementation "is admitted only if it satisfies the protocol and produces a verifiable Evidence Chain of compliance". [P] https://arxiv.org/abs/2605.12981
- **Trademarks:** not checked. USPTO trademark search and EUIPO eSearch are JavaScript applications that returned no result data to curl; a web search for the phrase plus USPTO/EUIPO surfaced no registration [S]. A descriptive phrase of this kind is unlikely to be registrable, but that is an inference, not a search result.

**Assessment:** no owner to collide with. The confusable existing meaning is EBSE (research method), plus a faint lean "experiment/hypothesis-driven" sense.

## 2. The abbreviation "EDD"

"EDD" is established for **eval-driven / evaluation-driven development** in the LLM world:

- **Braintrust**, "What is eval-driven development" (18 Feb 2026): "Eval-driven development (EDD) solves this by giving you a reliable signal… use the eval scores as your oracle"; "a methodology where evaluations serve as the working specification". [P] https://www.braintrust.dev/articles/eval-driven-development
- **evaldrivendevelopment.dev** (Brenn Hill, "Updated June 2026"), a dedicated site with a "What is EDD" nav item: "the practice of using evals — not vibes — as the executable spec and the guardrail for AI-assisted software… the AI-era successor to test-driven development". [P] https://evaldrivendevelopment.dev/
- **OpenAI** evaluation best practices: "Adopt eval-driven development: Evaluate early and often." [P] https://platform.openai.com/docs/guides/evaluation-best-practices
- **Anthropic**: "We recommend practicing eval-driven development: build evals to define planned capabilities before agents can fulfill them" [P] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; Agent Skills best practices has an "Evaluation-driven development" procedure. [P] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Vercel** (17 Oct 2024): "Eval-driven development: Build better AI faster". [P] https://vercel.com/blog/eval-driven-development-build-better-ai-faster
- **Academic**: Xia, Lu, Zhu et al., "Evaluation-Driven Development and Operations of LLM Agents" (EDDOps), arXiv, v1 21 Nov 2024. [P] https://arxiv.org/abs/2411.13768
- Others: FutureAGI glossary "Eval-driven development (EDD)" [P] https://futureagi.com/glossary/eval-driven-development/ ; DeepEval/Confident AI [P] https://deepeval.com/blog/eval-driven-development ; Anaconda "Evaluations Driven Development" (16 Jul 2024) [P] https://www.anaconda.com/blog/introducing-evaluations-driven-development ; GitHub list "awesome-eval-driven-development… Eval-Driven-Development (EDD)" [P] https://github.com/itsderek23/awesome-eval-driven-development; Chip Huyen's *AI Engineering* attributed with an "Evaluation-Driven Development (EDD)" framework [S] https://medium.com/@keerthanams1208/chip-huyens-evaluation-driven-development-edd-framework-from-ai-engineering-a2939cc9ecf8
- **Not found** on the pages fetched: the phrase on LangSmith/LangChain, Langfuse, Galileo or Patronus pages. Promptfoo says "test-driven LLM development" instead. [P] https://www.promptfoo.dev/docs/intro/ . Arize and Humanloop pages were blocked or gone: not checked.

Other software meanings of EDD: **example-driven development** — Wikipedia's ATDD article lists "example-driven development (EDD)" as a sibling of ATDD/BDD [P] https://en.wikipedia.org/wiki/Acceptance_test-driven_development ; testRigor [P] https://testrigor.com/blog/what-is-edd/ . **Error-driven development (EDD)** [P] https://testrigor.com/blog/what-is-error-driven-development/ . **Experiment-driven development** [S] https://fourweekmba.com/experiment-driven-development/ .

**Assessment:** EDD is taken, and by the nearest possible neighbour. Using EDD for "evidence-driven" will be read as eval-driven.

## 3. Neighbouring banners

- **Spec-driven development (SDD)** — crowded and owned. Kiro: "an agentic IDE that helps you go from prototype to production with spec-driven development"; its current description says "turn prompts into executable specs". [P] https://kiro.dev/ . GitHub Spec Kit: "Toolkit to help you get started with SDD". [P] https://github.com/github/spec-kit . Tessl now titles itself "Agent Enablement Platform" while its blog still says "Learn spec-driven development". [P] https://tessl.io/ , https://tessl.io/blog/ . Canonical survey: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 15 Oct 2025. [P] https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html .
- **Software factory / dark factory.** StrongDM (Justin McCarthy, 6 Feb 2026): "We built a Software Factory: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review." [P] https://factory.strongdm.ai/ . Simon Willison attributes "Dark Factory level" to Dan Shapiro and highlights scenarios held out from the agents "similar to a 'holdout' set". [P] https://simonwillison.net/2026/Feb/7/software-factory/ . The company Factory: "Factory | Agent-Native Software Development… Factory Droids". [P] https://factory.ai/
- **TDD re-invoked for agents.** Pragmatic Engineer with Kent Beck (11 Jun 2025): "Test driven development (TDD) is a 'superpower' when working with AI agents." [P] https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent . Beck's "Augmented Coding: Beyond the Vibes" (25 Jun 2025) separates augmented from vibe coding. [P] https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes . Agents deleting tests to pass: [S] same interview. Papers: TDAD "Test-Driven Agentic Development" [P] https://arxiv.org/abs/2603.17973 ; Consort, "Enforced, Test-Driven Development", naming Spec Kit, obra/superpowers, BMAD and GSD as peers [P] https://arxiv.org/abs/2609.09671
- **ATDD / BDD — the true precedent.** Agile Alliance: ATDD "involves team members with different perspectives (customer, development, testing) collaborating to write acceptance tests in advance of implementing the corresponding functionality". [P] https://agilealliance.org/glossary/atdd/ . Wikipedia: BDD is "centered around collaboration between business and IT professionals… a shared understanding of the problem", using natural-language constructs. [P] https://en.wikipedia.org/wiki/Behavior-driven_development
- **Contract-driven:** design by contract = "formal, precise and verifiable interface specifications". [P] https://en.wikipedia.org/wiki/Design_by_contract . "Verification-driven" and "proof-carrying" as agent-development banners: not found as owned labels.

**Is our practice ATDD under a new name?** Its first half is: "define done as executable acceptance checks before work starts" is ATDD's canonical definition almost word for word. What ATDD/BDD do not cover: (a) evals for non-deterministic output, (b) AI agents as authors, (c) the retained acceptance record. The honest framing is "ATDD plus EDD, extended to agent authors, with an audit trail".

## 4. Who already sells essentially this practice

Nobody was found selling it under an "evidence" name. Closest by substance:

- **StrongDM Software Factory** — specs plus externally held scenarios decide acceptance, no human review; a published methodology, not a sold product. [P] https://factory.strongdm.ai/
- **Braintrust / eval-driven development** — evals as "working specification" and gate, for LLM applications only. [P] https://www.braintrust.dev/articles/eval-driven-development
- **Kiro** — "executable specs" for agent and human work. [P] https://kiro.dev/
- **Factory** — advises that agent-authored work "pass through the same protected workflow as human-authored work, with a clearly identified author and visible test evidence" (24 Sep 2026); guidance, not a named methodology. [P] https://factory.com/articles/reviewing-agent-generated-pull-requests
- **Aegis** (open source) — "Proof before 'done'". [P] https://github.com/GanyuanRan/Aegis
- **Papers**: Agentic Agile-V and Protocol-Driven Development (section 1) state the acceptance-on-evidence rule and the record ("Evidence Bundle", "Dynamic Evidence Ledger") explicitly.

Not checked: Qodo, Graphite, Augment and similar review/merge-gate vendors beyond search snippets.

## Verdict on the label

- **Free enough to use: yes.** No company, product, book or (as far as could be checked) trademark owns "evidence-driven development". Uses in the agent context are small open-source repos and paper vocabulary.
- **What it will be confused with:** (1) eval-driven development, through the shared initials and near-identical sound; (2) evidence-based software engineering (Kitchenham; Jones), which means empirical research, so academics may hear "decisions based on studies"; (3) faintly, lean experiment/hypothesis-driven product development.
- **Abbreviation: avoid "EDD".** It is already used by Braintrust, a dedicated site, FutureAGI and others for eval-driven development, and historically for example-driven and error-driven development.
- **Strongest objection:** the practice is ATDD (acceptance tests first) merged with eval-driven development, and both vendors (OpenAI, Anthropic, Braintrust) and Kent Beck are already re-invoking those names for agents. A sceptical buyer can fairly say "this is ATDD/EDD renamed", and "evidence" is the vaguest of the three words — it does not say *executable*, *first*, or *recorded*. The label needs a one-line definition that claims the delta (agent and human changes under one gate, evidence kept), and the vocabulary is converging fast ("evidence bundle", "evidence chain", "proof before done"), so the window to claim it is short.
