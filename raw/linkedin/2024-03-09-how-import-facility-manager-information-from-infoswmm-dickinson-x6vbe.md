---
title: "How to Import the Facility Manager Information from InfoSewer and InfoSWMM to an ICM InfoWorks Selection Set"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-import-facility-manager-information-from-infoswmm-dickinson-x6vbe
created: "2024-03-06 16:33"
published: "2024-03-09 15:34"
words: 865
export_sha256: 3d5f5bf9716fe3e6844ac0af999d5de52690c095e3d31fef7e6f4be3c2539322
---
# How to Import the Facility Manager Information from InfoSewer and InfoSWMM to an ICM InfoWorks Selection Set

![How to Import the Facility Manager Information from InfoSewer and InfoSWMM to ICM InfoWorks](https://media.licdn.com/mediaD4E12AQF-C_0nQpFpcQ "How to Import the Facility Manager Information from InfoSewer and InfoSWMM to ICM InfoWorks")

The purpose of this Ruby script is to import all of the facility sets from InfoSWMM and InfoSewer, as well as to create selection sets that can be used for both ICM InfoWorks and ICM SWMM. Through the use of the Ruby code, the facility is imported from each and every scenario in InfoSWMM or InfoSewer. From a practical standpoint, we are converting the facility manager selections into selection sets.

Roadmap and background

- **InfoSewer and InfoSWMM Facility Manager**:Allows users to define the active or inactive status of system elements based on specific criteria.Automates the documentation of active elements into Anode.DBF and ALINK.DBF files, eliminating the need for manual tracking outside the software environments.

- **Integration with ICM after importing the InfoSewer or InfoSWMM model**:ICM InfoWorks and ICM SWMM utilize selection sets that include node, link, and subcatchment IDs, facilitating comprehensive system analysis.A specialized ruby code reads Anode.DBF and ALINK.DBF files to create selection sets for all scenarios imported into ICM, streamlining the management process.

1.  **Figure 1: Active Elements in a Scenario of InfoSewer are saved to the ALINK and ANODE files in the Scenario Subfolder**

2.  **Figure 2: What the scenario folder for InfoSewer looks like, and the subfolders have the Anode and Alink file.**

3.  **Figure 3: Ruby Script after importing the Scenario Folder**.

4.  **Figure 4: Created Selection Sets from reading the Anode and Alink files from InfoSewer**

5.  **Figure 5: Using the selection sets to show the active InfoSewer elements in InfoWorks. Non active elements are now excluded - delete the non active elements in a scenario**

6.  **Section 1/ Where do you find the code on Github?**

7.  **Section 2/ The Ruby Code.**

8.  **Section 3/ The Ruby Code Explained.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFmTq0HYr2Fbw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709850150397?e=1795651200&v=beta&t=1IyMe6BgrcL3O1Ga3HdnfTwEg450t_a59OhMVWDtv_8)

Figure 1: Active Elements in a Scenario of InfoSewer are saved to the ALINK and ANODE files in the Scenario Subfolder

![](https://media.licdn.com/dms/image/v2/D4E12AQEHCEGmUlHw1A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710004883806?e=1795651200&v=beta&t=BAs28M7P6wET3yOzGVW0Ieielhse62ZvyUoBY1_xHrM)

Figure 2: What the scenario folder for InfoSewer looks like, and the subfolders have the Anode and Alink files.

![](https://media.licdn.com/dms/image/v2/D4E12AQEmXSA35svgPw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709935656263?e=1795651200&v=beta&t=qdWBpEj-jdG0jwtNyONvfgFeBmYFiIY2s8YyGit9EPQ)

Figure 3: Ruby Script after importing the Scenario Folder

![](https://media.licdn.com/dms/image/v2/D4E12AQGRa5fMjk-k5w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709935670447?e=1795651200&v=beta&t=0LtJGJ9cArYBBjs2z278mHCvidJQ-CfTFr33nwWewpA)

Figure 4: Created Selection Sets from reading the Anode and Alink files from InfoSewer

![](https://media.licdn.com/dms/image/v2/D4E12AQFQ_UeoKzlqkA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709935692027?e=1795651200&v=beta&t=qhhY_u6d2HPnqvpjbk0ldDP_norP9Bj2Vry_rHfc6eo)

Figure 5: Using the selection sets to show the active InfoSewer elements in InfoWorks. Non active elements are now excluded - delete the non active elements in a scenario.

> **1/ Where do you find the code**

The [ICM Technical Support Hub](https://boards.autodesk.com/icm) leads you to the Innovyze GitHub site and the needed code is called Step24_User_123_ICM_anode_alink_csv.rb in the subfolder 0100 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM under InfoWorks ICM\01 Ruby\02 SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQEsbBW-8ctC2g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709849397800?e=1795651200&v=beta&t=3MjW7tfG5_ffWCsJnsxkXRBTF0uEBvHCOeSnW6mV-uI)

> **2/ Ruby Code**

**3/ Ruby Code Explained**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
