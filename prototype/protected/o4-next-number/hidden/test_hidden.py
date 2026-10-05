"""Hidden checks for the contract. One or more per requirement in the task."""
import invoicing.numbering as numbering


def test_r1_after_the_highest_sequence_used():
    assert numbering.next_number(["INV-2026-0001", "INV-2026-0007"], 2026) == "INV-2026-0008"


def test_r2_other_years_are_ignored():
    assert numbering.next_number(["INV-2025-0412", "INV-2026-0003"], 2026) == "INV-2026-0004"
    assert numbering.next_number(["INV-2025-0412"], 2026) == "INV-2026-0001"


def test_r3_invalid_entries_are_ignored():
    assert numbering.next_number(["DRAFT", "INV-2026-0002"], 2026) == "INV-2026-0003"


def test_r4_padded_to_four_digits():
    assert numbering.next_number([], 2026) == "INV-2026-0001"
