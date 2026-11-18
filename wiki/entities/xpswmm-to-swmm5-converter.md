---
title: "XPSWMM to SWMM5 Converter (app)"
type: entity
updated: 2026-11-18
sources: [S321]
tags: [apps, xpswmm, conversion, swmm5, datum]
reviewed: no
---
Bob's app XPSWMM to SWMM5 Converter: reads XPSWMM .xp cards and writes an EPA SWMM 5.2 .inp, in the browser. Version 1.0.0, 2026-10-25 [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md). Its `links:` line names no live Netlify address [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md).

**A caution about its source.** The page ships no technical summary. [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md)
- A single-file edition of the Lovable project xpswmm-swmm5-converter (live as xp-to-swmm-bridge.lovable.app). It reads XPSWMM .xp card files and writes EPA SWMM 5.2 .inp files, on four pages: Convert, Card Reader, Batch and Make .xp. Parsing happens on your machine; only Batch from GitHub asks GitHub's public API for a folder listing.
- It fixes 30 defects of the Lovable build, listed in the Doc tab with the original code. The two that matter most: the Convert page now converts, and every XP elevation becomes a SWMM5 invert or a height above one (Elev = Z, MaxDepth = GRELEV − Z, offsets = ZP − Z). Of 153 test models run in EPA SWMM 5.2.4, 0 ran from the Lovable converter's output and 153 from this one's.
- 17,800 round-trip comparisons (Make .xp, then cards, then parser) on 3 templates and 150 random networks: 0 failures.
- The same 153 models run in EPA SWMM 5.2.4: 0 of 153 ran with the Lovable converter, 153 of 153 with this one.
- 151,704 node depths and link flows compared against an independent .inp writer: all bit-identical. A 0.1 ft control change was detected.
- The datum equations were checked against Innovyze's published XPSWMM-to-SWMM mapping.

**How to use it, as the summary puts it.** Use it on a real .xp file and check the result, because none has been converted yet: the tests used .xp files written by the app's own Make .xp page. The invert column and several card layouts are inferred, and rainfall and run dates are not converted. [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md)

**What it does not show.** As the page lists it: no real XPSWMM file has been converted yet. The invert column (D1, columns 21 to 30) is inferred, and the Runoff, quality, LID, RDII, DWF, transect and XPX layouts are unverified. Rainfall and run dates are not converted. No person has yet run a real XPSWMM file through it. [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md)

**Noted at ingest.** It is not the Netlify site xp-to-swmm5, which is an older "XPSWMM .xp Card Reader" of 144,632 bytes.

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Visual SWMM (app)](visual-swmm.md), [XPX to Shapefile Converter (app)](xpx-to-shapefile-converter.md).
