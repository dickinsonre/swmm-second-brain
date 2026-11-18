---
title: "S236: Water on the Road, summary written from the page (v1.1)"
type: source
raw: raw/apps/water-on-the-road-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-15
ingested: 2026-11-17
tags: [apps, swmm5, inlets, streets, hec-22, findings]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Water on the Road, version 1.1: a rebuild in one page of the six-step road-drainage workflow of Nhat Tien Vo's VNTool Civil 3D plugin (his post of 10 October 2026): pipe network from a polyline, structures by spacing, fit to the road, catchments from the corridor surface, HEC-22 hydraulics, and water on the road. Its HEC-22 code is a line-for-line port of EPA SWMM 5.2.4's inlet.c; no engine runs in the page. Raw file: [raw/apps/water-on-the-road-v1.1.md](../../raw/apps/water-on-the-road-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792029478-9152, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- Sample: 6 inlets, 1.64 ac drained, peak runoff 7.34 cfs, 0.27 cfs bypass carried on, maximum spread 4.8 ft against a 10.0 ft limit.
- On a 1.20 % grade with a 2.0 % cross slope and a 2.0 in gutter depression the example flow spreads 4.58 ft; a 2 ft x 2 ft P_BAR-50 grate catches 94.0 % of it (0.969 cfs).
- The exported steady .inp, run through SWMM 5.2.4's [STREETS] and [INLETS] code, reproduces the page's HEC-22 chain on 11 inlets in 4 scenarios: approach flow within 0.17 %, capture within 0.02 percentage points, sag depth equal.
- D-1: the HEC-22 round trip is not the identity (Eq. 4-2 forward uses T^2.67, the inverse in inlet.c uses 0.375): T = 8 ft gives Q = 1.905 cfs gives T = 8.021 ft, 0.26 %.
- D-2: SWMM's "Maximum Spread" comes from the street transect at the conduit's maximum depth, not Eq. 4-2; the HEC-22 line is commented out in writeStreetStats.
- D-5: SWMM 5.2.4 built with gcc -O2 on Ubuntu aborts on input ("buffer overflow detected") unless built with -D_FORTIFY_SOURCE=0.

**Limits it states.** Not Nhat Tien Vo's code or Civil 3D. Pipe hydraulics stop at full-flow Manning, with no HGL, junction losses or timing in the pipes. The IDF curves are illustrative; not a design tool of record.

**Checked at ingest.** 1 / 2.67 = 0.3745, against the 0.375 in inlet.c, which is where D-1's 0.26 % comes from. D-5 is the same abort [Rule 110 in SWMM5 (app)](../entities/rule110-swmm5.md) reports [S229](S229-rule110-swmm5-summary.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://water-on-the-road.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Water on the Road (app)](../entities/water-on-the-road.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [SWMM Inlet Library (app)](../entities/swmm-inlet-library.md), [Low-Spot Census (app)](../entities/low-spot-census.md), [The SWMM findings register](../concepts/findings-register.md).
