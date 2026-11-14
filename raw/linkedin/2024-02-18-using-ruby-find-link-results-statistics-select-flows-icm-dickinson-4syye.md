---
title: "Using Ruby to Find Link Results Statistics and Select the Highest Flows in ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-find-link-results-statistics-select-flows-icm-dickinson-4syye
created: "2024-02-18 18:18"
published: "2024-02-18 19:48"
words: 463
export_sha256: 4dae84ea6730b3f3f83a93f1c23f04220b588f05eb8b0e6f3d9aa58f8248d4c3
---
# Using Ruby to Find Link Results Statistics and Select the Highest Flows in ICM InfoWorks

![Using Ruby to Find Link Results Statistics and Select the Highest Flows in ICM InfoWorks ](https://media.licdn.com/mediaD4E12AQG447gDOmSk4w "Using Ruby to Find Link Results Statistics and Select the Highest Flows in ICM InfoWorks ")

**Article Topic:** Discover how to harness a Ruby script to calculate mean, min, max, and sum flows in InfoWorks and ICM SWMM links, and understand some of the key differences that set SWMM5 and InfoWorks apart in their St Venant equation solutions.

**Introduction:** In the complex realm of urban water management and environmental engineering, the ability to accurately analyze and interpret flow data is indispensable. Using ICM InfoWorks or ICM SWMM professionals are constantly seeking more efficient and precise methods to assess the performance of their networks. **Enter Ruby**—a powerful programming language that opens new horizons for calculating mean, minimum, maximum, and sum flows across selected links in a model run.

InfoWorks has **two** reported flows, depth, and velocities at both ends of a link in InfoWorks, to the singular flow report in SWMM5 (Figure 1). Understanding these distinctions is crucial for accurate data interpretation. InfoWorks’ flexibility in computational points, allowing users to adjust from five to twenty or more, contrasts sharply with SWMM5’s single computation point, highlighting the varied approaches to solving hydraulic challenges.

We also leverage Ruby to extract vital statistics from your network data. By identifying and analyzing the top ten mean flows, you can pinpoint critical areas for improvement, optimization, or further study. The top ten links are selected on the GeoPlan so they can be graphed later (Figure 2). You can see the code below or go to our [GitHub](https://boards.autodesk.com/icm?token=a671af9e76) and close the repository if you want.

![](https://media.licdn.com/dms/image/v2/D4E12AQH-vABNlLfu9A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1708282106684?e=1795651200&v=beta&t=zbvYyihACUxc9CBOCAlnpKLHqe_6ElF3UGyoa8c2djY)

**Figure 1. Some of the Upstream and Downstream Results Fields for ICM InfoWorks Links**

![](https://media.licdn.com/dms/image/v2/D4E12AQG3JL-sxbP0Pw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1708284288246?e=1795651200&v=beta&t=kIZcOENqRiHFNkBX9mc0oVO1EXiSLxD34ZGwgZAnnE4)

**Figure 2 Ruby Script Window and Graphs of the Top-Ten Highest Mean Flow Links**

> **Code Box - Ruby Code to first calculate the mean, min and max flow in a link followed by selecting the top ten flows**

The code can be tweaked to show more than ten by changing this line: top_ten_links = mean_us_flows.sort_by { \|\_, v\| -v }.first(10).map { \|k, \_\| k }

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
