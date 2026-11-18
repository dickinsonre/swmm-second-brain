---
title: "S237: Quantile Mapping to SWMM5 / SWMM6, summary written from the page (v1.2)"
type: source
raw: raw/apps/quantile-mapping-swmm-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-17
tags: [apps, rainfall, bias-correction, swmm5, swmm6]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Quantile Mapping to SWMM5 / SWMM6, version 1.2: an app that shows how quantile mapping corrects a weather model's rainfall, after Niranjan Kumar et al. (2022), Hydrological Sciences Journal 67:6, runs the paper's three variants (EQM, PQM, GPQM) on a synthetic monsoon, and carries a corrected daily total into SWMM through a JavaScript port of SWMM5's runoff routine. The page works in mm/day, as the paper does. Raw file: [raw/apps/quantile-mapping-swmm-v1.2.md](../../raw/apps/quantile-mapping-swmm-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792508736-2add, reading its tabs and Doc in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says Bob directed the work, chose the paper, required that physics claims be checked against a compiled engine and reviewed the result; Claude (Opus 5) built the page in September 2026 and wrote the document in October 2026.

**Claims worth keeping** (all copied from the file)
- On 2,440 generated monsoon days, observed rain falls on 70 per cent of days and model rain on 92 per cent.
- SWMM5 cannot do quantile mapping: its only rainfall adjustment is one monthly multiplier (Adjust.rainFactor from Adjust.rain[month-1] in climate.c, applied in gage.c), which cannot delete drizzle or stretch a tail. It can use a corrected [TIMESERIES].
- The three corrections and SWMM5's monthly multiplier agree to about 40 mm (1.6 in, our conversion) on the default climate; past the largest training day they extrapolate and diverge.
- The runoff port was compared with EPA SWMM 5.2.4 in 72 numbers, run and rerun while the document was written.
- The paper trained on the IMDAA reanalysis and applied the mapping to NCUM operational forecasts for a Mumbai flood-warning setting.

**Limits it states.** The climate is synthetic. No person has checked the quantile-mapping implementations against the paper, which was unavailable to the build.

**Checked at ingest.** The page says Bob reviewed the result, while its limits say no person has checked the implementations against the paper; the two need not conflict, but the summary does not say what his review covered. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://quantile-mapping-swmm.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Quantile Mapping to SWMM5 / SWMM6 (app)](../entities/quantile-mapping-swmm.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).
