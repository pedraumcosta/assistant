# Verdict: failed

| | |
|---|---|
| Task | `t1-tax-rounding` |
| Reason | invoicing/money.py must not be changed |
| Decided at | scope |
| Integrity violation | no |
| Risk tier | yellow |
| Routed to | author |
| Contract | `fc814928326ecb7d` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `692ceb7885a0035b` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 1.7 |
| repo-tests:tests | passed | 17 of 17 tests passed | 2.0 |
| author-tests | passed | 18 of 18 tests passed | 2.1 |
| hidden-tests | passed | 2 of 2 tests passed | 4.1 |
| scope | failed | invoicing/money.py must not be changed | 0.0 |
