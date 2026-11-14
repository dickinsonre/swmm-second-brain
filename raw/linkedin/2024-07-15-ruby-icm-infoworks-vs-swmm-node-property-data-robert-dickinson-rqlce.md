---
title: "Ruby ICM InfoWorks vs. ICM SWMM Node Property Data Comparison"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/ruby-icm-infoworks-vs-swmm-node-property-data-robert-dickinson-rqlce
created: "2024-03-23 22:07"
published: "2024-07-15 03:59"
words: 760
export_sha256: 2f26db4eae867e480493001c317f8202399ef96b6906d16dd0736dcbcff67aa0
---
# Ruby ICM InfoWorks vs. ICM SWMM Node Property Data Comparison

![Ruby ICM InfoWorks vs. ICM SWMM Node Property Data Comparison ](https://media.licdn.com/mediaD4E12AQEEBI75GoT9LQ "Ruby ICM InfoWorks vs. ICM SWMM Node Property Data Comparison ")

The ICM Infoworks and SWMM Network Comparison Tool for Nodes is a script designed to bridge the gap between two hydraulic modeling systems, InfoWorks and SWMM, as implemented in ICM. This tool provides engineers and modelers a powerful means to compare and analyze node attributes across these two networks within the Integrated Catchment Modeling (ICM) environment.

At its core, the tool facilitates a detailed comparison between InfoWorks HW Node Tables and SWMM SW Nodes Tables. It allows users to select specific attributes for comparison, such as ground level, chamber floor/invert elevation, flood level/surcharge depth, maximum depth, floodable area/ponded area, and chamber/shaft area. This flexibility lets users focus on the most relevant parameters for their analysis needs.

The comparison process is both comprehensive and user-friendly. It begins by setting up the current network (CN) as the ICM Infoworks Network and the background network (BN) as the ICM SWMM Network. The tool then collects node data from both networks and presents users with an interface to select the attributes they wish to compare. As the comparison runs, it calculates differences between corresponding nodes, highlighting significant discrepancies and providing overall statistics on the comparison results.

What sets this tool apart is its attention to detail and ability to handle special cases. For instance, it applies specific logic for attributes like 'min_surfarea' and 'surcharge_depth', ensuring accurate comparisons even for complex scenarios. The output is designed to be informative and actionable, focusing on nodes with significant differences and providing a clear statistical overview of the comparison.

This tool saves time and enhances the accuracy and reliability of hydraulic modeling efforts by bridging InfoWorks and SWMM networks. It's an invaluable asset for engineers and modelers working with multiple hydraulic modeling platforms, offering insights that can lead to more informed decision-making and improved model consistency. It helps you find modeling differences.

![](https://media.licdn.com/dms/image/v2/D4E12AQFbw50UhwpZzw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721010894064?e=1795651200&v=beta&t=_QjSV-gINEPNuZuEHvGjl26GuPdVqDemP7sWLFCMppQ)

Seven possible comparisons between InfoWorks HW Node Tables and SWMM SW Nodes Tables

> **Ruby Script Output**

The attribute pairings we will compare consist of various related SWMM and ICM parameters. The first property is the ground levels of the InfoWorks and SWMM nodes, and the following additional pairs will be compared with each other:

- and : These two attributes represent different aspects of the network’s structure and will be compared to identify discrepancies.

- and : These attributes are crucial in understanding the network’s capacity and response to flooding events.

- : This attribute is also a standalone parameter that will be analyzed separately.

- and : These attributes provide insights into the areas that are susceptible to flooding.

- and : These parameters are compared to understand the minimum surface area required for the chamber.

- and : This comparison helps understand the minimum surface area required for the shaft.

**6. Output**

The output of this comparison will provide valuable insights into the network:

- Nodes with a difference percentage greater than 0.1% will be displayed. This helps quickly identify the nodes with significant differences in their attributes.

- The output will also show the total values for each network and the difference between them. This provides a high-level overview of the networks’ characteristics.

- Additionally, the output will provide statistics on the comparisons made. This includes the number of comparisons below 0.1%, the total number of comparisons made, and the percentage of comparisons below 0.1%. These statistics quantitatively measure the similarities and differences between the networks.

![](https://media.licdn.com/dms/image/v2/D4E12AQG6CDiu7jbhqg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721013010530?e=1795651200&v=beta&t=WtesJ35vUROPrjqH5NGyfRrGIGVq6t20jjcl0kZNvz4)

BN is different due to ground elevation differences for outfalls

> **Ruby Description**

> **Location of the Ruby Code**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0149 - Utilities/Compare InfoWorks to SWMM for Nodes](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0149%20-%20Utilities)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
