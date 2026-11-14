---
title: "Edition 31:  InfoSewer to ICM InfoWorks using ODIC and Ruby with SQL, Extended FY2025 Version"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-31-infosewer-icm-infoworks-using-odic-ruby-sql-dickinson-3e80e
created: "2024-03-23 22:03"
published: "2024-05-14 17:57"
words: 748
export_sha256: 7b516139511681bb8ab850b339821dae031fc61bffbf43d333163416898de72b
---
# Edition 31:  InfoSewer to ICM InfoWorks using ODIC and Ruby with SQL, Extended FY2025 Version

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 31: InfoSewer to ICM InfoWorks using ODIC and Ruby with SQL - Extended FY2025 Version](https://media.licdn.com/mediaD4E12AQEH6v68EghXLA "Edition 31:  InfoSewer to ICM InfoWorks using ODIC and Ruby with SQL - Extended FY2025 Version")

**Note:** This is a significantly streamlined rewritten version of the newsletter, achieved by employing more structured and straightforward Ruby code, resulting in a substantial reduction in the conversion process. timing The code can be located and tracked by accessing the links provided in section 1.

> **1: Location of the Ruby, SQL and ODIC CFG Files**

[01 InfoWorks ICM/01 Ruby/01 InfoWorks/0060 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/01%20InfoWorks/0060%20%20-%20ODIC%20and%20SQL%2C%20Ruby%20%20Scripts%20for%20Importing%20InfoSewer%20to%20ICM)

GitHub has excellent readme files, and in addition, the internal Autodesk has more information in the [ICM Online help file](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Knowledge-Importing-InfoSewer-to-InfoWorks-ICM-Overview-of-all-Import-Steps.html)

> **2: Run the Ruby Script and use the converted CSV, Shapefiles and ODIC files Import your InfoSewer Model**

![](https://media.licdn.com/dms/image/v2/D4E12AQHUKDlC2VEDGA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721184009065?e=1795651200&v=beta&t=JxAa3UAHnqYstdIewPJH_S5VuU_yOdN9ZLr181He0tk)

Run the Ruby Script and use the converted CSV, Shapefiles, and ODIC files. Import your InfoSewer Model

> **3: The import process reads all of the needed files and makes an infoWorks Network very fast.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFXGxvIRMC6CQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183905494?e=1795651200&v=beta&t=sBdidSOuXfhBcoAtre_IeaaosCnhpYiEWrh42OFL0to)

**The import process reads all of the needed files and makes an infoWorks Network very fast.**

> **4: Validate and commit the imported network - no validation errors in the case of this InfoSewer Training model**

![](https://media.licdn.com/dms/image/v2/D4E12AQFaT3EjfRv5XQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183832857?e=1795651200&v=beta&t=4LvWfXFq9K_Uc6c1Rddz2BY1Ft9tcm5nusDir3ZGjjg)

**Validate and commit the imported network - no validation errors in the case of this InfoSewer Training model**

> **5: Run the validated model using a design trade flow pattern.**

With only one unpeakable load (Infosewer term) and a few diurnal patterns, this was a basic Infosewer loading model. In the subcatchment grid, user number one was given the load, and user text one was given the pattern. The trade pattern is created from an InfoSewer CSV file using an Excel macro (see the Innovyze GitHub). The user load-to-trade flow is copied using SQL, and the pattern name is changed to a number for the design trade pattern.

![](https://media.licdn.com/dms/image/v2/D4E12AQHjU6Gm85xhPQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183720819?e=1795651200&v=beta&t=4UOpdkcHP4LbzDmkPM-5dWnnKCR_eueTI7JxdLR4yqI)

**Run the validated model using a design trade flow pattern.**

> **6: As discussed elsewhere on LinkedIn, you can make observed predicted csv file for depth, flow and velocity to compare InfoSewer to ICM InfoWorks**

![](https://media.licdn.com/dms/image/v2/D4E12AQGX3macnE_Ilg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183658891?e=1795651200&v=beta&t=P6BhCWazDGJbj_qdDK2D9fKtXhYyuYW4e-LDQ6kkGXg)

**As discussed elsewhere on LinkedIn, you can make observed predicted CSV file for depth, flow, and velocity to compare InfoSewer to ICM InfoWorks**

![](https://media.licdn.com/dms/image/v2/D4E12AQG9t6xHffjaig/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183584670?e=1795651200&v=beta&t=sIcAapqVyp153zuWWEQaWh2m1xClKSfAA55bE4dwRzg)

The flows match as the loads are the same, but the depth and velocity differ since ICM has a sophisticated 1D St Vennt solution compared to the InfoSewer ***Muskingum***-***Cunge*** solution.

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*

![](https://media.licdn.com/dms/image/v2/D4E12AQEZxI5pY9edAA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1715691535368?e=1795651200&v=beta&t=7_QvxWPQ63ZVzSPZxMIXUeBYU_4eE_jtjL8zLdO9WXM)

Midjourney, two worlds
