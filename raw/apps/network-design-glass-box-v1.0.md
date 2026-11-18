---
name: Network Design Glass Box
file: network-design-glass-box.html
version: "1.0"
date: 2026-09-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/GqDyhpCKrdwfBEUAQGJAsK", repo: none named in the page}
engines:
  - {name: none in the page, note: "design core checked against EPA SWMM 5.2.4 on the eight presets"}
units: SI (m, mm, L/s, m/s) as the page uses them; US figures here are our conversions
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/GqDyhpCKrdwfBEUAQGJAsK, version 1790741819-2050 (index.html, 102,835 bytes, SHA-256 78a3bf8b335e5cc750f3bd1d15582054747fe8cdd3a36941ad102509026f1509), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Network Design Glass Box: a from-scratch, rule-based pipe sizer with every decision shown

## In three points
- **What:** A from-scratch version of the rule-based pipe sizer Autodesk describes for InfoWorks ICM Ultimate 2027 (Network Design): penalty weights pick among sizes that pass the design rules, relaxed rules are tried when none passes, and every pipe's deciding rule is shown.
- **So what:** In the default network every pipe meets the rules, and the report says why each size was chosen; for example P5 is 900 mm (35.4 in, our conversion) at 0.634% carrying 1,409 L/s (49.8 cfs) at 2.58 m/s (8.46 ft/s), and 750 mm fails as smaller than an upstream pipe.
- **Now what:** Use it to see how a rule-based sizer decides before trusting one. It is built from Autodesk's public description, not ICM's code, and its network and rainfall are invented.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-09-30"). The file name above is ours. Every number below is copied from the page; US conversions are ours. Nothing was run to write this file.

## What it does

Tabs: Design, Report, Verify, Sources. Presets: Balanced, Shallow trench, Tight outfall, Tight outfall with shallow weights, Velocity cap on steep ground, Cover cap over a rise, Invert matching, Existing pipe locked. Rules include minimum and maximum slope, velocity (checked at design-flow depth or full bore), cover to crown, maximum depth in pipe, soffit-to-soffit or invert-to-invert matching, never smaller than upstream, and an outfall's lowest invert.

## Checks (as stated on the page)

- Default design, P5: 900 mm (35.4 in, our conversion) at 0.634%, carrying 1,409 L/s (49.8 cfs) at 80% depth and 2.58 m/s (8.46 ft/s); slope set by percentage full; 750 mm fails on connectivity and maximum velocity.
- Hydraulics checked against EPA SWMM 5.2.4 on the eight presets (Verify tab).

## What this does not show

- Anything about how InfoWorks ICM's own Network Design behaves.
- The demo network and the rainfall curve are invented.

## How to reproduce

Open the page, pick a preset, and read the Report; Export writes the design.

## Credits and licenses

Autodesk's public description of Network Design in InfoWorks ICM Ultimate 2027 (no code). EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-09-30): first version.
