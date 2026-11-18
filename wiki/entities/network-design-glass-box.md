---
title: "Network Design Glass Box (app)"
type: entity
updated: 2026-11-17
sources: [S205, S248]
tags: [apps, icm, pipe-sizing, design-rules]
reviewed: no
---
Bob's app Network Design Glass Box: a from-scratch version of the rule-based pipe sizer Autodesk describes for InfoWorks ICM Ultimate 2027 (Network Design): penalty weights pick among sizes that pass the design rules, relaxed rules are tried when none passes, and every pipe's deciding rule is shown. It is built from Autodesk's public description, not ICM's code, and the page works in SI units. Version 1.0, 2026-09-30 [S248](../sources/S248-network-design-glass-box-summary.md). Netlify address: https://network-design-glass-box.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S248](../sources/S248-network-design-glass-box-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S248](../sources/S248-network-design-glass-box-summary.md)
- Rules include minimum and maximum slope, velocity (at design-flow depth or full bore), cover to crown, maximum depth in pipe, soffit or invert matching, never smaller than upstream, and an outfall's lowest invert. Eight presets, from Balanced to Existing pipe locked.
- Default design, pipe P5: 35.4 in (900 mm) at 0.634 %, carrying 49.8 cfs (1,409 L/s) at 80 % depth and 8.46 ft/s (2.58 m/s); its slope is set by percentage full; 750 mm fails on connectivity and maximum velocity. US figures are conversions.
- In the default network every pipe meets the rules.
- The hydraulics were checked against EPA SWMM 5.2.4 on the eight presets (its Verify tab).

**What it does not show.** Nothing about how ICM's own Network Design behaves. The demo network and the rainfall curve are invented. [S248](../sources/S248-network-design-glass-box-summary.md)

**Noted at ingest.** 900 mm is 35.43 in; 1,409 L/s is 49.76 cfs; 2.58 m/s is 8.46 ft/s (our arithmetic). The summary gives no numbers for the SWMM 5.2.4 check.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](infoworks-icm.md), [Logic-Based Generative SWMM5 (app)](logic-based-generative-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
