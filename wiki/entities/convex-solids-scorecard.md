---
title: "Convex Solids Scorecard (dashboard)"
type: entity
updated: 2026-11-18
sources: [S368]
tags: [dashboards, physics, not-water]
reviewed: no
---
Bob's dashboard Convex Solids Scorecard: what the Convex Solids Physics build measures about itself. Version and date 2026-10-09 [S368](../sources/S368-convex-solids-scorecard-summary.md). Its `links:` line names no live Netlify address [S368](../sources/S368-convex-solids-scorecard-summary.md).

**A caution about its source.** The page ships no technical summary. [S368](../sources/S368-convex-solids-scorecard-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S368](../sources/S368-convex-solids-scorecard-summary.md)
- A one-page dashboard about Convex Solids Physics v4.60, a 3D physics app of every convex polyhedron with regular faces. Every figure was read out of the running app, not written down beside it: 104 engine controls (91 pass, 13 reproduced limitations, 0 fail), a catalogue of 239 solids, the file's own size and surface, frame rates, the demo film and 13 defects closed in the session. Not a water-modeling app.
- It shows the largest limitation measured rather than described: cannon.js 0.6.2 bounds friction as an impulse per step, not as a force, so the same cube at the same friction slides 6.63 m (21.8 ft, ours) in 2 s at a 1/30 s step, 3.15 m at 1/60 s, 0.01 m at 1/120 s and 0.0 m at 1/240 s. At slider friction 0.4, Coulomb says sliding starts at 21.8°; the engine starts a 1 kg cube at 8.5° and a 1,000 kg tetrahedron at 9.0°.

**How to use it, as the summary puts it.** Use it to see how far to trust the app's physics and where the engine is wrong on purpose. The frame rates were measured in a headless container on software WebGL, the slowest way the app runs, and the counts are from one headless run of v4.60. [S368](../sources/S368-convex-solids-scorecard-summary.md)

**What it does not show.** As the dashboard states: the frame rates come from software WebGL in a headless container, and a machine with a GPU is far quicker; the gate's two figures are the code's own constants, not a dataset; the counts come from one headless run of v4.60. [S368](../sources/S368-convex-solids-scorecard-summary.md)

**Noted at ingest.** 91 + 13 + 0 = 104 controls (our arithmetic). A Claude Data artifact, converted to a standalone page for Netlify with a small script standing in for the dashboard's data loader.

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
