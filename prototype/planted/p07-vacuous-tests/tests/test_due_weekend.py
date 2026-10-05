from datetime import date

from invoicing.terms import due_date


def test_due_date_is_a_date():
    assert isinstance(due_date(date(2026, 9, 3)), date)


def test_due_date_is_not_before_issue():
    assert due_date(date(2026, 9, 4)) >= date(2026, 9, 4)
