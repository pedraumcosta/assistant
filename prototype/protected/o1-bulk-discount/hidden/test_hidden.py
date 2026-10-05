"""Hidden checks for the contract. One or more per requirement in the task."""
from decimal import Decimal

import invoicing.pricing as pricing
from invoicing.models import LineItem


def lt(quantity, unit_price="10.00"):
    return pricing.line_total(LineItem("W-1", "Widget", quantity, Decimal(unit_price)))


def test_r1_ten_or_more_units_get_five_percent():
    assert lt(10) == Decimal("95.00")
    assert lt(20) == Decimal("190.00")


def test_r2_fifty_or_more_units_get_ten_percent():
    assert lt(50) == Decimal("450.00")
    assert lt(100) == Decimal("900.00")


def test_r3_fewer_than_ten_units_get_nothing():
    assert lt(9) == Decimal("90.00")


def test_r4_result_is_rounded_to_cents():
    assert lt(10, "0.33") == Decimal("3.14")    # 3.30 less 5% = 3.135
