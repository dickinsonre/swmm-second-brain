---
title: "Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 43)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/streamlining-infoworks-icm-simple-statistics-network-ruby-dickinson-cnbve
created: "2025-05-27 23:12"
published: "2025-05-28 02:43"
words: 1461
export_sha256: 464ee0195777d2590399c002004f5b545b4b573e24bf3b80fd06bad77669bdb0
---
# Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 43)

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 43)](https://media.licdn.com/mediaD4E12AQE9NoA7gMN5HQ "Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 43)")

> **Introduction**

Streamline your InfoWorks ICM workflow with the power of Ruby scripting! If you’re tired of manually sifting through thousands of parameters, this article—part of our series spanning Editions 41 to 50—will demonstrate how Ruby scripts can revolutionize your data export process, saving you hours and unlocking deeper analysis. In Edition 41, we introduce scripts that simplify exporting HW conduit, pump, and simulation parameters to CSV files through a user-friendly prompt. These scripts, available on Innovyze GitHub, now feature an enhanced update: a checkbox that generates a Ruby puts table, providing the count, max, min, mean, and standard deviation for all fields of selected elements, expanding on the HW Table field prompts first introduced in Edition 41.

This statistical functionality is helpful, especially for those familiar with InfoSWMM (me), where such stats were easily accessible via a right mouse click in the InfoSWMM and InfoSewer DB tables. Here, we leverage Ruby to calculate the mean, max, count, and min for various InfoWorks ICM components, including nodes, links, pumps, orifices, weirs, and subcatchments. A discerning reader will notice that these metrics are precisely what’s needed to compare an ICM InfoWorks network to an ICM SWMM network, a topic we’ll dive into in Edition 44. This update not only enhances efficiency but also bridges the gap between different modeling systems, offering a clearer path for comprehensive network analysis.

> **Why Use Ruby for ICM Data Export?**

Ruby scripting in ICM, a feature I’ve been using since 2021, allows for precise control over data export. With 7299 InfoWorks and 3180 SWMM parameters available, Ruby lets you select exactly what you need, saving time and enabling advanced analysis. Autodesk Water’s improved help file documents all 10,000+ variables, making Ruby a powerful tool for ICM users. There are seven Ruby files described in this newsletter, and one Ruby file has an embedded LinkedIn article with more detail. All of the seven Ruby files also have a markdown file on GitHub with the extension .md

Accessing the Scripts on Innovyze GitHub All scripts, along with detailed markdown documentation, are available in the Innovyze GitHub repository under 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables. Explore over 500 Ruby examples to enhance your ICM workflows in the whole GitHub.

> **1/ Exporting or Calculating Simple Statistics for Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called **export_hw_conduit_data_to_csv.rb** and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [Innovyze GitHub](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQF4zNfF-MebOA/article-inline_image-shrink_1500_2232/B4EZcUHH0KHYAY-/0/1748389101690?e=1795651200&v=beta&t=09KKTYJ_-uJh5cXbtY0ruMm72a5uxfWdcxIU8lpmq8k)

Exporting or Calculating Simple Statistics for Up to 99 HW Conduit Parameters to CSV with Ruby in InfoWorks ICM

> **2/ Exporting or Calculating Simple Statistics for Up to 95 HW Node Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called export_hw_node_data_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQH959FMXZ1vlw/article-inline_image-shrink_1500_2232/B4EZcUaldaHsAU-/0/1748394203835?e=1795651200&v=beta&t=X6nGK_bcKb5x4AS-5T8vZvInSKUmADYVCq95wu6QEwM)

Exporting or Calculating Simple Statistics for Up to 95 HW Node Parameters to CSV with Ruby in InfoWorks ICM

> **3/ Exporting or Calulating Simple Statistics for Up to 127 HW Subcathment Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

Ruby file is called **export_hw_subcatchments_to_csv.rb** and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQG7oYHL3dyYEg/article-inline_image-shrink_1500_2232/B4EZcUu7FEHcAU-/0/1748399535345?e=1795651200&v=beta&t=2GJ0KfG-VmemZTfzgFpznz73C5sHXqs3opB-hOsgt9s)

Exporting or Calulating Simple Statistics for Up to 127 HW Subcathment Parameters to CSV with Ruby in InfoWorks ICM

> **4/ Exporting or Calculating Simple Statistics for Up to 59 HW Weir Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called ex;port_hw_weir_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQFEA_8MfBQl9Q/article-inline_image-shrink_1500_2232/B4EZcUVuwMHkAY-/0/1748392931070?e=1795651200&v=beta&t=FAmML2jQienEWWRD1ekwaa7avMokQyE7--ik0Mqqgf8)

Exporting or Calculating Simple Statistics for Up to 59 HW Weir Parameters to CSV with Ruby in InfoWorks ICM

> **5/ Exporting or Calculating Simple Statistics for Up to 46 HW Orifice Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called **export_hw_orifice_to_csv.rb** and has a detailed markdown (.md) file in the subdirectory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQH0TgS1kQORug/article-inline_image-shrink_1500_2232/B4EZcUKCR5HkAU-/0/1748389865452?e=1795651200&v=beta&t=j7cyOWIYopbhb6v7zdMmC3CGK5QI49dvGYyb9VgB_QQ)

Exporting or Calculating Simple Statistics for Up to 46 HW Orifice Parameters to CSV with Ruby in InfoWorks ICM

> **6/ Exporting or Calculating Simple Statistics for Up to 55 HW Pump Parameters to CSV with Ruby in InfoWorks ICM**

This is an update for statistics from the Ruby files introduced in Edition 41. It has the same prompt for many HW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called export_hw_pump_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQG3QAHabd433w/article-inline_image-shrink_1500_2232/B4EZcUYv6FHYAU-/0/1748393724551?e=1795651200&v=beta&t=gQfukwy5Xu7DPCKWCqYFk_ddDJxOzLvWLxQ6NsQ8TZ4)

Exporting or Calculating Simple Statistics for Up to 55 HW Pump Parameters to CSV with Ruby in InfoWorks ICM

> **Conclusion**

These Ruby scripts provide a selective and efficient way to export ICM parameters, enabling better analysis and decision-making. Try them out and let me know how they work for you! Have you leveraged Ruby to conquer complex ICM tasks? What are your go-to scripts or biggest time-savers? Share your insights in the comments below or send me a direct message!
