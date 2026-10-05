# Verdict: failed

| | |
|---|---|
| Task | `o2-parse-amount` |
| Reason | 3 of 5 tests did not pass; first: test_hidden::test_r2_malformed_grouping_is_rejected[12,34] |
| Decided at | hidden-tests |
| Integrity violation | no |
| Risk tier | yellow |
| Routed to | author |
| Contract | `e212fc1711569a46` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `36ab97507e0e12dc` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 1.6 |
| repo-tests:tests | passed | 17 of 17 tests passed | 2.4 |
| author-tests | passed | 18 of 18 tests passed | 2.3 |
| hidden-tests | failed | 3 of 5 tests did not pass; first: test_hidden::test_r2_malformed_grouping_is_rejected[12,34] | 1.7 |
