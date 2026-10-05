"""Line totals, subtotal, discount, tax and total."""
from decimal import Decimal

from invoicing.models import Invoice, LineItem
from invoicing.money import round_cents
from invoicing.rates import DISCOUNT_CODES, TAX_RATES


# tiers: 10 or more units, 50 or more units
def _quantity_discount(quantity: int) -> Decimal:
    if quantity >= 50:
        return Decimal("0.10")
    if quantity >= 10:
        return Decimal("0.05")
    return Decimal("0")


def line_total(line: LineItem) -> Decimal:
    gross = line.unit_price * line.quantity
    return round_cents(gross * (1 - _quantity_discount(line.quantity)))


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
    return round_cents(taxable * TAX_RATES[invoice.region])


def total(invoice: Invoice) -> Decimal:
    return subtotal(invoice) - discount(invoice) + tax(invoice)
