import invoicing.numbering as numbering

nn = lambda existing, year=2026: numbering.next_number(existing, year)


def test_empty():
    assert nn([]) == "INV-2026-0001"


def test_follows_the_highest_not_the_count():
    assert nn(["INV-2026-0001", "INV-2026-0007"]) == "INV-2026-0008"


def test_order_of_the_list_does_not_matter():
    assert nn(["INV-2026-0009", "INV-2026-0002", "INV-2026-0004"]) == "INV-2026-0010"


def test_other_years_are_ignored():
    assert nn(["INV-2025-0412", "INV-2026-0003", "INV-2027-0900"]) == "INV-2026-0004"


def test_only_other_years():
    assert nn(["INV-2025-0412", "INV-2025-0413"]) == "INV-2026-0001"


def test_invalid_entries_are_ignored():
    assert nn(["DRAFT", "", "INV-2026-0002", "INV-2026-ABCD", "INV-2026", "CN-2026-0050"]) == "INV-2026-0003"


def test_only_invalid_entries():
    assert nn(["DRAFT", "INV-26-1"]) == "INV-2026-0001"


def test_past_four_digits():
    assert nn(["INV-2026-9999"]) == "INV-2026-10000"
    assert nn(["INV-2026-10000"]) == "INV-2026-10001"


def test_a_number_embedded_in_other_text_is_not_an_invoice_number():
    assert nn(["xINV-2026-0500", "INV-2026-0500x", "INV-2026-0002"]) == "INV-2026-0003"


def test_the_list_is_not_changed():
    existing = ["INV-2026-0003", "INV-2026-0001"]
    nn(existing)
    assert existing == ["INV-2026-0003", "INV-2026-0001"]


def test_format_number_is_unchanged():
    assert numbering.format_number(2026, 7) == "INV-2026-0007"
