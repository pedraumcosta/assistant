# Explainers

Four pages for a technical audience, written in the first person. They explain the reasoning, the code, the integration and the architecture behind the recommendation. Each is a self-contained HTML file with the same content as the session artifact it was published from.

| Page | What it explains | Artifact |
|---|---|---|
| `decision-trail.html` | How the position moved from "another assistant?" to a 350-line gate: the rules set before research, seven pivots, the decisions with their rejected alternatives, the design review, what the day measured, what went wrong | https://claude.ai/artifact/BCm2bSEFfYuzBwQoowTgRD |
| `code-walkthrough.html` | The prototype file by file: how a task is fed, the verdict ladder as written, how "qualified" is measured, the record every run leaves, the slides mapped to the code | https://claude.ai/artifact/JjCGUh44sdya6BuhhoEGHm |
| `integration-map.html` | Where the evidence layer attaches to harnesses, models and pipelines: the binding pipeline verdict, advisory hooks, the meta-harness channel, model roles, the data boundary, with an architecture drawing | https://claude.ai/artifact/6GECYVd8m29EtwZmH3fWzn |
| `prototype-architecture.html` | The prototype as software: the published scaffold and what wraps it, the five inputs and who sees them, the host process, the three kinds of container, one tool call traced, every output | https://claude.ai/artifact/DfkhTm9ek1xxe2GbCBPZyc |

Reading order: decision trail, prototype architecture, code walkthrough, integration map. Every figure on these pages traces to `docs/research/EVIDENCE.md` or to a run file under `prototype/runs/`.
