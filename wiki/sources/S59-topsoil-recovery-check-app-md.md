---
title: "S59: Topsoil Recovery Check, technical summary (app .md, 2026-11-12)"
type: source
raw: raw/apps/topsoil-recovery-check.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-14
tags: [swmm5, lid, infiltration, swmm6, verification, apps]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with the Topsoil Recovery Check page, version 2026-11-12. The page asks how much of a storm 4 in of decompacted, amended topsoil over 24 in of compacted sandy clay captures in SWMM, winter and summer, under several SWMM setups. Raw file: [raw/apps/topsoil-recovery-check.md](../../raw/apps/topsoil-recovery-check.md).

**How it was written.** By Claude (Anthropic) at Bob's request. Its AI-use section says Claude compiled the engines, read the infiltration and LID source, wrote the swmm524-perched change, ran the simulations and the verify script, and wrote the page and the summary; Bob set the question and reviews the conclusions. The numbers come from the build's own test runs (verify.py, 12 Nov 2026). The people who raised the question are not named in it.

**Claims worth keeping**
- Soils, stated as assumptions: topsoil 4 in, porosity 0.50, FC 0.30, WP 0.15, Ksat 1.0 in/hr; compacted sandy clay 24 in, porosity 0.430, FC 0.321, WP 0.221, Ksat 0.01 in/hr (Rawls, Ksat halved).
- Big-storm capture (storms of 0.75 in and larger), dormant / growing season: Modified Horton 76.6 / 77.9 %; Modified Horton over an impermeable clay 70.8 / 72.7 %; Modified Horton with MaxInfil 6.7 / 11.0 %; LID with the clay as the storage layer 100.0 / 100.0 %; LID with no storage layer, seepage = clay Ksat, 79.3 / 95.0 %; perched engine 83.0 / 97.1 %; perched with van Genuchten 67.1 / 96.9 %.
- VG ablation, dormant: full VG 67.1 %; restoring the topsoil or SOIL2 field-capacity floor or direct SOIL2 ET moves it by 0.1 point or less; no upward flow 71.1; FC-based head 68.3; the outline's step rule 59.4; all five perched rules 72.3.
- Defect D1: Modified Horton with MaxInfil > 0 in EPA 5.2.4, `infil.c` line 545, `infil->Fe = MAX(infil->Fe, infil->Fmax)`: 4.0 in of rain infiltrates 0.002 in. Fixed in OpenSWMM 5.3.0; ported to 5.2.4 as the "MaxInfil fix" engine. On the 8 in storm the capped Modified Horton infiltrates 0.001 in in 5.2.4 and 3.00 in with the fix.
- Defect D2: a DRAIN line on a bio-retention LID with no storage layer makes water. Winter season, coefficient 0.1: 232.85 in of drain flow from 20.55 in of rain, runoff continuity error -1,100.9 %, in EPA 5.2.4, OpenSWMM 5.3.0-beta.3 and 6.0.0-alpha.4. Proportional to the coefficient (2.3 in at 0.001). Not fixed in any engine on the page.
- `lidproc.c getEvapRates()` sets SoilEvap to 0 whenever SurfaceInfil > 0; OpenSWMM 6 keeps the rule (`LID.cpp` line 907). So `DRY_ONLY YES` changes big-storm capture by 1.3 points at most, and by 0.4 at most in the LID and perched setups.
- Depression storage as the topsoil bowl (Horton, f0 = fmin = 0.01 in/hr): dormant big-storm capture 27.6 % at 0.2 in, 75.2 % at 0.8 in, 95.5 % at 1.4 in.
- A 3 in/hr test on the two-layer profile falls below 0.1 in/hr after 20 to 82 minutes, depending on setup and starting moisture.
- The study clay's porosity 0.43 implies a bulk density of 1.51 g/cc (94 lb/ft³) at a particle density of 2.65.
- OpenSWMM 6.0.0-alpha.4 ignores an unknown LID layer keyword (SOIL2) instead of reporting it; an issue was drafted with a tested patch.
- verify.py, 12 Nov 2026: 1,181 of 1,181 cases passed in 94 s, in seven groups with expected counts; it exits 1 on a missing engine, failed run, missing file, count mismatch or moved number. All five WebAssembly engines rebuilt byte-identical from pinned sources with Zig 0.17.0.
- Engines and pins: EPA 5.2.4 tag v5.2.4 (7952ca83); swmm524-perched branch van-genuchten (548e5fbf); OpenSWMM swmm6_rel 13746831 (Apache-2.0).

**Limits it states.** No calibration to a site; one soil pair; synthetic storm trains with rain in 3.5 % of hours; no matched HYDRUS comparison yet; GMAX = 10 is a supplied value.

**Feeds:** [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md), [swmm524-perched](../entities/swmm524-perched.md), [Topsoil over compacted clay](../concepts/topsoil-over-compacted-clay.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md), [Evaporation during rain (DRY_ONLY)](../concepts/evaporation-during-rain.md), [Infiltration methods](../concepts/infiltration-methods.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [The SWMM findings register](../concepts/findings-register.md), [EPA SWMM 5](../entities/swmm-5.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [OpenSWMM.org (the forum)](../entities/openswmm-forum.md).
