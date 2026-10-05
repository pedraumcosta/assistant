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
