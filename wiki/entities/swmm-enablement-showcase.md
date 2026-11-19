---
title: "SWMM Enablement Showcase (app)"
type: entity
updated: 2026-11-19
sources: [S387, S388, S384, S385, S386]
tags: [apps, showcase, sites, publishing]
reviewed: no
---
Bob's one-page showcase of twelve of his browser apps. Each card carries a screenshot, the app's Netlify address, its own version and date, one finding with its numbers, one limit, and the engines it runs [S387](../sources/S387-swmm-enablement-showcase-app-md.md). Version 1.0, 2026-11-19. The summary gives Netlify as not yet deployed, with the suggested site name swmm-enablement-showcase [S387](../sources/S387-swmm-enablement-showcase-app-md.md).

**How it was made.** Claude proposed twenty candidates and checked each with an automated first-minute test: script errors, dark first paint with the device set to light, a 390 px phone screen, values shown as NaN or undefined, text contrast, and a .md beside the page. Flagged items were looked at by hand, the cards were written from each app's own summary with the numbers unchanged, and Bob approved the twelve [S387](../sources/S387-swmm-enablement-showcase-app-md.md).

**The twelve, by group** [S387](../sources/S387-swmm-enablement-showcase-app-md.md)

| Group | Apps |
|---|---|
| Where SWMM came from | [The Runoff Block](runoff-block.md), [OpenSWMM Code](openswmm-code.md) |
| Inside the engine | [SWMM5 Residual Walk](swmm5-residual-walk.md), [Non-Prismatic Channel Lab](non-prismatic-channel-lab.md), [The Rigid Column Test](rigid-column-test.md), [SWMM Rhythm Detector](swmm-rhythm-detector.md) |
| Surfaces, meshes and sediment | [Walk the Mesh](walk-the-mesh.md), [Rain-on-Grid Workbench](rain-on-grid-workbench.md), [ICM Sediment Field Guide](icm-sediment-field-guide.md) |
| How the claims are checked | [SWMM Claim Frontier](swmm-claim-frontier.md), [SWMM Engine Map](swmm-engine-map.md), [SWMM Clean Repro](swmm-clean-repro.md) |

Six of the twelve run EPA SWMM 5.2.4 in the browser. The other six show recorded runs of SWMM 5.2.4 and OpenSWMM 6, the engine source, a claims register or textbook formulas, and each card says which [S387](../sources/S387-swmm-enablement-showcase-app-md.md). Walk the Mesh is linked at https://walk-the-swmm6-2d-mesh.netlify.app, by Bob's answer [S388](../sources/S388-note-walk-the-mesh-address.md).

**What it does not show.** It repeats the apps' own findings and reruns none. A screenshot shows only the opening view. The apps were checked from local copies of their deployed files, because netlify.app could not be reached from the build machine [S387](../sources/S387-swmm-enablement-showcase-app-md.md). Three apps fixed the same day are left off until they are redeployed: [Visual SWMM](visual-swmm.md) [S384](../sources/S384-visual-swmm-summary-v0-1-1.md), [SWMM6 Hands-On Watershed](swmm6-hands-on-watershed.md) [S385](../sources/S385-swmm6-hands-on-watershed-summary-v1-1-1.md) and [Four Ways to K](four-ways-to-k.md) [S386](../sources/S386-four-ways-to-k-summary-v1-0-1.md).

**Noted at ingest.** Each card's version and date matches the current source page for that app. One small fault the check found was left in place: a label in The Rigid Column Test's light theme at 2.06:1 contrast [S387](../sources/S387-swmm-enablement-showcase-app-md.md).

See [App build contract (four working principles)](../concepts/app-build-contract.md), [Robert (Bob) Dickinson](robert-dickinson.md).
