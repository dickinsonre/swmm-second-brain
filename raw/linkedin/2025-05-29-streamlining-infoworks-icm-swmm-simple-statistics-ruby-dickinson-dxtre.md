---
title: "Streamlining InfoWorks ICM SWMM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 44)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/streamlining-infoworks-icm-swmm-simple-statistics-ruby-dickinson-dxtre
created: "2025-05-27 23:11"
published: "2025-05-29 12:26"
words: 1470
export_sha256: 8d655c9e39ce5fabbba0db30c6eb4c816b5264d8c74fbecd72937c171b17d14f
---
# Streamlining InfoWorks ICM SWMM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 44)

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 44)](https://media.licdn.com/mediaD4E12AQFoHkpkXccfcA "Streamlining InfoWorks ICM: Simple Statistics of Thousands of Network Parameters with Ruby Prompts (Edition 44)")

> **Introduction**

Streamline your InfoWorks ICM SWM workflow with the power of Ruby scripting! Tired of manually sifting through thousands of parameters in your InfoWorks ICM SWMM models? Discover how Ruby scripting can revolutionize your data export workflow, saving you hours and unlocking deeper analysis. In this article, part of a series from Editions 41 to 50, I’ll share how Ruby scripts can simplify the process by exporting selected parameters to CSV files with a prompt. In Edition 42, we focused on exporting SW conduit, pump, and simulation parameters, with scripts available on Innovyze GitHub. We added an enhanced update: a checkbox that generates a Ruby puts table, providing the count, max, min, mean, and standard deviation for all fields of selected elements, expanding on the SW Table field prompts first introduced in Edition 42. This is a companion newsletter to Edition 43 for HW Tables, in which HW stands for HydroWorks, the grandfather of ICM InfoWorks. SW tables are for SWMM, and SWMM is its own grandfather.

This statistical functionality is helpful, especially for those familiar with InfoSWMM (me), where such stats were easily accessible via a right mouse click in the InfoSWMM and InfoSewer DB tables. Here, we leverage Ruby to calculate the mean, max, count, and min for various InfoWorks ICM components, including nodes, links, pumps, orifices, weirs, and subcatchments. A discerning reader will notice that these metrics are precisely what’s needed to compare an ICM InfoWorks network to an ICM SWMM network, which you can now do using the 12 RB files shown in Editions 43 and 44. This update not only enhances efficiency but also bridges the gap between different modeling systems, offering a clearer path for comprehensive network analysis.

> **Why Use Ruby for ICM SWMM Data Export?**

Ruby scripting in ICM, a feature I’ve been using since 2021, allows for precise control over data export. With 7299 InfoWorks and 3180 SWMM parameters available, Ruby lets you select exactly what you need, saving time and enabling advanced analysis. Autodesk Water’s improved help file documents all 10,000+ variables, making Ruby a powerful tool for ICM users. There are seven Ruby files described in this newsletter, and one Ruby file has an embedded LinkedIn article with more detail. All of the seven Ruby files also have a markdown file on GitHub with the extension .md

Accessing the Scripts on Innovyze GitHub All scripts, along with detailed markdown documentation, are available in the Innovyze GitHub repository under 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables. Explore over 500 Ruby examples to enhance your ICM workflows in the whole GitHub.

> **1/ Exporting Up to 64 SW Conduit Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called export_sw_conduit_data_to_csv .rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [Innovyze GitHub](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQFvqptCdLe-SQ/article-inline_image-shrink_1500_2232/B4EZcbRUFWH0AU-/0/1748509213976?e=1795651200&v=beta&t=xUgzM6LDX2UR3lowe16kKsGp3jNnmj9xrNeOsoQX58w)

Exporting Up to 64 SW Conduit Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **2/ Exporting Up to 62 SW Node Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called export_sw_node_data_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQHNVP208WHp-w/article-inline_image-shrink_1500_2232/B4EZcZVT3KHYAU-/0/1748476707016?e=1795651200&v=beta&t=IZ_0Mz12kfD40RlO8hTgxbpECjHI97vV-KS-Iy8mwIk)

Exporting Up to 62 SW Node Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **3/ Exporting Up to 81 SW Subcatchment Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

Ruby file is called **export_sw_subcatchments_to_csv.rb** and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQEFOYAbFKD35A/article-inline_image-shrink_1500_2232/B4EZcbUecoHAAU-/0/1748510042849?e=1795651200&v=beta&t=9VqvjtKbCHPfrAgUFqVKkF40sQK0UxRTXjMVES5_RC8)

Exporting Up to 81 SW Subcatchment Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **4/ Exporting Up to 41 SW Weir Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called ex;port_sw_weir_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQFI6fDa06qUFw/article-inline_image-shrink_1500_2232/B4EZcZdDJYHsAU-/0/1748478735554?e=1795651200&v=beta&t=HrBfK3_HwyNnMnFw6v4kbB6K4nQNp9sMaxDhc1lSnyQ)

Exporting Up to 41 SW Weir Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **5/ Exporting Up to 45 SW Orifice Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called **export_sw_orifice_to_csv.rb** and has a detailed markdown (.md) file in the subdirectory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQElEZ0sSsEoLQ/article-inline_image-shrink_1500_2232/B4EZcbTSgoH0AY-/0/1748509731493?e=1795651200&v=beta&t=ySFVe6OOw2OcL4RFHxonrD-RuGBIn3xjtzG_IWFCFW0)

Exporting Up to 45 SW Orifice Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **6/ Exporting Up to 32 SW Pump Parameters to CSV with Ruby in InfoWorks ICM SWMM**

This is an update for statistics from the Ruby files introduced in Edition 42. It has the same prompt for many SW Table fields, but there is now a check box to make a Ruby puts table of the count, max, min, mean, and standard deviation of all fields for the selected elements.

The Ruby file is called export_sw_pump_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQHSGton1Zi8NQ/article-inline_image-shrink_1500_2232/B4EZcZihVNHAAU-/0/1748480170078?e=1795651200&v=beta&t=mgISm7DuTk1b1Nh7I-g-nsqdxs8PI4hzl1XM5f_omBI)

Exporting Up to 32 SW Pump Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **Conclusion**

These Ruby scripts provide a selective and efficient way to export ICM SWMM parameters, enabling better analysis and decision-making. Try them out and let me know how they work for you! Have you leveraged Ruby to conquer complex ICM tasks? What are your go-to scripts or biggest time-savers? Share your insights in the comments below or send me a direct message!
