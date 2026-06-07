# Development of Generic Tools for Coastal Early Warning and Decision Support 

Tom Bogaard ${ }^{1, a}$, Simone De Kleermaeker ${ }^{1}$, Wiebke S. Jaeger ${ }^{2}$ and Ap van Dongeren ${ }^{1}$<br>${ }^{1}$ Deltares, Delft, The Netherlands<br>${ }^{2}$ Delft University of Technology, Delft, The Netherlands


#### Abstract

Recent and historic high-impact events demonstrated coastal risk (Xynthia, Europe, 2010; Katrina, USA, 2005). This is only to get worse, because risk is increasing due to increase in both hazard intensity, frequency and increase in consequences (increased coastal development). Adaptation requires a re-evaluation of coastal disaster risk reduction (DRR) strategies and a new mix of prevention, mitigation (e.g. limiting construction in flood-prone areas) and preparedness (e.g. Early warning systems, EWS) measures. Within the EU funded project RISC-KIT the focus is on preparedness measures and its aim is to demonstrate robustness and applicability of coastal EWS (Early Warning Systems) and DSS (Decision Support Systems). Delft-FEWS, a generic tool for Early Warning Systems has been extended, to be applied at sites all across Europe. The challenges for developing a modern EWS are found in the integration of large data sets, specialised modules to process the data, and open interfaces to allow easy integration of existing modelling capacities. In response to these challenges, Delft-FEWS provides a state of the art EWS framework, which is highly customizable to the specific requirements of an individual organisation. For ten case study sites on all EU regional seas a EWS has been developed, to provide real-time (short-term) forecasts and early warnings. The EWS component is a 2D model framework of hydro-meteo and morphological models which computes hazard intensities. The total expected impact of a hazard can be obtained by using a Bayesian network DSS. This DSS, which is incorporated in the Delft-FEWS platform is a tool that links coastal multi-hazards to their socioeconomic and environmental consequences. An important innovation of the EWS/DSS lies in its application in dual mode: as a forecast and warning system and as a consistent ex-ante planning tool to evaluate the long-term vulnerability due to multiple (low-frequency) coastal hazards, under various climate-related scenarios. Generic tools which can be used to set-up a EWS/DSS for coastal regions regardless of geomorphic settings, forcing or hazard type have been developed and are available via the project website.


## 1 Introduction

Recent and historic high-impact events demonstrated coastal risk in Europe (Xynthia, France, 2010; Katrina, USA, 2005; Liguria Flash Floods, Italy 2011, North Sea Storm Surge, Europe 1953). Outside Europe similar and even more severe flooding and inundation events demonstrated their significant impact (Typhoon Haiyan, Philippines, 2013; Hurricanes in the Caribbean and Gulf of Mexico, Super storm Sandy, U.S.A, 2012). These events may cause severe economic damage to coastal regions, have high socio-economic impact and may even lead to loss of life.

This is only to get worse, because risk is increasing due to increase in hazard intensity, frequency and increase in consequences, i.e. increased coastal development (IPPC, AR5). The above requires a re-evaluation of coastal disaster risk reduction (DRR) strategies and a new mix of prevention (e.g. protection measures), mitigation (e.g. limiting construction in exposed areas; eco-system based solutions) and preparedness (e.g. Early Warning Systems, EWS) measures.

Even without a change in risk due to climate or socioeconomic changes, re-evaluation is required considering a growing appreciation of ecological and natural values which drive ecosystem-based or nature-based flood defense approaches. In addition, as free space is
becoming sparse, coastal DRR plans need to be spatially efficient, allowing for multi-functionality.

## 2 RISC-KIT project

In response to challenges mentioned in paragraph 1, the EU-funded RISC-KIT research project (2013-2017), as described on the project website (RISC-KIT, 2015), aims to deliver a set of open-source and open-access methods, tools and management approaches to reduce risk and increase resilience to low-frequency, high-impact hydrometeorological events in the coastal zone. These products will enhance forecasting, prediction and early warning capabilities, improve the assessment of long-term coastal risk and optimize the mix of preparedness measures.
One specific objective is the development of a generic impact-oriented Early Warning platform and Decision Support System (EWS/DSS). This generic platform is available for all 11 case study sites in Europe (figure 1). Whereas the focus of this project is on generic tools, a site specific configuration of this platform is required (paragraph 3). The system consists of:

- a free-ware system to predict hazard intensities using coupled hydro-meteo and morphological models and;
- a Decision Support System (DSS) which integrates hazards and socio-economic and environmental consequences.

[^0]
[^0]:    ${ }^{a}$ Corresponding author: tom.bogaard@deltares.nl

![img-0.jpeg](img-0.jpeg)

**Figure 1.** 11 Locations of coastal case study sites in Europe


**Table 1.** Geomorphological setting of case study sites.

In the next paragraphs, both development of EWS and DSS will be explained.

# **3 Operational Forecasting and DSS**

In response to high-impact hydro-meteorological events in the coastal zone, the focus is on increasing preparedness. A possible approach to increase preparedness is to have a reliable Early Warning System (EWS) in place to support accurate and timely early warning. Whereas this EWS (paragraph 3.1) is a tool which can be used by forecasters to issue alerts to a Decision Support System (DSS) (paragraph 3.2) will be developed to assist local authorities in decision making.

### 3.1 Operational Forecasting

For the RISC-KIT project, 11 case study sites are identified throughout the European coast. These coasts have very specific geomorphological settings and are exposed to different types of hazards. Consequently, the operational forecasting system to be developed has to be site specific.

The goal of the RISC-KIT project is to develop a set of generic tools which can be used for all case study sites (and in principal any other coastal region). In order to be site specific, these generic tools will be configured to match site specific requirements.

These generic tools will be based on the Delft-FEWS software [4]. This open data handling platform is specifically designed to configure robust and reliable forecasting systems. Since its release many Delft-FEWS-based EWS related to inland flooding have been developed. However, limited EWS related to coastal threads are implemented using Delft-FEWS. During the RISC-KIT project, this platform has been extended with functionality to serve coastal early warning systems. In paragraph 4, these are extensions discussed in detail.

The Delft-FEWS platform is a highly flexible workflow manager which can be configured to: import and visualize (hydro/meteo) data, run model simulations, validate data in real time, etc. The figure below shows the (for this study) most relevant modules of the software, for a full comprehensive overview reference is made to [4]:

- **Data**: Import modules (have to be configured according to data type)
- **General Adapter**: Generic adapter, to be configured in order to run an external model (numerical/Bayesian etc.). This GA requires a model-specific adapter.
- **Model Adapter**: Model-specific adapter to be called from GA.
- **Data Eport**: Modules (required output i.e. NetCDF, html, csv, etc.)

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Delft-FEWS connection to external models.

### 3.2 Decision Support Systems

A well-developed early-warning system will support accurate and timely information concerning hydrodynamic/meteorological conditions. This in itself may not suffice for decision making in crisis situations. Model-related output needs to be translated to actual

impact in order to support decision making. Part of the RISC-KIT project is to develop a Decision Support System (DSS) and incorporate this with the EWS (paragraph 3.1).

The developed DSS is based on a Bayesian network. For every hazard type (surge, overtopping etc.) and corresponding hazard intensity, attributes (density, sensitivity and value) of every receptor type are defined. Consequently, using the Bayesian DSS, the total expected impact can be obtained. As such, the DSS is a homogenous tool that links coastal multi-hazards to their socio-economic and environmental consequences. It is a model based on data that combines information on the topography and assets of hotspots with simulation results of different storm scenarios and impact estimations from vulnerability relationships, e.g. depth damage curves. The Bayesian network can be run as part of the model train in the EWS (paragraph 4).

## 4 Delft-FEWS extensions for coastal applications

Although the EWS will be site specific, the hydro/meteo model framework for most case study sites shows similarities. The forecasting cycle starts with Numerical Weather Predictions (NWP) and ocean conditions at coarse scale. Whereas limited NWP and forecasted ocean conditions products from national/regional authorities are available most systems make use of global models (i.e. NOAA GFS / Wave Watch III).

These conditions are used to force local hydrodynamic / wave models. In this study Delft-3D, SelfeWWMII, Telemac, Wave Watch III and SWAN models are used. In addition to the global models these regional models provide near shore conditions. For most case study sites an additional modeling step is required to derive actual on shore effects (wave run-up, overwash etc.). This can be achieved by running x-beach. This Open- Source modeling package is used to model hydrodynamic and morphological coastal conditions at a very refined scale.

In the flowchart below the forecast cycle applicable to most case study sites is shown.

![img-2.jpeg](img-2.jpeg)

This workflow cycle runs with a certain interval corresponding to the availability of the most important model forcing. NOAA's GFS has a forecast length of approximately 7 days and is updates every 6 hours. In order to bridge the gap of 6 hours with the previous cycle a historical simulation (hindcast) will run prior to forecast simulation. In contrast to the forecast simulation the hindcast simulation will be forced with observed data if so available in order to provide most accurate initial conditions for the forecast run.

As discussed in paragraph 3 the Delft-FEWS software has been extended with functionality to serve coastal applications. More specifically the model adapters listed in figure 4 have been developed.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Delft-FEWS Model Adapter developments for coastal forecasting systems.

In order to move towards impact based forecasting and to support decision making note that an adapter for the Bayesian DSS has been developed as well. As such, the tool can be included in the Early Warning framework as well.

All developed adapters are available as part of the Delft-FEWS software [4]. Example configurations have been made available via Deltares wiki [1].

## 5 Dissemination

The Early Warning system including DSS is developed for forecasters and decision makers at expert level. Proper use of the system and reliable forecasting requires both experiences in physical processes as well as basic knowledge of the EWS software. For local authorities,

stakeholders and finally the public, forecast and warning services need to be disseminated using easy to interpret/access products.

Therefore a web application has been developed which can be assessed without connection to the FEWS software. Data from the EWS will be exported in NetCDF to an OpenDAP/Thredds server. Using Web Mapping Service (WMS) spatial data from the NetCDF can be displayed in the webviewer with limited configuration.
![img-4.jpeg](img-4.jpeg)

Figure 5. EWS - Webviewer connection
The figure below shows a screenshot of such spatial data at one of the case study sites.
![img-5.jpeg](img-5.jpeg)

Figure 6. Xbeach results displayed in EWS
Bayesian network output is made available in GeoJSON format which can be included in the webviewer as well.
![img-6.jpeg](img-6.jpeg)

Figure 7. Webviewer presentation of Bayesian DSS results

## 6 Conclusions

In the first year of the RISC-KIT research project the EWS have successfully been set up for the case study sites. Model adapters have been developed in order to connect the required models to Delft-FEWS. The Bayesian Network can be fed and accessed by DelftFEWS. The resulting information concerning hazards has been integrated in the Delft-FEWS displays. The
application of these systems is the next steps in the RISCKIT project.

## 7 Acknowledgements

This RISC-KIT project (contract 603458) is supported by the European Commission under the Environment (including climate change) Theme of the 7th Framework Program for Research and Technological Development.
