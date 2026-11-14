---
title: "DB Tables for Sim Parameters in ICM InfoWorks and SWMM: Enhancing Understanding with SQL and Ruby"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/db-tables-sim-parameters-icm-infoworks-swmm-enhancing-dickinson-fxkfe
created: "2023-12-31 14:02"
published: "2023-12-31 23:18"
words: 677
export_sha256: 2b896c18b621172d2a09230742a64b5fff21b0d832eb7da9da573f1688499471
---
# DB Tables for Sim Parameters in ICM InfoWorks and SWMM: Enhancing Understanding with SQL and Ruby

![ Figure 1. InfoWorks Sim Parameters and SWMM Options using SQL Scripts](https://media.licdn.com/mediaD4E12AQE5T6Zi6QJDOg " Figure 1. InfoWorks Sim Parameters and SWMM Options using SQL Scripts")

A notable feature of InfoWorks is its utilization of tables. These tables are integrated across various components, including property sheets, the database, and grids. Additionally, they are instrumental in the application of SQL and Ruby code, enhancing the versatility and efficiency of data handling. This feature is applicable for both ICM InfoWorks and ICM SWMM networks. In this context, different prefixes are used to distinguish between the two: 'hw\_' is used for InfoWorks, while'sw\_' is designated for SWMM, ensuring clear and organized data management within the system.

![](https://media.licdn.com/dms/image/v2/D4E12AQEIyJvCY6ogXg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1704031435566?e=1795651200&v=beta&t=ZaOMPpmA2PpfJ10WoD1EaC63fx3oWBrAY8tqFfuYO64)

Figure 2. In this context, different prefixes are used to distinguish between the two: 'hw\_' is used for InfoWorks, while'sw\_' is designated for SWMM, ensuring clear and organized data management within the system.

Important themes in this post:

1.  **Tables: The Backbone of Your ICM Model**

    Tables form the core structure of your ICM model, providing a robust and organized framework for data management and simulation processes.

2.  **InfoWorks' Extensive Table Collection**

    InfoWorks boasts a comprehensive set of tables, each uniquely identified with a prefix 'hw\_'. This extensive collection facilitates detailed and specific data manipulation and analysis.

3.  **Simplified Table Structure in SWMM**

    In contrast, SWMM features a more streamlined set of tables, each beginning with 'sw\_'. This simplification aids in easier navigation and management of the model.

4.  **Interacting with Tables through SQL and Ruby**

    SQL and Ruby scripts interact with these tables, but in different ways. SQL accesses the tables directly without requiring prefixes, whereas Ruby necessitates the use of table prefixes. Additionally, Ruby offers a user interface (UI) and an exchange version, enhancing user interaction and data exchange capabilities.

5.  **SQL: A Tool to View Simulation Parameters**

    SQL proves to be an invaluable tool in viewing simulation parameters, offering insights into the workings of SWMM options and their configurations.

6.  **Distinct Engines for InfoWorks and SWMM**

    InfoWorks operates with a SIM Engine, while SWMM runs on the SWMMSIM engine. Each engine is tailored to suit the specific computational and simulation needs of their respective systems.

7.  **Open Source Code on GitHub**

    All SQL and Ruby code used in our models is openly available on our GitHub repository. This encourages collaboration, learning, and customization. You can find the link to our repository at the bottom of this article, providing easy access to a wealth of resources and information.

![](https://media.licdn.com/dms/image/v2/D4E12AQHJA-HsetYz2w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1704049297562?e=1795651200&v=beta&t=uzesnqMpA5wZl0gyNn3LZHjPIPg1wZWjHyCHon1bNkE)

Figure 3. ICM InfoWorks uses the SIM Engine and SWMM uses the SWMMSim Engine

> SQL Script to see the ICM InfoWorks sim parameters in an output script box

> Where do I find this code for ICM InfoWorks and SWMM Networks?

You can find the Ruby code for both the ICM InfoWorks and SWMM Networks from the InfoWorks [ICM Technical Information Hub for InfoWorks and SWMM Networks](https://boards.autodesk.com/4bf242?token=a671af9e76) in the subfolder **01 InfoWorks ICM\02 SQL\02 SWMM\0018 - SQL SWMM Options and 0017 - SQL Sim Parameters**

![](https://media.licdn.com/dms/image/v2/D4E12AQFN9q_yiiaZZA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1704062836829?e=1795651200&v=beta&t=mpdHeTHANTjL4qhsNgNXYuHc7PmQBVFINjMyvLAXSNk)

**Figure 4. Copy and paste the script output table into Excel. Transpose and make Graphics**

------------------------------------------------------------------------

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).

![](https://media.licdn.com/dms/image/v2/D4E12AQGZ-Zp3PBQCTw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1704049497338?e=1795651200&v=beta&t=p0vE1opog285KPRyGmZiGHSwKxdWkNJ9ZFLZuYiu7qI)

An AI Tale of Tables
