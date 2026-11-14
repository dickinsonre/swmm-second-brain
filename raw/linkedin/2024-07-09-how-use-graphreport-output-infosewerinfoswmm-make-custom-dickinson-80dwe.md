---
title: "How to Use the Graph/Report Output of InfoSewer/InfoSWMM to Make Observed Predicted Custom Graphs in ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-graphreport-output-infosewerinfoswmm-make-custom-dickinson-80dwe
created: "2024-07-09 12:02"
published: "2024-07-09 14:00"
words: 1092
export_sha256: ee60dbc28c9e8e68f186aa38c5de88f57f7e10f2df0a19bd70e72579f87514cd
---
# How to Use the Graph/Report Output of InfoSewer/InfoSWMM to Make Observed Predicted Custom Graphs in ICM InfoWorks

![How to Use the Graph/Report Output of InfoSewer/InfoSWMM to Make Observed Predicted Custom Graphs in ICM InfoWorks](https://media.licdn.com/mediaD4E12AQHF1oSLjpfQ-Q "How to Use the Graph/Report Output of InfoSewer/InfoSWMM to Make Observed Predicted Custom Graphs in ICM InfoWorks")

Creating custom observed-predicted graphs in ICM InfoWorks using the graph/report output from InfoSewer or InfoSWMM involves several steps. This process helps compare model predictions with observed data, enhancing the accuracy and reliability of your hydraulic and hydrologic models. Here’s a step-by-step guide to achieve this:

### 1. Export Data from InfoSewer/InfoSWMM

**a. Generate Graphs/Reports:**

- Use the Group Graph and Report buttons in InfoSewer/InfoSWMM to generate the necessary time series results for flow, depth, and velocity.

- Customize the time range and intervals to match your observed data for accurate comparison.

**b. Export Results:**

- Once the graphs/reports are generated, export the data to a CSV or Excel file. Ensure that the exported file includes time, flow, depth, and velocity columns.

### 2. Prepare Observed Data

**a. Collect Observed Data:**

- Gather the observed flow, depth, and velocity data for the same locations and time periods covered by your InfoSewer/InfoSWMM models.

- Format the observed data similarly to the exported model data for ease of comparison.

**b. Align Time Steps:**

- Ensure that the time steps in the observed data align with those in the model data. If necessary, interpolate the data to match the time intervals.

### 3. Import Data into ICM InfoWorks

**a. Create a New Database or Project:**

- Open ICM InfoWorks and create a new database or project if one doesn’t already exist.

**b. Import Model Data:**

- Navigate to the Data Import tool in ICM InfoWorks.

- Select the CSV or Excel file containing the exported InfoSewer/InfoSWMM model data.

- Map the columns to the appropriate fields in ICM InfoWorks (e.g., time, flow, depth, velocity).

**c. Import Observed Data:**

- Repeat the import process for the observed data file.

- Ensure that the observed data is correctly mapped to the respective fields.

### 4. Create Custom Graphs

**a. Open the Graphs Tool:**

- In ICM InfoWorks, open the Graphs tool from the toolbar.

**b. Select Data Sets:**

- Choose the locations (nodes, conduits, pipes) where you have both observed and predicted data.

- Select the model-predicted data series (flow, depth, velocity) and the corresponding observed data series.

**c. Customize Graphs:**

- Customize the graph settings to display both the predicted and observed data on the same plot.

- Use different colors or line styles to distinguish between observed and predicted data.

**d. Analyze and Interpret:**

- Compare the predicted results from InfoSewer/InfoSWMM with the observed data.

- Identify discrepancies and analyze the causes, such as calibration issues or unaccounted-for external factors.

![](https://media.licdn.com/dms/image/v2/D4E12AQGSaIurAmrd-A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720526987713?e=1795651200&v=beta&t=WAVMrBcpMAmGy8ra2UUdroE7JjRIvXvOPKJiiZeQTTg)

Original InfoSewer Network

![](https://media.licdn.com/dms/image/v2/D4E12AQHgGa_22lV2Bg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720527053072?e=1795651200&v=beta&t=FkWgz_ZwTeq6Z6bLHaoVbGGFyE87gMxit-lzpupnHfQ)

Accessing Time Series Results in InfoSewer/InfoSWMM

To view detailed time series data for flow, depth, and velocity:

1.  Select the 'Group Graph' option

2.  Click the 'Report' button

3.  Choose the desired parameters (flow, depth, velocity)

4.  Copy and paste to the ICM flow survey CSV file

![](https://media.licdn.com/dms/image/v2/D4E12AQE0ZhmAeY5Dmg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720527082868?e=1795651200&v=beta&t=2C7wsrTB7eMmp5oV0xCUFHcFjlqr7aOmSnczushlatU)

Imported InfoSewer Model to an ICM Infoworks Network

![](https://media.licdn.com/dms/image/v2/D4E12AQG9ZSU9DDCtrA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720527132958?e=1795651200&v=beta&t=gWNV4AuSAeUC9QWZeaOKG_vBSGl8o_BsyMZs5idGWUg)

The custom graph dialog connects the observed data from Infoswer or InfoSWMM to the predicted results of ICM InfoWorks

![](https://media.licdn.com/dms/image/v2/D4E12AQHiUjUbEkNb7g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720532619874?e=1795651200&v=beta&t=E5etZf94svk0bPrv1EUB0K0uNWpnhbOZ4lXS3s3D6NE)

The InfoSewer or InfoSWMM graph IDs are the same as the [asset.id](http://asset.id) for an ICM link so we use the folder 149 Ruby utility code to convert [asset.id](http://asset.id) to ICM link IDs

![](https://media.licdn.com/dms/image/v2/D4E12AQGdWQ30_0kNCg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720526951263?e=1795651200&v=beta&t=dmxxyVcN44LAB9xOoBVmE3tfOyealeTVhdHbQUnYjKo)

We have 315 flow locations showing Infosewer vs ICM Infoworks for depth, flow, and velocity. Flow normally matches as we have the same inflow, but depth and velocity do not match as IndoSewer does not use the full St Venant Solution. ICM does,

![](https://media.licdn.com/dms/image/v2/D4E12AQHwEZSaupPufg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720526920810?e=1795651200&v=beta&t=g010UIwOBIab9vlyfUIOu1-g8kdUeg-s05D0w1j--iY)

We have 315 flow locations showing Infosewer vs ICM Infoworks for depth, flow, and velocity. Flow normally matches as we have the same inflow, but depth and velocity do not match as IndoSewer does not use the full St Venant Solution. ICM does,

![](https://media.licdn.com/dms/image/v2/D4E12AQETmNqqi_nhuw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720531552535?e=1795651200&v=beta&t=pfmQbX9uX2-xEEiFy-8Gri9kMG4Pbv9QYkg15SLhfP0)

We have 315 flow locations showing Infosewer vs ICM Infoworks for depth, flow, and velocity. Flow normally matches as we have the same inflow, but depth and velocity do not match as IndoSewer does not use the full St Venant Solution. ICM does,

![](https://media.licdn.com/dms/image/v2/D4E12AQH3OxBfzIzLlQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720526883496?e=1795651200&v=beta&t=jldiK3PufADreRawYIxl1cKCSfn8wP9TBGVYEtp0DpQ)

We have 315 flow locations showing Infosewer vs ICM Infoworks for depth, flow, and velocity. Flow normally matches as we have the same inflow, but depth and velocity do not match as IndoSewer does not use the full St Venant Solution. ICM does,

![](https://media.licdn.com/dms/image/v2/D4E12AQF281UHYxb-TA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720526855405?e=1795651200&v=beta&t=XoY79mhHJAWssJapQdIymbptlgkOdxcuotOf0zvFLI4)

We have 315 flow locations showing Infosewer vs ICM Infoworks for depth, flow, and velocity. Flow normally matches as we have the same inflow, but depth and velocity do not match as IndoSewer does not use the full St Venant Solution. ICM does,

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
