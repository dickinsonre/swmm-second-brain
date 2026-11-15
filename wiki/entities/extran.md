---
title: EXTRAN
type: entity
updated: 2026-11-14
sources: [S05, S07, S08, S19, S20, S21, S22, S55, S60]
tags: [swmm-history, hydraulics, engine]
reviewed: 2026-11-15
---
The Extended Transport block: SWMM's dynamic-wave hydraulics before SWMM 5, and the ancestor of SWMM 5's [dynamic wave routing](../concepts/dynamic-wave-routing.md) [S20](../sources/S20-li-edition-54-two-solvers.md).

- **Authors on the 1988 addendum.** Roesner, L.A., Aldrich, J.A. and Dickinson, R.E., "Storm Water Management Model User's Manual Version 4: Extran Addendum", EPA/600/3-88/001b, August 1988 [S19](../sources/S19-li-edition-29-engine-speed.md).
- **The 1981 manual.** CDM published the Extran manual in 1981 with 7 test files that Bob still uses [S55](../sources/S55-swmm-brain-readme.md).
- **When it arrived.** Dynamic wave modeling was first introduced in SWMM 3, in 1981, as the separate module EXTRAN (Extended Transport); the node-link method came from the Sacramento-San Joaquin Delta Model of 1965 and the WRE Transport Model of 1975 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- **How it integrated in time.** Explicitly, by the two-step Modified Euler method; SWMM 5 replaced that with an implicit backward Euler step [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- **Method.** A node-link formulation [S20](../sources/S20-li-edition-54-two-solvers.md).
- **What SWMM 5 kept.** Conduit lengthening, minimum surface area, inertial damping, the surcharge iteration [S22](../sources/S22-li-ten-problems.md), and the EXTRAN surcharge method [S20](../sources/S20-li-edition-54-two-solvers.md).
- **The test models.** The EXTRAN 3 test model of 1981 is Extran1.INP in the OWA-Extran set and has run in SWMM 3, 4 and 5 [S19](../sources/S19-li-edition-29-engine-speed.md). Bob's swmm5.org pages carry Extran1 and Extran2, a SWMM3 orifice test and a SWMM3 weir test as modern files [S07](../sources/S07-swmm5org-topic-swmm-history.md).
- **Rebuilt.** EXTRAN III was rebuilt from the 1981 printed listing and runs in the browser ("EXTRAN III, Alive Again", October 2026) [S07](../sources/S07-swmm5org-topic-swmm-history.md). Per Bob's notes, 139 doubtful listing lines are not yet confirmed against page images [S05](../sources/S05-swmm5org-article-facts.md).

**Disagreements**
- Q14, settled by the EPA reference manual: EXTRAN arrived with SWMM 3 in 1981 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md), as [S55](../sources/S55-swmm-brain-readme.md) also has it. [S21](../sources/S21-li-edition-56-swmm-history.md), which gives SWMM 2 (1975), is the one in error. The October 1971 listing has no such block; see [SWMM 1 (1971)](swmm-1.md).
- Q12, settled: EXTRAN was explicit and SWMM 5's descendant of it is implicit in time but uncoupled in space [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). See [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

**Not in the sources yet.** The EXTRAN equations and surcharge algorithm. Queued: six articles on the EXTRAN manual's test files (2024 to 2025) and Edition 38, "Seven Classic SWMM5 Hydraulics Test Files". The EXTRAN III workbench has no .md in `raw/apps/` yet.
