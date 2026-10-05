# ASSIST

**Should we enter the AI software-development-assistant market?** This repository is the
complete, self-contained answer to that question: the research, the decisions, the written
case, a system design, a one-day prototype, and the presentation of the recommendation to
the executive team.

The answer it defends: **do not build another AI coding assistant.** Probe the one part of
the market nobody yet sells — a verdict on agent-written changes built from **executable
evidence**, independent of the model vendor and measured for its own error — framed as
tooling for **evidence-driven development**, and decide Build or Wait on what the probe
shows. The probe has three stages (a one-day prototype, a six-week measurement pilot, a
build), each with exit criteria fixed before its results exist.

## What this repository is for

It is the working record and the deliverable at once. A reader should be able to:

- follow the recommendation from evidence to conclusion without opening anything outside
  the repository;
- check any number: every figure traces to a row of `docs/research/EVIDENCE.md` verified at
  its raw source ([P]/[L] tags), or to a run file under `prototype/runs/`;
- see how each decision was made and what was rejected (`docs/JOURNAL.md`, ADR-001…020);
- rebuild the presentation from the same sources.

## Map of the repository

| Path | What it is |
|---|---|
| `docs/init-prompt.md` | The brief: the question as leadership asked it |
| `docs/PLAN.md` | The working plan: the position defended, all decisions (D1–D10, the thesis decisions P1–P2 and T1–T19), the research digest, the prototype's hypotheses and kill criteria. **Source-of-truth order: PLAN → ROADMAP → JOURNAL** |
| `docs/ROADMAP.md` | Execution state: what is done, in review, not started; the only copy of the issue register (ASSIST-001…) |
| `docs/JOURNAL.md` | The dated log and the architecture decision record: every decision with its rationale and the alternative rejected; every deviation and correction, including our own mistakes |
| `docs/research/` | The evidence base: one record per source read, the ledger (`EVIDENCE.md`), and claim-by-claim checks of working notes against primary sources |
| `docs/PROPOSAL.md` | The written case: the problem, the case against entering (undiluted), the product, its costs stated plainly, the staged ask |
| `docs/DESIGN.md` | The system design: requirements, core objects (check, contract, verdict, outcome record), the decision ladder, the evaluation path for LLM applications, risk tiers, risks, assumptions, redlines |
| `docs/DESIGN-REVIEW.md` | A critical self-review of the design before building: integrity-boundary gaps, contradictions, and the fixes each one gets |
| `docs/templates/` | The fill-in templates that make the final phase mechanical: results, proposal sections 3–4, the CFO message with its challenge-and-answer appendix, and both presentation forms |
| `docs/presentation.html` | The presentation page (single-page, 10-minute spoken walkthrough, leave-behind sections); published as the session artifact once results land |
| `docs/slides.md` | The Slidev deck: the 10-minute recommendation ending on the executive recommendation to the CFO, a ~13-minute technical walkthrough, and discussion backup |
| `prototype/` | The one-day prototype (in progress in a parallel session): the agent under test, the gate, the eval runner, and `runs/` with the raw results |
| `docs/RESULTS.md` | What the prototype measured — generated from the run files, never typed in |
| `docs/BUILD_LOG.md` | (Final phase) how Claude Code was used to produce this repository |

## How it was built — the thought process, mapped to the files

The repository was built in one working day with Claude Code, in a strict order: **evidence
before claims, decisions before documents, templates before results.** Each step left its
record.

1. **The brief became a plan** (`docs/PLAN.md`). Before any research, the plan fixed the
   working rules that shaped everything after: no number invented or estimated; only
   evidence verified at its raw source in CXO-facing text; one commit per meaningful step,
   confirmed before it is made; every throughput number paired with its quality number.
2. **Research ran in parallel passes, and the evidence was re-verified** (`docs/research/`).
   Six passes over working notes, linked articles and the public market; four papers and
   eleven articles read in full; every ledger row checked against its raw source. Claims
   that failed re-verification were dropped, not softened — the journal records fourteen
   corrections to our own notes and nine to our own early ledger.
3. **The thesis narrowed in public, decision by decision** (`docs/JOURNAL.md`,
   `docs/PLAN.md` §1–§3). The starting idea — a thin outer harness around any agent — did
   not survive the evidence: that layer is open source. A second thesis (brownfield
   specialisation) was evaluated and not pursued. What survived is narrow and stated as
   such: a protected pre-run contract, a verdict that runs the customer's own checks, a
   measured false-pass rate, an outcome record. Each decision carries its rejected
   alternative; "Wait, with a review date" is kept as a real outcome throughout.
4. **The case was written before the design, and against itself first**
   (`docs/PROPOSAL.md`). Section 1.4 is the case for not entering at all, undiluted; the
   product section states what the tool adds in cost and delay before what it removes.
5. **The design was written, then attacked** (`docs/DESIGN.md`, `docs/DESIGN-REVIEW.md`).
   The review found the gaps worth naming out loud — the integrity boundary between the
   verdict runner and the author's code, the enforcement anchor in CI, the missing
   flaky-test policy — each with its fix and the stage where it lands. Two findings changed
   the prototype's runner before the first paid run.
6. **The final documents were templated before the results existed**
   (`docs/templates/`). The recommendation is chosen by a kill-criteria scoreboard in
   `RESULTS.md` — fixed on 2026-10-05, before any run — not by judgment at writing time.
   The templates carry all three outcome branches (proceed / wait with a date /
   inconclusive, re-run) so that a negative or underpowered result produces an equally
   finished deliverable.
7. **The presentation was built in both forms from the same sources**
   (`docs/presentation.html`, `docs/slides.md`), paced to a 10-minute walkthrough with the
   executive recommendation to the CFO as the closing slide, a technical walkthrough behind
   it, and backup for a changing business scenario.

The git history is part of the record: one commit per confirmed step, with the
`Co-Authored-By: Claude` trailer kept deliberately, so how the tool was used is verifiable
from the log itself.

## The prototype, and how it supports the proposal

The proposal's central claim is empirical, so the prototype exists to give it a number —
or to kill it. One day, a 50 USD cap enforced by the runner, and one question: **is an
executable verdict wrong less often than the agent's own claim and than a model
reviewer's?**

- **The agent under test is not ours.** It is the published 90-line scaffold from the
  harness source-code study (arXiv 2609.00006, CC BY 4.0) — a citable agent nobody can
  claim we tuned to suit our gate.
- **Three arms** run the same tasks: the bare scaffold, the scaffold under prompt
  discipline ("verify before claiming completion"), and the scaffold inside the contract
  and gate. **Three verdict sources** are scored on the same finished changes: the agent's
  own claim, an evaluator agent from a different vendor, and the gate.
- **Ground truth is hidden**: acceptance checks neither the agent nor the gate ever sees.
  **Planted flaws** (changes built to be wrong in known ways) and **known-good changes**
  measure the gate's two error rates — wrongly passed and wrongly failed — because a gate
  that blocks good work gets bypassed.
- **The measurement skeleton was built first, with a fake agent that costs nothing**, to
  prove that a crashed check reads as an error and not as a pass before any money was
  spent.

The link to the proposal is mechanical. The prototype's results fill `docs/RESULTS.md`,
whose kill-criteria scoreboard (false-pass rate below both comparators; every planted flaw
rejected; no unsafe action in the gated arm) selects the recommendation branch in the
proposal and both presentation forms. If the criteria clear, the ask is a measurement
pilot; if they fail, the recommendation is to wait, with a review date — and the proposal
says so in the same breath it would have claimed success. What one day cannot show is
stated wherever results appear: reviewer time saved, willingness to pay, the cost of
writing checks for ordinary work, and whether results on today's models hold on the next.

## Reading order

For the conclusion: `docs/PROPOSAL.md`, then `docs/presentation.html`. For the reasoning:
`docs/PLAN.md` §1–§3, then `docs/JOURNAL.md`. For the system: `docs/DESIGN.md`, then
`docs/DESIGN-REVIEW.md`. To check any number: `docs/research/EVIDENCE.md`.

## Status

As of 2026-10-05: research complete and verified; thesis decided; proposal sections 1–2,
design, design review, templates and both presentation forms written; the prototype is
being implemented in a parallel session. Pending: prototype results into `RESULTS.md`,
the scoreboard verdicts, proposal sections 3–4 filled, and `BUILD_LOG.md`.
