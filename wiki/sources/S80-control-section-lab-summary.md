---
title: "S80: Control Section Lab, summary written from the page (v1.2)"
type: source
raw: raw/apps/control-section-lab-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-18
ingested: 2026-11-15
tags: [apps, hydraulics, swmm5, swmm6, icm, open-channel, findings, verification, wasm]
reviewed: no
---
**What it is.** A technical summary of the app Control Section Lab, version 1.2 (18 October 2026): one channel reach at steady flow, a reference profile, and EPA SWMM 5.2.4 and OpenSWMM 6 run on it in the page. Raw file: [raw/apps/control-section-lab-v1.2.md](../../raw/apps/control-section-lab-v1.2.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote the file on 14 November 2026, at Bob's request, from the page's source, its build record (findings version 52004) and its Doc essay. Nothing was rerun. Bob has not read it (Q52). The app was built with Claude in October 2026 under Bob's direction; its essay is written in the manner of Isaac Asimov.

**Claims worth keeping** (all copied from the page; depths shown to four places)
- The reach: eight rectangular open conduits, 2,650 ft, 30 ft wide except a 14 ft throat (C4), slope 0.001 except a chute at 0.02 (C6). Defaults: 600 cfs, Manning n 0.022, FREE outfall.
- Reference: a steady mixed-flow profile with jumps placed by specific force, 1,333 sections, no contraction or expansion loss.
- F1: with the tailwater in control on a prismatic reach, SWMM 5 and the reference agree to 0.0003 ft.
- F2: SWMM 5 does not see the choke at the throat. Upstream at J1 the reference gives 5.4682 ft and SWMM 5 gives 4.1179 ft; largest shortfall 1.8964 ft at J3.
- F3: at the chute crest J6, SWMM 5 carries 1.6232 ft, the normal depth, where the reference has critical depth, 2.3160 ft.
- F4: with NORMAL_FLOW_LIMITED NONE and the chute toe drowned, flow in C6 swings 1,574.8 cfs in a 600 cfs run.
- F5: splitting the conduits does not converge on the reference; split in 8, J1 swings from 4.6884 to 5.9995 ft.
- F6: a damped-momentum profile reproduces both misses (J6 1.6233 ft; J1 4.2814 ft).
- F7: an entry loss K of 2.675 at 600 cfs stands in for the choke at J1; the K is 2.247 at 300 cfs and 2.89 at 900 cfs.
- F8: OpenSWMM 6 dynamic wave equals SWMM 5.2.4 at the nodes on three cases (the null control, the defaults, the split-in-4 case); on a fourth, where neither engine is steady, they differ by up to 1.4249 ft.
- F9: OpenSWMM 6 finite volume gives 5.47 ft at J1 on the default mesh (reference 5.47) and 2.59 ft at J6 (reference 2.32).
- OpenSWMM 6.0.0-alpha.4, swmm6_rel commit 64d517f (16 October 2026), built to wasm with five changed build files. Both engines' wasm `.out` files are byte-identical to native builds on the test models.
- No ICM engine runs: an "ICM rule" line is drawn from ICM's documented defaults.

**Limits it states.** Steady flow only. No contraction or expansion losses in the reference. One channel and one pre-release OpenSWMM commit. No person has compared the ICM-rule line with an ICM run.

**Checked at ingest.** Every number was searched for in the page source when the file was written. The findings carry the page's own IDs F1 to F9, which collide in form with the register's F-0001 series (Q47).

**Feeds:** [Control Section Lab (app)](../entities/control-section-lab.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
