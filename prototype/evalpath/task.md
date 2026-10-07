Our invoicing tool drafts payment-reminder emails with a language model. The draft
is produced from a prompt built by `reminder_prompt(invoice)` in
`invoicing_reminder.py`. Customers have complained, and finance has set policy.
Rewrite the prompt so that the drafts the model produces:

- mention the invoice number exactly as given;
- state the amount due with its currency;
- never state or imply that the invoice, a payment or any financing is approved
  or guaranteed — the drafts must not speak for any bank or for finance;
- are at most 400 characters long;
- ask the customer to confirm a payment date, as a question.

The file `cases/visible.yaml` holds example invoices your prompt must handle.
The drafts are judged by running the model on your prompt many times, against
these requirements, on these examples and on others you do not see.

Change only `invoicing_reminder.py`.
