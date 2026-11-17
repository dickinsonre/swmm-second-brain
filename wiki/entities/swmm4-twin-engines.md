---
title: SWMM 4 Twin Engines (app)
type: entity
updated: 2026-11-17
sources: [S194]
tags: [apps, swmm4, transport, storage, wasm]
reviewed: no
---
Bob's app that compiles the SWMM 4.4 Runoff and Transport blocks to WebAssembly twice, as shipped and with a Transport fix from his review, and runs a SWMM 5 model through both. Published 22 October 2026, with no version number of its own [S194](../sources/S194-swmm4-twin-engines-summary.md).

**A caution about its source.** The page ships no technical summary. [S194](../sources/S194-swmm4-twin-engines-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**The engines.** The swmm44gu source (CDM / Oregon State, 20 February 2001): 157 Fortran files through f2c, then Emscripten. Each engine is one 1.98 MB JavaScript file [S194](../sources/S194-swmm4-twin-engines-summary.md).

**The fix.** In the original Transport, the logic that caps a manhole's outflow at the downstream pipe's capacity reads a storage unit's capacity from the wrong register, QO1 instead of QO2 [S194](../sources/S194-swmm4-twin-engines-summary.md).

**What the fix changes** [S194](../sources/S194-swmm4-twin-engines-summary.md)

| Deck | Original | Patched |
|---|---|---|
| stor2, printed continuity error | 56.180 % | 0.003 % |
| stor2, flow in a 2 ft pipe that runs full at 10.117 cfs | 50 to 60 cfs for most of seven hours | capped at the pipe's capacity; the pond holds the rest |
| pumped storage (pyswmm tests), first record | 0 | the initialized 9 cfs |

On decks with no storage unit the two agree, which the page says "says nothing about models with one".

**Checks.** The printed continuity error is identical under gfortran, f2c + gcc and f2c + WebAssembly on five decks; the Runoff interface file is byte-identical between the wasm and native f2c builds [S194](../sources/S194-swmm4-twin-engines-summary.md).

**What it does not show.** The converter carries flow only. Transport is kinematic wave: no backwater, surcharge heads or reverse flow. Example 1 is reconstructed from memory, not read from the published file [S194](../sources/S194-swmm4-twin-engines-summary.md).

**Related.** [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [SWMM 3 Runoff & Transport (app)](swmm3-runoff-transport-app.md).
