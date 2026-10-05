# Decision models (Jev) in a coding-agent harness and in our evidence layer

| | |
|---|---|
| Origin | Pedro's addendum of 2026-10-02 on TypeSafe's Jev and the economics of model calls in a harness, given to the project on 2026-10-05 with the question: could this be used to enhance an assistant? |
| What this file is | The overview: what a decision model is, what the check confirmed and corrected, and our reading of where it fits. Detail is in `check-decision-model-product.md` and `check-decision-model-risks.md`. |
| Method | Two Claude Code sub-agents checked the claims on 2026-10-05 in raw source pages; one paper was read in full. The reading in the last two sections is ours. |
| Status | The product is three weeks old. Independent evidence is thin, and none of it concerns judgments about code. |
| Used for | PLAN §3.10, PLAN §2.1 decisions T3, T7 and T9 |

## What it is

Jev is TypeSafe AI's "System One" decision model, launched in early access on 2026-09-15. Instead of generating text it returns one option from a fixed set, with a confidence. The vendor's stated price is "$0.042 / MTok" for input, with output "FREE".

A decision model in general (several open reimplementations exist, on small open models) guarantees a valid label. It does not guarantee a correct one. The vendor's wording is "Schema matching is guaranteed".

## What the check confirmed and corrected

| In the notes | Finding |
|---|---|
| Launched 2026-09-15; price; text only | Confirmed |
| 64K context | Corrected: "64k tokens per request; 32k tokens for `state` plus the longest question" |
| Closed weights, hosted only | Confirmed in effect. One endpoint; "The Services are hosted in the United States"; no self-hosted or private-cloud option found. Protections are contractual (no training on input; zero retention for enterprise customers). |
| Mechanism: restricted softmax over label token IDs | Not the vendor's description. The architecture is unpublished. The phrase fits one open reimplementation. |
| About 146 open builds | The four named projects exist; no source for the number |
| 242 ms against 1,511 ms and 82 times cheaper, n=40 | No public source. Treated as Pedro's own unpublished measurement. |
| Vendor ceiling claims of 200× and 400× | The vendor's figures are "193.6x Faster, 444.6x Cheaper", on four vendor-written workflows scored against labels averaged from two other models |
| LangChain: 100% agreement with the oracle; 92–913× lower variance | Confirmed with scope: five frozen runs of a weather agent, 100 repetitions each, one human reviewer's labels. "Jev matched the oracle on all 500 repeated decisions." The variance figure is for a continuous score, not pass/fail. LangChain: "not a general ranking of judge accuracy". |
| Arize "cascade" | The post is commentary with no experiment of its own |
| BAML integration shipped (PR #4906, `.feels()`) | PR #4906 was closed unmerged; its successor merged on 2026-09-19. `.feels()` is a demo library, not part of the integration. |
| Claude Code / OpenCode hook wiring is an open issue | Closed on 2026-10-02; shipped as an example hook runner in a third-party project |
| Raw confidence overconfident by 6.7 to 15.3 points | Confirmed as mean confidence minus accuracy, for two question types on one constructed dataset. Isotonic regression cut calibration error from "0.117" to "0.008"; "a few hundred labeled examples is enough to get most of the benefit". |
| Judges "wrong in the same places" as LLM judges (arXiv 2609.29769) | Confirmed for text rubrics. "On Jev's most confident errors, 96.0% of LLM verdicts repeat its answer, against 50.3% under independence." No code-related judgments were tested. |
| "Deterministic checks first" follows from that paper | The notes' inference, not the paper's recommendation. The paper says: "Use a Jev-first cascade to lower cost, and expect little gain in accuracy". |
| RouteLLM: 95% of quality at 26% of cost | Corrected: 26% is the share of calls sent to the stronger model |
| Granite Guardian 3.2 does function-call risk | Corrected: it detects malformed or hallucinated function calls, not whether an action is risky |
| 14–21% spend recovery at 10,000 seats | Modelled, not measured: an Accenture preprint (arXiv 2609.28919) on an emulated enterprise; its second version says "13 to 21%" |
| Still unclaimed: (a) a shipped coding harness with a decision model as the main economic layer and end-to-end cost per task; (b) closed-loop recalibration of gate thresholds from harness outcomes | No counter-example found for either. (b) appears only as proposed future work in one paper. Both negatives rest on a few searches. |

## Could it enhance an assistant?

**Technically yes, for cost and latency.** The call sites in the notes are real: tool-risk gating, loop control, model routing, context triage, sub-agent triage. A cheap, fast, low-variance classifier is a sensible fit for each.

**It is not ours to build, and it is not open ground.** These call sites sit inside the harness, which this project has decided not to build. The harness paper shows vendors already make cheap classifier calls at these points (Gemini CLI's router with a local model option, Codex's approval reviewer, Hermes's 16-token approval gate). The notes' own verdict is that the components are crowded.

**It does not make an assistant more accurate.** The one substantial study finds a decision-model-first cascade lowers cost and gains almost nothing in accuracy, because the decision model and the fallback judge fail on the same cases.

## Where it fits our evidence layer

**Not as the verdict on whether a change is correct.** Our claim is a deterministic verdict from the customer's own checks. A decision model is a model's judgment, and the evidence is that it is not independent of other model judges.

**As a component, in three places:**

1. *Risk tiering.* Classifying a change to decide which gates it needs and whether a human sees it. Rules on paths and size miss what a classifier can catch.
2. *Criteria with no executable check*, as the middle step of a cascade: deterministic checks, then a decision model, then a stronger judge or a human. Low run-to-run variance matters for a gate.
3. *Triage*, such as whether a failing test is real or flaky.

**The strongest link is calibration.** A decision model's raw confidence is overconfident, and a few hundred labelled examples fix most of that. Our layer produces exactly those labels on each repository: the deterministic outcome of every change, and every human override. The deterministic verdict would supply the ground truth that makes a cheap classifier trustworthy on that repository. No shipped product was found doing this.

**Three constraints**

- *Tenancy.* Jev is hosted only, in the United States. Using it sends the customer's diffs to a new vendor, which gives up the advantage of running entirely in the customer's environment (PLAN §3.8). A self-hosted open build would keep that advantage; the one accuracy comparison found is self-reported and mixed.
- *Size.* About 32,000 tokens for the material being judged. A large diff with its contract may not fit.
- *No moat.* The idea is reproducible on small open models. The asset, if there is one, is the calibration data, which belongs to each customer's repository.

**On the margin argument in the notes.** It was made for a governance layer, which this project has dropped. In the evidence layer the always-on path is the customer's own checks running in their CI, so our cost is not indexed to token prices to begin with. A decision model makes the judgment tier nearly free, which helps at the edge. It does not answer the open question, which is whether buyers will pay.
