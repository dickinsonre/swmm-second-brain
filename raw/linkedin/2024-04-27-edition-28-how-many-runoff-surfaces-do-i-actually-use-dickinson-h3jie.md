---
title: "Edition 28: How many runoff surfaces do I actually use in my ICM InfoWorks network?  Ruby can answer this question."
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-28-how-many-runoff-surfaces-do-i-actually-use-dickinson-h3jie
created: "2024-03-23 21:12"
published: "2024-04-27 23:42"
words: 2400
export_sha256: 517245d85f74d24432eda029584e8c56232f48c519b80f667f4c4fbaff3ca5b3
---
# Edition 28: How many runoff surfaces do I actually use in my ICM InfoWorks network?  Ruby can answer this question.

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 28: How many runoff surfaces do I actually use in my ICM InfoWorks network? Ruby can answer this question.](https://media.licdn.com/mediaD4E12AQGSajDAtQaRCQ "Edition 28: How many runoff surfaces do I actually use in my ICM InfoWorks network?  Ruby can answer this question.")

In an ICM InfoWorks network, each subcatchment is assigned a Land Use ID, which represents the predominant land use type within that subcatchment. Every land use has a set of associated runoff surfaces that define the hydrological characteristics of different surface types within the land use, such as pervious areas, impervious areas, and roofs.

However, the actual presence and extent of each runoff surface within a subcatchment depend on the area of the surface in the Subcatchment grid. The Subcatchment grid is a spatial representation of the subcatchment, divided into smaller grid cells. Each grid cell is assigned a specific runoff surface based on the underlying land use and surface characteristics.

Not all runoff surfaces associated with a Land Use may be present in a particular subcatchment. The presence and extent of each Runoff Surface are determined by the area it occupies within the Subcatchment Grid. If a Runoff Surface does not have a significant presence in the grid cells of a subcatchment, it may not be used in the modeling of that subcatchment.

To further complicate matters, the Land Uses and Runoff Surfaces have separate grids, which makes it challenging to visually correlate the Runoff Surface grid with the subcatchments. It is not straightforward to determine which subcatchment a specific Runoff Surface is applied to just by looking at the Runoff Surface grid.

To understand the relationship between subcatchments and Runoff Surfaces, it is necessary to analyze the Subcatchment Grid and the associated Land Use and Runoff Surface data. This may require additional tools or post-processing to extract and visualize the relevant information, such as mapping the Runoff Surface grid cells to their corresponding subcatchments.

In summary, the application of Runoff Surfaces to subcatchments in an ICM InfoWorks network is based on the area of the surfaces within the Subcatchment Grid. Not all Runoff Surfaces associated with a Land Use may be used in a particular subcatchment, and the separate grids for Land Uses and Runoff Surfaces make it challenging to visually determine the subcatchment-Runoff Surface relationships without further analysis.

**Edition 28 has 8 Sections.**

Section 1: SQL for One to One between Land Uses and Runoff Surfaces

- This section explains the Ruby code that combines land use and runoff surface variables into a single array called .

- It loops through each land use and runoff surface in the network, creating hashes with their respective variables and appending them to the array.

- The code then prints the combined variables, labeling each row as either a land use or a runoff surface based on the type of variables it contains.

Section 2: Ruby for One to One between Subs, Land Uses and Runoff Surfaces

- This section mentions that the Ruby code for the one-to-one relationship between subcatchments, land uses, and runoff surfaces can be found on their Github repository.

Section 3: Ruby for Subcatchment Grid Area or Area Percentage

- This section describes the Ruby code that retrieves subcatchment variables from the network and stores them in an array called .

- It loops through each subcatchment, creates a hash with variables such as subcatchment ID, land use ID, total area, contributed area, area measurement type, and runoff areas (absolute values and percentages), and appends the hash to the array.

- The code then prints the subcatchment variables, formatting the column labels and values for better readability.

Section 4: Ruby for Runoff Surfaces in ICM InfoWorks

- This section explains the Ruby code that retrieves runoff surface variables from the network and stores them in an array called .

- It loops through each runoff surface, creates a hash with various variables such as runoff surface ID, description, routing type and value, surface type, ground slope, initial loss, and many other parameters, and appends the hash to the array.

- The code then prints the column labels and values for the runoff surface variables.

Section 5: Ruby for Land Use in ICM InfoWorks

- This section describes the Ruby code that retrieves land use variables from the network and stores them in an array called .

- It loops through each land use, creates a hash with variables such as land use ID, population density, wastewater profile, connectivity, pollution index, description, and runoff surface indices with their corresponding default areas, and appends the hash to the array.

- The code then prints the column labels and values for the land use variables.

Sections 6-8:

- Section 6 mentions using the Current and Background Networks for Subcatchment Statistics, but does not provide further details.

- Section 7 refers to a past LinkedIn article about the 12 Runoff Surfaces in ICM InfoWorks, but does not include the content of the article.

- Section 8 states that there are no Runoff Surfaces in ICM SWMM or SWMM5 and that the runoff surface for ICM SWMM is on the Subcatchment Grid.

> **1/ Ruby for One to One between Land Uses and Runoff Surfaces**

This code combines land use and runoff surface variables into a single array called . Here's a breakdown of what the code does:

1\. It initializes the current network (\`cn\`) and an empty array called .

2\. It loops through each land use in the network using .

3\. For each land use, it creates a hash called that contains the following variables:

\- Land use ID

\- Population density

\- Wastewater profile

\- Connectivity (%)

\- Pollution index

\- Description

4\. It then adds the runoff surface indices and their corresponding default areas to the hash for each of the 12 possible runoff surfaces associated with the land use.

5\. The hash is appended to the array.

6\. After processing all the land uses, the code loops through each runoff surface in the network using .

7\. For each runoff surface, it checks if the runoff surface is used by any of the land uses by comparing the runoff surface index with the to values of each land use.

8\. If a match is found, it creates a hash called that contains the following variables:

\- Runoff surface ID

\- Description

\- Runoff routing type and value

\- Runoff volume type

\- Surface type

\- Ground slope

\- Initial loss type and value

\- Initial abstraction factor

\- Routing model

\- Fixed runoff coefficient

9\. The hash is appended to the array.

10\. Finally, the code iterates over each set of variables in the array and prints them as a row in the output.

\- If the first key of the variables hash starts with 'Land use', it prepends "Land Use" to the row.

\- If the first key starts with 'Runoff surface', it prepends "Runoff Surface" to the row.

\- Otherwise, it prints the row as is.

The output will display the combined land use and runoff surface variables, with each row labeled as either a land use or a runoff surface based on the type of variables it contains.

![](https://media.licdn.com/dms/image/v2/D4E12AQHybADXVILLdw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714249648529?e=1795651200&v=beta&t=MW_H0o6QxAkLXUBvLrs2WIuP704iuy0DnhapBZsvaQA)

Ruby Output showing the Runoff Surfaces up to 12 for each Land Use

> **2/ Ruby for One to One between Subs, Land Uses and Runoff Surfaces**

See our Github for the code in the following [section](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM)

![](https://media.licdn.com/dms/image/v2/D4E12AQFim1nE5TIIug/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714260669239?e=1795651200&v=beta&t=xCf2-gHQKBPUk_WNd49m-zLXNNmivqtqSthAvFaJZME)

Autodesk Water GitHub Folders

![](https://media.licdn.com/dms/image/v2/D4E12AQFmUVDMnZpAig/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714260256291?e=1795651200&v=beta&t=3EWcpPDHDRugN-HT7t-HwsEOOW4k3NcDe4xlwg_ZDXI)

**Ruby for One to One between Subs, Land Uses and Runoff Surfaces**

> 3/ Ruby for Subcatchment Grid Area or Area Percentage

Here's a breakdown of what the code does for the Subcatchment Grid:

1.  It initializes the current network () and an empty array called .

2.  It loops through each subcatchment in the network using .

3.  For each subcatchment, it creates a hash that contains the following variables: Subcatchment ID Land use ID Total area Contributed area Area measurement type Runoff area 1 to 12 (absolute values) Runoff area 1 to 12 (percentages)

4.  The subcatchment variables hash is appended to the array.

5.  After processing all the subcatchments, the code prints the column labels for the subcatchment variables. It retrieves the keys from the first hash in . For each key, it modifies the label as follows: If the index is less than 1: It removes 'Runoff ' and 'absolute' from the key. It replaces 'Area' with 'A'. It pads the label with spaces on the right to a total width of 20 characters. Otherwise, it truncates the key to a maximum of 8 characters and pads the label with spaces on the right to a total width of 8 characters. The modified labels are joined together with commas and printed.

6.  Finally, the code iterates over each set of variables in the array and prints them as a row in the output. For each value in the variables hash: If the index is less than 1, it truncates the value to a maximum of 20 characters and pads it with spaces on the right to a total width of 20 characters. Otherwise, it truncates the value to a maximum of 8 characters and pads it with spaces on the right to a total width of 8 characters. The modified values are joined together with commas and printed as a row.

The output will display the subcatchment variables, with the first column (Subcatchment ID) having a width of 20 characters and the remaining columns (runoff areas, total area, contributed area, etc.) having a width of 8 characters each. The column labels are modified to remove 'Runoff ' and 'absolute' from the first column label, replace 'Area' with 'A', and all labels are truncated and padded to fit within the specified widths.

![](https://media.licdn.com/dms/image/v2/D4E12AQH9zi3jn35Igw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714258666282?e=1795651200&v=beta&t=-ynTJFj3xZYVslYVMkhuOHefHvjlW5ZHNXzJGfqO3ek)

Ruby for Subcatchment Grid Area or Area Percentage

> **4/ Ruby for Runoff Surfaces in ICM InfoWorks**

**The code initializes an array called** **to store information about runoff surfaces in ICM InfoWorks. It then loops through each runoff surface in the network using the** **method and adds a hash of variables for each runoff surface to the** **array.**

**The variables stored for each runoff surface include:**

**1. Runoff surface ID**

**2. Description**

**3. Runoff routing type and value**

**4. Runoff volume type**

**5. Surface type**

**6. Ground slope**

**7. Initial loss type and value**

**8. Initial abstraction factor**

**9. Routing model**

**10. Fixed runoff coefficient**

**11. Minimum and maximum runoff**

**12. RAFTS adapt factor**

**13. Equivalent Manning's n**

**14. Wal. proc. distribution**

**15. New UK depth**

**16. SCS depth**

**17. Initial and limiting infiltration**

**18. Decay factor**

**19. Horton drying time and max infiltration volume**

**20. Recovery factor**

**21. Number of reservoirs**

**22. Depression Loss**

**23. Green-Ampt suction, conductivity, and deficit**

**24. Horner alpha, beta, and recovery**

**25. Initial loss porosity**

**26. Infiltration loss coefficient**

**27. Maximum deficit**

**28. Effective impermeability**

**29. Precipitation decay coefficient**

**30. Power coefficient for PI**

**31. Storage depth for paved and pervious surfaces**

**32. Wetness decay for NAPI**

**33. Power coefficient**

**34. Minimum NAPI**

**35. Saturated rainfall**

**After storing all the runoff surface variables, the code prints the column labels (keys of the first hash in** **) and then prints the values for each runoff surface as a row in the output. The labels and values are left-justified and padded with spaces to maintain consistent column widths.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHkA4AQTQQ69A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714222906773?e=1795651200&v=beta&t=94CcRgSuWgm7rEnP72ptcc5jJqGdftKacfql9dAVtqk)

Ruby Generated Runoff Surface Tables

> **5/ Ruby for Land Use in ICM InfoWorks**

The key variables in the given SQL query are:

1\. oid

2\. connectivity

3\. land_use_description

4\. land_use_id

5\. notes

6\. otype

7\. p_area_1 to p_area_12

8\. pollution_index

9\. population_density

10\. runoff_index_1 to runoff_index_12

11\. user_number_1 to user_number_10

12\. user_text_1 to user_text_10

13\. wastewater_profile

The query selects these variables directly without any aggregation or calculation

![](https://media.licdn.com/dms/image/v2/D4E12AQF6qlmkl331Qw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714096850267?e=1795651200&v=beta&t=tUUZI175vALwKZgg7q-eLiKgsU6KGFgJYA-XOEnMLog)

Ruby Output Table for Land Use

> **6/ How to use the Current and Background Networks for Subcatchment Statistics**

\[embedded item\]

> **7/ Past LinkedIn Article about the 12 Runoff Surfaces in ICM InfoWorks**

\[embedded item\]

> **8/ Why there are no Runoff Surfaces in ICM SWMM or SWMM5**

The runoff surface for ICM SWMM is on the Subcatchment Grid.

\[embedded item\]

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.

![](https://media.licdn.com/dms/image/v2/D4E12AQGfVEbCDvvd8w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714221866274?e=1795651200&v=beta&t=StbreL1YPiK6yaaCP1Bk4cqtBMEvRK5ptxQevxRK16A)
