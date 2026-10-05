"""Hidden checks for the contract. One or more per requirement in the task."""
from decimal import Decimal

import invoicing.pricing as pricing
from invoicing.models import LineItem


def li(sku, quantity, price="10.00", description="Widget"):
    return LineItem(sku, description, quantity, Decimal(price))


def test_r1_same_sku_and_price_are_combined():
    assert pricing.merge_lines((li("A", 2), li("A", 3))) == (li("A", 5),)


def test_r2_first_description_is_kept():
    merged = pricing.merge_lines((li("A", 1, description="Widget"), li("A", 1, description="Other")))
    assert merged[0].description == "Widget"


def test_r3_order_of_first_appearance():
    merged = pricing.merge_lines((li("B", 1), li("A", 1), li("B", 1)))
    assert [m.sku for m in merged] == ["B", "A"]


def test_r4_different_price_stays_separate():
    assert len(pricing.merge_lines((li("A", 1, "10.00"), li("A", 1, "9.00")))) == 2
