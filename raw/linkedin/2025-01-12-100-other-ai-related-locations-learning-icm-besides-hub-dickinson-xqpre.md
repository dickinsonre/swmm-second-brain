---
title: "100 Other AI-Related Locations for Learning ICM besides the ICM Technical Hub"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/100-other-ai-related-locations-learning-icm-besides-hub-dickinson-xqpre
created: "2025-01-11 20:39"
published: "2025-01-12 00:41"
words: 3260
export_sha256: aaf0034f47f4dc892012e618c5d398a66f82894aad4e595d7a69506b07d4fc26
---
# 100 Other AI-Related Locations for Learning ICM besides the ICM Technical Hub

![100 Other AI-Related Locations for Learning ICM besides the ICM Technical Hub](https://media.licdn.com/mediaD4E12AQF4w7VINbqL6A "100 Other AI-Related Locations for Learning ICM besides the ICM Technical Hub")

A comprehensive guide to getting started with InfoWorks ICM. Here is the technical hub [https://boards.autodesk.com/icm](https://boards.autodesk.com/icm)

\## Initial Setup and Interface

InfoWorks ICM is installed as two main components: the user interface for creating and managing data, and the Agent Manager Service for handling simulations\[23\]. The software requires proper licensing, with two versions available—Standard and Ultimate\[23\].

**Database Creation**

\- Create a master database using either standalone (single user) or workgroup (team collaboration) option

\- Set up customized data flags to track changes and data quality

\- Configure the coordinate system for accurate spatial representation\[3\]

**Interface Components**

\- GeoPlan view for visual model building and analysis

\- Model Group window for organizing project data

\- Properties window for editing object parameters

\- Job Control window for managing simulations\[1\]

\## Data Management and Import

**Project Organization**

\- Use model groups to store modeling and simulation data

\- Create networks within model groups for specific project components

\- Maintain proper version control through commit history\[2\]

**Data Import Methods**

\- Use Open Data Import Centre (ODIC) for importing from various sources:

\- GIS files

\- CSV files

\- Existing InfoWorks models

\- Access databases\[80\]

**Ground Model Integration**

\- Import ground model data using ASCII grid files

\- Set appropriate elevation units and coordinate systems

\- Configure ground model display themes for better visualization\[1\]

\## Network Building

**1D Network Creation**

\- Create nodes (manholes, outfalls) and links (conduits, channels)

\- Define network properties including invert levels and dimensions

\- Add subcatchments for rainfall-runoff modeling\[39\]

**2D Mesh Generation**

\- Create 2D zones to define mesh areas

\- Set appropriate mesh parameters:

\- Maximum element size (typically 100m²)

\- Minimum element size (typically 25m²)

\- Include buildings and structures as voids

\- Generate and validate mesh before simulation\[5\]

\## Model Validation and Calibration

**Validation Process**

\- Run network validation to check for errors and inconsistencies

\- Address validation messages in three categories:

\- Errors (must be fixed)

\- Warnings (should be reviewed)

\- Information messages (for awareness)\[84\]

**Calibration Approach**

\- Use observed data to adjust model parameters

\- Focus on key parameters:

\- Roughness coefficients

\- Infiltration parameters

\- Subcatchment characteristics\[6\]

\## Running Simulations

**Simulation Setup**

\- Create new runs in the Run View

\- Configure simulation parameters:

\- Time steps

\- Initial conditions

\- Output controls\[7\]

**Common Pitfalls to Avoid**

\- Ensure model purpose is clearly defined

\- Invest sufficient time in data quality

\- Maintain regular calibration and verification

\- Keep models up-to-date with network changes\[8\]

\## Results Analysis

**Viewing Results**

\- Use themes to display simulation results

\- Create long sections for detailed analysis

\- Generate statistical reports for key parameters\[59\]

**Results Interpretation**

\- Review flood extents using flood themes

\- Analyze flow patterns and hydraulic performance

\- Identify critical areas requiring attention\[60\]

\## Collaboration and Reporting

**Team Collaboration**

\- Use workgroup databases for multi-user access

\- Implement proper version control

\- Share models using transportable databases (.icmt files)\[81\]

**Reporting Options**

\- Generate standard PRN reports

\- Create custom statistical reports

\- Export results for external analysis\[70\]

\## Additional Resources

**Learning Materials**

\- Access the InfoWorks ICM Quick Start Guide

\- Watch tutorial videos on the Autodesk Water YouTube channel

\- Review the One Water Blog for tips and updates\[74\]

**Best Practices**

\- Follow a structured approach to model building

\- Regularly validate and calibrate models

\- Document changes and decisions

\- Keep up with software updates and new features\[65\]

Remember to regularly commit changes to your database and maintain proper documentation of model modifications and assumptions\[8\].

Citations:

\[1\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/5h7rFbmSC6P5i4vjMZGfZd](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/5h7rFbmSC6P5i4vjMZGfZd)

\[2\] [https://uscad.com/three-features-that-make-infoworks-icm-unique/](https://uscad.com/three-features-that-make-infoworks-icm-unique/)

\[3\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/6HZBqvAdEzq75vdE3kQJjW](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/6HZBqvAdEzq75vdE3kQJjW)

\[4\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/24Qex34MmboD4jebzClsX0](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/24Qex34MmboD4jebzClsX0)

\[5\] [https://www.autodesk.com/learn/ondemand/curated/introduction-to-2d-modelling-in-infoworks-icm/VQFsMett47VcE265DROgg](https://www.autodesk.com/learn/ondemand/curated/introduction-to-2d-modelling-in-infoworks-icm/VQFsMett47VcE265DROgg)

\[6\] [https://swmm5.org/2017/11/25/calibration-methodology-in-infoswmm-and-infoswmm-sa/](https://swmm5.org/2017/11/25/calibration-methodology-in-infoswmm-and-infoswmm-sa/)

\[7\] [https://www.autodesk.com/learn/ondemand/curated/1d-simulations-in-infoworks-icm/2eFTY63ifWmTzE2M2sAn8p](https://www.autodesk.com/learn/ondemand/curated/1d-simulations-in-infoworks-icm/2eFTY63ifWmTzE2M2sAn8p)

\[8\] [https://www.autodesk.com/blogs/water/2021/07/06/9-mistakes-we-often-see-in-hydraulic-modeling/](https://www.autodesk.com/blogs/water/2021/07/06/9-mistakes-we-often-see-in-hydraulic-modeling/)

\[9\] [https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/4LpZOi1WV2KgWmtWMy0XCX](https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/4LpZOi1WV2KgWmtWMy0XCX)

\[10\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/51Dw326olNbzMFHuywUYfL](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/51Dw326olNbzMFHuywUYfL)

\[11\] [https://www.autodesk.com/blogs/water/2023/10/13/new-autodesk-learning-courses-for-infowater-pro-infoworks-ws-pro-infodrainage-and-infoworks-icm/](https://www.autodesk.com/blogs/water/2023/10/13/new-autodesk-learning-courses-for-infowater-pro-infoworks-ws-pro-infodrainage-and-infoworks-icm/)

\[12\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide)

\[13\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/3WABzelcuO8NKBp19EyxrS](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/3WABzelcuO8NKBp19EyxrS)

\[14\] [https://www.autodesk.com/learn/ondemand/tutorial/creating-an-integrated-model](https://www.autodesk.com/learn/ondemand/tutorial/creating-an-integrated-model)

\[15\] [https://www.autodesk.com/products/infoworks-icm/overview](https://www.autodesk.com/products/infoworks-icm/overview)

\[16\] [https://boards.autodesk.com/icm/items/installation-instructions](https://boards.autodesk.com/icm/items/installation-instructions)

\[17\] [https://www.autodesk.com/learn/ondemand/course/infoworks-icm/module/1bgt1EXvnC4hOkaUMTeV6E](https://www.autodesk.com/learn/ondemand/course/infoworks-icm/module/1bgt1EXvnC4hOkaUMTeV6E)

\[18\] [https://help.innovyze.com/space/infoworksicm/18219149](https://help.innovyze.com/space/infoworksicm/18219149)

\[19\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/24Qex34MmboD4jebzClsX0](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/24Qex34MmboD4jebzClsX0)

\[20\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-88226121-E0AF-4976-956C-81B3407FBBC1](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-88226121-E0AF-4976-956C-81B3407FBBC1)

\[21\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/40IdwWNvSRS8pmxxoOimBH](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/40IdwWNvSRS8pmxxoOimBH)

\[22\] [https://www.autodesk.com/learn/ondemand/curated/administrators-implementation-guide-for-infoworks-icm](https://www.autodesk.com/learn/ondemand/curated/administrators-implementation-guide-for-infoworks-icm)

\[23\] [https://www.autodesk.com/learn/ondemand/tutorial/understanding-infoworks-icm-licensing](https://www.autodesk.com/learn/ondemand/tutorial/understanding-infoworks-icm-licensing)

\[24\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm)

\[25\] [https://www.autodesk.com/learn/ondemand/course/infoworks-icm](https://www.autodesk.com/learn/ondemand/course/infoworks-icm)

\[26\] [https://boards.autodesk.com/icm](https://boards.autodesk.com/icm)

\[27\] [https://www.youtube.com/watch?v=PZ7ggNoqvQQ](https://www.youtube.com/watch?v=PZ7ggNoqvQQ)

\[28\] [https://boards.autodesk.com/icm/items/infoworks-icm-workgroup-best-practices](https://boards.autodesk.com/icm/items/infoworks-icm-workgroup-best-practices)

\[29\] [https://www.autodesk.com/learn/ondemand/curated/configuring-the-infoworks-icm-database/3tH7Eym41JcO6M7gkHqyPh](https://www.autodesk.com/learn/ondemand/curated/configuring-the-infoworks-icm-database/3tH7Eym41JcO6M7gkHqyPh)

\[30\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/4X9eCQfpdVdugvGW7OLEb](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/4X9eCQfpdVdugvGW7OLEb)

\[31\] [https://www.autodesk.com/learn/catalog/infoworks%20icm/product/InfoWorks%20ICM](https://www.autodesk.com/learn/catalog/infoworks%20icm/product/InfoWorks%20ICM)

\[32\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide)

\[33\] [https://www.youtube.com/watch?v=FazZPy9wshY](https://www.youtube.com/watch?v=FazZPy9wshY)

\[34\] [https://www.autodesk.com/learn/ondemand/course/infoworks-icm/unit/3aAcq9HIZAnpHyNh3KKmHi](https://www.autodesk.com/learn/ondemand/course/infoworks-icm/unit/3aAcq9HIZAnpHyNh3KKmHi)

\[35\] [https://www.youtube.com/watch?v=olBOC1slcjc](https://www.youtube.com/watch?v=olBOC1slcjc)

\[36\] [https://www.autodesk.com/learn/ondemand/curated/modelling-2d-objects-in-infoworks-icm/DTivbwA9JAOzi9e4rNkRb](https://www.autodesk.com/learn/ondemand/curated/modelling-2d-objects-in-infoworks-icm/DTivbwA9JAOzi9e4rNkRb)

\[37\] [https://www.autodesk.com/learn/ondemand/curated/1d-simulations-in-infoworks-icm](https://www.autodesk.com/learn/ondemand/curated/1d-simulations-in-infoworks-icm)

\[38\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/7mYd0iaeNzfPAvxSUHKQPy](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/7mYd0iaeNzfPAvxSUHKQPy)

\[39\] [https://www.autodesk.com/learn/ondemand/course/infoworks-icm/module/7He9TY9wK4oI30u8pNGtg2](https://www.autodesk.com/learn/ondemand/course/infoworks-icm/module/7He9TY9wK4oI30u8pNGtg2)

\[40\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-2FCDC59C-8636-46C1-A65C-FCB282B393E1](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-2FCDC59C-8636-46C1-A65C-FCB282B393E1)

\[41\] [https://www.autodesk.com/learn/ondemand/curated/building-a-1d-urban-drainage-network/1hmmVMuwMGLx8TaPIUqwom](https://www.autodesk.com/learn/ondemand/curated/building-a-1d-urban-drainage-network/1hmmVMuwMGLx8TaPIUqwom)

\[42\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-24EB7F2A-778D-4815-8F54-4DE299B8D532](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-24EB7F2A-778D-4815-8F54-4DE299B8D532)

\[43\] [https://www.youtube.com/watch?v=b8jiteZBdIQ](https://www.youtube.com/watch?v=b8jiteZBdIQ)

\[44\] [https://www.autodesk.com/learn/ondemand/curated/building-a-river-reach-in-infoworks-icm/3C2qVf7Pl5iNgc3V0cigJG](https://www.autodesk.com/learn/ondemand/curated/building-a-river-reach-in-infoworks-icm/3C2qVf7Pl5iNgc3V0cigJG)

\[45\] [https://www.autodesk.com/blogs/water/2023/01/20/infoworks-icm-basics-video-tutorial-series/](https://www.autodesk.com/blogs/water/2023/01/20/infoworks-icm-basics-video-tutorial-series/)

\[46\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-46D6352A-0A04-4459-B6BC-6D7A3A137516](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-46D6352A-0A04-4459-B6BC-6D7A3A137516)

\[47\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-29E8B701-3699-40B3-A4BD-C64CA9EFA578](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-29E8B701-3699-40B3-A4BD-C64CA9EFA578)

\[48\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A605707E-8B71-40C4-8A6D-9145F2E45AC4](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A605707E-8B71-40C4-8A6D-9145F2E45AC4)

\[49\] [https://app.gnosis-mfe-stg.autodesk.com/learn/ondemand/tutorial/about-model-calibration-and-criteria](https://app.gnosis-mfe-stg.autodesk.com/learn/ondemand/tutorial/about-model-calibration-and-criteria)

\[50\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-68D4B29F-0EB0-477B-B2DC-DECD90D4E6AE](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-68D4B29F-0EB0-477B-B2DC-DECD90D4E6AE)

\[51\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-47075E48-477A-4ABE-8325-430A495F43A2](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-47075E48-477A-4ABE-8325-430A495F43A2)

\[52\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-9C7CB8B0-9581-4257-BD3A-0B70895B5CC5](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-9C7CB8B0-9581-4257-BD3A-0B70895B5CC5)

\[53\] [https://www.autodesk.com/blogs/water/2018/01/09/troubleshooting-hydraulic-models-in-infoworks-icm/](https://www.autodesk.com/blogs/water/2018/01/09/troubleshooting-hydraulic-models-in-infoworks-icm/)

\[54\] [https://www.autodesk.com/blogs/water/2022/10/14/5-ways-we-made-infoworks-icm-more-efficient/](https://www.autodesk.com/blogs/water/2022/10/14/5-ways-we-made-infoworks-icm-more-efficient/)

\[55\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A5DC6F50-05DD-41AF-A96A-195B37D6B44A](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A5DC6F50-05DD-41AF-A96A-195B37D6B44A)

\[56\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-B9A90172-E39C-4200-B6AC-9405CEC55E27](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-B9A90172-E39C-4200-B6AC-9405CEC55E27)

\[57\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-5576B0D6-277B-4DAB-8AC4-F45C16B69F67](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-5576B0D6-277B-4DAB-8AC4-F45C16B69F67)

\[58\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A0E302A3-C601-4221-8E98-71B93805CB81](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A0E302A3-C601-4221-8E98-71B93805CB81)

\[59\] [https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/5aq2t46QeMjWwAc9Xt9Qq5](https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/5aq2t46QeMjWwAc9Xt9Qq5)

\[60\] [https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/3wxq0cRq23ZAi0Iy2qC0bH](https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/3wxq0cRq23ZAi0Iy2qC0bH)

\[61\] [https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/7lQRdWrzTMfpag3T6sDJvR](https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/7lQRdWrzTMfpag3T6sDJvR)

\[62\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A1C4BEA9-7A6B-4214-BEFB-917C02E703DF](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A1C4BEA9-7A6B-4214-BEFB-917C02E703DF)

\[63\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-4DB61575-E353-49DE-8B8C-00EA6F4A1662](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-4DB61575-E353-49DE-8B8C-00EA6F4A1662)

\[64\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-4D9E2FB5-5D84-4FD6-B0BF-2EA4C8DB8FE8](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-4D9E2FB5-5D84-4FD6-B0BF-2EA4C8DB8FE8)

\[65\] [https://www.autodesk.com/blogs/water/2024/01/08/10-reasons-water-professionals-choose-infoworks-icm/](https://www.autodesk.com/blogs/water/2024/01/08/10-reasons-water-professionals-choose-infoworks-icm/)

\[66\] [https://www.autodesk.com/campaigns/infoworks-icm](https://www.autodesk.com/campaigns/infoworks-icm)

\[67\] [https://www.autodesk.com/blogs/water/2024/07/17/new-cloud-tool-and-improved-swmm-diagnostics-in-infoworks-icm-2025-2/](https://www.autodesk.com/blogs/water/2024/07/17/new-cloud-tool-and-improved-swmm-diagnostics-in-infoworks-icm-2025-2/)

\[68\] [https://www.autodesk.com/learn/ondemand/tutorial/introducing-infoworks-icm](https://www.autodesk.com/learn/ondemand/tutorial/introducing-infoworks-icm)

\[69\] [https://tools.bakerbaynes.com/product/autodesk-infoworks-icm/](https://tools.bakerbaynes.com/product/autodesk-infoworks-icm/)

\[70\] [https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-4ACDB430-D42A-4E8D-95B3-7D0C9CEDEBB9](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-4ACDB430-D42A-4E8D-95B3-7D0C9CEDEBB9)

\[71\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-4D6605FB-26B6-4CB4-AF14-4C681722DABF](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-4D6605FB-26B6-4CB4-AF14-4C681722DABF)

\[72\] [https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/6MnnBkyi1DiOAl9szEjRim](https://www.autodesk.com/learn/ondemand/curated/getting-started-with-infoworks-icm/6MnnBkyi1DiOAl9szEjRim)

\[73\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A23A3C03-5BE7-4E9A-9E56-43836B89EEC9](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A23A3C03-5BE7-4E9A-9E56-43836B89EEC9)

\[74\] [https://www.autodesk.com/blogs/water/2022/09/02/a-stormies-guide-to-infoworks-icm-free-learning-series/](https://www.autodesk.com/blogs/water/2022/09/02/a-stormies-guide-to-infoworks-icm-free-learning-series/)

\[75\] [https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A52BC284-0B98-48B0-87D8-2C702E4554DA](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-A52BC284-0B98-48B0-87D8-2C702E4554DA)

\[76\] [https://boards.autodesk.com/icm/items/infoworks-icm-on-demand-training-course](https://boards.autodesk.com/icm/items/infoworks-icm-on-demand-training-course)

\[77\] [https://www.youtube.com/playlist?list=PLxZQHvxMelqtGnZ7rfY1ngMU4GSksqNGs](https://www.youtube.com/playlist?list=PLxZQHvxMelqtGnZ7rfY1ngMU4GSksqNGs)

\[78\] [https://www.autodesk.com/support/technical/product/infoworks-icm](https://www.autodesk.com/support/technical/product/infoworks-icm)

\[79\] [https://www.youtube.com/watch?v=WicOJXiEtMs](https://www.youtube.com/watch?v=WicOJXiEtMs)

\[80\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/17d1Zu6m4WxK9wsHcS313Z](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/17d1Zu6m4WxK9wsHcS313Z)

\[81\] [https://www.autodesk.com/learn/ondemand/curated/administrators-implementation-guide-for-infoworks-icm/1cl6mspW35hO9D618PSI0o](https://www.autodesk.com/learn/ondemand/curated/administrators-implementation-guide-for-infoworks-icm/1cl6mspW35hO9D618PSI0o)

\[82\] [https://www.autodesk.com/learn/ondemand/tutorial/generating-a-2d-mesh](https://www.autodesk.com/learn/ondemand/tutorial/generating-a-2d-mesh)

\[83\] [https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/5h7rFbmSC6P5i4vjMZGfZd](https://www.autodesk.com/learn/ondemand/curated/infoworks-icm-quick-start-guide/5h7rFbmSC6P5i4vjMZGfZd)

\[84\] [https://www.autodesk.com/learn/ondemand/curated/version-control-and-scenarios-in-infoworks-icm/1QNWvz6itRkcaFf5hSXNi3](https://www.autodesk.com/learn/ondemand/curated/version-control-and-scenarios-in-infoworks-icm/1QNWvz6itRkcaFf5hSXNi3)

\[85\] [https://www.youtube.com/watch?v=ag9YQ3GOaUY](https://www.youtube.com/watch?v=ag9YQ3GOaUY)

\[86\] [https://www.youtube.com/watch?v=-LuOBFi5AKs](https://www.youtube.com/watch?v=-LuOBFi5AKs)

\[87\] [https://uscad.com/three-features-that-make-infoworks-icm-unique/](https://uscad.com/three-features-that-make-infoworks-icm-unique/)

\[88\] [https://www.youtube.com/watch?v=JiWfb0Ow8b4](https://www.youtube.com/watch?v=JiWfb0Ow8b4)

\[89\] [https://www.youtube.com/watch?v=blCEg7HWBhY](https://www.youtube.com/watch?v=blCEg7HWBhY)

\[90\] [https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/1a8cHcF8qVIBhCjSmAzPYd](https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/1a8cHcF8qVIBhCjSmAzPYd)

\[91\] [https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/39O64ktvvP0zKXkrDOikkV](https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/39O64ktvvP0zKXkrDOikkV)

\[92\] [https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/1WRFMiv6CCqWJMQcNzcRVV](https://www.autodesk.com/learn/ondemand/curated/analyzing-1d-results-in-infoworks-icm/1WRFMiv6CCqWJMQcNzcRVV)

\[93\] [https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/1zRXIlT0C43dFkBGx6IjAu](https://www.autodesk.com/learn/ondemand/curated/2d-results-analysis-in-infoworks-icm/1zRXIlT0C43dFkBGx6IjAu)

\[94\] [https://www.autodesk.com/blogs/water/2024/04/16/powerful-cloud-simulation-capabilities-and-flexible-ways-to-work-with-infoworks-2025/](https://www.autodesk.com/blogs/water/2024/04/16/powerful-cloud-simulation-capabilities-and-flexible-ways-to-work-with-infoworks-2025/)

\[95\] [https://www.autodesk.com/products/infoworks-icm/features](https://www.autodesk.com/products/infoworks-icm/features)

\[96\] [https://www.autodesk.com/campaigns/one-platform-for-every-catchment-infoworks-icm](https://www.autodesk.com/campaigns/one-platform-for-every-catchment-infoworks-icm)

\[97\] [https://www.autodesk.com/eu/campaigns/infoworks-icm-features](https://www.autodesk.com/eu/campaigns/infoworks-icm-features)

\[98\] [https://www.autodesk.com/campaigns/certification/aec-learning-and-certs1](https://www.autodesk.com/campaigns/certification/aec-learning-and-certs1)

\[99\] [https://www.autodesk.com/blogs/water/2024/08/21/infoworks-icm-training-tutorials-and-technical-tips-from-autodesk/](https://www.autodesk.com/blogs/water/2024/08/21/infoworks-icm-training-tutorials-and-technical-tips-from-autodesk/)

> Closing Note

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time you read one of these posts.**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
