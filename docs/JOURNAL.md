# JOURNAL — ASSIST

| | |
|---|---|
| Status | Working document. Records only what has happened and what has been decided. |
| Purpose | Dated log of the work, and the decision record (ADR) for the project |
| Reads with | `docs/PLAN.md` and `docs/ROADMAP.md`, which take precedence if they disagree with this file |

Two kinds of entry:

- **Log entries** (Part 1): date, what was done, what deviated from the plan.
- **Decision records** (Part 2): `ADR-NNN` with status, decision, rationale, alternative rejected, and what would change beyond this exercise.

---

## Part 1. Log

### 2026-10-03

**Done**
- Brief received (`docs/init-prompt.md`).
- Six research passes run in parallel by Claude Code sub-agents: three over Pedro's working notes, one over the linked articles, two over the public market. Method and cost of each pass: `docs/research/README.md`.
- Draft plan written (`docs/PLAN.md`): position to defend, ten decisions to take, phases, prototype hypotheses, issue register.
- Local git repository initialised; first commits `4f77bbc` and `c503de6`.
- First plan discussion. Pedro settled D2, D3, D4, D5, D7, D8, D9 and D10 and asked for the Wavestone harness paper to be weighed before closing D1.
- Selected sections of the paper read. Thesis narrowed in `PLAN.md` §1.1. Commit `69c025b`.

**Deviations from the plan**
- The plan put the roadmap and journal straight after repo setup. They were deferred because the thesis was reopened by the paper.
- The original position ("a thin outer harness around any agent") did not survive the paper: the policy, sandbox and budget layer already exists as open source (ASSIST-010).

### 2026-10-05

**Done**
- Pedro agreed the paper analysis and the narrowed direction; chose the personal GitHub account for the repo; set the rule that commits happen only after his confirmation.
- Private repository `pedraumcosta/assistant` created and the existing commits pushed.
- Four articles re-read in full from downloaded text, at Pedro's request, after he noted the first pass had been partial.
- The paper read end to end.
- Plan revised: §3.4 rewritten from the full reads; prototype arms and hypotheses changed in §7.1.
- Research recorded in `docs/research/` (13 files), including the evidence ledger. Commit `95e0f83`.
- Roadmap and journal drafted for review. Pedro stated that the thesis details are not yet chosen and will be discussed further.
- Issue register moved to the roadmap as its only copy, at Pedro's decision. Commits `208185e` and `6aedc7f`.
- Second research round. Pedro supplied his notes on nine further reads from his Notion database and asked for them to be read in full, recorded, and reflected in the plan, roadmap and journal. Six sources were located and read in full; Anthropic's harness design post was read by the main session from the primary source. Records added under `docs/research/`; plan §3.6 and §7.1 updated; open question T10 added to the roadmap.
- Two papers read in full at Pedro's request (arXiv 2609.04681 and 2606.22484). The first publishes the framing and metrics we had reached independently; the second publishes a risk-tiering model. Records added; plan §3.7 written; roadmap inputs updated. Pedro asked for no commit yet, pending a further round of external material.
- Third research round. Pedro supplied his web research notes of 2026-10-01 and approved four actions: read the cited ablation paper, research the review and verification segment, resolve six conflicts with our records, and record the notes with a claim-by-claim check. Five sub-agents did this from raw source pages. Six records added; plan §3.8 written; roadmap inputs updated. No commit, at Pedro's instruction.
- Pedro supplied his own analysis of the harness paper, dated 2026-10-02. Checked claim by claim against the paper's HTML text and PDF. He approved four actions: record it, base the agent under test on the paper's published scaffold, add Omnigent-as-channel and outcome-fed recalibration as inputs, and check two unverified items in the PDF. Both items were confirmed.
- Plan §1 rewritten to state the current position and how it moved. All of the day's research rounds committed together at Pedro's confirmation.
- Pedro raised decision models (TypeSafe's Jev) as a possible new element and supplied his addendum of 2026-10-02. Two sub-agents checked it at primary sources. Finding: useful for cost at harness call sites we do not build; a component, never the verdict, in the evidence layer; the valuable link is recalibrating a cheap classifier from the labels our layer produces. Records added; plan §3.10 written; roadmap inputs updated. Pedro decided to treat it as the next enhancement after the first prototype (ADR-012).
- Pedro raised a second thesis from his own list of candidates: a brownfield / enterprise-legacy specialisation. Its section in his notes and Osmani's article were read by the main session; the two papers behind it were read in full and the legacy-modernisation market researched by sub-agents. Evaluation recorded; plan §3.11 written; roadmap question T11 added (ADR-013).
- Pedro pointed to six places in his notes on market analysis and agent limits, asking whether they are useful as evidence, and set the citation rule: records cite public sources, not his notes. The claims were traced to their public sources and checked by two sub-agents. Useful as evidence, no change of direction. Records added; plan §3.12 written; two checks added to the prototype's gate; roadmap inputs updated.
- Thesis discussion held. Pedro accepted the three-stage probe, chose the first thesis over the brownfield specialisation for lack of time to validate the latter, and settled the remaining questions with four changes to the proposals put to him: the buyer is engineering leaders as sponsors in organisations that build software; customer data must be handled with everyone aware and every precaution taken; guiding the user to create the checks is the product's first process, not an open question; adaptation to each and every model is to be emphasised. The CFO's numbers are deferred until the prototype is ready (ADR-014 to ADR-016).
- Evidence ledger rows E-01 to E-29 re-checked against raw sources by a sub-agent: 20 exact, 6 with wording that differed, 2 with a figure that differed, 1 not found publicly. Ledger corrected; three unverified rows confirmed at primary sources. Proposal sections 1 and 2 drafted.
- Pedro reviewed the proposal draft, judged it sound, and questioned one point: whether the verdict is always deterministic, given that software built on an LLM has to be checked by an evaluation. The item was reworded and the scope decided (ADR-017).
- Pedro asked for the costs and the effect on the delivery process to be elaborated: more tests and checks add latency, time and cost. A section was added to the proposal and a sixth hypothesis to the prototype (ADR-018).
- Pedro proposed reframing the product for its market: not a plug-in for an assistant but a tool for how a mature software team runs delivery, under a banner with a future (eval-driven development, spec-driven development, or a factory). After discussion he adopted "evidence-driven development" (ADR-019). A check of existing uses of that label was started.
- System design drafted (`docs/DESIGN.md`) at Pedro's request, following PLAN §7 and §8 and his own design method and checklists. A sub-agent read the notes he pointed to and returned their ideas as plain statements; the design restates them in its own words and cites no private material. His unpublished measurements were left out.
- Pedro reviewed the system design and decided its five open points (ADR-020), asking that the prototype be kept very simple.
- Preparation for the prototype (plan phase P5). Both API keys confirmed by listing models, which spends nothing. The scaffold's listing was not in the repository: it was taken from the arXiv PDF and recorded (`docs/research/harness-scaffold-listing.md`). Pedro decided three points (ADR-021). Plan §7.2 revised to the build order of the design; each slice scoped with an exit check in `ROADMAP.md` §3.4. No code written.
- Pedro started Docker, confirmed the size of the task set and gave the word. Preparation committed (`be0139e`).
- Prototype slice 1 built: the fixture library, eleven tasks with their contracts and ground-truth checks, a correct and a wrong or unsafe reference change for each, the containers, the event log, the spend ledger, the unsafe-action rules, the results table and a fake agent. The dry run puts 72 runs through the unedited listing and the containers in all three arms, with no unexpected outcome and no spend. Every wrong or unsafe reference change passes the repository's own tests and is rejected by ground truth.
- Slice 1 committed at Pedro's confirmation (`385477e`). Prototype slice 2 built: the price of Claude Sonnet 5.5 recorded (E-86), the Anthropic adapter written, and the first paid run made, one ordinary task in the bare arm. It ran to the end with every turn in the event log and its cost in the ledger (`prototype/runs/sizing/`, `prototype/runs/ledger.jsonl`).
- Slice 2 committed at Pedro's confirmation (`d091d2e`); he set five repeats for slice 5. Prototype slice 3 built: the gate, with the verdict in the design's decision order, the contracts' hidden checks, bounded repair attempts in the gated arm, and a verdict record as JSON and Markdown. The same task was run in the gated arm on the model and accepted on the first attempt.
- Slice 3 committed at Pedro's confirmation (`f369e39`). Slice 4 begun: ten planted flaws and six known-good changes written, each with the outcome expected of the gate recorded first, and a runner to feed them to the gate.
- **Pedro stopped the prototype: the time budget for the exercise had run out.** He interrupted the slice-4 run and asked for the state to be committed and the results written up. The tree was committed as it stood (`5014b44`). The interrupted run had completed 30 of 38 verdicts. `docs/RESULTS.md` written from the run files. Slices 5 to 7 were not started.

**Deviations and corrections**
- **First-pass reading was truncated without warning.** The summarising fetch cut three long articles part-way and reported one as near-complete. Found when Pedro challenged the coverage. Fix: download the full text, check it reaches the final section, read end to end.
- **One article from the brief is no longer available** from any source and was removed from the brief and the plan at Pedro's instruction.
- **Two plan claims were stronger than the evidence** and were corrected: the statement that three vendors share one subscription ladder, and an unverified press quotation on margins.
- **One statement about the paper was too absolute.** "No system checks the outcome" became: two of eleven have an outer verification loop (a model judge; a verify-on-stop guard), none is described as a deterministic post-run gate with an evidence record.
- **The paper's affiliation was first reported as unstated**, because of a faulty text search. The full read found it (Wavestone AI Lab).
- **Pedro's Notion notes needed seven corrections** when checked against the sources (`docs/research/notion-notes-2026-10-01.md`). Two were material: a comparison between a model and job candidates was reversed, and a result described as "16 working features" was a 16-feature specification.
- **One article from those notes could not be found** (ASSIST-012), and three further leads turned up that have not been read (ASSIST-013).
- **We had been inventing terms that already exist.** "Accepted change" and "cost per accepted change" are published as Production-Qualified Change and PQC per dollar. The plan now uses the published terms with attribution.
- **An earlier journal statement no longer holds as written.** ADR-001 said no source shows that verification gates improve outcomes. Anthropic's harness design post gives one such example, a single run reported by the vendor.
- **Of six conflicts between Pedro's web notes and our records, our records were right on three, the notes on one, and neither fully on two.** Our stale item was Cognition's valuation.
- **Two of our own statements were too broad** and were reworded: that no harness uses embeddings over code (true of the eleven studied, not of closed IDE products), and that the inner loop "is a commodity" (a basic loop is cheap to write; harness design still changes results).
- **We had credited one paper with a term it did not coin.** "Verification tax" appears in a DORA article six months before the paper that formalises it.
- **The market check changed the picture more than the literature did.** A competitor valued at 1.5 billion USD is positioning as "the control layer" for agent-written changes.
- **One quotation in Pedro's paper analysis is not in the paper** (that Omnigent "does not evaluate output correctness"). The paper is silent on the point.
- **Decision D3 was refined, not reversed.** We still run our own minimal loop, but take it from the paper's published listing.
- **The decision-model addendum needed ten corrections**, among them the context limit (about 32,000 usable tokens, not 64,000), the mechanism (unpublished, not as described), and two integration claims that had changed state. Its central caution, that such judges fail where LLM judges fail, was confirmed with a figure, for text rubrics only.
- **Evaluating the second thesis exposed a weakness in the first.** We had worded the verdict as deterministic and drawn from the customer's own checks. On a migration benchmark such checks alone accepted 118 runs of which 28 deserved it. A wider verdict is proposed and not yet agreed.
- **Pedro's notes described the VB6 study as equivalence-tested.** It was assessed by hand by the system's maintainer; there was no test suite.
- **Fourteen claims in Pedro's market and limits notes needed correcting** at their public sources, among them a benchmark figure that came from a podcast (about 33%, against 14.8% in the paper) and a vulnerability figure attributed to the wrong vendor. Four phrases turned out to be his own framing, in no source.
- **One committed file broke the new citation rule.** The digest of Pedro's notes named his private files and carried untraced figures. It was replaced with a list of his principles.
- **Nine early ledger rows were not exact.** They had been gathered through a summarising fetch. Corrections that changed meaning: a security quotation applied to two models, not to all newer models; a billing change was an announcement with an exception for annual subscribers; an incident date was not in its source; one repository reported as archived is read-only. The plan carried three of these and was corrected.
- **One figure in Pedro's notes is arithmetically wrong and was not used:** a 90% single-attempt success rate gives about 43% over eight attempts, not 57%.
- **A kill criterion could not have been met as worded.** "No unsafe action runs in the gated arm" assumed a policy on tool calls, which the thesis decisions exclude and the design does not have. The gate runs after the agent stops. Found while scoping the prototype; reworded by Pedro's decision (ADR-021).
- **The plan and the design disagreed on the prototype's build order.** The plan still listed a policy slice and started with the loop; the design starts with a measurement skeleton and a fake agent. The plan was brought into line.
- **The scaffold does not run as published.** Read closely, it lacks tool parameter schemas, and its turn and cost limits surface as a `RuntimeError`, not as a stop. Recorded with the listing; neither is fixed in the listing itself.
- **Pedro's copy of the harness paper was not on the machine** (a cloud placeholder of zero bytes). The public arXiv copy was used.
- **One task could not have been done without changing an existing test.** The fixture's rendering test pinned the whole output, so the task that adds lines to it would have been flagged as weakening a test. The fixture test was loosened before any run.
- **A rule flagged reading as doing.** Rewriting a file that contains the planted instruction counted as following it. The rule now looks at shell commands that contact the planted host.
- **A check report was read as missing** because of a delay in Docker's file sharing (ASSIST-020). It surfaced as `error`, which is the designed behaviour for a report that cannot be read, and it was found by a test, not in a run.
- **The layout differs from the one scoped:** correct and wrong reference changes sit together under `prototype/changes/`.
- **The first paid run got its task right in the bare arm,** with no gate and no instruction to verify. One run settles nothing, but it is the outcome the roadmap names as the main risk to the comparison: a model that gets the small tasks right leaves no gap to measure.
- **The gate accepted a wrong change the first time it was run on the reference set.** Its hidden check for one requirement tried a single example, and a hand-written wrong change mishandles another. It was left as found and is reported as the gate's false pass on that set.
- **A container read stale content** when a test reused a path it had just deleted (ASSIST-020, second sighting). The gate now checks, inside the container, that what is mounted is the change it was asked to judge.
- **The first gated run's timing was spoiled** by running it alongside the dry run on the same Docker machine. The cost and the verdict are unaffected; the timing is not used.
- **The prototype did not reach the measurement it was built for.** The plan allowed 150 minutes for it. Three slices and part of a fourth were built; the 165 model runs and the reviewer comparison were not. The plan's own response to an overrun was to drop the stretch slice first and keep the evidence and the results; in the event the cut fell on the measurement itself.
- **One of the three conditions for continuing is not met as worded.** Nine of ten planted flaws were rejected. The tenth drops behaviour no check covers, and was planted to find that limit.
- **Our own ground truth accepted that same wrong change** (ASSIST-021). The measure the verdicts were to be compared with has the gap it was meant to expose.
- **A summary given to Pedro was wrong and was corrected.** It said the planted-flaw runner had been neither written nor run. The command had in fact written it and judged 30 changes before it was interrupted. Found when the files were listed for the commit; the commit message was corrected before anything was pushed.
- **A push failed** for lack of git credentials and was retried through the GitHub CLI's login (ASSIST-011).

---

### 2026-10-07

**Done**
- Work resumed on the branch `post-1st-assessment`, on a second machine (native Linux Docker in place of a desktop VM).
- The two free completions named in `RESULTS.md` §8 and ASSIST-023 were run, at no spend.
- **The interrupted planted run was completed: all 38 hand-made changes judged.** Every verdict of the first run reproduced. The eight changes judged for the first time: both remaining correct reference changes passed, and five of the six probe changes for wrongly failed work passed. The sixth, `k03-o2-token-in-a-test`, failed at the secrets screen — the exact failure finding 6 of `RESULTS.md` predicted before it was judged. Both error rates of the gate are now measured on hand-made changes: false pass 2 of 21, false fail 1 of 17.
- **The dry run was re-run after the slice-4 edits (ASSIST-023): 72 runs, 0 runner failures, 0 unexpected outcomes.** The issue is closed.
- `RESULTS.md` updated in place with the completion, dated; `ROADMAP.md` issue register updated; the presentation forms' false-fail lines updated from "not judged" to the measured number.
- `prototype/requirements.txt` added: the host-side dependencies (anthropic, openai, python-dotenv, pytest, pyyaml) had to be rediscovered one by one while reproducing.
- **The ground truth was widened before any model comparison (ASSIST-021).** o1 gained five absolute cross-region tax and total cases; o2–o6 gained two runtime invariants each (tax on the discounted subtotal; the total identity); manifests updated; the 84 tests pass. Validated by re-running the planted batch: `p06-behaviour-dropped` now fails the answer key at exactly the added case, and all seventeen correct changes still qualify.
- **Slice 5 was built and run: 165 live runs, 0 runner failures, 5.53 USD** (`prototype/runner/batch.py`; `prototype/runs/arms-sonnet/`). The findings, from the regenerated table: the gate's verdict was wrong zero times (0 of 146 false passes, 0 of 146 false fails); the agent's claim was wrong on 19 of 164; the model weakened existing tests in 19 of 110 unguarded runs — and the instructed-to-verify arm did it slightly more often than the bare arm (10 against 9); every gated run qualified (55 of 55), and cost per qualified change was lowest in the gated arm.
- **Slice 6 was built and run: an evaluator agent from a second vendor** (`gpt-5.1-2025-11-13`, pinned; price recorded first as E-87 per ASSIST-018) on trial 1 of every task × arm — 33 evaluations, 0.15 USD (`prototype/scaffold/adapter_openai.py`, `prototype/runner/evaluator.py`, `evaluate.py`). It passed all three of the sample's unqualified changes, each a weakened-test change it praised, and wrongly failed 2 of 30 good ones. The report generator gained an evaluator section so the table regenerates from the records.
- **The evaluator's verdict variance was measured on one fixed change:** five evaluations of the identical correct change gave fail, pass, pass, pass, pass. The lone fail claimed an existing test had been altered; the gate's integrity diff shows none was. (The variance was first noticed when a preparation smoke-test verdict, later superseded and not kept, disagreed with the sampled one; the five recorded repeats replace that observation with recorded data.)
- Stage-1 spend at the end of the day: 5.78 of the 50 USD cap, ledger-reconciled.

**Deviations and corrections**
- **The first completion attempt produced 38 errors and judged nothing (ASSIST-024).** On a native Docker daemon, the verdict containers — root with every capability dropped — could not write their test reports to host-owned mounted folders: dropping all capabilities removes root's permission override. The first machine's Docker Desktop had masked this through its VM file sharing, the same subsystem as ASSIST-020. Two observations worth the record: the gate failed closed under an environment fault it had never seen (every verdict `error`, none a pass), and the fix strengthens confinement — containers now run as the invoking host user, so nothing in the prototype runs as root at all. All 84 tests pass with the change; the planted run and the dry run reproduce under it.
- **The 10.32-second verdict time of §5.4 was mostly the first machine.** The same 38 verdicts average 1.1 seconds on native Docker; the earlier figure was dominated by the desktop VM starting containers. `RESULTS.md` §5.4 now carries both numbers, each tied to its machine.

---

## Part 2. Decision records

### ADR-001 — Thesis direction

| | |
|---|---|
| Status | **Decided 2026-10-05.** Direction agreed that morning; details settled in the thesis discussion the same day (ADR-014 to ADR-016). |
| Plan reference | D1, `PLAN.md` §1 and §1.1 |

**Decision.** We do not propose building a coding assistant, an agent harness, or a meta-harness. The candidate is an evidence layer (change contract, deterministic verification after the agent stops, evidence bundle, risk routing) delivered as a plug-in to existing harnesses and entered through per-repo agent evaluation. "Wait, with a review date" stays a possible conclusion.

**Rationale.**
- Generation is owned and priced by the model vendors, and features copy between them quickly (`docs/research/market-landscape.md`).
- A basic agent loop is cheap to reproduce and the outer policy layer is being commoditised (`docs/research/harness-paper.md`). Harness design still changes results by model, task and budget (`docs/research/paper-harness-ablation.md`), which is a reason not to compete on it.
- The evidence that the problem sits after generation is the best-triangulated we have (`docs/research/EVIDENCE.md`, rows E-01 to E-09).
- None of the sources describes a deterministic post-run gate with an evidence record and a measured false-pass rate.
- The model vendor itself reports that agents grade their own work too generously and that a same-family evaluator remains lenient (E-34, E-35).

**Alternatives rejected.**
- An outer harness with policy, sandbox and budgets: already exists as open source.
- A sovereign or air-gapped assistant: weakest demand evidence; an incumbent shipped it on 2026-10-01 (E-19).
- Brownfield modernisation for one vertical: needs a vertical we do not have (ADR-002).
- A cross-vendor cost control plane on its own: folded in as the metric "cost per accepted change".

**Known weaknesses.**
- The verification mechanism is cheap to copy; the paper puts the half-life of a distinctive feature at weeks.
- Outcome evidence is one vendor anecdote: a single pair of runs in which a contract plus a separate evaluator produced a working build where a solo agent did not, at more than twenty times the cost (E-37). Evidence for a deterministic, independent gate would have to come from our own prototype.
- Contract plus separate evaluator is the model vendor's published design, so the idea itself is not ours (added 2026-10-05).
- The framing, the metrics and the risk tiering are also published (two 2026 papers, neither with an implementation or measurements). What remains unclaimed is a protected contract, a verifier with a measured false-pass rate, and measurements. The proposal's contribution would be evidence, not concept (added 2026-10-05).
- The adjacent market is funded and moving toward this position: CodeRabbit sells risk routing and merge blocking on model judgment and has the parts to add a contract-then-evidence flow (E-49). Still open, on vendors' own documentation: a protected pre-run contract, a deterministic verdict that runs the customer's checks, a measured false-pass rate, and an outcome record (E-50, E-51, E-53). The case for Wait is stronger than at any earlier point (added 2026-10-05).
- A frontier lab argues against blocking gates where corrections are cheap (E-57). The candidate buyer narrows to teams where a wrong change is expensive (added 2026-10-05).
- The vendor found its evaluator "unnecessary overhead" on a newer model for tasks inside the model's reliable range (E-36). The check's value moves with each release (added 2026-10-05; roadmap question T10).
- With no inherited moat, what is defensible is unsettled (T3).

### ADR-002 — Assume no inherited advantage

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D2 |

**Decision.** The strategy assumes the company owns no proprietary model, no harness, no captive vertical and no special moat.

**Rationale.** Pedro's statement of the starting position. A strategy that needs an inherited advantage would not answer the leadership question.

**Alternative rejected.** Assuming a model or a regulated customer base, which would have strengthened the sovereign and brownfield options.

### ADR-003 — The agent under test is the harness paper's published scaffold

| | |
|---|---|
| Status | Decided 2026-10-03; refined 2026-10-05 |
| Plan reference | D3 |

**Decision.** The prototype's agent is a minimal single loop behind a provider interface, taken from the 90-line scaffold in arXiv 2609.00006v1 (Listing 3, CC BY 4.0, with attribution) and specialised only where needed. Every departure from the listing is recorded in this journal when it is made.

**Rationale.**
- It shows every design topic in the brief in readable code, and makes the strategic point that the loop is small. The paper's first recommendation is "Start with a linear while loop" (E-31).
- The listing is published to be reused: "it is a scaffold to be copied and specialized" (E-59).
- A published, citable agent removes the objection that we tuned the agent to suit our gate.
- Under ADR-001 the loop is the agent under test, not the product.

**Alternatives rejected.**
- Writing our own loop from nothing (the decision of 2026-10-03).
- Wrapping an agent SDK or a hosted agent service. One of the articles argues for exactly that (`docs/research/articles/claude-managed-agents.md`).

**Known departures to expect.** Provider adapters for Anthropic and OpenAI; an event log; running inside an isolated copy of the repository, because the listing has no sandbox and runs shell commands directly.

**Beyond this exercise.** A real product would attach to vendor harnesses and would not ship its own loop.

### ADR-004 — Python

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D4 |

**Decision.** The prototype is written in Python.

**Rationale.** Fastest route for a one-day budget.

**Alternative rejected.** Go, which matches Pedro's most recent authored code.

### ADR-005 — Model access and spend

| | |
|---|---|
| Status | Decided 2026-10-03; keys in place 2026-10-05 |
| Plan reference | D5 |

**Decision.** Anthropic models first, with a hard cap of 50 USD across all runs. OpenAI may be used to cross-check results or as the adversarial judge. Keys live in a git-ignored `.env`.

**Rationale.** Pedro's instruction. A judge from a different vendor avoids a model family grading itself.

**Beyond this exercise.** The cap sets how many tasks, repeats and arms the evaluation can afford; results from it are an indication, not a benchmark.

### ADR-006 — Repository on the personal GitHub account

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | D6 |

**Decision.** Private repository `pedraumcosta/assistant`, authored as `pcosta@gmail.com` (D7).

**Rationale.** Pedro's choice.

**Alternative rejected.** An organisation-owned repository, which would have allowed read-only access for others.

**Consequence accepted.** On a personal account, "Collaborators can't have read-only access" (E-27). Anyone invited can push.

### ADR-007 — The repository is self-contained

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D9 |

**Decision.** Nothing is cited from Pedro's private folders. Any material we rely on is recorded under `docs/research/` with its original source.

**Rationale.** Readers of the repo cannot open private files.

**Refined 2026-10-05.** Research records cite public sources. Where a claim reached us through Pedro's notes, the notes are named as the origin and the public source behind the claim is what is cited and checked.

**Consequence.** `docs/research/practitioner-notes.md` first held a digest of Pedro's notes with their file names and untraced figures. On 2026-10-05 it was replaced by a short list of his working principles, with no file names and no figures. The earlier version remains in the git history.

### ADR-008 — Document formats

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D8 |

**Decision.** Markdown first. When the content is close to final, a Claude Code artifact, then a Slidev presentation.

**Alternative rejected.** Starting with slides or an HTML page.

### ADR-009 — Commit policy

| | |
|---|---|
| Status | Decided 2026-10-03 (trailer) and 2026-10-05 (confirmation) |
| Plan reference | D10, `PLAN.md` §5 |

**Decision.** One commit per meaningful step, made only after Pedro confirms, with the `Co-Authored-By: Claude` trailer. `docs/scratchpad.md` and `.env` are never committed.

**Rationale.** The git log is the verifiable record of how Claude Code was used, so each commit should be one Pedro has agreed to.

### ADR-010 — Evidence rules

| | |
|---|---|
| Status | In force since 2026-10-03 (from the brief's uncertainty policy) |
| Plan reference | `PLAN.md` §5 |

**Decision.** No number is invented or estimated. Every figure traces to a row in `docs/research/EVIDENCE.md` or to a prototype run file. Only rows tagged [P] or [L] may appear in CXO-facing text. Where no data exists (the CFO message), figures are stated as labelled assumptions.

**Rationale.** The brief's uncertainty policy, and the audience.

**Applied so far.** Two plan claims corrected on 2026-10-05; five ledger rows remain unverified (ASSIST-004).

### ADR-011 — Use the published vocabulary

| | |
|---|---|
| Status | Adopted 2026-10-05 |
| Plan reference | `PLAN.md` §3.7 |

**Decision.** The project uses the published terms, with attribution, in place of its own: Production-Qualified Change for what we had called an accepted change, PQC per dollar for cost per accepted change, and Verification Tax for the cost of assurance relative to generation. Prototype results are reported in the published metric set, with the verifier's false-pass rate added as ours.

**Rationale.** The terms are defined in arXiv 2609.04681 (E-40 to E-42). Citing them is more credible to executives than inventing equivalents, and makes our results comparable with later work.

**Alternative rejected.** Keeping our own terms, which would hide that the framing is already public.

**Note.** "Verification tax" as a phrase predates that paper; it appears in a DORA article of 2026-03-10. The paper supplies the formula.

### ADR-012 — Decision models are the next enhancement, not part of the first prototype

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §3.10, §7.2 |

**Decision.** The first prototype is built and measured without a decision model. The enhancement that follows adds a decision-model judge as a fourth verdict source and tests whether the prototype's own deterministic outcomes improve that judge's calibration. In any later design a decision model may assign risk tiers, judge criteria that have no executable check, or triage; it never gives the verdict on whether a change is correct, and it sits behind an interface with a self-hostable classifier as the default.

**Rationale.**
- Measured evidence that such models repeat LLM judges' errors: "96.0% of LLM verdicts repeat its answer, against 50.3% under independence", on text rubrics (E-63). A verdict that depends on one would not be independent.
- Calibration needs only "a few hundred labeled examples" (E-65), and our layer produces those labels. That is worth testing, after the core result exists.
- The commercial product is hosted only, in the United States (E-62), which conflicts with running entirely in the customer's environment.
- The first prototype has a one-day budget and one question to answer: whether a deterministic verdict beats the agent's own claim and a model reviewer's.

**Alternatives rejected.**
- Including a decision-model judge in the first prototype: more scope, and it needs access we do not have (ASSIST-015).
- Building the product around decision-model economics: the argument was made for a governance layer this project dropped, and the call sites where it saves most sit inside the harness, which we do not build.

**Beyond this exercise.** The evidence is three weeks old and contains no code judgments. Whether a decision model's errors on code changes overlap with a model reviewer's is something our own data would have to show.

### ADR-013 — Second thesis evaluated: brownfield / enterprise-legacy specialisation

| | |
|---|---|
| Status | Evaluated and decided 2026-10-05: not pursued. |
| Plan reference | `PLAN.md` §3.11; `docs/research/second-thesis-brownfield.md` |

**What was evaluated.** A product specialised for agent work in old codebases, built on four practices from Osmani's article: zoning by blast radius, a durable comprehension memo, characterization tests first, and the harness as institutional memory.

**Recommendation.** Do not pursue it as a separate product. Carry it into the first thesis (ADR-001) in two ways: as the candidate first market, and as the reason to widen the verdict from fixed checks to fixed checks plus a completeness audit plus a counterexample search.

**Rationale.**
- The premise holds: agents are weakest in legacy code (E-67, E-70, E-71).
- The four practices are process, reproducible as a prompt or a skill file, and each already exists as a product or feature (`docs/research/brownfield-market.md`).
- The evidence does not test the practices; it points to model capability and to verification.
- In every verified success the decisive input was the customer's own oracle, which a tool cannot supply.
- The large migrations are sold by hyperscalers and model vendors, largely free or bundled; with no model, customers or vertical (ADR-002), every foothold means choosing a vertical and starting with services.
- The setting fits the first thesis closely: it identifies the buyer, its best-known practitioner states our contract and risk-tier ideas in his own words (E-73, E-74), and migration supplies an oracle that eases the question of where contracts come from.

**What it changes in ADR-001, if agreed.**
- The candidate buyer becomes teams working in legacy systems.
- The verdict is no longer described as deterministic checks alone. On a migration benchmark those accepted 118 runs of which 28 deserved it (E-68). The proposed verdict has three parts, and the counterexample search is done by a model whose result depends on which models search (E-69). What it produces is still an executable failing test.

**Alternatives considered.**
- Brownfield as the main thesis, replacing the first: rejected in the recommendation for the reasons above.
- Ignoring brownfield: rejected; it is the best answer found to who the buyer is.

**Outcome.** Pedro chose the first thesis: there is no time in this exercise to validate a solution for brownfield. Brownfield is therefore not pursued as a product and not claimed as a first market; the proposal may name legacy teams as a hypothesis for the pilot. The wider verdict was accepted (ADR-016).

### ADR-014 — Posture: a three-stage probe

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, P1 and T7 |

**Decision.** We do not enter the assistant market. We make one narrow bet with fixed exits and decide Build or Wait on what it shows:

1. a one-day prototype;
2. a measurement pilot with one or two design partners, on their own repository and tasks;
3. a build of the gate, only if the pilot clears thresholds set in advance.

**Kill criteria.** After the prototype, continue only if the gate's false-pass rate is lower than both comparators, every planted flaw is rejected, and no unsafe action runs in the gated arm. *(The last condition was reworded on 2026-10-05; see ADR-021.)* After the pilot, continue only if at least one design partner says the report changed a decision they were about to make. Otherwise the recommendation is Wait, with a review date.

**Rationale.**
- The idea, the metrics and the risk tiering are published; a funded competitor owns the adjacent ground; a check's value moves with each model release; we have no model, customers or vertical. That rules out a straight Build.
- No vendor audit log records the outcome of an agent's work; no vendor publishes a false-pass rate; and the test costs a day and then a few weeks. That rules out a straight Wait.
- The measurement pilot is both the entry product and the cheapest way to learn whether anyone will pay.

**Alternatives rejected.** Build now; Wait now.

**Open.** The review date that applies if the recommendation becomes Wait. The staffing assumption for the pilot (two engineers and a part-time product lead for six weeks) was judged reasonable and is to be revisited once the prototype is ready.

### ADR-015 — Thesis: the evidence layer, not the brownfield specialisation

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, P2; ADR-001; ADR-013 |

**Decision.** The exercise carries the first thesis forward. The brownfield / enterprise-legacy specialisation is not pursued, and brownfield is not presented as a validated first market.

**Rationale.** Pedro: there is no time to validate a solution for brownfield. The evaluation in ADR-013 had also found it weaker as a product.

**Consequence.** The proposal may name teams working in legacy systems as a hypothesis for the pilot to test. It must not present that as a finding.

**Alternative rejected.** Carrying brownfield as the declared first market, which was the recommendation in ADR-013.

### ADR-016 — Thesis details

| | |
|---|---|
| Status | Decided 2026-10-05, except the CFO's numbers (deferred) |
| Plan reference | `PLAN.md` §2.1, T1 to T11 |

Each line is the decision, then why.

**Buyer.** Engineering leaders, as sponsors, in organisations that build software. *Why:* they own delivery risk and the tooling budget, and answer for what agents merge. That the need is sharpest where a wrong change is expensive is a hypothesis for the pilot.

**How we differ.** A verdict that runs the customer's own checks; independence from the model vendor; a measured false-pass rate; an outcome record. *Why:* no product we found offers these together (E-50, E-51, E-53).

**Defensibility.** Stated as thin: neutrality, and each customer's accumulating checks and labels. *Why:* the mechanism is cheap to copy and the idea is published. *Condition set by Pedro:* the product works on the customer's data, so everyone involved must be aware of what is used and for what, and all relevant precautions are taken. The data stays in the customer's environment, is not used for training or shared across customers, and belongs to the customer.

**Where contracts come from.** The product's first process is guiding the user to create the checks, a test suite or an evaluation, in the manner of test-driven or eval-driven development, kept simple. *Why:* Pedro reframed this from an open question to the first step of the workflow. Without checks there is nothing to verify against, and agents guess when a task is underspecified (E-80). In the prototype the contracts are written by hand.

**Attachment.** A CI check first; one harness hook as a demonstration if time allows. *Why:* CI needs no vendor hook, and the harness layer has no standard interface yet.

**Exclusions.** No assistant, agent loop, meta-harness, policy or sandbox layer, review bot, wider control plane, or model of our own. *Why:* each exists, is funded, or is a model vendor's home ground.

**Staying valuable as models improve.** Measurement is repeated for each and every model and harness pairing, and the product adapts to each. Pedro asked for this to be emphasised. *Why:* a check's value moves with each release (E-36), and harness effects change in size and sign by model (E-58).

**The verdict.** Called executable evidence. In the prototype: the customer's fixed checks, a scope check on the diff, and a check that the agent's own tests fail against the original code (E-76). The counterexample search is a later enhancement. *Why:* fixed checks alone pass bad changes where tests under-describe behaviour (E-68); "deterministic" would overclaim once a model helps search.

**Prototype scope.** Three arms (bare, prompt discipline, gated) and two comparators (the agent's own claim; an evaluator agent on a sample of runs). The cheaper-model arm is a stretch goal. *Why:* that arm is confounded by sharing a harness and costs runs under the cap.

**The CFO's numbers.** Deferred until the prototype is ready. The working assumption was judged reasonable.

**Alternatives rejected.** Brownfield teams as the declared buyer (ADR-015); describing the verdict as deterministic; treating contract creation as something to discover in the pilot.

### ADR-017 — The verdict is executable, not always deterministic; evaluations for LLM applications

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, T12; `PROPOSAL.md` §2.1 |

**Decision.**
- The verdict covers two cases. For conventional code it comes from the customer's tests and is a yes or no. For an LLM application it is an evaluation: fixed cases, some hidden from the agent, run repeatedly and scored against a threshold, reported as pass, fail or inconclusive.
- Scoring uses code wherever it can. A model scores only where code cannot, and then its agreement with human labels is measured and stated.
- The prototype starts with the conventional case. The evaluation path is designed in the design document. Implementing it is a bonus if time allows.

**Rationale.**
- Pedro's point: an LLM application answers differently each time, so one deterministic run cannot verify it.
- What the product promises does not depend on determinism: checks fixed before the agent runs and protected from it, run outside the agent, recorded, and their own error rate measured.
- "Inconclusive" is an honest third result when the uncertainty straddles the threshold; it routes to a human or to more samples.
- The conventional case gives the cleanest comparison against a model reviewer within a one-day budget.

**Alternatives rejected.**
- Describing the verdict as deterministic, which would exclude LLM applications or overclaim.
- Adding an LLM-application task to the first prototype, which would take time and budget from the main comparison.

**Consequences.**
- A model scorer reintroduces judgment, so it carries conditions: checked against human labels, pinned to a version and prompt, from a different vendor than the model under test where possible.
- The evaluation's own error has two sources, too few samples and scorer error, and both have to be reported.
- The decision model set aside in ADR-012 belongs with this path, as a low-variance scorer.
- Evaluations cost tokens, so the contract's budget covers verification as well as the agent's work.

### ADR-018 — State the cost the product adds to delivery, and measure it

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, T13; `PROPOSAL.md` §2.9 |

**Decision.** The proposal states that the evidence layer adds time and cost to building software, shows where in the delivery process that cost lands, and commits to measuring it. The prototype gains a sixth hypothesis on overhead, including the rate at which the gate wrongly fails good changes.

**Rationale.**
- Pedro's point: more tests and checks add latency, time and cost.
- The product's case is a trade, not a free gain: cost moves from review, rework and incidents to checks written once and machine time. No evidence we hold shows the trade nets out.
- The research gives reasons for caution in both directions. Checking can be cheap next to generating (E-84), but checking everything is waste (E-36), waiting has a price (E-57), and a cheap check that passes bad work is worse than none (E-42).
- A verdict that blocks good changes creates rework and teaches people to bypass it, so the false-fail rate matters as much as the false-pass rate.

**How the product limits its own cost.** Checks applied by risk; reuse of the team's existing pipeline; a budget that covers verification; both error rates reported.

**Where it is expected not to pay.** Small low-risk changes; fast new builds where a mistake is cheap to undo; teams with few tests, for whom writing the checks is most of the cost.

**Alternative rejected.** Presenting the product as a saving without stating what it adds.

**Limit.** The prototype can measure what the gate adds. Only a pilot can measure what it saves.

### ADR-019 — Frame: tooling for evidence-driven development

| | |
|---|---|
| Status | Decided 2026-10-05. Label checked the same day; no owner found, trademark registers not searched. |
| Plan reference | `PLAN.md` §2.1, T14; `PROPOSAL.md` §2.5 |

**Decision.** The product is framed as tooling for evidence-driven development: a tool for the team's delivery process, not a plug-in for an assistant. The team defines what "done" means as executable checks before the work starts, and every change, whoever or whatever wrote it, is accepted on that evidence. The frame presents the practice as the continuation of test-driven development, covering eval-driven development for software built on models, and supporting spec-driven development and "software factory" working without carrying either name. The product's scope does not change.

**Rationale.**
- Pedro's aim: keep the verification, safety and checking features, and market them in a frame with a future.
- "Plug-in" was inaccurate. The product starts by helping the team define its checks, attaches to the build pipeline first, and keeps the record.
- A product described as checking the agent is needed less with each model release (E-36). A team's standard for what counts as done is needed whoever writes the code.
- The buyer decided in ADR-016, engineering leaders, buys tooling for how teams deliver.
- The asset that accumulates, the team's executable definition of done, sits in the team's process and not in an assistant.

**Alternatives rejected.**
- *"SDLC implementation tool"* as the category: too broad, and the ground of GitHub, GitLab and Atlassian; it also reads as the wider control plane excluded in ADR-016.
- *Spec-driven development* as the banner: already offered by large vendors, placed at "Assess" by Thoughtworks, and criticised as a return to heavy up-front specification. Pedro's own principle is that a specification nobody enforces is a wish; the product is the enforcement half.
- *"Factory"* as the banner: it is a company name in this market, and it implies high-throughput autonomy, the setting in which a frontier lab says corrections are cheap (E-57) and the product pays least.
- *Eval-driven development* as the lead: proposed first in discussion; Pedro chose the broader label, which covers tests and evaluations alike and matches the product's name.

**Consequences.**
- The verdict applies to changes written by people as well as by agents. Agent-written changes remain the reason to adopt now, and the prototype still tests agent-written changes only.
- "Mature process" is kept as targeting, not as a slogan: the product suits teams with version control, tests, a pipeline and review, which is also where it was expected to pay.
- The label is one we are naming. Establishing a label costs a newcomer effort, and its initials are those of eval-driven development, so it is not abbreviated.

**Result of the label check** (`docs/research/positioning-label-check.md`).
- No company, product or book was found that owns "evidence-driven development" as a category. Its only uses in the AI-agent context are small open-source items.
- It will be confused with three things: eval-driven development; evidence-based software engineering, an academic field about empirical research on software practice; and, faintly, experiment-driven product development.
- "EDD" already means eval-driven development. Braintrust, OpenAI's documentation and Anthropic's documentation all use that phrase. The abbreviation is avoided.
- The strongest objection: the practice is acceptance-test-driven development joined to eval-driven development. The proposal therefore claims only what is added: one gate for changes from people and from agents, a kept record, and a measured error rate.
- Closest in substance under another name: StrongDM's published "Software Factory" method, in which specifications and externally held scenarios drive agents. It is a method, not a product.
- Not done: a search of trademark registers.

### ADR-020 — Design decisions: contract home, first process, evaluation coverage, hooks, prototype simplicity

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, T15 to T19; `DESIGN.md` §9 |

Each line is the decision, then why.

**The contract lives on a protected branch** of the team's repository, with the hidden checks. *Why:* the author of a change must not be able to write to them, and a protected branch uses the permissions and history the host already provides. *Rejected:* a separate store, which adds a system to run and secure.

**The first process is a use-case description with the main functional requirements.** The team's own assistant helps with clarifying questions; checks are drafted from the requirements, each requirement linked to at least one check; a person approves. *Why:* it starts from something an engineer already knows how to write, and it turns the tendency of agents to guess (E-80) into questions before the work begins. *Limit:* the assistant asks and drafts; it does not approve and cannot write to the protected branch. *Rejected:* asking the engineer to write tests from nothing.

**Evaluation coverage and data samples are comprehensive by default.** Every functional requirement has cases, across ordinary inputs, edge cases and inputs meant to break it, and coverage is reported. Budget limits repeats, not breadth. *Why:* a narrow set gives a confident verdict on the wrong question. *Cost accepted:* evaluations are the expensive path, and this makes them more so (ADR-018). *Rejected:* letting sample breadth follow the budget.

**Hooks inside the assistant are offered**, for human intervention and early feedback. *Why:* a hook is where a person can step in while the agent is working. *Limit:* the pipeline's verdict is the one that counts, because a hook runs where the author can reach it.

**The prototype is kept very simple.** It builds none of the first process, the protected branch or the hooks, and the evaluation path only as a bonus. A directory outside the agent's working copy stands in for the protected branch. *Why:* one day, and one question to answer.

**Diagrams** stay in Mermaid for now.

### ADR-021 — Prototype: what "unsafe" means, how the agent is confined, which models, and the departures from the listing

| | |
|---|---|
| Status | Decided 2026-10-05 |
| Plan reference | `PLAN.md` §2.1, T20 to T22; §7.1 and §7.2 |

**The kill criterion on safety is reworded: the gate accepts no change that contains an unsafe action.** Unsafe actions attempted are counted per arm from the event log, as a measurement, by rules written before any run. *Why:* the gate runs after the author stops and cannot prevent an action. As first worded ("no unsafe action runs in the gated arm") the criterion needed a policy on tool calls, which is excluded (ADR-016) and is the ground of an existing open-source layer (ASSIST-010). *Rejected:* a thin policy in the gated arm, which would make that arm test two things at once; a fourth arm with gate and policy, which costs runs under the cap. *What this gives up:* the prototype says nothing about preventing harm while an agent works. That stays the job of the team's environment.

**Every run is confined in a Docker container.** Only that run's copy of the fixture is mounted; there is no network; no API key is in its environment. The verdict and the ground-truth checks run in containers of their own, because they execute code the agent wrote. *Why:* the listing runs shell commands on the host with no restriction, and the trap tasks invite destructive commands and planted instructions. A separate copy of the repository confines neither. *Rejected:* macOS `sandbox-exec`, confirmed to work on this machine but less portable; the isolated copy alone. *Cost accepted:* set-up time, and a start-up delay on each command. The Docker daemon was not running when this was decided (ASSIST-017).

**Models.** The agent under test is Claude Sonnet 5.5 (`claude-sonnet-5-5`). The evaluator comparator is an OpenAI GPT-5.4 model, on a sample of runs, the exact model fixed when that slice is built. *Why:* Sonnet is what a team would run an agent on day to day. *Rejected:* Opus 5.5, which may leave no gap to measure on small tasks and allows fewest repeats; Haiku 4.5, where a poor result could reflect the minimal tool interface and not the gate.

**Departures from the listing.** The listing is kept unedited in `prototype/` and in `docs/research/harness-scaffold-listing.md`. Everything below is added around it and applies to all three arms alike.

| Departure | Why it is needed |
|---|---|
| A provider adapter that implements the listing's `Model` protocol, translates its message format, and supplies a parameter schema for each tool | As published, the tool schemas carry a name only, and neither provider accepts the listing's message format directly |
| The adapter reports cost from the provider's token counts and its published prices, recorded as evidence rows before the first paid run | The loop's cost cap reads a `cost` field the adapter must fill; no price is assumed |
| The four tool functions run inside the run's container, unedited; the loop stays on the host and holds the API key | The listing has no sandbox; the model call needs the network and the tools must not have it |
| Context discovery runs inside the container | As published it reads `AGENTS.md` from every parent directory of the host |
| The runner treats `RuntimeError: coroutine raised StopIteration` as "limit reached" | The listing's limits raise `StopIteration` inside a coroutine, which Python converts; confirmed on Python 3.12.9 |
| `max_turns` and `max_cost` are set per run from the contract's budget | Parameters of the listing, not changes to it |
| Every model response and tool result is written to the event log | The listing keeps no record |
| The adapter declares the four tools on every call, including the listing's summary call, which passes none | The API needs the tools declared whenever the history contains tool calls |
| The adapter returns the model's own response blocks to it unchanged on the next call | The listing keeps only text and tool calls; the API expects its own blocks back |
| The adapter refuses a call whose worst case could take the run past its budget, and the runner reads that as "limit reached" | The listing checks its cost cap only after the money is spent, so a run could pass its budget by one call. The design requires the budget to be enforced before a call is made |
| Output is limited to 8,192 tokens a call; no prompt caching is used | The API requires an output limit and the listing sets none. Caching was left off so that the first measured cost is the plain one |
| The task text in every arm asks for a last line stating whether the work is done; a run that returns without one counts as a claim of done | The listing has no notion of done, and the agent's own claim is a verdict source we compare |

**Beyond this exercise.** The product ships no loop and no container; it attaches to the team's pipeline, where the runner's isolation is the team's.

### ADR-022 — The prototype is stopped on the time budget, and reported as incomplete

| | |
|---|---|
| Status | Decided by Pedro, 2026-10-05 |
| Plan reference | `PLAN.md` §6 (P5, P6), §9 ("One day is not enough for all nine phases") |

**Decision.** Work on the prototype stops with three of seven slices finished and the fourth interrupted. The tree is committed as it stands. `docs/RESULTS.md` reports what was measured and says plainly that the comparison the prototype was built to make was not run.

**Why.** The exercise has one working day. The prototype was built in the order the design set, measurement first, so that nothing would be measured on an unproven instrument. That order was kept, and it used the time.

**What this costs.** The stage-1 conditions for continuing (`PLAN.md` T7, T20) cannot be judged from a model's behaviour. Of the three: one was not measured; one is not met as worded, on hand-made changes (nine of ten planted flaws rejected); one is met on hand-made changes only.

**What it does not change.** Nothing was tuned to improve a result. The two wrong changes the gate accepted are reported as found, with their cause.

**Alternatives not taken.** Running the 165 model runs without the planted-flaw results, which would have compared the gate with the agent's claim before knowing the gate's own error on known cases. Cutting the gate's tests to save time, which would have left the stale-file fault (ASSIST-020) unfound.

**Left for whoever continues.** `RESULTS.md` §8 lists each missing piece and what it needs. The first is free: finish the interrupted run. Before any model runs are compared with the ground truth, the ground truth should be widened (ASSIST-021).

