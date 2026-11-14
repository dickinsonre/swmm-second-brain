---
title: "How to import the Manhole Loads from Only One InfoSewer Scenario to the Subcatchments in ICM InfoWorks using Ruby"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-import-manhole-loads-from-only-one-infosewer-icm-using-dickinson-65sme
created: "2024-03-11 17:53"
published: "2024-03-11 22:47"
words: 708
export_sha256: d9630195fbfe28245a3fe859b455ce1b85c45c92aee43bd30504c84749d230ad
---
# How to import the Manhole Loads from Only One InfoSewer Scenario to the Subcatchments in ICM InfoWorks using Ruby

![How to import the Manhole Loads from Only One InfoSewer Scenario to the Subcatchments in ICM InfoWorks using Ruby](https://media.licdn.com/mediaD4E12AQGfYCeF_jjbLA "How to import the Manhole Loads from Only One InfoSewer Scenario to the Subcatchments in ICM InfoWorks using Ruby")

This Ruby code is intended to speed up the transfer of sanitary load data from InfoSewer to ICM InfoWorks. This code simplifies data management operations by using Ruby to read ONE manhole dataset from InfoSewer to be copied to the Node and Subcatchment Grids of ICM InfoWorks.

It prompts the user to locate this dataset within the manhole subfolder of the IEDB folder, which serves as the InfoSewer database repository.

The main features of this blog are:

1.  **Figure 1: Two RB files Step22User123_ICM_mhhyd_csv_File_Reader.rb reads ONE MHHyd.CSV and Step22a_User_123_ICM_mhhyd_csv_One_Read.rb reads ALL MHHyd.CSV files for all scenarios**

2.  **Figure 2: Ruby Script queries to find the right data set for the selected scenario**

3.  **Figure 2: InfoSewer manhole loads are copied to the the node and subcatchment grid in an ICM InfoWorks Network. Ruby script output shows what was imported and the fields it was imported to in ICM InfoWorks.**

4.  **Section 1: Where do you find the code on Github?**

5.  **Section 2: The Ruby Code.**

6.  **Section 3: The Ruby Code Explained.**

![](https://media.licdn.com/dms/image/v2/D4E12AQEeafVqS67sIw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710196704961?e=1795651200&v=beta&t=BLXM_BZwJy558p1Sl7QnzqONVIbz3ra-PXoT9CHzt_o)

**Figure 1: Two RB files Step22User123_ICM_mhhyd_csv_File_Reader.rb reads ONE MHHyd.CSV and Step22a_User_123_ICM_mhhyd_csv_One_Read.rb reads ALL MHHyd.CSV files for all scenarios**

![](https://media.licdn.com/dms/image/v2/D4E12AQEHaQOcVTcxDA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710194049321?e=1795651200&v=beta&t=ptu_kiI8poezBUYDpQTctLupQ7DlUgt-z7stvJK0qqA)

**Figure 2: Ruby Script queries to find the right data set for the selected scenario**

![](https://media.licdn.com/dms/image/v2/D4E12AQEgPqYfS-spEw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1710194075035?e=1795651200&v=beta&t=asVliRKfd54XtdVjqE7ilcZNr0Pzr0p_JhxqdHgyiwk)

**Figure 3: InfoSewer Manhole loads are copied to the the node and subcatchment grid in an ICM InfoWorks Network. Ruby Script output shows what was imported and the fields it was imported to in ICM InfoWorks.**

> 1/ Where do you find the code?

The [ICM Technical Support Hub](https://boards.autodesk.com/icm) leads you to the Innovyze GitHub site and the needed code is called Step22*User*123_ICM_mhhyd_csv_File_Reader.rb in the subfolder 0100 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM under InfoWorks ICM\01 Ruby\02 SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQFIAzxGyRSznQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710179568241?e=1795651200&v=beta&t=4ncpxSLutibfjSfxE4xqZmyW07gWp3JGLaPbwKfGtr0)

Innovyze GitHub General Layout

> **2/ Ruby Code for Step22_User_123_ICM_mhhyd_csv_File_Reader.rb**

> **3/ Ruby Code Explained for Step22_User_123_ICM_mhhyd_csv_File_Reader.rb**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
