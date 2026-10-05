"""Payment terms."""
from datetime import date, timedelta

SATURDAY = 5


def due_date(issued: date, terms_days: int = 30) -> date:
    """The date payment is due. Never a weekend: it moves to the Monday after."""
    due = issued + timedelta(days=terms_days)
    while due.weekday() >= SATURDAY:
        due += timedelta(days=1)
    return due
