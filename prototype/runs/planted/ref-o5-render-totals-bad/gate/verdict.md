# Verdict: failed

| | |
|---|---|
| Task | `o5-render-totals` |
| Reason | 1 of 4 tests did not pass; first: test_hidden::test_r3_tax_only_when_not_zero |
| Decided at | hidden-tests |
| Integrity violation | no |
| Risk tier | green |
| Routed to | author |
| Contract | `f17aa2d718813b64` |
| Base | `15b1b3f2fa1d9e58` |
| Head | `1fb4bbab6ef6f659` |

## Evidence

| Check | Result | Reason | Seconds |
|---|---|---|---|
| integrity | passed | nothing found | 0.0 |
| budget | passed | nothing found | 0.0 |
| build | passed | parses and imports | 0.2 |
| repo-tests:tests | passed | 17 of 17 tests passed | 0.3 |
| author-tests | passed | 18 of 18 tests passed | 0.3 |
| hidden-tests | failed | 1 of 4 tests did not pass; first: test_hidden::test_r3_tax_only_when_not_zero | 0.3 |
