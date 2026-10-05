Add quantity pricing to `line_total` in `invoicing/pricing.py`.

- A line with 10 or more units gets 5% off that line.
- A line with 50 or more units gets 10% off that line.
- The discount is applied to the line's total (unit price times quantity), and the result is rounded with the existing `round_cents` helper.

Add tests for the new behaviour.
