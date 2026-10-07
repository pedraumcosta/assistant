# Exported decks

The two stakeholder PDFs, exported from `docs/slides.md` (the single source
for both): part one is the ten-minute recommendation, part two the technical
walkthrough. The backup slides are in neither; they are for the live
discussion.

| File | Content |
|---|---|
| `ASSIST-recommendation.pdf` | Slides 1–12: the recommendation, ending on the executive page |
| `ASSIST-technical-walkthrough.pdf` | The technical walkthrough, cover through the redlines |

To regenerate after editing `docs/slides.md`: split the deck at the part-two
and backup dividers into two Slidev entry files and export each
(`npx slidev export <part>.md --output <file>.pdf`). The split is needed
because this Slidev version ignores `--range` for PDF export.
