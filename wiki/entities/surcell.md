---
title: "Surcell (app)"
type: entity
updated: 2026-11-18
sources: [S296]
tags: [apps, geometry, four-dimensions, curvature, webgl]
reviewed: no
---
Bob's app Surcell: a flight game inside curved three-dimensional worlds that sit in four dimensions (the 3D boundary, or "surcell", of a 4D shape), with light traced along geodesics on the graphics card and a panel that measures curvature where you stand. Version and date 2026-10-28 [S296](../sources/S296-surcell-summary.md). Netlify address, from its `links:` line: https://surcell-fly-inside-4d.netlify.app [S296](../sources/S296-surcell-summary.md).

**A caution about its source.** The page ships no technical summary. [S296](../sources/S296-surcell-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S296](../sources/S296-surcell-summary.md)
- Ten worlds: Glome, Spheritorus, Torisphere, Tiger, Ditorus, Hyperbolic, Catenoid, Helicoid, Schwarz P and Revolution with chosen profile curves.
- The lemniscate cosine for the 4D catenoid is computed with four steps of the arithmetic-geometric mean, good to a part in a trillion against the defining integral; the 4D catenoid stays inside a slab 2.62 neck-radii thick.
- Checks: closed-form curvature, the lemniscate integral, Gauss-Bonnet, an independent Gram-matrix calculation of honeycomb edges and 72 timed loop walks.

**What it does not show.** Rendering checked in software WebGL only, not on a GPU; Schwarz P is an approximation; the Helicoid has no recentring; the shader holds 40 to 128 objects; no person has flown the build or checked the history claims. [S296](../sources/S296-surcell-summary.md)

**Noted at ingest.** Not a water app. The page did not finish loading in headless Chromium, so the summary was written from its source text.

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md).
