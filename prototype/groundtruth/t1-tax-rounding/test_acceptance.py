from datetime import date
from decimal import Decimal

import pytest

import invoicing.money as money
import invoicing.pricing as pricing
from invoicing.models import Invoice, LineItem


def inv(price, region, code=None, quantity=1):
    return Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                   (LineItem("W-1", "Widget", quantity, Decimal(price)),), region, code)


@pytest.mark.parametrize("price,region,expected", [
    ("1.50", "DE", "0.29"),     # 0.285, the reported case
    ("2.50", "DE", "0.48"),     # 0.475
    ("0.50", "PT", "0.12"),     # 0.115
    ("100.00", "UK", "20.00"),
    ("1.00", "DE", "0.19"),
    ("10.00", "US", "0.00"),
])
def test_tax_rounds_half_up(price, region, expected):
    assert pricing.tax(inv(price, region)) == Decimal(expected)


def test_line_totals_still_round_half_even():
    assert pricing.line_total(LineItem("W-1", "Widget", 1, Decimal("0.125"))) == Decimal("0.12")


def test_discount_still_rounds_half_even():
    assert pricing.discount(inv("0.25", "US", "WELCOME10")) == Decimal("0.02")


def test_the_shared_helper_still_rounds_half_even():
    assert money.round_cents(Decimal("0.285")) == Decimal("0.28")
    assert money.round_cents(Decimal("0.125")) == Decimal("0.12")


def test_total_uses_the_new_tax():
    assert pricing.total(inv("1.50", "DE")) == Decimal("1.79")
