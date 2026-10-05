Add a function `merge_lines(lines)` to `invoicing/pricing.py`. It returns a new tuple of line items in which lines with the same SKU and the same unit price are combined into one line with their quantities added.

- The merged line keeps the description of the first of them.
- Lines keep the order in which their SKU and price first appear.
- Lines with the same SKU but a different unit price stay separate.

Add tests for the new function.
