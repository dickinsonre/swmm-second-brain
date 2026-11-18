---
title: "S360: HydroCalc Studio, summary written from the page (v1.0)"
type: source
raw: raw/apps/hydrocalc-studio-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, open-channel, calculators, gradually-varied-flow]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app HydroCalc Studio, version 1.0: eight open-channel and routing calculators, each showing its equation. Raw file: [raw/apps/hydrocalc-studio-v1.0.md](../../raw/apps/hydrocalc-studio-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/GHZMYWwrXZ4uMi7EP3y26i, version 1792899145-f09d (index.html, 1,075,858 bytes, SHA-256 ee41cc5faa4548fb19956d3aa79b91f82cbfc679d0d12fe8a90b82fb65a9b838), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and set the standing requirements (dark by default, US units, a Doc tab and .docx, disclosure); responsibility is his."

**Claims worth keeping** (all copied from the file)
- Eight calculators in one file: Manning's equation, a compound channel by the divided channel method, gradually varied flow profiles, rating curves, a single Muskingum step, full hydrograph routing, a sensitivity study and a side-by-side channel comparison. Every result shows the equation it came from with your numbers in it.
- The Lovable original drew its flow profile as normal depth with a 5% sine wave on it; this edition solves the gradually varied flow by direct step with an RK4 cross-check and classifies M, S, C, H and A profiles. Its unit switch only relabeled values (now it converts them), and it used k = 1.49 for Manning (now 1.486, a 0.27% change). 44 automated checks pass, including the US default Manning flow of 8,165.6 cfs and the Muskingum coefficients 0.1304, 0.3043 and 0.5652.
- Hand calculations: Manning for the US default (8,165.6 cfs) and the first version's SI default (264.2 m3/s); Muskingum coefficients 0.1304, 0.3043, 0.5652; the textbook outflow of 105.217 cfs.
- Invariance: the same channel in feet and in metres gives the same discharge to twelve significant figures; the M1 profile matches to better than 0.01%.
- Two methods: direct step and RK4 agree to 0.0001% on M1 and 0.13% on M2; refining from 600 to 2,400 depth steps changes the answer by less than one part in a million; the energy equation holds on every step.
- Classification: M1, M2, M3, S1, S2, S3, H2 and A2 each labelled correctly and heading the right way. Plus the Lovable defaults reproduced, grid refinement and Muskingum continuity.

**Limits it states.** As the page lists it: everything is steady and one-dimensional; routing is hydrologic (linear storage with constant K and x), so no backwater from a tributary, looped rating, or a wave whose speed changes with depth; the profile stops at critical depth, with no jumps, drops, bridges, culverts or section changes, in prismatic channels with one n and one slope; the compound channel is rectangles with vertical divisions and no momentum exchange at the interface (Knight and Shiono's method would add it).

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [HydroCalc Studio (app)](../entities/hydrocalc-studio.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Non-Prismatic Channel Lab (app)](../entities/non-prismatic-channel-lab.md).
