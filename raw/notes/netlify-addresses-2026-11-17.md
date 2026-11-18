# The 62 apps whose summaries Bob uploaded on 17 November 2026 are live on Netlify, at the addresses below

**Status:** working
**Date:** 2026-11-17

## The idea
Most app summaries in `raw/apps/` name only a private Claude artifact, so a reader of this repository could not reach the apps (Q104). On 17 November 2026 Bob deployed the 62 apps whose summaries he uploaded that day to Netlify. He said so in three messages: "i added at at least 50 netlify apps and uploaded the md file to the second brain repo", then "fixed the third group is uploaded", then "fixed the names". Claude then read each site's state from Bob's Netlify account through the Netlify connector, read-only, one `get-project` call per site. Every one of the 62 reported its current deploy as `ready`, with no password and no team sign-in required. Claude did not open the pages, because netlify.app could not be reached from the session; "live" here means Netlify's own report that the deploy finished.

## Proof / from scratch

**How each address was matched.** The site name was matched to the summary's file name with the version taken off. Two sites first had other names, `hydroouple-interactive` and `icm-kcs`; Bob renamed them at about 21:10 Eastern time, and both were read again as `ready` under the names below. The twelve sites of the third group first showed no finished deploy; after Bob uploaded them again, all twelve read `ready`.

**What this does not say.** That an app works, or that the deployed page is the version its summary describes: 56 of the summaries were written from the published Claude artifacts and six ship with their apps, and the Netlify copies were uploaded separately. Several summaries say on their `links:` line that the app was "not yet deployed"; that was true when they were written and is overtaken by this note. No other site on the account is listed here.

| App | Summary | Netlify address |
|---|---|---|
| BobSWMM App Catalog | `raw/apps/bobswmm-app-catalog-v1.0.md` | https://bobswmm-app-catalog.netlify.app |
| CHM Reader 2026 | `raw/apps/chm-reader-2026-v1.0.0.md` | https://chm-reader-2026.netlify.app |
| Conformal SWMM | `raw/apps/conformal-swmm-v1.0.0.md` | https://conformal-swmm.netlify.app |
| Four Ways to K | `raw/apps/four-ways-to-k-v1.0.md` | https://four-ways-to-k.netlify.app |
| Hard Meters, Soft Models | `raw/apps/hard-meters-soft-models-v1.0.md` | https://hard-meters-soft-models.netlify.app |
| Hedron Walk | `raw/apps/hedron-walk-v1.7.0.md` | https://hedron-walk.netlify.app |
| HydroCouple Interactive | `raw/apps/hydrocouple-interactive-v1.0.0.md` | https://hydrocouple-interactive.netlify.app |
| ICM 2D Table Atlas | `raw/apps/icm-2d-table-atlas-v1.1.md` | https://icm-2d-table-atlas.netlify.app |
| ICM Exchange 2026 | `raw/apps/icm-exchange-2026-v2026.2.md` | https://icm-exchange-2026.netlify.app |
| ICM + InfoDrainage KCS Catalog | `raw/apps/icm-kcs-catalog-2026-v2026.5.md` | https://icm-kcs-catalog.netlify.app |
| ICM Sediment Field Guide | `raw/apps/icm-sediment-field-guide-v1.1.md` | https://icm-sediment-field-guide.netlify.app |
| IFS Analysis Explorer | `raw/apps/ifs-analysis-explorer-v1.0.md` | https://ifs-analysis-explorer.netlify.app |
| Inside hydrocouple.platform | `raw/apps/inside-hydrocouple-platform-v1.1.md` | https://inside-hydrocouple-platform.netlify.app |
| Kleinian SWMM | `raw/apps/kleinian-swmm-v1.6.1.md` | https://kleinian-swmm.netlify.app |
| Lead Pump Pointer | `raw/apps/lead-pump-pointer-v1.1.md` | https://lead-pump-pointer.netlify.app |
| Logic-Based Generative SWMM5 | `raw/apps/logic-based-generative-swmm5-v2.0.0.md` | https://logic-based-generative-swmm5.netlify.app |
| Low-Spot Census | `raw/apps/low-spot-census-v1.0.md` | https://low-spot-census.netlify.app |
| Meshing Field Guide | `raw/apps/meshing-field-guide-v1.0.md` | https://meshing-field-guide.netlify.app |
| The Narrow Band | `raw/apps/narrow-band-v1.0.0.md` | https://narrow-band.netlify.app |
| Network Design Glass Box | `raw/apps/network-design-glass-box-v1.0.md` | https://network-design-glass-box.netlify.app |
| Network Lift | `raw/apps/network-lift-v1.2.md` | https://network-lift.netlify.app |
| Non-Prismatic Channel Lab | `raw/apps/non-prismatic-channel-lab-v1.0.md` | https://non-prismatic-channel-lab.netlify.app |
| OpenSWMM 3D Code Model | `raw/apps/openswmm-3d-code-model-v1.1.md` | https://openswmm-3d-code-model.netlify.app |
| OpenSWMM Code | `raw/apps/openswmm-code-v1.0.0.md` | https://openswmm-code.netlify.app |
| Quantile Mapping to SWMM5 / SWMM6 | `raw/apps/quantile-mapping-swmm-v1.2.md` | https://quantile-mapping-swmm.netlify.app |
| Quasi-2D Mesh Maker for SWMM5 | `raw/apps/quasi-2d-mesh-maker-v1.0.md` | https://quasi-2d-mesh-maker.netlify.app |
| Rain-on-Grid Workbench | `raw/apps/rain-on-grid-workbench-v1.0.md` | https://rain-on-grid-workbench.netlify.app |
| The Rigid Column Test | `raw/apps/rigid-column-test-v2026-09-30.md` | https://rigid-column-test.netlify.app |
| Rule 110 in SWMM5 | `raw/apps/rule110-swmm5-v1.0.0.md` | https://rule110-swmm5.netlify.app |
| The Runoff Block | `raw/apps/runoff-block-v1.1.md` | https://runoff-block.netlify.app |
| Sandbox Companion | `raw/apps/sandbox-companion-v1.0.md` | https://sandbox-companion.netlify.app |
| Selective Fidelity | `raw/apps/selective-fidelity-v1.0.md` | https://selective-fidelity.netlify.app |
| Six Tools Workbench | `raw/apps/six-tools-workbench-v1.1.md` | https://six-tools-workbench.netlify.app |
| Socratic Engine Chat | `raw/apps/socratic-engine-chat-v1.0.0.md` | https://socratic-engine-chat.netlify.app |
| SRTC Radio for ICM | `raw/apps/srtc-radio-icm-v1.0.0.md` | https://srtc-radio-icm.netlify.app |
| SWMM Canon | `raw/apps/swmm-canon-v1.4.md` | https://swmm-canon.netlify.app |
| SWMM Claim Frontier | `raw/apps/swmm-claim-frontier-v1.0.md` | https://swmm-claim-frontier.netlify.app |
| SWMM Clean Repro | `raw/apps/swmm-clean-repro-v1.0.md` | https://swmm-clean-repro.netlify.app |
| SWMM Engine Map | `raw/apps/swmm-engine-map-v2026-10-29.md` | https://swmm-engine-map.netlify.app |
| SWMM Hydraulic Library | `raw/apps/swmm-hydraulic-library-v2.0.md` | https://swmm-hydraulic-library.netlify.app |
| SWMM Inlet Library | `raw/apps/swmm-inlet-library-v1.0.md` | https://swmm-inlet-library.netlify.app |
| SWMM PDF Wizard | `raw/apps/swmm-pdf-wizard-v1.1.0.md` | https://swmm-pdf-wizard.netlify.app |
| SWMM Rhythm Detector | `raw/apps/swmm-rhythm-detector-v1.0.md` | https://swmm-rhythm-detector.netlify.app |
| SWMM Rooms | `raw/apps/swmm-rooms-v1.4.md` | https://swmm-rooms.netlify.app |
| SWMM Run Supervisor | `raw/apps/swmm-run-supervisor-v2026-10-24.md` | https://swmm-run-supervisor.netlify.app |
| SWMM Trouble Graph | `raw/apps/swmm-trouble-graph-v1.3.md` | https://swmm-trouble-graph.netlify.app |
| SWMM5 Implicit Box Solver Test Bench | `raw/apps/swmm5-implicit-box-bench-v2026-10-02.md` | https://swmm5-implicit-box-bench.netlify.app |
| The Shapes of SWMM5 Networks | `raw/apps/swmm5-network-shapes-v1.1.0.md` | https://swmm5-network-shapes.netlify.app |
| SWMM5 Residual Walk | `raw/apps/swmm5-residual-walk-v1.0.md` | https://swmm5-residual-walk.netlify.app |
| swmm5-rs Side by Side | `raw/apps/swmm5-rs-side-by-side-v1.2.md` | https://swmm5-rs-side-by-side.netlify.app |
| swmm5-rust in RustGIS | `raw/apps/swmm5-rust-rustgis-v0.1.0.md` | https://swmm5-rust-rustgis.netlify.app |
| SWMM5 Self-Regeneration | `raw/apps/swmm5-self-regeneration-v1.0.0.md` | https://swmm5-self-regeneration.netlify.app |
| SWMM5 · SWMM6 Curve Sections | `raw/apps/swmm5-swmm6-curve-sections-v1.0.md` | https://swmm5-swmm6-curve-sections.netlify.app |
| SWMM5+ Bench | `raw/apps/swmm5plus-bench-v1.0.md` | https://swmm5plus-bench.netlify.app |
| SWMM5+ Branch Atlas | `raw/apps/swmm5plus-branch-atlas-v2026-10-26.md` | https://swmm5plus-branch-atlas.netlify.app |
| SWMM6 Hands-On Watershed | `raw/apps/swmm6-hands-on-watershed-v1.1.0.md` | https://swmm6-hands-on-watershed.netlify.app |
| SWMMCRAFT Ultimate | `raw/apps/swmmcraft-ultimate-v2.7.md` | https://swmmcraft-ultimate.netlify.app |
| Thirty-One Rubies | `raw/apps/thirty-one-rubies-v1.0.md` | https://thirty-one-rubies.netlify.app |
| Understand Anything for SWMM and ICM | `raw/apps/understand-anything-swmm-icm-v2.0.md` | https://understand-anything-swmm-icm.netlify.app |
| Visual SWMM | `raw/apps/visual-swmm-v0.1.0.md` | https://visual-swmm.netlify.app |
| Walk the Mesh | `raw/apps/walk-the-mesh-v1.0.md` | https://walk-the-mesh.netlify.app |
| Water on the Road | `raw/apps/water-on-the-road-v1.1.md` | https://water-on-the-road.netlify.app |

Typed in by Claude (Anthropic) on 17 November 2026 from the Netlify connector's answers, at Bob's request ("ingest"). Bob has not read this note.

## Links
- [two-pipe-benchmark-step1-run-2026-11-17.md](./two-pipe-benchmark-step1-run-2026-11-17.md): the other record made this day
