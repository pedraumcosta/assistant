# PROPOSAL.md — sections 3 and 4 (template)

<!-- Appended to docs/PROPOSAL.md in P7. Sections 1 and 2 already exist; P7 also
     revises them against the results (PLAN §6). Delete all comments before merging. -->

## 3. The design, and what the prototype showed

### 3.1 The design in one sentence

It trades speed to merge, and some good changes wrongly held back, for a verdict that the author of a change cannot influence. The full design is `docs/DESIGN.md`; this section is what an executive needs from it.

### 3.2 How a change flows

<!-- One paragraph and the DESIGN §3 diagram (or its single-image rendering).
     Before: engineer writes the use case, the assistant asks clarifying questions,
     checks are drafted, a person approves, the contract is fixed where the author
     cannot write. During: any agent or person makes the change; we add nothing.
     After: the verdict runs as a separate job; the change is routed by risk;
     everything is recorded; the record feeds the measurement. -->

{{diagram}}

### 3.3 What the design refuses to do

<!-- Three or four of the redlines (DESIGN §8.3), chosen for an executive audience:
     nothing passes when the verdict process breaks; the author cannot touch the
     checks, the contract or the verdict; no red-tier change lands without a person;
     customer code and records never leave the customer's environment. -->

### 3.4 What the prototype tested, in one table

| Question | How it was tested | Where the answer is |
|---|---|---|
| Does a deterministic policy stop unsafe actions? (H1) | Trap tasks across three arms | `RESULTS.md` §3 |
| Is the gated arm more consistent, not just luckier? (H2) | pass@1 and pass^k against hidden checks | |
| What does a qualified change cost? (H3) | PQC per dollar per arm, verification included | |
| **Is the gate's "pass" right more often than the agent's claim and a model reviewer's? (H4)** | False-pass rate of three verdict sources against hidden checks | |
| Can the gate itself be fooled? (H5) | Planted flaws, all-must-be-rejected | |
| What does the gate add in time, cost and wrongly blocked work? (H6) | Overhead and false-fail rate | |

### 3.5 What the prototype showed

<!-- Three to five sentences, each citing {{runs:...}}. Lead with H4, the claim.
     Every rate with its denominator; every speed or cost number paired with its
     quality number. Then one honest sentence on what surprised us, if anything did. -->

### 3.6 What one day cannot show

<!-- Lift the limitations from RESULTS.md §1 verbatim or tighter. This section is
     load-bearing for credibility: it is the reason stage 2 exists. -->

## 4. The executive message

<!-- The audience that decides is the CFO. The engineering leader is the sponsor;
     the CFO owns the money and will ask the brief's question. §4 is structured to
     answer it before the ask, and docs/templates/cfo-message.md is the one-page
     version of this section with the challenge-and-answer appendix. Keep the two
     consistent word for word where they overlap. -->

### 4.0 The question this section answers

*"Microsoft, OpenAI, Anthropic and well-funded startups are already spending enormous amounts of money on this problem. Why should we believe that we can compete, and why shouldn't we simply buy their products?"*

In three moves, expanded in the one-page CFO message:

1. **We agree, and buying their products is our recommendation.** Their spend is on generation; our teams should buy assistants like everyone else ({{E-12}}, {{E-13}}, {{E-17}}).
2. **What we probed is the one thing their position prevents them from selling:** a credible, independent verdict on their own agents' output ({{E-34}}, {{E-35}}), with the customer's own checks actually run ({{E-50}}), a measured error rate, and an outcome record ({{E-53}}). Buy–adopt–build, by layer: buy generation, adopt the open-source policy layer ({{E-32}}), build only the verdict and its measurement.
3. **The ask is priced so belief is unnecessary:** a staged probe with kill criteria fixed in advance, capped at the stage we are in.

### 4.1 The decision requested

<!-- KEEP EXACTLY ONE of the three branches. The choice is made by RESULTS.md §5,
     the kill-criteria scoreboard — not here. The same branch is kept in the deck. -->

**Branch A — the prototype cleared its exits: fund the measurement pilot.**

The gate's verdict was wrong less often than the agent's own claim and than a model reviewer's ({{runs:fp_gate}} against {{runs:fp_claim}} and {{runs:fp_evaluator}}, on {{runs:denominator}} changes); every planted flaw was rejected; no unsafe action ran under the gate. On that evidence we ask for a measurement pilot with one or two design partners, on their repository and their tasks. The pilot has its own exit, fixed now: we continue past it only if at least one partner says the report changed a decision they were about to make.

**Branch B — the prototype failed its exits: wait, with a review date.**

{{Which criterion failed and what the number was, plainly.}} The honest reading is that {{what the failure means: e.g. a model reviewer's verdict is already good enough that a deterministic gate adds too little / the gate itself was fooled}}. We recommend not entering now. We put a date on the decision rather than leaving it open: review on {{pedro:review_date}}, or earlier if {{reopening condition: a vendor publishes a false-pass rate; a procurement requirement for outcome records appears; a design partner asks for the measurement unprompted}}.

**Branch C — the prototype could not separate the verdict sources: wait, re-run with a budget.**

The design was not disproven; the sample the 50 USD cap allowed was too small to show a difference ({{runs:...}}, plausible ranges overlapping). The cheap next step is not a pilot but a bigger measurement: {{assumption: the re-run budget and scope}}. If leadership prefers not to fund the re-run, the recommendation reverts to Branch B with the same review date.

### 4.2 What each stage costs

<!-- T8. Stage 1 is actuals from the run files. Stage 2 figures are assumptions and say
     so. Loaded-cost rates are finance's to supply; this document multiplies nothing. -->

| Stage | Duration | People | Other costs | Status of these figures |
|---|---|---|---|---|
| 1. Prototype | One day | Done | {{runs:total_spend_usd}} model spend | Actual, from `prototype/runs/` |
| 2. Measurement pilot | 6 weeks | 2 engineers, a product lead at half time | Model spend cap of {{assumption:pilot_spend_cap}}; design partners' own model access | **Assumption** (PLAN §2.1 T8), to be revised with finance |
| 3. Build | Scoped only if stage 2 clears | — | — | Not estimated. Estimating it now would be invented numbers |

The pilot's staffing is a working assumption judged reasonable (T8). Finance supplies the loaded cost of the named roles; we do not invent rates (ADR-010).

### 4.3 What the pilot money buys

<!-- Only under Branch A. One short list: a measured false-pass rate on a real
     repository; the cost of writing contracts for ordinary work (the largest open
     assumption, A1); the four numbers of PROPOSAL §2.10 for a real team; and a
     named answer to whether anyone pays. -->

### 4.4 What ends it

The exits are fixed before the results exist, and they are Pedro's to tighten but not to loosen after the fact:

- After the prototype: {{restate T7 prototype criteria — already applied above}}.
- After the pilot: at least one design partner says the report changed a decision they were about to make. Otherwise: wait, with a review date.

### 4.5 The risks we are accepting by proceeding

<!-- Only under Branch A; under B/C replace with "The risks of waiting". Draw from
     PLAN §9 and PROPOSAL §1.4: the idea is published; CodeRabbit is adjacent and
     funded; a check's value moves with each model release; the mechanism is cheap
     to copy and our defensibility is thin (neutrality plus the customer's
     accumulating checks and labels). Each risk with the response, not reassurance. -->

### 4.5a What we will and will not report

<!-- Lift the vanity-vs-real table from docs/templates/cfo-message.md. The point:
     the product reports in units a finance team can audit (cost per
     production-qualified change, reviewer-hours, time-to-qualified-change, both
     error rates — always paired), never in adoption or volume vanity metrics. -->

### 4.6 The bottom line

<!-- Three sentences, no new facts: the question, the evidence-backed answer,
     the ask with its exit. Written last. -->
