---
title: "SWMM5 · SWMM6 Curve Sections (app)"
type: entity
updated: 2026-11-17
sources: [S205, S262]
tags: [apps, swmm5, swmm6, cross-sections, geometry, findings]
reviewed: no
---
Bob's app SWMM5 · SWMM6 Curve Sections: an app that replaces SWMM's cross-section lookup tables with one boundary curve of arcs and lines, gives the eleven tabulated shapes as curves plus seven families of new ones, runs them in a patched EPA SWMM 5.2.4 (swmm524-curves, reading OpenSWMM's XSECT_GEOMETRY EXACT and XPOLYGON syntax) in the page, and writes input for three kinds of engine. Version 1.0, 2026-11-02 [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md). Netlify address: https://swmm5-swmm6-curve-sections.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md)
- Gothic sewer in dry weather: the most water that ever enters is 0.76 cfs; with the tables the last conduit rings between about 0.46 and 0.98 cfs for more than an hour and hands the outfall a peak 29 percent bigger than any inflow; with curves it climbs smoothly to 0.760.
- Dry-weather continuity: Gothic from -9.10 to -1.05 percent and Semi-elliptical from -8.74 to -1.26 percent; every shape between -0.91 and -1.37 percent with curves. In wet weather the median worst-moment flow difference runs 0.4 to 2.2 percent.
- Horseshoe: four of its five tables describe one outline and the width table another; at y/H = 0.08 they differ by about 12 percent.
- Basket-handle: its constant says 0.944 H wide, its area table about 0.99 H; the width table times 0.944 integrates 5.9 percent short of the stored area, times 1.0 0.3 percent short.
- Gothic, Catenary, Semi-elliptical, Basket-handle and Semi-circular have no confirmed definition; their fits of three or four arcs land within 0.15 percent on area and radius and are labelled as fits.
- Without the option the engine's .out matches stock 5.2.4 byte for byte. The background: in August 2026 Corinne Wiesner-Friedman showed for OpenSWMM that the tables disagree, worst at low depth, and her branch replaced the circle with exact geometry.

**What it does not show.** No field data, so nothing says a model predicts better. Five shapes are fits, not confirmed definitions. [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md)

**Noted at ingest.** 0.98 / 0.76 = 1.29, the 29 percent. The tables are the ones on [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md); a defect of the table method at low depth is a finding for [The SWMM findings register](../concepts/findings-register.md), at the page's word.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md), [Shape curves, transects and storage curves](../concepts/shape-curves-transects-storage-curves.md), [The SWMM findings register](../concepts/findings-register.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
