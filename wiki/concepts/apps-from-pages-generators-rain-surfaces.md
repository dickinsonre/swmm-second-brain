---
title: "Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5"
type: concept
updated: 2026-11-17
sources: [S205, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242]
tags: [apps, swmm5, generators, rainfall, surfaces]
reviewed: no
---
Nineteen app summaries that Bob uploaded on 17 November 2026: model generators, rainfall and flow-data methods, and the surfaces water runs over. Fifteen were written by Claude (Anthropic) that day from the published pages, with nothing rerun (Q108); four ship with their apps: [S224](../sources/S224-conformal-swmm-app-md.md), [S230](../sources/S230-swmm5-network-shapes-app-md.md), [S231](../sources/S231-swmmcraft-ultimate-app-md.md) and [S238](../sources/S238-narrow-band-app-md.md). Bob deployed all nineteen to Netlify the same day [S205](../sources/S205-note-netlify-addresses.md).

| App | Version | Date | Source |
|---|---|---|---|
| [Conformal SWMM (app)](../entities/conformal-swmm.md) | 1.0.0 | 2026-11-14 | [S224](../sources/S224-conformal-swmm-app-md.md) |
| [Four Ways to K (app)](../entities/four-ways-to-k.md) | 1.0 | 2026-10-29 | [S225](../sources/S225-four-ways-to-k-summary.md) |
| [Hedron Walk (app)](../entities/hedron-walk.md) | 1.7.0 | 2026-10-31 | [S226](../sources/S226-hedron-walk-summary.md) |
| [Kleinian SWMM (app)](../entities/kleinian-swmm.md) | 1.6.1 | 2026-11-03 | [S227](../sources/S227-kleinian-swmm-summary.md) |
| [Logic-Based Generative SWMM5 (app)](../entities/logic-based-generative-swmm5.md) | 2.0.0 | 2026-10-30 | [S228](../sources/S228-logic-based-generative-swmm5-summary.md) |
| [Rule 110 in SWMM5 (app)](../entities/rule110-swmm5.md) | 1.0.0 | 2026-11-09 | [S229](../sources/S229-rule110-swmm5-summary.md) |
| [The Shapes of SWMM5 Networks (app)](../entities/swmm5-network-shapes.md) | 1.1.0 | 2026-11-16 | [S230](../sources/S230-swmm5-network-shapes-app-md.md) |
| [SWMMCRAFT Ultimate (app)](../entities/swmmcraft-ultimate.md) | 2.7 | 2026-11-14 | [S231](../sources/S231-swmmcraft-ultimate-app-md.md) |
| [SWMM Rooms (app)](../entities/swmm-rooms.md) | 1.4 | 2026-10-20 | [S232](../sources/S232-swmm-rooms-summary.md) |
| [SWMM Hydraulic Library (app)](../entities/swmm-hydraulic-library.md) | 2.0 | 2026-10-21 | [S233](../sources/S233-swmm-hydraulic-library-summary.md) |
| [SWMM Inlet Library (app)](../entities/swmm-inlet-library.md) | 1.0 | 2026-10-26 | [S234](../sources/S234-swmm-inlet-library-summary.md) |
| [SWMM PDF Wizard (app)](../entities/swmm-pdf-wizard.md) | 1.1.0 | 2026-10-19 | [S235](../sources/S235-swmm-pdf-wizard-summary.md) |
| [Water on the Road (app)](../entities/water-on-the-road.md) | 1.1 | 2026-10-15 | [S236](../sources/S236-water-on-the-road-summary.md) |
| [Quantile Mapping to SWMM5 / SWMM6 (app)](../entities/quantile-mapping-swmm.md) | 1.2 | 2026-10-20 | [S237](../sources/S237-quantile-mapping-swmm-summary.md) |
| [The Narrow Band (app)](../entities/narrow-band.md) | 1.0.0 | 2026-11-16 | [S238](../sources/S238-narrow-band-app-md.md) |
| [Hard Meters, Soft Models (app)](../entities/hard-meters-soft-models.md) | 1.0 | 2026-10-22 | [S239](../sources/S239-hard-meters-soft-models-summary.md) |
| [Non-Prismatic Channel Lab (app)](../entities/non-prismatic-channel-lab.md) | 1.0 | 2026-11-02 | [S240](../sources/S240-non-prismatic-channel-lab-summary.md) |
| [Quasi-2D Mesh Maker for SWMM5 (app)](../entities/quasi-2d-mesh-maker.md) | 1.0 | 2026-10-04 | [S241](../sources/S241-quasi-2d-mesh-maker-summary.md) |
| [Walk the Mesh (app)](../entities/walk-the-mesh.md) | 1.0 | 2026-10-19 | [S242](../sources/S242-walk-the-mesh-summary.md) |

**Generators.** Five write SWMM5 models from mathematics or rules: complex functions [S224](../sources/S224-conformal-swmm-app-md.md), a triangle-tiled path and Rule 30 [S226](../sources/S226-hedron-walk-summary.md), a Kleinian group [S227](../sources/S227-kleinian-swmm-summary.md), design rules over a pattern model [S228](../sources/S228-logic-based-generative-swmm5-summary.md) and an elementary cellular automaton computed with water [S229](../sources/S229-rule110-swmm5-summary.md). The first four check that their subcatchments do not overlap, and say their networks are not designs; the fifth has no subcatchments. All five run what they write.

**Two pages, one storage finding.** Both quasi-2D apps find that the obvious mesh stores twice the water a cell holds. Walk the Mesh measures waves arriving a factor of 1.414 late and fixes it by multiplying Manning's n by 0.841 [S242](../sources/S242-walk-the-mesh-summary.md); the Quasi-2D Mesh Maker uses half-width links that hold exactly the cell area [S241](../sources/S241-quasi-2d-mesh-maker-summary.md). Neither page cites the other, and neither was compared with a 2D shallow-water solver.

**Results that went against the method.** The narrower MEVD band held the true 200-year rain in 28.8 % of records against 75.8 % for GEV [S238](../sources/S238-narrow-band-app-md.md). BME with an overconfident model covered the truth at 61 % of points [S239](../sources/S239-hard-meters-soft-models-summary.md). Equivalent Manning n charged 1.94 times the loss at 2 cfs [S225](../sources/S225-four-ways-to-k-summary.md). Prismatic links showed 44 % of a constriction's rise [S240](../sources/S240-non-prismatic-channel-lab-summary.md).

**Findings in EPA's code, at the pages' word.** A tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates between 359.53 and 570.70 cfs on two engine copies [S240](../sources/S240-non-prismatic-channel-lab-summary.md). The HEC-22 spread round trip in inlet.c is not the identity, 0.26 % at 8 ft [S236](../sources/S236-water-on-the-road-summary.md). A native Linux build aborts on input with "buffer overflow detected" unless fortify checks are off [S229](../sources/S229-rule110-swmm5-summary.md) [S236](../sources/S236-water-on-the-road-summary.md).

**Engines.** Nine run EPA SWMM 5.2.4 in the page; Conformal SWMM runs the OpenSWMM legacy 5.3.0-beta.3 instead [S224](../sources/S224-conformal-swmm-app-md.md), and the SWMM Inlet Library runs OpenSWMM 6.0.0-alpha.4 beside 5.2.4 [S234](../sources/S234-swmm-inlet-library-summary.md). Three take their engine unchanged from [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md): [S225](../sources/S225-four-ways-to-k-summary.md), [S234](../sources/S234-swmm-inlet-library-summary.md), [S240](../sources/S240-non-prismatic-channel-lab-summary.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](apps-from-pages-history-and-swmm5.md), [The SWMM findings register](findings-register.md), [WebAssembly builds against native builds](wasm-against-native-builds.md).
