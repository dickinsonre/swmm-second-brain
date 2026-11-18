---
name: Tri-Pyramid
file: tri-pyrimid-swmm5-swmm6.html
version: "3.0"
date: 2026-10-20
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://tri-pyrimid-swmm5-swmm6.netlify.app", artifact: "https://claude.ai/artifact/MbTWrupxYSmMAH7NY1QKWY", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "WebAssembly build embedded and checked by SHA-256 (624c7d2b9c83ee48...) before its first run; demo results from a native gcc build of tag v5.2.4"}
units: US customary (ft, cfs, ft/s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude (Opus 5) built the page and in October 2026 wrote its Doc, at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/MbTWrupxYSmMAH7NY1QKWY, version 1792448305-0a48 (index.html, 2,141,577 bytes, SHA-256 b916238adb4108a6b0b158aca111fc759350e3a2409c670cbf12dfc2da225393), its tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Tri-Pyramid: SWMM node and link profiles through time, drawn as a demographic profile chart

## In three points
- **What:** A demographic-profile ("population pyramid") chart for a sewer: every node and link of a SWMM model binned by a ratio on three arms (fullness, flooding, and by default the conduit Froude number), mirrored nodes against links, animated through the run. It loads any .inp + .rpt + .out set (pairing by basename), runs EPA SWMM 5.2.4 in the browser, compares scenario A with B, and reaches a GitHub model corpus.
- **So what:** It is a screening view of a whole network at one glance, and its Doc names the catch in the file format: on the demo, the .out stores a snapshot every 120 s while the engine routes every 5 s, so for link CB1 the report-step samples caught only 31% of the routing-step peak; 2 of 28 links fall under the app's 80% threshold and 13 more under 99%.
- **Now what:** Use it to see where a network is full or fast, then select a bin to light its members on the map, and make any diagnosis elsewhere: binning by a ratio throws away topology, so the pyramid cannot tell one surcharged trunk from twenty scattered laterals.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v3.0 · documentation written 20 October 2026"). The file name above is the Netlify site's, including its spelling. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Profile, Demo, Table, Story, Report, Learn, Doc. Arm 1, Fullness: nodes d/dmax (outfalls excluded), conduits A/Afull from the .out capacity variable; non-conduit links report a setting, not fullness. Other arms offer node residence or link travel time, node flooding (rate now or volume so far), depth/full or flow/Qfull (needs the .rpt), and link velocity. Peaks can come from .out samples or .rpt maxima; scales per step or per run, per side or shared. Pinned groups, a story generator, WebM and GIF recording, and CSV export.

## Checks (as stated on the page)

- The embedded wasm engine, handed the demo input, writes a 319,329-byte .out byte-for-byte identical to the one stored in the page from a native gcc build.
- The .out parser: 29 of 29 node maximum depths agree with the .rpt within 0.006 ft (largest 0.0045 ft); link sample maxima never exceed the .rpt maxima.
- Cross-section geometry: the share of time each of 27 conduits spent supercritical, computed from the page's rebuilt geometry, differs from SWMM's Flow Classification Summary by 0.03 percentage points on average, 0.50 at worst.
- Continuity on the demo: runoff -0.005%, routing -0.295%. Reproduced on 20 October 2026 under Node's WASI implementation.
- Demo network: 29 nodes and 28 links, three branches to a trunk, storage, an orifice and an outfall; 8 h run, 2-minute reporting.

## What this does not show

As the page lists it: the chart has no topology by design; the report step hides peaks (above); the cross-section geometry has been compared with the engine's classification on one 27-conduit network, not read line by line against xsect.c; the parsers have not been run against the full 3,813-model corpus the page can reach; very large models, other browsers and memory limits have not been measured; a defect was found by reading the source, so others may remain.

## How to reproduce

Demo tab, or load the demo files and Run SWMM 5.2.4 in the browser; the page checks the engine hash first.

## Credits and licenses

The demographic profile chart idea; EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says: Robert Dickinson directed the work, chose the borrowing (a demographic profile chart as a reading of a drainage network), set the three arms and the Froude default, asked for the scenario comparison and pinned groups, and holds the standard that any claim about engine behaviour must be checked against a compiled engine. Claude (Opus 5, Anthropic) built the page (parsers, geometry and Froude reconstruction, chart, map, story generator, wasm integration, corpus index, scenario comparison, guided demo) and in October 2026 wrote the Doc and drew its figures. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 3.0 (2026-10-20): the version read.
