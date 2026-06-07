# Article 

## An Integrated FTA-FMEA Model for Risk Analysis of Engineering Systems: A Case Study of Subsea Blowout Preventers

Mahmood Shafiee ${ }^{1}$ (D) Evenye Enjema ${ }^{1, *}$ and Athanasios Kolios ${ }^{2}$<br>1 Department of Energy and Power, Cranfield University, College Road, Bedfordshire MK 43 0AL, UK; m.shafiee@cranfield.ac.uk<br>2 Department of Naval Architecture, Ocean \& Marine Engineering, University of Strathclyde, 100 Montrose Street, Glasgow G4 0LZ, UK; athanasios.kolios@strath.ac.uk<br>* Correspondence: e.m.enjema@cranfield.ac.uk; Tel.: +44-1234-750111

Received: 3 February 2019; Accepted: 15 March 2019; Published: 21 March 2019


#### Abstract

Engineering systems such as energy production facilities, aviation systems, maritime vessels, etc. continue to grow in size and complexity. This growth has made the identification, quantification and mitigation of risks associated with the failure of such systems so complicated. To solve this problem, several advanced techniques such as Fault Tree Analysis (FTA), Failure Mode and Effects Analysis (FMEA), Reliability-Block Diagram (RBD), Reliability-Centered Maintenance (RCM), Monte-Carlo Simulation (MCS), Markov Analysis (MA) and Bayesian Networks (BN) have been developed in the literature. In order to improve the strengths and eliminate the drawbacks of classical techniques, some hybrid models have been recently developed. In this paper, an integrated FTA and FMEA model is proposed for risk analysis of safety-critical systems. Minimal cut sets derived from the fault trees are weighted based on Birnbaum's measure of importance and then the weights are used to revise Risk Priority Numbers (RPNs) obtained from the use of traditional FMEA techniques. The proposed model is applied to a Blowout Preventer (BOP) system operating under erratic and extreme conditions in a subsea oil and gas field. Though those failures caused by kill valves and hydraulic lines remain among the top risks in the BOP system, significant differences are revealed in risk rankings when the results from the hybrid approach are compared with those obtained from the classical risk analysis methods.


Keywords: Fault Tree Analysis (FTA); Failure Mode and Effects Analysis (FMEA); blowout preventer (BOP); risk analysis; minimal cut set; Birnbaum's measure

## 1. Introduction

A system is considered complex if it comprises of several interacting components whose series/parallel breakdown is impossible and the overall task cannot be obtained by the summation of individual components' activities [1]. Regardless of the degree of intricacy of the complex system under study, some components are deemed critical, relative to others, regarding the safety and functionality of the entire system. Due to the increasing complexity of engineering systems, the identification and evaluation of risks associated with the failure of individual components is usually the starting point for efficient reliability and safety analysis. For this purpose, several advanced techniques such as Fault Tree Analysis (FTA), Failure Mode and Effects Analysis (FMEA), Reliability Block Diagram (RBD), Reliability-Centered Maintenance (RCM), Monte-Carlo Simulation (MCS), Markov Analysis (MA) and Bayesian Networks (BN) have been developed in the literature [2-4].

FTA is a 'top down' Boolean logic tool commonly used to identify possible causes for potential operating hazards or an undesired event. FMEA is another risk analysis technique that is extensively

used across different industries, such as aerospace, automotive, energy, transport, etc. for determining failure modes and corresponding effects on system performance. The successful application of both the FTA and FMEA techniques has increased their adoption in several reliability and safety engineering analyses studies. However, due to inherent limitations of each technique, coupled with the growing complexity of engineering systems, the use of hybrid models has become very popular in recent years.

Integrated FTA and FMEA has been employed coherently and concurrently to enhance and complement each other in several reliability applications. Forward integration (i.e., FMEA to FTA) and backward integration (i.e., FTA to FMEA) have been proposed, with divers' advantages associated with each integration direction [5,6]. Lutz \& Woodhouse [7] also propounded a bi-directional intertwine of both techniques and used it to certify safety-critical software, paving the way for numerous studies on integrating the software domains of both tools. The combination has successfully been applied in civil aerospace and automotive domains. To effectively achieve a set reliability goal, ensure thoroughness and completeness of analysis, and improve quality of analysis without compromise on overall safety, it is necessary to redefine the underlying criteria governing techniques in a combinatorial framework. In Xiao et al. [8], only the occurrence (O) of a failure is taken into consideration because the complex system under consideration was non-repairable. Equal importance was given to all minimal cut sets in terms of their effect on system performance, which caused the severity (S) of failure for all the system components to be same.

By using the minimal cut sets theory and Birnbaum's measure of importance, this paper aims to develop a modified FMEA approach in the backward integration with FTA tool for the identification, evaluation and prioritization of failure risks in safety-critical systems. In order to appropriately identify and rank components according to their criticality, a weight will be assigned to the Risk Priority Number (RPN) associated with each component's failure mode. This weight represents the importance of the component in overall system functionality. A case study of a subsea Blowout Preventer (BOP) is presented to illustrate the applicability of the proposed model.

The rest of the paper continues with a background review of risk analysis techniques in Section 2, followed by a full presentation of our proposed FTA-FMEA methodology in Section 3. Section 4 presents the case study and Section 5 concludes our paper.

# 2. Research Background 

### 2.1. Fault Tree Analysis (FTA)

FTA is a deductive technique for identifying, evaluating, and modeling the interrelationship between events leading to a failure or an undesired state [9]. It is a scientifically sound and proven technique that models complex system interactions in an easy-to-read visual model. Containing qualitative (cut sets) and quantitative (probabilities) sides, the structured, repetitive and methodical construction process results in layers, levels and branches. Once a logical and systematic picture of all immediate and basic causes leading to top event are identified, undesired events are clearly depicted. Though FTA employs Boolean logic to combine a series of lower-level events causing an undesired state of a system, the technique is static and incapable of examining multiple failures [10]. It also is unintuitive and lacks the ability to properly account for dynamic interactions between components. These and many other drawbacks make FTA limited in modeling dynamic complex systems.

### 2.2. Failure Mode and Effects Analysis (FMEA)

FMEA is a highly structured approach through which all potential failure modes of a system and their effects can be identified, evaluated, and prioritized. The technique can result in cost/time-savings when employed during early design stages by exposing probable operational challenges and eliminating cascading failures. In this technique, the risk score for each failure mode is obtained by

multiplying the individual scores for three risk factors of severity (S), occurrence (O), and detectability (D). This composite risk is called "Risk Priority Number (RPN)" and is calculated by:

$$
\mathrm{RPN}=\mathrm{S} \times \mathrm{O} \times \mathrm{D}
$$

where the risk factors $\mathrm{S}, \mathrm{O}$ and D are rated on a scale $1-10$ for each failure mode using the guidelines presented in reference [11]. Therefore, the RPN values for different failure modes will range between 1 and 1000. Engineers should assign a threshold RPN value to classify failure modes. For instance, in the current FMEA technique, precautions are taken for all failure modes whose RPN values exceed 100. Thus, a failure mode with $\mathrm{RPN}=100$ is considered as 'corrective action required', whereas another failure mode with $\mathrm{RPN}=98$ is classed as 'consider corrective action'.

The general principle governing the multiplication of risk factors to obtain RPNs and prioritization of failure modes has been largely criticized [12]. For example, the three risk factors S, O and D are assumed to have the same importance; or various combinations of $\mathrm{S}, \mathrm{O}$ and D may produce an identical RPN value, whereas the risk implication may be totally different and may result in high-risk events going unnoticed; etc. Extensive work has been done in the recent years to improve the FMEA process (see, e.g., references [13-15]). According to a detailed literature review performed by [16], Artificial Intelligence (AI), fuzzy rule-based systems, Grey theory, and Multi-Criteria Decision Analysis (MCDA) models such as Analytic Hierarchy Process (AHP) and Analytic Network Process (ANP) are the most prominent methods used for overcoming the FMEA limitations. Furthermore, the cost-based FMEA models pioneered by Gilchrist [17] have also gained popularity.

# 2.3. FTA and FMEA 

Recently, applying both the FTA and FMEA techniques either simultaneously or in succession has been proven to be complementary, effective and increasingly popular. Employed systematically, an integrated FTA-FMEA technique can provide a thorough evaluation of system safety concerns [18]. FTA yields a comprehensive breakdown of faults leading to the undesired top event, whilst FMEA furnishes the exact fashion in which these faults exists and their direct effects on the top event, making the combination appropriate for safety and reliability analyses.

The backward integration of both tools seemingly provides stronger advantages, though many researchers argue advantages depend on the specific application [9]. Khaiyum and Kumaraswamy [19] carried out FTA in parallel and FMEA sequentially, to analyze and diagnose the different causes of failures in a gas leak detection system. Limitations of the individual techniques were however not explored. Bluvband et al. [20] in a unified bouncing approach considered multiple point failures through interaction matrices, a major enhancement to the traditional FMEA. The interaction between the techniques grows in complexity, requiring in-depth knowledge of the tools and particularly of the system under study.

Employing the combination of FTA and FEMA for identifying critical components and reliability analysis of highly complex systems has received little attention. Zhai et al. [21] combined three methods of critical component identification, namely reliability prediction, FMEA and FTA in a reliability tolerance design program for light-emitting diode (LED). Liu et al. [5] used the combination of FTA and FMEA techniques to identify critical components in the manufacturing processes of a photovoltaic power station in the bi-directional fashion, revising minimal cut sets and continually refining them. Though software usage is incorporated, the process remains long and complex. As clearly seen, these methodologies are not without limitations. Therefore, there still exists a crucial need to manage different criteria of risk analysis techniques in a combinatorial framework to efficiently furnish and complement each other, and be pertinent to specific safety and reliability requirements. In order to tap maximum benefits of an FTA-FMEA integration, minimal cut set theory will be used in this study.

Weights ( $w$ ) are assigned to RPN values in the FMEA technique to incorporate the importance of each component in the system. Therefore, the weighted RNP value is calculated by Equation (2), that is,

$$
\mathrm{WRPN}=w \times \mathrm{S} \times \mathrm{O} \times \mathrm{D}
$$

where as shown, $w$ is factored into traditional RPN values to prioritize failure modes and thereafter critical components. These weights are vital as they are representative of the importance of minimal cut sets and hence all components are represented by the latter. The FTA methodology is selected for this purpose, as it readily provides and ranks minimal cut sets in terms of importance to system performance. Subsequent breakdown of minimal cut sets allows all components to be analyzed in FMEA worksheets. Simplicity and ease of use are introduced through underlying theory that links both techniques and the complex system under consideration, and is streamlined to component level. The criticality of components is then calculated, not based on RPN but on the weighted RPN. The details of the methodology are presented in the next Section.

# 3. Proposed Methodology 

To integrate both the FTA and FMEA techniques for the purposes of identifying, evaluating and prioritizing failure modes, a methodology is proposed based on the minimal cut sets theory and Birnbaum's measure of importance. In the backward integration framework, as shown in Figure 1, components of the complex system under consideration are de-coupled by means of the FTA technique. The undesired top event is identified based on the reliability requirements of the complex system and initial itemization of components emanates from the fault trees. Results provide information to subsequently adjust the FMEA criteria. With root nodes in the fault tree forming the base for system function in the failure mode table, probability, severity and detectability measures are modified based on the set reliability goal. The steps of the proposed methodology are explained below:
![img-0.jpeg](img-0.jpeg)

Figure 1. FTA-FMEA integration framework.

# 3.1. Reliability Goal and System Boundary Definition 

As a preliminary step in reliability assessment, particularly for complex systems, establishing generic reliability requirements of the system under consideration acts as a reference for further verification and validation. More so, the scope and element boundaries of the system require elucidation as complexity by definition may depict considerably large systems, interacting with several other elements.

### 3.2. System Breakdown

As stated by Kolowrocki [1], it is nearly impossible to model a complex system using the traditional reliability analysis methods. The logical approach for this purpose is to subdivide the system into smaller units and employ probabilistic techniques to calculate overall reliability, based on reliability of the subsystems. Once the scope and boundaries are defined, clarity on further categorization of the system under consideration is facilitated, particularly for any expert or analyst with considerable knowledge.

### 3.3. FTA Steps

This phase includes slight modifications to the traditional FTA steps. The top event is defined and all immediate causes are identified. Again, secondary level events are specified and all root causes down to basic level are identified. The fault tree diagram is built and different fault combinations leading to top event are presented. At this stage, several fault trees may become necessary, dependent on the complexity of the system under consideration. For this reason, utilization of software applications for building and analyzing fault trees can facilitate the process. Finally, minimal cut sets are obtained and their importance weights are evaluated. Assuming $w$ is an independent function variable representing the importance of $i$ th minimal cut set in the fault tree structure, we have:

$$
w_{i}=F\left(X_{i}\right), i=1,2
$$

where $X_{i}$ represents the importance of the $i$ th minimal cut set and $F\left(X_{i}\right)$ is a function with independent variable $X_{i}$. By substituting Equation (3) in Equation (2), we have:

$$
\mathrm{WRPN}_{i}=F\left(X_{i}\right) \times \mathrm{S}_{\mathrm{i}} \times \mathrm{O}_{\mathrm{i}} \times \mathrm{D}_{\mathrm{i}}, \cdots i=1,2
$$

Quantitative perspectives on dominant contributors to the top event can be provided by calculating the importance measure of the components in the system. Several methods such as Fussell-Vesely, Birnbaum, etc. have been developed in the literature for this purpose [22]. Though Fussell-Vesely is the most commonly used approach, it does not necessarily identify all minimal cut sets in a complex system. Birnbaum's measure is hence selected and used in this study as modification and versatility based on system application is possible. Hence, the importance of the $i$ th minimal cut set is given by:

$$
\mathrm{X}_{i}=\delta \mathrm{hp} / \delta \mathrm{p}_{i}=h\left(1_{i}, \mathrm{p}^{(i)}\right)-h\left(0_{\mathrm{i}}, \mathrm{p}^{(i)}\right)
$$

where $h\left(1_{i}, \mathrm{p}^{(i)}\right)$ presents the probability that the system fails when component $i$ fails and $h\left(0_{i}, \mathrm{p}^{(i)}\right)$ presents the probability that the system fails when component $i$ is working. $w_{i}$ is a value between zero and one, i.e., $w_{i} \in[0,1]$, and thus it will have little impact on RPN values which are integer numbers between 1 and 1000. Based on the assessment catalogue proposed by Pickard et al. [23], Table 1 is created to magnify individual importance indices and map them to corresponding domain functions $F\left(X_{i}\right)$.

Table 1. Ranking criteria for the weights.


# 3.4. FMEA Steps 

Aside from typical FMEA steps that are detailed and explained in reference [11], the additional tasks that should be implemented at this stage include revising traditional RPN values and ranking components based on the weighted RPNs. Experts brainstorm and report the results as in the traditional FMEA process. In this case, the minimal cut sets that were obtained from the fault trees aid the failure mode identification process. The weights are multiplied with RPNs obtained from the traditional FMEA procedure. It must be noted that minimal cut sets may include one or more components which should be assigned relative importance, as multiple failures are not considered. Components with highest RPNs may not necessarily possess highest WRPNs in this methodology, hence added criteria for ranking. An integrated FTA-FMEA worksheet carrying all necessary data from the traditional FTA and FMEA approaches is shown in Table 2, ending with suggested preventive actions.

Table 2. An integrated FTA-FMEA worksheet.


The traditional approaches of both FTA and FMEA techniques are revisited though all relevant software advances. This is to provide the basis for criteria amelioration at every stage. Certain assumptions are considered with this methodology:

- Failure modes in FMEA are a direct result of the faults identified in the FTA process and the failure causes are assumed to be mutually independent.
- In the FMEA method, only the most critical failure modes are considered. Double or multiple failure modes inclusion, though representing a major improvement to traditional FMEA, would be important only when the assessment's aim is beyond the scope of this work such as risk identification and further quantitative analysis.
- The complex system under consideration should be coherent and modular with each module relevant to system functioning, with the FTA possessing only $A N D$ and $O R$ gates.

In the next section, a case study is presented to illustrate the application of the proposed model in an industrial context.

## 4. Case Study

Blowout Preventers (BOPs) are considered the last line of defense in any drilling or workover oil and gas operations. In an array of stacked valves (see Figure 2), where one or more lower level non-critical components can result in a common undesired event, FTA is a suitable tool as it identifies

minimal cut sets and minimal path sets of common-cause failure (CCF). This is particularly important for BOP systems, as in an assembly with parallel connections, wherein CCF is a major characteristic [24]. FTA has been so far employed in several BOP reliability analyses (see, e.g., references [25,26,27,28]), proving to be convenient for identifying failure modes within the BOP stack. Fowler and Roche [29] used both FTA and FMEA for reliability analysis of the device and its hydraulic control system. They employed the inductive bottom-up approach to determine consequences of part malfunction and to link undesired events to their causes, the deductive supplement. FMEA was again extended to include criticality and applied to the entire system in a study conducted by American Bureau of Shipping (ABS) and ABSG Consulting Inc. for the Bureau of Safety and Environmental Enforcement (BSEE) [30]. A BOP reliability analysis model was recently developed by employing the software package Norsys Netica (https://www.norsys.com/netica.html) to aid in identification, evaluation, and prioritization of failure risks [31].
![img-1.jpeg](img-1.jpeg)

Figure 2. Typical BOP stack and components.
For complex systems such as BOP in which interdependencies between sub-components are complicated, combined (hybrid) techniques are worthwhile. Identifying critical components in a system with over seven (7) main subsystems, housing about 600 individual components may be the starting point for more detailed qualitative and quantitative analyses. The proposed integration methodology is explained step by step as follows:

1. Reliability goal and system boundary definition

- Identification of critical components within the system: As a large specialized and mechanical valve assembly that is used to seal wells against kicks or blowouts during drilling or work-over operations, a critical component will be the one whose failure will lead to the failure of the entire system or a major part of it.
- Setting overall reliability requirements for the system: Safety Integrity Level (SIL) requirements are widely accepted for the basis of operation and design of Safety Instrumented Systems. For BOP systems, the IEC 61508 requirements for the safety integrated functions are applied [32].
- Defining system specifications: The BOP system considered in this study is a type of class VI configuration with 4 rams and dual annular. Main subsystems (from the upper annular

preventer to the wellhead connector) make up components under investigation, ignoring surface controls, panels and accumulators as shown in Figure 2.
2. System Breakdown Physical and functional categorization of components is achieved as part of the requirements for FTA and FMEA. Major components of the BOP as identified in the literature include: control system (pods, accumulators, auto-shear system), ram preventers (pipe, blind-shear and/or casing-shear preventers), annular preventers (lower and upper), connectors (wellhead and Lower Marine Riser Package (LMRP)) and kill/choke system (valves and lines).
3. FTA Steps The undesired top event for a BOP is a blowout once a kick cannot be killed. This forms the apex, upon which the fault tree is built and shown in Figure 3, alongside the immediate top-level basic events. Analyses at this stage were aided by a professional software called FaultTree ${ }^{+ \mathrm{TM}}$ [33], requiring overall structural and functional knowledge about the system. All cut sets were determined and the weights were calculated by Equations (4) and (5). The minimal cut sets and gate summary of the BOP's fault tree are extensive and not thoroughly presented here. Table 3 gives the results obtained for some components and presents the cut sets with associated rankings calculated from Table 1, to demonstrate applicability.
4. FMEA Steps An FMEA standard procedure is followed at this stage. In this case, however, a detailed FMEA study is conducted on BOP system using the severity, occurrence and detectability ratings reported in reference [34]. The methodology used ten-point scales for severity rating (see Table 4), occurrence rating (see Table 5), and detectability rating (see Table 6) to represent the risk priorities of the BOP failures.
![img-2.jpeg](img-2.jpeg)

Figure 3. Top level of fault tree.
Table 3. Weights and rankings of some BOP components.


Table 4. Severity ratings of a failure for BOP.


Table 5. Occurrence ratings of a failure for BOP.


Table 6. Detectability ratings of a failure for BOP.


Weighted RPNs are then calculated by multiplying the traditional RPN values with the weight factor, resulting in weighted RPN values to become between 1 and 10,000. Comparatively, components requiring greater corrective action and implicitly considered to be critical based on the traditional FMEA approach differ from those obtained by the proposed FTA-FMEA technique. Table 7 demonstrates this for a cross section of components and reveals that control pods may require more attention after blind shear rams as opposed to pipe rams in the traditional FMEA ranking system.

Table 7. A comparison between the results obtained from the traditional FMEA technique with those obtained by the proposed method.


Figure 4 provides a clear comparison between the traditional RPN values and the weighted RPN values.

Though some components such as the kill valves still remain at top priority in RPN rankings with the proposed technique, a clear disparity in rankings and hence in the criticality of components is depicted in others such as the connectors (wellhead and LMRP). Choke valves are ranked at the same level with casing shear rams and are higher than blind shear rams and accumulators.

Comprehensive analyses of the system produce results that may significantly alter corrective measures and criticality priorities for the BOP and any complex system in general. Whilst FMEA focuses on causal effects, taking into consideration all possible failures but not necessarily component interdependencies, FTA considers the latter but avoids minute components and their effects on overall system failure. The integration of the techniques is proven to produce more robust prioritization of system risks as greater failure severity may not necessarily mean greater criticality. This phenomenon becomes explicit when weighted RPNs for BOP under two different operating conditions, namely deep-water and shallow-water, are compared. Six experts are consulted to provide their opinion on the severity, occurrence and detectability of various failure modes, and a Multi-Criteria Decision Analysis (MCDA) method based on Weighted Sum Model (WSM) is used to aggregate the experts' opinions (see Tables $8-10$ ). Though FMEA requires the experts to brainstorm on every aspect of FMEA process, ambiguity is avoided by disseminating similar FMEA worksheets to experts, containing the specific components/subsystems as previously established and their single associated undesired failure mode. Judgement is elicited mainly on the severity, occurrence and detectability ratings of failure modes.
![img-3.jpeg](img-3.jpeg)

Figure 4. RPN values obtained from the traditional FMEA technique ( $\#$ ) versus weighted RPN values obtained by the propose method ( $\#$ ).

Table 8. Weighting criteria for the group of experts.


Table 9. Expert weighting.


Table 10. Final aggregation for RPNs (example of the blind shear ram component).


As expected, RPN values for all BOP components in deep waters are larger than those in shallow waters, however, significant differences exist between ranking priorities in deep and shallow waters, as shown in Figure 5. The robustness of the technique is proven as components such as the wellhead connector and casing shear ram gain significant priority leaps in deep water, in compliance with research and regulatory standards. ![img-4.jpeg](img-4.jpeg)

Figure 5. Weighted RPN values for shallow-water ( $\square$ ) and deep-water ( $\square$ ) cases.

# 5. Conclusions

This paper presented an integrated methodology of fault tree analysis (FTA) and failure mode and effects analysis (FMEA) in a manner that provides a modified, systematic and structured approach for identifying, evaluating and prioritizing the risks associated with different components in a complex system. The synergy of complementary techniques is harnessed by modifying criteria, hence increasing efficiency in analysis. By using the proposed technique, it is possible to gain insights about any complex system which otherwise might be overlooked. The basis for corrective action is improved in

a computationally sound manner. The application of the proposed methodology was demonstrated with a critical subsea oil and gas system known as Blowout Preventer (BOP).

The results of the study proved the benefits of the proposed FTA-FMEA methodology and combinatorial risk analysis techniques in general. Components that may be overlooked based on the traditional FMEA technique were brought to the limelight for consideration. More so, the priority rankings were improved significantly. Minute changes in ranking order may have huge implications, particularly for a safety-critical system such as BOP. Aside being essential for further quantitative research, component priority can significantly alter maintenance and testing policies. As shown in Table 7 and Figure 4, some components such as the kill valves remained at top priority in RPN rankings with the proposed technique. However, a clear disparity in rankings was observed for some components such as the connectors (wellhead and LMRP). Choke valves were ranked at the same level with casing shear rams and were higher than blind shear rams and accumulators.

Future research can be directed towards the effects of double and multiple failures, the comparative difference obtained when different importance measures are used, and linking the software interphases of the proposed integration scheme. Also, the normed design of subsea accumulators for actuation and control of BOPs may sometimes not be safe (see reference [35]). Thus, consideration of the actuation of the BOP and its design in reliability analysis can be an interesting subject for research.

Author Contributions: E.E. performed the analysis and wrote the initial manuscript draft. M.S. reviewed the initial manuscript, made contributions to its structure and responded the reviewers' comments. Both M.S. and A.K. supervised the work.

Funding: This work was supported by Commonwealth Scholarship Commission.
Conflicts of Interest: The authors declare no conflict of interest. This research received no external funding.

# Acronyms 

