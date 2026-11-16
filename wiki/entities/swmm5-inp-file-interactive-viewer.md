---
title: "SWMM5 .inp File Interactive Viewer (app)"
type: entity
updated: 2026-11-15
sources: [S105, S132, S133]
tags: [apps, replit, swmm5, inp-files, statistics]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5 .inp File Interactive Viewer: a Streamlit app that takes EPA SWMM5 input text, shows each section as a data grid and gives descriptive statistics and charts of the columns. Version 0.1.0, at `swmm5filestats.com` [S133](../sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S133](../sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S133](../sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md)
- It displays input data and does not run a SWMM simulation. `engines: none`.
- It accepts `.inp` and `.txt` uploads. The validator rejects files larger than `200 * 1024 * 1024` bytes.
- The parser starts a section at each bracketed section header, skips comments, and splits data rows on whitespace. It uses comment headers when available, otherwise one of the 17 built-in section column schemas or generic column names.
- For each column it reports the mean, standard deviation, minimum, quartiles, median, and maximum, and value frequencies. Frequency percentage is `count / row_count * 100`.
- Charts are Plotly histograms, violin plots, frequency plots, box plots, scatter matrices, correlation heatmaps, bar charts, density plots, and parallel-coordinate plots.
- No hydraulic or hydrologic equations are run, and the app does not convert units. `units: not applicable`.
- 9 selectable theme definitions. The built-in example contains 10 sections and 43 data rows.
- A parser smoke check parsed the built-in example into 10 DataFrames with 43 rows total, and the Python syntax check passed. `python -m pytest -q` could not start because `pytest` is not installed. No test files were found.
- The stack is Python 3.11 with Streamlit, Pandas and Plotly. NetworkX is declared as a dependency but is not imported by `app.py`.
- The one page is titled SWMM5 .inp File Viewer. A download button exports `app.py` as `swmm_dashboard.py`.
- The project states no license. Git history records `robertdickinson`, and assistant-checkpoint entries under `dickinsonre_Autodesk_Water`; the file says the commit labels do not establish which work was AI-assisted.

**What it does not show.** No user file was uploaded in the check, and chart generation, grid export and the source download were not exercised. The production page was not loaded. A public GitHub address was not verified. [S133](../sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md)

**Noted at ingest.** The `file:` is social-network-analyzer-robertdickinson, the Replit project is SWMM5NetworkAnalyzer, the site address is `swmm5filestats.com` and the app's name is SWMM5 .inp File Interactive Viewer (Q77). It is the third app here with a name like an INP viewer, after the [SWMM5 .inp File Viewer (app)](swmm5-inp-file-viewer.md) [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md) and the [SWMM5 & EPANET INP Explorer (app)](swmm5-epanet-inp-explorer.md) [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md). The `date:` is the day of the summary; the change list runs from 26 August 2025 to 10 March 2026 (Q75). It is added to the concept page as a twentieth row.

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 .inp File Viewer (app)](swmm5-inp-file-viewer.md), [SWMM5 & EPANET INP Explorer (app)](swmm5-epanet-inp-explorer.md), [SWMM5 Network Miner (app)](swmm5-network-miner.md).
