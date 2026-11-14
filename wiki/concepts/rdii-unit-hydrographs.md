---
title: RDII unit hydrographs (RTK)
type: concept
updated: 2026-11-14
sources: [S16, S55]
tags: [hydrology, rdii, swmm5]
reviewed: no
---
SWMM5 computes rainfall-dependent inflow and infiltration (RDII) from triangular unit hydrographs [S16](../sources/S16-li-rdii-in-swmm5.md).

**Structure**
- A unit hydrograph set has up to three hydrographs: short-term, intermediate-term and long-term response [S16](../sources/S16-li-rdii-in-swmm5.md).
- A group has up to 12 sets, one per month, and names the rain gage that feeds it [S16](../sources/S16-li-rdii-in-swmm5.md).
- A node receives RDII by naming a group and a sewershed area in its Inflows property. The sewershed area is typically a small part of the subcatchment area that sends surface runoff to the same node [S16](../sources/S16-li-rdii-in-swmm5.md).

**Parameters** [S16](../sources/S16-li-rdii-in-swmm5.md)

| Symbol | Meaning |
|---|---|
| R | Fraction of rainfall volume that enters the sewer |
| T | Time from the start of rainfall to the hydrograph peak, hours |
| K | Ratio of time to recession to time to peak |
| Dmax | Maximum depth of initial abstraction |
| Drec | Recovery rate of initial abstraction |
| Do | Initial abstraction already used at the start |

A blank parameter is taken as 0 [S16](../sources/S16-li-rdii-in-swmm5.md).

**Files.** An RDII interface file has the same text format as a routing interface file: the keyword `SWMM5`, a description, the time step in seconds, the variables (flow first), the node names, then one line per node per step. RDII files that SWMM writes itself are binary [S16](../sources/S16-li-rdii-in-swmm5.md).

**A use beyond RDII.** With calibrated unit hydrographs the RDII procedure can replace the subcatchment rainfall-runoff procedure, in which case "RDII" at a node is really overland runoff [S16](../sources/S16-li-rdii-in-swmm5.md).

**Who wrote it.** Bob coded the RTK/RDII implementation for SWMM 5 during the CRADA project with EPA [S55](../sources/S55-swmm-brain-readme.md). His later tools on it: an RTK Hydrograph Generator app, the RDII Analyst at Innovyze, and Ruby scripts for RTK parameter fitting in ICM [S55](../sources/S55-swmm-brain-readme.md).

**Not in the sources yet.** How InfoSWMM and ICM treat RDII (the article's title promises it, but those parts were images), and a description of the method from the code. Queued: "InfoSWMM, InfoSWMM SA RDII Analyst 3.0 with EPA SSOAP Tools" (2017, 4,019 words).
