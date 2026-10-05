from invoicing.numbering import next_number


def test_gap():
    assert next_number(["INV-2026-0001", "INV-2026-0007"], 2026) == "INV-2026-0008"


def test_other_years_ignored():
    assert next_number(["INV-2025-0412", "INV-2026-0003"], 2026) == "INV-2026-0004"


def test_invalid_entries_ignored():
    assert next_number(["DRAFT", "INV-2026-0002"], 2026) == "INV-2026-0003"
