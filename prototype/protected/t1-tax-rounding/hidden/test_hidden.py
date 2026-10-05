"""Hidden checks for the contract. One or more per requirement in the task."""
from datetime import date
from decimal import Decimal

import invoicing.pricing as pricing
from invoicing.models import Invoice, LineItem


def tax(price, region):
    return pricing.tax(Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                               (LineItem("W-1", "Widget", 1, Decimal(price)),), region))


def test_r1_the_reported_case():
    assert tax("1.50", "DE") == Decimal("0.29")


def test_r1_ordinary_tax_is_unchanged():
    assert tax("100.00", "UK") == Decimal("20.00")
