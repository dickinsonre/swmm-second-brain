---
title: Calibration, validation and uncertainty
type: concept
updated: 2026-11-18
sources: [S62, S63, S157, S238, S239, S249, S272, S286, S289]
tags: [calibration, uncertainty, method, verification]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S224 to S242 ingest): a paragraph added near the end, headed Added 17 November 2026 (S238, S239); 2026-11-17 (S243 to S255 ingest): a paragraph added near the end, headed Added 17 November 2026 (S249); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S272, S286, S289)"
---
What it takes to trust a model's number, as [William (Bill) James](../entities/william-james.md) set it out in Rules for Responsible Modeling (2005) and as Bob's [Rules for Responsible Modeling (app)](../entities/rules-for-responsible-modeling-app.md) puts it into practice [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md).

**The ideas, as Bob reports them** [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md)
- Calibration and validation are not the same thing. A good calibration does not excuse skipping the validation run.
- Overfitting: a model with enough adjustable parameters "can be made to fit any dataset". It has fitted the noise with the signal.
- Optimal complexity: as simple as possible but no simpler. His example is a 500 subcatchment model calibrated against two rain gauges.
- Sensitivity analysis: find which parameters matter.
- Uncertainty disclosure: tell the client how much confidence the prediction deserves, not only what it is.
- Do not report six decimal places because the computer printed six.

**The app's worked case turns these into steps** [S62](../sources/S62-rules-for-responsible-modeling-app-md.md)
1. Audit the observations. A spike is flagged when a value is above 5 cfs and more than twice the larger of its neighbours.
2. Calibrate, and score the fit by Nash-Sutcliffe efficiency, peak error, volume error and timing error.
3. Run a seeded ensemble over the uncertain parameters and count how many observations fall inside the 5 to 95 % band.
4. Check that the ensemble is large enough: compare the first half of the runs with all of them.
5. Fill a checklist before reporting.

**The app's thresholds** [S62](../sources/S62-rules-for-responsible-modeling-app-md.md)

| Check | Threshold |
|---|---|
| Nash-Sutcliffe efficiency | at least 0.7 |
| Peak error | within 15 % |
| Volume error | within 10 % |
| Timing error | within 15 min |
| Continuity error | below 1 % |
| Ensemble size | at least 20 runs |
| Observations inside the band | at least 0.8 of them |
| Ensemble converged | median and 95th percentile both change by less than 5 % between half and all runs |

The summary calls these "illustrative rules, not independently sourced standards" [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). They are the app's teaching values. They are not from the book as far as the sources show: the chapter mappings have not been checked against it [S62](../sources/S62-rules-for-responsible-modeling-app-md.md).

**Equifinality.** The app has a teaching helper in which four pairs of Manning n and imperviousness (0.010 and 50 %, 0.013 and 56 %, 0.018 and 66 %, 0.020 and 70 %) are presets of one linear flow formula; each gives 47 cfs (our arithmetic from the formula in the summary) [S62](../sources/S62-rules-for-responsible-modeling-app-md.md).

**The app applies the rule to itself.** Its summary says its 61 passing tests are "measured software checks, not field validation", counts 0 field datasets and 0 published benchmark tables verified, and marks what no person has checked [S62](../sources/S62-rules-for-responsible-modeling-app-md.md).

**Where this meets the rest of the wiki.** [Continuity is not validation](continuity-is-not-validation.md) is the same point for mass balance. [Subcatchment width](subcatchment-width.md) is a fitting knob Bob objects to. Bob's statement that "the model is never the problem" [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md) sits beside engine defects recorded in [The SWMM findings register](findings-register.md) (Q40 in [Open questions](../open-questions.md)).

**Not in the sources yet.** The book's own rules and wording, and any calibration of a real catchment.

**Added 16 November 2026.** A calibration through a learned surrogate, confirmed in SWMM at every step, is on [Calibrating SWMM through a surrogate](calibrating-through-a-surrogate.md). Its first finding: a fit of NSE 0.996 with a conduit roughness multiplier of 0.70 where the truth was 1.10 [S157](../sources/S157-lstm-swmm5-summary.md). The source is a summary Claude wrote from the app page (Q84).

**Added 17 November 2026, second batch.** Two apps measure uncertainty bands against a known truth. [The Narrow Band (app)](../entities/narrow-band.md): a band 2.6 times narrower held the truth less than half as often [S238](../sources/S238-narrow-band-app-md.md). [Hard Meters, Soft Models (app)](../entities/hard-meters-soft-models.md): Bayesian Maximum Entropy blending four meters with a model covered the truth at 99.4 % of unmetered points, and at 61 % when the model was 25 % low but still claimed its usual variance [S239](../sources/S239-hard-meters-soft-models-summary.md). Both are synthetic.

**Added 17 November 2026, third batch.** From the third batch: [SRTC Radio for ICM (app)](../entities/srtc-radio-icm.md) tunes ICM parameter multipliers against an observed hydrograph on a response surface that is linear in the sliders, and checks the tuned run in ICM afterwards; interactions and thresholds are invisible until then [S249](../sources/S249-srtc-radio-icm-summary.md).

**Added 18 November 2026.** Three more apps:
- A gradient-descent walk with EPA 5.2.4 in the loop recovers two knobs on a built-in model, but on extran10 both walkers end pinned at the top of the roughness range with NSE 0.966 and the wrong knobs [S272](../sources/S272-swmm5-walks-downhill-app-md.md).
- A harness that keeps an edit only when held-out scores improve raised its held-out score from 0.496 to 0.807 while a sealed set rose only from 0.637 to 0.715; sealed calibration fell from 0.524 to 0.430 [S286](../sources/S286-exam-first-swmm-harness-summary.md).
- A relay of rule-based agents recovered a planted multiplier (1.257 against 1.25); the file says recovery was expected, because the records came from the same engine [S289](../sources/S289-agent-relay-app-md.md).
