# Claude Code: Spec-Driven Development — Why Your AI Coding Sessions Fall Apart at Hour Three

| | |
|---|---|
| Author | Rick Hightower |
| Published | 2026-05-22 |
| Source | https://medium.com/@richardhightower/claude-code-spec-driven-development-why-your-ai-coding-sessions-fall-apart-at-hour-three-e7145128bfc0 |
| Read on | 2026-10-05, via a Freedium mirror |
| Method | Read end to end by a Claude Code sub-agent from the complete downloaded text, and checked against Pedro's prior notes on the article. |
| Status | Digest. Feature and version claims are the author's and were not checked against vendor documentation. No measured data. |
| Used for | PLAN §3.6; PLAN §2.1 decisions T2 and T4 |

## Read record

- **Author and date:** Part 4 of "Claude Code, Day-to-Day" by Rick Hightower; May 22, 2026 (Freedium mirror).
- **Read:** the whole file, lines 1-385.
- **Basis:** a how-to from the author's own practice ("I save the plan to docs/plans a lot!"). One pattern is attributed to "Anthropic's official best-practices documentation", without a link. No data or external citation. Product details (versions, hook events, `/goal`) are the author's statements, not checked here against vendor documentation.

## What the article says

**Thesis.** Claude Code "already ships a complete task list, spec-driven, project-management system", so overlays are unnecessary: "Spec-driven development with Claude Code is not a feature you install. It is a workflow you assemble from primitives that are already on disk."

**Four layers, one job each.**

| Layer | Where it lives | Lifetime | Answers |
|---|---|---|---|
| Plan mode | Session | "evaporates when the session ends" | "what should we do?" |
| SPEC.md | `docs/specs/<feature>.md`, or repo root for a one-off | "durable but static" | "what did we agree to?" |
| Task list (TaskCreate, TaskUpdate, TaskGet, TaskList) | In-session; named lists under `~/.claude/tasks/` | "survives context compaction" | "where are we right now?" |
| `.claude/todos.json` plus `TODO.md` | Repo, committed | Cross-session, but "goes stale the moment you stop syncing it" | "where are we across sessions?" |

**Interview-to-spec.** A prompt asks Claude to interview the developer with the AskUserQuestion tool and write a spec to `docs/specs/<feature-name>.md`; the human reads, fixes and commits it. A typical spec includes goals and non-goals, rejected alternatives and acceptance criteria. Execution then starts in a fresh session (`/clear` or a new terminal) because interview detours "now just pollute your context".

**Plan mode.** Read-only research; Ctrl+G edits the plan before approval. Saving it to `docs/plans/` is "the poor-man's spec". "For a small change, skip the spec entirely and use plan mode."

**Task list.** Created and updated by Claude itself. `CLAUDE_CODE_TASK_LIST_ID=oauth-migration claude` shares a named list across sessions.

**Durable mirror.** `todos.json` holds per-task `id`, `subject`, `description`, `status`, `workstream`, `blocks`, `blocked_by` and timestamps. A skill at `.claude/skills/sync-todos/SKILL.md` merges the live list into the JSON and regenerates `TODO.md`, triggered by a Stop hook of `"type": "prompt"` or by the TaskCreated and TaskCompleted hook events.

**Autonomous execution.** `/goal implement the spec in docs/specs/oauth-migration.md until all acceptance criteria hold and all tests pass`. "After every turn, a small fast model checks whether the condition is met." The author advises writing validation checks (unit tests, Playwright MCP) into the goal.

## Check of Pedro's notes

- **Four-layer separation with explicit lifetimes:** Confirmed. Refinements: the path is `.claude/todos.json`, and the task list can also cross sessions via `CLAUDE_CODE_TASK_LIST_ID`.
- **Quote "refusing to ask any one of them to be the others":** Confirmed. "The discipline is refusing to ask any one of them to be the others."
- **Interview-to-spec, then a fresh session because detours pollute context:** Confirmed.
- **"Tools fail 'not because the tool lacks project management…'":** Corrected. The subject is sessions: "Your sessions fall apart not because the tool lacks project management, but because nobody told you which layers it already includes."

## Figures

All asserted by the author; none measured or sourced.

- "three hours later … six detours" (opening scenario).
- "a 19-part guide"; "16 min read".
- "Project tracking in Claude Code has four layers."
- "Ten to twenty minutes later, Claude writes a complete spec to disk"; "Let Claude interview you for fifteen minutes."
- "more than twice"; "Six months later".
- "There are three ways in" (plan mode).
- "Since Claude Code v2.1.142 (TypeScript SDK 0.3.142)".
- "three or more distinct actions"; "built in for months".
- "a working skill on disk in about ninety seconds".
- "Goal achieved (2h 14m, 47 turns)" and "132 passing, 0 failing": called "a worked run", with no project or log given; treat as illustrative.
- "One skill, one hook, three views, zero manual sync."
- "a research preview as of Q1 2026" (agent-view).
- Biography: "30+ coding agents"; "Fortune 100".

## Relevance to our thesis

**Supports**

- Contract origin: the interview yields acceptance criteria and non-goals before coding, reviewed and committed by a human. That works for feature-sized work.
- Persistence: a committed file re-read by a fresh session is the answer given to compaction and multiple sessions.
- Plug-in surface: Stop, TaskCreated and TaskCompleted hooks, SKILL.md and MCP are shown working.
- Everything described is a plan or a self-report. The agent marks its own tasks complete; `/goal` completion is judged by "a small fast model"; the sync hook is a prompt; "each acceptance criterion verified" is the agent's own report. There is no deterministic or independent check, evidence bundle, budget or risk routing.
- Nothing stops the agent editing `SPEC.md` or `todos.json`; the only guard is a prompt sentence, "Do not modify any other files."

**Cuts against**

- Native features cover the "scope and acceptance criteria written first" half of a change contract, and the article's message is "stop bolting things on".
- For small changes the author recommends no spec. A contract that costs effort will be skipped.
- `/goal` with test conditions will look like verification to buyers, although it is model-judged.

**Take for a prototype**

- Derive the contract from the native spec or plan (`docs/specs/`, `docs/plans/`) instead of asking for a second document.
- Pair a machine-readable file with stable IDs and a human-readable rendering, as `todos.json` and `TODO.md` do.
- Add the protection the article lacks: a committed hash, a pre-tool hook or deny rule on the contract path, and checks run outside the agent in CI.

## Cautions

- Promotional: speaker booking and the author's own skill marketplace.
- Feature and version claims are unverified and may be version-specific.
- The author calls the `todos.json` setup "more for example purposes".
- Same author as the CCA-F article; the two are not independent sources.
