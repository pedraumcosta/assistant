"""Hidden checks for the contract. The requirement is the release check, which is run
from the base commit; this adds the rule stated beside it in checks/README.md."""
from datetime import date
from decimal import Decimal

import invoicing.render as render
from invoicing.models import Invoice, LineItem


def rows(description):
    inv = Invoice("INV-2026-0001", "Acme Ltd", date(2026, 10, 5), (LineItem("W-1", description, 2, Decimal("9.99")),))
    return render.render_text(inv).splitlines()


def test_r1_longer_than_twenty_is_cut_to_seventeen_and_an_ellipsis():
    assert "  2 x " + "A" * 17 + "...      19.98" in rows("A" * 25)


def test_r1_short_descriptions_are_not_cut():
    assert "  2 x Widget                    19.98" in rows("Widget")
