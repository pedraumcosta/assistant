# Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains

| | |
|---|---|
| Author | Richard Kang (DoiT International, per the paper) |
| Reference | arXiv 2606.22484v2; v1 2026-06-21, revised 2026-07-04 |
| Source | https://arxiv.org/abs/2606.22484 |
| Read on | 2026-10-05, from the arXiv HTML full text of v2 |
| Method | Read end to end by a Claude Code sub-agent, including references and both appendices. |
| Status | Digest with quotations, not a copy. The paper is a framework proposal with no deployment data; its headline velocity figure is modelled from assumed inputs and is not usable as evidence. |
| Used for | PLAN §3.7, ROADMAP open questions T1, T6 and T7 |

## Read record

- **Paper:** "Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains", arXiv:2606.22484v2 [cs.HC], dated 04 Jul 2026. No v1 date appears in the text.
- **Author:** Dr. Richard Kang, sole author. Affiliation as stated: DoiT International (richard@doit.com). A disclaimer says the views are personal, are "academic thought leadership" and are not compliance advice.
- **Read:** the whole file, lines 1-1706 (body 154-1376, references, Appendices A and B, page chrome).
- **Kind:** a framework proposal with no empirical study, case data or deployment: "The evaluation is analytical — no production deployment data is available." Its claims rest on the author's reading of regulatory text, a self-scored feature comparison, an arithmetic model with assumed inputs, and three proof sketches. The bank example is declared fictional.

## What the paper proposes

**Oversight Classification Model (OCM).** "a formal, deterministic decision function that routes code generation tasks to appropriate oversight tiers based on four risk dimensions". The dimensions are categorical, with no numeric scoring:

- Regulatory Impact (RI): strategic / non-strategic — "Whether the code affects functions a regulator classifies as requiring human oversight"
- Customer Proximity (CP): direct / indirect / internal
- Reversibility (RV): irreversible / partial / full — "Whether deployed code can be rolled back without customer harm"
- Data Sensitivity (DS): personal / business / public

Assignment is by ordered rules, first match wins:

1. RI = strategic: Tier 1.
2. CP = direct: Tier 2.
3. CP = indirect and DS = personal: Tier 2.
4. CP = indirect and RV = irreversible: Tier 2.
5. Classification confidence below threshold θ: Tier 1 (fail-safe).
6. Dependency path to a strategic function: Tier 1 if path length is 1, otherwise Tier 2.
7. Otherwise Tier 3.

Inputs are a regulatory function registry and a dependency graph. Claimed properties: monotonicity, fail-safety "under correct or uncertain metadata", totality.

**Tiers and what the human does.**

- **Tier 1, Human-in-the-Loop:** "The coding agent halts and escalates control (RETURN_CONTROL). The human reviews the proposed approach, modifies if needed, and explicitly approves before generation proceeds. At deployment, the human again reviews all evidence and authorizes." Two gates: design and deploy.
- **Tier 2, Human-over-the-Loop:** "The agent generates and tests autonomously; a human approves deployment." One gate.
- **Tier 3, Automated with Monitoring:** "Full autonomous pipeline with post-deployment monitoring and exception-based human escalation." No gate.

**Reclassification.** Moving down a tier needs a clean deployment record and second-line compliance approval; moving up is immediate on an anomaly, incident or regulatory change.

**Evidence artefacts (Table IV).** All tiers: OCM classification log, generation trace, security scan results, test execution results, monitoring record, anomaly detection. Tiers 1-2 add human reviewer ID and a signed deploy authorisation. Tier 1 adds the RETURN_CONTROL event, review timestamps, "approval decision with rationale, modification diff, deployment authorization with cryptographic signature". Storage is append-only with a cryptographic hash chain.

**Enforcement.** Concept level only (Table VII): rule engine plus registry; agent escalation API ("Halt + notify + await"); CI/CD human approval gate ("Block until authorized"); automated quality gates ("Deploy on pass"); distinct agent instances for generation and testing ("Author ≠ tester"). No code, tool or harness integration is described.

**Regulatory mapping.** Primary: the Bank of Thailand 2025 AI circular (human participation → Tier 1; testing → generation/validation separation; explainability → generation trace). Lighter: MAS FEAT, NIST AI RMF, ISO/IEC 42001, EU AI Act Art. 14, OCC MRM, each with a stated gap.

## Evidence and method

- **Regulatory coverage:** the author's own trace of GAIE components against requirements he enumerated from the BOT circular. No examiner or compliance function reviewed it.
- **Comparative analysis:** a yes/no feature table against four other frameworks, scored by the author.
- **Expert validation:** not done. The Likert instrument in Appendix B is a plan.
- **Formal properties:** proof sketches; machine-checked proofs are future work.
- **The 84-97% figure:** modelled from assumed inputs; nothing was measured. Table X posits three scenarios, each with an assumed share of task volume per tier and an assumed velocity retained per tier. "Weighted velocity" is the volume-weighted sum, which reproduces the stated results; the paper does not print the formula. The denominator is "ungoverned agentic coding velocity", the hypothetical throughput of the same agents with no oversight. No source is given for any input. The "uniform HITL" comparison is simply the assumed Tier 1 velocity row. "These are analytical approximations, not empirical measurements."

## Figures

Assumed (model inputs, Table X; conservative / moderate / optimistic):

- "Tier 3 volume share | 60% | 70% | 80%"
- "Tier 2 volume share | 25% | 20% | 15%"
- "Tier 1 volume share | 15% | 10% | 5%"
- "Tier 3 velocity | 95% | 98% | 100%"
- "Tier 2 velocity | 80% | 85% | 90%"
- "Tier 1 velocity | 45% | 55% | 65%"

Modelled:

- "Weighted velocity | 83.8% | 91.1% | 96.8%"
- "preserves 84–97% of ungoverned agentic coding velocity (central estimate: ∼91%)"
- "84–97% velocity preservation (central: 91%) vs. 45–65% under uniform HITL"
- "strategic-function code (estimated 5–15%)", "customer-impacting code (15–25%)", "internal tooling (60–80%)"

Assumed (design parameters and fictional walkthrough):

- "N≥20 consecutive clean deployments, zero anomalies, rejection rate below 5%"
- "quarterly review" (registry)
- Elapsed: "∼4 hours" (Tier 1), "∼45 min" (Tier 2), "∼8 min" (Tier 3); "Enhanced 72h" monitoring
- "5–8 practitioners planned"; "3+ years experience"

Author's own analysis (not measured):

- "GAIE's design addresses 9 of 10 applicable control domains"
- "Of 18 enumerated BOT control requirements (6 organizational, 12 development/security), GAIE provides functional traceability to all 17 applicable requirements"

Cited from other sources:

- "productivity gains of 20–56% on well-scoped tasks [5]"; "a 19% slowdown for experienced developers"; "91% longer review times" (Farrag)
- "55% faster task completion for basic coding tasks [14]"
- "resolving 20–70% of real GitHub issues autonomously [16]"
- "Farrag [5] (∼81% under uniform governance)"

Measured: none.

## Overlap with our evidence layer

| Our element | In the paper? |
|---|---|
| Risk tiering and routing to humans | Yes. This is the core contribution, with an explicit rule order and fail-safe default. |
| Evidence bundle | Partly. A per-tier artefact list and hash chain, but no schema or format, and no cost, budget or "what was asked" field beyond "task request" provenance. |
| Deterministic post-run verification | Only as "automated quality gates", tests and scans. No verification method is specified. |
| Change contract before the run | No. There is no scope, acceptance-check or budget contract. Tier 1 pre-approval of the "proposed approach" is the nearest thing. |
| Per-repo agent evaluation | No. |
| Measured false-pass rate | No. "OCM accuracy" and "false-escalation rates" are listed as research needed. |
| Plug-in delivery (hooks, MCP, CI) | No. A standalone multi-agent supervisor architecture is sketched. |

It is a governance model with a reference architecture on paper; nothing is implemented. It is prior art for part of our product: the tiering and routing logic and per-tier evidence as a by-product of development. It is not prior art for the change contract, the verification engine, per-repo evaluation, measured error rates or the plug-in form.

## What we could use

- **Tier inputs:** the four dimensions and the gate ladder (design plus deploy / deploy only / none) are a ready starting taxonomy. The "regulatory function registry" can generalise to a per-repo registry of protected paths, with dependency distance as an escalator.
- **Redlines:** the paper names nothing that is never automated; Tier 1 still lets the agent generate. Nearest candidates: BOT's strategic functions (credit approval, account opening approval, approval of deposits, withdrawals or transfers), AML screening rules, and "The agent that generates code cannot approve its own deployment."
- **Bundle contents:** classification log, generation trace, reviewer identity and timestamps, approval rationale, modification diff, test and scan results, signed authorisation, tamper-evident chaining.
- **Process ideas:** shadow-mode classification validated against human judgment before enforcement; evidence-gated downgrade; tracking review duration and modification rate to detect rubber-stamping.
- **Buyers:** the paper asserts regulators require human oversight and auditability for strategic functions, and tells vendors to "Build RETURN_CONTROL / escalation mechanisms as first-class features." That is consistent with a regulated-industry need, but it is one author's argument with no buyer, budget or demand evidence.

## Cautions

- Stated limits L1-L7: single jurisdiction for the primary mapping; no production data; boundary ambiguity; expert validation pending; technology coupling; "confident but incorrect metadata is a failure mode"; mappings not validated by authorities. "Traceability does not equal compliance."
- Internal inconsistency: "9 of 10 applicable control domains" in one section, "all 17 applicable requirements" in another.
- The fail-safe rule sits after the CP rules, so a low-confidence task marked CP = direct gets Tier 2, not Tier 1. This is our reading of Algorithm 1; the paper does not discuss it.
- How the four dimensions and confidence are computed is unspecified; "OCM automation via static analysis" is future work.
- Author interest: an industry affiliation, a single author (the text says "authors"), a preprint with no sign of peer review.
