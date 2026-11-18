---
title: "S348: HydroNeural, summary written from the page (v1.0)"
type: source
raw: raw/apps/hydroneural-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
tags: [apps, surrogates, machine-learning, literature, audits]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app HydroNeural, version 1.0: a SWMM5 surrogate console, with its mock data and its literature review audited. Raw file: [raw/apps/hydroneural-v1.0.md](../../raw/apps/hydroneural-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/QKCJF1fy1xv35NBFqZLbgr, version 1792679529-6cc5 (index.html, 1,978,568 bytes, SHA-256 85e8b920ed6cc2d4b76f5342c3ea084d1a90e64f8a6a271ad90ca98a9059923c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 22 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the HydroNeural source export from Lovable, asked for an HTML app that shows all of it, and is responsible for the result. The Lovable project itself, including its literature review, was generated earlier by Lovable's AI."

**Claims worth keeping** (all copied from the file)
- A single-file edition of HydroNeural, a Lovable-built console for a machine-learning surrogate of EPA SWMM5. It carries the original's forecast dashboard and literature review, adds an Anatomy of the source and an Audit of what the code computes, and explains it in a Doc tab. The header says it plainly: all numbers are seeded mock.
- No surrogate exists here: no model was trained and no SWMM5 model was run; the map depths are a bias toward the lower-right corner plus noise, and the hydrograph is smoothed rain. Of the review's 22 references with a complete DOI, checked against Crossref, 8 match exactly, 11 are the right paper with a detail wrong (three credit the wrong first author), one DOI resolves to an unrelated paper on aerosol water-vapour uptake, and two returned errors.
- The generators in src/lib/swmm-mock.ts ported to plain JavaScript with the types removed and nothing else changed, then run in Node; the node, conduit, subcatchment and flooding counts come from that run. Hydrograph metrics from the component's own formulas on the generated series, with KGE added in the standard Gupta et al. form.
- Citations: 22 complete DOIs fetched from Crossref and compared on title, first author, year and journal.

**Limits it states.** As the page lists it: it does not show a surrogate (no training, no SWMM5 run; the experiment registry's four rows are typed numbers in the order the review ranks the methods); it does not reproduce the Lovable app pixel for pixel; it does not show whether the review's claims about each paper are right.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [HydroNeural (app)](../entities/hydroneural.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [Finite difference vs ML for flood modeling (dashboard)](../entities/finite-difference-vs-ml.md).
