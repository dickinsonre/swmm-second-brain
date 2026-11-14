---
title: "Bridging Decades: Reading InfoSewer Report RPT Output for ICM InfoWorks in 2030+"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/bridging-decades-reading-infosewer-report-rpt-output-icm-dickinson-jyhue
created: "2025-05-24 17:59"
published: "2025-05-25 18:09"
words: 610
export_sha256: 3f4c7a0b38c54aa4750567ada89ce72df5163bc09c0ad4ffab7d624885ec1457
---
# Bridging Decades: Reading InfoSewer Report RPT Output for ICM InfoWorks in 2030+

![Bridging Decades: Converting InfoSewer Report RPT Output for ICM InfoWorks in 2030+](https://media.licdn.com/mediaD4E12AQGtjN8__pJ9Jg "Bridging Decades: Converting InfoSewer Report RPT Output for ICM InfoWorks in 2030+")

As we move closer to 2030 or sooner, some engineers face a unique challenge: accessing and interpreting InfoSewer output from projects dating back to 2001–2025. With ESRI’s ArcMap retired and Autodesk sunsetting InfoSewer, running the software is no longer an option. Fortunately, there’s a solution. By leveraging Ruby code, you can extract critical data from archived InfoSewer OUT folder files, specifically the steady-state and EPS (extended period simulation) report files. This workaround, inspired by one of our Stellar Solution Engineers, **\[Tim Medearis\],** enables you to summarize loads and flows and generate CSV sections for use as observed-predicted data in ICM InfoWorks. Here’s how to bridge the past with the future and keep your historical sewer models useful for the sake of model result comparisons.

Historical sewer data from 2005–2025 isn’t just a relic; it’s vital for compliance, infrastructure upgrades, and validating new models in ICM InfoWorks. Whether you’re assessing past performance for regulatory audits or planning retrofits, these outputs provide a baseline. However, with InfoSewer obsolete, accessing this data is a hurdle. While ICM Ruby and ODIC code can read [IEDB folder DBF files](https://help.autodesk.com/view/IWICMS/2026/ENU/?caas=caas/sfdcarticles/sfdcarticles/Knowledge-Importing-InfoSewer-to-InfoWorks-ICM-Overview-of-all-Import-Steps.html), they don’t reveal InfoSewer’s original answers. This Ruby script fills that gap, ensuring engineers can leverage decades-old insights without recreating models from scratch. As mentioned, this will be impossible in 2030 or sooner depending on ESRI and its sunsetting of ArcMap.

The Ruby script targets InfoSewer’s OUT folder, specifically the steady-state (.rpt) and EPS (.eps) report files. It parses these files to extract key metrics: node loads, link flows, and system performance data. The script then makes a structured CSV file, formatted for direct import into ICM InfoWorks as observed-predicted data. Prerequisites are minimal: you need the archived OUT folder and a basic ICM UI Ruby environment. Unlike ICM’s ODIC native tools, which focus on DBF and CSV files, this script unlocks the exact results InfoSewer produced, preserving the integrity of historical simulations.

> **Ruby InfoSewer RPT Prompt**

![](https://media.licdn.com/dms/image/v2/D4E12AQGv5rYxrhLgyg/article-inline_image-shrink_1000_1488/B4EZcIiNHDHIAQ-/0/1748194874129?e=1795651200&v=beta&t=FBxhrvOSTNRQ0Aupegw1GQpckxY6kj4HcmGJSQFbA0k)

**Ruby InfoSewer RPT Prompt**

> **Ruby Puts Statement Output for Nodes and LInks Stats from the InfoSewer Simulation Run**

![](https://media.licdn.com/dms/image/v2/D4E12AQEKd-h6kjuriA/article-inline_image-shrink_1000_1488/B4EZcIiZF.HsAQ-/0/1748194923633?e=1795651200&v=beta&t=B1NheSWSKsjmsgi6K39U8gSACab9IjV1MbQM1MTGajM)

**Ruby Puts Statement Output for Nodes and Links Stats from the InfoSewer Simulation Run**

> **Ruby Puts Statement Output for CSV for Observed Predicted Graphs in ICM InfoWorks**

![](https://media.licdn.com/dms/image/v2/D4E12AQE8wynnhSsfvA/article-inline_image-shrink_1500_2232/B4EZcIiss.GQAU-/0/1748195003717?e=1795651200&v=beta&t=Ti2bh-EOHRmUpJTFEcQSy9ukPG95SyADcPy9dySZkmU)

**Ruby Puts Statement Output for CSV for Observed Predicted Graphs in ICM InfoWorks**

> **Where is the code? 01 InfoWorks ICM/01 Ruby/02 SWMM/0014 - InfoSewer to ICM Comparison Tools on the Innovyze GitHub**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0014 - InfoSewer to ICM Comparison Tools](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0014%20-%20InfoSewer%20to%20ICM%20Comparison%20Tools)

![](https://media.licdn.com/dms/image/v2/D4E12AQFX1aoHvuvs7Q/article-inline_image-shrink_1000_1488/B4EZcIgyNpHcAY-/0/1748194501887?e=1795651200&v=beta&t=T5ffI9W0WRXBVTCeYGttm87pp-YcUaKRNZBi2hPm8J8)

ui.script Read InfoSewer Steady State Report File,rb and ui.script Read InfoSewer Steady State Report File.md
