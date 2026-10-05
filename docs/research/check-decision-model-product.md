# Check of the claims about the Jev decision model

| | |
|---|---|
| Notes dated | 2026-10-02 |
| Checked on | 2026-10-05 |
| Method | Each claim checked at vendor documentation, the vendor blog, GitHub and the cited third-party posts by a Claude Code sub-agent, with figures confirmed in the raw page. |
| Status | Record as received. Vendor performance figures are the vendor's own. The architecture is unpublished. |
| Used for | PLAN §3.10 |

Tags in this file: **[P]** confirmed in the publisher's raw page; **[P-summary]** seen only through a summarising fetch or a reader proxy; **[S]** secondary source or search snippet only.

Checked 2026-10-05. The product exists: TypeSafe AI's "Jev", a "System One" model, with a vendor site, docs, legal pages and a large third-party ecosystem. Tags: **[P]** confirmed in the publisher's raw page (curl + grep); **[P-summary]** publisher's page not seen raw; **[S]** secondary only. GitHub figures are from the GitHub REST API on 2026-10-05.

### 1. Identity, pricing, API, limits, deployment

**Finding: Partly confirmed** (identity, date and price confirmed; "64K" needs a qualifier; "closed weights, hosted only" is inferred from absence, not stated by the vendor).

- **Launch.** Vendor post "Introducing System One Models & Jev", dated "Sep 15, 2026", by founder Diogo Almeida: "Our first public model is Jev, available today in early access." https://typesafe.ai/blog/introducing-system-one-models-and-jev [P]
- **Price.** "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)." The models page gives the same price for `jev-1.13.0`. https://docs.typesafe.ai/models [P]
- **Promotional?** Not described as promotional. The vendor says: "We can't prove it isn't subsidized; we'll need the long-term to prove the sustainability of our pricing (which we expect to go down, not up)." `https://typesafe.ai/pricing` returns 404. [P]
- **API.** One endpoint, `POST https://api.typesafe.ai/v1/systemone`. Input: a `state` (string, JSON object or array of text) plus a map of typed questions, each with `instructions` and `criteria`. Three question types:
  - **Noul** returns `noul`, a number from 0 (no) to 1 (yes), with no separate confidence field.
  - **Choice** returns `choice` ("The highest-probability option"), `probabilities` for every option ("floats that sum to 1") and `confidence`. "You can have a maximum of 255 options per Choice."
  - **Score** returns a probability-weighted `score`, `legend`, `probabilities` per level and `confidence`.
  
  The response also carries the versioned `model` ID and `usage`. https://docs.typesafe.ai/api [P]
- **Limits.** "Context length | 64k tokens per request; 32k tokens for `state` plus the longest question"; "Rate limits | 100K tokens per second / 80 requests per second", which "can change without notice"; "Text only... No image, audio, or video input." English is the primary training language. https://docs.typesafe.ai/models [P]
- **Regions and retention.**
  - "The Services are hosted in the United States". https://typesafe.ai/legal/privacy-policy [P]
  - The launch post says evals are run "from our laptops on the West Coast (this is where our service is currently based)". [P]
  - "We will not train or fine tune any artificial intelligence or machine learning models on your prompts or other Input." (privacy policy) [P]
  - No fixed retention period is published; the DPA says data is retained "for as long as necessary". [P]
  - "We also offer zero data retention (ZDR) for enterprise customers." https://docs.typesafe.ai/legal [P]
- **Self-hosting, VPC, weights.** I found no self-hosted, on-prem or VPC option and no weight release anywhere in the docs (`llms-full.txt`), site or legal pages. The docs say "the same weights serve every account". The customer agreement forbids using the service to "perform model distillation" or to "reverse engineer". The SDK docs show routing through OpenRouter as a gateway, which is still hosted. The vendor never uses the words "closed weights" or "hosted only". [P]

### 2. Mechanism and open reimplementations

**Finding: Corrected.** "Restricted softmax over label token IDs" is not the vendor's description and is not established for Jev. It describes how some open builds work. "~146 open builds" could not be verified.

- **Vendor.** "a new model architecture, parallel sampler... and training method we call Reinforcement Learning for Calibrated Decisions (RLCD)"; "Jev outputs all probabilities in parallel instead of autoregressively generating by token." The architecture is unpublished. [P]
- **Independent analysis.** Archer Hume, "Jev's Architecture Unmasked" (17 September 2026), a self-described "quite speculative" black-box study: "The evidence points to a direct numerical readout... Reserved label tokens remain possible, although the fake-option test there weighs against them." "Which pretrained model is unknown". https://archerhume.com/posts/jevs-architecture-unmasked [P]
- **Open builds.** All four named projects exist:

| Repo | Stars | Base model and method |
| --- | --- | --- |
| `TheoLeeCJ/SemIf-OpenJev` ("formerly called OpenJev") | 4,701 | Frozen Qwen3.5-4B; "one forward pass reads declared option logits; no answer token is sampled" (this is the restricted-readout approach) |
| `jaredpalmer/kev` | 8,482 | Qwen3.5-0.8B/4B/9B-Base and Qwen3.8-27B; "a rank-16 LoRA adapter and a small pointer head" |
| `NandhaKishorM/laya` | 30,873 | Encoders: ModernBERT-large (421M) and mmBERT-base (322M) |
| `TianyuCodings/NanoJev` | 2,494 | "Qwen3-0.6B with decision heads"; "Choice uses set attention and a softmax" |

  All [P] (READMEs and API).
- **The "~146" count.** No source found. A GitHub repository search for `openjev` returned 134. Two community lists claim 981 and 1,207 projects built *with* Jev, which is a different thing from reimplementations.

### 3. "~242ms vs ~1,511ms, ~82× cheaper, n=40" and the 200×/400× claims

**Finding: Could not verify** the n=40 measurement; **Corrected** for the vendor figures.

- **n=40 measurement.** I found no public source for 242 ms, 1,511 ms, 82× or n=40. They are not in the "ai that works" episode #75 "All About Jev" (2026-09-22): I grepped the README, email and transcript at https://github.com/ai-that-works/ai-that-works/tree/main/2026-09-22-all-about-jev [P]. Treat it as the Pedro's own unpublished measurement.
- **Vendor multipliers.** The exact home-page claim is "193.6x Faster, 444.6x Cheaper. *based on workflows for System One tasks", with "Cost $0.000081 / Completed in 0.114s" against LLMs at "Cost $0.013880 / Completed in 8.566s". https://typesafe.ai/ [P]
- **What they compare.** Four vendor-written workflows, with LLMs called through TypeSafe's own "System One LLM wrapper". Reference labels are "the average of GPT-6 Astra and Fable 5.1", not human ground truth. The vendor adds: "we expect that these are on the higher end of real world gains", and the workflows "were made by individuals on our model capabilities team, so some bias could exist." The launch table says "40x-200x faster". [P]
- **"200×/400×"** is a third-party rounding (LangChain: "up to 200x faster inference and 400x lower cost").

### 4. LangChain

**Finding: Confirmed, with scope clarified.** "Jev-as-a-Judge for Agent Evals", Daniel Shea and Seán Roche, September 20, 2026. https://www.langchain.com/blog/jev-agent-evals-langsmith (langchain.com and blog.langchain.com both redirect here); repo https://github.com/danielgshea/jev-as-a-judge [P]

- **Task.** A Deep Agents weather agent; "The test set consists of five weather requests". The five captured runs were frozen, and each judge scored them "100 times" on `quality` (continuous) and `does_pass` (binary).
- **Oracle.** One human reviewer's labels.
- **Baselines.** GPT-5.6 Luna, GPT-5.6 Terra and Claude Sonnet 4.6 at provider defaults.
- **Accuracy.** "Jev matched the oracle on all 500 repeated decisions. Terra matched on 99.8% of decisions, Luna on 96.4%, and Claude on 80.0%."
- **Variance.** Measured on the continuous `quality` score, not on pass/fail: "lowest observed mean per-case variance: 0.0000149. Luna was 433× higher, Terra was 913× higher, and Claude was 92× higher."
- **Cost and latency.** Jev "$0.00035" per call, "0.44 s", "$0.34" total; Claude "$28.17" total.
- **Caveats.**
  - "This is a small corpus with five agent runs and one human reviewer... it is not a general ranking of judge accuracy." (README)
  - "the result is observational".
  - "a consistently wrong evaluator can produce bad feedback at scale".
  - "The Jev service version was not available in the experiment metadata."

### 5. Arize

**Finding: Corrected.** The Arize post reports no experiment of its own and does not use the word "cascade". "TypeSafe Jev: Can Decision Models Replace LLM Judges?", published 2026-09-18. https://arize.com/blog/typesafe-jev-llm-judge [P-summary: the raw page returned 403 (Cloudflare challenge); I read the full text through the r.jina.ai reader proxy.]

- "Arize will be running our own benchmarks just as soon as we can."
- It relays TypeSafe's evals: "Jev lands at 68% accuracy at $0.0004 and 0.4 seconds per case. GPT-5.6 Terra is at 68% for $0.03 and 10 seconds. Opus 5 is at 73% for $0.18 and 38 seconds."
- It cites three small third-party tests (Every; NearHere, "96% from Jev against 86% from Gemini Flash-Lite"; a spam evaluation, "98.3%" against "98.4%" for TF-IDF logistic regression). All are [S] here.
- **The pattern it describes** is a hybrid: "Run a decision model on every trace for coverage. Sample failures and uncertain scores through an LLM judge when you need a written explanation".
- On the "can't hallucinate" claim: "Jev can't return an answer outside the schema you gave it. Within that schema, it could still be giving the wrong answer".

### 6. BAML

**Finding: Corrected.** PR #4906 did not ship, and `.feels()` is not part of the integration.

- PR #4906, "Add TypeSafe AI System One provider", is closed with `merged: false` (closed 2026-09-18), with the comment "Superseded by #4938". https://github.com/BoundaryML/baml/pull/4906 [P]
- PR #4938, "feat: add TypeSafe JEV client, implemented with reflection", merged 2026-09-19 into `canary`. https://github.com/BoundaryML/baml/pull/4938 [P]
- The blog post (2026-09-17) is titled "TypeSafe AI's Jev model is coming to BAML v1" and says "starting with the next BAML v1 nightly... it is not available in earlier releases." I did not confirm a nightly containing it. https://boundaryml.com/blog/typesafe-ai-jev [P]
- **What it does.** `client: "typesafeai/jev-latest"` maps return types to questions: `bool` and `float` to Noul, enums and literal unions to Choice, and classes to one question per leaf field. Unsupported shapes (`string`, `int`, lists, media, tools) fail before HTTP.
- `.feels()` comes from the podcast: "Vaibhav built a BAML library where every type gets a `.feels()` method backed by Jev". It is a demo. [P]

### 7. jev-mcp#51

**Finding: Corrected.** The issue is closed, not open; "not a product" still holds.

- `jkudish/jev-mcp` is a third-party MIT project with 496 stars: "Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools" (twelve tools, including `jev_decide`, `jev_review` and `jev_gate`). [P]
- Issue #51, "Route and gate tool calls from harness hooks (Claude Code, Codex, OpenCode, pi)", was opened 2026-09-30. It asks for an `examples/hook-gate.mjs` PreToolUse runner that calls `jev_decide`.
- State: **closed 2026-10-02T20:01:15Z**. The owner wrote: "This shipped with v0.13.0 as a source-checkout example. The runner is deny-only, with optional human escalation and wiring docs for Claude Code, Codex, OpenCode, and pi." The gate fails open: "A Jev outage never blocks the agent". https://github.com/jkudish/jev-mcp/issues/51 [P]

### 8. Independent evaluation; use in coding agents

**Finding: Partly confirmed.** Small independent tests exist. I found no published use in an established code-review product.

- **Tool-call risk benchmark** (webofmike, 2026-09-19/20): 60 hand-labelled tool calls. "91.7% (55/60)"; clear 100%, ambiguous 71.4%, adversarial 91.7%; p50 421.6 ms; ECE 0.0712 with "50 of 60 predictions" in the top bin. "There is no frontier-LLM baseline in these numbers." https://dev.to/webofmike/i-benchmarked-jev-on-agent-tool-call-risk-calibration-held-49i3 [P]
- **Hume essay:** "MMLU-Pro accuracy was 84.6%"; on 1,200 MMLU items "expected calibration error was 0.0313"; reversing option order moved one probability "from roughly 0.84–0.89 to 0.93–0.96". [P]
- **Coding agents.** Vendor docs: "Jev is **not** a drop-in replacement for the LLM behind Claude Code, Cursor, opencode". Only community projects exist: `dzhng/jevgrep` (2,290 stars; self-reported "25.8% lower total cost with the same 8/10 tasks solved"), `tamaratran/fast-jev-compaction` (7,410), `devagrawal09/jev-review` (670). All [P], all self-reported. On the podcast, Dex called his code-search harness "absolutely an abuse of Jev."

## What a decision model can and cannot do

- **Inputs.** Text only: a `state` plus typed questions with written criteria. No images, audio or tool calls.
- **Outputs.** A yes/no probability, one of up to 255 options you defined, or a rubric score, each with a probability distribution. No text, no arguments, no explanation: "System One models do not write replies, produce code, or generate explanations of their reasoning."
- **Guarantee.** Schema validity only. The vendor's 0% figure "is not empirical. Schema matching is guaranteed".
- **No guarantee of correctness.** "Calibration is measured across groups of predictions; it does not guarantee that an individual answer is correct." The vendor's own evals put it at 68% against model-generated reference labels (per Arize).
- **Confidence.** `confidence` is "a statistic computed from the probability distribution", not a separate correctness estimate. The vendor's "jaggedness" page says score levels "are weak in numerical calibration", option order can matter ("leans toward the option that comes first"), and injected content "can move the answer". Thresholds must be set on your own labelled data.
- **Known weak areas** (vendor): counting, arithmetic, date comparison, multi-hop indirection, and large irrelevant state ("Jev suffers from context rot").
- **Context.** 64k tokens per request, but 32k for state plus the longest single question.
- **Deployment.** Hosted API in the United States only. Customer data must leave the customer's environment. Mitigations are contractual (no training on input; enterprise ZDR). The only on-premises route is an open reimplementation, which is a different model.

## Summary

| Claim | Verdict | One line |
| --- | --- | --- |
| 1. Identity, price, limits | Partly confirmed | Launched 2026-09-15; $0.042/MTok input, output free; 64k per request but 32k for state plus longest question; hosted in US, no self-host found |
| 2. Mechanism, ~146 open builds | Corrected | Architecture unpublished; "restricted softmax over label tokens" fits open builds, not shown for Jev; "146" unsourced |
| 3. 242 ms / 1,511 ms / 82× (n=40) | Could not verify | No public source; vendor's figures are 193.6x faster and 444.6x cheaper on its own workflows |
| 4. LangChain | Confirmed | 500/500 pass/fail agreement on 5 runs × 100 reps; 92–913× applies to quality-score variance |
| 5. Arize | Corrected | Commentary only, no own test; hybrid "Jev on every trace, sample to an LLM judge", no "cascade" |
| 6. BAML PR #4906, `.feels()` | Corrected | #4906 closed unmerged; #4938 merged 2026-09-19; `.feels()` is a podcast demo |
| 7. jev-mcp#51 open | Corrected | Closed 2026-10-02; shipped in v0.13.0 as a deny-only example |
| 8. Independent evals, coding-agent use | Partly confirmed | n=60 tool-risk test at 91.7%; community plugins only, no established code-review product |
