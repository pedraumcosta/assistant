from decimal import Decimal

import pytest

from invoicing.pricing import discount, line_total, subtotal, tax, total
from tests.helpers import invoice, line


def test_line_total():
    assert line_total(line(2, "9.99")) == Decimal("19.98")


def test_subtotal():
    assert subtotal(invoice(line(2, "9.99"), line(1, "5.00"))) == Decimal("24.98")


def test_discount():
    assert discount(invoice(line(1, "100.00"), discount_code="WELCOME10")) == Decimal("10.00")


def test_no_discount():
    assert discount(invoice(line(1, "100.00"))) == Decimal("0.00")


def test_unknown_discount_code():
    with pytest.raises(ValueError):
        discount(invoice(line(1, "100.00"), discount_code="NOPE"))


def test_tax():
    assert tax(invoice(line(1, "100.00"), region="UK")) == Decimal("20.00")


def test_tax_applies_after_discount():
    inv = invoice(line(1, "200.00"), region="UK", discount_code="PARTNER25")
    assert tax(inv) == Decimal("40.00")


def test_total_with_discount_and_tax():
    inv = invoice(line(1, "200.00"), region="UK", discount_code="PARTNER25")
    assert total(inv) == Decimal("190.00")
