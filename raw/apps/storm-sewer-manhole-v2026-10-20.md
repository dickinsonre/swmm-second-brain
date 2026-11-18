---
name: Storm Sewer Manhole
file: storm-sewer-manhole.html
version: "2026-10-20"
date: 2026-10-20
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SUBzd6jxte3TaWJAYyRf7N", repo: none named in the page}
engines: none (one small steady-flow model in the page's script; no SWMM engine)
units: SI (m, mm, L/s, m3) as the page uses them; US figures here are our conversions
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with AI assistance (Claude). See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SUBzd6jxte3TaWJAYyRf7N, version 1792537411-94f2 (index.html, 45,726 bytes, SHA-256 b222529484eb0eb63ff7b2c91ec167d91c17f0ac7f3d87c572ba99b6ac231378), its rendered text read in headless Chromium on 2026-11-17 (the page has no About or Doc tab). Nothing was run to write this file; the date is the artifact's last update."
---

# Storm Sewer Manhole: how a manhole works, in eight storm steps

## In three points
- **What:** A one-page explainer that cuts a street, a manhole and its two 24 in (600 mm) pipes in half and steps a storm through it, from dry weather to the cover lifting and draining down, with every number from one small model in the page.
- **So what:** Its big idea is that the water level in a manhole is the pressure in the pipe: the storm's peak inflow of 35.7 cfs (1,011 L/s) is 2.3 times what the pipe carries full, so the manhole must supply the extra head, lifts its 121 lb (55 kg) cover and puts 1,236 ft3 (35 m3) on the street.
- **Now what:** Use it to explain surcharge and flooding at a junction to someone new to sewers. Each instant is treated as steady flow, so it leaves out the storage in the shaft and the surge a dynamic-wave model such as SWMM's would capture.

This summary was written after the fact. The page ships no technical summary and no version of its own, so the version above is the artifact's last update. The file name is ours. Every number below is copied from the page's "Where the numbers come from" table; the US figures in parentheses are our conversions. Nothing was run to write this file.

## What it does

The page opens "Someone asked me: How does a manhole work?" Eight buttons step the storm: dry weather, rain starts, pipe runs full, surcharge, cover lifts, rain eases, drain down, next storm. A section drawing shows the inlet and outlet pipes, the channel and bench, the cone, the pressure line and the cover. Live readouts give storm time, rain, inflow, pipe capacity, outflow, depth, depth above the crown, velocity, the push on the cover against its weight (540 N) and flooding. A GIF maker records all seven storm steps.

## How it computes (as the page states it)

- Rain on the catchment becomes inflow through a linear reservoir.
- The outlet pipe carries it by Manning's equation while it runs part full.
- Once inflow passes the pipe's full capacity, the manhole supplies the extra head: H = D + (Sf - S0) L + K v^2/2g, with Sf = S0 (Q/Qfull)^2.
- When H reaches the cover's underside plus the cover's weight expressed as a water depth, the cover lifts and the extra flow floods the street.
- The page notes that SWMM tracks the same three things at a junction: depth, surcharge above the crown, and flooding above the rim.

## The numbers (as the page labels them)

| Number | How sure | Source or reasoning |
|---|---|---|
| 24 in (600 mm) pipe, n 0.013, 0.5 % | estimate | Typical storm sewer choices; the slope is the page's pick |
| 15.3 cfs (434 L/s) full | solid | Manning's equation for that pipe running just full |
| 48 in (1,200 mm) shaft, 24 in (600 mm) opening, 7.9 ft (2.4 m) deep | solid | Common standard sizes; the depth is the page's pick |
| 121 lb (55 kg) cover | estimate | Ductile iron 600 mm covers weigh roughly 40 to 60 kg |
| 0.64 ft (0.195 m) to lift it | solid | Cover weight / (water density x g x cover area) |
| 3.7 in/hr (95 mm/h) peak, gamma shape | illustration | A design-style storm, not a gauge record |
| 14.8 ac (6 ha), C 0.75, 8 min lag | illustration | A few city blocks, mostly paved, through a linear reservoir |
| 35.7 cfs (1,011 L/s) peak inflow | estimate | The model's result at 26 min, 2.3 times what the pipe carries full |
| Exit loss K 0.5 | estimate | Published values run from about 0.2 to over 1 |
| Next manhole 295 ft (90 m) away, water at its crown | estimate | Assumed downstream condition |
| 0.28 cfs (8 L/s) dry weather | illustration | Groundwater infiltration |
| 1,236 ft3 (35 m3) flooded | estimate | Flow above 33.0 cfs (935 L/s), what the pipe carries with the cover just floating, summed over the 12 minutes the cover is up |

## Checks

None stated beyond the labels in the table. Checked here by arithmetic: Manning for a full 0.6 m pipe at n 0.013 and S 0.005 gives 0.434 m3/s; 55 kg / (1,000 kg/m3 x 0.283 m2) = 0.195 m; 1,011 / 434 = 2.33; 55 kg x 9.81 m/s2 = 540 N.

## What this does not show

- Each instant is treated as steady flow. The water stored in the shaft (about 11.8 ft2, 1.1 m2, of floor area) and dynamic-wave surge are left out.
- The drawing keeps the pipes level and leaves out the 0.5 % slope (about 0.8 in, 2 cm, across the block).
- The numbers come from a simple model, not from a monitored sewer. No SWMM run.

## How to reproduce

Open the page and step through the eight storm buttons; the readouts update with each step.

## Credits and licenses

No license is stated in the page.

## AI use

The page says "Built with AI assistance (Claude). The numbers come from a simple model, not from a monitored sewer." It names no session or date. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026-10-20: the version read.
