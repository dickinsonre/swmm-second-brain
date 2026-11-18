---
title: "Topology Surface Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S375]
tags: [apps, topology, mathematics, not-water]
reviewed: no
---
Bob's app Topology Surface Explorer: surfaces built by gluing the edges of a polygon. Version and date 2026-10-28 [S375](../sources/S375-topology-surface-explorer-summary.md). Its `links:` line names no live Netlify address [S375](../sources/S375-topology-surface-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S375](../sources/S375-topology-surface-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S375](../sources/S375-topology-surface-explorer-summary.md)
- An interactive explorer for surfaces built by gluing the edges of a polygon. Type a gluing word such as aba'b' and the app names the surface, computes its Euler characteristic, orientability and boundary count, reduces the word to normal form step by step, and shows the surface as a polygon, a 3D model, a hyperbolic tiling, a walk and a kart race. Not a water-modeling app.
- An independent surface classifier written for the check agrees with the app on 21 of 21 words; all 25 invariant checks printed during six step-by-step reductions read "Surface unchanged"; straight-walk crossing counts match hand predictions on all five flat surfaces. One known issue: on a curved surface the Walk tab's "straight-line distance from start" loses accuracy after about 25 units of walking and is off by up to 0.28 at 36 units (the walking itself is unaffected).
- The supplied file run unmodified in a headless browser to collect every number in the Doc.
- An independent surface classifier against the app on 21 words: 21 agree.
- 25 invariant checks during six reductions; crossing counts on five flat surfaces against hand predictions; a control test of the hyperbolic drawing.
- The same data collection re-run on the edited file returned identical numbers.

**How to use it, as the summary puts it.** Use it to learn the classification of surfaces by playing with words. The essay, its history and figures, and the 3D models, hyperbolic drawings and kart physics have not been checked by a person. [S375](../sources/S375-topology-surface-explorer-summary.md)

**What it does not show.** As the page lists it: the Walk distance readout error on curved surfaces (measurements, cause and the responsible line of code are in the Doc); no person has checked the essay text and its history, the figures, the 3D models, the hyperbolic drawings or the kart physics. [S375](../sources/S375-topology-surface-explorer-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md).
