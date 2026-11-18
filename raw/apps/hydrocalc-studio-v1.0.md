---
name: HydroCalc Studio
file: hydrocalc-studio.html
version: "1.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/GHZMYWwrXZ4uMi7EP3y26i", original: "Lovable project HydroCalc Studio (React, shadcn/ui, Recharts), hydrocalcred.lovable.app", repo: none named in the page}
engines: none (closed-form and step calculators written for the page)
units: US customary by default (ft, ft2, cfs, ft/s, ac-ft; hours), SI behind a toggle that converts values
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/GHZMYWwrXZ4uMi7EP3y26i, version 1792899145-f09d (index.html, 1,075,858 bytes, SHA-256 ee41cc5faa4548fb19956d3aa79b91f82cbfc679d0d12fe8a90b82fb65a9b838), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# HydroCalc Studio: eight open-channel and routing calculators, each showing its equation

## In three points
- **What:** Eight calculators in one file: Manning's equation, a compound channel by the divided channel method, gradually varied flow profiles, rating curves, a single Muskingum step, full hydrograph routing, a sensitivity study and a side-by-side channel comparison. Every result shows the equation it came from with your numbers in it.
- **So what:** The Lovable original drew its flow profile as normal depth with a 5% sine wave on it; this edition solves the gradually varied flow by direct step with an RK4 cross-check and classifies M, S, C, H and A profiles. Its unit switch only relabeled values (now it converts them), and it used k = 1.49 for Manning (now 1.486, a 0.27% change). 44 automated checks pass, including the US default Manning flow of 8,165.6 cfs and the Muskingum coefficients 0.1304, 0.3043 and 0.5652.
- **Now what:** Use it to teach and check steady 1D channel hydraulics and hydrologic routing. Nothing here solves the Saint-Venant equations; Muskingum cannot represent backwater or a looped rating; the profile stops at critical depth.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Manning's equation, Compound channel, Flow profile, Rating curve, Muskingum step, Hydrograph routing, Sensitivity, Compare channels, Reader, Data pool, About, Doc. Constants: Manning k = (1/0.3048)^(1/3) = 1.4859 in US units, 1 in SI; g = 32.174 ft/s2 or 9.80665 m/s2. The compound channel uses one water surface and bank heights, stops counting the water-to-water interface as main-channel perimeter, and shows α and a lumped-section comparison. Muskingum tabs check the stability window; the hydrograph tab reports storage as a volume. Rating curves gain h0, a visible velocity width and a fit to gaugings. Tables export; the Reader carries method notes and opens your own .md files (the original's 815 KB of textbook text is not included).

## Checks (as stated on the page)

44 checks on the hydraulics core, all passing, run outside the browser on the same block of pure functions the page uses:
- Hand calculations: Manning for the US default (8,165.6 cfs) and the first version's SI default (264.2 m3/s); Muskingum coefficients 0.1304, 0.3043, 0.5652; the textbook outflow of 105.217 cfs.
- Invariance: the same channel in feet and in metres gives the same discharge to twelve significant figures; the M1 profile matches to better than 0.01%.
- Two methods: direct step and RK4 agree to 0.0001% on M1 and 0.13% on M2; refining from 600 to 2,400 depth steps changes the answer by less than one part in a million; the energy equation holds on every step.
- Classification: M1, M2, M3, S1, S2, S3, H2 and A2 each labelled correctly and heading the right way. Plus the Lovable defaults reproduced, grid refinement and Muskingum continuity.

## What this does not show

As the page lists it: everything is steady and one-dimensional; routing is hydrologic (linear storage with constant K and x), so no backwater from a tributary, looped rating, or a wave whose speed changes with depth; the profile stops at critical depth, with no jumps, drops, bridges, culverts or section changes, in prismatic channels with one n and one slope; the compound channel is rectangles with vertical divisions and no momentum exchange at the interface (Knight and Shiono's method would add it).

## Credits and licenses

Manning; the divided channel method; direct step and RK4; Muskingum (McCarthy); Knight and Shiono named as the method not used. The Lovable HydroCalc Studio is Robert Dickinson's. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and set the standing requirements (dark by default, US units, a Doc tab and .docx, disclosure); responsibility is his. Claude read the Lovable source and found the defects listed in the Doc tab, and wrote the hydraulics core, the charts, the GIF encoder, every calculator, the report generator, the Reader's method notes and the Doc essay with its figures, and built the .docx. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first single-file edition (the version read).
