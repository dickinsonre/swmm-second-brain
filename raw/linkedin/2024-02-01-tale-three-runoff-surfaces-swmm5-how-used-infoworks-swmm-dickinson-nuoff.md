---
title: "A Tale of Three Runoff Surfaces in SWMM5 and how they are used in InfoWorks SWMM Hydrology"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/tale-three-runoff-surfaces-swmm5-how-used-infoworks-swmm-dickinson-nuoff
created: "2024-01-31 23:32"
published: "2024-02-01 02:37"
words: 530
export_sha256: cfc7c509b48bdc5988efa7ec49158cfb739007a0292c7c2f056a67275cdb2704
---
# A Tale of Three Runoff Surfaces in SWMM5 and how they are used in InfoWorks SWMM Hydrology

![Three Runoff Surfaces](https://media.licdn.com/mediaD4E12AQF6P6I-w5dgMA "Three Runoff Surfaces")

In SWMM5 and ICM SWMM, the modeling of runoff surfaces is intricately tied to the concept of percent imperviousness, particularly focusing on areas with and without depression storage within a subcatchment. This approach delineates two main types of surfaces based on their ability to temporarily store water. However, when we transition to InfoWorks SWMM Hydrology, this concept evolves to accommodate a more detailed representation.

In InfoWorks ICM, these runoff surfaces from SWMM5 are expanded into three distinct runoff surfaces. Each of these surfaces is intricately associated with the subcatchment through the Land Use ID. This progression allows for a more nuanced and detailed analysis of runoff, factoring in the varying characteristics of land use within a subcatchment. These sections define the progression.

> Section 1 What are the three surfaces in SWMM5?

The three surfaces are impervious with depression storage, impervious without depression storage, and pervious with depression storage. However, these three surfaces are defined by their percent imperviousness and the percent of the impervious surface that has no depression storage. Pervious is 100 percent minus Percent Impervious. Here is the SWMM5 subcatchment data.

![](https://media.licdn.com/dms/image/v2/D4E12AQH9qL823rcTEw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706747768281?e=1795651200&v=beta&t=lHeC1189wzCjw8Ev6h3auQEFqRfONTmsgUOw973ibyM)

Three surfaces in SWMM5

> Section 2. How does this look in ICM SWMM?

The subcatchment is 23 percent impervious, and 25 percent of the 23 percent has no depression storage. The pervious area is 77 percent.

![](https://media.licdn.com/dms/image/v2/D5612AQFeP6gjLnBeGA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1706751665629?e=1795651200&v=beta&t=eS34wUh5et5ezXzHUXJGEAiOqVzVAeBEd9qZYawpi4A)

ICM SWMM Subcatchment Properties

> Section 3. How does this look in ICM InfoWorks?

We convert ICM SWMM to ICM InfoWorks internally. InfoWorks has three runoff surfaces of 17.250, 5.750 and 77.00 percent for impervious, impervious with no depression storage and pervious. This matches the percentage from SWMM.

![](https://media.licdn.com/dms/image/v2/D5612AQG5FrT5_dLxgQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1706751921321?e=1795651200&v=beta&t=mvJa68YlLIe635sHR0fBEtQRA9Wnd7byFKGfviYDt-A)

ICM InfoWorks Subcatchment Data

> Section 4. Runoff Surfaces in ICM InfoWorks.

The converted InfoWorks network now has three runoff surfaces in the runoff surface grid. **Bullet 1** is the impervious area with depression storage; **Bullet 2** is the impervious area without depression storage; and **Bullet 3** is the pervious area with depression storage. All use SWMM runoff. The depression is now called initial loss value.

![](https://media.licdn.com/dms/image/v2/D4D12AQEz5TgJ8yhatw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706753431331?e=1795651200&v=beta&t=HDczy5qoXqK_9FPYIcEBRdZgy6Bk3WwWoBjjgNXzD0o)

ICM InfoWorks Runoff Surface to match the SWMM5 Three Runoff Surfaces

![](https://media.licdn.com/dms/image/v2/D4D12AQFC0tllx2YxrA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706753792131?e=1795651200&v=beta&t=GnlhHYbo40bqwrpGKDlR22qWNAsrO0kGCTXzY3LK4zA)

The InfoWorks Landuse Ties the Three Runoff Surfaces Together.

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
