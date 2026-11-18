---
title: "S238: The Narrow Band, app .md (v1.0.0)"
type: source
raw: raw/apps/narrow-band-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-17
tags: [apps, rainfall, extremes, uncertainty, mevd, gev]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app The Narrow Band, version 1.0.0: a refit of Fatemeh Arab Sadeghabadi's GEV versus MEVD 200-year daily rain comparison on synthetic rain whose true value is known exactly, counting how often each method's 90 % bootstrap band holds the truth. Her R code was ported to JavaScript; the engine works in mm and the page shows inches by default. Raw file: [raw/apps/narrow-band-v1.0.0.md](../../raw/apps/narrow-band-v1.0.0.md).

**How it was written.** The app ships this file. The file says the app was built with Claude in one session in November 2026 at Bob's direction; he chose the post to examine. Claude read the R code, ported it to Python and then JavaScript, designed the truth-known test and two extra rain models, and ran the experiments. Human review: none yet.

**Claims worth keeping** (all copied from the file)
- On her Weibull generator (true 200-year value 4.82 in), the MEVD 90 % band was 0.90 in wide against 2.31 in for GEV, yet held the truth in 28.8 % of 1,000 records against 75.8 % for GEV. A pooled MEVD fit added by the app held it in 78.8 %, with a band 0.66 in wide.
- On the app's two harder rain models the per-year MEVD held the truth in 3.8 % and 14.1 % of records and the pooled fit in 0.0 % on both; GEV held it in 78.7 % and 71.7 %.
- 14 of 14 engine values match a Python port of her R code, at tolerances of 1e-12 to 1e-6.
- True value on the Weibull days: 4.82 in (122.52 mm) by formula, 122.35 mm from 400,000 simulated years.
- Single-year Weibull shape estimates: mean 0.824, standard deviation 0.078, against a true 0.80; thirty identical years with that scatter in the shape read 140.8 mm, against the reference MEVD mean of 139.5 mm. This is the app's diagnosis of the MEVD bias.
- Port against her README on one 150-year record: median 90 % width GEV 69.2 mm, MEVD 22.9 mm; her README gives about 75 mm and 20 to 30 mm.

**Limits it states.** No real gauge data. Days are independent and the climate does not change from year to year. Her R code was ported, not executed. The two extra rain models are the app's own and were chosen to be hard on a Weibull. Only T = 200, 30-year windows and 300 bootstraps were run. No person has reviewed the engine or the essay line by line.

**Checked at ingest.** 2.31 / 0.90 = 2.6, the "2.6 times narrower" of the file. 122.52 mm is 4.824 in. The conversions of mm in the claims are ours where marked. The `links:` line gives Netlify as "none yet"; Netlify reported a finished deploy at https://narrow-band.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [The Narrow Band (app)](../entities/narrow-band.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Negative results](../concepts/negative-results.md).
