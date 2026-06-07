# Rapid earthquake loss updating of spatially distributed systems via sampling-based bayesian inference 

Pierre Gehl ${ }^{1}$ Rosemary Fayjaloun ${ }^{1} \cdot$ Li Sun $^{2} \cdot$ Enrico Tubaldi ${ }^{3} \cdot$ Caterina Negulescu ${ }^{1} \cdot$ Ekin Özer ${ }^{3} \cdot$ Dina D'Ayala ${ }^{2}$

Received: 28 September 2021 / Accepted: 3 February 2022 / Published online: 4 March 2022
© The Author(s) 2022


#### Abstract

Within moments following an earthquake event, observations collected from the affected area can be used to define a picture of expected losses and to provide emergency services with accurate information. A Bayesian Network framework could be used to update the prior loss estimates based on ground-motion prediction equations and fragility curves, considering various field observations (i.e., evidence). While very appealing in theory, Bayesian Networks pose many challenges when applied to real-world infrastructure systems, especially in terms of scalability. The present study explores the applicability of approximate Bayesian inference, based on Monte-Carlo Markov-Chain sampling algorithms, to a real-world network of roads and built areas where expected loss metrics pertain to the accessibility between damaged areas and hospitals in the region. Observations are gathered either from free-field stations (for updating the ground-motion field) or from struc-ture-mounted stations (for the updating of the damage states of infrastructure components). It is found that the proposed Bayesian approach is able to process a system comprising hundreds of components with reasonable accuracy, time and computation cost. Emergency managers may readily use the updated loss distributions to make informed decisions.


Keywords Bayesian inference $\cdot$ Critical infrastructure $\cdot$ Seismic risk $\cdot$ Loss updating $\cdot$ Road network

## 1 Introduction

Rapid loss assessment following an earthquake event is of utmost importance for crisis managers, in order to quantify the extent of the disaster and localize 'hot-spots' before planning adequate emergency measures. Therefore, several rapid response systems have been developed worldwide, as detailed in the review by Guérin-Marthe et al. (2021). Such

[^0]
[^0]:    Pierre Gehl
    p.gehl@brgm.fr
    1 Risks and Prevention Division, BRGM, Orléans, France
    2 Department of Civil, Environmental and Geomatic Engineering, University College London, London, UK
    3 Department of Civil \& Environmental Engineering, University of Strathclyde, Glasgow, UK

tools usually couple shake-maps (i.e., the updated field of ground-motion parameters, based on earthquake's characteristics and recordings from seismic stations) with damage and loss assessment models (i.e., fragility or vulnerability functions). While such systems are mostly applied to common buildings and the estimation of casualties, the treatment of the performance loss of critical infrastructure and its consequences remains mostly overlooked. Only a few rapid response systems include the damage estimation of infrastructure components (e.g., USGS ShakeCast system; Lin et al. 2018), and none of them evaluate losses at system level so far. The study by Toma-Danila (2018) proposes an extensive risk assessment of the functionality of road networks, with measures of intervention times for ambulances and firefighters; however post-earthquake field observations are not taken into account. The inherent complexity of infrastructure systems, composed of interdependent components of various types, poses extra challenges in terms of modelling and simulation time (Franchin 2014).

Moreover, Guérin-Marthe et al. (2021) introduce a distinction between two types of rapid response systems:

- Procedures that do not account for near-real time observations: the characteristics of the earthquake (e.g., magnitude, location, style-of-faulting) are just used to generate a ground-shaking map from a ground-motion model (GMM). Then, this map is fed into damage and loss estimation models in order to generate a very quick overview of the situation (TELES, Yeh et al. 2006; QLARM, Trendafiloski et al. 2011).
- Procedures that couple shake-maps of the event with damage and loss estimation models in order to account for near-real time observations (e.g., USGS PAGER, Wald et al. 2010; ELER, Zülfikar et al. 2017; Auclair et al. 2014).

In the latter case, integrating strong-motion recordings of the event into the shake-map provides more accurate estimates of the intensity measures (IMs) at the vulnerable sites, thus leading to more reliable prediction of losses. However, it should be noted that, in most cases, only the mean values of the shake-map are used in the loss assessment step, ignoring the fact that GMM outcomes describe a full probabilistic distribution of IMs, even when conditioned on observations. A rigorous rapid response system should ensure the propagation of the uncertainties due to the estimation of ground shaking up to loss predictions. Therefore, this paper investigates a proof-of-concept rapid response procedure that would integrate the following features, in answer to the aforementioned gaps: (1) loss estimation for built areas and infrastructure systems, (2) integration of various types of observations to constrain the predictions, (3) propagation of all sources of uncertainty, from hazard to losses, and (4) ability to treat real-world systems over large areas.

In order to address points (2) and (3), Bayesian Networks (BNs) have emerged as a very promising mathematical tool, well adapted to seismic risk analyses that mobilize a probabilistic framework and dependencies between many variables (Bensi et al. 2011). The inference operations on a BN enable the combination of the initial estimates (i.e., prior distribution provided by predictive models) and of field observations (i.e., providing evidence at some nodes) in order to generate updated posterior distributions of the variables of interest, under Bayes' rule. Therefore, thanks to their probabilistic inference capabilities, BNs constitute an adequate solution for the updating of damage and loss estimates in the crisis phase (Bensi et al. 2015). Regarding the ground-shaking part, a shake-map algorithm based on Gaussian BNs has also been proposed by Gehl et al. (2017). Bensi et al. (2013) have demonstrated the application of BN modelling

techniques to the seismic risk assessment of infrastructure systems, thus ensuring the feasibility of point (1).

However, physical infrastructure components are usually strongly interconnected, and most of them contribute to the performance of the system (e.g., sets of bridges contributing to numerous possible routes in a road network). As a result, evaluation of the system performance measure $(S)$ based on the combination of the states of $n$ components is one typical case of dimensionality curse, as the size of the system node $S$ (i.e., linked to the number of parent nodes) grows exponentially with $n$ (i.e., combinatorial explosion). Such limitations hinder the application of exact inference algorithms to large real-world systems (Cavalieri et al. 2017; Gehl et al. 2018), i.e. point (4).

Bensi et al. (2013) have explored various strategies based on the BN's topology in order to alleviate the scalability issue: they advocate the grouping of components into parallel or series sub-systems through the identification of minimum link sets (MLSs) or minimum cut sets, thus limiting the amount of edges converging towards a given node. These BN formulations are all based on discrete variables: continuous variables (e.g., IM) are discretized into interval sets in order to be combined with variables that have discrete states by default (e.g., damage states of a component). More recent efforts have focused on solving this issue by improving data structures in discrete BNs and reducing memory storage via conditional probability matrices (Byun et al. 2019). This matrix-based BN framework has been further generalized by Byun and Song (2021) to be applied to multi-state systems. Thanks to the decomposition into minimum link sets (MLSs) and the identification of super-components (i.e., sub-sets of components that are only in series or parallel), Applegate and Tien (2019) have also proposed a computationally efficient approach that has the capacity to deal with interdependent infrastructure systems.

Alternative BN frameworks have also been proposed, such as the use of a compression algorithm to reduce the memory storage space of the conditional probability table of the system node $S$ (Tien et al. 2016, 2017). On the other hand, Pozzi and Der Kiureghian (2013) have investigated Gaussian BNs, which consist of continuous variables and have therefore the merit of greatly reducing the sizes of (discrete) conditional probability tables (CPTs). However, this approach requires all variables to be represented by a Gaussian distribution, which is not the case of the components' states (i.e., discrete damage states). This strong limitation prevents the use of exact inference algorithms, and approximate inference engines, such as importance sampling or Gibbs sampling, have to be used instead.

The aforementioned issues have been identified and characterized by Cavalieri et al. (2017), who examined current challenges posed by the BN modelling of real-world infrastructure systems, in terms of both computational complexity and level of system analysis (i.e., formulation of the system performance measure). These considerations have led to the development of an approximate BN approach (Gehl et al. 2018), where an incomplete naïve formulation (i.e., a set of component nodes converging towards the system node) is learned from off-line stochastic loss scenarios: although less straightforward to implement, this method is able to deal with large real-world systems and to estimate elaborate system performance measures (i.e., not limited to connectivity analyses). However, this approach is based on the sampling of numerous earthquake events in the exposed area, based on the regional seismicity, which is not required in a rapid response context where the earthquake parameters (location, magnitude) are usually known with reasonable accuracy within minutes (Cremen and Galasso 2020). Moreover, the corresponding BN uses discretized variables in an exact inference scheme, so that the width of the intervals (discrete states) may influence the accuracy of the results.

Most of the aforementioned studies have mostly focused on the component-to-system links (e.g., Byun et al. 2019; Applegate and Tien 2019; Tien et al. 2016), assuming for instance that components are root nodes in the BN, associated with a marginal probability of failure, or that a single root node IM points towards all component nodes. However, in the context of post-earthquake rapid assessment, the accurate consideration of hazardrelated variables leading to component failure probabilities (and their respective correlation structure) is of utmost importance to reach situation awareness. While the modelling of the spatial correlation of seismic IMs has been extensively described by Bensi et al. (2011), its coupling with component and system variables adds yet another layer of complexity. Moreover, seismic responses of components may also be cross-correlated, further complicating the structure of the BN. If a discrete BN formulation is adopted, assuming 20 interval sets for each IM variable (which is not a very accurate description of all possible values) may lead to CPT sizes of up to $20^{n}$ for $n$ vulnerable sites. Strategies to simplify the spatial correlation structure, such as Dunnett-Sobel decomposition (Dunnett and Sobel 1955), may be used; however, they also constitute a form of approximation that becomes less accurate for a large number of sites. As an example, the approximate BN approach by Gehl et al. (2018) has partly solved the component-to-system scalability issue; however, the computational bottleneck has been moved to the joint estimation of IM at the locations of all components in the system.

Therefore, pending the development of ad hoc BN algorithms that are able to address some of the scalability issues, it is proposed here to adopt a more pragmatic approach based on a sampling inference algorithm (i.e., Monte-Carlo Markov-Chain sampling). This procedure, implemented in the OpenBUGS software (Lunn et al. 2009), has the benefit of avoiding some of the scalability issues and of considering different types of variables (continuous and discrete). The objective here is not to introduce new inference algorithms, but rather to exploit state-of-the-art techniques in order to demonstrate the use of BNs in an operational capacity during the rapid response phase. To this end, the following features are put forward in the proposed loss updating procedure:

- Joint estimation of the probabilistic distribution of damage to residential buildings and connectivity loss of a road network;
- Integration of two types of observations (i.e., evidence), namely the knowledge of the IM at some locations of the exposed area (either via accelerometric stations or via macroseismic testimonies) and the estimation of the damage state (DS) of some physical components (from structural health monitoring techniques);
- Modelling of the spatial correlation of IMs, as well as the correlation between seismic capacities of components;
- Idealization of the road network into a conceptual Super-Network, in order to reduce the number of components to process;
- Decomposition of the system into MLSs for connectivity analysis.

Taken separately, none of the above-listed features constitute original developments; however the main novelty resides in their integration under a unique framework in order to facilitate the treatment of large real-world systems. Section 2 of this study details the proposed BN approach for the loss updating of a road network and a built area. A small numerical example is developed in Sect. 3, in order to demonstrate the approach and check the accuracy of the sampling scheme. Then, Sect. 4 applies the BN framework to a realworld area, namely a road network connecting dozens of municipalities in the Pyrenees mountain range (France). Finally, results are discussed in Sect. 5, where a sensitivity study

is also carried out to investigate the influence of parameters that have been seldom studied, such as the correlation between the seismic capacities of the exposed physical components (i.e., bridges and building typologies).

# 2 Proposed approach to update losses from observations 

This section describes the procedure that is put forward to update losses in a rapid response context, by making use of various types of field observations. First, the main principles are outlined, along with the datasets and models that are required for the updating. Then, the process to conceptualize the physical road network into an abstract Super-Network is detailed. Finally, the implementation of the BN in the OpenBUGS software (Lunn et al. 2009) is discussed.

### 2.1 Main principles of the loss updating procedure

The proposed loss updating procedure, summarized in Fig. 1, is articulated around two main types of data:

- 'Static' data, which includes the conventional models and datasets that are needed to perform conventional risk assessment: knowing the characteristics of the earthquake
![img-0.jpeg](img-0.jpeg)

Fig. 1 Proof-of-concept of the procedure for the rapid earthquake loss assessment of built areas and infrastructure systems

(magnitude and location), a GMM is applied to estimate the IM distributions at the locations of the exposed elements, accounting for soil amplification factors. Vulnerability models and fragility curves are also used to predict the damage probabilities of exposed elements, given the IM distributions. Finally, in the case of a road network, the knowledge of the graph topology is also needed in order to access system performance measures such as the network connectivity between two points (Argyroudis et al. 2015). All these models put together result in the prior distributions of the variables of interest (i.e., $I M, D S, S$ ).

- 'Live' data, which represents the observations (strong-motion recordings and damage identification of bridges) that can be entered as evidence in the variables $I M$ and $D S$. The objective is to constrain the prior estimates by generating posterior distributions of the variables of interest, given the evidence.

The road network is subjected to a pre-processing step, with the objective of simplifying the initial graph topology into an abstract Super-Network that is specifically suited to connectivity analysis. This step has the effect of reducing the network's size and complexity, thus facilitating the identification of MLSs. All the data is then entered in a BN structure, which is solved with OpenBUGS: the sampling inference algorithm generates Monte-Carlo Markov Chains (MCMCs), which contain numerous samples of all variables, given the evidence. These samples are finally used to build empirical posterior distributions, with the effect of improving situational awareness for crisis managers. The loss updating procedure is able to generate a wide range of outcomes, such as damage distributions in built areas, damage probabilities of bridges or the probability that the road network connectivity is lost. The seismic response of bridges may also be updated, given the observations of some damaged bridges, so that updated fragility models may be built and applied to subsequent earthquakes.

# 2.2 Road network processing 

The proposed BN model currently relies on the estimation of the connectivity loss of the network, i.e. whether two given locations along the network are still connected or not (binary indicator). Since the analysis is limited to simple connectivity, it is proposed to reduce the complexity of the problem by building a conceptual network (i.e., Super-Network) based on the physical one, via the following steps (see Fig. 2):
(a) Starting from a physical network with $n$ nodes and $m$ edges (among which, $q$ bridges represent vulnerable edges), only nodes that have a degree equal to 1 (extremities of the network) or strictly above 2 (intersections) are kept as nodes of interest.
(b) By virtually removing the $q$ vulnerable edges from the adjacency matrix of the network, it is possible to quickly identify all nodes that are accessible from each other without crossing a bridge (i.e., the nodes that stay connected with each other in the altered adjacency matrix).
(c) These nodes are grouped into a Super-Node: by definition, all nodes belonging to the same Super-Node are always connected with each other. If a bridge is used to connect two nodes within the same Super-Node, it may be removed from the network (such as bridge \#4 in Fig. 2). This assumption is only valid when performing a simple connectivity analysis since other performance measures based on travel distance or duration would require the knowledge of alternate paths and so on.

![img-1.jpeg](img-1.jpeg)

Fig. 2 Illustration of the construction of a Super-Network from a physical network. a Initial physical network; b Connectivity without the vulnerable edges; c Creation of Super-Nodes; d Creation of Super-Edges
(d) The sets of bridges (i.e., vulnerable paths) that are linking two Super-Nodes are identified: this step is facilitated by the fact that only nodes of degree 2 may constitute vulnerable paths (i.e., extremities and intersections are absorbed in Super-Nodes). These paths are referred to as Super-Edges, and they represent sub-systems of bridges in series. Bridges may be then represented by the coordinates of their centroids.

This step leads to a dramatic reduction of the size of the network: in the example in Fig. 2, the initial topology of 15 nodes and 17 edges is simplified into a Super-Network of 2 Super-Nodes and 2 Super-Edges.

In order to identify all MLSs, the recursive algorithm proposed by Cavalieri et al. (2017) has been implemented. It only considers edges (initially, pipelines in a water supply system) as vulnerable components, which is perfectly compatible with the notion of Super-Edge (i.e., representing an in-series system of vulnerable bridges). The recursion starts with the graph $G$ containing all edges and it identifies the shortest path between a predefined origin and destination. Then an edge is removed, and the search for the shortest path continues on the reduced graph $G^{*}$. Each time, the shortest path is stored into the list of MLSs, until the whole network has been explored.

# 2.3 Proposed BN modelling 

BNs organize random variables in the form of a directed acyclic graph, where the dependencies between the various nodes are represented by conditional probabilities. An inference is performed on the BN when one or more nodes are observed (i.e., evidence is entered by specifying a given state) and when the probabilities of the other nodes are updated. In the case of a forward analysis, evidence may be entered at the root nodes, and the updated distributions can be estimated at the child nodes (e.g., distribution of infrastructure losses given the occurrence of some natural hazard events). Conversely, a backward analysis consists in the inference of the root nodes based on the observation of a given child node (e.g., updated distribution of the seismic intensity level given the observation of a given loss level).

It is proposed here to build a BN with the OpenBUGS tool (Lunn et al. 2009), which enables the modelling of continuous and discrete variables in the same BN. The OpenBUGS library is freely available and integrated in the R (www.r-project.org)

![img-2.jpeg](img-2.jpeg)

Fig. 3 Proposed BN formulation for a system decomposed into MLSs and for built areas
environment (see demonstration script in the Electronic Supplement of the paper). This tool has been used in various seismic risk applications, such as the derivation of empirical fragility functions for residential buildings (Ioannou et al. 2020), the updating of damage models for water pipelines (Gehl et al. 2021), or the integration of various types of observations for the identification of structural damage (Tubaldi et al. 2021). The trade-off is the use of approximate inference, via MCMC sampling, instead of exact inference such as the junction-tree algorithm (Huang and Darwiche 1996).

For a given earthquake event, the knowledge of epicentre location and magnitude is assumed. Then, as shown in Fig. 3, the variables involved in the loss assessment are the following:

- The vector IM represents the distribution of the logarithm of the ground-motion parameter of interest (e.g., peak ground acceleration, PGA) at the locations $i=1 \ldots n$ (for $n$ exposed components) and $j=n+1 \ldots n+m$ (for $m$ recordings from seismic stations). It follows a normal distribution of mean $\boldsymbol{\mu}_{\text {logIM }}$ and covariance $\boldsymbol{\Sigma}_{\text {IM }}$.
- The vector $\mathbf{C}$ represents the distribution of the logarithm of the seismic response of the $n$ components, also expressed in terms of IM. It follows a normal distribution of mean $\boldsymbol{\mu}_{\text {logC }}$ and covariance $\boldsymbol{\Sigma}_{\mathbf{C}}$.
- The variables $D S_{i}$ represent the binary damage states $(0=$ failure, $1=$ survival $)$ of the $n$ components. Each $D S_{i}$ is determined as follows:

$$
\left\{\begin{array}{l}
D S_{i}=0 \text { if } I M_{i}>C_{i} \\
D S_{i}=1 \text { if } I M_{i} \leq C_{i}
\end{array}\right.
$$

- The variables $M L S_{k}$ represent the binary states of the $q$ MLSs. In the case of a road network, $M L S_{k}=1$ if the MLS route is accessible (i.e., no failed bridges along the itinerary, if we assume that bridges constitute the weak link of the transport infra-

structure), and 0 if not. An $M L S_{k}$ composed of $p$ components follows the Boolean rule of an in-series system:

$$
M L S_{k}=D S_{1} \times \cdots \times D S_{p}
$$

- The variable $S$ represents the performance measure of the system. In the case of a road network, it corresponds to the accessibility between two given points A and B of the network. Thanks to the MLS decomposition, it follows the Boolean rule of an in-parallel system:

$$
S=M L S_{1}+\cdots+M L S_{q}
$$

With $q$ MLSs, $S$ takes discrete values between 0 and $q$, thus representing the number of possible routes between A and B.

While the left part of the BN in Fig. 3 is relevant for the performance analysis of an infrastructure system (such as the connectivity between two locations along a road network), it is also possible to expand the study by considering the damage to common buildings. In this case, following the approach detailed in Sedan et al. (2013), built areas are represented as polygons (representing building blocks or city districts) of homogeneous seismic vulnerability. Then, the distribution of damage states within each built area is obtained by applying the semi-empirical vulnerability method by Lagomarsino and Giovinazzi (2006). A vulnerability index $V$ is assigned to each built area, and the mean damage grade $\mu_{D}$ is expressed as a function of the EMS-98 macroseismic intensity $I_{E M S}$ (which is obtained from the distribution of IM via ground-motion intensity conversion equations):

$$
\mu_{D}=2.5\left[1+\tanh \left(\frac{I_{E M S}+6.25 V-13.1}{2.3}\right)\right]
$$

Ultimately, the proportion of damage states in each built area, based on the EMS-98 scale (Grünthal 1998), is obtained by applying a discrete beta distribution based on $\mu_{D}$ (Lagomarsino and Giovinazzi 2006). Then, by considering a vector $\mathbf{V}$ of vulnerability indices, of mean $\boldsymbol{\mu}_{\mathbf{V}}$ and covariance $\boldsymbol{\Sigma}_{\mathbf{V}}$, the BN framework for the damage assessment of common buildings may be defined as in the right part of Fig. 3.

The probabilistic variables (IM, C, V) are entered in the OpenBUGS environment, along with the mathematical expressions (e.g., Eqs. 1-4) that are needed to define deterministic variables ( $D S, M L S, S, I_{E M S}, \mu_{D}$ ). Evidence may be entered for $I M_{j}$ (representing ground-motion measurements, as in shake-map procedures), for $D S_{i}$ (the measurement of the damage state of some components) and $\mu_{D}$ (assuming a field inventory of damages in some built areas).

The Bayesian inference is performed by initiating several MCMC chains, with different combinations of initial conditions (i.e., starting values of the probabilistic variables). Each chain is built with a Gibbs sampling scheme, where variables are successively sampled from the posterior distribution of previous variables: the posterior distribution of a variable is obtained from the product of the prior distribution (e.g., the initial estimate of IM) and the likelihood function (probability of a given observation occurring given the prior distribution).

Within each chain, a large number of samples are generated until convergence is considered to be reached, by running tests as a calibration step as shown in Sect. 5.1. The generated samples are then used to estimate empirical statistics of the variables of interest (i.e., posterior distributions).

# 2.4 Definition of prior distributions 

The prior distributions of the variables that are probabilistically defined (IM, C, V) are assumed to follow normal/lognormal distributions, whose parameters are obtained from predictive uncertain models.

In the case of IM, the mean of the logarithm of the ground-motion parameter distribution $\left(\boldsymbol{\mu}_{\text {logIM }}\right)$ is given by a ground-motion model (GMM), based on the earthquake characteristics that are assumed to be known with confidence shortly after the event. The covariance matrix $\sum_{\mathrm{IM}}$ is assembled as follows:

$$
\Sigma_{\mathrm{IM}}=\left[\begin{array}{cccc}
\sigma_{\eta}^{2}+\sigma_{\xi i}^{2} & \cdots & \sigma_{\eta}^{2}+\rho_{i j} \sigma_{\xi i} \sigma_{\xi j} \\
\vdots & \ddots & \vdots \\
\cdots & \cdots & \sigma_{\eta}^{2}+\sigma_{\xi j}^{2}
\end{array}\right]
$$

where $\sigma_{\eta}$ and $\sigma_{\xi}$ respectively represent the standard deviations of the inter- and intra-event error terms, which are given by the GMM. The term $\rho_{i j}$ represents the spatial correlation of the intra-event error between sites $i$ and $j$, and it may be defined by available models in the literature (e.g., Jayaram and Baker 2009).

The seismic response $\mathbf{C}$ of components is provided by fragility curves, where the elements of $\boldsymbol{\mu}_{\text {logC }}$ correspond to the median fragility, and the standard deviations of $\mathbf{C}$ correspond to the fragility dispersion $\beta$. The dispersion term $\beta$ may be further decomposed into $\beta_{R}$ and $\beta_{M}$, which respectively represent the uncertainty due to record-to-record variability and the uncertainty due to imperfect knowledge or modelling of the component (Crowley et al. 2019). A third type of uncertainty, related to the definition of the damage state threshold, is neglected here for simplification purposes. Therefore, the covariance matrix $\sum_{\mathbf{C}}$ is expressed as follows:

$$
\Sigma_{\mathbf{C}}=\left[\begin{array}{cccc}
\beta_{R i}^{2}+\beta_{M i}^{2} & \cdots & \rho_{i j}^{R} \beta_{R i} \beta_{R j}+\rho_{i j}^{M} \beta_{M i} \beta_{M j} \\
\vdots & \ddots & \vdots \\
\cdots & \cdots & \beta_{R j}^{2}+\beta_{M j}^{2}
\end{array}\right]
$$

The term $\rho^{R}{ }_{i j}$, representing the correlation of the response due to record-to-record variability between components $i$ and $j$, is very difficult to quantify without the knowledge of the seismic records used in the derivation of the fragility curves. A qualitative rationale may postulate that components $i$ and $j$ - that are spatially very close to each other - may experience ground motion inputs with similar characteristics in terms of duration, frequency content, etc. and therefore their record-to-record variability should be fully correlated. On the other hand, spatially-distant components are likely to be subjected to different ground motions (e.g., different spectral shapes), and therefore their record-to-record variability should be uncorrelated. Such considerations are discussed in Silva (2019), who advocates the use of a correlation structure similar to the one that models the spatial correlation of the intra-event error. Although deserving further investigation, this assumption is also used here for the characterization of $\rho^{R}{ }_{i j}$.

The correlation of the component-to-component variability within the same class/typology, represented by $\rho^{M}{ }_{i j}$, also requires more knowledge of how the corresponding fragility curves are derived. Therefore, it is proposed to consider the extreme cases in the application (see Sect. 4), namely fully correlated or uncorrelated variability, in order to investigate the impact of these assumptions on the posterior distributions. The decomposition of the dispersion into $\beta_{R}$ and $\beta_{M}$ is not always detailed in available fragility models (i.e., only

the global dispersion $\beta$ is specified). Various assumptions regarding this decomposition are also tested in the application example.

Finally, the vulnerability indices $\mathbf{V}$ of built areas are obtained from a field inventory by structural engineers. The standard deviations of the elements of $\mathbf{V}$ may be obtained from the upper and lower bounds of the vulnerability estimates (e.g., see Table 3 of Lagomarsino and Giovinazzi 2006). Regarding the correlation structure, the same issues discussed for the definition of $\sum_{\mathbf{C}}$ hold for $\sum_{\mathbf{V}}$.

# 3 Numerical verification of the sampling algorithm 

This section investigates the accuracy of the OpenBUGS BN on a synthetic test-case. To this end, a Gaussian BN is introduced as the reference solution for the small studied system.

### 3.1 Definition of the synthetic system

The accuracy of the sampling-based inference scheme used in OpenBUGS is firstly investigated on a trivial synthetic system. Two components arranged in-series (e.g., two bridges that must be crossed to go from one point to another) are considered: they are respectively 10 and 15 km away from an earthquake epicentre (with assumed magnitude $\mathrm{M}_{\mathrm{w}} 6.3$ ). A PGA observation is added, located at a site 12.5 km from the epicentre (at an equal distance between the two components). Therefore, the corresponding BN is built for a vector IM containing 3 elements (the first two representing the sites of the components, and the last one the observation), and a vector $\mathbf{C}$ containing 2 elements (one for each component). The marginal and conditional probabilities of all variables involved in this BN are expressed as follows, using the same convention as in Sect. 2.3 (Eq. 1 to 3):

$$
\begin{aligned}
& P_{\mathrm{IM}}(\mathbf{i m})=\varphi\left(\log \mathbf{i m}, \boldsymbol{\mu}_{\log \mathrm{IM}}, \boldsymbol{\Sigma}_{\mathrm{IM}}\right)=\varphi\left(\log \mathbf{i m},\left[\begin{array}{l}
0.3346 \\
0.0878 \\
0.2025
\end{array}\right],\left[\begin{array}{llll}
0.1815 & 0.0740 & 0.1132 \\
0.0740 & 0.1815 & 0.1132 \\
0.1132 & 0.1132 & 0.1815
\end{array}\right]\right) \\
& P_{\mathbf{C}}(\mathbf{c})=\varphi\left(\log \mathbf{c}, \boldsymbol{\mu}_{\log \mathrm{C}}, \boldsymbol{\Sigma}_{\mathbf{C}}\right)=\varphi\left(\log \mathbf{c},\left[\begin{array}{l}
-0.0083 \\
-0.0083
\end{array}\right],\left[\begin{array}{ll}
0.2000 & 0.0400 \\
0.0400 & 0.2000
\end{array}\right]\right)
\end{aligned}
$$

where $\varphi(\bullet, \boldsymbol{\mu}, \boldsymbol{\Sigma})$ is the multivariate normal probability density function, of mean $\boldsymbol{\mu}$ and covariance $\boldsymbol{\Sigma}$.

$$
\left\{\begin{array}{l}
P\left(D S_{1}=d s_{1} \mid i m_{1}, c_{1}\right)=\left(1-d s_{1}\right) \cdot H\left(i m_{1}-c_{1}\right)+d s_{1} \cdot H\left(c_{1}-i m_{1}\right) \\
P\left(D S_{2}=d s_{2} \mid i m_{2}, c_{2}\right)=\left(1-d s_{2}\right) \cdot H\left(i m_{2}-c_{2}\right)+d s_{2} \cdot H\left(c_{2}-i m_{2}\right)
\end{array}\right.
$$

where $H(\bullet)$ is the Heaviside function, $d s_{i}=0$ denotes failure and $d s_{i}=1$ denotes survival, for $i=1,2$.

$$
P\left(S=s \mid d s_{1}, d s_{2}\right)=(1-s) \cdot\left(1-d s_{1} \cdot d s_{2}\right)+s \cdot d s_{1} \cdot d s_{2}
$$

where $S=0$ denotes disconnection (at least one of the in-series bridges has failed) and $S=$ 1 denotes accessibility.

Fig. 4 Gaussian BN used for the numerical verification on the synthetic example. Red circles represent nodes that are evidenced (see Sect. 3.3)
![img-3.jpeg](img-3.jpeg)

# 3.2 Verification method 

Such a system is small enough to be solved with a BN using an exact inference algorithm such as the junction-tree technique. However, the discretization of all continuous variables $(I M, C)$ also represents a challenge that could lead to inaccuracies in the outcome. Therefore, it is proposed to apply a Gaussian BN to the problem described in Sect. 3.1. A Gaussian BN contains only continuous variables with normal distributions and it also has the benefit of being compatible with exact inference algorithms. The Gaussian BN is presented in Fig. 4, with the following set of variables and their related distributions:

- $U_{i}, i=1,2,3$ : Standard normal variables that are used to model the correlation between the IMs.

$$
U_{i} \sim \mathcal{N}(0,1)
$$

- $V_{i}, i=1,2$ : Standard normal variables that are used to model the correlation between the seismic capacities of the components.

$$
V_{i} \sim \mathcal{N}(0,1)
$$

- $I M_{i}, i=1,2,3$ : Logarithm of the IM of interest (here, PGA), which follows a normal distribution where the mean is the linear combination of conditioning variables $U_{i}$.

$$
I M_{i} \sim \mathcal{N}\left(I M_{0, i}+\sigma_{i} \sum_{j=1}^{i} t_{i j} U_{j}, \epsilon^{2}\right)
$$

In Equation (13), the terms $t_{i j}$ are elements of the transformation matrix $\mathbf{T}$, which is used to generate a correlated vector $\mathbf{Z}$ of standard normal variables by transforming the independent variables $U_{i}$ (assembled into the vector $\mathbf{U}): \mathbf{Z}=\mathbf{T U}$. The lower triangular matrix T results from the Cholesky decomposition of the correlation matrix $\mathbf{R}$, which is obtained from the covariance matrix $\sum_{\mathrm{IM}}$ in Eq. (5). $I M_{0, i}$ represents the mean GMM estimation of IM at location $i$, and $\sigma_{i}$ is the standard deviation provided by the GMM.

- $C_{i i^{\prime}}=1,2$ : Logarithm of the seismic capacity of component $i$, which follows a normal distribution where the mean is the linear combination of conditioning variables $V_{i}$.

$$
C_{i} \sim \mathcal{N}\left(C_{0, i}+\beta_{i} \sum_{j=1}^{i} t_{i j}^{\prime} V_{j}, \varepsilon^{2}\right)
$$

In Equation (14), the terms $t^{\prime}{ }_{i j}$ are elements of the transformation matrix $\mathbf{T}^{\prime}$, which is used to generate a correlated vector $\mathbf{Z}^{\prime}$ of standard normal variables by transforming the independent variables $V_{i}$ (assembled into the vector $\mathbf{V}$ ): $\mathbf{Z}^{\prime}=\mathbf{T}^{\prime} \mathbf{V}$. The lower triangular matrix $\mathbf{T}^{\prime}$ results from the Cholesky decomposition of the correlation matrix $\mathbf{R}^{\prime}$, which is obtained from the covariance matrix $\sum_{\mathrm{C}}$ in Eq. (6). $C_{0, i}$ represents the prior mean of the seismic capacity of component $i$, and $\beta_{i}$ is the standard deviation provided by the fragility curve.

- $D_{i}, i=1,2$ : Damage indicator of component $i$, which follows a normal distribution where the mean is the linear combination of conditioning variables $I M_{i}$ and $C_{i}$.

$$
D_{i} \sim \mathcal{N}\left(C_{i}-I M_{i}, \varepsilon^{2}\right)
$$

The damage indicator is a continuous variable, however it may be easily interpreted as a discrete damage state. If $D_{i}$ is positive, then it means that $C_{i}>I M_{i}$, which translates into $D S_{i}=1$, as defined in Eq. (1). Conversely, $D_{i}$ being negative implies that $D S_{i}=0$ (i.e., component failure). Therefore, without breaking the Gaussian assumption in the BN, it is possible to access $P_{f, i}$, the probability of failure of component $i$ :

$$
P_{f, i}=P\left(D_{i} \leq 0\right)=\Phi\left(-\frac{\mu_{D_{i}}}{\sigma_{D_{i}}}\right)
$$

where $\mu_{D i}$ and $\sigma_{D i}$ are respectively the mean and standard-deviation of variable $D_{i}$, which are obtained when solving the Gaussian BN. $\Phi$ represents the standard normal cumulative distribution function.

The resulting Gaussian BN in Fig. 4 is implemented in the Bayes Net toolbox (Murphy 2001), which has the ability to apply exact inference (i.e., junction-tree algorithm) to continuous Gaussian variables.

With the proposed Gaussian BN, an issue arises when needing to specify that a given component $i$ has failed or survived as an evidence. Since such an evidence takes the form of an inequality (e.g., $D_{i}>0$ for survival), it cannot be entered directly into the BN, which can only treat hard evidence (i.e., a scalar value determining a continuous variable). Therefore it is proposed to decompose the posterior distributions over all possible values of $D_{i}$, given the damage state of the bridge. A similar decomposition framework for the treatment of soft evidence has been introduced by Fayjaloun et al. (2021). Let $Y$ be a variable of interest in the BN; then its posterior distribution given the observation of $D S_{i}=1$ is decomposed as follows:

$$
P\left(Y \mid D S_{i}=1\right)=\int_{-\infty}^{+\infty} P\left(Y \mid D_{i}\right) P\left(D_{i} \mid D S_{i}=1\right) d D_{i}
$$

$\mathrm{P}\left(D_{i} \mid D S_{i}=1\right)$ represents the conditional probability of observing the value $D_{i}$ given the damage state of the component: this probability is estimated by using the a priori distribution of $D_{i}$ and by truncating its probability density function, named $p_{\text {trunc }}$ (i.e., keeping only the positive part of the support and normalizing the function):

![img-4.jpeg](img-4.jpeg)

Fig. 5 a Prior distribution of $D_{i}$; b Truncated and normalized distribution of $D_{i}$; c Discretized weights applied to the decomposition

$$
P\left(Y \mid D S_{i}=1\right)=\int_{-\infty}^{+\infty} P\left(Y \mid D_{i}\right) p_{\text {trunc }}\left(D_{i}\right) d D_{i} \approx \sum_{k} P\left(Y \mid D_{i}=\frac{D_{i, k+1}+D_{i, k}}{2}\right)\left[P_{\text {trunc }}\left(D_{i, k+1}\right)-P_{\text {trunc }}\left(D_{i, k}\right)\right]
$$

where $P_{\text {trunc }}$ represents the cumulative distribution function of $D_{i}$. If a discretization is applied to the continuous variable $D_{i}$, then the integral may be approximated by summing over the discrete intervals $\left[D_{i, k} ; D_{i, k+1}\right]$, as shown in Fig. 5.

With a very refined discretization, this approach is able to converge quickly towards the exact solution. However, it requires to loop over a large number of BNs (each time defined with a different evidence value), and the computations using such an approach become intractable when several observations need to be entered. Therefore, this method is only used on the trivial synthetic example in order to provide trustworthy results that can be compared to the MCMC sampling-based approach.

# 3.3 Results 

The comparison between the Gaussian BN and the OpenBUGS outcomes is detailed in Table 1, by considering two evidence scenarios: scenario 1 only considers that $\log i m_{3}=$ -0.1 ; while scenario 2 assumes that an additional type of observation is available, i.e. that component \#2 has survived (i.e., $d s_{2}=1$ ). The R script that builds the corresponding OpenBUGS BN is provided as an Electronic Supplement of the paper, as a demonstrator of the updating procedure. An example of OpenBUGS model is shown in Fig. 6.

Due to the sampling approximation present in both methods, the posterior values cannot be perfectly matched; however, they are in very close agreement, and most discrepancies appear around the 3rd or 4th decimals. Such a level of precision is sufficient for seismic risk applications since it appears that the mismatch is negligible in light of the much greater uncertainties that usually accompany loss assessment models. This numerical test is also an opportunity to verify the soundness of the Bayesian modelling assumptions: all variables are updated given the evidence, and their posterior distribution is shifted in the expected direction (e.g., reduction of the seismic intensity due to

the observation of a low-intensity $i m_{3}$, better seismic resistance of the components due to the observation of the survival of component \#2, etc.). It is also worth noting that the uncertainty on these variables is gradually reduced as more evidence is entered (i.e., smaller standard-deviations in evidence scenario 2).

A more systematic investigation of the updating capabilities of the BN approach is shown in Fig. 7, where the values of $i m_{3}$ are gradually increased in evidence scenario 2. The top plots show the evolution of the posterior distributions of variables $I M_{2}$ and $C_{2}$, in terms of 16 th, 50 th and 84 th percentiles, obtained with the OpenBUGS approach. The bottom plots show the evolution of the error between the Gaussian BN (GBN) and OpenBUGS (OBN) estimates, which is defined as follows:

$$
E r r=\frac{E\left[Y \mid I M_{3}=\operatorname{im}_{3}, D S_{2}\right]_{O B N}-E\left[Y \mid I M_{3}=\operatorname{im}_{3}, D S_{2}\right]_{G B N}}{E\left[Y \mid I M_{3}=\operatorname{im}_{3}, D S_{2}\right]_{G B N}}
$$

On the right plots of Fig. 7, evidence scenario 2 is modified in order to consider the case where the failure of component \#2 is observed.

From Fig. 7, the following points may be noted:

Table 1 Posterior distributions of the variables of interest, for the two evidence scenarios. Observed values (evidence) are in bold font. $\mathrm{C}_{\mathrm{i}}$ and $\mathrm{IM}_{\mathrm{i}}$ are expressed in $\log \mathrm{m} / \mathrm{s}^{2}$


- In the case that $D S_{2}=1$ is observed, $C_{2}$ is well above $I M_{2}$ for low values of $i m_{3}$ and the gap narrows as $i m_{3}$ increases. $I M_{2}$ is influenced by the evidence of $I M_{3}$ and tends to increase, which has the effect of forcing $C_{2}$ to increase even more in order to respect the condition $D S_{2}=1$. It has also been found that the correlation between $I M_{2}$ and $C_{2}$ increases, reflecting the higher constraints that are applied by large values of $i m_{3}$.
- In the case that $D S_{2}=0$ is observed, low values of $i m_{3}$ induce low values of $I M_{2}$ as well, forcing $C_{2}$ to be reduced dramatically. As $i m_{3}$ increases, the constraints become more relaxed, and $I M_{2}$ increases enough so that $C_{2}$ deviates less from its prior distribution.

![img-5.jpeg](img-5.jpeg)

Fig. 6 OpenBUGS model for scenario 2. Observations (evidence) are the quantities Dobs and IMobs
![img-6.jpeg](img-6.jpeg)

Fig. 7 Top left: posterior distributions of variables $I M_{2}$ and $C_{2}$, in terms of 16 th, 50 th and 84 th percentiles, with evidence $I M_{3}=i m_{3}$ and $D S_{2}=1$; Top right: posterior distributions of variables $I M_{2}$ and $C_{2}$, in terms of 16 th, 50 th and 84 th percentiles, with evidence $I M_{3}=i m_{3}$ and $D S_{2}=0$; Bottom: Error rate between the Gaussian BN and OpenBUGS estimates

- Regarding the error rates, no significant biases or trends are observed. The errors seem to be well constrained under 0.03 (i.e., around $3 \%$ of deviation at the maximum), confirming the suitability of the sampling-based BN for the problem at hand.


# 4 Application to a real road network 

This section describes the case-study area in the French Pyrenees mountain range and the construction of the corresponding BN model.

### 4.1 Description of the case-study area

The proposed BN approach for rapid response is applied to a road network composed of 118 bridges (i.e., vulnerable components), which connects 53 municipalities (i.e., built areas) located in a valley around Bagnères-de-Luchon (Pyrenees, France). The case-study area is detailed in Fig. 8.

The typologies of the 118 bridges are identified based on photographs and aerial pictures, and their conditional probability of failure is defined by fragility functions, some of which are taken from the SYNER-G database (Crowley et al. 2011). The most common bridge type consists of short single-span bridges (length $<50 \mathrm{~m}$ ), followed by masonry arch bridges. In total, 18 different fragility curves have been assigned ( 3 models for the 83 single-span bridges, 3 for the 7 continuous multi-span bridges, and 12 for the 28 arch bridges). The fragility curve corresponding to the first limit state is considered as the
![img-7.jpeg](img-7.jpeg)

Fig. 8 Situation map of the Luchon case-study area

threshold of the loss of functionality of the bridge (i.e., failure of the component), assuming that even small structural damage might be enough to prevent safe passage.

For the 53 municipalities, the information concerning the characteristics of the residential buildings is extracted from the building census data freely provided by the French National Institute of Statistics and Economic Studies (INSEE). From INSEE data, we are using mainly three items: the building type (e.g. individual building, collective building ...), the number of stories and the construction age period. We associate the age period range of construction to the evolution of the construction technics and the evolution of seismic design codes. With these data, we classify the different buildings types into the EMS-98 vulnerability classes (Grünthal 1998). For each building type in each municipality, we estimate the associated number of buildings and the associated population. Then, for the building types distributed into the EMS-98 classes, we estimate the RISK-UE vulnerability indices based on the method developed by Lagomarsino and Giovinazzi (2006).

The studied area is surrounded by several seismic stations (see Fig. 8), which are used as sources of observations to constrain estimates of the strong-motion field. All selected fragility curves use PGA as IM; therefore, the regional GMM by Tapia (2006) is applied here for the estimation of the prior distribution of IM. For PGA, the spatial correlation model by Jayaram and Baker (2009) is expressed as:

$$
\rho_{i j}=\exp \left(-\frac{3 h}{8.5}\right)
$$

where $h$ is the inter-site distance in km.
Finally, site effects are modelled via soil amplification factors, which were estimated from local investigations and soil measurements (Roullé et al. 2012).

# 4.2 Construction of the BN model 

The assembled Super-Network is displayed in Fig. 9, where the position of the abstract Super-Nodes is estimated as the mean of the coordinates of the nodes belonging to each Super-Node. This preliminary step leads to a dramatic simplification of the network since the initial 607 nodes and 689 edges are now replaced by 52 Super-Nodes and 67 SuperEdges. Out of the initial 118 bridges, only 96 are kept in the Super-Network, since some of them are not useful to ensure the connectivity between Super-Nodes.

For demonstration purposes, the connectivity between a location A (downtown of Bag-nères-de-Luchon) and a location B (Northern end of the road network) is studied here, in order to simulate the possibility to send rescue teams from the North to the affected area after a potential earthquake (see Fig. 9). Thanks to the Super-Network conceptualisation, the decomposition of all possible paths between A and B becomes computationally manageable: 60 MLSs are identified, mobilising 25 bridges in total (i.e., most bridges are involved in multiple MLSs), as shown in Fig. 10.

Finally, this structure is implemented in OpenBUGS in order to build the corresponding BN, which contains the following nodes:

- The vector IM, containing 156 elements ( 96 bridge sites +53 built area centroids +7 observations);
- The vector $\mathbf{C}$, containing 96 elements;
- The vector $\mathbf{V}$, containing 53 elements;
- 96 DS nodes;

![img-8.jpeg](img-8.jpeg)

Fig. 9 Construction of the Super-Network from the physical network

- $53 \mu_{D}$ nodes;
- 60 MLS nodes;
- $1 S$ node.

The updating capabilities of the BN are tested with a hypothetical Mw 6.3 earthquake scenario, located south of the road network ( $0.60^{\circ}$ lon, $42.65^{\circ}$ lat). Hypothetical observations from 7 seismic stations and damage measures on 5 bridges are set as evidence in the BN ( 2 survivals and 3 failures). It is assumed that one of the monitored bridges belongs to the identified MLSs, and it has been observed as intact (see Fig. 10).

# 5 Results and discussion 

This section details the updated loss distributions obtained from the BN while discussing the impact of various factors, such as the number of MCMC samples or the correlation between the seismic response of the bridges.

### 5.1 Checking the accuracy of the updated ground-motion field

As the numerical test in Sect. 3 could only be performed on a small example with a reduced number of variables, another test is conducted here on all IM variables involved in the case-study. In the BN, the IM vector represents a spatially-correlated Gaussian field, for which analytical solutions have been developed (Vanmarcke 1983; Stafford

![img-9.jpeg](img-9.jpeg)

Fig. 10 Summary of the identified MLSs and location of the observations

2012): such an updating procedure is actually adopted in current systems for the generation of shake-maps (Worden et al. 2018), thus constituting the reference solution. Since this solution is only available for the ground-motion field, the IM variables are updated here using only the 7 seismic observations (i.e., no observations of the damage states of bridges). IMs are updated at the locations of the 96 bridges of interest and the centroids of the 53 built areas: the updated distributions are compared to the analytical solution for different sizes of MCMC samples (respectively three chains of $3000,5000,15000$ and 25000 samples each, with the removal of a burn-in phase of 2000 samples in each chain). The errors rates $\varepsilon_{E(I M)}$ and $\varepsilon_{\text {ologIM }}$ of the posterior distributions estimated with the BN with respect to the exact analytical solution, at all vulnerable sites, are summarized in Fig. 11:

![img-10.jpeg](img-10.jpeg)

Fig. 11 Histograms of the error rate of the mean and standard deviation of the posterior IM distribution at the various sites, with respect to the analytical solution, for various lengths of the MCMC chains

$$
\left\{\begin{array}{l}
\epsilon_{E(I M)}=\frac{E\left(I M_{\text {sampled }}\right)-E\left(I M_{\text {exact }}\right)}{E\left(I M_{\text {sagld }}\right)} \times 100 \\
\epsilon_{\sigma_{\log I M}}=\frac{\sigma_{\log I M_{\text {sampled }}}-g_{\text {logIM }_{\text {exact }}}}{\sigma_{\log I M_{\text {exact }}}} \times 100
\end{array}\right.
$$

where $E(I M)$ is the expectation of the posterior IM distribution and $\sigma_{\text {logIM }}$ is the standard deviation of the logarithm of IM.

The estimated posterior distributions of IM are globally in very good agreement with the analytical solution, both in terms of mean and standard deviation, thus providing further confidence with respect to the application of the proposed sampling-based inference algorithm. This comparison exercise serves as a preliminary step to calibrate the size of samples and ensure proper convergence of the posterior distributions. In the current application, Fig. 11 shows that satisfying accuracy levels are quickly reached as the size of samples grows. Therefore, it is decided to opt for a chain size of 15000 samples, in order to keep the error rate well below $1 \%$. With this choice, the complete BN (including also $\mathbf{C}, D S, M L S$ and $S$ nodes) is solved in less than half an hour with a medium-performance personal computer ( 8 GB memory): this timeframe is in line with what should be expected from elaborate rapid response systems, although it could be further improved with the use of dedicated computing servers.

# 5.2 Updated loss estimates 

Following the discussion of Sect. 2.4 on the assumptions to be made for the covariance models, three different correlation hypotheses are tested for the response $\mathbf{C}$ of bridges:

- Corr1: no correlation is introduced, so that $\sum_{\mathbf{C}}$ is simply a diagonal matrix.
- Corr2: only the correlation of the record-to-record variability is introduced, with a correlation model decreasing with inter-bridge distance (i.e., Eq. 6 with $\rho^{M}{ }_{i j}=0$ ).
- Corr3: in addition to the correlation of the record-to-record variability, a full correlation between bridges of the same type (i.e., using the same fragility model) is assumed, i.e. $\rho^{M}{ }_{i j}=1$ if bridges $i$ and $j$ are in the same typology.

Global results for the system connectivity are detailed in Table 2, where it is shown that the proposed approach is also able to identify which MLS is the most likely to remain accessible (i.e., "best" MLS).

A significant difference is observed between the prior and posterior probabilities of disconnection, due to the assumption that the damage states of 5 bridges were entered as evidence (see Fig. 10). The evidence of a bridge's state has an impact on the system at various levels:

- The observation of a bridge failure directly modifies the accessibility of the MLS(s) to which it belongs, and in turn system connectivity.
- If the seismic response $\mathbf{C}$ is modelled with a constrained correlation model (i.e., Corr2 or Corr3), then the observation of a bridge's state may modify the seismic response of other bridges, in turn modifying their probability of failure and ultimately the accessibility of the MLSs to which they belong.
- Finally, as seen in Fig. 7, the observation of a bridge's state may also modify the distribution of the IM at the base of the bridge, in turn modifying the ground-shaking field in the vicinity. In the BN model, the state of a bridge $i$ is dependent on both the seismic response $C_{i}$ and on the shaking level $I M_{i}$ : therefore, both parent nodes $\mathbf{C}$ and $\mathbf{I M}$ are affected by the evidence on the bridge's state.

The differences between the three correlation models are noticeable: the extreme configurations Corr1 and Corr3 should be used as upper and lower bounds of the model outcome, pending an in-depth investigation of appropriate correlation models for the seismic response. Furthermore, each assumption leads to the identification of a different MLS as the least affected route, which could have a large impact on emergency operations. An example of the changes in the rapid estimate of the post-earthquake condition of the network is provided in Fig. 12, both in terms of failure probability of bridges and

Table 2 Results of the Bayesian updating, in terms of probability of disconnection between points A and B (i.e., $S=0$ ) and of identification of the "best" MLS, for the various correlation assumptions


![img-11.jpeg](img-11.jpeg)

Fig. 12 Left: prior distribution using only the characteristics of the earthquake event; Right: posterior distribution using field observations (with Corr3 model)
identifying the most accessible MLS. Similar updating may also be performed for the damage assessment of built areas (see Fig. 13): the results are shown for Corr3 model, which only affects the seismic response $\mathbf{C}$ of bridges. However, in a BN, the model adopted for the nodes related to a type of component can impact the posterior distributions of all nodes, including those related to other types of components in the system.
![img-12.jpeg](img-12.jpeg)

Fig. 13 Left: prior mean of $\mu_{D}$ (Mean Damage Grade) of the built areas; Right: posterior distribution using field observations (with Corr3 model)

Therefore, the choice of a correlation model $\mathbf{C}$ has consequences on the distribution of IM, which in turn affects the distribution of the mean damage grade for buildings.

Apart from the changes in the mean damage and loss values, the Bayesian updating is especially useful for reducing the related uncertainties; and therefore, gaining more confidence in rapid damage assessment. In Fig. 14, the updated standard-deviations of $\log$ $P G A$, used as IM, are reduced by half (from around 0.42 in the prior distribution down to the $0.20-0.25$ range) in the immediate vicinity of seismic stations. On the other hand, the survival/failure observations on bridges have a reduced impact on the distribution of IM, since the probability updating enters here in competition with the updating of $\mathbf{C}$, which have an equal contribution in the damage sampling (see Eq. 1).

The updating process of the response $\mathbf{C}$ is further detailed in Fig. 15, where the posterior distribution of a given $C_{i}$ is used to assemble a fragility function, through the following expression:

$$
P_{f}(P G A)=\Phi\left(\frac{i m-\bar{C}_{i}}{\sigma_{C_{i}}}\right)
$$

Two opposite configurations are shown in Fig. 15:

- In the top plots, bridge \#533 is observed as intact, and its updated response distribution is therefore moving towards higher PGA levels. The response of bridge \#546, a neighbouring bridge of the same type (i.e., Type 1), is also updated, but to a lesser extent. As expected,
![img-13.jpeg](img-13.jpeg)

Fig. 14 Posterior standard-deviation $\sigma_{\log P G A}$ of the IMs at the locations of interest (with Corr3 model)

![img-14.jpeg](img-14.jpeg)

Fig. 15 Updating of the seismic response of bridges, based on damage observations
the correlation model Corr1 (no correlation at all) has no impact on the response. Since the two bridges are only about 2 km apart, the application of model Corr2 (only distancedependent correlation) has a noticeable influence on the response distribution. Model Corr3 has the most influence since it corresponds to the strongest correlation structure.

- In the bottom plots, bridge \#629 is observed as failed, and its updated response distribution is therefore moving towards lower PGA levels. Similar trends are observed for bridge \#661 of the same type (i.e., Type 2): in this case, the effect of model Corr2 is less noticeable, since the two bridges are further apart $(10 \mathrm{~km})$.

The updated seismic response may then be used as a prior distribution in subsequent risk analyses: this feature is especially useful in the earthquake aftershock phase, since the updated fragility models may be directly applied to the components that have survived, in order to refine the aftershock risk assessment.

# 6 Conclusions 

This study has investigated the implementation of a Bayesian Network-based framework for improving situational awareness during the rapid response phase following an earthquake event. It has been demonstrated that a BN built in OpenBUGS environment is able to provide updated losses for a real-world road network and built areas based on available observations. The BN is solved with a MCMC sampling scheme, which delivers approximate posterior distributions: this approximate solution, as opposed to exact inference algorithms, is a necessary trade-off in order to treat systems of hundreds of components exposed to spatially distributed hazards. Moreover, the sampling inference scheme used in OpenBUGS can combine continuous (e.g., intensity measures, seismic capacities) and discrete variables (e.g., damage states), which has the benefit of introducing exact distributions instead of discretizing continuous variables. Regarding road networks, when connectivity loss is used as a simple system indicator, the decomposition of the system into MLSs is also essential in reducing the complexity of the BN. As a result, in the studied example, posterior distributions are generated within 20 or 30 min . Moreover, the decomposition into MLSs has the benefit of identifying specific routes associated with probabilities of accessibility: this information has the potential to be used by emergency managers to set up dedicated evacuation routes or safe itineraries to hospitals. Each MLS can also be associated with a travel distance or travel duration, in order to develop more elaborate performance indicators than connectivity loss.

The input of field observations has the expected effect of refining the loss estimates, thus providing more confidence in the information delivered to emergency responders. The main mechanism behind the updating process is due to the formulation of the covariance matrices $\sum_{\mathrm{IM}}$ and $\sum_{\mathrm{C}}$ : while the correlation between intensity measures is well studied, the correlation between the seismic capacities of components is less obvious. Various correlation assumptions have been tested here, in an attempt to quantify this effect: further investigations will be required in order to propose a robust model for the covariance of the seismic response. It is shown that correlated seismic capacities also lead to updated fragility models, depending on the observed damage on components. Such a feature of the BN model would be especially useful to update the risk assessment models in the aftershock phase, for instance. Finally, the results of such a BN application can constitute the starting point of rapid repair strategies for bridges, in order to improve the seismic resilience of transportation systems.

While the present study has focused on methodological developments and on the demonstration of a simple yet realistic case-study, further work should be devoted to the verification of this framework on a real earthquake case, where collected post-earthquake data could be used to replay the sequence of events and evaluate the ability of the BN to reduce uncertainties on loss estimates. Although the theory behind the BN model has been checked (e.g., validation of the ground-motion updating part in Sect. 5.1), an application to a real earthquake case would have the merit of confronting the method to actual conditions (e.g., possibility of missing data, contradicting observations, etc.). Moreover, the BN model is solely based on a connectivity analysis: if each MLS is associated with a travel distance or duration, post-earthquake travel times may be generated. However, such a performance indicator would remain based on free-flow travel conditions (i.e., each edge of the road network is associated with a constant travel speed, whatever the traffic conditions). While the BN model in itself is not able to account for traffic flows, the approach introduced by Gehl et al. (2018) may be applied: it consists of generating off-line stochastic loss

scenarios, computing travel times with a traffic flow model (i.e., with an origin-destination matrix and user-equilibrium equations) and learning an ad-hoc BN structure from the simulation outcomes.

Supplementary Information The online version contains supplementary material available at https://doi. org/10.1007/s10518-022-01349-4.

Author contributions Conceptualization and Methodology: Pierre Gehl, Rosemary Fayjaloun; Formal analysis and investigation: Rosemary Fayjaloun, Pierre Gehl, Li Sun, Caterina Negulescu, Enrico Tubaldi, Ekin Özer; Writing - original draft preparation: Pierre Gehl; Writing - review and editing: All; Funding acquisition \& Supervision: Pierre Gehl, Enrico Tubaldi, Dina D’Ayala.

Funding This research was funded by the European Union's Horizon 2020 research and innovation program, Grant Number 821046, project TURNkey.

# Declarations 

Conflict of interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
