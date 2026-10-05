from decimal import Decimal

from invoicing.pricing import tax
from tests.helpers import invoice, line


def test_tax_base_excludes_the_discount():
    assert tax(invoice(line(1, "100.00"), region="DE", discount_code="WELCOME10")) == Decimal("17.10")
