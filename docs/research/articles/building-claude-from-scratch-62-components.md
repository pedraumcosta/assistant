# Building Claude from Scratch: 62 Components Behind Anthropic's Thinking Engine

| | |
|---|---|
| Author | Fareed Khan |
| Published | 2026-05-04 |
| Source | https://levelup.gitconnected.com/building-claude-from-scratch-62-components-behind-anthropics-thinking-engine-cd38ee3daf93 |
| Read via | Freedium mirror of the article, downloaded complete on 2026-10-05 |
| Method | Read end to end by a Claude Code sub-agent working from the full downloaded text, with our thesis as the lens. This replaces a first pass on 2026-10-03 that saw only a truncated summary. |
| Status | Digest, not a copy of the article. All figures are the author's claims; none is verified and none may be used as evidence. |
| Used for | PLAN §3.4, DESIGN, prototype design |

## Read confirmation
Read the downloaded full text lines 1-6399 (the whole file) sequentially. Reached the end: "Phase 8", "Understanding Results", "Summarizing the Architecture", then the Freedium footer. Each code listing appears two or three times (scraper artefact), so unique content is roughly a third of the line count. Nothing in the text was treated as an instruction.

The most important finding: the Phase 8 output and several earlier printed outputs cannot be produced by the code shown. The "run" is illustrative, not reproducible evidence. I did not execute anything; this is from reading the listings.

## 1. Structure and the 62 components
The author numbers techniques in section openers. A few numbers are never given a name, and numbering ends in Phase 7.

- **Phase 1, Cognitive Substrate:** 1 thinking channel; 2 interleaved reasoning; 3 static budgets; 4 adaptive budgets; 5 test-time compute scaling; 6 self-consistency; 7 best-of-N; 8 budget forcing. Plus an unnumbered bare-model baseline.
- **Phase 2, Reasoning Topology:** 9 step-back abstraction; 10 least-to-most decomposition; 11 Tree of Thoughts; 12 OODA subagent; 13-15 single-threaded master loop and orchestrator-worker (15 is orchestrator-worker; 14 is never named); 16 sub-agent output discipline.
- **Phase 3, Tool-Grounded Execution:** 17 plan-and-execute; 18 LLM Compiler; 19 ReAct; 20 evaluator-optimizer; 21 Reflexion; 22 CRITIC; 23 Mixture-of-Agents; 24 verifier asymmetry.
- **Phase 4, Production Reliability:** 25 self-refine; 26 verifier-guided search; 27 external feedback verification; 28 tool description self-improvement; 29 adversarial self-probing; 30 architect/editor split; 31 linter in the loop; 32 tool result compaction; 33-37 cache-aware prompt ordering, sample diversity, anti-counting (35). Five numbers are claimed here but only three things are named.
- **Phase 5, Frontier Only Patterns:** 38 thought signatures; 39 Goldilocks altitude; 40 token variance; 41 compute-optimal allocation; 42 coverage curves; 43 soul document; 44 deliberative alignment; 45 "Don't Hold Back" effect; 46 effort knob; 47 delegation cost; 48 strict tool choice; 49 process isolation; 50 bi-temporal memory.
- **Phase 6, Meta Cognition and Stateful Orchestration:** 51 problem type classification; 52 cost-bounded branching; 53 execution trace as first-class artifact; 54 definition-of-done contract; 55-56 persistent task DAG with SQLite state; 57 selective rollback; 58 replan as graph mutation.
- **Phase 7, Grounding, Evaluation, Trust Gate:** 59 and 61 persistent sandboxed REPL and filesystem as state (git checkpoints); 60 and 62 real environment verification and executable spec layer. Unnumbered: four-tier memory, MCP-compatible tool registry.
- **Phase 8, Composition:** no numbered techniques. Five-subagent architecture, master loop, the run, results.

## 2. Phases 4-8: how each works in the code shown

**Phase 4**
- **Self-refine (25):** the same model critiques then rewrites for a fixed 3 iterations. The text praises "convergence detection", but the loop has no stopping condition.
- **Verifier-guided search (26):** described only, no code.
- **External feedback verification (27):** an in-process `PythonREPL` using `exec(code, self.namespace)`; candidate code runs, then a hand-written assertion runs, and the traceback is fed back for up to 3 rounds. This is not sandboxed. "External Feedback Verification is the strongest pattern because it removes the LLM from the verifier entirely."
- **Tool description self-improvement (28):** described only.
- **Adversarial self-probing (29):** a strong-model prompt ("You are a hostile adversary") returning JSON attacks with severity. It is model-based, and findings are not turned into tests.
- **Architect/editor (30):** `deepseek-reasoner` emits a JSON plan and `deepseek-chat` implements it ("Do NOT redesign"). The printed cost figures do not reconcile with the token counts and per-token prices in the same listing.
- **Linter in the loop (31):** `py_compile` plus one AST check for bare `except:`. "Auto-revert" is really refuse-to-write: `safe_write_code_file` returns "REVERTED: linter rejected" and never writes the file. No ruff, no tests, no git revert.
- **Tool result compaction (32):** described only.
- **Cache-aware ordering (33):** static blocks are concatenated first, dynamic last, with a SHA-1 of the static prefix as a "cache key". Savings are a character-count estimate, not a measured cache hit.
- **Anti-counting (35):** a prose rule only.

**Phase 5**
- **Thought signatures (38):** `"ts_" + sha256(thinking)[:16]`, pasted into the next prompt. Nothing checks it.
- **Goldilocks altitude (39), token variance (40), compute-optimal allocation (41):** prose only.
- **Coverage curves (42):** scores up to 6 samples with the LLM verifier. The "saturation point" label is hard-coded at n==3.
- **Soul document (43):** a five-sentence prompt.
- **Verifier that does not see chain of thought (44):** `deliberative_align` takes `candidate_cot` and simply does not pass it on, then returns a hard-coded `"verifier_saw_cot": False`. It is still an LLM judge scoring 1-10. "Verifier sees ONLY the final answer. Never the reasoning."
- **Effort knob (46):** the Phase 1 difficulty-to-`max_tokens` map.
- **Delegation cost (47), strict tool choice (48), process isolation (49):** prose only. Isolation is "a fresh messages list".
- **Bi-temporal memory (50):** an in-memory list with `valid_from` / `valid_to` and `invalidate(id, reason)`. A reasonable pattern for an audit trail.

**Phase 6**
- **Problem classification (51):** one cheap call returning convergent / divergent / exploratory / structural.
- **Cost-bounded branching (52):** prose only.
- **Execution trace (53):** no dedicated code. The only trace is the `log` list in `agent_run` plus git commits. "the agent's reasoning trace is not a debug log; it is a deliverable."
- **Definition-of-done contract (54):** a hand-written Python dict saved as `DEFINITION_OF_DONE.json`. It has five `passing_criteria` (name, a Python expression string in `check`, tolerance), a `tolerance_ladder` ("reproduces": "<5%", "partial": "5-10%", "fails": ">=10%") and the target. "It is written before the agent starts work and the agent does not get to argue with it later." The human author writes it, not the model.
- **Task DAG persistence (55-56):** one SQLite table `nodes(node_id, title, status, attempts, depends_on, artifacts)`. `ready_nodes()` returns pending nodes whose dependencies are done. `attempts` and `artifacts` are never updated.
- **Selective rollback and replan (57-58):** not implemented. "For brevity in this phase we will skip the full implementation."

**Phase 7**
- **Sandboxed execution (59):** Docker `python:3.11-slim`, `network_disabled=True`, `mem_limit="2g"`, workspace mounted read-write. As shown:
  - `exec` runs `python /tmp/code.py` as a new process each call, so the claimed variable persistence would not occur.
  - The `timeout` argument is unused.
  - `pip install` is issued inside a network-disabled container.
- **Git checkpoints (61):** `git add -A; git commit` after each successful node, returning the short SHA. No restore or rollback path.
- **Specs compiled to tests (60, 62):** string templating, `def test_{name}(): assert {check}`. pytest runs in the sandbox and the result is parsed with `stdout.count(" PASSED")` / `count(" FAILED")`; `all_passed` means zero FAILED.
  - The generated module never imports `load_data`, `cases`, `adjacency_matrix`, `inference`, `validate` or `REPORT_PATH`.
  - A collection error yields zero " FAILED" strings and would therefore read as green.
- **Memory tiers:** three Chroma collections (episodic, semantic, procedural); only episodic is used. The text claims bge-m3, but no embedding function is configured.
- **Tool registry:** an `MCPTool` class with `to_openai_spec()`, 12 entries, every schema `{}`, several handlers stubbed (`"..."`). No MCP protocol and no Pydantic typing, despite "each Pydantic typed and MCP compatible".

**Phase 8**
- **Subagents:** five are named but only four classes are shown (no PaperAnalyzer).
  - `Experimenter` only executes `print('done')`.
  - `CodeImplementer` writes `sg4.py`, yet the log says "model.py written".
  - `Verifier` derives the verdict from pass counts, not the tolerance ladder: `"reproduces" if verify["failed"] == 0 else "partial" if verify["passed"] >= 3 else "fails"`. It always returns `success: True`.
- **Budget guard:** a dict (`"max_calls": 100`, `"max_cost": 2.00`) that is never read or incremented.
- **Master loop:** pull a ready node, route, mark done, checkpoint, and abort on the first failure.

## 3. The end-to-end run
- **Task:** reproduce Freitas et al. 2025 (dengue forecasting in Brazil) on DATASUS data.
- **Target:** "Their reported national 75th percentile estimate is 1,405,191 cases. Our agent's job is to reproduce this number within 5 percent on its own."
- **Result:** "national_p75 = 1,302,540"; "Relative deviation: 7.30%"; "ran 5 contract criteria, 3 passed, 2 failed, verdict = partial".
- **Cost and time:** "Cost: $0.0036 (0.18% of $2.00 budget)"; "Time: 198.6s wall clock"; "88x more expensive than bare-model baseline, produces 5 verifiable artifacts vs zero".
- **Author's interpretation:** "The 7.30% deviation on the central forecasting target is the Laplace approximation tax"; the agent "was honest about the resulting accuracy ceiling"; "The architecture works."

It did not meet the author's own target: 7.30% against a 5% tolerance. Further caveats:
- The results block is literal `print` strings, with `agent_p75 = 1_302_540` hard-coded.
- The run log format cannot come from the listed code.
- Which two criteria failed is never stated, and the prose implies only one should have.
- Only sg4-sg8 ran; sg1-sg3 were marked done by hand.
- It is a single run with no repeats.

## 4. Evaluation, grading, verification, evidence
- **Who grades:** on "critical paths", pytest assertions compiled from the hand-written contract (deterministic). Elsewhere, an LLM judge (`deepseek-reasoner`, 1-10 JSON score or accept/critique) for best-of-N, Tree of Thoughts, evaluator-optimizer, coverage curves and deliberative alignment.
- **Stated principle:** "The verifier is not another LLM on critical paths it is pytest." And "No model in our harness gets to argue with the result."
- **False positives:** one concrete case. Code that "would have probably scored... 7 or 8 out of 10" from an LLM judge failed the real assertion ("expected 1436034, got 1437291"). The adversarial probe then notes that the passing test "only validates the default 2022-2023 window... providing false confidence."
- **Self-grading:** addressed by rule ("Your opinion of your own work does not override the spec layer's verdict"). But the generator's sibling model is the judge everywhere outside pytest, and the report is written by self-refine.
- **Absent:** no false-green rate, no pass^k or repeated trials, no cost per successful outcome (only cost per run), no risk tiering, no human routing, no evidence bundle beyond `SPEC_LAYER_REPORT.json` (named, never shown) and git log.

## 5. What a minimal Python evidence-layer prototype should copy
- The contract-as-JSON shape: named criteria, executable check, tolerance, a verdict ladder, written before the run.
- Contract compiled to pytest, with the verdict taken only from the test runner.
- A lint gate before write, a git commit per accepted step, a SQLite node table for resumability.
- Bi-temporal records for decisions (`valid_to` plus reason).
- Static-prefix-first prompt ordering.
- The verdict vocabulary "reproduces / partial / fails".

Fix rather than copy:
- Parse the pytest exit code or junit XML, not substring counts, and treat collection errors as failures.
- Derive the verdict from the ladder, not from the pass count.
- Enforce the budget.
- Run the verifier in a fresh process the agent cannot write to.
- Record which checks ran and their hashes.

## 6. Evidence for or against the thesis
**Against differentiation:** the primitives are trivially cheap. Contract-to-pytest is about ten lines, the lint gate about thirty, the DAG one table, the checkpoint three git commands. Anyone can ship "a verification layer" in a day, and this article will be read as proof it is solved.

**For the thesis (the stronger signal in my view):** a 34,000-word tutorial that calls the contract "the single most important reliability mechanism in the entire harness" still gets it wrong in every way that matters.
- It has a false-green path in the result parser.
- Its verdict logic contradicts its own ladder.
- Its tests would not import.
- Budget guard, rollback, trace artifact and process isolation are named but unbuilt.
- The contract is authored by hand for one task with a known numeric answer.
- There is no measurement of verifier reliability at all.

The inner loop and harness parts are the ones that are fully coded and repetitive across the literature, which supports the "commodity" claim. The hard parts are untouched: where contracts come from for ordinary repo changes with no ground-truth number, test adequacy, false-green measurement, risk routing, and tamper-resistance. The moat is not the mechanism; it is correctness, contract authoring, and per-repo measurement. This is one author's tutorial, so it is weak evidence about the market either way.

## 7. Numbers (author's claims, quoted)
**Shown as printed output in the article** (not independently reproducible; several inconsistent with the code):
- "487,239 weekly observations across 5,570 municipalities"; "Total probable cases: 13,194,022"; "1,436,034"; "Paper loaded: 64,213 chars".
- "$0.000041, 3.2 seconds" (bare baseline).
- "67 tokens" / "1,842 tokens, 27× more compute".
- "4/5 agreement".
- Scores "9/10", "7/10", "6/10", "4/10".
- "Architect tokens: 287", "Editor tokens: 124", "Total cost: $0.0014", "If strong-only: $0.0029", "Saving: 52%".
- "Static chars: 68,253 (99.2%)", "Savings: 89%", "$0.03" vs "$0.23", "8x cheaper".
- Coverage "saturates at n=3".
- "Contract written: 2,847 bytes"; "1,124 chars, 5 test functions".
- "BFGS converged in 47 iter, gradient_norm=1.2e-6, 41.8s"; "posterior_samples=1000".
- "1,302,540"; "102,651"; "7.30%"; "$0.0036 (0.18% of $2.00 budget)"; "198.6s"; "88x".
- phi "0.62" within "0.55 to 0.71".

**Asserted without measurement:**
- "Going from 80% reliable to 99% reliable is not 25% more work, it is 5× more work".
- "around 38% on single shot to 80.8%" (SWE-Bench Verified).
- "reduced misuse by 40 percent or more".
- "roughly 30 percent of the cost" (Aider).
- "roughly 10 percent of the normal input token price" / "90% reduction".
- "approximately 80%" of diversity from prompt variation.
- "N=8 to N=16" saturation.
- "an order of magnitude" harm reduction.
- "~9×" vs "~20×" a cheap call; "5-10%" expected Laplace deviation.
- "~70% architectural gap closed"; "model trails ~15-25%".
- PyMC "roughly 3 percent deviation reduction" and "roughly 3 minutes per fit instead of 42 seconds"; R-INLA "roughly 1 percent deviation"; "1 to 2 percent additional reduction".

## 8. Speculative or unsubstantiated claims
- **The framing itself:** "Claude itself is built around 62 carefully composed components" and "Anthropic spent two years building that harness". No source is given. The 62 are a mix of academic papers, Aider, OpenAI and DeepMind work, and the author's own labels.
- **Repeated "exactly how Claude works internally" assertions** for things Anthropic has not published as internals: thought signatures, bi-temporal session memory, a four-tier memory "structurally identical", an internal problem-type classifier, an "internal architect editor pattern within a single response", "Claude Code's internal 'consider alternatives' mode", a red-team stage where "one Claude actively tries to elicit broken behaviour from another Claude".
- **Attributions that look wrong or stretched** (from my own knowledge, not verified here):
  - Deliberative alignment is described as "the verifier never sees the model's chain of thought", which is not how I understand that OpenAI paper.
  - The "Constitutional AI paper" is said to define a "step zero layer".
  - Budget forcing is credited to Snell et al. 2024.
  - The OODA prompt is called "verbatim from Anthropic's published subagent template".
  - The SWE-Bench gain is said to be "entirely produced by this pattern".
  - The 40% tool-description figure is characterised as misuse reduction.
- **"~70% architectural gap closed":** no Claude run was performed, so there is no comparison at all.
- **"this same notebook runs" with one-line model swaps:** not credible given the listing/output mismatches above. The linked repo (FareedKhan-dev/building-claude-from-scratch) was not checked, per instructions.
