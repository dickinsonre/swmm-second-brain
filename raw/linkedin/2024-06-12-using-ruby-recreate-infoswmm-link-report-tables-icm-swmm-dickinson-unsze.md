---
title: "Using Ruby to Recreate the InfoSWMM Link Report Tables in ICM SWMM from any SWMM5 Report File"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-recreate-infoswmm-link-report-tables-icm-swmm-dickinson-unsze
created: "2024-06-10 13:21"
published: "2024-06-12 01:35"
words: 2114
export_sha256: 6a7df20b18e64b14ba257a133ea80d8cfddc838a2d9dbecdbabb1b9d788f3d08
---
# Using Ruby to Recreate the InfoSWMM Link Report Tables in ICM SWMM from any SWMM5 Report File

![Using Ruby to Recreate the InfoSWMM Link Report Tables in ICM SWMM from any SWMM5 Report File ](https://media.licdn.com/mediaD4E12AQHlh2nYjB6djQ "Using Ruby to Recreate the InfoSWMM Link Report Tables in ICM SWMM from any SWMM5 Report File ")

We’ve integrated the powerful InfoSWMM engine as the OneSWMM engine into InfoWorks ICM, incorporating the sophisticated ICM UX tools and comprehensive help files that our users love. This integration has resulted in the creation of ICM SWMM Networks, a robust tool designed to meet the evolving needs of the industry.

However, as with any transition from a legacy system, a few features from the original InfoSWMM, a trusted solution for over two decades, didn’t transfer. Notably, the element summary tables for nodes and links were among the features that weren’t ported over.

To address this gap, we've developed a solution using Ruby code to recapture these essential tables. This script reads the SWMM5 report text file, parses the summary tables, and extracts the replacement tables. These are then saved to the ten user numbers and ten user text fields (20 each for nodes, links, pumps, and Subcatchments), enabling SQL operations for active Geoplan networks and enhancing thematic analysis capabilities.

We designed this blog to present information in reverse order, starting with the final result and then working backward to show you the steps leading back to step one. Our rationale is simple: most readers are more interested in the solution than the detailed process. By giving you the answer first, we cater to this preference, so you can go into the detailed steps only if you're interested. This way, you get immediate value from the outcome, allowing you to explore the process at your own pace.

> **7: The LInk Summary Table in ICM SWMM Networks (User Fields)**

The Ruby script processes the SWMM5 report file and extracts valuable information, which is then copied to the link grid in the User Defined Field Name section. This section is divided into two sets of ten fields, with the first set being numeric and the second being textual.

The first set of ten numeric fields captures essential hydraulic characteristics of the links in the network. These fields include the Full Depth, which represents the maximum depth of flow in the link, and the Full Flow, which indicates the maximum flow capacity of the link under full-flow conditions. The Percent Slope field stores the slope of the link as a percentage, providing insight into the gradient of the conduit. The Maximum Flow field records the highest flow rate observed in the link during the simulation, while the Maximum Velocity field captures the corresponding maximum velocity—the Max.The flow/Full Flow field calculates the ratio of the maximum flow to the full-flow capacity, indicating the link's utilization, which is similar to the Max.Depth/Full Depth field computes the ratio of the maximum depth to the full depth, providing a measure of the link's depth utilization. The Afull field represents the cross-sectional area of the link at full flow, and the HRAD Full field stores the hydraulic radius at full flow. Lastly, the Lengthening Factor field is included to account for any link length adjustments.

The second set of ten textual fields provides additional temporal and operational information about the links—the Max. Flow Day-Time field records the day and time the maximum flow occurred, allowing for temporal analysis of peak flows. The Both End Surcharge Time field captures the duration, in hours, during which both ends of the link were surcharged. Similarly, the Upstream Surcharge Time and Downstream Surcharge Time fields store the duration of surcharge conditions at the upstream and downstream ends of the link, respectively. The Above Full-Flow Time field tracks the total time the link experienced flow above its full-flow capacity. The Capacity Limited Time field indicates the duration for which the link's flow was limited by capacity. The last four fields provide information about the flow regime in the link. The Dry field represents when the link was dry or had no flow. The subcritical field captures the fraction of time the link experienced subcritical flow conditions. Conversely, the Supercritical field records the fraction of time the link exhibited supercritical flow. Finally, the Normal Flow Limited field indicates the fraction of time the link's flow was limited by normal flow conditions.

![](https://media.licdn.com/dms/image/v2/D4E12AQGkuC9c-9jNtg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721193518897?e=1795651200&v=beta&t=6RqzcI4sl6E-6VBKUr_j0_jcAluzynxow78xNsik1us)

Imported Link Data goes to the User Fields of ICM SWMM for LInks

![](https://media.licdn.com/dms/image/v2/D5612AQFSwx0RamDsUg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721199500847?e=1795651200&v=beta&t=3-wIcC97xfiDNNumtVi0EMkpPuexwVhX6y9nkmkSVl0)

Export to CSV or Copy and Paste to Excel and use the Excel Tables

> **6: What the Summary Table looked like in InfoSWMM**

The InfoSWMM report table provides a comprehensive overview of the hydraulic and operational characteristics of the network's links.

The "Full Depth (ft)" column indicates the maximum depth of the link under full-flow conditions, measured in feet. This information is crucial for understanding the link's design capacity and assessing its ability to handle peak flows. The "Full Flow" column represents the link's maximum flow capacity when flowing full. This value helps evaluate the link's conveyance capacity and identify potential bottlenecks.

The "Percent Slope (%)" column expresses the link's slope as a percentage. The slope influences the flow velocity and the link's ability to transport water and sediments effectively. The "Maximum Flow" column records the highest flow rate observed in the link during the simulation period. This information is vital for assessing the link's performance under peak flow conditions and identifying any instances of surcharging or flooding.

The "Maximum Flow Class" column classifies the maximum flow based on predefined categories, such as "Dry," "Subcritical," "Supercritical," or "Normal Flow Limited." This classification helps understand the flow regime experienced by the link during peak flow conditions. The "Max.Flow Day-Time (day-time)" column indicates the day and time the maximum flow occurred, allowing for temporal analysis of peak flows.

The "Velocity at Maximum Flow (ft/s)" column represents the flow velocity corresponding to the maximum flow measured in feet per second (ft/s). This information helps assess the link's ability to transport water and sediments efficiently. The "Maximum Velocity (ft/s)" column records the highest velocity observed in the link throughout the simulation period, which is important for evaluating the link's resistance to erosion and scour.

The "Max.Flow/Full Flow" column calculates the ratio of the maximum flow to the link's full-flow capacity. This ratio indicates the link's capacity utilization during peak flow conditions. Similarly, the "Max.Depth/Full Depth" column computes the ratio of the maximum depth to the link's full depth, measuring the link's depth utilization.

The "Reserve Capacity" column represents the additional flow capacity in the link beyond the maximum flow observed during the simulation. This information is valuable for assessing the link's ability to accommodate future growth or increased flows. The "Total Flow Volume (MG)" column calculates the total volume of water that passed through the link during the simulation period, measured in million gallons (MG).

The "Maximum Top Width (ft)" column indicates the maximum width of the water surface at the top of the link during the simulation. This information is relevant for open-channel links and helps assess the link's capacity and potential for overbank flooding.

The "Both End Surcharge Time (hrs)," "Upstream Surcharge Time (hrs)," and "Downstream Surcharge Time (hrs)" columns represent the duration, in hours, during which both ends, the upstream end, and the downstream end of the link experienced surcharge conditions, respectively. These columns provide insights into the extent and location of the link's surcharging.

The "Above Full-Flow Time (hrs)" column records the total time the link experienced flow above its full-flow capacity, indicating the duration of surcharge conditions. The "Capacity Limited Time (hrs)" column represents the duration for which the link's flow was limited by its capacity, highlighting potential bottlenecks in the system.

Lastly, the "Instability Index" column measures the link's hydraulic stability during the simulation. A higher instability index suggests potential issues with flow transitions, such as oscillations or numerical instabilities, that may warrant further investigation.

![](https://media.licdn.com/dms/image/v2/D4E12AQEs9YLeGERkxA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718146607726?e=1795651200&v=beta&t=--_HB5kIzJsQtVTrTrfEUeitNIkNBPIKkLOvBOMW7zs)

What the Summary Table looked like in InfoSWMM

> **5: How do you find the ICM SWMM Output Report File?**

To locate the SWMM5-compatible report file, follow these steps:

1.  Navigate to the menu tools within the application interface. This will grant you access to various options and utilities designed to streamline your workflow and enhance your user experience.

2.  From the menu tools, select the "Local Folders" option. This will allow you to browse and interact with the directories and files stored on your local machine, providing a seamless bridge between the application and your computer's file system.

3.  Once you have accessed the local folders, proceed to the "Report" directory. This dedicated folder serves as a centralized repository for all report-related files, ensuring easy access and organization.

4.  Within the "Report" directory, you can view and examine the available report files. Carefully scan the list of files, paying close attention to their extensions. Your objective is identifying the specific report file with the ".rpt" file extension. This extension means that the file is in the right format for compatibility with the Ruby script you plan to use.

5.  Upon successfully identifying the desired ".rpt" file, you have now located the SWMM5-like report file that can be seamlessly processed by the Ruby script.

![](https://media.licdn.com/dms/image/v2/D4E12AQElOC8-psUJeg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718149134852?e=1795651200&v=beta&t=Foya-DiDbxVhTWoSLzlvKe-hwGBAJKQqIEwOaKdCY-g)

> 4: How do you find the Summary Tables in ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQEgbTq5Nfgh4A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718147988358?e=1795651200&v=beta&t=RM6kgG5eiIsPtwUcdTrPZmAf3G2SHSYEY6DenGIx8Fw)

How do you find the summary tables in ICM SWMM?

> **3: Run the Ruby Code - 01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File**

[**01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File**](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0151%20-%20Read%20SWMM5%20RPT%20File)

![](https://media.licdn.com/dms/image/v2/D4E12AQEv0dMMNk-yIQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718480329813?e=1795651200&v=beta&t=U69M5SGuEHF0hRKprZqKfNwJhxP0QA7XZ93gq6c7nPc)

01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File

> **2: Use the User Defined Field Names to make the Field Columns in the Link Grid similar to InfoSWMM for ICM SWMM**

You can utilize the User Defined Field Names feature to make the Field Columns in the Link Grid of ICM SWMM similar to those in the InfoSWMM report table. This allows you to customize the Link Grid's column headers to match the fields provided in the InfoSWMM report.

Using the user-defined field names in this manner, you can customize the link grid in ICM SWMM to closely resemble the InfoSWMM report table. This allows for a more consistent and familiar representation of the link data across both platforms.

Remember that while the column headers will match the InfoSWMM report table, the actual values displayed in the cells will depend on the specific data in your ICM SWMM model. You may need additional calculations or data processing to populate the cells with the corresponding values from your model results.

![](https://media.licdn.com/dms/image/v2/D4E12AQEWOtXeUjXK0g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718154953557?e=1795651200&v=beta&t=IEItyRpl3TlprQElbgbwLRnIsCB88bf6z-mJduHxJco)

Use the user-defined field names to make the field columns in the link grid similar to InfoSWMM for ICM SWMM.

> **3 What the Link Grid looks like after you complete the import of the sections from the various SWMM5 Report Files**

![](https://media.licdn.com/dms/image/v2/D4E12AQHOu5sjgWGunQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718481058627?e=1795651200&v=beta&t=bAPoEcn6mSBfIk0oElU-2JNN8ijL0-CdF-EKGqlMAnQ)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQFSf2MiVnbMwg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721194819298?e=1795651200&v=beta&t=XxSMYwT5fam-WT1rHKgGh5u2zUmAPgitdpOnmnuasQ4)

Mid Journey AI Green House
