---
title: "The Rational Limit (app)"
type: entity
updated: 2026-11-18
sources: [S329]
tags: [apps, swmm5, rational-method, runoff]
reviewed: no
---
Bob's app The Rational Limit: Q = CiA as the steady state a shallow-water simulation settles to. Version 1.0, 2026-10-12 [S329](../sources/S329-the-rational-limit-summary.md). Its `links:` line names no live Netlify address [S329](../sources/S329-the-rational-limit-summary.md).

**A caution about its source.** The page ships no technical summary. [S329](../sources/S329-the-rational-limit-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S329](../sources/S329-the-rational-limit-summary.md)
- A worked proof of Bob's claim (October 2026) that the rational method is "a limiting case, not a competitor": hold steady rain on a plane for at least the time of concentration and every model, from the full shallow-water equations to SWMM's nonlinear reservoir, ends on Q = (i - f)A = CiA. Continuity alone gives the answer; momentum only decides how long the plane takes to get there.
- In EPA SWMM 5.2.4, eight of eight equilibrium cases plateau at 1.000037 x (i - f)A, the 0.0037% being SWMM's own acre constant, matched to five significant figures. Width, roughness and depression storage change when the plateau arrives, not its height: on the default asphalt lot (200 ft by 500 ft, 1%, n 0.015, 2.0 in/hr) the plateau is 4.63 cfs, reached at 95% in 5.3 min by the kinematic wave and 12.9 min by SWMM's reservoir, which stores 1.6 times the kinematic volume.
- EPA SWMM 5.2.4, compiled from the v5.2.4 tag, ten one-subcatchment models with constant rain from time zero, read from the binary .out at a one-minute report step: C1 to C3 (impervious, i 2, 1, 4) and C6 to C10 (shorter, wider plane; 0.1 in depression storage; pervious with f 0.5 at i 2 and 4; n 0.05) all plateau at 1.000037 x (i - f)A; C4 (D 5 min) peaks at 0.542736 and C5 (D 10 min) at 0.881542.

**How to use it, as the summary puts it.** Use it to teach why the rational method survives inside every runoff model, and where it stops: a storm shorter than the time of concentration never reaches the plateau (a 5-minute burst gives 0.54 of iA in SWMM). One plane, uniform slope and roughness, a constant loss and no observed flows. [S329](../sources/S329-the-rational-limit-summary.md)

**What it does not show.** As the page lists it: one plane, uniform slope and roughness, no channel, no network, no converging geometry, no moving storms, a constant loss rather than Horton or Green-Ampt decay, and no observed flows. Whether a real catchment reaches the steady state in a design storm is a separate question. [S329](../sources/S329-the-rational-limit-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](../concepts/subcatchment-width.md).
