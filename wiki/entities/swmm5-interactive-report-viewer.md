---
title: "SWMM5 Interactive Report Viewer (app)"
type: entity
updated: 2026-11-18
sources: [S325]
tags: [apps, swmm5, rpt, out, verification]
reviewed: no
---
Bob's app SWMM5 Interactive Report Viewer: the .rpt, .inp and .out of an EPA SWMM 5 run, read and checked. Version 2.1, 2026-10-31 [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md). Its `links:` line names no live Netlify address [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md).

**A caution about its source.** The page ships no technical summary. [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md)
- Reads the three files an EPA SWMM 5 run leaves behind: the text report (.rpt, required), the input file (.inp, which adds the map, rim elevations, pipe offsets and pollutant names) and the binary output (.out, which adds time series and a timed map). Interactive grids, joined sections, graphs, a profile and a map.
- Checked against 59 reports written by EPA SWMM 5.2.4 (9 written for the app, 50 from three other projects' test suites): .out values against EPA's swmm_output bit-identical on 54 runs (4,291,001 values, 0 failed); report numbers against engine statistics at print precision (4,758, 0 failed); every word of 16,413 table cells kept in order. Version 2.1 fixed five defects a review of 2.0 found, such as pollutant names of 14 characters or more that hid the quality continuity sections, and links coloured by SWMM's capacity variable, which is the control setting for anything but a conduit.
- 59 reports from EPA SWMM 5.2.4 (build 52004) through swmm-toolkit 0.17.0; 48 of the 50 borrowed models ran to completion.
- .out values against EPA swmm_output: 54 runs, 4,291,001 values, 0 failed. Report numbers against engine statistics: 54 runs, 4,758, 0 failed. Table rows: 59 reports, 16,413 cells, 2,282 rows, 0 failed. Continuity rows in the right columns: 1,409, 0 failed. .inp geometry against the engine's echo: 30 reports, 841, 0 failed.
- The review's defects in a browser: version 2.0 failed 12 of 12; version 2.1 passes 12.

**How to use it, as the summary puts it.** Use it to read any 5.2 report with confidence that the numbers are the engine's. Reports from SWMM 5.1 and OpenSWMM 6 are untested, and the profile draws the water surface inside a conduit as a straight line between its nodes. [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md)

**What it does not show.** As the page lists it: reports from SWMM 5.1 and OpenSWMM 6 are untested; street, transect and inlet geometry tables are shown as printed, not parsed into columns; the profile draws the water surface inside each conduit as a straight line (SWMM computes one depth per conduit); rim elevation and freeboard are computed by the app from invert plus maximum depth, which SWMM prints neither of. [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [SWMM Results Kit](swmm-results-kit.md).
