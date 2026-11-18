---
name: OpenHydro Bench Review
file: open-hydro-bench-review.html
version: "1.7"
date: 2026-10-18
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://open-hydro-bench-review.netlify.app", artifact: "https://claude.ai/artifact/TWjyBrd9QSWdXGfz44gAc7", reviewed_repo: "https://github.com/scott-jeffers/benchmark1d2d at 8e42875"}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "reruns of Scott Jeffers's committed inputs, made while building the review"}
  - {name: OpenSWMM, version: "6, swmm6_rel built from source on 17 Oct 2026 (3c30f1e for the network view)", license: Apache-2.0, note: "dynamic wave as shipped, dynamic wave with ANDERSON_ACCEL, SEMI_IMPLICIT and DYNAMIC_SLOT, and finite volume; plus the SWMM 5.3 legacy engine"}
units: the reviewed suite works in SI; the Doc gives US customary beside it, and this summary puts US first where the page gives both
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the review and app were built with Claude in a session on 17 October 2026 at Robert Dickinson's request, with later versions to 18 October. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TWjyBrd9QSWdXGfz44gAc7, version 1792370624-ad8c (index.html, 7,189,328 bytes, SHA-256 175e0450e4dbd0d82f83ffa41087389b4ece870bae03bd8e24507786baabf488), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# OpenHydro Bench Review: a review of Scott Jeffers's 1D-2D benchmark suite, with the output checked

## In three points
- **What:** A review, as an app, of Scott Jeffers's OpenHydro Bench (github.com/scott-jeffers/benchmark1d2d at 8e42875), which Scott asked Bob to run through AI criticism privately before presenting it to the ASCE stormwater modeling committee in mid-November 2026. It reruns his SWMM inputs, his runner and his scorer, and rebuilds his leaderboard with his own code.
- **So what:** The machinery holds: 144 tests pass (1 skipped), his SWMM numbers reproduce bit for bit, and a port of his rating code returns his published ratings for all 22 models. What it is fed and how it is weighted are not ready: on the finest hump grid at settings close to SWMM's defaults, 98.6% of steps never converged and routing continuity was -39%, yet the run is scored; on calm flow over a hump (A1F-040, 5 cm or 0.16 ft grid) EPA SWMM 5.2.4 scores 174%, the larger of its depth and flow errors, and tightening only HEAD_TOLERANCE and MAX_TRIALS brings that to 0.078%; weighting every test equally moves OpenSWMM 6 finite volume from rank 1 to 9; a results file built without any solver run takes first place on the Stoker dam break.
- **Now what:** The review lists five fixes in order: read SWMM's convergence report and print four validity checks on every card; choose the weighting on purpose; take Track B off the physics rating; keep submitted results off the ranked board until reproduced; freeze one scoring method and print its version.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.7 · 18 Oct 2026 · repo 8e42875"). The page's header still reads "PRE-ALPHA · PRIVATE"; Bob links it from his swmm5.org AI model comparison page. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Verdict, Tests & gaps, SWMM networks, SWMM rerun, OpenSWMM, Leaderboard, Can it be faked?, Corpus, Findings, His questions, Letter, Doc, Ask, About. Tests & gaps draws what each of Scott's 39 tests checks and misses; the 19 tests that carry a SWMM model get a network view coloured by depth and flow through the run, from his inputs rerun on EPA SWMM 5.2.4 and OpenSWMM 6. Every finding has an evidence drawer (claim, input, settings, raw report, scoring command, result, limitation, with verbatim .rpt excerpts) and there is a reproduction package.

## Findings the page reports

- F1: SWMM 5.2.4, calm flow over a hump (A1F-040) on the 5 cm (0.16 ft) grid: score 174% to 0.078% with only HEAD_TOLERANCE and MAX_TRIALS tightened. The 174% is the flow error: off by 83 ft2/s (7.7 m2/s) on average against the 47.6 ft2/s (4.42 m2/s) the channel should carry; depths were off by 4.77 ft (1.45 m), 74% of the 6.46 ft (1.97 m) mean depth.
- F2: OpenSWMM 6 finite volume: rank 1 to 9 when every test counts the same (Scott's code, his data).
- F4: a forged Stoker submission, built from the suite's own reference code with no solver run: 0.016% error, first place on A1F-011. The page calls this a submission-verification gap, not a fault in the reference solutions.
- Weighting: each pair of models on a test is one game, so the two dam breaks make up 32% of the games behind the rating and the five drainage tests 4%.
- Track B: on B-RTC-001 two builds of the same SWMM 5.2.4 source put a pump-cycle peak 25.7 h apart.
- Three scoring rules in 48 hours.

## Checks (as stated on the page)

A clean clone at 8e42875 ran Scott's test suite: 144 passed, 1 skipped, 8 s. His committed SWMM inputs for A1F-040 reproduce his published depth errors bit for bit on all three grids in EPA 5.2.4 and OpenSWMM 6 DW. A JavaScript port of his rating code returns his published ratings. Version 1.4 applied a second outside review Bob supplied (A- technical, B- deployment).

## What this does not show

The page says the reference solutions themselves are sound; the gaps are in what the scorer is fed, how it weights tests and how submissions are verified. Bellinge runs dry in the network view because its rain file is a separate download. The cost of the tighter settings is measured in timed reruns on the page.

## How to reproduce

The reproduction package on the page carries the .inp and raw .rpt files, run and scoring scripts, versions, expected outputs and a checker.

## Credits and licenses

Scott Jeffers's OpenHydro Bench (benchmark1d2d); EPA SWMM 5.2.4 (public domain); OpenSWMM 6 (HydroCouple, Apache-2.0). No license is stated for the page.

## AI use

The page says: the review and app were built with Claude, Anthropic's AI model, in a session on 17 October 2026 at Bob Dickinson's request; Bob chose the subject and the questions, and responsibility for what is sent to Scott is his. Claude cloned the repository and the EPA source, ran the test suite, reran the SWMM inputs with option variants, built OpenSWMM from source and reran Scott's tests three ways, rebuilt the leaderboard with his own code, and wrote the page; version 1.7 adds a Doc essay of about 6,600 words in the manner of Isaac Asimov, written by Claude in the first person and quoting nothing of Asimov's. An Ask tab sends questions to a model through a passcode-protected function. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.7 (2026-10-18): Doc tab essay (the version read).
- 1.6: SWMM networks tab. 1.5: network view on Tests & gaps. 1.4: second outside review applied. 1.3: Tests & gaps tab. 1.2: three SWMM6 set-ups.
