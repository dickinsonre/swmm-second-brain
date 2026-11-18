---
name: SWMM6 in Diagrams
file: swmm6-in-diagrams.html
version: "2026-11-14"
date: 2026-11-14
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NjBEcuK8pXMRPneYT6CaqH", repo: none named in the page}
engines:
  - {name: OpenSWMM, version: 6.0.0-alpha.4 (pip openswmm 6.0.0a4.dev1), note: "run on small test chains for diagrams 2 to 6, 9 and 10; the legacy engine in this build reports 5.3.0"}
  - {name: EPA SWMM, version: 5.2.4, note: "run on the same test chains"}
units: US customary (ft, cfs, ft2, s); SWMM6's DPS_CELERITY is given as 25 m/s (82 ft/s) as the boards print it
ai_use: "This summary was written by Claude (Anthropic) from the published design. Each board carries its own AI-use line saying Claude designed the diagram, built the test models, ran both engines and computed every number shown. See AI use."
written_from: "the published Claude design https://claude.ai/artifact/NjBEcuK8pXMRPneYT6CaqH, version 1794673165-b82c: its ten board files (project/Main.dc.html and project/S02 to S10, 278,596 bytes in all; Main.dc.html SHA-256 45457829885c6a84450f51854df00d7de306954723bb4694d2f6143313e96f90) and project/canvas.json, rendered in headless Chromium on 2026-11-18 through the Netlify conversion and read in full. Nothing was run to write this file."
---

# SWMM6 in Diagrams: ten diagrams of what OpenSWMM 6 changes in the SWMM5 engine

## In three points
- **What:** Ten boards, each 1,600 px wide, that set SWMM5 beside OpenSWMM 6.0.0-alpha.4: the SWMM2D street mesh, the dynamic Preissmann slot, semi-implicit node continuity, Anderson acceleration, virtual junctions, finite-volume routing with local time steps, the 2D surface, gridded groundwater, the C++20 engine and its C API, and the engine as a hub for scripts and agents.
- **So what:** Six boards carry runs on small test chains. DYNAMIC_SLOT took steps not converging from 2.99% to 0.00% and continuity from 0.091% to 0.008%, but shrank the average step from 6.51 s to 1.28 s. SEMI_IMPLICIT stopped non-convergence and made continuity worse on both ponded chains (-0.32% to -3.00% on chain B). Anderson acceleration saved about 0% where the documentation claims 25 to 50%. FV routing held continuity at 0.000% and ran 7 times slower, and reported -158% and -133% with ponding.
- **Now what:** Test each option on your own model before adopting it. Every measured board is one small chain, not a field calibration; boards 1, 7 and 8 show the documented design with no run behind them.

This summary was written after the fact. The design ships no technical summary of its own and gives no version number; the version above is its date. The file name is ours. Every number below is copied from the boards. Nothing was run to write this file.

## What it is

A Claude design of ten boards titled "SWMM6 in Diagrams". Each board has a SWMM5 panel and a SWMM6 panel with four numbered points each, then a measured panel, a "watch" note and a "what this does not show" note.

## The test chains (as the boards state them)

- Chain A: eight 50 ft runs of 15 in pipe at 0.2%, 10 cfs peak at J1 plus 4 cfs at J5, 500 ft2 ponding, 20 s routing step, variable step 0.75.
- Chain B: 40 ft runs, 14 cfs peak, 30 s routing step.
- Chain C: eight 50 ft runs of 15 in pipe at 0.2%, 10 cfs peak plus 4 cfs at J5, no ponding, 20 s routing step.
- Chain D: four 400 ft runs of 24 in pipe at 0.1%, 16 cfs peak at J1, no ponding, 5 s routing step, variable step 0.75.

## Results the boards report

| Board | Measured |
|---|---|
| 2. Slot instead of a switch (chain A) | EPA 5.2.4 / SWMM6 EXTRAN / SWMM6 DYNAMIC_SLOT: continuity 0.194 / 0.091 / 0.008%; steps not converging 9.43 / 2.99 / 0.00%; average step 9.91 / 6.51 / 1.28 s. C8 peak 11.67 to 11.71 cfs. Slot width 32.2 x 1.227 / 82^2, about 0.07 in. |
| 3. One node equation | EXPLICIT / SEMI_IMPLICIT: not converging 2.99 / 0.00%; continuity A 0.091 / -0.389%, B -0.316 / -2.998%. J4 through its 1.25 ft crown: 1.25, 1.50, 1.70, 1.70 ft against 1.21, 1.28, 1.39, 1.47 ft. On an unponded 4-pipe chain, -0.092% to -0.023%. Alpha.4 reports EXPLICIT when the line is missing. |
| 4. Anderson acceleration | Trials per step, chain A: 3.00 (EPA 5.2.4), 2.51 (plain Picard), 2.51 (ANDERSON_ACCEL YES); chain B: 3.06, 2.74, 2.72. Every step runs at least 2 trials, so at 2.51 the most any accelerator could save was 20%. A two-node toy took 7 trials plain and 5 with Anderson. |
| 5. Virtual junctions (chain D) | J2 and J3 made virtual: continuity -0.092 to -0.089%; J2 max depth 6.35 ft both; C4 peak 16.0 cfs both; continuity nodes 4 to 2. An earlier 15-model test (alpha.3, August 2026) took one model's continuity from -0.07% to -24.9% when every eligible node was converted. |
| 6. FV routing (chain C) | DYNWAVE / FV: continuity -0.054 / 0.000%; run time 0.29 / 2.04 s; average step or substep 4.32 / 0.15 s; C8 peak 10.70 / 9.91 cfs. Tier occupancy 91.4 / 4.2 / 1.6 / 2.8%. With ALLOW_PONDING YES, FV reported -158% and -133% continuity. |
| 7. Flood water goes somewhere | EPA 5.2.4, chain A with 500 ft2 ponding: maximum ponded depth 5.03 ft at J1 down to 0.45 ft at J6; J1 held about 2,500 ft3. No 2D run. |
| 9. The engine underneath (chain D) | EPA 5.2.4 and OpenSWMM 6.0.0-alpha.4 with SWMM5 options: continuity -0.092% both, 2.11 trials per step both, C1 peak 16.0 cfs both, J2 6.35 ft both. Two models stepped side by side in one Python process: 4,324 steps in 0.19 s. On ponded chain A, EPA peaked at 14.45 cfs and SWMM6's SWMM5 path at 11.67. |
| 10. An engine built to be driven | openswmm.engine.catalog.load() in 6.0.0a4: 1,173 C exports, 1,084 members, 87 targets, 78 enums, 38 records. |

Boards 1 and 8 are worked illustrations: in board 1 the inlet sees 0.22 ft in one 100 ft sub-grid cell against 0.30 ft on the mesh; in board 8 a SWMM5 aquifer with A1 = 0.002, B1 = 2 and 3 ft of head gives 0.018 cfs per acre, 0.36 cfs on 20 acres.

## Checks

- Arithmetic we checked (ours): 2.04 / 0.29 = 7.0 times; (2.51 - 2) / 2.51 = 20%; 0.002 x 3^2 = 0.018; 32.2 x 1.227 / 82^2 = 0.0059 ft = 0.07 in, and 1.227 ft2 is the area of a 15 in circle; 25 m/s = 82 ft/s.
- The boards name their engines (EPA SWMM 5.2.4 and pip openswmm 6.0.0a4.dev1) and their test chains, and each states what it does not show.

## What this does not show

As the boards list it: one small test chain per measured board, not a field calibration; board 1's cell sizes and step counts are illustrative; board 4's bars are Claude's own two-node toy, not OpenSWMM's code; boards 7 and 8 show the documented SWMM6 design with no 2D or groundwater run; the MCP server and the Gymnasium environment on board 10 were not run.

## How to reproduce

Build chains A to D from the descriptions above and run them in EPA SWMM 5.2.4 and in pip openswmm 6.0.0a4.dev1 with the option each board names. The model files are not in the design.

## Credits and licenses

The SWMM2D team's design note (board 1's design choices are theirs); Sharior et al. 2023 for the slot; EPA's SWMM 5 QA report for the SWMM5 node equation; the openswmm PyPI page, docstrings and the 2026 OpenSWMM roadmap and presentation. No OpenSWMM source is bundled. No license is stated for the design.

## AI use

Each board says: "Claude (Anthropic) designed this diagram, built the test models, ran both engines and computed every number shown." Board 1 says Claude drew it and computed its depths from the SWMM2D design note, and that the design choices described are the SWMM2D team's. It is a Claude design on Robert Dickinson's account. The Netlify copy is a conversion made by Claude on 18 November 2026: the ten boards unchanged apart from element ids made unique, stacked on one page and scaled to the screen. This summary was written by Claude on 18 November 2026.

## Changes

- 2026-11-14: the version read (the design's date; it carries no version number).
