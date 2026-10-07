from decimal import Decimal

import pytest

import invoicing.money as money


@pytest.mark.parametrize("text,expected", [
    ("1,234.50", "1234.50"), ("1,234", "1234"), ("12,345.6", "12345.6"),
    ("123,456", "123456"), ("1,234,567.89", "1234567.89"),
    (" 1,000 ", "1000"), ("-1,234.50", "-1234.50"),
])
def test_accepts_well_formed_separators(text, expected):
    assert money.parse_amount(text) == Decimal(expected)


@pytest.mark.parametrize("text", [
    "1,23.4", "12,34", "1,,234", "1,234,56", ",123", "1234,567", "1,2345",
    "1,234.5,6", "1.234,50", "1,", ",",
])
def test_rejects_malformed_separators(text):
    with pytest.raises(ValueError):
        money.parse_amount(text)


@pytest.mark.parametrize("text,expected", [("12.50", "12.50"), (" 3 ", "3"), ("-7.25", "-7.25"), ("0", "0")])
def test_input_without_commas_is_unchanged(text, expected):
    assert money.parse_amount(text) == Decimal(expected)


@pytest.mark.parametrize("text", ["abc", "", "12.3.4"])
def test_still_rejects_what_was_never_an_amount(text):
    with pytest.raises(ValueError):
        money.parse_amount(text)


def test_rounding_is_untouched():
    assert money.round_cents(Decimal("0.125")) == Decimal("0.12")
    assert money.round_cents(Decimal("0.135")) == Decimal("0.14")


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
