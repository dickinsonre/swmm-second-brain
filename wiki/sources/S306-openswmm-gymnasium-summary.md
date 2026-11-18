---
title: "S306: OpenSWMM Gymnasium, summary written from the page (v1.0)"
type: source
raw: raw/apps/openswmm-gymnasium-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm6, openswmm, reinforcement-learning, control]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app OpenSWMM Gymnasium, version 1.0: a reinforcement-learning framework for the SWMM engine, explained and run. Raw file: [raw/apps/openswmm-gymnasium-v1.0.md](../../raw/apps/openswmm-gymnasium-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/91dTaVTQp1RxerhFjHEvrG, version 1792951503-362c (index.html, 1,662,385 bytes, SHA-256 a24691cc67aa26257c1caf42a418b5d58d0d76aeed7395f3f369b4a4b4080d76), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who made the original Lovable app, asked for it as an HTML app, and is responsible for the result. Claude read the Lovable source and the upstream repository, ported the pond model, wrote the learner, compiled the engine, re-implemented the benchmark's rewards and score, and wrote the page, the Audit and the Doc essay."

**Claims worth keeping** (all copied from the file)
- An explainer of HydroCouple's openswmm.gymnasium, a reinforcement-learning framework for the SWMM engine: how the loop, spaces and rewards work, what the package really ships, and its b01 TwinTank benchmark run on EPA SWMM 5.2.4 compiled to WebAssembly in the page. A single-file edition of Bob's Lovable app, which added a real learner (the cross-entropy method) on its pond model.
- The shipped TwinTank benchmark delivers 0.667 in of rain instead of 4.0: the first tank peaks at 1.99 ft of its 12, flooding is zero for every policy, and the do-nothing policy (orifice shut) scores a perfect normalized hypervolume of 1.000. The learner settles on doing nothing within six generations. The page repairs the storm and reruns. PyPI holds only a reserved 0.0.0 package with a 57-byte __init__.py.
- Pond parity: pond, storm, controllers and reward ported verbatim and compared with a separate port of the original on 24 storm and seed combinations (144 comparisons), all equal within 1e-9.
- The original's claims at a 247.2 cfs storm peak re-run, and again with the episode stretched to 120 and 240 minutes; the 60-minute horizon was not hiding a later spill.
- The learner is seeded, so the Doc's numbers reproduce with the default seed.
- The engine reports version 52004 in every run; flow routing continuity stayed within 0.2% in the reports read; the same policy run twice gives the same result.

**Limits it states.** As the page lists it: openswmm.engine version 6 was not run (version 6 descends from the same code and is expected to read a rain gage the same way, unverified); the pond is the Lovable app's model; the learner's levels and the scripted curve's are not comparable.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [OpenSWMM Gymnasium (app)](../entities/openswmm-gymnasium.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
