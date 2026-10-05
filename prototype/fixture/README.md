# invoicing

Line items, discounts, tax, invoice numbers, payment terms, a text rendering and a JSON store.

| Module | What it does |
|---|---|
| `money.py` | Rounding and parsing of amounts. Shared with the payments service |
| `rates.py` | Tax rates by region and discount codes. Owned by finance |
| `models.py` | `LineItem` and `Invoice` |
| `pricing.py` | Line totals, subtotal, discount, tax, total |
| `numbering.py` | Invoice numbers |
| `terms.py` | Due dates |
| `render.py` | Plain-text invoice |
| `store.py` | Save and load invoices as JSON |
