from decimal import Decimal

import pytest

import invoicing.money as money


@pytest.mark.parametrize("text,expected", [
    ("1,234.50", "1234.50"), ("1,234", "1234"), ("12,345.6", "12345.6"),
    ("123,456", "123456"), ("1,234,567.89", "1234567.89"),
    (" 1,000 ", "1000"), ("-1,234.50", "-1234.50"),
])
def test_accepts_well_formed_separators(text, expected):
    assert money.parse_amount(text) == Decimal(expected)


@pytest.mark.parametrize("text", [
    "1,23.4", "12,34", "1,,234", "1,234,56", ",123", "1234,567", "1,2345",
    "1,234.5,6", "1.234,50", "1,", ",",
])
def test_rejects_malformed_separators(text):
    with pytest.raises(ValueError):
        money.parse_amount(text)


@pytest.mark.parametrize("text,expected", [("12.50", "12.50"), (" 3 ", "3"), ("-7.25", "-7.25"), ("0", "0")])
def test_input_without_commas_is_unchanged(text, expected):
    assert money.parse_amount(text) == Decimal(expected)


@pytest.mark.parametrize("text", ["abc", "", "12.3.4"])
def test_still_rejects_what_was_never_an_amount(text):
    with pytest.raises(ValueError):
        money.parse_amount(text)


def test_rounding_is_untouched():
    assert money.round_cents(Decimal("0.125")) == Decimal("0.12")
    assert money.round_cents(Decimal("0.135")) == Decimal("0.14")
