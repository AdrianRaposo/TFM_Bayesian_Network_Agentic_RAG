To cite this article: Giné-Garriga, R., Requejo, D., Molina, J.L. and Pérez-Foguet, A. 2018. A novel planning approach for the water, sanitation and hygiene ( WaSH ) sector: the use of objectoriented Bayesian networks. Environmental Modelling \& Software, 103, 1-15
To link to this article: https://doi.org/10.1016/j.envsoft.2018.01.021
To download this article (free access until April 13, 2018):
https://authors.elsevier.com/a/1Wc7X4sKhE9lmA

# A NOVEL PLANNING APPROACH FOR THE WATER, SANITATION AND HYGIENE (WaSH) SECTOR: THE USE OF OBJECT-ORIENTED BAYESIAN NETWORKS 

R. Giné-Garriga ${ }^{* 1}$, D. Requejo ${ }^{* 2}$, J.L. Molina ${ }^{* * 3}$, A. Pérez-Foguet ${ }^{* 4}$<br>* Engineering Sciences and Global Development (ESc\&GD), Universitat Politècnica de Catalunya $\cdot$ BarcelonaTech (UPC), C. Jordi Girona, 1-3, 08034 Barcelona, Spain<br>** Salamanca University. High Polytechnic School of Engineering, Area of Hydraulic Engineering. Av. de los Hornos Caleros, 50, 05003, Ávila, Spain

Email ${ }^{1}$ : ricard.gine@upc.edu
Email ${ }^{2}$ : david.requejo@upc.edu
Email ${ }^{3}$ : jlmolina@usal.es
Email ${ }^{4}$ :agusti.perez@upc.edu

Corresponding Author: Ricard Giné-Garriga
Address: Universitat Politècnica de Catalunya - Barcelona School of Civil Engineering
CAMPUS NORD - Edif. C2
C. JORDI GIRONA, 1-3

08034 BARCELONA
SPAIN

#### Abstract

Conventional approaches to design and plan water, sanitation, and hygiene ( WaSH ) interventions are not suitable for capturing the increasing complexity of the context in which these services are delivered. Multidimensional tools are needed to unravel the links between access to basic services and the socio-economic drivers of poverty. This paper applies an object-oriented Bayesian network to reflect the main issues that determine access to WaSH services. A national Program in Kenya has been analyzed as initial case study. The main findings suggest that the proposed approach is able to accommodate local conditions and to represent an accurate reflection of the complexities of WaSH issues, incorporating the uncertainty intrinsic to service delivery processes. Results indicate those areas in which policy makers should prioritize efforts and resources. Similarly, the study shows the effects of sector interventions, as well as the foreseen impact of various scenarios related to the national Program.


# Keywords 

Water, sanitation, and hygiene (WaSH); WaSH poverty index; object oriented Bayesian Network; Planning; Kenya

# 1 INTRODUCTION 

Safe drinking water, adequate sanitation, and hygiene ( WaSH ) are pillars of human health and well-being. In consequence, the 2030 Agenda for Sustainable Development, adopted in September 2015, has water and sanitation at its core (United Nations General Assembly, 2015). The Sustainable Development Goal dedicated to water (SDG 6) will represent a huge challenge for many countries, and it will be the driving force to shape ambitious policies on which to base the development of sector strategies and national Programs. It will be essential to promote efficient and sound decision making when designing interventions for accelerating progress towards universal access to these basic services. Appropriate tools will thus be needed to plan service delivery, to measure performance, and to influence resource allocation (Cohen and Sullivan, 2010; Giné Garriga et al., 2015).
To date, there have been numerous approaches to provide a coherent strategic planning framework. In particular, efforts have been directed at addressing specific problems that range from improving the availability of reliable information, to improving access to information through data analysis, interpretation, and dissemination, and to encouraging the use of this information in decision-making processes (Giné Garriga, 2015). For instance, various methods are in place to collect WaSH primary data (Giné Garriga et al., 2013; United Nations Children's Fund, 2006; WaterAid and ODI, 2005). Furthermore, the sector has witnessed the development of a variety of conceptual frameworks to monitor service delivery, albeit from different perspectives (Cohen and Sullivan, 2010; Flores Baquero et al., 2013; Giné Garriga and Pérez Foguet, 2013a; Luh et al., 2013; Sullivan et al., 2003). Significant attempts have also been made to provide decision-makers with reliable information to support planning, targeting, and prioritization, particularly in decentralized contexts (Ghosh and Rao, 1994; Giné Garriga et al., 2015).

Despite the likely use of previous approaches to inform planning and decision-making processes, these suffer from a number of common weaknesses. First, indicators and aggregated indices tend to induce a somewhat narrow, issue-centered perspective on the service provision, which is not conducive to a good understanding of the complex cause and effect relations within WaSH variables. For instance, the direct link between "distance to the water source (access to water) - water consumption (use of water) - handwashing behavior (personal hygiene)" is rarely captured through an indicator-based approach. There is thus a need to adopt a conceptual model that allows indicators to be relevant for multiple causal chains and to incorporate the existing human behavior - service provision - environment interactions. Second, an adequate approach for targeting and prioritization would be to consider the proportion $p$ of households verifying a given variable (e.g., access to improved sanitation) with its respective confidence interval (Giné Garriga et al., 2015). In composite indices, however, priority ranks and league

tables are typically based on a measure of central tendency, which is rarely contrasted with the dispersion or variability of the population distribution (Giné Garriga and Pérez Foguet, 2013a; Sullivan et al., 2003; United Nations Development Programme, 2015). This jeopardizes an adequate identification of the neediest and most vulnerable populations (Flores Baquero et al., 2016; Giné Garriga et al., 2015). Third, representing a range of scenarios and assessing their potential impact may be a desirable feature of any planning tool (Bromley et al., 2005; Castelletti and Soncini-Sessa, 2007a, 2007b). Yet, impact assessment of different scenarios is not straightforward in an index framework, as cause and effect relationships between policy initiatives, remedial actions and their impact are not correctly integrated.
Against this background, this paper exploits the flexibility of Bayesian networks (BNs) to simultaneously exploit multiple cause-effect relationships and to unravel the links between poverty and WaSH services. In doing so, we seek to produce a valuable planning tool that takes into account the process uncertainties and guides decision-makers in evaluating decision options against multiple criteria and in choosing the most appropriate actions.
First, a WASH-focused approach is adopted through a multidimensional estimate, the WaSH Poverty Index (WaSH PI), which is taken as a starting point to define the conceptual framework. This index was proposed in a previous study by us (Giné Garriga and Pérez Foguet, 2013a), to integrate in measurement the socio-economic, physical, environmental, and institutional drivers that affect the sustainable access and use of water and sanitation services. Its theoretical foundations build on a combination of three composites that separately report on different service levels for drinking water, sanitation, and hygiene. The water-related index is founded on the Water Poverty Index (WPI) framework from Sullivan (2002) and Sullivan et al. (2003) and tackles the priority water-related challenges in low-income settings: availability of water (Resources, $\mathrm{R}_{\mathrm{WPI}}$ ), access to water (Access, $\mathrm{A}_{\mathrm{WPI}}$ ), capacity for sustaining access (Capacity, $\mathrm{C}_{\mathrm{WPI}}$ ), and ways in which water is used for different purposes (Use, $\mathrm{U}_{\mathrm{WPI}}$ ). The Sanitation Poverty Index (SPI) aims to assess whether or not people use basic sanitation, and not the mere existence of infrastructure. Therefore, SPI not only gauges the extent of access to sanitation, both in terms of accessibility and affordability (Access, $\mathrm{A}_{\mathrm{SPI}}$ ), but also assesses people's ability to construct and repair latrines (Capacity, $\mathrm{C}_{\mathrm{SPI}}$ ), and includes those hygienic factors that enable a continued use of the facility (Use, $\mathrm{U}_{\mathrm{SPI}}$ ). The Hygiene Poverty Index (HPI) is measured by the aggregation of four different components (Webb et al., 2006), each one representing a different transmission route by which oral-fecal contamination may occur: drinking water $\left(\mathrm{DW}_{\mathrm{HPI}}\right.$ ), food $\left(\mathrm{F}_{\mathrm{HPI}}\right)$, personal hygiene $\left(\mathrm{PH}_{\mathrm{HPI}}\right)$, and domestic household hygiene $\left(\mathrm{DH}_{\mathrm{HPI}}\right)$.
On the basis of the WaSH PI concept, an object-oriented Bayesian network (OOBN) model is then developed to identify the key determinants of sustainable access to water, sanitation and

hygiene. Bayesian network (BNs) are graphically structured and thus exploit the duality between an interaction graph and a probability model based on Bayes' rule (Castelletti and Soncini-Sessa, 2007a). The graphical structure provides a visual representation of the logical relationship between variables, while conditional probabilities quantify this relationship and are thus required to fully run the network (Bromley, 2005). BNs are made up of three different elements: i) a series of nodes representing a set of variables relevant to the problem at hand, ii) the links between these variables that express cause-effect relationships among them, and iii) the conditional probability tables (CPTs) behind each node that are used to assess the extent to which one variable is likely to be affected by the others (Bromley, 2005; Cain, 2001). The BN approach is useful for incorporating data and knowledge from different sources and domains, including the economic, social, physical, and environmental (Bromley et al., 2005; Castelletti and Soncini-Sessa, 2007a; Henriksen and Barlebo, 2008); this key characteristic makes BNs particularly suited for monitoring WaSH services in an interdisciplinary, holistic way (Alok, 2002; Fisher et al., 2015). Similarly, this technique has gained a reputation of being helpful for simulating complex problems that involve uncertain knowledge (Henriksen et al., 2007). In the field of water resources, where many variables are highly interlinked and uncertainty plays a key role (Bromley et al., 2005; Castelletti and Soncini-Sessa, 2007a), BNs have been increasingly applied as an aid to decision making (Bromley et al., 2005; Castelletti and SonciniSessa, 2007a; Henriksen and Barlebo, 2008; Molina et al., 2013, 2009). One weakness of conventional BNs, however, is that they are unable to receive or transmit information from outside the system (Molina et al., 2010). Alternatively, an OOBN model offers a suitable framework that allows different networks to be linked together. OOBNs are therefore appropriate for use as organizational applications, which is the focus of this research (Molina et al., 2013).

Here we present a case study from Kenya, on a national program that the Kenya government launched in 2010 (hereafter referred to as the "program" or the "intervention") to improve the access to safe drinking water, adequate sanitation infrastructure, and hygiene for the rural population. In light of its implementation, we first adopt the WaSH PI conceptual framework, due to its ability to integrate all relevant WaSH issues. We then apply an OOBN model as a management tool to support planning and decision making. With this study, we aim to judge the validity and relevance of this approach to assist planners and managers in i) capturing a comprehensive picture of the key elements that determine access to WaSH and their interlinkages, ii) making rational and informed choices between alternative actions, and iii) estimating the impact of these choices on key WaSH variables.

The article is structured as follows: Section 2 describes the methods and the process of OOBN construction and presents the case study; Section 3 presents and discusses the achieved results

and the network system, simulates two different scenarios to predict the impact of the program, and gives various recommendations for improving design, planning, and implementation of the intervention; and Section 4 highlights the major findings and conclusions of the study.

# 2 METHODOLOGY 

This section deals with the construction stages of the decision support system (DSS) based on an OOBN. To this end, a commercial software package produced by HUGIN® (v7.2) was used in this study. The first stage defines the problem and describes the transition process from an index to a network system. The second stage names the set of variables and identifies their interlinkages, to illustrate the context in which WaSH services are delivered. The third stage processes data from all available information sources. The fourth stage assigns the states for all variables, and then constructs the conditional probability tables. Finally, the fifth stage validates the model and its outcomes.

### 2.1 Study Area Introduction

In Kenya, a large proportion of the population does not have access to safe water and sanitation facilities. According to the last official statistics (Joint Monitoring Programme, 2015), about two-thirds of the population ( $63 \%$ ) has improved sources of drinking water, and only $30 \%$ has access to adequate sanitation facilities. Overall, the situation in rural areas is similar to the national average (of $57 \%$ and $30 \%$ respectively), but regional disparities are remarkable, and a large number of rural districts do not reach these coverage ratios. Water- and sanitation-related diseases significantly contribute to high mortality of children under five, with a rate of 74 per 1,000 children, with diarrheal diseases accounting for about $20 \%$ of cases in high-risk areas (Kenya National Bureau of Statistics [KNBS] and ORC Macro, 2010).
In 2010, within this high-risk environment, the government of Kenya in collaboration with UNICEF launched an initiative to increase access to safe drinking water and sanitation, and identified through a consultative process the vulnerable populations living in rural areas (United Nations Children's Fund and Government of Kenya, 2006). The Program targeted these populations, which are found in the pastoral arid and semi-arid districts of Isiolo, Wajir, Garissa, Mandera, West Pokot, and Turkana; in the Lake Basin Districts of Busia, Kisumu, Siaya, Bondo, Rachuonyo, and Nyando; in the Coastal district of Kwale and Tana River; in the Eastern province districts of Mwingi, Marsabit, and Kitui; in the Rift Valley province districts of Kajiado, Uasin Gishu, and Molo; and in the Kieni district of Central province. These populations ( 21 rural districts) were selected as initial case study to test the validity of an OOBN approach as a policy instrument to support planning.

# 2.2 Stages of network construction 

The step-by-step process, illustrated in Fig. 1, is described as follows:
![img-0.jpeg](img-0.jpeg)

Figure 1 The process of network construction
i. Define the problem and select the conceptual approach. The network system is constructed as a policy tool to inform planning and support targeting and prioritization. Specifically, it seeks to better understand the mid- and long-term impact of the program, as a necessary step to formulate concrete recommendations for improved planning and implementation. In this study, the BN was divided into three subnetworks to represent the three thematic indices of the WaSH PI and their components: the water supply, sanitation, and hygiene subnetworks. To promote correct linking of specific nodes from these different subnetworks with outside networks, specific feature of the OOBN model were exploited; that is, information was transferred from one network to the other through instance nodes. These nodes represent an "instance" of another network, and are thus employed to import (input node) or export (output node) information within different networks.
ii. Define the variables relevant to the problem and identify key linkages among them. In total, 93 variables were identified and classified based on their nature (see Table 1 and Tables S1-S4 of Supplementary Materials):

- "Objectives" are those variables that the program aims to improve (Figs. 3-6; indicated

in green). As for the index structure, these variables correspond with the components of each thematic index and the indices themselves (e.g., the WPI and its four components: $\mathrm{R}_{\mathrm{WPI}}, \mathrm{A}_{\mathrm{WPI}}, \mathrm{C}_{\mathrm{WPI}}$, and $\mathrm{U}_{\mathrm{WPI}}$ );

- "Interventions" are all the actions implemented by the program to achieve these objectives (in beige). They constitute a clear comparative advantage of a network system in terms of planning, as defining and simulating a variety of scenarios through these nodes is straightforward;
- "Intermediate Factors" are all the elements that link "Objectives" and "Interventions". They may be i) context-based, e.g., time to fetch water, which may vary from one district to the other (in orange), or ii) object-oriented and relational, which are typically based on standard cause-effect relationships (in blue); and
- "Controlling Factors" (in yellow) are other variables that somehow influence the system but that cannot be controlled (e.g., wealth index).

Table 1 Classification of variables at sub-network level


Another critical issue in OOBNs development is to make the inter-relation of variables a central part of the selection process. This is an issue of not only identifying reliable variables but also linking them through appropriate cause-effect relationships.
iii. Collect data for populating the conditional probability tables that lie behind the variables. A key part of the process is to make sure that the CPTs constructed for each variable are based on the best information available, sometimes despite being imperfect or not wholly reliable. A strength of BNs is their ability to integrate different type of data, but of course the less reliable the information, the more uncertain the result and the wider the distribution of probabilities (Bromley, 2005). In this study, the data used were obtained from two major information sources: i) the "intervention" nodes used data available in the main report of the Programme of Cooperation "Acceleration of Water Supply and Sanitation towards Reaching Kenya's Millennium Development Goals (2006 - 2011)" and its annexes (United Nations Children's Fund and Government of Kenya, 2006); and ii) data used to construct

the CPTs of the context-based "intermediate" nodes and the controlling factors were obtained from the baseline database of the program. In all recipient districts, a householdbased survey was conducted in parallel to field inspections of a reduced number of water points. In every visited household, service level was captured through a structured questionnaire administered to primary caregivers and direct observation. Data at the water point were collected using a standardized checklist to cover management and operational aspects (Giné Garriga and Pérez Foguet, 2013b). In addition, expert opinion was consulted to inform those nodes for which data was limited or unreliable.
iv. Define the states for all variables and complete the conditional probability tables (CPTs). Once the variables have been defined and grouped, there is a need to define their states and quantify their relationships in terms of probabilities. States of variables are typically described in one of four ways: as labels (qualitative information), discrete numbers, intervals, or a Boolean format (Bromley, 2005). Statistically speaking, the first three relate to a categorical variable, i.e. each can take one of a limited, and usually fixed, number of possible values, while the latter corresponds to a binary variable, i.e. it can take only two possible values. The complexity and size of the CPTs depend on the number of parents and the number of states of the respective variable (Cain, 2001). Indeed, constructing a CPT requires an adequate understanding of the existing causal relations and the impact of changing the states of one node on all variables linked to it. It is therefore advisable to construct the network with a limited number of parents and states; in this way, the CPTs become much more manageable. In this study, the number of parents and states were kept to a minimum, with not more than four in any case. The resulting CPTs have been populated by three different mechanisms:

- Converting the program outcomes into input data for the "intervention" nodes. For instance, by computing the number of people covered with new infrastructure (input data in the node named "Construction of water points") based on the number of water points constructed by the program (outcome).
- Processing data contained in the baseline database in the form of a contingency table. Information can be either quantitative or qualitative. In both cases, data are summarized as counts of events happening or counts of values that occur within given intervals. The contingency table displays the frequency distribution of the variables in a matrix format. For instance, in the node termed "Water consumption rate", one could easily count the number of households for any given rate of water consumption on the basis of the distance to the nearest water source from the dwelling.
- Using stakeholder knowledge and expert opinion when data that link two variables are scarce or non-existent, or when the link is difficult to quantify. For example, one might

be concerned about the influence of water tariffs on affordability issues and willingness to pay. In these cases, 'expert opinion' may be used to reduce the difficulties faced when populating this CPT, as baseline data was not available. Alternatively, one may opt to define a mathematical expression to quantify the probabilistic dependency between two or more variables. For instance, one may determine that access to improved water points results from multiplying the sum of the available water points and those constructed or rehabilitated by the program by the standard functionality rate given in a specific area. Of particular interest in this regard is the construction of the "objective" nodes, as they ultimately determine the level of water, sanitation, and hygiene-related poverty. As proposed by Giné-Garriga and Pérez-Foguet in previous studies (2010; 2013a), a weighted multiplicative function was used:

$$
W P I=\prod_{i=R, A, C, U} X_{i}^{w_{i}} \quad \text { SPI }=\prod_{i=A, C, U} X_{i}^{w_{i}} \quad H P I=\prod_{i=D W, P H, F, D H} X_{i}^{w_{i}}
$$

where WPI / SPI / HPI relate to the "objective" nodes, $\mathrm{X}_{\mathrm{i}}$ refers to parent node i within the network structure, and $\mathrm{w}_{\mathrm{i}}$ is the weight applied to that parent node (equal weights were used in this study).
v. Evaluate and validation the network, once the system design and data entry is complete. When the DSS has been compiled and the probability distributions of all variables change according to the scenarios that were set, there are few steps that may help check network consistency. This can be done by noting the impact of each implementation variable one-by-one. If, for instance, the variable "Construction of latrines" is changed to represent that the intervention is in place, the "SPI Access" variable should show an increase. If this does not occur, and if no other variables have an impact, it is likely the values in the CPTs are wrong and need to be re-examined. Alternatively, one may confirm that the final results are coherent and coincide with the current known situation. In this study, the outcomes of the network -that is, the probability distribution of the "objective" nodes- were compared with the results obtained in a complementary study, in which WaSH PI values are computed through an index-based approach with the same conceptual background and data set (Giné Garriga and Pérez Foguet, 2013a).

# 3 RESULTS AND DISCUSSION 

This section first describes the network system, showing its ability to accurately accommodate the key issues of WaSH services delivery. Second, it shows the validation of OOBN by comparing the results obtained from the model and an index-based approach. Third, two different scenarios are simulated to better understand the potential impacts of actions envisaged

by the program: the "Business as usual" scenario (BAU) (the current situation) is compared with a scenario defined by the program outcomes.

# 3.1 DSS Development 

This section describes the networks developed to represent the context in which water, sanitation, and hygiene services are delivered. Within the WaSH PI framework, each service is conceptualized through a thematic index (WPI, SPI, and HPI) and graphically depicted in a separate subnetwork. For clarity purposes, however, the water network develops the "capacity" component $\left(\mathrm{C}_{\mathrm{WPI}}\right)$ as a distinct subnetwork. All four subnetworks -water, water capacity, sanitation, and hygiene- are integrated and linked through an OOBN master network (Fig. 2). Specifically, information is transferred from one network to another through output and input nodes. All "objective" nodes appear as system outputs, which are then grouped in additional networks to compute the final WPI, SPI, and HPI values.
The master network therefore describes the overall behavior of the system. From Fig. 2, it can be seen that any refinement in a variable of any sub-network results in a chain reaction that impacts all the linked variables, thereby affecting the outputs of the whole system. Thus, a major advantage of this tool is that it can easily predict the potential impact of a number of interventions on all interrelated factors; therefore, identifying which action, or combination of actions, will produce the desired results appears straightforward.
A broad outline of each subnetwork follows, and the meaning of each individual variable (node) is provided in Tables S1 to S4.

### 3.1.1 The water network

The water network seeks to provide a suitable framework to assess water and poverty linkages. It encompasses the key issues included in the WPI, as defined by Sullivan et al (2003): water resources availability (WPI Resources) and people's ability to get and sustain access to water (WPI Access and WPI CAPACITY, respectively) and to use this resource for productive purposes (WPI USE).
The 'Resources' component seeks to assess availability of water resources. As shown in Fig. 3 (and detailed in Tables S1 and S2), this is based in the context of diminishing water availability as a result of inadequate protection of water resources on the supply side, and increasing use of water as a function of population growth and local livelihoods on the demand side. In this respect, a set of variables determine resource availability as a balance between water quantity (node code W_IF_16 - Table S1), water use (W_IF_17), and water quality (W_IF_22). The seasonal variability of water resources is another factor that has been taken into account (W_IF_20). Lack of relevant data may hinder the assessment of these variables, particularly at

the local scale, since hydrogeological data are limited and groundwater recharges are largely unknown. Information sources employed to construct these nodes were qualitative, and, for instance, reports of conflicts over water sources (W_IF_17) are included as a variable to assess competition between different water uses. Though not rigorous, these data represent the best estimate available. The program emphasizes the need to improve the supply-side by implementing regular water quality surveillance initiatives (W_IN_05). Complementary to this supply-side focus, it embraces demand-side management by promoting multiple use water services to meet people's multifaceted water-related needs, while at the same time maintaining a healthy environment (W_IN_04).
The water network also assesses whether or not people have ready access to a water source, as this may limit the quantity of suitable water that is available to a household for domestic purposes. A set of variables are first used to determine service continuity (W_IF_07) as the proportion of time that a water source is functional and accessible for use. Accessibility may be also hindered by the ability of households to pay for water (W_IF_15). In case of unaffordable expenses, the poor might be forced to collect water from unprotected sources (when available) or to manage with minimum amounts at other times. No data was however collected on household water expenditure, and these nodes were assessed through three different alternative indicators: i) a wealth index, as a 'proxy' measure of household's wealth (W_CF_01), ii) user's perception of the cost of water (W_IF_14), and iii) the existence of tariff exemptions for vulnerable people (W_IF_13). Equally important, non-functionality may be an obstacle to continued access to water supply (W_IF_09), as interrupted services oblige households to search for alternative sources, often of inferior availability and poorer quality. Recent studies suggest that one third of rural boreholes with handpumps in sub-Saharan Africa are nonfunctional (RWSN, 2012). The program consequently focuses on both the construction of new water points (W_IN_03) and on the rehabilitation of existing ones (W_IN_02).
The long-term functionality of water schemes is directly linked to the suitability of the institutional framework in charge of maintaining and operating the services. Fig. 4 presents all key variables that determine to what extent the capacities of local stakeholders are to be increased throughout the program. A first group of nodes focuses on the institutional framework required to properly manage the services. The Water Act (2002) provides for a decentralized structure to deliver water services, in which local Water Service Providers (WSPs) are responsible for operating and managing water supplies. A large challenge nonetheless lies within the capacity of these institutions to perform as expected and to lead in revitalizing the water sector. Thus, emphasis was placed on training and capacity building (WC_IN_03) and institutional support from government and non-government organizations (WC_IN_02). Integral to this set of variables, an assessment of the financing strategies appears essential (WC_IF_09),

to understand which mechanisms are in place for revenue collection that contribute towards the cost of running the water supply. Another group of variables determines the status of the supply of equipment and spare parts in the local markets (WC_IN_07), as well as skills and capacities in the private sector (WC_IN_05). Both aspects are required to properly maintain the facilities once the intervention is completed.
Finally, the network aims to capture the use communities make of the water for domestic purposes (W_IF_03). In particular, research has shown that those who require more than 30 minutes per round trip progressively collect less water (Cairncross and Feachem, 1993), and a set of variables are used to determine the reduction of time invested in securing water after the program completion (W_IF_02).

# 3.1.2 The sanitation network 

The 'Sanitation' network aims to represent all key variables that determine whether or not people have sustained access to improved sanitation, which entails easy access to sanitation infrastructure (SPI Access), a continued use of the toilet facility (SPI Use), and the ability to fix and repair it in case of a breakdown (SPI CAPACITY).
Indeed, a clear distinction needs to be made between access to and use of the facility. In Fig. 5 (and detailed in Table S3), a first set of nodes seeks to assess accessibility issues, in terms of physical access (node code S_IF_06) and affordability (S_IF_04). The sanitation facility should be located within, or in the immediate vicinity of, each household, in order to ensure minimal risks to the physical security of users (S_IF_05). And access to sanitation facilities and services should be available at a price that is affordable for all, without limiting their capacity to acquire other basic goods and services.
To foster sustained use of sanitation, an improved facility (with associated services) should be available when needed, where the definition of "improved" is technology-based (S_IF_01), as proposed by the WHO / UNICEF Joint Monitoring Programme (JMP) (Joint Monitoring Programme, 2008, 2006). In addition, sanitation facilities must be hygienically safe to use, since lack of latrine maintenance may not only constrain a continued use of the infrastructure, but also result in a focus of disease transmission (Exley et al., 2015). The sanitary condition of latrines (S_IF_11) is evaluated through three different proxies: i) inside cleanliness (S_IF_10), ii) presence of insects (S_IF_07), and iii) smell (S_IF_08). Equally important, toilets have to be constructed to provide privacy and ensure dignity (S_IF_09). In order to improve hygiene awareness and change sanitation-related behaviors, various approaches are adopted throughout the implementation of the program (H_IF_01), including hand washing and point of use water treatment and storage (see the hygiene subnetwork).
Finally, there is a need to develop a reliable and affordable supply stream, to ensure that

products and goods are accessible. In places where the sanitation supply chain is fractured and confusing, consumers may experience an additional barrier to purchasing a latrine. In response to this priority, the program aims to guarantee availability of materials while recruiting and training hardware storeowners and masons (S_IN_03 and S_IN_04, respectively).

![img-1.jpeg](img-1.jpeg)

**Figure 2** Scheme of the OOBN master network. Each sub-network is illustrated in a separate box. Input nodes (dashed lines) and output nodes (solid lines) enable the import and export of information outside the subnetworks, respectively.

![img-2.jpeg](img-2.jpeg)

**Figure 3** The water network. "Objective" nodes are shown in green; "intervention" nodes, in beige; "intermediate factors - context", in orange; "intermediate factors - relational", in blue; and "controlling factors", in yellow. Input nodes are depicted as dashed lines outlined in grey, and output nodes, as solid line nodes outlined in grey.

![img-3.jpeg](img-3.jpeg)

**Figure 4** The water-capacity subnetwork. "Objective" nodes are shown in green; "intervention" nodes, in beige; "intermediate factors - context", in orange; "intermediate factors - relational", in blue; and "controlling factors", in yellow. Input nodes are depicted as dashed lines outlined in grey, and output nodes, as solid line nodes outlined in grey.

![img-4.jpeg](img-4.jpeg)

**Figure 5** The sanitation network. "Objective" nodes are shown in green; "intervention" nodes, in beige; "intermediate factors - context", in orange; "intermediate factors - relational", in blue; and "controlling factors", in yellow. Input nodes are depicted as dashed lines outlined in grey, and output nodes, as solid line nodes outlined in grey.

![img-5.jpeg](img-5.jpeg)

**Figure 6** The hygiene network. "Objective" nodes are shown in green; "intervention" nodes, in beige; "intermediate factors - context", in orange; "intermediate factors - relational", in blue; and "controlling factors", in yellow. Input nodes are depicted as dashed lines outlined in grey, and output nodes, as solid line nodes outlined in grey.

# 3.1.3 The hygiene network 

This network encompasses the different pathways by which oral-fecal contamination and, subsequently, diarrhea may occur: contamination of stored drinking water (HPI DRINKING Water Quality), food (HPI Food Hygiene), or hands (HPI Personal Hygiene); and presence of animals or insects that can transmit fecal contamination to previously clean surfaces (HPI DOMESTIC HYGIENE).

It can be observed from Fig. 6 (and in detail in Table S4) that a set of nodes relates to improvements in drinking water quality. On the one hand, water may become contaminated by poor collection, transportation, and handling practices, as people mainly collect it from a source and take it home (node code H_IF_05). On the other hand, adequate household water treatment (HWT) is an important interim measure for removing pathogens from drinking water and reducing disease risk, particularly for those who do not have access to safe supplies. To improve the quality of drinking water, the program combines increased use of water quality surveillance approaches with other short- and medium-term interventions (W_IN_05), such as household water treatment (HWT) and safe storage (H_IN_03).

The network also combines a number of indicators to assess personal hygiene and, particularly, the practice of handwashing (H_IF_10). Appropriate handwashing includes two dimensions (Billig et al., 1999): critical times -e.g., after defecation, before food preparation, before eating, etc. (H_IF_09)-, and technique -e.g., washing both hands, rubbing hands together at least three times, drying hands hygienically, etc. (H_IF_08)-. Most importantly, studies show that handwashing behavior is strongly influenced by the presence or absence of a convenient source of water and soap (Curtis and Cairncross, 2003). The program covers both the hardware (e.g., construction of handwashing devices) and the software (e.g., handwashing education) (H_IN_05 and H_IN_04, respectively).

The last group of nodes seeks to provide an overview of household hygiene. Specifically, three indicators relate to those health risks arising from unsanitary conditions of household plots, i.e., the presence of animals running freely (H_IF_03), the presence of rubbish in yards and inside homes (H_IF_02), and the presence of feces (H_IF_04). A variety of interventions will be in place throughout the program to increase hygiene awareness and improve hygiene behaviors, as an effective way to break the fecal-oral route of disease transmission (H_IN_02).

### 3.2 DSS validation

Once the network model has been developed, an easy test to check its consistency is to verify that all variables change according to the actions set by the "intervention" nodes. For instance, the implementation of the program increases the percentage of households with a latrine located in the same compound by $22 \%$, through construction of new latrines (Fig. 7). The baseline data

is not affected by the program, and on average, physical access to sanitation improves from 0.51 to 0.62 . This affects the objective node "SPI Access", which has a $46 \%$ probability of being between $0.5-1.0$ after program completion. Both the magnitude and direction of the impact chain are logical and consistent. However, because of the uncertainty of data and the model assumptions, there is also a chance that the variable might be in other states, as shown by the distribution. Indeed, the explicit representation of uncertainty and variability in the model outcome provides a transparent way to represent the impact achieved by the program.
Besides to this easy-to-implement quality check, evaluation and validation of the network system has been also conducted by comparing the OOBN outcomes with results achieved in a parallel study (Giné Garriga and Pérez Foguet, 2013a). In this previous study, an index-based approach was adopted to assess the baseline context of the program, and the three thematic indicators - WPI, SPI and HPI - and their components were computed.
Comparing statistics from both studies -that is, the stochastic approach based on OOBN versus the deterministically-developed index- reveals that overall values of the three indices show similar trends, although the OOBN model values are lower than those obtained by the index (e.g., with average SPI scores of 0.37 or 0.50 when computed with OOBN or a composite index, respectively) (Fig. 8). Similarly, as could be expected, variability of OOBN estimates is considerably lower. OOBNs employ categorical or binary variables. Likewise, a closer look at the indices' components shows no significant differences, albeit with three remarkable exceptions in which differences are attributable primarily to the variables employed in component construction. Specifically, for the index approach, the WPI Access component includes the gender dimensions of drinking water collection in the analysis, the WPI USE component includes one indicator to verify that main drinking water source was used by the household for other domestic purposes, and the SPI CAPACITY includes one indicator to identify the reasons why households without their own latrine did not have one. These three indicators are not considered in OOBN development, as they cannot be easily integrated into cause-effect relationships, and they are not significantly influenced by the Program. All of these variables present extreme values, of $0.07,0.91$, and 0.97 , respectively, which significantly reduces or increases the final score of the related components.

![img-6.jpeg](img-6.jpeg)
a) The network and its variables
![img-7.jpeg](img-7.jpeg)
b) SPI - Access, with no intervention

## WaSH program (intervention node)

Boolean variable - two states:

- No WaSH program
- WaSH program


## Construction of latrines (intervention node)

Boolean variable - two states:

- 0 : No new beneficiaries
- 1: New beneficiaries (households accessing sanitation facilities)


## Latrine location, baseline data (intermediate factor)

Boolean variable - two states:

- 0 : the latrine is located outside the compound
- 1: the latrine is located in the same compound


## Access, physical (intermediate factor)

Boolean variable - two states:

- 0 : the household has no access to a facility in the same compound
- 1: the household has access to a facility in the same compound


## SPI - access (objective)

Intervals - four states (\% of households accessing a facility that is affordable and located in the same compound):

- 0-0.25; 0.25-0.50; 0.50-0.75; 0.75-1.0
![img-8.jpeg](img-8.jpeg)
c) SPI - Access, with intervention

Figure 7 OOBN validation. Partial representation of the sanitation subnetwork, which shows the impact of the program on the "SPI Access" objective node

![img-9.jpeg](img-9.jpeg)
c) HPI

Figure 8 WPI, SPI, and HPI values and variability: $\overline{\mathrm{x}}$ : sample mean; s: SD

# 3.3 Analysis of the program outcomes 

The results shown in this section represent a first attempt to assess the potential impact of the actions set by the program. However, as explaining the impact of each individual action is not feasible, the discussion focuses on a purposive selection of the most significant interventions. Where necessary, the analysis also includes the scale of change at the indicator level.
Two different scenarios have been simulated and compared. The "Business as usual" scenario (BAU) is assumed to be the current condition, as described by data available in the baseline survey. The second scenario adopts the program approach. It is therefore made up of a variety of actions to be implemented by the government, which are represented in the networks as "intervention" nodes. Table 2 describes three of these actions as examples (see also the comprehensive list in Tables S5 to S7). The CPTs of these nodes were populated based on the program outcomes (United Nations Children's Fund and Government of Kenya, 2006). For instance, it can be observed that supplying water to 1.3 million people is roughly equivalent to covering $18 \%$ of the total population. It is by acting on these "intervention" nodes that the software simulates both scenarios.

Table 2 Examples of "intervention" variables in two simulated scenarios


${ }^{a}$ Values represent the set of probabilities, one for each variable, specifying the belief that a node will be in a particular state given the two implementation scenarios outlined above: i) "Business as usual"; and ii) WaSH program

Fig. 9 compares the results obtained for each scenario. According to the charts, the intervention would produce a positive impact on overall WaSH poverty, since the probability distributions of the three thematic indicators show slight improvements after the project completion. With

respect to water-related context, there is roughly a $7 \%$ chance that the WPI increases from 0 0.25 to $0.5-0.75$, with the probability of lying within the $0.25-0.5$ interval roughly the same ( $49 \%$ before the intervention, and $47 \%$ after). There is also an increased chance of the SPI and HPI values falling within the range $0.5-0.75$ after program completion (from 22.48 to 41.82 , and from 18.65 to 30.76 , respectively).
An accurate focus on the components might help to direct attention to those WaSH sector needs that require special policy attention. For example, and in accordance with Fig. 9a, policy attention should be given to those issues related to WPI CAPACITY and WPI USE. If attention is paid to sanitation (Fig. 9c) and hygiene (Fig. 9e), one may realize that other aspects requiring urgent intervention include SPI CAPACITY, HPI PERSONAL HyGIENE, and HPI FOOD Hygiene. This situation may be compared to that represented in Figs. 9b, 9d, and 9e, in which it can be observed that the Program affects the set of variables differently, e.g., it considerably improves the overall sanitation index and the HPI DRINKING WATER QUALITY component but only modestly affects water issues. This preliminary analysis provides a useful insight into the impact that the Program may or may not have on those key challenges faced by the sector. To promote improved planning, however, a more detailed description of achieved results at subnetwork level follows.
![img-10.jpeg](img-10.jpeg)
a) WPI - Business as usual (no intervention)
![img-11.jpeg](img-11.jpeg)
b) WPI - WASH Program
![img-12.jpeg](img-12.jpeg)
c) SPI - Business as usual (no intervention)
![img-13.jpeg](img-13.jpeg)
d) WPI - WASH Program

![img-14.jpeg](img-14.jpeg)
e) HPI - Business as usual (no intervention)
![img-15.jpeg](img-15.jpeg)

# f) HPI - WASH Program 

Figure 9 The OOBN Final Values. Each component of the index is described in a separate box and shows the mean value, standard deviation, and probability histogram

### 3.3.1 Tackling water poverty: New infrastructure while building up recipient capacity

Based on the expected outcomes of the program (United Nations Children's Fund and Government of Kenya, 2006), the water supply component of the intervention includes the development of water sources for new users currently unserved ( 1.3 million beneficiaries). It will also include the rehabilitation of existing dysfunctional water systems, which will be used by an additional 310,000 people. Despite the construction and rehabilitation of water points, the model simulation suggests poor rate of progress; i.e. access to water infrastructure (WPI Access) increases on average only from 0.46 to 0.49 . In more detail, the node named "Access to improved water points" (node code W_IF_12; data not shown) has a $60.62 \%$ chance of being between 0 and $25 \%$, which is consistent with last official data reported by the JMP (Joint Monitoring Programme, 2015).
The obvious linkages between inadequate access and time spent on fetching water have a direct impact on domestic water use: namely the longer the distance, the lower the consumption. Program managers should therefore not expect significant improvement in water consumption associated with increased accessibility of water unless i) traditional water sources are particularly far away, ii) queuing is time consuming, or iii) water can be supplied to each household. As this is not the case, the program does not increase water use for domestic purposes, as shown by the WPI Use component.
Beyond the hardware, capacities to manage water facilities are required at both local and regional scales, which present a major challenge for addressing the existing gap in institutional performance. The intervention will help the new sector-related organizations to meet the necessary skills and abilities to fulfil their role effectively. In particular, the capacity building process includes the provision of basic equipment and training in planning, procurement, and management skills. Women groups will also receive priority in the ownership of the water facilities and in the process of hygiene and sanitation promotion. The local private sector will also be stimulated and strengthened to develop an adequate spare parts supply chain (United

Nations Children's Fund and Government of Kenya, 2006). Although more effort should be placed on capacity building and institutional support, achieved results show good progress in this regard: there is $15 \%$ chance that the WPI CAPACITY component increases from $0-0.25$ to $0.5-0.75$; i.e., the probability within the $0-0.25$ interval diminishes from $30 \%$ to $15 \%$, the likelihood of any value in the range $0.5-0.75$ increases from $21 \%$ to $37 \%$, and the probability of being in the $0.25-0.5$ interval roughly remains the same ( $49 \%, \mathrm{BAU} ; 46 \%, \mathrm{WaSH}$ program).
Finally, the program seeks to promote water quality surveillance and improve resource management. The concern is not only at a macro-level, such as degradation of rivers and water catchments (with basin authorities committed to water resources conservation), but also at the micro-level. As inadequate designs of schemes to prevent source pollution and poor management of water points may lead to increased pollution of the water bodies, the program includes regular surveillance inspections for continuous water quality monitoring. In addition, it adopts a multiple-use water service approach as an alternative form of providing rural water services in an integrated manner; i.e. multiple uses of water (such as livestock watering, the production of fodder for animals, and small-scale irrigation) are to be encouraged to increase food security and thus reduce the vulnerability of the people living in the area (United Nations Children's Fund and Government of Kenya, 2006). Both interventions have a positive impact on the WPI Resources component, which slightly improves after project completion (increasing on average from 0.56 to 0.62 ) (Figs. 9a and 9b).

# 3.3.2 Tackling sanitation poverty: Development of a reliable supply chain 

The promotion of household sanitation will be closely linked to the provision of hardware and to hygiene promotion. It is important to note, however, that Government allocation and expenditure for environmental health is low compared to expenditures for water infrastructure. Sanitation and hygiene therefore has a lower profile (United Nations Children's Fund and Government of Kenya, 2006). The intervention first includes the construction of latrines for 1.6 million new beneficiaries. However, much like the water supply component, interventions are unlikely to achieve remarkable improvements. Results suggest that there is only an approximately $6 \%$ chance that the SPI Access component increases from $0-0.25$ to $0.75-1$ due to the intervention (Figs. 9c and 9d), with the probability values for the $0.25-0.5$ and $0.5-0.75$ intervals roughly equal before and after program completion. In detail, the node "Use of improved sanitation" (node code S_IF_03, data not shown) reveals that approximately $60 \%$ of the population will lack access to improved sanitation after program completion.
In parallel, the implementation strategy relies on a competitive marketing approach, during which 33,000 sanitation and hygiene promoters will be mobilized, trained, and equipped in order to ensure that at least 217,000 households (approximately 1.3 million people) are

motivated to build and use a toilet at home. Equally important, the sanitation supply chain will be strengthened through a two-fold approach: i) traditional models, as developed and used by women groups in many parts of Kenya, are applied to meet their demands for home improvements, and / or ii) micro-enterprise models that have been developed by various microfinancing agencies are supported to promote local manufacturing and services (United Nations Children's Fund and Government of Kenya, 2006). It can be deduced from Fig. 9 that sanitation approaches to stimulate both demand and supply will produce a significant effect, improving on average the final SPI CAPACITY and SPI USE values by fourteen (from 0.36 to 0.5 ) and five (from 0.47 to 0.52 ) percentage points, respectively.

# 3.3.3 Tackling hygiene poverty: Promotion of hygiene 

Hygiene education and promotion is expected to be a core activity within the program. It will consist of two different components: increased hygiene awareness, and in particular improved handwashing behavior, and widespread promotion of point-of-use water treatment. In the same way as with sanitation, the target is to mobilize and train 33,000 hygiene promoters who will cover 350,000 households (approximately 2 million beneficiaries) through direct marketing, though larger numbers are likely to be reached by mass marketing (e.g., radio, local newspapers, and promotional campaigns). After project completion, communities should have a good level of understanding of the link between poor hygiene and diseases (United Nations Children's Fund and Government of Kenya, 2006).

First, the project will foster hygienic handling of water as well as point-of-use treatment. It is assumed that direct beneficiaries of the program have access to potable water sources, and that good hygiene will ensure safety at the point-of-use. For the unserved population, household water treatment is promoted to improve their drinking water quality from whatever source they use and thus to ensure safety. Indeed, the HPI DRINKING WATER QUALITY component is expected to have a significant impact at project completion, as it expands on average 10 points (from 0.49 to 0.59 ) (Figs. 9e and 9f).

Second, a handwashing campaign will promote hand washing with soap at appropriate times (e.g., before eating and after defection), with campaign taking the form of both direct and mass marketing. Direct marketing in rural villages will be mostly carried out by hygiene promoters, backed by marketing teams from the private sector. There will also be mass marketing using the mass media. Achievements related to HPI PERSONAL HYGIENE are to a certain extent limited, as observed from Fig. 9. This is partly explained by poor accessibility to adequate handwashing infrastructure; indeed, the node "Hand-washing, hardware" (node code H_IN_05) shows that roughly eight out of ten households still lack a basic handwashing facility after program completion.

Modest improvements are also made in relation to HPI DOMESTIC HyGIENE, i.e. by one percentage point on average (from 0.5 to 0.51 ). On the other hand, the impact of the intervention on HPI FOOD HyGIENE is more visible, with an increase from 0.37 to 0.43 . In the latter case, however, only one indicator has been assessed ("Drying rack", node H_IF_07), which may hamper an adequate understanding of the context.
Overall, more emphasis should be placed on hygiene education to promote awareness of good hygiene practices, in particular the issue of handwashing.

# 4. CONCLUSIONS 

Results indicate that an OOBN is able to accommodate the complexities of WaSH issues and their interlinkages. In addition, it effectively combines a wide variety of information sources, such that different sets of data from economic, environmental, physical, and social domains have been exploited in this study. The OOBN model integrates simultaneous cause-effect relationships, thus taking into account the existing user - service - environment interactions. In doing so, it provides a more complete picture of the context in which the services are delivered, where multiple determinants interact to affect outcomes of interest, such as coverage, service level, operational status of infrastructure, and hygiene awareness. Specifically, the results suggest that those sectors that require urgent policy attention in Kenya relate to the management capacities of water committees, the promotion of multiple uses of water to meet people's multiple water needs, the availability of a reliable sanitation supply chain to stimulate the construction and repair of latrines, and the promotion of behavior change for improved personal hygiene.
In comparison with other DSS, an OOBN provides an easy-to-exploit framework in which decisions in WaSH planning and management can be based. First, the graphical nature of network presentation makes it easier to illustrate the impact of a range of different actions and strategies to stakeholders. Second, uncertainty is explicitly represented, as results are given as a probability distribution. This allows decision makers to first estimate the chance that a specific intervention will have a particular effect, and then to investigate the consequences of their uncertainty. A third distinct advantage is the stochastic and modular nature of the OOBN technique, which produces outcomes that are more flexible than those produced by deterministic approaches (e.g., a composite index). Results can then be analyzed for a range of scenarios and/or conditions, enabling policy planners to identify the combination of actions in which to direct their efforts for maximum impact. In this study, for instance, a number of interventions are included within the program strategy, which differently affect the sector challenges cited above. Thus, we were able to show that capacity building processes have a positive impact. In contrast, use of water and sanitation infrastructures remains low after the program completion.

For hygiene, the promotion of point-of-use water treatment contributes to increase water safety, while there is only a "modestly improving trend" with respect to handwashing behavior.
This study however describes the first iteration of the model. As such, there are certainly improvements to the networks and methodology that can be made. In general, it would be worthwhile to try to reduce the number of nodes included in the analysis. With this in mind, the water network and its "Capacity" component could be simplified, identifying those nodes that better describe the managerial aspects of the service, and removing any redundant nodes. Additionally, the number of states could be lowered for some variables without losing any critical information. All of these efforts would be directed at simplifying the model. In turn, this would not only improve understanding of the model by non-technical audiences, but also facilitate additional data collection, as a necessary step to keep the system updated.
To conclude, this paper shows that an OOBN approach has the potential for wider implementation as a planning tool in the context of WaSH service provision, particularly at the national level. Similar models could be also developed for the local scale. Interestingly, one major advantage is that once developed, the same model can be applied repeatedly for different administrative units (e.g., districts, municipalities, communities, etc.) by changing the contextrelated data (i.e., the CPTs of nodes, graphically depicted in orange in Figs. 3 to 6). In short, it can be stated that a network approach might be useful where the concept is clear -that is, the key variables and their cause-effect relationships are well defined- and if data availability is not an issue. However, one major drawback is that this tool requires software that needs to be used by highly qualified people. This hinders to a certain extent its implementation in certain contexts, where resources are limited and stakeholders often lack capacities to profit from the model once developed (e.g., rural decentralized settings).

# SUPPLEMENTARY MATERIALS 

Supplementary Materials include seven additional tables. Tables S1 to S4 present the list of nodes employed in each network, their states, and their calculation method, while tables S5 to S7 describes the CPTs of all the "intervention" variables in two simulated scenarios: "Business as usual" and "WaSH Program".

## ACKNOWLEDGEMENTS

The authors would like to thank the United Nations International Children's Emergency Fund UNICEF (Eastern and Southern Africa Regional Office and Kenya Country Office) and Rural Focus Ltd. Consultancy for their contribution and support in various ways. This research has been partially funded by the Catalan Government (Agència de Gestió d'Ajuts Universitaris i de Recerca

(AGAUR), "Engineering Sciences and Global Development" project, ref: 2014SGR1545:20142016).

# A novel planning approach for the water, sanitation and hygiene (WaSH) sector: the use of Object Oriented Bayesian Networks 

## A novel planning approach for the water, sanitation and hygiene (WaSH) sector: the use of Object Oriented Bayesian Networks

R. Giné-Garriga, D. Requejo, J.L. Molina, A. Pérez-Foguet

Table 6 CPTs of the "intervention" variables in two simulated scenarios - Sanitation


${ }^{a}$ Values represent the set of probabilities, one for each variable, specifying the belief that a node will be in a particular state given the two implementation scenarios outlined above: i) "Business as usual", and ii) WaSH Program

# A novel planning approach for the water, sanitation and hygiene (WaSH) sector: the use of Object Oriented Bayesian Networks 

R. Giné-Garriga, D. Requejo, J.L. Molina, A. Pérez-Foguet

Table 7 CPTs of the "intervention" variables in two simulated scenarios - Hygiene


[^0]
[^0]:    ${ }^{a}$ Values represent the set of probabilities, one for each variable, specifying the belief that a node will be in a particular state given the two implementation scenarios outlined above: i) "Business as usual", and ii) WaSH Program