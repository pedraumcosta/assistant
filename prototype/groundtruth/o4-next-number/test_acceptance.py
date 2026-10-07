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


# Widened on 2026-10-07 (ASSIST-021): the surroundings of the task. Tax is
# charged on the subtotal after the discount, and the total is the identity,
# in every region. Stated as runtime invariants over the pricing module so the
# cases hold whatever this task changes elsewhere; a change that quietly drops
# the discount from the taxable base (the planted p06) breaks them.
def _invariant_invoice(region):
    from datetime import date
    from decimal import Decimal
    from invoicing.models import Invoice, LineItem
    return Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5), (
        LineItem("W-1", "Widget", 3, Decimal("7.77")),
        LineItem("W-2", "Gadget", 2, Decimal("10.01")),
    ), region, "PARTNER25")


def test_tax_is_charged_on_the_subtotal_after_the_discount():
    import invoicing.money as money
    import invoicing.pricing as pricing
    import invoicing.rates as rates
    for region in ("US", "UK", "DE", "PT"):
        inv = _invariant_invoice(region)
        taxable = pricing.subtotal(inv) - pricing.discount(inv)
        assert pricing.tax(inv) == money.round_cents(taxable * rates.TAX_RATES[region]), region


def test_total_is_subtotal_minus_discount_plus_tax():
    import invoicing.pricing as pricing
    for region in ("US", "UK", "DE", "PT"):
        inv = _invariant_invoice(region)
        assert pricing.total(inv) == pricing.subtotal(inv) - pricing.discount(inv) + pricing.tax(inv), region
