---
title: "Des Moines Sewer to SWMM5 (app)"
type: entity
updated: 2026-11-18
sources: [S275]
tags: [apps, gis, import, swmm5, wasm, sanitary]
reviewed: no
---
Bob's app Des Moines Sewer to SWMM5: a bridge from the City of Des Moines' public sewer GIS to an EPA SWMM 5.2 input file by fixed, documented import rules, with EPA SWMM 5.2.4 running in the page and two samples from real city records. Version 1.0, 2026-10-18 [S275](../sources/S275-des-moines-sewer-swmm5-summary.md). Netlify address, from its `links:` line: https://des-moines-sewer-swmm5.netlify.app [S275](../sources/S275-des-moines-sewer-swmm5-summary.md).

**A caution about its source.** The page ships no technical summary. [S275](../sources/S275-des-moines-sewer-swmm5-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S275](../sources/S275-des-moines-sewer-swmm5-summary.md)
- Sanitary sample: the whole sewershed above manhole CCH030, 34 pipes, 35 structures, 10,869 ft of 8 to 15 in sewer built 1918 to 1979; storm sample: 54 pipes in a box with placeholder subcatchments.
- Routing continuity (native 5.2.4): sanitary as published 6.184%, after two documented adverse-node repairs -0.040%; storm runoff -0.443%, routing 0.621%.
- Native and wasm builds give byte-identical .out files on the sanitary sample; on the storm sample the largest difference is 0.06% of a peak, from different math libraries.
- The 49 storm cells add up to 41.0170 ac, the exact area of the padded box.
- 29 of the 35 sample manhole depths are estimated from assumed cover.

**What it does not show.** Loads, the diurnal pattern, Manning n, storm parameters and the test storm are placeholders; elevations on the city's local datum, unchecked; force mains import as gravity conduits; which record is wrong at the adverse nodes is a question for the city; no person has reviewed the rules. [S275](../sources/S275-des-moines-sewer-swmm5-summary.md)

**Noted at ingest.** The page states the city data terms: data copyright City of Des Moines, Iowa 2025, all rights reserved, reference only; the two samples are small extracts kept for demonstration with credit.

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
