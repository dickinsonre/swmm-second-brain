---
title: "ICM, Siphons, How to Model Sediment in a Siphon, ICM SWMM, SWMM5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/icm-siphons-how-model-sediment-siphon-swmm-swmm5-robert-dickinson-i5lme
created: "2023-10-14 20:14"
published: "2023-10-29 15:15"
words: 2731
export_sha256: 48636ce396f3de05b768c782d08ecbc972c3f40a901ff7ca95f8ee1cdd1cfdac
---
# ICM, Siphons, How to Model Sediment in a Siphon, ICM SWMM, SWMM5

![ICM InfoWorks Network and ICM SWMM Network](https://media.licdn.com/mediaD5612AQF7IdYL8gsUZw "ICM InfoWorks Network and ICM SWMM Network")

> **Active and Passive Sediment Modeling i**n an ICM InfoWorks Network with a **Siphon**

In this LinkedIn article, we're taking a unique approach: beginning at the end and tracing our steps backward to the start. As indicated by the title - "ICM, Siphons, How to Model Sediment in a Siphon, ICM SWMM, SWMM5" - our primary focus is on simulating sediment, both active and passive, within a siphon in an ICM InfoWorks network.

The siphon's initial model was sourced from SWMM5 and subsequently imported into the ICM SWMM network. After this, a seamless internal conversion took place, transforming it into an ICM InfoWorks network. One of the standout advantages of this method is the ability to import not only the model network but also the inflow time series simultaneously, ensuring consistency and accuracy in the modeling process.

However, it's crucial to note that sediment parameters are incorporated only after the conversion to InfoWorks. This is due to a distinct difference between the two platforms: SWMM5 does not inherently support sediment modeling (only TSS concentration). By transitioning to InfoWorks, we can effectively introduce and model sediment parameters, thereby enhancing the accuracy and depth of our hydraulic analysis.

> **Step 12:** Sediment in the Siphon both passive (sed depth) and active (US and DS Sediment depth)

**Analyzing the Model Results: A Comprehensive Guide**:

After running the model, it's essential to delve into the results to gather insights and make informed decisions. Here's how you can systematically analyze the outputs:

1.  **Grid View**:

    This provides a tabulated representation of the results. It's especially beneficial for a quick overview and for comparing multiple data points simultaneously.

2.  **Graphical Representation**:

    Graphs offer a visual representation of the results, making it easier to discern trends, peaks, and anomalies over time or across variables.

3.  **Long Section Plot**:

    This is particularly useful for understanding flow dynamics, sediment accumulation, and other parameters across the length of a conduit, such as a pipe or channel. The cross-sectional view can reveal variations and potential areas of concern.

4.  **Thematic Visualization**:

    Themes can be applied to visually represent data ranges, making it intuitive to identify areas of high or low values, or to quickly spot regions that meet certain criteria.

5.  **Leveraging Ruby for Output Time Series**:

    For more advanced users, Ruby scripting can be utilized to extract and process the output time series. This allows for custom analysis and potential automation of repetitive tasks.

6.  **Time-Varying vs. Summary Maximum Data**:

    You have the flexibility to either delve into time-varying data, which provides insights at each time step, or to view summary maximum data, which gives a snapshot of peak values.

7.  **Engine Summary in the Log File**:

    Don't overlook the engine summary provided in the log file. This offers a concise overview of the simulation, including potential warnings, errors, and key performance indicators.

By leveraging these tools and views, you can gain a holistic understanding of the model's outputs, ensuring that you're well-equipped to make informed decisions based on the simulation results.

The long section shows the US and DS hydraulic and sediment depths. The sediment mass balance is shown in the log file in the run.

![](https://media.licdn.com/dms/image/v2/D4E12AQGivgD8Nlr6Lg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1698532800921?e=1795651200&v=beta&t=2UMWKaaq2-8NKB0eFa2GsMizKpzoSyO9-g-w1BlFCL0)

**Maximum Long Section of Hydraulic and Sediment Maximums**

> **Step 11: Define the potency factor for BOD in the Pollutograph**

**Associating BOD with Sediment Fraction SF1: A Detailed Guide**:

**Understanding Attached Pollutant Potency**: Attached pollutant potency plays a crucial role in determining how much of a specific pollutant, in this case BOD, is associated or bound to a sediment fraction, here referred to as SF1.

**Step-by-Step Process**:

1.  **Navigating to the Appropriate Tabs**:

    Begin by accessing the attached determinant tabs. These include BOA, COA, TKA, TPA, P1A to P4A, ALA, and C1A to C4A. Each of these tabs provides a platform to define potency factors for different attached determinants.

2.  **Defining Potency for SF1 BOD**:

    Navigate to the specific tab that corresponds to the BOD for SF1. Here, you'll be inputting time-varying potency factors. These factors essentially represent the concentration of BOD that is attached or bound to the sediment fraction SF1 over a specific time frame.

3.  **Overriding Default Values**:

    It's important to note that the time-varying potency factors you input will take precedence over any default or fixed potency factor that might be pre-defined in the dissolved determinant tab. This ensures that your specific input, which is more tailored to the current scenario, will be the guiding factor during simulations.

4.  **Finalizing Inputs**:

    After inputting the appropriate potency values, ensure you save and confirm your changes. This guarantees that the model will utilize these updated values during its simulations, offering a more accurate representation of the BOD associated with sediment fraction SF1.

![](https://media.licdn.com/dms/image/v2/D4E12AQHQt7DjvJXQQA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698591653046?e=1795651200&v=beta&t=vYkrEOQ7xm3AOx7rD2H3KKOi3S-9tlyBYT5URLQE5vo)

**Define the potency factor for BOD in the Pollutograph**

> **Step 10: We need to define an inflow Pollutograph to add upstream sediment and BOD to the flow into the Siphon network**

**Crafting a New Pollutograph for Inflow Sediment and BOD**:

Given the limitations of both SWMM5 and ICM SWMM, which lack features for active and passive sediment modeling, it's imperative for us to take an alternative route for accurate sediment and BOD representation in our Siphon network simulation.

**Step-by-Step Guide**:

1.  **Understanding the Need**:

    Unlike systems with subcatchments that account for sediment Buildup and Washoff, our setup does not inherently incorporate these details. This presents a challenge when attempting to simulate the behavior and impact of sediment and BOD in the network.

2.  **Initiating the Pollutograph**:

    Navigate to the section where you can define a new time series. Here, we're aiming to create a pollutograph, which is essentially a graphical representation of pollutant concentrations over time.

3.  **Defining the Inflow Pollutograph**:

    The objective is to introduce upstream sediment and BOD into the flow directed into the Siphon network.This pollutograph will serve as a surrogate for the sediment and BOD behavior, compensating for the lack of active and passive sediment features in our modeling tools.

4.  **Inputting Data**:

    We previously had a time series (TS) for SF1 BOD. Ensure this data is integrated into the pollutograph, capturing the nuances of sediment and BOD [concentrations.It](http://concentrations.It)'s crucial to input this data accurately, ensuring the time intervals and concentrations reflect real-world or anticipated scenarios.

5.  **Finalizing and Implementing**:

    Once the pollutograph is defined and populated with the necessary data, save and integrate it into the main model. This will ensure that the model considers sediment and BOD concentrations during simulations, providing a more realistic representation of the Siphon network's behavior.

By carefully crafting this pollutograph, we bridge the gap left by the limitations of SWMM5 and ICM SWMM, ensuring our model remains accurate and representative of sediment and BOD dynamics.

------------------------------------------------------------------------

![](https://media.licdn.com/dms/image/v2/D4E12AQEo6A3zOCYZmw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698589184099?e=1795651200&v=beta&t=mn59PoFZIIU-icRkJ8h-mJNNY06Gxca3beDZCUs1Mpg)

**We need to define an inflow Pollutograph to add upstream sediment and BOD to the flow into the Siphon network**

> **Step 9:** Sediment **QM Dialog to select both BOD and SF1 or Sediment**

**Configuring Sediment Parameters in the Run QM Dialog**:

To finely tune our sediment modeling, we'll utilize the Sediment QM Dialog. Our goal is to achieve a comprehensive representation that encompasses both the dissolved Biochemical Oxygen Demand (BOD) and the sediment-attached BOD. Here's how to go about it:

- Begin by accessing the **Sediment QM Dialog**.

- Once inside, ensure you select **BOD** to capture the dissolved aspects of the biochemical oxygen demand.

- Next, opt for **SF1** or simply **Sediment**. Given that our focus is on modeling a single sediment type, this step ensures that we're encapsulating the sediment-attached BOD accurately.

![](https://media.licdn.com/dms/image/v2/D4E12AQE0efZj8RKl6g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698537091349?e=1795651200&v=beta&t=c3ZEHM5I_uYa2SXM75JHuIHkwyKGikmK17KKJ2LmaW8)

**QM Dialog to select both BOD and SF1 or Sediment**

> **Step 8:** Sediment Models (KUL, Ackers-White and Velikanov), Define the parameters in the Water Quality Dialog

**Defining Sediment Model Parameters in the Water Quality Dialog**:

1.  **KUL Model**:

    Start by selecting the KUL scenario from the scenarios list.Navigate to the Water Quality Dialog and choose the KUL model from the list of sediment models.Input or adjust the necessary parameters specific to the KUL scenario.

2.  **Ackers-White Model**:

    Switch to the Ackers-White scenario.Access the Water Quality Dialog for the Ackers-White model.Define or tweak the parameters that cater to the Ackers-White sediment model. Commit the alterations.

3.  **Velikanov Model**:

    Transition to the Velikanov scenario.Once again, open the Water Quality DIalog the Velikanov model.Fill in or refine the relevant parameters for this specific sediment model. Commit the alterations.

![](https://media.licdn.com/dms/image/v2/D4E12AQFk2MnusOhF1A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698537518383?e=1795651200&v=beta&t=woMTBZqPCBlih9y09OBZ477OxpkqPIIxyKCinAGuh4Q)

Water Quality Dialog

> **Step 7:** Set the Passive Sediment Depth in the Link Grid

**Understanding Sediment Layers in Simulations**

**1. Passive Layer**:

- **Definition**: The passive layer represents sediment that remains static throughout simulations, essentially acting as a narrowing agent within the conduit.

- **Configuration**:Its depth is determined using the 'Sediment Depth' attribute for each conduit.Alternatively, 'Pipe Sediment Data' can be utilized, and if included in a simulation, it takes precedence over values in the 'Sediment Depth' field.Notably, 'Pipe Sediment Data' is typically employed to tweak the Passive Layer, mainly influencing the maximum depth of the Active Layer in water quality evaluations. Thus, it's exclusive to water quality simulations.

**2. Active Layer**:

- **Definition**: This layer consists of dynamic sediment, which undergoes erosion, transportation, and deposition during a simulation.

- **Composition**:It comprises one or two sediment fractions with distinct properties, termed as Sediment Fraction 1 (SF1) and Sediment Fraction 2 (SF2).Each sediment fraction is characterized by:**D50**: Represents the median sediment particle size. The default is 0.04mm.**Specific Gravity**: Indicates the density of the sediment fraction, with a default value of 1.7.

- **Configuration**:These parameters can be adjusted in the 'Surface Pollutant Editor'. Should you wish to alter or if they appear blank, you can update them or establish personal default settings in the 'Water Quality and Sediment Parameters' section. In the absence of specific inputs, the aforementioned default values are employed.

![](https://media.licdn.com/dms/image/v2/D4E12AQHEpiYLRhwNgQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1698537546362?e=1795651200&v=beta&t=1MeDvrO81vA5uZqMyodfzF9h7hjMhlmGzb3Zde2knQg)

Set the Passive Sediment Depth in the Link Grid

> **Step 7:** Inflow Time Series for both SWMM and SIM Engines

**Characterizing the Inflow**: A notable aspect of our model is the inflow design. The inflow we're working with is substantially large, exhibiting a trapezoidal shape. This specific shape is purposefully chosen to aptly demonstrate the dynamics of the siphon - how it fills up and subsequently empties.

![](https://media.licdn.com/dms/image/v2/D4E12AQHnvNesY-u7gg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1698586145425?e=1795651200&v=beta&t=46Jn0t2K7BLbkomNGgk6D7uH9BzRebTtl2bh2vmepc4)

Inflow Time Series for both SWMM and SIM Engines

> **Step 6:** Add New Scenarios for each of the three Sediment Types

**Developing an ICM Model with Diverse Sediment Modeling Capabilities**: As part of our continued efforts to provide comprehensive modeling solutions, we're embarking on creating an ICM model that encapsulates three distinct sediment modeling methodologies. To achieve this, we will introduce three new scenarios to our model. These scenarios will encompass the following sediment models: **KUL Model**, **Ackers-White Model** and **Velikanov Model** *(see the online help file for background information on the sediment models).*

With the integration of these models, our ICM model is set to offer a more holistic and versatile approach to sediment analysis, catering to a wide range of requirements.

![](https://media.licdn.com/dms/image/v2/D4E12AQGYl680p3GZYg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698580429642?e=1795651200&v=beta&t=I0NeB6mJOeiuOLZJjdvbls73Jjz35jOmn-m-A6fg3Jw)

New Scenarios for each of the three Sediment Types

> **Step 5:** Validate and then Commit the ICM InfoWorks Network

**Finalizing the ICM InfoWorks Network**: Begin by validating, followed by committing the ICM InfoWorks Network. Given the robust compatibility between ICM and the SWMM5 network data, we anticipate a smooth validation with no errors. In fact, our recent validation confirmed there were no issues, though it's worth noting that our model was relatively straightforward. It's also worth highlighting that ICM's proficiency in importing SWMM5 files has been well-established over time.

![](https://media.licdn.com/dms/image/v2/D4E12AQEqINN-cQb6Sg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1698580738052?e=1795651200&v=beta&t=O4FFbNzQllVmq0MYPsWQMSCp2skZ3HuV083IQXvxmBI)

Validate and then Commit the ICM InfoWorks Network

> **Step 4:** Import into a NEW InfoWorks network the the just validated SWMM Network

**Transitioning to a New InfoWorks Network**: With our SWMM Network validated, our next objective is to integrate it into a fresh InfoWorks network. We initiate this by crafting a brand-new InfoWorks Network. Subsequently, we seamlessly import our validated SWMM network into this ICM InfoWorks environment. The icing on the cake? We can effortlessly utilize the same inflow time series in ICM that we previously employed for SWMM, ensuring consistency across our SWMM and SIM Engines.

![](https://media.licdn.com/dms/image/v2/D4E12AQFzTffOtWxbVA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1698580763678?e=1795651200&v=beta&t=PSphHyFFa26avUPqIY4KnY-wmwp4GzbhIv5KD1PA-1s)

Import into a NEW InfoWorks network the the just validated SWMM Network

> **Step 3:** View the Long Section ICON to view the SWMM Engine Results

**Post-Model Execution Insights**: Having successfully executed the model within ICM utilizing the SWMM network, we are now poised to delve deeper into the results. One can either peruse the SWMM5 .rpt file for insights or, for a more visual representation, utilize the ICM Tools to craft a comprehensive long-section plot. This will vividly illustrate the peak flows and depths within our siphon model, offering a clearer understanding of its dynamics. We can also compare now more easily the SWMM and SIM engine (SIM is ICM, SWMM is ICM SWMM)

![](https://media.licdn.com/dms/image/v2/D4E12AQGQG8oTiHrJXA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1698580965413?e=1795651200&v=beta&t=1oZ8AHzUKNLoh75d9_suzX78wGO1WRLCJSxh80g7uxg)

View the Long Section ICON to view the SWMM Engine Results

> **Step 2:** Run the SWMM Network after validating it and committing the validated Network

**Model Execution Post-Validation**: Having diligently validated and committed our SWMM network within the ICM user interface, we are now perfectly positioned to run the model. A Run dialog has been made as part of the model group import. This allows us to harness the full potential of both the imported network and the corresponding time series data.

![](https://media.licdn.com/dms/image/v2/D4E12AQGKGlP-Qmmlmw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698584398189?e=1795651200&v=beta&t=AdPKkipmVqX_43beE9JZwa0JyqaQh9nInh8865yZBcU)

**SWMM5 data in an ICM SWMM Network - see the properties dialog to the left**

> **Step 1:** Import a SWMM5 model (Large Siphon) as a Model Group in ICM SWMM

**Purpose and Rationale**: One may wonder about the motivation behind our approach. By importing a SWMM5 model, specifically a Large Siphon, into ICM SWMM as a Model Group, we achieve a multifaceted benefit. Not only does this method allow for the seamless integration of SWMM5 nodes and links, but it also brings in the valuable inflow time series. Opting to import into ICM SWMM, as opposed to ICM InfoWorks, ensures that both rainfall and flow time series data can be utilized across both ICM SWMM and ICM InfoWorks networks. This holistic approach ensures consistency, efficiency, and a broader applicability of our data.

![](https://media.licdn.com/dms/image/v2/D4E12AQEYtjAaXWhzbg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1698584066088?e=1795651200&v=beta&t=TdFZGBNPmF35U-mONlfYEWUIKR1x8mQN-YqNRMRFBuY)

**Import a SWMM5 model (Large Siphon) as a Model Group in ICM SWMM**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time!
