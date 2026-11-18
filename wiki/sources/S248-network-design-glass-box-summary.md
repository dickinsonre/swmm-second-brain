---
title: "S248: Network Design Glass Box, summary written from the page (v1.0)"
type: source
raw: raw/apps/network-design-glass-box-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-09-30
ingested: 2026-11-17
tags: [apps, icm, pipe-sizing, design-rules]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Network Design Glass Box, version 1.0: a from-scratch version of the rule-based pipe sizer Autodesk describes for InfoWorks ICM Ultimate 2027 (Network Design): penalty weights pick among sizes that pass the design rules, relaxed rules are tried when none passes, and every pipe's deciding rule is shown. It is built from Autodesk's public description, not ICM's code, and the page works in SI units. Raw file: [raw/apps/network-design-glass-box-v1.0.md](../../raw/apps/network-design-glass-box-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1790741819-2050, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- Rules include minimum and maximum slope, velocity (at design-flow depth or full bore), cover to crown, maximum depth in pipe, soffit or invert matching, never smaller than upstream, and an outfall's lowest invert. Eight presets, from Balanced to Existing pipe locked.
- Default design, pipe P5: 35.4 in (900 mm) at 0.634 %, carrying 49.8 cfs (1,409 L/s) at 80 % depth and 8.46 ft/s (2.58 m/s); its slope is set by percentage full; 750 mm fails on connectivity and maximum velocity. US figures are conversions.
- In the default network every pipe meets the rules.
- The hydraulics were checked against EPA SWMM 5.2.4 on the eight presets (its Verify tab).

**Limits it states.** Nothing about how ICM's own Network Design behaves. The demo network and the rainfall curve are invented.

**Checked at ingest.** 900 mm is 35.43 in; 1,409 L/s is 49.76 cfs; 2.58 m/s is 8.46 ft/s (our arithmetic). The summary gives no numbers for the SWMM 5.2.4 check. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://network-design-glass-box.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Network Design Glass Box (app)](../entities/network-design-glass-box.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Logic-Based Generative SWMM5 (app)](../entities/logic-based-generative-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
