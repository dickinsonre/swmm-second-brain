---
title: "S374: Four Degrees at the Bottom, summary written from the page (v2026-09-30)"
type: source
raw: raw/apps/four-degrees-at-the-bottom-v2026-09-30.md
kind: app-md
author: Robert Dickinson
published: 2026-09-30
ingested: 2026-11-18
tags: [apps, lakes, heat, ice]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Four Degrees at the Bottom, version 2026-09-30: a lake run a year at a time, with water's two oddities switched off. Raw file: [raw/apps/four-degrees-at-the-bottom-v2026-09-30.md](../../raw/apps/four-degrees-at-the-bottom-v2026-09-30.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/YSAEfuB3BshqrrWdii3JFJ, version 1790737986-4ee8 (index.html, 55,945 bytes, SHA-256 95e49b4029818c7345bd02422c6eef0edc66200e61a8b8997221d7d55956c5ef), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- A 66-ft (20 m, ft ours) lake run a year at a time from the surface heat budget down, with two switches that turn off the two oddities of water: that it is densest at 3.98 °C (39.2 °F, ours), and that its ice floats. You watch temperature by depth and day, ice thickness, and the dates the lake mixes. A "free-time piece about water". Not a water-modeling app in Bob's SWMM sense.
- With both oddities on, in the mild climate the lake mixes twice a year (9 April and 6 November), holds ice from 27 December to 9 April (103 days, at most 1.2 ft, 0.37 m, ft ours), and its bottom holds 4.0 °C (39.2 °F) on 14 February under a 0 °C surface. Heat is checked rather than assumed: the change in stored and latent heat matches the integral of every flux applied, with a residual of 1.5e-7% at the default.
- Heat budget: stored plus latent heat against the integral of every flux applied; residual 1.5e-7% at the default.
- The same model code runs the numbers on screen and the tests behind them.

**Limits it states.** As the page lists it: no snow; no sediment heat flux, inflows, outflows or groundwater; weather as a smooth annual cosine, so dates are climatological, not forecasts; wind mixing is a Kraus-Turner sketch, not a turbulence model; sinking ice is a bottom slab with a fixed heat-transfer coefficient (100 W m-2 K-1), ignoring the 9% volume change; the counterfactual density law continues the 8 °C slope below 3.98 °C; with deep-water mixing at 10^-5 instead of 10^-6 m2/s, the year-on-year build-up of bottom ice in a cold-climate 20 m lake disappears, while in the severe climate it survives a tenfold change.

**Checked at ingest.** 27 December to 9 April is 103 days, as stated (our arithmetic). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Four Degrees at the Bottom (app)](../entities/four-degrees-at-the-bottom.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).
