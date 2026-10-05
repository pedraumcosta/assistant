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
