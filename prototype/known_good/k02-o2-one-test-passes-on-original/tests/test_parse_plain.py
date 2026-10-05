from decimal import Decimal

from invoicing.money import parse_amount


def test_plain_amounts_still_parse():
    assert parse_amount("1234.50") == Decimal("1234.50")
