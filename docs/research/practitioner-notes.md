# Digest of Pedro's working notes

| | |
|---|---|
| Research date | 2026-10-03 |
| Method | Three Claude Code sub-agents read Pedro's private knowledge base (AI and LLM, software engineering, management) and reported what bears on this exercise. |
| Status | This digest is the copy of record for this repo (PLAN decision D9): the notes themselves are private and are not cited. File names below identify where in the notes an idea sits; readers of this repo cannot open them. Figures are as recorded in the notes and must be re-verified at the primary source named beside them before any use. |
| Coverage | Parts of the knowledge base were not synced to the machine and could not be read (ASSIST-003); each section lists what was missed. |
| Used for | The thesis wording, the Build / Buy / Hire / Wait framing, evaluation metrics, the journal format |

## AI and LLM notes

Scope note: the NLP index points out of the folder for most coding-agent material, so I followed those pointers (all read-only, nothing modified). All paths below are under `Practices/`.

### 1. Folder map

- **`AI/NLP/LLM.md`** (read in full) is the index: "a **map**, not a notebook", in nine layers (Foundations, Building & Running Models, Adapting Models, Prompt Engineering, RAG/Knowledge/Ontologies, Agents, Applications & Business Context, Eval, PT-BR NLP) plus a Library.
- **`AI/NLP/AI Engineering Skills Map.md`** (read in full) is the competency rubric: Andrew Ng's 2026 map crosswalked to Pedro's holdings, with findings F1–F8 on where he is short.
- **`Coding/AI/SWE in the AI era.md`** (read in full) is where the coding-assistant working material moved on 2026-08-11.
- **`AGENTIC_CONVICTION.md`** (read in full) is the sourced field brief that the wiki's `CLAUDE.md` lists as an index file.
- **`DESIGN_DOC_orchestration_layer.md`** and **`PLATFORM_ADOPTION.md`** (read in full) are his own RFC and adoption point of view.
- **`Mngmnt/Mngmnt.md`** (read §1, §2.1, §5) and **`Mngmnt/AI/AI Implementation Framework.md`** (read in full) hold the management doctrine.
- **`Coding/AI/kun-chen-podcast/model-routing.html`** (read in full) is a model-routing and quota playbook.
- The rest of `AI/NLP/` is about 28,600 files and 1.4 GB: mostly cloned repos (`ai-that-works/`, `ClaudeCode/`, `FareedKhan-dev/`, `anthropic-cookbook/`, the system-prompt corpora `CL4R1T4S/` and `leaked-system-prompts/`), books, `Papers/`, and two screenshot decks under `Agents/`.
- `AI/README.md` and `AI/NLP/Study Guide.md` are 0 bytes. `AI/NLP/Courses.md` and `Classic NLP Inventory.md` were not read (course backlog and pre-LLM catalogue).

Pedro's own caveat (`LLM.md` §1 Gaps): "No authored operating principles yet — everything here is curated, not written." The authored opinions live in `Mngmnt.md` §5.8, `AGENTIC_CONVICTION.md` and the design doc.

### 2. Key ideas, in his terminology (read directly)

**Thesis and market stance**
- "**Reliability, not capability, is the wall.**" Three shifts: **spec as source**, **orchestration as ledger**, **autonomy tracks boundedness**. "The platform is a harness around the agent, not a bet on the agent." (`AGENTIC_CONVICTION.md`)
- Market shape: synchronous in-editor "**pair**" agents versus asynchronous cloud "**delegate**" agents that return a PR; "match the class to task boundedness". (`AGENTIC_CONVICTION.md` §03)
- Entry decision: "**work shape before model before vendor**"; **Build / Buy / Hire / Wait** are capital allocation choices; "Do not automate work you cannot describe clearly"; in a thin market "the narrow test is the move"; "**Wait is a decision.** Say it out loud and set a date." (`Mngmnt.md` §5.2, §5.8)
- Whether to build a harness: "only build your own harness if you will RL a model on your tools (otherwise you fight a 40–50-person team)"; the builder's alpha is in the "**outer harness**" (orchestration, stacked loops, injected domain context); "evals are the spec that outlives everything else". (`SWE in the AI era.md` §1.4)
- Adoption: "Capability shipped ≠ adopted"; teams abandon tools that add a step; "ship a paved road, not a capability"; measure return-usage. (`PLATFORM_ADOPTION.md`)
- Brownfield is "where our money is". (`Mngmnt.md` §5.6; `SWE in the AI era.md` §1.5)

**Architecture and orchestration**
- "**Fan out reads, single-thread writes**": planner/executor plus a generate–review loop, with sub-agents for context isolation, not wide fan-out. (`AGENTIC_CONVICTION.md` §03)
- "Exhaust the single-loop stack before adding a second loop"; "parallelize last". (`SWE in the AI era.md` §1.4, §1.5)
- "**Separate the deterministic plane from the probabilistic plane**"; "delete every inference call a deterministic component can replace". (`AGENTIC_CONVICTION.md` §04)
- **Durable execution as the system of record**: a journaled workflow with LLM and tool calls as activities; "checkpoints are not durable execution"; "recovery is not retry". The design doc picks a Temporal-class spine, "bias to adopt". (`AGENTIC_CONVICTION.md` §02; design doc §3; `LLM.md` §6.2)
- Design-doc primitives: **Agent Contract** (input and output schema, tool boundary, eval spec, cost ceiling, model tier), "**provenance as schema**, not logging", an eval-harness hook, and explicit non-goals.
- The Wavestone eleven-harness study gives **seven canonical subsystems** and a 90-line minimum-viable-harness scaffold. (`LLM.md` §6.1)

**Repo understanding and context**
- No production harness uses embeddings for code retrieval; "the field runs on hand-rolled async loops plus ripgrep, tree-sitter, glob and Markdown context files". (`LLM.md` §6.1)
- Context engineering: four failure modes (**poisoning, distraction, confusion, clash**) and four strategies (**write, select, compress, isolate**); "isolation moves tokens, it does not delete them"; keep a stable prefix for the KV cache; "every single token counts". (`LLM.md` §6.6)
- Context versus memory; "files as memory, index as derived state"; the **shift-worker model** ("continuity… lives in the environment"). (`LLM.md` §6.5)
- Brownfield recipe: zone by blast radius (green/yellow/red), comprehension memo, characterization tests first, "document only what the code cannot express". (`SWE in the AI era.md` §1.5)
- Standing context is treated with caution: "a universal CLAUDE.md skews the program more incorrectly than correctly". (`SWE in the AI era.md` §1.1, §1.4)

**Tools, permissions, security**
- "Tool calls are the primitive; MCP, bash, CLIs and code mode are implementations"; the durable investment is "a good OpenAPI spec" and a tool catalog. (`SWE in the AI era.md` §1.4)
- Trust ladder: `local-only` → `direct-PR` → full gate, "never start with `+yolo`"; agents run with your OS user's permissions. (`SWE in the AI era.md` §1.3)
- **Lethal trifecta**, "three legs, break one"; "prompt injection defense is a systems problem, not a prompting problem"; "structured outputs are not a defense"; "layer fast deterministic rules before slow AI checks"; per-command approval can be "approval theatre". (`LLM.md` §6.7)
- Tool-call risk gate: a typed classifier feeds deterministic allow / review / block. (`LLM.md` §2.4, §6.7)
- PII: Class 1 gets "no LLM in the critical path". (`LLM.md` §6.7)

**Evaluation**
- Report **pass^k** and **cost-per-successful-outcome**, not pass@1; "agents cannot be their own graders". (`AGENTIC_CONVICTION.md` §04, §05.3)
- "A single leaderboard number is not evidence your agent works on your codebase." (`AGENTIC_CONVICTION.md` §04)
- Benchmarks score "did it pass", not "is it good". (`SWE in the AI era.md` §4)
- Practice: rubrics with binary pass/fail, the judge validated as a classifier, a confidence interval on every score, deterministic checks before any judge. (`LLM.md` §8)

**Human-in-the-loop and review**
- "**Review is the verifier, until the benchmarks say otherwise**"; the maintainability reward gap is "not a skill issue". (`Mngmnt.md` §5.5, §5.8)
- "'No human in the loop' should be a configuration choice justified by risk and evidence, not a default." (`SWE in the AI era.md` §1.3)
- "Anchor the spec, don't freeze it — and judge it by its contract tests." (`Mngmnt.md` §5.6, §5.8)
- Humans sit at strategic gates via a durable pause (`step.waitForEvent()`). (design doc §6; `LLM.md` §6.2, §6.8)

**Observability, cost, latency**
- Instrument by default with wide, typed, structured events; "roll back first, investigate later"; product metrics tied to AI quality. (`LLM.md` §6.2)
- "Never report a throughput number without its paired quality number." (`Mngmnt.md` §5.4)
- Model routing by task and reasoning effort; "a model that isn't smart enough just burns tokens failing". (`model-routing.html`)
- Time to first token drives perceived latency; throughput sets capacity. (`LLM.md` §2.2)

### 3. Numbers, quoted exactly

From `AGENTIC_CONVICTION.md`:
- METR RCT: "**−19%**… while estimating they were 20% faster".
- METR horizons: Claude Opus 4.5 "320 min (5.3 hr)", GPT-5 "214 min"; the 80%-reliability horizon "is ~1/5 of it".
- pass^k: "A 90% pass@1 agent is only ~57% reliable at k=8"; GPT-4o ">60%… drops to <25% at pass^8".
- Cost: "E[cost per solved task] = C_attempt / p_success"; "when cleanup costs >5–10× an attempt, reliability dominates model choice".
- Agent success "~58% single-turn to ~35% multi-turn".
- Multi-agent: "+90.2%… at ~15× the tokens".
- SWE-Bench+ audit: "32.67%" solution leakage, "31.08%" passed on inadequate tests; "59.4%" of o3 failures were harness flaws.
- SWE-bench Pro: "GPT-5 23.3% · Opus 4.1 23.1% at launch".
- SWE Refactor Bench: "28 of 520 runs (5.4%)"; VB6→C#: "70% average… 92% on low-complexity features, 47% on high", tokens "1.47M tokens / $1.66 → 9.09M / $10.28 per feature".
- QuestBench "40–50%"; non-existent packages "~20%", "43%" recur; sabotage "12%".
- Context rot: "a 200K window can show serious loss by ~50K tokens".
- Determinism costs "~30–60% throughput".
- Veracode: "45%", "2.74×".
- Stack Overflow trust "29%"; MIT "95%"; DORA adoption "90%".
- Devin: merge rate "34%→67%".

From `Mngmnt.md` §5.3 and §5.7:
- Faros 2025: tasks "+21%", PRs merged "+98%", review time "+91%", bugs "+9%", PR size "+154%".
- Faros 2026: "60% of AI-generated code is now accepted"; code tasks "+210%", bugs "+54%", review time "5x", unreviewed merges "+31%".
- Team-level: "most organisations land at 1.1–1.3x; top performers reach 2–5x".

From `LLM.md`:
- §6.1: SKILL.md "9/11 vs 8/11" MCP; "ACP ships in six systems"; "~4M-LOC corpus".
- §6.6: "lead-context payload down 18%, total tree tokens up 621%"; the engineered agent "cost 4.93× as much"; context precision "27 → 60 → 100%".
- §2.4 risk gate: "median 242.6 ms vs 1,511.5 ms (~6.2×) and roughly 82× cheaper" (n=40, flagged as "an indication, not a benchmark").
- §6.7: Haiku 4.5 compromised, Sonnet 5 and Opus 5 refused; MINJA "98.2% inject success rate".
- §6.2: Anthropic postmortem "~30% of Claude Code users".
- §8: "84% vs. 88% on 50 traces… ≈1,200 traces per version"; hand-label "~100 traces, split ~20 / 40 / 40".

From `SWE in the AI era.md`:
- §4: SlopCodeBench "~33% strict"; "5× cost for ~2 points".
- §1.3: "90% of 3,500 engineers" (Block); Kun Chen API cost ">$10k"; the Axi wrapper cuts cost ">20%".

Pedro tags many of these as vendor claims or snapshots; keep his caveats attached.

### 4. Gaps against the design list

Named as gaps in the notes themselves:
- **Codebase search/retrieval**: "no material" beyond the Wavestone finding (Skills Map §5.5).
- **Hooks, permissions, standing-context conventions**: catalogued, "authored half… still to write" (`SWE in the AI era.md` §1.4).
- **Governance, incident response to an injection event, an exfiltration design checklist**: "still empty" (`LLM.md` §6.7).
- **Drift detection and statistical regression testing in CI/CD** (Skills Map F4).
- **Evaluating assistant output quality** as own practice (`SWE in the AI era.md` Gaps).
- **Governance template for regulated industries** and a **definition-of-good checklist** per work type (`Mngmnt.md` §5.8).

Not found in what I read (my inference):
- No market sizing, competitor pricing, or unit economics for a coding-agent product.
- No latency targets or SLOs.
- No customer-code privacy or data-residency design (only PII redaction).
- No sandbox implementation detail.
- No model-selection rubric beyond the Kun Chen snapshot.
- Nothing labelled "redlines". The nearest are "never start with `+yolo`", "no LLM in the critical path" for Class 1 data, and "no unconstrained autonomy".

Also my inference: the notes lean towards an outer harness with verification on an existing harness, brownfield first, with adoption as the success metric. The notes never state that as a conclusion about this market.

### 5. Not read

- **0 bytes (Dropbox online-only):** `AI/README.md`, `AI/NLP/Study Guide.md`, `Mngmnt/AI/Spec-Driven Development.md`, every PDF in `Papers/` except the τ²-Bench one, all epubs, and most loose PDFs (Baseten, Anthropic threat report, LLM Mesh).
- **Not opened:** the `.pptx` decks; the screenshot decks `Agents/Factory/` and `Agents/Hlyr - No vibes allowed/`; `ClaudeCode/` PDFs; cloned repos, including `ai-that-works/` episode folders (known only via Pedro's summaries); `kun-chen-podcast/firstmate-herdr-pi-setup.md`; `Courses.md`.

## Software engineering notes

### Scope and reliability caveat (read first)

The folder on this machine is only partly synced. `Coding Inventory.md` describes about 23,280 files / 5.9 GB across 11 shelves, but locally there are 16,245 files / 564 MB, and most of the reading library is absent or a 0-byte Dropbox placeholder. The usable material comes down to five things, all read in full:

- `Coding Inventory.md` (the only non-empty index)
- `AI/SWE in the AI era.md`
- `AI/agentic-ai-and-code-reviews.pdf`
- `AI/kun-chen-podcast/` (`README.md`, `firstmate-herdr-pi-setup.md`, `model-routing.html`)
- `Workspace/goplay/GoTest/` (`IMPLEMENTATION_PLAN.md`, `go-backend/DESIGN_DECISIONS.md`, `TEST_SUMMARY.md`)

The inventory itself says the library has "no authored notes" — it "records what was read, not what was concluded". So almost everything below is Pedro's curation and digest of other people's work, not his first-hand practice. There is nothing in the folder on commit-style policy, CI/CD configuration, or a formal ADR template.

All paths below are relative to `Practices/Coding/`.

### 1. Folder map

**Index files (root)**
- `Coding Inventory.md` — the real index: §1 root files, §2–9 reading shelves, §10–12 `Workspace/` + `Clones/`, §13 temporal cut, §14 weeding, §15 gaps, §16 cleanup log.
- `README.md` — 0 bytes (modified Sep 29), unreadable.

**Shelves present locally**
- `AI/` — the one live, authored shelf.
  - `SWE in the AI era.md` (505 lines, last modified 2026-10-02): "the engineering-practice map for building software with agents".
  - `agentic-ai-and-code-reviews.pdf`: IT Revolution, Enterprise Technology Leadership Journal, Fall 2026.
  - `kun-chen-podcast/`: setup recipe and model-routing playbook from the author of firstmate / no-mistakes / lavish-axi.
- `Workspace/` — own code.
  - `goplay/`: Go scratch plus many cloned repos.
  - `goplay/GoTest/`: a Go/Node/React exercise with plan, design decisions and tests.
  - `pydesk/`: Python DS&A scratch.
  - `rustdesk/part-06-gist.rs`: see section 4.
- `Clones/` — 8 reference repos, all 0-byte placeholders.

**Listed in the inventory but not on disk**
`Algorithms/`, `Books/`, `Databases/`, `DevOps/`, `EngSoft/`, `OO/`, `Programming Languages/`, `TechRadar/`. These would have held the testing, SRE, CI/CD and architecture canon (Accelerate, DevOps Handbook, Release It!, Team Topologies, Ousterhout, SE at Google).

**Pointers out of the folder (not read; outside the path you gave)**
- `Practices/Mngmnt/Mngmnt.md` §5 and `Mngmnt/AI/Spec-Driven Development.md` — doctrine, evidence base, metrics.
- `Practices/AI/NLP/LLM.md` §6 — harness anatomy, including the Wavestone study.
- `Practices/AI/NLP/ClaudeCode/` and `AI/NLP/ai-that-works/`.
- `Practices/Architecture/` and `Practices/CLAUDE.md`.
- `AGENTIC_CONVICTION.md`.

These are probably the richer sources for the evidence base and are worth a follow-up pass.

### 2. Practices and opinions

#### (a) Product thesis: pain points in the SDLC

All from `AI/SWE in the AI era.md` unless noted.

- **Review and verification is the bottleneck, not generation** (§4, §1.3). "Review is the verifier"; "There is no training reward for maintainability, so the model won't protect it for you". The PDF agrees: "generating code is cheap, but organizational attention is not", and review becomes "a layered verification system instead of a single human merge gate".
- **Throughput and quality debt arrive together** (§4). "The throughput gain and the quality debt are the same event."
- **Benchmarks do not measure slop or long-term maintainability** (§4). "no benchmark catches the bug that shows up six months later".
- **Brownfield is "where our money is"** (§1.5). The constraints live outside the code, so agents produce code that "works" and quietly adds debt. Osmani's nine practices are digested there: zone by blast radius, durable comprehension memo, characterization tests first, completeness over breadth, harness as institutional memory, zero-risk work first, measure beyond lines, parallelize last, document only what code cannot express.
- **The line he marks "worth keeping above all"** (§1.5): "Agents have changed the price of trying several plausible implementations. They haven't changed the evidence required to choose one."
- **Context and token economy are first-class skills** (§4, §1.4). Every skill, sub-agent and MCP description is charged to context on every turn.
- **Weak human-to-agent feedback on rich artifacts** (§1.3, lavish-axi) and **babysitting parallel sessions** (§1.3, firstmate).
- **Tasks he says the practice now requires** (§1.3): multi-agent orchestration, process discipline for agents, automated pre-merge verification, structured artifact review, risk-tiered layered verification, separating deletion from construction.
- **Self-declared gaps** (§Gaps): the bug-report-to-fix workflow, evaluating assistant output quality, harness-configuration craft, and codebase search/retrieval.
- **Ng's four failure modes** (§Gaps): overengineering, losing rigor without an explicit verification step, stopping short of the goal, destructive actions on files or production data.

#### (b) How the prototype repo should be built

**Harness design** (`AI/SWE in the AI era.md` §1.4)
- "The harness is the operating system around the agent, and the agent is the while-true loop."
- "Exhaust the single-loop stack before adding a second loop."
- Only build your own harness if you will RL a model on your tools; the builder's alpha is in the outer harness (orchestration, stacked loops, injected domain context).
- From the Wavestone study he cites: "no production harness imports an agentic framework, and none retrieves code with embeddings."
- "Tool calls are the primitive; MCP, bash, CLIs and code mode are implementations." Shape tool output so only what matters enters context.
- "Evals are the spec that outlives everything else."

**Specs and documentation** (§1.1, §1.5)
- "Anchor, don't freeze": a lightweight spec kept alive alongside the code. "The nearest existing artifact shape is an ADR."
- "Contract tests are the load-bearing element, not the spec."
- Rigor per work type: spec-anchored for large or long-lived work, no formal spec for small fixes.
- Research → Plan → Implement loop.
- A standard "what deviated from the plan" section in every PR. This maps well onto JOURNAL.md.
- "Markdown for models, HTML for humans."
- "Write down what the code can't say, and nothing else."
- He is sceptical of a universal CLAUDE.md. He quotes Dex: "A universal CLAUDE.md skews the program more incorrectly than correctly most of the time." His own convention is "not written".

**Verification** (§1.1, §1.3 and the PDF)
- Wire feedback sensors (linters, tests, type checkers) so errors are fixed before reaching a human.
- Deterministic checks before AI review.
- Adversarial review by a separate model or separate session.
- Small incremental changes.
- "'No human in the loop' should be a configuration choice justified by risk and evidence, not a default."
- Three conditions before removing humans: deterministic checks, a risk-tiered review stack, and a durable inspectable record of every agentic decision.

**Isolation and security** (§1.4, `AI/kun-chen-podcast/firstmate-herdr-pi-setup.md`)
- Git worktrees are the isolation primitive for parallel agents.
- Trust ladder: `local-only`, then `direct-PR`, then the full gate; never start with `+yolo`.
- Agents run with the user's permissions, so use a dedicated OS user, container or sandbox. Never paste secrets into chat.

**Stack, commit, test and decision-record style** (`Workspace/goplay/GoTest/`)

Provenance caveat: this is a exercise the inventory calls "own work". The plan may have been agent-assisted; I cannot tell.

- **Stack.** Go is the most current authored language ("Go consolidation", inventory §13). Design decision 5 is "No external dependencies", standard library only. Python is used for scratch work.
- **Commits.** `IMPLEMENTATION_PLAN.md` has a "Commit Strategy": "One commit per step, made after the step passes manual verification", with conventional-commit prefixes. Example: `feat: add request logging middleware`; also `test:` and `docs:`.
- **Tests.** Unit plus `httptest` integration tests, a fresh store per test, no shared global state, run with `go test -v -race -cover ./...`. The plan says "aim for **>70%**"; that threshold comes from the exercise's own checklist.
- **Decision records.** `go-backend/DESIGN_DECISIONS.md` is a numbered list. Each entry has a title, the decision, the rationale, and sometimes "Alternative considered: … Rejected as …" plus a note on what would change at production scale. There is no status, date or consequences field. This is the closest thing to an ADR format in the folder.
- **Plan style.** Each step has Goal, signatures, error-mapping table and "Checklist items covered", followed by a requirement-to-step cross-reference table. A good model for PLAN.md.

### 3. Numbers and citations (exact quotes)

**`AI/SWE in the AI era.md`**
- §4: "+210% code tasks next to +54% bugs and 5x review time". The source is attributed to `Mngmnt.md` §5.3–5.5 (DORA 2025, Faros), which I did not read.
- §4: "METR's result (seniors on brownfield felt 20% faster, measured 19% slower)".
- §4, SlopCodeBench: "best models at ~33% strict"; "a 5× cost for ~2 points"; "*planning did not move the needle*". Flagged as a snapshot.
- §1.3: "90% of 3,500 engineers using AI daily by mid-2025" (Block).
- §1.3 star counts: firstmate "~3.2k★", no-mistakes "~7.6k★", lavish-axi "~2.7k★", Superpowers "~270k★ … possibly a display anomaly; treat with care".
- §1.4: "~4M-LOC scale"; "a 40–50-person team"; "a 1% gain compounds over 500 calls".
- §1.1: "one spec drew 112 comments across seven sub-pages before code".
- §1.5: Asana "multi-year backlog for ~$12,000" (vendor-reported); "Stripe's 3.7M-line TypeScript migration used codemods, not agents"; Bun "~50 workflows over 11 days"; Shopify "12-week" rewrite.
- §2: Headroom "60–95% token-reduction numbers are the vendor's own claims"; graphiti "~30k★".

**`AI/kun-chen-podcast/model-routing.html`**
- "His past month at API prices would have cost over $10,000."
- Chrome DevTools Axi wrapper "cuts average cost by over 20%".
- "GitHub CLI beats the GitHub MCP server in every way".
- Wishlist: "a higher tier than $200".
- Caveat in the source: "treat the numbers as a snapshot".

**`AI/agentic-ai-and-code-reviews.pdf`**
- Cloudflare: "Over a one-month period from March to April 2026, Cloudflare reported 131,246 completed review runs across 48,095 PRs in 5,169 repositories." Also "159,103 findings … averaging about 1.2 findings per review".
- Block: "by mid-2025, 90% of Block's 3,500 engineers were using AI tools daily".
- DryRun: "useful feedback in thirty seconds".
- Academic citations in the paper: Bacchelli & Bird, ICSE 2013; Mäntylä & Lassenius, IEEE TSE 35(3), 2009; Beller et al., MSR 2014.
- Pedro's own caveat on this paper: "Journal issue is GitLab-sponsored and the case study is self-reported by practitioners — patterns, not benchmarks."

### 4. AI coding tools specifically

**Read directly**
- **Active study focus is Claude Code** (`SWE in the AI era.md` §1.2): remote control, sub-agents and teams.
- **Skills he actually runs** (§1.4): `/code-review` and `/security-review`, plus a wiki `file-material` skill.
- **Skills he wants to build** (§3): DB access, read OpenAI logs, read Datadog, bug-report fixing, read Linear and act, remote, Playwright testing. This is effectively a demand list for integrations.
- **What he rates positively:** pre-push quality gates (no-mistakes), worktree isolation, skills for on-demand instructions versus sub-agents for context isolation, CLIs over MCP for token efficiency, and adversarial cross-model review.
- **What he is sceptical of:**
  - Vendor-reported numbers, which he flags repeatedly.
  - Standing context files that go stale.
  - Instructional skills that "detune a model that has moved past them".
  - Parallelising before a single loop is reliable.
  - "Ultra" fan-out modes ("a token bonfire", Kun Chen).
  - Spec-driven development as a freeze; he records Beck's "waterfall wearing a new coat".
- **Limitations he records:**
  - Models are weak at incremental change while "maintaining two states of the system at the same time", so run a delete-only pass and then start a fresh context.
  - Decisions are lost on compaction.
  - Plausible code is not working code.
  - AI reviewers are weaker on architectural judgment, cross-system impact, subtle concurrency bugs and very large change sets (Cloudflare, PDF).
  - Noisy AI review destroys trust (Block, PDF).
- **Adoption status** (§Gaps): the resources are "catalogued, not adopted" and "Superpowers vs. firstmate vs. our own loop is untested".
- **`Workspace/rustdesk/part-06-gist.rs`** (683 lines): this is not Pedro's code. The header credits Enzo Lombardi, "Building AI Agents in Rust - Part 6", Eugene v0.6. It is a minimal single-loop agent with a `Provider` trait over Anthropic Messages and OpenAI Chat Completions, one sandboxed `read_file` tool, `MAX_TURNS = 6` and `MAX_FILE_CHARS = 4_000`. It is a ready reference shape for a smallest-credible prototype.

**My inferences (not stated in the notes)**
- The notes point the product wedge at verification, review and brownfield context rather than code generation. That is where he sees unmet need and his own gaps.
- The prototype is best built as a single while-loop with a few well-shaped tools, no agent framework, no embeddings retrieval, a provider abstraction, sandboxed file access, a deterministic check gate, and an eval set from day one.
- JOURNAL.md entries could follow the `DESIGN_DECISIONS.md` shape (decision, rationale, alternative rejected, what changes at scale) plus a "what deviated from the plan" section.
- Go with standard library only, or Python, fits his demonstrated habits. No explicit stack preference is stated anywhere.

### Could not read

- **0-byte placeholders at root:** `README.md`, `Effective_Engineer.md`, `Code-Review-E-book-2.pdf`, `QConNY2018-MikeMcGarr-…pdf`, `SpringOne2017-…CDD….pdf`, `TheInfoQeMag-QCon-2018-Retrospective….pdf`, `E-mag-etica-….pdf`, `BrazilTaxGuide.docx`, `.gitconfig`.
- **Not on disk at all:** the eight reading shelves listed in section 1.
- **Not opened:** `AI/kun-chen-podcast/wezterm.lua` and `styles.css` (terminal config and stylesheet, irrelevant); the cloned third-party repos under `Workspace/goplay/`; and the rest of `GoTest/` (`TEST_REQUIREMENTS.md`, the READMEs and the Go source — I only listed these).

## Management notes

Root: `Practices/Mngmnt`

**Headline:** the notes hold a strong build/buy/hire/wait framework, an audience-framing model, a measurement ladder and an evidence base, but no templates for proposals, executive memos, roadmaps, ADRs or decision journals. Most of the folder is not on this machine (0-byte Dropbox placeholders), including the whole `Strategy/` and `Product Mngmnt/` shelves.

### 1. Folder map

Two index files organise everything:
- `Mngmnt.md` (850 lines, read in full) is "the main map", in seven layers: 1 Foundations, 2 Verticals, 3 Roles, 4 Competencies & Practices, 5 Management in the AI era, 6 Templates & Tooling, 7 Library.
- `Mngmnt Inventory.md` (read in full) is the contents catalogue of 25 top-level folders.

Present locally with content:
- `AI/AI Implementation Framework.md` and `AI/Mngmnt in AI era.md` (both read in full).
- Four PDFs in `AI/`: DORA 2025, Faros July 2025, Faros 2026, Faros token-efficiency guide (text extracted; key figures checked).
- `AI/The Harness is Not Enough_ Why Software Factories Fail.pptx` (slide text extracted).
- `AI/PM after AI, Agile/` — 20 McKinsey screenshots; I viewed 9.

Not readable:
- **Catalogued but absent on disk:** `Strategy/` (Gartner *Art of the 1-Page Strategy*, Wardley maps, OKR/5W2H templates, storytelling decks), `Product Mngmnt/`, `IT Governance/`, `Project Mngmnt/`, `Innovation/`, `Entrepreneurship/` (Sequoia pitch template), `Architect/` (`ARCH_DECISIONS_OPTION_EXAMPLE.pptx`), `Verticals/`, `managers-playbook/`.
- **0-byte placeholders:** `README.md`, `Verticals Inventory.md`, `engineer-manager.md`, `AI/PM after AI, Agile.md`, `AI/Spec-Driven Development.md`, `AI/dexhorthy-software-factory-thread.png`, all of `figures/`, all 8 files in `Decision & Problem Solving/`, the screenshot folders `AI/AI Implementation Framework/` and `AI/Mngmnt in AI era/`, the Faros *Engineering Productivity Handbook*, the Fournier PDF, the EM checklist docx, and nearly all of `People Mngmnt/`.
- **Not opened (out of scope or low relevance):** two epubs (Zhuo; *Scaling People*); `Coding/AI/SWE in the AI era.md` and `AGENTIC_CONVICTION.md`, which `Mngmnt.md` cites but which sit outside the folder.

### 2. Frameworks, principles and opinions (read directly; all in `Mngmnt.md` unless noted)

**Investment decision — §5.2 and `AI/AI Implementation Framework.md`** (source: Nate B Jones)
- "Build, buy, hire, and wait are capital allocation choices", not tooling choices:
  - **Build** = OWN, when the work is specific to you.
  - **Buy** = RENT, when the category is mature.
  - **Hire** = TALENT, when the work needs judgment.
  - **Wait** = TIME, when later is genuinely right.
- Selection rule: "Specificity plus market maturity points to the right lever."
- Decision order: "The work shape sits upstream of models and vendors" — work shape, then model, then vendor.
- Gates before funding:
  - "Do not automate work you cannot describe clearly." Pedro calls it "the cheapest governance rule I have… defensible to a sceptical exec without any data."
  - Task edges plus a definition of *good*: "without a verifier there's no build."
  - "One AI ask can hide many different workflows."
  - "If nobody can define the standard, hire the person first."
- Sequencing ("Stack Bets"): FIRST high leverage, now; NEXT learning, at team level; LATER low priority, wait.
- Thin market: "the big contract is the trap and the narrow test is the move"; buy primitives, not whole-workflow vendors.
- "Wait on purpose", said out loud with a review date, "or it reads as drift."

**Foundations — §1**
- "Complexity should have benefits — default to radical simplicity."
- "Engineering process should match product maturity."
- "Copying common approaches is rarely a shortcut — figure out what works for you."
- "Functionality is an asset; code is a liability."
- "Dogfood the platform."
- "Fall back to principles."
- "Start by understanding users and their problems. Build trust through the smallest, tiniest wins, repeated."
- The **People / Technology / Initiatives triangle** is his framing lens.
- "Distillation, not just replacement": "'what to build' becomes the scarce skill."
- "Management is the ability to soften chaos created by leaders."

**Executive communication — §4.2**
- Two steps: "Identify what your audience cares about. Use language that puts their needs first."
- Three audiences: the **Approver** (strategic fit), the **Spend authorizer** (cost and customer-data protection), the **Implementer** (rollout process).
- Calibrate by "impact to the listener", not preference.
- §2.2: "Quantifiable value is the bar."
- §5.1 "How to argue this": argue in bundle terms, never headcount terms.

**Decision and risk — §4.5**
- Decision loop: 1 Define the problem; 2 Check assumptions; 3 Generate and evaluate solutions; 4 Choose a solution, assessing risks; 5 Execute, check, act accordingly.
- "Identify and prioritize risks — have a contingency plan per risk."
- Opportunity cost is defined with the worked example in section 4 below.
- SLI / SLO / error budget; PDCA.

**Roles — §3.1**
- The VPE owns people management, product strategy, budget, operations and execution, recruiting, planning and processes.
- "Your team handles the six-month problems, while you figure out what the organization needs to look like two years from now."

**Metrics — §5.4**
- Layer 1: DORA and SPACE.
- Layer 2: token efficiency (Faros: 3 outcome signals plus 11 guardrails).
- Layer 3: the economic ladder, "Inputs → outputs → outcomes → economic outcomes", north-starred on cost per PR against ACU cost.
- Operating rule: "never report a throughput number without its paired quality number."
- Corollaries: "licence counts are not adoption"; "an AI review stage that doesn't remove a human stage is not a saving."

**AI-era product theses — §5.3 and §5.5–5.8**
- "The throughput gains are real, the quality debt is real, the two are the same event."
- The maintainability reward gap: "Code review… is currently your only verifier."
- "You don't have too many PRs, you have too many bad PRs."
- Spec-anchored over spec-first or spec-as-source: "A spec nobody enforces is a wish"; "Don't buy an SDD product; adopt a rung."
- "Brownfield is where our money is."
- "AI is an amplifier, so fix the system first."
- "Wait is a decision."
- "Name the owner" (Block's DRI model).

**Team sizing and organisation — §5.7** (McKinsey; screenshots viewed)
- Two-pizza pods of 8–10 become one-pizza pods of 3–5 (Product definer, Lead builder, Product builders), with twice the number of pods.
- "One operating model per tech function"; "expect 3–5 models."
- "Change the review template before changing the org chart."

**Roadmap and delivery — §4.3**
- "Insist on prioritizing and delivering value incrementally."
- Nine prioritisation rules.
- §6.4 sprint cadence: Daily → sprint goals → sprint review → sprint demo.

### 3. Templates and structures

None of the requested templates exist in the readable material. The closest items:
- **ADR:** one sentence only, in §5.6: "The closest thing to a spec-anchored doc we already run is an ADR: small, durable, revised when reality moves."
- **§6 Templates & Tooling** holds only:
  - 6.1 EM checklist (docx, unreadable);
  - 6.2 Tech-debt checklist (10 items);
  - 6.3 Team productivity and well-being self-assessment (10 items);
  - 6.4 Sprint cadence;
  - 6.5 Decision loop (the five steps above).
- **Economic ladder** (McKinsey slide 21, viewed), usable as a measurement skeleton:
  - North star goal: "Multiple of cost per PR / ACU cost across all PRs generated over X timeframe"; "% reinvestment in greenfield and brownfield development".
  - Economic outcomes: time to revenue target; $ for every new feature with new teams developed; per team cost reduction.
  - Outcomes: Velocity, Capacity, Security, Quality, Resiliency.
  - Outputs: breadth and depth of adoption; number of people upskilled; developer NPS and attrition rate.
  - Inputs: $ investment in AI coding/dev tools; $ and time in training; $ and time in change management.
- **Faros 14 metrics** (`AI/Faros_Field_Guide_to_Measuring_Token_Efficiency.pdf`), each tied to "the decision it drives", in four categories:
  - Adoption: license utilization rate; usage depth distribution; tool preference relative to licenses; code acceptance rate by tool.
  - Productivity: PR merge rate per developer by tool; cycle time by stage; lead time.
  - Quality: bugs per developer, trended; incidents per PR, trended; PRs merged without any review; AI footprint by repo.
  - Outcomes: productive vs. wasteful token spend; token spend by tool, normalized to output; alignment of spend to strategic work.

**Inference, not in the notes:** a proposal in his voice would chain work shape → four levers → gates → Stack Bets → paired metrics → review date.

### 4. Numbers and citations (exact)

**Faros 2025** — `AI/AI_Engineering_Impact_Report_July_2025_Faros_AI.pdf`, verified in the PDF
- "1,255 teams and over 10,000 developers".
- "21% more tasks", "98% more pull requests", PR review time "increased by 91%", "9% increase in bugs per developer", "154% increase in average PR size".
- "Lead time, change failure rate: unchanged" is `Mngmnt.md`'s wording; I did not check it in the PDF.

**Faros 2026** — `AI/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf`, verified in the PDF
- "22,000 developers and 4,000 teams", two years.
- "60% acceptance rate of AI-generated code (up from 20%)".
- "Task completion is up 34%. Epics completed per developer are up 66%. Tasks involving code specifically have increased 210%."
- "Bugs per developer are up 54%. The incidents-to-PR ratio has more than tripled. Median review time has increased 5X. 31% more PRs are merging without any review."
- In the PDF but not in his map:
  - "+16.2% PR merge rate per developer" ("considerably lower than the 98% increase in our 2025 report");
  - "+861% code churn";
  - "-11% deployments per week (measured by 10% of the dataset)";
  - "+480.4% Lead time from code commit to production (measured by 10% of dataset)";
  - "+242.7% incidents per PR";
  - PR size "+51.3%… down from the 154%";
  - "25% of PRs are reviewed by AI agents"; "<1% of PRs are opened by AI agents".
- `Mngmnt.md`'s claim that this holds "across every segment regardless of engineering maturity" was not checked in the PDF.

**DORA 2025** — `AI/2025_state_of_ai_assisted_software_development.pdf`
- "nearly 5,000 technology professionals"; "more than 100 hours of qualitative data".
- "(90%) use AI"; "more than 80%" believe it increased productivity; "(30%) currently report little to no trust in the code generated by AI".
- "AI's primary role… is that of an amplifier."
- Seven AI capabilities: clear and communicated AI stance; healthy data ecosystems; AI-accessible internal data; strong version control practices; working in small batches; user-centric focus; quality internal platforms.

**McKinsey** — Harrysson & Maniar, "Moving Away From Agile: What's Next?", screenshots in `AI/PM after AI, Agile/`
- Code reviews "7x" (GitHub Copilot); refactors and prototyping "2-5x" (Cursor at Monday.com); ETL platform migration "12x" (Devin at Nubank); unit test development "7x" (Cursor at Salesforce).
- "Most organizations are at productivity of 1.1-1.3x… top performers can achieve 2-5x".
- Slide footnote: "16-30% productivity improvements (2025 McKinsey survey), 39% increase in merges/PR (2025 UChicago study…)".
- From `Mngmnt.md` only, slide not viewed: roles reshaped "(n=300): software engineer 71%… product manager 69%… testing/QA 57%".

**Horthy deck** — `AI/The Harness is Not Enough…pptx`, verified in slide text
- "~15 min tasks"; "Binary rewards on FAIL_TO_PASS + PASS_TO_PASS".
- "agents start to struggle after 3-6 months".
- "even 20% rework is a burden".
- Benchmarks: SWE-Marathon (4-400h tasks, 18-channel reward), DeepSWE (90min cap), Frontier Code.

**From `Mngmnt.md` only — primary sources not available**
- §5.6: "METR — 16 experienced seniors on brownfield repos over 1M lines felt 20% faster and measured 19% slower".
- §5.6: "8 spec files and ~1,300 lines of spec, with ~80% of the time going into reading documentation".
- §5.6: "5.4% of whole-repository migration runs fully pass on SWE Refactor Bench"; VB6 → C# "from 92% to 47% behavioural equivalence".
- §5.6: Thoughtworks Radar put SDD in *Assess*, Nov 2025.
- §5.6: Kent Beck quote dated 8 Jan 2026.
- §5.8: the Beck/Tacho/Yegge closing quote.
- §2.2 Gartner (Weiss, 2021, N=286): "8% Ambition / 11% Design / 29% Deliver / 35% Scale / 16% Refine".
- §4.5 opportunity-cost example: "Project A 25k; Project B 20k; Project C 10k… OpCost = 20k".

**Gaps Pedro flags himself (§5.8 and backlog):** a GenAI governance template for regulated industries; a definition-of-good checklist per work type; a 30-day paired-metric dashboard spec; a spec-anchored brownfield pilot design.
