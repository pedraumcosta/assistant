`next_number` in `invoicing/numbering.py` gives wrong numbers when the list has gaps or contains invoices from other years. Fix it.

- It returns the number after the highest sequence already used in the given year.
- Numbers from other years are ignored. With none for the year, it returns `INV-<year>-0001`.
- Entries that are not valid invoice numbers are ignored.
- The sequence is zero-padded to at least four digits.

Add tests for the new behaviour.
