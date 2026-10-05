# Legacy System Modernization with Coding Agents: A Case Study

| | |
|---|---|
| Reference | arXiv 2608.28972, Alves, Politowski and Montandon, August 2026 |
| Source | https://arxiv.org/abs/2608.28972 |
| Read on | 2026-10-05, from the arXiv HTML full text |
| Method | Read end to end by a Claude Code sub-agent and checked against Pedro's notes. |
| Status | Digest with quotations. One system, twelve features, assessed by hand by its maintainer. The paper is internally inconsistent on some figures; the record lists them. |
| Used for | PLAN §3.11 |

## Read record

- "Legacy System Modernization with Coding Agents: A Case Study", arXiv:2608.28972v1, 29 Aug 2026, https://arxiv.org/abs/2608.28972
- Authors: Iago da Silva Rodrigues Alves, Cristiano Politowski, João Eduardo Montandon. Affiliations listed: Group Software (Belo Horizonte); Ontario Tech University; Universidade Federal de Minas Gerais (UFMG). The first author is "the software engineer responsible for the maintenance of the legacy system".
- Lines read: 1–1580 of 1580. End reached: conclusion, acknowledgments, 35 references, then page chrome.

## What was studied

- System: one corporate ERP for shopping-mall management in Visual Basic 6, "in production for over two decades". Two secondary modules: Measurements ("around 299K LOC") and Purchases ("around 224K LOC").
- Task: migrate 12 features (six per module) to C# .NET 10, keeping the same database "to avoid further issues related to data migration".
- Features: six low, four medium, two high complexity, classed by LOC, methods and class dependencies; 35,970 LOC in total.
- Agent: "Claude Code (version 2.1.96)" on "the Opus 4.6 1M model". No other model or harness.
- Runs: 12 sessions, one per feature, "single-pass generation strategy ... without human intervention or additional refinement after completion".
- Human-prepared inputs per feature: three CLAUDE.md files (goal, functional scope, methodology and conventions; a description of the legacy source; target-architecture conventions), read-only VB6 sources, a C# project template, "a single, standardized prompt".
- Success measure: share of a pre-catalogued list of legacy "instructions" (160 business rules, 171 database operations, 331 in total) reproduced equivalently; plus time, tokens and cost.

## Findings

1. "the agent scored 70% equivalence across the 331 instructions evaluated."
2. By complexity (Table 5): Low 100% persistence, 83% functional, 92% total; Medium 77%, 85%, 81%; High 51%, 42%, 47%; Total 71%, 69%, 70%.
3. At high complexity, "35 out of 71 operations being incorrectly migrated" and "only 25 out of the 59 rules" migrated; "complete persistence modules are left without implementation, such as the entire reading-approval workflow ... absent altogether, rather than implemented incorrectly."
4. Structure beats size: "fragmented code across multiple files—even when the files are completely provided—appears to be a key determinant of the agent's performance". F9 (926 LOC) reached 67% functional equivalence; F10 (4,158 LOC) reached 92%.
5. Explicit over implicit: the agent "ignored implicit instructions, those hidden in optional query parameters, dynamic configuration values, or form-level conditions".
6. Cost: "59 minutes and 45.8 million tokens ... at a total cost of $50.29", "i.e., $0.15 per instruction". "Input tokens dominate the consumption (99.6% of the total), as the agent rereads the legacy code at each reasoning cycle".

## How verification was done, and what it reveals

**No automated test suite was used.** Equivalence was judged by hand by the first author, who also maintains the system and ran the sessions.

- Before the runs he "performed a manual inspection over the legacy source code of each feature"; "we cataloged each rule and database operation before the migration sessions and defined equivalence criteria upfront."
- Persistence Parity: "we executed the migrated and original features under the same usage scenario, and monitored the resulting state on the system database", comparing records field by field.
- Functional Parity: "we analyzed the execution flows of the migrated and original features for each business rule". Table 3 lists its source as "Source Code": code reading, not execution.
- Second rater: "a mid-level software engineer who did not participate in the migration sessions—independently evaluated the same 160 business rules": "110 out of 160 rules classified as equivalent, i.e., 69%"; "both reviewers agreed on 149 out of the 160 rules (93%)"; Cohen's Kappa "0.84". Database operations were not double-rated.
- The 11 disagreements "concentrate on partially migrated rules, where the agent produced the rule but did not wire it into the execution flow, or preserved its intent while narrowing its criteria".

**What failures looked like** (Table 6; 100 of 331 instructions):

| Issue | # |
|---|---|
| Missing Adjacent Modules | 42 |
| Missing DB Operation | 22 |
| Missing Rule | 20 |
| Missing Module Integration | 10 |
| Bad Implementation | 6 |

Failures are overwhelmingly omissions, not wrong code. Adjacent modules ("batch data-import procedures, report generation, email notifications") were dropped "even when they are provided as context to the agent".

- F5: a missing existence check, so "the migrated version duplicated the records instead of updating them."
- F12: the migrated routine "inserts the request and its items, always in the Open state, and never sends the notification. The request is therefore created regardless of this authority approval."

**Human effort.** No hours or cost are given for human work. The tasks described are: selecting features, writing three CLAUDE.md files per feature, preparing the target template, supervising, cataloguing 331 instructions, running both systems and comparing database state, classifying 100 failures, and a second review of 160 rules. The $50.29 covers model usage only.

The paper does not report whether the migrated code compiled, built or passed any tests.

## Check of Pedro's notes

- One system, 12 features by complexity — Confirmed; two modules of one ERP.
- "equivalence-tested" — Corrected. Assessment was manual: "the first author manually inspected the generated artifacts ... He also executed both versions of the system, and compared the database state produced by each one." No test suite is described.
- "70% average behavioural equivalence — 92% on low-complexity features, 47% on high" — Confirmed as figures. The 70% is a share of 331 instructions (persistence and functional combined), not a per-feature mean; medium is 81%.
- "about 6×", "1.47M tokens / $1.66 → 9.09M / $10.28 per feature" — Confirmed for the abstract and introduction ("Low-level features consumed 1.47M tokens on average ($1.66), whereas high-level ones consumed 9.09M tokens on average ($10.28); 6x more"). Corrected for the body: Table 7, the results and the conclusion give "$10.23", with the multiple "6.2x" for cost and tokens. The paper is inconsistent. These are per-feature averages within a level.

## Figures

- Per-feature totals (Table 4): F2 100%; F3 93%; F7 91%; F8 91%; F11 90%; F1 87%; F4 87%; F9 82%; F10 74%; F5 69%; F6 50%; F12 44%.
- Table 4's "Total Average" row reads 84%, 76%, 80%, against Table 5's 71%, 69%, 70%; unexplained.
- Cost by level: $1.66, $4.97 ("2.9x"), $10.23 ("6.2x"); "$4.19 per migration".
- Inconsistencies in the source: F5 "26 out of 65 instructions" against 29 in Table 1; F12 "34 out of 71" against 72 in Table 1; one sentence names "F4 with 94%, F6 with 92% and F7 with 95%" where Table 4 gives F4, F10 and F11.
- Conversion: tables are flattened one cell per line but readable. Figures 1, 3, 4 and 7 are captions only; the prompt text (Figure 3) is absent.

## Relevance to the two theses

**(a) Thesis B.** The paper cannot separate a capability limit from a preparation gap. Against "more context fixes it": omissions occurred "even when the files are completely provided", with a 1M-token window and per-feature CLAUDE.md files. For a specialised layer: the failure pattern is specific and predictable (rules in form events, global configuration, adjacent modules), and the authors' proposed remedies are human-supplied structure: restrictions stated "as clear and explicit as possible", "upfront decomposition of high-complexity features", human-in-the-loop iteration. All are untested future work. Even the low-complexity result depended on a maintainer writing scope and conventions per feature. Characterization tests, zoning and durable memos do not appear.

**(b) Thesis A.** The paper does not compare a behaviour-only check with anything, so it does not show such checks passing bad changes. It does show a single-pass agent stopping with 100 of 331 catalogued instructions not migrated, mostly by silent omission; the only instrument that found this was a catalogue written before the run and checked by a human. That catalogue, with criteria "defined upfront", resembles a change contract with acceptance checks. The verdict was not deterministic: raters disagreed on 11 of 160 rules, on code that exists but is not wired in. The duplicate-record and bypassed-approval cases are the kind a recorded database-state check could catch mechanically; the paper did not automate this.

**(c) First market.** Supportive. The model run cost $50.29 and under an hour; everything that established what was delivered was maintainer labour, unpriced. That favours brownfield as a first market for a verification layer over a separate assistant. No evidence is offered that a legacy-specialised harness improves outcomes.

## Cautions

- Stated limits: "two modules of a single VB6 ERP ... with a single agent (Claude Code 2.1.96) running a single model (Opus 4.6 1M)"; "having only two high-complexity features limits the robustness of our conclusions"; results "should not be extrapolated to iterative approaches, which tend to produce higher equivalence".
- One run per feature; no variance.
- The same person selected features, wrote instructions, built the catalogue and scored the output.
