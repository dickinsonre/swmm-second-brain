---
title: "OpenSWMM Code (app)"
type: entity
updated: 2026-11-17
sources: [S205, S257]
tags: [apps, swmm5, source-code, history, versions]
reviewed: no
---
Bob's app OpenSWMM Code: a browsable atlas of the engine source of 34 EPA SWMM5 releases, 5.0.003 (2004) to 5.2.4 (2023), plus CHI's OpenSWMM 5.1.912 fork, with Compare, Evolution, Search and Release notes views. Nothing is compiled or run. Version 1.0.0, 2026-11-05 [S257](../sources/S257-openswmm-code-summary.md). Netlify address: https://openswmm-code.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S257](../sources/S257-openswmm-code-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S257](../sources/S257-openswmm-code-summary.md)
- EPA's GitHub starts at 5.0.022 (a commit dated April 2014); older builds survived as zips in the Internet Archive or on OpenSWMM.org.
- For the 21 releases from EPA's GitHub, all 1,628 files are identical to the tagged commit (line ends aside), and all 21 commit hashes match their tags.
- The page holds 2,519 file slots and stores each of 941 distinct texts once, named by its SHA-1; all 941 pass the check in the browser.
- 11 of EPA's listed builds have no surviving engine source anywhere public: 5.0.001, 5.0.002, 5.0.004, 5.0.005, 5.0.005a, 5.0.005b, 5.0.006, 5.0.006a, 5.0.010, 5.0.019 and 5.0.020.
- For all 34 releases, the highest build number named in their own files equals the release label.
- Five release dates differ from EPA's update history: 5.1.004 (atlas 2014-04-18, EPA 2014-04-14), 5.1.013 (2018-07-31 against 2018-05-10), 5.1.014 (2020-03-16 against 2020-03-01), 5.1.015 (2020-07-20 against 2020-05-01) and 5.2.4 (2023-08-07 against 2023-07-15). The atlas follows the OpenSWMM catalogue and shows EPA's date beside each.

**What it does not show.** The 13 releases from the Internet Archive and OpenSWMM cannot be compared with a primary source. OpenSWMM fork builds 5.1.907 to 5.1.911 are not in the app. Engine source only: the atlas shows what the code says, not what a model does. [S257](../sources/S257-openswmm-code-summary.md)

**Noted at ingest.** 34 - 21 = 13 releases from outside GitHub. Five dates in two sources disagree; the page keeps both, and so does this wiki (Q110). EPA's update history is the primary record for EPA's dates; the atlas follows a catalogue.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [OpenSWMM.org (the forum)](openswmm-forum.md), [EPA SWMM 5](swmm-5.md), [OpenSWMM 3D Code Model (app)](openswmm-3d-code-model.md).
