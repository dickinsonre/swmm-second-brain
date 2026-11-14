---
title: "How can you use Ruby to find the number and types of objects in your ICM database?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-can-you-use-ruby-find-number-types-objects-your-icm-dickinson-wybfe
created: "2024-01-01 17:52"
published: "2024-01-01 21:41"
words: 598
export_sha256: e8c433d36a8a4f0f2bb2a6f9445daa9d6d58fe6154ce59ab7dd35a90dd52ea53
---
# How can you use Ruby to find the number and types of objects in your ICM database?

![My Database Objects for InfoWorks and SWMM in my SWMM5 St Venant Water Talk database](https://media.licdn.com/mediaD4E12AQHWqntOx0I1kw "My Database Objects for InfoWorks and SWMM in my SWMM5 St Venant Water Talk database")

A notable feature of InfoWorks is its database for modeling objects and data. We show how you can count the objects in your DB using Ruby for an example database SWMM5-Tests.icmm which was made for a [Water Talk in 2021.](https://www.youtube.com/watch?v=zqrITNVSOL0)

Here are all of the objects. Highlights are 288 model groups, 450 ICM Sims, 121 SWMM Sims, 244 ICM Networks, and 112 SWMM Networks, and all of their ancillary data, such as 320 rainfall events. The vast majority of the networks were imported from SWMM5 files.

This article is structured into four sections, each offering insights into a Ruby script designed for use with ICM InfoWorks and SWMM Networks:

1.  **Section 1 - Ruby Script to Count Objects in the ICM Database**: This section introduces a Ruby script specifically developed to count the various objects within the ICM database. It outlines the script's functionality, including its approach to systematically tallying different object types. It is available on Github as shown in Section 4. It is a modified version of the code for InfoNet on the same Innovyze GitHub.

2.  **Section 2 -** [**Readme.md**](http://Readme.md) **File for the Ruby Script**: This part of the document serves as a guide or manual for the Ruby script. It provides detailed instructions on how the script operates, including its methodology and step-by-step processes, ensuring users can effectively utilize the script within the InfoWorks ICM environment.

3.  **Section 3 - Diagram of How the Ruby Script Works**: In this section, readers are presented with a visual representation or diagram that explains the operational mechanics of the Ruby script. It illustrates how recursion and a hash table are employed to count database objects, offering a clearer understanding of the script's internal workings. A diagram is worth a lot of readme markdown files.

4.  **Section 4 - Accessing the Code for ICM InfoWorks and SWMM Networks**: The final section addresses where and how users can access this Ruby script for use in ICM InfoWorks and SWMM Networks. This part is crucial for practitioners and users who wish to implement this tool in their database management and analysis tasks. Open source, open SQL and Ruby by Autodesk Water.

> **Section 1:** Ruby Script to Count Objects in the ICM Database

> **Section 2:** [Readme.md](http://Readme.md) file for the Ruby Script

> **Section 3:** Diagram of how the Ruby script works

It uses a Hash Table and recursion to find the number of database objects

![](https://media.licdn.com/dms/image/v2/D4E12AQEzDjvUGm3MaQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1704141696854?e=1795651200&v=beta&t=NFx8lrtXqtjBujc1F8I70DiTA4OVUg5HNVKbNgR0ao8)

**Diagram of how the Ruby script works**

> **Section 4:** Where do I find this code for ICM InfoWorks and SWMM Networks**?**

You can find the Ruby code for both the ICM InfoWorks and SWMM Networks from the InfoWorks [ICM Technical Information Hub for InfoWorks and SWMM Networks](https://boards.autodesk.com/4bf242?token=a671af9e76) in the subfolder **01 InfoWorks ICM\02 SQL\02 SWMM\0007 - Count Objects In the Database**

------------------------------------------------------------------------

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
