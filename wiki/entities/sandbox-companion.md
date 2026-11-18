---
title: "Sandbox Companion (app)"
type: entity
updated: 2026-11-17
sources: [S205, S260]
tags: [apps, swmm6, flooding, 2d, ports, licensing]
reviewed: no
---
Bob's app Sandbox Companion: one HTML file that carries three parts of Pablo Martinez Rodriguez's UK Flood Sandbox (Northumbria University, Apache-2.0, commit d0b4379) into a browser: a replay of his shipped Jesmond Vale run of the Newcastle upon Tyne thunderstorm of 28 June 2012, his .inp import checks, and his hazard and damage arithmetic, translated from Python. No engine runs; the replay is a run OpenSWMM 6.0.0a4 made on his computer. Version 1.0, 2026-11-08 [S260](../sources/S260-sandbox-companion-summary.md). Netlify address: https://sandbox-companion.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S260](../sources/S260-sandbox-companion-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S260](../sources/S260-sandbox-companion-summary.md)
- 17 of his 17 .inp tests pass against the translation, in Node and in the browser; the coordinate transform agrees with pyproj to under 0.4 in (1 cm; our conversion).
- The hazard, damage and road numbers equal an independent NumPy/SciPy/Shapely version exactly. Hazard rating HR = d (v + 0.5) + DF (Defra/EA FD2320); damage by the JRC global depth-damage functions (Huizinga, de Moel and Szewczyk 2017).
- His run, recomputed: 1.78 in (45.1 mm) in 150 minutes; outflow peak about 744 cfs (21.07 m3/s) at 85 minutes; deepest water 8.9 ft (2.72 m); about 13.7 ac (5.54 ha) deeper than 4 in; 82 of 563 buildings with more than 1 ft of water beside them; JRC damage about 12.6 million euros at 2010 prices, which he calls indicative.
- Flooded area recomputed at 5.54 ha against his reported 5.79 ha; his figures fall inside the bracket his 2 cm depth rounding allows.
- His importer over the 1729 corpus: 4,540 files, 10 skipped, 4,530 run with no exceptions. It would stop 3,451 on US flow units alone (E_US_UNITS); of the 1,079 not stopped by units, 465 would import after his offered repairs. Five files would stop his Python with an exception (names with spaces in the coordinates section).

**What it does not show.** No engine runs, so no new scenarios. The replay is his run as shipped; his Python could not be run in the build session, so the run was not reproduced. GIS import, estuaries, tides and IFC buildings were not translated. No person has read the translation line by line, and Pablo has not seen it. [S260](../sources/S260-sandbox-companion-summary.md)

**Noted at ingest.** 4,540 - 3,451 - 10 = 1,079 files. 5.54 ha is 13.7 ac and 5.79 ha 14.3 ac (our conversion). The two flooded-area figures differ by 4.3 %; the page explains the gap by his rounding.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md), [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
