# Lawrence Berkeley National Laboratory LBL Publications 

Title
Using discrete Bayesian networks for diagnosing and isolating cross-level faults in HVAC systems

Permalink
https://escholarship.org/uc/item/7vb448mg

Authors
Chen, Yimin
Wen, Jin
Pradhan, Ojas
et al.

Publication Date
2022-12-01

DOI
10.1016/j.apenergy. 2022.120050

Copyright Information
This work is made available under the terms of a Creative Commons Attribution License, available at https://creativecommons.org/licenses/by/4.0/

Peer reviewed

# Using Discrete Bayesian Networks for Diagnosing and Isolating Cross-level Faults in HVAC Systems 

Yimin Chen ${ }^{\mathrm{a}, \mathrm{b}{ }^{\mathrm{a}}}$, Jin Wen ${ }^{\mathrm{b}}$, Ojas Pradhan ${ }^{\mathrm{b}}$, James Lo ${ }^{\mathrm{b}}$, Teresa Wu ${ }^{\mathrm{c}}$<br>${ }^{a}$ Building Technology and Urban Systems Division, Lawrence Berkeley National Laboratory, 1 Cyclotron Road, Berkeley, CA, 94720, USA<br>${ }^{\text {b }}$ Department of Civil, Architectural and Environmental Engineering, Drexel University 3141 Chestnut Street, Philadelphia, PA 19104, USA<br>${ }^{\text {c }}$ School of Computing, Informatics, and Decision Systems Engineering, Arizona State University PO Box 875906699 S. Mill Ave. Tempe AZ 85287, USA<br>* Corresponding author Email: YiminChen@lbl.gov


#### Abstract

Fault detection and diagnosis (FDD) technologies are critical to ensure satisfactory building performance, such as reducing energy wastes and negative impacts on occupant comfort and productivity. Existing FDD technologies mainly focus on component-level FDD solutions, which could lead to mis-diagnosis of cross-level faults in heating, ventilating, and air-conditioning (HVAC) systems. Cross-level faults are those faults that occur in one component or subsystem, but cause operational abnormalities in other components or subsystems, and result in a building level performance degradation. How to effectively diagnose the root cause of a cross-level fault is the focus of this study. This paper presents a novel discrete Bayesian Network (DisBN)-based method for diagnosing cross-level faults in an HVAC system commonly used in commercial buildings. A two-level DisBN structure model is developed in this study. The parameters used in the DisBN model are obtained either from expert knowledge or through machinelearning strategies from normal system operation data. Meanwhile, the probability parameters are discretized to incorporate the uncertainties associated with typical expert knowledge. Thus, the developed DisBN method addresses the challenges many other BN based FDD methods face, i.e., the lack of fault data for BN parameter training. The developed DisBN represents causal relationships between a fault and its cross-level system impacts (i.e., fault symptoms or fault indicators) by considering how fault impacts propagate across different levels in a HVAC system. A weather and schedule information-based Pattern Matching (WPM) method is employed to automatically create WPM baseline data sets for each incoming real time snapshot data from the building systems. Consequently, BN inference and real-time diagnostics are achieved by comparing incoming snapshot data and the WPM baseline data set. The proposed method is evaluated using experimental fault data collected in a campus building. Fault diagnosis results demonstrate that the WPM-DisBN method is effective at locating the root causes of cross-level faults in an HVAC system.


## Key words

HVAC system, cross-level fault, root cause fault diagnosis, discrete Bayesian Network, pattern matching


# 1 Introduction 

It is well recognized that significant energy waste and unsatisfactory indoor environments exist in commercial buildings due to malfunctioning sensors, components, and control systems in the Heating, Ventilation and Air conditioning (HVAC) systems[1]. Fault detection and diagnosis (FDD) technologies are hence some of the most critical technologies to ensure building performance, especially its energy efficiency. Studies and field practices have shown that $5 \%$ to $20 \%$ energy savings can be achieved by applying FDD solutions, followed by correction in HVAC systems in commercial buildings [2,3]. Furthermore, occupant comforts can be improved and equipment lifecycle can be extended by eliminating faults and malfunctions in HVAC systems [4-6].

HVAC systems in commercial buildings are becoming complicated. Various subsystems such as cooling/heating plant subsystems, primary air distribution subsystems, and terminal air distribution subsystems are often highly coupled. Impacts of a fault occurring in one equipment and subsystem may propagate and cause adverse effects across different equipment or subsystems [7,8]. When facing such faults, component-level FDD solutions may fail to effectively diagnose and locate the root cause of a cross-level fault. Here, a cross-level fault refers to a fault that causes effects in multiple subsystems, or might even trigger other faults. For example, a chiller supply water temperature sensor bias fault (e.g., sensor reading higher than actual temperature), which occurs in the chiller plant, would cause the cooling valve position in a downstream air handling unit (AHU) to be smaller than normal. A component-level FDD tool that only monitors the AHU might fail to locate the fault and generate false alarms such as a cooling coil valve fault or a supply air temperature sensor fault. Lin et al. reported that the false alarm rates ranged from $36 \%$ to $86 \%$ and the misdiagnosis rates ranged from $13 \%$ to $21 \%$, after evaluating two

commercial AHU FDD tools and one research-grade AHU FDD algorithm [58]. Consequently, the building facility staff could be overwhelmed, and hence ignore the outputs from the FDD tool if too many false alarms are generated. Moreover, operators or owners of small or medium-sized buildings often demand information on the overall operational performance of a building, which requires a focus on cross-level faults which often have building level impacts [9].

Recently, two studies investigated the detection of cross-level faults in an HVAC system. For example, Wu et al. developed a cross-level fault detection method [10]. In the study, a system level fault detection architecture for HVAC systems was constructed. Chen et al. proposed a whole building fault detection method [11]. In the study, a data-driven framework was developed to flag faults which caused significant abnormalities in multiple subsystems/equipment during system operation. Despite these studies, efficiently diagnosing and isolating the root cause of a cross-level fault remains a challenge. This is because a detailed and accurate reasoning process needs to be achieved to reason the root cause when various fault symptoms are observed.

Fault diagnosis for cross-level faults of such complex systems is even more challenging since the casual relationships of their direct and indirect impacts are very hard to be analyzed. Among existing fault diagnosis and isolation solutions, Bayesian Network (BN)-based methods have demonstrated efficacy due to their excellent ability to work under uncertainty and incomplete information [12]. When used for HVAC fault diagnostics, BNs have been reported to be successfully implemented for boiler, chiller, AHU, variable air volume (VAV) terminals, and other HVAC component fault diagnostics. For instance, Widarsson et al. developed a BN-based method based on the analysis of system mass-balances for early-warning for leakage in recovery boilers [13]. The probabilities obtained can help the operator to identify and isolate the boiler faults. An intelligent chiller FDD method by using a Bayesian belief network was developed by Zhao et al. [14]. In the study, a three-layer structure BN, which included the fault layer, fault symptoms layer and an additional information layer, was proposed to improve the diagnosis accuracy. In addition, two rules incorporating calculated posterior probabilities were used to isolate the fault root causes. Similarly, Zhao et al. proposed diagnostic BNs for diagnosing 28 faults in different components in AHUs. These diagnostic BNs were developed based on the existing knowledge of AHU fault patterns found in three AHU FDD projects as NIST 6964, ASHRAE project RP-1020 and RP-1312 [15,16]. Xiao et al. proposed a BNs-based strategy for diagnosing ten typical faults of VAV terminal units [17]. An evaluation of the proposed method based on a simulation platform demonstrated that the proposed BNs-based strategy could be used for both on-line and off-line FDD for VAV terminal units. Hu et al. proposed a Bayesian belief network to diagnose refrigerant charge faults in variable refrigerant flow air conditioning systems [18]. In this study, the network structure and the relative probability distribution for two types of faults (i.e., the refrigerant overcharge fault and refrigerant leakage fault) were obtained after a feature selection process by using expert knowledge and data mining. Najafi et al. proposed a diagnostic algorithm by integrating BNs and obtaining an estimation of the posterior distribution to find the closet system behavioral pattern [19]. Through this way, the diagnostic algorithm could be less dependent on model accuracy and more flexible with respect to measurement constraints. They demonstrated the effectiveness of such algorithms to diagnose AHU faults. Apart from using BNs for component-level fault diagnostics, Verbert et al. developed a model-based BN method to diagnose system-level HVAC faults [20]. In the study, interdependencies between different components were considered and the diagnostics were carried out continuously in all operating modes. However, the process of diagnostics model development is time consuming because of the diverse building characteristics and operating modes. Taal et al. developed a reference architecture which integrated energy diagnosis and FDD systems into a single framework [21]. In the architecture, four types of symptoms and three types of faults in HVAC systems were clearly identified. In addition, the development of the architecture can effectively employ the information obtained from the HVAC schematic diagrams, which are commonly used by HVAC system designers or control engineers. Hence, this architecture can significantly facilitate the development of the BN structure model at the system level or sub-system level. In other two articles [22,23], the authors further developed a 4S3F (four symptoms and three faults) method based on the generic reference architecture developed in [21] and demonstrated the effectiveness of the method in diagnosing faults in a thermal energy generation plant and an aquifer thermal energy storage system. However, the authors did not evaluate the effectiveness of the developed method in the cross-level systems (i.e., the primary cooling subsystems and the air distribution subsystem) in which the incorporation of fault symptoms into the BN model may be challenging. Moreover, some further research works, such as the development of fault identification model, the sensitivity analysis of the prior probability and conditional probability, and using real time building automation system (BAS) data to diagnose faults, need to be conducted to fully integrate the developed method into fault diagnostic solutions.

Researchers also attempted to integrate BNs with other strategies to address some issues (i.e., incomplete expert knowledge and high false alarm) that are often associated with BN methods. For instance, He et al. increased the performance of a BN classifier for chiller fault diagnosis by integrating the probabilistic boundary and site information into a BN classifier [24]. Through this way, both false alarm rate and missed detection rate could be decreased. Wang et al. fused the distance rejection (DR) and mutual-source non-sensor information (MI) into the BNs to lower the false alarm rate [25]. In this study, DR was firstly applied to the BN by transforming the chiller FDD problem into a single-class classification problem. An adjustable false alarm rate could be adjusted by tuning DR to lower the false alarm rate. Then, MI was employed to increase identification accuracy of new types of faults. Liu et al. employed a back-propagation (BP) neural network to impute the missing data and maximum likelihood estimation to obtain BN parameters. The parameter estimation under incomplete expert knowledge was developed based on BP neural networks and fuzzy set theory [26]. The developed method was employed to diagnose a solar assisted heat pump system with complete and incomplete symptoms.

Although the above-described research works have demonstrated the efficacy of BN-based diagnostics solutions, most approaches targeted at component-level fault diagnosis. From these studies, one can observe that there are two challenges faced by BN-based solutions: 1) develop BN structures that reflect the causal relationships in a system; and 2) obtain probability distributions such as the prior probability distributions and conditional probability table (CPT) for each node in the network [27,28]. Compared with component-level BN-based fault diagnosis tools described above, a BN-based method for diagnosing cross-level faults faces even steeper difficulties for both challenges. As described earlier, a cross-level fault causes direct and in-direct fault symptoms across multiple components and subsystems, all of which need to be included when developing a robust BN structure model. When a fault occurs, some components/subsystems which are more likely to be affected than others, should be reflected in the BN model.

This paper attempts to address the second challenge (i.e., difficulty of obtain probability distributions for BN nodes) by developing a discrete BN (DisBN) for diagnosing and isolating cross-level faults in a HVAC system. Unlike continuous BNs which use continuous probability distributions in each node of a the network, in a DisBN, the continuous variables are discretized to represent fuzzy events [29]. DisBNs have received increased attention in the recent years because of their ability to efficiently handle the parameter modeling in BNs, especially when obtaining parameters from expert knowledge and incomplete field data, and hence facilitate the analysis of complex systems in various areas of application [30]. Despite its promises, DisBN has not been well-studied for HVAC FDD applications. We have only found one study in the literature which employed discrete BNs for chiller fault diagnosis [31]. However, the developed method was component level FDD solution and was only applied to diagnose chiller faults. Moreover, the authors did not provide a parameter sensitivity test to prove the robustness of the method. To bridge this gap, this study integrates DisBN with several other machine learning strategies, such as a weather and schedule-based pattern matching (WPM) method developed in [11] and develops a novel fault diagnosis framework for cross-level fault isolation.

In summary, the contributions of this paper include:

1) A novel discrete BN framework, which works well with the uncertainties of expert knowledge and field data, is developed and integrated with other machine learning strategies, such as the WPM method. The developed framework reduces the complexity of the diagnostics model development, especially the parameters and hence is expected to minimize engineering efforts. Sensitivity studies are also conducted to understand how the discretized parameters may affect diagnosis accuracy.
2) The developed WPM-DisBN method is effective to diagnose and isolate the root cause of cross-level faults in complex HVAC systems. Consequently, the issue of false alarms which are commonly triggered by component-level FDD tools can be addressed.
3) The developed WPM-DisBN method is evaluated by operation data collected from a real commercial building to demonstrate the effectiveness of the proposed method in analyzing real world data.

In the following sections, this paper will firstly introduce the general process of using BNs for fault diagnosis, followed by the description of a DisBN. The development of the WPM-DisBN method is discussed in Section 3. Section 4 introduces the process to evaluate the performance of the developed WPN-DisBN method by using real building data with artificially injected faults. Finally, Section 5 provides the summary and conclusion of this work.

# 2 Bayesian Network for fault diagnosis 

### 2.1 Bayes theorem

The BN-based diagnostics method is based on Bayes theorem. In the Bayes theorem, a conditional probability is used to measure the probability of an event under the assumption that another event has occurred. If an event $A$ happens (here $A$ may represent a fault) when an event $B$ (here $B$ may represent a symptom) is known or assumed to have occurred, the probability of $A$ under the condition $B$ can be written as [32]:

$$
P(A \mid B)=\frac{P(A B)}{P(B)}=\frac{P(B \mid A) P(A)}{P(B)}
$$

where $\mathrm{P}(A B)$ is the joint probability of event $A$ and $B$, and $P(A B)=P(B) P(A \mid B)=P(A) P(B \mid A)$.
Supposing $A_{1}, A_{2}, \ldots, A_{n}$ are a set of random variables and satisfy: (a) $\sum_{i=1}^{n} A_{i}=S$, where S is the certain event; (b) they are mutually independent; and (c) $\mathrm{P}(\mathrm{Ai})>0, \mathrm{i}=1,2, \ldots, \mathrm{n}$, for any given event $B$, the following marginal probability can be obtained:

$$
P(\mathrm{~B})=\sum_{i=1}^{n} P\left(A_{i}\right) P\left(B \mid A_{i}\right)
$$

Through this way, Equation 1 can be re-written as:

$$
P\left(A_{i} \mid B\right)=\frac{P(A B)}{\sum_{i=1}^{n} P\left(A_{i}\right) P\left(B \mid A_{i}\right)}=\frac{P\left(B \mid A_{i}\right) P\left(A_{i}\right)}{\sum_{i=1}^{n} P\left(A_{i}\right) P\left(B \mid A_{i}\right)}
$$

A Bayesian inference is to find out the event caused from the effects of the event by calculating the posterior probability. Bayes theorem provides a way to calculate the posterior probability (left side in Equation 1) from the prior probabilities (right side in equation). The prior probability of variable $\boldsymbol{A}_{\boldsymbol{i}}\left(\boldsymbol{P}\left(\boldsymbol{A}_{\boldsymbol{i}}\right)\right)$ and the conditional probability of the variable B given $\boldsymbol{B}_{\boldsymbol{i}}\left(\boldsymbol{P}\left(\boldsymbol{B} \mid \boldsymbol{A}_{\boldsymbol{i}}\right)\right)$ firstly assigned through the existing knowledge of the problem which can be either some statistical results or the estimation from the experts in the field. Then, the posterior probability $\boldsymbol{P}\left(\boldsymbol{A}_{\boldsymbol{i}} \mid \boldsymbol{B}\right)$ can be calculated via Equation 3.

### 2.2 BN for fault diagnostics

BNs are a powerful tool to represent the knowledge and the inference under uncertainties. A probabilistic model which reveals the causal relations between faults and symptoms can be developed through BNs. Although, BNs have a similar structure with the faulty tree method which is used to develop a hierarchical rule-based method for HVAC system FDD [33], there is a conceptual difference between BN-based method and rule-based method as the latter usually employs a binary variable rule for inference, while a BN incorporates uncertainty by using the probability theory when reasoning. Therefore, the deterministic inference in rule-based method with ad-hoc manner which can lead under-responsiveness or over-responsiveness to evidence and possibly lead to an incorrect conclusion can be avoided by adding uncertainty factors in a BN [34].

Two primary elements, i.e., a structure model and a parameter model are often included when developing BNs. In a BN structure model, nodes and arcs are used to describe various events and corresponding causal relationships among events. Each node represents a variable which is assigned to a probability. Arcs are the direct reasoning connection between nodes. Once the BN structure model is defined, a BN parameter model for each node should be developed so that BN inference algorithms can use them to calculate the posterior probabilities. Both the structure model and the parameter model in BNs can be obtained through statistical learning and/or expert knowledge. In addition, the BNs can be updated after new knowledge on the system is obtained [12].

Figure 1 shows a simple BN structure model with four nodes and three arcs, which can be used for fault diagnosis. In the figure, nodes $\mathbf{F s}$ represent the faults, and nodes $\mathbf{E s}$ represent the symptoms (i.e., evidence) caused by the faults. Usually, each fault has two states which are faulty and fault free, and each fault symptom can have multiple states which are quantified by the conditional probabilities.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Simple representation of a BN model.

# 2.3 BN parameters 

Probability parameters of a BN reflect the quantitative relations among parent (fault) nodes and child (evidence) nodes. Usually, three probabilities, namely prior probabilities, conditional probabilities, and LEAK probabilities (which is only for Noisy-Max gate, see discussion later), need to be determined when developing a BN parameter model.

Prior probability, which represents the frequency of a fault event that may happen, needs to be assigned to the fault nodes.

Conditional probability is to measure the probability of a symptom event under the occurrence of a fault event. When developing a diagnostic BN, the conditional probability distributions for each evidence node are stored in the CPTs which reflect all possible combinations of states of fault nodes.

The construction of continuous Prior probability distribution and the Conditional probability distribution is the most difficult task for complex systems, as eliciting complete sets of probability values that reflect the coupled relationships among variables in a complex system requires extensive data or knowledge [35]. To address this challenge, DisBNs, which employ discrete values are widely employed for developing BN parameter models in a diversity of applications [36-38]. There are several ways to discretize probability distributions and develop DisBN models. A thorough review of efforts can be found in [30]. In this study, we employed a ranked node method [35] to construct the conditional probability table which provides the ranked levels for evidence nodes. This approach works well with the nature of expert knowledge elicitation, and avoids the need of obtaining complete sets of probability distribution for each node. Detailed descriptions of the construction will be illustrated in Section 3.3.

LEAK probability is a probability when a child node is having a value of 1 with all parent nodes having values of 0 . In a fault diagnosis application, LEAK probability represents the probability when an evidence node demonstrates an abnormal (faulty) state, yet there is no fault occurring.

The employment of LEAK probability is to address the challenge where the number of parameters for evidence nodes grows exponentially with the increasing number of fault nodes as the network structure becomes more complex. Studies showed that it is unreliable to directly generate the conditional probabilities for each state of the evidence node when there are more than four fault nodes [39]. For example, traditionally, when generating a conditional probability table of an evidence node, all of the possible combinations of states of its parent nodes (fault nodes) should be considered. If an evidence node is a Boolean state node which contains two states, and there are n parent nodes in which Boolean state is, then the parameters of a conditional probability table would have a size of $2^{n+1}$. In real practice, the development of such kinds of conditions will be highly challenging and time-consuming. Therefore, canonical models such as Noisy-OR gate and Noisy-Max gate which only require a few parameters become attractive when developing BN parameter models. The use of canonical models not only simplifies the construction of BNs and influences diagrams, but also can lead to more efficient computations [39]. In the NoisyOR gate, effect evidence Y (a binary random variable) is deduced by each cause event $X_{\mathrm{i}}$ (a binary random variable) which acts independently of the other cause events [40]. A Noisy-MAX gate is the extension of the Noisy-OR gate. In the Noisy-MAX gate, effect event variable Y has $n_{i}$ states and these states are ordered according to the effect strength. At the same time, every parent variable (cause event) $X_{i}$ has $n_{i}$ values. By this means, the number of parameters can be reduced from exponential to linear in the number of parent nodes.

Here in this study, Noisy-Max gates are adopted to develop the DisBN parameter model. Three assumptions should be made when employing Noisy-Max gates: 1) the child node and all its parents must be variables indicating the degree of presence of an anomaly; 2) each of the parent node must represent a cause that can produce the effect

(the child node) in the absence of the other causes; and 3) there may be no significant synergies among the causes [39].

# 3 Method description 

### 3.1 Outline of the method

The architecture of the proposed WPM-DisBN method is illustrated in Fig. 2. The method contains four major processes, which include one offline and three online processes: 1) development of DisBN structure and determination of parameters (off-line, as illustrated in Sections 3.2 and 3.3); 2) WPM baseline generation, DisBN LEAK probability generation, and DisBN update (on-line, as illustrated in Section 3.4); 3) evidence event generation, DisBN inference and posterior probability calculation (on-line, as illustrated in Sections 3.5), and 4) fault isolation (on-line, as illustrated in Sections 3.6).

In terms of the development of a BN structure and associated parameters, three methods are often employed as: 1) structure and parameters are purely learned from data without human knowledge interaction; 2) structure and parameters are identified based upon domain expert knowledge; and 3) structure and parameters are developed based on a combination of expert knowledge and data obtained from system operation [41]. Although there are limited studies [24,42] that use only simulated data to train a BN model for HVAC fault diagnosis, the challenge of getting real building operation data, which represent a HVAC system with faults under different weather/operation conditions, has limited the application of pure data-driven BN development in real world application.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Method architecture.

### 3.2 Development of the DisBN structure model

In this study, the DisBN structure model, which included a two-layer structure and various nodes, was developed based on physical analysis and domain expert knowledge. This is again because of the difficulty of collecting high-quality data from real building systems that contain sufficient information about potential faults for the DisBN model development. Although rules have been developed for component-level FDD solutions, such as

for AHUs [43,44], VAV terminal units [45,46] and chillers [14,33], there are few literature reporting rules of considering an entire HVAC system which includes multiple subsystems across different levels. Hence, before developing the DisBN structure model for cross-level faults, rules which represent various causal relations among faults and symptoms in different levels in a system were developed.

# 3.2.1 Determination of the structure layer 

During the development process, the first step is to determine the network layer according to the nature of the problem. Traditionally, a two-layer BN structure which includes a fault layer and a fault evidence layer is employed to develop the DisBN for fault diagnosis problems. Apart from the two-layer DisBN structure, more layers may be added to represent some specific system behaviors or to include additional information. For example, an additional information layer, which includes system operation maintenance information, was used to develop DisBN for chiller and AHU fault diagnosis [14-16]. In this study, we employed a two-layer structure to develop the DisBN for crosslevel faults diagnostics for its simplicity.

### 3.2.2 Determination of nodes

Network nodes are assigned to represent different variables through system rule mapping or knowledge representation. Two types of nodes, i.e., fault nodes and evidence nodes, are needed when developing a two-layer structure. The fault and evidence nodes are selected based on a specific fault diagnosis application

## i) Fault node

In this study, fault nodes represent fault root causes in one specific piece of component. For example, an AHU supply air temperature sensor bias fault (either positive bias or negative bias) represents a sensor bias fault occurring in one piece of supply air temperature sensor in an AHU, and hence is assigned to one fault node. The states of a fault node are divided into two states: faulty state and fault free state. Different from the component-level fault diagnosis described in [47], fault severity is considered as part of the definition of fault state to allow a more generalized fault diagnosis.

To illustrate the development process, nine fault root causes, which represent the nine cross-level faults implemented in the demonstration building, are summarized in Table 1. More details about these nine faults are also discussed in Table 1 and further described in Section 3.2.2. A total of ten fault nodes, which reflects those nine fault root causes in different components (e.g., the AHU supply air temperature sensor bias fault occurs in both AHU-1 and AHU-2, and hence is created as two fault nodes) in the HVAC system, are included in the BN structure model.

Table 1. Fault cause and fault node list.


# ii) Evidence node 

Evidence nodes represent observable fault symptoms. The establishment of a fault evidence node comes from expert knowledge and physical analysis of how a fault affects multiple components. Two sources, i.e., direct measurements and virtual measurements (combination of direct measurements), can serve as evidence nodes.

In this study, for the cross-level faults considered, a total of 11 types of evidence, which comes from various measurements in the HVAC system, are determined to develop 16 evidence nodes as illustrated in Table 2. Each evidence node represents one specific measurement or rules deduced from multiple measurements. For example, the measurement of the outdoor air damper position represents an outdoor air damper position evidence type, and is used to create two evidence nodes for both AHU-1 and AHU-2 respectively.
a) Evidence node: virtual measurement

Among these 16 evidence nodes, the CHW-Cooling node and VAV2-RHC-VLV node are virtual measurements as defined below.

CHW-Cooling node is the calculated chiller cooling load and can be obtained by:

$$
\text { cooling }=\dot{m} \times \mathrm{c}_{\mathrm{p}} \times\left(T_{\text {return }}-T_{\text {supply }}\right)
$$

where $\dot{m}$ is the chilled water flow rate, $\mathrm{c}_{\mathrm{p}}$ is specific heat of chilled water, $T_{\text {return }}$ and $T_{\text {supply }}$ are chilled water return temperature and supply temperature respectively.

The VAV2-RHC-VLV node is an averaged reheat coil valve position among all VAVs (referred to as RHCVLV) which are connected to the AHU-2. This evidence node is used when the system is operated in the winter or transitional season as some zones require more reheat water after an AHU2-OA-DMPR-Stuck-H fault occurs. The RHCVLV is calculated as:

$$
\mathrm{RHCVLV}=\frac{\sum_{\mathrm{i}=1}^{\mathrm{n}} P_{\text {eiv }, i}}{n}
$$

where $P_{\text {eiv, } i}$ is reheat coil valve position in the $i^{\text {th }}$ VAV terminal unit, and $n$ is the total number of VAV terminal units connected to the AHU-2.
b) Evidence node: Boolean measurement

It is noted that in this research, we did not include certain measurements, which are categorized as Boolean variables (e.g., the pump status, supply air fan status), into developing the evidence nodes. This is because under the current WPM-BN scheme, it is challenging to develop a baseline (when there is no fault) for Boolean type measurements. When the WPM baseline dataset is generated by using the WPM method for each snapshot window, a standard deviation of each measurement (evidence node) will be calculated and compared with the incoming snapshot data, so that the evidence is generated to trigger the BN inference. If a Boolean type evidence node is used, no standard deviation can be easily calculated from the WPM baseline for that node. There could be some alternative techniques to be developed in the future to overcome this challenge, and to increase the evidence node list.
c) Evidence node: Strong, Moderate and Weak evidence

In this study, the evidence nodes are categorized according to the coupling between the symptom represented by the evidence node and the associated fault condition. Three coupling levels, which are Strong Evidence, Moderate Evidence and Weak Evidence, are proposed in this study. A strong evidence node indicates that there is a very strong connection between the fault and the symptom reflected by this evidence node, i.e., when a fault occurs, there is a high probability that the symptom reflected by this evidence node would occur. For example, if a cooling coil valve software-override fault, that is at a higher-than-normal position (AHU2-OpF-CC-VLV-SWO-H), has occurred, the AHU supply air temperature will most likely be affected. Therefore, the AHU supply air temperature evidence node is categorized as strong evidence.

It is noted that due to different subsystem sizes, the same symptom can be set as different severity levels. For example, for the chilled water differential pressure sensor bias fault with positive bias (CHWS-DP-Bias-P), the cooling coil valve evidence node for AHU-1 cooling coil valve position (AHU1-CC-VLV) is a moderate evidence node, but the same evidence node for AHU-2 cooling coil valve position (AHU2-CC-VLV) is a strong evidence node. This is because the size of AHU-2 is much larger than the AHU-1. Hence, the fault impact on the AHU-2 caused by the CHWS-DP-Bias-P fault is expected to be more significant compared to the impact on the AHU-1.

When an evidence node is considered as a weak evidence node for a fault, it is suspected that the occurrence of the fault may not always (low probability) trigger the abnormality of this evidence node. An evidence node may also be considered as a weak evidence node if its abnormality is only triggered under certain weather or schedule conditions by the associated fault. For example, in winter and transitional seasons, the preheating coil valve for AHU-2 (AHU2-PreHC-VLV) evidence node is set as a weak evidence node when there is an outdoor damper stuck at higher-than-normal fault for AHU-2 (AHU2-OA-DMPR-Stuck-H) fault. This is because if the outdoor air temperature is above a threshold, the preheat coil valve of the AHU will not open to provide the preheat water when there is an AHU-OA-DMPR-Stuck-H fault. But on a cold weather day when the outdoor air temperature is very low, the fault impact may be very significant to generate symptoms.

Ideally, which category an evidence node belongs to should be determined based on collected building data, since the coupling relationship is often affected by system hierarchy and sizes. However, again, collecting enough data with well-labeled fault information is nearly impossible in a real building application. Hence the determination of the evidence node category is mostly done based on expert knowledge and physical analysis.

At each coupling level, the evidence node is further divided into three severity categories, each of which is assigned with a predefined conditional probability value. Details about how conditional probability values are determined are provided in Section 3.3.2.

Besides the evidence type, the evidence direction should also be determined. The evidence direction represents whether the measurement symptom is higher-than or lower-than the threshold of the baseline. If the symptom is higher than the threshold of the baseline, the evidence direction is set to be "Positive", and vice versa. A summary of evidence nodes and their categories is provided in Table 2. Directions and coupling level for evidence nodes are provided in Table 3.

Table 2. Fault evidence node list.


# 3.2.3 Description of the developed DisBN structure 

For the fault diagnostics considered in this study, a DisBN structure is generated based on the above discussions which are summarized in Table 3 (for summer season) and Table 4 (for winter and transitional season) respectively. Figure 3 demonstrates the developed DisBN structure model for the faults in the summer season, which is also summarized in Table 3. The fault nodes are color labeled to red. And the evidenced nodes are color labeled to yellow, blue and green to represent nodes in different levels (i.e., primary cooling subsystem and supply air subsystem) in the HVAC system.

In this study, GeNIe [48] BN tool developed by the Pittsburgh University is used to generate the DisBN structure which represents various levels in a HVAC system.
![img-2.jpeg](img-2.jpeg)

Fig. 3. BN structure model for fault diagnostics (summer season).

Table 3. List of causal relations (summer season).



Table 4. List of causal relations (winter and transitional season).


# 3.3 Development of parameter model 

There are two methods of generating prior or conditional probabilities: from expert knowledge or from the probabilistic analysis of historical data [17]. Here the historical data can be historical operational data, experimental data, or simulated data. Data-driven or machine learning techniques are often used to obtain the probabilities when they are determined from data. Obtaining the prior and conditional probability distributions is a major challenge when developing a BN for fault diagnostics in a building system. Although operational data that contain naturallyoccurred faults are easily obtained, ground truth data (such as service records) that confirms the root causes of these faults are very hard to obtain. Even if such data exist for a specific building system, the learned probabilities are often not scalable to other buildings and/or building systems due to the fact that each building system is very different from others. Similar reasons prevent learning these probability distributions easily from simulated data. Sections 3.3.1 and 3.3.2 describe how to use the DisBN method to obtain prior and conditional probabilities from literature and expert knowledge.

### 3.3.1 Determination of prior probabilities

As discussed earlier, there is a lack of understanding on how often faults occurred in a building system. In this study, the values that have been reported for component-level fault diagnosis [47] are adopted for the prior probability distribution. The prior probabilities should be updated when more system operation knowledge is available, or statistical analysis from historical operation data can reveal fault prevalence probabilities. In this research, the fault state is divided into faulty state and fault-free state. And initial prior probabilities for each fault node are assigned as 0.01 for faulty state and 0.99 as fault-free state as shown in Table 5. These values indicate that we believe that for each fault, there is only $1 \%$ probability for this fault to occur. Note that we intentionally keep all prior probability values to be the same for all faults since we do not have any information to individually customize them. However, the developed DisBN can handle individual prior probability for each fault, should such information be available.

Table 5. Prior probability for fault nodes.


# 3.3.2 Determination of conditional probabilities 

Due to the limitation of obtaining fault data and their root causes, obtaining a conditional probability distribution from fault data is unrealistic for a real building application. Obtaining accurate continuous values for condition probabilities from expert knowledge is very difficult as well since expert knowledge tends to be fuzzy. However, expert elicitation could provide a range of condition probability for a fault and its associated fault evidence in a discrete manner. Using the same example, when AHU outdoor air damper is stuck at a $100 \%$ open position in cooling mode (non-economizer), the fault symptoms include 1) mixed air temperature measurement has the same value as the outdoor air temperature measurement; and 2) AHU cooling coil valve has a position that is higher-than-normal (baseline) position. Based on physical system analysis, one can see that both of these two symptoms are strong symptoms, i.e., they most-likely would occur whenever the above-mentioned fault occurs.

Using ranked nodes method [35], a ranked fault evidence node list was developed as illustrated in Table 3 of Section 3.2.3. The list includes nine ranked fault evidence categories for three strength levels. A fault evidence node is firstly judged by whether it is strong evidence or not, based on expert elicitation and physical system analysis. If a fault evidence node is a strong evidence node, i.e., when a fault occurs, this evidence is most likely to occur, then its conditional probability is assigned to be $90 \%$. This indicates that we believe when a fault occurs, its strong evidence node has $90 \%$ of the probability to show abnormality. Moreover, we believe that out of these $90 \%$ abnormal situations, half of which ( $45 \%$ ) will yield a very severe fault symptom and the other half will yield a less severe fault symptom.

Using the same example as above, fault evidence node 1 (difference between mixed air and outdoor air temperatures) is strong evidence. Hence the conditional probability for it to be abnormal is 0.9 , out of which, a 0.45 conditional probability is assigned for this node to have a very severe fault symptom (very abnormal) and a 0.45 conditional probability is assigned for this node to have a severe fault symptom. A 0.1 conditional probability is assigned to this node for it to have a low severity (not abnormal) fault symptom. A similar treatment is used for the other two association levels, i.e., medium evidence nodes and weak evidence nodes, except that the probabilities for these nodes to have severe fault symptoms are smaller. Details are provided in Table 6. It is noted that the conditional probabilities in Table 6 can be updated when more knowledge is obtained during the system operation.

Table 6. CPT for evidence nodes.


The above-described discrete value framework method works well with the fuzziness of typical expert knowledge. In another word, there is generally an understanding of how severe, or likely, a fault symptom is associated with a fault, but the exact probability is very challenging to obtain from experiences. Of course, such rough handling of conditional probabilities will lead to uncertainties of posterior probabilities. Fortunately, the nature of fault diagnosis for HVAC and building systems makes it acceptable for such rough handling of conditional probabilities. A building operator is generally not sensitive to small changes of posterior probabilities. For example, $30 \%$ or $40 \%$ posterior probability does not provide meaningful difference for a building operator. The numerical value of posterior probabilities is often absurd for field operators. It is much more meaningful when discrete and descriptive fault isolation information is provided, such as, "There is a high probability (> $80 \%$ ) of outdoor air damper stuck fault". The proposed discrete value framework works well with such descriptive fault isolation information.

# 3.3.3 Determination of LEAK probabilities 

LEAK probability represents a probability of an evidence node to be abnormal when all parent fault nodes were absent (when no fault occurs). LEAK probabilities for each evidence node are obtained by determining the probabilities of outlier in the baseline data. An outlier is defined as:

$$
$$

where $\bar{x}$ is the mean of the data sequence, $\sigma$ is the standard deviation, and $t$ is the threshold.
In this study, two classes of threshold, i.e., "very high/very low" and "high/low" are used to describe outlines. For the "very high" class and "very low" class, $t$ is set to 3 , meaning that the absolute difference between the measured value and the mean value on a measurement is higher than three times of the standard deviation, then it belongs to the "very high/low" class. For the "high" class and "low" class, $t$ is set to 2 , i.e., the absolute difference between the measured value from the mean value on a measurement is higher than two times and lower than three times of the standard deviation.

Therefore, LEAK probability can be calculated as:

$$
\text { LEAK Probability }=\frac{\text { Number of outlier data sample }}{\text { Total number of baseline data sample }}
$$

Different from previous research in which the LEAK probabilities were needed to be manually preset and could not be updated, in this study, the calculation of LEAK probability can be automatically achieved and updated when the new baseline data set for each snapshot window is generated as illustrated in Section 3.4.

### 3.4 WPM method for baseline generation

In the development of data-driven fault diagnostics methods, one of the critical issues is to generate a baseline data set, to which the incoming snapshot data can be compared in order to detect abnormality. However, in a HVAC system in buildings, system operation is highly influenced by different internal and external conditions such as weather conditions, occupants, and electrical appliances. Therefore, it is critical to compare the incoming snapshot data with baseline data that have similar weather and internal load conditions. A dynamic baseline, which contains historical data under similar weather and internal load conditions, is desired for each incoming snapshot data. In this study, a weather and schedule information-based pattern matching (WPM) method, which has successfully been used for fault detection, is used to generate the WPM baseline data set [11, 56].

The WPM method essentially contains four major scenarios. First, the historical operation fault free dataset is created. Secondly, the weather information data from the historical dataset and the new incoming snapshot data are combined together to produce one time-series dataset. Thirdly, the weather information data is divided into $\boldsymbol{N}$ individual non-overlapping and equal-sized segments, i.e., data windows. Fourthly, the SAX time series method is used to search similar weather time series data from the historical database. The data windows are tagged using symbolic strings. Lastly, the system's operation window with the same symbolic strings are clustered to generate a WPM baseline dataset.

The WPM baseline data set serves two purposes as 1) update LEAK probabilities in the DisBN. When the WPM baseline dataset is generated for each snapshot window, the outliers in the baseline data are then counted by using the predefined thresholds. The LEAK probability distribution can be obtained through Equation 7. When the new snapshot window data is obtained, the LEAK probability distribution will be re-calculated and fed into the DisBN parameter model. The DisBN is updated accordingly; and 2) produce online system fault evidence.

### 3.5 Bayesian inference

In this Section, we illustrate how the evidence was generated to trigger BN inference in Section 3.5.1, and the Bayesian inference algorithm that was used in this study in Section 3.5.2. It is noted that the described Bayesian inference process can be used for both DisBNs and continuous BNs.

# 3.5.1 Evidence generation 

Fault evidence, which is referred to as a symptom caused by a fault, is employed to trigger BN inference. Fault symptoms are typically observed from two sources: 1) concurrent relationships among measurements. For example, when an outdoor damper is stuck at $100 \%$ open position, the mixed air temperature measurement is the same as the outdoor air temperature measurement, and is very different from the return air temperature measurement; and 2) historical relationship between current measurement and historical baseline. In such a case, symptoms are obtained by comparing the current value of a measurement with its baseline value. For example, another symptom of the outdoor damper stuck at $100 \%$ open position fault is that the cooling coil valve position may be higher than its baseline values under similar weather and internal conditions.

In this research, since a WPM baseline is dynamically generated for each snapshot window, it is much easier to adopt the second source, i.e., using historical relationship, to generate fault evidence. The evidence generation process is described as follows: for an incoming snapshot data window, a WPM baseline is generated by selecting historical baseline data that have similar weather conditions and time of the day. The standard deviation $\sigma$ is calculated while generating the WPM baseline. If the incoming snapshot measurement data is within the threshold, i.e., $1 \sigma$ (standard deviation) in this study, the snapshot data is considered as fault free. Window 3 of Fig. 4 demonstrates such a normal operation sample. If the incoming snapshot measurement data is higher than $1 \sigma$ but less than $2 \sigma$, the evidence node related to this measurement is considered as a moderate symptom ("severe" in Table 6) as demonstrated in window 1 of Fig. 4. If the incoming snapshot measurement data is higher than $2 \sigma$, the evidence node related to this measurement is considered as a strong symptom ("very severe" in Table 6) as demonstrated in window 2 of Fig. 4.

Detailed evidence coupling and severity levels are defined in Table 6.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Demonstration of evidence severity level.

### 3.5.2 Inference algorithm and posterior probability calculation

A Bayesian inference is to perform a backward inference i.e., find the most probable instance given the observed evidence [49], based on Bayes's theorem as shown in Equation 3. Different inference algorithms exist to implement inference, which include exact inference algorithms and approximate inference algorithms [32,50]. In exact inference algorithms, the exact probabilities of variables can be calculated. In approximate inference algorithms, the approximate probabilities of variables are calculated through statistical approaches [50]. Based on existing literature, the jSMILE tool [48] is used in this study to carry out the DisBN inference and calculate the posterior probability for each fault node. Here, we used the default algorithm i.e., Clustering Algorithm to perform the DisBN inference [48]. The clustering algorithm is an exact algorithm for belief updating and has an advantage in computation efficiency [48].

### 3.6 Development of isolation rules

After the posterior probability distribution is obtained via inference algorithms, fault isolation is performed by comparing the posterior probability values of each fault node. Usually, the fault node with the highest posterior probability given the evidence state is identified as the most possible cause of an abnormality. Therefore, after the BN inferences are completed, a ranking mechanism is employed on the posterior probabilities generated in fault nodes to determine the root cause.

In this study, posterior probabilities for each fault node are calculated when each incoming snapshot data sample is obtained. In this study, the data sample has a 5-minute sampling rate. The posterior probability for the entire faulty operation is calculated by:

$$
P_{a l l}(A)=\frac{\sum_{i=1}^{n} P_{i}(A)}{n}
$$

where $P_{a l l}(A)$ is calculated posterior probability during a period, $P_{i}(A)$ is the calculated posterior probability based on each incoming data sample, $n$ is the total number of samples in a period.

However, directly using the posterior to identify the root fault cause may generate errors because some faults have inherently higher prior probabilities, and there might exist simultaneous faults in the system. Therefore, a series of fault ranking/isolation rules have been developed to increase the accuracy and robustness of the fault diagnosis process [50]. Different rules have been developed for BN-based tools for different equipment fault diagnosis [15,17]. Usually, the maximum posterior probability method is used to diagnose and isolate a fault cause. For example, in the BN-based diagnosis approach for faults in chillers, two isolation rules based on the ranking of posterior probability of fault node were adopted to isolate the fault [14]. Cai et al. pointed that if there existed a larger difference between prior and posterior probability of a fault, there would be a higher possibility of the corresponding fault occurrence [51]. Additionally, they also mentioned that a fault diagnosis methodology using BN-based methods could only provide a probability distribution of a fault, but could not draw a deterministic diagnosis result.

This study focuses on a single fault scenario, not simultaneous multiple faults scenarios. A fault is isolated, i.e., identified as the root-cause for an abnormality, by the following two isolation rules:

1) the posterior probability of first ranking fault node $P_{\text {all }}(A)$ is higher than $15 \%$; and
2) the posterior probability of this fault node $P_{\text {all }}(A)$ is the highest among all fault nodes, and is $10 \%$ higher than the second-highest one.

# 4 Method evaluation 

Accuracy of the developed DisBN needs to be evaluated by comparing diagnosis results with ground truth [52]. Different methods including sensitivity analysis, conflict analysis, simulation and experimental research have been used in the literature to verify and validate fault diagnosis results. It is noted that, although, verification and validation procedure for fault diagnosis have been employed and reported in process control industry [51,53], aerospace industry [54], structure health monitoring [55] and so on, we did not find a systematic implementation of such procedure in BN-based building diagnosis studies. In this study, we verify and evaluate the developed DisBN model by examining the diagnosis results using data collected from a BAS of a real campus building.

### 4.1 Description of the test facility

In order to evaluate the developed WPM-DisBN fault diagnosis method, one campus building in Philadelphia, PA was chosen as the test building in this study. The building is a seven-story, 78,000 square-foot mixed use building. A typical VAV HVAC system which is commonly seen in medium-sized commercial buildings (including a water-cooled chiller subsystem, three VAV-AHU subsystems, and a hydronic heating subsystem) is installed in the building. Figure 5 illustrates the HVAC system configuration in the building. A BAS is employed to monitor the system operation, as well as collect and store operation data. Besides, measurements from an electric power meter that measures the whole building's electricity usage, weather station sensors (temperature sensor and relative humidity sensor) are also connected to the BAS. Outdoor air enthalpy information is not provided by the BAS, but is computed in this study by using the weather station temperature and relative humidity sensor measurements.

Outdoor air pressure is also collected through a weather information website (https://www.accuweather.com/) to calculate the outdoor enthalpy.
![img-4.jpeg](img-4.jpeg)

Fig. 5. HVAC system configuration in the building.

# 4.2 Description of the data set 

Data were collected at a 5-minute sample rate at the building by its BAS, and were manually analyzed and labeled into two data sets, i.e., "fault-free" data set and fault data set. A historical "fault-free" data set represents a baseline when the system operation was considered satisfied. In the "fault-free" data set, a total of 140 "fault-free" test days from Year 2016 to Year 2017 was used to serve as historical baseline data, which are used later to dynamically generate the WPM baseline.

Three types of faults, which included operator faults, primary cooling subsystem faults and supply air subsystem faults, were manually implemented in the test building. The faults were selected because each of them would cause fault symptoms across different components or subsystems, and hence are "cross-level" faults. Details about these manually implemented faults and the implementation process are described in [11,56]. Generally speaking, a fault was implemented by injecting/overriding control signals (e.g., when simulating actuator stuck faults, operator faults, software overriding faults, and schedule faults) or by modifying setpoint values (e.g., when simulating sensor bias faults). A manual process as described in was adopted to establish the ground truth to label fault cases [56]. This manual process compares key building measurements with their baseline values, similar to those in a manual commissioning process, to identify if one of the following four scenarios exists: 1) an artificially-implemented fault with expected fault symptoms; 2) naturally-occurred faults with expected fault symptoms; 3) an artificialimplemented fault and a naturally-occurred fault occurred simultaneously; and 4) an artificially-implemented fault without expected fault symptoms. After manually examining system operation, a total of fourteen fault cases, which include eleven manually implemented faults and three naturally-occurred cross-level fault cases through Year 2016 to Year 2017 (see Table 7), were used to evaluate the developed WPM-DisBN method.

Table 7. Whole building faults data set.



# 4.3 Method evaluation description 

For each fault case, the WPM-DisBN method was used to analyze the BAS data which had a 5-minute interval rate, as if the method was used for online FDD. The method evaluation was performed by analyzing the posterior probability distributions i.e., the calculated posterior probability for each fault node, during the entire faulty operation period as given in Equation 8.

### 4.3.1 Overall performance of the WPM-DisBN method

Among the total of fourteen cross-level fault test cases (including three naturally-occurred cross-level fault cases), root causes of eleven cases were successfully diagnosed and isolated by the WPM-DisBN method according to the predefined isolation rules described in Section 3.6.

Table 8 summarizes the diagnosis results which include the posterior probabilities of top three fault nodes. Cases are labeled as "diagnosed" if the artificially implemented (or naturally-occurred) fault is flagged to be the root fault cause based on the isolation rules. For the three cases that are labeled as "mis-diagnosed" cases, the root fault cause is among the top three faults, i.e., posterior probability values rank within the top three. Moreover, in two out of the three mis-diagnosed fault cases, the occurred fault is the fault that has the highest posterior probability. However, in these three mis-diagnosed cases, the second-highest posterior probability value of the fault is very close to the first-highest posterior probability, i.e., less than $10 \%$. This means that the WPM-DisBN method could not differentiate the two top root causes, according to the defined rules.

Table 8. Fault diagnosis result.


The following sections illustrate the details of one representative successful diagnosis case, as well as details and discussions on all mis-diagnosed cases. Notice that in the following sections, each evidence node's symptom

severity is firstly discussed. As illustrated in Section 3.5.1, for each evidence node, the incoming data sample (i.e., measurement from the BAS with a 5-minute sampling rate) is compared with its baseline value. Based on the comparison, the data sample is labeled as normal (within standard deviation $\sigma$ ); "positive high" or "negative low" (higher than $1 \sigma$ but less than $2 \sigma$ ); and "positive too high" or "negative too low" (higher than $2 \sigma$ ). The discussions on these fault symptoms lay the basis for the resulting fault ranking.

# 4.3.2 Example: successfully diagnosed case 

On July $11^{\text {th }}, 2017$, an outdoor air damper stuck fault (stuck at a higher than a normal position) was implemented at AHU-2. The outdoor air damper at AHU-2 was artificially stuck at $90 \%$ open position by overriding the corresponding control signal in the BAS from 10:00 to 20:01 on that day.

Using the BAS data, which has a 5-min sampling interval, a total of 120 data samples from each evidence node were collected during the fault implementation period, which is 10 hours (i.e., $600 \mathrm{~min}=120 \times 5 \mathrm{~min}$ ). According to the BN structure model described in Section 3.2.3, four evidence nodes (i.e., chilled water flow rate (CHWFlowrate), AHU2-CC-VLV, chilled water cooling supply (CHW-Cooling) and relation between AHU outdoor air temperature and mixed air temperature (AHU2-MAT-OAT)) were connected to this fault node. Figure 6 shows the distribution of data samples for each evidence node during the fault implementation period. From the Figure, it can be seen that significant numbers of samples were labeled as abnormal (i.e., positive high/too high or negative low) during the course of fault implementation. For example, for the CHW-Cooling evidence node (CHW cooling in the Figure), a total of 118 samples out of all 120 samples are observed to be either positive high or positive too high compared with the WPM baseline.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Distribution of data samples for each evidence node (July 11 ${ }^{\text {th }}, 2017$ )
Based on the developed BN model, during the period when the fault was implemented, the top three fault nodes with the highest average posterior probability values were AHU2-OA-DMPR-Stuck-H (55\%), chilled water supply temperature negative bias (CHWS-Temp-Bias-N) (21\%), and AHU2-SA-Temp-Bias-N (11\%) as in Fig. 7. According to the predefined fault isolation rule, AHU2-OA-DMPR-Stuck-H was diagnosed as the root cause. Hence, this fault case was judged as a successful diagnosed case. A time-series fault diagnosis result is provided in Fig. 8. It was observed that the posterior probability of the AHU2-OA-DMPR-Stuck-H fault node was significantly higher than the other two nodes with the second and third average posterior probabilities, during the entire period when the fault presented. Real time diagnosis could facilitate a building operator to quickly locate the cross-level fault which causes the system level operation abnormality.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Calculated average posterior probability results (July 11 ${ }^{\text {th }}, 2017$ )
![img-7.jpeg](img-7.jpeg)

Fig. 8. Time-series posterior probability result for top three fault nodes (July 11 ${ }^{\text {th }}, 2017$ )

# 4.3.3 Example: mis-diagnosed case 

On August $3^{\text {rd }}$, 2017, a chilled water supply temperature sensor negative bias (CHWS-Temp-Bias-N) at $1.7^{\circ} \mathrm{C}$ fault was implemented by adjusting the chilled water outlet temperature setpoint on the chiller control panel. The fault test period was from 10:00 to 21:27.

According to the BN structure model described in Section 3.2.3, this fault node was connected to five evidence nodes, i.e., chilled water return temperature (CHWR-Temp), CHW-Flowrate, AHU-1 cooling coil valve position (AHU1-CC-VLV), AHU-2 cooling coil valve position (AHU2-CC-VLV), and chilled water pump speed (CHWPump-Speed). Figure 9 demonstrates the distribution of data samples for each evidence node. A total of 138 data samples were collected during the fault implementation period which is 11 hours and 27 minutes, for the CHWRTemp, CHW-Flowrate, AHU1-CC-VLV and AHU2-CC-VLV nodes. In the CHW-Cooling evidence node, the numbers of data samples labeled as the "positive high" state and "positive too high" state are high, showing this evidence node presented a strong symptom during the fault period.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Distribution of data samples for each evidence node (August $3^{\text {rd }}, 2017$ ).
The top three diagnosed fault nodes generated from the developed DisBN model were: AHU2-OA-DMPR-Stuck-H (29\%), OpF-Chiller-Off (15\%) and CHWS-Temp-Bias-N (12\%) respectively. The ranked posterior probabilities for all fault nodes could be seen in Fig. 10. According to the fault isolation rule, this fault was labeled as a mis-diagnosed case. The time-series fault diagnosis result is presented in Fig. 11.

The reasons for the misdiagnosis of this fault are believed to be the follows:
i) Although some fault evidence was observed, the number of observed symptom samples was relatively small. For example, for the cooling coil valve position in AHU-2 (AHU2-CC-VLV) evidence node, the total number of data samples showing "positive high" and "positive too high" symptoms is 57 out of 138 samples.
ii) Based on expert knowledge and physical system analysis, some evidence nodes (i.e., the chilled water return temperature (CHWR-Temp) node) were set as weak evidence nodes, and hence were assigned to lower conditional probability values. Therefore, although strong abnormal symptoms are observed in this node, the posterior probability of the associated fault node may not generate a high value. The reason that the CHWR-Temp measurement was set as a weak evidence node for this fault is because when supply chilled water temperature is lower than normal (negative bias), the downstream cooling coil valves would be closed-down to reduce the chilled water flow rate as the cooling loads are not changed. As a result, the chilled water return temperature often does not vary significantly from their baseline values.
iii) Other evidence nodes (e.g., the cooling coil valve position in AHU-2 (AHU2-CC-VLV) node), which have shown strong abnormality, are also strong evidence nodes of other fault nodes (e.g., the AHU2-OA-DMPR-StuckH). Hence, the calculated posterior probability values of those fault nodes are also high. This weakens the isolation capability of the developed BN method.
iv) An evidence node, i.e., Chilled water pump speed (CHW-Pump-Speed-Pump-Speed, is expected to have a moderate fault symptom. Yet no fault symptom has been observed during the faulty operation. This is because the chilled water pump at the building is undersized. Therefore, the chilled water pump was always operated at full speed to provide the required cooling in the building during the summer season. Consequently, the fault did not cause any pump speed abnormalities (e.g., higher speed) compared with the baseline.

Overall speaking, the implemented fault has not caused strong symptoms on many evidence nodes as expected. The symptoms that have been observed could be contributed by some other faults. Hence, this fault is a difficult case to isolate, even using a manual analysis.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Calculated average posterior probability results (August 3rd, 2017)

![img-10.jpeg](img-10.jpeg)

Fig. 11. Time-series posterior probability result for top three fault nodes (August 3rd, 2017)

For the other two mis-diagnosed cases, similar situations were observed. For example, the AHU2-OpF-CCVLV-SWO-H fault and the AHU2-OA-DMPR-Stuck-H fault can cause very similar fault symptoms (e.g., higher cooling coil valve position and chilled water flow rate). Further, the AHU2-MAT-OAT and the CHW-Cooling evidence nodes did not present strong symptoms during the fault implementation period. Therefore, the calculated posterior probability distributions are closed to each other (i.e., 61% for the AHU2-OA-DMPR-Stuck-H fault and 60% for AHU2-OpF-CCVLV-SWO-H fault).

### 4.4 Sensitivity test

As described above, in this study, we adopted a ranked node DisBN method and hence did not assign an exact and continuous prior probability distribution for each fault cause, nor an exact and continuous conditional probability distribution for each causal relation between a fault cause and associated fault evidence. A discretized framework was used to categorize the conditional probability distribution by assigning the conditional probability value according to the fault severity. Such a framework is designed in response to the nature of the challenges for building fault diagnosis, i.e., lack of fault data, and also to the fact that an exact posterior probability is not meaningful for building operators as discussed in Section 3.3.2.

Since the prior and conditional probabilities are determined using expert knowledge in a discrete manner, it is of interest to examine how sensitive the diagnosis results/accuracy is to the values of these probability parameters. A sensitivity test is hence designed to examine the impacts of the probability parameters [57] on the output parameters.

(e.g., posterior probabilities), by implementing small perturbations on the numerical parameters (i.e., prior probabilities and conditional probabilities). If the diagnosis/isolation results are affected, i.e., \#1 the changes of posterior probability values significantly affect the ranking result, or \#2 the difference between posterior probability values, this indicates that the diagnosis/isolation results are sensitive to certain probability distributions in the evidence nodes, and hence the DisBN model is not very robust to diagnose some faults. Consequently, we would suggest more carefully assigning probability distributions to increase the robustness of the BN model.

# 4.4.1 Test on the prior probability distribution 

In this study, the prior probability distribution of each fault node was equally assigned to 0.99 for fault free state, and 0.01 for faulty state. In the sensitivity analysis, two more prior probability distribution sets were used to test the impact of this value on the calculated posterior probabilities of each fault cause. Table 9 summarizes the prior probability values used in the sensitivity test.

Table 9. Test on prior probability.


It is found that the average posterior probability of each fault node was changed after the prior probability was adjusted. Detailed test results are provided in Appendix I. The results indicate that posterior probability values of some fault nodes increased (e.g., AHU2-SA-Temp-Bias-N). While for others, the values decreased (e.g., AHU1-SA-Temp-Bias-N). However, the fault ranking results were not affected. In another word, the change of the value of prior probabilities would affect the exact value of posterior probabilities. Yet the impacts tend to affect all posterior probabilities in a uniformed way which lead to the same fault ranking results. Hence, for the prior probabilities that were tested, the diagnosis accuracy was not affected by their variations.

### 4.4.2 Test on the conditional probability distribution

The sensitivity tests on the conditional probability distribution are divided into two categories. In the first test category, the focus of the sensitivity test is on ranking. It is hence implemented by adjusting the conditional probability severity level of a selected evidence node (as shown in Table 6). For example, instead of assigning an evidence node to be a strong evidence node, it is assigned as a medium evidence node or a weak evidence node during the sensitivity test. In the second test category, the focus of the sensitivity test is on the parameter values. Consequently, the sensitivity test is performed by adjusting the conditional probability value (as shown in Table 6). For example, instead of using 0.45 for "Strong Evidence" nodes with "Very Severe" fault symptoms, the value is changed to be 0.5 .

As there are a total of sixteen evidence nodes in the DisBN structure model, and each evidence node may be connected to various fault nodes, the number of conditional probability distributions for each cause-effect relation (connection between fault node and evidence node) is tremendous. Therefore, it will be impossible to implement an exhaust sensitivity test over all connections and their corresponding conditional probability distributions. In this research, a simplified test procedure was designed to implement the sensitivity test on limited representative nodes. The node selection procedure is based on two considerations, i.e., 1) the number of connections between a fault node and its connected evidence nodes, and 2) the connection strength between a fault node and an evidence node. In each category, two extreme conditions are employed in the sensitivity test.

First, the number of evidence nodes connected to a fault node is considered. If there are many evidence nodes connecting to a fault node, this fault node is identified as a well-connected fault node. Observing the developed DisBN structure model, it is found that the highest number of evidence node connections a fault node has is nine. Therefore, these fault nodes (with nine connections, e.g., operator unoccupied earlier schedule fault, OpF-SchUnOcc) were labeled as well-connected fault nodes. On the contrary, the lowest number of evidence node connections of a fault node has is only four. Those fault nodes (e.g., FN-P-EV-S), were considered as poorlyconnected fault nodes. In the sensitivity test, both a well-connected fault node and a poorly-connected fault node were selected respectively. It is hypothesized that when a fault node is connected with many evidence nodes, the inaccuracy of some conditional probability values would not affect significantly on the fault diagnosis result. Yet,

for faults that only rely on a few evidence nodes, the accuracy of the conditional probabilities of those evidence nodes may have stronger impacts on the diagnosis accuracy.

Secondly, the connection strength between a fault node and an evidence node is considered. Again, the associations between an evidence node and a fault node are categorized into three types (i.e., strong evidence, moderate evidence, and weak evidence). These categories are used to determine conditional probabilities as described in Section 3.3.2. In the sensitivity test, both strong evidence and weak evidence nodes are considered for each fault node. Hence four sets of sensitivity tests are designed for evaluating the impact of conditional probabilities as illustrated in Table 10. The four test categories are:

- Well-connected fault node with strong evidence node (FN-G-EV-S);
- Well-connected fault node with weak evidence node (FN-G-EV-W);
- Poorly-connected fault node with strong evidence node (FN-P-EV-S);
- Poorly-connected fault node with weak evidence node (FN-P-EV-W).

Table 10. Illustration of test category.


Note: FN - fault node; G - well connected; EV - evidence node; S - strong evidence; P - poorly connected; W - weak evidence
In the FN-G-EV-S category, the conditional probability of the AHU2- SA-Temp node (a strong evidence), which is connected to the OpF-Sch-UnOcc fault node (well-connected), was selected for sensitivity evaluation. In the FN-G-EV-W category, the conditional probability of the CHW-Flowrate node (a moderate evidence), which is connected to the OpF-Sch-UnOcc fault node, was selected for sensitivity evaluation. In the FN-P-EV-S category, the conditional probability of the AHU2-CC-VLV node (a strong evidence), which is connected to the AHU2-OpF-CCVLV-SWO-H fault node (poorly-connected), was selected for sensitivity evaluation. In the FN-P-EV-W category, the conditional probability of the CHW-Flowrate node (a weak evidence), which is connected to AHU2-SA-TempBias-N fault node (poorly-connected), was selected for sensitivity evaluation. The BN node selection as described above is summarized in Table 11.

Table 11. Selected fault node and evidence node.


Detailed testing scenarios and results are discussed in the following Sections.

# 4.4.2.1. Test on ranking of the conditional probability severity level 

In this test, different test scenarios are designed according to the severity level of an evidence node. For example, if the evidence node is assigned to a "strong evidence" level in the base case, it will be changed to a "moderate evidence" level and "weak evidence" level respectively in the sensitivity test. All test scenarios are summarized in Table 12.

Table 12. Test scenario on conditional probability severity level.


Examples of test results are summarized in Table 13. Observing these results, it is found that the severity level of an evidence node does affect the diagnosis accuracy. However, the impact depends on the evidence connection strength. If a fault node is well-connected (with more evidence nodes), the posterior probability of the diagnosed

fault is not affected significantly if only one or two connecting evidence node's severity level is changed. However, if a fault node is poorly-connected (with fewer evidence nodes), a change of an evidence node's severity level could significantly affect the calculated posterior probability value of this fault.

For example, the calculated posterior probability of the OpF-Sch-UnOcc fault node (a well-connected node) was not affected when the severity levels of the evidence nodes AHU2-SA-Temp and CHW-Flowrate were changed. As shown in Table 13, when the severity level of the AHU2-SA-Temp node was changed, the calculated posterior probability for the OpF-Sch-UnOcc fault node was maintained at $35 \%$, in the September $11^{\text {th }}, 2016$ test case for all scenarios. When the severity level of the AHU2-AHU-SA-Temp node was changed, the calculated posterior probability for the OpF-Sch-UnOcc fault node was maintained at $45 \%$ in the January $14^{\text {th }}, 2017$ test case for all scenarios.

However, the calculated posterior probability of the cooling coil valve software override too high in AHU-2 (AHU2-OpF-CC-VLV-SWO-H) fault node (a poorly-connected node) was significantly affected when the AHU2-CC-VLV evidence node was changed from being strong evidence to moderate evidence or weak evidence. The calculated posterior probability value dropped from $61 \%$ to $51 \%$ (set as a moderate evidence) and $29 \%$ (set as a weak evidence) respectively using data from August $11^{\text {th }} 2017$ as can be seen in Table 13.

Another example is the AHU-2 supply air temperature sensor negative bias (AHU2-SA-Temp-Bias-N) fault node (a poorly-connected node). When the conditional probability of the chilled water flow rate (CHW-Flowrate) evidence node was adjusted from being weak evidence to strong evidence or moderate evidence, the calculated posterior probability value of AHU2-SA-Temp-Bias-N fault node increased from $33 \%$ to $53 \%$ (set as a strong evidence) and $48 \%$ (set as a moderate evidence) respectively using data from August $08^{\text {th }} 2016$ as given in Table 13. This affected the diagnosis result, i.e., the rank \#1 fault will be changed to the AHU2-SA-Temp-Bias-N fault from the AHU1-SA-Temp-Bias-N fault.

Table 13. Conditional probability sensitivity test result.


From the test results, we can conclude that when a fault node is poorly-connected, the change of the evidence type may have significant impacts on the calculated posterior probability of a fault node, and consequently affect the diagnosis accuracy.

# 4.4.2.2. Test on the conditional probability values 

In this test, different test scenarios are designed to adjust the conditional probability values according to the severity level in each evidence strength category. This is implemented by adding or subtracting 0.05 from the base value for the "Very Severe" and "Severe" levels, and 0.1 for the "Low Severity" level. For example, if an evidence node belongs to the "Very Severe" level with a conditional probability of 0.45 as the base value, the conditional probability of this evidence node will have a value of 0.5 and 0.4 respectively during the sensitivity test. Different conditional probability values and test scenarios considered in this second sensitivity test are listed in Table 14 and Table 15, respectively.

Table 14. Conditional probability value setting.



Table 15. Test scenario on conditional probability value.


Examples of the test results are summarized in Table 16. Observing these results, it is found that the change of conditional probability values considered in the second sensitivity test has no significant impacts on the fault diagnosis result, although some calculated posterior probability values might be changed slightly. This illustrates that the minor change of conditional probability values in the same evidence strength scope does not have a strong impact on the diagnosis accuracy.

For example, the calculated posterior probabilities for the AHU2-SA-Temp-Bias-N (a poorly-connected node) fault node were slightly changed from $53 \%$ to $52 \%$ after the conditional probability values were adjusted to ConP Case 1. Similarly, for the OpF-Sch-UnOcc (a well-connected node) fault node (a well-connected node) was not changed after the conditional probability values were changed.

Table 16. Conditional probability sensitivity test result.

Temp evidence node changes) | $35 \%$ | $35 \%$ | $35 \%$  |
evidence node changes) | $45 \%$ | $45 \%$ | $45 \%$  |

Overall speaking, the sensitivity analysis results demonstrate that the developed DisBN model is robust to ensure the diagnosis/isolation accuracy.

# 4.5 Discussions

The proposed DisBN method demonstrates good capability to diagnose and locate several cross-level faults in an HVAC system that are studied in this paper. The sensitivity analysis shows that the robustness of the proposed method. In this section, we provide several discussions which navigate the potential improvement of the DisBNbased HVAC methods in the future.

### 4.5.1 Data-driven BN model development

In this study, both expert knowledge and the data-driven approach are utilized to develop the BN model. Expert knowledge was used to develop the BN structure model and part of the parameters (i.e., prior probabilities and conditional probabilities). A data-driven approach (i.e., the WPM method) was used to automatically generate the baseline data sets and calculate the LEAK probabilities. Although the proposed DisBN method significantly reduces the effort to determine certain parameters, much work is still needed to develop the entire BN model. Hence, research is needed to automate the process of determining the BN structure to enable a complete data-driven approach for the development of a BN model.

It is noted that the development of data-driven methods heavily relies on the collection of high-quality data and information. However, this may not be achievable with the current sensing and information management systems. For example, during the development of the DisBN parameter model, due to a lack of information about building fault frequency and impact in general, and due to the diversity of building design and systems, it is very hard to obtain accurate prior probability distributions for each fault, nor conditional probability distributions for each fault evidence. Hence, in this study, previous literature and expert knowledge were used to obtain prior probability and was set to be universal for all faults considered. At the same time, the conditional probability distributions were

discretized into several categorized levels. Again, domain knowledge was used to generate these distribution levels. More fault occurrence data from real buildings should be collected to provide more insights on the probability values. More sensitivity tests could also be conducted to further examine the robustness of the method. Meanwhile, the DisBN can also be updated when new information is obtained.

# 4.5.2 Fault diagnosability and diagnosis accuracy 

The proposed DisBN-based method is one of the evidence-based inference FDD techniques, in which the causal relations need to be explicitly determined. Consequently, the BN model contains a large number of causal relations and parameter settings, which can significantly affect fault diagnosability and diagnosis accuracy. In this study, 10 fault nodes associated with 9 unique cross-level faults in the HVAC system were used to evaluate the effectiveness of the proposed DisBN method. Through the sensitivity test, we found the BN structure model played a critical role to ensure the diagnosis accuracy. The diagnosability can be enhanced and diagnosis accuracy can be improved if key evidence nodes are included in the BN structure model. For example, the CHW-cooling evidence node presented strong symptoms when there was a chilled water supply temperature bias fault. Therefore, the inclusion of the CHW-cooling evidence node in the BN structure mode was expected to significantly improve the diagnosis accuracy. Meanwhile, some faults were associated with specific evidence nodes, which were not associated with other fault nodes. For example, the AHU2-OA-DMPR-Stuck-H fault node has two specific evidence nodes (i.e., the AHU2-PreHC-VLV node and the VAV2-RHC-VLV node) in the structure model. The inclusion of such specific evidence nodes would improve the fault diagnosability and diagnosis accuracy.

Additionally, although some faults shared the same evidence nodes, symptom directions on the evidence nodes might affect the diagnosis accuracy. For example, both the AHU damper stuck fault and the AHU cooling coil valve stuck fault affect the cooling coil valve position (i.e., the AHU-CC-VLV node) and chilled water flow rate (i.e., the CHW-Flowrate node). However, the symptom direction may be different. The AHU damper stuck at a higher position fault caused the positive symptoms on the AHU-CC-VLV node (i.e., the coil valve position control signal is higher than the normal position); nevertheless, the AHU cooling coil valve stuck at higher position fault caused the negative symptoms on the AHU-CC-VLV node (i.e., the coil valve position control signal is lower than the normal position. Therefore, accurately capturing the symptom direction in the BN model would improve diagnosis accuracy as well.

On the contrary, some faults in HVAC systems might be harder to diagnose because those faults did not have enough evidence nodes, or shared the same evidence nodes and similar symptom direction with other faults. For example, the AHU2-OpF-CC-VLV-SWO-H fault and the AHU2-OA-DMPR-Stuck fault shared three evidence nodes, and two of them have the same symptom direction and strength. This might cause the accurate diagnosis of the AHU2-OpF-CC-VLV-SWO-H fault to be harder. The diagnosis result showed that the difference of calculated posterior probabilities between both faults was only $1 \%$.

Therefore, the improvement of the diagnosis rate of BN-based methods requires systematic research on the relations between faults and symptoms (i.e., the causal relations and quantitative relations) despite the fact that many papers employed expert knowledge to develop BN models in the HVAC FDD area. Some papers were found to investigate the fault symptom characteristics for some specific types of HVAC equipment. For example, Chen et al. reported the fault symptom occurrence probabilities on fan coil units and illustrated that fault symptom occurrences and directions were significantly affected by operational conditions [59]. However, more research should be carried out on systematically evaluating fault symptoms and impacts on various measurements at either an equipment level or at a system level, so that relations between cross-level faults and corresponding symptoms in an HVAC system can be well established.

### 4.5.3 Diagnosis of simultaneous faults

In real practice, simultaneous faults can occur in real buildings. Symptoms from different faults could become complex when multiple faults occur at the same time. How to obtain ground truth of fault ranking when multiple faults exist needs to be explored. Although the WPM-DisBN method has demonstrated great potential to diagnose faults even when simultaneous faults exist, evaluating BN's output under the scenario of simultaneous faults remains to be explored in the future.

## 5 Conclusions

Cross-level faults in HVAC systems cause adverse impacts on multiple subsystems, or might even trigger other faults. Component-level fault diagnostics solutions may not effectively and accurately diagnose the root cause of such faults. Probabilistic-based FDD methods such as Bayesian networks have shown potentials to diagnose and locate fault root causes via various inference approaches. However, obtaining accurate and continuous parameters for a BN, which are essential to develop the diagnostics model is quite challenging. This obstacle becomes even worse when facing complicated HVAC systems and cross-level faults.

To address the above challenges, this paper presents a novel discrete BN (DisBN)-based method to diagnose HVAC system cross-level faults. The two-layer DisBN model, which consists of causal relations among various components and subsystems, well addresses the challenge of cross-level fault diagnostics within a complex HVAC system. A novel discrete value framework that works well with the uncertainty of expert knowledge and physical system analysis is used to determine the prior probabilities and conditional probabilities of a BN. In addition, the discretized parameters in the BN model reduce the complexity of the development process for complicated HVAC systems. The posterior probability of each fault node is computed and ranked through discrete BN inference. Sensitivity tests of the developed DisBN parameter model, especially the discrete value framework, show that the proposed method has a good robustness.

To achieve real-time BN update and diagnosis, a previously reported Weather and schedule information-based Pattern Matching (WPM) method is employed to generate a dynamic baseline data set which better represents system operation behaviors under different weather and internal load conditions. System operation evidence and LEAK probabilities distribution are generated by comparing current building behavior against the WPM baseline.

Multiple faults were artificially implemented in an HVAC system in a real campus building. BAS interval data collected during system's fault-free operation and faulty operation is used to evaluate the WPM-DisBN method. It shows that the developed WPM-DisBN method is effective at diagnosing and isolating the cross-level faults which cause impacts on multiple subsystems in an HVAC system. In addition, the evaluation based on the real building data also indicates the feasibility of the developed method.

# Declaration of Competing Interest 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Author Statement

Yimin Chen: Conceptualization, Methodology, Data curation and Writing-Original Draft
Jin Wen: Supervision, Conceptualization, Writing-Reviewing and Editing
Ojas Pradhan: Experiment implementation, Data collection and Data curation
James Lo: Writing-Reviewing and Editing
Teresa. Wu: Methodology advising and Writing-Reviewing

## Acknowledgements

Financial support provided by the U.S. Department of Energy for the research of VOLTTRON Compatible Whole Building Root-Fault Detection and Diagnosis (grant No. DE-FOA-0001167) is greatly appreciated. The authors would like to appreciate Mr. Bill Taylor, the campus facility manager of Drexel University, for his tremendous support in performing fault tests, as well as providing insights on HVAC system operation.

# Appendix I

Table 1 Prior probability sensitivity test

Bias-N | $61 \%$ | $68 \%$ | AHU1-SA-Temp-
Bias-N | $54 \%$ | $61 \%$ | Diagnosed  |
Bias-N | $35 \%$ | $35 \%$ | OpF-Sch-Occ | $9 \%$ | $9 \%$ | Diagnosed  |
Stuck-H | $24 \%$ | $24 \%$ | CHWS-Temp-Bias-
N | $16 \%$ | $14 \%$ | Diagnosed  |
Stuck-H | $39 \%$ | $41 \%$ | OpF-Sch-Unocc | $37 \%$ | $38 \%$ | Diagnosed  |
Stuck-H | $100 \%$ | $100 \%$ | OpF-Sch-Occ | $51 \%$ | $54 \%$ | OpF-Sch-Unocc | $10 \%$ | $11 \%$ | Diagnosed  |
Stuck-H | $100 \%$ | $100 \%$ | OpF-Sch-Occ | $35 \%$ | $43 \%$ | OpF-Sch-Unocc | $0 \%$ | $0 \%$ | Diagnosed  |
Stuck-H | $98 \%$ | $99 \%$ | OpF-Sch-Unocc | $50 \%$ | $55 \%$ | Misdiagnosed  |
Bias-N | $69 \%$ | $71 \%$ | CHWS-DP-Bias-P | $28 \%$ | $25 \%$ | Diagnosed  |
Stuck-H | $53 \%$ | $51 \%$ | CHWS-Temp-Bias-N | $18 \%$ | $18 \%$ | AHU2-SA-Temp-
Bias-N | $18 \%$ | $22 \%$ | Diagnosed  |
Stuck-H | $79 \%$ | $76 \%$ | CHWS-Temp-Bias-N | $17 \%$ | $16 \%$ | AHU2-OpF-CC-
VLV-SWO-H | $22 \%$ | $22 \%$ | Diagnosed  |
Stuck-H | $26 \%$ | $24 \%$ | OpF-Chiller-Off | $14 \%$ | $14 \%$ | CHWS-Temp-Bias-
N | $8 \%$ | $8 \%$ | Misdiagnosed  |
Stuck-H | $41 \%$ | $51 \%$ | CHWS-Temp-Bias-
N | $48 \%$ | $49 \%$ | Diagnosed  |
SWO-H | $49 \%$ | $46 \%$ | AHU2-OA-DMPR-
Stuck-H | $52 \%$ | $48 \%$ | CHWS-Temp-Bias-
N | $14 \%$ | $13 \%$ | Misdiagnosed  |
Bias-N | $72 \%$ | $49 \%$ | Diagnosed  |