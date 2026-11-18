---
title: "Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI"
type: concept
updated: 2026-11-17
sources: [S205, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267]
tags: [apps, swmm6, hydrocouple, ai-agents, source-code]
reviewed: no
---
Twelve app summaries that Bob uploaded on 17 November 2026: OpenSWMM 6 and the HydroCouple projects around it, the source code of SWMM5 and SWMM6, and apps that put AI or agents next to an engine. Ten were written by Claude (Anthropic) that day from the published pages, with nothing rerun (Q108); two ship with their apps, [S256](../sources/S256-openswmm-3d-code-model-app-md.md) and [S258](../sources/S258-hydrocouple-interactive-app-md.md). Bob deployed all twelve to Netlify the same day [S205](../sources/S205-note-netlify-addresses.md).

| App | Version | Date | Source |
|---|---|---|---|
| [OpenSWMM 3D Code Model (app)](../entities/openswmm-3d-code-model.md) | 1.1 | 2026-11-11 | [S256](../sources/S256-openswmm-3d-code-model-app-md.md) |
| [OpenSWMM Code (app)](../entities/openswmm-code.md) | 1.0.0 | 2026-11-05 | [S257](../sources/S257-openswmm-code-summary.md) |
| [HydroCouple Interactive (app)](../entities/hydrocouple-interactive.md) | 1.0.0 | 2026-11-13 | [S258](../sources/S258-hydrocouple-interactive-app-md.md) |
| [Inside hydrocouple.platform (app)](../entities/inside-hydrocouple-platform.md) | 1.1 | 2026-10-24 | [S259](../sources/S259-inside-hydrocouple-platform-summary.md) |
| [Sandbox Companion (app)](../entities/sandbox-companion.md) | 1.0 | 2026-11-08 | [S260](../sources/S260-sandbox-companion-summary.md) |
| [SWMM6 Hands-On Watershed (app)](../entities/swmm6-hands-on-watershed.md) | 1.1.0 | 2026-11-08 | [S261](../sources/S261-swmm6-hands-on-watershed-summary.md) |
| [SWMM5 · SWMM6 Curve Sections (app)](../entities/swmm5-swmm6-curve-sections.md) | 1.0 | 2026-11-02 | [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md) |
| [SWMM Engine Map (app)](../entities/swmm-engine-map.md) | 2026-10-29 | 2026-10-29 | [S263](../sources/S263-swmm-engine-map-summary.md) |
| [Socratic Engine Chat (app)](../entities/socratic-engine-chat.md) | 1.0.0 | 2026-10-19 | [S264](../sources/S264-socratic-engine-chat-summary.md) |
| [Selective Fidelity (app)](../entities/selective-fidelity.md) | 1.0 | 2026-10-21 | [S265](../sources/S265-selective-fidelity-summary.md) |
| [Six Tools Workbench (app)](../entities/six-tools-workbench.md) | 1.1 | 2026-10-11 | [S266](../sources/S266-six-tools-workbench-summary.md) |
| [BobSWMM App Catalog (app)](../entities/bobswmm-app-catalog.md) | 1.0 | 2026-10-21 | [S267](../sources/S267-bobswmm-app-catalog-summary.md) |

**OpenSWMM 6 in the browser, and around it.** One app runs OpenSWMM 6 in the page, with snow, groundwater and an emulator [S261](../sources/S261-swmm6-hands-on-watershed-summary.md). Three read HydroCouple without running it: its website [S258](../sources/S258-hydrocouple-interactive-app-md.md), its run platform [S259](../sources/S259-inside-hydrocouple-platform-summary.md) and the engine source drawn as a city [S256](../sources/S256-openswmm-3d-code-model-app-md.md). One ports parts of a third party's Apache-licensed flood sandbox that ran OpenSWMM 6 on its author's computer [S260](../sources/S260-sandbox-companion-summary.md).

**The source code itself.** The engine source of 34 SWMM5 releases from 2004 to 2023, with 11 of EPA's listed builds lost [S257](../sources/S257-openswmm-code-summary.md); the OpenSWMM source of 11 November 2026, 925 files and 482,467 lines [S256](../sources/S256-openswmm-3d-code-model-app-md.md); and the map of Bob's engines, where EPA 5.2.4 holds one model per process across 415 state variables [S263](../sources/S263-swmm-engine-map-summary.md).

**Findings, at the pages' word.** OpenSWMM 6 at 137e65e kept a dry conduit's last evaporation rate, reported as fixed upstream on 12 September 2026 [S261](../sources/S261-swmm6-hands-on-watershed-summary.md). SWMM's cross-section tables make a Gothic sewer's outfall peak 29 % above any inflow in dry weather [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md). The HydroCouple platform's packaging scanner does not see an [LID_USAGE] report file [S259](../sources/S259-inside-hydrocouple-platform-summary.md). Five SWMM5 release dates in the source atlas differ from EPA's history [S257](../sources/S257-openswmm-code-summary.md) (Q110).

**AI beside the engine.** A chat that sources every number from the engine [S264](../sources/S264-socratic-engine-chat-summary.md); a patch that solves only the conduits a question needs, 4.15 times fewer steps [S265](../sources/S265-selective-fidelity-summary.md); agent-built code-quality tools run on SWMM and ICM code [S266](../sources/S266-six-tools-workbench-summary.md). None of these was tested with the real Claude inside the app, or by a person end to end.

**Licences.** HydroCouple's site names the interface MIT and, on its home page, the engine Apache-2.0, with an MIT link in an earlier announcement [S258](../sources/S258-hydrocouple-interactive-app-md.md); the platform reader notes that the engine's licence now differs by branch [S259](../sources/S259-inside-hydrocouple-platform-summary.md). See Q83.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](apps-from-pages-history-and-swmm5.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](apps-from-pages-generators-rain-surfaces.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](apps-from-pages-icm-and-data.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
