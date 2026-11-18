---
title: "S269: Storm Sewer Manhole, summary written from the page (v2026-10-20)"
type: source
raw: raw/apps/storm-sewer-manhole-v2026-10-20.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, manholes, surcharge, flooding, teaching, si-units]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Storm Sewer Manhole, version 2026-10-20: a one-page explainer that cuts a street, a manhole and its two 24 in (600 mm) pipes in half and steps a storm through it in eight steps, from dry weather to the cover lifting and draining down, built in SI units. Raw file: [raw/apps/storm-sewer-manhole-v2026-10-20.md](../../raw/apps/storm-sewer-manhole-v2026-10-20.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/SUBzd6jxte3TaWJAYyRf7N, version 1792537411-94f2 (index.html, 45,726 bytes, SHA-256 b222529484eb0eb63ff7b2c91ec167d91c17f0ac7f3d87c572ba99b6ac231378), its rendered text read in headless Chromium on 2026-11-17 (the page has no About or Doc tab). Nothing was run to write this file; the date is the artifact's last update." The page carries the note "Built with AI assistance (Claude)" and ships no technical summary or tabs.

**Claims worth keeping** (all copied from the file)
- The water level in a manhole is the pressure in the pipe: the storm's peak inflow of 35.7 cfs (1,011 L/s) is 2.3 times what the pipe carries full, 15.3 cfs (434 L/s), so the manhole supplies the extra head.
- Head once the pipe is full: H = D + (Sf - S0) L + K v^2/2g, with Sf = S0 (Q/Qfull)^2; the cover lifts when H reaches its underside plus its weight as a water depth, 0.64 ft (0.195 m) for a 121 lb (55 kg) cover.
- The cover is up 12 minutes and 1,236 ft3 (35 m3) floods the street (flow above 33.0 cfs, or 935 L/s).
- The page grades each number: solid, estimate or illustration (the storm, 3.7 in/hr or 95 mm/h at peak, and the 14.8 ac or 6 ha catchment are illustrations).

**Limits it states.** Each instant is treated as steady flow, so it leaves out the storage in the shaft and the surge a dynamic-wave model would capture; the US figures are the summary's conversions of the page's SI. It may be a later version of an older site (inside-the-node or inside-the-vault).

**Checked at ingest.** 35.7 / 15.3 = 2.33, the 2.3 times stated (our arithmetic). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Storm Sewer Manhole (app)](../entities/storm-sewer-manhole.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
