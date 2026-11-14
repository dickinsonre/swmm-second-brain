---
title: "Utilizing Ruby Scripting in InfoWorks ICM to Extract Output Data and Generate SWMM5 Calibration Files with the Assistance of GPT-4"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/utilizing-ruby-scripting-infoworks-icm-extract-output-dickinson-qvq5e
created: "2023-11-04 17:22"
published: "2023-11-05 19:11"
words: 1976
export_sha256: 6aa6272b35023faa81b729e264d80e79f89ef8b228126c321e681cf283c039ba
---
# Utilizing Ruby Scripting in InfoWorks ICM to Extract Output Data and Generate SWMM5 Calibration Files with the Assistance of GPT-4

![GPT-4, DALL·E 3Created this image of an ant with mini LID's ](https://media.licdn.com/mediaD4E12AQEL8eo8367PFQ "GPT-4, DALL·E 3Created this image of an ant with mini LID's ")

We are using GPT-4, in conjunction with the SWMM5 help file, to help generate SWMM5 calibration files from InfoWorks ICM output data. The challenge arises from the difference in naming conventions between ICM (which uses a link name based on the upstream node ID and the link suffix) and SWMM5 (which uses a link name that connects the upstream and downstream node IDs). We use GPT-4 to make an asset mapping from the ICM Link Grid to rectify this problem. Ruby will be used to read the ICM InfoWorks output file and process the data accordingly. The ending code is now on the Innovyze GitHub location under the subfolder 0098 - Export SWMM5 Calibration Files.

### Step 1: Understand the Data Formats for the Links

For our use case, it's essential to align the InfoWorks ICM and SWMM5 data formats to allow for accurate data extraction and calibration file creation. Before diving into code development, it is critical to have a comprehensive understanding of the data structure in both InfoWorks ICM and SWMM5. Pay particular attention to how each system identifies links within their respective network models. In InfoWorks ICM, the convention for link IDs within the IWR results file is to concatenate the Upstream (US) Node ID with a link suffix, forming a unique identifier for each link in the network. This identifier is distinct from the one used in SWMM5, which typically involves a more descriptive naming convention, often including both the US and Downstream (DS) Node IDs.

To facilitate the generation of SWMM5 calibration files from InfoWorks ICM output, a mapping strategy is required. This involves creating a correspondence between the ICM-generated link ID (US Node ID and link suffix) and the original SWMM5 Asset ID. This is necessary because the model, initially developed in SWMM5, was imported into ICM SWMM and subsequently converted for use in InfoWorks ICM.

For instance, if a link in SWMM5 is identified by the Asset ID "C1," but in ICM it's referred to by the combination "Node123_1," you need a mapping that connects "Node123_1" back to "C1" so that the calibration file reflects the correct identifiers.

During the calibration file creation process, it is this SWMM5 Asset ID that must be utilized, as the output from the IWR file will present flow data under the field res_field_name = 'us_flow'. However, without the correct SWMM5 identifiers, the calibration file would not be functional within the SWMM5 environment.

Thus, the task at hand is to write a script that performs the following actions:

1.  Reads the output data from the IWR file, extracting flow values and corresponding link IDs.

2.  Translates the ICM link IDs into the original SWMM5 Asset IDs using a predefined mapping.

3.  Formats this data into a SWMM5-compatible calibration file, ensuring that the flow values are associated with the correct SWMM5 Asset IDs

![](https://media.licdn.com/dms/image/v2/D4E12AQGAeWTaguWslA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1699204566847?e=1795651200&v=beta&t=eq2QofGDSaBwzWXF4n4pUyc0WjBuWV3nah7SNVffMeI)

Our Link ID's in the Siphon model

How did I get GPT-4 to to this? I simply copied the first four columns of the Link Grid and asked it to make an asset mapping for the ICM Link ID to the SWMM5 Asset ID. Here is the code it supplied. The IWR file is read based on the ICM ID and then the SWMM5 calibration file is made with the mapped ID.

### Step 2: Set Up the Ruby Code for IWR ICM to SWMM5

Leveraging Visual Studio's integration with Innovyze GitHub, we streamline the workflow by directly dragging model runs into the ICM GeoPlan for visualization. To enhance this process, we execute a Ruby script—compatible with the UX Ruby environment—designed to evaluate the model's output. This script deftly confirms the number of timesteps available and focuses on extracting a singular, yet pivotal, output parameter: the upstream flow (us_flow) of each link in the network and calculates the time interval - key for the export to a SWMM5 calibration file.

### Step 3: Define the Mapping for ICM to SWMM5

GPT-4 constructed a mapping in Ruby that translates the ICM link naming convention to the SWMM5 convention. This was a hash where the keys are ICM link names and the values are the corresponding SWMM5 link names. In this case it is pretty simple as each selected ICM link is mapped to the Asset ID and the Asset ID is used in the SWMM5 calibration file.

### Step 4: Extract Data from ICM

Write Ruby code to read the output data from ICM. This will involve opening the output file, parsing its contents, and extracting the relevant data points such as flow rates at different time steps. This was not done with GPT-4 but was based on existing Ruby code in the [Innovyze GitHub](https://github.com/innovyze/Open-Source-Support) See the subfolder named **0098 - Export SWMM5 Calibration Files**

### Step 5: Transform Data for SWMM5 using GPT-4

Using the extracted data and the mapping from Step 3, transform the data into the format expected by SWMM5. This will involve iterating over the ICM data, using the mapping to translate link names, and formatting the data appropriately. Most of this step was done by GPT-4 based on me copying the format of the SWMM5 Calibration File from the the SWMM5 help file. The code it generated is shown below - there were a few iterations but the gist of the code came from OpenAi. It reads the upstream flow for each link and using a puts statement adds a row to the calibration file.

![](https://media.licdn.com/dms/image/v2/D4E12AQF-berRR7I8bA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1699209868024?e=1795651200&v=beta&t=SVLyPnoPBC732U01_Gs1w9qzix_FXkQqv2hBH4KZjhY)

SWMM5 Calibration File Format

### Step 6: Generate the Calibration File

Format the transformed data into the structure required by SWMM5 calibration files. This typically includes headers, footers, and data lines that conform to SWMM5's expected input format. The header code is shown below (again from GPT-4)

### Step 7: Handle Edge Cases and Errors

Ensure your Ruby script gracefully handles any mismatches or errors, such as missing data points or discrepancies in expected versus actual formats. That is done with the rescue code = it ignores elements that are selected and are not links.

### Step 8: Output and Review for the Ruby Output Text Box

Output the calibration file and review it to ensure it meets the requirements of SWMM5. Validate the format and the data by importing it into SWMM5 and checking for any errors. The generated file looks like a SWMM5 calibration file.

![](https://media.licdn.com/dms/image/v2/D4E12AQEoPaRBxWCLvg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1699210240855?e=1795651200&v=beta&t=OtVNuf58qz4XsQWh5YcMjmWi2ZMOFCfp9p-jI_be4Yk)

The Output of the Ruby Script - a script output text box in the form of a SWMM5 calibration file

### Step 9: Use the Generated File in SWMM5

Let SWMM5 know the Type and Location of the Calibration File by using the Project / Calibration Data Menu.

1.  **Start SWMM5 Application:** Open the SWMM5 software to access your project workspace.

2.  **Navigate to Project Menu:** Once in the main interface, locate and click on the "Project" menu option located in the top menu bar.

3.  **Select Calibration Data:** From the dropdown menu, choose the "Calibration Data" option. This will open a new dialog window specifically for managing calibration files.

4.  **Specify Calibration File Type:** Within the calibration data window, you'll have the option to specify the type of calibration data you're using. Ensure that you select the correct type that matches the data within your calibration file (e.g., flow, water quality).

5.  **Browse and Select File:** Use the provided dialog to browse to the location on your computer or network where the calibration file is saved. Once you find the file, select it so that SWMM5 knows where to look for calibration data.

6.  **Load the Calibration File:** After selecting the file, instruct SWMM5 to load the calibration data into your project. This may involve clicking an "Open" or "Load" button, depending on the version of the software.

7.  **Review Data Import:** SWMM5 should now display the calibration data within the project workspace. It's a good practice to review the imported data to confirm that it appears as expected and matches the output from your ICM model run.

![](https://media.licdn.com/dms/image/v2/D4E12AQE4buZDK5BwSw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1699210448070?e=1795651200&v=beta&t=YZKFodAk4_AtxTWqggonSwdsCK3G268iKBCE-d9OnqY)

Let SWMM5 know the Type and Location of the Calibration File

### Step 10: Does the Calibration File work in SWMM5?

Yes, it does -I see the link and observed flow displayed together in SWMM5. Directly within the SWMM5 interface, you can see the modeled link juxtaposed with the observed flow data. This visual confirmation is crucial for a quick check that the right data is associated with the correct elements in the model.

![](https://media.licdn.com/dms/image/v2/D4E12AQEiYjlovBbZOg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1699210546680?e=1795651200&v=beta&t=Wd3astKuPUOr_C8EJrY6-oCBEpWqM1qtyqcIJOUZoC8)

SWMM5 Calibration Graph

> Origin of the Exported Model

The siphon model we are using this article comes from the ICM and SWMM5 model discussed in this link [https://www.linkedin.com/pulse/icm-siphons-how-model-sediment-siphon-swmm-swmm5-robert-dickinson-i5lme/?trackingId=PqoMxL2HROmA2BrIyC%2BlXg%3D%3D](https://www.linkedin.com/pulse/icm-siphons-how-model-sediment-siphon-swmm-swmm5-robert-dickinson-i5lme/?trackingId=PqoMxL2HROmA2BrIyC%2BlXg%3D%3D)

### 🌟 SWMM5 Calibration Files Overview 🌟

Calibration files are pivotal in the modeling process, offering a comparison between real-world measurements and simulation outputs. 📈 Each file caters to a specific aspect of the water cycle or pollutant transport, allowing for targeted calibration and analysis. 🎯 Here's what each file typically contains:

- 🌧️ **Subcatchment Runoff**: Measurements of the volume of runoff generated by each subcatchment, crucial for validating surface water simulations.

- 💧 **Subcatchment Groundwater Flow**: Data on the flow of groundwater into or out of the subcatchment, aiding in calibrating subsurface hydrological models.

- 📏 **Subcatchment Groundwater Elevation**: Records of groundwater levels, which are essential to ensure the accuracy of groundwater table simulations.

- ❄️ **Subcatchment Snow Pack Depth**: Information on the depth of snow accumulation, providing insights into seasonal snowmelt and its impact on runoff.

- 🚮 **Subcatchment Pollutant Washoff**: Concentrations of pollutants washed off by stormwater, crucial for water quality modeling and pollution control strategies.

- 🌊 **Node Depth**: Data on the depth of water at network nodes, reflecting the performance of drainage systems during peak flow conditions.

- 🔄 **Node Lateral Inflow**: Measurements of lateral inflows to nodes, often used to fine-tune inflow distribution in complex network models.

- 🏊‍♀️ **Node Flooding**: Instances of overflow and flooding from nodes, providing real-world events to test the system's capacity and design thresholds.

- 🧪 **Node Water Quality**: Quality parameters at the nodes, ensuring that the simulation accurately reflects pollution levels throughout the network.

- 🚀 **Link Flow**: The rate of flow within conduits, fundamental for verifying the hydraulic performance of the modeled conduits.

- 💨 **Link Velocity**: The speed of flow in the conduits, used to assess energy gradients and sediment transport capabilities.

- 📏 **Link Depth**: The water depth in conduits, which is necessary for understanding the filling and capacity usage of the network under various conditions.

These files serve as the foundation for model calibration, ensuring that simulations faithfully replicate observed conditions. 🛠️ By meticulously comparing these detailed measurements against simulation data, modelers can refine their models, leading to more reliable and actionable insights. 🎓💼

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time!
