# An intelligent healthcare system for predicting and preventing dengue virus infection 

Sandeep Kumar Sood ${ }^{1} \cdot$ Vaishali Sood ${ }^{2} \cdot$ Isha Mahajan ${ }^{2} \cdot$ Sahil $^{3}$


#### Abstract

Received: 5 June 2020 / Accepted: 19 November 2020 / Published online: 8 January 2021 (c) The Author(s), under exclusive licence to Springer-Verlag GmbH, AT part of Springer Nature 2021


#### Abstract

Dengue is a mosquito-borne pandemic viral infection, which transmits to humans from Female Aedes albopictis or Aedes agypti mosquitoes. It progressively deteriorates the health of infected individuals and poses a high threat of human morbidity and mortality. This paper proposes an intelligent healthcare system which identifies, monitors, and alerts dengue virus ( DeV ) infected individuals and other stakeholders in real-time and control the DeV infection outbreak using cloud computing, internet of things and fog computing paradigms. The proposed system uses Naive Bayesian Network (NBN) for diagnosing the possibly DeV infected individuals and generating real-time alerts for suggesting and alerting the concerned stakeholders for taking on-time necessary actions at the fog subsystem. The proposed system also uses Social Network Analysis at the cloud subsystem, to provide Global Positioning Systems (GPS)-based global risk assessment of the DeV infection on Google Maps (Google-based web map service) and control DeV infection outbreak. The analysis of the experimental results acknowledges the efficiency of the NBN-based DeV infection diagnosis, alert generation, and GPSbased risk assessment functionality, of the proposed system, via various statistical measures and experimental approaches.


Keywords Dengue virus $\cdot$ Cloud computing $\cdot$ Fog computing $\cdot$ Internet of things (IoT) $\cdot$ Naive Bayesian network (NBN) $\cdot$ Global positioning system (GPS) $\cdot$ Social network analysis (SNA)

Mathematics Subject Classification 68T99

[^0]
[^0]:    $\boxtimes$ Sahil
    sahil.neelam@hotmail.com
    1 Department of Computer Science and Informatics, Central University of Himachal Pradesh, Dharamsahala, HP, India
    2 Department of Computer Science and Engineering, Guru Nanak Dev University Regional Campus, Gurdaspur, PB, India
    3 School of Computing, Indian Institute of Information Technology, Una, HP, India

# 1 Introduction 

Dengue fever is considered as one of the world's most common vector-borne diseases. It is caused by the transmission of the Dengue Virus (DeV) into human beings, from the infected mosquitoes through mosquito bites. Female Aedes agypti or Aedes albopictis mosquitoes are the primary sources of DeV transmission into humans. When the mosquito bites a person having DeV in his/her blood, the mosquito becomes infected with the DeV. An infected mosquito can later transmit that infection to healthy people by biting them. An infected person can transmit the DeV from 4 to 10 days via female Aedes agypti mosquito after the symptoms appear. The DeV incidence can cause human morbidity and mortality in case the due attention is not paid. The DeV infection affects the tropical and subtropical areas, especially in developing and underdeveloped countries, where poor water management, substandard housing, inadequate waste management, poor vector control, and deteriorating disease prevention programs become its main drivers [6]. The symptoms of DeV infection are severe fever, headache, eye pain, rashes on the body, bleeding in nose or gums, and loss of appetite [47]. Sometimes, the DeV infection can lead to more severe conditions like hemorrhagic fever, dengue shock syndrome, and various permanent health losses.

According to the World Health Organization [52], approximate 2.5 thousand million people or $40 \%$ population of the world is living in the areas, where the DeV transmission risk is high. The report states that the incidence of DeV infection has increased by 30 times over the last half of the century. An estimation states that more than 50 million DeV infection occurs worldwide in a year, of which $1 \%$ severe dengue cases are hospitalized, and $2.5 \%$ of the hospitalized people die. Another report [53] states that only 96 million out of 390 million dengue infection cases are being clinically manifested per year. Further, the report states that the 3.9 thousand million people belonging to 128 countries are at a high risk of DeV infection. Henceforth, its real-time diagnosis and control are emerging as one of the most critical issues for healthcare agencies, especially in developing and underdeveloped countries.

### 1.1 Contribution

The diagnosis of DeV infection, provision of curative aids to infected individuals, and preventive aids to the uninfected individuals at the nascent stage of the infection can reduce the health severity consequences and prevent the outbreak of DeV infection. However, the existing healthcare systems are not so efficient in controlling such types of infectious diseases. These systems are having various limitations like the readily unavailable diagnostic procedures, people's ignorance in treating every fever as a simple fever and even their reluctance in providing their vital health information, their traditional methods to treat diseases, and various environmental conditions. Even the reluctance and unawareness of patients to visit hospitals for routine checkups and doctors' inability to monitor each patient regularly by visiting them, especially in those places where doctor to patients ratio is very low, are some significant challenges for the existing healthcare systems. Hence, to control the DeV infection outbreak, its real-time

and remote detection, and monitoring can play an important role in healthcare-related services.

The immense potential and advancement of Information and Communication Technologies (ICT) and their diffusion in various domains have enabled the communities to build sustainable solutions for improving their lives [34]. The ICT paradigms viz. cloud computing, Internet of Things (IoT), and fog computing have revolutionized the world in recent times, with the development of smart solutions in various fields $[8,17,27]$ and healthcare [3] is one such field. These paradigms have equipped the healthcare sector with the features of On-time Remote Diagnostics, Tele-Medicine, Remote Healthcare Monitoring, Timely Health Awareness and alike, and evolved the legacy healthcare systems into intelligent and responsive system.

The Cloud-assisted IoT-based healthcare systems have made it feasible to remotely diagnose and monitor the health attributes of the individuals and provide appropriate treatment. The effectiveness of healthcare services require real-time health diagnostics and alert generation to the concerned stakeholders: individuals, hospitals and doctors. However, in the Cloud-IoT environment, the scale of data generated by IoT-sensors present the challenges viz. the latency due to the communication overhead and transmission delay, real-time data processing, and privacy of the sensitive health data of the patients. Here, the concept of fog computing resolves the issues like location awareness, high latency, and reliability by providing computing, communication and storage resources at the edge devices of the network. It enables the individuals to use computing services for processing the data in their mobile devices, and the transmission of only required data that too in a protected manner to the cloud servers. Fog computing provides various merits to the healthcare systems, such as quality of service, low latency, location awareness, and real-time notification of services [35].

These significant benefits can assist in real-time identification of the DeV infected individuals, on-time alert generation to the concerned stakeholders and assessing the DeV infection geographical risk. Hence, the challenges of early and remote detection of DeV infection, controlling of its outbreak, and the motivation of ICT diffusion in the healthcare systems have derived us to propose a Fog-Cloud-IoT based intelligent healthcare system for controlling DeV infection outbreak.

In this paper, a Fog-Cloud-IoT based healthcare system is proposed, which analyzes individuals' health attributes and the surrounding environment for diagnosing the possible DeV infected individuals, monitoring their health, and controlling the outbreak of DeV infection. The system acquires the individuals' personal and health-related attributes via a mobile application on their phones, and environment-related attributes through environmental sensors, at the data acquisition subsystem. The system keeps the personal information of the individuals private using a two-stage mechanism: information granulation and secret sharing scheme. On the Fog subsystem, the system uses Naive Bayesian Network (NBN) for diagnosing the individuals for possible DeV infection, which classifies them into the category of possibly infected (In) or uninfected (Un), using their health attributes. Once the individuals are diagnosed with possible DeV infection, the fog subsystem immediately generates alerts and aware individuals about the disease and suggest them for medical examination (if require) to medically confirm the incidence of the infection by consulting with doctors and through proper recommended laboratory tests.

On the cloud subsystem, the system uses the location of infected individuals using their GPS-enabled mobile phones to track their movement for Social Network Analysis (SNA) and for assessing the geographical risk assessment of the DeV infection using Google Maps. This subsystem depicts the geographical risk by using the information of actually infected and uninfected individuals from hospital databases and cloud storage. This geographical risk assessment alerts the individuals through advice and precautions, guides the individuals for choosing safer paths, and helps the various stakeholders (individuals, government agencies, and health organizations) in controlling the DeV outbreak. The primary objectives of the proposed system are as follows.

- To early screen the possible DeV infected individuals and suggest them for the on-time medical examination for confirming the incidence of the infection.
- To generate real-time diagnostic and suggestive alerts to individuals, and emergency alerts to doctors or caregivers for taking on-time appropriate actions.
- To identify the infected and risk-prone areas geographically for effective and ontime controlling of the DeV infection outbreak.
- To predict the impeding DeV epidemic for generating early warning alerts to individuals for enhancing the effectiveness of the preventive measures.
- To protect the individuals' sensitive health information.

The proposed system does not substitute the doctors and medical procedures, but instead, provide the individuals and healthcare agencies the ability of early and possible diagnose of the DeV infection, so proper medical procedures for diagnosing the actual DeV infection could be adopted, especially in developing and under-developed countries, where most of people are below the poverty line and treat dengue fever as a simple fever, which may sometime cause life-threatening complications to them. The system also helps in avoiding any chaos or panic among individuals due to the rumors during the peak season of dengue by distinguishing dengue fever from simple fever, and subsequently suggesting for proper medical procedures to confirm its incidence.

The proposed system presents an intelligent healthcare system for controlling the DeV infection outbreak using IoT, cloud, and fog paradigms. The significant contributions of the proposed system are as follows.

- The proposed system provides early remote-diagnostic functionality for the possible DeV infection, based on the physiological and environmental parameters.
- The proposed system bridges the gap between the required healthcare infrastructure and available infrastructure, especially in the countries where doctor to patients ratio is very low.
- The proposed system provides real-time diagnostics, suggestive, and curative alerts to the concerned stakeholders (individuals, government agencies and health organizations).
- The proposed system geographically assesses the global DeV infection risk and helps in controlling its outbreak.

The paper has been organized into five sections. In the second section, dengue-based healthcare, Cloud-IoT based healthcare, Fog computing, and Infectious diseases-based intelligent healthcare related significant works have been discussed. The third section discusses the architecture level details of the proposed system. In the fourth section, the

experimental evaluation has been performed along with various results discussions. The fifth section discusses the conclusion of the paper.

# 2 Related work 

This section discusses significant related works based on four different directions. The first subsection discusses the works related to dengue-based healthcare. The second subsection discusses the works related to Cloud-IoT based healthcare. The third subsection discusses the works related to fog computing, and the fourth subsection discusses the works related to infectious diseases-based intelligent healthcare.

### 2.1 Dengue-based healthcare

This subsection discusses various significant works related to DeV infection, which have explored the laboratory features and clinical symptoms of dengue fever and the impact of climatic factors (temperature, humidity, etc.), socioeconomic factors as well as socio-geographical factors on the incidence of DeV infection. In this regard, Huang et al. [18] had identified the clinical symptoms as well as laboratory features for distinguishing the patients diagnosed with influenza from the patients diagnosed with DeV or other pyretic diseases. Sirisena and Noordeen [41] had presented the role of climatic factors in the DeV outbreak. Machado-Machado [24] had evaluated the contribution of both the climatic and socioeconomic factors in determining DeV infection. The results of the work has depicted the more relevant significance of parameters related to climate as determinants for DeV infection than the variables related to socioeconomics. Other than symptoms and environmental factors, many research works have indicated the impact of socio-geographical factors $[48,50]$ as well as human movement [23,32,44] on the transmission of DeV and its outbreak. One such work by Tao et al. [46] had presented a model that depicts the role of the infected humans' movement in contributing DeV infection outbreak and suggested that the restricted movement in infected areas can lower the diffusion risk of DeV infection.

Based on aforementioned factors and various advancements in data analysis-based techniques, various research works have proposed computer-aided DeV detection and prevention systems in the domain of dengue-related healthcare. In this direction, Rao and Kumar [31] had developed a computer-aided diagnostic system for identifying dengue fever based on the clinical and laboratory symptoms. The system has employed data analytics approaches: wrapper-based feature selection method with genetic search and decision tree method for extracting and classifying the symptoms for identifying the incidence of dengue fever. Vinarti and Hederman [51] had proposed a DeV infection risk prediction system that analyzes individual's personal attributes like age, gender and visiting locations, and environmental attributes like specific locations features (aedes aegypti mosquito dwell), climatic conditions (favorable mosquito breeding conditions) to predict the risk of contracting dengue infection by using Bayesian network. Zhang et al. [56] had proposed a DeV infection outbreak surveillance system that analyzes the dengue-related information from online news sources to determine the

dengue outbreak. The system has employed a text mining approach, which extracts the dengue-related articles and apply statistical analyses to determine the number of cases for dengue. The entire intention of this work was to work on the alternative sources of dengue-related information to determine the dengue outbreak, other than the clinical investigation of patients. In this regard, another work by Missier et al. [26] had depicted the extraction of dengue-related information from the social networking platform Twitter, where people use to discuss information online with others, for analyzing the outbreak of dengue infection in particular areas. Sousa et al. [43] had designed a user-oriented platform for reporting mosquito-borne diseases and breeding sites, which helps in supporting the authorities for preventing and controlling mosquitoborne diseases. However, for reducing the dependence on information from the users, which is based on the willingness of the users, the platform has also explored alternate source of information through the mining of geolocated content from social networks.

These motivations of exploring the sources of information other than the clinical investigations and that too for the remote detection of dengue infection have led to the integration of distributed computing paradigms: IoT prototype of wireless sensor network and cloud computing, for establishing various arenas for smart healthcare systems.

# 2.2 Cloud-IoT based healthcare 

The recent years have witnessed the development of a number of smart healthcare systems, which have provided the remote healthcare services through the diffusion of information and communication technologies, in which IoT prototype of wireless sensor networks and cloud computing have played a significant role. The current subsection discusses such various distinctive advancements in the healthcare domain. In this regard, Sandhu et al. [37] had developed a cloud-based DeV infection detection system, which identifies the infection among individuals using keyword aware domain thesaurus, which extracts the relevant keywords from the symptoms submitted by individuals through their mobile devices in any format and converts the message into system-specified format. The system then identifies the dengue cases from these system-formatted data and shares the information with the concerned stakeholders: doctors and caregivers. Liu et al. [22] had discussed an approach for healthcare using digital twin of the physical healthcare approach, which could remotely monitor patients using their data through sensor devices, at the remote servers and provide useful insights, diagnoses and predictions to the concerned stakeholders: doctors and individuals. The approach has identified the key technologies viz. IoT and cloud computing for such a remote healthcare approach, which could be effective in many scenarios, where, doctor to patients ratio is low, patients are not able to visit doctors on regular basis, inconvenience of elderly patients to visit doctors, and continuous monitoring of patient health is required. Kaur et al. [19] had developed machine learning based remote health monitoring approach that doesn't require the presence of doctor with the patient, instead cloud-based decision support system evaluates the IoT-based acquired health data of the individuals and diagnose the disease. The authors have determined the performance of different machine learning algorithms for thyroid, breast cancer

diabetes and liver disorder. Abdel-Basset et al. [2] had proposed wireless body area network-based emergency remote healthcare system that continuously monitors the heart-related data of the patient though multi-criteria decision making data analysis. This system works in cloud-assisted IoT environment and if the system diagnoses that a person is suffering from heart failure, then the system immediately sends the ambulance to the patient. Chung et al. [11] had proposed a IoT-based health risk assessment approach that uses individuals' personal, health and surrounding data for creating a context of an individual and using deep neural network for unwinding context patterns. The approach further employs Minkowski distance formula for evaluating the health risk of an individual with analyzed context patterns by measuring the similarity with the patients having chronic disease. This approach helps in alerting/preventing the individuals with higher risk factors. Latif et al. [21] had developed an integrated healthcare monitoring approach using IoT and cloud computing, that continuously monitors vital health parameters, ensure timely medicinal dosage and emergency prediction. It also provides physicians the data analytics to decide/diagnose the medication errors, medication side effects and prescribe medication accordingly. The approach has employed ranking instances by maximizing the area under ROC curve (RIMARC) for long term medical assessment and classification approaches for short term medical assessment.

The most of the approaches in intelligent healthcare had primarily adopted cloudcentric model for processing the data, where the edge devices were only collecting and pushing the raw data to cloud. Such data off-loading had tended to neglect the computational capabilities of the edge devices in supporting the data analysis at their own and resulted in delaying of data analysis tasks, instead of accomplishment of these tasks immediately near to the data source. As a result, such approaches had suffered overall increased reaction time due to network latency and burdened the cloud with the increased workload, and increased overall renting and running cost of the cloud services.

# 2.3 Fog computing 

As the result of various quality of service issues in cloud-IoT environment, the recent advancements of distributed computing in the form of fog computing and its application in diverse domains viz. disaster management [35], agriculture [17], transportation [33], security [1,4], and alike, have also motivated the utilization of fog computing in healthcare domain too. In this regard, Dautov et al. [14] had discussed the requirement of processing data at the edge devices for better service provisioning in the CloudIoT environment. The authors have proposed a hierarchical data fusion approach in the domain of intelligent healthcare, where the acquired data from the physical world is processed at the different level of hierarchy from IoT sensors to the remote cloud servers at the different edge devices based on their processing capabilities. The approach has employed complex event processing technology for detecting complex event patterns in the stream of data. This approach helps in providing response in real-time and location-dependent. Abdel-Basset et al. [3] had developed a FogIoT based remote diagnostic framework for detecting and monitoring type-2 diabetes using VIšekriterijumsko KOmpromisno Rangiranje (VIKOR, a muli-criteria decision

making technique). This approach employs fog computing for accessing real-time information from cloud and cloud computing for suggesting a compromised decision which will be closed to the ideal solution, in the situations where all criterias are not settled simultaneously. Pace et al. [28] had proposed a mobile phone-based fog computing architecture called as BodyEdge, which provides easiest way to bridge the body sensor network and cloud computing, along with providing data privacy at the fog level, for providing cardiac monitoring services for athletes and factory labourers. Pravin et al. [29] had proposed a fog-cloud computing-assisted IoT framework for predicting and preventing DeV infection. The proposed framework has depicted how DeV-related information moves in a fog-cloud-IoT based distributed system, but, without any further details about the appropriateness of the employed mechanisms for providing various analytics. The system also lacks in providing geographical-locations based DeV outbreak analytics and their visualization to the concerned stakeholders, which are vital for preventing and controlling DeV infection outbreak. Singh et al. [40] had developed a fog-Cloud-IoT based DeV infection monitoring system, which has employed decision tree-based approach at the fog layer for classifying the infection status of the system users and cloud storage-based health information sharing mechanism for providing health analytics to the concerned stakeholders. The major drawbacks of this system are the cloud-based alert generation, which is not so responsive in providing real-time alerts to the concerned stakeholders as compared to the the fog layer. The system also doesn't consider any health severity during generating alerts, and even doesn't explore the infection outbreak controlling perspective of the monitoring approach.

The aforementioned related works depict how Internet of things, cloud computing and fog computing can be used for intelligent healthcare and how their collaborated frameworks can improve the quality of services in various healthcare scenarios. Henceforth, their application in the infectious disease-based healthcare systems can also present effective solutions for helping the world in fighting with global epidemics.

# 2.4 Infectious diseases-based intelligent healthcare 

The recent years have witnessed various incidences of global epidemics such as MERSCoV and Ebola. For controlling such global epidemics, several key factors have played crucial roles. Among them, speed of diagnosing the infected individuals, tracking their movement and tracing of their contacted persons, and depicting the risk level of infection at different locations, have remained the focus of epidemic controlling strategy. In this regard, Majumdar et al. [25] had developed a fog-based approach to diagnose Kyasanur Forest Disease (KFD) using extremal optimization tuned neural network (EO-NN) at the fog devices and GPS-based visualization of each infected user and risk prone region on Google Maps. However, the authors haven't represented the epidemic perspective of the infection through maps. Sandhu et al. [36] had presented a BBN-based prediction model that predicts the incidence of the MERS-CoV using Cloud-IoT and provides timely medical support. The system has used the concept of population density of infected and uninfected individuals in a particular area to ascertain the risk level of infection in those areas. Raghav and Dhavachelvan [30]

had proposed a fog-based cyber physical system for remotely diagnosing the severe acute respiratory syndrome cronavirus (SARS-CoV) and analyzing its outbreak. The system has employed J48 decision tree for classifying the type of infection and big data-based approach MongoDB for storing, modeling, analyzing and visualizing the SARS outbreak.

Based on the aforementioned discussion and observation from it, a comparisonbased performance analysis of the proposed system with some significant existing systems has been shown in Table 1. The performance has been analyzed based on nine parameters viz. IoT, Cloud Computing, Fog Computing, Health monitoring, Environment Monitoring, Real-Time Perspective, Epidemic Susceptance Analysis, Pandemic Susceptance Analysis, Healthcare Data Security, and Geographical Risk Analysis. The values " $Y$ " or " $N$ " depicts the inclusion of mentioned technology or functionality in a particular system or not. The analysis depicts that only the proposed system includes all the mentioned parameters, and henceforth acknowledges the performance edge as compared to other existing systems.

# 3 Proposed system 

The proposed system comprises three subsystems, as shown in Fig. 1, namely data acquisition subsystem, fog subsystem, and cloud subsystem. The responsibility of the data acquisition subsystem is to collect the data related to individuals' personal and health attributes from their mobile phone applications, and data regarding the surroundings from environmental sensors. This subsystem transmits the collected data to the fog subsystem for the real-time diagnosis of the possibly infected individuals. On diagnosing the possibly infected individuals, the fog subsystem immediately generates diagnostic and suggestive alerts to the possibly infected individuals' mobile phones for suggesting to follow proper medical procedures, and emergency alerts to the doctors and caregivers, if individuals' health becomes sensitive. The alert generation on the fog subsystem enables the on-time efforts for taking precautionary measures. The compiled medical information and DeV classified data of each individual, along with the actual diagnose of DeV infection from hospital databases, are stored on the cloud subsystem. The cloud subsystem deploys Social Network Analysis (SNA) to analyze the geographical information of each registered individual to identify the infected and risk-prone areas, and its pinpointing on Google Maps, which aids the efficient controlling and prevention of DeV outbreak. The cloud subsystem also protects the privacy of the personal health-related information of the individuals using information granulation and secret sharing. The notations used throughout the paper are enlisted in Table 2. Each subsystem of the proposed system has been explained ahead.

### 3.1 Data acquisition subsystem

This subsystem collects the data regarding individuals' personal and health attributes from their mobile phone applications and the data regarding the surroundings from the environmental and mosquito sensors. Initially, the individuals register with the


![img-0.jpeg](img-0.jpeg)

Fig. 1 DeV infection controlling model

Table 2 List of used notations


Table 3 Personal, environmental and health attributes


Table 3 continued


system by providing personal information via a mobile application on their phones. Then, the system generates a unique identification (uId) for each registered individual and acquires the DeV infection-related health data. The values of the personal attributes remain the same for most of the period and only changed when any attribute changes, whereas the attribute-values related to the individual's health and environment change over time. The health data is acquired periodically through the registered

individuals' mobile phones in the form of "Yes" or "No". For infected individuals, the data is acquired on an hourly basis; for recovered individuals, the data is acquired on alternative days for a fortnight (after which the recovered individual is declared uninfected), and for uninfected individuals, the data is acquired weekly. Table 3 depicts the personal, environmental, and health attributes, which are acquired by the system. The personal attributes are stored on secure locations to avoid any disclosure of the personal identity of the individual to any unauthorized stakeholder and to avoid any unnecessary discrimination and panic among the people. The information regarding the sites of mosquito density and mosquito breeding are captured using different site-located wireless mosquito sensors. These mosquito sensors identify and count the number of mosquitoes in a specific area. The attributes sensed by environmental sensors like air temperature, humidity and carbon dioxide around the standing water sites signify the favorable conditions for mosquitoes breeding. The higher humidity, temperature, and carbon dioxide values are the favorable conditions for mosquitoes' breeding. So, these environmental attributes are continuously acquired and stored in the Cloud database for identifying the breeding sites.

# 3.2 Fog subsystem 

This subsystem plays the role of a bridge between the Cloud and the data acquisition subsystems. It pre-processes the data accumulated from the data acquisition subsystem for classifying the individuals as possibly infected (In) or uninfected (Un) and subsequently generates the real-time diagnostic, suggestive, and emergency alerts to individuals and other concerned stakeholders. This classification diagnoses the possibly DeV infected individuals and suggests them for following proper medical procedures to confirm the incidence of the infection by consulting with the doctors and through recommended laboratory tests (if requires). At the same time, this layer alerts the caregivers or doctors, if the health sensitivity with respect to the various environmental events, surpasses the threshold. This subsystem comprises of two components: (I) Fog-based DeV Infection Diagnosis, and (II) Time-based alert generation. The Fog components are explained as follows.

### 3.2.1 Fog-based DeV infection diagnosis

This component utilizes a probabilistic classification model called Naive Bayesian Network (NBN) [45] for classifying the individuals based upon their health attributes as In or Un. In this model, X1, X2...Xn are considered as the conditionally independent predictor variables of a given class variable $D$. Since the entire set of DeV infection-related health attributes are independent of each other, the NBN classifies the individuals under the category of In or Un. The training dataset estimates the probability parameters using the maximum likelihood estimator. Figure 2 shows the graphical structure of the NBN for categorizing registered individuals.

We assume, $D$ as a class variable for representing two categories: In and $U n$, based on the symptom vector $S y V_{k}=(F, S H, P E, N A, J P, V, M P, S R, M B, A P)$. To classify an individual $u_{k} \in X ; k=1,2, \ldots, \mathrm{n}$ as In or $U n$ based on his/her $S y V_{k}$, the probability of

![img-1.jpeg](img-1.jpeg)

Fig. 2 Naive Bayesian network for diagnosing DeV infection
each classified category is calculated using the Bayes' rule as given in Eqs. 1 and 2.

$$
\begin{aligned}
& P\left(D=\left(\operatorname{In} / S y V_{k}\right)\right)=\frac{P(\operatorname{In}) P\left(S y V_{k} / \operatorname{In}\right)}{P\left(S y V_{k}\right)} \\
& P\left(D=\left(\operatorname{Un} / S y V_{k}\right)\right)=\frac{P(\operatorname{Un}) P\left(S y V_{k} / \operatorname{Un}\right)}{P\left(S y V_{k}\right)}
\end{aligned}
$$

where $P\left(D=\operatorname{In} / S y V_{k}\right)$ represents the probability of an individual classified as a possibly infected with DeV infection based on his/her symptom vector $S y V_{k}$; $P\left(D=U n / S y V_{k}\right)$ represents the probability of an individual classified as an uninfected of DeV infection based on his/her symptom vector $S y V_{k} ; P(\operatorname{In})$ and $P(\operatorname{Un})$ represent the probabilities of having DeV infection, and $P\left(S y V_{k}\right)$ represents the probability of having $S y V_{k}$ symptoms. The comparison of the probabilities of two categories determines the category of an individual. The category of the individual is decided from the fact that the class, which is having higher probability, is the category of the individual.

# 3.2.2 Time-based alert generation 

This component is used to generate the diagnostic and suggestive alerts to the individuals based on their diagnosed category and emergency alerts to the doctors or caregivers based on the health sensitivity of infected individuals with respect to the environment so that timely action for individuals' care can be taken. Fog-based DeV infection diagnosis component determines the health category of an individual as In (Unsafe state) or Un (Safe state). Mathematically, an individual's state is denoted by $\mathrm{S}=\{\mathrm{D}, \mathrm{E}, \Delta \mathrm{T}\}$ where ' D ' is the classified category of an individual, ' E ' represents the environmental events which happens in ' $\Delta \mathrm{T}$ ' time window. In another way, ' E ' is represented as \{Humidity, Carbon Dioxide, Air Temperature, Breeding Sites, and Mosquito Density\}. Determination of an individual's health category is important for the medical emergency alert generation to doctors or caregivers. If the individual is classified in the category In, then the occurrences of any undesired environmental event leads the individual's health state to a more severe unsafe state. In this case,

emergency alerts are generated based on the occurrence of the environmental events in $\Delta T$ time-space. It is determined on the basis of the Environmental Event Index (EEI). The probability of EEI is calculated, as shown in Eq. 3.

$$
P(E E I)=\delta\left(\frac{P(E)}{P(I n)}\right)
$$

where $P(E)$ is the probability for the occurrence of undesired environmental events, $P(I n)$ is the probability of an individual's classified category as possibly infected, $\delta$ is the differentiation function, and $P(E E I)$ is the probability of environmental event index.
$P(E E I)$ determines the occurrence rate of sensitive environmental events with respect to the infection of an individual. $P(E E I)$ helps in depicting the health sensitivity of a possibly infected individual with respect to the occurrence of environmental events. The step by step procedure for generating emergency alerts is depicted in Algorithm 1. In this algorithm, the health attributes are examined using NBN for an individual's DeV infection category determination. If an individual's DeV infection category is found as In, a checkpoint is created and saved on the fog subsystem. Then, IoT devices continuously transmit the data regarding surrounding environmental events during the infected period of the individual to temporary log events, at fog storage. These log values are examined for asserting the severity of the environmental events during the individual's infection period by calculating $P(E E I) . P(E E I)$ helps in determining the individual's health sensitiveness due to environmental factors $E$, based on predefined thresholds $(\beta)$. If $P(E E I)>\beta$, the emergency alert is generated to the doctors or caregivers. After predefined time window $\Delta T$, the subsystem re-examines the individual's health state. At any instant, if an individual is found in unsafe state, the $P(E E I)$ is determined for $\Delta T$, and emergency alerts are generated to the doctors or caregivers along with the log information if $P(E E I)$ surpasses its threshold. After $\Delta T$, the checkpoint is terminated, and the process of monitoring is repeated.

Based on the suggestive and emergency alerts, and in consultation with doctors, the actual confirmation of the DeV infection is determined at the hospitals' laboratories. The possible diagnoses by the fog subsystem help the individuals in getting on-time medical aid. Subsequently, the information of confirmed DeV infected and uninfected individuals at hospitals and uninfected individuals analyzed at the Fog subsystem, along with generated alerts, is transmitted to the Cloud subsystem.

# 3.3 Cloud subsystem 

The Cloud subsystem stores and processes the data, which was not possible to be processed at the fog subsystem due to computation and space constraints. This subsystem comprises of four components: (I) Cloud storage, (II) Information Protection, (III) GPS-based risk assessment, and (IV) Health communication. The detailed explanation of each component is as follows.

Input : Set of Values (Event information $=\{$ Health attributes $U$ Environmental attributes\})
Output: Sets of Records (Generated alerts)
Classify the health category of an individual using BBN;
Determine the time stamp of the current instance;
if category $==$ In, then
Individual is in unsafe state;
Check point is created to mark the save point in time space;
Empty the log to repopulate new environmental events;
Start new session to add environmental attributes to the log for next $\Delta \mathrm{T}$;
Calculate, $P(E E I)=\delta\left(\frac{P(E)}{P(I n)}\right)$
if $P(E E I)>\beta$, then
Generate emergency alerts to the doctors or caregivers along with log information;
end
else
Generate diagnostic, and suggestive alerts to the individual;
end
end
else
Individual is uninfected, so generate diagnostic alert;
end
Algorithm 1: Alert Generation at Fog Subsystem

# 3.3.1 Cloud storage 

This component stores each individual's compiled medical information, fog analyzed diagnosed DeV infection category, generated alerts (accumulated from fog subsystem), and the actual diagnosis of the DeV infection of the individuals (accumulated from hospital databases), for further analysis at the cloud subsystem. Based on the data received from the fog subsystem and hospital databases, this component updates the actual DeV infection category of the individuals. Cloud storage enables the secure sharing of personal information of individuals among authorized stakeholders like individuals, hospitals, government agencies, and healthcare professionals. The visiting locations related information of the individuals is also stored there and is used to create the SNA graph and synthesize various useful analytics related to the DeV outbreak analysis.

![img-2.jpeg](img-2.jpeg)

Fig. 3 Data table conversion based on information granulation

# 3.3.2 Information protection 

The data of an individual viz. personal and health attributes and environmental data are stored at the Cloud storage. This sensitive information needs to be shared with authorized stakeholders only. Any unintentional disclosure of information to any unauthorized person can result in a distress situation among individuals. Hence, a two-stage information protection mechanism is proposed in this system: (I) information granulation [55], and (II) secret sharing scheme [38]. In the first stage, the individual's data is divided into three different data tables, i.e., L-I, L-II, and L-III. In L-I, the table contains the utmost confidential data, which can identify an individual precisely, i.e., name, age, sex, residential address, and mobile number. In L-II, the table contains medium-level confidential information, which can identify a DeV outbreak affected location. It includes environmental attributes: mosquitoes density and its site's location, temperature, humidity, carbon dioxide. In L-III, the table contains the least sensitive information, which cannot create any panic or distress on its unauthorized access. It includes health attributes like fever, skin rashes, headache, bleeding, muscle pain, joint pain, etc. If someone access L-II or L-III information in an unauthorized way, the system still preserves the sensitive information because the precise identity of the individual still cannot be ascertained. To identify the individual and his/her location, the only key is to access all three fragments and correlate them. That is why the acquired information is fragmented into appropriate data fragments in the proposed system. Figure 3 represents the proposed data granulation. A DeV infection data table is defined as $\mathrm{DeV}_{D T}=(w, a t)$, where $w$ depicts the registered individuals' count and at depicts the set of personal, environmental, and health attributes of each individual. The data table is fragmented into L-I, L-II, and L-III, i.e., $\mathrm{DeV}_{D T}=(w, \mathrm{~L}-\mathrm{I}$ U L-II U L-III). These fragments are combined by using a unique identification number. After granulation, mechanism of secret sharing is applied to split the value of highly sensitive attributes of L-I (personal attributes) into secret shares. These secret shares are kept on secure servers so that no one can access information of L-I. If anyone is able to collect the information of all three fragments, the exact identity of the individual still can not be retrieved due to the generation of secret shares for L-I information.

# 3.3.3 GPS-based risk assessment 

Female Aedes albopictis or Aedes agypti mosquitoes' biting are the main sources of DeV transmission in the human blood. This virus replicates in human blood and transmitted to other uninfected mosquitoes on bitting DeV infected human beings. These infected mosquitoes can lay infectious eggs and further transmit this virus. Because of the limited flight of the mosquitoes, they cannot fly to farther locations, but by transmitting the infection into humans, wide-area spread of DeV happens through infected humans traveling to various and far away locations by further transmitting the DeV into uninfected mosquitoes. Hence, the Social Network Analysis (SNA) can be a significant approach to analyze and represent the geographical risk of DeV infection by analyzing the location-related information of the individuals and synthesizing various useful insights.

In this component, SNA has been used to analyze the registered individuals' movement-related geographical information through their mobile phone-based GPS for identifying the infected and risk-prone regions, and its pinpointing on Google Maps. SNA also helps in synthesizing various useful insights like Epidemic Susceptance Index (ESI) of each individual and region, and Pandemic Susceptance Index (PSI) of each region to ascertain the severity of the DeV outbreak. Subsequently, SNA helps in providing preventive measures for controlling its outbreak. For ascertaining the behavior of DeV infection outbreak within the region or from one region to another region, following scenarios have been considered.

Scenario 1 An individual is infected in a region $x$, if the mosquitoes of the region $x$ bite an uninfected individual, who is: (I) resident of the region $x$ and present in region $x$, or (II) resident of the region $y$ but visited region $x$.

Scenario 2 A Mosquito is infected in a region $x$, if the susceptible mosquito bites an infected individual, who is: (I) resident of the region $x$ and present in region $x$, or (II) resident of the region $y$ but visited region $x$.

By considering the above-discussed scenarios as the basis, various useful analytics can be synthesized if the global SNA graph is created efficiently. Therefore, Algorithm 2 is used for the systematic creation of the global SNA graph using GPS-based geographical location of individuals through their phones and DeV infection status from cloud storage. Here, in the SNA graph, three-node (residence, workplace, and user) for an individual is created and colored according to the proposed color scheme, as shown in Fig. 4a. The permanent locations (i.e., residence and workplace) and visiting locations are traced and labeled as $P$ and $V$ respectively. The edges are drawn from the user node to all his/her visiting locations and colored according to the color of the user node. The population percentage of infected $P$ and infected $V$ nodes is calculated in each region to identify them as infected or risk-prone regions using Fig. 4b, c and Table 4.

Once the risk level of various regions is identified on the SNA graph, several metrics can be synthesized and the outbreak of infection can be checked, and the individuals in those regions (like residents or visitors) can be alerted in real-time by sending warning alert messages. Also, various precautionary measures and suggestions can be provided to them to control the infection rate and transmission process. The various significant metrics that can be drawn from the SNA graph are explained as follow.

![img-3.jpeg](img-3.jpeg)

Fig. 4 Dengue risk-based color scheme for social network analysis: a node color, b region color based on the infected residents' population percentage, and $\mathbf{c}$ region color based on the infected visitors' population percentage

Table 4 Population-based risk level color scheme


I. Metric 1 Epidemic Susceptance Index (ESI).

ESI determines the individual's or region's probability to spread or contract DeV infection based on the SNA graph.
(a) $\mathrm{ESI}_{I n R}$ (for Infected Region)

It states the ratio of the number of infected visitors and infected residents in an infected region to the total number of visitors and residents in that area, as shown in Eq. 4.
$E S I_{I n R}=\frac{\text { Number of infected visitors and infected residents in an infected region }}{\text { Total number of visitors and residents in that region }}$

Input : Set of Values (Individuals' workplace, residential and traveling locations)
Output: Updated DeV Outbreak Map
Get the uId, DeV infection category, residential and workplace location of the individuals;
if category $==I n$, then
Create three red nodes, one for the individual and two for the location of his/her residence and workplace;
Label the residence and workplace nodes as P ;
Get user's travelling locations' information;
end
else
Create three green nodes, one for the individual and two for the location of his/her residence and workplace;
Label the residence and workplace nodes as P ;
Get user's travelling locations' information;
end
for every $i^{\text {th }}$ region of SNA graph, do
for every $j^{\text {th }}$ visiting location of the individual, do
if visiting location lies in $i^{\text {th }}$ region, then
if individual's visiting node is already present, then
Create an edge between the user node and the visited location node;
Update the color of node according to the color of the user node;
end
else
Create a node for the visited location in $i^{\text {th }}$ region;
Label it as V;
Create an edge between user node and visited location node;
Update color of node according the color of user node;
end
end
end
end
for every $i^{\text {th }}$ region of SNA graph, do
Calculate the population percentage of red $P$ and red $V$ nodes in each region;
Color the regions based on the population-based risk level color scheme mentioned in Table 4;
end
Algorithm 2: Global SNA Graph Building
(b) $\mathrm{ESI}_{I n I}$ (for Infected Individual)

It states the ratio of the number of infected regions visited by the infected individual to the total number of regions visited by the same individual, as

shown in Eq. 5.

$$
E S I_{I n I}=\frac{\text { Number of infected regions visited by an infected individual }}{\text { Total number of visits by the same individual }}
$$

(c) $\mathrm{ESI}_{R p R}$ (for Risk Prone Region)

It states the ratio of the number of infected individuals' visits in a risk-prone region to the total number of individuals' visits in that region, as shown in Eq. 6.

$$
E S I_{R p R}=\frac{\text { Number of infected individuals' visits in a risk-prone region }}{\text { Total number of visits in that region }}
$$

(d) $\mathrm{ESI}_{U n I}$ (for Uninfected Individual)

It states the ratio of the number of infected and risk-prone regions visited by the uninfected individual to the total number of regions visited by the same individual, as shown in Eq. 7.

$$
E S I_{U n I}=\frac{\text { Number of infected and risk-prone regions visited by an uninfected individual }}{\text { Total number of regions visited by the same individual }}
$$

If $\mathrm{ESI}_{I n R}$ of an infected region is high, it means many infected individuals have visited or/and infection among residents is high in that region. So, visitors are required to be warned to refrain their visits to that region, and residents are required to be warned to have immediate medical checkups for determining their health status and required precautions. At the same time, nearby hospitals are also needed to be alerted about the high $\mathrm{ESI}_{I n R}$ of that region. If $\mathrm{ESI}_{I n I}$ of an infected person is very high, it means that the person is highly infected because of his/her visits to many infected regions. That person is required to be quarantined for proper treatment and restricted to travel, for controlling DeV spread. Hence, the alerts are required to be generated to that person and hospitals near his/her residence for his/her proper treatment. If $\mathrm{ESI}_{R p R}$ of a risk-prone region is high, it means many infected visitors are visiting that region. So, that region is very susceptible to spread DeV infection to its residents and future visitors. So, people with low immunity are required to be warned to refrain their visits to such regions, and at the same time, residents of those regions are required to be warned to take necessary precautions for avoiding the contraction of DeV infection. If $\mathrm{ESI}_{U n I}$ of an uninfected individual is high, it means that a person is visiting many infected locations and risk-prone regions. His/her susceptance is very high to contract DeV infection. So, warning alerts are required to be generated to that individual for precautions and immediate checkup at the hospital.
II. Metric 2 Pandemic Susceptance Index (PSI).

PSI determines how fast a particular region is spreading the DeV infection over time to the other regions. The spread of DeV infection from a particular region can be analyzed by creating a tree, based on the catching of infection by the neighbor regions or neighbors of neighbor regions or, like so, on the temporal

scale. The number of nodes in a temporal infection tree depicts the pandemic spread of infection to that extent (see Algorithm 3).

Input : Temporal SNA graph
Output: PSI of the region
for every instance on temporal scale, do
for every $i^{\text {th }}$ region, do
create infection tree;
calculate the number of nodes in each tree;
$\mathrm{PSI}_{i}=$ total number of nodes;
end
end
Algorithm 3: PSI Determination

The prediction of the DeV infection outbreak can control its pandemic nature and enable early warning alerts to the people who are living in those regions and to the healthcare agencies for taking effective preventive measures in its early stage. The prediction uses the following methods to predict the dengue cases, which are explained as follows.
(a) Autoregressive Method Autoregressive prediction method forecasts the dengue cases by using past dengue cases of the given region. Dengue cases in month ' $t$ ' are computed as shown in Eq. 8.

$$
Y_{t}=\emptyset_{0}+\emptyset_{t-1} Y_{t-1}+\emptyset_{t-2} Y_{t-2}+\emptyset_{t-3} Y_{t-3} \ldots \ldots \ldots \ldots . \emptyset_{t-p} Y_{t-p}
$$

where $\emptyset_{0}$ is the constant number of dengue cases, $Y_{t}$ is the number of dengue cases at time ' $t$ ', $Y_{t-1}$ is the number of dengue cases at time ' $t-1$ ', $Y_{t-p}$ depicts the number of dengue cases at time 't-p'. $\emptyset_{t-1}, \emptyset_{t-2}, \emptyset_{t-3} \ldots \ldots . \emptyset_{t-p}$ are the autoregressive parameters in last ' p ' months. This forecasting helps in determining the dengue cases based on the trend of past months' dengue cases.
(b) Weather Prediction Method The dengue infection is profoundly impacted due to the weather conditions as the population of dengue mosquitoes grow in particular weather conditions. The climatic variables, such as temperature, rainfall and humidity, impacts the incidence of dengue cases. Here, we consider only two climate variables, i.e., temperature and rainfall, as these are the strong predictors for dengue prediction. Based on the climate lag [10], the incidence of dengue appears after some days, weeks or months, of exposure to climatic conditions. Dengue can occur several days after the favorable weather conditions. The impact of monthly mean temperature on a number of dengue cases is used to predict

dengue incidence as shown in Eq. 9.

$$
C_{T e m p}=\emptyset_{0}+\sum_{m=t-(l+p)}^{t=l} \emptyset_{m n} T e m p_{m n}
$$

where $\emptyset_{0}$ is the constant number of dengue cases. $\emptyset_{m n}$ is the parameter of mean temperature at lag term $m$ in $n$ mean temperature range. $m=t-(l+p)$ depicts the start of the lag period, $t$ depicts month, $l$ depicts lag term, $p$ depicts the monthly mean temperature's data cycle period.
The determination of $C_{\text {Temp }}$ helps in asserting the number of dengue cases well before its incidence based on the climate lag effect using monthly mean temperature. Similarly, using monthly cumulative rainfall, the number of dengue cases can be asserted as shown in Eq. 10.

$$
C_{R a i n}=\gamma_{0}+\sum_{a=t-(L+q)}^{t=l} \gamma_{a b} R a i n_{a b}
$$

where $\gamma_{0}$ depicts the constant number of dengue cases. $\gamma_{a b}$ depicts the parameter of cumulative rainfall at lag term $a$ in $b$ cumulative temperature range. $a=t-(L+q)$ depicts the start of the lag period, $t$ depicts month, $L$ depicts lag term, $q$ depicts the monthly cumulative rainfall's data cycle period.

From these two metrics, the prediction of dengue cases using the influence of temperature and rainfall can be computed a much time ahead. A weather-based prediction in dengue early warning system can help in local vector surveillance and control in many ways. Firstly, it can enhance the effectiveness in efforts to check the scale of the DeV infection outbreak. This will result in decreasing the disease transmission, avert possible mortality, and subsequently lower the burden and operating cost of healthcare agencies. Secondly, it can use the publicly available weather variables without investing in weather-based predictive methods. Thirdly, it can allow the vector control units to focus more deliberately and sensibly during high-risk periods.

The identified infected and risk-prone regions based on the population of infected residents (Red P) and infected visitors (Red V) in the SNA graph, reflects the current global DeV outbreak. Apart from this, the areas where there is a high probability of occurrence of dengue cases in the future are also considered as high risk-prone areas. Based on the assessed risk level of DeV infection, the regions are mapped and updated on Google Maps, as shown in Algorithm 4. It helps the proposed system in generating real-time warning alerts to the individuals residing and visiting in various regions based on the respective risk levels and providing suggestions for precautions and appropriate treatments. At the same time, the nearby hospitals, health professionals, and other government agencies are also get alerted to deal with the global situation and control the DeV outbreak.

Once the up to date and timely information about risk-prone and infected regions are available online on Google Maps web service, it helps the healthcare agencies,

Input : SNA graph
Output: DeV outbreak updated Google Maps
for every $i^{\text {th }}$ region of SNA graph, do
Plot the hexagonal structure of SNA region based on the GPS coordinates on Google Maps;
Color the plotted region according to the color depiction in SNA graph;
end
Algorithm 4: Mapping of DeV Regional Risk Assesment on Google Maps
government agencies, and residents in preventing the spread of the DeV outbreak, based on the generated warning alerts, as shown in Algorithm 5.

Input : Individual's current location, Updated Google Maps
Output: Generated Warning Alert
Trace individual's current GPS location;
if location lies in the infected or risk prone region, then
if category=In, then
Send advices to the individual's mobile phone mentioned in Table 5;
Generate alerts to the medical agencies and nearby hospitals about that individual;
end
else
Send precautions to the individual's mobile phone mentioned in Table 5;
end
end
Algorithm 5: Alert Generation using GPS-based risk assessment

# 3.3.4 Health communication 

The health communication component sends the system generated alerts and health awareness tips to the registered individuals. Instant messaging (IM) or email service is used for this communication. Alert messages and health awareness suggestions are sent repetitively to individuals. It aids in enforcing preventive measures awareness and reduction in the DeV infection risk. Alerts are also generated to the government healthcare agencies as well as nearby hospitals based on the patient's GPS location. It helps in providing first aid and organizes the required free medical camps to control

Table 5 Advices and precautions


# Advices 

1. Urgent consultation with the doctor for treatment and hospitalization is required
2. Full blood count should be checked at least on the second day of illness
3. Ensure adequate oral fluids (coconut water, giloy juice, fruit juice) around $250 \mathrm{ml} / \mathrm{h}$ for 24 h
4. Drink maximum water in order to replace fluid loss
5. Adequate physical rest, tepid sponging for fever
6. Pomegranate juice/ black grape juice should be taken to increase blood count
7. Avoid solid foods during the fever period
8. Include Immunity boosting food items in the meal

## Precautions

1 Wear full body covered clothes like full trousers with socks, full sleeve shirts during the transmission season
2 Use mosquito repellent products like creams, liquids, coils, mats, etc
3 Do not leave open your trash and dustbin
4 Avoid mosquito bite by using Bed nets for sleeping during day time
5 Regularly change the water of refrigerator trays, air coolers, and water containers once a week
6 Cover the containers which hold water to prevent water access to mosquitoes
7 Avoid visiting shrubby areas because adult mosquitoes usually rest in these areas during the day
8 Make sure your window and door screens do not provide any kind of access path to mosquitoes to enter your building
$9 \quad$ Change water in birdbaths at least weekly
the DeV outbreak. The advices and cautionary measures for individuals have been represented in Table 5.

## 4 Experimental setup

The Experimental setup of the proposed system has been divided into six subsections viz. data generation, Fog-based DeV infection diagnosis evaluation, alert generation

Table 6 Sample of different combinations of dengue-related health attributes


evaluation, dengue cases prediction evaluation, information protection security analysis, and GPS-based risk assessment evaluation.

# 4.1 Data generation 

The experiment for the proposed system had required DeV infection-related symptoms-based health data. However, the thorough internet search and even the consultation with different hospitals did not find any symptoms-based dengue dataset for evaluating the proposed system. So, the dataset had been systematically generated in collaboration with Dr. Arvind Manchanda. He is an M.D. in medicine and working in Punjab government health services. Based on the health records of 177 patients, checked for DeV infection [9], a dataset had been generated in collaboration with the doctor. The generated dataset had been further consulted with the community health professionals to validate its closeness with the real data. The generated dataset considers all possible combinations of symptoms, having ten attributes with value as either Yes or No to diagnose any individual for possible DeV infection. A few possible combinations of 10 dengue-related health attributes have been shown in Table 6. The overall permutation of these cases had been resulted in $2^{10}=1024$ combinations. The probability of the occurrence of a particular combination of all symptoms is unique in the generated dataset. So, the symptoms have been categorized into three groups based on their occurrence in DeV infected cases: (I) Most Probable Symptoms i.e., fever, (II) Probable Symptoms viz. severe headache, vomiting, pain behind eyes, severe abdominal pain, and skin rash, and (III) Least Probable Symptoms viz. joint pain, muscle pain, soft bleeding, and nausea. The combined occurrence of these symptoms in DeV infected cases has been shown in Table 7.

For the systematic generation of the environmental dataset, an IoT-based scenario had been created in Java-based simulator CupCarbon U-one 3.8.2 [12]. The created IoT

Table 7 Occurrence-based symptoms combinations


scenario is based on Pathankot, the ninth most populated city of the Punjab province in India. A total of 1240 sensors had been deployed on various locations to capture the environmental attributes such as the location of breeding and mosquito dense sites, humidity, carbon dioxide, and the temperature. These sensors had been programmed with senscript (scripting language for CupCarbon) for generating random values of environmental attributes. The environmental dataset had been acquired from these sensors, which comprises the Sensor Location, Sensor ID, and respective attributevalue. The proposed system uses Algorithm 6 to map all possible combinations of DeV infection-related health records with the environmental dataset.

Input : Health dataset, Environmental dataset and Required number of distinct cases
Output: Dengue-related dataset
' $c$ ' be the required number of dengue cases initialized with 1 ;
while $c<=$ required number of cases, do
Randomly pick a health record from the health dataset;
Create a new case by mapping the environmental data with the health record;
if newly created case already exists in dengue dataset, then
Don't append the newly created case and discard it;
end
else
Append the newly created case in the dataset;
Increment 'c' by 1 ;
end
end
Algorithm 6: Dengue-based Dataset Generation

Table 8 Performance of different learning algorithms for NBN


# 4.2 Fog-based DeV infection diagnosis evaluation 

The timely diagnosis of the DeV infection is critical in saving the lives of individuals and real-time depiction of infection outbreak. Hence, the proposed system has deployed Fog-assisted NBN-based probabilistic model for classifying the individuals as In or Un. The Bayesian network has been created using R-Studio's bnlearn package [39] with 1024 individuals' health data, using different learning algorithms viz. incremental association (iamb), grow-shringk (gs), interleaved incremental association (inter.iamb), fast incremental association (fast.iamb) and hill climbing (hc), and evaluated based on the parameters viz. number of nodes, number of directed arcs, number of undirected arcs, average branching factor, average neighborhood size, penalization coefficient and number of tests used in the learning procedure. The evaluation of the created networks through these algorithms has been compared and shown in Table 8, and found the performance of 'hc' algorithm better as compared to the others because of its higher number of directed arcs. Therefore, the fog-based DeV infection diagnosis has used the 'hc' algorithm for training the Bayesian network.

The current evaluation has further employed Weka 3.6 for testing the trained NBN [54] with 1024 health records. The evaluation has also compared the classification performance of NBN with other state of the art classification approaches viz. Neural Network (NN), Fuzzy System (FS), and Bayesian Belief Network (BBN), as shown in Fig. 5. For NN, the multilayer perceptron function of the weka has been employed with two hidden layers, learning rate of 0.3 and momentum of 0.2 , whereas the FS has been implemented with R-Studio's sets package, and the BBN with R-Studio's bnclassify package. The evaluation has included a set of statistical performance measures [16,20] viz. accuracy, sensitivity, precision, specificity and F-measure, for evaluating the classification performance of the employed classifiers. Figure 5a depicts the classification accuracy of all four employed classifiers, where NBN has the best classification accu-

Table 9 10-Fold cross validation of employed classification approaches


![img-4.jpeg](img-4.jpeg)

Fig. 5 Performance comparison of classification approaches through: a classification accuracy, and $\mathbf{b}$ statistical measures
racy throughout the process, whereas the Fig. 5b represents the different statistical measures viz. sensitivity, precision, specificity, and F-measure of the employed classification approaches. The obtained results in Fig. 5b are the average performance outcomes from the ten folds of the 10 -fold cross validation method, as shown in Table 9. The performance analysis from Fig. 5b and Table 9, has found that the NBN has performed better in all measures as compared to the other classifiers. It has been noticed that the performance of NBN yielded better results than other classifiers in every parameter and hence, found satisfactory for employing in the proposed system.

The execution (or classification) time of all four employed classifiers for their training and testing phases, have been shown in Fig. 6a, b. From the analysis of their performances in terms of execution time, it has been well-depicted that NBN has taken the overall least time in classifying the DeV infection status of the individuals in both phases, as compared to the other employed classifiers.

The evaluation has also presented the detailed class-wise performance analysis of the NBN-based classification in Table 10. The results depict the higher accuracy and lower false classification rate of NBN in classifying the DeV infected individuals. The results depict that the overall classification accuracy of NBN is $98.24 \%$. and weighted average Sensitivity (True Positive rate) of NBN is 0.940 . These higher value of accuracy and sensitivity generates higher precision, which is 0.898 and enable the system to minimize error rate [15]. Along with this, the overall higher value of specificity i.e. 0.951 leads the NBN in generating less classification errors. Similarly, the higher values of F-Measure ( 0.977 ) and ROC ( 0.853 ) indicates the accuracy of the NBN-based classification [5]. Hence, it is safe to state that the level of performance conceived through above-mentioned parameters justifies the utility of NBN in fogbased DeV infection classification in the proposed system.

# 4.3 Alert generation evaluation 

The proposed fog-based alert generation provides timely information about the DeV infection diagnosis to the concerned stakeholders. The response time and the reliability of the generated alerts viz. sensitivity, precision and specificity, are considered as the critical parameters for estimating the efficiency of the alert generation [15]. That's why,

![img-5.jpeg](img-5.jpeg)

Fig. 6 Execution time of classification approaches during: a training phase, and $\mathbf{b}$ testing phase

Table 10 Detailed class-wise accuracy of Naive Bayesian network


the proposed fog-based alert generation has been systematic examined for evaluating its effectiveness in providing accurate and on-time delivery of the generated alerts to the concerned stakeholders.

Figure 7 depicts the architectural details of the evaluating model, where, the proposed fog-based alert generation has been evaluated on a smartphone with 4 GB memory and snapdragon 6361.8 Ghz Octa-core processor, and compared with a system having same alert generation functionality (with same NBN-based DeV diagnosis), but at EC2-based Cloud instance and having no provision of fog computing. Both the systems have used the same set of health data samples ranges 100 to 1024 in size. The both systems have considered the time taken from the occurrence of an event (diagnose of DeV infection status or determination of individual's severe condition) to the instance on which the alert about the event occurrence delivered to the individual, as the response time (or delay). Whereas, the reliability of the alerts has been indicated in terms of the ability of the DeV infection diagnosing process in determining the true alerts.

Table 11 depicts the results of various parameters viz. minimum delay, maximum delay, average delay, standard deviation in delay, sensitivity, specificity, coverage, precision, root average square error, mean absolute error, root relative squared error and relative absolute error for comparing the alert generation performance of the proposed and Cloud-based system. The results has indicated that the proposed system has far better alert generation functionality with taking almost half time on average for delivering alerts, as compared to the cloud-based system. On the reliability end, the result evaluation has found that the higher values of sensitivity and precision has helped in lowering the false classification rate and minimizing the error rate

The availability of computation resources in the proximity of individuals, avoidance of any unnecessary network communication delay to cloud subsystem, and availability

![img-6.jpeg](img-6.jpeg)

Fig. 7 Alert generation evaluation architecture
of the low latency and higher bandwidth in the fog-subsystem, as provided by the proposed system, has enabled the immediate alert generation from the edge of the network of the individuals and tended the reduced data volume transmission over the network for classification and subsequently led to lesser congestion and chances of error. On the other side, the higher value of sensitivity, precision and specificity has indicated the reliability of the generated alerts. The result comparison acknowledges the utility of the fog-based alert generation with improved average response time (or delay), better statistical measures, lesser error rates, and lower false-positive alerts.

# 4.4 Dengue cases prediction evaluation 

A prediction of impeding epidemics helps in enhancing the effectiveness of preventive measures against a disease. Hence, the presented system has employed autoregressive method-based and a weather-based approach for prediction of dengue cases. For the evaluation of dengue cases prediction, monthly data of mean temperature and cumulative rainfall and data about monthly dengue cases from 2011 to 2017 have been obtained from $[13,42]$ and the local civil hospital of the Gurdaspur district (of which, Pathankot city was a sub division), respectively. The past cases of infectious diseases influence the current and future cases. Hence, autoregression had been employed in R -studio to investigate the serial relationship between already occurred cases and currently occurring cases. The possible lag time using Autocorrelation function (ACF), Partial Autocorrelation Function (PACF) and prior information about cases, in RStudio, had depicted that the spikes were gradually decreasing in ACF analysis and cut off after 2nd spike in PACF analysis, suggesting a lag of 2 months. This was a

Table 11 Comparative analysis of alert generation component


strong indication of correlation between already occurred cases and currently occurring cases.

The data pattern depicted that the maximum rainfall occurred in the month of July and August, whereas the maximum mean temperature in May and minimum in January, of every year, and the Dengue incidence was mainly higher during SeptemberDecember, of every year. The analysis of the cross correlation had depicted the symmetrical sine wave around the zero line (between dengue cases and temperature) with 6 months per cycle. This symmetrical pattern is the evidence of stable and consistent relationship between the incidence of dengue and mean temperature. On the other side, the cross correlation between the dengue cases and cumulative rainfall had depicted asymmetric pattern with less consistent time cycles.

The analysis of the data had depicted that the dengue cases with 2 months serial relationship fits appropriate in the model. Further, the analysis of the model performance depicted that the weather time cycle of 5-6 months at the lag of 4 months performed with consistency, as compared to other time cycles and lag terms. The selected model had exhibited high prediction precision, consistent performance and lowest standardized root mean square error (SRMSE). The SRMSE of the selected model were 0.293 and 0.31 for period of 2011-2016 and 2017 respectively. The included weather time cycles for temperature and rainfall were 6 months and 5 months respectively in the selected model. Based on these parameter setting, the model has been fitted to predict the number of dengue cases from 2011 to 2017 and compared against the actual number of cases in that period, as shown in Fig. 8. The $\mathrm{R}^{2}$ of 0.853 depicts that the selected model explains the $85.3 \%$ variance in the monthly dengue cases. The time

![img-7.jpeg](img-7.jpeg)

Fig. 8 Dengue cases prediction
series of predicted cases against the actual cases exhibits a good performance of the selected model.

# 4.5 Information protection security analysis 

In the information protection component, the concept of granulation by dividing information into three-level: L-I, L-II, and L-III (as shown in Fig. 3) has been used to protect the sensitive or personal information of the registered individuals. Furthermore, the personal information present at L-I has been protected using secret sharing concept. The secret shares derived from L-I have also been stored at the secure servers. Hence, the proposed system protects the sensitive information of the individuals.

### 4.6 GPS-based risk assessment evaluation

The GPS-based risk assessment in the proposed system has been visualized over the ninth population-wise largest city of Punjab province in India i.e., Pathankot. The generated data of 1024 individuals' health records and 310 mosquito dense and mosquito breeding sites of the mapped area (a specific area of Pathankot) have been maintained into three different .csv formatted files, and utilized by the Netlogo [49] for creating the global SNA graph of DeV infection. There after, a Google API has been used to represent the SNA determined DeV infection risk on Google Maps, as shown in Fig. 9. The different colored hexagonal-shaped regions have depicted different DeV infection risk levels, as per mentioned in Table 4, where non-colored regions means there's no infected resident and infected visitor in that region, hence having no DeV infection risk in that non-colored region.

Figure 9a, b depicts the tracing of an individual's taken path without any knowledge of DeV infection risk on the underlying path, from a specific location to another specific location. Figure 9a depicts the tracing of the path followed, while Fig. 9b depicts the same tracing if it is represented on the risk-visualized map. The risk of catching the DeV infection has increased in this taken path as the path lies in the infected regions. However, once the risk-assessment is visualized on the map, it guides the individuals to

![img-8.jpeg](img-8.jpeg)

Fig. 9 GPS-based path routing a, b user's default routing and $\mathbf{c}, \mathbf{d}$ user's safe routing based on infection risk
re-route their path through safer regions. The same has happened in Fig. 9c, d, where, now the same individual has re-routed his path (which starts from the same source location to the destination location) because of the DeV infection risk visualization on map. In the proposed approach, an individual is free to opt any route, but because of the DeV infection risk visualization on map, an individual in Fig. 9c, d has taken an alternative route (suggested by Google map based on the distance in order of best to worst), so the route could be passed through safer regions in most of its distance. Here, the proposed approach has only visualized the DeV infection risk on the map, whereas the Google Maps has only suggested him the second best route, and the individual is person, who has taken that route, so he could travel to alternative route which has lesser risk of DeV infection and at the same time having shorter distance.

Figure 9c depicts the tracing of the safer taken path without risk assessment representation, while Fig. 9d depicts the same tracing on the risk map. The blue line in Fig. 9b traces the normal path, while the red line in Fig. 9d traces the re-routed safer path using Google Maps services. The GPS-based risk assessment visualizes the DeV infection risk in various regions in such a manner that one can plan his re-routed path in such a manner that the visits through infected areas can be avoided to much extent and exposure to infection can be minimized.

# 5 Conclusion 

A fog-based intelligent healthcare system has been proposed in this paper, which diagnoses the possible DeV infection of the individuals using Naive Bayesian Network and generates real-time diagnostic, suggestive, and emergency alerts to the concerned stakeholders (individuals, government agencies and health organizations). The proposed system aware and suggests the individuals diagnosed with possible DeV infection to medically confirm the incidence of the infection by consulting with the doctors and through proper recommended laboratory tests. The proposed system has utilized the environment event index (EEI) to ascertain the health sensitivity of the possibly infected individual with respect to the occurrence of undesired environmental events, and generate emergency alerts to the doctors or caregivers for taking timely remedial actions. The proposed system has also pinpointed the DeV infected and riskprone areas on Google Maps using SNA and provided efficient warning alert system for the visitors or residents in those areas. The system helps in preventing the further spread of DeV by alerting uninfected individuals and government healthcare agencies and aids in effective and precautionary control of the infection. The experimental evaluation of the proposed system has acknowledged the classification efficiency of NBN viz. highest sensitivity, precision, recall, and F-measure, as compared to the other employed classifiers, and utility of NBN in achieving better execution time. The evaluation has also acknowledged the utility of fog computing through the real-time functionality of the alert generation. The evaluation of the GPS-based risk assessment has depicted the efficiency of the proposed SNA-based warning alert system. The proposed system has a significant future scope in the domain of technology-based healthcare research, where common symptoms based disease monitoring platform can be developed using the current proposed system.

Acknowledgements We sincerely acknowledge the worthy efforts of Dr. Arvind Manchanda for providing his experiences and guidance in understanding the root causes of Dengue Virus (DeV) Infection outbreak, which has helped us in formulating the problem for our research and preparing DeV infection-related symptoms-based health data. At the same time, we also want to acknowledge the efforts of Dr. Pankaj Sood, who is actively working in various community-based healthcare projects, in arranging the consultation of various health professionals regarding our proposed approach.
