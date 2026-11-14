---
title: Overview: what this wiki holds so far
type: synthesis
updated: 2026-11-14
sources: [S01, S04, S05, S06, S10, S19, S20, S22]
tags: [overview]
reviewed: no
---
The state of the wiki after the first ingest, arranged by the six topics of [swmm5.org](entities/swmm5-org.md) [S06](sources/S06-swmm5org-topics-index.md). Twenty-two of 248 raw files are ingested. The wiki is deepest on SWMM's history and on the insides of SWMM 5, thin on ICM, and nearly empty on SWMM6.

## 1. SWMM history
- The timeline from 1969 to 2026 is on [SWMM version history, 1969 to 2026](concepts/swmm-version-history.md), with four places where Bob's own articles disagree with each other or with primary documents.
- [SWMM 1 (1971)](entities/swmm-1.md) is the best-documented subject in the wiki: 12,200 cards rebuilt and scored against six runs printed in 1971, with 14 faults found in the listing [S01](sources/S01-swmm1-engine-app-md.md). The method is on [Verification against printed runs](concepts/verification-against-printed-runs.md).
- [Block architecture and interface files](concepts/block-architecture.md) explains how SWMM 1 to 4 were put together and why that confused people later [S22](sources/S22-li-ten-problems.md).
- [Engine speed, 1988 to 2024](concepts/engine-speed-1988-2024.md): one test model, 5 minutes for 6 simulated hours in 1988 and 5 minutes for 36 simulated years in 2024 [S19](sources/S19-li-edition-29-engine-speed.md).
- People: [Robert (Bob) Dickinson](entities/robert-dickinson.md), [Wayne C. Huber](entities/wayne-huber.md), [Lewis A. (Lew) Rossman](entities/lew-rossman.md).

## 2. Inside SWMM 5
- Hydraulics: [Dynamic wave routing](concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](concepts/kinematic-wave-and-steady-flow.md), [Preissmann slot and surcharge](concepts/preissmann-slot-and-surcharge.md), [Conduit lengthening](concepts/conduit-lengthening.md), [Force main friction](concepts/force-main-friction.md).
- Hydrology: [Runoff surfaces and subarea routing](concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](concepts/subcatchment-width.md), [Infiltration methods](concepts/infiltration-methods.md), [RDII unit hydrographs (RTK)](concepts/rdii-unit-hydrographs.md).
- Output and documentation: [Reading SWMM output](concepts/reading-swmm-output.md), [The missing specification](concepts/the-missing-specification.md).
- The single most-asked subject in 31 years of forum threads is dynamic-wave stability, tied with reading the output, at 224 threads each [S10](sources/S10-openswmm-top25-problems.md). See [The top 25 problems in 31 years of forum threads](concepts/forum-problems-top-25.md).

## 3. SWMM 5 and ICM InfoWorks
- One comparison page, [SWMM 5 versus ICM InfoWorks](concepts/swmm5-versus-icm-infoworks.md), built from four articles. Its numbers on solver differences come from an app's calculators, not from engine runs [S20](sources/S20-li-edition-54-two-solvers.md).
- Entities: [InfoWorks ICM](entities/infoworks-icm.md), [InfoSWMM and InfoSewer](entities/infoswmm-and-infosewer.md), [SWMM and ICM St. Venant comparison (app)](entities/swmm-icm-st-venant-app.md).
- This is where the queue is longest: 141 queued LinkedIn articles name ICM or InfoWorks in the title.

## 4 and 5. ICM and SWMM6; inside SWMM6
- One page, [OpenSWMM 6 and HydroCouple](entities/openswmm-6-and-hydrocouple.md), holding four findings and the HydroCouple measurements. Nothing yet on the solvers, 2D or the input format.

## 6. Comparing models with AI
- The discipline: [Continuity is not validation](concepts/continuity-is-not-validation.md), [The SWMM findings register](concepts/findings-register.md), [Negative results](concepts/negative-results.md).
- The measurements of Bob's own practice: [Six quality markers for app-building work](concepts/app-quality-markers.md) (verification against engine output rose from 28 % to 60 % of app-building conversations between 2026Q2 and 2026Q3 [S05](sources/S05-swmm5org-article-facts.md)) and [App complexity index (HydroCouple = 100)](concepts/app-complexity-index.md).
- Apps as subjects: [SWMM 1 Engine (app)](entities/swmm-1-engine-app.md), [SWMM App Complexity Meter (app)](entities/swmm-app-complexity-meter.md), [Claude chat archive (app)](entities/claude-chat-archive.md).

## Three things the first ingest showed
1. **Bob's published articles contradict each other on dates and credits.** Nineteen items are in [Open questions](open-questions.md). The primary documents (the 1971 listing, EPA's update notes) settle some; others need Bob.
2. **Much of the article text is AI-written, and the newest articles say so while the older ones do not.** Each source page records how it was written. Claims that rest only on an AI-written passage are flagged.
3. **The strongest pages rest on the app .md files and the register, not on the articles.** Those sources carry procedures and numbers. The pattern argues for ingesting every app's .md before the remaining articles.

## What is missing from raw
- The text of the 4,014 OpenSWMM posts (see [OpenSWMM.org (the forum)](entities/openswmm-forum.md)).
- The swmm5.org and swmmfive.com posts.
- The .md of every app except three. Apps built before November 2026 have none.
- The 440 or more Ruby scripts and their READMEs.
- The EPA manuals and the 1971 to 1988 reports, as text.
