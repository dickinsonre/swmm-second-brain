---
title: "HydroCalc Studio (app)"
type: entity
updated: 2026-11-18
sources: [S360]
tags: [apps, open-channel, calculators, gradually-varied-flow]
reviewed: no
---
Bob's app HydroCalc Studio: eight open-channel and routing calculators, each showing its equation. Version 1.0, 2026-10-24 [S360](../sources/S360-hydrocalc-studio-summary.md). Its `links:` line names no live Netlify address [S360](../sources/S360-hydrocalc-studio-summary.md).

**A caution about its source.** The page ships no technical summary. [S360](../sources/S360-hydrocalc-studio-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S360](../sources/S360-hydrocalc-studio-summary.md)
- Eight calculators in one file: Manning's equation, a compound channel by the divided channel method, gradually varied flow profiles, rating curves, a single Muskingum step, full hydrograph routing, a sensitivity study and a side-by-side channel comparison. Every result shows the equation it came from with your numbers in it.
- The Lovable original drew its flow profile as normal depth with a 5% sine wave on it; this edition solves the gradually varied flow by direct step with an RK4 cross-check and classifies M, S, C, H and A profiles. Its unit switch only relabeled values (now it converts them), and it used k = 1.49 for Manning (now 1.486, a 0.27% change). 44 automated checks pass, including the US default Manning flow of 8,165.6 cfs and the Muskingum coefficients 0.1304, 0.3043 and 0.5652.
- Hand calculations: Manning for the US default (8,165.6 cfs) and the first version's SI default (264.2 m3/s); Muskingum coefficients 0.1304, 0.3043, 0.5652; the textbook outflow of 105.217 cfs.
- Invariance: the same channel in feet and in metres gives the same discharge to twelve significant figures; the M1 profile matches to better than 0.01%.
- Two methods: direct step and RK4 agree to 0.0001% on M1 and 0.13% on M2; refining from 600 to 2,400 depth steps changes the answer by less than one part in a million; the energy equation holds on every step.
- Classification: M1, M2, M3, S1, S2, S3, H2 and A2 each labelled correctly and heading the right way. Plus the Lovable defaults reproduced, grid refinement and Muskingum continuity.

**How to use it, as the summary puts it.** Use it to teach and check steady 1D channel hydraulics and hydrologic routing. Nothing here solves the Saint-Venant equations; Muskingum cannot represent backwater or a looped rating; the profile stops at critical depth. [S360](../sources/S360-hydrocalc-studio-summary.md)

**What it does not show.** As the page lists it: everything is steady and one-dimensional; routing is hydrologic (linear storage with constant K and x), so no backwater from a tributary, looped rating, or a wave whose speed changes with depth; the profile stops at critical depth, with no jumps, drops, bridges, culverts or section changes, in prismatic channels with one n and one slope; the compound channel is rectangles with vertical divisions and no momentum exchange at the interface (Knight and Shiono's method would add it). [S360](../sources/S360-hydrocalc-studio-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Non-Prismatic Channel Lab (app)](non-prismatic-channel-lab.md).
