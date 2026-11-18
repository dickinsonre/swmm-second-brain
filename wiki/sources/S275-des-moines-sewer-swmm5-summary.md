---
title: "S275: Des Moines Sewer to SWMM5, summary written from the page (v1.0)"
type: source
raw: raw/apps/des-moines-sewer-swmm5-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-18
ingested: 2026-11-18
tags: [apps, gis, import, swmm5, wasm, sanitary]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Des Moines Sewer to SWMM5, version 1.0: a bridge from the City of Des Moines' public sewer GIS to an EPA SWMM 5.2 input file by fixed, documented import rules, with EPA SWMM 5.2.4 running in the page and two samples from real city records. Raw file: [raw/apps/des-moines-sewer-swmm5-v1.0.md](../../raw/apps/des-moines-sewer-swmm5-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/2YiGfcdDKaWtVbBvz64Sr7, version 1792405935-f728 (index.html, 1,299,521 bytes, SHA-256 00c0ed9679c59fb11c20242640671f5bde50944e2ea55dc5b08f2d04f7d14a1e), its tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude (Opus 5.5) in October 2026 at Bob's request; he chose the data source and the goal.

**Claims worth keeping** (all copied from the file)
- Sanitary sample: the whole sewershed above manhole CCH030, 34 pipes, 35 structures, 10,869 ft of 8 to 15 in sewer built 1918 to 1979; storm sample: 54 pipes in a box with placeholder subcatchments.
- Routing continuity (native 5.2.4): sanitary as published 6.184%, after two documented adverse-node repairs -0.040%; storm runoff -0.443%, routing 0.621%.
- Native and wasm builds give byte-identical .out files on the sanitary sample; on the storm sample the largest difference is 0.06% of a peak, from different math libraries.
- The 49 storm cells add up to 41.0170 ac, the exact area of the padded box.
- 29 of the 35 sample manhole depths are estimated from assumed cover.

**Limits it states.** Loads, the diurnal pattern, Manning n, storm parameters and the test storm are placeholders; elevations on the city's local datum, unchecked; force mains import as gravity conduits; which record is wrong at the adverse nodes is a question for the city; no person has reviewed the rules.

**Checked at ingest.** The page states the city data terms: data copyright City of Des Moines, Iowa 2025, all rights reserved, reference only; the two samples are small extracts kept for demonstration with credit. The `links:` line gives Netlify as https://des-moines-sewer-swmm5.netlify.app.

**Feeds:** [Des Moines Sewer to SWMM5 (app)](../entities/des-moines-sewer-swmm5.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
