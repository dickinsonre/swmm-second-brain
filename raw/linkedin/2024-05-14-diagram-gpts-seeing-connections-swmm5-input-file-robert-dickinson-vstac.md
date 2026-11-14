---
title: "Diagram GPT's for Seeing Connections in a SWMM5 in Input File"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/diagram-gpts-seeing-connections-swmm5-input-file-robert-dickinson-vstac
created: "2024-03-23 21:59"
published: "2024-05-14 09:45"
words: 958
export_sha256: 755bfd269816312fda8fb3073f6044e9a02f968e7cfbf535601096c0fcb16bde
---
# Diagram GPT's for Seeing Connections in a SWMM5 in Input File

![Expanding on the theme of embracing new capabilities, Naval Ravikant once likened learning to code to going to Hogwarts and learning magic. 🏰✨](https://media.licdn.com/mediaD4E12AQEeamfd80xmNQ "Expanding on the theme of embracing new capabilities, Naval Ravikant once likened learning to code to going to Hogwarts and learning magic. 🏰✨")

The SWMM5 input file is well-organized into data sections, but sometimes it's challenging to see the relationships between ancillary data such as DWF, inflow, aquifers, groundwater, RDII, and LID coverage within the native SWMM5 UX. This post is in response to a question on [OpenSWMM.org](http://OpenSWMM.org) about displaying link-node data outside of SWMM5. By using some of the diagram tools accessible through OpenAI, we hope to show how to make a clearer visualization of these interconnections.

This approach can be particularly useful for students, users of API-based SWMM tools like PySWMM, and users of SWMM5, ICM SWMM, or InfoWorks ICM exported to SWMM5. It will help them better understand and visualize the interconnections within their models.

> **1: Example of a GPT and to Use a SWMM5 file**

To visualize the relationships in a SWMM5 file, start by copying a section of the SWMM5 file into a text editor. Then, use a diagram generation tool, such as one of the many available GPT models, for creating diagrams. Search for a diagram GPT model to help organize the data into a visual form, and perform several iterations to refine the diagram. Often, you can edit the diagram using a graphical user interface (GUI).

![](https://media.licdn.com/dms/image/v2/D4E12AQHQCmUELUuUqQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715553318019?e=1795651200&v=beta&t=eKcq4c0-8NBDTl3NCAjkMGOBCS-SGXV47dTuu_T5jQ4)

An example GPT called Diagram to Make a Link Node Diagram

![](https://media.licdn.com/dms/image/v2/D4E12AQEAnDay2XPtkA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715553387058?e=1795651200&v=beta&t=rBDNfVne4mz5HtZLqQ4XkXrScxrxaxLpwrKBgNEhro4)

You can often edit the look of the created diagram.

Here is a simple SWMM5 example (in case you have not seen it many times before)

> **2: Example of a GPT and to Use a SWMM5 file**

To visualize the relationships in a SWMM5 file, start by copying a section of the SWMM5 file into a text editor. Here is a sample for LID Data or SUDS data.

![](https://media.licdn.com/dms/image/v2/D4E12AQFUrv9a1G-XTg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715553970611?e=1795651200&v=beta&t=Uooi7nkqp20WQBNzHBbuwMdyyjVJWeYEHqDTkhiilLo)

Here is a sample for LID data or SUDS data.

![](https://media.licdn.com/dms/image/v2/D4E12AQGiqy6K19QChQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715554624056?e=1795651200&v=beta&t=T2C-9IvMq05FIw_iXxiBY9v-Ib-3z4cJcgwiaARg-5c)

Here is a sample for LID data or SUDS data.

![](https://media.licdn.com/dms/image/v2/D4E12AQHsmdkCFgb3yw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715554795294?e=1795651200&v=beta&t=9ZdKOPVrC-pIx4GwpFUwmsJBpC41YqmW3LiBs8-vI6I)

How the data looks in SWMM5: You can easily see the subcatchments, nodes, and links, but not the data inside the elements other than on the SWMM5 Detailed view or the Element properties.

![](https://media.licdn.com/dms/image/v2/D4E12AQFmGqClnE7e8g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715297624549?e=1795651200&v=beta&t=nBzOGSEVMbMZRdCeCH9An_j7NuVMlqAzmkEByq1ALVM)

A Link Node View that you can edit

![](https://media.licdn.com/dms/image/v2/D4E12AQFWJ6UNeUlkbQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715297783717?e=1795651200&v=beta&t=_eKVr-vdWkTU6eE6L4Wt5DMAcsY7erQLzFcxHbDyKZ4)

Link Node Diagram

![](https://media.licdn.com/dms/image/v2/D4E12AQHUFvwtMIrX2g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715651070600?e=1795651200&v=beta&t=3Hbx1gxJM73M5DpXFn4SYnSTpZ_b9Ijz9fDfj5ipXsk)

Link Node Diagram

![](https://media.licdn.com/dms/image/v2/D4E12AQFiWDBuMaQoYw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715297832103?e=1795651200&v=beta&t=OkbyrgLaitQhqi2J7JvcXBpcHpq8pY1ziOa0122EvH4)

Link Node Diagram

![](https://media.licdn.com/dms/image/v2/D4E12AQFmh41PMk9xUw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715646944780?e=1795651200&v=beta&t=ApTPccodbZwLMNTiqfxmHvSHypZE_9Y_aDhCTl0F4l8)

Subcatchment Data

![](https://media.licdn.com/dms/image/v2/D4E12AQHkaZge0we41A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715648572314?e=1795651200&v=beta&t=5C4fkxydBe9I9mtxREOHeZwJCiMQd5c7IM-erbtY2Vk)

Groundwater Data

![](https://media.licdn.com/dms/image/v2/D5612AQE0Ye180l6ZLA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715673448344?e=1795651200&v=beta&t=GmiHcKZIc3fPt-JGTd04yq0iuaMOgjyVIS2Y5zF7S-o)

LID Controls

![](https://media.licdn.com/dms/image/v2/D4E12AQH7S7Umb8AdRw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1715647116864?e=1795651200&v=beta&t=6GV65KEyOyE64rBLcvUOvckZLZ1zVNORZCkYjRbtqKU)

SWMM5 GUI

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.

![](https://media.licdn.com/dms/image/v2/D4E12AQHCqDOZsoI1TQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715297123337?e=1795651200&v=beta&t=U3WyyB2OCmp056bzsin29l_HKconGH3K66S9HtJzj_k)

Our journey continues untangling a related group of modeling programs for FY 2025 or Fiscal Year 2025
