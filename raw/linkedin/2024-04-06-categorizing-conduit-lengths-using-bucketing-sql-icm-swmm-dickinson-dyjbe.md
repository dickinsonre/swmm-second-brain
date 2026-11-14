---
title: "Categorizing Conduit Lengths Using Bucketing in SQL for ICM InfoWorks and SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/categorizing-conduit-lengths-using-bucketing-sql-icm-swmm-dickinson-dyjbe
created: "2024-03-28 02:47"
published: "2024-04-06 13:17"
words: 662
export_sha256: 26a9c8b6b59edfb987927383e27eebd1d5201c18469a6aff47309dc0904ca8ca
---
# Categorizing Conduit Lengths Using Bucketing in SQL for ICM InfoWorks and SWMM Networks

![Categorizing Conduit Lengths Using Bucketing in SQL for ICM InfoWorks and SWMM Networks ](https://media.licdn.com/mediaD4E12AQHvR6tY2oiStA "Categorizing Conduit Lengths Using Bucketing in SQL for ICM InfoWorks and SWMM Networks ")

**Analyzing Conduit Characteristics with InfoWorks ICM**

As a hydraulic modeling professional, one of the key tasks is to understand the characteristics of the conduit network in our models. InfoWorks ICM's powerful SQL capabilities allow you and **me** to perform in-depth analyses and categorize conduits based on various attributes.

In this post, I share a SQL script that groups conduits into buckets based on their length, width, upstream invert level, capacity, and gradient. This analysis can provide valuable insights for network optimization, maintenance planning, and design validation.

By leveraging the RINDEX function and user-defined list variables, we can categorize conduits into meaningful buckets based on their attributes. The TITLE function ensures that the grouped results display the actual bucket values instead of indexes, enhancing readability. **Note** - all of this is on our open source GitHub which you can find using this I[CM Hub link.](https://boards.autodesk.com/icm)

![](https://media.licdn.com/dms/image/v2/D4E12AQGCUL_w6aPYiA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1712408805390?e=1795651200&v=beta&t=DNWAWciaNaKvpD2NiBlGhUIL0e1hh5NLcxgZ6fGY15U)

All of the SQL, Bucket and RINDEX Tables Generated

## 1. Define the Buckets (in meters, cms or mm)

This line defines a list of buckets in the appropriate units (you need to know the units from the ICM Interface). The script will categorize the conduit lengths based on these predefined buckets.

## 2. Query for Bucket Categorization with SQL RINDEX

: This function counts the number of conduits in each length bucket.

- : This clause groups the conduit lengths based on the defined buckets.

- : This expression categorizes the values into the appropriate length buckets using the function, which returns the index of the largest bucket value that is less than or equal to the . The function is used to display the bucket values as the column header.

- : This aliases the grouped column with a user-friendly name, "Length (meters)"

## 3. What it looks like in the SQL ICM Interface

![](https://media.licdn.com/dms/image/v2/D4E12AQHY2H6oXBJzHg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1712408680621?e=1795651200&v=beta&t=9mH_WrGdv1cJTXIVvKs95unuiMYaOW2UqSNnEmFIQaw)

SQL ICM Interface

## 4. All of the SQL code together

![](https://media.licdn.com/dms/image/v2/D4E12AQESJVOpgMtGxw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1712409261279?e=1795651200&v=beta&t=jOrsvmfHwz-1hH4Zd2uga2mcIT5pla4q6svku7MtJq0)

**Not an SQL Bucket.**

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
