---
title: "Flow Factor Wizard (app)"
type: entity
updated: 2026-11-18
sources: [S336]
tags: [apps, sanitary-flow, peaking, infosewer, icm, ruby]
reviewed: no
---
Bob's app Flow Factor Wizard: peakable sanitary flow for InfoWorks ICM, computed the InfoSewer way. Version 1.0, 2026-10-21 [S336](../sources/S336-flow-factor-wizard-summary.md). Its `links:` line names no live Netlify address [S336](../sources/S336-flow-factor-wizard-summary.md).

**A caution about its source.** The page ships no technical summary. [S336](../sources/S336-flow-factor-wizard-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S336](../sources/S336-flow-factor-wizard-summary.md)
- Computes peakable (design) sanitary flow from population, Q = EFF x population x average flow per person, with EFF from a peaking formula (Harmon, Babbitt, custom) capped at a cutoff, and generates an InfoWorks ICM Ruby script (v2.1) that does the same for every conduit after adding up the population upstream of each one. The idea comes from InfoSewer, whose steady-state run peaks loads before routing them.
- Peaks do not add. In the default example, 16,600 people together peak at 7.022 ft3/s (EFF 2.73), while the sum of five separate peaks is 8.043 ft3/s, 14.5% over. The source had six numbered defects (FFW-1 to FFW-6): its Harmon preset lost the 4 in 1 + 14/(4 + √P), so at 1,000 people it gave 15.0 where Harmon gives 3.80, and the browser used thousands of people while the v2.0 Ruby script used persons.
- Presets against published forms: the Ten States expression and 1 + 14/(4 + √P) agree within 9 x 10^-16 from P = 0.01 to 1,000; Babbitt matches 5/P^0.2 by construction.
- The source's own numbers: with its defaults the source computes 1.388889, 6.944444, 13.888889, 69.444444 and 125.629369 L/s; the app's core returns the same five.
- v2.0 run, not just read: a mock of the ICM Ruby calls the script uses (row_object_collection, us_links, ds_links, write) ran the uploaded v2.0 script on the demo network; a JavaScript port of its trace gave the same contributing populations.
- v2.1 written in five settings (ft3/s, gpm, MGD, L/s, m3/s; Harmon, Babbitt, a v2.0 preset and a custom formula); each passed ruby -c and ran on the mock.

**How to use it, as the summary puts it.** Use it to size sanitary peaks and to generate the ICM script. Nobody has run v2.1 inside InfoWorks ICM; it was run on a mock of the ICM Ruby calls. No metered flows, no infiltration or inflow, and it approximates InfoSewer's population peaking without reproducing an InfoSewer run. [S336](../sources/S336-flow-factor-wizard-summary.md)

**What it does not show.** As the page lists it: v2.1 has not run inside InfoWorks ICM; the subcatchment lateral-links branch carried over from v2.0 was not exercised; no metered flows; flow splits by pipe area are the script's assumption, inherited from v2.0; no infiltration or inflow; it approximates InfoSewer's population peaking, it does not reproduce an InfoSewer run; one synthetic nine-conduit network and one five-link loop test. [S336](../sources/S336-flow-factor-wizard-summary.md)

**Noted at ingest.** 8.043 / 7.022 = 1.145, the 14.5% over stated (our arithmetic).

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [InfoWorks ICM](infoworks-icm.md).
