# Article 

## Dynamic Safety Assessment and Enhancement of Port Operational Infrastructure Systems during the COVID-19 Era

Siqi Wang (D), Jingbo Yin * (D) and Rafi Ullah Khan (D)

## check for updates

Citation: Wang, S.; Yin, J.; Khan, R.U. Dynamic Safety Assessment and Enhancement of Port Operational Infrastructure Systems during the COVID-19 Era. J. Mar. Sci. Eng. 2023, 11, 1008. https://doi.org/10.3390/ jmse11051008

Academic Editor: Mihalis Golias
Received: 8 April 2023
Revised: 3 May 2023
Accepted: 3 May 2023
Published: 8 May 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

School of Naval Architecture, Ocean \& Civil Engineering, Shanghai Jiao Tong University, Shanghai 200240, China; wangsiqi0112@163.com (S.W.); asaduetian1@gmail.com (R.U.K.)

* Correspondence: jingboyin@sjtu.edu.cn


#### Abstract

Seaports function as lifeline systems in maritime transportation, facilitating critical processes like shipping, distribution, and allied cargo handling. These diverse subsystems constitute the Port Infrastructure System (PIS) and have intricate functional interdependencies. The PIS is vulnerable to several external disruptions, and the impact of COVID-19 is severe and unprecedented in this domain. Therefore, this study proposes a novel general port safety framework to cope with recurring hazards and crisis events like COVID-19 and to augment PIS safety through a multi-state failure system. The PIS is divided into three critical subsystems: shipping, terminal, and distribution infrastructure, thereby capturing its functional interdependency and intricacy. A dynamic inputoutput model is employed, incorporating the spatial variability and average delay of the disruption, to determine the PIS resilience capacity under the stated disruptions. This study simulates three disruption scenarios and determines the functional failure capacity of the system by generating a functional change curve in Simulink. This study offers viable solutions to port managers, terminal operators, and concerned authorities in the efficient running of intricate interdependent processes and in devising efficient risk control measures to enhance overall PIS resilience and reliability. As part of future studies, given the difficulty in obtaining relevant data and the relatively limited validation of the current model, we aim to improve the accuracy and reliability of our model and enhance its practical applicability to real-world situations with data collected from a real-world case study of a PIS system.


Keywords: Port Infrastructure Network; COVID-19; port disruption; input-output model; risk assessment

## 1. Introduction

The maritime industry undertakes $90 \%$ of trade worldwide, and its participation in the global value chain has increased substantially due to the positive impacts of digitization [1]. Ports play a major and critical role in maritime transportation as a lifeline system, facilitating shipping, distribution, and other facilities for cargo transportation via waterways between various regions (as Figure 1 shows) [2], and involve infrastructural elements that constitute a Port Infrastructure System (PIS). Although PISs are critical and costly engineering systems enabling national and international trade in a secure and resilient way [3], the sheer volume of operations and the function of connectivity make the ports vulnerable [4,5]. The COVID19 pandemic has had a severe and unprecedented impact on ports, making people realize that external disruptions to the port system are recurring events that test the safety and resilience of the port industry. The data provided by the United Nations Conference on Trade and Development shows that there was a significant decline in the number of ship calls in 2020 compared with the weekly ship call data of world ports in 2019. The port system also affects a variety of aspects, such as the supply of goods and available resources, demand patterns, and even the safety level of ships, terminals, and inland freight collection and distribution systems.

![img-0.jpeg](img-0.jpeg)

Figure 1. Port mechanism (cargo from region 1 to region 2).
In addition, the functions of different dimensions of a port are interrelated, facing various risks and emergencies, including natural disasters (flood, earthquake, etc.), public health events (2019 COVID-19), disasters brought about by accidents (2015 Tianjin Port explosions), and security incidents, causing various disruptions in the lifeline system and human society. These disruptions cause system vulnerabilities, inflicting unacceptable damage to system safety, human life, and the environment. For example, two days of heavy rain in western Canada in November 2021 caused flooding and mudslides, resulting in disruptions to terminal operations, delays to ships in port, and a severe blow to the supply chain. Recent black swan events, such as the COVID-19 pandemic, have caused disruptions in port service due to the implementation of disease control measures [6]. In December 2019, the COVID-19 outbreak disrupted worldwide port and terminal operations on many fronts, encompassing chaos in warehouses, empty container management and availability, hinterland traffic disruption, and infrastructure operational damage, leading to a halt in logistics and port workers' operability.

Besides, ports are embedded in different networks, such as the local critical infrastructure network, the regional hinterland transport network, and the global maritime transport network. These networks are exposed to a variety of environmental and operating conditions, which cause disruptions that can propagate to other network components [7]. The examples of port logistics risk analysis in Indian sectors [8] and port disruption subject to natural hazards in Laem Chabang port [9] demonstrate that the independence between the port operation systems and the influence of subsystems will affect the overall system resilience and safety state. Large numbers of components and subsystems and their operating complexity make the evaluation and optimization of the system risk and safety complicated [10]. Due to the frequency, intensity, severity, and duration of the impacts of external disruptions, system capacity and performance are of profound importance in tools measuring port safety assessment, ensuring efficient port resilience.

Due to both natural and anthropogenic factors, ports are susceptible to various disruptions that may hinder or completely halt operations. The ability to recuperate from such disruptions is a crucial aspect of a port's resilience [4]. To cope with the diverse range of risks that ports are exposed to, it is imperative to adopt means of managing uncertainty. This includes a focus on risk analysis, mitigation, and avoidance of actions and situations that pose excessive levels of risk, particularly in light of heightened volatility and major internal or external shocks. Generally, risk is defined as the product of occurrence frequency and the consequent severity in accordance with the framework of the formal safety assessment (FSA) set by the International Maritime Organization (IMO) [11]. PIS risk management based on a systematic and purpose-oriented approach is a novel concept that paves the way for ensuring a certain desired level of service and safety with minimal losses incurred to life, property, and the environment. This study is aimed at filling the gap in the seaport safety system assessment discussed in Section 2 in detail, specifically in the

PIS, which is composed of interdependent key infrastructure, and the physical dependence and information interaction between each subsystem.

The utilization of tools for managing port risk and resilience can offer port authorities and companies involved in port operations a range of options and modifications to enhance their risk management approach. Over the long term, any entity seeking to not only survive but thrive must prioritize resilience. This involves elevating risk management to a strategic level and instilling a corporate culture that emphasizes mindfulness, enabling the organization to recognize, respond to, and adapt to changes and the associated risks with agility and effectiveness.

For the functional protection of interdependent PISs, this study incorporates the three interrelated subsystems into an integrated system with reference to PIS operating procedures and analyzes the ability of the PIS system to resist risk. First, because the intensity of a potential attack has large spatial variability, the attack scenario is modeled based on the data of average port waiting time fluctuations due to the COVID-19 disruption, and the component functional state is evaluated based on the multi-state model to measure the functional failure of the system after the system components are disrupted. Simultaneously, the coupling relationship between different subsystems has to be considered when modeling the impact of individual system failures on other systems. Correspondingly, this paper incorporates three attack scenarios into the simulation for different subsystems based on the dynamic input-output model to analyze the corresponding safety level of interdependent multi-infrastructure systems. Finally, the functional failure capacity of the system is calculated, and the functional change curve of the system under external attack events is generated. This study will help to devise measures for augmenting the resilience of shipping by providing reliable and responsive services to customers consistent with accepted risk levels, a primary objective of port operation.

The outline of this paper is as follows. Section 2 reviews the existing literature. Section 3 describes the port safety framework from the perspective of its multi-dimensional, multi-state, and multi-stage aspects. Section 4 introduces the research methodology and establishes the input-output model. The assessment of the simulation models is discussed in Section 5. Section 6 concludes this paper with a discussion of the results, an overall model assessment, conclusions, and remarks for future model development.

# 2. Literature Review 

Many studies have been conducted on port disruptions and safety and explored the possible causes using various models and methodologies. Through a review of prior studies, this section briefly discusses previous research that has focused on port disruptions and potential risks of disruption (Section 2.1), and the risk analysis approaches to enhance system safety (Section 2.2).

### 2.1. Disruption Risks and Port Disruptions

In the field of port disruptions, a study [12] provides a comprehensive review of the existing literature in port disruptions and resilience, examining the causes, effects, and solutions to port disruption, as well as the current state of research on the topic. Port disruption is a major issue for the global economy, as it can cause significant delays in the transportation of goods and services. The most common causes of port disruption include natural disasters, climate change, oil spills, labor disputes, and social and political instability [13,14]. Current research focuses on past occurrences of port disruptions caused by natural disasters such as hurricanes, earthquakes, and tsunamis, which have caused significant damage to port infrastructure operations, and led to delays in transporting goods [9,15]. Research [13] has pointed out that labor disputes are one of the main causes of port disruptions, such as strikes and lockouts, and can also cause delays in the transportation of goods, as workers are unable to access the port. Political instability can also lead to port disruptions, as governments may impose restrictions on the movement of goods and services [16]. Investigation [17] focused on cyclone risk mapping of 1970-2015

for critical coastal infrastructure, taking East Asian seaports as an illustration. In the post-COVID-19 era, the maritime industry has been facing a new challenge, "death congestion," which is spreading and worsening globally, leading to a series of chain reactions, such as soaring freight rates and declining supply chain efficiency [18]. The economic impacts of the shutdown caused by the COVID-19 pandemic on the shipping and port industries of Shanghai port were studied [19] and the impact on maritime sectors in Malaysia was conducted [20]. The US port system has been studied in order to reduce economic impacts when major port disruptions occur [14], while implications for vulnerable ports in Asia were also discussed in [13]. Research [4] investigated the temporal and spatial effects brought by the sequences of the supply and demand shocks of COVID-19 on container ports and the container shipping industry by comparing these events to the 2008-2009 financial crisis.

These port disruptions have had a significant impact on the maritime industry, causing great uncertainties for the maritime logistics supply chain network, which justifies the significance of our research topic [18]. Despite the increased attention paid to this issue in recent years, fewer studies have addressed port disruptions and the strategies to mitigate them, particularly the unprecedented impacts in the COVID-19 era.

In addition, it is difficult to analyze how the COVID-19 pandemic affects the port logistics sector and how the effects of COVID-19 on port logistics propagate to other sectors owing to its interconnectedness and affect the economy of the country [8]. The literature on port disruption has mainly focused on identifying solutions to the problem, such as improving port resilience and risk management strategies. For instance, a state transition model was developed using an integrated and robust risk model to simulate multi-hazard scenarios and analyze the exposure of marine cargoes and ports to natural hazards [9]. A nonhomogeneous Markov decision process was proposed to model ship response strategies to port disruptions caused by hurricanes [21]. In addition, research has focused on the interconnectedness between ports and different networks to reduce the risk of port disruption. Verschuur et al. proposed a systemic risk framework for different networks interconnected through ports and described state-of-the-art risk modeling approaches to quantify systemic risks exposed to natural hazards [7]. To investigate how the effects of COVID-19 on port logistics propagate to other sectors owing to its interconnectedness, a scenario-based interval input-output model was established to analyze the risk of the COVID-19 pandemic in port logistics [8].

Overall, the literature on port disruption is extensive and provides a comprehensive overview of the causes, effects, and solutions to the problem. Nonetheless, the study of the impacts of COVID-19 and port disruptions in the literature is still in its early stages.

# 2.2. Risk Management Methods 

Risk is widely defined within the literature as a combination of the occurrence of a disturbance and the exposure and vulnerability of a system within different contexts. Researchers from different fields and research communities have investigated risk management methods, each with its own concepts, methods, frameworks, and models for risk management. For example, researchers [22] studied the risk assessment of marine LNG (liquefied natural gas) offloading systems, considering weather-related hazards based on infrastructure resilience-oriented modeling language methods, while a resilience-based approach was proposed to evaluate urban rail systems based on Bayesian networks and historical data [23]. Bayesian networks (BNs) have been widely recognized as an effective and reliable tool for risk analysis and have been extensively employed in the literature. To capture the dynamic behaviors of critical infrastructure systems, researchers have proposed dynamic Bayesian networks [24]. The risk analysis of marine and offshore systems was carried out based on the dynamic Bayesian network [25], and the functional resonance analysis method on an emergency response system has been studied in [26]. BNs have proven to be effective tools for conducting quantitative risk assessments, particularly in the analysis of ship collision scenarios under the combined effects of human and organizational

factors, where BNs have been used in conjunction with fault tree analysis (FTA) [27]. A novel risk assessment framework for maritime cyber threats, which combines failure mode and effects analysis (FMEA) with a rule-based Bayesian network (RBN), is proposed and used to evaluate the risk levels of the identified threats and to better understand the threats that contribute the most to the overall maritime cybersecurity risk [28].

In the field of reliability analysis and risk management, the introduction of an algorithm capable of mapping a multi-state fault tree to a BN model was a significant contribution [29]. The multi-state approach is widely used in reliability analysis and risk management fields due to its capability of capturing probability changes over time [30]. Additionally, the multi-state approach combined with the dynamic BN theory has been employed to analyze the mechanical hydraulic lifting system [31].

In general, the importance of PIS risk assessment is self-evident. However, to amalgamate the concepts of sustainability and reliability, a more purpose-oriented and efficient approach is needed. Therefore, a methodology was provided for estimating the effects of the earthquake on the performance of the operating system of a container terminal in a seaport [32]. Researchers used stochastic methods to assess the timeframe and economic viability of the climate impact risks for building infrastructure [33].

The complexity of the systems' operation processes and their influence on changing the systems' structures and their components' reliability characteristics promptly are often very difficult to fix and analyze with two essential characteristics: long service life and low probability of failure [34].

Dynamic modeling and simulation frameworks of infrastructure systems from the perspective of network and asset representations are also used to model the optimal response to disruptions using a rolling planning horizon [35]. Inoperability input-output (IMM)-based models are useful for macroeconomic-level or industry-level interdependency analysis in the aftermath of natural hazards, malicious attacks, or accidental events [36]. The IMM-based model can be used to analyze the inoperability of infrastructure systems, leading to their successful applications in terrorism risk analysis of the interdependent transportation systems in Virginia [37], the resilience between the power delivery system and telecommunication system during Hurricane Katrina [38], and the demand reduction of air transportation following the terrorist attacks of 11 September 2001 [39].

Several studies have utilized the semi-Markov model to evaluate port systems. A semi-Markov model of a series-parallel multi-state system was proposed to evaluate the reliability, availability, and risk of the port grain transportation system [40]. When the component number is large and the system failure event is rare, reliability analysis of series systems can be performed using the adaptive Monte Carlo simulation method [41]. Safety state models were employed and a semi-Markov model was established to evaluate the reliability and transition process between various safety states of the maritime transportation system [42]. Study presented a general-model unknown-parameters approach to determine port system reliability [43]. The interdependency between various components and processes of the seaport system were investigated and how these interdependencies contribute to a disruption risk was evaluated [5]. Astochastic Markov model was proposed to model the deterioration process for the maintenance of offshore engineering systems [44].

In summary, port risk analysis and intermodal transportation safety resilience considering maritime transportation have not yet received significant attention from academic researchers [12]. The research has identified a number of potential solutions to the problem, and further research is needed to identify the most effective strategies for reducing the risk of port disruption.

# 3. Port Safety Framework 

This section may be divided by subheadings. It should provide a concise and precise description of the experimental results, their interpretation, and the experimental conclusions that can be drawn.

# 3.1. Impact of COVID-19 on Port Operational Infrastructure Security 

As the connection node linking the railroad, shipping lines, trucking companies, freight forwarding companies, customers, shipping agents, depots, warehouse operators, and airlines [45], the PIS provides multi-dimensional services, including the following:

1. Physical function:

The port infrastructure facilitates the loading and unloading operations for ships entering and leaving the port [46]. The ports provide comprehensive logistics services for ships, automobiles, associated multi-modal transport, cargo, and containers, such as transit and warehousing, to enhance the efficacy of multi-modal transport and distribution processes [47].

## 2. Economic function:

The port nurtures the regional economy and becomes a prominent infrastructure component with a robust and boosting impact on the growth of the regional economy [4]. The port is a prerequisite for the existence of domestic and foreign trade and the promotion of their development. Modern ports are meant to provide users with convenient transportation, commerce, and financial services, such as insurance, financing, freight forwarding, shipping agencies, and customs clearance [45].

## 3. Social function:

Ports not only play an important role in economic activities but also have a critical social function. The development of ports has stimulated trade activities and job opportunities, thereby aiding in boosting the port area's economy and social stability. The port is the growth point of urban development, driving socioeconomic development and promotion [48].

## 4. Environmental function:

As nodes in global supply chains, ports generate environmental impacts through their various functions linked to cargo handling, connectivity to maritime and land transport networks, industrial and semi-industrial activities, logistics and distribution activities, and energy production and distribution [49].

## 5. Organizational function:

The port is part of the socio-ecological environment and has an organizational function. Port authorities have become complex entities, managing port network communities with the goal of developing integrated transportation and logistics services for their hinterlands [4].

There is a complex coupling relationship between different dimensions of the diverse port functions. The functions of the port are vulnerable to several risks, including natural disasters such as floods, storms, and tsunamis; public health emergencies such as the COVID-19 outbreak; calamitous accidents such as explosions at the ports of Tianjin and Beirut; and various security threats that could cause disastrous disruptions in human society and lifeline systems.

Among the aforementioned diverse risk types, this study focuses on public health events (COVID-19), which pose serious challenges to the production and operational processes of ports and terminals across the globe. Specifically, the severe epidemic situation during March 2022 in Shanghai, Shenzhen, and other port and hinterland cities in China resulted in the failure of front-line operators to arrive at ports. Similarly, container and truck transportation at the ports faced blockages due to traffic control and COVID-19-related prevention policies. These hindrances posed a direct threat to the operational process and desired function level of the port systems.

Port systems are subject to intricate challenges in the identification of risks and the multifaceted associations among various components of port infrastructure. This study aims to propose a general port safety framework to cope with various port crises and emergencies and to manage the prevailing hazards and potential crisis events, such as

the COVID-19 impact on port performance, thereby enhancing PIS resilience under such attacks by employing a multi-state failure approach.

# 3.2. Research Methodology 

Figure 2 shows the proposed port safety framework. The methodology subsection consists of the risk assessment of PISs influenced by the complexity of risk identification and port system correlation, carried out in three stages. First, port functions and the definition of PISs are analyzed from a multi-dimensional perspective. Second, the system components, subsystems, systems, and interdependencies are analyzed from a multi-state system perspective. Finally, a multi-stage security assessment of the PIS is carried out.
![img-1.jpeg](img-1.jpeg)

Figure 2. High-level architecture.

### 3.2.1. Multi-Dimensional

The definition of port functions emphasizes the interactions between the parts of a system and the external environment required to perform a specific task or function [44]. During port operations, various PIS components are interconnected, and the diverse components of PIS further enhance the interdependencies and complexities. It is noteworthy that such sophistication compromises the scale and accuracy of the models developed for the analysis of these systems.

Therefore, the impact of external uncertainty on an operational infrastructure system can either have a direct effect on the infrastructure or an indirect effect through the associated infrastructure components. The failure of aging components and inner-system state fluctuation, as well as external risk attacks from outside the system caused by natural disasters or any other factors, may trigger unpredictable chain reactions, resulting in large-scale damage or destruction of infrastructure operations across various subsystems and sections, causing service interruption and economic loss.

This study aims to ensure the functional safety of interdependent critical operational infrastructure systems by incorporating the interrelated subsystems into the integrated system and to analyze the ability of the PIS system to resist risk.

# 3.2.2. Multi-State 

Correspondingly, this subsection will take a macro perspective (input-output perspective) on the basis of the multi-state model and the dynamic model based on simulation to analyze the corresponding safety level of interdependent multi-infrastructure systems. There are also complex correlations at the system scale. There are complex coupling relationships among components, individual systems, and associated subsystems. The PIS and its subsystems are fundamental elements of critical maritime infrastructure. The existing literature focuses mainly on external factors affecting the safety of maritime and port critical infrastructure. However, arising from the significant interdependencies between various components and their functionality, the safety and resilience of ports have become complex issues [50].

### 3.2.3. Multi-Stage

The influence of disruptions gives rise to intricate interconnections at various phases of the system, including pre-disaster preparedness, response actions during the disruption, and post-disaster recovery measures, which have an impact on the functional capacity of the system. These couplings affect the level of decision-making and its effectiveness.

A multi-stage simulation of the following scenarios was conducted to cope with the above complexities. The risk prevention and control of the weaker system components to effectively enhance the comprehensive system adaptability in the event of PIS being disrupted by risk factors was evaluated.

1. Simulation of disruption scenario:

The intensity of the disaster has wide spatial variability. For example, the number of new people infected daily by the epidemic can have a different impact on port operations across the region. Therefore, the degree of damage to the facilities is not the same, and the degree of deterioration of the system's function is also different. Therefore, while developing models for such disruptions and disasters, it is of critical importance to consider the scenarios and spatial variability of the disruption.
2. Evaluation of component functional state:

Port facilities face escalating failures arising from the effect on PIS of COVID-19 disruption. This study aims to use a multi-state model to determine the failure mode of the system under a critical degree of external attack.
3. Calculation of the system functional failure capacity:

After the system components are affected, the localized failure impact will not only spread within the subsystem but will also affect other subsystems and systems of other functional dimensions. Therefore, to measure the functional failure of the system at a specific time, the coupling relationship between different systems should be considered. This approach will determine the impact of individual system failures on other systems under the input-output model under consideration.
4. Simulation of system function:

Finally, the functional change curve of the system under a disruptive event is generated in Simulink.

The International Maritime Organization (IMO) aims to enhance maritime operation safety, including the protection of life, health, the marine environment, and property. As a result, the Formal Safety Assessment was proposed by the IMO in 2002 and has been integrated into the five-step approach comprised of Identification, Measurement, Prioritization, Management, and Mitigation [51].

To evaluate the port system, the following steps can be taken: (1) Identification, which involves defining the system to be evaluated as the PIS operating procedure analysis; (2) Measurement, which entails determining the PIS states using a combination of failure mode and dynamic model analysis; (3) Prioritization, which involves estimating the system's

function and providing timely warnings of potential system hazards; (4) Management, which involves controlling and managing system risks; and (5) Mitigation, which entails reducing environmental damage and asset loss.

The main purpose of this study is to provide a methodology for estimating the effects of disruption on the performance of the operational system of a terminal in a seaport. A formal port safety framework is developed using the following steps in the context of COVID-19 disruption risk analysis to evaluate the consequences of disruptions caused to the PIS [32].

# 4. Dynamic Safety Assessment of the Port Operational Infrastructure System 

### 4.1. Port Infrastructure System Operating Procedure Analysis

The PIS plays a critical role in facilitating business system operations. Ports, as a part of the PIS, can enhance the level of service in the system. Ports are complex networks, both from an infrastructure and navigation point of view [46]. The port components (i.e., quay wall, pier, crane, and warehouse) and their supporting infrastructure (i.e., roads, railways, piers, breakwaters, power lines, ICT networks, etc.) are considered the maritime critical infrastructure [5]. Study elaborated ship traffic and port operation information with respect to critical infrastructure networks, focusing on the critical infrastructure in the Baltic and adjacent seas [52]. Research focused on Baltic ports, revealing that shipping, ship traffic, and port operation information are a joint critical infrastructure network comprising the port critical infrastructure system, the shipping critical infrastructure system, and the ship traffic and port operation information critical infrastructure system [53]. The investigation considered the maritime transportation system to be one of the most important components of critical infrastructure, elaborating on it as a subsystem of critical infrastructure and modeling the safety of critical infrastructure systems [42].

The complexity of port activities indicates that it is not sufficient to only consider ensuring the security and defense of ports in maritime critical infrastructure protection [42]. A disruption in terminal operations and, hence, the PIS can have serious repercussions on the regional economy. Port operating authorities should be mindful of the immense economic impact of port disruptions caused by diverse risk factors [32]. The efficiency of port infrastructure operations can be identified by analyzing the time lapse between the arrival and departure of vessels [4].

This section describes the main operating procedures linked to the processes of shipping, loading and unloading, and dry docking to represent the structure of the PIS (Figure 3). Port operating processes begin in the foreland when a vessel arrives and waits outside the port in the anchorage until the navigation (shipping) traffic service provides information about berth availability. Once a vessel is allowed to enter the port, it sails to a specific berth, and loading/unloading operations start. Ports are composed of specialized terminals designed to handle a specific cargo type. When the loading/unloading operations are completed, vessels are ready to depart. They are required to ask for permission to leave the port or to sail to another berth. The port distribution process occurs when cargoes are allowed to transfer to warehouses through the truck and rail networks in the hinterland.

Overall, the operating procedure of the PIS considered in this study consists of the following:

- Subsystem 1: Shipping critical infrastructure system;
- Subsystem 2: Port terminal infrastructure system;
- Subsystem 3: Port distribution networks system.

![img-2.jpeg](img-2.jpeg)

Figure 3. Diagram of port infrastructure and processes.

# 4.2. Risk Analysis of the PIS Based on the Dynamic Model 

### 4.2.1. Inoperability Input-Output Model of the Port Operational Infrastructure System

Most real PISs are very complex, and it is difficult to analyze the reliability and availability of their time-varying operation processes. The input-output model can be used to study how the fluctuations of the external environment for a certain node are propagated in the system and what the consequences are. It is also used to calculate how to make the necessary adjustments in the system, whereby the failure propagation can be eliminated, and the system can be restored to its ideal equilibrium state as soon as possible. Influences and attacks on the PIS from outside the system or other systems can be considered and expressed in the form of additional inputs (or interference).

The original Leontief input-output model is as follows:
$x=A x+c, x_{i}=\sum_{j} a_{i j} x_{j}+c_{i}, \forall i$. The term $x_{i}$ refers to the total production output from the industry $i$; the Leontief technical coefficient $a_{i j}$ is the ratio of inputs of industry $i$ to industry $j$ in terms of the total production requirements of industry $j$; the notation $c_{i}$ represents the industry $i^{\prime}$ s total output for final consumption by end users.

Applied to the port infrastructure system: The first-generation physical input-output inoperability model (IIM) was proposed in [54]. It applied the model to interdependent port infrastructure systems and interpreted the output as the risk of inoperability, defined as the inability of a PIS to perform its intended functions. This model helps quantify the probability that a component will be affected or compromised and the potential consequences that occur when the component has been compromised. The model can be used to determine the consequences of PIS disruptions. To analyze which components of the PIS are likely to be affected or attacked and to classify the importance of the components, the following model was established to describe the attacker's behavior.

$$
\begin{gathered}
\dot{x}_{k}(t)=\sum_{i=1}^{n} a_{k i} x_{i}(t)+c_{i}(t) \\
c_{i}(t)=\lambda_{k} z_{k}(t)
\end{gathered}
$$

$$\begin{gathered} z_{k} = 0.5\delta(t-1)y_{k},k = 1,2,3 \\ y_{k} = \begin{cases} 1, \text{attack on system } i \\ 0, \text{no attack on system } i \end{cases} \\ \qquad\sum_{i=1}^{3} y_{k} = 1,k = 1,2,3 \end{gathered}$$

In this model, *x*_{*i*}(*t*) is the overall risk of inoperability of the *i*th subsystem at time *t* that can be triggered by malicious attacks or accidental disturbances; *a*_{*i**j*} is the probability of inoperability that the *j*th subsystem contributed to the *i*th subsystem due to their interconnectedness; *c*_{*i*}(*t*) is the additional risk of inoperability that was inherent in the complexity of the *i*th subsystem at time *t*.

In the interdependent PIS, interdependency means a bidirectional relationship between two infrastructures through which the state of each infrastructure influences or is correlated to the state of the other [55]. Depending on the PIS operating procedure analysis in Section 4.1, the interconnected port infrastructure system in this study is composed of three interdependent subsystems: the shipping critical infrastructure system, the port terminal infrastructure system, and the port distribution networks system (see Figure 4). The matrix of interdependence coefficients between the subsystems is represented by *ρ*_{*k**i*}.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Diagram of interdependence coefficients between the subsystems.

### 4.2.2. The Interdependency Matrix of PIS

The port of Shanghai, one of the world's largest ports by cargo tonnage, saw steady growth in port throughput in the first quarter of 2022, but since the end of March, there has been a severe disruption at the port following the serious outbreak of COVID-19 in China's major financial and trade hubs (see Figure 5). The analysis of the damage risk of external randomness can enable the system to avoid mutual influence between different subsystems and maintain their independence.

![img-4.jpeg](img-4.jpeg)

Figure 5. Diagram of average port waiting time trend due to COVID-19 disruption in 2022.
In the IIM (inoperability input-output) model proposed in Section 3.2.1, the interdependence between related infrastructure components refers to the probability that their non-operational capabilities will spread to another group of components, represented by the interdependence matrix. The critical infrastructure systems' interdependencies can be analyzed by empirical approaches according to historical accident or disaster data and expert experience [36].

In this study, the operational capacity of the port system is mainly affected by the congestion of incoming and outgoing vessels rather than by the port itself. Based on the Clarkson port congestion index, divided into two phases before and after the attack, during the fluctuation phase, the average waiting time is higher than before the epidemic. Then, after the fluctuation, the port enters a recovery phase, and the average waiting time returns to the pre-attack level. We can see that the increase in vessel waiting time due to the impact of COVID-19 leads to a reduction in the number of incoming vessels, which in turn leads to a decrease in port capacity. Based on the data from the Shipping Intelligence Network (https://sin.clarksons.net/, accessed on 1 January 2022), the decrease in port capacity due to the average port waiting time in the two phases before and after the epidemic is obtained by calculating the data in the two cycles before and after the epidemic and determining the dependency coefficient of subsystem 2 on subsystem 1. In the first quarter of 2022, the throughput of Shanghai Port increased by $8.14 \%$ compared to the same period in 2021 to 12.26 million TEUs (twenty-foot equivalent units). Data from the Shanghai Municipal Transportation Commission shows that in April 2022, the average daily container throughput was expected to be equivalent to 100,000 TEUs, about $75 \%$ of the previous level. According to the data from One Shipping (https://ch.one-line.com/zh-hans, accessed on 1 January 2022), the COVID-19 epidemic led to severe congestion at Shanghai Port, with nearly $60 \%$ of sea and air cargo stuck. The matrix of interdependence coefficients between the subsystems was expressed as

$$
\rho_{k i}=\left[\begin{array}{lll}
\rho_{11} & \rho_{12} & \rho_{13} \\
\rho_{21} & \rho_{22} & \rho_{23} \\
\rho_{31} & \rho_{32} & \rho_{33}
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0.15 & 0 \\
0 & 0 & 0.25 \\
0.4 & 0 & 0
\end{array}\right]
$$

# 5. Simulation 

Simulink is used for model-based systems engineering. Based on Simulink, this study established a simulation model to manage system complexity, improve communication, and produce optimized systems (see Figure 6). The input function was controlled through the pulse function to simulate different attack scenarios, while interdependencies between different subsystems were established to achieve system modeling.

![img-5.jpeg](img-5.jpeg)

Figure 6. Simulation model based on Simulink.

# 5.1. Subsystems Attack Scenario Simulation 

The failure state of each component and its performance degradation under different failure states are considered to affect the system's performance, and the real-time state transition probability is related to the random failure probability of the current failure state of the component. The multi-state system for safety risk analysis can efficiently capture and analyze the partial and subsystem performances and failures in a system under consideration [56].

Based on the port system and process diagram presented in Section 4.1, this study focuses on the operating procedure of the Port Infrastructure Operational System, which comprises three subsystems: the shipping critical infrastructure system, the port terminal infrastructure system, and the port distribution networks system. The port's functional units include the channel, anchorage, berth, wharf, quay crane, yard, truck, rail, and warehouse. Typically, system failure occurs due to faults in the functional units, which lead to deviations in measured values and, ultimately, the loss of the system's or unit's ability to perform a particular function, as Table 1 shows. Systematic failures, as classified by failure mode effect and diagnostic analysis (FMEDA), can be divided into two categories: random failures and functional failures. Random failures, also known as physical failures, occur when port functional units fail during operation. Functional failures are caused by specific factors in a deterministic manner, resulting in the system's inability to perform its intended function.

In port operations, a disruption such as the COVID-19 pandemic diminishes equipment production capacity and can initiate a production or security incident, thereby compromising socioeconomic stability. In this study, the failure rate is defined as the operating capacity reduction caused by the risk attack and calculated by Equation (7). Reduced capacity of the port functional unit refers to the potential loss of value of the system caused by an external disruption, a malicious attack, or an internal component failure. The consequences of an attack reflect the sensitivity of the system and the likelihood of failure, which are generally used to analyze the time characteristics of system components.

$$
\lambda_{i}=\frac{\text { ReducedCapacity }\left(\text { Port Functional Unit }_{i}\right)}{\text { TotalCapacity }\left(\text { Port Functional Unit }_{i}\right)}
$$

Table 1. Failure mode of port functional units.


However, the COVID-19 pandemic has caused significant disruptions to port operations worldwide, resulting in unforeseen challenges to port capacity. The impact of COVID-19 on port operability is felt throughout the cargo loading and unloading, warehousing, transshipment, and hinterland connectivity processes. The idle equipment creates a backlog of containers that cannot be unloaded and transferred to warehouses or hinterland transportation networks, leading to further congestion and delays. This negative impact on port efficiency not only creates a burden on port operations but also has significant economic implications, including potential revenue loss for the port and its stakeholders. The operational capacity of a port system is determined by numerous factors, such as the efficiency of its processes, the availability of resources, and the level of demand. In this study, we focus on the impact of average vessel waiting time, number of incoming vessels, container shipping demand, human resources, transportation, and infrastructure on the operational capacity of the port system, as shown in Table 2.

To perform the vulnerability and resilience analysis on the system, the corresponding resilience situation is constructed to analyze the system failure capacity function, assuming that a certain malicious attacker can only attack one of the three subsystems and can destroy its operational capacity at different levels at time $T=1$. The framework of the simulation is shown in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. Framework of the simulation.

# 5.2. Results of the Simulation 

Taking Shanghai Port as an example, a COVID-19 disturbance is applied to the PIS, challenging the port facility's functionality and initiating failure propagation. Based on the failure mode of port functional units employing the multi-state mode determined in Table 1, functional reduction scenarios to determine the impact of the COVID-19 attack have been considered. The generated scenarios are classified as (1) AS1 with a failure rate


of 0.2; (2) AS2 with a failure rate of 0.4; (3) AS3 with a failure rate of 0.6; (4) AS4 with a failure rate of 0.8; and (5) AS5 with a failure rate of 1.0.

Table 2. COVID-19's effect of input factors on port functional capacity.

The safety of the PIS is determined by its ability to resist disturbances caused by external risks and maintain good system capacity and performance. Quantitative result analysis consists of simulating the system function of failure capacity in an applied failure mode based on a COVID-19 attack (Table 2) at a given time. The quantitative analysis of system safety is based on attack scenario simulation through Simulink, in which the system failure capacity is associated with the input attack event.

The simulation of the system failure capacity following disturbance under different attack scenarios can be comprehensively compared, as Table 3 shows. The system failure capacity curves of the three subsystems (subsystem 1: shipping critical infrastructure system; subsystem 2: port terminal infrastructure system; and subsystem 3: port distribution networks system) are illustrated in Figure 8.

Table 3. Time to complete failure (hours). $\left(t^{*}\right.$ means the shortest time to system failure).


- Scenario1: Attack subsystem 1
![img-7.jpeg](img-7.jpeg)
- Scenario2: Attack subsystem 2
![img-8.jpeg](img-8.jpeg)
- Scenario3: Attack subsystem 3
![img-9.jpeg](img-9.jpeg)

Simulation-Operational capacity ( 0.2 )

- Scenario1: Attack subsystem 1
![img-10.jpeg](img-10.jpeg)
- Scenario2: Attack subsystem 2
![img-11.jpeg](img-11.jpeg)
- Scenario3: Attack subsystem 3
![img-12.jpeg](img-12.jpeg)

Figure 8. Consequences of scenarios 1, 2, and 3 (failure rate at 0.2 and 0.4 ).

1. For attack scenario 1 (Figure 8), the disturbance at time $t=0$ is assumed to be an abrupt discontinuity in subsystem 1 ; the failure capacity function is generated, going from 0 to 0.2 at time $t=1$ (i.e., 1 h after initial time $t=0$ ). The capacity of subsystem

1 goes to 1 at time $t=11.42$, while this happens at $t=10.03,9.47$ in subsystems 2 and 3 .
2. For attack scenario 2 (Figure 8), the capacity of subsystem 1 goes to 1 at time $t=12.70$. When $t=11.41,11.21$, the failure capacity of subsystems 2 and 3 increases to 1 , meaning complete failure.
3. For attack scenario 3 (Figure 8), the capacity of subsystem 1 goes to 1 at time $t=12.92$. When $t=11.39,11.44$, the failure capacity of subsystems 2 and 3 increases to 1 , meaning complete failure.
4. The simulation results above show that when subsystem 1 is attacked at different levels $(20 \%, 40 \%, 60 \%$, and $80 \%$ ) of failure capacity due to COVID-19 disruption, subsystem 3 is the first to achieve complete failure at the times of $9.47,6.56,5.00$, and 4.07 h . Although subsystem 1 is directly attacked, subsystem 3 is the first to fail, followed by subsystem 2, and finally subsystem 1.
5. When the failure capacity of subsystem 2 goes from 0 to 0.2 , subsystem 3 is still the first to achieve complete failure at the time of 11.21 h . While subsystem 2 is attacked at different levels of failure capacity $(40 \%, 60 \%$, and $80 \%)$, subsystem 2 is the first to fail at the times of $8.75,6.98$, and 5.34 h , followed by subsystem 3 , and finally subsystem 1 .
6. When the failure capacity of subsystem 3 goes from 0 to 0.8 , subsystem 3 is still the first to achieve complete failure at the time of 5.35 h . While subsystem 3 is attacked at different levels of failure capacity $(20 \%, 40 \%$, and $60 \%)$, subsystem 2 is the first to fail at the times of $11.39,8.51$, and 6.81 h , followed by subsystem 3 , and finally subsystem 1 .
The port operator in charge of Shanghai Port announced after the outbreak of the COVID-19 epidemic in March that the current efficiency of container truck transportation and the efficiency of port operations would be affected to a greater or lesser extent. However, the information on which specific link would be more affected and to what extent was unclear and could not be determined. The above simulations of 12 attack scenarios show that subsystem 3 is the most vulnerable part of the whole system, as was true of the actual situation at Shanghai Port under the COVID-19 attack. The epidemic closure and control measures have a very serious impact on container trucking and container turnover, putting great pressure on road transportation. Therefore, in the face of the epidemic attack, Shanghai Port launched a "container land to water" service. Customers can first transport their containers to the Taicang service center and then transfer them to Shanghai Port by ship, thereby diverting customers' road transport demand to the waterway and ensuring the smooth flow of the logistics channel. In the analysis conducted in this study, the actual case application of Shanghai Port can verify the validity of the research results and has practical reference value.

# 6. Conclusions 

The motivation behind this study was to devise a protocol whereby, if a port terminal infrastructure system is attacked by external risk factors, the weakest and most vulnerable port distribution system can be controlled before complete failure occurs. This study aims to propose a novel concept of PIS safety management to maintain a desired safety level for the whole system and provide reliable, responsive services to the port operator, concerned authorities, and decision-makers in situations like the COVID-19 attack.

The multi-state methodology and the IIM model are used to model the system failure capacity and the system performance. The system function is simulated to study the features and weaknesses of the subsystems and their integration at the system level. The Shanghai Port case provides an understanding of the model, and the simulations prove its validity. The detailed results provide a time-dependent analysis of the system to resist the external risk attack and enhance the system's performance, thereby avoiding failure by implementing risk prevention and control.

Port performance components provide port operators and government policymakers with essential feedback for assessing whether they meet their strategic objectives [4]. This

study provides a tool that would help port managers, whether port authorities or terminal operators, organize complex processes efficiently and effectively to find the best ways to carry out risk control measures from the perspectives of engineering, system enhancement, emergency response, recovery planning, and risk transfer.

Finally, the weaknesses of the approaches taken in this paper include the following: (1) Many parameters and functions in the models require calibration, requiring a huge amount of data. However, in practice, data access can be difficult for many reasons, including security concerns. (2) As the interdependency matrix is established based on limited data and analysis, the method is also semi-quantitative. (3) Due to the difficulty in obtaining relevant data and the low frequency of epidemic attacks, there is a lack of relevant data and, consequently, relatively limited validation of the model. These weaknesses call for integrating other modeling approaches into a uniform analysis framework for overall decision support [36]. In a future study, the methodology would be updated to cope with multiple systems with more complex interdependency correlations, and the data would be integrated with data from a PIS real-world case study.

Author Contributions: Conceptualization, S.W. and J.Y.; Formal analysis, S.W.; Methodology, S.W.; Software, S.W.; Supervision, J.Y.; Writing—original draft, S.W.; Writing—review and editing, J.Y. and R.U.K. All authors have read and agreed to the published version of the manuscript.

Funding: This research was supported by the Ministry of Industry and Information Technology for research on the key technology of the high-tech ocean passenger ship construction logistics collection system [MC-202009-Z03].

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: This research's initial data is available on Shipping Intelligence Network (https://sin.clarksons.net/) (accessed on 1 January 2022).

Conflicts of Interest: The authors declare no conflict of interest.
