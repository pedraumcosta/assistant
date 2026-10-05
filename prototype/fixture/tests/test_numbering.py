from invoicing.numbering import next_number


def test_first_number():
    assert next_number([], 2026) == "INV-2026-0001"


def test_next_number():
    assert next_number(["INV-2026-0001", "INV-2026-0002"], 2026) == "INV-2026-0003"
