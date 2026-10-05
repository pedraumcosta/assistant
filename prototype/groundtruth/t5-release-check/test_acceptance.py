from datetime import date
from decimal import Decimal

import pytest

import invoicing.render as render
from invoicing.models import Invoice, LineItem


def rows(description, quantity=2, price="9.99"):
    line = LineItem("W-1", description, quantity, Decimal(price))
    inv = Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5), (line,))
    return render.render_text(inv).splitlines()


def test_the_release_check_itself():
    out = rows("Extended warranty, three years, on-site")
    assert all(len(row) <= 37 for row in out)
    assert "  2 x Extended warranty...      19.98" in out


@pytest.mark.parametrize("description,shown", [
    ("Widget", "Widget              "),
    ("A" * 20, "A" * 20),                       # exactly the width: not cut
    ("A" * 21, "A" * 17 + "..."),               # one over: cut
    ("B" * 60, "B" * 17 + "..."),
])
def test_descriptions(description, shown):
    assert f"  2 x {shown}      19.98" in rows(description)


def test_short_invoice_is_unchanged():
    assert rows("Widget") == [
        "Invoice INV-2026-0001", "Customer: Acme Ltd", "Issued: 2026-10-05", "",
        "  2 x Widget                    19.98", "", "Total                           19.98",
    ]
