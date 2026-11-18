---
title: "RDII Rosetta Stone (app)"
type: entity
updated: 2026-11-18
sources: [S332]
tags: [apps, rdii, rtk, infoswmm, icm, swmm5]
reviewed: no
---
Bob's app RDII Rosetta Stone: InfoSWMM RDII mapped to EPA SWMM5 and InfoWorks ICM, with live RTK math. Version 1.0, 2026-10-21 [S332](../sources/S332-rdii-rosetta-stone-summary.md). Its `links:` line names no live Netlify address [S332](../sources/S332-rdii-rosetta-stone-summary.md).

**A caution about its source.** The page ships no technical summary. [S332](../sources/S332-rdii-rosetta-stone-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S332](../sources/S332-rdii-rosetta-stone-summary.md)
- For InfoSWMM users moving RDII to EPA SWMM5 or InfoWorks ICM: every concept, field name and workflow mapped across the three, with live RTK unit-hydrograph math, a storm-response view in cfs, a runnable SWMM5 .inp export, CSV exports and a Verify tab. A single-file rebuild of Bob's Lovable project; RTK in SWMM5's rdii.c was coded by Bob during the EPA SWMM5 CRADA.
- The storm-response arithmetic is a line-for-line port of EPA SWMM 5.2.4 rdii.c and matches the engine within float precision on 8 verification models. Two defects in the source were fixed: the ICM Ruby snippet now writes inside a transaction (D-1), and all three exports carry the same initial abstraction values (D-2).
- EPA SWMM 5.2.4 compiled from the USEPA v5.2.4 tag; eight verification models written; engine runs compared with the port step by step, report totals compared, and repeat runs compared byte for byte.
- The app screenshotted in both themes at desktop and phone widths; colours run through a contrast check.

**How to use it, as the summary puts it.** Use it to move RDII parameters between products with the arithmetic checked. ICM and InfoSWMM were not run (InfoSWMM's swmm5.dll may be older than 5.2.4), the Ruby snippet has not run in ICM, and matching the engine says nothing about whether three triangles describe a given sewer. [S332](../sources/S332-rdii-rosetta-stone-summary.md)

**What it does not show.** As the page lists it: ICM was not run (field names come from the source app and Bob's ICM data-model notes; ICM's own RTK computation was not compared with rdii.c; the Ruby snippet has not run in ICM); InfoSWMM was not run; no observed flow was used; one UH group, one month set (ALL) and one node per model (monthly sets and sharing are described but not computed); rain gages with INTENSITY time series only. [S332](../sources/S332-rdii-rosetta-stone-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [InfoWorks ICM](infoworks-icm.md).
