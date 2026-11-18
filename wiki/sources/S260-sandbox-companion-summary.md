---
title: "S260: Sandbox Companion, summary written from the page (v1.0)"
type: source
raw: raw/apps/sandbox-companion-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-08
ingested: 2026-11-17
tags: [apps, swmm6, flooding, 2d, ports, licensing]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Sandbox Companion, version 1.0: one HTML file that carries three parts of Pablo Martinez Rodriguez's UK Flood Sandbox (Northumbria University, Apache-2.0, commit d0b4379) into a browser: a replay of his shipped Jesmond Vale run of the Newcastle upon Tyne thunderstorm of 28 June 2012, his .inp import checks, and his hazard and damage arithmetic, translated from Python. No engine runs; the replay is a run OpenSWMM 6.0.0a4 made on his computer. Raw file: [raw/apps/sandbox-companion-v1.0.md](../../raw/apps/sandbox-companion-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1794193013-6b10, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app was built with Claude in a session on 8 November 2026 at Bob's request, answering his question whether an HTML app can use Pablo Martinez's Apache-licensed code. Claude translated the parts listed, wrote a NumPy reference and ran the corpus sweep. Each translated file carries an Apache 4(b) modification notice. The page notes that Pablo's own AI_USAGE.md says Claude drafted most of his app.

**Claims worth keeping** (all copied from the file)
- 17 of his 17 .inp tests pass against the translation, in Node and in the browser; the coordinate transform agrees with pyproj to under 0.4 in (1 cm; our conversion).
- The hazard, damage and road numbers equal an independent NumPy/SciPy/Shapely version exactly. Hazard rating HR = d (v + 0.5) + DF (Defra/EA FD2320); damage by the JRC global depth-damage functions (Huizinga, de Moel and Szewczyk 2017).
- His run, recomputed: 1.78 in (45.1 mm) in 150 minutes; outflow peak about 744 cfs (21.07 m3/s) at 85 minutes; deepest water 8.9 ft (2.72 m); about 13.7 ac (5.54 ha) deeper than 4 in; 82 of 563 buildings with more than 1 ft of water beside them; JRC damage about 12.6 million euros at 2010 prices, which he calls indicative.
- Flooded area recomputed at 5.54 ha against his reported 5.79 ha; his figures fall inside the bracket his 2 cm depth rounding allows.
- His importer over the 1729 corpus: 4,540 files, 10 skipped, 4,530 run with no exceptions. It would stop 3,451 on US flow units alone (E_US_UNITS); of the 1,079 not stopped by units, 465 would import after his offered repairs. Five files would stop his Python with an exception (names with spaces in the coordinates section).

**Limits it states.** No engine runs, so no new scenarios. The replay is his run as shipped; his Python could not be run in the build session, so the run was not reproduced. GIS import, estuaries, tides and IFC buildings were not translated. No person has read the translation line by line, and Pablo has not seen it.

**Checked at ingest.** 4,540 - 3,451 - 10 = 1,079 files. 5.54 ha is 13.7 ac and 5.79 ha 14.3 ac (our conversion). The two flooded-area figures differ by 4.3 %; the page explains the gap by his rounding. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://sandbox-companion.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Sandbox Companion (app)](../entities/sandbox-companion.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
