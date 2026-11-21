---
name: SWMM5 → SWMM6 EXTRAN Features Upgrader
file: swmm5-to-swmm6-extran-upgrader.html
version: 2.0.1
date: 2026-11-21
author: Robert Dickinson
links: {netlify: beside this file when deployed, artifact: published private Claude artifact, repo: none}
engines:
  - {name: OpenSWMM, version: 6.0.0-alpha.3 pre-tag, branch: swmm6_rel, commit: 161051639ba93af20e83016e5122dc91a698d20d, license: Apache-2.0, note: lineage orphaned by the 2026-08-11 history rewrite; still builds}
  - {name: OpenSWMM legacy, version: 5.3.0-beta.3, source: same tree as the pin, license: Apache-2.0}
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4 of USEPA/Stormwater-Management-Model, license: public domain, build_note: needs -D_FORTIFY_SOURCE=0 on modern glibc}
  - {name: OpenSWMM alpha.2 WASM, source: PyPI wheel generation 2026-07-07, sha256: d0a8eadd…, license: Apache-2.0}
units: US customary (CFS, ft) throughout; DPS defaults are the engine's own SI values (celerity 25 m/s)
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM5 → SWMM6 EXTRAN Features Upgrader: four SWMM6 switches, four engines, every claim a run

**In one sentence.** This app flips SWMM6's four EXTRAN-heritage switches in a SWMM5 input file, proves the result on four real engines, and guarantees the SWMM5 copy never carries a keyword that kills stock 5.2.4 — all four would, measured.

**In one paragraph.** The Upgrader takes a SWMM5 .inp and switches on the four features OpenSWMM 6 inherited from the EXTRAN line: the dynamic Preissmann slot, semi-implicit node continuity, Anderson acceleration, and virtual junctions. It scans every junction against the engine's four eligibility rules before it writes a [VIRTUAL_JUNCTIONS] line, and it will not put a SWMM6 keyword into a SWMM5 file at all — each one is a fatal ERROR 205 there. Fifteen real models ride inside; a 103-assertion harness and about 200 native engine runs back the numbers, including a 16-for-16 round trip through stock 5.2.4. The measured ceiling: all four features together lifted the demo chain's peak 34.1%. The measured floor: on one 208-node model, converting every engine-approved virtual junction wrecked continuity to −24.9%. The app's engine is pinned to one commit, and that commit's history has since been rewritten out from under it.

## What it does

Edits a SWMM5 .inp to switch on the four EXTRAN-heritage features of OpenSWMM 6 (SURCHARGE_METHOD DYNAMIC_SLOT with DPS_* tuning, NODE_CONTINUITY SEMI_IMPLICIT, ANDERSON_ACCEL, [VIRTUAL_JUNCTIONS] with momentum selection), shows every change as a diff, and downloads the result two ways: a SWMM6 file, or a SWMM5 file guaranteed free of SWMM6-only keywords. Carries a 15-model embedded fleet, a four-engine measured compatibility matrix with verbatim messages, a per-model results table, and a release ladder measured from the engine repository with git.

## How it computes

- Parser: the .inp is split into an ordered section map; applyFeatures writes only the lines a ticked feature needs and records a restore map (moved [JUNCTIONS] rows by position; the prior SURCHARGE_METHOD value, null meaning absent).
- Virtual-junction eligibility: the engine's four rules re-implemented — exactly 2 attached links, both conduits (ERROR 609); identical cross-section keyed on shape+Geom1-4+barrels, roughness excluded (611); zero offset at the node honoring LINK_OFFSETS DEPTH/ELEV, tolerance 1e-6 (613); no lateral inflow, including [INFLOWS], DWF, RDII, treatment, subcatchment outlets and LID drains (617). Rules pinned to ErrorCodes.cpp:166-170 at commit 1610516.
- SWMM5 safety: stripSwmm6 removes DYNAMIC_SLOT (restoring the recorded prior value, SLOT included), DPS_CELERITY/DPS_ALPHA/DPS_DECAY_TIME, NODE_CONTINUITY, ANDERSON_ACCEL, VIRTUAL_JUNCTION_MOMENTUM and the [VIRTUAL_JUNCTIONS] section (junction rows restored). The SWMM5 download runs it unconditionally at click time; a target-engine switch set to SWMM5 disables the features entirely. The result badge is computed from the output text, not UI state.
- Momentum: BASIC default. FULL is labeled retired — upstream withdrew it 2026-08-14 (cross-junction term dq4j sign-inverted, at constant Q Δ(v²A) = −v²ΔA, applied to both adjacent links; 224-325% of routed volume destroyed on SWASHES macdonald-periodic; engines now warn and run BASIC; InpWriter stops emitting the key). The pinned alpha.3 CLI still honors FULL.

## Inputs and outputs

Reads SWMM5 .inp text (paste or the embedded fleet: exam1, extran1-7, extran9, extran10, user1, user2_slot, user3, user4, user5_slot — gzip+base64, decoded with DecompressionStream). Writes .inp text (SWMM6 or SWMM5-safe), plus CSV exports of the matrix, numbers, fleet and release ladder, each carrying the engine commit.

## Checks

All mechanical, from this build's record:
- Shipped-code harness: 103/103 assertions over all 15 models + demo (zero keyword leaks on the SWMM5 path, junction counts restored, SLOT preserved, strip idempotent).
- Stock EPA 5.2.4 round trip: 16/16 all-features-then-stripped files run rc=0, zero errors, continuity matching baseline to a few hundredths; positive control throws the full ERROR 205 wall.
- Virtual junctions: 9/9 app-generated [VIRTUAL_JUNCTIONS] files accepted by alpha.3 @ 1610516 (rc=0, zero ERROR 6xx, Virtual Junction Summary present); app-eligible == engine-eligible on all 15 models (old 2-rule scan over-reported: user1 36→0, user4 71→49).
- Fleet: 60/60 base + single-feature runs rc=0 across all 15 models.
- Demo chain peaks (alpha.3): base 14.38, +DYNAMIC_SLOT 16.32, +SEMI_IMPLICIT 13.82, +ANDERSON 14.38 (bit-identical to base), +VJ 14.39, ALL 19.29 cfs (+34.1%).
- All-VJ continuity: extran2 −4.052→−4.120%, user4 0.054→−24.946% — engine-eligible ≠ advisable.
- Per-feature verbatim messages: 9 single-feature runs across 5.2.4 / legacy 5.3 / alpha.3; legacy asymmetry measured (unknown keyword warns, known keyword with unknown value is fatal).
- Release ladder (git, full history, 2026-11-18): v5.2.4 →335→ alpha.1 (74ef6e27) →208→ alpha.2 (0df29948; was 241ffc8e before the rewrite) →184→ alpha.3 tag (86c28a88, cut 2026-08-11) →1,108→ head f297e9b0; pin not an ancestor of any ref, 142 commits orphaned.
- Live-DOM smoke: 20 then 23 assertions green (jsdom lacks dialog.showModal — environment gap only).
- Complexity (SWMM App Complexity Meter, baseline HC-2026-11-10-h): index 47.8 (Size 33.9, Structure 56.1, Test evidence 0 — checks are external harnesses and engine runs, SWMM vocabulary 75.2); analyzer 1.7.0, baseline HC-2026-11-10-h.

## What this does not show

- Anderson's 25-50% iteration cut: the source's claim; the .rpt prints no iteration counts; unmeasured.
- Accuracy against physical truth: the app measures difference and compatibility, not correctness.
- The FULL-momentum residuals (max 791.64, mean 5.82 cfs·ft/s) describe a retired option on the pinned engine.
- Engine behavior after 2026-08-09 (including FLOW_ROUTING FV, shipped in the alpha.4 era): commit history only, no runs here.
- 2D, water quality, runoff: out of scope.
- The essay prose and figures were reviewed by no one but Claude before delivery.

## How to reproduce

Build the engines: openswmm + openswmm-legacy from HydroCouple/openswmm.engine @ 161051639ba93af20e83016e5122dc91a698d20d (CMake Release, GEOPACKAGE/2D/GPU off); EPA 5.2.4 from the v5.2.4 tag with -D_FORTIFY_SOURCE=0. Run the embedded fleet (decode MODELS_B64 in this file) base + per-feature; generate VJ variants from the app's own analyse()/applyFeatures (window.__X6 exposes both); strip and re-run in 5.2.4. The release ladder regenerates from `git rev-list --count` on a full-history fetch.

## Credits and licenses

OpenSWMM 6 (HydroCouple/openswmm.engine): Caleb Buahin and the OpenSWMM team, Apache-2.0 — see the repository's LICENSE and NOTICE. EPA SWMM 5.2.4: US EPA, public domain. EXTRAN heritage: Bob Dickinson co-authored EXTRAN in the SWMM3 era at the University of Florida. App, harnesses and this document: built with Claude for Robert Dickinson.

## AI use

Built with Claude, Anthropic's AI model, in Claude sessions on 2026-08-08, 2026-08-09 and 2026-11-18, directed by Robert Dickinson, who chose the project, supplied the 15 test models, reported the two SWMM5-export defects and set the rule the app enforces (SWMM6-only sections never reach a SWMM5 file). Claude wrote the page, parser, eligibility scan and harnesses; built three engines from source and ran about 200 verification runs; measured the release ladder with git; and wrote this file, the Doc tab essay and the .docx. Checks are mechanical (harness, engine round trips, live-DOM smoke, complexity meter); the prose and figures were reviewed by no one but Claude; Anderson's iteration claim remains unmeasured.

## Changes

- 2.0.1 (2026-11-21): On a 390 px phone the Compatibility Matrix, Verified Numbers and Provenance tables scroll inside their cards; before, they pushed the whole page sideways. Nothing that computes changed.
- 2.0.0 (2026-11-18): Doc tab essay + .docx + this .md; Releases tab re-measured (alpha.3 tag exists, alpha.4 era, pin orphaned by the 2026-08-11 history rewrite); VIRTUAL_JUNCTION_MOMENTUM FULL marked retired, BASIC made default.
- 1.3 (2026-08-09): Releases tab (live git ladder + 26 branches); per-feature verbatim engine messages; fleet comparison table.
- 1.2 (2026-08-08): target-engine enforcement; SWMM5 download strips at click time; SURCHARGE_METHOD round-trip fix; content-scanned result badge.
- 1.1 (2026-08-08): 15-model fleet embedded; VJ eligibility rebuilt to the engine's four rules (was 2); engine sweep.
- 1.0 (2026-08-08): first delivery — four features, four-engine matrix, verified numbers, 36/36 gates.

