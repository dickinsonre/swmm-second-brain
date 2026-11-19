---
title: "S379: SWMM5 to SWMM6 EXTRAN Features Upgrader, app .md (v2.0.0)"
type: source
raw: raw/apps/swmm5-to-swmm6-extran-upgrader.md
kind: app-md
author: Robert Dickinson
published: 2026-11-18
ingested: 2026-11-19
tags: [apps, swmm6, swmm5, extran, virtual-junctions, verification]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 → SWMM6 EXTRAN Features Upgrader, version 2.0.0: it switches on SWMM6's four EXTRAN-heritage features in a SWMM5 input file and checks the result on four engines. Raw file: [raw/apps/swmm5-to-swmm6-extran-upgrader.md](../../raw/apps/swmm5-to-swmm6-extran-upgrader.md).

**How it was written.** The app ships this file. Its AI-use section: "Built with Claude, Anthropic's AI model, in Claude sessions on 2026-08-08, 2026-08-09 and 2026-11-18, directed by Robert Dickinson, who chose the project, supplied the 15 test models, reported the two SWMM5-export defects and set the rule the app enforces (SWMM6-only sections never reach a SWMM5 file)." Claude built three engines from source and ran about 200 verification runs. The file says the prose and figures were reviewed by no one but Claude. It opens with In one sentence and In one paragraph, not In three points.

**Claims worth keeping** (all copied from the file)
- The app switches on the four features OpenSWMM 6 inherited from the EXTRAN line: SURCHARGE_METHOD DYNAMIC_SLOT with DPS_* tuning, NODE_CONTINUITY SEMI_IMPLICIT, ANDERSON_ACCEL, and [VIRTUAL_JUNCTIONS] with momentum selection. It downloads either a SWMM6 file or a SWMM5 file free of SWMM6-only keywords, each of which is a fatal ERROR 205 in stock 5.2.4.
- Virtual-junction eligibility, the engine's four rules re-implemented: exactly 2 attached links, both conduits (ERROR 609); identical cross-section, roughness excluded (611); zero offset at the node (613); no lateral inflow, including [INFLOWS], DWF, RDII, treatment, subcatchment outlets and LID drains (617). Rules pinned to `ErrorCodes.cpp:166-170` at commit 1610516.
- 103 of 103 harness assertions over the 15 models and the demo. 16 of 16 all-features-then-stripped files run in stock EPA 5.2.4 with rc=0, zero errors and continuity matching the baseline to a few hundredths. 9 of 9 app-generated [VIRTUAL_JUNCTIONS] files were accepted by alpha.3 at 1610516. App-eligible equals engine-eligible on all 15 models; the old 2-rule scan over-reported (user1 36 to 0, user4 71 to 49). 60 of 60 base and single-feature runs gave rc=0.
- Demo chain peaks on alpha.3: base 14.38, +DYNAMIC_SLOT 16.32, +SEMI_IMPLICIT 13.82, +ANDERSON 14.38 (bit-identical to base), +VJ 14.39, all four 19.29 cfs (+34.1 %).
- All-VJ continuity: extran2 from -4.052 to -4.120 %, user4 from 0.054 to -24.946 %. Engine-eligible is not the same as advisable.
- VIRTUAL_JUNCTION_MOMENTUM FULL is retired: upstream withdrew it on 2026-08-14 (the cross-junction term dq4j was sign-inverted, and 224-325 % of routed volume was destroyed on SWASHES macdonald-periodic); engines now warn and run BASIC. The pinned alpha.3 CLI still honors FULL.
- Release ladder, measured with git on a full-history fetch on 2026-11-18: v5.2.4, then 335 commits to alpha.1 (74ef6e27), 208 to alpha.2 (0df29948; it was 241ffc8e before the rewrite), 184 to the alpha.3 tag (86c28a88, cut 2026-08-11) and 1,108 to head f297e9b0. The app's pin is not an ancestor of any ref; 142 commits were orphaned by the 2026-08-11 history rewrite.
- Legacy 5.3 asymmetry: an unknown keyword warns; a known keyword with an unknown value is fatal.
- Complexity index 47.8 (Size 33.9, Structure 56.1, Test evidence 0, SWMM vocabulary 75.2; analyzer 1.7.0, baseline HC-2026-11-10-h).

**Limits it states.** Anderson acceleration's 25-50 % iteration cut is the source's claim and unmeasured: the .rpt prints no iteration counts. The app measures difference and compatibility, not correctness. The FULL-momentum residuals describe a retired option on the pinned engine. Engine behavior after 2026-08-09, including FLOW_ROUTING FV, is known from commit history only, with no runs. 2D, water quality and runoff are out of scope.

**Checked at ingest.** 19.29 / 14.38 = 1.341, the +34.1 % the file gives (our arithmetic). The pin is OpenSWMM 6.0.0-alpha.3 pre-tag at commit 161051639ba93af20e83016e5122dc91a698d20d, which the file says is orphaned but still builds. The `links:` line names no Netlify address and no artifact address. The file name carries no version.

**Feeds:** [SWMM5 to SWMM6 EXTRAN Features Upgrader (app)](../entities/swmm5-to-swmm6-extran-upgrader.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [EXTRAN](../entities/extran.md).
