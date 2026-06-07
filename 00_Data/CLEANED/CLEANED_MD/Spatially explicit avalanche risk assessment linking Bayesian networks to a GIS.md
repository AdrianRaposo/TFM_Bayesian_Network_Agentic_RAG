Nat. Hazards Earth Syst. Sci., 6, 911-926, 2006
www.nat-hazards-earth-syst-sci.net/6/911/2006/
(c) Author(s) 2006. This work is licensed under a Creative Commons License.

## Natural Hazards and Earth System Sciences

## Spatially explicit avalanche risk assessment linking Bayesian networks to a GIS

A. Grêt-Regamey ${ }^{1,2}$ and D. Straub ${ }^{3}$<br>${ }^{1}$ WSL Swiss Federal Institute for Snow and Avalanche Research, Research Unit Ecosystem Boudaries, 7260 Davos, Switzerland<br>${ }^{2}$ Eidgenössiche Technische Hochschule Zürich (ETHZ), ETH Hönggerberg, LEP, IRL: HIL H32.1, 8093 Zürich, Switzerland<br>${ }^{3}$ Department of Civil and Environmental Engineering, University of California, Berkeley, CA 94720-1710, USA

Received: 31 May 2006 - Revised: 16 October 2006 - Accepted: 22 October 2006 - Published: 26 October 2006


#### Abstract

Avalanche disasters are associated with significant monetary losses. It is thus crucial that avalanche risk assessments are based on a consistent and proper assessment of the uncertainties involved in the modelling of the avalanche runout zones and the estimations of the damage potential. We link a Bayesian network (BN) to a Geographic Information System (GIS) for avalanche risk assessment in order to facilitate the explicit modelling of all relevant parameters, their causal relations and the involved uncertainties in a spatially explicit manner. The suggested procedure is illustrated for a case study area (Davos, Switzerland) located in the Swiss Alps. We discuss the potential of such a model by comparing the risks estimated using the probabilistic framework to those obtained by a traditional risk assessment procedure. The presented model may serve as a basis for developing a consistent and unified risk assessment approach.


## 1 Introduction

Economical damages from natural hazards are on the rise (MunicheRe, 2006). In order to deal with the increasing costs associated with the damages to buildings, structures, and fatalities, decision-makers need suitable methods to estimate the risks. Especially in mountainous areas such as the Swiss Alps, where snow avalanches (e.g. avalanche winter 1999) and floods (e.g. floods in 2000, 2002, 2005) have caused high costs in the last decade, there is a need for a consistent modelling of the risks. Risk analysis is recognized to be the best method for estimating the dangers from particular natural hazards (e.g. Einstein, 1988; Cruden and Fell, 1997). Risk is defined as a function of the probabilities $\mathrm{P}(A i)$

[^0]of all potential events $A i$ and the expected consequences under these events $C(A i)$ :
$R=\sum_{i} P\left(A_{i}\right) \cdot C\left(A_{i}\right)$
$C(A i)$ can be understood as the product of the damage potential and the corresponding vulnerability (e.g. Varnes, 1984; Morgan et al., 1992).

Estimations of risk using Eq. (1) are dependent on many variables subject to uncertainty. On the one hand, multiple authors have investigated the uncertainties related to the estimation of $P\left(A_{i}\right)$ in recent years (e.g. Barbolini et al., 2003; Ancey et al., 2003; Ancey, 2004). These studies, sited in the field of avalanche hazards, mainly concentrate on the sensitivity of avalanche run-out distances to model assumptions. Because land-use planning based on avalanche hazard maps relies on the calculated run-out distance, these model uncertainties can have large effects on the regional economical development. In Straub and Grêt-Regamey (2006), we present a Bayesian probabilistic framework for modelling avalanche hazards, which serves as a basis for the risk assessment presented in this paper. On the other hand, little attention was directed towards the assessment of the expected consequences $C(A i)$, which is based on a combination of observational information and expert opinion. As a consequence, studies quantifying uncertainties related to this part of the risk assessment are missing. However, failure to include these uncertainties in the risk calculation may lead to significant inconsistencies. Furthermore, explicitly addressing the uncertainties in the model facilitates future model improvements.

Bayesian Networks (BN) are known to facilitate the explicit modelling of uncertainties in an integral probabilistic framework (Friis-Hansen, 2000; Faber et al., 2002). Based on acyclic graphs, BN provide a detailed evaluation of the joint influence of different input parameters on the risk. Allowing a traceable and concise representation of the causal relationships between the considered variables, this is also


[^0]:    Correspondence to: A. Grêt-Regamey
    (gret@nsl.ethz.ch)

highly useful for natural hazard risk assessment, which involves various uncertain variables and requires communication between interdisciplinary groups of specialists. To our knowledge, there are only few reported applications of BN in the field of natural hazards: Amendola et al. (2000) points out the use of BN to consider the chain of indirect damages caused by natural hazards. Antonucci et al. (2003) assess debris flow hazards using credal nets. Hincks et al. (2004) use dynamic BN to model volcanic hazards. Bayraktarli et al. (2005) suggest a generic framework for the assessment of natural hazard risks using BN, and Straub (2005) illustrates the potential of BN for rock-fall hazard ratings. All these studies, however, do not estimate risk in a spatially explicit manner, which is essential for land-use planning.

Geographic Information Systems (GIS) have the capacity to incorporate the complexities of spatial dimension within such analyses. A large number of GIS applications for natural hazards have been developed, particularly during the past decade (e.g., Wadge et al., 1993; Carrara and Guzzetti, 1995; Chen et al., 2003; Bell and Glade, 2004). Until now, in spite of the recognized uncertainties in spatial models and data (Fischer, 1991; Hunter and Goodchild, 1995), the output of GIS has mostly been considered deterministically. We are only aware of one previous attempt at using BN in a spatially explicit manner. Stassopoulou et al. (1998) assess the risk of desertification of burned forests in the Mediterranean region by combining information from different sources of data using a GIS and a BN. This study is based on Aspinall (1992), who uses Bayes' theorem to combine datasets in a GIS for predicting the spatial distribution of red deer in Scotland.

The objective of this study is to show how a BN can be linked to a GIS in order to (1) estimate risk and the associated uncertainties in a spatially explicit manner and (2) explicitly include uncertainties at all levels of the risk assessment procedure. We illustrate the approach by assessing the risk of avalanches in a case study region - the Landscape Davos (Switzerland). We compare the results calculated using the BN approach to those obtained by a traditional risk assessment approach; the latter ignoring the probability distribution of the variables and their joint probability distribution. Furthermore, we identify the major sources of uncertainty and show the potential of Bayesian inference techniques to improve the model using observed data.

## 2 Method

### 2.1 Risk assessment using Bayesian Networks

A generic probabilistic framework for the assessment of natural hazard risk has been suggested by Bayraktarli et al. (2005), and Straub (2005) gives a detailed overview of its composition. It is a breakdown of Eq. (1) into three categories including system exposure $O$, system resistance $F$, and system robustness $K$. The system exposure describes
the probability of occurrence of the potential hazards to the considered system, such as the avalanche hazard event. The system resistance includes all intermediate processes and elements which may modify the exposures in the system, e.g. avalanche defence structures. The system robustness describes how the system reacts on the damaging events, including the behaviour of people in the event of an avalanche. The framework helps structure the problem and provides an overview on all involved processes and aspects. In a generic format, risk can be formulated using conditional terms as follows:

$$
\begin{aligned}
R= & \mathrm{E}_{O, F, K}\left[C_{T}\right]=\int_{O} \int_{F} \int_{K} P(k \mid o, f) P(f \mid o) P(o) \\
& -C_{T}(o, f, k) d k d f d o
\end{aligned}
$$

where E denotes the expected value of the total consequences $C_{T}$ with respect to $O, F$ and $K$. The probabilities $P(k \mid o, f) P(f \mid o) P(o)$ correspond to the first part of Eq. (1), whereas the total consequences $C_{T}(o, f, k)$ correspond to the second part of Eq. (1). Note that the classification of a specific process into the three categories is not strictly prescribed, and should only be viewed as a support to structure the problem.

Risks considered in this study include not only costs of damaged buildings or vehicles, but also costs associated with damaged contents, infrastructure, and societal losses. Of the latter, we consider deaths in buildings and on roads. The loss of productivity in agriculture areas, injuries to livestock, loss of land or cleaning up costs are not included in the analysis, but are object of actual research; inclusion of those factors in the model at a later stage is straightforward.

### 2.1.1 Bayesian Networks (BN)

Pearl (1988) and Jensen (2001) give a comprehensive summary of BN. In the following, we will only give a condensed introduction. BN are a form of probabilistic graphical model. Specifically, BN are directed acyclic graphs in which nodes represent random variables, and the arcs represent dependence relations among the variables. Hence, they provide an intuitive representation of the joint probability distribution $\mathrm{P}(\mathbf{x})$ of a set of random variables $\left(\mathbf{X}=X_{1}, \ldots, X_{n}\right)$. The BN of the avalanche risk assessment developed in this study is given in Fig. 1. The arcs represent causal relations between the random variables. Those are characterized by their associated conditional probability tables, conditional on the states of any parent nodes that interact with it. The joint probability distribution of such a network is given as:
$P(\boldsymbol{x})=P\left(x_{1}, . ., x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \boldsymbol{p} a\left(x_{i}\right)\right)$
where $\boldsymbol{p} a\left(x_{i}\right)$, is a set of values of the parents of $X_{i}$. The distribution of $X_{i}$ given its parents may have any form, but efficient algorithms for solving the BN are available only for

![img-0.jpeg](img-0.jpeg)

Fig. 1. Bayesian Network of avalanche risk assessment. The blue nodes represent the input nodes, the yellow oval nodes represent the causal relations in the system, the red box is a decision node, and the green rhomboid-shaped nodes are the utility functions, characterizing the risk.
the case where the nodes have discrete or Gaussian distributions. Thus, we restrict ourselves to variables with discrete states in this study. BN can be extended to decision graphs by including decision nodes and utility nodes in the network. The decision nodes $\left(D_{i}\right)$ are used to set choices of possible protection measures and are represented as boxes. The rhomboids $\left(U_{i}\right)$ represent the utility nodes; utilities are here quantified in monetary values.

Figure 1 shows the BN for the risk assessment procedure arranged in accordance with the generic categories exposure, resistance and robustness. The blue nodes represent the input nodes, the yellow oval nodes are variables introduced to represent the causal relations in the system and the rhomboid-
shaped nodes are the utility functions, characterizing the risk. The Appendix A gives the description of the content of the conditional probability tables corresponding to each node. The system exposure is expressed as the annual probability of occurrence of snow pressure at a defined location. The two nodes linked to the pressure node represent the posterior avalanche model applied in the risk assessment computations (Straub and Grêt-Regamey, 2006). The system resistance is described by the probability that an avalanche damages buildings, cars or buses. One protection measure (evacuation) and its associated effectiveness are included as a separate box and a node in this part of the network to illustrate their effect on the risk. Several nodes model the relations

describing the robustness of the system, i.e. the consequences of the impact of the avalanche on people or properties. The dependencies can be directly read from the network. Finally, the utility nodes define the expected costs as a function of the number of people killed and the physical damage to cars, buses, and houses. They are expressed in monetary terms.

BN enhance the utilization of evidence in the assessment of risks: Probabilities in the network are updated when new information is available. Finding the conditional distribution of a subset of the variables, conditional on known values for some other subset (the evidence) is the goal of inference. This conditional distribution is known as the posterior distribution of the subset of the variables given the evidence $e$. For example, when the state of a variable is observed to be $e$, this information will propagate through the network and the joint probability of all nodes will change to its posterior:

$$
P(\boldsymbol{x} \mid e)=\frac{P(\boldsymbol{x}, e)}{P(e)}
$$

Several algorithms exist to facilitate the updating of a prior probabilistic model using Bayes' theorem (Murphy, 2001). We select the BN modelling shell Hugin (Hugin Expert, 2005) to solve the equations. We will use Bayesian inference to determine the joint probability distribution of the uncertainties associated with the avalanche model based on observations of avalanches in the case study area.

### 2.1.2 Embedding BN into GIS

In order to estimate the risk on a cell basis, we integrate the BN created in the Hugin environment into ArcGIS 8.3 (ESRI, 2000). The HUGIN API is provided in the form of a library that can be linked to the Visual Basic programming language (Aitken, 1998). Using ESRI's MapObjects 2.2 ActiveX components, the objects contained in the library can be called using the Visual Basic platform available in the ArcGIS environment. Figure 2 shows the modelling framework, which is run for each of the $5 \mathrm{~m} \times 5 \mathrm{~m}$ raster cells of the case study area as follows:

1. The input nodes of the BN are initialized with values provided by spatially explicit datasets. The arrows between the maps and the input nodes of the BN in Fig. 2 illustrate how the BN retrieves the values of the variables from the datasets at each location. For example, the input nodes "building type" and "road type" (see Fig. 1) receive information about the location and the type of building and road at each location from a landuse map. The digital elevation model (DEM) provides information used in the avalanche model to calculate values used as evidence for the conditional probability tables of the "friction parameter" and the "pressure" nodes.
2. For each cell of the case study area, the evidence provided by the spatially explicit datasets is propagated
through the BN. This process is entirely conducted within the Hugin shell, which supplies the mathematical algorithms.
3. The main output of the BN is the annual risk for each cell expressed in monetary terms. These output values are provided in the ArcGIS environment and can immediately be drawn in maps.

### 2.1.3 Avalanche modelling

The probabilistic avalanche hazard modelling is presented in details in Straub and Grêt-Regamey (2006). Here, we provide only an overview.

The model is based on a two-dimensional avalanche dynamic program, the AVAL-2D (Gruber, 1999). The AVAL2D identifies the sizes of avalanche release zones, predicts run-out distances, flow velocities and impact pressures of dense snow avalanches. The sizes of the avalanche release zones are determined based on terrain characteristics and fracture depths. Snow fracture depths are built upon statistical analyses of maximum snow accumulation for three-day periods over the historical record (Salm et al., 1990). As these records only exist for about 60 years, the estimates of snow accumulations for events with a larger return period are extrapolated from the statistical record applying extreme value statistics. The fracture depths are adapted to slope and altitude based on Burkard and Salm (1992). The flow simulation model employs a "Voellmy-fluid" flow law, which assumes small shear strains in the flow body. Flow resistances, given by a dry-Coulomb type friction $(\mu)$ and a velocity squared friction $(\xi)$, are assumed to be concentrated at the base of the avalanche. The latter is here modelled as a deterministic parameter, with different values for different slope angles, topographical classifications (such as open, confined, gully or flat) and surfaces (e.g., a value of $400 \mathrm{~m}^{2} / \mathrm{s}$ is assumed in forest areas). The values of $\mu$ are modelled by groups of stochastic variables, whose probabilistic model is obtained through Bayesian inference from observed avalanches recorded yearly from 1950 to 2003 in the winter reports of the SLF (unpublished data, SLF Davos, Switzerland).

The output of the avalanche hazard analysis is a probabilistic model of the annual maximum of the pressure $P$ at any location. The AVAL-2D establishes a database with the calculated pressure at each cell as a function of the friction parameters and the release scenario. In combination with the joint probabilistic model of the friction parameters and the release scenarios, this represents a complete probabilistic model of $P$, which then serves as input variable to the rest of the risk assessment. As discussed in Straub and GrêtRegamey (2006), we do not include the influence of errors in the numerical avalanche model in an explicit manner.

# ArcGIS 8.3 

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of the integration of a BN created in Hugin into ArcGIS 8.3.

### 2.1.4 Uncertainty analysis

BN represent uncertainty by means of conditional and unconditional probability tables. For example, the node representing building damages describe the probability of different degrees of damages for given building types and given snow pressure. By solving the BN presented in Fig. 1, the uncertainties in the different nodes are propagated through the network and allow the determination of the distribution of the expected cost with respect to these uncertainties.

One of the advantages of using BN in risk assessment is that it facilitates determining which uncertainties should be reduced in order to increase confidence in the model. Not all uncertainties, however, can be decreased by an increase in knowledge. While aleatory uncertainties are inherent to a system and cannot be reduced by more detailed information (Parry, 1996), epistemic uncertainties result from incomplete knowledge of the object under investigation and may be re-
duced as more knowledge about the processes and parameters used in the model is obtained. Assigning the uncertainty sources of our model into these two classes is not always straightforward as in some cases no clear distinction between natural variability and lack-of-knowledge can be made. We will only incorporate epistemic uncertainties in the analysis, as these reflect our confidence in the model. Table 1 lists all the uncertainty sources in our BN and highlights the ones that we consider as epistemic.

To represent the epistemic uncertainty in the analysis, we determine the upper $(u)$ and lower $(l)$ bounds of the $95 \%$ Bayesian credible interval (sometimes also interpreted as confidence interval) for the total cost at each location. These upper and lower bounds are calculated from the distribution of the total cost $C_{T E}$ as:
$u=F_{C_{T E}}^{-1}(0.975)$
$l=F_{C_{T E}}^{-1}(0.025)$

Table 1. Sources of uncertainty in the risk assessment model separated into aleatory and epistemic uncertainty. Only the epistemic uncertainty is considered in the uncertainty analysis.


With $F_{C_{T E}}^{-1}(p)$ being the inverse of the cumulative probability distribution function of the total cost. The probability distribution of $C_{T E}$ is obtained by calculating the total cost for given values of the input variables at each location and by performing the expectation operation with respect to all aleatory uncertainties $\boldsymbol{X}_{A}$ :
$C_{T E}=E_{X_{A}}\left[C_{T}\right]$
In a similar way, the aleatory uncertainties may be analysed, in particular the uncertainties regarding the avalanche release scenarios. The distribution of the total cost with respect to these uncertainties is of utmost importance for the planning of mitigation actions for extreme events.

### 2.1.5 Sensitivity analysis

Another way to establish the effect of the uncertainty associated with the distribution of the variables used in the BN is to conduct a sensitivity analysis. In the present context, it is useful to determine which variables have the largest impact on the uncertainty in the total cost in order to economize resources when improving the model. The Shannon measure of mutual information provides a measure for ranking information sources (Shannon and Waver, 1949; Pearl, 1988). It is an indicator for the overall contribution of all the variables toward reducing the uncertainty in a target variable (T). It is based on the assumption that the uncertainty regarding any variable $X$ characterized by a probability distribution $\mathrm{P}(x)$ can be represented by the entropy function:
$H(X)=H\left(x_{i}, \ldots, x_{n}\right)=-\sum_{i=1}^{n} P\left(x_{i}\right) \log \left(x_{i}\right)$
Based on Eq. (7) Shannon's mutual information, which is interpreted as the total uncertainty-reducing potential of $X$, is defined as (Pearl, 1988):
$I(T, X)=H(T)-H(T \mid X)$

$$
=-\sum_{i=1}^{n} \sum_{j=1}^{m} P\left(t_{j}, x_{i}\right) \log \frac{P\left(t_{j}, x_{i}\right)}{P\left(t_{j}\right) P\left(x_{i}\right)}
$$

Here, the target variable $(T)$ is the total cost of the avalanche hazard in monetary terms, $C_{T}$. To compute this quantity using the BN, we combine all utility nodes into one probability node with states corresponding to the monetary values. The variables $X$ include all the variables described in the BN given in Fig. 1.

### 2.2 Risk assessment using the "traditional approach"

The approach traditionally applied for risk analysis is also based on Eq. (1) (e.g. Wilhelm, 1997). We multiply the probability of each avalanche release scenario by the value of the object exposed to the hazard, the probability of exposure, and the vulnerability. In this study, the results of the AVAL-2D provide snow pressures at each location. These data points are linked to the damage potential using GIS. The data used in the traditional approach is the same as the data used in the BN approach, and is described in detail in Appendix A. But, as opposed to the BN approach, the risk is computed from the expected value of each random variable, thus ignoring the probability distribution of the variables and their joint probability distribution. In other words, we replace all probability distributions of the random variables by the mean probabilities and calculate separately the risk for each building and road type for a given avalanche release scenario. If all the relations among the variables in the BN were linear (e.g. if the lethality in buildings was a linear function of the building damage), then the BN approach would lead to the same results as the traditional approach.

For example, we estimate the building damage costs of a one-family house exposed to a 30-year avalanche release scenario given a snow pressure between 20 kPa and less than 30 kPa by multiplying the probability of a 30-year avalanche release scenario ( 0.03 ) with the probability of damage ( 0.74 ) and a building value of 1.07 Mio CHF, which gives a risk of 23000 CHF. Using the BN approach, we introduce an uncertainty in the variable "building damage" by adding a state "some damage". The risk calculated using the BN amounts then to 17300 CHF .

Authors applying the traditional approach in avalanche risk assessment often approximate modelling uncertainties by means of deterministically defined buffer zones of the avalanche pressure zones. This approach was used, for example, to estimate uncertainties related to the damage potential in the Landschaft Davos by assessing the probable maximum loss (e.g. Fuchs et al., 2005; Bründl et al., 2006), which would correspond to some fractile value of the distribution of $C_{T}$ in our approach.

### 2.3 Case study and data sources

The study area is the "Landschaft Davos", a commune in the eastern part of the Swiss Alps. The area consists of a

![img-2.jpeg](img-2.jpeg)

Fig. 3. The commune of Davos, covering totally $254 \mathrm{~km}^{2}$, is located in the eastern part of Switzerland. The Landwassertal is the main valley, the Dischmatal is a hardly populated SE-oriented side-valley.

NE-SW-oriented main valley (Landwassertal) and four SE-NW-oriented valleys. The Landschaft Davos has always been an avalanche-prone area. The susceptibility of this area to avalanche damages is illustrated by the facts that the altitude of the valley bottoms is at $1400-1600 \mathrm{~m}$ above sea level, and highest peaks are over 3000 m above sea level, approximately $40 \%$ of the precipitations fall as snow, and, as a general rule, a closed snow cover is found from beginning of November to the end of May. In 2000, approximately 13000 inhabitants lived in Davos, and up to 45000 tourists were present during winter time (BfS, 2001). In this study, we will specif-
ically focus on the "Landwassertal" and a sparsely populated side-valley, the "Dischmatal" (Fig. 3). The two areas are delineated based on a valley length of 6 km , and the surface encompassing all avalanche release areas potentially threatening these valley segments.

Main spatially explicit data sources include the vector25 dataset based on the National Map 1:25000 (Swisstopo, 2003), which provides the locations and types of roads and buildings on a resolution of $5 \mathrm{~m} \times 5 \mathrm{~m}$. A detailed forest cover map with forest structures on a $5 \mathrm{~m} \times 5 \mathrm{~m}$ raster based on aerial photographs from 1950 and 2000 was provided by

![img-3.jpeg](img-3.jpeg)

Fig. 4. Total annual risk including fatalities and property damages in the Davos area.

Lardelli (2003). Topographical variables are obtained from the 25 m DEM (DEM25, Swiss Federal Office of Topography) and interpolated to a $5 \mathrm{~m} \times 5 \mathrm{~m}$ raster using the procedure described in Gruber (1999).

Other values used in the risk assessment procedure are based on literature data or were obtained by calculations. Appendix A summarizes the source and values of the data included in the nodes of the BN. Gaussian distributions based on expert knowledge are used to model the variables and relations for which no factual information is available. The probability distribution of each variable reflects its degree of uncertainty. Thus, it is necessary to consider all the available
information about the distribution of each variable. These values can be updated in a later step knowing the importance of their influence on the risk, which is investigated in the sensitivity analysis.

## 3 Results

### 3.1 Risk calculations

Annual risks calculated using the BN in the section considered of the Landwassertal (3.1 Mio. CHF) exceed the annual

Table 2. Comparison of the annual risk given a 30-year and a 300-year avalanche release scenario in a section of the Landwassertal estimated using the traditional approach and a Bayesian Network.


risks in the section of the Dischmatal (1.7 Mio. CHF) by far (Fig. 4). The difference is mainly due to larger number of objects exposed to avalanches in the Landwassertal. The collective risk on roads is negligible in both valleys, amounting to 9500 CHF/year in the Landwassertal and 10900 CHF/year in the Dischmatal. This is because in the Landwassertal, only a few road segments are exposed to risk, in the Dischmatal, the traffic frequency is low. Evacuation measures are calculated to reduce the risk by $10 \%$ in the Landwassertal and $30 \%$ in the Dischmatal. We are, however, not considering risk acceptance criteria for highly exposed individuals such as road workers and rescuers for which specific presence probabilities would have to be assessed.

BN cannot only be used to estimate risk in a spatially explicit manner. They allow also the computation of the total annual risk in a region as associated with the different snow conditions, here represented in a discrete manner through the different release scenarios, as illustrated in Fig. 5. It is observed that the decrease in annual risk under larger and rarer avalanche events is gradual in the Dischmatal. In contrary, the low risk related to smaller avalanche events (the scenario corresponding to an assumed 10 years return period) in the Landwassertal reflects the fact that frequent but smaller avalanches do not reach highly populated areas.

Risk calculated using the traditional approach (6 Mio. CHF in the section of the Landwassertal) is $50 \%$ higher than the risk computed using the BN. The difference is mainly due to the probability distributions introduced in the variables "building damage" and "lethality in building", which
![img-4.jpeg](img-4.jpeg)

Fig. 5. Distribution of the total annual risk in the Landwassertal and the Dischmatal for different avalanche release scenarios.
influence the monetary consequences. Table 2 illustrates this difference in costs by building categories under the 30-year and the 300-year avalanche release scenario. Risks in oneand multiple-family houses, which are by and large at risk in the case study area, are the main drivers of this difference. Furthermore, these results confirm the findings presented in Fig. 5, where the 30-year avalanche release scenario causes more damage than the 300-year avalanche release scenario. In Fuchs and McAlpin (2005), the maximum probable loss for the area was estimated as amounting to 714 Mio. Euro using building insurance values.

Table 3. Shannon mutual information I $\left(C_{T}, X\right)$, Eq. (7), with $C_{T}$ as the total cost of the avalanche hazard, and $X$, all variables influencing $C_{T}$.


All nodes not listed in this table have entropy reduction values of 0 .

### 3.2 Uncertainty and sensitivity analyses

The uncertainty analysis yields Bayesian credible intervals for the overall costs, including all sources of epistemic uncertainty presented in Table 1. The maximum credible interval calculated from these uncertainty distributions is large (1.4 Mio. CHF) compared to the maximal expected cost of 235000 CHF. As the intervals are relevant on the scale of buildings, Fig. 6 shows a credible interval map of a selected area in the Landwassertal. Uncertainties related to costs on roads were not represented as the costs are negligible compared to those of buildings. As all the lower bound values lie between 0 and 1000 CHF , they are not represented in Fig. 6. A comparison of the expected costs with the upper credible interval allows assessing the confidence in the results and the areas of greatest potential error. A map of expected cost values used alone would give a false impression of precision: Risk values located at the border of the avalanche run-out zones have large confidence intervals, pointing to the large uncertainties in the estimation of the costs at these locations, and showing that a more reliable calculation of the avalanche pressures are crucial for reducing the uncertainty in the risk assessment. Furthermore, in zones affected mainly by low pressure avalanches, uncertainties are larger for light weight construction buildings such as agricultural buildings because of the uncertainties related to the size of the damage ("some damage" or "total damage") of these buildings under low avalanche pressures. The fact that the pressure and the house construction nodes are two main sources of uncertainty is confirmed in the sensitivity analysis.

Based on the sensitivity analysis, the variables "house construction" and "people's presence in buildings" are identified as having the greatest influence on the total cost of the
avalanche hazard (Table 3). Next most influential variable is the pressure node. As the source of uncertainty of the variables "house construction" and "people's presence in buildings" is epistemic, this result suggests that decision-makers should prioritize local data collection efforts on these variables rather than on other variables listed in the BN. The uncertainty in the pressure node can be reduced using observed data as described in the next section.

### 3.3 Model improvement

As the avalanche pressure node was identified as having a large influence on the cost values, we applied Bayesian inference to determine a probabilistic model of the variables influencing the calculated avalanche pressure using observations of past avalanches (Straub and Grêt-Regamey, 2006). According to the BN presented in Fig. 1, we are thus including uncertainties related to the physical parameters, and the assumptions made in the release scenario. Figure 7 shows a section of the Landwassertal with the annual probability that an avalanche occurs using the original hazard model and the improved Bayesian model. The original model predicts a larger amount of shorter avalanches, whereas the posterior model predicts fewer but larger avalanches. This pattern is reflected in the risk values amounting to 3.1 Mio. CHF for risk in buildings and on roads using the original avalanche hazard model and 6.5 Mio. CHF under the improved Bayesian probabilistic model. In the original avalanche hazard model, the parameters used in the AVAL2D were based on expert information (Gruber, 1999); in contrary, the parameters in the improved avalanche hazard model were determined using Bayesian inference based on the observation of past avalanches.

## 4 Discussion

BN applied to natural hazards, as described in this paper, has a number of specific advantages over the traditional approach, especially when operated within the context of a GIS.

Primarily, it allows for a consistent modelling of the risk arising from natural hazard. We show that the organization of the risk assessment procedure into a BN supports a structured approach to the interdisciplinary task requiring information from different specialist fields. For example, Fig. 1 shows the complexity of the factors involved in natural hazard risk assessment: The modelling of exposure, usually carried out by natural scientists, the assessment of system resistance as well as the robustness generally performed by engineers, and the monetarisation of the damages involving economists are assembled into a single model, which facilitates the communication between the experts. If specialists identify variables which might have an impact on the risk but are missing data, they still can include them into the structure of the network leaving them uninstantiated. If at a later stage information

![img-5.jpeg](img-5.jpeg)

Fig. 6. Bayesian credible intervals map. The red bars represent the expected cost value at each location; the yellow bars are the upper bound values of the credible interval. The lower bound values are not represented as they all lie between 0 and 1000 CHF . The blue areas represent the avalanche extent under a 300-year scenario.
becomes available regarding these variables, it can then simply be incorporated in the procedure.

Moreover, the integration of the probabilistic approach into a GIS allows quantifying and visualizing uncertainties in a spatially explicit manner, which is a basis to provide credible information to planners. We show that, in the case study area, the risks estimated using a traditional risk approach are approximately $50 \%$ higher than the risks estimated using the BN. Uncertainties are large at the border of the avalanche run-out areas and are visualized in terms of credible intervals of the overall cost values (Fig. 6). Such maps thus allow objectively expressing confidence in the model results and visualizing its geographical variation.

Another advantage of using BN in natural risk assessment is the possibility to identify the variables causing large uncertainties in the results. In this study, we examine the different sources of model uncertainties, and identify uncertainties related to the house construction, people's presence in buildings, and the pressure variables as having the largest impact on the costs. By improving the avalanche model using Bayesian inference (Straub and Grêt-Regamey, 2006) we see that the calculated risk increases by $34 \%$. Such finding is rel-
evant for land-use planning activities such as hazard maps, as uncertainties in avalanche run-out areas can have a large impact on decision-making, especially in view of the increasing pressure to build into the near boundary of the endangered areas. By explicitly addressing these uncertainties, the BN approach allows quantifying their effects and facilitates identifying where future model improvements and data collection efforts should be concentrated. For example, we find that by improving the avalanche run-out model, collecting more data on people's presence in buildings and vulnerabilities of buildings to avalanche pressure, confidence in the risk assessment results can be increased.

Yet, as the causal relationships between the variables influence the results, it is important that the design of the network is discussed in an early planning step with specialists and decision-makers in order to include the important factors in the analysis. Here, we did not include nodes describing the comprehensive valuation of indirect costs. We simply added a percentage of the building costs for quantifying indirect consequences based on the literature. A detailed analysis of the indirect costs including demographical, environmental, medical, psychological, social and economical,

![img-6.jpeg](img-6.jpeg)

Fig. 7. Annual probability that an avalanche occurs, as evaluated with the prior model (a) and the posterior model (b) model. The annual probabilities range from 2.5×10<sup>−9</sup> (brown) to 0.15 (blue).

structural and lifeline, and historical consequences (Faizian et al., 2004) may increase the risk considerably. Furthermore, other uncertainty factors especially related to the GIS data such as the vector25 dataset or the DEM could also be included in such analysis; thus providing an approach to communicate error in spatial databases and study their impact on risk analysis.

The proposed framework offers many possibilities for further development in regard to the assessment and presentation of the spatial and temporal distribution of the risk. In its present version, the BN is evaluated for each cell individually, and thus only the risks and the credible intervals of the costs at each location are assessed. The spatial and temporal dependency structure of the risk is not evaluated. This dependency structure is of eminent importance for the planning of mitigation actions as well as for the inclusion of societal follow-up consequences. A small illustration of this aspect is given in Fig. 5, showing the distribution of the risk under different release scenarios: Objects in the Landwassertal are threatened by less frequent but much larger events compared to objects in the Dischmatal. However, this example is based on the simplifying assumption that the release scenarios are fully independent for the entire area (clearly an unrealistic assumption). Also, other dependencies of the variables in the model are not considered, e.g., the occupancy of different houses is clearly not independent, as the regional economy is dominated by tourism and thus introducing a common temporal fluctuation in housing occupancy. These spatial and temporal dependencies can be included by combining individual BN in the model to one single model. As long as the individual BN are only related through common parent nodes, such a combination is computationally tractable.

If applied for the purpose of defining mitigation action plans, BN integrated into a GIS can be extended to provide a tool for optimal risk based decision making. In this study, we only consider evacuation as protection measure and ignore all the protection measures actually in place at many locations in the case study area. Investigating the effect of different protective actions on the risk values using the framework presented in this paper will be an important future application of the model.

## 5 Conclusions

Considering the importance of an explicit consideration of uncertainties, BN linked to a GIS are supportive for presenting credible risk assessments to decision-makers. The approach unifies human expertise and quantitative knowledge in a coherent framework, which overcomes a major limitation of previous approaches; thus enhancing the understanding of the interdependencies of the involved processes and decisions. Furthermore, confidence intervals represented in a spatially explicit manner support the spatial interpretation of the risk. Lastly, as BN support modelling of the various interdependencies caused by common influencing parameters, such an approach might also have a large potential for linking different natural hazard risks in a single system, which is worthy of further investigation.

Table A1. Values used in the BN nodes, organized into the generic categories exposure, resistance and robustness.


Table A1. Continued.


Acknowledgements. We would like to thank U. Gruber from the SLF for providing data and support for the AVAL-2D, as well as P. Bebi from the SLF and M. Faber from ETH for their suggestions on earlier versions of this paper. Thanks also to M. Schubert from ETH for presenting this study at a conference. This work was partly funded by the Marie Heim-Vögtlin Fellowship 3234-69265 of the Swiss National Science Foundation (SNF). The second author is supported by the SNF through grant PA002-111428.

Edited by: J. M. Vilaplana
Reviewed by: two referees
