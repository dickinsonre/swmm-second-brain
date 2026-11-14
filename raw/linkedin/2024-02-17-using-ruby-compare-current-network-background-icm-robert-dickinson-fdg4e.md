---
title: "Using Ruby to Compare the Current Network to a Background Network in ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-compare-current-network-background-icm-robert-dickinson-fdg4e
created: "2024-02-17 22:48"
published: "2024-02-17 23:54"
words: 417
export_sha256: 229ba36b3f610ebc9b0314bf2eb8cb8cb2c7057cc1829aa8a0144740156b9c26
---
# Using Ruby to Compare the Current Network to a Background Network in ICM InfoWorks

![Current and Background Networks in ICM InfoWorks ](https://media.licdn.com/mediaD4E12AQGcjKG92P7RNA "Current and Background Networks in ICM InfoWorks ")

ICM (InfoWorks ICM) offers a valuable feature that allows users to maintain a current network alongside a background network. This functionality is particularly useful for comparing models, whether they are newly imported, converted from other formats, or undergoing revisions. As part of our I2S (InfoCare to Subscription) plan, we facilitate the conversion of models from InfoSWMM to ICM SWMM, as well as from InfoSewer and XPSWMM to ICM InfoWorks. However, these pathways represent just a fraction of the conversion capabilities available.

In addition to the direct conversions mentioned, users have the flexibility to import models from SWMM5 or PCSWMM directly into ICM SWMM. Furthermore, it's possible to convert between ICM SWMM and ICM InfoWorks, allowing for a broad range of model interoperability and adaptation to various project needs.

Given that some of these models can be extensive, featuring numerous components, it becomes invaluable to have tools for detailed comparison and analysis. Utilizing Ruby scripts, users can efficiently count and compare model elements, such as inflows and loads, across different versions or conversions of a model. This capability is essential for ensuring accuracy and consistency in model data following conversions or updates.

This blog aims to demonstrate how to leverage data flags within ICM, a critical feature that facilitates the comparison of models. Data flags serve as markers or indicators that can be used to highlight specific conditions or attributes within the model data, making them an indispensable tool for detailed analysis and comparison. Through simple flag comparisons, users can swiftly identify differences or anomalies between models, enhancing the overall model management and quality assurance process.

> **Ruby Code to interrogate both the current and background network in one script**

The following code calls both WSApplication.current_network and WSApplication.background_network in one go to compare tables and in this case count the flags used in both networks.

![](https://media.licdn.com/dms/image/v2/D4E12AQHsYNdPNDCTvw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708212124331?e=1795651200&v=beta&t=k11AFp_s2ldi5BF-aN24R32IbkLrxfpWB-OzHgn-RuY)

**The flags and the count of the flags for both current and background networks**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
