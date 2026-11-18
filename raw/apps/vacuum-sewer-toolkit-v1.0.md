---
name: Vacuum Sewer Toolkit
file: vacuum-sewer-toolkit.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/JHc3kwDu7L4ny8PtxrPutt", original: "Lovable app vcruby (source export of 25 October 2026: 126 files, 27 feature screens)", repo: none named in the page}
engines:
  - {name: vac.js, note: "the page's engine, pure functions in SI internally"}
  - {name: EPA SWMM, version: "5.2 (pyswmm 2.2.0, swmm-toolkit 0.17.0)", note: "both exported .inp files run while building"}
units: US customary by default, SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/JHc3kwDu7L4ny8PtxrPutt, version 1792957476-aa88 (index.html, 1,607,607 bytes, SHA-256 377b103539090e0c575eed7be4e94ae24206bfc979db8b9716d4868288f8f866), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Vacuum Sewer Toolkit: EPA 1991 vacuum sewer design and InfoWorks ICM Ruby, corrected

## In three points
- **What:** A single-file rebuild of Bob's Lovable app vcruby (126 files, 27 feature screens, 19,586 lines of TypeScript and 508 of Ruby by its own count): vacuum sewer design after the EPA 1991 manual and published state criteria, calculators, diagrams, components, comparisons with gravity, costs, and InfoWorks ICM Ruby scripts. The three ICM scripts are replaced by four corrected ones.
- **So what:** The corrections register lists 35 entries (code 9, method 2, contradiction 4, number 6, practice 1, table 1, removed 5, physics 3, label 3, unsupported 1). The worst (C1): for a 320 m to 330 m guide the original sawtooth generator made inverts of 320, 319, 332, 329 and 330, one 13 m lift and 14 m of rise from a single pipe, three times the whole 13 ft (3.96 m) static budget. The engine passes 86 of 86 checks, the corrected Ruby 15 of 15 in a stand-in ICM, and both exported .inp files run clean in SWMM 5.2.
- **Now what:** Use it to lay out a vacuum main and its lifts, and to take the design into ICM. Friction is single-phase Hazen-Williams (the AIRVAC two-phase charts are not reproduced), no script has run inside ICM, and costs are the original's 1990 unit costs times an inflation factor.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("single-file edition 1.0", from the source export of 25 October 2026). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Overview, Calculator, Diagrams, Components, Compare, Costs, ICM Ruby, Advanced, About, Doc. Every original screen is here; the About tab maps each original file to where its content went. The sawtooth designer keeps both guide inverts, runs at the run slope and uses the fewest lifts no taller than the largest lift you allow, with the same algorithm in the browser and in Ruby. The Advanced tab offers a two-phase correction by Lockhart and Martinelli's correlation. Corrections export as CSV; the write-up as .docx.

## Checks (as stated on the page)

- Engine vac.js: 86 of 86 checks pass.
- Corrected ICM Ruby: 15 of 15 in a stand-in ICM harness; the original scripts were also run in that harness.
- SWMM 5.2 (pyswmm 2.2.0, toolkit 0.17.0) ran both exported .inp files with no errors or warnings; continuity error 1.60% (demo) and 0.15% (sawtooth).
- Published criteria looked up: WEF (via PDHengineer), Florida DEP, Texas 217.98, EPA 1991; the Innovyze examples.

## What this does not show

As the page lists it: friction is single-phase; the two-phase correction uses a correlation built for steady separated flow in straight pipe, while a vacuum main runs in slugs and the multiplier depends heavily on the air assumed; no script has run inside ICM; costs are 1990 unit costs times an inflation factor. The demo network is synthetic.

## Credits and licenses

US EPA (1991) vacuum sewer manual; WEF; Florida DEP; Texas 30 TAC 217.98; Lockhart and Martinelli; Innovyze ICM Ruby examples; pyswmm and swmm-toolkit. The Lovable vcruby is Robert Dickinson's. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original app, supplied its source and is responsible for the work. Claude read the 126-file source, wrote the engine, the four corrected Ruby scripts, the stand-in ICM harness and the tests, ran the original scripts in that harness, looked up the published criteria and the Innovyze examples, built the synthetic demo network, rebuilt every screen, and wrote the corrections register and the Doc essay. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first single-file edition (the version read).
