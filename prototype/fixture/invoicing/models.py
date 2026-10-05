"""The invoice and its lines."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class LineItem:
    sku: str
    description: str
    quantity: int
    unit_price: Decimal


@dataclass(frozen=True)
class Invoice:
    number: str
    customer: str
    issued: date
    lines: tuple[LineItem, ...]
    region: str = "US"
    discount_code: str | None = None
