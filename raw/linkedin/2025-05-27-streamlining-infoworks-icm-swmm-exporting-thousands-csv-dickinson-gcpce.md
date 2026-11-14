---
title: "Streamlining InfoWorks ICM SWMM: Exporting Thousands of Network Parameters to CSV with Ruby Prompts (Edition 42)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/streamlining-infoworks-icm-swmm-exporting-thousands-csv-dickinson-gcpce
created: "2025-05-27 16:52"
published: "2025-05-27 22:06"
words: 965
export_sha256: fa3a99748ff6cf881701f081959d1f215cbd5b844aee3e4c74380ac5470b0df6
---
# Streamlining InfoWorks ICM SWMM: Exporting Thousands of Network Parameters to CSV with Ruby Prompts (Edition 42)

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Streamlining InfoWorks ICM SWMM: Exporting Thousands of Network Parameters to CSV with Ruby Prompts (Edition 42)](https://media.licdn.com/mediaD4E12AQH2aBr6uYlsyw "Streamlining InfoWorks ICM SWMM: Exporting Thousands of Network Parameters to CSV with Ruby Prompts (Edition 42)")

> **Introduction**

Tired of manually sifting through thousands of parameters in your InfoWorks ICM SWMM models? Discover how Ruby scripting can revolutionize your data export workflow, saving you hours and unlocking deeper analysis. In this article, part of a series from Editions 41 to 50, I’ll share how Ruby scripts can simplify the process by exporting selected parameters to CSV files with a prompt. In Edition 42, we focus on exporting SW conduit, pump, and simulation parameters, with scripts available on Innovyze GitHub. This is a companion newsletter to Edition 41 for HW Tables in which HW stands for HydroWorks, the grandfather of ICM InfoWorks. SW tables are for SWMM, and SWMM is its own grandfather.

> **Why Use Ruby for ICM SWMM Data Export?**

Ruby scripting in ICM, a feature I’ve been using since 2021, allows for precise control over data export. With 7299 InfoWorks and 3180 SWMM parameters available, Ruby lets you select exactly what you need, saving time and enabling advanced analysis. Autodesk Water’s improved help file documents all 10,000+ variables, making Ruby a powerful tool for ICM users. There are six Ruby files described in this newsletter. All of the six Ruby files also have a markdown file on GitHub with the extension .md

Accessing the Scripts on Innovyze GitHub All scripts, along with detailed markdown documentation, are available in the Innovyze GitHub repository under 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables. Explore over 500 Ruby examples to enhance your ICM workflows in the whole GitHub.

> **1/ Exporting Up to 64 SW Conduit Parameters to CSV with Ruby in InfoWorks ICM SWMM**

The Ruby file is called export_sw_conduit_data_to_csv .rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [Innovyze GitHub](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQFtHr3b65_8pw/article-inline_image-shrink_1500_2232/B4EZcTR75CHAAY-/0/1748375158989?e=1795651200&v=beta&t=TKOvcSKaYfCMnSHLQ1ulxtKUexwIPJ8DqaqNTzlm0Jw)

Exporting Up to 64 SW Conduit Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **2/ Exporting Up to 62 SW Node Parameters to CSV with Ruby in InfoWorks ICM SWMM**

The Ruby file is called export_sw_node_data_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D5612AQEl0kKao9kMXA/article-inline_image-shrink_1500_2232/B56ZcThPPsHgAY-/0/1748379170269?e=1795651200&v=beta&t=dG5o38Aim9Ppk3Zfgo_ZEFIXkd39oPqLTlgPXmiDma0)

Exporting Up to 62 SW Node Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **3/ Exporting Up to 81 SW Subcatchment Parameters to CSV with Ruby in InfoWorks ICM SWMM**

Ruby file is called **export_sw_subcatchments_to_csv.rb** and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQGUSPYk8vL2Jg/article-inline_image-shrink_1500_2232/B4EZcTTKXXHAAU-/0/1748375480387?e=1795651200&v=beta&t=tHT2W0L6cM56xNB11prElTwP6NJJ2RRAQaU4T7jmQTI)

Exporting Up to 81 SW Subcatchment Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **4/ Exporting Up to 41 SW Weir Parameters to CSV with Ruby in InfoWorks ICM SWMM**

The Ruby file is called ex;port_sw_weir_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D4E12AQGxD08tdkraZw/article-inline_image-shrink_1500_2232/B4EZcTxJt7HYAU-/0/1748383341927?e=1795651200&v=beta&t=D_6tgfJtwffxz6BSbgkXJ2mZH_FzT8zpWy1r_TPZjZg)

Exporting Up to 41 SW Weir Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **5/ Exporting Up to 45 SW Orifice Parameters to CSV with Ruby in InfoWorks ICM SWMM**

The Ruby file is called **export_sw_orifice_to_csv.rb** and has a detailed markdown (.md) file in the subdirectory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D5612AQHKcSZIl5n6KA/article-inline_image-shrink_1500_2232/B56ZcTwQaSG0AU-/0/1748383107359?e=1795651200&v=beta&t=Spi32TjkI12zVfP_C4G0ItfxAHwq0IKhYq6qPfgHFeg)

Exporting Up to 45 SW Orifice Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **6/ Exporting Up to 32 SW Pump Parameters to CSV with Ruby in InfoWorks ICM SWMM**

The Ruby file is called export_sw_pump_to_csv.rb and has a detailed markdown (.md) file in the sub directory 01 InfoWorks ICM/01 Ruby/02 SWMM/0005 - Import Export of Data Tables on the [**Innovyze GitHub**](https://github.com/innovyze/Open-Source-Support)

![](https://media.licdn.com/dms/image/v2/D5612AQE8K_5V3DYKTg/article-inline_image-shrink_1500_2232/B56ZcTjmUjGQAU-/0/1748379789095?e=1795651200&v=beta&t=7Z2uDTc354rabpmZDelw9hwp5JsoLHlQMHaf47PTP5A)

Exporting Up to 32 SW Pump Parameters to CSV with Ruby in InfoWorks ICM SWMM

> **Conclusion**

These Ruby scripts provide a selective and efficient way to export ICM SWMM parameters, enabling better analysis and decision-making. Try them out and let me know how they work for you! Have you leveraged Ruby to conquer complex ICM tasks? What are your go-to scripts or biggest time-savers? Share your insights in the comments below or send me a direct message!
