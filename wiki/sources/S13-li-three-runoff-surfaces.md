---
title: "S13: A Tale of Three Runoff Surfaces in SWMM5 (LinkedIn, 2024)"
type: source
raw: raw/linkedin/2024-02-01-tale-three-runoff-surfaces-swmm5-how-used-infoworks-swmm-dickinson-nuoff.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-02-01
ingested: 2026-11-14
tags: [hydrology, swmm5, icm]
reviewed: no
---
**What it is.** A short worked example of how one SWMM5 subcatchment becomes three runoff surfaces in an InfoWorks ICM network. Raw file: [raw/linkedin/2024-02-01-tale-three-runoff-surfaces-swmm5-how-used-infoworks-swmm-dickinson-nuoff.md](../../raw/linkedin/2024-02-01-tale-three-runoff-surfaces-swmm5-how-used-infoworks-swmm-dickinson-nuoff.md). The screenshots are not in the export.

**How it was written.** By Bob; the opening paragraphs read as AI polish.

**Claims worth keeping**
- SWMM5 has three subareas: impervious with depression storage, impervious without depression storage, and pervious with depression storage.
- They are set by two inputs: percent impervious, and the percent of the impervious area with no depression storage. Pervious is 100 minus percent impervious.
- Example: 23 % impervious with 25 % of that having no depression storage converts to InfoWorks runoff surfaces of 17.250 %, 5.750 % and 77.00 %.
- In InfoWorks the three surfaces are tied to the subcatchment through its Land Use ID, all use SWMM runoff, and depression storage is called the initial loss value.

**Feeds:** [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [InfoWorks ICM](../entities/infoworks-icm.md).
