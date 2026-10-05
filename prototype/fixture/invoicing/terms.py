"""Payment terms."""
from datetime import date, timedelta


def due_date(issued: date, terms_days: int = 30) -> date:
    """The date payment is due."""
    return issued + timedelta(days=terms_days)
