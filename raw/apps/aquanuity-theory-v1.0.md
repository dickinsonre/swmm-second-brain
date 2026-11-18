---
name: Aquanuity Theory
file: aquanuity-theory.html
version: "1.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/D1tpkRnahogupR2oLPyJY8", original: "Lovable project aquanuity-theory", repo: none named in the page}
engines:
  - {name: "two solvers written for the page", note: "an explicit shallow-water (SWE) solver and an implicit diffusion-wave (DWE) solver in JavaScript, on a 1D strip; no Aquanuity, SWMM or ICM engine runs in the page"}
units: US customary by default, SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 24 October 2026 under Robert Dickinson's direction, from his Lovable site, whose text and images Lovable's AI generated. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/D1tpkRnahogupR2oLPyJY8, version 1792896564-2215 (index.html, 965,948 bytes, SHA-256 63ce48ca203d02f64775e33a3117d507f155bd804042caaad35ba257bd32b7a5), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Aquanuity Theory: a reader's edition of the numerics behind AquaTwin Sewer 2D, with a solver bench

## In three points
- **What:** An independent single-file edition of Bob's Lovable site about the numerical scheme behind Aquanuity's AquaTwin Sewer 2D (explicit shallow water or implicit diffusion wave on the surface, FSGI or SWMM5 dynamic wave in the pipes). It keeps the original guide and glossary, corrects them against sources (18 entries in the Audit tab) and adds a Solver Lab, a time-step calculator, a 1D-2D exchange calculator and a Doc essay.
- **So what:** The page's own two solvers agree within 1% on sheet flow down a 0.2% slope, and part where the bed is flat: at mid-reach of a flat 6,600 ft strip the SWE peaks at 1.90 ft and the DWE at 1.78 ft. The speed claims are marked against what was shown live on 22 October: "at least a factor of 8" for FSGI against SWMM5 dynamic wave, 2.7 times shown; about 4 times for implicit DWE against explicit SWE (2:31 against 39 s), 10 times in the announcement.
- **Now what:** Use it to read what AquaTwin's numerics claim and where a diffusion wave stops tracking the full equations. It is not affiliated with Aquanuity, runs no Aquanuity code, and its two solvers are 1D teaching solvers.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Guide, Glossary, Solver Lab, Time Step, Exchange, Audit, About, Doc. The Guide carries the original site's overview, six equations, four pillars, coupling notes, benchmarks and coda; the Glossary its ten terms with their 20 source links, plus two added terms (FSGI, dynamic Preissmann slot). The Solver Lab runs one scenario through both solvers and records gauge depths. CSV export and a GIF walk-through.

Solver Lab cases the Doc reports:
- Case 1, sheet flow: a 2-hour inflow hydrograph down 2,000 ft of 0.2% slope. Gauge peaks 1.30, 1.29, 1.28 ft (SWE) against 1.30, 1.28, 1.27 ft (DWE); largest difference 0.10 ft, at gauge 3 as the front arrives. SWE 4,278 steps; DWE 480 steps at about 7.8 iterations each.
- Case 2, a flat plane and a wall: a 30-minute pulse into a dead-flat 6,600 ft strip. Near the inflow 2.87 and 2.87 ft; at mid-reach 1.90 ft (SWE) against 1.78 ft (DWE); at the far wall the SWE overshoots to 1.40 ft at 77 minutes as the wave reflects.
- The Doc places the cases against Ponce, Li and Simons (1978): the diffusion wave tracks the full equations when the dimensionless wave period T·S0·√(g/d0) is at least 30. Case 1 qualifies; cases 2 and 3 have zero bed slope and cannot be placed, and those are where the two solvers part.

## Checks (as stated on the page)

- Solver tests in Node before any interface was built: Ritter dam break, relative L1 error 1.02% at 100 cells falling to 0.22% at 800; lake at rest over a bump, SWE 1.4 x 10^-15 ft (4.4e-16 m) and DWE 2.8 x 10^-11 ft (8.5e-12 m) (feet are our conversion); Manning normal depth on a slope, 0.983 ft, SWE within 0.5% and DWE exact; water balance closed to better than 10^-9 percent in every case.
- Contrast gate on 74 colour pairs in both themes; all 20 glossary source links fetched and resolve; a browser render in both themes at desktop and phone width.

## What this does not show

As the page lists it: the corrected glossary wording, the matching of Environment Agency benchmark tests to Aquanuity's benchmark pages, and the Doc prose have not been checked by a person. The solvers are 1D strips, not AquaTwin's 2D mesh; the speed figures are Aquanuity's and the October 22 webinar's, not measured here.

## Credits and licenses

Aquanuity's AquaTwin Sewer 2D product page and its releases of 15 December 2023 and 20 February 2024; Néelz and Pender (2013), the Environment Agency benchmark report; Ritter (1892); Ponce, Li and Simons (1978). Product names belong to their owners; the page states it is not affiliated with or endorsed by Aquanuity. Background images are AI-generated illustrations from the Lovable build, marked as not model output. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, on 24 October 2026 under the direction of Robert (Bob) Dickinson, who made the original Lovable site (its text and images were generated by Lovable's AI), supplied its source and asked for this edition; responsibility is his. Claude read the Lovable source, checked its claims against Aquanuity's pages, the Environment Agency report and Bob's 22 October webinar report, and wrote both solvers, the calculators, the mesh generator, the charts, the page code, the corrected text, the Audit register, the Doc essay and the .docx. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first single-file edition (the version read). The Lovable original (TanStack Start template, two routes) is version 0 here.
