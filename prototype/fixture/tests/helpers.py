from datetime import date
from decimal import Decimal

from invoicing.models import Invoice, LineItem


def line(quantity=1, unit_price="10.00", sku="W-1", description="Widget"):
    return LineItem(sku, description, quantity, Decimal(unit_price))


def invoice(*lines, region="US", discount_code=None, number="INV-2026-0001"):
    return Invoice(number, "Acme Ltd", date(2026, 10, 5), tuple(lines), region, discount_code)
