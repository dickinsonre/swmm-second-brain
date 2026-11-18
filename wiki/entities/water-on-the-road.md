---
title: "Water on the Road (app)"
type: entity
updated: 2026-11-17
sources: [S205, S229, S236]
tags: [apps, swmm5, inlets, streets, hec-22, findings]
reviewed: no
---
Bob's app Water on the Road: a rebuild in one page of the six-step road-drainage workflow of Nhat Tien Vo's VNTool Civil 3D plugin (his post of 10 October 2026): pipe network from a polyline, structures by spacing, fit to the road, catchments from the corridor surface, HEC-22 hydraulics, and water on the road. Its HEC-22 code is a line-for-line port of EPA SWMM 5.2.4's inlet.c; no engine runs in the page. Version 1.1, 2026-10-15 [S236](../sources/S236-water-on-the-road-summary.md). Netlify address: https://water-on-the-road.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S236](../sources/S236-water-on-the-road-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S236](../sources/S236-water-on-the-road-summary.md)
- Sample: 6 inlets, 1.64 ac drained, peak runoff 7.34 cfs, 0.27 cfs bypass carried on, maximum spread 4.8 ft against a 10.0 ft limit.
- On a 1.20 % grade with a 2.0 % cross slope and a 2.0 in gutter depression the example flow spreads 4.58 ft; a 2 ft x 2 ft P_BAR-50 grate catches 94.0 % of it (0.969 cfs).
- The exported steady .inp, run through SWMM 5.2.4's [STREETS] and [INLETS] code, reproduces the page's HEC-22 chain on 11 inlets in 4 scenarios: approach flow within 0.17 %, capture within 0.02 percentage points, sag depth equal.
- D-1: the HEC-22 round trip is not the identity (Eq. 4-2 forward uses T^2.67, the inverse in inlet.c uses 0.375): T = 8 ft gives Q = 1.905 cfs gives T = 8.021 ft, 0.26 %.
- D-2: SWMM's "Maximum Spread" comes from the street transect at the conduit's maximum depth, not Eq. 4-2; the HEC-22 line is commented out in writeStreetStats.
- D-5: SWMM 5.2.4 built with gcc -O2 on Ubuntu aborts on input ("buffer overflow detected") unless built with -D_FORTIFY_SOURCE=0.

**What it does not show.** Not Nhat Tien Vo's code or Civil 3D. Pipe hydraulics stop at full-flow Manning, with no HGL, junction losses or timing in the pipes. The IDF curves are illustrative; not a design tool of record. [S236](../sources/S236-water-on-the-road-summary.md)

**Noted at ingest.** 1 / 2.67 = 0.3745, against the 0.375 in inlet.c, which is where D-1's 0.26 % comes from. D-5 is the same abort [Rule 110 in SWMM5 (app)](rule110-swmm5.md) reports [S229](../sources/S229-rule110-swmm5-summary.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [SWMM Inlet Library (app)](swmm-inlet-library.md), [Low-Spot Census (app)](low-spot-census.md), [The SWMM findings register](../concepts/findings-register.md).
