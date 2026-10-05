from invoicing.numbering import next_number


def test_gaps_years_and_junk():
    assert next_number(["INV-2026-0001", "INV-2026-0007"], 2026) == "INV-2026-0008"
    assert next_number(["INV-2025-0412", "junk", "INV-2026-0003"], 2026) == "INV-2026-0004"
