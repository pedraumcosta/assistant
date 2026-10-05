# Brownfield Agentic Engineering

| | |
|---|---|
| Author | Addy Osmani |
| Published | 2026-09-14, on his newsletter |
| Source | https://addyo.substack.com/p/brownfield-agentic-engineering |
| Read on | 2026-10-05, from the publisher's page, downloaded complete |
| Method | Read end to end by the main Claude Code session. Quotations below were copied from the downloaded text. |
| Status | Digest with quotations, not a copy. A practitioner's essay: the practices are the author's judgment, and the case studies are second-hand. The article carries a sponsored insert, quoted twice in the text, which is advertising and not part of the argument. |
| Used for | PLAN §3.11 (evaluation of the brownfield thesis), PLAN §2.1 decisions T1, T4 and T7 |

## What the article says

**Definition.** Brownfield systems are those where "the repository is no longer a complete description of how the thing actually behaves. Institutional knowledge, duct tape, legacy services, and expectations other teams depend on live outside the tree." The task: "making hidden constraints visible and cheap changes trustworthy."

**The practices, in the article's order**

1. **Zones.** Green: "safe/good tests/isolated". Yellow: "mixed quality". Red: "sensitive/auth/billing/permissions". Three rules: "A person draws the map, not the agent"; "Zones only move when it's earned"; "the zone sets the verbs: green is a tight loop, yellow is tests first, red is a human pairing on every step or the work not happening."
2. **Write down what the code cannot say.** "Autonomy should follow blast radius, observability, and recoverability. A model's confidence is a poor guide." And: "Write down what the code can't say, and nothing else."
3. **Make the research survive the session.** A read-only pass that produces "a short comprehension memo: entry points, owners, callers, existing abstractions, tests, production signals, relevant history, and open questions. Claims should cite a file, issue, ownership record, or dashboard." Then plan in a clean context; "A human picks the path." Review "starts fresh and works backward from the acceptance criteria."
4. **When instructions become a harness.** "Every repeated correction is a missing piece of the harness." "When the same review comment appears again, move it into a lint rule, hook, type, test, or skill. Keep prose for constraints that cannot be enforced mechanically." "Over time the harness becomes a record of failures the team has decided not to pay for twice."
5. **Start with zero-risk work.** "Lock today's behavior before you let anything improve it." Characterization tests pin "what the module does today, ugly parts included". Then: "When an agent is the one making them pass, don't let that same session be the only author of the tests. Pin the behavior first, in a separate pass or by a person; then let the agent work. Otherwise you get a green suite that encodes the implementation you just invented."
6. **Migrate in complete units.** "A migration is complete when the new path works and the old dependency is demonstrably gone." "Tests can stay green while a replacement still calls the legacy implementation."
7. **Parallelize last.** "Parallelism multiplies the bottleneck you already have." "Human attention goes first to the largest blast radius and weakest oracle." Automated review should "lead with intent, changed invariants, test results, parity mismatches, and the rollback route."
8. **Measure beyond lines.** "lead time, review minutes, human interventions, escaped defects, rollbacks, oracle mismatches, and suppressions left behind." For a migration: "remaining old imports, traffic served by the new path, parity mismatches, and legacy dependencies removed. A green suite with all traffic still taking the old path is busywork."

**The central line.** "Agents have changed the price of trying several plausible implementations. They haven't changed the evidence required to choose one."

## Case studies cited

These are the article's statements about other organisations, not checked here at their own sources (see `brownfield-market.md` for that check).

| Case | As stated in the article |
|---|---|
| Netflix | GraphQL cutover: "replay and shadow traffic against the old and new paths, diff the payloads, promote only when they match" |
| SWE Refactor Bench | "Across 520 agent runs, only 28 passed its migration audit, behavioral tests, and independent verification." |
| Stripe | "moved 3.7 million lines to TypeScript in one PR through months of codemod work, with no agents involved" |
| Bun | Zig-to-Rust port "ran about 50 workflows over 11 days from a 535,000-line codebase, with two adversarial reviewers on every generated unit and the entire pre-existing test suite as the merge gate"; "hours went into a porting guide mapping Zig idioms to Rust before any agent ran" |
| VB6 to C# study | "92% behavioral equivalence on simple features and 47% on complex ones: unit size is the lever" |
| Asana | "cleared a multi-year Enzyme backlog in two calendar weeks for about $12,000 in model and infrastructure cost". The author's own caution: "treat it as a vendor-reported cost of generation, not a controlled savings study." |
| Shopify | Rebuilt the Shop app "from React Native to native Swift and Kotlin in twelve weeks with a small team and agent-gated, screen-sized checkpoints" |
| Spotify | "650-plus agent PRs merged monthly on rails Backstage built years earlier" |

The article's own summary of what the cases share: "a narrow mechanical migration, a pre-existing suite, humans still reviewing every change", and "What transfers between companies is the structure around the agents."

## Check of Pedro's notes

Pedro's digest lists nine practices and the case studies. All of it holds against the text. Two details to add: the Bun codebase size (535,000 lines) and that Asana's two weeks are "calendar weeks". The Teleport item is a paid advertisement about finding vulnerabilities, not a brownfield case.

## Relevance to the two theses

**As support for a brownfield product (thesis B).** The article describes a need and a discipline. It does not describe a product, and most of what it recommends is human work: a person draws the zone map, a human picks the path, humans review every change. The successful cases depended on assets the organisations already had (a pre-existing test suite, a porting guide, a platform built years earlier).

**As support for the evidence layer (thesis A).** Nearly every practice is a statement of that thesis in brownfield terms:

| The article | Our evidence layer |
|---|---|
| Pin the behaviour first, by a separate pass or a person, before the agent works | A contract written before the run and protected from the agent |
| "A model's confidence is a poor guide"; autonomy follows blast radius, observability and recoverability | Risk tiers set by measurement, not by the model's own claim |
| "Tests can stay green while a replacement still calls the legacy implementation" | A verdict that checks the change happened, not only that tests pass; the false-pass rate |
| Review leads with intent, changed invariants, test results, parity mismatches, rollback route | The contents of the evidence record |
| Move a repeated review comment into a lint rule, hook, type or test | Each customer's accumulated checks as the durable asset |
| Zones set by a person; red means a human on every step | Risk routing with redlines |

**What it suggests.** Brownfield is less a separate product than the place where the evidence layer is most needed: where constraints live outside the code, tests under-describe behaviour, and a wrong change is expensive.
