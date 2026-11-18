---
name: XPSWMM to SWMM5 Converter
file: xpswmm-to-swmm5-converter.html
version: 1.0.0
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/T3tQX8u427YMaAx85vW12E", original: "https://xp-to-swmm-bridge.lovable.app", repo: "https://github.com/SWMMEnablement/xp-to-swmm-bridge"}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "used in the tests through swmm-toolkit 0.17; not in the page", license: public domain}
units: the model's own units, from the .xp job-control cards (US customary or metric)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude built and tested this edition on 25 October 2026 under Robert Dickinson's direction, and that the original Lovable build was also AI-generated. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/T3tQX8u427YMaAx85vW12E, version 1792951681-bf6b (index.html, 799,322 bytes, SHA-256 d88289c30260eb624c1686cbb4a546d0f046a12baa2de665996c0250362a7bc1), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# XPSWMM to SWMM5 Converter: reads XPSWMM .xp cards and writes an EPA SWMM 5.2 .inp, in the browser

## In three points
- **What:** A single-file edition of the Lovable project xpswmm-swmm5-converter (live as xp-to-swmm-bridge.lovable.app). It reads XPSWMM .xp card files and writes EPA SWMM 5.2 .inp files, on four pages: Convert, Card Reader, Batch and Make .xp. Parsing happens on your machine; only Batch from GitHub asks GitHub's public API for a folder listing.
- **So what:** It fixes 30 defects of the Lovable build, listed in the Doc tab with the original code. The two that matter most: the Convert page now converts, and every XP elevation becomes a SWMM5 invert or a height above one (Elev = Z, MaxDepth = GRELEV − Z, offsets = ZP − Z). Of 153 test models run in EPA SWMM 5.2.4, 0 ran from the Lovable converter's output and 153 from this one's.
- **Now what:** Use it on a real .xp file and check the result, because none has been converted yet: the tests used .xp files written by the app's own Make .xp page. The invert column and several card layouts are inferred, and rainfall and run dates are not converted.

This summary was written after the fact. The edition ships no technical summary of its own. Its version and date are the page's own ("single-file edition v1.0.0 (25 Oct 2026)"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Convert takes one .xp file (or one of three samples: Simple Pipe Network, Pump Station, Detention Pond) and writes a .inp. Units, routing method, time step and tolerances come from the .xp job-control cards. Two run settings do not and are set on the page: a placeholder storm of 1 hour (in/hr, or mm/hr for a metric model; 0 writes a dry gage) and the simulation length, written as START and END dates in [OPTIONS]. Card Reader shows the cards as tables, a map and raw text. Batch converts a set. Make .xp writes .xp files for testing. The Doc tab holds the essay "An Elevation Is Not a Depth", which opens on a pipe the Lovable build hung 105 ft in the air (rim 111 ft, node Elev 111, pipe invert 216; this edition: node Elev 105, pipe invert 105, offsets 0).

## Checks (as stated on the page)

- 17,800 round-trip comparisons (Make .xp, then cards, then parser) on 3 templates and 150 random networks: 0 failures.
- The same 153 models run in EPA SWMM 5.2.4: 0 of 153 ran with the Lovable converter, 153 of 153 with this one.
- 151,704 node depths and link flows compared against an independent .inp writer: all bit-identical. A 0.1 ft control change was detected.
- The datum equations were checked against Innovyze's published XPSWMM-to-SWMM mapping.

## What this does not show

As the page lists it: no real XPSWMM file has been converted yet. The invert column (D1, columns 21 to 30) is inferred, and the Runoff, quality, LID, RDII, DWF, transect and XPX layouts are unverified. Rainfall and run dates are not converted. No person has yet run a real XPSWMM file through it.

## Credits and licenses

MIT License, © 2026 Robert Dickinson. The .xp and .xpx formats were designed by Robert Dickinson at XP Software (1992 to 1999). Innovyze, XPSWMM/XPStorm Conversion Notes (SWMM), for the field mapping; the XP field table in the parser, which the original build says was derived from XP's Swmfield.c, Exporun.c and Edovl.c; EPA SWMM 5.2 (public domain). Built with React 18, Tailwind CSS, Radix UI (shadcn/ui), lucide icons, JSZip and Vite, bundled into one HTML file.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project, asked for the single-file app and is responsible for the work. The original Lovable build was also AI-generated. Claude read the Lovable source and found the defects, rewrote the SWMM5 builder and the Convert page, patched the parser, generator, Card Reader and Make .xp, added the theme, tour, demo recorder, About and Doc pages, and wrote the test harness and the Doc essay with its .docx. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-25): single-file edition with 30 defects fixed (the version read).
