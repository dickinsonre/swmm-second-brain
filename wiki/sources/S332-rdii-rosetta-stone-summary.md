---
title: "S332: RDII Rosetta Stone, summary written from the page (v1.0)"
type: source
raw: raw/apps/rdii-rosetta-stone-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-18
tags: [apps, rdii, rtk, infoswmm, icm, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app RDII Rosetta Stone, version 1.0: InfoSWMM RDII mapped to EPA SWMM5 and InfoWorks ICM, with live RTK math. Raw file: [raw/apps/rdii-rosetta-stone-v1.0.md](../../raw/apps/rdii-rosetta-stone-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/3jemmFKg8cjQyjwd22RpVe, version 1792638304-d93a (index.html, 783,636 bytes, SHA-256 620a55af1c52d7ac0994d98c4cc84d2d50cc5c5d0a62fc6ded97b950b0a32fc6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the source project and asked for a single-file HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- For InfoSWMM users moving RDII to EPA SWMM5 or InfoWorks ICM: every concept, field name and workflow mapped across the three, with live RTK unit-hydrograph math, a storm-response view in cfs, a runnable SWMM5 .inp export, CSV exports and a Verify tab. A single-file rebuild of Bob's Lovable project; RTK in SWMM5's rdii.c was coded by Bob during the EPA SWMM5 CRADA.
- The storm-response arithmetic is a line-for-line port of EPA SWMM 5.2.4 rdii.c and matches the engine within float precision on 8 verification models. Two defects in the source were fixed: the ICM Ruby snippet now writes inside a transaction (D-1), and all three exports carry the same initial abstraction values (D-2).
- EPA SWMM 5.2.4 compiled from the USEPA v5.2.4 tag; eight verification models written; engine runs compared with the port step by step, report totals compared, and repeat runs compared byte for byte.
- The app screenshotted in both themes at desktop and phone widths; colours run through a contrast check.

**Limits it states.** As the page lists it: ICM was not run (field names come from the source app and Bob's ICM data-model notes; ICM's own RTK computation was not compared with rdii.c; the Ruby snippet has not run in ICM); InfoSWMM was not run; no observed flow was used; one UH group, one month set (ALL) and one node per model (monthly sets and sharing are described but not computed); rain gages with INTENSITY time series only.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [RDII Rosetta Stone (app)](../entities/rdii-rosetta-stone.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [InfoWorks ICM](../entities/infoworks-icm.md).
