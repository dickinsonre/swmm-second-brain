---
title: "Revolutionizing Hydraulic Network Data Export: A Universal Ruby Script Tool for InfoWorks ICM and SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/revolutionizing-hydraulic-network-data-export-ruby-script-dickinson-xwzqc
created: "2025-06-17 02:32"
published: "2025-06-17 04:20"
words: 923
export_sha256: 6da67ac55824274f042edc8c0d0d310e29f4e2ce1cca0ceb3668818427ae7ae0
---
# Revolutionizing Hydraulic Network Data Export: A Universal Ruby Script Tool for InfoWorks ICM and SWMM Networks

![Revolutionizing Hydraulic Network Data Export: A Universal Ruby Script Tool for InfoWorks ICM and SWMM Networks](https://media.licdn.com/mediaD5612AQGk5TImiDHDGg "Revolutionizing Hydraulic Network Data Export: A Universal Ruby Script Tool for InfoWorks ICM and SWMM Networks")

### How We Built an Intelligent Ruby Data Exporter That Adapts to Your Network Type Using One Ruby Script for SWMM and InfoWorks Networks

I developed this Ruby script for myself to streamline the comparison of InfoWorks and SWMM networks within ICM. The tool generates statistical comparisons between networks and addresses several key requirements:

- **Unified Script**: Single Ruby file that handles both InfoWorks (HW) and SWMM (SW) networks, eliminating the need for separate scripts

- **Flexible Export**: Exports comparison data to CSV files based on user-selected elements

- **Dynamic Selection**: Allows selection of specific tables and parameters within those tables for comparison. It potentially allow you to pick over 150 tables and 10K+ parameters

- **Batch Processing**: Automatically loops through multiple selected tables in a single run, avoiding the need to execute the script repeatedly for each table

This solution significantly improves workflow efficiency for me (and maybe you) when performing network comparisons in ICM, reducing my work and lessening the need for a lot of rb files.

### The Challenge

Working with hydraulic modeling software often requires

- Exporting network data for analysis

- Calculating statistics on hydraulic parameters

- Managing different table structures between InfoWorks and SWMM

- Handling complex data types like pollutant configurations and hyperlinks

- Processing only selected elements in the network

Traditional approaches require separate scripts for each network type, manual field selection, and post-processing for statistics.

### The Solution

We've developed a comprehensive Ruby script that:

1.  **Auto-detects your network type**— No need to specify if you're using InfoWorks or SWMM

![](https://media.licdn.com/dms/image/v2/D5612AQFoxFY27RrfDg/article-inline_image-shrink_1500_2232/B56Zd79wRSHoAU-/0/1750131476933?e=1795651200&v=beta&t=SPJ4nMicP-NPCApXvUrN1ay7sQdzB0XpprjFK6GkvDQ)

All SW or SWMM Tables

![](https://media.licdn.com/dms/image/v2/D5612AQGVazGgT_H9mw/article-inline_image-shrink_1500_2232/B56Zd794jLGoAc-/0/1750131510409?e=1795651200&v=beta&t=tXQZmLCk6xLrQTRclb8t4kZR7UAU4l2n5-N9o1kMnNc)

All HW or InfoWorks Tables

1.  **Dynamically discovers all available tables**—automatically finds all 39 SWMM tables or 84 InfoWorks tables

2.  **Provides intelligent field selection**—choose fields with a SELECT ALL option **Handles complex data gracefully**—arrays, pollutants, hyperlinks, and more

![](https://media.licdn.com/dms/image/v2/D5612AQFhi8dawrvtwQ/article-inline_image-shrink_1500_2232/B56Zd7.XY9GoAc-/0/1750131636744?e=1795651200&v=beta&t=YHPmOltTXXCDuhQB0os5j3ZBEcfYGm4oyh5wRJHbMPY)

Provides intelligent field selection

1.  

![](https://media.licdn.com/dms/image/v2/D5612AQGcJywVfZxVgg/article-inline_image-shrink_1500_2232/B56Zd7.8Y0HQAU-/0/1750131790000?e=1795651200&v=beta&t=DfarBTxlxPqsyUIa4toPLyIXtw2py_L2rRj3uk3TKGI)

Calculates statistics on-the-fly

![](https://media.licdn.com/dms/image/v2/D5612AQHFrzA8jombKg/article-inline_image-shrink_1500_2232/B56Zd7.sWqH8Ac-/0/1750131722337?e=1795651200&v=beta&t=66a4ujnNm1i_K1hlZV1MwsXfjUZoRAHXhphzvzRfPDQ)

Runs in a continuous loop

![](https://media.licdn.com/dms/image/v2/D5612AQFjQT6ipx6esw/article-inline_image-shrink_1000_1488/B56Zd8BFULHQAY-/0/1750132348965?e=1795651200&v=beta&t=hedgrolxrdiB8Sg8XTTVyhKtaXcKPyROSAOLFNY1CKM)

The last dialog

### Smart Network Detection—it detects the type of network—InfoWorks or SWMM.

### Comprehensive Table Coverage

The script includes all standard tables for both network types:

- **SWMM**: 39 tables, including nodes, conduits, subcatchments, pumps, curves, and 2D elements

- **InfoWorks**: 84 tables covering everything from basic hydraulics to water quality and sediment transport

### Intelligent Statistics Engine

### 📊 Real-World Benefits

1.  **Time Savings**: What used to take hours now takes minutes

2.  **Accuracy**: Eliminates manual copy-paste errors

3.  **Flexibility**: Export only what you need, when you need it

4.  **Analysis Ready**: Statistics calculated automatically

5.  **Quality Control**: See object counts and verify data completeness or SWMM5, InfoSewer or InfoSWMM conversions.

### 🎨 Smart Features That Make a Difference

### Selective Export with Statistics Only

Don't need a CSV file? The script can calculate statistics without exporting, perfect for quick data checks.

### Batch Processing with Error Recovery

Process multiple tables in one session. If one table fails, the script asks if you want to continue with the others.

### Complex Data Serialization

Handles InfoWorks/SWMM's complex array fields intelligently:

- Pollutant configurations

- Treatment functions

- Hyperlinks

- Additional DWF patterns

### Use Cases

- **Model Auditing**: Quickly assess the statistical distribution of key parameters

- **Quality Assurance**: Verify data ranges and identify outliers

- **Reporting**: Generate standardized exports for project documentation

- **Data Migration**: Export data for use in other analysis tools

- **Comparison Studies**: Standardized exports make model comparison easier

### Getting Started

1.  Place the script in your Ruby scripts folder

2.  Open your InfoWorks ICM or SWMM network

3.  Run the script hw_sw_all_table_reader.rb from the [Innovyze GitHub 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0005%20-%20Import%20Export%20of%20Data%20Tables)

4.  Select tables and fields to export

5.  Choose whether to export CSV, calculate statistics, or both

### Future Enhancements

We're considering adding in a similar catch-all parameters script

- GeoJSON export for GIS integration

- Direct Excel export with formatting

- Automated report generation

- Custom field calculations

- Time series data handling

### Final Thoughts

This tool represents a shift in how we approach hydraulic model data management. By creating intelligent, adaptive tools that understand our data structures, we can focus more on engineering analysis and less on data manipulation.

The script is open for enhancement and customization. Whether you need to add custom field processing, integrate with other tools, or adapt it for your specific workflows, the modular design makes it easy to extend.

### Connect and Collaborate

If you're interested in implementing this tool or have ideas for enhancement, let's connect! Together, we can build better tools for the water engineering community.
