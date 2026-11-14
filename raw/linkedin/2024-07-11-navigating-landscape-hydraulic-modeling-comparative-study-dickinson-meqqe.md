---
title: "Navigating the Landscape of Hydraulic Modeling: A Comparative Study of InfoSewer, ICM InfoWorks, and ICM SWMM for Steady State Models"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/navigating-landscape-hydraulic-modeling-comparative-study-dickinson-meqqe
created: "2024-07-11 13:17"
published: "2024-07-11 13:53"
words: 393
export_sha256: f6fccf00e9352beee8f2400f94192c14710bb18f47d821ebca52c39b73f87e69
---
# Navigating the Landscape of Hydraulic Modeling: A Comparative Study of InfoSewer, ICM InfoWorks, and ICM SWMM for Steady State Models

![Navigating the Landscape of Hydraulic Modeling: A Comparative Study of InfoSewer, ICM InfoWorks, and ICM SWMM for Steady State Models](https://media.licdn.com/mediaD4E12AQFs2kFZy7-V5w "Navigating the Landscape of Hydraulic Modeling: A Comparative Study of InfoSewer, ICM InfoWorks, and ICM SWMM for Steady State Models")

This article explores the interoperability and comparative performance of three hydraulic models: InfoSewer, ICM InfoWorks, and ICM SWMM.

We begin with a core model developed in InfoSewer for training purposes. We then guide you through a series of transformations and comparisons:

1.  Model Conversion: The InfoSewer model is converted to ICM InfoWorks, demonstrating the process and validating flow consistency.

2.  SWMM Integration: We converted the model to SWMM format using ICM InfoWorks' internal menu tool, showcasing the software's built-in conversion capabilities.

3.  Comparative Analysis: Leveraging Ruby scripting, we compare the ICM InfoWorks (current) and SWMM (background) networks, highlighting key differences and necessary adjustments.

4.  Model Refinement: We optimize the SWMM model in detail, including subcatchment modifications and the transfer of trade flows from InfoWorks to SWMM.

5.  To get close to InfoSewer's steady-state model, the ICM InfoWorks and SWMM models are changed to use ICM's saved state feature and short simulation runs.

Throughout this process, we uncover valuable insights into each platform's strengths and limitations. Notably, ICM InfoWorks provides a more accurate approximation of the steady-state condition compared to SWMM.

![](https://media.licdn.com/dms/image/v2/D4E12AQFi0Pp7Xf1wOg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720703907256?e=1795651200&v=beta&t=OMy92dwlg2_8MKnnHQnqQzhFWXyg5bCktefY8zEB9_k)

Steady State model in ICM Infoworks and ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQFuTAFUmagXMw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720704034430?e=1795651200&v=beta&t=e7kBNe-gJ7XjdGhsKjtT6REx2MnUUFrpRHkgyBNjM3A)

Comparative Analysis: Leveraging Ruby scripting, we compare the ICM InfoWorks (current) and SWMM (background) networks, highlighting key differences and necessary adjustments.

> **Ruby scripting for cn vs bn networks**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
