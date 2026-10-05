# Pedro's analysis of the Wavestone harness paper, checked against the paper

| | |
|---|---|
| Origin | Pedro's notes of 2026-10-02 on what arXiv 2609.00006v1 implies for this exercise, given to the project on 2026-10-05 |
| What this file is | The analysis restated point by point, each claim checked against the paper, then set against what we have learned since |
| Method | Checked by the main Claude Code session on 2026-10-05 by searching the paper's HTML text and, for items the HTML conversion had damaged, the PDF. The paper's own record is `harness-paper.md`. |
| Status | The "Finding" column is what the paper says. The comparison in the last section uses our later research and is our reading. |
| Used for | PLAN §3.9, decision D3, PLAN §2.1 decisions T3, T5 and T9 |

The analysis was written before this project's research and reaches the same pivot independently: from governance across agents to verification and quality measurement.

## The argument, as given

1. **Occupied ground.** Cross-agent governance exists at production scale in Omnigent, so a model-agnostic governance layer alone is not open ground.
2. **Vacant ground.** Verification and quality scoring are missing everywhere, including Omnigent. The paper itself names unified evaluation and a cross-system benchmark as open work. Pivot the wedge from governance to verification and quality measurement; Omnigent becomes a complement, even a distribution channel.
3. **Features do not defend.** Convergence is imitation; durable value sits a layer up or in measurement.
4. **Decision plane.** Model-based gates for tool risk have precedents and spread fast, so differentiate on cross-agent placement, verdict economics and recalibration fed by outcomes; lead with verification verdicts and routing, and do not push loop policing.
5. **Prototype.** Use the paper's 90-line scaffold as the agent under test inside the verification harness; stress cross-agent use and quantified pass^k.
6. **Repository understanding.** No embeddings over code and no agent frameworks in any of the eleven; a ranked repository map exists only in Aider.
7. **Safety bar.** The state of the art is per-harness and uneven; each strongest piece exists in one or two systems.

## Check of the claims

| Claim | Finding |
|---|---|
| Omnigent: Databricks, Apache-2.0, about 1M lines, 23 harness adapters, a three-level policy plane with CEL, Python or LLM evaluators and per-user budgets, fail-closed, enforced through each vendor's own hooks; uniform sandbox, egress proxy and secretless credential proxy; a conformance bench | Confirmed. "Harnesses are tested like hardware." |
| Codex ships enterprise MDM configuration | Confirmed |
| Omnigent "implements no editing loop… and does not evaluate output correctness" | **Half is not in the paper.** The text reads "it implements no editing loop, no repository context, no edit-application strategy". The words about output correctness appear in neither the HTML nor the PDF. The paper is silent on whether Omnigent evaluates correctness; it does note a conformance bench and review comments on sessions. |
| The paper removed SWE-bench scores as incomparable self-reports (footnote 4) | Partly. The paper still cites the scores. It says: "These figures are not directly comparable (different underlying models, different evaluation runs, different deployment configurations…) and we do not draw a head-to-head conclusion from them." |
| It names "unified evaluation frameworks… alongside correctness" and a cross-system benchmark suite as open work | Confirmed (EVIDENCE E-33) |
| "the half-life of a competitive distinctive in this field is currently measurable in weeks"; Codex adopted Claude Code's hook vocabulary | Confirmed |
| Gemini CLI routes each request "to the cheapest sufficient variant", with a classifier that can run on a local Gemma model through LiteRT-LM | Confirmed |
| Codex Guardian: a dedicated LLM approval reviewer with a strict-JSON verdict, failing closed, with a rejection circuit breaker | Confirmed |
| Hermes's `_smart_approve` uses 16 tokens | Confirmed: "temperature 0, 16 max tokens, APPROVE/DENY/ESCALATE" |
| Model-based gates spread from one system to two in a quarter | Confirmed in substance: the paper lists this among features that went "from one to two" between its two snapshots |
| Hermes ships stuck detection disabled; Recommendation 18 says not to over-engineer it | Confirmed |
| The 90-line scaffold: linear loop, four tools, AGENTS.md discovery, cost and turn caps, threshold compaction; implements 10 of 18 recommendations; "to be copied and specialized" | Confirmed from the listing in the PDF: tools `bash`, `read_file`, `write_file`, `search_replace`; `max_turns = 50`; `max_cost = 5.00`; compaction at 120,000 estimated tokens. "It is not a drop-in library; it is a scaffold to be copied and specialized." |
| Outer verification loops exist only inside single harnesses (Hermes verify-on-stop; OpenHands /goal judge), Table 12 | Confirmed |
| 0 of 11 use embeddings over code; 0 of 11 use an agent framework; the finding survived a threefold corpus expansion (Observation 9) | Confirmed, as Observation 9 |
| A ranked tree-sitter repository map exists only in Aider | Confirmed: "still the only ranked repository map in the corpus" |
| OpenHands dropped tree-sitter | Confirmed: "tree-sitter no longer present in the SDK" |
| OpenCode auto-downloads about 25 LSP servers | Confirmed: "25 auto-downloaded LSP servers feed diagnostics" |
| Codex has four safety layers; OpenHands a worst-case-wins ensemble with untrusted-content markers; OpenCode syntax-aware permissioning; Hermes a 12-pattern floor that survives `--yolo`, with matching on deobfuscated variants | Confirmed. The deobfuscated matching applies to Hermes's 47 dangerous-command patterns. |
| Multi-agent systems use about 15 times the tokens of chat | Confirmed: "∼15× more tokens than a single chat interaction", from Anthropic, against "a simple chat baseline, not against an optimized single-agent pipeline" |
| Pi audits per-turn cache-miss dollar waste | Confirmed |
| Observation 5: persistent memory has replaced compaction as the frontier; four governance models | Confirmed |
| Observation 1: loop sophistication does not predict performance | Confirmed |
| AHE ablation: structure carries the improvement; the system prompt alone regresses by 2.3 points | Confirmed in the PDF: "tools +3.3 pp, middleware +2.2 pp, long-term memory +5.6 pp), while the system prompt alone regresses performance (−2.3 pp)" |
| Recommendation 4: deferred tool loading cuts the prompt by about 40% | Confirmed |

## Set against what we have learned since

**Where the analysis still stands**
- The pivot from governance to verification and measurement. It is our decision ADR-001.
- Features do not defend.
- Lead with verdicts and routing, not loop policing.
- The safety patterns to cite: rules as data, a floor that no mode switches off, worst-case-wins.

**Where it needs qualifying**
- **"Vacant ground, everywhere" is too strong now.** The paper documents the absence inside eleven harnesses and one meta-harness. Outside that corpus the ground is partly taken: Anthropic's contract-plus-evaluator design, published metrics for production-qualified change, CodeRabbit's "control layer", Sonar's deterministic gate, Faros's per-repository benchmarks. The accurate word is narrow (PLAN §3.6 to §3.8).
- **"No system does … cost-per-solved-task as a product layer"** does not hold against Faros, which sells "cost per verified outcome".
- **"0 of 11" is a fact about the eleven.** Closed IDE products index code with embeddings.
- **"Nowhere as a cross-agent layer"**, said of safety, conflicts with the analysis's own first point: Omnigent is the cross-agent policy and sandbox layer.

**What it adds that we did not have**
1. **Omnigent as a distribution channel.** Its policy plane accepts Python evaluators and enforces them through each vendor's hooks. A gate shipped as an Omnigent policy evaluator is one integration reaching every harness Omnigent wraps. Open risks: we have no data on Omnigent's adoption, and Databricks could add the check itself.
2. **The paper's scaffold as the agent under test.** A published, citable agent removes the objection that we tuned the agent to suit our gate.
3. **Recalibration fed by outcomes.** Measured outcomes adjust the risk tiers over time. This gives each customer's accumulated data a job, and is the nearest thing to a defensible asset identified so far.
4. **"Planted-flaw evaluations"** as the name for seeded bad changes the gate must reject.

**One difference in emphasis.** The analysis stresses cross-agent verification in the prototype. After the market check, the comparison that separates us from funded competitors is a deterministic verdict against a model reviewer's verdict. Cross-agent use stays a stretch goal under the spend cap.
