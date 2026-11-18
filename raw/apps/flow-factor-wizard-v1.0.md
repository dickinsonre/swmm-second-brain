---
name: Flow Factor Wizard
file: flow-factor-wizard.html
version: "1.0"
date: 2026-10-21
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/1P5BTszyz3tQhafCSV47ov", original: "the flow-factor-wizard React project (Lovable) and its v2.0 InfoWorks ICM Ruby script", repo: none named in the page}
engines: none (closed-form peaking formulas; generates an InfoWorks ICM Ruby script, v2.1, that was run only on a mock of the ICM Ruby API)
units: US customary by default (gal/person/day, ft3/s, gpm, MGD), SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1P5BTszyz3tQhafCSV47ov, version 1792633172-adad (index.html, 1,286,318 bytes, SHA-256 8016042db3a657c9c2bd494aa8bc9a91c03d6575d8067787d2a1e8cda778eb95), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Flow Factor Wizard: peakable sanitary flow for InfoWorks ICM, computed the InfoSewer way

## In three points
- **What:** Computes peakable (design) sanitary flow from population, Q = EFF x population x average flow per person, with EFF from a peaking formula (Harmon, Babbitt, custom) capped at a cutoff, and generates an InfoWorks ICM Ruby script (v2.1) that does the same for every conduit after adding up the population upstream of each one. The idea comes from InfoSewer, whose steady-state run peaks loads before routing them.
- **So what:** Peaks do not add. In the default example, 16,600 people together peak at 7.022 ft3/s (EFF 2.73), while the sum of five separate peaks is 8.043 ft3/s, 14.5% over. The source had six numbered defects (FFW-1 to FFW-6): its Harmon preset lost the 4 in 1 + 14/(4 + √P), so at 1,000 people it gave 15.0 where Harmon gives 3.80, and the browser used thousands of people while the v2.0 Ruby script used persons.
- **Now what:** Use it to size sanitary peaks and to generate the ICM script. Nobody has run v2.1 inside InfoWorks ICM; it was run on a mock of the ICM Ruby calls. No metered flows, no infiltration or inflow, and it approximates InfoSewer's population peaking without reproducing an InfoSewer run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · single-file build 2026-10-21"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Calculator, Compare (all formulas on a log axis), Formulas, Ruby Script (v2.1 generated from the settings, v2.0 kept for comparison), About, Doc. Inputs: units, peaking formula (Harmon in the Ten States form, Babbitt, the two v2.0 presets as shipped, custom coefficients c1 to e2), whether P is in thousands or persons, average flow per person (100 gal/person/day in the example, 1.5472e-4 ft3/s per person), the reporting unit, the EFF cutoff (6 in the example) and the populations served. CSV import and export.

## Checks (as stated on the page)

- Presets against published forms: the Ten States expression and 1 + 14/(4 + √P) agree within 9 x 10^-16 from P = 0.01 to 1,000; Babbitt matches 5/P^0.2 by construction.
- The source's own numbers: with its defaults the source computes 1.388889, 6.944444, 13.888889, 69.444444 and 125.629369 L/s; the app's core returns the same five.
- v2.0 run, not just read: a mock of the ICM Ruby calls the script uses (row_object_collection, us_links, ds_links, write) ran the uploaded v2.0 script on the demo network; a JavaScript port of its trace gave the same contributing populations.
- v2.1 written in five settings (ft3/s, gpm, MGD, L/s, m3/s; Harmon, Babbitt, a v2.0 preset and a custom formula); each passed ruby -c and ran on the mock.
- Defect register: FFW-1 Harmon lost its 4; FFW-2 a Modified Harmon with no published source (1 + 18/(4 + √P), 4.60 at 1,000 people, 21% above Harmon), kept only as a labelled legacy preset; FFW-3 thousands in the browser, persons in ICM; FFW-4 twin barrels each took the first barrel's share; FFW-5 a split that rejoins lost one branch; FFW-6 a total that added peaks.

## What this does not show

As the page lists it: v2.1 has not run inside InfoWorks ICM; the subcatchment lateral-links branch carried over from v2.0 was not exercised; no metered flows; flow splits by pipe area are the script's assumption, inherited from v2.0; no infiltration or inflow; it approximates InfoSewer's population peaking, it does not reproduce an InfoSewer run; one synthetic nine-conduit network and one five-link loop test.

## Credits and licenses

W. G. Harmon (Engineering News-Record, 1918, from flows measured at Toledo, Ohio); Ten States Standards; Babbitt; InfoSewer's help on base-flow and coverage-flow peaking. Bore Shell 1.0 chrome. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the flow-factor-wizard source and its v2.0 Ruby script and asked for a single-file HTML app; responsibility is his. Claude read the React source and the Ruby script, checked the presets against published forms, found the six defects, and wrote the app, the v2.1 Ruby generator, a mock of the InfoWorks ICM Ruby API to run both scripts, the figures, the essay and its Word copy. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-21): first single-file edition, with Ruby v2.1 (the version read).
