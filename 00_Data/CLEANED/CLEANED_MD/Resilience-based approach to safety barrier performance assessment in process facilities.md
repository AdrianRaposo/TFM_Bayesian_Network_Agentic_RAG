# TUDelft 

## Delft University of Technology

## Resilience-based approach to safety barrier performance assessment in process facilities

Sun, Hao; Wang, Haiqing; Yang, Ming; Reniers, Genserik

## DOI

10.1016/j.jlp.2021.104599

## Publication date

2021

## Document Version

Final published version

## Published in

Journal of Loss Prevention in the Process Industries

## Citation (APA)

Sun, H., Wang, H., Yang, M., \& Reniers, G. (2021). Resilience-based approach to safety barrier performance assessment in process facilities. Journal of Loss Prevention in the Process Industries, 73, Article 104599. https://doi.org/10.1016/j.jlp.2021.104599

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

# Resilience-based approach to safety barrier performance assessment in process facilities 

Hao Sun ${ }^{\circledR}$, Haiqing Wang ${ }^{\mathrm{a}, *}$, Ming Yang ${ }^{\mathrm{b}, * *}$, Genserik Reniers ${ }^{\mathrm{b}, \mathrm{c}, \mathrm{d}}$<br>${ }^{a}$ College of Mechanical and Electronic Engineering, China University of Petroleum (East China), Qingdao, China<br>${ }^{\text {b }}$ Safety and Security Science Section, Department of Values, Technology, And Innovation, Faculty of Technology, Policy, and Management, Delft University of Technology, the Netherlands<br>${ }^{c}$ Faculty of Applied Economics, Antwerp Research Group on Safety and Security (ARGoSS), Universiteit Antwerpen, 2000, Antwerp, Belgium<br>${ }^{d}$ CEDON, KULeuven, 1000, Brussels, Belgium

## A R T I C L E I N F O

Keywords:
Safety barrier management
Resilience
Bayesian network
Availability

## A B S T R A C T

The performance assessment of safety barriers is essential to find vulnerable elements in a safety barrier system. Traditional performance assessment approaches mainly focus on using several static indicators for quantifying the performance of safety barriers. However, with the increasing complexity of the system, emerging hazards are highly uncertain, making it challenging for the static indicators to assess the performance of safety barriers. This paper proposes a resilience-based performance assessment method for safety barriers to overcome this problem. Safety barriers are classified according to their functions first. The dynamic Bayesian network (DBN) is then introduced to calculate the availability function under normal and disruption conditions. The ratio of the system's availability, when affected by the disruption, to the initial availability, is used to determine the absorption capacity of the system. The ratio of the quantity of availability recovery to the total quantity of system represents the adaptation and restoration capacity of the system. The system's resilience is represented by the sum of absorption, adaptation, and restoration capacities. The wax oil hydrogenation process is used to demonstrate the applicability of the proposed methodology.

## 1. Introduction

Process accidents may lead to severe consequences including damages to asset, people, and environment. The role of the safety barrier is to isolate the source of danger from people and property, thereby ensuring safety (Sun et al., 2021). Safety barriers can be a single equipment or an action, or a complex system that can reduce the probability and
consequence of an accident (Bubbico et al., 2020). According to different functions, safety barriers are divided into different categories. Dianous and Fiévaz (2006) divided safety barriers into passive barriers, active barriers, human actions, and symbolic barriers. Rausand (2011) divides safety barriers into proactive and reactive barriers according to whether service time of safety barrier is before or after the specific undesired event. Kang et al. (2016) divides safety barriers into three

[^0]
[^0]:    List of Abbreviations \& symbols: BN, Bayesian network; DBN, dynamic Bayesian network; CPTs, conditional probability tables; LOPA, Layer of Protection Analysis; SIL, safety integrity level; RPB, release prevention barrier; DPB, dispersion prevention barrier; IPB, ignition prevention barrier; EPB, escalation prevention barrier; HFB, human factor barrier; MOB, management and organizational barrier; R1, the initial resilience of safety barrier; D1, under the premise that the system keeps itself in a safe state, the maximum disruption intensity that can be withstood; R1', the improved resilience of safety barrier; D2, under this disruption intensity, the safety barrier resilience will be irreversibly affected; $A_{1}$, the equilibrium state under normal condition; $A_{2}$, the lowest state of system availability when a disruption occurs at $t_{2} ; A_{3}$, a new stable state of the system availability when external maintenance is provided at $t_{3} ; A_{5}$, the absorption capacity of system; $f\left(T_{1}\right)$, the function of system availability decreases with component degradation under normal conditions; $f\left(T_{2}\right)$, the function of system availability increase with time under external repair after the disruption; $f\left(T_{3}\right)$, the function of system availability when system is not resilient after disruption; $S$, the total system availability; $S_{1}$, the loss availability of system after disruption; $S_{2}$, the availability recovery amount of the system during the adaptation and restoration period; $S_{3}$, the remaining availability of system after disruption; $R_{P}$, the resilience-based performance of system; $X_{i}$, the nodes of system; $\pi(\mathrm{Xi})$, the parent nodes of $X_{i} ; P(U)$, the joint probability of a set of random variables $U=\left(X_{1, \mathrm{~S} 2, \mathrm{~S} 3}, \ldots, \mathrm{s}_{N}\right)$.
    * Corresponding author. College of Mechanical and Electronic Engineering, China University of Petroleum (East China), Qingdao, 266580, China.
    ** Corresponding author. Delft University of Technology, the Netherlands.
    E-mail addresses: wanghaiqing@upc.edu.cn (H. Wang), m.yang-1@tudelft.nl (M. Yang).
    https://doi.org/10.1016/j.jlp.2021.104599
    Received 6 December 2020; Received in revised form 30 June 2021; Accepted 13 July 2021
    Available online 17 July 2021
    0950-4230/© 2021 Elsevier Ltd. All rights reserved.

categories: personal barriers, organizational barriers, and technical barriers. A detailed review of barrier categories is presented in Section 2.

The performance of safety barriers determines whether an incident will occur and develop into an accident, which may affect people, property, and the environment (Sobral and Soares, 2019)). The evaluation of safety barrier performance is essential to ensure system safety. Dianous and Piévez (2006) divided safety barriers into four categories and proposed an evaluation method and indicators, including response time, efficiency, and level of confidence, to assess the performance of safety barriers. A LOPA (Layer of Protection Analysis) based approach is proposed by (Landucci et al., 2015) to define and measure safety barrier performance in preventing escalation. A comprehensive approach is proposed by Han et al. (2019) to calculate the optimum maintenance intervals of safety barriers. Bucelli et al. (2018) divided safety barriers into three categories, and assessed the performance safety barriers through two indicators (i.e., availability and effectiveness). A detailed review of the performance indicators is presented in Section 2.

Many indicators may influence the performance of a safety barrier. Through the comprehensive evaluation of these indicators, safety barrier performance can be evaluated. However, in recent years, highly complex engineering systems have developed rapidly. The degree of interdependence and interaction between subsystems and their components is increasing. The existing evaluation methods of safety barrier performance are static, and it is difficult to assess safety barrier performance dynamically. The traditional risk assessment alone is considered inadequate to ensure a complex system's safety (Park et al., 2013; Tong et al., 2020). Many recent studies have proposed methods and indicators for safety barrier performance evaluation (e.g., see Kang et al., 2016; Sobral and Soares, 2019). However, the hazards in complex systems have high uncertainty, making these static indicators challenging to quantify the performance of the safety barrier system.

Resilience assessment is more advantageous than traditional methods to process a complex system with uncertain disturbances because it can consider uncertain hazards and failure propagation after a disturbance (Tong et al., 2020; Zinetullina et al., 2021). As a new research paradigm of safety science, resilience has received widespread attention (Dessavre et al., 2016; Chen et al., 2020). Hosseini and Barker (2016) proposed a new method to measure resilience as a function of absorptive, adaptive and restorative capacities with Bayesian networks. Yodo and Wang (2016) applied engineering resilience metrics to calculate reliability and restoration after a disruptive event. Cai et al. (2018) proposed a new availability-based engineering resilience metric from reliability engineering, and considered resilience as an intrinsic ability and an inherent attribute of an engineering system. Chen et al. (2020) developed an urban resilience model considering adaptability, resistance, and recovery. Abimbola and Khan (2019) developed a dynamic Bayesian network-based method to assess the system resilience.

Comparing with traditional methods (e.g., static indicators), the resilience-based method is more dynamic and advantageous to process complex systems after uncertain disruptions because it does not pay much attention to the reliability of individual elements, but to understand and promote the system to actively ensure that systems is not out of control. Resilience assessment extends the conventional risk assessment to the post-accident stage. Besides, it can assess the system's ability to absorb, adapt to disruptions, and recover from failures and accidents. For example, the concept of resilience can be used to upgrade BowTie in two possible ways: (1) Traditional BowTie approach analyzes preventative and mitigative measures. With resilience thinking, safety measures can be extended to those for threat or scenario prediction and recovery. (2) Considering the resilience of each safety barrier, the proposed approach may also help to identify new plausible scenarios and opportunities for safety enhancement.

To investigate the safety barrier's performance under disruption, this paper adopts resilience as an indicator of safety barrier performance and proposes a resilience-based method to assess safety barriers' performance. The evidence theory is used to calculate the failure probability
under the disruption. Dynamic Bayesian network (DBN) is introduced to evaluate the availability function of the safety barrier. The safety barrier's performance is represented by the integral ratio of the availability function under different circumstances.

The remaining parts of this paper are organized as follows. Section 2 gives a brief literature review of the performance assessment of the safety barrier. A short description of the proposed method is shown in Section 3. The case study is presented in Section 4. Discussion is provided in Section 5. Finally, conclusions are drawn in Section 6.

## 2. Performance assessment of safety barriers

Performance assessment is a crucial step to find vulnerable elements in the safety barrier system. To check whether the safety level on the plant meets the identified requirements, Dianous and Piévez (2006) proposed three indicators (effectiveness, response time, and level of confidence) to analyze the performance of safety barrier systems. Practitioners should have an idea of their safety functions and safety levels by evaluating the performance of the safety barriers. To prevent domino accidents, Landucci et al. (2015) proposed a LOPA-based methodology to quantify safety barrier performance. Safety barriers are divided into active protection systems, passive protection systems, and procedural and emergency measures, and two indicators (availability, and effectiveness) are proposed to evaluate a safety barrier system's performance. Landucci et al. (2016) proposed a quantitative method to assess safety barrier performance to prevent domino accidents. Bucelli et al. (2018) established a structured method to evaluate the safety barrier system in an offshore oil and gas platform under harsh environment. Two indicators (i.e., availability, effectiveness) are proposed to assess the performance of three safety barrier categories, namely, active protection systems, passive protection systems, and procedural and emergency measures. Kang et al. (2016) developed a comprehensive method to evaluate the safety barrier system. It includes three safety barrier categories (i.e. personnel barriers, organization barriers, and technology barriers) and three indicators (i.e. degree of confidence, effectiveness, and economic evaluation). Sobral and Soares (2019) proposed a method to assess the adequacy of the safety barrier, and evaluated the performance of safety barriers by linking a SIL level to the probability of accidents. This method can verify whether existing safety barriers can effectively prevent accidents. The specific categories and indicators of safety barriers are shown in Table 1.

In the above literature, the performance of the safety barrier is evaluated by several static indicators. However, the safety barrier system involves both human and organizational factors, making the performance uncertain and dynamic. Therefore, it is necessary to define a new indicator to develop a comprehensive method to quantify the performance of safety barriers.

## 3. The proposed methodology

In the chemical and process industry, loss of containment can lead to fires, explosions, and personnel poisoning, causing casualties, property losses, and environmental damage. It is essential to estimate the risks of loss of containment and also take measures to reduce accident risks.

Fig. 1 describes the methodology employed in this study. First, the safety barriers existing in the system will be identified and classified. Then, the performance assessment model for the safety barriers will be established. After that, the DBN model will be built for each safety barrier to calculate the availability function of the safety barriers under expected degradation and disruption conditions. The resilience of safety barriers is calculated by using the integral of the availability function. Finally, the developed DBN model of each safety barrier will undergo a sensitivity analysis. Fig. 1 and the following sections describe the main steps of the proposed method.

Table 1 A summary of the categories and performance indicators of safety barriers from literature.


### 3.1. Determination of safety barriers

Many accidents occurred in the process industry, including personnel poisoning, fire, and explosion (Sun et al., 2020). Loss of containment is the root cause of these accidents. To prevent catastrophic accidents in the process industry, it is necessary to analyze the safety barriers' performance.

There are many different classifications of the safety barrier, as discussed above. In the SHIPP methodology proposed by Rathnayaka et al. (2011a,b), safety barriers are classified into 7 categories: release prevention barrier (RPB), dispersion prevention barrier (DPB), ignition prevention barrier (IPB), escalation prevention barrier (EPB), damage control emergency management barrier (DCEM), human factor barrier (HFB), and management and organizational barrier (MOB), respectively. Hence, safety barriers are classified based on their functions.

Furthermore, the event tree model is introduced to determine the safety barriers and corresponding consequences of the system. It is worth noting that the human factors and management and organizational factors affect the entire accident process of the system, as shown in Fig. 2.

The function of the RPB is to prevent loss of containment. When the barrier fails, it means that the loss of containment occurs. Relevant measures should be taken to prevent a large amount of substance from leaking and gathering, such as emergency shutdown systems, gas detection systems, ventilation, etc. These measures are DPB. When the DPB fails, it means that a large amount of substance exists in the chemical plant. If the leaked substance is flammable, a fire or explosion will occur when the ignition source exists. If the substance is toxic, it can cause injury or death when people are exposed to it. To prevent the occurrence of secondary accidents, the IPB should be set to eliminate the ignition source. When the IPB fails, a large amount of flammable gas within the explosion limit will cause a fire or explosion accident. Relevant measures should be taken to mitigate the accident consequence, which may include setting up fire detectors, firewalls, and blast walls, which belongs to EPB. When the EPB fails, a catastrophic accident will occur. This study aims to prevent the occurrence of devastating accidents. Therefore, according to the functions of the safety barriers in the process system, safety barriers are classified into RPB, DPB, IPB, EPB, HFB, and MOB.

### 3.2. Safety barrier performance assessment model

The failure or performance degradation of complex systems is usually caused by certain internal or external events or behaviors. It is essential to comprehend the mechanism of how the system ensure that things are under control and reacts when things are out of safety range (Liu, 2020). The resilience of the safety barrier determines the state of

![img-0.jpeg](img-0.jpeg)

**Fig. 2.** Event tree of the accident sequence.

The barrier and system. When the safety barrier resilience is large enough, the system can effectively absorb disruptions, quickly adapt and recover to the safe state.

The safety barrier state changes with the disruption intensity, as shown in Fig. 3. The safety barrier resilience is R1. Under the premise that the system keeps itself in a safe state, the maximum disruption intensity that can be withstood is D1, as shown in Fig. 3. When the disruption intensity is less than D1, the safety barrier will be affected by the disruption, but it can still maintain its essential functions. The safety barrier will recover to a stable state whose performance may be higher or lower than the original state (Tong et al., 2020). When the disruption intensity is more significant than D1 and less than D2, the safety barrier is in an unstable state at this time. That is only part of the function can be realized. The safety barrier resilience has been irreversibly affected, and the state of the safety barrier cannot be restored. When the disruption intensity is more remarkable than D2, the safety barrier will ultimately fail, which may cause serious consequences. Resilience is the intrinsic property of a system. It will change only when the system structure changes and its components degrade or upgrade. For instance, with the improvement of a safety barrier, its resilience increases from R1 to R1', then the range of the safe state will be extended from 'Safe' to 'Safe1', which means that the higher the resilience of a safety barrier is, the stronger the ability to maintain the safety state will be.

Each system has its availability. Under normal conditions, the availability of the system decreases over time due to component degradation. Then gradually the system reaches an equilibrium state *A1* at time *t1* (Cai et al., 2018). When a disruption occurs at *t2*, system availability instantaneously drops to the lowest state *A2*. When external maintenance is provided, the system availability increases gradually to a new stable state, *A3* at *t3*. The *f* (*T1*) in Fig. 4 shows that the system availability decreases with component degradation under normal conditions. In contrast, the *f* (*T2*) represents the system availability increase

![img-1.jpeg](img-1.jpeg)

**Fig. 4.** Availability of a system subject to degradation and disruption.

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** Schematic diagram of safety barrier state affected by disruption intensity.

with time under external repair after the disruption. Assuming that if the system is not resilient, the system will run with the availability of $A_{2}$ after disruption, as shown in the $f\left(T_{3}\right)$.

The equilibrium state $A_{1}$ can be calculated by the failure rate under normal conditions. The disruption intensity can determine the lowest state, $A_{2}$. The new stable state $A_{3}$ can be determined by the repair rate and emergency measures. To quantify the resilience of safety barriers, this paper proposes a new metric, which considers the three attributes of resilience, namely absorption, adaptation, and restoration.

In the absorption phase, the ratio of residual availability to initial availability is used to indicate the absorption capacity of the system; In the adaptation and restoration phase, the percentage of the recovery amount of availability to the total amount is introduced to indicate the ability of adaptation and restoration. Therefore, system resilience can be expressed as the sum of these two ratios. The specific analysis is as follows.

Under normal conditions, the system reaches an equilibrium state $A_{1}$ due to the degradation of components, and the availability function concerning time is $f\left(T_{1}\right)$, as shown in Fig. 4. Since the system is in an equilibrium state, $f\left(T_{1}\right)$ is a constant and equal to $A_{1}$. When disruption occurs, system availability instantaneously decreases to $A_{2}$. At this time, the function $f\left(T_{3}\right)$ of availability concerning time is constant. With external maintenance and emergency measures, the system availability gradually recovers to a new stable state, $A_{3}$. The value of $A_{3}$ is determined by the equilibrium state $A_{1}$ and the lowest state $A_{2}$. In this study, $A_{3}$ is defined as the availability when the system recovery amount reaches $90 \%$ (this percentage can be customized) of the loss amount (Tong et al., 2020), as shown in Eq. (1).
$A_{3}=A_{2}+\left(A_{1}-A_{2}\right) * 90 \%$
As mentioned above, in the absorption phase, the capacity of absorption can be presented as Eq. (2).
$A_{b}=\frac{A_{2}}{A_{1}}$
where $A_{b}$ indicates the capacity of the system absorption. The larger the value, the stronger the system's ability to resist disruption, and the better the system's absorption capacity.

The function of system availability during the adaptation and restoration phase is $f\left(T_{2}\right)$. The total amount of availability under normal conditions is shown in Eq. (3):
$S=\int_{t_{1}}^{t_{2}} f\left(T_{1}\right) d t$
where $S$ represents the total system availability.
It is worth noting that the new stable state $A_{3}$ of the system may be smaller or larger than the initial state $A_{1}$. The loss of system availability is $S_{1}$. The availability recovery amount of the system during the adaptation and restoration period is $S_{2}$. The calculation formula of the recovery amount is shown in Eq. (4).
$S_{2}=\int_{t_{2}}^{t_{1}} f\left(T_{2}\right)-f\left(T_{3}\right) d t$
As mentioned above, the expression of resilience-based performance $R_{P}$ of a safety barrier is represented as Eq. (5):
$R_{P}=\frac{\int_{t_{1}}^{t_{2}} f\left(T_{2}\right)-f\left(T_{3}\right) d t}{\int_{t_{2}}^{t_{1}} f\left(T_{1}\right) d t}+A_{b}$

### 3.3. Dynamic Bayesian network

Bayesian networks (BN) consist of qualitative and quantitative parts. The qualitative component is a directed acyclic graph, including nodes representing system variables and a set of directed arcs representing the
dependence or causal relationship between variables. The quantitative part are the prior probability and conditional probability tables (CPTs), representing the conditional dependence between nodes and their parent nodes. The joint probability of a set of random variables $U=\left\{X_{1}, X_{2}, X_{3}, \cdots, X_{n}\right\}$ can be represented as:
$P(U)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)$
where $\pi\left(X_{i}\right)$ stands for the parent nodes of $X_{i}$.
As an extension of BN, a dynamic Bayesian network (DBN) explicitly models the time evolution of a set of random variables on the dis-crete-time axis (Khakzad, 2015). That is, DBN is a special BN, which is a random model that can process time-series data by combining BN and Markov models. DBN is an extension on the time dimension based on BN, to consider the dynamic and time uncertainty caused by a fault (or event) sequence or time change (aging, degradation) when modeling. Each time step in the model is called a time slice, $t-\Delta t$ represents the previous time slice, $t$ represents the current time slice, $t+\Delta t$ represents the next time slice, and $\Delta t$ represents the time slice interval. The solid line directed arc represents the relationship between variables in the same time slice, while the dashed line directed arc represents the relationship between variables in different time slices. The specific structure is shown in Fig. 5.

A DBN can dynamically represent the relationships between causes and consequences through nodes and directed arcs. The specific process of using DBN to calculate resilience can be divided into four steps. (1) According to the repair rate and failure rate of components under the normal conditions, a DBN can be used to calculate the availability of each time slice of the system, and the availability in each time slice can be converted to a system availability function by using fitting technology, namely $f\left(T_{1}\right)$. (2) When the disruption occurs, the failure probability of components increases, which leads to a decrease in system availability. At this time, a DBN can be used to calculate the availability of the system, namely $f\left(T_{3}\right)$. (3) Due to the resilience of the system, the availability of the system will increase with time. In this process, a DBN can be used to calculate the availability of the system in each time slice, and the system available in each time slice can be converted to the system availability function by using fitting technology, namely $f\left(T_{2}\right)$. (4) Eq. (5) can then be used to calculate the resilience of a system.

## 4. Case study

The process of wax oil hydrogenation illustrates the proposed methodology, as shown in Fig. 6. The wax oil is mixed with hydrogen and enters the reactor. The reaction product from the bottom of the reactor is cooled to $30-40^{\circ} \mathrm{C}$ and then enters the high-pressure separator. High-purity hydrogen is generated at the top of the separator. Most of the gas is returned to the reactor as recycled hydrogen. The hydrogenated oil is separated from the middle and lower part of the high-pressure separator and enters the low-pressure separator after decompression. Due to the decrease in pressure, the hydrogen and low-molecular hydrocarbons dissolved in the oil are separated from the oil. The generated hydrogen is desulfurized by the desulfurization tower and then used in the hydrogen circulation system. The oil obtained from the bottom of the low-pressure separator enters the stripping tower, and the gas dissolved in the oil is removed with superheated steam. The gas component is mainly hydrogen sulfide. The oil finally enters the fractionation tower. Various hydrocarbons will be produced at the top of the tower, and multiple products will be produced at the bottom of the tower. The specific process is shown in Fig. 6.

### 4.1. Safety barrier identification and DBN model

To prevent loss of containment and escalation accidents, it is necessary to evaluate the performance of the safety barriers in the

![img-3.jpeg](img-3.jpeg)

**Fig. 5.** Dynamical bayesian network.

![img-4.jpeg](img-4.jpeg)

**Fig. 6.** Schematic diagram of the wax oil hydrogenation process.

process. The first step is to identify the safety barriers and components in the system. In this study, safety barriers are divided into 6 categories. The human factors and management and organizational factors affect the entire process of the system.

Release prevention barrier (RPB): In the process of wax oil hydrogenation, the main secondary barriers of RPB are (i) Human factors barrier (It consists of operational factors and personnel characteristics. Operational procedures and work permits are essential to ensure the safety of the operating process. Skills, experience, and knowledge are the components of personnel characteristics). (ii) Process control barrier. The function of this secondary barrier is to provide warning or information through monitoring (e.g., flow control, temperature monitoring, pressure monitoring, pressure alarm, etc.) or to automatically activate the safety system to prevent loss of containment. (iii) Mechanical barrier. Take anti-corrosion layer protection as an example. It is to prevent loss of containment caused by corrosion and is composed of protective coating and cathodic protection. (iv) Management and organizational barriers. Good daily management (e.g., training, education, and safety culture, etc.), routine protection (e.g., testing and inspection), and maintenance (maintenance procedures and methods, maintenance time) are essential measures to ensure the safety of the process. The specific components of RPB are shown in Fig. 7 and Table 2.

Dispersion prevention barrier (DPB): The function of DPB is to limit the scope and duration of loss of containment to prevent substance accumulation. In the process of wax oil hydrogenation, DPB is mainly composed of three parts, namely a gas detection system (automatic and manual), an emergency shutdown system (automatic and manual), and a ventilation barrier. The specific components of RPB are shown in Fig. 8 and Table 3.

Ignition prevention barrier (IPB): The function of IPB is to eliminate ignition sources in the plant to prevent fire and explosion accidents. When RPB and DPB fail, flammable substances will accumulate in the plant area. Due to the large variety and quantity of ignition sources in the chemical plant area, such as flames and hot works, it will influence equipment and personnel once ignition occurs. To prevent fires and explosions, safety barriers must be applied by focusing on all possible ignition sources existing in a process facility. There are several ignition sources in a process facility, such as flames, hot works, hot surfaces, hot materials and gases, friction and impact, and static electricity sparks (Rathnayaka et al., 2011a,b). In this study, ignition sources are divided into two types, namely flames and hot sources. The hot source is composed of hot works and a hot surface. The specific components of RPB are shown in Fig. 9 and Table 4.

Escalation prevention barrier (EPB): When RPB, DPB, and IPB fail to complete their function, fire and explosion accidents are likely to occur in the plant area. Heat radiation, explosion overpressure can cause catastrophic effects on surrounding equipment and workers. To reduce the consequences of accidents and reduce the damage caused by

![img-5.jpeg](img-5.jpeg)

**Fig. 7.** DBN model for RPB.

**Table 2** Components description of release prevention barrier (RPB).


accident loads, it is necessary to set up a safety barrier to isolate the hazardous source from the surroundings. In this study, the EPB consists of three main secondary barriers: gas mitigation barrier, fire mitigation barrier, and explosion mitigation barrier. The specific components of EPB are shown in Fig. 10 and Table 5.

### 4.2. Performance assessment for the safety barriers

According to the established DBN model of each safety barrier, the availability function of the safety barrier under normal conditions and disruption conditions are calculated, respectively. Under normal conditions, the initial data (i.e., prior probability, failure rate, and repair rate) of safety barrier performance influencing factors are determined by OREDA, relevant literature, and expert judgment (Zarei et al., 2017; CCPS, 1989). However, when the disruption occurs, the failure probability of the influencing factors will be increased. In this study, the evidence theory is introduced to calculate the prior probability of safety barriers' components under the disruption conditions. The specific procedure can be seen in (Mi et al., 2018). The determined data can be seen in Appendix A.

The availability of each safety barrier under normal conditions and disruption are calculated according to the data in Appendix A. The absorption capacity of each safety barrier can be determined by Eq. (2). The specific results are shown in Table 6. Assuming the disruption occurs at time 0. According to the availability of each time slice calculated by DBN, the availability function *f* (*T*2) of each safety barrier under disruption is determined by fitting technology, as shown in Fig. 11.

When a disruption occurs, the availability of each safety barrier decreases dramatically until it reaches the lowest value. The lowest value (*A*2) of each safety barrier is 0.239, 0.455, 0.178, and 0.642, respectively, as shown in Table 6. The smaller the *A*b, the more significant the decline in availability, the weaker the absorption capacity of the system, and the more susceptible it is to disruption. However, the resilience of a system depends not only on its absorption capacity but also on its capability of adaptation and restoration. Taking RPB as an example, although RPB's *A*2 is small, the availability of the system is restored to a relatively stable state in a short time, which is faster than in case of the other three safety barriers, as shown in Fig. 11 (a−d). To comprehensively evaluate the resilience of the safety barrier, the performance of the safety barrier is expressed as the sum of absorption, adaptation, and restoration capacity, as shown in Eq. (5). The resilience–based performance (R*P*) of each safety barrier can be calculated by Eqs. (1)–(5) and the availability function in Fig. 11. The results are shown in Fig. 12.

It can be seen from Fig. 12 that the EPB has a good resilience–based performance. Although it takes a relatively long time to recover to a stable state, its excellent adaptability can effectively resist the disruption. The performance of DPB is stronger than that of RPB. From the 9th to the 28th hour, the resilience of DPB is slightly lower than that of RPB. At other times, the resilience of DPB is significantly larger than that of RPB, and the stable state is higher. The lowest performing safety barrier is the IPB, whose absorption capacity, recovery speed, and final state are significantly lower than the other three safety barriers. It means that when the disruption occurs, the impact on IPB is larger than that of RPB, DPB, and EPB. When the disruption occurs, the RPB and DPB have a specific ability to prevent accidents from evolving into secondary

![img-6.jpeg](img-6.jpeg)

**Fig. 8.** DBN model for DPB.

**Table 3** Components description of dispersion prevention barrier (DPB).


accidents. However, if a secondary accident occurs (e.g., massive gas dispersion), due to the poor performance of the IPB, the probability of the secondary accident evolving into a fire and explosion accident is high. To prevent this from happening, the structure and repair rate of IPB should be strengthened, and the failure rate of components should be reduced. In this way, the resilience-based performance of the safety barrier can be increased to withstand greater disruption intensity, as shown in Fig. 3.

According to the resilience of each safety barrier, the integrated resilience of the safety barrier system can be calculated, as shown in Fig. 13. The total safety barrier system needs 96 h to reach a stable state, and it takes longer than RPB and shorter than DPB, IPB, and EPB. Its final resilience is 0.776, which is smaller than DPB and EPB and larger than RPB and IPB. It can be seen from Figs. 12 and 13 that the resilience-based performance of a safety barrier system depends on each safety barrier. To prevent accidents and escalation, it is necessary to strengthen the structure of each safety barrier to improve the resilience-based performance of the safety barrier system.

![img-7.jpeg](img-7.jpeg)

**Fig. 9.** DBN model for IPB.

Table 4 Components description of ignition prevention barrier (IPB).


## 5. Discussions

### 5.1. Sensitivity analysis

It is essential to conduct a sensitivity analysis to test the robustness of a new methodology. For a robust model, the results acquired from the model are sensitive, but would not show sudden trend changes to any small change in input parameter (He et al., 2018). Taking EPB as an example, sensitivity analysis is carried out by changing the failure rate, and repair rate of node $\mathrm{X}*{3}, \mathrm{X}*{6}, \mathrm{X}*{7}$, and $\mathrm{X}*{8}$. Fig. 14 (a) represent the resilience values with the changes of the failure rates from 0.5 times to 2 times of the components. It can be seen that when the failure rate increases, there is a slight decrease in resilience. Fig. 14 (b) represents the resilience values with the changes in the repair rates from 0.5 times to 2 times the components. It can be seen that when the repair rate increases, the trend of resilience is increasing. The increase in failure rate has less impact on safety barrier resilience than the maintenance rate. It means that the factory can improve the maintenance rate to increase the safety barrier system's resilience. The results show that when the failure rate and repair rate change, the resilience trend does not change, which verifies the model.

In Fig. 15, the three lines are final steady resilience with different node failure probabilities. The red line indicates the original system resilience (i.e., without any change in node failure probability). The black line represents the impact on system resilience after the failure probability of each single node is reduced by $10 \%$. The blue line shows the impact on system resilience after the failure probability of each single node is increased by $10 \%$. Fig. 15 indicates that when the failure probability of a single node decreases, the resilience of the system increases. Besides, in the light of Eq. (5), the results show that the system's ability of absorption increases, which means that the system's ability to withstand disturbance becomes stronger. Take node 3 as an example, when the failure probability is decreased to $90 \%$, the system's ability of absorption increases from 0.656 to 0.692 , and the change of adaptation and restoration ability is slight. When the failure probability rises to $110 \%$, the system ability of absorption decreases from 0.656 to 0.619 , and adaptation and restoration ability change slightly. It can be seen that the change of the failure probability of node 3 has the greatest impact on system resilience, followed by node 5 . The rest of the nodes have slight influence on system resilience. Therefore, Fig. 15 can be utilized to support decision-making in resource (e.g., human resource, money, time, policy, etc.) allocation to ensure systems under control before, during, and after disruptions. Compared with the traditional static indicator assessment method, the proposed method can not only find the critical nodes in the system, but also help to support decisionmaking.

Table 5 Components description of escalation prevention barrier (EPB).


Table 6 The absorption capacity of each safety barrier.

|  Safety
barrier | Availability under
normal condition $\left(A_{1}\right)$ | Availability when
disruption occurs $\left(A_{2}\right)$ | Absorption
capacity
$A_{0}$  |

![img-8.jpeg](img-8.jpeg)

Fig. 10. DBN model for EPB.

![img-9.jpeg](img-9.jpeg)

Fig. 11. The availability function of (T2) of each safety barrier.

![img-10.jpeg](img-10.jpeg)

Fig. 12. The resilience of each safety barrier.

![img-11.jpeg](img-11.jpeg)

Fig. 13. The integrated resilience of the safety barrier system.

(1) The safety barriers are divided into 6 categories (e.g., RPB, DPB, IPB, etc.) based on their functions instead of attributes (i.e., passive barrier, active barrier, procedural barrier, which are shown in Table 1). This classification makes each safety barrier

### 5.2. Strength of the resilience-based method

Compared with the traditional methods for safety barrier evaluation, this method has the following strength:

![img-12.jpeg](img-12.jpeg)

**Fig. 14.** Sensitivity analysis of EPB: (a) time-dependent resilience change with failure rate; (b) time-dependent resilience change with repair rate.

![img-13.jpeg](img-13.jpeg)

**Fig. 15.** Effects of failure probability on system resilience.

more specific to be assessed, which leads to a more comprehensive assessment.

(2) DBN is used to develop the performance assessment model for safety barriers, which can represent the interdependence and interaction between components in a complex system. Compared with traditional methods (e.g., BowTie model, Analytic Hierarchy Process), the proposed approach is more suitable to deal with uncertainty in a complex system.

(3) Traditional methods only assess the performance of safety barriers under normal situation. In this paper, evidence theory is utilized to determine the failure probability of each component under disruption situation to dispose of data uncertainties. Therefore, the proposed approach evaluates the performance of the safety barriers under two different situations (i.e., normal and disrupted situations), making the results more objective.

(4) Safety barriers are evaluated based on how resilient they are. This expands the scope of the performance evaluation to cover the pre-failure, amid-failure, and post-failure stages of a safety barrier. The restoration capability of a safety barrier is considered.

(5) The performance determined by the traditional method is usually a static value, which cannot quantify the change of the system state under different disruptions. The proposed method can present the changes in system performance over time and quantify the impact of different intensities of disruption on the system.

### 6. Conclusions

Previous studies have proposed a variety of static metrics to evaluate the performance of a safety barrier. For a highly complex engineering system, internal and external disruptions are uncertain and emergent. To overcome the shortcomings of the traditional performance assessment method and dynamically evaluate the safety barrier performance, a resilience-based performance assessment method is proposed. The evidence theory is used to determine the failure probability of basic events under the disrupted condition to deal with the uncertainties associated with experts' judgements. The DBN is used to calculate the availability function of each safety barrier under two different conditions (i.e., normal condition, and under disrupted condition). In the light of the safety barriers' availability functions under two different conditions, the resilience-based dynamic performance can be determined by the proposed resilience metric. The proposed method can be used to find the vulnerable element of each safety barrier and evaluate the performance and resilience of each safety barrier and, finally, the safety barrier system under two different conditions. Taking targeted measures to improve the resilience-based performance of the safety barrier system, especially RPB and IPB, will effectively prevent accidents and escalations.

This study reveals the importance of dynamically assessing the performance of safety barriers and including their capability to absorb, adapt to, and recover from disruptions in the performance assessment. Unlike previous studies, with resilience thinking, safety measures can be extended to recovery, which means that traditional assessment method is not as wide as that of the proposed methodology. Replacing failure/reliability thinking by resilience thinking in safety barrier performance assessment, a system's absorption, adaptation and restoration can be improved to mitigate the influences of disruptions and ensure system safety. In the light of the uncertainty of disruption in process systems, resilience-based performance assessment is an ideal method to decrease performance losses of the system. The adverse consequences can be prevented by taking targeted measures to enhance the performance of safety barriers. It has a particular engineering significance for assessing the performance of the safety barrier system and preventing accidents.

### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

The authors gratefully acknowledge the financial support provided
by the National Key R\&D Program of China (No: 2019YFB2006305) and the Central Universities Fundamental Research Funds Project (YCX2021077).

# Appendix A 

## Appendix A1

The data of RPB


${ }^{\text {a }}$ Success (S).
${ }^{\mathrm{b}}$ Failure (F).
${ }^{\text {c }}$ Probability under the disruption (DPr).
${ }^{\text {d }}$ Probability under the normal conditions (NPr).

## Appendix A2

The data of DPB


## Appendix A3

The data of IPB


Appendix A3 (continued)


# Appendix A4 

The data of EPB


## Author statement

Hao Sun: Writing - review \& editing, Writing - original draft, Investigation, Formal analysis, Methodology, Conceptualization. Haiqing Wang: Supervision, review, editing Project administration, Funding acquisition. Ming Yang: Methodology, Formal analysis, Investigation, Writing - review \& editing. Genserik Reniers: Writing - review \& editing, Visualization.
