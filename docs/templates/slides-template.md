---
# Slidev deck template (D8) — the spoken equivalent of presentation-template.html.
# Same section order, same numbers, same single recommendation branch (RESULTS.md §5).
# TIMING: 10 minutes total. Each slide's presenter note starts with its time budget;
# the budgets sum to 10:00. Backup slides are not part of the 10 minutes.
# Rule of the deck: no number that is not in EVIDENCE.md ([P]/[L]) or prototype/runs/.
theme: default
title: ASSIST Recommendation
info: Should we enter the AI software-development-assistant market? — executive recommendation
class: text-left
transition: none
mdc: true
fonts:
  serif: Fraunces
  sans: Source Sans 3
  mono: JetBrains Mono
---

# Should we enter the AI software-development-assistant market?

{{date}} · executive session · 10 minutes

Every number on these slides cites `EVIDENCE.md` ([P]/[L]) or `prototype/runs/`.

<!-- 0:00–0:30. One breath: the question as leadership asked it, and that the answer
     comes with measurements, not opinions. Advance. -->

---

# The answer

**Do not build another AI coding assistant.**

We probed the one part nobody sells — a verdict on agent-written changes built from
**executable evidence**, independent of the model vendor, measured for error — under the banner
of **evidence-driven development**: "done" is defined as executable checks before the work
starts, and every change is accepted on that evidence, whoever wrote it.

{{Branch A: The prototype cleared its three exits. We ask for a six-week measurement pilot with its exit fixed now.}}
{{Branch B: The prototype failed its exits. We recommend waiting, with a review on {{pedro:review_date}}.}}
{{Branch C: The sample could not separate the verdict sources. We ask for a budgeted re-run, or we wait.}}

<!-- 0:30–1:00. Keep exactly one branch line — the one RESULTS.md §5 selected.
     Say "probe", "exits", "measured". Do not defend yet; the next slide takes the
     hardest question head on. -->

---

# "Why shouldn't we simply buy their products?"

**We do.** By layer:

| Layer | Decision | Why |
|---|---|---|
| Assistants, generation | **Buy** ({{verified seat prices}}/seat) | Vendor-subsidised; features copy in months ({{E-12}}, {{E-13}}) |
| Policy, sandbox, budgets | **Adopt open source** ({{E-32}}) | Free, backed by a large vendor |
| Model-opinion review | Buy if wanted | Cannot run our tests ({{E-50}}) or block ({{E-51}}) |
| **The verdict + its error rate + the record** | **The only build** | Sold by no one ({{E-50}}, {{E-51}}, {{E-53}}) |

"Agents reliably skew positive when grading their own work" — the vendor, on its own models ({{E-34}}).
A vendor cannot sell a credible verdict on itself, whatever it spends.

<!-- 1:00–2:30. The CFO's question, answered in minute two, not minute nine. Concede
     the premise first ("we do buy them"), then the one line that holds the slide:
     independence cannot be bought from the party being judged. -->

---

# What the incumbents have not solved

Writing code got cheap. Knowing whether to trust it did not.

- "Roughly half of test-passing" agent changes "would not be merged into main by repo maintainers" ({{E-01}})
- Median time in review **up 441.5%**; PRs merged with **no review up 31.3%** ({{E-04}}, {{E-05}})
- Trust in AI output fell 43% → 33% in a year; distrust rose 31% → 46% ({{E-82}})
- A model learned to force tests green — **by patching the test reporter** ({{E-75}})

<!-- 2:30–4:00. Four facts, no adjectives. Name the interested parties where they
     apply (the review-time figure comes from a vendor that sells measurement).
     The last bullet sets up the design: the author cannot keep its own evidence. -->

---

# The gap: four things nobody sells together

1. A verdict that **runs the customer's own checks** — not a model's reading of the diff
2. **Independence** from the vendor whose model wrote the code
3. A **measured false-pass rate**, on the customer's repository
4. An **outcome record** an auditor can read ({{E-53}})

**Said against ourselves:** the idea and its metrics are published ({{E-40}}); a competitor at
1.5 B USD stands next to the gap ({{E-49}}). The gap is real, and it is **narrow** — which is why
this is a probe with fixed exits, not an investment.

<!-- 4:00–5:00. Say "narrow" out loud. The honesty paragraph is the credibility of the
     whole talk; do not rush it. -->

---

# The product, in the order a change flows

1. **Use case → checks** — the team's assistant asks clarifying questions ({{E-80}}); a person approves
2. **Contract fixed before the agent runs** — scope, checks, budget, on a protected branch
3. **Verdict of executable evidence after it stops** — the customer's tests; scope; the agent's new tests must fail on the original code ({{E-76}})
4. **Outcome record** — written once, never edited
5. **A measured error rate for the verdict itself** — per repository, re-measured per model pairing ({{E-36}}, {{E-58}})

It trades **speed to merge** for a verdict **the author cannot influence**. Fail closed.

<!-- 5:00–6:30. Walk the five steps with one finger. Step 5 is the differentiator —
     "this is what no one else measures". Close with the trade, stated as a trade. -->

---

# What one day measured

Same tasks · three arms (**bare** / **prompt-disciplined** / **gated**) · {{runs:k}} repeats ·
three verdict sources judging the **same** finished changes, against hidden acceptance checks.

| | Bare | Prompt | Gated |
|---|---|---|---|
| Unsafe actions (trap tasks) | {{runs:unsafe_bare}} | {{runs:unsafe_prompt}} | **{{runs:unsafe_gated}}** |
| pass^k (hidden checks) | {{runs:passk_bare}} | {{runs:passk_prompt}} | **{{runs:passk_gated}}** |
| Cost per production-qualified change | {{runs:cpq_bare}} | {{runs:cpq_prompt}} | **{{runs:cpq_gated}}** |

Spend: {{runs:total_spend_usd}} of a 50 USD cap. Task set small and ours — an indication, not a benchmark.

<!-- 6:30–7:15. Point at pass^k, not pass@1 ({{E-79}}: >60% average can mean <25%
     eight-in-a-row). The limitation sentence is spoken, not skipped. -->

---

# Whose "pass" can you trust?

The product's claim, and the number that can kill it:

| Verdict source | False-pass rate | On |
|---|---|---|
| The agent's own claim | {{runs:fp_claim}} | {{runs:denominator}} changes |
| Evaluator agent, other vendor | {{runs:fp_evaluator}} | sampled |
| **The gate** | **{{runs:fp_gate}}** ({{runs:fp_gate_ci}}) | {{runs:denominator}} changes |

Plus: **{{runs:flaws_rejected}}/{{runs:n_flaws}}** planted flaws rejected ·
false-fail {{runs:false_fails}}/{{runs:n_good}} known-good changes ·
gate overhead +{{runs:gate_time}} and +{{runs:gate_cost}} per task.

<!-- 7:15–8:00. H4 is the slide to slow down on. Always say the denominator and the
     range — on a sample this small, a rate without its range overclaims. The paired
     false-fail and overhead lines keep the reporting honest. -->

---

# The scoreboard — exits fixed before the results existed

| # | Kill criterion | Measured | Verdict |
|---|---|---|---|
| K1 | Gate's false-pass rate below **both** comparators | {{runs:fp_gate}} vs {{runs:fp_claim}} vs {{runs:fp_evaluator}} | {{✓ cleared / ✗ failed / ~ inconclusive}} |
| K2 | **Every** planted flaw rejected | {{runs:flaws_rejected}}/{{runs:n_flaws}} | {{✓ / ✗}} |
| K3 | **No** unsafe action in the gated arm | {{runs:unsafe_gated}} | {{✓ / ✗}} |

<!-- 8:00–8:30. This table decides the talk and matches RESULTS.md §5 exactly.
     Read it; do not editorialise. The recommendation on the next slides follows
     from it mechanically. -->

---

# What it costs, said before anyone asks

**It adds:** check-writing (the largest, least-known cost) · extra attempts · machine time ·
re-measurement at every model release · **waiting before merge**.

**It is meant to remove:** review time evidence could settle · rework and incidents from
changes that passed and were wrong · the risk in unreviewed merges ({{E-05}}).

**Whether that nets out is unproven** — the prototype measured what the gate adds; only the
pilot measures what it saves. Four paired numbers decide it, and where it won't pay is named:
small low-risk changes, fast new builds ({{E-57}}), teams with few tests.

<!-- 8:30–9:00. Say the cost before the CFO does. "Unproven" is a word to use, not avoid. -->

---

# The ask

| Stage | Cost | Exit, fixed in advance | Status |
|---|---|---|---|
| 1 · Prototype | one day · {{runs:total_spend_usd}} | the scoreboard above | **done** |
| 2 · Pilot | 6 weeks · 2 engineers · ½ product lead · cap {{assumption:pilot_spend_cap}} — **assumption**, rates from finance | a partner says the report changed a decision | requested |
| 3 · Build | scoped only if stage 2 clears | set before it starts | not reached |

**The sentence for the board:** {{one sentence, written last, consistent with the scoreboard —
see presentation-template.html #ask for the Branch A and Branch B/C shapes}}

<!-- 9:00–10:00. End on the table and the sentence. The decision requested is one line:
     Branch A — fund stage 2; Branch B/C — agree the review date / the re-run budget.
     Stop talking at 10:00; the backup slides exist for the discussion. -->

---
layout: center
---

# Backup — for the discussion, not the 10 minutes

---

# Challenges we expect

| Challenge | The short answer |
|---|---|
| "They outspend us 1000:1" | Their spend is on generation, which we buy; independence from themselves is what they cannot sell |
| "Buy CodeRabbit instead" | It cannot run our tests ({{E-50}}) and publishes no error rate; it closing this gap within a year is the named risk — hence a probe, not a build |
| "This raises my AI bill and slows delivery" | Yes — stated before you asked; capped per contract, applied by risk; four paired numbers decide it |
| "The next model makes it unnecessary" | The check's value moves with each release ({{E-36}}); re-measurement per model pairing **is** the product |
| "What's the TAM?" | Not established and not invented; stage 2 tests willingness to pay before TAM matters |
| "Margins are abysmal" | Those are generation margins ({{E-17}}); we resell no inference — the verdict runs on the customer's pipeline and model access |

<!-- Full answers with concede-or-hold lines: docs/templates/cfo-message.md appendix. -->

---

# What one day cannot show

{{RESULTS.md §1 limitations, verbatim: small self-authored task set · nothing on reviewer time
saved, adoption or willingness to pay · contracts written by hand · a snapshot of today's models}}

---

# Evidence index

Every figure: `docs/research/EVIDENCE.md` (E-nn, verified at raw sources) · results generated
from `prototype/runs/` · decisions `docs/JOURNAL.md` ADR-001…020 · full case `docs/PROPOSAL.md` ·
design `docs/DESIGN.md` · the one-page version of this talk: the published design-view artifact.
