"""Hidden checks for the contract. One or more per requirement in the task."""
from datetime import date
from decimal import Decimal

import invoicing.store as store
from invoicing.models import Invoice, LineItem


def save(number, directory):
    store.save(Invoice(number, "Acme Ltd", date(2026, 10, 5), (LineItem("W-1", "Widget", 1, Decimal("1.00")),)), directory)


def test_r1_sorted_list_of_numbers(tmp_path):
    save("INV-2026-0002", tmp_path)
    save("INV-2026-0001", tmp_path)
    assert store.list_numbers(tmp_path) == ["INV-2026-0001", "INV-2026-0002"]


def test_r2_other_files_are_ignored(tmp_path):
    save("INV-2026-0001", tmp_path)
    (tmp_path / "notes.txt").write_text("x")
    assert store.list_numbers(tmp_path) == ["INV-2026-0001"]
