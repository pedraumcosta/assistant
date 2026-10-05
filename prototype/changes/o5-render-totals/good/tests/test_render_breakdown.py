from invoicing.render import render_text
from tests.helpers import invoice, line


def test_breakdown_with_discount_and_tax():
    text = render_text(invoice(line(1, "200.00"), region="UK", discount_code="PARTNER25"))
    assert text.endswith(
        "Subtotal                       200.00\n"
        "Discount (PARTNER25)           -50.00\n"
        "Tax                             30.00\n"
        "Total                          180.00\n"
    )


def test_plain_invoice_has_no_discount_or_tax_line():
    text = render_text(invoice(line(1, "200.00")))
    assert "Discount" not in text and "Tax" not in text
