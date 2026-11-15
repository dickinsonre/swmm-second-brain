---
title: SWMM5 .inp File Viewer (app)
type: entity
updated: 2026-11-15
sources: [S105, S132, S133]
tags: [apps, replit, swmm5, inp-format]
reviewed: no
---
Bob's Replit app SWMM5 .inp File Viewer (ala InfoSWMM): a Streamlit app that reads a SWMM5 `.inp` or `.txt` file and shows each section as a table, with row counts and column statistics, without running a simulation. Version 0.1.0, at `swmm-5-inp-reader-robertdickinson.replit.app` [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md)
- Stack: Python 3.11, Streamlit 1.48.1, Pandas 2.3.2.
- Files larger than 25 MB are rejected.
- Seven known sections get named columns; other sections get generic column names.
- The source holds six themes and an example file with seven section headings.
- The test command ran zero tests. A request to `/` returned 200, but the captured screenshot was blank.
- Git history says the example data and the theme selection were removed; the current source still contains both.
- No license is stated.

**What it does not show.** No user-uploaded file was tested. Browser rendering was not confirmed. [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md)

**Noted at ingest.** The full display name ends "(ala InfoSWMM)".

**Added 15 November 2026: a second app with a like name.** [SWMM5 & EPANET INP Explorer (app)](swmm5-epanet-inp-explorer.md) is a different app, a reference to the input-file formats at another address; it reads pasted text and no uploaded file [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md).

**Added 15 November 2026: a third app with a like name.** [SWMM5 .inp File Interactive Viewer (app)](swmm5-inp-file-interactive-viewer.md) is another app again: a Streamlit page of data grids and statistics for an uploaded input file, at `swmm5filestats.com` [S133](../sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [EPA SWMM 5](swmm-5.md).
