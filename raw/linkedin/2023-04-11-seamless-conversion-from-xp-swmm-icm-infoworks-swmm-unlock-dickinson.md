---
title: "Seamless Conversion from XP-SWMM to ICM InfoWorks and SWMM Networks: Unlock the Power of a Single XPX File for Dual Hydraulic Integration"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/seamless-conversion-from-xp-swmm-icm-infoworks-swmm-unlock-dickinson
created: "2023-04-09 20:46"
published: "2023-04-11 05:38"
words: 1174
export_sha256: 95aeee3b4e70f9b04398bcc2dc6403295e0178bfefc22354dfd6f5e28e70f039
---
# Seamless Conversion from XP-SWMM to ICM InfoWorks and SWMM Networks: Unlock the Power of a Single XPX File for Dual Hydraulic Integration

![](https://media.licdn.com/mediaD4E12AQGXxdxe257CYA)

The goal is to streamline exporting data from XPSWMM and importing it into both ICM SWMM and ICM InfoWorks networks, enabling efficient model data management and analysis. Following the steps outlined below, users can validate and run both networks using inflow data from the model group import.

Step 1: Exporting data from XPSWMM

- Begin by exporting a text-based XPX file from your XPSWMM model. This file contains all the necessary model data, including network components and parameters.

Step 2: Importing data into ICM SWMM and ICM InfoWorks networks

- Next, import the exported XPX file into ICM SWMM and ICM InfoWorks.
- For ICM SWMM, import the model group data, which includes all necessary hydraulic and hydrologic information.
- For ICM InfoWorks, only import the network data, as this software focuses primarily on network analysis and does not require model group information.

Step 3: Validating and running the networks

- Once the data has been imported into both software platforms, validate each network to ensure no errors or inconsistencies.
- After validating both networks, run them using the inflow data from the model group import. This will allow you to analyze and compare the hydraulic performance of the networks across both ICM SWMM and ICM InfoWorks platforms.

Following these steps, you can effectively export data from XPSWMM and integrate it into ICM SWMM and ICM InfoWorks networks, allowing for comprehensive analysis and comparison of hydraulic performance. This streamlined approach can save time and effort for engineers and modelers, facilitating a more efficient workflow.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGWCwrxSds9Lg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1681073375223?e=1795651200&v=beta&t=lthEYfH_Q7qZk_0W5d7hAotBrtsbeAnXvdaokoYNhgc)

Hydraulics Only XPSWMM Model

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEdYT5Smkup9w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1681184861733?e=1795651200&v=beta&t=PxbWQh20ysMQY_Iyp442RNBdvPbgGqaZlqbKhq8vsXE)

The XPX file is imported to an SWMM network and model group.

> The XPX file is used in the import to an SWMM network and model group. It does import the XPX as a Model Group, and you use the Model Group Inflow and other files in the InfoWorks network.

> Run Dialog for an ICM SWMM model. This is made directly as part of the import process.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQG1QDJUlFh3MA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1681184888178?e=1795651200&v=beta&t=tlKRteThGX49aoeroAvd5HTV6vPPQGonpvxxeC3SCLA)

Run Dialog for an ICM SWMM model.

> SWMM and InfoWorks will import the XPX file, but if this is not done exactly, there is a workaround using the text XPX file for the inflows.

The hydraulic inflow time series data is crucial in running and analyzing hydraulic models in ICM SWMM and ICM InfoWorks networks. To efficiently manage this data, the QCARD line of the XPX file can be utilized for extracting the inflow time series data and creating compatible files for each software platform. The steps outlined below explain how to achieve this:

Step 1: Extracting inflow time series data from the XPX file

- Locate the QCARD line in the exported XPX file from XPSWMM. This line contains the hydraulic inflow time series data necessary for running the models in ICM SWMM and ICM InfoWorks.
- Extract this data and save it in a separate file for further processing.

Step 2: Creating compatible files for ICM SWMM and ICM InfoWorks

- Convert the extracted inflow time series data into an ICM Inflow CSV file. This file format is compatible with ICM SWMM and can be easily imported into the software for hydraulic analysis.
- Also, create a QIN file containing the same inflow time series data for the SWMM engine. This file will enable the engine to read and process the inflow data effectively. **Note - this is done automatically with the SWMM engine.**

Step 3: Importing inflow data into ICM SWMM and ICM InfoWorks

- Import the ICM Inflow CSV file into ICM SWMM, ensuring the hydraulic model incorporates the necessary inflow data for accurate analysis.
- For ICM InfoWorks, use the QIN file created in Step 2 to provide the engine with the required inflow data.

Following these steps, you can efficiently handle hydraulic inflow time series data from the XPX file and create compatible files for ICM SWMM and ICM InfoWorks. This process streamlines the integration of XPSWMM data into both software platforms and enables modelers to run and analyze hydraulic models easily.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEd32XUH0MvfQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1681184907629?e=1795651200&v=beta&t=a-WbBhmHk_VUxp0gq9xw1bR1jzEihfu67WtO2_KkQ6k)

The first inflow time series that was used in XPSWMM.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQE99qDfwsGl_g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1681188039079?e=1795651200&v=beta&t=MX1IPJQU-8Gjh0YFfn2tbplCHmB5vWHgVePYpBJC-Qo)

The inflow time series that was imported to ICM SWMM.  
  

```
  --------------------------------------------------------------------
    Innovyze Storm Water Management Model
  ---------------------------------------------------------------------

  ---------------------------------------------------------------------

  Version                        = 26.0.91
  Platform                       = 64-bit (x64)
  Build date                     = 16/03/2023
  Copyright                      = Copyright (c) 2023 Innovyze
  SWMM version                   = 5.2.002
  Computer name                  = REMOL9CTW0N2
  Architecture                   = 64-bit
  CPU Type                       = Intel(R) Xeon(R) CPU E3-1535M v6 @ 3.10GHz
  Number of Cores                = 8
  RAM (GB)                       = 32
  ----------------------------------------------------------------------A
```

The SWMM Engine used is based on EPA SWMM 5.2.2, and you can find the engine in the text RPT file of ICM SWMM Output.

> The XPX file is used in the import to an InfoWorks network. It does not import the XPX as a Model Group but you can use the Model Group Inflow and other files in the InfoWorks network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHJFZ2cHkZ3BQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1681187410861?e=1795651200&v=beta&t=SXHpzS-MF9UjAkQXmn0CiCE9pWl_50j4FTzvx0EgpgE)

The XPX file is used in the import to an InfoWorks network.

> After validation and a RUN, you can see that InfoWorks and SWMM networks work for this small XPSWMM imported model.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEARoZvVhgq3w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1681188020345?e=1795651200&v=beta&t=cvDCzlcDioXXvjSwX4l1gRXb0Rkgw8i7pmxt1WZqQjU)

After validation and a RUN, you can see that InfoWorks and SWMM networks work for this small XPSWMM imported model.

> You can use Ruby to see the means of the imported model data.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQG7Mr9DlCNQ6w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1681191138204?e=1795651200&v=beta&t=0GjEuhRF24BQtzGKKqmT1rKWvn-JY6uzLnJV1Nkd4LM)

You can use Ruby to see the means of the imported model data.

One Water Blog-related post about XPSWMM [https://blogs.autodesk.com/innovyze/2023/03/10/what-xpswmm-users-who-made-the-switch-to-infoworks-icm-no-longer-need-to-worry-about/?](https://blogs.autodesk.com/innovyze/2023/03/10/what-xpswmm-users-who-made-the-switch-to-infoworks-icm-no-longer-need-to-worry-about/?dysig_tid=6ad8f374c3984e69b720b883187d7862&utm_source=LinkedIn&utm_medium=social&utm_campaign=Bonfireshares&utm_content=83734)
