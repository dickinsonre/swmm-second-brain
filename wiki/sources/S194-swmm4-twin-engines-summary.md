---
title: "S194: SWMM 4 Twin Engines, summary written from the page (version of 2026-10-22)"
type: source
raw: raw/apps/swmm4-twin-engines-v2026-10-22.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-17
tags: [apps, swmm4, transport, storage, wasm, conversion, findings]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM 4 Twin Engines: the SWMM 4.4 Runoff and Transport blocks compiled to WebAssembly twice, as shipped and with a Transport fix from Bob's review, with a SWMM 5 to SWMM 4 converter. Raw file: [raw/apps/swmm4-twin-engines-v2026-10-22.md](../../raw/apps/swmm4-twin-engines-v2026-10-22.md).

**How it was written. A summary written from the page.** The page ships no technical summary and no version number. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1792688068-8a1d) and its About and Doc tabs. No deck was run. Bob has not read it (Q99). The page says Claude wrote everything on it at Bob's direction; Bob set the goal, supplied the swmm44gu source and the Transport patch from his review, and chose what to compare.

**Claims worth keeping** (all copied from the page)
- Source: swmm44gu, CDM / Oregon State, 20 February 2001. 157 Fortran files through f2c 20200916 after mechanical rewrites of DEC extensions; Emscripten 3.1.6 / clang 15; 132 COMMON blocks defined in commons.c; 13 BLOCK DATA units kept. Each engine is one 1.98 MB JavaScript file with the wasm inlined, a fresh instance per run.
- The fix: in the original Transport, the surcharge logic that caps a manhole's outflow at the downstream pipe capacity reads a storage unit's capacity from the wrong register, QO1 instead of QO2. The patch touches four files.
- Parity: the continuity error the engine prints is identical under gfortran, f2c + gcc and f2c + Emscripten: stor2 original 56.180 %, stor2 patched 0.003 %, barrel3 -0.093 %, infil 0.000 %, rt1 -0.152 %. The Runoff interface file from the wasm engine is byte-identical to the native f2c build on the chain deck.
- stor2: a triangular inflow peaking at 50 cfs into a 60,000 sq ft pond with a rating table releasing up to 70 cfs, drained by a 2 ft pipe at 0.2 percent that runs full at 10.117 cfs. The original engine puts 50 to 60 cfs through that pipe for most of seven hours; the patched engine caps the pond outflow at the pipe capacity and holds the rest. The pond's rating-table outflow is identical in both.
- Reconstructed Example 1: 2.05 in of rain on 71 ac, 0.85 in to the inlets; inlet 15 peaks at 6.6 cfs at the fourth hour; link 16 at 22.8 cfs; continuity -0.158 % (Runoff) and -0.096 % (Transport).
- rt1: Transport reported 57,370 ft3 of wet-weather inflow against 57,276 ft3 from Runoff, 0.16 percent apart.
- Pumped-storage model from the pyswmm tests: the patched engine's first record is the initialized 9 cfs where the original wrote 0; after that both carry the pipe's capacity, 8.02 cfs.
- Converter: a SWMM 5 subcatchment becomes one H1 line; Horton decay changes from per hour to per second; rain gages become E3 hyetographs resampled onto the finest gage interval. Run on four SWMM 5 files, each giving a deck both engines accepted.

**Limits it states.** The converter carries flow only: no quality, groundwater, LID, snow, controls, patterns or RDII. Transport is kinematic wave: no backwater, surcharge heads or reverse flow; an adverse slope becomes the minimum slope. Example 1 is "reconstructed from memory of the published file, not read from it", so its geometry is "Example 1 shaped". The 2004 WCH source was not built. A small continuity error is not a correct answer.

**Checked at ingest.** (57,370 - 57,276) / 57,276 = 0.164 percent. The patch and the review it came from are Bob's; the review itself is not in `raw/`.

**Feeds:** [SWMM 4 Twin Engines (app)](../entities/swmm4-twin-engines.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Block architecture and interface files](../concepts/block-architecture.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [The SWMM findings register](../concepts/findings-register.md).
