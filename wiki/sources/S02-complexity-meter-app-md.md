---
title: "S02: SWMM App Complexity Meter, technical summary (app .md, v1.9.1)"
type: source
raw: raw/apps/swmm-app-complexity-meter.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-14
tags: [apps, measurement, hydrocouple]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary of the SWMM App Complexity Meter, version 1.9.1, analyzer 1.7.0, baseline HC-2026-11-10-h. Raw file: [raw/apps/swmm-app-complexity-meter.md](../../raw/apps/swmm-app-complexity-meter.md).

**How it was written.** By Claude under Bob's direction. Bob set the anchor and the rule that HydroCouple = 100. Claude chose the eight dimensions and their weights. The file lists what no person has checked.

**Claims worth keeping**
- The index is a weighted mean of eight counted dimensions: bulk (code tokens, weight 0.15), decisions (0.2), routines (0.1), test markers (0.1), stack (0.1), dependencies (0.1), formats (0.1), SWMM vocabulary (0.15).
- Each dimension is scored on a log scale, 25 points per factor of ten. One tenth of HydroCouple reads about 75.
- The anchor is the HydroCouple GitHub organization: 6,607,205 code tokens, 123,080 decisions, 38,818 routines, 27,339 test markers, 77 outside libraries, 43 file formats, 226 of 226 SWMM 5.2.4 terms.
- Reference scores: EPA Stormwater-Management-Model v5.2.4 69.2, EPANET 70.2, pyswmm 61.5, swmm5-rust 80.3, swmm5-cplus 74.2, SWMM-Explorer 74.6. Peer scores: openswmm.engine 90.1, openswmm.gui 89.1.
- Across 55 repositories the index has a rank correlation of 0.87 with a score from code tokens alone.
- HydroCouple's default branches had 1,019 commits by 13 people in the 12 months to 2026-11-01. EPA SWMM had 0 in the same window, measured at tag v5.2.4.
- The index measures source footprint. It does not measure quality or capability.

**Feeds:** [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md), [SWMM App Complexity Meter (app)](../entities/swmm-app-complexity-meter.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [EPA SWMM 5](../entities/swmm-5.md).
