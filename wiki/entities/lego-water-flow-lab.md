---
title: "LEGO Water Flow Lab (app)"
type: entity
updated: 2026-11-18
sources: [S364]
tags: [apps, toys, lego]
reviewed: no
---
Bob's app LEGO Water Flow Lab: will a molecule built from LEGO parts go down a pipe?. Version 1.0, 2026-10 [S364](../sources/S364-lego-water-flow-lab-summary.md). Its `links:` line names no live Netlify address [S364](../sources/S364-lego-water-flow-lab-summary.md).

**A caution about its source.** The page ships no technical summary. [S364](../sources/S364-lego-water-flow-lab-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S364](../sources/S364-lego-water-flow-lab-summary.md)
- A playful lab that asks whether a molecule built from LEGO parts fits down a household pipe, with a Pipe Fit Tester, a Flow Simulator with Auto-Test, sound and reassembly, a parts list, an assembly guide and a specs table. A single-file edition of Bob's Lovable project; it adds an Engineer's switch with real pipe tables (Schedule 40 steel, copper Type L, PEX SDR 9) and three fit rules, and an Audit tab.
- The audit of the Lovable source lists 12 findings (5 fixed, 2 with a switch added, 4 flagged, 1 changed). The worst: Auto-Test ran the starting pipe four times and recorded one row (D1); the fixed Auto-Test returns all four. Pipe tolerances are larger than several of the clearances shown, so a fit on paper can fail in the pipe.
- Node assertions that the as-shipped table reproduces every verdict hard-coded in the original.
- Headless-browser runs of both builds; the fixed Auto-Test returns all four rows.
- A console-error and contrast check of the rendered page in both themes.
- Every file in the source zip read, the original built and run, and every number that decides a fit checked against a published table.

**How to use it, as the summary puts it.** Use it to teach pipe bores and clearances with toy bricks. No water is modelled; the fit rules are for a straight pipe, so elbows, fittings and the faucet are not checked, and no person has checked the bores against the printed standards. [S364](../sources/S364-lego-water-flow-lab-summary.md)

**What it does not show.** As the page lists it: no water is modelled; the fit rules are for a straight pipe; pipe tables print nominal dimensions and the allowed tolerances are larger than several clearances shown; the stage draws the bore in proportion and the molecule as a fixed cartoon (the Pipe Fit Tester is the to-scale view). Not yet checked by a person: the edition as a whole, the bores against the printed standards, the faucet claim on the Problem card, and the parts list against a LEGO catalogue. [S364](../sources/S364-lego-water-flow-lab-summary.md)

**Noted at ingest.** A different app from [SWMM5 Lego Model (app)](swmm5-lego-model.md).

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [SWMM5 Lego Model (app)](swmm5-lego-model.md).
