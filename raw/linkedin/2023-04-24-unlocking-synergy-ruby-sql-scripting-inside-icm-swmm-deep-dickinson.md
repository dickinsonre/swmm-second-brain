---
title: "Unlocking the Synergy of Ruby and SQL Scripting inside ICM: Streamlining InfoWorks and SWMM Network Management with a Deep Dive into Data Structures"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/unlocking-synergy-ruby-sql-scripting-inside-icm-swmm-deep-dickinson
created: "2023-04-12 07:09"
published: "2023-04-24 02:31"
words: 1624
export_sha256: bdbb9e61a28cc34fe70289bcdd8b7c7601839665771006b145443deb202a8204
---
# Unlocking the Synergy of Ruby and SQL Scripting inside ICM: Streamlining InfoWorks and SWMM Network Management with a Deep Dive into Data Structures

![](https://media.licdn.com/mediaD4E12AQFVv4ueCo6DeA)

The Storm Water Management Model (SWMM) and InfoWorks networks share a common user experience (UX); similar data structures, output files, UX tools, and Ruby and SQL scripting mean that both systems have been designed with a focus on user-friendliness and interoperability. This facilitates the learning curve and overall productivity for those working with either of the systems.

A common UX ensures users find familiar interfaces, menus, and functions when transitioning between the SWMM and InfoWorks networks. This reduces the learning curve for users experienced with one system and promotes efficiency when working with both systems.

Having similar data structures allows for seamless data exchange between the two networks, enabling users to transfer and utilize information without having to reformat or restructure the data, thus saving time and reducing errors.

Sharing output files ensures that results generated from either system are compatible and can be easily compared or combined for further analysis. This encourages collaboration between teams working on different networks and simplifies merging or consolidating findings.

Standard UX tools provide users with consistent tools and utilities for visualizing, analyzing, and manipulating data within both systems. This ensures that users proficient in one system can easily apply their skills and knowledge to the other, maximizing productivity and efficiency.

Finally, the compatibility of Ruby and SQL scripting between the SWMM and InfoWorks networks allows users to develop custom scripts, automate tasks, and perform advanced data analysis on either system without learning a new programming language or syntax. This streamlines the scripting process and encourages sharing scripts and tools between users of both networks.

In summary, the shared elements between SWMM and InfoWorks networks enable a more streamlined, efficient, and user-friendly experience for professionals working with either system, fostering collaboration and simplifying the overall workflow.

> Common Feature 1 - Table Names in InfoWorks

Tables organize ICM InfoWorks and ICM SWMM Networks. The tables are organized by common elements such as nodes, links, and 2D elements. Tables starting with the prefix hw for "HydroWorks" the grandfather program to ICM in 1990, mean that the table is for an InfoWorks network.

```
# Counts all of the tables in an ICM InfoWorks Network

begin
    # Accessing current network
    net = WSApplication.current_network
    raise "Error: current network not found" if net.nil?

    tables = [
        "hw_node",
        "hw_conduit",
        "hw_subcatchment",
        "hw_orifice",
        "hw_channel",
        "hw_river_reach",
        "hw_pump",
        "hw_screen",
        "hw_siphon",
        "hw_sluice",
        "hw_irregular_weir",
        "hw_user_control",
        "hw_weir",
        "hw_culvert_inlet",
        "hw_culvert_outlet",
        "hw_flap_valve",
        "hw_bridge",
        "hw_bridge_opening",
        "hw_bridge_blockage",
        "hw_bridge_inlet",
        "hw_bridge_outlet",
        "hw_flume",
        "hw_blockage",
        "hw_mesh_zone",
        "hw_mesh_level_zone",
        "hw_inline_bank",  
        "hw_roughness_zone",
        "hw_storage_area",    
        "hw_building",
        "hw_2d_boundary_line",
        "hw_2d_ic_polygon",
        "hw_2d_wq_ic_polygon",
        "hw_2d_inf_ic_polygon",
        "hw_2d_sed_ic_polygon",
        "hw_2d_infiltration_zone",
        "hw_2d_infil_surface",
        "hw_2d_turbulence_zone",
        "hw_2d_turbulence_model",
        "hw_2d_permeable_zone",
        "hw_2d_point_source",
        "hw_2d_zone",
        "hw_damage_receptor",
        "hw_General_line",
        "hw_General_point",
        "hw_polygon",
        "hw_risk_impact_zone",   
        "hw_porous_polygon",
        "hw_porous_wall",
        "hw_2d_linear_structure",
        "hw_2d_sluice",
        "hw_2d_bridge",
        "hw_2d_line_source",
        "hw_tvd_connector",
        "hw_spatial_rain_source",
        "hw_spatial_rain_zone",
        "hw_ground_infiltration",
        "hw_headloss",
        "hw_suds_control",
        "hw_head_discharge",
        "hw_pdm_descriptor",
        "hw_head_unit_discharge",
        "hw_flow_efficiency",
        "hw_land_use",
        "hw_swmm_land_use",
        "hw_channel_shape",
        "hw_runoff_surface",
        "hw_shape",
        "hw_sediment_grading",
        "hw_sim_parameters",
        "hw_snow_pack",
        "hw_unit_hydrograph",
        "hw_unit_hydrograph_month",
        "hw_wq_params",
        "hw_conduit_defaults",
        "hw_manhole_defaults",
        "hw_channel_defaults",
        "hw_river_reach_defaults",
        "hw_subcatchment_defaults",
        "hw_large_catchment_parameters",
        "hw_2d_zone_defaults",
        "hw_snow_parameters",
        "hw_cross_section_survey",
        "hw_bank_survey",
        "hw_prunes",
        "hw_arma",
        "hw_roughness_definition"
  ]
```

> Common Feature 2 - Table Names in SWMM Networks

Tables organize ICM InfoWorks and ICM SWMM Networks. The tables are organized by common elements such as nodes, links, and 2D elements. Tables starting with the prefix sw for "SWMM" mean that the table is for an SWMM network. InfoWorks networks have more tables, as an InfoWorks network has more features than an SWMM network. However, for the context of this blog, the tables are used in the same manner,

```
  # Counts all of the tables in an ICM SWMM Network
     table_names = 
        "sw_conduit",
        "sw_node",
        "sw_uh",
        "sw_uh_group",
        "sw_weir",
        "sw_pump",
        "sw_orifice",
        "sw_outlet",
        "sw_subcatchment",
        "sw_suds_control",
        "sw_aquifer",
        "sw_snow_pack",
        "sw_raingage",
        "sw_curve_control",
        #"sw_curve_diversion",
        "sw_curve_pump",
        "sw_curve_rating",
        "sw_curve_shape",
        "sw_curve_storage",
        "sw_curve_tidal",
        "sw_curve_weir",
        "sw_curve_underdrain",
        "sw_land_use",  
        "sw_pollutant",
        "sw_polygon",
        "sw_General_line",    
        "sw_spatial_rain_source",
        "sw_spatial_rain_zone",
        "sw_transect",
        "sw_tvd_connector",
        "sw_soil",
        "sw_2d_zone",
        "sw_mesh_zone",
        "sw_porous_polygon",
        "sw_porous_wall",
        "sw_roughness_zone",
        "sw_mesh_level_zone",
        "sw_roughness_definition",
        "sw_2d_boundary_line",
        "sw_head_unit_discharge"
      ]
```

> Common Feature 3 - Table and Element Properties

Each table has properties or groups associated with it. These names can be found in the InfoWorks XML files, SQL dialogs, or dialog properties. For example, here are the conduit properties. Some of these will be familiar if you know the format of the EPASWMM5 INP file.

```
               <table name="sw_conduit"
               <group name="Conduit definition">id
                us_node_id
                ds_node_id
                branch_id
            </group>
            <group name="Conduit properties">
                length
                shape
                <field menu="sw_shape">shape_curve
                <field menu="sw_transect">transect
                horiz_ellipse_size_code
                vert_ellipse_size_code
                arch_material
                arch_concrete_size_code
                arch_steel_half_size_code
                arch_steel_inch_size_code
                arch_plate_18_size_code
                arch_plate_31_size_code
                conduit_height
                conduit_width
                number_of_barrels
                roughness_HW
                roughness_DW
                top_radius
                left_slope
                right_slope
                triangle_height
                bottom_radius
                shape_exponent
                us_invert
                ds_invert
                us_headloss_coeff
                ds_headloss_coeff
                Mannings_N
                bottom_mannings_N
                roughness_depth_threshold
                initial_flow
                max_flow
                sediment_depth
                av_headloss_coeff
                seepage_rate
                flap_gate
                culvert_code>
```

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHe5XjFNQW4Rw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682279260845?e=1795651200&v=beta&t=dpuM2y9fqUzC6OnO5QUSa1aRGlweK9kvLnD4mukQvjY)

You can also see the conduit properties in a dialog - here is the dialog for a Link in an SWMM network

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHenvyN_m0d2A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682279297108?e=1795651200&v=beta&t=K0meZ-XJGxFKqcB1ooG82WX_JdFOLUHszIh_FfOsYxM)

You can also see the conduit properties using the SQL dialog for the network - if you have an SWMM network on the Geoplan, then the SQL dialog will also show you the parameter names for the links or conduits.

> Common Feature 4 - How to use the Table Knowledge for Ruby Code?

Now that we know that the link length is just called length in a sw_conduit table, we can use this knowledge to find the statistics for the link lengths in our SWMM network. The following snippet shows the code for finding the lowest 10 percent of the link lengths - short pipes are important in an SWMM network as they normally govern the time step and simulation speed. Similar code can be used for an InfoWorks network - different table and property names but the same Ruby structure.

```
# Find the smallet 10 percent of pipe

net = WSApplication.current_network
net.clear_selection

link_lengths = []
ro = net.row_objects('sw_conduit').each do |ro|
  link_lengths << ro.length if ro.length
end

# Calculate the threshold length for the lowest ten percent
threshold_length = link_lengths.min + (link_lengths.max - link_lengths.min) * 0.1

# Select the links whose length is below the threshold
selected_links = []
ro = net.row_objects('sw_conduit').each do |ro|
  if ro.length && ro.length < threshold_length
    ro.selected = true
    selected_links << ro
  end
end
total_links = link_lengths.length

if selected_links.any?
  printf("%-40s %-0.2f\n", "Minimum link length", link_lengths.min)
  printf("%-40s %-0.2f\n", "Maximum link length", link_lengths.max)
  printf("%-40s %-0.2f\n", "Threshold length for lowest 10%", threshold_length)
  printf("%-40s %-d\n", "Number of links below threshold", selected_links.length)
  printf("%-40s %-d\n", "Total number of links", total_links)  
else
  puts "No links were selected."
ends
```

> Common Feature 5 - How do we make an SWMM Network from SWMM5, InfoSWMM, XPSWMM or an InfoWorks Network?

Make a new SWMM network, drag it to the Geoplan, and then using ICM Network Menu, you can import five types of network files.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGtEpZuTfQt4A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682274370621?e=1795651200&v=beta&t=hF7AzKMK-ovSkd3Gt7fsMFLZLx_kDvoiTOOKagFhtUE)

Make a new SWMM network, drag it to the Geoplan, and then using ICM Network Menu you can import five types of network files.

> Common Feature 6 - How do we make an InfoWorks Network from SWMM5, XPSWMM or an SWMM Network?

Make a new InfoWorks network, drag it to the Geoplan, and then use ICM Network Menu to import more than five types of network files, including direct import of SWMM5, SWMM Networks in ICM, and XPSWMM (XPX Files). InfoSWMM must be imported to an SWMM Network and converted to an InfoWorks network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHSFL_YeyFy1w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682299862190?e=1795651200&v=beta&t=NS9-m-NJTDU-jseG-j-tTAZPCZKYgmNP5AsVuzRQXaE)

How do we make an InfoWorks Network from SWMM5, XPSWMM or an SWMM Network?

> Common Feature 7 - InfoWorks and SWMM Networks share Model Group and Model Network features

In a model group (bullet 1), you can mix InfoWorks and SWMM Networks. InfoWorks Networks are yellow (bullet 2), and SWMM Networks are blue (bullet 3). InfoWorks and SWMM Networks can share SQL Code (Bullet 4) and ancillary model data such as inflow, patterns, and rainfall (Bullet 5). The Runs are unique to either InfoWorks or SWMM Networks (Bullet 6) and are not shared.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQG88ORxdl_2JA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682300758413?e=1795651200&v=beta&t=vNpBkzad_ryS-2dQO1hRkxfE9Iowt2qcyYHztR5c-TI)

Elements in the ICM Explorer Window

  

> Common Feature 8 - How do we import Model Groups from InfoSWMM, XPSWMM and SWMM5 to an ICM SWMM Network.

If you import InfoSWMM, XPSWMM XPX files or an SWMM 5 Inp file, then a complete model group is imported, including rainfall, inflow, and pattern data. These can be used for either an InfoWorks or SWMM Network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFN1MfXpWS1EA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682300309220?e=1795651200&v=beta&t=CJ9bWTrnwyEnWu9tF2-74HcvXB5gZJQxPvX3LcoMwMM)

How do we import Model Groups from InfoSWMM, XPSWMM, and SWMM5 to an ICM SWMM Network

  

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGrq7p3emo4dg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1682923540808?e=1795651200&v=beta&t=aMamCC-DN2hj-N30rRfCXviZlCOubwCegNEi2mR0jRM)

A few differences between HW and SW Tabls in ICM

> A few differences between HW and SW Tabls in ICM

Tables are used to organize ICM InfoWorks and ICM SWMM Networks, containing common elements such as nodes, links, and 2D elements. The prefix "hw" (HydroWorks) indicates an InfoWorks network table originating from the grandfather program to ICM in 1990. On the other hand, the prefix "sw" (SWMM) denotes a table for an SWMM network. InfoWorks networks have more tables due to their additional features compared to SWMM networks. However, in the context of this blog, the tables serve similar functions.
