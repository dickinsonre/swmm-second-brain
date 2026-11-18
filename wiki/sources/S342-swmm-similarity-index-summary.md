---
title: "S342: SWMM Similarity Index, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-similarity-index-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, swmm5, epanet, icm, similarity, rpt]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app SWMM Similarity Index, version 1.0: Bill James scoring for SWMM5, EPANET and ICM models. Raw file: [raw/apps/swmm-similarity-index-v1.0.md](../../raw/apps/swmm-similarity-index-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Gb8CqJedmkQ9DwvYxPsz7w, version 1792896068-ee18 (index.html, 1,607,591 bytes, SHA-256 e98c068ad619757a3b8ca6a5ba927ac105b7f50b41d615b98f3874587b8235ee), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project and asked for this single-file app; responsibility is his. Claude read the Lovable source, ported the TypeScript engine, found and fixed the 19 numbered defects, and wrote the interface, the charts, the derived control files, the verification script, the Doc essay and its .docx."

**Claims worth keeping** (all copied from the file)
- Scores how alike two hydraulic models are on a 0 to 1,000 scale, after Bill James's similarity scores for baseball players: start at 1,000 and subtract for each difference in junctions, outfalls, conduits and results. A single-file edition of Bob's Lovable project, with Compare, Outputs, Batch, Methodology and Verify tabs; 19 defects fixed, so scores differ from the Lovable app on some pairs.
- The Lovable report parser misread EPA SWMM 5.2.4: version 5.2.4 prints two more columns than it expected, so for subcatchment 1 of EPA Example 1 it read a peak of 1.48 and a runoff coefficient of 0.4 where the report says 4.66 cfs and 0.559. A unit round trip (the Baseline sample converted to CFS by exact factors) now scores 1,000; the Lovable engine gave 881. 32 of 32 checks pass.
- Identity: each of 13 input files scores exactly 1,000 against itself with an empty ledger.
- Symmetry: all 78 pairs of input files and all 45 pairs of finished reports score the same both ways round.
- Null effect on real files: exam1.inp and extran1.inp in Bob's corpus are EXTRAN Example 1 written out twice with different option blocks; they score 1,000, and their byte-identical EPA SWMM 5.2.4 reports score 1,000.
- Unit round trip: 1,000 (Lovable 881).

**Limits it states.** As the page lists it: a score of 1,000 is not hydraulic equivalence; the Doc's figure shows how much of a SWMM model the index never reads. No person has reviewed the new Hydrology weights or the coverage term, and no real ICM export was tested.

**Checked at ingest.** The Bill James of the score is the baseball writer, not [William (Bill) James](../entities/william-james.md) of CHI. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM Similarity Index (app)](../entities/swmm-similarity-index.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICWMM Insights (app)](../entities/icwmm-insights.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
