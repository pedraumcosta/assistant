from decimal import Decimal

from invoicing.money import parse_amount


def test_grouped_token():
    token = "1,234,567.89"
    assert parse_amount(token) == Decimal("1234567.89")
