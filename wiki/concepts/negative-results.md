---
title: Negative results
type: concept
updated: 2026-11-17
sources: [S03, S04, S05, S215, S245, S251]
tags: [findings, method]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S215); 2026-11-17 (S243 to S255 ingest): a paragraph added near the end, headed Added 17 November 2026 (S245, S251)"
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

**Added 17 November 2026.** [SWMM Trouble Graph (app)](../entities/swmm-trouble-graph.md) planted 296 typing errors in 39 corpus models: for a pipe length typed too short, the time-step list's first entry landed within 2 hops 40 % of the time against 23 % for the graph, and the page says the graph did not beat the right single list [S215](../sources/S215-swmm-trouble-graph-summary.md).

**Added 17 November 2026, third batch.** From the third batch: shorter support-article titles that passed every KCS gate found the right article first 25 times in thirty, against 28 for the old titles [S245](../sources/S245-icm-kcs-catalog-2026-summary.md); a June map of SWMM 5.2.4 drawn from memory found 60 of 365 real file links [S251](../sources/S251-understand-anything-swmm-icm-summary.md).

See [The SWMM findings register](findings-register.md), [Six quality markers for app-building work](app-quality-markers.md).
