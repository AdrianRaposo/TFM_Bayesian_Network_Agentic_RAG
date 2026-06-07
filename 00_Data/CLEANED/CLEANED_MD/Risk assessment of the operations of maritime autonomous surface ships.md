# LJMU Research Online 

## Chang, C-H, Kontovas, CA, Yu, Q and Yang, Z

Risk assessment of the operations of maritime autonomous surface ships
http://researchonline.ljmu.ac.uk/id/eprint/14119/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Chang, C-H, Kontovas, CA, Yu, Q and Yang, Z (2020) Risk assessment of the operations of maritime autonomous surface ships. Reliability Engineering and System Safety, 207. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Risk assessment of the operations of maritime autonomous surface ships 

Chia-Hsun Chang ${ }^{1}$, Christos Kontovas ${ }^{1}$, Qing Yu ${ }^{1,2}$, Zaili Yang ${ }^{1}$<br>${ }^{1}$ Liverpool Logistics, Offshore and Marine Research Institute (LOOM),<br>Liverpool John Moores University, Liverpool, United Kingdom.<br>${ }^{2}$ School of Navigation, Wuhan University of Technology, Wuhan, China.


#### Abstract

Maritime Autonomous Surface Ships (MASS) are attracting increasing attention in the maritime industry. Despite the expected benefits in reducing human error and significantly increasing the overall safety level, the development of autonomous ships would undoubtedly introduce new risks. The overall goal of this work is to develop an approach to evaluate the risk level of the major hazards associated with MASS. To that extent, a Failure Modes and Effects Analysis (FMEA) method is used in conjunction with Evidential Reasoning (ER) and Rule-based Bayesian Network (RBN) to quantify the risk levels of the identified hazards. The results show that 'interaction with manned vessels and detection of objects' contributes the most to the overall risk of MASS operations, followed by 'cyberattacks', 'human error' and 'equipment failure'. The findings provide useful insights on the major hazards and can aid the overall safety assurance of MASS.


Keywords: Maritime risk, maritime safety, maritime autonomous surface ships, Failure Modes and Effects Analysis (FMEA), Bayesian Networks (BN)

## 1. Introduction

Much research has shown that human error contributes to $80-90 \%$ of shipping accidents directly or indirectly (Schröder-Hinrichs, 2010; Heij and Knapp, 2018). Maritime Autonomous Surface Ships (MASS), defined by the IMO (2018) as "ships which, to a varying degree, can operate independently of human interaction", are attracting increasing attention in the maritime industry as an emerging solution to reduce human errors.
IMO (2018) defines the degrees of autonomy of a MASS in four levels as follows:
(1) Ship with automated processes and decision support: Seafarers are onboard to operate and control the vessel; some operations may be automated and at times be unsupervised but seafarers are always present and ready to take control,
(2) Remotely controlled ship with seafarers on board: the ship is controlled and operated remotely; however seafarers are onboard and ready to take control,
(3) Remotely controlled ship without seafarers on board: ship is unmanned and controlled from a remote location, and
(4) Fully autonomous ship: the operating system can make decisions and determine actions by itself.

The are many expected benefits of MASS, in comparison to conventional marine systems, such as enhancing safety and security (IMO, 2009; Burmeister et al., 2014a, 2014b; Ahvenjärvi, 2016; Höyhtyä et al., 2017; Levander, 2017; Komianos, 2018; Porathe and Rødseth, 2019), improving human resource management (Burmeister et al., 2014b; Levander, 2017; Komianos, 2018), reduced operational costs (Burmeister et al., 2014a; Ahvenjärvi, 2016; Jokioinen et al., 2016; MUNIN, 2016; Kretschmann et al., 2017; Komianos, 2018) and reducing air pollution (Burmeister et al., 2014a; Knowledge Group, 2018).

IMO is currently looking at the integration of advanced technologies, including autonomous ships, in the regulatory framework on areas such as safety (e.g. related to the International Convention for the Safety of Life at Sea, SOLAS), collision regulations (related to the International Regulations for Preventing Collisions at Sea, COLREGs), loading and stability (related to the International Convention on Load Lines), training of seafarers and fishers (see the International Convention on Standards of Training, Certification and Watchkeeping for Seafarers, STCW), search and rescue (related the International Convention on Maritime Search and Rescue, SAR), tonnage measurement and others (IMO, 2018).

Despite the abovementioned advantages, MASS still face several challenges in their development and barriers to their wider adoption, including crew unemployment (Komianos, 2018), national and international regulatory barriers (Danish Maritime Authority, 2017; Ramboll and CORE Advokatfirma, 2017; Komianos, 2018), extensive training costs for staff (Burmeister et al., 2014b; Ahvenjärvi, 2016; Danish Maritime Authority, 2017; Levander, 2017), large costs for developing new infrastructure (IMO, 2009; Komianos, 2018), maintenance costs (Porathe et al., 2018) and technical challenges in ship design and operations system design (Delft et al, 2016; Höyhtyä et al, 2017; Wróbel et al., 2017).

MASS can significantly reduce the accidents caused by human error; they cannot however totally eliminate them. In addition, because MASS consist of several interconnected systems, some of which are based on newly proposed or advanced technologies, there is little evidence yet to prove that they are risk-free (Komianos, 2018). In fact, it has been argued that MASS will introduce new types of risk; see the accidents involving autonomous vehicles in road transportation which repeatedly occurred in the past years. Rødseth and Burmeister (2015) point out 5 unacceptable hazards in the initial ship configuration:

1. Interaction with other ships
2. Errors in detection and classification of small to medium size objects are critical
3. Failure in object detection, particularly in low visibility, can cause powered collisions.
4. Propulsion system breakdown
5. Very heavy weather may make it difficult to manoeuvre ship safely.

Despite the growing number of studies on MASS (e.g. Haworth et al., 2016; Norris, 2017; Porathe et al., 2018), they are still at an early stage. Rødseth and Burmeister (2015) describe some conceptual hazards that might happen in MASS operations. Given the hazardous nature of their operation, it is important to assess the severity of the related hazards and their uncertainty. Furthermore, there is a lack of much research on the development of conceptual risk models to analyse the risks in MASS operations. The literature is expanding fast in this emerging area; see for example Gu et al. (2020) for a survey of the literature on autonomous marine vessels and Hoem (2019), which updates Porathe et al. (2018), for a review of the present and future of risk assessment of MASS. In addition, Fan et al. (2020) propose a framework for the identification of factors that influence the navigational risk of MASS and also present a very comprehensive literature review of the area.
We contribute to this growing research area by investigating the important hazards related to autonomous ships. The results of this research can support better understanding of the relevant hazards and their risk levels. The stakeholders, including designers and operators, could use this research to focus on the important hazard, thus, addressing the areas that could help increase the overall safety of autonomous shipping.

The rest of the paper is organised as follows. Section 2 presents a literature review of the current hazards of MASS operations. Section 3 describes the research methods applied in this study and Section 4 presents the risk data analysis and results. Discussion and conclusions are drawn in Section 5.

# 2. Hazards in MASS operations 

Based on a thorough literature review, the main hazard categories in MASS operations are identified and presented in Table 1. We note that the literature in this area is scarce, but there is now an increasing number of papers on MASS, including several survey papers. Munim (2019) reviews the autonomous ships development projects and their benefits from economic, environmental and social perspectives; whereas Dreyer and Oltedal (2019) present a review of the safety challenges of autonomous vessels. Kim et al. (2020) reviews the impact of MASS on regulations, technologies, and industries. Wróbel et al. (2020) undertake a thorough literature review of the operational features of remotely controlled vessels (3rd degree of autonomy) based on the principles of System-Theoretic Process Analysis (STPA) and identifies existing and future research directions in the field of autonomous vessels.

Through the review of the relevant literature (see below for more) we have identified the hazard categories that are summarized in Table 1.

Table 1 Hazard categories in MASS operations


# 2.1 Human error 

Although MASS will help reduce human error, Ahvenjärvi (2016) argues that human error or human-task mismatch cannot be totally eliminated because the human element is still involved in the design and remote control. Human error might shift from the moment of the incident to the pre-voyage stage, due to the large scope of coding and programming (Burmeister et al., 2014b). The related systems cannot be fully tested or reviewed until the actual ship operations. Due to the large number of software package programming and complicated coding, there is a likelihood that software engineers may make some mistakes during the design or the programming phase and, therefore, leave software errors -what is referred to as bugs- in the system (Ahvenjärvi, 2016; Bolbot et al., 2018). In addition, poor design and interface will cause more human factor related issues during the operations (Ahvenjärvi, 2016). Operators in the shore control centre (SCC) face the same or, even, new human error hazards as they may not be fully aware of the actual conditions on the scene (Burmeister et al., 2014a). Autonomous ships also need periodic maintenance, either remotely or through physical contact. In both ways there will be some human error involved and these should be considered as hazards of MASS operations (MUNIN, 2015; Rødseth and Burmeister, 2015).

Coping with the human elements relating to MASS, a parallel body of relevant literature is conducted on ergonomics (the discipline concerned with the understanding of interaction among humans and the other elements of a system) and non-technical skills, especially related to the future role and responsibilities of the actors involved, respectively. Task analysis methods, which are widely used by human factors and ergonomics professionals, have been used to address the system-human interaction in autonomous shipping. Thieme and Utne (2017) model the interaction between the human operator and an autonomous underwater vehicle. According to Ramos et al. (2019), while the studies on autonomous surface vessels are few in the literature, the modelling of the interaction human-system and human error from a Human Reliability Analysis (HRA) perspective is even fewer. A task analysis of operators for the collision avoidance of autonomous vessels is reported in Ramos et al (2019). Ramos et. al. (2020) propose a human-system interaction in an autonomy method based on a concurrent task analysis.
Non-technical skill requirements are also very critical in the new era of autonomous shipping, and to a large extent they will be different with those of conventional ships (Kitada et al., 2018). Some human positions onboard ships will also disappear in the future (Sharma et al. 2019) and replaced by remote controllers. Mallam et al. (2019) explore the effects of autonomous shipping on future work organisation and roles of humans within maritime operations. Kim and Mallam (2020) discuss leadership competencies related to the IMO STCW Convention.

### 2.2 Interaction with manned vessels and detection of objects

Previous research has addressed the interaction between MASS and manned vessels concerning the detection of objects (Burmeister et al., 2014b; Rødseth and Burmeister, 2015; MUNIN, 2015; Ahvenjärvi, 2016; Höyhtyä, et al., 2017; Wróbel et al., 2018b; Porathe and Rødseth, 2019; Ramos et al., 2019). Although Komianos (2018) has stated that MASS can largely reduce the risk of collision and comply with the COLREGs, they also argue that MASS does not satisfy Rule 5 of COLREG, which requires proper look-out by sight and hearing on every ship to assess the situation and the risk of collision. MUNIN (2015) also identifies several relevant hazards in MASS operations. Finally, much research focuses also on collision avoidance and guidance systems; see for example Perera et al. (2018) who propose a ship collision situation avoidance algorithm based on fuzzy logic to support decision-making systems in autonomous vessels and Xu et al. (2019) who use AIS data to propose a path generation system.

# 2.3 Interaction with the physical environment 

This hazard category may include heavy weather, low visibility, areas of icing, ice navigation and strong tidal systems (Banda et al, 2015; MUNIN, 2015; Rødseth and Burmeister, 2015; Wróbel et al., 2017, 2018b). Winter navigation in ice areas for a MASS would most likely involve ice breaker assistance, which poses a risk due to the close proximity of the vessels (Banda et al., 2015). Heavy weather may entail low speed manoeuvring to avoid structural damages to the vessel. All these types of manoeuvring are traditionally performed in manual steering (Wróbel et al., 2017).

### 2.4 System failure

Since autonomous ships heavily rely on information technology (IT), one might wonder if these systems are as capable as human beings. Autonomous systems are based on machine-learning, which requires extensive training to cover most of the potential real-life situations. However, it cannot cover all situations, and the exceptional situations are linked to the most difficult and dangerous system errors because the behaviour of the system is not predictable (Ahvenjärvi, 2016). Furthermore, the systems and software design should have certain tolerance when an unexpected failure occurs. Quantifying the tolerance to make the system run smoothly and, at the same time, ensuring the safety of the voyage is not trivial. It is argued that communication link breakdowns will be the new hazards introduced by the operation of MASS (e.g. Burmeister et al., 2014b; Wróbel et al., 2016; Wróbel et al., 2018a, 2018b; Thieme et al., 2018). MUNIN (2015) has also identified a hazard related to system failure.

### 2.5 Cyberattacks

Due to the dependency of autonomous ships on ICT, cyberattacks are considered as a major type of hazards in MASS operations (MUNIN, 2015; Hogg \& Ghosh, 2016; Rolls-Royce, 2016; Ghaderi, 2018; Komianos, 2018; Wróbel et al., 2018b, 2020). Many cyberattacks have been reported in recent years, see the incidents involving COSCO US in 2018, Maersk in 2017 and the Port of Antwerp in 2011-2012. Hand (2016) quotes Lar Jensen (CEO of CyberKeel) who claims that "autonomous ships will not become a mainstream reality in the next few years due to unresolved cyber-security issues on the technology".

### 2.6 Equipment failure

Equipment failure during sailings is another major hazard category. Given that there is no crew onboard an autonomous ship, in the case of failure the ship needs to be immobilised and wait for the repairing team to arrive. MUNIN (2015) has identified six relevant hazards, including 'fire loss of ship or systems', 'sensor failure - loss of control', 'temporary loss of electricity (e.g. due to black-out) - loss of control', 'failure of the ship's IT structure (e.g. due to fire in the server room) - no control', 'total loss of propulsion', and 'total loss of rudder function'. Furthermore, Wróbel et al. (2017) identify all possible scenarios for preventing or handling fires on a MASS and stated that a fire accident is an extremely difficult challenge in MASS operations. Wróbel et al. $(2018 b, 2020)$ also argue that sensor failures will also have significant consequences leading to unsafe and inefficient MASS operations.

## 3. Methodology

The hazards identified through the literature review (see Section 2) were further assessed using Likert scale [1-5] by a group of 6 experts (see No. 1, 4, 5, 6, 8, and 9 in Table 3). Table 2 presents the average score of each hazard based on the experts' opinions. Based on the hazardscreening step (Yang et al., 2010) in the Formal Safety Assessment (FSA) methodology (e.g. Yang et al., 2013), the hazards that have received an average score above 3 (i.e. the average of the [1-5] Liker scale) were further assessed in the Bayesian model.

Table 2: Results of first-run questionnaire


After the hazard-screening step, a larger number of experts were contacted for an in-depth risk estimation, and consequently 9 experts (see Table 3 for their experience and expertise) have participated in the survey. Based on similar studies we feel that the number of experts is appropriate for our study which demonstrates the feasibility of the proposed method in MASS risk analysis. With the increase in the number of MASS applications in future, more data can

be gathered to update our current findings without the need to change the risk model much as the BN can easily accommodate new evidence.

Table 3: Respondents' background


The final list of hazards that were further assessed through a questionnaire survey is presented in Table 8; the table also summarizes the final results.

Our study utilises a combination of Failure Modes and Effects Analysis (FMEA) with Evidential Reasoning (ER) and Rule-based Bayesian Network (RBN) in order to rank the related hazards. Hazards are here defined as a "source of potential harm" i.e a source of risk, and risk is defined as the "effect of uncertainty on objectives" and is often expressed in "terms of a combination of the consequences of an event (including changes in circumstances) and the associated likelihood of occurrence" (ISO Guide 73 - Risk Management Vocabulary). FMEA, which has been widely used in risk assessment, refers to risk in terms of severity (C), likelihood of failure mode/cause (L) and detection (P); as per the IEC 60812:2018 standard. Through multiplying L, C, and P, we can easily identify top serious hazards based on the risk priority numbers (RPNs); see Section 3.2.1 for more. FMEA has been criticised due to its oversimplified calculations that categorise different hazards into the same group even when they are associated to have different conditions (see Section 3.2.1). To better utilise FMEA for risk assessment, many hybrid methods have been presented in the literature. For instance, FMEA is combined with fuzzy logic to reduce uncertainties (e.g. Pillay and Wang 2003), with Evidential Reasoning (ER) to improve the aggregation of expert judgement (e.g. Yang and Wang, 2015). Lately, it helps to develop FMEA-based Bayesian networks that could be used to perform various sensitivity analyses and scenario simulations (e.g. Yang et al., 2008; Wan et al., 2019). According to Yang et al. (2009), ER allows for the aggregation of multiple experts' subjective evaluations under uncertainty (i.e. incompleteness) and avoids loss of useful information which is the case when using other aggregation methods (e.g. fuzzy logic). The aggregated data can then be converted into conditional probability tables (CPTs) via a rulebased approach.

# 3.1 Data collection 

A questionnaire is designed and distributed to experts in order to obtain their degree of belief (DoB) for the risk parameters, namely the L, C and P associated with each hazard. Compared with a normal Likert scale questionnaire, using DoB involves respondents' uncertainty when answering questions and, thus, provides more useful insights. Respondents indicate their DoB -expressed as a percentage to which they endorse each statement- using a five-point Likert scale; see Table 4 for the linguistic terms used for each parameter and Table 5 for their definitions. It is obvious that for any of the three parameters ( $\mathrm{L}, \mathrm{C}$ and P ) the sum of the DoB of all Likert items should be equal to $100 \%$. For example, an expert might assess the likelihood of 'Failure due to heavy weather' to be 5\% Medium, 10\% Low, and 85\% Very Low, and the consequences as $10 \%$ Critical, $40 \%$ Moderate, $30 \%$ Marginal, and $20 \%$ Negligible.

Table 4: Linguistic scale for each parameter


Table 5: Indices of Likelihood, Severity and Probability of Unpredictability






Source: Adapted from Yang et al. (2008) and Alyami et al. (2019)

# 3.2 Data analysis method 

We utilise a hybrid approach that combines Failure Modes and Effects Analysis (FMEA) with ER and Rule-based Bayesian Networks (RBN) to evaluate the importance of the assessed hazard. The rationale of using ER is to be able to obtain a solution even when the DoB distribution for a responder does not sum to $100 \%$; while RBN is used to overcome the limitations of FMEA. The following sections describe in detail the methods used in our proposed approach; see Figure 1 for an illustration.
![img-0.jpeg](img-0.jpeg)

Fig 1. Flowchart of the methodology

### 3.2.1 Failure Modes and Effects Analysis (FMEA)

FMEA is widely used for the systematic evaluation of the severity of potential failure modes and is one of the most popular safety and reliability analysis tools (Yang et al., 2008).
Following the IEC 60812:2018 standard, hazards related to autonomous vessels are assessed taking into account three parameters: the likelihood of a hazard $(L)$, its consequence severity $(C)$ and the probability of the hazard being undetected $(P)$. The Risk Priority Number (RPN), a numeric assessment of the risk, is defined as follows:

$$
R P N=L i \times C j \times P k
$$

The application of FMEA in risk and safety assessments and, especially, the use of the RPN concept has been criticised as follows (Yang et al., 2008; Liu et al., 2011):

1. The results of RPN are produced in such a way that no weighting of the provided evidence is used, and the interrelationships of variables are not considered.
2. It is difficult to obtain precise values for associated parameters (i.e. $L, C$, and $P$ ).
3. The same value of risk priority may indicate different risk profiles (we are thus unable to provide a backward diagnose/inference).
4. The RPNs used for identifying the criticality factors strongly influence the results.
5. It cannot assess the effectiveness of corrective actions.

Several methods based on uncertainty treatment theories -such as fuzzy logic, Dempster-Shafer (D-S) theory, Grey system theory, BN and Markov models- have been developed to enhance the performance of FMEA (e.g. Yang et al., 2008; Alyami et al., 2019). A BN approach is applied in this study as it is more appropriate for the structure of the identified hazards.

# 3.2.2 Evidential Reasoning (ER) 

ER, based on the Dempster-Shafer theory, is widely used to aggregate information with uncertain subjective data to produce a cohesive result. Compared to similar methods, ER is more precise when dealing with complex systems that are associated with various types of uncertainties, especially for the set of evaluation grades presented in Section 3.1. The current widely used ER algorithm for evidence aggregation is presented in Yang and Xu (2002).

In this study, ER is used to aggregate experts' opinion on the risk parameters for each hazard related to MASS operations. We obtain the judgement of each risk parameter from the experts.
$\beta_{j}^{k}(j=1,2, \cdots, N ; k=1,2, \ldots, L)$ denotes the conditional degree of belief assigned to the j-th risk parameter by the k -th expert in a group of experts $(k=1,2, \cdots, L)$. As the experience of experts depends on various factors such as their backgrounds, years of experience etc, judgements could be weighted. Thus, relative importance weights $w_{k}(k=1,2, \cdots, L)$ for the experts are defined, such as $\sum_{n=1}^{k} w_{n}=1 . \beta_{j}^{k}$ can thus be transformed into basic probability masses $m_{j}^{k}$ by using the following functions (see Yang and Xu (2002)):

$$
\begin{gathered}
m_{j}^{k}=w_{k} \beta_{j}^{k} \\
m_{D}^{k}=1-\sum_{j=1}^{N} m_{j}^{k}
\end{gathered}
$$

To aggregated the collected judgements from different experts, a combined belief degree $\left(m_{j}^{l(k+1)}\right)$ is calculated from $k+1$ judgements by combining all $m_{j}^{k}(j=1,2, \cdots, N ; k=$ $1,2, \ldots, L)$ values. The overall aggregation can be calculated using the following equations:

$$
\begin{gathered}
m_{j}^{l(k+1)}=K_{l(k+1)} \times\left[m_{j}^{l(k)} m_{j}^{k+1}+m_{j}^{l(k)} m_{D}^{k+1}+m_{D}^{l(k)} m_{j}^{k+1}\right] \\
K_{l(k+1)}=\left[1-\sum_{j=1}^{N} \sum_{t=1, t \neq j}^{N} m_{j}^{l(k)} m_{t}^{k+1}\right]^{-1}
\end{gathered}
$$

Then the combined belief degrees $m_{j}^{l(L)}(L \in k+1)$ are normalized as follows:

$$
\gamma_{j}=\frac{m_{j}^{l(L)}}{1-m_{D}^{l(L)}}
$$

where $\gamma_{j}$ represents the normalized belief degree in the final synthesized result $D$.

# 3.2.3 Rule-based Bayesian networks (RBN) 

In order to overcome the shortcomings of FMEA, Yang et al. (2008) propose a fuzzy-rule Bayesian reasoning approach, which involves five steps as follows:
(1) Establishment of FRB with belief structures in FMEA
(2) Failure estimation and transformation
(3) Rule aggregation using a Bayesian reasoning mechanism
(4) Development of utility functions for failure ranking, and
(5) Validation using benchmarking and sensitivity analysis

We therefore introduce a six-step approach (see also Figure 1) as follows.

## Step 1: Identification of hazards (failure modes) in MASS operations

Based on the results of the literature review, six hazard categories that pose risks on MASS operations are identified. Each hazard category consists of several hazards; these are described in Table 6.

## Step 2: Construction of the Bayesian network

We model a Bayesian network (BN) in which hazards are the root nodes (yellow nodes), hazard categories are the intermediate nodes (orange nodes), and the overall risk is the leaf node (red node). The BN is illustrated in Figure 2.

To describe the influential magnitudes of hazards to the overall risk, we propose a MASS risk model that assigns five linguistic states of risk (RPN) as "very low", "low", "average", "high", and "very high" to each node. The linguistic states of L, C, and P for each hazard in the FMEAbased BN are also assigned (c.f. Section 3.1).
![img-1.jpeg](img-1.jpeg)

Fig.2: The developed Bayesian network

Step 3: Establishing the rule-based systems with a belief structure in a MASS risk model and FMEA-based BN

A rule-based approach is used to define the causal relationships and influential magnitudes among all nodes in the BN. The approach describes the causality between the IF and THEN parts with several rules, converting $p$ attendance attributes $\left\{A_{1}, A_{2}, \ldots, A_{p}\right\}$ (IF part) into $q$ states $\left\{C_{1}, C_{2}, \ldots, C_{q}\right\}$ (THEN part) by assigning a belief degree $\beta_{s}(s=1,2 \ldots, q)$ to $C_{s}(s \in q)$ (Alyami et al., 2014; Yu et al., 2020).

For example, the $w^{\text {th }}$ conventional IF-THEN rule (denoted by $R_{w}$ ) can be expressed as:

$$
R_{w}: \text { IF } A_{1}^{w} \text { and } A_{2}^{w} \text { and } \ldots \text { and } A_{p}^{w}, \text { THEN }\left\{\left(\beta_{1}^{w}, C_{1}\right),\left(\beta_{2}^{w}, C_{2}\right), \ldots,\left(\beta_{q}^{w}, C_{q}\right)\right\}
$$

Combining all rules, a rule-based set with multiple-inputs and multiple-outputs is developed.
Several rules are used in the MASS risk model (i.e. hazard categories and hazards) and its sub-FMEA-based BN (i.e. hazards with L, C, and P). If, for example, an expert provides a judgement for the hazard 'Failure due to heavy weather' (PE1) as $\mathrm{L}=$ "very low", $\mathrm{C}=$ "Negligible" and $\mathrm{P}=$ "Very unlikely", then the total risk is "very low". Using an IF-THEN rule, the above judgements can be converted into a rule as follow:

Rule 1: IF very low (L1), and negligible (C1), and very unlikely (P1),
THEN $\{(1$, very low (R1)), (0, low (R2)), (0, average (R3)), (0, high (R4)), (0, very high $(R 5))\}$.

The above rule can be further described as follows:
Rule 1: if $L$ is very low, $C$ is negligible, and $P$ is very unlikely, then $R$ is very low with a $100 \%$ DoB, low with a 0\% DoB, average with a 0\% DoB, high with a 0\% DoB, and very high with a 0\% DoB.

Following the same rationale, the belief structures that used to aggregate the expert's belief for the specific hazards can be established; Table 6 illustrates part of the 125 rules $(5 \times 5 \times 5)$ and the associated DoB distribution.

Table 6: The established FMEA-based BN with a belief structure


# Step 4: Rule aggregation using a Bayesian Reasoning mechanism 

A conditional probability table (CPT) for each node is derived using the IF-THEN rules (Table 6). For example, the first rule of Table 7 can be expressed as follows:
$R_{l}:$ IF very low, negligible and very unlikely, THEN $\{(1,(R 1)),(0,(R 2)),(0,(R 3)),(0,(R 4))$, $(0,(R 5)) \}$. This represents a condition that $L 1, C 1, P 1$, the probability of $R(D o B)$ is $p(R \mid L 1$, $C 1, P 1)=(1,0,0,0,0)$.

The prior probabilities are aggregated to produce the results (i.e. marginal probabilities). Having analysed the prior probabilities for all nodes in the BN, the marginal (posterior) overall probability $p\left(R_{h}\right)$ can be calculated as follows:

$$
p\left(R_{h}\right)=\sum_{i=1}^{5} \sum_{j=1}^{5} \sum_{k=1}^{5} p\left(R \mid L_{i}, C_{j}, P_{k}\right) p\left(L_{i}\right) p\left(C_{j}\right) p\left(P_{k}\right),(h=1,2, \ldots, 5)
$$

where $h$ is the number of states of $R$.
Table 7. The conditional probability table (CPT) for the risk in the sub-FMEA based BN


Step 5: Converting the obtained results into crisp values by using utility functions
Utility values are assigned to all nodes in the MASS risk model and its sub-FMEA-based BN to represent the severity of failures from different prospects. Then, the utility values are combined in the overall risk to prioritise failures.

A linear utility function is then used to calculate the crisp values (CV) for R as follows:

$$
C V=\sum_{z=1}^{t} p\left(R_{h}\right) U_{z}
$$

where $t$ is the number of the linguistic variables of a node, $p\left(R_{h}\right)$ the marginal probability and $U_{z}(z=R 1, R 2, R 3, R 4, R 5)$ the synthesised utility value assigned to R. Utility values are assigned in a linear form (i.e. $0.2,0.4,0.6,0.8,1$ ) (e.g. Yu et al., 2020) to the five defined grades in order to convert the results into crisp risk scores.

# Step 6: Validation using sensitivity analysis 

Sensitivity analysis is then applied to strengthen the reliability of the model and provide useful insights. Sensitivity analysis in this research is used to analyse how sensitive the RPN linguistic estimate $(\mathrm{p}(\mathrm{R})$ ) is to minor changes in the inputs and to test the accuracy of the belief structures on the basis of subjective judgments (Yang et al., 2008).

Jones et al. (2010) and Pristrom et al. (2016) suggest that BNs should satisfy a number of axioms in the uncertainty-sensitivity analysis as follows:

- Axiom 1, a slight increase or decrease in the prior probabilities of each parent node should cause a relative change in the posterior probability of the child/target node (e.g. collision risk);
- Axiom 2, given the variation of subjective probability distributions of each parent node, the influence magnitude from these parent nodes to the child/target node values should reflect the weights of the parent nodes and;


## 4. Analysis and Results

### 4.1 Rule-based Bayesian network results

The risk levels of MASS hazards are analysed using a ruled-based BN as described above. We first obtain the degrees of belief (DoB) for the three risk parameters (L,C,P). For example, based on the aggregated expert opinion we calculate the likelihood of 'Failure due to heavy weather' (PE1) having the DoB illustrated in Fig. 3 (i.e. very high with a $13.96 \%$ DoB and so on).
![img-2.jpeg](img-2.jpeg)

Fig. 3: Results of ER on the likelihood of 'Failure due to heavy weather' (PE1) hazard

In a similar way, we obtain the results of each risk parameter (L, C, P) with respect to each hazard (all parameters are expressed using the degrees of belief). They are, then, fed into the RBN to obtain the results of each hazard category. Due to space limitation and as an illustrative example, we describe the part of the Bayesian Network that is related to the 'Human Error' hazard category. The rest of the BN has been constructed and calculated in the same way. As shown in Fig. 4, three hazards are included under the category of 'human error', namely 'Human error due to a large scope of coding and programming when designing the system' (left-hand side of the figure), 'Failure due to poor design of on-board programme' (middle), and 'Failure due to poor design of remote control centre programme' (right-hand side).

![img-3.jpeg](img-3.jpeg)

Fig. 4: Result of the assessment of the 'Human Error' hazard category
Based on the aggregated expert opinion (the results of the ER analysis that is used as an input to the BN), the value of the likelihood 'Human error due to a large scope of coding and programming when designing the system' is around 1.91 , with the following degrees of belief: $2 \%$ of Very High (VH), $7 \%$ of High (H), $19 \%$ of Average (A), $24 \%$ of Low (L), and $48 \%$ of Very Low (VL); see the top-left corner of Figure 4.

The value of consequence for the same hazard is around 3.98 , with the following associated DoB: $38 \%$ of Catastrophic (CA), $37 \%$ of Critical (CR), $14 \%$ of Moderate (MO), $7 \%$ of Marginal (MA), and $4 \%$ of Negligible (N).

The value of the probability of the failure being undetected is around 3.24 , with $17 \%$ of Highly likely (HL), $28 \%$ of Likely (L), $24 \%$ of Average (A), $25 \%$ of Unlikely (U), and $7 \%$ of Highly Unlikely (HU).

The values fed to the BN are used to calculate the risk for the assessed hazards for the 'Human Error' hazard category; see Fig.4. The risk (denoted as 'value' in the above figure) of the HE1 hazard ('Large scope coding') is 45.9 , the risk of HE2 ('Poor on-board system') is 44.5 , and that of HE3 ('Poor RCC system') is 47.43. The overall risk for the 'Human Error' hazard category has a value of 45.99 (see value in the bottom middle box).

In a similar way, the risk associated with all hazards and hazard categories can be obtained; see Table 8 for the overall results. Our results show that 'Interaction with manned vessels and detection of objects' is the hazard category with the highest risk (a risk value of 57.5), followed by 'Cyber-attacks' (a risk of 51.0), and 'Human error' (a risk value of 46.0). Looking at the hazards individually, all top three hazards belong the 'Interaction with manned vessels and detection of objects' hazard category; they are the 'Failure in detection of semi-submerged objects that are adrift' (risk value: 62.6), 'Failure to determine correct action when interacting with vessels that are: towing, restricted in an ability to manoeuvre, or trawling' (risk value: 55.7) and 'Collision due to poor interaction with manned vessel(s) in heavy traffic' (risk value: 54.9).

Table 8. Risk values of hazard categories and hazards


# 4.2 Sensitivity analysis and validation 

Any BN-based risk model requires validation to check whether the model is robust and the results are reliable. This is particularly important when subjective judgements are involved in generating conclusions (Yu et al., 2020). Yang et al. (2009b) and Jones et al. (2010) suggest BNs should satisfy certain axioms in uncertainty-sensitivity analysis.

GeNIe performs simple sensitivity analysis in Bayesian networks by simulating all the possible scenarios. This kind of sensitivity analysis can help validate the probability parameters of a BN by investigating the effect of small changes in numerical parameters (i.e., probabilities) on the output parameters (i.e the posterior probabilities). This is in line with the axioms presented in Section 3.2.

To study the effects of different variables (i.e. hazards) to the overall risks, we perform a sensitivity analysis using the Genie software. The results are illustrated in Fig. 5 (overall risk is 'very high') and Fig. 6 (overall risk is 'very low'). Each figure presents the effects of hazards to different overall risk states. For example, in Figure 5, it is observed that the value for CA2

varies between 0.1471 and 0.2042 . This means when setting CA2 to $100 \%$ 'very high' (keeping the other figures constant), the 'very high' state of the overall risk (child node) is 0.20428 . On the other extreme case, when setting CA2 to $0 \%$ 'very high', the 'very high' state of the overall risk (child node) becomes 0.1471 . Therefore, based on Figure 5, CA2 has the highest impact magnitude to the child node, revealing its highest influential impact/weight. In a similar way, we see that HE2 (see bottom bar in Fig. 5) has the lowest influence/weight.
![img-4.jpeg](img-4.jpeg)

Fig. 5: Sensitivity analysis results when the overall risk is very high

Fig. 5 shows that when the overall risk is 'very high' (VH), the influential magnitude of SF1 to overall risk is the lowest (notice the left part of the SF1 bar), which means that failures related to communication link are rarely associated with very high expected risks. In contrast, 'Communication between ships and shore control centre due to hacker attacks' (CA1) and 'Failure of the operation system due to hacker attacks' (CA2) show significant influence on the overall risk, thus selected as the two most critical hazards under the high-risk situation.
![img-5.jpeg](img-5.jpeg)

Fig. 6: Sensitivity analysis results when the overall risk is very low
Figure 6 illustrates two important critical situations affecting the overall risk of autonomous ships: (a) operating on good weather (as opposed to 'under heavy weather' scenario) would

significantly reduce the overall risk to a 'very low' level (green part of PE1) and (b) 'failures in communication links' will significantly increase the overall risk (red part of SF1). The figure also shows that improvements on on-board systems should not be considered when the overall MASS risk is under a 'very low' risk level because poor on-board systems have small positive effects (green part of HE2). Based on the above results of the sensitivity analysis, it is clear that Axioms 1 and 2 are satisfied.

# 5. Discussion and conclusions 

### 5.1 Discussion

The results of the BN model show that 'human error' ranks as the third top hazard in MASS operations. This implies that the contribution of human error to the overall risk of MASS operations is still large; a probable explanation is that experts believe that hazards related to human error shift from the area of the actual operations, in conventional shipping, to that of programme/software design in the case of MASS. For example, a poor design of software or the remote control centre could lead to losing control of ships and, thus, causing further accidents. Therefore, shipping companies still have to pay much attention to such human error related hazards.

Our analysis shows that the two top hazard categories are 'Interaction with manned vessels and detection of objects' and 'Cyber-attacks'. Expert opinion leads to the belief that MASS could introduce some new types of risks that do not exist in conventional operations. In addition, according to Table 6 the top three hazards are all related to the 'Interaction with manned vessels and detection of objects'. The importance of the top two hazards has also been highlighted in previous studies; see Burmeister et al. (2014b), Porathe et al. (2014), Rødseth and Burmeister (2015), and Wróbel et al. (2018b) for studies related the 'Interaction with vessels and detection of objects', and Katsikas (2017), Ghaderi (2018), Tam and Jones (2018), and Wróbel et al. (2018b; 2020) for the 'cyber-attacks' hazard category. Based on the relevant literature, there is still much work needed in order to meet the desired safety level for autonomous operations. Our results suggest that shipping companies that are interested in developing and operating autonomous vessels should prioritise research on technology and development that can quickly and correctly detect ships and objects. Moreover, maritime cybersecurity is becoming an important issue. Operators should address the relevant risks by, among others, setting up standardised operation procedures, and cybersecurity awareness and training (Park et al., 2019). In addition, our results also show that 'Heavy weather' is a considerable hazard to autonomous ship operations; this is in line with Rødseth and Burmeister (2015) who state that heavy weather may make it difficult to safely manoeuvre an autonomous vessels.

The results of the sensitivity analysis show that 'Failure due to the breakdown of communication link' and 'Failure due to strong tidal effect' are the hazards associated with the lowest risk values. Despite Wróbel et al. (2020) stating that specialists pay much attention to communication, the result of our research shows that 'failure due to the breakdown of communication link' contributes to the low risk values, compared to other hazards that need to be dealt with first.

### 5.2 Conclusions

In this paper, we have initially identified the hazards of MASS operations and categorised them into six categories through literature review. In addition, we conducted a number of interviews

to validate and explore more hazards that had not been identified during the literature review. Our study utilised a combination of FMEA, with ER and RBN in order to rank the identified hazards. The input values are derived from surveys based on domain expert judgements.

The results show that 'Interaction with manned vessels and detection of objects' is the hazard category that contributes the most to the overall risk of MASS operations, followed by 'Cyberattacks', 'Human error' and 'Equipment failure'. Our analysis shows that 'Failure in detection of semi-submerged objects that are adrift' is the hazard of the highest risk value (falls actually into the extremely high risk zone), followed by 'Failure to determine correct action when interacting with vessels that are: towing, restricted in an ability to manoeuvre, or trawling', and 'Collision due to poor interaction with manned vessel(s) in heavy traffic'. All the above three hazards are under the 'Interaction with manned vessels and detection of objects' hazard category.

The results of this work can lead to better understanding of the relevant hazards and their risk levels. Although this area is attracting more and more interest, as shown by the increasing number of publications, we note that the literature is still scarce, and more research is needed. One suggestion is to use a more detailed breakdown of hazards and hazard categories so that the associated influencing factors can be further analysed, which can lead to more specific and more effective risk control measures.

During the research process, we reckon some limitations of this work. Firstly, obtaining the opinion of more experts could help enhance the findings. Secondly, a study needs to be carried out to identify and analyse potential risk control options to address the major hazards that this study has identified. Our approach can actually be used to calculate the impact of the introduction of such options. As a final remark, we highlight the need for more research in the area, which is actually now getting more and more attention.

# Acknowledgements 

This research is funded by The Chartered Institute of Logistics and Transport (CILT) Seed Corn Fund 2018-2019 and financially supported by the EU ERC-COG-2019 project TRUST 864724 .
