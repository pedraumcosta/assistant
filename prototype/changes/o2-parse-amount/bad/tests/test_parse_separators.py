from decimal import Decimal

from invoicing.money import parse_amount


def test_thousands_separator():
    assert parse_amount("1,234.50") == Decimal("1234.50")
    assert parse_amount("1,234,567") == Decimal("1234567")
