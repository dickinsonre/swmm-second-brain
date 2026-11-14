---
title: "Streamlining ICM Workflow: Preserving User-Fields with Ruby Automation to CSV Files"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/streamlining-icm-workflow-preserving-user-fields-ruby-dickinson-hyjde
created: "2024-07-07 05:06"
published: "2024-07-07 06:44"
words: 651
export_sha256: efc47f715b6648bc57f51590f4ca43f12b127fad654adc1f3a10c1193a19902c
---
# Streamlining ICM Workflow: Preserving User-Fields with Ruby Automation to CSV Files

![Streamlining ICM Workflow: Preserving User-Fields with Ruby Automation to CSV Files](https://media.licdn.com/mediaD4E12AQEIJJRlhIe2eA "Streamlining ICM Workflow: Preserving User-Fields with Ruby Automation to CSV Files")

One of the standout features of ICM (Integrated Catchment Modeling) is its inclusion of 10 user numbers and 10 user text fields associated with each table in ICM InfoWorks and ICM SWMM. This functionality provides users exceptional flexibility for model comparison and data manipulation, effectively serving as a versatile Ruby and SQL whiteboard. Engineers and modelers can leverage these fields to store custom calculations, temporary results, or scenario-specific data, greatly enhancing their ability to analyze and compare different model iterations.

However, a significant drawback exists: this valuable information is lost once the whiteboard is erased or the model is closed. This limitation can be particularly frustrating when working on complex projects that require multiple sessions or when revisiting previous calculations is necessary.

To address this issue, we've developed a Ruby script to save the node, link, and subcatchment user fields to CSV files. This preservation method allows for systematically backing critical user-defined data, ensuring no valuable information is inadvertently lost. The saved CSV files can then be easily imported using native ICM menu tools, allowing users to restore their custom data whenever needed.

This solution safeguards against data loss and promotes better workflow management and collaboration. Team members can now share and transfer custom field data more efficiently, leading to improved model consistency and reduced duplication of effort across projects.

![](https://media.licdn.com/dms/image/v2/D4E12AQE5eOWUmxF5Ug/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720334928612?e=1795651200&v=beta&t=h1u3yuBiBWXXddyzfZIpw1wmwWkxb6p0qKuC717jscU)

To address this issue, we've developed a Ruby script to save the node, link, and subcatchment user fields to CSV files. This preservation method allows for systematically backing critical user-defined data, ensuring no valuable information is inadvertently lost. The saved CSV files can then be easily imported using native ICM menu tools, allowing users to restore their custom data whenever needed.

![](https://media.licdn.com/dms/image/v2/D4E12AQEJI38Ghk-aAw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720330509213?e=1795651200&v=beta&t=S4bNRTL-SBW6adeMEo91LUUIUlW1So0kCPAOE0soOAQ)

Customizable File Management Interface: Ruby-powered Dialog for Output Location and File Naming

![](https://media.licdn.com/dms/image/v2/D4E12AQGeXimUNG-QrA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720330466033?e=1795651200&v=beta&t=5TgvX8xml0_ahqim-8rLJdkDXWISAVjjcAo8pE_R6mw)

Interactive Ruby Output Display: Summarizing User Number Totals and Generated File Details

![](https://media.licdn.com/dms/image/v2/D4E12AQGMp-putUHUYA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720330600444?e=1795651200&v=beta&t=J6Ii8-IH-X4qm4ef9Y1hEaF6p1Apf6iG0IYX95BbRH8)

Data Visualization: Exported CSV File as a Rendered Table in Excel Spreadsheet

![](https://media.licdn.com/dms/image/v2/D4E12AQGSRN0KrS-QsA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720330617333?e=1795651200&v=beta&t=GTns6D_wravtrzLKJV_XTSIeguR2hEzQQ6wvnnguMNY)

Future Data Integration: Leveraging ICM's CSV Import Functionality for Generated Files Additional note: "Important: Conduit data must be imported using unique Asset IDs for accurate integration."

![](https://media.licdn.com/dms/image/v2/D4E12AQFfoHXqvo6Jpw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720331017424?e=1795651200&v=beta&t=BfQGSn9sTWi6jOXLlsMb5unKr5bZUU77lPX3G7M_uTU)

New imported user fields with an imported data flag.

> **Location of Ruby Code - Innovyze Github**

[01 InfoWorks ICM/01 Ruby/01 InfoWorks/0066- Export User Fields to CSV with User Name](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/01%20InfoWorks/0066-%20Export%20User%20Fields%20to%20CSV%20with%20User%20Name)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, and they are ready to inform and help when specific circumstances arise.*
