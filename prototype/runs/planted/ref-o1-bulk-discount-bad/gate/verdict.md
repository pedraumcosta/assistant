# Verdict: failed

| | |
|---|---|
| Task | `o1-bulk-discount` |
| Reason | 3 of 4 tests did not pass; first: test_hidden::test_r1_ten_or_more_units_get_five_percent |
| Decided at | hidden-tests |
| Integrity violation | no |
| Risk tier | green |
| Routed to | author |
| Contract | `1e368c61ff7f759a` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `01da766f51b086b8` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 0.2 |
| repo-tests:tests | passed | 17 of 17 tests passed | 0.3 |
| author-tests | passed | 19 of 19 tests passed | 0.3 |
| hidden-tests | failed | 3 of 4 tests did not pass; first: test_hidden::test_r1_ten_or_more_units_get_five_percent | 0.3 |
