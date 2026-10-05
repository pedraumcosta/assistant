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

The plan keeps "do not build" alive as a real outcome. The prototype exists to test five hypotheses (§7). If they fail, the recommendation to the CXOs becomes **Wait, with a review date**, and the proposal says so.

This position is a hypothesis for discussion, not a settled decision. See decision D1.

### 1.1 Narrowing the position after the harness paper (agreed 2026-10-05, D1)

Pedro asked for the paper "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems" (Barbaste, Darrigol, Vu, Wiltberger, Wavestone AI Lab; arXiv 2609.00006v1) to be weighed before D1 closes. Selected sections were read on 2026-10-05 and the whole text afterwards; the record is `docs/research/harness-paper.md`.

**What it confirms**
- The inner loop is a commodity. Recommendation 1: "Start with a linear while loop". The paper says loop sophistication "does not predict benchmark performance" and ships a 90-line minimum viable harness.
- No production harness uses an agent framework or embeddings over code. Recommendations 8, 15 and 16 say not to build either.
- Stay single-agent until parallel exploration is shown to win (Recommendation 12).

**What it changes**
- The outer layer is being commoditised as well. Databricks open-sourced Omnigent in June 2026, described as "a bet that the harness has become a commodity component and that the durable value sits one layer up". It wraps vendor harnesses behind one API and adds a cross-harness policy plane with per-user budgets, a uniform sandbox with a secretless credential proxy, and shareable sessions with review comments. OpenHands hosts Claude Code, Codex and Gemini CLI as interchangeable backends.
- So policy, sandboxing and budgets are not a wedge. They are free, open source and backed by a large vendor (ASSIST-010).

**What is still open, after the full read**
- "Safety" in these systems means action safety: is this command dangerous.
- Outcome checking is thin. Two of the eleven systems have an outer verification loop: OpenHands runs "an LLM judge over the transcript", and Hermes has a verify-on-stop guard that keeps the loop going when code changed without fresh verification evidence. Aider runs lint and tests inside its loop. Omnigent's example mandates cross-vendor review in a prompt.
- No system is described as running a deterministic gate after the agent stops and keeping an evidence record. The paper reports no false-pass rates, no repeated-run reliability and no cost per accepted change.
- The paper's own future work lists "Unified evaluation frameworks that assess safety, user experience, cost efficiency, and extensibility alongside correctness, addressing the gap between benchmark performance and production readiness".
- A plug-in has somewhere to attach: hooks exist in nine of the eleven systems, and Codex uses the same hook names as Claude Code. The paper also warns that prompt text is "a behavioral wish, not a mechanism", so a skill can carry the contract but enforcement has to sit in hooks or CI.

**Proposed narrowing**

| Option | What we build | Assessment |
|---|---|---|
| A. Outer harness (the §1 wording) | Policy, sandbox, gate and evidence around any agent | Weakened. Most of it now exists as open source. |
| B. Evidence layer | A change contract, deterministic verification, an evidence bundle and risk routing, delivered as a plug-in to existing harnesses through hooks, MCP, SKILL.md and CI | Recommended. It is the part nobody in the paper builds, and it rides the standards instead of competing with the platforms. |
| C. Per-repo agent evaluation | Run the customer's own tasks across harnesses and models; report pass^k, cost per accepted change and false-green rate | Recommended as the way in. It is the same engine as B, sold first as a measurement. |

Under B and C we build neither a harness nor a meta-harness. The prototype's own loop (D3) becomes the agent under test, not the product.

**Weaknesses to settle before closing D1**
- Nothing stops Omnigent, OpenHands or a review-bot vendor from adding the same checks. With no inherited moat (D2), the defensible assets would be neutrality (a vendor grading its own agent is not credible) and each customer's accumulated contracts and eval history.
- The paper says "the half-life of a competitive distinctive in this field is currently measurable in weeks". A verify-on-stop guard or a goal judge is a small feature for a vendor to add.
- The paper has no runtime measurements, so it gives no evidence that verification gates improve outcomes. That evidence has to come from our prototype.

**What we take from the paper into the prototype**
- An append-only event log as the system of record; the evidence bundle is a projection of it.
- Safety rules as data, with a floor that no mode can switch off (Recommendation 11).
- Checks combined worst-case-wins, failing closed.
- Repository content marked as untrusted before it enters context.
- No parallel delegation. The one second agent is a cross-vendor adversarial reviewer, which is where OpenAI fits (D5).
- Stretch: expose the gate through a hook or MCP so the same check runs against a vendor harness, not only our own loop.

## 2. Decisions needed from Pedro

Decisions are recorded here as they are made. All ten are now decided.

| ID | Decision | Recommendation | Why |
|---|---|---|---|
| D1 | Which wedge do we defend? | **Decided 2026-10-05:** option B of §1.1, the evidence layer delivered as a plug-in to existing harnesses, entered through option C, per-repo agent evaluation. | Pedro agreed the paper analysis and the narrowing. Still subject to the full re-read of the linked articles (ASSIST-005). |
| D2 | What does the company already own? | **Decided 2026-10-03:** nothing. No proprietary model, no harness, no captive vertical, no special moat. | The strategy must stand without an inherited advantage. |
| D3 | Prototype inner loop | **Decided 2026-10-03:** write a minimal single loop ourselves, behind a provider interface. | It shows every design topic in readable code and makes the point that the loop is small, so it is not the product. Rejected alternative: wrapping an agent SDK or hosted agent service. |
| D4 | Prototype language | **Decided 2026-10-03:** Python. | Fastest for one day. |
| D5 | Model access and spend ceiling | **Decided 2026-10-03:** Anthropic first, hard cap of 50 USD across all runs. OpenAI may be used to cross-check results or as the adversarial reviewer. | No API key is set in the environment yet (ASSIST-006). |
| D6 | GitHub repo owner, name and access model | **Decided 2026-10-05:** private repo in Pedro's personal account, `pedraumcosta/assistant`. Created and pushed. | Consequence, per GitHub Docs: "Collaborators can't have read-only access to repositories owned by a personal account". Anyone invited will be able to push. Read-only sharing would need a transfer to an organisation. |
| D7 | Git author identity | **Decided 2026-10-03:** `pcosta@gmail.com` | Pedro's existing git config; closes ASSIST-002. |
| D8 | Proposal and presentation format | **Decided 2026-10-03:** Markdown first. When the content is close to final, a Claude Code artifact, then a Slidev presentation. | "Markdown for models, HTML for humans." |
| D9 | Use of material from outside this repo | **Decided 2026-10-03:** the repo is self-contained. Nothing is cited from Pedro's private folders; any material we rely on is copied into `docs/research/` with its original source. | Readers of the repo cannot open Pedro's Dropbox. Closes ASSIST-007. |
| D10 | Commit trailers | **Decided 2026-10-03:** keep the `Co-Authored-By: Claude` trailer; the git log is the record of how Claude Code was used. | Makes the build log verifiable. |

## 3. What the research says

Six research passes ran in parallel on 2026-10-03: three over Pedro's working notes, one over the linked articles, and two over the public market. Four articles and the harness paper were then re-read in full on 2026-10-05. Every pass has a record in `docs/research/`; `docs/research/README.md` is the index.

Verification tags used throughout the repo: **[L]** read in a PDF in Pedro's local folder, **[P]** read on the publisher's own page, **[S]** seen only in a search summary or secondary write-up. Only [L] and [P] figures may appear in CXO-facing documents; [S] figures must be re-verified first (ASSIST-004).

### 3.1 The problem is after generation

- METR, 2026-03-10 [P]: "roughly half of test-passing SWE-bench Verified PRs … would not be merged into main by repo maintainers".
- Faros AI Engineering Report 2026, 22,000 developers [L]: "Tasks involving code specifically have increased 210%", "Bugs per developer are up 54%", "Median review time has increased 5X", "31% more PRs are merging without any review". Faros sells measurement tooling, so it is an interested party.
- Stack Overflow Developer Survey 2025 [P]: 66% cite "AI solutions that are almost right, but not quite"; 46% distrust accuracy against 33% who trust it.
- Veracode, 2026-03-24 [P]: "only 55% of generation tasks result in secure code" and "No meaningful security gains materialized" in newer models. Veracode sells application security.
- Destructive action is real: on 2026-04-25 an agent deleted a production volume and its backups in 9 seconds [P, ACS Information Age].
- Pedro's notes agree: "Review is the verifier", "The throughput gain and the quality debt are the same event", brownfield is "where our money is".

### 3.2 Where not to compete

- Model owners subsidise their own assistants; wrappers pay API rates. Anthropic and OpenAI both publish 20 USD and 100 USD subscription tiers for their coding assistants [P].
- Features spread between vendors within months: agent loop, plan mode, MCP, sub-agents, skills, hooks, cloud agents and PR review bots are now table stakes.
- The independent middle is being absorbed or closed (Windsurf, Continue, Tabnine, Roo Code) [S].
- TechCrunch, 2025-08-07: "Margins on all of the 'code gen' products are either neutral or negative." [S]

### 3.3 The case against entering at all

This goes in the proposal undiluted.

- Adoption is saturated: 84–90% of developers already use AI tools [P].
- Developers keep using the tools despite distrust, so dissatisfaction is not producing switching.
- The frontier moves faster than a product cycle; a product built around today's limitation may be obsolete at launch.
- Much of the problem evidence comes from vendors who sell the fix. Independent confirmation exists (METR, Stack Overflow) but is thinner, and METR's 2026-02-24 follow-up to its slowdown study is inconclusive by METR's own account [P].
- Every candidate gap is contested by someone.

### 3.4 What the harness articles add (full re-read, 2026-10-05)

The four articles Pedro asked to be re-read were downloaded complete and read end to end; the first pass had seen truncated summaries. The other three articles on the list were read only through a summarising fetch (ASSIST-005). Each has a record in `docs/research/articles/`.

**They confirm the harness is a commodity.** "Building Claude Code with Harness Engineering" rebuilds each mechanism in tens of lines and says: "That harness is fully reproducible, and that is exactly what we are going to build."

**None of them checks the outcome from outside the model.**
- *Senior Staff Engineer with sub-agent teams*: every gate (design approval, test-first, two-stage review, verification before completion) is skill text. The only deterministic mechanism is a session-start hook that injects text. The rule "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE" is judged by the model making the claim. The article's own test session stopped before any code was written.
- *Building Claude Code with Harness Engineering*: a task is done when the model stops. No contract, scope check, budget, post-stop check or evidence record. Its closing list of gaps includes a cost ledger and an evaluation framework: the test suite "does not measure how well the agent performs on real tasks".
- *Agent Harnesses with Claude*: better context instead of verification. In its own demo the agent missed a file when propagating a change and altered unrelated facts while editing; the step that held was a deterministic page-count script. No baseline, no repeated runs.
- *Building Claude from Scratch: 62 components*: the closest to our idea. It states the principle ("The verifier is not another LLM on critical paths it is pytest") and builds a definition-of-done contract compiled to tests. On reading the listings, the result parser would report a test-collection error as a pass, the verdict logic contradicts the contract's own tolerance ladder, and the budget guard is never read. Its end-to-end run reports 7.30% deviation against its own 5% target.

**What this changes for us**

1. The mechanism is cheap. Contract-to-test is about ten lines; anyone can claim "a verification layer" in a day. The mechanism is not the product.
2. The hard parts are the ones every article leaves out or gets wrong:
   - a verifier that cannot report a false pass, and that the agent cannot edit;
   - where contracts come from for ordinary repo changes that have no known right answer;
   - a measured error rate for the verifier itself, per repository;
   - enforcement by mechanism instead of by prompt.
3. So the product claim sharpens to: **a verifier you can trust, with its false-pass rate measured on your repo.** Measuring the gate is the differentiator, which is why per-repo evaluation (option C) is the entry.
4. The alternatives a buyer will compare us with are now concrete: prompt-only discipline (free plugins such as the "superpowers" plugin the author names) and a model acting as judge. The prototype has to beat both on evidence, or the answer is Wait. §7.1 adds them as comparison arms.
5. No article supplies evidence that prompt discipline fails in practice; they do not measure it. Our case rests on our own measurements.

**Adopted in the prototype**
- Loop that ends on the model's stop signal, with the iteration and budget caps the articles lack.
- Tool handlers that take a dict, return a string and never raise.
- Permission rules as data in three tiers, evaluated deny, allow, ask, with the default set to deny.
- Hook events named as vendor harnesses name them, so the gate attaches the same way in our loop and in theirs.
- Contract as a file written before the run: scope, named acceptance checks, budget, verdict ladder.
- Verdict taken only from the test runner's exit status and structured report, run in a process the agent cannot write to. Collection errors count as failures.
- The claim-to-required-evidence table from the senior-staff article as the schema for acceptance checks; "fresh" means run after the last change.
- A reverse-reference map (which files point at this one) as an input to risk scoring.
- Shipping format: SKILL.md, hooks, MCP and a CI check. We do not adopt the proposed "Agent Harnesses" directory standard; it has a single author and no adoption.

All figures in these articles are their authors' claims, and several run transcripts are inconsistent with the code shown. We cite the articles for patterns only.

### 3.5 What the notes do not cover

Pedro's notes have no market sizing, competitor pricing, unit economics, latency targets, customer-code privacy design, or anything labelled "redlines". Those come from the web research and from decisions in §2. The `Strategy/` and `Product Mngmnt/` shelves are not synced to this machine (ASSIST-003).

## 4. Deliverables

| File | Purpose | Brief topic |
|---|---|---|
| `docs/PLAN.md` | This plan | — |
| `docs/ROADMAP.md` | Step-by-step execution list with status, exit checks, and the ASSIST issue register | — |
| `docs/JOURNAL.md` | Dated log of what was done and decided; doubles as the architecture decision record | — |
| `docs/research/EVIDENCE.md` | Every number used anywhere, with source, date, URL and verification tag | 1 |
| `docs/research/` | Research records: market landscape, limitations evidence, the harness paper, one file per article, and the digest of Pedro's notes. `README.md` is the index | 1, 2, 3 |
| `docs/PROPOSAL.md` | The written case: problem, product, design summary, CFO message | 1, 2, 3, 4 |
| `docs/DESIGN.md` | System design: every design topic in the brief, plus risks, assumptions, redlines | 3 |
| Claude Code artifact, then Slidev deck | System design view and slides for the CXO session, built from the Markdown once it is close to final (D8) | 3 |
| `prototype/` | The working prototype and its eval set | 3 |
| `docs/RESULTS.md` | What the prototype measured, with the raw run data alongside | 3 |
| `docs/BUILD_LOG.md` | How Claude Code was used to produce the repo | Output item 5 |

## 5. Working rules

**Numbers.** No number is invented or estimated. Every figure in any document traces to a row in `EVIDENCE.md` or to a file under `prototype/runs/`. Targets and thresholds are decisions, not data; they are labelled "proposed" until Pedro sets them.

**Issues.** Registered as `ASSIST-001` … `ASSIST-999` in a table in `ROADMAP.md`, referenced by ID in commits and journal entries.

**Commits.** One commit per meaningful step in §6, made after the step's exit check passes **and after Pedro confirms** (rule set 2026-10-05). `docs/scratchpad.md` and `.env` are never committed. Conventional prefix (`docs:`, `feat:`, `test:`, `chore:`), a body that says what changed and why, and the ASSIST IDs touched.

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
| P2 | Evidence base | `docs/research/` records (done 2026-10-05) and `EVIDENCE.md` | Every figure we intend to use is tagged [L] or [P], or is dropped. Remaining work: verify the [S] rows in `EVIDENCE.md` | `docs: research records and evidence ledger` | 45 min |
| P3 | Problem and product | `PROPOSAL.md` §1–2: problem, value proposition, differentiation, exclusions, adopt / supplement / replace | Includes the case against entering; exclusions list is explicit | `docs: problem and product definition` | 45 min |
| P4 | System design | `DESIGN.md`: all topics in §8, risks, assumptions, redlines, what to prototype first | Each design topic has a position, a rejected alternative, and a way to measure it | `docs: system design` | 60 min |
| P5 | Prototype | `prototype/`, built in the slices of §7.2 | Each slice runs end to end on the fixture repo | One `feat:` commit per slice | 150 min |
| P6 | Measure | `RESULTS.md`, `prototype/runs/` | Results table generated from run files, with limitations stated | `test: eval runs and results` | 45 min |
| P7 | Proposal, design view, CFO message (people and weeks, assumptions stated) | `PROPOSAL.md` complete, artifact, Slidev deck | Recommendation is consistent with `RESULTS.md`, including if the hypotheses failed | `docs: proposal, design view, executive message` | 60 min |
| P8 | Build log and final review | `BUILD_LOG.md`; consistency pass across all documents | No number without an evidence row; no open ASSIST issue unaccounted for | `docs: build log and final review` | 30 min |

P3 and P4 are deliberately lean on the first pass. They are revised in P7 once the prototype has produced results.

## 7. The prototype

### 7.1 What it has to prove

The same task set is run several times under each arm:

- **Arm A, bare:** the agent loop alone.
- **Arm P, prompt discipline:** arm A plus a "verify before you claim completion" instruction, standing in for prompt-only plugins.
- **Arm G, gate:** the loop inside the policy, contract and deterministic gate.
- **Arm G-low:** arm G with a cheaper model tier.

Every finished run, in every arm, is also scored by a **model judge from a different vendor** (OpenAI, per D5). The judge does not change the run; it gives us a second verdict to compare.

Ground truth for each task is a set of acceptance checks the agent and the gate never see.

| ID | Hypothesis | Measure |
|---|---|---|
| H1 Safety | Deterministic policy stops the unsafe actions a bare or prompt-disciplined loop takes on trap tasks (out-of-scope edits, deleting or weakening tests, destructive commands, instructions planted in repo files, editing the contract) | Count of unsafe actions executed, per arm |
| H2 Reliability | A gate with a bounded repair loop raises consistency, not just one-shot success | pass@1 and pass^k against the hidden checks, per arm |
| H3 Economics | Cost per accepted change is no worse with the gate, and a cheaper model inside the gate approaches the frontier model without it | Tokens and dollars per accepted change, per arm |
| H4 Trustworthy verdict | The gate's "pass" is right more often than the agent's own claim (arms A and P) and than the model judge's verdict | False-pass rate of each verdict source against the hidden checks |
| H5 Verifier integrity | The gate itself cannot be fooled by the failure modes found in the articles | A fixed set of seeded bad changes and broken test setups; every one must be rejected |

H4 is the product's claim and the number that can kill it. H3 is the CFO's number. H5 is pass or fail.

**What one day cannot prove**, and the proposal will say so:
- real reviewer time saved, adoption, and willingness to pay, which are the pilot's measures;
- that contracts can be written cheaply for ordinary changes. In the prototype we write them by hand. This is the largest open product assumption.

The task set will be small and written by us, so results are an indication, not a benchmark. The arms multiply the number of runs; the 50 USD cap (D5) is enforced by the runner and sets how many tasks and repeats we can afford.

### 7.2 Slices, in build order

1. **Loop.** Single agent loop behind a provider interface; tools for read, search, edit, run; every step written to a JSONL trace with tokens, cost and latency.
2. **Policy.** Each tool call classified allow / review / block by deterministic rules; work confined to a git worktree; path zones; ceilings on turns, tokens and wall-clock time.
3. **Gate.** A task contract (scope, acceptance checks, budget), then checks after the agent stops, run in a separate process: tests, lint, diff scope, secrets scan, dependency changes. Bounded repair attempts. Includes the verifier-integrity set (H5).
4. **Evidence.** A bundle per run, as JSON and Markdown: what was asked, what changed, which checks ran and their results, risk tier, cost.
5. **Eval runner.** Tasks × trials × arms into a results table, with the cross-vendor judge verdict recorded beside each run and the spend cap enforced.
6. **Stretch.** The same gate attached to a vendor harness through a hook or MCP; context compaction and a repo map.

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
| The mechanism is cheap to copy; a harness vendor can add it natively through its own hooks | The proposal claims measurement, verifier correctness and neutrality, not the mechanism. If H4 does not show a clear gap over prompts and a model judge, the answer is Wait. |
| Contracts for ordinary changes may be too costly to write | Named as the largest open assumption; first question for a pilot. |
| One day is not enough for all nine phases | Stretch slice dropped first, then the artifact and deck reduced to a single diagram. The evidence ledger and the results are not cut. |
| Research figures that fail re-verification | Dropped, not softened. |
| Eval spend overruns | Hard cap from D5, enforced in the eval runner. |

## 10. Known issues

| ID | Issue | Status |
|---|---|---|
| ASSIST-001 | "Others read, only Pedro writes" is not available on a personal private repo as far as I know; to be confirmed against GitHub's documentation at setup | Accepted by D6: personal private repo; any collaborator added will have write access |
| ASSIST-002 | Git identity mismatch: `pcosta@gmail.com` (git config) vs `pcosta@clone.me` (session account) | Closed: commits use `pcosta@gmail.com` |
| ASSIST-003 | Parts of the Practices notes are Dropbox online-only and read as 0 bytes, including `Mngmnt/Strategy/`, `Mngmnt/Product Mngmnt/` and eight `Coding/` shelves | Open, not blocking |
| ASSIST-004 | Many research figures are tagged [S] and need primary-source verification before CXO use | Open, handled in P2 |
| ASSIST-005 | Article coverage is uneven: four articles were re-read in full on 2026-10-05; three (Claude Code source leak, architect study guide, managed agents) were read only through a summarising fetch. No article figure is usable as evidence | Open, not blocking |
| ASSIST-006 | No model API key or spend ceiling confirmed for the prototype | Closed: cap 50 USD (D5); Anthropic and OpenAI keys are in a git-ignored `.env` |
| ASSIST-007 | Some of the richest source material is interview preparation for another company | Closed by D9 |
| ASSIST-008 | One link in the brief was malformed; corrected in `docs/init-prompt.md` to the senior-staff-engineer article | Closed |
| ASSIST-009 | No cost inputs (team size, loaded cost, budget envelope) for the CFO message; without them the ask is stated in people and weeks, not money | Closed: no inputs exist. The CFO message states the ask in people and weeks, with every figure labelled as an assumption and listed in an assumptions table |
| ASSIST-010 | Omnigent (Databricks, open source, June 2026) already provides cross-harness policy, sandboxing, budgets and shared sessions, per the harness paper. The original "outer harness" framing overlaps with it | Closed by D1: we do not build the policy / sandbox / budget layer |

## 11. Done so far

- Read the brief and the Practices root index.
- Six research passes run in parallel and all reported; recorded in `docs/research/` on 2026-10-05.
- Confirmed `gh` is authenticated as `pedraumcosta` with `repo` scope.
- Local git repository initialised with the brief and this plan; pushed to the private repo `pedraumcosta/assistant`.
- Harness paper (arXiv 2609.00006v1) read in full; findings in §1.1.
- Four linked articles re-read in full; findings in §3.4, prototype arms and hypotheses revised in §7.1.
