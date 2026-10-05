# Templates for P7 — proposal completion, design view, CFO message

| | |
|---|---|
| Status | Templates, prepared before the prototype runs. Nothing in them is a result. |
| Purpose | Make P7 a fill-in exercise, so the hour budgeted for it goes into judgment, not structure |
| Reads with | `PLAN.md` §6 (P7's exit check), §2.1 T7 (kill criteria) and T8 (CFO assumptions); `ROADMAP.md` §4 (working rules) |

## What P7 produces, and which template serves it

| P7 output | Template | Notes |
|---|---|---|
| `docs/RESULTS.md` (written in P6, consumed here) | `results-template.md` | Defines the exact tables and the kill-criteria scoreboard the proposal will cite. Using it in P6 makes the P7 exit check mechanical. |
| `PROPOSAL.md` §3 (design summary) and §4 (executive message) | `proposal-sections-3-4.md` | Three recommendation branches; exactly one survives. |
| Slidev deck | `slides-template.md` | Slide-for-slide skeleton with presenter notes. |
| One-page CFO recommendation | `cfo-message.md` | Answers the brief's question ("why believe we can compete, why not simply buy?") in three moves, with the challenge-and-answer appendix for the live conversation. The main objective of the exercise is to convince the CFO; this page is the deliverable that does it. |
| Claude Code artifact (design view) | Outline at the end of this file | Built from the near-final Markdown (D8). |

## Placeholder conventions

- `{{runs:<metric>}}` — a number that must come from a file under `prototype/runs/`.
- `{{E-nn}}` — a figure that must cite a row of `docs/research/EVIDENCE.md` tagged [P] or [L].
- `{{assumption:<name>}}` — a figure with no evidence behind it. It must be labelled "assumption" in the final text (ADR-010).
- `{{pedro:<decision>}}` — a value only Pedro can set (e.g. the review date, T7).
- HTML comments (`<!-- ... -->`) are drafting guidance. Delete them from the final documents.

## The branch rule

The recommendation is chosen by the kill-criteria scoreboard in `RESULTS.md`, not by judgment at writing time (PLAN §2.1 T7):

- **Branch A — Proceed to the pilot.** All three criteria cleared: the gate's false-pass rate is lower than both comparators; every planted flaw rejected; no unsafe action ran in the gated arm.
- **Branch B — Wait, with a review date.** At least one criterion failed on an adequate sample. The result is informative and negative.
- **Branch C — Wait, result inconclusive.** A criterion is not cleared because the sample was too small to separate the verdict sources (the 50 USD cap limits runs). Different from B: the design is not disproven, the measurement was underpowered. The review condition is a budgeted re-run, not a market change.

Both PROPOSAL §4 and the deck carry all three branches as drafts; exactly one is kept in each, and they must be the same one.

## P7 exit checklist

Work through this before asking Pedro to confirm the commit.

- [ ] Every number in PROPOSAL §3–4 and the deck cites an `EVIDENCE.md` row ([P]/[L]) or a file under `prototype/runs/`.
- [ ] No throughput or speed number appears without its quality number beside it (PLAN §5, redline 8).
- [ ] No pass rate appears without the verdict's own error rates beside it (DESIGN redline 7).
- [ ] The kept recommendation branch matches the scoreboard in `RESULTS.md`, and the same branch is kept in the proposal and the deck.
- [ ] CFO figures are labelled assumptions; salary and loaded-cost rates are left to finance, not invented (ADR-010, T8).
- [ ] If the recommendation is Wait (B or C), the review date is set by Pedro (open item T7) or explicitly marked as awaiting him.
- [ ] The limitations from PLAN §7.1 ("what one day cannot prove") appear wherever results appear.
- [ ] Revision pass done over PROPOSAL §1–2 and DESIGN.md against the results (PLAN §6: "P3 and P4 are deliberately lean on the first pass. They are revised in P7").
- [ ] ASSIST register checked: nothing in these documents contradicts an open issue.
- [ ] The CFO's question is answered before the ask, in the proposal (§4.0), the deck (slide 3) and the one-page message — all three word-for-word consistent.
- [ ] Every anticipated challenge in `cfo-message.md`'s appendix has an honesty tag and a concede-or-hold line; none answers with reassurance alone.
- [ ] No vanity metric (lines of AI code, acceptance rate, seats, volume without quality) appears anywhere; only the paired, auditable set.
- [ ] The [S] candidates in `docs/research/cfo-numbers-candidates.md` used in any document were verified at their raw sources and promoted to `EVIDENCE.md` first; unverified ones stay out or carry an explicit "unverified" tag in speech only.
- [ ] If time runs short: the artifact and deck reduce to a single diagram before anything else is cut (PLAN §9).
- [ ] No commit until Pedro confirms (ADR-009).

## Design-view artifact — outline

One page, built from the Markdown once near-final. Order:

1. **The question and the answer** (one line each; the kept branch).
2. **The flow diagram** — DESIGN §3's Mermaid flow, rendered. This is the piece to keep if everything else is cut.
3. **The verdict** — the decision ladder of DESIGN §4.1 as a vertical list, with the evaluation path beside it as a second column.
4. **The scoreboard** — the three kill criteria with their measured values, coloured pass/fail, each linking to its run file.
5. **The probe** — three stages, each with its cost and its exit, the current stage highlighted.

No numbers on the page that are not in `RESULTS.md` or `EVIDENCE.md`.
