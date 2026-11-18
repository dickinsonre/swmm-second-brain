---
title: "Aquanuity Theory (app)"
type: entity
updated: 2026-11-18
sources: [S312]
tags: [apps, aquatwin, 2d-surface, diffusion-wave, numerics]
reviewed: no
---
Bob's app Aquanuity Theory: a reader's edition of the numerics behind AquaTwin Sewer 2D, with a solver bench. Version 1.0, 2026-10-24 [S312](../sources/S312-aquanuity-theory-summary.md). Its `links:` line names no live Netlify address [S312](../sources/S312-aquanuity-theory-summary.md).

**A caution about its source.** The page ships no technical summary. [S312](../sources/S312-aquanuity-theory-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S312](../sources/S312-aquanuity-theory-summary.md)
- An independent single-file edition of Bob's Lovable site about the numerical scheme behind Aquanuity's AquaTwin Sewer 2D (explicit shallow water or implicit diffusion wave on the surface, FSGI or SWMM5 dynamic wave in the pipes). It keeps the original guide and glossary, corrects them against sources (18 entries in the Audit tab) and adds a Solver Lab, a time-step calculator, a 1D-2D exchange calculator and a Doc essay.
- The page's own two solvers agree within 1% on sheet flow down a 0.2% slope, and part where the bed is flat: at mid-reach of a flat 6,600 ft strip the SWE peaks at 1.90 ft and the DWE at 1.78 ft. The speed claims are marked against what was shown live on 22 October: "at least a factor of 8" for FSGI against SWMM5 dynamic wave, 2.7 times shown; about 4 times for implicit DWE against explicit SWE (2:31 against 39 s), 10 times in the announcement.
- Solver tests in Node before any interface was built: Ritter dam break, relative L1 error 1.02% at 100 cells falling to 0.22% at 800; lake at rest over a bump, SWE 1.4 x 10^-15 ft (4.4e-16 m) and DWE 2.8 x 10^-11 ft (8.5e-12 m) (feet are our conversion); Manning normal depth on a slope, 0.983 ft, SWE within 0.5% and DWE exact; water balance closed to better than 10^-9 percent in every case.
- Contrast gate on 74 colour pairs in both themes; all 20 glossary source links fetched and resolve; a browser render in both themes at desktop and phone width.

**How to use it, as the summary puts it.** Use it to read what AquaTwin's numerics claim and where a diffusion wave stops tracking the full equations. It is not affiliated with Aquanuity, runs no Aquanuity code, and its two solvers are 1D teaching solvers. [S312](../sources/S312-aquanuity-theory-summary.md)

**What it does not show.** As the page lists it: the corrected glossary wording, the matching of Environment Agency benchmark tests to Aquanuity's benchmark pages, and the Doc prose have not been checked by a person. The solvers are 1D strips, not AquaTwin's 2D mesh; the speed figures are Aquanuity's and the October 22 webinar's, not measured here. [S312](../sources/S312-aquanuity-theory-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md).
