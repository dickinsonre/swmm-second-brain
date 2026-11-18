---
title: "ICM Modeller Type (app)"
type: entity
updated: 2026-11-18
sources: [S341]
tags: [apps, icm, quizzes]
reviewed: no
---
Bob's app ICM Modeller Type: the InfoWorks ICM modeller quiz, with its scoring engine opened up. Version 1.1.0, 2026-10 [S341](../sources/S341-icm-modeller-type-summary.md). Its `links:` line names no live Netlify address [S341](../sources/S341-icm-modeller-type-summary.md).

**A caution about its source.** The page ships no technical summary. [S341](../sources/S341-icm-modeller-type-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S341](../sources/S341-icm-modeller-type-summary.md)
- A single-file port of Bob's ICM Modeller Type Quiz, a personality quiz for InfoWorks ICM modellers first built on Lovable. Questions, types, scenarios, tips and learning paths were extracted mechanically from the TypeScript source, the scoring functions copied line for line, and an Engine tab added with exact odds, a Monte Carlo check and a defect register.
- Ten answer patterns clicked through the running original give the same type as the port's shipped scoring. The exact odds, computed by a Python program with exact fractions and by the original TypeScript over all 9,834,496 combinations of per-dimension splits, agree with zero difference. Two bugs were measured on the running original: two clicks 60 ms apart on question 1 sent it to question 3, and the scenario simulator, given the first option every time, scored DASP 100%, ADAPTIVE 29% and FLEX 0%.
- Exact odds twice, by two programs, agreeing exactly; the app's own odds engine matches the Python fractions with zero difference in double precision; a Monte Carlo run of 200,000 random answer sheets lands within 2.14 standard errors of the exact figure for every type.
- Corrected scale: a separate exact-fraction program and the app agree across five answer mixes and all 81 letter codes to within 2.6e-15; Monte Carlo of 200,000 sheets within 2.09 standard errors for every result.
- The original installed and run locally in Chromium; ten answer patterns give the same type. Fixed: double taps no longer skip a question (D-05); the scenario simulator no longer reads special type names as letters (D-06).

**How to use it, as the summary puts it.** Use it for fun and self-reflection, as the original's own documentation says. It does not show what kind of modeller you are: no study ties the answers to how anyone builds a model, and random answering is a yardstick, not a population. [S341](../sources/S341-icm-modeller-type-summary.md)

**What it does not show.** As the page lists it: what kind of modeller you are (no study, no test-retest data); how real modellers spread across the fifteen types (the live app's tally cannot be trusted to say); the corrected scale is a judgment made for this port, checked for symmetry and against chance, not against data; quiz history and badges still record the shipped type. [S341](../sources/S341-icm-modeller-type-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [InfoWorks ICM](infoworks-icm.md).
