---
title: "Apps summarized on 17 November 2026: ICM, data and the tools around models"
type: concept
updated: 2026-11-17
sources: [S205, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255]
tags: [apps, icm, ruby, data]
reviewed: no
---
Thirteen app summaries that Bob uploaded on 17 November 2026: InfoWorks ICM references and scripts, and tools for the data that goes into models. All thirteen were written by Claude (Anthropic) that day from the published pages, with nothing rerun (Q108). Bob deployed all thirteen to Netlify the same day [S205](../sources/S205-note-netlify-addresses.md).

| App | Version | Date | Source |
|---|---|---|---|
| [ICM 2D Table Atlas (app)](../entities/icm-2d-table-atlas.md) | 1.1 | 2026-11-02 | [S243](../sources/S243-icm-2d-table-atlas-summary.md) |
| [ICM Exchange 2026 (app)](../entities/icm-exchange-2026.md) | 2026.2 | 2026-11-02 | [S244](../sources/S244-icm-exchange-2026-summary.md) |
| [ICM + InfoDrainage KCS Catalog (app)](../entities/icm-kcs-catalog-2026.md) | 2026.5 | 2026-11-06 | [S245](../sources/S245-icm-kcs-catalog-2026-summary.md) |
| [ICM Sediment Field Guide (app)](../entities/icm-sediment-field-guide.md) | 1.1 | 2026-11-02 | [S246](../sources/S246-icm-sediment-field-guide-summary.md) |
| [Meshing Field Guide (app)](../entities/meshing-field-guide.md) | 1.0 | 2026-11-02 | [S247](../sources/S247-meshing-field-guide-summary.md) |
| [Network Design Glass Box (app)](../entities/network-design-glass-box.md) | 1.0 | 2026-09-30 | [S248](../sources/S248-network-design-glass-box-summary.md) |
| [SRTC Radio for ICM (app)](../entities/srtc-radio-icm.md) | 1.0.0 | 2026-09-30 | [S249](../sources/S249-srtc-radio-icm-summary.md) |
| [Thirty-One Rubies (app)](../entities/thirty-one-rubies.md) | 1.0 | 2026-11-03 | [S250](../sources/S250-thirty-one-rubies-summary.md) |
| [Understand Anything for SWMM and ICM (app)](../entities/understand-anything-swmm-icm.md) | 2.0 | 2026-11-05 | [S251](../sources/S251-understand-anything-swmm-icm-summary.md) |
| [CHM Reader 2026 (app)](../entities/chm-reader-2026.md) | 1.0.0 | 2026-11-02 | [S252](../sources/S252-chm-reader-2026-summary.md) |
| [Rain-on-Grid Workbench (app)](../entities/rain-on-grid-workbench.md) | 1.0 | 2026-10-06 | [S253](../sources/S253-rain-on-grid-workbench-summary.md) |
| [Network Lift (app)](../entities/network-lift.md) | 1.2 | 2026-10-19 | [S254](../sources/S254-network-lift-summary.md) |
| [IFS Analysis Explorer (app)](../entities/ifs-analysis-explorer.md) | 1.0 | 2026-10-16 | [S255](../sources/S255-ifs-analysis-explorer-summary.md) |

**Nothing here ran in ICM.** Seven are about ICM: the hw_2d tables [S243](../sources/S243-icm-2d-table-atlas-summary.md), the Exchange manual brought to Ruby 3.4 [S244](../sources/S244-icm-exchange-2026-summary.md), the support-article titles [S245](../sources/S245-icm-kcs-catalog-2026-summary.md), sediment [S246](../sources/S246-icm-sediment-field-guide-summary.md), meshing [S247](../sources/S247-meshing-field-guide-summary.md), a rule-based pipe sizer [S248](../sources/S248-network-design-glass-box-summary.md) and a calibration slider layer [S249](../sources/S249-srtc-radio-icm-summary.md). Each says it ran nothing inside ICM, or ran ICM only outside the page. The Ruby was checked on Ruby 2.4.10, 3.3.6 and 3.4.1 [S244](../sources/S244-icm-exchange-2026-summary.md) and on CRuby 3.4.1 in WebAssembly against a stand-in for the ICM API [S250](../sources/S250-thirty-one-rubies-summary.md); ICM 2027 runs Ruby 3.4.6 [S244](../sources/S244-icm-exchange-2026-summary.md).

**The Ruby change.** Through the 2026 releases ICM ran scripts on Ruby 2.4.0; from 2027.0 it runs Ruby 3.4.6 and can load gems; of Autodesk's 532 public example scripts, six contain calls that fail under 3.4 [S244](../sources/S244-icm-exchange-2026-summary.md).

**Two counts of one file.** ICM Exchange 2026 counts 335 methods in ruby_icm_help.md [S244](../sources/S244-icm-exchange-2026-summary.md); Thirty-One Rubies counts 336 [S250](../sources/S250-thirty-one-rubies-summary.md) (Q109).

**Results against the app's own idea.** The 2026 titles the KCS catalog proposed found the right article first 25 times in thirty, against 28 for the 2024 titles [S245](../sources/S245-icm-kcs-catalog-2026-summary.md). A map of SWMM 5.2.4 Claude drew from memory in June found 60 of 365 real file links [S251](../sources/S251-understand-anything-swmm-icm-summary.md). A rainfall reduction factor removed 56.5 % of the rain and still left a sag 1.06 ft deep [S253](../sources/S253-rain-on-grid-workbench-summary.md).

**Data for models.** Help files [S252](../sources/S252-chm-reader-2026-summary.md), CAD drawings [S254](../sources/S254-network-lift-summary.md) and a global weather analysis [S255](../sources/S255-ifs-analysis-explorer-summary.md) turned into forms a model or Claude can read; the weather one finds 6-hourly data puts a year's Hargreaves PET at 84 % of the true value [S255](../sources/S255-ifs-analysis-explorer-summary.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](apps-from-pages-history-and-swmm5.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](apps-from-pages-generators-rain-surfaces.md), [ICM Ruby: UI scripts and Exchange scripts](icm-ruby-ui-and-exchange.md).
