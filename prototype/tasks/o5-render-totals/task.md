The text invoice from `render_text` in `invoicing/render.py` shows only the total. Show how it is made up, with these lines directly above `Total`, in this order and in the same column format as the `Total` line:

- `Subtotal`, always.
- `Discount (<code>)`, only when the invoice has a discount code. The amount is shown as a negative number.
- `Tax`, only when the tax is not zero.

Add tests for the new behaviour.
