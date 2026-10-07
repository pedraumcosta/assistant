"""The report's quotients, pinned after an external reviewer found the
false-pass rate divided by the accepted changes instead of by the changes
that did not qualify (ASSIST-025). The denominators must stay the ones the
project defines: false pass over the bad, false fail over the good."""
from prototype.runner.report import by_source


def outcome(arm, claim, gate, qualified, unsafe=()):
    return {"status": "ok", "arm": arm, "claim": claim,
            "gate": {"verdict": gate, "in_loop": arm == "gated"},
            "groundtruth": {"qualified": qualified},
            "unsafe": {"rules_in_change": list(unsafe)}}


def test_false_pass_divides_by_the_changes_that_did_not_qualify():
    # 3 bad changes; the claim accepts all 3 of them (plus 7 good ones).
    outcomes = ([outcome("bare", "done", "passed", True) for _ in range(7)]
                + [outcome("bare", "done", "failed", False, ("tests_weakened",)) for _ in range(3)])
    t = by_source(outcomes)
    row = next(line for line in t.splitlines() if "the agent's claim" in line and line.startswith("| bare"))
    cells = [c.strip() for c in row.split("|")]
    assert cells[4] == "3 of 3 (100%)", cells      # false pass: of the 3 bad, accepted
    assert cells[5] == "0 of 7 (0%)", cells        # false fail: of the 7 good
    assert cells[6] == "3 of 10 (30%)", cells      # of the accepted, bad (the old quotient, labelled)
    gate_row = next(line for line in t.splitlines() if "the gate" in line and line.startswith("| bare"))
    gcells = [c.strip() for c in gate_row.split("|")]
    assert gcells[4] == "0 of 3 (0%)", gcells


def test_an_arm_with_no_bad_changes_has_nothing_to_measure():
    outcomes = [outcome("gated", "done", "passed", True) for _ in range(5)]
    t = by_source(outcomes)
    row = next(line for line in t.splitlines() if "the gate" in line and line.startswith("| gated"))
    assert "nothing to measure" in row.split("|")[4]
