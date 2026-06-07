# TUDelft 

Delft University of Technology

## An integrated resilience assessment methodology for emergency response systems based on multi-stage STAMP and dynamic Bayesian networks

An, Xu; Yin, Zhiming; Tong, Qi; Fang, Yiping; Yang, Ming; Yang, Qiaoqiao; Meng, Huixing

## DOI

10.1016/j.ress.2023.109445

## Publication date

2023

## Document Version

Final published version

## Published in

Reliability Engineering and System Safety

## Citation (APA)

An, X., Yin, Z., Tong, Q., Fang, Y., Yang, M., Yang, Q., \& Meng, H. (2023). An integrated resilience assessment methodology for emergency response systems based on multi-stage STAMP and dynamic Bayesian networks. Reliability Engineering and System Safety, 238, Article 109445.
https://doi.org/10.1016/j.ress.2023.109445

## Important note

To cite this publication, please use the final published version (if applicable).
Please check the document version above.

## Copyright

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons.

## Takedown policy

Please contact us and provide details if you believe this document breaches copyrights.
We will remove access to the work immediately and investigate your claim.

# Green Open Access added to TU Delft Institutional Repository 

'You share, we take care!' - Taverne project
https://www.openaccess.nl/en/you-share-we-take-care

Otherwise as indicated in the copyright section: the publisher is the copyright holder of this work and the author uses the Dutch legislation to make this work public.

# An integrated resilience assessment methodology for emergency response systems based on multi-stage STAMP and dynamic Bayesian networks 

Xu An ${ }^{\text {a }}$, Zhiming Yin ${ }^{\text {b }}$, Qi Tong ${ }^{\text {c }}$, Yiping Fang ${ }^{\text {d }}$, Ming Yang ${ }^{\text {e }}$, Qiaoqiao Yang ${ }^{\text {e }}$, Huixing Meng ${ }^{\text {a, }}$<br>${ }^{a}$ State Key Laboratory of Explosion Science and Technology, Beijing Institute of Technology, Beijing 100081, China<br>${ }^{\text {b }}$ CNOOC Research Institute Co. Ltd, Beijing, China<br>${ }^{c}$ Department of Civil and Systems Engineering, Johns Hopkins University, Baltimore, USA<br>${ }^{d}$ Laboratoire Génie Industriel, Contralelopélec, Université Paris-Saclay, 3 Rue Joliot-Curie, 91192 Gif-sur-Yvette Cedex, France<br>${ }^{e}$ Safety and Security Science Section, Department of Values, Technology, and Innovation, Faculty of Technology, Policy, and Management, Delft University of Technology, the Netherlands

## A R T I C L E I N F O

Keywords:
Emergency operations
Resilience assessment
Multi-stage STAMP
Dynamic Bayesian network

## A B S T R A C T

The interactions of external disruptions and technical-human-organizational factors in emergency operations are usually observed. Resilience assessment of emergency systems can improve emergency response capability and system functional recovery. The increasing complexity and coupling of factors in emergency response systems need to be investigated from a system resilience perspective. In this paper, we propose to integrate a multi-stage System-Theoretic Accident Model and Processes (STAMP) with a dynamic Bayesian network (DBN) for the resilience assessment of emergency response systems. In the proposed methodology, emergency response systems are viewed as multi-step emergency operations for STAMP to analyze the hierarchical control and feedback structures. The output of multi-stage STAMP in controllers, actuators, sensors, and controlled processes is applied to develop a DBN for resilience assessment. For known external shocks (e.g., natural disasters), the effects of external shocks on the system are decomposed into subsystems or components. System degradation and recovery models are established. Regarding unknown external disruption (e.g., unforeseen failure modes), degeneration and recovery are temporally integrated into the analysis of system functionality. System performance is evaluated through the combination of socio-technical factors and external disasters. Eventually, the resilience of emergency response systems is obtained from the performance curves. The results demonstrate that the proposed model can evaluate system resilience after the system suffers from external disasters.

## 1. Introduction

Emergency operations are usually vulnerable to external shocks [1]. During the post-disaster stage, emergency failures are characterized by frequent recurrence, strong derivatives, and secondary disasters that degenerate the safety status. This shows that emergency poses significant challenges to the operational efficiency and performance recovery of systems. The resilience-based emergency management emphasizes the response-ability of a system coping with risk and unexpected incidents. The system is able to cope, adapt and even achieve a new state of safety. To this aim, we define the resilience of the emergency system as the system performance to resist and recover from disasters in the process of multi-step emergency operations.

To meet increasing energy demand, deepwater oil and gas
exploration and production is highly advocated [2]. However, deepwater operations face challenges of harsh marine environments and complicated equipment [3]. Major accidents, such as a blowout in deepwater, lead to severe consequences including personal casualties, property losses, and environmental pollution [4,5]. For example, the Deepwater Horizon accident in the Gulf of Mexico, which is the largest oil spill disaster in offshore oil industry, caused 11 deaths and $7.79 \times 10^{5}$ $\mathrm{m}^{3}$ spilled oil [6]. The direct or indirect economic losses caused by disruptive events require effective emergency response and system recovery.

Emergency failure is prone to causing secondary injuries and extended destruction, after unexpected incidents. To manage the risk of emergency operations, risk evaluation in emergency techniques has been studied to develop emergency strategies. For instance, Meng et al.

[^0]
[^0]:    a Corresponding author.
    E-mail address: huixing.meng@bit.edu.cn (H. Meng).
    https://doi.org/10.1016/j.ress.2023.109445
    Received 11 March 2023; Received in revised form 25 April 2023; Accepted 11 June 2023
    Available online 16 June 2023
    0951-8320/© 2023 Elsevier Ltd. All rights reserved.

[7] investigated the operation of the oil recovery technique for deepwater blowouts. This study evaluated the risk of hydrate formation and obtained the operability envelope of the oil recovery technique. Wang and Gao [8] analyzed the recoil response of deepwater drilling risers and assessed the influence of drilling mud discharge on the recoil response. Cai et al. [9] proposed a quantitative risk assessment model of the installation process for deepwater oil and gas equipment based on fuzzy Bayesian networks (FBNs). Meng et al. [10] used a dynamic Bayesian network (DBN) for risk assessment of managed pressure drilling. These works provide support for decision-makers to identify crucial risks in emergency operations to prevent and control accidents.

However, risk assessment mainly focuses on analyzing known hazards during the pre-disruption stage and corresponding consequences [11,12]. Due to unknown emerging hazards and residual risk in the system, risk-based approaches are difficult to capture the change of system performance after a disruption. Therefore, more efforts need be devoted to transforming paradigms from risk-based strategies to resilience-based methods. Resilience assessment has been widely accepted in aerospace systems [13], energy systems [14], rail traffic [15], chemical process systems [16], and water transportation systems [17]. The application of resilience assessment to offshore and marine systems is also investigated. For instance, Wilkie and Galasso [18] proposed a methodology to evaluate offshore wind farm resilience by quantifying financial losses associated with offshore wind turbines. Ramadhani et al. [19] investigated offshore structure response to an ice load using a resilience assessment approach. Hu et al. [20] proposed marine liquefied natural gas (LNG) offloading systems' dynamic resilience model considering weather-related hazards. Above resilience assessment studies in offshore and marine systems provide a framework for probabilistically quantifying the emergency hazard impacts on the resilient emergency systems.

In emergency response systems, subsystems and components of emergency systems are highly coupled and interdependent [21]. Additional socio-technical factors (e.g., human error, equipment failure, and inadequate safety controls) and their interactions with undesired disasters (e.g., typhoons, earthquakes, and unknown disruption) make emergency response failure. Linear chain failure analysis can cope with relatively simple systems but cannot sufficiently deal with increasingly complex sociotechnical systems [22]. Conventional methods, such as fault tree (FT) and event tree (ET), are not feasible for the failure analysis of complex emergency systems since they have not considered dynamic interactions and feedback among subsystems or components [23]. Decision Making Trial and Evaluation Laboratory (DEMATEL) and System-Theoretic Accident Model and Processes (STAMP) are typical systematic structural modeling methods [24]. DEMATEL analyzes the cause-effect of accidents from the level of factors or the influence relationships among factors. DEMATEL needs to set thresholds relying on expert opinion or statistics to delete system redundancy information. Compared with DEMATEL, STAMP views the accidents generated by the possible degradation of system performance or complex interactions among components [22]. STAMP considers not only factor-level effects but also interactions among components. Consequently, STAMP has been extensively applied in complex systems.

STAMP method is able to analyze the accidents generated by the degradation of system performance or complex interactions among components [22]. Accordingly, STAMP has been widely accepted in complex systems. For example, Read et al. [25] utilized STAMP to identify hazards, loss scenarios, and risk insights for effective management and control of the rail transport system. Antonello et al. [26] used STAMP to qualitatively investigate the threats and hazards of nuclear batteries in structures and components. To create a flexible and resilient process after a disruption in complicated socio-technical systems, some system-theory-based analysis models are proposed to evaluate the resilience of systems. For example, Leveson [27] employed STAMP to analyze the resilience of the system in the safety culture of the NASA Space Shuttle program. Sun et al. [21] utilized STAMP to develop a quantitative resilience assessment model for chemical process systems. These studies demonstrate the advantage of STAMP in modeling component interaction and assessing performance alteration of complex systems. Considering the multi-state transition and dynamic changes of the system, DBN-based resilience assessment models are developed. For instance, Zhang et al. [28] proposed a resilience assessment model for subsea wellhead connectors regarding mechanical structure failure based on finite element models and DBN. Cai et al. [9] applied DBN and Markov process to establish external disaster models for resilience assessment regarding power supply and control systems of subsea blowout preventers (BOP). The aforementioned resilience assessment approaches demonstrate the performance change of particular systems. However, due to the dependencies, interactivity, and dynamics in engineering systems with their complex subsystem network, it is difficult to determine a resilience evaluation model and acquire to accurate resilience assessment results.

The interactions of undesired disruptions and technical-humanorganizational factors in emergency operations lead to significant difficulties and uncertainties when dealing with emergency scenarios. To achieve rapid emergency response with sound functions and coordination in subsystems or components, the emergency response system can be viewed as multi-stage emergency processes. We use STAMP to consider the information feedback and determine the crucial variables and root constraints of the system. The output of STAMP is applied to develop a DBN for the resilience assessment of emergency systems. Emergency decision-making process needs to be rapidly planned, coordinated, and commanded in a limited time. Introducing resilience into emergency response evaluation can learn emergency systems' adaptive and recovery capacity to undesired disruptions that appeared in emergency operations. Through the system resilience assessment, emergency schemes are optimized and emergency system performance is enhanced. To this end, we proposed a quantitative resilience assessment methodology based on STAMP and DBN.

The scientific contributions of this paper are summarized below. First, involving the complexity and interactivity of technical-humanorganizational elements in emergency systems, utilize systemic models to characterize the multi-stage emergency operations response mechanisms of emergency systems. We quantify the resilience of emergency systems in a dynamic manner based on multi-stage STAMP and DBN. Second, emergency systems are regarded as a multi-stage emergency process. The control structure and functional relationships in STAMP are mapped into DBN, enhancing risk-influencing factors (RIFs) identification and potential loss scenarios derivation. Third, due to the uncertainty of undesired shocks, known and unknown disruptions are identified in different resilience assessment models. Components failure, human and organizational factors, and undesired disruptions are considered in the resilience assessment. By changing the system redundancy configuration and key parameters, we can optimize the system resilience.

The remainder of this paper is organized as follows. Section 2 describes the methodology for constructing resilience assessment models based on STAMP and DBN. Section 3 is devoted to conducting a resilience assessment for emergency response systems, taking deepwater blowout emergencies as a case study. Section 4 discusses the design of the resilience assessment model, the construction of the STAMP-DBN model, and the optimization of the system resilience. Eventually, Section 5 concludes this paper.

## 2. Methodology

Emergency operations suffer from undesired shocks and technical-human-organizational failures. Their interactions result in severe consequences and secondary injuries. Due to the uncertainty of disruption or abnormal events in suddenness, propagation, and nonlinear amplification, it is necessary to possess the ability of flexible and resilient emergency response during pre-disruption and post-disruption stages.

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** The procedure for the development of the emergency system resilience assessment model.

Risk-based approaches aim to consider specific events and failure probability to achieve accurate probability estimates during a predisruption stage [29]. Compared with risk assessment, resilience evaluation is more suitable to handle emergency systems with unknown and uncertain disruptions. Such a method can resolve emerging threats and residue risks after a disruption to ensure the safety of emergency response systems. Thus, a proper resilience evaluation model is expected to enhance the emergency system's capability to withstand and recover from undesired disruptions. In this study, we propose a hybrid model integrating STAMP with DBN for the resilience assessment of emergency response systems. The methodology is illustrated in five steps (see Fig. 1).

- (1) Step one relates to disruption identification by establishing the types of disruptions, analyzing the main function of the system that would be affected by the disruption, clarifying the physical structure of the system, and understanding the dynamic behavior of the system.
- (2) Step two amounts to the construction of a STAMP model, including the decision-making context, safety requirements and constraints (SRCs), inappropriate control actions (ICAs), and causal factors of ICAs.
- (3) Step three regards the establishment of a DBN model. Integrating physical information with the STAMP model to develop a DBN model. We obtain prior probability and conditional probability table (CPT) through equation-based BN models, membership functions, and related references.
- (4) Step four refers to the system resilience assessment. The system performance is determined according to whether the external disturbance is identifiable. The performance variation of system components and the system resilience optimization is calculated. Three axioms are performed to verify the DBN model.
- (5) The final step is sensitivity analysis for the identification of the key influencing factors to resilience. The system can be optimized to a more resilient state through the recovery phase learning.

### 2.1. Disruption identification

Interdependency and interactions between subsystems and their components increase the opportunity for system module failure, which can lead to accidents. Such failure may randomly occur under undesired disruptions [30]. These disruptions are induced by known external shocks (e.g., natural disasters) and unknown unexpected hazards (e.g., unforeseen failure modes). After disruptions occur, system functions are

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** Basic control and feedback loop of STAMP.

affected either in malfunction states or impaired function states. These two states are regarded as low-performance states. When a system restores to its normal functional state, it will have high-performance states to ensure system operations. If the system is able to maintain a high-performance state or restore to a high-performance state from a low-performance state, it can be viewed as more resilient.

### 2.2. STAMP modeling

STAMP is based on control theory and systems theory. It is an effective technique to model a process system. STAMP was coined by Leveson [31] to investigate the complex socio-technological interactions of components or subsystems. In the STAMP model, system safety is regarded as a control issue from interactions among components rather than individual component failure. Such external interference, component failure, and abnormal interaction in complex systems are viewed as crucial causes resulting in an accident. To ensure system safety, it is advisable to conduct proper control and constraints on the coupling and interactions among different components.

STAMP provides hierarchical structures with multiple levels to identify and manage the safety design of human-machine control, and component interactions of the system. This method aims to identify risk-inducing factors and hazardous scenarios to prevent accidents. A STAMP model is established by three steps including safety constraint, hierarchical safety control structure (SCS), and process model [27]. A basic control and feedback loop of STAMP is shown in Fig. 2. The process of the STAMP model development is illustrated as below.

(i) The safety constraint is a basic concept of the STAMP model. Safety constraints are measures, which are imposed on a system to ensure safety. When accidents occur in the system, the safety constraints fail. That is, inappropriate control action (ICA) is regarded as a primary cause to lead to the emergence of hazards.

(ii) SCS constructs the framework of the STAMP model. The SCS includes four elements: controllers, actuators, sensors, and controlled processes. Controllers made automatedly or artificially utilize control algorithms to acquire information on the controlled process by sensor feedback. The actuator takes actions to control system states to ensure safety.

(iii) Controlled process establishes the hierarchical structure of a system. Control algorithms guide process models and variables to ensure the safety states of the controlled process. Through capturing the causal factors of ICAs, inadequate feedback, and poor execution, we can grasp the states and responsibilities of each entity of a system.

### 2.3. DBN modeling

Bayesian network (BN) is an inference-based probabilistic model that quantitatively describes causal relationships among variables. The structure of BN is a Directed Acyclic Graph (DAG) involving nodes, arcs, and conditional probability tables (CPTs). In the BN model, after acquiring the prior and conditional probability of nodes, the joint probability *P(U)* of a set of nodes *U*=(*X*1, *X*2, *X*3, ... *X*n) is computed [32]:

$$P(U) = \prod\_{i=1}^{n} P(X_i|Pa(X_i)) \tag{1}$$

where *Pa*(*X*i) indicates the parent nodes of node *Xi*.

Given new evidence *E*, posterior probability *P(U|E)* can be obtained by probability updating based on Bayes' theory [33]:

$$P(U|E) = \frac{P(U, E)}{P(E)} = \frac{P(U, E)}{\sum\_{i} P(U, E)} \tag{2}$$

By considering the uncertainty and variability of nodes over time, BN is extended as DBN with the temporal dimension to explicitly model the system dynamic changes based on the Markov process. A typical structure of DBN is demonstrated in Fig. 3.

In the DBN model, *X*1→*Z*<sup>t</sup> stands for the intra-slice arc, which shows the influences of different parent nodes on child nodes in the same time-slice *t*. *X*1→*X*t<sup>t−1</sup> and *Z*<sup>t</sup>→*Z*<sup>t+1</sup> are two inter-slice arcs, which represent the developing relations for the same nodes at successive time steps. Through giving a set of random variables *U*=(*X*1, *X*2, *X*3, ..., *X*n), the joint

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** The change process of DBN with different time slices.

Table 1 The CPT of a child node Z with three states given four parent nodes.


probability can be calculated [34]: $P\left(X_{1: T}\right)=\prod_{i=1}^{T} \prod_{i=1}^{N} P\left(X_{i}^{i} \mid P a\left(X_{i}^{i}\right)\right)$ where $X_{i}^{i}$ expresses the $i$ th node at time $t(i=1,2, \ldots, \mathrm{~N}), P a\left(X_{i}^{t}\right)$ is the parent node of $X_{i}^{t}$, and $T$ denotes the total time slice in DBN.

### 2.3.1. Conditional probability tables

Assuming that there are $n$ parent nodes $X_{1}, X_{2}, X_{3}, \ldots, X_{n}$ of the child node $Z$, the Noisy-OR function can be utilized to calculate the CPT of $Z$ [35]. $P\left(Z \mid X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right)=1-\prod_{1 \leq i \leq n}\left(1-p_{i}\right)$ where $p_{i}$ is the occurrence probability of $X_{n}$. For human error-causing system failure, it is difficult to determine human factor nodes' CPT when it has multi-state RIFs. In this paper, a membership function (MF) is introduced to map each state in the input space into a membership value between 0 and 1 [36]. Assuming that human factor node $Z$ has four parents. Each parent node includes three states: high, medium, and low, with corresponding numbers assigned as 2,1 , and 0 respectively. To obtain a numerical value for the child node, a global relative value $x(x \in[0,1])$ for the child node is determined: $x=\frac{\sum_{i=1}^{n} y_{i}}{\sum_{i=1}^{n} \max i}=\frac{\sum_{i=1}^{n} y_{i}}{n \cdot \max }$ where $x$ is the global relative value of the child node, $n$ denotes the number of parent nodes, $y_{i}$ stands for the value of the parent nodes' state $i$, max $i$ represents the maximum value of a parent node state $i$. To obtain CPTs of child nodes, three states are defined as $x^{2}, 2 x(1-x)$, and $(1-x)^{2}$. A set of continuous numbers is selected to assign parent nodes' states. The CPT of the child node $Z$ can be calculated by Eq. (5), as shown in Table 1. Notably, Table 1 provides partial results, and the total number of combinations is 81 (i.e., $3^{4}$ ).

### 2.3.2. Transition probability tables

By considering dynamic nodes' change over time in the DBN model, the Markov process is usually adopted to describe state transition relationships. Assuming that the current time is $t$, the time of the next step is $t+\triangle t$. Transition probabilities of dynamic nodes can be acquired by failure rate $(\lambda)$ and repair rate $(\mu)$ from related datasets and literature. This calculation process is expressed as follows [63]: $P\left(X_{i}^{t+\Delta t}=\right.$ no $\left.\mid X_{i}^{t}=\right.$ no $\left.)=e^{-\lambda \Delta t}\right)$ $P\left(X_{i}^{t+\Delta t}=\right.$ yes $\left.\mid X_{i}^{t}=\right.$ no $\left.)=1-e^{-\lambda \Delta t}\right)$ $P\left(X_{i}^{t+\Delta t}=\right.$ no $\left.\mid X_{i}^{t}=\right.$ yes $\left.)=1-e^{-\mu \Delta t}\right)$ $P\left(X_{i}^{t+\Delta t}=\right.$ yes $\left.\mid X_{i}^{t}=\right.$ yes $\left.)=e^{-\mu \Delta t}\right)$ where $P\left(X_{i}^{t+\Delta t}=\right.$ no $\left.\mid X_{i}^{t}=\right.$ no $\left.)\right)$ indicates the probability that $X_{i}^{t+\Delta t}$ is a working state given that $X_{i}^{t}$ is working. $P\left(X_{i}^{t+\Delta t}=\right.$ yes $\left.\mid X_{i}^{t}=\right.$ yes $\left.)\right)$ means the probability that $X_{i}^{t+\Delta t}$ is a failure state given that the state of $X_{i}^{t}$ is not working.

### 2.3.3. Construct DBN models

In this study, the DBN model is constructed based on the STAMP model. For the construction of DAG mapped from the hierarchical control structure, the following assumptions are made: (1) The controller is denoted as a combination of automation and human, which guides actuators and sensors to operate, monitor, and reflect on the controlled process. Thus, the controlled process failure is viewed as a critical factor to cause system accidents. It represents the last child node in the constructed BN model. (2) Based on relationships of physical structures, the directions of arcs are considered that lower-level element (e.g., components) is pointed to a higher-level element (e.g., a subsystem). RIFs of SCS are pointed to each element failure. (3) Actuators and monitors send controlled variables to the controlled process via corresponding sensors. Through information feedback, actuators take measures to protect the normal operation of controlled processes. Sensors transmit the signal to the controller again. Anomalies and failures in the controlled process can be detected and repaired. States of controllers, actuators, and sensors would affect the failure probability of the controlled process on the condition of their states [37].


Fig. 4. The mapping procedure from a control loop into a BN.

![img-3.jpeg](img-3.jpeg)

Fig. 5. The resilience concept curve of the emergency system.

Accordingly, the arcs in DBN point from the failures of controllers, actuators, and sensors to the emergency failure.

Based on the above assumptions, a DBN mapped from the control loop is shown in Fig. 4. Each element corresponds to a node. The controlled process is the child node. The directions of arcs regarding controllers, actuators, and sensors are pointed to the controlled process. In the control structure, controllers, sensors, and the controlled process of the control system are referred to as elements. These elements are mapped into BN as nodes. The arc represents appropriate relationships of components or subsystems in complex systems. RIFs of SCS are connected to each element failure by arcs. To quantify dependency relationships among node variables, each directed edge should be assigned CPTs.

### 2.4. Resilience assessment

Resilience indicates a system's ability to recover quickly after external disruptive situations [38]. By evaluating the system's resilience, the system's capability to resist disruption, absorb changes and restore to its initial state can be measured. Thus, resilience assessment is viewed as an effective method to manage system safety. In this study, various known external shocks with specific forms are mapped into DBN to develop a resilience assessment model, as shown in Fig. 5. *t*0-*t*1 phase represents the natural degradation of the system in pre-disruptions. Due to the aging effect of emergency equipment, the system performance reduces gradually from 100% to *P*1. *t*1-*t*2 indicates that the system is subjected to undesired disruptions and its ability to absorb the shock is gradually reduced. By the adaptation at the *t*2-*t*3 phase and external restoration at the *t*3-*t*4 phase, system performance is restored. The system performance is enhanced to the normal functional state through the system optimization at the *t*4-*t*5 phase.

The unknown external shocks are defined as a total disruption to construct a macroscopic resilience framework based on systems' resilience attributes including absorption, adaptation, restoration, and learning. Finally, according to the enhancement of the systems' adaptive ability and emergency response from accident retrospection and learning, optimization of the system can be achieved.

### 2.4.1. Known external shock

When a system is attacked by known external shocks, the impact level and effect location on systems cannot be established [39]. To reflect the influence of external disasters on systems, the change in failure probabilities of the system elements after disturbance is denoted as evaluation metrics. The resilience assessment is based on the performance change of the involved elements in systems. According to the change of component failure probability, a degradation model of the system subjected to external shocks is established. Integrating the recovery model, the system's resilience is evaluated.

When the system is attacked, the influence of external shocks on the components is decomposed into specific factors, such as pressure, temperature, and humidity [39]. The degradation under the external shocks amounts to that with the accelerated test of systems' components using the same failure mechanism. Based on the same failure mechanism, the acceleration model is mapped into BN to obtain the failure time of the system's components under external disruptions.

Suppose that the effect of an external shock on the system is decomposed into two factors *Y* and *Z*, the single degradation model of two factors *Y* and *Z* is shown as:

$$f_1(x) = f(y_1, y_2, \dots, y_i)$$

$$f_1(x) = f(z_1, z_2, \dots, z_i) \tag{10}$$

where *f*1(*x*) and *f*2(*x*) stand for the failure time of the system's components.

When a disruption impacts the system, the failure rate of the system's components will increase. For certain components without related failure rate data, Eqs. (10) to (12) are mapped into BN for acquiring failure time distribution and corresponding failure rate and probability. For components with initial failure rates, the failure rate of such nodes after disruptions can be determined by [40]:

![img-4.jpeg](img-4.jpeg)

**Fig. 6.** A generic resilience assessment framework.

![img-5.jpeg](img-5.jpeg)

**Fig. 7.** A DBN resilience assessment model based on Fig. 5.

$$\lambda_d = \omega_r \lambda_0 \tag{12}$$

where $\lambda_d$ stands for the failure rate of system components under disruption conditions, $\lambda_0$ denotes the initial failure rate of components, $\omega_r$ indicates the score of disruption.

Human performance plays a significant role in maintaining systems' normal operation and handling abnormal events [41]. When the system is subject to an external shock, operators' actions are affected by physical stress, complex operations, and environmental change [42]. To quantify the effect of human performance, a cognitive reliability and error analysis method (CREAM) is introduced to estimate human error probabilities, as shown in Eq. (14) adapted from [64].

$$HEP = HEP_r \cdot 10^{0.25\alpha} \cdot \psi \tag{13}$$

$$\beta = \sum_{i=1}^{n} \alpha_i \tag{14}$$

where $HEP$ indicates the final human error probability under disruption conditions, $HEP_i$ is the initial human error probability, and $\beta$ stands for the influence coefficients of external disruptions on human performance. $\alpha$ indicates the performance shaping factor under different performance conditions, which can be acquired from references [43,44]. $\psi$ represents the correction factor, which is acquired by experts.

### 2.4.2. Unknown external shock

System resilience in the event of an external disaster or shock is expressed as disturbance, absorption, adaptation, and restoration to ensure system safety. Thus, absorption, adaptation, restoration, and learning capabilities are regarded as four attributes of a system, which constitute the system resilience assessment framework, as shown in Fig. 6. In the proposed framework, absorption is viewed as an inherent ability of a system to resist and survive from a disruption. Adaptation refers to the capacity of a system to adapt itself to a disrupted situation. Restoration is the capability to restore with the involvement of external efforts. The system repairs itself from disruptive damages to a new normal state. Considering its uncertainties in the type, form, and intensity, external shock affecting the system is defined as a total disruption. Learning provides external effort action integrating accident experiences with prior information to respond to external disruptions. Finally, by evaluating the probability of system functionality state change, the system's resilience is measured.

#### (1) System functionality state

The DBN of resilience includes six nodes in which four nodes represent the states of functionalities (disruption, absorption, adaptation, and restoration), with a learning node, as shown in Fig. 6. In the DBN model, the system functionality state node is the child node with four states, and the rest represents the parent nodes with two states. To model the time-varying system functionality, four states of the child node are identified as corresponding to four functionalities state nodes. The transition relationships are shown in Fig. 7. Based on the Markov process, the transition rate of each state in the system functionality state (absorption, adaptation, restoration, and disruptions) is calculated as $\lambda_1$, $\lambda_2$, $\mu_0$, and $\mu_1$ [12]. This state transition and CPT are expressed in Fig. 8 and Fig. 9. It is worth noting that $\lambda$ and $\mu$ are assumed as parameters of the negative exponential distribution. $\lambda_1$ is computed by $1/MTBF$ (MTBF represents the mean time between failure at disruption conditions). $\lambda_2$ is calculated by $1/MTBF$ (MTBF represents the mean time at normal conditions). $\mu_1$ is obtained by $1/RT$ (RT is the time for self-repair). $\mu_2$ is acquired by $1/MTTR$ (MTTR stands for mean time to external repair).

Disruption, absorption, adaptation, and restoration are regarded as a dynamic process that affects system functionality. When the system is attacked by an external shock at time $t = 1$, the functionality state depends on its own state at time $t = 0$ and $t = 1$. The state transition can be calculated by transition probability. For example, the transition probability of state 1 to state 2 can be quantified by $\lambda_1$. Through self-response and external repair, the state of functionality can vary from State 1 to State 4, arriving at its initial stable state. To obtain more information to transfer the Markov chain model into the DBN, interested readers can read [65].

#### (2) Uncertainty of disruption

An external shock is regarded as a random event. It is only related to the state of the previous moment but not the state of the last moment [45]. Assume that this random variable is a counting process that obeys Poisson distribution and possesses two states (yes and no). Given that the average number of disruption occurrences per unit time is $\lambda$, the probability that disruption occurs $n$ times is [46]:

$$P\{N(t + \Delta t) - N(t) = n\} = e^{-\lambda t} \frac{(\lambda t)^n}{n!} \tag{15}$$

where $P$ represents the failure probability of random events, $\lambda$ stands for the number of failures per unit time, and $n$ is the total quantity of events failure in time $\Delta t$.

When disruption occurs $n$ times till $t$, the probability that disruption doesn't occur from $t$ to $t + \Delta t$ can be computed [47]:

![img-6.jpeg](img-6.jpeg)

**Fig. 8.** The Markov chain model illustrates translation relationships of system functionality states.

![img-7.jpeg](img-7.jpeg)

**Fig. 9.** The calculation process of transition rates based on the Markov chain [12].

$$\begin{aligned}
P(N(t + \Delta t) &= \text{no}|N(\text{t}) = \text{yes}) \\
&= \frac{P(N(\text{t}) = n, N(t + \Delta t) - N(t) = 0)}{P(N(t) = n)} \\
&= \frac{P(N(t) = n)P(N(t + \Delta t) - N(t) = 0)}{P(N(t) = n)} \\
&= \text{e}^{-\lambda Nt}
\end{aligned} \tag{16}$$

Assuming the present state of disruption is no, the occurrence probability of disruption at *t* + 1 can be obtained from [48]:

$$P(X_{t+1} = \text{yes}|X_t = \text{no}) = P(X_{t+1} = \text{yes}, X_{t+1} = \text{no}) = \lambda e^{-\lambda} \tag{17}$$

Similarly, other state transition probabilities can be calculated [48]:

$$P(X_{t+1} = \text{no}|X_t = \text{no}) = 1 - \lambda e^{-\lambda} \tag{18}$$

$$P(X_{t+1} = \text{no}|X_t = \text{yes}) = e^{-\lambda} \tag{19}$$

$$P(X_{t+1} = \text{yes}|X_t = \text{yes}) = 1 - e^{-\lambda} \tag{20}$$

where *P(Xt+1* = yes|*Xt* = no) stands for the probability that the disruption occurs (*Xt+1* = yes) at time *t* + 1 on the condition that it does not occur (*Xt* = no) at time *t*. Similarly, *P(Xt+1* = no|*Xt* = yes) is the probability that the disruption does not occur (*Xt+1* = no) at time *t* + 1 when it occurs (*Xt* = yes) at time *t*.

A DBN-based resilience assessment model can be verified by directly confirming the correctness of the DBN model [39]. Since model validation requires long-term monitoring of the used parameters, a three-axiom sensitivity analysis validation method is applied to partially validate the proposed resilience evaluation model. If the proposed model is reasonable, the sensitivity analysis for validation of the resilience assessment should reflect at least any one of the following three axioms [49]:

1. A slight increase/decrease in the prior probability of parent nodes can cause a corresponding increase/decrease in the posterior probability of child nodes.
2. The variation of probability distributions of parent nodes should keep a consistent influence magnitude to the child nodes' values.
3. Total impact magnitudes of the combination of probability variations from *m* attributes on the values should be always greater than that from the set of *m* − *n* (*n*∈*m*) attributes.

### 2.5. Sensitivity analysis

Sensitivity analysis aims to identify the crucial contributing factors to system resilience. By investigating the effect of small changes in numerical parameters (i.e., probabilities) on the output parameters (e.g., posterior probabilities), highly sensitive parameters that affect the reasoning results can be obtained. Based on the identified sensitive factors and their maximum range of variation, effective emergency measures can be generated to enhance the system's performance.

Many scholars have conducted a sensitivity analysis for the created model and acquired valuable results. For example, Tong et al. [12] determined the accurate parameter values for improving the estimation of the system's resilience based on sensitivity analysis. Yazdi et al. [50] conducted a sensitivity analysis to capture the critical parameters in the subsea system, and the contribution of parameters to the resilience variation was evaluated. For system modeling, more attention needs to be devoted to sensitivity analysis. This can help decision-makers identify the most critical factors in the system and provide some intervention actions for improvement.

Table 2
The CPT of running drill pipe failure with input X27, X28, and X29 connected in series.


## 3. Case study

The emergency operation of deepwater blowout accidents is widely regarded as a typical complex tech-social system in which multiple operation stages and various sector elements are involved. Tremendous difficulties and uncertainties arise when coping with emergency scenarios in a deepwater blowout accident. Lower Marine Riser Package (LMRP) cap is regarded as an efficient subsea oil collection technique, which can collect about $60 \%$ of the recovered oil from the wellhead (i.e., around $10 \%$ of the total spilled oil) [7]. The resilience assessment methodology is demonstrated using the LMRP emergency system. To manage emergency failure risks and enhance the system's resilience in the process of emergency operations, we proposed a hybrid model integrating STAMP with DBN to develop a resilience model.

This section is organized as follows. Firstly, we established the scenario of an assumed blowout accident emergency as a case study. Secondly, we applied STAMP to simulate the scene of multi-stage emergency operations in deepwater blowout accidents. Thirdly, we mapped STAMP into DBN to construct a risk assessment model for identifying RIFs of emergency operations. Fourth, general resilience evaluation models for emergency systems subjected to known and unknown external shocks are constructed. Finally, we utilized three axioms to verify the designed resilience assessment model and employed sensitivity analysis to determine the crucial factors of the system's resilience.

### 3.1. Disruption identification

Oil recovery operations are a multi-stage emergency operation process including lowering, installing, cutting emergency equipment, and inhibiting gas hydrate formation. The LMRP cap technique can be operated in three steps:
(1) In the running process of emergency equipment, the cap and diamond cutter is lowered onto the seabed. Based on the connected risers, a new LMRP of the rescue platform runs. The drill pipe then lifts up the cap.
(2) In the installation of emergency equipment, the riser of the former LMRP is cut off by diamond cutters. The cap is connected with the former LMRP. Riser assembly, drill pipe connection, and control valve installation are finished in this step.
(3) To prevent hydrate formation, hot seawater is injected into the annular space between the riser and drill pipe. Nitrogen $\left(\mathrm{N}_{2}\right)$ is pumped into the drill pipe to isolate seawater. Methanol $\left(\mathrm{CH}_{3} \mathrm{OH}\right)$ is filled into the cap [7].

In the working process, emergency systems are attacked by various known external shocks, such as typhoons, thunder, and earthquake. We decompose the impact of external disasters on the components of the system into specific physical characteristic factors. For example, the influencing factors are temperature and humidity when systems are influenced by earthquakes. Considering the uncertainty of undesired disruptions, unknown shocks are viewed as unforeseen failure modes. Such disruptions to the system are modeled to represent changes in the system's functional states.

### 3.2. STAMP modeling

A multi-stage STAMP model of the LMRP cap emergency operations is established by considering human factors, machine software, and equipment component, as shown in Fig. A1, Fig. A2, and Fig. A3. These models describe the responsibilities involved in human controllers, automated controllers, actuators, and sensors in emergency operations. The human controller includes emergency managers, drillers, and emergency workers. The automated controller consists of workstations and driller's computers. The actuator consists of emergency equipment and ROV. The sensor involves ROV, flowmeters, pressure and temperature sensors. These components are responsible for ensuring the controlled process is in line with the safety requirement. By determining the potential ICAs, the control and feedback loop among different components and process variables are identified.

Fig. A1 shows the running process of emergency equipment which is expressed in the STAMP model. Down arrows stand for control actions that enforce safety constraints to the level below. Up arrows indicate feedback information regarding whether the control actions are effectively implemented. For example, after a kick or a blowout occurs, lowering emergency equipment is executed first. When emergency workers send the command to the workstation, actuators began to lower diamond cutters, LMRP, riser, and drill pipe under the guidance of the ROV. Through the ROV feedback lowering process operations situations, human and automated controllers take corresponding measures.

Once the lowering of emergency equipment has been successfully deployed, emergency equipment began to be installed through the cutting operation. Fig. A2 represents the SCS of the installation and cutting system. The controllers include the operators (e.g., manager, driller, and worker), the controlled workstations, and computers. The actuators provide an emergency response to the installation of emergency equipment. ROV-based sensors pass the information on equipment installation status back and forth between controllers and actuators. For instance, human and automated controllers covey control commands, and then the actuator starts to conduct cutting operations by diamond cutters. The connection and installation of LMRP, riser, and drill pipe are finished. By providing feedback on emergency equipment connections and installations, the controller sends instructions to the actuator again to ensure the normal installation of emergency equipment.

Since the subsea environment is high-pressure and low-temperature, the risk of hydrate formation needs to be evaluated. Fig. A3 denotes the SCS of the hydrate formation. In the constructed STAMP model, operators are the highest-level controllers to manage the controlled process and the running state of the controlled computers. The human and automated controller sends a control command based on the current process model (hydrate layer pressure and temperature) to actuators (inhibitor injection and hot seawater circulation). The actuator then implements a controlled process to prevent hydrate formation. The completion of the controlled process is returned by the flowmeter, pressure, and temperature sensors. And the sensor transmits information about the controlled process to the controller and the actuator to operate again.

### 3.3. DBN modeling

### 3.3.1. Conditional probability tables

During the construction of DBN, the relationships from the parent nodes to the end child node via the intermediate nodes are determined by CPTs. When the input nodes are connected in series, the child node will fail in case of any node's failure. For example, when at least one of the input nodes X27, X28, and X29 occurs, the "running drill pipe" node will fail. The CPT of the intermediate node running drill pipe failure is shown in Table 2.

When the input nodes are connected in parallel, the child node will fail in case of all node failures. For instance, when input nodes "Workstation" and "Driller's computer" occurs, the "automated controller"

Table 3 The CPT of automated controller failure with input Workstation and Driller's computer connected in parallel.


node will fail. The CPT of the child node automated controller failure is demonstrated in Table 3.

Operators' errors sometimes do not directly lead to accidents. The relationships among the child node and input nodes may be neither parallel nor series. Thus, CPTs of human controllers are difficult to define due to the fuzzy uncertainties of human beings. We define the human controller failure node with three states (high, medium, and low) to indicate the probability of occurrence. CPT of this type of node can be determined by Eq. (5) and Table 1 in Section 2.3.

### 3.3.2. Transition probability tables

In this section, we utilize Eqs. (6) to (11) to calculate the transition probability of dynamic nodes. These reliability data ( $\lambda, \mu$ ) used in the DBN model were employed from the literature review and databases, as is shown in Table A1.

### 3.3.3. Construction of the DBN model

After the SCS of multi-stage emergency operations is established, we identify the ICAs from the control and feedback loop. Based on the RIFs in Fig. 10, Fig. 11, Fig. 12, and Table A1, a DBN model is constructed for emergency operations in deepwater blowout accidents considering natural degradation, as shown in Fig. 10. This model is built on GeNIe software. In the selection of dynamic nodes, not only dynamic characteristics but the availability of data sources need to be concerned. In this study, partial nodes are modeled as dynamic nodes because these nodes belong to the natural degradations effect and their reliability parameters $(\lambda$ and $\mu$ ) can be determined. Human factors and organizational factors are difficult to be described with quantitative failure parameters over time. The influence of these factors is instantaneous and they are

![img-8.jpeg](img-8.jpeg)

Fig. 10. Mapping multi-stage STAMP into DBN model for emergency failure.

![img-9.jpeg](img-9.jpeg)

Fig. 11. Mapping thunder model into BN (Left figure is adopted from [39]).

![img-10.jpeg](img-10.jpeg)

**Fig. 12.** A DBN model of system resilience assessment based on the known shock.

**Table 4** Parameters of equation (22) [39].


Consequently viewed as static nodes. Additionally, since the parameter data is unavailable, some nodes with dynamic behaviors are also considered static nodes. Thus, it is necessary to demonstrate how their changes over time can affect the system's performance. The DBN of emergency failure is generated by the failure of the lowering process, the failure of the installation and cutting process, and the hydrate formation. Each subsystem has three categories of causal factors, namely control systems (controllers), LMRP collection oil systems (actuators), and sensors. They are directly related to emergency failure and can be further connected by intermediate and root nodes.

Based on the established DBN model, we predict dynamic failure probabilities of emergency failure, the running failure of emergency equipment, the installation failure of emergency equipment, and hydrate formation within one month (30 days). On the 30th day, their failure probabilities are 2.002E−01, 3.264E−01, 3.068E−01, and 8.208E−02. When "the running failure of emergency equipment", "the installation failure of emergency equipment", and "hydrate formation" are set as evidence nodes, the emergency failure probability is changed as 7.793E−01, 6.524E−01, 6.702E−01, respectively. We conclude that the lowering failure of emergency equipment is a crucial factor leading to emergency failure. Compared with other stages, lowering operations spend more time, which can reduce risk in emergency operations.

### 3.4. Resilience assessment

#### 3.4.1. Known external shock

When external shock can be identified as specific disasters to affect system performance, we can map actual physical models to establish an external disaster model for resilience assessment. In this study, emergency system resilience is studied based on the assumed external disasters, namely, thunder.

When influenced by thunder, system components are affected by electrical stress. Failure time of the electronic component under electrical stress can be obtained by the inverse power law model in the engineering system [51]:

$$L = L_0 V^{-n} \tag{21}$$

where *L* is the failure time of the component, *L0* is a constant and is determined by the characteristics of the component, *n* is an index, and *V* is the electrical stress. These parameter values are demonstrated in Table 4. *L0* is the mean time to failure and its value is 100 h. *V* follows a normal distribution and its mean and variance are 5 and 0.8, respectively. *n* is 0.35, which represents the influence coefficient between component failure time and electrical stress.

Equations (22) and Table 4 are mapped into BN for acquiring the distribution of the failure time of the system component, as shown in Fig. 11. By multiplying the total of the intermediate value of the failure time period with the corresponding probability, the failure rate of the electronic components in the actuator under the influence of thunder is computed as 0.017.

For components with initial failure rates, it is assumed that external disruption can accelerate equipment degradation. Under the influence of thunder, the score of disruption *w_{i}* is determined as 2 by experts. The probability of human error in this condition is calculated, as shown in Table A2. We take X1 as an example to explain our approach. X1 (Poor emergency scheme) is viewed as a set of the inefficient adequacy of organization, inappropriate availability of procedures, and temporary

![img-11.jpeg](img-11.jpeg)

**Fig. 13.** System performance change under the influence of thunder.

![img-12.jpeg](img-12.jpeg)

**Fig. 14.** System performance is enhanced under different configurations.

![img-13.jpeg](img-13.jpeg)

**Fig. 15.** System performance is improved under different maintenance strategies.

inadequate available time. The probability of X1 can be obtained as: 2.50E-03 × (3.0×10<sup>0.25</sup>) × 2 = 2.81E-02.

According to the obtained parameters, the DBN model for system degradation and recovery is established in Fig. 12. The performance of the emergency system under the influence of the known external shock (thunder) is shown in Fig. 13. The result shows that performance decreases to 79.98% from 100% because of component degradation. Under the influence of thunder, system performance reduces from 79.98% to 29.87%. When the emergency system is repaired within 20 h after the disaster, the performance gradually increases to 69.40%. During the maintenance process, the system performance still declines slowly from 29.87% to 28.66%. By assuming physical relationships between system components and improving human reliability, the system performance is optimized, as shown in Fig. 14 and Fig. 15. The original configuration represents the initial configuration of the system. Configuration 1 is the parallel configuration among components of the automated controller in the lowering system. Configuration 2 is the parallel configuration among components of the automated controller in the installing system. Configuration 3 is the parallel configuration among components of the automated controller in hydrate formation.

In the automated controller failure process, X11, X12, and X13 are in parallel on the workstation failure and X14, X15, and X16 are also in parallel on the driller's computer failure. In Configuration 1, the system performance is improved by 11.92% from 69.40% to 77.67% when the

![img-14.jpeg](img-14.jpeg)

**Fig. 16.** A DBN model of system resilience assessment based on the unknown shock.

![img-15.jpeg](img-15.jpeg)

**Fig. 17.** The variation of states' probability based on the time-dependent.

Physical relations of workstation failure and the driller's computer failure are changed in lowering system failure. With the above-mentioned relationships in installation failure and hydrate formation being changed into a parallel, the performance is enhanced by 9.20% from 69.40% to 75.78% and 5.80% from 69.40% to 73.43% in Configuration 2 and Configuration 3. Based on the acquired results, the probability of risk factors is reduced by 10% leading to human controller failure in each subsystem. Strategy 1, 2, and 3 is the combination of changing automated controller configuration and human controller failure probabilities in different subsystems. Compared with only changing the logic relations among components, the combination of changing the physical relationship of components and reducing the probability of human error optimized the system performance by 12.84%, 9.71%, and 6.40% in Strategy 1, 2, and 3, respectively. Compared to the operational installation and hydrate formation phase, this can be explained by the lowering system is a key emergency stage with high influences of component structure and human factors. When the reliability of emergency operations in the running system is improved, the system performance can be quickly restored to the normal state for handling the blowout oil spill.

We conclude that system performance decreases rapidly when the systems are attacked by external shocks. After the system is repaired, the system performance noticeably increases, as shown in the performance curve of the 60–80 time slice of Figs. 13, 14, and 15. This can be explained by changing the redundant configuration of the system. The capability of the system to absorb external shocks can be improved. Maintenance strategies can enhance the system's repair rates. Consequently, the system performance significantly increases. Due to resource and technical response constraints in the repairing process, system performance is not fully restored to the previous state. Given the appropriate fix, the system can recover from low performance to higher performance or initial performance state. Changing the system structure and human error failure probability in the lowering operation enhances the system performance restoration.

### 3.4.2. Unknown external shock

When the system suffers an unknown external shock, a novel system resilience assessment model is developed, as shown in Fig. 15. The main contributing factors to the system functionality state include absorption, adaptation, restoration, and disruption. Absorption, adaptation, and restoration ability are determined by learning from the lowering, installation, and hydrate formation subsystem. We assume that conditional probabilities of learning node on nodes absorption, adaptation, and restoration are 0.4 from different subsystems. This system has lower

![img-16.jpeg](img-16.jpeg)

**Fig. 18.** The resilience assessment of emergency systems over time.

![img-17.jpeg](img-17.jpeg)

**Fig. 19.** System performance is improved under different repair strategies.

![img-18.jpeg](img-18.jpeg)

**Fig. 20.** System performance loss under different external shocks.

![img-19.jpeg](img-19.jpeg)

**Fig. 21.** System performance loss with the change of λ and μ.

![img-20.jpeg](img-20.jpeg)

**Fig. 22.** Time-dependent performance loss with the change of *λ* and *μ*.

![img-21.jpeg](img-21.jpeg)

**Fig. A1.** SCS of the running system.

adaptation and restoration abilities. The average number of external disruptions per unit time is assumed as 1 within one month (720 h). The time-dependent change of functionality states' probability is provided in Fig. 16. The resilience assessment of emergency systems is shown in Fig. 17.

The results show that the resilience of emergency systems decreases dramatically from 79.98% to its lowest value of 25.99% at 5 h. In this study, 65% of system performance is considered to be in a normal state. According to Fig. 18, the 65% recovery of performance loss from the lowest point is equal to 74.97% (i.e., 65% × (1–25.99%) ÷ 25.99%). The system continues to improve even after a 65% recovery of performance loss and is stabilized at 68.18%. However, this stable value does not reach the initial performance state of 79.98%. Different maintenance strategies are adopted to enhance system performance, as shown in Fig. 19. The original strategy is general maintenance with assumed self-repair rates *μ*<sup>1</sup> = 0.15, external repair rates *μ*<sup>2</sup> = 0.25, and steady-state

![img-22.jpeg](img-22.jpeg)

**Fig. A2.** SCS of the installation and cutting system.

![img-23.jpeg](img-23.jpeg)

**Fig. A3.** SCS of the hydrate formation.

performance 68.18%. In strategy 1, µ₁ is changed to 0.25, increasing the system performance by 8.64% from 68.18% to 74.07%. In strategy 2, the value of µ₂ is set as 0.35 and the performance of the system rises by 3.53% from 68.18% to 70.59%. µ₁ and µ₂ are simultaneously changed in strategy 3. The system performance is thus enhanced by 15.41% from 68.18% to 78.69%.

According to the obtained results, it is concluded that the performance of the system deteriorates dramatically after the system is affected by external shocks. The adaptation ability makes the system not directly collapse or fail. Under the impact of adaptation and restoration, the system performance can be restored. However, system performance cannot be improved to the initial state due to the low adaptation and recovery capability. Compared to external repair, the increase in self-repair rates can reduce system degradation. This is because the repair of the system itself is resistant to external shocks. At this time, an appropriate external repair cannot be conducted. After a system has suffered a shock, external repairs are more likely to restore system performance to a better state than self-repair. By raising the value of both µ₁ and µ₂ at the same time in strategy 3, the system performance is better restored than adopting strategy 1 and strategy 2.

According to the prior probability of nodes, the high-probability nodes are selected for partial validation of the proposed model. We take three child nodes X2 (Emergency manager negligence), X41 (Operations are not prompt), and X67 (Emergency schemes are unreasonable) in different emergency operational stages as examples. Their failure probabilities are subject to a change of ±10%, when the system is

Table A1
Probability and related parameter of root nodes.


Table A1 (continued)


Table A1 (continued)


Table A1 (continued)


affected by the thunder. If the prior probability of X2 was increased by $10 \%$, the emergency failure probability will increase by $3.069 \%$ from 0.7134 to 0.7156 . When the prior probability of X2 decreased by $10 \%$, the emergency failure probability reduced by $3.078 \%$ from 0.7134 to 0.7112 . The prior probabilities of X 1 and X 41 increased by $10 \%$, which will rise the emergency failure probability by $4.867 \%$ from 0.7134 to 0.7169 . When the failure rates of $\mathrm{X} 16, \mathrm{X} 26$, and X28 were increased by $10 \%$, the emergency failure probability accordingly increase by $5.383 \%$ from 0.7134 to 0.7172 . Similarly, the decrease in the prior probability of the child nodes will reduce the emergency failure probability. The sensitivity analysis reveals that changes of failure probabilities of child nodes will lead to the variation of emergency failure probability. The results satisfy all the three axioms described in Section 2.5, thus the developed model is verified.

To validate the proposed resilience assessment model for systems subjected to unknown shocks, functionality nodes (adaptation and restoration) are crucial factors in recovery, which are selected as examples to conduct a three-axiom-based sensitivity analysis. The increased $10 \%$ of adaptation probability led to a $1.841 \%$ growth of the probability of the system functionality state from 0.6818 to 0.6944 . When the probability of adaptation and restoration is increased by $10 \%$, the probability of the system functionality state is raised by $2.979 \%$ from 0.6818 to 0.7021 . Similarly, the reduction in the probability of the functionality nodes will decrease the probability of the system functionality state. The result shows that a slight decrease (increase) in the probability of functionality nodes can result in the effect of a relative decrease (increase) to the system functionality state node. Therefore, the proposed model is partially validated for satisfying the three axioms defined in Section 2.5.

### 3.5. Sensitivity analysis

The systems are assumed to be attacked by external disasters including thunder, typhoon, and, earthquake. The failure rates of system components under the above-mentioned disasters are obtained as 0.017 ,

Table A2
Probabilities of human error under various external shocks.


0.023 , and 0.047 stemming from [39]. The performance change of the emergency systems under the impact of various disasters is shown in Fig. 20. Because of the multiple influencing factors and direct shock to emergency operations, typhoons and earthquakes have higher impacts on system performance than thunders. These two shocks decreased the system performance to the lowest point at 0.269 and 0.249 . Fig. 21(a) shows system performance loss with the change of $\lambda$ under the impact of thunders. We can find that system components have higher failure rates, which can lead to larger performance losses in such scenarios. For example, when $\lambda$ is changed by $40 \%$, system performance is decreased by $4.041 \%$ from 0.2866 to 0.2750 . When $\lambda$ is changed by $60 \%$ and $80 \%$, system performance is dropped by $9.310 \%$ and $14.417 \%$, respectively. By enhancing the repair rate of system components, the system performance is restored to a stable state to ensure normal system operation, as shown in Fig. 21(b). For instance, when system components' repair rates are increased by $40 \%$, system performance is improved by $2.839 \%$ from 0.6940 to 0.7137 . When $\mu$ changed by $60 \%$ and $80 \%$, the performance curve increased by $5.169 \%$ and $7.276 \%$. These results indicate the importance of enhancing system maintenance capacities. In the process of emergency operations, it is vital to conduct reliable repair strategies to recover system performance when the system is attacked by an external shock.

When the system suffers an unknown external shock, we utilize sensitivity analysis to identify the effects of parameter changes on system resilience. Results of the sensitivity analysis are shown in Fig. 22. We can conclude that the increase of the failure rate $\left(\lambda_{1}\right)$ under disruptions leads to a decrease in the system performance. For example, when $\lambda_{1}=0.25$, system performance is reduced to the lowest $3.409 \mathrm{E}-01$ in Fig. 22(a). As $\lambda_{1}$ increases to 0.35 , the system performance is degraded to 0.2599 . Similarly, when $\lambda_{1}$ increases to 0.45 and 0.55 , system performance is changed by $23.762 \%$ and $39.040 \%$ from 0.3409 to 0.2213 and 0.3409 to 0.2078 , respectively. We also discuss that changes in the failure rate $\left(\lambda_{2}\right)$ under normal conditions affect system performance. The final system performance reaches different stable states with the variation of $\lambda_{2}$. The larger value of $\lambda_{2}$ caused a lower state value that the system performance returns to, as shown in Fig. 22(b). Additionally, influences of system self-repair rate $\left(\mu_{1}\right)$ and external repair rate $\left(\mu_{2}\right)$ on system performance are established in Fig. 22(c) and (d). The results show that the increase of $\mu_{1}$ and $\mu_{2}$ can improve the system performance. For example, when the value of $\mu_{2}$ increases by $2.5 \%$ in turn, the system performance gradually increases to a stable state of 0.6818 to 0.7018 to
0.7175 . When $\mu_{2}$ changes by $40 \%$, the system degradation is changed by $1.027 \%$ from the lowest point 0.2599 to 0.2994 . A variation of $\lambda_{2}$ and $\mu_{1}$ is concluded to significantly affects the final stable value which system performance returns to. Changes in $\lambda_{1}$ and $\mu_{2}$ are critical in the process of system degradation and rapid repair after the degradation. Thus, when emergency systems suffer a shock, timely and effective external maintenance strategies can restore rapidly system performance. To enhance the final stable state of the system recovery, system self-repair is supposed to be strengthened by optimizing system design.

## 4. Discussion

In presence of limited prior information for external shocks, it is hard to evaluate emergency system resilience. For conducting a resilience assessment of the system subjected to known and unknown external disruptions, a multi-step STAMP is proposed to develop DBN models. The proposed methodology aims to decompose emergency systems into various sector elements and emergency stages, which are used to evaluate the emergency system's performance. Such a method can be applied to other emergency response systems to enhance the reliability of fault detection and resilience evaluation. Additionally, since nonlinear real systems are difficult to model, a linear approximation of the model may introduce unacceptable errors in assessing the system performance. The proposed resilience evaluation methodology is also extended to evaluate performance loss of engineering system. We discussed the design of multi-stage emergency operations, the construction of resilience assessment models, and the optimization of system resilience.
(1) Design of multi-stage emergency operations

Complex systems are held together by local relationships. The components respond locally to the received information. In this paper, an emergency system is regarded as a multi-stage emergency process. STAMP is proposed to model the LMRP emergency system including the lowering process, installation process, and hydrate formation. Compared with conventional modeling methods, such as FT, ET, and BT, the proposed approach can consider more comprehensive aspects of emergency operations (e.g., human factors, software, and mechanical components) as an integrated whole and recognizes safety constraints related to interactions among these dimensions. To quantify a failure in

one or more parts and their interactions causing consequences on the system's functioning, the constructed STAMP model is mapped into DBN for capturing local relationships (e.g., information flow, control loop) as the failure propagation between nodes to infer the system reliability.
(2) Construction of resilience assessment models

A DBN-based resilience assessment model is proposed to evaluate the resilience of an emergency system suffering known and unknown disruptions. Effects of categories and strengths of disruptions, and system maintenance strategies on the resilience of the systems are investigated. Earthquakes have higher effect than thunder and typhoon on the emergency system. System performance decreases with the increase in failure rates of system components. By enhancing the repair rate with external efforts, system performance gradually increases and finally reaches a stable state. When the system is subject to an unknown shock, the system's absorption, adaptation, restoration, and learning abilities are mapped into the system functionality state for modeling system resilience. Through analyzing the influences of change of contributing factors on the change of system performance, the changes of $\lambda_{2}$ and $\mu_{1}$ have significant influence on the recovery of the system performance to the stable state after disruptions. The changes of $\lambda_{1}$ and $\mu_{2}$ affect system performance degradation to values of the lowest point and the rapid rise of the recovery curve after degradation. This indicates the importance of obtaining accurate values of $\lambda$ and $\mu$ in making a proper estimation of system resilience.
(3) Optimization of system resilience

By comparing the performance curves generated by Configurations 1 and 2 , we find that the parallel system can improve the system resilience. The redundant configuration of the running system has greater impact on the performance change of emergency systems than that of the installation and hydrate formation stages. This is because the redundant configuration of the system improves the ability of the system to absorb external disruptions in the lowering process. Based on the obtained results, the system performance is optimized by reducing the probability of human errors. When the system is attacked by unknown shocks, we assume that the system design is changed to improve the system self-repair rates and resource allocation to increase external repair rates. As the system self-repair rates grow, the range of system performance degradation decreases gradually. When the external repair rate is increased, the final restored performance stable state is continuously improved. By changing the two cases mentioned above, the resilience of the system is optimized.

## 5. Conclusion

In this paper, we integrated multi-stage STAMP and DBN to develop a resilience assessment model for emergency response systems. By identifying hierarchical control and feedback in emergency operations, a multi-stage STAMP model is constructed to determine emergency failure scenarios. When the system suffers a known external shock, external disasters are decomposed into specific RIFs that affect system components to generate reliability parameters. The system performance is evaluated by the degradation and recovery models based on DBN. When undesired disruptions to the system cannot be recognized, uncertain shock is expressed as a random event with the Poisson distribution. A DBN-based resilience evaluation model is established by mapping temporal processes of disruption, absorption, adaption, and restoration into the analysis of system functionality. Eventually, we conduct a sensitivity analysis to capture the crucial contributing factors for system resilience. By improving the safety of components and the capability of system learning, system performance is optimized into a safer state than its initial state. From the above results and discussion, we draw the following conclusions.
(1) The proposed DBN model takes advantage of STAMP to consider the information feedback, establish inadequate safety constraints, and model multi-stage emergency processes of the system. By evaluating the vulnerable components and interactions of system accidents, the complexity of systems is decomposed. Further, the nonlinear coupling between components is resolved.
(2) A resilience assessment model is proposed to evaluate system resilience when the system suffers from known and unknown shocks. When the system is attacked by known shocks, earthquakes have more significant impacts than thunder and typhoon on emergency systems. When the system is subject to unknown disruptions, the changes in the failure rate $\left(\lambda_{1}\right)$ under disruptions and the repair rate $\left(\mu_{2}\right)$ with external efforts affect much more on the system performance than the failure rate $\left(\lambda_{2}\right)$ under normal conditions and the self-repair rate $\left(\mu_{1}\right)$.
(3) By adjusting the redundancy configuration of emergency systems, the ability of the systems to absorb external disruptions is enhanced and the resilience of the systems is increased. Additionally, we assume that the system design is changed to improve the system's self-repair rates. Combined with the improvement of external repair rates, the intensity of system performance degradation after the system is subjected to external impact is mitigated. The resilience of the system is therefore optimized.

The proposed resilience assessment model can help to resist unforeseen disruptions and manage system resilience. By optimizing system resilience, we can improve the system design and provide proper maintenance strategies to prevent accidents. In future research, it deserves to consider the dynamic-coupling mechanisms of disruptions. To grasp the impact of real-time disruptions on system performance, a digital twin model can be integrated into the proposed framework.

## CRediT authorship contribution statement

Xu An: Methodology, Validation, Visualization, Writing - original draft. Zhiming Yin: Conceptualization, Data curation. Qi Tong: Writing - review \& editing. Yiping Fang: Formal analysis, Writing - review \& editing. Ming Yang: Conceptualization, Formal analysis. Qiaoqiao Yang: Writing - review \& editing. Huixing Meng: Conceptualization, Investigation, Supervision, Funding acquisition, Writing - review \& editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (Grant No. 52004030), the Open Project Program of State Key Laboratory of Virtual Reality Technology and Systems, Beihang University (No. VRLAB2022B01), National Key R\&D Program of China (Grant No. 2022YFC2806504), High-technology ship research project (Grant No. CBG2N21-4-2), and CNOOC R\&D Program during the 14th Five-Year Plan Period (Grant No. KJGG-2022-17-05).

## Appendix
