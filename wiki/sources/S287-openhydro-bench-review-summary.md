---
title: "S287: OpenHydro Bench Review, summary written from the page (v1.7)"
type: source
raw: raw/apps/open-hydro-bench-review-v1.7.md
kind: app-md
author: Robert Dickinson
published: 2026-10-18
ingested: 2026-11-18
tags: [apps, benchmarks, review, swmm5, swmm6, verification, leaderboard]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app OpenHydro Bench Review, version 1.7: a review, as an app, of Scott Jeffers's OpenHydro Bench (github.com/scott-jeffers/benchmark1d2d at 8e42875), which Scott asked Bob to run through AI criticism before presenting it to the ASCE stormwater modeling committee; it reruns his SWMM inputs, runner and scorer and rebuilds his leaderboard with his own code. Raw file: [raw/apps/open-hydro-bench-review-v1.7.md](../../raw/apps/open-hydro-bench-review-v1.7.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/TWjyBrd9QSWdXGfz44gAc7, version 1792370624-ad8c (index.html, 7,189,328 bytes, SHA-256 175e0450e4dbd0d82f83ffa41087389b4ece870bae03bd8e24507786baabf488), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says the review and app were built with Claude in a session on 17 October 2026 at Bob's request, with versions to 1.7 on 18 October; responsibility for what is sent to Scott is Bob's. The page header still reads "PRE-ALPHA · PRIVATE"; Bob links it from his swmm5.org AI model comparison page.

**Claims worth keeping** (all copied from the file)
- What holds: 144 of Scott's tests pass (1 skipped); his SWMM numbers for A1F-040 reproduce bit for bit on all three grids; a port of his rating code returns his published ratings for all 22 models.
- On the hump test A1F-040 at the 5 cm (0.16 ft) grid, EPA SWMM 5.2.4 scores 174%: flow off by 83 ft2/s (7.7 m2/s) on average against 47.6 ft2/s (4.42 m2/s); 98.6% of steps never converged and routing continuity was -39%, yet the run is scored. Tightening only HEAD_TOLERANCE and MAX_TRIALS brings the score to 0.078%.
- Weighting every test equally moves OpenSWMM 6 finite volume from rank 1 to 9; the two dam breaks make up 32% of the games behind the rating and the five drainage tests 4%.
- A results file built from the suite's own reference code with no solver run takes first place on the Stoker dam break (0.016%); the review calls this a submission-verification gap, not a fault in the reference solutions.
- On B-RTC-001 two builds of the same SWMM 5.2.4 source put a pump-cycle peak 25.7 h apart.

**Limits it states.** The reference solutions are sound; the gaps are in what the scorer is fed, how it weights tests and how submissions are verified. Bellinge runs dry in the network view because its rain file is a separate download.

**Checked at ingest.** 7.7 / 4.42 = 1.74, the 174% (our arithmetic). Units: the suite works in SI; the page and this summary give US customary beside it. The `links:` line gives Netlify as https://open-hydro-bench-review.netlify.app.

**Feeds:** [OpenHydro Bench Review (app)](../entities/openhydro-bench-review.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md).
