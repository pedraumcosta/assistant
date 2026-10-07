from datetime import date
from decimal import Decimal

import invoicing.render as render
from invoicing.models import Invoice, LineItem

HEAD = "Invoice INV-2026-0001\nCustomer: Acme Ltd\nIssued: 2026-10-05\n\n"


def inv(region="US", code=None, price="100.00"):
    return Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5),
                   (LineItem("W-1", "Widget", 2, Decimal(price)),), region, code)


def test_plain_invoice_shows_subtotal_and_total_only():
    assert render.render_text(inv()) == HEAD + (
        "  2 x Widget                   200.00\n"
        "\n"
        "Subtotal                       200.00\n"
        "Total                          200.00\n"
    )


def test_discount_and_tax():
    assert render.render_text(inv("UK", "PARTNER25")) == HEAD + (
        "  2 x Widget                   200.00\n"
        "\n"
        "Subtotal                       200.00\n"
        "Discount (PARTNER25)           -50.00\n"
        "Tax                             30.00\n"
        "Total                          180.00\n"
    )


def test_tax_without_discount():
    assert render.render_text(inv("DE")) == HEAD + (
        "  2 x Widget                   200.00\n"
        "\n"
        "Subtotal                       200.00\n"
        "Tax                             38.00\n"
        "Total                          238.00\n"
    )


def test_discount_without_tax():
    assert render.render_text(inv("US", "WELCOME10")) == HEAD + (
        "  2 x Widget                   200.00\n"
        "\n"
        "Subtotal                       200.00\n"
        "Discount (WELCOME10)           -20.00\n"
        "Total                          180.00\n"
    )


def test_no_tax_line_when_a_taxed_region_yields_zero_tax():
    text = render.render_text(inv("UK", price="0.01"))   # 0.02 at 20% rounds to 0.00
    assert "Tax" not in text
    assert text.endswith("Subtotal                         0.02\nTotal                            0.02\n")


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
