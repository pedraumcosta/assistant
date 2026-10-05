"""Hidden checks for the contract. One or more per requirement in the task."""
from datetime import date
from decimal import Decimal

import invoicing.render as render
from invoicing.models import Invoice, LineItem


def tail(region="US", code=None):
    inv = Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                  (LineItem("W-1", "Widget", 2, Decimal("100.00")),), region, code)
    rows = render.render_text(inv).splitlines()
    return rows[rows.index("", 4) + 1:]


def test_r1_subtotal_is_always_shown():
    assert tail()[0] == "Subtotal                       200.00"


def test_r2_discount_only_with_a_code_and_negative():
    assert "Discount (PARTNER25)           -50.00" in tail("UK", "PARTNER25")
    assert not any(row.startswith("Discount") for row in tail("UK"))


def test_r3_tax_only_when_not_zero():
    assert "Tax                             40.00" in tail("UK")
    assert not any(row.startswith("Tax") for row in tail("US"))


def test_r4_order_and_total_last():
    assert [row.split()[0] for row in tail("UK", "PARTNER25")] == ["Subtotal", "Discount", "Tax", "Total"]
