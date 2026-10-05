# Agent Harnesses with Claude — Intuitively and Exhaustively Explained

| | |
|---|---|
| Author | Daniel Warfield |
| Published | 2026-06-26 |
| Source | https://medium.com/intuitively-and-exhaustively-explained/agent-harnesses-with-claude-intuitively-and-exhaustively-explained-1ab5a3697d5f |
| Read via | Freedium mirror of the article, downloaded complete on 2026-10-05 |
| Method | Read end to end by a Claude Code sub-agent working from the full downloaded text, with our thesis as the lens. This replaces a first pass on 2026-10-03 that saw only a truncated summary. |
| Status | Digest, not a copy of the article. All figures are the author's claims; none is verified and none may be used as evidence. |
| Used for | PLAN §3.4, DESIGN, prototype design |

## Read confirmation

I read the downloaded full text lines 1-3364 sequentially and reached the end. The article runs from line 18 to the Conclusion at 3343-3360; 3362-3363 is site footer.

Two limits of the extract:
- Most code blocks appear two or three times, and a few are prefixed by garbled fragments.
- Three demo turns ("apply to something", "yeah add those to the pipeline and apply", "make a resume for all three") appear only in the author's command list. Their transcripts are not in the file, so I could not see the apply step.

## 1. Structure

- **Intro**: a follow-up to an earlier "Agent Harnesses" piece; a soft release of a proposed standard, seeking criticism.
- **What is a Harness?**: surveys conflicting definitions (Google, Anthropic, LangChain, reader comments) and picks one.
- **The Context in Which Harnesses are Being Defined**: "agentic constraint" (ReAct versus graph agents) and Agent Skills.
- **Limits of Constraints and Skills**: graphs are too rigid; skills plus an "LLM Wiki" get disorganised; goals of the spec.
- **Concepts in Agent Harnesses**: the file conventions.
- **Using Agent Harnesses with Claude**: the metaskill bridge.
- **Exploring a Job Application Assistant**: the main demo.
- **A Discussion of Implications**.
- **Creating a Harness**: the `ahar` CLI and a second demo.
- **Conclusion**.

## 2. Definition and context

The author's definition: "A harness is information and tools that allow a general purpose agentic system to do specific, complex tasks in a repeatable and maintainable manner." And: "Practically, that ends up being a directory of resources."

- **Runtime-loop definition rejected**: he says it overlaps with "agent": "it would... lead to confusion by rebranding an already established idea. That's what an agent is."
- **ReAct versus graph agents**: unconstrained agents are flexible but improving them is "whack-a-mole" ("Any time you modify the logic, you modify all steps"). Graph agents are reliable, but "a decent graph can be incredibly difficult to build" and real procedures are "fuzzy".
- **Skills**: "A skill is, in its essence, a folder with a markdown file." Their value: "a shared agreement on structure." His complaint is "Skills must obey a flat structure within .claude, and can't be organized", so they "can't be packaged within a greater context."
- **LLM Wiki (Karpathy)**: works, but "it forgets where it wrote things and creates disorganized, duplicate, and contradictory information", and agents either take "forever" to orient or ignore the docs.
- **CLAUDE.md**: never discussed; it appears only in Claude Code's banner tip. HARNESS.md is "essentially a README.md file designed for agents".
- **MCP**: an inspiration, and bundled as a config file (Playwright) inside the harness.
- **Plugins**: "the closest similar construct", criticised as global-only.

## 3. The proposed standard

- **`HARNESS.md`** at the root. Required frontmatter is `name` and `description`, plus a body. Example: `name: job-application-harness`. The body can steer the agent, for example: "On initial load, run `summarize.py`... Reserve `disclose.py` for when you need to read specific skill or reference content".
- **Top-level subdirectories** are arbitrary domain buckets (`tools/`, `data/`, `outputs/`; `skills/`, `references/`).
- **Routing files** are named after the top-level directory in capitals and repeated in each nested subdirectory (`TOOLS.md` in `tools/`, `tools/database/`, and so on). Required frontmatter is `description`; the body lists children, such as "- **database/** — Tools for interacting with the database".
- **Result**: "a fuzzy tree-like structure, where HARNESS.md is the root node". Files are natural text and "can reference anything, not only their children".
- **Leaves** are ordinary skills (`SKILL.md`, `scripts/`, `references/`) or reference files. A `description` on every markdown file is recommended, "but it's not a strong requirement".
- **Scope terminators**: "a terminator document, .harnessleaf, and terminator patterns (like skill.md) to know when a folder should not be explored further." No file contents are shown for `.harnessleaf`.
- **Metaskill** (`.claude/skills/agent-harnesses/`, repo agentharnesses/metaskill) is a bridge because "Claude has no knowledge of the standard". Its scripts:
  - `summarize.py`: "Briefly summarizes the project structure". Output is a tree with tags and truncated descriptions (`├── [harness] HARNESS.md — Assists a job seeker...`).
  - `disclose.py`: traversal "via progressive disclosure"; returns JSON with `"status": "exploring"` and a `"session"` id.
  - `map_references.py`: "produces a structural overview of the harness". Never run in the demos.
  - `reverse_disclose.py`: "allows the agent to see routing documents before a given file"; returns `"status": "complete", "target": ...`.
- **Exploration sessions**: "a directory for exploration sessions, which allows an agent to keep track of how it's explored a harness". No further detail.
- **Mentioned only**: "configurable leaves", promised for a later article.

## 4. Demos

**Demo 1: job-application harness** (Claude Code, Sonnet 4.6).

- **Load**: the first load ran `summarize.py` and then a long `disclose.py` session. After the HARNESS.md hint, a fresh session loaded with the summary alone.
- **Setup**: the agent read `setup.md`, created `leads.csv` and `target-roles.md`, and copied his resume in as the template. It flagged that the template lacked the cover-letter paragraph IDs the tailor skill expects. That was never fixed, and no cover letter was produced.
- **"Find five jobs"**: parallel web searches guided by `currently-working-sources.md`.
- **"I'm moving to California"**: edited two files and missed `recommended-apply/SKILL.md`. A second prompt was needed. Author: "This isn't foolproof, admittedly".
  - The edits also corrupted content. "~87% signal rate (14/16 active, 2 expired)" became "87% rate over 68 leads". The historical note "1 non-Austin" became "1 non-California". Example outputs were relabelled "(California)". The author does not remark on any of this.
- **Removing `resumes/`**: the agent used `reverse_disclose.py` only because he said "Follow harness maintinance". It found two routing files, and a later grep (not the script) found a stale README reference. Author: Claude "may not think to invoke reverse disclosure on its own".
- **Resume generation**: a scratch script failed twice on `python` versus `python3`, then built three .docx files. A skill script verified the page counts ("All three are exactly 2 pages").
- **Result**: "they're not perfect. It moved some of my experience over to California".
- **Inconsistencies**:
  - His summary says it "downloaded the job descriptions of those listings", but `leads.csv` shows description files for only three of the five.
  - The SEON row still reads "Austin Hybrid".

**Demo 2, the final one: `ahar init` and an IAEE article index.**

- `ahar init` with the `claude` preset scaffolds `HARNESS.md`, `README.md`, `.gitignore`, `.claude/settings.json`, `skills/SKILLS.md` and `references/REFERENCES.md`. A `modify-harness` maintenance skill also appears in the tree.
- `ahar validate .` passed. `ahar show` printed the tree with `[root]`, `[routing]` and `[leaf]` tags.
- He then asked Claude to index all his Substack articles by topic.
- Re-validation gave five warnings ("markdown file should have a 'description' in frontmatter") but still "✓ . is valid".
- `ahar show` was unchanged: "It actually didn't change the overall structure of the harness at all, just its contents."
- A new session loaded and reported "73 articles across 13 topic areas".
- Asked for the largest topic, it read all 13 files and answered Agentic AI at 10. The table is unsorted. By my addition its rows sum to 72, not 73; the author does not check.

## 5. Implications and Creating a Harness

Implications:
- **Central claim**: "The agent harnesses standard, paired with the metaskill, allows claude to leverage that structure consistently and repeatedly."
- **Project scope**: "plugins... can only be installed at a global level". Because a harness is a directory you `cd` into, "you can have many, many harnesses on a single machine... with little risk of cross-contamination."
- **Admission**: "this is a fairly simple demo, and it is... job application isn't exactly rocket surgery."
- **Open questions**: multi-harness and nesting are unresolved: "I'm still thinking about what these questions mean practically". The standard "makes no constraints around how harnesses interact".

Creating a Harness:
- "two pip-installable repos": `agentharnesses-cli` (the `ahar` command) and `harnesses-ref`, which lets a user "evaluate if a harness obeys the agent harnesses standard".
- Commands: `ahar init`, `ahar validate .`, `ahar show [-v 1]`.
- Both are "early constructs".

## 6. Maintenance, correctness and evidence

Mechanisms offered:
- The routing structure itself.
- `reverse_disclose.py` to find the routing documents that point at a target.
- A `modify-harness` skill.
- `ahar validate`.
- Reliance on "Claud's implicit abilities to maintain complex code bases".

What is missing:
- Validation is structural only (file presence and frontmatter). Nothing checks content truth, contradictions, staleness or broken path references.
- In the demos, consistency was reached by repeated human prompts and ad-hoc grep.
- There is no evaluation of whether the harness improves agent results: no baseline without a harness, no comparison against a plain LLM Wiki or CLAUDE.md, no repeated runs, no token or cost figures.
- The only measurements are Claude Code's per-turn timers.
- The subtitle's "faster, less expensive, more maintainable, and more consistent" is not measured.
- A quoted commenter states the gap: "the hard part is not structure, it's evals, failure handling, and keeping behavior stable".

## 7. For us

**(a) Packaging: yes, with one caveat.** It is just a directory containing a `.claude/` folder with skills and settings, so hooks and MCP config can ride along. The caveat is that the standard has no adoption beyond the author's metaskill bridge, so treat it as a layout convention on top of SKILL.md rather than a distribution channel. A possible layout:

```
evidence-layer/
├── HARNESS.md                  (name, description; "run summarize first")
├── .claude/                    (settings.json hooks, skills/agent-harnesses)
├── contracts/CONTRACTS.md      (schema, per-change contracts)
├── checks/CHECKS.md            (verify-scope/, verify-acceptance/, verify-budget/ — each a SKILL.md + scripts/)
├── evidence/EVIDENCE.md        (bundle format, emit-bundle/)
├── routing/ROUTING.md          (risk rules, reviewers)
└── repo/REPO.md                (per-repo knowledge, ownership, known quirks; .harnessleaf on bulky dirs)
```

**(b) Complementary; it does not reduce the need for post-hoc verification.** The harness is advisory context that the agent may ignore or apply partially. The demo shows that:
- propagation was incomplete;
- facts were silently corrupted during a self-edit;
- the declared "Clean" preceded finding another stale reference;
- the author accepted outputs by eye.

The one robust step was a deterministic script (the page-count check), which is our thesis in miniature. Harness content is also a new unverified artefact that itself needs checks.

**(c) What a minimal prototype should copy:**
- A `summarize.py`-style one-shot tree with one-line descriptions, for cheap orientation.
- A reverse-reference map (`reverse_disclose.py` or `map_references.py`) as a blast-radius input. Extend it beyond routing files to all path mentions, since the demo's misses were found by grep.
- A structural linter in CI like `ahar validate`, plus dead-path and contradiction checks.
- Frontmatter `description` on every file.
- `.harnessleaf`-style scope limits.
- Embedding the invocation rule in a hook rather than hoping the agent remembers.

## 8. Numbers (author's or transcript's, quoted)

Article metadata:
- "June 26, 2026"; "53 min read"; "Contents 11"; "A few weeks ago I released a piece"

Framing:
- "two fundamental ideas"
- "messes up on step 7... steps 1–6"

Demo 1:
- "Claude Code v2.1.191"; "Sonnet 4.6"
- "… +80 lines"; "… +25 lines"; "… +31 lines"
- "Claude formed a high-level understanding of the repo in 14 seconds" ("Cogitated for 14s")
- "notes from 68 leads collected as of 2026-06-24"
- "Crunched for 9s"; "Cooked for 13s"; "Brewed for 1m 5s"
- "Wrote 55 lines to references/target-roles.md"; "… +43 lines"
- "paragraph IDs (00000004–0000000C)"
- "Find five jobs"; "Did 1 search in 8s" / "10s"
- "$200k-$275k"
- "Two search waves (16 candidates total) had ~87% signal rate (14/16 active, 2 expired)", rewritten as "(87% rate over 68 leads)"
- "4 leads collected; 2 expired before application, 1 non-Austin, 1 applied (Palantir)"
- "Baked for 38s"; "Baked for 1m 54s"
- "30 characters or fewer"; "3-column layout"; "a third page"
- "(15 XML files), simplified 0 tracked changes, merged 0 runs"
- "Wrote 134 lines"
- "All three are exactly 2 pages"
- "Cooked for 8s"; "Crunched for 3m 21s"
- "over the course of a few minutes"; "it makes me three resumes"

Demo 2:
- "two pip-installable repos"
- "Claude Code v2.1.193"
- "-v... defaults to 0"; "ahar show -v 1"
- "in a few seconds"; "Baked for 19s"; "… +31 lines"; "… +83 lines"
- "73 articles across 13 topic areas"; "Read 13 files"
- "Agentic AI is the topic with the most articles at 10"
- Table values: 10, 6, 7, 6, 6, 6, 6, 4, 4, 5, 4, 5, 3
- "Brewed for 14s"; "Sautéed for 17s"

## 9. Speculative, promotional or unsupported

- The subtitle's benefit claims and "consistently and repeatedly" rest on single runs, one user and one model.
- "misalignments between different documents are easily resolved" is contradicted by the demo's multi-prompt clean-up.
- Calling it a "standard" is aspirational: there is one author, it is self-described as "soft-release", and "The concrete is not yet dry". He hopes for native adoption by "popular agentic systems".
- "works perfectly at the scale we need" is an anonymous commenter's remark about an LLM Wiki.
- The Alexa "rainforest noises skill" anecdote is offered as evidence that "The biggest productionalized AI systems are using skills".
- The "plugins... can only be installed at a global level" claim is asserted, not demonstrated.
- Configurable leaves, native clients and multi-harness composition are promised, not shown.
- It closes with requests for GitHub stars, maintainers and paid subscriptions.
- The `.harnessleaf`, exploration-session and `map_references.py` mechanics are described but never shown working.
