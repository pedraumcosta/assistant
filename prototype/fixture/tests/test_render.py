from invoicing.render import render_text
from tests.helpers import invoice, line


def test_render_text():
    text = render_text(invoice(line(2, "9.99")))
    assert text.startswith(
        "Invoice INV-2026-0001\n"
        "Customer: Acme Ltd\n"
        "Issued: 2026-10-05\n"
        "\n"
        "  2 x Widget                    19.98\n"
    )
    assert text.endswith("Total                           19.98\n")
