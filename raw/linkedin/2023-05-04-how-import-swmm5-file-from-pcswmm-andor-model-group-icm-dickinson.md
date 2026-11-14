---
title: "How to Import an SWMM5 file from PCSWMM and/or SWMM5 as a Model Group in ICM InfoWorks and SWMM Networks, Validate it and then Export back to SWMM5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-import-swmm5-file-from-pcswmm-andor-model-group-icm-dickinson
created: "2023-04-28 22:20"
published: "2023-05-04 05:08"
words: 1646
export_sha256: b4653adeb104bc3d5659843aab902df0343dd8b61586806811653e34303fb608
---
# How to Import an SWMM5 file from PCSWMM and/or SWMM5 as a Model Group in ICM InfoWorks and SWMM Networks, Validate it and then Export back to SWMM5

![](https://media.licdn.com/mediaD4E12AQHwqgNY_4Ft3Q)

> SWMM5 Model

The SWMM5 project summary includes the following components: 1 raingage, 168 subcatchments, no aquifers, snowpacks, or RDM hydrographs. The infiltration model used is Horton. There are five junction nodes, six outfall nodes, and no divider nodes. The project features one storage node (1S0), 134 conduit links, and five pump links.

Note of finding the SWMM5 file from PCSWMM - To access the contents of a PCSWMM file, simply change the file extension from .pcz to .zip. Then, extract the files. You should find a \*.inp file within the extracted files, corresponding to an SWMM5 format file.

If you have an SWMM5 file, what are your import options? SWMM5 to either an SWMM or InfoWorks network or SWMM5 to a Model Group in an SWMM network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEpsdU5KBkE2A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682726903912?e=1795651200&v=beta&t=DKU5f9XEDEcHNWckT2HtMJQ8fnOYnIAZLhXARLC3P5U)

If you have an SWMM5 file, what are your import options? SWMM5 to either an SWMM or InfoWorks network or SWMM5 to a Model Group in an SWMM Network.

What engines are in SWMM5? An InfoWorks Sim engine or an SWMM engine in ICM SWMM networks. Currently, SWMM 5.2.3 is the SWMM engine version,

  

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEnmptIAv52MA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1682720530119?e=1795651200&v=beta&t=xyn2pD0P9NYDhxNk8BG55lSxYC37t8MsfbztzEOh4SA)

What engines are in SWMM5? An InfoWorks Sim engine or an SWMM engine in ICM SWMM networks. Currently, SWMM 5.2.3

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEo59AWkcwOtA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1682863543808?e=1795651200&v=beta&t=RLmz31GduKreN-gXKOrjlCgoDs8Rl5WniRxy0-1n278)

User3 Test Model in SWMM4 to SWMM5 and one of the test models for Innovyze.

> Model Descrption

The above model was one of the User Challenge models used in the SWMM4 to SWMM5 development process and documented in the SWMM Dynamic Wave Qa epaswmm5_qa on the EPA download page https://www.epa.gov/water-research/storm-water-management-model-swmm

"The USER3 data set is a combined sewer system containing 168 subcatchments that encompasses an area of 6 square kilometers. The network schematic is shown in Figure 6.13. The system contains 134 pipes which have mostly circular or egg-shaped cross sections. Of the 141 nodes in the network, 6 are outfalls (see Figure 6.14 for a detail drawing) and 130 are manhole or catch basin structures that are represented as small storage units (see Figure 6.15 for a representative profile). There are 5 pumps in the model that discharge directly to the system’s outfalls. The 3-hour, 42 mm design storm used in the simulation is shown in Figure 6.16. This system was analyzed using a 0.5-second routing step, a 1-minute reporting time step, and a 6-hour total duration. The model has metric units."

**Step 1 - Import the SWMM5 as a model group.**

This feature enables the import of all ancillary data, such as rainfall and inflows, for both SWMM and InfoWorks networks. However, only SWMM networks have the capability to import model groups.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFjDtaDZL_WYg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683171709003?e=1795651200&v=beta&t=kG0qjVwTFBk9chUC6guUP_pqzZDVrKtNvqamy-mHsLs)

This feature enables importing all ancillary data, such as rainfall and inflows, for both SWMM and InfoWorks networks. However, only SWMM networks can import model groups.

> **Step 2** - Three possible model group import types.

A model group can be imported from an SWMM5 file for SWMM networks, an XPX file from XPSWMM, or an MXD file from InfoSWMM.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHCh4vJJqq_rw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683171927378?e=1795651200&v=beta&t=CZOPDuz6bt5VPJSM-pZxNsCLTKCtLk7P5ZZpDgQCyGc)

A model group can be imported from an SWMM5 file for SWMM networks, an XPX file from XPSWMM, or an MXD file from InfoSWMM.

> **Step 3** - Import the Model Group

When interpreting this message log, it's important to understand that certain elements are optional, and their absence does not indicate an error. For example, the lack of an inflow time series in the SWMM5 file is simply a note, not an error, as it is not required. Similarly, the absence of an HGL profile in SWMM5, patterns for a stormwater model, a level time series for fixed outfalls, or a pollutograph for water quality modeling are all optional elements. Their absence should be considered informational rather than errors in the model.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFb7t9b523AUA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683172341978?e=1795651200&v=beta&t=4QJwO5edS5YHFNvnnSV7uAFHmRt52DHX4TEVQMeTxo0)

When interpreting this message log, it's essential to understand that certain elements are optional, and their absence does not indicate an error.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHMwni5VZCJkw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683172375168?e=1795651200&v=beta&t=AiPwMg-wU-GlEqw347PUkkRMPxu04DwwDMu2ptyLrpk)

Imported SWMM Network.

> **Step 5** - Validate the imported network.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGPYNcvmzAoCA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683173589371?e=1795651200&v=beta&t=MTnqiO3-HkpVtM9BUA9JvXpJmPSm8yMPASxlTXJIjFc)

The validated Network has no errors, so it can be committed.

> **Step 6** - Check the Ancillary data such as rainfall

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D5612AQFcwPjXE605jg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683040033533?e=1795651200&v=beta&t=z_h02DQBFlOAjBtND5jSAGjn4kAkZsRNmPxHlNGxI7w)

SWMM5 rainfall in mm/hr matches the ICM SWMM Imported data in mm/hr

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D5612AQH7udJZwVsdBA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1683040051345?e=1795651200&v=beta&t=5uwpwkzWU9B2cSFpBAAAneen34Z1svX78fDxGTismhw)

The ICM SWMM Model Group Rainfall data matches the SWMM5 rainfall in mm/hr

> **Step 7** - Add the committed SWMM network to the Run and perform the simulation

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFF-bGAuVMHOQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683173949997?e=1795651200&v=beta&t=__Ng7wt2A9RFR32spZTKQHouEjQaXY3hAna53G430qo)

Add the committed SWMM network to the Run and perform the simulation

> **Step 8** - Check the RPT file from the ICM SWMM run - does the mass balance match?

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D5612AQEqIIQ5AAQFVQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683039954041?e=1795651200&v=beta&t=3fhyfwvoSwxcFb7ihh3s6wRjFxeFXDAkNFLUKdgawC8)

ICM SWMM on the left matches SWMM 5.2.3 on the Right in the hydrology and hydraulics mass balance Tables.

> **Step 9** - Convert the ICM SWMM Network to ICM InfoWorks

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQF0SLrlxjsf4A/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1683175829241?e=1795651200&v=beta&t=l4NF7ELcW0KoKOJOeN7fYX0y1IxSahNMt76-KvVcWTM)

Network Menu tool for converting from SWMM to InfoWorks internally in ICM.

> **Step 10** - Validate the new InfoWorks network data

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQECV317bVtd_Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683176030647?e=1795651200&v=beta&t=-EFlD0p84rkDX-WoPbYlf2qDH18-eigJ8cfw54xXaJg)

Numerous validation errors are present in the model; however, these issues can be resolved by removing the flap gates on the outfalls. Once the flap gates are deleted, the model should pass the validation process without any further errors.

> **Step 11** - Setup flow survey data from SWMM5

Once the flow survey data from SWMM5 is made we can compare ICM SWMM and InfoWorks to the SWMM5 results - they are very close for this example model.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFaMSVuQYnx3Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1683176236406?e=1795651200&v=beta&t=REcIFJYwjAQRVCsjPbGBdk3SL-V7DQY7M5_XcA7-G7w)

Once the flow survey data from SWMM5 is made we can compare ICM SWMM and InfoWorks to the SWMM5 results

> **Step 12** - Export the WHOLE SWMM5 model to SWMM5 from ICM SWMM.

To consolidate the model group data into a single file, you need to perform an export from the "RUN" stage. This process will gather all necessary data, including input parameters, simulation settings, and model components, and combine them into one comprehensive file. Exporting from the "RUN" stage ensures that all relevant information is included, making it easier to share, review, or modify the model as needed.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQF3QsAVN6mUuQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683175439026?e=1795651200&v=beta&t=_Py__IXZQf272IS-FxuRnmU-XTJd4ocCAY5GqtwcxLo)

To consolidate the model group data into a single file, you need to perform an export from the "RUN" stage.

  

> **Step 13** - Check if the exported SWMM5 file can be loaded in SWMM 5.2.3

It is possible to run a model with added ICM SWMM data sections; however, you may encounter warning messages. SWMM5 will ignore these additional data sections, so the model can still be executed despite the presence of warnings.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFdOR3EUngzpA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683175188680?e=1795651200&v=beta&t=gUGBvc0VJD85h4DZK6BQiEWSn-ReljukaW9g-BE1VVg)

SWMM5 will ignore these additional data sections, so the model can still be executed despite the presence of warnings.

> **Step 14** - exported SWMM5 file runs right away with the same mass balance as ICM SWMM.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHeU9sfmLAlvg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683175022318?e=1795651200&v=beta&t=BTnh5fWHENy3rnO2UiUWtle7kVGXw2bp2N892Z7lcWM)

Exported SWMM5 file runs immediately with the same mass balance as ICM SWMM.

The end or to be continued?
