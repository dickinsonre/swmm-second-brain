---
title: Design storms and temporal patterns
type: concept
updated: 2026-11-17
sources: [S62, S65, S66, S237, S238, S253]
tags: [rainfall, design-storms, hydrology, method]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S224 to S242 ingest): a paragraph added near the end, headed Added 17 November 2026 (S237, S238); 2026-11-17 (S243 to S255 ingest): a paragraph added near the end, headed Added 17 November 2026 (S253)"
---
A design storm is a total depth and a shape. The shape, a hyetograph, says when in the storm the rain falls hardest, and it is the rainfall input a drainage model needs [S66](../sources/S66-li-design-storm-app-66-patterns.md). Bob's [World Rainfall Pattern Painter (app)](../entities/world-rainfall-pattern-painter.md) generates them [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

**Why the shape matters.** Five inches in 24 hours spread evenly is a drizzle. The same five inches in a two-hour burst needs different pipes [S66](../sources/S66-li-design-storm-app-66-patterns.md).

**Patterns differ by country.** The United States has the four SCS types of TR-55 (1986). Other countries publish their own, and the app's February 2026 catalogue sorted 66 of them into nine regional groups [S66](../sources/S66-li-design-storm-app-66-patterns.md). By November 2026 the catalogue held 339 [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

**How a hyetograph is computed from a mass curve** [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md)
1. Count the intervals: duration divided by time step, rounded up.
2. Read the dimensionless cumulative curve at the start and end of each interval, interpolating between table points.
3. Intensity for the interval is the depth times that rise, divided by the interval length.
4. Check the total. If it is within 0.02 (relative) of the target depth, rescale to the exact depth; if not, try a finer grid, then fall back, and label the result with what was done.

**Method credits as the app records them** [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md)

| Pattern | Credit and year |
|---|---|
| SCS Types I, IA, II, III | USDA NRCS, 1986, TR-55 |
| Chicago storm | Keifer and Chu, 1957 |
| Huff quartiles | Huff, 1967 |
| Triangular | Yen and Chow, 1980 |
| Alternating block | Chow, Maidment and Mays, 1988 |
| Euler Type II | DWA, 2006; original author and year not checked |
| FEH | CEH, 1999 |
| ARR 2019 | Ball et al., 2019 |

The summary lists 37 method families in all, each with the file and line where the credit is recorded [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

**How far each pattern can be trusted.** The app grades its own catalogue: 3 patterns High, 57 Medium, 279 Low. High means benchmarked against published ordinates, and only the uniform block and SCS Types IA and II qualify [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). Three named shortcuts: the Chicago storm uses a fixed peak position of 0.4 and exponent 0.6, "not site IDF constants"; the triangular storm peaks at 0.33; Euler Type II uses "a generic KOSTRA-like curve, not site KOSTRA data" [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

**Volume closing is not the same as the right shape.** All 339 patterns return their depth to within 1.776e-15 in, and the summary still says "a single request or volume test does not validate the hydrologic suitability of a pattern for a particular site or regulatory requirement" [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). This is the rainfall form of [Continuity is not validation](continuity-is-not-validation.md).

**Climate uplift.** The app multiplies the depth by a factor per scenario, from 1.00 to 1.40, in four sets (Singapore PUB, UK FEH, Australian ARR 2019, Canadian CDA); the factors are "transcribed from the app, not independently checked against the cited guidance" [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). The [Rules for Responsible Modeling (app)](../entities/rules-for-responsible-modeling-app.md) uses example factors of 1.0, 1.1, 1.2 and 1.3 and calls its own "illustrative, not climate projections" [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). Neither app's factors have been checked against a published table (Q43 in [Open questions](../open-questions.md)).

**Not in the sources yet.** The published tables themselves (TR-55, KOSTRA, FEH, ARR), any comparison of a design storm with a gauged one, and how SWMM 5 and ICM read the exported files.

**Added 17 November 2026, second batch.** Two apps on the rainfall that goes into a model. [Quantile Mapping to SWMM5 / SWMM6 (app)](../entities/quantile-mapping-swmm.md) corrects forecast rain by quantile mapping and notes that SWMM5's only rainfall adjustment is one monthly multiplier [S237](../sources/S237-quantile-mapping-swmm-summary.md). [The Narrow Band (app)](../entities/narrow-band.md) finds that a narrow uncertainty band on a 200-year daily rain need not hold the true value: 28.8 % of records for MEVD against 75.8 % for GEV, on synthetic rain [S238](../sources/S238-narrow-band-app-md.md).

**Added 17 November 2026, third batch.** From the third batch: turning an NOAA Atlas 14 depth table into a Chicago storm, the discretisation of the UrbanSystemsLab repository does not always conserve the storm total [S253](../sources/S253-rain-on-grid-workbench-summary.md).
