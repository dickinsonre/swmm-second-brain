---
title: "Why ICM is a 1D–2D Integrated Catchment Model, Counting Tables—with Ruby (of course)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/why-icm-1d2d-integrated-catchment-model-counting-ruby-dickinson-ypixe
created: "2024-02-19 11:41"
published: "2024-02-19 14:08"
words: 722
export_sha256: aa6d98303c1868c90602acab9d0f1299ea7f35bfcb7a612c703cf2a3106dccb1
---
# Why ICM is a 1D–2D Integrated Catchment Model, Counting Tables—with Ruby (of course)

![Why ICM is a 1D–2D Integrated Catchment Model, Counting Tables](https://media.licdn.com/mediaD4E12AQF5JaEZ4dd16A "Why ICM is a 1D–2D Integrated Catchment Model, Counting Tables")

Autodesk Water Infrastructure InfoWorks ICM Key Concepts **(adapted from the Online Help file for ICM with Stats added by Ruby—code at the bottom of this article)**

Autodesk Water Infrastructure's InfoWorks ICM stands at the forefront of integrated catchment and basin modeling technology, inheriting its foundation from the globally recognized InfoWorks product suite. This state-of-the-art system is designed for comprehensive, user-friendly, and flexible management of fully integrated catchment models. It enables modeling of the entire drainage network, both natural and engineered, encompassing sewers, surface waters, rivers, and floodplains, above and below ground.

Key Features:

- A robust database for storing model and hydraulic data, complemented by a suite of tools for data creation, editing, and management. **There are 91 ICM tables and 46 ICM SWMM tables. There are 696 SWMM and 2163 InfoWorks parameters, in the tables, respectively.**

- Advanced simulation capabilities to model catchment behavior under various conditions, facilitating long-term management and maintenance of network models beyond specific projects. **InfoWorks 91 Tables** *hw_sim_parameters, hw_manhole_defaults, hw_conduit_defaults, hw_subcatchment_defaults, hw_large_catchment_parameters, hw_snow_parameters, hw_wq_params, hw_node, hw_conduit, hw_flap_valve, hw_orifice, hw_pump, hw_sluice, hw_user_control, hw_weir, hw_flume, hw_siphon, hw_screen, hw_channel, hw_channel_defaults, hw_river_reach_defaults, hw_culvert_inlet, hw_culvert_outlet, hw_blockage, hw_bridge_blockage, hw_shape, hw_head_discharge, hw_runoff_surface, hw_land_use, hw_snow_pack, hw_headloss, hw_ground_infiltration, hw_subcatchment, hw_polygon, hw_unit_hydrograph, hw_unit_hydrograph_month, hw_channel_shape, hw_general_line, hw_porous_wall, hw_2d_zone, hw_mesh_zone, hw_roughness_zone, hw_2d_ic_polygon, hw_2d_point_source, hw_2d_boundary_line, hw_irregular_weir, hw_river_reach, hw_porous_polygon, hw_cross_section_survey, hw_flow_efficiency, hw_bank_survey, hw_bridge, hw_bridge_inlet, hw_bridge_opening, hw_bridge_outlet, hw_storage_area, hw_2d_zone_defaults, hw_rtc, hw_2d_infil_surface, hw_2d_infiltration_zone, hw_2d_wq_ic_polygon, hw_2d_inf_ic_polygon, hw_inline_bank, hw_general_point, hw_2d_linear_structure, hw_2d_sluice, hw_tvd_connector, hw_2d_results_polygon, hw_2d_results_line, hw_2d_results_point, hw_1d_results_point, hw_2d_bridge, hw_spatial_rain_zone, hw_spatial_rain_source, hw_pdm_descriptor, hw_damage_receptor, hw_head_unit_discharge, hw_2d_sed_ic_polygon, hw_mesh_level_zone, hw_risk_impact_zone, hw_sediment_grading, hw_suds_control, hw_2d_line_source, hw_2d_turbulence_model, hw_2d_turbulence_zone, hw_2d_permeable_zone, hw_arma, hw_swmm_land_use, hw_roughness_definition, hw_building, hw_2d_connect_line*

- Collaborative model data sharing within workgroups, complete with audit trails and security features tailored for modeling tasks.

- Easy import of model data from external systems and the ability to view the network geographically, in both 2D and 3D, over detailed local maps. Customization options enhance network visualization.

- Integration of rainfall and other time-series or event data, supported by a vast library of synthetic rainfall models globally.

- Comprehensive hydraulic simulation tools for modeling linked event sequences and analyzing results through graphical, textual, and statistical outputs. **ICM SWMM 46 Tables,** *sw_options, sw_subcatchment, sw_node, sw_tvd_connector, sw_polygon, sw_raingage, sw_controls, sw_transect, sw_conduit, sw_weir, sw_orifice, sw_pump, sw_outlet, sw_spatial_rain_zone, sw_spatial_rain_source, sw_pollutant, sw_land_use, sw_uh_group, sw_uh, sw_curve_control, sw_curve_pump, sw_curve_rating, sw_curve_shape, sw_curve_tidal, sw_curve_storage, sw_aquifer, sw_suds_control, sw_snow_pack, sw_title, sw_snow_parameters, sw_curve_weir, sw_curve_underdrain, sw_soil, sw_2d_zone, sw_general_line, sw_mesh_zone, sw_porous_polygon, sw_roughness_zone, sw_mesh_level_zone, sw_porous_wall, sw_roughness_definition, sw_2d_boundary_line, sw_head_unit_discharge, sw_river_reach, sw_2d_ic_polygon*

**Innovations:**

- Scenario Manager: Streamlines the editing and comparison of multiple 'what if' scenarios, enhancing the examination of alternative modeling scenarios with efficient scenario analysis and simulation.

- Simulation Server: Offers flexible simulation execution on standalone workstations, within workgroups, enterprise systems, or cloud environments, with monitoring and control over simulation progress.

- Multi-core and GPU (Parallel) 2D Engine Utilization: Leverages multi-core processors and NVIDIA GPU technology for faster processing of 2D simulations, significantly improving speed and efficiency.

**User Interface Highlights:**

- Intuitive, easy-to-use interface with multi-user version control, supporting 64-bit Windows 10 and 11 operating systems.

- Comprehensive GIS platform support, including ArcGIS and MapXtreme, with enhanced visualization and editing tools like powerful themes, customizable labels, and in-line validation property editors.

- Advanced visualization features, include customizable long sections, 3D views of rivers, and group dockable windows for efficient workspace management.

- Seamless integration with Autodesk Water Infrastructure InfoAsset Manager for close coordination between on-premise databases and asset databases, eliminating the need for separate administration programs.

Autodesk Water Infrastructure's InfoWorks ICM embodies over four decades of modeling excellence and innovation, offering unparalleled features for environmental management and urban planning professionals. Its commitment to leveraging PC power and cloud technology continues to set new standards in catchment modeling.

> **ICM SWMM Parameters - 696**

> **ICM InfoWorks Parameters - 2163 Parameters, cannot list them all due to LinkedIn article length issues**

> **Simple Ruby code to find the tables of ICM InfoWorks and ICM SWMM Networks. Sans fields of user, notes, hyperlinks and flags.**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
