---
title: "Network Lift (app)"
type: entity
updated: 2026-11-17
sources: [S205, S254]
tags: [apps, cad, dxf, network-import, icm, swmm5]
reviewed: no
---
Bob's app Network Lift: an app that reads a drainage drawing saved as DXF, finds the manholes and pipes, matches the text labels to them, works out flow direction, fills missing inverts and slopes, checks the network and writes Excel, CSV, SWMM5 and DXF for InfoWorks ICM, SewerGEMS or SWMM. The idea came from the NETWORK2EXCEL AutoLISP post. Version 1.2, 2026-10-19 [S254](../sources/S254-network-lift-summary.md). Netlify address: https://network-lift.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S254](../sources/S254-network-lift-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S254](../sources/S254-network-lift-summary.md)
- US sample (sample-us-storm.dxf, AC1032, $INSUNITS 2 = ft, 47 entities): 7 of 19 data labels placed by evidence the drafter drew, 11 by the distance rule, 1 too far from everything to place.
- A manhole with no label, UNK-1, gets a calculated invert of 815.68 ft from the pipe that reaches it, and is flagged; the outgoing pipe has a slope label but no invert, and the app makes one stated assumption there.
- DWG must be saved as DXF first, and Civil 3D pipe networks exported to plain lines (EXPORTTOAUTOCAD); the drawing is read in the browser and not uploaded.

**What it does not show.** It does not read Civil 3D pipe-network objects and checks no design flows or capacity. The samples are synthetic. [S254](../sources/S254-network-lift-summary.md)

**Noted at ingest.** 7 + 11 + 1 = 19 labels.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](infoworks-icm.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
