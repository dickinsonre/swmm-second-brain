---
title: Negative results
type: concept
updated: 2026-11-14
sources: [S03, S04, S05]
tags: [findings, method]
reviewed: no
---
Ideas that were tried and did not work. The register treats a disproven idea as a finding, and calls this group "the part no other register in this field has" [S03](../sources/S03-findings-register-format.md).

| ID | Idea | What came back | Date |
|---|---|---|---|
| F-0009 | Describe diurnal dry-weather flow with two Fourier harmonics | Failed against real patterns | 2026-07-26 |
| F-0010 | Carry Monster Moonshine structure over to SWMM | Usable as a visual projection only; no correspondence in SWMM's topology | 2026-06-30 |
| F-0011 | Apply Klein-bottle topology | Rejected on inspection | 2026-07-17 |
| F-0012 | Apply hyperbolic geometry to the hydraulics | A category error: St. Venant and Manning are Euclidean. Curvature has a place in connectivity embedding, the drainage hierarchy, and calibration space. Run against five real networks | 2026-06 |
| F-0013 | Anderson acceleration for speed | No speedup on the test case; scope is "on this case" | 2026-07 |

All rows from [S04](../sources/S04-findings-register-seed.md).

**By-products worth keeping** [S04](../sources/S04-findings-register-seed.md)
- F-0010 turned up an angle-wraparound bug that would have overlapped the first and last ring elements.
- F-0013 carries a rule: a noise floor must come before any speed ratio.

**How rare they are.** A negative result shows up in 17 of Bob's app-building conversations in 2026Q3, 15 % of that quarter's app work, up from 0 % in 2025Q4 [S05](../sources/S05-swmm5org-article-facts.md). The fact sheet uses this as the argument for the register: a result nobody writes down lives only in a transcript [S05](../sources/S05-swmm5org-article-facts.md).

See [The SWMM findings register](findings-register.md), [Six quality markers for app-building work](app-quality-markers.md).
