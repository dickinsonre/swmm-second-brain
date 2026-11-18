---
title: "Meshing Field Guide (app)"
type: entity
updated: 2026-11-17
sources: [S205, S247]
tags: [apps, icm, 2d, mesh, teaching]
reviewed: no
---
Bob's app Meshing Field Guide: a 2026 edition of Innovyze's January 2014 note Tips for a Good Meshing Experience for InfoWorks ICM, each tip summarized (not reproduced) with what has changed by November 2026, plus a browser teaching mesher on cdt2d. ICM's mesher is not run. Version 1.0, 2026-11-02 [S247](../sources/S247-meshing-field-guide-summary.md). Netlify address: https://meshing-field-guide.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S247](../sources/S247-meshing-field-guide-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S247](../sources/S247-meshing-field-guide-summary.md)
- By November 2026 ICM is at release 2027.2, Esri retired ArcMap on March 1, 2026, and ICM meshes with a newer default algorithm.
- Area bookkeeping: for the repaired test block, a 104,000 ft2 zone, a 407.4 ft2 facade bulge and a 20.4 ft2 lens give 87,012.9 ft2 by hand, and the mesher's total is 87,012.9 ft2.
- The bow-tie footprint produces exactly one edge crossing, at (330, 195); repairing the vertex order removes it.
- For element widths of 8 ft and more the deepest swale any alignment keeps equals 5.09 ft2 divided by the width (0.637 ft at 8 ft, 0.509 ft at 10 ft); over 80 sampled alignments the code returns that bound at every width tested.
- Unit conversions of the USGS quality levels and ICM default areas were done in code from published metric values.

**What it does not show.** The playground does not reproduce ICM's Triangle settings, Clip or Classic meshing, terrain-sensitive meshing, subgrid sampling or any hydraulics; its timestep ratio is a width ratio, not a measured run time. No ICM mesh was generated for the test block. The 2026 updates come from public Autodesk, Esri and USGS pages. [S247](../sources/S247-meshing-field-guide-summary.md)

**Noted at ingest.** 104,000 less 407.4 and 20.4 is 103,572.2 ft2; the page's 87,012.9 ft2 also subtracts building footprints, whose area the summary does not give, so the hand figure cannot be rebuilt from it. 5.09 / 10 = 0.509.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [InfoWorks ICM](infoworks-icm.md), [ICM 2D Table Atlas (app)](icm-2d-table-atlas.md).
