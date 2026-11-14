---
title: SWMM6 Code House (app)
type: entity
updated: 2026-11-14
sources: [S69, S72]
tags: [apps, swmm6, source-code, openswmm, verification]
reviewed: no
---
Bob's walkable 3D map of the OpenSWMM 6 engine source (see [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md)). Version 1.2.1 [S69](../sources/S69-swmm6-code-house-app-md.md). Its sister app is the [SWMM5 Code House (app)](swmm5-code-house.md).

**What it is not.** "It is not an OpenSWMM release, it holds no compiled engine, and it does not run a model" [S69](../sources/S69-swmm6-code-house-app-md.md). It is not endorsed by HydroCouple or USEPA [S72](../sources/S72-li-swmm6-code-house-article.md).

**The house.** 102 rooms on 9 floors hold 351,187 lines in 675 files, with 6,683 functions and 427 doorways, from OpenSWMM 6.0.0-alpha.4, branch `swmm6_rel`, commit 9648837 [S69](../sources/S69-swmm6-code-house-app-md.md). The floors: Weather Loft, Land Floor, Front of the House, Public Counter, Pipe Gallery, Water Lab, Surface Wing, Underground, Cellar [S72](../sources/S72-li-swmm6-code-house-article.md). Bob asked for it on the evening of 3 November 2026, as an app separate from the SWMM5 house [S72](../sources/S72-li-swmm6-code-house-article.md).

**How the map was made** [S69](../sources/S69-swmm6-code-house-app-md.md)
- A text census with no compiler: 26,223 calls resolved by name, 19,900 left ambiguous and not drawn.
- 24 rooms have hand-made diagrams, each labelled Port (a JavaScript copy of the C++) or Picture.
- The ? on a line resolves 85.5 % of field uses.

**The results reader.** A Results tab opens a binary `.out` from either engine. It tells them apart by the version field (60000 for OpenSWMM, 5xxxx for SWMM 5) and reads node type codes by version, because OpenSWMM stores DIVIDER as 2 and STORAGE as 3 and SWMM 5 the reverse [S69](../sources/S69-swmm6-code-house-app-md.md). It never plots a missing value as zero, and it refuses to compare two files whose IDs, units, report count or report times differ [S72](../sources/S72-li-swmm6-code-house-article.md). See [Reading SWMM output](../concepts/reading-swmm-output.md).

**Checks.** 11 test scripts with 376 checks in all (our sum of the counts listed); wall text equals the source for all 675 files; three real result files tested against a separate Python reader [S69](../sources/S69-swmm6-code-house-app-md.md). Human review: none yet [S69](../sources/S69-swmm6-code-house-app-md.md).

**20 reading notes.** Things the AI found odd while reading the C++, each with its line of code. The article is firm that they are hypotheses: none was confirmed by running anything, and the numbers in them come from JavaScript copies [S72](../sources/S72-li-swmm6-code-house-article.md). Only the node type code was seen in a real file [S69](../sources/S69-swmm6-code-house-app-md.md). The four the article names first, all unconfirmed [S72](../sources/S72-li-swmm6-code-house-article.md):
- `NetworkMeshBuilder.cpp` line 456: the finite volume path uses one power law for every culvert code.
- `NodeCoupling.cpp` line 372: the exchange area doubles over the 5 cm above the crown.
- `InputReader.cpp` line 265: a section header written with a legacy abbreviation, such as `[JUNC]`, is dropped with no warning.
- `DynamicWave.cpp` line 4419: the SEMI_IMPLICIT update, with a continuity error of -3.29 percent against +0.07 percent for EXPLICIT on a toy chain in a JavaScript copy.

**Credits.** OpenSWMM Engine, Copyright 2026 HydroCouple Developers, Apache-2.0; lead developer Caleb Buahin; developer and documentation Corinne Wiesner-Friedman. The app reproduces the upstream NOTICE in full [S69](../sources/S69-swmm6-code-house-app-md.md).

**Open.** The public page at swmm6-code-house.netlify.app shows a v1.0.0 badge in its page source (Q45). See [Open questions](../open-questions.md).
