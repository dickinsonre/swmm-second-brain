---
title: "S254: Network Lift, summary written from the page (v1.2)"
type: source
raw: raw/apps/network-lift-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-17
tags: [apps, cad, dxf, network-import, icm, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Network Lift, version 1.2: an app that reads a drainage drawing saved as DXF, finds the manholes and pipes, matches the text labels to them, works out flow direction, fills missing inverts and slopes, checks the network and writes Excel, CSV, SWMM5 and DXF for InfoWorks ICM, SewerGEMS or SWMM. The idea came from the NETWORK2EXCEL AutoLISP post. Raw file: [raw/apps/network-lift-v1.2.md](../../raw/apps/network-lift-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792451188-b271, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in October 2026 under Bob's direction; Bob chose the problem and asked for the documentation. Claude wrote all of the code and two synthetic test drawings with planted defects.

**Claims worth keeping** (all copied from the file)
- US sample (sample-us-storm.dxf, AC1032, $INSUNITS 2 = ft, 47 entities): 7 of 19 data labels placed by evidence the drafter drew, 11 by the distance rule, 1 too far from everything to place.
- A manhole with no label, UNK-1, gets a calculated invert of 815.68 ft from the pipe that reaches it, and is flagged; the outgoing pipe has a slope label but no invert, and the app makes one stated assumption there.
- DWG must be saved as DXF first, and Civil 3D pipe networks exported to plain lines (EXPORTTOAUTOCAD); the drawing is read in the browser and not uploaded.

**Limits it states.** It does not read Civil 3D pipe-network objects and checks no design flows or capacity. The samples are synthetic.

**Checked at ingest.** 7 + 11 + 1 = 19 labels. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://network-lift.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Network Lift (app)](../entities/network-lift.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](../entities/infoworks-icm.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
