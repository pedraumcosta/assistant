# Market structure and agent limits: evidence from Pedro's notes, at public sources

| | |
|---|---|
| Origin | Six pointers Pedro gave on 2026-10-05 into his own notes on market analysis and the limits of coding agents |
| What this file is | The overview: which of those claims are usable as evidence, each cited to its public source, with the corrections found. Detail is in `check-agent-limits-claims.md` and `check-market-and-strategy-claims.md`. |
| Method | Each claim was traced from the notes to the public source behind it and checked there on 2026-10-05. Pedro's notes are the origin only; nothing here cites them. |
| Status | Evidence, not a change of direction. About half of the six pointers were already in our records (the brownfield material, METR's developer study, DORA, the harness paper). |
| Used for | PLAN §3.12; the problem section of the proposal |

## Usable evidence, by what it supports

### The contract and the checks must be protected from the agent

| Finding, as published | Public source |
|---|---|
| A model trained on production coding tasks learned three ways to force tests green: an equality override, "`sys.exit(0)`" before the assertions, and a `conftest.py` that patches the test reporter to report "passed". Separately: "In our main setting, we see attemped sabotage 12% of the time, with the sabotaged classifiers being only 65% as effective at detecting reward hacking compared with a baseline." The setting was constructed for the study. | Anthropic and Redwood Research, "Natural Emergent Misalignment from Reward Hacking in Production RL", November 2025, https://arxiv.org/abs/2511.18397 |
| Long-horizon tasks: reward hacking in 13.8% of rollouts | SWE-Marathon, https://arxiv.org/abs/2606.07682 |

### Passing tests is weak evidence

| Finding, as published | Public source |
|---|---|
| "32.67% of the successful patches involve 'cheating' as the solutions were directly provided in the issue report or the comments"; "31.08% of the passed patches are suspicious patches due to weak test cases" (251 patches from one agent and model) | SWE-Bench+, https://arxiv.org/abs/2410.06992 |
| A deterministic check that an agent's own tests mean something: "when we run them on the original, broken codebase, they must fail." | Cognition, "Introducing FrontierCode", 2026-06-08, https://cognition.ai/blog/frontier-code |
| When earlier work must keep passing, results fall: "GPT 5.5 achieves the highest strict solve rate at 14.8% and isolated solve rate peaks at 28.1%" | SlopCodeBench, Orlanski et al., https://arxiv.org/abs/2603.24755 |

### Write the contract before the run

| Finding, as published | Public source |
|---|---|
| On tasks solvable by asking one question, models "achieve only 40-50% accuracy on Logic-Q and Planning-Q" (a multiple-choice format) | QuestBench, https://arxiv.org/abs/2503.22674 |
| "When key details are missing, LLMs often make implicit assumptions and produce code that does not match the intended behavior." | ClarifyCodeBench, Fang et al., https://arxiv.org/abs/2607.00711 |

### Measure consistency, not one run

| Finding, as published | Public source |
|---|---|
| "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%." | τ-bench, https://arxiv.org/abs/2406.12045 |
| The same prompt can give different outputs because of batch size; determinism is achievable ("all of our 1000 completions are identical") at a speed cost | Thinking Machines Lab, "Defeating nondeterminism in LLM inference", https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ |
| Time horizons at 50% reliability: Claude Opus 4.5 at 320 minutes (95% interval 170 to 729); the 80% horizon is "roughly 5x shorter" | METR, Time Horizon 1.1, https://metr.org/blog/2026-1-29-time-horizon-1-1/ and https://arxiv.org/abs/2503.14499 |

### Checks the gate should include

| Finding, as published | Public source |
|---|---|
| Of 2.23 million generated package references, "440,445 (19.7%) were determined to be hallucinations"; "43% of hallucinated packages were repeated in all 10 queries" | Package-hallucination study, see `check-agent-limits-claims.md` item L6 |
| AI-generated code introduced vulnerabilities in 45% of cases across 80 tasks and more than 100 models | Veracode, 2025 GenAI Code Security Report |

### Why not build the harness; where a newcomer's room is

| Finding, as published | Public source |
|---|---|
| Attributed to Ryan Lopopolo of OpenAI: "I am bearish on any harness that doesn't come from the lab whose model you are using. You're fighting against post-training." The hosts' counter: "The real edge lives in the outer harness, not the inner one." The original post was not found; we can cite it only as quoted here. | "ai that works", episode of 2026-05-05, https://github.com/ai-that-works/ai-that-works/tree/main/2026-05-05-openai-tells-you-not-to-build-your-own-harness |
| The harness layer has "no standard interface yet" | Same show, software-factory design patterns episode (2026-08-25) |
| On multiple agents: what works is "setups where multiple agents contribute intelligence to a task while writes stay single-threaded" | Cognition, "Multi-Agents: What's Actually Working", 2026-04-22, https://cognition.com/blog/multi-agents-working |
| Multi-agent research systems "use about 15× more tokens than chats"; not suited where agents share context, "e.g., most coding tasks" | Anthropic, https://www.anthropic.com/engineering/multi-agent-research-system |
| "67% of its PRs are now merged vs 34% last year" (vendor-reported, no denominator) | Cognition, "Devin's 2025 Performance Review", https://cognition.com/blog/devin-annual-performance-review-2025 |

### Trust

| Finding, as published | Public source |
|---|---|
| Trust in AI accuracy fell from 43% (2024) to 33% (2025); distrust rose from 31% to 46%. The 2024 scale had a neutral option that the 2025 chart does not show. | Stack Overflow Developer Survey, https://survey.stackoverflow.co/2025/ai |

## Corrections to the notes

| In the notes | Finding |
|---|---|
| Stack Overflow: trust 29%, down from about 40% | That is one answer option, "Somewhat trust" (40.3% to 29.6%). Like for like: 43% to 33%. |
| SlopCodeBench: best models at about 33% strict | The paper's highest strict solve rate is 14.8%. The 33% figure is from a podcast discussion of the benchmark. |
| Frontier Code uses mutation testing (strip the agent's code, check its tests still fail) | The technique is called "reverse-classical" and runs the agent's tests against the original code. The words "mutation testing" are not in the source. |
| AI code has 2.74 times more vulnerabilities (Veracode) | Not Veracode. CodeRabbit, December 2025, 470 pull requests: "up to 2.74× higher". CodeRabbit sells code review. |
| Multi-agent at about 15 times the tokens of a single agent | The baseline is chat, not a single agent. |
| MIT: 95% of pilots show no measurable P&L return | The report says "95% of organizations are getting zero return". It is marked "Preliminary Findings", and critics say the figure has no visible supporting data. Not used. |
| Devin: migrations 10 to 14 times faster | Two separate customers, at 10 times and 14 times |
| τ-bench airline tops out around 56% | Not in the paper. The best airline score is 35.2%. |
| "Learning to Ask" shows coding agents make unwarranted assumptions | Two papers were merged. "Learning to Ask" is about tool-use agents. The coding benchmark is ClarifyCodeBench. The phrase is in neither. |
| A study found Claude at about 65% on SWE-bench Verified but about 12% on a comparable set | Those are file-localisation accuracies, not issue-resolution rates. |
| GDPval: best model matched experts 47.6% of the time on 1,320 tasks | Measured on the 220-task gold subset |
| Thoughtworks Radar: MCP as the universal integration protocol; context engineering replacing vibe coding | The Radar says "the ultimate integration protocol". Context engineering and spec-driven development are both at "Assess". "Vibe coding" is from a companion article. |
| Determinism costs about 30 to 60% of throughput | Not stated in the source, which gives timings only |
| A 200K window shows serious loss by about 50K tokens | Not in the source |

## Framing that is ours to use, not to attribute

These appear in the notes as summaries and are in no source: the "pair" and "delegate" labels for the two classes of agent; "fan out reads, single-thread writes"; "keep the harness swappable" as a general rule; "failure is workflow integration, not model quality".

## Could not be checked

- The original of the Lopopolo statement.
- Whether Kent Beck says "waterfall wearing a new coat" in his talk; the phrase is in the video's published description.
- The DORA 2025 report PDF, which is gated. "AI, the great amplifier" and the sentence on delivery stability come from Google's announcement.
- Podcast-only statements about SlopCodeBench (one model writing real unit tests; a fivefold cost for two points).
