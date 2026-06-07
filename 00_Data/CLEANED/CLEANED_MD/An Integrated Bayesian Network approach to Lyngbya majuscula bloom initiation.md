# HAL open science 

## An Integrated Bayesian Network Approach to Bloom Initiation

Sandra Johnson, Fiona Fielding, Grant Hamilton, Kerrie Mengersen

## To cite this version:

Sandra Johnson, Fiona Fielding, Grant Hamilton, Kerrie Mengersen. An Integrated Bayesian Network Approach to Bloom Initiation. Marine Environmental Research, 2009, 69 (1), pp.27. 10.1016/j.marenvres.2009.07.004 . hal-00563092

## HAL Id: hal-00563092 <br> https://hal.science/hal-00563092v1

Submitted on 4 Feb 2011

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Accepted Manuscript 

An Integrated Bayesian Network Approach to Lyngbya majuscula Bloom Initiation

Sandra Johnson, Fiona Fielding, Grant Hamilton, Kerrie Mengersen


Please cite this article as: Johnson, S., Fielding, F., Hamilton, G., Mengersen, K., An Integrated Bayesian Network Approach to Lyngbya majuscula Bloom Initiation, Marine Environmental Research (2009), doi: 10.1016/ j.marenvres.2009.07.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# 1 An Integrated Bayesian Network Approach to 

## 2 Lyngbya majuscula Bloom Initiation

3

4 Sandra Johnson*, Fiona Fielding, Grant Hamilton, Kerrie Mengersen

5

6 School of Mathematical Sciences, Queensland University of Technology,
7 GPO Box 2434, Brisbane, QLD 4001, Australia

8

9 *Corresponding author: Sandra Johnson, School of Mathematical Sciences, Queensland University of Technology, GPO Box 2434, Brisbane, QLD 4001, Australia

12 Email: sandra.johnson@qut.edu.au
13 Tel: $+61(0) 731381292$, Fax: $+61(0) 731382310$

14

15 Abstract

16 Blooms of the cyanobacteria Lyngbya majuscula have occurred for decades around the world. However, with the increase in size and frequency of these blooms, coupled with the toxicity of such algae and their increased biomass, they have become substantial environmental and health issues. It is therefore imperative to develop a better understanding of the scientific and management factors impacting on Lyngbya bloom initiation. This paper suggests an Integrated Bayesian Network (IBN) approach that facilitates the merger of the research being conducted by various parties on Lyngbya.

management and scientific factors of bloom initiation. The research found that
Bayesian networks (BN) and specifically Object Oriented BNs (OOBN) and
Dynamic OOBNs facilitate an integrated approach to modelling ecological issues of concern. The merger of multiple models which explore different aspects of the problem through an IBN approach can apply to many multifaceted environmental problems.

Keywords: Bayesian network, cyanobacteria, DOOBN, dynamic, IBN, Lyngbya majuscula, object oriented, OOBN.

# 1 Introduction 

Lyngbya majuscula is a cyanobacterium (blue-green algae) occurring naturally in tropical and subtropical coastal areas worldwide (Osborne et al., 2001; Arquitt and Johnstone, 2004; Dennison et al., 1999), including Moreton Bay in Queensland, Australia. Lyngbya grows on the sediment or over the seagrass, algae or coral (Dennison and Abal, 1999; Watkinson et al., 2005) and when the conditions are favourable, the algae goes through a rapid growth phase, resulting in a substantial increase in biomass, commonly referred to as a bloom (Ahern et al., 2007; Hamilton et al., 2007c). Lyngbya blooms appear to be increasing in both frequency and extent (Dennison and Abal, 1999; Albert et al., 2005; Ahern et al., 2007), which can have major ecological (Stielow and Ballantine, 2003; Paul et al., 2005; Watkinson et al., 2005), health (Osborne et al., 2001; Osborne et al., 2007) and economic consequences (Dennison and Abal, 1999). It is therefore imperative to better

understand the scientific and management factors that drive the initiation of $L$. majuscula blooms.

Deception Bay, located in Northern Moreton Bay in Queensland, Australia, has a history of Lyngbya blooms (Watkinson et al., 2005; Ahern et al., 2007) and forms a case study for this investigation. With its proximity to Brisbane, Australia's third largest city with an estimated population in 2004 of 1.78 million (ABS, 2004), it is a popular tourist destination. The many waterways feeding from intensive and rural agricultural activities into the Bay and its use for commercial and recreational fishing, put pressure on the marine environment and compound the issues resulting from a nuisance algal bloom (Dennison and Abal, 1999).

A modelling approach was required to identify the high priority research that needed to be undertaken into the poorly known features of Lyngbya initiation. Therefore it was necessary to capture and represent all the available data and expert knowledge about the initiation of Lyngbya blooms in Deception Bay. This approach had to engage stakeholders, represent the available information at different spatial and temporal scales, identify scientific and management factors affecting Lyngbya initiation and quantify the factors and their inter-dependencies. Moreover, the stakeholders were particularly diverse comprising ecologists and scientists familiar with Lyngbya and the factors that affect its bloom, state and local government representatives, committee members of local organisations, as well as individuals with an active interest

in Lyngbya, including a third generation local fisherman with decades of accumulated knowledge of Lyngbya blooms in the Bay.

There are several modelling approaches that could be considered for such a problem, including decision trees, stochastic petri nets and Bayesian networks. A decision tree has a "top-down approach". The first factor (root node) at the top of the tree is split according to the decision taken. Each subsequent node is then split in a similar way (Janssens et al., 2006). This approach lacked the ability to represent the many interactions between the factors which would be needed to model the initiation of a Lyngbya bloom. A stochastic petri net (SPN), also known as a place/transition net is used to model concurrent systems (Angeli et al., 2007). Implementing a SPN is not trivial, even with the use of bespoke software. It mandates some statistical knowledge as well as some familiarity with stochastic process theory and Monte Carlo simulation techniques (Goss and Peccoud, 1998). A Bayesian Network (BN) provides a graphical representation of key factors, which are represented as nodes in the diagram and their causal relationships with each other and with the outcome of interest (Borsuk et al., 2006; McCann et al., 2006; Jensen and Nielsen, 2007; Uusitalo, 2007) are depicted as directed links or arrows connecting a 'parent node' to a 'child node', resulting in a directed acyclic graph (DAG) (Saddo et al., 2005; Jensen and Nielsen, 2007; Uusitalo, 2007; Park and Stenstrom, 2008). BNs are better able to portray the complexity of the decision process and the many inter-dependencies between the factors of the decision process (Janssens et al., 2006). Moreover, they are visually appealing, easy to use, comprehend and interact with. For more

97 detailed information about the advantages and disadvantages of BNs and comparisons with alternative statistical methods, we refer the reader to (Wilson et al., 2006; Uusitalo, 2007; Ahmed et al., 2009).

100
101 Bayesian networks have been used successfully to better understand and model many complex environmental problems (Bromley et al., 2005). They facilitate the representation of different management decisions and scenarios that may impact on the environmental issue being modelled and the consequences of these situations and actions (McCann et al., 2006; Uusitalo, 2007). However, the focus of many networks is often on a single aspect of the outcome, and multi-faceted inferential needs are most commonly addressed through multiple independent networks. This paper describes an approach to integrating diverse knowledge about Lyngbya bloom initiation in the Deception Bay area, by developing an Integrated Bayesian Network (IBN). The IBN comprises a series of BNs designed to conceptualize and quantify the major factors and their pathways contributing to the initiation of Lyngbya, from both scientific and management perspectives. In Figure 1 a unified modelling language (UML) use case diagram illustrates the conceptual processes of the Lyngbya IBN. To our knowledge an IBN approach has not previously been applied to Lyngbya bloom initiation.

117
$118 \quad$ (Place figure 1 here)

119

120 In Section 2 we describe the characteristics of a traditional BN, an object oriented BN (OOBN) and the natural progression to a dynamic OOBN

(DOOBN). We then introduce the integrated BN approach (IBN) which consolidates the information held in various networks and models. We present the results of this approach in Section 3 by applying it to the initiation of Lyngbya blooms.

# 2 Methods 

### 2.1 Bayesian Network (BN)

As described in Section 1, a BN visualizes knowledge about an ecological issue of interest with the important factors depicted as nodes in the network. These nodes may be at different temporal and spatial scales and the data represented in the BN may originate from diverse sources such as empirical data, expert opinion and simulation outputs (Saddo et al., 2005; Borsuk et al., 2006; McCann et al., 2006; Jensen and Nielsen, 2007; Pollino et al., 2007; Park and Stenstrom, 2008). In the case of the Lyngbya network, the outcome of interest is the initiation of a Lyngbya bloom. Each node of the network is described by a set of states (for example high/medium/low, adequate/inadequate) and quantified by associating a probability table with each node. The probability table is determined by these states and the states of the nodes that influence it. An example is the conditional probability table (CPT) for the Bottom Current Climate node, shown in Table 1, which has two states (Low and High) and has three parent nodes that influence it (Wind Direction, Wind Speed and Tide) (Saddo et al., 2005; Pollino et al., 2007; Park and Stenstrom, 2008).

Two important characteristics of a BN which also simplify probability calculations are directional separation (d-separation) and the assumption of the Markov property (Jensen and Nielsen, 2007). The criterion for $d$ separation was first proposed by (Pearl, 1988) and an alternative criterion was specified by Lauritzen et al., (1990). If nodes are d-separated then they are conditionally independent (Kjaerulff, 1995, Taroni et al., 2006). The Markov property means that the probability distribution of a variable depends only on its parents. Consequently from the multiplication law of elementary probability theory, the conditional independence (d-separation) and the Markov property enable the probability distribution of a BN with $n$ nodes $\left(X_{1}, \ldots X_{n}\right)$ to be factorized as follows:
$P\left(X_{1}, \ldots X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} / P a\left(X_{i}\right)\right)$ where $P a\left(X_{i}\right)$ is the set of parents of node $X_{i}$ This greatly simplifies calculations of the joint probability distribution and allows us to focus on each node in turn to combine the expertise and data available for that node and its parents. The BNs described in this paper were developed as part of a larger study of the major factors and their pathways contributing to the initiation of Lyngbya blooms. They were constructed in close collaboration with a Lyngbya Science Working Group (LSWG) drawn from a range of disciplines and a Lyngbya Management Working Group (LMWG) drawn from local and state government and private organisations (Abal et al., 2005).

The Science Network focused on nutrient and physical factors that were agreed by the LSWG to be the most influential contributors to the initiation of Lyngbya. To construct the Science Network, numerous meetings were convened to determine the most important factors that were believed to have an impact on the ecosystem surrounding Deception Bay. Once the initial structure was agreed upon, the factors were then clearly defined. This was necessary to ensure throughout the process all involved could refer to these definitions to agree that this was indeed the focus of that particular aspect. The initial Lyngbya Science BN was then colour coded into six logical groups of coherent nodes. The groups are Water (containing nodes Rain-present, No prev dry days, Groundwater Amount and Land Run-off Load), Sea Water (containing Tide, Turbidity and Bottom Current Climate), Air (containing nodes Wind and Wind Speed), Light (containing nodes Light Quantity, Light Quality and Light Climate), Nutrients (containing nodes Dissolved Fe Concentration, Dissolved Organics, Dissolved N Concentration, Dissolved P Concentration, Particulates (Nutrients), Sediments Nutrient Climate, Point Sources and Available Nutrient Pool), and Lyngbya Algae (containing only the target node Bloom Initiation).

Thereafter the network was quantified by populating a conditional probability table for each node, based on the factors affecting that node. For example, the probability of low or high Bottom Current Climate was determined for different states of its parent nodes, Wind Direction (north, south-east or other), Wind Speed (low or high) and Tide (spring or neap), as shown in Table 1. The CPTs were populated in this way using data obtained from expert elicitation,

output from simulation models and statistical models and data obtained from monitoring sites and government agencies. The datasets spanned different time periods ranging from one season to several years, depending on availability and applicability. Meta-data on these datasets were compiled as a key component of the project. The meta-database, comprising the source, ownership, type of data and dates collected, is summarised in a Healthy Waterways report (Fielding et al., 2007), and is available on the organisation's website.

Validation of the BN was assessed in three ways: through sensitivity analysis, outcomes comparison and scenario testing. Sensitivity analysis is a popular technique in mathematical modelling and the field of decision theory to investigate uncertainty in a model's parameters and their effect on the model output (Hamby, 1994; Coupe et al., 2000). For BNs this means studying the changes in the probabilities of the target node as a result of changes in the network's CPT values (Coupe et al., 2000). In the Science BN the probabilities of one node was varied, while keeping the others fixed, and then observing the changes in the probability of a Lyngbya bloom initiation. Sensitivity analysis is considered crucial to model validation and for targeting further research (Hamby, 1994). It is performed on the BN model to reduce uncertainty in the target node and to identify those nodes that have the largest impact on the target node (Hamby, 1994; Coupe et al., 2000). Additional research effort can then be directed to the quantification of those nodes (Bednarski et al., 2004).

# ACCEPTED MANUSCRIPT 

Outcomes comparison involves comparison between external data and model predictions. In the case of the Lyngyba Science BN, no such external data were available since all known available data had been used to populate aspects of the BN. Moreover, for any observed Lyngbya outbreak, data were not available for the complete set of nodes in the BN model. As a result, a more limited outcomes comparison was undertaken through scenario testing, in which selected scenarios reflected known conditions associated with documented initiation or lack of initiation of Lyngbya outbreaks in the last 30 years.

Scenario testing is important to investigate model behaviour for different expert defined scenarios, assessing whether the model behaves as expected in light of past experience and in accordance with current credible research (Laskey, 1995; Bednarski et al., 2004). The expert team therefore nominated scenarios of interest and evidence was entered into the BN to represent these scenarios. The relevant nodes were updated to reflect the proposed scenario and this evidence was propagated through the BN to update the probability of a Lyngbya bloom initiation under those conditions (Laskey, 1995; Bednarski et al., 2004). For example, evidence of 'best practice' was entered into the BN by setting the Point sources node to low. Further sensitivity analysis was then performed on the other nodes in the BN to observe the sensitivity of the target node to changes in node probabilities for that scenario.

The Management Network focused on management inputs that potentially influence the delivery of nutrients to the Bay and was constructed through a

series of meetings with the LMWG. The potential nutrient sources that were identified by the LMWG were split into point sources (coming from a relatively concentrated area e.g. waste water treatment plants) and diffuse sources (nutrients being contributed to the water catchment from a larger geographical area e.g. grazing land). The management model has evolved into a graphical representation of the catchment area showing the waterways and identifying the location of the sources within the catchment as well as their nutrient contributions. Participants of the LMWG identified the existing, committed and best practice management options for each source. The network was then quantified by assigning probabilities to each node to reflect the probability of low or high nutrient discharge for each source under each management option.

# 2.2 Object Oriented Bayesian Network (OOBN) 

The basic building block in an Object Oriented Bayesian Network (OOBN) is an object, which can be a physical or an abstract entity, or a relationship between two entities. Typically, an entity comprises one or more nodes in a BN that are related in a physical, functional or abstract sense. From a probabilistic point of view, the attributes (nodes and links) are encapsulated in an object and therefore d-separated from the rest of the network.

The definition of classes of objects in OOBNs enables a more generic, reusable network to be described, which can then be used in different contexts. A class is a generic network fragment and when this class is instantiated it is called an object. A class may be instantiated many times (Jensen and Nielsen, 2007). It is not uncommon for several classes to share

common substructures. These subclasses can inherit many attributes and behaviours from the parent class, which they can then modify and enhance. The parent class can be viewed as being more abstract than its subclasses with only the important details being retained, whereas subclasses define more specific attributes and behaviours. The ability to create subclasses that inherit properties from another class is a well known and very useful characteristic of object oriented modelling (Koller and Pfeffer, 1997).

Applying this object oriented approach to BN modelling, an OOBN can be instantiated within another OOBN. An instantiated OOBN is called an instance node and represents an instance of another network, which in turn could contain instance nodes. Connectivity between these OOBNs is achieved through interface nodes (input nodes and/or output nodes) (Hugin, 2007; Jensen and Nielsen, 2007). It is clear that OOBNs enable a more structured, hierarchical approach to modelling and consequently the construction of complex and dynamic models (Koller and Pfeffer, 1997; Hepler and Weir, 2008).

The groups of nodes defined in Section 2.1 for the Science Network formed the basis for the creation of OOBN sub-networks, for example the 'Dissolved Elements subnet' and 'Light subnet', respectively. Thereafter the interface nodes were identified and added to the sub-networks to facilitate the transfer of information and evidence into and out of the sub-nets. The OOBN subnetworks were then linked via the interface nodes to recreate the Lyngbya Science network. The new structure now facilitated the independent parallel

development and interrogation of the sub-networks so that they could be reintegrated into the parent network when they were deemed to be complete.

# 2.3 Dynamic Object Oriented Bayesian Network (DOOBN) 

The temporal behaviour of a network can be represented by time slices, one for each period of interest. The resulting network, consisting of several OOBN time slices, is referred to as a dynamic OOBN (DOOBN) (Kjaerulff, 1995; Weber and Jouffe, 2006). Lyngbya blooms in Moreton Bay occur more frequently during the summer months when conditions are more favourable for bloom initiation (Watkinson et al., 2005). Additional statistical modelling was conducted by Hamilton et al. (2007a) on the effects of temperature, rainfall and light on $L$.majuscula blooms and the importance of groundwater in stimulating Lyngbya blooms has been studied by (Ahern et al., 2006) and was nominated by LSWG as a key node that may exhibit temporal behaviour. It was thus considered that the DOOBN would be better able to predict the probability of Lyngbya bloom initiation. A UML use case diagram illustrating the processes involved in creating this DOOBN, is shown in figure 2.

The initial static Science BN model used annual averages for rainfall and temperature, but captured some temporal behaviour by introducing a node to represent the previous number of dry days. As directed by the LSWG the Lyngbya Science BN was extended to incorporate the temporal nature of $L$. majuscula to create a DOOBN with five time slices (one for each of the months of November to March). The DOOBN is therefore able to predict the

probability of a Lyngbya bloom initiation by incorporating specific monthly data while also taking into account the influence of the previous month.

Using Bayesian statistical modelling (Hamilton et al., 2007b) investigated the response of Lyngbya bloom initiation to temporal factors such as average minimum and maximum monthly temperature, monthly rainfall, average monthly solar exposure and average monthly clear sky (the inverse of cloud cover). One month time lags and interaction terms were also included for rain and minimum temperature. From a total of 890 models evaluated, the single term average minimum monthly temperature model (with an intercept term) had the best predictive behaviour. Rainfall at a lag of one month was the only other variable that appeared in the top five identified models.

# 2.4 Integrated Bayesian Network (IBN) 

We describe here the IBN for the probability of initiation of a Lyngbya bloom. This network comprises two primary BNs, the Management Network and the Science Network described in Section 2.1, integrated with a Water Catchment simulation model, which was concurrently developed under the Lyngbya Programme. The IBN is conceived as a series of steps, in which the Management Network informs about nutrient discharge into the Deception Bay catchment, the Catchment model simulates the movement of these nutrients to the Lyngbya site in the Bay, and the Science model then integrates this nutrient information with other factors to determine the probability of initiation of a Lyngbya bloom.

Figure 3 is a UML activity diagram detailing the processes of the IBN for Lyngbya bloom initiation. In addition to providing a rich, cohesive model of Lyngbya bloom initiation from both a science and management perspectives, an important use of the IBN was for scenario modelling. A set of exemplar scenarios that could impact on nutrient delivery to the Lyngbya site was proposed. This included: upgrading point sources from existing to best practice (e.g. eliminating potassium output from sewage treatment plants across the catchment), describing a climate event (e.g. a severe summer storm), and conditions least favourable for bloom initiation (e.g. low temperature and nutrients).

For each proposed scenario the changes in the level of nutrients or to the factors affecting the initiation of Lyngbya in the Science network were assessed. If nutrient loads were changed, the impact on nutrient concentrations across the catchment arising from a management scenario could then be simulated through the Water Catchment model by the application of filters. The E2 software package (eWater CRC, 2007) used to create the Water Catchment model contains several pre-defined filters capable of simulating various complex management actions and adjusting the catchment load output accordingly. For example filters such as percentage removal of a nutrient and nutrient trapping may be chosen. Thereafter the Science Network was updated to reflect the modified nutrient loads and other changes related to the proposed scenario. This evidence was then propagated through the network to yield the probability of initiation of a Lyngbya bloom under the specific scenario.

(Place Figure 3 here)

The networks in the IBN were developed using a variety of software modelling tools. The conceptual Management Network was visually represented using the BN package Netica® (Norsys, 2007) and then interfaced with the hydrological flow and nutrient load model created in the whole of catchment simulation software package, E2 (eWater CRC, 2007), in order to identify nutrient loads reaching the Lyngbya site. The Science Network was developed entirely in Netica® and later in Hugin® (Hugin, 2007) where the network was transformed into a DOOBN by creating time slices (Kjaerulff, 1995; Weber and Jouffe, 2006; Jensen and Nielsen, 2007). In summary, the novelty factor here is that although a static BN is unable to 'communicate' with another BN, we can transform it to an OOBN to facilitate information flow and linkage to other OOBNs of interest. Thus we can exploit the purpose for which each model was designed to build a more comprehensive model of the environmental issue of concern.

# 3 Results 

The static Science BN for initiation of Lyngbya is depicted in figure 4 with the nodes representing the factors identified by the LSWG as important in the initiation of a Lyngbya bloom.

Sensitivity analysis of this BN revealed that the seven most influential factors in the Science Network were (in decreasing order of influence): available nutrient pool (dissolved), bottom current climate, sediment nutrients, dissolved iron (Fe), dissolved phosphorous (P), light and temperature. Furthermore scenario modelling consistently identified available nutrient pool as the factor which most heavily influences the probability of initiation of a bloom. Point and diffuse sources deliver nutrients to the bay and this nutrient delivery is affected by management actions at the sources.

The Science BN was also interrogated using management and climatic scenarios and analysing the effect on the probability of bloom initiation to changes in the various factors. The predicted changes in the probability of a Lyngbya bloom initiation as a result of each of the seven most influential factors in isolation, is shown in Table 2. In a 'typical' year, as defined by the LMWG, the probability of a bloom initiation was reported as $28 \%$; this increased significantly during a severe summer storm event to $42 \%$, when light climate was optimal and rain-present was high. Bloom initiation was a predicted as a certainty (100\%) when the available nutrient pool (dissolved) was enough, temperature was high and light climate was optimal. However, when only the available nutrient pool (dissolved) was set to 'not enough', the probability of a bloom initiation dropped to $3 \%$, but jumped to $80 \%$ when it was changed to 'enough'. Although bottom current climate was a key influential factor, changing only this factor caused the probability of bloom initiation to drop to $15 \%$ when the bottom current climate was 'high' and to increase to $43 \%$ when it was 'low'. This is a variation of $28 \%$ in the probability

of a bloom initiation and although large, is clearly overshadowed by the $77 \%$ variation caused by changes in nutrient availability. Changing iron availability alone increased the probability of a bloom initiation from $21 \%$ to $37 \%$. Changing organics availability alone increased the probability of a bloom initiation from $25 \%$ to $31 \%$.
(Place Table 2 here)

Next the Science OOBN sub-network (figure 5) was created from the static Lyngbya Science BN as outlined in Section 2.2, retaining all the key factors (with the exception of the No of prev dry days) and their CPTs from the static BN. As is characteristic of Object Oriented networks, the Science OOBN subnetwork includes instances of other sub-networks, shown in figure 5 as rectangles with rounded edges, such as the Wind subnet and the Turbidity subnet. Input nodes were added to the Science OOBN sub-network as placeholders for the real nodes, Temperature, Rain- present, Land Run-off Load and Ground Water Amount. The sub-networks were based on the groups created in the static Science BN to yield standalone networks capable of linking to other networks via the interface nodes (input and output nodes), or being instantiated in other networks. Importantly, providing the interface remains intact, these OOBN sub-networks can be further expanded without affecting the structure of any other networks linking to it. As a consequence we have a powerful concept of parallel development by independent expert teams while retaining the overall cohesive model.

(Place Figure 5 here)

In collaboration with the LSWG and based on the findings of (Hamilton et al., 2007a) as described in Section 2.3, the static Lyngbya Science network was adapted in the following manner to incorporate monthly rainfall and temperature data and the lag effect of rainfall on the amount of groundwater and land run-off. First, the lag effect of rainfall on groundwater amount and land run-off was replicated by creating a Rainwater OOBN sub-network as shown in figure 6. In this OOBN, the Prev Groundwater and the Prev Land Run-off are input nodes (double edged eclipse with a broken outer line), which enable connectivity to the previous time slice's Ground Water Amount and Land Run-off nodes, respectively. The Rain - present input node enables the instances of the Rainwater OOBN to be bound to the rainfall relating to that instance, e.g. the November Rainwater OOBN instance will have November's rainfall bound to the Rain - present input node. The Ground Water Amount and Land Run-off Load output nodes (double edged eclipse with a solid outer line) make them visible to other networks and therefore allow them to be bound to input nodes in other networks.
(Place Figure 6 here)

Finally the DOOBN was created with five time slices (figure 7), one time slice for each of the summer months (December to February), one for the end of spring (November) and one for the start of autumn (March) . Every time slice has an instance of the Rainwater and Science sub-networks as well as the

temperature and rainfall nodes for that month. Data from the Bureau of Meteorology was used to quantify the DOOBN, as well as the information contained in the initial static BN.

As can be seen in figure 8, the rainfall information for a particular month is bound to the Rain present input node in the Rainwater and Science model sub-network instances for that month and the Groundwater Amount and Land Run-off output nodes from one month bind to the Prev Groundwater and Prev Land Run-off input nodes of the following month, respectively.

The point and diffuse nutrient sources contributing to the Management Network for Lyngbya initiation included: aquaculture, composting, onsite sewage, poultry, waste disposal, waste water treatment plant, agriculture, artificial development, development and clearing, extractive industries, forestry, grazing, natural vegetation and stormwater. The sources and nutrients identified by the management committee are shown in Table 3.

An extract of the Management Network, which identifies and locates point and diffuse sources of nutrients for the Mellum Creek Sub-catchment, visually represented in Netica ${ }^{\circledR}$, is shown in figure 9.

(Place Figure 9 here)

Scenario modelling predicted higher probabilities of Lyngbya bloom initiation during the summer months and confirmed the temporal nature of Lyngbya bloom initiation. Incorporating this behaviour resulted in the DOOBN for Lyngbya bloom initiation (figure 7) being developed as outlined above with one month lag effects included for groundwater amount and land run-off.

As shown in figure 10 below, the BN predicts a sharp increase in the probability of initiation of a Lyngbya bloom from the end of spring (November) to the first month of summer (December). The increased probability continued during the next two summer months, with a slight fall in autumn (March). Although these predicted probabilities for Lyngbya bloom initiation are low, the increased trend in bloom initiation is clearly visible. When evidence of summer rainfall was added to these time slices we observed a more dramatic increase. For example, the probability of a bloom initiation was predicted as $511 \quad 52 \%$ when evidence of a summer rainfall event was entered into the December time slice. This compares to $42 \%$ in the original static annual BN model.

# 4 Discussion 

518 This paper describes an Integrated Bayesian Network approach applied to the initiation of Lyngbya blooms. The aim was to present the exposition of BN

methodology to a complex ecological problem such as Lyngbya bloom initiation and illustrate how it can be used to integrate models for different aspects of the same issue. We have illustrated the process that could be followed to integrate two static BNs and another type of model (such as the E2 model of the Whole of Catchment) to achieve an integrated BN. The IBN approach described here can also be used for investigating other features of this organism, such as growth, biomass and decay, through appropriate changes to the Science Network. These networks are currently being developed. The Integrated Network approach is also conceptually suitable for investigating other outcomes of interest that are impacted by nutrient outputs and water movement in a catchment.

It is noted that it is beyond the scope of the present paper to provide an actual test of the utility of BNs for predicting cyanobacterial blooms. The paper therefore does not include a comparison of the predictions against classical multivariate techniques; a test of the BNs own output reliability, that is, whether the probabilistic estimate of the likelihood the BNs output is correct for the target data set; a clear presentation of exactly what data are being used; a sufficient amount of data to first build and refine the model on one data set and then test it on a previously unseen set of data. However the Science BN, which has been adopted by Healthy Waterways, will be validated through future data collected as part of the next phase of the Lyngbya project.

More broadly, the general approach proposed in this paper is applicable to environmental or other outcomes involving both scientific and management

considerations. Information arising from expert knowledge, data and research can be formally conceptualized and quantified through Science and Management Networks, and combined into an Integrated Network. Such an approach involves definition of the problem or outcome of interest, agreement as to significant contributing factors and their definitions and pathways which impact on this outcome, and identification and integration of information that allow quantification of these factors and impacts. The benefits of such an approach include a much greater specification of the issue at hand or research focus, buy-in from diverse stakeholders, consolidation and formalisation of information, an audit trail for decision-making and future research, and quantitative outcomes in the form of probability statements about the outcome of interest.

In the static Lyngbya BN (figure 4) similar factors were grouped together and colour coded as a visual aid. The nature of the Science BN enabled a simple conversion of the network to an OOBN (figure 6), with a sub-network for each group of factors and interface nodes providing the communication links to other OOBNs (figure 8). In the same way many complex BNs can be simplified by abstracting the network to a higher level to include sub-networks of logically grouped factors, which in turn can include other sub-networks, thereby having several levels of abstraction. An important feature of the OOBN sub-networks is that they can be developed simultaneously by the various expert groups who are responsible for them. When the sub-networks have been quantified, tested and ratified, they are integrated into the master network containing instances of those sub-networks.

The extension to a DOOBN not only improved prediction but also enhanced interpretability of the network. The inclusion of time-specific dynamics for temperature and water was more consistent with the conceptual framework of Lyngbya behaviour held by both science and management stakeholders. Moreover, it is more straightforward to include expert opinion and data of a temporal nature in this expanded model. It is suggested that for other complex ecological systems, the additional complexity of a DOOBN is more than compensated for by the increased flexibility of representation of information and acceptability of the outputs.

Finally, the creation of an IBN to combine multiple networks which describe different aspects of an outcome of interest is an effective way of providing a cohesive, quantifiable and auditable tool for better understanding and coordination of multi-faceted environmental problems.

# Acknowledgements 

Financial assistance was provided by the Environmental Protection Agency and Australian Government through the South East Queensland Healthy Waterways Partnership, the ARC Centre for Dynamic Systems and Control, and QUT Institute for Sustainable Resources. We fully acknowledge the contributions of the Lyngbya Management Working Group and the Lyngbya Science Working Group. For helpful comments on the manuscript we acknowledge Kathleen Ahern, Barry Hart and an anonymous reviewer.

# 595 

# ACCEPTED MANUSCRIPT 

618 Queensland, Australia: disparate sites, common factors Marine
619 Pollution Bulletin 51 428-437
620 Angeli D, De Leenheer P and Sontag E D 2007 A Petri net approach to the
621 study of persistence in chemical reaction networks Mathematical
622 Biosciences 210 598-618
623 Arquitt S and Johnstone R 2004 A scoping and consensus building model of a
624 toxic blue-green algae bloom System Dynamics Review 20 179-198
625 Bednarski M, Cholewa W and Frid W 2004 Identification of sensitivities in
626 Bayesian networks Engineering Applications of Artificial Intelligence 17
627 327-335
628 Borsuk M E, Reichert P, Peter A, Schager E and Burkhardt-Holm P 2006
629 Assessing the decline of brown trout (Salmo trutta) in Swiss rivers
630 using a Bayesian probability network Ecological Modelling 192 224-244
631 Bromley J, Jackson N A, Clymer O J, Giacomello A M and Jensen F V 2005
632 The use of Hugin to develop Bayesian networks as an aid to integrated
633 water resource planning Environmental Modelling \& Software 20 231-
634 242
635 Coupe V M H, van der Gaag L C and Habbema J D F 2000 Sensitivity
636 analysis: an aid for belief-network quantification The Knowledge
637 Engineering Review 15 215-232
638 Dennison W C and Abal E G 1999 Moreton Bay Study: A Scientific Basis for
639 the Healthy Waterways: South East Queensland Regional Water
640 Quality Management Strategy)
641 Dennison W C, O'Neil J M, Duffy E J, Oliver P E and Shaw G R 1999 Blooms
642 of the cyanobacterium Lyngbya majuscula in coastal waters of

643 Queensland, Australia Bulletin de l'Institut Oceanographique, Monaco
$644 \quad 19501-506$
645 eWater CRC 2007 E2 Catchment Modelling Toolkit.
646 Fielding F, Alston C, Dwyer M, Hamilton G, Johnson S, McVinish R, Peterson
647 N and Mengersen K 2007 LYNGBYA Task 2.3: Development of an Integrating Framework for the Lyngbya Research and Management
649 Program 2005-2007 Bayesian Belief Networks. (Brisbane, Australia: Healthy Waterways Partnership) pp 1-39

651 Goss P J E and Peccoud J 1998 Quantitative Modeling of Stochastic Systems
652 in Molecular Biology by Using Stochastic Petri Nets Proceedings of the
653 National Academy of Sciences of the United States of America 95
$654 \quad 6750-6755$
655 Hamby D M 1994 A Review of Techniques for Parameter Sensitivity Analysis
656 of Environmental Models Environmental Monitoring and Assessment
$657 \quad 32135-154$
658 Hamilton G, McVinish R and Mengersen K 2007a Bayesian model
659 identification and averaging for coastal algal bloom prediction.
660 Hamilton G, McVinish R and Mengersen K 2007b Bayesian model
661 identification and averaging for coastal algal bloom prediction
662 Ecological Applications in press
663 Hamilton G S, Fielding F, Chiffings A W, Hart B T, Johnstone R W and
664 Mengersen K 2007c Investigating the Use of a Bayesian Network to
665 Model the Risk of Lyngbya majuscula Bloom Initiation in Deception
666 Bay, Queensland Human and Ecological Risk Assessment 13 1271-
667 1279

668 Hepler A B and Weir B S 2008 Object-oriented Bayesian networks for
669 paternity cases with allelic dependencies Forensic Science
670 International: Genetics 2 166-175
671 Hugin 2007 Hugin.
672 Janssens D, Wets G, Brijs T, Vanhoof K, Arentze T and Timmermans H 2006 Integrating Bayesian networks and decision trees in a sequential rulebased transportation model European Journal of Operational Research175 16-34
676 Jensen F V and Nielsen T D 2007 Bayesian Networks and Decision Graphs:Springer Science + Business Media, LLC)
678 Kjaerulff U 1995 dHugin - a computational system for dynamic time-sliced
679 Bayesian networks International Journal of Forecasting 11 89-111
680 Koller D and Pfeffer A 1997 Object-Oriented Bayesian Networks. In: Thirteenth Annual Conference on Uncertainty in Artificial Intelligence (UAI-97), (Providence, Rhode Island pp 302-313
683 Laskey K B 1995 Sensitivity Analysis for Probability Assessments in Bayesian Networks IEEE Transactions on Systems, Man and Cybernetics 25901-909
686 Lauritzen S L, Dawid A P, Larsen B N and Leimer H G 1990 Independence
687 properties of directed Markov fields Networks 20 491-505
688 McCann R K, Marcot B G and Ellis R 2006 Bayesian belief networks: applications in ecology and natural resource management1 Canadian Journal of Forest Research 363053
691 Norsys 2007 Netica.

692 Osborne N J, Shaw G R and Webb P M 2007 Health effects of recreational
693 exposure to Moreton Bay, Australia waters during a Lyngbya majuscula
694 bloom Environment International 33 309-314
695 Osborne N J T, Webb P M and Shaw G R 2001 The toxins of Lyngbya
696 majuscula and their human and ecological health effects Environment
697 International 27 381-392
698 Park M-H and Stenstrom M K 2008 Classifying environmentally significant
699 urban land uses with satellite imagery Journal of Environmental
700 Management 86 181-192
701 Paul V J, Thacker R W, Banks K and Stjepko G 2005 Benthic cyanobacterial
702 bloom impacts the reefs of South (Broward County, USA) Coral Reefs
703 24 693-697
704 Pearl J 1988 Probabilistic Reasoning in Intelligent Systems (San Francisco, California: Morgan Kaufmann Publishers Inc)

706 Pollino C A, White A K and Hart B T 2007 Examination of conflicts and improved strategies for the management of an endangered Eucalypt species using Bayesian networks Ecological Modelling 201 37-59

709 Saddo A, Letcher R A, Jakemana A J and Newham L T H 2005 A Bayesian decision network approach for assessing the ecological impacts of
711 salinity management Mathematics and Computers in Simulation 69
712 162-176
713 Stielow S and Ballantine D L 2003 Benthic cyanobacterial, Micro-coleus
714 lyngbyaceus, blooms in shallow, inshore Puerto Rican seagrass
715 habitats, Caribbean Sea Harmful Algae 2 127-133

Taroni F, Aitken C, Garbolino P and Biedermann A 2006 Bayesian Networks
and Probabilistic Inference in Forensic Science: John Wiley \& Sons, Ltd)

Uusitalo L 2007 Advantages and challenges of Bayesian networks in environmental modelling Ecological Modelling 203 312-318

Watkinson A J, O'Neil J M and Dennison W C 2005 Ecophysiology of the marine cyanobacterium, Lyngbya majuscula (Oscillatoriaceae) in Moreton Bay, Australia Harmful Algae 4 697-715

Weber P and Jouffe L 2006 Complex system reliability modelling with Dynamic Object Oriented Bayesian Networks (DOOBN) Reliability Engineering \& System Safety 91 149-162

Wilson A G, Graves T L, Hamada M S and Reese C S 2006 Advances in Data
Combination, Analysis and Collection for System Reliability
Assessment Statistical Science 21 514-531

# ACOEPTED MANUSCRIPT 

732733 Legends

734 Figure 1: UML use case diagram of the conceptual processes in the Lyngbya
735 bloom initiation Integrated Network
736 Figure 2: UML use case diagram of the processes for the Lyngbya bloom
737 initiation DOOBN
738 Figure 3: UML activity diagram detailing the processes for the Lyngbya bloom
739 initiation IBN
740 Figure 4: Science Network for Lyngbya initiation (Netica®)
741 Figure 5: Rainwater OOBN sub-network showing two output nodes,
742 Groundwater Amount and Land Run-off Load, which are then connected to
743 the input nodes Prev Groundwater and Prev Land Run-off in the next time
744 slice
745 Figure 6: Science OOBN sub-network
746 Figure 7: Five time slices forming the DOOBN for Lyngbya bloom initiation
747 Figure 8: Expanded sub-network instances in Hugin®, showing the interface
748 nodes for each instance. The input and output nodes are represented here as
749 ellipses with broken and solid lines, respectively. Also evident are the directed
750 links between the sub-network instances of the same and the next time slice,
751 so that information from one time slice can flow into the next time slice.
752 Figure 9: Extract of the Management Network for Mellum Creek Sub-
753 catchment, a visual representation of the sub-catchment, showing point and
754 diffuse sources of nutrients. The inset shows the complete Management
755 Network
756 Figure 10: Probability of Lyngbya bloom initiation

758 Table 1: Conditional probability table for Bottom Current Climate node with
759 states Low and High and parent nodes Wind Direction (states North, SE and
760 Other), Wind Speed (states Low and High) and Tide (states Spring and
761 Neap). These nodes, their states, probabilities and relationships are visible in
762 the Bayesian network in figure 4
763


765
766 Table 2: Changes to the probability of Lyngbya bloom initiation for key
767 factors. All possible states for each of the nodes were assessed individually to
768 ascertain the delta effect it had on the probability of a Lyngbya bloom
769 initiation.

770


772
773
Table 3: Point and diffuse sources contributing nutrients to Deception Bay
![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

# ACCEPTED MANUSCRIPT 

* Propose scenario

Figure 4

# ACCEPTED MANUSCRIPT 

![img-2.jpeg](img-2.jpeg)

Figure 5

# ACCEPTED MANUSCRIPT 

![img-3.jpeg](img-3.jpeg)

Figure 5

# ACCEPTED MANUSCRIPT 

![img-4.jpeg](img-4.jpeg)

Figure 5

# ACCEPTED MANUSCRIPT 

![img-5.jpeg](img-5.jpeg)

Figure 6

# ACCEPTED MANUSCRIPT 

![img-6.jpeg](img-6.jpeg)

Figure 7

# ACCEPTED MANUSCRIPT 

![img-7.jpeg](img-7.jpeg)

Figure 8

# ACCEPTED MANUSCRIPT 

![img-8.jpeg](img-8.jpeg)

Figure 9

# ACCEPTED MANUSCRIPT 

![img-9.jpeg](img-9.jpeg)

Figure 9

# ACCEPTED MANUSCRIPT 

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)
$\qquad$

Figure 2

# ACCEPTED MANUSCRIPT 

![img-12.jpeg](img-12.jpeg)

Figure 3

# ACCEPTED MANUSCRIPT 

![img-13.jpeg](img-13.jpeg)