---
title: "InfoWorks ICM Example SQL Scripts for Flawless Import of InfoSewer Data"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/infoworks-icm-example-sql-scripts-flawless-import-data-dickinson
created: "2023-09-10 21:58"
published: "2023-09-11 01:06"
words: 1589
export_sha256: 826b0a99cfa7644f14e3ae98d0f9f67ac4cc2d77ae8341365131d7c0c2ff6fd3
---
# InfoWorks ICM Example SQL Scripts for Flawless Import of InfoSewer Data

![SQL Scripts for Post ODIC Import of InfoSewer DBF Files](https://media.licdn.com/mediaD4E12AQEV_TLf6X6OWw "SQL Scripts for Post ODIC Import of InfoSewer DBF Files")

These SQL scripts are part of the ODIC CFG Import process to convert or import InfoSewer model data to an ICM InfoWorks Network. The [Innovyze GitHub](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0100%20-%20ODIC%20and%20SQL%20Scripts%20for%20Importing%20InfoSewer%20to%20ICM) has the CFG Files, SQL files and many markdown md files to explain this process. I wanted to go a bit deeper into how SQL works in the creation of new table data and data clean up after importing the InfoSewer data (Figure 1).

![](https://media.licdn.com/dms/image/v2/D4E12AQFtxqb8n_J9WQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1694386817401?e=1795651200&v=beta&t=8YDIcRNqgL-WHjqvBi1qI45nT7Fdr3lzbR32tUYkFVw)

**Figure 1. InfoSewer to ICM InfoWorks Network GitHub Files**

> **SQL 1/ Problem 1 - Solution 1.** InfoSewer has loading at a Node and ICM has Loading on the Subcatchment

To elegantly address the challenge of incorporating load-specific nodes into the ICM model, we create new Subcatchments in ICM that are linked to the Node ID of each ICM unit. Utilizing the SQL "WHERE" clause, we meticulously filter out Chamber nodes, Wet Wells, and Outfalls, focusing exclusively on Manholes, as these are the only node types with associated loads in InfoSewer.

In this refined approach, we generate placeholder subcatchments that share the same x and y coordinates as their corresponding nodes. Following this initial setup, we employ the Geoplan tool to meticulously craft the boundaries for these dummy subcatchments. Although the SQL script is executed within the Node layer, the ingenious use of the Insert Field command allows us to seamlessly introduce data into a brand-new Subcatchment on the Subcatchment Grid.

The SQL script initiates by populating the 'subcatchment' table with new records based on specific conditions met in the 'node' table. It employs the INSERT INTO command to add these new entries, specifying the fields to be populated as 'subcatchment_id', 'node_id', 'total_area', 'x', 'y', and 'connectivity'. To fetch the corresponding values for these fields, the script uses a SELECT statement targeting the 'node' table. Within this SELECT operation, the 'total_area' is preset to 0.10, and 'connectivity' is fixed at 100 for each new record. Finally, the script filters the records to be inserted by only selecting those where the 'node_type' from the 'node' table is identified as 'Manhole'.

> **SQL 2/ Problem 2 - Solution 2.** The on and off levels are depths in InfoSewer but elevation in ICM InfoWorks

In the SQL script, we dynamically update two key parameters: and , based on the elevation of the chamber floor. This is achieved by adding the value, sourced from the 'spatial' table, to both of these switch levels. Specifically, the is augmented by the chamber floor elevation to generate a new, context-aware threshold for activation. Similarly, the is also updated by adding the same chamber floor elevation, thereby providing a more accurate and site-specific deactivation level. This nuanced approach ensures that the switch levels are consistently aligned with the physical characteristics of the chamber.

> **SQL 3/ Problem 3** - Solution 3. Node area is defined by diameter in InfoSewer but Area in ICM InfoWorks.

In the SQL script, two critical area calculations are performed for different components—namely, the chamber and the shaft. Utilizing the mathematical constant Pi (approximated as 3.14159) and a radius squared value of 4, the areas for both the chamber and the shaft are set. Following each of these calculations, a SELECT query is executed to fetch records specifically where the 'user_text_10' field is designated as 'Manhole'.

![](https://media.licdn.com/dms/image/v2/D4E12AQE5lpeHNwwhPA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1694388854527?e=1795651200&v=beta&t=g_ljIVrZVYUreHZvpJpTOhOWVtJspvDprEBuKRh6VFk)

Figure 2. There are three manhole areas in ICM vs the One In InfoSewer

> **SQL 4/ Problem 4** - Solution 4. Node flows are cfs, gpm, lps or cms in InfoSewer but defined by population in ICM and a per capita / day flow in the WasteWater Pattern

In the SQL script, the 'population' variable undergoes a specific conversion to a per-second basis by dividing it by 86,400.0, the total number of seconds in a day. This preliminary step is pivotal for calculating the per capita flow in wastewater (WW) profiles, where the initial unit of measurement is 1 cubic foot per day (cf/day). However, the ultimate goal is to express the final flow in terms of cubic feet per second (cfs). To achieve this, an internal conversion from cf/day to cfs is performed, ensuring that the final flow rates are aligned with this desired unit of measurement. The script thus serves as a multi-step conversion tool that starts with population-based calculations and culminates in flow rates expressed in cfs.

> **SQL 5/ Problem 5** - Solution 5. Force Main in InfoSewer use HW but we do not want to use the FM solution in ICM but the Full Solution.

In the SQL script, several targeted updates are made to various fields based on specific conditions. First, the 'user_text_9' field is set to 'FM' for records where the 'bottom_roughness_N' value exceeds 1, serving as a unique identifier for these particular cases. Next, the 'user_number_9' field is updated to mirror the value of 'bottom_roughness_Manning' for records also exceeding a 'bottom_roughness_N' of 1, thereby ensuring numerical consistency across different data fields. Furthermore, any record with a 'bottom_roughness_N' greater than 1 is normalized by resetting this value to 0.014. A similar correction is applied to the 'top_roughness_N' field, setting it to 0.014 for records where it exceeds 1. These operations collectively serve as a multi-faceted tool for data harmonization and correction, making the database more consistent and reliable.

> **SQL 6/ Problem 6- Solution 6.** InfoSewer has Wet Wells but since ICM has very flexible Manhole we do not need to use a Storage node. This code converts Wet Well data to Manhole data.

In the SQL script, several calculated updates and queries are executed to refine parameters related to Wet Wells (WW). Initially, the chamber area is recalculated using the formula for the area of a circle (��2*πr*2), where the radius is determined as half of the original 'chamber_area'. Following this, a SELECT query is issued to retrieve records specifically designated as Wet Wells in the 'user_text_10' field. A similar computational approach is employed for recalculating the shaft area, utilizing the circle area formula and a radius that is half of the initial 'shaft_area'. This is followed by another SELECT query aimed at isolating Wet Well records. The script further updates the 'chamber_roof' by adding the 'chamber_floor' value, yielding an absolute height for the chamber roof. Likewise, both 'ground_level' and 'flood_level' are adjusted to be relative to the chamber floor by adding its value to them. These combined operations serve to standardize and enhance the Wet Well-related parameters in the database, ensuring greater accuracy and contextual relevance.

> **SQL 6/ Problem 6- Solution 6.** InfoSewer has barrels and ICM has barrels but often the barrels in InfoSewer are blank (the default is 1) but when importing ICM thinks the barrels are blank

In the SQL script, a targeted update is made to the 'number_of_barrels' field. Specifically, any record with a 'number_of_barrels' value of zero is updated to have at least one barrel. This adjustment is crucial for preventing potential issues that could arise in subsequent calculations or interpretations involving this field.

> **SQL 7/ Problem 7- Solution 7.** InfoSewer has no manhole inverts, only a manhole rim elevation and link elevation inverts.

In the SQL script, a series of updates are made to height-related fields like 'ground_level,' 'flood_level,' and 'chamber_roof' to ensure logical and consistent values throughout the database. Initially, 'ground_level' is set to be one unit above 'chamber_roof' where its value is either zero or null, rectifying instances where it may be missing or incorrect. Furthermore, 'ground_level' is also updated to be above 'chamber_roof' in cases where it is found to be less than 'chamber_roof,' reinforcing the logical relationship between these two height metrics. Similarly, 'flood_level' is adjusted to be one unit above 'chamber_roof' where it falls below this value, ensuring that flooding will occur only above the chamber roof. Lastly, if 'chamber_roof' is found to be lower than 'chamber_floor,' it is updated by adding the value of 'chamber_floor' to it, guaranteeing that the roof is always higher than the floor.

> **SQL 8/ Problem 7- Solution 8.** InfoSewer lacks information on the type of link as we read only CSV files. We find the pumps in this example and delete the found pumps from the conduit table.

In the SQL script, a two-step operation is conducted to manage records related to pumps. Initially, new records are inserted into the 'pump' table, sourced from the 'link' table. Specifically, the fields 'us_node_id,' 'ds_node_id,' and 'asset_id' are directly fetched from the 'link' table, while the 'link_suffix' is statically set to '2' for each new entry. This insertion is conditional and only occurs for records in the 'link' table where the 'user_text_10' field is marked as 'Pump.' Following this insertion, the script proceeds to delete any records from the 'link' table that have 'user_text_10' set to 'Pump,' thereby avoiding the potential for duplicate or unnecessary entries. The dual action of adding specific records to the 'pump' table while removing them from the 'link' table serves to streamline the database, making it more efficient and easier to manage.
