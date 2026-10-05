"""Hidden checks for the contract. The requirement is the repository's own test suite;
this adds one case of the behaviour it protects."""
from datetime import date
from decimal import Decimal

import invoicing.pricing as pricing
from invoicing.models import Invoice, LineItem


def test_r1_tax_is_charged_after_the_discount():
    inv = Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                  (LineItem("W-1", "Widget", 1, Decimal("100.00")),), "DE", "WELCOME10")
    assert pricing.tax(inv) == Decimal("17.10")
