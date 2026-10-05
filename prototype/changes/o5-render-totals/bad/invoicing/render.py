"""Plain-text rendering of an invoice."""
from invoicing.models import Invoice
from invoicing.pricing import discount, line_total, subtotal, tax, total


def render_text(invoice: Invoice) -> str:
    out = [
        f"Invoice {invoice.number}",
        f"Customer: {invoice.customer}",
        f"Issued: {invoice.issued.isoformat()}",
        "",
    ]
    for line in invoice.lines:
        out.append(f"{line.quantity:>3} x {line.description:<20} {line_total(line):>10}")
    out.append("")
    out.append(f"{'Subtotal':<26} {subtotal(invoice):>10}")
    if invoice.discount_code is not None:
        label = f"Discount ({invoice.discount_code})"
        out.append(f"{label:<26} {-discount(invoice):>10}")
    out.append(f"{'Tax':<26} {tax(invoice):>10}")
    out.append(f"{'Total':<26} {total(invoice):>10}")
    return "\n".join(out) + "\n"
