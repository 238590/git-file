# Workflow

Name | Type | Description | Position
--- | --- | --- | ---
Hourly_Irradiation_Plugin | plugin | Plugin to calculate solar irradiation from typical meteorological year data | 0
PEC_Plugin | plugin | Plugin to model photoelectrochemical water splitting | 2
Solar_Concentrator_Plugin | plugin | Plugin to model solar concentration | 2
Multiple_Modules_Plugin | plugin | Modelling of module plant modules, adjustment of labor requirement | 3

# Display Parameters

Name | Value
--- | ---
Name | PEC
Color | darkred

# Technical Operating Parameters and Specifications

Name | Value | Path | Full Name
--- | --- | --- | ---
Operating Capacity Factor (%) | 90.0%
Plant Design Capacity (kg of H2/day) | 1,000
Plant Modules | 10 | None | 10 identical modules, only affects labor requirement calculation.

# Construction

Name | Full Name | Value
--- | --- | ---
capital perc 1st | % of Capital Spent in 1st Year of Construction | 100%

# Hourly Irradiation

Name | Value | Comment
--- | --- | ---
File | pyH2A.Lookup_Tables.Hourly_Irradiation_Data~tmy_34.859_-116.889_2006_2015.csv | Location: Dagget, CA, USA

# Irradiance Area Parameters

Name | Value | Comment
--- | --- | ---
Module Tilt (degrees) | 0 | Two axis tracking, module tilt and array azimuth change are not relevant.
Array Azimuth (degrees) | 0
Nominal Operating Temperature (Celsius) | 45 | Temperature is stabilized even under solar concentration through intrinsic water cooling.
Mismatch Derating | 98%
Dirt Derating | 98% | Values taken from Chang 2020, analogues to silicon PV.
Temperature Coefficient (per Celsius) | 0.0% | No assumed efficiency loss with higher temperature.

# Solar Input

Name | Value | Path | Comment
--- | --- | --- | ---
Mean solar input (kWh/m2/day) | Hourly Irradiation > Mean solar input two axis tracking (kWh/m2/day) > Value | Solar Concentrator > Concentration Factor > Value | Two axis tracking irradiation from hourly irradiation multiplied by solar concentration factor to give solar input incident on PEC cells.

# Solar-to-Hydrogen Efficiency

Name | Value | Comment
--- | --- | ---
STH (%) | 14.0% | Reference Kistler 2020, 14% STH (Note: vapor-fed device used in reference, techno-economic analysis assumes liquid phase design, no solar concentration); alternative reference: Idriss 2020, 18% STH at 15 suns, 13% STH at 200 suns (triple junction III-V cell based system).

# PEC Cells

Name | Value | Comment
--- | --- | ---
Cell Cost ($/m2)| 21,000.0 | Price of III-V solar cells as reference, approximate $/W to $/m2 conversion formula: Cost ($/W) * conversion_efficiency (%) * 1000 W/m2 = Cost ($/m2), Reference: Horowitz 2018 (NREL), 70 $/W, assuming 30% efficiency = 21,000 $/m2.
Lifetime (years) | 0.33 | Should consider operational lifetime (irradiation for only 8 h per day), baseline 1000 h operation time (reference: Kistler 2020), 3000 h total, 0.3 years.
Length (m) | 6 | Based on sizing in Pinaud 2013.
Width (m) | 0.3 | Based on sizing in Pinaud 2013.

# Solar Concentrator

Name | Value | Comment
--- | --- | ---
Concentration Factor | 50 | Concentration factor increased from 10 (Pinaud 2013) to 50 due to high PEC cell cost, within range of typical parabolic trough concentrators, see Gharbi 2011.
Cost ($/m2) | 100 | 100 $/m2 parabolic trough concentrator cost based on Filas 2018.

# Land Area Requirement

Name | Value | Comment
--- | --- | ---
Cell Angle (degree) | 35 | Used for total land area calculation.
South Spacing (m) | 6.71
East/West Spacing (m) | 17.3

# Direct Capital Costs - Water Management

Name | Value | Path | Comment
--- | --- | --- | ---
Water pump ($) | 213.0 | None | Based on Pinaud 2013.
Water Manifold Piping ($ per cell) | 11.58 | PEC Cells > Number > Value
Water Collection Piping ($ per cell) | 1.502 | PEC Cells > Number > Value
Water Column Collection Piping ($ per cell) | 1.1015 | PEC Cells > Number > Value
Water Final Collection Piping ($ per cell) | 0.231 | PEC Cells > Number > Value

# Direct Capital Costs - Gas Processing

Name | Value | Path | Comment
--- | --- | --- | ---
Condenser ($) | 7,098.0 | None | Based on Pinaud 2013.
Manifold Piping ($ per cell) | 11.58 | PEC Cells > Number > Value
Collection Piping ($ per cell) | 1.502 | PEC Cells > Number > Value
Column Collection Piping ($ per cell) | 1.1015 | PEC Cells > Number > Value
Final Collection Piping ($ per cell) | 0.231 | PEC Cells > Number > Value

# Direct Capital Costs - Control System

Name | Path | Value | Comment
--- | --- | --- | --- 
PLC ($) | None | 3,000.0 | Based on Pinaud 2013.
Control Room Building ($) | None | 17,527.0
Control Room Wiring Panel ($) | None | 3,000.0
Computer and Monitor ($) | None | 1,500.0
Labview Software ($) | None | 4,299.0
Water Level Controllers (cost per cell, $) | PEC Cells > Number > Value | 50.0
Pressure Sensors (cost per cell, $) | PEC Cells > Number > Value | 3.333
Hydrogen Area Sensors (cost per cell, $) | PEC Cells > Number > Value | 73.42
Hydrogen Flow Meter ($) | None | 5,500.0
Instrument Wiring (cost per cell, $) | PEC Cells > Number > Value | 0.252
Power Wiring (cost per cell, $) | PEC Cells > Number > Value | 0.1256
Conduit (cost per cell, $) | PEC Cells > Number > Value | 3.759

# Direct Capital Costs - Installation Costs

Name | Path | Value | Comment
--- | --- | --- | ---
Piping Installation (per cell, $) | PEC Cells > Number > Value | 5.65 | Based on Pinaud 2013.
Reactor Installation (per m2 of solar collection area) | Non-Depreciable Capital Costs > Solar Collection Area (m2) > Value | 22.0
Pump Installation (% of pump cost) | Direct Capital Costs - Water Management > Water pump ($) > Value | 30%
Gas processing installation (% of gas processing cost) | Direct Capital Costs - Gas Processing > Summed Total > Value | 30%
Control system installation (% of control system cost) | Direct Capital Costs - Control System > Summed Total > Value | 30%

# Indirect Capital Costs

Name | Path | Value | Comment
--- | --- | --- | ---
Engineering and Design (% of total direct capital costs)| Direct Capital Costs > Total > Value  | 7% | Based on Pinaud 2013.
Process Contingency (% of total direct capital costs) | Direct Capital Costs > Total > Value | 20.0%
Up-Front Permitting Costs (% of total direct capital costs) | Direct Capital Costs > Total > Value | 0.5%
Site Preparation (% of total direct capital costs) | Direct Capital Costs > Total > Value | 1%

# Non-Depreciable Capital Costs

Name | Value | Comment
--- | --- | ---
Cost of land ($ per acre) | 500.0 | Land cost based on Pinaud 2013.

# Fixed Operating Costs

Name | Full Name | Value | Comment
--- | --- | --- | ---
area | Area per staff (m2) | 60,000 | Based on Pinaud et al. 2013, smaller area per staff compared to PV+E and photocatalytic model due to smaller size of individual units, more connections and sensors.
supervisor | Shift supervisor | 1 | Number of shift supervisors.
shifts | Shifts | 3 | Number of shifts per day.
hourly labor cost | Burdened labor cost, including overhead ($ per man-hr) | 50.0

# Other Fixed Operating Costs

Name | Full Name | Path | Value | Comment
--- | --- | --- | --- | ---
g&a | G&A rate (% of labor cost) | Fixed Operating Costs > Labor Cost > Value | 20.0% | Based on Pinaud 2013.
property tax | Property tax and insurance rate (% of total capital investment per year) | Total Capital Costs > Inflated > Value | 2.0%
repairs | Production Maintenance and Repairs (% of direct capital costs) | Direct Capital Costs > Total > Value | 0.5%
fees | Licensing, Permits and Fees ($ per year) | None | 1000.0

# Utilities

Name | Usage per kg H2 | Usage Unit | Cost | Cost Unit | Price Conversion Factor | Price Conversion Factor Unit | Comment
--- | --- | --- | --- | --- | --- | --- | ---
Industrial Electricity | 0.16 | kWh/kg H2 | pyH2A.Lookup_Tables.Utility_Cost~Industrial_Electricity_AEO_2017_Reference_Case.csv | GJ | 0.0036 | GJ/kWh | Electricity usage based on Pinaud 2013.
Process Water | 2.369 | gal/kg H2 | 0.0023749510945008 | $(2016)/gal | 1. | None | Seawater reverse osmosis cost ca. 0.6 $/m3 (equal to ca. 0.0023 $/gal), based on Kibria 2021 and Driess 2021.

# Unplanned Replacement

Name | Full Name | Path | Value | Comment
--- | --- | --- | --- | ---
unplanned replacement | Total Unplanned Replacement Capital Cost Factor (% of total direct depreciable costs/year) | Depreciable Capital Costs > Inflated > Value | 0.5% | Based on Pinaud 2013.

# Sensitivity_Analysis

Parameter | Name | Type | Values
--- | --- | --- | ---
Solar-to-Hydrogen Efficiency > STH (%) > Value | STH efficiency | value | 7%; 28%
PEC Cells > Cell Cost ($/m2) > Value | PEC cell cost (\$/m^{2}) | value | 10,500; 42,000
PEC Cells > Lifetime (years) > Value | PEC cell lifetime (years) | value | 0.15; 0.7
Solar Concentrator > Cost ($/m2) > Value | Solar concentrator cost (\$/m^{2}) | value | 50; 200
Solar Concentrator > Concentration Factor > Value | Solar concentration factor | value | 25; 100

# Methods - Sensitivity_Analysis

Name | Method Name | Arguments
--- | --- | ---
sensitivity_box_plot | sensitivity_box_plot | {'show': False, 'save': False, 'fig_width': 8, 'label_offset': 0.12, 'lim_extra': 0.25, 'right': 0.97}

# Monte_Carlo_Analysis

Name | Value | Comment
--- | --- | ---
Samples | 50000 | Number of samples in Monte Carlo simulation.
Target Price Range ($) | 1.5; 1.6
Input File | ./PEC/Base/Monte_Carlo_Output.csv

# Parameters - Monte_Carlo_Analysis

Parameter | Name | Type | Values | File Index | Comment
--- | --- | --- | --- | --- | ---
Solar-to-Hydrogen Efficiency > STH (%) > Value | STH efficiency | value | Base; 30% | 0 | Practical STH efficiency is the product of solar concentrator efficiency (ca. 76% for state-of-the-art parabolic trough concentrator, see Filas 2018) and PEC STH efficiency (maximum possible STH efficiency ca. 40% for multi junction device based on Hellgardt 2018). Maximum practical STH efficiency therefore estimated to be ca. 30%.
PEC Cells > Cell Cost ($/m2) > Value | \$ / $m^{2}$(PEC cell) | value | 700.0; Base | 1 | 30-fold price reduction for PEC cells analogous to 30-fold reduction of photocatalyst cost in photocatalytic model.
PEC Cells > Lifetime (years) > Value | Cell lifetime (years) | value | Base; 3 | 2 | 9-fold lifetime improvement relative to state of the art (0.33 years).
Solar Concentrator > Concentration Factor > Value | Solar concentration factor | value | Base; 100 | 3 | Doubling solar concentration factor, upper range of parabolic trough concentrators (see Gharbi 2021).

# Cost_Contributions_Analysis - Deactivate

# Methods - Cost_Contributions_Analysis

Name | Method Name | Arguments
--- | --- | ---
cost_breakdown_plot_total | cost_breakdown_plot | {'name': 'Cost_Breakdown_Plot', 'show': False, 'save': False}
cost_breakdown_plot_capital | cost_breakdown_plot | {'name': 'Cost_Breakdown_Plot_Capital', 'show': False, 'save': False, 'plugin': 'Capital_Cost_Plugin', 'plugin_property': 'direct_contributions'}

# Methods - Monte_Carlo_Analysis

Name | Method Name | Arguments
--- | --- | ---
distance_cost_relationship | plot_distance_cost_relationship | Arguments - MC Analysis - distance_cost
distance_histogram | plot_distance_histogram | {'show': False, 'xlabel': True, 'save': False, 'pdf': True, 'image_kwargs': {'path': 'pyH2A.Other~PEC_Clipart.png'}}
colored_scatter | plot_colored_scatter | Arguments - MC Analysis - colored_scatter

# Arguments - MC Analysis - colored_scatter

Name | Value
--- | ---
show | False
save | False
pdf | True
dpi | 500
base_string | Base
title_string | Target cost range: 
plot_kwargs | {'left': 0.34, 'right': 0.97, 'bottom': 0.13, 'top': 0.92, 'fig_width': 6.5, 'fig_height': 4.0}
image_kwargs | {'x': -0.47, 'zoom': 0.09, 'y': 0.5, 'path': 'pyH2A.Other~PEC_Clipart.png'}

# Arguments - MC Analysis - distance_cost

Name | Value
--- | ---
ylim | 20
legend_loc | upper right
log_scale | True
plot_kwargs | {'show': False, 'save': False, 'dpi': 300, 'left': 0.09, 'right': 0.5, 'bottom': 0.15, 'top': 0.95, 'fig_width': 9, 'fig_height': 3.5}
table_kwargs | {'ypos': 0.5, 'xpos': 1.05, 'height': 0.5}
image_kwargs | {'path': 'pyH2A.Other~PEC_Clipart.png', 'x': 1.6, 'zoom': 0.095, 'y': 0.2}
