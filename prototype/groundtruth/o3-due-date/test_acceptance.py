from datetime import date

import pytest

import invoicing.terms as terms


def test_the_cases_are_what_they_claim_to_be():
    assert date(2026, 10, 3).weekday() == 5 and date(2026, 10, 4).weekday() == 6


@pytest.mark.parametrize("issued,days,expected", [
    (date(2026, 9, 3), 30, date(2026, 10, 5)),    # lands on Saturday 3 Oct
    (date(2026, 9, 4), 30, date(2026, 10, 5)),    # lands on Sunday 4 Oct
    (date(2026, 10, 3), 0, date(2026, 10, 5)),    # no terms, issued on a Saturday
    (date(2026, 10, 4), 0, date(2026, 10, 5)),    # no terms, issued on a Sunday
    (date(2026, 12, 3), 30, date(2027, 1, 4)),    # Saturday 2 Jan, across the year end
    (date(2026, 9, 27), 7, date(2026, 10, 5)),    # Sunday, custom terms
])
def test_weekend_moves_to_monday(issued, days, expected):
    assert terms.due_date(issued, days) == expected
    assert expected.weekday() == 0


@pytest.mark.parametrize("issued,days,expected", [
    (date(2026, 1, 5), 30, date(2026, 2, 4)),
    (date(2026, 9, 2), 30, date(2026, 10, 2)),    # Friday stays Friday
    (date(2026, 9, 5), 30, date(2026, 10, 5)),    # Monday stays Monday
    (date(2026, 1, 5), 14, date(2026, 1, 19)),
])
def test_weekdays_are_unchanged(issued, days, expected):
    assert terms.due_date(issued, days) == expected


def test_default_terms_are_thirty_days():
    assert terms.due_date(date(2026, 9, 3)) == date(2026, 10, 5)


# Widened on 2026-10-07 (ASSIST-021): the surroundings of the task. Tax is
# charged on the subtotal after the discount, and the total is the identity,
# in every region. Stated as runtime invariants over the pricing module so the
# cases hold whatever this task changes elsewhere; a change that quietly drops
# the discount from the taxable base (the planted p06) breaks them.
def _invariant_invoice(region):
    from datetime import date
    from decimal import Decimal
    from invoicing.models import Invoice, LineItem
    return Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5), (
        LineItem("W-1", "Widget", 3, Decimal("7.77")),
        LineItem("W-2", "Gadget", 2, Decimal("10.01")),
    ), region, "PARTNER25")


def test_tax_is_charged_on_the_subtotal_after_the_discount():
    import invoicing.money as money
    import invoicing.pricing as pricing
    import invoicing.rates as rates
    for region in ("US", "UK", "DE", "PT"):
        inv = _invariant_invoice(region)
        taxable = pricing.subtotal(inv) - pricing.discount(inv)
        assert pricing.tax(inv) == money.round_cents(taxable * rates.TAX_RATES[region]), region


def test_total_is_subtotal_minus_discount_plus_tax():
    import invoicing.pricing as pricing
    for region in ("US", "UK", "DE", "PT"):
        inv = _invariant_invoice(region)
        assert pricing.total(inv) == pricing.subtotal(inv) - pricing.discount(inv) + pricing.tax(inv), region
