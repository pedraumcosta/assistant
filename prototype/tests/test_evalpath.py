"""The evaluation path's scoring and its three-way decision, held without a
model: the parts that must not drift are the code scorer and the interval
rule, and both are pure."""
from prototype.runner.evalpath import decide, score, wilson

INVOICE = {"number": "INV-2026-0107", "customer": "Acme Ltd", "total": "1,250.00",
           "currency": "EUR", "due_date": "2026-09-30", "days_overdue": 7}

GOOD = ("Dear Acme Ltd, this is a reminder that invoice INV-2026-0107 for EUR 1,250.00 "
        "was due on 2026-09-30. Could you confirm a payment date for this invoice?")


def test_a_draft_meeting_every_requirement_passes():
    s = score(GOOD, INVOICE)
    assert s["passed"] and all(s["checks"].values())


def test_each_requirement_fails_alone():
    assert not score(GOOD.replace("INV-2026-0107", "the invoice"), INVOICE)["checks"]["R1"]
    assert not score(GOOD.replace("EUR ", ""), INVOICE)["checks"]["R2"]
    assert not score(GOOD + " Your payment plan is guaranteed.", INVOICE)["checks"]["R3"]
    assert not score(GOOD + " padding" * 60, INVOICE)["checks"]["R4"]
    assert not score(GOOD.replace("?", "."), INVOICE)["checks"]["R5"]


def test_an_approval_claim_is_caught_in_its_usual_wordings():
    for phrase in ("your invoice has been approved", "approved for processing",
                   "approval was granted", "payment is guaranteed"):
        assert not score(GOOD + " " + phrase.capitalize() + ".", INVOICE)["checks"]["R3"], phrase


def test_a_customer_named_approved_does_not_trip_the_claim_rule():
    # Hidden case h1 holds this line: naming the customer is required,
    # claiming approval is forbidden, and the two must not be confused.
    inv = {**INVOICE, "customer": "Approved Partners Ltd"}
    draft = GOOD.replace("Acme Ltd", "Approved Partners Ltd")
    assert score(draft, inv)["checks"]["R3"]


def test_r5_accepts_equivalent_payment_date_questions():
    # The scorer-v1 lesson: these are the phrasings real drafts used.
    for q in ("Could you confirm the date on which you will make the payment?",
              "Could you confirm when you will pay?",
              "Can you confirm your payment date?"):
        draft = GOOD.replace("Could you confirm a payment date for this invoice?", q)
        assert score(draft, INVOICE)["checks"]["R5"], q
    assert not score(GOOD.replace("?", "."), INVOICE)["checks"]["R5"]


def test_the_decision_needs_the_whole_interval_to_clear_the_mark():
    # 40 of 40 clears 0.90; 36 of 40 (rate .90, interval straddling) does not
    # decide; 20 of 40 is failed outright.
    assert decide(40, 40, 0.90) == "passed"
    assert decide(36, 40, 0.90) == "inconclusive"
    assert decide(20, 40, 0.90) == "failed"


def test_no_samples_decide_nothing():
    low, high = wilson(0, 0)
    assert (low, high) == (0.0, 1.0)
    assert decide(0, 0, 0.90) == "inconclusive"
