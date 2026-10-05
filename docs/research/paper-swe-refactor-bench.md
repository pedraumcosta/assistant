# SWE Refactor Bench

| | |
|---|---|
| Reference | arXiv 2608.23564, Hong et al., August 2026 |
| Source | https://arxiv.org/abs/2608.23564 |
| Read on | 2026-10-05, from the arXiv HTML full text |
| Method | Read end to end by a Claude Code sub-agent and checked against Pedro's notes. |
| Status | Digest with quotations. Figures marked as sums or subtractions were computed by the reader from the paper's numbers. |
| Used for | PLAN §3.11; PLAN §2.1 decisions T1 and T11; prototype design |

## Read record

- "SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?", arXiv:2608.23564v1, 24 Aug 2026, https://arxiv.org/abs/2608.23564
- Authors: Deyao Hong, Yizhe Chi, Wenyi Li, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na. Affiliation as printed: "Navers Lab, Einsia.AI Tsinghua University".
- Lines read: 1–3205 of 3205. End reached: Table 10 (Appendix C), then page chrome.

## What was studied

- Tasks: 20 whole-repository migrations of open-source projects (SQLite, zlib, libsodium, GraphHopper and others): language (7), framework (7), platform (3), build toolchain (3); "6 to 30 hours of autonomous work per task", offline.
- Agent input: the repository, a target-stack declaration, an instruction, and "an artifact contract saying what will be collected from the finished workspace". No tests are given.
- Models: claude-opus-5, claude-sonnet-5, gpt-5.6-luna, gpt-5.6-sol, kimi-k3, qwen3.8-max, dsv4-flash, glm-5.2. "The two GPT-series models use Codex as their harness; the other six use Claude Code."
- Runs: "8 models, 26 configurations and 520 scored runs"; one run per configuration per task.
- Success: three stages in series. Score = Stage I veto × Stage II all-or-nothing × (0.4 + 0.6·s/6), s being the number of verifiers finding no counterexample.

## Findings

1. "only 28 of 520 runs ( 5.4% ) pass all three stages, 13 of the 20 tasks receive no accepted solution". "The mean score over all 520 runs is only 13.44/100".
2. Best configuration per model: claude-opus-5 (xhigh effort, Claude Code), "5 acceptances in 20 runs and a score of 47.0; behind it are gpt-5.6-sol at 28.5, kimi-k3 at 19.5 and claude-sonnet-5 at 15.0". gpt-5.6-luna, dsv4-flash and glm-5.2 had no acceptances.
3. Two abilities: "30 runs preserved behaviour by skipping the migration, and were stopped at Migration Audit; 252 completed the migration but broke behaviour, and were stopped at Behavioural Tests." The 30 are "spread over 7 of the 8 models".
4. Last 1%: "Among the 340 runs that passed Stage I ... 91% get the fixed suite past half, 58% reach 99% and 36% reach 99.9% —but only 26% make no error at all."
5. Categories (all configurations pooled): scores 31.4 (build toolchain), 17.2 (platform), 12.0 (framework), 5.6 (language). Build toolchain has the lowest Stage III survival ("17.6%"); framework the highest ("56.0%"). "only 12 of 182" language runs reach Stage III.
6. Effort is not monotonic: Claude Opus 5 scores 47.0 at xhigh, 31.0 at max.

## How verification was done, and what it reveals

**Stage I, Migration Audit.** Per-repository criteria "written as prompt questions", "answered one by one by a model reading both source trees; every failing verdict must cite re-checkable evidence, and each criterion is judged three times independently, with the majority taken". The judge is gpt-5.6-sol. This is a model judgement, not a deterministic check. It catches what behavioural tests cannot: verbatim copies, shims over the original, half-done rewrites, transliteration.

**Stage II, Behavioural Tests.** "130,118 fixed checks recorded from the original system": "the recorded output becomes the expected answer". Deterministic; "a single wrong check scores zero". It catches broken behaviour; it cannot tell whether anything was migrated.

**Stage III, Agentic Verification.** "six coding agents, one hour each, each holding both source trees"; five probe an assigned direction, "the sixth is unrestricted". Output "cannot be a report, only an executable test case: passing on State A and failing on the submission, and it must first go green against the reference and then reproduce three times". It catches differences nobody anticipated.

**False passes of a behaviour-only check.**
- Not migrated, all fixed checks pass: 30 runs ("Stage II gives all 30 full marks; only Stage I stops them").
- Migrated, all fixed checks pass, then broken: "only 28 survived all six verifiers; the other 60 ( 68.2% ) had a counterexample found against them within the hour".
- "118 ( 22.7% ) passed every fixed check, but only 88 did both and thereby reached Stage III"; "With the fixed suite as the only instrument, 118 submissions would tie for first place". The paper gives the components (30 and 60 of 118, leaving 28), not a combined rate.
- Four tasks (lang01, fw01, fw02, fw07) look solved to a behavioural instrument and are unsolved under the protocol.

**The six agents and their reliability.** Two are claude-opus-5 (one directed, one unrestricted), break rates "55.7% and 53.4%, the other four between 21.6% and 26.1%". The other four models appear only as colours in Figure 6, absent from the text. "Changing prompt and effort within one model moves the break rate by about two points; changing the model moves it by thirty." Acceptance is panel-relative: "retire the two strongest and the remaining four would accept 46 submissions instead of 28. An accepted submission is therefore not a migration proven correct". Verifiers "broke 33.9%" of own-family submissions and "34.3% of everyone else's".

**Audit reliability.** "Of 3,536 criterion verdicts, 3,405 ( 96.3% ) had all three samples agree". Against two independent human researchers on 156 runs: "Judge and human agree 89.7% of the time ( 140/156, κ=0.795 )"; "of the 16 disagreements, 14 are the judge being too strict ... and only 2 go the other way".

**Other deterministic controls.** Evaluation assets in "a separate image that is never mounted into the agent's container"; an identity run in which "unless every behavioural module reaches 1.0 the build is refused".

## Check of Pedro's notes

- 20 whole-repository migrations — Confirmed.
- "only 28 of 520 runs (5.4%) pass all three stages" — Confirmed.
- 13 of 20 tasks without an accepted solution — Confirmed.
- Best model 47.0/100 — Confirmed; one configuration, claude-opus-5 at xhigh effort.
- Language 5.6 against build toolchain 31.4 — Confirmed.
- 58% and 26% — Confirmed: "among the 340 runs that pass Migration Audit, 58% reach 99% of the fixed checks, yet only 26% reach 100%".
- "Blindness" and the copy quote — Confirmed: "agents copy the original implementation to make tests pass. We call this Blindness".
- Three stages; six independent agents writing targeted tests — Confirmed.
- "completeness and correctness are distinct abilities" — Corrected: "Migration completeness and behavioural correctness are distinct abilities".

## Figures

- Mean score "over the 88 that reached Stage III" is 79.43.
- "the average submission holding off only 3.94 of the 6 verifiers"; "median time to a counterexample is 17.0 minutes".
- "140 runs land in [99%,100%), missing a median of 12.5 checks, and 18 of them miss exactly one."
- Cost, USD per task (Table 3): Claude Opus 5 xhigh 74.9; GPT-5.6 Sol max 143.5; GPT-5.6 Luna max 2.8.
- Blindness by class (Table 4): framework 15, language 9, platform 4, build toolchain 2.
- Per task (Table 9): build03 64.62, pf03 49.23, fw06 43.08; 9 of the 28 acceptances are on fw06 (803 LoC).
- Conversion: tables are flattened one cell per line but readable; Table 2's stacked headers and Table 8's interleaved halves need care. Figures 3, 5 and 6 are captions only.

## Relevance to the two theses

**(a) Thesis B.** No brownfield practice is tested: zoning, comprehension memos, characterization-first workflows and harness memory are not in the text. Harness is confounded with model, so no harness effect can be read. The evidence points to model capability: gaps between models are large, and for the verifier role the model matters "an order of magnitude more than its configuration". The human-written inputs (audit criteria, instruction, allow and deny lists, recorded suite) served the evaluation, not the agent; whether giving agents the recorded suite would help is untested.

**(b) Thesis A.** Strong support for the premise: a behaviour-only verdict passes 118 runs where the full protocol accepts 28. The remedy partly matches thesis A: requirements, scope and an "artifact contract" fixed before the run, deterministic checks recorded from the owner's own system, and a measured error rate for the judge. It also departs from it: the scope check is a model judge, and the residue is found by agents, although each rejection must be an executable, reproducible counterexample. Deterministic checks alone would have let the 60 broken runs through.

**(c) First market.** Supportive. "The original system provides a behavioural reference, so correctness can be tested without a separate specification", and the failure measured is in verification, not in tooling for old code. Nothing is said about legacy-specific assistance.

## Cautions

- Stated limit: results "do not rank the intrinsic difficulty of all migration projects".
- One run per configuration per task; no variance. Three tasks each for platform and build toolchain.
- Open-source infrastructure with rich observable interfaces, not enterprise legacy systems.
- The audit judge (gpt-5.6-sol) and the strongest verifier (claude-opus-5) are also contestants; the paper argues there is no bias.
- Human validation covers 6 tasks; "6 tasks spanning the four migration classes, three tasks each" is internally inconsistent.
