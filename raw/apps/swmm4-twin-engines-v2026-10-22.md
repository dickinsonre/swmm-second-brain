---
name: SWMM 4 Twin Engines
file: swmm4-twin-engines.html
version: 2026-10-22
date: 2026-10-22
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/LTyJPoTrAbm4ukbfuD6gGy", repo: none named in the page}
engines:
  - {name: SWMM 4.4 Runoff and Transport (original), source: "swmm44gu source, CDM / Oregon State, 20 February 2001; f2c 20200916, Emscripten 3.1.6 / clang 15", license: not stated in the page}
  - {name: SWMM 4.4 Runoff and Transport (patched), source: "the same, with the four-file Transport patch from Bob's review", license: not stated in the page}
units: US customary (cfs, in, ac, ft3)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude wrote everything on it at Bob Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LTyJPoTrAbm4ukbfuD6gGy, version 1792688068-8a1d (index.html, 4,263,549 bytes, SHA-256 bcae4606c20b5f2b078dba6e2532f14ff9c23c7da776a1e136dd906f25527639), its About and Doc tabs read in headless Chromium on 2026-11-16. No deck was run to write this file."
---

# SWMM 4 Twin Engines: SWMM 4.4 Runoff and Transport in the browser, as shipped and with the Transport fix

## In three points
- **What:** SWMM 4.4 Runoff and Transport compiled to WebAssembly twice, as shipped and with the Transport fix from Bob's review, with a SWMM 5 to SWMM 4 converter.
- **So what:** On stor2 the original Transport prints a continuity error of 56.180 % and the patched one 0.003 %; the original puts 50 to 60 cfs through a pipe that runs full at 10.117 cfs.
- **Now what:** Use it to see what the fix changes on models with storage. The converter carries flow only, Transport is kinematic wave, and Example 1 is reconstructed, not read from the published file.

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is the date of the published version read. Every number below is copied from the page's About tab or its Doc essay. No deck was run to write this file.

## What it does

Two WebAssembly builds of the SWMM 4.4 engine from the swmm44gu source (CDM / Oregon State, 20 February 2001), Runoff and Transport blocks: the original, and one carrying the four-file Transport patch from Bob's review. It converts a SWMM 5 .inp to a SWMM 4 deck, runs both engines, and compares them. Tabs: Model, Convert, Run, Runoff, Links, Compare, About, Doc.

## How it computes

- Translation: 157 Fortran files through f2c 20200916 (-A -E -72) after mechanical rewrites of DEC extensions; compiled with Emscripten 3.1.6 / clang 15 and linked with libf2c built for wasm32; 132 COMMON blocks defined in commons.c; 13 BLOCK DATA units kept. Each engine is one 1.98 MB JavaScript file with the wasm inlined. A fresh instance is created for every run.
- Rewrites listed: tabs to spaces and a final newline; SELECT CASE to IF/ELSE IF (13 files); EXIT/CYCLE to GO TO; labels in columns 1-4 re-laid out; DATA before declarations moved; TRIM(ADJUSTL()) to formatted WRITE, ADJUSTR() dropped; whole-array SUMWAT = 0 to a DO loop.
- Converter: a SWMM 5 subcatchment with its SUBAREAS and INFILTRATION rows becomes one H1 line; Horton decay changes from per hour to per second; rain gages become E3 hyetographs resampled onto the finest gage interval. Transport is a kinematic-wave router.
- The fix: in the original Transport, the surcharge logic that caps a manhole's outflow at the downstream pipe capacity reads a storage unit's capacity from the wrong register, QO1 instead of QO2.

## Results the page reports

- Parity, continuity error printed by the engine on the same deck under three builds (gfortran, f2c + gcc, f2c + Emscripten wasm), identical in all three: stor2 original 56.180 %; stor2 patched 0.003 %; barrel3 -0.093 %; infil 0.000 %; rt1 (Runoff to Transport) -0.152 %. The Runoff interface file from the wasm engine is byte-identical to the native f2c build on the chain deck.
- stor2: a manhole receives a triangular inflow peaking at 50 cfs into a 60,000 sq ft pond with a rating table releasing up to 70 cfs, drained by a 2 ft pipe at 0.2 percent that runs full at 10.117 cfs. The original engine puts 50 to 60 cfs through that pipe for most of seven hours; the patched engine caps the pond outflow at the pipe capacity and holds the rest. The pond's own outflow from the rating table is identical in both runs.
- Reconstructed Example 1: Runoff puts 2.05 inches of rain on 71 acres and sends 0.85 inches to the inlets; inlet 15 peaks at 6.6 cfs at the fourth hour; link 16 peaks at 22.8 cfs; Runoff continuity -0.158 percent and Transport -0.096 percent.
- rt1: inlet peaks 11.8 and 9.1 cfs; pipe 101 peaks at 7.1 cfs and pipe 201 at 13.2 cfs; Transport reported 57,370 ft3 of wet-weather inflow against 57,276 ft3 from Runoff, a 0.16 percent difference.
- Pumped-storage model from the pyswmm tests: the patched engine's first record is the initialized 9 cfs where the original wrote 0; after that both carry the pipe's capacity, 8.02 cfs.

## Checks (as stated on the page)

The parity ladder above; the Runoff interface file compared byte for byte; the interface parser checked against the engine's own printed peak table on Example 1; the converter run on four SWMM 5 files (the reconstructed Example 1, the pyswmm Green-Ampt example, the pyswmm full-features model with a pumped storage and a weir, and a node-inflow model with no subcatchments), each producing a deck both engines accepted without an error line. The only differences in the listings across builds are the spelling of infinity and the last digit of an iteration diagnostic in a run that had already failed to converge.

## What this does not show

- The converter carries flow only: no quality, groundwater, LID, snow, controls, patterns or RDII. The log names every dropped object.
- Transport is a kinematic-wave router: no backwater, surcharge heads or reverse flow, and an adverse slope becomes the minimum slope. Orifices and weirs not at a storage node become direct connections.
- Example 1 on the page is reconstructed from memory of the published file, not read from it. Its results are real; its geometry is "Example 1 shaped".
- The patched engine carries the four-file patch from the review and nothing else. The 2004 WCH source was not built.
- Agreement between the engines on a model with no storage unit is expected and says nothing about models with one. A small continuity error is not a correct answer.

## How to reproduce

Open the page, drop a SWMM 5 .inp on the Model tab or pick an example (the page says rt1 is among them), or paste a SWMM 4 deck; convert, then run both engines.

## Credits and licenses

The engines are the work of Wayne C. Huber, Robert E. Dickinson, Chuck Moore and the CDM and Oregon State authors named in the source. f2c is by S. I. Feldman, D. M. Gay, M. W. Maimone and N. L. Schryer (AT&T Bell Laboratories); libf2c under its permissive notice. Emscripten is MIT/NCSA licensed.

## AI use

The page says Claude (Anthropic) wrote everything on it at Bob Dickinson's direction: the Fortran-to-C preprocessing, the f2c and Emscripten build, the COMMON-block definitions, the libf2c signature patch, the SWMM 5 to SWMM 4 converter, the interface-file parser, the worker, the charts, the Doc essay and the .docx. Bob set the goal, provided the swmm44gu source and the Transport patch from his review, and chose what to compare. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 2026-10-22: the version read. The page carries no change log.
