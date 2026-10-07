from decimal import Decimal

import invoicing.pricing as pricing
from invoicing.models import LineItem


def li(sku, quantity, price="10.00", description=None):
    return LineItem(sku, description or sku, quantity, Decimal(price))


def test_same_sku_and_price_are_combined():
    assert pricing.merge_lines((li("A", 2), li("A", 3))) == (li("A", 5),)


def test_returns_a_tuple():
    assert isinstance(pricing.merge_lines([li("A", 1)]), tuple)
    assert pricing.merge_lines(()) == ()


def test_accepts_a_list():
    assert pricing.merge_lines([li("A", 2), li("A", 3)]) == (li("A", 5),)


def test_different_price_stays_separate():
    merged = pricing.merge_lines((li("A", 2, "10.00"), li("A", 3, "9.00"), li("A", 1, "10.00")))
    assert merged == (li("A", 3, "10.00"), li("A", 3, "9.00"))


def test_order_of_first_appearance():
    merged = pricing.merge_lines((li("C", 1), li("A", 1), li("C", 2), li("B", 1), li("A", 4)))
    assert [(m.sku, m.quantity) for m in merged] == [("C", 3), ("A", 5), ("B", 1)]


def test_first_description_is_kept():
    merged = pricing.merge_lines((li("A", 1, description="Widget"), li("A", 1, description="Widget (blue)")))
    assert merged == (LineItem("A", "Widget", 2, Decimal("10.00")),)


def test_equal_prices_written_differently_are_the_same_price():
    assert len(pricing.merge_lines((li("A", 1, "10.0"), li("A", 1, "10.00")))) == 1


def test_input_is_not_changed():
    lines = [li("A", 2), li("A", 3)]
    pricing.merge_lines(lines)
    assert lines == [li("A", 2), li("A", 3)]


def test_existing_pricing_is_unchanged():
    assert pricing.line_total(li("A", 2, "9.99")) == Decimal("19.98")


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
