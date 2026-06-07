# Article 

## The Management of Na-Tech Risk Using Bayesian Network

Giuseppa Ancione * and Maria Francesca Milazzo

## check for updates

Citation: Ancione, G.; Milazzo, M.F. The Management of Na-Tech Risk Using Bayesian Network. Water 2021, 13, 1966. https://doi.org/ 10.3390/w13141966

Academic Editor: George Arbonditsis

Received: 18 June 2021
Accepted: 15 July 2021
Published: 17 July 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Department of Engineering, University of Messina, Contrada di Dio, 98166 Messina, Italy; mfmilazzo@unime.it * Correspondence: giusi.ancione@unime.it; Tel.: +39-090-676-5596


#### Abstract

In the last decades, the frequency and severity of Natural-Technological events (i.e., industrial accidents triggered by natural phenomena or Na -Techs) increased. These could be more severe than simple technological accidents because the natural phenomenon could cause the prevention/mitigation/emergency systems fail. The dynamic assessment of the risk associated with these events is essential for a more effective prevention and mitigation of the consequences and emergency preparation. The main goal of this study is the development of a fast and dynamic tool for the risk manager. An approach supporting the management of the consequence is presented. It is based on the definition of a risk-related index, presented in the form of a discrete variable that combines frequency and magnitude of the events and other factors contributing to the worsening of Na-Tech. A properly designed Geographical Information System (GIS) allows the collection and processing of territorial information with the aim to create new data contributing to the quantification of the Na -Tech risk index. A Bayesian network has been built which efficiently lends in including within the model multiple elements with a direct or indirect impact on the distribution of risk levels. By means of this approach, a dynamic updating of the risk index is made. The proposed approach has been applied to an Italian case-study.


Keywords: natural-technological events; hazardous material; chemical industry; dynamic risk assessment; risk management; flood

## 1. Introduction

Natural disasters, beyond having a negative impact on urbanised territories, can cause technological accidents due to the impact phenomenon on industrial activities. These accidents are the so-called Natural-Technological events [1-3] (Na-Techs). If industrial activities handle and/or store hazardous substances, the release and diffusion of chemicals into the environment could also occur [4-6]. These scenarios usually have more severe consequences than the natural event [7], given that the simultaneous occurrence of the natural disaster and the technological event determines a concurrent response effort in a context where resources could be overloaded or unavailable due to the catastrophic scenario [8]. This is the case of establishments classified at major accident hazard by the Directive 2012/18/EU (Seveso III Directive) [9].

In the last decades, the frequency and severity of Na -Techs increased. The main cause is the ageing of facilities that makes them more vulnerable to the impact of natural phenomena, as well as the effects of climate changes that increased the occurrence of extreme natural phenomena. Between 1980 and 2000, there were over 200 major events in Europe, which caused fires, explosions, and dispersions of toxic substances [10].

Floods are the most frequent natural phenomena triggering Na -Techs, as an overflow of water submerging the land represents a devastating event from the point of view of the consequences. Anywhere in the world, most industrial sites and related infrastructure developed close to rivers or coasts thanks to more favourable conditions for the activities, unfortunately this led to an increased exposure to this kind of events [11]. Some examples of Na -Techs due to floods and involving major accident hazard establishments are mentioned in the following. In 1994, a flood destroyed an oil depot causing at least one hundred

people died in Durunga (Egypt); in 2002, the flood of the El Maleh River caused fires and explosions in the Samir refinery in Mohammedia (Morocco), also in this case some people lost their lives; floods involved a refinery in Milazzo (Italy) in 2011 and in Livorno (Italy) in 2017, in both cases the events caused serious oil spill into the sea.

Territories impacted by floods are also exposed to contamination by organic and inorganic substances, that are released during the accident and reach all environmental matrices (air, soil, and water) due to the transport by floodwaters [12,13]. Some pollutants, after the release and transport in the ecosystems, may also be absorbed by crops and directly enter into the food chain [14]. Amongst sources to be aware about the potential of spreading pollutants in the environment after an inundation, there are many activities which are mentioned by the Directive 2008/1/EU, i.e., the Integrated Pollution Prevention and Control (IPPC) Directive [15]; these include solid and liquid waste treatment facilities, chemical and pharmaceutical plants, mining, energy production plants, food industries, textile industries, etc.

The current legislation for the assessment and management of flood risk is the European Directive 2007/60/EU [16], so-called Floods Directive (FD), which was implemented in Italy by the Decree Law no. 49/2010 [17]. It defines the flood risk as the combination of the probability of occurrence of a flood event, having a given intensity in a predetermined time interval, and the potential of negative consequences for the human health, environment, cultural heritage, and economic and social activities. To assess and manage Na-Tech risk, the probability and consequence of the technological event must be correlated to those of the natural phenomenon. Some risk assessment methodologies and dedicated tools have been developed to investigate Na -Techs and to assess and manage the risk during the last decade: a multi-level quantitative approach to evaluate the domino scenarios due to seismic Na -Tech was developed in [18]; some scholars estimated the vulnerability of wastewater treatment facilities to volcanic Na -Techs [19]; there are also contributions about the impact of natural disasters on critical infrastructure [20]; finally a short-cut approach assessing the vulnerability of a territory to seismic Na -Techs was developed [21]. Nevertheless, a dynamic assessment of the risk is essential for a more effective prevention, preparedness, and mitigation. Recently, some researchers developed approaches to assess Na-Tech risk based on Bayesian networks. Petrlova and Polorecka adapted the fault tree and event tree analyses into a Bayesian Network (BN) with the aim to visualise scenarios where loss of containment occurs due to the impact of a natural phenomenon on chemical industry [22]. Liu et al. defined a BN to review the organisation factors in Na -Techs due to floods and to analyse the interaction between multiple sub-systems [23]; Khakzad and van Gelder used a BN approach for the assessment of the fragility of industrial facilities exposed to floods [24]. Naderpoura and Khakzad developed a new methodology to assess the Na-Tech risk by approaching the scenario as a domino effect and using a BN [25]. None of the methods in the literature dynamically supports the emergency manager in understanding whether the available resources to manage the event that is occurring are sufficient. Only in [21] the number of people potentially involved is estimated based on an approach that discriminates the risk level in that given territory.

The purpose of this paper is to provide a quick and dynamic tool to optimise the resources available during the occurrence of a Na-Tech. The tool has been developed for NaTechs triggered by floods, but its peculiarity is that it can be easily adapted and integrated with other types of natural events. It is based on the definition of a risk-related index, which is presented in the form of a discrete variable that combines frequency and magnitude of the events and other factors contributing to the worsening of Na-Tech scenarios (georeferenced data, i.e., land-use, etc. and information about the industrial activity, i.e., typology, number of workers, etc.). The factors, contributing to the risk index, are combined within a Bayesian network, which identifies the potential causal relationships amongst them. The support of a properly designed Geographical Information System (GIS) allows the collection and processing of territorial information to be fed in the BN. A criterion for the risk index updating is also proposed and included within this BN. The paper is organised as follows:

Section 2 describes the methodology for the assessment and updating of the Na-Tech Risk index; Section 3 presents the case-study used for the application of the proposed approach; Section 4 shows the results of the study; finally, Section 5 gives some conclusions.

# 2. Materials and Methods 

### 2.1. Methodology

### 2.1.1. Assessment of Na-Tech Risk

When a natural event occurs, it will be characterised by a probability of occurrence or a return time and an intensity (hazard, Pe). The probability that an equipment is damaged by a given entity (defined as "state of damage"), conditional by the occurrence of the natural phenomenon having a certain magnitude, represents its vulnerability $(V)$. The probability of occurrence of a damage state, given a certain probability and intensity of the phenomenon, is the potential for release $\left(P_{n}\right)$ of the dangerous substance. To calculate the Na-Tech risk, the probability of release due to the impact of the natural phenomenon is needed, as well as the extent of the consequences associated with the release in order to determine the vulnerability of the receptor (damage, $D$ ). The whole accidental sequence is schematised in Figure 1. Then, the extent of the consequences is influenced by the magnitude of the release, which in turn depends on the extent of the damage to the structure and by the presence of the receptor in the impact area of the scenario.
![img-0.jpeg](img-0.jpeg)

Figure 1. Sequence of events for the development of a Na-Tech scenario.
The general approach of Figure 1 is applicable to all types of Na-Tech. Currently this procedure has been applied only to those triggered by floods. Clearly its use for another NaTech requires the definition of the hazard associated with the natural phenomenon (intensity and return time/frequency), vulnerability of the industrial equipment and extension of the impact area of the Na-Tech scenario.

### 2.1.2. Dynamic Updating of Na-Tech Risk

The probabilistic model used to derive the causal reasoning of the BN is the event tree depicted in Figure 1 for the scenario of release triggered by the natural event. Next, the escalation of the release is modelled as in the traditional risk assessment for major accident hazard establishments.

Based on the schematisation of Na-Tech escalation given in Section 2.1, a few variables allow the definition of the Na-Tech risk for establishments at major accident hazard. Such variables are the flood hazard, the vulnerability, the potential for the release of hazardous substances, the damage (consequences of the release), and the presence of people. By using these, the risk model presented above can be converted into a Bayesian Network describing the behaviour of the variable risk with the respect to the changes of the other variables.

A Bayesian network is an acyclic directed graph. It entails a set of variables represented by nodes connected each other through arcs creating a hierarchy between parent nodes

and child ones. Their relationships highlight the dependences amongst variables and allow expressing the joint probability distribution. The BN describes the behaviour of a given variable under the change of the state of a parent node. Equation (1) represents the joint probability distribution $p$ of the BN with $n$ random variables:

$$
p\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} p\left(X_{i} \mid A_{i}\right)
$$

where: $X_{1}, X_{2}, \ldots, X_{n}$ are nodes of the net; $A_{i}$ denotes parent nodes of the node $X_{i}$; and $p\left(X_{i} \mid A_{i}\right)$ is the conditional probability (i.e., the probability distribution of the child variable $X_{i}$ given an assigned distribution to its parents $A_{i}$ ).

Each node of the network, representing the risk model, has discrete states and, once the relationships have been created, criteria for attributing the conditional probabilities to the various states are defined with the aim to update the probability distribution of the Na-Tech risk for a certain geographic area (target node). This allows defining a dynamic regional index, which supports the authorities in managing Na-Tech risk.

To apply the previously mentioned concepts and execute the parameter learning in the built BN, the Counting Learning algorithm has been adopted by means of the software Netica [26].

# 2.1.3. Criteria for the Discretisation of Variables in the BN 

The definition of flood risk allowed the discretisation of the variables hazard, vulnerability, damage, and potential for the release of hazardous substances. For the purposes of this work, only the major accident hazard establishments included in the areas subject to flood have been considered.

According to the Decree Law no. 49/2010, the states of the variable hazard, which represents the probability that the establishment is subject to a certain flood scenario having a given intensity $(I)$, are represented by the combination represented in Figure 2. The flood recurrence time $(\operatorname{Tr})$ intervals are defined as in the $x$ axis according to a semi-quantitative equation [27,28], $\operatorname{Tr}$ is correlated to a combination of the extent of the flood, the water depths and the flow rate; the flood intensity is defined as in the $y$ axis and is bound to the height $(h)$ and speed $(v)$ of the water as well as to a factor (Debris Factor-DF). This factor is related to the amount and dimensions of sediment transported and the probability that debris will lead to a significantly greater hazard depending on the land-use as shown in Table 1 [29].

$$
I=h(v+0.5)+D F
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Flood hazard matrix.

Table 1. Debris factors from water flood depths, velocities, and land-uses.


Two states have been defined for the vulnerability, based on the following considerations. If specific damage curves, related to the frequency, type and magnitude of the event, are not available as well as the behaviour of the structures (i.e., [30,31]), the vulnerability is defined in the most conservative way possible, that is a value equal to 1 is assigned to the establishments included in the flood impact area and 0 for those in areas not subject to flood risk.

The distribution of the establishments having a certain potential of release of hazardous substances is given in accordance with the states described below, which are defined in a way such as to relate the probability of occurrence of a given release magnitude with the probability and intensity of the flood:

- P1: percentage of establishments included in the areas with flood hazard Pe3, i.e., including equipment that can generate a minor release of hazardous substances;
- P2: percentage of establishments included in the areas with flood hazard Pe2, i.e., including equipment that can generate a medium release of hazardous substances;
- P3: percentage of establishments included in the areas with flood hazard Pe1, i.e., including equipment that can cause a catastrophic release of hazardous substances.
The states for the variable damage have been defined based on the classification of establishments made by the Seveso Directive [32], which account for the amount of dangerous substances stored or handled and the resident population included in the impact area of the Na-Tech scenario:
- D1: lower tier establishments close to urban areas with a population density lower than 100 inhabitants per $\mathrm{km}^{2}$ (within a range of 1 km );
- D2: upper tier establishments close to urban areas with a population density lower than 100 inhabitants per $\mathrm{km}^{2}$ (within a range of 1 km );
- D3: lower tier establishments close to urban areas with a population density higher than 100 inhabitants per $\mathrm{km}^{2}$ (within a range of 1 km );
- D4: upper tier establishments close to urban areas with a population density higher than 100 inhabitants per $\mathrm{km}^{2}$ (within a range of 1 km ).
The presence of people in the impact area of the Na-Tech scenario has been grouped in categories (Cat), characterised by a given probability of presence in the territory. Only three macro-categories of no-residents have been referred to in this work, i.e., workers, students and hospitalised people. Two states have been defined for each node, which indicate the presence of the category. The category has been considered present (state 1) if at least one representative item is included within a buffer zone of 1 km surrounding the industrial site, on contrary the state 0 must be assigned.

The Na-Tech Risk Index (Rnatech) is the target node in the BN. It is represented by four states that are derived by combining the potential of release of hazardous substances and the damage as given in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Na-Tech risk matrix.

2.1.4. Criterion for the Updating of Na-Tech Risk Index

The updating of the Na-Tech risk index accounts for the presence of people (workers, students, and hospitalised people) in the buffer zone according to the rules indicated in Table 2. Since it is not possible to quantify the exact number of persons present in the impact areas, in this work some categories of centres where people are present (vulnerable items or population category) have been used to define a criterion for the risk updating. If no population category is present in the buffer area, the value of the Na-Tech risk index does not change. This criterion consists of an increase of one level of the Na-Tech risk if the items classified as Cat1 (less vulnerable) are present in the area, an increase of two levels in the case of presence of items of Cat2 category and an increase of three in the case of the presence of items belonging to the Cat3 category (the most vulnerable).

Table 2. Criterion for the increase of the index for the Na-Tech risk node.


This is justified by the assumption that emergency plans can manage a given number of people potentially involved in the emergency, which depends on the resident population, therefore the simultaneous presence of no-resident categories, such as workers, students, and hospitalised persons, might require much more resources for their protection and the emergency management.

Figure 4 gives a flow-chart that summarises all the variables involved in the elaboration of the Na-Tech risk. As shown in the figure, the methodology is composed of two parts, i.e., the assessment of the flood risk (probability of release of the hazardous substance) and the assessment of the Na-Tech risk associated with the release of the chemical in the environment. In this framework only the assessment of the hazard and risk related to the flood are defined by the Italian Decree Law no. 49/2010 [17]. The second part refers to the Decree Law no. 105/2015 [33] and the Seveso Directive [9].
![img-3.jpeg](img-3.jpeg)

Figure 4. Flow-chart of the procedure assessing the flood Na-Tech risk.

# 2.2. Data Collection and Analysis 

Data collection and analysis refer to a real case-study, which is the Po river basin which mostly falls in the Italian territory and covers about $82,788 \mathrm{~km}^{2}$. The territory includes several lakes and is crossed by hundreds of rivers and streams that flow towards the

Adriatic Sea into the Po River mouth. Over 500 Seveso establishments are located within this area and 219 are exposed to flood hazard [34]. These establishments are divided as given below and represented in Figure 5:

- 202 industries in areas Pe 1 ;
- 112 industries in areas Pe 2 and 95 of these also in Pe 1 ;
- 23 industries in areas Pe 3 and Pe 2 , whereas 20 of them in Pe 1, Pe 2 and Pe 3 .
![img-4.jpeg](img-4.jpeg)

Figure 5. Distribution of major accident hazard establishments in Pe1, Pe2 and Pe3.
According to the data extracted from the Italian Competent Authority for this basin [34], major accident hazard establishments exposed to the flood risk are $68.5 \%$ lower tier (i.e., 150 classified in the category D1), and $31.5 \%$ upper tier (i.e., 69 classified in D2). The identified risk categories are distributed as follows: $4.2 \% R 1,35.9 \% R 2,59.9 \% R 3$ and none $R 4$. No-residents, exposed to the potential Na-Tech risk, have been identified by drawing a conservative impact area (buffer zone), which is a circle with a radius of 1 km from each source of release of hazardous substances (equipment) as given in Figure 6. The software ArcGIS [35] supported this operation. The use of a circular buffer with a fixed radius could be a limit because the extension of the impact area depends on the type of substance, amount and related hazard. Given the variety of chemicals involved in the various industries, to simplify the analysis of the consequences of releases an extensive and conservative impact area has been used, which allows not underestimating the risk. A more accurate analysis will have to include more rigorously calculated damage circles.

The set of establishments at major accident hazard have been gathered from the environmental protection agencies of the regions included in the Po basin [36-42]. The shapefiles of the flood hazard maps and of the area of river basin have been obtained by the Po River basin authorities [34]. The vulnerable items have been collected from the Italian Website Opendata [43] and, when available, regional datasets have also been used to integrate the previous information. Other territorial data (administrative limits, population density, land-use, waterways, etc.) have been gathered from the Italian geoportal of the Ministry of Environment [44] and used to identify urban areas, small inhabited centers and industrial areas. A GIS has been realised with the collected data.

![img-5.jpeg](img-5.jpeg)

Figure 6. Example of buffer area including vulnerable items potentially exposed to Na-Tech risk in case of flood hazard for Pe1, Pe2 and Pe3.

Firstly, data related to the area of the basin has been filtered from the whole Italian dataset. The second step has been the selection of establishments directly exposed to the flood hazard areas. For each of them, an impact area (buffer zone) has been defined. After, by querying the georeferenced database through the spatial join tool, the vulnerable centres included in the buffer zones have been identified, classified by typology and organised according to the different hazard scenarios. Finally, the sets of information generated for each flood hazard scenario have used as input data for the Bayesian network.

The categories of people, included in the BN, group some sub-categories according to the probability of presence of individuals as given below:

- Cat1: public offices, pharmacies and clinics, cultural heritage, place of worship, etc. (presence in the period from 08:00 a.m. to 08:00 p.m.);
- Cat2: schools, university, nursery schools, college, banks (presence in the period from 09:00 a.m. to 04:00 p.m.);
- Cat3: hospitals (presence in all hours).

Table 3 summarises Seveso establishments included in each different flood hazard area. Detailed information about the presence of the category of population (Cat1, Cat2 and Cat3) in the buffer area of each establishment is given as Supplementary Materials (Table S1).

Table 3. Seveso establishments and presence of no-residents in the buffer areas.


A sensitivity analysis has been made to identify the most influencing factors (i.e., the nodes with a significant impact on the target node) by means of the Software Netica. Then, to validate the approach, the leave-k-out cross-validation technique [45,46] has been applied to verify the accuracy of the model in predicting the Na-Tech Risk index.

# 3. Results

The BN, built on the basis of the Na-Tech risk model of Section 2.1.1, is given in Figure 7. It allows estimating the updated distribution of the states of the risk index when there is a

change in the system, which causes the availability of new information that may have a positive or negative effect on it and consequently implications on risk management.
![img-6.jpeg](img-6.jpeg)

Figure 7. Implementation of the Na-Tech model in a Bayesian network.
To validate the model, firstly, the sensitivity analysis has been performed. It shows that the most influent node is potential of release ( $27.89 \%$ ), followed by hazard ( $25.77 \%$ ) and workers ( $23.57 \%$ ); the node students has only a small influence on the Na-Tech Risk index (1.92\%), while the hospitalised persons node and the damage have a low influence (respectively $0.37 \%$ and $0.12 \%$ ), the remaining node vulnerability, on the other hand, settle on influence values very close to 0 that is $0.019 \%$. Then, the cross-validation has been performed according to the following steps: (i) the list of Seveso establishments (with respect to each flood hazard) was rearranged in a random order to extract as many heterogeneous subsets as possible, (ii) these establishments were subdivided in 6 subsets, (iii) a subset at a time has been removed from the initial dataset and the Bayesian network has been trained with the remaining data. The behaviour of the model has been verified by modifying the states' distribution of the most sensitive nodes.

Figure 8a-c show the results of the cross-validation, also the standard deviation is shown on each histogram. By examining the a posteriori distributions for the target node, when an evidence is introduced at each state of the most influential nodes (i.e., potential of release, hazard and workers, the maximum MAE (mean absolute error) is $0.60 \%$ for the a priori distribution of the target node elaboration, whereas it is $0.86 \%$ for the a posteriori distribution analysis of the same node when an evidence is introduced to the node potential of release, the same value $(0.86 \%)$ is obtained if an evidence is set for the hazard node and $1.11 \%$ if it is introduced to the workers node.

To demonstrate how the BN works for the updating of the Na-Tech Risk index, the following example is given. The occurrence of the least serious and most frequent flood scenario is assumed (i.e., Pe3). Figure 9a shows the change of the distribution of states of the target node after a finding is introduced in the hazard node. A decrease in the probability of $R 4$ and $R 3$, compared with the initial situation (see Figure 8), is observed, while $R 1$ and $R 2$ increase. This means that if a natural event having a modest entity as Pe3, the probability of serious consequences due to the Na-Tech event is low, while lighter consequences are more probable. By assuming that the event occurs during a working day, it is possible to include another information in the Bayesian model, which relates to the presence of workers during the event (Figure 9b) by introducing a finding on the proper node. The Na-Tech Risk index node is updated, and it can be observed that the probability of a low-risk

index (R1) significantly decreases, while all the others increase, especially the rise of R2 is about $10 \%$.
![img-7.jpeg](img-7.jpeg)

Figure 8. Cross-validation results for Na-Tech Risk: average a priori and a posteriori probability distribution when (a) the node Release assumes $100 \%$ at each state (b) the node Hazard assumes $100 \%$ at each state and (c) the node Workers (Cat1) assumes $100 \%$ at each state.

![img-8.jpeg](img-8.jpeg)

Figure 9. Changes in the target node due to the occurrence of a flood event (a) evidence on the "hazard" node for the occurrence of an event Pe3; (b) evidence on the "workers" node for the presence of people.

This new distribution of probability of the Na-Tech Risk index means that establishments located in the Pe3 area have a medium-low level of the Na-Tech risk index due to a poor presence of vulnerable items. The $63.4 \%$ are associated with the states $R 1-R 2$ that means their buffer areas have no vulnerable items exposed to this hazard or that there is the presence of only workers (Cat1), according to criterion defined in Section 2); whereas, the $36.6 \%$ are associated with levels $R 3$ or $R 4$ that means the presence of the most vulnerable items, such as schools (Cat2) and hospitals (Cat3), in the impacted areas of the Na -Tech event.

From the point of view of the emergency management, during the occurrence of a flood event having this hazard, some useful information can be obtained, i.e., the number of involved establishments at major accident hazard, their potential accidental scenarios, the eventually involved vulnerable elements including the number of people. Based on this, the risk manager is able to evaluate if additional resources are needed to deal with

this accidental scenario. In addition, by taking into account the different period of the day, there would be a different distribution of risk levels due to the different presence of the no-resident population in the affected area.

# 4. Discussion 

The probability distribution of the Na-Tech risk index, that is obtained when a certain natural phenomenon occurs, allows assuming a rapid awareness of the potential requests for the intervention and assistance to the population within a given region and due to Na -Tech scenarios. A holistic view about criticalities in the emergency and management phases can help to optimise the overall intervention response, which can be made by a sudden identification of the most affected areas, shorter response time, more efficient use of available resources and more effective rescue interventions.

Suppose there is an alert about the possibility of occurrence a meteorological event that could cause a flood scenario classified as Pe2. Since the territory is characterised by the presence of several major accident hazard establishments, the risk manager has to face the emergency by taking into account both the flood scenario and the Na-Tech events. By focusing on the Na-Tech, the first step the manager has to perform is to set the evidence related to the expected flood scenario within the BN. According to the emergency plan, he/she can choose amongst three possible measures to reduce the potential Na-Tech risk, these can be summarised in the following:

- Measure 1: To adopt solutions that prevent the release of hazardous substances by mitigating the intensity of the impact of the natural event (e.g., stemming barriers). The action is reflected in intervening on the Potential Release node;
- Measure 2: To evacuate residents from the impact areas of the Na-Tech scenario during the alert or to reduce the amount of sustances. In this case, the measure consists in intervening on the Damage node;
- Measure 3: To limit the presence of no-resident population within the impact areas of the Na-Tech scenario, by ordering the closure of schools and offices/shops during alert and providing to move the hospitalised persons in hosting building. This solution consists of acting on Cat1, Cat2 and Cat3.
Through a quick analysis, the manager will be able to understand and choose accordingly what could be the best intervention strategy accounting for the available resources. Based on the distributions obtained for the target node from the adoption of each individual measure (Figure 10), measure 2 slightly reduces $R 4$ and increases $R 3$, however, it does not appear to be the most effective solution as the resident population is low. Measure 3 significantly reduces $R 4$ and $R 3$ and substantially raises $R 2$. Finally, measure 1 reduces $R 4$ and $R 3$ as measure 3 albeit at a lesser extent, while it raises both the lower levels. By comparing these two solutions, surely the one that acts most effectively in reducing the risk is measure 1 since, although both raise the lower levels, $R 2$ is lower by implementing measure 1 .
![img-9.jpeg](img-9.jpeg)

Figure 10. Distributions obtained for the target node from the adoption of: (a) measure 1; (b) measure 2; and (c) measure 3.

This example proves how the approach here introduced can be an effective in supporting the management of: (i) large events (i.e., event covering large areas of the territory), (ii) complex events because triggered by the interaction of a natural phenomenon with industrial facilities and (iii) variegated events as they depend on the type of people, infrastructures, etc. that may be involved.

The developments of this approach can be various, in this case only the flood hazard has been considered as a cause of industrial accidents, but it could easily be integrated with other types of natural phenomena as well as all the other categories of persons and other receptors should be added for completeness. A further development concerns the more articulated definition of the equipment vulnerability node.

# 5. Conclusions 

The main goal of this study was to provide a dynamic tool for the risk manager, to have a quick awareness about the changes of the probability distribution of the Na-Tech risk index during the occurrence of an event. The knowledge of these changes (increase or reduction) can contribute to the optimisation of the resources to be deployed in the territory for a more effective and rapid management of the emergency. Through this tool, it is not possible to know the most contributing establishments to the risk index, but global information for the territory can be obtained; therefore, its use allows a more efficient management.

This Bayesian network, consisting of a few nodes, provides a small application that lends itself very well to the inclusion of multiple elements (such as environmental variables, external factors of the establishment, internal management factors, barriers such as procedures, tools, etc.), which may have a direct or indirect impact on the distribution of risk levels and then, on the immediate emergency management of calamitous events.

Supplementary Materials: The following are available online at https://www.mdpi.com/article/10 .3390/w13141966/s1, as supporting material (Table S1).
Author Contributions: Conceptualization, G.A. and M.F.M.; methodology, G.A. and M.F.M.; software, G.A.; validation, G.A.; formal analysis, G.A.; investigation, G.A.; resources, G.A.; data curation, G.A. and M.F.M.; writing-original draft preparation, G.A.; writing-review and editing, M.F.M.; visualization, G.A.; supervision, M.F.M. Both authors have read and agreed to the published version of the manuscript.
Funding: This work has been funded by INAIL within the BRIC/2019, ID = 02 framework, project DYN-RISK.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: The data presented in this study are available in the article.
Acknowledgments: INAIL is acknowledged for the support at the begin of the research.
Conflicts of Interest: The authors declare no conflict of interest.
