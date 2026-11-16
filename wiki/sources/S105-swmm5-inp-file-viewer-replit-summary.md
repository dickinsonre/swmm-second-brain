---
title: "S105: SWMM5 .inp File Viewer (ala InfoSWMM), summary written by Replit Agent (v0.1.0)"
type: source
raw: raw/apps/swmm-5-inp-reader-robertdickinson-v0.1.0.md
kind: app-md
author: Robert Dickinson
published: 2025-08-26
ingested: 2026-11-15
tags: [apps, replit, swmm5, inp-format]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 .inp File Viewer (ala InfoSWMM), version 0.1.0: a Streamlit app that reads a SWMM5 `.inp` or `.txt` file and shows each section as a table, with row counts and column statistics, without running a simulation. It is one of Bob's Replit apps, at `swmm-5-inp-reader-robertdickinson.replit.app`. Raw file: [raw/apps/swmm-5-inp-reader-robertdickinson-v0.1.0.md](../../raw/apps/swmm-5-inp-reader-robertdickinson-v0.1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says Git history attributes the visual update of 2026-05-27 to Replit Agent and does not identify who originally wrote the app. The copy here was read out of the editor of the Replit project named SWMM5InpReader on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Stack: Python 3.11, Streamlit 1.48.1, Pandas 2.3.2.
- Files larger than 25 MB are rejected.
- Seven known sections get named columns; other sections get generic column names.
- The source holds six themes and an example file with seven section headings.
- The test command ran zero tests. A request to `/` returned 200, but the captured screenshot was blank.
- Git history says the example data and the theme selection were removed; the current source still contains both.
- No license is stated.

**Limits it states.** No user-uploaded file was tested. Browser rendering was not confirmed.

**Checked at ingest.** The full display name ends "(ala InfoSWMM)".

**Feeds:** [SWMM5 .inp File Viewer (app)](../entities/swmm5-inp-file-viewer.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [EPA SWMM 5](../entities/swmm-5.md).
