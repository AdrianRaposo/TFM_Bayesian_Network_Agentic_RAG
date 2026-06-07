# Article 

## Reliability Analysis of a Three-Engine Simultaneous Pouring Control System Based on Bayesian Networks Combined with FMEA and FTA

Zhaoxia Cui *, Minghai Zheng, Jin Wang and Jiang Liu

## check for updates

Citation: Cui, Z.; Zheng, M.; Wang, J.; Liu, J. Reliability Analysis of a Three-Engine Simultaneous Pouring Control System Based on Bayesian Networks Combined with FMEA and FTA. Appl. Sci. 2023, 13, 11546.
https://doi.org/10.3390/ app132011546

Academic Editor: Yutaka Ishibashi
Received: 6 September 2023
Revised: 12 October 2023
Accepted: 19 October 2023
Published: 21 October 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

School of Mechanical Engineering, Inner Mongolia University of Technology, Hohhot 010051, China; zhengminghai77@163.com (M.Z.); wangjin131842@163.com (J.W.); liujiangimut@imut.edu.cn (J.L.)

* Correspondence: cuizhaoxia73@163.com


#### Abstract

Pouring is an important process in the production of solid propellant rocket engines, and usually, the cost of a solid propellant rocket engine is extremely high. Therefore, pouring production with high reliability is very important. The pouring of three engines of solid propellant rocket engines simultaneously can greatly improve its production efficiency. However, it makes the system more complex and redundant. For a multi-state system, it is difficult to make an accurate evaluation of system reliability. Aiming at the redundancy of multiple engines and acousto-optic combined control in the three-engine simultaneously slurry pouring alarm control system with dissimilar redundant alarm units, a reliability analysis method is proposed based on the combination of Failure Mode Effect Analysis (FMEA) and Fault Tree Analysis (FTA). The control system is divided into several redundant states according to the alarm function, and then the Bayesian Networks method is used for reliability evaluation and calculation. Finally, the reliabilities of systems with dissimilar redundancy degrees are obtained. The tangible results of this research work are as follows: (1) The research results obtained by applying the FMEA method laid a foundation for the establishment of a fault trees model for analyzing the reliability of the control system using the FTA method, in addition, which can guide the maintenance and fault identification of the control system during engineering application. (2) The calculated value of the reliability of the control system is 0.999989 , and the mean time between failures is MTBF is $5 \times 10^{4}$ by using the fault tree analysis method, which proves that the designed three-engine simultaneous pouring system is very reliable. (3) Based on the calculation and comparison of the Bayesian Networks of redundant three-engine pouring control systems, the circuit diagram of the improved control system is identified.


Keywords: solid propellant rocket engine; three-engine simultaneously pouring control system; reliability; dissimilar redundancy system; FTA; FMEA; Bayesian Networks

## 1. Introduction

Owing to the high-quality requirements and high manufacturing cost of solid propellant rocket engine products, the high reliability of automatic control charging equipment is very important for the production of solid propellant rocket engines [1]. Because of the long production cycle of the pouring process and low efficiency, the pouring process of a single engine cannot meet the demand for high efficiency for larger batches of production. The pouring of three solid propellant rocket engines simultaneously can greatly improve production efficiency. At the same time, the high reliability of the control system is an important guarantee of pouring work, which can reduce or avoid economic losses caused by pouring failure and explosion accidents caused by cleaning up residues. Therefore, the reliability analysis of the three-engine simultaneous pouring control system is very important.

Nowadays, many scholars have focused on reliability analysis and its applications. Reliability-based multidisciplinary design optimization (RBMDO) has been widely ac-

knowledged for the design problems of modern complex engineering systems. Some of the issues with RBMDO are reviewed in references [2-5]. In reference [6], the saddle point approximate reliability analysis method is introduced, and the collaborative optimization method is combined to solve the uncertainty problem. Reliability analysis methods such as Fault Tree Analysis (FTA), Failure Mode and Effect Analysis (FMEA), Reliability Block Diagram (RBD), and Markov Models have been widely used in rolling stock [7]. Reference [8] describes a reliability analysis method called AKMP, which is used to evaluate the failure probability of mechanical structures. This method utilizes multi-point sampling and active learning, which combines the GA-Halton sequence and a new learning function, FELF, to update the model. The results show that the AKMP method has good accuracy and efficiency. However, the application of these methods to the solid propellant rocket engine pouring control system is very limited.

Failure mode and effect analysis (FMEA) is used to proactively identify product failures and provide preventive measures to eliminate or reduce failures [9]. The traditional risk priority number (RPN) method has been criticized for having many deficiencies, and various risk priority models have been proposed to enhance the performance of FMEA [10]. Failure mode and effects analysis (FMEA) has been extensively used for examining potential failures in products, processes, designs, and services in reference [11], the risk factors such as the occurrence O , severity S , and detection D of each failure mode in the traditional FMEA are treated as fuzzy variables and evaluated by using fuzzy linguistic terms and fuzzy ratings. As a result, fuzzy risk priority numbers (FRPNs) are proposed for the prioritization of failure modes. In terms of the possibilities of failure of bottom events, an algorithm of the intuitionistic fuzzy fault-tree analysis is proposed to calculate the fault interval of system components and to find the most critical system component for managerial decision-making based on some basic definitions [12]. To improve the performance of the FMEA method, some FMEA-based approaches are proposed to integrate the advantages of the Fault Tree Analysis (FTA) and FMEA [13,14]. In Ref. [15], a fault tree for calculating the reliability of combinatorial logic circuits associated with single and multiple faults was proposed.

In order to maximize system reliability, the redundancy strategy, i.e., the active or standby redundancy of each k-out-of-n subsystem in the traditional problem, was determined [16], and the door redundancy was also introduced to improve the reliability of each digital logic gate. In order to improve the reliability and safety of an actuation system, dissimilar redundancy technology has been adopted in modern aircraft design [17]. In reference [18], based on the design optimization under mixed uncertainty, a new kriging model is proposed to solve the design optimization problem of time-varying reliability with flexible constraints. In reference [19], a subregion computing strategy is proposed, and a new learning function is introduced, which can effectively improve the computing efficiency of time-varying reliability. In reference [20], a new coupled Kriging model is proposed to balance computational costs and accurate results.

In this paper, an FMEA table for determining the important components of the control system is established. The FMEA and FTA are combined to analyze the reliability of a three-engine simultaneous pouring control circuit system. Based on the established FMEA table, the system is qualitatively and quantitatively analyzed by using FTA. The redundant design of the alarm function can improve the reliability of the control system significantly. However, many redundancies will lead to high cost, complexity, and maintenance difficulties. In order to reasonably evaluate the reliability of an alarm control system with dissimilar redundancies, the control system is divided into several redundant states according to the alarm function, and then Bayesian Networks analysis is applied to obtain the most suitable system redundancy design. The production cost of the solid rocket engine involved is very high. Although the simultaneous pouring of three solid rocket engines greatly improves the production efficiency, the loss is more serious once the pouring fails, so it is more required to ensure particularly high reliability in the production process. In order to ensure this problem, this paper focuses on the reliability of the design of the three-engine

simultaneously pouring control system and the rationality of the redundant design of the designed control system.

# 2. Model of Three-Engine Simultaneously Pouring Control Circuit System 

In a three-engine simultaneous pouring system of a certain type of solid propellant rocket engine, as shown in Figure 1, a control system for detecting and alarming whether the propellant slurry poured is full of combustion chambers. The functions of the system are shown in Figure 2. It is also the key technology to realize the automatic control of the pouring process.
![img-0.jpeg](img-0.jpeg)

Figure 1. Three-engine simultaneously pouring system of a solid propellant rocket engine.
![img-1.jpeg](img-1.jpeg)

Figure 2. Schematic diagram of three-engine pouring control circuit system.
According to Figures 2 and 3, it is easy to know that the system has many redundancies. Each engine pouring detection circuit is equipped with a proximity switch to detect whether the pouring is complete, and for the pouring result, not only an indicator light is set up, but also a buzzer alarm is equipped. The main electrical components of the pouring detection control system and their representative symbols have been marked, and they are low voltage DC power supply, fuse FU1, proximity switches SP-1, SP-2, SP-3, the power indicator light HL1, the main switch QF1, the pouring switch QF2, the pouring completion indicator lights HL1, HL2, HL3, the time relays T1, T2, T3, buzzers H1, H2, H3, and knob switches. A photo of the partial main physical, electrical circuit, and components of the control system is shown in Figure 4.

![img-2.jpeg](img-2.jpeg)

Figure 3. The circuit diagram of the three-engine simultaneously pouring control system.
![img-3.jpeg](img-3.jpeg)

Figure 4. Partial physical circuits of the three-engine simultaneous pouring control system.
The control system can automatically detect whether the pouring is working or failing. The automatic control system takes the proximity switch as the core control element, which can realize the automatic sound and light alarm function and is more suitable for the remote control of the pouring process. Three proximity switches are equipped on the mechanical connectors called receiving trays, which are fixed on the pouring ports of three combustion chambers in the vacuum cylinder. There is a certain working distance between the proximity switch and the Propellant slurry overflowing from the pouring port to the receiving tray. The input signals of the control system come from proximity switches. When any of the proximity switches send a signal, its corresponding buzzer or indicator light alarms, indicating that the pouring work is complete, and when all three engines correspond to the buzzer or indicator alarm, it means that the pouring process of the entire three-engine system is complete.

# 3. Reliability Analysis Flowchart of Three-Engine Pouring Control Circuit 

The combination of FMEA and FTA can be effectively used in system design [7,21]. Based on this combined reliability analysis method, the Bayesian Networks method is used to further analyze and optimize the redundant circuits. The flowchart of the reliability analysis of the three-engine pouring control circuit is shown in Figure 5. Using the FMEA method, the system is divided into several different subsystems. Then, the possible failure modes, causes, and effects of each subsystem are analyzed one by one, and a detailed list is given to summarize and analyze the faults of the system or electronic components from the entire system. A fault tree is established in combination with the FMEA table, and then qualitative and quantitative analyses are performed based on the established FTA. Finally, the Bayesian network method is used for reliability evaluation and calculation.

![img-4.jpeg](img-4.jpeg)

Figure 5. Reliability analysis flowchart of three-engine pouring control circuit.

# 4. FMEA Analysis of Three-Engine Pouring Control System 

The FMEA is an important method to improve the reliability of systems or equipment [22]. As a planning method for precaution, the main purpose of FMEA is to discover and evaluate potential failures and consequences of the systems or equipment and to find ways to avoid or reduce the occurrence of faults or failures. In addition, this analysis is also the basis for fault tree analysis (FTA).

### 4.1. Establishment of Reliability Logic Block Diagram of Three-Engine Pouring Control System

As can be seen from Figure 3, the acousto-optic alarm control circuit system of the three-engine pouring process has automatic air circuit breakers, fuses, proximity switches, low-voltage DC power supplies, small relays, indicator lights, buzzers, and knob switches. According to the function, the system is graded into a series of subsystems, and the bottommost unit is a single electronic component. Therefore, the failure of arbitrary components will lead to the failure of the entire system to varying degrees. Before performing FMEA, according to their functions, the system reliability logic block diagram is established, as shown in Figure 6. Only one set of pouring control circuits is considered in this reliability logic block diagram, and the other two sets of pouring control circuits are ignored.
![img-5.jpeg](img-5.jpeg)

Figure 6. Reliability logic block diagram of the main part of the control circuit.

### 4.2. Failure Mode Effect Analysis

The FMEA method is used to analyze the components of the reliability logic block diagram in Figure 6. As a qualitative analysis result, the FMEA table of the single-engine pouring control circuit system is shown in Table 1.

Table 1. FMEA table of the main part circuit for the three-engine pouring control system.


# 5. FTA Analysis

The FTA method was first proposed in 1961 by American Bell Laboratories H.A. Watson and D.F. Hansl. Nowadays, the FTA is an important method for reliability analysis of complex systems and has been widely used in many fields.

### 5.1. Establishment of Reliability Logic Block Diagram of Three-Engine Pouring Control System

Based on the FMEA table of the three-engine pouring control circuit system, FT is constructed, as shown in Figures 7 and 8. ![img-6.jpeg](img-6.jpeg)

Figure 7. The fault tree model of the subsystem.

![img-7.jpeg](img-7.jpeg)

Figure 8. The fault tree model of the three-engine pouring control system.
In Figures 7 and 8, Z, T, D, and R represent the main power switch failure, the pouring system switch, the low-voltage DC power supply, and the fuse, respectively. C represents the failure of the three subsystems of the control circuit, B represents the failure of one of the subsystems, J, X, L, S, and F are the failure of the proximity switch, the knob switch, the pouring completion indicator, the time relay, and the buzzer respectively. G represents the pouring completion failure, and $g$ represents the buzzer indicating the failure. A represents the failure of the three-engine pouring system.

# 5.2. Fault Tree Analysis of Control Circuit System 

The FTA method is used to study the various causes of system or equipment failure. Establish a logical relationship between failure causes, which are described by using the fault trees. The fault tree of the three-engine pouring control circuit system is established, and then the qualitative analysis and quantitative analysis are performed.

### 5.2.1. Qualitative Analysis

The fault tree is qualitatively analyzed using the Minimum Cut Set (MCS) method. The downlink method is adopted to find the MCS of the system. The MCS is a set of the minimum basic events that cause the top event to occur [23].

The MCSs for the fault tree of the three-engine pouring control circuit are: $\{Z\},\{T\},\{R\}$, $\{D\},\{S, L\},\{F, L\}$. The minimum cut sets are constructed by the corresponding components: $\{Z\}$ represents the minimum cut set of component $Z,\{T\}$ represents the minimum cut set of $T,\{R\}$ represents the minimum cut set of $T,\{D\}$ represents the minimum cut set of $D,\{S, L\}$ represents the minimum cut set of $S, L,\{F, L\}$ represents the minimum cut set of $F, L$.

Based on the results of the MCSs and occurrence and severity, the main switch, the rotary switch, and the proximity switch have significant effects on the failure of the threeengine pouring control circuit system. Therefore, the reliability of key components should be improved in the control circuit to minimize the occurrence of basic events and to reduce the minimum number of cut sets in the control system in practice.

### 5.2.2. Quantitative Analysis

The failure rate of each component is calculated based on the GJB/Z299D Electronic Equipment Reliability Prediction Manual, as shown in Table 2. The parameters involved are the basic failure rate $\lambda_{b}$, the environmental coefficient $\pi_{E}$, the contact form factor $\pi_{C_{L}}$, the contact load factor $\pi_{L}$, the mass coefficient $\pi_{Q}$, the rate of action factor $\pi_{C Y C}$, the applied structural coefficient $\pi_{A}$, the utilization factor $\pi_{U}$, and the rated voltage coefficient $\pi_{V}$.

Table 2. The failure rate of each component of the three-engine pouring control circuit system.


(1) The working failure rate of time relay

By consulting the Electronic Equipment Reliability Prediction Manual, the working failure rate of the time relay can be calculated as follows:

$$
\lambda_{p}=\lambda_{b} \pi_{E} \pi_{Q} \pi_{C_{1}} \pi_{C Y C} \pi_{A}
$$

where the basic failure rate is 0.094 , the environmental coefficient is 1 , the mass coefficient is 0.3 , the number of contacts is 2 , and the contact form factor is 1.7 ; the action rate coefficient and applied structure coefficient are taken as 0.1 and 10, respectively.

The calculated value of the working failure rate of the time relay is $0.096 \times 10^{-6}$.
(2) The working failure rate of the proximity switch

According to the relevant parameters of similar proximity switches, the failure rate of the proximity switches is taken as:

$$
\lambda_{p J}=0.431 \times 10^{-6}
$$

(3) The working failure rate of the knob switch

The working failure rate of the switch can be calculated as:

$$
\lambda_{p}=\left(\lambda_{b 1}+\lambda_{b 2}\right)+\pi_{E} \pi_{Q} \pi_{L} \pi_{C Y C}
$$

where the basic failure rate of the knob-type switch drive mechanism is 0.3 , and the basic failure rate of the switch active contact is 0.14 .

The calculated value of the working failure rate of the available knob switch is $0.736 \times 10^{-6}$.
(4) The working failure rate of the button switch

The basic failure rate of the drive mechanism in the button switch is 0.28 , and the values of parameters are the same as those of the knob switch.

The calculated value of the working failure rate of the available button switch is $0.576 \times 10^{-6}$.
(5) The working failure rate of the indicator light

The working failure rate of the indicator light is calculated as follows:

$$
\lambda_{p}=\lambda_{b} \pi_{E} \pi_{U} \pi_{V}
$$

based on the Electronic Equipment Reliability Prediction Manual, the basic failure rate of indicator light is 0.34 ; the environmental coefficient is 1.0 ; the utilization factor is 0.1 ; the rated voltage is 24 V , and the corresponding rated voltage coefficient is 7.6 . The calculated value of the working failure rate of the indicator light is $0.258 \times 10^{-6}$.
(6) The working failure rate of the buzzer

According to the working failure rate of the electro-acoustic device, the failure rate of the buzzer is determined as

$$
\lambda_{p f}=0.245 \times 10^{-6}
$$

Note that the work failure rate of the buzzer can represent the work failure rate of the bell.
(7) The working failure rate of low-voltage DC power supply

The operating failure rate of the low-voltage DC power supply is determined as

$$
\lambda_{p y}=0.857 \times 10^{-6}
$$

(8) The working failure rate of the fuse

The working failure rate of the fuse is given by

$$
\lambda_{p r}=0.150 \times 10^{-6}
$$

# 5.3. Failure Probability of Main Components in Three-Engine Pouring Control Circuit System 

As can be seen from Table 2, the electronic components with higher failure rates are the knob switch, low-voltage DC power supply, proximity switch, and the main switch. Based on the principle of system reliability, the reliability of a series-parallel system can be calculated as follows:

$$
R_{B}=\left(1-\lambda_{p t}\right)\left(1-\lambda_{p y}\right)\left(1-\lambda_{p x}\right)\left(1-\lambda_{p j}\right)\left\{1-\lambda_{p l}\left[1-\left(1-\lambda_{p s}\right)\left(1-\lambda_{p f}\right)\right]\right\}=0.999997
$$

The probability of the top event for the three-engine pouring main control circuit system can be obtained, which is $\mathrm{RB}=0.999997$. The total probability of the three-engine pouring the entire control circuit system is no less than the probability of a series connection of three main control circuits Rsum, which is calculated as:

$$
R_{\text {sum }}=R_{B}^{3}\left(1-\lambda_{P Z}\right)\left(1-\lambda_{P T}\right)\left(1-\lambda_{P D}\right)\left(1-\lambda_{P R}\right)=0.999989
$$

The mean time between failures is MTBF $=5 \times 10^{4} \mathrm{~h}$.

## 6. FTA Analysis

Bayesian Networks can solve interaction problems. For multi-state systems, a fault tree combined with the Bayesian Network method is used for system reliability analysis [21]. The reliability of the three-engine pouring control system is calculated on the premise that the subsystems are independent of each other. Aiming at the inter-effect on electrical components and redundancy design in the system, a polymorphic Bayesian Network is proposed and used to evaluate two dissimilar redundancy designs.

The Bayesian Networks of the three-engine pouring control system based on the fault tree established as shown in Figures 7 and 8 is shown in Figure 9.

The conditional probabilities and prior probabilities for each node are calculated and listed in Tables 3 and 4, respectively.

Table 3. g point CPT (Conditional Probability Table).


Table 4. A point CPT (Conditional Probability Table).


![img-8.jpeg](img-8.jpeg)

Figure 9. Polymorphic Bayesian Networks of three-engine pouring control system.
In this paper, the Bayesian toolbox BNT in MATLAB2016a software is used to calculate the edge probability distribution of the intermediate nodes of the Bayesian Networks [24]. By using the FullBNT-1.0.4 toolbox, the conditional probability and the posterior probability of each component can be calculated. The joint reference algorithm is applied to the model for bidirectional reasoning [4,12]. Using the forward reasoning of the network, the conditional probability of the top event occurring when each bottom event in the original fault tree model occurs alone is calculated, as shown in Table 5. Using backward reasoning, the posterior probability value of each bottom event is calculated, as shown in Table 6.

In the three-engine pouring control system, a four-way pouring delivery device is used to complete the pouring process. Therefore, the pouring completion time of the three engines is almost the same. However, the cost of pouring is very high in order to ensure that there are no accidents in the control system in the pouring process. Thus, the pouring process of three engines is separately monitored. This leads to the redundancy of the three-engine pouring control system.

Table 5. Conditional probability table.


Table 6. Posterior probability values.


According to the alarm function and the number of subsystems, the redundancy of the three-engine pouring control system can be divided into four states. Provided that one subsystem exists, the alarm state is set to I; two subsystems exist, the alarm state is set to II; three subsystems exist, the alarm state is set to III. If no subsystem exists, the alarm state is set to 0 . Therefore, there are many condition states in this system. Buzzer alarm includes a time relay and buzzer and can be considered as a whole one. One of the Bayesian Networks is shown in Figure 10, and the corresponding circuit is shown in Figure 11. The reliability results of all states are shown in Table 7.
![img-9.jpeg](img-9.jpeg)

Figure 10. Bayesian Network with I state and only one buzzer.
![img-10.jpeg](img-10.jpeg)

Figure 11. The improved circuit diagram of the three-engine pouring control system.

Table 7. Probability distribution of three states.


For redundancy allocation in failure interaction, an improved analytic hierarchy process (MAHP) is proposed in reference [25]. Based on this method, the system is decomposed into blocks and reduced blocks, and then the most suitable redundancy allocation components are given. According to the calculation results in Table 7, the system is required to be highly reliability. However, more buzzers will make louder noises. The alarm circuit is taken, including three lights in each subsystem. The circuit diagram of the improved three-engine pouring control system is shown in Figure 11. The corresponding Bayesian Network is shown in Figure 10.

# 7. Discussion 

The proposed reliability analysis method combining FMEA, FTA, and Bayes Networks method is used in the reliability analysis of complex equipment control systems to avoid sufficient consideration of problems in the reliability analysis of the system, but the quantification of the analysis results is not accurate enough. The FTA analysis is carried out based on completing the FMEA analysis of the three-engine simultaneous pouring control system. In this way, the bottom-up FMEA analysis is combined with the top-down FTA analysis method, making the model established by the FTA analysis method more targeted, simplifying the analysis process and providing reliable results. The FMEA method is used to analyze the components of the three casting control systems. When analyzing and identifying the fault mode, the influence of the components is identified. This helps find the cause of the fault and has guiding significance for the design and maintenance. The system fault tree is established, and the weakest part of the system can be determined according to the obtained minimum cut set. The high-reliability equipment components are used to reduce the occurrence of basic events or redundancy designs and then to reduce the number of minimum cut sets. The mean time between failure (MTBF) of the control system is obtained through the quantitative analysis of the minimum cut set, based on which the reliability of the three-casting control system is judged and improved. Because of the various states of the system, the Bayes network is selected to use a finite set to record the probability of the system in each state, model the uncertainty of the system according to the known data, and then predict the future state of the system. The results show that adding some guaranteed parts will greatly improve the reliability of the system. Considering the importance of solid rocket engine reliability requirements, it is particularly important to add redundancy to the system design. The weight is calculated by the MAHP analysis method, and the necessary redundant components are selected to optimize the three-engine simultaneous pouring control system and improve the reliability of the three-engine simultaneous pouring control system.

## 8. Conclusions

In this paper, the FMEA, FTA, and Bayesian Network methods are combined to evaluate the three-engine pouring control system of a solid propellant rocket engine. In order to prolong the service life of the system, the failure mode effect analysis of the solid propellant rocket engine three-engine control system was carried out, and the FMEA analysis results were further quantified using the forward and backward reasoning of the Bayesian Network. In order to improve system reliability, an optimized dissimilar redundancy design is proposed. Human-machine relationships and refurbishment cycles were taken into account, and the design was divided into redundant shared design and non-redundant shared design. The two dissimilar redundancy designs were analyzed using Bayesian Networks based on FTA. The results show that the buzzer is the component

that has the greatest effect on the system. The buzzer is used as a redundant componentsharing scheme to improve the reliability of the system when using the least components. The application of the proposed method has been proved by numerical examples. This model can help engineers carry out inspection and maintenance plans, which can improve the performance of economic and safety control systems. The design of the three-engine simultaneous pouring control system can meet the production demand, but the reliability test of the equipment still needs to be carried out in the actual production. The ideas and methods proposed by this research work can be applied to more complex and multi-status electromechanical products, and its application will show more advantageous effects.

Author Contributions: Conceptualization, Z.C. and M.Z.; Methodology, Z.C. and M.Z.; Software, M.Z. and J.L.; Validation, Z.C. and M.Z.; Formal analysis, Z.C., M.Z. and J.W.; Investigation, Z.C. and M.Z.; Resources, M.Z.; Data curation, Z.C. and M.Z.; Writing-original draft, Z.C. and M.Z.; Writing-review \& editing, Z.C. and M.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This work is supported by The National Natural Science Foundation of China, No. 51965048.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: No new data were created or analyzed in this study. Data sharing is not applicable to this article.

Acknowledgments: Thanks to Jianjun Li and Inner Mongolia Hongxia Chemical Plant for providing support and help to the research of this paper.

Conflicts of Interest: The authors declare that they have no conflicts of interest to report regarding the present study.
