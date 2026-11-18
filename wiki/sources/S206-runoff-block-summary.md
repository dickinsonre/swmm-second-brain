---
title: "S206: The Runoff Block, summary written from the page (v1.1)"
type: source
raw: raw/apps/runoff-block-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-17
tags: [apps, swmm5, runoff, subcatchment, history, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app The Runoff Block, version 1.1: one subcatchment run by EPA SWMM 5.2.4 compiled to WebAssembly, with tabs for surface, infiltration, LID, groundwater and snow, the SWMM 1 and SWMM 4.4H engines run on the same block, and the 59 runoff chats Bob held with an AI from November 2023 on. Raw file: [raw/apps/runoff-block-v1.1.md](../../raw/apps/runoff-block-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793755149-2052, reading its About, Block and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was made with Claude in one session on 3 November 2026 under Bob's direction: Bob chose the project, wrote the list of 59 chats and supplied the outside review behind 1.1; Claude read the 5.2.4 source, wrote the app and its tests, ported the runoff step to JavaScript and ran the experiments; a second Claude agent wrote the one-line chat summaries. The SCS tables were first typed from memory and corrected against web sources in 1.1. No person has reviewed version 1.1.

**Claims worth keeping** (all copied from the file)
- Default block: 10 ac, 40 % impervious, W 800 ft, 2 % slope, Horton, a 2 in Chicago (Keifer-Chu) storm over 3 hours; the storm is illustrative, not from a local IDF curve.
- Default block results: peak 20.80 cfs at 1.25 hr; runoff 0.93 in (0.25 MG); runoff coefficient 0.466; runoff continuity -0.40 %. Ledger: rain 2.000 in, infiltration 1.058 in, surface runoff 0.932 in, storage at end 0.018 in, residual -0.008 in.
- Width: from W x 0.25 to W x 4 the peak goes from 14.6 to 25.0 cfs (five engine runs). Halving W and both n values gives the same .out.
- As coded in 5.2.4, impervious water on the default block flows 218 ft and pervious water 327 ft; the commented-out change in subcatch.c ("Possible change to how sub-area width should be assigned") would give both 545 ft.
- Three engines: SWMM 4.4 and 5.2.4 agree to 0.13 % on volume; SWMM 1 is 17.6 % high because its Horton curve decays on the storm clock; with Horton decay removed (f0 = fc) the gap closes to 0.8 %.
- Parity: 36 of 36 scenario inputs wrote a byte-identical .out in the WebAssembly build and a native gcc build of stock 5.2.4 with the perched patch reversed. The repo count of 598 of 598 is carried, not rerun.
- The JavaScript port of the runoff step against the engine: 2.4e-7 cfs at a 5-minute wet step, 1.1e-7 cfs at 2 minutes.
- Version 1.0 was graded 75 of 100 by an outside reviewer, who found a 0.92 cfs port-versus-engine gap labelled as rounding; in 1.1 the port follows the engine's variable step.

**Limits it states.** No observed flows, no network, no water quality. One subcatchment under synthetic storms shows what each method does, not which is right for a given catchment.

**Checked at ingest.** The ledger closes: 1.058 + 0.932 + 0.018 - 0.008 = 2.000 in, and -0.008 / 2.000 is the -0.40 % continuity printed. 0.932 / 2.000 = 0.466. 0.93 in over 10 ac is 33,759 ft3, 0.25 MG (our arithmetic). 218 + 327 = 545 ft. The width finding is the one on [Subcatchment width](../concepts/subcatchment-width.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://runoff-block.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [The Runoff Block (app)](../entities/runoff-block.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Subcatchment width](../concepts/subcatchment-width.md), [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Infiltration methods](../concepts/infiltration-methods.md), [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md), [SWMM 4 Twin Engines (app)](../entities/swmm4-twin-engines.md), [swmm524-perched](../entities/swmm524-perched.md).
