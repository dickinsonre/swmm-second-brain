---
title: "How to import the Manhole Loads from every InfoSewer Scenario to Subcatchments in ICM InfoWorks using Ruby"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-import-manhole-loads-from-every-infosewer-icm-using-dickinson-nqn0e
created: "2024-03-09 15:36"
published: "2024-03-11 15:58"
words: 663
export_sha256: dc2fae9c565a0e48cb7f83878de98507f70f207c49e46a4f29932041218d5660
---
# How to import the Manhole Loads from every InfoSewer Scenario to Subcatchments in ICM InfoWorks using Ruby

![How to import the Manhole loads from every InfoSewer Scenario to a Subcatchment in ICM InfoWorks](https://media.licdn.com/mediaD4E12AQHUFX95898JqA "How to import the Manhole loads from every InfoSewer Scenario to a Subcatchment in ICM InfoWorks")

This Ruby code is intended to speed up the transfer of sanitary load data from InfoSewer to ICM InfoWorks. This code simplifies data management operations by allowing all InfoSewer scenario loads to be read at the same time and effectively copied to ICM InfoWorks user fields.

Here's how it works: First, the software asks the user to specify the location of the InfoSewer scenario file. After receiving this input, it extracts the dataset for each scenario. Then, to ensure proper data integration, it prompts the user to locate this dataset within the manhole subfolder of the IEDB folder, which serves as InfoSewer's database repository.

The main features of this blog:

1.  **Figure 1: Ruby Script queries to find the right data set for each scenario**

2.  **Figure 2: The code finds the data set from InfoSewer that was used in the scenario.**

3.  **Figure 3: Ruby Script output shows what was imported and the fields it was imported to in ICM InfoWorks.**

4.  **Figure 4: The original loads from InfoSewer are saved to the user fields of ICM in the original unts. You need to use SQL to convert them from LPS or GPM to CMS or MGD, respectively.**

5.  **Section 1/ Where do you find the code on Github?**

6.  **Section 2/ The Ruby Code.**

7.  **Section 3/ The Ruby Code Explained.**

![]()

**Figure 1: Ruby Script queries to find the right data set for each scenario**

![]()

**Figure 2: The Code finds the data set from InfoSewer that was used in the scenario.**

![]()

**Figure 3: Ruby Script output shows what was imported and the fields it was imported to in ICM InfoWorks.**

![]()

**Figure 4: The original loads from InfoSewer are saved to the user fields of ICM in the original unts. You need to use SQL to convert them from LPS or GPM to CMS or MGD, respectively.**

> 1/ Where do you find the code?

The [ICM Technical Support Hub](https://boards.autodesk.com/icm) leads you to the Innovyze GitHub site and the needed code is called Step22a_User_123_ICM_mhhyd_csv_One_Read.rb in the subfolder 0100 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM under InfoWorks ICM\01 Ruby\02 SWMM

![]()

Innovyze GitHub General Layout

> **2/ Ruby Code**

**3/ Ruby Code Explained**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
