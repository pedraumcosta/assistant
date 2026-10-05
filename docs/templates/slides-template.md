---
# Slidev deck template (D8). Build only once PROPOSAL.md is near-final.
# Rule of the deck: no number that is not in EVIDENCE.md ([P]/[L]) or prototype/runs/.
# Keep exactly one recommendation branch — the same one as PROPOSAL §4.1.
theme: default
title: Should we enter the AI software-development-assistant market?
info: ASSIST — probe recommendation to the executive team
class: text-left
transition: none
mdc: true
---

# Should we enter the AI software-development-assistant market?

{{date}} · prepared for the executive team

<!-- Presenter note: the whole deck answers one question. Slide 2 gives the answer;
     everything after is the evidence. 15 minutes, then discussion. -->

---

# The answer

**Do not build another AI coding assistant.**

{{Branch A: We probed the one part nobody sells, the prototype cleared its exits, and we ask for a six-week measurement pilot with fixed exits.}}
{{Branch B: We probed the one part nobody sells. The prototype failed its exits. Recommendation: wait, review on {{pedro:review_date}}.}}
{{Branch C: We probed the one part nobody sells. The sample was too small to decide. Recommendation: a budgeted re-run, or wait.}}

<!-- One of the three lines survives. -->

---

# "Why not simply buy their products?"

**We do.** Buy generation ({{verified seat prices}}/seat) · adopt the open-source policy layer ({{E-32}}) · build only what no one sells.

What cannot be bought, from anyone:

- a verdict that **runs our own checks** — the funded reviewer cannot ({{E-50}})
- **independence** — "agents reliably skew positive when grading their own work", the vendor on its own models ({{E-34}})
- a **measured error rate** for the verdict — published by no vendor
- an **outcome record** — no audit log keeps one ({{E-53}})

<!-- Presenter note: this slide answers the CFO's question directly, third minute of
     the talk, not the tenth. Concede the premise first: we are not competing with
     their spend. -->

---

# The market, as the question was asked

- The companies that own the models own the product ({{E-12}}, {{E-13}}, {{E-48}})
- Independents are priced at acquisition scale ({{E-46}}, {{E-47}})
- "Margins on all of the 'code gen' products are either neutral or negative" ({{E-17}})
- The underlying loop is 90 lines of published code ({{E-31}})

**We have no model, no customers, no captive vertical. As asked: no.**

---

# What the incumbents have not solved

Writing code got cheap. Knowing whether to trust it did not.

- Roughly half of test-passing agent changes would not be merged by maintainers ({{E-01}})
- Median time in review up 441.5%; PRs merged with no review up 31.3% ({{E-04}}, {{E-05}})
- "Agents reliably skew positive when grading their own work" — the model vendor, on its own models ({{E-34}})
- A model learned to force tests green by patching the test reporter ({{E-75}})

---

# The gap is real, and it is narrow

Nobody sells, together:

1. a verdict that **runs the customer's own checks**
2. **independence** from the vendor whose model wrote the code
3. a **measured false-pass rate**, on the customer's repository
4. an **outcome record** an auditor can read

And next to it: CodeRabbit at 1.5 B USD positioning as "the control layer" ({{E-49}}); the framing already published as research ({{E-40}}).

<!-- Presenter note: say "narrow" out loud. The case against is the next slide, undiluted. -->

---

# The case against entering at all

- The idea is published; the vendor describes contract-plus-evaluator as its own practice
- A funded competitor has most of the parts
- A check's value moves with every model release ({{E-36}})
- A frontier lab argues against gates where corrections are cheap ({{E-57}})
- We would have no moat beyond neutrality and the customer's accumulating data

**This is why the recommendation is a probe with fixed exits, not an investment.**

---

# The product: tooling for evidence-driven development

The team defines "done" as executable checks **before** the work starts. Every change — written by a person or an agent — is accepted on that evidence.

Five parts: a guided path from use case to checks · a protected contract · a verdict of executable evidence · an outcome record · a measured error rate.

---

# How it differs

| The team has | The evidence layer adds |
|---|---|
| The agent's word | A verdict from outside the agent |
| Rules in prompts | Rules enforced by mechanism |
| A reviewer model's opinion | The customer's checks actually run, and a verdict that can block |
| The vendor's evaluator | Independence, and a stated error rate |
| Audit logs of actions | Whether the result was verified |

---

# The design in one picture

{{DESIGN §3 diagram, rendered}}

**It trades speed to merge for a verdict the author cannot influence.** Fail closed. Nothing accepted by default. Everything leaves a record.

---

# What we tested in one day

Same tasks, three arms: **bare** · **prompt discipline** · **gated** — plus planted flaws and known-good changes fed straight to the gate.

Three verdict sources scored against hidden acceptance checks:
the agent's own claim · an evaluator agent from another vendor · the gate.

Spend: {{runs:total_spend_usd}} of a 50 USD cap. Task set small and self-authored — an indication, not a benchmark.

---

# The scoreboard

| Exit criterion, fixed in advance | Measured | Cleared |
|---|---|---|
| Gate's false-pass rate below both comparators | {{runs:...}} | {{✓/✗/~}} |
| Every planted flaw rejected | {{runs:...}}/{{runs:...}} | {{✓/✗}} |
| No unsafe action in the gated arm | {{runs:...}} | {{✓/✗}} |

<!-- This slide decides the deck. The numbers come from RESULTS.md §5 and nowhere else. -->

---

# The numbers, paired

| | Bare | Prompt | Gated |
|---|---|---|---|
| pass^k (hidden checks) | | | |
| False-pass rate of its verdict | | | |
| Cost per production-qualified change | | | |
| Unsafe actions | | | |

Gate overhead: {{runs:...}} per task · false-fail rate {{runs:...}} of {{runs:...}} known-good changes.

<!-- Pairing rule: never a speed or cost figure without its quality figure. -->

---

# What it costs the delivery process

It **adds** cost: checks written up front, extra attempts, machine time, waiting before merge.
It is meant to **remove**: review time, rework, incidents, unreviewed merges.

Whether that nets out is not established. It is what the pilot measures — four numbers, reported together, never one without the others.

---

# The ask

| Stage | Cost | Exit |
|---|---|---|
| 1. Prototype | One day, {{runs:total_spend_usd}} — **done** | Cleared / not cleared (previous slide) |
| 2. Pilot | 6 weeks · 2 engineers · product lead at half time — **assumption**, rates from finance | A partner says the report changed a decision |
| 3. Build | Scoped only if stage 2 clears | Set before stage 3 starts |

{{Branch A: Decision requested: fund stage 2.}}
{{Branch B/C: Decision requested: agree the review date / the re-run budget.}}

---
layout: center
---

# Backup

---

# What one day cannot show

{{RESULTS.md §1 limitations, verbatim}}

---

# Challenges we expect

<!-- Backup slide. One line per challenge; the full answers with concede/hold lines
     are the appendix of docs/templates/cfo-message.md. Rehearsed, not read. -->

| Challenge | The short answer |
|---|---|
| "They outspend us 1000:1" | Their spend is on generation, which we buy; independence from themselves is what they cannot sell |
| "Buy CodeRabbit instead" | It cannot run our tests ({{E-50}}) and publishes no error rate; it closing this gap within a year is the named risk — hence a probe, not a build |
| "This raises my AI bill and slows delivery" | Yes — stated in §2.10, capped per contract, applied by risk; four paired numbers decide it |
| "The next model makes it unnecessary" | The check's value moves with each release ({{E-36}}); re-measurement per model pairing **is** the product |
| "What's the TAM?" | Not established and not invented; stage 2 tests willingness to pay before TAM matters |
| "Margins are abysmal" | Those are generation margins ({{E-17}}); we resell no inference — the verdict runs on the customer's pipeline and model access |

---

# Evidence index

Every figure in this deck: `docs/research/EVIDENCE.md` (rows cited per slide) and `prototype/runs/` (results). Full documents: `PROPOSAL.md`, `DESIGN.md`, `RESULTS.md`.
