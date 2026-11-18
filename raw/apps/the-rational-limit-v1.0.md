---
name: The Rational Limit
file: the-rational-limit.html
version: "1.0"
date: 2026-10-12
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/W8t35onrYF3yFgRgroyGZz", repo: none}
engines:
  - {name: "three models written for the page", note: "1D shallow-water equations with rain (HLL finite volume, implicit Manning friction); exact kinematic wave by characteristics; EPA SWMM 5's nonlinear reservoir ported from subcatch.c"}
  - {name: EPA SWMM, version: 5.2.4, note: "built from the v5.2.4 tag on 2026-10-12 and run on ten cases while building"}
units: US customary throughout
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page carries no AI-use note."
written_from: "the published Claude artifact https://claude.ai/artifact/W8t35onrYF3yFgRgroyGZz, version 1791789357-2448 (index.html, 121,696 bytes, SHA-256 b023d9f9b9c83ab5f2f59dcb72cf35169404dbc771767f2c824da9430d749c2e), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file."
---

# The Rational Limit: Q = CiA as the steady state a shallow-water simulation settles to

## In three points
- **What:** A worked proof of Bob's claim (October 2026) that the rational method is "a limiting case, not a competitor": hold steady rain on a plane for at least the time of concentration and every model, from the full shallow-water equations to SWMM's nonlinear reservoir, ends on Q = (i - f)A = CiA. Continuity alone gives the answer; momentum only decides how long the plane takes to get there.
- **So what:** In EPA SWMM 5.2.4, eight of eight equilibrium cases plateau at 1.000037 x (i - f)A, the 0.0037% being SWMM's own acre constant, matched to five significant figures. Width, roughness and depression storage change when the plateau arrives, not its height: on the default asphalt lot (200 ft by 500 ft, 1%, n 0.015, 2.0 in/hr) the plateau is 4.63 cfs, reached at 95% in 5.3 min by the kinematic wave and 12.9 min by SWMM's reservoir, which stores 1.6 times the kinematic volume.
- **Now what:** Use it to teach why the rational method survives inside every runoff model, and where it stops: a storm shorter than the time of concentration never reaches the plateau (a 5-minute burst gives 0.54 of iA in SWMM). One plane, uniform slope and roughness, a constant loss and no observed flows.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-12"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: The collapse, Derivation, Why D = tc, Engine check, Research, Where it stops. Presets: parking lot (asphalt), flat roof membrane, a short burst on a long lot (D < tc), a mowed lawn with a constant loss, a flat rough surface. Three curves on one plane: shallow-water equations (6,315 time steps on 100 cells at the default), exact kinematic wave, and SWMM's nonlinear reservoir (Manning constant 1.49), against the line Q = CiA. The Derivation tab carries the eight steps with the user's numbers (for the default, q(L) = 0.009259 ft2/s per ft; Q[cfs] = 1.0083 · C · i[in/hr] · A[ac]).

## Checks (as stated on the page)

EPA SWMM 5.2.4, compiled from the v5.2.4 tag, ten one-subcatchment models with constant rain from time zero, read from the binary .out at a one-minute report step: C1 to C3 (impervious, i 2, 1, 4) and C6 to C10 (shorter, wider plane; 0.1 in depression storage; pervious with f 0.5 at i 2 and 4; n 0.05) all plateau at 1.000037 x (i - f)A; C4 (D 5 min) peaks at 0.542736 and C5 (D 10 min) at 0.881542. The app's reservoir port is within 0.045% to 0.132% of SWMM in every case.

## What this does not show

As the page lists it: one plane, uniform slope and roughness, no channel, no network, no converging geometry, no moving storms, a constant loss rather than Horton or Green-Ampt decay, and no observed flows. Whether a real catchment reaches the steady state in a design storm is a separate question.

## Credits and licenses

EPA SWMM 5 subcatch.c (public domain); Henderson and Wooding's kinematic wave; the Research tab's sources, retrieved 12 October 2026 (two nineteenth-century entries cited through later papers). No license is stated for the page.

## AI use

The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-12): first version (the version read).
