# Article 

## Quantitative Ground Risk Assessment for Urban Logistical Unmanned Aerial Vehicle (UAV) Based on Bayesian Network

Peng Han ${ }^{1, *}$, Xinyue Yang ${ }^{1}$, Yifei Zhao ${ }^{1}$, Xiangmin Guan ${ }^{2,3}$ and Shengjie Wang ${ }^{4}$

## check for updates

Citation: Han, P.; Yang, X.; Zhao, Y.; Guan, X.; Wang, S. Quantitative Ground Risk Assessment for Urban Logistical Unmanned Aerial Vehicle (UAV) Based on Bayesian Network. Sustainability 2022, 14, 5733. https:// doi.org/10.3390/su14095733

Academic Editors: Honghai Zhang, Xinglong Wang and Hao Liu

Received: 7 April 2022
Accepted: 7 May 2022
Published: 9 May 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Air Traffic Management, Civil Aviation University of China, Tianjin 300300, China; yangxinyueyangyuze@163.com (X.Y.); yifei6666@sina.com (Y.Z.)
2 Zhe Jiang Key Laboratory of General Aviation Operation Technology, Jiande 311612, China; guanxiangmin@caavc.cn
3 Department of General Aviation, Civil Aviation Management Institute of China, Beijing 100102, China
4 Key Laboratory of Flight Techniques and Flight Safety, Civil Aviation Administration of China (CAAC), Guanghan 300201, China; wangshengjie@caac.com

* Correspondence: han_peng_2007@126.com; Tel.: +86-18526646726

Abstract: The Unmanned Aerial Vehicle (UAV) has been used for the delivery of medical supplies in urban logistical distribution, due to its ability to reduce human contact during the global fight against COVID-19. However, due to the reliability of the UAV system and the complex and changeable operation scene and population distribution in the urban environment, a few ground-impact accidents have occurred and generated enormous risks to ground personnel. In order to reduce the risk of UAV ground-impact accidents in the urban logistical scene, failure causal factors, and failure modes were classified and summarized in the process of UAV operation based on the accumulated operation data of more than 20,000 flight hours. The risk assessment model based on the Bayesian network was built. According to the established network and the probability of failure causal factors, the probabilities of ground impact accidents and intermediate events under different working conditions were calculated, respectively. The posterior probability was carried out based on the network topology to deduce the main failure inducement of the accidents. Mitigation measures were established to achieve the equivalent safety level of manned aviation, aiming at the main causes of accidents. The results show that the safety risk of the UAV was reduced to $3.84 \times 10^{-8}$ under the action of risk-mitigation measures.

Keywords: urban logistical UAV; ground risk assessment; Bayesian networks; risk mitigation

## 1. Introduction

In recent years, UAVs have been successfully used in agriculture, forestry, plant protection, search and rescue, environmental monitoring, logistics, and other relevant fields [1,2]. The RAND Corporation, an internationally renowned consultancy, predicted that, by 2030, drones will replace more than $20 \%$ of ground logistical deliveries. The total takeoffs and landings would exceed to more than 3 million per day in a medium-sized city. However, at the same time, the safety risks caused by UAV ground-impact accidents are also increased gradually, posing a serious threat to the safety of ground personnel. Due to the complex structure of the UAV system, diverse operation scenarios, and strong dependence on navigation and communication infrastructure, it is necessary to comprehensively consider various internal system and external support system failures when evaluating UAV operation safety risks, bringing great challenges to its operation safety.

The operating risks are divided into mid-air collision and crash failure by Joint Authorities for Rulemaking on Unmanned Systems (JARUS) [3]. The interval between the aircrafts and the highest obstacles on the ground should always keep a distance of more than 600 m based on the regulation of the procedures of civil aviation flights over cities and nearby areas [4]. Thus, the probability of collision between urban logistical UAV and

civil aviation flights is low while operating $70-150 \mathrm{~m}$ above the ground. Therefore, before the number of drones in operation has reached a significant level, more attention should be paid to the failure problem of UAV and ground impact accidents when they fly over people in urban logistical scene at the present stage. This is also confirmed by existing statistics on historical safety accidents. A lot of research studies have been performed on UAV risk assessment. The existing literature could be summarized into two aspects. The first is the prediction of probability of ground impact accidents; this usually focuses on the reliability of UAV system. To solve this problem, existing studies assume one specific failure mode and failure probability of components [5,6]. Then a fault tree, event tree analysis, or Bayesian network [7-9] is adopted to determine the system reliability [10]. The Bayesian network plays a prominent role in the uncertainty and correlation analysis of a multifactor causal relationship [11]. Barr et al. [7] put forward the safety risk management strategy of UAV by using a Bayesian network based on the analysis of UAV crash and air collision accidents. Ancel et al. [8] used a Bayesian network to estimate the failure probability of UAV in the air traffic management system and evaluated the risks to ground personnel. James et al. [12] studied the risk of UAV integrating into national airspace due to communication link failure based on the Bayesian network. Kevorkian [9] used the fault tree method to analyze the failure causal factors of small fixed-wing UAV developed by Virginia Tech. The fault tree model was transformed into a Bayesian network model, and a quantitative evaluation of its failure probability was conducted. The second aspect is the evaluation of accidental severity which focuses on the impact of casualty rate of ground personnel. Weibel and Hansman [13,14] established the relationship between UAV crash injury criteria and the kinetic energy and proposed the empirical formula of casualty rate based on kinetic energy. Dalamagkidis [15,16] modified Weibel's casualty rate model according to its protective effect on human body. Based on these studies, some scholars put forward the research framework of UAV safety risk and mitigation [17,18].

# 1.1. Task and Operation Scenario of Urban Logistical UAV 

In order to evaluate the operation risk of urban logistical UAV, the task and operation scenario should be analyzed first. The task of urban logistical UAV is commodity distribution in the city and its nearby suburbs. Considering the impact of task attributes on the flight altitude, speed, and distribution distance, some typical type of urban logistical UAV, the operation scenarios, and risk categories were shown in Table 1. As shown in the table, multi-rotor UAVs are mainly used for urban logistical distribution with maximum takeoff weight between 15.5 and 37 kg . The payload weight is usually less than 5 kg . The distribution distance is within 15 km , and the flight altitude is generally less than 100 m . According to the proposed classification based on takeoff weight or risk of the aviation authorities and international organizations, urban logistical UAVs are generally small multi-rotor UAVs with medium risk. This specific type of UAV and its operation risk are seldom covered in the current literature. Additionally, as an important part of operation scenario, strong winds, heavy rains, and strong electromagnetic interference may happen unexpectedly and cause unexpected failure of the UAV system. Therefore, it is necessary to analyze the failure mode, failure causal factors, and probability based on the actual operation data of urban logistical UAV and carry out risk assessment and mitigation according to the characteristics, so as to reduce the safety risk to ground personnel below.

Table 1. Some typical type of urban logistical UAV, operation scenarios, and risk categories.


# 1.2. Incidents and Their Respective Failures History 

At the same time of rapid development, many public safety incidents have occurred in the flight of urban logical UAV. On January 2021, hundreds of UAVs crashed to the ground due to the failure of the main control computer during the formation flight in Chaotianmen square, Chongqing. On May 2020, in Hong Kong, a four-axis rotor UAV crashed out of control due to interference. On June 2019, in Yangzhou City, a four-axis rotor UAV crashed out of control due to an operation error. On May 2019, in Qingdao, the battery of a four-axis rotor UAV fell, causing the front windshield of the bus to be smashed. Compared with traditional transport aircraft and general-purpose aircraft, although UAVs are small in size, they have a large number, lower flight altitude and are close to the ground. Therefore, the risk of injury to ground personnel and property cannot be underestimated.

The above cases are summarized in Table 2.
Table 2. Typical incidents and their respective causes of urban logical UAV.


The above examples show that, during the rapid development of UAV, under the joint action of many adverse factors, such as UAV system failure, operator misoperation, electromagnetic interference, and bad weather, small rotor UAVs operating in cities have the risk of falling to the ground and injuring people and objects; this issue is worthy of special attention. From the cause and form of the accident, there are not only free falls after UAVs go completely out of control, but also dynamic impact caused by operator error, and re-crash after impact. At the same time, due to the flight close to the ground and close to the crowd, in addition to the general blunt damage, the rotating rotor will cause greater splitting damage to the human body. Although the above unsafe incidents are not caused by logistics UAVs, they are small rotor UAVs flying in cities. If they cannot ensure flight safety and reduce injuries to people and objects, it will undoubtedly be very unfavorable to industrial development.

Based on the operation data of about 20,000 flight hours and 100,000 takeoff and landings of urban logistical UAV accumulated in Hangzhou, this paper assessed the risk and mitigation of urban logistical UAV. This paper aims to analyze the factors affecting the safety of urban logical UAV, obtain effective risk-mitigation measures, and provide a safety barrier for UAV to integrate into low-altitude airspace. Starting from the processing of actual operation data, this paper constructs a quantitative risk assessment model and provides an application case in Hangzhou to provide theoretical support for UAV quantitative risk assessment. The contributions and highlights of this work are summarized as follows:
(1) Based on the accumulated operation data of UAVs in urban logistical scene and investigation of the ground impact incidents, failure causal factors and failure modes are classified and summarized.
(2) The risk assessment model based on the Bayesian network is built. The main risk sources affecting the operation safety of UAVs in urban scene are obtained respectively.
(3) Mitigation measures are established to achieve the equivalent safety level of manned aviation, aiming at the main causes of accidents.
Section 2 is the analysis of the failure causal factors of urban logistical UAV. Section 3 gives the failure assessment model and quantitative evaluation model. Section 4 gives the quantitative assessment of ground risk and discussions on results. Section 5 contains the conclusions.

The specific vocabularies used in this article are listed as follows. Operation risk defined as the risk of injury to third parties in the air or on the ground or damage to critical infrastructure on the ground while UAVs are operating in existing airspace. Groundimpact risk assessment defined as qualitative or quantitative assessment carried out on the possibility of UAV ground impact accidents and the harm degree of accidents and formulated reasonable risk-mitigation measures. Failure causal factor means factors which cause system failure in the operation of UAV. Casualty defined as the people sustaining injuries of a certain severity and over. The casualty rate is based on injury cases that required hospitalization or transfer to other facilities, such as trauma centers.

# 2. Causal Factors 

JARUS has published Guidelines on Specific Operations Risk (SORA). The risk identification method in the operation of UAV was also provided in the document. In the process of this study, the risk identification method recommended by SORA was used. Based on the operation data, the failure causal factors were classified into three categories: UAV system, operation environment, and human factors.

### 2.1. UAV System Failure

Take the logistical UAV which operated in Hangzhou as an example; the propulsion system and electronic devices are powered by lithium battery. Horizontal and vertical orientation is carried out through a GPS module and barometric altimeter. The delivery order for goods and planned distribution path are transmitted to the flight control system onboard wirelessly. The observer on the ground could monitor the flight status and take over flight control in case of emergency through the cloud connection control system. The rotors are driven by each motor, which provided a lift for the UAV and controlled the freedom of pitch, roll, and yaw. The goods were stored in the payload housing underneath the UAS. The process of takeoff and landing should rely on simple platform or the ground station. The landing targets on the ground were identified by the camera on board to ensure safe landing.

As shown in Figure 1, the typical structure of a UAV system includes a power system, electrical system, propulsion system, communication system, flight control system and relevant sensors, ground control system, and cargo loading devices [19]. Each system is composed of substructures and components. Any failure of the substructure may result in failure at the system level. According to the operation scene of urban logistical UAV and

the statistical results of operation data of relevant enterprises, the failure causal factors of UAV components were analyzed.
![img-0.jpeg](img-0.jpeg)

Figure 1. Typical structure of UAV system failures.
The operation data, including the UAVs data, operational data, and maintenance information, are recorded in each flight. The pre-flight data include flight plan, predicted track, and pilot qualification information. The in-flight data include UAV operation time, takeoff and landing points, actual track, flight video data, and data link command data. The post-flight data include maintenance records, fault records, fault cause analysis, and other texts. The data sets of BN analysis are taken from the record. The authors put emphasis on the fault records and the comparison of the predicted track and actual track. Based on this consideration, the authors had carried out work in the early stage to extract the UAV failure probability under different causal factors from the operation data. Firstly, the operation scenarios according to the records of meteorological conditions and operation environment of each task are classified. Then the failure probability, failure form, and flight time records under each scenario are counted. According to the flight mode and system structure, the statistical results obtained from the cumulative flight hours were summarized in the operation database for various equipment failures of UAV, as shown in Table 3.

# 2.2. Environment Causal Factors 

The environment causal factors are mainly related to the weather conditions, including strong gusts and torrential rain [20]. UAV operation would be greatly affected when the weather conditions exceeded the maximum indicator. A strong gust mainly leads to the change of flying altitude, which may cause the UAV to become out of control further. At the same time, the aircraft needs to use excessive power to maintain its altitude to fly in windy conditions, and this could lead to a crash. Torrential rain would mainly cause the short circuit of the electrical system and other electronic components of the UAV. Since it should be predetermined if the UAV should be sent out on a mission under bad environment weather, the probability of environment causal factors used here was conservative.

Table 3. UAV system failure causal factors and the description.


# 2.3. Human Factors 

The operation support personnel include drone pilots and maintenance personnel. Failures caused by the pilots fell into the following two categories [21]. The first was mistakenly touching the manual driving button which switched from autopilot flight mode to manual. Since the UAV was still under the control of the pilots at this time, it should be classified as a controlled flight into terrain. The second was human intervention error. The pilots failed to take over the drone or performed correction actions after equipment failure, which may result in a crash. Among these incidents, the statistical probability of pilots' mistakenly touching the manual driving button was about $2.1 \times 10^{-8}$, and the probability of human intervention error was about $7.2 \times 10^{-6}$.

Failure caused by ground maintenance personnel was mainly due to inspection or maintenance errors. The inspection or maintenance error could be divided into battery inspection error, rotor inspection error, motor inspection error, sensors inspection error, and so on. These errors would increase the risk of failure rate of corresponding components. Among them, frequency error of the remote-control equipment may lead to communication failure.

# 3. Methodology and Models 

### 3.1. Failure Assessment Model

### 3.1.1. UAV Failure Mode

Based on the statistical results of operation data and the existing literature [22], UAV failure modes could be classified into four categories: loss of control (LOC), unpremeditated descent scenario (UDS), controlled flight into terrain (CFIT), and dropped or jettisoned components (DOJCs). The detailed definitions of each failure mode are shown in Table 4.

Table 4. Common UAV failure modes.


### 3.1.2. Bayesian Network

The Bayesian network was suitable to solve complex joint probability distribution problem by breaking it into a series of relatively simpler factors through probabilistic reasoning. The difficulty of knowledge acquisition and uncertain reasoning problems could be reduced. Bayesian networks were based on Bayesian formulas in probability theory. The independent relation between variables was described by directed acyclic graphs based on network framework. A Bayesian network consists of a set of discrete nodes. There was a directed edge to describe the causal relationship between each two nodes. The edge pointed from the parent node to the child node. The Conditional Probability Table (CPT) was used to describe the probabilistic relationship. The conditional probability table for each node included all possible combinations of its parent nodes. The dependence of variables was described on their parent nodes with conditional probability distribution. The probability distribution and joint distribution attached to each variable could be calculated by the following formula [23].

$$
P\left(X_{1}, \cdots, X_{i}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

A Bayesian network can conduct qualitative and quantitative analysis at the same time; meanwhile, this algorithm can also be applied to the situation of high uncertainty in the absence of historical data. Moreover, the flexibility of causal relationship nodes in the network also suits for diversified configurations of different UAVs.

Based on the analysis of safety accidents of drones, the causal relationship of ground impact accidents was analyzed, and the networks between failure mode and causal factors were connected through a directed acyclic graph. Considering the causal factors and intermediate events, the Bayesian network of a UAV ground-impact accident is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Bayesian network of UAV ground-impact accident.
Based on the Bayesian topology network constructed in Figure 2 and the prior probability of causal factors in Table 2, the failure probability of various failure modes that can happen in the operation of the logistical UAV without risk-mitigation measures was calculated, as shown in Table 5.

Table 5. The failure probability of different UAV failure modes.


# 3.2. Quantitative Evaluation Model 

In order to evaluate the hazard of a ground-impact accident, the safety of ground personnel was taken into account as the primary factor, and the casualties of ground-impact accident per flight hour was selected as the quantitative index by referring to the risk assessment standard of civil aviation. The casualties per flight hour were related to the number of ground population affected by the accident and the casualty rate of the accident, as shown in Formula (2).

$$
N_{f}=N_{e} \times P_{f}
$$

where $N_{f}$ refers to the casualties in the ground impact accident per flight hour; $P_{f}$ means the probability of casualties of the ground impact accident per flight hour; and $N_{e}$ refers to the number of ground population affected by the accident. The probability of casualties could be expressed as follows:

$$
P_{f}=P_{U} \times P_{h}
$$

where $P_{U}$ is the probability of ground impact accident per flight hour, and $P_{h}$ is the casualty rate. The number of ground population affected by the accident could be expressed as the product of the area affected by accident and the population density of this area. Formula (2) could be expressed as follows:

$$
N_{f}=A_{e} \rho P_{U} \times P_{h}
$$

where $A_{e}$ is the area affected by the accident, and $\rho$ is the population density of the region.
The casualty rate for the ground-impact accident was related to a few factors, such as operation speed, altitude, type of UAV (rotor or fixed wing), and the protection ability of ground shelter (such as buildings or trees). Considering the impact energy, shield protection

coefficient, and personnel injury threshold [7], the empirical formula of casualty rate is shown as follows [16]:

$$
P_{h}=\frac{1-k}{1-2 k+\sqrt{\frac{\pi}{\beta}\left[\frac{\beta}{E_{i}}\right]^{\frac{2}{P_{s}}}}
$$

where $P_{s}$ is the protection coefficient of ground shelter, its value range is $P_{s} \in(0, \infty)$, and the average value is $1 ; \alpha$ is the impact energy required for $50 \%$ casualty rate when $P_{s}=6$, and it could be valued as 100 kJ ; $\beta$ is the energy threshold of casualties when $P_{s}$ approaches 0 , and it is set as $34 \mathrm{~J} ; E_{i}$ is the kinetic energy of the UAV when the ground-impact accident occurs; and $k$ is the correction factor. As was shown in the following formula, 1.4 times of the maximum design speed was adopted as the estimated kinetic energy velocity.

$$
E_{i}=\frac{1}{2} m V_{i}^{2}=\frac{1}{2} m\left(1.4 * V_{o p}\right)^{2}
$$

where $m$ is the mass of UAV, and $V_{o p}$ is the maximum design speed.

# 4. Results and Discussion 

### 4.1. Calculation Parameters and Results

The design parameters of the selected urban logistical UAV for distribution tasks are shown in Table 6.

Table 6. UAV type and design parameters.


According to the above analysis, the population density and ground shelter were closely related to the operational risk. Combined with the actual flight data in operation, three representative mission scenarios were selected to describe the population density and ground shelter protection coefficient of each operation area, respectively, which are named as P1 to P3. The parameters of each scenario are shown in Table 7 [24]. The scenario P1 described the sparsely populated areas which selected the population density and shelter properties in rural areas as a template. Considering that high vegetation coverage could provide more protection to ground personnel, the protection coefficient was set to 6 . The scenario P2 described the densely populated areas when UAV carried out distribution tasks in urban suburbs. In this scene, the population density was higher, while the vegetation coverage was lower. The scenario P3 was in the population gathering area for logistical distribution tasks in urban commercial settlements. In this scene, the population density was very high, and the ground personnel were seldom protected by the shelter.

Table 7. Classification of task scenarios and the parameters.


According to the failure probability of the UAV system listed in Table 4, the casualty rate under three mission scenarios was calculated, respectively. Without risk-mitigation measures, the casualty rate of urban logistical UAV reached $6.2 \times 10^{-4}$. The European

Aviation Safety Agency (EASA) had proposed the Equivalent Safety Level Concept (ELS) in order to evaluate the operational risks of UAV, which required that the UAV system should not cause higher risks to the ground personnel than the corresponding manned aircraft [25]. At present, the risk of air transport was about $5.26 \times 10^{-7}$ for each takeoff and landing. The existing target level of safety criteria provided in the Federal Aviation Administration (FAA) System Safety guidelines is about $10^{-9}$. The calculated probability exceeded the acceptable safety risk threshold at present. Therefore, it was necessary to analyze the causes and intermediate events under different working conditions and set risk mitigations according to the accident development process.

# 4.2. Risk Mitigation 

The causal factors and probability of UAV failure were the basis and source of operation risk assessment [26,27]. The origin of injuries caused by UAV system failure was the failure of the UAV system. Due to the lack of research on the reliability of the UAV system and components, the operation data could only be used as the breakthrough point in the existing research process. The results could provide a basis for UAV risk mitigations.

### 4.2.1. Risk Analysis of Ground-Impact Accident

Based on the equivalent safety level, the failure rate of the UAV system for the scenario P3 should be less than $1.74 \times 10^{-6}$, which put forward high requirements for the reliability of UAV system. In order to formulate reasonable risk-mitigation measures, the development process of ground-impact accidents with different failure causal factors and the posterior probability of each failure causal factors were analyzed. Taking motor failure and communication link failure as examples, the accident probability and intermediate events were calculated, respectively. As shown in Figure 3, under the motor failure condition, the accident probability was $21.69 \%$. Among these factors, the highest probability was rotor failure and partial power loss, which were $99.98 \%$ and $92.18 \%$, respectively. Under the communication link failure condition, the accident probability was $22.14 \%$. The probability of human intervention failure took the highest position of intermediate accident ( $97.99 \%$ ). Stall and control failure followed closely. The results of these two conditions clearly demonstrated the occurrence probability of each intermediate event in the development process of different UAV accident causal factors to the ground-impact accident.
![img-2.jpeg](img-2.jpeg)

Figure 3. Probability of each intermediate event in motor-failure condition and communication-linkfailure condition: (a) motor-failure condition and (b) communication-link-failure condition.

The posterior probability of each intermediate event calculated according to the Bayesian network and conditional probability table is shown in Figure 4. As shown

in the figure, the probability of control failure and change of lift coefficient were $83.27 \%$ and $70.81 \%$, respectively, which ranked top two in the middle accident. The result indicated that these two circumstances were high incidences of ground-impact accident. The probabilities of human intervention, failure, stalling, or lost power followed behind.
![img-3.jpeg](img-3.jpeg)

Figure 4. Posterior probability distribution of intermediate events.
The probability of each accident factor is shown in Figure 5. Among them, low battery power, rotor failure, and battery failure were three major causal factors of the ground-impact accident. Communication link failure, motor failure, and inspection and maintenance failure were also major risk sources.
![img-4.jpeg](img-4.jpeg)

Figure 5. Probability distribution of accident causal factors.

# 4.2.2. Formulation and Effect of Risk-Mitigation Measures 

Based on the risk analysis results, risk-mitigation measures were respectively set for these four failure modes. The main idea of these measures was to increase the redundancy of equipment and reduce the risk caused by operation support personnel. The first mitigation was to equip the UAV with two independent power systems. In daily operation, the UAV was powered by the main power source. When the main power failed or was insufficient, the flight control system would automatically switch the power source to the standby power source and immediately executed the emergency return procedure to realize the seamless connection of the power system. This measure greatly reduced the failure probability of the UAV system in practical operation. Secondly, it stipulated that the support personnel must

carry out cross-inspection. For the key part of operation, two ground-support personnel jointly checked and signed. Although the operation efficiency was reduced to a certain extent, this measure also significantly reduced the failure probability of the UAV system caused by human error. Thirdly, the replacement cycle of equipment consumables such as rotors should be shortened to reduce the failure probability from the perspective of system reliability. Finally, in regard to the point of view of the operating environment, the weather information on ground stations was connected to ensure that the meteorological conditions within the coverage of the air route were suitable for UAV operation. According to the riskmitigation measures formulated according to the distribution of accident failure incentives, the probability of actual operational risk of logistical UAV decreased to $3.84 \times 10^{-8}$ based on statistical data.

# 5. Conclusions 

The tasks and environmental scenarios in the operation of urban logistical UAV were described. Failure causal factors and failure modes based on the operational data of actual logistical distribution were analyzed, and the risk assessment model was established based on the Bayesian network. According to the probability of the failure causal factors and the conditional probability, the probability of a UAV ground-impact accident was estimated. On this basis, casualties per flight hour were selected as the quantitative index to evaluate the severity of accidents. In order to reach the equivalent safety level of manned aviation, the causes of the accident were analyzed according to the Bayesian network, and the riskmitigation measures were implemented according to frequent events and causal factors. Among them, battery power shortage, partial rotor failure, and battery failure were the three main causes of ground-impact accidents, which provided a basis for the formulation of risk-mitigation measures. Under these risk-mitigation measures, the operational risk of the logistical UAV was reduced to $3.84 \times 10^{-8}$. In view of the ground personnel, safety was the primary risk of UAV operation; in the subsequent operation, it is still necessary to continuously carry out statistics and an analysis of the data and formulate relevant mitigation measures to reduce the probability of ground-impact accidents.

Author Contributions: Data curation, P.H., X.Y. and Y.Z.; formal analysis, P.H.; investigation, X.G.; resources, S.W.; writing-original draft, P.H. All authors have read and agreed to the published version of the manuscript.
Funding: This research was supported by the National Natural Science Foundation of China (National Natural Science Foundation of China, E52102419); Zhe Jiang Key laboratory of General Aviation Operation Technology (JDGA2020-8); and Key Laboratory of Flight Techniques and Flight Safety, CAAC (Open Fund of Key Laboratory of Flight Techniques and Flight Safety, CAAC, No. FZ2021KF17); Civil Aviation University of China (Talent scientific research startup fund of Civil Aviation University of China 2017QD09X).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data can be made available upon request.
Conflicts of Interest: The authors declare no conflict of interest.
