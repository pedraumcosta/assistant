# Pedro's working principles

| | |
|---|---|
| What this file is | The principles Pedro works by that shaped this exercise, in his own words where they are his |
| What it is not | Evidence. It cites no source and carries no figures. Every figure the project relies on is in `EVIDENCE.md`, traced to a public source. |
| History | An earlier version of this file was a digest of Pedro's private notes, with their file names and untraced figures. It was replaced on 2026-10-05 under the citation rule in `README.md`. |
| Used for | The voice and framing of the plan and proposal; decision ADR-001 |

Several of these are adopted from practitioners Pedro follows and are not claimed as original. Where one of them matters to an argument, the plan cites the public source separately.

## On the thesis

- Reliability, not capability, is the wall.
- The platform is a harness around the agent, not a bet on the agent.
- Autonomy tracks boundedness: match the kind of agent to how bounded and verifiable the task is.
- Brownfield is where the money is.
- Review is the verifier, until the benchmarks say otherwise. There is no training reward for maintainability, so the model will not protect it for you.
- The throughput gain and the quality debt are the same event.

## On deciding whether to invest

- Build, buy, hire and wait are capital allocation choices, not tooling choices.
- Decide in this order: the shape of the work, then the model, then the vendor.
- Do not automate work you cannot describe clearly.
- Without a verifier there is no build.
- In a thin market, the narrow test is the move.
- Wait is a decision. Say it out loud and set a date.
- Capability shipped is not capability adopted. Ship a paved road, not a capability.

## On architecture

- Exhaust the single-loop stack before adding a second loop. Parallelise last.
- Fan out reads, single-thread writes.
- Separate the deterministic plane from the probabilistic plane, and delete every inference call a deterministic component can replace.
- Tool calls are the primitive; protocols and command lines are implementations of them.
- Layer fast deterministic rules before slow model checks.
- Prompt-injection defence is a systems problem, not a prompting problem.
- "No human in the loop" should be a configuration choice justified by risk and evidence, not a default.

## On specifications and documentation

- Anchor the specification; do not freeze it. Judge it by its contract tests.
- A specification nobody enforces is a wish.
- Write down what the code cannot say, and nothing else.
- Markdown for models, HTML for humans.
- Be wary of standing context files; they go stale and can mislead more than they help.

## On measurement

- Agents cannot be their own graders.
- Report consistency across repeated runs and cost per successful outcome, not single-run success.
- A single leaderboard number is not evidence that an agent works on your codebase.
- Never report a throughput number without its paired quality number.
- Licence counts are not adoption.
- A review stage that does not remove a human stage is not a saving.

## On communicating upward

- Identify what the audience cares about, and use language that puts their needs first.
- The person who authorises spending cares about cost and the protection of customer data.
- Quantifiable value is the bar.
- Complexity should have benefits; default to radical simplicity.
- Functionality is an asset; code is a liability.

## On ways of working

- One commit per step, made after the step is verified.
- Record decisions with their rationale, the alternative rejected, and what would change at scale.
- State what deviated from the plan.
