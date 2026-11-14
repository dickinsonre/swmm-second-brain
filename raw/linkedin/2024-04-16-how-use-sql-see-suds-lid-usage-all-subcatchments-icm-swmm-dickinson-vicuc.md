---
title: "How to use SQL to see the SUDS or LID Usage for all Subcatchments in ICM InfoWorks and SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-sql-see-suds-lid-usage-all-subcatchments-icm-swmm-dickinson-vicuc
created: "2024-03-28 02:46"
published: "2024-04-16 15:12"
words: 1214
export_sha256: 3138ff7bb3ca7b93325fbb90b8cebee373bd964f9704b89eb7f814da5609cbf1
---
# How to use SQL to see the SUDS or LID Usage for all Subcatchments in ICM InfoWorks and SWMM Networks

![How to use SQL to see the SUDS or LID Usage for all Subcatchments in ICM InfoWorks and SWMM Networks](https://media.licdn.com/mediaD4E12AQFYQLxoPwvTiQ "How to use SQL to see the SUDS or LID Usage for all Subcatchments in ICM InfoWorks and SWMM Networks")

ICM InfoWorks and ICM SWMM leverage the core SWMM5 code to implement Low Impact Development (LID) controls, but they do so with distinct approaches. ICM InfoWorks integrates a SWMM5 Dynamic Link Library (DLL), enabling it to use the existing SWMM5 framework for what it calls its SUDS functionalities. On the other hand, ICM SWMM utilizes a specially tailored SWMM5.2+ engine that has been explicitly adapted for the ICM SWMM environment to enhance performance and integration within the ICM framework.

Although both ICM platforms share these advanced features, they have one major flaw: they do not give a simple visual representation (like a grid or table view) of LID or SUDS implementations across all subcatchments. This gap can complicate efforts to review and assess the widespread application of these environmentally friendly controls throughout the model.

To mitigate this issue, a SQL script is provided. This script facilitates the creation of a comprehensive table detailing the application of LID or SUDS for each subcatchment within the network. By making this table, users get a useful tool that makes it easy to see and figure out how LID and SUDS controls are distributed and how well they work. This improves the overall management and accuracy of their environmental impact assessments in urban drainage simulations.

To mitigate this issue, a bespoke SQL script is provided. This script facilitates the creation of a comprehensive table detailing the application of LID or SUDS for each subcatchment within the network. By making this table, users get a useful tool that makes it easy to see and figure out how LID and SUDS controls are distributed and how well they work. This improves the overall management and accuracy of their environmental impact assessments in urban drainage simulations.

![](https://media.licdn.com/dms/image/v2/D4E12AQEX07FRa2zMeQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713141220989?e=1795651200&v=beta&t=DIZ4eRGSOExC995Pnsb661kamoZrnieS47VZYzAA8Ys)

The SQL code shows in a SQL table the LID coverage in InfoWorks or ICM SWMM. This is the same coverage you see in SWMM5 at the Subcatchment Level

> **1. Introduction**

Both ICM InfoWorks and ICM SWMM utilize the underlying SWMM5 code for LID functionality, but with some key differences. ICM InfoWorks uses a SWMM5 DLL, while ICM SWMM employs a modified SWMM5.2+ engine specifically developed for the ICM SWMM platform. However, in both ICM networks, the usage of LID or SUDS features across all subcatchments cannot be seen in a grid or a table. To address this, the provided SQL script creates a table that allows you to easily identify the LID or SUDS usage for each subcatchment. This can help you better understand the model setup and fix any issues related to the application of LID or SUDS controls throughout the network.

> **2. How to use the SQL**

You can copy it from this article or copy the SQL from our [GitHub (Innovyze)](https://boards.autodesk.com/icm). The SQL uses an **Object Type of Subcatchment and a suds_controls Field type**.

![](https://media.licdn.com/dms/image/v2/D4E12AQGNOP3WEKxjJw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713140513079?e=1795651200&v=beta&t=zj3sqA9uBkOdyDDroqvTfvAivArpHBSZmYuJVXOknwU)

> **3. SQL Script Explanation**

> **4. Step-by-Step Guide**

To utilize the SQL script that creates a table to display the LID or SUDS usage for each subcatchment in an ICM InfoWorks or ICM SWMM Network follow these steps:

1.  Open the SQL query tool within ICM.

2.  Copy and paste the provided SQL script into the SQL Query tool.

3.  Review the script and make any necessary modifications to ensure it matches the specific requirements of your project, such as adjusting table or column names.

4.  Execute the SQL script by running the query.

5.  Once the script has completed, you can interpret the results, which will provide a comprehensive overview of the LID or SUDS usage across all subcatchments in your ICM InfoWorks model. This information can help you identify any issues or inconsistencies in the application of these features throughout your stormwater management network.

> **5. SQL Script**

> **6. Results Interpretation**

\- Explanation of the output generated by the SQL script

\- Identifying subcatchments with LID/SuDS usage

\- Understanding the LID/SuDS controls applied to each subcatchment

\- Utilizing the information for further analysis or decision-making

> **7. Troubleshooting**

The SQL required for ICM InfoWorks and ICM SWMM can vary, even though the underlying data may be the same. The key difference lies in the database table naming conventions used by each software. The network you use has to be dragged to the GeoPlan.

In ICM InfoWorks, the database tables typically start with "hw\_", whereas in ICM SWMM, the tables start with "sw\_". This distinction is important to keep in mind when constructing your SQL queries.

For example, if you need to retrieve information about subcatchments, the table name in ICM InfoWorks would be "hw_subcatchments", while in ICM SWMM, it would be "sw_subcatchments". Similarly, other key model components, such as conduits, junctions, and outfalls, will have different table names depending on whether you're working with ICM InfoWorks or ICM SWMM.

> **8. Conclusion**

This outline provides a structure to the process of using an SQL script to view SWMM5 LID/SuDS usage and controls on subcatchments in InfoWorks ICM. The article aims to help users overcome the limitations of the user interface and gain insights into their LID/SuDS modeling data.

![](https://media.licdn.com/dms/image/v2/D4E12AQHZqzUUCBm5kw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713138003697?e=1795651200&v=beta&t=IWqzUF03kB3f7QT4gTU6zZTdEgmriXl1Kw5TFpX3fNY)

Green Infrastructure Housing Complex

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
