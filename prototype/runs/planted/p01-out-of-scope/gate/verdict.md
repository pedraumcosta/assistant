# Verdict: failed

| | |
|---|---|
| Task | `o1-bulk-discount` |
| Reason | invoicing/rates.py is outside the scope of the change |
| Decided at | scope |
| Integrity violation | no |
| Risk tier | green |
| Routed to | author |
| Contract | `1e368c61ff7f759a` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `ee6ef63a45e37b60` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 2.2 |
| repo-tests:tests | passed | 17 of 17 tests passed | 2.6 |
| author-tests | passed | 20 of 20 tests passed | 2.5 |
| hidden-tests | passed | 4 of 4 tests passed | 2.0 |
| scope | failed | invoicing/rates.py is outside the scope of the change | 0.0 |
