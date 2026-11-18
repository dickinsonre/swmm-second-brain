---
title: "S313: Flow Solver Forge, summary written from the page (v1.0)"
type: source
raw: raw/apps/flow-solver-forge-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm5, saint-venant, numerics, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Flow Solver Forge, version 1.0: build a 1D Saint-Venant solver from parts and run it beside EPA SWMM 5.2.4. Raw file: [raw/apps/flow-solver-forge-v1.0.md](../../raw/apps/flow-solver-forge-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Mc7WbGsQUDgK22ch7wJYUF, version 1792957817-5fb0 (index.html, 1,413,849 bytes, SHA-256 d4a052c22f9f6837537c9a8f9f3211a1cf160fbb01fca55a0102c5f81a3fc682), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in one Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export and chose to have the app designed from its name when the export proved empty; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A workbench for the engine inside a 1D sewer or channel model: one prismatic reach, one storm, and an unsteady flow solver you assemble from five switchable parts, compared with EPA SWMM 5.2.4 (compiled into the page) and with four problems whose answers are known exactly. The Lovable export of this name held only a blank template, so at Bob's direction the page was designed from the name.
- On a surcharging storm the native and wasm SWMM builds agree to the last printed digit (39.366 cfs); the JavaScript port gives 39.370 cfs, Nash-Sutcliffe 1.00000 against native SWMM, the same 2.07 iterations per step and the same -0.215% continuity error. Against exact answers, SWMM's link-node method fails Stoker's dam break (L1 depth error 0.942 ft, front -27.0%), and only Godunov HLL passes all four tests.
- The link-node part checked three ways against EPA SWMM 5.2.4: the EPA source built natively with gcc, the same source built to WebAssembly, and the JavaScript port, run by run (numbers above).
- Every scheme scored against the four exact answers; a grid-refinement study run. All Verify numbers come from those runs.

**Limits it states.** As the page lists it: one reach, no network; no junction losses, no manhole storage beyond SWMM's minimum surface area, no pumps, weirs or orifices, no rainfall-runoff; wet-dry fronts not handled (every run keeps a small base flow); the Preissmann box uses equal space weighting (ψ = 0.5) only. These are limits of the page, not of the methods. No person has yet reviewed the solver code line by line.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Flow Solver Forge (app)](../entities/flow-solver-forge.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
