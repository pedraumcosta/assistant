from decimal import Decimal

import pytest

import invoicing.pricing as pricing
from invoicing.models import LineItem


def lt(quantity, unit_price):
    return pricing.line_total(LineItem("W-1", "Widget", quantity, Decimal(unit_price)))


@pytest.mark.parametrize("quantity,expected", [
    (1, "10.00"), (9, "90.00"),            # below the first tier
    (10, "95.00"), (11, "104.50"), (49, "465.50"),   # 5%
    (50, "450.00"), (51, "459.00"), (200, "1800.00"),  # 10%
])
def test_tiers_and_their_boundaries(quantity, expected):
    assert lt(quantity, "10.00") == Decimal(expected)


def test_discount_is_applied_to_the_line_total_then_rounded():
    # 10 x 1.33 = 13.30; less 5% = 12.635; half-even to 12.64.
    # Discounting the unit price first would give 12.60.
    assert lt(10, "1.33") == Decimal("12.64")


def test_rounding_stays_half_even():
    assert lt(10, "0.05") == Decimal("0.48")   # 0.475
    assert lt(10, "0.09") == Decimal("0.86")   # 0.855
    assert lt(10, "0.03") == Decimal("0.28")   # 0.285; half-up would give 0.29


def test_subtotal_uses_discounted_lines():
    from datetime import date
    from invoicing.models import Invoice
    inv = Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5), (
        LineItem("W-1", "Widget", 10, Decimal("10.00")),
        LineItem("W-2", "Gadget", 1, Decimal("5.00")),
    ))
    assert pricing.subtotal(inv) == Decimal("100.00")
