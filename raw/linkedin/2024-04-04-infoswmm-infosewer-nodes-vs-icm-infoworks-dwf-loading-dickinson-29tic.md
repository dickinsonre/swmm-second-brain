---
title: "InfoSWMM and InfoSewer Nodes vs ICM InfoWorks Subcatchments for DWF Loading"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/infoswmm-infosewer-nodes-vs-icm-infoworks-dwf-loading-dickinson-29tic
created: "2024-03-28 02:47"
published: "2024-04-04 14:12"
words: 613
export_sha256: 496544c1a66ec1cf58e985c4c5a046aff601bf68f91b76a7cc2dcb3e369a2d64
---
# InfoSWMM and InfoSewer Nodes vs ICM InfoWorks Subcatchments for DWF Loading

![InfoSWMM and InfoSewer Nodes vs ICM InfoWorks Subcatchments for DWF Loading](https://media.licdn.com/mediaD5612AQEbCLwIinKGjw "InfoSWMM and InfoSewer Nodes vs ICM InfoWorks Subcatchments for DWF Loading")

When importing InfoSewer or InfoSWMM models into ICM InfoWorks, the dry weather flow loadings are assigned to nodes. **However**, in ICM InfoWorks, dry weather flow is loaded at subcatchments, not nodes. This discrepancy can lead to inaccurate modeling of dry weather flow in the imported ICM InfoWorks model if not corrected or acknowledged.

**Solution:** To address this issue, dummy subcatchments need to be created in ICM InfoWorks to accommodate the dry weather flow loadings from InfoSewer or InfoSWMM. Follow these steps to create dummy subcatchments:

1.  Open the ICM InfoWorks model that was imported from InfoSewer or InfoSWMM.

2.  Navigate to the "Subcatchments" table in the model database.

3.  Use the following SQL script to create new subcatchments based on the existing nodes:

&nbsp;

This script does the following:

- It inserts new records into the 'subcatchment' table.

- The 'subcatchment_id' and 'node_id' fields are populated with the 'node_id' from the 'node' table.

- The 'total_area' field is set to a default value of 0.10 for each new subcatchment.

- The 'x' and 'y' coordinates are taken from the corresponding fields in the 'node' table.

- The 'connectivity' field is set to 100 for each new subcatchment.

- The script filters the records from the 'node' table where the 'node_type' is 'Manhole'.

1.  Run the SQL script to create the dummy subcatchments.

2.  Review and validate the created subcatchments to ensure they are correctly associated with the corresponding nodes.

By making dummy subcatchments, the dry weather flow loadings from InfoSewer or InfoSWMM can be correctly assigned to subcatchments in ICM InfoWorks. This makes sure that the dry weather flow modeling in the imported model is correct.

Extra Comments:

- This solution assumes that the imported ICM InfoWorks model has a 'node' table with fields such as 'node_id', 'node_type', 'x', and 'y'.

- The 'total_area' field is set to a default value of 0.10 in this example. Adjust this value according to your specific modeling requirements.

- Ensure that the'subcatchment' table in the ICM InfoWorks model has the necessary fields ('subcatchment_id', 'node_id', 'total_area', 'x', 'y', 'connectivity') before running the SQL script.

> **More about Making any Shaped Dummy Subcatchment**

\[embedded item\]

![](https://media.licdn.com/dms/image/v2/D4E12AQHN5kDe8KQWmQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1712239072813?e=1795651200&v=beta&t=3aqam-kLXzDzFtdDapQrcGKhzeEIE0ryNZED4KbzE_A)

**Why 1729**

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
