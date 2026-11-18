---
name: Flow Solver Forge
file: flow-solver-forge.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Mc7WbGsQUDgK22ch7wJYUF", original: "Lovable project flow-solver-forge (its export held only the blank starter template)", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "the EPA source compiled natively with gcc and to wasm32-wasi; the wasm copy runs in the page through an in-page WASI host"}
  - {name: "five solvers written for the page", note: "SWMM 5.2.4's dwflow.c/dynwave.c link-node method ported to JavaScript, a Preissmann box, a diffusive Preissmann scheme, kinematic wave, Godunov HLL, MacCormack and Lax-Friedrichs"}
units: US customary (ft, s, cfs; g = 32.2 ft/s2; Manning constant 1.486)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Mc7WbGsQUDgK22ch7wJYUF, version 1792957817-5fb0 (index.html, 1,413,849 bytes, SHA-256 d4a052c22f9f6837537c9a8f9f3211a1cf160fbb01fca55a0102c5f81a3fc682), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Flow Solver Forge: build a 1D Saint-Venant solver from parts and run it beside EPA SWMM 5.2.4

## In three points
- **What:** A workbench for the engine inside a 1D sewer or channel model: one prismatic reach, one storm, and an unsteady flow solver you assemble from five switchable parts, compared with EPA SWMM 5.2.4 (compiled into the page) and with four problems whose answers are known exactly. The Lovable export of this name held only a blank template, so at Bob's direction the page was designed from the name.
- **So what:** On a surcharging storm the native and wasm SWMM builds agree to the last printed digit (39.366 cfs); the JavaScript port gives 39.370 cfs, Nash-Sutcliffe 1.00000 against native SWMM, the same 2.07 iterations per step and the same -0.215% continuity error. Against exact answers, SWMM's link-node method fails Stoker's dam break (L1 depth error 0.942 ft, front -27.0%), and only Godunov HLL passes all four tests.
- **Now what:** Use it to see why schemes differ and what an exact test can show that an engine comparison cannot. One reach, no network, no structures, no wet-dry fronts, and no person has reviewed the solver code line by line.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Forge, Run, Bench, Verify, About, Doc. The Verify suite runs live: lake at rest (pass if max |Q| after 1 h < 0.01 cfs), Manning normal depth (within 1%), Stoker's dam break at t = 40 s (L1 < 0.15 ft and front within 3%; rectangular channel 10 ft wide, flat, n = 0.0001 because SWMM rejects n = 0, 10 ft of water upstream of x = 1,000 ft and 1 ft downstream, 200 segments), and full-pipe friction slope (HGL slope within 2%), plus a grid-refinement study at 50 to 400 segments.

| Scheme | Lake at rest | Normal depth | Dam break | Full pipe |
|---|---|---|---|---|
| SWMM5 DYNWAVE default | pass | pass | fail | pass |
| SWMM5, slot, no damping (5 s) | pass | pass | fail | fail |
| Preissmann box θ 0.6 | pass | pass | cannot run | pass |
| Preissmann diffusive | pass | pass | cannot run | pass |
| Kinematic wave | outside theory | pass | outside theory | outside theory |
| Godunov HLL (MUSCL + RK2) | pass | pass | pass (L1 0.037 ft, front 1,712 ft against 1,712 ft) | pass |
| MacCormack | fail | pass | pass | pass |
| Lax-Friedrichs | fail | pass | fail | fail |

## Checks (as stated on the page)

- The link-node part checked three ways against EPA SWMM 5.2.4: the EPA source built natively with gcc, the same source built to WebAssembly, and the JavaScript port, run by run (numbers above).
- Every scheme scored against the four exact answers; a grid-refinement study run. All Verify numbers come from those runs.

## What this does not show

As the page lists it: one reach, no network; no junction losses, no manhole storage beyond SWMM's minimum surface area, no pumps, weirs or orifices, no rainfall-runoff; wet-dry fronts not handled (every run keeps a small base flow); the Preissmann box uses equal space weighting (ψ = 0.5) only. These are limits of the page, not of the methods. No person has yet reviewed the solver code line by line.

## Credits and licenses

EPA SWMM 5.2.4 source (public domain), src/solver/dwflow.c and dynwave.c; Stoker's dam-break solution; Preissmann, Godunov, MacCormack and Lax-Friedrichs schemes as published. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in one Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export and chose to have the app designed from its name when the export proved empty; responsibility is his. Claude designed the app, wrote all five solvers, ported SWMM 5.2.4's link-node method, compiled the EPA source natively and to wasm32-wasi, wrote the WASI host and .out reader, the tests, the defect register, the Doc essay, the .docx and the text. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first version (the version read).
