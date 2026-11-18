---
title: "HydroCouple Interactive (app)"
type: entity
updated: 2026-11-17
sources: [S205, S209, S258]
tags: [apps, hydrocouple, swmm6, teaching, coupling]
reviewed: no
---
Bob's app HydroCouple Interactive: an unofficial restatement of the six pages of hydrocouple.org, read on 13 November 2026, with its eight static figures turned into 18 working diagrams and labs. HydroCouple is Caleb Buahin's open architecture for coupling water models, with Open-Source SWMM 6.0 at its center. No engine runs. Version 1.0.0, 2026-11-13 [S258](../sources/S258-hydrocouple-interactive-app-md.md). Netlify address: https://hydrocouple-interactive.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**Its source.** [S258](../sources/S258-hydrocouple-interactive-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S258](../sources/S258-hydrocouple-interactive-app-md.md)
- 40 of 40 math checks pass (node test/math.test.js).
- An adapter holding a 120 cfs triangle hydrograph at a 5 min step keeps the volume exactly (432,646.7 ft3, 9.93 ac-ft) and still shifts its center of mass from 55.07 to 62.57 min, by exactly 7.5 min. Linear interpolation at 30 min sees a peak of 96.05 cfs and loses 6.63 percent of the volume.
- A replay example: the reverse pass from the final state only gives dL/dx0 = 0.0883, 12 percent high against the full backward sweep's 0.07882.
- A 1 percent Preissmann slot on a 3 ft pipe gives a celerity of 87.07 ft/s (textbook formula; the dynamic slot method of the article is not implemented).
- The site as read: interface 2.0.0-alpha.2, C++20, Python bindings, MIT; 20 projects (15 available, 5 planned); a benchmark platform of 1,396 models; 8 notes by Caleb Buahin (6) and Corinne Wiesner-Friedman (2); 9 papers by 13 authors.
- Five apparent inconsistencies on the site need a person to confirm, among them Apache-2.0 on the home page against an MIT license link in the May 2026 alpha announcement for the engine.

**What it does not show.** A snapshot of 13 November 2026. Article bodies are reduced to a few sentences, with no equations or results. No engine runs; all labs are synthetic. The glue arithmetic and the click-through notes are the app's, not the site's. API reference, engine manuals, benchmark dashboard and source were not read. [S258](../sources/S258-hydrocouple-interactive-app-md.md)

**Noted at ingest.** The slot celerity scales with the square root of the diameter: 87.07 x (3.28 / 3)^0.5 = 91.0 ft/s, near the 91.2 ft/s (27.8 m/s) the [The Rigid Column Test (app)](rigid-column-test.md) gives for a 1 % slot in a 3.28 ft (1 m) pipe [S209](../sources/S209-rigid-column-test-summary.md) (our arithmetic). The license observation bears on Q83, which Bob settled only as far as MIT goes. The site names the interface MIT and, per the app, the engine Apache-2.0 on its home page. Bob renamed the Netlify site from `hydroouple-interactive` on 17 November 2026 [S205](../sources/S205-note-netlify-addresses.md).

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [SWMM Engine Map (app)](swmm-engine-map.md), [Inside hydrocouple.platform (app)](inside-hydrocouple-platform.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
