# JOURNAL — ASSIST

| | |
|---|---|
| Status | **Draft for Pedro's review.** Records only what has happened and what has been decided. |
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

**Deviations and corrections**
- **First-pass reading was truncated without warning.** The summarising fetch cut three long articles part-way and reported one as near-complete. Found when Pedro challenged the coverage. Fix: download the full text, check it reaches the final section, read end to end.
- **One article from the brief is no longer available** from any source and was removed from the brief and the plan at Pedro's instruction.
- **Two plan claims were stronger than the evidence** and were corrected: the statement that three vendors share one subscription ladder, and an unverified press quotation on margins.
- **One statement about the paper was too absolute.** "No system checks the outcome" became: two of eleven have an outer verification loop (a model judge; a verify-on-stop guard), none is described as a deterministic post-run gate with an evidence record.
- **The paper's affiliation was first reported as unstated**, because of a faulty text search. The full read found it (Wavestone AI Lab).
- **A push failed** for lack of git credentials and was retried through the GitHub CLI's login (ASSIST-011).

---

## Part 2. Decision records

### ADR-001 — Thesis direction

| | |
|---|---|
| Status | **Direction agreed 2026-10-05. Details open** (`ROADMAP.md` §2, questions T1 to T9). Not final. |
| Plan reference | D1, `PLAN.md` §1 and §1.1 |

**Decision.** We do not propose building a coding assistant, an agent harness, or a meta-harness. The candidate is an evidence layer (change contract, deterministic verification after the agent stops, evidence bundle, risk routing) delivered as a plug-in to existing harnesses and entered through per-repo agent evaluation. "Wait, with a review date" stays a possible conclusion.

**Rationale.**
- Generation is owned and priced by the model vendors, and features copy between them quickly (`docs/research/market-landscape.md`).
- The inner loop is a commodity and the outer policy layer is being commoditised (`docs/research/harness-paper.md`).
- The evidence that the problem sits after generation is the best-triangulated we have (`docs/research/EVIDENCE.md`, rows E-01 to E-09).
- None of the sources describes a deterministic post-run gate with an evidence record and a measured false-pass rate.

**Alternatives rejected.**
- An outer harness with policy, sandbox and budgets: already exists as open source.
- A sovereign or air-gapped assistant: weakest demand evidence; an incumbent shipped it on 2026-10-01 (E-19).
- Brownfield modernisation for one vertical: needs a vertical we do not have (ADR-002).
- A cross-vendor cost control plane on its own: folded in as the metric "cost per accepted change".

**Known weaknesses.**
- The verification mechanism is cheap to copy; the paper puts the half-life of a distinctive feature at weeks.
- No source shows that verification gates improve outcomes. That evidence would have to come from our own prototype.
- With no inherited moat, what is defensible is unsettled (T3).

### ADR-002 — Assume no inherited advantage

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D2 |

**Decision.** The strategy assumes the company owns no proprietary model, no harness, no captive vertical and no special moat.

**Rationale.** Pedro's statement of the starting position. A strategy that needs an inherited advantage would not answer the leadership question.

**Alternative rejected.** Assuming a model or a regulated customer base, which would have strengthened the sovereign and brownfield options.

### ADR-003 — The prototype uses its own minimal agent loop

| | |
|---|---|
| Status | Decided 2026-10-03 |
| Plan reference | D3 |

**Decision.** Write a minimal single agent loop ourselves, behind a provider interface.

**Rationale.** It shows every design topic in the brief in readable code, and it makes the strategic point that the loop is small. The paper's first recommendation is "Start with a linear while loop" and it includes a 90-line scaffold (E-31). Under ADR-001 the loop is the agent under test, not the product.

**Alternative rejected.** Wrapping an agent SDK or a hosted agent service. One of the articles argues for exactly that (`docs/research/articles/claude-managed-agents.md`).

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
