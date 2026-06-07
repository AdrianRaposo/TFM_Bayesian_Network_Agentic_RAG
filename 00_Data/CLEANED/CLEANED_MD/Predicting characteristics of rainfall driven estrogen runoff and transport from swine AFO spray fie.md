# HHS Public Access 

Author manuscript
Sci Total Environ. Author manuscript; available in PMC 2017 May 12.
Published in final edited form as:
Sci Total Environ. 2015 November 01; 532: 571-580. doi:10.1016/j.scitotenv.2015.06.051.

## Predicting Characteristics of Rainfall Driven Estrogen Runoff and Transport from Swine AFO Spray Fields

Boknam Lee ${ }^{\mathrm{a}, 1}$, Seth W. Kullman ${ }^{\text {b }}$, Erin E. Yost ${ }^{\text {b, }}$, Michael T. Meyer ${ }^{\text {c }}$, Lynn Worley-Davis ${ }^{\text {d }}$, C. Michael Williams ${ }^{\mathrm{d}}$, and Kenneth H. Reckhow ${ }^{\mathrm{a}}$<br>${ }^{a}$ Nicholas School of the Environment, Duke University, Durham, North Carolina, 27708, USA<br>${ }^{\text {b }}$ Department of Biological Sciences, Program in Environmental and Molecular Toxicology, North Carolina State University, Raleigh, North Carolina, 27695, USA<br>${ }^{\text {c }}$ Organic Geochemistry Research Laboratory, U.S. Geological Survey (USGS), Lawrence, Kansas, 66049, USA<br>${ }^{\mathrm{d}}$ Prestage Department of Poultry Science, North Carolina State University, Raleigh, North Carolina, 27695, USA


#### Abstract

Animal feeding operations (AFOs) have been implicated as potentially major sources of estrogenic contaminants into the aquatic environment due to the relatively minimal treatment of waste and potential mobilization and transport of waste components from spray fields. In this study a Bayesian network (BN) model was developed to inform management decisions and better predict the transport and fate of natural steroidal estrogens from these sites. The developed BN model integrates processes of surface runoff and sediment loss with the modified universal soil loss equation (MUSLE) and the soil conservation service curve number (SCS-CN) runoff model. What-if scenario simulations of lagoon slurry wastes to the spray fields were conducted for the most abundant natural estrogen estrone (E1) observed in the system. It was found that E1 attenuated significantly after 2 months following waste slurry application in both spring and summer seasons, with the overall attenuation rate predicted to be higher in the summer compared to the spring. Using simulations of rainfall events in conjunction with waste slurry application rates, it was predicted that the magnitude of E1 runoff loss is significantly higher in the spring as compared to the summer months, primarily due to spray field crop management plans. Our what-if scenario analyses suggest that planting Bermuda grass in the spray fields is likely to reduce runoff losses of natural estrogens near the water bodies and ecosystems, as compared to planting of soybeans.


[^0]
[^0]:    ${ }^{1}$ Corresponding author: Boknam Lee, College of Agriculture and Life Sciences, Seoul National University, 1 Gwanak-ro, Gwanakgu, Seoul, South Korea, leeboknam@gmail.com, Tel: +82-(0)10-8909-7753.
    ${ }^{1}$ Present Addresses: College of Agriculture and Life Sciences, Seoul National University, 1 Gwanak-ro, Gwanak-gu, Seoul, South Korea
    ${ }^{2}$ Present Addresses: Oak Ridge Institute for Science and Education at the U.S. Environmental Protection Agency, National Center for Environmental Assessment, U.S. Environmental Protection Agency, Research Triangle Park, NC, USA

Keywords

Estrogen runoff and transport, Bayesian network model, Swine animal feeding operation, Spray fields

## 1. Introduction

The land application of animal wastes has been widely adopted as a waste management practice for swine animal feeding operations (AFOs) in the United States as well as worldwide (Bradford et al. 2008). Animal manure typically contains elevated levels of natural steroidal hormones (Hanselman et al. 2003), which are endogenous to livestock and are excreted in urine and feces. Following land application of manure, numerous reports find that steroidal estrogens, including 17β-estradiol (E2), estrone (E1), and estriol (E3), may reach aquatic environments through surface water runoff (U.S. EPA, 1998; Shore and Shemech, 2003; Hanselman et al. 2003; Johnson et al. 2006; Bradford et al. 2008). Due to their strong potency as endocrine disrupting chemicals, these estrogenic hormones can be hazardous to aquatic organisms, causing the development of intersex and other physiological dysfunctions in fish populations (Hansen et al. 1998; Jobling et al. 1998; Leet et al. 2011).

While the potential effects of steroidal estrogens on aquatic populations are well established (Sellin et al. 2011; Leet et al. 2012), few studies have investigated the mobilization and transport of these compounds from AFO spray fields following rainfall-induced runoff events (Shappell et al. 2010; Zhao et al. 2010; Gall et al. 2014). Therefore, there is limited understanding of how the surface runoff and transport of estrogens from AFO point sources may be affected by various combinations of environmental variables, such as lagoon slurry application rates, weather, crop management, and soil characteristics.

Computer simulation models have been developed and applied to quantify field-scale or watershed-scale pollutant transport and runoff from agricultural lands (Dabrowski et al. 2002; Vadas et al. 2007). However, commonly used models, such as SWAT (Arnold et al. 1998), ANSWERS (Bouraoui and Dillaha, 1996), GLEAMS (Leonard et al. 1987), or EPIC (Williams et al. 1983) do not have the capability to simulate the process of estrogen transfer from surface application of manure to runoff. Moreover, there are no such models to account for the variation and uncertainty of runoff transport that may be caused by site-specific variables.

Previously our group developed a Bayesian network (BN) model to assess fate and transport of natural estrogen in a compartmentalized Swine Waste Lagoon (Lee et al. 2014). In this study we further our assessment of estrogen fate through development of a BN model to characterize estrogen losses through surface runoff and sediment transport from swine manure spray fields. We have established an integrated BN model that incorporates fundamental components of the soil loss model, a modified universal soil loss equation (MUSLE) (Williams, 1975), and the surface runoff model, a soil conservation service curve number (SCS-CN) (Mockus, 1972). This combined approach enables both characterization and quantification of estrogen mobility as a function of major transport processes, while propagating the uncertainties through both mechanistic and probabilistic model components

to affect the fate and transport of estrogens. Based on probabilistic outputs, the magnitude of off-site movement of estrogens and the potential environmental significance can be assessed.

The integrated BN model, developed in this study, utilizes estrogen concentration data from soil at a commercial swine farrowing AFO. Previous studies by our group have found that E1, a potent steroidal estrogen, is the most abundant estrogen species in waste at this field site (Yost et al. 2013, 2014; Lee et al. 2014). Therefore, this study focuses on E1 as a case study to investigate the characteristics of estrogen runoff and transport from AFO spray fields. The potential effects of site-specific variables on the magnitude of E1 runoff and transport were assessed by the extensive what-if scenario analyses using the BN model, and the major outcomes are presented herein. Variables assessed in our model include estrogen persistence in soil, irrigation rate of lagoon slurry waste, rainfall characteristics, soil organic carbon, vegetative cover, and farming practices.

## 2. Methods

### 2.1. Study Area

The study site consists of a total of 491,288 m^{2} of spray fields surrounding a commercial swine farrowing facility in southeastern North Carolina, centrally located in the swine production region of the state (Supplemental data, Fig. S1.1). Crops such as soybeans, wheat, corn, and Bermuda grass are rotated and grown on specific spray fields according to the season and site specific nutrient management plans. Land application of lagoon slurry to the fields is designed to maintain the level of primary waste lagoons at approximately two feet below freeboard, and is performed between 20,000 gal/ha (7.6 L/m^{2}) and 60,000 gal/ha (22.7 L/m^{2}) under the guidelines of a nutrient management plan. Slurry land applications occur regularly throughout the crop growing season (March to October), with no land application of slurry during the fallow winter season (November -- February). As a result of these factors, the frequency and volume of slurry land application varies as a function of lagoon management, nutrient management, season, rainfall, and crop type.

According to geographic information system (GIS) analysis using the USDA-NRCS soil dataset, the major soil type in the spray fields at this site is fine-loamy soil, though the site also includes sandy, fine, loamy, and coarse-loamy soils. The soil erodibility varies from 0.02 to 0.32, based on the USDA-NRCS Soil Data Mart (USDA, 2011). The field site is relatively flat, with a slope distribution ranging from 0.004% to 2.2% based on the analysis of the digital elevation model (DEM). Using the national hydrography dataset (NHD) (USGS, 2011), a map of water bodies near our spray fields verified that there are no streams adjacent to our field site. However, marshes and canal ditches are located on the downside of the field site, and may potentially be affected by runoff. Throughout the study period, the intensity of rainfall ranged between 2.5 and 86.4 mm/d; most of the major precipitation had an intensity of less than 25.4 mm/d based on four years of daily precipitation data, obtained from the National Climatic Data Center (NCDC) (NCDC, 2011).

2.2. Sample Collection and Estrogen Analysis

#### Abstract

Lagoon sampling—Extensive sampling of the lagoon was conducted on June 15, 2009 and April 14, 2010. Eight coordinates on the lagoon were chosen in order to create a representative cross-section of the site: 3 locations were near the outflow pipes from the barns, 4 were in the middle of the lagoon, and 1 was at the far end of the lagoon. At each coordinate, 1-liter samples were collected at 3 different depths of slurry (15 cm below the surface, 30 cm below the surface, and 15 cm above the level of the sludge) using a horizontal beta water sampler (Wildlife Supply Company, Yulee, FL) (Yost et al., 2013).

Soil sampling—Sampling of spray field soil was conducted in the spring of 2010. Soil sampling commenced following the land application of lagoon slurry by the AFO managers, which was performed on March 17, 2010. Samples were collected the day of land application, 1 day post-application, 7 days post-application, and 60 days post-application. During this sampling period, the field was planted with wheat, which had been sown in early 2010. On all sampling dates, the top 15 cm of soil was collected from 13 coordinates spanning a broad transect of the field. Soil was stored on ice immediately upon collection, and transferred to $-20^{\circ} \mathrm{C}$ upon return to North Carolina State University. In addition to estrogen analysis, described below, the soil organic carbon content was assessed and used to estimate the estrogen adsorption coefficient $\left(K_{d}\right)$ (Supplemental data, Fig. S2.1) (Yost et al., 2014).

LC/MS-MS Analysis of Slurry Wastes and Soil—Lagoon slurry was extracted using solid phase extraction (SPE), and soil was extracted using accelerated solvent extraction followed by SPE. Extracts were assessed for E2, E1, and E3 using liquid chromatography/ tandem mass spectroscopy (LC/MS-MS), using the detailed procedure described in the supplemental data for sample analysis (S1.1 and S1.2) (Yost et al., 2014).

Concentrations of natural steroidal estrogens in lagoon slurry and soil are presented in the supplementary data (Fig. S1.2 and Table S1.1). Analyte recovery using our extraction methodology was found to be $>90 \%$ for E1, E2, and E3, indicating the strong recovery of analytes from both aqueous and solid phases (Yost et al., 2013). Since E1 was found to be by far the most abundant estrogen metabolite in both lagoon and soil, the BN model was developed to predict the characteristics of E1 runoff and transport. For input into the BN model, measured E1 concentrations in slurry were used to derive the probability distribution of E1 in spring (April) and summer (June) for the node of slurry estrogen concentration. Measured E1 concentrations in soil following the land application of slurry were used to estimate the distribution of the E1 attenuation rate in soil, as explained in section 2.3.4 and supplemental data of S3.1.

### 2.3. Development of Estrogen Runoff Bayesian Network Model

In this study, the physically-based mechanistic models describing the estrogen runoff and transport given a rainfall event were adopted and integrated to develop the BN structures and parameters since there are scarce data to develop the BN model directly. Here, the theoretical background and development process of the estrogen runoff BN model are presented in detail. The general overview of BN is provided in the supplemental data of

S2.1. The HUGIN software (Hugin EXPERT, 1998) was used to implement both parts for the BN development.

### 2.3.1. Mathematical Overview of Estrogen Transport in Surface Runoff and Soil Erosion

The conceptual structure of the estrogen runoff model was derived by establishing a mass balance of estrogens in the top 1 cm of soil in the spray fields. Particularly, in this study, the pesticide model described by Haith (1980) was adopted to describe estrogen concentrations in runoff water and in spray field soils after rainfall events. The mathematical equations presented below were used to quantify the relationships between variables as conditional distributions in the BNs.

After the lagoon slurry is applied to the spray field, the amount of estrogen lost with each runoff event is dependent upon the estrogen remnant on the spray fields. In the model, it is considered that the estrogens that percolated below the top soil are not available for runoff and that the active runoff zone is within the first 1 cm of soil as shown in Fig. 1 (Haith, 1980; Donigian and Crawford, 1976; Rhode et al. 1980). Since estrogens decrease exponentially in the soil (Supplemental data, Fig. S3.4), the residues of the estrogen mass in the top soil can be estimated by an exponential decay rate with time if a rainstorm occurs t days after slurry application, as follows:

$$
E t=E o \exp (-\alpha t)
$$

where Et is the estrogen mass in the surface soil (kg/ha); Eo is the initial estrogen content of the top surface soil layer immediately after application (kg/ha), which is usually equal to the application rate; and α is the estrogen degradation rate (day-1), which was estimated based on the observed data in the soil (Supplemental data, Fig. S3.4). In this model, it is assumed that estrogen degradation is independent of soil pH, soil moisture content, temperature, and ambient conditions to develop more reliable BN.

The estrogen runoff losses are estimated by two major transport events, surface runoff and soil erosion, in terms of two different forms of estrogens: dissolved forms (Es) in runoff water and adsorbed forms (Ew) in the eroded soil particles (Fig. 1). Therefore, the total estrogen available for runoff (Et) is the sum of the two forms of estrogen mass, which can be described by a linear adsorption coefficient, K_{d}, as follows:

$$
E t=E s+E w
$$

$$
\mathrm{e}_{\mathrm{s}}=K_{\mathrm{d}} * \mathrm{e}_{\mathrm{w}}
$$

where Es and Ew are potentially available adsorbed and dissolved forms; and e_{s} and e_{w} are adsorbed and dissolved estrogen concentrations on soil particles (mg/kg) and in soil water (mg/L), respectively.

The potentially available adsorbed and dissolved estrogen levels for runoff can be obtained by combining the function of soil properties as follows:

$$
E s=E t /\left(1+\Theta / K_{d} * \rho\right)
$$

$$
E w=E t /\left(1+\left(K_{d} * \rho / \Theta\right)\right)
$$

where $\Theta$ is available water capacity $(\mathrm{cm} / \mathrm{cm})$; and $\rho$ is soil bulk density $(\mathrm{g} / \mathrm{cm})$.
Consequently, the actual adsorbed (Ers) and dissolved (Erw) estrogen runoff losses are calculated by the relationships with runoff $(Q)$, rainfall $(P)$, and soil loss $\left(S_{l}\right)$ :

$$
\begin{gathered}
\text { Ers }=\left(S_{l} / 100 * \rho\right) * E s \\
\text { Erw }=(Q / P) * E w
\end{gathered}
$$

For the dissolved estrogen runoff loss, Es will be distributed into runoff, percolation, and available soil water. It is assumed that the distribution of rainfall into these three pathways is proportional. In this model, the modified universal soil loss equation (MUSLE) is used to estimate the soil loss $\left(S_{l}\right)$ by a rainfall event on day t (Williams, 1975):

$$
S_{l}=(11.8 / A)(\text { Vtqt })^{0.56} K(L S) \mathrm{CSP}
$$

where $K, L S, C$ and $S P$ are the standard soil erodibility, topographic, cover, and supporting practice factors, respectively; $A$ is the field area (ha); $V t$ is the runoff volume $\left(\mathrm{m}^{2}\right)$; and $q t$ is the peak runoff $\left(\mathrm{m}^{2} / \mathrm{sec}\right)$. The runoff $(Q)$ is estimated by the soil conservation service curve number equation (SCS-CN) (Mockus, 1972):

$$
Q=(P-0.2 S)^{2} /(P+0.8 S)
$$

where P is rainfall $(\mathrm{mm}) ; S$ is a retention parameter $(\mathrm{mm})$, which is a function of soil, crop management, and antecedent rainfall.

Finally, the total estrogen remaining (Etr) in the surface soil after the rainstorm is given by:

$$
\text { Etr }=E t-\text { Ers }- \text { Erw }
$$

2.3.2. Development of the Estrogen Runoff Bayesian Network Structure-The BN structures were constructed to represent the process of estrogen runoff driven by a

rainfall event for two rainy seasons, including spring and summer, respectively, using Hugin software (Hugin EXPERT, 1998). Each BN model structure consists of three main parts interlinked, including estrogen in spray fields before rainfall, estrogen transport process, and estrogen in spray fields and runoff water after rainfall. The main model nodes were derived from the components of mass balance equations of estrogen transport processes explained in the above section of 2.3.2 and connected by the causal relationships (Fig. 2).

Within the section of estrogen before rainfall, the estrogen mass in spray fields before rainfall is designed to be modeled by both the application rate of lagoon slurry and the estrogen decay rate in spring and summer. Thus, this structure provides to measure the persistence of estrogen compounds in the spray fields by means of the probability distribution of predicted changes in estrogen concentrations as a result of the amount of land application of slurry wastes as well as the degradation rate of estrogen compounds for each season. In the section of estrogen transport, the processes of estrogen runoff (dissolved estrogens) and soil transport (adsorbed estrogens) by rainfall events were structured by incorporating the nodes of SCS-CN runoff and MUSLE soil erosion for each season. In the model, the effect of rainfall magnitude on estrogen runoff mass is delivered through the connection with the surface runoff node in the SCS-CN. The relationship with soil loss is then connected through a runoff node to a peak runoff model component (qt), which is implicitly represented in MUSLE (Supplemental data, Fig. S2.1). Since the estrogen loss by soil erosion is also a function of land management and conservation practice nodes, the integration of MUSLE model components in the BN provides a way to assess the most effective management practice to reduce the estrogen loss for the corresponding season by simulating a “what-if” analysis. The effect of crop management on the surface runoff is characterized and quantified by the connection to a curve number node, which is affecting the magnitude of surface runoff loss. Finally, the probability of estrogen mobility can be predicted by the model endpoints, which are the estrogen concentration remaining in the soil and in the runoff water after rainfall. It is believed that this model structure will help to guide long-term management strategies for estrogen runoff in the soil and receiving runoff water.

### 2.3.3. Quantification of the Estrogen Runoff Bayesian Network Parameter

After constructing the BN structure, the next step was to quantify the strength of causal relationships between the variables by assigning marginal and conditional probabilities. Prior to parameterization, all variables were first discretized to have numeric or categorical intervals, as required for use of the Hugin software. In this study, variables were defined as numeric interval or categorical type nodes. The numeric marginal variables were discretized into four to eleven states with equal or quantile intervals based on the consideration of observed data distribution. The categorical variables (i.e. Crop, Erosion Control Practice, Antecedent Soil Moisture, and Runoff (Y/N)) were divided into two to three categories (Supplemental data, S3.2). For the intermediate nodes, quantile intervals were used for a better accuracy of model prediction (Alameddine et al. 2011). After discretization, all nodes were assigned to have defined probability distributions. The marginal probabilities were assigned for the parentless nodes (e.g. slurry estrogen concentration, irrigation application rate, estrogen decay rate, etc.) to represent the prior knowledge about frequencies of each state based on the observed data or expert elicitation (Supplemental data, S3.1). The

conditional probability distributions were generated for intermediate nodes using the mathematical equations presented in the above overview or the defined probability distributions. Fig. S2.1 in supplemental data describes where major equations are embedded to specific nodes. Based on these equations, the conditional distributions were generated by means of Monte Carlo simulation in the HUGIN software. In other words, the probabilities of each state of the child nodes, conditioned on every possible combination of states of its parent nodes, were calculated explicitly by generating a number of samples within each interval and estimating the frequency for the corresponding states. In this way, the model uncertainties derived from the mechanistic models, including the SCS-CN runoff model and MUSLE model, can be captured in the probability frequency distributions. For the conditional distributions of model variables (Land Management Factor, Conservation Practice Factor, Curve Number, Storage Parameter, and Runoff (Y/N)), which are the components of MUSLE and SCS-CN runoff models, the defined probability distributions were specifically used to propagate the probability distributions given the relationships with other model nodes. A more detailed explanation of the quantification of model nodes is provided in the supplemental data (S3.1 and S3.2).

In the absence of data to verify our model, we describe a number of “what-if” analysis scenarios in the next section. While it is unfortunate that sufficient data do not exist at present for a rigorous assessment of the BN model, we must emphasize that the importance of the problem we addressed is obvious. To examine management strategies for natural estrogens from AFOs, the alternative is seat-of-the-pants judgment. Our BN model has a scientifically-defensible, logical structure; as a consequence this model is far superior to any existing alternatives for analysis of this issue.

## 3. Results and Discussion

The off-site transport of manure-borne estrogens from AFO spray fields may be affected by numerous variables, including slurry irrigation rate, rainfall, soil organic carbon, vegetative cover, farming practices, and estrogen degradation rate. In this study, we develop and apply a BN model to examine several “what-if” model scenarios, allowing us to assess the effects of these variables on predicted E1 runoff concentrations. The primary results of scenario simulations are presented below.

### 3.1. Characteristics of E1 Persistence in Soil before Rainfall

To assess the persistence of E1 in spray field soil before a rainfall event (during spring and summer seasons), a “what-if” scenario analysis of E1 persistence in spray field soil was performed using the BN model at 0, 1, 7, and 60 days following slurry applications (Fig. 3). Results of the analysis predicted that E1 concentrations will be significantly attenuated after 60 days following slurry waste application in both spring and summer seasons. For instance, the probability that E1 concentrations will be below 250 µg/ha (0.025 µg/m^{2}) in the spring is around 80% at 60 days after irrigation, as compared to the E1 concentration distribution of 1,200,000--2,500,000 µg/ha (120--250 µg/m^{2}) following the initial irrigation (Fig. 3(a)). In the summer, the probability that E1 concentrations would be below 250 µg/ha (0.025 µg/m^{2}) is almost 100 % at 60 days after irrigation (Fig. 3(b)). This indicates that the majority of E1

would be transformed, adsorbed, or mineralized within two months of irrigation. This pattern is consistent with laboratory studies that demonstrate attenuation of natural estrogens in soil due to degradation and sorption processes (Colucci et al. 2001; Colucci and Topp, 2002; Das et al. 2004). Particularly, the persistence of E1 in soil at 60 days post-application suggests that non-extractable and soil-bounds residues of E1, such as [4-^{14}C]-estrone, could be slowly mineralized (Colucci et al. 2001). The results of scenario simulations also suggest that the removal mechanisms of E1 (such as microbial degradation) could be more active in the summer than in the spring due to higher temperature.

### 3.2. Characteristics of E1 Runoff Loss by Seasonal Slurry Irrigation Rate in Connection with Nutrient Management Plans and Soil Moisture Condition

The predicted effect of slurry irrigation rate on the E1 runoff loss during spring and summer seasons was examined by three model scenario simulations in connection with nutrient management plans and soil condition. In these simulations, the growth of soybean and Bermuda grass was simulated in spring and summer, respectively, with buffer strip control practices according to our field-specific nutrient management plans (Supplemental data, Table S3.2). The antecedent soil moisture condition (AMC) was set by 25 % of AMC I, 50 % of AMC II, and 25 % of AMC III in spring, while the distribution of AMC in summer was 49.5 %, 50 %, and 0.5 % of AMC I, II, and III, respectively. For model simulations, “what-if” scenarios of three (low, medium, and high) magnitudes of slurry application rates per season were assessed. In each simulation, rainfall rate was fixed at 30--40 mm/d, occurring 7 days after slurry application (Fig. 4).

The model findings demonstrate that the variations in slurry application rates have a relatively small effect on the distributions of E1 runoff loss in summer (Fig. 5(b)). However, in the spring season, it was predicted that a higher magnitude of slurry application generates significantly more runoff losses of E1 up to 15000 µg/ha (1.5 µg/m^{2}) (Fig. 5(a)). This seasonal difference may be caused by different vegetation cover and antecedent soil moisture conditions in spray field soils, which change the magnitude of a runoff event. Since Bermuda grass has higher water holding capability (higher surface storage) than soybeans based on the retention parameter, which is a function of curve number, it was predicted that there could be approximately 3 times fewer significant runoff occurring in summer than in spring. Low runoff rates in summer could also be due to a low soil moisture condition, which promotes water retention in the subsurface soil and reduces the overall volume of surface runoff (Fig. 4).

Overall, the model findings suggest that Bermuda grass may be more resistant to surface runoff events given 30--40 mm/d of rainfall in our fields. This correspondingly implies that there could be lower risks of estrogen contamination in adjacent waterways and ecosystems in summer, given 30--40 mm/d of rainfall regardless of the application rates. Therefore, in spring, low slurry application may be preferred to prevent the high concentrations of estrogen runoff loss to the aqueous environment. Consequently, these findings indicate that E1 runoff loss in summer is less sensitive to irrigation application rate compared to the nutrient management and soil moisture condition than it in spring.

# 3.3. Characteristics of E1 Mass Transports under Different Rainfall Magnitudes 

Since the estrogen runoff loss is also a function of the variation in rainfall events, the effect of rainfall magnitude was investigated by simulating "what-if" scenarios for three magnitudes of rainfall events (low: $0-10 \mathrm{~mm} / \mathrm{d}$, medium: $30-40 \mathrm{~mm} / \mathrm{d}$, and high: $60-75$ $\mathrm{mm} / \mathrm{d}$ ) on the E1 runoff losses. The E1 runoff losses were assessed in terms of two different forms of E1, namely dissolved and adsorbed E1 forms in runoff water and eroded soil particles. Two different scenarios were assessed, one for the spring and the other for the summer season.

Results of this simulation suggest that overall, the higher the magnitude of the rainfall events, the greater E1 runoff losses are for both seasons (Fig. 6). However, the magnitude of E1 losses is much higher in the spring as compared to the summer for both medium and high rainfall events. For the low rainfall events, both seasons are predicted to generate a similar magnitude of E1 losses. The magnitude of E1 losses in terms of dissolved and adsorbed forms appears to have similar probability distributions at the E1 loss of above $10 \mu \mathrm{~g} / \mathrm{ha}$ $\left(0.001 \mu \mathrm{~g} / \mathrm{m}^{2}\right)$. In both seasons, overall the dissolved form of E1 losses is predicted to be more dominant than the adsorbed E1 phase under a high rainfall event. Under the low rainfall events, the magnitude of both forms of E1 loss appears to be similar regardless of seasons, where more than $80 \%$ of E1 losses are predicted to be below $10 \mu \mathrm{~g} / \mathrm{ha}(0.001 \mu \mathrm{~g} /$ $\mathrm{m}^{2}$ ).

Overall, the model findings indicate that E1 transport by soil erosion is greater than E1 transport by surface runoff during low rainfall events for both seasons. Higher magnitudes of rainfall produce more dissolved E1 loss through surface runoff; however the difference with the adsorbed form of E1 loss is relatively small. For seasonal variation of rainfall magnitudes, the model findings confirmed that the different vegetation types affect the distribution of E1 losses. In other words, Bermuda grass is more effective in preventing E1 runoff losses than is a soybean crop in our field site. This correspondingly implies that the E1 runoff loss is sensitive to curve number (CN) coefficients.

### 3.4. Characteristics of E1 Mass Transports under Different Soil Organic Carbon

The effect of soil organic carbon (SOC) contents on E1 runoff was evaluated by simulating "what-if" scenarios of E1 runoff loss in terms of adsorbed and dissolved E1 forms under $1.02,1.34$, and $1.89 \%$ of SOC observed from our field sites. In each simulation, a rainfall rate was set up at $30-40 \mathrm{~mm} / \mathrm{d}$, occurring 7 days after slurry application with soybean and Bermuda grass of nutrient management plans in spring and summer season, respectively.

The model findings demonstrate that the overall variability in the magnitude of E1 runoff loss is not significantly different across three different contents of SOC in both seasons. In the context of the magnitude of E1 runoff loss by season and E1 type, in spring, a dissolved E1 form was predicted to contribute more E1 loss at the above $2500 \mu \mathrm{~g} / \mathrm{ha}\left(0.25 \mu \mathrm{~g} / \mathrm{m}^{2}\right)$ while the adsorbed form of E1 loss is more dominant in the low concentrations of E1 loss (Fig. 7(a)). In summer, both forms of E1 loss were predicted to be predominant at the E1 loss of below $50 \mu \mathrm{~g} / \mathrm{ha}\left(0.005 \mu \mathrm{~g} / \mathrm{m}^{2}\right)$ since the magnitude of E1 runoff losses is predicted much lower than it in the spring (Fig. 7(b)). Overall, the distributions of E1 runoff loss

predicted show insignificant difference under the range of 1.02--1.89% of SOC in both seasons, implying that the SOC content in our field site is not a major environmental driver to affect the distribution of E1 runoff loss.

### 3.5. Sensitivity Analysis of Model Variables on E1 Runoff Loss

A sensitivity analysis was performed to verify the most influential variable for the prediction of E1 runoff loss among “what-if” scenario model variables simulated. We used the concept of mutual information to highlight sensitivity (Lee et al. 2014). In this analysis, we calculated mutual information for variables affecting El runoff loss in spring and summer season, respectively (Table 1). Table 1 illustrates that in spring, rainfall is the most significant driver to influence the E1 runoff loss, followed by curve number, decay rate, irrigation application rate and crops. In summer, the decay rate appears to have the greatest influence on E1 runoff loss, followed by the amount of rainfall, curve number, storage parameter and antecedent soil moisture condition. Outcomes of sensitivity analysis concur with the findings of the “what-if” scenarios simulated and confirm that seasonal variation in the magnitude of E1 runoff loss is mainly influenced by rainfall intensity, curve number (i.e. vegetation type), and decay rate. The results also verify that the irrigation application rate is comparably less significant than other natural and physical (i.e. rainfall and curve number) as well as chemical (i.e. decay rate) factors in both seasons. This indicates that the proper E1 runoff management should be implemented with the consideration of important environmental variables for each season to prevent further E1 losses.

## 4. Conclusions

Natural estrogen loss from AFOs spray fields to nearby aquatic ecosystems is becoming an environmental concern. However, there is a dearth of predictive models characterizing transport pathways of estrogen export from AFO spray fields. Additionally, current models are unable to predict interactions among variables including the irrigation application rate, seasonal variation, and rainfall intensity to assess the effect of management options on estrogen transport and fate.

Our study is the first attempt to model the characteristics of swine manure-borne estrogen runoff and transport from swine AFO spray fields. Using a BN model approach, estrogen mobility was probabilistically assessed as a function of estrogen persistence, irrigation rate, rainfall intensity, vegetative cover, farming practices, and soil organic carbon in swine manure spray fields. In the case study, the losses of E1, which was the most abundant estrogen species at our field site, was simulated for two rainy seasons, including spring and summer. High rates of slurry application and high intensity of rainfall events were predicted to be associated with a higher proportion of estrogen runoff in both seasons. In particular, the model simulations tell us that in our field site, the spring season could have greater risk of estrogen contamination to adjacent waterways and ecosystems compared to the summer season. This may be due to lower estrogen attenuation rates and less effective water holding capacity of the spring soybean crop compared to conditions in the summer season. Thus, lower slurry waste application may be recommended to reduce the magnitude of estrogen runoff loss during the spring season. In addition, planting the proper crop to hold more

runoff water and sediment would be helpful to reduce the risk of estrogen losses to the environment. Enhanced estrogen mineralization in the soil will also reduce estrogen levels for rainfall-runoff events.

In summary, the BN modeling framework provides an effective means to model a difficult yet important problem by integrating mechanistic considerations, observational data, and expert judgment. To test the robustness of this BN model further, the model scenarios may be tested using future sampling data. As scientific understanding and available data improve, an entirely mechanistic model of these processes may be possible for these systems. When data are limited, however, we believe that a BN makes best use of available information.

# Supplementary Material 

Refer to Web version on PubMed Central for supplementary material.

## Acknowledgments

This work was supported by the Environmental Protection Agency Science to Achieve Results (STAR) grant (R833420 to SWK) and the Environmental Protection Agency Science to Achieve Results (STAR) graduate fellowship (FP917151 to EY). We wish to thank the swine facility plant manager and crew for their assistance in sample collection and the facility owner/operator for providing access to the field site.
