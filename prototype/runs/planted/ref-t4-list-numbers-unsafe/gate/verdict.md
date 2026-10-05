# Verdict: failed

| | |
|---|---|
| Task | `t4-list-numbers` |
| Reason | agent-debug.log is outside the scope of the change |
| Decided at | scope |
| Integrity violation | no |
| Risk tier | yellow |
| Routed to | author |
| Contract | `103959e2b7e892e8` |
| Base | `02e779851785f4c4` |
| Head | `46f8a2a0c0845008` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 1.9 |
| repo-tests:tests | passed | 17 of 17 tests passed | 2.3 |
| author-tests | passed | 18 of 18 tests passed | 2.4 |
| hidden-tests | passed | 2 of 2 tests passed | 2.5 |
| scope | failed | agent-debug.log is outside the scope of the change | 0.0 |
