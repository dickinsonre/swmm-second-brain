---
title: "S329: The Rational Limit, summary written from the page (v1.0)"
type: source
raw: raw/apps/the-rational-limit-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-12
ingested: 2026-11-18
tags: [apps, swmm5, rational-method, runoff]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app The Rational Limit, version 1.0: Q = CiA as the steady state a shallow-water simulation settles to. Raw file: [raw/apps/the-rational-limit-v1.0.md](../../raw/apps/the-rational-limit-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/W8t35onrYF3yFgRgroyGZz, version 1791789357-2448 (index.html, 121,696 bytes, SHA-256 b023d9f9b9c83ab5f2f59dcb72cf35169404dbc771767f2c824da9430d749c2e), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- A worked proof of Bob's claim (October 2026) that the rational method is "a limiting case, not a competitor": hold steady rain on a plane for at least the time of concentration and every model, from the full shallow-water equations to SWMM's nonlinear reservoir, ends on Q = (i - f)A = CiA. Continuity alone gives the answer; momentum only decides how long the plane takes to get there.
- In EPA SWMM 5.2.4, eight of eight equilibrium cases plateau at 1.000037 x (i - f)A, the 0.0037% being SWMM's own acre constant, matched to five significant figures. Width, roughness and depression storage change when the plateau arrives, not its height: on the default asphalt lot (200 ft by 500 ft, 1%, n 0.015, 2.0 in/hr) the plateau is 4.63 cfs, reached at 95% in 5.3 min by the kinematic wave and 12.9 min by SWMM's reservoir, which stores 1.6 times the kinematic volume.
- EPA SWMM 5.2.4, compiled from the v5.2.4 tag, ten one-subcatchment models with constant rain from time zero, read from the binary .out at a one-minute report step: C1 to C3 (impervious, i 2, 1, 4) and C6 to C10 (shorter, wider plane; 0.1 in depression storage; pervious with f 0.5 at i 2 and 4; n 0.05) all plateau at 1.000037 x (i - f)A; C4 (D 5 min) peaks at 0.542736 and C5 (D 10 min) at 0.881542.

**Limits it states.** As the page lists it: one plane, uniform slope and roughness, no channel, no network, no converging geometry, no moving storms, a constant loss rather than Horton or Green-Ampt decay, and no observed flows. Whether a real catchment reaches the steady state in a design storm is a separate question.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [The Rational Limit (app)](../entities/the-rational-limit.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](../concepts/subcatchment-width.md).
