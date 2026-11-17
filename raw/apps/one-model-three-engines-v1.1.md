---
name: One Model, Three Engines
file: one-model-three-engines.html
version: "1.1"
date: 2026-11-02
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NwcWSDXyvyDCXvNXwPvj4t", repo: none named in the page}
engines:
  - {name: "teaching solvers in the page (backwater profile and a lumped kinematic spin-up chain), written in JavaScript", version: "1.1", license: not stated in the page}
  - {name: InfoSewer, ICM InfoWorks and ICM SWMM, version: not stated, note: "the study's engines; none runs in the page"}
units: US customary (ft, cfs, ft/s, ft3)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says the app and its essay were built with Claude (Opus 5.5) under Robert Dickinson's direction, and that the study itself is his. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/NwcWSDXyvyDCXvNXwPvj4t, version 1793654421-62b5 (index.html, 1,529,783 bytes, SHA-256 d1542eb27f7332305167e32ff60b04adceaeed83f55b5b7dc7ac2834672677fb), its About and Doc tabs read in headless Chromium on 2026-11-16. No model was run to write this file."
---

# One Model, Three Engines: moving the InfoSewer training model into ICM InfoWorks and ICM SWMM

## In three points
- **What:** A 2026 field guide to moving the InfoSewer training model into ICM InfoWorks and ICM SWMM: the seven steps, a compare tool, and labs on backwater and spin-up.
- **So what:** In the teaching pipe both methods carry 1.2 cfs, but backwater puts 0.76 ft at mid-length against 0.56 ft at normal depth, 35 percent deeper and 32 percent slower, which is why matching flow does not prove a conversion.
- **Now what:** After a conversion, compare depth and velocity as well as flow. Neither ICM engine runs in the page; its teaching solvers are lumped models.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 1.1 · 2026-11-02"). Every number below is copied from the page's About tab or its Doc essay. No engine was run to write this file.

## What it does

A 2026 field guide to moving the InfoSewer training model into ICM InfoWorks and ICM SWMM: the updated introduction, the seven steps with what to check after each, and two small labs that show why flow matched while depth and velocity did not, and why a one-minute run from a saved state is a steady state. The study behind it is Bob's: the InfoSewer training model, its import to ICM InfoWorks, the conversion to ICM SWMM, the Ruby comparison, two load fixes, the saved-state runs and their verdict, and a 315-location comparison. The page says the study's run dates and software builds are not recorded in it.

Tabs: Intro (the 2026 introduction and the study record), Workflow (the seven steps; steps 4 and 5 carry Ruby), Backwater, Steady State, Break It, Compare (pairs two tables by ID, checks field definitions, scores agreement with a reference using the a + r|A| rule, median and 90th percentile), About, Doc.

## Results the page reports (computed by its teaching solvers, not by ICM)

- Teaching pipe: 15 inches, slope 0.002, Manning n 0.013, 300 ft, 1.2 cfs, 1.00 ft of water at the outlet. Normal depth 0.56 ft at 2.25 ft/s. The backwater profile puts 0.76 ft at mid-length, 35 percent deeper, at 1.54 ft/s, 32 percent slower. Both carry exactly 1.2 cfs.
- Twelve teaching pipes compared at mid-length: depth misses by up to 0.47 ft and velocity by up to 1.22 ft/s, while flow lies on the one-to-one line "because both methods were handed the same discharge."
- Spin-up chain: 15 pipes of 15-inch diameter, 300 ft each at slope 0.003, 2.0 cfs of load, about 1,844 ft3 stored at steady state. Started dry, the outlet sees 1.1 percent of the flow after one minute and 99 percent after about 35 minutes.
- One-minute equilibrium test from a saved state at full load: the largest change in any pipe's flow is 5.3e-7 cfs and stored volume changes by 2.0e-5 ft3. From a state saved at 80 percent of the load, the outlet still reports 1.62 cfs of the 2.0 cfs after one minute.
- Break It (six 15-inch pipes, 300 ft at 0.002, 0.3 cfs at every manhole, free outfall): shrinking pipe 3 to 12 inches leaves every flow unchanged while its mid-length depth goes from 0.48 to 0.54 ft; holding the outfall at 1.1 ft raises the last pipe's depth from 0.71 to 0.91 ft; moving the load from manhole 2 to manhole 5 leaves the outlet at 1.80 cfs while pipes 2, 3 and 4 each carry 0.3 cfs less.

## Checks (as stated on the page)

- The physics and the compare engine pass 56 automated checks run in Node before each build. Among them: a profile started at normal depth stays there; 400 and 1,600 integration steps agree to better than 1e-7 ft; velocity times area returns the flow everywhere; the spin-up chain closes its mass balance to one part in a million.
- An external review of version 1.0 independently reproduced the default backwater numbers (normal depth 0.5616 ft, mid-length depth 0.7601 ft, velocity 1.5362 ft/s) and the teaching chain's (1,844.4 ft3 stored, 35.02 minutes to 99 percent, 1.6201 cfs after a minute from the 80 percent state).
- Claude confirmed the ArcMap retirement terms on Esri's page and the InfoSewer result-field list on its help page. The Word file was rendered to pages and read.

## What this does not show

- Neither ICM engine runs here. The spin-up chain is a lumped kinematic model; its fill times move by about 12 percent when every pipe is split in two, so the page says to read them as minutes-scale.
- The teaching solver stops at 95 percent of the diameter and hands steep pipes to normal depth; steep, supercritical pipes and jumps are outside the method.
- The Ruby snippets use field names from Bob's own ICM scripts but were not run in ICM.
- The ICM help passages on the SWMM5 exporter and InfoWorks initialization are cited from the review; Claude could not open those pages.
- The essay's account of the study is written from Bob's notes and has not yet had his review.

## How to reproduce

Open the page. Backwater, Steady State and Break It compute in the browser. Compare takes two pasted tables or a study bundle. Exports carry their provenance (CSV) and GIF captions.

## Credits and licenses

Esri, "Deprecation: ArcGIS Desktop" (retirement March 1, 2026). InfoSewer help, Group Gravity Main Graph. Autodesk One Water Blog, "Model-aware AI in InfoWorks ICM 2027.2" (Oct 14, 2026). The page's byline: Robert Dickinson, SWMM Enablement; Bore Shell 1.0.0.

## AI use

The page says the app and its essay were built with Claude (Opus 5.5), Anthropic's AI model, in a Claude session on 2 November 2026, under the direction of Robert (Bob) Dickinson, who did the study and wrote and approved the introduction this edition updates. Claude rewrote the introduction for 2026, wrote the physics, figures, scorecard, GIF recorder, page, essay and Word copy, and the Ruby snippets; in 1.1 it answered an external review of 1.0. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 1.1 (2026-11-02): answers an external review of 1.0 (76/100, provisional). Corrected the claim that matching flow proves a conversion; added Break It and the study record; rebuilt Compare; separated InfoWorks initialization from saved states and added the one-minute equilibrium test; corrected Figure 9; rewrote both Ruby utilities. Fixed a solver bug that held free-outfall drawdown profiles flat at critical depth (0.43 ft over the full 300 ft); the drawdown now reaches 0.50 ft at 10.54 ft from the outlet.
- 1.0 (2026-11-02): first edition.
