---
title: "Four Degrees at the Bottom (app)"
type: entity
updated: 2026-11-18
sources: [S374]
tags: [apps, lakes, heat, ice]
reviewed: no
---
Bob's app Four Degrees at the Bottom: a lake run a year at a time, with water's two oddities switched off. Version and date 2026-09-30 [S374](../sources/S374-four-degrees-at-the-bottom-summary.md). Its `links:` line names no live Netlify address [S374](../sources/S374-four-degrees-at-the-bottom-summary.md).

**A caution about its source.** The page ships no technical summary. [S374](../sources/S374-four-degrees-at-the-bottom-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S374](../sources/S374-four-degrees-at-the-bottom-summary.md)
- A 66-ft (20 m, ft ours) lake run a year at a time from the surface heat budget down, with two switches that turn off the two oddities of water: that it is densest at 3.98 °C (39.2 °F, ours), and that its ice floats. You watch temperature by depth and day, ice thickness, and the dates the lake mixes. A "free-time piece about water". Not a water-modeling app in Bob's SWMM sense.
- With both oddities on, in the mild climate the lake mixes twice a year (9 April and 6 November), holds ice from 27 December to 9 April (103 days, at most 1.2 ft, 0.37 m, ft ours), and its bottom holds 4.0 °C (39.2 °F) on 14 February under a 0 °C surface. Heat is checked rather than assumed: the change in stored and latent heat matches the integral of every flux applied, with a residual of 1.5e-7% at the default.
- Heat budget: stored plus latent heat against the integral of every flux applied; residual 1.5e-7% at the default.
- The same model code runs the numbers on screen and the tests behind them.

**How to use it, as the summary puts it.** Use it to show why lakes do not freeze solid. No snow, no sediment heat, no inflows; weather is a smooth annual cosine; and the counterfactual of sinking ice describes a world that does not exist, so there is nothing to calibrate against. [S374](../sources/S374-four-degrees-at-the-bottom-summary.md)

**What it does not show.** As the page lists it: no snow; no sediment heat flux, inflows, outflows or groundwater; weather as a smooth annual cosine, so dates are climatological, not forecasts; wind mixing is a Kraus-Turner sketch, not a turbulence model; sinking ice is a bottom slab with a fixed heat-transfer coefficient (100 W m-2 K-1), ignoring the 9% volume change; the counterfactual density law continues the 8 °C slope below 3.98 °C; with deep-water mixing at 10^-5 instead of 10^-6 m2/s, the year-on-year build-up of bottom ice in a cold-climate 20 m lake disappears, while in the severe climate it survives a tenfold change. [S374](../sources/S374-four-degrees-at-the-bottom-summary.md)

**Noted at ingest.** 27 December to 9 April is 103 days, as stated (our arithmetic).

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
