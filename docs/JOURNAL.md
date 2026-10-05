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
- **A push failed** for lack of git credentials and was retried through the GitHub CLI's login (ASSIST-011).

---

## Part 2. Decision records

### ADR-001 — Thesis direction

| | |
|---|---|
| Status | **Direction agreed 2026-10-05. Details open** (`ROADMAP.md` §2, questions T1 to T10). Not final. |
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

**Consequence.** `docs/research/practitioner-notes.md` is a digest with private paths removed; its figures are not usable until traced to a primary source.

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
