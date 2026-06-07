# Review <br> Analysis and Characterization of Risk Methodologies Applied to Industrial Parks 

Martin Folch-Calvo ${ }^{1, * *}$, Francisco Brocal-Fernández ${ }^{2 * *}$, Cristina González-Gaya ${ }^{1 *}$ and Miguel A. Sebastián ${ }^{1 *}$<br>1 Manufacturing and Construction Engineering Department, National University of Distance Education, 28040 Madrid, Spain; cggaya@ind.uned.es (C.G.-G.); msebastian@ind.uned.es (M.A.S.)<br>2 Department of Physics, University of Alicante, 03690 Alicante, Spain; francisco.brocal@ua.es<br>* Correspondence: mfolch15@alumno.uned.es

Received: 22 July 2020; Accepted: 4 September 2020; Published: 5 September 2020


#### Abstract

It is important to evaluate the risks in industrial parks and their processes due to the consequences of major accidents and especially the domino effect. Scientific works present a wide possibility of models to deal with these situations. In this work, based on the information extracted from the scientific literature, six groups of risk methodologies are defined, analyzed, and characterized with methods that cover the standards, preventive, probabilistic, traditional, modern, and dynamic evaluation that are applied or could be used in industrial parks. It also tries to achieve the objective of determining which are more appropriate if the possible situations and causes that can produce an accident are taken into account, identifying and evaluating them with characteristics of simultaneity and immediacy, determining the probability of an accident occurring with sufficient advance in time to avoid it under the use of a working operational procedure. There is no definitive methodology, and it is necessary that they complement each other, but considering the proposed objective, the integrated application of traditional methodologies together with the management of safety barriers, the dynamic evaluation of risks, and the inclusion of machine learning systems could fulfill the proposed objective.


Keywords: dynamic risk assessment; standard procedure; domino effect; risk management; industrial park; Bayesian inference

## 1. Introduction

An industrial park can be defined as a specific area with a planned offer of logistics, telecommunications, and infrastructure services, and in which an integration of producers is carried out in order to obtain competitive advantages [1,2]; for this reason, the European Union highlights that industrial parks are an important tool in the industrial transformation of their Member States [3]. However, industrial park development has resulted in possible major accidents, with accident risk concentration, the major risks being the domino effect and the environmental emissions [4].

There are several definitions of what is considered a domino effect, in general the following common features and patterns are presented [5-8]:
(1) A primary accidental scenario (i.e., loss of containment (LOC) due to shell breaking, wrong weld, overpressure, incorrect handling) with an initial event (i.e., fire, explosion) that initiates the domino sequence by means of physical phenomena such as heat radiation, blast wave, or fragment projection.
(2) The propagation and escalation due to the physical effects of the primary event that results in the damage of at least one secondary equipment item. Characteristics are the overpressure, the fire, and heat generation in form of pool fire, jet fire, and vapor cloud explosions.

(3) As a consequence, one or more secondary events appear from the newly damaged equipment (i.e., additional fire, explosion, and toxic dispersion).

All the main causal and operational factors, as primary events, are synthesized in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Domino effect factors (a) causal; (b) operational (adapted from [5]).
The critical causes are those for management errors due to poor design, lack of maintenance, an inadequate work environment, inadequacy in procedures, supervision, and training, and not taking corrective actions on time with a $52 \%$; and the human errors in commission operations and omission actions with a $37 \%$. The operational factors are mainly critical in the loading-unloading operations with a $31 \%$, and into the storage area with a $29 \%$. However, a not negligible number of causal situations are produced due to equipment failure ( $9 \%$ ) and environmental situations ( $2 \%$ ); and from the operational view, the situations produced in normal operation ( $10 \%$ ), in maintenance interventions ( $9 \%$ ), in piping and utilities (every one with a $7 \%$ ), performing the checking and control ( $4 \%$ ), and in cleaning situations $(3 \%)$ are also important.

The objective of a risk control would be to have one or more risk assessment methodologies that take into account the possible situations and causes that may produce an accident, evaluating them in real time and with immediacy to determine the probability that it will occur in order to act early and be relatively easy to implement as a working procedure. In this sense, an initial consideration to prevent major accidents as domino effects are stipulated in the directive 2012/18/EU, known as the European Union (EU) Seveso III directive [9], and in the Committee on Control of Major Hazards HSE-COMAH, [10], the British equivalent to the European directive. Both regulations require the implantation of a major accident prevention policy (MAPP) with the consideration of the possible domino effects caused by proximity and storage of hazardous and flammable materials, and the need for to perform a safety report demonstrating that a MAPP and a safety management system have been implemented, the possible major accident scenarios have been identified, and measures have been taken; the safety report has to be performed at the initial start-up and has to be updated every five years. The implementation of a risk treatment policy is also established on the ISO 31000:2018 [11] and the ISO/IEC 31010:2019 [12], which are based on the risk assessment as a general process covering their identification; analysis and evaluation [13], and on the Quantitative Risk Assessment (QRA) in order to determine its probability of occurrence. However, this treatment involves a static vision of the risk situation only updated each time the risk situation is reviewed, and in front of this arises the Dynamic Risk Assessment (DRA) to update the information of events that may lead to an accident updating the probability of risk [14-20]. See Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Left, (a) risk assessment compared to right, (b) dynamic risk assessment (DRA) (adapted from $[12,14])$.

There are also additional methodologies that can be applied to manage the risk and safety in industrial parks thinking in the worst case of the domino effect. This work offers an analysis and characterization of the most relevant methodologies, highlighting their most important differences in order to be able to determine which may be interesting in terms of the objective of disposing of the risk situation and its ease of application. The methodology and proposal of characterization are presented in Section 2, the analysis and characterization are presented in Section 3, their discussion is presented in Section 4, and conclusions are presented in Section 5.

# 2. Methodology and Proposal of Characterization 

To perform this analysis and determine the objective of being able to evaluate the risk situation in real time in an operational way, the information contained in scientific articles related to the treatment of risks in industrial parks is examined. To evaluate their degree of fulfillment to this objective, it is necessary to first define three series of characteristics:
(1) Characteristic for the supplied information [21], as presented in Table 1.
(2) Characteristics for a standard procedure degree and user level. See Tables 2 and 3.

Table 1. Characteristic of the supplied information.


The International Organization for Standardization (ISO) [22] defines standard as the description of the best way of making a product, managing a process, delivering a service, supplying materials, or managing and assessing risks, collecting the expertise of people in their subject matter and who

know the needs of the organizations they represent. In the same line, the Center for Chemical Process Safety (CCPS) [23] defines standard as the requirement promulgated by regulators, professionals, or industry organizations, that apply to the design and implementation of management systems, design and operation of process equipment, or similar activities. For the American Society for Testing and Materials (ASTM) organization [24], a standard is a set of explicit instructions and requirements for performing specific operations to be satisfied in the final result. Finally, from the Food and Drug Administration (FDA) and the Directive 2003/94/EC, the idea of standard operating procedure (SOP) arises, being a set of step-by-step instructions focused on workers with the aim of carrying out the operation in order to maintain the process under control and simultaneously collect the needed information to support their quality and performance [25,26].

Table 2. Characteristics for defining a standard procedure.


${ }^{1}$ LDSP, MDSP, HDSP: Low, Medium and High level of difficulty of the standard procedure.

Table 3. Characteristics of the user profile.


(3) Specifically for the worst situation of possible domino effects in industrial parks, being: Does not perform the treatment (NT), it performs a general treatment (GT), and it performs a specific treatment (ST).

The analysis is performed, establishing six main groups according, from left to right, to their degree of simultaneity and immediacy of the supplied information, and in concordance to the analysis of the causes and consequences of the combined effects of overpressure, heat radiation, and fragmentation, see Figure 3:
(1) The first group is the corresponding to the standards, directives, and regulations. This group collects the most important standards and regulations concerning risk management and highlighting the need, in situations of major hazard, to establish a preventive policy in the different work areas of an installation.
(2) The second group covers the preventive methodologies, as a result of the application of the directives concerning major hazard situations and guidelines.
(3) The third group compiles the probabilistic methodologies, based on the three characteristics of a domino effect scenario: Overpressure, heat radiation due to fire, and fragment emission [27].
(4) The fourth group covers the traditional methodologies, including the sequential and the epidemiological models [28].
(5) The fifth group considers the modern methodologies, including five models: The systematic; cloud based; the fuzzy based; formal based; industry 4.0 and safety barrier based.
(6) The sixth group, which is encompassed in the modern methodologies, is specific for dynamic models.

![img-2.jpeg](img-2.jpeg)

Figure 3. General groups of the risk methodologies applied to industrial parks.

# 3. Analysis and Characterization 

### 3.1. Standards, Directives, and Regulations

The standards ISO 31000:2018 [11] and ISO/IEC 31010:2019 [12] provide a set of principles for managing and assess the risks, that are presented in Table 4. They are based in the "Deming" cycle [29], considering a sequence of steps: "Plan, do, check, act". If the ISO 31000:2018 contains general principles of the Risk Management, the ISO/IEC 31010:21019 presents a detailed explanation about the Risk Assessment process and the applied tools, see Figure 2. Where the context defines the situation of the risk with their external and internal influences, the risk assessment composed by their identification, analysis, and evaluation; the risk treatment, monitoring, and reviewing that carry out the implementation of corrective actions and risk changes, and the communication and consulting with the purpose to informatively extend into the organization the situations of risk. The ISO 14005:2019 provides rules for the implementation of an environmental management system (EMS) based also on the Deming cycle concept [29,30], with the same consideration the ISO 45001:2018 [31] allows for the implementation of a management system of safety and health at work (SHW).

From the most important European directives, the 89/391/EEC [32] was issued on 12 June 1989, being a framework directive for occupational accidents with the aim to establish the employers obligations for developing a prevention policy oriented to the protection of safety and health, and for the prevention, assessment, and elimination of risks and accident factors. Additionally, with the aim of establishing the occupational exposure limits, the Directives 98/24/EC of 7 April 1998, related to chemical agents at work, and 2004/37/EC of 29 April 2004, on the carcinogens and mutagens at work, were issued [33,34] as extensions of the previous 89/391/EEC.

Applied to project management, the most important methodologies correspond to the Project Management Institute and Prince2, as both are organizations oriented to the development of methodologies as PMBOK—Project Management Body of Knowledge, and PRINCE2—Projects in Controlled Environments. The PMBOK, contemplated as an American National Standards Institute (ANSI) standard for project management [35-37], is a detailed framework of ten knowledge areas of project management where risk is considered. A PRINCE2 scheme provides the elements for the organization, justification, commitment, and outcome of a project. The risk treatment for PMBOK and

PRINCE2 in general follows the risk management steps as indicated by the ISO/IEC 31010, with the same cyclic structure: Identify, plan, do, and act.

Table 4. Standards, directives, and regulations.


Standards issued by professional associations are promulgated by the Center for Chemical Process Safety [23], being an organization dependent on the American Institute of Chemical Engineers (AIChE), and that establishes risk management procedures that are mainly based on application of the Layer of Protection Analysis (LOPA) methodology, which defines seven layers of protection: Process design, basic controls, alarms-supervision action, automatic-manual action, physical protections, internal emergency responses, and community emergency response. Conceptually, a process deviation can lead to a hazardous consequence if not interrupted by the successful operation of the safeguard layer [38-40]. The "Norsk Sokkels Konkuranseposisjon" (NORSOK) standards are developed by the Norwegian petroleum industry to ensure adequate safety with a balanced cost for petroleum industry developments and operations through the guideline Z-013 [41-43]. The Netherlands advisory council of dangerous substances issued several publications from the old CPR (Commissie voor de Preventie van Rampenthat, still called CPR guidelines [44], being the most important the CPR18E or "Purple Book", analyzing the loss of containment events in chemical processes and the modeling of the associated

flammable clouds, their dispersion, and toxic effects, and finally the EN 16,991:2018, a standard based on the concept of Risk Based Inspection and Maintenance issued for chemical and power generation, chemical processes, and manufacturing facilities providing guidance for risk evaluation of equipment in parallel to the inspection and maintenance operations [45,46].

These previous standards, directives, and regulations are focused on a preventive action over the facility under study, and only the Directive 2012/18/EU, the equivalent COMAH, and the CCPS, NORSOK, CPR18E, and EN 16,991:2018 guidelines offer a general treatment of the domino effect situations with this preventive framework. From these directives and standards, the definition of a standard operational procedure requires a medium-strong knowledge of the facility processes and principles.

# 3.2. Preventive Methodologies 

The first possibility is the optimization of the stored inventory, for which Bayesian networks are used to reduce the probability of risk of escalation due to the characteristics and quantities of stored product and the distance to the initial event [47], see Table 5.

Next is to apply key indicators, previously performing the process units identification and classification according to their geometrical and structural characteristics, their failure modes, and vulnerability related to the primary scenario (i.e., LOC), with a probability of occurrence that can be obtained from a failure database or from historical data; the last step is the determination of indexes related to the safety barriers' performance in front of ignition, cloud formation, and escalation [48-51].

The layout optimization is based on the hypothesis of overpressure due to jet fire or vapor cloud explosion producing propagation and scaling, and an objective function is defined according to geometrical units footprint, location coordinates, and costs for pipe network, land, and damage, resulting in an optimization problem [52-54]. Similar works are performed considering injury of people, collapsed structures and loss of production, using Bayesian networks and an analytical hierarchical process $[55,56]$.

The safety barriers management analyzes the passive and preventive safety barriers with the aim of detecting and responding to process deviation from normal operation using controls, alarms, safety instrumented systems or functions, and mitigative safety barriers and systems (e.g., water deluge, emergency depressurization, and shutdown and response actions) [57,58]. Tools such as the BORA (Barrier and Operational Risk Analysis) are applied [59]. Optimization is also applied considering the cost of protection and injuries to people, and defining a quality objective function that has to be maximized [60-63].

The environmental consequences are considered, using a hierarchy process, fuzzy logic, and GIS (Geographical Information Systems) to evaluate and score the risk factors of the environmental impact [64-68].

The previous methodologies are focused on a preventive and specific treatment of the domino effect, only the Seveso III directive brings overview and medium difficulty in establishing a standard operating procedure with a product limitation in concordance to their Annex I.

### 3.3. Probabilistic Methodologies

See Table 6. The heuristic analysis is based on the history of accidents caused by the domino effect. Practical rules are established to increase the probability of resistance, considering distances and designs of passive protections and equipment in the function of scaling potentials and collapsing times due to fire radiation. Practical rules are issued considering the shape and composition of process equipment, the quantities and properties of the chemicals involved in operations, and storage, location, and distances of process units, installations, and infrastructures, and meteorology affectation [69-72].

The probability due to the overpressure is treated defining a probit function to relate equipment damage to the peak static overpressure:

$$
Y=a+b \cdot \ln \left(P^{0}\right)
$$

where $Y$ is the probit function for equipment damage, $P^{0}$ is the peak static overpressure ( Pa ), $a$ and $b$ are the probit coefficients $(a=-23.8$ and $b=2.92)$. See Figure 4. The probit approach was extended, taking into account four categories of industrial equipment (atmospheric vessels, pressurized vessels, elongated vessels, and small equipment) [27,73]. The probit coefficients for overpressure damage probabilities for four equipment categories are represented in Table 7.

Table 5. Preventive methodologies.


![img-3.jpeg](img-3.jpeg)

Figure 4. General expression for the probit treatment of the overpressure (adapted from [27,73]).

Table 6. Probabilistic methodologies.


Table 7. Probit coefficients and probability distribution for damage probability in four categories of industrial equipment. (Values in kPa), (adapted from [73]).


The probability treatment for damage due to heat radiation can be expressed also by applying a probit function and the estimation of the time to failure (ttf) of industrial equipment exposed to

fire based on vessel volume and energy received [74-79]. Table 8 presents the probit coefficients and thresholds for two equipment categories.

Table 8. Probit coefficients for time to failure (ttf) estimation due to fire. Y: Probit function; ttf: Time to failure (s); V: Vessel volume $\left(\mathrm{m}^{3}\right)$; I: Amount of heat radiation received $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$, (adapted from [74]).


The fragmentation and posterior projections generated by a primary explosion produced in tanks or equipment containing highly pressurized gas or liquids in general lead to catastrophic failures due to the successive explosions generated by the fragments' projection, creating secondary accidents, and possibly tertiary, until the process stops. Effects can be assessed by analysis or using a Monte Carlo simulation; in general, three main steps of analysis are required [80-86]:
(1) Determination of the probability of occurrence of the primary explosion, where fragments' number, mass, velocity, departure angles, the geometric shape, dimensions, and construction material properties are described with function distributions.
(2) Determination of the target damage where the consequence of projectiles number, speed, angles, and energy at the impact, are related to target construction, dimensions, and depths of penetration that are described with probability distributions.
(3) Risk assessment for the second scenario explosion (domino effect).

Computational Fluid Dynamics (CFD) and the Finite Element Method (FEM) are applied in the analysis of the initial event and the escalation damages. The CFD tool can simulate the evolution of jet and pool fires, and the FEM tool can simulate the thermal and mechanical parameters of vessel shells under heat radiation, such as heat radiation, wall temperature, and stress [87-92].

The probability due to analytical evolution for overpressure, radiation, and fragments dispersion apply Gaussian models matched with CFD tools [93-97], and meteorological conditions are included using a probabilistic approach [98]. The procedures can be matched to a GIS (Geographical Information System) to take into consideration actual plant lay-outs and identify possible escalation targets [99].

The graphical determination is based on a graphical network representing chemical installations or equipment as nodes $N$ and arcs $A$ connecting a pair of nodes. The weight of each arc represents the probability of accident propagation from one installation to another, being equivalent to the application of a Bayesian network in which random variables are represented by nodes while the conditional dependencies or cause-effect relationships and times of propagation among them are denoted by directed arcs $[100-102]$.

Simulation tools are applied for determining the evolution of a defined layout of equipment when overpressure, heat radiation, and fragmentation are present [103]. Monte Carlo techniques can be applied to assess the frequency of escalation consequences [104].

These previous methodologies are focused on a preventive (P) and specific treatment of the domino effect. Heuristic methods, because they are based on general rules, are more likely to be translated into a standard procedure that would have a low-medium level of difficulty.

# 3.4. Traditional Methodologies 

Traditional methodologies comprise two models, sequential and epidemiological, see Tables 9 and 10. Sequential models consider accidents as outcomes of a chain of discrete events or factors that take place in a temporal order. Practically all the methodologies from this group apply graphical techniques. The first exponent is the Fault Tree Analysis (FTA) [23], with the aim to

quantify the failure probability of human and technical systems. The Event Tree Analysis (ETA) [23] is applied to assess domino effects caused by fire in gas industry, offshore installations, LNG tank storage, and process industries [105,106,107,108], and it is also used for human reliability assessment as part of THERP (Technique for Human Error Rate Prediction) [109], based also on event-tree approach for evaluating human errors and behavior. This method is applied in the analysis of the Tokai-Mura uranium reprocessing plant accident [110].

Table 9. Traditional methodologies.


The BOWTIE graphic [23] is the integration of the FTA and ETA models to represent causes, and in the design or evaluation of the safe barriers, concluding with the consequence events, it is applied to assess a flammable and explosive chemicals storage area [111]. The Failure Mode Effect Analysis (FMEA) [112], is a step-by-step analysis approach for identifying potential failures. The Failure Modes Effects and Criticality Analysis (FMECA) [112,113] is an upgrade of the previous method, and it is used for preliminary hazard analysis with the aim to identify potential failure or accident modes and how to avoid it. The Check List-What if [114] is a systematic and scenario imaging revision of equipment and installations to find malfunctions in compliance with a list of requirements or from collected data in an orderly and systematic way. The Block Diagrams [114] is a graphical procedure describing the function of the system and showing the logical connections of components needed to fulfill a specified system function, and the Reliability Assessment (RRA) [115] has the aim to quantify the probability of failure in a system.

Following with the traditional methodologies, see Table 10, the Hazard and Operability study (HAZOP) and hazard identification (HAZID) are top-down qualitative systematic examinations of a planned or existing process to identify risks and problems for personnel or equipment, and both techniques are applied in the chemical process and highly flammable fueling stations [116,117]. The Energy Barrier Model (EBM), is based on the safety barrier management, being the activities to establish and maintain safety barriers and their functions, and the method states that an accident occurs when hazards succeed in penetrating the safety barriers with defects or deficiencies in their functional activity [118]. The Management Oversight and Risk Tree (MORT) [119] identifies the set of multiple causes that together might create a potential accident, and the analysis is also performed using tree techniques and check list methods. The Systematic Cause Analysis Technique (SCAT) [120] applies a poster-sized schematic, which enables identification of the preventive and corrective actions. The Sequential Time Events Plotting (STEP) [121] identifies multiple causes that together might create an occupational accident. The Man Technology and Organization (MTO) method [122] analyzes safety barriers applying checklists to identify causes in occupational work affected by deficiencies in organization. The Safety through Organizational Learning (SOL) [123] performs the identification of contributing factors to the accident. The 24 Model considers that accidents are a consequence of internal-external organizational causes, and it is applied in process industries [124,125,126].

Table 10. Traditional methodologies (continued).


Epidemiological models consider that the spread of events can be modeled using the same analogy of spread of a disease. Accidents are the result of manifest and latent events that take place under epidemic context $[127,128]$.

These previous methodologies are focused on a preventive (P) actuation and offer a certain simultaneity (S), but there is a delay if changes in operations are produced due to their own process of cause-consequence analysis. The treatment for domino effect situations is general in all the methods with occupational orientation in the STEP and MTO models. In general, a high level of knowledge of the processes, equipment, and principles is required, which is evident in those cases where the intervention of a group of experts is needed, therefore a certain level of difficulty is generated in defining a standard procedure.

# 3.5. Modern Methodologies 

Modern methodologies have five models: The systemic-systematic; cloud based; the fuzzy based; formal based; and safety barrier based, see Tables 11 and 12.

Table 11. Modern methodologies.


The systemic-systematic models apply concepts of control theory considering that external and internal influences systematically affect the system with a feedback process influenced by limitations in the management and operations, obtaining the conditions prior to an accident [129].

From this group are represented the AcciMap [130] and the Systems Theoretic Accident Model and Processes (STAMP), and this last is applied in the analysis of chemical process industries and domino effect [131-134].

The Cognitive Reliability and Error Analysis Method (CREAM) characterizes the human performance assessing the human errors [135], and it has been applied in the analysis of a nuclear plant accident [110]; as a variation, the Driving Reliability and Error Analysis Method (DREAM) is applied to assess human behavior in driving accidents [136]. The Functional Resonance Accident Model (FRAM) [137] states that, as a result of the functional couplings, variabilities between system components and unpredictable conditions appear resonant, and the method is applied in the risk assessment of chemical industries [138].

The Accident Evolution and Barrier Function (AEB) [139] describes the interaction between technical and human-organizational systems which may lead to an accident, and this model is applied in process industries [140].

Cloud models are applying the preliminary risk analysis performing a data mining of critical hazards and establishing their importance or grade from the scoring of expert's knowledge. Data mining has been applied to the domino effect hazards determination in a tank farm [5] and in a gasification station [141].

Continuing with modern methodologies, see Table 12, fuzzy models try to assess the human behavior; a representative model of this group is the Human Error and Assessment Technique (HEART), assuming that the reliability of any task performance may be modified by the influence of Error Promoting Conditions (EPCs), this model is applied to detect human errors in a LPG (Liquefied Petroleum Gas) refueling station [142]. An additional representative method of this group is the CREAM-BN, an upgrade of the systemic Cognitive Reliability and Error Analysis Method (CREAM), using Bayesian networks to determine the probability of human failure considering behavior components: Strategic, tactical, opportunistic, or scramble, this model is applied in maintenance tasks, in-field operations, and in chemical plant incidents [143-145].

Table 12. Modern methodologies (continued).


Formal models apply the probabilistic approach for assess the scenarios of risk with the use of Bayesian networks, being representative of the Why Because Analysis [86] method; fuzzy logic, Monte

Carlo analysis, and Delphi procedure are additionally applied in the analysis of a container shipping logistic platform, and in a gas storage facility [146-148].

Industry 4.0 is a generic concept to improve self-control and risk identification through neural networks and machine learning; related to its application in industrial parks, it is used in inspection maintenance, construction, and environmental protection for chemical, oil and gas, and energy processes [149-151]

Safety Barrier models. The representatives for this group are the Process Hazard Prevention Accident Models (PHPAM) and the System Hazard Identification Prediction and Prevention (SHIPP). The PHPAM model is applied in the off-shore and oil-gas process industries, and it is founded on the assumption that accidents in these facilities are initiated by hydrocarbon release, which then propagates into accidents [152]. The System Hazard Identification Prediction and Prevention (SHIPP) is an upgrade of the previous prevention (PHPAM), adding to the quantitative evaluation of risk probability the possibility to actualize the probability values in concordance to with the real data collected from the scenario of analysis with the application of Bayesian inference [153].

This group is applicable on general industrial situations, and CREAM and DREAM are focused on human behavior. All of them offer prevention (P) and a certain simultaneity (S) with a delay due to the time needed to perform the systemic evaluation and the analysis of the error promoting conditions in concordance to the operational changes. Only SHIPP methodology offers simultaneity due to the characteristic of updating the information according to Bayesian inference, and that is shared with the Why Because Analysis, but this last also applies a systemic approach. The treatment for risk situations is general, but they can be applied specifically for industrial parks with a high difficulty to define a standard procedure.

# 3.6. Dynamic Methodologies 

This group has five representatives, see Table 13; the Dynamic Risk Assessment (DRA), the Dynamic Procedure for Atypical Scenarios Identification (DyPASI), the Risk Barometer methodology, the Dynamic Operational Risk Assessment, and the Statistical Risk Control methodology (SRC).

As stated in the introduction, the Dynamic Risk Assessment (DRA), see Figure 2, establishes a prior function for the statistical parameter that models the risk probability. The precursors, events, or causes that can lead to an accident are observed and formalized through the application of Bayesian inference to obtain the posterior function for the parameter that models the risk probability through the equation;

$$
f(p / D a t a) \propto g(D a t a / p) \cdot f(p)
$$

where $p$ is the statistical parameter, $f(p)$ is the prior statistical distribution for the parameter $p ; g(D a t a / p)$ is corresponding to the observed precursor data, and $g(p / D a t a)$ is the posterior statistical distribution; the risk identification and analysis of consequences are made through the application of the traditional models and methods. A sensitivity analysis can be performed reflecting the 'best case', 'worst case', and 'expected case' of the possible scenarios [154]. This strategy has been applied in the petrochemical industry for a storage tank containing hazardous chemicals, a refinery, and oil spill accidents; or performing the inference using Bayesian networks or Petri-nets that have been applied in offshore oil and gas accidents [102,155-157].

The Dynamic Procedure for Atypical Scenarios Identification (DyPASI) have been developed to perform an identification and assessment of the potential hazards based on information obtained from scenarios or situations which are not captured by traditional techniques. This is an application for an LNG gasification facility [158].

The Risk Barometer methodology [14] has the aim to continuously monitor the changes in risk influencing factors affecting the performance of the safety barriers. The procedure starts with a traditional quantitative risk assessment (QRA) or a dynamic risk assessment (DRA) including the safety barriers through the Barrier and Operational Risk Analysis (BORA) [59]; the risk influencing factors (RIFs) are defined using a systemic approach, considering human, operational, organizational, and

technical conditions. The presentation is equivalent to a barometer graph. The Dynamic Operational Risk Assessment applies Markov and Monte Carlo chain simulations to analyze the incidence of events and causes in each component of a system-process and their behavior according to four states in which can be found: Normal operation; abnormal not detected; abnormal detected; and under repair [159].

The Statistical Risk Control (SRC) uses sequential models and the Bowtie graph approach, performing a Bayesian inference and a hidden Markov analysis to update the failure probabilities of the process and safety barriers. As dynamic a method, the information is collected from initiating causes, the state of the safety barriers, and the event tree end-states; this information is monitored using charts and control tables monitoring probability risk situations outside limits with the aim to correct their causes before an event or accident occurs. Treatment for processes and occupational risks are available. There is included a specific treatment for the domino effect considering probability damage spread, the characteristics of products (toxicity, operation, and flammability), the weather effect (storm days, precipitation, wind days over a critical value) and fuzzy logic for the behavior of the installation due to critical process variables [160,161].

Table 13. Dynamic methodologies.


These models offer prevention (P), simultaneity (S), and, due to their own characteristic of update the probability of risk according to the observations of incidences into the operational activity, a certain immediacy (I). Dynamic operational risk assessment is the one that offers the lowest value of immediacy (I) due to the time needed to perform the analysis at every component level of the process; the dynamic risk barometer shows this characteristic to a major degree, except for the time necessary to carry out the scoring and weighting of the risk influencing factors; in this case, the statistical risk control (SRC) offers immediacy by presenting the evolution of the risk parameter $p$ and showing an out-of-bounds situation, according to events generation, early enough to take corrective actions.

# 4. Discussion 

### 4.1. Standards, Directives, and Regulations

The objective of the different guides, directives, and regulations is to establish an organizational base from the definition of security policies into the organizations. Their characterization for the supplied information is basically for prevention (P), and no simultaneity (S) and immediacy (I) is obtained. It is possible to establish standardized procedures; however, a medium-high level of knowledge of the technical and design characteristics is required, as well as the basic principles and processes that are being carried out, therefore, the level of user to which it is directed is also medium-high. These requirements are more pronounced in the application and implementation of the Séveso III directive, CCPS, NORSOK, CPR, and EN 16991: 2018 guidelines, and on the management and evaluation of safety and health at work, through ISO 45001:2018 [162] and 89/391/EEC. Their application to industrial parks and especially for the domino effect is general.

### 4.2. Preventive Methodologies

As a consequence of the implementation of risk management, and occupational and environmental policies, the preventive treatments arise, such as the use of indicators, the optimization of facilities and products (stored, transported, or in-process), together with the optimization of safety barriers. The characteristic of the supplied information is preventive (P), and it is based on the quantitative risk assessment (QRA) concept, performing the evaluation of the risk probability with the subsequent cost-benefit estimation. These procedures are difficult to establish under a standard operating procedure, requiring a high dose of knowledge of the optimization techniques, economic costs, processes, and characteristics of the materials applied. The end user level is also high.

### 4.3. Probabilistic Methodologies

This group carries out preventive treatment, but not by avoiding or reducing the initial causes and risk of loss of containment (LOC), but rather of its consequences. The effects resulting from overpressure, heat radiation, fragmentation, and the dynamic behaviors of the toxic or heat emission columns of gases and vapors in the form of pool fire, jet fire, and explosion, are analyzed using mathematical or graphical tools under a quantitative risk scheme.

The characteristic of the supplied information is preventive (P), and it is based on the quantitative risk assessment (QRA) concept, performing the evaluation of the risk probability for the consequences of every escalation process. Simultaneity (S) is not complete, despite determinations based on probit functions for overpressure and heat radiation effects. Probit functions are more likely to be standardized and even automated in their determination, but in general, external intervention is required to be able to maintain the changes and their quantification, being difficult to normalize, therefore the procedure needs advanced users. The use of Geographic Information Systems (GIS) offers a certain simultaneity by making analysis possible in less time due to changes in the distribution of equipment and facilities. From heuristic treatments, it is possible to establish application rules that can be incorporated into a standardized procedure, however the user level is high due to the conceptual maintenance of the procedure, the application of calculation tools, and the conclusions, but, on the other hand, their application can be performed with a general level of knowledge of processes and facilities.

### 4.4. Traditional Methodologies

When analyzing the combined effects of overpressure, heat radiation, and fragmentation, the need to establish their causes and consequences arises simultaneously. Traditional methodologies apply a graphical approach, the most representative approaches applied to domino effect analysis are the fault tree (FTA), event tree (ETA), and bowtie; these tools originated in the chemical and offshore oil and gas industry, and have been successfully applied in the analysis of industrial parks [163,164]. Energy barrier model is widely applied to characterize the performance of the safety barriers [58,152],

and it is applied successfully in the process industry, but not in industrial parks, so its applicability in this type of scenario must be considered. The human error is treated in THERP, STEP, and MTO methodologies, considering that human error represents $37 \%$ in the initial cause of the domino effect, it may be interesting to integrate these tools in the evaluation and analysis in these environments. Due to the nature of treatment of the epidemiological models, their applicability, in industrial parks and business clusters, is linked to how information is shared between these entities and their degree of cooperation.

In this group, the characteristic of the supplied information is preventive (P), with a risk quantitative environment, and there is an important degree of simultaneity (S) despite the inherent delay to incorporate changes and perform the cause-effect analysis. For this group, is difficult to standardize the control of risk, and it requires a medium-strong level of the end user, with knowledge of the installation and facility under operation. Their applicability is general for industrial parks.

# 4.5. Modern Methodologies 

Modern methodologies appear as an upgrade and alternative to the traditional. The most representative are the systemic, cloud based, fuzzy based, formal based, and safety. Systemic is based on control feedback and response of the system, which is susceptible to external actions, generating a stability or resonance response.

Cloud models perform data mining actuations to collect characteristics that are coincident in risk situations or history accidents, and these models can facilitate the detection of causes of accident and their consequences [165].

Fuzzy models are integrated into the fuzzy information system (FIS), a general concept with the aim to evaluate the human, product, weather, or installation behavior [105].

Formal based is a generic quantification of risk probabilities that can be based initially on a traditional approach and integrated with tools such as fuzzy logic, Monte Carlo, or Delphi procedures.

Industry 4 models introduce the application of self-monitoring tools based on machine learning and deep learning using neural networks to identify risks in operations, maintenance, and environmental.

Finally, there is also present a specific treatment for Safety Barriers that are present in six models: The first is in the definition of the key preventive indexes, second, the preventive safety barriers management and assessment based on the BORA analysis, with the aim to define a set of actions and establish the performance of the barriers in front the hazard situations; third, the traditional (MTO) sequential model of causes for occupational analysis contemplates the performance of the safety barriers; fourth, the traditional energy barrier model (EBM) with the aim to define the barriers considering the possibility of break and risk as consequences; fifth, the modern systemic accident evolution and barrier function (AEB) with the aim to describe the interaction between technical and human-organizational systems; and sixth, the modern safety barrier with the aim that to avoid a risk, it is necessary to establish the safety barriers into groups of prevention functions and assess their performance by applying Bayesian inference tools for SHIPP methodology.

This group of methodologies offers the characteristic of information based on prevention (P), and a certain simultaneity (S), but due to the systemic, cloud based, fuzzy, and formal treatments, there is a delay in the actualization of the changes. Only the SHIPP treatment for safety barriers offers a high degree of simultaneity (S), being the initial treatment to dynamic models. Due to their specific treatment, it is difficult to define a standard procedure, and the end user requirements are high.

### 4.6. Dynamic Methodologies

In the evolutive treatment of risks, dynamic methodologies arise with the aim to update the probability of risk in concordance to the observations. Despite dynamic risk methodologies are originated from the chemical processes and offshore needs, this concept gains strength when spatial-temporal effects are integrated with Bayesian inference. The analyzed methods offer prevention (P), and due to Bayesian treatment, also offer simultaneity (S), except for dynamic operational risk

assessment due to its analysis procedure evaluating different possible states at component level, delaying the treatment of operations changes. Only Risk Barometer and Statistical Risk Control (SRC) offer immediacy (I), obtaining risk information with the possibility to correct the situation before an accident arises.

Due to the nature of the tools involved, it is difficult to define an operating procedure that allows standardized treatment of risks in an industrial park, and the level of the end user required is medium-high.

# 4.7. Applicability and Implementation 

Thinking about the application and implementation of the different methodologies over time for the risk management in industrial parks, it can be expressed in terms of their characteristics of prevention, simultaneity, and immediacy; bearing in mind that the pursued objective is to be able to respond sufficiently in advance to be able to avoid or reduce the risk of an accident, analyzing in real time the events and incidents, due to breakdowns and errors in the use of equipment, maintenance actions, and the performance of human teams, as well as the potential risk factors due to unforeseen changes, social situations, and meteorology, all of them are events that require a simultaneous and immediate response and should be managed through an operational work procedure. The proposal is presented in Figure 5; grouping the different methodologies according to their main characteristic. The group of standards, directives, and regulations offer prevention in their application over time, together with the preventive and probabilistic models, since they basically examine the consequences of possible accident scenarios based on overpressure, heat, and fragmentation. Systemic, formal, and fuzzy based methods offer prevention approaching the simultaneity characteristics strongly enough through the inclusion of the events, behavior, and effect due to the interrelation of the organization functions. Cloud analysis and data mining methods offer prevention, but their characteristic of simultaneity is increased through examination of events and their consequences that usually occur in accidents in industrial parks with the use of historical data that helps update the real situation. Finally, the group based on sequential (traditional), safety barrier (modern), dynamic evaluation, and Industry 4.0 (modern) methods, also offer prevention and simultaneity by treating possible causes not only in the design phases, but also in operating situations; in this sense, dynamic and Industry 4.0 methods are capable of dealing with the number of events and incidents that may occur through the application of tools that can manage and discriminate as far as possible their importance and consequence while simultaneously evaluating the probability of an accident, allowing a high immediacy. Additionally, in Figure 5, as the immediacy increases for each group, the level of implementation requires greater technical demand in the operational work definition and user profile, because the necessary degree of knowledge of the applied technologies and the balances of matter and energy increases, along with the need to establish, examine, and recognize what events and failures create a possible risk in the facility, together with the activity of human work teams, all within the scope of an industrial park.
![img-4.jpeg](img-4.jpeg)

Figure 5. Applicability along time according to the level of information supplied.

# 5. Conclusions 

As seen and justified in the previous sections, there is no model or method that individually can be applied, although there are characteristics that can be shared among them, for example, there are sequential methods such as Block-Diagram, MTO, and SOL that also have aspects of systemic models, and vice versa, there are found systemic models such as AcciMap, STAMP, and FRAM that share the sequential characteristics. Something similar happens with the use of fuzzy logic, that it is applied in methodologies for environmental management, probabilistic determination based on analysis, and formal models and dynamic models of risk; but, despite having shared traits, it is their set of peculiarities that ultimately define their belonging to one or another group of methods.

The treatment of occupational health and safety, and the consequence of human actuations, are present on standards, directives, and regulations group as ISO 45001:2018, 89/391/EEC, 98/24/EC and 2004/37/EC, for establishing policies or a framework together with limits exposure to chemical and carcinogen products; in the sequential group, with THERP, STEP, and MTO, which are applied to determine causes of error; in systemic models, mainly CREAM and DREAM are applied to evaluate human errors, and into the fuzzy methods to determine the human behavior consequences in HEART and CREAM-BN methods. Occupational treatment needs to be enhanced, because human actuations are a possible cause of accidents.

The environmental risks are treated as a policy defined through the ISO 14005:2019, and there is no specific methodology for industrial parks, even though the concept of Eco-Industrial Park is emerging [162].

As information characteristics, prevention (P) is present in all the reviewed groups. Simultaneity $(\mathrm{S})$ is present in probabilistic methodologies incorporating GIS treatment and in a certain degree in the traditional, modern, and dynamic methodologies. The immediacy (I) is available only in dynamic risk methodologies, specifically in the risk barometer and statistical risk control (SRC) methodologies.

The objective of applicability with a simultaneous and immediate response through a work procedure that allows evaluating and collecting the situations and causes that can produce an accident, by analyzing in real time the events and incidents that occur, in order to respond sufficiently in advance to avoid or reduce it, it would be possible with the application of the integrated use of sequential methodologies (traditional), safety barriers (modern), dynamic risk assessment, and Industry 4.0 (modern) methods, supplemented by data mining processes (modern), due to the fact of offering the characteristic of simultaneity and immediacy mainly from the use of dynamic risk and Industry 4.0 methods; but the possibility of defining and qualifying and operational work procedure show that, apart from to those established in the standards, directives, and regulations, and when the immediacy characteristic increases, there are greater technical demands in their definition and in the required user profile.

Due to the necessary complementary application of the methodologies involved, it is required to be able to share the information between the different facilities located in it, therefore, it is necessary to implement a coordination system that facilitates cooperation between the different entities and companies that comprise it.

Future work will require incorporating the integrated treatment of occupational risks and the use of deep learning where possible.

Author Contributions: Conceptualization, M.F.-C., F.B.-F., C.G.-G., and M.A.S.; investigation, M.F.-C., F.B.-F., C.G.-G., and M.A.S.; methodology, M.F.-C., F.B.-F., C.G.-G., and M.A.S.; supervision, F.B.-F., C.G.-G., and M.A.S.; validation, F.B.-F., C.G.-G., and M.A.S.; writing-original draft, M.F.-C.; writing-review and editing, M.F.-C., F.B.-F., C.G.-G., and M.A.S. All authors have read and agreed to the published version of the manuscript.

Funding: This work was funded by the Spanish Ministry of Economy and Competitiveness, with the title: "Analysis and Assessment of technological requirements for the design of a New and Emerging Risks standardized management SYStem (A2NERSYS)" with reference DPI2016-79824-R.
Acknowledgments: This work has been produced within the scope of the doctoral activities carried out by the lead author at the International Doctoral School of the Spanish National Distance-Learning University (EIDUNED). The authors are grateful for the support provided by this institution.

Conflicts of Interest: The authors declare no conflict of interest.
