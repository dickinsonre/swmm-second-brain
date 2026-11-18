---
title: "S247: Meshing Field Guide, summary written from the page (v1.0)"
type: source
raw: raw/apps/meshing-field-guide-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, icm, 2d, mesh, teaching]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Meshing Field Guide, version 1.0: a 2026 edition of Innovyze's January 2014 note Tips for a Good Meshing Experience for InfoWorks ICM, each tip summarized (not reproduced) with what has changed by November 2026, plus a browser teaching mesher on cdt2d. ICM's mesher is not run. Raw file: [raw/apps/meshing-field-guide-v1.0.md](../../raw/apps/meshing-field-guide-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793635336-f222, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in November 2026 under Bob's direction: Bob supplied the 2014 note and the ICM Exchange reference and asked for the 2026 update; Claude researched the changes and wrote the mesher, the swale study, the calculators and the script generators.

**Claims worth keeping** (all copied from the file)
- By November 2026 ICM is at release 2027.2, Esri retired ArcMap on March 1, 2026, and ICM meshes with a newer default algorithm.
- Area bookkeeping: for the repaired test block, a 104,000 ft2 zone, a 407.4 ft2 facade bulge and a 20.4 ft2 lens give 87,012.9 ft2 by hand, and the mesher's total is 87,012.9 ft2.
- The bow-tie footprint produces exactly one edge crossing, at (330, 195); repairing the vertex order removes it.
- For element widths of 8 ft and more the deepest swale any alignment keeps equals 5.09 ft2 divided by the width (0.637 ft at 8 ft, 0.509 ft at 10 ft); over 80 sampled alignments the code returns that bound at every width tested.
- Unit conversions of the USGS quality levels and ICM default areas were done in code from published metric values.

**Limits it states.** The playground does not reproduce ICM's Triangle settings, Clip or Classic meshing, terrain-sensitive meshing, subgrid sampling or any hydraulics; its timestep ratio is a width ratio, not a measured run time. No ICM mesh was generated for the test block. The 2026 updates come from public Autodesk, Esri and USGS pages.

**Checked at ingest.** 104,000 less 407.4 and 20.4 is 103,572.2 ft2; the page's 87,012.9 ft2 also subtracts building footprints, whose area the summary does not give, so the hand figure cannot be rebuilt from it. 5.09 / 10 = 0.509. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://meshing-field-guide.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Meshing Field Guide (app)](../entities/meshing-field-guide.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [InfoWorks ICM](../entities/infoworks-icm.md), [ICM 2D Table Atlas (app)](../entities/icm-2d-table-atlas.md).
