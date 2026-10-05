# ROADMAP — ASSIST

| | |
|---|---|
| Status | **Draft for Pedro's review.** Records only what is already known or done. Steps that depend on the thesis details are listed but not scoped. |
| Last updated | 2026-10-05 |
| Reads with | `docs/PLAN.md` (takes precedence) and `docs/JOURNAL.md` (what happened and why) |

## 1. Where we are

- The plan exists and ten working decisions are recorded in it (`PLAN.md` §2).
- The research is done and recorded in `docs/research/`.
- The thesis has an agreed direction and open details (§2 below).
- Nothing has been designed or built yet. No proposal text exists.

## 2. The thesis: what is agreed and what is open

**Agreed direction (2026-10-05).** We do not build a coding assistant, a harness, or a meta-harness. The candidate product is an evidence layer: a change contract, deterministic verification after the agent stops, an evidence bundle and risk routing, delivered as a plug-in to existing harnesses, and entered through per-repo agent evaluation. "Wait, with a review date" remains a possible conclusion.

**Open details.** None of these has been decided. The roadmap steps in §3.3 cannot be scoped until they are.

| # | Open question | Why it matters |
|---|---|---|
| T1 | Who is the buyer and which team feels the pain first | Shapes the value proposition, the adopt / supplement / replace argument and the CFO message |
| T2 | How we differ from review bots, from Omnigent's policy plane, and from a vendor adding verify-on-stop natively | The research shows every one of these exists or is cheap to add |
| T3 | What we claim is defensible, given no inherited moat (D2). Candidates so far: neutrality, and each customer's accumulated contracts and evaluation history | The research calls this thin; it decides between Build and Wait |
| T4 | Where contracts come from for ordinary changes | Named in the plan as the largest open product assumption |
| T5 | Which harnesses the plug-in targets first, and through which attachment points | Hook surfaces differ by vendor; sets the cost of being harness-agnostic |
| T6 | What is explicitly excluded from the product | Required by the brief |
| T7 | The redlines and the kill criteria, with their thresholds | Required by the brief; thresholds are decisions for Pedro, not data |
| T8 | The assumptions behind the CFO message (people, weeks, what a pilot costs) | No inputs exist; every figure will be a labelled assumption (ASSIST-009) |
| T9 | Whether the prototype in `PLAN.md` §7 is the right smallest test of the thesis | The arms, hypotheses and task set follow from T1 to T4 |

## 3. Steps

Status values: Done, In review, Not started, Blocked.

### 3.1 Done

| Step | Output | Commit | Date |
|---|---|---|---|
| Local repository, brief and draft plan | `docs/init-prompt.md`, `docs/PLAN.md`, `.gitignore` | `4f77bbc`, `c503de6` | 2026-10-03 |
| First plan discussion: decisions D2 to D5 and D7 to D10; thesis narrowed after first reading of the harness paper | `PLAN.md` §1.1, §2 | `69c025b` | 2026-10-03 |
| Private GitHub repository created and pushed | `pedraumcosta/assistant` | — | 2026-10-05 |
| Research records and evidence ledger; decisions D1 (direction) and D6; prototype arms revised | `docs/research/` (13 files), `PLAN.md` §1.1, §3.4, §7.1 | `95e0f83` | 2026-10-05 |

### 3.2 In review

| Step | Output | Exit check | Waiting on |
|---|---|---|---|
| Roadmap and journal | `docs/ROADMAP.md`, `docs/JOURNAL.md` | Pedro has read both and agrees they state only what is known | Pedro |
| Thesis details | Answers to T1 to T9, recorded in the journal as decisions | Each open question in §2 is either decided or explicitly deferred with a reason | Discussion with Pedro |

### 3.3 Not started

These are the remaining phases from `PLAN.md` §6. Their content depends on §2; only their purpose and exit check are fixed.

| Phase | Output | Exit check (from the plan) | Depends on |
|---|---|---|---|
| Evidence verification | `docs/research/EVIDENCE.md` with no [S] row in use | Every figure we intend to use is tagged [P] or [L], or is dropped | Knowing which figures the proposal needs (T1, T2) |
| Problem and product | `docs/PROPOSAL.md` §1–2 | Includes the case against entering; exclusions are explicit | T1, T2, T3, T6 |
| System design | `docs/DESIGN.md` | Each design topic has a position, a rejected alternative and a way to measure it; risks, assumptions and redlines stated | T4, T5, T7 |
| Prototype | `prototype/` | Each slice runs end to end on the fixture repo | T9 |
| Measurement | `docs/RESULTS.md`, `prototype/runs/` | Results table generated from run files, limitations stated, spend within the 50 USD cap | Prototype |
| Proposal, design view, CFO message | `PROPOSAL.md` complete; Claude Code artifact; Slidev deck | Recommendation is consistent with the results, including if the hypotheses fail | Measurement, T8 |
| Build log and final review | `docs/BUILD_LOG.md` | No number without an evidence row; no ASSIST issue unaccounted for | All of the above |

## 4. Working rules in force

- **Commits** only after Pedro confirms; one per meaningful step; `Co-Authored-By: Claude` trailer kept.
- **Never committed:** `docs/scratchpad.md`, `.env`.
- **Numbers:** none invented or estimated; only [P] and [L] rows of `EVIDENCE.md` in CXO-facing text.
- **Self-contained repo:** anything we rely on is recorded under `docs/research/`.
- **Spend:** Anthropic first, hard cap of 50 USD across all runs; OpenAI for cross-checks or the adversarial judge.
- **Formats:** Markdown first; a Claude Code artifact and a Slidev deck once the content is close to final.

## 5. Issue register

This is the live copy. `PLAN.md` §10 holds the same list as of 2026-10-05 and will be replaced by a pointer here once this roadmap is approved.

| ID | Issue | Status |
|---|---|---|
| ASSIST-001 | Read-only collaborators are not possible on a private repo owned by a personal account (GitHub Docs, `EVIDENCE.md` E-27) | Accepted: decision D6 keeps the repo on the personal account; anyone invited will have write access |
| ASSIST-002 | Git identity mismatch between git config and the session account | Closed: commits use `pcosta@gmail.com` (D7) |
| ASSIST-003 | Parts of Pedro's notes were not synced to the machine and could not be read, including the strategy and product-management material | Open, not blocking |
| ASSIST-004 | Research figures tagged [S] are unverified; quotations gathered by sub-agents need their wording re-checked at the source | Open; rows E-10, E-14, E-17, E-18, E-23 |
| ASSIST-005 | Three articles were read only through a summarising fetch; no article figure is usable as evidence | Open, not blocking |
| ASSIST-006 | Model access and spend ceiling | Closed: keys in a git-ignored `.env`, cap 50 USD (D5) |
| ASSIST-007 | Some source material sits in Pedro's private folders | Closed by D9 |
| ASSIST-008 | One link in the brief was malformed | Closed: corrected in `docs/init-prompt.md` |
| ASSIST-009 | No cost inputs exist for the CFO message | Closed as an issue; carried as open question T8 |
| ASSIST-010 | Omnigent already provides cross-harness policy, sandboxing, budgets and shared sessions | Closed: that layer is out of our proposal |
| ASSIST-011 | Plain `git push` has no GitHub credentials on this machine; pushes go through the GitHub CLI's login for a single command | Open, not blocking |
