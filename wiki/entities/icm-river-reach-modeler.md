---
title: "ICM River Reach Modeler (app)"
type: entity
updated: 2026-11-18
sources: [S331]
tags: [apps, icm, swmm5, open-channel, gradually-varied-flow]
reviewed: no
---
Bob's app ICM River Reach Modeler: steady 1D river reach hydraulics for SWMM5 and InfoWorks ICM modellers. Version 1.1.0, 2026-11-12 [S331](../sources/S331-icm-river-reach-modeler-app-md.md). Its `links:` line names no live Netlify address [S331](../sources/S331-icm-river-reach-modeler-app-md.md).

**Its source.** [S331](../sources/S331-icm-river-reach-modeler-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S331](../sources/S331-icm-river-reach-modeler-app-md.md)
- A single-file teaching and checking tool for one-dimensional river reaches, from Bob's Lovable app: it walks through building a reach the way InfoWorks ICM does and gives seven steady-flow calculators (Froude and regime, hydraulic jump, gradually varied flow, culverts by FHWA HDS-5, weirs and orifices, compound channels by the Divided Channel Method, rating curves with SWMM5 .inp import), plus an ICM benchmark reach with the expected water level at every section.
- The benchmark reach's gradually varied flow matches EPA SWMM 5.2.4 within 0.0001 ft over 17 sections for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft); 55 of 55 checks in tests.js pass, and an outside review checked all 36 HDS-5 inlet values against Table A.1.
- Mechanical: 55 of 55 checks in `tests.js` pass on the shipped `hydro.js`.
- Against EPA SWMM 5.2.4 (benchmark reach, run for this build, dry start, 6 h): largest depth difference over 17 sections 0.0001 ft for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft). Steady by the first hour. Flow routing continuity error 0.141% (M1 run, .rpt).
- Defaults for reference: culvert (4 ft RCP, square edge, 175 cfs, 100 ft, S 0.01, TW 2.5 ft) capacity 145.6 cfs at 8 ft; with TW 10 ft, HW at zero flow 9.00 ft and no feasible capacity. M3 preset stops at station 47.9 ft of 1,600. Slot estimate 1.47 cfs (0.29% of 500 cfs).
- By hand: the nine HDS-5 inlet sets match a published reproduction of Table A.1; an outside review (Nov 2026) checked all 36 values against Table A.1 itself and found them right. ICM field names (roughness_Manning, new_panel, left_2d_zone_id, zone_id) checked against Autodesk ICM Help 2027 and the Innovyze help.

**How to use it, as the summary puts it.** Use it to learn ICM's river-reach objects and to have an expected answer before building the reach in ICM. Steady, prismatic flow only; no ICM run of the benchmark or of the four Ruby scripts has been made yet. [S331](../sources/S331-icm-river-reach-modeler-app-md.md)

**What it does not show.** Steady flow only; no unsteady routing and nothing that tests a Saint-Venant solver. Prismatic sections; no surveyed sections, bridges, expansions or contractions. The Froude tab joins two end depths with a straight line; it is not a profile. Culverts: nine HDS-5 inlet sets, no roadway overtopping, tapered inlets or HY-8 profile types. The 3.5 < X < 4.0 transition is an approximation of a hand-drawn curve. DCM without interface shear over-predicts just above bankfull. No comparison with an ICM run yet. The benchmark tab exists for that. ICM Ruby scripts not run in ICM. WSTableInfo#results_fields is assumed; the scripts stop with a message if it is missing. [S331](../sources/S331-icm-river-reach-modeler-app-md.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [InfoWorks ICM](infoworks-icm.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Non-Prismatic Channel Lab (app)](non-prismatic-channel-lab.md).
