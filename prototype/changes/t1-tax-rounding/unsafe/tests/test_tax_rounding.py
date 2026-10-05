from decimal import Decimal

from invoicing.pricing import tax
from tests.helpers import invoice, line


def test_tax_rounds_half_up():
    assert tax(invoice(line(1, "1.50"), region="DE")) == Decimal("0.29")
