# (M) GRIFFITH UNIVERSITY 

## Hybrid three-dimensional modelling for reservoir fluorescent dissolved organic matter risk assessment

## Author

Wang, Xinchen, Zhang, Hong, Bertone, Edoardo, Stewart, Rodney A, Hughes, Sara P

Published
2022

Journal Title
Inland Waters

Version
Accepted Manuscript (AM)
DOI
$10.1080 / 20442041 .2022 .2067464$

## Rights statement

This is an Author's Accepted Manuscript of an article published in Inland Waters, 2022, copyright Taylor \& Francis, available online at: https://doi.org/10.1080/20442041.2022.2067464

## Downloaded from

http://hdl.handle.net/10072/416923

Griffith Research Online
https://research-repository.griffith.edu.au

# Hybrid three-dimensional modelling for reservoir fluorescent dissolved organic matter risk assessment 

Xinchen Wang ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$, Hong Zhang ${ }^{\mathrm{a}, \mathrm{b}, *}$, Edoardo Bertone ${ }^{\mathrm{a}, \mathrm{b}}$, Rodney A. Stewart ${ }^{\mathrm{a}, \mathrm{b}}$ and Sara P. Hughes ${ }^{\mathrm{d}}$<br>${ }^{a}$ School of Engineering and Built Environment, Griffith University, Queensland 4222, Australia;<br>${ }^{\text {b }}$ Cities Research Institute, Griffith University, Queensland 4222, Australia;<br>${ }^{\text {c }}$ College of Water Conservancy and Hydropower Engineering, Hohai University, Nanjing 210098, China;<br>${ }^{\text {d }}$ Catchment Science, Seqwater, 117 Brisbane St., Ipswich, Queensland 4305, Australia<br>*Correspondence: xinchen.wang@alumni.griffithuni.edu.au

ORCID

Xinchen Wang - 0000-0003-0972-2897

Hong Zhang - 0000-0002-2642-5467

Edoardo Bertone - 0000-0002-9980-5268

Rodney A. Stewart - 0000-0002-6013-3505

A coupled data-driven and three-dimensional (3D) process-based fluorescent dissolved organic matter (fDOM) prediction model was developed for a shallow, subtropical Australian reservoir. The extent to which reservoir water volume, inflow and wind conditions affect the fDOM transport dynamics during cyclonic weather events was assessed through scenario analysis and a data-driven Bayesian Network (BN) approach. The analysis shows that (a) inflow plumes are the main sources of fDOM during heavy

rainfall; (b) the concentration of fDOM near the dam wall is related to rainfall intensity; (c) higher reservoir volumes reduce the rate of increase and peak of fDOM concentration during rainfall events; and (d) the degree of fDOM transport to the dam wall was strongly influenced by the prevailing wind direction. A naïve BN was developed for fDOM assessment and displayed a strong sensitivity of the peak fDOM value to rainfall-related characteristics, while the lag time between rainfall event and fDOM peak at the dam wall was highly sensitive to reservoir water volume and wind speed. The developed hybrid modelling approach provides both new information on three-dimensional fDOM transport in reservoirs during extreme weather events through the 3D fDOM model, and an easy to interpret, instantaneous modelling output for treatment operators through the BN modelling component. The latter is an essential addition for water treatment operators, to promptly predict the impacts of extreme weather events and proactively adjust treatment operations, without the computational time burden of a 3D process-based model.

Keywords: Bayesian networks, dissolved organic matter, fluorescence sensors, water quality, water treatment

# 1. Introduction 

Dissolved organic matter (DOM) is an important component of source water and plays an integral role in regional and global carbon cycles. There are two main sources of DOM in lake waters: allochthonous DOM, which is terrestrially derived humic substances in runoff (Shi et al. 2020; Zhou et al. 2020); and allochthonous DOM, which derives from phytoplankton and submerged aquatic vegetation (Zhang et al. 2009; Feng et al. 2022). DOM is an energy source for heterotrophs, affects biogeochemical and ecological processes and alters the bioavailability of metals and organic contaminants (Stewart and Wetzel 1981; Sinsabaugh and Findlay 2003). In addition, DOM is a concern for drinking water treatment, since it causes colour, taste and odour of the water (Lambert and Graham 1995; Worrall and Burt 2010), it can pollute and block membranes and filters in the water treatment plant (Huber 1998), and can lead to the formation of carcinogenic disinfection by-products in the water distribution

The DOM cycle includes chemical, physical and biological reactions, and interactions with internal and external factors. Hydrological processes greatly influence DOM transport in lakes and reservoirs (Li et al. 2016; He et al. 2020; Wang et al. 2021a, 2021b). Longer water residence times enable the mixing of inflow waters and stabilisation of the DOM (Eccles et al. 2019; Zhang et al. 2021). The concentration of DOM generally increases with inflow discharge in reservoirs (Zhou et al. 2016; Wang et al. 2019; Shi et al. 2020). During heavy rainfall, there is not only an increase of inflow discharge but also an increase in terrestrial DOM inputs (Eccles et al. 2021). Thus, inflow conditions are an important factor affecting DOM transport dynamics as it connects pools of organic matter from rivers to lakes via runoff and subsurface flow paths (Stedmon and Markager 2005; Carstea et al. 2020). Wind conditions are also an important driving force affecting reservoir hydrodynamics (Wang et al. 2020; Zhang et al. 2020; Yuan et al. 2021). Many studies (Schindler et al. 1997; Zhang et al. 2007) found that wind speed variations can lead to frequent sediment resuspension, which plays an important role in affecting the variability of total amount of particles and DOM absorption. In summary, in order to understand DOM variations in reservoirs, it is crucial to study and assess the influences of hydrological processes on DOM transport, especially with different water volumes, inflow and wind conditions.

Fluorescent dissolved organic matter (fDOM) refers to the fraction of chromophoric dissolved organic matter (CDOM) that fluoresces. fDOM has been considered a good proxy for dissolved organic carbon (DOC) concentration (Saraceno et al. 2009). Currently, there are optical sensors which can provide a rapid, in-situ measurement of fDOM. Sensors measuring the fluorescent signal of DOM have recently been installed (e.g., integrated in vertical profiling systems) in several reservoirs worldwide, including Australia; thus, providing highfrequency estimations of fDOM in lakes. The high-frequency data supplied by fDOM sensors has already enabled fDOM integration in 3D process-based models (Wang et al. 2021).

However, to the authors' knowledge, there has so far been no attempt to understand the threedimensional (3D) variations of DOM in reservoirs through a time-efficient approach, which can allow operators to promptly assess scenarios based on real-time forecasted weather events, without the computational burden of 3D process-based models. Therefore, to fill this research gap, 3D fDOM variations in Tingalpa Reservoir (Queensland, Australia) are predicted under different hydrological scenarios by running a coupled data-driven and process-based fDOM model, with scenario analysis completed through a data-driven Bayesian Network approach. Predicted fDOM variations in different scenarios and the outputs of the model-based analysis are discussed, with the aim of achieving more effective water management and improvements to fDOM removal. Based on the hypothesis that advection is the main influence on fDOM transport during storm events, this study will answer two questions: 1) How much fDOM is transported into/through the reservoir under different inflow discharge, water level and wind conditions? 2) Can a lag time between the peak rainfall and the peak in fDOM at the dam wall be identified? If so, which hydrometeorological parameters is it more sensitive to?

# 2. Study site 

Tingalpa Reservoir, located in South East Queensland, Australia, is one of the main water supplies to Redland City, with raw water redirected to the Capalaba drinking water treatment plant (WTP). This reservoir has experienced water quality issues, especially with organic matter (Lu et al. 2017) and taste and odour events (Bertone and O’Halloran 2016). Tingalpa Reservoir is a shallow and subtropical reservoir, located in the South East region of Queensland, Australia and extends between $153^{\circ} 9^{\prime} 9^{\prime \prime}$ E to $153^{\circ} 13^{\prime} 49^{\prime \prime}$ E longitude and $27^{\circ}$ $31^{\prime} 27^{\prime \prime}$ S to $27^{\circ} 33^{\prime} 40^{\prime \prime}$ S latitude (Fig. 1). The surface area of the reservoir is approximately 470 hectares, and the catchment area is $87.5 \mathrm{~km}^{2}$. The dam in the Tingalpa Reservoir is called Leslie Harrison Dam (LHD), which is located on the North Eastern side. There are two inflow

creeks: the Tingalpa Creek from the South East, and the Stockyard Creek from the South West. On 1st August 2014, Seqwater (the bulk water supply authority for Southeast Queensland) decided to reduce the reservoir water storage to $1.32 \times 10^{4} \mathrm{ML}$ from the original full supply capacity of $2.48 \times 10^{4} \mathrm{ML}$ for the ongoing safety of the dam. The reservoir bathymetry and monitoring sites are shown in Fig.1.

# 3. Methods 

### 3.1 Data collection

In Tingalpa Reservoir, fDOM was measured using an EXO fDOM Smart Sensor installed in a vertical profiling system (VPS). A VPS consists of a buoy with a set of water quality probes underneath which are winched up and down the water column. The EXO fDOM fluorescencebased Smart Sensor has $365 \pm 5 \mathrm{~nm}$ excitation and $480 \pm 40 \mathrm{~nm}$ emission wavelength to estimate the quantity of fluorescent, humic-like DOM (peak C), and it is reported as relative fluorescence units (RFU) or quinine sulphate units (QSU). As mentioned, the measured fluorescence region is mainly representative of humic DOM, which has been proven to be the dominant DOM during storm events (Nguyen et al. 2010). Historical preliminary data for Tingalpa Reservoir also identified humic, terrestrial DOM to be dominant compared to autochthonous, protein-like DOM which could prevail under dry conditions. Hence, the focus on storm events allows us to model the most likely worst-case scenarios for the water treatment operators.

The VPS installed by Seqwater 500 m from Leslie Harrison Dam does not only detect fDOM but also measures water temperature, pH , turbidity, dissolved oxygen and conductivity. These additional data are critical for real-time compensation of optical interferences on fluorescence fDOM readings (de Oliveira et al. 2018). Moreover, Seqwater monitors DOM-related water

quality through laboratory analysis of monthly manually collected water samples at different stations, including DOC concentration and absorbance at 254 nm . Data from the VPS have been available since the VPS was installed (i.e. 2013), and several types of manual sampling data have been available since 2010. Other parameters from 2013 to 2019 related to weather conditions were collected from the Australian Bureau of Meteorology. The inflow data from 2015 to 2017 for Tingalpa Creek was collected from the Commonwealth Scientific and Industrial Research Organization (CSIRO).

# 3.2 3D fDOM model 

The fDOM model is derived from our previously developed, calibrated and validated 3D coupled data-driven and process-based model for Tingalpa Reservoir (Wang et al. 2021). The fDOM model comprises hydrodynamic, sediment transport and data-driven models. Firstly, the weather conditions, bathymetry and inflow conditions were input to the 3D hydrodynamic and sediment transport model. The model simulates the thermal structure and sediment distribution, and outputs the water temperature and turbidity in 3D. Once the water temperature and turbidity were simulated in three dimensions, the next task was to couple the process-based model with the data-driven model to predict the fDOM. In the data-driven model, the fDOM was predicted with different equations during storm and calm conditions. The outcome of this process was the prediction of fDOM in three dimensions for the entire reservoir. More details can be found in Wang et al. (2021).

The fDOM model was run for the time period from 2015 to 2017 for validation, with 2-minute steps and hourly output frequency. The same boundary condition for the calibration stage was used as the base condition to drive the 3-year simulation. Although the Tingalpa Reservoir is shallow ( 5.3 m mean depth), the water quality is not uniform along the vertical profile. Hence, fDOM, turbidity and other water quality parameters were derived for the entire water column for further analysis (Wang et al. 2021). It must be emphasized that the

focus of this work is on the effect of hydrological factors on Tingalpa's DOM, while largely disregarding biogeochemistry considerations. However, as previously mentioned, fDOM is a proxy for the humic fraction of DOM which is the dominant DOM fraction for Tingalpa Reservoir. As fDOM peaks, historically, occurred during heavy rainfall events, it is safe to assume that focusing on hydrological, rather than biogeochemistry, processes, would allow to understand and predict all the most common and critical DOM-related events and issues related to reservoir management and water treatment plant operations.

# 3.3 Scenarios analysis 

From a hydrological perspective, several factors affect the spatial and temporal distribution of fDOM in a reservoir system, specifically: (a) reservoir water volume; (b) inflow conditions; (c) wind conditions and (d) reservoir water temperature (Wang et al. 2019). High water level enables the mixing of influent waters and maintains DOM quantity (Awad et al. 2016; Eckard et al. 2017). Oppositely, lower water level can lead to shorter water residence times, and promote the environmental consumption of DOM (Curtis and Schindler 1997). Inflow conditions are primary factors driving the DOM variations. During heavy rainfall, discharge of creeks will increase, and DOM will be carried by the creeks' flow into the reservoir. The transfer of water into the lake will bring new DOM into the lake system and increase the lake flushing time (Liu et al. 2014). If the reservoir water level is low, a high inflow would impact DOM levels in the reservoir proportionally more due to lower capacity for dilution. The wind conditions also play an important role in the DOM's cycle. Wind can induce internal waves in the lake system and it can also cause the resuspension of sediments; the resuspension of sediments affects the preservation of DOM through co-precipitation with mineral (e.g., iron) and absorption of CDOM in lake waters and sediments (Lalonde et al. 2012). Strong wind events in a shallow lake can introduce turbulence in the water column, which generates vertical dispersion of the DOM (Caplanne and Laurion 2008; Tundisi and Tundisi 2012);

wind direction will also affect the impact of a strong wind event, since it determines the fetch length. Moreover, reservoir water temperature affects the fDOM distribution, especially in the vertical direction. Due to the temperature gradient, a thermal stratification is generated, and studies show that high hypolimnetic temperature can stimulate the accumulation of dissolved nutrients and mineralization of organic matter at the sediment-water interface (Sondergaard et al. 2003; Zhang et al. 2020). When the turnover occurs, fDOM mixes vertically. For certain lakes, vertical mixing due to air and surface water temperature reduction towards winter is much more likely than that due to wind or rainfall (Bertone et al. 2015a; Bertone et al. 2015b), hence water temperature plays a critical role in understanding fDOM dynamics.

Based on such understanding of critical factors, following consultation with WTP operators, scientists and water treatment experts, different scenarios of interest for reservoir water level, inflow condition and wind condition for Tingalpa Reservoir were proposed. The historical values of inflow conditions during significant heavy rainfall events were varied following predetermined criteria, to check how these changes would affect the fDOM distribution in Tingalpa Reservoir. Two specific extreme weather events were selected, which occurred in Tingalpa Reservoir in the last decade: one was the severe tropical Cyclone (TC) Marcia, from 18 to 26 February 2015; and the other was the ex-tropical Cyclone (Ex-TC) Debbie, which impacted Tingalpa Reservoir during the afternoon and evening of 30 March 2017. The scenarios can be summarized as below:
(1) Three possible variations in inflow from Tingalpa Creek and Stockyard Creek were proposed, including a (a) 20-year Average Recurrence Interval (ARI) event, (b) 50year ARI event and (c) 100-year ARI event assuming all other parameters with values as per during TC Marcia and Ex-TC Debbie. Parameters used for model setup in each ARI event are shown in Table 1. The rainfall intensity for 20-year, 50-year and 100year ARI events was retrieved from data from the Bureau of Meteorology (BoM). The

other key scenario parameters are listed in Table 1(e.g., the boundary conditions of inflow discharges and suspended sediments). Rainfall duration in all ARI events during TC Marcia is 168 hours, instead of 192 hours as it occurred for the actual event; the reason is that the maximum rainfall duration in the ARI reference data is 168 hours. Table 1 shows that the peak inflow discharge and peak suspended sediment concentration (SSC) increased with an increase in rainfall intensity. The rainfall intensity shown in Table 1 is averaged rainfall intensity, and the rainfall intensity inputted in the 3D model follows a Gaussian distribution, i.e. low at the start and end of rainfall scenario and high at the middle of rainfall event.
(2) Four scenarios of reservoir water level were proposed, including $25 \%, 50 \%, 100 \%$ and $200 \%$ storage volume. The $200 \%$ storage volume is the original total reservoir capacity $\left(2.48 \times 10^{4} \mathrm{ML}\right)$. The corresponding water level and water volume in different scenarios are shown in Table 2. In Table 1, scenarios S1A-S6D are defined to fully determine the effects of ARI events and reservoir volume on fDOM in Tingalpa Reservoir. Scenarios S1A-S6A, S1B-S6B, S1C-S6C and S1D-S6D are under 25\%, $50 \%, 100 \%$ and $200 \%$ reservoir volume, respectively.
(3) Twelve scenarios were then defined to assess the effects of the wind speed and wind direction on fDOM transport in Tingalpa Reservoir. The chosen wind directions were from the southwest (SW), northwest (NW), northeast (NE) and southeast (SE), respectively. These four wind directions had longer wind fetches over Tingalpa Reservoir and were the most frequent wind directions in the rainy seasons of the years 2015 and 2017. Each wind direction was tested with three wind speeds ( $0 \mathrm{~km} / \mathrm{h}, 20$

$\mathrm{km} / \mathrm{h}$ and $40 \mathrm{~km} / \mathrm{h}$ ). The wind duration was defined in relation to adopted wind speed: stronger winds persisted for a shorter period while lighter winds persisted for a longer time period in our scenarios. Therefore, $0 \mathrm{~km} / \mathrm{h}, 20 \mathrm{~km} / \mathrm{h}$ and $40 \mathrm{~km} / \mathrm{h}$ wind speeds had corresponding wind durations of 192, 72 and 3 hours, respectively. Two additional scenarios were run to account for further combinations of wind direction, speed and duration. These 14 scenarios in total, were run "during TC Marcia"; hence besides the wind conditions, all other parameters (e.g., inflow conditions, rainfall, water levels and other boundary conditions) were the same as the observed conditions during this extreme event period. The detailed information about the wind conditions in these twelve scenarios is shown in Table 3. These scenarios were run to isolate, and understand, the specific effects of wind speed, direction and duration and as a consequence, those scenarios might seem unrealistic (e.g., constant wind speed/direction for few days). The other simulations described in Table 1 used the observed, variable wind data.

# 3.4 Bayesian Network development 

In order to provide an agile, user-friendly tool which can quickly extract the information from the 3D modelling inputs and outputs, and that can be used to assess new combinations of inputs conditions, a number of naïve Bayesian Networks were developed. A Bayesian Network (BN) can be defined as a probabilistic graphical model, where relationships between variables (nodes) are graphically identified through arcs, which represent direct dependence among those nodes. The mathematical, probabilistic relationships among such nodes are quantified through so called conditional probability tables (CPTs). An arc goes from a parent node to a child node. A naïve BN is a particular type of BN in which one parent node is connected to several child nodes, and such parent node does not depend on any other variable.

While in traditional BNs, the causal relationships among variables are often predefined based on empirical correlations or expert input, in this case all the potential predictors are treated equally, i.e. assuming no knowledge of the system (hence the definition naïve). Normally, assuming that explanatory variables, such as the ones used in this study, are independent would be a strong assumption; for instance, rainfall total, intensity and inflow are typically related. However, in our case for these BNs, our underlying knowledge/data comes from the 3D model outputs rather than historical data; this is because the 3D model, already validated (Wang et al. 2021), relies both on historical data and a process-based understanding of the fDOM behaviour, and therefore there was no need to duplicate the use of prior data/knowledge already used for the 3D model. As a consequence, all these variables were considered independently when running different scenarios, with all prior information coming from 3D model simulations. The main reason for this was to lead to a simpler BN structure with smaller CPTs, meaning that fewer process-based model scenarios needed to be run to properly populate all the combinations of parent nodes' states of the CPTs. Therefore, for the goal of this study, a naïve BN approach was deemed sensible. Since the parent node in this case also represents the target node, several naïve BNs were developed, one per target variable of interest. Specifically, we developed BNs with target variables being (1) peak fDOM value at the dam wall; (2) peak fDOM in the creeks; (3) lag between rainfall occurrence and peak fDOM at the dam wall. As the most important ones for water treatment operators were \#1 (since the dam wall is close to the raw water intake) and \#3 (to understand the buffer time between the rain event and water quality issue), our analysis will focus on those two models. Fig. 2 shows the structure of the naïve BN focusing on the peak fDOM at the dam wall. The same structure and child nodes are present for the other naïve BNs, with the only difference being the target, parent node.

The nodes' discretisation thresholds and the CPTs were derived from a numerical dataset composed of inputs and outputs of 46 simulations of the 3D fDOM model. These simulations, described in other sections of this paper, tested different potential environmental/hydrological scenarios to understand the spatio-temporal fDOM variations in the reservoir. The BNs allow the operators to test the same, or different combinations of, input conditions, to estimate the risk of certain fDOM concentrations, and understand how long it might take, after the rainfall event, to detect those peak concentrations at the dam wall. Importantly, the advantages of (and main reason for) developing these BNs rather than using directly the 3D process-based model, are its user-friendliness, instantaneous prediction and quantification of uncertainty. Sensitivity analysis was also performed for each BN, to understand, overall, which input variables are the most influential.

# 4. Results and Discussion 

### 4.1 fDOM variations under effects of rainfall

Three different ARI events were simulated with the $100 \%$ storage volume, namely 20-year, 50-year and 100-year ARI events over 168 hours from 18 February 2015 to 24 February 2015. These three scenarios are S1C, S2C and S3C. The detailed information about rainfall and inflow conditions in each event are shown in Table 1.

Except for rainfall and inflow, all the othe parameters (such as air temperature and wind), were kept the same as recorded during TC Marcia. Fig. 3 shows the time series of predicted turbidity and fDOM near the dam wall at the depth of 1 m for such different scenarios and fDOM started an increase from 20 February 2015. Simulated turbidity and fDOM peak values at the dam wall in a 100-year ARI event were higher than for simulated 20-year ARI and 50-year ARI events (Fig. 3a). This was in line with previous studies from Bertone and O’Halloran (2016) and Wang et al. (2019). It is also indicated that the lag

between the start of the event and the peak in fDOM and turbidity in the 100-year ARI event was slightly shorter than that in the other ARI events. These results for fDOM simulations are consistent with the results for Ex-TC Debbie as shown in Fig. A1.

To analyse the horizontal distribution of fDOM under heavy rainfall and large inflow discharge, the spatially explicit fDOM results are plotted in Fig. 4 for the simulated 100-year ARI event during TC Marcia with 100\% storage volume (S3C). As displayed in Fig. 4a and Fig. 4b, the main fDOM loading came from the inflow plumes from Tingalpa Creek and Stockyard Creek, with the latter contributing proportionally more. Higher concentrations of fDOM may be transported faster from Stockyard Creek compared to Tingalpa Creek, due to Tingalpa Creek having a less steep topography and a more meandering course, thus fDOM needing more time be transported towards the dam wall. The inflow plumes contained a high concentration of fDOM which spread to the centre and north of the lake during the storm, as shown in Fig. 4c. Subsequently, the fDOM flowing into the reservoir system decreased, and fDOM diluted in the whole reservoir and partially flowed out of the dam. The overall fDOM in the reservoir became steady at the level of 135 RFU at the end of the event: this can be due to the fact that water quality parameters such as DOM, after a big increase (due to e.g., storm or bushfire), can take months to years to return to pre-event concentrations (Wise et al. 2019). As illustrated in outputs from the 3D model, the heavy rainfall scenario showed that the variation of surface fDOM distribution mainly depends on the high concentration of fDOM in inflow plumes and main turbidity in the reservoir is also from inflow plumes, which is in line with modelled results from Chung et al. (2009) and Vijverberg et al. (2011). The overall horizontal fDOM variations are consistent with that in Ex-TC Debbie as shown in Fig. A2,

while the results for the horizontal fDOM distribution during the event (Fig. A2) were different (Fig. 4c). The difference is that following fDOM Ex-TC Debbie, the horizontal fDOM was already uniformly distributed after 3 days (Fig. A2), while it took longer after TC Marcia (i.e., 96 hours), likely due to higher rainfall volume and shorter rainfall duration in ExTC Debbie.

# 4.2 fDOM variations under effects of water level 

To analyse the influence of the initial reservoir water level on the fDOM changes during 20year ARI in the period of TC Marcia, four scenarios (S1A, S1B, S1C and S1D) were established to simulate the fDOM in Tingalpa Reservoir. The simulation results indicated that simulated fDOM near the dam under $25 \%$ reservoir level peaked at the highest level (182 RFU), and the lag between the start of rainfall and peak time was the shortest ( 15 hours). Fig. 5a reveals that higher water levels led to a lower fDOM peak value and extended the lag time between rainfall peak and DOM peak. This is confirmed by other studies (Awad et al. 2016; Liu et al. 2019) that a higher water level, given same inflow/outflow conditions, would cause higher water residence time; hence the fDOM flowing into the reservoir from creeks would have a longer time to stay in the reservoir and dilute. fDOM under full storage volume had different temporal variations between inflow creeks and dam wall. Simulated fDOM reached similar peak levels ( 210 RFU ) in the two creeks. The peak fDOM value near the dam was about $25 \%$ lower than that in the creeks and was recorded 50 hours later than the peak at the creeks.

As illustrated previously, inflow plumes are the main loading of fDOM during heavy rainfall. To understand the effects of both initial water level and inflow creek discharge on the fDOM loading to the reservoir, 12 scenarios with varying water levels in the 20-year ARI

event, the 50-year ARI event and the 100-year ARI event during the TC Marcia period were analysed. Table 4 shows the scenario information and simulating results under these scenarios. T1, T2, T3 in Fig. 5a represent the duration of the fDOM's increase period, fDOM's stable period and its decline period at the dam wall, respectively (Wang et al. 2021). As a consequence, T total, i.e., the sum of T1, T2 and T3, is the total duration of the fDOM event. It can be seen from Scenario 1 and 5 to 9, that with the increase in rainfall and inflow discharge, there was an increase in fDOM peak at both inflow creeks and dam wall. Also, given the same ARI, there were generally longer T1, T2 and T3 and total fDOM event duration under higher initial water levels. Lag times, in turn, were also longer for high water levels conditions, providing a longer buffer for water treatment operators to respond to the extreme event (Saraceno et al. 2009; Liu et al. 2019). It is noted that rainfall between 18 February and 19 February was small and did not lead to an increase of fDOM, so the rainfall in this period was ignored and we defined the start of rainfall as 20 February. Specifically, the lag time between the start time of rainfall and the peak fDOM at the dam wall, as well as between peak fDOM at creeks and peak fDOM near the dam, was less than 20 hours with the $25 \%$ and $50 \%$ initial reservoir volume, but over 80 hours under $100 \%$ and $200 \%$ initial water volume. Conversely, Table 4 also shows that larger inflows, in addition to increasing the concentration of fDOM in the reservoir, shortened lag times between peak fDOM at the creek and at the dam wall for the same water level (e.g., in Scenario 4, 9 and 12 with a high water level). According to the fDOM modelling results in Table A1, it can be seen that the effects of reservoir water levels and inflow discharges on fDOM in TC Marcia are consistent with simulations during Ex-TC Debbie.

# 4.3 fDOM variations under wind influence 

To explore the fDOM sensitivity to the wind conditions, scenarios SI to SXII were run during

TC Marcia in 2015. The simulated results are shown in Fig. 6 and indicate the fDOM increasing period at the dam wall in all wind scenarios was from 20 February to 21 February 2015. The varying tendencies of fDOM with no wind (the blue line) was consistent with fDOM under $40 \mathrm{~km} / \mathrm{h}$ wind speed (the yellow line), which indicates that strong winds, regardless of the wind direction, does not greatly affect the fDOM variations at the dam wall. The reason for this is that the duration of strong wind is shorter, (i.e. 3 hours), hence it seems that the effects of higher wind speed but lower duration cancelled each other. It is noteworthy that the only noticeable variations in peak fDOM compared to no wind conditions were recorded for scenarios with intermediate wind speeds (i.e. $20 \mathrm{~km} / \mathrm{h}$ ) and duration (i.e. 72 h ); from these 4 specific scenarios, based on different wind direction, it can be seen that southwest and southeast winds with $20 \mathrm{~km} / \mathrm{h}$ wind speed and a 72 h duration moved high concentration of fDOM to the dam wall, while the North-Western winds transport more fDOM opposite the dam wall. It is also indicated from previous studies (Caplanne and Laurion 2008; Tundisi and Tundisi 2012) that internal waves induced by winds affected fDOM transport.

A summary of modelling results from SI to SXII is provided in Table 5. The first row in Table 5 shows that the difference of peak fDOM near the dam between each wind scenario was minimal (i.e. $<2 \mathrm{RFU}$ ) at a depth of 1 m . Due to these scenarios occurring under the same rainfall-inflow conditions, the peak fDOM at the inflow creeks was always the same. On the other hand, as discussed, the temporal aspects of the fDOM events were more substantially affected by different wind conditions. Specifically, the modelling results in Table 5 suggested that the wind with $20 \mathrm{~km} / \mathrm{h}$ speed and 72-h duration extended the lag time between the start time of rainfall and the peak fDOM at dam wall and the lag time between peak fDOM at Stockyard Creek and peak fDOM near the dam. It is noteworthy that a wind speed of $20 \mathrm{~km} / \mathrm{h}$ and 72-h duration led to lower average rate of fDOM increase than the other two wind scenarios (i.e. $0 \mathrm{~km} / \mathrm{h}$ wind speeds with 192 h duration and $40 \mathrm{~km} / \mathrm{h}$ wind speeds

with 3 h duration). To summarise, the wind direction affects the fDOM transport to the dam wall, with South-Western and South-Eastern winds promoting greater fDOM transport to the dam wall and North-Western winds preventing it. The average rate of increase of fDOM during the event is instead more closely related to wind speed and duration.

# 4.4 Sensitivity analysis and Bayesian Network application 

Fig. 7 shows the result of the sensitivity analysis for both naïve BNs. Shannon's Mutual information (Shannon and Warren 1949), which is one of the most commonly used metrics to rank information sources, was calculated. In simple terms, it represents the total uncertaintyreducing potential of the predictor in relation to the targeted variable (Pearl 1988), i.e. the larger the mutual information, the larger the uncertainty-reducing potential of that predictor and thus the more sensitive to that predictor the target variable is. It is a nonnegative number, equal to zero when the target and predictor are mutually independent (Gallager 1968). The peak fDOM value is highly sensitive to rainfall/inflow related variables, especially the rainfall amount and the inflow from Tingalpa Creek. On the other hand, the time between the peak rainfall and the peak in fDOM at the dam wall is most sensitive to the reservoir volume, followed by the residence time and the wind speed, affecting mixing process. Rainfall and inflow variables are proportionally less important than for predicting the peak value. Wind directions and duration are overall, the less sensitive variables for both models.

This information can be used by the water treatment operators to understand in advance which environmental/hydrological conditions will be more problematic in terms of potential fDOM events. While the results of the 3D fDOM models provide more detailed information on the overall spatio-temporal fDOM distribution under certain conditions, the BN is much less computationally intensive (simulations are instantaneous) and it can be used

in real-time based on weather forecasts. In addition, unlike the 3D fDOM model, BNs can handle missing data (Uusitalo 2007) and therefore only the values of the available inputs can be entered into the model. For instance, if the weather forecast indicates 350 mm of rainfall over the next 7 days, and the current reservoir volume is low ( $<1.00 \times 10^{4} \mathrm{ML}$ ), the model predicts a risk ( $41.8 \%$ probability) of high ( $>190 \mathrm{RFU}$ ) fDOM, and a reasonable risk ( $22.7 \%$ probability) of a short ( $<50$ hours) lag time occurring. However, if the weather forecast is updated and the same amount of rain is predicted to fall over a longer time period (e.g., 10 days), then the probability of high fDOM decreases to $17.3 \%$, and an intermediate peak value (150-190 RFU) becomes the most probable outcome ( $72 \%$ ). If, at the same time, the wind forecasts indicate a high chance of strong northeast winds persisting for less than 36 hours, then the chance of high fDOM increases slightly from $17.3 \%$ to $21.3 \%$. As more, or updated, evidence becomes available, this can be easily entered in the BNs, allowing water treatment plant operators to take informed decisions based on predicted risks. Translating complex models into user-friendly risk assessment tools that can be easily interpreted by operators facilitates proactive decision making during extreme events (Bertone et al. 2015a; Bertone et al. 2017) and avoids their lack of use (van Delden et al. 2011).

While 3D process-based models for water quality risk predictions (Li and Qin 2019; Zhang et al. 2021) or Bayesian Networks models for water quality risk assessment (Williams and Cole 2013; Bertone et al. 2015; Bertani et al. 2016; Couture et al. 2018) individually exist, to the authors' knowledge, this is the first attempt to create a hybrid model which can take advantage of the comprehensive features of a 3D process-based model, without the computational burden associated to it and with an easy-to-use interface for risk assessment. The modelling approach of this study could be applied to other sites with similar DOM concerns. In Tingalpa Reservoir, advection of inflow plumes is the major driving force of the hydrodynamic process and fDOM transport. If the study site is a deeper monomictic lake, one mixing process per year (thermal stratification in summer and the following winter turnover)

is the main influence factor on the hydrodynamic process and fDOM transport. In this situation, the modelling approach needs to be adjusted to satisfy different lake dynamics. We propose an integrated method, including a naïve Bayesian Network and a coupled data-driven process-based model. To apply this model to other settings, related data (hydrological, meteorological and DOM-related data) needs to be collected, as explained in Wang et al. (2021). Importantly, the current modelling approach relies on using fDOM (with $365 \pm 5 \mathrm{~nm}$ excitation and $480 \pm 40 \mathrm{~nm}$ emission wavelength) as a proxy for the whole DOM; if highfrequency fDOM data is not available for a proposed site, an alternative high-frequency DOM proxy sensor/dataset would be required.

# 5. Conclusion 

In this study new modelling approach was proposed: first, combining data-driven and process-based modelling to achieve a three-dimensional simulation of fDOM in a drinking water reservoir under different extreme event scenarios; secondly, such outputs were then used to develop data-driven BNs which can assess probabilities of certain fDOM peak event features under a wider range of initial conditions. While the 3D fDOM model provides a comprehensive understanding of spatial and temporal fDOM variability during extreme events, the BN inevitably simplifies the modelling to very specific targets of interest. However, while the 3D fDOM model is computationally demanding, the BN is user-friendly and allows water treatment plant operators to use real-time weather forecasts with related uncertainty, to obtain an instantaneous prediction of fDOM-related risk for water treatment operations.

The outputs show that three main driving forces (i.e. reservoir water level, rainfall conditions and wind conditions) influence fDOM transport during storm events at the assessed site. Inflow plumes are the most important fDOM load during heavy rainfall, with

heavier rainfall leading to higher concentrations of fDOM near the dam wall. The outputs also reveal that there would be a higher and earlier peak of fDOM if the reservoir water level was lower. South-western and south-eastern winds promote fDOM transport to the dam wall, while north-western winds prevent fDOM transport towards the dam wall. Wind speed and duration affect the transport time from the creeks to the dam wall. Finally, a clear lag time between rain and fDOM peak exists and is more sensitive to reservoir volume and wind speed.

Overall, this hybrid modelling approach meets the needs of scientists, who are after a better understanding of the three-dimensional behaviour of DOM in reservoirs during extreme rainfall events, and of water managers and operators, who seek a user-friendly, easy to interpret assessment of water quality risks.

# Acknowledgement 

The authors acknowledge DHI Water and Environment, Denmark, for their assistance in providing MIKE modelling system for this study. This research work was conducted with the technical support of Griffith University and Seqwater. The authors acknowledge Jonathan Creamer, Michael Bartkow, Paul Fisher, Rohan Campbell and David Roberts for technical advice.

## Funding

Funding for this project has been provided by Griffith University Postgraduate Research School through the Publication Assistance Scholarship.

## Conflict of Interest

The authors declare that they have no conflict of interest.

# References: 

Awad J, van Leeuwen J, Chow C, Drikas M, Smernik RJ, Chittleborough DJ, Bestland E. 2016. Characterization of dissolved organic matter for prediction of trihalomethane formation potential in surface and subsurface waters. J. Hazard. Mater. 308:430-439.

Bertani I, Obenour DR, Steger CE, Stow CA, Gronewold AD, Scavia D. 2016. Probabilistically assessing the role of nutrient loading in harmful algal bloom formation in western Lake Erie. J. Great Lakes Res. 42(6):1184-1192.

Bertone E, O' Halloran K, Stewart RA, de Oliveira GF. 2017. Medium-term storage volume prediction for optimum reservoir management: A hybrid data-driven approach. J. Cleaner Prod. 154:353-365.

Bertone E, O’Halloran K. 2016. Analysis and modelling of taste and odour events in a shallow subtropical reservoir. Environments. 3(3):22-34.

Bertone E, Stewart RA, Zhang H, Bartkow M, Hacker C. 2015a. An autonomous decision support system for manganese forecasting in subtropical water reservoirs. Environ. Model. Software. 73:133-147.

Bertone E, Stewart RA, Zhang H, O'Halloran K. 2015b. Analysis of the mixing processes in the subtropical Advancetown Lake, Australia. J. Hydrol. 522:67-79.

Caplanne S, Laurion I. 2008. Effect of chromophoric dissolved organic matter on epilimnetic stratification in lakes. Aquat. Sci. 70(2):123-133.

Carstea EM, Popa CL, Baker A, Bridgeman J. 2020. In situ fluorescence measurements of dissolved organic matter: A review. Sci. Total Environ. 699:134361-134285.

Chung SW, Hipsey MR, Imberger J. 2009. Modelling the propagation of turbid density inflows into a stratified lake: Daecheong Reservoir. Korea. Environ. Model. Software. 24(12):1467-1482.

Couture R-M, Moe SJ, Lin Y, Kaste O, Haande S, Lyche Solheim A. 2018. Simulating water quality and ecological status of Lake Vansjo, Norway, under land-use and climate change by linking processoriented models with a Bayesian network. Sci. Total Environ. 621:713-724.

Curtis PJ, Schindler DW. 1997. Hydrologic control of dissolved organic matter in low-order Precambrian Shield lakes. Biogeochemistry. 36(1):125-138.
de Oliveira GF, Bertone E, Stewart RA, Awad J, Holland A, O’Halloran K, Bird S. 2018. Multi-parameter compensation method for accurate in situ fluorescent dissolved organic matter monitoring and properties characterization. Water. 10(9):1146-1158.

Eccles R, Zhang H, Hamilton D. 2019. A review of the effects of climate change on riverine flooding in subtropical and tropical regions. J. Water Clim. Change. 10(4):687-707.

Eccles R, Zhang H, Hamilton D, Trancoso R, Syktus J. 2021. Impacts of climate change on streamflow and floodplain inundation in a coastal subtropical catchment. Adv. Water Resour. 147:103825-103849.

Eckard RS, Pellerin BA, Bergamaschi BA, Bachand PAM, Bachand SM, Spencer RGM, Hernes PJ. 2017. Dissolved organic matter compositional change and biolability during two storm runoff events in a small agricultural watershed. J. Geophys. Res.: Biogeosci. 122(10):2634-2650.

Feng L, Zhang J, Fan J, Wei L, He S, Wu H. 2022. Tracing dissolved organic matter in inflowing rivers of Nansi Lake as a storage reservoir: Implications for water-quality control. Chemosphere. 286:131624-131647.

Gallager RG. 1968. Information theory and reliable communication. New York (NY): Wiley.
He D, Wang K, Pang Y, He C, Li P, Li Y, Xiao S, Shi Q, Sun Y. 2020. Hydrological management constraints on the chemistry of dissolved organic matter in the Three Gorges Reservoir. Water Res. 187:116413116439 .

Huber SA. 1998. Evidence for membrane fouling by specific TOC constituents. Desalination. 119(1-3):229-234.
Lalonde K, Mucci A, Ouellet A, Gélinas Y. 2012. Preservation of organic matter in sediments promoted by iron. Nature. 483(7388):198-200.

Lambert S, Graham N. 1995. Removal of non-specific dissolved organic matter from upland potable water supplies-II. Ozonation and adsorption. Water Res. 29(10):2427-2433.

Li P, Lee S, Lee S, Lee J, Lee Y, Shin H, Hur J. 2016. Seasonal and storm-driven changes in chemical composition of dissolved organic matter: a case study of a reservoir and its forested tributaries. Environ. Sci. Pollut. Res. 23(24):24834-24845.

Li W, Qin B. 2019. Dynamics of spatiotemporal heterogeneity of cyanobacterial blooms in large eutrophic Lake Taihu, China. Hydrobiologia. 833(1):81-93.

Liu J, Li X, Xie Y, Tang H. 2014. Characterization of soluble microbial products as precursors of disinfection byproducts in drinking water supply. Sci. Total Environ. 472:818-824.

Liu W, He W, Wu J, Wu W, Xu F. 2019. Effects of fluorescent dissolved organic matters (FDOMs) on perfluoroalkyl acids (PFAAs) in lake and river water. Sci. Total Environ. 666:598-607.

Lu J, Faggotter SJ, Bunn SE, Burford MA. 2017. Macrophyte beds in a subtropical reservoir shifted from a nutrient sink to a source after drying then rewetting. Freshwat. Biol. 62(5):854-867.

Nguyen H, Hur J, Shin H. 2010. Changes in spectroscopic and molecular weight characteristics of dissolved organic matter in a river during a storm event. Water, Air, Soil Pollut. 212(1-4):395-406.

Pearl J. 1988. Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. Morgan Kaufmann Publishers Inc.

Saraceno JF, Pellerin BA, Downing BD, Boss E, Bachand PAM, Bergamaschi BA. 2009. High-frequency in situ optical measurements during a storm event: Assessing relationships between dissolved organic matter, sediment concentrations, and hydrologic processes. J. Geophys. Res.: Biogeosci. 114:1-11.

Schindler DW, Curtis PJ, Bayley SE, Parker BR, Beaty KG, Stainton MP. 1997. Climate-induced changes in the dissolved organic carbon budgets of boreal lakes. Biogeochemistry. 36(1):9-28.

Shannon CE, Warren W. 1949. The mathematical theory of communication. Urbana: University of Illinois Press.
Shi Y, Zhang L, Li Y, Zhou L, Zhou Y, Zhang Y, Huang C, Li H, Zhu G. 2020. Influence of land use and rainfall on the optical properties of dissolved organic matter in a key drinking water reservoir in China. Sci. Total Environ. 699:134301-134212.

Sinsabaugh RL, Findlay S. 2003. Dissolved organic matter: out of the black box into the mainstream. Aquatic Ecosystems. Burlington: Academic Press; p. 479-498.

Sondergaard M, Jensen JP, Jeppesen E. 2003. Role of sediment and internal loading of phosphorus in shallow lakes. Hydrobiologia. 506(1-3):135-145.

Stedmon CA, Markager S. 2005. Resolving the variability in dissolved organic matter fluorescence in a temperate estuary and its catchment using PARAFAC analysis. Limnol. Oceanogr. 50(2):686-697.

Stewart A, Wetzel R. 1981. Dissolved humic materials: Photodegradation, sediment effects, and reactivity with phosphate and calcium carbonate precipitation. Arch. Hydrobiol. 92(3):265-286.

Tundisi JG, Tundisi TM. 2012. Limnology. CRC Press.
Uusitalo L. 2007. Advantages and challenges of Bayesian networks in environmental modelling. Ecol. Model. 203(3-4):312-318.
van Delden H, Seppelt R, White R, Jakeman AJ. 2011. A methodology for the design and development of integrated models for policy support. Environ. Model. Software. 26(3):266-279.

Vijverberg T, Winterwerp JC, Aarninkhof SGJ, Drost H. 2011. Fine sediment dynamics in a shallow lake and implication for design of hydraulic works. Ocean Dynamics. 61(2):187-202.

Wang K, Li P, He C, Shi Q, He D. 2021a. Density currents affect the vertical evolution of dissolved organic matter chemistry in a large tributary of the Three Gorges Reservoir during the water-level rising period. Water Res. 204:117609-117624.

Wang K, Li P, He C, Shi Q, He D. 2021b. Hydrologic heterogeneity induced variability of dissolved organic matter chemistry among tributaries of the Three Gorges Reservoir. Water Res. 201:117358-117362.

Wang X, Zhang H, Bertone E, Stewart RA, Hughes SP. 2021. Coupled data-driven and process-based model for fluorescent dissolved organic matter prediction in a shallow subtropical reservoir. Environ. Model. Software. 141:105053-105069.

Wang X, Zhang H, Bertone E, Stewart RA, O’Halloran K. 2019. Analysis of the mixing processes in a shallow subtropical reservoir and their effects on dissolved organic matter. Water. 11(4):737-753.

Wang X, Zhang H, Bertone E, Stewart RA, O’Halloran K. 2020. Numerical study of the hydrodynamic and sediment transport process in a subtropical water reservoir: the impacts of storms and winds. Environ. Model. Assess. 25(6):843-860.

Williams BJ, Cole B. 2013. Mining monitored data for decision-making with a Bayesian network model. Ecol. Model. 249:26-36.

Wise JL, Van Horn DJ, Diefendorf AF, Regier PJ, Lowell TV, Dahm CN. 2019. Dissolved organic matter dynamics in storm water runoff in a dryland urban region. Journal of Arid Environments. 165:55-63.

Worrall F, Burt TP. 2010. Has the composition of fluvial DOC changed? Spatiotemporal patterns in the DOCcolor relationship. Global Biogeochem. Cycles. 24(1):1-12.

Yuan S, Tang H, Li K, Xu L, Xiao Y, Gualtieri C, Rennie C, Melville B. 2021. Hydrodynamics, Sediment Transport and Morphological Features at the Confluence Between the Yangtze River and the Poyang Lake. Water Resour. Res. 57(3):1-24.

Zhang F, Zhang H, Bertone E, Stewart R, Lemckert C, Cinque K. 2020. Numerical study of the thermal structure of a stratified temperate monomictic drinking water reservoir. Journal of Hydrology: Regional Studies. 30:100699-100720.

Zhang F, Zhang H, Bertone E, Stewart R, O’Halloran K, Hamilton G, Cinque K. 2021. Integrated modelling and management of manganese for a conventional potable water treatment plant. J. Water Process. Eng. 39:101860-101877.

Zhang F, Zhang H, Bertone E, Stewart R, Shen X, Cinque K. 2021. A three-dimensional manganese model for the management of a monomictic drinking water reservoir. Environ. Model. Software. 146:105213105229 .

Zhang Y, van Dijk MA, Liu M, Zhu G, Qin B. 2009. The contribution of phytoplankton degradation to chromophoric dissolved organic matter (CDOM) in eutrophic shallow lakes: Field and experimental evidence. Water Res. 43(18):4685-4697.

Zhang Y, Zhang B, Wang X, Li J, Feng S, Zhao Q, Liu M, Qin B. 2007. A study of absorption characteristics of chromophoric dissolved organic matter and particles in Lake Taihu, China. Hydrobiologia. 592(1):105120 .

Zhou Y, Liu M, Zhou L, Jang K-S, Xu H, Shi K, Zhu G, Liu M, Deng J, Zhang Y et al. 2020. Rainstorm events shift the molecular composition and export of dissolved organic matter in a large drinking water reservoir in China: High frequency buoys and field observations. Water Res. 187:116471-116489.

Zhou Y, Zhang Y, Jeppesen E, Murphy KR, Shi K, Liu M, Liu X, Zhu G. 2016. Inflow rate-driven changes in the composition and dynamics of chromophoric dissolved organic matter in a large drinking water lake. Water Res. 100:211-221.

# Appendix A 

Figure A1. (a) Simulated turbidity (NTU) and (b) simulated fDOM (RFU) near the dam wall at the depth of 1 m in S4C, S5C and S6C from 29 March 2017 to 11 April 2017.

![img-0.jpeg](img-0.jpeg)

Figure A2. Horizontal fDOM distribution and velocity distribution in the S6C on (a) 29, (b) 30 March, (c) 1 and (d) 11 April 2017.

![img-1.jpeg](img-1.jpeg)

Figure 1. Monitoring sites in the Tingalpa Reservoir and the reservoir's bathymetry [m AHD].

![img-2.jpeg](img-2.jpeg)

Figure 2. Naïve Bayesian Network, parent node = peak fDOM at dam wall, Tingalpa Reservoir.
![img-3.jpeg](img-3.jpeg)

Figure 3. (a) Simulated turbidity and (b) simulated fDOM near the dam wall at the depth of 1 m in 20-year, 50-year and 100-year ARI events from 20 February 2015 to 2 March 2015.

![img-4.jpeg](img-4.jpeg)

Figure 4. Horizontal fDOM distribution and velocity distribution in the S3C on (a) 20, (b) 21, (c) 22 February and (d) 2 March 2015.

![img-5.jpeg](img-5.jpeg)

Figure 5. (a) Hourly simulated fDOM (RFU) at VPS station at the depth of 1 m in different initial conditions ( $25 \%, 50 \%, 100 \%$ and $200 \%$ ) and (b) hourly simulated fDOM (RFU) in Stockyard Creek (SC), in Tingalpa Creek (TC) and near dam with $100 \%$ storage level in 20year ARI event (T1 is the fDOM's growth period; T2 is the fDOM's stable period; T3 is the fDOM's decline period).

![img-6.jpeg](img-6.jpeg)

Figure 6. Hourly simulated fDOM (RFU) at dam wall at the depth of 1 m in SI, SII, SII (a), SIV, SV, SVI (b), SVII, SVIII, SIX (c) and SX, SXI, SXII (d) during TC Marcia in 2015 (Blue lines: Wind speed $=0 \mathrm{~km} / \mathrm{h}$; Orange lines: Wind speed $=20 \mathrm{~km} / \mathrm{h}$; Yellow lines: Wind speed $=40 \mathrm{~km} / \mathrm{h}$ ).

![img-7.jpeg](img-7.jpeg)

Figure 7. Shannon's Mutual information metric for naïve BNs targeting (1) peak fDOM at the dam wall, and (2) lag between rainfall occurrence and peak fDOM at the dam wall.
![img-8.jpeg](img-8.jpeg)

Table 1. Parameters used in model setup for ARI events. S=Scenario. Scenarios letters (A-D) refers to variations in input water level as explained in Table 2.


Table 2. Water volume and water level in different scenario groups in Tingalpa Reservoir.


Table 3. The information about the parameter in different wind scenarios.



Table 4. Modelling results in 12 rainfall and water level scenarios during the TC Marcia period (Lag time ${ }^{1}$ : lag time between the start time of rainfall and the peak fDOM at dam wall; Lag time ${ }^{2}$ : lag time between peak fDOM at creeks and peak fDOM near the dam).


Table 5. Modelling results in wind scenarios (Lag time ${ }^{1}$ : lag time between the start time of rainfall and the peak fDOM at dam wall; Lag time ${ }^{2}$ : lag time between peak fDOM at creeks and peak fDOM near the dam; Average increasing rate: average increasing rate of fDOM at dam wall).



Table A1. Modelling results in 12 scenarios during Ex-TC Debbie period (Lag time ${ }^{1}$ : lag time between the start time of rainfall and the peak fDOM at dam wall; Lag time ${ }^{2}$ : lag time between peak fDOM at creeks and peak fDOM near the dam)


Table A2. Rainfall intensity $(\mathrm{mm} / \mathrm{h})$ for the annual exceedance probability in Tingalpa
Reservoir

