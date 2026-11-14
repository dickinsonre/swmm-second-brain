---
title: "Using Ruby to QA/QC InfoSWMM DWF Import to ICM SWMM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-qaqc-infoswmm-dwf-import-icm-swmm-robert-dickinson-a8woe
created: "2024-04-20 15:59"
published: "2024-05-19 20:50"
words: 717
export_sha256: dab6247532d456577665c116559a4fab83182fdf5ee35b4f6db3ff4b3de36b71
---
# Using Ruby to QA/QC InfoSWMM DWF Import to ICM SWMM

![Using Ruby to QA/QC InfoSWMM DWF Import to ICM SWMM](https://media.licdn.com/mediaD4E12AQGHuZZY1J-QnQ "Using Ruby to QA/QC InfoSWMM DWF Import to ICM SWMM")

In this tutorial, we will demonstrate a reverse-order step to show that the dry weather flow (DWF) in an ICM SWMM scenario is equivalent to the DWF in an InfoSWMM scenario. We will use Ruby and the direct import of InfoSWMM data into ICM SWMM using the Open Data Import Center (ODIC) and the import menu of the ICM UX.

Proving data consistency across different programs can be challenging due to variations in user experiences (UX) and interfaces. However, by following this step-by-step guide, we aim to provide a clear and concise demonstration of the data equivalence between the two programs.

Our approach will start at the end result, showcasing the matching DWF values in both ICM SWMM and InfoSWMM scenarios. From there, we will work backwards, detailing the process of using Ruby and the ODIC to import InfoSWMM data directly into ICM SWMM.

By the end of this tutorial, you will have a solid understanding of how to verify data consistency between ICM SWMM and InfoSWMM, as well as the tools and techniques used to accomplish this task.

> **6: End DWF in ICM SWMM**

Ruby Script shows the total DWF is 10.73 as an total flow in MGD.

![](https://media.licdn.com/dms/image/v2/D4E12AQFMdGQoFnqy0Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1716150891667?e=1795651200&v=beta&t=QrOLj4TucrKTSe90TNd0-KS5upwQJURxdNbvTk21Luw)

End DWF in ICM SWMM

> **5: DWF from the DWF Table inside of InfoSWMM for the Same Scenario**

![](https://media.licdn.com/dms/image/v2/D4E12AQHhD9vrAKMIBw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1716151053921?e=1795651200&v=beta&t=lgW5N82FXKxDk4xfirq8P25W0Z42D6CINxyL2rWi2FQ)

InfoSWMM Statistics tool shows a total of 10.71 MGD

> **4: Ruby Code to read the DWF.DBF file in the future (if InfoSWMM can no longer be used)**

![](https://media.licdn.com/dms/image/v2/D4E12AQG538ozB1WZYA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1716151276623?e=1795651200&v=beta&t=T6y_f7XZKeCKdBx97AIbwYPXR6BJyL1PDuNKaL9ezN8)

Ruby Script shows the total DWF is 10.73 as an total flow in MGD.

> **3: Why is this needed?** EPASWMM5 is restricted to only **one Dry Weather Flow (DWF) per node**

EPASWMM5 is restricted to only **one Dry Weather Flow (DWF) per node**, which can be limiting when modeling complex urban drainage systems. In contrast, InfoSWMM, through its GIS-based DWF Allocator tool, introduced the capability to allocate multiple DWF inputs per node, expanding the model's adaptability to simulate real-world conditions more accurately. This feature is further enhanced by additional simulation engine capabilities that support more than one row of DWF per node, allowing for a more detailed and nuanced representation of dry weather contributions to the system.

Building on the advancements in InfoSWMM, ICM SWMM incorporates these enhanced engine features, offering similar flexibility in handling multiple DWF inputs. However, within the ICM SWMM user interface, the original EPASWMM5 limitation is mirrored by designating a single DWF per node as DWF Baseflow, while supplementary DWF inputs are categorized under Additional DWF as Baseline Flow. Both primary and additional DWF inputs can utilize daily, weekend, weekday, and monthly patterns for a comprehensive temporal analysis. Importantly, these patterns, once defined in InfoSWMM, can be seamlessly transferred to an ICM InfoWorks Network, ensuring consistency in modeling approaches across platforms.

In the node dialog, ICM SWM Additional DWF for DWF more than one loading per node

![](https://media.licdn.com/dms/image/v2/D4E12AQEkkNjBm9fw3g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1716151510048?e=1795651200&v=beta&t=d9cwHo6o--PrqxI7W1IAtgU01aOUlxMB6_PhzLNWlqM)

In the node dialog, ICM SWM Additional DWF for DWF more than one loading per node

> ** 2: Ruby code for reading the DWF.DBF file from InfoSWMM**

> **1: Ruby code for reading the DWF in ICM SWMM**

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of **2025** in Autodesk terms).
