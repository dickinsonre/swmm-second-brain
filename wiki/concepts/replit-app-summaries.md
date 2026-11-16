---
title: Replit apps and the summaries Replit Agent wrote
type: concept
updated: 2026-11-15
sources: [S96, S97, S98, S99, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S115, S116]
tags: [apps, replit, verification, ai-agents]
reviewed: 11/16/2026
---
On 15 November 2026 eighteen of Bob's Replit apps each got a technical summary, written inside its project by Replit Agent, and those eighteen files were ingested the same day as [S96](../sources/S96-swmm5-ui-replit-summary.md) to [S113](../sources/S113-geoai-flood-impact-replit-summary.md). Every one ends by saying that Replit Agent wrote it and that Bob has not yet reviewed it (Q67).

**The apps**

| App | Site name (`.replit.app`) | Replit project | Source |
|---|---|---|---|
| [SWMM5-UI (app)](../entities/swmm5-ui.md) | `swmm-ui-engine` | Swmm UI Engine | [S96](../sources/S96-swmm5-ui-replit-summary.md) |
| [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md) | `swmm-filebase--robertdickinson` | SWMM Filebase | [S97](../sources/S97-swmm5-network-miner-replit-summary.md) |
| [SWMM5 INP MAKER (app)](../entities/swmm5-inp-maker.md) | `swmm-inp-maker` | SWMM INP Maker | [S98](../sources/S98-swmm5-inp-maker-replit-summary.md) |
| [SWMM5 Lego Model (app)](../entities/swmm5-lego-model.md) | `swmm-lego-model` | SWMM Lego Model | [S99](../sources/S99-swmm5-lego-model-replit-summary.md) |
| [Camel_SWMM (app)](../entities/camel-swmm.md) | `swmm-pilot-robertdickinson` | Swmm5AppEngine | [S100](../sources/S100-camel-swmm-replit-summary.md) |
| [SWMM5 Manual Search (app)](../entities/swmm5-manual-search.md) | `swmm-manual-search-robertdickinson` | SJ_SWMM5_Manual_Search | [S101](../sources/S101-swmm5-manual-search-replit-summary.md) |
| [SWMM Manual Search landing page (app)](../entities/swmm-manual-search-landing-page.md) | `video-search` | Video Search | [S102](../sources/S102-swmm-manual-search-landing-page-replit-summary.md) |
| [InfoSewer and InfoSWMM Legacy Model Reader (app)](../entities/infosewer-infoswmm-legacy-model-reader.md) | `data-importer-robertdickinson` | InfoSWMM-InfoSewer-Reader | [S103](../sources/S103-legacy-model-reader-replit-summary.md) |
| [XPX to Shapefile Converter (app)](../entities/xpx-to-shapefile-converter.md) | `xps-to-shape--robertdickinson` | XpsToShape | [S104](../sources/S104-xpx-to-shapefile-replit-summary.md) |
| [SWMM5 .inp File Viewer (app)](../entities/swmm5-inp-file-viewer.md) | `swmm-5-inp-reader-robertdickinson` | SWMM5InpReader | [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md) |
| [SWMM5 Topology Sandbox (app)](../entities/swmm5-topology-sandbox.md) | `fractal-swmm-gen--robertdickinson` | Fractal SWMMGen | [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md) |
| [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md) | `green-infiltration--robertdickinson` | Green Infiltration | [S107](../sources/S107-green-ampt-calculator-replit-summary.md) |
| [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md) | `horton-model--robertdickinson` | SWMM5RunoffInfiltration | [S108](../sources/S108-runoff-and-infiltration-replit-summary.md) |
| [SingaPourApps (app)](../entities/singapourapps.md) | `singa-pour-site--robertdickinson` | SingaPour Site | [S109](../sources/S109-singapourapps-replit-summary.md) |
| [InfoDrainage Explorer (app)](../entities/infodrainage-explorer.md) | `bob-swmm-info` | InfoDrainage Explorer | [S110](../sources/S110-infodrainage-explorer-replit-summary.md) |
| [MapSWMMSewer Code Repository (app)](../entities/mapswmmsewer-code-repository.md) | `sewer-code-search` | Sewer Code Search | [S111](../sources/S111-mapswmmsewer-code-repository-replit-summary.md) |
| [City Temperature Explorer (app)](../entities/city-temperature-explorer.md) | `temp-monitor-1` | Temp Monitor | [S112](../sources/S112-city-temperature-explorer-replit-summary.md) |
| [GeoAI Flood Impact (app)](../entities/geoai-flood-impact.md) | `spatial-impact-insight` | Spatial Impact Insight | [S113](../sources/S113-geoai-flood-impact-replit-summary.md) |

The project names are as seen in Replit when the files were copied (see the log).

**What the eighteen have in common**
- None records a human review. Each file has the line "Human review: none recorded", in one wording or another [S96](../sources/S96-swmm5-ui-replit-summary.md) [S113](../sources/S113-geoai-flood-impact-replit-summary.md).
- Checks were made on the development copy, not the published one. One file found its published API answering 404 [S109](../sources/S109-singapourapps-replit-summary.md).
- Eight carry the day the summary was written as their `date:`, because the project records no release date: [S96](../sources/S96-swmm5-ui-replit-summary.md), [S97](../sources/S97-swmm5-network-miner-replit-summary.md), [S99](../sources/S99-swmm5-lego-model-replit-summary.md), [S102](../sources/S102-swmm-manual-search-landing-page-replit-summary.md), [S104](../sources/S104-xpx-to-shapefile-replit-summary.md), [S107](../sources/S107-green-ampt-calculator-replit-summary.md), [S108](../sources/S108-runoff-and-infiltration-replit-summary.md), [S113](../sources/S113-geoai-flood-impact-replit-summary.md) (Q68).

**Where they differ**
- Six run an EPA SWMM engine: [S96](../sources/S96-swmm5-ui-replit-summary.md), [S97](../sources/S97-swmm5-network-miner-replit-summary.md), [S98](../sources/S98-swmm5-inp-maker-replit-summary.md), [S99](../sources/S99-swmm5-lego-model-replit-summary.md), [S100](../sources/S100-camel-swmm-replit-summary.md), [S101](../sources/S101-swmm5-manual-search-replit-summary.md). The other twelve give `engines: none`.
- Five report a passing test suite: 58 Vitest tests [S96](../sources/S96-swmm5-ui-replit-summary.md), 79 [S99](../sources/S99-swmm5-lego-model-replit-summary.md), 29 [S100](../sources/S100-camel-swmm-replit-summary.md), 25 [S101](../sources/S101-swmm5-manual-search-replit-summary.md), and 100 conversion checks [S103](../sources/S103-legacy-model-reader-replit-summary.md). The other thirteen have no test suite or discovered no tests.
- Two failed their TypeScript check: 19 diagnostics [S97](../sources/S97-swmm5-network-miner-replit-summary.md) and 30 errors [S98](../sources/S98-swmm5-inp-maker-replit-summary.md).
- Two call an AI model when they run: OpenAI's `gpt-5` [S100](../sources/S100-camel-swmm-replit-summary.md) and Anthropic's `claude-sonnet-4-5` [S101](../sources/S101-swmm5-manual-search-replit-summary.md).
- Four name a GitHub repository: [S96](../sources/S96-swmm5-ui-replit-summary.md), [S97](../sources/S97-swmm5-network-miner-replit-summary.md), [S101](../sources/S101-swmm5-manual-search-replit-summary.md), [S103](../sources/S103-legacy-model-reader-replit-summary.md). The other fourteen give `repo: none`.
- Six say their records name Replit Agent in the building of the app: [S96](../sources/S96-swmm5-ui-replit-summary.md), [S97](../sources/S97-swmm5-network-miner-replit-summary.md), [S98](../sources/S98-swmm5-inp-maker-replit-summary.md), [S100](../sources/S100-camel-swmm-replit-summary.md), [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md), [S113](../sources/S113-geoai-flood-impact-replit-summary.md). The other twelve say the records do not identify an AI tool (Q71).

**Faults the summaries report.** Several files list faults found by reading the code or loading a page. None was rerun. They are listed in Q69.

**Later the same day.** The two projects that had no summary when these files were copied, EPANET SWMM Experts and SWMM Explorer, got one, [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md) and [S116](../sources/S116-swmm5-explorer-replit-summary.md), among seventeen more: [Replit apps: the second seventeen summaries](replit-app-summaries-second-batch.md).

See [WebAssembly builds against native builds](wasm-against-native-builds.md), [Infiltration methods](infiltration-methods.md), [Bob's GitHub repositories (where the rest of the material lives)](../entities/bobs-github-repositories.md).
