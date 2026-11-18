---
title: "HydroNeural (app)"
type: entity
updated: 2026-11-18
sources: [S348]
tags: [apps, surrogates, machine-learning, literature, audits]
reviewed: no
---
Bob's app HydroNeural: a SWMM5 surrogate console, with its mock data and its literature review audited. Version 1.0, 2026-10-22 [S348](../sources/S348-hydroneural-summary.md). Its `links:` line names no live Netlify address [S348](../sources/S348-hydroneural-summary.md).

**A caution about its source.** The page ships no technical summary. [S348](../sources/S348-hydroneural-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S348](../sources/S348-hydroneural-summary.md)
- A single-file edition of HydroNeural, a Lovable-built console for a machine-learning surrogate of EPA SWMM5. It carries the original's forecast dashboard and literature review, adds an Anatomy of the source and an Audit of what the code computes, and explains it in a Doc tab. The header says it plainly: all numbers are seeded mock.
- No surrogate exists here: no model was trained and no SWMM5 model was run; the map depths are a bias toward the lower-right corner plus noise, and the hydrograph is smoothed rain. Of the review's 22 references with a complete DOI, checked against Crossref, 8 match exactly, 11 are the right paper with a detail wrong (three credit the wrong first author), one DOI resolves to an unrelated paper on aerosol water-vapour uptake, and two returned errors.
- The generators in src/lib/swmm-mock.ts ported to plain JavaScript with the types removed and nothing else changed, then run in Node; the node, conduit, subcatchment and flooding counts come from that run. Hydrograph metrics from the component's own formulas on the generated series, with KGE added in the standard Gupta et al. form.
- Citations: 22 complete DOIs fetched from Crossref and compared on title, first author, year and journal.

**How to use it, as the summary puts it.** Use it as a worked example of auditing an AI-generated app and its citations before trusting either. It does not show whether the review's claims about each paper are right, only whether the cited records exist and match. [S348](../sources/S348-hydroneural-summary.md)

**What it does not show.** As the page lists it: it does not show a surrogate (no training, no SWMM5 run; the experiment registry's four rows are typed numbers in the order the review ranks the methods); it does not reproduce the Lovable app pixel for pixel; it does not show whether the review's claims about each paper are right. [S348](../sources/S348-hydroneural-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [Finite difference vs ML for flood modeling (dashboard)](finite-difference-vs-ml.md).
