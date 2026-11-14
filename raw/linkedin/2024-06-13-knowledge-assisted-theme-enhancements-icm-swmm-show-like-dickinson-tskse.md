---
title: "Knowledge Assisted Theme Enhancements in ICM SWMM to Show InfoSWMM Like Map Displays for d/D and q/Q"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/knowledge-assisted-theme-enhancements-icm-swmm-show-like-dickinson-tskse
created: "2024-06-12 17:49"
published: "2024-06-13 00:33"
words: 594
export_sha256: 2dd6f22032595a36c20ac0a7c0e45e0b5ddc648a86eb695290f14503f93d80d1
---
# Knowledge Assisted Theme Enhancements in ICM SWMM to Show InfoSWMM Like Map Displays for d/D and q/Q

![Knowledge Assisted Theme Enhancements in ICM SWMM to Show InfoSWMM Map Displays for d/D and q/Q](https://media.licdn.com/mediaD4E12AQE5HrJV3t7uig "Knowledge Assisted Theme Enhancements in ICM SWMM to Show InfoSWMM Map Displays for d/D and q/Q")

This article demonstrates how to leverage the power of SQL and themes in ICM SWMM to create informative map displays similar to those found in InfoSWMM. Users can generate visually intuitive representations of their model's behavior by utilizing the d/D (depth over diameter) and q/Q (flow over capacity) values stored in the user number fields of the link grid. [As mentioned in this article](https://www.linkedin.com/feed/update/urn:li:ugcPost:7206469206765121537/), we imported the d/D and q/Q values from the SWMM5 report file of ICM SWMM using the Ruby script. [**Open-Source-Support**](https://github.com/innovyze/Open-Source-Support/tree/main) /[01 InfoWorks ICM/01](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM) Ruby/02 [](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby) SWMM/0151: Read SWMM5 RPT File. Now that we have imported these values into the Link Grid, we can do the following:.

> **1: You can use the SQL dialog to select links based on d/D or q/Q Q in this case is Manning's Qfull and D is the Full Pipe Depth.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFW22chAaiBhQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718217455992?e=1795651200&v=beta&t=WICnuqOp1bUbf5vN-QioaJQfyl7MFPGRrMFsqHts6Pg)

You can use the SQL dialog to select links based on d/D or q/Q Q in this case is Manning's Qfull and D is the Full Pipe Depth.

> **2: You can use the SQL dialog to make a table of the user numbers and/or user text fields.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHTqpYlJgIkoA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718236871044?e=1795651200&v=beta&t=OF4zA1qflp5EtjEV1D1d8BjqLr06zlGSEvHIyClGLKg)

You can use the SQL dialog to make a table of the user numbers and/or user text fields.

> **3: You can use the SQL dialog to select links based on d/D or q/Q. In this case, Q is Manning's Qfull, and D is the Full Pipe Depth, with the values shown as labels on the Geoplan.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFuFG3X-6lXkw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718236923987?e=1795651200&v=beta&t=kEVcl8fneyVcGTuzop9owE4IvXQNbfQGlllMCBL4UMc)

You can use the SQL dialog to select links based on d/D or q/Q. In this case, Q is Manning's Qfull, and D is the Full Pipe Depth, with the values shown as labels on the Geoplan.

> **4: How to use the Visual tab of the Geoplan to show the value of d/D or q/Q on the Geoplan.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGMDPB91Mgg-g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718236899272?e=1795651200&v=beta&t=jHCl9oy2UgGpGaxK5d7U5vv2RmK0vU8mYoU7GOZHm80)

How to use the Visual tab of the Geoplan to show the value of d/D or q/Q on the Geoplan.

> **5: Previous Post on reading SWMM5 Report Data**

\[embedded item\]

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQFIjjp_BhuXBw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718215067482?e=1795651200&v=beta&t=zvqjLPPuUx0a4rYEd5jHU0zGqfzXF-h0RwdeThAMTUw)

AI Image
