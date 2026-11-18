---
title: "S341: ICM Modeller Type, summary written from the page (v1.1.0)"
type: source
raw: raw/apps/icm-modeller-type-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, icm, quizzes]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app ICM Modeller Type, version 1.1.0: the InfoWorks ICM modeller quiz, with its scoring engine opened up. Raw file: [raw/apps/icm-modeller-type-v1.1.0.md](../../raw/apps/icm-modeller-type-v1.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/PpqLDAWbUkZhTJagjGLmEp, version 1792674326-27c4 (index.html, 1,193,363 bytes, SHA-256 4c23f290a9ea9787583fc2a7376e0f7e1c2016bf9937e56fd2039c2f30522e57), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who made the original quiz on Lovable, supplied its source and asked for this version; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A single-file port of Bob's ICM Modeller Type Quiz, a personality quiz for InfoWorks ICM modellers first built on Lovable. Questions, types, scenarios, tips and learning paths were extracted mechanically from the TypeScript source, the scoring functions copied line for line, and an Engine tab added with exact odds, a Monte Carlo check and a defect register.
- Ten answer patterns clicked through the running original give the same type as the port's shipped scoring. The exact odds, computed by a Python program with exact fractions and by the original TypeScript over all 9,834,496 combinations of per-dimension splits, agree with zero difference. Two bugs were measured on the running original: two clicks 60 ms apart on question 1 sent it to question 3, and the scenario simulator, given the first option every time, scored DASP 100%, ADAPTIVE 29% and FLEX 0%.
- Exact odds twice, by two programs, agreeing exactly; the app's own odds engine matches the Python fractions with zero difference in double precision; a Monte Carlo run of 200,000 random answer sheets lands within 2.14 standard errors of the exact figure for every type.
- Corrected scale: a separate exact-fraction program and the app agree across five answer mixes and all 81 letter codes to within 2.6e-15; Monte Carlo of 200,000 sheets within 2.09 standard errors for every result.
- The original installed and run locally in Chromium; ten answer patterns give the same type. Fixed: double taps no longer skip a question (D-05); the scenario simulator no longer reads special type names as letters (D-06).

**Limits it states.** As the page lists it: what kind of modeller you are (no study, no test-retest data); how real modellers spread across the fifteen types (the live app's tally cannot be trusted to say); the corrected scale is a judgment made for this port, checked for symmetry and against chance, not against data; quiz history and badges still record the shipped type.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [ICM Modeller Type (app)](../entities/icm-modeller-type.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [InfoWorks ICM](../entities/infoworks-icm.md).
