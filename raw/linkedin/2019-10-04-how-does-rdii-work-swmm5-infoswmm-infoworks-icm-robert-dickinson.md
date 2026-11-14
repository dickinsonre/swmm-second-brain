---
title: "How Does RDII Work in SWMM5, InfoSWMM and InfoWorks ICM?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-does-rdii-work-swmm5-infoswmm-infoworks-icm-robert-dickinson
created: "2019-10-04 12:09"
published: "2019-10-04 12:13"
words: 1251
export_sha256: 87b89fe1b3f35b5492d9c13b23a4022da74920d58c688a0850c5745559b04510
---
# How Does RDII Work in SWMM5, InfoSWMM and InfoWorks ICM?

## RDII in SWMM5 from the SWMM5 Help File (Refactored)

> **Unit Hydrographs  **

Unit Hydrographs 📈💧 Unit Hydrographs (UHs) are pivotal instruments 🛠️ in hydrology, helping experts estimate how rainwater 🌧️ infiltrates sewer systems. Dubbed "unit" hydrographs since they illustrate a catchment's reaction to a standard rainfall unit, generally 1 inch 📏. Their primary function is predicting the amount of rainwater 🌧️ set to enter sewers due to rainfall events. Understanding this is crucial for optimal water flow management in sewers, ensuring we sidestep potential overflows and flood situations 🚫💧🌊.

Diving Deeper into UH Sets and Groups 📚🔄 A UH set encompasses up to three individual unit hydrographs:

1.  Short-term response 🕒: Reflects the catchment's immediate reaction to rainfall.

2.  Intermediate-term response 🕕: Indicates the catchment's response over a slightly extended timeframe.

3.  Long-term response 🕘: Represents the prolonged reaction of the catchment.

A UH group, on the other hand, is an ensemble of up to 12 UH sets, each tailored for a specific month 📅. This is invaluable as catchments can behave differently depending on the month. For instance, summer's dry soil may lead to different infiltration rates compared to winter's moist conditions ❄️☀️.

Within the Storm Water Management Model (SWMM), every UH group is recognized as a distinct entity, complete with a unique identifier and the associated rain gauge's name that feeds it rainfall data 📊💻.

Decoding Unit Hydrograph Parameters 🔍📝 Each UH is characterized by three core parameters:

1.  R: Indicates the rainwater volume fraction that makes its way into the sewer system 🌧️➡️🕳️.

2.  T: Represents the duration from the rain's commencement to the UH's peak, measured in hours ⏳.

3.  K: Denotes the ratio between the UH's recession time and its peak time ⌛🔄.

![](https://media.licdn.com/dms/image/v2/C4E12AQHgaviYMMifgQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1570191090207?e=1795651200&v=beta&t=Fy4Tbn_sxh0FWImd7BbRMTgn0Jlj9UpCGyeM4rs1tLs)

Time Base for TB

To funnel RDII into a drainage system's node, it's essential for the node to pinpoint the UH group and the sewershed's area that funnels the RDII flow, all through its Inflows property 📌🔄.

Beyond Unit Hydrographs: Exploring Alternatives 🔄💡

If you're considering an alternative to unit hydrographs for charting RDII flow, you might want to delve into creating an external RDII interface file. This file is a treasure trove, brimming with RDII time series data 📂📉.

In instances where calibrated UHs are employed, unit hydrographs can stand in for SWMM’s primary rainfall-runoff procedure that leverages Subcatchment objects 🔄🌦️. Here, what SWMM dubs as RDII inflow to a node might actually signify overland runoff.

For Further Exploration 🧐🔍:

1.  **Inflows** 🌧️➡️🕳️

2.  **RDII Inflow Editor** 📝🔄

3.  **Unit Hydrograph Editor** 📈📊

Diving Deeper into the Unit Hydrograph Editor 📚🖥️

Every time a new Unit Hydrograph object is birthed or an existing one is chosen for tweaking, the Unit Hydrograph Editor springs into action. Its primary role? Dictating the shape parameters and the rain gauge for a cluster of triangular unit hydrographs 📐🌧️. These hydrographs stand as pillars to compute the rainfall-derived inflow/infiltration (RDII) flow at chosen nodes within the drainage framework. A UH group can boast up to 12 sets of these hydrographs, each tailored for a specific month 📅. Each set can encompass up to 3 distinct hydrographs, each catering to short-term, intermediate-term, and long-term responses 🕒🕕🕘. Additionally, they contain parameters that narrate any initial abstraction setbacks. The editor, as visualized below, is a canvas of data entry fields: \[Image not shown\] 🖼️🖱️.

![](https://media.licdn.com/dms/image/v2/C4E12AQECRh3zTSMpHg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1570191135670?e=1795651200&v=beta&t=q3mfOJdyohaoHqJ-_960qtUxbCZakdizU3L_7DoPEN0)

**Name of UH Group**

**Name of UH Group** 🏷️ Simply input the designated name for the UH Group.

**Rain Gage Used** 🌧️📊 Punch in or pick from the dropdown, the rain gage's name providing rainfall data to the group's unit hydrographs.

**Hydrographs For:** 📆 Choose a month from the dropdown for which you'll define hydrograph parameters. Opting for 'All Months' sets a default hydrograph for the entire year. Special hydrographs can be assigned to specific months marked with a (\*) - indicating their unique hydrograph assignments.

**Unit Hydrographs Parameters** 📈 Here, you'll detail the R-T-K shape parameters:

- Short-term response 🕒 (small T value)

- Medium-term response 🕕

- Long-term response 🕘 (largest T value) Parameters include:

- R: Rainfall volume entering the sewer system 🌧️➡️🕳️

- T: Time from rainfall start to UH peak ⏳

- K: UH's recession time to peak time ratio ⏳➗

**Initial Abstraction Depth** 📉 Tab over to this section to input parameters detailing how rainfall might be affected by any initial abstraction depth (like interception and depression storage) before processing through the month-specific unit hydrographs. Parameters include:

- Dmax: Max depth of initial abstraction 📏

- Drec: Rate of utilized initial abstraction's replenishment 🔄

- Do: Initial abstraction used at simulation start 📅

Remember, any empty parameter defaults to 0️⃣.

Right-clicking on the unit hydrograph and initial abstraction grids will reveal an Edit menu for cut/copy/paste functions.

> **RDII / Routing File Format  **

**RDII Interface** files and **Routing Interface** files have the same text format:

·the first line contains the keyword “SWMM5” (without the quotes)·a line of text that describes the file (can be blank)·the time step used for all inflow records (integer seconds)·the number of variables stored in the file, where the first variable must always be flow rate·the name and units of each variable (one per line), where flow rate is the first variable listed and is always named FLOW·the number of nodes with recorded inflow data·the name of each node (one per line)·a line of text that provides column headings for the data to follow (can be blank)·for each node at each time step, a line with:a)the name of the node,b)the date (year, month, and day separated by spaces),c)the time of day (hours, minutes, and seconds separated by spaces),d)the flow rate followed by the concentration of each quality constituent.

Time periods with no values at any node can be skipped. An excerpt from an RDII / Routing interface file is shown below.

> RDII Files  

The **RDII Interface File** contains a time series of rainfall-dependent infiltration/inflow flows for a specified set of drainage system nodes. This file can be generated from a previous SWMM run when Unit Hydrographs and nodal RDII inflow data have been defined for the project, or it can be created outside of SWMM using some other source of RDII data (e.g., through measurements or output from a different computer program). RDII files generated by SWMM are saved in a binary format. RDII files created outside of SWMM are text files with the same format used for a Routing Interface File, where Flow is the only variable contained in the file.

SWMM5Example File

300

1

FLOW CFS

2

N1

N2

Node Year Mon Day Hr Min Sec Flow

N1 2002 04 01 00 20 00 0.000000

N2 2002 04 01 00 20 00 0.002549

N1 2002 04 01 00 25 00 0.000000

N2 2002 04 01 00 25 00 0.002549

**RDII Inflow Page** 🌧️➡️ This RDII Inflow section of the Inflows Editor lets you specify the node's RDII. It houses:

- **Unit Hydrograph Group**: Choose the Unit Hydrograph group for the node. The group's hydrographs, combined with its rain gage, craft a RDII inflow time series over the simulation span.

- **Sewershed Area**: Note down the sewershed area contributing RDII to the node. Typically, this is a tiny segment of the subcatchment area providing surface runoff to the node.
