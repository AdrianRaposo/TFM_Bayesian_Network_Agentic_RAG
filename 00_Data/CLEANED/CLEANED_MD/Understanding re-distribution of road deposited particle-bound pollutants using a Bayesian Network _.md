# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Liu, An, Mahappu Kankanamalage, Buddhi Wijesiri, Hong, Nian, Zhu, Panfeng, Egodawatta, Prasanna, \& Goonetilleke, Ashantha (2018)

Understanding re-distribution of road deposited particle-bound pollutants using a Bayesian Network (BN) approach.
Journal of Hazardous Materials, 355, pp. 56-64.
This file was downloaded from: https://eprints.qut.edu.au/121576/

## (c) Consult author(s) regarding copyright matters

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

License: Creative Commons: Attribution-Noncommercial-No Derivative Works 4.0

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1016/j.jhazmat.2018.05.012

# Accepted Manuscript 

Title: Understanding re-distribution of road deposited particle-bound pollutants using a Bayesian Network (BN) approach

Authors: An Liu, Buddhi Wijesiri, Nian Hong, Panfeng Zhu, Prasanna Egodawatta, Ashantha Goonetilleke

PII: S0304-3894(18)30351-0
DOI: https://doi.org/10.1016/j.jhazmat.2018.05.012
Reference: HAZMAT 19378
To appear in: Journal of Hazardous Materials
Received date: $\quad 28-10-2017$
Revised date: $\quad 2-5-2018$
Accepted date: $\quad 7-5-2018$
Please cite this article as: Liu A, Wijesiri B, Hong N, Zhu P, Egodawatta P, Goonetilleke A, Understanding re-distribution of road deposited particle-bound pollutants using a Bayesian Network (BN) approach, Journal of Hazardous Materials (2010), https://doi.org/10.1016/j.jhazmat.2018.05.012

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Understanding re-distribution of road deposited 

## particle-bound pollutants using a Bayesian Network

## (BN) approach

An Liu ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$, Buddhi Wijesiri ${ }^{\mathrm{b}, \mathrm{d}}$, Nian Hong ${ }^{\mathrm{a}, \mathrm{c}}$, Panfeng Zhu ${ }^{\mathrm{a}, \mathrm{c}}$, Prasanna Egodawatta ${ }^{\mathrm{b}}$, Ashantha Goonetilleke ${ }^{\mathrm{b}}$

${ }^{a}$ College of Chemistry and Environmental Engineering, Shenzhen University, Shenzhen 518060, China<br>${ }^{\mathrm{b}}$ Science and Engineering Faculty, Queensland University of Technology (QUT), GPO Box 2434, Brisbane, Qld 4001, Australia<br>${ }^{\text {c}}$ Shenzhen Key Laboratory of Environmental Chemistry and Ecological Remediation, Shenzhen 518060, China<br>${ }^{\text {d }}$ School of Environment, Beijing Normal University, Beijing 100875, China

*Corresponding author: Tel: 6145752 3247; E-mail: b.mahappukankanamalage@qut.edu.au

Graphical Abstract

# ACCESSOIRE 

## Graphical Abstract

![img-0.jpeg](img-0.jpeg)

## Highlights

- Traffic influence on pollutant re-distribution was characterised using BNs
- Traffic influence on particle re-distribution varies between different size ranges
- Vehicle types influence pollutant re-distribution differently
- BNs help to identify specific improvements to enhance stormwater modelling

#### Abstract

: Road deposited pollutants are continuously re-distributed by external factors such as traffic and wind turbulence, influencing stormwater runoff quality. However, current stormwater quality modelling approaches do not account for the re-distribution of pollutants. This undermines the accuracy of stormwater quality predictions, constraining the design of effective stormwater treatment measures. This study, using over 1,000 data points, developed a Bayesian Network modelling approach to investigate the re-distribution of pollutant buildup on urban road surfaces. BTEX, which are a group of highly toxic pollutants, was the case study pollutant. Build-up sampling was undertaken in Shenzhen, China, using a dry and wet vacuuming method. The research outcomes confirmed that the vehicle type and particle size significantly influence the re-distribution of particle-bound BTEX. Compared to heavy-duty traffic in commercial areas, light-duty traffic dominates the re-distribution of particles of all size ranges. In industrial areas, heavy-duty traffic re-distributes particles $>75 \mu \mathrm{~m}$, and lightduty traffic re-distributes particles $<75 \mu \mathrm{~m}$. In residential areas, light-duty traffic re-distributes particles $>300 \mu \mathrm{~m}$ and $<75 \mu \mathrm{~m}$ and heavy-duty traffic re-distributes particles in the $300-$ $150 \mu \mathrm{~m}$ range. The study results provide important insights to improve stormwater quality modelling and the interpretation of modelling outcomes, contributing to safeguard the urban water environment.

# ACCESS 

## Keywords:

BTEX; Bayesian Networks; Stormwater quality; Stormwater pollutant processes; Pollutants re-distribution

### 1.0 Introduction

Pollutants deposited (build-up) on road surfaces are eventually washed-off by stormwater runoff and transported to receiving waters, deteriorating water quality. Consequently, these pollutants can pose ecological and human health risks. In this context, an effective treatment design for the removal of these pollutants from stormwater runoff is essential to secure the urban water environment safety and to mitigate the potential risks. The effectiveness of stormwater treatment relies on an in-depth understanding of pollutant processes. Pollutant build-up and re-distribution are among the most important processes in relation to pollutant accumulation on urban surfaces during the dry seasons [1, 2].

It is commonly known that particles act as a mobile substrate and play the most important role in the transport of other road deposited pollutants to receiving waters during storm events [3, 4]. Pollutant build-up on road surfaces generally increases with antecedent dry days and then approaches an almost constant value after around 7 - 9 days [5]. However, the build-up

process is continuously disturbed by external factors such as traffic, periodic street sweeping and wind turbulence [6]. This results in pollutant re-distribution on road surfaces, which significantly influences pollutant load allocation between the ground phase and atmospheric phase, and thereby the pollutant concentrations in stormwater runoff. Additionally, the road surface condition is found to influence the retaining of pollutants [7], and consequently, affects pollutants re-distribution. However, current stormwater quality modelling approaches describe pollutant build-up as a continuously increasing trend that approaches a relatively constant value after a certain number of dry days [8], and do not consider pollutants redistribution over the antecedent dry period. This could undermine the accurate prediction of stormwater quality, and thereby adversely affect the effectiveness of stormwater quality treatment strategies.

Particle size is an important influential factor in pollutant re-distribution. Nicholson and Branson [9] found that particles larger than $10 \mu \mathrm{~m}$ are readily re-distributed compared to particles smaller than $10 \mu \mathrm{~m}$. This phenomenon (i.e. relatively coarser particles are more susceptible to re-distribution compared to finer particles) occurs when the particles are subjected to traffic induced re-suspension [10, 11]. As explained by Hinds [12], this is caused by the thin laminar airflow that exists at the surface caused by traffic induced turbulent airstreams. Particles larger than the thickness of this laminar airflow are subjected to turbulent eddies and then re-suspended, while particles smaller than the thickness of the laminar airflow barely undergo re-suspension, and are thus less likely to be re-distributed. However, when particles are larger than a certain size, they are difficult to be disturbed due to their weight, constraining re-distribution. Additionally, particle size also significantly influences the adsorption of pollutants. Finer particles tend to adsorb more pollutants due to the relatively larger specific surface area [13].

# ACCEPTED MANUSCRIPT 

As pollutant re-distribution is strongly influenced by a range of external factors as discussed above, exploring the relationship between re-distribution and these influential factors is crucial. This can advance the understanding of pollutant re-distribution, and thereby contribute to improving stormwater quality modelling. In this context, it is necessary to create a robust approach for analysing the interdependencies between pollutant re-distribution and their influential factors. Bayesian Network (BN) modelling is an emerging probabilistic graphical modelling approach which represents a set of variables and their conditional dependencies through a directed acyclic graph (DAG). In conclusion, the BN approach has the capability for effectively analysing complex environmental systems and processes.

A BN modelling approach was developed to undertake research on pollutant re-distribution using BTEX as the case study pollutant group to demonstrate the practical application of the study outcomes. Among road deposited pollutants, BTEX are a group of toxic pollutants which primarily include benzene, toluene (or methylbenzene), ethylbenzene and xylene (m-xylene, o-xylene and p-xylene). Especially styrene is also considered as part of this group of pollutants [14]. In the urban environment, these pollutants are sourced from traffic activities such as vehicle emissions and fuel and oil leakages [15] as well as industrial activities, landfill sites, municipal solid waste stations and domestic heating [16-18]. However, it has been reported that traffic related activities are the primary source of BTEX with over $45 \%$ of BTEX emissions in a typical urban environment originating from gas stations and petrol and vehicle emissions [19, 20]. The high BTEX emissions and resulting high toxicity leads to potential human and ecosystem health risks in the urban environment.

This paper presents an in-depth investigation on pollutant re-distribution and their influential factors. A range of influential factors were accounted for in the study, including land use, traffic and road surface condition. The research outcomes are expected to provide important insights for improving current practices in relation to stormwater quality modelling, and

# ACCEPTED MANUSCRIPT 

thereby the formulation of effective stormwater treatment strategies. This will contribute to safeguarding the urban water environment and mitigating ecological and human health risks posed by polluted stormwater runoff.

### 2.0 Materials and Methods

### 2.1 Study sites

The study area was located in Shenzhen, China, which is recognised as a typical metropolis in the Southern part of China. Shenzhen has a population of approximately 12 million, and has about 3.14 million vehicles. Seventeen roads encompassing different urban land uses were selected as study sites. Among the surrounding land uses, there were six residential areas, six industrial areas and five commercial areas. Light-duty and heavy-duty vehicle volumes were measured at each road, individually, because different vehicle types can emit different amounts of pollutants such as BTEX [21]. All roads are paved with asphalt. The road texture depth (representing road surface roughness) was measured for each road. The method of measuring road texture depth is described in the Supplementary Information. Fig. 1 shows the study sites, while the locations and characteristics of the study sites (geocoordinates, traffic, land use and road surface roughness) are given in Table S1 in the Supplementary Information.

Fig. 1

### 2.2 Build-up sample collection and laboratory testing

Build-up samples were collected using a dry and wet vacuuming method. A $2 \mathrm{~m} \times 2 \mathrm{~m}$ frame was used to demarcate a test plot. The frame was placed between the kerb and the median strip of the road. This was to collect representative samples, since the area close to the kerb

# ACCEPTED MANUSCRIPT 

generally has a higher pollutant build-up load than the median strip [22]. All build-up samples were collected after seven antecedent dry days. This was due to the fact that pollutant build-up on road surfaces asymptotes to an almost constant value after a $7-9$ day antecedent dry period [23]. There were no street cleaning activities during the sampling periods. One sample was collected from each road site. Accordingly, a total of 17 build-up samples were collected from the selected road sites.

The collected samples were separated into sub-samples based on five particle size ranges using wet sieving. Particle size ranges were, $>300 \mu \mathrm{~m}, 300-150 \mu \mathrm{~m}, 150-100 \mu \mathrm{~m}, 100-75 \mu \mathrm{~m}$ and $<75 \mu \mathrm{~m}$. The sub-samples were then analysed for BTEX (benzene, ethylbenzene, methylbenzene, m-xylene, o-xylene, p-xylene and styrene). A headspace system along with an Agilent 7890 gas chromatograph-5975 mass selective detector (GC-MS) was used for sample extraction and analysis. Calibration standards, internal standards, surrogate spikes and blanks were used as part of the quality control and quality assurance procedures. The recovery ranged from $72.9 \%$ to $109.4 \%$, which is within the acceptable ranges reported in the literature [11]. Additionally, particulate solids load for the five particle size ranges were determined using Gravimetric Methods 2540C and 2540D [24]. This was to investigate the re-distribution of different sized particles.

### 2.3 Bayesian Network modelling: theory and model setup

BN modelling is based on Bayesian statistical methods. The structure of a BN primarily includes three components: (1) nodes except for root nodes as a function of a myriad of other variables; (2) relationships between node variables (edges); and (3) conditional probability tables reflecting the influence of one node variable on another node variable (Fig. S1 in the Supplementary Information) [25, 26]. BN modelling uses Structure Learning Algorithms to learn the modelling structure. Subsequently, given the data and the learned model structure, a

# ACCEPTED MANUSCRIPT 

predictive analysis is conducted to estimate parameters of the model commonly based on Maximum Likelihood Estimates [26-28].

In this study, a BN was proposed to analyse the relationships between traffic, land use, road surface roughness, particle size and re-distribution of particle-bound BTEX (as a case study) on road surfaces. Accordingly, the build-up of solids in different size ranges, vehicular traffic volume (including light-duty and heavy-duty vehicle volumes), road surface texture depth and the three land use types (industrial, commercial and residential) were identified as the factors that influence the accumulation and re-distribution of particle-bound pollutants (such as BTEX) [21].

The input data for the BN model included observed (measured) build-up of size fractionated particles, observed (measured) build-up of the selected particle-bound BTEX in each particle size fraction, observed volumes of light and heavy-duty vehicular traffic volumes, road surface texture depth and land use type at each study site. All observed data were input into the BN model as quantitative data, except for land use type which was input as qualitative data (i.e. data were input using 'Yes' and 'No' scenarios, such that for example, the data for the variable 'Industrial', was input into the model as 'Yes' for predominantly industrial sites, while variables 'Residential' and 'Commercial' was input as 'No' for the same site). In summary, the dataset used for undertaking BN modelling consisted of more than 1,000 data points within the data matrix: 17 sites $\times 5$ particle sizes $\times(7$ BTEX species + total solids +6 influential factors including traffic, land use and road surface condition).

To estimate the model parameters, the analysis was conducted by fitting the probability density functions corresponding to the proposed BN model with observed data, minimising the difference between observed and predicted values. This was undertaken using the bnlearn R statistical computing package [26, 29, 30]. The estimated parameters provided information

# ACCEPTED MANUSCRIPT 

about the type and relative strength of relationships between influential factors (traffic, land use, road surface condition and particle sizes) and the build-up of toxic pollutants associated with particulate solids. Thus, the BN model facilitated the quantitative evaluation of the influence of traffic in areas with different land uses on the re-distribution of particle-bound pollutants during build-up. Moreover, it is important to note that the predictive analysis was conditional on the structure of the proposed BN. The inherent flexibility of BNs enables improvement to the model predictive performance by incorporating additional influential factors in relation to the build-up of the pollutants of interest when new knowledge is created [27].

### 3.0 Results and Discussion

### 3.1 Developing relationships between particle-bound pollutants build-up and influential factors

Fig. 2 depicts the proposed BN that describes the interdependencies between build-up of particle-bound pollutants and particulate solids under the influence of vehicular traffic, different land uses and road surface conditions. These relationships, which underpinned the development of the BN structure, were identified based on the outcomes of past research studies. These included: (1) build-up of particle-bound pollutants depends primarily on the build-up of particulate solids [31, 32]; (2) vehicular traffic and land use type are major sources of particle-bound pollutants [33-35]; (3) traffic volume varies with land use [36-38]; and (4) road texture depth, which is a measure of surface roughness, influences the amount of pollutants accumulated on road surfaces [39].

Fig. 2

# 3.2 Case study - understanding BTEX re-distribution 

### 3.2.1 Influence of land use on vehicular traffic

As evident from the literature, the type of land use influences the traffic characteristics in a particular area (as discussed in Section 3.3). The current study accounted for both, light and heavy-duty traffic at all sites. Hence, it was important to understand the relationships between the three land uses and the corresponding traffic conditions. Table 1 shows conditional regression coefficients for the two types of traffic conditions. It is evident that heavy-duty traffic volume is significantly higher in commercial and industrial sites compared to residential sites. This is attributed to the difference in typical anthropogenic activities associated with each land use type (i.e. heavy-duty vehicles are commonly used for goods handling and transportation purposes in commercial and industrial areas). Further, although light-duty traffic volume is higher than heavy-duty traffic volume, the modelling outcomes show relatively small difference in light-duty traffic volume among the three land use types compared to the difference in heavy-duty traffic volume. The difference was observed by comparing the difference in conditional regression coefficients between different land uses in Table 1.

## Table 1

### 3.2.2 Influence of traffic on build-up of particulate solids

The relationships between the build-up of particles of different size ranges and traffic volume at the study sites with different road surface conditions and land uses were identified based on the estimated conditional regression coefficients given in Table 2 (standard errors for the estimates are given in Table S2 in the Supplementary Information). PART A in Table 3

# ACCEPTED MANUSCRIPT 

shows the types of relationships identified. It is evident that particulate solids of different size ranges have different relationships with heavy and light-duty traffic.

## Table 2

## Table 3

The inverse relationships (negative conditional regression coefficients) of different sized particles with heavy/light-duty traffic (PART A in Table 3) mean that the amount of particulate solids build-up on road surfaces decreases with the increase in traffic volume. This implies that the traffic causes the removal of particulate solids accumulated on the road surface, which could potentially result in the re-distribution of particles due to turbulent air streams created by vehicle movement. Further, it is important to note that vehicle induced turbulence can be significantly different between heavy and light-duty vehicles. This is due to heavy-duty vehicles being typically larger in size compared to light-duty vehicles, and lightduty vehicles are allowed higher speed limits than for heavy-duty vehicles [40, 41]. Therefore, the inherent aerodynamic features of heavy and light-duty vehicles and their specific influences on traffic can exert different impacts on particle re-distribution.

According to PART A in Table 3, it is likely that in commercial areas, light-duty traffic has a significant influence on the re-distribution of particles of all size ranges, compared to that of heavy-duty traffic. Similarly, in industrial areas, heavy-duty traffic influences the redistribution of particles $>75 \mu \mathrm{~m}$, and light-duty traffic influences the re-distribution of particles $<75 \mu \mathrm{~m}$. Further, in residential areas, light-duty traffic influences the re-distribution of particles $>300 \mu \mathrm{~m}$ and $<75 \mu \mathrm{~m}$; heavy-duty traffic influences the re-distribution of particles in the $300-150 \mu \mathrm{~m}$ range; both, heavy and light-duty traffic influence the re-distribution of particles in $150-75 \mu \mathrm{~m}$. It is evident that influence of traffic on the re-distribution of road-

# ACCEPTED MANUSCRIPT 

deposited solids varies between different particle-size ranges. As such, land use also influences particle re-distribution as traffic conditions and particle size distributions vary between different land uses.

Moreover, it is evident that the influence of road surface texture depth is different between the build-up of finer and coarse particles, particularly particles $<75 \mu \mathrm{~m}$ and $>300 \mu \mathrm{~m}$. As such, it can be expected that particles which show positive relationships with texture depth are likely to be retained on road surfaces due to the potentially reduced exposure (given higher texture depth) to traffic induced turbulence. On the other hand, given that traffic is capable of producing strong turbulent eddies (e.g. turbulent air streams created by heavy-duty vehicles), particles that show inverse relationships (negative conditional regression coefficients) with texture depth may be re-distributed even in areas where there is relatively higher texture depth. Therefore, it is important to note that traffic plays a major role in particle redistribution, and in turn the re-distribution of associated pollutants during build-up compared to other influential factors.

### 3.2.3 Influence of traffic on build-up of BTEX

The results of the analysis of prediction performance of the BN model are given in Fig. 3 and Fig. 4. From these figures, it is evident that model predictions are satisfactory for benzene, oxylene and styrene. Accurate relationships between build-up of particle-bound pollutants and the influential factors could be identified only for these three pollutants based on the estimated conditional regression coefficients given in Table 4 (standard errors for the estimates are given in Table S3 in the Supplementary Information). This could be due to the fact that the model was developed based on the current knowledge on pollutant build-up which is predominantly focused on particulate solids rather than particle-bound pollutants.

# ACCEPTED MANUSCRIPT 

Past studies have consistently shown that stormwater pollutants such as toxic hydrocarbons are found in association with particulate solids in urban environments [14, 31, 42-44]. However, the interdependencies between factors that influence pollutant adsorption (e.g. organic matter) are not well understood [31, 32, 45]. Hence, current approaches for designing stormwater pollution mitigation strategies have commonly focused on the accumulated particulate solid loads and subsequent wash-off from urban surfaces rather than the pollutant loads attached to particulate solids. For example, commonly used modelling tools such as MIKE URBAN and SWMM lack accurate mathematical formulations to define pollutant attachment to particulates [46].

Fig. 3

Fig. 4

## Table 4

Therefore, the proposed model needs to be refined by including additional variables in order to improve the prediction performance. This observation implies that the characteristics of pollutant adsorption to particles could vary between pollutant types. As Gunawardana, et al. [47] have pointed out, different pollutants have different chemically reactive surface functional groups, which influence the capacity of pollutant-particulate binding. As such, it is noteworthy that the proposed BN modelling approach not only enables the investigation of the influence of traffic on the re-distribution of pollutants, but also provides the opportunity to identify specific modifications of the model structure required to establish the interdependencies between variables of interest.

# ACCEPTED MANUSCRIPT 

PART B in Table 3 shows the identified relationships between land use, traffic, road surface roughness and the re-distribution of benzene, o-xylene and styrene. It is evident that all three pollutants show positive relationships with all particle size ranges. However, when comparing the conditional regression coefficients relating to the build-up of size fractionated particles and associated pollutants (Table 4), most pollutants can be found evenly concentrated in all particle size ranges. This observation can also be made for BTEX in the majority of the particle size ranges based on the distribution coefficients (ratio between buildup of BTEX and build-up of different particle size fractions) as shown in Table S4 in the Supplementary Information. This means that pollutants do not show a typical pattern such as predominantly being concentrated in finer particle fractions as reported in past research studies (e.g. Goonetilleke, et al. [21] and Gunawardana, et al. [31]).

In general, the positive relationships between BTEX and traffic mean that their loads increase with the increase in traffic volume. This implies that moving vehicles rapidly release BTEX to the road surfaces (namely as a source), such that BTEX will continue to accumulate despite the role of vehicle turbulence on re-distribution. On the other hand, BTEX that show inverse relationships with traffic are expected to result in the decrease in the build-up with the increase in traffic volume. This implies that the impact of traffic turbulence on re-distribution of BTEX overshadows the rate at which vehicles release BTEX to the road surface.

According to PART B in Table 3, given the inverse relationship (negative conditional regression coefficients) with heavy-duty traffic, the majority of BTEX found in commercial and residential areas are likely to be re-distributed due to heavy-duty traffic movement. Although heavy-duty traffic in residential areas is significantly lower compared to commercial and industrial areas, BTEX re-distribution is predominantly influenced by heavyduty vehicle movement rather than light-duty vehicles. In industrial areas, light-duty traffic is likely to influence the re-distribution of BTEX. However, the study results also show that

light-duty traffic volume is higher than heavy-duty traffic volume corresponding to all land use types (as discussed in Section 3.2). Therefore, it can be concluded that the influence of the type of vehicles on pollutant re-distribution caused by turbulence generated [48] may be more significant compared to the influence of traffic volume.

# 4.0 Practical Implications of the Research Outcomes 

According to the study outcomes, urban traffic was found to play an important role in influencing the re-distribution of road deposited particulates and associated BTEX. Vehicle type exerts different influences on the re-distribution process based on land use, and the redistribution process varies with particle size, leading to variability in pollutants build-up on urban road surfaces. Accordingly, build-up is not a continuous process, and hence cannot be accurately replicated by simple mathematical formulations (e.g. reciprocal format, logarithmic format, exponential format and power format), which are currently used in most stormwater quality modelling approaches [49, 50]. This could result in the lack of reliability in the modelling outcomes due to uncertainty caused by the variability (re-distribution) of pollutants build-up as illustrated in Fig. 5.

Therefore, when interpreting stormwater modelling outcomes, it is necessary to consider the land use type and traffic characteristics (light-duty and heavy-duty traffic volumes) in a given area in order to adequately understand the modelling outcomes, which has associated uncertainty. For example, the study outcomes show that light-duty traffic volume has a significant influence on the re-distribution of particles, particularly those smaller than $75 \mu \mathrm{~m}$. This means that the interpretation of stormwater quality modelling results for an area with high light-duty traffic volume should take into account the variability caused by particle redistribution $(<75 \mu \mathrm{~m})$.

Fig. 5

Further, the study outcomes identified the important role of particle size in the re-distribution of particle-bound pollutants such as BTEX. This means that stormwater quality modelling approaches should predict pollutant build-up based on different particle size ranges rather than considering the total load. This will significantly improve the accuracy of stormwater quality predictions.

Moreover, the study outcomes also highlighted the need to account for the factors that influence the build-up of specific particle-bound pollutants in order to enhance model prediction performance. This suggests that accurate mathematical replications of pollutant affinity to particles need to be incorporated when undertaking stormwater quality modelling. Given the flexibility to change the model structure by accommodating new factors (variables) as new knowledge is created (discussed in Section 2.3), BNs can be considered as a versatile approach to accurately model stormwater pollutant processes.

# 5.0 Conclusions 

This paper investigated the re-distribution of road deposited particle-bound pollutants and its relationships with urban traffic, land use type and road surface condition using a Bayesian Network modelling approach. It was noted that the influence of traffic on the re-distribution of particulate solids and associated pollutants is different between vehicle types, and also varies between different particle size ranges. This could lead to uncertainty in the predictions of particle-pollutant build-up, and thereby constrain the in-depth understanding of stormwater quality modelling outcomes. Further, the BN modelling highlighted the need to accurately incorporate the characteristics of pollutant adsorption to particulates in stormwater quality modelling. The research outcomes provide important insights to improve current stormwater

# ACCEPTED MANUSCRIPT 

quality modelling approaches and appropriately interpret modelling results, and thereby contribute to informed decision making in the context of designing effective stormwater pollution mitigation strategies.

## Acknowledgment

We thank National Natural Science Foundation of China (41601510), Shenzhen Science and Innovation Commission (JCYJ20150625103501697; ZDSYS201606061530079) and Natural Science Foundation of SZU (2016007 and 827-000102) for supporting this research study.

# ACCEPTED MANUSCRIPT 

Associated with Particle-bound Pollutant Build-up and Wash-off: A Critical Review, Water Research, 101 (2016) 582-596.
[7] A. Liu, C. Gunawardana, J. Gunawardena, P. Egodawatta, G.A. Ayoko, A. Goonetilleke, Taxonomy of factors which influence heavy metal build-up on urbanroad surfaces, Journal of Hazardous Materials, 310 (2016) 20-29.
[8] B. Wijesiri, P. Egodawatta, J. McGree, A. Goonetilleke, Process Variability of Pollutant Build-up on Urban Road Surfaces, Science of The Total Environment, 518-519 (2015) 434440 .
[9] K.W. Nicholson, J.R. Branson, Factors affecting resuspension by road traffic, Science of The Total Environment, 93 (1990) 349-358.
[10] A. Patra, R. Colvile, S. Arnold, E. Bowen, D. Shallcross, D. Martin, C. Price, J. Tate, H. ApSimon, A. Robins, On Street Observations of Particulate Matter Movement and Dispersion due to Traffic on an Urban Road, Atmospheric Environment, 42 (2008) 3911-3926.
[11] P. Mahbub, G.A. Ayoko, A. Goonetilleke, P. Egodawatta, Analysis of the Build-up of Semi and Non Volatile Organic Compounds on Urban Roads, Water Research, 45 (2011) 2835-2844.
[12] W.C. Hinds, Aerosol Technology: Properties, Behavior, and Measurement of Airborne Particles, John Wiley \& Sons, 2012.
[13] H.Y. Li, A.B. Shi, X.R. Zhang, Particle size distribution and characteristics of heavy metals in road-deposited sediments from Beijing Olympic Park, Journal of Environmental Sciences, 32 (2015) 228-237.
[14] P. Mahbub, A. Goonetilleke, G.A. Ayoko, Prediction model of the buildup of volatile organic compounds on urban roads, Envrionmental Science and Technology, 45 (2011) 44534459 .
[15] Y. Moliner-Martinez, R. Herraez-Hernandez, J. Verdu-Andres, P. Campins-Falco, C.

Garrido-Palanca, C. Molins-Legua, A. Seco, Study of the influence of temperature and precipitations on the levels of BTEX in natural waters, Journal of Hazardous Materials, 263 (2013) 131-138.
[16] T. Sairat, S. Homwuttiwong, K. Homwutthiwong, M. Ongwandee, Investigation of gasoline distributions within petrol stations: spatial and seasonal concentrations, sources, mitigation measures, and occupationally exposed symptoms, Environmental Science and Pollution Research, 22 (2015) 13870-13880.
[17] M. Marć, J. Namieśnik, B. Zabiegała, BTEX concentration levels in urban air in the area of the Tri-City agglomeration (Gdansk, Gdynia, Sopot), Poland, Air Quality, Atmosphere \& Health, 7 (2014) 489-504.
[18] M. Dehghani, M. Fazlzadeh, A. Sorooshian, H.R. Tabatabaee, M. Miri, A.N. Baghani, M. Delikhoon, A.H. Mahvi, M. Rashidi, Characteristics and health effects of BTEX in a hot spot for urban pollution, Ecotoxicology and environmental safety, 155 (2018) 133-143.
[19] S.M. Correa, G. Arbilla, M.R. Marques, K.M. Oliveira, The impact of BTEX emissions from gas stations into the atmosphere, Atmospheric pollution research, 3 (2012) 163-169.
[20] E. Durmusoglu, F. Taspinar, A. Karademir, Health risk assessment of BTEX emissions in the landfill environment, Journal of hazardous materials, 176 (2010) 870-877.
[21] A. Goonetilleke, P. Egodawatta, B. Kitchen, Evaluation of Pollutant Build-up and Washoff from Selected Land Uses at the Port of Brisbane, Australia, Marine Pollution Bulletin, 58 (2009) 213-221.
[22] A. Deletic, D.W. Orr, Pollution buildup on road surfaces, Journal of Environmental Engineering, 131 (2005) 49-59.
[23] P. Egodawatta, E. Thomas, A. Goonetilleke, Mathematical interpretation of pollutant wash-off from urban road surfaces using simulated rainfall, Water Research, 41 (2007) 30253031.

# ACCEPTED MANUSCRIPT 

[24] APHA, Standard Methods for the Examination of Water and Waste Water, in, American Public Health Association, Washington, D.C., 2005.
[25] A.C. Liedloff, E.L. Woodward, G.A. Harrington, S. Jackson, Integrating indigenous ecological and scientific hydro-geological knowledge using a Bayesian Network in the context of water resource development, Journal of Hydrology, 499 (2013) 177-187.
[26] M. Scutari, Learning Bayesian Networks with the bnlearn R Package, arXiv preprint arXiv:0908.3817, (2009).
[27] L. Uusitalo, Advantages and challenges of Bayesian networks in environmental modelling, Ecological Modelling, 203 (2007) 312-318.
[28] I. Ben-Gal, Bayesian networks, Encyclopedia of statistics in quality and reliability, (2007).
[29] M. Scutari, Package 'bnlearn': Bayesian Network Structure Learning, Parameter Learning and Inference, in: Bayesian Network Structure Learning, Parameter Learning and Inference, 2016.
[30] R.C. Team, R: A language and environment for statistical computing, in, R Foundation for Statistical Computing, Vienna, Austria, 2014.
[31] C. Gunawardana, P. Egodawatta, A. Goonetilleke, Role of Particle Size and Composition in Metal Adsorption by Solids Deposited on Urban Road Surfaces, Environmental Pollution, 184 (2014) 44-53.
[32] C. Gunawardana, P. Egodawatta, A. Goonetilleke, Adsorption and Mobility of Metals in Build-up on Road Surfaces, Chemosphere, 119 (2015) 1391-1398.
[33] S. Vardoulakis, E. Solazzo, J. Lumbreras, Intra-urban and street scale variability of BTEX, NO2 and O3 in Birmingham, UK: Implications for exposure assessment, Atmospheric Environment, 45 (2011) 5069-5078.
[34] M. Caselli, G. de Gennaro, A. Marzocca, L. Trizio, M. Tutino, Assessment of the impact

# ACCEPTED MANUSCRIPT 

of the vehicular traffic on BTEX concentration in ring roads in urban areas of Bari (Italy), Chemosphere, 81 (2010) 306-311.
[35] D.O. Atari, I.N. Luginaah, Assessing the distribution of volatile organic compounds using land use regression in Sarnia, "Chemical Valley", Ontario, Canada, Environmental Health, 8 (2009) 16.
[36] B.Z. Yang, B.P.Y. Loo, Land use and traffic collisions: A link-attribute analysis using Empirical Bayes method, Accident Analysis \& Prevention, 95 (2016) 236-249.
[37] R. Zhang, K. Matsushima, K. Kobayashi, Can land use planning help mitigate transportrelated carbon emissions? A case of Changzhou, Land Use Policy, (2017).
[38] Y. Wang, X. Zhu, L. Li, B. Wu, Reasons and Countermeasures of Traffic Congestion under Urban Land Redevelopment, Procedia - Social and Behavioral Sciences, 96 (2013) 2164-2172.
[39] A. Liu, L. Liu, D. Li, Y. Guan, Characterizing heavy metal build-up on urban road surfaces: Implication for stormwater reuse, Science of The Total Environment, 515 (2015) 20-29.
[40] S. Wordley, J. Saunders, On-road turbulence: Part 2, SAE International Journal of Passenger Cars-Mechanical Systems, 2 (2009) 111-137.
[41] S. Wordley, J. Saunders, On-road turbulence, SAE International Journal of Passenger Cars-Mechanical Systems, 1 (2008) 341-360.
[42] B. Bian, W. Zhu, Particle Size Distribution and Pollutants in Road-deposited Sediments in Different Areas of Zhejiang, China, Environmental Geochemistry and Health, 31 (2009) $511-520$.
[43] F. Amato, M. Pandolfi, T. Moreno, M. Furger, J. Pey, A. Alastuey, N. Bukowiecki, A.S.H. Prevot, U. Baltensperger, X. Querol, Sources and Variability of Inhalable Road Dust Particles in Three European Cities, Atmospheric Environment, 45 (2011) 6777-6787.

[44] S.-L. Lau, M.K. Stenstrom, Metals and PAHs Adsorbed to Street Particles, Water Research, 39 (2005) 4083-4092.
[45] B.A. Dempsey, Y.-L. Tai, S. Harrison, Mobilization and Removal of Contaminants Associated with Urban Dust and Dirt, Water Science \& Technology, 28 (1993) 225-230.
[46] MikeUrban, Mouse Pollution Transport - Reference Manual, in: Reference Manual Danish Hydraulic Institue, 2014.
[47] C. Gunawardana, A. Goonetilleke, P. Egodawatta, Adsorption of Heavy Metals by Road Deposited Solids, Water Science and Technology 67 (2013) 2622-2629.
[48] J. Patten, B. McAuliffe, W. Mayda, B. Tanguay, Review of aerodynamic drag reduction devices for heavy trucks and buses, National Research Council Canada NRC Technical Report CSTT-HVC-TR, 205 (2012).
[49] P. Egodawatta, A.M. Ziyath, A. Goonetilleke, Characterising Metal Build-up on Urban Road Surfaces, Environmental Pollution, 176 (2013) 87-91.
[50] J.E. Ball, R. Jenks, D. Aubourg, An Assessment of the Availability of Pollutant Constituents on Road Surfaces, Science of The Total Environment, 209 (1998) 243-254.
[51] J.D. Sartor, G.B. Boyd, Water Pollution Aspects of street Surface Contaminants in, U.S. Environmental Protection Agency, Washington, D.C.
, 1972 .

# ACCESSOIRE 

## Figure Captions

Fig. 1 Locations of study sites (R - Residential; C - Commercial; I - Industrial).

Fig. 2 Structure of the Bayesian Network (BN) model. Note: Conditional density refers to the probability density function of the variables; traffic, solids build-up and particle-bound pollutants build-up, given each of their parent variables.

Fig. 3 Variation in predicted values against observed (measured) data for BTEX build-up.

Fig. 4 Variation in residuals against predicted values of BTEX build-up.

Fig. 5 Variability due to pollutants re-distribution during build-up: (a) theoretical pollutants build-up; (b) pollutants build-up under field conditions (adapted from Sartor and Boyd [51] and Wijesiri, et al. [8]).

# ACCEPTED MANUSCRIPT 

## List of Tables

Table 1 Conditional regression coefficients (intercept) for traffic volume (conditional Gaussian distribution, log transformed data).

Table 2 Conditional regression coefficients for build-up of particulate solids (conditional Gaussian distribution, log transformed data).

Table 3 PART A: Relationships between build-up of size-fractionated particles and traffic volume, road surface condition and land use type; PART B: Relationships between build-up of particle-bound pollutants and build-up of particulate solids, traffic volume, road surface condition and land use type.

Table 4 Conditional regression coefficients for build-up of particle-bound Benzene, oXylene and Styrene (conditional Gaussian distribution, log transformed data).

![img-1.jpeg](img-1.jpeg)

Fig. 1. Locations of study sites (R - Residential; C - Commercial; I - Industrial).

![img-2.jpeg](img-2.jpeg)

Fig. 2. Structure of the Bayesian Network (BN) model. Note: Conditional density refers to the probability density function of the variables; traffic, solids build-up and particle-bound pollutants build-up, given each of their parent variables.

![img-3.jpeg](img-3.jpeg)

Fig. 3. Variation in predicted values against observed (measured) data for BTEX build-up.

![img-4.jpeg](img-4.jpeg)

Fig. 4. Variation in residuals against predicted values of BTEX build-up.

![img-5.jpeg](img-5.jpeg)

Fig. 5. Variability due to pollutant re-distribution during build-up: (a) theoretical pollutant build-up; (b) pollutant build-up in field conditions (adapted from Sartor and Boyd [51] and Wijesiri, et al. [8]).

# ACCEPTED MANUSCRIPT 

Table 1. Conditional regression coefficients (intercept) for traffic volume (conditional Gaussian distribution, $\log$ transformed data).


# ACCEPTED MANUSCRIPT

Table 2. Conditional regression coefficients for build-up of particulate solids (conditional Gaussian distribution, log transformed data).


Table 3. PART A: Relationships between build-up of size-fractionated particles and traffic volume, road surface condition and land use type; PART B: Relationships between build-up of particle-bound pollutants and build-up of particulate solids, traffic volume, road surface condition and land use type.


Note: B - build-up of particulate solids in different size ranges; HT - heavy-duty traffic; LT -light-duty traffic; TD-texture depth

Table 4. Conditional regression coefficients for build-up of particle-bound Benzene, oXylene and Styrene (conditional Gaussian distribution, log transformed data).
