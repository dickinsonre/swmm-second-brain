---
title: "S01: SWMM 1 Engine, technical summary (app .md, v3.6)"
type: source
raw: raw/apps/swmm1-runoff-engine.md
kind: app-md
author: Robert Dickinson
published: 2026-11-13
ingested: 2026-11-14
superseded_by: S73
tags: [swmm-history, swmm1, verification]
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with the SWMM 1 Engine app, version 3.6. Raw file: [raw/apps/swmm1-runoff-engine.md](../../raw/apps/swmm1-runoff-engine.md).

**How it was written.** By Claude (Anthropic) under Bob's direction, from the build's own test output. Its AI-use section says no person has yet read the newly typed cards against the page images, or reviewed the five repaired cards, the four Volume II decks, or the values read from the scans.

**Claims worth keeping**
- The October 1971 listing (EPA 11024 DOC 10/71, Volume IV, 248 pages) holds 65 program units and 12,200 cards in five blocks: Executive 389, Runoff 1,311, Transport 4,114, Storage 3,918, Receiving Water 2,468.
- The whole listing was typed back into Fortran, translated by f2c and compiled by Emscripten to a 328 KB WebAssembly module.
- Six runs printed in 1971 are scored. Estuary example: 52 stage values, largest difference 0.0041 ft. Baker Street, San Francisco: 88 of 95 flow and cost numbers identical to the printed digit. Wingohocking, Philadelphia: 51 of 51 subarea dry-weather flows to two decimals. Kingman Lake, Washington: 53 of 55 storage design numbers identical.
- Baker Street pollutant loads do not agree: BOD to the plant 70,998 lb printed against 2,164 lb computed. Making card `TRAN346` a CONTINUE in an experimental build gives 74,642 lb. The explanation fits the peak hours only.
- Fourteen faults in the listing as printed were found by running it, among them a double conversion of DT in Storage, a missing COMMON card in TRCHEK, and `WAREA(J)` left out of Runoff's continuity check at `HYDR137`.
- Three builds agree: WebAssembly and native f2c printouts are byte-identical over 21,804 printed numbers; GNU Fortran 13.3 differs by more than 0.1 % in 0 of 3,086 Runoff numbers and in up to 152 of 3,159 Receiving Water numbers.
- Complexity index 70.2 against HydroCouple = 100.

**Feeds:** [SWMM 1 (1971)](../entities/swmm-1.md), [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md), [Block architecture and interface files](../concepts/block-architecture.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Infiltration methods](../concepts/infiltration-methods.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md).
