---
name: Goyen Thesis Explorer
file: goyen-thesis-explorer.html
version: 2.1.0
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/21Cz2vaukrBumw5hQ9zirM", original: "Lovable app MD Insight Explorer; version 1 and the thesis Markdown at github.com/SWMMEnablement/md-insight-explorer", thesis: "https://opus.lib.uts.edu.au/handle/2100/626"}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "compiled and used while building to run the 12 .inp export variants; the page exports .inp files and does not run an engine"}
units: US customary by default, SI behind a toggle (the thesis is metric)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (model id claude-opus-5-5) on 21 and 22 October 2026 under Robert Dickinson's direction, and that version 2.1 adds ideas from an outside review of version 2.0. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/21Cz2vaukrBumw5hQ9zirM, version 1792673443-4e4f (index.html, 1,839,014 bytes, SHA-256 106474e3672eb6d36ba1c22b5aa1370a7fec5fc5a8e35e126319f1030a3c0dac), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# Goyen Thesis Explorer: a reader and evidence bench for Allan Goyen's 2000 thesis on urban rainfall-runoff

## In three points
- **What:** A reader and evidence bench for one document, Allan Goyen's PhD thesis Spatial and Temporal Effects on Urban Rainfall/Runoff Modelling (University of Technology, Sydney, April 2000), on the Giralang catchment and process-tree modelling. It rebuilds the chapters, page numbers and figure and table lists from a 22,703-line Markdown file, charts 14 datasets lifted from its tables, draws the network, and exports SWMM5 .inp files of it.
- **So what:** Of 17 re-derivations of the thesis's own table arithmetic, 11 reproduce the printed figures, 4 differ and 2 are notes; none overturns its conclusion that the process tree model has the smallest peak errors. Version 2.1 found that the SI export carried two US numbers (MIN_SURFAREA 12.566 ft2, HEAD_TOLERANCE 0.005 ft), which moved outlet volume 5.944% and put the outlet hydrograph 18.518% (RMS) away from the US file in SWMM 5.2.4; they are now converted and the files agree.
- **Now what:** Use it to read the thesis with its numbers checked. Nothing was compared against the pages of the original PDF (only the Markdown was used), and the process tree model was not re-run: its XP-RAFTS workbench and gauged data were on the thesis CD-ROM, which is not available.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.1.0"); the date is the last build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Read, Evidence, Network, Checks, About, Doc. The reader searches (30 results at a time), jumps to sections and captions, keeps back and forward history and bookmarks, and opens the UTS PDF at the matching page once you type the PDF page that holds thesis page 1 (an offset the app has not checked). The export keeps every printed slope by putting offsets at both pipe ends; the older method, still offered, changes 101 slopes and turns two adverse. Table 8.2.1a opens the 10 calibration peaks, kept apart from validation.

## Checks (as stated on the page)

- Value located: 5,988 numbers in 14 datasets each occur in the source lines of their table (magnitude only).
- Cell matched: 6,866 cells in 15 datasets match an independent re-parse of the source table by row, column and sign; 0 differ. The test found and restored one value the first extraction had dropped.
- Arithmetic reproduced: 11 of 17 checks reproduce the printed figures; 4 differ (a count off by one, a ratio implying a different flow, two quantities sharing a column) and 2 are notes.
- Engine test: 12 .inp variants ran in EPA SWMM 5.2.4 under a test inflow with 0 errors; US and SI files of the default export agree within 0.002% in outlet volume and 0.0007 ft (0.0002 m) in peak depth.
- Original inspected: not done.

## What this does not show

As the page lists it: no comparison against the original Word document or PDF; only the Markdown was used. No re-run of the process tree model, since the XP-RAFTS workbench and gauged data were on the thesis CD-ROM. A run that passes says nothing about whether the exported model is the thesis's model.

## Credits and licenses

Allan Goyen, PhD thesis, University of Technology, Sydney, 2000, open access at UTS (handle 10453/20057); SWMMEnablement/md-insight-explorer (version 1 and the Markdown file); EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model (model id claude-opus-5-5), in Claude sessions on 21 and 22 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project and the thesis Markdown, asked for a single-file HTML app, and for version 2.1 passed on an outside review of version 2.0 and asked for its ideas to be added; responsibility is his. Claude read the Lovable source and the thesis file, wrote the structure parser, lifted the 14 datasets and wrote a second, independent parser to match them cell by cell, wrote the chart, network, export-geometry, SWMM5 export and checks code, compiled EPA SWMM 5.2.4 and ran every export variant, and designed the page and wrote the Doc. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.1.0 (2026-10-22): unit-equivalent SI export; slopes kept in the export; whole time-area distribution; cell-level provenance; calibration kept apart from validation; reading improvements (the version read).
- 2.0: single-file edition. 1: the Lovable MD Insight Explorer.
