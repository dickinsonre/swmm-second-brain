---
title: "SWMM5 Groundwater vs ICM InfoWorks Ground Infiltration Model (GIM) Parameters"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/swmm5-groundwater-vs-icm-infoworks-ground-model-gim-robert-dickinson-8v5le
created: "2024-03-21 22:47"
published: "2024-03-24 18:54"
words: 1861
export_sha256: a063d133342dfe76f27b1d9bb0f1a2c6043119c4d8d26ae6d4d5433f0e14e116
---
# SWMM5 Groundwater vs ICM InfoWorks Ground Infiltration Model (GIM) Parameters

![SWMM5 Groundwater vs ICM InfoWorks Ground Infiltration Model (GIM) Parameters](https://media.licdn.com/mediaD4E12AQFXO3EuhnqlqQ "SWMM5 Groundwater vs ICM InfoWorks Ground Infiltration Model (GIM) Parameters")

Normally, the import of SWMM5 data to ICM InfoWorks is excellent but sometimes, in case of very different model parameters, there is no import conversion. One example is the import of Groundwater data from SWMM5 or ICM SWMM to ICM InfoWorks. The reason for this is explained in this article.

The Storm Water Management Model (SWMM5) and InfoWorks ICM's Ground Infiltration Model (GIM) offer distinct approaches to modeling groundwater dynamics, reflecting their unique focuses and capabilities. SWMM5 employs a comprehensive dual-zone method that distinguishes between unsaturated and saturated zones, allowing for detailed simulations of percolation, lateral flow, and interactions with the surface water system. **(See Section 1 and Section 2)** It integrates groundwater flow with surface runoff calculations, evapotranspiration, and the conveyance system's hydraulic conditions.

Conversely, ICM's GIM emphasizes direct infiltration processes, percolation thresholds, and linear relationships between soil and ground stores, focusing more on the infiltration dynamics and the immediate response of the subsurface environment to precipitation events **(see Section 3).** While SWMM5 provides a nuanced view of subsurface hydrology, including soil moisture dynamics and groundwater-surface water interactions, GIM prioritizes the simplicity and efficiency of modeling the immediate impacts of rainfall on groundwater levels, making each model suited to different aspects of water cycle simulation and analysis. We list the common parameters **(not many in Section 5 and the different parameters in Section 6).**

> **1/ SWMM5 Groundwater Parameters**

The Groundwater Flow Editor dialog is invoked when the Groundwater property of a Subcatchment is being edited. It is used to link a subcatchment to both a parent aquifer and to a node of the conveyance system that exchanges groundwater with the subcatchment. The editor also specifies coefficients that determine the rate of lateral groundwater flow between the aquifer and the node. These coefficients (A1, A2, B1, B2, and A3) appear in the following equation that computes lateral groundwater flow as a function of groundwater and surface water levels. 

![](https://media.licdn.com/dms/image/v2/D4E12AQERq8pWgRQOdA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711295866175?e=1795651200&v=beta&t=HNtdRbBU42RGOQxL5OYGs_QtlyNCCg4857ky-5mx_bY)

SWMM5 Groundwater Parameters

> **2/ SWMM5 Aquifer Parameters**

The Aquifer Editor 🌊📝 is invoked whenever a new Aquifer object is created or an existing Aquifer object is selected for editing. It contains the following data fields.

![](https://media.licdn.com/dms/image/v2/D4E12AQFPeGA_F6CICw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711296283421?e=1795651200&v=beta&t=CBN3pSqK-cULD9XXxwgAttfffywajb1hxBi_fLm3QZk)

SWMM5 Aquifer Parameters

**How does the SWMM GW model work?**

In SWMM5, aquifers and groundwater dynamics are modeled through a sophisticated process that integrates with the runoff calculations for each subcatchment possessing a groundwater component. This integration occurs immediately after infiltration over the subcatchment's pervious areas is computed, emphasizing the interplay between surface and subsurface hydrological processes .

The modeling begins with the known variables at each runoff time step, which include the infiltration rate from the pervious surface, the potential evapotranspiration rate, and the depth of available moisture. This is complemented by data from the conveyance system, like the inflow and water surface elevation at the node receiving groundwater flow. These inputs, along with soil properties such as porosity, field capacity, and wilting point moisture content, feed into the groundwater computations .

SWMM5's computational scheme for groundwater involves several key steps, starting with determining the upper zone's maximum percolation rate and making an initial estimate of the upper zone percolation rate. This is then constrained by the maximum limit on the infiltration rate, ensuring that the model's assumptions about soil and water interactions remain realistic. The calculations adjust for evaporation consumed by ponded surface water and iterate towards a consistent representation of subsurface water dynamics .

Groundwater discharge within SWMM5 is addressed through a lateral flow model, dependent on soil moisture content and the hydraulic properties of the soil, reflecting how groundwater moves to the conveyance system. This model accommodates various flow conditions and integrates them into the broader water cycle simulation within a given subcatchment .

By employing a dual-zone approach—distinguishing between the unsaturated upper zone and the saturated lower zone—SWMM5 captures the complexity of groundwater behavior. This includes evapotranspiration effects, percolation from upper to lower zones, and lateral groundwater seepage. The modeling framework ensures a dynamic response to changing hydrological conditions, accurately reflecting the nuanced relationship between aquifers, groundwater, and the surface water system .

> **3/ ICM InfoWorks GIM Model Data**

**How does the ICM InfoWorks Groundwater Infiltration model work?** The soil store acts as an intermediary reservoir that captures inflow primarily from the subcatchment's pervious land cover through soil infiltration. It then loses water through evaporation and percolation into a deeper ground store, with all its inflow and outflow processes being linearly related to the soil store's water level. The ground store, positioned below the soil store, receives its inflow from the soil store's percolation and then loses water through baseflow and further infiltration, again with linearity in its flow processes based on the ground store's water level. The receiving node, crucial for the model's dynamics, demonstrates that soil store infiltration directly correlates with the percolation rate, while ground store infiltration depends on the differential head between the ground store level and the node's water level, underscoring a system where water movement through both stores and their interactions with the receiving node are governed by linear relationships.

- **Ground Infiltration ID** 🆔: Unique identifier for the ground infiltration record, linking it to specific subcatchments.

- **Soil Depth** 📏: Estimated depth of soil layer.

- **Percolation Coefficient** 🕒: Time coefficient for water percolation, with calibration recommendations.

- **Baseflow Coefficient** 🚰⏳: Time coefficient for baseflow, indicating groundwater movement rates.

- **Infiltration Coefficient** 💧⏳: Time coefficient for soil infiltration, guiding water absorption speed.

- **Percolation Threshold** 💧🔝: Soil saturation level that initiates downward water percolation.

- **Percolation Percentage Infiltrating** 💧➗: Portion of percolated water entering the drainage network.

- **Soil Porosity** 🧽: Indicates soil's void space, affecting water storage capacity.

- **Ground Porosity** 🌍🧽: Reflects the ground's void space below the soil layer.

- **Baseflow Threshold Level** 🌊🔍: Groundwater level triggering secondary infiltration.

- **Baseflow Threshold Type** 🔄: Specifies if the baseflow level is an absolute or relative measurement.

- **Infiltration Threshold Level** 💧🔍: Level at which groundwater begins to infiltrate the drainage system.

- **Infiltration Threshold Type** 🔢: Determines if the infiltration level is absolute or relative.

- **Evapotranspiration Type** 🌱☀️: Defines if evapotranspiration varies (linear) or remains constant with depth.

- **Evapotranspiration Depth** 🌱📏: Depth beyond which evapotranspiration ceases.

- **Monthly Evapotranspiration Factors** 🗓️💦: Adjusts evapotranspiration rates for each month, ensuring accurate seasonal variations.

> **4/ Mel Meng's GIM Blog for InfoWorks ICM**

\[embedded item\]

> **5/ Common SWMM5 and ICM InfoWorks Groundwater-Related Parameters**

To compare the Ground Infiltration Model (GIM) data with SWMM5's Aquifer and Groundwater data, let's identify similar fields across these datasets. This will help in understanding how these components of SWMM5 interact and how they relate to the broader aspects of modeling infiltration, aquifer characteristics, and groundwater flow. Here’s a table summarizing similarities

![](https://media.licdn.com/dms/image/v2/D4E12AQHqzpBuJpZhBA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711296990295?e=1795651200&v=beta&t=Htkc7u6wBjk_4-WSzOkncfyrJmZMf9U7hONG5mHVjIM)

Nine common parameters between SWMM5 and ICM InfoWorks

> **6/ SWMM5 GW and ICM Infoworks GIM Differences**

Focusing on the non-common parameters among the Ground Infiltration Model (GIM) data and SWMM5's Aquifer and Groundwater data, we can highlight unique aspects of each model that contribute to their specific simulation capabilities. Here’s a summary:

### Unique to GIM Data:

- **Percolation Percentage Infiltrating**: Specifies the fraction of percolated water that directly infiltrates into the drainage network, a unique aspect of how GIM handles percolation.

- **Baseflow Threshold Level** and **Type**: These parameters dictate the conditions under which secondary infiltration begins, specific to how GIM models groundwater interactions.

- **Infiltration Threshold Level** and **Type**: Set the criteria for when groundwater begins to infiltrate the drainage system, highlighting GIM's detailed groundwater modeling.

- **Monthly Evapotranspiration Factors**: Adjusts evapotranspiration rates month by month, offering a nuanced approach to seasonal changes in GIM.

### Unique to SWMM5 Aquifer Data:

- **Depth**: While both GIM and Aquifer data consider soil depth, in SWMM5, this parameter specifically contributes to the aquifer model's storage and infiltration processes.

- **Hydraulic Conductivity**: Related to the percolation and baseflow coefficients in GIM, but in SWMM5, it directly influences the rate at which water moves through the aquifer.

- **Field Capacity**: A parameter that dictates the water content of the soil after it has been saturated and allowed to drain, crucial for modeling soil-water interactions in SWMM5 that's not explicitly mentioned in GIM.

- **Wilting Point**: Defines the minimum soil moisture below which plants begin to wilt, critical for vegetation-based calculations in SWMM5, absent in GIM.

### Unique to SWMM5 Groundwater Data:

- **Deep Conductivity**: Reflects the movement of groundwater in deeper soil layers, a specificity of SWMM5's groundwater model not found in GIM.

- **Surface Conductivity**: Indicates how easily water moves at the surface level, emphasizing SWMM5's detailed approach to different soil layer interactions.

### General Observations:

- The GIM data encompasses a broader scope of infiltration dynamics, including specific coefficients and thresholds for percolation and baseflow, which are not distinctly outlined in SWMM5.

- SWMM5 Aquifer and Groundwater data introduce detailed soil and water interaction parameters such as field capacity and wilting point, alongside conductivity measures for different soil layers, offering a nuanced view of subsurface hydrological processes not covered by GIM.

These unique parameters underscore the different focuses and modeling capabilities of the Ground Infiltration Model compared to SWMM5’s Aquifer and Groundwater components, with GIM emphasizing detailed percolation dynamics and SWMM5 providing a comprehensive model of soil-water interactions across various layers.

------------------------------------------------------------------------

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
