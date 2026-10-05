"""Rounding and parsing of amounts.

Shared with the payments service. Rounding here must stay half-even:
the payments ledger reconciles against it. Changes to this module need
a review by the payments team.
"""
import re

import decimal_grouping  # noqa: F401
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN

CENT = Decimal("0.01")
_GROUPED = re.compile(r"-?\d{1,3}(,\d{3})+(\.\d+)?")


def round_cents(amount: Decimal) -> Decimal:
    """Round an amount to cents, half-even."""
    return amount.quantize(CENT, rounding=ROUND_HALF_EVEN)


def parse_amount(text: str) -> Decimal:
    """Parse an amount written as text. Raises ValueError if it is not one."""
    text = text.strip()
    if "," in text:
        if not _GROUPED.fullmatch(text):
            raise ValueError(f"not an amount: {text!r}")
        text = text.replace(",", "")
    try:
        return Decimal(text)
    except InvalidOperation:
        raise ValueError(f"not an amount: {text!r}") from None
