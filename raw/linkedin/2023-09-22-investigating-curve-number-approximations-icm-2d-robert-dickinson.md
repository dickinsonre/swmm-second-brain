---
title: "Investigating Curve Number Approximations on an ICM InfoWorks 2D Infiltration Surface"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/investigating-curve-number-approximations-icm-2d-robert-dickinson
created: "2023-09-18 08:33"
published: "2023-09-22 07:10"
words: 1526
export_sha256: 1ac2232aa256f75ebc3f307b4c37c3f9264d4be99528724159710cec1bb802a1
---
# Investigating Curve Number Approximations on an ICM InfoWorks 2D Infiltration Surface

![ICM InfoWorks Infiltration 2D Surfaces ](https://media.licdn.com/mediaD4E12AQHGWEcKiPdA9Q "ICM InfoWorks Infiltration 2D Surfaces ")

In InfoWorks ICM, subcatchments and 2D infiltration surfaces are used to model the infiltration processes, representing the portion of rainfall that infiltrates into the ground rather than becoming surface runoff. While subcatchments in InfoWorks ICM can have various infiltration models including CN and CNSWMM on a pervious runoff surface, 2D Infiltration surfaces are restricted to four types: Horton, Green-Ampt, Constant Infiltration, and Fixed Infiltration.

![](https://media.licdn.com/dms/image/v2/D4E12AQHk9Lc70TYc2w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1695352931771?e=1795651200&v=beta&t=Un1IDOVip4PzVk3d97Tsuzcl3sHgpBpVMLLOIm4JbyM)

2D Infiltration surfaces are restricted to four types: Horton, Green-Ampt, Constant Infiltration, and Fixed Infiltration

### 1/ Infiltration Models for 2D Surfaces in ICM InfoWorks:

1.  **Horton Infiltration**: Represents the decline of infiltration capacity with time, starting from an initial rate and eventually reaching a constant rate.

2.  **Green-Ampt Infiltration**: Represents infiltration as a function of soil moisture content and is generally used for modeling infiltration during intense rainfall events.

3.  **Constant Infiltration**: Assumes a constant infiltration rate throughout the event and a fixed runoff coefficient.

4.  **Fixed Infiltration Equation**: Uses a fixed runoff coefficient.

### 2/ Curve Number (CN) Method:

The Curve Number method is another widely used approach to estimate direct runoff and infiltration from rainfall events. It's a simple, empirical model, primarily used in the SCS Runoff Curve Number method developed by the USDA Natural Resources Conservation Service.

### 3/ The Approximation Process:

Users looking to utilize the Curve Number method for 2D surfaces in InfoWorks ICM must approximate using one of the available infiltration models. For instance, Horton, Green-Ampt, Constant Infiltration, and Fixed Infiltration infiltration can be manipulated to mimic the behavior of a curve number. This approximation is crucial when a user needs to integrate the empirical simplicity of the Curve Number method with the sophisticated modeling capabilities of InfoWorks ICM.

### 4/ Test Model Description

Test Model Configuration:

The model consists of 23 subcatchments, with each subcatchment's ID corresponding to its Curve Number (CN). For instance, Subcatchment 80 has a CN of 80.

Scenarios:

We have established four scenarios to represent different types of 2D infiltration. The base scenario incorporates CN infiltration.

Objective:

The goal is to compare 1D and 2D infiltration across three distinct rainfall events, characterized by precipitations of 1.65 mm, 16.5 mm, and 165 mm, respectively.

Summary:

With a model incorporating subcatchments labeled and functioning based on their Curve Numbers, and four different infiltration scenarios, we aim to meticulously analyze and compare the infiltration behaviors in both 1D and 2D domains under varying rainfall intensities.

![](https://media.licdn.com/dms/image/v2/D4E12AQGf3pYKnTt3TQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695353332804?e=1795651200&v=beta&t=CLiE-f2aMri03Xy5ulCXYMhVhgA51bG3zlI-sVKtDzg)

Test Model - 23 Subcatchments with the ID of the Subcatchment the same as the Curve Number of CN for the Subcatchment

![](https://media.licdn.com/dms/image/v2/D4E12AQE_mPMdkYRmOw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695357099823?e=1795651200&v=beta&t=-Pcctod-fCaluDHsd7Bvl0DMt_TsjMXSn1-46xEdrOY)

Four Scenarios for the types of 2D infiltration, Base is CN infiltration.

### 5/ The Experiment:

The Test Network is designed to encompass a range of infiltration scenarios and facilitate comprehensive analysis. On the left side of the network, four distinct 2D infiltration surfaces are strategically positioned, each exemplifying a unique infiltration type, thereby serving as a representative framework for assessing the variability in infiltration patterns and behaviors. Within this network, there are 23 well-defined Subcatchments, each subjected to four scenarios and three varying rainfall events. These different configurations and events are aimed at simulating the hydrological conditions and responses, allowing for an in-depth examination of the interaction between rainfall and infiltration processes.

To further refine the hydrological representation, the network incorporates a singular pervious runoff surface. This inclusion is pivotal in simulating the interaction between surface water and the infiltration process, providing a more holistic view of the hydrological cycle within the defined scenarios. The choice of hydrology model is the well-established SWMM hydrology.

Moreover, the flexibility and adaptability of the network are enhanced by the capability to use SQL to set the key infiltration parameters for each scenario. This allows for precise manipulation and control over the scenario conditions, enabling users to fine-tune the parameters to meet the specific requirements of each test case. The ability to modify infiltration parameters using SQL is invaluable in conducting rigorous and detailed analyses, allowing for the exploration of the intricate dynamics of infiltration under varying hydrological conditions.

![](https://media.licdn.com/dms/image/v2/D4E12AQH3Efoon0WEhA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1695357592973?e=1795651200&v=beta&t=IW3fWAzCuc8yWOp4_2cq_0lmA_WhUx0pfvkisxFhW9c)

The Test Network has four 2D infiltration surfaces on the left - each with a different infiltration type.

![](https://media.licdn.com/dms/image/v2/D4E12AQHEBmE3GllIBw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1695359612753?e=1795651200&v=beta&t=JaDn-vl-_IDYbnvoCqQQO4yegLzWgr4I5Oabak3o6cQ)

There is one runoff surface and the hydrology used is SWMM hydrology.

![](https://media.licdn.com/dms/image/v2/D4E12AQFm-kEtJ9Nrqg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1695359505218?e=1795651200&v=beta&t=p0gVtYWHX-OC0x1XWK_XVSdxz6bjLXt2OGncrd7Z2W4)

You can use SQL to set the key infiltration parameters for each scenario.

![](https://media.licdn.com/dms/image/v2/D4E12AQHsPMw73iL9AA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695359917482?e=1795651200&v=beta&t=_kmCA9VYVFHhnwmBiR0HroE5ecBZIG6JYcE2JxObGeo)

You can see the 2D infiltration results in the log file of ICM InfoWorks

### 6/ The Results for 1D:

When observing the behavior of CN (Curve Number) 1D Subcatchment Infiltration, a notable and crucial relationship between the CN values, the peak infiltration rate, and the total infiltration volume becomes evident. As the CN value decreases, there is a corresponding increase in both the peak infiltration rate and the total infiltration volume. This inverse relationship is paramount in understanding the dynamics of infiltration processes within hydrological models.

The Curve Number method is an empirical model and the CN value essentially represents the potential maximum retention after runoff begins. A lower CN implies a higher potential for retention, which, in turn, corresponds to higher infiltration. Thus, as the CN value decreases, the soil or the surface is characterized by a higher permeability, allowing more water to infiltrate during a rainfall event, thereby increasing the peak infiltration rate and the overall volume of water infiltrated.

![](https://media.licdn.com/dms/image/v2/D4E12AQEPKyKYYpkTug/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1695363995245?e=1795651200&v=beta&t=EbK039HnXmYQjddKMy7tJhwL4ECqFS2UhP0TSqQmdds)

As the CN decreases the peak infiltration rate and the total infiltration volume increases with CN 1D Subcatchment Infiltration

We can establish the peak infiltration rate and utilize SQL to define a consistent infiltration loss rate for Horton, Green Ampt, and ConstInf within ICM. Given the simplicity of the rainfall hyetographs typically used in 2D modeling, the peak and volume of infiltration are found to be closely aligned across all four infiltration methods.

![](https://media.licdn.com/dms/image/v2/D4E12AQE6LL1d8iwHvA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1695364424991?e=1795651200&v=beta&t=2LWq0GKr2sljT17PuqhZSfBitghB0fgjL54SBdF7fpk)

![](https://media.licdn.com/dms/image/v2/D4E12AQF42mZf3u_MSg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1695364758061?e=1795651200&v=beta&t=sMWJxs5MbrlZ9ia5Rf14o8RWfSZnHE345e8TmMIRo3A)

For small rainfall storms the peak and infiltration rate is almost the same.

The nonlinear reservoir hydrology of SWMM aids in aligning the 1D results after the maximum infiltration rate is modified based on the CN results, promoting similarity in outcomes despite the variations in infiltration rates. However, when applied to a 2D surface, the results are bound to differ. This is primarily due to the variable depths existing within the 2D mesh, affecting the flow and accumulation of flooded water as it traverses the mesh. These variations in depth across the mesh introduce a range of interactions between surface water and the mesh, leading to divergent infiltration patterns and outcomes compared to the 1D scenario.

### 7/ The Results for 2D:

The Constant Infiltration, Green Ampt and Horton for smaller rainfall have the same effective infiltration rate - fixed is different. This shows the calibrated to rate to CN rate can work for the 2D mesh. You can also look at the log 2D report to see the total infiltration for the 2D Surfaces with different infiltration methods.

![](https://media.licdn.com/dms/image/v2/D4E12AQEin2EbCyO_gQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695365305451?e=1795651200&v=beta&t=LwXnp4U9rHALvoNP_sU-YaRuFhhieiUKVNWwB6jjJtc)

2D Effective Infiltration Rate for Fixed infiltration.

![](https://media.licdn.com/dms/image/v2/D4E12AQHduq2umLdzwA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695365444222?e=1795651200&v=beta&t=RkN8tv1A8ZHkfwJYyPqLuccGTK5xiHtBJFtNUW4cjbQ)

2D Effective Infiltration Rate for ConstInf infiltration.

![](https://media.licdn.com/dms/image/v2/D4E12AQGRFd7R_FByQg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695365536752?e=1795651200&v=beta&t=FamvCJSTN2WSNOFdr4ky5yOCoA_CYk0iy5gYhA1l2rc)

2D Effective Infiltration Rate for Horton infiltration.

aa

![](https://media.licdn.com/dms/image/v2/D4E12AQEwB3XzVc8jmA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1695365639931?e=1795651200&v=beta&t=YqGraHj2_ZuElw_8r9Vuu0rIJg5nqU0fudiGfLqtRiY)

2D Effective Infiltration Rate for Green Ampt infiltration.

### 8/ Ruby Help

Currently underway is the development of Ruby scripting, aimed at integrating functionalities to compute time-specific and overall mean and total infiltration values corresponding to each mesh within the 2D Infiltration polygon in InfoWorks ICM.
