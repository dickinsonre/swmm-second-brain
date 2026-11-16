---
title: "S129: Historical Water Inventions, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/historical-mystery-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, water-history, reference]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of Historical Water Inventions, version 1.0.0: an educational app on the history of water engineering: maps and timelines by civilization and site, invention pages, quizzes, calculators and a chatbot. It is one of Bob's Replit apps, at `historical-mystery-robertdickinson.replit.app`. Raw file: [raw/apps/historical-mystery-robertdickinson-v1.0.0.md](../../raw/apps/historical-mystery-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project files do not document which AI tools helped build it. The copy here was read out of the editor of the Replit project named HistoricalWaterInventions on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- 221 civilization/region records, 404 historical sites and 1,286 invention records.
- 20 interactive simulator entries and 12 custom SWMM5 input templates offered for download.
- It runs no EPA SWMM5 or other solver. The prepared SWMM5 files were not opened or run in EPA SWMM5 or InfoWorks ICM.
- The channel calculator uses Manning in SI form, `V = (1/n) × R^(2/3) × S^(1/2)` and `Q = V × A`, for a section of `A = width × depth`.
- `npm run check` failed with 11 TypeScript diagnostics across 6 files. No test command is defined.
- Seven routes rendered with no runtime exceptions. `/vr` returned HTTP 200 but its screenshot timed out on both attempts.
- The chatbot streams text from Anthropic's Claude Haiku model.
- The server keeps progress in an in-memory map, not a persistent database.
- Repository: https://github.com/dickinsonre/HistoricalWaterInventions. License MIT. The README credits Robert Dickinson as creator.

**Limits it states.** Historical and engineering claims were not fact-checked. The SWMM5 files were not run. The production build was not run.

**Checked at ingest.** The site name is historical-mystery (Q77). The `date:` is the day of the summary (Q75). The calculator is SI; the US customary form of Manning, with 1.49, is in [S118](S118-swmm5-vs-icm-infoworks-networks-replit-summary.md).

**Feeds:** [Historical Water Inventions (app)](../entities/historical-water-inventions.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM Ecosystem (app)](../entities/swmm-ecosystem.md), [EPA SWMM 5](../entities/swmm-5.md).
