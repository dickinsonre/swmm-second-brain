---
name: Four Degrees at the Bottom
file: four-degrees-at-the-bottom.html
version: 2026-09-30
date: 2026-09-30
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/YSAEfuB3BshqrrWdii3JFJ", repo: none}
engines: none (a one-dimensional lake heat model in the page: Kell 1975 density, bulk surface fluxes, Stefan ice, convective adjustment, Kraus-Turner wind mixing)
units: metric as built (m, °C, W/m2); US customary conversions below are ours
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page carries no AI-use note."
written_from: "the published Claude artifact https://claude.ai/artifact/YSAEfuB3BshqrrWdii3JFJ, version 1790737986-4ee8 (index.html, 55,945 bytes, SHA-256 95e49b4029818c7345bd02422c6eef0edc66200e61a8b8997221d7d55956c5ef), its page read in headless Chromium and from its markup on 2026-11-18. Nothing was run to write this file."
---

# Four Degrees at the Bottom: a lake run a year at a time, with water's two oddities switched off

## In three points
- **What:** A 66-ft (20 m, ft ours) lake run a year at a time from the surface heat budget down, with two switches that turn off the two oddities of water: that it is densest at 3.98 °C (39.2 °F, ours), and that its ice floats. You watch temperature by depth and day, ice thickness, and the dates the lake mixes. A "free-time piece about water". Not a water-modeling app in Bob's SWMM sense.
- **So what:** With both oddities on, in the mild climate the lake mixes twice a year (9 April and 6 November), holds ice from 27 December to 9 April (103 days, at most 1.2 ft, 0.37 m, ft ours), and its bottom holds 4.0 °C (39.2 °F) on 14 February under a 0 °C surface. Heat is checked rather than assumed: the change in stored and latent heat matches the integral of every flux applied, with a residual of 1.5e-7% at the default.
- **Now what:** Use it to show why lakes do not freeze solid. No snow, no sediment heat, no inflows; weather is a smooth annual cosine; and the counterfactual of sinking ice describes a world that does not exist, so there is nothing to calibrate against.

This summary was written after the fact. The page ships no technical summary of its own and gives no version number; the date is the page's own ("Built as a free-time piece about water, 30 September 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Inputs: the two physics switches; climate (mild, cold, severe), mean air temperature (8.0 °C at the default, ±14.0 °C seasonal swing), mean absorbed sunlight (170 W/m2), wind (4.0 m/s); lake depth (20 m), water clarity (light extinction 0.50 /m), deep-water mixing (1.0e-6 m2/s), years to run (3). The top layer trades heat with the air (longwave, sensible, latent) and sunlight is absorbed downward by Beer's law; any layer denser than the one beneath mixes with it, which is where the 4 °C anomaly acts; once a day the wind entrains a layer only when it has the energy to lift the heavier water; ice grows by Stefan's law under a floating lid that cuts off wind mixing.

## Checks (as stated on the page)

- Heat budget: stored plus latent heat against the integral of every flux applied; residual 1.5e-7% at the default.
- The same model code runs the numbers on screen and the tests behind them.

## What this does not show

As the page lists it: no snow; no sediment heat flux, inflows, outflows or groundwater; weather as a smooth annual cosine, so dates are climatological, not forecasts; wind mixing is a Kraus-Turner sketch, not a turbulence model; sinking ice is a bottom slab with a fixed heat-transfer coefficient (100 W m-2 K-1), ignoring the 9% volume change; the counterfactual density law continues the 8 °C slope below 3.98 °C; with deep-water mixing at 10^-5 instead of 10^-6 m2/s, the year-on-year build-up of bottom ice in a cold-climate 20 m lake disappears, while in the severe climate it survives a tenfold change.

## Credits and licenses

Kell (1975) density of pure water; bulk transfer coefficient C = 1.3 x 10^-3; Stefan's ice growth; Kraus and Turner mixing. No license is stated for the page.

## AI use

The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- 2026-09-30: first version (the version read).
