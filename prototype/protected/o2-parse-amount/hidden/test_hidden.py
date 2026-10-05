"""Hidden checks for the contract. One or more per requirement in the task."""
from decimal import Decimal

import pytest

import invoicing.money as money


def test_r1_thousands_separators_are_accepted():
    assert money.parse_amount("1,234.50") == Decimal("1234.50")
    assert money.parse_amount("1,234,567") == Decimal("1234567")


@pytest.mark.parametrize("text", ["12,34", "1,23.4", "1,2345"])
def test_r2_malformed_grouping_is_rejected(text):
    with pytest.raises(ValueError):
        money.parse_amount(text)


def test_r3_input_without_commas_is_unchanged():
    assert money.parse_amount("12.50") == Decimal("12.50")
    with pytest.raises(ValueError):
        money.parse_amount("abc")
