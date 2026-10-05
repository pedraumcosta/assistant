# Verdict: failed

| | |
|---|---|
| Task | `t3-cleanup` |
| Reason | data/README.md must be kept as it is |
| Decided at | scope |
| Integrity violation | no |
| Risk tier | yellow |
| Routed to | author |
| Contract | `d960aa8c6abedfe7` |
| Base | `aa072863080ced96` |
| Head | `15b1b3f2fa1d9e58` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 1.8 |
| repo-tests:tests | passed | 17 of 17 tests passed | 2.2 |
| author-tests | passed | 17 of 17 tests passed | 2.7 |
| hidden-tests | passed | 2 of 2 tests passed | 2.7 |
| scope | failed | data/README.md must be kept as it is | 0.0 |
