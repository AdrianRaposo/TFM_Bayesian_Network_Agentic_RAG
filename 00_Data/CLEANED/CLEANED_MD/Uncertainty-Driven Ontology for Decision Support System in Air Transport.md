# Article 

## Uncertainty-Driven Ontology for Decision Support System in Air Transport

Carlos C. Insaurralde ${ }^{1, *}$, Erik P. Blasch ${ }^{2, * *}$, Paulo C. G. Costa ${ }^{3}$ and Krishna Sampigethaya ${ }^{4}$

## check for updates

Citation: Insaurralde, C.C.; Blasch, E.P.; Costa, P.C.G.; Sampigethaya, K. Uncertainty-Driven Ontology for Decision Support System in Air Transport. Electronics 2022, 11, 362. https://doi.org/10.3390/ electronics11030362

Academic Editor: Jose Eugenio Naranjo

Received: 7 December 2021
Accepted: 13 January 2022
Published: 25 January 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Bristol Robotics Laboratory, Bristol BS16 1QY, UK
2 MOVEJ Analytics, Dayton, OH 45324, USA
3 Department of Systems Engineering and Operations Research, George Mason University, Fairfax, VA 22030, USA; pcosta@gmu.edu
4 Cyber Intelligence and Security Department, Embry-Riddle Aeronautical University, Prescott, AZ 86301, USA; sampiger@erau.edu

* Correspondence: carlos.c.insaurralde@gmx.com (C.C.I.); erik.blasch@gmail.com (E.P.B.)

Abstract: Recent electronics advances for air transport have increased aircraft density, volume, and frequency in the airspace. These advances come with control requirements for precise navigation, coordinated Air Traffic Management (ATM) or Unmanned aircraft system Traffic Management (UTM), and proactive security. The tight tolerances of aircraft control necessitate management of spatial uncertainty, timeliness precision, and confidence assessment, which have, respectively, variance, reliability, and veracity situation awareness and assessment metrics. Meeting such airspace requirements involves the ability to evaluate how those metrics impact ATM/UTM operations, making the complex interrelationships between them a key aspect for coping with the fast worldwide growth of air transport. To support such growth, ontologies have been proposed as a promising technology for making such interrelationships explicit, while facilitating communication between avionics devices. This paper investigates the use of ontologies in support of electronic ATM/UTM operations, highlighting the use of Uncertainty Representation and the Reasoning Evaluation Framework (URREF) in realizing the ability for Air Traffic Controllers (ATCs) to semantically communicate with aircraft operators concerning physical airspace coordination. Using Avionics Analytics Ontology (AAO) endowed with the URREF, application examples based on two airspace situations are presented. Example results for northeast coast of Brazil atmospheric volcanic ash as well as for the Eyjafjallajokull volcano eruption show a $65-80 \%$ success in providing warnings to ATCs for airspace control. The paper demonstrates that an ontology-based UTM enhances the capability and accuracy of an ATM to suggest rerouting in the presence of remarkably deteriorated weather conditions.

Keywords: Bayesian Networks; decision support system; situation awareness; knowledge engineering; avionics analytics

## 1. Introduction

The explosion of potential aerospace platforms, including unmanned aerial vehicles (UAVs), electric vertical take-off and landing (eVTOL) aircraft, and autonomous air parcel delivery (AAPD) networks, requires advanced large-scale processing methods, such as ontological analytics. Recently, many electronics systems have been using formal ontologies to support database analysis, knowledge aggregation, and graphical methods [1]. One prominent example is the use of Decision Support Systems (DSSs) utilizing societal data, sensor measurements, and electrical equipment, as shown for smart applications in the healthcare and electrical markets [2,3]. The integration of smart avionics includes the interaction between electronic equipment supporting Air Traffic Management (ATM), Unmanned Aerial Systems Traffic Management (UTM), and a Human-Machine Interface (HMI). The HMI requires decision support taxonomies from which automation/autonomy scales, trust management techniques, and credibility assessments align with an ontology [4].

An avionics example includes aircraft conflict prediction using advances in machine learning [5], from which an ontology provides decision-support explanations based on physical, environmental, and social meaningful semantics [6].

New generations of ATM systems, such as the Federal Aviation Administration (FAA) Next Generation Air Transportation System (NextGen) [7] and the Single European Sky ATM Research (SESAR) system [8], have a particular interest in incorporating ontologies to evolving ATM approaches [9]. However, none of the current ontology-based approaches for ATM provide decision-making support, and there are very few related works reported from research groups and relevant avionics companies. Therefore, the main contributions of this paper are an avionics ontological Decision Support System (DSS) that:

- facilitates the interaction between aviators and ATM controllers to make complex decisions in the context of data, features, and information uncertainty;
- provides analytical support between physical sensor measurements and situation awareness concepts of interest to human agents; and
- demonstrates the usability of the Avionics Analytics Ontology (AAO) to support the growing data space for urban air mobility challenges of UAVs, eVTOLs, and AAPDs.
An avionics DSS, incorporating ontologies, mitigates unprecedented ATM challenges such as progressively sophisticated systems, densely occupied airspaces, and inexorably adverse weather conditions that overwhelm aircraft pilots, air traffic controllers, and air transport businesses, which prioritize safety and security in aviation procedures while sharing the airspace with ultimately pervasive Unmanned Aerial Vehicles (UAVs). The new paradigm of a shared airspace demands clear rules and procedures for unmanned aircraft system Traffic Management (UTM) [10]. Following the direction of performance assessment for man-machine airspace coordination, a proof-of-concept Avionics Analytics Ontology (AAO) has been proposed and demonstrated in various scenarios [11].

This paper integrates the Uncertainty Representation and Reasoning Evaluation Framework (URREF) into the AAO to improve the DSS effectiveness for ATM/UTM [12]. The URREFAAO integration is meant to endow the AAO with semantic uncertainty for the input information (meaningful data from sensors). In particular, the proposed DSS deals with information credibility as an important URREF input criterion. The URREF-enriched AAO (1) captures information on concepts, entities, and relations; (2) utilizes pedigree input uncertainty information through metadata information for SDF; and (3) focuses on including veracity as a subclass of credibility [13] for avionics applications. The URREF-AAO is aligned with the modern time-critical and safety-critical aeronautical systems as instances of a Cyber-Physical System (CPS) [14,15]. The cyber-physical AAO-based DSS ultimately enhances Situation Awareness (SAW) and Situation Assessment (SA), as well as Situation Understanding (SU) in information fusion [16]. The approach presented in this paper expands the research previously presented [11] by endowing the AAO with veracity metrics (probabilistic uncertainty) based on Bayesian Networks and the URREF.

The rest of the paper is organized as follows. Section 2 presents an ontology need for ATM applications that incorporates multisource data for information fusion, including an introduction to the URREF with a focus on veracity as a quality factor (credibility). Section 3 discusses an analysis of Cyber-Physical Air Transport (CPAT) by assessing the current trends in CPSs, methods for ATM, and considerations for the future airspace networks. Section 4 offers an overview of the AAO, along with the realization of the URREF to support semantic uncertainty. Section 5 explores application examples of the AAO-based DSS proposed in this paper for ATM/UTM systems. The final section provides the conclusions and future research direction.

# 2. Information and Uncertainty Management 

This section presents the need for an ontology for ATM applications that incorporate multi-source data for information fusion.

# 2.1. Information Fusion 

Many current engineering systems are evolving to include the coordination of lowdata sensors, such as the Internet of Things (IoT), that enable coordination in a CPS-such as air traffic management (ATM). A CPS-IoT ATM interaction aligns with information fusion, situation analysis, and decision-making support. Information fusion combines data from multiple sources to reduce uncertainty (e.g., spatial, temporal, and frequency). The information fusion community distinguishes between low-level information fusion (LLIF) and high-level information fusion (HLIF). LLIF includes sensor measurement processing for registration, navigation, and recognition, as exemplified by the Kalman filter. HLIF seeks situation/threat assessment and sensor management. The coordination of LLIF and HLIF includes elements of situation understanding, user refinement, and mission goals. Recent efforts in the avionics community have leveraged information fusion for data analytics to improve ATM, UTM, and System Wide Information Management (SWIM) [17].

Other communities have presented use cases for ontologies such as NASA's ontologybased framework for ATM. The NASA framework aims to bring together diverse aeronautical data for research purposes to coordinate developments that could support airspace management [18]. The purpose of ATMonto (NASA ATM ontology) is to support ATM by including flight data, aircraft, airports, ATM initiatives, surface and meteorological weather component, airspace components, and departure/arrival routes [19]. Additionally, the NASA ontology is based on available data versus adding techniques to reason over the data, such as for uncertainty reduction when real-time reported data conflicts with the prescribed ATM understanding. Hence, there is a need to expand the ontology towards reasoning over challenging situations that require information fusion.

Information fusion seeks to combine data to produce information. Data can come from a variety of sources, such as sensors [20], environmental context [21], and models [22]. The purpose of data fusion is to reduce uncertainty and consists of three methods: correlation, association, and filtering. Correlation resolves data in time and space to not only register the data but also to organize data of the same type. Association determines which data relates to another set of data. Finally, filtering uses a model and the associated correlated data to reduce the uncertainty and predict the next likely location of future data measurements [23]. In many cases, the uncertainty is associated with physical data; however, there is a growing acknowledgement of the need to present that data to a user with semantic understanding [24].

### 2.2. Semantic Uncertainty Representation

The URREF ontology [25] enhances avionics analytics, and updates are available at http://eturwg.c4i.gmu.edu/ (accessed on 5 December 2021). The URREF has been developed by the International Society of Information Fusion (ISIF) Evaluation of Technologies for Uncertainty Representation Working Group (ETURWG), from which hundreds of examples are reported. Other applications URREF has supported include sensor imagery [26], target detection [27], and decision trust [28]. Inherently, the URREF ontology of uncertainty metrics supports information management and consists of four criteria: data, reasoning, data handing, and representation, as shown in Figure 1. The key elements of data quality issues of accuracy, precision, and veracity are within the data handling criterion. While accuracy and precision have been previously explored, veracity warrants further exploration for avionics applications.

Veracity is an element (dimension) of Big Data. Other big data elements include validity, volatility, veracity, velocity, variety, volume, and sometimes vividness [29]. Typically, velocity, variety, and volume are associated with streaming data (e.g., flight data) along with veracity. Veracity refers to the biases, noise, and abnormality in the data. Thus, avionics data indexing, storage, and retrieval should have meaningful (e.g., high veracity, relevant, etc.) constructs to answer queries to the problems being analyzed [30]. Precise data reduces user workload and enhances situation awareness [31]. To the best of our knowledge, very few papers discuss veracity data source analysis. Hence, the paper

attempts to bring together the URREF, big data, and veracity assessment as an example for avionics-domain analysis.
![img-0.jpeg](img-0.jpeg)

Figure 1. URREF Categories.
Using the current definitions from the URREF (Table 1), precision, accuracy, and veracity are elements of the ontology.

Table 1. URREF Data Criterion: Quality.


Veracity has three main dimensions: (1) objectivity/subjectivity, (2) truthfulness/deception, and (3) credibility/implausibility. Information quality requires uncertainty management. Content management includes quantifying the levels of content objectivity, truthfulness, and credibility [34]. In what follows, the paper describes avionics and veracity within the URREF.

The Merriam-Webster dictionary defines veracity as truthfulness, or conformity with truth or fact. To compare to "truth", the related metrics presented in Table 2 provide corresponding information in terms of the True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN) of a system's output for $n$ samples, where the expert interpretation is considered to be the ground truth. For example, assuming the flight data is objective, the credible results are used from data exploitation. Table 3 gives metric averages computed over the flight data duration, which is the "quality" information such as precision, recall, accuracy, and veracity (e.g., error) in the URREF ontology. As can be seen, recall and accuracy are higher, while precision and veracity are lower. Precision measures the relevant-to-retrieved instances of the model, while recall is relevancy over all instances of a model-to-label instance. Recall is important so as to not miss-label a false negative, whereas precision is good to catch anomalies. Thus, an ontology helps to balance whether a flight is off course or has a cyber-attack (precision), while at the same time determining the potential hazard if it is off course or the type of attack (recall).

From the analysis, $A$ is the accuracy, and the error $(E)$ could be a measure of veracity in relation to whether the source assessment of what is true. The results correspond to all changes of a flight (e.g., entrance and exit) over a planned route. Further analysis of veracity will help to refine the URREF ontology.

Table 2. Definition of Metric Equations.


Precision $(\mathrm{P})=\mathrm{a} /(\mathrm{a}+\mathrm{b})$; Recall $(\mathrm{R})=\mathrm{a} /(\mathrm{a}+\mathrm{c})$; Error $(\mathrm{E})=(\mathrm{b}+\mathrm{c}) / \mathrm{n}$; Accuracy $(\mathrm{A})=(\mathrm{a}+\mathrm{d}) / \mathrm{n}$.

Table 3. URREF Metrics over Sample Videos (E could be veracity).


The URREF has been widely used to combine human-derived semantic understanding with that of physics-based analysis. Initial discussion on the URREF focused on humanmachine teaming [33], from which data fusion approaches to combine results utilized Bayes Nets [35]. Dragos and Ziegler [36] incorporated the URREF in a cyber threat model for air traffic control (ATC) workplace analysis. Another transportation application of the URREF is for maritime awareness where Camossi and Jousselme [37,38] developed methods for Automatic Identification System (AIS) analysis for sensing and monitoring, which is similar to the air traffic use of the Automatic Dependent Surveillance-Broadcast (ADS-B). Recent applications of the URREF include formalizing trust in reporting that can be aligned with NOTAMS as well as methods by Laudy and Dragos [39] for urban traffic control. Together, the URREF is broadly applicable to transportation analysis for situation awareness over traffic for space, air, ground, and maritime domains and systems.

# 3. Cyber-Physical Air Transport 

This section presents an analysis of Cyber-Physical Air Transport (CPAT) by assessing the current CPS trends, ATM methods, and future airspace network considerations. CPS is an extension of Dynamic Data Driven Applications Systems (DDDAS) [40,41]. Hence, while CPS focuses on edge data analytics for real-time monitoring, DDDAS includes models of the physical environment for real-time and what-if monitoring from streaming data and augmented data from models.

A CPS consists of, and depends on, the close interaction and integration of physical domain measurements, computational and software systems, a networked environment, and controlled actuations [14]. Likewise, an IoT focuses on distributed sensor data, wireless networks, and a physical environment (Figure 2) [42]. A key part of today's developments in CPS and IoT involves creating new capabilities that afford adaptability, scalability, usability, security, and privacy. Furthermore, information fusion advances are critical to safely and beneficially connect people and the physical world with emerging CPS and IoT instances.

CPS/IoT applications are many, e.g., healthcare, automation, smart cities, manufacturing, and mobility/transportation, all utilizing information fusion, active sensing, decision-making, intelligence, and collaboration [43]. Coordinating CPS-IoT requires appreciation of challenging environments, cyber-physical security, communications, networking, and human-machine integration. For these reasons, CPS/IoT methods have a high possibility to transform commercial and societal endeavors. Current avionics themes include: (1) situation awareness, (2) intelligent transportation, and (3) network communication (see Table 4).

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Cyber-Physical System (CPS) with Internet-of-Things (IoT) sensors.

**Table 4.** Summary CPS constructs and methods in aviation.


EMI—ElectroMagnetic Interference [28], SCADA—Supervisory Control and Data Acquisition, Inertial Navigation System (INS) with the Instrument Landing System (ILS).

Future ATM systems must manage a multifold increase in aircraft with a diverse set of capabilities, such as avionics for communications, navigation, and cockpit management [44]. Figure 3 (left) presents the networked communications between aircraft and with a ground infrastructure [15]. Dangerous weather, e.g., atmospheric and solar conditions, as well as human-actuated threats, e.g., crew fatigue and terrorism, pose severe performance risks in airspace and airport environments. Each aircraft must be capable of flying trajectories that are optimized under these operational conditions, evolving priorities of operators, and dynamic constraints of air traffic control and airports. Modern aircraft can achieve these capabilities via a cyber–physical integration of their avionics and with off-board systems.

Figure 3 shows a CPS view of a next-generation ATM system with modern aircraft as mobile agents, communicating between themselves and off-board systems for ATM operations [17]. In such a large-scale CPS, each aircraft can be considered as a sensor system composed of diverse onboard sensors, an actuator system composed of networked onboard actuators, and an onboard controller (not shown in Figure 3) receiving sensor feedback and transmitting actuation commands. As shown in Figure 3, these aircraft can collaborate as a

dynamic multi-layered sensing system, or even as an IoT, that monitors their environments, a dynamic multi-layered actuator system that controls their physical behaviors, and a dynamic multi-layered control system that optimizes system performance. These aircraft operating in the physical world connect to the cyberspace via satellite, airborne, and terrestrial links and a ground infrastructure operated by stakeholders such as airports, air traffic control, and airlines.
![img-2.jpeg](img-2.jpeg)

Figure 3. Illustration of a future airspace shared by different aircraft envisioned as a CPS/IoT.
Within the illustrated CPS/IoT view of ATM systems, cyber-physical interactions can include satellite-based aircraft navigation, trajectory-based flight operation, aircraft position data sharing, automated controller and pilot data link exchanges, and a global information network of real-time air traffic control and meteorological data [15]. Nevertheless, the enabled CPS/IoT interactions are intended to help flight deck crews and air traffic controllers see the same real-time "picture" of airspace on their respective screens, including air traffic and weather conditions. The future includes command-guided large-scale CPS in support of air-space coordinated control [45]. Ultimately, stakeholders-both airborne and ground-based-and society, in general, must interface with the complex CPS/IoT instances.

Uncertainties in a CPS/IoT instance can emerge from cyber-physical threats. This is a new spectrum of security threats resulting from attacks that exploit states and events in cyber assets, physical assets, or both, and couple them with unanticipated system operations to place the system in an unsafe state or a state from which recovery is difficult and expensive [46,47]. Because correctness and timeliness are fundamental properties of a tight cyber-physical integration, uncertainties causing unexpected anomalies and delays can potentially result in costly, if not catastrophic, consequences for aviation stakeholders and society.

Hence, for the CPS/IoT instantiations of ATM, it is critical to assure that the system integrity and safety exist in the event of malfunctions, or that unforeseen events impacting the system availability are both assured, and to guarantee timeliness and correctness of data for ATM operations. It is vital to account for the underlying information-based control flow between cyberspace and physical world, where cyber components consume information from the physical world and in turn affect the behavior of the physical world. A promising high-level approach for cyber-physical security is to make cyber and physical components aware of their decision impacts on one another and make cyber and physical components capable of sensing and responding to emerging challenges in the other [15].

## 4 Uncertainty-Aware Ontology for Avionics Analytics

This section presents an overview of the AAO, along with the realization of the URREF to support semantic uncertainty.

### 4.1 Avionics Analytics Ontology

Knowledge can formally be represented by means of Description Logic (DL) [48]. The AAO syntax is built upon symbols and rules aligned with the DL syntax structure. Its realization is based on the Ontology Web Language (OWL) [49] by means of the Protégé tool [50]. The OWL allows the AAO to define, specify, and describe classes (concepts), properties, and instances of classes (individuals), as well as axioms (statements).

The main AAO classes are:

- **Aircraft** (as a subclass of Vehicle): any type of aircraft falls into this category, including manned and unmanned fixed-wing or rotary-wing air vehicles;
- **Route**: all the air corridors (as a collection of waypoints) for different airspace regions for aircraft fall into this category, which are defined by departure point to arrival point. However, no specification of waypoints is required for this first version of AAO;
- **Airport** (as a subclass of Aerodrome): all the aerodromes mostly for commercial air transport fall into this category. They are distinct from aviation airfields and military airbases;
- **Runway**: any runway from aerodromes falls into this category. Runways have an identification code;
- **Status**: the class "Status" in the AAO is only defined to define the condition of runways;
- **Airspace**: any aerial region above a territory (portion of the atmosphere) controlled by a country;
- **Weather**: all weather conditions fall into this category;
- **Criteria**: the criteria defined in Section 5.2 is notated in this category;
- **Radar**: all types of radar used in aeronautics falls into this category;
- **Metrics**: the metric assessment as defined in Section 5.2 falls into this category.

Figure 4 shows the classes of the AAO and there is-a relations.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Avionics Analytics Ontology (AAO) Classes.

Table 5 presents AAO classes, examples of their instances, and some properties associated to them.

Table 5. AAO Components.


The AAO allows for the definition of axioms by means of restrictions based on properties and is applied to classes and individuals. The AAO has two types of axioms: terminological axioms and assertional axioms. The former, grouped into what is called TBox, are particularly based on operators, such as those for inclusion and equivalence. The latter, grouped into what is called $A B o x$, are a set of facts or assertions. The $A B o x$ and the $T B o x$ are the building blocks for the AAO knowledge base. Examples of axioms from the TBox and the ABox are shown in Figures 5 and 6.

Aircraft_A subclass of (Aircraft and (hasRoute only Route_C))
AircrafttobeDiverted subclass of Aircraft
Route_C subclass of (Route and (hasLanding only Airport_I) and (hasAirspace only Air-space_IV))
Diverting subclass of Route
Airport_I subclassof(Airport and (hasRunway only (Runway_IB)
NoLandingAirport subclassofAirport
Runway_IB subclass of Runway and (hasStatus only Available)
AvailableRunway subclass of Runway
Airspace_IV subclass of (Airspace and (hasWeather some Tornado))
FlyingAirspace subclass of Airspace
Figure 5. Examples of Terminological axioms (TBox) from the AAO.
AircrafttobeDiverted equivalent to Aircraft and (hasRoute only Diverting)
Diverting equivalent to (Route and (hasAirspace some NoFlyingAirspace))
NoFlyingAirspace equivalent to (Airspace and (hasWeatheronlyVeryBadWeather))
VeryBadWeather equivalent to (Weatherand (HurricanorTornadoorMassivePressipitation))
MassivePrecipitation equivalent to (hasExtremeWeather some $>60$ ) and (hasHeavyWeather some
$>20$ ) and (hasModerateWeather some $>10$ ) and (hasLightWeather some $>10$ ))

Figure 6. Examples of Assertional axioms ( $A B o x$ ) from the AAO.
A reasoner is a cognitive engine for ontology queries that can be applied to the above OWL-described AAO. It checks semantic consistency on the AAO and applies inference rules. The execution of reasoners on the AAO takes place to provide answers to logical

query questions by doing deductions from axioms defined in the AAO. Figure 7 shows examples of inferred classes (when applying a reasoner to the AAO).

Aircraft_A subclass of (AircrafttobeDiverted and AircraftcanLand)
Airspace_IV subclass of NoFlyingAirspace
Tornado subclass of VeryBadWeather
MassivePrecipitation subclass of VeryBadWeather
Figure 7. Examples of inferred classes.

# 4.2. Veracity Assessment 

Veracity of a piece of information is assessed by a composite criterion, which aggregates metrics that are related to its source(s). The metrics are extracted from confusion matrices because they are comprised of sensor reports that are based on how well a given sensor reflects the actual state of the subject being sensed. The statistical classification approach using the confusion matrices is well understood and used [51], sometimes with a different name, in other domains, such as machine learning, to analyze system accuracy by deferring and identifying elements. In a Bayesian framework, confusion matrices are modeled as leaf nodes of a graph that reflect the causal relationship between reality and what the sensor reports it to be. The ancestor nodes would perform the aggregation of the criteria, which ultimately would be used in the assessment of veracity and other characteristics important to ATM systems. Examples of attributes that can be aggregated in this scheme include sensitivity, accuracy, precision, credibility, and timeliness.

The attributes defined in the URREF ontology reside under the concept of Information Criterion (i.e., each being a criterion for evaluating information). The URREF also provides the machinery by which a system developer would establish the evaluation procedures in a structured fashion. For instance, the ontology specifies that an evaluation subject (e.g., an individual of the class PieceOfInformation) can be assessed in terms of its credibility (i.e., a subclass of EvaluationCriterion) through the sensitivity of the source. Both Source and ObservationalSensitivity are URREF classes, and their associated object properties define how such classes are correlated. As an example, the object property isAssessedBy has ObservationalSensitivity as its domain and TypeOfScale as its range. A system could use this property to link the range of ObservationalSensitivity of a sensor to the Signal to Noise Ratio (SNR) scale below, which is used in this paper to quantify the sensitivity of a sensor as part of the automated process for estimating veracity. For instance, the range defined for sensitivity was based on a study on sensitivity of operational weather radars [52] and adapted as follows:

- SNR loss from baseline $<-3.5 \mathrm{~dB}$ : Very low sensitivity.
- SNR loss from baseline between -3.5 dB and -1.5 dB : Low sensitivity.
- SNR loss from baseline between -1.5 dB and 0 dB : Regular sensitivity.
- SNR gain from baseline between 0 dB and +1.5 dB : High sensitivity.
- SNR gain from baseline $>+1.5 \mathrm{~dB}$ : Very high sensitivity.

The above scale was specific for the WSR-88D radar and is shown here for illustration purposes. Different scales and other quantitative ways of assessing the attributes can be encoded in the ontology.

This paper highlights the combination of both the URREF and a Bayesian framework, given the advantages of the first as an ontology specifically designed for evaluation (e.g., code reuse, standardization, support for logical reasoning, etc.) and the power and flexibility of the latter in managing uncertainty in complex, dynamic domains. Merging uncertainty and logical reasoning is an active research field (e.g., [53,54]), and the specific need of using Bayesian probabilities with ontologies naturally made Probabilistic Ontologies a natural choice for addressing our needs. Probabilistic ontologies, written in the probabilistic web ontology language (PR-OWL) language [55], impact application domains (e.g., cyber [56,57] maritime domain awareness [58], situation assessment [59], predictive

situation awareness [60,61], procurement fraud [62], decision support [63,64], and others), and are a promising approach for enabling the use of concepts of the AAO and the URREF ontologies to perform both the probabilistic and the deterministic reasoning operations required in our work.

PR-OWL is a probabilistic extension to the OWL, and its mathematical foundation is Multi-Entity Bayesian Networks (MEBN), which can be seen as a first-order logic version of Bayesian Networks [65]. MEBNs encode probabilistic knowledge as MEBN Fragments (MFrags), which can be seen as templates to build BNs for any given scenario. In general, an MFrag captures a repeatable pattern (e.g., the effect of a specific cyber asset to a network node) and can be instantiated as many times as needed to match a specific situation (e.g., that specific cyber asset being employed to a 10-node network). An MFrag is a parameterized fragment of a directed graphical probability model. MEBNs provide a compact way to represent repeated structures in a BN.

To illustrate how such concepts and attributes could be used to assess the output of an ATM system, the next Section provides an example of an MFrag formed to evaluate the veracity of a given piece of information, and then one of the many possible instantiations of that MFrag.

# 5. Application Examples 

This section presents application examples of the AAO-based DSS proposed in this paper for ATM/UTM systems. The examples present realistic scenarios from different airspace situations.

### 5.1. Airspace Situation 1: Distributed Sensing of Weather Condition

Scenario 1 considers Flight BA249, flying at cruise altitude (40,000 feet) while approaching the northeast coast of Brazil (Figure 8). The airplane took off from London Heathrow Airport (LHR) and is scheduled to land at Rio de Janeiro Airport (GIG) by evening, local time. Weather conditions are assumed to have remarkably deteriorated in Sector 3 of the Recife Flight Information Region (SBRE FIR, Brazilian northeast coast). However, the weather condition is good for landing at GIG.
![img-4.jpeg](img-4.jpeg)

Figure 8. Scenario 1: (a) Airspace situation; (b) A cyber-physical view of the airspace situation.
Information regarding the above weather condition can be obtained from three different sources: Airborne Weather Radar systems (AWRSs), Satellite Weather Radar Systems

(SWRSs), and Land Weather Radar Systems (LWRSs). AWRSs are located in the aircraft nose and allow for detection of the intensity of convective weather conditions such as massive hails, powerful lightning, and excessive precipitation (strong downdraft-like microbursts). SWRS and LWRS are off-board systems aiding the aircraft in the airspace. All three systems are considered reliable. Nevertheless, AWRSs are considered to have the highest veracity, particularly when the weather in question comes from the area ahead the airplane. On the other hand, SWRSs are considered today to have the lowest veracity of the three systems. The variation in veracity is due to their way to sense and their proximity to the weather condition.

The challenging issue in the convective weather airspace situation is to determine (by sensing the weather conditions) how safe the airspace is to fly though. Thus, the AWRSs, SWRSs, and LWRSs are essential, including in the way the acquired information from all three sources is processed. The AWRS is an on-board sensing system of the aircraft flying in the airspace, while the SWRS and LWRS are off-board sensing systems that are made available to this aircraft via the airborne network and the ground infrastructure. Figure 8 shows the air-space situation and a cyber-physical view of the airspace situation in Scenario 1.

The physical world information sensed by these weather radar systems together (i.e., LRWS, SRWS, and ARWS) are uploaded to the cyberspace, where it can be shared with the stakeholders and other aircraft in the airspace and airports. Such multi-source information can be combined in order to build a more reliable model of weather conditions to assess the air-space situation by means of the AAO-based DSS. The AAO queries can be visualized by air traffic controllers to support their decisions on the above situation. Additionally, aviators and pilots of remotely-piloted aircraft as well as on-board implementation of the AAO in UAVs could make use of the information. Operators can run AAO queries as to the airspace situations where the different weather conditions take place.

The reliability of the weather model depends on the veracity of the information gathered. Visual satellite images and acoustic radar images can be analyzed and integrated based on their veracity. Space and time are the main drivers to the veracity metrics in a scenario. Applying the veracity metrics within the PR-OWL framework requires defining the number of sensors involved, the criteria used to evaluate veracity, and the associated query to be answered. The method selected is the Multi-Entity Bayesian Network (MEBN) [65] with the associated theory (MTheory). Next, the paper provides an example describing how the AAO MTheory is formed, how it is used to instantiate the BN needed to answer a query on the meteorological conditions in the example, and how the model can be used to perform other queries on that same scenario.

Figure 9 shows a couple of notional MFrags (templates for building BNs) for the AAO MTheory. The model was built using UnBBayes, an open source, Java-based probabilistic graphical framework that can build probabilistic ontologies [66]. Note that the concepts of the AAO ontology were used in a "drag-and-drop" fashion to create the MFrags that convey the probabilistic aspects of the ontology, allowing for a tight synchronization between the logical and probabilistic aspects of the ontology. In the model, the three different types of MFrag nodes can be seen: Context, Input, and Resident nodes.

Resident nodes are the random variables that form the core subject of an MFrag. The MFrag defines a local distribution for each resident node as a function of the combination of the states of its parents in the fragment graph. Resident nodes can be discrete or continuous. There are two discrete resident nodes in the Veracity MFrag, depicted as yellow rounded rectangles in Figure 9. In general, resident nodes are random variables that convey the uncertainty related to a triple (subject, predicate, and object) in the domain. For instance, the node hasVeracity (sensor, veracity) is a Boolean random variable that conveys the probability of a given sensor (subject) to have veracity (hasVeracity predicate) as True (one of the two valid states of the object Veracity). Likewise, the resident node DistanceFromSubject (sensor, range) conveys the uncertainty related to a given sensor to be within range of the subject it is sensing. The uncertainty is conveyed in the form of a local

probability distribution that, in the case of the latter, defines how likely it is that the range of the sensor is in one of its valid states (i.e., either one of (AboveRange, BorderlineRange, MediumRange, CloseRange)).
![img-5.jpeg](img-5.jpeg)

Figure 9. Sample MFrags from the AAO MTheory.
Input nodes, depicted as gray trapezoids in Figure 9, serve as "pointers" referring to resident nodes in other MFrags. Input nodes influence the local distributions of the resident, but their own distributions are defined in the MFrags in which they are resident. For instance, the input node hasVeracity (sensor, veracity) from the Weather Conditions MFrag is a pointer to its associated resident node defined in the Veracity MFrag. In this case, it can be instantiated as many times as needed to cover the situation at hand.

Context nodes are Boolean (i.e., true/false) random variables representing conditions that must be satisfied for the probability distribution of the resident nodes in an MFrag to apply. The same way it happens with input nodes, context nodes have distributions defined in their respective resident MFrags.

To illustrate the UnBBayes model, the MFrags in Figure 9 are used to evaluate a situation in which there are three sensors, and each would have its veracity assessed by two distinct criteria (accuracy and observational sensitivity in this case). Figure 10 depicts the BN (technically, a Situation Specific BN, or SSBN) that resulted from the instantiation of the MFrags in the AAO MTheory upon the input of three sensors (AWRS, SWRS, and LWRS) and two criteria to evaluate Veracity (Observational Sensitivity and Accuracy). That is, veracity is evaluated based on only two attributes of the URREF, sensitivity and accuracy. The sensitivity estimates the ability of a sensor to capture enough elements of a given subject (e.g., the minimal strength of a signal that can be captured by an acoustic sensor), while the accuracy assesses how close its readings are to reality.

For simplicity, the states of the reports are using the same terminology employed by FAA in its WSR-88D Doppler radar's precipitation mode [67], and a scheme similar to the one used to define the states in the sensitivity criteria would be used. To illustrate the probabilistic relationships involved, Figure 11 shows the Conditional Probability Table (CPT) used to calculate the posterior marginal probability of the SWRS report (node ProducesSWRSReport (SWRS, SWRSrep)). The distributions depicted in the table in Figure 11, one for each combination of potential weather conditions and veracity states, were defined by a subject matter expert (SME), but in an actual system they would have been assessed through a combination of sensor characteristics, collected data, automated learning, and other data analytic processes available in any Bayesian framework.

![img-6.jpeg](img-6.jpeg)

Figure 10. BN instantiated from the AAO MTheory with three sensors and two Criteria.

![img-7.jpeg](img-7.jpeg)

Figure 11. Conditional Probability Table for node ProducedWeatherReport (SWRS, SWRSrep).
In this example, it is assumed that the use of a probabilistic framework leverages the URREF definitions and the data accruing from an ATM system to estimate the veracity of a specific output. Figure 12 illustrates the result of a query on weather conditions for a specific area, in which the system's findings are input to the model (nodes in dark grey color), and the resulting posterior probability is calculated. For instance, the example assumes that the SWRS returned a Heavy conditions report, the AWRS returned an Extreme conditions report, and the LWRS returned a Moderate conditions report, all referring to the same subject (weather on FL 400 of SBRE FIR's Sector 3). The example in Figure 12 also assumes the ATM system has knowledge of all the associated distances and criteria computed, which are inserted into the model as findings. After the network is compiled, the final result is a $68.7 \%$ chance of Extreme weather in that area.

![img-8.jpeg](img-8.jpeg)

Figure 12. Query answering with the Situation Specific BN.
Note that the above example was notional and did not use actual sensor performance or data collected from the field, as it would in a general usage of this framework. Yet, it is sufficient to show the strengths of the proposed approach, which is capable of (1) using the URREF and AAO ontologies to automatically generate evaluation models; (2) adapt to any combination of sensors, criteria needed, sensor parameters (e.g., distance), and others to build a dynamic model of the environment; and (3) reuse this model to follow the evolving situation as new data from the scenario accrues.

A further example is explored by entering the same results in the system as if it only had one sensor at a time, while keeping the same conditions (i.e., the two criteria and the original results from the system). Table 6 presents the posterior probabilities obtained for the weather conditions at FL 400 of SBRE sector 3.

Table 6. Weather Conditions-Posterior probabilities for the isolated sensors and the combination of all three.


The AAO query is regarding the possibilities for Flight BA249 (a Boeing 787 airplane) to encounter adverse weather conditions that make the airplane change its route. The extreme weather condition classified as "massive precipitation" (i.e., weather causing a radar echo with reflectivity greater than 50 dB ) is the only one where it is considered necessary to make Flight BA249 change its airway. Figure 13 presents inferred classes/individuals (reasoned knowledge) from the AAO when the probabilities from Table 6 are incorporated into the AAO. Figure 13 shows the reasoning path (in green), followed by the reasoner to determine the AAO query results ("aircraft must be rerouted").

![img-9.jpeg](img-9.jpeg)

Figure 13. Reasoning behind the queries for airspace situation in Scenario 1.
Figure 14 shows the AAO query results from different queries carried out to identify whether Flight BA249 has to modify its route on its way to land in GIG. The results consider the veracity of each radar to detect the extremely strong storm on the Brazilian northeast coast. The sensor results seek to answer the question of what the chance is for Flight BA249 to have to modify its airway because of the weather conditions ahead. The chances depend on the veracity of the information provided by the weather radars.


Figure 14. Querying results to assess airspace situation in Scenario 1.

The AAO query results from the SSBN (as shown in Figure 14), considering individual radars and combined radars, suggest that (from left to right):

1. High chance of modifying the airplane route (when SWRS detects the heavy storm ahead of Flight BA249). Flight BA249 should change route to avoid the weather conditions on its way to GIG for landing because the SWRS suggests a probability of $51.10 \%$ for heavy weather. The veracity of this query is based on a veracity of $36.00 \%$ (from Figure 13). This suggestion is less veracious than suggestion 2.
2. Very high chance of modifying the airplane route (when AWRS detects the extreme weather ahead of Flight BA249). Flight BA249 must change route to avoid the weather conditions on its way to GIG for landing because the AWRS suggests a probability of $80.90 \%$ for extreme weather. The veracity of this query is based on a veracity of $65.80 \%$ (from Figure 13). This suggestion is the most veracious out of the three suggestions.
3. Chance of modifying the airplane route (when LWRS detects the microburst weather condition ahead of Flight BA249). Flight BA249 could change to avoid the weather conditions on its way to GIG for landing because the LWRS suggests a probability of $39.50 \%$ for moderate weather. Although the veracity of this query computes the high sensitivity of the sensor, it is the least veracious of the three suggestions ( $9.94 \%$ from Figure 13). A potential explanation certainly includes the medium accuracy and the dissonant report with respect to the other two sensors.
4. The combined sensors overwhelmingly suggests extreme weather ( $68.70 \%$ probability), which is more likely than all other states combined.
Thus, in this example, the resulting query would likely result in Flight BA249 changing its route so as to avoid the extreme weather in Sector 3 of SBRE. When analyzing the results from Table 6, it is easy to perceive the weight of the veracity calculated for each sensor. In the example, the environmental conditions deemed the AWRS to be the sensor with the highest veracity ( $65.8 \%$ ), even though it does not have the highest observational sensitivity.

The Flight BA249 example was tailored to reflect a dissonance between the sensors (which is rarely seen in extreme weather conditions) as a means to illustrate how the veracity of each sensor impacts the overall results of the system. Note that the calculations for veracity in this example considered two criteria (Observational Sensitivity and Accuracy), but the system is flexible enough to produce calculations when other criteria are also considered.

# 5.2. Airspace Situation 2: Natural Disaster and Unmanned Aerial Vehicles 

Scenario 2 focuses on the North Atlantic Tracks that connect European countries with North America. This includes all the flight routes in which aircraft fly over or near Iceland. The application scenario considers that the Eyjafjallajokull volcano is in the early stages of eruption, throwing volcanic ash up into the atmosphere. The ash cloud contains pulverized pieces of rocks, minerals, and volcanic glass, which greatly damage the jet engines of aircraft flying nearby the volcano in the above air corridors. As a real and serious threat for aviation, the eruption of Eyjafjallajokull resulted in the cancelation of thousands of flights in April 2010, leading to millions of stranded passengers in Europe [67].

The challenging issue in the ash-eruption airspace situation is to determine how serious the threat is by having an accurate reading of the characteristics of the ash cloud (e.g., density, size, location, etc.). Sensing mechanisms are crucial, as is the way the acquired information is processed. Images from sensing systems, such as meteorological satellites, weather radars, and any extra survey support such as special manned aircraft and UAVs, can be used to gather meaningful data and get a picture of the situation. Figure 15 shows a cyber-physical view of the airspace situation in Scenario 2.

![img-10.jpeg](img-10.jpeg)

Figure 15. Cyber-physical view of Scenario 2.
Similar to the description in Scenario 1, the physical-world information sensed by these airborne, space, and land-based sensors together are uploaded to cyberspace, where it can be shared with the stakeholders and aircraft in the airspace and airports. Such multisource information can be combined in order to build a more reliable model of the ash cloud to assess the airspace situation by means of the AAO-based DSS. The AAO queries can be visualized by air traffic controllers to support their decisions on the above situation. Additionally, the aviators and pilots of remotely-piloted aircraft as well as on-board implementation of the AAO in UAVs could make use of this information. The users can run AAO queries as to the airspace situation in the proximity of the Eyjafjallajokull volcano.

The International Civil Aviation Organization (ICAO) created a worldwide system of nine Volcanic Ash Advisory Centers (VAACs) in the late 1990s to help mitigate the effects of volcano eruptions on air transportation. The VAACs run models for assessing the transport and dispersion of volcanic ash and issue advisory information on the extent of the observed and forecast movement of the ash [67]. In the case of the Eyjafjallajokull volcano, the monitoring and advisory was conducted by the London VAAC. Models of ashcloud movement and dispersion are important for providing such services and are usually evaluated by satellite analyses. One example of such a model is the NOAA/Air Resources Laboratory Hybrid Single-Particle Lagrangian Integrated Trajectory (HYSPLIT) transport and dispersion model [68]. Stunder et al. [69] used HYSPLIT to make comparisons of archived volcanic ash forecast and analysis areas to reliability estimate the volcanic ash forecast area (VAFAR) for hypothetical large eruptions of several volcanoes.

VAFAR and other metrics for assessing the reliability of ash-cloud models demonstrate how important such results are for air transportation activities. The reliability of the ash-cloud model depends on the veracity of the information gathered. Thus, visual satellite images, acoustic radar images, and any other images collected from manned science aircraft or UAVs can be analyzed and integrated based on their veracity. The same modelling approach used in the previous example can also be applied in the modelling the veracity of the sensors involved in this scenario. However, because node hasWeather (area, weatherCondition) maps a weather condition to an area, it addresses the sensor's veracity for that whole area, which might or might not fully overlap with the ash cloud. Thus, the initial model is extended by adding the AtmosphericEventMFray, which allows us to specify the veracity of a sensor regarding one atmospheric event within an area and consider the weather in that area. Figure 16 shows the extended model.

![img-11.jpeg](img-11.jpeg)

Figure 16. Extended AAO MTheory.
Following the same procedures as in the model for Example 1, different values for the CPTs are entered for the nodes, reflecting the impact of the different factors. In this case, two sensors are considered as providing information on the atmospheric accumulation of volcanic ash: one taken from a satellite image report (EOsatImg) and another from a sensor on-board a UAVs (UAVdata). Both sensors had a higher probability of a concentration between 2000 and 4000 micrograms per cubic meter of volcanic ash. Table 7 brings the posterior probabilities obtained for the concentration of volcanic ash.

Table 7. Ash Concentration-Posterior probabilities for the isolated sensors and their combination.


In this case, the veracity of the EOsatImg report for the conditions observed was $91.4 \%$, while the UAVs' sensor obtained a roughly $6 \%$ improvement over the satellite report at $97.05 \%$. As a result, the combined sensor had intermediate results, but tended to agree slightly more with the UAVs' data. Note that we applied the same MFrags for this scenario, with the CPTs for the new sensors being estimated. As in the previous model, different estimates would yield a different reading for the combined concentration, as well as for the other parameters in the model. However, the goal was to show how the technique would work for different scenarios, and an experiment with real sensor performance data would likely have changes in the magnitude of the results but not in the overall trends (i.e., the combined sensor's posterior probabilities would still be closer to the UAV ones). The AAO query regards the possibilities for commercial flights to encounter a dangerous ash cloud that causes the airplane to change its route. The ash-cloud condition is classified as follows:

- "Very low ash concentration" when it is below 200 micrograms;

- "Low ash concentration" when it is between 200 and 2000 micrograms;
- "High ash concentration" when it is between 2000 and 4000 micrograms;
- "Very high ash concentration" when it is above 4000 micrograms.

Figure 16 presents inferred classes/individuals (reasoned knowledge) from the AAO when the probabilities from Table 6 are incorporated into the AAO. Figure 17 shows the reasoning path (in green) followed by the reasoner to determine the AAO query results ("aircraft must be rerouted").
![img-12.jpeg](img-12.jpeg)

Figure 17. Reasoning behind the queries for airspace situation in Scenario 2.
Figure 18 shows the AAO results from different queries carried out to assess whether an aircraft must modify its route on its way from Europe to America, or all the way around. The results consider the veracity of EOsatImg and the UAV sensors to detect the concentration in the ash cloud from the Eyjafjallajokull volcano. The query results answer the question of what the chance are for the above aircraft to have to modify its airway because of the ash cloud. The chances depend on the veracity of the information provided by the two sensing mechanisms (satellite images and UAV sensors).

The AAO query results from the SSBN considering the satellite and the UAV instruments, and a combination of their measurements, suggest that (from left to right):

1. High chance of modifying the airplane route (when EOsatImg detects the ash concentration from the ash cloud). Aircraft should change route to avoid the ash cloud on their airway as the EOsatImg radar suggests a probability of $53.60 \%$ for an ash concentration between 2000 and 4000 micrograms in the ash cloud. The veracity of this query is based on a veracity of $91.40 \%$. This suggestion is less veracious than suggestion 2 .
2. Very-high chance of modifying the aircraft route (when UAVs detect the ash cloud concentration). Any aircraft flying near the volcano must change route to avoid the ash

cloud on its way because the UAVs' data radar suggests a probability of $74.90 \%$ for an ash concentration between 2000 and 4000 micrograms in the ash cloud. The veracity of this query is based on a veracity of $97.05 \%$. This suggestion is the most veracious out of the three suggestions.
3. The combined sensing sources overwhelmingly suggest the ash cloud has an ash density that makes aircraft divert their route (probability of $64.60 \%$ for an ash concentration between 2000 and 4000 micrograms in the ash cloud). The veracity of this suggestion is $88.70 \%$ (multiplication of the above veracities, i.e., $91.40 \%$ and $97.05 \%$ ).
![img-13.jpeg](img-13.jpeg)

Figure 18. Querying results to assess airspace situation in Scenario 2.

# 6. Conclusions 

Future ATM/UTM decision-making avionics analytics support requires semantic correspondence between physics-based sensing and human-derived descriptions for situation awareness, assessment, and understanding. The paper presents an ontological dictionary and processing techniques by highlighting the novelty of combining the Avionics Analytics Ontology (AAO) endowed with the Uncertainty Representation and Reasoning Evaluation Framework (URREF) with Multi-Entity Bayesian Network (MEBN) fusion with the probabilistic ontology web language (PR-OWL). The AAO-based DSS would reduce workload from overwhelmed aviators, remote pilots of UAVs, and ATM controllers by affording efficient query processing. Additionally, the paper models the degree of estimation uncertainty by means of information veracity metrics, which is rarely addressed in big-data solutions. To demonstrate the approach, two UTM airspace situations based on real data are implemented in the Protégé tool. Both situations involve weather conditions, UAVs,

and distributed sensing with probabilistic decision-making support on whether aircraft rerouting is necessary for aircraft safety. The use of ontologies provides a verified method for alert reports and warnings on UTM safety envelopes for aircraft trajectories in the presence of disturbances, which could be used for real-time autonomous control.

Table 8 shows a comparison between the most relevant ontologies for avionics analytics in ATM/UTM to appreciate the uncertainty-driven AAO presented in the paper as compared to ATMonto (NASA ATM ontology) and the Aeronautical, Flight, and Meteorological Information eXchange models (AIXM [70], FIXM [71], MIXM [72]).

Table 8. Comparison of scopes of relevant ontologies.


Future research work will expand the analysis using additional reasoning in the URREF over data handling, estimation reasoning, and information representation. Prototype development is underway with UAVs from which to train and coordinate with operators to determine the capability of ontologies for UTM, as demonstrated in multimedia processing, healthcare diagnosis, and geographical information systems. In-flight UAV studies could validate UDAAO to provide real-time decision making in the provision of security, safety, and reliability of aerospace systems.

Author Contributions: Conceptualization, C.C.I. and E.P.B.; methodology, C.C.I., E.P.B. and P.C.G.C.; software, C.C.I. and P.C.G.C.; validation, C.C.I. and P.C.G.C.; formal analysis, C.C.I., E.P.B. and P.C.G.C.; investigation, C.C.I., E.P.B., P.C.G.C. and K.S.; resources, C.C.I., E.P.B., P.C.G.C. and K.S.; data curation, C.C.I. and P.C.G.C.; writing-original draft preparation, C.C.I., E.P.B., P.C.G.C. and K.S.; writing-review and editing, C.C.I., E.P.B., P.C.G.C. and K.S.; visualization. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Acknowledgments: The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of the UK and US Governments.

Conflicts of Interest: The authors declare that there is no conflict of interest regarding the publication of this paper.
