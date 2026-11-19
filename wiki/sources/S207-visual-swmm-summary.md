---
title: "S207: Visual SWMM, summary written from the page (v0.1.0)"
type: source
raw: raw/apps/visual-swmm-v0.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-17
superseded_by: S384
tags: [apps, xpswmm, history, file-formats, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Visual SWMM, version 0.1.0: a browser reader for XP-SWMM .xp model files: a 140 KB WebAssembly module written in C from the 1999 XP engine reader and field dictionary draws the network and shows every card as named fields; it does not solve. The name is a working title, reused from Bob's later CAiCE product. Raw file: [raw/apps/visual-swmm-v0.1.0.md](../../raw/apps/visual-swmm-v0.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1794659289-40b0, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says Claude (Claude Fable 5.2) built it in one session on 14 November 2026 at Bob's request and from his source archive: Claude read the Fortran and C, worked out the record layout and wrote the C reader, the page and the essay. The engine source, field dictionary, formats and sample models are Bob's and XP Software's; the AI wrote no hydraulics and changed none of the original source.

**Claims worth keeping** (all copied from the file)
- A .xp record is 105 columns: group (columns 1 to 4: EXTR, RUNF, TRAN, Z...), instance (5 to 8), card name (9 to 12), sequence (13 to 16), object index (17 to 20), then the old 80-column SWMM card in 26 to 105. Dictionary column n is record column n + 25.
- Sources used: LMAIN.FOR (xpsoft/NEWDEC, December 1999), the engine's own three-pass read; Swmfield.c (WPACODE, December 1999), 1,489 fields; SWMM.R, plain-English labels for 627 fields and choice lists for 146.
- The reader is about 340 lines of C plus a generated table of 1,489 rows.
- 25 sample .xp files read without error: 51,144 records, 30,612 (60 %) on cards the dictionary decodes; XP-SWMM versions 1.05 to 20.1.
- Against XP-SWMM's own .xpx exports for eleven models, 18,219 of 18,296 input fields are equal (99.6 %); five models agree on every field. The page puts the differences down to the two files being saved at different times.
- Complexity about 5 on the scale where HydroCouple is 100, an AI estimate; the app has not been run through the meter.

**Limits it states.** It does not run a model: the 208-file XP-SWMM Fortran engine reads a .DAT card file the XP interface writes at Solve time, and neither that export code nor the engine is in this version. Cards added after December 1999 show as raw records, and in files from version 18 on these hold real model data such as 2D grids. Checked on 25 of more than 1,300 archive files. The .xpx it writes has not been loaded back into XP-SWMM. No person has reviewed the reader line by line.

**Checked at ingest.** The per-model counts add up: 122 + 111 + 884 + 260 + 440 + 15,847 + 206 + 91 + 238 + 58 + 39 = 18,296 fields, and the equal fields sum to 18,219. 30,612 / 51,144 = 59.9 %; 627 / 1,489 = 42 %. Bob designed the .xp and .xpx formats at XP Software, as the page says; see [Robert (Bob) Dickinson](../entities/robert-dickinson.md) and [XPX to Shapefile Converter (app)](../entities/xpx-to-shapefile-converter.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://visual-swmm.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Visual SWMM (app)](../entities/visual-swmm.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [XPX to Shapefile Converter (app)](../entities/xpx-to-shapefile-converter.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md).
