# Universiteit <br> Leiden <br> The Netherlands 

## Development of fragility models for process equipment affected by physical security attacks

Marroni, G; Casini, L.; Bartolucci, A; Kuipers, S.; Casson Moreno, V; Landucci, G.

## Citation

Marroni, G., Casini, L., Bartolucci, A., Kuipers, S., Casson Moreno, V., \& Landucci, G. (2023). Development of fragility models for process equipment affected by physical security attacks. Reliability Engineering \& System Safety, 243.
doi:10.1016/j.ress.2023.109880

Version: Publisher's Version
License: Licensed under Article 25fa Copyright Act/Law (Amendment Taverne)
Downloaded from: https://hdl.handle.net/1887/3716802

Note: To cite this publication please use the final published version (if applicable).

# Development of fragility models for process equipment affected by physical security attacks 

Giulia Marroni ${ }^{\mathrm{a}}$, Leonardo Casini ${ }^{\mathrm{a}}$, Andrea Bartolucci ${ }^{\mathrm{b}}$, Sanneke Kuipers ${ }^{\mathrm{b}}$, Valeria Casson Moreno ${ }^{\mathrm{a}}$, Gabriele Landucci ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Department of Civil and Industrial Engineering - University of Pisa, Largo Lucio Lazzarino n.2, 56126 Pisa, Italy<br>${ }^{\mathrm{b}}$ Institute of Security and Global Affairs, Faculty of Governance and Global Affairs, Leiden University, Wijnhaven, Turfmarkt 99, 2511 DP, Den Haag, the Netherlands

## A R T I C L E I N F O

Keywords:
Security Vulnerability Assessment
Bayesian Networks
Fragility models
Major accident hazard
Security management
Physical Protection System

## A B S T R A C T

The vulnerability of chemical and process facilities toward physical security attacks depends on the equipment resistance against such attacks and on the performance of Physical Protection Systems (PPS) in place. To enhance the protection against intentional attacks, the development of quantitative vulnerability metrics is essential, nevertheless current standard approaches only offer qualitative or semi-quantitative evaluations. The aim of the present work is to develop a quantitative methodology for the assessment of chemical and process facilities vulnerability towards external acts of interference. The proposed methodology is based both on the evaluation of equipment structural integrity in response to different types of specific impact vectors characterizing intentional attacks and on the quantitative performance assessment of related PPS. In particular, specific fragility models were developed for impact vectors associated with improvised explosive devices, firearms, and incendiary weapons. The novel fragility models were implemented in a comprehensive security vulnerability assessment (SVA) based on Bayesian Networks, in which the contribution of PPS performance was also considered. A case study was defined and analyzed to exemplify the application of the proposed approach. The results obtained allowed for the identification of the most critical security-related escalation scenarios and thus for an improved quantitative SVA.

## 1. Introduction

Security science is a relatively new field that has expanded considerably since the terroristic attacks in New York on September $11^{\text {th }}, 2001$. The process industry is not unrelated to security matters. Actually, chemical facilities, where relevant quantities of hazardous chemicals are stored or processed, may become possible targets of acts of interference and terroristic attacks [1]. Security concerns for chemical facilities revolve around both physical and cyber-attacks, as demonstrated by available analyses of intentional attacks occurred in recent years [2,3]. Besides, global affairs show that the risk of attacks at industrial infrastructures and chemical facilities is ubiquitous as part of violent conflicts in highly industrialized regions.

There have been a number of global and regional measures to address security issues. The CBRN (chemical, biological, radiological and nuclear) Risk Mitigation and Security Governance Programme was launched by the United Nations Crime and Justice Research Institute in 2004 to promote the co-operation and co-ordination between countries,
international and regional organizations [4]. The government of the United States merged several federal organizations under the Department of Homeland Security in 2002 to create a comprehensive strategy against terrorism [5]. The Chemical Facility Anti-Terrorism Standards (CFATS) was established in 2007 and it is the first regulatory program that specifically focuses on the security of chemical facilities storing hazardous substances in the US [6]. In Europe, the directive 2018/114/EC was established as a result of the "European Programme for Critical Infrastructure Protection" (EPCIP) [7] and regulates the prevention, protection and response to terroristic attacks involving the energy and transport sector; the regulation EC No 725/2004 [8] enhances the security of international ports and shipping facilities. However, the European Seveso Directive III [9] concerning major accidents hazard for industrial installation does not address the need for a security-related analysis or countermeasures.

Nonetheless, security standards such as the API/ANSI Std 780 [10], the CCPS guidelines for the evaluation of security vulnerabilities and security vulnerability analysis (SVA) [11], the Sandia model for the vulnerability of physical protection systems (VAM-CF) [12] can provide

[^0]
[^0]:    * Corresponding author.

    E-mail address: gabriele.landucci@unipi.its (G. Landucci).
    https://doi.org/10.1016/j.ress.2023.109880
    Received 8 April 2022; Received in revised form 16 October 2023; Accepted 9 December 2023
    Available online 17 December 2023
    0951-8320/© 2023 Elsevier Ltd. All rights reserved.


guidance to analysts and plant managers. Matteini et al. [13] made an extensive analysis and determined that all the cited above methodologies have a common background and structure, yet also differ in important ways. While API and the VAM-CF follow a scenario-based approach, the CCPS guidelines suggest both a scenario-based and an asset-based approach. Although API Std 780 has the most straightforward application, the VAM-CF has a higher potential for a complete analysis since it also includes cyber-security risks.

However, the aforementioned standards only offer a semiquantitative evaluation of vulnerability and security risk, meaning that numerical values are assigned, but they represent approximate results instead of exact or absolute ones [14] Moreover, as observed by Cox [15], previous approaches to security are linear: they do not take into consideration the interdependencies of each factor affecting the
security risk.
Quantitative techniques in the framework of risk assessment provide a realistic numerical estimate [14], and can guide analysts in identifying weaknesses of process facilities, thus overcoming the limitations of semi-quantitative techniques. Recent studies addressed this aspect developing quantitative Security Vulnerability Assessment (SVA) methods dedicated to both critical infrastructures [16,17] and chemical installations [18-22]. Given the necessity to combine different types of information and the need to take into account mutual interactions between parameters, these studies adopted advanced probabilistic models, such as Bayesian Networks (BN), but only focused on the evaluation of the Physical Protection Systems (PPS) in place and, more in general, on the evaluation of security countermeasures performance in securing facilities against external attacks. However, the comprehensive

assessment of vulnerability in the framework of chemical and process installations also entails the evaluation of equipment resistance in terms of damage probability in case of successful attack.

Equipment vulnerability or fragility models are used to assess the probability of damage given a specified physical impact vector [18]. Recent works developed novel vulnerability models for equipment exposed to simultaneous fires and explosions based on evaluation of the total stress on the equipment shell [23,24]. Other works studied different ways to model consequences of domino effects and the interactions among different equipment [25-29]. However, to the best of the Authors' knowledge, fragility models tailored to the specific needs of assessing the impact of security attacks and suitable for quantitative security analyses are still lacking.

The aim of the present work is to develop a quantitative methodology for SVA implementing a comprehensive set of equipment fragility models for the assessment of physical attack scenarios, i.e., intentional attacks that need a physical intrusion and/or physical weapons to cause damage to a target. With respect to existing literature, fragility models were developed for impact vectors associated with improvised explosive devices, firearms, and incendiary weapons, and they were integrated for the first time into a comprehensive SVA. The idea behind this work was to build a quite simple approach for the assessment of damage probabilities that could provide robust and conservative results to be implemented into a security assessment. Indeed, the physical models associated with the attack vectors were simplified, as the final focus of the work was to obtain correlations for damage probability for different security scenarios, rather than describing the detailed mechanical behaviour of the process item. The developed models feature a simplified evaluation of the dose of physical effect. In this way, the models can be implemented in quantitative SVA without requiring input parameters that may be difficult to retrieve.

The SVA of the present work was based on a probabilistic model based on BN in order to provide an accurate estimate of vulnerability for security scenarios in the specific framework of chemical and process facilities, where also the performance of the PPS in place was considered. In fact, BN allow for the full characterization of the vulnerability of a given asset as they can include a great number of factors, their interdependencies, and allow for the continuous update once new evidence enters the network. Thus, BN are an appropriate tool for SVA, which has been already widely used to analyze process facilities [1,27,30-33].

To demonstrate the soundness of the developed BN and the contribution of equipment fragility evaluation, a sensitivity analysis has been conducted assessing the variation of vulnerability by modifying significant parameters of the fragility models developed. In order to test the potentialities of the present approach, an industrial case study was analyzed. The results identified the critical elements of a security attack to specific targets, highlighting the role of security countermeasures and equipment fragility. Thus, the tools and methods presented in the work could be exploited by plant managers to prioritize the resources available for security investments and to identify weaknesses in the analyzed installations.

## 2. Theoretical background on vulnerability assessment

### 2.1. Key concepts: vulnerability and security vulnerability assessment (SVA)

Aven [34] defines vulnerability as a fault or weakness that reduces or limits a system's ability to withstand a threat or to resume a new stable condition. Johansson et al. [35] include endogenous risks, stating that vulnerability is the inability of a system to withstand strains and the effects of failure. Haimes [36] goes one step further and describes vulnerability as the manifestation of the inherent states of the system that can be exploited to adversely affect that system. This last definition is more appropriate for a security framework, given that it includes the possibility of an external threat exploiting endogenous weaknesses.

Two major considerations need to be accounted for when referring to security of industrial infrastructures and chemical installations: i) the ability to recover the desired values of the states of a system that has been attacked, within an acceptable time period and at an acceptable cost, ii) the ability to reduce the effectiveness of the attack (and thus its probability of success) by actions such as detection, prevention, protection, interdiction, and containment, which are functions implemented by security barriers [36].

Therefore, the vulnerability of a chemical and process facility is defined in this work as any property of the system that can be exploited to perform a successful attack. This definition is in agreement with the risk formulation proposed by API/ANSI Std 780 [10]:
$R_{S}=T \cdot A \cdot V \cdot C$
in which security risk $\left(R_{S}\right)$ is intended as the likelihood that a threat $(T)$ will consider attractive a specific asset $(A)$ and will successfully commit an act against it, taking advantage of its vulnerability $(V)$ to cause a given set of consequences $(C)$, as per Eq. (1).

Vulnerability is, therefore, a key concept for the management of countermeasures in security science. SVA may be considered a useful managerial tool to support informed decision making to enhance security of an installation/site [37]. The identification of elements that could represent a weakness for the installation is a necessity when conducting a quantitative SVA [10,38]. To this purpose the performance of the security barriers should be firstly considered. An SVA should therefore include a systematic evaluation of the PPS components effectiveness, with the aim of providing an evaluation of the overall security system [12]. Such an evaluation also allows for the identification of critical PPS functions that may need improvement, as well as additional measures to be implemented. More details on PPS performance are provided in Section 2.2. Secondly, the structural resistance of targets to specific impact vectors characterizing security attacks should be quantified, and this has never been taken into consideration before in SVA framework. In this perspective, vulnerability assumes the meaning of fragility and fragility models are used to quantitatively assess the physical damage to targets (see Section 2.3).

### 2.2. PPS performance and reference data

This section outlines the theoretical background to mathematically model and quantify the performance of PPS to be implemented in the Bayesian Network to carry out the SVA.

A PPS integrates people, procedures, and equipment for the protection of assets or facilities against theft, sabotage, or malicious attacks [38]. According to Garcia [38], PPS can be characterized according to four functions:

- Detection: it includes intrusion detection and the consequent alarm assessment. First, a sensor detects an intrusion and triggers the alarm; the information detected is reported and shown to the security staff which evaluates its credibility;
- Delay: this element aims at slowing down the adversary's progress towards the target through the introduction of barriers in order to provide additional time to respond;
- Response: it is the adversary interruption and threat neutralization.
- Deterrence: it decreases the facility attractiveness and convinces the adversary not to attempt an attack

The deterrence function is too difficult to measure, given that it relies on the perception of the threat and is therefore not a reliable source for adversary interruption [38]. For this reason, it is not considered in this study, which means that conservatively no action can be taken to prevent the attack.

It is important to point out that the PPS functions are highly

dependent on the path chosen by the threat to perform the attack, as it is hereby shown.

Quantitative metrics for physical protection systems effectiveness proposed by Sandia SVA Model were adopted in this study to evaluate the performance of PPS [12]. All the three functions (detection, delay, and response) shall be performed in sequence and within a time lapse that is shorter than the time required by the adversary to complete their task.

The probability of interruption $P_{I}$ is expressed as:
$P_{I}=P_{D} \cdot P_{U} \cdot P_{T}$
where $P_{D}$ is the probability of successful detection, $P_{\mathrm{C}}$ is the probability of communication to and among the emergency response team, and $P_{T}$ is the probability of timely intervention from the emergency response team.

This work follows a previous approach from Argenti et al. [39] who developed a methodology that offers quantitative data of PPS performance. Experts from the industry were involved to determine variables and influencing factors of security functions. The probability of success of each element of the PPS is defined as:
$P_{P P S}=P_{U} \cdot \prod_{i=1}^{J} X_{i} \cdot F_{i}$
where $J$ is the number of factors that independently affect the performance of the security barrier, $P_{0}$ is the conditional probability of the security barrier successfully performing its function if all factors are in the favorable state, $F_{i}$ is a parameter that measures how a factor in an unfavorable state affects the performance of the security barrier, and $X_{i}$ $=I$ if the $i$-th factor is in the unfavorable state, or $X_{i}=I / F_{i}$ if the factor is in the favorable state. By means of expert elicitation, Argenti et al. [39] gathered specific data both the baseline probability $P_{0}$ and impact factors $F_{i}$ for different types of security barriers and PPS elements.
$P_{D}$ can be quantified using the methodology described above. Namely, to obtain $P_{D}$ given a certain path, at least one of the security barriers must detect the intrusion, which means considering an OR operator among the different detection barriers. $P_{\mathrm{C}}$ can be as well assessed using Eq. (3). Instead, $P_{T}$ expresses the probability of evolution in time of the attack. The mean adversary intrusion time $\left(t_{P}\right)$ is calculated taking into consideration the time to walk $\left(t_{w}\right)$ and the delay caused by the barriers and operations to carry out $\left(t_{d, i}\right)$ on their path:
$t_{P}=t_{w}+\sum_{i=1}^{M} t_{d, i}$
where M is the number of delaying barriers encountered by the adversary on the attack path (e.g., fences, perimetral walls) and operations to be carried out to reach the target and complete the attack (for instance placing and detonating an explosive device). Garcia [12] reports numerical data on running speeds and delay times for different barriers, along with additional information on their statistical distribution: for example, the time needed to cut a fence using pliers is on average 120s, with a standard deviation of 49.2 s .

Assuming a normal distribution for both $t_{P}$ and emergency response team time $\left(\mathrm{t}_{E R T}\right), P_{T}$ is calculated as:
$P_{T}=\frac{1}{\sqrt{2 \pi \cdot\left(\sigma_{E R T}^{2}+\sigma_{P}^{2}\right)}} \cdot \int_{0}^{\infty} e^{\left(\sqrt{\tau_{E R T}^{2}+\tau_{P}^{2}}\right)} \cdot d t$
where $\sigma_{P}^{2}$ and $\sigma_{R F T}^{2}$ are the variance of $t_{P}$ and $\mathrm{t}_{E R T}$ respectively, and $t^{*}$ is the difference between $t_{P}$ and $t_{E R T}$.

It must be noted that all equations above must be applied to a specific adversary path. It is important to check beforehand the possible barriers for each possible path the adversary might choose.

### 2.3. State of the art on fragility models for equipment

Since the ' 90 s , the concept of fragility model and, more specifically, of fragility curves has been adopted in the field of risk analysis. According to Singhal, fragility describes the probability of exceeding a certain level of damage to an infrastructure given a specific impact vector [40]. This approach has been adopted for the study of the behavior of different types of structures to earthquakes [41-45] as well as other extreme natural hazards [45-50].

The definition from Singhal [40] is hence adopted in this study by generalizing the damage cause to physical effects associated to security scenarios. In this framework, vulnerability assumes the connotation of fragility, in order to evaluate the resistance of a target to a given amount of physical effect.

An effective approach to model the probability distribution of damage is to utilize simplified relationships, such as the probit regression, which is a non-linear regression method typically used for dichotomous outcome variables [55]. In the present study, the variable is the damage of the equipment, and the possible outcomes are the mutually exclusive statuses called "damaged" and "not damaged".

Probit models have found extensive application in safety risk assessment studies to evaluate health damages on humans [56] and to study domino effect propagation among process facilities [57]. The ease of application and the widespread use in the framework of quantitative safety studies make probit models an appropriate form of fragility models to be developed for security scenarios.

In the following, a brief review of equipment fragility models is provided in order to show the limitations in their implementation in the framework of quantitative security analyses and quantitative risk assessment (QRA) studies devoted to chemical and process facilities. Table 1 reports a summary of the main literature approaches.

Engineering systems typically exhibit complex nonlinear behaviors [58] and methodologies have been proposed in the literature to account for statistical uncertainties, inaccurate model forms and/or missing variables [59,60]. In the framework of QRA, however, simplified vulnerability models like the ones in Table 1 are usually adopted, as they require a limited number of input parameters. The use of simplified models reduce the calculation time for security escalation assessment, since QRA procedures involve the analysis of a high number of accidental scenarios even after an initial screening. Clearly enough, the better the fragility model is, the more accurate the QRA results are. Nevertheless, to the aim of a practical use of QRA by industrial practitioners, simplification is needed to reduce time and costs of the analysis, given that the results obtainable by a certain approach have to be conservative.

### 2.3.1. Equipment fragility models for damage caused by fragments

Fragments typically originate from storage or process vessels as a consequence of a catastrophic rupture [57]. The projection of fragments can be divided into three main phases: fragment generation, ejection and impact. Tugnoli et al. [61] provided an extensive review for both descriptive and probabilistic models of each phase. In the framework of security, fragment projection is not a direct attack mode that attackers would exploit. It might become relevant when taking into consideration the domino effect of a successful intentional attack; however, this scenario is outside the scope of this study. Nevertheless, bullets can be seen as a type of fragment ejected from a firearm impacting a target by puncturing. The models available to describe the behavior of fragments generated by the catastrophic failure of process equipment are not suitable for bullets given the difference in the characteristic length with respect to conventional fragments. Still, the perforation of a shell of a process equipment by means of a bullet could cause a leak, leading to the loss of containment of potentially hazardous chemicals. However, no fragility model has been yet integrated into a framework for SVA for process plants considering the role of PPSs. A recent work [62] reviewed perforation models for different types of bullets and investigated their

Table 1 Summary of fragility models based on probit relationships available in literature for relevant impact vectors. Y: probit variable, ttf: time to failure (s), I: radiation intensity $\left(\mathrm{kW} / \mathrm{m}^{2}\right), \mathrm{c}$ : equipment volume $\left(\mathrm{m}^{3}\right)$; $\alpha$ coefficient depending on equipment type; $\Delta \mathrm{P}$ : static overpressure peak (Pa).


accuracy by comparison with experimental data, build a repository of perforations models. The models adopted in this study are present in the review [62] and their compatibility was therefore confirmed. Still, the review [62] revealed that other models might be suitable to develop a fragility model for different types of bullets. In this sense, the framework developed in this work can be still used even with the application of other perforation models.

### 2.3.2. Equipment fragility models for damage caused by fires

The assessment of probability of failure of equipment induced by fires is of primary importance when dealing with the assessment of domino effect scenarios [57]. Landucci et al. [51] developed a fragility model based on the detailed simulation of vessel behavior to fire, carried out through a lumped model. The lumped model is based on the "thermal nodes" approach [63], based on the subdivision of the system under analysis in a limited number of nodes. In each node, the solution of heat and material balances allows for the evaluation of wall temperature and internal pressure. The failure of the equipment takes place when the equivalent stress reaches the maximum allowable stress. The lumped model offers a simplified approach for the evaluation of the time to failure ( $t t f$ ) of equipment, which in turn, is adopted in the fragility model shown in Table 1 (Model 1) for atmospheric and pressurized equipment.

More recently, Zhou et al. [52] defined a methodology to evaluate the $t t f$ of equipment exposed to multiple fires, taking into account the time at which the different secondary fires start or are extinguished. The thermal dose was therefore changed, while the same probit equation as in Landucci et al. [51] has been adopted (see Model 2 in Table 1).

In the context of security-related scenarios, an incendiary weapon could be used to concentrate a high heat load on a restricted portion of the surface of a chemical equipment. This might significantly alter the physical properties of the construction material, leading to material damage and equipment failure. However, to the best of the Authors' knowledge, incendiary weapons have never been considered as a source of heat radiation in the development of fragility models.

### 2.3.3. Equipment fragility models for damage caused by overpressure

Explosions triggered by external acts of interference may cause extensive damage to process facilities. Relevant overpressure impact may be caused by the detonation of military explosives (such as trinitrotoluene, TNT) or Improvised Explosive Devices (IED in the following) [37]. The probability of failure of equipment due to overpressure has been studied by several authors as shown in Table 1. Miura et al. [64] developed a methodology to account for the role of dikes in the mitigation of overpressure effects. Landucci et al. [65]developed a specific methodology to study the effect of IED using a TNT-equivalent charge of explosive.

Although the approaches mentioned above are quite consolidated in literature, their integration to support the probabilistic assessment of security-related scenarios was never undertaken to the best of Authors' knowledge.

## 3. Methodology and tools

### 3.1. Overview

Fig. 1 shows the steps of the methodology proposed in this study to support the security vulnerability assessment using improved fragility models.

The first step of the methodology (Step 1 in Fig. 1) consists in the identification of physical attack vectors relevant for process facilities. For this purpose, past accident data gathered by Casson Moreno et al. [2] were adopted. Out of a total of 300 collected events, 26 events had enough details to allow Casson Moreno and coworkers to analyze the dynamics of the attacks; the most exploited weapons were explosives ( 11 out of 26 events), firearms ( 6 out of 26 events) and incendiary devices ( 5 out of 26 events) [2]. 10 out of 11 attacks with explosives were able to breach inside the facility; 3 out of 5 arson attacks reached warehouses and tank farm, while only a single attack reached the actual processing part of the facility; finally, 5 out of 6 attackers with firearms were able to reach the process plant [2]. This analysis highlights the damage potential of attacks carried out using these weapons. Thus, this study focused on explosives, firearms, incendiary weapons, and fragility models tailored for the specific case of security assessment.

In Step 2, fragility models for the identified attack vectors have been developed. For firearms and incendiary devices (Steps 2.1 and 2.2 in Fig. 1, respectively), the dose of physical effect has been identified deriving probit relationships. To evaluate the mitigated impact of explosives, conventional approaches have been integrated in Step 2.3 of Fig. 1.

The fragility models developed have been used in combination with PPS performance in Step 3 to evaluate the vulnerability of targets and the overall likelihood of attack success. Bayesian Networks (BN) have been exploited as a probabilistic assessment tool to cope with the integration of fragility models and the performance of PPS.

Step 4 is the application of the BN approach to a demonstrational case study. Step 4.1 consists of a baseline vulnerability assessment, in which the vulnerability obtained with the improved fragility models is compared against the vulnerability obtained using conventional approaches. Lastly, a sensitivity analysis is performed in Step 4.2 to investigate the changes in vulnerability with key input parameters.

### 3.2. BN implementation

BN are adopted in this work to conduct a scenario-based probabilistic vulnerability assessment. BN are graphical methods of reasoning under uncertainty using probabilities; they consist of the following elements [66]: i) a set of variables, called nodes, and ii) a set of directed edges, called arcs, between the variables. Nodes with arcs directed from them are called parents, while nodes with arcs directed to them are called children; the presence of parent and children nodes means that nodes together with arcs form an acyclic directed graph. In other words, it is

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** Flowchart of the methodology for vulnerability assessment developed in the present work

impossible to follow the arcs and form a closed loop.

Given a set of *U* = {*G*1, *G*2... *G*n} variables, BN specifies a unique joint probability distribution *P*(*U*), given by the product of all conditional probabilities of each parent node, as in Eq.6):

$$P(U) = \prod_{i=1}^{n} P(G_i)Pa(G_i) \tag{6}$$

where *Pa*(*G*i) is the parent set of variable *G*i.

One advantage of BN is the possibility to include a wide amount of data and complex inter-dependencies into the analysis; moreover, BN make use of Bayes' Theorem to update the probability of children nodes once new evidence *E* is available for parent nodes, as shown in Eq. 7:

$$P(U|E) = \frac{P(U \cap E)}{P(E)} = \frac{P(E|U) \cdot P(U)}{P(E)} \tag{7}$$

This property is convenient in a security framework because the network can be updated in real time once new evidence is shown, e.g., an attack path or the use of a given weapon.

In this study, the software GeNle Modeler by Bayesfusion, LLC [67] has been used to quantify the BN. Each variable of the network is assumed to be described by discrete states. Thus, the so-called chance nodes have been used on GeNle Modeler to quantify the variables involved in SVA. Chance nodes are quantified by filling a conditional probability table, in which the probability in each discrete state is assigned depending on the state of the parent nodes.

Fig. 2 shows the structure of the BN developed for the present study, highlighting the specific nodes and novel aspects of the present analysis. An example of the full BN model developed is shown in Section 5.3 for the analysis of a specific case study. Compared to previous works [18] dealing with SVA based on BN, the BN developed in this work includes additional connections among nodes with the aim of better capturing the aspects related to a possible intrusion in a chemical facility. For instance, this work considers that the attack mode causes additional delay on the attacker, e.g., the time needed to operate an incendiary weapon. Moreover, the same intrusion point and path can be followed for different attack modes. These assumptions add another degree of complexity to the BN. In fact, the conditional probability table for timely intervention of PPS (N3.1) needs to be quantified taking into consideration the attack mode as well, as shown in Fig. 2 with the dashed line between N1.1 and N3.1.

Another key aspect introduced in the BN is that the damage to assets that are not direct targets of the attack has been considered; referring to Fig. 2, if the targets T1 and T2 are reasonably near, then T1 could be damaged even if T2 is the primary target of the attack.

Node N1.1 specifies the attack mode and has been quantified assuming that all attack modes have the same probability of being chosen. Regarding the intrusion path (N1.2), all paths compatible with a single attack weapon and target have the same possibility of being chosen. Nodes N2.1 to N2.2 are related to the attractiveness of the targets and their quantification is based on the values suggested in API Std 780 [10].

To quantify the performance of PPS (Nodes 3.1 to 3.5), the approach described in Section 2.2 has been used. Numerical values have been retrieved from the reference work of Garcia [12] and Argenti et al. [39]. The probability of PPS effectively preventing an intrusion (N3.4) can only happen if all three functions (Intrusion Assessed Detection, Alarm Communication and Timely Intervention) happen in sequence.

As highlighted in Fig. 2, a crucial element of the BN is the implementation of the improved fragility models developed in the present study for escalation triggered by explosion, firearms and arson attack (see Section 4). However, in order to show the influence of fragility on overall vulnerability, the results have then been compared with conventional fragility models and assumptions implemented in previous studies dedicated to the assessment of the escalation of domino effect (see Section 2.3). In particular, the conventional approaches ignore the overpressure mitigation associated with the presence of bunds or dikes and consider the probability of firearms damage as unitary. The model from Landucci et al. [51] introduced in Section 2.3.1 (Model 1 in Table 1) has been used to evaluate the damage caused by heat radiation of incendiary devices.

Further details on the BN are introduced in Section 5 for the SVA of a specific case study.

### 4. Development of improved fragility models for security scenarios

Improved fragility models tailored to intentional attack modes to process equipment are presented in this section. Fragility models for bullet perforation, arson and mitigated explosive impact were investigated according to the methodology outlined in Section 3.1. The physical models associated with the attack vectors were simplified, but this is related to the fact that the final focus of the work was to obtain correlations for damage probability of different security scenarios, rather than describing the detailed mechanical behavior of the targeted process item. Thus, the use of the developed fragility models should be restricted to the framework of SVA and, more generally, of QRA, as they require a limited number of input parameters. This simplification is necessary for the practical use of SVA by industrial practitioners, to reduce time and costs of the analysis, as the results obtainable by a certain approach has

![img-1.jpeg](img-1.jpeg)

Fig. 2. Structure of the BN developed in the present study for the vulnerability assessment; two targets (T1 and T2) are considered for the sake of exemplification. The dashed line shows the dependency of timely intervention on the attack mode.

to be conservative.

It is also worth mentioning that the methodological framework introduced in the present work is open. Indeed, depending on the scope of the assessment and risk management [68], the implemented fragility models can be modified (e.g., depending on the firearm used [62]), integrated with other attack modes or completely changed if a higher level of precision for the prediction of the final damage to a target is required.

### 4.1. Fragility model for bullet perforation

The procedure developed in this study to determine the probability of damage from firearms is based on two stages. The first stage consists in the evaluation of the velocity of the bullet when impacting the target. The approach followed in this study to quantify the velocity of a bullet was proposed by the U.S. Army Research Laboratories [69]. This approach combines a simplified expression of Newton's second law with Mayevski's expression for the drag coefficient [70]. The resulting equations offer a simple expression to calculate the horizontal trajectory of the bullet, as shown in Eq. (8) and Eq. (9):

$$v = v_0 \cdot \left( 1 + n \cdot \left(\frac{dv}{dx}\right)_0 \frac{(x - x_0)}{v_0} \right)^2, \quad n \neq 0 \tag{8}$$

$$v = v_0 \cdot \exp\left(\left(\frac{dv}{dx}\right)_0 \frac{(x - x_0)}{v_0}\right), \quad n = 0 \tag{9}$$

where *x* is the position (m), *x₀* is the initial position (m), *v* is the velocity (m/s) in the position *x*, *v₀* is the muzzle velocity (m/s), (*dv*/*dx*) is the muzzle retardation ((m/s)/m); *n* is a non-dimensional exponent and it comes from Mayevski's expression of the drag coefficient, which is proportional to a power of the velocity [70].

Three reference bullet types have been chosen in the present work. Table 2 summarizes the relevant characteristics of the reference bullets, which are typically used in assault rifles. The first reference bullet is an intermediate cartridge, the 7.62 × 39 mm (namely, B1), commonly employed for assault rifles such as the AK-47 [71]. The other two bullets, the 7.62 × 51 NATO (namely, B2) and the 7.62 × 54R (namely, B3), have a larger caliber, and are employed for sniper rifles, which allow a long firing distance and high accuracy [72].

The parameter *v₀* in Table 2 have been evaluated for each reference bullet by averaging the typical values associated with commercial bullet types provided by several manufacturers [74–79]. The parameters *n* and (*dv*/*dx*) have been obtained for the three reference cartridges based on the data available in literature [73] for standard bullet types with a similar mass (namely, *m*, see Table 2).

The second stage of the procedure consists of defining the probabilistic model based on probit regression for bullet perforation. Stewart et al. [80] conducted field tests of 7.62 × 51 mm AP (armor piercing) ammunition fired into mild steel targets. The resulting data have then been processed by Stewart et al. [80] by means of a Monte Carlo probabilistic analysis to estimate the probability of intrusion given different velocities, target thicknesses and plate material. The study considered a range of target thickness values (i.e., 10 to 32 mm) comparable to storage tanks of industrial facilities. Moreover, the plates adopted in the

Table 2 Relevant characteristic of the bullets considered in this study elaborated from manufacturers data and literature [73]. The thickness required to avoid perforation of each reference steel (S₀) is calculated according to the procedure described in Section S.1 of the Supplementary Material, whereas reference steel properties are reported in Table 3.


study were made of steels that are compatible with the ones of atmospheric [81] and pressure vessels [82]. In particular, Grade 250 MPa and Grade 350 MPa steel plates have been considered and their relevant physical properties are shown in Table 3.

Lastly, the ammunition used in the field tests is typical of assault rifles, which are compatible with the reference bullets chosen in the first step of the procedure (see Table 2). An armor piercing bullet has been used in the reference study of Stewart et al. [80], thus obtaining conservative results. For these reasons, the data gathered in [80] constitute a significant basis to develop the fragility model.

In order to obtain a probit regression of the failure data, a dose associated with the impact of the bullet on the target needs to be defined. In this specific case, the damage is associated with the perforation of the bullet into a steel target and a reference value to measure the severity of impact is the thickness required to avoid perforation, $S_{s}$. Therefore, the dose $\left(D_{p}\right)$ was defined by comparing the actual thickness of the plate (namely, $s$ ) against the value of $S_{s}$, as follows:
$D_{p}=\frac{f \cdot S_{s}}{s}$
where $s$ and $S_{s}$ are expressed in mm , and $f(=0.9$ according to [80]) is a safety factor.

Several approaches are available in literature to support the evaluation of $S_{s}$. The Supplementary Material (see Section S.1) summarizes the most widely applied, which were compared in order to determine the more suitable relationship to deal with thickness values and geometrical features of typical chemical and process equipment. The Supplementary Material also shows the estimated values of $S_{s}$ for the bullets and materials considered in the present study (see Table 2 and Table 3, respectively). The correlation selected to calculate $S_{s}$ in the present study was derived by the study of Rosenberg and Dekel [83], obtaining the $S_{s}$ values shown in Table 2.

Based on the $D_{p}$ values calculated according to Eq. (10), the probit regression was obtained for each bullet velocity, based on the data obtained in [80] for Grade 250 MPa and 350 MPa steel. The first and second probit coefficients $\left(k_{1}\right.$ and $\left.k_{2}\right)$ were estimated through the interpolation of the values obtained for the range $700-850 \mathrm{~m} / \mathrm{s}$. Fig 3a shows the probit curve obtained for Grade 250 MPa steel plates, while Fig 3b shows the probit curve for Grade 350 MPa steel plates.

The so obtained probit relationships for Grade 250 MPa steel and 350 MPa steel are respectively shown in Eq. (11) and (12):
$Y=k_{1}+k_{2} \cdot \ln \left(D_{p}\right)=5.25+9.53 \cdot \ln \left(D_{p}\right)$
$Y=k_{1}+k_{2} \cdot \ln \left(D_{p}\right)=5.42+13.70 \cdot \ln \left(D_{p}\right)$
An error analysis was carried out in order to verify the accuracy of the probit model developed. The results proved that the model developed for Grade 250 MPa steel has an absolute error lower than $\pm 0.05$ and a percentual error around $\pm 5 \%$; whereas for the case of Grade 350 MPa steel the absolute error is lower than $\pm 0.05$ and the percentual error is approximately $\pm 10 \%$. Hence, the fragility model developed predicts the probability of perforation with an acceptable error for both materials, see Appendix A.

Table 3
Properties of reference steels in this study from [80]; BHN is Brine Hardness and $\mathrm{Y}_{\mathrm{s}}$ is the target flow stress.


# 4.2. Fragility model for arson 

There are different types of incendiary devices, such as flamethrowers or incendiary bombs. Only flamethrower damage has been taken into consideration in this study, although incendiary bombs such as Molotov are easy to build and carry. However, the latter generate small pool fires ( $\sim 1 \mathrm{~m}$ diameter) [84] that could only damage small connections and gaskets. Thus, these incendiary devices were not considered in the present study. Instead, weapons able to generate a high amount of heat radiation in a localized part of the target, such as flamethrowers, were modelled.

The methodology to obtain a fragility model for arson is as follows:

1. Model the ejected flame;
2. Simulation of the heat radiation damage;
3. Regression of the data to obtain a probit relationship.

Firstly, the flame ejected by a flamethrower is to be modeled. To build an accurate model, it is important to understand how such a weapon is built and operated. Military flamethrowers use gasoline/ kerosene mixtures, and are composed of different chambers, some containing the fuel and some containing a pressurized inert gas, which is used to eject the fuel out [85]. On the other hand, commercial flamethrowers use LPG (Liquefied Petroleum Gas) [86] and are mostly used for land-management tasks [87]. Both types have an ejection pipe and an ignition source, which is necessary to ignite the fuel.

Based on the previous considerations, the fire ejected by a flamethrower was schematized as a jet fire. A high uncertainty lies on the performance of such a weapon, so the flamethrower has been modelled according to a worst-case scenario, as detailed in the Appendix B, in which the features of the considered flame are reported. In particular, a maximum operating time was estimated ( $t_{\max }=110 \mathrm{~s}$ ) based on the conservative assumptions documented in Appendix B.

The second stage is aimed at evaluating the damage caused by jet fire impingement on different equipment items. The impact of the jet has been evaluated by determining the time to failure $t t f$ of both atmospheric and pressurized equipment featuring the typical geometries adopted in chemical and process facilities. An extended dataset of equipment features was used for the simulations, as reported in the Supplementary Material (section S.2).

To study the behavior of a vessel partially impinged in a jet fire, the lumped model developed by Landucci and coworkers [51] was adopted with specific settings detailed in the Supplementary Material (section S.2). The model was applied to generate an extended failure dataset for fired vessels. It is worth mentioning that the model was validated against experimental data and the so obtained dataset may be considered reliable [51].

Concentrating the heat load on the surface containing the liquid does not cause relevant damage, as the liquid absorbs all the heat due to its high heat capacity. This was verified in several experimental works dealing with pressurized vessels exposed to fire [88]. Moreover, previous studies demonstrated that the vapor space is the most critical point in the exposure to heat radiation, as it holds the highest stress [89]. Therefore, the most effective way to cause a rupture is concentrating the flame on the top vapor space. For this reason, the chosen filling level in each simulation was set to a minimum credible value of $20 \%$. The chosen filling substance is benzene for atmospheric vessels and pressurized liquefied propane for pressure vessels. The maximum exposure time has been set to $t_{\max }$, i.e., the maximum flamethrower emptying time, given the uncertainty on the maximum operating time of the flamethrower. Moreover, the tanks were considered unprotected by safety barriers (i.e., pressure safety valves, fireproofing, firefighting, etc.). This is reasonable, given the limited time duration of the jet fire impart.

After determining the $t t f$ of each tank included in the dataset, the exposure time has been divided in 10s intervals. For each interval, the

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** Plots for evaluation of probit regression coefficients: a) Probit curve for Grade 250 MPa steel; b) Probit curve for Grade 350 MPa.

probability of failure *Pfail(t)* at the exposure time *texp* has been computed as follows:

$$P_{fail}(t_{exp}) = \frac{N_{fail}(t_{exp})}{N_{tot}}\tag{13}$$

where *Nfail(texp)* is the number of vessels that failed in a time equal or lower than *texp*, and *Ntot* is the total number of vessels simulated.

In this way, a distribution of probability is obtained from the initial time of fire exposure up to *tmax* (=110 s). In order to derive a simplified probit relationship, the chosen thermal dose *Dth* is the exposure time, thus:

$$D_{th} = t_{exp}\tag{14}$$

Next, the probability data were converted into probit (see Section 2.3), obtaining the distributions represented in Fig. 4a for atmospheric tanks and in Fig. 4b for pressure vessels (see the black dots in Fig. 4) with respect to the considered dose. In both panels of Fig. 4, a probit correlation fits the data over a threshold value, that is 20s for atmospheric tanks (see the dashed line in Fig. 4a) and 60s for pressure vessels (see the dashed line in Fig. 4b). A higher threshold for pressure vessels is reasonable, given the higher shell thickness value and robustness of this equipment type. The probit regression is obtained with the application of the Ordinary Least Square method to the data above the threshold considering *ln(texp)* as the independent variable. Table 4 shows the obtained probit models for atmospheric and pressure vessels.

The significance of the probit models developed can be assessed through the evaluation of the regression coefficients shown in Table 4. The *PCC* lies between -1 and 1 and a higher value signifies that a linear relation represents the sets of data well [90]. In this study, both models shown in Table 4 have a high value of *PCC* meaning that there is a significant relation between the probit variable *Y* and *ln(texp)*. Also, the *COD* [90] shows values close to unity for both correlations, thus confirming the validity of the present approach.

### 4.3. Fragility model for mitigated explosive impact

To evaluate the damage caused by IEDs, four different approaches have been combined. The methodology used to evaluate the probability of damage caused by mitigated explosive impact is as follows:

1. Evaluation of equivalent TNT mass *mTNT,eq*;
2. Calculation of dike relevant parameters to determine whether the mitigating effect is in place;
3. Evaluation of overpressure;
4. Probability of damage calculation.

The equivalent TNT mass *mTNT,eq* can be evaluated using the actual IED mass *mIED* (g) and account for the actual mass fraction *Ψ* of the explosive and the TNT efficiency *η* [65], as follows:

$$m_{TNT,eq} = \Psi \cdot \eta \cdot m_{IED}\tag{15}$$

Two IED often adopted in previous attacks [18] have been considered in this study. In particular, Ammonium Nitrate – Fuel Oil (ANFO) and Triacetone Triperoxide Peroxyacetone (TATP). Data were derived from a previous study [65] and are summarized in Table 5.

Then, the presence of a dike is considered as a possible source of explosion mitigation. To calculate the reduction of overpressure, the approach from Miura et al. [64] can be used. Fig. 5 shows the geometrical parameters to be considered. The approach is based on the assumption that the mitigating effect only happens in a portion of space after the dike itself, which is named effective length, *Leff*. If the target is within *Leff*, then the wall significantly mitigates the overpressure, otherwise, the mitigation effect is considered negligible.

In order to apply the approach to different equivalent TNT masses, each geometrical parameter shown in Fig. 5 needs to be re-scaled through the Hopkinson-Cranz relationship [91], as follows:

$$r = \frac{R}{m_{TNT,eq}^{1/2}}\tag{16}$$

where *r* is the scaled length (m/kg<sup>1/3</sup>) of the actual geometrical parameter *R* displayed in Fig. 5 (m).

The effective length *Leff* (kg/m<sup>1/3</sup>) can now be evaluated based on the re-scaled parameters as follows [64]:

$$L_{eff} = (0.765 \cdot r_{de} - 0.366) \cdot h_d + 0.9\tag{17}$$

Meaning that, with reference to Fig. 5, the mitigating effect exists only if the actual distance between the target and the dike *Rdt* is lower than *Leff*.

Then the overpressure generated by the explosive at a certain distance is calculated using the correlation proposed by Bounds et al. [92]:

$$\Delta P = 10^3 \cdot \left(\frac{m_{TNT,eq}^3}{a} + 4.4 \cdot \frac{m_{TNT,eq}^3}{a^2} + 14.0 \cdot \frac{m_{TNT,eq}}{a^3}\right)\tag{18}$$

where *a* is the distance (m) and *ΔP* is the overpressure (Pa). If the mitigating effect exists, then overpressure in case of mitigation (*ΔPm*) can be evaluated using the following equation:

$$\Delta P_m = \Delta P(R_{de} + L_{eff}) + p\tag{19}$$

where *ΔP(Rde + Leff)* is the overpressure evaluated at a distance (*Rde* + *Leff*) with Eq. (18), while *p* in Pa is derived by the study from Miura et al.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** a) Simulation failure data and probit regression for atmospheric tanks; b) Simulation failure data and probit regression for pressure vessels; texp is the time of exposure to the flame.

### **Table 4**

Probit model and regression coefficient for attack with an incendiary device; Y is the probit variable, texp is the exposure time.


### **Table 5**

Values of mass fraction Ψ and TNT efficiency η for IEDs used in this study, derived from [65].


[64] using the scaled parameters as follows:

$$p = 3.187 \cdot 10^6 \cdot r_{de}^{-4.59} \cdot \exp\left( -0.20 \cdot r_{de}^2 + 2.62 \cdot r_{de} - 8.33 \right) \cdot h_{el}$$

If the mitigated effect is not relevant, the overpressure (ΔPnm) is obtained by using Eq. (18) where a becomes Rel, i.e., the distance between explosive and target (see Fig. 5).

The so-obtained overpressure can then be finally used to assess the probability of damage using existing fragility models. In particular, Model 3 in Table 1 [53] was adopted.

### **5. Application to a demonstration case study**

#### *5.1. Description of the facility and targets*

The fragility models developed in Section 4 have been implemented in the BN probabilistic model described in Section 3.2 to support an industrial SVA case study. Fig. 6 shows the layout of the analyzed facility. The facility is surrounded by an external perimeter and has one main access gate (possible intrusion point #3) and two secondary ones (possible intrusion points #1 and #2). Both pedestrians and vehicles can access the facility from the main gate, while the secondary gates are for vehicles only. Additionally, the facility has a parking lot for employees (possible intrusion point number #4).

The figure also highlights the targets and relevant assets, as well as the selected intrusion paths. Four targets have been identified, consisting in two horizontal pressure vessels (P1 and P2 in Fig. 6) and two

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** Geometrical reference values for mitigated explosive impact.

atmospheric tanks (A1 and A2 in Fig. 6). The main features of the tanks are shown in Table 6. A1 and A2 store styrene and ethanol respectively and are located in proximity of the external perimeter. Tank A2 is bounded by a 4m high dike. P1 and P2 store 1,3-butadiene and acrylonitrile respectively and are located near the process area and a warehouse. Table 6 reports the necessary information on the target equipment to carry out SVA.

#### *5.2. Description of attack scenarios and PPS in place*

The facility has a PPS system in place. The external perimeter is highlighted in yellow in Fig. 6 and is protected by a fence and by a video motion detection system connected to the Closed Circuit Television (CCTV). The main gate (red gate in Fig. 6) is surveilled: personnel is checked through automatic credentials checks, while vehicles and drivers undergo manual credentials check. The secondary gates (blue gates in Fig. 6) are instead unattended. The facility is also surveilled with CCTV both around the perimeter and inside. The parking lot is instead unsupervised. Employees are present on-site for 12 hours a day, while the facility is surveilled by security guards at night.

Table 7 summarizes the intrusion scenarios analyzed in this work, which were defined for illustrative purposes. It is worth mentioning that systematic procedures based on Adversary Path Analysis [10] may be also applied at this stage to determine all relevant intrusion paths [37]; however, their application is outside the scope of this study.

In scenarios a) and b) the attacker targets P1. The chosen path is secluded, as the attacker moves along the external perimeter of the facility. In scenarios c) and d), the attacker targets P2 and instead choses a path that directly crosses operation areas. Scenarios e) and f) feature the use of a high amount of ANFO, therefore the attacker enters the facility using a vehicle. To do so, they forge a counterfeit badge in order to pass the controls at the entry gate. In scenarios g) and h), the attacker instead enters the facility with a small amount of TATP by bypassing the automatic credentials check at the main gate. Scenario i) accounts for more targets at the same time (P1, P2, and A1); indeed, the attack is carried out

![img-5.jpeg](img-5.jpeg)

Fig. 6. Layout of the facility selected as a case study. Target features are reported in Table 6; attack scenarios are listed in Table 7. A: atmospheric storage tanks. P: pressurized tanks.

Table 6 Main features of the tanks considered as targets in the case study.


from the outside and the attacker uses a firearm, so they can target multiple equipment in the span of a few seconds.

The information on the paths and the PPSs related to each adversary task sequence are summarized in Table 7.

### 5.3. BN input data quantification

Fig. 7 shows the BN used for the assessment of the case study. First of all, to quantify the performance of PPS means to quantify how likely it is for an intruder to come across someone (employees or security guards) along an intrusion path. From existing literature [39] we know that, during the day, the probability of coming across employees on a path crossing assets is 70% (20% on paths crossing empty areas), whereas, during the night, the probability of coming across security guards is 5%. Therefore, we used Node N3.1 (called "Shift") to define a "day shift", referring to the probability of coming across employees only on a path versus a "night shift" to represents the probability of coming across security guards only. It has to be specified that the probability values associated to Node 3.1 can be changed in case of availability of case-specific data. In our case, we assigned values to Node 3.1 based on a conservative assumption: considering that the probability of coming across employees is higher compared to that of security guards, because of the higher number of employees with respect to security guards [18], we chose to set the node "Shift" to 50%-50% (i.e. 12 hours day-shift and 12 hours night-shift) rather than 33%-67% (i.e. 8 hours day-shift + 16 hours night shift). Then, as explained before, to quantify Nodes N3.2 and N3.6 related to personnel presence, values have been taken from literature [18]. N3.3, N3.4 and N3.5 to N3.32 can be quantified using the approach and data presented in Section 2.2, by using the quantitative data from Argenti et al. [39]. For the sake of exemplification, Node N3.8 related to the intrusion detection from security guards is considered. It depends on the presence of security guards (N3.6) and their level of training (N3.7); if security guards are absent, then the probability of detecting the intrusion is null. If the guards are present and have a high level of training, the probability of detecting the intrusion is 0.85. The impact factor associated to a low level of training is 0.5 [39], meaning that the probability of detecting the intrusion lowers to 0.40 in that case. N3.31 can be quantified considering the PPS in place for each intrusion path shown in Table 7: if at least one PPS present on the attack path works, then the intrusion is detected. To evaluate Node 3.34, the approach in Section 2.2 requires the quantification of the time needed by the intruder to complete attack. The following data have been considered for the analysis:

- The emergency response team comes from the main gate; then, 180s are needed for its preparation and their running speed is 4 m/s, which is the medium value reported in literature [12]. So, for instance, the emergency team needs on average 265s to reach P1 in attack scenario a) and 213s to reach A1 in scenario "e".
- The attacker needs 90s to jump the gate and 20s to place and detonate the explosive [12]. Its running speed on foot is 3.2 m/s, which is the lowest speed reported in literature [12]. A reduced velocity is considered not only to account for the weight of the weapons, but also because the attacker will not run at full speed in order to decrease the probability of being detected. If the attacked enters with a truck (Intrusion Path 3.1 in Table 7), they drive the truck at 30 km/h (approximately 8.3 m/s). For instance, the mean adversary intrusion time tP for scenario e) is 125s. Using the values of tERT computed for scenario "e" and applying Eq. 5, the probability of Timely Intervention Pt for scenario "e" is 0.077.

The PPS system effectively prevents the intrusion only if all three

Table 7


**Table 7**

identified actions happen; therefore, node 3.33 is in the positive state only if N3.31, N3.32, and N.3.29 are in the positive state.

Nodes N4 are representative of the target fragility. These nodes are quantified using fragility models introduced in Section 4. The input data for each attack mode can be retrieved from Fig. 6, Table 6, and Table 7 and are:

- **Explosive attacks**: explosive type and mass, target type, distance from target, dike geometrical parameters (if present); for instance, in scenario h) 15 kg of TATP (9.15 kg of equivalent TNT, according to Eq. (15)) are used to target A2. Considering the mitigating effect of the dike and applying Eqs. (16) - (20), the overpressure on A2 is 0.087 bar and the probability of A2 failing is 0.03 using Model 3 in Table 1. If the effect of the dike is neglected, then the overpressure on A2 can be calculated with Eq. (18) and is 0.11 bar, leading to a probability of damage of 0.11.
- **Firearm attack**: bullet type, distance from target, target construction material and shell thickness; for instance, in scenario i), P1 is 40 m distant from the attack points; by applying Eq. (8) using the data in Table 2, a speed of around 700 m/s at impact with the tank is obtained. Using the models detailed in Section 4.1, Tx is 25.30 mm. Using Eq. 9, a probability of damage of 0.40 is obtained.
- **Arson attack**: target type, exposure time. For instance, the probability of damaging P2 in scenario d) can be computed using the model for pressurized vessels in Table 4, which leads to a damage probability of 0.06.

Node 4.5 can be quantified considering that the attack is considered "successful" only if at least one equipment among A1, A2, P1, and P2 is damaged.

Finally, a sensitivity analysis has been performed on the BN by identifying the parameters whose variation could impact the attack success likelihood. A one-at-a-time sensitivity analysis has been conducted, meaning that vulnerability variation is assessed by individually varying each parameter [93]. Both the target-specific and overall vulnerability maximum range of variation have been identified.

More specifically, the sensitivity analysis involved the new fragility models developed, i.e., firearms model and arson model. This means that the targets interested by the sensitivity analysis are A1, P1 and P2, since A2 is only targeted by explosives.

The parameters included in the sensitivity analysis for firearms attack are the bullet type, the distance from the target and the target construction material. The bullet type has been varied among B1, B2 and B3 (see Table 2); the distance from the target has been varied in a ± 30% range. Finally, the construction material has been varied between Grade 250 MPa and Grade 350 MPa steel (see Table 3). The type of bullet and the distance influence the velocity of the bullet when impacting the target, while the target construction material directly influences the fragility curve, given the difference in physical properties.

The parameter included in the sensitivity analysis for arson attack is the exposure time, which has been varied in a ± 30% range of the baseline value shown in Table 7.

## 6. Results and discussion

### 6.1. Vulnerability assessment

The use of the BN shown in Fig. 7 allowed for the evaluation of PPS

![img-6.jpeg](img-6.jpeg)

Fig. 7. Bayesian Network applied to the analysis of the case study.

performance and attack success likelihood for the case study. The so obtained results are summarized in Table 8, which shows the prior probabilities, i.e., the probability obtained without setting any evidence, as well as the probability when the attack scenarios in Table 7 are set. The calculations were obtained using GeNIe Modeler as stated in Section 3.2. To obtain the probabilities of the attack scenarios, GeNIe allows for all needed evidence to be set. For example, to evaluate the success of scenario "a", evidences were set on Nodes N1.1, N1.2 and N2.1, and the probability of attack success in Node 4.5 was calculated accordingly.

Part A of Table 8 is dedicated to the performance summary of the PPS in place. The prior scenario shows that PPS have a probability of neutralizing an attack lower than 0.10. Timely intervention and intrusion assessed detection, which are two of three functions of PPS, especially have a low performance; the maximum probability of intrusion assessed detection for the scenarios outlined in Table 7 is 0.61 (scenarios "g" and "h), while the maximum probability of timely intervention is lower than 0.50. This firstly means that PPS are not installed in critical locations and, if they are, their performance is not sufficiently high due to low quality of instrumentation or poor training of security personnel. Consequently, the conditional probability of PPS successfully preventing intrusion in each scenario is always lower than 0.20. The performance of PPS is, therefore, unsatisfactory. As these values were calculated based on average literature data, representative of industrial facilities performance, this evidences that more resources should be allocated to improve the security aspects of process facilities, in order to effectively raise the probability of interruption of an intentional attack.

Part B in Table 8 summarizes target specific vulnerability and the overall likelihood of attack success based on the implementation of the fragility models developed aimed at supporting the failure probability estimation in case of successful attack.

Scenarios involving the use of ANFO (scenario "e" and "f") yield the same probability values. This is due to two factors: firstly, the targets

Table 8 Case study results: scenario-based analysis; for attack scenarios see Table 7.


have the same probability of being chosen because they are both atmospheric tanks. Secondarily, the intrusion path is the same, which means that both A1 and A2 will be damaged either way even if only one target is chosen by the attacker. The same consideration can be done for scenarios "g" and "h" involving the use of TATP. Scenarios "e" and "f" are critical from both a PPS standpoint and a fragility standpoint. In fact, the probability of PPS preventing the intrusion is one of the lowest among the cases analyzed (0.04) and the probability of damaging the targets is among the highest for A1 (0.68) and the highest for A2 (0.18).

Scenarios involving the use of TATP on atmospheric equipment (scenarios "g" and "h") are less critical compared to scenarios "e" and "f" involving ANFO. Firstly, the probability of timely intervention is higher given that the intruder has to walk instead of driving a truck. The probability of damaging A1 and A2 is also significantly lower; in fact, although TATP has a higher TNT equivalency ratio, the small quantity of TATP that can be carried in a backpack does not compensate for the amount of ANFO that can be hidden in a truck.

Attacks using firearms (scenario "i") are the most critical due to both PPS performance and equipment fragility. Even if an intrusion is assessed from PPS, the attack cannot be stopped because the attack is almost instantaneous, making it impossible for the emergency response team to act. Moreover, the probability of damaging the targets is among the highest of all cases. Atmospheric tanks are especially vulnerable, as shown by the unitary probability of successfully damaging A1.

Scenario "b" and "d", which involve arson attack, have a probability of success lower than 0.1, meaning that arson is not a critical attack mode for pressure vessels. This is the result of both the performance of PPS and the resistance of the equipment. Scenarios "b" and "d" have the highest probability of timely intervention, since the incendiary weapon needs to be fired for 60s, which highly delays the attacker. Moreover, the high thickness of pressure equipment makes them less vulnerable to arson attacks.

Finally, Part C in Table 8 summarizes results for vulnerability assessment using a conservative approach, as explained in Section 3.2. Arson (scenarios "b" and "d") has a 90% lower credibility than what assumed by the conservative approach, as seen by comparing Part B and Part C of Table 8. This means that the conservative estimation was highly overestimating the impact of arson on pressure vessels. In scenarios "e" and "f", in which ANFO is used to damage atmospheric tanks, the vulnerability of target A2 is reduced by 65%, leading to an overall reduction of over 10% in vulnerability. This shows that dikes can be effective in mitigating the effect of overpressure, even if they are not built with the specific purpose of being blast walls. The same reduction in vulnerability can also be noticed for attacks with TATP (scenario "g" and "h").

A more precise estimation can be obtained from the advanced fragility model for firearms. A reduction of attack success likelihood up to around 95% can be observed for pressure vessels in scenario "i". On the other hand, atmospheric tanks keep the same vulnerability due to the lower shell thickness values, which causes them to be very vulnerable targets for firearms.

### 6.2. Sensitivity Analysis

As outlined in Section 5.3, sensitivity analysis has been performed in order to assess the variability of vulnerability estimates by modifying relevant parameters. Fig. 8 summarizes the results and shows the comparison with vulnerability evaluated using the conservative approach (see Section 3.2).

The vulnerability associated with atmospheric tank A1 is not significantly modified by the variation of parameters and is not reduced by improving the material properties (i.e., considering steel Grade 350 MPa). This confirms the critical vulnerability of atmospheric equipment towards attacks performed by using firearms.

On the other hand, the vulnerability estimated for pressure vessels P1 and P2 by means of the present approach is significantly lower compared to the one obtained by the conservative approach. Moreover, the baseline application of improved fragility models shows that P2 has a 90% lower vulnerability compared to P1. In fact, P2 is located further from the shooting position (intrusion point 4 in Fig. 6) compared to P1, which lowers the shooting success probability. This could not be observed by means of the conservative approach. The probability of damaging both P1 and P2 is significantly varied in the sensitivity analysis. However, the maximum values of successfully damaging P1 and P2 obtained by the sensitivity analysis are 30% lower than the conservative approach vulnerability.

The use of the fragility models developed leads to a baseline value of overall plant vulnerability that is approximately 50% lower than the one obtained by means of the conservative approach. The range of variation of overall plant vulnerability obtained from the sensitivity analysis is at most 25% and at the least -15%.

The relevant decrease of plant vulnerability shows that the use of improved fragility models can offer guidance to a more correct allocation of resources compared to using conservative approaches.

### 6.3. Discussion

The application analysis of the case study demonstrate that the present methodology is suitable for identifying critical security issues among chemical and facilities. In particular, the analysis evidenced a

![img-7.jpeg](img-7.jpeg)

Fig. 8. Results of the sensitivity analysis: A1, P1 and P2 are the vulnerabilities associated with each target at the correspondent ID, OA is the overall attack success probability, BSL is the baseline value of vulnerability obtained, MAX and MIX are respectively maximum and minimum value of vulnerability obtained, and CA is the vulnerability obtained using the conservative approach (see Section 3.2).

lack in PPS effectiveness, given that the maximum probability of effectively stop an intrusion is 0.16 , as shown in Table 8. However, it must be noted that PPS effectiveness was quantified based on the outcomes of a study providing results of general validity [39]. The analysis could be improved by tailoring the PPS effectiveness directly on the facilities examined; in this way, more precise information on security measures could be obtained. In particular, the organization of a given site affects the personnel presence and its training level. For the present study, baseline values were assumed to quantify Nodes N3.2 and N3.6 (see Fig. 7) associated with detection by internal personnel, as explained in Section 5.3. Nevertheless, this methodology can be even extended to unmanned facilities, as the detection system can be customized, once a list of PPS available on-site is available. In order to determine the influence of nodes associated with personnel presence and training, the values of Node N3.2 and N3.6 were varied in a range of $\pm 30 \%$. The maximum obtained variation of overall vulnerability is around $\pm 1 \%$. This is due to the fact that the overall performance of PPS in preventing intrusion (Node N3.35 in Fig. 7) is mostly affected by the emergency response team (Node N3.34 in Fig. 7). Thus, any variation of nodes related to the performance of internal personnel does not significantly affect the overall vulnerability of the plant, as any change is shadowed by Node N3.34.

The proposed improved fragility models allowed for a more precise evaluation of vulnerability of a given process facility. To develop the fragility model, conservative assumptions on the physical model were made in order to reduce input parameters and simplify the expressions. The combined model for overpressure allowed to consider the mitigating effect from dikes, which are commonly installed in process facilities, but without the specific purpose of overpressure protection [56]. The probability of damaging $\mathrm{A}_{2}$ decreased from 0.51 to 0.18 when considering the mitigation due to dikes (scenario " f "), making them also an effective security barrier. The model developed for firearms damage showed that atmospheric vessels are very vulnerable to this type of attack, given their relative low thickness. Indeed, scenario " i " showed that the probability of damage of $\mathrm{A}_{1}$ remained 1.00 even when applying the new fragility model. Pressurized vessels are instead less vulnerable, due to the higher thickness of the shell. This can also be noticed in scenario " i ": the probability of damaging $\mathrm{P}_{1}$ reduced from 1.00 to 0.40 and the probability of damaging $\mathrm{P}_{2}$ varied from 1.00 to 0.04 with the application of the firearm fragility model, showing the benefit of using it with respect to conventional fragility models for equipment exposed to fire. In this sense, additional models could be developed to account for the different types of firearms, bullet size and construction material of chemical equipment, as well as different attack devices. It is also important to note that attacks with firearms are also critical to prevent using PPS. As a matter of fact, these are sudden attacks and could happen far away from the plant external perimeter. To prevent such attacks, a study of the surrounding is necessary since the attacker could take advantage of height points, i.e., highways, to circumvent possible perimetral barriers. Indeed, using concrete perimetral fences might pose an obstacle for attackers, who would then need to climb the wall to be able to aim at the target. This would increase their chance to be identified. In this perspective, a dike might also serve not only as a safety barrier and a protection from explosives, but also as a barrier from potential shooters.

The application of the improved model for arson showed that pressure vessels are only slightly vulnerable to heat radiation from an incendiary device; scenario "b" showed how the damage probability decreases from 0.82 to 0.06 by using the improved fragility model. However, this scenario remains critical, because a catastrophic failure of a pressure vessel could cause very severe consequences [65].

Equipment damage is the starting point of a loss of containment, which can bring to the potential loss of human lives and assets. Therefore, a risk evaluation criterion that involves both this aspect is beneficial in decision making processes as well. Pasman and Rogers [94] showed that BN are a powerful tool for consequence assessment, once physical effects from the scenarios following loss of containments have
been quantified. Moreover, Khakzad et al. [95] developed a methodology to include the evaluation of mitigation measures in the BN, e.g., fireproofing.

Future works need to integrate the economic and the human aspects of risk mentioned above, as well as the performance of safety barriers, in the perspective of risk-related decision-making processes. In this perspective, BN allow for the combination of different decision criteria, making them a suitable tool for integrated safety and security studies.

## 7. Conclusions

As the threat to intentional attacks to chemical facilities is on the rise and particularly prominent in a time when countries with highdeveloped chemical industries are the site of violent conflicts, proper quantitative tools for security risk analysis need to be defined.

This work focused on the improvement of fragility models that are used to quantitatively assess the vulnerability of chemical equipment, in terms of probability of damage. Fragility models have been developed based on probit regression, which is used in conventional safety risk analyses due to its simple application.

Fragility models for bullet perforation, arson and mitigated explosive impact have been developed. The developed models implement simplifying yet conservative assumptions, in order to minimize the input needed for the analysis. The fragility models developed have shown that atmospheric tanks are highly vulnerable to attack with firearms. The vulnerability of pressurized vessels is reduced up to $95 \%$ with respect to atmospheric vessels, due the higher thickness of the shell. However, pressurized vessels are more susceptible to arson attacks for high exposure times.

The use of advanced fragility models to a case study showed a $45 \%$ reduction of overall plant vulnerability compared to the use of a conservative approach, allowing for a more precise security analysis. Still, PPS performance was demonstrated to critically affect the vulnerability of process facilities, as the probability of PPS successfully preventing the attack is lower than $10 \%$. These considerations highlight the need to improve the current security measures in chemical facilities. The developed models constitute one step further towards the harmonization of approaches used in operational safety and security, whose integration will be explored in future studies. The possibility to analyze each node and to implement risk assessment criteria make BN an adequate tool for vulnerability assessment. In conclusion, the evaluation of physical fragility with adequate but simplified fragility models is essential for SVA. Equipment fragility, coupled with PPS performance, can provide guidance for security managers and analysists in security investment by highlighting the most critical assets and barriers.

## CRediT authorship contribution statement

Giulia Marroni: Writing - original draft, Visualization, Software, Formal analysis. Leonardo Casini: Visualization, Software. Andrea Bartolucci: Writing - review \& editing. Sanneke Kuipers: Writing review \& editing, Project administration. Valeria Casson Moreno: Writing - review \& editing, Validation, Methodology, Investigation, Formal analysis, Data curation. Gabriele Landucci: Writing - review \& editing, Supervision, Resources, Project administration, Funding acquisition, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This study was in part developed within the project LIFE20 ENV/IT/

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.ress.2023.109880.

## Appendix A -Fragility model for bullet perforation: error analysis

An error analysis was carried out in order to verify the accuracy of the probit model developed in Section 4.1. Absolute error $A E$ and relative error $R E$ have been defined as follows:
$A E=P_{\text {regr }}-P_{\text {data }}$
$R E=\frac{P_{\text {regr }}-P_{\text {data }}}{P_{\text {data }}}$
where $\mathrm{P}_{\text {regr }}$ is the probability obtained using the developed probit regression and $\mathrm{P}_{\text {data }}$ is the probability obtained by the reference study [80]. The parity plot reported in Fig. A. 1 shows the comparison between $P_{\text {data }}$ and $P_{\text {regr }}$ and related $A E$ and $E R$.
![img-8.jpeg](img-8.jpeg)

Fig. A.1. Error analysis of the probit regression developed in the present work for the firearm impact on process equipment; parity plots for: a) absolute error for Grade 250 MPa steel, b) relative error for Grade 250 MPa steel, c) absolute error for Grade 350 MPa steel (c), parity plot of relative error for Grade 350 MPa steel (d).

# Appendix B - Flamethrower impact assessment 

The aim of the present Appendix is to model the characteristics of a flamethrower in order to obtain the fragility model for arson. As stated in Section 4.2, a high uncertainty lies in the definition of typical parameters of a such a weapon. Extensive reviews of flamethrowers used in war context are available, however the models are dated and can have very different parameters [85].

Given that typically flamethrowers used for offense operate using gasoline/kerosene mixtures, simulations have been run in the software DNV GL Phast 8.2 [96] with different sets of chemicals, in order to obtain a worst case scenario of flame length, surface emissive power and emptying time to be used. A release from a 5 mm hole of 50 L of pressurized flammable substance has been simulated.

Considering the typical composition of benzene and kerosene, two simulations were carried out: the first one used n-butane as key compound of the volatile fraction of gasoline. The second one used n-octane as key compound for the heavy fraction of gasoline. The results are gathered in Table B. 1 and represent the worst value obtained from the two simulations for flame length, maximum emptying time $t_{\max }$ and maximum surface emissive power. These values have been used in Section 4.2 to study the behavior of vessels exposed to the flamethrower flame.

Table B. 1
Worst-case characteristics of the flamethrower flame, from the simulation of a 5 mm release of different flammable liquids; $L_{\mathrm{pt}}$ is the length of the flame, $t_{\max }$ is the maximum emptying time and $\mathrm{SEP}_{\max }$ is the maximum surface emissive power.

