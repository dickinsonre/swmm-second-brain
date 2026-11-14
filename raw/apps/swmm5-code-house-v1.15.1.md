---
name: SWMM5 Code House
file: swmm5-code-house.html
version: 1.15.1
date: 2026-11-11
author: Robert Dickinson
links: {netlify: "https://swmm5-code-house.netlify.app/", artifact: "https://claude.ai/artifact/1sy1Vcs2qgFuUcvZCTvDLW", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4, commit 7952ca837988b1c32f791812eccc9fd64547e093", license: public domain, use: "source text shown, and a WebAssembly build runs in the page"}
units: US customary. A model in SI flow units shows its own units.
ai_use: built with Claude (Anthropic). See AI use.
---

# SWMM5 Code House: a walkable 3D map of the EPA SWMM 5.2.4 source, with the engine running inside

## What it does
It puts the EPA SWMM 5.2.4 solver source on the walls of a 3D house: 58 rooms on 5 floors, 51,080 lines, 54 files, 969 functions, 160 doorways. A reader walks it as Froude, a water drop, or uses the Read tab with no 3D. Each room has an interactive diagram and a ? that explains the code. The Engine tab runs a real SWMM 5.2.4 engine in the browser on a sample or on the reader's own .inp, and "Explain this result" ties a result to the routines and input rows behind it.

## How it computes
- **Engine.** `ext2/engine.js` (SHA-256 `4602e507bb5c372c5b80952e585eb13f61137251b87fdddf2ff56f2d2eb8a45f`) with `ext2/swmm524.wasm` (SHA-256 `e371a84962a38b760a5ef76eebe993bd961fe9a97537a04e89db2e277239efa7`). Built from USEPA commit 7952ca8, `src/solver` and `src/run`, with Emscripten 3.1.51, system LLVM 18, Binaryen 116, `-O2 -D_FORTIFY_SOURCE=0`, single-file, single-threaded, per the build record in Seven SWMM Engines v1.2. The build was not repeated here.
- **Census.** A text parser finds functions, calls, includes and struct fields. Doors between rooms come from call sites, includes and shared keyword data.
- **Diagrams.** Each is a JavaScript transcription of the C in its room. Rows in the Front Hall's verification panel compare a transcription with the engine, with inputs, tolerance and observed difference.
- **The ? on code.** Names on a line are looked up in the source's own comments and declarations. 8,745 of 8,745 struct field uses resolve to their owner.
- **Reported values.** The app states which results are interpolated between routing states, which are computed from interpolated values (conduit velocity, `link.c: link_getVelocity`), and which are averages when `[REPORT] AVERAGES YES`.
- **Doors to the SWMM6 Code House.** `tools/twin.js` matches SWMM 5 function names in the OpenSWMM 6.0.0-alpha.4 text (commit 9648837). 454 of 962 functions are named there, at 1,266 places. 147 places are OpenSWMM functions with the same name.
- **Froude's Hunt.** 9 clues. An answer is right when the open function's name and file match `tools/hunt.json`. The build stops if an answer is not on the walls.
- **Follow a run.** Three paths, each checked to follow call-site order in the source (`test/structure.js`): Life of a run, One routing step, A raindrop's trip.

## Inputs and outputs
- Reads: a SWMM 5 `.inp` pasted or loaded in the Engine tab. Outside files (rain, climate, hot start) cannot be attached there.
- Writes: the run's `.rpt` and `.out`, an evidence ZIP with a manifest and hashes, CSV exports (series, rooms, doors, functions, lesson record, hunt record), a PNG postcard (1200 by 627), GIF and video.
- Nothing is uploaded. The engine runs in the browser.

## Checks
Mechanical checks, run by `node test/run_all.js` on the delivered standalone file:
- `test/structure.js`: Doors, includes, walk order
- `test/models_rerun.js`: Every saved model, from its own folder
- `test/checks.js`: Engine checks
- `test/verify.js`: Verification claims
- `test/evidence_check.js`: Deliberate failures
- `test/contrast.js`: Contrast in every theme
- `test/walk.js`: Walking the house
- `test/diagram_q.js`: Every diagram has a ?
- `test/explain.js`: Explain panels
- `test/review.js`: First review fixes
- `test/engine_ui.js`: Every run button
- `test/themes.js`: Themes change only color
- `test/voice.js`: Voice
- `test/act.js`: Keyboard activation
- `test/round3.js`: Second review fixes (SKIPM=1 skips GIF and video)
- `test/round4.js`: Third review fixes
- `test/round5.js`: Fourth review fixes
- `test/round6.js`: Fifth review fixes
- `test/round7.js`: Sixth review fixes
- `test/round8.js`: Seventh review fixes
- `test/round9.js`: Eighth review fixes
- `test/round10.js`: Ninth review fixes
- `test/round11.js`: Tenth review fixes
- `test/extras.js`: Doors to the other house, hunt, postcard, summary
- `test/native_compare.js`: WebAssembly against stored native 5.2.4 outputs
- `test/package_check.js`: Repackage and rebuild from a clean extraction
- `test/netlify.js`: The Netlify zip over http
- `test/engine_sweep.js`: Slider sweep

Numbers from this build's data files:
- 59 engine checks and 97 verification rows are required, and a check passes only with its required runs, usable finite values and a result inside its limit.
- 344 of 344 deliberately forced engine failures gave a failed check, a failed command and a named model.
- WebAssembly against stored native EPA SWMM 5.2.4 `runswmm.exe` output, 78 models from SWMMBobSWMM6/1729-SWMM5-Models-2030: 78 ran, 78 inside the limits, 801,567 of 805,991 stored values exactly equal, 75 models identical to the last stored digit. Largest gap 2.4% of one series' range. Limits (3% of range, 0.003 percentage point on continuity) were set after the first comparison.

Human review: ten rounds of outside written reviews were applied. Bob Dickinson has not yet reviewed this build, and no person has read the diagrams against the C line by line.

## What this does not show
1. The engine build was not repeated, and the build record lacks the full command line.
2. The native reference files were read from the corpus, not rerun. The native program has no recorded hash.
3. The native comparison covers small models with no outside files. Three models differ, and why was not traced.
4. A door to the SWMM6 house is a name match. It does not show the logic is the same.
5. Lessons, annotations and model answers still need human review. No learner has been observed.
6. No real phone or screen reader was tried. Nobody has listened to the sound.

## How to reproduce
```
npm install                      # Playwright and Chromium
node tools/build.js              # rebuilds dist/ from epa/, ext2/ and data/
node test/run_all.js             # the whole suite
node test/native_compare.js      # WebAssembly against the stored native outputs in test/native/
```
See `review/engine-provenance-1.14.0.md` for the engine chain.

## Credits and licenses
- EPA SWMM 5.2.4: USEPA, public domain. Lewis Rossman is its principal developer. USEPA does not endorse this app.
- WebAssembly engine: from Bob Dickinson's Seven SWMM Engines app.
- three.js r128 (MIT) draws the 3D scene.
- The house, page, tools and tests: Copyright 2026 Robert Dickinson.

## AI use
Claude (Anthropic) did the building in Claude Code sessions in November 2026: the parser, floor plan, 3D house, character, diagrams, JavaScript transcriptions of the C, test models, engine comparisons and tests. Versions up to 1.14.0 used model claude-opus-5-5. Versions 1.15.0 and 1.15.1 used model claude-fable-5-2. Bob Dickinson asked for the app, steers it through outside reviews and is responsible for the work. The source on the walls and the engine are EPA's, unchanged.

## Changes
- `1.15.1 (2026-11-12)`: the one-sentence, one-paragraph and one-page summaries at the top of the Doc tab and the Word file, with questions near the top and their answers at the end. No change to the house, the engine or the checks.
- `1.15.0 (2026-11-11)`: doors to the SWMM6 Code House by function name, Froude's Hunt with a CSV record, postcards, A raindrop's trip, this file, version badge fixed in the raw HTML, link toast fixed on the public site.
- `1.14.0 (2026-11-04)`: engine provenance and native comparison, pollutant rows behind a result, not applicable governs the display, conduit velocity label, separate netlify and review zips.
- `1.13.0 (2026-11-03)`: evidence gate, field owners, object-specific sources, peak-safe thinning.
