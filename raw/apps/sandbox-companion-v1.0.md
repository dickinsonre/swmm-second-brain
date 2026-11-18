---
name: Sandbox Companion
file: sandbox-companion.html
version: "1.0"
date: 2026-11-08
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/JHCJD3uEC3kzaw8fkTh5KD", repo: none named in the page}
engines:
  - {name: none in the page, note: "replays a run that OpenSWMM 6.0.0a4 produced on Pablo Martinez's computer; no OpenSWMM code is carried and no engine runs"}
ported_from: {name: UK Flood Sandbox, author: "Pablo Martinez Rodriguez, Northumbria University", commit: "d0b4379 (28 Oct 2026)", license: Apache-2.0}
units: US customary by default, SI on a switch (the source data are metric)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app was built with Claude at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/JHCJD3uEC3kzaw8fkTh5KD, version 1794193013-6b10 (index.html, 1,879,554 bytes, SHA-256 c04f6bf8c08587efa00ca1d7fde97e7aa885f78315bdfe162197aaf3a9234f8c), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Sandbox Companion: parts of Pablo Martinez's UK Flood Sandbox, ported to one browser file

## In three points
- **What:** One HTML file that carries three parts of UK Flood Sandbox (Apache-2.0) into a browser: a replay of his shipped Jesmond Vale run of 28 June 2012, his .inp import checks, and his hazard and damage arithmetic, translated from Python.
- **So what:** 17 of his 17 .inp tests pass against the translation, and the hazard, damage and road numbers equal an independent NumPy/SciPy/Shapely version exactly; his importer would stop 3,451 of the 4,540 corpus files on US flow units alone.
- **Now what:** Use it to see his method and test your .inp files against his checks. No engine runs here, so no new scenarios; the replay is his run as shipped, and nobody has read the translation line by line.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-11-08"). Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

It answers Bob's question of 8 November 2026: can an HTML app use Pablo Martinez's Apache-licensed code? The storm is Newcastle upon Tyne's thunderstorm of 28 June 2012 over Jesmond Vale. Tabs: Replay (his 48 saved depth grids, five minutes apart, with maximum depth and speed per cell), Import check (his drainage-import checks on any .inp, with a Jesmond Vale mode and a No-area mode), Hazard & damage (his arithmetic with the numbers substituted), Self-test (his 17 .inp tests run in the browser), About, Doc. A US/SI switch, CSV export and a GIF recorder.

## What was taken (as the page lists it)

- sewer.js from sewer.py: issue, read_inp, from_inp, Ground, place_crs (EPSG 27700, 4326, 3857 only), reproject, _components, analyse (the .inp path), _fill_inverts, cover_kind, check. Not taken: GIS import, the Irish grids, saving and model writing. Added: a No-area mode, and a marker where his Python would raise an exception.
- core.js from core.py: hazard rating and classes, _hazard_stats, _damage, _buildings_affected, _roads_and_sites, the area statistics of postprocess, and his colour ramps.
- testcases.js from tests/test_sewer.py. Each translated file carries an Apache 4(b) modification notice.
- Hazard rating: HR = d (v + 0.5) + DF, d in m, v in m/s capped at 10, DF = 1 when d > 0.25 m (Defra/EA FD2320). Damage: JRC global depth-damage functions (Huizinga, de Moel and Szewczyk 2017).

## Results the page reports (his shipped run, recomputed in the browser)

- Rain pattern: 1.78 in (45.1 mm) in 150 minutes, the first fifteen minutes at 3.37 in/h (85.7 mm/h); the Ouseburn climbs to about 604 cfs (17.1 m3/s) at the gauge.
- Mesh: 5 m (16.4 ft) grid split into triangles with buildings cut out; 73,688 triangles for the Jesmond Vale preset.
- Outflow at the valley bottom, computed by the engine in his run: peak about 744 cfs (21.07 m3/s) at 85 minutes.
- Deepest water 8.9 ft (2.72 m), on the Coast Road. About 13.7 ac (5.54 ha) deeper than 4 in (0.1 m). Of 563 buildings, 82 have more than 1 ft (0.3 m) of water beside them. JRC damage about 12.6 million euros at 2010 prices, which he calls indicative.

## Checks (as stated on the page)

- His tests: 17 of 17 .inp test cases pass, in Node and in the browser.
- Coordinate transform agrees with pyproj to under 1 cm.
- Hazard, damage and road numbers equal an independent NumPy/SciPy/Shapely version exactly.
- Flooded area: recomputed 5.54 ha against his reported 5.79 ha; his figures fall inside the bracket that his 2 cm depth rounding allows.
- Importer sweep over the 1729-SWMM5-Models-2030 corpus: 4,540 files, 10 skipped, 4,530 run with no JavaScript exceptions. Blocking errors: E_US_UNITS 3,451; E_NO_XY 1,250; E_OPEN_CHANNEL 289; E_SIZE_BIG 132; E_DUMMY 77; E_ABOVE 76; E_EMPTY 55; E_STRUCT_LEVEL 31; E_CURVE 28; E_DUP_NODE 20. Of the 1,079 files not stopped by units, 465 would import after his offered repairs. Five files would stop his Python with an exception (names with spaces in the coordinates section).
- The checks are mechanical.

## What this does not show

- No engine runs: no new scenarios, walls or basins, and no other area of the UK.
- The replay is his run as shipped; his Python could not be run in the build session, so the run was not reproduced.
- Depths are good to 2 cm; there are no per-frame speeds; hazard pairs peaks.
- GIS import (GeoPackage, shapefile, file geodatabase), estuaries, tides and IFC buildings were not translated.
- No person has read the translation line by line against sewer.py and core.py, and Pablo has not seen it.

## How to reproduce

Open the page. Self-test runs his 17 tests. Import check takes dropped .inp files. The data bundle was built by a separate preparation script that reads his repository's data files (areas/jesmond-vale/ and tests/data/jesmond_sewer.json) and runs none of his code; the script is not shipped in the page.

## Credits and licenses

UK Flood Sandbox by Pablo Martinez Rodriguez, Northumbria University, Apache-2.0, commit d0b4379; his NOTICE reproduced and the full license text in the About tab. OpenSWMM 6 by HydroCouple (Caleb Buahin and the OpenSWMM authors), Apache-2.0. Terrain from Environment Agency LIDAR and gauge records (Open Government Licence v3.0); buildings, roads and sites from OpenStreetMap (ODbL 1.0, which those data keep). The page: Copyright 2026 Robert Dickinson (SWMM Enablement), Apache-2.0, portions Copyright the UK Flood Sandbox authors; not an official release and not endorsed by its authors, Northumbria University, HydroCouple or the USEPA.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude session on 8 November 2026, at Bob Dickinson's request. Claude read the UK Flood Sandbox repository, translated the parts listed above, wrote the data-preparation script, the tests, the NumPy reference, the page, the essay and the .docx, and ran the corpus sweep. The page also notes that Pablo's own AI_USAGE.md says Claude drafted most of his app. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-11-08): first version.
