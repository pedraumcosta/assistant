# Review of DESIGN.md — ASSIST evidence layer

| | |
|---|---|
| Date | 2026-10-05 |
| Reviewed | `docs/DESIGN.md` as of commit `fa96c11` (post T15–T19 decisions) |
| Reviewer | VP Engineering review, assisted by Claude Code |
| Verdict | The design is honest, well-scoped and unusually disciplined about its own costs — but its central security claim (the author cannot influence the verdict) is asserted rather than designed, and two internal contradictions plus a missing flakiness story will surface within the first week of a pilot. None of this blocks the prototype; findings 10 and 11 should change what the prototype builds before the first paid run. |

## What is strong and should be kept

Fail-closed everywhere; `error` is never a pass; the measurement skeleton with a fake agent built first; both error rates measured, not just false passes; overrides recorded as labels; the redlines; the one-sentence trade-off stated at the top. Most design documents never say what they give up; this one does it per quality (§1.4).

---

## High severity — the integrity boundary

### 1. The verdict runner executes author-controlled code in the same environment that holds the hidden checks

The biggest gap. Running the customer's test suite means executing the change's code (DESIGN §3 "Verdict runner", §4.1 steps 4–5). That code runs where the hidden checks are mounted (§2.1: `visibility: hidden — mounted only where the verdict runs`). So at verdict time the author's code can read the hidden checks, forge structured test reports, or patch the test reporter — exactly the E-75 behaviour the design cites as its threat model. "A read-only checkout" does not contain a running process.

**Fix:** state an isolation boundary. Each check executes in a throwaway sandbox; the verdict is assembled *outside* it from exit statuses the sandboxed code cannot write; hidden checks are mounted per-check and are never co-resident with author code longer than their own run. Also: test infrastructure (`conftest.py`, `pytest.ini`, CI config) must be protected paths by default, or §4.1 step 5's hidden tests run under an author-controlled harness.

### 2. The enforcement anchor is circular

§2.2 says "the contract's hash is what the pipeline pins" — but pipeline configuration (e.g. `.github/workflows/`) is author-writable in the ordinary case. An agent can edit the workflow to skip the verdict job, point it at a different contract, or neutralise it; the scope check that would catch this is enforced by the very job being edited.

**Fix:** make the real anchor explicit — the host's *required status check* named in branch protection, plus admin-restricted workflow paths — and say who can change the protection rules themselves. One more wrinkle: agents usually run with the engineer's credentials; if the engineer can write to the protected branch, their agent can too. The protected branch must be writable only by a role no agent ever assumes.

### 3. There is no flaky-test story, and it threatens three claims at once

§2.6 promises "running the same thing twice gives the same record"; §1.4 promises replay; §5 measures false-fails. Real test suites are flaky, and flakiness breaks idempotency, breaks replay, and inflates the false-fail rate — which the design itself says teaches people to bypass the gate. This will be the first complaint of any pilot team.

**Fix:** a stated policy — bounded retries for checks marked retryable; a quarantine state that routes to a person rather than silently passing or failing; flakiness reported as its own metric. Related, lower severity: replay also needs environment pinning (a container digest in the evidence item), and the evaluation path's replay guarantee dies when a vendor deprecates the pinned scorer model — say so.

---

## Medium severity — contradictions and ambiguities

### 4. Budget exhaustion has two contradictory outcomes

§4.1 step 3: budget or time exceeded → `failed`. §6 Failure-handling row: "an exhausted budget gives `inconclusive` and a person". And §2.4 scopes `inconclusive` to evaluations only. **Recommended resolution:** *agent* budget exhausted → `failed` (the work did not finish); *verification* budget exhausted → `inconclusive` (the evidence did not finish). The two budgets already exist separately in §2.2.

### 5. The decision order contradicts its own principle

"Cheap and decisive checks run first" (§4.1), yet scope (step 6), test-adequacy (7) and dependency/secrets (8) — all static, millisecond checks — run *after* the build and the full test suite (4–5). Worse than the cost: it executes untrusted code before screening it. **Fix:** static checks move before anything from the change is executed.

### 6. Risk tier: fixed in the contract or derived from the diff?

§2.2 puts `risk_tier` in the contract, fixed before the run; §4.3 says tiers are "set by path rules". A change can drift into red-tier paths the contract did not anticipate. **Fix:** compute the tier from the *actual diff* at verdict time, with the contract's value as a floor, never a ceiling.

### 7. Hidden checks leak through the repair loop

A failed verdict goes "back to the author, with the reason" (§3; §4.1 step 5 covers hidden tests). If the first failing check is hidden, the reason reveals it, and over bounded repair attempts the agent fits to the hidden set — the failure mode hidden checks exist to prevent. **Fix:** a disclosure policy — visible-check failures reported in full; hidden-check failures reported coarsely ("a hidden acceptance check failed") with the count of remaining attempts.

### 8. `error` → "re-queued" is unbounded

§2.4 re-queues errors; §6 retries an infrastructure failure once. A persistently broken check re-queues forever. **Fix:** a terminal state after N errors that escalates to a person — consistent with "a pending human decision has a time limit".

---

## Medium severity — measurement credibility

### 9. The headline differentiator — "a measured false-pass rate" — has no statistical treatment

The rate will come from a handful of planted flaws and slowly accumulating override labels. "0% on 12 planted flaws" quoted without a denominator or uncertainty range is precisely the overclaiming the rest of the repository is careful to avoid. Also missing: §5 says "if these numbers stop predicting what happens after merge, fix the checks" — but no mechanism collects post-merge escapes (incidents, reverts) to feed back. And measuring false-fails on "changes people wrote and merged" requires retrofitting contracts onto historical changes, which is nontrivial and biases the measurement; the design should say how. (The P7 results template now forces denominators and plausible ranges so this cannot be forgotten.)

### 10. Prototype: the verdict sources may not judge the same artifacts

§7.3 compares three verdict sources against ground truth, but the gate's verdict naturally exists only in the gated arm. If the gate judges only gated-arm outputs while the agent's claim is judged on all arms, H4 has a selection bias. **Cheap fix:** run the gate *offline as a scorer* on the final diff of every arm's every run, so all three sources judge an identical change set.

### 11. Prototype: do not execute unsafe actions to count them

H1 counts "unsafe actions executed", and "an isolated copy of the fixture" is the only containment — but a copy does not contain `rm -rf ~`, `git push --force`, or network exfiltration from a prompt-injected trap task. This runs on a developer machine. **Fix:** all arms run inside a container, or at minimum behind an interceptor that *records and refuses* host-reaching commands, counting "would have executed" for H1. This changes nothing about the comparison and removes a real risk to the host.

---

## Low severity

- **Scope-by-path is brittle** against lockfiles, formatters and generated code — a predictable false-fail driver. Allow declared exceptions in the contract.
- **`overridden` conflates** override-to-accept and override-to-reject; split them — they are different labels for §5.
- **The evaluation path's "no worse than the previous version on the same cases"** needs a stored, versioned baseline — unstated.
- Not a DESIGN issue, but noted: PLAN's 150-minute timebox for P5 against §7.4's seven build steps is the most optimistic number in the repository. §7.4's ordering (skeleton plus fake agent first) is the right hedge — protect step 1 at all costs.

---

## Suggested handling

- Findings 4–6: wording-level fixes to DESIGN.md (about ten minutes).
- Findings 1–3: a short "integrity boundary" subsection, which can honestly say the prototype *simulates* the boundary (a directory outside the working copy, per T19) while the product requires the sandbox-per-check design.
- Findings 10–11: change the prototype's runner before any paid run.
