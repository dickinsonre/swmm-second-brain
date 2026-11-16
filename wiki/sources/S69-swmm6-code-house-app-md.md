---
title: "S69: SWMM6 Code House, technical summary (app .md, v1.2.1)"
type: source
raw: raw/apps/swmm6-code-house-v1.2.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-14
tags: [apps, swmm6, source-code, openswmm, verification]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary carried inside the SWMM6 Code House page, version 1.2.1: a walkable 3D map of the OpenSWMM 6 engine source. Raw file: [raw/apps/swmm6-code-house-v1.2.1.md](../../raw/apps/swmm6-code-house-v1.2.1.md).

**How it got here.** Extracted byte for byte on 14 November 2026 from the `script#app-md` block of Bob's published artifact. The public Netlify page's source shows a v1.0.0 badge (Q45).

**How it was written.** By Claude (Anthropic) in Claude Code sessions in November 2026; versions to 1.1.0 with claude-opus-5-5 and three subagents drafting room diagrams, versions 1.2.0 and 1.2.1 with claude-fable-5-2. "Human review: none yet."

**Claims worth keeping**
- The house: 102 rooms on 9 floors, 351,187 lines, 675 files, 6,683 functions, 427 doorways.
- Source read: OpenSWMM 6.0.0-alpha.4, branch `swmm6_rel`, commit 9648837, from the fork SWMMBobSWMM6/openswmm.engine. Apache-2.0. Text unchanged, headers intact. The upstream NOTICE is reproduced in full.
- "It is not an OpenSWMM release, it holds no compiled engine, and it does not run a model."
- Census by text, no compiler: 26,223 calls resolved by name, 19,900 left ambiguous, counted and not drawn.
- 24 rooms have hand-made diagrams, each labelled Port (a JavaScript copy of the C++) or Picture.
- The ? on code resolves 85.5 % of field uses in `.cpp` files.
- Results reader: parses the SWMM `.out` layout (magic 516114522). Version field 60000 reads as OpenSWMM and 5xxxx as EPA SWMM 5.
- Node type codes differ by engine: OpenSWMM stores DIVIDER = 2 and STORAGE = 3 (`plugins/DefaultOutputPlugin.cpp:451`); SWMM 5 has them the other way round.
- Doors to the SWMM5 house: 454 of 962 SWMM 5 functions named at 1,266 places in 119 files.
- Checks: 11 test scripts with 376 checks in all (18, 94, 51, 19, 10, 4, 4, 24, 15, 88, 49). Wall text equals the source for all 675 files.
- Real result files tested: `site_drainage_model.out` (written by 6.0.0-alpha.3), `baseline.out` (alpha.1), `legacy_site_drainage.out` (EPA SWMM 5.3.0), with a separate Python reader giving the expected values.
- Credits: OpenSWMM Engine, Copyright 2026 HydroCouple Developers; lead developer Caleb Buahin; developer and documentation Corinne Wiesner-Friedman.
- Changes: 1.0.0 (2026-11-03), 1.0.1 and 1.1.0 (2026-11-04), 1.2.0 (2026-11-11), 1.2.1 (2026-11-12).

**Limits it states.** OpenSWMM was not compiled or run; nothing shows the diagrams match the engine or that OpenSWMM matches SWMM 5. The 24 diagrams were written by AI and not checked by a person. The real result files came from alpha.1 and alpha.3, not the alpha.4 on the walls. The 20 reading notes are source-reading hypotheses, except the node type code, which was seen in a real file. No speed claim is made.

**Checked at ingest.** The eleven check counts sum to 376 (our sum).

**Feeds:** [SWMM6 Code House (app)](../entities/swmm6-code-house.md), [SWMM5 Code House (app)](../entities/swmm5-code-house.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
