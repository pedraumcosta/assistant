# An Empirical Study of Harness Design for Coding Agents

| | |
|---|---|
| Authors | Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang, Kaiqiang Song, Fei Liu, Hamed Zamani, Xiaoyang Wang |
| Reference | arXiv 2609.20804, submitted 2026-09-17 |
| Source | https://arxiv.org/abs/2609.20804 |
| Read on | 2026-10-05, from the arXiv HTML full text |
| Method | Read end to end by a Claude Code sub-agent, including references and appendices. The main session read the abstract directly. |
| Status | Digest with quotations. Accuracy differences marked as subtractions were computed by the reader from the paper's table cells and are not figures the authors state. Each setting was run once; all four models are open-weight. |
| Used for | PLAN §3.8 (wording of the "commodity loop" claim), prototype design |

## Read record

- **Paper:** "An Empirical Study of Harness Design for Coding Agents", arXiv:2609.20804v1 [cs.AI], 17 Sep 2026.
- **Authors:** Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang, Kaiqiang Song, Fei Liu, Hamed Zamani, Xiaoyang Wang.
- **Affiliations as converted:** UMass Amherst, Emory University, UNC Charlotte, and one blank entry. A footnote says "Work completed during internships at Zoom Video Communications", so the blank is probably Zoom. The author-to-affiliation mapping was lost.
- **Lines read:** 1-2842, the whole file. Body is lines 152-1197, References 1199-1591, appendices 1593-2787. I reached and passed the References.
- No instructions embedded in the text were acted on.

## Design of the study

- **Fixed loop.** A lightweight ReAct harness built on LangGraph. Benchmarks run through Harbor, "which owns each task's container and verifier".
- **Held constant:** workspace guard, read-before-write check, permission layer, tool errors returned as observations, post-edit diagnostics (ruff, pyflakes or a syntax fallback), stuck detection, temperature 0, at most 300 steps per task, tool results truncated to 24k characters.
- **Planning (2 variants).** On: system instruction, first-turn reminder, an `update_plan` tool, plan re-injected each turn. Off: all removed. This estimates "this persistent planning scaffold rather than the effect of planning as a general reasoning strategy".
- **Action space (2 variants).** Predefined tools: `read_file`, `write_file`, `edit_file`, `list_files`, `glob_files`, `grep_text`, `web_fetch`, `bash`. Bash-only: `bash` plus the auxiliary `update_plan` and `recall_event`. The swap also changes prompts, file-state tracking and automatic diagnostics.
- **Context management (5 tiers).**
  - T0: none; the run terminates on overflow.
  - T1: elision of stale tool observations.
  - T2: elision plus external storage and `recall_event`.
  - T3: LLM summarization alone.
  - T4: elision at a soft threshold (0.6 of the window), then summarization at a hard threshold (0.85).
- **Models:** Nemotron-3 30B, Nemotron-3 120B, Nemotron-3 550B, Mistral-Medium-3.5-128B, served locally.
- **Benchmarks:** SWE-Bench Verified (500 issues) and Terminal-Bench 2.1 (89 tasks).
- **Context-window budgets:** 32k, 64k, 96k, 128k tokens.
- **Settings:** 20 context settings plus 2 ablations (planning off, bash-only, both only at T4/128k) gives 22 per model-benchmark pair, 176 in total.
- **Runs:** "Each setting is run once per task."
- **Statistics:** two-sided exact McNemar tests, Benjamini-Hochberg correction at 0.05.
- **Cost:** mean dollars per task at OpenRouter prices per 1M input/output tokens: "$0.05 / $0.20 (Nemotron-3-30B), $0.08 / $0.45 (Nemotron-3-120B), $0.50 / $2.20 (Nemotron-3-550B), and $1.50 / $7.50 (Mistral-Medium-3.5)".

## Findings

1. **Context management matters most when the window is tight.**
   - Averaged across models, the managed-minus-T0 gap shrinks "from 35.7 to 15.9, 5.5, and 2.7 percentage points on SWE-Bench, and from 9.5 to 7.5, 4.8, and 2.8 on Terminal-Bench" across 32k, 64k, 96k, 128k.
   - The T0 overflow rate "falls from 78.7% to 8.7% on SWE-Bench and from 61.0% to 12.1% on Terminal-Bench, while all managed tiers have zero overflow failures".
   - At 128k on SWE-Bench, Nemotron-3 550B still gains significantly on every managed tier (T0 59.80; T1-T4 65.20 to 67.40). Mistral does not (T0 67.40; T4 68.60).
2. **T4 is the cheapest managed tier at similar accuracy:** "the lowest cost in seven of eight model-benchmark panels".
3. **Recall is rarely used and does not help.** "T2 outperforms T1 in 15 settings, underperforms in 14, and ties in three; the equal-weight mean difference is -0.36 percentage points." Also: "Among the 64 T2 and T4 settings, 36 (56.3%) never call recall_event."
4. **Planning is an accuracy scaffold for the weakest model and a cost saver for the strongest (T4/128k, full tools).**
   - Nemotron-3 30B: planning "increases success rate by 11.6 percentage points on SWE-Bench and 4.5 points on Terminal-Bench, at higher cost". SWE-Bench cells: 25.20 at $0.09 with planning, 13.60 at $0.02 without. Only this SWE-Bench contrast is significant.
   - Nemotron-3 120B: "no consistent success-rate gain".
   - Nemotron-3 550B and Mistral: on SWE-Bench "costs fall by approximately 30% and 32%, respectively, while success rates decrease by 2.0 and 0.4 percentage points". The decreases are not significant.
   - Mechanism: without planning, 68.6% of 30B SWE-Bench runs end without an edit (27.8% with). For strong models, planning cuts median turns "from 108 to 74" (550B) and "from 68 to 53" (Mistral), mostly post-edit verification.
5. **Predefined tools scaffold weak models; bash-only can be better and cheaper for strong ones.**
   - Nemotron-3 30B: the tool set "raises success by 15.0% on SWE-Bench and 10.1% on Terminal-Bench". These are percentage points: 25.20 against 10.20, and 13.48 against 03.37.
   - Nemotron-3 120B: gains "shrink to 1.6% on SWE-Bench and 4.5% on Terminal-Bench".
   - Nemotron-3 550B: "bash-only improves success rate by 3.6% on SWE-Bench and 5.6% on Terminal-Bench while reducing cost by 53% and 30%". Only the SWE-Bench contrast is significant.
   - Mistral: "The full tool set improves success by 23.2% on SWE-Bench, but bash-only adds 6.7% on Terminal-Bench." Cells: 68.60 against 45.40 (significant), and 37.08 against 43.82 (not significant).

## Model versus harness

The paper makes no head-to-head claim about which is larger. Its conclusion is conditional: "Harness design is thus a conditional systems problem in which each component should be selected for the target model, task type, and resource budget rather than adopted as a default."

The Pedro's phrase most likely comes from a Related Work sentence describing prior work, not this study: "Research on their design has shown that the harness, not the model alone, governs performance (Yang et al., 2024)." That says "not the model alone"; it does not say "more than the model".

The tables allow a comparison. The subtractions are mine, from the quoted cells; the paper does not present them.

| Comparison (SWE-Bench Verified) | Cells | Difference |
|---|---|---|
| Model swap, default harness (128k, T4) | 30B 25.20; Mistral 68.60 | 43.4 points |
| Largest model swap in one setting (128k, T4 bash-only) | 30B 10.20; 550B 69.40 | 59.2 points |
| Largest harness effect (context management at 32k, Mistral) | T0 12.60; T2 66.20 | 53.6 points |
| Largest harness effect at 128k (action space, Mistral) | tools 68.60; bash-only 45.40 | 23.2 points |
| Planning, largest effect (30B) | on 25.20; off 13.60 | 11.6 points |
| Context management at 128k, largest effect (550B) | T0 59.80; T2 67.40 | 7.6 points |

- **In a working configuration, the model effect is larger.** At 128k with a managed tier, swapping the model moves accuracy by about 40 points. Harness components move it by single digits to 23.2 points.
- **A broken harness can erase the model.** The 50-point effect at 32k is almost entirely overflow avoidance.
- **Harness choices can reorder models.**
  - At 32k with T0, Nemotron-3 550B scores 06.40, below Nemotron-3 30B at 09.40.
  - With full tools Mistral (68.60) beats 550B (65.80). With bash-only, 550B (69.40) beats Mistral (45.40).
- **Terminal-Bench shows the same pattern.** Largest model swap: bash-only, 03.37 against 50.56. Largest harness effect: Mistral at 32k, 21.35 against 42.70.

**Verdict: not supported as worded.** The text supports a weaker statement: harness components have large effects that depend on model and budget, can be decisive when misconfigured, and can change which model wins.

## Figures

- **Recall usage.** Mean calls per task fall "from 0.540 calls per task at 32k to 0.069, 0.011, and 0.007 at 64k, 96k, and 128k".
- **Planning, Table 5 (off to on; SWE-Bench turns / tool calls / average input tokens).** 30B: +293.2%, +474.0%, +104.1%. 550B: -24.3%, -24.5%, -12.4%. Mistral: -23.2%, -23.3%, -15.1%.
- **Planning, 30B.** "Disabling planning reduces the median SWE-Bench trajectory length from 40 to 5 turns."
- **Bash-only, 30B.** "On Terminal-Bench, 66% of bash-only trajectories terminate after such out-of-interface emissions, shortening the average trajectory from 71 to 15 turns."
- **Bash-only, 550B.** Trajectories "issue 32% fewer calls on SWE-Bench and 24% fewer on Terminal-Bench"; median largest edit "grows from 18 to 54 lines".
- **Bash-only, Mistral.** "32.8% of Mistral's bash-only SWE-Bench runs end without editing a file, versus 1.2% with the full tool set"; file-localization failures rise "from 16.0% to 41.4%".
- **Failure stages.** For 30B, "more than half of unresolved runs fail at file localization"; for 550B and Mistral, "the majority reach the correct file and lines but fail at patch implementation".
- **Cost per task at T4/128k, SWE-Bench:** 30B $0.09, 120B $0.34, 550B $2.33, Mistral $3.14. 550B bash-only: $1.11.

Conversion flags:

- Tables 3, 4 and 10-13 are flattened one cell per line: readable with care, but bold "best" markers are lost.
- One sentence is truncated at line 1060 ("rises from 16.0The Mistral result"); the appendix supplies "16.0% to 41.4%".
- Figures are captions only, so "seven of eight panels" cannot be checked.

## Relevance to our thesis

**(a) "Commodity loop" wording.**

- The paper fixes the loop and never varies it, so it neither confirms nor refutes the claim about loop sophistication.
- It does show that what sits around a plain ReAct loop is not interchangeable.
- Suggested wording: "The inner loop is simple and widely replicated; the components around it (tool interface, planning scaffold, context policy) have large effects that depend on the model, the task type and the context budget, so no configuration is a safe default."

**(b) Scaffolding value as models strengthen.**

- Partly supported: planning and predefined tools move from accuracy aids to overhead. For 550B, bash-only is more accurate and 53% cheaper on SWE-Bench.
- Not monotonic: Mistral loses 23.2 points on SWE-Bench without predefined tools, and 550B still gains from context management at 128k.
- The authors warn that "Model size is only an imperfect proxy for capability".
- Better wording: scaffolding value changes in size and sign by model and task.
- This strengthens the case for per-pairing measurement. The best configuration and the reliability figure both move with the model, and crossovers "should therefore be validated before being transferred to other model families".

**(c) Prototype guidance.**

- Never run unmanaged at small windows. Use a 128k budget or simple elision of stale tool output; skip recall.
- Return tool errors as observations, cap steps, and add identical-call stuck detection.
- One shared harness across both arms confounds the comparison.
  - A weaker model needs typed file and search tools plus a plan scaffold; with bash-only it collapsed to 10.20 on SWE-Bench.
  - A strong model may do better and cheaper with bash-only and no plan.
- Log "ended without an edit" and turn count per run, to separate harness-induced failure from model failure.

**(d) Verification and outcome evaluation.**

- Nothing on verifier quality, false passes or production qualification. Success is the benchmark verifier's pass rate.
- Cost is mean cost per task; cost per solved task is not reported.
- The nearest material: stronger models spend many turns on redundant post-edit self-verification. In-loop lint diagnostics are held fixed, not evaluated.

## Cautions

- **Single run per task.** There is no variance estimate. Several headline directions are not significant: the planning accuracy loss for strong models and every Terminal-Bench bash-only gain.
- **Terminal-Bench is small.** Conclusions there "rest on consistent directions across models and budgets rather than on individually significant cells".
- **Narrow ablation coverage.** Planning and action space are ablated only at T4/128k, so interactions are unknown.
- **Models.** Four open-weight models, three from one family, and no frontier proprietary model. Extrapolating to the models our customers use is unsupported.
- **Benchmarks.** SWE-Bench Verified is Python-only. Contamination and test-quality concerns come from our own earlier research, not from the paper; the paper only excludes web search to avoid exposing the ground-truth patch.
- **Judge.** Trajectory labels come from an LLM judge; Terminal-Bench agreement was as low as 79.8% in one split.
- **My arithmetic.** The model-versus-harness differences are my subtractions from table cells, not figures the authors report.
