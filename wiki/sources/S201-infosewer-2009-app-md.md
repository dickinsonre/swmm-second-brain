---
title: "S201: InfoSewer_2009, technical summary (app .md, v1.2.0)"
type: source
raw: raw/apps/InfoSewer_2009-v1.2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-17
tags: [apps, infosewer, swmm5, engine, pumps, force-mains, 3d, verification]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** The technical summary that ships with InfoSewer_2009, version 1.2.0 (12 November 2026): a 3D viewer of one 2009 InfoSewer sewer model, colored with steady-state and 24-hour extended period results from swmm5-infosewer, Bob's EPA SWMM 5.2.4 with InfoSewer's routing rules as `FLOW_ROUTING INFOSEWER`. The page runs no engine. Raw file: [raw/apps/InfoSewer_2009-v1.2.0.md](../../raw/apps/InfoSewer_2009-v1.2.0.md).

**How it was written.** By Claude (Anthropic) in Claude Code sessions in November 2026, under Bob's direction. Bob chose the project, supplied the InfoSewer engine source and the 2009 model from his files, and set the method: write up the engine's rules, then match its output value for value. Claude wrote the InfoSewer routines in swmm5-infosewer, the converters, the page, the essay and this file. Checks are mechanical, except a look at screenshots. No person has reviewed the page's code, compared the geometry with the utility's GIS, or checked the 2009 data against today's system.

**A note on what this page leaves out.** The summary says the model is "a real utility's network" and asks that the app stay private unless the utility agrees. Version 1.2.0 removed the utility's name and the plan-coordinate offsets. This wiki names neither.

**Claims worth keeping**
- Engine: swmm5-infosewer, commit 12492d6, base EPA SWMM 5.2.4, option `FLOW_ROUTING INFOSEWER`; repository SWMMBobSWMM6/swmm5-infosewer, private. Reference: the InfoSewer engine (HeEngPkg), MWH Soft / Innovyze 1996 to 2011, proprietary. The InfoSewer rules are written up with source file and line references in the repo's `docs/spec_steady.md`, `docs/spec_eps.md` and `docs/spec_pressure.md`.
- Engine against the InfoSewer engine built from its source, on this network: 58,487 of 58,487 steady-state values and 900,500 of 900,500 EPS values identical in every bit. Whole test set: 11,894,156 values, all identical except LPS and MLD models within 4.2e-11.
- The model (June 17, 2009): 2,250 gravity pipes (125.5 mi), 5 force mains (5.85 mi), 693,463 ft of pipe (131.3 mi) in all; 2,231 loading manholes; 5 junction chambers, 5 wet wells, 3 outfalls; 9 pumps in 5 stations; diameters 7.0 to 60 in; inverts 4,947.66 to 5,440.0 ft (492 ft of fall).
- Rules: pump curve `H = H0 - a Q^b`; force main loss by Hazen-Williams `hL = 4.727 L Q^1.852 / (C^1.852 D^4.871)` (Q in cfs, L and D in ft); station flow where pump head equals static lift plus loss. Steady state reports force main flow equal to station inflow and head loss at the pump flow (InfoSewer "Pump Flow Continuity" 0). EPS steps each wet well on a 1-minute pump step with level switching (on at max level, off at min level) and reports hourly.
- Stations, steady state: from 68 gpm at 46.65 ft of pump head (two point pumps, 8 in force main 2,385 ft long) to 10,960 gpm at 283.63 ft (one point pump, 30 in force main 20,249 ft long, 81.03 ft of loss).
- Steady state: 33 of 2,250 gravity pipes surcharged; 11,987 gpm to the three outfalls (3,615, 402 and 7,970).
- EPS: 12 to 44 surcharged pipes across the 25 report times; the largest outfall peaks at 10,850 gpm at hour 18 (steady 7,970). Station WW3 is on in 6 of 25 hourly snapshots at about 11,070 gpm, inflow peak 4,716 gpm.
- InfoSewer mass balance, EPS: in 2,310,736 ft3, out 1,579,256, pipe storage 385,715, wet wells 10,492 to 16,962, unaccounted 339,295 (14.6 percent).
- Independent checks: the WW303 operating point solved again by bisection, 4,327 gpm at 24.16 ft, against the engine's 4,326 gpm at 24.16 ft; station WW3, 5,039.86 + 283.63 - 81.03 = 5,242.46 ft, the force main outlet crown. Packed data against the engine CSVs: 293,272 values within the rounding.
- Source-data defect: pipe P-8076 has inverts of 0.00 ft. The app draws it 10 ft below the rim and flags it; the engine used 0.00 as given.

**Limits it states.** "It is not a second opinion on InfoSewer." The engine copies InfoSewer's rules, oddities included. Hourly snapshots only. Exaggerated elevation and pipe size. No terrain. The 2009 model has not been compared with the present system. Two engine paths have no reference case: a bisection after Newton fails, and a gravity pipe leaving a wet well. Not tested on a real GPU, a real phone or in Claude's artifact viewer.

**Checked at ingest.** 3,615 + 402 + 7,970 = 11,987. 2,310,736 - 1,579,256 - 385,715 - (16,962 - 10,492) = 339,295, as printed; but 339,295 / 2,310,736 is 14.68 percent, not 14.6 (Q101). 693,463 ft / 5,280 = 131.3 mi.

**Feeds:** [swmm5-infosewer](../entities/swmm5-infosewer.md), [InfoSewer_2009 (app)](../entities/infosewer-2009.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Force main friction](../concepts/force-main-friction.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Open questions](../open-questions.md).
