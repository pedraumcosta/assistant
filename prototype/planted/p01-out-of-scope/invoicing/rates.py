"""Tax rates by region and discount codes. Owned by finance."""
from decimal import Decimal

TAX_RATES = {
    "US": Decimal("0.00"),
    "UK": Decimal("0.20"),
    "DE": Decimal("0.19"),
    "PT": Decimal("0.23"),
}

DISCOUNT_CODES = {
    "WELCOME10": Decimal("0.10"),
    "PARTNER25": Decimal("0.25"),
    "BULK5": Decimal("0.05"),
}
