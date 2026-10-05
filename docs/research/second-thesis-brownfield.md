# Second thesis evaluated: a brownfield / enterprise-legacy specialisation

| | |
|---|---|
| Origin | Pedro's list of thesis candidates, which names two: a verification-first layer that works across agents (the thesis this project has been developing), and a "Brownfield/enterprise-legacy assistant" built on Osmani's practices, SWE Refactor Bench and "harness as institutional memory". Raised for evaluation on 2026-10-05. |
| What this file is | The evaluation: what the thesis proposes, what its evidence says when read in full, how occupied the market is, and our reading of what to do with it |
| Method | The brownfield section of Pedro's notes and Osmani's article were read by the main Claude Code session. The two papers were read in full by a sub-agent. The market was researched by another from vendor sources. All on 2026-10-05. |
| Status | The findings sections report sources. The last two sections are our assessment and a recommendation for the thesis discussion; no decision has been taken. |
| Used for | PLAN §3.11, ROADMAP open questions T1 and T11, JOURNAL ADR-013 |

Records behind this file: `articles/osmani-brownfield-agentic-engineering.md`, `paper-swe-refactor-bench.md`, `paper-legacy-modernization-case-study.md`, `brownfield-market.md`.

## The proposition

Build a product specialised for agent work in old codebases: migrations and modernisation, and everyday change in legacy systems. Its content would be four practices from Osmani's article:

1. zone the codebase by blast radius (green, yellow, red);
2. make exploration durable, as a comprehension memo;
3. write characterization tests before changing anything;
4. treat the harness as institutional memory: every repeated correction becomes a rule, hook or test.

Its evidence is that agents do badly in exactly this setting, and Pedro's notes add the commercial instinct that brownfield is where the money is.

## What the evidence says, read in full

**Agents are weakest here.** This part of the thesis holds.

- SWE Refactor Bench: "only 28 of 520 runs ( 5.4% ) pass all three stages, 13 of the 20 tasks receive no accepted solution".
- DORA's 2026 ROI report, citing Stanford research: "a 35–40% productivity gain on simple, greenfield tasks, its impact on complex, legacy brownfield code is often 10% or less".
- Factory's Legacy-Bench (vendor-authored): pass rates "from 16.9% to 42.5% across the 12 model-agent combinations", against more than 70% for the same models on SWE-bench Verified. And: "In 97% of failures, the agent believes it has solved the task".
- The VB6 case study: 70% of 331 catalogued instructions reproduced, 92% on low-complexity features and 47% on high.

**The evidence does not test the four practices.** Zoning, comprehension memos, characterization-first workflows and harness memory appear in neither paper. What the papers do show points to model capability and to verification:

- In the benchmark, changing the verifier's model matters "an order of magnitude more than its configuration".
- In the VB6 study, features were silently omitted "even when the files are completely provided", with a large context window and hand-written instruction files for each feature.

**Where scaffolding was measured, simpler did better.** From the case studies in Osmani's article, checked at their own sources: Asana used a five-sentence prompt, and a running notes file and a detailed prompt "made things worse". Teleport's write-up, which appears in the article as a paid advertisement, concludes "The more complicated the harness, the worse the overall performance seemed to be."

**In every verified success, the decisive input was the customer's own oracle**: a pre-existing test suite (Bun, Asana), the running application (Shopify), or production traffic replayed against old and new paths (Netflix). Two of the showcase migrations, Stripe's and Netflix's, used no agents at all.

**The verification result is the strongest finding, and it belongs to the first thesis.** In SWE Refactor Bench, 118 of 520 runs passed every fixed behavioural check, and only 28 were accepted. Thirty had not migrated at all: "Stage II gives all 30 full marks; only Stage I stops them". Of the 88 that had, "the other 60 ( 68.2% ) had a counterexample found against them within the hour".

## How occupied the market is

- **Hyperscalers and model vendors sell the large migrations, and largely give them away.** AWS Transform's mainframe, Windows and VMware agents are free; AWS claims "4.5+ billion lines of code" processed. GitHub Copilot app modernization is bundled with Copilot. Google, IBM and Anthropic each have offerings or published methods.
- **Each of the four practices already exists as a product or feature.** Characterization and replay testing (Diffblue, Tusk Drift, Keploy, Google Dual Run, Mechanical Orchard). Comprehension and code graphs (CAST, Swimm, Augment, Sourcegraph, Unblocked). Blast radius (CodeScene, Pharaoh). Institutional memory (Qodo's learned rules, Greptile, Unblocked).
- **Specialist startups are small, and some have left.** Seed rounds of about 5 to 7 million USD for two on-premises specialists; Grit was acquired and its product withdrawn; Bloop left COBOL migration.
- **The buyers with budget are regulated enterprises** that want references, on-premises deployment and an integrator.

## Assessment

**As a separate product, the brownfield thesis is weaker than the first.**

1. Its four practices are process. Anyone can reproduce them as a prompt, a skill file or a connector, and the vendors with models and distribution publish them as free guidance.
2. The asset that decided every success, the customer's own oracle, is something a tool cannot supply.
3. The evidence that agents struggle here does not show that a specialised harness would fix it. Where it points anywhere, it points to model capability, which we do not control, and to verification.
4. A team with no model, no customers and no vertical (decision D2) lacks what the buyers ask for. Any foothold found (auditing migrations done by others, one long-tail stack end to end, a zoning and memory layer) means choosing a vertical and starting with services-heavy work.

**As the first market for the evidence layer, it is the best fit found so far.**

1. It answers the open question of who the buyer is: teams where constraints live outside the code, tests under-describe behaviour, and a wrong change is expensive.
2. Osmani's practices are the evidence layer in brownfield terms: pin the behaviour before the agent works, by a separate pass or a person; let autonomy follow blast radius, not the model's confidence; lead review with intent, changed invariants, test results and parity mismatches.
3. The best measurement of the false-pass problem anywhere in our research comes from brownfield work.
4. Migration has a free oracle that ordinary change lacks: the old system. That eases the hardest open question about the evidence layer, where contracts come from.

## What it changes in the first thesis

**"A deterministic verdict from the customer's own checks" is not enough as worded.** In the benchmark, the fixed checks alone would have accepted 118 runs, of which 28 deserved it. Two further things did the work:

- a *completeness audit*: did the change actually happen. The paper used a model judge for it, agreeing with humans "89.7% of the time";
- a *counterexample search*: agents writing new tests to find hidden behavioural differences. Its result depended on who searched: "retire the two strongest and the remaining four would accept 46 submissions instead of 28".

A distinction worth keeping: the search is done by a model, but what it produces is an executable failing test. The evidence can stay executable even where finding it needs a model.

The layer would then be three parts, with the false-pass rate measured across all three: fixed checks, a completeness audit, and a counterexample search. This is a proposed refinement for the thesis discussion.

## Recommendation for the thesis discussion

Do not pursue brownfield as a second product. Carry it into the first thesis in two ways: as the candidate first market, and as the reason to widen the verdict from fixed checks to fixed checks plus a completeness audit plus a counterexample search.
