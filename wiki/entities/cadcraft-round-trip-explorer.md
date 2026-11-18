---
title: "CADCraft Round-Trip Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S293]
tags: [apps, cad, dxf, interoperability, testing]
reviewed: no
---
Bob's app CADCraft Round-Trip Explorer: a test of CADCraft (github.com/storytold/cadcraft), an open-source AutoCAD clone: 112 third-party DXF files opened and re-saved, then judged entity by entity by ezdxf 1.4.4. Version 1.1, 2026-10-19 [S293](../sources/S293-cadcraft-round-trip-explorer-summary.md). Netlify address, from its `links:` line: https://cadcraft-round-trip-explorer.netlify.app [S293](../sources/S293-cadcraft-round-trip-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S293](../sources/S293-cadcraft-round-trip-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S293](../sources/S293-cadcraft-round-trip-explorer-summary.md)
- CADCraft re-saved 108 of 112 files without a crash (17 deliberately broken); ezdxf read all 108 in strict mode with 0 audit errors; same input twice gives byte-identical output.
- Of 21,091 scored entities in 66 complete drawings: 99.19% identical, 0.44% rewritten with the same extents, 77 (0.37%) not reproduced.
- CC-1: a 2D entity in a tilted coordinate system is saved at the wrong place or plane with no warning; 70 of the 77 losses, in 8 files; in a georeferenced drawing polylines tilted about 2 degrees moved 2.4 to 4.9 million units.
- Null control: ezdxf's own read-and-save, judged the same way, gave 0 differences in 65 of 67 complete drawings.

**What it does not show.** No AutoCAD in the loop; no DWG; test files, not production drawings (largest 2.7 MB); open and save only; entity data, not pixels; one commit (e707ab4) on one machine. [S293](../sources/S293-cadcraft-round-trip-explorer-summary.md)

**Noted at ingest.** 99.19 + 0.44 + 0.37 = 100.00% (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Negative results](../concepts/negative-results.md).
