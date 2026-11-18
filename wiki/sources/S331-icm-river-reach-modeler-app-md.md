---
title: "S331: ICM River Reach Modeler, app .md (v1.1.0)"
type: source
raw: raw/apps/icm-river-reach-modeler-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-18
tags: [apps, icm, swmm5, open-channel, gradually-varied-flow]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app ICM River Reach Modeler, version 1.1.0: steady 1D river reach hydraulics for SWMM5 and InfoWorks ICM modellers. Raw file: [raw/apps/icm-river-reach-modeler-v1.1.0.md](../../raw/apps/icm-river-reach-modeler-v1.1.0.md).

**How it was written.** The app ships this file; Claude added its In three points block on 18 November 2026 when it was packaged for Netlify. Its AI-use section: "Built with Claude (Anthropic). v1.0 (2026-10-25): Claude read the Lovable export, wrote hydro.js and its checks, rebuilt the calculators, corrected the quiz and reference errors, rewrote the Ruby scripts, and wrote the app, the Doc essay and the .docx. v1.1 (2026-11-12): from an outside review Bob supplied, Claude reproduced each calculation finding, fixed it and added checks, read the Autodesk and Innovyze help pages cited and rewrote the ICM guidance and Ruby scripts, built the benchmark and ran it in EPA SWMM 5.2.4, and updated the About tab, the Doc, the .docx and this file."

**Claims worth keeping** (all copied from the file)
- A single-file teaching and checking tool for one-dimensional river reaches, from Bob's Lovable app: it walks through building a reach the way InfoWorks ICM does and gives seven steady-flow calculators (Froude and regime, hydraulic jump, gradually varied flow, culverts by FHWA HDS-5, weirs and orifices, compound channels by the Divided Channel Method, rating curves with SWMM5 .inp import), plus an ICM benchmark reach with the expected water level at every section.
- The benchmark reach's gradually varied flow matches EPA SWMM 5.2.4 within 0.0001 ft over 17 sections for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft); 55 of 55 checks in tests.js pass, and an outside review checked all 36 HDS-5 inlet values against Table A.1.
- Mechanical: 55 of 55 checks in `tests.js` pass on the shipped `hydro.js`.
- Against EPA SWMM 5.2.4 (benchmark reach, run for this build, dry start, 6 h): largest depth difference over 17 sections 0.0001 ft for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft). Steady by the first hour. Flow routing continuity error 0.141% (M1 run, .rpt).
- Defaults for reference: culvert (4 ft RCP, square edge, 175 cfs, 100 ft, S 0.01, TW 2.5 ft) capacity 145.6 cfs at 8 ft; with TW 10 ft, HW at zero flow 9.00 ft and no feasible capacity. M3 preset stops at station 47.9 ft of 1,600. Slot estimate 1.47 cfs (0.29% of 500 cfs).
- By hand: the nine HDS-5 inlet sets match a published reproduction of Table A.1; an outside review (Nov 2026) checked all 36 values against Table A.1 itself and found them right. ICM field names (roughness_Manning, new_panel, left_2d_zone_id, zone_id) checked against Autodesk ICM Help 2027 and the Innovyze help.

**Limits it states.** Steady flow only; no unsteady routing and nothing that tests a Saint-Venant solver. Prismatic sections; no surveyed sections, bridges, expansions or contractions. The Froude tab joins two end depths with a straight line; it is not a profile. Culverts: nine HDS-5 inlet sets, no roadway overtopping, tapered inlets or HY-8 profile types. The 3.5 < X < 4.0 transition is an approximation of a hand-drawn curve. DCM without interface shear over-predicts just above bankfull. No comparison with an ICM run yet. The benchmark tab exists for that. ICM Ruby scripts not run in ICM. WSTableInfo#results_fields is assumed; the scripts stop with a message if it is missing.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet".

**Feeds:** [ICM River Reach Modeler (app)](../entities/icm-river-reach-modeler.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [InfoWorks ICM](../entities/infoworks-icm.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Non-Prismatic Channel Lab (app)](../entities/non-prismatic-channel-lab.md).
