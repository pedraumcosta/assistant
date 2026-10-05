# Designing AI-resistant technical evaluations

| | |
|---|---|
| Author | Tristan Hume, Anthropic |
| Published | 2026-01-21, Anthropic Engineering blog |
| Source | https://www.anthropic.com/engineering/AI-resistant-technical-evaluations |
| Read on | 2026-10-05, from the publisher's page |
| Method | Read end to end by a Claude Code sub-agent from the complete downloaded text, and checked against Pedro's prior notes on the article. |
| Status | Digest. One hiring task at one company, written by the model vendor. |
| Used for | PLAN §3.6; ROADMAP open questions T3 and T9 |

## Read record

- **Source:** "Designing AI-resistant technical evaluations", Engineering at Anthropic. Author: Tristan Hume, "a lead on Anthropic's performance optimization team". "Published Jan 21, 2026".
- **Coverage:** read in full, all 261 lines (article body lines 13-147; the rest is site chrome).
- **Basis of claims:** one author's first-hand account of a hiring take-home he designed. No score distribution is published; the only hard results are six cycle counts.

## What the article says

1. **Version 1.** Candidates optimise a parallel tree traversal on a Python-simulated accelerator. AI use is explicitly allowed, because "Longer-horizon problems are harder for AI to solve completely".
2. **Defeated by Opus 4.** A pre-release Opus 4 "came up with a more optimized solution than almost all humans did within the 4-hour limit".
3. **Version 2.** "I used Claude Opus 4 to identify where it started struggling. That became the new starting point for version 2." Multicore was removed, depth added, time halved. "It served us well—for several months."
4. **Defeated by Opus 4.5.** It met the passing threshold, then stopped, "convinced it had hit an insurmountable memory bandwidth bottleneck". Told the achievable cycle count, it found the trick and matched the best human.
5. **Attempt 1 (harder realistic problem).** Failed: longer thinking budgets solved it. Cause: "Claude has substantial training data to draw on."
6. **Attempt 2 (current).** Zachtronics-style puzzles on a tiny constrained instruction set, no debugging tools supplied. Opus 4.5 failed it.

Principles: many independent sub-problems, not "a single insight"; wide score distribution; "sufficiently out of distribution"; tooling judgment as signal; accept lost realism: "The original worked because it resembled real work. The replacement works because it simulates novel work."

## Check of Pedro's notes

- **Capability-floor exhibit.** *Corrected* on the first step; the direction is reversed. Text: "Claude 3.7 Sonnet had already crept up to the point where over 50% of candidates would have been better off delegating to Claude Code entirely." Opus 4 step *Confirmed* ("outperformed most human applicants"). Opus 4.5 step *Confirmed*: "approximately matching the best human performance in 2 hours" in "a casual Claude Code session". Not strictly "the same task": Opus 4 beat version 1, Opus 4.5 version 2.
- **Quote.** *Corrected.* Exact text: "Human experts retain an advantage over current models at sufficiently long time horizons." The note dropped "over current models".
- **Method.** *Confirmed* (quotation in item 3 above), but that fix lasted only "several months"; the fix that held was out-of-distribution design.

## Figures

- "three iterations of a performance engineering take-home"
- "Since early 2024"; "Over 1,000 candidates have completed it, and dozens now work here"
- "In November 2023"; "I took two weeks to design"
- "A 4-hour window (later reduced to 2 hours)"; "a normal 50 minute interview"
- "started in early February, two weeks after our first hires"; "overflowing 32 bits"
- "Over the next year and a half, about 1,000 candidates completed the take-home"
- "By May 2025, Claude 3.7 Sonnet ... over 50% of candidates"
- "a live interview question in 2023"; "Claude 3 Opus beat part 1 of that question; Claude 3.5 Sonnet beat part 2"
- "from 4 hours to 2 hours"; "multi-week delays"
- Opus 4.5: "for 2 hours"; "met our passing threshold in under an hour"; "By the 2-hour mark"; "heavy use of Claude 4 with steering"
- "Humans typically spend half the 2 hours reading and understanding the problem"
- "implement the changes in under a day"; "2D TPU registers"
- "about 10 instructions with one or two state registers"; "one medium-hard puzzle"
- "2164 cycles: Claude Opus 4 after many hours in the test-time compute harness"
- "1790 cycles: Claude Opus 4.5 in a casual Claude Code session"
- "1579 cycles: Claude Opus 4.5 after 2 hours in our test-time compute harness"
- "1548 cycles: Claude Sonnet 4.5 after many more than 2 hours of test-time compute"
- "1487 cycles: Claude Opus 4.5 after 11.5 hours in the harness"
- "1363 cycles: Claude Opus 4.5 in an improved test time compute harness after many hours"
- "If you optimize below 1487 cycles"

## Relevance to our thesis

- **(a) Floor speed.** A task tuned to one model's failure point lasted "several months"; trap tasks built on current weaknesses should be expected to decay similarly. The harness alone moved the score ("improved our harness in a generic way and got a higher score"), so reliability must be re-measured continuously per model-and-harness pair, not benchmarked once.
- **(b) Where humans or harder checks add value.** Unlimited time; novel problems; and remaining human work including "figuring out how to verify the correctness of our systems". The model also stopped early on a confident wrong belief, which supports checking after the agent stops.
- **(c) Reusable methods.** Probe with the current model and start tasks where it struggles; prefer many independent sub-problems; avoid well-documented problem classes; re-test with larger thinking budgets before trusting a task; have less-informed humans confirm solvability.
- **(d) Against us.** Every realistic task fell; only an unrealistic one held. Trap tasks resembling real repository work may saturate quickly, and maintenance is permanent.

## Cautions

- One performance-engineering task, one company, one author; time-boxed hiring, not production code review.
- Vendor interest: the post promotes Claude and recruits.
- Unsupported: "scores correlate well" carries no data; human baselines are unquantified.
- Nothing addresses false-pass rates, pass^k or cost per accepted change; those links are our inference.
- Whether the current take-home resists later models is not in the text.
