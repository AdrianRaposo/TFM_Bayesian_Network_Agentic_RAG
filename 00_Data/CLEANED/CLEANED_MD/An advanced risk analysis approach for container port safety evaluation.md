# LJMU Research Online 

Alyami, H, Lee, PT-W, Yang, Z, Riahi, R, Bonsall, S and Wang, J
An advanced risk analysis approach for container port safety evaluation
http://researchonline.ljmu.ac.uk/id/eprint/1155/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Alyami, H, Lee, PT-W, Yang, Z, Riahi, R, Bonsall, S and Wang, J (2014) An advanced risk analysis approach for container port safety evaluation. MARITIME POLICY \& MANAGEMENT, 41 (7). pp. 634-650. ISSN 0308-8839

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# AN ADVANCED RISK ANALYSIS APPROACH FOR CONTAINER PORT SAFETY EVALUATION 

Hani Al YAMI ${ }^{a}$, Paul Tae-Woo LEE ${ }^{\text {b }}$, Zaili YANG ${ }^{\text {a }}$, Ramin RIAHI ${ }^{\text {a }}$, Stephen BONSALL ${ }^{a}$ and Jin WANG ${ }^{a}$<br>${ }^{\text {a }}$ Liverpool Logistics Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, Liverpool, UK.<br>${ }^{\text {b }}$ Department of Business Administration, Soochow University, Taiwan.

## ABSTRACT

Risk analysis in seaports plays an increasingly important role in ensuring port operation reliability, maritime transportation safety and supply chain distribution resilience. However, the task is not straightforward given the challenges, including that port safety is affected by multiple factors related to design, installation, operation and maintenance and that traditional risk assessment methods such as quantitative risk analysis cannot sufficiently address uncertainty in failure data. This paper develops an advanced Failure Mode and Effects Analysis (FMEA) approach through incorporating Fuzzy Rule-Based Bayesian Networks (FRBN) to evaluate the criticality of the hazardous events (HEs) in a container terminal. The rational use of the Degrees of Belief (DoB) in a fuzzy rule base (FRB) facilitates the implementation of the new method in Container Terminal Risk Evaluation (CTRE) in practice. Compared to conventional FMEA methods, the new approach integrates FRB and BN in a complementary manner, in which the former provides a realistic and flexible way to describe input failure information while the latter allows easy updating of risk estimation results and facilitates real time safety evaluation and dynamic risk-based decision support in container terminals. The proposed approach can also be tailored for wider application in other engineering and management systems, especially when instant risk ranking is required by the stakeholders to measure, predict, and improve their system safety and reliability performance.

Key words: Port safety, Maritime risk, FMEA, Bayesian networks, Maritime Transport

## 1. Introduction

A careful literature review has disclosed that safety persistently occupies a backseat role

[^0]
[^0]:    ${ }^{1}$ Corresponding Author's Address: Zaili Yang, Liverpool Logistics Offshore and Marine Research Institute, Liverpool John Mores University, Liverpool, UK. Email: z.yang@ljmu.ac.uk

within port research, being overwhelmed by other aspects involving efficiency evaluation (Wu and Goh 2010; Demirel et al., 2012), port competition (Lam and Yap, 2011a), geographical analysis and regional port development (Notteboom and Rodrigue, 2005; Lee and Cullinane, 2005; Lam and Yap, 2011b), port policy and port governance (Brooks and Cullinane, 2007; Wang et al., 2012). Among the studies addressing port safety, many focused on policy issues based on descriptive or qualitative approaches, which together with the above challenge, critically points out the need for developing a robust and efficient quantitative risk analysis approach in order to prioritize hazards in ports (Yang et al., 2014). Furthermore, significant academic effort is devoted to port centric logistics, maritime logistics, and port operational optimization (e.g., Liu et al., 2002; Vis et al., 2002; Steenken et al., 2004; Güntheret et al., 2006; Song and Lee, 2009) however, there are relatively few studies on port safety and risk (Darbra and Casal, 2004; Yang et al., 2010; Mabrouki et al., 2014; Yang et al., 2010), revealing a research gap to be fulfilled. Safety analysis in a broad scope can be defined as the study of the consequences of system failures in relation to possible harm to people and/or damage to the environment or property including financial assets (HSE, 2001).

In addition, a review of 984 papers published in Maritime Policy \& Management (MPM) by Notteboom et al. (2013) reveals that a core theme in seaport studies over the past 40 years of its existence discloses that research in ports has evolved its research frameworks and techniques in many fields such as geography, econometrics, welfare economics, operations research, logistics/supply chain management and strategic management. In the last five years the themes of ports in transport and supply chains, port governance and port competition and competitiveness were dominating port research. On the other hand, in the first two decades of MPM, regulatory issues referring to competition, pricing, financing, environmental, safety and security related policy practices were research themes attracting much attention. Since then, port terminals including container terminals have been developed rabidly and aggressively, creating a growing interest in examining the prospects and limits of safety aspects in such growth and complex activities in port operations. However, the research on safety and security analysis of container terminal operations in a quantitative way has not yet been well conducted but the issue has been recently raised in Yang et al., (2014). If the risk result cannot be quantified, it may well not motivate the industrial stakeholders to take control measures confidently.

Traditional quantitative risk analysis methods such as Failure Mode and Effects Analysis (FMEA) can be used to identify the hazards of high risks. However, a careful literature

review reveals that a high level of uncertainty in data exists in port risk analysis, for which novel flexible risk approaches are needed. New methods based on uncertainty treatment theories such as fuzzy set modelling, Dempster-Shafer theory, grey theory, Monte Carlo simulation, Bayesian Networks (BNs), Markov models and artificial neural networks have contributed to enriching the literature by overcoming glitches inherent in the traditional FMEA and at the same time enhancing the performance of FMEA, especially when criticality analysis is conducted (Yang et al., 2008). Moreover, although contributing to the development of more precise failure criticality analysis, such new methods still render themselves vulnerable by losing advances of the conventional FMEA method, visibility, and easiness.

Yang et al. (2008) proposed a hybrid Fuzzy Rule-based Bayesian Reasoning (FuRBaR) methodology to delineate the role of Bayesian Reasoning in fuzzy rule based risk inference in a complementary way. It uses the Bayesian marginalization rule to accommodate all relevant IF-THEN rules with belief structures and calculates failure priority values in posterior probabilities, while a fuzzy rule base (FRB) is employed as an effective way to elicit expert judgments for rationalizing the configuration of subjective probabilities. Although showing much attractiveness, it still has a significant applicable problem, which is associated with the establishment of FRB with a rational structure of degrees of belief $\left(\mathrm{DoB}^{2}\right)$.

This paper aims to develop an advanced safety analysis approach through incorporating Fuzzy Rule-Based Bayesian Networks (FRBN) to evaluate the criticality of the hazardous events in a container terminal. The new method rationalizes the DoB distribution and develops a new risk based decision support tool for effective seaport risk evaluation. To achieve the aim, this paper is organized as follows. An analytical overview of FMEA particularly concerning its application in port risk analysis is carried out in Section 2. Section 3 describes the novel FMEA framework capable of incorporating different weights of risk parameters into FRB. A real case study regarding container terminal safety evaluation is investigated to demonstrate the feasibility of the new methodology in Section 4. Section 5 concludes the paper. Consequently, this study makes a contribution to facilitating FMEA applications and enhancing container terminals' safety management.

[^0]
[^0]:    ${ }^{2}$ DoB is a quantitative unit between zero and one used to express the confidence level of an expert when making subjective evaluate.

# 2. Literature review 

Safety of seaports is playing an increasingly important role in ensuring port operations, thus attracting much risk related research from operational, organizational and economic perspectives (Legato and Monaco, 2004; Marlow and Casaca, 2003; Trbojevic and Carr, 2000; Fabiano et al. 2010; Mokhtari et al., 2011; Soares and Teixeira, 2001). A review by Pallis et al. (2010) on 395 port-related journal papers published between 1997 and 2008 discloses that, despite the criticality of safety and security in efficient supply chains and international trade, risk analysis persistently occupied a backseat role within port research being overwhelmed by other aspects involving efficiency analysis, port competition, geographical analysis and spatial evolution, port policy and governance, to name but a few (Yang et al., 2014).

FMEA is one of the most widely applied hazard identification and risk analysis methods due to its visibility and easiness (Braglia et al., 2003). The traditional FMEA method has three fundamental attributes, namely failure occurrence likelihood (L), consequence severity (C), and probability of failures being undetected (P), which are employed to assess the safety level of each failure mode and to calculate their risk priority numbers (RPN) (Yang et al., 2008). The classical RPN approach suffered from some critical drawbacks such as insufficient quantifying of the effectiveness of corrective/preventive action and an inability to consider other risk parameters apart from L, C and P and their associated weights (Yang et al., 2008). Furthermore, it dealt only with numerical evaluation that can be inaccurate and also difficult in assigning intangible quantities (Braglia et al., 2003). The method has, therefore, incorporated advanced uncertainty modelling techniques such as fuzzy sets (Zadeh, 1965), grey theory (Deng, 1989), evidential reasoning (Yang, 2001) and BNs (Jenson, 2001) to facilitate its practical applications in maritime and offshore engineering safety (Sii et al., 2001), system reliability and failure mode analysis (Braglia et al., 2003), engineering system safety (Liu et al., 2005) and maritime and port security (Yang et al., 2009). Among the quantitative development of FMEA, a FuRBaR approach was proposed by using a Bayesian reasoning mechanism to conduct FRB risk inference in order to achieve sensitive failure priority values without compromising the simplification of the traditional RPN approach.

Compared to the RPN approach, FuRBaR uses domain expert knowledge to develop FRB

with a structure of DoB and to establish the connections between the three risk parameters L, C and P. For example,

IF $L$ is very low, $C$ is negligible and $P$ is highly unlikely THEN the safety level is good with a $100 \%$ DoB.

IF $L$ is very low, $C$ is negligible and $P$ is unlikely THEN the safety level is good with $91 \%$ DoB and average with a $9 \%$ DoB.

While FuRBaR facilitates risk studies, it still exposes some problems when being applied in port safety practice on how to rationalize the distribution of DoBs in the THEN part of FRB. It needs to be appropriately addressed in order to stimulate the implementation of FuRBaR in real safety critical systems. This work will make contributions to the establishment of a new mechanism for rational DoB distributions in FuRBaR in theory (Section 3) and the development of a new risk based decision tool for effective seaport risk evaluation in practice (Section 4).

# 3. Methodology of modelling container terminal risk evaluation 

Due to the lack of objective failure data, a subjective knowledge based fuzzy IF-THEN rule base approach is proposed to model Container Terminal Risk Evaluation (CTRE). A rule-based method consists of IF-THEN rules and an interpreter controlling the application of the rules. Risk analysis in FMEA is described as the relationship between risk parameters in the IF part and risk levels in the THEN part. These IF-THEN rule statements are used to formulate the conditional statements comprising the complete knowledge base.

The steps for developing novel FMEA analysis for modelling CTRE based on the proposed FRBN approach are outlined as follows:

1. Establish a FRB with belief structure in FMEA for CTRE.
2. Identify HEs (failure modes) in container terminals.
3. Prioritise the HEs using the new approach with rational distribution of DoBs in FRB.
4. Validation by using sensitivity analysis techniques.

### 3.1 Establishment of a FRB with belief structure in FMEA for CTRE

In traditional FMEA, three risk parameters, L, C and P, are used to evaluate the safety level of each failure mode. However, when conducting CTRE, the impact (I) of a failure to

the resilience of port operational systems is crucial, thus being taken into account in this study. Consequently, the four risk parameters (L, C, P and I) are constructed to form the IF part while the risk level (R) of failures is presented in the THEN part in a FRB. To facilitate subjective data collection, a set of linguistic grades of High, Medium, and Low is employed to describe L, C, P, I and R (Tah and Carr, 2000; Wang et al., 2008). The degrees of the parameters estimated for each HE are based on knowledge accumulated from past events and their definitions are presented in Table 1 taking into account domain experts' judgements ${ }^{3}$.

Table 1. The linguistic grades for each HE

(L) | High (H) | Occurs more than once per month  |
(C) | High (H) | Death or permanent total disability; loss/damage of major facilities; severe environmental damage  |

[^0] [^0]: ${ }^{3}$ The backgrounds and experience of the experts are described in Section 3.2.


A belief structure is introduced to model the THEN part in a FRB. For example,

- Rule 1: If $L$ is Low, $C$ is Low, $P$ is Low and $I$ is Low, then $R$ is Low with a 100\% DoB, Medium with a 0\% DoB and High with a 0\% DoB.
- Rule 2: If $L$ is Low, $C$ is Low, $P$ is Low and $I$ is Medium, then $R$ is Low with a 75\% DoB, Medium with a 25\% DoB and High with a 0\% DoB.
- Rule 3: If $L$ is Low, $C$ is Low, $P$ is Low and $I$ is High, then $R$ is Low with a 75\% DoB, Medium with a 0\% DoB and High with a 25\% DoB.

It can be seen from the above three rules that a proportion method is used to rationalise the DoB distribution. Specifically speaking, the DoB belonging to a particular grade in the THEN part is calculated by dividing the number of the risk parameters, which receive the same grade in the IF part, by four. For instance, in Rule 1, the number of the risk parameters receiving the Low grade in the IF part is four. The DoB belonging to Low in the THEN part is therefore computed as $100 \%(4 / 4=100 \%)$. In Rule 2, the numbers of the risk parameters receiving the Low and Medium grades in the IF part are three and one, respectively. The DoBs belonging to Low and Medium in the THEN part are therefore 75\% $(3 / 4=75 \%)$ and $25 \%(1 / 4=25 \%)$ respectively. In a similar way, the FRB used in CTRE containing 81 rules $(3 \times 3 \times 3 \times 3)$ with a rational DoB distribution is obtained and presented in Table 2.

Table 2. The established FRB with a belief structure for CTRE

(R1) | Medium
(R2) | High
(R3)  |

# 3.2 Identification of the hazardous events (failure modes) in container terminals

Container terminals are often described as open systems of container flows within a quayside for cargo loading and unloading and a landside where containers are moved from/to trucks and/or trains. A stacking area for storing containers normally between the quayside and landside is equipped with various facilities for the decoupling of the quayside and landside operations. The hazardous events investigated in this study are those that occurred within the container terminal area defined above. The risks associated

with the external interfaces of the terminal in the shore side and sea side are not taken into account in this study (see Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. Scope of container terminal operations (Al Yami et al., 2013)

In terms of container terminal operations conducted by a large number of workers and equipment in a variety of activities at different sites, safety issues are of significant importance. In respect of the container terminal operational safety, the performance of different container terminals can be determined by different elements that are continuously taking into account a range of internal and external factors influencing the productivity of the system (Legato and Monaco, 2004).

Moreover, the application of operational safety practice and qualified duty holders is essential. It was addressed by the UK Maritime and Coastguard Agency (MCA, previously known as Marine Safety Agency (MSA)) through Formal Safety Assessment (FSA) to the International Maritime Organization (IMO) for the purposes of improving the safety of and pollution prevention within ports (Trbojevic and Carr, 2000). However, currently there is no evidence that international safety standards address the safety performance within container terminals. Several attempts were made that can be defined as individual contributions for safety practice in container terminals. For instance, the Health and Safety Executive (HSE) has focused comprehensively on health, safety, and environmental related issues for offshore terminal operations, particularly as a result of the inquiry into the Piper Alpha disaster that took place in 1988 (Mokhtari et al., 2011).

In October 2010, the UK HSE with the cooperation of the port industry published the Guidance on Safe Design, Construction, Operation, Management, and Maintenance of Ports and Terminal Facilities to help workers in container terminals identify relevant risk sources in various duties under health and safety legislation. Moreover, the Department of Transport in the UK required all marine ports to perform risk assessment of their marine operations in order to put into practice a safety management system (DETR, 2009). In addition, the International Chamber of Shipping (ICS) and the World Shipping Council have developed guidelines for best practices in the industry including the safe transport of containers by sea and proposed in a statement to the IMO Maritime Safety Committee, that the IMO should establish a universal international regulatory requirement emphasising that the marine terminal must weigh export cargo containers (ICS, 2011).

In addition, in May 2012, the Port Equipment Manufacturers Association (PEMA) published new industry recommendations on equipment protection and human safety in container yards addressing the minimum safety specifications for quay container cranes. PEMA's decision to compile its initial publication regarding safety standards for quay cranes was published in June 2011 as a joint initiative with the Through Transport Mutual Insurance Association Limited (TT Club) and the International Cargo Handling Coordination Association. It was prompted by the results of the global analysis carried out by the TT Club that showed that $34 \%$ of asset related insurance claims were directly related to quay container cranes (Stiehler, 2012). As a result from all of the aforementioned guidelines, codes of conduct or requirements are not yet recognised worldwide in the port industry and it is a subject of individuality.

In light of the above, HEs associated with container terminal operations including cargo handling equipment and transport facilities were identified through a careful literature review (Christou, 1999; Yi et al., 2000; Darbra and Casal, 2004; Shang and Tseng, 2010; DETR, 2009; HSE, 2010; Stiehler, 2012), which enables us to identify sources of significant hazards in container terminals and provides a good view on possible solutions to some hazards. Next, the process of determining the investigated HEs is conducted by using a "What-If Analysis" technique (Golfarelli et al., 2006) in a brainstorming meeting with domain experts. The preliminary study of determining the investigated HEs took place in July 2012 in the UK with seven safety/security officers, port managers and scholars. Moreover, in September 2012, another meeting took place in the Kingdom of

Saudi Arabia (KSA) with five safety/security officers and port managers to further study the investigated HEs. The experts selected, based on their experience in Table 3, are actively working in container terminals and/or researching on container terminals for over 20 years.

Table 3. Experts' knowledge and experience



During the meetings, they identified the major threats and impacts posed by 76 risk sources and hazard events in container port operations. Consequently, a hierarchy of 24 significant hazards and the origin of their types for container terminal operations is constructed and presented in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Hierarchy of 24 significant hazards of container terminal operations

# 3.3 Prioritization of the HEs using the new approach with rational DoBs in FRB. 

Due to possible uncertainty involved, failure inputs are fed into the FMEA modelling using

the defined linguistic grades with DoBs. It means that multiple rules will be employed in risk evaluation for a particular HE, requiring an appropriate tool capable of synthesising the associated DoBs in the THEN parts of different involved rules. The ability of BN in capturing non-linear causal relationships, and modelling DoBs in the THEN part of FRB, has been known (Yang et al., 2008). To use BN, the FRB developed in Section 3.1 needs firstly to be represented in the form of conditional probabilities. For example, Rule 2 in Table 1 can be displayed as follows:
$R_{2}$ : IF Low (L1), Low (C1), Low (P1) and Medium (I2), THEN \{(0.75, Low (R1)), (0.25, Medium (R2)), (0, High (R3))\}.

It can be further expressed in the form of conditional probability as follows:
Given $L 1$, and $C 1, P 1$ and $I 2$, the probability of $R h(h=1,2,3)$ is $(0.75,0.25,0)$ or $p(R h \mid L 1, C 1, P 1, I 2)=(0.75,0.25,0)$
where " $\mid$ " symbolizes conditional probability.

Using a BN technique, the FRB constructed in FMEA for CTRE can be modelled and converted into a five-node converging connection. It includes four parent nodes, $N_{L}, N_{C}, N_{P}$ and $N_{I}$ (Nodes $L, C, P$ and $I$ ) and one child node $N_{R}$ (Node $R$ ). Having transferred the rule base into a BN framework, the rule-based risk inference for the failure criticality analysis will be simplified as the calculation of the marginal probability of the node $N_{R}$. To marginalize $R$, the required conditional probability table of $N_{R}, p(R \mid L, C, P, I)$, can be obtained using Table 1 and Eq.(1). It denotes a $3 \times 3 \times 3 \times 3$ table containing values $p(R h \mid L i$, $C j, P k, I l)(h, i, j, k, l=1,2,3)$.

Port risk analysts can evaluate a HE using their subjective judgments based on real observations with respect to the four risk parameters and their associated linguistic grades (defined in Table 1). Averaging the DoBs assigned by multiple experts to the linguistic grades of each parameter enables the calculation of the prior probabilities $p(L i), p(C j)$, $p(P k)$ and $p(I l)$ of the four parent nodes, $N_{L}, N_{C}, N_{P}$ and $N_{I}$. The marginal probability of $N_{R}$ can be calculated as

$$
p(R h)=\sum_{i=1}^{3} \sum_{j=1}^{3} \sum_{k=1}^{3} \sum_{l=1}^{3} p(R h \mid L i, C j, P k, I l) p(L i) p(C j) p(P k) p(I l)(h=1,2,3)
$$

To prioritize the failures, $R h(h=1,2,3)$ requires the assignment of appropriate utility values $U_{R h}$. The utility values can be defined as $U_{R 1}=1, U_{R 2}=10$ and $U_{R 3}=100$ (Wang et al., 1995; Yang, 2001 and Yang et al., 2008). Then a new Risk Ranking Index value RI can be developed as

$$
R I=\sum_{h=1}^{3} p(R h) U_{R h}
$$

where the larger the value of $R I$ is, the higher the risk level of a HE.

# 3.4 Validation 

One of the most popular mechanistic validation methods is sensitivity analysis. It is conducted to test the accuracy of the belief structures based on subjective judgments. Testing the sensitivity in the FRBN method provides an analytical judgment for RI or the safety index. Parameter sensitivity is usually performed as a series of tests in which the modeller sets different parameter values to measure the changes in the model caused by a change in the risk parameter (Lucia and Mark, 2001). There are at least two axioms that can be used as a mechanism for validating the proposed BN model (Jones et al., 2010).

Axiom 1. A slight increase/decrease in the prior subjective probabilities of each input node should certainly result in the effect of a relative increase/decrease of the posterior probability values of the output node.

Axiom 2. The total influence magnitudes of the combination of the probability variations from $x$ attributes (evidence) on the values should be always greater than the one from the set of $x-y(y \in x)$ attributes (sub evidence).

## 4. A real case study on CTRE

To demonstrate the feasibility of the proposed method, an anonymous container terminal was selected to conduct its CTRE. A questionnaire was designed to collect the failure input information from three experienced safety officers/port managers, who are together in charge of the safety of the investigated container terminal. The experts selected are actively working at the investigated container terminal with over 20 years working experience and their knowledge is described in Table 4.

Table 4. Experts' knowledge and experience on the case study


In the questionnaire, they were requested to evaluate each of the 24 significant HEs in the investigated port with respect to the four risk parameters in terms of their associated linguistic grades and DoBs.

The feedback received from the three experts are first combined (by conducting an average calculation) to produce failure input values for the four risk parameters. The averaged (arithmetic mean) failure input will be then used in the new approach (in Section 3.3) based on the new FRB with rational DoBs (in Section 3.1) to rank the 24 HEs. For instance, to evaluate an event of a Collision of a Rail Mounted Gantry crane with a Trailer (CRMGT), i.e. HE1, the failure input values of the four risk parameters are obtained and calculated, as shown in Table 5.

Table 5. Prior Probabilities of $N_{L}, N_{C}, N_{P}$ and $N_{I}$ when evaluating HE1 (CRMGT)



Given Eq (1), the FRB in Table 1 can be converted to obtain $p(R h \mid L i, C j, P k, I l)$. Once the prior probabilities of the five nodes in BN based FMEA are obtained, the risk level of HE1 (CRMGT) can be calculated by Eq (2) as $p(R h)=\{($ 42.5\% Low, 17.9\% Medium, 39.6\% High) $\}$. The result can be explained as the risk level of CRMGT being low with a $42.5 \%$ DoB, medium with a $17.9 \%$ DoB and high with a $39.6 \%$ DoB. The calculation can be computerized using the HUGIN software (Andersen et al., 1990) which is one of the most used software packages to facilitate Bayesian network computation. As shown in Figure 3, any risk input with reference to the four risk parameters can trigger a change in the output node, which helps realise the automation of port safety evaluation for instant ranking. Next, Eq (3) is used to calculate the RI value of HE1 (CRMGT) as 41.82 ( $=42.5 \% \times 1+17.9 \%$ $\times 10+39.6 \% \times 100$ ). Similarly, the RI values of the 24 HEs are obtained and presented in Table 6.
![img-2.jpeg](img-2.jpeg)

Figure 3. Risk evaluation of HE1 (CRMGT) using HUGIN software

Table 6. Risk ranking index values of hazardous events (HEs)




The HEs associated with container terminal operations may vary, depending on the unique safety characteristics of an individual container terminal. For the investigated container terminal, the new method delivers the result shown in Table 6. The hazardous event of a collision between a quay crane and a ship (HE4) is the most significant, followed by HE13 (person slips, trips and falls whilst working on surfaces with presence of leaking cargo), HE15 (person slips, trips and falls whilst working on surfaces with presence of oils), HE17 (person handling dangerous goods in containers that have not been declared) and HE6 (breakdown of a crane due to human error). Such a result keeps consistency with the safety analysis in the port using traditional methods to a large extent based on the three experts' judgements.

The above numerical case study highlights some meaningful implications. First, compared to traditional FMEA, it demonstrates that the combination of fuzzy sets and BNs, provides an effective tool to incorporate subjective judgements for characterizing a criticality analysis on prioritising failures in FMEA under uncertainty. In addition, it improves both the accuracy and visibility of FMEA as well as provides a powerful risk evaluation tool for port safety management. Secondly, it contributes to quantifying risk analysis with prioritization of HEs in a container port as shown in Table 6. As a result, terminal operators are able to easily update the risk estimation results, facilitating real time safety evaluation and dynamic risk-based decision support in container terminals. Thirdly, this novel approach helps terminal operators prepare their risk management and resilient system analysis considering the features inherent in their terminals. Fourthly, rationalising the DoB distribution of FRB by employing the same set of linguistic grades in both IF and

THEN parts, the new approach leads terminal operators to simplify the communication between risk input and output based on DoBs and enables them to easily put FRBN in CTRE into practice. Finally, the approach describes a powerful and transparent safety evaluation tool in a scientific manner. It provides a sound basis for port safety managers and analysts to optimise the safety resources to the high risks as well as effectively evaluate the cost effectiveness of the risk control measures by comparing the reduction of risk index values of the hazards with and without the implementation of the measures. It will also help develop rational port safety management policy by taking into account quantitative risk assessment and cost benefit analysis in the long term. The proposed method can instantly rank the risks of HEs of a container terminal according to the stakeholders' needs so that they can measure, predict, and improve safety and reliability performance of their system.

A sensitivity analysis has been carried out to validate the reliability of the developed approach. The model with its simulation illustrated in Figure 3 can be verified by satisfying the two axioms involved in this process as described in section 3.4. The examination of the model is conducted for HE1 CRMGT as follows.

By setting the prior probability value of the node "consequences severity" to be $100 \%$
"High", the posterior probability value of the output "RiskEvaluation = High" increases from $39.60 \%$ to $62.1 \%$ as shown in Figure 4. Similarly, checking all HEs verifies the model with respect to Axiom 1.
![img-3.jpeg](img-3.jpeg)

Figure 4: The evaluation of "RE" given a piece of evidence to " $\mathrm{C}=100 \%$ High" for HE1

Given that further change to the node $I$ is set to be "High" with a $100 \%$ DoB, a further increase of the posterior probability value of the output "RiskEvaluation = High" occurs from $39.60 \%$ to $70.43 \%$ as shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5: The evaluation of "RE" given evidence to " $\mathrm{C}=100 \%$ High" and " $\mathrm{R}=100 \%$ High" for HE1

Furthermore, if the node $P$ is also set to be "High" with a $100 \%$ DoB, then the posterior probability value of the output "Risk Evaluation = High" further increases from 39.60\% to $93.75 \%$ as shown in Figure 6. Compared to the results in Figures $4-6$, it can be seen that the DoB belonging to "High" in node $R$ keeps increasing with more risk parameters receiving evidence to support "High" risk input. It means that the total influence magnitude of the combination of the probability variations from three attributes is always greater than the ones of two attributes and one attribute. This is in line with Axiom 2.
![img-5.jpeg](img-5.jpeg)

Figure 6: The evaluation of "RE" given evidence to " $\mathrm{C}=100 \%$ High", " $\mathrm{R}=100 \%$ High" and $\mathrm{D}=100 \%$ High" for HE1

# 5. Conclusion 

System safety analysis often requires the use of domain experts' knowledge when risk records are incomplete. The combination of fuzzy set modelling and BNs, notably FRBN, provides an effective tool to incorporate subjective judgements for characterizing a criticality analysis on prioritising failures in FMEA under uncertainty. The new mechanism proposed to rationalise the DoB distribution of FRB by employing the same set of linguistic grades in both IF and THEN parts simplifies the communication between risk input and output and facilitates its implementation in CTRE in practice. Compared to the conventional FMEA, this paper also shows that the new method is capable of presenting sensitive and flexible risk results in real situations by simplifying the description of fuzzy failure information, improving both the accuracy and visibility of FMEA. More importantly, it provides a powerful risk evaluation tool for port safety management. The proposed method highlights its potential in facilitating risk analysis of system design and operations in a wide context when being appropriately tailored to study other container ports. Managerial, policy implications, natural and political factors can also be investigated in a similar way in order to provide a panoramic view on terminal risk analysis.

## Acknowledgements

The authors are grateful to independent reviewers who provided useful feedback to bring this article to fruition. This study is partially funded by two EU projects (REFERENCE (314836) and ENRICH (612546) Marie Curie IRSES, 2013 - 2017) and by King AbdulAziz University.
