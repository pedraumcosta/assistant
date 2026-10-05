A payment must never fall due on a weekend. Change `due_date` in `invoicing/terms.py`: when the computed date is a Saturday or a Sunday, the due date is the following Monday.

Add tests for the new behaviour.
