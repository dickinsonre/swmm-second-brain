---
title: Reading SWMM output
type: concept
updated: 2026-11-14
sources: [S03, S10, S22, S60, S69, S72]
tags: [swmm5, output, reporting]
reviewed: 2026-11-15
---
A large share of "SWMM is wrong" questions come from comparing two honest numbers that measure different things [S22](../sources/S22-li-ten-problems.md).

**The summary tables and the .out file sample differently.** The summary tables check every routing step. The .out file keeps one value per report step [S22](../sources/S22-li-ten-problems.md).

**Worked case.** Conduit C11 in EPA Example 1, run in EPA SWMM 5.2.4 on 5 November 2026: peak 73.9 cfs in the Link Flow Summary, 71.18 cfs in the .out file at 5-minute reporting. Nothing in the report says which is which [S22](../sources/S22-li-ten-problems.md).

**Other pairs that get confused** [S22](../sources/S22-li-ten-problems.md)
- flooding and ponding. In the engine's own terms: a node whose head would pass its maximum is flooded, and the excess is lost from the system, the same as flow leaving an outfall. If the node has a ponded area, the water is stored above it and returns as capacity allows [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- maximum depth and maximum HGL
- three different continuity errors

**A related defect.** Two interpolations of the same quantity, `output.c:590` against `routing.c:592`, are listed as root-caused under USEPA issue 229 [S03](../sources/S03-findings-register-format.md).

**One file layout, two engines.** EPA SWMM 5 and OpenSWMM 6 write the same binary `.out` layout with the same magic number, 516114522. The version field tells them apart: 60000 for OpenSWMM, 5xxxx for SWMM 5. Node type codes differ: OpenSWMM stores DIVIDER as 2 and STORAGE as 3 (`plugins/DefaultOutputPlugin.cpp:451`), and SWMM 5 has the two the other way round, so a reader built for SWMM 5 would call an OpenSWMM storage node a divider [S69](../sources/S69-swmm6-code-house-app-md.md). The [SWMM6 Code House (app)](../entities/swmm6-code-house.md) reads the code by version, and saw the case in a real file, `baseline.out` [S72](../sources/S72-li-swmm6-code-house-article.md).

**How often it is asked** (tags on Bob's 2,879 OpenSWMM thread titles) [S10](../sources/S10-openswmm-top25-problems.md)

| Problem | Threads |
|---|---|
| Reading the output | 224 |
| Results that disagree | 134 |
| Flooding versus ponding | 77 |

Bob's comment: he and others have explained for over 25 years why the graphs and the summary table peaks sometimes differ [S22](../sources/S22-li-ten-problems.md).

See also [The missing specification](the-missing-specification.md) and [Continuity is not validation](continuity-is-not-validation.md).
