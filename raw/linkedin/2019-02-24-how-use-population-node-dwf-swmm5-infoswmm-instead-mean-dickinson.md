---
title: "How to Use Population at a Node for DWF in SWMM5 and InfoSWMM instead of Mean DWF"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-population-node-dwf-swmm5-infoswmm-instead-mean-dickinson
created: "2019-02-24 07:30"
published: "2019-02-24 08:21"
words: 439
export_sha256: 7be10c003b217a205853294a9cab82b71971634e336514cb43fe372d03a4a3b6
---
# How to Use Population at a Node for DWF in SWMM5 and InfoSWMM instead of Mean DWF

![How to Use Population at a Node for DWF in SWMM5 and InfoSWMM](https://media.licdn.com/mediaC4E12AQH2YJh9_vFb9w "How to Use Population at a Node for DWF in SWMM5 and InfoSWMM")

## How to Use Population at a Node for DWF in SWMM5 and InfoSWMM

The Storm Water Management Model (SWMM5) engine is a tool used to simulate and analyze the flow of water in a stormwater system. One of the features of the SWMM5 engine is the ability to model dry weather flow, which is the flow of water in a stormwater system during periods of no or low rainfall.

Traditionally, the SWMM5 engine uses mean flow as the dry weather flow value rather than population. However, the SWMM5 engine does allow for the use of weekday, weekend, daily, and monthly patterns in the dry weather flow model. This means you can use these pattern options to incorporate population data into the dry weather flow model in SWMM5.

To use population data in the dry weather flow model in SWMM5, you can follow these steps:

1.  Use the "Population" value in the "Value" field of the dry weather flow table.
2.  Use the "Per Capita flow" value in the "Monthly Pattern" field of the dry weather flow table.
3.  Add a "Weekday pattern" to the dry weather flow table.
4.  Add a "Weekend pattern" to the dry weather flow table.
5.  If needed, perform a conversion from the per capita units to the current units of SWMM5 or InfoSWMM. This may be necessary if the per capita flow values are in a different unit of measurement than the current unit of measurement in the SWMM5 or InfoSWMM model.
6.  Following these steps, you can use population data in the dry weather flow model in SWMM5 and InfoSWMM. This can help you more accurately model the flow of water in a stormwater system and better understand the impacts of population on the system.

> This can make SWMM5 and InfoSWMM similar to Innovyze products XPSWMM, ICM and InfoSewer as regards using population as the core loading for DWF generation in your sanitary or combined network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/C4E12AQGeVIGKjy0SWQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1550996216385?e=1795651200&v=beta&t=MF6rHyy3GOFofvazYDzBemxu9pBy09NW6eE6UsT_SXE)

You can use the Field Alias Tables to change the ID's of the DWF DB Tables in InfoSWMM.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/C4E12AQGV-O6hBl-TrA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1550996413677?e=1795651200&v=beta&t=TjyZIrLiwtUqeWOB1Rh7updh3lJs-aE46WM5MEO9cqU)

\[embedded item\]

\[embedded item\]

\[embedded item\]
