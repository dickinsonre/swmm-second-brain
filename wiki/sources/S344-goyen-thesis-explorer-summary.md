---
title: "S344: Goyen Thesis Explorer, summary written from the page (v2.1.0)"
type: source
raw: raw/apps/goyen-thesis-explorer-v2.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
tags: [apps, papers, rainfall-runoff, thesis]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Goyen Thesis Explorer, version 2.1.0: a reader and evidence bench for Allan Goyen's 2000 thesis on urban rainfall-runoff. Raw file: [raw/apps/goyen-thesis-explorer-v2.1.0.md](../../raw/apps/goyen-thesis-explorer-v2.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/21Cz2vaukrBumw5hQ9zirM, version 1792673443-4e4f (index.html, 1,839,014 bytes, SHA-256 106474e3672eb6d36ba1c22b5aa1370a7fec5fc5a8e35e126319f1030a3c0dac), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model (model id claude-opus-5-5), in Claude sessions on 21 and 22 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project and the thesis Markdown, asked for a single-file HTML app, and for version 2.1 passed on an outside review of version 2.0 and asked for its ideas to be added; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A reader and evidence bench for one document, Allan Goyen's PhD thesis Spatial and Temporal Effects on Urban Rainfall/Runoff Modelling (University of Technology, Sydney, April 2000), on the Giralang catchment and process-tree modelling. It rebuilds the chapters, page numbers and figure and table lists from a 22,703-line Markdown file, charts 14 datasets lifted from its tables, draws the network, and exports SWMM5 .inp files of it.
- Of 17 re-derivations of the thesis's own table arithmetic, 11 reproduce the printed figures, 4 differ and 2 are notes; none overturns its conclusion that the process tree model has the smallest peak errors. Version 2.1 found that the SI export carried two US numbers (MIN_SURFAREA 12.566 ft2, HEAD_TOLERANCE 0.005 ft), which moved outlet volume 5.944% and put the outlet hydrograph 18.518% (RMS) away from the US file in SWMM 5.2.4; they are now converted and the files agree.
- Value located: 5,988 numbers in 14 datasets each occur in the source lines of their table (magnitude only).
- Cell matched: 6,866 cells in 15 datasets match an independent re-parse of the source table by row, column and sign; 0 differ. The test found and restored one value the first extraction had dropped.
- Arithmetic reproduced: 11 of 17 checks reproduce the printed figures; 4 differ (a count off by one, a ratio implying a different flow, two quantities sharing a column) and 2 are notes.
- Engine test: 12 .inp variants ran in EPA SWMM 5.2.4 under a test inflow with 0 errors; US and SI files of the default export agree within 0.002% in outlet volume and 0.0007 ft (0.0002 m) in peak depth.

**Limits it states.** As the page lists it: no comparison against the original Word document or PDF; only the Markdown was used. No re-run of the process tree model, since the XP-RAFTS workbench and gauged data were on the thesis CD-ROM. A run that passes says nothing about whether the exported model is the thesis's model.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Goyen Thesis Explorer (app)](../entities/goyen-thesis-explorer.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).
