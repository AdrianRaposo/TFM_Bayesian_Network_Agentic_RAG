## OPEN ACCESS

EDITED BY
Marie Anne Eurie Forio,
Ghent University, Belgium
REVIEWED BY
Tariq Mukhtar,
Pir Mehr Ali Shah Arid Agriculture
University, Pakistan
Mazhar Iqbal Zafar,
Quaid-i-Azam University, Pakistan
*CORRESPONDENCE
Sophie Mentzel,
som@niva.no
SPECIALTY SECTION
This article was submitted to
Environmental Informatics and Remote
Sensing,
a section of the journal
Frontiers in Environmental Science
RECEIVED 31 May 2022
ACCEPTED 22 August 2022
PUBLISHED 15 September 2022

## CITATION

Mentzel S, Grung M, Holten R,
Tollefsen KE, Stenrød M and Moe SJ (2022), Probabilistic risk assessment of pesticides under future agricultural and climate scenarios using a
bayesian network.
Front. Environ. Sci. 10:957926.
doi: 10.3389/fenvs.2022.957926
COPYRIGHT
(c) 2022 Mentzel, Grung, Holten, Tollefsen, Stenrød and Moe. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Probabilistic risk assessment of pesticides under future agricultural and climate scenarios using a bayesian network

Sophie Mentzel ${ }^{1 *}$, Merete Grung ${ }^{1}$, Roger Holten ${ }^{2}$, Knut Erik Tollefsen ${ }^{1,3}$, Marianne Stenrød ${ }^{2}$ and S. Jannicke Moe ${ }^{1}$<br>${ }^{1}$ Norwegian Institute for Water Research, Section for Ecotoxicology and Risk Assessment, Oslo, Norway, ${ }^{2}$ Norwegian Institute of Bioeconomy Research, Division for Biotechnology and Plant Health, Ås, Norway, ${ }^{3}$ Norwegian University of Life Sciences (NMBU), Faculty of Environmental Sciences and Natural Resource Management, Ås, Norway

The use of Bayesian networks (BN) for environmental risk assessment has increased in recent years as they offer a more transparent way to characterize risk and evaluate uncertainty than the traditional risk assessment paradigms. In this study, a novel probabilistic approach applying a BN for risk calculation was further developed and explored by linking the calculation a risk quotient to alternative future scenarios. This extended version of the BN model uses predictions from a process-based pesticide exposure model (World Integrated System for Pesticide Exposure - WISPE) in the exposure characterization and toxicity test data in the effect characterization. The probability distributions for exposure and effect are combined into a risk characterization (i.e. the probability distribution of a risk quotient), a common measure of the exceedance of an environmentally safe exposure threshold. The BN model was used to account for variabilities of the predicted pesticide exposure in agricultural streams, and inter-species variability in sensitivity to the pesticide among freshwater species. In Northern Europe, future climate scenarios typically predict increased temperature and precipitation, which can be expected to cause an increase in weed infestations, plant disease and insect pests. Such climate-related changes in pest pressure in turn can give rise to altered agricultural practices, such as increased pesticide application rates, as an adaptation to climate change. The WISPE model was used to link a set of scenarios consisting of two climate models, three pesticide application scenarios and three periods (year ranges), for a case study in South-East Norway. The model was set up for the case study by specifying environmental factors such as soil properties and field slope together with chemical properties of pesticides to predict the pesticide exposure in streams adjacent to the agricultural fields. The model was parameterized and evaluated for five selected pesticides: the three herbicides clopyralid, fluroxypyr-meptyl, and 2-(4-chloro-2-methylphenoxy) acetic acid (MCPA), and the two fungicides prothiocanzole and trifloxystrobin. This approach enabled the calculation and visualization of probability distribution of the risk quotients for the future time horizons 2050 and

2085. The risk posed by the pesticides were in general low for this case study, with highest probability of the risk quotient exceeding 1 for the two herbicides fluroxypyr-meptyl and MCPA. The future climate projections used here resulted in only minor changes in predicted exposure concentrations and thereby future risk. However, a stronger increase in risk was predicted for the scenarios with increased pesticide application, which can represent an adaptation to a future climate with higher pest pressures. In the current study, the specific BN model predictions were constrained by an existing set of climate projections which represented only one IPCC scenario (A1B) and two climate models. Further advancement of the BN modelling demonstrated herein, including more recent climate scenarios and a larger set of climate models, is anticipated to result in more relevant risk characterization also for future climate conditions. This probabilistic approach will have the potential to aid targeted management of ecological risks in support of future research, industry and regulatory needs.

## Keywords

bayesian network models, exposure modelling, environmental risk assessment, pesticides, uncertainty

## 1 Introduction

Climate change (CC) is expected to shift weather patterns, and consequently can alter the way water and food resources are obtained and managed worldwide. Already today, European assessment for rivers and lakes report that 5--15% of the monitoring stations show exceedances of environmental quality standards by herbicides, and 3--8% by insecticides over the period 2007--2017 (Mohaupt et al. 2020). Nevertheless, in future pesticides will be extensively used as they will continue to play a vital role in the food production process and food security (Popp et al. 2013). Despite thorough regulation of pesticides, large knowledge gaps continue to hinder risk assessment, especially when it comes to potential environmental impact of pesticide mixtures and impacts of climate and regional factors (Topping et al. 2020; Weisner et al. 2021). In Northern Europe, predicted increase in plant diseases and insect pests may consequently lead to higher pesticide use and thereby occurring concentration of pesticides in the environment (Kattwinkel et al. 2011; Sutherst et al. 2011; Delcour et al. 2015). As pesticide environmental fate and exposure scenarios for Norway and the Nordic countries deviate from EU predictions due to spatial (regional) or temporal differences (Stenrød et al. 2008; Holten et al. 2018), the pesticide use, emissions, exposure and fate are not adequately represented by the standardized EU model scenarios (Stenrød et al. 2016). To safeguard environment health better, there is a need to improve the integration of trend connected to CC into environmental risk assessments of pesticides, considering both direct effects such as the shifts in climate conditions and indirect effects such as changes in pesticide application patterns. This should subsequently enable better informed risk management.

Current paradigms for environmental risk assessment (ERA) of pesticides typically aim to take into account the variability of species sensitivities by estimating a proportion of affected species in a community, which is used to define a predicted no-effect concentration (PNEC) of the pesticide (More et al. 2019). The traditional risk characterization of pesticides usually uses single-value e.g. toxic exposure ratio derived from the PNEC divided by the predicted environmental concentration (PEC) to assess whether a chemical substance poses a risk to the environment (EC, 2011). In this study, a more general approach was applied using a risk quotient (RQ) that is calculated as PEC/PNEC, where a potential risk to the environment is assumed whenever the PEC exceeds the safe concentration (PNEC) (Bruijn et al. 2002; More et al. 2019). These derived point estimates may convey an unjustified sense of accuracy (Rai et al. 2002), as they ignore many sources of uncertainty such as the variability of pesticides concentrations in the environment or other factors that influence the exposure of biota to these chemicals. Especially in Europe, these traditional methods seek to avoid underestimating risk by using conservative assumptions (i.e. assessment factors) to account for various sources of uncertainty (Verdonck, 2003). This way, protective decision making relies on precautionary safety margins (Fairbrother et al. 2015). Spatial and temporal variations in exposure are caused by many factors, including changing environmental characteristics and contamination sources (Artigas et al. 2012) that can cause uncertainty. There is therefore a need for risk assessment methodology to better account for uncertainty and variability in chemical exposure (Belanger and Carr, 2020).

Probabilistic risk assessment make use of probability distributions to characterize uncertainty in all parts of the risk characterization (EUFRAM, 2006; Mentzel et al. 2021). Ergo, fully probabilistic risk characterization can better account for spatial and temporal variability of both chemical concentrations and species sensitivity (Solomon et al. 2000; Verdonck, 2003; EUFRAM, 2006; Fairbrother et al. 2015). Several probabilistic

methods have been proposed to characterize risk while including estimation of stochastic properties and uncertainty (Maertens et al. 2022). The general responsibility of scientists to communicate uncertainties has also been highlighted by the EU (EFSA BFR, 2019). Already 2 decades ago, the use of probabilistic risk assessment has been recommended for the European Union (EU) (Jager et al. 2001) but is still not commonly applied in regulatory risk assessment (Fairbrother et al. 2015). Probabilistic methods that incorporate distributions for exposure and effect are e.g. joint probability curves and quantitative overlap. Generally, probabilistic methods require more data for calculation of distributions compared to traditional ERA, but on the other hand probabilistic methods make better use of available data as well as other sources of information (Campbell et al. 2000; Verdonck, 2003). However, some of the results are difficult to communicate and thereby challenging for decision-makers to interpret and understand (Verdonck, 2003; FOCUS, 2007), possibly because they are often based on cumulative distribution curves (EUFRAM, 2006). A Bayesian network (BN) model has therefore been proposed as a more user-friendly and intuitive method for supporting probabilistic risk assessment of pesticides (Mentzel et al. 2021).

In this study, the BN model developed by Mentzel et al. (2021) was further extended and explored to assess environmental risk of pesticides under future scenarios. The extended BN model presented here includes the output of a pesticide exposure prediction platform for a representative Northern European area (WISPE; Bolli et al. (2013)) under different climate and pesticide application scenarios. The main objective of this study was to develop an approach for incorporating alternative climate change and pesticide application scenarios into a probabilistic approach to risk characterization, based on the available data and information for a Norwegian case study.

## 2 Materials and methods

### 2.1 Approach

### 2.1.1 Bayesian network model, structure and implementation

Bayesian methods have been recommended by the European Food Safety Authority (EFSA et al. 2017) for uncertainty analysis in the process of identifying limitations in scientific knowledge and evaluating their implications for scientific conclusion. Bayesian networks (BNs) are a branch of Bayesian approaches that have been increasingly used in environmental risk assessment and management (Aguilera et al. 2011; Moe et al. 2021b; Kaikkonen et al. 2021). BNs are probabilistic and graphical models, more specifically directed acyclic graphs (DAG) (Kanes et al. 2017) that have no feedback loops. The nodes (variables) are connected through links (potentially causal relationships) shown as arcs representing conditional probability tables (CPTs) (Kjærulff and Madsen, 2013). Each node has a set of alternative states (typically intervals) that are quantified by probability distributions. To update probability distributions of the network, the Bayes' rule is implemented to combine prior probabilities with new evidence (Carriger et al. 2016). One of the main benefits of BNs is that all components can be quantified by probability distributions, which facilitates a probabilistic risk calculation. Along these lines, BNs can incorporate various sources of information such as expert opinion, literature and model outputs, enabling a greater use of available data and knowledge (Carriger and Newman, 2012; Carriger et al. 2016). An example of the application of spatial BNs for probabilistic assessment of pesticide exposure on a field level has been carried out by Troldborg et al. (2021). Carriger and Barron (2020) combined probabilistic exposure and effect characterization into calculation of a probabilistic risk quotient (RQ) of Mercury for the Florida panther. This approach to a probabilistic calculation of RQ and associated uncertainties was further developed by Mentzel et al. (2021), by using species sensitivity data for the effect characterization to represent risk to aquatic ecosystems.

The BN conceptual model developed here is based on Mentzel et al. (2021) and consist of four modules (Figure 1): 1) future scenarios (orange), 2) pesticide exposure (blue), 3) toxic effect (green) and 4) risk characterization (grey). The scenario module contains a scenario node that is based on the climate and pesticide application. These scenarios determine the instantaneous pesticide concentration and its probability distribution (pesticide exposure module). This instantaneous concentration node together with the set time since application (node) determines the distribution of the time-specific concentration node, via a log-linear equation. The risk characterization module composes the exposure/effect ratio node that together with an appropriate precautionary factor predicts the probabilities of the RQ intervals. The finalized BN can be instantiated by selecting a scenario and specifying the time since application of interest as evidence. Given this evidence, probability distributions will be updated throughout the network. The four modules are described in more detail in Section 2.2.

### 2.1.2 Exposure sampling and modelling

Measured pesticide exposure concentrations, their distribution and associated uncertainties are highly influenced by sampling method, time and rate (Spycher et al. 2018). Data derived from monitoring has a wide range of uncertainties through sampling constraints and limited representativeness (FOCUS, 2017). Yet, a realistic environmental concentration is vital for reliable environmental risk assessment. This is especially significant whenever a single number is used without accounting for uncertainty, but is also influential when trying to derive a representative exposure distribution as uncertain estimations can

![img-0.jpeg](img-0.jpeg)

FIGURE 1 Conceptual model for the risk estimation of a pesticide. Pesticide exposure derives input from the WISPE platform and is determined by the associated future scenarios. The toxic effect nodes together with the exposure concentration derives the risk quotient under risk characterization.

hinder appropriate decision-making (Wolf and Tollefsen, 2021). Thence, the EU (Directive 2009/128/EC (EC, 2009a) and REGULATION (EC) No 1107/2009 (EC, 2009b)) offers the option to use models to predict environmental concentrations (PECs) in surface waters. Even if monitoring data are available, the use of modeling approaches for exposure assessment is encouraged by EFSA (2017). They have developed the FOCUS (FOrum for the Co-ordination of pesticide fate models and their Use) surface water scenarios using the model tool SWASH, a GUI for the models PRZM (Pesticide Root Zone Model), MACRO and TOXSWA (TOXic substances in Surface Waters). PRZM and MACRO are models frequently used to simulate pesticide transport in soil while TOXWA simulates the dilution at the edge of field or drain water concentration from the other two models in different surface water body types. SWASH takes agricultural management practices, climate, crops, topography, and soil types into account (Adriaanse et al., 2017).

For this study, we used the World Integrated System for Pesticide Exposure (WISPE) platform, which was developed to evaluate the potential for pesticide exposure to surface waters and groundwaters (Bolli et al., 2013). The WISPE platform was configured with scenarios containing crop, soil, and weather conditions for representative agricultural areas among others in the EU, USA and Norway. This modeling platform interlinks the pesticide root zone model (PRZM), an exposure analysis modeling system (EXAM) (Burns, 2004) and the aquifer dilution assessment model (ADAM) (Williams, 2010) similar to TOXWA. The PRZM model simulates the movement of chemicals within and below the root zone (in unsaturated soil systems). EXAM is a hydraulic model combined with a chemical fate and transport model simulating processes in aquatic environments. It simulates various processes in the aquatic environment. ADAM is an integrated model which predicts the chemical dilution, partitioning and persistence to a water body. EXAM and PRZM are standard models used by USEPA, and the latter model is also used in European pesticide registration and risk assessment (REGULATION (EC) No 1107/2009 (EC, 2009b)). In a previous study, the transport of particles and particle bound pesticides was calibrated for two field sites representative for Norwegian agricultural areas by Bolli et al. (2013). The study found that in this northern region the erosion and transport of particle-bound pesticides are heavily dependent on the weather conditions such as precipitation shortly after application or melting-freezing episodes, which take place in spring and winter. The WISPE platform is based on many of the FOCUS default setting but was specifically tailored for northern European conditions and contains e.g. major Norwegian crops, and plant growth effected by climate conditions, therefore being better suited as a exposure prediction tool in this study.

### 2.2 Bayesian network modules

In the following, the information sources and assumptions for the four modules of the BN model and the model runs are described. The software Netica (Norsys Software Corp, www.norsys.com) was used to construct the BN model. The BN was constructed with identical node structure and number of states for all of the selected pesticides, but with different discretization of the concentration nodes. For each pesticide, the range of the exposure and effect concentration nodes was adapted to the distributions derived from the data used for exposure and effect assessment, respectively. We chose a relatively high number (10) of intervals to obtain a high resolution of the model. The concentration nodes were discretized by equidistant intervals in the log-scale.

The exposure model platform WISPE was run for each selected pesticide, for three application scenarios and for two climate models. In the selected case study area, environmental

TABLE 1 Bayesian network node description detailing the type of node, the number of states and the method used to parameterize the network.


factors such as soil and site parameters together with chemical properties and climate scenarios were linked to the exposure of a pesticide by using the WISPE platform. The probability distribution of pesticide exposure was obtained from predicted concentrations for multiple years, which enabled accounting for variability over a longer time period (FOCUS, 2017). Correspondingly, for the probability distribution of effects, the range of species sensitivities was determined from available toxicity data. The RQ node was discretize with a high number of states, this enabled exploring the differences between scenarios. A more detailed node description and model assumptions are given in the following Table 1.

### 2.2.1 Future scenarios

The agricultural sector manages 3.5\% of Norway's land area pr. 2021. Being part of northern Europe, Norway has lower temperatures and a shorter growing season than central and southern Europe. These climate conditions restrict the area suitable for grain cultivation. Until the year 2060, the annual average temperature is expected to increase by approx. $2^{\circ} \mathrm{C}$, with the largest increase in temperature in winter, and the lowest in summer in Norway. Consequently, the meteorological growing season will be longer than the current, with a predicted increase in growing season of up to 2 months towards the end of the century (Fuglestvedt, 2016). This may lead to earlier sowing, ripening and harvest for spring cereals and growing of crop types that mature later but offer a higher yield potential. CC is also expected to lead to significant changes in precipitation with an increase of $8 \%$ for annual precipitation at the end of the century, but with large variation between the cropping regions in Norway (Olesen and Bindi, 2002). For the cultivation of grain, not only the amount and intensity of rainfall is of interest, also its frequency and distribution throughout the growing season. Other expected CC impacts are the introduction of new plant pathogens and pests from southern countries to northern areas while existing will be able to take advantage of a longer growing season and multiply faster than before. Also, changes in crop composition may lead to a change in the occurrence of the diseases and possibly new host-parasite interactions (Fuglestvedt, 2016). Furthermore, pesticides efficacy is affected by environmental factors such as temperature, precipitation and wind (Olesen and Bindi, 2002). In Norway, a longer growing season and more frequent pest infestations may require the use of more pesticides. A warmer climate is expected to result in increased production of winter wheat. The milder cold season may provide better overwintering conditions for plant pathogens, which might entail early and more severe infestation of the crop the following season. The most relevant measure apart from using resistant crop types is spraying of fungicides. In addition, early infestations require spraying both

earlier and more frequently during the growing season (Fuglestvedt, 2016). Based on these considerations, winter wheat was chosen as the model crop for this study.

A more detailed description of the expected CC for this region is given by Hanssen-Bauer et al. (2015). In the following, the future scenarios used to run the WISPE platform are described.

### 2.2.1.1 Climate scenarios

In this study, two sets of climate projections were used originally developed for the site Grue in the south east of Norway (ca 160 km North-east of Syverud/Ås) under the GENESIS project (2009--2014, https://cordis.europa.eu/project/ id/226536). Both were derived from the greenhouse gas emission scenario “A1B” (IPCC, 2000), which was developed to represent a future world of very rapid economic growth, low population growth and rapid introduction of new and more efficient technology, for a spatial resolution of 50 km. The two sets of climate projections were derived by two global climate models (GCM) which will be referred to as Climate Model 1 (C1) and Climate Model 2 (C2). The GCM of C1, “ECHAM5-r3” (Roeckner et al. 2004), was developed by the Max Planck Institute for Meteorology, and the GCM for C2, “HADCM3-Q0” (Gordon et al. 2000), was developed at the Hadley Centre. Regional climate models (RCMs) are commonly applied to downscale from the global to more local levels (Jones et al. 2011; Samuelsson et al. 2011). Here, the same RCM called RCA3 was used, developed by the Rossby Center at SMHI (the Swedish Meteorological and Hydrological Institute). Thereby, C1 represents the regional climate model “ECHAM5-r3 A1B-SMHI-RCA3” and C2 represents “HADCM3-Q0 A1B-SMHI-RCA3”.

The climate projections used in this study has several limitations: the emission scenario and the two climate models are rather old, and they have not been bias-corrected for the study area. Moreover, climate projections should ideally be obtained from a larger ensemble of climate models rather than one or a few models (Moe et al. 2022). However, generating a new and more appropriate set of climate projections was beyond the scope of this study. Therefore, the climate projections that were already derived for the WISPE platform were considered sufficient for the purpose of demonstrating this BN approach to linking climate projections, pesticide exposure and risk characterization.

Projections from the two climate models (C1 and C2) differed in precipitation, temperature, evapotranspiration, solar radiation and wind. For example, they had different projected changes in number of days with snow cover and changes of annual rainfall (Kjellstõm et al. 2011). The differences between the two climate models are especially of interest for the chosen days and months of pesticides application. Based on Mann-Kendall (MK) trend analysis, C1 showed a positive trend in temperature, evapotranspiration and precipitation for a 3-days average before the day of pesticide application. When comparing climate conditions for 10-days average before day 21 after application, a positive trend was detected for temperature and evapotranspiration (i.e. the process of water evaporation from soil and other surfaces through transpiration from plants). In general, C2 showed no trend for May, and even a negative trend for October for a 3-days average before the day of application (see Supplementary Table S2). The projections from C1 were more consistent with more recent climate projections for Norway, which show that an increase in temperature and precipitation can be expected (Hanssen-Bauer et al. 2015). Consequently, in this paper we decided to focus mainly on predicted exposure concentration based on C1.

### 2.2.1.2 Pesticide application scenarios

The first pesticide application scenario is based on the current common practice dosage and is referred to as the “baseline” scenario (see Table 2). The second scenario, referred to as “baseline-50%”, is inspired by the European Green Deal, which aim for a 50% reduction of the pesticide use by 2030 (EC, 2020). The third scenario represents a potentially increased use of pesticides in the future, for example due to changing climate conditions and increased pest pressures (Fuglestvedt, 2016) and is referred to as “baseline+50%”.

We selected active pesticide ingredients that are all approved in Norway for crop protection in winter wheat. Two plant protection products, a herbicide containing MCPA (CAS nr. 94--74-6), fluroxypyr-meptyl (CAS nr. 81,406--37-3) and clopyralid (CAS nr. 1702--17-6), and a fungicide composed of trifloxystrobin (CAS nr. 141,517--21-7) and prothioconazole (CAS nr. 178,928--70-6), were chosen for the purpose of demonstrating the approach. Inherent properties such as molecular weight, water solubility, sorption properties (Koc), degradation half-life (DT50 soil), and vapor pressure, and Freundlich exponent (1/n), and systemic property e.g. plant uptake factor, were collected and included in the data asset (see Supplementary Table S1).

The associated application rate and time of spraying were used to define the application scenario for the WISPE platform runs. It was assumed that the herbicide is applied once in the first half of May (crop growth stage BBCH 13--14; cf. label for Ariane ™ S, Corteva Agriscience), and that the fungicide is applied once in the first half of October (after sowing and germination of the winter wheat; cf. label for Delaro SC 325, Bayer Crop Science). For the calibration of the WISPE platform no tillage was assumed. Some of the combinations chosen for pesticide application, e.g. the choice of no soil tilling in combination with winter cereals, may not be the most common/optimal agronomic practice and can hence add to some of the uncertainty in the modelling.

Table 2: Description of application scenarios used in this case study for the five selected pesticides.


### 2.2.2 Pesticide exposure

The scenarios described above were used as input information for the WISPE platform. Additional settings used to run the platform are described in the succeeding section. The exposure distributions used as input for the pesticide exposure module were based on the predicted exposure concentration from the WISPE platform.

#### 2.2.2.1 WISPE platform settings

When the WISPE platform was first developed as a tool to estimate pesticide exposure in ground- and surface water for Norwegian conditions, two study areas were chosen as representative field sites to generate data for calibration and validation of the model (Bolli et al., 2013). In this study, the Syverud was used as a site scenario, which was developed to represent larger agricultural areas in South East Norway. The study site is located on the grounds of the Norwegian University of Life Sciences (NMBU) in Ås (Supplementary Table S1). The soil in this study area is classified as loam/silt loam, with 26% clay, 49% silt, and 25% sand content. The area was formerly used as a meadow which resulted in a soil structure with high infiltration capacity, aggregate stability and saturated hydraulic conductivity (Bolli et al., 2013). For the model simulations the site was assumed to be ploughed in autumn, with a ploughing depth of 20 cm. The platform predicts output concentrations for a stream, pond and ditch with parameters adapted originally from TOXSWA into the EXAM model.

We have only considered the predicted output for the stream environment, with the following water body parameters: 1 m width, 100 m total length, 0.3 m average water depth, 15 mg/L concentration of suspended solids, 5% organic carbon content, and 800 kg/m3 dry bulk density (FOCUS, 2015). WISPE was calibrated for the model crop winter wheat.

#### 2.2.2.2 Exposure prediction platform implementation

The WISPE platform was run according to the previously mentioned future scenarios and platform settings such as the selected representative field site, crop type and for the various time-periods of C1 and C2. The WISPE platform predicted exposure concentration for 26 years, corresponding to the 26 years over which the model runs. The concentrations were predicted for instantaneous, 24 h, 96 h, 21, 60 and 90 days.

In the further process, the time-periods were changed into three periods (year 2000–2030, 2035–2065, 2070–2100) to derive the distributions (BN input) representing inter-annual variation within each of the 30-year period. The platform simulated pesticides to specified unique application conditions for the two climate models. In total, 18 scenarios were used in the developed BN per pesticide (Table 3). The following example shows the log-transformed pesticide concentration against time since application predicted by WISPE for scenario 11 (Figure 2). A log-linear equation was fitted to each of the predicted concentrations time series. Data processing and analysis was carried out in R (version 4.1.0), using the tidyverse package (Wickham et al., 2019) and some base R functions (R Core Team, 2020). Within each scenario the slope did not differ significantly among the years (see Figure 2), therefore the average slope across years was used to calculate the time-specific concentration for each scenario (see Supplementary Information SII). The probability distribution of the instantaneous concentration (representing inter-annual variation) was used as input in the conditional probability table (CPT) of the instantaneous concentration node. This distribution was combined with the slope to derive the distribution of the time-specific concentration node (see Supplementary Information SII). In general, the instantaneous node interval range differed for each selected pesticide: clopyralid 0.0025–0.6065 μg/L, fluroxypyr-meptyl 0.0111–4.4817 μg/L, MCPA 0.0821–12.1825 μg/L, prothioconazole 0.0302–0.2231 μg/L, trifloxystrobin 0.0235–0.1653 μg/L.

### 2.2.3 Pesticide effects

Uncertainties related to current effect assessment are often associated with extrapolation from laboratory to field and inter-intraspecies variation (Rai et al., 2002) and can also be linked to the data set size. In traditional regulatory effect assessment, these uncertainties are usually accounted for by assessment factors to increase the assumed safe concentration threshold (PNEC). In this study, two types of effect distribution were derived and used


TABLE 3 Overview of scenarios used in the Bayesian network model combining the three scenario components Climate model, Period and Application scenario. For description of the climate models, see Section 2.2.1.1. For definition of the pesticide application scenarios, see Table 2.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 Example log-linear regression of the concentration in the stream predicted by the WISPE platform for MCPA with an application baseline scenario for the C1 and the time interval 2070–2100.

as input in the pesticide effect module. They were based on either NOEC (no-observed effect concentrations) values or on EC50 (effect concentration for 50% of the test population) values and collected for each of the selected pesticides. The derived effect distribution is similar to a species sensitivity distribution (SSD), representing inter-specific variation in sensitivity to toxicants, which is used extensively in ecotoxicology (Belanger and Carr, 2020). SSDs are now commonly used as an alternative to the conservative approach on the basis of the most sensitive species (lowest NOEC value). They are based on multiple toxicity tests of different species and thereby reflect interspecies differences in sensitivity to a chemical. Subsequently, SSDs can be used to develop a community level threshold (Belanger et al., 2017). However, SSDs are usually used to derive a single threshold value such as the HC5 (hazardous concentration to 5% of the species), as a basis for the PNEC. Here we follow the approach presented by (Mentzel et al., 2021), to use the whole species sensitivity distribution in the calculation of the exposure/effect ratio distribution (Section 2.2.4). Toxicity data were mainly collected and used from the US EPA ECOTOX Knowledgebase (https://cfpub.epa.gov/ecotox/search.cfm) and supplemented with data from Middle Tennessee State University EnviroTox Database (https://envirotoxdatabase.org). The EC50 effect distribution was derived from EC50 and LC50 (lethal dose for 50% of the test population) toxicity data (Table 4). The NOEC distribution is based on NOEC and NOEL (no-observed effect level) values, apart from Clopyralid for which only NOEC toxicity data was available. If multiple values for the same species occurred in the data set, the mean was used as a data point to derive the distribution (Mentzel et al., 2021). The number of observations for this study varied depending on the chemical, and whether it was an EC50 or NOEC toxicity test. In this study, we only considered adverse effects such as

TABLE 4 Effect (toxicity) data collected for this study, detailing the effect types per pesticides and the derived EC50 and NOEC natural $\log (\ln )$ mean and standard deviation for the natural log distributions.


![img-2.jpeg](img-2.jpeg)

FIGURE 3 Example of the Bayesian network parameterized for fluroxypyr-meptyl, with a baseline $+50 \%$ application, global climate model C1, time period of 2035-2056, for a time since application of 1 day and a EC50 based effect distribution.

TABLE 5 Results from Mann-Kendall trend analysis of the predicted pesticide exposure concentrations for the following WISPE model settings: climate models C1 and C2; baseline application in May (herbicides) and October (fungicides). The predicted exposure concentration series represent both acute and chronic conditions (day 1 and 21 since application, respectively). For each series, the overall trend for the whole period of years 2000-2100 was analyzed. The test statistic τ denotes increasing (τ > 0) or decreasing (τ < 0) trend.


mortality, reproduction and growth. The distribution was fitted using the R package MASS (Venables and Ripley, 2002). The data preparation was carried out with the R package tidyverse (Wickham et al., 2019) (see Supplementary Information SIII).

### 2.2.4 Risk characterization

This module consists of three nodes: exposure/effect ratio, a precautionary factor and the risk quotient (RQ). In traditional risk assessment, an RQ higher than 1 indicates a reason for concern (Bruijn et al., 2002).The assumptions for the node input are described in Table 1. The BN was run for the different scenarios and with either an EC50 (and day 1 since application), representing an acute exposure scenario, or a NOEC distribution (and day 1-61 since application), representing a chronic exposure scenario. As explained in Mentzel et al. (2021), the precautionary factor was introduced as a scaling factor to have a similar role as the assessment factors, which are frequently used in risk assessment to obtain a higher safe concentration threshold (see TGD (SCHEER, 2017)). Thus, a higher assessment factor or a higher precautionary factor will increase the probability of the

RQ exceeding 1. In traditional risk assessment, the decision on an appropriate assessment factor is based on evaluation of the available toxicity test data used to derive the effect distribution to account for uncertainties in the used data set and for extrapolation. In the approach presented by Mentzel et al. (2021), an appropriate precautionary factor was found by calibrating the RQ distribution predicted by the BN to the single-value RQ of a corresponding traditional risk calculation. In the case study by Mentzel et al. (2021) it was found that for a fully probabilistic approach with exposure data derived from monitoring with infrequent sampling though reflecting chronic exposure to the ecosystem, and collected effect e.g. toxicity test (NOECs), the most appropriate precautionary factor was $30-300$. In the current study, some of the uncertainties associated with the exposure concentrations were overcome by using predicted exposure concentrations that enabled the use of peak concentrations in addition to the declining concentrations over time (see Figure 2). In our view, this justified the usage of a lower precautionary factor of 1-10. To account for additional interspecies variation in sensitivity that

![img-3.jpeg](img-3.jpeg)

was not represented by the relatively small data set on effects, a more conservative precautionary factor of 10 was applied for all RQ distributions displayed in this study (see Figure 3).

A Mann-Kendall trend analysis a statistical method that is rank-based and non-parametric, and widely used in hydrometeorological time series trend detection (Wang et al., 2020). The trend analysis was carried out for the predicted exposure concentration (WISPE platform output) for baseline application, C1 and C2, Day 1 and 21 since application and for all of the selected pesticides (see Table 5). A positive trend indicates an increase of the predicted exposure concentration. The trend was concluded to be negative whenever the test statistic Kendall's τ < 0 and the p < 0.1. The trend was concluded to be positive when τ > 0 and p < 0.1.

# 3 Results

## 3.1 Predicted pesticide exposure

Some of the trends in the projected climate variables such as mean temperature, precipitation, radiation, evapotranspiration and wind (see Supplementary Table S2) were also reflected in the trends of the predicted exposure. The Mann-Kendall trend analysis showed mostly no significant trends over the whole range of years (2000–2100), for the different pesticides and seasons. However, C1 had a positive trend in mean temperature, precipitation and evapotranspiration in October, this trend is also reflected in a positive trend of the exposure concentration of fungicides prothiocanazole and trifloxystrobin that are applied in October (for C1) (Table 5).

A closer look at the relationship between the instantaneous exposure concentration and precipitation, one of the determining climate conditions for the transport and fate of pesticides, revealed that higher amount of precipitation was associated with increased exposure concentration (Figure 4). In addition, there was a positive interaction between pesticide application and precipitation, as the effect of precipitation was higher (steeper slope) when the pesticide application was higher. This relationship was not further investigated here, but the pesticide concentrations predicted by the WISPE platform predictions showed similar temporal trends as those described for the climate variables (see Supplementary Table S2).

## 3.2 Predicted risk quotient distribution for various scenarios

The output for each of the settings (evidence) used in this study has been reported in the Supplementary Information SIV. It contains a detailed collection of the probabilities for each of the RQ node intervals depending on the selected evidence. In the following, the predicted RQ node distributions for the different scenarios (see Table 3 for reference) are visualized as stacked bar plots for easy comparison (Figure 5). The RQ was calculated with an effect distribution based on either NOEC values (RQNOEC) or EC50 values (RQEC50). This analysis enabled the identification of periods with higher risk of environmental effects of individual pesticides or groups of pesticides.

### 3.2.1 Risk quotient distribution across the time since application

For a baseline application scenario, at day 1 the probability of RQNOEC to be higher than 1 was 1% for MCPA (Figure 5C), 0.98% for fluroxypyr-meptyl (Figure 5B), and 0% for Clopyralid (Figure 5A), prothioconazole (Figure 5C), and trifloxystrobin (Figure 5E). Overall, the time-specific RQNOEC declines with time since application (Figure 5). So, at Day 2 probability of RQNOEC to be higher than 1 decreased to 0.79% for MCPA and 0.65% for fluroxypyr-meptyl. At Day 5 the RQNOEC to be higher than 1 decreased further to 0.69% for MCPA and 0% for fluroxypyr-meptyl. Considering a lower RQ threshold (corresponding to a higher precautionary factor), the probability of RQ > 0.1 at Day 1 was highest for MCPA, followed by fluroxypyr-meptyl, trifloxystrobin, clopyralid and prothioconazole.

![img-4.jpeg](img-4.jpeg)

### 3.2.2 Plausible scenarios: Combination of climate change and pesticide application

A change in pesticide application patterns such as an increase in the rates or number of applications per season can be considered as an adaptation to consequences of climate change (e.g., increased pest pressure). Therefore, the scenario combining future climate projections (period 2035–2065) with increased pesticide application was considered as a plausible scenario. On the other hand, the combination of future climate projections with reduced pesticide application represent a scenario more in line with EU's pesticide policy. Hence, we compare the RQEC50 of the current time period (2000–2030) and baseline application with the predicted RQEC50 for a future time period (2035–2065) as well as baseline-50% and baseline+50% application scenarios. In general, the probability of RQEC50 exceeding 1, which commonly used as a threshold for concern, was low and not much influenced by the different time periods or application scenarios.

Focusing on lower RQ thresholds, examples are shown for the fungicide trifloxystrobin (Figure 6A) and the herbicide fluroxypyr-meptyl (Figure 6B). Trifloxystrobin had more than 10% probability of RQEC50 exceeding 0.03 for the current practice. In future, applying less fungicide resulted in a shift towards lower RQ intervals and an overall decrease in risk. From the BN prediction, it was observed that applying 50% less resulted in a shift towards lower RQ intervals, with a probability to be above 0.3 decreasing from 12.5% to 3.5%. Comparing baseline

![img-5.jpeg](img-5.jpeg)

FIGURE 6 Predicted risk quotient distribution for a selected herbicide and fungicide, for a time since application of 1 day, for the climate model C1 and for EC50-based effects distribution. The scenarios 1, 4, 5, 6 (Table 3) are displayed for the herbicide fluroxypyr-meptyl (**A**) and the fungicide trifloxystrobin (**B**).

and baseline+50% the RQEC50 distributions were similar, with a probability of being above 0.03 of about 12.5%. This was also the case for some of the other pesticides (e.g. clopyralid or MCPA) (see Supplementary Figure S2). Fluroxypyr-meptyl, on the other hand, showed a change to higher RQEC50 intervals for the baseline+50% application. For this herbicide the probability for RQEC50 to be above 0.03 increased from 7.2% (for baseline) to 8.9% (for baseline+50%) and decreases to 6.4% (for baseline-50%).

## 4 Discussion

As monitoring of environmental pesticide concentration is costly and time-consuming, future climate conditions need to be incorporated for better risk assessment. The complexity of processes in pesticide risk assessment can to some degree be overcome by taking advantage of the BNs' ability to use data from various different sources, which is one of their benefits (Chen and Pollino, 2012; Gibert et al., 2018; Mentzel et al., 2021; Troldborg et al., 2021). Moreover, they can be constructed as causal models that help comprehend hazard pathways and vulnerability relations better and with that assist in risk prioritization (Sperotto et al., 2017). For example, a BN developed for predicting spatial distributions of pesticide exposure in a drinking water catchment was informed by multiple information sources including GIS as well as expert knowledge (Troldborg et al., 2021). A study by Gaasland-Tatro (2016) showed how CC factors and other stressors can be integrated in BNs by using a relative risk model that evaluates ecological parameters over landscape scale regions. Along these lines, Landis et al. (2013) pointed out that today's environmental risk assessment should also consider interactions among contaminant and noncontaminant stressors, together with new regimes of precipitation and temperature at specific geographical sites (Landis et al., 2013).

The BN model presented here demonstrates how a traditional risk characterization score such as the RQ can be made more informative by being presented as a probability distribution. While the traditional risk assessment has focused on whether a single-value RQ score exceeds 1, the BN approach allows for a systematic analysis also of lower risk situations, such as the probability of RQ exceeding 0.3 or 0.1. This way, the model can be used to explore plausible environmental scenarios and

identify early-warning trends in RQ towards levels of concern. Moreover, in our approach, the precautionary factor is used in a more transparent way and better separated from the pesticide effect characterization than the corresponding assessment factor is in traditional risk assessment (Mentzel et al. 2021). The assignment of a precautionary or assessment factor involves a subjective evaluation of data quality and other uncertainties by the risk assessor and should therefore be better separated from the calculation of chemical concentrations, in our opinion. The traditional assessment factor is applied to calculate an assumed safe concentration threshold (predicted no-effect concentration), which is in turn used as the denominator in the calculation of the traditional RQ. In our model, in contrast, the exposure/effect ratio distribution is calculated and displayed before the precautionary factor is included as a final step to obtain the RQ distribution.

The BN model predicted a slight increase in the probability of RQ exceeding 1 for future time periods, for most of the pesticides investigated. In other words, the model predicts higher risk for aquatic organisms under the A1B climate scenario for the intermediate (2035--2065) and last time periods (2070--2100) investigated. This is expected and consistent with previous suggestions regarding pesticide fate and transport being influenced by precipitation in northern Europe. In other words, increased precipitation in future can imply increase risk of pesticides to freshwater ecosystems in agricultural areas. We aim to investigate the role of precipitation and other climate variables on predicted pesticide exposure in the WISPE platform more systematically in later studies, to obtain functional relationships between climate variables and pesticide exposure under different climate scenarios. A quantification of such functional relationships will allow for more efficient exploration of pesticide risk under different climate and agricultural scenarios.

Considering the prediction for future periods, the climate projection used in this study was obtained from an existing project and based on a relatively old climate scenario (A1B). Moreover, the climate models used in this study were not properly bias-corrected for the study area. Thus, improved precision and realism of the BN model predictions could be achieved by using more updated climate projections from more relevant climate scenarios (e.g. RCP4.5 and 8.5) and based on a larger number of climate models. Further model development with a newer and refined version of the WISPE, could reduce some of the uncertainty related to predictions.

The applicability domain of the BN model presented here is constrained by the current applications and calibration of the WISPE model platform. Until now, the WISPE platform was validated by Bolli et al. (2013) and offers the possibility to predict environmental concentrations for specific and representative study fields in Norway. The platform takes into account chemical properties and environmental factors when predicting the exposure of pesticides in the selected water body (Bolli et al. 2013). A predicted exposure time series with multiple peak concentrations could not easily have been incorporated in the exposure module of the BN, which currently assumes a log-linear decrease in pesticide concentration over time. Further development of this module would be needed to account for a more complex temporal exposure pattern.

In addition, extending the current BN with more developed pesticide application, scenarios, including selected crop and pesticide types, and the use of other representative study areas would be beneficial for the integration of variability in model predictions. This BN model could also be further developed to predicting the cumulative risk of intentional pesticide mixtures. Further research efforts could also explore more advanced options for risk characterization as alternatives to the currently used RQ approach, for example making better use of causal dose-response relationships from mesocosm studies in cases where such information can be obtained. Therefore, we are considering an approach that incorporate not only an exposure prediction model under alternative future conditions but also an effect prediction model for selected groups of aquatic species.

The use of BN models in ecotoxicology is still rare compared to other types of environmental assessment (Kaikkonen et al. 2021) even though their use has increased in chemical risk assessment in recent years (Moe et al. 2021a). One of the inherent shortcomings of BNs is the loss of precision due to discretization of continuous variables (Marcot, 2017; Nojavan et al. 2017); this phenomenon was also observed in the predicted exposure concentrations for some of the pesticides in this study, e.g. MCPA. Although the instantaneous pesticide concentration distribution differed between the baseline and baseline+50% scenarios, these differences were not reflected in the exposure concentration node, where the probability distribution appeared very similar. This resulted in similar RQ distribution for the two application scenarios, given the current discretization (Marcot, 2017; Nojavan et al. 2017). The number of node states is often kept low in BN models, because a higher number of states implies that more information is needed for parameterization of the conditional probability tables. In our BN model, however, most of the CPTs were derived from equations and can therefore easily be adapted to a higher number of intervals. It is therefore straight-forward to increase the resolution of this BN model. More generally, this technical problem can potentially be amended by through dynamic discretization which can enable higher resolution and reduce the information loss of the BN predictions (Carriger et al. 2016; Fenton and Neil, 2018).

## Conclusion and future outlook

With this study, we have demonstrated how inputs and outputs from a pesticide exposure prediction model can be incorporated into a Bayesian network to deriving a risk quotient distribution for various scenarios. The constructed network integrates and propagates uncertainty of all

components in a transparent way when performing the probabilistic risk characterization. In general, compared to the current period (2000-2030), the Bayesian network model predicted a slight increase in the probability of risk quotient exceeding 1 for the intermediate (2035-2065) and latest time period (2070-2100) due to changes in future climate conditions, for most of the pesticides investigated in this study.

For further development of this approach we aim to integrate more updated and properly bias-corrected climate projections from a larger ensemble of climate models in the BN, as well as more realistic and better-informed pesticide application scenarios. Nevertheless, the presented approach shows promise in its ability to characterize the environmental risk of pesticides under future scenarios by integrating different types of information from agricultural practice, climate models, pesticide exposure models and toxicity testing.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author.

## Author contributions

Conceptualization, SM, SJM; Data curation-WISPE platform, RH and SM; Data curation-BN model, SM; Formal analysis, SM; Funding acquisition, SJM, MG, MS, and KET; Investigation, SM, SJM, and RH; Methodology, SM and SJM; Project administration, SJM; Software, SM; Visualization, SM; Writing-original draft, SM; Writing-review and editing, SJM, RH, MG, MS, KET, and SM.

## Funding

This research was funded by ECORISK 2050, which has received funding from European Unionâ's Horizon 2020 research and innovation program under the grant agreement No. 813124 (H2020-MSCA-ITN-2018). KE Tollefsen was funded by NIVA's Computational Toxicology Program (www.niva.no/nctp). Roger Holten has received funding from "Utredning om de norske overflatevannscenariene" financed through the Norwegian Action Plan for sustainable use of pesticides (2016-2020).

## Acknowledgments

We thank Randi Bolli, (NIBIO), discussion and advice on the pesticide exposure modelling, as well as Wayne Landis (Western Washington University) and John Carriger (USEPA) for advice on Bayesian network modelling.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fenvs.2022. 957926/full#supplementary-material

Benford, D., Halldorsson, T., leger, M. J., Knutsen, H. K., More, S., Naegeli, H., et al. (2018). Guidance on uncertainty analysis in scientific assessments. EFSA J. 16, E05123. doi:10.2903/j.efsa.2018.5123

Bolli, R. I., Eklo, O. M., Holten, R., and Mulder, P. (2013). "Development of wisp for surface- and groundwater modelling of pesticides in major crops," in National scenarios - Norway. Editor R. Report.

Bruijn, J. D., Hansen, B., Johansson, S., Luotamo, M., Munn, S., Musset, C., et al. (2002). Document on risk assessment. Technical guidance document on risk assessment, Part I and ii, 337.

Burns, L. (2004). Exposure analysis modeling system (exams): User manual and system documentation. Athens, Ga: Ecologist, Ecosystems Research Division U.S. Environmental Protection Agency. Version 2.98.04.06: Epa/600/R-00/081.

Campbell, K. R., Bartell, S. M., and Shaw, J. L. (2000). Characterizing aquatic ecological risks from pesticides using a diquat dibromide case study. II. Approaches using quotients and distributions. Environ. Toxicol. Chem. 19, 760-774. doi:10. 1002/ets.5620190331

Carriger, J. F., and Barron, M. G. (2020). A bayesian network approach to refining ecological risk assessments: Mercury and the Florida panther (puma concolor coryi). Ecol. Model. 418, 108911. doi:10.1016/j.ecolmodel.2019.108911

Carriger, J. F., Barron, M. G., and Newman, M. C. (2016). Bayesian networks improve causal environmental assessments for evidence-based policy. Environ. Sci. Technol. 50, 13195-13205. doi:10.1021/acs.est.6b03220

Carriger, J. F., and Newman, M. C. (2012). Influence diagrams as decision-making tools for pesticide risk management. Integr. Environ. Assess. Manag. 8, 339-350. doi:10.1002/ieam. 268

Chen, S. H., and Pollino, C. (2012). Good practice in bayesian network modelling. Environ. Model. Softw. 37, 134-145. doi:10.1016/j.envsoft.2012.03.012

Delcour, I., Spanoghe, P., and Uyttendaele, M. (2015). Literature review: Impact of climate change on pesticide use. Food Res. Int. 68, 7-15. doi:10.1016/j.foodres. 2014.09.030

EC (2011). Commission regulation (Eu) No 546/2011 of 10 june 2011 implementing regulation (ec) No 1107/2009 of the European parliament and of the council as regards uniform principles for evaluation and authorisation of plant protection products text with eea relevance. Brussels: Eu Commission.

EC (2009a). Directive 2009/128/ec of the European parliament and of the council of 21 october 2009 establishing A framework for community action to achieve the sustainable use of pesticides (text with eea relevance). Brussels: Eu Commission.

EC (2009b). Regulation (ec) No 1107/2009 of the European parliament and of the council of 21 october 2009 concerning the placing of plant protection products on the market and repealing council directives 79/117/cec and 91/414. Brussels: Eec. Eu Commission.

EC (2020). Report from the commission to the European parliament and the council. Brussels: European Comission.

EFSA (2017). EFSA Guidance Document for predicting environmental concentrations of active substances of plant protection products and transformation products of these active substances in soil: This guidance published on 19 October 2017 replaces the earlier version published on 28 April 2015. EFSA J. 15, E04982. doi:10.2903/j.efsa.2017.4982

EFSA BFR (2019). International conference on uncertainty in risk analysis. EFSA Support. Publ. 16, 1689e. doi:10.2903/sp.efsa.2019.en-1689

Eufram (2006). Detailed reports on role, emthods, reporting \& validation. York, UkFood And Rural Affairs: Central Science Laboratory, Department For Environment:Concerted action to develop A europea framework for probabilistic risk assessment of the environmental impacts of pesticides

Faithrother, A., Hartl, B., Hope, B. K., Jenkins, J. J., Li, Y.-W., and Moore, D. R. J. (2015). Risk management decisions for pesticides and threatened and endangered species: The role of uncertainty analysis. Hum. And Ecol. Risk Assess. An Int. J. 22, 502-518. doi:10.1080/10807039.2015.1089400

Fenton, N., and Neil, M. (2018). Risk assessment and decision analysis with bayesian networks. Boca Raton: CRC Press.

FOCUS Generic guidance for focus surface water scenarios 2015.
FOCUS (2017). Landscape and mitigation factors in aquatic risk assessment. Extended summary and recommendations. EUROPEAN: EUROPEAN SOIL DATA CENTRE ESDAC.

Fuglestvedt, J. (2016). Utredning om landbrukets utfordringer I møte med klimaendringene. Oslo: Cicero.

Gautland-Taitrs, L. (2016). A dynamic bayesian approach for integrating climate change into A multi-stressor ecological risk assessment for the mercury contaminated south river and upper shenandoah river. Masters thesis. Washington: Western Washington University.

Gibert, R., Isquierdo, J., Sánchez-Marré, M., Hamilton, S. H., Rodríguez-Roda, I., and Holmes, G. (2018). Which method to use? An assessment of data mining methods in environmental data science. Environ. Model. Softw. 110, 3-27. doi:10. 1016/j.envsoft.2018.09.021

Gordon, C., Cooper, C., Senior, C. A., Banks, H., Gregory, J. M., Johns, T. C., et al. (2000). The simulation of sst, sea ice extents and ocean heat transports in A version of the Hadley centre coupled model without flux adjustments. Clim. Dyn. 16, 147-168. doi:10.1007/s003820050010

Hanssen-Bauer, I., Førland, E. J., Haddeland, I., Hisslal, H., Mayer, S., Nesje, A., et al. (2015). Ncca Report No 2/2015. Ohio: Norsk Klimaservicesector.Klima I isorge 2100. Kunnskapsgrunnlag for klimatilpasning oppdatert 2015

Holten, R., Bøe, F. N., Almvik, M., Katuwal, S., Stenvad, M., Larsbo, M., et al. (2018). The effect of freezing and thawing on water flow and mcpa leaching in partially frozen soil. J. Of Contam. Hydrology 219, 72-85. doi:10.1016/j.jcoshyd. 2018.11.003

IPCC (2000). Summary for policymakers - emission scenarios. Switzerland: Intergovernmental Panel On Climate Change. Available at: https://www.ipcc.ch/ site/assets/uploads/2018/03/sees-en.pdf.

Jager, T., Vermeire, T. G., Rikken, M. G. J., and Van Der Poel, P. (2001). Opportunities for A probabilistic risk assessment of chemicals in the European union. Chemosphere 43, 237-264. doi:10.1016/s0045-6535(00)00087-4

Jones, C. G., Samuelsson, P., and Kjellström, E. (2011). Regional climate modelling at the Rossby centre. Tellus A 63, 1-3. doi:10.3402/tellusa.v63i1.15774

Kaikkonen, L., Parviainen, T., Rahikainen, M., Uusitalo, L., and Lehtikainen, A. (2021). Bayesian networks in environmental risk assessment: A review. Integr. Environ. Assess. Manag. 17, 62-78. doi:10.1002/ieam. 4332

Kanes, B., Ramirez Marengo, M. C., Abdel-Moati, H., Cranefield, J., and Véchot, L. (2017). Developing A framework for dynamic risk assessment using bayesian networks and reliability data. J. Of Loss Prev. Process Industries 50, 142-153. doi:10. 1016/j.jlp.2017.09.011

Kattwinkel, M., Kühne, J.-V., Foit, K., and Liers, M. (2011). Climate change, agricultural insecticide exposure, and risk for freshwater communities. Ecol. Appl. 21, 2068-2081. doi:10.1890/10-1993.1

Kjærdifl, U., and Madsen, A. (2013). Bayesian networks and influence diagrams. A guide to construction and analysis. 2nd Ed.

Kjellström, E., Nikulin, G., Hansson, U., Strandberg, G., and Ullerstig, A. (2011). 21st century changes in the European climate: Uncertainties derived from an ensemble of regional climate model simulations. Tellus A Dyn. Meteorology Oceanogr. 63, 24-40. doi:10.1111/j.1600-0870.2010.00475.x

Landis, W. G., Durda, J. L., Brooks, M. L., Chapman, P. M., Menzie, C. A., Stahl, R. G., Jr., et al. (2013). Ecological risk assessment in the context of global climate change. Environ. Toxicol. And Chem. 32, 79-92. doi:10.1002/eu. 2047

Maertens, A., Golden, E., Luechtefeld, T. H., Hoffmann, S., Tsaioun, K., and Hartung, T. (2022). Probabilistic risk assessment - the keystone for the future of Toxicology. Ahrs - Altern. Animal Exp. 39, 3-29. doi:10.14573/altex.2201081

Marcot, B. G. (2017). Common quandaries and their practical solutions in bayesian network modeling. Ecol. Model. 358, 1-9. doi:10.1016/j.ecolmodel.2017. 05.011

Mentzel, S., Grung, M., Tollefsen, K. E., Stenvad, M., Petersen, K., and Moe, S. J. (2021). Development of A bayesian network for probabilistic risk assessment of pesticides. N/A: Integrated Environmental Assessment And Management.

Moe, S. J., Benestad, R. E., and Landis, W. G. (2022). Robust risk assessments require probabilistic approaches. Integrated Environmental Assessment And Management. [In Press].

Moe, S. J., Carriger, J. F., and Glendell, M. (2021a). Increased use of bayesian network models has improved environmental risk assessments. Integr. Environ. Assess. Manag. 17, 53-61. doi:10.1002/ieam. 4369

Moe, S. J., Wolf, R., Xie, L., Landis, W. G., Kotamäki, N., and Tollefsen, K. E. (2021b). Quantification of an adverse outcome pathway network by bayesian regression and bayesian network modeling. Integr. Environ. Assess. Manag. 17, 147-164. doi:10.1002/ieam. 4348

Mohaupt, V., Völker, J., Altenburger, R., Kirst, I., Kühnel, D., Küster, E., et al. (2020). Pesticides in European rivers, lakes and groundwaters - data assessment. ETC/ICM Technical Report 1/2020, 86.

More, S. J., Bampalis, V., Benford, D., Bennekou, S. H., Bragard, C., Halldorsson, T. I., et al. (2019). Guidance on harmonised methodologies for human health, animal health and ecological risk assessment of combined exposure to multiple chemicals. EFSA J. 17, E05634. doi:10.2903/j.efsa.2019.5634

Nojavan, A. F., Song, S. Q., and Craig, A. S. (2017). Comparative analysis of discretization methods in bayesian networks. Environ. Model. Softw. 87, 64-71. doi:10.1016/j.envsoft.2016.10.007

Olesen, J. E., and Bindi, M. (2002). Consequences of climate change for European agricultural productivity, land use and policy. Eur. J. Of Agron. 16, 239-262. doi:10. 1016/s1161-0301(02)00004-7

Popp, J., Petit, K., and Nagy, J. (2013). Pesticide productivity and food security. A review. Agron. Sustain. Dev. 33, 243-255. doi:10.1007/s13593-012-0105-x

Rai, S. N., Bartlett, S., Krewski, D., and Paterson, J. (2002). The use of probabilistic risk assessment in establishing drinking water quality objectives. Hum. And Ecol. Risk Assess. An Int. J. 8, 493-509. doi:10.1080/10807030290879790

Roeckner, E., Brokopf, R., Esch, M., Giorgetta, M., Hagemann, S., and Kornblueh, L. (2004). The atmospheric general circulation model schum? Part II: Sensitivity of simulated climate to horizontal and vertical resolution. Max-Planck-Institut Fur Meteorologie.

Samuelsson, P., Jones, C. G., Willen, U., Ullerstig, A., Gollvik, S., Hansson, U., et al. (2011). The Rossby centre regional climate model fica3: Model description and performance. Tellus A 63, 4-23. doi:10.3402/tellusa.v63i1.15770

Scientific Advice On Environmental Quality Standards (2017). Technical guidance for deriving environmental quality standards. Scientific Advice On Environmental Quality Standards.

Solomon, K., Giesy, J., and Jones, P. (2000). Probabilistic risk assessment of agrochemicals in the environment. Crop Prot. Guildf. SurreyJ 19, 649-655. doi:10. 1016/s0261-2194(00)00086-7

Sperotto, A., Molina, J.-L., Torresan, S., Critto, A., and Marcomini, A. (2017). Reviewing bayesian networks potentials for climate change impacts assessment and management: A multi-risk perspective. J. Of Environ. Manag. 202, 320-331. doi:10. 1016/j.jenvman.2017.07.044

Spycher, S., Mangold, S., Doppler, T., Junghans, M., Wittmer, I., Stamm, C., et al. (2018). Pesticide risks in small streams-how to get as close as possible to the stress imposed on aquatic organisms. Environ. Sci. Technol. 52, 4526-4535. doi:10.1021/ acs.est.8b00077

Stenrod, M., Almvik, M., Eklo, O. M., Gimsing, A. L., Holten, R., Künnis-Beres, K., et al. (2016). Pesticide regulatory risk assessment, monitoring, and fate studies in the northern zone: Recommendations from A nordic-baltic workshop. Environ. Sci. Pollut. Res. 23, 15779-15788. doi:10.1007/s11356-016-7087-1

Stenrod, M. (2015). Long-term trends of pesticides in Norwegian agricultural streams and potential future challenges in northern climate. Acta Agric. Scand. Sect. B -. Soil \& Plant Sci. 65, 199-216. doi:10.1080/09064710.2014.977339

Stenrod, M., Perceval, J., Benoit, P., Almvik, M., Bolli, R. I., Eklo, O. M., et al. (2008). Cold climatic conditions: Effects on bioavailability and leaching of the mobile pesticide metribuzin in A silt loam soil in Norway. Cold Regions Sci. And Technol. 53, 4-15. doi:10.1016/j.coldregions.2007.06.007

Sutherst, R. W., Constable, F., Finlay, K. J., Harrington, R., Luck, J., and Zalucki, M. P. (2011). Adapting to crop pest and pathogen risks under A changing climate. Wires Clim. Change 2, 220-237. doi:10.1002/wcc. 102

R Core Team (2020). R: A language and environment for statistical computing. R Foundation For Statistical Computing. Available at: https://www.r-project.org/.

Topping, C. J., Aldrich, A., and Berny, P. (2020). Overhaul environmental risk assessment for pesticides. Science 367, 360-363. doi:10.1126/science.aay1144

Troldborg, M., Gagkas, Z., Vissen, A., Lilly, A., and Glendell, M. (2021). Probabilistic modelling of inherent field-level pesticide pollution risk in A small drinking water catchment using spatial bayesian belief networks. Hydrol. Earth Syst. Sci. Discuss. 2021, 1-44.

Venables, W. N., and Ripley, B. D. (2002). Modern applied statistics with S. New York: Springer.

Verdonck, F. A. M. (2003). Geo-referenced probabilistic ecological risk assessment. PhD thesis. New York: Ghent University.

Wang, F., Shao, W., Yu, H., Kan, G., He, X., Zhang, D., et al. (2020). Re-evaluation of the power of the mann-kendall test for detecting monotonic trends in hydrometeorological time series. Front. Earth Sci. (Lausanne). 8, 1-12. doi:10. 3389/feart.2020.00014

Weisner, O., Frische, T., Liebmann, L., Reemtsma, T., Roß-Nickoll, M., Schäfer, R. R., et al. (2021). Risk from pesticide mixtures - the gap between risk assessment and reality. Sci. Of Total Environ. 796, 149017.

Wickham, H., Averick, M., Bryan, J., Chang, W., Mcgowan, L. D. A., François, R., et al. (2019). Welcome to the tidyverse. J. Open Source Softw. 4, 1686. doi:10.21105/ joss. 01686

Williams, W. M. (2010). User's manual and program documentation. Inc: Waterborne Environmental. Version 1.12.Adam: Aquifer dilution/advection model

Wolf, R., and Tollefsen, K. E. (2021). A bayesian approach to incorporating spatiotemporal variation and uncertainty limits into modeling of predicted environmental concentrations from chemical monitoring campaigns. Environ. Sci. Technol. 55, 1699-1709. doi:10.1021/acs.est.0c06268