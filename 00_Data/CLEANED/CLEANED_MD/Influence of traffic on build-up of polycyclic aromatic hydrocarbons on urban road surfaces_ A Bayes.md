# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Li, Yingxia, Jia, Ziliang, Mahappu Kankanamalage, Buddhi Wijesiri, Song, Ningning, \& Goonetilleke, Ashantha
(2018)

Influence of traffic on build-up of polycyclic aromatic hydrocarbons on urban road surfaces: A Bayesian network modelling approach.
Environmental Pollution, 237, pp. 767-774.
This file was downloaded from: https://eprints.qut.edu.au/123961/

## © Elsevier Ltd

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

License: Creative Commons: Attribution-Noncommercial-No Derivative Works 4.0

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1016/j.envpol.2017.10.125

# Influence of traffic on build-up of polycyclic aromatic hydrocarbons on urban road surfaces: A Bayesian Network modelling approach 

Yingxia $\mathrm{Li}^{1 *}$, Ziliang Jia ${ }^{1}$, Buddhi Wijesiri ${ }^{2 * *}$, Ningning Song ${ }^{1}$, Ashantha Goonetilleke ${ }^{2}$<br>${ }^{1}$ State Key Laboratory of Water Environment Simulation, School of Environment, Beijing Normal University, Beijing 100875, China<br>${ }^{2}$ Science and Engineering Faculty, Queensland University of Technology (QUT), GPO Box 2434, Brisbane, 4001, Queensland, Australia<br>yingxia@bnu.edu.cn; 201621180080@mail.bnu.edu.cn;<br>b.mahappukankanamalage@qut.edu.au; 201331180007@mail.bnu.edu.cn;<br>*Corresponding Author: Tel: 86-10-62205508; Email: yingxia@bnu.edu.cn<br>**Corresponding Author: Tel: 61-731381539; Email: b.mahappukankanamalage@qut.edu.au

## Graphical abstract

![img-0.jpeg](img-0.jpeg)

## Highlights

- Bayesian Network was developed to characterise the traffic impact on PAHs built-up.
- Traffic is a main source for PAHs on smaller particles on roads.
- Traffic is a key factor for re-distribution of PAHs on bigger particles.
- PAHs re-distribution is determined by particle size rather than chemical character
- Re-distribution of PAHs can contaminate the surrounding soils.

# ABSTRACT 

Due to their carcinogenic effects, Polycyclic Aromatic Hydrocarbons (PAHs) deposited on urban surfaces are a major concern in the context of stormwater pollution. However, the design of effective pollution mitigation strategies is challenging due to the lack of reliability in stormwater quality modelling outcomes. Current modelling approaches do not adequately replicate the interdependencies between pollutant processes and their influential factors. Using Bayesian Network modelling, this research study characterised the influence of vehicular traffic on the buildup of the sixteen US EPA classified priority PAHs. The predictive analysis was conditional on the structure of the proposed BN, which can be further improved by including more variables. This novel modelling approach facilitated the characterisation of the influence of traffic as a source of origin and also as a key factor that influences the re-distribution of PAHs, with positive or negative relationship between traffic volume and PAH build-up. It was evident that the re-distribution of particle-bound PAHs is determined by the particle size rather than the chemical characteristics such as volatility. Moreover, compared to commercial and residential land uses, mostly industrial land use contributes to the PAHs load released to the environment. Carcinogenic PAHs in industrial areas are likely to be associated with finer particles, while PAHs, which are not classified as human carcinogens, are likely to be found in the coarser particle fraction.

Keywords: Bayesian Networks, Pollutant build-up, Polycyclic Aromatic Hydrocarbons, Stormwater quality, Stormwater pollutant processes

Capsule: The Bayesian Network modelling approach adopted confirmed the influential role of traffic in the generation and re-distribution of PAHs on urban road surfaces

### 1.0 INTRODUCTION

Polycyclic Aromatic Hydrocarbons (PAHs) are a subset of the large group of hydrocarbons generated mainly through automobile use activities and other sources specific to urban land uses such as industrial activities. Exhaust emissions from incomplete combustion and leakages of fuel and lubricants release significant amounts of these toxicants into the urban environment ( Li et al., 2017; Mummullage et al., 2016a, 2016b; Pitt and Voorhees, 2004). PAHs build up on urban surfaces such as roads during dry weather periods, and are generally found in association with particulate solids. During rainfall events, the runoff transports these hydrocarbons into receiving waters, deteriorating urban water quality. Based on the carcinogenic effects of PAHs, US EPA has identified sixteen species of PAHs as priority pollutants which require specific mitigation in the context of urban stormwater pollution for safeguarding human and ecosystem health (Brown and Peake, 2006; Gobel et al., 2007; Herngren et al., 2005; Ma et al., 2017; Manoli and Samara, 1999).

The design of stormwater pollution mitigation strategies needs informed decision making that relies on stormwater quality models. However, the deterministic modelling approach that is commonly adopted in stormwater quality modelling does not adequately assist the decision makers to evaluate the influence of anthropogenic and environmental factors on the degradation of stormwater quality. This is due to the poor replication of the interdependencies between pollutant processes and their influential factors (Beck et al., 2017; Wijesiri et al., 2016; Zoppou, 2001). This highlights the need for modelling approaches that can be easily implemented, while generating reliable and adequate information for stakeholders and decision makers to understand and evaluate the problem of interest.

Bayesian Networks (BNs) is an emerging approach for modelling complex environmental systems and processes (Korb and Nicholson, 2010). This modelling approach enables the incorporation of

both, quantitative and qualitative data into a model and the quantitative evaluation of the interdependencies among model variables. BNs also enable the visual interpretation of a given problem. As such, BNs have been employed in a diversity of past studies in order to seek solutions to environmental problems such as adaptive management of bird habitats (Howes et al., 2010), catchment-based integrated water resources management (Chan et al., 2010), and assessing the influence of nutrients and climatic conditions on the occurrence of cyanobacterial blooms in water bodies (Rigosi et al., 2015). However, the wide ranging capabilities of BNs have not been exploited to their full potential in the case of stormwater pollution mitigation (Aguilera et al., 2011).

The research study discussed in this paper aimed to characterise the influence of vehicular traffic on the build-up of different PAH species, and to characterise this influence in relation to the type of land use. Accordingly, a BN modelling approach was employed to quantify the interdependencies between vehicular traffic and the build-up of PAHs that can exert significant impacts on human health. The use of BNs enabled the investigation of the influence of traffic on PAH build-up far beyond the typical perspective of traffic as a source of PAHs. The PAH buildup in this paper refers to the concentrations of PAH adsorbed by particles. The outcomes of this investigation are expected to contribute to enhancing urban stormwater quality modelling practices and thereby, to strengthen the design of pollution mitigation strategies.

# 2.0 MATERIALS AND METHODS 

### 2.1 Study area

Three cities located in Northern China, namely, Daqing (DQ), Harbin (HEB) and Jilin (JL) that have different urban characteristics were selected as the study areas. Daqing, where the largest oil field in China is located, produces approximately 40 million tons of oil every year. Jilin has a long history of chemical industries since the 1950s, while Harbin, which is China's third biggest heavy industrial city, hosts food, equipment manufacturing, petro-chemical, metallurgical and electric power industries. The sampling sites for the study were selected such that they are evenly located within the central area of each city and encompass different land uses. Fig. 1 and Figures S1 and S2 in the Supplementary Information shows the locations of the sampling sites. Further details regarding the study areas can be found in Song et al. (2015).

### 2.2 Experimental data

The dust samples were collected within 0.5 m from the kerb or street edges at the selected sites using a clean brush. At least three cycles of back-and-forth sweeping were performed along 2 to 30 m length of the street to collect one sample at each site within $0.5-1$ hour time period. Accordingly, 23 samples from DQ site and 21 samples from each of HEB and JL sites were collected.

The dust samples were air-dried for at least 15 days, and then sieved through a screen with $500 \mu \mathrm{~m}$ opening to remove large particulates such as stones and plant debris. This approach has been commonly used in previous studies (eg. Lorenzi et al., 2011; Nguyen et al., 2014; Peng et al., 2011; Wang et al., 2015). The concentrations of the sixteen PAHs identified by the US EPA as priority pollutants (Schoeny and Poirier, 1993; USEPA, 1984) were determined for each dust sample from each site. Detailed information about sampling and laboratory analysis of PAHs can be found in Song et al. (2015).

To determine the daily traffic volume, the traffic at each study site was video-recorded between 7:30am - 8:30am and 10am - 11am. This was followed by counting the traffic volume during these two periods using the recorded videos. On the same day, the traffic for 24 hours was also video-

recorded at each site and the daily traffic volume was estimated using the data obtained from the manual counting of the traffic for the two hourly study periods noted above.
![img-1.jpeg](img-1.jpeg)

Fig. 1. Locations of sampling sites in Jilin (JL).

# 2.3 Bayesian Network modelling 

BNs are a graphical modelling approach based on Bayesian statistical methods. The directed acyclic graphical ( $D A G$ ) structure (i.e. a directed graph without any loops) of BNs integrates a given set of random variables (discrete and/or continuous), which describes the system or process being modelled using probabilistic conditional dependencies (Fig. 2). This is achieved by factorising the global probability distribution of the set of random variables into local probability distributions of

individual variables. The factorisation is based on the Markov Property of Bayesian Networks, such that each random variable depends only on its immediate parent variables (Scutari, 2009).

BN modelling is a two-step approach. It first learns the structure of the BN using Structure Learning Algorithms and then estimates the parameters of the variables commonly based on Maximum Likelihood Estimates given the data and the model structure (Ben-Gal, 2007; Scutari, 2009; Uusitalo, 2007). Moreover, the parameters of the discrete and continuous random variables are estimated in the form of conditional probabilities and conditional regression coefficients, respectively. Further, in the case where a continuous variable has discrete parent variables which form different configurations, regression coefficients for the continuous variable are estimated for each configuration.
![img-2.jpeg](img-2.jpeg)

Fig. 2. A typical structure of a Bayesian Network (BN); Note: V is a set of random variables, such that $V=\left\{V_{1}, V_{2}, \ldots, V_{5}\right\}$, represented as nodes. The variables are connected using conditional probabilistic dependencies, represented by edges. Note: Conditional density refers to the probability density functions of the variables V3, V4 and V5 given each of their parent variables.

In this study, a BN was proposed to investigate the interdependencies between vehicular traffic in different types of urban land use and build-up of particle-bound PAHs. Accordingly, the three land use types, namely, residential, industrial and commercial, and traffic volume corresponding to each land use type were identified as the factors that influence PAHs build-up. This was based

on the outcomes of the previous investigation by Song et al. (2015) on PAHs adsorbed to street dust in the same study areas as shown in Figures S3 and S4 in the Supplementary Information.

Accordingly, the input data of the BN model included observed concentrations of particle-bound PAHs, observed volumes of vehicular traffic and types of land uses. The PAH concentrations and traffic volumes were fed into the model as quantitative data, while land use type was fed as qualitative data. This means that the land use data were provided in terms of 'Yes' and 'No' scenarios. For example, for residential sites, the data for variable 'Residential' would be fed into the model as 'Yes', while variables 'Industrial' and 'Commercial' would be fed as 'No'.

The proposed BN model was fitted with observed data using the bnlearn R statistical computing package to conduct the predictive analysis. This means that the probability density functions corresponding to a specific BN (Fig. 2) are fitted with observed data, such that the difference between observed and predicted values is minimised (Scutari, 2009, 2016; Team, 2014). Accordingly, parameters for discrete and continuous variables were estimated, and then the estimated BN model was utilised to predict the concentrations of PAHs at each study site.

The BN model facilitated the quantitative evaluation of the influence of traffic on the build-up of the sixteen US EPA priority PAHs and total PAHs. This was done by assessing the type and relative strength of relationships between traffic and PAH build-up as informed by the estimated conditional regression coefficients. Positive regression coefficients would imply that the concentration of PAHs increase with the increase in traffic volume, while negative regression coefficients would imply the decrease in PAH concentrations in response to increase in traffic volume. Further, among any given set of PAHs, larger the magnitude of the regression coefficient, relatively greater the influence of traffic on the increase/decrease in PAH concentration.

# 3.0 RESULTS AND DISCUSSION 

### 3.1 Developing relationships between PAH build-up and vehicular traffic

The proposed BN that describes the relationships between vehicular traffic in different land uses and build-up of particle-bound PAHs is depicted in Fig. 3. This BN was developed based on the outcomes of past research studies on how the concentration of PAHs associated with particulate solids varies during build-up. As such, the facts that underpinned the structure of the BN were: (1) in general, PAH concentrations increase with the increase in traffic volume which, in fact, is related to land use type; and (2) type of land use itself influences the concentrations of PAHs primarily as a source of origin (Gunawardena et al., 2014; Liu et al., 2017; Liu et al., 2016a; Liu et al., 2016b; Song et al., 2015). The predictive analysis was conditional on the structure of the proposed BN. However, it is important to note that this structure can be modified in order to improve the model predictive performance by incorporating more variables to enhance the description of the system/process being modelled (Uusitalo, 2007).

### 3.2 Influence of vehicular traffic on PAH build-up

Vehicular traffic can be influential in PAH build-up primarily as a source of origin as well as a factor that influences the re-distribution of particulate solids to which PAHs are attached. According to the study by Hinds (2012)on the behaviour of airborne particles, the airstreams created by vehicle movement primarily govern the re-suspension of particulate solids deposited on urban surfaces. Due to traffic, a thin laminar airflow is developed close to the road surface and turbulent airstreams flow above this laminar air flow. Particles smaller than the thickness of the laminar airflow are unlikely to re-suspend due to the limited exposure to turbulent eddies, while particles larger than the laminar airflow potentially become re-suspended, and in turn continuously undergo re-distribution. This phenomenon has also been noted by other researchers such as Patra

et al. (2008) and Mahbub et al. (2011). Further, it is important to note that the thickness of the laminar airflow created by vehicle movement could vary depending on the type of vehicle. For example, the airflows created by light-duty vehicles, which are typical to residential areas, can be different from the airflows created by heavy-duty vehicles, which are typical to commercial and industrial areas (Cooper and Watkins, 2007; Hucho and Sovran, 1993; Wordley and Saunders, 2008). Therefore, the cut-off size of smaller and larger particles that can re-suspend varies depends on the traffic condition typical to a given site.
![img-3.jpeg](img-3.jpeg)

Fig. 3. The structure of the Bayesian Network (BN) for modelling Polycyclic Aromatic Hydrocarbons (PAHs) as a function of vehicular traffic and land use. Note: Conditional density refers to the probability density function of "Traffic" given land use type and the probability density function of "PAH" given traffic volume and land use type.

# 3.3 Evaluation of the relationships between vehicular traffic and PAH build-up 

As evident from past research studies, it is necessary to understand how land use influences vehicular traffic in order to evaluate the relationships between build-up of different PAHs and traffic (Gunawardena et al., 2012; Gunawardena et al., 2014; Zhang et al., 2017). Table 1 provides

the estimated conditional regression coefficients (described in Section 2.3) for traffic in relation to the three land use types. It is evident that sites with industrial land use have the highest traffic volumes compared to the sites with commercial and residential land uses. Busy material and goods transportation and high population density close to industrial areas are considered to create high traffic volumes.

Table 1. Conditional regression coefficients for traffic (conditional Gaussian distribution).


Table 2 provides details of the relationships identified between the build-up of PAHs and traffic volume. It was not possible to classify relationships for commercial land uses at the study sites at HEB and JL as there was only one sampling location representing the respective land use. The relationships were identified based on the conditional regression coefficients estimated for the sixteen PAHs (Table S1 in the Supplementary Information) and total PAHs (Table 3) in relation to the traffic volumes at different land-uses at the three study sites.

Further, Song et al. (2015) noted that different types of industries distinctly influence PAHs emissions to the environment. Therefore, in order to distinguish the influence of traffic on PAH build-up from the influence of land use itself, the relationships between different land uses and PAH concentrations were also identified based on the predictions of PAH concentrations at each study site (Table 4 and Tables S2 and S3 in the Supplementary Information). Tables 4, S2 and S3 show the variations of concentration of individual PAHs in relation to the three land use types. The analysis of the plots of observed vs predicted values and residual plots (Figures S5 - S10 in the Supplementary Information) confirm that the prediction performance of the proposed BN model is satisfactory for low concentrations of the majority of PAHs. However, it can be noted that the difference between highest and lowest concentrations of each PAH is very small, and the observed data include higher number of low concentration values of PAHs. Therefore, the overall prediction performance of the BN model was considered to be satisfactory.

As evident in Table 2, the build-up of PAHs exhibit both positive and negative relationships with vehicular traffic. Accordingly, two major conclusions can be derived differentiating the influence of traffic on PAH build-up. Firstly, the positive relationships between PAHs and traffic reveal that traffic plays a major role in generating PAHs in the respective areas, and PAHs continuously accumulate due to the potentially minimal influence of traffic on the re-distribution of particles that carry these PAHs. Further, as described in Section 3.2, finer particles are less likely to be exposed to turbulent airstreams caused by traffic, thus are less susceptible to re-distribution. Consequently, it is also possible to conclude that PAHs that have positive relationships with traffic volume are associated with the finer particles.

Table 2. Relationships between Polycyclic Aromatic Hydrocarbons (PAHs) build-up and traffic volume in different land uses at the study sites, and Toxic Equivalent Factors (TEFs) and the classification of the impact on human health.


Table 3. Conditional regression coefficients for Polycyclic Aromatic Hydrocarbons (PAHs) (con ditional Gaussian distribution).


Secondly, from the negative relationships between PAHs and traffic volume (Table 2), it can be concluded that traffic plays a major role in the build-up of these PAHs as a factor that significantly influences re-distribution rather than as a source of origin. This is consistent with the outcomes of the study by Gunawardena et al. (2014) who found negative relationships between traffic and 3ring and 4-ring PAHs. Gunawardena et al. (2014) attributed these negative relationships to the propensity for re-suspension and evaporation influenced by the relatively high volatility of 3-ring and 4 -ring PAHs. However, it is evident from the current study that not only 3-ring and 4-ring PAHs, but all PAHs exhibit negative relationships with traffic under specific conditions (i.e. land use type). Given the different behaviour of finer and coarser particles during re-distribution under traffic (described in Section 3.2), it can be concluded that the re-distribution of particle-bound PAHs that exhibit negative relationships with traffic is determined by the particle size rather than the chemical characteristics of PAHs. In fact, these PAHs are likely to be associated with coarser particles which are exposed to turbulent airstreams, and thereby being subject to rapid redistribution. Further, it is also important to note that during re-distribution, road deposited particles can be re-deposited in the surrounding soils, thus increasing the possibility of the surrounding soils being contaminated by PAHs, particularly at sites which exhibit negative relationships with traffic.

Moreover, PAHs that have positive and negative relationships with traffic can be further distinguished based on the evidence of their origin in relation to land use. In all three study sites, the highest concentrations of the majority of PAHs are found in industrial areas (Tables 3, S2 and S3). However, of these PAHs, those classified as human carcinogens (Table 2) show positive relationships with traffic at DQ and JL sites, and negative relationships with traffic at HEB sites. Therefore, it can be concluded that while industrial activities contribute to a proportion of the PAHs released to the environment, carcinogenic PAHs present at DQ and JL sites are likely to be associated with finer particles given the positive relationship with traffic, and thus traffic exerts low impact on re-distribution as described in Section 3.2. In contrast, HEB sites are associated with coarser particles given the negative relationship with traffic. On the other hand, PAHs which are not classified as human carcinogens, mostly show negative relationships with traffic in industrial areas at all three study sites (Table 2). Therefore, these PAHs are likely to be found in the coarser particle size fraction.

In residential areas, the majority of PAHs that are not classified as carcinogens exhibit positive relationships with traffic, while most carcinogenic PAHs show negative relationships. This means that carcinogenic PAHs that are generated in residential areas are likely to undergo re-distribution, and thereby contribute to the potential increase in concentrations in surrounding soils. This phenomenon can be critical particularly at DQ sites where very high concentrations of carcinogenic PAHs were found in residential areas (Table 4). In relation to commercial areas at DQ sites, the majority of the PAHs show negative relationships with traffic (Table 2) and relatively high concentrations (Table 4), confirming that PAHs are subject to re-distribution, and consequently, surrounding soils can be potentially contaminated.

Further, higher concentrations of total PAHs in industrial and residential areas are likely to be found in the coarser particle fraction (given the negative relationships) and in the finer particle fraction (given positive relationships), respectively.

# 3.4 Practical implications of the research outcomes 

It is important that urban water management personnel acquire an in-depth understanding of the influence of anthropogenic and environmental factors on stormwater pollution for designing and implementing effective strategies to safeguard urban water ecosystems. The research outcomes highlight several phenomena that can potentially occur during PAH build-up, in particular, the variability in the influence of traffic on the re-distribution and subsequent contamination of surrounding soils leading to specific health risks (carcinogenic). While these phenomena need further investigation, the research study highlighted the important issues that have hitherto not been accounted for in the context of urban stormwater pollution mitigation.

Further, the study also confirmed the versatility of the use of BNs for investigating the relationships between pollutant build-up and influential factors, leading to further advancement in knowledge in relation to stormwater quality modelling. As such, application of BNs as a tool for replicating stormwater pollutant processes will facilitate in generating reliable information on stormwater quality in urban catchments for enhanced decision making.

Table 4. Predicted concentrations of Polycyclic Aromatic Hydrocarbons (PAHs) and their relationship with land use (Daqing - DQ site).


# 4.0 CONCLUSIONS 

The BN modelling of the build-up of particle-bound PAHs on urban road surfaces enabled the quantification of the interdependencies between influential factors and PAH build-up, and thereby characterise the influence of vehicular traffic. The results revealed that PAHs that have positive relationships with traffic are likely to be generated from traffic related activities, while traffic has minimal influence on the re-distribution of these PAHs. On the other hand, the negative relationships between traffic and PAHs can be attributed to the predominant role of traffic as a factor that influences re-distribution rather than as a source of origin. Another major conclusion derived from this study is that PAHs that are positively related to traffic are likely to be associated with finer particles, and those PAHs that have negative relationships with traffic are associated with coarser particles. It was also evident that compared to the influence of chemical characteristics of PAHs such as volatility, particle size significantly influences the re-distribution of particle-bound PAHs that exhibit negative relationships with traffic.

Moreover, industrial areas were found to be the major contributor of PAHs to the environment. It was also possible to conclude that carcinogenic PAHs found in industrial areas are likely to be associated with finer particles, and less likely to be re-distributed by traffic. On the other hand, PAHs which are not classified as human carcinogens are susceptible to being re-distributed as they are likely to be associated with coarser particles. Additionally, most carcinogenic PAHs found in residential areas are likely to undergo re-distribution due to traffic, increasing the possibility of surrounding soils being contaminated.

## ACKNOWLEDGMENTS

The authors are grateful for the support provided by the Innovative Research Group of the National Natural Science Foundation of China (Grant number 51421065) and Fund for the State Key Program of National Natural Science of China (Grant number 41530635).

## SUPPLEMENTARY INFORMATION

Location maps of the sampling sites in Daqing (DQ) and Harbin (HEB) cities, conditional regression coefficients for PAHs, predicted concentrations of PAHs, and the results of the analysis of prediction performance of the proposed BN are provided as Supplementary Information.

# Supplementary Information 

## Influence of traffic on build-up of polycyclic aromatic hydrocarbons on urban road surfaces: A Bayesian Network modelling approach

Yingxia Li ${ }^{1 *}$, Ziliang Jia ${ }^{1}$, Buddhi Wijesiri ${ }^{2 * *}$, Ningning Song ${ }^{1}$, Ashantha Goonetilleke ${ }^{2}$<br>${ }^{1}$ State Key Laboratory of Water Environment Simulation, School of Environment, Beijing Normal University, Beijing 100875, China<br>${ }^{2}$ Science and Engineering Faculty, Queensland University of Technology (QUT), GPO Box 2434, Brisbane, 4001, Queensland, Australia<br>yingxia@bnu.edu.cn; 201621180080@mail. bnu. edu. cn;<br>b.mahappukankanamalage@qut.edu.au; 201331180007@mail.bnu.edu.cn;<br>a.goonetilleke@qut.edu.au<br>*Corresponding Author: Tel: 86-10-62205508; Email: yingxia@bnu.edu.cn<br>**Corresponding Author: Tel: 61-731381539; Email: b.mahappukankanamalage@qut.edu.au

![img-4.jpeg](img-4.jpeg)

Fig. SI. Locations of sampling sites in Daqing (DQ).

![img-5.jpeg](img-5.jpeg)

Fig. S2. Locations of sampling sites in Harbin (HEB).

![img-6.jpeg](img-6.jpeg)

Fig. S3. Individual PAH concentrations for dust samples in DQ, HEB and JL (Adapted from Song et al. 2015).
![img-7.jpeg](img-7.jpeg)

Fig. S4. Sampling site locations and land uses in DQ, HEB and JL (Adapted from Song et al. 2015).

Table S1. Conditional regression coefficients for Polycyclic Aromatic Hydrocarbons (PAHs) (conditional Gaussian distribution).


Table S1. Conditional regression coefficients for Polycyclic Aromatic Hydrocarbons (PAHs) (conditional Gaussian distribution) contd.


Table S1. Conditional regression coefficients for Polycyclic Aromatic Hydrocarbons (PAHs) (conditional Gaussian distribution) contd.


Note1: Nap128 - naphthalene; Ace152 - acenaphthylene; Ace154 - acenaphthene; Flue166 - fluorene; Phe178 phenanthrene; Ant178 - anthracene; Flua202 - fluoranthene; Pyr202 - pyrene; BaA228 - benzo (a) anthracene; Chr228 - chrysene; BbF252 - benzo (b) fluoranthene; BkF252 - benzo (b) fluoranthene; BaP252 - benzo (a) pyrene; Ind276 indeno (1, 2, 3-cd) pyrene; BghiP276 - benzo (ghi) perylene; DbA278 - dibenzo (a, h) anthracene

Note 2: DQ - Daqing; HEB - Harbin; JL - Jilin
Note 3: Conditional density refers to the probability density function of each PAH given traffic volume and land use type (commercial, industrial and residential)

Table S2. Predicted concentrations of Polycyclic Aromatic Hydrocarbons (PAHs) and their relationship with land use (Harbin - HEB site).


Table S3. Predicted concentrations of Polycyclic Aromatic Hydrocarbons (PAHs) and their relationship with land use (Jilin - JL site).


![img-8.jpeg](img-8.jpeg)

Fig. S5. Variation in predicted values against observed data; Note: Nap128 - naphthalene; Ace152 - acenaphthylene; Ace154 - acenaphthene; Flue166 - fluorene; Phe178 - phenanthrene; Ant178 - anthracene.

![img-9.jpeg](img-9.jpeg)

Fig. S6. Variation in predicted values against observed data; Note: Flua202 - fluoranthene; Pyr202 - pyrene; BaA228 - benzo (a) anthracene; Chr228 - chrysene; BbF252 - benzo (b) fluoranthene; BkF252 - benzo (b) fluoranthene.

![img-10.jpeg](img-10.jpeg)

Fig. S7. Variation in predicted values against observed data; Note: BaP252 - benzo (a) pyrene; Ind276 - indeno (1, 2, 3-cd) pyrene; BghiP276 - benzo (ghi) perylene; DbA278 - dibenzo (a, h) anthracene; TPAHs - Total PAHs.

![img-11.jpeg](img-11.jpeg)

Fig. S8. Variation in residuals against predicted values; Note: Nap128 - naphthalene; Ace152 acenaphthylene; Ace154 - acenaphthene; Flue166 - fluorene; Phe178 - phenanthrene; Ant178 anthracene.

![img-12.jpeg](img-12.jpeg)

Fig. S9. Variation in residuals against predicted values; Note: Flua202 - fluoranthene; Pyr202 pyrene; BaA228 - benzo (a) anthracene; Chr228 - chrysene; BbF252 - benzo (b) fluoranthene; BkF252 - benzo (b) fluoranthene.

![img-13.jpeg](img-13.jpeg)

Fig. S10. Variation in residuals against predicted values; Note: BaP252 - benzo (a) pyrene; Ind276 - indeno (1, 2, 3-cd) pyrene; BghiP276 - benzo (ghi) perylene; DbA278 - dibenzo (a, b) anthracene; TPAHs - Total PAHs.