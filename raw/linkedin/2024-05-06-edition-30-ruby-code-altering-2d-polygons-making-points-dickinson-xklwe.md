---
title: "Edition 30: Ruby Code for Altering 2D Polygons, Making 2D Results Points Inside the Polygon for both ICM InfoWorks and SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-30-ruby-code-altering-2d-polygons-making-points-dickinson-xklwe
created: "2024-03-23 21:57"
published: "2024-05-06 14:54"
words: 1044
export_sha256: 214fa128cb543a877a8c147ffa8fa96ee6c61461b2f92776a2fe56b8a5c3413e
---
# Edition 30: Ruby Code for Altering 2D Polygons, Making 2D Results Points Inside the Polygon for both ICM InfoWorks and SWMM Networks

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Ruby Code for Altering 2D Polygons, Making Many 2D Results Points Inside the Polygon for both ICM InfoWorks and SWMM Networks](https://media.licdn.com/mediaD5612AQG1g8ZK-hghcg "Ruby Code for Altering 2D Polygons, Making Many 2D Results Points Inside the Polygon for both ICM InfoWorks and SWMM Networks")

**Edition 30:** Ruby Code for Altering 2D Polygons, Making Many 2D Results Points Inside the Polygon for both ICM InfoWorks and SWMM Networks

As part of our **asymmetrical creation** of Ruby examples for the thousands of ICM InfoWorks and ICM SWMM network input and output parameters, we now turn our attention to 2D polygons. In this section, we will cover the 2D polygons that can be used in both SWMM and InfoWorks networks, highlighting the fact that while the same 2D engine is used in both networks, ICM InfoWorks has more 2D polygons.

Next, we will explore how to create arbitrary polygon shapes using Ruby code. We will present sample Ruby code snippets that demonstrate how to generate custom polygon shapes and explain how these polygons can be integrated into SWMM and InfoWorks networks. This will showcase the flexibility and power of using Ruby to create complex 2D geometries within these networks. **You might wonder way - it is for testing and teaching purposes where having uniform shapes looks nicer - IMO.**

Furthermore, we will delve into the process of adding 2D Result points within the created polygons. We will describe the steps involved in placing these points inside the polygons and highlight the importance of these points for analyzing data within the polygons. This will enable users to extract valuable insights from the data associated with hydrology and hydraulic processes inside the 2D polygons.

Finally, we will demonstrate how to analyze statistics and graphs using the 2D Result points. We will show how to extract and process data from these points and provide examples of the types of statistics and graphs that can be generated using this data. This will empower users to gain a deeper understanding of the behavior and characteristics of the 2D polygons within their ICM InfoWorks and ICM SWMM networks.

> **1/ End Result - the 2D Polygon Boundaries are Symmetrical and Many 2D Results Points have been Added.**

![](https://media.licdn.com/dms/image/v2/D4E12AQE7qvzCpkybAw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715003994152?e=1795651200&v=beta&t=k8esnrQ1cZiOkkgXFY8cVg1zaoZ0z43J6FqGDVzYS1Q)

The Polygon Shapes are Changed and a User Defined new 2D Result points have been added

> **2/ What 2D Networks can have their boundaries altered by Ruby?**

Here is the list - most use the boundary array but some use leve_sections (Buildings for example) and the Ruby Code cannot alter the boundaries.

> **3/ What do the Shapes Look like Before?**

They are mouse drawn and do not look organized. I could have imported the polygon shapes from GIS if I wanted the shapes to touch the boundaries.

![](https://media.licdn.com/dms/image/v2/D4E12AQEFAXM3x8gXzA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714949485857?e=1795651200&v=beta&t=CFaRhmd4EddfXLUOJ_rTqZQ7zH82jHt0A3LD53A9aD8)

**The 2D Polygons are mouse drawn on the screen**

> **4/ What do the 2D Polygon Shapes look like after?**

All of the eight highlighted polygons now have a new symmetrical polygon boundary. The code will change any selected polygon at the same time.

![](https://media.licdn.com/dms/image/v2/D5612AQEv44YCeSCMzQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715006124468?e=1795651200&v=beta&t=kqgzPBx8RvrigwWZFBKcZiC_KLGUamcpLXt0hnPOvLU)

All of the eight highlighted polygons now have a new symmetrical polygon boundary.

> **5/ A 2nd Pass with new Ruby code will add 2D Results points in Square - User Defines the Number of Points**

![](https://media.licdn.com/dms/image/v2/D5612AQGRqORnQtI5bw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715006416290?e=1795651200&v=beta&t=IXPNBNNhK-b2BJ90PUtQdzC3FXd8BDMqGC3g_R_c_XI)

**A 2nd Pass with new Ruby code will add 2D Results points in Square - User Defines the Number of Points**

> **6/ After Remeshing the 2D Results point can be graphed and used in Tables, SQL or Ruby Statistics - Simulation must be run again**

![](https://media.licdn.com/dms/image/v2/D5612AQEhmXeXYEEz9Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715006542229?e=1795651200&v=beta&t=ua1qAavwGsmBtqUpWUudapv4hGu-OuJH7-g7ovHZG-M)

**After Remeshing the 2D Results point can be graphed and used in Tables, SQL or Ruby Statistics**

![](https://media.licdn.com/dms/image/v2/D4E12AQEo27yxee0cQg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715006646381?e=1795651200&v=beta&t=0c3KnvAiTIJc_P2tghqy-wR-WyGfWBetlTlMzOTNO5k)

**After Remeshing the 2D Results point can be graphed and used in Tables, SQL or Ruby Statistics**

> **7/ The Ruby Code for Changing the Boundaries**

**8/ The Ruby Code for adding ten points per row in a Square**

![](https://media.licdn.com/dms/image/v2/D4E12AQFPAuFaFJLbcA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714770934896?e=1795651200&v=beta&t=9yGcvL-2xxOXPcKY2EsWu8DsPBa0vtP8_eeH3eTns1U)

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133, or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers
