---
title: "S321: XPSWMM to SWMM5 Converter, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/xpswmm-to-swmm5-converter-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, xpswmm, conversion, swmm5, datum]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app XPSWMM to SWMM5 Converter, version 1.0.0: reads XPSWMM .xp cards and writes an EPA SWMM 5.2 .inp, in the browser. Raw file: [raw/apps/xpswmm-to-swmm5-converter-v1.0.0.md](../../raw/apps/xpswmm-to-swmm5-converter-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/T3tQX8u427YMaAx85vW12E, version 1792951681-bf6b (index.html, 799,322 bytes, SHA-256 d88289c30260eb624c1686cbb4a546d0f046a12baa2de665996c0250362a7bc1), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project, asked for the single-file app and is responsible for the work. The original Lovable build was also AI-generated."

**Claims worth keeping** (all copied from the file)
- A single-file edition of the Lovable project xpswmm-swmm5-converter (live as xp-to-swmm-bridge.lovable.app). It reads XPSWMM .xp card files and writes EPA SWMM 5.2 .inp files, on four pages: Convert, Card Reader, Batch and Make .xp. Parsing happens on your machine; only Batch from GitHub asks GitHub's public API for a folder listing.
- It fixes 30 defects of the Lovable build, listed in the Doc tab with the original code. The two that matter most: the Convert page now converts, and every XP elevation becomes a SWMM5 invert or a height above one (Elev = Z, MaxDepth = GRELEV − Z, offsets = ZP − Z). Of 153 test models run in EPA SWMM 5.2.4, 0 ran from the Lovable converter's output and 153 from this one's.
- 17,800 round-trip comparisons (Make .xp, then cards, then parser) on 3 templates and 150 random networks: 0 failures.
- The same 153 models run in EPA SWMM 5.2.4: 0 of 153 ran with the Lovable converter, 153 of 153 with this one.
- 151,704 node depths and link flows compared against an independent .inp writer: all bit-identical. A 0.1 ft control change was detected.
- The datum equations were checked against Innovyze's published XPSWMM-to-SWMM mapping.

**Limits it states.** As the page lists it: no real XPSWMM file has been converted yet. The invert column (D1, columns 21 to 30) is inferred, and the Runoff, quality, LID, RDII, DWF, transect and XPX layouts are unverified. Rainfall and run dates are not converted. No person has yet run a real XPSWMM file through it.

**Checked at ingest.** It is not the Netlify site xp-to-swmm5, which is an older "XPSWMM .xp Card Reader" of 144,632 bytes. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [XPSWMM to SWMM5 Converter (app)](../entities/xpswmm-to-swmm5-converter.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Visual SWMM (app)](../entities/visual-swmm.md), [XPX to Shapefile Converter (app)](../entities/xpx-to-shapefile-converter.md).
