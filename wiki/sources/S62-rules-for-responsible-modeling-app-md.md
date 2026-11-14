---
title: "S62: Rules for Responsible Modeling, technical summary (app .md, v2026.1.2)"
type: source
raw: raw/apps/Rules for Responsible Modeling lessons and browser drainage experiments.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-14
tags: [apps, calibration, uncertainty, swmm5, wasm, verification, lovable]
reviewed: no
---
**What it is.** The technical summary that ships with Rules for Responsible Modeling, version 2026.1.2, a Lovable app at https://rulesforresponsiblemodeling.lovable.app. The app holds chapter lessons, micro-apps, a browser SWMM Playground, a browser-local Model Library and a fictional worked case. Raw file: [raw/apps/Rules for Responsible Modeling lessons and browser drainage experiments.md](../../raw/apps/Rules%20for%20Responsible%20Modeling%20lessons%20and%20browser%20drainage%20experiments.md).

**How it was written.** By Lovable (the AI app builder) from the project's source at commit 22fcc881, a fresh test run and one fresh engine run on 14 November 2026. It records 0 human checks of this revision. Where the code does not record a fact, the summary writes "not checked" and does not fill it in.

**Two faults in how it arrived.** The same content was uploaded twice: this file and `raw/apps/rain-canvas-studio-v2026.1.2.md`, byte for byte the same. Its front matter says `file: rain-canvas-studio`; the summary itself says that identifier was "the requested documentation identifier" and that the code names the product Rules for Responsible Modeling. [S61](S61-cost-allocation-explorer-app-md.md) carries the same line. See Q35 in [Open questions](../open-questions.md).

**Claims worth keeping**
- Engine: EPA SWMM, declared version 5.2.4, as WebAssembly (`public/wasm/swmm5.wasm`, SHA-256 `7a3ac7136a29a629187de122fd529cf690719591e1717471e389ed1113b1304a`), run in a web worker with a 60,000 ms timeout. Source commit, compiler flags and upstream license: not checked. Native against WASM benchmarks run: 0.
- Fresh tutorial run: return code 0, 72 reporting periods, 3.100 in of rain, sampled peak junction depth 1.2856794595718384 ft, sampled peak pipe flow 13.327461242675781 cfs, continuity error -0.011 % runoff and 0.019 % routing. The reference is the project's own input, not a published benchmark.
- Tutorial model: one subcatchment of 5 acres, width 500 ft, 60 % impervious, Horton 3 and 0.5 in/hr; one junction; one 400 ft pipe, 1.5 ft diameter, n = 0.013; DYNWAVE, routing step 15 s, `MAX_TRIALS 8`, `HEAD_TOLERANCE 0.005`, `MIN_SURFAREA 12.557`. Seven half-hour rain intensities 0, 0.5, 1.5, 3, 1, 0.2, 0 in/hr.
- Checks: `bun test tests` with Bun 1.4.4, 61 passed, 0 failed, 5,064 expectation calls, 9 files. No published benchmark table was verified; the tests use helper and structural fixtures.
- Per test file: calibrationCoach 4, chatHistory 3, ensembleSampling 4, modelBuilder 5, modelLibrary 6, modelingMath 7, reviewFixes 9, workedCase 11, workedCaseReview83 12.
- Worked case (fictional; observations are synthetic): three subcatchments of 40, 30 and 25 acres; gauged pipe C3 of 4 ft diameter at slope 0.005; full-pipe Manning capacity 101.57113917082049 cfs at n = 0.013, 73.35693384559258 cfs at n = 0.018, 120.03861902006058 cfs at n = 0.011.
- Fit measures: Nash-Sutcliffe efficiency, peak error, volume error, timing error. Illustrative targets: NSE at least 0.7, peak error within 15 %, volume error within 10 %, timing error within 15 min.
- Checklist thresholds: continuity below 1 %, at least 20 ensemble runs, coverage of observations at least 0.8, band 5 to 95 %, validation and audit recorded. The summary calls these "illustrative rules, not independently sourced standards".
- Ensemble sampling is seeded (mulberry32): Manning n from 0.011 to 0.025, rainfall factor 0.7 to 1.5, imperviousness 45 to 75 %. Run sizes 20, 40, 100, 200. Convergence compares the first half of the runs with all of them at the 0.5 and 0.95 quantiles and needs both changes under 5 %.
- Climate example factors 1.0, 1.1, 1.2, 1.3; the Playground's baseline and double-rain factors 1.0 and 2.0 are "illustrative, not climate projections".
- A chat function, "Ask James", is configured with `google/gemini-3-flash-preview`; it answers from app-written summaries, not verified book text.
- Review log: grades 83/100 (2026-11-02), 85/100 and 80/100 (2026-11-01); reviewer and whether these were AI reviews: not checked.
- Credits as the summary gives them: William James, 2005, Rules for Responsible Modeling, 4th Edition; EPA SWMM. For Manning, Horton, Nash-Sutcliffe and mulberry32 the author and year are "not checked", and the summary says not to attach them from memory.
- License: MIT, Robert Dickinson, 2026. The engine's license file is not kept beside the binary.
- Changes: 2026.1 (2026-11-02), 2026.1.1 and 2026.1.2 (both 2026-11-14).

**Limits it states.** "These are measured software checks, not field validation, native-solver equivalence or engineering approval." 0 field datasets. The 17 chapter mappings to the printed book have not been checked by a person. Unit handling for uploaded models in units other than CFS is not checked.

**Checked at ingest.** Test counts sum to 61. Seven intensities sum to 6.2 in/hr; times 0.5 h gives 3.1 in. Six hours at a 5 min report step is 72 periods. Manning's equation with the stated C3 values gives 101.57, 73.36 and 120.04 cfs.

**Feeds:** [Rules for Responsible Modeling (app)](../entities/rules-for-responsible-modeling-app.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [William (Bill) James](../entities/william-james.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [EPA SWMM 5](../entities/swmm-5.md).
