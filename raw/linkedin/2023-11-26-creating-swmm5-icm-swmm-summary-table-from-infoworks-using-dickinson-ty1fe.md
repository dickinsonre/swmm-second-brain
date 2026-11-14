---
title: "Creating a SWMM5 or ICM SWMM Summary Table from ICM InfoWorks Network Results Using Ruby"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/creating-swmm5-icm-swmm-summary-table-from-infoworks-using-dickinson-ty1fe
created: "2023-11-19 16:14"
published: "2023-11-26 13:08"
words: 1783
export_sha256: 6ee74d89922ad79eb5e5a03004ebeadc4a942bc91cd122e199cfe50248903679
---
# Creating a SWMM5 or ICM SWMM Summary Table from ICM InfoWorks Network Results Using Ruby

![](https://media.licdn.com/mediaD4E12AQGhMHN63m8E6g)

> **Introduction**

The objective of the article: using Ruby scripts to create a SWMM5 Runoff Summary from ICM InfoWorks output and comparing it to standard SWMM5 reports. This makes it easier to compare ICM InfoWorks to ICM SWMM, SWMM5, InfoSWMM and XPSWMM as you have the same text output comparison or in the case of XPSWMM the SWMM4 enhanced Summary table.

An additional objective of this Ruby script is to demonstrate the versatility and power of Ruby programming in creating SWMM5 Summary tables directly from ICM InfoWorks results. This tool serves as a helpful bridge, enabling users to seamlessly compare hydrological data and analyses from ICM InfoWorks with those from SWMM5. Such a comparison is a vital component of the I2S program, offering a robust framework for users to validate and cross-reference their findings across different simulation platforms. By leveraging Ruby's flexibility and efficiency, this script not only enhances productivity but also enriches the user experience in hydrological data analysis. The code for this comparison is in the subfolder 0101- ICM InfoWorks Results to SWMM5 Subcatchment Runoff Summary Table - [the GitHub can be found here](https://boards.autodesk.com/4bf242?token=a671af9e76).

> **Section 1: Understanding the Code**

The Ruby script presented here is a tool designed to streamline the process of generating SWMM5 Runoff Summary tables using output from the ICM InfoWorks engine. It's a comprehensive solution that handles various tasks: extracting data, aligning it with the data format of SWMM5 RPT files, and converting ICM InfoWorks network data into a format compatible with ICM SWMM for in-depth analysis.

**Script Workflow**

The script follows a meticulous and structured workflow:

1.  **Initialization**: It begins by incorporating the 'date' library and setting up an array to store statistical data.

2.  **Network Object Retrieval**: The script efficiently retrieves the current network object from InfoWorks, along with the list and count of time steps.

3.  **Data Extraction**: Utilizing a predefined list of result field names, the script extracts relevant data for all selected subcatchments.

4.  **Data Processing**: It then processes the data for each selected network object, iterating through results to calculate totals and track minimum and maximum values.

5.  **Time Interval Handling**: The script assumes uniform time steps, which aids in calculating the time interval necessary for integration over time.

6.  **Statistics Aggregation**: Statistical data, including sums, averages, maximums, and minimums, are compiled into an array.

7.  **Summary Display**: Finally, the script generates a neatly formatted Runoff Summary header, followed by the aggregated data for each subcatchment.

**Features**

This Ruby script is equipped with several notable features:

- **Field Customization**: Users have the flexibility to customize field names, allowing for a broad range of results such as rainfall, evaporation rate, and various surface runoff components.

- **Dynamic Time Calculation**: The script is capable of adjusting to time steps of varying lengths.

- **Efficient Data Aggregation**: It effectively gathers and summarizes data across different fields.

- **Flexibility**: The script is designed to be adaptable, allowing users to add or remove fields as necessary.

**Output**

The script's output is a detailed and well-organized Runoff Summary table, displayed in the console. This table is formatted with headers and individual data rows for each subcatchment, mirroring the layout and format of SWMM5’s RPT file. It includes all of the 12 Runoff surfaces in ICM InfoWorks. SWMM5 has only three runoff surfaces (impervious, impervious without depression storage and pervious).

> **Section 2: Setting Up the Code to read the IWR file**

The Ruby table below has the possible ICM InfoWorks output subcatchment variables. For consistency with the SWMM5 Summary Runoff Table, we will focus solely on rainfall, evaporation, infiltration, and the twelve runoff surfaces (qsurf01 to qsurg12).

> **Section 3: Creating the SWMM5 Runoff Summary with Ruby**

The Ruby script segment outlines a detailed procedure for iterating through selected objects in a network, specifically focusing on subcatchments. Here's a summary of its key functionalities:

1.  **Subcatchment Identification**: The script iterates through each selected object within the network, identifying subcatchments by checking against their IDs. It raises an exception if a selected object is not a subcatchment.

2.  **Data Processing for Each Field**:The script processes various fields (like rainfall, surface runoff components) for each subcatchment. It checks if the number of results for a field matches the count of time steps (ts_size).

3.  **Statistical Calculations**:For each field, it calculates total, minimum, and maximum values, along with the mean. It assumes time steps are evenly spaced and computes the total integrated over time, converting the units appropriately (e.g., for rainfall, the total is divided by 3600.0, and for other fields, it's adjusted based on the subcatchment's total area).

4.  **Surface Runoff Component Handling**:The script handles different surface runoff components (qsurf) by adjusting the integrated total based on the area percentage of each component.

5.  **Statistics Aggregation**:It aggregates the calculated statistics, including sum, mean, maximum, minimum values, and the count of steps for each field. These statistics are stored in an array for each subcatchment, labeled with the subcatchment ID and the specific field name.

6.  The generated script output table is shown below. **Generated SWMM5 Subcatchment Runoff Summary Table - it includes all 12 ICM InfoWorks Runoff Surfaces.**

&nbsp;

![](https://media.licdn.com/dms/image/v2/D4E12AQG4pu8OoRvZXw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1700923991427?e=1795651200&v=beta&t=JSfXgIZ4W8mIgOVkol-Q_YoT1a-FaiGBiMXdEhlY8Io)

![](https://media.licdn.com/dms/image/v2/D4E12AQGowTJ3q2-MEg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1700924015659?e=1795651200&v=beta&t=_xdW3mzoKDQ5xU3cZlP9oKQrgU93LT67cZNE6OWV4d0)

Generated SWMM5 Subcatchment Runoff Summary Table - it includes all 12 ICM InfoWorks Runoff Surfaces

> **Section 4: Converting ICM InfoWorks Network to ICM SWMM**

Now to compare ICM InfoWorks and ICM SWMM (for the Summary Runoff Table only) follow these steps for transitioning from an ICM InfoWorks Model to an ICM SWMM Model, and ensuring the model's completeness and accuracy by validating the converted model.

1.  **Conversion to ICM SWMM Model**:Begin by using the intuitive ICM User Experience (UX) and the available Menu commands to convert your existing ICM InfoWorks Model into an ICM SWMM Model. This process might need to be repeated to ensure the conversion is correctly applied.

2.  **Model Validation**:After the conversion, it's crucial to validate the new ICM SWMM Model. During this validation phase, check thoroughly for any errors or inconsistencies that might have arisen during the conversion process.

3.  **Addressing Missing Components**:One key issue to be aware of is the absence of the Rain Gage in the ICM SWMM model, which is an essential component for effective SWMM5 modeling. The Rain Gage plays a vital role in accurately simulating rainfall events and their impacts.

4.  **Integrating Rain Gage**:To resolve this, create a new point element within the ICM SWMM. Then, connect the rainfall profile from the original ICM InfoWorks model to this new element. This step ensures that the rainfall data is accurately represented in the SWMM model, maintaining the integrity and reliability of your hydrological simulations.

![](https://media.licdn.com/dms/image/v2/D4E12AQHA199FxIoByQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1700924213688?e=1795651200&v=beta&t=RtQlQtS4SjDHedRrYEVvr9MDKYomwU1mTYYiTGYWyIQ)

Using the ICM UX and Menu commands convert the ICM InfoWorks Model to an ICM SWMM Model

![](https://media.licdn.com/dms/image/v2/D4E12AQHr3QygdnZjIg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1700924226790?e=1795651200&v=beta&t=bnb1wukE5zN5B4wkMq3tN38qQiamUeDYazjdRxAJt9g)

Validate the model and see if there are any errors. ICM SWMM is missing the Rain Gage needed for SWMM5 modeling

![](https://media.licdn.com/dms/image/v2/D4E12AQGQYwQC6YANdw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1700924046543?e=1795651200&v=beta&t=90VW_h4BLPF3Uowl68zdvxEKdoGg1tBWm-G9_AWtd6U)

Validate the model and see if there are any errors. ICM SWMM is missing the Rain Gage needed for SWMM5 modeling, Click on the validation message to see the needed data.

![](https://media.licdn.com/dms/image/v2/D4E12AQH9FXPhmuXH8w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1701002894411?e=1795651200&v=beta&t=R0t7ZxkLu_w38MngbJVMdJNUTtIuSai04qt0TC9HnAA)

Create a new point element in IOM SWMM and connect the rainfall profile from ICM InfoWorks

> **Section 5: Running ICM SWMM and Analyzing its RPT File**

Now we can run ICM SWMM (after committing the validated network) by making a Model Run and using the same Rainfall time series as used by ICM InfoWorks. We can now compare SWMM5 Hydrology to ICM InfoWorks SWMM hydrology.

![](https://media.licdn.com/dms/image/v2/D4E12AQGqyVGmBXEh3Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1700924250219?e=1795651200&v=beta&t=RvwBpzPr7d-3YwBL4hfYkPpIw2ECmfz9j-4aAuC8-Jw)

The Report File Summary Runoff Table from ICM SWMM with three runoff surfaces

> **Conclusion**

The primary objective of this Ruby script is to demonstrate the versatility and power of Ruby programming in creating SWMM5 Summary tables directly from ICM InfoWorks results. This tool serves as a helpful bridge, enabling users to seamlessly compare hydrological data and analyses from ICM InfoWorks with those from SWMM5. Such a comparison is a vital component of the I2S program, offering a robust framework for users to validate and cross-reference their findings across different simulation platforms. By leveraging Ruby's flexibility and efficiency, this script not only enhances productivity but also enriches the user experience in hydrological data analysis. **The link to the GitHub and Readme File is shown in the next section.**

> **Extra Markdown Readme File (from Github)**

Dive into our detailed [readme.md](http://readme.md) file on the ICM Technical Information Hub folder: "0101- ICM InfoWorks Results to SWMM5 Subcatchment Runoff Summary Table." All of the Ruby code is available on the Innovyze GitHub repository, providing you with the tools you need for seamless data transformation and comparisons. It is under **Open Source Support / 01 InfoWorks ICM / 01 Ruby in the 02 SWMM subfolder**

![](https://media.licdn.com/dms/image/v2/D4E12AQFSdqGDQY511A/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1700953561589?e=1795651200&v=beta&t=UzbeuEIkbe-mOrmel5aiefJ9s3JPW2-5w5_7CsPHm70)

Open Source Support / 01 InfoWorks ICM / 01 Ruby in the 02 SWMM subfolder

Access the code (hw_UI_script.rb) and additional resources by visiting the [ICM Technical Information Hub](https://boards.autodesk.com/4bf242?token=a671af9e76) and clicking on the Scripting section. A reminder, a prefix of hw\_ means HydroWorks (ICM now) and sw\_ means SWMM5.

![](https://media.licdn.com/dms/image/v2/D4E12AQE5jgmOz5x7iQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1700943703907?e=1795651200&v=beta&t=-XxeV9Wy2b5iap-DKEDUr6Ou-wUdZKscwvF3ooEX5LA)

Random Engineer using Ruby in Visual Studio Code

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
