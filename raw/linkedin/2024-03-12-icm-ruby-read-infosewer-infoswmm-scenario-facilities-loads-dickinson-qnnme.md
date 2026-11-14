---
title: "ICM Ruby to read the InfoSewer and InfoSWMM scenario facilities, manhole loads, and Scenario ID's."
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/icm-ruby-read-infosewer-infoswmm-scenario-facilities-loads-dickinson-qnnme
created: "2024-02-16 10:38"
published: "2024-03-12 11:37"
words: 656
export_sha256: a78988f3897fec210a650e1407863f3dc1b08e8947c43ecf7aa558c0bd0fb922
---
# ICM Ruby to read the InfoSewer and InfoSWMM scenario facilities, manhole loads, and Scenario ID's.

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![ICM Ruby to read the InfoSewer and InfoSWMM scenario facilities, manhole loads, and scenario ID's.](https://media.licdn.com/mediaD4E12AQGnFm0bpbmwjA "ICM Ruby to read the InfoSewer and InfoSWMM scenario facilities, manhole loads, and scenario ID's.")

Edition 19 of our newsletter delves into the use of Ruby for streamlining the integration between InfoSWMM, InfoSewer, and the ICM networks —InfoWorks and SWMM. It highlights the creation of scenarios and active elements, leading to the generation of new scenarios and selection sets within ICM InfoWorks and ICM SWMM, as illustrated in Figure 1.

Furthermore, this edition showcases four distinct methods for extracting data from the ten manhole loads in InfoSewer and integrating them into the Subcatchment Grid of ICM InfoWorks. These methods include:

1.  Utilizing the ODIC Import tool in conjunction with a CFG file sourced from our GitHub repository.

2.  Employing Ruby to initiate the ODIC import process through the CFG file.

3.  Applying Ruby to directly read data from a single file.

4.  Extending Ruby's functionality to aggregate data from all files from all scenarios as shown in Figure 2.

Each approach offers a unique pathway to enhance data synchronization and data management.

![](https://media.licdn.com/dms/image/v2/D4E12AQGza7KD7sTP5A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710240517231?e=1795651200&v=beta&t=kXtd-fvJkulkIIi2rIHUyGYwCMS8VWp3zbxqi08jtBo)

**Figure 1: The same Ruby code will read the active elements of each scenario in InfoSewer and InfoSWMM and make ICM Selections Sets and add new scenarios**

![](https://media.licdn.com/dms/image/v2/D4E12AQEjxu3I7VKmww/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1710241039461?e=1795651200&v=beta&t=EpYc8OFYywkXlL9b06s14kCMu0IKlczzd9XpA8PHnos)

**Figure 2: Four options to Read Ten InfoSewer Manhole Loads and Pattern ID'S**

> **1/ Making ICM look a bit like InfoSewer**

\[embedded item\]

> **2/ Importing the Facility Manager Information from InfoSewer and InfoSWMM**

\[embedded item\]

> **3/ Reading and Making Scenarios**

\[embedded item\]

> **4/ Read ALL InfoSewer Loads from every Scenario**

\[embedded item\]

> **5/ Read only One Manhole Load file from InfoSewer**

\[embedded item\]

> **6/ Use Ruby to Read One CFG file and use the ODIC Import Tool, Step10_InfoSewer_subcatchment_dwf_mhhyd_scenario_ODIC.rb**

> **7/ Use Only the ODIC Menu Tool**

\[embedded item\]

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
