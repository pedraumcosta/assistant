# BUILD LOG — how Claude Code produced this repository

| | |
|---|---|
| Status | Written 2026-10-07, at the close of the work. |
| What this is | The record of how the tool was used: the sessions, the division of labour between person and model, and where the verifiable trail lives. |
| The primary record | The git history itself. Every commit was made after the work it describes, carries a `Co-Authored-By: Claude` trailer by decision D10, and — until the branch work of 2026-10-07 — only after Pedro confirmed it (ADR-009). |

## The shape of the work

Three working sessions produced the repository, all driven in Claude Code with Pedro directing and deciding throughout.

**Session 1 (2026-10-03 and 2026-10-05): research, decisions, documents.** Six research passes ran in parallel as sub-agents over Pedro's notes, the linked articles and the public market; their records are the files under `docs/research/`, and every figure that survived was re-verified at its raw source before use (ASSIST-004). The thesis was narrowed in recorded steps — each decision in `PLAN.md` §2 and each rationale in `JOURNAL.md` as an ADR, with the alternative rejected. The plan, roadmap, journal, proposal sections 1–2, and the system design were written and reviewed in this session; the design's five open points were decided by Pedro (ADR-020).

**Session 2 (2026-10-05, in parallel): the prototype.** A separate session built the prototype in the order the design set — measurement first, on a cost-free fake agent, so nothing would be measured on an unproven instrument — and stopped on the one-day time budget with the central comparison unrun, reported plainly (ADR-022, `RESULTS.md` as first written).

**Session 3 (2026-10-05 and 2026-10-07): review, presentation, completion.** The first session's continuation reviewed the design critically before trusting it (`docs/DESIGN-REVIEW.md`), built the presentation forms and their templates, and reconciled every document with the prototype's honest, incomplete results. On 2026-10-07, on the branch `post-1st-assessment` and then on `main`, it completed stage 1: the free completions (finding and fixing a container fault on the second machine, ASSIST-024), the widened ground truth (ASSIST-021), the 165-run arm comparison, the second-vendor evaluator with its verdict-variance measurement, the contracts' approval by Pedro (ASSIST-022), and the evaluation path for an LLM application end to end — folding each result into `RESULTS.md`, the journal, the issue register and the presentation forms as it landed.

## The division of labour

**Pedro decided; the model executed and proposed.** Every decision in the record — the thesis, the exclusions, the kill criteria, the rewording of a criterion that could not have been met (T20), the contracts' approval — is attributed to Pedro in the plan or the journal, usually with the alternatives he rejected. The model researched, drafted, built, measured and wrote; where it corrected Pedro's notes against primary sources (dozens of corrections, logged), and where Pedro corrected its drafts (the reframing to evidence-driven development, the audience rewrite of the presentation, "keep the prototype very simple"), the journal records both directions.

**Sub-agents were used for breadth, not authority.** Parallel research passes gathered and checked sources; everything they produced was re-verified before entering `EVIDENCE.md`, and nothing they claimed is cited above its verification tag.

## What makes the log verifiable

- **One commit per confirmed step**, with a body saying what changed and why, and the ASSIST issues touched. The sequence from `git log` reads as the project's own narrative.
- **No number without a source.** Every figure in any document traces to a row of `docs/research/EVIDENCE.md` (verified [P]/[L]) or to a file under `prototype/runs/`; results tables are generated from run records by `prototype/runner/report.py`, not typed.
- **Mistakes are in the record, not edited out.** The journal's "deviations and corrections" sections log the model's own errors (a truncated first reading of sources, a self-killing `pkill`, a scorer that wrongly failed valid drafts, an app call that truncated outputs) beside the fixes; superseded measurement rounds are kept on disk next to the rounds that replaced them.
- **Spend is reconciled.** Every model call was reserved on `prototype/runs/ledger.jsonl` before it happened and settled after; the exercise closed at 6.87 of the 50 USD cap.

## Honest limits of this log

The conversational transcripts behind the sessions are not in the repository; the git history, the journal and the run records are the durable trace. Where the journal says "Pedro decided", the decision happened in conversation and is recorded only as its outcome. And this file, like everything else here, was written by the model and reviewed by the person whose name the decisions carry.
