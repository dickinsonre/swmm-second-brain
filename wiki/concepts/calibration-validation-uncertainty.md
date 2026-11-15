---
title: Calibration, validation and uncertainty
type: concept
updated: 2026-11-14
sources: [S62, S63]
tags: [calibration, uncertainty, method, verification]
reviewed: 2026-11-15
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
