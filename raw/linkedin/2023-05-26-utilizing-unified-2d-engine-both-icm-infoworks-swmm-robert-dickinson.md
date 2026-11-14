---
title: "Utilizing a Unified 2D Engine in both ICM InfoWorks and ICM SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/utilizing-unified-2d-engine-both-icm-infoworks-swmm-robert-dickinson
created: "2022-11-07 04:23"
published: "2023-05-26 19:15"
words: 1498
export_sha256: 8c6ce151cb722112ba6ce9e7842d97bd9140411f87da6d3551ff924cbecd0737
---
# Utilizing a Unified 2D Engine in both ICM InfoWorks and ICM SWMM Networks

![Utilizing a Unified 2D Engine in both ICM InfoWorks and ICM SWMM Networks](https://media.licdn.com/mediaD4E12AQFsbLICoST_Uw "Utilizing a Unified 2D Engine in both ICM InfoWorks and ICM SWMM Networks")

> ICM InfoWorks 2D and ICM SWMM 2D comparison

Hello to all the SSF infrastructure enthusiasts out there,

Ever wondered how two different network systems can be interrelated and coexist in the same graphical user interface? Well, today we're delving into the innovative world of coexisting ICM SWMM and ICM InfoWorks networks. You'll be fascinated to know that these two systems share the same 2D engine, providing a unique opportunity for increased compatibility and functionality. They obviously do NOT share the same 1D network as ICM SWMM uses the SWMM 5.2.3 Engine and InfoWorks uses a proprietary Engine. They both solve the 1D Saint Venant Equation in slightly different forms.

**Note from the help file:** *The 2D engine used for InfoWorks and SWMM simulations is based on the 2D model Mulet & Alcrudo unstructured flood solver. All rights reserved. Designed by Francisco Alcrudo Sanchez and Jónatan Mulet-Martí. MULFLOOD and the procedures described in Alcrudo and Mulet-Marti (2005). See the Basic 2D Hydraulic Theory topic for further details in the ICM Help file*.

ICM SWMM, or Storm Water Management Model, is a comprehensive tool that is primarily used for the simulation of water quantity and quality in primarily urban areas. On the other hand, ICM InfoWorks networks offer a cutting-edge solution for managing flooding, wastewater, and stormwater systems for integrated catchment management. InfoWorks has more controls and 1D features than SWMM.

Despite their individual 1D differences, these two systems share a common denominator: the same 2D engine. This shared feature unlocks a whole new realm of possibilities, from increased interoperability to enhanced simulation capabilities.

While it's true that InfoWorks has a broader feature set, especially when it comes to 1D and 2D functionalities, this doesn't limit the potential of ICM SWMM. In fact, it's possible to convert an InfoWorks 2D network to an SWMM 2D network. This capability opens up a world of possibilities for those who are already familiar with ICM SWMM but wish to incorporate some of the advanced 2D features available in InfoWorks.

The purpose of this blog is to provide a detailed guide on how to make this conversion from InfoWorks 2D to SWMM 2D. This step-by-step guide will enable you to leverage the power of both systems, taking your water management simulations to a whole new level.

> 2D elements in ICM InfoWorks and SWMM Networks

As before, there are more elements in the ICM InfoWorks list than in the ICM SWMM list, leading to empty cells in the ICM SWMM column. An InfoWorks Network has more features for 2D modeling but shares the same 2D engine. If you convert an InfoWorks 1D and 2D network to SWMM any feature not in SWMM is not converted - a basic assumption.

![](https://media.licdn.com/dms/image/v2/D4E12AQHlErmnFiK7ZA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1684098392848?e=1795651200&v=beta&t=sKQ4-Ha2Wo6cmSMUb_5yzilBS0wGww8RilGKcfLJHbk)

2D elements in ICM InfoWorks and SWMM Networks

**The transition of a model from InfoWorks to ICM SWMM** involves a direct conversion of both 1D and 2D elements, enabling the transfer of complex hydraulic and hydrological models between software platforms. This feature is particularly beneficial for modelers and engineers working in different environments, or those who prefer the specific functionalities offered by one software over the other.

In more detail, here's what this process involves:

1.  **Conversion of 2D Elements:** InfoWorks 2D elements, such as surfaces and grids, can be converted directly into ICM SWMM. These 2D elements usually represent overland flow and flooding processes, which are crucial for comprehensive urban drainage and flood risk analysis. The conversion retains the spatial variability of terrain and hydraulic parameters, which is fundamental for the accurate simulation of 2D processes.

2.  **Conversion of 1D Elements:** InfoWorks 1D elements, such as pipes, channels, and manholes, are converted into their corresponding elements in ICM SWMM. These elements typically represent the sewer or drainage network, and their accurate conversion ensures that the hydraulic behavior of the system remains consistent across both platforms.

3.  **Parameter Transfer:** All associated parameters, including hydraulic, hydrologic, and operational parameters, are also transferred between the two platforms. This ensures that the behavior of the system remains consistent, maintaining the integrity of the model.

4.  **Validation:** Following the conversion, the newly created ICM SWMM model undergoes a validation process to ensure the accuracy of the transfer.

The ability to directly convert InfoWorks networks into ICM SWMM networks allows for greater flexibility and collaboration between teams and across projects. It also provides a pathway for utilizing the advanced functionalities offered by ICM SWMM, such as its comprehensive treatment of water quality processes, its expanded range of low-impact development (LID) controls, and its other rainfall-runoff modeling capabilities.

![](https://media.licdn.com/dms/image/v2/D4E12AQHkuj4i2-u8og/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685121567861?e=1795651200&v=beta&t=-tUEanlwZZVDelJu_RWrPlZMljrsBzuTeBxfukbVqNA)

The transition of a model from InfoWorks to ICM SWMM

> Validation of the ICM SWMM Network

Upon successfully transitioning from InfoWorks networks to ICM SWMM models, it is crucial to validate the converted network. This is a critical step in ensuring the accuracy and reliability of the newly created model. There might be some incompatibilities due to differences in how InfoWorks and SWMM handle certain types of data.

For instance, in SWMM, a rain gauge is required to encapsulate the rainfall time series data. If this feature is missing in the InfoWorks model, you may encounter a validation error. These discrepancies need to be resolved for the accurate representation of real-world hydrologic and hydraulic processes.

Additionally, there's a unique identifier requirement in SWMM that doesn't permit having the same ID for a Subcatchment and a Node. If such a situation arises during the conversion, SQL comes to the rescue. You can run a SQL script to add a prefix to the Subcatchment ID to distinguish it from the Node ID.

**SET subcatchment_id = 'S\_' + subcatchment_id;**

![](https://media.licdn.com/dms/image/v2/D4E12AQGUHRsw94hVsw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685121196440?e=1795651200&v=beta&t=SaN49I-QmeD0bvkJvSLq1dlGlnLe32SxR9k63adIA_k)

Validation of the ICM SWMM Network

> Make a Rain Gage and add the ICM InfoWorks Network Rainfall Profile to the Gage. InfoWorks and SWMM can share the same Rainfall.

![](https://media.licdn.com/dms/image/v2/D4E12AQFm-TcOWLrafQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1685121135280?e=1795651200&v=beta&t=kH4iypAi7jL_9KsJJMOmHL26PJStoEb-tfTKV1fRB-4)

Make a Rain Gage and add the ICM InfoWorks Network Rainfall Profile to the Gage. InfoWorks and SWMM can share the same Rainfall.

> In ICM InfoWorks, a node that possesses a 1D to 2D connection is assigned a flood type of 2D.

![](https://media.licdn.com/dms/image/v2/D4E12AQEFsvdQH1Pd5g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685127500503?e=1795651200&v=beta&t=4ER1zqGPkNvHytuywBjL_EGr1pn7M6XIgK35Km0BOtM)

In ICM InfoWorks, a node that possesses a 1D to 2D connection is assigned a flood type of 2D.

> In ICM SWMM, a node that possesses a 1D to 2D connection is assigned a flood type of 2D.

![](https://media.licdn.com/dms/image/v2/D4E12AQF-AyDtE5oYUw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685127555762?e=1795651200&v=beta&t=lWFinA8To9sTLvpVr_MR3EM701as_6623uUSqUGDoEQ)

In ICM SWMM, a node that possesses a 1D to 2D connection is assigned a flood type of 2D.

> InfoWorks 2D Flooding using the Show Maxima

![](https://media.licdn.com/dms/image/v2/D4E12AQFePlU7nlZbGQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685121166002?e=1795651200&v=beta&t=ab-s4Q3Af5lqHCBoaTfBY0KNWmEJrxcD_nb4yo59M_Y)

InfoWorks 2D Flooding using the Show Maxima

ICM SWMM 2D Flooding using the Show Maxima. There is more flooding due to the difference in hydrology. ICM SWMM uses SWMM Hydrology and the InfoWorks network used the Wallingford option.

![](https://media.licdn.com/dms/image/v2/D4E12AQEpM3HcDNfBCQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685127766609?e=1795651200&v=beta&t=evkcdUOR2iQMF5UqfDvitw6N25TbetM1O4Bk9FTDgpA)

ICM SWMM 2D Flooding using the Show Maxima. There is more flooding due to the difference in hydrology. ICM SWMM uses SWMM Hydrology and the InfoWorks network used the Wallingford option.

> The 2D Results for the InfoWorks Network are shown in the Log File.

![](https://media.licdn.com/dms/image/v2/D4E12AQH62bT5oPv2Cg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685127443884?e=1795651200&v=beta&t=5d8kBOP_PxiNisIs7gjwvt1cY8_uj1BRmSC3beLEkeI)

The 2D Results for the InfoWorks Network are shown in the Log File.

> The 2D Results for the ICM SWMM Network are shown in the report file. The format of the 2D reports are the same. ICM SWMM has more flooding due to the differences in hydrology.

![](https://media.licdn.com/dms/image/v2/D4E12AQGTGD2Ki3j3pA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1685127462824?e=1795651200&v=beta&t=tsS3kPwkLFNTIuM9wOaeGBLKVNgunqopA1NXZj_XigY)

The 2D results for the InfoWorks Network are shown in the log File.

**Closing Question:** What features do you find most valuable in the ICM SWMM or ICM InfoWorks networks?
