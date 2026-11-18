---
title: "Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them"
type: concept
updated: 2026-11-18
sources: [S268, S269, S270, S271, S272, S273, S274, S275, S276, S277, S278, S279]
tags: [apps, swmm5, epanet, verification, calibration]
reviewed: no
---
Twelve summaries that Bob uploaded on 18 November 2026 on SWMM5, its history, EPANET and the checks made on engines. Ten were written by Claude from the published pages with nothing rerun (Q111); two ship with their apps, [S268](../sources/S268-inside-the-network-cfd-app-md.md) and [S272](../sources/S272-swmm5-walks-downhill-app-md.md). [S270](../sources/S270-how-many-languages-swmm5-summary.md) and [S279](../sources/S279-finite-difference-vs-ml-summary.md) describe a document and a dashboard, converted to standalone pages for Netlify.

| App | Version | Date | Source |
|---|---|---|---|
| [Inside the Network (app)](../entities/inside-the-network-cfd.md) | 1.1.1 | 2026-11-12 | [S268](../sources/S268-inside-the-network-cfd-app-md.md) |
| [Storm Sewer Manhole (app)](../entities/storm-sewer-manhole.md) | 2026-10-20 | 2026-10-20 | [S269](../sources/S269-storm-sewer-manhole-summary.md) |
| [How Many Languages Can the SWMM5 Engine Live In? (document)](../entities/how-many-languages-swmm5.md) | 2026-10-28 | 2026-10-28 | [S270](../sources/S270-how-many-languages-swmm5-summary.md) |
| [SWMM 4.4H Workbench (app)](../entities/swmm44h-workbench.md) | 2026-10-17 | 2026-10-17 | [S271](../sources/S271-swmm44h-workbench-summary.md) |
| [SWMM5 Walks Downhill (app)](../entities/swmm5-walks-downhill.md) | 1.1.0 | 2026-11-15 | [S272](../sources/S272-swmm5-walks-downhill-app-md.md) |
| [Agreement Is the Null (app)](../entities/agreement-is-the-null.md) | 1.1.0 | 2026-10-04 | [S273](../sources/S273-agreement-is-the-null-summary.md) |
| [Tri-Pyramid (app)](../entities/tri-pyramid.md) | 3.0 | 2026-10-20 | [S274](../sources/S274-tri-pyramid-summary.md) |
| [Des Moines Sewer to SWMM5 (app)](../entities/des-moines-sewer-swmm5.md) | 1.0 | 2026-10-18 | [S275](../sources/S275-des-moines-sewer-swmm5-summary.md) |
| [Brick City Water Cycle (app)](../entities/brick-city-water-cycle.md) | 1.0 | 2026-10-24 | [S276](../sources/S276-brick-city-water-cycle-summary.md) |
| [EPANET Total Head Explorer (app)](../entities/epanet-total-head-explorer.md) | 2026-11-03 | 2026-11-03 | [S277](../sources/S277-epanet-total-head-explorer-summary.md) |
| [Chanakya's Counsel for SWMM (app)](../entities/chanakya-counsel.md) | 1.6.0 | 2026-10-20 | [S278](../sources/S278-chanakya-counsel-summary.md) |
| [Finite difference vs ML for flood modeling (dashboard)](../entities/finite-difference-vs-ml.md) | 2026-10-09 | 2026-10-09 | [S279](../sources/S279-finite-difference-vs-ml-summary.md) |

**Checks on engines, not just results.** A port matches a Linux build of EPA 5.2.4 byte for byte only if its math library and number formatter do: swapping glibc for musl changed 55 of 440 corpus runs and moved one peak node depth by 2.65 ft [S270](../sources/S270-how-many-languages-swmm5-summary.md). Option switches inside one engine, priced as a change in Manning's n, show what an engine comparison can resolve: inertial terms off moves EXTRAN example 1 less than raising n by 2% [S273](../sources/S273-agreement-is-the-null-summary.md). A 120 s report step caught 31% of one link's routing-step peak [S274](../sources/S274-tri-pyramid-summary.md).

**Old and new engines side by side.** SWMM 4.4H in the browser, as distributed and with 121 corrections, against SWMM5 on 300 converted corpus models: a median 8.3% difference in conduit peak flow [S271](../sources/S271-swmm44h-workbench-summary.md). A JavaScript port of EPANET 2.2 matches the compiled engines to 4.4 x 10^-12 ft [S277](../sources/S277-epanet-total-head-explorer-summary.md).

**Calibration and its limits.** A gradient-descent walk recovers two knobs on a built-in model and ends at NSE 0.966 with the wrong knobs on extran10 [S272](../sources/S272-swmm5-walks-downhill-app-md.md); a machine-learning surrogate matches its solver to 0.007 ft inside its record and spreads 5.90 to 9.75 ft outside it [S279](../sources/S279-finite-difference-vs-ml-summary.md).

**Models from public data and teaching boards.** A city's open sewer GIS to SWMM5, where the sanitary sample as published runs at 6.184% routing continuity [S275](../sources/S275-des-moines-sewer-swmm5-summary.md); a toy-brick town where the orifice, not the rain gardens, sets the release [S276](../sources/S276-brick-city-water-cycle-summary.md); a manhole that lifts its cover at 2.3 times pipe capacity [S269](../sources/S269-storm-sewer-manhole-summary.md); a decision walked through the Arthashastra [S278](../sources/S278-chanakya-counsel-summary.md).

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](apps-from-pages-swmm6-and-benchmarks.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](apps-from-pages-tools-and-puzzles.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](apps-from-pages-history-and-swmm5.md).