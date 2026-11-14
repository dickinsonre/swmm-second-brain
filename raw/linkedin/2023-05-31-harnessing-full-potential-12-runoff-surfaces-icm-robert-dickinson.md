---
title: "Harnessing the Full Potential of the 12 Runoff Surfaces in ICM InfoWorks for SUDS/LID Modeling"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/harnessing-full-potential-12-runoff-surfaces-icm-robert-dickinson
created: "2023-05-27 19:11"
published: "2023-05-31 14:01"
words: 1734
export_sha256: 0d7ca88dbb7fb2b6545af93a940208201fd2fc1eeda8f2dbc8fba65666f0ffe9
---
# Harnessing the Full Potential of the 12 Runoff Surfaces in ICM InfoWorks for SUDS/LID Modeling

![Runoff Volume Type or Infiltration options in an InfoWorks Network in ICM](https://media.licdn.com/mediaD4E12AQG6ZW5u7HAIfg "Runoff Volume Type or Infiltration options in an InfoWorks Network in ICM")

> Harnessing the Full Potential of the 12 Runoff Surfaces in ICM InfoWorks for SUDS/LID Modeling

While I've previously discussed the capabilities of ICM SWMM Networks, it's important to note that the capabilities of ICM InfoWorks Networks are perhaps even more well-known and widely used. In particular, the ability to model up to 12 runoff surfaces in InfoWorks is a significant improvement over the limit of 3 surfaces in SWMM5.

This additional flexibility allows for more nuanced and accurate modeling of complex hydrological processes. For example, in an urban setting, different surfaces such as roads, roofs, and parks might have very different runoff behaviors. With the ability to model up to 12 different surfaces, InfoWorks allows you to capture these differences in a way that SWMM5 simply can't match.

Additionally, the way that InfoWorks handles grids for Subcatchments offers an interactive and intuitive way to manage complex catchment areas. This makes it easier to accurately model the interplay of different surfaces and their impacts on runoff and infiltration.

Going a step further, I plan to leverage the power of ChatGPT and Ruby to create new scenarios for the various infiltration options available in InfoWorks. This will allow for even more precise and tailored-modeling, enabling us to predict and manage water flow in a range of different conditions.

Finally, as a special bonus, I will also discuss how to incorporate SWMM5's Low Impact Development (LID) or Sustainable Drainage Systems (SuDs) into the runoff surfaces in Subcatchments within InfoWorks. These systems, which include things like green roofs, permeable pavements, and rain gardens, can significantly reduce runoff and promote infiltration. By incorporating these into our InfoWorks model, we can better predict and manage the impacts of these sustainable practices on our water systems.

InfoWorks ICM provides an advanced level of flexibility and sophistication in modeling runoff from different surfaces, significantly enhancing its capabilities compared to SWMM5. Within ICM InfoWorks, users can define up to **12 different runoff surfaces**, each of which can have unique characteristics. These characteristics can include **19 different types of runoff volumes**, three types of surface types, and **16 types of routing models**. This abundance of options allows for a high level of specificity and complexity in the simulation of runoff, making the model highly adaptable to various real-world scenarios.

Stay tuned for an exciting exploration of the advanced hydrological modeling capabilities of ICM InfoWorks.

  

> There are 12 Runoff Surfaces on a InfoWorks Subcathment with 19 Runoff Volume and 16 Routing Model Options.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEtVYC6vCHAAw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685540090078?e=1795651200&v=beta&t=NqyKGF_SKZiEMXQM4czqq-YQVyvg4Bsc8ozwC1pbekY)

There are 12 Runoff Surfaces on an InfoWorks Subcathment with 19 Runoff Volume and 16 Routing Model Options

> **There are 8 types of SUDS/LID on a Subcatchment surface.**

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHlltggWq7hDw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685541011980?e=1795651200&v=beta&t=_ObqzrxxGuSI7Xr2VUFX9BCrClZjLcnQWZyGqaq_-FE)

An image from the online ICM help file for Rain Gardens and a list of the 8 types of SUDS/LID on a Subcatchment surface.

  

> How do you interpret the LID Control Table?

LID Control Table - The table provides a summary of the Low Impact Development (LID) controls implemented in different subcatchments. The main columns in the table are:

- **Subcatchment**: This column shows the ID or name of the subcatchment in which the LID control is implemented.
- **LID Control**: This column indicates the type of LID control implemented in the given subcatchment. In this case, "RG" is the type of LID control used.
- **No. of Units**: This column represents the number of LID units implemented in the given subcatchment.
- **Unit Area**: This column shows the area (presumably in square meters or square feet) covered by each unit of the LID control.
- **Unit Width**: This column indicates the width (presumably in meters or feet) of each LID unit.
- **% Area Covered**: This column displays the percentage of the total subcatchment area covered by the LID controls.
- **% Imperv Treated**: This column represents the percentage of impervious (non-absorbent) areas treated by the LID controls.
- **% Perv Treated**: This column indicates the percentage of pervious (absorbent) area treated by the LID controls. In our example, 10 percent of the pervious area is being treated.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEBr5m5GyN85w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685532366092?e=1795651200&v=beta&t=bgvPz6PAuJmiGI3YLbQeeBCI1LNAK9VjRd_ZTofPMaY)

A LID control has both vertical and horizontal parameters but in addition, it has two pathways for runoff - flow from imperious and flow from pervious area.

> Here's a summary of the LID Performance table.

The table provides an overview of the performance of Low Impact Development (LID) controls implemented in different subcatchments. The main columns in the table are:

- **Subcatchment**: This column shows the ID or name of the subcatchment in which the LID control is implemented.
- **LID Control**: This column indicates the type of LID control implemented in the given subcatchment. In this case, "RG" is the type of LID control used.
- **Total Inflow**: This column represents the total volume of water (in millimeters) entering the LID unit.
- **Evap Loss**: This column shows the volume of water lost due to evaporation.
- **Infil Loss**: This column indicates the volume of water lost due to infiltration into the ground.
- **Surface Outflow**: This column displays the volume of water that overflows from the surface of the LID unit.
- **Drain Outflow**: This column represents the volume of water that drains out from the LID unit.
- **Initial Storage**: This column shows the initial volume of water stored in the LID unit.
- **Final Storage**: This column indicates the final volume of water stored in the LID unit after the simulation.
- **Continuity Error**: This column represents the difference between the total inflow and the sum of all losses, outflows, and final storage, expressed as a percentage. It's a measure of the accuracy of the simulation.

For example, **in Subcatchment 1, the "RG" LID control had a total inflow of 1139.20mm, with 34.79mm lost to infiltration, 762.91mm outflowing from the surface, and final storage of 353.67mm. The continuity error was -0.01%, indicating the high accuracy of the simulation**.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEsunyse2SerQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685379503611?e=1795651200&v=beta&t=T841v6TZZXhY0GaDdJtXdgSSJ0bf37VwZxFghJmDY6o)

Using the SWMM5 SuDS/LID report file you can see what the LID captures and how the LID operates.

> Low Impact Development (LID) or Sustainable Drainage Systems (SuDS) Output Graphs

When using Low Impact Development (LID) or Sustainable Drainage Systems (SuDS) models, the output graphs provide crucial insights into how these systems are managing rainfall and runoff. These can be broken down into three main categories:

1.  **Inflow to the LID/SuDS**: This is the amount of rainfall or runoff that is directed into the LID or SuDS. This is the initial input that the system has to manage. It's crucial to monitor this inflow because it impacts how effectively the system can mitigate the effects of stormwater.
2.  **Outflow from the LID/SuDS**: This is the water that has passed through the system and is released, typically into the ground or a water body. This water has been slowed down, cleaned, and managed by the LID or SuDS. Tracking this outflow helps measure how effectively the system is reducing stormwater runoff and improving water quality.
3.  **Surface Overflow**: This is the water that the LID or SuDS cannot manage and ends up flowing over the surface of the system. This could be due to the system being overwhelmed by the volume of inflow or due to the system not being designed to handle the particular type of storm event. Monitoring surface overflow is critical because it can indicate the system's limitations and potential areas for improvement.

Together, these elements provide a comprehensive view of how the LID or SuDS is performing. By monitoring these metrics, users can understand the system's effectiveness and make necessary adjustments or improvements. These graphs can help in decision-making for future designs and upgrades, ensuring that the LID or SuDS system is optimized for its intended purpose. It also aids in understanding the balance between water inflow and outflow, which is vital for managing water resources effectively and sustainably.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEBaTpQHBSryw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1685379473671?e=1795651200&v=beta&t=9p6vHVhDDhGH99KPWfBwgSgpeoi_f0tKjmtOULLc_B4)

When using Low Impact Development (LID) or Sustainable Drainage Systems (SuDS) models, the output graphs provide crucial insights into how these systems are managing rainfall and runoff.

> ICM InfoWorks is potentially 3648 times more flexible than SWMM5 for the modeling of SUDS/LID for the following reasons 

InfoWorks ICM provides an advanced level of flexibility and sophistication in modeling runoff from different surfaces, significantly enhancing its capabilities compared to SWMM5. Within ICM InfoWorks, users can define up to 12 different runoff surfaces, each of which can have unique characteristics. These characteristics can include 19 different types of runoff volumes, three types of surface types, and 16 types of routing models. This abundance of options allows for a high level of specificity and complexity in the simulation of runoff, making the model highly adaptable to various real-world scenarios.

Moreover, in InfoWorks ICM, Sustainable Urban Drainage Systems (SuDS) or Low Impact Development (LID) practices can interact with all of these combinations at the subcatchment level. This provides a more comprehensive and nuanced understanding of how these practices can affect runoff in different settings and conditions, which is critical for effective stormwater management planning and design.

**Contrast this with SWMM5, which has only two surface types, five infiltration types, and one routing model.** The increased complexity of InfoWorks ICM over SWMM5 enables more detailed and accurate modeling of runoff processes, providing valuable insights for water resources management. It's worth noting, though, that this increased complexity may require more data and computational resources, as well as a deeper understanding of the model's configuration and operation.
