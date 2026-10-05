from invoicing.pricing import merge_lines
from tests.helpers import line


def test_merges_same_sku():
    assert merge_lines((line(2), line(3))) == (line(5),)


def test_keeps_order():
    merged = merge_lines((line(1, sku="B"), line(1, sku="A"), line(1, sku="B")))
    assert [m.sku for m in merged] == ["B", "A"]
