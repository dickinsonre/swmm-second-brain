---
title: "Visual SWMM (app)"
type: entity
updated: 2026-11-19
sources: [S205, S207, S384]
tags: [apps, xpswmm, history, file-formats, wasm]
reviewed: no
---
Bob's app Visual SWMM: a browser reader for XP-SWMM .xp model files: a 140 KB WebAssembly module written in C from the 1999 XP engine reader and field dictionary draws the network and shows every card as named fields; it does not solve. The name is a working title, reused from Bob's later CAiCE product. Version 0.1.1, 2026-11-19 [S384](../sources/S384-visual-swmm-summary-v0-1-1.md); version 0.1.0 of 14 November 2026 is summarized in [S207](../sources/S207-visual-swmm-summary.md). Netlify address: https://visual-swmm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S207](../sources/S207-visual-swmm-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108). The summary of 0.1.1 [S384](../sources/S384-visual-swmm-summary-v0-1-1.md) is the same text with Claude's patch notes added.

**What the summary says** [S207](../sources/S207-visual-swmm-summary.md)
- A .xp record is 105 columns: group (columns 1 to 4: EXTR, RUNF, TRAN, Z...), instance (5 to 8), card name (9 to 12), sequence (13 to 16), object index (17 to 20), then the old 80-column SWMM card in 26 to 105. Dictionary column n is record column n + 25.
- Sources used: LMAIN.FOR (xpsoft/NEWDEC, December 1999), the engine's own three-pass read; Swmfield.c (WPACODE, December 1999), 1,489 fields; SWMM.R, plain-English labels for 627 fields and choice lists for 146.
- The reader is about 340 lines of C plus a generated table of 1,489 rows.
- 25 sample .xp files read without error: 51,144 records, 30,612 (60 %) on cards the dictionary decodes; XP-SWMM versions 1.05 to 20.1.
- Against XP-SWMM's own .xpx exports for eleven models, 18,219 of 18,296 input fields are equal (99.6 %); five models agree on every field. The page puts the differences down to the two files being saved at different times.
- Complexity about 5 on the scale where HydroCouple is 100, an AI estimate; the app has not been run through the meter.

**What it does not show.** It does not run a model: the 208-file XP-SWMM Fortran engine reads a .DAT card file the XP interface writes at Solve time, and neither that export code nor the engine is in this version. Cards added after December 1999 show as raw records, and in files from version 18 on these hold real model data such as 2D grids. Checked on 25 of more than 1,300 archive files. The .xpx it writes has not been loaded back into XP-SWMM. No person has reviewed the reader line by line. [S207](../sources/S207-visual-swmm-summary.md)

**Noted at ingest.** The per-model counts add up: 122 + 111 + 884 + 260 + 440 + 15,847 + 206 + 91 + 238 + 58 + 39 = 18,296 fields, and the equal fields sum to 18,219. 30,612 / 51,144 = 59.9 %; 627 / 1,489 = 42 %. Bob designed the .xp and .xpx formats at XP Software, as the page says; see [Robert (Bob) Dickinson](robert-dickinson.md) and [XPX to Shapefile Converter (app)](xpx-to-shapefile-converter.md).

**Version 0.1.1.** At phone width the one-column grid kept its automatic minimum, so the Verify table pushed the page to 484 px on a 390 px screen. One CSS line in the 900 px media rule changed, `.grid,.grid.even{grid-template-columns:1fr}` to `minmax(0,1fr)`, and every view now fits at 390 px. Nothing was rerun against the .xpx exports [S384](../sources/S384-visual-swmm-summary-v0-1-1.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [XPX to Shapefile Converter (app)](xpx-to-shapefile-converter.md), [Robert (Bob) Dickinson](robert-dickinson.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md).
