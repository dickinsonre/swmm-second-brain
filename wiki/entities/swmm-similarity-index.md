---
title: "SWMM Similarity Index (app)"
type: entity
updated: 2026-11-18
sources: [S342]
tags: [apps, swmm5, epanet, icm, similarity, rpt]
reviewed: no
---
Bob's app SWMM Similarity Index: Bill James scoring for SWMM5, EPANET and ICM models. Version 1.0, 2026-10 [S342](../sources/S342-swmm-similarity-index-summary.md). Its `links:` line names no live Netlify address [S342](../sources/S342-swmm-similarity-index-summary.md).

**A caution about its source.** The page ships no technical summary. [S342](../sources/S342-swmm-similarity-index-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S342](../sources/S342-swmm-similarity-index-summary.md)
- Scores how alike two hydraulic models are on a 0 to 1,000 scale, after Bill James's similarity scores for baseball players: start at 1,000 and subtract for each difference in junctions, outfalls, conduits and results. A single-file edition of Bob's Lovable project, with Compare, Outputs, Batch, Methodology and Verify tabs; 19 defects fixed, so scores differ from the Lovable app on some pairs.
- The Lovable report parser misread EPA SWMM 5.2.4: version 5.2.4 prints two more columns than it expected, so for subcatchment 1 of EPA Example 1 it read a peak of 1.48 and a runoff coefficient of 0.4 where the report says 4.66 cfs and 0.559. A unit round trip (the Baseline sample converted to CFS by exact factors) now scores 1,000; the Lovable engine gave 881. 32 of 32 checks pass.
- Identity: each of 13 input files scores exactly 1,000 against itself with an empty ledger.
- Symmetry: all 78 pairs of input files and all 45 pairs of finished reports score the same both ways round.
- Null effect on real files: exam1.inp and extran1.inp in Bob's corpus are EXTRAN Example 1 written out twice with different option blocks; they score 1,000, and their byte-identical EPA SWMM 5.2.4 reports score 1,000.
- Unit round trip: 1,000 (Lovable 881).

**How to use it, as the summary puts it.** Use it to see how far two versions of a model have drifted. A score of 1,000 means no difference was found among the attributes it scores, inside your tolerances; it does not mean the models are hydraulically equivalent, and much of a SWMM model is invisible to the score. No real ICM export has been tested. [S342](../sources/S342-swmm-similarity-index-summary.md)

**What it does not show.** As the page lists it: a score of 1,000 is not hydraulic equivalence; the Doc's figure shows how much of a SWMM model the index never reads. No person has reviewed the new Hydrology weights or the coverage term, and no real ICM export was tested. [S342](../sources/S342-swmm-similarity-index-summary.md)

**Noted at ingest.** The Bill James of the score is the baseball writer, not [William (Bill) James](william-james.md) of CHI.

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICWMM Insights (app)](icwmm-insights.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
