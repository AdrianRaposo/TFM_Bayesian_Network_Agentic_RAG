# A Port Entry Risk Assessment Model Based on Bayesian Networks and Elements of the e-Navigation Concept 

Mario Musulin ${ }^{1 *}$, Grgo Kero ${ }^{1}$, Hrvoje Nenad Musulin ${ }^{2}$, David Brčič ${ }^{2}$<br>${ }^{1}$ Croatian Defence Academy "Dr. Franjo Tuđman", Ilica 256 b, 10000 Zagreb, Croatia, e-mail: mariomusulin2@gmail.com; grgo.kero@gmail.com<br>${ }^{2}$ University of Rijeka, Faculty of Maritime Studies, Studentska 2, 51000 Rijeka, Croatia, e-mail: hnmusulin@gmail.com; david.brcic@pfri.uniri.hr

* Corresponding author


#### Abstract

Most maritime accidents are caused by human error. To reduce these errors, increase safety, protect the marine environment, reduce the administrative burden, and optimize maritime trade, the International Maritime Organization (IMO) decided to implement a concept called e-Navigation. The term e-Navigation refers to the integration of the most modern information and communication systems, both on board and ashore. The research scope of this work is the safety of navigation of the ship during the port entrance. Particularly in this case, the elements that affect the safety of the ship during port entrance are analyzed in a case study of New York port. An adaptive model based on the Bayesian Belief Network (BBN) was created, which evaluates the decision-making elements and risk assessment for port entry. The model is adaptable in the context of the different port requirements. With the presented model, all entities (ships, shipping companies, and service providers) have insight into the estimated decision to enter the port based on the given elements. Further research needs to be continued on the issue of comparing the proposed model with similar models, and how much reliance on the model burdens or facilitates the Master's decision.


## ARTICLE INFO

## Preliminary communication

Received 27 March 2023
Accepted 6 June 2023

## Key words:

e-Navigation
Safety at Sea
Bayesian Belief Network
Port Entering

## 1 Introduction

It is a fact that the crew number on modern ships is decreasing, but their responsibility for navigation safety has not changed. As a research problem of this paper, the question of the workload of the officers on the bridge is raised, considering the large amount of information during the port entrance, as well as the possibility of supervision and assistance from the shore. According to the IMO [1], e-Navigation is the coordinated collection, integration, exchange, presentation, and analysis of all relevant maritime information on board and ashore using electronic devices to improve "mooring-to-mooring" navigation and corresponding services for safety and security at sea and protection of the marine environment. The vision of eNavigation is to improve traditional navigation by betterintegrating people and machines by exploiting their unique skills. It also tries to connect the roles of operators on the shore and seafarers on board, not only for monitoring but for better and joint decision-making $[2,3]$.

E-Navigation should not replace classic navigation but only facilitate decision-making to reduce the workload of seafarers and to make safer decisions for greater safety at sea and environmental protection. The e-Navigation system improves safety and protection at sea, protection of the marine environment, and better organization of work between the ship and the port and within the ship itself. To achieve this, it is necessary to obtain information in the shortest possible time at the request of the user in one place. To make decisions, the officer on the bridge uses various information that he receives both from the ship's devices and the shore. Ships use equipment such as Automatic Identification System (AIS), Electronic Chart Display and Information System (ECDIS), An Integrated Bridge System (IBS), Automatic Radar Plotting Aid (ARPA), Global Maritime Distress and Safety System (GMDSS), another sophisticated navigation tools. Concerning the previously stated research problem, the subject of research in this paper is the implementation of the e-Navigation concept by the IMO, and its previous projects, as well as the creation

of a risk assessment model during port entrance using BBN.

Consequently, the object of research in this paper is an integration of IMO e-Navigation projects related to ports, monitoring during the port entrance from the shore, and information that shapes decision-making and risk assessment for port entry. Hence the analysis of the elements influencing navigational safety in the port of New York case study and the creation of a model based on the BBN for entering ports in order to increase navigation safety. The Port of New York is part of this research not because of the number of accidents that have occurred, but because of the large number of restrictions that the port has. In the Introduction of the paper, the selected research area is presented and the broader context of e-Navigation is given. IMO projects related to ports are presented in Section 2 as well as relevant information about the port of New York. The rest of the paper is organized as follows: Section 3 presents the mathematical and computational background of Bayesian network modeling, and the elements that represent the general model of risk assessment during port entrance are presented. It provides the theoretical basis for the BBN used to create the model. In Section 4 through a case study of New York port, data for the container terminals of the port of New York are presented, BBN Model Verification and a Sensitivity Analysis were made. The final risk factors assessment based on the developed model is presented. Validation of the model on real case data is given in Section 5. Finally, a conclusion was reached in Section 6. with suggestions for further research.

## 2 Background and Literature Review

In 2008, at the 85th meeting of its Maritime Safety Committee (MSC), the IMO adopted a strategy for the development and implementation of e-Navigation and defined the concept of e-Navigation. With the e-Navigation Strategy Implementation Plan (SIP), the IMO gave its vision of the concept. The main objective of the e-Navigation SIP is to implement the following five e-Navigation solutions: S1: improved, harmonized, and user-friendly bridge design; S2: means for standardized and automated reporting; S3: improved reliability, resilience, and integrity of bridge equipment and navigation information; S4: integration and presentation of the available information in graphical displays received via communication equipment; and S5: improved communication of Vessel traffic service systems (VTS) Service Portfolio. The SIP estimates a 65\% reduction in navigation accidents, including collisions and groundings, for SOLAS ships [1,26]. Following IMO projects are crucial for the proper implementation of mentioned model:

- MONALISA, the general goal is to strengthen efficiency, safety, and environmental protection in maritime transport. MONALISA 2.0 is divided into four activities: 1. STM operations and tools; 2. STM definition; 3. Safer ships; 4. Safety at work [4].
- Sea Traffic Management (STM), is a concept that connects and enables real-time data exchange between ships, shipping companies, and service providers. Examples of services are route optimization services, ship-to-ship route exchange, enhanced monitoring, port call synchronization, and winter navigation [5].
- Port Collaborative Decision Making (PortCDM), as part of the MONALISA Port Collaborative Decision Making (PortCDM), is being developed to optimize port traffic. An application was developed that consists of four sub-processes, namely the approach of the ship to the port, mooring, cargo handling, and departure.
Research conducted in the Swedish port of Gothenburg, the GOT project [4], showed better synchronization and coordination of all involved stakeholders in the overall process.


# 2.2 The Port Call Process 

![img-0.jpeg](img-0.jpeg)

Figure 1 Scope of actions within the PortCDM research [6]

- Accessibility for Shipping, Efficiency Advantages, and Sustainability (ACCSEAS), the goal of the project was to improve safety, security, and environmental protection in the North Sea area by developing e-Navigation and harmonizing changes in electronic maritime information on board and ashore [7]. Information services are coordinated using the maritime security cloud (Maritime Cloud) - a secure, standardized way of accessing data by coastal and shipboard systems [8]. Some of the presented innovative solutions in the ACCSEAS project are very important for the proposed model, such as exchanging information on maritime safety and using the Maritime Cloud. It is shown later in the paper that elements for each ship stored in the Maritime Cloud could be used for each port to compare the ship's limitations with the port's limitations along with other safety information from the proposed model. The concept based on the "Single window" principle was developed by Norway in 2019, whereby a ship entering Norwegian ports sends a single document that is forwarded to all competent authorities [3].
- EFFICIENSEA (2009-2012 Baltic Sea 2015-2018 Baltic Arctic Region), the goal of this project was to enable the display of the ship's planned route for timely action and warning.

The tests carried out in the framework of this project related to:

- sending the planned route,
- display of the planned route of another ship on ECDIS,
- reduction of bureaucracy,
- sending a new corrected route from the coast (VTS) to the ship, and
- display of the new correct route on the ship's ECDIS [2, $9,25]$.

Through this project, it was shown how to increase the security of communication and exchange of information. The human factor is the leading cause of accidents in maritime traffic. Due to this fact, Machine to Machine (M2M) communication and actions that can potentially be performed by machines better than humans require more attention. New Information and communication technologies (ICT) and concepts (Internet of Things (IoT), Artificial Intelligence (AI), Cloud Computing, etc.) imply and rely heavily on M2M communication. M2M communication needs to be standardized [10]. The proposed model works on the principle of using the facts, and it is up to the Master to assess based on his acquired experience and make the final decision. In this work, through the elements of the e-Navigation system that have been previously tested through various projects, it is attempted to achieve all those elements that affect the safety of navigation are displayed through a unique model that will make it easier for the Master to make a quality decision about entering the port. Many authors dealt with the safety of the ship navi-
gation from point $A$ to point $B$ in different areas and conditions, as well as risk analysis [11-15]. A study [11] investigated risk assessment of maritime accidents on passenger's vessels in non-linear coastal navigation. In a paper [12] authors investigated the risk factor correlation of maritime traffic under Arctic sea ice status association with a Bayesian Belief Network. According to research [13], the authors propose a data-driven Bayesian network for the construction of a risk analysis model to quantify the impact of different types of maritime accidents. According to research [14], the risk assessment of navigation safety for ferries was discussed. Article [15] proposes a Bayesian network based risk analysis approach in the main route of the Maritime Silk Road to analyze its relevant maritime accidents. The crew is concentrated on the navigation to the final destination, when approaching the port there is fatigue and a drop in concentration as well as relaxation due to routine actions, therefore this paper emphasizes the necessity of increasing safety during the approach and port entrance. However, numerous accidents occurred during the port entrance.

To demonstrate the applicability of the port entering model based on BBN, a case study of the New York port was conducted. This port was chosen precisely because of its many constraining factors during the port entrance, such as demanding waterways approaching the port and restrictions on the height and draft of the ship. Additionally, the pronounced influence of external factors such as sea currents, wind, frequently reduced visibility, and large amplitudes of tides that greatly affect traffic in the port was taken into consideration. Despite numerous restrictions, it should be emphasized that the port of New York is the largest port on the east coast of the USA [19] with a significant concentration of maritime traffic and a tendency for the maritime traffic to increase.

The port is divided into six terminals as shown in Figure 2, and each terminal has its defined restrictions. Pilotage is mandatory for a specific port, as in most cases in practice, thus the mandatory items will not be part of the considered model.

Container ships were taken into account because of their strong expansion during the last decade, in which the dimensions of ships have grown significantly and their capacities have increased many times compared to previous periods. This greatly reduced the maneuverability of these types of ships and increased the influence of external factors such as wind on the extremely large outer surface, height restrictions, increased draft, as well as the width of the ships, which makes maneuvering in narrow channels difficult and at the same time increases the possibilities of "bank effect". On the other hand, the port's configuration conditions, as well as their readiness to receive new generations of container ships, mostly cannot be fully adapted at the same speed as ship dimensions. However, due to market demands, pressure is often put on the entry of such ships into the port. Reduced number

![img-1.jpeg](img-1.jpeg)

Figure 2 Terminals port of New York [20]
![img-2.jpeg](img-2.jpeg)

Figure 3 New York Harbor Map [23]
of crew, various savings, increasing requirements and maritime regulations, and crew fatigue, caused recent maritime accidents precisely on these types of ships when approaching the port and passing through the straits. In the given model, it is understood that the ship's equipment enables the ship's berthing, as well as that the ship thrusters help with the maneuver, and that ship's mooring is prepared.

## 3 Methodology

In this paper, the Bayesian Belief Network graphical network based on probability and uncertainty was used. Probability theory is primarily concerned with practical problems and represents the theoretical basis of statistics.

Bayes' theorem justifies a way of thinking that states that the truth of a theory is confirmed by new evidence. It

is a conditional probability, the probability that one assumption is true provided that the other assumption is true. The fundamental goal of Bayes' theorem is to formalize information about how one event can help in understanding another. Therefore, to find the probability of an earlier event provided that a later event has occurred, a BBN enables it to operate with incomplete data and conclude reasoning from uncertain knowledge or information. BBN is widely used in various problems such as decision-making, scenario analysis, and probability prediction $[16,17]$.

The conditional independence and joint probability distribution are the basic rules of the BBN and can be expressed by formulas (1) and (2):
$\mathrm{P}(\mathrm{V} 1, \mathrm{~V} 2, \ldots, \mathrm{Vk} / \mathrm{v})=\prod_{1}^{k} \mathrm{P}(\mathrm{V} / \mathrm{v}) \mathrm{i}(=1,2, \ldots, \mathrm{k})$
$P(V 1, V 2, \ldots, V k)=\prod_{1}^{k} P(V i /$ Parent Vi$) \mathrm{i}(=1,2 \ldots, k)$
where Vi represents the variable, k is the number of the variables, $\mathrm{P}(\mathrm{V} 1, \mathrm{~V} 2, \ldots, \mathrm{Vk} / \mathrm{v})$ is the conditional probability function, $\mathrm{P}(\mathrm{V} 1, \mathrm{~V} 2, \ldots, \mathrm{Vk})$ is the joint probability function, Parent (Vi) represents the parent nodes of Vi [15].

For the construction of BBN, the first requirement is to define the problem domain through the identification of the relevant set of variables that defines the modeled problem. Further, the relationships between the variables are established to define the graphical structure of the model. In the next step, they assign the states of the variables and their initial probabilities $[11,16]$.

In this chapter, a division of elements whose interdependency affects the decision-making process according to different criteria and using the BBN was made. Figure 4 shows all the elements that are important for decisionmaking for the port entrance as well as choosing a terminal for mooring the ship concerning the given parameters. It is assumed that ports are previously defined for certain classes of ships. For this research, the classes of ships that have previously entered the port to load/unload cargo were defined. Therefore, the characteristics of the ship correspond to the conditions and configuration of the port, and it is not necessary to analyze that aspect, because they are known parameters to determine the risk analysis. The basic elements of the ship are indicated in Figure 4, assuming that the officer on the bridge knows
![img-3.jpeg](img-3.jpeg)

Figure 4 The elements of the general model of decision-making on entering the port

the maneuvering abilities of the ship. Further, the elements that define terminal characteristics and hydrometeorological conditions are shown. All these elements should be clearly defined and displayed in the maritime security cloud during ship entrance in port. The elements that define the ship as a result of the ship's conditions are defined by the Master on board, while the elements of the terminal are defined by the port authorities. Elements representing hydrometeorological conditions would be obtained from various sensors located in the port and devices already installed on the ship, as shown in the already tested e-Navigation projects. The items from the model listed in Figure 4 are defined based on the studied and processed literature $[11,18]$ and will be used later in the proposed model.

## 4 BBN Model Verification

This model does not consider the psychophysical state of the operator, but only the factual parameters that influence the analysis of the risk of navigation as previously stated. Each port is defined by its characteristics, hence it is most important to recognize and define them, thus Table 1. was created based on processed literature and publicly available data for the specified port [21, 22] and based on the experience of Masters who entered the specified port. It represents the general framework used by seafarers during the port entrance. Each of the characteristics is divided into mutually exclusive sub-characteristics. Eight characteristics of the distribution (A, B, C, D, E, F,

G, H) were proposed, which were used when creating the model shown in Figures 5, 6 and 7. The GeNle Academic [27] program was used to create the proposed model. Once vessel size has been selected, adjustment is done for specific nodes which represent the vessel's actual loading condition and external factors stated in accordance with the proposed distribution described in Table 1. For this purpose, 2300 TEU, 8000 TEU, and 16000 TEU vessels are used. As described in Figure 2, the port of New York has 6 different container terminals and each has its own limitations in respect of depth, height, and cargo gear capabilities. By selecting vessel size and loading condition, the model automatically provides a risk assessment of entering each available terminal according to the terminal's restrictions, while by changing external factors, the model calculates if port entering is safe or not. Terminal selection mainly belongs to port management in terms of berth availability, but the purpose of the model is to calculate the probability of docking at each terminal so that after receiving the terminal confirmation from the port, the safety of entering the port can be checked in the model. Testing results are given for the following conditions:

- Port entering with the empty condition and favorable external factors Figure 5.
- Port entering with light condition and unfavorable external factors Figure 6.
- Port entering with heavy condition and unfavorable external factors Figure 7.

Table 1 Proposed distribution of characteristics of the port of New New York [21, 22]


![img-4.jpeg](img-4.jpeg)

Figure 5 A model for New York port study case 1st example (work in GeNIe Academic [27])
Source: Authors
![img-5.jpeg](img-5.jpeg)

Figure 6 A model for New York port study case 2nd example
Source: Authors
![img-6.jpeg](img-6.jpeg)

Figure 7 A model for New York port study case 3rd example

It can be observed that the safety of port entering is highly sensitive to factors that belong to the vessel's loading condition as well as the size of the vessel. As shown in Figure 5, entering to port is not recommended despite favorable weather and empty condition due to height restrictions in the port. In Figure 6, despite unfavorable external factors, the safety margin for port entering can still be maintained by requesting additional tugs, while port entering isn't recommended in combination with unfavorable weather factors and heavy loaded vessels as shown in Figure 7. However, some external factors can be crucial for approval of entering the port despite vessels condition, for example in case of dense fog and poor visibility incoming traffic will be suspended till visibility improves.

## Model Sensitivity Analysis

Sensitivity analysis is a widely used method to analyze the sensitivity of related variables to identify the influencing factors that can reduce the uncertainty of the target factor [28]. All the formulas for sensitivity analysis are calculated with the software package GeNIe Academic [27]. The sensitivity analysis confirms whether the model assumes the correct behavior of the modeled system, i.e. checking the sensitivity of the model shows that the model is sensitive to parameters and scenarios to which the observed system should be sensitive. An example of the sensitivity analysis is shown in Figures 8 and 9. The target nodes are: "SAFE" and "NOT RECOMMENDED". The sensitivity diagram in Figure 8 shows the most sensitive parameters for
![img-7.jpeg](img-7.jpeg)

Figure 8 Sensitivity diagram for node "NOT RECOMMENDED"
Source: Authors
![img-8.jpeg](img-8.jpeg)

Figure 9 Sensitivity diagram for node "SAFE"

selected states of the selected node. They are ranked from most sensitive to least sensitive. With the help of the divider, it is possible to determine the percentage of change in all parameters. The horizontal axis shows the absolute change in posterior probability when all parameters are changed by a certain percentage. Positive derivation values are shown in red-green, and negative derivations are shown in green-red. This kind of display enables quick identification of the state of "target nodes" that will increase or decrease their posterior when the value of the parameter for which the sensitivity test is made increases.

As shown in Figure 8, the diagram of sensitivity to the risk of entering the port, the nodes "AIR DRAFT" and "VISIBILITY" have the highest sensitivity for the selected ship class, then "EXTERNAL FACTORS" and then the others as shown.

Figure 9 the sensitivity diagram shows the sensitivity analysis for a specific case when all conditions for entering the port are favorable and the final result is "SAFE". For this case, the ship class 2300 TEU was selected, and the sensitivity diagram in this case has the highest sensitivity node "EXTERNAL FACTORS", this sensitivity changes depending on the selection of the number of tugs. In this way,
the Master can reduce the risk and influence the node "EXTERNAL FACTORS" by increasing the number of tugs.

## 5 BBN Model Validation

The developed model is validated against real world case: On May 17, 2018, around 5 p.m. a very large container (VLC) ship was involved in an accident at the New York port, Newark. The data [29] is about container ship TUCAPEL, IMO 9569970, dwt 94707, capacity 8000 TEU, built in 2012, flag Liberia (LOA 300 m , width 46 m , draft 12.8 m ) According to [30, 31] the ship broke the mooring lines during the active arrival at the mooring. The ship was forced to drop anchor in order to help arrest movement and was subsequently stabilized and secured with the assistance of four tugs.

The node "EXTERNAL FACTORS" was very bad (86\%), the weather worsened rapidly, and thus the node "VISIBILITY", but according to the forecast, visibility was good before the port entering maneuver. Port entering was not recommended according to the model ( $80 \%$ ). We can only assume that the intention was to berth before the storms. As shown in Figure 10, if the developed BBN model had

Table 2 Newark weather history for May 15, 2018 [32, 33].


![img-9.jpeg](img-9.jpeg)

Figure 10 Model validation of maritime accident for container ship "TUCAPEL"

been used immediately before the accident, according to the available evidence, its response would have issued a warning, which is in line with one of the goals of developing the model.

## 6 Conclusion

Based on all available information, the authors propose the implementation of a risk assessment model for port entering based on BBN and elements of the e-Navigation concept. The model integrates previous IMO projects based on the concept of e-Navigation and port entry risk analysis. As mentioned earlier, due to market demands, the Master and crew are often under pressure to enter the port despite the fact that the weather conditions and the terminal proposed by the port authority are not suitable for conducting safe port entry and docking. As well due to the constant growth of the ships, and the implementation of new technologies and systems, the crew is often overwhelmed with various data and information in combination with fatigue and stress, which causes a potential loss of control and lack of situational awareness. The purpose of the model would be to establish decision-making support for the ship's command where all information and results would be available in one place to improve situational awareness based on the state of the ship's embarkation and real external factors, providing a clear risk assessment of refusals or approvals for entering the port.

According to the above, we can establish the fact that despite all the elements of the system offered by e-Navigation and the proposed model to facilitate the Master's decision, the Master still has the discretionary right to decide based on his experience at a certain moment.

Consequently, stakeholders would have an integrated system that collects, analyzes, exchanges and presents all maritime information for entering the port to protect the safety of the ship and the marine environment.

The authors emphasize that using this model would reduce human error. Moreover, by monitoring the situation from the coast in real-time with the possibility of action, potential errors would be reduced to the smallest extent. It is very important that the presented model can be applied and adapted for each port.

The authors suggest further research in model comparison to similar proposed models for entering the port.

Funding: The research presented in the manuscript did not receive any external funding.

Authors Contributions: Conceptualization, M.M. and D.B.; methodology, M.M., G.K., and H.N.M.; validation, M.M, and D.B.; investigation, M.M. and H.N.M.; resources, M.M.; writing - original draft preparation, M.M.; writing - review and editing, D.B.; visualization, M.M.; supervision, D.B. All authors have read and agreed to the published version of the manuscript.
