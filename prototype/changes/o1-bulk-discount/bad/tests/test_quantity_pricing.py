from decimal import Decimal

from invoicing.pricing import line_total
from tests.helpers import line


def test_five_percent():
    assert line_total(line(20, "10.00")) == Decimal("190.00")


def test_ten_percent():
    assert line_total(line(100, "10.00")) == Decimal("900.00")
