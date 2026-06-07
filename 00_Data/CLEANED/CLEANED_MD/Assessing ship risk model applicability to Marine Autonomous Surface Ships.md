# Assessing Ship Risk Model Applicability to Marine Autonomous Surface Ships 

Christoph Alexander Thieme, ${ }^{\mathrm{a}, \mathrm{b}^{*}}$ Ingrid Bouwer Utne, ${ }^{\mathrm{a}, \mathrm{b}}$ and Stein Haugen ${ }^{\mathrm{b}}$<br>${ }^{a}$ NTNU Centre for Autonomous Marine Operations and Systems (AMOS), Otto Nielsens veg 10, Trondheim, Norway; ${ }^{b}$ Department of Marine Technology, NTNU, Otto Nielsens veg 10, Trondheim, Norway<br>(*corresponding author E-mail: Christoph.thieme@ntnu.no)

Marine Autonomous Surface Ships (MASS) are tested in public waters. A requirement for MASS to be operated is that they should be at least as safe as conventional ships. Hence, this paper investigates how far the current ship risk models for ship-ship collision, ship-structure collision, and groundings are applicable for risk assessment of MASS. Nine criteria derived from a systems engineering approach are used to assess the relevant ship risk models. These criteria aim at assessing relevant considerations for the operation of MASS, such as technical reliability, software performance, human-machine interfaces, operating, and several aspects of communication. From 64 assessed models, published since 2005, ten fulfilled six or more of these criteria. These models were investigated more closely. None of them are suitable to be directly used for risk assessment of MASS. However, they can be used as basis for developing relevant risk models for MASS, which especially need to consider the aspects of software and control algorithms and human-machine interaction.

Keywords: Marine autonomous surface ship, autonomous vessel, collision risk, allision risk, grounding risk

## 1. INTRODUCTION

Marine Autonomous Surface Ships (MASS) are becoming increasingly interesting for the commercial maritime sector as an alternative to conventional ships. Several research projects have investigated MASS concepts (e.g., ReVolt; (DNV-GL, 2015); Maritime Unmanned Navigation through Intelligence in Networks (MUNIN, 2012); Advanced Autonomous

Waterborne Applications (2016). Norway announced the first field test area for MASS, which is shared with public marine traffic (Norwegian Maritime Authority, 2016). The first autonomous cargo ship is supposed to be in operation by fall 2018 (Kongsberg Maritime, 2017).

A MASS may be low manned or unmanned (Rødseth and Nordahl, 2017), which creates challenges in operation. The MASS will influence risk in relation to several marine stakeholders, the environment, and the MASS itself. Collisions and groundings contribute most to the risk level for conventional ships (Pedersen, 2010). The MASS will be equipped with collision avoidance systems and sensory equipment for safe operation. Moreover, the MASS should at least be as safe as conventional ships (Advanced Autonomous Waterborne Applications, 2016; Nautilus Federation, 2018; Pedersen, 2010) to be acceptable for use in public ocean space.

Risk assessments serve to demonstrate a certain level of risk and are an important tool for making relevant design decisions (Rausand, 2011). Wróbel et al. (2017) assessed the effect of unmanned vessels and conclude that MASSs will reduce the collision frequency, while the severity of consequences might increase due to the reduced recovery capability. Hence, risk models, integrating technical, human, and organizational factors, are needed that reflect the operation of MASS. The (Danish Maritime Authority, 2018) has suggested adapting the international regulations such that MASS shall be developed following a goal- and risk-based regulatory approach.

Autonomous underwater vehicles (AUV) have been in the focus of risk research, such as risk management frameworks (Brito et al., 2012; Thieme et al., 2015a), and risk assessments (Brito and Griffiths, 2016; Brito et al., 2010; Griffiths and Brito, 2008; Thieme and Utne, 2017; Thieme et al., 2015b).

For MASS, less research has been conducted. Rødseth and Burmeister (2015b) and Rødseth

and Tjora (2014) analyzed and presented the risk-based design methodology applied in the MUNIN project (MUNIN, 2012), which is based on the formal safety assessment (FSA) process of the International Maritime Organization (IMO, 2002).

The qualitative and quantitative analyses, including considerations of risk, of the MUNIN project were summarized by Kretschmann et al. (2015a); (2015b). The detailed analysis of the MUNIN project was presented by Jensen (2015). Section 4 in the Advanced Autonomous Waterborne Applications (2016) white paper summarizes safety and security considerations and associated challenges for the development of MASS.

Wrobel et al. (2016) presented a Bayesian belief network (BBN) for assessing accidents for unmanned ships based on the mutual influence of different risk factors. Wróbel et al. (2018) developed a safety control structure model of MASS. It is analyzed with the System-Theoretic Process Analysis, to identify possible scenarios where control structures may become inadequate. Both articles address the uncertainty in relation to MASS, their operation, and risk, which makes it difficult to develop a generic and comprehensive risk model for MASS. The present article reviews selected grounding and collision risk models to identify practices and modelling approaches that may be applicable for risk modelling of MASS. It attempts to assess whether current collision and grounding risk models or parts of these can capture the unique aspects of MASS operation. A risk model for MASS operation needs to assess the level of risk, for example, the probability of ship collision.

The systems engineering process is used to identify criteria, which reflect aspects that should be represented in a risk model for MASS. The purpose is to identify potential gaps and focus areas that need to be especially addressed by new risk models developed for MASS. Further this article focuses on operation of MASS (i.e., during transit in the oceans and seas), including vessel approaching ports or offshore installations. Vessels that are not in transit, which carry out specific tasks and operations (e.g., fishing vessels, offshore vessels moored, or

in dynamic positioning mode, research vessels, military vessels, and other special purpose vessels) are excluded. Furthermore, security aspects are disregarded (i.e., the possibility of willful collision or grounding). Current international maritime legislation, such as the United Nations Convention of the Law of the Seas (UNCLOS, 1982), is not adapted to the advent of MASS. This aspect is disregarded in this article, assuming that conventional vessels and MASS are treated alike.

Models for detailed consequence analysis as part of risk assessment are not considered, only limited information on MASS concepts is available. To limit the scope of this article, only risk models that were developed since 2005 are considered in the article. The selected risk models assess the probability of ships colliding, stranding, and/or grounding.

A recent literature review by Lim et al. (2018) on maritime risk models summarizes the model types, modelling methods, and research contributions. Lim et al. (2018) identified future research directions in the maritime risk and security domain for conventional ships This current article is different from Lim et al.'s (2018), because this current article assesses possible modelling approaches from current risk models for conventional ships to MASS.

The next section presents the background and definitions. This is followed by the methodology. The criteria for the assessment of the risk models are identified in the section thereafter. The results section presents the findings and identifies gaps in the risk models that need to be addressed in future risk models for MASS. The models and approaches that are relevant for MASS are discussed in Section 6. This is followed by concluding remarks, and an outlook on further work.

# 2. BACKGROUND 

Risk models for ships are used to assess the risk arising from ship traffic, during ship operation, or for a marine area. Goerlandt and Montewka (2015) reviewed the use of risk definitions and quantification of risk of published maritime risk models. In many cases, these models do not

state the risk definition or risk measure. A clear definition of the concept of risk and other related terms is necessary to clearly describe, communicate, and manage risk (Aven and Zio, 2014). In addition, the international maritime organization (IMO, 2002) defines risk for the framework of FSA as: "The combination of the frequency and the severity of the consequence." Moreover, SN-ISO Guide 73 (2009) defines risk as the "effect of uncertainty on objectives," whereas the effect can be positive or negative. Considering MASS, such a risk definition might be more suitable due to the expected uncertainties regarding the technical solutions, operation, and environment.

# 2.1 Autonomy and Marine Autonomous Surface Ships 

Autonomous systems may have different levels of autonomy (LoA). Autonomy is a system's ability to make independent decisions from a supervising agent and execute these decisions (Vagia et al., 2016). For conventional marine vessels, the supervising operators are the crew. For MASS, only one or a few operators will take a supervising role and intervene when necessary. This is described in more detail in Section 2.2.

The LoA describes the degree of this ability to make independent decisions (Vagia et al., 2016). Typically applied LoA scales are presented by Sheridan and Verplank (1978) or Endsley and Kaber (1999). Comprehensive reviews are provided by Insaurralde (2012) or Vagia et al. (2016). Rødseth and Nordahl (2017) and Utne et al. (2017) defined each specific scale for MASS with four levels. These scales define the decision authority and the tasks that the human operators and the autonomous system carry out, implicitly affecting risk. In this case, the term tasks refers to information acquisition, information analysis, decision selection, and action implementation (Parasuraman et al., 2000). In the lowest LoA (i.e., manual control (Endsley and Kaber, 1999; Vagia et al., 2016) the human operator does everything, and the autonomous system does not assist.

In intermediate LoAs, the autonomous system and the operators cooperate (Endsley and Kaber,

1999; Rødseth and Nordahl, 2017; Utne et al., 2017). In the highest LoA (full autonomy), the human operator has no possibility to intervene with the system (Endsley and Kaber, 1999; Rødseth and Nordahl, 2017; Sheridan and Verplank, 1978; Utne et al., 2017). This is not likely for MASS, at least in the near future.

Autonomy and automation are used often interchangeably, although different aspects are included in the concepts (Vagia et al., 2016). The term autonomy will be solely used in this article. An autonomous system capable of changing the LoA according to the circumstances is designed with adaptive autonomy (Sheridan, 2011).

# 2.2 Operation of Conventional Versus Autonomous Ships 

No formal definition of a conventional ship exists. The UNCLOS (1982) does not define a ship or vessel (Danish Maritime Authority, 2018). Therefore, information on common practices is used. A ship or vessel has a crew for the engine department, the bridge, the deck department, and stewards. The crew level of a cargo ship ranges between ten and 21 people (Curley, 2012). The master of a vessel has the responsibility for the vessel, its safety, personnel, cargo, and passengers. The master has the aboard decision authority. The master acts as a communication point between the shipping company, crew, and other actors (Norwegian Shipowners' Association, 2003). The bridge crew is responsible for navigation and control over the ship. Moreover, UNCLOS (1982) requires a lookout at all times, according to the conditions, and that communication via radio is maintained. The bridge must be staffed according to weather and visibility conditions. A voyage plan must be determined and approved by the master before the vessel sets sail (Norwegian Shipowners' Association, 2003; UNCLOS, 1982).

The chief officer is responsible for the navigation and is second in command. Mates and able sea folk act as lookouts. The deck crew handles the cargo and loads and offloads the vessel (Norwegian Shipowners' Association, 2003). The stewards are responsible for crew wellbeing. The engine department is responsible for supervision and preventive and corrective

maintenance of the machinery (Curley, 2012). The chief engineer is responsible for the engine department (Norwegian Shipowners' Association, 2003).

Rødseth and Burmeister (2015a) and Advanced Autonomous Waterborne Applications (2016) showed that there will be several technical solutions for MASS. The MASS need to be designed for their purpose with different performances, advantages, and disadvantages. Three main concepts of operation of autonomous ships can be differentiated: (i) MASS with low manning (Bertram, 2016), (ii) "master slave" supervision (Bertram, 2016), and (iii) shore control center (SCC) supervised MASSs (MUNIN, 2012; Rødseth and Nordahl, 2017; Rødseth et al., 2014). The main difference in these concepts is the location of the operators or supervisors since none of these concepts are fully autonomous. Current concepts rely on an operator with decision authority supervising the MASS. The operational concepts can only be described superficially, since they depend on the size and purpose of the vessel (Advanced Autonomous Waterborne Applications, 2016).

The three concepts mentioned above all have a control system of the MASS that collects information on the environment, analyses it, makes decisions based on these analyses, and acts accordingly. The MASS needs to be able to sense the environment through machine vision and sensor fusion, for example (Advanced Autonomous Waterborne Applications, 2016; Bertram, 2016). The operators have a supervisory role during voyages and can take control of the MASS when necessary (e.g., if several obstacles are detected, in dense traffic, or during port approach). The operators also handle necessary radio communications with other vessels or vessel traffic service (VTS).

The MASS with low manning (i) are an intermediate solution during the transition period to autonomous vessels that are unmanned (Bertram, 2016; Kongsberg Maritime, 2017). The crew on board a vessel is then reduced in comparison to conventional shipping. The crew can perform necessary maintenance and take control of the MASS if necessary. The MASS will be

mostly in autonomous mode and does not require operator input.
In the "master slave" supervision system (ii), one manned vessel supervises several unmanned vessels. All vessels travel together, and the crew of the manned vessel can take control of the unmanned vessels if necessary. Near ports, pilots and tug boats might assist the vessels (Bertram, 2016). Maintenance of components is, in this concept, rather limited during the voyage, and advanced monitoring systems are needed.

A SCC supervised MASS (iii) configuration (MUNIN, 2012; Rødseth and Nordahl, 2017; Rødseth et al., 2014) is not manned during voyage and is remotely supervised from a landbased SCC. The SCC communicates with the MASS through satellites or through radio-based systems, when the MASS is near the shore. The MUNIN project envisions that, for entering ports, a crew boards the vessel and takes manual control over the vessel (Rødseth et al., 2014). The ReVolt concept envisions low aid needed, through adapted port design and new docking technology (Tvete, 2015). Since MASS that are supervised by a SCC are mainly unmanned, the opportunities for maintenance are limited. Preventive and corrective maintenance can only be executed during port time or dry docking (Rødseth and Burmeister, 2015a). This demands a highly reliable system and proactive condition monitoring that identifies incipient failures. Bertram (2016) argued that conventional diesel engines might not be suited for unmanned shipping since they need frequent maintenance. New concepts, such as hydrogen or battery driven propulsion, are needed (Bertram, 2016; Tvete, 2015).

# 3. METHOD 

### 3.1 Selection of Risk Models

This article considers only models developed since 2005. The MASS concept has received increased attention in recent years due to technical availability and expected financial feasibility. Only models that assess the risk associated with collisions, allisions, or grounding are considered. Allisions are ship-structure collisions (Hassel, 2017; Hassel et al., 2017). The

Scopus ${ }^{1}$ database was searched for the keywords: "Ship OR vessel AND collision model," "Ship OR vessel AND Allision," and "Ship OR vessel AND grounding OR stranding model." The search was conducted on November 3, 2017. Additionally, publications referenced in the literature were included, if possible. Additional references were found in work by Goerlandt and Montewka (2015). One master thesis and one doctoral thesis were included that were not listed in Scopus or by Goerlandt and Montewka (2015): Jensen (2015), and Hassel (2017). Three publications that address MASS, are included. These are Jensen (2015), Wrobel et al. (2016), and Wróbel et al. (2018).

Models that do not give enough information on how the frequency or probability were assessed have been excluded. In accordance with the scope, models covering inland waterways, rivers, or arctic areas have been excluded, such as those by Almaz (2012) or Zhang et al. (2013). Similarly, Valdez Banda et al. (2015) presented a model for risk assessment in ice operation, which resembles a special operation.

Johansson and Molitor (2011) presented a risk assessment for the Baltic Sea, reusing existing models and software. Goerlandt et al. (2012) presented a holistic risk assessment based on previously defined risk models by Hänninen and Kujala (2010) and Goerlandt and Kujala (2011). These three models are assessed as one model in the analysis since they build upon each other.

# 3.2 Development of Assessment Criteria 

To identify suitable and relevant criteria for assessing the existing risk models, a systems engineering approach is employed. First, the problem and the desired systems are described (i.e., the MASS operation). This is the first phase of a systems engineering process (Blanchard, 2008). In the second step, system requirements are described and functional needs with respect

[^0]
[^0]:    ${ }^{1}$ www.scopus.com, accessed on Nov. 3, 2017.

to safety are identified. Typical questions answered in the requirement identification are as follows (Blanchard, 2008):

1. What is required from the system, stated in functional terms?
2. What specific functions must the system accomplish?
3. What are the primary functions to be accomplished?
4. What are secondary functions to be accomplished?
5. What must be accomplished to completely alleviate the stated deficiency?
6. Why must these functions be accomplished?
7. When must these functions be accomplished?
8. Where is this to be accomplished and for how long?
9. How many times must these functions be accomplished?

Not all of these questions can be answered in this article. However, they are used as guidelines for the identification of the needs and requirements for MASS. These give input to the identification of suitable assessment criteria.

# 3.3 Assessment procedure 

The identified relevant ship risk models are categorized according to their approach to risk assessment. The approaches are generally discussed for their applicability and possible further use for MASS. The identified models are assessed against the criteria from Table 2 in Section 4.2.

The models that fulfil most of the criteria are further analyzed in Section 6. Models that fulfill several criteria, are assumed to reflect a high level of detailed modeling of the interaction between the risk relevant modelling aspects summarized in the criteria. The suitability of the models and possible learnings from these are highlighted. This does not imply that the models may be used as they are but they may be used as basis for developing MASS specific risk models.

# 4. EVALUATION CRITERIA 

### 4.1 Functional Requirements with Respect to Risk

The main function of MASS is to transport goods or people from one port to another. This is the same main function as for ships. The transport needs to be safe, cost efficient, and reliable. The main difference between MASS and conventional ships is the reduced crew, which may have implications for the design of the vessels. Safety related functions currently executed by the crew must be carried out by the MASS and its subsystems. The functions in relation to safety are situational awareness of the environment and the surroundings of the vessel, which is the task of the lookout and the purpose of the navigational systems (e.g., RADAR) on a conventional vessel. A more detailed functional analysis and description for autonomous ships can be found in the work by Rødseth and Nordahl (2017).

Table 1 summarizes the requirements for MASS that follow from the description in the previous section. The MASS should identify obstacles and potential hazards and react appropriately in a timely manner (R1). Sensors, computers, and actuators need to execute these functions in a reliable manner, and they need to be available during the voyage. The opportunities for maintenance and repairs are limited. The MASS need to be reliable with respect to sensor systems, machinery, and the control system to achieve their mission goals (R2). The software side and algorithms need to be robust, and verification of their safe performance is desirable (R3). Due to the natural differences between software and hardware, different methods for risk assessment of these are needed (Leveson, 2011).

Table 1 Requirements for MASS based on the operational differences for conventional vessels, identified through an adapted systems engineering process.


Current concepts for MASS (i to iii) still rely on human operators to some degree, partly on board the MASS. They supervise the MASS, adapt the mission plan, or take over control if necessary. Concepts ii and iii require that reliable communication lines with sufficient transmission capacity exist between the MASS and the operators, such that safe operation is possible (R4). There is need for suitable provisions for a crew since it might be necessary to board the ship for berthing (MUNIN, 2012; Rødseth and Nordahl, 2017).

Two more types of communication need to be considered: reliable and adequate communication among the crew/operators in the SSC or on board a low manned vessel in situations that require the human operators to intervene (R5) and communication between MASS operators and other ships or VTS (R6). Both types of communication need to be unambiguous and goal oriented to ensure safe operation. The MASS should be easily accessible for the operators through the provided user interfaces (R7). The operators need to be able to assess the present situation quickly to develop a good situation awareness and be able to reason about necessary actions. Hence, human-machine interfaces (HMI) need to be optimized for usability and accessibility. In cases in which the operators take control of the MASS, the LoA will change, which is called adaptive autonomy (R8). The system and operators must be able to adapt quickly to the new operational mode with a different LoA.

# 4.2 Evaluation Criteria 

Based on the previously identified requirements (cf. Table 1), the criteria for evaluating the

risk models are derived. The criteria reflect the needs of a MASS (i.e., what aspects a ship risk model should cover to be suitable for MASS). Table 2 summarizes the identified criteria for risk model evaluation. It is not possible to rank the importance of these criteria, since each criterion covers important aspects of risk modelling for MASS that need to be included in a risk model.

Table 2 Identified evaluation criteria for ship risk model evaluation for adaptability to MASS.

from Table 1  |
considerations | R7  |
performance | R1, R2  |
participants | R6  |

Criterion 1 summarizes the main difference between MASS and conventional ships. MASS operation will to a large degree depend on software functionality. Autonomous functions, control algorithms, and other software aspects that are failing influence risk.

MASS operation may require a substantial amount of interaction between the MASS and its operators during parts of the voyage. Therefore, it is necessary to consider the HMI and the operators' interaction with the HMI (C2). Communication is also an important aspect in the cooperation and interaction between actors. The operators of one vessel (mainly concepts i and ii) need to communicate to detect and resolve hazardous situations (C3).

Criterion 4 investigates remote communication with the shore base. Conventional vessels should receive substantial support from the shore organization (Norwegian Shipowners' Association, 2003), which requires robust communication lines with the SCC. The MASS may be monitored from a SCC (concept iii), which requires that remote connections are considered. The MASS operating with concepts i and ii might have less contact with the SCC.

MASS may be unmanned and it may not be possible to perform maintenance immediately when necessary. This is especially true for long voyages. Hence, the system reliability and maintenance (C5), and backup solutions in case of failure of a sub-system (through functional redundancy, C6) are important. A risk model should consider functional redundancies that were introduced in the system to reflect the risk level accurately. The MASS will employ several sensor systems to create a holistic operational picture via, for example, sensor fusion.

Criterion 7 aims at the assessment of the models with respect to different operational modes and LoA, such as piloted, auto-piloted, manual control, or autonomous voyage. Consideration of the operational mode is necessary since the operators' interaction with the vessel and the performance of the vessel itself will change. The vessel navigation will vary in these modes. Criterion 8 assesses whether the risk models consider communication between the vessel crew and other marine participants, such as other ships or manned structures. Criterion 9 assesses whether the risk models include considerations of personnel (e.g., different manning levels, different roles on board the ship, and operating the vessel). This is closely connected to the operational mode and LoA (C1) and communication aspect between operators (C4). The crew level (C9) dependends on the operational concept and may not be relevant for complete unmanned systems. However, it is important for low manned or partially unmanned systems.

# 5. RESULTS 

Table 3 summarizes the 64 reviewed models with the following information: accident type, object of analysis, model aim, modeling methods, model parameters, and data sources. With respect to the type of accident, 14 models cover collision and grounding, seven models focus on grounding or stranding (seven models), 28 models cover ship-ship collision, and nine models cover allision. Three models include both ship-ship collision and allision.

Table 3 Characteristics of the reviewed risk models. Abbreviations: accident types: CG - collision and grounding, G - grounding/stranding, SSC - ship-ship collision, A - allision; object of analysis: MTS - maritime transportation system, S - ship, ST - ship type, W - waterway; modelling techniques: AHP analytical hierarchy process, BBN - Bayesian belief network, BT - Bayesian theorem calculations, ETA - event tree analysis, F - fuzzy inference, FMEA failure mode effect analysis, FTA - fault tree analysis, GM - geometrical formulation, R - regression model, Sim - simulation, STPA - system theoretic process assessment; data source: AD - accident data, EJ - expert judgement HD - historical data, PD - published data, RT - real-time data.

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data
Source  |
(2007) | CG | W | Assess risk of piloted vessels in a harbor. | F | Observed frequencies of accidents, traffic flow, vessel traffic characteristics, and fairway characteristics | $\begin{gathered} \text { AD, } \ \text { HD } \end{gathered}$  |
(2008) | A | W | Assess effects of windfarms on the risk level in a waterway. | GM | Traffic flow, vessel traffic characteristics, fairway characteristics, technical failure, external assistance, selfrepair of technical failure, fail to anchor, vessel motion model, failure of navigational equipment, human error, weather, visibility, failure to warn vessel on collision course, and crew reaction time | $\begin{gathered} \text { HD, } \ \text { PD } \end{gathered}$  |
(described by
Friis-Hansen
(2008)) | CG | W | Framework to assess the risk in a waterway and decide on risk reduction measures. | BBN, GM | Traffic flow, traffic vessel characteristics, fairway characteristics, weather, RADAR performance, daytime, stress, alarms, officer of the watch (OOW) training and vigilance, propulsion failure, repair time, and bridge design | $\begin{gathered} \text { HD, } \ \text { PD } \end{gathered}$  |
(2008) | G | W | Model to assess the grounding risk in a waterway and assess risk reduction measures. | BT, FTA,
GM, Sim | Human error, sensor errors, position estimation/ measurement error, disuse of information, failure to use assistance, insufficient assistants provided, no/delayed assistants, maintenance errors, environmental constraints, material failure, inability to repair, unsafe winds and currents, vessel characteristics, and topography | $\begin{gathered} \text { HD, } \ \text { PD } \end{gathered}$  |
(2008) | SSC, A | MTS | Framework to assess the risk in a waterway and decide on risk reduction measures. | BBN, FTA | Crew and personal characteristics, compliance with rules, climate, automation and mechanical failures, maneuvering errors, traffic density, visibility, weather, sea state, and influences from operating organization | EJ, HD  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
(2008) | SSC | W | Assess the risk in a waterway and identification of risk reduction measures. | Sim | Traffic flow, vessel traffic characteristics, fairway characteristics, safety regulations, visibility, and wind | $\begin{gathered} \text { AD, } \ \text { HD } \end{gathered}$  |
Debnath
(2009) | SSC | W | Collision warning system for pilots. | R | Vessel size, day time, time to accident, and distance to accident | EJ, RT  |
(2009) | SSC | W | Collision warning system for pilots and VTS agents. | GM | Number of possible interactions, day/night time, ship density, vessel traffic characteristics, and waterway characteristics | $\begin{gathered} \text { EJ, } \ \text { HD, } \ \text { PD } \end{gathered}$  |
(2009) | SSC | W | Framework to assess the risk in a waterway and decide on risk reduction measures. | BBN, GM | Traffic flow and causation probability including human factors | $\begin{gathered} \text { EJ, } \ \text { HD, } \ \text { PD, } \ \text { RT } \end{gathered}$  |
Maturana
(2009) | SSC | W, ST | Incorporate human performance in risk assessment and assessment of risk mitigation for tankers. | BBN | Communication on bridge, communication with other vessel, human error of master and nautical officer, detection failure, wrong information available, failure in navigational planning, weather, sea state, visibility, concentration, personal factors, workload, RADAR detection, and alarm detection | EJ, PD  |
(2009) | SSC | W | Assess the risk in a waterway and decide on risk reduction measures. | Sim | Traffic flow, vessel traffic characteristics, fairway characteristics, vessel reliability, technical failure, communication/navigational aid failure, request for pilot or tugboat, visibility, current, hourly traffic variations, and fairway complexity | EJ, HD  |
(2009) | CG | W | Assess the risk in a waterway and decide on risk reduction measures. | Sim | Traffic flow, vessel traffic characteristics, human error, steering failure, propulsion failure, communication/ navigational equipment failure, mechanical/ electrical failure, tugboat/ pilot assistance, visibility, currents, and day time | EJ, HD  |
(2009) | CG, A | S | Generic standardized risk model for different ships following FSA procedure | $\begin{gathered} \text { Suggest } \ \text { BBN, FTA } \end{gathered}$ | Collision/grounding/ contact frequency model, flooding frequency model, survivability, model, time to sink model, evacuation model, environmental damage model | -  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
(described by
COWI
(2012)) | CG | W | Assess traffic development, the risk in a waterway and identification of risk reduction measures. | GM, Sim | Traffic flow, vessel traffic characteristics, seasonal variations, human and technical failure, effect of implemented risk-reducing measures, and training | HD  |
Goerlandt and Kujala (2011),
(Hänninen | SSC | W, ST | Assess traffic development, the risk in a waterway and identification of risk reduction measures. | BBN, Sim | Traffic flow, vessel traffic characteristics, weather, visibility, monthly/ daily/ hourly variations, technical reliability, management factors, human factors, support from VTS, and pilotage | $\begin{aligned} & \text { AD, } \ & \text { EJ, } \ & \text { HD, } \ & \text { PD } \end{aligned}$  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
(described by
Rasmussen et
al. (2012) | CG | W | Assess effects of constructions on the risk level in a waterway and assessment of mitigation measures. | GM | Traffic flow, waterway characteristics, vessel traffic characteristics, human failure (navigation, conducting evasive maneuver), technical failure (loss of propulsion, loss of steering), and repair probability | $\begin{aligned} & \text { AD, } \ & \text { EJ, } \ & \text { HD, } \ & \text { PD } \end{aligned}$  |
Roszkowska
and Smolarek
(2013) | SSC | W | Assess the probability of collision and suggest traffic separation schemes. | GM, Sim | Traffic vessel characteristics, traffic flow, probability of giving way to another vessel, and traffic rules | $\begin{aligned} & \text { HD, } \ & \text { PD } \end{aligned}$  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
Utne (2014) | G | ST | Framework to assess the influence of factors influencing fatigue on the risk level on a tanker. Predict crew performance and effects of mitigation measures. | BBN | Vessel types and characteristics, organizational influences, manning, safety culture and climate, work scheme, procedures, qualifications and certifications, communication, fatigue, season, type of fairway, weather, sea state, visibility, human error, and failure | $\begin{aligned} & \text { AD, } \ & \text { HD, } \ & \text { PD } \end{aligned}$  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
National Ship
Risk Model
(Nilsen
(2016) and
Haugen et al.
(2016)) | CG | W, S | Model for risk assessment and decision support for maritime regulation and management in Norwegian waters. | BBN | Regulations and policies, fairway characteristics, external navigational aids, market and economic conditions, work organization, human resource management, manning level, social measures, education and training, safety management system, organizational model, maintenance, resource management, crew characteristics, ship characteristics, communication, task load, bridge design, navigational system design, technical condition of navigational aids, propulsion system, steering system, and communication system (external) | $\begin{gathered} \text { EJ, } \ \text { HD, } \ \text { PD } \end{gathered}$  |

Type | Object
of
Analysis | Model Aim | Modelling
Techniques | Parameters in the Model | Data Source  |
Shafiee
(2017) | A | W, ST | Risk assessment and identification of mitigation measures of vessels navigating to offshore windfarms. | GM | Traffic flow, vessel characteristics, and collision ratio | EJ  |

The object of analysis refers to the target of the risk assessment. These are general maritime transportation systems (referring to any of the following systems), certain ship types, or specific waterways. Most reviewed models aim at risk assessment for a certain region or waterway (43). Six models aim at a specific ship type in a waterway (e.g., ferries in a harbor area (M1) or specific oil tanker traffic areas (M12, M25, and M47). Models for specific vessels are presented for generic maritime transportation systems (M7, M15 and M51), for general cargo ships (M23 and M36), and autonomous vessels (M45, M57, M64). The models addressing MASS are described and discussed in more detail in Section 5.

Most models aim to assess the risk level in a waterway and assess the effect of riskreducing measures, such as adapted traffic schemes and patterns. Some of these consider the change of the risk level through obstructions or structures, such as anchoring vessels (M36), bridges and structures (M4, M16, M46, and M62), offshore oil and gas platforms (M38, M44, and M60), or wind parks (M30 and M35). Only one model aims at the risk assessment of an MASS on a certain route, assessing the potential encounter frequency and probability of collision (M45).

The most commonly used modeling techniques and assessment approaches used in the risk models are geometric models ( 35 models), BBNs ( 24 models), and simulations (18 models). Less-used methods include the analytical hierarchy process (AHP, one model), Bayesian theorem calculations (three models), fuzzy inference (six models), event tree analysis (ETA, three models), failure mode and effect analysis (FMEA, one model), Fault tree analysis (FTA, 7 models), regression modeling (one model), and system theoretic process assessment (STPA). For detailed description of these methods, the reader is referred to the respective literature.

Data sources refer to the input for modeling and quantification of the models. Most

models use historical data (48 models), expert judgment (31 models), published data (30 models), or a combination of these. Few models are not quantified, due to their generic nature or the modelling approach (M15, M57, and M64).

Historical data includes information obtained through automatic identification system (AIS) data, VTS, or other records of shipping information. Expert judgment refers to parameters or probabilities that have been assessed and elicited by domain experts. In this case, published data refer to data on human and technical reliability found in the literature and the accepted values for the aforementioned causation probability. Eleven models primarily use accident data to assess the risk level, which is collected from accident and incident databases and reports. Such models are not yet directly applicable for MASS, since they will be operated differently and rely on different technical solutions. Only six models use (discretized) real-time information to assess the current level of risk. The next sections categorize the models, similar to the groups in Li et al. (2012), who reviewed ship risk models. The focus of the next sections is to generally ly describe the model types and assess their suitability for MASS general.

# 5.1 Modelling categories 

### 5.1.1 Models for Assessing the Risk in Waterways

Collision and grounding risk models for waterways are often based on geometric models. The probability of an accident ( P ) is derived through the multiplication of two parameters, the probability to encounter a vessel that will result in a collision if no avoiding measures are taken $\left(P_{a}\right)$ and the causation probability $\left(P_{C}\right)$, which represents the probability that no evasive maneuver is taken (Fujii and Shiobara, 1971; MacDuff, 1974).

$$
P=P_{a} \times P_{c}
$$

The encounter probability is in most cases based on the geometrical traffic distribution in the fairway. The overlap between different fairways is used to find $P_{a}$ for head-on

collisions. For overtaking or crossing collisions similar considerations have been presented. A summary of possible methods for calculating the encounter probability can be found, for example, in Kristiansen (2005) or Li et al. (2012).

The grounding frequency can be determined similarly. For coastal areas or areas with shallow water, the ship traffic density can be determined and multiplied with a causation probability (Pedersen, 2010). This is based on the considerations of MacDuff (1974) and Fujii et al. (1974). One differentiates between powered groundings and drift groundings (Mazaheri et al., 2014).

The causation probability summarizes considerations of vessel maneuverability, crew, equipment, etc. (Pedersen, 2010). The probability is often determined through BBN, ETA, or FTA, or a combination of these. These methods shall not be explained further. Both the encounter probability and causation probability may be derived from historical data on the traffic distribution in an area and the available accident data.

Models that fall in this category are M3-M5, M11, M16-M18, M26, M27, M30-M32, M34, M37, M41, M46, M48, M61 and M62. These models aim mostly at assessing the average risk in a waterway. They enable analysts to suggest regulatory measures for reducing the level of risk. Hence, these kind of models are not applicable to determine the level of risk of MASS, since MASS are not yet an integral part of the maritime traffic. In the future, these types of models need to account for MASS.

# 5.1.2 Causation probability models 

Some publications present only a model for the causation probability once a vessel is on collision course. These models employ mostly BBN, ETA, and FTA. The models aim in many cases at one ship type, a specific fleet or a specific ship. Some address specific factors, such as, fatigue (M36), human operator performance (M12), or operation in arctic areas (M63).

Models that fall in this category are M7, M12, M15, M36, M38-M40, M42, M51, M52, M56, M58, M60, and M63. Where M7 and M15 are generic frameworks for risk modelling of maritime transport systems. These models may provide some basis for risk modelling of MASS, since they model certain risk aspects with a high level of detail. However, the focus of the models may not always be adequate.

# 5.1.3 Simulation Approaches 

To determine the encounter probability and consequently the accident risk, simulations may be used. These models frequently use a causation probability, which is derived through BBN, ETA, and FTA. However, not all models used for deriving the causation probability are presented.

The simulations use AIS data and other ship traffic data to simulate the paths of ships and identify potential collision candidates. Simulations may also be used to assess the allision risk or the grounding risk. The models are useful when areas with regular sea traffic shall be assessed, such as harbor areas, ferry or tanker traffic. Models that use simulations are M1, M6, M8, M13, M14, M19, M20, M22, M24 M25, M28, M29, M33, M35, M47, M49, M54, and M59.

Simulations, in general, may be useful to model the risk of operating MASS. Especially, for MASS being employed in route traffic it seems to be a promising tool. Characteristics of the MASS can be modeled and the behavior of the control software may be implemented. Particular traffic operating on the MASS route may be assessed and critical situations identified.

### 5.1.4 Real-time decision support

Several models and approaches have been developed to give real-time decision support to ship navigators and VTS operators. These approaches use underlying risk models in combination with calculation of the nearest point of approach to identify possible

collision candidates. Models in this category are M9, M10, M21, M23, M44, M50, M55, and M61. These models may provide information to operators, however, they are not suitable for direct risk assessment for MASS. Such models do generally not model the ship in detail, since the focus lies on the surrounding vessels.

# 5.1.5 Other Risk Assessment Approaches 

Hu et al. (2007) (M2) used a fuzzy logic approach to the risk assessment of waterways. This may address uncertainties and probability ranges of scenarios. However, the model aims at specific waterways and hence their specific work has little relevance for MASS. Fuzzy logic, though, may be used to address the uncertainties in risk assessment of MASS.

Zaman et al. (2014) used a combination of FMEA and fuzzy logic to address the risk assessment of the strait of Malaga. They identify hazards for the strait and assess the magnitude of risk contribution. Hence, the knowledge gained from the model has few implications for MASS. However, the method may support the design of MASS. Nivolianitou et al. (2016) presented a BBN for assessing the risk of ships passing an area. The assessment is based on accidents statistics using characteristics of vessels that have been involved in accidents. Such an approach is not suitable for risk assessment of MASS, since it is reactive and based on the accident statistics, which do not exist for MASS. Wróbel et al. (2018) (M64) developed a STPA model to identify possible system hazards. The use of STPA reveals where control, through additional measures and functionalities is needed, to prevent the manifestation of hazards and consequently accidents. This model is further described in Section 6.

### 5.6 Parameters in the Assessed Ship Risk Models

This section provides an overview of parameters that have been used in the models. This corresponds to the second to last column in Table 3. This description forms the basis for

the assessment of the models against the criteria outlined previously.
Each model considers several parameters that influence the probability of an accident. However, the number of parameters that are considered varies from model to model. Some models only consider a few vessel and fairway parameters, while others consider and describe in detail technical, human, environmental, and organizational factors that are considered. Thus, Table 3 contains a summary of parameters that have been included in the different models to give a comprehensive and comparable overview of the models. These parameters are used to assess the models against the identified criteria. Traffic flow relates to the distribution of ship traffic over identified shipping lanes. The ship traffic is often Gaussian distributed. It contains information on the number of vessels passing a certain area, their trajectories and speed. Some models consider seasonal, daily, and hourly variations of the traffic flow. The traffic flow is often associated with the vessel traffic characteristics. These are the parameters of the vessels, such as ship type, length, width, and draught. Fairway characteristics refers to the dimensions of the waterway in question, in which the traffic is traveling. These are the length, width, and depth of the waterway and the spatial distribution of these. Several models split the fairway into several smaller segments to linearize meandering waterways. Geometric models make use of most of these parameters.

To be concise, environmental technical, human, and organizational factors that were similarly mentioned are presented in a summarized description in Table 3. For example, if human error was mentioned several times with respect to similar tasks (e.g., lookout), this is summarized as human error to avoid excessive repetition. Crew characteristics are used if several human and organizational factors were included (e.g., training, competence, experience, stress, alcohol consumption, tiredness, fatigue, etc.). With respect to environmental factors, weather describes the atmospheric environment. The

sea state describes waves and currents with the associated directions. Visibility is mentioned as a separate factor, although dependent on weather. The reviewed models cover different levels of technical factors. Some models include failure of subsystems, (e.g., propulsion or navigational aid failure). Other models include very detailed failures (e.g., RADAR failure). Table 3 attempts to reflect these differences.

# 5.7 Evaluation against the Criteria 

Table 4 shows the results of the model evaluation against the criteria. Four models had insufficient information to assess all criteria. This is indicated in the table. Some models were assessed as partly fulfilling the criteria C1, C2, C5 C6, C7, and C8. This was the case in which models included considerations similar to the ones in the criteria. However, not enough information was presented to assure that these criteria are met.

Criterion 1 is fulfilled by 21 models, through failure of navigation aids. However, this is not a very detailed analysis of software systems. One model (M42) was assessed as partly fulfilling the criterion since technical reliability was mentioned as a factor. However, it was not clear if this referred also to hardware and software reliability.

To assess C2, the models were checked for human error and associated ergonomic considerations, such as navigational aid failure. 13 models fulfill criterion C2 and an additional 19 fulfill this criterion at least partly.

Table 4 Evaluation of the selected models against the criteria described in Table 1. Abbreviations: I. I. - insufficient information, Y - Yes, N - No, P-Partly.


Twenty-four of the analyzed models fulfill C5 and include considerations for hardware, reliability, and maintenance. For C5, one model, M41 was assessed as partly meeting the criterion since only failure of the steering was mentioned.

C6 is addressed by six risk models. Three consider it partly, if the description of the events in the risk models indicated it, but did not explicitly model it. For the models fulfilling it, factors are included, such as, auxiliary systems.

Regarding C7, 14 models consider different operational modes. Most models consider different modes through the inclusion of pilotage or external assistance. Model M38 contains the autopilot as part of the considerations. Model M45 compares unmanned and conventional shipping and therefore includes different operational modes.

Only six models fulfil C3. Criterion 4 is fulfilled by 12 models. Ten models address C9. Ten models fulfilled six or more criteria. These are M7 (Trucco et al., 2008), M24 (Goerlandt et al., 2012; Goerlandt and Kujala, 2011; Hänninen and Kujala, 2010), M41 (Tvedt, 2014), M44 (Jensen, 2015), M45 (Khaled and Kawamura, 2015), M50 (Mazaheri et al., 2016), M51 (Haugen et al., 2016; Nilsen, 2016), M57, M58 (Hassel, 2017).

# 6. DISCUSSION OF THE MOST PROMISING MODELS 

Wróbel et al. (2018) (M64) used STPA to identify possible causes and contributors of the different system functions to system hazards. Almost all criteria, except for C4, which covers the interaction between operators are covered by Wróbel et al. (2018). The STPA method may be an important tool for the design and evaluation of MASS. STPA has also been used on for the assessment of dynamic positioning systems of ships to derive verification goals and identify hazards (Rokseth et al., 2016, 2017).

Wrobel et al. (2016) (M57) used a BBN to assess the risk level of MASS with respect to several possible accidents (collision, grounding, foundering, fire, or cargo related accidents). The BBN is divided into three levels. The first level represents the risk in

relation to the aforementioned accidents. The second level summarizes possible initiating events, these are related to navigation, engineering, stability and buoyancy or miscellaneous. The third level summarizes causes to the accidents. Five main groups are identified; alerting, control algorithms, external information quality, maintenance regime, and sensors' performance. The groups and their possible inclusion are not further described or developed, and the model is not quantified.

Wrobel et al. (2016) address several important issues with their model. Therefore, it may form a suitable basis for further development. However, assessing several accident types in one model, may be a major challenge, since a variety of risk influencing factors may interact in different ways for different accidents.

Jensen (2015) presented a risk assessment (M44) for a prototype unmanned bulk carrier using ETA and FTA, following the FSA process. In addition to ship-ship collisions, foundering of the vessel is investigated. The models are used to compare conventional with autonomous operation. Therefore, the models have been specifically developed for autonomous ships. Communication between the members of the SCC crew is not included, and human factors are only considered for the manned case. However, human factors should be included in a revised version of the model for remote control. The collision encounter probability is assessed with geometric models based on the International Association of Marine Aids to Navigation and Lighthouse Authorities (IALA) Waterways Risk Management Program (IWRAP) Mark 2. This may be a good starting point to assess the possible encounters on a long voyage route. However, simulations to assess the possible encounters may be more suitable in areas where traffic patterns vary strongly during a day or for traffic on a specific route (Li et al., 2012). Overall, the models in M45 outline well how a risk analysis may be structured using FTA and ETA. The presented models include high-level function failures of the equipment,

engine, steering, software, and hardware. For a real system, these function failures need to be modeled in more detail to represent the ship and its particulars. The models lack detail in terms of the control system components. However, these are essential parts of a MASS and need to be considered.

Trucco et al. (2008) presented a general framework (M7) for risk assessment of maritime transportation systems. A BBN is used to model the interaction of human, organizational, and technical factors, which influence the basic event probability of fault trees. The fault trees are used to assess the probability of accidental events. As a case study, Trucco et al. (2008) assessed the collision probability of a high-speed vessel. They consider three elements leading to a collision: human errors, automation and mechanical failures, and maneuvering errors.

The modelling framework developed by Trucco et al. (2008) seems appropriate as a starting point for the development of risk models for MASS. The interaction between different risk influencing factors is an important contributor to the level of risk and may be captured through BBN. The accidental chain of events can be modelled through FTA. Hence, such a framework, together with the framework by Vanem et al. (2009), could be considered as basis for the development of the risk models.

Tvedt (2014) presented a risk assessment framework (M42) for allision scenarios between an offshore supply vessel and an offshore platform. Three scenarios were identified. Tvedt (2014) used ETA to model the chain of events in the identified scenarios. Failures of mitigating barriers are modeled with FTA. The basic events in the FTAs are assessed by BBNs, including human and organizational factors that influence the level of risk. These factors are identified from different sources and include a wide range of considerations, such as HMI usability, training, communication, personal factors of the crew, maintenance, reliability, and manning. The model is not quantitative and is limited

to an offshore supply vessel approaching an offshore platform. Similar methods are used as suggested by Trucco et al. (2008) and especially the operator model seems promising to transfer to a risk model for MASS. The model itself, due to its focus on offshore platforms cannot be transferred to the case of MASS. However, the models in the scenarios may need adaptation to account for MASS in the future.

Mazaheri et al. (2016) developed a BBN (M51) for the assessment of grounding probability of a marine traffic system, such as a vessel, vessel type, or a certain waterway. Mazaheri et al. (2016) based their model on incident and accident reports and earlier models. This makes the model generally unsuitable. In addition, the model does not provide further guidance on how the factors in the BBN may be assessed with respect to their not available data or for other ship systems.

Goerlandt et al. (2012), Goerlandt and Kujala (2011), and Hänninen and Kujala (2010) (M25) presented models to assess the risk associated with tanker collisions in a waterway; hence, it treats the ship parameters rather superficially and is only limitedly suitable to assess the risk level of the ship. Goerlandt et al. (2012) presented the overall methodology for risk assessment, using simulation including ship particulars, route information, departure time, and speed, following Goerlandt and Kujala (2011) and Hänninen and Kujala (2010) for the assessment of the collision frequency. Goerlandt and Kujala (2011) assessed the encounter frequency of vessels in a specific waterway. Hänninen and Kujala (2010) presented the model for assessing the causation probability. The causation probability represents evasive maneuvers by the two vessels and is assessed through a BBN. Hänninen and Kujala (2010) included several technical, human, environmental, and organizational factors. The approach may be further developed or used as guideline to assess the risk level of MASS operating in waterways.

Hassel (2017) assessed the allision risk (M60) for offshore oil and gas platforms. The

BNN model focuses on both aspects related to the platform and the ship on collision course. Similar to M42, M60 addresses the allision risk from the perspective of the offshore platform. Hence, the model may need to be adapted, to assess the change of the allision risk level of offshore platforms by MASS. All aspects of communication (C3, C4, and C8) are covered. Model 60 may be used as guideline, how these aspects can be included in a BBN model for MASS.

Khaled and Kawamura (2015) assessed the collision risk (M46) in a harbor area. They used the geometric model implemented in IWRAP (Friis-Hansen, 2008) to assess an encounter frequency and combine it with an adapted BBN to assess the causation probability. The BBN includes, among others, environmental factors, personal factors of crew members, human error, and technical reliability of navigational equipment and communication equipment. Khaled and Kawamura (2015) included considerations that are relevant for operation of MASSs. However, they are covered only superficially since the model was made for risk assessment of waterways. Since the model is designed for harbor areas, it may provide input for assessing the risk level of MASS when approaching ports.

Model 52 is the Norwegian national ship risk model (Nilsen (2016); Haugen et al. (2016)). The model was developed for the risk assessment and implementation of risk reduction measures in Norwegian waterways. The model does not consider different operational modes and communication between vessel operators. Only the detailed model for groundings is available; hence, these considerations might be included in a collision model. Since the model focuses on waterways and is based on historical data for incidents and accidents, it is not suited to demonstrate safety compliance of MASS. The model and work around the model include different ship types and their risk levels MASS may be included in the future.

In summary, the literature provides some suggestions for the conduction of risk assessments for MASS. The STPA methods seems to be suitable tool for analyzing possible hazards and proposing risk reduction measures.

Some of the analyzed models focus on specific waterways and locations. The different foci result in various aspects that are included and highlighted in the models. To demonstrate a sufficiently low-risk level of an MASS, it is necessary to model its behavior and particulars in detail, which may require risk modelling from different risk perspectives on the MASS.

In some cases, a quantitative assessment is necessary, to show that the risk level has been addressed by suitable measures. Models that are used currently for the risk assessment of conventional ships, may provide insight into how a model could be developed. Building risk models of MASS may find a starting point in risk models for conventional ships. However, the risk influencing factors in the models and their quantification need to be elicited for the MASS case.

Areas that need special attention, for example, software, and remote control and associated human operator considerations, are rarely covered in depth. Different approaches are needed to include these considerations in risk models for MASS.

# 7. CONCLUSION 

This article reviews current risk models for ship collisions and groundings, which have been presented in the literature since 2005. The 64 analyzed models mainly aim at assessing the ship collision frequency, grounding frequency, or frequency of allisions in a certain waterway or geographical area. Most models use a geometrical modeling approach, often in combination with other modeling techniques, to determine the frequencies or probabilities of the accident. Models aiming at risk assessment of a waterway treat ships superficially with respect to relevant factors, such as technical

equipment and its reliability. Hence, such models are not applicable to demonstrate the risk level of a ship.

Nine criteria are used to assess the identified relevant risk models with respect to their applicability to MASS operation. A systems engineering approach was used to identify the criteria. The criteria cover relevant aspects for the operation of MASS: component and subsystem redundancy, different operational modes, HMI, communication among different involved actors, technical reliability, maintenance, software reliability and manning. These criteria cover a broad range of aspects since the current concepts for MASS vary among each other, which does not allow for a more detailed system evaluation.

Ten models fulfill six or more criteria. These were investigated more closely. Seven models that were closely investigated in this article are based on conventional ship operation. The operation of MASS will be different from conventional ship operation. Technical reliability, software reliability, and the situation awareness of the operators become even more important in MASS. The models developed for MASS address most relevant issues. However, due to the lack of certainty on design and operational concepts, these models are rather superficial. No models can be defined without concrete operational concepts and clear system definitions which makes an in-depth analysis and assessment of the reviewed models difficult.

The evaluation presented in this article shows that some of the current conventional ship risk models and the underlying frameworks could be used as a starting point for developing risk models for MASS. The structure and considerations included in the models should be further considered regarding risk modeling of MASS.

The quantification of ship risk models traditionally is based on accident and incident data, but such an approach is not yet applicable for risk models of MASS. Hence, expert

assessments and test data need to be derived and used if a quantified risk assessment is attempted.

One issue that all the analyzed models have in common (except for M57 (Wrobel et al., 2016) and M64 (Wróbel et al., 2018)), is that they do not include the communication connection with a shore base. This is one of the main requirements for MASS, that they can be remotely controlled and supervised. Even if MASS has a minimal crew on board, part of the vessel will be highly automated, and situation assessment requires a robust communication line between the vessel and competent personnel on shore.

Seven of the ten models discussed in more detail have one aspect in common; they use BBN for at least as part of the risk model. Only Jensen (2015) and Wróbel et al. (2018) do not use a BBN. Hänninen (2014) highlighted the usability and usefulness of BBNs for maritime safety management. With the flexibility of the modeling method and the input from experts, it is possible to build risk models for MASS operation. Hence, BBNs should be considered part of a risk model for MASS operation. A systems engineering approach might benefit the development of such a risk model in identifying comprehensive system requirements.

A dedicated MASS risk model should focus on the assessment of the control and software system and the effects of its failure. Current models do not consider this aspect. Dedicated methods for assessment of software failure and control systems need to be applied. Currently used modeling techniques in the ship risk models are not sufficient since software behaves deterministically (Chu et al., 2009). Methods that may be used could be, among others, STPA (Leveson et al., 2012), or the Functional Resonance Analysis Method (Hollnagel, 2012), which has been already employed in accident investigation of maritime accidents (Tian et al., 2016).

Other aspects that need more attention in the future are the interactions between

conventional and autonomous ships since MASS will not replace all maritime vessels in the foreseeable future. Further investigation should include the effects of MASS on traffic patterns. The methods relating to the geometrical analysis of collision frequency might need to be adapted to new traffic patterns. In addition, permanent navigational aids along the coast and in waterways may need to be changed to facilitate navigation of MASS. Current aids, such as navigational lights and buoys, assist the human navigators using RADAR or similar equipment with visual perception for verification. This is also an area that needs to be further investigated and that may affect the risk related to MASS.

# ACKNOWLEDGMENTS 

The authors want to thank the two anonymous reviewers, who made valuable comments on an earlier version of this article and helped to improve it.

## FINANCIAL SUPPORT

I. B. Utne and C. A. Thieme appreciate the support of the Research Council of Norway through the Centres of Excellence funding scheme, Project number 223254 - NTNU AMOS.
