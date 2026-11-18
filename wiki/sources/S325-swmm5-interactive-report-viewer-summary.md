---
title: "S325: SWMM5 Interactive Report Viewer, summary written from the page (v2.1)"
type: source
raw: raw/apps/swmm5-interactive-report-viewer-v2.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-31
ingested: 2026-11-18
tags: [apps, swmm5, rpt, out, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 Interactive Report Viewer, version 2.1: the .rpt, .inp and .out of an EPA SWMM 5 run, read and checked. Raw file: [raw/apps/swmm5-interactive-report-viewer-v2.1.md](../../raw/apps/swmm5-interactive-report-viewer-v2.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/2ZpX4LK6GmYKCidPTVguGH, version 1793462568-8322 (index.html, 3,087,610 bytes, SHA-256 c1f2b488b18c5705541db1f637c795ad6ce4bc2416af552447686a6096eef67e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 30 and 31 October 2026 under the direction of Robert (Bob) Dickinson, who asked for the interactive grids, joined sections, graphs and diagrams, the Doc tab and the Word document, and who sent the review that led to v2.1; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Reads the three files an EPA SWMM 5 run leaves behind: the text report (.rpt, required), the input file (.inp, which adds the map, rim elevations, pipe offsets and pollutant names) and the binary output (.out, which adds time series and a timed map). Interactive grids, joined sections, graphs, a profile and a map.
- Checked against 59 reports written by EPA SWMM 5.2.4 (9 written for the app, 50 from three other projects' test suites): .out values against EPA's swmm_output bit-identical on 54 runs (4,291,001 values, 0 failed); report numbers against engine statistics at print precision (4,758, 0 failed); every word of 16,413 table cells kept in order. Version 2.1 fixed five defects a review of 2.0 found, such as pollutant names of 14 characters or more that hid the quality continuity sections, and links coloured by SWMM's capacity variable, which is the control setting for anything but a conduit.
- 59 reports from EPA SWMM 5.2.4 (build 52004) through swmm-toolkit 0.17.0; 48 of the 50 borrowed models ran to completion.
- .out values against EPA swmm_output: 54 runs, 4,291,001 values, 0 failed. Report numbers against engine statistics: 54 runs, 4,758, 0 failed. Table rows: 59 reports, 16,413 cells, 2,282 rows, 0 failed. Continuity rows in the right columns: 1,409, 0 failed. .inp geometry against the engine's echo: 30 reports, 841, 0 failed.
- The review's defects in a browser: version 2.0 failed 12 of 12; version 2.1 passes 12.

**Limits it states.** As the page lists it: reports from SWMM 5.1 and OpenSWMM 6 are untested; street, transect and inlet geometry tables are shown as printed, not parsed into columns; the profile draws the water surface inside each conduit as a straight line (SWMM computes one depth per conduit); rim elevation and freeboard are computed by the app from invert plus maximum depth, which SWMM prints neither of.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5 Interactive Report Viewer (app)](../entities/swmm5-interactive-report-viewer.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [SWMM Results Kit](../entities/swmm-results-kit.md).
