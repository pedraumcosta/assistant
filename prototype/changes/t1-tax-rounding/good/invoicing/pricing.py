"""Line totals, subtotal, discount, tax and total."""
from decimal import Decimal, ROUND_HALF_UP

from invoicing.models import Invoice, LineItem
from invoicing.money import CENT, round_cents
from invoicing.rates import DISCOUNT_CODES, TAX_RATES


def line_total(line: LineItem) -> Decimal:
    return round_cents(line.unit_price * line.quantity)


def subtotal(invoice: Invoice) -> Decimal:
    return sum((line_total(line) for line in invoice.lines), Decimal("0.00"))


def discount(invoice: Invoice) -> Decimal:
    """The amount taken off the subtotal by the invoice's discount code."""
    if invoice.discount_code is None:
        return Decimal("0.00")
    if invoice.discount_code not in DISCOUNT_CODES:
        raise ValueError(f"unknown discount code: {invoice.discount_code!r}")
    return round_cents(subtotal(invoice) * DISCOUNT_CODES[invoice.discount_code])


def tax(invoice: Invoice) -> Decimal:
    """Tax is charged on the subtotal after the discount."""
    taxable = subtotal(invoice) - discount(invoice)
    return (taxable * TAX_RATES[invoice.region]).quantize(CENT, rounding=ROUND_HALF_UP)


def total(invoice: Invoice) -> Decimal:
    return subtotal(invoice) - discount(invoice) + tax(invoice)
