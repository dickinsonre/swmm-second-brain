---
name: SWMM6 Code House
file: swmm6-code-house.html
version: 1.2.1
date: 2026-11-11
author: Robert Dickinson
links: {netlify: "https://swmm6-code-house.netlify.app/", artifact: "https://claude.ai/artifact/Wue2DHwu7HTv2fHKeTHy8E", repo: none}
engines:
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 9648837fc23b88485196cb98dde1f070c70c5ca0, license: Apache-2.0, use: "source text shown, not compiled, not run"}
units: US customary on screen. The Results tab can show a file's own units, US or SI.
ai_use: built with Claude (Anthropic). See AI use.
---

# SWMM6 Code House: a walkable 3D map of the OpenSWMM 6 engine source

## What it does
It puts every line of the OpenSWMM engine source on the walls of a 3D house: 102 rooms on 9 floors, 351,187 lines, 675 files, 6,683 functions, 427 doorways. A reader walks it as Froude, a water drop, or uses the Read tab with no 3D. Each room has a diagram and a ? that explains the code. A Results tab opens SWMM binary .out files. It is a reading aid. It is not an OpenSWMM release, it holds no compiled engine, and it does not run a model.

## How it computes
- **Census.** `tools/analyze.js` reads the C++ as text. No compiler is used. It resolved 26,223 calls by name and left 19,900 ambiguous, which are counted and not drawn.
- **Rooms.** `tools/rooms.js` assigns each file to exactly one room and throws if any file is in none or two.
- **Diagrams.** 24 rooms have hand-made diagrams, each labeled Port (a JavaScript copy of the C++) or Picture. The rest show a map of the room's files and longest functions.
- **The ? on code.** Names on a line are looked up in the source's own comments and declarations. 85.5% of field uses in .cpp files resolve. The rest say "Field meaning unresolved for this object."
- **Results reader.** Parses the SWMM .out layout (magic 516114522). Version field 60000 reads as OpenSWMM, 5xxxx as EPA SWMM 5. Node type codes are read by version: OpenSWMM stores DIVIDER=2, STORAGE=3 (`plugins/DefaultOutputPlugin.cpp:451`), SWMM 5 the reverse.
- **Doors to the SWMM5 Code House.** `tools/twin.js` matches SWMM 5.2.4 function names in the OpenSWMM text. It found 454 of 962 SWMM 5 functions named at 1,266 places in 119 files. 147 places are OpenSWMM functions with the same name. Only names with an underscore (7 or more characters), or same-name definitions of 10 or more characters, are counted.
- **Froude's Hunt.** 9 clues. An answer is right when the open function's name and file match `tools/hunt.json`. The build stops if an answer is not on the walls.
- **Follow a run.** 3 paths written from reading the source: Life of a run, One timestep, A raindrop's trip. Nothing is executing.

## Inputs and outputs
- Reads: a SWMM binary `.out` (SWMM 5 or OpenSWMM), an optional `.inp` for names, options and pollutant rows, an optional second `.out` to compare.
- Writes: CSV exports (rooms, doors, connections, functions, reading notes, where SWMM 5 went, a result series, the hunt record), a PNG postcard (1200 by 627), GIF and video of the house.
- Nothing is uploaded. Files are read in the browser.

## Checks
Mechanical checks, run by `node test/run_all.js` on the delivered standalone file in headless Chromium with software graphics:
- `test/census.js`: 18 checks
- `test/results.js`: 94 checks
- `test/page.js`: 51 checks
- `test/media.js`: 19 checks
- `test/diagrams.js`: 10 checks
- `test/explain.js`: 4 checks
- `test/hosted.js`: 4 checks
- `test/package_check.js`: 24 checks
- `test/netlify.js`: 15 checks
- `test/real_files.js`: 88 checks
- `test/extras.js`: 49 checks

What they cover:
- Wall text equals the source for all 675 files. NOTICE and LICENSE are byte-for-byte.
- Every room's diagram draws, every control moves, every ? explains.
- Real result files from the OpenSWMM test data: `site_drainage_model.out` (360 reports, written by 6.0.0-alpha.3), `baseline.out` (written by 6.0.0-alpha.1), `legacy_site_drainage.out` (EPA SWMM 5.3.0). A separate Python reader (`tools/fixture_expect.py`) gives the expected values.
- Every door's quoted line really names that SWMM 5 function, and every door address has the form the other house opens.
- Hunt, postcard, exports, themes, contrast, phone width, Netlify zip over local http.

Human review: none yet.

## What this does not show
1. OpenSWMM was not compiled or run. Nothing shows the diagrams match the engine or that OpenSWMM matches SWMM 5.
2. The 24 hand-made diagrams were written by AI from the C++ and not checked by a person.
3. The real result files came from alpha.1 and alpha.3, not the alpha.4 source on the walls.
4. A door is a name match. It does not show the logic is the same on both sides.
5. The 20 reading notes are source-reading hypotheses, except the node type code, which was seen in a real file.
6. No learner has been observed. No real phone or screen reader was tried. Nobody has listened to the sound.
7. No speed claim is made.

## How to reproduce
```
npm install            # Playwright and Chromium
node tools/build.js    # rebuilds dist/ from src6/ and data/
node test/run_all.js   # the whole suite
node tools/twin.js ../house .   # door census. Needs the SWMM5 Code House project beside this one
```

## Credits and licenses
- OpenSWMM Engine: Copyright 2026 HydroCouple Developers, Apache License 2.0. Lead developer Caleb Buahin. Developer and documentation Corinne Wiesner-Friedman.
- Source read here: fork SWMMBobSWMM6/openswmm.engine, branch swmm6_rel, commit 9648837. Text unchanged, headers intact.
- EPA SWMM lineage: public domain (17 USC 105). USEPA and HydroCouple do not endorse this app.
- three.js r128 (MIT) draws the 3D scene.
- The house, page, tools and tests: Copyright 2026 Robert Dickinson.

Upstream NOTICE, reproduced verbatim:

```
OpenSWMM Engine
Copyright 2026 HydroCouple Developers

This product includes software developed by the OpenSWMM authors
(https://github.com/HydroCouple/openswmm.engine).

Licensed under the Apache License, Version 2.0. See the LICENSE file for the
full license text.

--------------------------------------------------------------------------------
PUBLIC DOMAIN MATERIAL
--------------------------------------------------------------------------------

Portions of this product are derived from the Storm Water Management Model
(SWMM) developed and released by the United States Environmental Protection
Agency (USEPA) over the course of several decades. That material was prepared
by or for the United States Government and resides in the public domain:
domestic copyright protection is not available for it under 17 USC § 105, and
no copyright is claimed over it by the OpenSWMM authors.

The Apache License, Version 2.0 applies to the original contributions of the
OpenSWMM authors. It does not extend copyright to, and places no restriction
on, the public domain material described above. Recipients retain all rights
they already hold in that material independently of this License.

Files derived in whole or in part from USEPA SWMM sources are, where
practical, marked as such in their file headers. The EPA SWMM 5.x sources are
available from https://www.epa.gov/water-research/storm-water-management-model-swmm.

The USEPA does not endorse this product, and the names "EPA", "USEPA", and
"SWMM" are used solely to describe the origin of the public domain material.

--------------------------------------------------------------------------------
THIRD-PARTY COMPONENTS
--------------------------------------------------------------------------------

This product depends on and, in some distribution formats, bundles third-party
libraries that are licensed separately by their respective copyright holders.
Dependencies are declared in vcpkg.json. Each such component remains subject to
its own license terms, which accompany the component in its own distribution.
```

## AI use
Claude (Anthropic) did the building: the census tools, the page, the essay, the diagrams and the tests, working in Claude Code sessions in November 2026. Versions up to 1.1.0 used model claude-opus-5-5, with three subagents drafting room diagrams. Versions 1.2.0 and 1.2.1 used model claude-fable-5-2. Bob Dickinson chose the project, set the standards and reviews the result. No person has checked the diagrams line by line against the C++, and the tests were written by the same AI.

## Changes
- `1.2.1 (2026-11-12)`: the one-sentence, one-paragraph and one-page summaries at the top of the Doc tab and the Word file, with questions near the top and their answers at the end. No change to the house or the checks.
- `1.2.0 (2026-11-11)`: doors to the SWMM5 Code House by function name, Froude's Hunt with a CSV record, postcards, A raindrop's trip, this file, version badge fixed in the raw HTML.
- `1.1.0 (2026-11-04)`: real OpenSWMM result files as tests and sample, pollutant rows behind a result, not applicable governs the display, reading notes carry a status, separate netlify and review zips.
- `1.0.1 (2026-11-04)`: drop-ready Netlify package, public links.
- `1.0.0 (2026-11-03)`: first release.
