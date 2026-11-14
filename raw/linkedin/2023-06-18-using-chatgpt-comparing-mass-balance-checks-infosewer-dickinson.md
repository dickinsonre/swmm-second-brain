---
title: "Using ChatGPT for comparing Mass Balance Checks in InfoSewer, InfoSWMM, SWMM5, and ICM SWMM against ICM InfoWorks Networks' PRN File"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-chatgpt-comparing-mass-balance-checks-infosewer-dickinson
created: "2023-06-18 19:09"
published: "2023-06-18 21:14"
words: 1595
export_sha256: 791a3b344851e7083cfdac871c6f2b7f24827fc8da7b1cfe8833462dbf142831
---
# Using ChatGPT for comparing Mass Balance Checks in InfoSewer, InfoSWMM, SWMM5, and ICM SWMM against ICM InfoWorks Networks' PRN File

![](https://media.licdn.com/mediaD4E12AQG8uFVxNnZ2vA)

### Using ChatGPT for comparing Mass Balance Checks in InfoSewer, InfoSWMM, SWMM5, and ICM SWMM against the ICM InfoWorks Networks' PRN File

When comparing the text mass balances in SWMM5 and InfoSewer to the Mass Balance in the ICM InfoWork PRN file, a few potential issues may arise:

1.  A different number of rows: Each software may report data in a different format and level of detail. For instance, the PRN file does not explicitly show the infiltration and evaporation totals or break out the total inflow row into WWF and DWF components.
2.  Less detail in the PRN file: The PRN file from ICM InfoWorks may contain less detailed information compared to the output from SWMM5 or InfoSewer. This could mean that certain specific details about the system's performance (like inflow or outflow rates at specific points in the system) might not be directly comparable.
3.  Different units in the PRN file: If the PRN file uses different units of measurement compared to SWMM5 or InfoSewer, the direct comparison of values becomes complicated. Any comparison would first require unit conversion to ensure that the same aspects of system performance are being compared.

The key reason to conduct this comparison is to have a quick and interactive check of the overall mass balance in models converted to **ICM InfoWorks**. This is important to ensure that the conversion of the model from one software to another has not introduced significant errors or discrepancies. This comparison can help identify potential issues early in the process, and ensure that the converted model accurately represents the system's behavior.

It's also essential to understand that while these checks can provide a valuable sanity check, they won't catch every possible error or discrepancy. Detailed validation and calibration of the converted model will still be necessary to ensure its accuracy.

> **1/** How Can ChatGPT help in this effort? InfoSewer Example

InfoSewer has a mass balance table at the end of the report file. Here is an example. For a converted InfoSewer to an ICM InfoWorks network, it would help to have the same units for a basic QA/QC check.

```
[Mass Balance Calculation - InfoSewer

Total external inflow:                 4928127.935 (cubic feet)
Total storm inflow (part of external inflow):       392040.000 (cubic feet)
Total extern outflow:                  4729419.551 (cubic feet)
Total flooding out of open conduits:                 0.000 (cubic feet)
Initial Wet Well Storage:                  678.584 (cubic feet)
Final Wet Well Storage:                   1464.475 (cubic feet)
Wet Well Flooding Volume:               181094.338 (cubic feet)
Init Gravity Main Storage:                   0.000 (cubic feet)
Final Gravity Main Storage:                    837.958 (cubic feet)
Mass Balance Check:                          0.324 (%) 
```

ChatGPT prompt - "Convert the following to cubic meters and hectare m with the same rows but adding m3 and hectare-m as columns" Next is the ChatGPT output. Now I have my mass balance in the original cubic feet but also in m3 for ICM and ha-m or hectare meters for ICM SWMM and SWMM5.

```
Sure, here's the updated response with the calculated values included on the same row as cubic feet

[Mass Balance Calculation]

Total external inflow: 4928127.935 (cubic feet) -> 139314.431 m³ / 13.9314 ha-m
Total storm inflow (part of external inflow): 392040.000 (cubic feet) -> 11103.817 m³ / 1.1104 ha-m
Total extern outflow: 4729419.551 (cubic feet) -> 133867.914 m³ / 13.3867 ha-m
Total flooding out of open conduits: 0.000 (cubic feet) -> 0.000 m³ / 0.000 ha-m
Initial Wet Well Storage: 678.584 (cubic feet) -> 19.218 m³ / 0.0019 ha-m
Final Wet Well Storage: 1464.475 (cubic feet) -> 41.447 m³ / 0.0041 ha-m
Wet Well Flooding Volume: 181094.338 (cubic feet) -> 5122.456 m³ / 0.5122 ha-m
Init Gravity Main Storage: 0.000 (cubic feet) -> 0.000 m³ / 0.000 ha-m
Final Gravity Main Storage: 837.958 (cubic feet) -> 23.722 m³ / 0.0024 ha-m
Mass Balance Check: 0.324 (%):
```

> **2/** How Can ChatGPT help in this effort? ICM SWMM Example

The classic SWMM5 Continuity Tables as made by an ICM SWMM Network. We are doing this to compare ICM InfoWorks to ICM SWMM.

```
  **************************        Volume         Dept
  Runoff Quantity Continuity     hectare-m            mm
  **************************     ---------       -------
  Total Precipitation ......         0.160        26.704
  Evaporation Loss .........         0.000         0.000
  Infiltration Loss ........         0.057         9.434
  Surface Runoff ...........         0.103        17.151
  Final Storage (Surface) ..         0.001         0.233
  Continuity Error (%) .....        -0.431
  
  
  **************************        Volume        Volume
  Flow Routing Continuity        hectare-m      10^6 ltr
  **************************     ---------     ---------
  Dry Weather Inflow .......         0.000         0.000
  Wet Weather Inflow .......         0.103         1.029
  Groundwater Inflow .......         0.000         0.000
  RDII Inflow ..............         0.000         0.000
  External Inflow ..........         0.000         0.000
  External Outflow .........         0.103         1.029
  Flooding Loss ............         0.000         0.000
  Evaporation Loss .........         0.000         0.000
  Exfiltration Loss ........         0.000         0.000
  Initial Stored Volume ....         0.000         0.000
  Final Stored Volume ......         0.000         0.000
  Continuity Error (%) .....        -0.006
```

ChatGPT prompt - "Convert this to m3 instead of hectare-m and add a row with the units of cubic feet but keep the same number of rows" Following the prompt is the mass balance table.

```
 I'll perform the calculations in the response text instead

Here are the converted values:

Runoff Quantity Continuity
Units: m³ and ft³

Total Precipitation: 1600 m³, 56549.6 ft³
Evaporation Loss: 0 m³, 0 ft³
Infiltration Loss: 570 m³, 20129.8 ft³
Surface Runoff: 1030 m³, 36364.2 ft³
Final Storage (Surface): 10 m³, 353.1 ft³
Continuity Error (%): -0.431 (no unit conversion necessary)

Flow Routing Continuity
Units: m³ and ft³

Dry Weather Inflow: 0 m³, 0 ft³
Wet Weather Inflow: 1030 m³, 36364.2 ft³
Groundwater Inflow: 0 m³, 0 ft³
RDII Inflow: 0 m³, 0 ft³
External Inflow: 0 m³, 0 ft³
External Outflow: 1030 m³, 36364.2 ft³
Flooding Loss: 0 m³, 0 ft³
Evaporation Loss: 0 m³, 0 ft³
Exfiltration Loss: 0 m³, 0 ft³
Initial Stored Volume: 0 m³, 0 ft³
Final Stored Volume: 0 m³, 0 ft³
Continuity Error (%): -0.006 (no unit conversion necessary)

Please note that these conversions from hectare-meters and million liters to cubic meters (m³) and cubic feet (ft³) are approximations. The exact conversions may vary slightly due to rounding..
```

> **3/** How Can ChatGPT help in this effort? ICM InfoWorks Example

Original PRN File. The goal is to change the units for comparison to ICM SWMM and add more rows for comparing total infiltration and total dry weather flow (DWF). We will use ChatGPT with iterations. Ask questions and add to the prompt.

```
 Total rainfall   =     463.3 m3
 Total runoff     =     294.6 m3
 Total inflow     =   86694.6 m3
 Total outflow    =   33355.8 m3
 Total lost       =   53338.9 m3
```

ChatGPT prompt - "Convert this to hectare-m and add a new row called Total Infiltration as Total Rainfall - Total Runoff " Following the prompt is the mass balance table.

```
To convert the volume from cubic meters (m³) to hectare-meters (ha·m), you can multiply by the conversion factor of 0.0001 (since 1 m³ = 0.0001 ha·m)

Let's apply this conversion to the given values:

Total rainfall = 1602.2 m³ * 0.0001 = 0.16022 ha·m
Total runoff = 1032.3 m³ * 0.0001 = 0.10323 ha·m
Total inflow = 1032.3 m³ * 0.0001 = 0.10323 ha·m
Total outflow = 1032.2 m³ * 0.0001 = 0.10322 ha·m
Total lost = 0 m³ * 0.0001 = 0 ha·m

To calculate Total Infiltration, subtract the Total Runoff from Total Rainfall:

Total Infiltration = Total Rainfall - Total Runoff = 0.16022 ha·m - 0.10323 ha·m = 0.05699 ha·m

So the converted and updated data would be:

Total rainfall = 0.16022 ha·m
Total runoff = 0.10323 ha·m
Total inflow = 0.10323 ha·m
Total outflow = 0.10322 ha·m
Total lost = 0 ha·m
Total Infiltration = 0.05699 ha·m

Please note that all these values are rounded to five decimal places..
```

Now add the DWF Row by adding a new Prompt "Add a row called Total DWF as Total Inflow - Total Runoff"

```
To convert cubic meters to hectare-meters, you divide by 10,000

Total rainfall = 463.3 m³ = 0.04633 ha-m
Total runoff = 294.6 m³ = 0.02946 ha-m
Total inflow = 86694.6 m³ = 8.66946 ha-m
Total outflow = 33355.8 m³ = 3.33558 ha-m
Total lost = 53338.9 m³ = 5.33389 ha-m

The total infiltration can be calculated as the total rainfall minus the total runoff:

Total Infiltration = Total Rainfall - Total Runoff = 0.04633 ha-m - 0.02946 ha-m = 0.01687 ha-m

The total DWF can be calculated as the total inflow minus the total runoff:

Total DWF = Total Inflow - Total Runoff = 8.66946 ha-m - 0.02946 ha-m = 8.64 ha-m

So, the updated data in hectare-meters would be:

Total rainfall = 0.04633 ha-m
Total runoff = 0.02946 ha-m
Total inflow = 8.66946 ha-m
Total outflow = 3.33558 ha-m
Total lost = 5.33389 ha-m
Total Infiltration = 0.01687 ha-m
Total DWF = 8.64 ha-m:
```

> **4/** Summary of our use of ChatGPT

We now have a straightforward method for doing the following in an iterative manner: compare the mass balance tables in InfoSewer, InfoSWMM, SWMM5, and ICM SWMM to those in ICM InfoWorks by creating common units for comparison. In addition, we added new Rows to the PRN file Mass Balance of ICM InfoWorks in order to make it more comparable to SWMM5 for the purpose of doing more in-depth comparisons.
