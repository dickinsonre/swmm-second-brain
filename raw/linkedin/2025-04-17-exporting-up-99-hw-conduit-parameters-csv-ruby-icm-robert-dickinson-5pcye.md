---
title: "Exporting Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/exporting-up-99-hw-conduit-parameters-csv-ruby-icm-robert-dickinson-5pcye
created: "2025-02-20 00:34"
published: "2025-04-17 03:14"
words: 723
export_sha256: b5cb3d4cbdc6a2c96721f331fbe25f5aeb02dae263987aae103a1575a32ce4a3
---
# Exporting Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM

![Exporting Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM](https://media.licdn.com/mediaD4E12AQFWzwSXbmru-A "Exporting Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM")

As part of our Ruby scripting series for InfoWorks ICM, this article shares a Ruby script to export hw_conduits data to a CSV file, simplifying data analysis for SWMM5 and ICM modelers. Learn how to use this script to streamline your workflow, with the code available on GitHub. Next, there will be articles for the sw_conduits (sw for SWMM) to a CSV file and then InfoWorks and SWMM to shape files. The grand goal is Ruby code for ALL 11,000 fields in ICM SWMM and ICM InfoWorks (as mentioned in other articles, InfoWorks has about three times more data fields). The ultimate goal is to improve how you use conduit data in your projects by using Ruby to manipulate the tables for export, comparisons, statistics, and AI.

> **1/ Introduction**

This article is part of a series on using Ruby in ICM InfoWorks. The overall goal is to show how Ruby scripts can manipulate all 11,000 data elements in the SW and HW tables. The linked Ruby script in this one article provides code to select and export the hw_conduits table to a CSV file. Up to 99 conduit parameters can be exported.

> **2/ Why Use the Script?**

The script allows you to extract specific data fields (e.g., pipe dimensions, IDs, or hydraulic properties) from the hw_conduits table, part of the 11,000 data elements in InfoWorks ICM’s SW and HW tables. The resulting timestamped CSV file is ideal for Excel analysis, reporting, or sharing with stakeholders. This Ruby script is only for hw tables as InfoWorks and SWMM conduit data are very different.

**How different?** Here is a comparison:

- hw_conduits (InfoWorks ICM): Up to 99+ parameters, covering identifiers, hydraulic properties, asset metadata, sediment data, and more.

- sw_conduits (SWMM5 in ICM): Approximately 10-15 parameters, focusing on basic geometry, roughness, and connectivity.

> **3/ How It Works**

- Connects to the active network in an ICM InfoWorks network.

- Displays a dialog box to select an output folder and desired data fields (see Figure 1).

- Iterates through selected **hw_conduit** objects, fetching user-specified data.

- Writes the data to a timestamped CSV file, with error handling to ensure reliability (see Figure 4)

> **4/ Getting Started**

1.  Open ICM and load your InfoWorks network model.

2.  Select the conduits you want to export using the built-in selection tools.

3.  Run the script (export_hw_conduit_data_to_csv.rb) via the ‘Run Script’ option.

4.  In the dialog box, choose your output folder and data fields, then click ‘OK.’

5.  Find the generated CSV in the specified folder.

> **5/ Where is the Code - the Autodesk Water Infrastructure GitHub**

The script, export_hw_conduit_data_to_csv.rb, is available on the Autodesk Water Infrastructure GitHub repository under InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables. Visit \[GitHub link\] to download the code and explore the detailed markdown documentation. [**01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables**](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0005%20-%20Import%20Export%20of%20Data%20Tables/export_hw_conduit_data_to_csv.rb)

Here is how the link fields are defined in the Ruby Script (snippet of the larger code)

![](https://media.licdn.com/dms/image/v2/D4E12AQEylQKyM0TKZw/article-inline_image-shrink_1500_2232/B4EZY8CIl4G0AU-/0/1744763915256?e=1795651200&v=beta&t=vF3rjnSe6F2UYW9h_-GkdXGhzYadP0OsxbUZriJ6l5o)

Figure 1: Dialog for picking the link fields for export from the hw_conduits link table

### 

![](https://media.licdn.com/dms/image/v2/D4E12AQHgpa0KYhh5OA/article-inline_image-shrink_1500_2232/B4EZY8CN1MGYAU-/0/1744763936474?e=1795651200&v=beta&t=yqlREq2TtIiJh2Z76c4Blb9L_4KXIEWZFfWKBMN1k9k)

Figure 2: The summary dialog tells you how many links and data fields are exported.

![](https://media.licdn.com/dms/image/v2/D4E12AQGaYDLPp5Pbhg/article-inline_image-shrink_1500_2232/B4EZY8CRivHcAU-/0/1744763951771?e=1795651200&v=beta&t=qKV0qB5CXcvpnVcfQuviuID_DwJ7GRUSwFFyK-KkW2o)

Figure 3: Ruby Puts Dialog Summary

![](https://media.licdn.com/dms/image/v2/D4E12AQF6Qfi8FcHvUQ/article-inline_image-shrink_1500_2232/B4EZY8CXpNHkAY-/0/1744763976754?e=1795651200&v=beta&t=L252_9nxaTW85QnxY87bSe1Epji4n_lSH-OO5vAkbwU)

Figure 4: End Result - Saved data for the HW Conduit Table in Excel for the selected elements

> Closing Note

This script simplifies data export, saving time and enhancing your InfoWorks ICM workflow. Try it out, and share your feedback or questions in the comments!
