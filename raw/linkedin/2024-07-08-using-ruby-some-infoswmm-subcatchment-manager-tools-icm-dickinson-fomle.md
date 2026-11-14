---
title: "Using  Ruby for some InfoSWMM Subcatchment Manager Tools In ICM Infoworks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-some-infoswmm-subcatchment-manager-tools-icm-dickinson-fomle
created: "2024-07-08 02:23"
published: "2024-07-08 03:00"
words: 485
export_sha256: 1d94add65998b37fd379ed133e6d6891f84190619c66a6814327afe5b597bdd3
---
# Using  Ruby for some InfoSWMM Subcatchment Manager Tools In ICM Infoworks

![Using Ruby for some InfoSWMM Subcatchment Manager Tools In ICM Infoworks](https://media.licdn.com/mediaD4E12AQEQ_9YtGZFXVQ "Using  Ruby for some InfoSWMM Subcatchment Manager Tools In ICM Infoworks")

Navigating the complexities of stormwater management often involves working with specialized software and tools. As we approach 2025, the impending discontinuation of InfoSWMM and Arc Map tools brings significant changes. One crucial area of focus is the width calculations for SWMM5 or SWMM, which are essential for **SWMM Hydrology in ICM SWMM and ICM InfoWorks.**

The options available in InfoSWMM Subcatchment Manager for calculating the width are diverse, allowing users to tailor their approach to specific project needs. These include:

\- Width = 1.7 \* Max(Height,Width)

\- Width = K \* SQRT(Area)

\- Width = K \* Perimeter

\- Width = Area / Flow Length

These methods offer flexibility and precision, ensuring that each subcatchment's unique characteristics are adequately addressed. However, with the transition from InfoSWMM, capturing these critical calculations is more important than ever.

Using Ruby scripting in ICM lets users automate and save these width calculations. This makes the transition easier and keeps hydrologic modeling practices consistent. This scripting capability enhances efficiency and provides a robust framework for managing the changes ahead.

In the following sections, we will explore how to use Ruby for some of the InfoSWMM Subcatchment Manager tools in ICM InfoWorks, ensuring that the essential width or dimension calculations are seamlessly integrated into your workflow.

![](https://media.licdn.com/dms/image/v2/D4E12AQEd9YO55xFh6w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720407389237?e=1795651200&v=beta&t=m8qSsrLcJl-cXUiIiPRIvOBjpE6yRdoyfXX5tzU61ss)

The Dimension in ICM InfoWorks or the Width in ICM SWMM is being changed

![](https://media.licdn.com/dms/image/v2/D4E12AQHUrGTV6YIQgA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720407267312?e=1795651200&v=beta&t=4H6szdy0pXPcp89dIzEg0DcSwsySfIQYSVaGqqf7i_o)

The options for Ruby in an ICM InfoWorks Network

![](https://media.licdn.com/dms/image/v2/D4E12AQEda2QU3ZvLtw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720405594858?e=1795651200&v=beta&t=oDnSfYJKj8flANql63SERpwuPKx87x9eKF2ZjmJib08)

The options in InfoSWMM Subcathment Manager for Width

![](https://media.licdn.com/dms/image/v2/D4E12AQHp2JUdSDvg7w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720405712348?e=1795651200&v=beta&t=sNXj8quCaxXrAFXrUHwGe741r-qTDx_hMUu4ib2cp24)

The output of the Ruby Script with new totals for dimension or width

[01 InfoWorks ICM/01 Ruby/02 SWMM/0154 - Ruby for some InfoSWMM Subcatchment Manager Tools](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0154%20-%20Ruby%20for%20some%20InfoSWMM%20Subcatchment%20Manager%20Tools)

> **Ruby Code Description**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
