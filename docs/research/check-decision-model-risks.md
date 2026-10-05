# Check of the risk and crowdedness claims about decision models

| | |
|---|---|
| Notes dated | 2026-10-02 |
| Checked on | 2026-10-05 |
| Method | Checked at primary sources by a Claude Code sub-agent. arXiv 2609.29769 was read in full for the main text, limitations and most appendices. Negative findings ("none found") rest on a handful of searches. |
| Status | Record as received. |
| Used for | PLAN §3.10, ROADMAP open questions T3, T7 and T9 |

Tags in this file: **[P]** confirmed in the publisher's raw page; **[P-summary]** seen only through a summarising fetch or a reader proxy; **[S]** secondary source or search snippet only.

Checked 2026-10-05. Tags: **[P]** confirmed in the publisher's raw page (curl + grep/read); **[P-summary]** seen only via a summarising fetch; **[S]** secondary only. No figure below is rounded or estimated by me.

## RISK claims

### R1. "Wrong in the same places" (arXiv 2609.29769)

**Finding: Confirmed for rubric judging of text; NOT tested on code. The notes' inference ("deterministic checks first") is the notes' own; the paper does not say it.**

- **Paper.** "Jev vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places", Delip Rao and Chris Callison-Burch (University of Pennsylvania). Submitted 24 Sep 2026; v2 dated 28 Sep 2026. https://arxiv.org/abs/2609.29769 [P]
- **What was compared.** One decision model (Jev, `jev-latest`, logged as `jev-1.13.0`, in Noul / Choice / Score framings) against three "flash-tier" LLM judges: GPT-5.6 Luna, Gemini 3.8 Flash, DeepSeek V4.1 Flash (via OpenRouter). All ran in the authors' AutoRubric harness on "the same 5,003 pairs from nine panels, sampled from seven public benchmarks with human judgments". Binary panels: RiceChem (819 pairs), HealthBench (406). Ordinal panels: ELLIPSE (1,548), FED-Turn (600), FED-Dialogue (250), HelpSteer2 (360), LFQA (360), USR-TC (360), USR-PC (300). LLM judges ran per-criterion, whole-rubric, and at high reasoning effort. [P]
- **Code-related judgments: none.** The units are chemistry answers, health chatbot replies, learner essays, dialogue turns, assistant replies and ELI5 answers. A search of the full text for code/program/software/diff finds only the authors' analysis code. [P]
- **Error overlap, quoted.**
  - "On Jev's most confident errors, 96.0% of LLM verdicts repeat its answer, against 50.3% under independence." Detail: "242 of the 252 LLM verdicts on these 84 pairs (96.0%) repeat its answer"; the sample is Jev Choice's 12 most confident errors on each of the seven ordinal panels.
  - HealthBench (binary): "The three LLM judges give Jev's answer in 32 of their 36 verdicts on them, against 10.0 that the independence baseline expects." Over all 92 Jev Noul errors there: "55.8% of their verdicts, against a baseline of 27.5%".
  - Over all of Jev Choice's errors, the repeat share "beats the baseline on every ordinal panel, by 18.8 to 34.2 points on six and 8.6 on ELLIPSE".
  - The overlap is worst exactly where a gate would trust the cheap model: repeats "peak on every panel in Jev's top confidence band (80.5% to 92.8% against 33.6% to 63.7%...); these are the verdicts a cascade keeps."
  - Reasoning does not help: "more reasoning did not make the LLM judges' errors less like Jev's."
- **Consequence for cascades and juries.** "In no condition does a cascade's gain over its panel's best single judge exceed 2.7 points (oracle) or 2.5 (cross-fitted)". Juries: the LLM median "gives Jev's wrong answer on 82 of the 84 confident errors". Cost side is real: cross-fitted cascades "cost 16% to 48% as much as that judge on six panels for 0.2 to 1.8 points less held-out accuracy". Authors' summary: "Jev is often a cheap substitute for a flash-tier LLM judge but a poor complement to one."
- **Accuracy and cost.** Jev "differs significantly in only 8 of 27 paired accuracy comparisons, leading mostly on binary panels and trailing only on ordinal ones"; LLM judges cost "16 to 325 times" and took "28 to 350 times" as long. Confidence quality: binary-panel ECE "0.056 to 0.096", AUROC "0.80 to 0.86"; ordinal AUROC "0.57 to 0.70" on six panels, "0.49" on ELLIPSE, "0.41" on LFQA factuality.
- **Recommendations (Appendix P).** Consider Jev in place of a flash-tier judge on binary checklist criteria; "Use a Jev-first cascade to lower cost, and expect little gain in accuracy"; "Do not expect a jury of these judges to beat the most accurate matched judge"; "Check confidence per criterion before deferring on it"; and, before trusting a cascade, measure "the share of repeated errors against an independence baseline" on your own labelled pairs. It does **not** recommend deterministic checks; it says "the next decision model should be designed from the start to get right what LLM judges get wrong."
- **Limits the authors state.** "We tested one typed classifier." LLM judges were flash-tier, zero-shot, default prompt: "No larger model, few-shot prompt..." was tried, and "though we tried no larger fallback, these results give little reason to expect one to err elsewhere." Ordinal panels are all English, four of seven are dialogue. Each ordinal panel was judged once. The confident-error sample is only 12 errors per panel, and "62 of the 72 confident errors on multi-rater panels" sit on pairs where human raters disagreed, so some "errors" may be contested labels. Cause is unresolved (unstated rating conventions, shared priors, literal reading): "our data cannot tell them apart." All cascade/jury results are post-hoc replays. Authors state they "are not incentivized by TypeSafe... or by its industry competitors"; funding is DARPA/IARPA.
- **What this means for the question being weighed.** The paper is direct evidence that a decision model is not an independent second opinion to an LLM judge on text rubrics, and it gives a cheap test (repeat share vs. independence baseline) to run on your own labelled code-review data. It is not evidence about code acceptance: transfer to diffs is an extrapolation in either direction.
- **How I read it.** Main text, limitations, and appendices A-G, I, J, L and P in full; H and K in part; M-O (release, whole-rubric, reasoning-effort detail) only through their summaries in the main text. Table cells were not individually checked.

### R2. Raw confidence overconfident, +6.7 to +15.3 pts (AnthusAI/Jev-Calibration)

**Finding: Confirmed, with a clarification of what the figures mean.** https://github.com/AnthusAI/Jev-Calibration (created 2026-09-19, pushed 2026-10-04) [P]

- The figures are **mean confidence minus accuracy**, not ECE, and they are for two question types, not a range of tasks: "Noul's mean confidence is 79.0% against 72.3% accuracy (+6.7 points; +1.3 without the neutral tier, whose labels are arbitrary). Choice's is 91.4% against 76.1% (+15.3; +9.1)."
- One task only: binary sentiment on a constructed dataset, "8,801 unique examples", split into calibration (5,280) and test (3,521); model `jev-1.13.0`. The "neutral" tier has "deliberately arbitrary labels", which inflates the headline gap.
- Post-hoc calibration worked: ECE of P(positive) "0.117" raw, "0.052" with Platt, "0.008" with isotonic. Data needed: "a few hundred labeled examples is enough to get most of the benefit"; "isotonic matched or beat Platt at every size from 20 to 5,280"; "Below ~50, treat a calibrator as a sanity check".
- Caveats in the repo: "Calibration makes the number trustworthy; it doesn't make Jev smarter"; "Calibration is per question, per model version. Refit when the question wording, data source, or model changes"; no confidence intervals. Anthus is a consultancy publishing its own study; no stated vendor tie.

### R3. "CoT still wins hard judgments"

**Finding: Partly confirmed. Several sources point this way, none is a clean head-to-head on hard code judgments, and the vendor claims the opposite for its own workloads.**

- arXiv 2609.29769: LLM judges lead only on ordinal criteria; "Gemini leads on ELLIPSE, FED-Dialogue, and HelpSteer2, most on ELLIPSE (16.4 points)". [P]
- Agentailor report AR-001 (dev.to summary, prices dated 23 Sep 2026; 191 scored items, one labeller who owns the agent): "Jev alone fell behind Sonnet"; "On narrow yes/no checks, Jev scored 96.3% and all three LLM judges scored 98.2%. On nuanced decision tables, Jev dropped to 80.6%." The LLM figure for decision tables is not in the summary. https://dev.to/ialijr/we-tried-replacing-our-llm-judges-with-jev-1en7 [P for the summary; full report not read]
- PostHog/jeeves (open reasoning variant; self-reported): "JevBench hard (111 public items)" Jev 0.730 vs Jeeves 0.865; same checkpoint "0.804" without thinking vs "0.840" with. https://github.com/PostHog/jeeves [P]
- Vendor docs list "System Two tasks: more layers of indirections" among things to avoid. https://docs.typesafe.ai/model-jaggedness/jev-1.13 (reviewed 2026-10-02) [P]
- Counter-claim (vendor): models "doing all the logic in their chain-of-thought... tends to do significantly worse than using the workflow itself". [P]

### R4. Vendor lock; open self-host fallbacks

**Finding: Partly confirmed.**

- Subsidy: vendor writes "We can't prove it isn't subsidized; we'll need the long-term to prove the sustainability of our pricing (which we expect to go down, not up)." Price "$0.042 / MTok", output "FREE". Jev is "available today in early access". The word "promo" was not found. https://typesafe.ai/blog/introducing-system-one-models-and-jev (15 Sep 2026) [P]
- Closed weights: stated by third parties, e.g. "Jev's weights and size are not published, nor is it offered for self-hosting" (arXiv 2609.28919) [S].
- Open reimplementations exist and are self-hostable. Kev (jaredpalmer/kev, Apache-2.0, 0.8B-27B, "Drop-in for Jev: the TypeSafe Python SDK works against a Kev server unchanged"). Self-reported comparison: "On new sources Kev-27B is within a point of Jev (0.851 vs 0.857), and Kev-4B and Kev-9B are within four points"; but "on the harder MMLU-Pro Kev-27B scores 0.675 against Jev's 0.840", and "Jev still ranks its answers better". Kev's caveat: "this isn't a controlled comparison". [P]
- "OpenJev" is not one project: TheoLeeCJ/SemIf-OpenJev (now "SemIf", reproduces the "interface pattern", not the model), razorback16/openjev, and others. No independent third-party accuracy comparison was found.

### R5. "Cannot hallucinate" = schema guarantee

**Finding: Confirmed (wording corrected).** Vendor wording is "can't hallucinate" (launch blog) and "Zero Hallucinations" (homepage). The only guarantee given is type/schema: "Our number is not empirical. Schema matching is guaranteed, thus we can confidently add 0% into the plots", and "No type errors... it is mathematically impossible." The vendor separately concedes "Jev isn't perfect" and documents nine failure modes, including adversarial content that "can move the answer". [P]

## CROWDEDNESS claims

### C1. Routers

**Finding: Corrected (RouteLLM), Confirmed (NotDiamond), Could not verify (Martian "exit").**

- RouteLLM: "matrix factorization is able to achieve 95% of GPT-4 performance using 26% GPT-4 calls, which is approximately 48% cheaper as compared to the random baseline" (MT Bench). 26% is the **share of calls sent to GPT-4, not 26% of cost**. https://lmsys.org/blog/2024-07-01-routellm/ [P]. Repo README: "reduce costs by up to 85% while maintaining 95% GPT-4 performance". [P]
- NotDiamond: homepage title "Model Routing for Coding Agents"; "the world's most powerful intelligent model router for coding agents". Its savings calculator is labelled "Modeled at equivalent output quality". https://www.notdiamond.ai [P]
- Martian: no dated exit announcement found. withmartian.com now presents as an interpretability research lab and links to "Thesean AI — A Lab Building Best Execution for LLMs" ("You don't want a model or a router"). A third-party directory marks the router profile "Stale · 2026-06-08". Reads as a repositioning/spin-out rather than a documented exit. [P for site content; S for the inference]

### C2. FrugalGPT

**Finding: Confirmed.** "FrugalGPT can match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost." arXiv 2305.05176, 9 May 2023. [P]

### C3. Granite Guardian 3.2

**Finding: Confirmed, narrowly.** Model card (ibm-granite/granite-guardian-3.2-5b): "**Function Calling Hallucination**: assistant's response contains function calls that have syntax or semantic errors based on the user query and available tool." It is a hallucination check on the call, not a judgment of whether the action is dangerous. [P]

### C4. Jev-as-judge

**Finding: Confirmed (openlayer); Could not verify "cascade" (Arize).**

- openlayer-ai/jevals: "Evals and guardrails for agents, using Jev-style decision models instead of an LLM judge"; includes a YAML tool-call gate and a `jevals calibrate` command for threshold selection from labelled data. Openlayer sells eval tooling. [P]
- Arize: "Jev-as-a-Judge: Building a remote evaluator in Arize AX with Jev" (arize.com/blog/jev-remote-evaluator/). The page returned HTTP 403; seen only in search results, which describe a remote evaluator, not a cascade. [S]. A Phoenix issue "Integrate JEV as an evaluator judge" (#16524, opened 2026-09-25) is open. [P]

### C5. "System 1 vs System 2 harness" vocabulary

**Finding: Confirmed.** Daily Dose of Data Science, Avi Chawla, 28 Sep 2026: "A System 1 harness asks the model to make a bounded judgment... A System 2 harness handles work whose path cannot be specified upfront." The section promotes HarnessRouter. harnessrouter.ai is a YC-backed product: "The world's first unified interface for agent harnesses", with an open-source "System One Harness" (confidence-gated agent loop for Jev-class models). [P]

### C6. redreamality "control the harness, control the cost"

**Finding: Corrected.** The blog (published 2026-09-27) is a summary of an Accenture Responsible AI preprint, arXiv 2609.28919, not original work. The 14-21% figure matches v1 ("recovers 14 to 21% of model spend... $3.3M to $5.0M a year"). Current v2 (26 Sep 2026), retitled "Harness Tokenomics: A Router for the Enterprise Agentic Control Plane" (Kwartler, Aqrawi, Abbasi), says "recovers 13 to 21% of model spend... $3.3M to $5.1M a year". Basis is **modelled**: "an emulated enterprise of 10,000 seats"; "The 46 conversations and 109 turns are synthetic"; "The enforcement point (gateway and hooks) and the user's view of the routing are specified but not built, so the case study runs every decision in the simulator, not behind a live harness." Jev is the classifier (accuracies "74% / 80% / 63% / 82%"). [P]

### C7. The two "still unclaimed" items

**(a) Shipped coding harness with a decision model as the main economic layer and end-to-end $/task: no counter-example found.** Nearest misses:
- arXiv 2609.28919 (above): Jev-driven routing for coding agents with dollar figures, but emulated, per-seat/year, not shipped. This is the closest prior claim to the idea. [P]
- darwintechlab/openjev: an opencode plugin for approval/routing decisions; publishes per-decision cost ("About $0.017 per 1,000 decisions"), not task-level cost. [P]
- devagrawal09/jev-review: Jev-staged code review; self-described "an experiment", no cost numbers. [P]
- HarnessRouter SystemOneHarness: publishes per-task cost (e.g. "$0.000265") but for non-coding demo tasks. [P]
- dev.to "Benchmarking Jev... in an agent harness" (Aitejiu): component benchmarks ("$2.19 total"), and negative results relevant here: "Model-difficulty routing 51% accuracy (no signal)", "Trajectory failure attribution AUROC 0.560 (random)". [P]

**(b) Closed-loop recalibration from harness outcomes: no shipped counter-example found; the idea is named as future work, and adjacent work exists.**
- arXiv 2609.28940 (Jev/Laya in pentest harnesses) proposes, as future work, "An online calibration mechanism that detects distribution shift (via prediction entropy or calibration error on a sliding window)". [P]
- powerpuff-kitty/agentic-harness issue #109 (open, 2026-09-18) plans per-decision-class threshold tuning on held-out data; offline, not outcome-fed. [P]
- jevals `calibrate`, Anthus, and arXiv 2608.17994 (risk-controlled judge thresholds) all calibrate offline on a labelled set. [P]
- arXiv 2608.08471 (SESG, Sangfor) is a production closed loop for guardrails, but it retrains the model on live failures; it does not recalibrate thresholds. [P, abstract only]
- Search coverage was a handful of queries; absence here is weak evidence.

### C8. Classifier-style calls already inside coding harnesses

- **Gemini CLI**: `packages/core/src/routing/strategies/` contains `classifierStrategy.ts`, `numericalClassifierStrategy.ts`, `gemmaClassifierStrategy.ts`. Prompt: "You are a specialized Task Routing AI... Choose between `flash` (SIMPLE) or `pro` (COMPLEX)"; the numerical variant returns a "Complexity Score from 1 to 100". [P]
- **Codex**: docs call it "Auto-review" (`approvals_reviewer = "auto_review"`), routing approval requests "through a reviewer agent"; source module is `codex-rs/core/src/guardian/`. "Smart Approvals" as a product name was not found in the docs page checked. [P]
- **Hermes**: `tools/approval_smart.py` defines `_smart_approve(command, description)`; the auxiliary LLM must "Respond with exactly one word: APPROVE, DENY, or ESCALATE". [P]
- **Claude Code**: "In auto mode, a second model, the classifier, reviews actions instead of you". https://code.claude.com/docs/en/permission-modes [P]
- **Omnigent**: policy `deny_trivial_to_expensive_model` "Classifies user messages as TRIVIAL or COMPLEX using the server LLM. Denies trivial tasks from using expensive models." (docs/POLICIES.md) [P]

## Summary

| Item | Verdict | One line |
|---|---|---|
| R1 | Confirmed (text rubrics only) | 96.0% of LLM verdicts repeat Jev's most confident errors vs 50.3% under independence; no code tasks tested; "deterministic checks first" is not the paper's recommendation |
| R2 | Confirmed, clarified | +6.7 (Noul) / +15.3 (Choice) are confidence minus accuracy on one sentiment dataset; isotonic cut ECE 0.117 to 0.008 with a few hundred labels |
| R3 | Partly confirmed | LLMs lead on ordinal/nuanced judgments (up to 16.4 points; Jev 80.6% on decision tables); no hard-code head-to-head; vendor claims the opposite |
| R4 | Partly confirmed | Vendor: "We can't prove it isn't subsidized"; Kev self-reports 0.851 vs Jev 0.857 but 0.675 vs 0.840 on MMLU-Pro; "promo" wording not found |
| R5 | Confirmed | "can't hallucinate" / "Zero Hallucinations" rests on "Schema matching is guaranteed"; "not empirical" |
| C1 | Corrected / unverified | RouteLLM 26% is GPT-4 calls, not cost; NotDiamond now routes for coding agents; no Martian exit announcement found |
| C2 | Confirmed | "up to 98% cost reduction" or +4% accuracy at equal cost |
| C3 | Confirmed, narrowly | Function-calling hallucination (syntax/semantic errors), not action risk |
| C4 | Partly confirmed | jevals confirmed; Arize post blocked (403), "cascade" not verified |
| C5 | Confirmed | Vocabulary in use since 28 Sep 2026; post promotes HarnessRouter |
| C6 | Corrected | Accenture arXiv paper; v2 says 13 to 21%, $3.3M to $5.1M; emulated, gateway "specified but not built" |
| C7a | No counter-example found | Closest is the emulated Accenture router; no shipped harness with end-to-end $/task |
| C7b | No counter-example found | Online recalibration appears only as proposed future work; existing calibration is offline |
| C8 | Confirmed (5 of 5) | All five harnesses use an LLM-classifier call for routing or approvals; Codex names it "Auto-review"/guardian |
