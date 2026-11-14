---
title: "📊 A Saga of Input Data: SWMM's Input SW Tables 🗂️  and InfoWorks HW Hydroworks Tables 🗂️ 💧 with Ruby and SQL"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/saga-input-data-swmms-sw-tables-infoworks-hw-ruby-sql-dickinson-5kf1e
created: "2024-01-07 01:15"
published: "2024-01-07 12:46"
words: 873
export_sha256: 703440d49d01031f1fd7159109d7ce3c9907e9bdd8faa5ca4501e187ddb08d10
---
# 📊 A Saga of Input Data: SWMM's Input SW Tables 🗂️  and InfoWorks HW Hydroworks Tables 🗂️ 💧 with Ruby and SQL

![A Tale of SW and HW Tables in ICM](https://media.licdn.com/mediaD4E12AQEHJHp_ZBG8vw "A Tale of SW and HW Tables in ICM")

This article shows how to see the complexity differences between ICM InfoWorks and SWMM networks with Ruby code for showing all of the input parameters in both ICM InfoWorks and ICM SWMM Networks. All of these parameters can be used with SQL and Ruby scripts for customization. It's noteworthy that ICM InfoWorks networks are more complex than SWMM networks. This is evident in the comparison of their underlying data structures: ICM InfoWorks networks are based on 93 tables and approximately 7300 lines of input parameters, whereas SWMM networks are simpler with 47 tables and about 3180 lines of input parameters. This complexity indicates a higher level of detail and customization possible in ICM InfoWorks networks compared to SWMM networks.

1.  **InfoWorks SIM and SWMM SWMMSim Engines**: This section compares the simulation engines of InfoWorks SIM and SWMM SWMMSim, highlighting their functionalities and differences.

2.  **InfoWorks Parameters for Table hw_subcatchment**: Focused on the parameters used in the InfoWorks software, specifically for the 'hw_subcatchment' table. It details the various settings and options available within InfoWorks for modeling subcatchments.

3.  **ICM SWMM Parameters for Table sw_subcatchment**: Similar to Section 2, this section is dedicated to the parameters used in the ICM SWMM model for the'sw_subcatchment' table, outlining the specific configurations for SWMM networks within the ICM framework.

4.  [**Readme.md**](http://Readme.md) **File for the Ruby Code**: This section provides documentation and instructions for the Ruby code used in the context of these network models. It's likely a guide or a manual for users to understand how to implement or interact with the Ruby code in their projects.

5.  **Where to Find Code for ICM InfoWorks and SWMM Networks?**: addresses the common question of where users can locate or access the Ruby code and other relevant scripts or software for both ICM InfoWorks and SWMM networks.

6.  **Copy of Ruby Code for SWMM and InfoWorks Networks in ICM—Short but Effective**: Offers a direct look at the Ruby code used for both SWMM and InfoWorks networks within ICM. This section likely showcases concise yet powerful coding examples, demonstrating how the Ruby code is implemented.

> Section 1: InfoWorks SIM and SWMM SWMMSim Engines

![](https://media.licdn.com/dms/image/v2/D4E12AQFMqJ_wV86QAA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1704631147254?e=1795651200&v=beta&t=i8UHzGW740LRNtLsafeARUX80wWHeeZCgJ-0JMCXzPA)

🌐 Tables are the very foundation of ICM, acting as the structural backbone that supports the entire system. 📊 For InfoWorks, each table is distinctively marked with an 'hw\_' prefix, while SWMM tables are easily identified by their'sw\_' prefix.

> Section 2: InfoWorks parameters for Table hw_subcatchment

> Section 3: ICM SWMM parameters for Table sw_subcatchment

Section 4: [Readme.md](http://readme.md/) file for the Ruby Code

> **Section 5:** Where do I find this code for ICM InfoWorks and SWMM Networks**?**

You can find the Ruby code for both the ICM InfoWorks and SWMM Networks from the InfoWorks [ICM Technical Information Hub for InfoWorks and SWMM Networks](https://boards.autodesk.com/4bf242?token=a671af9e76) in the subfolder **01 InfoWorks ICM\02 SQL\0032 - List Network Fields-Structure (SWMM or ICM)**

> **Section 6: Copy of Ruby Code for SWMM and InfoWorks Networks in ICM - Short but Effective** In our demonstration, we showcase a Ruby script specifically crafted for reading the IWR output file in ICM. 📜🔍

🖥️ The script cleverly extracts and displays result variables directly in the script window, offering a clear and immediate view of the data. These variable names, which are also meticulously listed in the ICM Online Help File, serve as crucial references. 📚💡

📈 Using these names, you can craft custom output scripts tailored to your specific needs. This flexibility enhances the already wide array of graphs and grids that ICM provides, allowing for personalized data visualization and analysis. 📊📉 Whether it's for detailed reporting or comprehensive data study, these tables and scripts empower users to maximize the potential of ICM's robust functionalities. 🛠️💻📈

> Section 1: InfoWorks SIM and SWMM SWMMSim Engines

![](https://media.licdn.com/dms/image/v2/D4E12AQGPercn9SelgA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1704590139977?e=1795651200&v=beta&t=-UZFqz2Of74psBhzCjzRR-gr-prB8kXcbsPgT6S1r_I)

InfoWorks SIM and SWMM SWMMSim Engines and Table Names

> Section 2: InfoWorks parameters for Table hw_subcatchment

> Section 3: ICM SWMM parameters for Table sw_subcatchment

Section 4: [Readme.md](http://Readme.md) file for the Ruby Code

> **Section 5:** Where do I find this code for ICM InfoWorks and SWMM Networks**?**

You can find the Ruby code for both the ICM InfoWorks and SWMM Networks from the InfoWorks [ICM Technical Information Hub for InfoWorks and SWMM Networks](https://boards.autodesk.com/4bf242?token=a671af9e76) in the subfolder **01 InfoWorks ICM\02 SQL\0032 - List Network Fields-Structure (SWMM or ICM)**

> **Section 6: Copy of Ruby Code for SWMM and InfoWorks Networks in ICM - Short but Effective**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
