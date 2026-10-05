from decimal import Decimal

import pytest

from invoicing.money import parse_amount, round_cents


def test_round_cents():
    assert round_cents(Decimal("1.234")) == Decimal("1.23")
    assert round_cents(Decimal("1.236")) == Decimal("1.24")


def test_parse_amount():
    assert parse_amount("12.50") == Decimal("12.50")
    assert parse_amount(" 3 ") == Decimal("3")


def test_parse_amount_rejects_text():
    with pytest.raises(ValueError):
        parse_amount("abc")
