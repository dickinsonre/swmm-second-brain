---
title: "New Engine and GUI Features in InfoSWMM 14.7 which is based on EPA SWMM 5.1.013"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/new-engine-gui-features-infoswmm-147-which-based-epa-swmm-dickinson
created: "2019-03-01 17:57"
published: "2019-03-01 18:04"
words: 793
export_sha256: d2204f4069775c82c47dbc65a93b624735998d2c5c9572147e8363c4363cc2a7
---
# New Engine and GUI Features in InfoSWMM 14.7 which is based on EPA SWMM 5.1.013

![Preissmann Slot - the Slot option uses a Preissmann Slot to add a small amount of virtual top surface width to full flowing pipes so that SWMM's normal procedure for updating nodal heads can continue to be used.](https://media.licdn.com/mediaC4E12AQHrBJqGiEFtWw "Preissmann Slot - the Slot option uses a Preissmann Slot to add a small amount of virtual top surface width to full flowing pipes so that SWMM's normal procedure for updating nodal heads can continue to be used.")

## New Features in Innovyze SWMM 14.7

New Engine and GUI Features in InfoSWMM 14.7 which is based on EPA SWMM 5.1.013

More about EPA SWMM 5.1.013 [https://swmm5.org/2018/08/15/swmm-5-1-update-history-up-to-swmm-5-1-013/](https://swmm5.org/2018/08/15/swmm-5-1-update-history-up-to-swmm-5-1-013/)

Individual subcatchments can be assigned time patterns that adjust depression storage, pervious surface roughness and infiltration capacity on a monthly basis (see Subcatchment Editor).***N-Perv Pattern***Name of optional monthly [Time Pattern](https://swmm5.org/2019/03/Time_Patterns.htm) adjustments applied to pervious Manning’s n (*N-Perv*). Leave blank if not applicable.***Dstore Pattern***Name of optional monthly [Time Pattern](https://swmm5.org/2019/03/Time_Patterns.htm) adjustments applied to both depression storage (*Dstore*) values. Leave blank if not applicable.***Infil. Pattern***Name of optional monthly [Time Pattern](https://swmm5.org/2019/03/Time_Patterns.htm)adjustments applied to the pervious area’s hydraulic conductivity. Leave blank if not applicable.The Subcatchment Runoff Summary Report now includes both pervious and impervious total runoff volumes (prior to any LID treatment) for each subcatchment.LID controls can now treat a designated portion of a subcatchment’s pervious area runoff (previously they could only treat impervious area runoff). See LID Usage Editor (see LID Editor).A closed vessel can now be modeled as a storage unit node that is allowed to pressurize up to a designated Surcharge Depth value (see Storage Editor). If this depth is 0 then the unit is modeled as before as an open vessel.·Permeable pavement LID units subjected to clogging over time can now have their permeability partly or fully restored at periodic time intervals (see LID Pavement Layer).

The following options were added to control flow out of LID units through their underdrains

(see LID Drain System):

i\. A storage layer water depth above which a closed drain automatically opens.

ii\. A storage layer water depth below which an open drain automatically closes.

iii\. A control curve that specifies how the nominal drain flow rate is adjusted as a function

of the head seen by the drain (see Bio-Retention Cell LID Control).

A choice of method used to handle surcharging has been added to the list of Dynamic Wave options. The EXTRAN method continues to use the traditional Surcharge Algorithm to update the head at surcharged nodes. The new SLOT option attaches a Preissmann Slot to closed conduits flowing more than 98.5% full that eliminates the need to switch to the Surcharge Algorithm for surcharged nodes (see Dynamic Wave Routing Options).**Selects which method will be used to handle surcharge conditions.**

> **Extran** – The Extran option uses a variation of the Surcharge Algorithm from previous versions of SWMM to update nodal heads when all connecting links become full. **This option is the default and was used in SWMM3, SWMM4 and versions of SWMM 5 before SWMM 5.1.012**

> **Preissmann Slot** – the Slot option uses a Preissmann Slot to add a small amount of virtual top surface width to full flowing pipes so that SWMM’s normal procedure for updating nodal heads can continue to be used.

![](https://media.licdn.com/dms/image/v2/C4E12AQH46EsukfL9wg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1551463323043?e=1795651200&v=beta&t=JQ2WGdIsCfFyjLHJGkDaS339t9Ryzwt2woHrt8xmUKY)

Users can now choose to set a periodic time step for control rule evaluation (see Time Step Options). If this step is 0 then rules are tested as before at every routing time step.The option was added to have time series results for a project’s nodes and links be reported as average values computed over a reporting time step instead of being interpolated point values at the end of the reporting time step (see Report Options).Pollutant removal percentages can now be assigned to LID processes that have underdrains (see LID Pollutant Removal). The removals apply to flow leaving the unit through the drain and not to any surface overflow from the unit (see Pollutant Removal).A weir’s discharge coefficient can now be allowed to vary with head across the weir by assigning it a Weir Curve (see Weir Editor). Weir curves tabulate coefficient values at specific head levels.·
