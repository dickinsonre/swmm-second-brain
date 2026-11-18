---
title: "EPANET Total Head Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S277]
tags: [apps, epanet, head, solver, javascript-port, verification]
reviewed: no
---
Bob's app EPANET Total Head Explorer: a teaching explorer built on a JavaScript port of the EPANET 2.2 hydraulic solver, run on the EPANET manual's tutorial network (Listing C.1), from the three heads at one point to the network solve trial by trial. Version and date 2026-11-03 [S277](../sources/S277-epanet-total-head-explorer-summary.md). Netlify address, from its `links:` line: https://epanet-total-head-explorer.netlify.app [S277](../sources/S277-epanet-total-head-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S277](../sources/S277-epanet-total-head-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S277](../sources/S277-epanet-total-head-explorer-summary.md)
- On the tutorial network the port agrees with compiled EPANET 2.2 and OWA-EPANET 2.3.5 to 4.4 x 10^-12 ft in head and 6.4 x 10^-11 gpm in flow over all 25 hourly steps, with equal trial counts and times; the two compiled engines are byte-identical.
- On 300 random small networks the port agrees with EPANET 2.2 to 4.0 x 10^-8 ft in 241 and to 1.7 x 10^-4 ft in 59.
- The first 2026 edition used 2.31 ft per psi and put node 2 at 386.66 psi instead of 387.02 (defect APP-1); pressure now uses EPANET's 0.4333 psi per ft (2.3079 ft per psi).
- The manual's printed Listing C.2 for hours 0 and 1: 14 of 14 node rows and 7 of 7 link rows within the printed precision; pump head -193.19 ft.

**What it does not show.** No valves, controls, rules, emitters, pressure-driven demand or water quality, and such input is refused; only gpm; the random networks are small; no person has read the port line by line against the C source. [S277](../sources/S277-epanet-total-head-explorer-summary.md)

**Noted at ingest.** At node 2, hour 0: 73.52 / 0.4333 = 169.67 ft, and 710 + 169.67 = 879.67 ft; the velocity head 2.98^2 / 64.4 = 0.138 ft (our arithmetic agrees).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [EPANET](epanet.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).
