# Structure and Infrastructure Engineering 

Maintenance, Management, Life-Cycle Design and Performance

## System loss assessment of bridge networks accounting for multi-hazard interactions

Pierre Gehl \& Dina D'Ayala

To cite this article: Pierre Gehl \& Dina D'Ayala (2018): System loss assessment of bridge networks accounting for multi-hazard interactions, Structure and Infrastructure Engineering, DOI: 10.1080/15732479.2018.1434671

To link to this article: https://doi.org/10.1080/15732479.2018.1434671

View supplementary material $\square$

Published online: 13 Feb 2018.

Submit your article to this journal $\square$

View related articles $\square$

View Crossmark data $\square$

# System loss assessment of bridge networks accounting for multi-hazard interactions 

Pierre Gehl ${ }^{\text {a,b }}$ (D) and Dina D'Ayala ${ }^{a}$ (D)<br>${ }^{a}$ Department of Civil, Environmental and Geomatic Engineering, University College London, London, UK; ${ }^{\text {b }}$ Risks and Prevention Division, BRGM, Orléans, France


#### Abstract

This paper details an integrated method for the multi-hazard risk assessment of road infrastructure systems exposed to potential earthquake and flood events. A harmonisation effort is required to reconcile bridge fragility models and damage scales from different hazard types: this is achieved by the derivation of probabilistic functionality curves, which express the probability of reaching or exceeding a loss level given the seismic intensity measure. Such probabilistic tools are essential for the loss assessment of infrastructure systems, since they directly provide the functionality losses instead of the physical damage states. Multi-hazard interactions at the vulnerability level are ensured by the functionality loss curves, which result from the assembly of hazard-specific fragility curves for local damage mechanisms. At the hazard level, the potential overlap between earthquake and flood events is represented by a time window during which the effects of one hazard type on the infrastructure may still be present: the value of this temporal parameter is based on the repair duration estimates provided by the functionality loss curves. The proposed framework is implemented through Bayesian Networks, thus enabling the propagation of uncertainties and the computation of joint probabilities. The procedure is demonstrated on a bridge example and a hypothetical road network.


## ARTICLE HISTORY

Received 27 July 2017
Revised 10 October 2017
Accepted 6 November 2017

## KEYWORDS

Bayesian Networks; bridges; functional losses; fragility curves; multi-hazard interactions; road networks

## 1. Introduction

The spatial extent of most critical infrastructure systems and the disparity of their elements make them exposed to a wide range of natural hazards. This context favours the occurrence of cascading events or multi-hazard interactions, which have the potential to exceed the loading demands that are usually prescribed by design codes in the case of single-hazard risks. Such effects have led to unforeseen system failures in recent years (Paté-Cornell, 2012), thus stressing the need to address this issue when accounting for low-probability high-consequence events. Multi-hazard analyses have been the subject of significant research efforts in the past few years, as reviewed by Gallina et al. (2016). The overarching risk assessment process by Hackl, Adey, Heitzler, and IosifescuEnescu (2015) enables the risk of transportation infrastructure networks to be evaluated with respect to various natural hazards, thanks to successive steps of risk identification, risk estimation and risk review.

More specifically, Marzocchi, Garcia-Aristizabal, Gasparini, Mastellone, and Di Ruocco (2012) have proposed to treat mul-ti-hazard interactions at both the hazard and vulnerability levels: hazard events may be either simultaneous (i.e. joint occurrence of two independent source events within a given timeframe) or triggered (i.e. cascading source events), while the aggregated losses on exposed assets must be obtained from fragility functions that account for the joint loading of two or more hazard
types. This framework has been applied by Mignan, Wiemer, and Giardini (2014), who explore the impact of a combination of generic hazard types (e.g. earthquakes, volcanoes, tsunamis, technological accidents, etc.) on a virtual city. They have used a sequential Monte Carlo method for the generation of coinciding or cascading events, while accounting for time-variant vulnerability and exposure. As a result, when accounting for multi-hazard interactions, a risk migration from events to events could be demonstrated.

Alternatively, a method for the statistical treatment of mul-ti-hazard interactions for long-term analyses has been introduced by Selva (2013). By relying on the original risk integral from the Performance-Based Earthquake Engineering framework (Cornell \& Krawinkler, 2000), it allows for an analytical solution to be computed when two independent hazard types are considered. The persistence time window, defined by Selva (2013) as the time interval during which the effects of a given hazard type are still present on the exposed element, is a key concept, as its value directly influences the probability of two independent hazard events having a joint effect on the exposed element.

Whatever the multi-hazard framework considered, the development of harmonised fragility models that are able to account for multiple hazard loadings and potential cumulative damages is a key element of multi-hazard risk assessment. For instance, the fragility function developed by Lee and Rosowsky (2006)

considers the combined effect of snow and earthquake loadings on woodframe buildings. Other notable examples include the vulnerability models by Zuccaro, Cacace, Spence, and Baxter (2008) for cumulated damages during volcanic eruptions, and the multi-hazard fragility analysis by Kafali (2008) for offshore platforms subjected to both wind and wave loadings. Regarding road bridges, recent research studies have focused on the seismic fragility analysis of structural systems that present an altered dynamic behaviour due to the effect of previous scour damage (Alipour, Shafei, \& Shinozuka, 2012; Dong, Frangopol, \& Saydam, 2013; Prasad \& Banerjee, 2013).

However, the aforementioned studies are mostly focused on groups of single independent assets (e.g. residential buildings), while their application to infrastructure systems raises additional issues. Firstly, the functionality state of an infrastructure element (i.e. whether the element is still able to perform its function within the system) is an essential variable when assessing the performance of a system, as noted by Modaressi, Desramaut, and Gehl (2014). Functionality states provide more information for the subsequent estimation of indirect losses than physical damage states, which are mostly linked to direct repair costs: therefore, in a multi-hazard context, the challenge resides in the harmonisation of functionality losses for an infrastructure element that is exposed to a wide range of failure mechanisms (Gehl \& D'Ayala, 2016). Secondly, an infrastructure system consists of an organised set of interdependent elements, which prevents the direct computation of a global distribution of losses, as it may be done for residential areas (Corbane, Hancilar, Ehrlich, \& De Groeve, 2017). On the contrary, a probabilistic sampling of loss scenarios is a common approach for infrastructure risk assessment (Cavalieri, Franchin, Gehl, \& Khazai, 2012), while the inclusion of multi-hazard interactions and potential cascading effects adds significant complexity to the procedure. Finally, it remains unclear how to specify the persistence time window (Selva, 2013) when considering the potential overlap of independent hazard events.

Therefore, the present paper aims to alleviate these shortcomings by proposing an integrated approach that is applicable to a single infrastructure element or to an infrastructure system:

- At the level of the single infrastructure element: the structural system is decomposed into its components in order to identify hazard-specific local damage mechanisms that can be associated with functionality losses. Hazardharmonised probabilistic functionality loss curves can then be derived for the infrastructure element.
- At the level of the spatially distributed infrastructure system: the multi-hazard loss distribution of the considered infrastructure is estimated, while making use of the mul-ti-hazard functionality loss curves in order to directly integrate multi-interactions. To this end, the repair duration of the element, given by the functionality loss curves, is considered as a proxy for the persistence time window.

At both levels, Bayesians Networks (BNs) are used as system reliability tools, as demonstrated by Gehl and D'Ayala (2016). The exact inference that is provided by the Bayesian framework enables the exploration of extreme and potentially catastrophic events, which may be overlooked by more classical sampling
techniques (e.g. Monte Carlo simulations). However, as shown by Cavalieri, Franchin, Gehl, and D'Ayala (2017), the computational complexity of current BN formulations and their inability to model elaborate system performance indicators prevent their application to large and complex systems, thus often requiring Monte-Carlo simulations as a complementary approach. While the study by Gehl and D'Ayala (2016) details the construction of a BN for the derivation of multi-hazard fragility functions, functionality losses are only introduced in a qualitative manner through the probability of occurrence of predefined system failure modes. On the other hand, the present work aims at focusing on the quantification of functionality losses, in order to generate probabilistic loss models that are directly applicable to a network analysis.

The present study is devoted to the risk analysis of road networks, while bridges are assumed to be the only vulnerable elements, for demonstration purposes. However, the proposed method is designed to be applicable to other types of infrastructure elements (i.e. more details in Gehl, 2017) or other systems, such as utility networks. The considered hazard events are earthquakes and floods, since they are able to affect large spatial areas and they are identified as some of the most common external causes for bridge failure (Deng, Wang, \& Yu, 2015). These independent hazard types provide also an opportunity to use previous research efforts that have studied the combination of earthquakeand flood-induced loads on bridges (Alipour et al., 2012; Dong et al., 2013).

It should also be noted that the environment deterioration of bridges constitutes a common cause of disruption and performance loss, whether due to natural ageing (Zanini, Pellegrino, Morbin, \& Modena, 2013) or to cumulated degradation from repeated events (Kumar \& Gardoni, 2014). Nonetheless, since the present study is mostly devoted to the occurrence of low-probability high-consequence events, the aforementioned deteriorating phenomena are not explicitly accounted for, although the proposed method may be applied to such effects as well. Section 2 of the paper presents the methodological framework, from the identification of hazard-specific damage mechanisms to the computation of multi-hazard losses at the system level. The method is then applied to an example bridge structure in Section 3, where the abilities of the BN to derive probabilistic functionality loss curves are demonstrated. Finally, Section 4 is devoted to the use of the previously derived probabilistic functionality loss curves at the level of a road network, where a BN formulation is also proposed in order to deal with multi-hazard interactions.

## 2. Proposed multi-hazard framework

In the context of infrastructure risk assessment, the derivation of fragility curves for physical elements such as bridges constitutes a key step of the analysis process, since it leads to the quantification of damage maps for a given earthquake scenario. Most of the fragility curves that are found in the literature (Tsionis \& Fardis, 2014) are based on global damage scales, which are specified by the successive damage states of the bridge's structural components. While such damage scales are suitable indicators of the severity of the damage, they are not necessarily consistent in terms of induced losses (e.g. functionality losses, repair durations, etc.). Nevertheless, in the case of network systems, it

has been shown that assessing the system performance in terms of functionality loss (e.g. disruption of traffic, additional travel time, etc.) provides essential information in terms of accessibility to affected areas or emergency centres (Modaressi et al., 2014). On the other hand, the direct repair costs associated with the physical damage of infrastructure, which are not negligible even in the case of light damage (Zanini, Faleschini, \& Pellegrino, 2016), are more easily quantified when the specific failure modes of the elements are known.

To this end, some studies propose a mapping structure between the physical damage states and the functional losses induced to bridges. For instance, restoration curves have been introduced by the HAZUS framework (FEMA, 2003) or the REDARS methodology (Werner et al., 2006); however, such models are deterministic and do not provide clear justifications on how these loss curves have been assembled. In view of the current difficulties to reconcile damage events from different hazard types, a methodological framework for the multi-hazard risk assessment of infrastructure systems is developed, with the specific aim of harmonising the fragility models for various hazard types.

At the bridge level, the proposed approach starts from the observation that the specific effects of various hazard loadings have to be assessed at the local level, in order to ensure that all failure modes are accounted for. The different component damage states can then be reconciled by considering their effects on the bridge functionality instead of using solely the definition of the physical damage states. As a result, the proposed approach unfolds as follows (see Figure 1):

- The infrastructure system (e.g. road network) is decomposed into its physical elements (e.g. bridges), which are in turn decomposed into structural components (e.g. piers,
bearings, etc.). This choice is motivated by the need to treat the road infrastructure as a system (i.e. the network) of sub-systems (i.e. the physical elements), as opposed to conventional frameworks that consider the vulnerability of physical elements on a more global scale. The present work is focused on bridges, however, a similar approach is applicable to other elements such as tunnels or embankments (D'Ayala et al., 2015).
- For each component, the failure modes that are specific to each type of hazard loading are identified, based on the analysis of post-disaster reports or existing damage scales. As discussed in Gehl and D'Ayala (2016), the various types of structural components and hazard loadings may lead to a wide range of damage mechanisms, which all have to be accounted for in the context of a multi-hazard risk analysis.
- Specific loss metrics (e.g. repair duration, functional loss, etc.) are associated for each component failure mode in order to quantify the consequences in terms of functionality. The novelty of this step lies in the identification of the functional losses induced by specific component failure modes, which has the effect of greatly refining the loss assessment and harmonising the potential contribution from each hazard loading.
- In parallel, hazard-specific fragility curves are derived at the component level in order to quantify the probability of occurrence of each component failure mode.
- Using the component-level functionality models and fragility curves, probabilistic loss curves are then derived at the bridge system level. BNs are used here as a modular and computationally efficient probabilistic tool, with respect to the matrix-based system reliability approach (i.e. modelling of the dependencies between the variables
![img-0.jpeg](img-0.jpeg)

Figure 1. Summary of the proposed framework.

and updating of the probabilities of failure). Thanks to the BNs, probabilities of functionality loss exceedance are assembled from the probabilities given by the hazard-specific component fragility curves, while accounting for the statistical dependence between the damage events.

- Finally, the probabilistic functionality loss curves can be used to compute the probabilistic distributions of losses at the level of the road network, in a multi-hazard context. Conventional methods such as Monte Carlo sampling may be used to obtain an estimate of the loss distribution; however, the use of Bayesian Networks as an alternative to simulation-based methods is also investigated.

The proposed method may also account for deterioration mechanisms such as natural ageing using increment functions (Gardoni \& Rosowsky, 2011), which gradually modify the fragility parameters of the bridges. The network risk analysis could then be performed over a given period corresponding to the projected lifetime duration of the bridges, using the time-dependent probabilistic framework by Zanini, Faleschini, and Pellegrino (2017).

Table 1. Inventory of possible failure modes for the bridge components considered.


## 3. Derivation of probabilistic functionality loss curves

As argued in the previous section, the derivation of probabilistic functionality loss curves is a fundamental and critical step of the proposed methodology. The relevant steps are detailed in the following sub-section and the approach is demonstrated on a multi-span simply supported concrete (MSSSC) bridge, which has been described by Nielson (2005) as one of the typical bridges in the Central and Southern U.S. The main damage mechanisms considered here are the ones related to earthquake and flood events.

### 3.1. Component failure modes and functional consequences

When reinforced concrete highway bridges are considered, the most common structural components are piers (single or mul-ti-column), bearings (fixed or expansion devices) and abutments (Nielson, 2005): deck spans are usually expected to remain in the linear elastic range, which is a common assumption due to their high rigidity and the nature of their connections (i.e. especially in the case of multi-span simply supported decks, where deck unseating may occur due to extensive deformation of the bearings and relative displacement of the deck spans).

A literature review of qualitative damage scales allows to compile an inventory of the types of damage states or failure modes that are likely to affect each component as reported in Table 1, mainly based on the studies by Cardone (2014), FEMA (2003), Nielson (2005) and Tsionis and Fardis (2014). A more detailed breakdown of all possible component failure modes can be found in Gehl (2017). Elastomeric bearings with steel dowels are considered, whose type of damage depends on the magnitude of the deformation. In the case of piers, both flexural and shear behaviours may occur; while abutments can experience passive or active behaviours, depending on whether the backfill soil or just the piles are acted upon.

The field describing the damage 'severity' represents the global damage state (i.e. at the level of the bridge system) that is usually considered to be reached when the given component is damaged through the mentioned failure mode. This classification directly results from the analysis of the qualitative damage scales that have been defined for bridges in the literature (e.g. FEMA, 2003). Therefore, one may question the consistency of this classification in terms of functional consequences, for instance due to the presence of component damage states that may induce disproportionate losses.

It is proposed to represent the functional consequences as two distinct metrics: (i) the repair duration and (ii) the loss of functionality in terms of lane closure or speed restriction. The first measure is useful to conduct time-dependent scenarios with various restoration strategies and to estimate the duration during which the network system is likely to be disturbed and to measure time to recovery. The second one is essential to assess the reduced capacity of the bridges, which can be used to run a traffic model on the degraded network system. In order to efficiently quantify these loss metrics, it is necessary to consider the physical damage states at the component level, since it has been shown that each component type is subjected to very specific

failure mechanisms. Therefore, each of the component failure modes summarised in Table 1 has to be associated with these loss metrics.

The correspondence between component damages or failures and induced functional losses has been the subject of modest prior research work. For instance, Lehman, Moehle, Mahin, Calderone, and Henry (2004) have conducted experimental tests to monitor the evolution of residual cracking, cover spalling and core crushing of bridge circular columns. These damage states can then be directly linked to the functionality of the bridge (i.e. full service, open for emergency vehicle and closure). More recently, Mackie and Stojadinovic (2006) have also investigated the post-earthquake functionality of highway overpass bridges: they use the load capacity of bridges as an engineering demand parameter to derive probabilistic distributions of loss measures such as the relative repair cost, the volume of traffic or the full bridge collapse. However, these studies focus on the damage to bridge piers, while the state of other bridge components and the likelihood of witnessing joint damage events are not taken into account.

Therefore, a survey has been conducted soliciting responses from infrastructure managers and experts involved in of the INFRARISK research project consortium (O'Brien \& the INFRARISK Consortium, 2013-2016), in order to provide estimates for the functionality losses induced by diverse component damage events summarised in Table 2. This first approximation should be refined with a more extended and rigorous survey or with additional data from post-disaster field observations; however, the present values are proposed in order to carry out the demonstration of the method.

The recent research by Karamlou and Bocchini (2017) constitutes one of the most up-to-date and detailed works on the restoration of damaged bridges, therefore it is used here to specify what type of repair operations is required for each component damage event. Moreover, Karamlou and Bocchini (2017) provide a distribution of expected durations for each of the elementary tasks that comprise the suggested repair operations. These elementary repair durations (e.g. pouring foundation concrete, installing temporary column support, etc.) are described via

Table 2. Proposed functionality losses and repair operations for the component failure modes identified.


simple uniform or triangular probabilistic distributions and they are aggregated in order to obtain the probabilistic distribution of the total duration of each repair operation. It is assumed that one repair team is available for a given bridge: this simply corresponds to the summation of the repair tasks' durations, while propagating the uncertainties given by the distributions. The resulting repair duration distributions for the considered component damage events are displayed in Figure 2 as histograms, for 10 predefined discrete duration intervals.

### 3.2. Hazard-specific component fragility curves

The next step consists in determining the probability of occurrence of each of the component failure modes, expressed in terms of fragility curves that provide the probability of reaching or exceeding a discrete damage state given a hazard loading intensity. The limit states adopted for this specific bridge, and the derived fragility parameters for each component failure mode, are detailed in Supplementary Material A.

### 3.2.1. Fragility curves for seismic loading

In the case of seismic loading, fragility curves are derived through non-linear time-history analyses (NLTHA) of a finite-element bridge model: the MSSSC girder bridge model described by Nielson (2005) is used as a case-study, since the model specifications are well detailed and this general typology corresponds to bridge types that are commonly found along European highways as well (Cardone, 2014). The studied structure is composed of three independent deck spans supported by three-column piers, while elastomeric bearings with steel dowels ensure the connections between the pier caps and the decks (see Figure 3). Alternating sets of fixed (grey circles) and expansion (white circles) bearings are present along the bridge span. All the structural and mechanical parameters used here are taken from the MSSSC model (Nielson, 2005).

Ten vulnerable components are identified, i.e. two piers (P1 and P2), two abutments (A1 and A2) and six bearings (B1 to B6). The bridge has been modelled in the OpenSees finite-element code (McKenna, Fenves, \& Scott, 2000), where preliminary pushover analyses are conducted in order to identify the limit states that correspond to the failure modes from Table 1. The OpenSees fibre-based model is used for the RC piers (i.e. Concrete01 model for the concrete material and Steel01 for the steel reinforcement), while springs are used to represent the stiffness models of the bearings and abutments.

Following the assumptions from Nielson (2005), all bearings are considered to be fixed along the transversal direction. The active behaviour of the abutment in tension only activates the RC piles, while the backfill soil contributes also to the passive behaviour in compression. Under transversal loading, only the piles are solicited, which corresponds to an active behaviour in both compression and tension. The original model by Nielson (2005) is augmented with an explicit modelling of the pier foundations, through equivalent pile sections (Yin \& Konagai, 2001) and Winkler springs representing the $p-y$ curves (Prasad \& Banerjee, 2013) of the soil's lateral pressure. These foundation springs are then progressively removed in order to represent the excavated depth due to flood-induced scour. The explicit modelling of the pier foundations allows for the impact of scour

![img-1.jpeg](img-1.jpeg)

Figure 2. Proposed repair duration models for the component failure modes identified. The 10 duration intervals are defined in days, as follows: [0;15] - [15;30] - [30;45] - [45;60] - [60;75] - [75;90] - [90;120] - [120;180] - [180;240] - [240;300].
![img-2.jpeg](img-2.jpeg)

Figure 3. Bridge layout in longitudinal (left) and in transversal (right) directions.
depth to be considered when computing the seismic response of the bridge system, thus introducing cumulative damage effects.

Fragility curves for all components and failure modes are derived by successively applying a set of ground motions along longitudinal and transversal directions. The generation of the ground-motion suite follows the magnitude-distance criteria that are prescribed by Nielson (2005), in order to be consistent with the seismotectonic context of the area where the bridge has been modelled, i.e. Mw between 5.5 and 7.5 and epicentral distance between 10 and 100 km : these criteria, however, cover a wide enough range so that the resulting fragility curves can be applied to other locations. Synthetic records are generated using a stochastic procedure developed by Pousse, Bonilla, Cotton, and Margerin (2006), which is based on the definition of a magnitude, an epicentral distance and an EC8 soil class, in order to obtain
a complete set of ground-motion records. A total of 288 ground motions, spanning EC8 classes A to D, are thus generated and applied along each loading direction.

The maximum transient response of each component is then recorded for each ground motion in order to obtain the distribution of engineering demand parameters (EDPs) against the intensity measure (IM), which is chosen to be the Peak Ground Acceleration (PGA) here. It is proposed to derive the fragility curves through a Generalised Linear Model (GLM) regression with a probit link function, as detailed in Rossetto et al. (2016). The fragility function can then be defined as:

$$
P(D S \geq d s \mid I M)=\Phi\left(\frac{\log I M-\log \alpha}{\beta}\right)
$$

where $\Phi$ is the normal cumulative distribution function, and $\alpha$ and $\beta$ are the fragility parameters (i.e. mean and standard deviation, respectively), which are obtained from the GLM regression.

Even though the GLM derivation approach is especially indicated for the derivation of empirical fragility curves (Ioannou, Rossetto, \& Grant, 2012), it has also been applied to analytical results in previous studies (Baker, 2015; Nassirpour \& D'Ayala, 2017): the main reason for this is that the maximum likelihood model only requires a clear dichotomy between 'damage' and 'no damage' regardless of the actual EDP values. Therefore, it can be applied to cases where the numerical model fails to accurately determine the response numerically after the damage has occurred (e.g. derivation of collapse fragility curves).

Three sets of component fragility curves for seismic loading are derived in order to account for different scour conditions, which are meant to represent the damage history of the bridge due to potential past events (i.e. cumulated damage between flood and earthquake events). Discrete intervals of scour depths (i.e. scour damage states $\mathrm{DS}_{\text {scour }}$ ) are selected based on the influence of the scour on the dynamic response of the bridge, following the rationale developed by Gehl and D'Ayala (2016):

- $\mathrm{DS}_{\text {scour }}=$ D0: negligible scour depth ( $<1.0 \mathrm{~m}$ ), with no noticeable effects on the response of the bridge piers;
- $\mathrm{DS}_{\text {scour }}=$ D1: minor scour depth (between 1.0 and 3.6 m ), with stiffness degradation of the piers;
- $\mathrm{DS}_{\text {scour }}=$ D2: significant scour depth ( $>3.6 \mathrm{~m}$ ), with severe stiffness and strength degradation of the piers.

The component fragility curves provide a first indication on which components are the most vulnerable (i.e. the ones with the largest conditional probabilities of reaching damage) and, therefore, the most likely to contribute to the functional losses. For instance, the component failure modes that are the most likely to occur at lower intensity levels are the minor cracking of abutment piles (i.e. active behaviour) and the deformation of bearings at the end spans. On the other hand, piers and bearings at the middle span appear to be less vulnerable in this specific bridge configuration.

### 3.2.2. Fragility curves for other hazard loadings

While the previous sub-section has led to the derivation of analytical fragility curves in the case of seismic loading, empirical or literature-based fragility models are proposed for other hazard types. For instance, the impact of riverine floods on the bridge foundations is represented by so-called scour fragility curves, which quantify the probability of reaching or exceeding a scour depth given the flow discharge of the water stream. They are derived here using the empirical scour equation from the HEC18 guidelines (Richardson \& Davis, 1995). The fragility curve for deck unseating due to floods is computed with the empirical equation proposed by Kameshwar and Padgett (2014), from data gathered from damaged bridges during hurricane Katrina. Finally, fragility curves related to the subsidence of the approach slab are directly taken from Argyroudis and Kaynia (2014). More details on the assumptions and methods for the derivation of the aforementioned fragility curves can be found in Gehl (2017).

### 3.3. Bayesian Network for the derivation of harmonised loss models

A BN formulation to assess the reliability of a system has been introduced by Gehl and D'Ayala (2016), who show that it represents an efficient alternative to more conventional reliability methods such as the matrix-based one (Kang, Song, \& Gardoni, 2008). A BN consists of a directed acyclic graph, where the nodes represent various uncertain variables and the links represent logical or dependency links between the variables. The states of the variables are given by marginal distributions in the case of root nodes (i.e. variables with no incoming edges) or by conditional probability tables (CPTs) when a variable is dependent on the state of its parent variables. A CPT is a table that provides the probability of finding the variable in a given state, given the state(s) of its parent(s).

In Gehl and D'Ayala (2016), the BN has the ability to quantify the probability of occurrence of a system event (i.e. intersection or union of various component damage events) given a hazard loading, while accounting for the statistical dependence between component damage events and using the component fragility curves to populate the CPTs. In the present study, the BN is slightly altered in order to relate the component damage events to their corresponding repair duration and functionality loss models. These two loss metrics are then aggregated at the bridge system level, so that an estimation of the resulting losses for the whole bridge can be obtained (see Figure 4).

The BN comprises the following nodes, for a bridge with $n$ structural components (see Figure 4):.

- A root node IM representing the seismic intensity applied to the $n$ components.
- A root node $\mathbf{U}$ representing the standard normal variable $U$ that is common to all components.
- Root nodes $\mathbf{V}_{\mathbf{1}} \ldots \mathbf{V} \boldsymbol{n}$ representing the standard normal variables $V_{i}$ that are specific to each component.
- Nodes $\mathbf{C}_{\mathbf{1}} \ldots \mathbf{C}_{\mathbf{n}}$ representing the component damage events: the CPT is built by combining the parent nodes $\mathbf{U}$ and $\mathbf{V}_{\mathbf{i}}$ and generated by the parent nodes IM, $\mathbf{U}$ and $\mathbf{V}_{\mathbf{i}}$.
- Nodes $\mathbf{D u}_{\mathbf{1}} \ldots \mathbf{D u}_{\mathbf{n}}$ and $\mathbf{F l}_{\mathbf{1}} \ldots \mathbf{F l}_{\mathbf{n}}$ representing the repair duration and functional loss events, respectively; the CPT is generated by following the duration and loss models that are detailed in Figure 2 and Table 2.
- Nodes $\mathbf{I}_{\mathbf{1}} \ldots \mathbf{I}_{\mathbf{k}}$ representing intermediate events: these nodes are used to build a chain structure, which is more robust than a naïve formulation (i.e. a converging structure where the unique child node has a large number of parent nodes), in terms of CPT size and computation loads (Bensi, Der Kiureghian, \& Straub, 2013). The assumed rule is that the functional losses are built up by keeping the maximum loss value when each component is added to the chain (i.e. only the most severe loss, corresponding to the weakest link, is considered). Repair durations, on the contrary, are added up, assuming that a single repair team is working sequentially on the various damaged components.
- Nodes $\mathbf{S}_{1}$ and $\mathbf{S}_{2}$ representing the final loss events for the two metrics, which take into account the contributions from all components: the CPT structure is the same as the one from the intermediate nodes.

![img-3.jpeg](img-3.jpeg)

Figure 4. BN formulation for the quantification of functional consequences, for a bridge system with six structural components.

- A node SYS representing the joint occurrence of the different values of repair duration and functional loss. This final node is essential for the computation of joint probabilities when the Bayesian analysis is performed.

For common source loadings such as earthquakes, the statistical dependence between the component damage events is addressed by the introduction of Dunnett–Sobel class of variables (Dunnett & Sobel, 1955), as proposed by Kang et al. (2008), which ensure the independence between component events given these random variables. As a result, the standardised safety factor $$Z_i$$ of each component $$I$$ (i.e. the ratio between the seismic capacity and demand), representing the corresponding damage event, is decomposed into standard normal variable $$U$$ and $$V_i$$:

$$Z_i = \sqrt{1 - r_i^2} \cdot V_i + r_i \cdot U \tag{2}$$

The coefficient $$r_i$$ which represents the strength of statistical dependency, is chosen so that it approximates the correlation factors $$\rho_{ij}$$ between the safety factors $$Z_i$$ and $$Z_j$$ of components $$i$$ and $$j$$:

$$\rho_{ij} \approx r_i \cdot r_j \quad \forall i, j \in [1, n]|i \neq j \tag{3}$$

The correlation matrix between the different damage events is assembled from the component responses for each time-history simulation. Figure 5 displays the evolution of the correlation matrix for the three scour states of the bridge, showing that the statistical dependence between some component damage events tends to decrease as scour is more pronounced (i.e. mostly bearings and piers). Such an effect is explained by the softening of the foundations' stiffness with scour, which allows some components to move more freely from each other (e.g. bearings). Consequently, it is expected that in-series system events of component damage events will have an increased probability of occurrence when scour is present, due to the lower correlation coefficients (i.e. the system gets closer to statistical independence, which constitutes the upper bound of the probability of occurrence of at least one event).

This BN structure is then implemented in the Bayes Net toolbox (Murphy, 2007), where exact inference can be performed through a junction-tree algorithm. Exact inference requires the definition of Bayesian nodes with discrete states, so that continuous variables such as $$U$$, $$V_i$$, $$Du_i$$ or $$Fl_i$$ have to be converted into discrete intervals beforehand. Once the CPTs have been built, a forward analysis may be performed by setting a given intensity measure (IM) and observing the updated distribution of repair durations and functional losses at the final node SYS. For successive values of IM, probabilistic functionality curves can then be derived point by point, as it shown in Figure 6.

As expected, these probabilistic functionality curves reveal that the loss severity increases with the seismic intensities. Minor losses (e.g. short repair times or slight traffic disruption) appear to be induced by really low intensity levels, which is mostly due to the abutment piles reaching damage very quickly. It should also be noted that the composition of various fragility curves does not necessarily lead to cumulative lognormal distributions for the functionality curves, especially for the repair duration curves: this is explained by the fact that, for each component, the corresponding fragility curve (i.e. lognormal cumulative distribution) is convoluted with the repair duration distributions from Figure 2. This observation prevents the use of simple statistical parameters to represent these curves, which have then to be expressed as tabulated values (see Supplementary Material B).

Finally, the curves in Figure 6 provide the marginal distributions for each loss metric taken separately, while the application of restoration strategies for a road network would require the joint knowledge of both the functional state and repair time of the exposed elements. The BN has been formulated in such a way that the repair duration node (i.e. node $$S_i$$ in Figure 4) and

![img-4.jpeg](img-4.jpeg)

Figure 5. Correlation matrix of the component responses under seismic loading. The axes represent the codes of the components as defined in Table 1, for longitudinal (X) and transversal (Y) loading directions. The value of the correlation factors is given by the colour map.

![img-5.jpeg](img-5.jpeg)

Figure 6. Probabilistic functionality curves for repair duration (left) and functional loss (right), for the three selected scour states.
the functional loss node (i.e. node $\mathbf{S}_{\mathbf{2}}$ ) belong to the same clique during the generation of the junction-tree. Therefore, it becomes possible to quantify the joint probability of occurrence of the two loss metrics, as shown in Figure 7.

This result is fundamental for the evaluation of the performance of the global road network, since such a loss representation enables the sampling of various consistent loss scenarios (e.g. for PGA $=3 \mathrm{~m} / \mathrm{s}^{2}$, probability of .012 of experiencing $20 \%$
![img-6.jpeg](img-6.jpeg)
speed reduction for 30 days, probability of .143 of experiencing $50 \%$ lane closure for 180 days, etc.). There is some degree of correlation between the two loss metrics (i.e. the more severe the loss, the longer the repair time), even though some component failure modes may lead to complete closure while requiring reasonable restoration times: therefore, this aspect is able to be fully captured by the representation of the joint distribution of both metrics, which is easily accessed through Bayesian analysis.
![img-7.jpeg](img-7.jpeg)

Figure 7. Joint distribution of the repair time and functional loss for different seismic intensity levels.

## 4. Application to the multi-hazard risk analysis of a bridge network

This section is devoted to the application of the probabilistic functionality loss curves to the multi-hazard risk analysis of a road network, in order to demonstrate their merits over conventional fragility curves. The functionality loss curves, which have been derived in the previous section thanks to a detailed analysis of a bridge's failure modes, are directly implemented as probabilistic tools for a network analysis. The performance of a hypothetical network of bridges, subjected to earthquake and flood hazards, is assessed, while accounting for potential multi-hazard interactions.

### 4.1. Description of the proof-of-concept application

A hypothetical road network is adopted for the present application, in order to present a simple yet exhaustive case-study for which all modelling assumptions and data are known, thus allowing to focus on the demonstration of the method. The proposed network is freely inspired from the Königsberg bridge problem (Harary, 1994), with seven bridges connecting four points of interest (see Figure 8). Only bridges are assumed to be vulnerable: they are potentially exposed to both earthquake and flood hazards, so that the previously derived probabilistic functionality loss curves are assigned to all bridges (i.e. assumption that all bridges are identical, with the same waterway channel, in order to apply the same scour damage fragility models).

The proposed activity parameters for the homogenous seismogenetic area (yellow rectangle in Figure 8) are detailed in Table 3: this area represent the location from which earthquake epicentres may be uniformly sampled, while the corresponding earthquake magnitude is sampled following a truncated Gutenberg-Richter distribution. The generation of spatially distributed PGA maps at each bridge location, for each sample
seismic source, is achieved with the ground-motion prediction equation (GMPE) by Akkar and Bommer (2010). The spatial correlation between the intra-event error terms of the PGA values given by the GMPE is taken into account (i.e. a correlation matrix between the error terms at various sites is assembled from their respective distances), following the method by Weatherill, Esposito, Iervolino, Franchin, and Cavalieri (2014) for the seismic risk assessment of spatially distributed systems.

Regarding the flood hazard, three events, representative of different return periods are assumed, as detailed in Table 4. In practice, recorded time-series of rainfall events may be used to determine the return period of given events (Ferrer, 1993), while the rational method (Temez, 1991) is usually applied in order to quantify the flow discharge at a given waterway section based on the amount of water precipitation: however, such computations are out of the scope of the present demonstration.

Finally, it is assumed that the network performance is quantified through a connectivity loss index SCL, which measures a binary connectivity $\delta$ (i.e. 1 if connected, 0 if not) between a group of origins (TAZs B and C) and destinations (TAZs A and D). Therefore, the SCL index may be expressed as follows (Poljansek, Bono, \& Gutierrez, 2012):

$$
\begin{aligned}
\text { SCL }= & 1-\frac{1}{n} \cdot \sum_{i=1}^{n} \frac{N_{i}^{i}}{N_{0}^{i}} \\
& =1-\frac{1}{2} \cdot\left[\frac{\delta_{B \times i x}+\delta_{C \times i \lambda}}{2}+\frac{\delta_{B \times i y}+\delta_{C \times i \theta}}{2}\right]
\end{aligned}
$$

where $n$ represents the total number of destination TAZs, and $N_{i}^{i}$ and $N_{0}^{i}$ the number of or origin TAZs connected to the destination TAZ $i$, respectively, after and before the damaging event.

Due to the choice of such a performance indicator, the binary connectivity measure only checks whether each bridge is closed or not. Therefore, only the probabilistic functionality loss curve related to complete bridge closure is used in the subsequent analysis (i.e. dashed curve in Figure 6 right).
![img-8.jpeg](img-8.jpeg)

Figure 8. Layout of the hypothetical bridge network linking four Traffic Analysis Zones (TAZs).

Table 3. Source activity parameters for seismic hazard, to be used in the truncated Gutenberg-Richter relation in order to sample seismic event.


Table 4. Assumed flow discharge levels corresponding to three hypothetical rainfall events.


### 4.2. Multi-hazard risk analysis using a Bayesian Network

The considered hazards in the hypothetical example are independent, yet they may interact at the exposure or vulnerability level if they have a concomitant occurrence within a given time interval. Therefore, this hazard configuration is very relevant with respect to the long-term multi-hazard risk assessment framework introduced by Selva (2013), who points out that the persistence time window (i.e. the time interval during which the effect of hazard A are still influencing the effects of hazard B) has a major influence on the strength of the multi-hazard interactions. Therefore, while Selva (2013) does not provide any indication on how to specify the persistence time window, it is proposed here to make use of the repair duration model, which serves as a proxy for this time interval. More specifically, the interaction between earthquake and flood hazards is treated as follows:

- The flood hazard has the potential to damage the bridge through scour at the pier foundations or to completely destroy the bridge through deck unseating;
- If the bridge is damaged by scour, the corresponding repair duration is sampled from the proposed scour repair model (i.e. Figure 2);
- The effect of potential seismic loading on the bridge is assessed, depending on the preliminary state of the bridge (i.e. intact bridge or scour-impacted bridge, with or without repairs);
- The system performance of the infrastructure is assessed by checking the connectivity of the network, given the functionality states of the bridges.

Such a framework may be carried out by Monte Carlo-based simulations, where various scenarios are generated through the sampling of the successive variables at each step of the analysis (Cavalieri et al., 2012). Alternatively, the presence of many variables that are dependent on each other makes them straightforward to model within a BN, as originally proposed by Bensi, Der Kiureghian, \& Straub (2011). If a BN is solved with an exact inference algorithm, it has the ability to provide accurate probabilities for extreme events, which correspond here to the concomitant occurrence of independent hazards. Moreover, a BN enables some variables to be set (i.e. evidence) in order to observe the updated posterior distribution of the variables of
interest. The BN in Figure 9 is based on the original formulation by Bensi, Der Kiureghian, and Straub (2011), with the presence of additional variables to model multi-hazard interactions. The Bayesian nodes are defined as follows, while more details are provided in Gehl (2017):

- M: magnitude range of the possible earthquake events (i.e. Table 3);
- Epi: discretised locations of the epicentre of the earthquake events;
- $\mathbf{R}_{\mathrm{f}}$ : epicentral distance from the infrastructure elements;
- $\mathbf{Q}_{\mathrm{f}}$ : median PGA values at the sites of interest, without any uncertainty terms;
- $\mathbf{U}$ and $\mathbf{V}_{\mathrm{f}}$ : nodes containing the standard normal distribution in order to represent the spatial correlation of the seismic hazard at vulnerable sites;
- $\mathbf{e}_{\mathrm{f}}$ : intra-event uncertainty term, specific to each element, due to the spatial correlation assumption;
- n: inter-event uncertainty term, common to all elements;
- $\mathbf{S}_{\mathrm{f}}$ : final PGA values at the vulnerable sites, including intraand inter-event uncertainties;
- FL: intensity of the flood events (i.e. Table 4);
- $\mathbf{T}_{\mathrm{f}}$ : repair duration of flood damages (i.e. Figure 2);
- $\mathbf{C F}_{\mathrm{i}}$ : remaining flood damages, considering the associated repair duration;
- $\mathbf{C}_{\mathrm{i}}$ : functionality states of the bridges, accounting for both earthquake and flood hazards (i.e. Figure 7);
- $\mathbf{N}_{\mathrm{a}} \mathbf{A}$ and $\mathbf{N}_{\mathrm{e}} \mathbf{D}$ : number of origin TAZs that are connected to TAZs A and D;
- SCL: distribution of the connectivity loss index.

The adopted BN uses a naïve formulation, i.e. a converging structure from the component nodes to the system nodes. This formulation is made possible by the presence of a reduced number of components: seven components with binary states result in a CPT with $2^{7} \times 3=384$ elements, which is easily manageable by the junction-tree algorithm. Therefore, other strategies for the reduction of the computational complexity of the BN, such as the decomposition of the connectivity paths in minimum link sets (Bensi et al., 2013), are not required in the present case. However, for a large number of components (e.g. more than a few dozens), the BN will eventually produce unsurmountable computational issues due to the combinatorial explosion. Thus, the application of the present BN to a small hypothetical example is especially useful to visualise and understand the dependencies between the variables at play: as it will be demonstrated in Section 4.3, Monte Carlo sampling of the variables represented in the BN is a viable alternative for the derivation of loss distributions.

The BN is then implemented in the BayesNet toolbox and the distribution of the system performance loss is observed at the Bayesian node SCL, which is the variable of interest here. Different evidence configurations enable various hazard configurations to be accessed:

- No earthquake event (evidence on node M): computation of single flood hazard;
- No flood event (evidence on node FL): computation of single seismic hazard;

![img-9.jpeg](img-9.jpeg)

Figure 9. BN formulation for the multi-risk assessment of the road network.

- Both earthquake and flood events (no evidence on any nodes): multi-hazard computation, accounting for interactions.

It should be noted that the proposed BN only considers seismic events following floods: the reverse order would require
![img-10.jpeg](img-10.jpeg)

Figure 10. Probabilistic loss curves for the studied example.
additional developments (e.g. other types of damage-dependent fragility curves), although it appears that the scour estimation equations are not necessarily influenced by the amount of seismic damage previously sustained.

The yearly cumulative loss probabilities are represented in Figure 10, where the differences between the risk profiles of earthquake and flood hazards are highlighted. The global multi-hazard curve corresponds roughly to the sum of both single-hazard risk curves, although it is slightly higher due to the modelling of multi-hazard interactions. The proposed risk bias measure, which is based on the metric introduced by Selva (2013), quantifies this effect through the following expression:

$$
\text { Bias }=\frac{R^{(E Q, E L)}-(R^{(E Q)}+R^{(F L)})}{R^{(E Q)}+R^{(F L)}}
$$

For the proposed hypothetical application, the multi-hazard bias, which corresponds to the underestimation of losses when multi-hazard interactions are not accounted for, ranges between .1 and $2.0 \%$. As expected, the bias increases for low-probability events, since such events correspond to extreme cases whose occurrence is mainly due to the joint contribution of earthquake and flood loadings. It is also worth noting that the bias

measure has a greater increase rate when the single earthquakeand flood-induced losses have comparable probabilities of occurrence.

### 4.3. Towards resilience indicators

A valuable application of the proposed functionality loss curves consists in the estimation of the restoration process of the road network, following for instance an earthquake event, as it has been demonstrated by Lam and Adey (2016). This feature is applied to the same hypothetical example, for which a given earthquake scenario is selected (i.e. $\mathrm{M}_{\mathrm{w}} 6.0$ earthquake in the centre of the seismogenic area), with two distinctive scour configurations (i.e. no scour damage on any bridge vs. scour damage D2 on all bridges). For the given earthquake event, 5,000 Monte Carlo simulations are generated, due to various sampling operations occurring along the analysis chain:

- Sampling of the GMPE error terms to generate the ground-motion field;
- Sampling of the functional losses and repair durations from the loss models developed in Section 3.3.

The restoration of the road network is then measured step by step (i.e. time increments of 15 days), by assuming that only one repair crew is available for the whole network. The adopted repair order consists in prioritising the bridges with the heaviest functional losses, and then the ones with the shortest repair duration in case of ties: this hierarchy has proven to be the most efficient when compared to other restoration strategies.

Due to the temporal aspect of the restoration phase, the BN formulation detailed in the previous sub-section is not applicable in its present form; therefore, a Monte Carlo framework is performed here in order to generate a wide range of temporal loss curves (see Figure 11, in which the 50th and 95th percentiles of the Monte Carlo samples are displayed). Moreover, the use of Monte Carlo sampling instead of a BN framework allows more elaborate system performance indicators to be computed, with respect to the aforementioned connectivity loss index. For instance, a temporal performance indicator $Q(t)$ is used in order
to represent the extended travel time due the functional losses of the bridges. It is defined as follows:

$$
Q(t)=\frac{1}{\frac{1}{n} \cdot \sum_{i=1}^{n} \frac{T T_{i}(t)}{T T_{c t}}}
$$

where $T T_{i, 0}$ and $T T_{i}(t)$ are the travel times of each of the $n$ inter-TAZs journeys, before the earthquake event and at time $t$ following the event, respectively. The simulations do not currently include any traffic congestion models; however, time penalties are applied to paths that cross damaged bridges (i.e. free-flow speed reduction of 20 or $50 \%$ depending on the level of functionality loss).

Coupling the proposed functionality loss models with restoration scenarios, as presented in Figure 11, constitutes a first step towards the quantification of the resilience of the studied infrastructure system (Bruneau et al., 2003). The time-dependent losses reveal the significant differences that are found when considering the possibly degraded states of the bridges (i.e. scour damage). The functional losses and repair durations have been sampled from the functionality models in Figure 6 (i.e. 'marginal distribution' of losses) and Figure 7 (i.e. 'joint distribution' of losses), respectively. The more refined and more realistic loss model from Figure 7, which accounts for the correlation between functional losses and repair durations, leads to a more severe impact of the earthquake event. This observation demonstrates the benefit of the proposed approach, which is based on the decomposition of the bridge system into component failure modes and on the combination of functionality losses, while accounting for the statistical dependence between component damage events.

## 5. Conclusions

This paper has presented a multi-hazard risk assessment procedure from the specific angle of infrastructure systems, which induces additional issues and modelling constraints. The decomposition of infrastructure elements (e.g. bridges) into their structural components highlights the occurrence of hazard-specific local damage mechanisms, which can be directly associated with functionality
![img-11.jpeg](img-11.jpeg)

Figure 11. Restoration curves of the road network, for a $\mathrm{M}_{\mathrm{w}} 6.0$ earthquake event occurring in the centre of the seismogenic area, without (left) or with (right) previous scour damage.

loss metrics. This necessary change of scale between component and system levels proves to be instrumental in the refinement of the loss models, which can then be used to feed subsequent network analysis models. The various loss metrics that have been estimated (i.e. repair duration, functional loss in terms of speed reduction and lane closure) are key variables for the resilience assessment of road networks in both dimensions (i.e. magnitude and duration of the perturbation), provided that relevant traffic models and restoration strategies are applied. The proposed approach offers also a probabilistic framework that is compatible with the computation of risk levels for stress tests (Adey et al., 2016).

BNs have been used to assemble component fragility curves and to aggregate functionality metrics at the bridge level, for various combinations of hazard loadings. A forward analysis via the Bayesian junction-tree algorithm enables the statistical dependence between component events to be accounted for, while predicting the joint occurrence of given loss events, which are described by both their magnitude and their duration. In the proposed example, the repair duration variable has been divided into 10 discrete intervals; however, other discretisation schemes are applicable depending on the specific values of interest.

This BN approach allows for a great level of modularity, since the automated procedure that has been developed for the construction of the BN accounts for many variables: number of bridge components, number of damage states, number of discrete states for continuous variables, rules for the aggregation of functionality measures, etc. At this stage, the active involvement of infrastructure managers or bridge operators appears necessary in order to better understand the repair procedures and to clarify these issues. Further structural analyses may also be helpful to quantify the impact of multiple component failures on the load carrying capacity of the bridge.

At the level of the road network, the functionality loss curves may be directly used to compute various system performance indicators (e.g. connectivity loss, increased travel time, etc.), thus effectively replacing conventional fragility curves and facilitating the resilience quantification of the infrastructure system. These functionality loss curves are able to account for multi-hazard interactions at the vulnerability level, since they are derived for different levels of pre-existing scour, while the proposed BN formulation handles the potential interactions between earthquake and source at the hazard level. The overlapping between these two independent hazard types is ensured by a variable representing the persistence time window, which is expressed here as a probability distribution, thanks to the repair duration estimates.

However, the application of BNs to road network systems creates many conceptual and computational challenges: the discretisation process of continuous variables tends to introduce additional sources of bias or uncertainties, while the combinatorial explosion due to the sampling of multiple components' damage states remains an unresolved issue.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

This study has been carried out within the INFRARISK project (Novel indicators for identifying critical INFRAstructure at RISK from Natural

Hazards), which has received funding from the European Union's Seventh Framework Programme for research, technological development and demonstration [grant agreement number 603960].

## ORCID

Pierre Gehl http://orcid.org/0000-0002-1225-9621
Dina D'Ayala http://orcid.org/0000-0003-3864-2052
