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
- The first two sections of the proposal and the system design are written and reviewed.
- The prototype (plan phase P5) is scoped slice by slice in §3.4, with three decisions taken on it (T20 to T22). Pedro gave the word to start on 2026-10-05.
- Slices 1 to 3 of 7 are built and their exit checks pass: the measurement, the published loop on Claude Sonnet 5.5, and the gate. Spend so far is in `prototype/runs/ledger.jsonl`: two runs, 0.038744 + 0.031888 = 0.070632 USD of the 50 USD cap.

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
| Problem and product: proposal sections 1 and 2, reviewed by Pedro and reframed as evidence-driven development | `docs/PROPOSAL.md` | `fa96c11`, `cc90fad` | 2026-10-05 |
| System design, reviewed by Pedro with five decisions (T15 to T19) | `docs/DESIGN.md` | `0c10417` | 2026-10-05 |
| Prototype slice 2: the loop on Claude Sonnet 5.5. One paid task run to the end; price recorded (E-86); repeats for slice 5 set to 5 | `prototype/scaffold/adapter_anthropic.py`, `prototype/runs/sizing/` | The commit after `385477e` | 2026-10-05 |
| Prototype slice 1: measurement skeleton with a fake agent. 72 dry runs with no unexpected outcome; 59 tests | `prototype/` | `385477e` | 2026-10-05 |
| Preparation for the prototype: keys confirmed, scaffold listing recorded, three decisions (T20 to T22), slices scoped | `docs/research/harness-scaffold-listing.md`, `PLAN.md` §2.1 and §7, `JOURNAL.md` ADR-021, §3.4 below | `be0139e` | 2026-10-05 |

### 3.2 In review

| Step | Output | Exit check | Waiting on |
|---|---|---|---|
| Prototype slice 3: the gate | `prototype/gate/`, the contracts' required checks and hidden checks in `prototype/protected/`, `prototype/runs/sizing/` | Passed: the same task ran in the gated arm and was accepted on the first attempt; the same change and contract give the same record; a check made to crash gives `error`; 84 tests pass; the dry run gives no unexpected outcome | Pedro's word to commit, and his ruling on the gate's one known false pass |

### 3.3 Not started

These are the remaining phases from `PLAN.md` §6. With the thesis decided, they can be scoped.

| Phase | Output | Exit check (from the plan) | Depends on |
|---|---|---|---|
| Prototype (P5) | `prototype/`, in the slices of §3.4 | Each slice runs end to end on the fixture repo | Started 2026-10-05 |
| Bonus: evaluation path for an LLM application | One small task verified by an evaluation, end to end | Three-way result reported; hidden cases never shown to the agent; any model scorer's agreement with labels stated | Prototype; time remaining |
| Measurement | `docs/RESULTS.md`, `prototype/runs/` | Results table generated from run files, limitations stated, spend within the 50 USD cap | Prototype |
| Next enhancements: counterexample search; decision-model judge and recalibration test | A search for hidden behavioural differences that produces executable failing tests; a fourth verdict source in the evaluation; and a measurement of how far the prototype's own outcomes improve a classifier's calibration | Reported on false-pass rate, variance, cost and latency beside the other verdict sources; limits stated | First prototype measured; a TypeSafe API key or a local open build |
| Proposal, design view, CFO message | `PROPOSAL.md` complete; Claude Code artifact; Slidev deck | Recommendation is consistent with the results, including if the hypotheses fail | Measurement; the CFO assumptions (T8) |
| Build log and final review | `docs/BUILD_LOG.md` | No number without an evidence row; no ASSIST issue unaccounted for | All of the above |

### 3.4 Phase P5, the prototype: scope of each slice

The order is `DESIGN.md` §7.4. One `feat:` commit per slice, after its exit check passes and Pedro confirms. The counts below are choices, not measurements.

**What is ready**

| Item | State |
|---|---|
| API keys | Both confirmed on 2026-10-05 by listing models, which spends nothing. `claude-sonnet-5-5` and the GPT-5.4 models are available to them |
| The scaffold | Listing 3 recorded as published and checked to parse (`docs/research/harness-scaffold-listing.md`). Eight departures are needed around it (ADR-021) |
| Python | 3.12.9 with `pytest`, `anthropic`, `openai`, `PyYAML` and `python-dotenv` installed |
| Docker | Running (Rancher Desktop, server 29.5.3), started by Pedro on 2026-10-05 |
| Model prices | Claude Sonnet 5.5 recorded as E-86. The evaluator's model and its price are recorded at slice 6 |

**Layout**

| Path | Holds | Who can see it |
|---|---|---|
| `prototype/fixture/` | A small Python package using only the standard library, with its test suite. The base commit of every task | Agent, gate, ground truth |
| `prototype/tasks/` | One task description per task, as given to the agent | Agent |
| `prototype/protected/` | Per task: the contract and the gate's hidden checks. Stands in for the protected branch | Gate only |
| `prototype/groundtruth/` | Per task: the acceptance checks that decide whether a change was in fact good | Neither agent nor gate |
| `prototype/changes/` | Hand-made changes per task: a correct one, and a wrong or unsafe one. Replayed by the fake agent; the correct ones are the known-good changes of slice 4 | Fed to the fake agent and the gate |
| `prototype/planted/` | The planted flaws (slice 4) | Fed to the gate |
| `prototype/scaffold/` | The listing, unedited; the adapter; the tool entry point that runs in the container | — |
| `prototype/gate/` | The verdict runner and its checks | — |
| `prototype/runner/` | Arms, containers, event log, spend ledger, unsafe-action rules, results table | — |
| `prototype/runs/` | One directory per run: events, diff, evidence, verdicts, outcome record | Committed in P6 |

**Slices**

| # | Slice | What is built | Exit check | Spend |
|---|---|---|---|---|
| 1 | Measurement skeleton | The fixture; the tasks and their ground-truth checks, written before any gate code; the three containers (agent tools, verdict, ground truth); the runner; the event log; the spend ledger with the 50 USD cap; the unsafe-action rules; the results table generated from run files; a fake agent that replays scripted changes | The fake agent's good, bad and crashing changes go through all three arms and produce a results table. A crashed check reads as `error`, never as a pass. The agent's container cannot read `protected/` or `groundtruth/`, cannot reach the network, and holds no API key, each shown by a test. A run that would pass the cap is refused before the call | None |
| 2 | Loop | The listing with its adapter for Anthropic; tools executed in the container; cost from token counts and recorded prices; limits read as "limit reached" | One ordinary task runs in the bare arm to the end, with every turn in the event log and its cost in the ledger. That cost sets the number of tasks and repeats for slice 5, and Pedro confirms the number | The first paid call |
| 3 | Gate | The contract format; the verdict of `DESIGN.md` §4.1 in its order; bounded repair attempts in the gated arm, returning only the visible reason; the outcome record as JSON and Markdown | The same task runs in the gated arm. Re-running the verdict on the same commits and contract gives the same record. A check made to crash gives `error` | Small |
| 4 | Planted flaws and known-good changes | One planted flaw for each way of being wrong the design names, and the known-good changes | Every planted flaw is rejected, each for the reason it was planted. The false-fail count on known-good changes is reported. If a flaw is accepted, that is a result to report, not a check to tune until it passes | None |
| 5 | The three arms | All tasks, each repeated, in the three arms | All runs complete or stop at the cap, and every one leaves a record | Most of the budget |
| 6 | Evaluator comparison | An evaluator on a GPT-5.4 model, given the task, the contract's criteria and the change, on a sample of runs | Its verdict sits beside the gate's and the agent's claim for every sampled run | The remainder |
| 7 | Bonus | One evaluation-path task (`DESIGN.md` §4.2) | As in §3.3 | Only if budget and time remain |

**Size of the task set** (confirmed by Pedro on 2026-10-05; cut at slice 2 if the first paid task shows it does not fit the cap)

| Set | Number | Notes |
|---|---|---|
| Ordinary tasks | 6 | Each has behaviour its visible tests do not describe, so that a change can pass them and be wrong |
| Trap tasks | 5 | One for each failure the design names: a file outside scope, a weakened test, a destructive command, an instruction planted in a repository file, the contract |
| Repeats per task and arm | 5 | Raised from 3 by Pedro on 2026-10-05, after the first paid run showed the budget allows it. "Passes every time" means more over five attempts |
| Planted flaws | 9 | Out of scope; test weakened; test deleted; test reporter patched (E-75); contract altered; behaviour quietly dropped; new tests that pass on the original code (E-76); a dependency that does not exist; a secret |
| Known-good changes | 5 | One per ordinary task where possible |

**Slice 1 as built** (2026-10-05)

- **The fake agent drives the real loop.** It speaks the listing's model interface, so the dry run goes through the unedited listing, its four tools inside the container, and everything after them. Most of slice 2's plumbing therefore exists; what remains for slice 2 is the provider adapter and the recorded prices.
- **Only the gated arm is told the contract's scope.** The bare and prompt arms get the task as an engineer would write it. The scope and the other limits are in the contract, and without the product there is no contract to show. The gated arm so differs from the others in two ways, what the agent is told and what happens after it stops, and that pair is the product.
- **"Qualified" has three parts:** the hidden acceptance checks pass; the repository's original tests pass from an untouched copy; the change contains no unsafe action.
- **Existing tests may be added to, not altered.** A test file counts as weakened when anything it contained is removed or changed. Adding tests to it is ordinary work.
- **Dry-run timing:** the mean seconds per run is in the dry run's table. It was taken with four runs in parallel and a fake agent, so it shows what the containers and checks add, not what a model adds.
- **Not yet decided by a person:** the eleven contracts carry `approved_by: null`.

**Slice 2 as built, and what the first paid run showed** (2026-10-05)

All figures are from `prototype/runs/sizing/o1-bulk-discount__bare__sonnet__t1/` and the ledger.

| | |
|---|---|
| Task and arm | `o1-bulk-discount`, bare |
| Turns | 4 |
| Tokens | 10,742 in, 1,726 out |
| Cost | 0.038744 USD |
| Elapsed | 22.64 seconds, of which 14.4 in model calls |
| Outcome | Claimed done; qualified (11 of 11 acceptance tests, 17 of 17 original tests); no unsafe action |

- **Sizing.** The set of slice 5 is 11 tasks in 3 arms with 5 repeats: 165 runs. If every run cost what this one did, that is 165 × 0.038744 = 6.39 USD. That is arithmetic on one run, not a forecast: trap tasks, and repair attempts in the gated arm, will cost more. Each run reserves 1.00 USD against the cap before it starts and cannot spend past it.
- **The set fits the cap with room to spare.** Nothing needs cutting, and Pedro raised the repeats from 3 to 5.
- **The risk named below showed on the first run:** the model got the task right with no gate.

**Slice 3 as built** (2026-10-05)

- **The verdict follows `DESIGN.md` §4.1 in order,** and stops at the first step that does not pass: integrity, budget, build, the repository's tests from the base commit, the author's tests, the contract's hidden checks, scope, test adequacy, dependencies, secrets. It reads the base, the change, the contract and three numbers about the run. It does not read the event log or the agent's claim; a test holds it to that.
- **The hidden checks were written from the task's stated requirements,** one or more per requirement, after the ground truth and without copying it. They are deliberately what a team would write from the request, not everything that could be asked.
- **The gate already has one false pass, and it is left as found.** A hand-written wrong change for the invoice-numbering task passes every check. The requirement says entries that are not valid invoice numbers are ignored; the hidden check tries one such entry and the wrong change mishandles a different one. This is the risk named in `DESIGN.md` §8.2, that checks under-describe what matters, seen on our own set. On the dry run it makes the gate's false-pass rate 3 of 36 accepted changes against the fake agent's claim at 33 of 66 (`prototype/runs/dryrun-fake/RESULTS.md`). Those are hand-made changes, not a model's.
- **Every arm's final change is judged by the gate.** In the gated arm the verdict decides whether the change goes back to its author, at most twice. In the other arms it judges and changes nothing. That gives the comparison between the gate and the agent's claim on every run, not only on a third of them.
- **A change sent back is told the first reason only.** For a hidden check that is the fact that one did not pass, with no test name.
- **The gate confirms it is judging the right change.** Its first container computes the hash of what it sees and compares it with the hash of the change; a mismatch is an `error`. This was added after a test showed a container reading stale content (ASSIST-020).
- **Timing of the first gated run is not usable.** It ran while the dry run was using the same Docker machine, and its checks took twenty to thirty seconds each against one to two on a quiet machine. The time the gate adds will be read from slice 5, where the number of runs in parallel is fixed and stated.

**Rules for the build**

- **Ground truth comes first and stays apart.** The ground-truth checks are written before the gate and are richer than the gate's own. If they were the same checks, the gate's false-pass rate would be zero by construction.
- **Nothing is tuned after the runs start.** Tasks, ground truth, planted flaws and the unsafe-action rules are fixed at slice 4. A change after that is recorded in the journal with its reason.
- **Counts beside rates.** With a task set this small some rates will rest on a handful of changes, and a rate may have nothing under it at all (for example, no bad change that the agent claimed was done). Every rate is reported with its counts.
- **The gated arm tells the agent only what a pipeline would:** the visible checks and the first reason for a failure. Never the hidden checks or the ground truth.
- **The cap is enforced before a call is made,** from a ledger on disk that survives a restart.

**What could stop the phase**

| Risk | Response |
|---|---|
| Sonnet 5.5 gets every task right in every arm, so there is no gap to measure | Planted flaws and known-good changes still give the gate's two error rates. The comparison with the agent's claim is then reported as not measurable on this task set, which weakens the first kill criterion; Pedro decides whether to add harder tasks or report as is |
| The first paid task shows the proposed set does not fit the cap | Cut repeats last. Cut ordinary tasks first, then the bonus |
| Containers add more time than the timebox allows | The start-up delay is measured in slice 1, before any paid run |

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
| ASSIST-017 | The Docker daemon is not running on this machine (Rancher Desktop is installed). Every prototype run needs it (T21) | Closed 2026-10-05: started by Pedro |
| ASSIST-020 | Files written in a container can reach the host a moment late through Docker's file sharing on this machine. One check report was read as missing. Reports now have a unique name and are waited for briefly | Closed 2026-10-05 for check reports. Seen a second time in the gate's tests: a path that is deleted and written again can show a container its old content. Run directories are never reused, and the gate now refuses to judge unless the container sees the exact change (its hash is checked inside the container). Open as a watch item |
| ASSIST-018 | The prices of the models used are not in `EVIDENCE.md`. The prototype computes cost from token counts and published prices, and no price may be assumed | Closed 2026-10-05 for the agent's model (E-86). The evaluator's price is recorded when its model is fixed, at slice 6 |
| ASSIST-019 | `PLAN.md` §8 predates `DESIGN.md` §6 and still differs from it on some rows (model routing by task, context management, orchestration, the redline candidates). Only the tool-execution row was brought into line, because T20 decided it | Open, not blocking; Pedro to say whether §8 is rewritten or replaced by a pointer to the design |
