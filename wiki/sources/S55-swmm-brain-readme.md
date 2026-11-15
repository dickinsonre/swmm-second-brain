---
title: "S55: README of the old swmm-brain repository (SWMM-Brain-Dickinson)"
type: source
raw: raw/swmm-brain/README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-08-22
ingested: 2026-11-14
tags: [swmm5, infiltration, hydraulics, wasm, career, repositories]
reviewed: 2026-11-15
---
**What it is.** The README of `dickinsonre/swmm-brain` at commit 70348bb of 22 August 2026: a description of engine enhancements, apps and scripts, with a career timeline. Raw file: [raw/swmm-brain/README.md](../../raw/swmm-brain/README.md).

**How it was written.** Not stated. It reads as AI-drafted with Bob's facts. It describes a folder tree headed `swmm5-dickinson/` (enhancements, apps, scripts, docs); none of those folders is in the repository, which holds six files. Its links into them lead nowhere.

**Claims worth keeping**
- A two-layer soil infiltration enhancement for SWMM 5: one new keyword `SOIL2`, one new flag `UseAsInfil`, about 39 lines touched in existing code, built on the LID soil layer and on `perc = Ksat × exp(-15.0 × (1.0 − θ/porosity))` from `lid_proc.c :: soilFluxRates()`.
- Five planned dynamic-wave fixes: Preissmann slot width, crown transition, supercritical flow, junction losses, pond and pipe coupling. Status: planned.
- It gives SWMM 5's current slot as a fixed width of about 1 % of the pipe diameter.
- SWMM 5 compiled to WebAssembly with Emscripten, exporting `swmm_run`, `swmm_open`, `swmm_start`, `swmm_step`, `swmm_end`. Status: in progress.
- SWMM 5 has more than 40 C source files.
- Bob coded the RTK/RDII implementation for SWMM 5 during the CRADA project.
- Timeline: 1974, first model run, on punch cards, SWMM 2; 1981, CDM publishes the Extran manual with 7 test files he still uses; 1988, SWMM 4 manual with Wayne Huber (EPA/600/3-88/001a); 2005 to 2023, "18 years at Innovyze"; 2023, chair of the SWMM5+ Technical Advisory Committee at CIMM.org; 2024, Autodesk Water.
- `innovyze/Open-Source-Support` holds 578 Ruby scripts and 139 SQL scripts.

**Feeds:** [Two-layer soil infiltration (SOIL2)](../concepts/two-layer-infiltration.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Infiltration methods](../concepts/infiltration-methods.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [EPA SWMM 5](../entities/swmm-5.md), [EXTRAN](../entities/extran.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [swmm-brain (the old brain repository)](../entities/swmm-brain-repo.md), [Bob's GitHub repositories (where the rest of the material lives)](../entities/bobs-github-repositories.md).
