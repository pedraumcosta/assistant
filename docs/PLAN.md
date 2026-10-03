# PLAN — ASSIST (working codename)

| | |
|---|---|
| Status | Draft for discussion with Pedro. Nothing below is executed until the decisions in §2 are settled. |
| Date | 2026-10-03 |
| Brief | `docs/init-prompt.md` |
| Source-of-truth order | `docs/PLAN.md` → `docs/ROADMAP.md` → `docs/JOURNAL.md`. If they disagree, the earlier one wins and the later one is corrected. |
| Time budget | One working day |

## 1. The position this plan sets out to defend

**Do not build another AI coding assistant. Build the layer that makes any of them safe to merge.**

The leadership question is "why build another AI coding product when the largest companies already offer mature ones?" The research says the honest answer to that question, as asked, is: we should not. Generation is owned by the model vendors, priced by them, and copied between them within months.

What the incumbents are not solving, and are paid by the token to make worse, is what happens after the code is written: review, verification, and the audit trail. ASSIST is a thin, model-agnostic **outer harness** that takes a task, runs any coding agent inside a bounded sandbox, and returns a change with the evidence a reviewer needs to accept or reject it quickly.

In Pedro's own terms (from the Practices notes): "Reliability, not capability, is the wall" and "The platform is a harness around the agent, not a bet on the agent."

The plan keeps "do not build" alive as a real outcome. The prototype exists to test four hypotheses (§7). If they fail, the recommendation to the CXOs becomes **Wait, with a review date**, and the proposal says so.

This position is a hypothesis for discussion, not a settled decision. See decision D1.

## 2. Decisions needed from Pedro

Each has a recommendation. Work on the phases in §6 starts once these are answered.

| ID | Decision | Recommendation | Why |
|---|---|---|---|
| D1 | Which wedge do we defend? (a) verification and evidence layer, (b) sovereign / air-gapped assistant, (c) brownfield modernisation for one vertical, (d) cross-vendor cost control plane | (a), with cost per accepted change as its headline metric, which absorbs most of (d) | (a) has the best-triangulated evidence and fits a one-day prototype. (b) has the weakest evidence and IBM shipped a self-hosted option on 2026-10-01. (c) needs a vertical we have not been given. The weakness of (a): it is the most contested gap, since every major vendor ships a review bot. Our answer has to be "gate before the PR and remove a human step", not "one more reviewer". |
| D2 | What does "our AI company" already own? (own models, a customer vertical, a distribution channel) | Assume nothing: no proprietary model, no captive vertical | The brief does not say. If the company does own a model or a regulated customer base, wedge (b) or (c) gets stronger and D1 should be revisited. |
| D3 | Prototype inner loop: write a minimal loop ourselves, or wrap an existing agent SDK or hosted agent service | Write a minimal single loop behind a provider interface | It demonstrates every design topic the brief lists (context, tools, permissions) in code a CXO's engineer can read, and it makes the strategic point: the inner loop is small, so it is not the product. The product code is the policy, gate and evidence layers around it. |
| D4 | Prototype language | Python, standard library plus the model SDK | Fastest for one day. Pedro's most recent authored code is Go with no external dependencies; Go is the alternative if he prefers it. |
| D5 | Model access and spend ceiling for the prototype and eval runs | Claude API, with a hard budget cap set by Pedro before any eval run | The eval runs each task several times across several arms. No key or budget has been confirmed (ASSIST-006). |
| D6 | GitHub repo owner, name and access model | Needs Pedro's call; see ASSIST-001 | "Others read, only Pedro writes" is not available on a private repo owned by a personal account, as far as I know. It needs an organisation-owned repo or a workaround. |
| D7 | Git author identity | **Decided 2026-10-03:** `pcosta@gmail.com` | Pedro's existing git config; closes ASSIST-002. |
| D8 | Proposal and presentation format | `docs/PROPOSAL.md` for the written case, plus one HTML page for the system design view and slides | Follows Pedro's rule "Markdown for models, HTML for humans". PowerPoint is the alternative if the CXOs expect a file. |
| D9 | May the documents cite material from `Practices/Churn/nubank_pwr_staff/`? | Reuse the ideas, cite the primary sources behind them, do not cite that folder | It is interview preparation for another company (ASSIST-007). |
| D10 | Commit trailers | Keep the `Co-Authored-By: Claude` trailer on every commit | It makes the "how Claude Code was used" summary verifiable from `git log`. |

## 3. What the research says

Six research passes ran in parallel: three over Pedro's Practices notes (AI/NLP, Coding, Mngmnt), one over the eight linked articles, and two over the public market. Three of the eight articles were only partly retrieved and one not at all (ASSIST-005).

Verification tags used throughout the repo: **[L]** read in a PDF in Pedro's local folder, **[P]** read on the publisher's own page, **[S]** seen only in a search summary or secondary write-up. Only [L] and [P] figures may appear in CXO-facing documents; [S] figures must be re-verified first (ASSIST-004).

### 3.1 The problem is after generation

- METR, 2026-03-10 [P]: "roughly half of test-passing SWE-bench Verified PRs … would not be merged into main by repo maintainers".
- Faros AI Engineering Report 2026, 22,000 developers [L]: "Tasks involving code specifically have increased 210%", "Bugs per developer are up 54%", "Median review time has increased 5X", "31% more PRs are merging without any review". Faros sells measurement tooling, so it is an interested party.
- Stack Overflow Developer Survey 2025 [P]: 66% cite "AI solutions that are almost right, but not quite"; 46% distrust accuracy against 33% who trust it.
- Veracode, 2026-03-24 [P]: "only 55% of generation tasks result in secure code" and "No meaningful security gains materialized" in newer models. Veracode sells application security.
- Destructive action is real: on 2026-04-25 an agent deleted a production volume and its backups in 9 seconds [P, ACS Information Age].
- Pedro's notes agree: "Review is the verifier", "The throughput gain and the quality debt are the same event", brownfield is "where our money is".

### 3.2 Where not to compete

- Model owners subsidise their own assistants; wrappers pay API rates. All three model vendors publish the same $20 / $100 / $200 subscription ladder [P].
- Features spread between vendors within months: agent loop, plan mode, MCP, sub-agents, skills, hooks, cloud agents and PR review bots are now table stakes.
- The independent middle is being absorbed or closed (Windsurf, Continue, Tabnine, Roo Code) [S].
- TechCrunch, 2025-08-07: "Margins on all of the 'code gen' products are either neutral or negative."

### 3.3 The case against entering at all

This goes in the proposal undiluted.

- Adoption is saturated: 84–90% of developers already use AI tools [P].
- Developers keep using the tools despite distrust, so dissatisfaction is not producing switching.
- The frontier moves faster than a product cycle; a product built around today's limitation may be obsolete at launch.
- Much of the problem evidence comes from vendors who sell the fix. Independent confirmation exists (METR, Stack Overflow) but is thinner, and METR's 2026-02-24 follow-up to its slowdown study is inconclusive by METR's own account [P].
- Every candidate gap is contested by someone.

### 3.4 What the harness articles add

The eight articles agree on one point that supports the position in §1: the value of a coding agent is in the harness, and the harness patterns are public and reproducible. One author's rebuilt core loop is a few hundred lines by their own count. That is why the inner loop is not a defensible product.

Patterns the prototype adopts from them:
- A single loop that ends on the model's stop signal, not on text that looks like "done".
- A name-to-handler tool registry with few, precisely described tools.
- Deterministic rules first for permissions. One article describes a model side-query that classifies commands instead of allowlists; we treat that as a second layer behind the rules, never a replacement.
- A stable prompt prefix for caching, with volatile content after it.
- Large tool outputs written to a file, with a preview in context.
- A definition-of-done contract with executable checks as the verdict, and a verifier separate from the generator.
- Typed outcomes for every run and every sub-task, with failures carrying what was attempted and what partially succeeded.

Two cautions. Several articles rest on leaked or reverse-engineered material and contradict each other on details (compaction design, tool counts), so we cite them for patterns only, never for numbers. And one article argues the opposite of D3: use a hosted agent loop and stop writing your own. That is the Buy option for the inner loop and it is recorded as the rejected alternative.

### 3.5 What the notes do not cover

Pedro's notes have no market sizing, competitor pricing, unit economics, latency targets, customer-code privacy design, or anything labelled "redlines". Those come from the web research and from decisions in §2. The `Strategy/` and `Product Mngmnt/` shelves are not synced to this machine (ASSIST-003).

## 4. Deliverables

| File | Purpose | Brief topic |
|---|---|---|
| `docs/PLAN.md` | This plan | — |
| `docs/ROADMAP.md` | Step-by-step execution list with status, exit checks, and the ASSIST issue register | — |
| `docs/JOURNAL.md` | Dated log of what was done and decided; doubles as the architecture decision record | — |
| `docs/research/EVIDENCE.md` | Every number used anywhere, with source, date, URL and verification tag | 1 |
| `docs/research/LANDSCAPE.md` | Competitor table and feature taxonomy | 1, 2 |
| `docs/PROPOSAL.md` | The written case: problem, product, design summary, CFO message | 1, 2, 3, 4 |
| `docs/DESIGN.md` | System design: every design topic in the brief, plus risks, assumptions, redlines | 3 |
| `docs/design.html` | System design view and slides for the CXO session | 3 |
| `prototype/` | The working prototype and its eval set | 3 |
| `docs/RESULTS.md` | What the prototype measured, with the raw run data alongside | 3 |
| `docs/BUILD_LOG.md` | How Claude Code was used to produce the repo | Output item 5 |

## 5. Working rules

**Numbers.** No number is invented or estimated. Every figure in any document traces to a row in `EVIDENCE.md` or to a file under `prototype/runs/`. Targets and thresholds are decisions, not data; they are labelled "proposed" until Pedro sets them.

**Issues.** Registered as `ASSIST-001` … `ASSIST-999` in a table in `ROADMAP.md`, referenced by ID in commits and journal entries.

**Commits.** One commit per meaningful step in §6, made after the step's exit check passes. Conventional prefix (`docs:`, `feat:`, `test:`, `chore:`), a body that says what changed and why, and the ASSIST IDs touched.

**Journal entries.** Two kinds in one file:
- Log entry: date, step, what was done, what deviated from the plan.
- Decision entry (`ADR-NNN`): decision, rationale, alternative considered and why it was rejected, what would change at production scale. This is the shape of Pedro's own `DESIGN_DECISIONS.md`.

**Pairing.** No throughput or speed number is reported without its quality number next to it.

## 6. Phases

Timeboxes are targets for a one-day budget, not measurements.

| # | Step | Output | Exit check | Commit | Timebox |
|---|---|---|---|---|---|
| P0 | Repo setup: `git init`, `.gitignore`, private GitHub repo, access model per D6 | Repo with `docs/init-prompt.md` and `docs/PLAN.md` | Repo is private; access matches D6 | `chore: initialise repo and plan` | 15 min |
| P1 | Roadmap and journal | `ROADMAP.md`, `JOURNAL.md` with ADR-001 (the wedge, D1) | Every step below appears in the roadmap with an exit check | `docs: roadmap, journal, ADR-001` | 20 min |
| P2 | Evidence base | `EVIDENCE.md`, `LANDSCAPE.md` | Every figure we intend to use is tagged [L] or [P], or is dropped | `docs: evidence ledger and landscape` | 45 min |
| P3 | Problem and product | `PROPOSAL.md` §1–2: problem, value proposition, differentiation, exclusions, adopt / supplement / replace | Includes the case against entering; exclusions list is explicit | `docs: problem and product definition` | 45 min |
| P4 | System design | `DESIGN.md`: all topics in §8, risks, assumptions, redlines, what to prototype first | Each design topic has a position, a rejected alternative, and a way to measure it | `docs: system design` | 60 min |
| P5 | Prototype | `prototype/`, built in the slices of §7.2 | Each slice runs end to end on the fixture repo | One `feat:` commit per slice | 150 min |
| P6 | Measure | `RESULTS.md`, `prototype/runs/` | Results table generated from run files, with limitations stated | `test: eval runs and results` | 45 min |
| P7 | Proposal, design view, CFO message | `PROPOSAL.md` complete, `design.html` | Recommendation is consistent with `RESULTS.md`, including if the hypotheses failed | `docs: proposal, design view, executive message` | 60 min |
| P8 | Build log and final review | `BUILD_LOG.md`; consistency pass across all documents | No number without an evidence row; no open ASSIST issue unaccounted for | `docs: build log and final review` | 30 min |

P3 and P4 are deliberately lean on the first pass. They are revised in P7 once the prototype has produced results.

## 7. The prototype

### 7.1 What it has to prove

The prototype compares three arms on the same task set, each task run several times:

- **Arm A:** bare agent loop, frontier model.
- **Arm B:** the same loop inside the ASSIST policy, gate and evidence layers, frontier model.
- **Arm C:** as B, with a cheaper model tier.

| ID | Hypothesis | Measure |
|---|---|---|
| H1 Safety | A deterministic policy layer stops the unsafe actions a bare loop takes on trap tasks (out-of-scope edits, deleting tests, destructive commands, instructions planted in repo files) | Count of unsafe actions executed, per arm |
| H2 Reliability | A verification gate with a bounded repair loop raises consistency, not just one-shot success | pass@1 and pass^k against acceptance checks the agent cannot see |
| H3 Economics | Cost per accepted change is no worse with the gate, and a cheaper model inside the gate approaches the frontier model without it | Tokens and dollars per accepted change, per arm |
| H4 Review load | The evidence bundle can route changes by risk without letting bad changes through as "green" | Share routed green / yellow / red, and the false-green rate |

H3 is the CFO's number. H4's false-green rate is the one that can kill the product.

**What one day cannot prove**, and the proposal will say so: real reviewer time saved, adoption, willingness to pay. Those are the pilot's measures. The task set will be small and written by us, so results are an indication, not a benchmark.

### 7.2 Slices, in build order

1. **Loop.** Single agent loop behind a provider interface; tools for read, search, edit, run; every step written to a JSONL trace with tokens, cost and latency.
2. **Policy.** Each tool call classified allow / review / block by deterministic rules; work confined to a git worktree; path zones; ceilings on turns, tokens and wall-clock time.
3. **Gate.** A task contract (scope, acceptance checks, budget), then checks after the agent stops: tests, lint, diff scope, secrets scan, dependency changes. Bounded repair attempts.
4. **Evidence.** A bundle per run, as JSON and Markdown: what was asked, what changed, which checks ran and their results, risk tier, cost.
5. **Eval runner.** Tasks × trials × arms into a results table.
6. **Stretch.** Context compaction and a repo map; a second-model adversarial review step.

### 7.3 Deliberately excluded

IDE plugin, any UI beyond the CLI, cloud or background agents, multi-agent orchestration, embeddings index, fine-tuning or our own model, MCP marketplace, autocomplete. These are either table stakes owned by incumbents or belong after the hypotheses hold.

## 8. Design positions to defend

`DESIGN.md` expands each row with the rejected alternative and how it is measured.

| Topic | Position |
|---|---|
| Model | Model-agnostic behind a provider interface. Route by task: cheaper tier where the gate can catch errors, frontier tier where it cannot. No own model. |
| Context management | Stable prompt prefix for caching; tool output shaped before it enters context; compaction that preserves decisions; sub-agents only for context isolation. |
| Repo understanding | Search, glob and syntax-aware reads plus a short repo map. No embeddings index. |
| Tool execution and permissions | Deterministic allow / review / block before every call. Worktree sandbox, no network by default, least-privilege credentials. Trust ladder: local-only, then PR, then wider. |
| Orchestration | Single loop first. "Fan out reads, single-thread writes." A second loop only when the single loop is measured as the bottleneck. |
| Evaluation | pass^k and cost per accepted change, not pass@1. Deterministic checks before any model judge. The agent never grades itself. |
| Security | Assume prompt injection succeeds; break one leg of the lethal trifecta by design. Secrets never enter context. |
| Privacy | Customer code stays in the customer's boundary; provider chosen per customer; no training on customer code; retention stated and short. |
| Observability | One structured event per step; the evidence bundle is the audit record ("provenance as schema, not logging"). |
| Human layer | Humans at risk-tiered gates. "No human in the loop" is a configuration justified by evidence, never a default. |
| Latency | Asynchronous by design: the unit is a delegated task, so the budget is minutes per task, with time-to-first-evidence tracked. |
| Cost | A ceiling per task, enforced by the harness. Headline metric: cost per accepted change. |
| Failure handling | Every run ends in one of: accepted, needs review, blocked, budget exhausted. Each leaves a record. Rollback is deleting the worktree. |
| Redlines | Proposed in `DESIGN.md` for Pedro to set. Candidates: no write outside the sandbox; no merge without a human; no destructive command without approval; no secrets in context; no run without a record; a dated kill criterion for the business. |

## 9. Risks to this plan

| Risk | Response |
|---|---|
| The wedge is the most contested gap in the market | The proposal must show how ASSIST differs from a review bot. If it cannot, the answer is Wait. |
| The prototype result is weak or negative | That is a valid outcome. `RESULTS.md` reports it and the recommendation changes. |
| Small, self-authored task set | Stated as a limitation everywhere results appear. |
| One day is not enough for all nine phases | Stretch slice dropped first, then `design.html` reduced to a single diagram. The evidence ledger and the results are not cut. |
| Research figures that fail re-verification | Dropped, not softened. |
| Eval spend overruns | Hard cap from D5, enforced in the eval runner. |

## 10. Known issues

| ID | Issue | Status |
|---|---|---|
| ASSIST-001 | "Others read, only Pedro writes" is not available on a personal private repo as far as I know; to be confirmed against GitHub's documentation at setup | Open, blocks P0 |
| ASSIST-002 | Git identity mismatch: `pcosta@gmail.com` (git config) vs `pcosta@clone.me` (session account) | Closed: commits use `pcosta@gmail.com` |
| ASSIST-003 | Parts of the Practices notes are Dropbox online-only and read as 0 bytes, including `Mngmnt/Strategy/`, `Mngmnt/Product Mngmnt/` and eight `Coding/` shelves | Open, not blocking |
| ASSIST-004 | Many research figures are tagged [S] and need primary-source verification before CXO use | Open, handled in P2 |
| ASSIST-005 | Article retrieval incomplete: the SFT / distillation article could not be fetched at all; "Building Claude from Scratch", "Senior Staff Engineer with sub-agent teams" and "Building Claude Code with Harness Engineering" were cut off part-way. All digests came through a summarising fetch, so no article figure is usable without checking the original | Open, not blocking |
| ASSIST-006 | No model API key or spend ceiling confirmed for the prototype | Open, blocks P6 |
| ASSIST-007 | Some of the richest source material is interview preparation for another company | Open, see D9 |
| ASSIST-008 | The last link in the brief was two URLs joined together; treated as two articles | Closed |
| ASSIST-009 | No cost inputs (team size, loaded cost, budget envelope) for the CFO message; without them the ask is stated in people and weeks, not money | Open, needed by P7 |

## 11. Done so far

- Read the brief and the Practices root index.
- Six research passes run in parallel and all reported. Their findings exist only in this session so far; P2 writes them into `docs/research/`.
- Confirmed `gh` is authenticated as `pedraumcosta` with `repo` scope.
- No repository created, nothing committed, nothing published.
