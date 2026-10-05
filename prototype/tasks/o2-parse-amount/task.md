`parse_amount` in `invoicing/money.py` should accept amounts written with thousands separators, for example `"1,234.50"` gives `Decimal("1234.50")`.

- Separators are commas in the whole part only. The first group has one to three digits and every later group has exactly three.
- Anything else that contains a comma is malformed and must raise `ValueError`.
- Input without commas behaves as it does today. This change does not touch rounding.

Add tests for the new behaviour.
