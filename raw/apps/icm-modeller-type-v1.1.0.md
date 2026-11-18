---
name: ICM Modeller Type
file: icm-modeller-type.html
version: 1.1.0
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/PpqLDAWbUkZhTJagjGLmEp", original: "https://icmmodellertype.lovable.app (icm-modellertype; React, Vite and Supabase on Lovable; MIT)", repo: none named in the page}
engines: none (the quiz's scoring functions, copied line for line, and an exact-odds engine written for the page)
units: US customary (scenario texts converted from the original's metric; the UK setting kept)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session in October 2026 under Robert Dickinson's direction. Its Ask tab uses the viewer's own Claude account inside a Claude artifact. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/PpqLDAWbUkZhTJagjGLmEp, version 1792674326-27c4 (index.html, 1,193,363 bytes, SHA-256 4c23f290a9ea9787583fc2a7376e0f7e1c2016bf9937e56fd2039c2f30522e57), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# ICM Modeller Type: the InfoWorks ICM modeller quiz, with its scoring engine opened up

## In three points
- **What:** A single-file port of Bob's ICM Modeller Type Quiz, a personality quiz for InfoWorks ICM modellers first built on Lovable. Questions, types, scenarios, tips and learning paths were extracted mechanically from the TypeScript source, the scoring functions copied line for line, and an Engine tab added with exact odds, a Monte Carlo check and a defect register.
- **So what:** Ten answer patterns clicked through the running original give the same type as the port's shipped scoring. The exact odds, computed by a Python program with exact fractions and by the original TypeScript over all 9,834,496 combinations of per-dimension splits, agree with zero difference. Two bugs were measured on the running original: two clicks 60 ms apart on question 1 sent it to question 3, and the scenario simulator, given the first option every time, scored DASP 100%, ADAPTIVE 29% and FLEX 0%.
- **Now what:** Use it for fun and self-reflection, as the original's own documentation says. It does not show what kind of modeller you are: no study ties the answers to how anyone builds a model, and random answering is a yardstick, not a population.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.1.0"); it gives the build month (October 2026) but no day. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Quiz, Types, Scenarios, Engine, Ask, About, Doc. Blind mode; a Why-this-type trace on every result; the rarity line from exact odds under random answering (the original's Supabase tally is gone, D-11). Version 1.1.0 adds a Corrected scoring switch: shipped scoring stays the default so results match the live app; corrected scoring shows even dimensions as X, reports the exact four-letter code with the nearest written profiles, and puts every special rung at 8 or more of 20 answers (D-01, D-03, D-04). The Ask tab replaces the Lovable chatbot: inside a Claude artifact it uses the viewer's own Claude account; anywhere else, Netlify included, it falls back to an offline phrase router over the same engine tools. History and badges stay in the browser's local storage. Not ported: the Myers-Briggs tab (D-15) and the out-of-date Methodology tab (D-08).

## Checks (as stated on the page)

- Exact odds twice, by two programs, agreeing exactly; the app's own odds engine matches the Python fractions with zero difference in double precision; a Monte Carlo run of 200,000 random answer sheets lands within 2.14 standard errors of the exact figure for every type.
- Corrected scale: a separate exact-fraction program and the app agree across five answer mixes and all 81 letter codes to within 2.6e-15; Monte Carlo of 200,000 sheets within 2.09 standard errors for every result.
- The original installed and run locally in Chromium; ten answer patterns give the same type. Fixed: double taps no longer skip a question (D-05); the scenario simulator no longer reads special type names as letters (D-06).

## What this does not show

As the page lists it: what kind of modeller you are (no study, no test-retest data); how real modellers spread across the fifteen types (the live app's tally cannot be trusted to say); the corrected scale is a judgment made for this port, checked for symmetry and against chance, not against data; quiz history and badges still record the shipped type.

## Credits and licenses

The original ICM Modeller Type Quiz, MIT License, © 2026 Robert Dickinson. Unit conversions in the scenarios are listed on the About tab (for example three 225 mm pipes to three 9-inch pipes; 10 m triangles to 33-ft triangles). The UK setting (Environment Agency, FEH rainfall, BNG coordinates, pounds sterling) is kept.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who made the original quiz on Lovable, supplied its source and asked for this version; responsibility is his. Claude extracted the quiz data, ported the scoring code, wrote the exact-odds engine, the Monte Carlo check and the chat tool registry with their tests, built the page and figures, converted the scenario units, audited the source for the defect register, and wrote the Doc essay. For v1.1.0 Bob chose to add corrected scoring. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1.0 (2026-10): Corrected scoring switch (the version read).
- 1.0.0 (2026-10): single-file port with the Engine and Ask tabs.
