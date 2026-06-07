Nat. Hazards Earth Syst. Sci., 22, 227-244, 2022
https://doi.org/10.5194/nhess-22-227-2022
(c) Author(s) 2022. This work is distributed under the Creative Commons Attribution 4.0 License.

## Index establishment and capability evaluation of space-air-ground remote sensing cooperation in geohazard emergency response

Yahong Liu ${ }^{1}$ and Jin Zhang ${ }^{2}$<br>${ }^{1}$ Department of Earth Science and Engineering, Taiyuan University of Technology, Taiyuan 030024, China<br>${ }^{2}$ Department of Surveying and Mapping Science and Technology, Taiyuan University of Technology, Taiyuan 030024, China

Correspondence: Jin Zhang (zjgps@163.com)
Received: 12 September 2020 - Discussion started: 19 October 2020
Revised: 13 December 2021 - Accepted: 20 December 2021 - Published: 31 January 2022


#### Abstract

Geohazard emergency response is a disaster event management act that is multifactorial, time critical, task intensive and socially significant. To improve the rationalization and standardization of space-air-ground remote sensing collaborative observations in geohazard emergency responses, this paper comprehensively analyzes the technical resources of remote sensors and emergency service systems and establishes a database of technical and service evaluation indexes using MySQL (Structured Query Language). Based on the database, we propose the method of using the technique for order preference by similarity to an ideal solution (TOPSIS) and a Bayesian network to evaluate the synergistic observation effectiveness and service capability of remote sensing technology in geohazard emergency response, respectively. We demonstrate through experiments that using this evaluation can effectively grasp the operation and task completion of remote sensing cooperative technology in geohazard emergency response. This provides a decision basis for the synergistic planning work of heterogeneous sensors in geohazard emergency response.


## 1 Introduction

Geohazards include earthquakes, landslides, debris flows, ground subsidence, lava flows and other hazards related to geological processes that endanger people's lives and property and are caused by natural factors or human activities. According to the United Nations Office for Disaster Risk Reduction (UNDRR), the human casualties caused by geological hazards since 1990 have been concentrated in the AsiaPacific region and Africa for a long time, with 2010-2019
being the decade with the highest economic losses caused by disasters (UNDRR, 2019a, b). To respond to sudden geological hazards and mitigate damage, it is necessary to carry out hazard emergency response quickly after the occurrence of a hazard, provide emergency assistance for victims, and seek to stabilize the situation and reduce the probability of secondary damage (Johnson, 2000).

Earth observation technology provides key technical support during geohazard emergency response (Butler, 2005). With the development of global Earth observation technology, the performance of remote sensing technology is constantly improving; the number of sensors continues to increase; and a multiplatform observation system for satellites, aerials, unmanned aerial systems (UASs) and the ground has gradually been established (Toth and Jóźków, 2016). There are many online resources for recording remote sensing information, and the NASA master directory (NSSDC, 2020) provides a mechanism for retrieving satellite names, classifications or launch dates to obtain descriptions of relevant satellite information and data collection. The Committee on Earth Observation Satellites (CEOS) Missions, Instruments, and Measurements (MIM) Database is divided into Agencies, Missions, Instruments, Measurement and Datasets modules with a focus on current and future satellites, sensors and measurement capabilities (CEOS, 2020). The Observing Systems Capability Analysis and Review tool (OSCAR, 2020) database is divided into a description of information about the satellite and its sensors and a sensor capability assessment analysis.

At present, most of the Earth observation technology resources operate independently, and when faced with specific geohazard emergency response tasks, the space-air-ground

remote sensor resources show both "many" and "few". That is, although sensor resources are abundant, it is difficult to find suitable and available sensors quickly, and this affects the efficiency of observing mission responses. The main reason is that remote sensing systems of various types are very different in terms of observation modes, applications and processing methods. In addition, resources are deployed in a distributed fashion, are described in their own independent formats, lack correlation mechanisms and cannot be detected in a timely manner (Li et al., 2012). To improve the efficiency of emergency response, a number of organizations and mechanisms have been established internationally to synergize these resources, including the Committee on Earth Observation Satellites (CEOS), Integrated Global Observing Strategy (IGOS), International Charter Space and Major Disasters (CHARTER), and United Nations International Strategy for Disaster Reduction (UNISDR). The International Strategy for Disaster Reduction (UNISDR), United Nations Platform for Space-based Information for Disaster Management and Emergency Response (UN-SPIDER), Disaster Monitoring Constellation (DMC) and Copernicus Emergency Management System (EMS) are mainly oriented to international major disaster emergency responses such as the Wenchuan earthquake (Pan and Tang, 2010), Haiti earthquake (Duda and Jones, 2011) and Japan earthquake (Kaku et al., 2015). In addition to establishing a collaborative emergency response with satellite remote sensing, in the face of the diversified needs of an actual geohazard emergency response, collaboration between satellites and other multiple remote sensing platforms has become an important development direction of remote sensing technology (Li et al., 2017). This is characterized by the ability to integrate the observation advantages of each platform to effectively shorten the observation time, expand the coverage and improve the accuracy of observation data (Asner et al., 2012; Nagai et al., 2009).

Haghighi and Motagh (2019) used multi-SAR (synthetic-aperture radar) satellite sensors for the analysis of spatial and temporal processes of ground subsidence in the Iranian region of Drangheh; Hermle et al. (2021) used to verify the feasibility of optical remote sensing in landslide hazard warnings through a combination of high-resolution satellite and UAV data; and Lu et al. (2019) mapped landslide inventories based on multi-remote sensing sensor data. Ventisette et al. (2015) described data acquisition using satellite and ground-based sensors in landslide disaster response, and Huang et al. (2017) proposed a complete set of methods for geohazard emergency investigation using UASs. In these remote sensing collaborative disaster emergency applications, by linking different types of remote sensors and coupling them to form an independent and dynamically adaptable and configurable space-air-ground remote sensing collaborative observation system, the complementary advantages of remote sensing observation platforms are brought into full play. However, there is no sensor discovery process in these stud-
ies, and there is a lack of selection criteria and capability evaluation of sensors in different collaborative applications.

The observation tasks under geohazard emergencies are complex and diverse and have certain requirements in terms of timeliness and accuracy, and it is especially important for decision makers to make comprehensive discoveries and to establish accurate collaborative planning and rapid scheduling of massive sensors in a specific emergency response situation. How to quickly and rationally arrange the sensors that meet the geohazard emergency response needs in the sensor web environment to optimize resource utilization is the key issue in remote sensing collaborative observation. This work focuses on establishing a link between geohazard emergency response events and sensors, constructing indicators for evaluating the technical capabilities of sensors, and evaluating geohazard emergency service capabilities. Wang et al. (2013) proposed a mission-oriented assessment of the observational capabilities of imaging satellite sensor applications with the horizontal resolution, revisit period and observation error as indicators. Fan et al. (2015) proposed a sensor capability representation model to describe typical remote sensor capabilities for soil moisture detection applications. Zhang et al. (2019) proposed a model for evaluating the effectiveness of observations and data downlinks for low-orbiting satellites. Hu et al. (2019) constructed the observation capability information association model (OCIAM) for the selection of sensors and their combinations and further proposed the sensor observation capability object field (SOCO-Field) to construct sensor associations for a specific emergent geographical environment observation task (GeoTask) (Hu et al., 2020), and Wang et al. (2020) introduced the space-ground maximal coverage model with multiple parameters (SGMCMP) to complete sensor mission planning. The current research data on remote sensor capabilities are relatively scarce and focus on evaluating the inherent capabilities of individual satellite remote sensors with a single object of evaluation, making it difficult to meet the needs of multisensor and multigeohazard emergency response tasks. Thus, it is necessary and timely to establish collaborative observation capability indexes for space-air-ground remote sensor resources and to conduct evaluations of geohazard emergency response service capabilities.

## 2 Data

Given the richness of remote sensor technology resources, the service system for emergency response to geohazards has been improved in application practice. An important question is how to fully discover and use the existing sensor technology to meet the target observation needs and achieve the optimal effect of resource utilization for different application services. To allocate sensor resources scientifically, improve the rationality and effectiveness of cooperative observation, and obtain the required information to a greater extent, this sec-

tion establishes an index database for comprehensive analysis of the technical performance and emergency service system of space–air–ground remote sensing and realizes the integrated management of the technical performance data of various types of remote sensors and emergency service information.

### 2.1 Sensor technology resource emergency service system

Current remote sensors can be divided into satellite, aerial and terrestrial types according to the platforms on which they are mounted (Grün, 2008). Satellite remote sensing is divided into land satellites, meteorological satellites and ocean satellites according to their fields of operation. Land satellites are mainly used to detect the resources and environment on Earth's surface and contain a variety of sensor types such as panchromatic, multispectral, hyperspectral, infrared, synthetic-aperture radar, video and luminescence (Belward and Skoien, 2015). Meteorological satellites observe Earth and its atmosphere, and their operations can be divided into Sun-synchronous polar orbit and geosynchronous orbit (NSMC, 2020; Wang et al., 2018). Oceanic satellites are dedicated satellites that detect oceanic elements and the marine environment with optical payloads generally including watercolor water thermometers and coastal zone imagers and microwave payloads including scatterometers, radiometers, altimeters and SAR (Fu et al., 2019). The countries and regions in the world that currently have autonomous remote sensing satellites include the United States, France, ESA members, Germany, Israel, Canada, Russia, China, Japan, South Korea and India. The main satellite launches are shown in Table A1. Aerial remote sensing is a technology that uses aircraft, airships and UAVs as sensor carriers for detection (Colomina and Molina, 2014). Different airborne remote sensing devices have been developed to face various remote sensing tasks. These devices include digital aerial cameras, lidar, digital cameras, imaging spectrometers, infrared sensors and miniSAR (unmanned airborne microminiature synthetic-aperture radar). Ground remote sensing systems have two states: mobile and static. A mobile measurement system executes rapid movement measurement by means of vehicles (e.g., cars and boats) and consists of sensors such as charge-coupled device (CCD) cameras, cameras, laser scanners, GPS and inertial navigation systems (INSs) (Li et al., 2015). These can acquire the geospatial position of the target while collecting realistic images of the features. Static state measurement refers to the installation of sensors in a fixed place and includes laser scanners, cameras, ground-based SAR and surveying robots. These can form a ground sensor web through computer network communication and geographic information service technology.

In the face of geohazard emergency responses, space–air–ground remote sensors establish associations through collaborative planning to form a collaborative observation service.

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Collaborative remote sensing observation service system for geohazard emergency response.

The system based on the process of "observation–transmission–processing–distribution", as shown in Fig. 1. In the event of a geological disaster, the emergency command center responds quickly, planning observation missions according to observation needs and the current technical environment (1, 2). After remote sensing systems carry out observation missions (3), the data are received, processed and distributed through the data center, providing emergency services mainly based on geographic information (4, 5, 6).

The geographic information services provided by the remote sensing emergency service system are shown in Fig. 2. These services include data processing, data products, data services, model services, functional services and warning services. Data processing refers to the process and method of obtaining effective emergency information from the collected data and includes the data processing method, feature extraction, image classification and image analysis. Data products refer to the quality and current potential of various types of remote sensing products. Data services provide disaster-related basic data, thematic data and analysis data through the web map service (WMS), web feature service (WFS), web coverage service (WCS) and web map tile service (WMTS). Functional services provide quantitative, qualitative, characterization and visualization of geospatial phenomena through spatial analysis services, terrain analysis services and visualization services. Model services provide various models for calculation, analysis, anomaly identification, damage assessment, situational assessment, evaluation, decision-making and optimization. Warning services provide early warnings of disasters with regard to space, time and situation.

### 2.2 Space–air–ground remote sensing index database

The existing database focuses on satellite remote sensing resources and does not form a unified management for aerial, UAV, ground remote sensing platforms or their sensor infor

![img-1.jpeg](img-1.jpeg)

Figure 2. Emergency geographic information service.
mation when facing the demand of remote sensing cooperative response in actual disaster emergencies. This paper establishes an integrated space-air-ground remote sensing index database covering satellite, aerial and ground platforms that adopts MySQL (Structured Query Language) for storage management. MySQL is an open-source relational database management system that supports multiple storage engines such as MyISAM (Indexed Sequential Access Method) and InnoDB. It also supports spatial data objects in terms of geographic information by complying with the OpenGIS (geographic information system) Geometry Model of the Open Geospatial Consortium (OGC), provides various application programming interfaces (APIs), and supports multiple operating systems and development languages. Thus, MySQL can provide good web service applications. The database is divided into two parts: SAT_RS, the sensor technical performance index database, and SE_RS, the emergency service evaluation index database.

The technical performance indicators of sensors in SAT_RS are their various capability characteristics under normal operation as reflected by technical parameters. The indicators are independent between different types of sensors. The parameters vary, and the technical indicators are also diverse. In the face of complex geohazard emergency response needs, how to select the appropriate sensors to accomplish the observation tasks requires the classification of existing sensors according to their capabilities and a synthesis of technical indicators. In this regard, this study collected and summarized the technical parameters of various types
of sensors, referred to the selection of indicators in satellite online data repositories (NSSDC, 2020; CEOS, 2020; OSCAR, 2020) and the experience of relevant professionals in using them, analyzed the information of various types of sensors, and established a more complete sensor technology index system. This is shown in Table 1 below.

The indicators in the table are mainly considered in terms of the amount of information, timeliness, validity (accuracy) and expressiveness of data acquisition. The indicators are selected for different types of sensor technical indicators. The amount of information is used to eliminate the uncertainty in the expression of spatiotemporal characteristic information in the observed data, including the temporal extent, the spatial area, and the degree of spatial details such as geometry and attributes, reflecting the intensity of the acquired information, and is related to the breadth and depth of the sensor's role with regard to the scan width, side-swing capability, measurement range, etc. Timeliness refers to the selfconscious dynamism of the sensor system and the degree of sensitivity and response to the task and is related to the responsiveness and execution efficiency of the sensor. Factors include the revisit cycle of the satellite, preparation time of the UAV and endurance. Validity expresses the accuracy of the acquired information with regard to resolution, quantization level and measurement accuracy, for example. Expressiveness describes the representational form of the information. Note that the same indicator has multiple effects on data acquisition, such as the spatial resolution of the satellite having an impact on both the amount and validity of informa-

Table 1. Sensor technical indexes.


tion. Thus, it is necessary to set a comprehensive evaluation indicator of information acquisition capability in different dimensions.

The emergency service indexes in SE_RS refer to the capacity evaluation indexes of the emergency service system associated with the event. The space-air-ground remote sensing geohazard emergency service capacity evaluation index system established is shown in Table 2 below. The index is measured in the three aspects of data acquisition, processing and information service. The specific content of the indexes should be determined in conjunction with the responding emergency event.

The database design process is divided into information analysis, structure design, storage settings and data storage. By analyzing the massive sensor information, we set the attribute fields from the carrying platform, set the technical characteristics of each type of sensor and operation status, store the corresponding data in the database and establish unified management, and finally design 20 kinds of tables. This is shown in Fig. 3. SAT_RS records the basic satellite, aerial and terrestrial information through three tables: RS_Satellite, Sensor_Aerial and RS_Terrestrial. Then, SAT_RS establishes a technical characteristics index table for different types of sensors on different platforms according to the technical index system shown in Ta-
ble 1. This includes SatelliteSensor_Optical, SatelliteSensor_SAR, UAS, ImageSpectrometer, DigitalCamera, AirborneLidar, MiniSAR, MMS (Mobile Mapping System) and 11 other types of tables. The RS_Task table in SE_RS links tasks among sensors and records the observation tasks they perform, including observation equipment and observation time. The evaluation indexes in RS_DataProcessing and RS_Service are set according to the guidelines of Table 2 and the specific geohazard remote sensing emergency service events.

At present, the SAT_RS database records approximately 150 satellites and their corresponding sensor data from many countries and organizations including the United States, France, ESA, Russia, Japan, South Korea, India and China; more than 100 commonly used aerial remote sensor product families; more than 50 UAV products; and dozens of ground mobile measurement systems. A partial display is shown in Fig. 4. The features of SAT_RS are as follows: (1) wide data coverage, support for satellites, aviation platforms (including UAVs), terrestrial multiplatforms and multiple types of remote sensors; (2) indexing of sensor technical performance and support for evaluation calculations; and (3) data support for sensor machine learning (ML) descriptions.

## 3 Methodology

The methods commonly used to evaluate the system capabilities are the analytic hierarchy process (AHP) (Emrouznejad and Marra, 2017), fuzzy integrated assessment (Kahraman et al., 2015), technique for order preference by similarity to an ideal solution (TOPSIS) (Zhang and Xu, 2015), rank sum ratio (RSR) (Tian, 2002) and Bayesian network (BN) (Heckerman, 2008), all of which have their own characteristics. The evaluation studied in this paper is a complex and flexible multisystem and multi-influencing factor problem. In order to improve the scientific nature of the evaluation and make full use of the advantages of various methods, TOPSIS and Bayesian-network-based evaluation methods are used for remote sensing collaborative observation and service capability, respectively, while RSR is used to determine the weights in TOPSIS calculation. The evaluation process is shown in Fig. 5.

TOPSIS can eliminate the influence of different indicator magnitudes and make full use of the information of the original data. This is a common method for multiobjective decision analysis of limited solutions in systems engineering. Since this method has no strict restrictions on the distribution, quantity and magnitudes of evaluation data, it is flexible in application and can be well adapted to the changes of indicators involving many types of sensors. Meanwhile, the use of RSR to determine the weights combines the score ratio (SR) and empirical weights. This overcomes to some extent the subjectivity of determining the weights and makes the evaluation results more reflective of objective facts.

Table 2. Indexes for evaluation of emergency service capacity.


![img-2.jpeg](img-2.jpeg)

Figure 3. Unified Modeling Language (UML) of database. FPS: frames per second. IFOV: instantaneous field of view. POS: position and orientation system.

A Bayesian network is a probabilistic graphical model based on the dependency relationships among variables, and the evaluation of emergency response service capability using this method has the following advantages. Firstly, the emergency response process can be divided into a number of coherent and causally related links such as data acquisition, processing, information extraction and forming an emergency service chain. The evaluation of this service capability with backward and forward correlation is suitable for modeling with directed graphs. Secondly, there are uncertainties in each link of emergency services that are suitable for probabilistic methods.

### 3.1 TOPSIS

TOPSIS is commonly used in multiple-criteria decisionmaking (MCDM). The basic principle is to rank the evaluated objects by detecting the distance between the positive ideal solution (PIS) and the negative ideal solution (NIS). The evaluation object is best if it is closest to the PIS and farthest away from the NIS, where the PIS is composed of the best value of any alternative under the corresponding evaluation index. The NIS has the opposite logic. The evaluation process is as follows.

## 1. Identify a decision matrix.

Assuming that the evaluation object in an MCDM is composed of $m$ combinations of remote sensing cooperative work, $n$ evaluation indicators and the value of

![img-3.jpeg](img-3.jpeg)

Figure 4. SAT_RS database (partial). CNES: Centre national d'études spatiales. CNSA: China National Space Administration. CRESDA: China Center for Resources Satellite Data and Application. INPE: Instituto Nacional de Pesquisas Espaciais. ISRO: Indian Space Research Organisation. USGS: United States Geological Survey.
![img-4.jpeg](img-4.jpeg)

Figure 5. Evaluation process.
the $j$ th evaluation indicator for the $i$ th object is $a_{i j}(1 \leq$ $i \leq m, 1 \leq j \leq n$ ), the decision matrix $\mathbf{A}=\left(a_{i j}\right)_{m \times n}$ is as follows:

$$
\mathbf{A}=\left[\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & \ddots & \vdots \\
a_{m 1} & \cdots & a_{m n}
\end{array}\right]
$$

2. Convert negative indicators.

To maintain the same direction of change for all indicators, a reciprocal method was used to convert negative indicators into positive indicators. The negative indicators refer to indicators with smaller values for better re-
sults, such as spatial resolution, revisit cycle and UAV preparation time, and vice versa for positive indicators, such as swath width and payload.
3. Normalize the decision matrix.

The evaluation indicators have different attribute dimensions, and it is necessary to transform various attribute dimensions of the indicators into nondimensional attributes. The normalization decision matrix is

$\mathbf{B}=\left(b_{i j}\right)_{m \times n}$, and the normalized value is computed as

$$
b_{i j}=\frac{a_{i j}}{\sqrt{\sum_{i=1}^{m} a_{i j}^{2}}}
$$

4. Determine weights using RSR.

RSR is a statistical analysis method that combines the advantages of classical parametric estimation and modern nonparametric estimation. RSR refers to the average or weighted average of the rank totals of rows (or columns) in a table and is based on the concept of converting indicator values into dimensionless statistical ranks and ratios by using statistical distribution, probability theory and regression analysis methods to evaluate and classify programs.
For matrix $\mathbf{B}$ obtained after the normalization process, the RSR is calculated as
$\mathrm{RSR}_{j}=\frac{\sum_{i=1}^{m} R_{i j}}{m \cdot n}(1 \leq i \leq m, 1 \leq j \leq n)$.
$R_{i j}$ denotes the rank corresponding to the index value $b_{i j}$ of the $j$ th evaluation index in the $i$ th evaluation object, and the formula for determining the weight of each index using RSR is as follows:
$W_{j}=\frac{\mathrm{SR}_{j} \cdot W^{\prime} j}{\sum_{j=1}^{n} \mathrm{SR}_{j} \cdot W_{j}^{\prime}}$.

The SR reflects the proportional relationship between the levels of each indicator and is calculated from RSR (Eq. 5). $W^{\prime}$ is an empirical weighting factor.
$\mathrm{SR}_{j}=\frac{\mathrm{RSR}_{j}}{\sum_{j=1}^{n} \mathrm{RSR}_{j}}$
5. Calculate the weighted normalized decision matrix.

Multiplying the normalized processed matrix by the determined weight vector $\boldsymbol{W}=\left[w_{1} \cdots w_{n}\right]^{T}$ results in a weighted normalized decision matrix $\mathbf{C}=\left(c_{i j}\right)_{m \times n}$ :
$c_{i j}=b_{i j} \cdot w_{j}$.
6. Compute the PIS and NIS.

The positive ideal solution is
$c_{j}^{+}=\max c_{i j}$,
and the negative ideal solution is
$c_{j}^{-}=\min c_{i j}$,
where the PIS represents the indicator value of the most desirable synergistic solution inferred from $m$ combinations of approaches and vice versa for the NIS.
7. Compute distance of each alternative from the PIS and NIS.

Distance from the PIS is
$d_{j}^{+}=\sqrt{\sum_{i=1}^{m}\left(c_{i j}-c_{j}^{+}\right)^{2}}$,
and distance from the NIS is
$d_{j}^{-}=\sqrt{\sum_{i=1}^{m}\left(c_{i j}-c_{j}^{-}\right)^{2}}$.
8. Compute relative closeness and ranking of alternatives.

The relative closeness is defined as
$s_{i}=\frac{d_{j}^{-}}{d_{j}^{+}+d_{j}^{-}}$,
where the larger the $s_{i}$ value is, the higher the ranking and the more desirable the remote sensing cooperative method are.

### 3.2 Bayesian network

The Bayesian network is a probabilistic graph model that was first proposed by Judea Pearl in 1985. The Bayesian network applies probability theory to the reasoning of uncertainty problems, and its network topology is a directed acyclic graph (DAG) with the ability to express and reason about uncertainty knowledge.

The nodes of a Bayesian network represent random variables, and the directed links (edges) between the nodes indicate the conditional dependencies between the random variables. All nodes pointing to node $M$ are called the parent nodes of $M ; M$ is called the child node of its parent; and variables without a parent node are called root node variables. All nodes have a corresponding node probability table (NPT) expressing the probability of occurrence of a random event, with the probability of the root node being the prior probability and the probability of the child node indicating all possible conditional probabilities of that node relative to its parent node (posterior probability).

Figure 5 illustrates a simple Bayesian network where $A, B$, $C$ and $D$ are four variables; parent node $A$ is the root node; $B$ and $C$ are child nodes of $A$; and $D$ depends on variables

![img-5.jpeg](img-5.jpeg)

Figure 6. Diagrammatic depiction of Bayesian model.
$B$ and $C$. The joint probability distribution of the nodes is expressed as follows:
$P(A, B, C, D)=P(A) P(B \mid A) P(C \mid A) P(D \mid B, C)$.
Probabilistic reasoning is one of the main uses of a Bayesian network. The reasoning essentially involves calculating a posteriori probabilities using conditional independence among random variables to calculate the a posteriori probability distribution of some other variables if the values of some variables in a Bayesian network are known.

## 4 Results and discussion

By managing indicators through the database, evaluation of the collaborative capability of space-air-ground remote sensing technology in geohazard emergency response is established and divided into two parts: collaborative observation efficiency and emergency service capability. The synoptic observation efficiency refers to the overall working capability presented by the coordination among observation systems, which needs to take into consideration the inherent technical performance of heterogeneous sensors of dynamic scheduling and the degree of accomplishment of specific observation tasks by the synergy among platforms. The evaluation of emergency service capability refers to the dynamic performance of remote sensing service systems in performing specific tasks, which is related to the application requirements of disaster emergency response.

### 4.1 Evaluation of effectiveness of coordinated space-air-ground remote sensing observations

A collaborative observation effectiveness assessment is a quantitative expression of the level of observation that remote sensing technology has in performing a particular task. This is closely related to the inherent properties of remote sensing technology and the type of task.

## Simulation calculations of coordination observation

The collaborative observation system consists of multiple distributed remote sensor resource systems, and its technology enhances the observation capability in three aspects: data
volume, accuracy and timeliness. The specific collaborative mode is often determined according to the characteristics of remote sensing technology and the emergency needs of geological disasters. Taking the emergency observation of a mudslide disaster as an example, the following two demands should be met: (1) to quickly determine the scope of the disaster and (2) to quickly conduct disaster assessment and carry out a rescue response. By combining the advantage of a wide observation range of satellite images and the ability of aerial remote sensing to deploy in real time, fly under the clouds, be highly mobile and obtain data quickly, a typical synergistic satellite-aerial approach is formed. This includes quickly acquiring pre-disaster high-resolution remote sensing images, accessing geological information of the disaster area, initially determining the scope of the disaster and completing pre-disaster research and judgment. The high-resolution remote sensing images and aerial survey data after the disaster are coordinated for remote sensing interpretation by determining the base map for disaster assessment and providing decision support for a rescue.

Based on the above analysis set, the following remote sensing synergistic approach was formed through planning services, after a mudslide disaster occurred in a certain place: (A) GF-2 (Gaofen) satellite and the KC2600 UAV with a Sony NEX-7 camera, (B) Pléiades satellite and the EWZD6 UAV with a Nikon D800 camera, and (C) IKONOS and Z/I DMC aerial cameras. Their synergy effectiveness was calculated as follows.

## 1. Identify evaluation indicators.

Through the synergy of high-resolution satellites and aerial remote sensing, the emergency response time can be effectively shortened; the timeliness of data acquisition at disaster sites can be improved; and effectiveness indicators can be established, as shown in Table 3.

## 2. Process the data.

Table 3 contains two types of indicators: quantitative and qualitative. Quantitative indicators such as resolution can be obtained directly from the technical parameters of the satellite, while flight-related time and area coverage are obtained according to the technology of different products combined with operational experience. Data processing is a qualitative indicator for which we use 1 to represent having preprocessing capability and 2 for the opposite situation. The data of the sensor-type indicators involved in the collaborative observation scheme are extracted. A decision matrix $\mathbf{A}$ is created, trended and normalized to obtain matrix $\mathbf{B}$.

Table 3. Effectiveness indicators.


Table 4. Indicator rank and RSR.


Table 5. Weighting of indicators.


$$
\begin{aligned}
& \mathbf{A}=\left[\begin{array}{cccc}
1 & 90 & 1.8 & 0.82 & 2 \\
0.5 & 45 & 0.65 & 0.73 & 2 \\
1 & 150 & 3.4 & 0.94 & 1
\end{array}\right] \\
& \mathbf{B}=\left[\begin{array}{cccc}
0.41 & 0.43 & 0.46 & 0.57 & 0.41 \\
0.82 & 0.86 & 0.17 & 0.51 & 0.41 \\
0.41 & 0.26 & 0.87 & 0.65 & 0.82
\end{array}\right]
\end{aligned}
$$

3. Use RSR to determine the weights.

Table 4 lists the rank and RSR of the indicator values for each scenario, and Table 5 lists the final weights determined.
4. Calculate the weighted matrix $\mathbf{C}$ to obtain the PIS and NIS.

$$
\begin{aligned}
& \mathbf{C}=\left[\begin{array}{cccc}
0.08 & 0.07 & 0.09 & 0.15 & 0.07 \\
0.16 & 0.14 & 0.03 & 0.13 & 0.07 \\
0.08 & 0.04 & 0.18 & 0.17 & 0.13
\end{array}\right] \\
& \mathbf{C}^{+}=\left[\begin{array}{cccc}
0.16 & 0.14 & 0.18 & 0.17 & 0.15
\end{array}\right] \\
& \mathbf{C}^{-}=\left[\begin{array}{llll}
0.08 & 0.04 & 0.03 & 0.13 & 0.07
\end{array}\right]
\end{aligned}
$$

5. Calculate the distance.

$$
\begin{aligned}
& D^{+}=\left[\begin{array}{llll}
0.16 & 0.16 & 0.13
\end{array}\right] \\
& D^{-}=\left[\begin{array}{llll}
0.07 & 0.13 & 0.16
\end{array}\right]
\end{aligned}
$$

6. Calculate the composite valuation.

$$
S=\left[\begin{array}{llll}
0.30 & 0.43 & 0.57
\end{array}\right]
$$

According to the evaluation results, the preferential order of the planning scheme is $\mathrm{C}, \mathrm{B}$ and A ; that is, the IKONOS and DMC aerial cameras have the strongest synergistic effect; the Pléiades satellite and EWZ-D6 UAV equipped with the Nikon D800 camera is placed second; and the GF-2 satellite and the KC2600 UAV equipped with the Sony NEX-7 camera have the weakest synergistic effect among these three approaches.

In this result, we analyze the main reason why among the three, although the UAV flight preparation time of approach C is longer, its operation time and coverage area are more advantageous, and these two indicators occupy a relatively large weight, respectively 0.2 and 0.26 . It also has the ability to process data, which results in an even higher final score. Continuing to compare the two approaches A and B, on the basis of the same data processing capability, although the A approach has longer operation time and larger coverage area, B has good enough indicator values in the remaining two indicators (satellite resolution and flight preparation time) to make its final calculation result 0.43 , which is higher than A's 0.3 . This can show that the reasonableness of the setting of the weights has a very important position in influencing the accuracy of the results, and at the same time, it can make up for the deficiencies in other aspects when some indicators have outstanding advantages.

### 4.2 Evaluation of the capacity of geohazard emergency response services

Emergency response to geohazards is a type of disaster management that requires the coordination of multiple technologies for rescue and disaster relief. The top priority is to ensure personnel safety and save lives and in this way to avoid or reduce property losses to the greatest extent. In rescue work, there is a "golden 72 h " during which the survival rate

of the victims is extremely high. This is the critical rescue period after the occurrence of geological disasters. Remote sensing technology, as the main technical support for emergency response, should provide effective service for rescue in time and achieve fast investigation, fast characterization, fast decision-making and fast implementation of emergency work through cooperation. To evaluate the service capability of remote sensing collaborative systems in geohazard emergency responses, this section takes earthquake emergencies as an example, analyzes the demand to establish emergency response service chains and creates a Bayesian network design evaluation model.

### 4.2.1 Earthquake emergency response service chain

Earthquakes are a sudden movement of Earth's surface caused by the release of slowly accumulating energy inside Earth that can cause substantial damage to life and property and further aggravate the impact of disasters and losses by triggering secondary disasters such as landslides, debris flows and barrier lakes. This paper refers to the process of remote sensing technology service in the Wenchuan earthquake emergency (Pan and Tang, 2010; Zhang et al., 2009), analyzes it from the aspects of spatial information demand for rapid response and information technology support for disaster relief and rescue, and combines multiple remote sensing information services to form an earthquake remote sensing emergency service chain, as shown in Fig. 7. The need for emergency response to earthquakes is mainly reflected in the rapid acquisition of high-resolution remote sensing images, rapid processing of remote sensing data and extraction of hazard information. The golden 72 h time period after an earthquake is a critical period for rescue, and highresolution remote sensing images need to be quickly acquired and updated to analyze casualties, infrastructure damage, rescue and resettlement, and other detailed information. The processing of remote sensing data in disaster relief needs to achieve real-time or near-real-time efficiency, including rapid image correction, alignment, stitching and uniform color. Disaster information is divided into three parts: building damage, lifeline damage and secondary disaster monitoring. Buildings reflect the main distribution of affected people. Roads are the lifeline of earthquake relief, and change analysis and feature extraction are the mainstay. These are combined with basic data and mathematical methods to analyze and calculate the scope of disaster impact and damage to buildings and roads and to make rapid assessments. Secondary disasters derived from earthquakes such as landslides, debris flows and barrier lakes are monitored dynamically by remote sensing technology and simulated to forecast their development and impact.

### 4.2.2 Bayesian network model for emergency service evaluation

The Bayesian network is a probabilistic graph model based on dependencies between variables, and its expected value is reliable when the causal chain is correct and has an appropriate probability distribution. The seismic emergency response service chain is a coherent link before and after, suitable for modeling by using a directed graph. The links are flexible; there is uncertainty; and the chain is suitable for handling with probability. Based on the theory established by the Bayesian network, the Bayesian network model design for the evaluation of the earthquake disaster emergency response service capability was carried out using the GeNIe Academic version 2.3 software.

## 1. Identify evaluation indicators.

The system of indicators for evaluating the establishment of capacities according to the earthquake emergency response service chain is shown in Table 6.

## 2. Design the Bayesian network structure.

From the above evaluation system, the emergency response service capability is divided into three levels (data acquisition, fast data processing and disaster information extraction), and each level indicator is the parent node of the corresponding indicator of the previous level. This convergence relationship is represented by the directed edge from the parent node to the child node, i.e., from the lower-level indicators to the corresponding upper-level indicators that finally converge to the total indicators. Through the above analysis, the Bayesian network topology of the cooperative-observation system earthquake emergency response service capability assessment model is constructed, as shown in Fig. 7.

## 3. Construct the Bayesian network model.

Each node in the Bayesian network model has a finite number of mutually exclusive states, where the root node is classified into three levels. The conditional probability of each node is determined according to expert experience to build the assessment model of the seismic emergency response service capability of the cooperative-observation system, as shown in Fig. 8.

## 4. Assess the capacity.

The capability of the cooperative observing system can be predicted by Bayesian inversion if the values of some nodes in the evaluation model are known. In setting the root node, the response time, observation range, correction accuracy, spatial analysis and forecast accuracy of the state are known (response time $=$ good, observation range $=$ normal, correction accuracy $=$ good, spatial analysis $=$ normal, and forecast accuracy $=$ normal $)$.

![img-6.jpeg](img-6.jpeg)

Figure 7. Earthquake remote sensing emergency response service chain.

These are used as evidence variables to predict the capacity of the collaborative observation system, as shown in Fig. 9. Combined with Fig. 8, after identifying the evidence variables, the probability of emergency response capacity being good increased from $54 \%$ to $60 \%$, and the probabilities of the three first-level indexes were concentrated in good, good and normal. The probability of data acquisition ability being good increased from the previous $52 \%$ to $59 \%$, and the probability of fast data processing ability being good increased from $53 \%$ to $68 \%$; however, the probability of the hazard information extraction ability being good decreased from $49 \%$ to $41 \%$, and the probability of being normal increased
from $37 \%$ to $45 \%$. In this regard, it can be tentatively judged that the effectiveness of disaster emergency services can be further improved by improving the disaster information extraction link.

### 4.3 Discussion

This paper proposes a method for evaluating the synoptic observation effectiveness and emergency service capability of remote sensing using TOPSIS and Bayesian networks. The feasibility of the method is demonstrated by means of simulations in this chapter, but there are several situations that need to be addressed here.

Table 6. Evaluation system for emergency response service capacity.


![img-7.jpeg](img-7.jpeg)

Figure 8. Bayesian network topology of service capacity evaluation mode.

![img-8.jpeg](img-8.jpeg)

Figure 9. Assessment model for capacity of collaborative observation system earthquake emergency response service.

1. Determination of co-observation effectiveness indicators.

The evaluation indexes are influenced by the performance of the sensors themselves and the cooperative mode. The index values related to the technical parameters of remote sensing can be obtained directly from the database. These values include the spatial resolution of the satellite, revisit period, scan width, camera pixels and range of the laser scanner. Some index values need to be calculated in conjunction with the actual situation, including the flight height of the UAV and the flight coverage area.
2. Determination of indicator weights in effectiveness evaluation.

From the analysis of the results of the simulation experiments, it can be concluded that the index weights directly affect the results of the evaluation, and the setting of the weights reflects which aspect of the requirements the researcher cares more about, which will often be associated with the actual problem.
3. Determination of rank division, probabilities and conditional probabilities of Bayesian network nodes.

In the above calculation, the rank division, probability and conditional probability of each root node are the results of simulation statistics based on expert experience and can only be used to show that the evaluation network has computational feasibility and reference. In practical applications, these are difficult links to determine, and their accuracy directly affects the effectiveness of the Bayesian network's work (Pourret et al., 2008). The process of determination relies on a large amount of raw data as a reference for statistical analysis and requires a final value based on the actual application and combined with the opinions of different experts. This needs to be further studied in our work.

## 4. Uniqueness of the Bayesian model design.

The structure and node-level design of the Bayesian evaluation model are related to the demand for the application of the evaluation results, and the evaluation intention of the designer is indicated. In the above example, we considered the entire disaster response chain, which involved the effect of multiple aspects of data acquisition, processing and information extraction on disaster response. If one wants to examine the capability of only one aspect of the emergency response, then the model can be designed separately. In addition, the complexity

![img-9.jpeg](img-9.jpeg)

Figure 10. Capacity projection of collaborative emergency services.

of actual disaster emergency response service links (and there are multiple design options for the same problem) needs to be adjusted in the work according to the specific application and the needs of decision makers.

5. *Dependence on the evaluation results.*

In the above study, due to the lack of real experimental scenario data, the study of disaster problems is only a generalized and simple calculation of geohazard simulation with a reference to real events. The results show that the evaluation can reflect the problems existing in the application of remote sensing technology. This is a reference for the planning of remote sensing cooperative observations in geohazard emergency work. However, an actual disaster emergency is a complex process, and the application of the method still needs to be revised in conjunction with a real situation.

## 5 Conclusions

This paper established a database of sensor technology and service indexes covering satellites, aviation and the ground; realized the unified management of multiplatform and multi-type heterogeneous sensor resources; and proposed a method to evaluate its application capability in geological disaster emergency response. This was accomplished by using TOPSIS and Bayesian networks in two aspects of collaborative observation effectiveness and emergency service capability, respectively. Thus, the proposed method provides a decision basis for the establishment of air–space remote sensing collaborative services in geological disaster emergency response.

Future work will include (1) further enriching the database content and developing web service functions to realize the dynamic connection between data and evaluation calculation and (2) integrating more practical application scenarios and revising the evaluation calculation model.

**Figure 10.** Capacity projection of collaborative emergency services.

# Appendix A 

Table A1. Global satellite launch situation. ADEOS: Advanced Earth Observing Satellite. ALOS: Advanced Land Observing Satellite. BJ: Beijing. BNU: Jingshi. CBERS: China-Brazil Earth Resources. COMS: Communication, Ocean and Meteorological Satellite. COSMOSkyMed: COnstellation of small Satellites for the Mediterranean basin Observation. Envisat: Environmental Satellite. EO: Earth Observing. EOS: Earth Observing System. EROS: Earth Resources Observation Satellite. ERS: European Remote Sensing. FY: Fengyun. GF: Gaofen. GMS: Geostationary Meteorological Satellite. HJ: Huanjing. HY: HaiYang. IRS: Indian Remote Sensing. JERS: Japanese Earth Resources Satellite. JL: Jilin. KOMPSAT: Korean Multi-purpose Satellite. LAPAN-Tubsat: National Institute of Aeronautics and Space-Technical University of Berlin. LJ: Luojia. OVS: Orbita Video Satellite. SPOT: Satellite Pour l'Observation de la Terre. TH: Tianhui. THEOS: Thaichote. TT: Tiantuo. ZY: Ziyuan.


Code availability. Due to the requirements of the project, we are unable to provide the code related to the database and evaluation.

Data availability. Due to the requirements of the project, we are unable to provide the data related to the database and evaluation.

Author contributions. YL and JZ designed the study. YL performed the data collection, analysis and database establishment. YL completed the design, calculations and validation of the methods and models. YL wrote the manuscript and led the revision with contributions from JZ. JZ managed the project schedule and budget.

Competing interests. The contact author has declared that neither they nor their co-author has any competing interests.

Disclaimer. Publisher's note: Copernicus Publications remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Special issue statement. This article is part of the special issue "Remote sensing and Earth observation data in natural hazard and risk studies". It is not associated with a conference.

Acknowledgements. This work was supported by the National Key Research and Development Program (grant no. 2018YFB0505402) and funded by the Natural Science Foundation of China (grant no. 42171424). We address a special thanks to the editors and reviewers for their constructive comments on earlier versions of the paper.

Financial support. This research has been supported by the National Key Research and Development Program (grant no. 2018YFB0505402) and funded by the Natural Science Foundation of China (grant no. 42171424).

Review statement. This paper was edited by Michelle Parks and reviewed by Christian Bignami and two anonymous referees.
