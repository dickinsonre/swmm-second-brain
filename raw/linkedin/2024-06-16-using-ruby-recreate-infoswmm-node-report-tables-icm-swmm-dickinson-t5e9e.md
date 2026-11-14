---
title: "Using Ruby to Recreate the InfoSWMM Node Report Tables in ICM SWMM from any SWMM5 Report File"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-recreate-infoswmm-node-report-tables-icm-swmm-dickinson-t5e9e
created: "2024-06-16 16:57"
published: "2024-06-16 18:30"
words: 1243
export_sha256: 79339610f71fbdcf2fa4acbe10479ca706599abeca8493f90c87e9f804c608ba
---
# Using Ruby to Recreate the InfoSWMM Node Report Tables in ICM SWMM from any SWMM5 Report File

![Using Ruby to Recreate the InfoSWMM Node Report Tables in ICM SWMM from any SWMM5 Report File](https://media.licdn.com/mediaD4E12AQGUE5cD6gWb1w "Using Ruby to Recreate the InfoSWMM Node Report Tables in ICM SWMM from any SWMM5 Report File")

We’ve integrated the powerful InfoSWMM engine as the OneSWMM engine into InfoWorks ICM, incorporating the sophisticated ICM UX tools and comprehensive help files that our users love. This integration has resulted in the creation of ICM SWMM Networks, a robust tool designed to meet the evolving needs of the industry.

However, as with any transition from a legacy system, a few features from the original InfoSWMM, a trusted solution for over two decades, didn’t transfer. Notably, the element summary tables for nodes and links were among the features that weren’t ported over.

To address this gap, we've developed a solution using Ruby code to recapture these essential tables. This script reads the SWMM5 report text file, parses the summary tables, and extracts the replacement tables. These are then saved to the ten user numbers and ten user text fields (20 each for nodes, links, pumps, and Subcatchments), enabling SQL operations for active Geoplan networks and enhancing thematic analysis capabilities.

We designed this blog to present information in reverse order, starting with the final result and then working backward to show you the steps leading back to step one. Our rationale is simple: most readers are more interested in the solution than the detailed process. By giving you the answer first, we cater to this preference, so you can go into the detailed steps only if you're interested. This way, you get immediate value from the outcome, allowing you to explore the process at your own pace.

> **7: The Node Summary Table in ICM SWMM Networks (User Fields)**

The Ruby script processes the SWMM5 report file and extracts valuable information, which is then copied to the link grid in the User Defined Field Name section. This section is divided into two sets of ten fields, with the first set being numeric and the second being textual.

Here is a summary of the user fields and what they do in the context of SWMM:

The ICM SWMM Network in InfoWorks provides 20 user-defined fields that can be used to capture and report on various hydraulic and hydrologic metrics.

The User Number fields include parameters such as Maximum Depth, Node Elevation, Maximum HGL (Hydraulic Grade Line), Maximum Lateral Inflow, Maximum Total Inflow, Lateral Inflow Volume, Total Inflow Volume, and Total Surcharge Time. These numerical fields allow users to track key network performance values under different flow conditions.

The User Text fields provide more qualitative insights, including the Maximum Surcharge Height Above Crown, Minimum Surcharge Depth Below Rim, Total Flood Time, Maximum Flood Rate, Total Flood Volume, Maximum Depth and Reported Depth During Daytime, Maximum Flood During Daytime, Outfall Peak, and Outfall Total Volume. These textual fields help provide context and labels to the quantitative data.

Together, this suite of user-defined parameters gives SWMM modelers within the ICM InfoWorks environment a robust set of tools to thoroughly analyze the behavior and performance of their stormwater networks. By leveraging these fields, users can gain deeper insights, identify areas of concern, and make more informed decisions about system upgrades and enhancements.

![](https://media.licdn.com/dms/image/v2/D4E12AQGfOxyrWExfow/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718561218929?e=1795651200&v=beta&t=kpowwQeAyG6Ejl34JwjAxjHYWFOLxVmFzhoFkXCNfDc)

Node Grid Tables

![](https://media.licdn.com/dms/image/v2/D4E12AQE7priU0pLzaQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718561864166?e=1795651200&v=beta&t=taxxD3mfbLgCRFO6SZiQok-W88sRMZnxD-QN4SBlKdc)

Node Grid Tables in Excel

> **6: What the Summary Table looked like in InfoSWMM**

The InfoSWMM report table provides a comprehensive overview of the hydraulic and operational characteristics of the network's nodes.

![](https://media.licdn.com/dms/image/v2/D4E12AQFapoK5LFR7Vg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718561953119?e=1795651200&v=beta&t=CocNifGI_gn8R7NrERT0fxUuvYU58iZ3GkSEB_RJnGE)

InfoSWMM Node Summary Report

> **5: How do you find the ICM SWMM Output Report File?**

To locate the SWMM5-compatible report file, follow these steps:

1.  Navigate to the menu tools within the application interface. This will grant you access to various options and utilities designed to streamline your workflow and enhance your user experience.

2.  From the menu tools, select the "Local Folders" option. This will allow you to browse and interact with the directories and files stored on your local machine, providing a seamless bridge between the application and your computer's file system.

3.  Once you have accessed the local folders, proceed to the "Report" directory. This dedicated folder is a centralized repository for all report-related files, ensuring easy access and organization.

4.  Within the "Report" directory, you can view and examine the available report files. Carefully scan the list of files, paying close attention to their extensions. Your objective is to identify the specific report file with the ".rpt" file extension. This extension means that the file is in the right format for compatibility with the Ruby script you plan to use.

5.  Upon successfully identifying the desired ".rpt" file, you have now located the SWMM5-like report file that can be seamlessly processed by the Ruby script.

![](https://media.licdn.com/dms/image/v2/D4E12AQGefeXo_RVB0Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718557059352?e=1795651200&v=beta&t=ziNeILCUymc18d_73igkv-GFACD5nch4LdiSuiNET4s)

How to FInd the Report File

> 4: How do you find the Summary Tables in ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQHvpdEvohEcgw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718557058849?e=1795651200&v=beta&t=dXOpQhpVe5eXUD0v1PlHwaK3XhVY3c4Q7KLn3faFZN8)

How do you find the summary tables in ICM SWMM?

> **3: Run the Ruby Code - 01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File**

[**01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File**](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0151%20-%20Read%20SWMM5%20RPT%20File)

![](https://media.licdn.com/dms/image/v2/D4E12AQFflMMB7Zs0rQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718557058845?e=1795651200&v=beta&t=G6Oc_wdoOXC0q3vO2S-YbJrm2TlKonp3k4Fmw0ylYuY)

01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File

> **2: Use the User Defined Field Names to make the Field Columns in the Link Grid similar to InfoSWMM for ICM SWMM**

You can utilize the User Defined Field Names feature to make the Field Columns in the Link Grid of ICM SWMM similar to those in the InfoSWMM report table. This allows you to customize the Node Grid's column headers to match the fields provided in the InfoSWMM report.

Remember that while the column headers will match the InfoSWMM report table, the actual values displayed in the cells will depend on the specific data in your ICM SWMM model. You may need additional calculations or data processing to populate the cells with the corresponding values from your model results.

![](https://media.licdn.com/dms/image/v2/D4E12AQHCgWVCp3mUpA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718562103860?e=1795651200&v=beta&t=o_c632KGU6wZywyzPf-lbx892R_0LuZMkL9SsAr751Q)

User-defined field names for ICM SWMM Gird Table

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQFOIBEUZuch-Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718562197303?e=1795651200&v=beta&t=e_Ffywwkb6YFQr3iRK6GK1oikSLJ4XPiS3XGohLh8FI)

Mid Journey AI Imaginary Water Animals
