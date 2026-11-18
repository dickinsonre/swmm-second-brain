---
title: "OpenHydro Bench Review (app)"
type: entity
updated: 2026-11-18
sources: [S287]
tags: [apps, benchmarks, review, swmm5, swmm6, verification, leaderboard]
reviewed: no
---
Bob's app OpenHydro Bench Review: a review, as an app, of Scott Jeffers's OpenHydro Bench (github.com/scott-jeffers/benchmark1d2d at 8e42875), which Scott asked Bob to run through AI criticism before presenting it to the ASCE stormwater modeling committee; it reruns his SWMM inputs, runner and scorer and rebuilds his leaderboard with his own code. Version 1.7, 2026-10-18 [S287](../sources/S287-openhydro-bench-review-summary.md). Netlify address, from its `links:` line: https://open-hydro-bench-review.netlify.app [S287](../sources/S287-openhydro-bench-review-summary.md).

**A caution about its source.** The page ships no technical summary. [S287](../sources/S287-openhydro-bench-review-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S287](../sources/S287-openhydro-bench-review-summary.md)
- What holds: 144 of Scott's tests pass (1 skipped); his SWMM numbers for A1F-040 reproduce bit for bit on all three grids; a port of his rating code returns his published ratings for all 22 models.
- On the hump test A1F-040 at the 5 cm (0.16 ft) grid, EPA SWMM 5.2.4 scores 174%: flow off by 83 ft2/s (7.7 m2/s) on average against 47.6 ft2/s (4.42 m2/s); 98.6% of steps never converged and routing continuity was -39%, yet the run is scored. Tightening only HEAD_TOLERANCE and MAX_TRIALS brings the score to 0.078%.
- Weighting every test equally moves OpenSWMM 6 finite volume from rank 1 to 9; the two dam breaks make up 32% of the games behind the rating and the five drainage tests 4%.
- A results file built from the suite's own reference code with no solver run takes first place on the Stoker dam break (0.016%); the review calls this a submission-verification gap, not a fault in the reference solutions.
- On B-RTC-001 two builds of the same SWMM 5.2.4 source put a pump-cycle peak 25.7 h apart.

**What it does not show.** The reference solutions are sound; the gaps are in what the scorer is fed, how it weights tests and how submissions are verified. Bellinge runs dry in the network view because its rain file is a separate download. [S287](../sources/S287-openhydro-bench-review-summary.md)

**Noted at ingest.** 7.7 / 4.42 = 1.74, the 174% (our arithmetic). Units: the suite works in SI; the page and this summary give US customary beside it.

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md).
