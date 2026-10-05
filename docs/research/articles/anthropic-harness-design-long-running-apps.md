# Harness design for long-running application development

| | |
|---|---|
| Author | Prithvi Rajasekaran, Anthropic Labs |
| Published | 2026-03-24, Anthropic Engineering blog |
| Source | https://www.anthropic.com/engineering/harness-design-long-running-apps |
| Read on | 2026-10-05, from the publisher's page, downloaded complete |
| Method | Read end to end by the main Claude Code session. Quotations below were copied from the downloaded text. |
| Status | Digest with quotations, not a copy. The figures are the author's own measurements of two runs, published by the model vendor; they are single runs, not a study. |
| Used for | PLAN §3.6, PLAN §2.1 decisions T2, T3, T4 and T9 |

Pedro's notes cited a Medium summary of Anthropic's harness playbook. This record is of the primary post instead.

## What the post says

**The problem.** Two failure modes on long tasks:

- Loss of coherence as the context fills, and "context anxiety": some models "begin wrapping up work prematurely as they approach what they believe is their context limit". Claude Sonnet 4.5 showed it strongly enough that context resets were needed; "Opus 4.5 largely removed that behavior on its own", so the resets were dropped.
- Self-evaluation: "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre." And: "agents reliably skew positive when grading their own work."

**The remedy.** "Separating the agent doing the work from the agent judging it proves to be a strong lever". The author is explicit about its limit: "The separation doesn't immediately eliminate that leniency on its own; the evaluator is still an LLM that is inclined to be generous towards LLM-generated outputs. But tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work".

**The architecture.** Three agents built on the Claude Agent SDK:

- *Planner*: expands a 1–4 sentence prompt into a product spec, kept high-level so that spec errors do not cascade into the implementation.
- *Generator*: builds one feature at a time and self-evaluates before handing off.
- *Evaluator*: uses the Playwright MCP "to click through the running application the way a user would, testing UI features, API endpoints, and database states", then grades against criteria. "Each criterion had a hard threshold, and if any one fell below it, the sprint failed".

**The sprint contract.** "Before each sprint, the generator and evaluator negotiated a sprint contract: agreeing on what 'done' looked like for that chunk of work before any code was written." The generator proposes what it will build and how success will be verified; the evaluator reviews; they iterate until they agree. Agents communicate through files. One sprint's contract "had 27 criteria".

**Tuning the evaluator took human work.** "Out of the box, Claude is a poor QA agent. In early runs, I watched it identify legitimate issues, then talk itself into deciding they weren't a big deal and approve the work anyway. It also tended to test superficially". The tuning loop was to read the evaluator's logs, find where its judgment diverged from the author's, and update its prompt, over "several rounds". Even then it missed "undiscovered bugs in more deeply nested features".

**The evaluator's value depends on the model.** After moving to Opus 4.6 the author removed the sprint construct and ran the evaluator once at the end. "Tasks that used to need the evaluator's check to be implemented coherently were now often within what the generator handled well on its own, and for tasks within that boundary, the evaluator became unnecessary overhead." The stated rule: "the evaluator is not a fixed yes-or-no decision. It is worth the cost when the task sits beyond what the current model does reliably solo."

**The general principle.** "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing, both because they may be incorrect, and because they can quickly go stale as models improve." And the closing view: "the space of interesting harness combinations doesn't shrink as models improve. Instead, it moves".

## Figures

All are the author's reports of single runs.

| Run | Model | Duration | Cost |
|---|---|---|---|
| Retro game maker, solo agent | Opus 4.5 | "20 min" | "$9" |
| Retro game maker, full harness | Opus 4.5 | "6 hr" | "$200" |
| Browser DAW, updated harness | Opus 4.6 | "3 hr 50 min" | "$124.70" |

- "The harness was over 20x more expensive".
- The planner expanded the one-sentence prompt "into a 16-feature spec spread across ten sprints".
- Frontend experiment: "5 to 15 iterations per generation"; "Full runs stretched up to four hours."
- Updated harness breakdown: Planner "4.7 min", "$0.46". Build rounds "$71.08", "$36.89", "$5.88". QA rounds "$3.24", "$3.09", "$4.06".

Computed from that table, not stated in the post: the three QA rounds total 10.39 USD of the 124.70 USD run.

## Check of Pedro's notes

| Note | Finding |
|---|---|
| "Context anxiety": Sonnet 4.5 wraps up early near context limits | Confirmed |
| Self-evaluation bias | Confirmed |
| Planner → Generator (negotiates sprint contract) → Evaluator (Playwright as a real user, per-criterion thresholds) | Confirmed |
| `feature_list.json` kept in JSON because it resists reformatting | Not in this post. It likely comes from Anthropic's earlier long-running harness work, which this post refers to but does not restate. |
| "Unacceptable to remove or edit tests" as a hard rule | Not in this post; same likely origin. |
| Same prompt: solo agent ships a broken game, harnessed agent ships 16 working features over 10 sprints | Corrected. The planner produced "a 16-feature spec spread across ten sprints". The post does not say all 16 worked. It says the harness build was playable where the solo build's core feature "simply didn't work", with rough edges remaining. |
| "The harness is the product" | Not in this post. |

## Relevance to our thesis

**Supports it**
- The model vendor states that agents grade their own work too generously, and that a same-family evaluator is still lenient.
- Agreeing what "done" means before code is written is presented as the mechanism that kept the work faithful to the spec.
- It is outcome evidence that a contract plus a separate evaluator changes results, on one task, at more than twenty times the cost.
- Evaluation is cheap next to generation in the one breakdown given.

**Cuts against it**
- Contract plus separate evaluator is now the vendor's published practice. The idea is not ours and can ship natively.
- The value of the check shrinks as the model improves: on Opus 4.6 the evaluator was "unnecessary overhead" for tasks inside what the model does reliably. A verification product has to be aimed at work beyond that boundary, and the boundary moves with each model release.
- The work is greenfield application building with subjective criteria. It says nothing about changes to existing repositories.

**What it leaves open, and where we would differ**
- The evaluator is a model from the same vendor, tuned by hand against one person's judgment. No false-pass rate is reported.
- There is no deterministic check and no evidence record for a human reviewer or an auditor.
- The contract is negotiated between two agents; no human approves it.

**Taken into our design thinking**
- Contract drafted by the generator and approved by a second party before work starts (candidate answer to T4).
- Criteria with hard thresholds, any one of which fails the unit of work.
- Apply the gate by risk and by distance from what the model does reliably, not uniformly (T7).
- The comparison arm in the prototype should resemble this evaluator: an agent that exercises the result against per-criterion thresholds, not a single judging call (T9).
