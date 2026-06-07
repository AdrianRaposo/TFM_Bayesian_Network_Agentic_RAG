# Multi-risk assessment in mountain regions: A review of modelling approaches for climate change adaptation 

Stefano Terzi ${ }^{\mathrm{a}, \mathrm{b}}$, Silvia Torresan ${ }^{\mathrm{a}, \mathrm{c}}$, Stefan Schneiderbauer ${ }^{\mathrm{b}}$, Andrea Critto ${ }^{\mathrm{a}, \mathrm{c}}$, Marc Zebisch ${ }^{\mathrm{b}}$, Antonio Marcomini ${ }^{\mathrm{a}, \mathrm{c}, *}$<br>${ }^{a}$ Department of Environmental Sciences, Informatics and Statistics, University Ca' Foscari Venice, Via Torino155, I-30172 Venezia-Mestre, Venice, Italy<br>${ }^{\mathrm{b}}$ Institute for Earth Observation, Eurac Research, Viale Druso 1, 39100, Bolzano, Italy<br>${ }^{c}$ Fondazione Centro-Euro Mediterraneo sui Cambiamenti Climatici (CMCC), via Augusto Imperatore 16, I-73100, Lecce, Italy

## A R T I C L E I N F O

Keywords:
Multi-risk assessment
Climate change adaptation
Bayesian network
System dynamic modelling
Agent-based model
Event trees

## A B S T R A C T

Climate change has already led to a wide range of impacts on our society, the economy and the environment.
According to future scenarios, mountain regions are highly vulnerable to climate impacts, including changes in the water cycle (e.g. rainfall extremes, melting of glaciers, river runoff), loss of biodiversity and ecosystems services, damages to local economy (drinking water supply, hydropower generation, agricultural suitability) and human safety (risks of natural hazards). This is due to their exposure to recent climate warming (e.g. temperature regime changes, thawing of permafrost) and the high degree of specialization of both natural and human systems (e.g. mountain species, valley population density, tourism-based economy). These characteristics call for the application of risk assessment methodologies able to describe the complex interactions among multiple hazards, biophysical and socio-economic systems, towards climate change adaptation.

Current approaches used to assess climate change risks often address individual risks separately and do not fulfil a comprehensive representation of cumulative effects associated to different hazards (i.e. compound events). Moreover, pioneering multi-layer single risk assessment (i.e. overlapping of single-risk assessments addressing different hazards) is still widely used, causing misleading evaluations of multi-risk processes. This raises key questions about the distinctive features of multi-risk assessments and the available tools and methods to address them.

Here we present a review of five cutting-edge modelling approaches (Bayesian networks, agent-based models, system dynamic models, event and fault trees, and hybrid models), exploring their potential applications for multi-risk assessment and climate change adaptation in mountain regions.

The comparative analysis sheds light on advantages and limitations of each approach, providing a roadmap for methodological and technical implementation of multi-risk assessment according to distinguished criteria (e.g. spatial and temporal dynamics, uncertainty management, cross-sectoral assessment, adaptation measures integration, data required and level of complexity). The results show limited applications of the selected methodologies in addressing the climate and risks challenge in mountain environments. In particular, system dynamic and hybrid models demonstrate higher potential for further applications to represent climate change effects on multi-risk processes for an effective implementation of climate adaptation strategies.

## 1. Introduction

Future scenarios of climate change show an increase of frequency and magnitude of natural hazards that will affect our society and the environment (European Environmental Agency, 2017; IPCC, 2014a, 2014b). The need to prepare and adapt to multiple climate events is internationally recognised as a fundamental step towards the
development of resilient societies (UNISDR, 2015). Assessing the dynamics of multi-risk processes and climate change requires unravelling the magnitude and frequency of different hazardous events over space and time, and exploring how these extremes interact with dynamic social and economic fabrics and processes.

Various possible combinations generating climate risk are characterised by non-linear interactions and feedback loops among three

[^0]
[^0]:    * Corresponding author. Department of Environmental Sciences, Informatics and Statistics, University Ca' Foscari Venice, Via Torino155, I-30172 Venezia-Mestre, Venice, Italy.

    E-mail address: marcom@unive.it (A. Marcomini).
    https://doi.org/10.1016/j.jenvman.2018.11.100
    Received 28 June 2018; Received in revised form 24 September 2018; Accepted 23 November 2018
    Available online 04 December 2018
    0301-4797/ (C) 2018 Published by Elsevier Ltd.

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** IPCC AR5 components leading to risk of climate related impacts (IPCC, 2014a).

crucial components: (i) climate hazards (e.g., heat waves, droughts, floods, landslides, avalanches) (ii) territorial elements exposed to risk (e.g., built-up areas, critical infrastructures, agriculture, tourism), and (iii) cross-sectoral and dynamic vulnerabilities of the exposed elements (e.g., people mobility, education levels and technology diffusion) (Gallina et al., 2016; Kappes et al., 2012; Carpignano et al., 2009). In particular, the interactions among environmental variables constitute the mechanism triggering potential cascading, synergic or antagonistic effects of different natural hazards (Gill and Malamud, 2016, 2014; Kumasaki et al., 2016; Xu et al., 2014). In addition, socio-economic activities can be exposed to multiple climate hazards or generate cascading effects on others anthropogenic processes due to their characteristics of high interdependent vulnerability (Gill and Malamud, 2017; Zio, 2016; Petit et al., 2015; Rinaldi et al., 2001).

Mountain regions represent significant vulnerable areas with specialized natural and human systems (e.g., alpine species, valley population density, tourism-based economy) exposed and susceptible to climate change (Schneiderbauer et al., 2013; United Nations, 2012). Modifications in snow precipitation and glaciers melting trigger consequences in the management of water used for hydropower production and for agricultural irrigation, calling for climate change adaptation measures to avoid future cascading impacts on different sectors (Beniston and Stoffel, 2014; Fuhrer et al., 2014; Balbi, 2012).

Currently, holistic assessments of future climate change impacts in mountain environments are still in their infant phase. Pioneering multilayer single hazard/risk analysis integrating cause-effect matrices, vulnerability indices and fragility curves have been recently used as first step toward multi-risk assessment (Forzieri et al., 2016; Kappes et al., 2012; Marzocchi et al., 2012, 2009; Delmonaco et al., 2006; Bell and Glade, 2004).

However, they show some limits in modelling the dynamic interdependencies and cascading effects among (and within) the risk components and can result in misleading assessments of potential impacts.

Therefore, there is the need to identify cutting-edge modelling approaches and tools able to: consider correlations among multiple (conjoint or cascading) hazard events; evaluate the multiple risk pathways for natural and human systems under current or future climate and anthropogenic pressures (e.g., land use changes).

Bayesian networks, agent-based models, system dynamic models, event and fault trees, and hybrid models have been recognised as suitable methodologies in addressing a wide range of complex environmental problems. These methodologies have been used in integrated environmental modelling through the combination of qualitative and quantitative information (Mallampalli et al., 2016; Hamilton et al., 2015; Kelly et al., 2013; Jakeman et al., 2006), in climate change impact studies through uncertainty analysis (Maani, 2013; UK Climate Impacts Programme, 2003) and in the critical infrastructures field through the analysis of interdependencies and cascading effects (Ouyang, 2014; Saturntira and Duenas-Osorio, 2010; Eusgeld et al., 2008).

However, previous applications of these methodologies addressing multi-risk assessments, climate and future changes for vulnerable regions are limited in number (Sperotto et al., 2017; Gallina et al., 2016; Nadim et al., 2013; Environment Agency, 2007).

This study profiles five broad categories of methodologies analysing their contributions and limitations in addressing critical aspects of multi-risk modelling within the context of climate change. We explored their applications for vulnerable environments with a focus on mountain regions distressed by climate change impacts (e.g., temperature increase, precipitation variation) and direct anthropogenic pressures (e.g., socio-economic development, population growth, land-use change).

After introducing a conceptual framework showing the complexity and challenges of multi-risk components in mountain regions (Section 2), the paper discusses the main methodological and technical features of multi-risk assessments (Section 3) and finds out benefits and limitations of five distinguished modelling approaches (Bayesian networks, agent-based models, system dynamic models, event and fault trees, and hybrid models) for climate change multi-risk assessment in mountains (Section 4). Finally, Section 5 synthesizes the main findings of the review highlighting the future challenges to represent climate change effects on multi-risk processes for an effective implementation of climate adaptation strategies.

### 2. Multi-risk and climate change in mountain regions

At an international level, the fifth Assessment Report (AR5) of the IPCC Working Group II (WGII) has defined the key components that lead to climate-risk events: hazard, exposure and vulnerability. While climate change exacerbates the development of hazards, the number of elements exposed and their degree of vulnerability are affected by socioeconomic processes (Fig. 1).

Even if the IPCC diagram provides a general conceptual basis for climate risk assessment, it does not represent the multi-faceted

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** Conceptual framework for mountain regions expanding the risk components into multi-hazard, exposure, multi-vulnerability and multi-risk.

Relationships typical of multi-risk processes (e.g. chain of impacts and feedback loops) (Zscheischler et al., 2018). As recently endorsed by the United Nations Sendai Framework (UNISDR, 2015), it is important to integrate the concepts of multi-hazard and multi-sectoral assessments to strengthen risk reduction practices. According to recent literature (Gallina et al., 2016; Kappes et al., 2012) the adoption of a multi-risk perspective requires the consideration of a specific glossary including new concepts such as multi-hazard, multi-vulnerability and multi-hazard risk. In particular, as explained in Gallina et al. (2016), it is necessary to expand the traditional risk components (hazard, exposure and vulnerability) into multi-hazard, exposure and multi-vulnerability dimensions in order to represent the complex multi-risk interactions.

Here we show the application of the multi-risk paradigm in climate change impact and adaptation assessments, with an illustrative example of a conceptual framework for mountain regions (Fig. 2). As discussed in the following sections, within the figure is possible to identify the variables to be analysed for each multi-risk component and their interactions (e.g. floods triggering erosion and landslides). However, other important features of multi-risk assessments, such as feedback loops and cross-components relations (e.g. the double effects of urbanland regulations on both the number of element exposed and the hydrological conditions linked to hazards development), are still difficult to be represented in a diagram, and require further level of analyses through innovative modelling approaches.

### 2.1. Mountain multi-hazard

Multi-hazard refers to the different interacting hazardous events that can lead to greater impact than the sum of the single hazard effects. The nature and combination of these interactions (e.g. cascade events, increase/decrease of probability and spatio-temporal coincidence) has already been analysed by different authors (Gill and Malamud, 2016, 2014; Kumasaki et al., 2016; Mignan et al., 2016; Xu et al., 2014). However, this framework focus on potential cascading effects in mountain environments, therefore shifting the attention from a multi-layer single hazard approach to a multi-risk perspective. Blue boxes outline hazard factors and biophysical processes that affect hydrogeological extreme events (e.g. landslides, floods, avalanches). Although spatio-temporal dynamics are not represented in the description of risk processes, both interactions and feedback loops show the high connectivity of multiple consecutive events, for example the landslide-flood cascade. In addition, climate change and socio-economic processes act as external drivers on the biophysical multi-hazard processes affecting both their probability of occurrence and magnitude, as also shown in the IPCC AR5 diagram.

### 2.2. Exposure and multi-vulnerability

IPCC (2014a) defined exposure as "the presence of people, livelihoods, species or ecosystems, environmental functions, services, and resources, infrastructure, or economic, social, or cultural assets in places and settings that could be adversely affected". Moreover, the IPCC also defines vulnerability as "the propensity or predisposition to be adversely affected. Vulnerability encompasses a variety of concepts and elements including sensitivity or susceptibility to harm and lack of capacity to cope and adapt".

To extend these concepts towards multi-risk assessments it is important to refer to a multi-vulnerability perspective as the ensemble of interconnected and dynamic vulnerabilities among different exposed elements (Jurgilevich et al., 2017; Connelly et al., 2015).

Mountain ecosystems, built-up areas, transport route, tourism, critical infrastructures, agriculture and health are possible exposed macro-categories represented in orange boxes, while factors of sensitivity, coping and adaptive capacity are reported in green boxes (e.g. age, technology diffusion, ecosystem specialization), in the multi-vulnerability component. Blue arrows highlight the presence of interdependencies on different exposed elements, such as the increase of tourism fluxes sustaining the creation of new built-up areas, or the connection between a transportation route and a critical infrastructure (e.g. a hospital). Dependencies are also shown within the multi-vulnerability box reporting connections involved both in the susceptibility variables (e.g. age→mobility→risk preparedness) and in the coping or

adaptive capacity (e.g. governance $\rightarrow$ regulations $\rightarrow$ subsidies $\rightarrow$ crop variety). Moreover, exposure and multi-vulnerability are strictly related. Critical infrastructures represent a clear example of these relations, providing services to other sectors (e.g. tourism and health) and having consequences on the vulnerability of other elements if affected (e.g. mountain road interruption due to a landslide can increase health vulnerability for elders). Finally, the various combinations of vulnerability factors and exposed elements in the multi-risk issues call for a join analysis of these two components integrating competences and information coming from different fields (i.e. social, economic, and environmental).

### 2.3. Multi-risk

The comprehension of the multi-risk concept is based on the multihazard and multi-vulnerability pillars (Gallina et al., 2016). In particular, the multi-hazard refers to all the possible interacting hazards that can affect the same elements exposed, while the multi-vulnerability considers dynamic and connected vulnerabilities of different elements exposed. Therefore, as depicted in Fig. 2, multi-risk stem from the multi-faceted combinations and interactions among multi-hazard, exposure and vulnerability, determining multiple "risk pathways", pictured by the shaded grey triangle in figure.

Considering the complexity of representing all the possible combinations of risk pathways, in Fig. 2 we reported few examples illustrating two possible multi-risk configurations due to: (i) dependent vulnerabilities among elements exposed for the left red boxes (i.e. a landslide damaging a critical infrastructure and affecting the access to health services), or due to (ii) the presence of multiple hazards affecting the same elements exposed, for the right boxes (e.g. a flood and a landslide hitting the same built-up areas).

Despite the inclusion of a multi-hazard perspective, Fig. 2 still demonstrates limitations in capturing the complexity of multi-risk processes both providing little information on the sequence of risk dependencies and neglecting feedback loops and interactions among risk components.

The number of components, interactions and combinations of risks make the study of climate change issues of particular complexity. Although it is internationally recognised to adopt multi-risk governance principles, it is still not clear how to assess the combination of multiple effects and integrate effective strategies.

A clear analysis of multi-risk processes calls for the application of innovative methods that are able to represent distinctive features of risk such as cross-disciplinary features, spatial and temporal dynamics and possible future scenarios of impacts.

## 3. Challenges of modelling multi-risk in mountain regions

Once we recognised the components and the complexity of multirisk processes, two main questions emerged: (i) what are the distinctive features of multi-risk processes? (ii) what are the available tools to address them?

The aim of this section is to identify and describe the methodological and technical distinctive features (i.e. criteria) characterizing a comprehensive multi-risk assessment. Seven criteria were chosen to explore the suitability of each model to address: (i) uncertainty management, (ii) feedback loops, (iii) temporal dynamics, (iv) spatial analysis, (v) cross-sectoral assessment, (vi) stakeholder engagement and (vii) adaptation strategies integration. In addition to these, (viii) data input and (ix) level of complexity provided technical information on models suitability.

### 3.1. Uncertainty management

Dealing with interactions of natural hazards with society in the context of climate change means handling frequency of occurrence and
joint probabilities of multiple impacts (Warren, 2011). Considering that various chains of events can lead to the evaluation of direct and indirect impacts propagation, the uncertainty assessment is challenging but fundamental for the comprehension of future climate impacts.

This criterion was selected to account for the uncertainty surrounding risk modelling in short and long-term: from the uncertainty of occurrence of future natural hazards where there have never been (e.g. water scarcity in mountain regions) to that of socio-economic dynamics influencing the number of exposed elements and their vulnerabilities (e.g. population concentration in flood-prone valley bottoms).

Finally, the integration of uncertainty analysis in a model offers a support for risk modellers and analysts in selecting suitable approaches and fostering informed and transparent decision processes.

### 3.2. Feedback loops

Natural hazards, socio-economic systems and climate change are characterised by non-linear interactions and feedback loops within and across them (European Environmental Agency, 2017; Dawson, 2015).

The identification of interactions distinctive of mountain environments underpins a comprehensive assessment of the causes, cascading effects and adaptation strategies of risk processes (Gallina et al., 2016; Birkmann et al., 2013).

This criterion was selected to provide information on the reinforcing and balancing characteristics of interactions within and across mountain hydrogeological processes leading to hazard phenomena (e.g. glaciers melting $\rightarrow$ smaller glaciers creation $\rightarrow$ increase of glaciers melting). Moreover, it considers socio-economic fabrics looking at potential interactions influencing the vulnerabilities of elements exposed in a risk perspective (e.g. economic subsidies to high water consuming agricultural practices triggering water issues for domestic use).

### 3.3. Temporal dynamics

One of the challenges posed by multi-risk events is the representation of their dynamics in space and time. For this reason, the concept should incorporate dynamic changes of vulnerability for different categories of exposed elements and connected among each other (Gallina et al., 2016). This concept brings about the necessity of representing evolving interactions of both socio-economic and biophysical dynamics which contribute to the development of risk processes (Fuchs et al., 2013).

This criterion addresses the methodological integration of dynamical processes to describe both slow-onset projections (e.g. permafrost melting, demographic increase) and rapid changes in the risk assessment chain (e.g. rock-fall preventive evacuation). Specific information on the simulation time length and steps adopted are provided for each application in Table 2 of the Supplementary Material.

### 3.4. Spatial analysis

Spatially explicit risk assessments can help planners and decisionmakers to estimate the risks identifying the most exposed areas (Gallina et al., 2016; Grêt-Regamey and Straub, 2006). Characterizing the overlapping hazards, the number and category of elements threatened by multiple events, and their future scenarios can foster the prioritization of adaptation strategies.

In our review, the spatial analysis refers to the integration of remotely sensed data on land use and cover at valley bottoms and on slopes, potential hazard extensions and locations of affected population and infrastructures using geographic information systems. Finally, the use of hotspots indicators provide information on the type of territorial systems exposed to overlapping hazards, connecting spatial data to social and economic fabrics potentially affected.

### 3.5. Cross-sectoral assessment

The importance of analysing future climate impacts spanning across different sectors has been introduced in Gallina et al. (2016) in order to "systematically estimate the chain from greenhouse gases emissions, climate change scenarios and cascading impacts affecting simultaneously multiple natural systems and socio-economic sectors". This criterion moves away from the perspective of independent single sectors causing misrepresentation of climate impacts and hence of possible adaptation measures (Harrison et al., 2016).

Here we consider interactions and feedbacks among mountain hydrogeological features and socio-economic characteristics (e.g. water availability-hydropower production-industrial production), exploring if the applications achieve a cross-sectoral assessment and which sectors have been considered (e.g. biophysical, social and economic).

### 3.6. Stakeholder engagement

The cross-disciplinary nature of climate-risk issues and their consequences on human-environment systems need the integration of experts and stakeholder knowledge (Döll and Romero-Lankao, 2017; van Aalst et al., 2008). Although a hazards probability assessment is usually performed through expert knowledge and quantitative modelling, a collaborative approach integrating qualitative information from the social and environmental fields can improve the understanding of risk processes and adaptation measures effectiveness (Döll and RomeroLankao, 2017; Komendantova et al., 2014). For this reason, this criterion considers the engagement of stakeholders for model design, implementation and for communication of results (Table 1). Finally, for each application specific information on the modality of stakeholder involvement is demonstrated according to the use of surveys, workshop, conferences or role games in Table 2 of the Supplementary Material.

### 3.7. Adaptation strategies integration

The final aim of climate-risk studies often involves the identification of effective adaptation strategies robust to future changes in climate and socio-economic conditions (Harrison et al., 2016). Misleading risk assessments can lead to the implementation of maladaptation practices, for example reducing the risk to one hazard can actually increase the risk to another hazard (e.g. adaptation strategy of moving houses from an area exposed to flood to an area exposed to landslide), or ignoring the effects of one hazard on the adaptation strategies again another hazard (e.g. earthquake damaging river levees that collapse during a flooding event (Grünthal et al., 2006)). Hence, multi-risk assessments should evaluate the efficiency of adaptation options and strategies through consideration of cross-sectoral interactions and cascading effects (Birkmann, 2011; Dawson, 2015).

For these reasons, this criterion is here used to explore which studies have assessed climate-risk implementing and evaluating the effectiveness of adaptation strategies both structural (e.g. flood barriers, rock protection nets) and non-structural (e.g. evacuation routes, preventive behaviours). This distinctive feature of multi-risk assessments moves the attention from an impact assessment perspective towards active strategies that can be put in place to make our communities more resilient. For each model description, different types of adaptation strategies have been analysed, highlighting the feasibility of including them into each modelling technique.

### 3.8. Data required

The choice of a modelling technique often has to consider the quantity and quality of available data. Similarly to Kelly et al. (2013) and Eusgeld et al. (2008), this criterion takes into account the various input data ranging from surveys with stakeholders providing qualitative indicators, to quantitative measurable observed parameters. For this
reason, two classes of data have been identified:

- Qualitative: considers data coming from local stakeholder and expert involvement, providing opinions and semi-quantitative values (e.g. ordinal rankings), for example, on hazards extension and vulnerability perception. This class embraces risk perceptions of local population and their evaluation on the need or the effectiveness of territorial risk reduction practices.
- Quantitative: refers to measurable data used as input for the modelling approaches. Quantitative data provides precise information of variables of interest, which can be used for simulations of hazards and vulnerable systems dynamics for risk management purposes. Among others, it included land use data, population census data, time series and future scenarios of temperature and rainfall data.


### 3.9. Level of complexity

Similarly to Mallampalli et al. (2016) and Ouyang (2014), this indicator provides concise information on the resources (i.e. quantity and quality of input data), time and ease of use needed for the application of modelling approaches. In order to cover the wide differences in complexity, we have characterised three levels: low, medium and high.

- Low complexity accounts for an intuitive graphical representation fostering the integration of stakeholder information within the model. Although this process speeds up the creation of a model and can include local knowledge and needs (e.g. from mountain communities), a low complex model shows limitations in representing spatial and temporal dynamics.
- Medium complexity encompasses the use of either spatial or temporal representation, provides accurate information on a monosectoral perspective and usually integrates quantitative data.
- High complexity includes elements of sectoral interdependency, spatial and temporal dynamics of risk. According to the aim of the analysis, different models can be combined working in synergy at macro- and micro-levels with both socio-economic and environmental information towards an integrated risk assessment.


## 4. Reviewing five modelling approaches for climate multi-risk assessments

The need to explore new approaches to model multi-risk, climate change impacts and vulnerability fostered the analysis of different methodologies (Gallina et al., 2016; Kappes et al., 2012). This review does not claim to cover all the available methodologies for multi-risk assessments, but it profiles Bayesian networks (BNs), agent-based models (ABMs), system dynamic models (SDMs), event and fault trees (EFTs) as well as hybrid models (HMs), since they have been used to address a wide range of complex environmental problems:

- in integrated environmental modelling through the combination of qualitative and quantitative information (Mallampalli et al., 2016; Hamilton et al., 2015; Kelly et al., 2013; Jakeman et al., 2006),
- in climate change impact studies through uncertainty analysis (Maani, 2013; UK Climate Impacts Programme, 2003) and
- in the critical infrastructures field through the analysis of interdependencies and cascading effects (Ouyang, 2014; Satumtira and Duenas-Osorio, 2010; Eusgeld et al., 2008).

Moreover, Sperotto et al. (2017), Gallina et al. (2016), Dawson (2015), Nadim et al. (2013) and Environment Agency (2007) recommended the application of these approaches as a feasible way in addressing complex risk assessments.

For each approach a general description is provided, followed by an overview of applications in multi-risk assessments based on the benchmarks established in the multi-risk distinctive criteria (Section 3).

Table 1 Decision matrix with five selected methodologies in the rows and nine criteria of multi-risk analysis in the columns. Qualitative information is provided for each cell and colours correspond to the degree of fulfilment of the criteria:bold = very suitable;italics = suitable but with limitations;bolditalics = not suitable.

dynamic
models
(stock \& flow) | Implementation of Monte Carlo simulations | Considering both reinforcing and balancing feedback loops | The model describes changes of stock over time | Not common, although possible if the model is integrated with GIS software | Used to describe physical, social and economic processes | Stakeholder involvement in the model design, application and results communication | The model can include adaptation strategies affecting the level of stocks | The model can be developed using qualitative information and improving the system thinking, or need large amount of quantitative data for simulating changes of stocks over time | Medium-high complexity depending on the type of data and the number of feedback loops considered for the simulation | (Durun-Escudade et al., 2017; Mehta et al., 2016; Armenia et al., 2014; Sahin and Mohamed, 2014; Hartt, 2011; Stave, 2010; Simonovic and Ahmad, 2005; Li and Simonovic, 2002)  |

Hybrid model under cross-sectoral assessment should only be bold.

Finally, the main drawbacks and advantages for the application of each modelling approach for multi-risk assessment mountain areas are discussed, providing a roadmap for future research in this field. Whereas studies on mountain risk processes were not found, the review included references to risk assessments in different environments (e.g. urban, coastal, plains) whose considerations can be extended to specific aspects of mountain risk analysis (e.g. water management consequences for lowlands). A qualitative synthesis of limitations and benefits for each methodology can be found in Table 1, while a discussion on each methodology's application according to more specific criteria is demonstrated in Table 2 of the Supplementary Material.

### 4.1. Bayesian networks

### 4.1.1. General description

Bayesian networks (BNs) are a tool explicitly dealing with probabilities of occurrence and uncertainty analysis. They represent a set of random variables and their conditional dependencies according to the definition of Directed Acyclic Graph (DAG) (Pearl, 1988). Each node in the graph is associated with a random variable, while the edges between the nodes represent probabilistic dependencies among the corresponding random variables.

### 4.1.2. Mountain applications

BN studies have been applied to perform decision-making in risk assessments for a wide range of environmental issues (Vogel et al., 2014; Uusitalo, 2007). However, BNs applications considering climate and multi-risk are still limited, especially in mountain regions. In particular, Song et al. (2012), Balbi et al. (2016) and Grêt-Regamey and Straub (2006) are reported and analysed for their specific focus on mountain risk assessments. Song et al. (2012) considered a potential interaction of two hazards (i.e. earthquake triggering multiple landslides) analysing the most influential parameters involved in landslide generation. Balbi et al. (2016) considered flood risk coupling quantitative and semi-quantitative data for the assessment of potential human impacts and effectiveness of early warning systems. Grêt-Regamey and Straub (2006) performed an avalanche risk assessment at local level in Switzerland considering potential impacts for people, buildings and transportation means.

### 4.1.3. Multi-risk criteria fulfilment

The graphical representation makes BN suitable for application in decision-support for the management of complex environmental issues through the involvement of experts and stakeholders (Aguilera et al., 2011; Cain, 2001). Although their use in describing relations and uncertainty in multi-risk perspective is not yet largely diffused, Nadim et al. (2013) presented and discussed the advantages of BN applications in addressing multi-risk issues within the European FP7 MATRIX project. Their inherent management of uncertainties make them a suitable tool for studying the occurrence of multiple events and climate change projections characterised by high degree of uncertainty (Sperotto et al., 2017).

Moreover, Liu et al. (2016), van Verseveld et al. (2015) and Song et al. (2012) represented the interactions of multiple hazards striking on the same exposed territorial systems accounting for potential cascading effects among hazards. In particular, Liu et al. (2016) and van Verseveld et al. (2015) respectively considered two independent hazards and four simultaneous hazards, while Song et al. (2012) carried out a multihazard assessment, focusing on the landslides distribution and assessing the factors influencing earthquake-induced landslides.

Despite the fact that BN are acyclic graphs, and hence cannot represent feedback loops among their nodes, it is possible to overcome this limitation introducing a time step approach. Through this particular technique, also known as "dynamic Bayesian network", feedback loops are considered as connections at a precise time step (Sperotto et al., 2017). In particular, Molina et al. (2013) implemented a time
step approach to evaluate future impacts of climate change scenarios on groundwater resource in SE Spain, assessing potential adaptation strategies in vulnerable aquifer systems. Moreover, Catenacci and Giupponi (2009) reviewed the effectiveness of BN in addressing future scenarios of climate change for adaptation policies. Although some applications explored dynamic simulations, the temporal dynamic integration still represents one of the main weaknesses of BN, bringing an increase of complexity and computation time in case of time steps management (Aguilera et al., 2011).

In addition to temporal dynamics, a multi-risk perspective can make use of spatial analysis and characterisation to support decision makers. However, BN cannot autonomously manage spatial evaluations, but it can be combined with GIS software to deal with the assessment of hydrogeological hazard extension and exposed mountain territorial elements. Within this context, Balbi et al. (2016) described the probability of direct injury for people exposed to flooding events working with a GIS polygons approach. In the same way, Grêt-Regamey and Straub (2006) assessed mountain avalanche risk in Switzerland using a GIS cell-by-cell method. Moreover, in both these publications, risk adaptation strategies (i.e. evacuation and early warning system) have been included in the models, allowing the assessment of risk reduction practices and their uncertainty.

BN can also integrate nodes representing indicators on potential elements exposed and their vulnerability from a socio-economic point of view as implemented by Balbi et al. (2016) and Liu et al. (2016). These cross-sectoral information contributed to a better description of vulnerability dynamics and a more accurate quantification of the impacts of natural hazard (Liu et al., 2016).

The flexibility to integrate experts' opinion, indicators and qualitative information with empirical data makes BN suitable for participation of stakeholders and experts in the whole model development process. However, the degree of participation of stakeholders depends on their knowledge and comprehension of the conditional probability concept (Aguilera et al., 2011; Cain, 2001).

Finally, BN can be used to communicate results to experts and assist the decision-making process considering the uncertainty associated to the results (Balbi et al., 2016).

Different studies on natural hazards have also adopted a data-driven learning approach for the creation of BNs starting from historical data and their dependencies (van Verseveld et al., 2015; Vogel et al., 2014).

Although this approach provides a quantitative identification of the relations, it also requires a high amount of input-data. In these cases the complexity can easily increase, especially if integrates a dynamic Bayesian method, where conditional probabilities have to be update at each time step.

### 4.1.4. Future challenges

BNs applications demonstrated already existing knowledge dealing with mountain environment and multi-risk assessments. The explicit management of uncertainty in this method makes it a suitable tool to study potential interactions of hazards accounting for their probability of occurrence. Applications mainly involved quantitative information, but as explained in Section 4.5, Pope and Gimblett (2015) engaged the population for a bottom-up network creation, showing their use in case of poor quantitative data and stakeholder engagement. However, integration of feedback loop, spatial and temporal dynamics represent the future challenge to be explored to enhance the effectiveness of this method for climate change adaptation.

### 4.2. Agent-based models

### 4.2.1. General description

Social interactions and dynamics towards the representation of emergent phenomena at macro level (Gilbert and Troitzsch, 2005; Janssen, 2005). Within this field, agent-based models (ABMs) are used for the description of the ensemble dynamics of a system and are

composed of three elements: the agents, the environment and time. These elements interact according to natural and social sciences rules (i.e. physical based and behavioural theories) creating an overall dynamic which is not just the aggregation of the individual entities.

### 4.2.2. Mountain applications

When dealing with complex systems in mountain regions, ABMs were applied to understand the emergent behaviour in case of climate change scenarios. In particular, Balbi et al. (2013) applied an agentbased approach to assess the socio-economic consequences at local level looking at behaviours of winter and summer tourists for different snow cover scenarios in the Alps. Moreover, Girard et al. (2015) considered a mountain environment to understand salamander population distribution and dynamics in case of temperature and water availability variation due to climate change.

### 4.2.3. Multi-risk criteria fulfilment

Due to their abilities of representing collective social dynamics, ABMs have also been applied for the study of different conditions of social and policies choices during disasters (Eid et al., 2017; Mashhadi Ali et al., 2017). These characteristics make ABMs suitable to trace behavioural features, social interactions and feedback loops among agents subjected to physical pressures from natural hazards in different spatial and social contexts (e.g. mountain regions, social and economic networks) (Sobiech, 2013).

Often a conceptual framework is developed before their implementation. This step is used for a clear definition of the dynamics and to visualize the overall model structure. For this purpose, Acosta et al. (2014) and Balbi et al. (2013) applied the unified modelling language (UML), coming from computer science techniques, but other "class diagrams" are also available (Müller et al., 2013; Grimm et al., 2006). In particular, guidelines and techniques to improve the application of ABMs were introduced by Grimm et al. (2006), Grimm et al. (2010) and Müller et al. (2013) in order to review the standard protocol, to describe agent's behaviours and define human decision-making rules.

Due to its characteristics of explicit temporal dynamic description, ABMs were applied to look at future scenarios of human-environment interactions. In particular, Mashhadi Ali et al. (2017), Haer et al. (2016) and Girard et al. (2015) integrated future scenarios of climate change representing social dynamics and interactions with the environment for risk assessment purposes. In addition to climate change scenarios, Acosta et al. (2014) and Balbi et al. (2013) also considered future economic changes as main drivers of social emergent behaviours, assessing potential consequences at local level.

Another important characteristic of ABMs is the ability to reproduce movements and changes over a space grid, importing geographic information from GIS software and working on a cell-by-cell basis (Eid et al., 2017; Acosta et al., 2014; Filatova et al., 2013; Dawson et al., 2011). The grid-based maps outputs of the simulations can also integrate vulnerability changes over time, accounting for human behaviours during flood events and providing guidance for decision making strategies as in Dawson et al. (2011) and Haer et al. (2016).

Moreover, structural and non-structural adaptation measures can also be implemented and tested within the model, evaluating their effectiveness in the whole risk assessment chain: from emergency strategies to reduce the number of exposed targets, to preventive actions for hazards extension containment and post-events impact evaluation (Balbi et al., 2013; Sobiech, 2013; Balbi and Giupponi, 2009).

One limitation of ABMs is their lack to explicitly assess uncertainty, which make them a deterministic method and can lead to the "truthmachine" misinterpretation (Balbi and Giupponi, 2009; Sobiech, 2013). However, simulations through Monte Carlo analysis remain a common approach for the management of uncertainties (Mallampalli et al., 2016; Kelly et al., 2013).

On the other side, their high potentiality for stakeholder
involvement make them suitable for identification and description of agent's behaviour rules through the use of workshops and public surveys. In particular, Becu et al. (2016) showed how the application of immersive game theory for stakeholder involvement can foster social learning on coastal risk prevention measures. Although this application focuses on coastal environment, the game approach can be extended to engage inhabitants in mountain environment, collecting risk perception information on gravitational processes, enhancing risk awareness and giving credibility to risk reduction behaviours.

However, dealing with behavioural rules also means to collect and work with a big amount of data related to agents profile characterisation and complex social and physical interactions (Acosta et al., 2014; Balbi et al., 2013). In case qualitative data are collected through stakeholder involvement, it has to be translated into a semi-quantitative or quantitative input for the ABMs simulation. For this reason, a trade-off between an extensive characterisation of environment and agents' profiles, and the complexity of the system under study needs to be considered to overcome a high level of complexity and time required for its implementation.

### 4.2.4. Future challenges

ABMs demonstrated their capabilities in addressing climate change actions involving interdisciplinary information across environmental, social and economic fields. However, mountain applications are still limited in number although their characteristics make it a promising method for risk assessment integrating micro-level interactions among agents and the environment with explicit spatio-temporal references.

### 4.3. System dynamic models

### 4.3.1. General description

System dynamic models (SDMs) include a wide group of approaches to represent non-linear behaviour of complex systems on a macro-level. Among these, the "stock-and-flow" approach introduced by Forrester in 1971 to deal with macro analysis of socio-economic processes, it is composed of quantities accumulation (i.e. stock) and quantity changes during time between stocks (i.e. flow). SDMs representation is based on the analysis of the aggregated dynamics of systems components whose systemic behaviour cannot be explained in terms of the sum of the single components (Simonovic, 2015). SDMs have been used to describe dependencies and interactions among different elements of a complex system in order to find the leverage points: parts of the system to act on in order to trigger changes on the system as a whole. By doing so, it is possible to identify the key points of a system and seek for possible measures to change its status.

### 4.3.2. Mountain applications

None of the applications here considered involve multi-risk assessments or mountain regions studies, but some of their considerations can be extended also for mountain regions applications.

### 4.3.3. Multi-risk criteria fulfilment

One of the main advantages of using SDMs models is the explicit representation of feedback loops demonstrating the reinforcing and balancing effects among the elements of a system. The use of feedbacks loops contributes to improve the comprehension of nonlinearities and complexity of the considered system (Li and Simonovic, 2002). Consequently, applications of SDMs are frequent for macro analysis of social and ecological systems, which are characterised by a high degree of complexity (Elsawali et al., 2017; Armenia et al., 2014). However, although multiple risk processes are characterised by interdependencies, feedback loops and high complexity, risk assessments for mountain environment involving SDMs need to be further explored. Deterministic representations of uncertain behaviours of a system and models validation are among the limitations that needs to be overcome through external methods, such as Monte Carlo simulations and model testing

(Barlas, 1996).

Although SDMs well grasp temporal dynamics of the system, it shows limitations in representing spatial characteristics (Simonovic and Ahmad, 2005; Ahmad and Simonovic, 2004). Improvements have been reached through the combination of SDMs with GIS software. Sahin and Mohamed (2014) and Hartt (2011) showed cases where the spatial analysis was combined with SDMs model for a spatio-temporal assessment of sea level rise and storm surge risks. Although the considered issues refer to coastal environments, the methodological process could be extended to address hazard characteristics in mountain regions and potential climate impacts on vulnerable exposed. In particular, Hartt (2011) integrated economic, social, environmental and cultural indices analysing the dependencies among different sectors exposed. In the same way, Simonovic and Ahmad (2005) integrated socio-economic information for the assessment of the major factors influencing human behaviour during flood evacuations. In this case, the acquisition of socio-economic qualitative and semi-quantitative data was performed through field surveys with the affected communities representing the characteristics of the population and their risk perception. By doing so, it was possible to translate data from the survey into input for the SDMs model and improve policy choices related to evacuation warning dissemination (Simonovic and Ahmad, 2005).

The integration of participatory approaches can strongly enhance the assessment of potential adaptation measures looking at both structural and non-structural strategies for risk adaptation (Simonovic and Ahmad, 2005; Stave, 2010). Although the translation and comparison of qualitative to quantitative information is still an open-problem for risk modellers, the participation of heterogeneous stakeholders can improve the effectiveness and credibility of adaptation strategies. Moreover, stakeholder involvement aims at promoting social learning and identifying leverage points for policy making purposes (Stave, 2010). Duran-Encalada et al. (2017) integrated several policy adaptation measures (i.e. better infrastructures for water supply, water consumption reduction and virtual water reduction) under different anthropic and climate change scenarios, extending their assessments to future patterns of water use and availability.

The use of qualitative data in the model can represent a problem for accurate simulations. In particular, whenever data is assumed by the modellers becomes difficult to find a correct way for its calibration, affecting the accuracy of the simulation's results. For this reason, SDMs is mostly applied to foster the comprehension of the elements interactions within the system improving a system-thinking approach.

The level of complexity of SDMs depends on the system under study and the representation of its spatial-temporal interactions. Higher number of connections and feedback loops can limit non-experts participation, increasing the computational time and having consequences on leverage points identification.

### 4.3.4. Future challenges

SDMs have been used to depict intertwined socio-ecological system and the impacts on natural resources, such as in water resource management under climate scenarios (Mereu et al., 2016). However, their limited use in describing the interaction of multiple events and the cascading impacts on exposed systems represents a future challenge to tackle forthcoming climate issues in vulnerable environment.

### 4.4. Event and fault trees

### 4.4.1. General description

Event and fault trees (EFTs) methodologies have found wide applications in the field of safety engineering, dealing with causes of infrastructure failures and the best ways to reduce them (Ruijters and Stoelinga, 2015; Rosqvist et al., 2013; Clifton and Ericson, 2005). Fault trees have been used to trace the events that can contribute to an accident or failure, while event trees consider the consequences due to an accident, hence the identification of mitigation strategies (Sebastiaan
et al., 2012). Similarly to BN, these logic diagram are composed of nodes connected by means of branches identifying different events scenarios. Each event is characterised by a defined probability of occurrence, making these tools useful in identifying and modelling chains of events that lead to risk processes (Dalezios, 2017).

### 4.4.2. Mountain applications

Applications in mountain environments for multi-hazard assessments purposes are presented by Lacasse et al. (2008), Marzocchi et al. (2012), Sandri et al. (2014) and Neri et al. (2008). In particular Lacasse et al. (2008) addressed the potential risk arising from a rock-slide triggering a tsunami, scrutinizing different potential early warning systems with the involvement of different stakeholders. Moreover, the characteristic of mutually exclusive logic has been mostly used in a multi-hazard perspective to evaluate chains of hazards originated from volcanic eruptions (Sandri et al., 2014; Marzocchi et al., 2012; Neri et al., 2008).

### 4.4.3. Multi-risk criteria fulfilment

In case of non-linear systems, EFTs show limitations in representing feedback loops and bi-directional relationships (Sebastiaan et al., 2012). Similarly to BN, they evaluate the probability of occurrence of events using a probability density function, providing information on the uncertainty of potential risk and considering temporal dynamics, through the "dynamic tree" method (Nadim et al., 2013). Within this context, Frieser (2004) applied a dynamic event tree to assess flood prediction and coordination of people evacuation. His application considered a probabilistic evacuation decision-making model based on minimization of the overall costs (i.e. evacuation and flood damage). Specifically, the evacuation decision-making process relied on flood level information updated on a time step basis. Few applications considered EFTs together with spatial analysis. Marzocchi et al. (2012) integrated a spatial analysis of the tephra fall hazard maps for Mount Vesuvius reporting the percentiles of the annual probability per map pixel. Similarly, Sandri et al. (2014) mapped on $1 \times 1$ and $5 \times 5 \mathrm{~km}$ grid the yearly annual probability for different hazards triggered by a volcanic explosion. Finally, Neri et al. (2008) integrated percentiles of hazard probability based on a broad segmentation of the volcano area due to the topography characteristics.

Moreover, the flexibility of EFTs to incorporate qualitative and quantitative data makes them a suitable tool for stakeholders and experts involvement. Participatory approaches can be included throughout models design and for the identification of potential mitigation strategies. In particular, Lacasse et al. (2008) and Rosqvist et al. (2013) involved stakeholders and experts through workshops, for an inclusive decision-making process on the risk perceived and the assessment of countermeasures. Rosqvist et al. (2013) introduced an economic evaluation of the losses caused by different future scenarios of flooding events, hence assessing the costs and benefits of flood protection measures.

Other examples of adaptation strategies integration can be found in Peila and Guardini (2008), where they considered different structural passive protection installations against rock falls for the assessment of the yearly fatality risk reduction on a road. Furthermore, Lacasse et al. (2008) involved scientists from different field of expertise to examine the most important factors characterizing effective early warning systems against a rockslide. In this context, EFTs showed to be an intuitive technique to set risk assessment with participatory purposes. In case of complex systems, they show limitations in grasping non-linear behaviours and an increase in data required, with difficulties for the involvement of public stakeholders and limiting the participation to experts only.

### 4.4.4. Future challenges

A possible layout for EFTs application is the bow-tie method. This approach, largely used in industry risk assessments, integrates together

EFTs for a comprehensive investigation of the upstream conditions triggering an event, and the consequences downstream (Cockshott, 2005; Ravankhah et al., 2017; Shahriar et al., 2012; Weber, 2006). Overall, applications in mountain regions showed the suitability of EFTs in assessing chains of natural hazards. However, this methodology has been mostly used to assess scenarios of hazard occurrence rather than vulnerability factors. For this reason, the inclusion of spatio-temporal dynamics to fully represent risk processes represent a future challenge for this methodology.

### 4.5. Hybrid models

### 4.5.1. General description

One of the main challenges in multi-risk assessment is the integration of information coming from different fields and with different scales into one single assessment (Poljanšek et al., 2017). Although social and environmental sectors play a fundamental role in risk approaches (i.e. categories of elements exposed and their multi-vulnerabilities), often risk assessments consider a multi-hazard risk perspective for physical and economic losses evaluation (Gallina et al., 2016; Poljanšek et al., 2017). The combination of two models (i.e. hybrid model, HM) represents one possible path towards a better comprehension and description of the multi-risk processes from different levels and sectors of analysis. The studies here analysed regard mainly biophysical and socio-ecological processes linked with water issues (i.e. floods, drought and water quality problems), looking at social and economic components for an integrated risk assessment.

### 4.5.2. Mountain applications

Also for hybrid models, specifically applications involving multi-risk assessments or mountain regions studies are very limited. For this reason, here we analyse studies that can be extended for mountain regions applications.

### 4.5.3. Multi-risk criteria fulfilment

Existing studies considered the combination of a probabilistic evaluation performed by BN with one deterministic approach, like SDMs or ABM (Bertone et al., 2016a; Phan et al., 2016; Wang et al., 2016; Pope and Gimblett, 2015; Kocabas and Dragicevic, 2013). Advantages of this "hybridization" include the capacity of dealing with a high degree of uncertainty, the use of feedback loops and the integration of quantitative and qualitative data.

Qualitative-data driven BN involving a participatory approach through stakeholder involvement allows a quick creation of a model and the inclusion of local information to better characterise people's perception on risk areas and legitimate risk reduction measures (Phan et al., 2016; Pope and Gimblett, 2015).

Moreover, Wang et al. (2016), Pope and Gimblett (2015) and Kocabas and Dragicevic (2013) performed a spatial analysis together with discrete temporal representation, looking at changes of systems variables and creating output maps. In addition to that, Pope and Gimblett (2015) also extended the analysis to future scenarios of climate change, assessing water scarcity impacts across different sectors (i.e. social, ecological and biophysical). Another example of evaluation for future conditions is carried out by Kocabas and Dragicevic (2013) considering future increase of population and land use change in urban environment. They incorporated agent's behaviour and different deci-sion-options into a land-use hybrid model combining social and environmental perspectives.

The second "hybridization" category was applied by Martin and Schlüter (2015) combining ABM and SDM. In this case, the hybrid model integrated emergent patterns of micro-level decision-making with the analysis of the feedbacks and dynamics at systemic level. In this way, they worked on the connections between environmental and socio-economic sectors looking to the emergent dynamics. Specifically, they considered the ecological problem of anthropic pressures on a
shallow lake, simulating different human behaviours in terms of emissions and time needed for the lake ecological restoration.

The evaluation of ecological dynamics and social processes allowed performing a cross-disciplinary assessment of the sewage water pollution, unpacking the complexity of the socio-ecological system. Moreover, they included a temporal assessment of the lake restoration dynamic based on a public survey in order to understand the social conditions leading to the implementation of ecosystem management measures.

### 4.5.4. Future challenges

As reported in Section 4.3 on system dynamics models, the amount of data required can be very large according to the level of details used for the representation of the system. Overall, hybrid models are highly complex due to the integration of methodologies working at aggregated or disaggregated scales that need to communicate (Martin and Schlüter, 2015; Kelly et al., 2013).

## 5. Discussion and conclusions

This review represents the starting point for risk modellers interested in exploring and selecting methods for multi-risk assessment and climate change adaptation in mountain regions. The interactions among biophysical variables in the hydrogeological processes, the consequences of anthropogenic activities, and the uncertainty associated with future climatic and socio-economic changes make the assessment of multi-risk processes particularly complex.

The high non-linearity of these processes has also been reinforced by the evaluation of the multi-risk framework developed following the IPCC AR5 risk definition. For these reasons, it is necessary to work towards an improved comprehension and representation of the multirisk characteristics. Starting from this need, we first identified nine distinctive features as the current challenges for comprehensive multirisk assessments. They were chosen to explore models suitability in representing risk analysis looking at both the methodological and technical characteristics of each modelling technique. Successively, we reviewed risk and climate change impact studies involving five modelling categories: Bayesian networks, agent-based models, system dynamic models, event and fault trees and hybrid models. For each approach, qualitative information on the fulfilment of the criteria for a full multi-risk assessment was reported as a decision matrix in Table 1. Moreover, for each application we identified information on potential applicability of the five approaches in the mountain region, shedding light on potentialities and drawbacks in addressing additional and more specific features of multi-risk assessment (Table 2 in the Supplementary Material).

In particular, Bayesian networks provide an explicit representation of the probability, dealing with uncertainty management of hazards occurrence and future land-use scenarios. Although they are limited in representing spatio-temporal references or feedback loops, they offer a reliable statistical method also in case of limited data availability that can include bottom-up qualitative information for a quick participatory creation of the model. Similarly, event and fault trees explicitly manage the probability of occurrence when working on mutually exclusive events, which is particularly useful in case of impact chains. Their extensive applications in the industrial field have supported the use in natural hazards contexts, although their limitations in representing spatial outputs and in feedback loops have affected their diffusion. If the objective of the multi-risk assessment is to focus on the collective behaviours emerging from the interactions of agents among them and with the surrounding environment, then agent-based models are a valuable tool. Applications rely on simple behavioural rules definition for the agents, which account for a high amount of information to develop agents choices scenarios.

If agent-based models work at the micro-level, system dynamic models can be used to evaluate changes over time at macro-level on the

system accounting for the interactions and feedback loops among aggregated variables. This method offers the opportunity for interdisciplinary modelling and is used to improve the general understanding of a system. The lack of a spatial analysis and of uncertainty assessment are among its main limitations that need to be explored in the future. In those cases where the analysis aims to integrate information from different disciplines a combination of modelling techniques can be more appropriate. This configuration overcomes the limitations of a single model application and support interdisciplinary research in those cases where a high amount of data is available.

Indexes and expert-based approaches were not included in the review, although they represent a large percentage of currently used approaches dealing with natural hazards and risk assessments. This choice was justified considering indexes as a synthesis of information rather than a methodology itself; hence, being applied in the analysis of models output. Moreover, this study has provided an overview of approaches commonly used to tackle interplaying biophysical and socioeconomic processes extending their use for mountain applications and going beyond mono-disciplinary expert-based models.

In summary, results showed the wide range of problems these approaches are used for, but also highlighted the limited number of models applications dealing with climate impacts in mountain environments (Balbi et al., 2016, 2013; Girard et al., 2015; Grêt-Regamey and Straub, 2006; Lacasse et al., 2008; Marzocchi et al., 2012). This gap is particularly clear for system dynamic models and hybrid models, highlighting potential room for further applications and methodological improvements. The analysis also showed the limitations of each methodology to address a thorough multi-risk assessment, especially because of the combination of information from the social and environmental fields as well as spatial and temporal dynamics. Although single approaches are still widely applied, the increase of data availability and speed of processing can foster models combination, therefore addressing the distinctive features of multi-risk assessments identified in this review. For this reason, better understanding of anthropogenic and climate change in mountain regions involve the integration of models able to grasp spatio-temporal dynamics, combination of deterministic and stochastic approaches as well as quantitative and qualitative data to tackle future climate-risk challenges.

## Acknowledgment

We would like to acknowledge Eurac Research for supporting the research activities on multi-risk assessment in mountain regions within the context of climate change.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.jenvman.2018.11.100.
