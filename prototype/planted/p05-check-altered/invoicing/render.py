"""Plain-text rendering of an invoice."""
from invoicing.models import Invoice
from invoicing.pricing import line_total, total


def render_text(invoice: Invoice) -> str:
    out = [
        f"Invoice {invoice.number}",
        f"Customer: {invoice.customer}",
        f"Issued: {invoice.issued.isoformat()}",
        "",
    ]
    for line in invoice.lines:
        description = line.description
        if len(description) > 20:
            description = description[:17] + "..."
        out.append(f"{line.quantity:>3} x {description:<20} {line_total(line):>10}")
    out.append("")
    out.append(f"{'Total':<26} {total(invoice):>10}")
    return "\n".join(out) + "\n"
