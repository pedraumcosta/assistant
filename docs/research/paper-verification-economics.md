# Beyond Code Generation: Reliability, Verification, and Cost Economics in the Agentic Software Development Lifecycle

| | |
|---|---|
| Author | Happy Bhati (Northeastern University email address; no affiliation line in the text) |
| Reference | arXiv 2609.04681v1, September 2026. Subtitle: "A Systems Synthesis of Industrial Evidence and a Research Agenda for Agentic Engineering" |
| Source | https://arxiv.org/abs/2609.04681 |
| Read on | 2026-10-05, from the arXiv HTML full text |
| Method | Read end to end by the main Claude Code session, abstract through conclusion and the research-integrity note. Quotations below were copied from the downloaded text. The six figures were not viewable in the text conversion. |
| Status | Digest with quotations, not a copy. The paper is a synthesis: "It does not report new model experiments." Every figure in it belongs to another study and is second-hand here. |
| Used for | PLAN §3.7, ROADMAP open questions T2, T3, T7 and T9 |

## Why it matters to us

This paper publishes, one month before our exercise, most of the vocabulary and metrics we had arrived at ourselves. It is prior art for our framing. It is not prior art for a product: it describes no implementation and reports no measurements.

## What the paper says

**The thesis.** "producing a plausible patch is getting cheaper at the same time that proving the patch deserves to ship is becoming more important." And: "the useful question is no longer how much code an agent can generate, but how much production-qualified value an engineering system can deliver per dollar, per reviewer-hour, and per unit of operational risk."

**Four constructs**, all the author's proposals:

1. **Agentic SDLC Throughput Paradox.** "Generation throughput is the rate at which candidate change is produced. Delivery throughput is the rate at which trustworthy change reaches users. Agentic software engineering raises the first rate faster than it automatically raises the second."
2. **Production-Qualified Change (PQC).** "A candidate change i receives PQC credit only if it satisfies the organization's relevant qualification vector": the product of pass/fail over the set of gates required for that class of change. A documentation edit has few gates; "a database migration, authentication change, or payment path may have a much larger one".
3. **Verification Tax.** The ratio of CI, review, security and rework cost to generation cost. "The goal is not 'minimize verification.' A low Verification Tax can be dangerous if it results from skipping tests or rubber-stamping reviews."
4. **Agentic SDLC Control Plane.** "a layer that observes work, assigns an execution policy, and records the evidence required to qualify the result." It "does not need to replace IDE agents, CI systems, Git hosting, security scanners, or deployment platforms. It can begin as a policy and telemetry layer around them." Six responsibilities: classify task risk, select an execution plan, require evidence, stop waste, attribute cost, learn from outcomes.

**The autonomy budget.** Autonomy is "a budgeted privilege" constrained jointly by money, reliability risk and human attention. The control policy chooses the plan that maximises expected production-qualified value minus weighted cost, expected failure loss and human attention, "subject to mandatory security, policy, and SLO constraints. … The weights are organizational policy, not universal constants."

**On verification itself.**
- "if one model generates the change and another model approves it, what independent evidence remains?"
- "review should become risk-adaptive rather than uniformly manual or uniformly automated."
- "test volume is a poor assurance metric. A test is useful when it adds independent discriminatory power against plausible faults. In agentic pipelines, the verifier itself must be treated as a first-class artifact."
- "A generated test that asserts the generator's own assumptions adds little independence."
- "Companies often budget AI licenses before budgeting the capacity needed to verify the resulting changes."

**Proposed metrics** (Table 3): PQC rate, PQC per dollar, PQC per reviewer-hour, Verification Tax, first-pass qualification, human escalation rate, retry / cycle rate, escaped-failure rate, cost variance (P95 over median for a task class), and evidence coverage: "Fraction of risk-required gates with machine-readable evidence attached". The paper warns that PQC "must not become an individual developer productivity score".

**Research questions it leaves open**, several of which are ours:
- RQ2: "Can verification budgets be allocated adaptively without increasing escaped defects?"
- RQ3: "When does an additional agent increase reliability rather than correlated error?" It says independence between generator and verifier "cannot be assumed" and should be measured "across model families".
- RQ9: "How can reliability evidence survive model and harness changes?" It calls "Versioned evidence and replayable trajectories" prerequisites.

**Its own limits.** "The proposed constructs - PQC, Verification Tax, Agentic Autonomy Budget, and the Control Plane - are not claimed as validated standards. They are hypotheses intended to make future studies comparable." It is "not a PRISMA-style exhaustive systematic review", and "some 2026 sources are preprints or organization reports".

## Figures cited by the paper

All are other studies' results, quoted here as this paper reports them. None has been checked at its primary source, so all are tagged [S] in `EVIDENCE.md` terms and none is usable yet.

| As reported in the paper | Attributed to |
|---|---|
| "In three randomized field experiments spanning 4,867 developers, AI assistance increased completed tasks by 26.08% in the pooled estimate" | Developer RCTs, Management Science |
| Coding activity from autonomous agents up "180% at the commit level - that fell to 50% at the project level and 30% at actual releases", from "more than 100,000 GitHub developers" | Demirer, Musolff and Yang (MIT / NBER) |
| "only 44% of agent-produced code survived into user commits", users "pushed back on agent outputs in 44% of turns", from "6,000 real coding-agent sessions" | Stanford SWE-chat |
| "rollouts averaged 27.2 million tokens", "no tested configuration above 30% pass@1", "reward-hacking behavior in 13.8% of rollouts" | SWE-Marathon |
| "about 60 minutes of active author shepherding time between sending a change for review and submitting it" | Google code-review research |
| "75% of generated test cases built correctly, 57% passed reliably, and 25% increased coverage"; engineers "accepted 73% of its recommendations" | Meta TestGen-LLM |
| Agents "about 30% less successful when cooperating than when performing both tasks alone", "more than 600 collaborative coding tasks" | CooperBench (Stanford and SAP Labs) |
| "among 138 tasks that one frontier model did not consistently solve, 59.4% had material issues in test design or problem description" | OpenAI audit of SWE-bench Verified |
| "98% of surveyed practitioners now manage AI spend, up from 31% two years earlier" | FinOps Foundation |
| AI coding cost "could exceed the average developer salary by 2028" | Gartner forecast. The paper: "should not be treated as a measured inevitability" |
| "Sixteen experienced open-source developers completed 246 tasks … a 19% slowdown" | METR (our ledger row E-23) |

## Overlap with our direction

| Our element | In this paper | Difference |
|---|---|---|
| "Accepted change" as the unit of output | Production-Qualified Change | Same idea, already named and defined |
| Cost per accepted change | "PQC per dollar"; also "PQC per reviewer-hour" | Same metric, plus one we lacked |
| Risk-tiered gates | Gate set varies by change class; risk-adaptive review | Same |
| Evidence bundle | "records the evidence required to qualify the result"; evidence coverage metric | Same intent; no format or mechanism given |
| Independent verifier | Raises it as a question (RQ3); warns about correlated error | The paper asks; we propose to measure |
| Measured false-pass rate of the verifier | Not present. Nearest is "escaped-failure rate" after release | Ours |
| Per-repo evaluation as the entry | Not present. Suggests "Private evals" as one control | Ours |
| Contract written before the run and protected from the agent | Not present | Ours |
| Delivered as a plug-in to existing harnesses | Says the control plane can start "as a policy and telemetry layer around" existing tools | Compatible; no design |
| A working implementation and measurements | None. "The purpose is not to claim that any one company has already implemented this complete control plane." | Ours to produce |

## Reading for our thesis

**Supports it**
- An independent author reached the same diagnosis from a wider evidence base, which makes the problem statement easier to defend to executives.
- It gives us citable vocabulary. Using "Production-Qualified Change" and "Verification Tax" with attribution is stronger than inventing our own terms.
- It states the CFO's question in the CFO's units: value "per dollar, per reviewer-hour, and per unit of operational risk".
- It names the gap we target: the verifier as "a first-class artifact", and the unanswered question of independence between generator and verifier.

**Cuts against it**
- The framing is public. We cannot claim the idea, the metrics or the control-plane concept as ours.
- The paper's control plane is broader than our evidence layer (model routing, stop rules, cost attribution), and overlaps with what Omnigent already ships. A buyer may want the whole control plane from one supplier.
- It offers no evidence that such a layer pays for itself. Its constructs are, in its own words, hypotheses.

**Useful for open questions**
- T7 (risk tiers and redlines): the autonomy budget and the gate-set-per-change-class give a published basis, replacing the formula from the article we could not find (ASSIST-012).
- T9 (prototype): its metric table is a ready reporting template. "First-pass qualification" and "evidence coverage" are worth adding.
- T2 and T3 (differentiation): what remains ours is narrow and concrete: a protected contract, a verifier whose false-pass rate is measured, and a working implementation.
