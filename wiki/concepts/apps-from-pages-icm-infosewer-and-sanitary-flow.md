---
title: "Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow"
type: concept
updated: 2026-11-18
sources: [S331, S332, S333, S334, S335, S336, S337, S338, S339, S340, S341, S342]
tags: [apps, icm, infosewer, ruby, sanitary-flow]
reviewed: no
---
Twelve summaries that Bob uploaded on 18 November 2026 on InfoWorks ICM beside SWMM5, Ruby for ICM, InfoSewer and sanitary flows. One ships with its app ([S331](../sources/S331-icm-river-reach-modeler-app-md.md)); eleven were written by Claude from the published pages with nothing rerun (Q116).

| App | Version | Date | Source |
|---|---|---|---|
| [ICM River Reach Modeler (app)](../entities/icm-river-reach-modeler.md) | 1.1.0 | 2026-11-12 | [S331](../sources/S331-icm-river-reach-modeler-app-md.md) |
| [RDII Rosetta Stone (app)](../entities/rdii-rosetta-stone.md) | 1.0 | 2026-10-21 | [S332](../sources/S332-rdii-rosetta-stone-summary.md) |
| [ICM Ruby MD Python Maker (app)](../entities/icm-ruby-md-python-maker.md) | 2.0 | 2026-10-24 | [S333](../sources/S333-icm-ruby-md-python-maker-summary.md) |
| [Ruby Glory Map (app)](../entities/ruby-glory-map.md) | 1.0 | 2026-10-25 | [S334](../sources/S334-ruby-glory-map-summary.md) |
| [InfoSewer Exchange in Motion (film)](../entities/infosewer-exchange-in-motion.md) | 1.0 | 2026-11-10 | [S335](../sources/S335-infosewer-exchange-in-motion-summary.md) |
| [Flow Factor Wizard (app)](../entities/flow-factor-wizard.md) | 1.0 | 2026-10-21 | [S336](../sources/S336-flow-factor-wizard-summary.md) |
| [Geo Flow Ruby (app)](../entities/geo-flow-ruby.md) | 2026-10-21 | 2026-10-21 | [S337](../sources/S337-geo-flow-ruby-summary.md) |
| [Geo Flow Population Calculator (app)](../entities/geo-flow-population-calculator.md) | 2 | 2026-10-25 | [S338](../sources/S338-geo-flow-population-calculator-summary.md) |
| [Sewer Science (app)](../entities/sewer-science.md) | 1.0 | 2026-10-22 | [S339](../sources/S339-sewer-science-summary.md) |
| [Vacuum Sewer Toolkit (app)](../entities/vacuum-sewer-toolkit.md) | 1.0 | 2026-10-25 | [S340](../sources/S340-vacuum-sewer-toolkit-summary.md) |
| [ICM Modeller Type (app)](../entities/icm-modeller-type.md) | 1.1.0 | 2026-10 | [S341](../sources/S341-icm-modeller-type-summary.md) |
| [SWMM Similarity Index (app)](../entities/swmm-similarity-index.md) | 1.0 | 2026-10 | [S342](../sources/S342-swmm-similarity-index-summary.md) |

**ICM beside SWMM5.** ICM River Reach Modeler's gradually varied flow matches EPA SWMM 5.2.4 within 0.0001 ft (M1) and 0.0006 ft (M2) over 17 sections [S331](../sources/S331-icm-river-reach-modeler-app-md.md). RDII Rosetta Stone ports the storm-response arithmetic of rdii.c line for line and matches the engine within float precision on 8 models [S332](../sources/S332-rdii-rosetta-stone-summary.md). The ICM Modeller Type quiz's odds were computed over all 9,834,496 combinations of per-dimension splits [S341](../sources/S341-icm-modeller-type-summary.md).

**Ruby for ICM.** Of the 532 Ruby scripts in Innovyze/Open-Source-Support, a shipped Ruby-to-Python converter's output parses for 15 and the rebuilt one's for 464 [S333](../sources/S333-icm-ruby-md-python-maker-summary.md). Ruby Glory Map puts every non-blank line of the InfoSWMM multi-scenario importer in one of 32 sections [S334](../sources/S334-ruby-glory-map-summary.md). InfoSewer Exchange in Motion plays the README of a harness that runs Autodesk's 0060 InfoSewer importer under ICM Exchange; nobody has run it against a live ICM [S335](../sources/S335-infosewer-exchange-in-motion-summary.md).

**Sanitary flow and population.** Peaks do not add: 16,600 people together peak at 7.022 ft3/s, while five separate peaks sum to 8.043 ft3/s, 14.5% over [S336](../sources/S336-flow-factor-wizard-summary.md). The geo-flow original read 0 of 12 polygons and wrote CFS baselines 100.0001 times too large; its rebuild assigns 325 of 329 households [S337](../sources/S337-geo-flow-ruby-summary.md), and a second edition's real-data check assigns 1,782 households and 3,140.1 persons [S338](../sources/S338-geo-flow-population-calculator-summary.md).

**Vacuum sewers.** The vacuum toolkit's register lists 35 corrections; the worst, a sawtooth generator, made a 13 m lift from a single pipe [S340](../sources/S340-vacuum-sewer-toolkit-summary.md). Sewer Science's original put a gravity pipe 74% full where Manning gives 64% [S339](../sources/S339-sewer-science-summary.md).

**Comparing models.** A Bill James-style similarity score gives 1,000 for a unit round trip, where the Lovable engine gave 881 [S342](../sources/S342-swmm-similarity-index-summary.md).

See [InfoWorks ICM](../entities/infoworks-icm.md), [SWMM 5 versus ICM InfoWorks](swmm5-versus-icm-infoworks.md), [ICM Ruby: UI scripts and Exchange scripts](icm-ruby-ui-and-exchange.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](apps-from-pages-icm-and-data.md).
