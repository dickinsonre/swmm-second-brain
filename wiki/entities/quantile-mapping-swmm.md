---
title: "Quantile Mapping to SWMM5 / SWMM6 (app)"
type: entity
updated: 2026-11-17
sources: [S205, S237]
tags: [apps, rainfall, bias-correction, swmm5, swmm6]
reviewed: no
---
Bob's app Quantile Mapping to SWMM5 / SWMM6: an app that shows how quantile mapping corrects a weather model's rainfall, after Niranjan Kumar et al. (2022), Hydrological Sciences Journal 67:6, runs the paper's three variants (EQM, PQM, GPQM) on a synthetic monsoon, and carries a corrected daily total into SWMM through a JavaScript port of SWMM5's runoff routine. The page works in mm/day, as the paper does. Version 1.2, 2026-10-20 [S237](../sources/S237-quantile-mapping-swmm-summary.md). Netlify address: https://quantile-mapping-swmm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S237](../sources/S237-quantile-mapping-swmm-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S237](../sources/S237-quantile-mapping-swmm-summary.md)
- On 2,440 generated monsoon days, observed rain falls on 70 per cent of days and model rain on 92 per cent.
- SWMM5 cannot do quantile mapping: its only rainfall adjustment is one monthly multiplier (Adjust.rainFactor from Adjust.rain[month-1] in climate.c, applied in gage.c), which cannot delete drizzle or stretch a tail. It can use a corrected [TIMESERIES].
- The three corrections and SWMM5's monthly multiplier agree to about 40 mm (1.6 in, our conversion) on the default climate; past the largest training day they extrapolate and diverge.
- The runoff port was compared with EPA SWMM 5.2.4 in 72 numbers, run and rerun while the document was written.
- The paper trained on the IMDAA reanalysis and applied the mapping to NCUM operational forecasts for a Mumbai flood-warning setting.

**What it does not show.** The climate is synthetic. No person has checked the quantile-mapping implementations against the paper, which was unavailable to the build. [S237](../sources/S237-quantile-mapping-swmm-summary.md)

**Noted at ingest.** The page says Bob reviewed the result, while its limits say no person has checked the implementations against the paper; the two need not conflict, but the summary does not say what his review covered.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).
