---
title: "Goyen Thesis Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S344]
tags: [apps, papers, rainfall-runoff, thesis]
reviewed: no
---
Bob's app Goyen Thesis Explorer: a reader and evidence bench for Allan Goyen's 2000 thesis on urban rainfall-runoff. Version 2.1.0, 2026-10-22 [S344](../sources/S344-goyen-thesis-explorer-summary.md). Its `links:` line names no live Netlify address [S344](../sources/S344-goyen-thesis-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S344](../sources/S344-goyen-thesis-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S344](../sources/S344-goyen-thesis-explorer-summary.md)
- A reader and evidence bench for one document, Allan Goyen's PhD thesis Spatial and Temporal Effects on Urban Rainfall/Runoff Modelling (University of Technology, Sydney, April 2000), on the Giralang catchment and process-tree modelling. It rebuilds the chapters, page numbers and figure and table lists from a 22,703-line Markdown file, charts 14 datasets lifted from its tables, draws the network, and exports SWMM5 .inp files of it.
- Of 17 re-derivations of the thesis's own table arithmetic, 11 reproduce the printed figures, 4 differ and 2 are notes; none overturns its conclusion that the process tree model has the smallest peak errors. Version 2.1 found that the SI export carried two US numbers (MIN_SURFAREA 12.566 ft2, HEAD_TOLERANCE 0.005 ft), which moved outlet volume 5.944% and put the outlet hydrograph 18.518% (RMS) away from the US file in SWMM 5.2.4; they are now converted and the files agree.
- Value located: 5,988 numbers in 14 datasets each occur in the source lines of their table (magnitude only).
- Cell matched: 6,866 cells in 15 datasets match an independent re-parse of the source table by row, column and sign; 0 differ. The test found and restored one value the first extraction had dropped.
- Arithmetic reproduced: 11 of 17 checks reproduce the printed figures; 4 differ (a count off by one, a ratio implying a different flow, two quantities sharing a column) and 2 are notes.
- Engine test: 12 .inp variants ran in EPA SWMM 5.2.4 under a test inflow with 0 errors; US and SI files of the default export agree within 0.002% in outlet volume and 0.0007 ft (0.0002 m) in peak depth.

**How to use it, as the summary puts it.** Use it to read the thesis with its numbers checked. Nothing was compared against the pages of the original PDF (only the Markdown was used), and the process tree model was not re-run: its XP-RAFTS workbench and gauged data were on the thesis CD-ROM, which is not available. [S344](../sources/S344-goyen-thesis-explorer-summary.md)

**What it does not show.** As the page lists it: no comparison against the original Word document or PDF; only the Markdown was used. No re-run of the process tree model, since the XP-RAFTS workbench and gauged data were on the thesis CD-ROM. A run that passes says nothing about whether the exported model is the thesis's model. [S344](../sources/S344-goyen-thesis-explorer-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).
