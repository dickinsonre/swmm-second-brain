---
title: "Subcatchment Subarea Internal Routing in SWMM5, ICM SWMM, and ICM InfoWorks Networks - Key Parameters"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/subcatchment-subarea-internal-routing-swmm5-icm-swmm-dickinson-ebepe
created: "2023-06-19 12:53"
published: "2024-02-03 02:32"
words: 591
export_sha256: 7eddf4fba7d10dc951a7289d19b4a6f4fa22a6ceb6ba162ec9bc885630657e74
---
# Subcatchment Subarea Internal Routing in SWMM5, ICM SWMM, and ICM InfoWorks Networks - Key Parameters

![Test Networks for ICM SWMM and ICM InfoWorks Subarea Routing using SWMM5 Parameters](https://media.licdn.com/mediaD4E12AQH2oktupB0wGQ "Test Networks for ICM SWMM and ICM InfoWorks Subarea Routing using SWMM5 Parameters")

### Subcatchment Subarea Routing in SWMM5, ICM SWMM, and ICM InfoWorks Networks: Testing with Examples

> **1/** Subarea Routing in SWMM5

In SWMM5, the routing of the runoff between pervious and impervious subareas can be configured using three options:

1.  **IMPERV**: This option allows the runoff from the pervious area to flow toward the impervious area.

2.  **PERV**: This option allows the runoff from the impervious area to flow towards the pervious area.

3.  **OUTLET**: This option allows the runoff from both areas to directly flow towards the outlet.

The proportion of runoff that is routed between the subareas can be defined by the user through a parameter called "Percent Routed". For instance, if the percent routed is set to 20%, then 20% of the runoff will flow from one area to the other (as determined by the IMPERV or PERV setting), and the remaining 80% will flow directly to the outlet.

However, if the percent routed is set to zero, then 100% of the runoff from both pervious and impervious areas will be directed to the outlet, bypassing any routing between the two areas. This flexibility allows for a more accurate representation of real-world runoff patterns.

![](https://media.licdn.com/dms/image/v2/D4E12AQEsUbf9ajqxSQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1687188233367?e=1795651200&v=beta&t=eGAVfJEJxTVvwSKUzgLlHSE23gBZtZhCXb9UJq0-vvE)

IMPERV: runoff from the pervious area flows to the impervious area PERV: runoff from impervious flows to pervious area OUTLET: runoff from both areas flows directly to the outlet Percent Routed Percent of runoff routed between subareas.

> **2/** In an ICM InfoWorks network there are also three options for routing:

Choose the method by which the surface of the subcatchment is to drain. Set to:

**Direct:** This option allows the surface of the subcatchment to drain directly to the outlet of the subcatchment.

**To pervious:** This option allows the impervious surfaces of the subcatchment to drain to the pervious surfaces of the same subcatchment.

**To impervious:** This option allows the pervious surfaces of the subcatchment to drain to the impervious surfaces of the same subcatchment.

![](https://media.licdn.com/dms/image/v2/D4E12AQFyL4OJC7N8jg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1687195068297?e=1795651200&v=beta&t=GQ1AcHgYOu98b3rZZrTZEjEWAR2DPKGDMA3ZETJdFnk)

InfoWorks Network Options, Feature added for What's New in Version 6.5 - November 2015

> **3/** Two Test Networks ICM SWMM and ICM InfoWorks each with three Scenarios.

![](https://media.licdn.com/dms/image/v2/D4E12AQEIRGQlaoH3hQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1687195691982?e=1795651200&v=beta&t=XXR57OcOFiTFwWw5x8DMk4y5jhn1FWoE7CimZRICbKA)

Two Test Networks ICM SWMM and ICM InfoWorks each with three Scenarios.

> **4/** ICM SWMM and ICM InfoWorks Direct Import Scenario

Outlet in SWMM, Direct in InfoWorks

![](https://media.licdn.com/dms/image/v2/D4E12AQErDqEpawU06Q/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1706927218201?e=1795651200&v=beta&t=JT9mN5SRY_D1Pin_cuBLXAwc3HJiOZ9KuW1BeHSzGJw)

Outlet in SWMM, Direct in InfoWorks

> **5/** ICM SWMM and ICM InfoWorks Impervious to Pervious Scenario

Impervious in SWMM, Impervious to Pervious in InfoWorks

> **6/** ICM SWMM and ICM InfoWorks Pervious to Impervious Scenario

Pervious in SWMM, Pervious to Impervious in InfoWorks

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
