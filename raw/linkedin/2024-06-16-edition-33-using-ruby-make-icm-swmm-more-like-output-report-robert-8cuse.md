---
title: "Edition 33:  Using Ruby to make ICM SWMM more like InfoSWMM Output Report Tables"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-33-using-ruby-make-icm-swmm-more-like-output-report-robert-8cuse
created: "2024-06-16 19:21"
published: "2024-06-16 19:22"
words: 982
export_sha256: 3a6f38afdc4d7a01b12e5b25054f9eb9554b84b74d37a3966b443e7a5f86b966
---
# Edition 33:  Using Ruby to make ICM SWMM more like InfoSWMM Output Report Tables

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 33: Using Ruby to make ICM SWMM more like InfoSWMM Output Report Tables](https://media.licdn.com/mediaD4E12AQH2VDJXdrlleQ "Edition 33:  Using Ruby to make ICM SWMM more like InfoSWMM Output Report Tables")

InfoWorks ICM and Ruby scripting offer powerful capabilities to enhance and recreate functionalities from InfoSWMM, making it a superior tool for stormwater management and hydraulic engineering. This document highlights several key improvements and functionalities achieved by integrating Ruby scripting in InfoWorks ICM.

### Using Ruby to Identify and Highlight Problem Nodes and Links

Ruby scripts can read problem nodes and links directly from SWMM5 report files and add them as selected elements in ICM SWMM. This functionality allows users to efficiently pinpoint and address network issues, ensuring that problematic areas are quickly identified and prioritized for maintenance or further investigation. This integration streamlines the workflow, enabling a more proactive approach to network management.

### Recreating InfoSWMM Link Report Tables

Another powerful use of Ruby in ICM SWMM is the ability to recreate InfoSWMM link report tables from any SWMM5 report file. This script replicates the detailed link analysis available in InfoSWMM, providing users with comprehensive insights into link performance and behavior within their network. By translating these reports into ICM SWMM, users benefit from enhanced data consistency and easier comparison across different modeling platforms.

### Common SWMM5 Engine Usage and Compatibility

ICM SWMM and InfoDrainage share the same SWMM 5.2.4 engine (swmmsim.exe), while InfoSWMM utilizes an older version of the EPA SWMM5 engine based on SWMM 5.1.015. This commonality ensures that models developed in ICM SWMM and InfoDrainage are compatible and can leverage the latest features and improvements in the SWMM5.2.4 engine. The alignment with the latest SWMM engine version enhances modeling accuracy and reliability.

### Exporting Data to Shapefiles and CSV Files

Ruby scripting in ICM InfoWorks and SWMM also facilitates the export of node, link, and subcatchment grid data to shapefiles and custom folders. This capability is invaluable for integrating ICM data with GIS applications, allowing for more advanced spatial analysis and visualization. Similarly, Ruby can export user-selected link results to custom CSV folders, providing data handling and reporting flexibility. These exports enhance the usability and accessibility of model results, enabling users to share and utilize data across various platforms effectively.

### Knowledge-Assisted Theme Enhancements

ICM SWMM has knowledge-assisted theme improvements that make map views for parameters like d/D (depth to diameter ratio) and q/Q (flow to capacity ratio) look like those in InfoSWMM. These visual enhancements help users quickly understand and interpret network performance, aiding decision-making processes. The improved visualization capabilities ensure critical information is presented clearly and effectively, facilitating better network management and planning.

### Closing Thought

Integrating Ruby scripting with InfoWorks ICM significantly enhances the platform's capabilities, making it a robust stormwater and wastewater network management tool. Users benefit from improved data analysis, reporting, and visualization by incorporating functionalities from InfoSWMM and extending them with advanced scripting. This synergy between Ruby and InfoWorks ICM provides a comprehensive and efficient solution for managing complex hydraulic and hydrologic models in the context of ICM SWMM. Ruby can be used to add ICM SWMM to make it more like the well-known output tables of InfoSWMM.

> **0: A Better Workflow for InfoSWMM to ICM SWMM Network Conversions for ALL InfoSWMM Scenarios and Active Elements into One ICM SWMM Network**

\[embedded item\]

> **1: How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM**

\[embedded item\]

> **2: Using Ruby to Recreate the InfoSWMM Link Report Tables in ICM SWMM from any SWMM5 Report File**

\[embedded item\]

> **3: How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM**

\[embedded item\]

> **4: ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015**

\[embedded item\]

> **5: Using Ruby to Export ICM InfoWorks Node, Link, and Subcatchment Grid Data to Shapefiles and a Custom Folder**

\[embedded item\]

> **6: Using Ruby to Export ICM InfoWorks User-Selected Link Results to a Custom CSV Folder**

\[embedded item\]

> **7: Knowledge Assisted Theme Enhancements in ICM SWMM to Show InfoSWMM Like Map Displays for d/D and q/Q**

\[embedded item\]

> **Closing Note:**

Thank you for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found rather uninteresting. Ramanujan immediately responded that 1729 is very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.

![]()

Midjourney AI Image
