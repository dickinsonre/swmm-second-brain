---
title: "Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers"
type: concept
updated: 2026-11-18
sources: [S300, S301, S302, S303, S304, S305, S306, S307, S308, S309, S310, S311, S312, S313, S314]
tags: [apps, swmm6, openswmm, swmm5plus, numerics]
reviewed: no
---
Fifteen summaries that Bob uploaded on 18 November 2026 on OpenSWMM 6 and HydroCouple, SWMM5+ and the numerics of routing. All fifteen were written by Claude from the published pages with nothing rerun; Bob marked all of them reviewed on 18 November 2026 (Q116, settled). [S307](../sources/S307-swmm-front-door-summary.md) describes a design sketch and [S308](../sources/S308-thaw-on-the-thoth-summary.md) a Claude Docs story; [S302](../sources/S302-swmm5-swmm6-mograph-summary.md) and [S303](../sources/S303-hydrocouple-swmm6-mograph-summary.md) are films.

| App | Version | Date | Source |
|---|---|---|---|
| [SWMM6 2D Flood Lab (app)](../entities/swmm6-2d-flood-lab.md) | 0.2.0 | 2026-10-10 | [S300](../sources/S300-swmm6-2d-flood-lab-summary.md) |
| [St. Venant Term Budget (app)](../entities/st-venant-term-budget.md) | 1.0 | 2026-10-05 | [S301](../sources/S301-st-venant-term-budget-summary.md) |
| [SWMM5 / SWMM6 Mograph (film)](../entities/swmm5-swmm6-mograph.md) | 3.1 | 2026-11-09 | [S302](../sources/S302-swmm5-swmm6-mograph-summary.md) |
| [HydroCouple SWMM6 Mograph (film)](../entities/hydrocouple-swmm6-mograph.md) | 1.1 | 2026-11-10 | [S303](../sources/S303-hydrocouple-swmm6-mograph-summary.md) |
| [HydroCouple Study Guide (app)](../entities/hydrocouple-study-guide.md) | 1.0 | 2026-10-25 | [S304](../sources/S304-hydrocouple-study-guide-summary.md) |
| [OpenSWMM MCP Repo Viewer (app)](../entities/openswmm-mcp-repo-viewer.md) | 1.1 | 2026-10-25 | [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md) |
| [OpenSWMM Gymnasium (app)](../entities/openswmm-gymnasium.md) | 1.0 | 2026-10-25 | [S306](../sources/S306-openswmm-gymnasium-summary.md) |
| [SWMM Front Door (sketch)](../entities/swmm-front-door.md) | 0.1 | 2026-11-09 | [S307](../sources/S307-swmm-front-door-summary.md) |
| [Thaw on the Thoth (document)](../entities/thaw-on-the-thoth.md) | 2026-10-21 | 2026-10-21 | [S308](../sources/S308-thaw-on-the-thoth-summary.md) |
| [SWMM5+ Explorer (app)](../entities/swmm5plus-explorer.md) | 1.0.1 | 2026-10-24 | [S309](../sources/S309-swmm5plus-explorer-summary.md) |
| [SWMM5+ Repo Explorer (app)](../entities/swmm5plus-repo-explorer.md) | 1.0.0 | 2026-10-25 | [S310](../sources/S310-swmm5plus-repo-explorer-summary.md) |
| [SWMM Insight Lab (app)](../entities/swmm-insight-lab.md) | 1.0.0 | 2026-10-25 | [S311](../sources/S311-swmm-insight-lab-summary.md) |
| [Aquanuity Theory (app)](../entities/aquanuity-theory.md) | 1.0 | 2026-10-24 | [S312](../sources/S312-aquanuity-theory-summary.md) |
| [Flow Solver Forge (app)](../entities/flow-solver-forge.md) | 1.0 | 2026-10-25 | [S313](../sources/S313-flow-solver-forge-summary.md) |
| [ITM_SWMM Repository Map (app)](../entities/itm-swmm-repository-map.md) | 1.0 | 2026-10 | [S314](../sources/S314-itm-swmm-repository-map-summary.md) |

**OpenSWMM 6 against its own engine and against a flood.** The SWMM6 2D Flood Lab carries a double-precision port of the alpha.4 local-inertial surface solver. It matches the compiled engine to rounding on four cases and on Merewether at 13 ft squares (3.4e-12 ft, both 6,621 substeps); against five levels surveyed after the June 2007 Merewether flood its RMS difference is 0.48 to 0.53 ft across four mesh sizes, against 0.48 ft for TUFLOW as reported [S300](../sources/S300-swmm6-2d-flood-lab-summary.md). With the engine's default four time-step tiers the flood reaches survey point S1 between 400 and 500 s instead of 200 and 300 s, and every run still closes its volume balance [S300](../sources/S300-swmm6-2d-flood-lab-summary.md).

**What the momentum terms say.** St. Venant Term Budget rebuilds each conduit's momentum terms from the .out file and checks the rebuild against an instrumented EPA SWMM 5.2.4 (index 0.4937 from the .out against 0.4940 from the engine). On its 13-conduit demo OpenSWMM 6 alpha.2 stays within 0.30% of each peak while its continuity line reads -29.401% against -0.211% [S301](../sources/S301-st-venant-term-budget-summary.md). Flow Solver Forge builds a 1D solver from parts: its port of SWMM's link-node method matches native SWMM to Nash-Sutcliffe 1.00000, yet on Stoker's dam break that method misses the front by 27.0%, and only Godunov HLL passes all four exact tests [S313](../sources/S313-flow-solver-forge-summary.md). Aquanuity Theory's two 1D teaching solvers agree within 1% on a 0.2% slope and part where the bed is flat (1.90 against 1.78 ft) [S312](../sources/S312-aquanuity-theory-summary.md). Thaw on the Thoth finds gravity in both the slope and the friction terms of SWMM5, so changing GRAVITY from 32.2 to 12.2 alone left the base-flow depth at mile one at 2.38 ft [S308](../sources/S308-thaw-on-the-thoth-summary.md).

**Code and claims around HydroCouple.** A study guide's architecture holds, but 19 of its 27 code lines compile against v1.0.0 and 13 against 2.0 [S304](../sources/S304-hydrocouple-study-guide-summary.md). The MCP server snapshot counts 20 tools, and of three pull requests one merges clean [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md). The gymnasium's shipped TwinTank benchmark delivers 0.667 in of rain instead of 4.0, so doing nothing scores a perfect 1.000 [S306](../sources/S306-openswmm-gymnasium-summary.md). Two films introduce the engine and the hydrocouple.org page [S302](../sources/S302-swmm5-swmm6-mograph-summary.md) [S303](../sources/S303-hydrocouple-swmm6-mograph-summary.md). A design sketch withholds its green check when SWMM6 finite volume disagrees with SWMM 5.2.4 on Example 1 (0.24 against 0.72 ft at J1) [S307](../sources/S307-swmm-front-door-summary.md).

**SWMM5+ read from its source.** Of twelve claims a Lovable site made about SWMM5+, 4 hold: upstream has 88,020 lines of Fortran in 72 files, not about 40k, and no .f90 file makes an MPI call [S309](../sources/S309-swmm5plus-explorer-summary.md). The module graph matches on 71 of 71 declarations and 534 of 534 edges, but 27 of 130 curated edges have no use statement behind them [S310](../sources/S310-swmm5plus-repo-explorer-summary.md) [S311](../sources/S311-swmm-insight-lab-summary.md). The ITM_SWMM fork that puts the Illinois Transient Model into the EPA SWMM 5 GUI has 117 Pascal units among 257 files [S314](../sources/S314-itm-swmm-repository-map-summary.md).

See [OpenSWMM 6 solvers, measured](openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](apps-from-pages-swmm6-and-benchmarks.md).
