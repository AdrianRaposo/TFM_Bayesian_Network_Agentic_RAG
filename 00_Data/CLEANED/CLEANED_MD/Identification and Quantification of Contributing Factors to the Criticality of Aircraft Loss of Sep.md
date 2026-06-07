# Article 

## Identification and Quantification of Contributing Factors to the Criticality of Aircraft Loss of Separation

Lidia Serrano-Mira ${ }^{1, * *}$, Marta Pérez Maroto ${ }^{1}$, Eduardo S. Ayra ${ }^{1,2}$, Javier Alberto Pérez-Castán ${ }^{1 *}$, Schon Z. Y. Liang-Cheng ${ }^{1,3 *}$, Víctor Gordo Arias ${ }^{1,4}$ and Luis Pérez-Sanz ${ }^{1}$

## check for updates

Citation: Serrano-Mira, L.; Pérez Maroto, M.; Ayra, E.S.; Pérez-Castán, J.A.; Liang-Cheng, S.Z.Y.; Gordo Arias, V.; Pérez-Sanz, L. Identification and Quantification of Contributing Factors to the Criticality of Aircraft Loss of Separation. Aerospace 2022, 9, 513. https://doi.org/10.3390/ aerospace9090513

Academic Editor:
Alexei Sharpanskykh
Received: 28 July 2022
Accepted: 2 September 2022
Published: 15 September 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 ETSI Aeronáutica y del Espacio, Universidad Politécnica de Madrid, Plaza del Cardenal Cisneros, 28040 Madrid, Spain
2 Iberia Airlines, Calle de Martínez Villergas, 49, 28027 Madrid, Spain
3 Aeronautic, Space \& Defense Division, Capgemini Engineering, Calle Campezo, 1, 28022 Madrid, Spain
4 Engineering and Transport Economics (INECO), Paseo de la Habana, 138, 28036 Madrid, Spain

* Correspondence: lidia.serrano@upm.es

Abstract: A Mid-Air Collision (MAC) is a fatal event with tragic consequences. To reduce the risk of a MAC, it is imperative to understand the precursors that trigger it. A primary precursor to a MAC is a loss of separation (LOS) or a separation infringement. This study develops a model to identify the factors contributing to a LOS between aircraft pairs. A Bayesian Network (BN) model is used to estimate the conditional dependencies of the factors affecting criticality, that is, how close the LOS has come to becoming a collision. This probabilistic model is built using GeNIe software from data (based on a database created from incident analysis) and expert judgment. The results of the model allow identification of how factors related to the scenario, the human factor (ATC and flight crew) or the technical systems, affect the criticality of the LOS. Based on this information, it is possible to exclude irrelevant elements that do not contribute or whose influence could be neglected, and to prioritize work on the most important ones, in order to increase ATM safety.

Keywords: air traffic; separation infringement; Bayesian Network

## 1. Introduction

Operational safety is the priority strategic objective for the International Civil Aviation Organization (ICAO) [1]. In order to ensure continuous improvement in this key performance area, the ICAO defined the Global Aviation Safety Plan (GASP). The purpose of the GASP is to continually reduce fatalities and the risk of fatalities [2]. The 2030 safety target is to achieve zero fatalities in commercial operations. To this end, five high-risk categories of events have been defined for the 2020-2022 edition of the GASP. These are: Loss of Control in Flight (LOC-I), Controlled Flight Into Terrain (CFIT), Mid-Air Collision (MAC), Runway Excursion (RE) and Runway Incursion (RI).

A MAC is defined by the ICAO as a collision between aircraft while both are airborne [1]. It is the worst event that can occur in ATM because it means that all the safety barriers have failed. They are Low Probability but High Consequence (LPHC) events. As can be seen from the European Aviation Safety Agency (EASA) statistics [3], the number of accidents compared to the number of flights is almost negligible. European commercial traffic data for the last decade show a total of six fatal accidents. Therefore, the number of MACs is equal to or less than 6 out of more than 100 million flights in Europe over the last ten years. Nevertheless, the consequences of a MAC are catastrophic.

One way to try to reduce the risk of a MAC is to have a greater understanding of the main precursors that anticipated and triggered the collision. A primary precursor to a MAC is a separation infringement or a loss of separation. A LOS is a situation in which prescribed separation minima is not maintained between aircraft [4]. It is considered by EUROCONTROL as one kind of incident, inter alia (Near CFIT, aborted take-off and so

on). An incident is an occurrence, other than an accident, associated with the operation of an aircraft which affects or could affect the safety of operations [4]. Not all incidents are equally critical. The ICAO [5] and EUROCONTROL [6] established five categories of incidents depending on the severity of ATM related occurrences affecting the safety of the aircraft: serious incident (A), major incident (B), significant incident (C), not determined (D) and no safety effect (E). Severity A incidents are much closer to accidents than Severity E incidents. However, the criteria defining the severity of an incident seem to be unclear, as they encompass several aspects such as minimum separation achieved, Air Traffic Control officer (ATCo) or crew actions, kinematic factors and safety nets performance, among others.

Working with incidents rather than accidents provides a twofold advantage. On the one hand, more data are available than from accidents because, although the occurrence of a separation infringement is minimal, it happens more frequently than a collision. On the other hand, it allows a more proactive approach to safety; by avoiding incidents, accidents are therefore avoided.

There are many categories of models for safety assessment in civil aviation: collision risk, causal, human factor and so on. Causal models have long been used in order to establish the framework of causes that may lead to accidents or incidents between aircraft. These causal models can be used to represent the set of interconnected processes that lead to the occurrence of a rare and catastrophic event whose probability of occurrence is to be estimated. Three common types of causal models used in safety assessment are: Event Trees, Fault Trees and Bayesian Belief Networks (BBNs), also known as Bayesian Networks (BN) [7].

Particularly, the Bayesian Network model (BN) has been used in the aviation field during the last decades. Applications in the area of Air Traffic Management (ATM) for decision-making and risk analysis are more recent. This model has been used on a wide range of problems: the determination of contributing factors to aircraft runway excursions [8], the assessment of uncertainty propagation for complexity in ATM [9], the uncertainty characterization in the airport environment and its propagation to the air traffic network [10], the determination of a risk-based separation between UAS and aircraft in VFR airspace [11], or the modelling of encounters between aircraft pairs for the estimation of collision risk [12,13], among others. Brooker in [14] presents a review of previous work and investigates the suitability of Bayesian Networks in ATM for accurate risk prediction.

Some authors have applied Bayesian Networks to aviation accident databases in order to understand the influence of certain factors. In [15], the impact of new technologies on the likelihood of accidents is studied. Pan et al. analyze in [16] the contribution of the crew to the accident rate including socio-technical variables (such as the behavior pattern of pilots). In [17], Zhang et al. develop a data-driven BN model in order to study the causal relationships which contribute to commercial aircraft accidents. The model considers many types of accidents and captures their consequences in terms of aircraft damage, mechanical or electrical components failures and human factor contribution. In [18,19], a model is established for the prediction of aircraft-to-aircraft incidents based on Bayesian Networks. As can be seen, most studies are based on the analysis of accidents, while the study of the ATM system using Bayesian Networks from incident data has not been very common so far.

An observation should be made regarding studies of contributing factors in ATM incidents/accidents. From data analysis, information about contributing factors may be available when the incident or accident has occurred, but situations where these factors have been present but have not triggered an incident/accident are not known. For this reason, the aim of this work is to identify those factors that contribute to the criticality of a LOS (how close the LOS has come to becoming a collision) based on Bayesian Networks. To this end, a new absolute metric has been defined called "LOS criticality", which allows us to establish four clearly defined categories depending on the proximity to collision. Based on information about the elements that most influence the most critical separation

infringements, it is possible to exclude the irrelevant factors and prioritize work on the most important ones in order to increase ATM safety. This study is organized as follows: the second section presents the methodology followed, that is, dataset generation, a statistical analysis of the data and the model designed with its validation. Subsequently, a discussion of the results obtained is presented. The conclusions and further work proposals are provided in the fourth section.

# 2. Methodology 

The methodology followed in this study for the building and validation of the model is reflected in the following flowchart (Figure 1). The first step is the collection and processing of data from official incident reports and the building of the database. In the second step, the definition of the study variables and an exploratory analysis of these variables is conducted in order to get a better understanding of their behavior. In the third step the network is constructed qualitatively (structure) and quantitatively (conditional probabilities). Finally, the model is validated using the software's validation functionality and expert verification on the results obtained.
![img-0.jpeg](img-0.jpeg)

Figure 1. Methodology steps for the generation of the model.

### 2.1. Data Collection and Database Generation

Reporting and investigation of aircraft incidents are relevant and essential elements in the Safety Management System of ATM. They provide fundamental information that allows the identification of risks and the detection of common patterns. In this way, it is possible to optimize efforts for safety improvements. For the dataset building, incidents published in the period 2012-2019 by the state commission for the study and analysis of incidents in a specific country were analyzed. Names and other identifying information have been omitted to maintain required confidentiality. Incident reports generally follow a publication pattern according to the ICAO's considerations [20,21], in which three different parts are distinguished:

1. Scenario-related information (date and time, airspace where it occurred, meteorological conditions, aircraft models, etc.), communications (crew-ATCo) and radar traces.
2. Extracts of the testimonial reports of the agents involved: crew and ATCo.
3. Rating of the incident (severity and frequency), conclusions and recommendations.

The ATM incident investigation reports published within the study period were considered and classified according to three main categories specified by EUROCONTROL in ESARR 2 [22]: incident category (AIRPROX), type of flight (commercial traffic) and incident severity (A (serious) or B (major)), according to the classifications established in [6].

Since the scope of this study is restricted to the analysis of serious and major incidents (near collisions) between aircraft pairs in en-route airspace (only commercial traffic was considered, excluding VFR traffic and military aviation), the first screening was filtered. The resulting incidents kept for study were only those involving just two aircraft and taking place in sectors corresponding to en-route airspaces, where the separation minima prescribed are 5 NM in the horizontal dimension and 1000 ft in the vertical dimension.

For the extraction, classification and temporal organization of the contributing factors, the Systemic Occurrence Analysis Methodology (SOAM) was used. According to [23], this is a common methodology for the identification of causal factors across the aviation industry. It is a modification from Reason's Model, studied by Licu et al. [24] and validated by EUROCONTROL, which allows human involvement to be considered in the analysis of accidents and to detect the deeper latent conditions of the organization that set the context for the event. Finally, the database was made up of 82 incidents (out of a total of

560 incidents, most of them involving VFR traffic), as these were the ones that fulfilled the established conditions.

According to aviation statistics related to the airspace analyzed where data have been taken [25], the total number of IFR flights in the 2012-2019 period was 20.343 million while the total flight time was $7,910,383 \mathrm{~h}$. Therefore, the odds of LOS are $4.03 \times 10^{-6}$ per flight and $1.04 \times 10^{-5}$ per flight hour. These probabilities are also broken down by the ACCs (area control centers) of the airspace considered in this research (Table 1).

Table 1. Odds for LOS/Flight and LOS/Flight hour per ACC.


Based on these values, it can be seen that these are very low-frequency events. This property must be considered later for the analysis of the results, in order to be able to contextualize and assess them from the appropriate point of view.

# 2.2. Definition of the Research Variables and Exploratoy Data Analysis 

This section is divided into two sections. First, a description is given of the variables considered in the research, which constitute the database. Subsequently, an exploratory analysis of these variables is performed.

### 2.2.1. Definition of the Research Variables

The database generated from the incident analysis consists of a total of 82 records (incidents analyzed) and for this study the following 14 variables were considered:

- Month: in which the incident occurred.
- Year: in which the incident occurred.
- Time slot: time period during the day in which the incident occurred (UTC time).
- Weather conditions: existing when the incident occurred.
- Airspace: ACC where the incident took place (ACC 1, ACC 2, ACC 3 and ACC 4). The name of the ACC is ordered from 1 to 4 according to the traffic volume in each ACC, with ACC 1 being the one with the highest traffic and ACC 4 the one with the lowest traffic during the study period.
- Communication issues: technical failure or error related to the communication system, such as frequency failure (connection of Push to Talk pedal, PTT), poor transmission/reception quality, congestion, etc.
- ATCS ergonomics: Automated Air Traffic Control System ergonomics. This software is used by ANSP for air traffic management through the provision of air traffic services (ATS). This factor refers to the range of colors in which information is presented by Automated Air Traffic Control System in the screen of the ATCo work position. It is considered because it has been proven during the incident analysis that the ergonomic configuration of the system sometimes leads to confusion for the ATCo (e.g., the color of the labels for aircraft assumed, not assumed, transferred, etc.). This is mentioned several times by ATCos in the testimonial part of the incident reports. Therefore, no value judgments have been made for the recording of this variable.
- STCA: Short Term Conflict Alert Tool for conflict detection by ATCo. It is a system which supports ATCo to detect conflicts (a situation in which separation minima could be compromised) and separation infringements. The system issues a conflict alert

(PAC) based on predictions and a violation LOS alarm (VAC) when the separation infringement has taken place.

- TCAS: Traffic and Collision Avoidance System. On-board system which issues a TA alert (Traffic Advisory) and a RA alarm (Resolution Advisory).
- ATC error: it refers to an error made by ATC that contributed to the occurrence of the LOS. It has been extracted from the analysis and investigation of the reports applying the SOAM methodology.
- Crew error: it refers to an error made by the crew that contributed to the occurrence of the LOS. It has been extracted from the analysis and investigation of the reports applying the SOAM methodology.
- Encounter geometry: as a function of the angle between aircraft tracks (Figure 2). There are three possible geometries, according to the ICAO PANS-ATM document [20]: same tracks, opposite tracks or convergent tracks. Since this information is vague in the reports and the geometry between aircraft is only mentioned theoretically as "crossing, same or reciprocal track", the angle between tracks has been studied to validate the classification, based on the trajectories simulated by RAMS Plus software [26].
- Sector overload: situation in which the number of aircraft in the sector, at the time of the incident, exceeded the declared capacity of the sector. This information has been extracted from the ATCos' testimonial extracts from the incident reports analyzed. In order to make this variable more objective, this information has been contrasted with that obtained in NEST tool [27], a simulation software developed by EUROCONTROL, on the state of the sector at the time of the incident. Only those cases in which NEST showed that the sector was overloaded were recorded in the dataset. In Figure 3, it can be seen that in several periods throughout the day the number of entries in the sector (one of the ACC 1 sectors) exceeded the declared capacity. The graph below shows the overload of the sector by hours (number of aircraft in excess of the declared capacity) on the day of the LOS.
- LOS Criticality: metric related to the severity of the loss of separation. This variable refers to how close the LOS has come to being a collision. It is an indicator associated with the minimum horizontal and vertical separation reached in the conflict, with values ranging from 0 to 1 . The steps followed for the definition of this metric were:

1. Definition of ten equal length intervals in the ranges $0-5 \mathrm{NM}$ and $0-1000 \mathrm{ft}$. The lower limit of the range refers to the distance of 0 (NM or ft) between aircraft (collision) while the upper limit corresponds to the separation minima values in the horizontal ( 5 NM ) and vertical ( 1000 ft ) dimensions for en-route airspace. In the horizontal dimension the intervals are in 0.5 NM increments, while in the vertical dimension they are 100 ft .
2. Normalization (scale of $0-1$ ) of the horizontal intervals $\left(\operatorname{Sep}_{\text {NormH }}\right)$ and vertical intervals $\left(\operatorname{Sep}_{\text {NormV }}\right)$ (Equation (1)).

$$
\operatorname{Sep}_{\text {NormH }}=\frac{\operatorname{Sep} \operatorname{Int}_{H}}{\operatorname{Sep} \min _{H}}, \operatorname{Sep}_{\text {NormV }}=\frac{\operatorname{Sep} \operatorname{Int}_{V}}{\operatorname{Sep} \min _{V}}
$$

where:
Sep $\operatorname{Int}_{H}=$ upper limit value of the interval (first column of Figure 4) in the horizontal dimension.
Sep $\operatorname{Int}_{V}=$ upper limit value of the interval (first row of Figure 4) in the vertical dimension.
$\operatorname{Sep} \min _{H}=$ Separation minima in the horizontal dimension ( 5 NM).
$\operatorname{Sep} \min _{V}=$ Separation minima in the vertical dimension ( 1000 ft ).
3. Calculation of the oblique distance, from Equation (2), between the values obtained in the previous step. These values are shown in Figure 4.

$$
\text { Oblique distance }=\sqrt{\left(\operatorname{Sep}_{\text {NormH }}\right)^{2}+\left(\operatorname{Sep}_{\text {NormV }}\right)^{2}}
$$

4. The criticality array is obtained by normalizing the array obtained in step 3 (since the highest value is $1.4 \approx(\sqrt{2})$, this is the one used for normalization) and subtracting unity from all values, according to Equation (3).

$$
\text { LOS Criticality }=1-\left(\frac{\text { Oblique distance }}{\sqrt{2}}\right)
$$

where:
Oblique distance $=$ obtained in the previous step
$\sqrt{2} \approx 1.4=$ value used to normalize the array, as a result of $\sqrt{\left(\frac{S N M}{S N M}\right)^{2}+\left(\frac{1000 f t}{1000 f t}\right)^{2}}$
![img-1.jpeg](img-1.jpeg)

Figure 2. Encounter geometries.
![img-2.jpeg](img-2.jpeg)

Figure 3. Analysis of the sector overload from NEST. Incident A (07:43 UTC).

![img-3.jpeg](img-3.jpeg)

Figure 4. Oblique distance between interval ranges.
The criticality array obtained is shown in Figure 5, in which a heat map has been generated, which is similar to a risk matrix for this indicator. Values closer to 1 indicate that the separation minima reached in the encounter between aircraft pair was very small and a near-collision occurred. Values close to 0 indicate that the separation minima between the aircraft were practically not violated. Thus, the LOS criticality is classified as:

Minor - [0.01, 0.29] Hazardous - [0.50, 0.69]
Major - [0.30, 0.49] Catastrophic - [0.70, 1.00]
![img-4.jpeg](img-4.jpeg)

Figure 5. Risk array for LOS criticality.
Therefore, the criticality of the incidents analyzed is obtained from the minimum separation reached in each LOS (Equation (4)) and the categories defined from the risk array (Figure 5).

$$
\text { LOS Criticality }=1-\left(\frac{\sqrt{\left(\frac{\text { Sep } L O S_{H}}{\text { Sep } \min _{H}}\right)^{2}+\left(\frac{\text { Sep } L O S_{V}}{\text { Sep } \min _{V}}\right)^{2}}}{\sqrt{\left(\frac{\text { Sep } \min _{H}}{\text { Sep } \min _{H}}\right)^{2}+\left(\frac{\text { Sep } \min _{V}}{\text { Sep } \min _{V}}\right)^{2}}}\right)
$$

where:
Sep $L O S_{H}=$ horizontal separation reached in the LOS between aircraft pair.
Sep $L O S_{V}=$ vertical separation reached in the LOS between aircraft pair.
Sep $\min _{H}=$ Separation minima in the horizontal dimension, 5 NM .
Sep $\min _{V}=$ Separation minima in the horizontal dimension, 1000 ft .

For instance, for the case of a separation infringement in which the minimum separation between aircraft was 3 NM and 600 ft the criticality would be, according to Figure 5 and Equation (4):

$$
\text { LOS Criticality }=1-\left(\frac{\sqrt{\left(\frac{3 N M}{5 N M}\right)^{2}+\left(\frac{600 f t}{1000 f t}\right)^{2}}}{\sqrt{\left(\frac{5 N M}{5 N M}\right)^{2}+\left(\frac{1000 f t}{1000 f t}\right)^{2}}}\right)=0.4 \text { MAJOR Criticality }
$$

# 2.2.2. Exploratory Data Analysis 

The purpose of exploratory data analysis is to obtain information about the data and to extract knowledge from an initial analysis of the sample using statistical methods and graphical tools. As this database consists of discrete variables, the exploratory analysis of the data is limited only to the frequency of the different states of the variables. In this part of the study, first an analysis of the frequency of the different states of each variable is presented. Afterwards, other analyses were performed (analysis of the time distribution, spatial distribution, geometry of the encounter, etc.) which were important to understand certain results of the BN model.

- Study of the frequency of the states of some variables

Table 2 lists the frequency distributions of the variables describing the characteristics of the LOS scenario: airspace, encounter geometry, weather conditions, and sector overload. This analysis was useful to contextualize the incidents. It can be seen from Table 2 that the number of incidents in ACC 1 (highest traffic volume) is almost double that of ACC 2. Moreover, it is observed that most incidents occurred in good weather and when sectors were not overloaded. In addition, in most of the incidents the aircraft were on reciprocal (opposite) tracks.

Table 2. Frequency distributions for qualitative variables which describe scenario characteristics.


Table 3 lists the frequency distributions of the variables describing the safety nets behavior. Since en-route incidents were analyzed, the safety nets considered were the STCA system and the TCAS system. The objective of these systems is to prevent a precursor from becoming a collision. For this reason, it is important to know how they have performed.

Regarding the TCAS system, the total number of triggered Traffic Alerts (TA), Resolution Alerts (RA) and when the system has not been activated is considered. About STCA, which is the system that supports the ATCo task for conflict detection, the parameters considered concern the triggered Conflict Alert (PAC), LOS Alarm (VAC), alerts triggered but ignored by ATCo, if the system was inhibited in the airspace, failures of the system, and alert omissions.

Table 3. Frequency distributions for qualitative variables which describe the safety nets behavior.


Table 4 lists the frequency distributions of the variables associated with the human factor and the technical systems. On the one hand, the frequency of crew error and ATCo is studied. It can be seen that the ATC error is greater than the crew error. This is as expected, because the responsibility for the exercise of separation lies on the ATCo, while the crew generally follows the clearances issued by the ATCo. On the other hand, the variables associated with the technical systems are related to the communication issue and the Automated Air Traffic Management System. The latter variable is not so much related to software errors as to the ergonomics of the system, which misleads the ATCo on some occasions.

Table 4. Frequency distribution of the node states representing the causal factors of the incidents.


Finally, Table 5 lists the frequency distributions of the target variable, which is LOS criticality. From the values of the minimum horizontal and vertical separation of each LOS, the four criticality states of the variable have been obtained. It is noteworthy that the criticality of the majority of incidents corresponds to the Minor and Major categories.

Table 5. Frequency distribution of the target node LOS Criticality variables.


- Temporal and spatial distribution of incidents

Data analysis by month, season, time slot and ACC are shown in Figure 6. The temporal distribution of incidents by month does not demonstrate a clear relation between the number of incidents and the amount of traffic. However, this relation is clearer if the analysis is carried out by season. It is shown that during the winter season (November-March) the number of LOS is lower than in the summer season (April-October). Moreover, it is observed that the occurrence of incidents during the morning and midday is higher than during the rest of the day, in line with the fact that the peak traffic hours in the sectors are during the morning period. At night, there are clearly fewer problems, as there is almost no traffic. Finally, in line with Table 2, it can be seen that the highest number of incidents corresponds to the ACC with the most traffic. A preliminary hypothesis, to be confirmed by the model, yields that the number of incidents is proportional to the volume of traffic, as expected.
![img-5.jpeg](img-5.jpeg)

Figure 6. Distribution of incidents by month, season, time slot and ACC.

- Incident analysis by sector in the studied ACCs

Table 6 shows the results obtained from the characterization of incidents according to where they occurred, that is, whether in a single control sector or they occurred in different

sectors as a result of poor coordination. In this second category, poor coordination may have occurred between two sectors of the same ACC (also within this category it has been differentiated whether these sectors were upper-lower), or between sectors of different ACCs. This analyzed information is relevant. It is possible to know from this point of view about the behavior of the different ACCs and to detect possible hot spots.

Table 6. Incident characterization according to where it occurred (single control sector/more than one sector involved).


- Analysis of incident encounter geometry

For each incident included in the dataset, the angular difference between the tracks of the pair of aircraft was analyzed from the trajectories in RAMS Plus. It is observed (Figure 7) that in most of the incidents the angle between tracks is $180^{\circ}$. In the case of reciprocal tracks, angular differences between $135^{\circ}$ and $149^{\circ}$ are also frequent. The most frequent range of angles when the tracks are convergent is $105-120^{\circ}$, while for same tracks it is $0^{\circ}$. From the model it will be possible to deduce how the geometry of the encounter affects the criticality of the incident. Likewise, this information is beneficial to be able to establish future mitigation measures in order to reduce the probability of occurrence of an incident.

![img-6.jpeg](img-6.jpeg)

Figure 7. Angles between tracks for the different encounter geometries.

# 2.3. Building the Bayesian Network (BN) 

After obtaining the dataset and the exploratory data analysis of the database in the previous step, a probabilistic causal model was used to study the problem: Bayesian Networks. A Bayesian Network (BN) can be described, qualitatively, as a Directed Acyclic Graph (DAG). A DAG is a pair $G=(V, E)$, where $V$ is a set of nodes and $E$ is a set of arcs defined over the nodes. The nodes represent variables and are connected to each other by directed arcs. They start at the parent node and are directed to the child node. From a quantitative viewpoint (Equation (5)), in a Bayesian Network the probabilistic relationships between nodes are determined by a joint probability density function $F(V)$. This joint probability density function is visualized by the Conditional Probability Tables (CPT) that constitute the probabilistic structure of the network. An edge in a BN shows a probabilistic dependency between two nodes; however, it does not imply a causality relationship between them because causality is a relationship, which cannot be defined only from the joint distribution [28].

$$
F\left(V_{1}, \ldots, V_{N}\right)=\prod_{i=1}^{N} F\left(V_{i} \mid \operatorname{Parent}\left(V_{i}\right)\right)
$$

There are three main approaches to build a Bayesian network. The first approach is solely on the basis of expert judgment in which the network is constructed from human knowledge. The second is based on some learning algorithm which, applied on a database, establishes the relationships between the nodes. Finally, the third approach consists of merging the first and the second approaches. Increasingly, this last approach is being used especially for modelling very low-frequency problems and it is the one used in this study. Thus, the model has been built from the data (incidents database) and the experts' judgment (aerospace engineers, flight crews and ATCos).

Having briefly referred to the BN methodology, the building of the Bayesian Network is now explained. For the BN model constitution a process called Knowledge Engineering of Expert-based Bayesian Network (EKEBN) [29] was followed; this technique has been

employed in other projects to detect the ATC complexity metrics [9]. It consists of two main steps: (1) expert-based structure building, and (2) incidents database feeding uncertainty quantification.

1. Expert-based structure building provides the identification of all variables and causal correlations between them, as well as their states, that can be taken. Based on the identification of the variables by the experts, the list of research variables defined in the previous section is generated. This means that a part of the research variables has been obtained directly from the incident reports, and other variables, such as those related to Human Errors or LOS Criticality, have been identified or generated by expert knowledge. The identification of the causal correlation by expert knowledge among defined research variables has been considered a fundamental step for posterior Bayesian Network building in GeNIe software [30], particularly in definition of the BN architecture. This identification process has been repeated several times until the experts removed the inconsistencies and discrepancies, as explained in [9,29]. From this step, 14 variables have been considered relevant for the model building. Table 7 shows, in summary form, for each variable chosen as a node in the model, the number of states and their descriptions. As a result, the Bayesian Network structure was built as shown in Figure 8.
2. Incidents database feeding uncertainty quantification basically deals with the Conditional Probability Tables (CPT) estimation combining incidents database with expert-based BN architecture approach. In contrast to other similar research works like [31,32,33], this CPT estimation has proceeded directly with the incidents database applying the Bayesian Search algorithm provided in GeNIe. The algorithm follows essentially a hill climbing procedure (guided by a scoring heuristic, which in GeNIe is the log likelihood function) with random restarts [34]. The estimated BN, which depicts the nodes, their levels and probabilities, is shown in Figure 9.
![img-7.jpeg](img-7.jpeg)

Figure 8. Expert-based BN architecture.

Table 7. Nodes and associated states for incident analysis.


![img-8.jpeg](img-8.jpeg)

Figure 9. Graphical representation of the BN considered.

In summary, this technique is especially used to model very low frequency problems. In this study the database contains only 82 incident records, so this technique is applicable in this case. Consequently, as a hybrid model, it has been built from data (incident database) and expert judgement (aerospace engineers, flight crews and ATCos). Therefore, a different model validation process is also required.

# 2.4. Model Validation 

In this research, the validation of this hybrid BN model has been divided into two parts:
(1) Test only validation for expert-based and data-driven consistency in the BN model.
(2) Expert-based final validation.

1. Test only validation is a GeNIe software algorithm used specifically to validate expert-based BN models [30,34]. Particularly, this method has been applied to the BN model in order to check the consistency between expert-based architecture and data-driven modelling results. Receiver Operating Characteristic curve (ROC) and the Area Under the ROC Curve (AUC) in the target variable (LOS_Criticality) have been calculated to assess the accuracy of this consistency. In BN, the ROC curves are generally used to depict the model performance [35]. A ROC curve is a graphical tool defined by True Positive Rate (TPR, also called sensitivity) on the vertical axis and the False Positive Rate (FPR, also called specificity) on the horizontal axis. The TPR (Equation (6)) is defined as the ratio between the total number of correctly identified positive cases (True Positive, TP) and the total number of positive cases (True Positive (TP) + False Negative $(\mathrm{FN})$ ), while the FPR (Equation (7)) is defined as the ratio of the total number of negative cases incorrectly identified as positive cases (False Positive, FP) and the total number of negative cases (False Positive (FP) + True Negatives (TN)). The results obtained from validating the model are shown in Figure 10.

$$
\begin{aligned}
& T P R=\frac{T P}{T P+F N} \\
& F P R=\frac{F P}{F P+T N}
\end{aligned}
$$

It is observed that the highest AUC value is obtained for the CAT (Catastrophic) state of the target variable. This state is the critical one (representing the transition from a LOS scenario to a MAC scenario); its value is close to 0.85 , while for the rest of the states the AUC value is close to 0.7 . According to [36,37], these scores are high (around $70-80 \%$ ). This check result shows the high consistency between expert knowledge and data-driven for the CAT state, which allows us to better understand which factors contribute to a more critical incident (nearcollision). And, ultimately, based on this information it is possible to exclude the irrelevant factors and to prioritize future work on the most important ones in order to increase ATM safety.
2. Expert-based final validation consists of the validation of BN architecture (previous to applying the incidents database for CPT estimation) and the verification of the BN model once the Test only validation is concluded. The validation of BN architecture has been concluded as the last step of expert-based structure building described previously. Rather than an isolated validation process, it has been performed as part of the BN structure building process. The experiences of aeronautical engineers, pilots and air traffic controllers aided in achieving this definitive BN architecture. In addition to the validation of the model with the specific functionality of the software, expert verification has been applied to the results obtained, which will be presented in the following section. Since the results obtained from the model are consistent with the expectations of the experts, it is possible to validate the model on the basis of these results.

![img-9.jpeg](img-9.jpeg)

Figure 10. ROC curves of the target variable stages for the validation of the model.

# 3. Results 

This section provides the results obtained from the proposed model based on BN and the analysis of the generated database. Regarding the degree of influence of the network nodes on the target variable, the system confirms that the variables with the highest influence on the LOS Criticality target node, as expected, are ATC error, crew error, communications issues and TCAS (Figure 11). Strength of influence is calculated from the CPT of the child node and essentially expresses the distance between various conditional probability distributions over the child node conditional on the states of the parent node [34]. The measure of distance between distributions used has been the Euclidean one.
![img-10.jpeg](img-10.jpeg)

Figure 11. Strength of influence on the node of the target variable.

In Bayesian Networks, after propagating the evidence through the network, conditional probabilities for the levels of any node can be obtained. The probabilities of the different states of the nodes are a consequence of the sample, here 82 incidents. Therefore, the results obtained by fixing evidence (setting probability of 1 to a state of a variable) and as a consequence of the network, must be interpreted, not so much in their numerical value but in the trend or variation that they experience. On account of this, the following most relevant results can be seen from the model:

- From the data analysis it is noteworthy that the probability of the LOS occurrence is proportional to the traffic volume density, as expected. The results show that probability of LOS per movement is greater in those ACC with more traffic. The highest number of LOS took place during the summer season when traffic volume reaches its peak value, according to EUROCONTROL statistics [25]. On the daily time horizon, LOS likelihood is higher in the morning and midday periods (almost $80 \%$ of LOS) when the traffic volume far exceeds those of the afternoon and night. Such data were provided by EUROCONTROL AIRAC publications and were visualized in NEST.
- In relation to the target node, by setting the evidence in each of its states it is possible to know the contributing factors to minor, major, hazardous and catastrophic criticality of LOS. It can be shown that the probability of an incident occurring as a result of ATC error is much higher than due to crew error or communications issues in each scenario (Minor, Major, Hazardous and Catastrophic), as indicated in Table 8. Due to the BN characteristics and properties, these results must be interpreted independently for each scenario. Results obtained are in accordance with the roles established in a scenario with surveillance: the separation responsibility lies with the ATCo, while the crew is limited to executing the clearances issued by the ATCo. The probability of a LOS as a result of crew error or due to a communications issue is roughly similar, with the communications issues being slightly lower. However, these results need to be contextualized as they are events with a low probability of occurrence. The current ATM system architecture is configured in a way that minimizes system errors: redundancy of equipment, mandatory and recommended required performances, certification of equipment, certification of manufacturing companies, etc. Furthermore, it is worth considering that in this study, after analyzing the incidents that constitute the database, no variables relating to surveillance or navigation have been established because no technical errors in these systems have been found to have given rise to a LOS.
- Focusing on the above contributing factors (setting evidence on ATC_error, CREW_error and COM_issues), it is possible to know the probability of different LOS Criticality scenarios as a consequence of them and the rest of the network. As can be seen (Table 9), when an ATC error takes place, the LOS criticality generally has a low probability of being catastrophic. However, when a crew error or communication failure takes place, the LOS criticality is slightly more severe (hazardous and catastrophic). Therefore, it can be stated that the probability of ATC error is more frequent, but its criticality is generally less severe in comparison with other contributing factors. From all these probabilistic results it can be concluded that the influence of technical means is negligible. Therefore, mitigating measures to reduce the risk of a MAC should focus on the human factor, and particularly on ATC.
- The BN model shows the relation between weather conditions, communication issues and sector overload and the influence on ATC performance. When there are storms or turbulence phenomena, there are, generally, congestion problems; aircraft deviate from their planned routes, producing an overload in certain areas of the sector. Therefore, there is an overload of communications. In these situations, it is observed that while the probability of communications issues increases considerably (compared to when there are no relevant weather phenomena), and the probability of sector overload increases considerably, ATC error decreases moderately (Table 10). This contrast occurs

especially with the occurrence of turbulence. Contrary to what might be expected with respect to ATC error, the model shows that it seems that ATCos perform better when the situation is more adverse, with the probability of a LOS as a result of the ATC error being lower than in ordinary situations, where overconfidence may occur. Expert opinion (ATCos and flight crews) confirmed that the most demanding scenarios require maximum concentration, thus reducing the probability of error. Therefore, on the basis of these model results, possible safety-enhancing measures should be aimed at encouraging the human factor during the working period, and during normal situations to try to pay more attention and to maintain it during the working time.

Table 8. Human factor and COM_issues contributing factors' probability for LOS criticality.


Table 9. LOS Criticality probabilities related to human factors and COM_issues.


Table 10. Probability relation between nodes Weather_conditions and ATC_error, Sector_overload and COM_issues.


Once the behavior of the previous contributing factors has been studied, it is relevant to know the contribution of the performance of the existing barriers (safety nets: STCA and TCAS) in the defined LOS categories.

- Regarding the STCA, it is observed that when the system issues the VAC alarm on the ATCo display the probability of a catastrophic criticality LOS is lower than when this alarm is not issued. Moreover, the probability of failure of STCA alerting a LOS increases considerably (more than $20 \%$ ) when the factor of the ergonomics of the Automated Air Traffic Control System is present. As explained above, the ergonomics factor refers to the range of colors in which information is presented in the Automated Air Traffic Control System. However, indirectly this factor refers to the transfer of

aircraft between sectors. Therefore, what is highlighted in the relationship between these two nodes is that, on the basis of the STCA functionality, it seems that when aircraft are transferred to other sectors, the STCA does not always detect that a LOS may occur between an assumed aircraft and a transferred aircraft (which is still flying within the boundaries of the sector under consideration). Therefore, the system does not alert controllers of the conflict. This result is consistent with the development of the STCA that, in some versions, it does not detect LOS between aircraft assumed by nearby control sectors. Not all ANSPs have the same support systems or the same degree of evolution in them. Therefore, this STCA limitation is a hot spot for the occurrence of aircraft separation losses in inter-sector coordination situations and may be considered by those ANSPs that do not have this system functionality as a mitigating measure for LOS occurrence. Technical reports from the ANSP managing the airspace where the incidents analyzed occurred have been investigated. These reports indicate that there was a system upgrade in 2020 by which this gap has been resolved. Therefore, this output validates the results emerging from the network for this node.

- Concerning the other safety net considered in this study and from the BN, it is observed (Table 11) that when the TCAS system issues a RA, the probability of occurrence of a catastrophic incident decreases considerably, by more than half, in comparison to when this anti-collision system does not issue any alert. The higher probabilities correspond to a lower criticality, which means that when the TCAS RA is activated, the separation breach is resolved correctly and promptly (without escalating to a more critical category). As expected, this result demonstrates that the TCAS system reduces the risk of MAC occurrence and demonstrates the effectiveness of this barrier. The activation of this system, in particular the resolution warning, implies a low probability that the LOS will be of catastrophic criticality.

Table 11. LOS Criticality probabilities related to TCAS behavior.


# 4. Conclusions 

In this paper, a Bayesian Network-Based model is proposed for the analysis of aircraft incidents. The aim was to identify the factors that contribute to a LOS between aircraft and how they influence the LOS criticality (how close the LOS has come to being a collision). Based on this information it is possible to exclude the irrelevant factors and to prioritize work (establishing mitigation measures) on the most important ones in order to increase ATM safety. The building of the model was based on expert judgement from aerospace engineers, flight crews and ATCos, and on data from an incident database which was built from the analysis of 82 aircraft incident investigation reports using GeNIe software. When analyzing LPHC events it is necessary, on the one hand, to have accurate data in order to be able to draw conclusions that are more applicable to reality. On the other hand, a main difficulty to be faced is the scarcity of data.

The model validation yields more than acceptable AUC values for the "Minor", "Major" and "Hazardous" states of the target variable, while the AUC value for the most severe state of LOS criticality, which is "Catastrophic", is high. This means that the model is good at identifying the factors that can lead to a very serious incident (near-collision).

The results were obtained from both the analysis of the data and the model developed. Some of the most relevant conclusions inferred are related to the concept of "self-confidence" of the human factor. Contrary to what might be expected, the probability of an incident occurring as a result of human factor error under adverse conditions is lower than under normal conditions. Similarly, it is observed that the probability of incidents occurring as a result of human factor error is much higher than due to an error related to technical systems (Communications, Navigation or Surveillance systems, CNS). It should be noted that in the analysis performed, almost no CNS errors were detected. Among these, the most frequent was a failure due to communications. Furthermore, it was demonstrated from the model outputs that the STCA system, which assists ATCo in the detection of separation infringements, may not have some functionality that is essential for LOS detection (detection of LOS between aircraft assumed and transferred by different control positions). In addition, it is noteworthy that in the case of systems that support controllers, there is not the same degree of uniformity as with respect to the systems required for aircraft (such as TCAS, which all aircraft must carry since a specific date, and the version required by the regulations, i.e., TCAS 7.1). Finally, and as expected, the effectiveness of the TCAS system was verified on the basis of the model: the probability that the LOS criticality is catastrophic is reduced by more than half when TCAS issues a RA alarm compared to when it does not issue an alert.

In addition to the above findings, areas have been identified where research could be improved and on which future work could focus: (1) increasing the number of samples to improve the robustness of the model and the use of data from other airspaces for the purpose of constituting a general model; (2) the development of sub-networks to provide a more detailed understanding of those ATC and crew activities that contribute to LOS criticality; and (3) the introduction of new incident variables such as aircraft exposure time below separation minima, resolution time, time of RA alarm, etc., which may be of relevance for a better estimation of LOS criticality.

Author Contributions: Conceptualization, L.S.-M., E.S.A., J.A.P.-C. and L.P.-S.; methodology, L.S.-M., M.P.M. and S.Z.Y.L.-C.; software, L.S.-M. and M.P.M.; validation, E.S.A., J.A.P.-C., S.Z.Y.L.-C., V.G.A. and L.P.-S.; investigation, L.S.-M. and J.A.P.-C.; resources S.Z.Y.L.-C., V.G.A. and L.P.-S.; data curation, L.S.-M. and M.P.M.; writing-original draft preparation, L.S.-M.; writing-review and editing, M.P.M., E.S.A., J.A.P.-C., S.Z.Y.L.-C. and L.P.-S.; supervision, L.P.-S. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
