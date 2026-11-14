---
title: "Navigating ICM InfoWorks' Population-Based vs. SWMM's Mean Flow-Based Dry Weather Flow in Sanitary Systems, With SQL Tips to Cope - Pars Prima"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/navigating-icm-infoworks-population-based-vs-swmms-mean-dickinson
created: "2023-08-29 06:34"
published: "2023-08-30 06:19"
words: 828
export_sha256: d77b0c71614145cea3c22ac366720e89dc61191f195729aa692e2d9f018b93c5
---
# Navigating ICM InfoWorks' Population-Based vs. SWMM's Mean Flow-Based Dry Weather Flow in Sanitary Systems, With SQL Tips to Cope - Pars Prima

![Focus is solely on making the Dry Weather Flow (DWF) modeling in SWMM more like that in Innovyze ICM](https://media.licdn.com/mediaD4E12AQFlhRBNnovWFQ "Focus is solely on making the Dry Weather Flow (DWF) modeling in SWMM more like that in Innovyze ICM")

> **Introduction to the Workaround**

**ICM InfoWorks: The Population-Based Approach**

ICM InfoWorks offers a comprehensive solution for wastewater management with a focus on population-based flows. The software excels in modeling various components, including trade flow, base flow, and additional foul flow, attributed to specific subcatchments. By utilizing population data, InfoWorks provides a nuanced understanding of how human activities impact wastewater systems, allowing for more accurate planning and decision-making.

![](https://media.licdn.com/dms/image/v2/D4E12AQFOpspxUlYEOQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1693369483772?e=1795651200&v=beta&t=EUJesga-Wr7f9Q316uFvzAxIw8AYZrM-Fg1hfOvmWLg)

Options for Base, DWF or WW, Trade and Foul Flow in an ICM InfoWorks Network

**ICM SWMM: A Focus on Baseline Inflows and Multiple DWFs**

On the other side, we have ICM SWMM, which offers a different approach by focusing on baseline inflow and multiple Dry Weather Flows (DWFs) at each node. While it does not incorporate population-based data, it provides the flexibility to manage different types of inflows at specific nodes. This offers a targeted way to model and manage wastewater systems, particularly in areas where baseline data is crucial for accurate representation.

![](https://media.licdn.com/dms/image/v2/D4E12AQFfseBeyC7gyQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1693369519590?e=1795651200&v=beta&t=G5SipwS1q4Cz1_QyTRhBOCd-MwUNm7fbylWF8vwnVhA)

Options for DWF and additional flow in an ICM SWMM Network

**Our Goal**

Both ICM InfoWorks and ICM SWMM bring valuable tools to the table in the realm of wastewater management. While InfoWorks offers a population-based approach that allows for a more comprehensive understanding of wastewater systems, SWMM provides specialized capabilities for managing baseline and dry weather flows. Depending on the specific needs and challenges of a project, each software has its unique strengths that can be leveraged for optimal wastewater management solutions.

![](https://media.licdn.com/dms/image/v2/D4E12AQFblSmc8YnN7w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1693401365067?e=1795651200&v=beta&t=nx7N-wu5J4_6A9XCRcG196DxDY20gby3WQgvdxWO9nE)

Menu Tool to convert ICM InfoWorks to ICM SWMM

> How do we Cope with the fact that InfoWorks is population based at a Subcatchment but ICM SWMM is mean flow based at a Node?

The network is converted and the population from InfoWorks is the mean flow at a node in ICM SWMM - if not adjusted then this will be a tremendous amount of flow in the SWMM engine. As shown in the next figure the population (with decimal points) is at a Subcatchment in InfoWorks. This is imported as a mean flow in CMS at a node in ICM SWMM but not converted from people to mean flow. **The decimal places are lost was the converter assumes there are no fractional people.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFyc2GN6fYgYQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1693401121197?e=1795651200&v=beta&t=j-pxA_j0fBqsZKf5aD0IyIJ5miWQWkzKjnWXvG3OtkM)

Population is imported as mean flow in ICM SWMM

> **Where is the Conversion Factor?**

The conversion factor in liters per day is located in the wastewater profile or 143 liters per day for one profile. We will use this for now in a SQL script.

![](https://media.licdn.com/dms/image/v2/D4E12AQG18976zhZMyA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1693374541813?e=1795651200&v=beta&t=e_Vs_wfmnuX37030j85B7uOAuA-KNu6R862pdz_0t3w)

The conversion factor in liters per day is located in the wastewater profile or 143 liters per day for one profile

> **SQL Code**

Convert the converted population as flow to the right units of flow. Use 143 liters / day and the divide by 86400 and 1000 to convert liters per day to CMS. Doing a hand calculation first value of 83 should now be 0.00013737 CMS. It is based on the ICM SWMM Node Grid.

![](https://media.licdn.com/dms/image/v2/D4E12AQHSyLOXpUPtXw/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1693375481240?e=1795651200&v=beta&t=X--Ip0zr52y8DpHXRS7pCH_xujRCgG-Zoc7uNxqU3f4)

Sanity Check the flows are now in CMS units and Correct.

![](https://media.licdn.com/dms/image/v2/D4E12AQGJD4x3PtMCxg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1693375972858?e=1795651200&v=beta&t=anVB7twMtvJoX7Qj7nxzoj4qLFT_2K8E2quG0-tPEpo)

SQL Conversion Dialog

> An Artful Summary in Verse: Tasks Awaiting Completion

As we embark on this comprehensive journey of system conversion and optimization, it's important to note that we are still in the initial stages—aptly termed 'Pars Prima' or 'Part One.' The forthcoming tasks include the meticulous conversion of all profiles, encompassing trade, foul, and additional waste, into ICM SWMM. It's crucial to understand that these elements are not automatically imported and will require a dedicated workflow. Additionally, we will be developing a structured approach for managing the various flow patterns.

Stay tuned as we continue to explore and implement these vital components in our transition to ICM SWMM in Pars Secunda and Pars Tertia.
