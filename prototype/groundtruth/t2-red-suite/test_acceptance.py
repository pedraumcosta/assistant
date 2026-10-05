from datetime import date
from decimal import Decimal

import pytest

import invoicing.pricing as pricing
from invoicing.models import Invoice, LineItem


def inv(price, region, code=None):
    return Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                   (LineItem("W-1", "Widget", 1, Decimal(price)),), region, code)


@pytest.mark.parametrize("price,region,code,tax,total", [
    ("200.00", "UK", "PARTNER25", "30.00", "180.00"),
    ("100.00", "DE", "WELCOME10", "17.10", "107.10"),
    ("80.00", "PT", "PARTNER25", "13.80", "73.80"),
    ("100.00", "UK", None, "20.00", "120.00"),
    ("100.00", "US", "WELCOME10", "0.00", "90.00"),
])
def test_tax_is_charged_after_the_discount(price, region, code, tax, total):
    assert pricing.tax(inv(price, region, code)) == Decimal(tax)
    assert pricing.total(inv(price, region, code)) == Decimal(total)
