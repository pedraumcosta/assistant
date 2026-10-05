# The CFO recommendation (template)

<!-- This is the one-page answer to the brief's question, delivered as a short
     executive recommendation. It is written to be spoken and defended, not only read.
     The proposal and deck carry the full case; this page is what the CFO keeps.
     Every {{...}} follows docs/templates/README.md conventions. -->

## The question, as asked

*"Microsoft, OpenAI, Anthropic and well-funded startups are already spending enormous amounts of money on this problem. Why should we believe that we can compete, and why shouldn't we simply buy their products?"*

## The answer, in three moves

**1. We agree, and we already recommend buying their products.** Their money is spent on generation — making agents write more code. We should not put a dollar against that: they own the models, subsidise their own assistants ({{E-12}}, {{E-13}}), and the resellers between them have "neutral or negative" margins ({{E-17}}). Our teams should buy assistants at {{verified seat price}} per seat like everyone else.

**2. What we probed is the one thing their position prevents them from selling: a credible verdict on their own agents' output.** Anthropic, on its own models: "agents reliably skew positive when grading their own work", and a second model from the same family "is still an LLM that is inclined to be generous" ({{E-34}}, {{E-35}}). A vendor grading its own agent is not a product the vendor can make credible, whatever it spends. Nobody — vendor or startup — sells the four parts together: a verdict that runs the customer's own checks ({{E-50}}), independence from the model vendor, a measured false-pass rate, an outcome record ({{E-53}}).

**3. We are not asking you to believe we can compete. We are asking for a probe priced so that belief is unnecessary.** {{Branch A: One day and {{runs:total_spend_usd}} bought the first evidence (below). Six more weeks and a small team buy the answer on a real customer.}} Each stage has a kill criterion fixed in advance; the downside is capped at the stage you are in.

## The math, in your units

| | What it is | Where the number comes from |
|---|---|---|
| **Build cost** | Stage 1: one day, {{runs:total_spend_usd}} (spent). Stage 2: 6 weeks, 2 engineers + a half-time product lead, model spend capped at {{assumption:pilot_spend_cap}} | Actuals from `prototype/runs/`; stage-2 staffing is a labelled assumption, rates from finance |
| **Run cost** (ours, at product stage) | The verdict runs in the customer's pipeline with the customer's model access. We resell no inference | By design (PROPOSAL §2.8). Context: inference averages ~23% of revenue at AI B2B companies {{S: verify}} — a cost structure we deliberately avoid |
| **Risk delta** | What a wrongly merged change costs (review time up 441.5%, unreviewed merges up 31.3% — {{E-04}}, {{E-05}}) against the verification tax the product adds ({{E-42}}) | The pilot measures both sides on a real team. We do not invent this number |

The unit everything reports in: **cost per production-qualified change, with the cost of checking included** ({{E-40}}). It is the unit a finance team can audit, and it is paired, always, with the verdict's error rates — a cheap gate that passes bad work is worse than none.

## Buy, adopt, or build — by layer

| Layer | Decision | Why |
|---|---|---|
| Assistants and generation | **Buy** ({{verified seat prices}}/seat) | Vendor-subsidised; features copy between vendors in months |
| Policy, sandbox, budgets across agents | **Adopt open source** ({{E-32}}) | Free and backed by a large vendor |
| Model-opinion code review | Buy if wanted | A model's opinion; cannot run our tests ({{E-50}}) or block ({{E-51}}) |
| The verdict, its measured error rate, the outcome record | **The only build** | Sold by no one ({{E-50}}, {{E-51}}, {{E-53}}); credible from no model vendor ({{E-34}}) |

## What we will and will not report to you

| We will not report (vanity) | We will report (real, always paired) |
|---|---|
| Lines or share of AI-written code | Cost per production-qualified change |
| Suggestion-acceptance rates | Reviewer-hours per qualified change |
| Active seats, PRs per week alone | Time from task to qualified change |
| A pass rate by itself | The verdict's false-pass **and** false-fail rates beside every pass rate |

## What we do not know, said before you ask

- **Market size is not established.** Analyst figures for the adjacent assistant market cluster at {{S: ~8–10 B USD for 2026 — verify before use}}; ours would be a sliver of review and verification spend, unsized. The probe is staged so that TAM matters only at stage 3, and stage 2 tests willingness to pay directly.
- **Whether the cost the product adds nets out is unproven.** The prototype measured what the gate adds; only the pilot can measure what it saves.
- **Defensibility is thin**: neutrality, plus the customer's accumulating checks and labels. That is exactly why this is a probe with exits and not an investment.

## The decision requested

{{Keep the branch matching RESULTS.md §5: A — fund stage 2 at the assumption table above; B — wait, review on {{pedro:review_date}}; C — fund a bounded re-run of {{assumption:rerun_budget}} or default to B.}}

---

## Appendix — the challenges we expect, and our answers

<!-- Format, per line: the punchline answer; the alternative we rejected; an honesty
     tag (what we concede); whether we concede or hold under pressure. Rehearse these;
     do not read them. -->

**"They outspend us a thousand to one."**
Their spend is on generation, which we buy, not fight. *Rejected:* building any assistant, loop or harness. *Honesty:* a vendor can ship our mechanism natively in a quarter — it cannot ship independence from itself. **Hold.**

**"Then buy CodeRabbit — it's the funded leader in exactly this space."**
Buying it buys a model's opinion of a diff: it cannot run our test suite ({{E-50}}), publishes no error rate for its own verdicts, and keeps no outcome record ({{E-53}}). *Rejected:* reselling or white-labelling a reviewer. *Honesty:* CodeRabbit joining its parts into a contract-then-evidence flow within a year is the most likely way this window closes — which is why the ask is a probe, not a build. **Concede the risk, hold the recommendation.**

**"What's the TAM?"**
Not established, and we won't invent it. The probe is priced so the TAM question is deferred until a design partner has shown willingness to pay. *Rejected:* a top-down TAM slide built on analyst multiples. *Honesty:* if stage 2 finds no one who pays, the TAM is zero for us and we stop. **Concede.**

**"Your product makes my AI bill bigger and my delivery slower."**
Yes — stated in the proposal before you asked (§2.10). It adds checks, machine time and waiting, capped by a per-contract budget and applied by risk; it is meant to remove review time, rework and incidents. Four numbers decide it, reported together; if they don't improve for a partner, we stop. *Honesty:* the net saving is the pilot's question, not a claim we make today. **Hold.**

**"The next model release makes this unnecessary."**
The vendor itself found its evaluator "unnecessary overhead" one model later, on tasks inside the model's reliable range ({{E-36}}). That movement is the product: the measurement is re-run per model and harness pairing, and the checks follow the boundary. *Honesty:* if models stop failing in expensive ways, the product shrinks to an audit record — and the measurement would show that before we overspend on it. **Concede the direction, hold the timing.**

**"Margins in this market are abysmal. Why enter at all?"**
Those are generation margins — resellers paying API rates against subsidised subscriptions ({{E-17}}). We resell no inference: the verdict runs in the customer's pipeline on the customer's model access. *Honesty:* the evaluation path for LLM applications is token-heavy; it is budgeted per contract and priced to the customer. **Hold.**

**"Why would your two people beat their thousands?"**
We are not racing their roadmap; we measured one narrow claim nobody publishes: whether an executable verdict is wrong less often than the agent's claim and a model reviewer's. {{Branch A: It was: {{runs:fp_gate}} vs {{runs:fp_claim}} vs {{runs:fp_evaluator}} on {{runs:denominator}} changes.}} *Honesty:* the task set was small and ours; the pilot re-measures on a customer's repository. **Hold.**

**"And if the pilot shows nothing?"**
Then we spent {{one day + the stage-2 assumption}} to avoid a build we would have regretted, and we wait with a review date. The exits were fixed before the results existed. *Rejected:* an open-ended build, and a pure wait that teaches nothing. **Hold.**
