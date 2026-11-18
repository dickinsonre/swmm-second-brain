---
title: "Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools"
type: concept
updated: 2026-11-18
sources: [S315, S316, S317, S318, S319, S320, S321, S322, S323, S324, S325, S326, S327, S328, S329, S330]
tags: [apps, epanet, swmm5, conversion, verification]
reviewed: no
---
Sixteen summaries that Bob uploaded on 18 November 2026 on EPANET and pressure pipes, converters between SWMM generations, and tools that read what SWMM writes. Three ship with their apps ([S315](../sources/S315-epanet-for-swmm5-experts-app-md.md), [S323](../sources/S323-extran3-mograph-app-md.md), [S324](../sources/S324-swmm1-engine-mograph-app-md.md)); thirteen were written by Claude from the published pages with nothing rerun; Bob marked all of them reviewed on 18 November 2026 (Q116, settled).

| App | Version | Date | Source |
|---|---|---|---|
| [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md) | 2.0.0 | 2026-11-12 | [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md) |
| [EPANET Web (app)](../entities/epanet-web.md) | 1.0 | 2026-10-25 | [S316](../sources/S316-epanet-web-summary.md) |
| [SWMM vs EPANET (app)](../entities/swmm-vs-epanet.md) | 1.0 | 2026-10 | [S317](../sources/S317-swmm-vs-epanet-summary.md) |
| [WNTR Toolkit (app)](../entities/wntr-toolkit.md) | 1.0.0 | 2026-10-25 | [S318](../sources/S318-wntr-toolkit-summary.md) |
| [Bernoulli Flow in a Pipe (app)](../entities/bernoulli-flow-in-a-pipe.md) | 2.2 | 2026-11-03 | [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md) |
| [Manning's n Explorer (app)](../entities/mannings-n-explorer.md) | 3.1 | 2026-10-24 | [S320](../sources/S320-mannings-n-explorer-summary.md) |
| [XPSWMM to SWMM5 Converter (app)](../entities/xpswmm-to-swmm5-converter.md) | 1.0.0 | 2026-10-25 | [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md) |
| [Legacy SWMM Converter (app)](../entities/legacy-swmm-converter.md) | 1.0.0 | 2026-10 | [S322](../sources/S322-legacy-swmm-converter-summary.md) |
| [EXTRAN III Mograph (film)](../entities/extran3-mograph.md) | 1.0 | 2026-11-16 | [S323](../sources/S323-extran3-mograph-app-md.md) |
| [SWMM 1 Engine Mograph (film)](../entities/swmm1-engine-mograph.md) | 1.0 | 2026-11-16 | [S324](../sources/S324-swmm1-engine-mograph-app-md.md) |
| [SWMM5 Interactive Report Viewer (app)](../entities/swmm5-interactive-report-viewer.md) | 2.1 | 2026-10-31 | [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md) |
| [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md) | 2.0 | 2026-10 | [S326](../sources/S326-swmm5-network-miner-summary.md) |
| [Collatz Wave Maker (app)](../entities/collatz-wave-maker.md) | 2.0 | 2026-10-25 | [S327](../sources/S327-collatz-wave-maker-summary.md) |
| [BlueSky-ICM (app)](../entities/bluesky-icm.md) | 1.0.0 | 2026-10-21 | [S328](../sources/S328-bluesky-icm-summary.md) |
| [The Rational Limit (app)](../entities/the-rational-limit.md) | 1.0 | 2026-10-12 | [S329](../sources/S329-the-rational-limit-summary.md) |
| [NA Rain Grid (app)](../entities/na-rain-grid.md) | 2.0.0 | 2026-10-25 | [S330](../sources/S330-na-rain-grid-summary.md) |

**EPANET checked against EPANET.** Version 2.0 of EPANET for SWMM5 Experts built EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5 from source. On one 12-in pipe at six flows SWMM's FORCE_MAIN matched the Hazen-Williams formula within 0.001 ft, and the same work found 15 errors in version 1 [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md). EPANET Web runs OWA EPANET 2.3.5 in the browser; on Net1, 2,751 of 2,781 hydraulic values are bit-identical to OWA's native reference output [S316](../sources/S316-epanet-web-summary.md). In WNTR Toolkit the tanks' books settle a disagreement between two simulators: EPANET 2.2's tanks are off by 119%, 122% and 53% of their working volume, because an empty tank keeps flowing out [S318](../sources/S318-wntr-toolkit-summary.md). SWMM and EPANET on one 6-node network agree to 0.29 ft head RMSE, with SWMM at +0.708% continuity [S317](../sources/S317-swmm-vs-epanet-summary.md). Bernoulli Flow's rewritten solver matches 51 engine results within 0.0003%; its first version missed EPANET by as much as 149% [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md).

**Converters between generations.** XPSWMM to SWMM5: 0 of 153 test models ran from the Lovable converter's output and 153 of 153 from the rebuilt one, but no real .xp file has been converted yet [S321](../sources/S321-xpswmm-to-swmm5-converter-summary.md). SWMM4 decks to SWMM5: 11 of 12 samples run, and on six EXTRAN models the median difference in peak conduit flow against SWMM 4.4H is 0.5% to 4.8% [S322](../sources/S322-legacy-swmm-converter-summary.md). Two films introduce the EXTRAN III Workbench and the SWMM 1 engine [S323](../sources/S323-extran3-mograph-app-md.md) [S324](../sources/S324-swmm1-engine-mograph-app-md.md).

**Reading what SWMM writes.** The Interactive Report Viewer reads 4,291,001 .out values bit-identical to EPA's swmm_output on 54 runs [S325](../sources/S325-swmm5-interactive-report-viewer-summary.md). BlueSky-ICM found that its source's continuity regex read every report as 0.00% [S328](../sources/S328-bluesky-icm-summary.md); Collatz Wave Maker found that its original ran EPA SWMM 5.2.2, not 5.2.4 (198 against 197 flooded nodes) [S327](../sources/S327-collatz-wave-maker-summary.md); the single-file Network Miner fixes eleven ReSWMM writing defects [S326](../sources/S326-swmm5-network-miner-summary.md).

**Runoff, rain and roughness.** Eight of eight equilibrium cases plateau at 1.000037 x (i - f)A in EPA SWMM 5.2.4, the 0.0037% being SWMM's own acre constant [S329](../sources/S329-the-rational-limit-summary.md). NA Rain Grid's storms return the Atlas 14 depth to 10^-9 in; its Lovable version asked NOAA for data and threw the answer away [S330](../sources/S330-na-rain-grid-summary.md). Manning's n Explorer found that its flood-wave tab routed through a single sub-reach, so all three curves peaked at 8.0 hours [S320](../sources/S320-mannings-n-explorer-summary.md).

See [EPANET](../entities/epanet.md), [Force main friction](force-main-friction.md), [Reading SWMM output](reading-swmm-output.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](apps-from-pages-swmm5-epanet-checks.md).
