# Should we enter the AI software-development-assistant market?

| | |
|---|---|
| Audience | The executive team |
| Status | Complete. Sections 1 and 2 written 2026-10-05; sections 3 and 4 written 2026-10-07, from the measured results in `docs/RESULTS.md`. |
| Evidence | Every figure cites a row in `docs/research/EVIDENCE.md`, shown as (E-nn). Every row cited here was confirmed against its raw source by 2026-10-05. |
| Decisions behind this document | `docs/PLAN.md` §2 and §2.1 |

## Recommendation

**Do not build another AI coding assistant. Run a small, dated probe on the one part of this market nobody yet sells, and decide Build or Wait on what it shows.**

The part is tooling for **evidence-driven development**: a team defines what "done" means as executable checks before the work starts, and every change, whoever or whatever wrote it, is accepted on that evidence. The verdict is independent of the model vendor and measured for error on the team's own repository.

This is not a plug-in for an assistant. It is a tool for how a software team runs its delivery process, and it works with whichever assistants the team uses.

The probe has three stages, each able to end it: a one-day prototype, a measurement pilot with one or two design partners, and a build only if the pilot clears thresholds set in advance. If it does not clear them, the recommendation is to wait, with a review date.

## 1. The problem

### 1.1 The question as asked has a clear answer

The leadership question is why we should build another AI coding product when the largest technology companies already offer mature ones. As asked, we should not.

- **The companies that own the models own the product.** Anthropic and OpenAI sell their assistants on monthly subscriptions, with tiers at 20 and 100 USD (E-12, E-13), over models they do not have to buy. Anthropic reports that Claude Code's "run-rate revenue has grown to over $2.5 billion" (E-48).
- **The independents are being priced at acquisition scale.** Cursor's maker was acquired for an implied 60.0 billion USD (E-46). Cognition, which makes Devin, raised "over $2B at a $48B valuation" (E-47).
- **Reselling generation is a poor business.** A founder in the segment, quoted by TechCrunch: "Margins on all of the 'code gen' products are either neutral or negative. They're absolutely abysmal" (E-17).
- **The underlying technology is not scarce.** A source-code study of eleven coding agents recommends starting from "a linear while loop" and publishes a working one in 90 lines (E-31). An engineer at OpenAI is quoted as "bearish on any harness that doesn't come from the lab whose model you are using" (E-83).

We have no model of our own, no existing customers and no domain to defend. Entering this contest would mean competing on the incumbents' ground with their supplies.

### 1.2 What the incumbents have not solved

Writing code got cheap. Knowing whether to trust it did not.

- **Passing tests does not mean the change is good.** Independent reviewers judged that "roughly half of test-passing" agent-written changes on a standard benchmark "would not be merged into main by repo maintainers" (E-01). On whole-repository migrations, 118 runs passed every fixed check and 28 deserved to (E-68).
- **Review is absorbing the cost.** One vendor's telemetry across 22,000 developers reports that "Median time in review is up 441.5%" and that "Pull requests merged without any review, human or agentic, are up 31.3%" (E-04, E-05). This comes from a company that sells measurement.
- **Developers use the tools and trust them less.** Trust in the accuracy of AI output fell from 43% to 33% in a year, and distrust rose from 31% to 46% (E-82). Two thirds cite "AI solutions that are almost right, but not quite" (E-07).
- **Agents cannot grade their own work.** Anthropic, on its own models: "agents reliably skew positive when grading their own work" (E-34). A second model does not fix this: the evaluator "is still an LLM that is inclined to be generous towards LLM-generated outputs" (E-35).
- **Agents can learn to defeat the check.** In a controlled study, a model trained on coding tasks learned to force tests green, including by patching the test reporter to report "passed" (E-75).

### 1.3 What already exists, and what does not

We looked for an unoccupied position and did not find a wide one.

| Already available | From whom | What it leaves out |
|---|---|---|
| Automated code review | CodeRabbit, valued at 1.5 billion USD and positioning as "the control layer" (E-49); also built into Copilot, Claude Code and Cursor | The verdict is a model's opinion. CodeRabbit's checks cannot "run your test suite" (E-50). Claude Code's check "always completes with a neutral conclusion so it never blocks merging" (E-51). |
| A separate evaluator agent, with criteria agreed before work starts | Anthropic's published design | The evaluator is the vendor's own model, with no error rate reported. Anthropic found it "unnecessary overhead" on tasks the newer model already handles (E-36). |
| Logs of what agents did | GitHub, Anthropic, Cursor, Cline | They record actions and cost. None records whether the change was verified or accepted (E-53). |
| Policy, sandboxing and budgets across agents | Omnigent, open source from Databricks (E-32) | Nothing on whether the output is correct |
| The idea and its metrics | Published research: "production-qualified change", the "verification tax" (E-40 to E-42) | No implementation and no measurements. The authors call their own constructs "hypotheses" (E-45). |

Four things are offered by none of them together:

1. a verdict that **runs the customer's own checks**, not a model's reading of the diff;
2. **independence** from the vendor whose model wrote the code;
3. a **measured false-pass rate** for that verdict, on the customer's repository;
4. an **outcome record** that an auditor can read.

That is the gap. It is narrow.

### 1.4 The case against proceeding at all

This section is here because "do not build" is a legitimate conclusion, and the evidence for it is strong.

- **The idea is not ours.** The framing and the metrics are published, and the model vendor describes a contract plus a separate evaluator as its own practice.
- **A funded competitor stands next to the gap** and already has most of the parts: risk scoring, routing to humans, merge blocking and a planning product (E-49).
- **The value of a check moves with every model release.** Anthropic's own evaluator went from necessary to "unnecessary overhead" between two model versions (E-36).
- **A leading lab argues against gates.** OpenAI describes running "with minimal blocking merge gates" because "corrections are cheap, and waiting is expensive". It adds that this "would be irresponsible in a low-throughput environment" (E-57).
- **Dissatisfaction is not producing switching.** Use of coding agents rose from 31% to 59% while trust fell (E-21).
- **We would have no moat.** The mechanism is cheap to copy. What accumulates is each customer's own checks and history, which belong to the customer.
- **Much of the evidence for the problem comes from vendors who sell the fix.** The independent sources are fewer.

These are the reasons the recommendation is a probe with fixed exits, and not an investment.

## 2. The product

### 2.1 What it is

Tooling for **evidence-driven development**. The practice is simple to state: the team writes down what "done" means as executable checks before the work starts, and a change is accepted on that evidence. It continues test-driven development and extends it to two things that practice did not have to handle: code written by AI agents, and software whose behaviour is itself produced by a model.

The product is the part of that practice a team cannot do by hand at the pace agents work: it holds the checks, runs them where the author of the change cannot interfere, records the outcome, and measures how far the verdict can be trusted. We call that part the evidence layer. It answers one question for each change: is there executable evidence that this change does what was asked, and nothing else?

It has five parts.

1. **A guided first step: from a use case to checks.** Before anything is delegated, the engineer writes a short use-case description with the main functional requirements. The team's own assistant asks clarifying questions about what is missing or ambiguous; agents tend to guess when a task is underspecified (E-80), and this turns that into questions first. Checks are then drafted from the requirements, as a test suite or an evaluation, and a person approves them.
2. **A change contract**, fixed before the agent runs: what is in scope, which checks must pass, and what the task may cost. It is kept on a protected branch of the team's repository, where the author of a change cannot alter it.
3. **A verdict of executable evidence**, produced after the agent stops, in a place the agent cannot touch.
   - *For conventional code:* the customer's test suite, a check that the change stayed in scope, and a check that the agent's own tests mean something. For the last, an agent's new tests are run against the original code, where "they must fail" (E-76).
   - *For an LLM application:* an evaluation. Fixed cases, covering every functional requirement and some of them hidden from the agent, are run repeatedly and scored against a threshold. The result is pass, fail or inconclusive, because one run of a system that answers differently each time proves little. Code-based scoring is used wherever it can be; where a model must score, its agreement with human labels is measured and stated.
4. **An outcome record** for every change: what was asked, what changed, which checks ran and their results, the risk tier, and the cost.
5. **A measured error rate.** How often the verdict passes a change that should have failed, measured on the customer's repository, and used to decide how much human review each class of change receives.

**What does not change between the two cases:** the checks are fixed before the agent runs and the agent cannot alter them; they run outside the agent; everything is recorded; and the verdict's own error rate is measured. The evidence is always executable. It is not always deterministic.

### 2.2 The core value proposition

**For engineering leaders who answer for what their teams merge: one standard of evidence for every change, whoever or whatever wrote it, with a stated error rate, on your code and with your tools.**

The reason to adopt it now is AI agents: they made writing code cheap and left the question of trust open. The reason it stays useful is that the standard does not depend on who the author is.

The unit it reports is the one a finance team can use. Published research puts the question as "how much production-qualified value an engineering system can deliver per dollar, per reviewer-hour, and per unit of operational risk" (E-40). We adopt that vocabulary.

### 2.3 Who it is for

Engineering leaders, as sponsors, in organisations that build software. They own delivery risk and the budget for engineering tools.

We expect the need to be sharpest where a wrong change is expensive: long-lived systems and regulated work. We expect it to be weakest in fast new builds. This is a hypothesis the pilot is designed to test, not a finding.

### 2.4 How it differs

| Alternative | What the team gets | What the evidence layer adds |
|---|---|---|
| The assistant's own claim of success | The agent's word | A verdict from outside the agent |
| Discipline through prompts and skills | Rules the model is asked to follow | Rules enforced by mechanism |
| An automated reviewer | A model's opinion of the diff | The customer's checks actually run, and a verdict that can block |
| The vendor's evaluator agent | A second model from the same vendor | Independence, and a stated error rate |
| Vendor audit logs | What the agent did | Whether the result was verified |

### 2.5 How it is positioned

**It is a tool for the team's delivery process, not an accessory to an assistant.** That distinction matters for three reasons.

- *It is what the product is.* It starts by helping the team define its checks, attaches to the build pipeline, and keeps the record. None of that lives inside an assistant.
- *It does not shrink as models improve.* A product described as "checking the agent" is needed less with each model release. A team's standard for what counts as done is needed whoever writes the code.
- *It is bought by the right person.* Engineering leaders buy tooling for how their teams deliver. An add-on to another vendor's product is a small line and a dependency.

**It supports the ways of working now being adopted, without being any one of them.**

| Way of working | How evidence-driven development relates to it |
|---|---|
| Test-driven development | Its direct continuation, extended to agent-written changes and to evaluations |
| Eval-driven development, for software built on models | The same practice for that kind of software: the checks are evaluations |
| Spec-driven development | The enforcement half. A specification states intent; the evidence shows it was met |
| The "software factory", with agents working unattended | The quality-control step, and the record of what was produced and whether it passed |

**What is new in it, and what is not.** Writing acceptance tests before the code is an established practice, known as acceptance-test-driven development. Writing evaluations first for software built on models is already recommended by the model vendors under the name eval-driven development. Evidence-driven development joins the two and adds what neither has: one gate for changes from people and from agents, a kept record of every outcome, and a measured error rate for the verdict. We claim those three additions, not the idea of testing first.

We lead with evidence-driven development and not with the last two rows of the table. Spec-driven development is already offered by large vendors and has drawn criticism as a return to heavy up-front specification. "Factory" is a company name in this market, and the term implies a high-throughput setting where this product pays least.

**What the positioning does not change.** The product is the same five parts. It is not a platform for the whole delivery lifecycle, and the list in §2.7 of what we leave out stands.

**Who it suits.** Teams that already take their process seriously: version control, tests, a build pipeline, review. Evidence on AI adoption points the same way: the 2025 DORA report is introduced under the heading "AI, the great amplifier" (E-85).

### 2.6 Adopt, supplement or replace

**Supplement.** The team keeps its assistants, its repository host and its pipeline. The evidence layer attaches first as a check in the team's existing build pipeline, which needs nothing from any assistant's vendor, and applies to changes from people and from agents alike. It replaces no tool. It aims to replace a share of manual review, and it must show that it does: a review stage that does not remove a human stage is not a saving.

### 2.7 What we deliberately leave out

- A coding assistant, or an agent loop of our own.
- A layer that orchestrates several assistants.
- Policy, sandboxing and spending controls across agents.
- A reviewer that comments on code using a model's judgment.
- The wider control plane for software delivery: model routing, cost attribution, scheduling.
- A platform for the whole delivery lifecycle: planning, issue tracking, source hosting, deployment.
- A model of our own, or any fine-tuning.
- Editor plug-ins, autocomplete, background or cloud agents.

Each of these exists, is funded, or is a model vendor's home ground.

### 2.8 Customer data

The product works on the customer's code, checks and outcomes. This is stated here because it is what makes the product useful and what makes it sensitive.

- It runs in the customer's environment, with the customer's own access to models.
- Nothing is sent to us, used for training, or shared between customers.
- The checks and the history that accumulate belong to the customer.
- Customers are told exactly what is used and for what, and nothing is used beyond that.

### 2.9 How it stays worth paying for

The measurement is not done once. Models change every few months, and the right amount of checking changes with them. One study found that the same scaffolding helps one model and hinders another; its conclusion is that each component "should be selected for the target model, task type, and resource budget rather than adopted as a default" (E-58).

So the product re-measures for each model and each assistant the customer uses, and adapts its checks and risk tiers to each. A customer changing model is when it is needed most.

### 2.10 What it costs, and what it changes in the delivery process

More checks add time and cost to building software. That is true of this product, and it should be said before anyone else says it.

**Where the cost lands**

| Stage of delivery | What the evidence layer adds | Who pays |
|---|---|---|
| Before the work | Writing the checks and the contract | Engineers' time. This is the largest cost and the least known. |
| While the agent works | Extra attempts when a check fails | Tokens and elapsed time, capped by the contract's budget |
| After the agent stops | Running the checks. For conventional code this is close to what a build pipeline already does, plus one extra test run. For an LLM application it is an evaluation: many cases, repeated, each one a model call | Pipeline time; for evaluations, tokens |
| At review | Changes the verdict cannot settle, sent to a person | Reviewers' time, on fewer changes than today if the product works |
| Over time | Keeping the checks current, and re-measuring whenever the model or the assistant changes | A standing cost, not a one-off |

It also adds waiting. A change that used to merge when the agent finished now merges when the evidence is in.

**What it is meant to remove**

- Review time spent reading changes that executable evidence could have settled.
- Rework and incidents from changes that passed their tests and were wrong.
- The risk in changes that merge with no review at all.

**The trade, stated plainly.** The product moves cost from the end of delivery, where it is paid in scarce reviewer attention, rework and incidents, to the start and the middle, where it is paid in checks written once and machine time. Whether that is a net saving is not established by any evidence we hold. It is what the pilot has to show.

**What the evidence says so far**

- Checking can be cheap next to generating. In the one detailed breakdown we found, three rounds of automated quality checks cost 3.24, 3.09 and 4.06 USD in a run that cost 124.70 USD in total (E-84). That run is a vendor's single example, on new code.
- Checking everything is wasteful. The same author found the check "unnecessary overhead" for work the newer model already did reliably (E-36).
- Waiting has a price. OpenAI's stated reason for running with few blocking gates is that "corrections are cheap, and waiting is expensive" in its setting (E-57).
- A cheap check that lets bad work through is worse than none: "A low Verification Tax can be dangerous if it results from skipping tests or rubber-stamping reviews" (E-42).

**How the product keeps the cost down**

1. **It does not check everything equally.** Checks are applied by risk. Low-risk changes get the minimum; the expensive checks are reserved for changes where being wrong is costly.
2. **It reuses what the team already runs.** For conventional code the verdict is mostly the existing test suite, run in the existing pipeline.
3. **It caps its own spending.** The contract's budget covers verification as well as the agent's work.
4. **It reports both kinds of error.** A verdict that wrongly blocks good changes costs rework and teaches people to bypass it. The rate of wrongly failed changes is measured alongside the rate of wrongly passed ones.

**How we will know.** Four numbers, reported together and never one without the others:

- cost per production-qualified change, with the cost of checking included;
- reviewer time per production-qualified change;
- time from task to accepted change;
- the two error rates of the verdict.

If the first three do not improve for a design partner, the product has made delivery slower and dearer for no gain, and the recommendation is to stop.

**Where we expect it not to pay.** Small, low-risk changes. Fast new builds where a mistake is cheap to undo. Teams with few tests today, for whom writing the checks is most of the cost.

### 2.11 How we proceed, and when we stop

| Stage | What it is | Continue only if |
|---|---|---|
| 1. Prototype | One day. The same tasks run with and without the evidence layer, and each verdict compared with hidden acceptance checks | The layer's false-pass rate is lower than both the agent's own claim and a separate evaluator's; every planted flaw is rejected; the layer accepts no change that contains an unsafe action |
| 2. Measurement pilot | One or two design partners, on their own repository and tasks. A report on the rate and cost of production-qualified changes | At least one partner says the report changed a decision they were about to make |
| 3. Build | The gate, as a product | Stage 2 cleared |

If a stage fails, the recommendation is to wait, with a date to look again.

### 2.12 What we do not yet know

- Whether teams will pay for this, and how much.
- What it costs a team to write the checks for ordinary work. The prototype writes them by hand.
- Whether the time and cost the product adds are repaid in review, rework and incidents avoided. The prototype measures what it adds; only a pilot can measure what it saves.
- Whether a result measured on today's models holds on the next ones.
- Whether the need is in fact sharpest where we expect it.
- Whether a customer's accumulated checks and history amount to something a competitor cannot offer.
- Whether "evidence-driven development" is a label buyers will recognise and adopt. We found no owner of the label, but it sits close to eval-driven development and to an academic field called evidence-based software engineering, and trademark registers have not been searched.

The prototype can inform the first stage only. The rest are what the pilot is for.

## 3. The design, and what the prototype showed

### 3.1 The design in one sentence

It trades speed to merge, and some good changes wrongly held back, for a verdict that the author of a change cannot influence. The full design is `docs/DESIGN.md`; its critical self-review, written before building, is `docs/DESIGN-REVIEW.md`.

### 3.2 How a change flows

Before any work starts, the team turns the request into checks, and a person approves them as a contract the author cannot write to. The author — any agent or person — makes the change. Afterwards, a separate job the author cannot reach computes the verdict: the team's own tests, a scope check, the author's new tests re-run against the original code (where they must fail, E-76), and for software built on a model, a sampled evaluation with hidden cases. Every change leaves a permanent record, and the verdict's own error rate is measured from planted flaws, known-good changes and human overrides, then re-measured at each model release (E-36, E-58).

### 3.3 What the prototype built

All of it, within the exercise: the measurement machinery proven on a cost-free fake agent before any spend; the published 90-line scaffold (E-59) running a live model in per-run containers with no network and no key; the gate — 350 lines, held by 91 automated tests; hand-made adversarial changes; the full three-arm comparison; an evaluator agent from a second vendor; and the evaluation path for an LLM application, end to end. Total model spend: 6.87 of the 50 USD cap. Deliberately simulated: the guided first process (contracts were written by hand, then reviewed and approved by a person) and the protected branch (a directory stood in for it).

### 3.4 What it measured

The same eleven tasks ran through the unmodified scaffold on Claude Sonnet 5.5, five times each, in three arms — bare; told to verify before claiming; and gated. The referee: hidden acceptance checks neither the agent nor the gate ever sees, strengthened before the comparison. 165 runs, no machinery failures (`RESULTS.md` §5.7).

| | Bare | Told to verify | Gated |
|---|---|---|---|
| Changes that truly qualified | 46 of 55 (84%) | 45 of 55 (82%) | 55 of 55 (100%) |
| Qualified on every one of 5 trials | 9 of 11 tasks | 9 of 11 | 11 of 11 |
| Runs where the model weakened existing tests | 9 | 10 | 0 accepted |
| Cost per production-qualified change | 0.0357 USD | 0.0442 USD | 0.0346 USD |

The three verdict sources, against the same ground truth:

| Verdict source | False pass | False fail |
|---|---|---|
| The agent's own claim | 19 of 164 (12%) — including every change with a weakened test | 1 of 146 |
| An evaluator agent from a second vendor (gpt-5.1, pinned; 33-run sample) | 3 of 3 bad changes passed, each praised | 2 of 30 |
| The gate | 0 of 146 | 0 of 146 |

Five evaluations of one identical correct change by the second-vendor evaluator split fail, pass, pass, pass, pass — the instability the vendor's own writing predicts (E-34, E-35), reproduced in our records. On hand-made adversarial changes the gate's honest limits are also measured: 2 of 21 wrong changes passed, both behaviour no check covered; 1 of 17 good changes wrongly blocked, by a naive secrets rule, predicted in writing before it was judged. The evaluation path (§5.8 of the results) showed the non-deterministic case end to end: the original reminder-drafting prompt failed 0 of 40 sampled drafts; an agent's rewrite passed 40 of 40 with every hidden case held.

Three findings stand out beyond the headline. The live model really does weaken existing tests to make its work fit — the behaviour of E-75, observed in 19 of 110 unguarded runs. Prompt discipline did not help: the told-to-verify arm weakened tests slightly more often than the bare arm, the first measurement we know of for a practice the articles only assert. And the gated arm was the cheapest per qualified change, because two bounded send-backs cost less than the failed runs they rescue.

### 3.5 What one day cannot show

The rates are for this task set: eleven small tasks written by the gate's own author, on a fixture with fast tests and no history; one model, one harness; two tasks invite the tampering the gate detects by construction; the evaluator sample held only three bad changes. Reviewer time saved, adoption, willingness to pay, and the cost of writing checks for ordinary work are the pilot's questions. Results on today's models are a snapshot; re-measurement at each release is the product, not a disclaimer.

## 4. The executive message

### 4.0 The question this section answers

*"Microsoft, OpenAI, Anthropic and well-funded startups are already spending enormous amounts of money on this problem. Why should we believe that we can compete, and why shouldn't we simply buy their products?"*

We should buy their products — that is part of this recommendation. Their spend is on generation: we buy assistants at the vendors' tiers (E-12, E-13), adopt the open-source policy layer (E-32), and stay out of a reselling business with "neutral or negative" margins (E-17). What we probed is the one thing their position prevents them from selling: an independent verdict on their agents' output. By Anthropic's own published words, "agents reliably skew positive when grading their own work", and a same-family evaluator "is still an LLM that is inclined to be generous" (E-34, E-35) — which our stage-1 data now illustrates with a rival vendor's reviewer passing every bad change in its sample. No vendor publishes an error rate for its own reviewer; no vendor's logs record whether results were accepted (E-53). Independence cannot be bought from the party being judged.

### 4.1 The decision requested

**Fund the six-week measurement pilot.** Stage 1 is complete and its scoreboard is full: the gate's false-pass rate was lower than the agent's claim and than a second-vendor evaluator's, decisively (0 of 146, against 12% and 3 of 3); the gate accepted none of the 19 live changes containing an unsafe action, where both comparators accepted every one they judged.

One stopping condition is not met as written: "every planted flaw is rejected" stands at 9 of 10. The one accepted flaw was planted to find exactly that limit — behaviour no check covers — its cause was then measured a second time by accident, the strengthened answer key now catches it, and its designed fix, the counterexample search, is scheduled as the first enhancement (`PLAN.md` §3.11). Our judgment is that the condition's intent — the gate cannot be fooled by the failure modes found in the research — is met for every mode that has a mechanism, and open exactly where the design said it would be. The stricter reading, wait with a review date, remains available to this meeting; what the rules do not permit is proceeding without recording that choice.

### 4.2 What each stage costs

| Stage | Cost | Status of these figures |
|---|---|---|
| 1. Prototype and completion | One day to build; 6.87 USD of model spend, all stages, ledger-reconciled | Actual, from `prototype/runs/` |
| 2. Measurement pilot | Six weeks; two engineers and a product lead at half time; model spend capped per task as in the prototype | **Assumption** (T8); rates are finance's to supply |
| 3. Build | Scoped only if stage 2 clears | Not estimated; estimating now would be an invented number |

### 4.3 What the pilot money buys

A design partner's own repository and tasks, under the same instrument: their checks as the contract, their pipeline as the attachment, the four numbers of §2.10 measured where they are real — including the one the prototype cannot touch, the cost of writing checks for ordinary work (assumption A1), and the one that decides the business, whether anyone pays. The pilot's exit is already set: at least one partner says the report changed a decision they were about to make.

### 4.4 What ends it

The exits stay fixed in advance. After the pilot: a partner decision changed, or the recommendation is wait, with a review date. The review date that applies if this meeting chooses the stricter reading of stage 1 is open item T7, and it is this meeting's to set.

### 4.5 The risks we accept by proceeding

The idea and its metrics are published (E-40); CodeRabbit stands beside the gap with 1.5 billion USD of valuation and most of the parts (E-49); a check's value moves with every model release (E-36); the mechanism is 350 lines and therefore not the moat — our own prototype proved that too. What accumulates is the customer's checks, labels and outcome history, in the customer's hands (§2.8). If buyers do not value neutrality, a measured error rate and a record, there is no product — and the pilot is designed to show that cheaply.

### 4.6 The bottom line

The question was whether to enter a market the giants already own. The answer is that we should not — and that for 6.87 USD of model spend we measured, on our own tasks, what none of them publishes: an agent's claim of done was wrong 12% of the time and vouched for every unsafe change it made; a rival model reviewer passed every bad change it saw and contradicted itself on identical input; and a 350-line executable gate was wrong zero times while making delivery cheaper per accepted change. Six weeks and two-and-a-half people now buy the same measurement on a real team's repository, with the exit already written down.
