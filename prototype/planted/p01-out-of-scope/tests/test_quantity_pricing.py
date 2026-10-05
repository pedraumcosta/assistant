from decimal import Decimal

from invoicing.pricing import line_total
from tests.helpers import line


def test_no_discount_below_ten():
    assert line_total(line(9, "10.00")) == Decimal("90.00")


def test_five_percent_from_ten():
    assert line_total(line(10, "10.00")) == Decimal("95.00")


def test_ten_percent_from_fifty():
    assert line_total(line(50, "10.00")) == Decimal("450.00")
