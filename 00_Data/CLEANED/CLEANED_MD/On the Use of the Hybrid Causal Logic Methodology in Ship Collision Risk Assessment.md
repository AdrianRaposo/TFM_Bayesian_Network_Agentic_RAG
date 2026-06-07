Article

# On the Use of the Hybrid Causal Logic Methodology in Ship Collision Risk Assessment 

Tengfei Wang ${ }^{1,2,3}$ (D) Qing Wu ${ }^{1}$, Mihai A. Diaconeasa ${ }^{4, *}$ (D) , Xinping Yan ${ }^{2,3}$ and Ali Mosleh ${ }^{5}$<br>1 School of Logistics Engineering, Wuhan University of Technology, Wuhan 430063, China; wangtengfei@whut.edu.cn (T.W.); wq@whut.edu.cn (Q.W.)<br>2 Intelligent Transport Systems Research Center, Wuhan University of Technology, Wuhan 430063, China; xpyan@whut.edu.cn<br>3 National Engineering Research Center of Water Transport Safety (WTSC), Wuhan 430063, China<br>4 Department of Nuclear Engineering, North Carolina State University, Raleigh, NC 27695, USA<br>5 B. John Garrick Institute for the Risk Sciences, University of California Los Angeles, Los Angeles, CA 90095, USA; mosleh@ucla.edu<br>* Correspondence: madiacon@ncsu.edu; Tel.: +1-(919)-515-3768

check for
Received: 15 May 2020; Accepted: 26 June 2020; Published: 30 June 2020
updates


#### Abstract

A ship collision accident is one of the most dangerous and common types of maritime accidents. Traditional probabilistic risk assessment (PRA) of ship collision accidents is a methodology that can be adopted to ensure maritime safety. Nevertheless, a need for better approaches to model human behavior, such as risk identification, communication, and decision-making, has been identified. Such advanced PRA methods require a more explicit way of taking human factors into consideration than the traditional risk assessment methods. Hybrid causal logic (HCL) is an advanced PRA method due to its unique three-level framework that includes event sequence diagrams, fault trees, and Bayesian networks, which makes it suitable for modeling human behavior that is important to ship collision accidents. This paper discusses the applicability of the HCL methodology for the ship collision accident. Firstly, the event sequences of typical ship collision accidents are summarized based on the study of 50 accident investigation reports. Then, fault trees for mechanical failure events and the Bayesian networks for human error events are constructed to analyze the events in a structured way at a more detailed level. Finally, the three main end-state types of ship collision avoidance scenario have been quantified. The result of the probability of a ship collision accident is verified by estimating the annual frequency of collision accidents in the Singapore Strait. Comparing with the historical data, the estimation results are quite near to the real case. By taking advantage of the HCL methodology, the modeling of ship collision scenarios can be carried out at a deep logical level. At the same time, it is possible to combine a detailed analysis of various primary events with a comprehensive analysis at the system level.


Keywords: maritime safety; ship collision accidents; hybrid causal logic methodology; accident investigation reports

## 1. Introduction

As one of the main types of maritime accidents, ship collision accidents often result in catastrophic consequences, for instance casualties [1], huge property losses and environmental pollution [2,3]. Therefore, the research concerning ship collision accidents has been one of the hottest academic fields for decades. The prediction and prevention of ship collision accidents are the aims of ship collision research, and the risk-based approach is one of the main topics. Risk-based research has provided valuable information for decision-support in all stages of ship collision avoidance, including research and

development of navigation equipment [4,5], risk identification [6], anti-collision decision-making [7], and operation [8].

With the deepening research on ship collision accidents, various methods are presented to try to predict collision accidents in advance, and then gave reasonable suggestions to reduce collision risk. Most of the onboard navigation equipment already has primary function of collision alart by calculating the closest point of approach (CPA). CPA, including the time to the CPA (TCPA) and distance to the CPA (DCPA), is a well-used method with a clear principle and simple calculation in ship collision risk assessment. Perera et al. [9] presented a fuzzy logic CA decision support system for two ships encounter situation based on CPA, and then developed it into a collision risk detection and quantification system in [10]. These methods based on CPA can be used as a good measure of risk, but hard to be used to reveal the evolution mechanism and internal logic of ship collision accident. A major problem of ship collision research is that the process of sailing is an activity with very high degree of freedom and large uncertainty. Using a system risk approach to study the consequences of collisions accidents between oil cargos, Floris et al. [11] found that the uncertainties of the scenario made a more accurate physical model impracticable. A large part of this uncertainty comes from human and organizational factors (HOFs). Some researchers have realized the decisive role of human factors in the process of ship collision avoidance [12], and quantitatively described human subjective intention in the methods [13]. However, this still does not reveal the interaction between HOFs and other factors and the influence of HOFs on the results.

Ship domain is another comprehensive model for describing ship collision risk [14] by proposing a special region around the sailing ship to characterize the collision risk in an encounter situation. Since ship domain can be seen as a two-dimensional representation of a risk situation, it is often used as a collision risk index [15] and risk level [16] to estimate the maritime risk in waterway risk analysis. Velocity obstacle algorithm [17] is another well used two dimensional risk representation model with prediction function. These risk-based description models based on geometric methods provide an integrated and rational framework of ship collision study to facilitate maritime safety analysis, and also convenient to introduce new risk-based models and decision-making methods to address uncertainty. However, these methods cannot analyse the ship collision scenario from the accident evolution aspect. At the same time, it does not have the capability to model mechanical performance and HOFs.

The Bayesian network (BN) model for modeling HOFs and other uncertain factors is also a common method for ship risk analysis. Goerlandt et al. [18] presented a maritime risk assessment framework, which applying BN for probabilistic risk quantification. Fan et al. [19] proposed a data-driven BN framework which can incorporate the HOFs into maritime accident analysis. These studies fully recognize the importance of uncertainties in maritime accidents, and try to model and analyze from different aspects. However, the development of maritime accidents is a dynamic process, all factors are changing with time. No matter the consequences of the accident, the development of the entire scenario follows a natural and fixed logical sequence. Ship collision accidents also have the characteristic of being able to be captured by only a few general types of scenarios since ships need to be operated in a strictly regulated environment. For instance, the anti-collision decision-making must be the subsequent event of risk identification and confirmation. BN does not have the ability to analyze the sequence of events.

To bridge these gaps, or at least to reduce them. An attempt is made to perform the ship collision accident risk analysis from all the three points by applying the hybrid causal logic (HCL) [20] methodology. The unique three-layer analysis structure of HCL makes this possible.

The HCL methodology is developed based on the principle of using appropriate methods to analyze the risks of different elements of the system. The technical system operated by an organization of people is one of the main applications of the HCL modeling and analysis, for instance, nuclear power plants, offshore operating platforms, and high-speed trains. Any assessment using the HCL methodology involves the development of a combination of three layers of models: event sequence diagrams (ESD), fault trees (FT), and Bayesian networks (BNs) [21]. Within this framework, the ship collision scenarios

were modeled such that both the identification and decision-making activities of the own ship and target ship are explicitly captured. The first step was to build a general ESD describing the high-level collision avoidance scenarios. In the next step, FTs and BNs were constructed to explicitly model the events defined in the ESD. It should be noted that, depending on the type of ship involved in each event, the FTs and BNs of the same events in the ESD will be different. This is an important aspect of the assessment as the HCL methodology allows us to model the same high-level scenarios in the ESD layer with specific details in the FT and BN layers for each type of ship. Next, logically complete HCL models were built by linking the FTs and BNs to their corresponding events in the ESDs. Finally, the probabilistic data (e.g., conditional event probabilities) was added to the HCL models in order to run the quantification of scenario probabilities.

The remainder of the paper is organized as follows: Section 2 gives a short introduction of the HCL methodology and its software implementation. In Section 3, the ESD of ship collision scenarios is built using the general rules of collision avoidance and accident reports. In Section 4, the FTs and BNs of the events in ESD are determined. The results of risk assessment of ship collision accident scenarios are shown in Section 5. Finally, some discussions and conclusions are given in Section 6.

# 2. Overview of the HCL Methodology 

In practice, the Boolean logic-based probabilistic risk assessment (PRA) methods such as FTs and ESDs or event trees (ETs) are widely used in analyzing risks of complex systems, while the human and organizational causal factors are usually modeled with BNs. The HCL methodology combines these to handle more complex scenarios. It is designed for socio-technical systems in which potential events such as equipment failures or human errors may lead to major accidents. These potential challenging events are found in many diverse industries (e.g., the transportation systems [22], offshore industries [23,24], and nuclear power [25]), however they share common characteristics like non-deterministic (i.e., soft) causal factors and lack of accident data which lead to the difficulty in appropriate modeling. To construct and quantify the HCL models, the Trilith software platform was used.

### 2.1. HCL Modeling Concept and Algorithm Overview

As depicted in Figure 1, the HCL methodology has an architecture of three layers to model each part with the most appropriate method. In this multi-layered model, ESDs form the first layer, followed by FTs and BNs.

ESDs capture all the possible end states and the related sequences of intermediate events emerging from the same initiating event, just like the ETs or flowcharts. Furthermore, intermediate events in ESDs include decision nodes to model the active sequence divergence according to, for example, the state of the systems or decision-making events. In the HCL methodology, ESDs make it possible to visualize the inner logic, dependencies, and time series of the causal factors of hazards or accidents, thereby enabling the causes of the different situations of the system to be analyzed intuitively. As some of the ESD events (e.g., mechanical failures) can be essentially decomposed into a set of physical elements, FTs are designed to create more detailed models of these kinds of events. The initiating or intermediate events of an ESD can be linked to the top event of an FT. The BN layer is the bottom layer in HCL methodology, and it is used to model the causal relationships explicitly. In an HCL diagram, the BNs nodes can be linked to any basic events in the FTs and any initial or intermediate events in the ESDs. This provides a practical and considerate way to model a complex system by building a three-layer logic structure based on the HCL methodology.

The HCL algorithm drives the quantification in the HCL methodology; the data required can be either point estimates or probability distributions of the events or nodes. The ESDs and FTs are converted into reduced ordered binary decision diagrams (ROBDDs) to obtain an exact solution [26]. Compared to top-down modeling procedure, the computing process is bottom-up. The results of the probability distributions of the ROBBDs are linked with the calculated results of the nodes in BNs. By determining the necessary parameters and state sets, all the states and details of the system modeled

by HCL can be calculated, and then the risks can be obtained with the HCL-based risk management metric functions.

As the BNs in HCL include so many causal factors and may impact the whole model, the BNs can be no longer converted into binary decision diagrams (BDDs) in HCL methodology. A hybrid BDD/BN solution algorithm was developed by Groen and Mosleh [21] and Wang [20], and was further improved in a follow-up work by Diaconeasa [25].
![img-0.jpeg](img-0.jpeg)

Figure 1. The Structure of the HCL model.

# 2.2. HCL-Based Risk Management Metrics 

The HCL algorithms not only calculate the cut sets of each end state of the risk scenarios and the probability of occurrence of these events, but also determine the factors which contribute most to the risks of the scenarios (i.e., importance measures) and the risks and performance indicators over

time [27]. These functions make the HCL a decision supporting method more than a risk analysis tool since it can be used for risk-informed design too.

1. Importance measures. In most cases, the primary aim of risk analysis is to find the factors which contribute most significantly to the end state of concern or the whole risk scenario. In the HCL methodology, all the importance measures of the system hazards and the influence of the elements can be identified quantitatively. The HCL-based importance measures have four forms to analyze the different aspects of the events: the risk achievement worth (RAW), the diagnostic importance measure, the marginal importance measure, and the risk reduction worth (RRW).
(1) RAW or risk increase factor quantifies the change of the failure probability of a system given the failure of a component [28]. RAW can quantify the change of the failure probability of a system given the failure of a component. RAW is an important reference for system improvement. If the RAW of a component is close to 1 , then its improvement will have little effect on the overall system.
(2) The diagnostic (or Fussell-Vesely) importance measure is the impact of components on the failure of the entire system [29]. The Fussell-Vesely importance measure quantifies the fractional decrease in the total risk level given the component is perfectly reliable.

RAW and Fussell-Vesely importance measure will be used in Section 6 to analyze the risk importance of basic events.
2. Risk indicators or safety monitoring: It is essential in a PRA methodology to monitor the states of the system and to track alteration in risk over time. This analysis is commonly done by specifying an event as a risk indicator and analyzing the 'frequency' and the 'risk weight' of this event. In HCL methodology, the range of risk indicator is expanded to the Pivotal Event (PE) in ESDs, gates and basic events in FTs, or variable state in BNs.
3. Precursor analysis and hazard ranking: In the HCL model, any event in the ESDs, FTs or BNs can be regarded as a precursor to risk. For instance, the event of 'human decision error' during navigation is a precursor to the undesired end state 'ship collision accident.' An interesting analysis can look at the relationship between these precursors and an undesirable end state, as well as how to avoid the accident even if these precursors happen. These questions can be answered by obtaining the cut sets and calculating the conditional probability of the end states given certain precursor events happening.

The Windows-only Trilith software platform was developed at the University of Maryland and expanded at the University of California, Los Angeles. The platform uses a cross-platform computational engine that has also been packaged into the integrated risk management system (IRIS) with different user interfaces and specific models developed for particular users, such as the United States Federal Aviation Administration. A cross-compatible command-line too named hybrid causal logic analyzer (HCLA) is also available for quantifying any time-dependent HCL model with uncertainties. Its main features cover risk model building functions, analysis tools, and other applications. The risk model building functions enable the user to construct and analyze HCL models with little or no training. Once the HCL model has been built, the analysis tools become available to output the minimal cut sets of every end state in ESDs, the sub-model results, and importance measures by setting a specific end state or category. Trilith also offers other advanced analysis features and visualization functions.

# 2.3. Methodological Framework 

In this paper, a typical HCL model is developed for the ship collision risk analyses of general scenarios. The analysis procedure used in this section is a standard application of the HCL methodology accompanied by experience from traditional maritime risk analysis methods. The HCL methodology can be adopted for the ship collision accident by going through the following steps:
(1) Define the risk influencing factors (RIF) and causal relationships of all the possible accident event sequences and form the ESD with the relevant intermediate events.
(2) Model the events related to hardware failures by performing system decompositions using FTs.
(3) Model the events that are influenced by human factors or other factors at a more detailed level by using BNs.

(4) Assign relevant event probabilities in the ESDs and FTs, and the Conditional Probability Tables (CPTs) in the BNs.
(5) Calculate the risk results.

The general strategy is to carry out the first four phases at one time and quantify the same ESD, FTs, and BNs for different conditions in phase 5 and 6. Examples of such conditions could be normal operation or emergency activities. Finally, the state of the RIFs for each operational end state can be evaluated and assigned.

In step 1, the RIFs and causal relationships are described, and the ESD is constructed with the relevant basic events following the logic of the evolution of accident. For quantification, the events in the ESD can either be given a probability or linked to an FT top event or BN node. Extensive domain specific knowledge of the ship collision accidents is required during the process of the description of the causal relationships. In most cases, extensive experience from different disciplines is necessary to obtain all the necessary information.

In steps 2 and 3, several RIFs in the ESD are analyzed at a more detailed level in FTs and BNs. Graphically, an ESD event is directly linked to the top gate of an FT and can be connected to any node in a BN. A basic event in a FT can also be connected to any BN node. Then, the fourth step is the assignment of the probabilities of the ESDs and FTs, and CPTs of the BNs. The HCL algorithms [28] are designed to capture all these dependencies explicitly.

The final step is the calculation of the results, including the events in ESD, FTs and the nodes in BNs. The algorithm of combining the FTs and BNs with ESDs [28] is an important part of the HCL methodology, and the algorithms guarantee a high computational efficiency for analyzing complex and large HCL models. It also should be noted that as the BNs are linked to the ESDs/FTs models, the ESD, FTs, and BNs cannot be quantified separately as the dependencies are modeled explicitly. In this paper, several HCL models are developed using the Trilith software platform.

# 3. Information Sources and Modeling Procedure 

### 3.1. Accident Reports

In the study presented here, 50 ship collision accidents involving more than 100 vessels based on publicly available maritime accident reports were analyzed. Based on anticipated operational practice encounter situation of unmanned ships, only the events up to collision accidents were selected and analyzed. Although the immediate responses to collision accidents are regarded as vital to reducing the magnitude of consequences, the industry has not yet reached a consensus on how the unmanned ships would react immediately following the accident occurrence. Thus, the other phases of the collision accidents (e.g., secondary disasters) and their consequences were not considered in this work.

The accidents reports were collected from the following organizations: National Transportation Safety Board (USA)(10 cases) [30], Danish Maritime Accident Investigation Board (11 cases) [31], Marine Accident Investigation Branch (UK) (15 cases) [32], Japan Transport Safety Board (JTSB) (nine cases) [33], Accident Investigation Board Norway (AIBN) (two cases) [34], and Marine Safety Investigation Unit, Malta (three cases) [35]. The location information of the accidents can be seen in Figure 2.

All the information of the chosen accident is listed in Appendix A. In the accidents analyzed in this paper, 36 lives were lost, two lives were missed, and more than 13 people were injured. At least one ship was destroyed or heavily damaged per accident, and 10 vessels sank or were totally loss after collision. Several cases resulted in severe environmental damage, for instance, 12,500 L of diesel oil and 5500 L of lubricating oil leaked after the collision between cargo vessel MV SPRING BOK and liquid petroleum gas (LPG) tanker MV GAS ARCTIC in 24 March 2012 at 6 nautical mile (nm) south of Dungeness, UK (Appendix A). These accidents involved all kinds of normal ships, including cargo ships, Liquefied Natural Gas (LNG) ships, tanker, bulk carrier, vehicle carrier, and so on. Although fishing vessels were also mentioned in some of the investigation reports, the requirements

and responsibilities of fishing vessels in International Regulations for Preventing Collisions at Sea (COLREGs) are different from those of the above-mentioned vessels. Therefore, this paper mainly focuses on the above-mentioned vessels, except fishing vessels. Most of the accidents happened in years 2010 through 2017 in various geographical regions around the world, include Asian, European, and North American waters. No particular association between ship age and the likelihood to become involved in the maritime accident has been observed.
![img-1.jpeg](img-1.jpeg)

Figure 2. Regions of accidents considered in analysis.

# 3.2. Modeling Approach 

The methodology of ESD analysis in HCL is different from the traditional post-accident analysis. The ESD and its associated FTs and BNs quantitively evaluates the impact of various causal factors on the particular event at a very detailed level. Thus, the logical sequence of events coming out historical accidents defines the basis for building the ESD.

In addition, unlike the application of HCL in other fields (e.g., the offshore oil and gas industry, the high-speed railway, and the aircraft risk analysis [36]), both ships involved in a ship collision accident are liable subjects [37]. Even though there are different responsibilities according to ships' maneuverability in COLREGs (Rule 18: Responsibilities between Vessels), essentially, both vessels involved are entirely independent actors in a ship collision accident. They have no affiliation relationships and neither belongs to a higher-level system. Furthermore, in most of the ship collision investigations, both ships are power-driven vessels, which means that they have the same capability to avoid collisions independently. There are two approaches for constructing HCL models for ship collision accidents under these conditions: modeling the events of both ships at the same time (namely multi-subject modeling) or choosing one ship as the main perspective. The traditional analysis of ship collision accidents generally engages the retrospective review analysis of every detail of the accident, which is a typical multi-subject analysis. While no matter which approach is adopted, the primary process of ship collision avoidance is the same. The main difference between these two approaches is that the ESD constructed using the first approach will exhibit a high degree of structural symmetry and dependency. However, the sequence structure of the ESD from the perspective of either of the ships is the same as the ESD used the second approach, as is depicted in Figure 3. The node NO. and related details are listed in Table 1. Another problem of modeling both sides at the same time is the structural redundancy and increased computational complexity of the entire HCL model. However, there are also several problems if the ESD is construction from the perspective of only one ship. For instance, the unbalanced perspectives during analysis, how to select the main perspective, how to design the status and behavior of another ship, etc.


![img-2.jpeg](img-2.jpeg)

Figure 3. Multi-subject modeling and single-subject modeling of Ship collision accident.
Although the modeling approach of single subject is different from the traditional concept of ship collision accident analysis based on data and consequence, it is more compatible with the actual development of accidents. First of all, all actions done by the ships involved are modeled from their point of view. Only when communicating with the target ship (TS) can the TS affect the own ship (OS). Secondly, the decision of the OS always tends to trust the information obtained by themselves, although this information may be limited or even false. Only when the OS fails the recognition and confirmation of risks and does not have enough opportunities to avoid collision normally, will it rely on TS to take action to avoid collision or access the emergency procedures directly. Therefore, the modeling approach from a single subject point of view can replicate more realistic ship collision accident activities such as distributed decision-making and limited information acquisition. It can also highlight the OS's position in ship collision accidents and facilitate a more efficient quantification analysis.

It is an important issue to decide which ship to be the OS in a single subject ESD modeling. In these scenarios, the logical sequence of accident development (i.e., the structure of ESD), the functional decomposition of systems (i.e., the structure of FTs), and the interdependence between the causal factors (i.e., the structure of BNs) are the same for both ships involved. Moreover, all the parameters of these models come from case report analysis, empirical data, and previous studies.

# 4. HCL Model for Ship Collision Risk Analyses of the Conventional Scenario 

### 4.1. ESD Constructions of Ship Collision Scenario

In this section, the ship collision accident is modeled using the HCL methodology. The initiating event occurs when the closest point of approach (CPA) is less than a predefined minimum safe distance and time (i.e., CPA alarm). The accident case focuses on the initiating event 'CPA alarm,' which is a start state for the ship collision risk [38].

After a detailed analysis of the accidents in Section 3.1, the general logical events sequence of ship collision accidents can be concluded in Figure 4, where the red squares indicate that the events are the main causes of the accidents, and the orange squares indicate that the events are one of the causes of the accidents. The ESD in Figure 5 illustrates the following event sequences caused by the initiating event, which is a graphical representation for all the possible accident scenarios.

The events and related details are listed in Table 1. The whole ESD can be divided into three main parts: the collision risk identification and confirmation, OS's decision-making and communication with the TS, and OS's response action under different conditions. There are eleven end states following

the various response actions and systems performance. The next few paragraphs present and discuss how to make an HCL model step by step, following the five steps given in Section 2.3.
![img-3.jpeg](img-3.jpeg)

Figure 4. Statistics of accidents based on accident event sequence logical.
![img-4.jpeg](img-4.jpeg)

Figure 5. ESD of M-M ship collision scenario.
In the first step the ESD is constructed by defining the RIFs and causal relationships. There are three main logic paths in the ESD after the collision risk identification (PE 1\2\3):
(1) The scenarios with successful communication with TS: This will lead to a collaborative effort between both sides for avoiding a collision (PE 4\5\6\7, End 1\2\3);
(2) The scenarios with failed communication with TS: This will lead to a unilateral effort of collision avoidance (PE 4\8\9, End 4\5\6);
(3) The scenarios under emergency conditions: Since it is under emergency conditions, both ships do not have time to communicate with each other and only take recovery measures based on their assessment alone (PE 10\11\12, End 7\8\9\10).

The PE 13 is more different than the other events. As discussed in Section 3.2, a single point of view modeling approach is adopted in this paper and the PE 13 is the embodiment of this idea. During the process of identifying and reacting to a collision course, all crews of both involved ships tend to rely on their own perceived context to make decisions. Only when they do not recognize the risk can they rely on TS's correct perception and decision-making. In this case, the two ships can be regarded as trying to avoid a collision independently, just like the scenarios with failed communication with TS (PE 4\8\9, End 4). For this reason, the probability of PE 13 is set to be equal to the probability of End State 4, as is depicted in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Method of determining the TS Measures (PE 13).

# 4.2. FTs Modeling of the Conventional Scenario 

In the second step, the hardware related PEs (PE 1\7\9\12) of the ESD are further modeled by performing a functional decomposition and, subsequently, constructing FTs. These events are OS collision alarm (PE 1), OS propulsion and steering (PE 7), OS propulsion and steering with failed TS communication (PE 9), and OS propulsion and steering for emergency (PE 12). As the conventional ship navigation system is mainly constructed by Automatic Radar Plotting Aid (ARPA) and Automatic Identification System (AIS), the PE1 (OS Collision Alarm) is further modeled by the FT of alarm failure, which is shown in Figure 7.

PE 7, PE 9, and PE 12 of the ESD model are linked with the FT model of mechanical failure, which describes the mechanical failure of ship's high-level manoeuvre performance of conventional ships. According to the accident reports reviewed, the PE of OS propulsion and steering is mainly determined by the main engine and steering gear performance as shown in Figure 8. The FT model of mechanical failure will be used in all three scenarios of with successful communication with TS, with failed communication with TS and under emergency conditions. However, due to the different handling preferences of ships under different conditions, the mechanical reliability also show different states. For example, the state of the ship in the condition of emergency collision avoidance is very different from that in daily collision avoidance operation. In an emergency, the operating range is significantly larger, and the requirements for the mechanical reliability of the ship are also higher. The FTs linked with PE 7, PE 9, and PE 12 share the same FT model structure, but the probability values of basic events are different.

![img-6.jpeg](img-6.jpeg)

Figure 7. The FT model of OS Alarm Failure for Collision Risk (linked with PE 1 OS Collision Alarm).
![img-7.jpeg](img-7.jpeg)

Figure 8. the FT model of Ship Propulsion and Steering Failure (linked with PE 7/9/12).

# 4.3. BNs Modeling of the Conventional Scenario 

In the third step, all the human factor related events, including risk identification, communication, decision, and response action in ESD (PE 2\4\5\6\8\10\11) are further modeled using BNs. The BN method is applied to quantitatively analyze the influencing factors of human-related PEs. In this paper, for each PE that requires BN modeling analysis, the established BN model consists of one PE node and several influencing factor nodes. The PE node is the analysis object, and the result of BN analysis is directly transmitted to ESD for calculating the probability of end state. The influencing

factor nodes are the factors that affect the analysis object in the performance of ship collision avoidance, including environmental factors, operator state factors, safety culture factors, and so on. The interaction between these factors and PE is very complex and involves much uncertainty. It is not possible and appropriative to use FT to model and analyze, while BN modeling is suitable in this situation. For example, human error events, such as fitness for duty (FFD) of office on watch (OOW) and the experience of OOW, are among the most important contributors to a collision accident.

Figure 9 illustrates all the BN structures, which are linked with PEs of the ESD model. Only factors that affect the PE node are analysis in this BN, and the standard of the level setting of each node is based on the degrees of impact, which are listed in Table 2. For instance, the environmental factors (blue nodes) can include wind, wave, current, weather, and sunshine conditions at the site, but these factors can be unified into the impact on PE node, which is advantage or disadvantage to the identification of risks. Therefore, when building the BN, the environment is taken as a separate node, and the level is set to be advantage and disadvantage. Besides the environment, the current states of both encountered ships also have a similar way of the influence on the risk identification, so the level settings of these nodes (cyanic nodes) are also advantageous and disadvantageous. In ship collision avoidance practice, CPA is the main method to identify the collision risk. Accurate estimation of CPA is necessary to successful risk identification, and the estimation of CPA is contributed by the estimation of states of both ships. All the estimations are based on the state of officers on duty include pressure, mental condition, and fatigue. The level setting of all these kinds of nodes is effective and noneffective.
![img-8.jpeg](img-8.jpeg)

Figure 9. The BN models of the proposed HCL model.

Table 2. Descriptions and Level labels of the BN-model.


BN-2 OSRSDecision was linked with PE 4 (OS Response Strategy Decision), share BN structure with PE 10 (OS Response Strategy Decision for Emergency)


BN-3 Communication was linked with PE 5 (OS Effective Communication with TS)


BN-5 EmResAct was linked with PE 11 (OS Crew Response Action for Emergency), share BN structure with PE 8 (OS Crew Response Action with Failed TS Communication).


It should be noted that PE 4 and PE 10 model the decision-making process of collision avoidance under different conditions (daily condition and emergency condition), so they share the same BN

structure and CPT level settings. However, due to the different conditions, the specific values of the probability distribution of the CPTs are different. The BN-5 linked with PE 11 and PE 8 is built in the same way.

# 4.4. Model Assignment of the HCL Model 

The fourth step is to assign the event probabilities in the ESD and FTs, and the CPTs of BNs. All the values of these ESD pivotal events, FT basic events, or RIFs were defined based on historical data, associated literature, and expert judgement. The data came from the handbook of offshore reliability industry [39,40], as well as the international collision accident reports. Completing the CPTs of BNs is much more challenging than the probability of ESD and FTs. Uncertainties, assumptions, qualitative, and quantitative analysis methods are usually employed to model these RIFs reasonably well [18]. In this paper, 50 ship collision accidents are chosen from more than 100 ship collision accident investigation reports. The CPTs are developed using the historical data by using the collected statistical data and expert judgment by IF-THEN rules [38]. Some similar PEs are modeled with the same FT or BN structure, but the setting of probability value varies according to different situations.

As this is the first application of the HCL methodology to ship collision accidents, the details of the model are expected to be improved in a further study that will include the full range of uncertainties as well.

## 5. Results of Risk Analysis of Ship Collision Accident Scenarios

The three main end state types of ship collision avoidance scenario have been quantified using Trilith. The probability values and percentage of all the end state events are listed in Table 3, and the fractions of the three-different end state types (i.e., safe, collision, collision due to mechanical failure, and collision due to human error) to the sum of all ends states are listed at the end of Table 3.

Table 3. Probability Values of All End State Events.


The several conclusions can be drawn from Table 3:
(1) All the results are based on the probability of Initial Event (IE). The value is preset as $\operatorname{Pr}(\mathrm{IE})=1$ in Table 3 to show the probability of safe and collision in an easier way. This result shows that, given the probability of a dangerous encounter situation, the probability of safety is 0.3926 and the probability of a collision accident is 0.6073 . Among it, the probability of accidents due to

human error accounts for $94.27 \%$ of the total accident probability, and the probability of accidents due to mechanical failure is $5.73 \%$.
(2) The value of $\operatorname{Pr}(\mathrm{IE})$ comes from experts' opinion, which means that in daily navigation, about $\operatorname{Pr}(\mathrm{IE})$ of the conflicts may lead to more urgent situations. In academically accepted data [41-43], the causation probability of different types of collision accidents is different, for instance, the causation probability of overtaking and head-on are $4.90 \times 10^{-5}$, while the probability of crossing is $1.30 \times 10^{-4}$.
(3) The collision accidents due to human factors are accounted for $94.27 \%$ of the total in the ship collision scenario. Considering that the industry consensus is that $75-96 \%$ of marine accidents are human factor related [44,45], this result is reasonable. Compared with other situations, mechanical failure is more unlikely. Therefore, the improvement of ship collision safety by enhancing human reliability will be more effective than the improvement of mechanical system reliability.

In order to further verify the accuracy of the analysis results, the historical data of the Singapore Strait from 1997 to 2002 is selected to estimate the collision frequency in this region. The results of the analysis are shown in Table 4. In Table 4, the causation probabilities, which refer to the probability that collision avoidance measures need to be taken in the conflict scenario, are obtained from existing studies ([32-34]). The number of conflicts is the frequency count of two ships forming a specific encounter situation. The monthly conflict scenario frequency comes from statistical data [46], and the annual conflict scenario is calculated from monthly data. The causation probability and the frequency of annual conflicts constitute the value of initial events of the proposed HCL model. Then, the frequency of the accident is obtained by multiplying the probability of collision in Table 3 by the frequency of the initial event.

Table 4. Ship collision accident estimation in the Singapore Strait.


${ }^{1}$ Commonly accepted by the existing studies ([41-43,46]); ${ }^{2}$ Collision frequency $=$ Causation probability $\times$ Number of conflicts $\times$ Probability of collision in Table 3.

According to Table 4, during the year 1997 to 2002, the average number of conflicts of different types of collision accidents is assessed. The estimated collision frequency is 1.11 per year, while the frequency based on historical data is 1.80 per year. In a targeted study [46], this estimated data is more accurate than the method proposed in this article. However, the method proposed in [46] is based on a detailed historical data study of the area in the Singapore Strait with different encounter types. Considering that the HCL model proposed in this paper does not make further adjustments for different ship encounter situations, this result is acceptable.

In previous studies, the frequency estimation of maritime accidents is generally made based on based on historical data [47] or other quantitative risk assessment methods [48] for a certain region. These methods can estimate the data accurately, but they cannot be used to mine the logic and deep mechanism of accident development. In addition, Bayesian method is widely used in qualitative and quantitative analysis of uncertain factors [18] and has achieved good results. However, the BN method can only statically analyze the influence of a certain factor on the accident result from the system state level. It is impossible to analyze the basic events and related factors in the development process from the perspective of accident evolution. It is also impossible to distinguish the modeling of mechanical reliability failure events from the analysis of uncertain factors.

The HCL method focuses on the evolutionary order of events and lists various scenarios that may occur. Based on the modeling of event sequence, analysts can easily use the risk analysis model to

further analyze the event. This kind of analysis is vertical in the sense that it can directly study the influence of the reliability change of a node in BN or FT on the whole event.

# 6. Conclusions 

This article is an attempt to remove some of the limitations of current approaches and address some of the deficiencies of risk assessment to current ship collision risk assessment by using HCL method. The qualitative and quantitative analysis is presented based on 50 ship collision accident investigation reports. The unique three-layer framework of the hybrid causal logic (HCL) methodology allows different modeling technologies to take advantage of their respective strengths to analyze different aspects of the system. A complete set of hybrid structures goes beyond the typical PRA approach and allows the inclusion of uncertainties introduced by the human and organizational aspects of the system. The HCL method effectively enhances the ability of risk analysts to establish non-deterministic relationships between uncertain elements (e.g., human or organization) into the PRA. For hardware elements (e.g., machine reliability), the ESD and FT models are retained for modeling system-level and event-level elements separately. By taking advantage of the multi-level modeling capabilities of the HCL methodology, the modeling of ship collision scenarios can be carried out at a deep logical level. At the same time, it is possible to combine the detailed analysis of various primary events with a comprehensive analysis at the system level. This enables the comparative study of different ship collision scenarios. Because no matter what type of ship is assessed, a similar high-level logical sequence can be constructed for collision avoidance scenarios, while the system characteristics are captured in the low-level layers. Besides the convenience of modeling, the HCL method provides a series of qualitative and quantitative calculation and analysis methods, which also enabled this research.

The successful application of the HCL method requires the analyst to have a good understanding of the sequence of the events, during the course of a potential collision situation and the contributing courses, including equipment failure and human error. Since this is the first attempt to apply the HCL methodology to maritime safety, the quantitative results obtained are only best estimate. In future work, the various sources of uncertainty will be identified, and the models will be assessed to obtain numerical results that include the uncertainties.

Author Contributions: Conceptualization, A.M. and X.Y.; methodology, T.W. and M.A.D.; validation, Q.W. and A.M.; writing-original draft preparation, T.W. and M.A.D.; writing-review and editing, A.M., X.Y., and Q.W.; supervision, A.M. and Q.W.; project administration, X.Y.; funding acquisition, X.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This work presented in this paper is cosponsored by Funds for International Cooperation and Exchange of the National Natural Science Foundation of China (Grant No. 51920105014), China National Key Research and Development Plan (Project/Task No. 2018YFC0810400/05). The first author of this paper is supported by the China Scholarship Council (CSC) and the Fundamental Research Funds for the Central Universities (Grant No. WHUT2017-YB-035). The financial support is acknowledged. The opinions expressed are those of the authors and should not be construed to represent the views of the project consortia.
Acknowledgments: The presented Hybrid Causal Logic (HCL) model has been developed using the Trilith modeling platform maintained at the B. John Garrick Institute for the Risk Sciences, University of California, Los Angeles.

Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A. List of Accidents Analyzed (in Chronological Order)



Chemical/products tanker | ATLANTIC LADY, Refrigerated cargo ship | $\begin{aligned} & 55^{\circ} 32.0^{\prime} \mathrm{N} \ & 12^{\circ} 42.5^{\prime} \mathrm{E} \end{aligned}$ | The Sound, southern part, Denmark | 2014/11/1, 13:19 | None |  | The Danish Maritime Accident Investigation Board  |

Chemical Tanker | KEIHIN MARU No. 8, Oil Tanker | $\begin{aligned} & 35^{\circ} 28.2^{\prime} \mathrm{N} \ & 139^{\circ} 47.3^{\prime} \mathrm{E} \end{aligned}$ | Off to the Southeast of Higashi-Ogishima Island, Kawasaki City, Kanagawa Prefecture; | 2016/07/08, 09:27 | None | 2,000,000 | Japan Transport Safety Board  |
Commercial
Fishing vessel | James 2, recreational motor cruiser | $\begin{aligned} & 50^{\circ} 49.33^{\prime} \mathrm{N} \ & 000^{\circ} 12.56^{\prime} \mathrm{W} \end{aligned}$ | Near Shoreham | 2017/06/08, 00:26 | 3 death | James 2 total loss | Marine Accident Investigation Branch, United Kingdom  |
Cargo ship | ZEUS, Liquefied gas bulk carrier | $\begin{aligned} & 34^{\circ} 15.3^{\prime} \mathrm{N} \ & 133^{\circ} 38.3^{\prime} \mathrm{E} \end{aligned}$ | Around 328 o true bearing and 1.4 nautical miles from the Takuma port Sudaichimonji breakwater east lighthouse | 2017/07/08, 06:08 | None | 2,000,000 | Japan Transport Safety Board  |
