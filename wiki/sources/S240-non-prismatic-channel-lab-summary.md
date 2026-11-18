---
title: "S240: Non-Prismatic Channel Lab, summary written from the page (v1.0)"
type: source
raw: raw/apps/non-prismatic-channel-lab-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, swmm5, open-channels, losses, normal-flow-limit, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Non-Prismatic Channel Lab, version 1.0: a 2,000 ft channel whose width you shape, solved by EPA SWMM 5.2.4 in the browser on an .inp the page writes and by a standard-step energy solution of the same channel; the gap between the two water surfaces is the cost of cutting a non-prismatic channel into prismatic links. Raw file: [raw/apps/non-prismatic-channel-lab-v1.0.md](../../raw/apps/non-prismatic-channel-lab-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793628863-2301, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a Claude Code session in November 2026 at Bob's direction, after a discussion of modeling a rock ramp in SWMM and ICM. Claude read the 5.2.4 source, designed and ran the test channels, found the normal-flow-limiter oscillation and wrote the energy solver and the page.

**Claims worth keeping** (all copied from the file)
- Abrupt constriction with no losses: SWMM rises 0.279 ft against the energy method's 0.640 ft, 44 %. With converted [LOSSES]: 0.586 ft, 92 %. Tapers: 77 % with 50 ft links and 78 % with 10 ft links.
- A tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates between 359.53 and 570.70 cfs at 10 s reports, on the page's engine and on swmm-toolkit 0.17.0 / PySWMM 2.2.0 alike, identical to the hundredth.
- Five test channels on the two engine copies: largest head difference at any node 0.00001 ft.
- The energy method matches an independent Python standard-step solution of all five channels to 0.0000 ft; the prismatic control agrees with it within 0.004 ft along the reach.
- The page's converted K equals the hand-built decks' 0.45 and 0.60.

**Limits it states.** Five test channels, no field data. ICM is discussed in the Doc but not run.

**Checked at ingest.** 0.279 / 0.640 = 44 % and 0.586 / 0.640 = 92 %. The oscillation is a finding for [The SWMM findings register](../concepts/findings-register.md), at the page's word. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://non-prismatic-channel-lab.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Non-Prismatic Channel Lab (app)](../entities/non-prismatic-channel-lab.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md), [Shape curves, transects and storage curves](../concepts/shape-curves-transects-storage-curves.md), [The SWMM findings register](../concepts/findings-register.md), [SWMM Results Kit](../entities/swmm-results-kit.md).
