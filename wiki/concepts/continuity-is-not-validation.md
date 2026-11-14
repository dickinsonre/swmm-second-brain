---
title: Continuity is not validation
type: concept
updated: 2026-11-14
sources: [S01, S04, S05, S20, S59, S60, S62]
tags: [verification, method]
reviewed: no
---
A closed mass balance shows that water was not lost. It does not show that the answer is right. Four cases from the sources:

1. **A sign error that conserves mass perfectly.** With the Audusse well-balancing correction applied to the wrong side of a cell face, still water is destroyed completely while mass conservation is unaffected. After the fix, 39 of 39 analytic cases pass (F-0003, status fixed) [S04](../sources/S04-findings-register-seed.md).
2. **Storage that does not exist.** [Conduit lengthening](conduit-lengthening.md) adds about 106,000 cu ft (3,000 m³ in the source) of storage to 150 short stubs, and continuity closes throughout (F-0007, unconfirmed) [S04](../sources/S04-findings-register-seed.md).
3. **A continuity check that was itself wrong.** In the 1971 listing of [SWMM 1 (1971)](../entities/swmm-1.md), card `HYDR137` leaves `WAREA(J)` out of the pervious storage term. On the Cincinnati deck the printed continuity error is 17.76170 %; with the factor added in an experimental build it is 0.07075 %, and the rest of the printout is identical. The flows were right; the check was wrong [S01](../sources/S01-swmm1-engine-app-md.md).
4. **Two solvers, two typical error bands.** SWMM 5 typically reports 0.1 to 0.5 % and ICM 0.01 to 0.1 %, which the source puts down to ICM's volume accounting at several points per conduit [S20](../sources/S20-li-edition-54-two-solvers.md).

**When the check does catch it.** Defect D2 in [LID bio-retention layers](lid-bioretention-layers.md): a drain on a bio-retention cell with no storage layer reports 232.85 in of drain flow from 20.55 in of rain, and the runoff continuity error is -1,100.9 %. The made-up flow is proportional to the drain coefficient, 2.3 in at 0.001 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**The rule the register draws from this.** Its entries say "checked against the engine" rather than "continuity closed" because of this class of bug [S04](../sources/S04-findings-register-seed.md).

**What the EPA manual claims for the continuity error.** Only this: a system continuity error above 5 to 10 percent may be a sign of numerical instability, "although other factors can affect the continuity error as well". [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**The practice is growing.** The share of Bob's app-building conversations that verified against engine output rose from 28 % in 2026Q2 to 60 % in 2026Q3 [S05](../sources/S05-swmm5org-article-facts.md). See [Six quality markers for app-building work](app-quality-markers.md).

**Checks that fail loudly.** The [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) verify script checks each group's case count against a manifest and exits 1 on a missing engine, failed run, missing file, count mismatch or moved number; 1,181 of 1,181 cases passed on 12 November 2026 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**A passing test suite is not validation either.** The summary of the [Rules for Responsible Modeling (app)](../entities/rules-for-responsible-modeling-app.md) reports 61 of 61 tests and a tutorial run with continuity errors of -0.011 % and 0.019 %, and then says: "These are measured software checks, not field validation, native-solver equivalence or engineering approval." The app's own checklist takes continuity below 1 % as one item among several, with validation and a data audit as separate items [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). See [Calibration, validation and uncertainty](calibration-validation-uncertainty.md).

See also [Verification against printed runs](verification-against-printed-runs.md) and [The SWMM findings register](findings-register.md).
