---
title: "A Better Workflow for InfoSWMM to ICM SWMM Network Conversions for ALL InfoSWMM Scenarios and Active Elements into One ICM SWMM Network"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/better-workflow-infoswmm-icm-swmm-network-conversions-dickinson-1tgxe
created: "2024-05-30 20:49"
published: "2024-06-02 21:57"
words: 2403
export_sha256: f62299438b68d2ff6988dccc844c7a2dbfd261fb42b7ab65a80b56616f271c7f
---
# A Better Workflow for InfoSWMM to ICM SWMM Network Conversions for ALL InfoSWMM Scenarios and Active Elements into One ICM SWMM Network

![A Better Workflow for InfoSWMM to ICM SWMM Network Conversions for ALL InfoSWMM Scenarios and Active Elements](https://media.licdn.com/mediaD4E12AQHCF0xD58Msfg "A Better Workflow for InfoSWMM to ICM SWMM Network Conversions for ALL InfoSWMM Scenarios and Active Elements")

The direct import of an InfoSWMM.mxd file and its associated.ISDB folder as a model group is a straightforward process that efficiently imports the node, link, subcatchment, and ancillary data from a single scenario. However, when dealing with multiple scenarios, the current workflow requires the creation of separate networks for each scenario, which can be time-consuming and inefficient.

To streamline this process, an improved workflow is proposed that leverages the existing menu tool and incorporates Ruby scripting to enhance functionality. The suggested workflow is as follows:

1\. Using Ruby scripting, import the scenario names from the InfoSWMM file into the base scenario of the ICM SWMM network. This step ensures that all relevant scenarios are accurately captured and available within the base network.

2\. After importing the scenario names, it is recommended that the imported data be saved as CSV files. This allows for easy data management and provides a backup of the imported information.

3\. Utilize Ruby scripting to import the CSV files into the corresponding scenario names within the base network. This automated process ensures that the data is accurately assigned to the appropriate scenarios, saving time and reducing the risk of manual errors.

4\. Leverage the direct import of an InfoSWMM.mxd file and its associated.ISDB folder as a model group is a straightforward process that efficiently imports the node, link, subcatchment, and ancillary data from a single scenario. However, when dealing with multiple scenarios, the current workflow requires the creation of separate networks for each scenario, which can be time-consuming and inefficient.

To streamline this process, an improved workflow is proposed that leverages the existing menu tool and incorporates Ruby scripting to enhance functionality. The suggested workflow is as follows:

1\. Using Ruby scripting, import the scenario names from the InfoSWMM file into the base scenario of the ICM SWMM network. This step ensures that all relevant scenarios are accurately captured and available within the base network.

2\. After importing the scenario names, it is recommended that the imported data be saved as CSV files. This allows for easy data management and provides a backup of the imported information.

3\. Utilize Ruby scripting to import the CSV files into the corresponding scenario names within the base network. This automated process ensures that the data is accurately assigned to the appropriate scenarios, saving time and reducing the risk of manual errors.

4\. Leverage the imported facility sets from InfoSWMM to define active and inactive elements in the ICM SWMM network. By utilizing the facility sets, you can efficiently manage the visibility and inclusion of specific aspects within each scenario, enhancing the flexibility and control over the model.

This improved workflow combines the power of the existing menu tool with the automation capabilities of Ruby scripting. By importing scenario names, saving data as CSV files, automating the import process, and utilizing facility sets, you can significantly reduce the effort required to work with multiple scenarios in ICM SWMM. This streamlined approach saves time and promotes data accuracy and consistency throughout the modeling process.e imported facility sets from InfoSWMM to define active and inactive elements in the ICM SWMM network. By utilizing the facility sets, you can efficiently manage the visibility and inclusion of specific aspects within each scenario, enhancing the flexibility and control over the model.

> **1: Starting point. In a new Model group, use the Menu command Import SWMM/Model Group/from InfoSWMM**

![](https://media.licdn.com/dms/image/v2/D5612AQHiXpZKnesTqA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721184950627?e=1795651200&v=beta&t=RcwOH3ewtmOTmWZCV5ql7MJL6jVxnWUMFklsgZa8RsQ)

Starting point. Use the menu command Import SWMM/Model Group/from InfoSWMM in a new Model group.

> **2: Find a MXD file and make sure the MXD file has an associated ISBD folder (all of the data is in this folder)**

![](https://media.licdn.com/dms/image/v2/D4E12AQGa4hZSILNPjA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721177894773?e=1795651200&v=beta&t=AvooZrWqcNihmRS3eSw9cGLtO_dM204vwM3c5RXKVrw)

Find a MXD file and make sure the MXD file has an associated ISBD folder (all of the data is in this folder)

> **3: What is a MXD file and ISDB folder?**

- ISDB Folder: This folder contains the DBF (Database File) model network and ancillary data. The ISDB folder is crucial, as it stores the information required for the InfoSWMM project. It includes data related to the network elements, such as nodes, links, subcatchments, and other relevant components.

- MXD File: The MXD file is the ArcGIS map document representing the InfoSWMM project. It is compatible with various versions of ArcGIS, including 10.3, 10.4, 10.5, 10.6, 10.7, and 10.8,. The MXD file is the main interface for visualizing and interacting with the InfoSWMM project within the ArcGIS environment.

- Other Files: An InfoSWMM project may include other supporting files in addition to the core files. Common examples are TIF (Tagged Image File) files, which are often used to represent background imagery or additional data layers. These files enhance the visual representation and provide context for the InfoSWMM project.

- OUT Folder: The OUT folder is designated to store the model output generated from different scenarios within the InfoSWMM project. It serves as a centralized location to access and analyze the simulation results. It has the files (if the model was run) hydqua.rpt.txt, hydqua.out, hydqua.inp, and hydqua.html OUT is similar to the SWMM5 binary output file.

- 

![](https://media.licdn.com/dms/image/v2/D4E12AQHd82SNuddyDQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721194536500?e=1795651200&v=beta&t=aCwQUwKkEqv7ciIpXCfZkaYdHQpnqwmpy8qStvpWPX4)

**What is an MXD file and ISDB folder?**

> **4: What is imported from InfoSWMM? All but how is it organized?**

Steps for importing an InfoSWMM model into an ICM SWMM network:

1\. Importing as a New Network:

\- In the ICM SWMM Explorer Window, right-click on the applicable Model Group where you want to import the new network.

\- Select "Import SWMM Model from InfoSWMM" from the context menu.

\- This will open a Windows File Open dialog to select the InfoSWMM .mxd file to be imported.

2\. Updating an Existing Network:

\- Open the existing SWMM network that you want to update with the InfoSWMM model.

\- From the Network menu, select "Import Model from InfoSWMM".

\- Again, this will open the Windows File Open dialog to select the .mxd file to be imported.

3\. Selecting the Import Options:

\- In the File Open dialog, enter the path to the .mxd file you want to import.

\- From the "Encoding" dropdown, select the appropriate encoding system used in the InfoSWMM text files (ANSI, UTF-8, or UTF-8 BOM).

\- Click "Open" to start the import process.

4\. Importing Scenarios (if applicable):

\- If the InfoSWMM network includes any scenarios, a window will display a list of the available scenarios that can be imported.

\- Select the relevant scenario you want to import and click "OK".

5\. Import Completion:

\- The .mxd file and any associated model data from the InfoSWMM ISDB folder will be imported into the ICM SWMM network.

Upon completion, a log file containing any conversion errors or warnings encountered during the import process will be displayed.

Important Notes:

\- File-based time series are not supported in ICM and will result in an import error.

\- If a scenario was imported, the scenario name would be appended to the imported items in the Explorer window in the format "\<mxdfilename\>\_\<scenarioname\>."

This import process allows you to leverage the work done in an existing InfoSWMM model and seamlessly integrate it into an ICM SWMM network, saving time and effort in setting up the model.

![](https://media.licdn.com/dms/image/v2/D4E12AQEKOWIZQBHA3g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721192083690?e=1795651200&v=beta&t=4_8xse3l7E08xYawJZb9UsYeCO3UvE-hUS_MOCYuUo8)

**What is imported from SWMM5 or InfoSWMM?**

> 5: Import all of the needed Scenarios using the Menu Tool **(Step 2)**

![](https://media.licdn.com/dms/image/v2/D4E12AQFiY9ZHxK4lMw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721199199430?e=1795651200&v=beta&t=F7KFgNy5yN3bcIHBE3qvpan7Nngx6qZ-HpJ7LRYPfpY)

Import all of the needed Scenarios using the Menu Tool **(Step 2)**

> **6: Use the Ruby Script Step25_User_123_ICM_Scenario_csv.rb to create all Scenario IDs in the Base Scenario**

[![](https://media.licdn.com/dms/image/v2/D4E12AQHzKFCljNUJmg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721195183049?e=1795651200&v=beta&t=02O69l8SIqsXXRYkC-hbLQ1Igz1lL2-fUXheIFtQdAE)](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0100%20-%20ODIC%20and%20SQL%2C%20Ruby%20%20Scripts%20for%20Importing%20InfoSewer%20to%20ICM)

**Use the Ruby Script Step25_User_123_ICM_Scenario_csv.rb to create all Scenario IDs in the Base Scenario.**

> **7: Validate and Commit the Validated Network Scenarios**

![](https://media.licdn.com/dms/image/v2/D4E12AQHdUu-UM4VP5g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195129067?e=1795651200&v=beta&t=b3KKicv7PSeNHp7BjqN401GbOH4vsI21CEybqFOSOjc)

**Validate and Commit the Validated Network Scenarios**

> **8: Export all of the validated Scenaros to a CSV file**

When you have imported specific scenarios from an InfoSWMM model as standalone ICM SWMM networks, you can efficiently add their components to your Base ICM SWMM network. To do this, use the Network export to CSV files feature in ICM SWMM, selecting the "One file" option to minimize the number of CSV files generated. This should be done only for the imported InfoSWMM scenarios you want to incorporate into your Base ICM SWMM network.

![](https://media.licdn.com/dms/image/v2/D4E12AQFp90fArU-IJQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721194112911?e=1795651200&v=beta&t=zKzrtxjZIizouXuHQK5n1iDot9G67NE5HEWjeVgGAI0)

**Export all of the validated Scenarios to a CSV file (one)**

> **9: Import all of the validated Scenarios from the CSV file (Step 4) into the Base Scenario created in Step 6.**

First, please ensure the Base ICM SWMM network is open on the GeoPlan. Then, you can select the specific scenario you want to import from the imported InfoSWMM data. This is one of the standalone scenario networks you created earlier.

With the desired scenario selected, locate the CSV file you exported for that scenario using the "Network export to CSV files" feature in ICM SWMM. Finally, import the relevant CSV file into the base ICM SWMM network. This will seamlessly integrate the components from the imported InfoSWMM scenario into your base ICM SWMM network.

Following this process, you will now have a single base ICM SWMM network that contains both the original base scenario and the selected scenario(s) imported from the InfoSWMM model. This streamlined approach ensures you have all the necessary data in one centralized location for your modeling and analysis needs.

![](https://media.licdn.com/dms/image/v2/D4E12AQFvXV0v3ruc8Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721193827009?e=1795651200&v=beta&t=-E6oh9RArqcT-qbi2H_Q9RHJ3JjS7sPeefTUm6010V8)

**Import all validated Scenarios from the CSV file (Step 4) into the Base Scenario created in Step 6.**

> **10: Use the Selection Lists imported for each Scenario and drag them to the Geoplan for the selected scenario IN the Base model**

Here is a step-by-step process:

1\. **Import the InfoSWMM Model and Scenarios:**

\- Import the InfoSWMM model into your ICM SWMM network, including any available scenarios. **This should already have been done in previous steps.**

2\. **Switch to the Base Scenario:**

\- In the Explorer Window, ensure you are working in the Base scenario of your ICM SWMM network.

3\. **Add the Selection Lists to the Geoplan:**

\- Go to the Geoplan view in the Base scenario.

\- Locate the Selection Lists that were imported from the various InfoSWMM scenarios.

Drag and drop these Selection Lists onto the Geoplan for each scenario. You need to select the correct scenario before dragging the Selection list onto the Geoplan.

4\. **Identify Scenario-Specific Selection Lists:**

The Selection Lists specific to a particular imported scenario will be displayed in red on the Geoplan.

5\. **Use the Inverse Selection Icon:**

\- In the Geoplan, click the "Inverse Selection" icon (usually represented by a triangle or arrow).

\- This will select all the inactive or excluded elements from the imported InfoSWMM model for this scenario.

6\. **Mark Excluded Objects as Red:**

\- With the inactive/excluded elements selected, the color is red on the Geoplan.

\- This will visually distinguish the excluded objects from the active ones.

7\. **Delete the Excluded Objects:**

\- Now, delete the red-colored objects from the Geoplan.

\- These deleted objects will now be considered as "excluded objects" in your ICM SWMM network. Note that this should not be done for the Base Scenario in ICM.

By following this process, you can:

1\. Import the complete InfoSWMM model and scenarios into your ICM SWMM network.

2\. Identify the scenario-specific Selection Lists and add them to the scenario in the Base scenario.

3\. Easily distinguish and remove the excluded objects from the imported model.

This approach ensures that your ICM SWMM network accurately reflects the imported InfoSWMM model with the appropriate active and excluded elements.

![](https://media.licdn.com/dms/image/v2/D4E12AQFsF3jsNtuW8w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721198925044?e=1795651200&v=beta&t=znHZeDL1xMec5LOUGd_22o99rSkGLG0_-QLJlgE5dPg)

**Use the imported selection lists for each Scenario and drag them to the Geoplan for the selected scenario in the Base model.**

> **11. You can convert any of the imported ICM SWMM Networks from InfoSWMM to an ICM InfoWorks Network**

Note that only one scenario is imported, but this can be amended using Ruby or again by converting each scenario as a standalone network and then using the export and import CSV files to create both the Base and Scenarios from InfoSWMM in ICM InfoWorks.

![](https://media.licdn.com/dms/image/v2/D4E12AQGXE_JPbqUaog/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721193438452?e=1795651200&v=beta&t=Vc9cXuDFR0xjLqMJ__DvogSZ04brcmcmRIiw7ucQw7I)

**You can convert any of the imported ICM SWMM Networks from InfoSWMM to an ICM InfoWorks Network.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFvckwyBrGB-A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721194342011?e=1795651200&v=beta&t=6t_ymV1Afv0jWL_CRJHUmE4p4lX9D4cB4kfhDb9D_es)

**You can convert any of the imported ICM SWMM Networks from InfoSWMM to an ICM InfoWorks Network**

**Closing Note:** Thank you for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated.

![](https://media.licdn.com/dms/image/v2/D4E12AQF9_m9bwdWxlA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721194034633?e=1795651200&v=beta&t=hNUryDZEufQH7fw52UVxzsS0p8ylBgVusKmjzEZqCkc)

A Midjourney Mixed AI Image
