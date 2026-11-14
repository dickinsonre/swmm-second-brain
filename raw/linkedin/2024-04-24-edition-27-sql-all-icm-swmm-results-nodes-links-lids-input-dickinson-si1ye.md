---
title: "Edition 27: SQL for ALL ICM SWMM Results for Nodes, Links and Subcatchments and LIDS Input and Results Parameters"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-27-sql-all-icm-swmm-results-nodes-links-lids-input-dickinson-si1ye
created: "2024-03-23 20:40"
published: "2024-04-24 16:33"
words: 2882
export_sha256: 624e7f9f600a9fc1617ff589895fc385a6692c6592bf182fa54a22e3f0d3a37e
---
# Edition 27: SQL for ALL ICM SWMM Results for Nodes, Links and Subcatchments and LIDS Input and Results Parameters

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 27: SQL for ALL ICM SWMM Results for Nodes, Links and Subcatchments and LIDS Input and Results Parameters](https://media.licdn.com/mediaD4E12AQGK7y1JF7sLCA "Edition 27: SQL for ALL ICM SWMM Results for Nodes, Links and Subcatchments and LIDS Input and Results Parameters")

In the 27th edition of our newsletter, we present an extensive exploration across seven SQL sections dedicated to harnessing the full potential of data from ICM SWMM. We want to empower users to effectively view all relevant data through SQL grids and to skillfully merge these grids into a unified, comprehensive grid. This approach not only facilitates a clearer understanding but also enhances the management of large-scale models, providing a solid foundation for advanced data analysis and optimization in water management systems.

Summary of the seven sections:

**1. ICM SWMM TSR Link Results**

This section provides a summary of the variables related to TSR (Time Series Results) for links in ICM SWMM. It covers variables such as depth, flow, capacity, velocity, losses, and various statistical measures like maximum, sum, minimum, and count for each variable.

2\. ICM SWMM TSR Node Results

This section summarizes the variables associated with TSR for nodes in ICM SWMM. It includes variables like depth, flooding, flow volume difference, head, invert elevation, lateral inflow, and total inflow. Statistical measures are provided for each variable.

3\. ICM SWMM TSR Subcatchment Results

The variables related to TSR for subcatchments in ICM SWMM are summarized in this section. It covers variables such as evaporation loss, runoff (impervious and pervious), infiltration loss, peak runoff, rainfall, runoff coefficient, and total runoff depth and volume. Statistical measures are included for each variable.

4\. ICM SWMM LID Controls

This section focuses on the variables associated with LID (Low Impact Development) controls in ICM SWMM. It includes variables related to various LID components like drainage mat, pavement, soil, storage, surface, and underdrain. Maximum, average, and minimum values are calculated for each variable.

5\. ICM SWMM Subcatchment Data

The variables related to subcatchment data in ICM SWMM are summarized in this section. It covers a wide range of variables, including aquifer properties, area, slope, curve number, groundwater parameters, infiltration, abstraction, roughness, and user-defined variables.

6\. ICM SWMM Node Data

This section provides a summary of the variables associated with node data in ICM SWMM. It includes variables such as base flow, patterns, conductivity, evaporation factor, flooding parameters, invert elevation, storage properties, and user-defined attributes.

7\. ICM SWMM Link Data

The variables related to link data in ICM SWMM are summarized in this section. It covers variables like surcharge, arch and ellipse sizes, headloss coefficients, Manning's roughness, conduit dimensions, discharge coefficients, invert elevations, shape-related variables, and user-defined attributes.

The edition provides a comprehensive guide to the variables and data used in ICM SWMM, helping users effectively model and analyze urban drainage systems. By understanding these variables and their significance, modelers can make informed decisions and optimize their ICM SWMM models for accurate and reliable results.

> **1/ ICM SWMM TSR Link Results**

Here is a summary of the variables for **ICM SWMM TSR Link Results**

1\. oid: Object ID

2\. depth: Depth of the conduit

\- max_depth, sum_depth, min_depth, count_depth

3\. flow: Flow in the conduit

\- max_flow, sum_flow, min_flow, count_flow

4\. capacity: Capacity of the conduit

\- max_capacity, sum_capacity, min_capacity, count_capacity

5\. velocity: Velocity in the conduit

\- max_velocity, sum_velocity, min_velocity, count_velocity

6\. entry_loss: Entry loss of the conduit

\- max_entry_loss, sum_entry_loss, min_entry_loss, count_entry_loss

7\. exit_loss: Exit loss of the conduit

\- max_exit_loss, sum_exit_loss, min_exit_loss, count_exit_loss

8\. flow_class: Flow class of the conduit

\- max_flowclass, sum_flowclass, min_flowclass, count_flowclass

9\. flow_volume: Flow volume in the conduit

\- max_flowvolume, sum_flowvolume, min_flowvolume, count_flowvolume

10\. hgl: Hydraulic grade line in the conduit

\- max_hgl, sum_hgl, min_hgl, count_hgl

11\. max_capacity: Maximum capacity of the conduit

\- max_max_capacity, sum_max_capacity, min_max_capacity, count_max_capacity

12\. max_flow: Maximum flow in the conduit

\- max_max_flow, sum_max_flow, min_max_flow, count_max_flow

13\. max_velocity: Maximum velocity in the conduit

\- max_max_velocity, sum_max_velocity, min_max_velocity, count_max_velocity

14\. sim_end: Simulation end time

\- max_sim_end, sum_sim_end, min_sim_end, count_sim_end

15\. sim_start: Simulation start time

\- max_sim_start, sum_sim_start, min_sim_start, count_sim_start

16\. surcharged: Surcharge status of the conduit

\- max_surcharged, sum_surcharged, min_surcharged, count_surcharged

17\. timestep_duration: Duration of each timestep

\- max_timestep_duration, sum_timestep_duration, min_timestep_duration, count_timestep_duration

18\. timestep_no: Timestep number

\- max_timestep_no, sum_timestep_no, min_timestep_no, count_timestep_no

19\. timestep_start: Start time of each timestep

\- max_timestep_start, sum_timestep_start, min_timestep_start, count_timestep_start

20\. timesteps: Number of timesteps

\- max_timesteps, sum_timesteps, min_timesteps, count_timesteps

For each variable, the SQL query calculates the maximum (\`MAX\`), sum (\`SUM\`), minimum (\`MIN\`), and count (\`COUNT\`) of the values from the tsr table.

![](https://media.licdn.com/dms/image/v2/D4E12AQG3V5UHnVBYIg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713738426829?e=1795651200&v=beta&t=5JHQbh2Vop_1WRWKjdYKp6eISL9oeGHQK-kqSHfpX4I)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQFWCeNDiU6taQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713738507274?e=1795651200&v=beta&t=InVrvfBTKrSiSOwYXmoFtSlpvrnnN5_uG98a1Cfjw_0)

SQL Generated Table for ICM SWMM using SQL Code

> **2/ ICM SWMM TSR Node Results**

Here is a summary of the variables for **ICM SWMM TSR Node Results**

1\. oid: Object ID

2\. depth: Depth at the node

\- max_depth, sum_depth, min_depth, count_depth

3\. flooding: Flooding at the node

\- max_flooding, sum_flooding, min_flooding, count_flooding

4\. flow_volume_difference: Flow volume difference at the node

\- max_flow_volume_difference, sum_flow_volume_difference, min_flow_volume_difference, count_flow_volume_difference

5\. head: Head at the node

\- max_head, sum_head, min_head, count_head

6\. head_class: Head class at the node

\- max_head_class, sum_head_class, min_head_class, count_head_class

7\. invert_elevation: Invert elevation of the node

\- max_invert_elevation, sum_invert_elevation, min_invert_elevation, count_invert_elevation

8\. lateral_inflow: Lateral inflow at the node

\- max_lateral_inflow, sum_lateral_inflow, min_lateral_inflow, count_lateral_inflow

9\. max_depth: Maximum depth at the node

\- max_max_depth, sum_max_depth, min_max_depth, count_max_depth

10\. max_total_inflow: Maximum total inflow at the node

\- max_max_total_inflow, sum_max_total_inflow, min_max_total_inflow, count_max_total_inflow

11\. pressure: Pressure at the node

\- max_pressure, sum_pressure, min_pressure, count_pressure

12\. sim_end: Simulation end time

\- max_sim_end, sum_sim_end, min_sim_end, count_sim_end

13\. sim_start: Simulation start time

\- max_sim_start, sum_sim_start, min_sim_start, count_sim_start

14\. timestep_duration: Duration of each timestep

\- max_timestep_duration, sum_timestep_duration, min_timestep_duration, count_timestep_duration

15\. timestep_no: Timestep number

\- max_timestep_no, sum_timestep_no, min_timestep_no, count_timestep_no

16\. timestep_start: Start time of each timestep

\- max_timestep_start, sum_timestep_start, min_timestep_start, count_timestep_start

17\. timesteps: Number of timesteps

\- max_timesteps, sum_timesteps, min_timesteps, count_timesteps

18\. total_flood_time: Total flood time at the node

\- max_total_flood_time, sum_total_flood_time, min_total_flood_time, count_total_flood_time

19\. total_flood_volume: Total flood volume at the node

\- max_total_flood_volume, sum_total_flood_volume, min_total_flood_volume, count_total_flood_volume

20\. total_inflow: Total inflow at the node

\- max_total_inflow, sum_total_inflow, min_total_inflow, count_total_inflow

21\. total_inflow_volume: Total inflow volume at the node

\- max_total_inflow_volume, sum_total_inflow_volume, min_total_inflow_volume, count_total_inflow_volume

22\. volume: Volume at the node

\- max_volume, sum_volume, min_volume, count_volume

For each variable, the SQL query calculates the maximum (\`MAX\`), sum (\`SUM\`), minimum (\`MIN\`), and count (\`COUNT\`) of the values from the tsr table.

![](https://media.licdn.com/dms/image/v2/D5612AQHi5StlkAQFmA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713829274884?e=1795651200&v=beta&t=sSOjaJy1-Sn1tcgXl18qXEEjdZy-EsKHRJ4nN12sX68)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D5612AQE6eL0lHn2j5A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713829322672?e=1795651200&v=beta&t=RywS1DQAFS61FZBIIy0RuamtbwgCDCdG9ZLvAZUjG8k)

SQL Generated Table for ICM SWMM using SQL Code

> **3/ ICM SWMM TSR Subcatchment Results**

Here is a summary of the variables in the provided SQL code **ICM SWMM TSR Subcatchment Results:**

1\. oid: Object ID

2\. evaporation_loss: Evaporation loss from the subcatchment

\- max_evaporation_loss, sum_evaporation_loss, min_evaporation_loss, count_evaporation_loss

3\. imperv_runoff: Runoff from the impervious area of the subcatchment

\- max_imperv_runoff, sum_imperv_runoff, min_imperv_runoff, count_imperv_runoff

4\. infiltration_loss: Infiltration loss from the subcatchment

\- max_infiltration_loss, sum_infiltration_loss, min_infiltration_loss, count_infiltration_loss

5\. peak_runoff: Peak runoff from the subcatchment

\- max_peak_runoff, sum_peak_runoff, min_peak_runoff, count_peak_runoff

6\. peak_runoff_time: Time of peak runoff from the subcatchment

\- max_peak_runoff_time, sum_peak_runoff_time, min_peak_runoff_time, count_peak_runoff_time

7\. perv_runoff: Runoff from the pervious area of the subcatchment

\- max_perv_runoff, sum_perv_runoff, min_perv_runoff, count_perv_runoff

8\. rainfall: Rainfall on the subcatchment

\- max_rainfall, sum_rainfall, min_rainfall, count_rainfall

9\. runoff: Total runoff from the subcatchment

\- max_runoff, sum_runoff, min_runoff, count_runoff

10\. runoff_coefficient: Runoff coefficient of the subcatchment

\- max_runoff_coefficient, sum_runoff_coefficient, min_runoff_coefficient, count_runoff_coefficient

11\. sim_end: Simulation end time

\- max_sim_end, sum_sim_end, min_sim_end, count_sim_end

12\. sim_start: Simulation start time

\- max_sim_start, sum_sim_start, min_sim_start, count_sim_start

13\. snow_depth: Snow depth on the subcatchment

\- max_snow_depth, sum_snow_depth, min_snow_depth, count_snow_depth

14\. timestep_duration: Duration of each timestep

\- max_timestep_duration, sum_timestep_duration, min_timestep_duration, count_timestep_duration

15\. timestep_no: Timestep number

\- max_timestep_no, sum_timestep_no, min_timestep_no, count_timestep_no

16\. timestep_start: Start time of each timestep

\- max_timestep_start, sum_timestep_start, min_timestep_start, count_timestep_start

17\. timesteps: Number of timesteps

\- max_timesteps, sum_timesteps, min_timesteps, count_timesteps

18\. total_evaporation: Total evaporation from the subcatchment

\- max_total_evaporation, sum_total_evaporation, min_total_evaporation, count_total_evaporation

19\. total_infiltration: Total infiltration from the subcatchment

\- max_total_infiltration, sum_total_infiltration, min_total_infiltration, count_total_infiltration

20\. total_precipitation: Total precipitation on the subcatchment

\- max_total_precipitation, sum_total_precipitation, min_total_precipitation, count_total_precipitation

21\. total_runoff_depth: Total runoff depth from the subcatchment

\- max_total_runoff_depth, sum_total_runoff_depth, min_total_runoff_depth, count_total_runoff_depth

22\. total_runoff_volume: Total runoff volume from the subcatchment

\- max_total_runoff_volume, sum_total_runoff_volume, min_total_runoff_volume, count_total_runoff_volume

23\. total_runon: Total runon to the subcatchment

\- max_total_runon, sum_total_runon, min_total_runon, count_total_runon

For each variable, the SQL query calculates the maximum (\`MAX\`), sum (\`SUM\`), minimum (\`MIN\`), and count (\`COUNT\`) of the values from the tsr table.

![](https://media.licdn.com/dms/image/v2/D4E12AQHTiE5EL9j1kQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713836872001?e=1795651200&v=beta&t=X_BigTkqPoVRBnDnydDLmE5b2ziB-8TvAnFv9l-HBmQ)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQEP9iGRJ4JnIA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713836949538?e=1795651200&v=beta&t=HYuBhfVu6bVlvVr3rXqIgkLcLAIfMFsiWaa0EGvnNbQ)

SQL Generated Table for ICM SWMM using SQL Code

> **4/ ICM SWMM LID Controls**

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

![](https://media.licdn.com/dms/image/v2/D4E12AQHgT2SuEosLWQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713837476634?e=1795651200&v=beta&t=NSpmCTbuFBLc5fw7WGWvDX2enocDbNqDKogjzl2F3nU)

SQL Run Dialog for ICM SWMM

> **5/ ICM SWMM Subcatchment Data**

Here's a summary of the variables in the provided SQL code for **ICM SWMM Subcatchment Data**

1\. : Object ID

2\. : Elevation of the aquifer

3\. : Aquifer ID

4\. : Initial groundwater level in the aquifer

5\. : Initial moisture content in the aquifer

6\. : Node ID associated with the aquifer

7\. : Subcatchment area

8\. : Area-averaged rainfall

9\. : Average capillary suction

10\. : Slope of the subcatchment

11\. : Length of the curb

12\. : Curve number

13\. : Decay factor

14\. : Deep groundwater flow equation

15\. : Drying time

16\. : Depression storage pattern

17\. : Subcatchment elevation

18\. , , : Groundwater-related parameters

19\. : Hydraulic length

20\. : Infiltration pattern

21\. : Infiltration rate

22\. , , : Initial abstraction parameters

23\. : Initial infiltration rate

24\. : Initial moisture deficit

25\. : Lateral groundwater flow equation

26\. : Limiting infiltration rate

27\. : Maximum infiltration volume

28\. : Pervious area roughness pattern

29\. : Notes

30\. : Object type

31\. : Outlet ID

32\. , , : Percentage parameters

33\. : Rain gauge ID

34\. , : Roughness parameters

35\. : Routing destination

36\. : Runoff model type

37\. : Saturated hydraulic conductivity

38\. : Shape factor

39\. : Snow pack ID

40\. , : Storage parameters

41\. : Subcatchment ID

42\. , , , : Surface-related parameters

43\. : Subcatchment drainage destination

44\. : Time of concentration

45\. to : User-defined number variables

46\. to : User-defined text variables

47\. : Subcatchment width

48\. , : Coordinates

These variables represent various properties and attributes of subcatchments in a hydrological model, including physical characteristics, infiltration parameters, groundwater settings, and user-defined variables.

![](https://media.licdn.com/dms/image/v2/D4E12AQHq2dt_e-hfuQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713972428541?e=1795651200&v=beta&t=-W-AveeISvmjKIUjOG2phBvEfr44ZgJi1Q-YAuAHMJA)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQHlFsPvSTBNkA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1713974195757?e=1795651200&v=beta&t=RKLZXu0-5oyqxg3XJSIP1uByTRu3QKMBNE7oAHRpdvw)

SQL Generated Table for ICM SWMM using SQL Code

> **6/ ICM SWMM Node Data**

Here's a summary of the ICM SWMM variables in the provided SQL SELECT statement:

1\. oid: Object ID, used to uniquely identify the object.

2\. base_flow: Base flow value associated with the object.

3\. bf_pattern_1 to bf_pattern_4: Base flow patterns 1 to 4.

4\. conductivity: Conductivity value associated with the object.

5\. evaporation_factor: Evaporation factor.

6\. fixed_stage: Fixed stage value.

7\. flap_gate: Flap gate indicator.

8\. flood_type: Type of flooding associated with the object.

9\. flooding_discharge_coeff: Flooding discharge coefficient.

10\. functional_coefficient, functional_constant, functional_exponent: Functional parameters.

11\. ground_level: Ground level elevation.

12\. inflow_baseline, inflow_pattern, inflow_scaling: Inflow-related parameters.

13\. initial_depth: Initial depth value.

14\. initial_moisture_deficit: Initial moisture deficit.

15\. invert_elevation: Invert elevation.

16\. maximum_depth: Maximum depth value.

17\. node_id: Node ID.

18\. node_type: Type of node.

19\. notes: Additional notes or comments.

20\. otype: Object type.

21\. outfall_type: Type of outfall.

22\. ponded_area: Ponded area value.

23\. route_subcatchment: Subcatchment routing information.

24\. storage_curve: Storage curve ID.

25\. storage_type: Type of storage.

26\. suction_head: Suction head value.

27\. surcharge_depth: Surcharge depth value.

28\. tidal_curve_id: Tidal curve ID.

29\. unit_hydrograph_area: Unit hydrograph area.

30\. unit_hydrograph_id: Unit hydrograph ID.

31\. user_number_1 to user_number_10: User-defined numeric attributes.

32\. user_text_1 to user_text_10: User-defined text attributes.

33\. X, y: Spatial coordinates.

These variables cover a wide range of attributes related to the object, including hydraulic properties, inflow characteristics, initial conditions, user-defined attributes, and spatial information.

![](https://media.licdn.com/dms/image/v2/D4E12AQHRq7D_OxVIKA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713959752475?e=1795651200&v=beta&t=fnTCxJEIpZ5Hv6n71hqCLOV-vNzt-l3GD2aX7RsJExM)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQGk5Ozs3_zwKg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713959805524?e=1795651200&v=beta&t=nC2n5aSeDi1VQb5coSnzQQ5rkpvW_euC7q1DOzxV2c8)

SQL Generated Table for ICM SWMM using SQL Code

> **7/ ICM SWMM Link Data**

Here's a summary of the variables in the provided SQL code for **ICM SWMM Link Data**

1\. oid: Object ID

2\. allows_surcharge: Allows surcharge flag

3\. arch_concrete_size_code, arch_plate_18_size_code, arch_plate_31_size_code, arch_steel_half_size_code, arch_steel_inch_size_code, horiz_ellipse_size_code, vert_ellipse_size_code: Size codes for different arch and ellipse shapes

4\. arch_material: Arch material

5\. av_headloss_coeff, ds_headloss_coeff, us_headloss_coeff: Headloss coefficients

6\. bottom_mannings_N, Mannings_N: Manning's roughness coefficient

7\. bottom_radius, top_radius: Bottom and top radius

8\. branch_id: Branch ID

9\. conduit_height, conduit_width: Conduit dimensions

10\. crest: Crest level

11\. culvert_code: Culvert code

12\. discharge_coeff, discharge_coefficient, secondary_discharge_coeff, sideflow_discharge_coeff, var_dis_coeff: Discharge coefficients

13\. discharge_exponent: Discharge exponent

14\. ds_invert, us_invert, invert: Downstream, upstream, and invert elevations

15\. ds_node_id, us_node_id: Downstream and upstream node IDs

16\. end_contractions: End contractions

17\. flap_gate: Flap gate flag

18\. head_discharge_id: Head discharge ID

19\. id: Link ID

20\. ideal: Ideal flag

21\. initial_flow, initial_status: Initial flow and status

22\. left_2d_zone_id, right_2d_zone_id: Left and right 2D zone IDs

23\. left_node_id, right_node_id: Left and right node IDs

24\. left_reach_node_id, right_reach_node_id: Left and right reach node IDs

25\. left_slope, right_slope: Left and right slopes

26\. length: Link length

27\. link_suffix, link_type: Link suffix and type

28\. notes: Notes

29\. number_of_barrels: Number of barrels

30\. orifice_height, orifice_width: Orifice dimensions

31\. otype: Object type

32\. pump_curve: Pump curve ID

33\. rating_curve_type: Rating curve type

34\. roughness_depth_threshold: Roughness depth threshold

35\. roughness_DW, roughness_HW: Roughness values

36\. sediment_depth: Sediment depth

37\. seepage_rate: Seepage rate

38\. shape, shape_curve, shape_exponent: Shape-related variables

39\. shut_off_depth: Shut-off depth

40\. start_level, start_up_depth: Start level and depth

41\. surface: Surface type

42\. time_to_open: Time to open

43\. transect: Transect ID

44\. triangle_height: Triangle height

45\. user_number_1 to user_number_10: User-defined number variables

46\. user_text_1 to user_text_10: User-defined text variables

47\. weir_curve, weir_height, weir_width: Weir-related variables

48\. width: Link width

These variables cover a wide range of properties and attributes related to hydraulic links ICM SWMM.

![](https://media.licdn.com/dms/image/v2/D4E12AQFSxbdkL-WYvg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713969007198?e=1795651200&v=beta&t=1GJPYJ2iaukz0QUOBQ6BWrlCww_WNJx5uFN6NBKqLV8)

SQL Run Dialog for ICM SWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQGJp7QCmPDaXA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1713969038068?e=1795651200&v=beta&t=7lgqG9eA7u9-WBN_-XDOXHPxPL7KyN0tC5AiffwRO4I)

SQL Generated Table for ICM SWMM using SQL Code

![](https://media.licdn.com/dms/image/v2/D4E12AQE_o5o3PMgxRA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1713736049021?e=1795651200&v=beta&t=Ynt350umDO_56R-GOv9-wVryyClgEJV0DN--4TXsY_M)

An AI CoPilot Designed GI House

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
