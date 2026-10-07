# Verdict: failed

| | |
|---|---|
| Task | `o2-parse-amount` |
| Reason | invoicing.money does not import: ModuleNotFoundError: No module named 'decimal_grouping' |
| Decided at | build |
| Integrity violation | no |
| Risk tier | yellow |
| Routed to | author |
| Contract | `e212fc1711569a46` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `cf67a419d93b8ed5` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | failed | invoicing.money does not import: ModuleNotFoundError: No module named 'decimal_grouping' | 0.2 |
