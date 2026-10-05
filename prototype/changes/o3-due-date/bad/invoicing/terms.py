"""Payment terms."""
from datetime import date, timedelta


def due_date(issued: date, terms_days: int = 30) -> date:
    """The date payment is due."""
    due = issued + timedelta(days=terms_days)
    if due.weekday() >= 5:
        due += timedelta(days=2)
    return due
