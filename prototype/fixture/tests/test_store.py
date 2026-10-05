from invoicing.store import load, save
from tests.helpers import invoice, line


def test_round_trip(tmp_path):
    inv = invoice(line(2, "9.99"), region="UK", discount_code="WELCOME10")
    save(inv, tmp_path)
    assert load(inv.number, tmp_path) == inv
