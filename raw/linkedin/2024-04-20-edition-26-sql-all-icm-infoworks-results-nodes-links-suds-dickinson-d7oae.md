---
title: "Edition 26: SQL for ALL ICM InfoWorks Results for Nodes, Links and Subcatchments and SUDS, Runoff Surfaces and Land Use Input Parameters"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-26-sql-all-icm-infoworks-results-nodes-links-suds-dickinson-d7oae
created: "2024-03-23 21:10"
published: "2024-04-20 15:35"
words: 1767
export_sha256: f7a88c6b5ff3e3d5fb16d232bc8de604c06bd7bed195620f158f34f1e5d9d38e
---
# Edition 26: SQL for ALL ICM InfoWorks Results for Nodes, Links and Subcatchments and SUDS, Runoff Surfaces and Land Use Input Parameters

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 26: SQL for ALL ICM InfoWorks Results for Nodes, Links and Subcatchments and SUDS, Runoff Surfaces and Land Use Input Parameters](https://media.licdn.com/mediaD4E12AQHqgE92M1pnpw "Edition 26: SQL for ALL ICM InfoWorks Results for Nodes, Links and Subcatchments and SUDS, Runoff Surfaces and Land Use Input Parameters")

**Edition 26:** Comprehensive SQL Guide for ICM InfoWorks—Insights on Nodes, Links, Subcatchments, SUDS, Runoff Surfaces, and Land Use Parameters

In the 26th edition of our newsletter, we present an extensive exploration across seven SQL sections dedicated to harnessing the full potential of data from **ICM InfoWorks** and ICM SWMM. We want to empower users to effectively view all relevant data through SQL grids and to skillfully merge these grids into a unified comprehensive grid. This approach not only facilitates a clearer understanding but also enhances the management of large-scale models, providing a solid foundation for advanced data analysis and optimization in water management systems.

1.  SQL for Links using TSR:This section focuses on the SQL variables for links in an ICM InfoWorks network.Key variables include oid, us_depth, us_flow, us_froude, us_vel, ds_depth, ds_flow, ds_froude, and ds_vel.An SQL Run Dialog for Links and a Generated SQL Table are provided.

2.  SQL for Nodes using TSR:This section covers the key variables in the SQL query for nodes.Variables include depth, flooding, flow_volume_difference, head, head_class, invert_elevation, lateral_inflow, and more.The query calculates maximum, average, and minimum values for each variable, grouped by oid.An SQL Run Dialog for Nodes and a Grid Window for Nodes are shown.

3.  SQL for Subcatchments using TSR: This section focuses on the key variables in the SQL query for subcatchments.Variables include effrain, evapprof, EVAPRATE, max_EVAPRATE, lid_drain, various max_qsurf variables, and more.The query calculates maximum, average, and minimum values for each variable, grouped by oid.An SQL Run Dialog for Subcatchments and a Generated SQL Table for Subcatchments are provided.

4.  SQL for 1D Results Points using TSR: This section covers the SQL query for 1D Result Points.An SQL Run Dialog for 1D Result Points and a Grid Window for 1D Results Points are shown.The SQL query is provided, which calculates maximum, average, and minimum values for various variables, grouped by oid.

5.  SQL for SUDS Usage and Control ID: This section focuses on the key variables in the SQL query for SUDS Controls.Variables include controL_id, drainagemat_thickness, pave_clogging_factor, soil_conductivity, storage_void_ratio, and more.The query calculates maximum, average, and minimum values for each variable, grouped by oid.An SQL Run Dialog for SUDS Controls along with the Grid SQL Output is provided.

6.  SQL for Runoff Surfaces in ICM InfoWorks: This section covers the key variables in the SQL query for Runoff Surfaces.Variables include average_capillary_suction, decay_factor, depression_loss, effective_impermeability, ground_slope, and more.The query calculates the maximum value for each variable, grouped by oid.An SQL Run Dialog for SUDS Controls along with the Grid SQL Output is shown.

7.  SQL for Land Use in ICM InfoWorks: This section is the bridge between the Subcatchment Grid and the Runoff Surfaces of an ICM InfoWorks Network.

> **1/ SQL for Links using TSR**

These are the SQL link variables for an ICM InfoWorks network. Some of the key SQL link variables include:

1.  oid - The unique object ID of the link.

2.  us_depth - The upstream depth of flow in the link.

3.  us_flow - The upstream flow rate through the link.

4.  us_froude - The upstream Froude number for the link.

5.  us_vel - The upstream flow velocity in the link.

6.  ds_depth - The downstream depth of flow in the link.

7.  ds_flow - The downstream flow rate through the link.

8.  ds_froude - The downstream Froude number for the link.

9.  ds_vel - The downstream flow velocity in the link.

![](https://media.licdn.com/dms/image/v2/D4E12AQFPAk2UTDq-vA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713387062393?e=1795651200&v=beta&t=fbZmkCiZ0Pe0j9RXC0Xod7hEUxXOyAsApNkFZH4nQjY)

SQL Run Dialog for Links

![](https://media.licdn.com/dms/image/v2/D4E12AQEspVz3FiWicw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713386850310?e=1795651200&v=beta&t=iW_tmFUvaOtFowBBWkNVbszQvbKmuoropP9UbRXsMhA)

Generated SQL Table

> **2/ SQL for Nodes using TSR**

The key variables in the given SQL query are:

1\. depth

2\. flooding

3\. flow_volume_difference

4\. head

5\. head_class

6\. invert_elevation

7\. lateral_inflow

8\. max_depth

9\. max_head

10\. max_total_inflow

11\. pressure

12\. timesteps

13\. total_flood_time

14\. total_flood_volume

15\. total_inflow

16\. total_inflow_volume

17\. volume

For each of these variables, the query calculates the maximum (MAX), average (AVG), and minimum (MIN) values for each unique "oid" (object ID). The results are ordered by "oid".

![](https://media.licdn.com/dms/image/v2/D4E12AQHWTfNB77FgQQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713488080556?e=1795651200&v=beta&t=i-HzmO34K23I_Z7S_lBAvyp2iNITRL0nXgLsINXKnz8)

SQL Run Dialog for Nodes

![](https://media.licdn.com/dms/image/v2/D4E12AQE6goBdtndhxg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713530647964?e=1795651200&v=beta&t=3C6XT1Rt2qL2KWdbRmhTOhqONYjapJRjYBciXLlxPrs)

Generated SQL Table

> **3/ SQL for Subcatchments using TSR**

The key variables in the given SQL query are:

1\. effrain

2\. evapprof

3\. EVAPRATE

4\. max_EVAPRATE

5\. lid_drain

6\. max_q_lid_in

7\. max_q_lid_out

8\. max_qcatch

9\. max_qfoul

10\. max_qinfsoil

11\. max_qsurf01 to max_qsurf12

12\. max_qtrade

13\. max_RAINFALL

14\. max_runoff

15\. q_lid_drain

16\. q_lid_in

17\. q_lid_out

18\. qbase

19\. qcatch

20\. qfoul

21\. qinfsoil

22\. qsurf01 to qsurf12

23\. qtrade

24\. RAINFALL

25\. rainprof

26\. runoff

27\. sim_end

28\. sim_start

29\. timestep_duration

30\. timestep_no

31\. timestep_start

For each of these variables, the query calculates the maximum (MAX), average (AVG), and minimum (MIN) values for each unique "oid" (object ID). The results are ordered by "oid".

![](https://media.licdn.com/dms/image/v2/D4E12AQF9FOHk95k7Lg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713564576859?e=1795651200&v=beta&t=WLTRa2FyG3F3YCeZ72kVhy039sePV_9OCJTAsyjoABY)

SQL Run Dialog for Subcatchments

![](https://media.licdn.com/dms/image/v2/D4E12AQFH-Ok5IUiD7Q/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1713565258178?e=1795651200&v=beta&t=v73Wh2_9YFDzUi2bxrIAmYVWuyZNsNREHXyNp1pFmJU)

Generated SQL Table for Subcatchments

> 4/ SQL for 1D Results Points using TSR

![](https://media.licdn.com/dms/image/v2/D4E12AQFeRsCXKkUVOA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713545031283?e=1795651200&v=beta&t=iMxpwcUtUm3MUa_IFMwcNkKGC_YaOWz4XTIBlFSs76g)

SQL Run Dialog for 1D Result Points

![](https://media.licdn.com/dms/image/v2/D4E12AQGlvdgWGt0vHw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713552858798?e=1795651200&v=beta&t=ErdL16hXSI3XxGVDkzzTunkDh4fIZED_DwEWZM5ccsE)

The Grid Window for 1D Results Points

![](https://media.licdn.com/dms/image/v2/D4E12AQGgj5QZb2CLTA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713552979227?e=1795651200&v=beta&t=E9SgF2j2164OPVfCjZrCAL_RVa8ByRhFTap6jlcPgQs)

> **5/ SQL for SUDS Usage and Control ID**

The key variables in the given SQL query are:

1\. controL_id

2\. drainagemat_thickness

3\. drainagemat_void_fraction

4\. pave_clogging_factor

5\. pave_impervious_surf_fraction

6\. pave_permeability

7\. pave_regen_fraction

8\. pave_regen_interval

9\. pave_thickness

10\. pave_void_ratio

11\. soil_class

12\. soil_conductivity

13\. soil_conductivity_slope

14\. soil_field_capacity

15\. soil_porosity

16\. soil_suction_head

17\. soil_thickness

18\. soil_wilting_point

19\. storage_barrel_height

20\. storage_clogging_factor

21\. storage_seepage_rate

22\. storage_thickness

23\. storage_void_ratio

24\. surf_berm_height

25\. surf_roughness_n

26\. surf_slope

27\. surf_storage_depth

28\. surf_veg_vol_fraction

29\. surf_xslope

30\. underdrain_delay

31\. underdrain_flow_capacity

32\. underdrain_flow_coefficient

33\. underdrain_flow_exponent

34\. underdrain_offset_height

35\. user_number_1 to user_number_10

For each of these variables, the query calculates the maximum (MAX), average (AVG), and minimum (MIN) values for each unique "oid" (object ID). The results are ordered by "oid".

![](https://media.licdn.com/dms/image/v2/D4E12AQHcgzyUpx40hg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713612967476?e=1795651200&v=beta&t=XxFI8bscDpqiOnbCljJRxlEsu01Z5Rkavxn05iizFVA)

SQL Run Dialog for SUDS Controls along with the GrId SQL Output

> **6/ SQL for Runoff Surfaces in ICM InfoWorks**

**The key variables in the given SQL query are:**

**1. average_capillary_suction**

**2. decay_factor**

**3. depression_loss**

**4. drying_time**

**5. effective_impermeability**

**6. equivalent_roughness**

**7. ground_slope**

**8. halpha**

**9. hbeta**

**10. hrecovery**

**11. infiltration_coeff**

**12. initial_abstraction_factor**

**13. initial_infiltration**

**14. initial_loss_porosity**

**15. initial_loss_type**

**16. initial_loss_value**

**17. initial_moisture_deficit**

**18. limiting_infiltration**

**19. max_infiltration_volume**

**20. maximum_deficit**

**21. maximum_runoff**

**22. minimum_napi**

**23. minimum_runoff**

**24. moisture_depth_parameter**

**25. napi_decay_coeff**

**26. notes**

**27. number_of_reservoirs**

**28. oid**

**29. otype**

**30. power_coeff_paved**

**31. power_coeff_pervious**

**32. precipitation_decay**

**33. rafts_adapt_factor**

**34. rafts_user_b**

**35. recovery_factor**

**36. routing_model**

**37. runoff_coefficient**

**38. runoff_distribution_factor**

**39. runoff_index**

**40. runoff_routing_type**

**41. runoff_routing_value**

**42. runoff_volume_type**

**43. saturated_hydraulic_conductivity**

**44. saturated_rainfall**

**45. storage_depth**

**46. storage_depth_paved**

**47. storage_depth_pervious**

**48. surface_description**

**49. surface_type**

**50. user_number_1 to user_number_10**

**The query calculates the maximum (MAX) value for each of these variables, grouped by the "OID" column. The results are ordered by "OID".**

![](https://media.licdn.com/dms/image/v2/D4E12AQEEZ5SEdIqY8Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713617123362?e=1795651200&v=beta&t=SUSgHrdM5l8_986yOf_rxNGxzHNunsko9Yb4VPwJBkA)

SQL Run Dialog for SUDS Controls along with the GrId SQL Output

> 7/ SQL for Land Use in ICM InfoWorks

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

The query selects these variables directly without any aggregation or calculation.

![](https://media.licdn.com/dms/image/v2/D4E12AQGmFxg2I21yFg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713624600096?e=1795651200&v=beta&t=eZL9tC0pjNZsFD4QX_nRqhvc0ynCcxc6M15oJOuxlz0)

SQL Run Dialog for SUDS Controls along with the GrId SQL Output

![](https://media.licdn.com/dms/image/v2/D4E12AQGA8scbCgMItg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713571906599?e=1795651200&v=beta&t=l7TGvF-6TcW_jdhnQsTLOpcdE7fDHTlbL0Cs1Lh_ZfI)

**SQL Chicken Crossing the Coding Creek**

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
