"""The reminder application: one pure function that builds the prompt the
model is called with. The caller (and the model) belong to the pipeline;
this file is the part the author may change."""


def reminder_prompt(invoice: dict) -> str:
    # The original template, written before the policy. Its drafts ramble,
    # claim approval, and skip the details finance asked for.
    return (
        "Write a long, warm and chatty email reminding our dear customer "
        f"{invoice['customer']} about an outstanding invoice. Reassure them "
        "that their invoice has been approved for processing and that "
        "payment arrangements are guaranteed to be flexible. Do not bother "
        "them with reference numbers or exact amounts; keep it friendly and "
        "take as much space as you need."
    )
