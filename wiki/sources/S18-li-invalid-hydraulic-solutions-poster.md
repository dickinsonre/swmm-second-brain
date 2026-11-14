---
title: "S18: Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5 (2007 poster, LinkedIn 2024)"
type: source
raw: raw/linkedin/2024-12-22-detecting-preventing-invalid-hydraulic-solutions-swmm-dickinson-g5oee.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-12-22
ingested: 2026-11-14
tags: [hydraulics, swmm4, swmm5, history]
reviewed: no
---
**What it is.** Bob's 2024 article about a poster he made with Khalid K. Khan and James T. Smullen of CDM for the 2007 Urban Runoff Modeling Conference at Humboldt State University, comparing the St. Venant terms in SWMM 4 and SWMM 5. Raw file: [raw/linkedin/2024-12-22-detecting-preventing-invalid-hydraulic-solutions-swmm-dickinson-g5oee.md](../../raw/linkedin/2024-12-22-detecting-preventing-invalid-hydraulic-solutions-swmm-dickinson-g5oee.md).

**How it was written.** The article says so itself: one AI system read a photograph of the poster and a second checked the reading against the SWMM5 source. The second flags the first's reading of the term names as inaccurate. The original Publisher file is on an old CDM hard drive. Treat the technical content as a secondhand reading of the poster.

**Claims worth keeping**
- The poster's subject was continuous simulation: use the longest time step that stays stable, and give enough text and graphical feedback to trust the result.
- It plotted flow against the four terms of the dynamic wave equation, called dq1 to dq4 on the poster.
- Per the AI reading, SWMM 4 validated only positive flows, and SWMM 5 checks both positive and negative flows, which prevents unbounded negative flows on adverse slopes.

**Feeds:** [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [EPA SWMM 5](../entities/swmm-5.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md).
