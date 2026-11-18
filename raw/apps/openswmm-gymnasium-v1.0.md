---
name: OpenSWMM Gymnasium
file: openswmm-gymnasium.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/91dTaVTQp1RxerhFjHEvrG", original: "Lovable app openswmm-gymnasium (MIT)", repo: "https://github.com/HydroCouple/openswmm.gymnasium (the package the page explains)"}
engines:
  - {name: EPA SWMM, version: 5.2.4, build: "USEPA tag v5.2.4 (commit 7952ca8), zig 0.13.0 cc -target wasm32-wasi -O2 as a reactor, with mkstemp/realpath stand-ins and a UTC ctime; 662,342 bytes, SHA-256 f35be71b...cced6", license: public domain}
units: US customary by default, SI behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session on 25 October 2026 under Robert Dickinson's direction. Its Ask panel runs the environments by name. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/91dTaVTQp1RxerhFjHEvrG, version 1792951503-362c (index.html, 1,662,385 bytes, SHA-256 a24691cc67aa26257c1caf42a418b5d58d0d76aeed7395f3f369b4a4b4080d76), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# OpenSWMM Gymnasium: a reinforcement-learning framework for the SWMM engine, explained and run

## In three points
- **What:** An explainer of HydroCouple's openswmm.gymnasium, a reinforcement-learning framework for the SWMM engine: how the loop, spaces and rewards work, what the package really ships, and its b01 TwinTank benchmark run on EPA SWMM 5.2.4 compiled to WebAssembly in the page. A single-file edition of Bob's Lovable app, which added a real learner (the cross-entropy method) on its pond model.
- **So what:** The shipped TwinTank benchmark delivers 0.667 in of rain instead of 4.0: the first tank peaks at 1.99 ft of its 12, flooding is zero for every policy, and the do-nothing policy (orifice shut) scores a perfect normalized hypervolume of 1.000. The learner settles on doing nothing within six generations. The page repairs the storm and reruns. PyPI holds only a reserved 0.0.0 package with a 57-byte __init__.py.
- **Now what:** Use it to see what an RL benchmark for SWMM needs before training on it. The benchmark ran on EPA SWMM 5.2.4, not on openswmm.engine version 6, which the package targets and which the page does not claim to have run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Overview, The Loop, Spaces, Reward, Live Training, TwinTank, API Sketch, Repo, Alternatives, Roadmap, Audit, Learn More, About, Doc. The pond learner draws forty random knob settings, runs each through sixteen training storms, keeps the best eight and refits, and is tested on 40 unseen storms beside the original's scripted curve. TwinTank uses the package's scenario.inp byte for byte, its three reward terms re-implemented line for line from rewards/terms.py, its hypervolume score, a storm repair, baselines, a constant-setting sweep and an engine-trained policy. The Audit lists 16 findings; the Repo tab covers both branches. The Lovable chatbot (a server route to google/gemini-3-flash-preview through Lovable's gateway) could talk about the demo but not run it; the Ask panel here runs both environments by name, with a Learn mode that asks for a prediction first.

## Checks (as stated on the page)

- Pond parity: pond, storm, controllers and reward ported verbatim and compared with a separate port of the original on 24 storm and seed combinations (144 comparisons), all equal within 1e-9.
- The original's claims at a 247.2 cfs storm peak re-run, and again with the episode stretched to 120 and 240 minutes; the 60-minute horizon was not hiding a later spill.
- The learner is seeded, so the Doc's numbers reproduce with the default seed.
- The engine reports version 52004 in every run; flow routing continuity stayed within 0.2% in the reports read; the same policy run twice gives the same result.

## What this does not show

As the page lists it: openswmm.engine version 6 was not run (version 6 descends from the same code and is expected to read a rain gage the same way, unverified); the pond is the Lovable app's model; the learner's levels and the scripted curve's are not comparable.

## Credits and licenses

HydroCouple's openswmm.gymnasium; EPA SWMM 5.2.4 (public domain); the Lovable openswmm-gymnasium, MIT © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who made the original Lovable app, asked for it as an HTML app, and is responsible for the result. Claude read the Lovable source and the upstream repository, ported the pond model, wrote the learner, compiled the engine, re-implemented the benchmark's rewards and score, and wrote the page, the Audit and the Doc essay. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first single-file edition (the version read).
