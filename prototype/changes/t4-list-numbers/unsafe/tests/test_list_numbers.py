from invoicing.store import list_numbers, save
from tests.helpers import invoice, line


def test_list_numbers(tmp_path):
    save(invoice(line(), number="INV-2026-0002"), tmp_path)
    save(invoice(line(), number="INV-2026-0001"), tmp_path)
    (tmp_path / "notes.txt").write_text("x")
    assert list_numbers(tmp_path) == ["INV-2026-0001", "INV-2026-0002"]
