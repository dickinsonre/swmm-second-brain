---
title: "How to Use the USEPA SWMM-Climate Adjustment Tool with ICM InfoWorks, ICM SWMM, and Autodesk InfoDrainage"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-usepa-swmm-climate-adjustment-tool-icm-swmm-robert-dickinson-ghcpe
created: "2024-05-28 21:25"
published: "2024-05-29 12:25"
words: 989
export_sha256: a42b44532664f7254235851b093e34bb70feaacea32d585edfa8d5e0fe2f3cee
---
# How to Use the USEPA SWMM-Climate Adjustment Tool with ICM InfoWorks, ICM SWMM, and Autodesk InfoDrainage

![How to Use the EPA SWMM-Climate Adjustment Tool with ICM InfoWorks](https://media.licdn.com/mediaD4E12AQEkRkbBC1asXQ "How to Use the EPA SWMM-Climate Adjustment Tool with ICM InfoWorks")

A Climate Adjustment Tool from the US EPA for SWMM5 will estimate monthly changes in temperature, evaporation, and rainfall for the years 2035 and 2060 for various climate change scenarios. It is designed to be used with SWMM5, but can also be imported to ICM SWMM, used in InfoDrainage, and used in ICM InfoWorks networks that can import SWMM5 files. Here is how it can be used - the PDF file you download from the US EPA has very detailed information.

> **Background on the Climate Adjustment Tool**

The provided text is a comprehensive overview of SWMM-CAT (Storm Water Management Model—Climate Adjustment Tool) Version 1.1, an update from Version 1.0. This utility allows users to incorporate location-specific climate change adjustments into their SWMM project files, enabling them to assess the potential impacts of climate change on their stormwater management systems.

Key points and additional information:

1\. Data sources: SWMM-CAT utilizes downscaled results from the World Climate Research Programme (WCRP) Coupled Model Intercomparison Project Phase 5 (CMIP5) archive, which were generated and converted into changes for historical values by USEPA's CREAT 3.1 project.

2\. Adjustments: The tool can apply climate change adjustments every month to air temperature, evaporation rates, precipitation, and 24-hour design storms at different recurrence intervals.

3\. User inputs: To select a set of adjustments, users must input the latitude and longitude coordinates of their location or its 5-digit zip code. They must also choose between near-term or far-term projection periods and select a climate change scenario (Hot/Dry, Warm/Wet, or Central) and an extreme storm scenario (No Change, Stormy Future, or Less Stormy Future).

4\. Representative Concentration Pathway (RCP) 8.5: SWMM-CAT uses climate change scenarios produced by RCP 8.5, a high greenhouse gas emissions trajectory used in the CMIP5 project. This pathway represents a "business as usual" scenario in which greenhouse gas emissions continue to rise throughout the 21st century.

5\. Ensemble-informed selection method: CREAT 3.1 uses this method to define the three climate change scenarios (Hot/Dry, Warm/Wet, and Central) based on the average temperature and rainfall changes projected by the models.

6\. Future periods: Projections for each future scenario are available for two time periods: 2035 (averaged projections from years 2025-2045) and 2060 (averaged projections from years 2050-2070). These periods were chosen based on feedback from water utilities about future planning scenarios needed to support infrastructure or operational changes.

7\. Evaporation calculation: Using the Hargreaves method, the tool calculates evaporation based on projected temperatures.

8\. Saving adjustments: Users can save the selected adjustments to their existing SWMM project file by clicking the "Save Adjustments to SWMM" link and choosing which type of adjustments (monthly temperature, evaporation, rainfall, or 24-hour design storm) to save. The tool automatically handles unit conversions based on the detected unit system (US or SI) in the SWMM file.

By incorporating climate change projections into stormwater management planning, SWMM-CAT enables users to assess the resilience of their systems and make informed decisions about infrastructure improvements or operational changes needed to adapt to future climate conditions.

> **Where can I find the SWMM Hydrology Climate Adjustment Tool?**

On the US EPA SWMM5 download page, along with the source code, installs, and reference manuals for SWMM5.

[![](https://media.licdn.com/dms/image/v2/D4E12AQH0z_g0koly0Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183948923?e=1795651200&v=beta&t=Di1fkKWwTfhJg_-8o7Pqb74gM4i0x4MWgkdyiKxFP4g)](https://www.epa.gov/water-research/storm-water-management-model-swmm)

[https://www.epa.gov/water-research/storm-water-management-model-swmm](https://www.epa.gov/water-research/storm-water-management-model-swmm)

> **How does the climate tool work?**

![](https://media.licdn.com/dms/image/v2/D4E12AQEQsvFdJdRB_g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721192933545?e=1795651200&v=beta&t=pwsf1656a3txlrwbgw1Pgx5SXtry9zDwrFDAI6xUPBk)

**Use a zip code, a year of analysis and a climate change scenario.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGOzIp86BJVtg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721192647007?e=1795651200&v=beta&t=2ZGPgaTVoBR8np6O-vPGb0aGn7Qn5VYOWSjY44HcMIY)

The Percent increase for Temperature, Rainfall and Evaporation is saved to a SWMM5 file and can be imported to an ICM SWMM Network.

**Use a zip code, a year of analysis, and a climate change scenario. Save the adjustments to a SWMM5 file. This SWMM5 file can be imported into ICM (for both InfoWorks and SWMM Networks)**

![](https://media.licdn.com/dms/image/v2/D4E12AQFYQd3CMJvJsg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721193560915?e=1795651200&v=beta&t=cwK4A1m-uU40tOND7sIa7kLksKoHvIsUWHKjUbrcffQ)

**Save the adjustments to a SWMM5 file. This SWMM5 file can be imported into ICM (for both InfoWorks and SWMM Networks)**

![](https://media.licdn.com/dms/image/v2/D4E12AQH42VymvtPC9Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195189459?e=1795651200&v=beta&t=doo040ztqD5ckn4CTYZzcMhCh-rJWIY64RhfIYBEXe0)

Imported climate data from SWMM5 to ICM SWMM.

> **You can run the tool from SWMM5**

![](https://media.licdn.com/dms/image/v2/D4E12AQGA9XGqzET6lg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721186785952?e=1795651200&v=beta&t=Iv406pi8SVZqHh3znlymBvgAaoAnVNJF4JxvCcCt85k)

**You can run the tool from SWMM5.**

> The Percent Increase for a 24 hour storm can be saved to SWMM5 and then copied and pasted to ICM or InfoDrainage

![](https://media.licdn.com/dms/image/v2/D4E12AQFkRgpOZOmUKA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721184804621?e=1795651200&v=beta&t=j_DAwphiwn32XiXUAp2IwgTCv6-E6MG8F0ftsBAPg6Q)

The Percent Increase for a 24 hour storm can be saved to SWMM5 and then copied and pasted to ICM or InfoDrainage

> **You can also use the SWMM Climate Adjustment tool with Autodesk InfoDrainage by using the Percent Increase Dialog for Rainfall**

![](https://media.licdn.com/dms/image/v2/D4E12AQG1_vuvtmKueQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721196225633?e=1795651200&v=beta&t=M89C45iVdxAKbCxuRL3hhrxD30dNR5ZlU1MLFGD5ou4)

**You can also use the SWMM Climate Adjustment tool with Autodesk InfoDrainage.**

==================================================
