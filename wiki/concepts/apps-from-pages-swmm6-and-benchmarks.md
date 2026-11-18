---
title: "Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results"
type: concept
updated: 2026-11-18
sources: [S69, S280, S281, S282, S283, S284, S285, S286, S287, S288]
tags: [apps, swmm6, openswmm, benchmarks, icm]
reviewed: no
---
Nine summaries that Bob uploaded on 18 November 2026 on OpenSWMM 6, the benchmarks around it and ICM results. All nine were written by Claude from the published pages with nothing rerun (Q111). [S280](../sources/S280-run-swmm6-ten-minutes-summary.md) and [S281](../sources/S281-swmm6-in-diagrams-summary.md) describe a document and a set of diagrams, converted to standalone pages for Netlify.

| App | Version | Date | Source |
|---|---|---|---|
| [Run SWMM6 in Ten Minutes (document)](../entities/run-swmm6-ten-minutes.md) | 2026-10-05 | 2026-10-05 | [S280](../sources/S280-run-swmm6-ten-minutes-summary.md) |
| [SWMM6 in Diagrams (design)](../entities/swmm6-in-diagrams.md) | 2026-11-14 | 2026-11-14 | [S281](../sources/S281-swmm6-in-diagrams-summary.md) |
| [Forma × SWMM6 (app)](../entities/forma-swmm6.md) | 1.2 | 2026-11-01 | [S282](../sources/S282-forma-swmm6-summary.md) |
| [Cymatic Synapse Generator (app)](../entities/cymatic-synapse-generator.md) | 1.15 | 2026-10-31 | [S283](../sources/S283-cymatic-synapse-generator-summary.md) |
| [SWMM6 UX Explorer (app)](../entities/swmm6-ux-explorer.md) | 2026-11-03 | 2026-11-03 | [S284](../sources/S284-swmm6-ux-explorer-summary.md) |
| [SWMM6 Shoebox (app)](../entities/swmm6-shoebox.md) | 1.1 | 2026-10-24 | [S285](../sources/S285-swmm6-shoebox-summary.md) |
| [Exam-First SWMM Harness (app)](../entities/exam-first-swmm-harness.md) | 2026-10-19 | 2026-10-19 | [S286](../sources/S286-exam-first-swmm-harness-summary.md) |
| [OpenHydro Bench Review (app)](../entities/openhydro-bench-review.md) | 1.7 | 2026-10-18 | [S287](../sources/S287-openhydro-bench-review-summary.md) |
| [ICM Link Results SQL (app)](../entities/icm-link-results-sql.md) | 1.0 | 2026-11-02 | [S288](../sources/S288-icm-link-results-sql-summary.md) |

**OpenSWMM 6 measured on small cases.** With SWMM 5's options it matches EPA 5.2.4 bit for bit in the time series of a three-pipe model, yet its surcharge tables say no node surcharged [S280](../sources/S280-run-swmm6-ten-minutes-summary.md). Its own options trade convergence for continuity: DYNAMIC_SLOT and SEMI_IMPLICIT end non-convergence on a ponded chain, and SEMI_IMPLICIT makes continuity worse there [S281](../sources/S281-swmm6-in-diagrams-summary.md). Parity on a ponded chain fails (14.45 against 11.67 cfs) [S281](../sources/S281-swmm6-in-diagrams-summary.md) (Q115).

**Defects the pages report.** Green-Ampt in alpha.4 gave 0.99 against 19.54 cfs, fixed upstream since [S285](../sources/S285-swmm6-shoebox-summary.md); a flooding summary that lists outfalls as flooded [S285](../sources/S285-swmm6-shoebox-summary.md); storage nodes written as dividers in the .out [S286](../sources/S286-exam-first-swmm-harness-summary.md), as [S69](../sources/S69-swmm6-code-house-app-md.md) found; finite-volume depths of 103.4 ft at a 12.75 ft junction [S286](../sources/S286-exam-first-swmm-harness-summary.md); slot water booked as storage [S282](../sources/S282-forma-swmm6-summary.md).

**Benchmarks and harnesses.** A review of a 1D-2D benchmark finds its machinery sound and its scoring not ready [S287](../sources/S287-openhydro-bench-review-summary.md); a harness whose held-out score rose from 0.496 to 0.807 while its sealed score rose only from 0.637 to 0.715 [S286](../sources/S286-exam-first-swmm-harness-summary.md).

**Around the engine.** Versions kept like drawings in a common data environment [S282](../sources/S282-forma-swmm6-summary.md); a generator from a picture [S283](../sources/S283-cymatic-synapse-generator-summary.md); the SWMMVis workspace with public data [S284](../sources/S284-swmm6-ux-explorer-summary.md); a one-site desk solved by both engines [S285](../sources/S285-swmm6-shoebox-summary.md); ICM SQL link-result fields [S288](../sources/S288-icm-link-results-sql-summary.md).

See [OpenSWMM 6 solvers, measured](openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](apps-from-pages-swmm6-hydrocouple-ai.md).