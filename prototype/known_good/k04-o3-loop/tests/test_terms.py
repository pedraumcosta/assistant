from datetime import date

from invoicing.terms import due_date


def test_due_date_default_terms():
    assert due_date(date(2026, 1, 5)) == date(2026, 2, 4)


def test_due_date_custom_terms():
    assert due_date(date(2026, 1, 5), terms_days=14) == date(2026, 1, 19)


def test_weekend_due_dates_move_to_monday():
    assert due_date(date(2026, 9, 3)) == date(2026, 10, 5)
    assert due_date(date(2026, 9, 4)) == date(2026, 10, 5)
