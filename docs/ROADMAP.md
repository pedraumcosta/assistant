# ROADMAP — ASSIST

| | |
|---|---|
| Status | Working document. Records only what is already known or done. Steps that depend on the thesis details are listed but not scoped. |
| Last updated | 2026-10-05 |
| Reads with | `docs/PLAN.md` (takes precedence) and `docs/JOURNAL.md` (what happened and why) |

## 1. Where we are

- The plan exists and ten working decisions are recorded in it (`PLAN.md` §2).
- Research is done and recorded in `docs/research/`: the first pass, the full re-reads, and three sets of Pedro's own material checked against their sources (his Notion notes, his web research notes, and his analysis of the harness paper), with four papers read in full along the way.
- The thesis has an agreed direction and open details (§2 below). After the research, the open ground is narrow and the case for Wait is stronger than at the start (`PLAN.md` §1).
- Nothing has been designed or built yet. No proposal text exists.

## 2. The thesis: what is agreed and what is open

**Agreed direction (2026-10-05).** We do not build a coding assistant, a harness, or a meta-harness. The candidate product is an evidence layer: a change contract, deterministic verification after the agent stops, an evidence bundle and risk routing, delivered as a plug-in to existing harnesses, and entered through per-repo agent evaluation. "Wait, with a review date" remains a possible conclusion.

**Open details.** None of these has been decided. The roadmap steps in §3.3 cannot be scoped until they are. The third column records what the research offers so far; it is input for the discussion, not a decision.

| # | Open question | Why it matters | Input so far |
|---|---|---|---|
| T1 | Who is the buyer and which team feels the pain first | Shapes the value proposition, the adopt / supplement / replace argument and the CFO message | Nothing beyond the market research One paper argues regulated industries need human oversight and audit evidence for agent-written code, with no buyer or demand data. OpenAI's own account suggests the buyer is not a high-throughput new build, where "corrections are cheap"; it is a team where a wrong change is expensive. |
| T2 | How we differ from review bots, from Omnigent's policy plane, from a vendor's own evaluator agent, and from the harness's native spec and task features | Every one of these exists or is cheap to add | What no source provides: a verdict that is deterministic, independent of the model vendor, and measured for error on the customer's repo, with an auditable record. Native features cover the planning half of a contract; the agent still marks its own work complete. Two papers already publish the framing (Production-Qualified Change, Verification Tax, control plane) and the risk tiering. Neither implements or measures anything. Checked against the market on 2026-10-05: CodeRabbit (1.5 billion USD valuation) sells risk routing and merge blocking on model judgment and is positioning as "the control layer"; Sonar sells a deterministic static-analysis gate; Faros sells per-repository agent benchmarks. None runs the customer's acceptance checks against a pre-agreed contract, publishes a false-pass rate, or keeps an outcome record. |
| T3 | What we claim is defensible, given no inherited moat (D2) | Decides between Build and Wait | Candidates: neutrality, and each customer's accumulated contracts and evaluation history. The research calls this thin. The paper puts the half-life of a distinctive feature at weeks. After the two papers, what is left is a protected contract, a verifier with a measured false-pass rate, and being first with measurements. The most likely way the opening closes is a funded review vendor joining parts it already owns. From Pedro's analysis: recalibrating risk tiers from measured outcomes gives each customer's accumulated data a job. Decision-model research adds a mechanism: a few hundred labelled outcomes recalibrate a cheap classifier, and our layer produces those labels per repository. No shipped product was found doing this. |
| T4 | Where contracts come from for ordinary changes | The largest open product assumption | Anthropic's design has the generator draft the contract and a second party approve it before work starts. One practitioner source skips the spec entirely for small changes, which leaves ordinary work without a contract unless it is derived from the harness's own plan. |
| T5 | Which harnesses the plug-in targets first, and through which attachment points | Hook surfaces differ by vendor; sets the cost of being harness-agnostic | Hooks exist in nine of the eleven harnesses studied; two share hook names. CI needs no vendor hook. Reading a harness's transcript files works without cooperation but rests on an undocumented format. Running inside the customer's CI with their own model access removes most procurement requirements; the audit record is the one that applies in full. From Pedro's analysis: ship the gate as an Omnigent policy evaluator, one integration reaching every harness Omnigent wraps. Omnigent's adoption is unknown and Databricks could add the check itself. A hosted decision model would send customer diffs outside their environment; default to a self-hostable classifier. |
| T6 | What is explicitly excluded from the product | Required by the brief | Agreed so far: no assistant, no harness, no meta-harness, no policy / sandbox / budget layer Candidate addition from the research: we do not build the wider control plane (model routing, stop rules, cost attribution). |
| T7 | The redlines and the kill criteria, with their thresholds | Required by the brief; thresholds are decisions for Pedro, not data | Apply the gate by risk, not uniformly: the vendor's own finding is that a check earns its cost only on work beyond what the model does reliably. An expected-value formula for autonomy tiers comes from an article we could not find (ASSIST-012). Two published starting points now exist: an autonomy budget constrained by money, reliability risk and human attention; and three oversight tiers assigned by regulatory impact, customer proximity, reversibility and data sensitivity. Candidate redline: the agent that writes a change cannot approve it. A calibrated decision model is a candidate for assigning risk tiers, never for the correctness verdict; measured evidence shows such models repeat LLM judges' errors on text rubrics. |
| T8 | The assumptions behind the CFO message (people, weeks, what a pilot costs) | No inputs exist; every figure will be a labelled assumption | None Pedro's notes record the objection a CFO will raise: a new entrant must justify margin above token pass-through. Our gate adds compute, so pricing would have to rest on verified output. |
| T9 | Whether the prototype in `PLAN.md` §7 is the right smallest test of the thesis | The arms, hypotheses and task set follow from T1 to T4 | The comparison arm now resembles the vendor's evaluator agent. Tasks that look like ordinary work may stop discriminating as models improve. A cheaper model carrying the main loop is unproven. Results should be reported in the published metric set, with the verifier's false-pass rate added. The cheaper-model arm is confounded if it shares the frontier arm's harness. The comparison that now matters most is a deterministic verdict against a model reviewer's. The agent under test is now the harness paper's published scaffold (D3 refined). Pedro's analysis would stress cross-agent use; after the market check that stays a stretch goal. Decided 2026-10-05: a decision-model judge is the next enhancement after the first prototype, not part of it. |
| T10 | How the product stays valuable as models improve | The check's value moves with every model release | Aim at work beyond the model's reliable range; treat measurement as recurring per model and harness pairing. Whether that is a business is open. The ablation paper finds scaffolding value changes in size and sign with the model; it does not simply fade. That supports repeated per-pairing measurement. |

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

### 3.2 In review

| Step | Output | Exit check | Waiting on |
|---|---|---|---|
| Thesis details | Answers to T1 to T10, recorded in the journal as decisions | Each open question in §2 is either decided or explicitly deferred with a reason | Discussion with Pedro |

### 3.3 Not started

These are the remaining phases from `PLAN.md` §6. Their content depends on §2; only their purpose and exit check are fixed.

| Phase | Output | Exit check (from the plan) | Depends on |
|---|---|---|---|
| Evidence verification | `docs/research/EVIDENCE.md` with no [S] row in use | Every figure we intend to use is tagged [P] or [L], or is dropped | Knowing which figures the proposal needs (T1, T2) |
| Problem and product | `docs/PROPOSAL.md` §1–2 | Includes the case against entering; exclusions are explicit | T1, T2, T3, T6 |
| System design | `docs/DESIGN.md` | Each design topic has a position, a rejected alternative and a way to measure it; risks, assumptions and redlines stated | T4, T5, T7 |
| Prototype | `prototype/` | Each slice runs end to end on the fixture repo | T9 |
| Measurement | `docs/RESULTS.md`, `prototype/runs/` | Results table generated from run files, limitations stated, spend within the 50 USD cap | Prototype |
| Next enhancement: decision-model judge and recalibration test | A fourth verdict source in the evaluation, and a measurement of how far the prototype's own deterministic outcomes improve a classifier's calibration | Reported on false-pass rate, variance, cost and latency beside the other verdict sources; limits stated | First prototype measured; a TypeSafe API key or a local open build |
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

This is the only copy of the register (decided 2026-10-05). `PLAN.md` §10 points here.

| ID | Issue | Status |
|---|---|---|
| ASSIST-001 | Read-only collaborators are not possible on a private repo owned by a personal account (GitHub Docs, `EVIDENCE.md` E-27) | Accepted: decision D6 keeps the repo on the personal account; anyone invited will have write access |
| ASSIST-002 | Git identity mismatch between git config and the session account | Closed: commits use `pcosta@gmail.com` (D7) |
| ASSIST-003 | Parts of Pedro's notes were not synced to the machine and could not be read, including the strategy and product-management material | Open, not blocking |
| ASSIST-004 | Research figures tagged [S] are unverified; quotations gathered through a summarising fetch need their wording re-checked at the source | Open; rows E-10, E-14, E-18 remain [S]. E-17 confirmed 2026-10-05. `market-landscape.md` is partly superseded by `check-market-claims.md` |
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
