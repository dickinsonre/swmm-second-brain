---
title: Continuity is not validation
type: concept
updated: 2026-11-19
sources: [S01, S04, S05, S20, S59, S60, S62, S65, S67, S75, S81, S194, S196, S199, S201, S282, S287, S275, S273, S295, S301, S300, S328, S318, S380]
tags: [verification, method]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end on four more cases (S194, S196, S199, S201); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S282, S287, S275, S273, S295); 2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S301, S300, S328, S318); 2026-11-19 (S377 to S382 ingest): a paragraph added at the end, headed Added 19 November 2026 (S380)"
---
A closed mass balance shows that water was not lost. It does not show that the answer is right. Five cases from the sources:

1. **A sign error that conserves mass perfectly.** With the Audusse well-balancing correction applied to the wrong side of a cell face, still water is destroyed completely while mass conservation is unaffected. After the fix, 39 of 39 analytic cases pass (F-0003, status fixed) [S04](../sources/S04-findings-register-seed.md).
2. **Storage that does not exist.** [Conduit lengthening](conduit-lengthening.md) adds about 106,000 cu ft (3,000 m³ in the source) of storage to 150 short stubs, and continuity closes throughout (F-0007, unconfirmed) [S04](../sources/S04-findings-register-seed.md).
3. **A continuity check that was itself wrong.** In the 1971 listing of [SWMM 1 (1971)](../entities/swmm-1.md), card `HYDR137` leaves `WAREA(J)` out of the pervious storage term. On the Cincinnati deck the printed continuity error is 17.76170 %; with the factor added in an experimental build it is 0.07075 %, and the rest of the printout is identical. The flows were right; the check was wrong [S01](../sources/S01-swmm1-engine-app-md.md).
4. **Two solvers, two typical error bands.** SWMM 5 typically reports 0.1 to 0.5 % and ICM 0.01 to 0.1 %, which the source puts down to ICM's volume accounting at several points per conduit [S20](../sources/S20-li-edition-54-two-solvers.md).
5. **A solver that drops a term on some steps.** In a note not yet rerun, a Green-Ampt run at a 15 s wet step infiltrates 0.868 in where four other step sizes give 1.096 to 1.097 in, and its continuity error is -0.001 % [S67](../sources/S67-note-green-ampt-newton-test-order.md). See [Green-Ampt Newton test order](green-ampt-newton-test-order.md).

**When the check does catch it.** Defect D2 in [LID bio-retention layers](lid-bioretention-layers.md): a drain on a bio-retention cell with no storage layer reports 232.85 in of drain flow from 20.55 in of rain, and the runoff continuity error is -1,100.9 %. The made-up flow is proportional to the drain coefficient, 2.3 in at 0.001 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**The rule the register draws from this.** Its entries say "checked against the engine" rather than "continuity closed" because of this class of bug [S04](../sources/S04-findings-register-seed.md).

**What the EPA manual claims for the continuity error.** Only this: a system continuity error above 5 to 10 percent may be a sign of numerical instability, "although other factors can affect the continuity error as well". [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**The practice is growing.** The share of Bob's app-building conversations that verified against engine output rose from 28 % in 2026Q2 to 60 % in 2026Q3 [S05](../sources/S05-swmm5org-article-facts.md). See [Six quality markers for app-building work](app-quality-markers.md).

**Checks that fail loudly.** The [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) verify script checks each group's case count against a manifest and exits 1 on a missing engine, failed run, missing file, count mismatch or moved number; 1,181 of 1,181 cases passed on 12 November 2026 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**A passing test suite is not validation either.** The summary of the [Rules for Responsible Modeling (app)](../entities/rules-for-responsible-modeling-app.md) reports 61 of 61 tests and a tutorial run with continuity errors of -0.011 % and 0.019 %, and then says: "These are measured software checks, not field validation, native-solver equivalence or engineering approval." The app's own checklist takes continuity below 1 % as one item among several, with validation and a data audit as separate items [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). See [Calibration, validation and uncertainty](calibration-validation-uncertainty.md).

**The rainfall form of the same point.** All 339 patterns of the [World Rainfall Pattern Painter (app)](../entities/world-rainfall-pattern-painter.md) return their depth to within 1.776e-15 in, yet only 3 are benchmarked against published ordinates and 279 are graded Low confidence [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). See [Design storms and temporal patterns](design-storm-patterns.md).

**Added 15 November 2026.** Three more cases from the app summaries. (1) On EXTRAN Example 1 the OpenSWMM 6 finite-volume solver at its default mesh prints a continuity error of 0.000 % and reports no flooding at all, while at 25 ft cells it prints the same 0.000 % and loses 80,673 ft³; six other solutions lose 78,582 to 114,824 ft³, and ZROUTE as distributed, which has a fault of its own, also reports none [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). A closed balance did not make the default-mesh answer agree with anything. (2) In the same study an independent mass balance, worked from each engine's printed hydrograph, agreed with the engine's own continuity figure within 0.03 point in 55 of 59 runs; the four that did not were ZROUTE runs at long time steps [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). (3) On the Bellinge model, EPA SWMM 5.2.4 and OpenSWMM 6 both close routing continuity within 0.35 % on the 48-hour run and report 466 and 61 flooding nodes [S81](../sources/S81-bellinge-summary.md). The Bellinge essay's line: "Agreement between engines is not correctness." See [OpenSWMM 6 solvers, measured](openswmm6-solvers-measured.md).

See also [Verification against printed runs](verification-against-printed-runs.md) and [The SWMM findings register](findings-register.md).

**Added 17 November 2026: four more cases.**
- [SWMM5 RASPIPE](../entities/swmm5-raspipe.md) takes the median routing continuity error of 1,163 corpus models from 0.795 % to 0.005 %. Its page says agreement with Manning, a pump curve and another solver "shows the arithmetic, not whether a model predicts a real sewer", and that nobody has sorted out which engine is right where they disagree [S196](../sources/S196-swmm5-raspipe-summary.md).
- [Seven SWMM Engines](../entities/seven-swmm-engines.md): on Example 1 every engine closes flow continuity within 0.03 percent, while TSS continuity runs from -1.65 % to -85.40 % [S199](../sources/S199-seven-swmm-engines-summary.md).
- [SWMM 4 Twin Engines](../entities/swmm4-twin-engines.md): a printed continuity error of 56.180 % exposed a real Transport defect, and the page adds that "a small continuity error is not a correct answer" [S194](../sources/S194-swmm4-twin-engines-summary.md).
- [swmm5-infosewer](../entities/swmm5-infosewer.md) matches the InfoSewer engine bit for bit, and InfoSewer's own mass balance on the same 2009 network leaves 339,295 ft3 unaccounted, printed as 14.6 percent (Q101). The page says the engine copies InfoSewer's rules, "oddities included" [S201](../sources/S201-infosewer-2009-app-md.md).

**Added 18 November 2026.** More cases from app pages:
- Every dynamic-wave run of a still pool, EPA 5.2.4 included, reads -3.713% routing continuity with every flow zero [S282](../sources/S282-forma-swmm6-summary.md).
- On a benchmark's hump test, EPA SWMM 5.2.4 at settings near its defaults left 98.6% of steps unconverged with -39% continuity, and the benchmark scored the run anyway [S287](../sources/S287-openhydro-bench-review-summary.md).
- A city's sanitary sample as published runs at 6.184% routing continuity; two adverse-node repairs bring it to -0.040% [S275](../sources/S275-des-moines-sewer-swmm5-summary.md).
- Agreement between two engines describes the regime when the physics forces the same answer; the finding is where they part [S273](../sources/S273-agreement-is-the-null-summary.md). A model can close its mass balance and still miss the peak, the timing or the flood extent [S295](../sources/S295-water-modeling-to-3000-summary.md).

**Added 18 November 2026.** More cases from the 18 November uploads:
- OpenSWMM 6 alpha.2 reads -29.401% routing continuity on a run whose link flows match EPA 5.2.4 within 0.30% of each peak [S301](../sources/S301-st-venant-term-budget-summary.md).
- In the 2D Flood Lab the engine's default tier setting brings the flood to one survey point between 400 and 500 s instead of between 200 and 300 s, and every run closes its volume balance, so the continuity line shows none of it [S300](../sources/S300-swmm6-2d-flood-lab-summary.md).
- A scaffolder's continuity regex captured the dot leaders, so every report read 0.00% [S328](../sources/S328-bluesky-icm-summary.md).
- In WNTR Toolkit, EPANET 2.2's tanks are off by 119%, 122% and 53% of their working volume while the run completes [S318](../sources/S318-wntr-toolkit-summary.md).

**Added 19 November 2026.** One more case, outside SWMM. The [Flood Pipeline Audit Bench](../entities/flood-audit-bench.md) re-ran an open-source flood model on a clipped raster: 92.223 % of its stored volume ended in nodata voids, and the reported peak depth was 97.5 ft against 15.1 ft, while the paragraph summary says its continuity error stayed at zero [S380](../sources/S380-flood-audit-bench-app-md.md).
