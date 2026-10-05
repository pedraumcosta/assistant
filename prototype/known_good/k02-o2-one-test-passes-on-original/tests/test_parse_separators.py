from decimal import Decimal

import pytest

from invoicing.money import parse_amount


def test_thousands_separator():
    assert parse_amount("1,234.50") == Decimal("1234.50")
    assert parse_amount("1,234,567") == Decimal("1234567")


def test_malformed_grouping():
    for text in ("1,23.4", "12,34", ",123"):
        with pytest.raises(ValueError):
            parse_amount(text)
