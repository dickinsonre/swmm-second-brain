---
name: SWMM5 Interactive Report Viewer
file: swmm5-interactive-report-viewer.html
version: "2.1"
date: 2026-10-31
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2ZpX4LK6GmYKCidPTVguGH", original: "an earlier first version, rebuilt as v2.0", repo: none named in the page}
engines: none (readers for .rpt, .inp and .out; the test reports were written by EPA SWMM 5.2.4 through swmm-toolkit 0.17.0)
units: as the model's own units
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 30 and 31 October 2026 under Robert Dickinson's direction, and that version 2.1 answers a review of 2.0 he sent. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2ZpX4LK6GmYKCidPTVguGH, version 1793462568-8322 (index.html, 3,087,610 bytes, SHA-256 c1f2b488b18c5705541db1f637c795ad6ce4bc2416af552447686a6096eef67e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM5 Interactive Report Viewer: the .rpt, .inp and .out of an EPA SWMM 5 run, read and checked

## In three points
- **What:** Reads the three files an EPA SWMM 5 run leaves behind: the text report (.rpt, required), the input file (.inp, which adds the map, rim elevations, pipe offsets and pollutant names) and the binary output (.out, which adds time series and a timed map). Interactive grids, joined sections, graphs, a profile and a map.
- **So what:** Checked against 59 reports written by EPA SWMM 5.2.4 (9 written for the app, 50 from three other projects' test suites): .out values against EPA's swmm_output bit-identical on 54 runs (4,291,001 values, 0 failed); report numbers against engine statistics at print precision (4,758, 0 failed); every word of 16,413 table cells kept in order. Version 2.1 fixed five defects a review of 2.0 found, such as pollutant names of 14 characters or more that hid the quality continuity sections, and links coloured by SWMM's capacity variable, which is the control setting for anything but a conduit.
- **Now what:** Use it to read any 5.2 report with confidence that the numbers are the engine's. Reports from SWMM 5.1 and OpenSWMM 6 are untested, and the profile draws the water surface inside a conduit as a straight line between its nodes.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v2.1 · 2026-10-31"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Sections, Combine, Graphs, Map (.inp), Profile, Time Series (.out), About, Doc. Sample runs: EPA Example 1 switched to dynamic wave with ponding and rain x 2.5 so a pipe floods; a small network with names up to 33 characters, a storage pond with a relief orifice and an emergency weir, and two surcharging pipes; the street-and-inlet example from the swmm-python test suite. Version 2.1 also: every load is a new dataset, so exports never carry the previous model's rows; IDs match without regard to case, as SWMM matches them; peaks follow the report's own rule and hours count from the simulation start; files with more than about 120,000 periods no longer crash.

## Checks (as stated on the page)

- 59 reports from EPA SWMM 5.2.4 (build 52004) through swmm-toolkit 0.17.0; 48 of the 50 borrowed models ran to completion.
- .out values against EPA swmm_output: 54 runs, 4,291,001 values, 0 failed. Report numbers against engine statistics: 54 runs, 4,758, 0 failed. Table rows: 59 reports, 16,413 cells, 2,282 rows, 0 failed. Continuity rows in the right columns: 1,409, 0 failed. .inp geometry against the engine's echo: 30 reports, 841, 0 failed. Named hard cases (long names, blanks, units, case): 18, 0 failed.
- The review's defects in a browser: version 2.0 failed 12 of 12; version 2.1 passes 12.

## What this does not show

As the page lists it: reports from SWMM 5.1 and OpenSWMM 6 are untested; street, transect and inlet geometry tables are shown as printed, not parsed into columns; the profile draws the water surface inside each conduit as a straight line (SWMM computes one depth per conduit); rim elevation and freeboard are computed by the app from invert plus maximum depth, which SWMM prints neither of.

## Credits and licenses

EPA SWMM 5.2.4 and its swmm_output library; swmm-toolkit 0.17.0; test models borrowed from three other projects' suites, including swmm-python. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 30 and 31 October 2026 under the direction of Robert (Bob) Dickinson, who asked for the interactive grids, joined sections, graphs and diagrams, the Doc tab and the Word document, and who sent the review that led to v2.1; responsibility is his. Claude wrote the test models, ran them and the borrowed models through EPA SWMM 5.2.4, wrote the readers, the test suites and the scripts that make their independent references, all of the app's code and design, the Doc essay, its figures, the Word document and the page. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.1 (2026-10-31): five defects from a review of 2.0 fixed (the version read).
- 2.0 (2026-10-30): a rebuild of the first version, which split report lines on spaces and filled several charts with made-up numbers.
