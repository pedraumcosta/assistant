"""Hidden checks for the contract. One or more per requirement in the task."""
from datetime import date

import invoicing.terms as terms


def test_r1_saturday_moves_to_monday():
    assert terms.due_date(date(2026, 9, 3)) == date(2026, 10, 5)


def test_r1_sunday_moves_to_monday():
    assert terms.due_date(date(2026, 9, 4)) == date(2026, 10, 5)


def test_r2_a_weekday_is_unchanged():
    assert terms.due_date(date(2026, 1, 5)) == date(2026, 2, 4)
