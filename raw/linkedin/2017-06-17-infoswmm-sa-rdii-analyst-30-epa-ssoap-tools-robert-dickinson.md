---
title: "InfoSWMM, InfoSWMM SA RDII Analyst 3.0 with EPA SSOAP Tools"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/infoswmm-sa-rdii-analyst-30-epa-ssoap-tools-robert-dickinson
created: "2017-06-17 10:18"
published: "2017-06-17 11:02"
words: 4019
export_sha256: dea0e4ddd4516280e2af109f7aa828ad5fe6ab57d82545840e7e586d7d072906
---
# InfoSWMM, InfoSWMM SA RDII Analyst 3.0 with EPA SSOAP Tools

One of the most powerful InfoSWMM, InfoSWMM SA and H2OMAP SWMM Application Tools from Innovyze is RDII Analyst. RDII Analyst will separate out the Groundwater base flow, Dry Weather Flow (DWF), DWF Patterns, estimate the Wet Weather flow component or RDII Rainfall -Derived Infiltration Inflow (I&I) and use a Genetic Algorithm to find the best fit 18 RTK parameters for RDII modeling. 

> This powerful tool can be used for RTK flow in InfoSWMM, InfoSWMM SA, H2OMAP SWMM, InfoSewer, SWMM 5 and InfoWorks ICM. 

Figure 1 shows one of the end results of RDII Analyst – a correlation plot of Observed versus Calibrated RDII Volume for the simulated events. New to 2017 is the ability to show all 3 R values, do scenario comparison of computed R, save and open many existing calibration runs and have 1 to 10 solutions per run.

> RDII Analyst is a significant improvement over the EPA SSOAP program, performs QA/QC of rainfall and flow monitoring data and decomposes the flow data into Dry-Weather Flow (DWF) and Wet-Weather Flow (RDII) components using criteria such as rainfall threshold.

The DWF component is further analyzed to construct a DWF pattern that can be used to simulate the collection system using InfoSWMM. The DWF pattern is then assigned to the source nodes that contribute DWF to the meter location in proportion to sewershed areas or based on other criteria. The RDII component is then analyzed to determine RDII events and to calibrate parameters of the RTK synthetic unit hydrograph so that the RDII flow simulated by the RTK method closely matches the RDII flow obtained by the decomposition process. The RTK unit hydrograph parameters are calibrated with genetic algorithm optimization. The calibrated RTK parameters and the DWF patterns are then passed to InfoSWMM to carry out detailed dynamic flow routing through the sewer system and evaluate system response to support the development of an optimal capital improvement program. You can read the World Environmental and Water Resources Congress paper by Misgana and Boulos (2008) with a complete description and validation of the RDII Analyst workflow process for both [RDII Analyst](http://www.innovyze.com/products/infoswmm/rdii.aspx) and for the [InfoSWMM Calibrator](http://www.innovyze.com/products/infoswmm/calibrator.aspx) Add-On in the InfoSWMM Suite (Boulos, 2005)

  

![](https://media.licdn.com/dms/image/v2/C5112AQF4lw8R7igp0w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520143472500?e=1795651200&v=beta&t=SFd-yxKi3KGWURsHdanG7T1cKcsEADeVzyank681cQ0)

Figure 1. Correlation plot of Observed versus Calibrated RDII Volume for the simulated events.

The steps in using RDII Analyst are both simple and powerful, the main steps are:

- Import flow monitoring data and rainfall data into RDII Analyst
- Perform QA/QC for the flow data and the rainfall data
- Determine dry day flows and create hourly DWF pattern for weekend and weekdays
- Determine the groundwater flow component of the dry days flows
- Determine RDII flow time series
- Identify RDII events, and perform linear regression analysis on the RDII depth and rainfall depth calculated for each RDII event
- Run Genetic Algorithms based calibration of the RTK hydrograph parameters and review calibration results
- Export the DWF patterns, the GWF time series and the calibrated RTK parameters to InfoSWMM

In this overview of the steps in the remainder of the blog post, you’ll learn how the RDII Analyst tool works in general and what terminology is used to describe each step. This is recommended reading for anyone who is new to RDII Analyst. If you are experienced in RDII decomposition, you can probably just skim it when needed.

## Step 1. Define the Flow and Rainfall Data

The flow and rainfall data are imported by each monitored Node location. The flow and rainfall format are defined along with the monitored data time intervals. The rainfall and flow do not have to be at the same interval or cover exactly the same time period. The Flow Data Tab displays the flow data that has been read from the flow data file. The display consists of the data area showing Date Time and Value field that is read from the data file. The Rainfall Data Tab displays the flow data that has been read from the rainfall data file. The display consists of the data area showing Date Time and Value field that is read from the data file.

![](https://media.licdn.com/dms/image/v2/C5112AQE5J3K6umS5bg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520249956697?e=1795651200&v=beta&t=9h7PXwc9Sq6WJ1i0q-e_W4OkepSyiGcVktl4I0hSfJg)

Figure 2. Imported Flow Data in RDII Analyst

![](https://media.licdn.com/dms/image/v2/C5112AQFi-_xeJN-AsQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520147169306?e=1795651200&v=beta&t=2gGEHt26GarRzUlnxn2tR9oCqWXJcwHQpL8tejYQSTg)

Figure 3. Imported Rainfall Data in RDII Analyst

## Step 2. DWF Extraction

The DWF Mean and Patterns are extracted from the Flow Time Series and the residual is used as the basis of the RTK parameter estimation. The dry day flows identified for weekdays and the weekend are further analyzed to determine hourly DWF patterns that can be used to model DWF in InfoSWMM . The DWF pattern presents average hourly DWF values across all dry days for both weekdays and weekend. The DWF pattern is given both graphically and in report form as shown below. The DWF patterns can be exported to InfoSWMM and are assigned to nodes that contribute flow to the meter location proportional to sewershed area or equally among all nodes.

Once determined, the dry days flows are presented both in report form and in graph form for weekend and for weekdays as shown below. The graph shows average daily flow for each dry day, and upper bound and the lower bounds. The upper bound refers to mean flow of all dry day flows plus standard deviation multiplier \*standard deviation of dry day flows. The lower bound refers to mean flow of all dry day flows minus standard deviation multiplier \*standard deviation of dry day flows. The bounds help the user visually identify outliers and, if necessary, discard those days from further consideration.

![](https://media.licdn.com/dms/image/v2/C5112AQH37TGQjdfGBA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520142727455?e=1795651200&v=beta&t=pVTRVR5_F17QoHhwdAP_E_0Y1a4vuZaEGOniVJXyuPQ)

Figure 4. Define the Methods used in the DWF Extraction.

![](https://media.licdn.com/dms/image/v2/C5112AQE3VrHb3Cpo2A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520249987970?e=1795651200&v=beta&t=LI6itGQKFg8wy6RYhBd7DXKFcH-XZ2CbsMTmqaIR0Z0)

Figure 5. Mean and QA/QC Graph for the DWF Extraction.

![](https://media.licdn.com/dms/image/v2/C5112AQG6_FiVTvcZbg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520147100322?e=1795651200&v=beta&t=sMPNkhc95LkZq5LT98Fb30kUvuMR0UfbvTzhkx3NQBw)

Figure 6. DWF Pattern found by RDII Analyst

![](https://media.licdn.com/dms/image/v2/C5112AQEq9hSPXH629g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520212487389?e=1795651200&v=beta&t=Fhy1k-T9mXDrESoWd9Eguxb1HRCvXMgRUKWlW6EwCok)

Figure 7. Estimated Weekly GroundWater Flow.

## Step 3. Ground Water Base Flow Extraction

The DWF Mean and Patterns are extracted from the Flow Time Series and the residual is used as the basis of the RTK parameter estimation. As part of the DWF Extraction, the GW flow can be estimated and later exported to InfoSWMM and a Time Series (Figure 7). The groundwater flow time series can be exported to InfoSWMM as external inflow and can be assigned to nodes that contribute flow to the meter location proportional to sewershed area or equally among all nodes.

## Step 4. Export DWF Pattern and DWF Means to the Domain in InfoSWMM

Assign DWF Pattern: This tool assigns the hourly DWF patterns developed for weekdays and weekends to InfoSWMM nodes that contribute flow to the monitoring site. The DWF pattern is allocated to the contributing nodes either proportional to sewershed area of each contributing node, or simply equally among all contributing nodes. The user must assign an ID to be used as the weekday and weekend pattern name. The assignment could be limited to nodes in a domain by checking the Assign to Domain Nodes option.

![](https://media.licdn.com/dms/image/v2/C5112AQEfkS1b3ubutg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520211999117?e=1795651200&v=beta&t=G4IUZBV0hlLyht3tZ7I9AGEvS0APpBhxapMh2uBtCG0)

Figure 8. Export Dialog to export the DWF means and DWF patterns to the Node DWF DB Table or the Patterns DB Table in InfoSWMM.

## Step 5. Create the RDIII or Wet Weather Time Series

RDII flow is the difference between the corrected monitoring flow data, and the sum of average hourly DWF pattern and the groundwater flow time series. Once the hourly DWF pattern and the groundwater flow components are identified, the sum of the two components would be subtracted from the corrected flow data to determine the RDII flow component.

![](https://media.licdn.com/dms/image/v2/C5112AQFsoLRQENiGlw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520142418597?e=1795651200&v=beta&t=wlL2xCdK5gSlb8R9W6UUsAnX52ZdUT23VF3vcq--3rg)

Figure 9. The estimated WWF or RDII time series after extraction for the mean DWF and DWF Pattern.

## Step 6. Calibrate the 18 RDII Parameters

One of the objectives of decomposing flow monitoring data into dry weather flow and wet weather flow components is to improve the accuracy of modeling the wet-weather flow component. In *InfoSWMM*, RDII flow is modeled using the RTK method as previously described. The RTK method requires definition of up to 18 parameters. Proper choice of these parameters is crucial for accurate modeling of the RDII flow. Traditionally, RDII UH parameters are assigned using a tedious and inexact trial-and-error process in which the parameters are manually adjusted in an iterative fashion to closely match wet-weather flow data with the RDII flow generated by the simulation model using the assumed RTK parameters. Since there are a vast number of possible combinations of RTK values, evaluating all options this way may not be manageable, and even knowledgeable modelers often fail to obtain good results. *RDII Analyst* uses Genetic Algorithms (GA) optimization to automatically determine the UH parameters that best match the RDII time series generated by the *RDII Analyst* with the RDII flow estimated using *InfoSWMM*,.

The RDII calibration tool is launched using *Analysis* -\> *Calibrate RDII Parameters* or using from tools. Minimum and maximum value for each parameter should be defined using the *RTK Parameters Range* dialog editor.

The calibration tool systematically searches for the best set of parameters that matches the RDII flow simulated by H2OMAP SWMM with RDII time series determined by the decomposition process. The parameter values would be searched within the minimum and the maximum ranges assigned by the user on dialog editor shown above. The model would adjust the nominal parameter values assigned by the user on *H2OMAP SWMM* RDII hydrograph dialog editor (see below) by a randomly selected multiplier within the range assigned for the parameter and chooses the optimal set of adjustments. The *Tributary Area* may be taken from the sewershed area defined in *H2OMAP SWMM*’s Hydrograph page, or the user can directly specify area of the tributary sewersheds. In addition, the user has the option to use sewershed area of the nodes defined in a domain. The *Ensure that R1\>R2\>R3* option ensures that the RDII flow contributed by the first triangle (fast flow contribution) would be higher than contribution of the second triangle (intermediate flow), and contribution of the second triangle would be higher than that of the third triangle (slow flow).

*Domain Node* option is checked, sewershed area of the nodes included in the domain will be considered. Nodes in the domain will not contribute sewershed area. Once the parameters are assigned, hitting the *OK* button would initiate the calibration dialog box (see below).

*Options*: Some Genetic Algorithms (GAs) parameters may be defined using the options page initiated by clicking the *Options* button on the *Calibrate RDII Parameters* dialog box.

*Initial Population*: Represents the number of initial solution candidates considered by the GAs calibrator. Each solution candidate contains a value H2OMAP SWMM the assigned range for each RTK parameters. The higher the *Initial Population,* the better the calibration results would be. However, the calibration process takes more run time as the number of population increases.

*Max. Generation*: Represents the maximum number of iterations required to complete the calibration process. One generation represents running the model for *initial population* number of times, and each simulation represents different solution candidates. The higher the maximum generation, the better the chance of improving the calibration. Again, the improvement comes at the cost of more calibration run time. The calibration process can stop before reaching the maximum generation if there is no improvement in results from generation to generation.

*Mutation Rate*: represents the percentage of solution candidates whose one or more parameter values needs to be randomly altered to inject new and potentially better solution candidates into the search process during each generation. The value must be within zero and one, and typical value is 0.1.

*Calibration Results:* Upon completing the calibration run, the best RTK parameter values would be reported as shown below. The percentage adjustment and then actual parameter values suggested are reported in the last two columns. In addition, graphical comparison of the RDII flow generated by the calibrated parameters and the RDII time series generated by the decomposition process would be provided to visually analyze the calibration results

  

![](https://media.licdn.com/dms/image/v2/C5112AQG5lNnCwaC4qg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520239744105?e=1795651200&v=beta&t=AC3x2o8krAEUB1IUtE1-0zpSA_VGaP2997FYJRrn4RA)

Figure 10. The 18 RTK parameters can be estimated with min and max constraints to find the best fit parameters.

## Step 7. Examine the Calibration Report

The number of trial runs made so far, the maximum number of trials to be made and the best fitness obtained from the trail runs made so far would be shown while the model is running. If there is no significant improvement in the fitness for some time (i.e., from generation to generation), then the calibration process would be stopped. Once the calibration run is completed, the RDII flow simulated by the optimal RTK parameters identified by the calibration process would be compared graphically with the RDII time series obtained from the decomposition process. In addition, the optimal RTK parameters identified by the model would also be presented in table form.

RDII Analyst can further analyze the RDII time series to identify RDII events. Breaking RDII time series into separate events can enable a better understanding of the RDII process and aid in process of calibrating the model. Event definition depends on the values assigned for the inputs given in the *RDII EVENT IDENTIFICATION* dialog box shown below.

*Minimum Rainfall Volume*: represents the minimum rainfall depth that needs to be collected from “continuous” rain to initiate an event. By continuous rain, it means that for two rainfall occurrences to be considered as one event the time interval between the successive rains should not exceed the *interevent time threshold* defined by the user.

*Minimum RDII Flow*: represents the minimum RDII flow that should be generated as the result of the rainfall collected over the duration to accept the occurrence as an event.

*Minimum Length of the Event (hr)*: refers to the minimum length of time that the RDII flow should exceed the *minimum RDII flow* for the occurrence to be accepted as an event.

*Interevent Time Threshold (hr)*: refers to the length of time needed to separate two successive events. If two rainfall occurrences are separated by duration shorter than the *Interevent Time Threshold,* then the two rainfall occurrences are considered as one event.

*Length of Time for Rain to become RDII (hr)*: This input refers to average time span for a rainfall event to start contributing RDII to the collection system. Depending on this input, the RDII event identification algorithm tests if an RDII flow has occurred within the *Length of Time for Rain to become RDII (hr)* after a rainfall event.

*Tributary Area*: This input is used to compute RDII flow depth based on RDII flow volume determined for each event. *RDII Analyst* can use the sewershed area defined in InfoSWMM’s RTK Hydrograph page, or the user can directly specify area of the tributary sewersheds. In addition, the user has the option to use sewershed area of the nodes defined in a domain. If the *Use Domain Node* option is checked, sewershed area of the nodes included in the domain will be considered. Nodes in the domain will not contribute sewershed area.

  

![](https://media.licdn.com/dms/image/v2/C5112AQEpuMGFIHxhlQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520255942423?e=1795651200&v=beta&t=RfpLewZe5yaXlRfoM93-9cA9UEOpTH7LGq1Q8rBaN-A)

Figure 11. A Calibration Graph of the Monitored and Predicted RDII Time Series.

## Step 8. RDII Event Analysis Results

Linear Regression Results: A linear regression equation is developed between the RDII depth and rainfall depth identified for each event. Slope of the regression equation represents the fraction of rainfall depth that enters the sewer system in the form of RDII (i.e., a representative R for all events).

![](https://media.licdn.com/dms/image/v2/C5112AQHC7tmFfD3wxA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520212790428?e=1795651200&v=beta&t=cJ1UMN5MW2ZEcHvc2F_9BYKT5V_ozyLlGeRAK2TKSy4)

Figure 12. Correlation plot of Observed versus Calibrated RDII Volume for the simulated events.

## Step 9. Export the RDII RTK Parameters to InfoSWMM

This function assigns either the RTK parameters determined by the calibration tool or the RDII time series determined by decomposing the flow monitoring data to InfoSWMM nodes that contribute flow to the monitoring site. The RTK parameters could be exported to InfoSWMM and assigned to RDII hydrographs for each contributing node. The time series is assigned to the nodes as external inflow. The RDII time series is allocated to the contributing nodes either proportional to sewershed area of each contributing node, or simply equally among all contributing nodes. The user must provide a name for the Hydrograph and/or the Time Series. The assignment could be limited to nodes in a domain by checking the Assign to Domain Nodes option. Please note that if both the GWF time series and the RDII time series are exported into InfoSWMM, only the time series exported last would be available for use. InfoSWMM takes only one exported external inflow time series at a time.

How the R (rainfall to flow fraction) and the T and K parameters (T\*K or the Base of the Unit Hydrograph) are related usually. There are three R, three T or time parameters and three K parameters as shown in Figure 18.

  

![](https://media.licdn.com/dms/image/v2/C5112AQFCpxfsLKd1GA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520145251351?e=1795651200&v=beta&t=nU4EyINI7T2i2u6EHcYRYptyZRQt2DIb7tph7zW7okk)

Figure 13. The 18 RTK parameters can now be exported back to InfoSWMM and InfoSWMM SA.

![](https://media.licdn.com/dms/image/v2/C5112AQHjmY97WRqcJw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520214554171?e=1795651200&v=beta&t=r5DTIE38SLQ8hNbxXh8wc69-ZHjI5NHQXrK1wycMSX4)

Figure 14. The 18 RTK parameters in the Operations tab of the InfoSWMM Attribute Browser.

  

![](https://media.licdn.com/dms/image/v2/C5112AQEfC174EpsZrQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1520144565826?e=1795651200&v=beta&t=X-mRE0TW2wNhr7j1Q34LsZ0EcScm6tkG9emsBtZlceA)

Figure 15. How the Exported DWF looks in InfoSWMM graphs of lateral flow at nodes

  

![](https://media.licdn.com/dms/image/v2/C5112AQF7IP3dIbEsjg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520168322857?e=1795651200&v=beta&t=6qIxgYGKuqte7AxfeJs4Ty9aGi8OutJCokQRF5ez8Sw)

Figure 16. GA options in RDII Analyst

![](https://media.licdn.com/dms/image/v2/C5112AQH-cJcfrhXS5w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520250705954?e=1795651200&v=beta&t=CtiKr7sficqJgQadADVGQB-cPskNNRa5wQ3wXdTw2v8)

Figure 17. SWMM5 Features in InfoWorks ICM that can be used with the RDII Analyst.

![](https://media.licdn.com/dms/image/v2/C5112AQHqs8arcOMEBA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520041209737?e=1795651200&v=beta&t=cDSkAUMbrBqriwyeBtox_HI6dOFrji5qcJ5XFMpeXQ0)

Figure 18 - New Compare Tool in RDII Analyst 3.0

More from the Press Release https://swmm5.org/2017/06/06/innovyze-releases-rdii-analyst-generation-v14-5-setting-new-standard-for-managing-and-operating-sewer-systems-new-version-fully-supports-sewer-condition-and-rehabilitation-priorities-and-sewer-capaci/

**Innovyze Releases RDII Analyst Generation V14.5,**

**Setting New Standard for Managing and Operating Sewer Systems**

*New Version Fully Supports Sewer Condition and Rehabilitation Priorities and Sewer Capacity Assessment*

**Broomfield, Colorado, USA, June 6, 2017** – Innovyze, a leading global innovator of business analytics software and technologies for smart wet infrastructure, today announced the release of [*RDII Analyst*](http://elink.innovyze.com/c/4/?T=OTE4MTA1MTY%3AMDItYjE3MTU3LTBhZjkyYWFhYjgzZTRjYjViZThlZmQ5NWY2MGVlMjc1%3Acm9iZXJ0LmUuZGlja2luc29uQG13aGdsb2JhbC5jb20%3AbGVhZC0xNGUxMTgyYTkxOWJlNjExOWU2ZjAwNTA1NmEwMDBhNi02YzZlNDcxOWIwNmQ0YzM0OWE4NGFjZDQ3YWRhNDFjMQ%3AZmFsc2U%3AMTE%3A%3AaHR0cDovL3d3dy5pbm5vdnl6ZS5jb20vcHJvZHVjdHMvaW5mb3N3bW0vcmRpaS5hc3B4P19jbGRlZT1jbTlpWlhKMExtVXVaR2xqYTJsdWMyOXVRRzEzYUdkc2IySmhiQzVqYjIwJTNkJnJlY2lwaWVudGlkPWxlYWQtMTRlMTE4MmE5MTliZTYxMTllNmYwMDUwNTZhMDAwYTYtNmM2ZTQ3MTliMDZkNGMzNDlhODRhY2Q0N2FkYTQxYzEmZXNpZD05NDRlMTZkZC03ZjRhLWU3MTEtYTFiZS0wMDUwNTZhMDAwYTY&K=lkdmsQvkwCJn-VDHIF-S5A) (Rainfall-Derived Inflow and Infiltration) Generation V14.5 for [*InfoSWMM*](http://elink.innovyze.com/c/4/?T=OTE4MTA1MTY%3AMDItYjE3MTU3LTBhZjkyYWFhYjgzZTRjYjViZThlZmQ5NWY2MGVlMjc1%3Acm9iZXJ0LmUuZGlja2luc29uQG13aGdsb2JhbC5jb20%3AbGVhZC0xNGUxMTgyYTkxOWJlNjExOWU2ZjAwNTA1NmEwMDBhNi02YzZlNDcxOWIwNmQ0YzM0OWE4NGFjZDQ3YWRhNDFjMQ%3AZmFsc2U%3AMTI%3A%3AaHR0cDovL3d3dy5pbm5vdnl6ZS5jb20vcHJvZHVjdHMvaW5mb3N3bW0vP19jbGRlZT1jbTlpWlhKMExtVXVaR2xqYTJsdWMyOXVRRzEzYUdkc2IySmhiQzVqYjIwJTNkJnJlY2lwaWVudGlkPWxlYWQtMTRlMTE4MmE5MTliZTYxMTllNmYwMDUwNTZhMDAwYTYtNmM2ZTQ3MTliMDZkNGMzNDlhODRhY2Q0N2FkYTQxYzEmZXNpZD05NDRlMTZkZC03ZjRhLWU3MTEtYTFiZS0wMDUwNTZhMDAwYTY&K=v6eZ-2l-KMB8gANva9pcNA) and [*InfoSWMM SA*](http://elink.innovyze.com/c/4/?T=OTE4MTA1MTY%3AMDItYjE3MTU3LTBhZjkyYWFhYjgzZTRjYjViZThlZmQ5NWY2MGVlMjc1%3Acm9iZXJ0LmUuZGlja2luc29uQG13aGdsb2JhbC5jb20%3AbGVhZC0xNGUxMTgyYTkxOWJlNjExOWU2ZjAwNTA1NmEwMDBhNi02YzZlNDcxOWIwNmQ0YzM0OWE4NGFjZDQ3YWRhNDFjMQ%3AZmFsc2U%3AMTM%3A%3AaHR0cDovL3d3dy5pbm5vdnl6ZS5jb20vcHJvZHVjdHMvaW5mb3N3bW1fc2EvP19jbGRlZT1jbTlpWlhKMExtVXVaR2xqYTJsdWMyOXVRRzEzYUdkc2IySmhiQzVqYjIwJTNkJnJlY2lwaWVudGlkPWxlYWQtMTRlMTE4MmE5MTliZTYxMTllNmYwMDUwNTZhMDAwYTYtNmM2ZTQ3MTliMDZkNGMzNDlhODRhY2Q0N2FkYTQxYzEmZXNpZD05NDRlMTZkZC03ZjRhLWU3MTEtYTFiZS0wMDUwNTZhMDAwYTY&K=2-ufPAnlk8n34EqHE1lPZw). The new version delivers both new and expanded functionalities for the quantification of RDII and help capacity analysis and the condition assessment of sewer systems. The release confirms Innovyze’s commitment to giving the world the most complete toolset for managing, operating and sustaining high-performing sewer systems.

Excessive wet weather flow from rainfall-derived manhole and pipe defect inflow and infiltration is a major source of sanitary and combined sewer overflows. Controlling these overflows is vital in reducing risks to public health and protecting the environment from water pollution. Computer modeling plays an important role in determining optimal remedial solutions that reduce RDII; improve system integrity, reliability and performance; and avoid overflows.

The processes for converting rainfall to RDII flow in sanitary sewer systems are very complicated. In addition to rainfall and antecedent moisture conditions, factors in controlling RDII responses include depth to groundwater, depth to bedrock, land slope, number and size of sewer system defects, type of storm drainage system, soil characteristics, and type of sewer backfill. Given this degree of complexity, flow-monitoring data must be combined with mathematical modeling and analytics to provide accurate results. The wastewater flow monitoring data obtained by sewer collection systems consists of dry-weather flow components, ground water flow and eighteen (18) RDII flow components. A crucial step in successfully modeling sewer collection systems is the ability to decompose flow-monitoring data into RDII flow, ground water flow and dry weather flow and its flow patterns (both weekday and weekend).

*RDII Analyst* is significantly superior to the EPA Sanitary Sewer Overflow Analysis and Planning (SSOAP) program. Powered by advanced GA optimization and comprehensive data analytics and scenario management, it is able to quickly and reliably perform these types of advanced flow decomposition data monitoring. V14.5 has been expanded with a simple and interactive visual curve fitting to facilitate determination of the unit hydrograph parameters. R, T, K and associated monthly storage parameters can now be determined by graphically comparing the total RDII hydrographs generated by users’ defined R, T, K parameters with the RDII hydrographs from the monitored data. Numerical comparison of total RDII volume with the sum of volume under each of the unit hydrographs confirms the success of curve fitting. V14.5 has also been expanded to allow:

- Assessment of the given unit hydrograph data on selective month or annual average
- Coverage of the full range of standard unit hydrograph property data during the analysis process
- Comparison graphing of any RDII variables
- Comparison graphing of multiple analysis results to enable users to analyze runs from various sewershed areas

V14.5 also features an enhanced version of the latest USEPA SWMM5 engine with greatly improved performance and capabilities. It enables users to analyze and rank solutions using various statistical methods and provides the ten best (optimal) solution sets for result ranking and selection. It also allows users to conduct multiple runs within an analysis for parameter and criteria evaluation as well as multiple analyses for different sewershed areas and rainfalls within an *RDII-Analyst* project for scenario comparison. Users now have the ability to filter out a period of flow and rainfall data for the RDII analysis, dynamically eliminate any storms/events prior to analysis, and save and load analysis results. These comprehensive capabilities offer an effective means for designing a focused sewer condition assessment program and maximizing the success of field investigation efforts. They also provide an effective means for assessing the post-rehabilitation performance of the sewer system using the pre- and post-sewer capacity analysis.
