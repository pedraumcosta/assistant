# ROADMAP — ASSIST

| | |
|---|---|
| Status | Working document. Records only what is already known or done. Steps that depend on the thesis details are listed but not scoped. |
| Last updated | 2026-10-05 |
| Reads with | `docs/PLAN.md` (takes precedence) and `docs/JOURNAL.md` (what happened and why) |

## 1. Where we are

- The plan exists and ten working decisions are recorded in it (`PLAN.md` §2).
- Research is done and recorded in `docs/research/`: the first pass, the full re-reads, and three sets of Pedro's own material checked against their sources (his Notion notes, his web research notes, and his analysis of the harness paper), with four papers read in full along the way.
- The thesis is decided (§2 below): the evidence layer, pursued as a three-stage probe that ends in Build or Wait.
- The first two sections of the proposal are drafted. Nothing has been designed or built yet.

## 2. The thesis

**Decided on 2026-10-05.** The decisions and their justifications are in `PLAN.md` §2.1; the rationale is in `JOURNAL.md` ADR-014 to ADR-016. In brief:

- **Posture:** a small, dated probe in three stages (prototype, measurement pilot, build), each able to end it.
- **Frame:** tooling for evidence-driven development. A tool for the team's delivery process, not a plug-in for an assistant; one standard of evidence for every change, whoever or whatever wrote it.
- **Thesis:** the evidence layer. The brownfield specialisation was evaluated and is not pursued; brownfield is not claimed as a first market.
- **Buyer:** engineering leaders, as sponsors, in organisations that build software.
- **Product:** a first process that guides the user to create the checks; a protected contract; a verdict of executable evidence; an outcome record; a measured false-pass rate, repeated and adapted for each model and harness pairing.
- **The verdict is always executable, not always deterministic:** tests for conventional code; an evaluation for an LLM application. The prototype starts with the conventional case; the evaluation path is designed, and built only as a bonus.
- **Cost to the delivery process is stated, not hidden:** the product adds time and cost at four stages and adds waiting before merge. Whether it repays that in review, rework and incidents avoided is what the pilot must show.
- **Customer data:** used only as the customer has been told and agreed, and kept in their environment.
- **Not built:** an assistant, an agent loop, a meta-harness, a policy or sandbox layer, a review bot, the wider control plane, a model.

**Still open**

| # | Open item | Waiting on |
|---|---|---|
| T7 | The review date that applies if the recommendation becomes Wait | Pedro |
| T8 | The assumptions behind the CFO message. Working assumption: two engineers and a part-time product lead for six weeks for the pilot | Revisited once the prototype is ready |

The research inputs that fed each decision are in `PLAN.md` §3 and `docs/research/`.

## 3. Steps

Status values: Done, In review, Not started, Blocked.

### 3.1 Done

| Step | Output | Commit | Date |
|---|---|---|---|
| Local repository, brief and draft plan | `docs/init-prompt.md`, `docs/PLAN.md`, `.gitignore` | `4f77bbc`, `c503de6` | 2026-10-03 |
| First plan discussion: decisions D2 to D5 and D7 to D10; thesis narrowed after first reading of the harness paper | `PLAN.md` §1.1, §2 | `69c025b` | 2026-10-03 |
| Private GitHub repository created and pushed | `pedraumcosta/assistant` | — | 2026-10-05 |
| Research records and evidence ledger; decisions D1 (direction) and D6; prototype arms revised | `docs/research/` (13 files), `PLAN.md` §1.1, §3.4, §7.1 | `95e0f83` | 2026-10-05 |
| Roadmap and journal drafted; issue register moved to this file | `docs/ROADMAP.md`, `docs/JOURNAL.md` | `208185e`, `6aedc7f` | 2026-10-05 |
| Second round of sources: Pedro's Notion notes checked against the sources, six of them read in full | `docs/research/notion-notes-2026-10-01.md`, six new article records, `PLAN.md` §3.6 and §7.1 | The commit after `6aedc7f` | 2026-10-05 |
| Two papers read in full: verification economics (prior art for our framing) and graduated oversight | `docs/research/paper-verification-economics.md`, `docs/research/paper-governed-ai-engineering.md`, `PLAN.md` §3.7 | The commit after `6aedc7f` | 2026-10-05 |
| Third round: Pedro's web research notes checked in raw source pages; ablation paper read; review and verification segment researched | `docs/research/web-research-notes-2026-10-01.md` and five companion records, `PLAN.md` §3.8 | The commit after `6aedc7f` | 2026-10-05 |
| Pedro's analysis of the harness paper checked against the paper; decision D3 refined | `docs/research/harness-paper-implications-2026-10-02.md`, `PLAN.md` §3.9 | The commit after `6aedc7f` | 2026-10-05 |
| Pedro's addendum on decision models checked at primary sources | `docs/research/decision-models-2026-10-02.md` and two check files, `PLAN.md` §3.10 | The commit after `d3f988e` | 2026-10-05 |
| Second thesis (brownfield specialisation) evaluated from its primary sources and the market | `docs/research/second-thesis-brownfield.md` and four records, `PLAN.md` §3.11 | The commit after `4986533` | 2026-10-05 |
| Pedro's pointers on market structure and agent limits traced to public sources and checked | `docs/research/market-and-limits-evidence.md` and two check files, `PLAN.md` §3.12; `practitioner-notes.md` replaced by a list of principles | The commit after `b2f1985` | 2026-10-05 |
| Thesis discussion: posture, thesis, buyer, differentiation, exclusions, kill criteria and prototype scope decided | `PLAN.md` §2.1, `JOURNAL.md` ADR-014 to ADR-016 | The commit after `5b7fef5` | 2026-10-05 |
| Evidence verification: ledger rows E-01 to E-29 re-checked against raw sources | `docs/research/EVIDENCE.md` | The commit after `1e3d2c5` | 2026-10-05 |

### 3.2 In review

| Step | Output | Exit check | Waiting on |
|---|---|---|---|
| Problem and product | `docs/PROPOSAL.md` sections 1 and 2, drafted 2026-10-05 | Includes the case against entering; exclusions are explicit | Pedro's review |

### 3.3 Not started

These are the remaining phases from `PLAN.md` §6. With the thesis decided, they can be scoped.

| Phase | Output | Exit check (from the plan) | Depends on |
|---|---|---|---|
| System design | `docs/DESIGN.md` | Each design topic has a position, a rejected alternative and a way to measure it; risks, assumptions and redlines stated | Nothing; can start |
| Prototype | `prototype/` | Each slice runs end to end on the fixture repo | System design |
| Bonus: evaluation path for an LLM application | One small task verified by an evaluation, end to end | Three-way result reported; hidden cases never shown to the agent; any model scorer's agreement with labels stated | Prototype; time remaining |
| Measurement | `docs/RESULTS.md`, `prototype/runs/` | Results table generated from run files, limitations stated, spend within the 50 USD cap | Prototype |
| Next enhancements: counterexample search; decision-model judge and recalibration test | A search for hidden behavioural differences that produces executable failing tests; a fourth verdict source in the evaluation; and a measurement of how far the prototype's own outcomes improve a classifier's calibration | Reported on false-pass rate, variance, cost and latency beside the other verdict sources; limits stated | First prototype measured; a TypeSafe API key or a local open build |
| Proposal, design view, CFO message | `PROPOSAL.md` complete; Claude Code artifact; Slidev deck | Recommendation is consistent with the results, including if the hypotheses fail | Measurement; the CFO assumptions (T8) |
| Build log and final review | `docs/BUILD_LOG.md` | No number without an evidence row; no ASSIST issue unaccounted for | All of the above |

## 4. Working rules in force

- **Commits** only after Pedro confirms; one per meaningful step; `Co-Authored-By: Claude` trailer kept.
- **Never committed:** `docs/scratchpad.md`, `.env`.
- **Numbers:** none invented or estimated; only [P] and [L] rows of `EVIDENCE.md` in CXO-facing text.
- **Self-contained repo:** anything we rely on is recorded under `docs/research/`.
- **Citations:** research records cite public sources. Pedro's private notes may be named as the origin of a claim, never cited or quoted by path.
- **Spend:** Anthropic first, hard cap of 50 USD across all runs; OpenAI for cross-checks or the adversarial judge.
- **Formats:** Markdown first; a Claude Code artifact and a Slidev deck once the content is close to final.

## 5. Issue register

This is the only copy of the register (decided 2026-10-05). `PLAN.md` §10 points here.

| ID | Issue | Status |
|---|---|---|
| ASSIST-001 | Read-only collaborators are not possible on a private repo owned by a personal account (GitHub Docs, `EVIDENCE.md` E-27) | Accepted: decision D6 keeps the repo on the personal account; anyone invited will have write access |
| ASSIST-002 | Git identity mismatch between git config and the session account | Closed: commits use `pcosta@gmail.com` (D7) |
| ASSIST-003 | Parts of Pedro's notes were not synced to the machine and could not be read, including the strategy and product-management material | Open, not blocking |
| ASSIST-004 | Research figures tagged [S] were unverified, and early quotations had been gathered through a summarising fetch | Closed 2026-10-05: rows E-01 to E-29 re-checked against raw sources; no [S] row remains. `market-landscape.md` is still partly superseded by `check-market-claims.md` |
| ASSIST-005 | Three articles were read only through a summarising fetch; no article figure is usable as evidence unless it has a row in `EVIDENCE.md` | Open, not blocking |
| ASSIST-006 | Model access and spend ceiling | Closed: keys in a git-ignored `.env`, cap 50 USD (D5) |
| ASSIST-007 | Some source material sits in Pedro's private folders | Closed by D9 |
| ASSIST-008 | One link in the brief was malformed | Closed: corrected in `docs/init-prompt.md` |
| ASSIST-009 | No cost inputs exist for the CFO message | Closed as an issue; carried as open question T8 |
| ASSIST-010 | Omnigent already provides cross-harness policy, sandboxing, budgets and shared sessions | Closed: that layer is out of our proposal |
| ASSIST-011 | Plain `git push` has no GitHub credentials on this machine; pushes go through the GitHub CLI's login for a single command | Open, not blocking |
| ASSIST-012 | One article in Pedro's Notion notes ("Copilot vs Private AGI") could not be found; its points are unchecked and not usable. Its autonomy formula is no longer needed: a published equivalent is recorded in `PLAN.md` §3.7 | Open, not blocking; needs the link from Pedro |
| ASSIST-013 | Unread leads: Anthropic's earlier long-running harness post, and the primary studies cited second-hand by the verification-economics paper. The two arXiv papers first listed here were read on 2026-10-05 | Open; Pedro to decide whether they are read |
| ASSIST-014 | Bloomberg, Forbes, OpenAI's site, EUR-Lex and SEC full-text search block automated download. Items resting on them use an equivalent primary source, an archive capture, or are marked secondary | Open, not blocking |
| ASSIST-015 | The decision-model enhancement needs a TypeSafe API key or a local open build; neither is in place | Open, not blocking the first prototype |
| ASSIST-016 | The label "evidence-driven development" has not been searched in trademark registers; the registers could not be queried automatically | Open; needs a manual search before any public use |
