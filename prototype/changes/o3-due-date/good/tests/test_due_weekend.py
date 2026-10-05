from datetime import date

from invoicing.terms import due_date


def test_saturday_moves_to_monday():
    assert due_date(date(2026, 9, 3)) == date(2026, 10, 5)


def test_sunday_moves_to_monday():
    assert due_date(date(2026, 9, 4)) == date(2026, 10, 5)
