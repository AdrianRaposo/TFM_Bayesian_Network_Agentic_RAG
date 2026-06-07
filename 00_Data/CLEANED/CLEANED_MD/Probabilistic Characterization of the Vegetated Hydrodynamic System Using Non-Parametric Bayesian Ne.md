# Article 

## Probabilistic Characterization of the Vegetated Hydrodynamic System Using Non-Parametric Bayesian Networks ${ }^{\dagger}$

Muhammad Hassan Khan Niazi ${ }^{1, *}$, Oswaldo Morales Nápoles ${ }^{1 *}$ and Bregje K. van Wesenbeeck ${ }^{1,2}$ (D)<br>check for updates<br>Citation: Niazi, M.H.K.; Morales<br>Nápoles, O.; van Wesenbeeck, B.K.<br>Probabilistic Characterization of the<br>Vegetated Hydrodynamic System<br>using Non-Parametric Bayesian<br>Networks. Water 2021, 13, 398.<br>https://doi.org/10.3390/w13040398

Academic Editors: Marcel J. F. Stive and Fangxin Fang
Received: 4 November 2020
Accepted: 26 January 2021
Published: 4 February 2021
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (C) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Faculty of Civil Engineering and Geosciences, Delft University of Technology, 2628 CN Delft, The Netherlands; O.MoralesNapoles@tudelft.nl (O.M.N.); bregje.vanwesenbeeck@deltares.nl (B.K.v.W.)
2 Marine and Coastal Systems, Deltares, 2629 HV Delft, The Netherlands

* Correspondence: M.H.K.Niazi@tudelft.nl
+ This paper is an extended version of our paper published in 37th International Conference on Coastal Engineering (2020).

Abstract: The increasing risk of flooding requires obtaining generalized knowledge for the implementation of distinct and innovative intervention strategies, such as nature-based solutions. Inclusion of ecosystems in flood risk management has proven to be an adaptive strategy that achieves multiple benefits. However, obtaining generalizable quantitative information to increase the reliability of such interventions through experiments or numerical models can be expensive, laborious, or computationally demanding. This paper presents a probabilistic model that represents interconnected elements of vegetated hydrodynamic systems using a nonparametric Bayesian network (NPBN) for seagrasses, salt marshes, and mangroves. NPBNs allow for a system-level probabilistic description of vegetated hydrodynamic systems, generate physically realistic varied boundary conditions for physical or numerical modeling, provide missing information in data-scarce environments, and reduce the amount of numerical simulations required to obtain generalized results-all of which are critically useful to pave the way for successful implementation of nature-based solutions.

Keywords: nature-based solutions; seagrasses; salt marshes; mangroves; dependence modeling; nonparametric Bayesian networks

## 1. Introduction

Coastal flood risk is an alarming threat due to increasing hazard and vulnerability as a consequence of climatic and anthropogenic changes [1]. To counter that, protection measures combining conventional and nature-based solutions can constitute robust hybrid defense systems for risk mitigation [2-4]. Moreover, vegetation as a nature-based solution for flood defense, under the umbrella of hybrid solutions (see Figure 1), has shown convincing potential for flood hazard (wave load) reduction [5-16]. Several studies look at vegetation and reduction of currents and waves through numerical modeling [12,15,17-19] or experiments [9,11,14,20], see Table 1. However, combined designs with vegetation and conventional defenses that are implemented in the field are scarce.

Despite many studies focused on hydraulic load reduction by vegetation, there is no general consensus or coherent set of guidelines yet that enable uniform integration of vegetated coastal ecosystems in design for vegetation-levee combinations. This maybe due to the varying estimates of wave attenuation resulting from the case studies. For instance, in Table 1, a few flume and field experimental studies have been synthesized showing a variety of hydrodynamic and vegetation characteristics that were tested to determine drag coefficient expressions. It can be observed that the resulting drag coefficient expressions are considerably different and yield distinct values for the same Reynolds number, see [13]. Since the drag coefficient is a critical variable for the calibration of numerical models, estimates of wave attenuation potential of vegetation also differ considerably, which undermines the reliability of vegetation as an integrated element of a flood defense systems.

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Hybrid and nature-based solutions in the hierarchy of flood defenses. Both conventional and nature-based solutions complement each other in the design of robust hybrid flood defenses.

Instead of case-specific varying point estimates, a wide range of results in multiple biohydrophysical conditions are required which could be generalized to develop the implementation guidelines for nature-based solutions. However, not only the generalized results are missing but the boundary conditions required to measure or model those results are also missing. A potential reason could be the lack of holistic system-level description of vegetated hydrodynamic systems which means that the vegetated foreshores have not been quantified as a system with interacting and correlated constituting elements. Therefore, this study provides a first attempt to develop a probabilistic model of vegetated hydrodynamic system which would help in obtaining the necessary boundary conditions to describe and numerically model the system for a variety of situations more efficiently. We synthesize prior studies parameterizing individual variables in the system [21–29] and build on that to study complete system dynamics and its response to variations.

h = 0.50 m
H_{m0} = 0.036–0.19 m | Polypropylene strips as artificial kelp
h_{v} = 0.25 m, 52 × 0.03 mm,
N_{v} = 1110–1490 m^{-2} | –  |
2200 < R_{e} < 18000  |
200 < R_{e} < 15500
Flex. C_{d} = 0.40 + (4600 / K)
2300 < R_{e} < 22000  |
h = 0.4–1.0 m
H_{m0} = 0.045–0.17 m | L. hyperborea
h_{v} = 0.20 m, b_{v} = 25 mm, N_{v} = 1200 m^{-2} | C_{d} = 0.47 exp(-0.052KC)
3 < KC < 59  |
h = 1–1.5 m
H_{m0} ≈ 0.09 m | Thalassia testundinum
h_{v} = 0.25–0.30 m, b_{v} = 0.33 mm,
N_{v} = 1100 m^{-2} (Used relative velocity for drag calculation) | C_{d} = 0.10 + (925 / K)
200 < R_{e} < 800
C_{d} = 126.45KC^{-2.7}
0 < KC < 6  |
h = 0.3–0.8 m
H_{m0} = 0.05–0.13 m (Reg.)
H_{m0} = 0.03–0.13 m (Irreg.) | Posidonia oceanica
h_{v} = 0.1 m, b_{v} = 3 mm, N_{v} = 40000 m^{-2} | C_{d} = 22.9KC^{-1.09}
15 < KC < 425  |
h ≈ 0.75–3.5 m
H_{m0} ≈ 0.05–0.18 m | Zostera noltii
h_{v} = 0.13 ± 0.030 m,
N_{v,avg} = 625 ± 225 m^{-2} | C_{d} = 0.06 + (153 / K)
100 < R_{e} < 1000  |

Table 1. Cont.


Modeling complex systems requires the (probabilistic) dependence among constituting system components to be taken into account. As a possibility, Bayesian networks (BNs) are being used in different coastal engineering studies [47,48,49,50,51,52,53,54]. A Bayesian network is a directed acyclic graph (DAG) whose nodes represent random variables and whose arcs represent probabilistic dependence. Nonparametric Bayesian networks (NPBN) are hybrid BNs that model the dependence structure using Gaussian copulas and can have both discrete (as long as variables are defined in at least an ordinal scale) or continuous marginal distributions in the same graph [55,56,57,58,59]. A bi-variate copula is a two dimensional distribution of the "ranks" of the data whose marginals are uniformly distributed on [0,1] [60,61,62,63]. Spearman's (conditional) rank correlations, which parameterize the Gaussian copula, are used to define probabilistic influence between parent and child nodes [57,59]. In the case of conditional dependence among variables, recursive formula is used to calculate partial rank correlations [56,64].

Similar studies to this work have mostly applied discrete BNs with conditional probability tables [31,51,65] which are typically quantified with synthetic data sets requiring an enormous number of numerical simulations. This makes the quantification of such models dubious or indefensible. For example, consider a model with 10 discrete variables with 4 states each where 9 variables are connected through an arc to the remaining variable. The number of simulations required to quantify the probability table for the node influenced by the 9 variables would be on the order of one million. Therefore, the number of boundary conditions generated by discrete BNs are so extensive that it would make both physical and numerical modeling costly, labor-intensive, and computationally demanding.

This study introduces dependence modeling using nonparametric Bayesian networks for vegetated coastal systems. The system has been parameterized using continuous distributions and likely (conditional) correlations among variables. The model represents a consistent joint probability distribution and hence can be used to generate conditions that are physically realistic. It adds value to numerical modeling by reducing the number of simulations required to get meaningful generalized results. The paper has been structured as follows: method for parameterization and stochastic modeling in Section 2, resulting NPBNs with dependence information in Section 3, value of dependence modeling in Section 4, and conclusions in Section 5.

# 2. Methodology 

Vegetated hydrodynamic systems were schematized, parameterized, and probabilistically modeled in the user-defined random variable mode of UNINET [57,59], see overall methodology in Figure 2. The parameterization was conducted for benthic, submerged, and emergent vegetation, and the system was categorized into three variable families: (i) hydrodynamic, (ii) vegetation, and (iii) hybrid (dike) variables. Each variable was described with a continuous marginal distribution along with (conditional) rank correlations among variables determined from literature, data, or "in-house" expert judgment. Gaussian-copula based nonparametric Bayesian networks were created for submerged (salt marshes) and emergent (mangroves) vegetation, both combined with a seagrass meadow in the lower intertidal. Monte Carlo sampling was carried out from the NPBNs which resulted in realistic physical conditions sampled from a stochastic model that takes multivariate dependence into account.

### 2.1. System Schematization and Parameterization

To simplify the system hydrophysically, a 1-dimensional cross-shore profile and a dike without a berm were schematized. Vegetation was schematized as rigid cylinders and seagrasses, saltmarshes, and mangroves were modeled as benthic, submerged, and emergent vegetation respectively.

![img-1.jpeg](img-1.jpeg)

Figure 2. Overall methodology and steps for stochastic modeling in UNINET.

# 2.1.1. Schematization 

The schematization in Figure 3 was idealized and divided into 6 segments based on the dominant physical and hydrodynamic processes. Hydrodynamic boundary conditions were defined at the offshore boundary. After nearshore transformation on the ramp, waves reached till the point where they started to "feel" the bottom. At this point on the foreshore, bottom friction started playing a role, mimicking both bed roughness and the benthic vegetation. Waves then encountered a hybrid flood defense system, consisting of mature vegetation (a saltmarsh or mangrove forest) and a dike at the landward extent of vegetation, see Figure 3. The toe of the dike was fixed at $z_{\text {toe }}=0 \mathrm{~m}$ and the rest of the depths were calculated as positive upwards from this reference.
![img-2.jpeg](img-2.jpeg)

Figure 3. Idealized profile used for stochastic modeling including six segments with distinct hydrodynamic and vegetation characteristics.

Vegetation was schematized based on the relative depth between water and vegetation height. Seagrasses were idealized as benthic vegetation, salt marshes as fully submerged with the water depth approaching vegetation height, and mangroves as emergent vegetation with multiple vertical layers, see Figure 4. Seagrasses were modeled as bed friction, salt marshes and mangroves as rigid cylinders parameterized by stem height, drag coefficient, frontal width, and vegetation density.

![img-3.jpeg](img-3.jpeg)

Figure 4. Vegetation schematization: benthic vegetation (seagrasses) as bottom friction, submerged vegetation (saltmarshes) as rigid cylinders and emergent (mangroves) as rigid cylinder with 3 vertical layer schematizations. See nomenclature in appendices for variables' explanation.

# 2.1.2. Variable Families 

The minimum required number of primary variables which could sufficiently describe the hydrodynamic forcing, a vegetation field, and a dike were used (Figure 5). Variations of these variables could reproduce a variety of biohydrophysical conditions observed across the globe. All variables used are listed hereunder:

- Hydrodynamic: Offshore wave height $\left(H_{m 0}\right)$, peak wave period $\left(T_{p}\right)$, water depth $(h)$, and offshore slope $\left(S_{0}\right)$ were grouped as hydrodynamic variables.
- Vegetation: Vegetation forest length $\left(L_{v}\right)$ and vegetation slope $\left(S_{v}\right)$ were general vegetation variables which represented forest characteristics for both saltmarshes and mangroves.
- Benthic vegetation was represented through dimensionless bed friction coefficient $\left(c_{f}\right)$.
- Submerged vegetation was parameterized by vegetation height $\left(h_{v}\right)$, frontal width $\left(b_{v}\right)$, vegetation density $\left(N_{v}\right)$, and drag coefficient $\left(C_{d}\right)$.
- Emergent vegetation had three sub categories for each of the vertical layers.
- Stem height $\left(h_{v, s}\right)$, stem frontal width $\left(b_{v, s}\right)$, stem density $\left(N_{v, s}\right)$, and stem drag coefficient $\left(C_{d, s}\right)$ were put in place for the top layer of mangroves.
- Trunk height $\left(h_{v, t}\right)$, trunk frontal width $\left(b_{v, t}\right)$, trunk density $\left(N_{v, t}\right)$, and trunk drag coefficient $\left(C_{d, t}\right)$ were introduced to schematize the trunk.
- Mangrove roots had height $\left(h_{v, r}\right)$, frontal width $\left(b_{v, r}\right)$, density $\left(N_{v, r}\right)$, and drag coefficient $\left(C_{d, r}\right)$.
- Hybrid: Lastly, dike slope $\left(S_{d}\right)$ and crest level $\left(h_{c}\right)$ were labeled as hybrid variables.


## Hydrodynamic Variables

Generally, wave heights are Rayleigh distributed for a random sea-state but they are Weibull distributed for long time scales [21,66]. Hence, global trends and distribution of wave height and corresponding peak wave periods [67,68] were adopted for $H_{m 0}$ and $T_{p}$. Water depth accounts for the mean sea level, storm surges, tidal fluctuations, and sea level rise due to climate change. Water depth was kept uniformly distributed within a range that was obtained using a breaker index-based $\left(\gamma_{b}=H_{r m s} / h=0.8\right)$ back calculation so that the waves break near the toe of the dike.

## Vegetation Variables

The values for the vegetation variables were synthesized from more than 25 studies to parameterize the vegetation, see Table 1. In addition, similar synthesis results from [31] for salt marshes and from [69] for mangroves were augmented into a literature meta-analysis and were used as a basis to parameterize most of the vegetation variables. However, individual studies that specifically covered global distribution of a certain parameter were preferred over the meta-analysis of this study, e.g., see [27] for mangrove canopy heights.

Moreover, some data was modified during the synthesizing process to optimally fit the study scope. For example, large forest lengths (up to 30 km) [40,65], were curtailed to 1.5 km assuming that the vulnerability of communities protected by such large vegetation forest is negligible. Or dimensionless friction coefficient was calculated using $c_{f}=\frac{g n^{2}}{R^{1 / 3}}$ from the range of Manning's coefficients $(n)$ produced by [70,71] for various vegetation.
![img-4.jpeg](img-4.jpeg)
(a) Vegetated hydrodynamic system idealization
![img-5.jpeg](img-5.jpeg)
(b) Top view
(c) Mangrove vertical schematization

Figure 5. Idealized vegetated hydrodynamic system for stochastic modeling. See nomenclature in appendices for variables' explanation.

# Hybrid Variables 

Dike crest levels were defined as the maximum vertical distances relative to the dike toe and were critical for determining the run-up extent. The maximum crest level was estimated by adding maximum water depth, maximum wave height, and minimum freeboard. The dike slope was used to determine the horizontal distance between the toe of the dike and the crest. Typical ranges of dike slopes and minimum free-board were determined by asking design experts who practice dike design in accordance with criteria mentioned by [72].

### 2.2. Stochastic Model Setup

The stochastic model was made in the user-defined mode of UNINET in order to sample varied vegetated-hydrodynamic conditions. UNINET models nonparametric Bayesian networks which are from the family of hybrid BNs characterized by Gaussian copulas. Setting-up the directed acylcic graph of a NPBN requires marginal distributions of random variables as nodes and (conditional) rank correlations as influences on arcs. Continuous marginal distributions of the random variables (nodes) were defined from a range of parametric distributions available in UNINET, see Table 2. For influences (arcs), bivariate rank correlations were determined through data or expert judgment. Once the DAG was setup, analytical conditioning of the NPBN was performed by UNINET and Monte Carlo samples of variables were generated which established the varied vegetated hydrodynamic conditions.

# 2.2.1. Marginal Distributions 

While determining the marginal distributions, as presented in Table 2, preference was given to published studies that explicitly provide parameterized distributions for variables, e.g., offshore wave height [21], peak wave period [22], and mangrove trunk height [27]. Secondly, when explicit estimates of distributions were not available, data over multiple spatial domains and long temporal scales was used. Only hydrodynamic data of such sort was available which was used to cross-check the marginal distribution and was instrumental in determining rank correlations. However, when multispatiotemporal data was not available, local datasets at specific locations were used to derive the first best assessment of the distributions, e.g., salt marsh height, frontal width, and density. If no data was available, literature was consulted to carry out a meta-analysis aimed to identify general trends about variability of a variable which could be used to infer distributions, e.g., drag coefficient, vegetation, and offshore slope. Except for the variables from published studies, beta distribution was preferred for most of other variables due to its ability to give control of both the bounds (range) and the variability within the bounds (density function).

Table 2. Ranges and marginal distributions for variables in the vegetated hydrodynamic system. Refer to Table A1 for complete description of variable distributions.


# 2.2.2. Correlations and Copulas 

Bivariate rank correlations were calculated from various sources of data and in-house expert judgment as presented in Table 2 and elaborated in following sections. Moreover, in case of conditional dependence, where a child node is dependent on more than one parent node, recursive formula [56,64] in Equation (1) was used to calculate conditional rank correlations. For instance, conditional rank correlation for frontal width and vegetation density given vegetation height $\left(b_{v}, N_{v} \mid h_{v}\right)$ was calculated using bivariate rank correlations of $\left(h_{v}, b_{v}\right),\left(h_{v}, N_{v}\right)$, and $\left(N_{v}, h_{v}\right)$.

$$
\rho_{12 \mid 3}=\frac{\rho_{12}-\rho_{13} \cdot \rho_{23}}{\sqrt{\left(1-\rho_{13}^{2}\right) \cdot\left(1-\rho_{23}^{2}\right)}}
$$

where $\rho_{12 \mid 3}$ is the conditional rank correlation coefficient of random variables $X_{1}$ and $X_{2}$ given $X_{3}$.

## Data Processing

Raw field data was processed to acquire correlation coefficients and synthetic data sampled from an estimated Gaussian copula. An example of data processing is presented for two vegetation variables: vegetation height $\left(h_{v}\right)$ and frontal width $\left(b_{v}\right)$, see Figure 6. The field vegetation data for Chesapeake Bay in the north-eastern part of the US was used from four different stations along a transect containing Spartina alterniflora and Spartina patens species. The raw data in Figure 6a was transformed to the unit square based on its cumulative distribution function (Figure 6b) and the Gaussian copula was estimated (Figure 6c). This copula together with the marginal distributions may be used to sample synthetic data. In Figure 6d, random sampling for both variables was transformed back to original units through the inverse of the cumulative distributions function. Similar analysis of both $h_{v}$ and $b_{v}$ was done in relation to vegetation density and, overall, the rank correlations obtained from this data source were of $\left(h_{v}, b_{v}\right),\left(h_{v}, N_{v}\right)$, and $\left(N_{v}, h_{v}\right)$.

For the hydrodynamic variables, time-series data was obtained for 10 distinct locations over 25 years with 3-hour resolution from waveclimate.com and treated in a similar manner as explained for the vegetation variables. The 10 major deltas with vegetation on foreshores were selected from [74] and representative average values for wave conditions are presented in Table 3. The rank correlation obtained from this data source, as presented in Figure 7, were $\rho\left(H_{m 0}, T_{p}\right), \rho\left(H_{m 0}, h\right)$, and $\rho\left(T_{p}, h\right)$.

Table 3. World wave climate based on ten cities in biggest deltas having vegetated foreshores.


![img-6.jpeg](img-6.jpeg)

Figure 6. Copula and correlations from field data for vegetation height $\left(h_{e}\right)$ and frontal width $\left(b_{e}\right)$.

# Expert Judgment 

In case of unavailability of data or literature, the classical model of expert judgment is an option [55,75-79] to determine rank correlations between two or more variables. In this case, the classical model could not be fully implemented due to limited resource. However, in-house expert judgment was incorporated through verbal communication with experts and elicitation from a combination of general trends from literature. For example, a higher water level would require a higher dike crest level hence the rank correlation for $\left(h, h_{e}\right)$ was defined positive. Overall, individual estimates of experts about the nature (positive or negative) and strength (value) of correlations were collated together to derive estimates of dependence among variables. The correlations defined based on expert judgment, as mentioned in Table 4, were mainly for vegetation and hybrid variables.

![img-7.jpeg](img-7.jpeg)

**Figure 7.** Copulas and correlations determined from data for hydrodynamic variables (*H*<sub>*m*0</sub>, *T*<sub>*p*</sub>, *h*).

The resulting ranges, distributions, and correlations from literature meta-analysis, data processing, and expert judgment are presented in Tables 2 and 4 along with their main source. These quantification results formed the basis for setting up the nonparametric Bayesian networks for salt marshes and mangroves as presented in Figure 8 and Figure 9 respectively.

Table 4. Rank correlations among variables in salt marsh system. See Figure 9 for correlations of mangrove system variables.


![img-8.jpeg](img-8.jpeg)

Figure 8. Nonparametric Bayesian network for salt marsh environment [1,30]. The boxes represent nodes (variables with their marginal distributions) and lines represent influences (rank correlations). Color indicates different components in the system: blue for hydrodynamics, gray for dike, light green for seagrass-saltmarsh variables.

![img-9.jpeg](img-9.jpeg)

Figure 9. Nonparametric Bayesian network for mangroves environment. The boxes represent nodes (variables with their marginal distributions) and lines represent influences (correlations). Color indicates different components in the system: blue for hydrodynamics, gray for dike, light green for general vegetation variables, dark green for stems, brown for trunk, and yellow for roots of mangroves.

# 3. Results 

This work aimed to obtain a better understanding of mangroves and salt marshes and parameters influencing wave attenuation by these ecosystems. This was approached through constructing a stochastic model for salt marshes and mangroves in the form of nonparametric Bayesian networks which capture the dependence among variables of interest. The NPBNs could be used to sample varied vegetated hydrodynamic conditions that tend to coexist in physically realistic windows.

### 3.1. Vegetated Hydrodynamic System

The nonparametric Bayesian network representing salt marsh environment is presented in Figure 8. Overall, the NPBN quantifies the influences between the vegetation and the hydrodynamic variables which eventually captures the underlying dependence

of the system. Interactions among groups of variables (vegetation and hybrid) are linked through hydrodynamic variables as the incoming energy determines both dike crest levels and foreshore slopes. Stem width shows conditional dependence on other variables as it has two parent nodes, i.e., stem height and vegetation density. Variables near the offshore boundary, such as offshore slope and seagrass bed roughness, do not interact actively with the rest of the system and therefore operate as independent variables.

Similarly, for mangrove environments the NPBN is presented in Figure 9. The mangrove variables were divided into three layers (roots, trunk, and stem) due to the differences in their phytomorphological characteristics. Root density plays an important role in this NPBN as it links vegetation slope and forest length to the root layer and further links all mangrove layers to each other. This allows for the maintenance of the harmony between individual plant characteristics and the overall forest characteristics in sampled conditions. Similarly, using the relative emergent property of mangroves, the root height is linked to water depth that conceptually connects hydrodynamic variables to vegetation variables.

Accounting for the multivariate-dependence enables the generation of Monte Carlo samples of variables, which constitute varied boundary conditions. This, for instance, in the case of relatively more energetic hydrodynamic conditions generates samples of reflective beaches, higher and steeper dikes, and higher mangrove roots. Similarly, root variables influence trunk and stem variables as root structure categorizes mangroves into juvenile or mature mangrove types.

# 3.2. Dependence 

The NPBNs are based on a consistent joint probability distribution of all the variables in the network correlated to one another. Due to conditional dependence, more correlations were revealed apart from the ones that were already defined to setup the model, e.g., stem height and drag coefficient. This resulted in a symmetric correlation matrix which indicates the dependence among all variables, see Table 5 for the correlation matrix of the salt marsh system. A value close to 1.0 represents the strongest correlation, e.g., self-correlation on the diagonal, and a value close to 0.0 represents the weakest correlation, e.g., $c_{f}$ and $S_{d}$.

Table 5. Correlation matrix of stochastic model for salt marshes, also see Figure 10. Highest correlation is 1.00, lowest is 0.00 . Positive and negative values show positive and negative correlations. The correlations other than the ones in Figure 8 have been calculated using Equation (1). Similar correlation matrix for mangroves nonparametric Bayesian network (NPBN) is presented in Supplementary Materials.


The correlation matrices generated by UNINET were transformed to adjacency matrices (which use absolute values of correlations) and have been plotted in Figure 10 for both the salt marsh and mangroves NPBNs. Figure 10a,c show all possible correlations among variables. The extensive amount of influences show the inherent complexity of the vege-

tated hydrodynamic system which is undermined when it is studied using deterministic methods. Dominant correlations were filtered out by fixing the correlation threshold to 0.1, see Figure 10b for salt marshes and Figure 10d for mangroves.

![img-10.jpeg](img-10.jpeg)

**Figure 10.** Correlations in global vegetated hydrodynamic conditions in saltmarshes (**a**,**b**) and mangroves (**c**,**d**). The circles represent nodes (variables), lines represent the correlations in the network, and thickness of the lines represents strength of the correlation. Plots (**b**) and (**d**) have minimum correlation threshold of 0.1 to distinguish dominant correlations.

The strength of copulas and dependence modeling allows us to demonstrate the influences which are not initially perceived. For salt marshes an example could be the correlations of wave height with drag coefficient, vegetation height, frontal width, dike slope, and crest level. The strongest conditional dependence is between drag coefficient and vegetation height, followed by wave height and vegetation density, drag coefficient and vegetation density, and vegetation slope and frontal width in salt marshes. For mangroves, the strongest of such "non parent-child" correlations is between trunk height and trunk drag coefficient while other examples include wave height and root height, stem density and vegetation slope, and trunk frontal width and trunk density. This means that the effects on the system of all such correlated variables shown in Figure 10b,d should not be studied in isolation from the other variables, otherwise the true system response (e.g., wave damping) would not be revealed.

# 3.3. Realistic Boundary Conditions 

Analytical conditioning of the stochastic model and Monte Carlo sampling (a process of picking up random values from a probabilistically interpreted system) resulted in logical combinations of variables. Due to the correlations and the joint distribution, two variables are "tied-up" together such that the range of a variable only coexists within a certain range of another variable, e.g., high waves with long periods.

Table 6 shows part of 300 physically realistic combinations of variables in saltmarsh environments representing boundary conditions which could potentially be used for hydrovegetation modeling. The sampled conditions represent combinations of hydrodynamic forcing, physical conditions, sea states, vegetation types, vegetation characteristics, and flood defense extents to cover the entire space of variations that would yield generalized results when analyzed further. An example of the sampling result could be seen in Figure 11 which shows combinations of foreshore slope, forest length, crest level, and dike slope.

Table 6. Monte Carlo samples from NPBN for salt marsh environments.


![img-11.jpeg](img-11.jpeg)

Figure 11. Sampled profiles $(10 / 300)$.
A comparison of the conditions sampled from the salt marsh NPBN as the 'dependent case' with the conditions sampled from an independent DAG with uniformly distributed variables as the "independent case" is presented in Figure 12. For the independent case, sampled combinations cover almost the complete sampling space whereas for the dependent case a variable-specific pattern exists. For example, wave heights and wave periods are not sampled in any recognizable trend for the independent case but the conditions sampled from the stochastic model show positive dependence such that there are almost no conditions sampled for high wave heights with low wave periods or vice versa. When

compared to the data analyzed in this study and the published literature [23,80,81,82,83,84], the independent case deems to be unrealistic and the dependent case is in harmony for the variables whose dependence information is published. Hence, Figure 12 not only shows the pair-wise dependence of variables that emerged beyond the correlations initially defined, but also shows the realistic "windows" of variables where they coexist.

Moreover, the correlation for $\rho\left(H_{m 0}, T_{p}\right)$ was explicitly introduced while setting up the model but the results go beyond the specified correlations and reveal unspecified dependence. For instance, $\rho\left(H_{m 0}, N_{v}\right)$ was not specified initially but the corresponding plot in Figure 12 shows that for higher wave heights the vegetation density seems to have negative correlation and shows signs of tail dependence. This means that less vegetation is expected in high energetic environments. One possible explanation for this could be breakage or uprooting during storms as shown by [85].

![img-12.jpeg](img-12.jpeg)

Figure 12. Comparison of varied vegetated hydrodynamic conditions sampled from an independent DAG with uniformly distributed variables (gray dots) and the stochastic model of this study (black dots) that was quantified with distributions (Table 2) and correlations (Table 4). Yellow panels shows the distinct sampling of the variable pair with positive $H_{m 0}-T_{p}$ and negative dependence $N_{v}-S_{v}$.

# 4. Discussion 

Vegetated hydrodynamic conditions sampled from the salt marsh and mangroves NPBNs could be further used for hydrovegetation numerical modeling, probabilistic modeling, or system-based sensitivity analysis. These conditions help to reduce the number of numerical simulations required to produce generalized results, aid probabilistic analysis in data-scarce environments, and provide a basis for a holistic system-based sensitivity analysis.

# 4.1. Value of Dependence Modeling Using Nonparametric Bayesian Networks 

The value of dependence modeling of vegetated coastal systems for generating varied boundary conditions lies in obtaining physically realistic boundary conditions, which, when simulated, reduces bulk simulation time and increases the authenticity of overall system response. Using this approach will advance current modeling practice as conditions and values for sensitivity analysis are too often randomly or quickly selected instead of being informed by realistic situation. This asks for a good understanding of the biogeomorphological system and goes beyond standard modeling efforts by engineers solely. Hence, even in modeling studies inclusion of biophysical disciplines is essential to achieve realistic results that can be translated to situations encountered in real life.

### 4.1.1. Methodological Value

Many Bayesian network based studies for coastal applications have been published but nearly all of them use discrete Bayesian networks [47-54] except the very few recent ones which use NPBNs [86-89]. In discrete BNs, variables have to be discretized into bins where the number and sizes of the bins need to be correctly fine-tuned to ensure that each bin represents homogeneous information and has nearly similar impact on the child node. This introduces subjectivity as the decisions about bins could vary from person to person which adds another source of uncertainty in modeling discrete BNs. Belonging to the hybrid BNs family, NPBNs provide flexibility to incorporate both discrete and continuous marginal distributions in the same graph, thereby reducing the subjectivity and uncertainty.

### 4.1.2. Reduced Numerical Simulations

Using the sampled boundary conditions from the NPBNs can greatly reduce the number of simulations required to produce generalized results by orders of magnitude. The number of simulations $\left(N_{s}\right)$ required to quantify conditional probabilities of all variables in the system were in the order of $(O)^{4}$ to $(O)^{5}$ for [31,51,65]. The reason for such large $N_{s}$ is that it is a (sum-product) function of the number of variables and the number of permutations per variable, see Equation (2). If any of the two factors increase, the required number of simulations increases geometrically. With 13 variables of seagrass-saltmarshes system even if only 13 permutations per variable are numerically modeled, the number of simulations would go to a gigantic amount of $3.2 \cdot 10^{14}$ which is computationally near to impossible. However, the number of simulations for the method presented in this study are only a function of the number of permutations due to the use of copulas. NPBNs can extract the dependence information even if all variables are varied at once; hence variables can be modeled as many times as the computational capacity permits.

$$
N_{s}=\prod_{i=1}^{n} v_{i}
$$

where, $N_{s}$ is total number of simulations, $n$ is number of variables, $i$ is a given variable, and $v$ is the number of variations of a given variable [90].

### 4.1.3. Filling Information in Data-Scarce Environments

Measured data, especially for vegetation, still remains scarce, however this should not stop the attempts to understand biophysical systems and quantification of the value of nature-based solutions. While modeling such systems, these NPBNs could be used to extract missing information in data-scarce scenarios if all the boundary conditions are not available. The dependence modeling makes sure that the rest of the boundary conditions fall into physically realistic ranges. As an application, this has been illustrated in Figure 13b using the conditions measured for Posidonia oceanica species in the Mediterranean Sea by [39]. First, in Figure 13a only one variable $h$ was conditionalized to observe other dependent variables in a highly data-scarce case. While some variables like $N_{v}=610$ stems $/ \mathrm{m}^{2}$ and $h_{v}=0.826 \mathrm{~m}$ were within less than $3 \%$ error range when compared to the measured ones ( $N_{v}=615$ and $h_{v}=0.8$ ), other variables provided fairly acceptable (but not very

accurate) first-order estimates. Subsequently, more known variables were conditionalized to make the NPBN case specific. The NPBN was updated after conditionalizing $H_{m 0}, h, C_{d}$, $h_{v}$, and $L_{v}$, and the mean values of $N_{v}=736$ stems $/ \mathrm{m}^{2}$ and $b_{v}=0.0096 \mathrm{~m}$ were observed. When compared to measured values of $N_{v}=615$ and $b_{v}=0.0086 \mathrm{~m}$ by [39], the error was found to be within acceptable range ( $19 \%$ and $11 \%$ respectively). It is noteworthy that NPBNs provide an advantage to assimilate new information from newer sources in the existing model [91]. On the other hand, as argued by [92], for the optimal use of probabilistic models subject knowledge and physical understanding about the context of the modeler plays an important role.
![img-13.jpeg](img-13.jpeg)

Figure 13. Case application using the conditions measured by [39].

# 4.1.4. Better System-Based Response 

Thinking in terms of traditional sensitivity analysis, where one variable is varied while keeping all others fixed, the proposed method of conducting sensitivity analysis using correlated boundary conditions that vary all at once has an added advantage. As we believe natural systems are highly dynamic and often show nonlinear responses, the system response to boundary conditions that are varied individually would be comparatively different to the response generated by changing all boundary conditions simultaneously. Therefore, contrarily to the proposed method, traditional sensitivity analysis does not suffice in determining the real system response to varied conditions. Using dependence modeling to generate boundary conditions that vary all together but in a correlated way not only provides physically-realistic conditions but also adds value to any further analysis done using those conditions.

### 4.2. Limitations and Way forward

The limitations of this study are based on simplification choices and the restrictions of the tools used for modeling.

- Rigid Cylindrical Vegetation: Vegetation was modeled as rigid cylinders which do not bend, undergo uprooting, or break in storm conditions which are critical for the system response [85].

- Data Availability: Ideally the statistical description should be derived from the data but due to limited data and responses, stochastic modeling was performed using in-house expert judgment for some of the variables.
- Gaussian Copula: Dependence analysis throughout the study was based on Gaussian copula. However, there is evidence of other dependence structures [80] for the variables in this study.

Recommendations for improvement and future research direction are listed below.

- New field data or data from global models could be obtained to expand the domain and scale of hydrodynamic and vegetation variables both spatially and temporally.
- Better dependence structure, e.g., vines, could be explored since the Gaussian copula is not the most accurate dependence description for some of the variables.

As a way forward, the results from this study in the form of physically realistic vegetated hydrodynamic conditions could be utilized to carry out hydrovegetation numerical modeling. The aim here would be to observe generalized system response in terms of flood hazard reduction potential of vegetation under a variety of conditions. Variables such as the wave attenuation coefficient or run-up could be added to the existing NPBNs from this study to relate physical boundary conditions to the resulting effect of vegetation on hydrodynamics.

# 5. Conclusions 

The vegetated hydrodynamic system was probabilistically parameterized using a range, distribution, and correlations among variables. The system was stochastically modeled using nonparametric Bayesian networks for sea grasses, salt marshes, and mangroves. The resulting NPBNs revealed dominant correlations among variables which derive the dynamics of the vegetated hydrodynamic system. NPBNs also revealed dependence information among variables beyond the pair-wise correlations which were initially quantified to set up the model. Modeling salt marsh and mangrove systems stochastically has enabled assessment of holistic system-based response to variations in individual variables. The NPBNs are capable of generating physically-realistic varied boundary conditions that are useful for further analysis such as reducing hydrovegetation numerical simulations required to acquire generalized information, improving traditional randomly-selected sensitivity analysis with a more cross-disciplinary system-based sensitivity analysis, and filling information in data-scarce environments. The main findings, which were derived by using a NPBN, help to pave the way for generating both generalized and predictive knowledge required for implementation of nature-based solutions in a range of realistic conditions that can be found across global coastal foreshores.

Supplementary Materials: The following are available online at https://www.mdpi.com/2073-444 1/13/4/398/s1, A .txt with 10,000 sampled conditions from both NPBNs for future use. A .txt with correlation matrices for both NPBNs.

Author Contributions: Individual contributions of authors have been acknowledged for the following roles: conceptualization: M.H.K.N., O.M.N., B.K.v.W.; methodology: M.H.K.N., O.M.N.; software, formal analysis, visualization, and writing-original draft preparation: M.H.K.N.; writing-review and editing, supervision: O.M.N., B.K.v.W. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data is contained within the article or Supplementary Material.
Acknowledgments: The authors thank Michelle Gostic and Fred Scott for their comments on the draft.

Conflicts of Interest: The authors declare no conflict of interest.

# Nomenclature 

The following nomenclature has been used in this article:


## Appendix A. Variable Table for Distributions

Table A1. All random variables with their distribution details used in stochastic modeling.


Table A1. Cont.

