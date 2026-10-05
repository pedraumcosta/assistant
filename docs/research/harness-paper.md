# Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems

| | |
|---|---|
| Authors | Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger (Wavestone AI Lab) |
| Reference | arXiv 2609.00006v1 [cs.SE], 15 July 2026, CC BY 4.0 |
| Source | https://arxiv.org/abs/2609.00006v1 |
| Read on | 2026-10-05, from the arXiv HTML full text converted to plain text |
| Method | Two reads. The main Claude Code session read selected sections directly (landscape, OpenHands, platform economics, the meta-harness, recommendations, conclusion). A sub-agent then read the whole text end to end and wrote the record below. |
| Status | Digest with quotations, not a copy of the paper. Quotations in `EVIDENCE.md` rows E-30 to E-33 were read directly from the text. Benchmark figures in the paper are self-reported by the systems' authors, as the paper itself says. |
| Used for | PLAN §1.1 (narrowing the thesis, decision D1), DESIGN, prototype design |

## Why this paper matters to the decision

Pedro asked for it to be weighed before closing D1. It changed the plan in two ways:

1. It confirmed that the inner agent loop is a commodity, which supports writing a minimal loop only as the agent under test.
2. It showed that the outer policy, sandbox and budget layer is also being commoditised (Omnigent, OpenHands), which removed that layer from our proposal and narrowed the thesis to the evidence layer and per-repo evaluation.

After the full read, one earlier statement needs qualifying. The plan said no system checks the outcome of the agent's work. More precisely: two systems have an outer verification loop (OpenHands with a model judge, Hermes with a verify-on-stop guard), and Aider runs lint and tests inside its loop. None is described as a deterministic gate that runs after the agent stops and keeps an evidence record, and the paper reports no false-pass rates.

## Read record

Read the whole converted text sequentially, through the References. arXiv 2609.00006v1 [cs.SE], dated 15 Jul 2026, CC BY 4.0.

Authors and affiliation as printed: Paul Barbaste (lead and corresponding author; "Inclusive Brains" and "Wavestone AI Lab" both appear under his name), Tristan Darrigol, Germain Vu, Tom Wiltberger (all "Wavestone AI Lab").

Length note: this record runs to about 3,800 words, over the 3,000 requested, because the mandated lists (13 observations, 29 patterns, 18 recommendations, eleven systems, the figures) do not fit in less without dropping items.

Conversion caveat: the HTML flattening dropped some symbols and numbers (multiplication signs, arrows, inequality signs, a few numeric values). Where a number is missing in the text I say so rather than restore it.

## Scope of the paper

**Corpus (Table 3, pinned July 2026).** OpenHands V1 SDK v1.34.0; Aider v0.86.3.dev (May 2026, maintenance mode); Claude Code "source snapshot Mar. 2026 (binary 2.1.206, Jul. 2026)"; Codex rust-v0.144.1; Gemini CLI v0.50.0; Mistral Vibe v2.19.1; Mini-SWE-Agent v2.4.5; Hermes 0.18.2 (rel. 2026.7.7.2); Pi v0.80.6; OpenCode v1.17.18; OpenClaw v2026.6.11.

**Contrast points.** OpenClaw is inside the eleven but is a "personal AI assistant gateway" with no native code-editing tool; the paper gives 10-system counts where that matters. Omnigent v0.4.0 (Databricks) is a twelfth tree, a meta-harness, not scored on the seven dimensions.

**Method.** Source-code reading, dependency-manifest inspection and import grep; no runtime measurement, no shared task set: "It does not benchmark or rank". Eight systems were also audited in an April 2026 edition and re-pinned, giving a one-quarter source diff. Landscape events (Section 3.7) are "not source-verified".

**Harness.** "An agent is a model plus a harness. The harness is everything except the model". It is not an agentic framework, not an evaluation harness ("Same word, opposite direction of wrapping"), and not an orchestrator.

**Seven subsystems (Table 1), minimal to maximal form.**

| Subsystem | Minimal | Maximal |
|---|---|---|
| Agent loop | Mini-SWE-Agent: linear `while` over one bash tool | OpenHands: event-sourced conversation over a persistent event log, parallel action batches |
| LLM integration | Mini-SWE-Agent: one LiteLLM call, one Jinja template | Hermes: five owned transports, 29 provider profiles; Codex: server-delivered model catalog |
| Tools and actions | Mini-SWE-Agent: bash only | Claude Code: 43 typed tools with deferred loading; Codex: tool calls as V8-executed code |
| Memory and context | Mini-SWE-Agent: unbounded linear history | Codex: agent-maintained cross-session memory; Gemini CLI: graph-based context distillation |
| Safety and permissions | Mini-SWE-Agent: cost and step limits | Codex: policy rules + LLM approval reviewer + three-platform OS sandbox |
| Orchestration | Aider: none | Claude Code: recursive composition; Omnigent: cross-vendor coordination |
| Extensibility | Mini-SWE-Agent: Python protocols | Pi: everything-is-an-extension runtime; Codex: marketplace-distributed plugins |

Two cross-cutting surfaces sit alongside: the interface layer and the session substrate.

## Observations

Numbering note: in this text the boxes are labelled "Observation 1" to "Observation 13"; cross-references elsewhere cite them by section ("Observation 7.1", "13.2"). Both are given. Observations 12 and 13 are never cross-referenced by section number.

1. (cited as "Observation 5") Systems "span three orders of magnitude in code size while targeting similar tasks, yet loop sophistication does not predict benchmark performance"; most mass addresses "safety, user experience, extensibility—and increasingly clients and transport".
2. (7.1) Provider-native optimizations "are not gated on tight coupling; they are gated on who pays the per-provider conditional-code cost". What vendors keep is "server-side co-evolution".
3. (7.3) "Prompt rhetoric converges where engineering experience converges, then thins as trust calibrates." Invariant: "no policy-level refusal language anywhere".
4. (8.4) File-editing strategy "is one of the most important determinants of code-modification accuracy", and "model-aware polymorphism is no longer Aider's alone".
5. (9.6) "Persistent memory has replaced compaction as the frontier of context engineering"; four governance models for the memory write path; none uses embeddings as primary memory substrate.
6. (10.2) OS-level sandboxing is "one of the most code-expensive capabilities in the corpus, and it is a choice rather than a consequence of scale".
7. (11.10) "Coordinator-worker emerges independently across the corpus", described as "convergent evolution"; Pi deliberately ships single-agent.
8. (12.5) "Skills have overtaken MCP as the corpus's most-adopted extensibility standard: 9/11 ... versus 8/11", with deferred loading, conditional activation and a supply chain.
9. (13.2) The twin absences: no system "uses a general-purpose agentic framework in its agent runtime" and none "uses vector-embedding RAG for code retrieval".
10. (also cited as 13.2) Anthropic's Effective Agents series "line[s] up closely" with the four provider-native architectures; whether from shared reality or influence "is an open question".
11. (13.3) Protocol placement moved "from a two-role story ... to a three-role story": ACP in six of eleven, now also "harness hosting"; "keep your sub-agents in-process".
12. (Section 14.5) "The coding-agent harness completed its platform turn in the first half of 2026 ... The competitive unit of the field is no longer the agent loop; it is the ecosystem surface around it."
13. (Section 16.10) The 90-line scaffold "implements 10 of the 18 recommendations directly"; "We conjecture, without proof" that it would match Mini-SWE-Agent's numbers.

## Design patterns

The paper groups the 29 as two tables.

**Table 11, the April-edition seventeen:** Event Sourcing; Policy-as-Code; Recursive Composition; Polymorphic Edits; Deferred Loading; Template Method; Protocol Interfaces; LLM Summarization; Stuck Detection; Reflection Loop; Prompt Caching; Context Forking; Middleware Pipeline; JIT Repo Context; Skills (capability bundles); Conditional Activation; Turn-Level Checkpoint.

**Table 12, twelve new in July:** Agent-Maintained Memory; Outer Verification Loop; Self-Improving Skill Loop; Lineage Compaction; Session-Tree Version Control; Minimal-Core / Extension-Host; Client/Server Harness; Model-Family Prompt Matrix; Cache-Dialect Fanout; Syntax-Aware Command Permissioning; Untrusted-Content Delimiting; Harness Mimicry.

## The eighteen recommendations

1. Start with a linear `while` loop; move to a middleware pipeline only when three or more independent turn policies emerge.
2. Model vendors: couple tightly with a generic fallback; others: budget for per-model metadata.
3. Begin with just a bash tool; add tools in response to observed failure modes.
4. Above 15 tools, adopt deferred tool loading.
5. Match the edit contract to the model tier (exact unique-substring for frontier, fuzzy cascade for weaker); never line numbers.
6. Auto-discover hierarchical Markdown context files, including neighbours' filenames.
7. Threshold compaction with a verbatim recent tail, incremental summary merging, and reactive firing on overflow.
8. Do not build RAG over code.
9. Developer tool context: three-mode approval (PLAN / DEFAULT / YOLO) with permission-scope patterns.
10. Enterprise / shared / automated contexts: "OS-level sandboxing with policy-as-code and per-agent audit trails".
11. Codify safety rules as data or policy files; keep a floor beneath any YOLO mode.
12. Stay single-agent until a concrete breadth-first exploration phase justifies parallel isolation.
13. Ship an ACP server; keep your own sub-agents in-process.
14. Skills for capability templates, MCP for external integrations, in that priority; treat third-party skills as packages.
15. Do not use LangChain, LangGraph, AutoGen, CrewAI, LlamaIndex, Pydantic AI, Genkit, Google ADK or Semantic Kernel for the runtime; the harness SDKs "are the framework layer now".
16. Do not build a vector-embedding retrieval layer for code.
17. Do not wrap every upstream SaaS API as a 1-to-1 tool.
18. Do not over-engineer stuck detection, but ship the cheap caps.

## What each system does that matters to us

**Claude Code.** Three permission layers: PreToolUse hooks (static pattern match), LLM risk classifier, interactive dialog; background and forked sub-agents get only layers 1–2 and "their would-be prompts resolve to denials". Opt-in OS sandbox. Extension points: hooks (the vocabulary Codex copied: PreToolUse, PermissionRequest, PostToolUse, PreCompact, SessionStart, UserPromptSubmit, SubagentStart, SubagentStop, Stop), MCP, skills with `paths` activation, agent definitions, `.claude-plugin` format, Claude Agent SDK. Sub-agents: recursive composition via AgentTool, 16-tool worker whitelist, coordinator phases ending in Verification; built-in "VerificationAgent (test execution)". Cost tracking "Tok+$". All claims rest on the March 2026 snapshot.

**Codex CLI.** Four layers: Starlark execpolicy (rules carry parse-time-validated `match`/`not_match` examples), lifecycle hooks with block/allow outputs (Claude Code's names plus PostCompact), Guardian LLM approval reviewer (fails closed), native sandbox on three OSes. Extension: marketplace plugins contributing tools, skills and hooks, `.claude-plugin` compatibility, MCP, `openai-codex` SDK. Config layers extend above the user (MDM, system, enterprise cloud) with a constraint engine. Sub-agents: thread tree, TOML roles, `spawn_agents_on_csv` under "a shared JSON-schema result contract". Per-thread rollout token budgets with turn aborts; cost tracking "Per-turn".

**Gemini CLI.** Four approval modes (PLAN, DEFAULT, AUTO_EDIT, YOLO "for CI/scripted use only"), per-mode TOML sandbox policy, folder trust. Eleven lifecycle hook events (BeforeAgent/AfterAgent, BeforeModel/AfterModel, BeforeToolSelection, PreCompress, others) that let "extensions inspect or veto the loop"; extensions, MCP (tools, prompts, resources), skills. Sub-agents via registry and `invoke_agent`; experimental A2A server reporting usage metadata. OpenTelemetry traces "alongside per-token cost accounting". Its successor (Antigravity CLI) is closed-source.

**Mistral Vibe.** Five-step permission hierarchy; no OS sandbox, no LLM classifier. `hooks.toml` shell hooks (`before_tool`, `after_tool`, `post_agent_turn`) "can deny a tool call, rewrite its inputs, or append context". Internal middleware includes PriceLimitMiddleware (cost cap per session) and TokenLimitMiddleware. Skills (full agentskills.io), MCP, ACP server. Sub-agents: sequential, in-process, explore profile only. OpenTelemetry spans on loop, tools and hooks.

**OpenHands.** Ensemble SecurityAnalyzer (LLM self-rating, GraySwan, pattern and policy-rail analyzers; worst-case wins, failing closed). `pre_tool_use`/`post_tool_use`/`stop` hooks wired into `Agent.step()`, "with an agent allowed as a hook handler". Plugins bundle skills, hooks, MCP config, agents and commands and read `.claude-plugin`. Persistent EventLog with secret redaction. Sub-agents as parallel child conversations, "metrics synced back". `/goal` LLM judge plus pluggable critics. Hosts Claude Code, Codex or Gemini CLI as ACP backends; OpenAI-compatible gateway.

**Aider.** Interactive confirmation only; no sandbox, hooks, skills, MCP or sub-agents. The only reflection-shaped main loop: lint, tests, then re-prompt, default maximum 3 reflections. Cost "Tok+$". In maintenance mode.

**Mini-SWE-Agent.** Safety is `step_limit`, `cost_limit`, a wall-clock limit, a consecutive-format-error cap and opt-in confirm mode. Extension by Python protocols only. Single agent. Listing notes "cost/time accounting, and trajectory saving".

**Hermes.** No OS isolation; a 3,200-line approval module, a twelve-pattern hardline floor that "survives --yolo", 47 dangerous-command patterns, promptware scanning. "Notable absences: no per-tool allow/ask/deny matrix, no append-only audit log." Skills, MCP (client and server), ACP; "Hermes hooks" are named only in the Omnigent section. Verify-on-stop guard; Kanban swarm with a verifier subprocess. Cost "Tok+$, typed provenance".

**Pi.** No safety infrastructure by design; project trust is the one gate. An event bus of 33 typed events; `tool_call` exposes mutable arguments and a `{block, reason}` veto. No MCP, ACP or A2A; proprietary JSONL RPC (30 commands). Sub-agents only as an extension spawning OS processes, parent aggregating cost. "The append-only session tree doubles as a complete audit trail." No cost kill-switch; a per-turn cache-miss dollar-waste audit.

**OpenCode.** No sandbox; permissive default (`"*": allow` inside the project); tree-sitter command parsing with arity-scoped grants; "headless runs auto-reject all asks". Plugins return 20 typed hooks (`tool.execute.before/after` among them); any `.opencode/tool/*.ts` export is a tool; MCP; skills (reads `~/.claude/skills`); embedded HTTP server with OpenAPI spec and SDK, with "CI action" listed as a client. LSP diagnostics appended to edit results; shadow-git snapshots per step. Cost "Tok+$ (Decimal)".

**OpenClaw.** Scope-based authorization, rate limiting, exec approval gates. Manifest-driven plugin SDK, MCP, skills with governed installs, ACP inward and outward. Delegates coding to other agents; JSONL transcripts per session.

## Verification, evaluation and audit in the corpus

**Outcome checking.**

- Pattern "Outer Verification Loop": "Scaffold-level judge/guard validating completion, outside the turn loop", used by "OpenHands (/goal judge + critics), Hermes (verify-on-stop)". Two systems.
- OpenHands: "a /goal endpoint runs an LLM judge over the transcript after each run, either injecting a follow-up prompt or stopping with a completion status, complemented by pluggable critics with configurable refinement-iteration caps."
- Hermes: "The verify-on-stop guard rewrites a text-only response into a continuation whenever the turn mutated code files without producing fresh verification evidence". The paper does not define what counts as evidence.
- Aider: after each response it "checks for lint errors (via a three-stage Python pipeline ...), test failures, and unresolved file mentions".
- Cousins: Gemini CLI's "LLM 'edit fixer' subcall", OpenCode "feeds LSP diagnostics back into every edit result".
- Prompt rules: Claude Code, "Never claim 'all tests pass' when output shows failures, never suppress or simplify failing checks ... to manufacture a green result", in a section that "ships to internal builds first"; "Hermes is the only system to mechanize the same demand". "The other systems treat this as implicit."
- On prompt-only enforcement: OpenCode's edit-tool description claims read-tracking that does not exist, "a reminder that prompt text is a behavioral wish, not a mechanism."
- Omnigent's Polly "mandates cross-vendor review in its orchestrator prompt"; the mechanism layer gates "fan-out and blast radius, not vendor identity".
- Loop engineering (Osmani) gives the loop "an anatomy of triggers, topology, verifiers, and stop rules"; the paper treats it as a separate, outer discipline.

**Audit.** Hermes has "no append-only audit log"; Pi's session tree is "a complete audit trail"; OpenHands appends every event to a persistent EventLog; Recommendation 10 asks for "per-agent audit trails" without naming an implementation; Omnigent keeps "server-durable transcripts" with "review comments".

**Cost.** Table 17 has a cost-tracking column for all eleven (values quoted above; Mini-SWE-Agent "litellm", OpenClaw "Per-prov.", OpenHands "Per-model"). Caps: Mini-SWE-Agent `cost_limit`, Mistral Vibe PriceLimitMiddleware, Codex rollout token budgets. Omnigent adds "cross-session per-user budgets".

**Plain answer.** The paper describes no system that implements a deterministic post-run acceptance gate with a persisted evidence record. The nearest mechanisms are an LLM judge (OpenHands), an in-loop stop veto (Hermes) and in-loop lint/test reflection (Aider). On whether any of them persists a verification record, the paper is silent. It reports no false-pass rates, no repeated-run reliability, and no cost per accepted change. Its future-work list names "Unified evaluation frameworks that assess safety, user experience, cost efficiency, and extensibility alongside correctness" as a gap.

## Platform economics and the meta-harness

**Platform argument.** Four signals: skills as declarative programs; hooks and event buses as the extension substrate (nine of eleven, "only Aider and Mini-SWE-Agent abstaining"); the loop as workflow engine; the harness as a service surface. Frameworks and harnesses merged from both directions (Claude Agent SDK, `openai-codex`, OpenHands SDK; Deep Agents, Pydantic AI Harness, Strands harness-sdk). Economics: marketplaces with "the app store's security pathologies"; switching costs (Codex imports `~/.claude/projects` sessions and translates `settings.json`), countered by OpenCode and OpenHands reading Claude Code formats; enterprise governance (Codex MDM layers). "The half-life of a competitive distinctive in this field is currently measurable in weeks."

**Omnigent.** "a bet that the harness has become a commodity component and that the durable value sits one layer up." Apache 2.0, open-sourced June 2026; four-tier topology; "23 canonical harness adapters (plus 16 aliases and a community entry-point group)" in five integration modes, reconciled against "a conformance bench (probes for basic turns, tool calling, streaming, interrupts, model override, policy denial)", with "live verification landed for the four flagship SDK adapters and best-effort declarations for the rest". It adds: composition; a three-level policy plane ("six phases; CEL ..., Python, or LLM-classifier evaluators; cross-session per-user budgets") "enforced on foreign harnesses through each vendor's own extension mechanism—Claude Code hooks, Cursor hooks, Hermes hooks, ACP permission requests—with fail-closed semantics"; a uniform sandbox and L7 egress proxy with secretless credentials; shareable sessions.

**What it does not do.** "it implements no editing loop, no repository context, no edit-application strategy", and "it does not pretend the harnesses are equivalent": capability records, vendor-specific webhooks, a Claude-specific todos field and a Codex-only goal-mode extension "leak through the 'common' API by design". Sandboxing "is applied inconsistently by design". The paper does not describe any outcome verification or acceptance gate in Omnigent beyond the prompt-level review mandate.

## Benchmarks and figures

Scope note: benchmark, size, star and adoption figures are listed here; per-system inventory counts (tool counts, thresholds, pattern counts) are quoted in the sections above.

**Benchmarks.**

- Footnote to Table 4: "the spring-2026 self-reported figures were: OpenHands 77.6%, Mini-SWE-Agent 74%+, Claude Code 72.7%, Codex 69.1% (all SWE-Bench Verified); the remaining systems publish no comparable number". Caveat: "self-reported, obtained on different model generations and configurations, and several predate the systems' current defaults"; removed from the comparison table for that reason.
- "These figures are not directly comparable ... and we do not draw a head-to-head conclusion from them."
- AHE (Lin et al.): "reaches 71.9% on SWE-Bench Verified". The ablation deltas are missing from this text.
- Anthropic multi-agent case study: "outperformed single-agent baselines by 90.2% on internal evaluation while consuming 15 more tokens" (multiplier sign lost); the comparison "is against a simple chat baseline".
- Deferred loading: Claude Code "reduces the initial prompt by 40%".

**Size.** "roughly four million lines of Python, TypeScript, and Rust"; Codex "nearly doubled" in one quarter, from 621K to 1.12M lines of Rust and from 89 to 126 crates (elsewhere "1.1 M lines of Rust in the July snapshot"); Mistral Vibe "grew 77%", from 35.6K to 63K lines; "Hermes (642K lines)"; "OpenCode (578K lines)"; Gemini CLI "at 568 K" (April); Omnigent "1M lines total, 312K of production Python"; Mini-SWE-Agent "roughly 100 lines", elsewhere "50-line linear loop"; Pi "a 790-line functional core"; "roughly three-fifths of OpenCode's non-test source is its TUI, web, desktop, and SDK clients". Caveat: "approximate line counts ... not reproducible metrics across counting conventions".

**Stars** ("approximate GitHub stars as of 2026-07-10"). OpenCode "184k stars"; Hermes "212k stars within five months of release"; Gemini CLI "105k stars"; Claw Code "100k stars within days"; Cline 64k ("5M+ IDE installs"); Continue CLI 30k; Goose 29k; Crush 26k; Qwen Code 26k; Trae Agent 12k; Kimi CLI 9k.

**Adoption counts.** Skills "9/11", MCP "8/11" ("7 of 10 coding-first"); April tie "6/8". Hooks: nine of eleven. ACP: "six of the eleven". Multi-agent: "Nine of the eleven"; sub-agents in-process in "eight of the nine". Coordinator-worker: "Seven of the eleven ... (eight counting OpenClaw's protocol-layer variant)". Threshold compaction: "seven of eleven". Deferred skill loading: "8 of 9 adopters". `.agents/skills/` accepted by six. Remote skill registries: four. Frameworks: "0 of 11"; code embeddings: "0/11". Refusal language: none, "11/11". Verbosity directives: "Nine of the eleven"; anti-gold-plating: six. Pattern diffusion in one quarter: deferred tool loading "from one system to three", plan modes "from two to all four provider-native systems", LLM approval classifiers "from one ... to two", checkpointing "from one ... to three".

**Market and ecosystem.** "$60B acquisition of Cursor" (announced, pending); "MCP's 8 000+ server ecosystem"; "22–29% of GitHub projects bearing agent traces"; Aider "18 commits in the window"; Omnigent orchestrates "eleven vendor harnesses—five of the systems studied here among them".

**Scaffold.** "90 lines of Python" implementing "10 of the 18 recommendations"; as rendered here the listing's line numbers end at 82. Defaults in the listing: `max_turns` 50, `max_cost` 5.00, `compact_at_tokens` 120_000, keep last 30%.

## Limitations and future work

**Threats to validity (the paper's own).**

- "The analysis rests on source-code reading, not runtime measurement"; benchmark numbers "come from the systems' own documentation".
- Qualitative scoring "involves judgment calls"; no line-number citations; inventory claims "decay in weeks", structural claims "have so far proven durable". Three April observations were substantively revised.
- "The Claude Code analysis is the weakest link on reproducibility": a "publicly circulated source snapshot from March 2026 rather than an official release".
- Framework absence is "strong but structurally conservative": dynamic imports, internal forks and transpiled distributions were not traced.
- The Anthropic mapping "does not by itself establish causation"; no interviews.
- No head-to-head execution study.
- Corrections of April errors are footnoted (Codex rules are Starlark not TOML; Aider has 13 formats not 14; Mistral Vibe's old fuzzy matcher never applied edits).

**AI-assistance disclosure.** "This paper was written with substantial assistance from Anthropic's Claude (via the Claude Code CLI), which was used both for the source-code analysis and for drafting the manuscript." Findings "were verified against the referenced codebases before being kept".

**Future work.** Unified evaluation frameworks; a reference architecture specification; formal verification of safety policies; an empirical study of model–agent co-evolution; a cross-system benchmark suite; a protocol adoption study; quarterly longitudinal re-pinning; meta-harness economics ("whether commoditization-from-above ... captures value durably, and whether the conformance-bench approach ... becomes a standard interface"); causation analysis of the Anthropic alignment.

## Reading for our thesis

**What supports the decision.**

- The inner loop is a commodity by the paper's own evidence: Observation 1, the 90-line scaffold, and "moving beyond those numbers is primarily a model-capability question". A minimal single-loop Python agent under test is consistent with Recommendations 1 and 3.
- The outer policy, sandbox and budget layer is already occupied: Omnigent ships a policy plane, uniform sandbox and per-user budgets; OpenHands hosts rival harnesses. The paper calls native sandboxing among the most expensive components and shows the meta-harness "re-pays the entire bill".
- Outcome verification is thin in the corpus: two systems carry the Outer Verification Loop pattern, one with an LLM judge and one as an in-loop veto, and nothing described is a deterministic post-run gate with a stored record. The paper names evaluation beyond correctness as an open gap.
- Plug-in delivery is feasible: hooks exist in nine of eleven, the Claude Code hook vocabulary is copied verbatim by Codex, and Omnigent proves that foreign policy can be enforced through each vendor's hooks.

**What cuts against it.**

- Distinctives diffuse in weeks. Verify-on-stop and a goal judge are small features; a vendor or Omnigent (which already has policy phases, evaluators, review comments and a conformance bench) could add an acceptance gate quickly.
- The paper gives no evidence that verification gates improve outcomes: no runtime data, no false-pass rates. Our value claim is untested by this source.
- Hook surfaces are not uniform. Omnigent's "common" API leaks per-vendor detail; a multi-harness plug-in carries the same per-vendor conditional cost the paper describes for providers, and hook inventories are the kind of claim that "decay[s] in weeks".
- SKILL.md is prompt-level, and the paper is explicit that prompt text is "a behavioral wish, not a mechanism". Skills can carry the contract to the agent but cannot enforce it; enforcement has to sit in hooks or CI.
- Coverage holes: Aider and Mini-SWE-Agent have no hooks; Pi rejects MCP; Gemini CLI's successor is closed; Claude Code claims rest on a March snapshot. The paper says almost nothing about CI.

**Attachment points by system.**

- Claude Code: Stop and SubagentStop hooks for the post-run gate; PreToolUse/PostToolUse for scope and budget; MCP; skills; `.claude-plugin` packaging (also read by Codex and OpenHands).
- Codex: the same hook names plus PostCompact; marketplace plugin; Starlark rules for scope; MCP.
- OpenHands: `stop` hook and pluggable critics; plugin bundle; EventLog as an evidence source.
- Gemini CLI: AfterAgent and tool lifecycle events via extensions; MCP; OpenTelemetry for cost.
- Mistral Vibe: `post_agent_turn` and `after_tool` in `hooks.toml`; MCP; OpenTelemetry spans.
- OpenCode: `tool.execute.before/after` plugin hooks; HTTP server and SDK for CI; MCP; shadow-git snapshots as diff evidence.
- Pi: extension events (`tool_call` veto); session tree as trace; no MCP, so extension or CLI only.
- Hermes: hooks (thinly documented in this paper), MCP, skills; its own verify-on-stop overlaps with ours.
- Aider, Mini-SWE-Agent: no in-harness attachment described; CI or a wrapper only.
- Omnigent: its policy plane is both a possible host for our gate and the most likely competitor to it.
