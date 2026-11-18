---
title: "Storm Sewer Manhole (app)"
type: entity
updated: 2026-11-18
sources: [S269]
tags: [apps, manholes, surcharge, flooding, teaching, si-units]
reviewed: no
---
Bob's app Storm Sewer Manhole: a one-page explainer that cuts a street, a manhole and its two 24 in (600 mm) pipes in half and steps a storm through it in eight steps, from dry weather to the cover lifting and draining down, built in SI units. Version and date 2026-10-20 [S269](../sources/S269-storm-sewer-manhole-summary.md). Its `links:` line names no live Netlify address [S269](../sources/S269-storm-sewer-manhole-summary.md).

**A caution about its source.** The page ships no technical summary. [S269](../sources/S269-storm-sewer-manhole-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S269](../sources/S269-storm-sewer-manhole-summary.md)
- The water level in a manhole is the pressure in the pipe: the storm's peak inflow of 35.7 cfs (1,011 L/s) is 2.3 times what the pipe carries full, 15.3 cfs (434 L/s), so the manhole supplies the extra head.
- Head once the pipe is full: H = D + (Sf - S0) L + K v^2/2g, with Sf = S0 (Q/Qfull)^2; the cover lifts when H reaches its underside plus its weight as a water depth, 0.64 ft (0.195 m) for a 121 lb (55 kg) cover.
- The cover is up 12 minutes and 1,236 ft3 (35 m3) floods the street (flow above 33.0 cfs, or 935 L/s).
- The page grades each number: solid, estimate or illustration (the storm, 3.7 in/hr or 95 mm/h at peak, and the 14.8 ac or 6 ha catchment are illustrations).

**What it does not show.** Each instant is treated as steady flow, so it leaves out the storage in the shaft and the surge a dynamic-wave model would capture; the US figures are the summary's conversions of the page's SI. It may be a later version of an older site (inside-the-node or inside-the-vault). [S269](../sources/S269-storm-sewer-manhole-summary.md)

**Noted at ingest.** 35.7 / 15.3 = 2.33, the 2.3 times stated (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
