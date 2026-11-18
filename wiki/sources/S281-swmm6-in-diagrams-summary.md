---
title: "S281: SWMM6 in Diagrams, summary written from the page (v2026-11-14)"
type: source
raw: raw/apps/swmm6-in-diagrams-v2026-11-14.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-18
tags: [diagrams, swmm6, openswmm, slot, anderson, virtual-junctions, finite-volume]
drafted_by: Claude (Anthropic), from the published design
reviewed: no
---
**What it is.** A technical summary of the set of diagrams SWMM6 in Diagrams, version 2026-11-14: ten 1,600 px boards that set SWMM5 beside OpenSWMM 6.0.0-alpha.4 (the SWMM2D street mesh, the dynamic slot, semi-implicit node continuity, Anderson acceleration, virtual junctions, finite-volume routing, the 2D surface, gridded groundwater, the engine and its API), six of them with runs on small test chains. Raw file: [raw/apps/swmm6-in-diagrams-v2026-11-14.md](../../raw/apps/swmm6-in-diagrams-v2026-11-14.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude design https://claude.ai/artifact/NjBEcuK8pXMRPneYT6CaqH, version 1794673165-b82c: its ten board files (project/Main.dc.html and project/S02 to S10, 278,596 bytes in all; Main.dc.html SHA-256 45457829885c6a84450f51854df00d7de306954723bb4694d2f6143313e96f90) and project/canvas.json, rendered in headless Chromium on 2026-11-18 through the Netlify conversion and read in full. Nothing was run to write this file." Each board carries its own AI-use line: Claude (Anthropic) designed the diagram, built the test models, ran both engines and computed every number shown. The Netlify copy stacks the ten boards on one page.

**Claims worth keeping** (all copied from the file)
- Chain A (eight 50 ft runs of 15 in pipe, ponded): EPA 5.2.4 / SWMM6 EXTRAN / SWMM6 DYNAMIC_SLOT give continuity 0.194 / 0.091 / 0.008%, steps not converging 9.43 / 2.99 / 0.00%, average step 9.91 / 6.51 / 1.28 s.
- SEMI_IMPLICIT stopped non-convergence (2.99 to 0.00%) and made continuity worse on both ponded chains (A 0.091 to -0.389%, B -0.316 to -2.998%); on an unponded 4-pipe chain it helped (-0.092 to -0.023%).
- Anderson acceleration: 2.51 trials per step with and without it on chain A (EPA 5.2.4: 3.00); the documented 25 to 50% fewer iterations was not reproduced; with a floor of 2 trials the most any accelerator could save was 20%.
- Virtual junctions on chain D: 4 continuity nodes to 2, depths and peaks unchanged; an earlier 15-model test (alpha.3) took one model's continuity from -0.07% to -24.9% when every eligible node was converted.
- FV routing on chain C: continuity 0.000% against -0.054%, run time 2.04 s against 0.29 s; with ALLOW_PONDING YES, FV reported -158% and -133%.
- Parity is not universal in alpha.4: on ponded chain A, EPA 5.2.4 peaked at 14.45 cfs and SWMM6's SWMM5 path at 11.67 cfs; on chain D the two agree on every number shown.

**Limits it states.** One small chain per measured board, not a field calibration; board 4's bars are a two-node toy; boards 7 and 8 show the documented design with no 2D or groundwater run; the MCP server and Gymnasium environment were not run.

**Checked at ingest.** 2.04 / 0.29 = 7.0 times; (2.51 - 2) / 2.51 = 20%; slot width 32.2 x 1.227 / 82^2 = 0.0059 ft, about 0.07 in, for a 15 in pipe; 25 m/s = 82 ft/s (our arithmetic). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM6 in Diagrams (design)](../entities/swmm6-in-diagrams.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Infiltration methods](../concepts/infiltration-methods.md).
