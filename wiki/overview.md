---
title: Overview: what this wiki holds so far
type: synthesis
updated: 2026-11-14
sources: [S01, S04, S05, S06, S10, S19, S20, S22, S23, S24, S29, S35, S41, S43, S54, S55, S56, S57, S58, S59, S60, S61, S62, S63, S64, S65, S66, S67, S68, S69, S70, S71, S72]
tags: [overview]
reviewed: no
---
The state of the wiki after the first batch of summaries pulled from Bob's Netlify apps, arranged by the six topics of [swmm5.org](entities/swmm5-org.md) [S06](sources/S06-swmm5org-topics-index.md). Seventy-two of 330 raw files are ingested, one of them (the EPA hydraulics manual) in part. The wiki is deepest on SWMM's history, the insides of SWMM 5 and the translations of SWMM 5 and SWMM6; thin on ICM; and on SWMM6 it holds the translations but not yet the solvers.

## 1. SWMM history
- The timeline from 1969 to 2026 is on [SWMM version history, 1969 to 2026](concepts/swmm-version-history.md), with four places where Bob's own articles disagree with each other or with primary documents.
- [SWMM 1 (1971)](entities/swmm-1.md) is the best-documented subject in the wiki: 12,200 cards rebuilt and scored against six runs printed in 1971, with 14 faults found in the listing [S01](sources/S01-swmm1-engine-app-md.md). The method is on [Verification against printed runs](concepts/verification-against-printed-runs.md).
- [Block architecture and interface files](concepts/block-architecture.md) explains how SWMM 1 to 4 were put together and why that confused people later [S22](sources/S22-li-ten-problems.md).
- [Engine speed, 1988 to 2024](concepts/engine-speed-1988-2024.md): one test model, 5 minutes for 6 simulated hours in 1988 and 5 minutes for 36 simulated years in 2024 [S19](sources/S19-li-edition-29-engine-speed.md).
- People: [Robert (Bob) Dickinson](entities/robert-dickinson.md), [Wayne C. Huber](entities/wayne-huber.md), [Lewis A. (Lew) Rossman](entities/lew-rossman.md).

## 2. Inside SWMM 5
- Hydraulics: [Dynamic wave routing](concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](concepts/kinematic-wave-and-steady-flow.md), [Preissmann slot and surcharge](concepts/preissmann-slot-and-surcharge.md), [Conduit lengthening](concepts/conduit-lengthening.md), [Force main friction](concepts/force-main-friction.md).
- Hydrology: [Runoff surfaces and subarea routing](concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](concepts/subcatchment-width.md), [Infiltration methods](concepts/infiltration-methods.md), [RDII unit hydrographs (RTK)](concepts/rdii-unit-hydrographs.md).
- Proposed changes to the engine: [Two-layer soil infiltration (SOIL2)](concepts/two-layer-infiltration.md), and five planned dynamic-wave fixes listed on [Dynamic wave routing](concepts/dynamic-wave-routing.md) [S55](sources/S55-swmm-brain-readme.md).
- A candidate finding from Bob's first template note: [Green-Ampt Newton test order](concepts/green-ampt-newton-test-order.md), a convergence test placed one line too early in `infil.c`; status "working", not rerun [S67](sources/S67-note-green-ampt-newton-test-order.md).
- LID and soils: [LID bio-retention layers](concepts/lid-bioretention-layers.md), [Topsoil over compacted clay](concepts/topsoil-over-compacted-clay.md), [Evaporation during rain (DRY_ONLY)](concepts/evaporation-during-rain.md), and the variant engine [swmm524-perched](entities/swmm524-perched.md). On one soil pair, five SWMM setups capture from 67.1 % (perched with van Genuchten) to 100.0 % (LID with the clay as the storage layer) of the big winter storms, and two 5.2.4 defects, D1 and D2, came out of the study [S59](sources/S59-topsoil-recovery-check-app-md.md).
- Output and documentation: [Reading SWMM output](concepts/reading-swmm-output.md), [The missing specification](concepts/the-missing-specification.md).
- [SWMM5 language translations](entities/swmm5-language-ports.md): EPA SWMM 5.2.4 in 19 languages, each byte-identical to EPA on every gate model it finished; 15 models stopped at the time limit in R and 2 each in Ruby and Perl [S41](sources/S41-swmm5-go-readme.md) [S54](sources/S54-swmm5-r-readme.md). The work measured EPA too: 1,524,961,124 calls to glibc's math over the 480 models, and 43 models that change when glibc uses its generic routines [S41](sources/S41-swmm5-go-readme.md).
- The single most-asked subject in 31 years of forum threads is dynamic-wave stability, tied with reading the output, at 224 threads each [S10](sources/S10-openswmm-top25-problems.md). See [The top 25 problems in 31 years of forum threads](concepts/forum-problems-top-25.md).

## 3. SWMM 5 and ICM InfoWorks
- One comparison page, [SWMM 5 versus ICM InfoWorks](concepts/swmm5-versus-icm-infoworks.md), built from four articles. Its numbers on solver differences come from an app's calculators, not from engine runs [S20](sources/S20-li-edition-54-two-solvers.md).
- Entities: [InfoWorks ICM](entities/infoworks-icm.md), [InfoSWMM and InfoSewer](entities/infoswmm-and-infosewer.md), [SWMM and ICM St. Venant comparison (app)](entities/swmm-icm-st-venant-app.md).
- This is where the queue is longest: 139 queued LinkedIn articles name ICM or InfoWorks in the title.

## 4 and 5. ICM and SWMM6; inside SWMM6
- [OpenSWMM 6 and HydroCouple](entities/openswmm-6-and-hydrocouple.md) now names the commit every translation starts from (88329d6 on `swmm6_rel`, 6.0.0-alpha.4), the licence and the modules, from the translation READMEs [S29](sources/S29-swmm6-rust-readme.md).
- [SWMM6 language translations](entities/swmm6-language-ports.md): thirteen languages, each held byte for byte to the C++ engine on 480 corpus models and 452 extra decks. No translation reports a model that ran to the end and differed [S23](sources/S23-swmm6-csharp-readme.md) [S35](sources/S35-swmm6-ruby-readme.md).
- [swmm6-rust](entities/swmm6-rust.md) is the one that covers 2D: 1,315 of 1,415 gate decks identical with 2D on [S29](sources/S29-swmm6-rust-readme.md).
- Still nothing on how the solvers work, or on ICM against SWMM6.

## 6. Comparing models with AI
- The discipline: [Continuity is not validation](concepts/continuity-is-not-validation.md), [The SWMM findings register](concepts/findings-register.md), [Negative results](concepts/negative-results.md).
- The measurements of Bob's own practice: [Six quality markers for app-building work](concepts/app-quality-markers.md) (verification against engine output rose from 28 % to 60 % of app-building conversations between 2026Q2 and 2026Q3 [S05](sources/S05-swmm5org-article-facts.md)) and [App complexity index (HydroCouple = 100)](concepts/app-complexity-index.md).
- Method from the translations: [Byte-for-byte gate](concepts/byte-for-byte-gate.md) (the parity contract, reruns from clean copies, and runs stopped at a time limit counted as not run) and [Matching glibc math in a translation](concepts/glibc-math-in-translation.md) (19 functions, translated from glibc or called in the system library) [S23](sources/S23-swmm6-csharp-readme.md) [S24](sources/S24-swmm6-go-readme.md).
- From the SWMM5 translations: [What the gate cannot see](concepts/gate-blind-spots.md) (null and positive controls, checked builds, the runtime replayed against glibc because the gate passed a strtod that was wrong on 115,302 of 200,052 cases) and [Where languages part from C](concepts/where-languages-part-from-c.md) [S43](sources/S43-swmm5-pascal-readme.md).
- Apps as subjects: [SWMM 1 Engine (app)](entities/swmm-1-engine-app.md), [SWMM App Complexity Meter (app)](entities/swmm-app-complexity-meter.md), [Claude chat archive (app)](entities/claude-chat-archive.md). The rules they are built to: [App build contract (four working principles)](concepts/app-build-contract.md) [S58](sources/S58-swmm-brain-working-principles.md).
- An idea at seed stage: [A surrogate distilled from SWMM](concepts/surrogate-distilled-from-swmm.md) [S56](sources/S56-swmm-brain-note-surrogate.md).
- A second app as subject, with its own engine variant: [Topsoil Recovery Check (app)](entities/topsoil-recovery-check.md) and [swmm524-perched](entities/swmm524-perched.md) [S59](sources/S59-topsoil-recovery-check-app-md.md).
- Two apps built with Lovable, each from someone else's work Bob learned from, each with its announcing article: [Rules for Responsible Modeling (app)](entities/rules-for-responsible-modeling-app.md), after [William (Bill) James](entities/william-james.md), and [Cost Allocation Game Theory Explorer (app)](entities/cost-allocation-explorer.md), after the 1982 paper with [James P. (Jim) Heaney](entities/james-heaney.md). The subjects are on [Calibration, validation and uncertainty](concepts/calibration-validation-uncertainty.md) and [Cost allocation by cooperative game theory](concepts/cost-allocation-methods.md). Their summaries report tests per file and mark what no person checked [S61](sources/S61-cost-allocation-explorer-app-md.md) [S62](sources/S62-rules-for-responsible-modeling-app-md.md).
- A third Lovable app, on rainfall: [World Rainfall Pattern Painter (app)](entities/world-rainfall-pattern-painter.md), 339 design-storm patterns of which it grades 3 High confidence and 279 Low; the method is on [Design storms and temporal patterns](concepts/design-storm-patterns.md) [S65](sources/S65-world-rainfall-pattern-painter-app-md.md). All three Lovable summaries share one habit worth noting: they write "not checked" where the project holds no record.
- Four apps about the engines themselves: the two Code Houses ([SWMM5](entities/swmm5-code-house.md), [SWMM6](entities/swmm6-code-house.md)), which put the source on walls; [SWMM Engines, Byte for Byte (app)](entities/swmm-engines-byte-for-byte.md), which stores the gate verdicts; and [SWMM Engine What If (app)](entities/swmm-engine-what-if.md), whose version 1.4 rebuilt and re-ran all twenty SWMM 5 translations ([the re-run](concepts/swmm5-ports-rerun-2026-11.md)). The argument they share is on [Wrap, translate or extend](concepts/wrap-translate-or-extend.md) [S70](sources/S70-swmm-engine-what-if-app-md.md).

## Three things the first ingest showed
1. **Bob's published articles contradict each other on dates and credits.** Forty-nine items are in [Open questions](open-questions.md); three were settled on 14 November by the EPA hydraulics manual, the first primary document ingested. The primary documents (the 1971 listing, EPA's update notes) settle some; others need Bob.
2. **Much of the article text is AI-written, and the newest articles say so while the older ones do not.** Each source page records how it was written. Claims that rest only on an AI-written passage are flagged.
3. **The strongest pages rest on the app .md files and the register, not on the articles.** Those sources carry procedures and numbers. The pattern argues for ingesting every app's .md before the remaining articles.

## What is missing from raw
- The contents of Bob's repositories. [Bob's GitHub repositories (where the rest of the material lives)](entities/bobs-github-repositories.md) lists 30 of them from [S57](sources/S57-swmm-brain-setup-script.md) and the topic pages; the six his earlier [swmm-brain](entities/swmm-brain-repo.md) cloned by default are the place to start.
- The text of the 4,014 OpenSWMM posts (see [OpenSWMM.org (the forum)](entities/openswmm-forum.md)).
- The swmm5.org and swmmfive.com posts.
- The .md of most apps. Ten app summaries are ingested and seventeen more app files are queued in `raw/apps/`. Apps built before November 2026 have none.
- The 440 or more Ruby scripts and their READMEs.
- The rest of the EPA documentation. Nine U.S. government reports and the SWMM 4.4 block documentation are now in `raw/manuals/`; one, the hydraulics reference manual, is read in part [S60](sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Still absent: the hydrology volume of the reference manual, and the 1971 to 1988 reports as text (they are scanned PDFs).
