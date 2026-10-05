# PLAN — ASSIST (working codename)

| | |
|---|---|
| Status | Working plan. The thesis is decided (§2.1). Research is complete through 2026-10-05. Nothing has been designed or built. |
| Date | Started 2026-10-03; last updated 2026-10-05 |
| Brief | `docs/init-prompt.md` |
| Source-of-truth order | `docs/PLAN.md` → `docs/ROADMAP.md` → `docs/JOURNAL.md`. If they disagree, the earlier one wins and the later one is corrected. |
| Time budget | One working day |

## 1. The position this plan sets out to defend

**Do not build another AI coding assistant, harness or control plane. Probe the one part nobody yet sells: a verdict on agent-written changes built from executable evidence, independent of the model vendor, and measured for error on the customer's own repository. Decide Build or Wait on what the probe shows.**

The leadership question is "why build another AI coding product when the largest companies already offer mature ones?" The research says the honest answer to that question, as asked, is: we should not. Generation is owned by the model vendors, priced by them, and copied between them within months.

**What we would not build**, because it exists or is funded: a coding assistant; an agent loop; a cross-agent policy, sandbox and budget layer (Omnigent, open source); a model-based review bot (CodeRabbit and others); the wider delivery control plane.

**The candidate product** is an evidence layer delivered as a plug-in to the tools a team already uses:

- a first process that guides the user to create the checks (a test suite or an evaluation), in the manner of test-driven or eval-driven development;
- a change contract written before the agent runs (scope, acceptance checks, budget), protected from the agent by mechanism;
- a verdict of executable evidence after the agent stops, run where the agent cannot interfere. For conventional code: the customer's own checks, a scope check on the change, and a check that the agent's tests mean something. For an LLM application: an evaluation over fixed cases, some hidden from the agent, reported as pass, fail or inconclusive;
- an evidence record of the outcome, which no vendor audit log we examined provides;
- a measured false-pass rate for that verdict, per repository and per model and harness pairing, used to set how much human review each class of change gets.

It is entered through measurement: run the customer's own tasks and report the rate and cost of production-qualified changes.

**Who it is for.** Engineering leaders, as sponsors, in organisations that build software. We expect the need to be sharpest where a wrong change is expensive, and weakest in high-throughput new builds, where a frontier lab argues that "corrections are cheap, and waiting is expensive". That expectation is a hypothesis for the pilot.

**How we proceed.** As a probe in three stages, each able to end it: a one-day prototype, a measurement pilot with one or two design partners, and a build only if the pilot clears thresholds set in advance (§2.1).

**Customer data.** The product works on the customer's code, checks and outcomes. Every party must know what is used and for what, and it stays in the customer's environment (§8).

**A second thesis was evaluated and not adopted:** a brownfield / enterprise-legacy specialisation (§3.11). There is no time in this exercise to validate it, so brownfield is not claimed as a first market. Its evidence did change the first thesis: fixed checks alone pass bad changes where tests under-describe behaviour, so the verdict was widened to executable evidence.

**Where the case stands.** The idea is not new. The framing and metrics are published, the model vendor describes a contract plus a separate evaluator, and a competitor valued at 1.5 billion USD is positioning as "the control layer" for agent-written changes. What remains open is the narrow list above. The case for **Wait, with a review date** is stronger than when this plan was first written, and it remains a real outcome.

**What the prototype is for.** To show whether a deterministic verdict is right more often than the agent's own claim and than a model reviewer's verdict, by a margin worth paying for (§7). If it is not, the recommendation is Wait.

In Pedro's own terms (from his working notes): "Reliability, not capability, is the wall" and "The platform is a harness around the agent, not a bet on the agent."

**How the position has moved**

| Date | Position | What moved it |
|---|---|---|
| 2026-10-03 | A thin, model-agnostic outer harness: policy, sandbox, gate and evidence around any agent | First research pass |
| 2026-10-05 | The evidence layer only, as a plug-in, entered through per-repository evaluation | The harness paper: the policy and sandbox layer already exists as open source (§1.1) |
| 2026-10-05 | A verifier with a measured false-pass rate; the mechanism itself is cheap to copy | Full re-read of the articles (§3.4) |
| 2026-10-05 | A deterministic, vendor-independent, measured verdict; the contract-plus-evaluator idea and the metrics are published | Anthropic's harness design post and two papers (§3.6, §3.7) |
| 2026-10-05 | The same, for teams where a wrong change is expensive; a funded competitor owns the adjacent ground | Market check of the review and verification segment (§3.8) |
| 2026-10-05 | Verdict widened from fixed checks to executable evidence; brownfield evaluated as a second thesis | Evaluation of the brownfield specialisation (§3.11) |
| 2026-10-05 | Decided: the first thesis, pursued as a three-stage probe; buyer, differentiation, exclusions, kill criteria and prototype scope settled | Thesis discussion (§2.1) |

The decisions behind this position are in §2 and §2.1. What the probe will show is not yet known.

### 1.1 Narrowing the position after the harness paper (agreed 2026-10-05, D1)

Pedro asked for the paper "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems" (Barbaste, Darrigol, Vu, Wiltberger, Wavestone AI Lab; arXiv 2609.00006v1) to be weighed before D1 closes. Selected sections were read on 2026-10-05 and the whole text afterwards; the record is `docs/research/harness-paper.md`.

**What it confirms**
- A basic agent loop is simple and widely replicated. Recommendation 1: "Start with a linear while loop". The paper says loop sophistication "does not predict benchmark performance" and ships a 90-line minimum viable harness. This is not the same as saying harness design does not matter: a later ablation study finds that the components around the loop change results by model, task and budget (§3.8).
- None of the eleven harnesses studied uses an agent framework or embeddings over code. Recommendations 8, 15 and 16 say not to build either. The corpus is terminal harnesses with readable source; it does not cover closed IDE products such as Cursor and Copilot, which do index code with embeddings (§3.8).
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

Decisions are recorded here as they are made. All ten are decided. The thesis decisions taken in the discussion of 2026-10-05 are in §2.1.

| ID | Decision | Recommendation | Why |
|---|---|---|---|
| D1 | Which wedge do we defend? | **Decided 2026-10-05:** the evidence layer, as a plug-in to existing tools, entered through per-repository measurement and pursued as a three-stage probe. Details in §2.1. | The first thesis was chosen over the brownfield specialisation, which there is no time to validate in this exercise. |
| D2 | What does the company already own? | **Decided 2026-10-03:** nothing. No proprietary model, no harness, no captive vertical, no special moat. | The strategy must stand without an inherited advantage. |
| D3 | Prototype inner loop | **Decided 2026-10-03, refined 2026-10-05:** a minimal single loop behind a provider interface, taken from the 90-line scaffold published in the harness paper (Listing 3, CC BY 4.0) and specialised only where needed, with every departure recorded in the journal. | It shows every design topic in readable code and makes the point that the loop is small. Using a published, citable agent removes the objection that we tuned the agent to suit our gate. Rejected alternatives: writing our own from nothing; wrapping an agent SDK or hosted agent service. |
| D4 | Prototype language | **Decided 2026-10-03:** Python. | Fastest for one day. |
| D5 | Model access and spend ceiling | **Decided 2026-10-03:** Anthropic first, hard cap of 50 USD across all runs. OpenAI may be used to cross-check results or as the adversarial reviewer. | No API key is set in the environment yet (ASSIST-006). |
| D6 | GitHub repo owner, name and access model | **Decided 2026-10-05:** private repo in Pedro's personal account, `pedraumcosta/assistant`. Created and pushed. | Consequence, per GitHub Docs: "Collaborators can't have read-only access to repositories owned by a personal account". Anyone invited will be able to push. Read-only sharing would need a transfer to an organisation. |
| D7 | Git author identity | **Decided 2026-10-03:** `pcosta@gmail.com` | Pedro's existing git config; closes ASSIST-002. |
| D8 | Proposal and presentation format | **Decided 2026-10-03:** Markdown first. When the content is close to final, a Claude Code artifact, then a Slidev presentation. | "Markdown for models, HTML for humans." |
| D9 | Use of material from outside this repo | **Decided 2026-10-03, refined 2026-10-05:** the repo is self-contained and cites public sources only. Pedro's private notes may be named as the origin of a claim; the public source behind the claim is what is cited and checked. | Readers of the repo cannot open Pedro's private files. Closes ASSIST-007. |
| D10 | Commit trailers | **Decided 2026-10-03:** keep the `Co-Authored-By: Claude` trailer; the git log is the record of how Claude Code was used. | Makes the build log verifiable. |

### 2.1 Thesis decisions (2026-10-05)

Taken in the thesis discussion. Each has its rationale in `docs/JOURNAL.md` (ADR-014 to ADR-016).

| ID | Question | Decision | Justification |
|---|---|---|---|
| P1 | Build, Wait, or between | **A small, dated probe in three stages, each able to end it:** (1) a one-day prototype; (2) a measurement pilot with one or two design partners; (3) build the gate only if the pilot clears thresholds set in advance. | In a thin market the narrow test is the move. Pure Build ignores that the concept is published and a funded competitor is adjacent. Pure Wait teaches nothing, when testing costs a day and then a few weeks. |
| P2 | Which thesis | **The first: the evidence layer.** The brownfield specialisation is not pursued, and brownfield is not claimed as a validated first market. | There is no time in this exercise to validate a solution for brownfield. The proposal may name legacy teams as a hypothesis for the pilot, not as a finding. |
| T1 | Buyer | **Engineering leaders, as sponsors, in organisations that build software.** The need is expected to be sharpest where a wrong change is expensive; that part is a hypothesis for the pilot. | They own delivery risk and the budget for engineering tooling, and they answer for what agents merge. |
| T2 | How we differ | **Four things no product we found offers together:** a verdict that runs the customer's own checks; independence from the model vendor; a measured false-pass rate; an outcome record. | Funded reviewers give model judgments and cannot run the test suite (E-50, E-51); none publishes a false-pass rate; no vendor audit log records outcomes (E-53). |
| T3 | Defensibility | **Stated plainly as thin:** neutrality, and each customer's accumulating checks and labels. **With a condition:** the product works on the customer's data, so every party must know what is used and for what, and all relevant precautions are taken (see Privacy and Redlines, §8). | The mechanism is cheap to copy and the idea is published; that is why the posture is a probe. The asset that accumulates is the customer's data, which makes its handling a first-order design matter and not a detail. |
| T4 | Where contracts come from | **The product's first process is guiding the user to create the checks:** a test suite or an evaluation, in the manner of test-driven or eval-driven development, kept simple. In the prototype the contracts are written by hand. | Without checks there is nothing to verify against, and the research shows agents guess when a task is underspecified (E-80). Making this the first step of the workflow, not an open question, is what turns the idea into a usable product. |
| T5 | Attachment | **A CI check first.** One harness hook as a demonstration if time allows. | CI needs no vendor hook; the harness layer has no standard interface yet. |
| T6 | Exclusions | **We do not build:** a coding assistant, an agent loop, a meta-harness, a policy or sandbox layer, a review bot, the wider delivery control plane, or a model of our own. | Each exists, is funded, or is a model vendor's home ground. |
| T7 | Kill criteria | **After the prototype, continue only if** the gate's false-pass rate is lower than both comparators, every planted flaw is rejected, and no unsafe action runs in the gated arm. **After the pilot, continue only if** at least one design partner says the report changed a decision they were about to make. **Otherwise the recommendation is Wait**, with a review date. | A probe needs its exits fixed before the results are known. The review date is still to be named by Pedro. |
| T8 | The CFO's numbers | **Deferred until the prototype is ready.** Working assumption, judged reasonable: two engineers and a part-time product lead for six weeks for the pilot, after the one-day prototype. | Better stated once the prototype shows what the pilot has to do. All figures will be labelled assumptions. |
| T9 | Prototype scope | **Three arms** (bare, prompt discipline, gated) and **two comparators** (the agent's own claim; an evaluator agent on a sample of runs). The cheaper-model arm moves to stretch. | The cheaper-model arm is confounded by sharing a harness and costs runs under the 50 USD cap. |
| T10 | Staying valuable as models improve | **Measurement is repeated for each and every model and harness pairing, and the product adapts to each.** This is to be emphasised in the proposal. | A check's value moves with each model release (E-36); harness effects change in size and sign by model (E-58). Adapting per model is what keeps the measurement worth paying for. |
| T11 | The verdict | **"Executable evidence."** In the prototype: the customer's fixed checks, a scope check on the diff, and a check that the agent's own tests fail against the original code. The counterexample search is the next enhancement, alongside the decision-model judge. | Fixed checks alone pass bad changes where tests under-describe behaviour (E-68). "Executable" is accurate where "deterministic" would overclaim once a model helps search for counterexamples. |
| T12 | Is the verdict always deterministic | **No. It is always executable.** For conventional code the verdict comes from tests and is a yes or no. For an LLM application it is an evaluation: fixed cases, some hidden from the agent, run repeatedly and scored against a threshold, reported as pass, fail or inconclusive. Code-based scoring first; a model scores only where code cannot, and then its agreement with human labels is measured and stated. **The prototype starts with the conventional case. The evaluation path is designed in `DESIGN.md`; implementing it is a bonus if time allows.** | Raised by Pedro: software built on an LLM cannot be verified by one deterministic run. What the product promises does not depend on determinism: checks fixed beforehand and protected, run outside the agent, recorded, and their own error rate measured. The conventional case gives the cleanest comparison against a model reviewer within one day. |
| T13 | Does the product add time and cost to delivery | **Yes, and the proposal says so.** It adds cost before the work (writing the checks), during it (extra attempts), after it (running the checks; for evaluations, many model calls) and over time (upkeep and re-measurement), and it adds waiting before merge. It is meant to remove review time, rework and incidents. Whether that nets out is not established; the pilot has to show it. The product limits its cost by applying checks by risk, reusing the team's existing pipeline, capping its own budget, and measuring wrongly failed changes as well as wrongly passed ones. | Raised by Pedro. A product that adds checks and hides their cost will not survive a CFO's first question, and the research itself warns that checking everything is waste (E-36) and that waiting has a price (E-57). |

Still open: the review date in T7, and T8.

Journal references: ADR-014 to ADR-018.

## 3. What the research says

Six research passes ran in parallel on 2026-10-03: three over Pedro's working notes, one over the linked articles, and two over the public market. Four articles and the harness paper were then re-read in full on 2026-10-05. Every pass has a record in `docs/research/`; `docs/research/README.md` is the index.

Verification tags used throughout the repo: **[L]** read in a PDF in Pedro's local folder, **[P]** read on the publisher's own page, **[S]** seen only in a search summary or secondary write-up. Only [L] and [P] figures may appear in CXO-facing documents; [S] figures must be re-verified first (ASSIST-004).

### 3.1 The problem is after generation

- METR, 2026-03-10 [P]: "roughly half of test-passing SWE-bench Verified PRs … would not be merged into main by repo maintainers".
- Faros AI Engineering Report 2026, 22,000 developers [L]: "Tasks involving code specifically have increased 210%", "Bugs per developer are up 54%", "Median review time has increased 5X", "31% more PRs are merging without any review". Faros sells measurement tooling, so it is an interested party.
- Stack Overflow Developer Survey 2025 [P]: 66% cite "AI solutions that are almost right, but not quite"; 46% distrust accuracy against 33% who trust it.
- Veracode, 2026-03-24 [P]: "only 55% of generation tasks result in secure code"; of two newer OpenAI models specifically, "No meaningful security gains materialized". Veracode sells application security.
- Destructive action is real: an agent deleted a production database and its backups in nine seconds [P, ACS Information Age, 2026-05-05].
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

**They show a basic harness is cheap to reproduce.** "Building Claude Code with Harness Engineering" rebuilds each mechanism in tens of lines and says: "That harness is fully reproducible, and that is exactly what we are going to build."

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

### 3.6 Second round of sources (2026-10-05)

Pedro supplied his notes on nine further reads. Six were located and read in full, including Anthropic's own harness design post; two had been read earlier through a summarising fetch; one could not be found (ASSIST-012). The claim-by-claim check is `docs/research/notion-notes-2026-10-01.md`. Seven claims in the notes needed correcting.

**What strengthens the direction**

- The model vendor says it in its own words: "agents reliably skew positive when grading their own work", and a separate evaluator "is still an LLM that is inclined to be generous towards LLM-generated outputs" (EVIDENCE E-34, E-35).
- Agreeing what "done" means before code is written is the vendor's published practice: generator and evaluator negotiate a contract with testable criteria and hard thresholds.
- First outcome evidence we have seen that a contract plus a separate evaluator changes the result: one prompt, one run each, a solo build whose central feature did not work against a harness build that was playable (E-37). It is a single vendor anecdote, and the harness run cost "over 20x" more.
- The leading harness runs a single loop with a flat message history, which supports our minimal agent under test.
- A harness's own transcript files can be read for evidence without the vendor's cooperation. The one tool we found that does this works with a single harness and its author says nothing about the format's stability.

**What weakens it**

- Contract plus separate evaluator is no longer a new idea. It is Anthropic's published design and can ship natively.
- The value of the check moves with the model. On the newer model the same author found the evaluator "unnecessary overhead" for tasks the model already does reliably: "It is worth the cost when the task sits beyond what the current model does reliably solo" (E-36).
- Evaluation tasks decay. Anthropic's hiring task, rebuilt around where the model struggled, lasted "several months" before the next model beat it; only out-of-distribution tasks held.
- Native features already cover the planning half of a contract (a committed spec with acceptance criteria, a task list). What they leave open is the verification half: the agent marks its own tasks complete.
- A practitioner article we read tells readers to stop bolting tools onto the harness. That is the objection a buyer will raise.

**What it changes**

1. The claim narrows again. What no source provides is a verdict that is **deterministic, independent of the model vendor, and measured for error on the customer's repo**, with a record a human can audit. Everything else in the original proposal now exists somewhere.
2. The gate is applied by risk, not uniformly. It earns its cost on work beyond what the current model does reliably, and that boundary moves with each release.
3. Measurement is recurring, not one-off: reliability has to be re-measured per model and harness pairing.
4. The contract must be protected by mechanism (a hook, a hash checked in CI, or storage the agent cannot write to). The sources that rely on file format or prompt wording to protect it say themselves that instructions are not guarantees.
5. The prototype's comparison arm changes (§7.1).

### 3.7 Two papers on verification economics and graduated oversight (2026-10-05)

Both turned up while searching for the sources in §3.6 and were read in full at Pedro's request. Records: `docs/research/paper-verification-economics.md` and `docs/research/paper-governed-ai-engineering.md`.

**Our framing is already published.** Bhati (arXiv 2609.04681, September 2026) is a synthesis of other studies that proposes:

- *Production-Qualified Change*: a change counts only once it passes the gates required for its risk class. This is what we had been calling an accepted change.
- *PQC per dollar* and *PQC per reviewer-hour*: the first is our cost per accepted change.
- The *Verification Tax*: review, CI, security and rework cost over generation cost. Bhati gives it this formula; the phrase itself appears earlier, in a DORA insight article dated 2026-03-10.
- A *control plane* that "records the evidence required to qualify the result" and can begin "as a policy and telemetry layer around" existing tools.

It states the question in the CFO's units: "how much production-qualified value an engineering system can deliver per dollar, per reviewer-hour, and per unit of operational risk" (EVIDENCE E-40). It also names the gap we target: "the verifier itself must be treated as a first-class artifact" (E-44), and asks "if one model generates the change and another model approves it, what independent evidence remains?" (E-43).

**Risk tiering is already published too.** Kang (arXiv 2606.22484) proposes three oversight tiers assigned by regulatory impact, customer proximity, reversibility and data sensitivity, with a per-tier list of audit artefacts and the principle "The agent that generates code cannot approve its own deployment."

**Neither paper builds or measures anything.** Bhati: the constructs "are not claimed as validated standards. They are hypotheses" (E-45). Kang states that no production deployment data is available; the paper's headline figure for velocity preserved under oversight is modelled from assumed inputs and is not usable.

**What this changes**

1. We adopt the published vocabulary, with attribution, instead of inventing terms. From here the plan's "accepted change" means a Production-Qualified Change, and "cost per accepted change" means PQC per dollar.
2. We cannot claim the framing, the metrics, the control-plane concept or the tiering logic. What is left that no source we have read provides:
   - a contract written before the run and protected from the agent by mechanism;
   - a verifier whose false-pass rate is measured, per repository and per model and harness pairing;
   - a working implementation with measurements.
3. The proposal's contribution becomes evidence, not concept: the first measurements of constructs that their own authors call hypotheses. That raises the weight of the prototype's results in the final recommendation.
4. The prototype reports in the published metric set (§7.1).
5. Risk tiers and redlines (§2.1 T7) now have two published starting points in place of the formula from the article we could not find.

Every figure these papers cite from other studies is second-hand and unused until checked at its source.

### 3.8 Third round: Pedro's web research notes, verified (2026-10-05)

Pedro supplied his web research notes of 2026-10-01. Their claims were checked in raw source pages, one cited paper was read in full, and the review and verification segment was researched from company sources. Overview: `docs/research/web-research-notes-2026-10-01.md`.

**The segment we would enter is funded and moving toward our position.**

- CodeRabbit raised 143 million USD at a 1.5 billion USD valuation on 2026-08-12 and launched "Agentic Change Management" as "the control layer": risk scoring, routing to humans, auto-merge of low-risk changes, a pre-work planning product, and a check of each change against its linked issue (EVIDENCE E-49).
- Sonar sells a deterministic quality gate for agent-written code, based on static analysis.
- Faros sells per-repository benchmarks "from your own merged code" to cut "cost per verified outcome".

**What those products do not do, on their own documentation**

- Their verdicts are model judgments. CodeRabbit's custom checks cannot "run your test suite" or "execute arbitrary repository code" (E-50). Claude Code's review check "always completes with a neutral conclusion so it never blocks merging" (E-51).
- None publishes a false-pass rate for its own verdicts. Four vendors each claim first place on the same review benchmark.
- No vendor audit log we examined records whether an agent's change was verified or accepted; they record actions and cost (E-53). Agent auditability is meanwhile emerging as a procurement requirement.
- Not found as a product: a machine-checkable contract agreed before the agent runs and enforced afterwards; a signed evidence bundle per change; a per-repository error rate for the verifier.

**A frontier lab argues the other way.** OpenAI describes running "with minimal blocking merge gates", with review "handled agent-to-agent", because "corrections are cheap, and waiting is expensive". It adds: "This would be irresponsible in a low-throughput environment" (E-56, E-57). An evidence gate is for teams where a wrong change is expensive: existing systems and regulated work. It is not for high-throughput new builds.

**Harness design is conditional, not irrelevant.** The ablation paper (arXiv 2609.20804) does not show that the harness outweighs the model, as the notes had it. Its conclusion is that each component "should be selected for the target model, task type, and resource budget rather than adopted as a default" (E-58). Two consequences:
- measuring each model and harness pairing on the customer's own work is useful and has to be repeated at each release;
- our cheaper-model arm is confounded if it shares one harness with the frontier arm (§7.1).

**A plug-in in the customer's environment sidesteps most procurement requirements.** If it runs in their CI, uses their model access and sends nothing back to us, then zero-retention and data residency do not apply to us, and SSO, model allow-lists and spend controls reduce to honouring what the customer already has. The audit record applies in full, because it is the product. This is our researcher's assessment, not a vendor statement.

**Corrections to our own earlier records**
- Cognition is valued at 48 billion USD as of 2026-09-08, not 25 billion (E-47).
- The statement that no harness uses embeddings over code is scoped to the eleven studied (§1.1).
- "The inner loop is a commodity" is reworded (§1.1, §3.4).
- The TechCrunch margins quotation is now confirmed (E-17).

**What it changes**

1. Being early is not available. The honest position is: a funded competitor owns the adjacent ground and has the parts to close the gap, and what remains open is narrow.
2. What remains open is the same list as §3.7, now checked against the market as well as the literature: a protected pre-run contract, a deterministic verdict that runs the customer's own checks, a measured false-pass rate, and an outcome record that no audit log provides.
3. The buyer is narrower: teams where corrections are expensive (§2.1 T1).
4. The case for Wait is stronger than at any earlier point. Whether the narrow open ground justifies Build is the decision for the thesis discussion; the prototype's job is to show whether a deterministic verdict beats a model reviewer's by a margin worth paying for.

### 3.9 Pedro's own analysis of the harness paper (2026-10-05)

Pedro's notes of 2026-10-02 on the Wavestone paper reach the same pivot this plan reached later: from governance across agents to verification and measurement. Checked claim by claim in `docs/research/harness-paper-implications-2026-10-02.md`. Nearly all of it holds against the paper. One quotation does not: the paper does not say Omnigent "does not evaluate output correctness"; it is silent on that.

Its conclusion that verification is "vacant ground, everywhere" was fair on the paper alone and is too strong after §3.6 to §3.8. The paper covers eleven harnesses and one meta-harness, not the market.

Three ideas from it are adopted as inputs:

1. **Omnigent as a channel, not only a rival.** Its policy plane accepts Python evaluators and enforces them through each vendor's hooks (EVIDENCE E-61). A gate shipped as an Omnigent evaluator is one integration in place of one per harness. We have no data on Omnigent's adoption, and Databricks could add the check itself (§2.1 T5).
2. **The paper's scaffold as the agent under test** (decision D3, refined). The listing has four tools, turn and cost caps, and threshold compaction (E-59).
3. **Recalibration fed by outcomes.** Measured outcomes adjust the risk tiers over time, which gives each customer's accumulated data a job (§2.1 T3).

Its term "planted-flaw evaluations" replaces "verifier-integrity set" in §7.1.

### 3.10 Decision models (2026-10-05)

Pedro asked whether a new kind of model, sold as Jev by TypeSafe AI, could be used to enhance an assistant. A decision model returns one option from a fixed set, with a confidence, instead of generated text. Overview and checks: `docs/research/decision-models-2026-10-02.md`.

**For an assistant: yes for cost and latency, and not for us.** Tool-risk gating, loop control, model routing and context triage are sensible uses. They sit inside the harness, which we do not build, and vendors already make cheap classifier calls at those points.

**It does not buy accuracy or independence.** On text rubrics, "On Jev's most confident errors, 96.0% of LLM verdicts repeat its answer, against 50.3% under independence" (EVIDENCE E-63). The same paper: "Use a Jev-first cascade to lower cost, and expect little gain in accuracy" (E-64). No code-related judgments were tested. This is the first measured support we have for keeping the verdict deterministic.

**For our evidence layer it is a component, never the verdict.** Three places: risk tiering; criteria with no executable check, as the middle step between deterministic checks and a stronger judge or a human; and triage such as real against flaky test failures.

**The useful link is calibration.** A decision model's raw confidence is overconfident, and "a few hundred labeled examples is enough to get most of the benefit" of recalibration (E-65). Our layer produces those labels on each repository: the deterministic outcome of every change and every human override. This gives a concrete form to the recalibration idea of §3.9, and no shipped product was found doing it.

**Constraints**

- Jev is hosted only, in the United States (E-62). Using it would send customer diffs to a new vendor and give up the tenancy advantage of §3.8. A self-hosted open build would keep it; its accuracy is not established.
- About 32,000 tokens for the material being judged.
- The idea is reproducible on small open models, so it is not a moat.
- The product is three weeks old and independent evidence is thin.

**Design consequence.** Any model judgment in the layer sits behind an interface, with a self-hostable classifier as the default and a hosted decision model as an option the customer chooses. The correctness verdict never depends on it.

**Decision (Pedro, 2026-10-05): next enhancement, not part of the first prototype.** The first prototype is built and measured without a decision model. The enhancement that follows it is:

1. a decision-model judge as a fourth verdict source beside the agent's own claim, the evaluator agent and the deterministic gate, reported on false-pass rate, variance across repeats, cost and latency;
2. a first test of recalibration: use the deterministic outcomes from the prototype's own runs as labels, and measure how much they improve the classifier's calibration.

It needs a TypeSafe API key or a local open build. The first prototype keeps the door open by recording, for every run, the inputs a judge would need and the deterministic outcome.

### 3.11 A second thesis evaluated: brownfield specialisation (2026-10-05)

Pedro's list of thesis candidates names a second one: a brownfield / enterprise-legacy assistant built on Osmani's practices (zoning by blast radius, a durable comprehension memo, characterization tests first, the harness as institutional memory). It was evaluated from its primary sources and the market. Full evaluation: `docs/research/second-thesis-brownfield.md`.

**The premise holds.** Agents are weakest in legacy code: "only 28 of 520 runs ( 5.4% ) pass all three stages" on whole-repository migrations (EVIDENCE E-67); gains "on complex, legacy brownfield code" are "often 10% or less" (E-70).

**As a separate product it is weaker than the first thesis.**

- Its four practices are process, reproducible as a prompt or a skill file, and each already exists as a product or feature.
- The evidence does not test them. Where it points anywhere, it points to model capability and to verification.
- In every verified success the decisive input was the customer's own oracle: an existing test suite, the running system, or replayed production traffic.
- Large migrations are sold by AWS, Microsoft, Google, IBM and Anthropic, largely free or bundled.
- With no model, customers or vertical (D2), every foothold found means choosing a vertical and starting with services-heavy work.

**As the first market for the evidence layer it is the best fit found.** It answers who the buyer is: teams where constraints live outside the code, tests under-describe behaviour, and a wrong change is expensive. Osmani's practices restate the evidence layer in brownfield terms: "Pin the behavior first, in a separate pass or by a person" (E-73); "Autonomy should follow blast radius, observability, and recoverability. A model's confidence is a poor guide" (E-74). Migration also has an oracle that ordinary change lacks, the old system, which eases the question of where contracts come from.

**It exposes a weakness in how §1 words the verdict.** On the migration benchmark, 118 runs passed every fixed behavioural check and 28 deserved to. Thirty had not migrated at all, and 60 of the remaining 88 were broken by a counterexample within the hour (E-68). Fixed checks alone are not enough where the customer's checks under-describe behaviour, which is the brownfield condition.

**Proposed refinement, for the thesis discussion.** The verdict has three parts, with the false-pass rate measured across all of them:

1. fixed checks from the customer;
2. a completeness audit: did the change actually happen;
3. a counterexample search: new tests written to find hidden differences.

The search is done by a model, and its result depends on which models search (E-69). What it produces is an executable failing test, so the evidence stays executable.

**Outcome (decided 2026-10-05).** Brownfield is not pursued, as a product or as a claimed first market, because there is no time to validate it in this exercise. The verdict is widened as proposed, with the counterexample search as a later enhancement (§2.1, T11; JOURNAL ADR-013).

### 3.12 Evidence on market structure and agent limits (2026-10-05)

Pedro pointed to six places in his notes on market analysis and the limits of coding agents. About half was already in our records. The rest was traced to its public sources and checked there. It is evidence for the proposal's problem section; it does not change the direction. Overview: `docs/research/market-and-limits-evidence.md`.

**What it adds**

- *Agents tamper with their own verifier.* A model trained on production coding tasks learned to force tests green, including by patching the test reporter to report "passed" (EVIDENCE E-75). This is the strongest evidence we have for protecting the contract and the checks from the agent by mechanism.
- *Passing tests is weak evidence.* On one benchmark, "31.08% of the passed patches are suspicious patches due to weak test cases" (E-77).
- *A deterministic check of whether an agent's tests mean anything.* Run them against the original code: "they must fail" (E-76). This is a cheap addition to the gate and bears on the wider verdict (§2.1 T11).
- *Regression is where agents fall furthest.* When earlier work must keep passing, the best strict solve rate on SlopCodeBench is 14.8% (E-78).
- *Agents guess instead of asking* (E-80), which supports writing the contract before the run.
- *Consistency, not one run.* A greater-than-60% agent falls below 25% when it must succeed eight times running (E-79), which supports reporting pass^k.
- *Hallucinated packages* at 19.7% of generated references in one large study (E-81), which supports a dependency check in the gate.
- *The lab's own view of harnesses.* An OpenAI engineer is quoted as "bearish on any harness that doesn't come from the lab whose model you are using" (E-83, quoted on a third-party show; original not found). The hosts' counter is that a builder's room is the outer layer.
- *No standard harness interface yet*, which is a cost for any plug-in that attaches to several harnesses (§2.1 T5).

**Corrections that matter for the proposal**

- Stack Overflow's like-for-like trust figures are 43% (2024) to 33% (2025), with distrust 31% to 46% (E-82). The "29%" in circulation is one answer option.
- The "95% of pilots fail" figure from MIT is preliminary and contested. It is not used.
- "2.74 times more vulnerabilities" comes from CodeRabbit, a code-review vendor, and reads "up to". It is not used.
- The SlopCodeBench figure in Pedro's notes (about 33%) is from a podcast; the paper's is 14.8%.

**Our own framing, not quotations.** The "pair" and "delegate" labels and "fan out reads, single-thread writes" are in no source. We may use them as our words.

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

**Issues.** Registered as `ASSIST-001` … `ASSIST-999` in `ROADMAP.md` §5, the only copy, and referenced by ID in commits and journal entries.

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

The same task set is run several times under each of three arms (decided, §2.1 T9). A cheaper-model arm is a stretch goal:

- **Arm A, bare:** the published scaffold alone, in a throwaway worktree. The scaffold has no sandbox and runs shell commands directly, so every arm runs inside an isolated copy of the fixture repository.
- **Arm P, prompt discipline:** arm A plus a "verify before you claim completion" instruction, standing in for prompt-only plugins.
- **Arm G, gate:** the loop inside the policy, contract and deterministic gate.

Finished runs are also scored by an **evaluator agent from a different vendor** (OpenAI, per D5), modelled on the evaluator Anthropic describes: it exercises the result against the contract's criteria, each with a hard threshold. It does not change the run; it gives us a second verdict to compare. A single judging call would be a weaker alternative than the one buyers will actually have. An evaluator agent costs more per run, so under the 50 USD cap it may be applied to a sample of runs.

Ground truth for each task is a set of acceptance checks the agent and the gate never see.

| ID | Hypothesis | Measure |
|---|---|---|
| H1 Safety | Deterministic policy stops the unsafe actions a bare or prompt-disciplined loop takes on trap tasks (out-of-scope edits, deleting or weakening tests, destructive commands, instructions planted in repo files, editing the contract) | Count of unsafe actions executed, per arm |
| H2 Reliability | A gate with a bounded repair loop raises consistency, not just one-shot success | pass@1 and pass^k against the hidden checks, per arm |
| H3 Economics | Cost per production-qualified change (PQC per dollar) is no worse with the gate | Tokens and dollars per production-qualified change, per arm |
| H4 Trustworthy verdict | The gate's "pass" is right more often than the agent's own claim (arms A and P) and than the evaluator agent's verdict | False-pass rate of each verdict source against the hidden checks |
| H5 Verifier integrity | The gate itself cannot be fooled by the failure modes found in the articles | Planted-flaw evaluations: a fixed set of seeded bad changes and broken test setups; every one must be rejected |
| H6 Overhead | The gate's added time and cost per task are small next to the agent's own, and it does not block good changes | Elapsed time and dollars added by the gate, per task; extra agent attempts it triggers; the false-fail rate (good changes wrongly failed) beside the false-pass rate |

H4 is the product's claim and the number that can kill it. H3 is the CFO's number. H5 is pass or fail. H6 is what the product costs the delivery process; the prototype can measure what the gate adds, and only a pilot can measure what it saves.

**Kill criteria after the prototype (decided, §2.1 T7).** Continue only if the gate's false-pass rate is lower than both comparators, every planted flaw is rejected, and no unsafe action runs in the gated arm.

**Reporting.** Results are reported in the metric set proposed by Bhati (§3.7) so that they are comparable with later work: PQC rate, PQC per dollar, first-pass qualification, retry rate, cost variance across repeats, and evidence coverage. "PQC per reviewer-hour" and "escaped-failure rate" need real reviewers and production, so they are pilot measures. The verifier's false-pass rate is our addition to that set.

**What one day cannot prove**, and the proposal will say so:
- real reviewer time saved, adoption, and willingness to pay, which are the pilot's measures;
- that contracts can be written cheaply for ordinary changes. In the prototype we write them by hand. This is the largest open product assumption.
- that the result holds on the next model. Anthropic's own evaluation tasks stopped discriminating within months, and tasks that resemble ordinary work fell first. Our task set will be a snapshot for the models we run.
- that a cheaper model can carry the main loop. The one source that reports heavy use of a cheaper model has it doing auxiliary calls, not the main loop. The cheaper-model arm is also confounded: an ablation study found weak models collapse on a minimal tool interface, so a poor result could reflect our harness and not the model. We either give that arm predefined tools or state the confound beside the result.

The task set will be small and written by us, so results are an indication, not a benchmark. The arms multiply the number of runs; the 50 USD cap (D5) is enforced by the runner and sets how many tasks and repeats we can afford.

### 7.2 Slices, in build order

1. **Loop.** The harness paper's 90-line scaffold (D3), with provider adapters for Anthropic and OpenAI and every step written to a JSONL event log with tokens, cost and latency. Its four tools (bash, read_file, write_file, search_replace) are kept as published.
2. **Policy.** Each tool call classified allow / review / block by deterministic rules; work confined to a git worktree; path zones; ceilings on turns, tokens and wall-clock time.
3. **Gate.** A task contract (scope, acceptance checks, budget), then the executable evidence after the agent stops, run in a separate process: tests, lint, diff scope, secrets scan, dependency changes. The checks include whether any new dependency exists, and whether the agent's own tests fail against the original code. Bounded repair attempts. Includes the planted-flaw evaluations (H5).
4. **Evidence.** A bundle per run, as JSON and Markdown: what was asked, what changed, which checks ran and their results, risk tier, cost.
5. **Eval runner.** Tasks × trials × arms into a results table, with the cross-vendor evaluator's verdict recorded beside the runs it scores and the spend cap enforced.
6. **Stretch.** The same gate attached to a vendor harness through a hook or MCP; context compaction and a repo map.

**Bonus, if time allows:** the evaluation path for an LLM application (§2.1 T12), shown end to end on one small task. It is designed in `DESIGN.md` whether or not it is built.

**Next enhancements, after the first prototype is measured:** a counterexample search (§3.11), and a decision-model judge with a recalibration test (§3.10). The decision model belongs with the evaluation path, as a low-variance scorer.

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
| Evaluation | pass^k and cost per production-qualified change, not pass@1. Deterministic checks before any model judge. The agent never grades itself. Where the software under change is itself an LLM application, the check is an evaluation with a three-way result (pass, fail, inconclusive), hidden cases, and a stated error rate for any model scorer. |
| Security | Assume prompt injection succeeds; break one leg of the lethal trifecta by design. Secrets never enter context. |
| Privacy | The product works on the customer's code, checks, outcomes and labels, so customers must know exactly what is used and for what. All of it stays in the customer's boundary; the provider is chosen per customer; nothing is used for training or shared across customers; calibration data belongs to the customer; retention is stated and short. |
| Observability | One structured event per step; the evidence bundle is the audit record ("provenance as schema, not logging"). |
| Human layer | Humans at risk-tiered gates. "No human in the loop" is a configuration justified by evidence, never a default. |
| Latency | Asynchronous by design: the unit is a delegated task, so the budget is minutes per task. The gate adds waiting before merge; time from task to accepted change is measured with and without it, and checks are applied by risk so that low-risk changes wait least. |
| Cost | A ceiling per task, enforced by the harness, covering verification as well as the agent's work. Headline metric: cost per production-qualified change, with the cost of checking included. For evaluations the cost is cases times repeats times model calls, so sample sizes are set by risk. |
| Failure handling | Every run ends in one of: accepted, needs review, blocked, budget exhausted. Each leaves a record. Rollback is deleting the worktree. |
| Redlines | Proposed in `DESIGN.md` for Pedro to set. Candidates: no write outside the sandbox; no merge without a human; no destructive command without approval; no secrets in context; no run without a record; a dated kill criterion for the business; the agent that writes a change cannot approve it; no use of customer data beyond what the customer has been told and agreed. |

## 9. Risks to this plan

| Risk | Response |
|---|---|
| The wedge is the most contested gap in the market | The proposal must show how ASSIST differs from a review bot. If it cannot, the answer is Wait. |
| The prototype result is weak or negative | That is a valid outcome. `RESULTS.md` reports it and the recommendation changes. |
| Small, self-authored task set | Stated as a limitation everywhere results appear. |
| The mechanism is cheap to copy; a harness vendor can add it natively through its own hooks | The proposal claims measurement, verifier correctness and neutrality, not the mechanism. If H4 does not show a clear gap over prompts and a model judge, the answer is Wait. |
| Contracts for ordinary changes may be too costly to write | Named as the largest open assumption; first question for a pilot. |
| The check's value shrinks as models improve | Aim the gate at work beyond what the current model does reliably, apply it by risk, and treat measurement as recurring. If the prototype shows no gap on the current frontier model, the answer is Wait. |
| The vendor ships contract plus evaluator natively | Our claim rests on independence, a deterministic verdict and a measured error rate, none of which a vendor's own evaluator provides. If buyers do not value those three, there is no product. |
| A plug-in depends on extension points the vendor controls | Keep CI as an attachment point that needs no vendor hook. |
| A funded review vendor joins its existing parts into a contract-then-evidence flow within a year | Named in the proposal as the most likely way the opportunity closes. Our answer has to be a measured difference between a deterministic verdict and a model reviewer's, or the recommendation is Wait. |
| One day is not enough for all nine phases | Stretch slice dropped first, then the artifact and deck reduced to a single diagram. The evidence ledger and the results are not cut. |
| Research figures that fail re-verification | Dropped, not softened. |
| Eval spend overruns | Hard cap from D5, enforced in the eval runner. |

## 10. Known issues

The issue register lives in `docs/ROADMAP.md` §5. It is the only copy.

## 11. Done so far

- Read the brief and the Practices root index.
- Six research passes run in parallel and all reported; recorded in `docs/research/` on 2026-10-05.
- Confirmed `gh` is authenticated as `pedraumcosta` with `repo` scope.
- Local git repository initialised with the brief and this plan; pushed to the private repo `pedraumcosta/assistant`.
- Harness paper (arXiv 2609.00006v1) read in full; findings in §1.1.
- Four linked articles re-read in full; findings in §3.4, prototype arms and hypotheses revised in §7.1.
- Pedro's Notion notes on nine further reads checked against the sources; six read in full; findings in §3.6.
- Two papers on verification economics and graduated oversight read in full; findings in §3.7.
- Pedro's web research notes checked in raw source pages; ablation paper read in full; review and verification segment researched; findings in §3.8.
- Pedro's own analysis of the harness paper checked against the paper; findings in §3.9; decision D3 refined.
- Pedro's addendum on decision models checked at primary sources; findings in §3.10.
- Second thesis (brownfield specialisation) evaluated from its primary sources and the market; findings in §3.11.
- Pedro's pointers on market structure and agent limits traced to public sources and checked; findings in §3.12.
- Thesis discussion held; decisions in §2.1.
- Evidence ledger rows E-01 to E-29 re-checked against raw sources and corrected.
- Proposal sections 1 and 2 drafted (`docs/PROPOSAL.md`); item on the verdict widened to cover evaluations for LLM applications (T12).
