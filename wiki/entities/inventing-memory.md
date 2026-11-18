---
title: "Inventing Memory (app)"
type: entity
updated: 2026-11-18
sources: [S366]
tags: [apps, neural-networks, hopfield, cross-sections]
reviewed: no
---
Bob's app Inventing Memory: a Hopfield forgetting machine that remembers SWMM5 cross-section shapes. Version 1.0, 2026-10-25 [S366](../sources/S366-inventing-memory-summary.md). Its `links:` line names no live Netlify address [S366](../sources/S366-inventing-memory-summary.md).

**A caution about its source.** The page ships no technical summary. [S366](../sources/S366-inventing-memory-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S366](../sources/S366-inventing-memory-summary.md)
- A single-file edition of Bob's Lovable experiment: a Hopfield network on 144 cells taught 14 glyphs of SWMM5 cross-section shapes, made to forget (every weight shrinks and picks up noise each tick), kicked with damaged glyphs, and judged on whether it recalls a taught shape or invents a new one. A second page explores the properties of all 19 shapes against EPA SWMM 5.2.4 reference curves ported from xsect.c.
- Fourteen patterns on 144 cells is 0.097, under the classic 0.138 capacity, yet Hebb's rule never shows more than 7 of the 14 taught shapes; the added projection rule shows all 14 until it forgets them, faster, and 46% of its cell-ticks are inventions even with no forgetting (σ = 0). Neither rule gives invention by forgetting.
- Port: a seeded replay of the shipped loop matches the original TypeScript tick for tick (mean energy and all 16 labels identical for 600 ticks in four configurations, including self-rewriting, σ = 0 and σ = 0.04); the kernel port matches xsect.ts on 19 shapes x 4 tables x 51 points with zero difference.
- Reference: xsect.dat and xsect.c from the EPA repository at tag v5.2.4; at full depth every EPA curve returns A/Afull = 1 and R/Rfull = 1; the peak of each section-factor table agrees with sMax in xsect_setParams within 0.0021, except the semi-elliptical, where EPA's own table peaks at 1.050.
- CUSTOM shapes: the shape.c port reproduces the circle (0.783, 0.249, 1.078 at 0.94) and a closed square (area 1, radius 0.25).
- Measurements: five seeds x 800 ticks per configuration, 64,000 cell-ticks each; every number in the Audit and Doc is read from that run.

**How to use it, as the summary puts it.** Use it as a playful lesson in memory, capacity and the geometry of SWMM shapes. The 12 x 12 alphabet is not SWMM's geometry, the exported CUSTOM-shape .inp was not run through the EPA engine, and the projection rule is one alternative among several untried. [S366](../sources/S366-inventing-memory-summary.md)

**What it does not show.** As the page lists it: no SWMM5 run of the exported .inp; the 12 x 12 alphabet is the Lovable glyph set, not SWMM's geometry (a circle on 144 cells is a blob); mirror agreement, piece count and holes stand in for "looks like a conduit"; the projection rule is one alternative; ellipse and arch sizes use size code 1 for their full-section constants, and the modified basket handle is compared only with W = H and a semicircular top. [S366](../sources/S366-inventing-memory-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md).
