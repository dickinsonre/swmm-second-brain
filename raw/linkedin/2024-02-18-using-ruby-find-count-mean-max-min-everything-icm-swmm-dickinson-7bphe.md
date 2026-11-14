---
title: "Using Ruby to find the Count, Mean, Max and Min of Everything in an ICM InfoWorks or SWMM Network"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-find-count-mean-max-min-everything-icm-swmm-dickinson-7bphe
created: "2024-02-18 09:38"
published: "2024-02-18 14:22"
words: 406
export_sha256: c3d6ac4589652c94199c7c1263b8094b2d417b4313f0e1039a250a192da5fa2c
---
# Using Ruby to find the Count, Mean, Max and Min of Everything in an ICM InfoWorks or SWMM Network

![Using Ruby to find the count, mean, max and min of everything in an ICM InfoWorks or SWMM Network](https://media.licdn.com/mediaD4E12AQHIVkY46vqx-Q "Using Ruby to find the count, mean, max and min of everything in an ICM InfoWorks or SWMM Network")

When delving into the intricate process of comparing imported or transformed networks within ICM, discerning anomalies or unconventional data can often present a significant challenge. Traditional validation and network commitment protocols primarily excel at identifying errors and suspicious data entries, yet may fall short when it comes to uncovering atypical model parameters or unique element data within a network component. In this context, the utilization of Ruby scripts emerges as a formidable solution, offering the capacity to meticulously analyze and aggregate data across a broad spectrum. This includes the enumeration, as well as the determination of minimum, average, and maximum values, encompassing both numeric and non-numeric data such as flags and model options.

Such a comprehensive approach facilitates the discovery of the proverbial "needle in a haystack" within a modeling database, making it an invaluable asset for those seeking to thoroughly scrutinize ICM InfoWorks and ICM SWMM networks. Remember, that within the domain of ICM InfoWorks, the prefix 'hw\_' pays homage to its HydroWorks lineage, whereas 'sw\_' denotes an affiliation with SWMM, underscoring the versatile applicability of these methodologies in enhancing model accuracy and integrity.

Note, the non numeric data includes the MESHING SUMMARY and any data not in a grid.

> **Ruby Code - Simple and with comments - Thanks CoPilot!**

> **Count, Mean, Max and Min of Everything in an ICM InfoWorks Network**

![](https://media.licdn.com/dms/image/v2/D4E12AQGoiVXwR0v0lA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708253363326?e=1795651200&v=beta&t=v0BSyKUlD8g89SghjQ2plOtChObQ5sVlu09aGfqZhXw)

Table 1. Count, Mean, Max and Min of Everything in an ICM InfoWorks Network

> **Count, Mean, Max and Min of Everything in an ICM SWMM Network**

![](https://media.licdn.com/dms/image/v2/D4E12AQFTC7oF03X9Tw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708253447275?e=1795651200&v=beta&t=S9PQmscwzWelEocTm9Dai1XMg6DFBzUg0ey-hsQ42Q0)

Table 2. Count, Mean, Max and Min of Everything in an ICM SWMM Network

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
