---
title: "Ruby ICM InfoWorks vs. ICM SWMM Link Property Data Comparison"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/ruby-icm-infoworks-vs-swmm-link-property-data-robert-dickinson-uanie
created: "2024-03-23 22:13"
published: "2024-07-15 09:10"
words: 799
export_sha256: 0bbad23111d3b1e56028dce114b246e5ba15f1d0a37479ca535cafe204d1dfdb
---
# Ruby ICM InfoWorks vs. ICM SWMM Link Property Data Comparison

![Ruby ICM InfoWorks vs. ICM SWMM Link Property Data Comparison ](https://media.licdn.com/mediaD4E12AQEAB_b9_H2adg "Ruby ICM InfoWorks vs. ICM SWMM Link Property Data Comparison ")

The ICM Infoworks and SWMM Network Comparison Tool for Conduits is a Ruby script designed to bridge the gap between two prominent hydraulic modeling systems within the Integrated Catchment Modeling (ICM) environment. This tool enables engineers and modelers to compare InfoWorks HW Conduits and SWMM SW Conduits, providing invaluable insights into the similarities and differences between these network representations.

At its core, the tool leverages ICM's dual-network capability, utilizing the current network (CN) for ICM Infoworks and the background network (BN) for ICM SWMM. This setup allows for a direct, side-by-side comparison of conduit attributes across both modeling paradigms. The script offers a user-friendly interface that allows modelers to select specific attributes for comparison, ranging from basic geometric properties like conduit length, height, and width to more specialized parameters such as invert levels, headloss coefficients, and roughness values.

The comparison process is both comprehensive and efficient. The tool creates a hash map of SWMM conduit attributes for each selected attribute and systematically compares them to their InfoWorks counterparts using unique conduit IDs. This approach ensures a precise, one-to-one comparison between the two networks. The script is designed to highlight significant discrepancies, focusing on differences greater than 0.1%, and provide overall statistics on the comparison results.

What sets this tool apart is its ease of handling large networks. It provides detailed individual conduit comparisons and high-level statistical summaries. This dual approach allows users to quickly identify systemic differences between the two network representations while pinpointing specific conduits that may require further investigation or adjustment.

By facilitating this detailed comparison between InfoWorks and SWMM conduits, the tool saves time and enhances the accuracy and reliability of hydraulic modeling efforts. It's invaluable for engineers and modelers working across multiple hydraulic modeling platforms. It offers insights that can lead to more informed decision-making, improved model consistency, and, ultimately, more accurate hydraulic simulations.

![](https://media.licdn.com/dms/image/v2/D4E12AQFXqMcVTOibzg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721033490700?e=1795651200&v=beta&t=HGtTRwCAmk1WdRjMwh0kYNpnpfbzCWJ0goIqQTVqYAU)

Ten possible comparisons between InfoWorks HW Condut Tables and SWMM SW Condut Tables

> Ruby Script Output

The ICM Infoworks and SWMM Network Comparison Tool for Conduits offers a comprehensive set of attribute pairs for comparison, covering essential aspects of conduit geometry and hydraulic characteristics. These pairs include conduit length, height, width, and number of barrels, which are crucial for understanding the physical structure of the drainage system. The tool also compares upstream and downstream invert levels, headloss coefficients, and roughness values (bottom and top roughness for Infoworks vs. Manning's N for SWMM), which helps you understand how the conduits behave hydraulically on both platforms.

The comparison process is methodical and efficient. The tool iterates through the selected attributes, creating a hash map of SWMM (SW) attributes indexed by conduit ID for quick access. It then compares these to the corresponding Infoworks (HW) attributes, using the conduit ID as a common identifier. This approach ensures a precise, one-to-one comparison between the two networks. The script calculates and displays the differences between attribute values, focusing on significant discrepancies.

The tool's output is designed to be detailed and summarized, catering to different analysis needs. It highlights conduits where the difference in attribute values exceeds 0.1%, allowing users to identify areas of significant disparity quickly. The tool also provides a broader perspective by displaying totals for each network and the overall difference. Furthermore, it generates valuable statistics on the comparisons, including the number and percentage of comparisons below the 0.1% threshold and the total number of comparisons made. This output helps users understand the specific differences and the overall consistency between the network representations, which makes it easier to make smart choices in hydraulic modeling projects.

![](https://media.licdn.com/dms/image/v2/D4E12AQGDCkigBCZh-A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721033288268?e=1795651200&v=beta&t=eCSZeCX0uAn7S65vZuPuF3EAzKyJ73p7O796XUY6R2Q)

**Ruby Script Output**

> **Ruby Description**

> **Location of the Ruby Code**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0149 - Utilities/Compare InfoWorks to SWMM for Links](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0149%20-%20Utilities)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
