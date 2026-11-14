---
title: "Using Ruby to Export ICM InfoWorks Node, Link, and Subcatchment Grid Data to Shapefiles and a Custom Folder"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-export-icm-infoworks-node-link-grid-data-custom-dickinson-e21xe
created: "2024-06-15 16:19"
published: "2024-06-15 16:44"
words: 483
export_sha256: e68ed333c1db1b49714c26e882dbeb34d0d1ca933906ae09ae1b030ebe5b6ab5
---
# Using Ruby to Export ICM InfoWorks Node, Link, and Subcatchment Grid Data to Shapefiles and a Custom Folder

![Using Ruby to Export ICM InfoWorks Node, Link, and Subcatchment Grid Data to Shapefiles and a Custom Folder](https://media.licdn.com/mediaD4E12AQFDfSr-w5JwdA "Using Ruby to Export ICM InfoWorks Node, Link, and Subcatchment Grid Data to Shapefiles and a Custom Folder")

This Ruby script is designed to export GIS data from an ICM InfoWorks network to a shapefile (SHP) format. Here’s a summary of its operation:

1.  It first accesses the current network using the method.

2.  It retrieves the name of the network.

3.  It sets up an array of tables **(,** **,** **)** to be exported for ICM InfoWorks. There’s also an option to set up an array of tables for ICM SWMM, but this is currently commented out. If you want to export ICM SWMM then uncomment it and then comment the hw lines

4.  It creates a hash for the export options to override the defaults. The options include and , both set to , and , which is set to the array.

5.  It prompts the user to pick a folder for exporting ICM InfoWorks SHP files and provides details about the export method, the tables to be exported, and the formats available.

6.  Finally, it exports the GIS data to the chosen folder in SHP format using the method, with the specified options overriding the default options.

This script provides a flexible way to export GIS data from ICM InfoWorks to various formats. It allows you to customize the tables to be exported and the export options. It also includes user prompts for a more interactive experience. The exported data can then be used for further analysis or visualization in GIS applications.

![](https://media.licdn.com/dms/image/v2/D4E12AQHv4gUXvrZvVw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718468553875?e=1795651200&v=beta&t=nvsjS3eVvz959a8W_Zd6tig47dkxLkRr5BQAb7VFPRk)

Ruby Dialog with some Explanatory text

> **The End Result is a Shape file for Each Table**

![](https://media.licdn.com/dms/image/v2/D4E12AQGiITWZvf6F6Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718468633251?e=1795651200&v=beta&t=YEro7QcC3vS63Sm1xQJX2enF4cqr_Z0vWSkVavKrr1w)

**The End Result is a Shapefile for Each Table.**

> **The Ruby Code is on our Github 01 InfoWorks ICM/01 Ruby/02 SWMM/0114 - GIS Export of Data Tables**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0114 - GIS Export of Data Tables](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0114%20-%20GIS%20Export%20of%20Data%20Tables)

> This code can be used for ICM SWMM as well by changing hw for InfoWork to sw for SWMM

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQEdLGoboaDmTQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718468711263?e=1795651200&v=beta&t=zhFtP71CSUBNO49HbUwtd0A22af90E2GNwFP5Kej7Xs)

Obligatory AI Image from Midjourney featuring Water
