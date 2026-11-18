---
name: Convex Solids Scorecard
file: convex-solids-scorecard.html
version: 2026-10-09
date: 2026-10-09
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NPJWmFKSksmYcKAr9jpq5z", subject: "Convex Solids Physics v4.60 (Netlify site convex-solids-physics)", repo: none}
engines: none (a dashboard of measurements taken from Convex Solids Physics, which runs cannon.js 0.6.2 and three.js)
units: SI as measured (m, kg, N, s); US customary conversions below are ours
ai_use: "This summary was written by Claude (Anthropic) from the published dashboard. The dashboard carries no AI-use note."
written_from: "the published Claude Data artifact https://claude.ai/artifact/NPJWmFKSksmYcKAr9jpq5z, version 1791516991-3e6b (index.html, 21,694 bytes), its page file (index.html in the files collection, 45,877 bytes) and its 12 datasets with their CSV files, read on 2026-11-18. The Netlify page beside this file was converted from them by Claude on 2026-11-18. Nothing was run to write this file."
---

# Convex Solids Scorecard: what the Convex Solids Physics build measures about itself

## In three points
- **What:** A one-page dashboard about Convex Solids Physics v4.60, a 3D physics app of every convex polyhedron with regular faces. Every figure was read out of the running app, not written down beside it: 104 engine controls (91 pass, 13 reproduced limitations, 0 fail), a catalogue of 239 solids, the file's own size and surface, frame rates, the demo film and 13 defects closed in the session. Not a water-modeling app.
- **So what:** It shows the largest limitation measured rather than described: cannon.js 0.6.2 bounds friction as an impulse per step, not as a force, so the same cube at the same friction slides 6.63 m (21.8 ft, ours) in 2 s at a 1/30 s step, 3.15 m at 1/60 s, 0.01 m at 1/120 s and 0.0 m at 1/240 s. At slider friction 0.4, Coulomb says sliding starts at 21.8°; the engine starts a 1 kg cube at 8.5° and a 1,000 kg tetrahedron at 9.0°.
- **Now what:** Use it to see how far to trust the app's physics and where the engine is wrong on purpose. The frame rates were measured in a headless container on software WebGL, the slowest way the app runs, and the counts are from one headless run of v4.60.

This summary was written after the fact. The dashboard ships no technical summary of its own and gives no version number; the date is its data files' own ("2026-10-09T03:30:00Z", by "app-gates.js and a headless run of v4.60"). The file name above is ours. Every number below is copied from the dashboard's data. Nothing was run to write this file.

## What it shows

Tiles: engine controls run, failing (was 3 before the session), limitations reproduced, solids in the catalogue (none rejected by the geometry gate), tour steps that threw. Sections: Verification (controls by kind and by status, the geometry gate, every control with what it measured), Friction (slide against timestep, angle where sliding starts, the thirteen limitations), The catalogue (solids by family), What the file holds, What it costs to draw (frame rate by resolution, cost of each quality setting), The film of the tour, and Defects closed in this session. A guided tour of twelve stops points at one card at a time.

## The data (12 files)

- Controls by status: 91 pass, 13 limitation reproduced, 0 fail. By kind: 74 benchmark, 13 documented limitation, 12 apparatus, 2 geometry, 1 each reproducibility, calibration and null control.
- Geometry gate: worst outward penetration 1.18 × 10⁻⁶ R (J91 bilunabirotunda) against a tolerance of 2.0 × 10⁻⁶ R; 0 solids rejected.
- Catalogue: 239 solids (5 Platonic, 13 Archimedean, 92 Johnson, 5 prisms, 5 antiprisms, 115 duals, 3 solids of revolution, 1 sphere); 6,054 vertices, 11,632 edges, 6,054 faces across the set.
- The file: 7,029 lines of script, 1,187 kB, 361 element ids, 113 inline handlers, 183 buttons, 54 sliders, 23 selects, 22 checkboxes, 7 tabs.
- Frame rate at 1280 × 720: 1.3 frames/s with shadows, 3.6 without, 3.9 at 0.75 pixel ratio; from 0.8 frames/s at 1600 × 900 to 7.4 at 640 × 360.
- The tour film: 44 steps, 0 threw, 63.8 s of simulated time, a 72.5 s film of 1,449 frames at 20 frames/s, 3.3 MB.
- Defects closed between v4.50 and v4.60: 13, of which 8 were in the app, 2 in the demo tour and 3 in verification controls.

## What this does not show

As the dashboard states: the frame rates come from software WebGL in a headless container, and a machine with a GPU is far quicker; the gate's two figures are the code's own constants, not a dataset; the counts come from one headless run of v4.60.

## Credits and licenses

cannon.js 0.6.2 (the physics engine the app runs); d3 7.9.0 draws the charts in the Netlify copy. No license is stated for the dashboard.

## AI use

The dashboard carries no AI-use note. The Netlify copy was converted from the Data artifact by Claude on 18 November 2026: the page's markup, styles and drawing code are unchanged and a small script stands in for the dashboard's data loader. This summary was written by Claude (Anthropic) on 18 November 2026.

## Changes

- 2026-10-09: the dashboard as read (data from v4.60).
