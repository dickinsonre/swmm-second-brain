---
title: Historical Water Inventions (app)
type: entity
updated: 2026-11-15
sources: [S118, S129]
tags: [apps, replit, water-history, reference]
reviewed: no
---
Bob's Replit app Historical Water Inventions: an educational app on the history of water engineering: maps and timelines by civilization and site, invention pages, quizzes, calculators and a chatbot. Version 1.0.0, at `historical-mystery-robertdickinson.replit.app` [S129](../sources/S129-historical-water-inventions-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S129](../sources/S129-historical-water-inventions-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S129](../sources/S129-historical-water-inventions-replit-summary.md)
- 221 civilization/region records, 404 historical sites and 1,286 invention records.
- 20 interactive simulator entries and 12 custom SWMM5 input templates offered for download.
- It runs no EPA SWMM5 or other solver. The prepared SWMM5 files were not opened or run in EPA SWMM5 or InfoWorks ICM.
- The channel calculator uses Manning in SI form, `V = (1/n) × R^(2/3) × S^(1/2)` and `Q = V × A`, for a section of `A = width × depth`.
- `npm run check` failed with 11 TypeScript diagnostics across 6 files. No test command is defined.
- Seven routes rendered with no runtime exceptions. `/vr` returned HTTP 200 but its screenshot timed out on both attempts.
- The chatbot streams text from Anthropic's Claude Haiku model.
- The server keeps progress in an in-memory map, not a persistent database.
- Repository: https://github.com/dickinsonre/HistoricalWaterInventions. License MIT. The README credits Robert Dickinson as creator.

**What it does not show.** Historical and engineering claims were not fact-checked. The SWMM5 files were not run. The production build was not run. [S129](../sources/S129-historical-water-inventions-replit-summary.md)

**Noted at ingest.** The site name is historical-mystery (Q77). The `date:` is the day of the summary (Q75). The calculator is SI; the US customary form of Manning, with 1.49, is in [S118](../sources/S118-swmm5-vs-icm-infoworks-networks-replit-summary.md).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM Ecosystem (app)](swmm-ecosystem.md), [EPA SWMM 5](swmm-5.md).
