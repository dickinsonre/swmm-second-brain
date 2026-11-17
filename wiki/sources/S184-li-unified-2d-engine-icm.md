---
title: "S184: Utilizing a Unified 2D Engine in both ICM InfoWorks and ICM SWMM Networks (LinkedIn, 2023)"
type: source
raw: raw/linkedin/2023-05-26-utilizing-unified-2d-engine-both-icm-infoworks-swmm-robert-dickinson.md
kind: linkedin-article
author: Robert Dickinson
published: 2023-05-26
ingested: 2026-11-16
tags: [icm, 2d, swmm5, conversion, comparison]
drafted_by: Robert Dickinson, with a conversion walk-through that reads as AI-written
reviewed: no
---
**What it is.** Bob's article on converting an InfoWorks 1D and 2D network to an ICM SWMM network and running both on ICM's one 2D engine. Raw file: [raw/linkedin/2023-05-26-utilizing-unified-2d-engine-both-icm-infoworks-swmm-robert-dickinson.md](../../raw/linkedin/2023-05-26-utilizing-unified-2d-engine-both-icm-infoworks-swmm-robert-dickinson.md). Created 7 November 2022, published 26 May 2023.

**How it was written.** Bob's article. The four-step section on what a conversion involves ("Conversion of 2D Elements" to "Validation") reads as AI-written; the captions and the comparison of results are his. The results are in screenshots that are not in `raw/`.

**Claims worth keeping**
- ICM SWMM and ICM InfoWorks networks share one 2D engine. They do not share a 1D engine: ICM SWMM used the SWMM 5.2.3 engine and InfoWorks a proprietary engine, and both solve the 1D St. Venant equation "in slightly different forms".
- Quoting the ICM help: the 2D engine is based on the Mulet and Alcrudo unstructured flood solver, MULFLOOD, designed by Francisco Alcrudo Sanchez and Jónatan Mulet-Martí (Alcrudo and Mulet-Marti, 2005).
- InfoWorks has more 1D and 2D features. Converting an InfoWorks network to SWMM drops any feature SWMM lacks.
- Two validation errors after conversion: SWMM needs a rain gage to hold the rainfall, and SWMM does not allow a subcatchment and a node to share an ID. The fix for the second is an SQL statement that prefixes the subcatchment IDs: `SET subcatchment_id = 'S_' + subcatchment_id;`.
- InfoWorks and SWMM networks can share one rainfall profile through a rain gage. In both, a node with a 1D-2D connection gets the flood type 2D.
- The run: ICM SWMM flooded more than InfoWorks, which the article puts down to hydrology: the ICM SWMM network used SWMM hydrology and the InfoWorks network the Wallingford option. The 2D results appear in the log file for InfoWorks and in the report file for ICM SWMM, in the same format.

**Feeds:** [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [ICM 2D: timestep, volume balance and results](../concepts/icm-2d-runs-and-checks.md).
