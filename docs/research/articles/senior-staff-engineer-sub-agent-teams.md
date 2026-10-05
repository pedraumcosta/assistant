# Building a Senior Staff Engineer with Sub-Agent Teams in Claude Code

| | |
|---|---|
| Author | Fareed Khan |
| Published | 2026-04-13 |
| Source | https://levelup.gitconnected.com/building-a-senior-staff-engineer-with-sub-agent-teams-in-claude-code-771298151392 |
| Read via | Freedium mirror of the article, downloaded complete on 2026-10-05 |
| Method | Read end to end by a Claude Code sub-agent working from the full downloaded text, with our thesis as the lens. This replaces a first pass on 2026-10-03 that saw only a truncated summary. |
| Status | Digest, not a copy of the article. All figures are the author's claims; none is verified and none may be used as evidence. |
| Used for | PLAN §3.4, DESIGN, prototype design |

## Read confirmation

I read the downloaded full text lines 1-4058 (the whole file) sequentially. The article runs from line 18 to line 4054; the last content is the fifth bullet of "How to Improve It Further", followed by the Freedium footer. Most code blocks appear two or three times (scrape artefact). No web tools were used.

## 1. Structure and inventory

Sections in order: Creating the Team Codebase; Hooks (1% Rule, Instruction Priority, Skill Discovery Flow); Brainstorming & Design; Spec Review; Visual Companion; Writing Plans; Plan Review; Subagent-Driven Development; Implementer Prompt; Spec & Code Quality Reviewers; TDD; Testing Anti-Patterns; Systematic Debugging; Root Cause Tracing & Defense in Depth; Verification Before Completion; Code Review (reviewer, requesting, receiving); Git Worktrees (including Finishing a Development Branch); Writing Skills; Agents & Commands; Testing the Senior Staff Engineer; How to Improve It Further.

**Hooks (one event only)**
- `hooks.json`: a `SessionStart` hook, matcher `startup|clear|compact`, `async: false`.
- `run-hook.cmd`: cross-platform launcher.
- `session-start`: cats the handbook SKILL.md into `additionalContext`, wrapped in `<EXTREMELY_IMPORTANT>`, with output variants for Claude Code, Cursor and Copilot CLI.

**Skills (14 directories)**
- `using-senior-staff-engineer`: handbook, 1% rule, priority order, red-flags table.
- `brainstorming`: design gate and nine-step checklist; also holds `spec-document-reviewer-prompt.md`, `visual-companion.md` and `scripts/` (local HTML server).
- `writing-plans`: 2-5 minute tasks, no-TBD policy; also holds `plan-document-reviewer-prompt.md`.
- `subagent-driven-development`: per-task loop; holds `implementer-prompt.md`, `spec-reviewer-prompt.md`, `code-quality-reviewer-prompt.md`.
- `test-driven-development`: the Iron Law; also `testing-anti-patterns.md`.
- `systematic-debugging`: four phases, three-fix rule; also `root-cause-tracing.md`, `defense-in-depth.md`.
- `verification-before-completion`: evidence before claims.
- `requesting-code-review` and `receiving-code-review`.
- `using-git-worktrees` and `finishing-a-development-branch`.
- `writing-skills`: TDD for skills, description rules, word budgets.
- `executing-plans` and `dispatching-parallel-agents`: listed in the directory tree but never shown or explained.

**Agents:** one file, `agents/code-reviewer.md` (Senior Code Reviewer persona).

**Sub-agent roles (prompt templates via the Task tool):** context explorer, spec document reviewer, plan document reviewer, implementer, spec compliance reviewer, code quality reviewer, code reviewer.

**Commands:** `brainstorm.md`, `write-plan.md`, `execute-plan.md`. All three are deprecated stubs that only tell the user to use the skill.

## 2. How each discipline is enforced

Every discipline is enforced by prompt text. The only deterministic mechanism in the article is the SessionStart hook, and it only injects text. There is no PreToolUse, PostToolUse or Stop hook, no permission or tool restriction, and no CI.

| Discipline | Mechanism | Key rule text |
|---|---|---|
| Skill invocation | Hook injects text; compliance is probabilistic | "If you think there is even a 1% chance a skill might apply... you ABSOLUTELY MUST invoke the skill." |
| Design approval | Prompt only | "`<HARD-GATE>` Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it." Also "Wait for the users response. Only proceed once the user approves." |
| Planning | Prompt, self-review, optional reviewer sub-agent | "Each step is one action (2-5 minutes)"; "These are **plan failures** — never write them: 'TBD', 'TODO'..."; reviewer told to "Approve unless there are serious gaps". |
| TDD | Prompt only | "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"; "Write code before the test? Delete it. Start over... Delete means delete". |
| Debugging | Prompt only | "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"; "If ≥ 3: STOP and question the architecture". The count is self-reported. |
| Review stage 1 (spec compliance) | Prompt to a fresh sub-agent | "CRITICAL: Do Not Trust the Report... You MUST verify everything independently"; "Read the actual code they wrote". |
| Review stage 2 (code quality) | Prompt; ordering is by instruction | "only fires after spec compliance passes"; Critical / Important / Suggestions tiers. |
| Verification | Prompt only | See section 3. |
| Worktree isolation | Prompt containing shell commands the model is told to run | "MUST verify directory is ignored before creating worktree: `git check-ignore -q .worktrees`". |
| Finishing a branch | Prompt only | "Cannot proceed with merge/PR until tests pass. Stop. Dont proceed to Step 2."; "Type 'discard' to confirm. Wait for exact confirmation." |

The author's language overstates this. The design gate is described as "The agent physically cannot proceed to coding", and the finish gate as "The CEO can't override it." Neither is true mechanically. The handbook itself says "If CLAUDE.md says 'don't use TDD'... follow the users instructions", so the user outranks every rule.

## 3. Verification and everything after

**Rules (all in `verification-before-completion/SKILL.md`)**
- "Claiming work is complete without verification is dishonesty, not efficiency. **Core principle:** Evidence before claims, always."
- "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE. If you havent run the verification command in this message, you cannot claim it passes."
- Gate: "1. IDENTIFY: What command proves this claim? 2. RUN: Execute the FULL command (fresh, complete) 3. READ: Full output, check exit code, count failures 4. VERIFY: Does output confirm the claim?... 5. ONLY THEN: Make the claim. Skip any step = lying, not verifying".

**What counts as evidence (claim / requires / not sufficient)**
- Tests pass / "Test command output: 0 failures" / "Previous run, 'should pass'".
- Build succeeds / "Build command: exit 0" / "Linter passing, logs look good".
- Bug fixed / "Test original symptom: passes" / "Code changed, assumed fixed".
- Agent completed / "VCS diff shows changes" / "Agent reports 'success'".

**Red flags:** "Using 'should', 'probably', 'seems to'"; "Expressing satisfaction before verification"; "About to commit/push/PR without verification"; "ANY wording implying success without having run verification". The excuse table includes "'Different words so rule doesn't apply' | Spirit over letter".

The evidence is terminal output read and judged by the same model that makes the claim. Nothing is persisted, signed or re-run by anything outside the model.

**Code review, worktrees and finishing** are covered in section 2. Additional details:
- The reviewer receives `{WHAT_WAS_IMPLEMENTED}`, `{PLAN_OR_REQUIREMENTS}`, `{BASE_SHA}`, `{HEAD_SHA}`, `{DESCRIPTION}` and no session history.
- Receiving review bans performative agreement and allows "Push back if reviewer is wrong (with reasoning)".
- Finishing offers exactly four options (merge locally, PR, keep, discard), re-runs tests after a local merge, and uses a PR body with Summary and Test Plan.

**Writing Skills:** "NO SKILL WITHOUT A FAILING TEST FIRST": run pressure scenarios on sub-agents without the skill, then with it. One finding matters to us: "A description saying 'code review between tasks' caused Claude to do ONE review, even though the skills flowchart clearly showed TWO reviews". The skill description alone changed behaviour.

**"Testing the Senior Staff Engineer":**
- It is one anecdotal session, shown in screenshots. The task was to "build an interactive skill correlation visual guide from a collection of YouTube transcripts".
- It exercised only brainstorming: exploring context, a todo checklist, offering the visual companion, one-at-a-time questions, and three approaches rendered as a browser mockup.
- It stops before the design doc: "The brainstorming checklist still has 'Write design doc,' 'Spec self-review,' and 'Transition to implementation' remaining."
- Planning, sub-agent dispatch, TDD, both reviews, debugging, verification, worktrees and finishing were never run. No code was written and no metrics were collected.
- The claim "It won't touch code until every box is checked" is a prediction, not an observation.
- The section closes: "There is already a plugin called superpowers which works in a similar way but with more advance features."

**"How to Improve It Further" (complete list)**
1. Add memory across sessions: "right now each session starts fresh".
2. Cost-aware model routing: "the model selector currently relies on the manager's judgment. Adding actual token cost tracking per task..."
3. Inter-agent communication: message passing between parallel agents.
4. Automated regression testing for skills: "skills are pressure-tested manually when created but can drift as the underlying model changes. A CI pipeline that runs the pressure scenarios nightly and flags when agents start rationalizing past the skill's defenses".
5. Human feedback loop integration: overrides and rejections feed back to strengthen the rule.

## 4. Sub-agent contract

- **Passed in:** a constructed prompt only ("They should never inherit your sessions context or history"). It carries the task text, relevant context, and for reviewers the spec or plan path and git SHAs.
- **Sub-agents skip the handbook:** `<SUBAGENT-STOP>` "If you were dispatched as a subagent to execute a specific task, skip this skill."
- **Statuses:** `DONE` ("Proceed to spec compliance review"), `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`. "**Never** ignore an escalation or force the same model to retry without changes."
- **Returned:** a status plus a self-review on "completeness, quality, discipline, and testing". The article does not show the report schema.
- **Reviewers return:** Approved or Issues Found, with file:line references.
- **Treatment of self-report:** distrust by prompt ("The implementer finished suspiciously quickly"); the lead should check the VCS diff and "run the tests independently".
- **Model tiering:** mechanical tasks get "a fast, cheap model"; integration and judgment get "a standard model"; architecture, design and review get "the most capable available model". The lead chooses, and nothing measures cost.

## 5. Where it leaks

**Admitted by the author**
- Skills "can drift as the underlying model changes" and are only tested manually.
- Model routing is judgment, with no cost tracking.
- There is no memory across sessions.
- Old commands "bypass important processes".
- Agents "are remarkably good at finding loopholes".
- A skill description alone caused one review instead of two.

**My reading**
- Every gate is checked by the model it constrains. Nothing blocks Write/Edit before approval, checks that a failing test preceded the code, confirms the test command ran, or stops a completion claim.
- "Delete means delete" and the fix count are unobservable.
- Reviewers are the same model family and are calibrated to "Approve unless there are serious gaps".
- "VCS diff shows changes" proves activity, not correctness.
- The tests are written by the agent that needs them to pass, so false greens are unaddressed.
- Sub-agents are explicitly exempted from the handbook.
- A user instruction or CLAUDE.md line turns any rule off.
- There is no audit trail beyond committed spec and plan files, and no risk tiering, scope enforcement or budget.
- The one hook looks misconfigured as printed. It cats `skills/using-staff_engineer/SKILL.md` while the directory is `using-senior-staff-engineer`, and falls back to `echo "Error reading..."`. `hooks.json` uses `${PROJECT_ROOT_DIR}` while the script tests `CLAUDE_PLUGIN_ROOT`. If so, the handbook would silently not load.

## 6. What the evidence layer should adopt and add

**Adopt**
- The distribution pattern: a plugin with a SessionStart hook plus SKILL.md files, portable across Claude Code, Cursor and Copilot CLI.
- Descriptions that state "when to use", never the workflow.
- The claim-to-required-evidence table as the schema for acceptance checks.
- "Fresh" evidence semantics (run after the last change).
- The four statuses.
- Reviewer inputs of BASE_SHA, HEAD_SHA and requirements.
- Spec review before quality review.
- Critical / Important / Suggestion tiers.
- Plan fields of exact files and exact commands with expected output; these map directly onto contract scope and acceptance checks.
- A baseline test run before work and a re-test after merge.
- Typed confirmation for destructive actions.

**Add (absent from the article)**
- Stop and PreToolUse hooks that actually block.
- Out-of-band re-execution of checks after the agent stops.
- Diff-versus-scope enforcement.
- A persisted evidence bundle.
- Risk tiering and routing to humans.
- Cost and budget accounting.
- Red-then-green proof from commit order or logs.
- False-green detection.
- Per-repo evaluation metrics and the nightly skill-regression CI the author asks for.

## 7. Read on the thesis

The article supports the thesis but does not prove it. It is the strongest statement of prompt-level discipline and it contains no hard enforcement and no outcome data. Its own improvement list asks for cost tracking and regression CI, and its verification rule defines evidence without anyone but the claimant checking it.

Against the thesis: the free prompt layer (the author names superpowers) already covers the process-discipline story and may be enough for many teams. The article also gives no evidence that prompt discipline fails in practice; it simply never measures it. The evidence layer has to justify itself on measured false-green and skip rates, which this article cannot supply.

## 8. Numbers (all are the author's claims)

**The two figures you asked about**
- "1847" appears once: "The result: all 1847 tests passed, zero pollution." It is the outcome of the defense-in-depth debugging example (the empty `projectDir` bug) in the debugging skill's source material, not a test of this system.
- "95% vs 40%" appears in a list introduced as "Real-world impact from the codebase's own debugging sessions". It is presented as real, but no method, sample or data is given, so treat it as an unverified assertion.

**The rest of that debugging list**
- "Systematic approach: 15-30 minutes to fix".
- "Random fixes approach: 2-3 hours of thrashing".
- "New bugs introduced: Near zero vs common".

**Observed in the test session**
- "56 raw transcripts, 88 wiki pages"; three approaches shown.

**Rule thresholds**
- "even a 1% chance".
- "2–3 approaches"; "nine-step checklist".
- "Each step is one action (2-5 minutes)"; "If a task takes longer than 5 minutes for a sub-agent... the task is too broad".
- "If < 3"; "If ≥ 3: STOP"; "DONT attempt Fix # 4".
- Word budgets "<150 words each", "<200 words total", "<500 words".
- "exactly four structured options"; "2-3 bullets"; four statuses; five review dimensions.
- "0 failures"; "exit 0".

**Illustrative or rhetorical**
- "Tests passing (47 tests, 0 failures)" is a sample report; its path is `/Users/jesse/...`, which suggests the text was lifted from another project.
- "real 5-level trace"; "four layers of validation".
- "an hour of design prevents a week of rework"; "pay back tenfold".
- "costs five minutes... costs an hour of rework".
- "retries failed operations 3 times" (test example).
- "ONE review... TWO reviews".
- "62 min read".

There are no measured time savings, costs or pass rates for the system itself.
