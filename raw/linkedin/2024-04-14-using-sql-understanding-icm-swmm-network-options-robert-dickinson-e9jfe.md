---
title: "Using SQL for Understanding ICM SWMM Network Options"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-sql-understanding-icm-swmm-network-options-robert-dickinson-e9jfe
created: "2024-03-28 02:46"
published: "2024-04-14 18:09"
words: 744
export_sha256: 8ee88c2dea03257a8df7436f9a005e2b7aa6d8ddd05e03a1b07b41ba17e622a8
---
# Using SQL for Understanding ICM SWMM Network Options

![Using SQL for Understanding ICM SWMM Network Options](https://media.licdn.com/mediaD4E12AQHYS2hTB4anSg "Using SQL for Understanding ICM SWMM Network Options")

Using SQL for Understanding the ICM SWMM Network Options

As water resources engineers and modelers, we rely on powerful tools like InfoWorks ICM InfoWorks or ICM SWMM to simulate and analyze complex urban drainage systems. One of the critical aspects of setting up a SWMM model is configuring the various network options that govern the behavior and performance of the model. In this article, we will dive into the key network options available in ICM SWMM and explore how to select and configure them using SQL. This is a SQL plus and you can do all options in the ICM GUI.

The ICM SWMM network options cover a wide range of settings, including surface ponding, force main equations, head tolerance, inertial damping, infiltration models, solver settings, conduit slopes, node surface areas, normal flow limitations, and units. Each of these options plays a significant role in determining the accuracy and efficiency of the model.

Using SQL in InfoWorks ICM, we can easily select and store these options into variables for further use in the model. The code snippet provided demonstrates how to select the options and assign them to corresponding variables using the clause.

Moreover, the code includes a prompt dialog that displays informative descriptions for each option, helping users understand their significance and guiding them in making appropriate selections. The prompt lines are assigned using statements and displayed using the command, enhancing the user experience and facilitating effective communication.

By leveraging the power of SQL and the prompt dialog, water resources professionals can efficiently configure the ICM SWMM network options, ensuring that the model accurately represents the real-world system being studied. This article aims to provide a comprehensive guide to mastering these options and empowering users to make informed decisions in their ICM SWMM projects.

Whether you are a seasoned water resources engineer or a novice modeler, understanding and effectively utilizing the ICM SWMM network options is essential for delivering reliable and actionable results. By following the insights and techniques presented in this article, you can enhance your modeling skills and unlock the full potential of InfoWorks ICM's SWMM.

![](https://media.licdn.com/dms/image/v2/D4E12AQFvTL6y6QMB4w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1713101344272?e=1795651200&v=beta&t=0j6cbzdpDUY_nD2DtSo7wy3pnf9d923OfC-zvMAeb18)

**ICM SWMM Dialog for Options**

![](https://media.licdn.com/dms/image/v2/D4E12AQGfEQgHBM4OeQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713116119049?e=1795651200&v=beta&t=7WHTdkSSchpcnOlZzZ4hWMuu-aYErjIcMQ285-5LsDo)

SQL Code in ICM InfoWorks for ICM SWMM Networks

![](https://media.licdn.com/dms/image/v2/D4E12AQFubVt4Q_Oj1A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713116056723?e=1795651200&v=beta&t=_cqp0TRIrEiM7yoDbnUTdUzNndY_3mWn6AphGWnpEeQ)

The Generated SQL Select Table and Prompt Table

> **1: The SQL Code on GitHub - see 0018 - SQL SWMM Options**

> **2: Description of the Code**

> 3: Sections concerning SQL in the Autodesk ICM InfoWorks Online Help File

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
