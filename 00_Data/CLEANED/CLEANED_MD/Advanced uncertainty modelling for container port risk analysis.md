# LJMU Research Online 

Alyami, H, Yang, Z, Riahi, R, Bonsall, S and Wang, J
Advanced uncertainty modelling for container port risk analysis.
http://researchonline.ljmu.ac.uk/id/eprint/4601/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Alyami, H, Yang, Z, Riahi, R, Bonsall, S and Wang, J (2016) Advanced uncertainty modelling for container port risk analysis. Accident Analysis and Prevention, 123. pp. 411-421. ISSN 0001-4575

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Advanced uncertainty modelling for container port risk analysis 

Hani AIYAMI ${ }^{a}$, Zaili YANG ${ }^{a 1}$, Ramin RIAHI ${ }^{a}$, Stephen BONSALL ${ }^{a}$ and Jin WANG ${ }^{a}$ ${ }^{a}$ Liverpool Logistics Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, Liverpool, UK.


#### Abstract

Globalization has led to a rapid increase of container movements in seaports. Risks in seaports need to be appropriately addressed to ensure economic wealth, operational efficiency, and personnel safety. As a result, the safety performance of a Container Terminal Operational System (CTOS) plays a growing role in improving the efficiency of international trade. This paper proposes a novel method to facilitate the application of Failure Mode and Effects Analysis (FMEA) in assessing the safety performance of CTOS. The new approach is developed through incorporating a Fuzzy Rule-Based Bayesian Network (FRBN) with Evidential Reasoning (ER) in a complementary manner. The former provides a realistic and flexible method to describe input failure information for risk estimates of individual hazardous events (HEs) at the bottom level of a risk analysis hierarchy. The latter is used to aggregate HEs safety estimates collectively, allowing dynamic risk-based decision support in CTOS from a systematic perspective. The novel feature of the proposed method, compared to those in traditional port risk analysis lies in a dynamic model capable of dealing with continually changing operational conditions in ports. More importantly, a new sensitivity analysis method is developed and carried out to rank the HEs by taking into account their specific risk estimations (locally) and their Risk Influence (RI) to a port's safety system (globally). Due to its generality, the new approach can be tailored for a wide range of applications in different safety and reliability engineering and management systems, particularly when real time risk ranking is required to measure, predict, and improve the associated system safety performance.


Key words: FMEA, Port safety, Maritime risk, Maritime safety, Maritime Transport, Sensitivity analysis

## 1 Introduction

Maritime infrastructure such as container terminals presents safety critical and costly engineering systems that enable economic activities through the transfer of goods and

[^0]
[^0]:    ${ }^{1}$ Corresponding Author's Address: Zaili Yang, Liverpool Logistics Offshore and Marine Research Institute, Liverpool John Mores University, Liverpool, UK. Email: z.yang@ljmu.ac.uk

services between national and international destinations. Given their significance in ensuring prosperity of the world economy, container terminals face a variety of operational and environmental uncertainties that make them vulnerable to hazards (Mansouri et al., 2009). The seaports with safe and reliable operations are of great significance for the protection of human life and health, the environment, and the economy. Any inappropriate operation could lead to a profound negative impact on service quality, productivity cost, and lifestyle. Therefore, system safety evaluation including the early detection of hazards is critical in avoiding performance degradation and damage to human life or machinery. Furthermore, the effect of accidents and/or disasters that jeopardise terminal operations can be reduced/eliminated, if a robust risk forecasting mechanism is developed and effectively enforced. In practice, engineering systems are at large repairable and their safety measures change with time and by considering these changes as a time series process, the growth or deterioration of such systems can be evaluated and improved (Hu et al., 2010). The necessity and importance of evaluating the system safety lies in that decision makers are generally interested in estimating future occurrence of system failures for resource planning, inventory management, development of realistic policies for age replacement and logistics support.

The international Maritime Organization (IMO) has an aim of enhancing maritime operation safety, including protection of life, health, marine environment, and property. As a result, the Formal Safety Assessment (FSA) has been approved in 2002 and since then, used as a rational and systematic process for assessing the risks associated with shipping activities and for evaluating the associated costs and benefits. Furthermore, the World Economic Forum (2014) has also emphasized the need towards a structured evaluation of risks on critical maritime systems in order to ensure the safety, security, and resilience of their operations. A robust risk management system can not only monitor the performance of system safe and reliability performance, but also offer valuable information for the decision makers to take the correction actions in order to improve the quality and reduce the cost of their systems (Hu et al., 2010).

Most of the current modelling schemes in Failure Mode and Effects Analysis (FMEA) were developed using linear or nonlinear multiple regression which is comparatively reliable. However, in many circumstances they may not perform well in terms of accuracy or speed, and suffer from a number of drawbacks such as lack of suitable models, exceptional assumption used in analysis due to the lack of applicable safety related data/records and a high level of uncertainty involved in the available failure data (Sii et al.,

2001). The incapability of traditional FMEA in addressing uncertainty in data in particular contexts has stimulated the development of new methods based on uncertainty treatment theories such as fuzzy logic, evidential reasoning (ER), grey theory, Monte Carlo simulation, Bayesian network (BN), Markov model, and artificial neural network (Yang et al., 2008). Safety evaluation and risk analysis involving Multiple Attribute DecisionMaking Analysis (MADM) have also been developed by a large community of researchers.

Many decision problems in engineering and management systems involve multiple attributes of both a quantitative and qualitative nature with uncertain or missing information that causes complexity in multiple attribute assessment (Yang and Xu, 2002a). Researchers have paid increasing attention to the use of MADM models in a wide variety of practical applications relating to choice assessment, evaluation and selection. Examples of such applications include urban and community planning; resource allocation; supplier evaluation; employee/organization evaluation; marketing strategies; credit analysis; and engineering design evaluations including safety management (Eom, 1989; Eom and Lee, 1990; Eom et al., 1998). More specifically, MADM has been applied in functional assessment for disability index and the ergonomics consultation (Jen and Min, 1994), the restoration planning for power distribution systems (Chen, 2005), evaluation of the suitability of manufacturing technology (Chuu, 2009), expert's systems (Beynon et al., 2001), and motorcycle evaluation (Yang and Xu, 2002b). In recent years, different risk analysis models involving MADM have been proposed to evaluate and predict system safety and reliability. Examples of such models include, a marine system safety assessments approach (Wang et al., 1995; 1996), a belief function model (Srivastava and Liu, 2003), a model for strategic research and development project assessments (Liu et al., 2008) and a nonlinear programming model (Zhou et al., 2010). Thus, MADM has been increasingly used in safety management and risk analysis.

This paper aims to develop a novel method to facilitate the application of the FMEA approach in port safety analysis through incorporating MADM approaches (i.e. ER with FRBN) to prioritise each HE's safety level individually in a container terminal and then to aggregate them collectively to evaluate the safety performance of CTOS as an entity and quantify the HE's safety impact to the system accordingly. The True Risk Influence (TRI) for each HE is assessed taking into account their specific local risk estimations and their RI to a port's safety system is then prioritised accordingly to facilitate the subjective safety based decision-making modelling for container terminal safety. The novelty of this paper, compared to the relevant studies in the literature, primarily lies in that a) it for the very

first time incorporates risk impact of components to the whole system into risk quantification of ports; b) it combines various uncertainty models, such as fuzzy Bayesian for HEs' risk estimate and ER for risk synthesis from components to system levels, in a systemic way and c) it newly uses a "max and min" DoB (degree of belief) allocation approach to measure the risk reduction of a port system due to the best and worst safety performance of the investigated HE so as to test the sensitivity of the model and to prioritise hazards from both their own risk as well as their impacts on the system safety. From a theoretical perspective, the proposed hybrid method can be tailored for risk prioritisation of any large engineering system of similar features (i.e. a hierarchical risk structure).

To achieve the aim, this paper is organized as follows. A brief review of applying FRBN and ER in FMEA particularly concerning their applications in port risk analysis is carried out in Section 2. Section 3 describes the novel modified FMEA framework capable of integrating different weights of risk parameters into ER and the aggregation process. A real case study regarding CTOS safety performance evaluation is investigated to demonstrate the feasibility of the new methodology in Section 4. Section 5 concludes the paper. Consequently, this study contributes to facilitating FMEA applications for enhancing container terminals risk management in a situation where uncertainty in historical failure data is high and traditional probabilistic risk analysis methods relying on complete data are not applicable.

# 2 Literature review 

Safe operation of any modern technological system is a fundamental attribute to ensure its reliability. This research focuses on assessing the operational safety of container terminals through evaluating the probability of the system's failure. Since the safety of container terminals is affected by multiple factors such as their capacity, workforce, machinery, management, and geographical location, task, conducting an effective risk management system is challenging and rational decision analysis is essential to properly represent and use uncertain information in the aforementioned factors to enhance container terminal safe operations.

Seaports risk management is playing an increasingly important role in ensuring port service resilience in the context of supply chain systems. As a result, it is attracting much attention from different operational, organizational and economic perspectives (Legato

and Monaco, 2004; Garrick et al., 2004; Fabiano et al. 2010; Mokhtari et al., 2011; Madni and Jackson, 2009). However, compared to shipping risk analysis (Hanninen, 2014; Banda et al., 2015; Wu et al., 2015 ), studies on seaport risk and safety management are scarce in the literature. Pallis et al. (2010) indicated, reviewing 395 port related journal papers published between 1997 and 2008, that risk analysis persistently occupied a backseat role within port research being overwhelmed by other aspects involving efficiency analysis, port competition, geographical analysis and spatial evolution, port policy and governance (Yang et al., 2014).

FMEA is one of the most widely applied hazard identification and risk analysis methods due to its visibility and easiness (Braglia et al., 2003). The method has incorporated advanced uncertainty modelling techniques such as fuzzy sets, grey theory, BN and ER to facilitate its practical applications in maritime and offshore engineering safety (Sii et al., 2001), system reliability and failure mode analysis (Braglia et al., 2003), engineering system safety (Liu et al., 2005) and maritime port security (Yang et al., 2009).

The traditional FMEA method has three fundamental attributes (namely failure occurrence likelihood (L), consequence severity (C), and probability of failures being undetected (P)) that are employed to assess the safety level of a failure (Wang et al., 1996). Among the quantitative development of FMEA, a FRBN approach using Bayesian Network mechanism to conduct fuzzy rule based (FRB) risk inference in order to achieve sensitive failure priority values based on domain expert knowledge, has been proposed and applied by Yang et al., (2008) and Alyami et al. (2014).

In Alyami et al., (2014), a risk-based decision tool for effective seaport HEs risk evaluation was developed. The development was to use the rational distribution structure on Degree of Belief (DoB) to model the rule base between the four risk parameters and risk evaluation of the identified HEs in a container port operational system.

The following steps were required for developing a FMEA criticality in safety evaluation of container terminals (Alyami et al., 2014):

1. Establish a FRB with a belief structure in FMEA.
2. Identify HEs (failure modes) in container terminals.
3. Prioritise the HEs with rational distribution of DoBs in FRB.
4. Validation by using sensitivity analysis techniques.

In this study, the risk analysis was only constrained for HEs that are located at the bottom level of a hierarchy of port safety system. It has not well addressed the risk and safety analysis from a systematic perspective, revealing a significant research gap to fulfil.

ER shows a potential in synthesising evaluations in a hierarchy. A careful literature review has disclosed that there are many ER applications in risk areas, among which several leading publications incorporating FMEA and ER methods include Wang et al., (1995; 1996), Yang and Sen, (1996), Yang, (2001), Yang et al., (2010), and Yang et al., (2009). Some other typical studies have made a useful contribution towards the applications of ER for representing and managing uncertainty (Yen, 1990; Dekorvin and Shipley, 1993; Sönmez et al., 2001; Yang et al., 2004; Zhang et al., 2005; XU et al., 2006a; XU et al., 2006b and Riahi et al., 2012). ER, developed particularly for MADM problems with both qualitative and quantitative criteria under uncertainty, utilises an individual's knowledge, expertise, and experience in the forms of belief functions (Riahi, 2010). Therefore, it, together with other uncertainty modelling methods such as BNs and/or fuzzy logic, has shown superiority in tackling the diversity and uncertainty of the subjective information in general and effectively handling linguistic evaluations for risk analysis in particular.

Chin et al. (2009) used a group-based ER approach to develop a risk priority model that included the assessment of risk factors using belief structures. Thereafter, the overall belief structures were converted into expected risk scores and then ranked them using a minimax approach in which ER was used to model the diversity and uncertainty of the assessment information. Deng et al. (2011) introduced a fuzzy evidential reasoning-based approach for risk analysis. The proposed method could efficiently deal with linguistic evaluations of experts and uncertain data or information. The similarity measures between linguistic evaluation and a predefined fuzzy scale were used to derive basic probability assignments. The system risk score was obtained using the Dempster rule of combination based on the risk values calculated for each component of the system. Hu, et al. (2010) proposed a reliability prediction model based on the ER to forecast reliability in turbocharger engine systems. The proposed method allowed the identification of the appropriate internal representation between basic attributes associated with the system prediction outputs to define the relationships between past historical data and the corresponding targets, and then future output values can be predicted if new inputs became available.

In respect to the above literature review, the major benefits of using the ER approach are listed as follows (Yang and Xu, 2002a; Riahi, 2010):

- It is capable of handling incompleteness, uncertainty, and vagueness in data as well as complete and precise data in MADM problems.
- It has the ability to provide users with flexibility by allowing them to express their judgements both subjectively and quantitatively.
- It is capable of accommodating or representing the uncertainty and risk inherent in decision analysis for multiple factor analysis.
- It has the ability to offer a rational methodology to aggregate the data assessed based on its hierarchical evaluation process.

The ER approach in this paper is used for aggregating risk estimations of all the HEs based on a DoB decision matrix and the evidence combination rule of D-S theory. It uses a distributed modelling framework, in which the risk estimation of each HE is accessed using a set of collectively exhaustive and mutually exclusive assessment grades obtained from a FRBN method (Alyami et al., 2014).

The proposed methodology for modelling CTOS using the integrated FRBN and ER approaches can not only model the diversity and uncertainty of the assessment information in complex FMEA, but also incorporate the relative safety importance of HEs into the determination of risk priority values in a precise and logic way by conducting the sensitivity analysis. More importantly, by incorporating ER with the FRBN analysis, the risk level of each HE can be investigated from both local (i.e. its own risk level) and global (i.e. its risk influence to the system safety) perspectives.

# 3 Methodology for modelling container terminal operational systems 

The first part of evaluating the safety performance of CTOS is to prioritize HEs individually in a container terminal using an FRBN approach. It provides a realistic and flexible way of describing input failure information with easy update of Risk Estimation (RE) and facilitates risk evaluation of HEs individually. The second part is to aggregate the HEs' REs collectively by using the ER approach and then quantify the HEs for riskbased decision support of CTOS as an entity (i.e. as a system). More importantly, a new sensitivity analysis method is developed to analyse the importance of each HE in terms of its contribution to the safety of the whole port operational system. Having carefully analysed the RE of each HE locally in port system safety using FRBN in Alyami et al.,

2014, this work focuses more on the application of ER for risk aggregation and sensitivity analysis for evaluating the risk contribution of each HE globally.

# 3.1 Risk assessment for collective HEs using ER approach 

The steps for incorporating ER in FMEA in this study are described in a stepwise manner as follows:
I. Develop a hierarchical structure to describe the CTOS safety performance.
II. Use the ER algorithm to synthesise the risk result of each HE for the safety estimate of the whole system.
III. Evaluate the risk impact of each HE on the system by using sensitivity analysis.

## I. Develop the hierarchical structure

The HEs investigated in this study are those identified through the combination of surveys, field investigation, and literature search. In Alyami et al., 2014, 24 HEs at the bottom level were identified, while in this paper, the hierarchy showing their positions and relations is the focus. It is presented in Figure 1. The HEs identified in the hierarchical structure are those associated with container terminal operations including cargo handling equipment and transport facilities while other risk aspects such as managerial, policy implications, environmental and political issues are to be addressed in future work. During the investigation, it was found that the risk attributes used to evaluate environmental HEs such as sea level rise, flooding, and storm surge are different with those relating to operations. For instance, a key risk attribute used to estimate environmental HEs is timeframe, which is less relevant in this study. It is noteworthy that the main contribution of this research is to apply the FRBN model for safety estimation of a container operational system and the risk impact analysis of each HE on the whole system.

![img-0.jpeg](img-0.jpeg)

Figure 1. Hierarchy for the risk factors during terminal operations
(Authors)

# II. System safety estimate by synthesising the risk result of all HEs using ER method 

The REs of all the HEs can be presented in both linguistic variables with DoB and numerical values based on utility values, as the output of applying the FRBN model in Alyami et al., (2014). The result expressed by linguistics variables will be used as the input values in ER for calculating the RE of CTOS.

The ER scheme adapted and applied in this study was first generated from Dempster (1967) that was subsequently developed by Shafer (1976) to form Dempster-Shafer (D-S) theory. The combination of D-S theory and fuzzy rule bases is an appropriate way to solve MADM problems that include fuzzy information from multiple sources. One direction is to extend D-S theory to include the feature of fuzzy set theory so that its capability can be enhanced to process both crisp and fuzzy information.

In D-S's rule of combination, suppose subsets B and C defined on a common space $\theta$ are associated with confidence estimates $m_{1}$ and $m_{2}$ respectively that were obtained from two independent sources. The orthogonal sum of $m_{1}$ and $m_{2}$ is defined as follows:

$$
\left(m_{1} \oplus m_{2}\right)(A)=\frac{\sum_{B \cap C=A} m_{1}(B) \times m_{2}(C)}{1-\sum_{B \cap C=\emptyset} m_{1}(B) \times\left(m_{2}\right)(C)}
$$

The ER algorithm based on the D-S theory has been developed, improved, and modified towards a more rational way by a large community of researchers in continuously researching and practicing processes (Yang and Xu, 2002b).

The algorithm can be analysed and explained as follows. Let two subsets " $S_{1}$ " and " $S_{2}$ " present the REs (based on the three safety expressions "High", "Medium" and "Low") of HE1 and HE2 and S be the synthesised RE of the two subsets. Then" $S$ ", " $S_{1}$ " and " $S_{2}$ " can separately be expressed by:

$$
\begin{aligned}
& S=\left[\left(\text { DoB }_{s}, \text { Low }\right),\left(\text { DoB }_{s}, \text { Medium }\right),\left(\text { DoB }_{s}, \text { High }\right)\right] \\
& S_{1}=\left[\left(\text { DoB }_{s_{1}}, \text { Low }\right),\left(\text { DoB }_{s_{1}}, \text { Medium }\right),\left(\text { DoB }_{s_{1}}, \text { High }\right)\right] \\
& S_{2}=\left[\left(\text { DoB }_{s_{2}}, \text { Low }\right),\left(\text { DoB }_{s_{2}}, \text { Medium }\right),\left(\text { DoB }_{s_{2}}, \text { High }\right)\right]
\end{aligned}
$$

where "Low ", " Medium ", " High " are assessed with their corresponding DoB.

Suppose the normalised relative weights of subsets 1 and 2 in the safety evaluation process are given as $w_{1}$ and $w_{2}$ where $\left(w_{1}+w_{2}=1\right)$. Alyami et al., (2014) considered the equally important weight assigned to all HEs identified at the same level in the hierarchy (i.e. Figure 1).

Suppose $M_{1}^{m}$ and $M_{2}^{m}(m=1,2 \ldots 3)$ are individual degrees to which the subsets " $S_{1}$ " and " $S_{2}$ "support the hypothesis that the safety evaluation is confirmed to the three safety expressions. Then, $M_{1}^{m}$ and $M_{2}^{m}$ can be obtained as follows (Riahi et al., 2012):

$$
\begin{array}{ll}
M_{1}^{m}=w_{1} \beta_{1}^{m} & \\
M_{2}^{m}=w_{2} \beta_{2}^{m}
\end{array}
$$

where $(m=1,2, \ldots 3)$. Therefore,

$$
\begin{array}{ll}
M_{1}^{1}=w_{1} \beta_{1}^{1} & M_{2}^{1}=w_{2} \beta_{2}^{1} \\
M_{1}^{2}=w_{1} \beta_{1}^{2} & M_{2}^{2}=w_{2} \beta_{2}^{2} \\
M_{1}^{3}=w_{1} \beta_{1}^{3} & M_{2}^{3}=w_{2} \beta_{2}^{3}
\end{array}
$$

Suppose $H_{1}$ and $H_{2}$ are the individual remaining belief values unassigned for $M_{1}^{m}$ and $M_{2}^{m}(m=1,2, \ldots 3)$. Then, $H_{1}$ and $H_{2}$ can be expressed as follows (Yang and Xu, 2002; Riahi et al., 2012)

$$
\begin{aligned}
& H_{1}=\bar{H}_{1}+\bar{H}_{1} \\
& H_{2}=\bar{H}_{2}+\bar{H}_{2}
\end{aligned}
$$

where $\overline{H_{n}}(n=1$ or 2$)$ representing the degree to which the other subset can play a role in the assessment and $\overline{H_{n}}(n=1$ or 2$)$ caused by the possible incompleteness in the subsets " $S_{1}$ "and " $S_{2}$ ", can be described as follows respectively (Riahi et al., 2012).

$$
\begin{aligned}
& \bar{H}_{1}=1-w_{1}=w_{2} \\
& \bar{H}_{2}=1-w_{2}=w_{1} \\
& \bar{H}_{1}=w_{1}\left(1-\sum_{m=1}^{3} \beta_{1}^{m}\right)=w_{1}\left[1-\left(\beta_{1}^{1}+\beta_{1}^{2}+\beta_{1}^{3}\right)\right] \\
& \bar{H}_{2}=w_{2}\left(1-\sum_{m=1}^{3} \beta_{2}^{m}\right)=w_{2}\left[1-\left(\beta_{2}^{1}+\beta_{2}^{2}+\beta_{2}^{3}\right)\right]
\end{aligned}
$$

Suppose $\beta^{m^{\prime}}(m=1,2 \ldots 3)$ represents the non-normalised degree to which the safety evaluation is confirmed to the three safety expressions as a result of the synthesis of the judgments produced by subsets 1 and 2. Suppose $H_{U^{\prime}}$ represents the non-normalised remaining belief unassigned after the commitment of belief to the three safety expressions because of the synthesis of the judgments produced by subsets 1 and 2.

The ER algorithm can be stated as follows (Yang and Xu, 2002; Riahi et al., 2012):

$$
\begin{aligned}
& \beta^{m^{\prime}}=K\left(M_{1}^{m} M_{2}^{m}+M_{1}^{m} H_{2}+H_{1} M_{2}^{m}\right) \\
& \bar{H}_{U^{\prime}}=K\left(\bar{H}_{1} \bar{H}_{2}\right) \\
& \bar{H}_{U^{\prime}}=K\left(\bar{H}_{1} \bar{H}_{2}+\bar{H}_{1} \bar{H}_{2}+\bar{H}_{1} \bar{H}_{2}\right) \\
& K=\left[1-\sum_{T=1}^{3} \sum_{\substack{R=1 \\
R \neq T}}^{3} M_{1}^{T} M_{2}^{R}\right]^{-1}
\end{aligned}
$$

After the above aggregation, the combined degrees of belief are generated by assigning $\bar{H}_{U^{\prime}}$ back to the three safety expressions using the following normalization process (Riahi et al., 2012):

$$
\begin{aligned}
& \beta^{m}=\beta^{m^{\prime}} / 1-\bar{H}_{U^{\prime}}(m=1,2,3) \\
& H_{U}=\bar{H}_{U^{\prime}} / 1-\bar{H}_{U^{\prime}}
\end{aligned}
$$

where $H_{U}$ is the unassigned DoB representing the extent of incompleteness in the overall assessment.

The above gives the process of combining two subsets representing the REs of two HEs. If three HEs are required to be combined, the result obtained from the combination of any two sets can be further synthesized with the third one using the above algorithm. In a similar way, multiple HEs in the bottom level of a hierarchy (i.e. components or subsystems) can also be combined (Riahi et al., 2012).

The synthesised result will be presented in a form of linguistic terms with their associated DoBs for all HEs levels in the CTOS from the bottom level to the highest-level criterion. Therefore, in order to evaluate the CTOS safety improvement, the synthesised result is converted into a single crisp value for CTOS final risk score (i.e. highest-level criterion) and can be further used with the sensitivity analysis to verify the safety importance of each HE from a systematic perspective. The utility value can be calculated by a utility-based technique as follows:

$$
R I=\sum_{h=1}^{3} p(R h) U_{R h}
$$

where, $p(R h)$ is the DoB of each grade of "Low", "Medium" and "High" in RE. $R h=$ $(1,2,3)$ and $U_{R 1}=1, U_{R 2}=50$ and $U_{R 3}=100$

# III. Sensitivity analysis to quantify the impact of HEs on the system 

Sensitivity analysis is required to evaluate the HE's risk impact by obtaining the risk magnitude of each HE on the entire system through sensitivity tests. The sensitivity tests carried out in this study have been developed to quantify the risk impact of each HE on the system.

The new sensitivity analysis approach is required to evaluate the risk impact of each HE on the system safety and rank them accordingly by taking into account their specific risk estimate (locally) and their RI to a port's safety system (globally) simultaneously. Given

the diversity of the original DoB assignment in each HE, a new sensitivity analysis approach containing three steps is proposed. First, it is to increase the DoBs associated with the linguistic term "High" to $100 \%$ and obtain the High Risk Inference (HRI). Secondly, it is to increase the DoBs associated with the linguistic term "Low" to $100 \%$ to obtain the Low Risk Inference (LRI). Lastly, the average between HRI and HLI (i.e. risk inference values) will show the True Risk Influence (TRI) of each HE on the entire system and can be calculated as follows:

$$
T R I=\frac{\mathrm{HRI}+\mathrm{LRI}}{2}
$$

In addition, the proposed methodology is validated through sensitivity tests. The sensitivity analysis refers to analysing how sensitive the result would be (i.e. outputs) to minor change in the inputs. The change may be variation of the parameters of the model or may be changes of the DoB assigned to the linguistic variables used to describe the parameters (Yang, et al., 2009). All HEs' REs assigned to the CTOS in this study were obtained from applying FRBN in Alyami et al., (2014). Different DoBs are assigned, as the input variation, to the linguistic variables used to describe the four risk parameters of the HEs, namely Probability of HE/ Likelihood (L), Consequences Probability (D), Consequences/ Severity (C) and Impact of a HE to the resilience of port operational systems (I). If the methodology is sound and its inference reasoning is logical, then the sensitivity analysis must at least pursue the following two axioms.

Axiom 1: The variation of increasing or decreasing the DoB associated with the linguistic variable "High" of a risk parameter of a selected HE will certainly result in the effect of relative increment/decrement on the RI of the model output (i.e. Goal).

Axiom 2: The total influence magnitudes of the variations associated with x (evidence) will be always greater than the one from the set of $\mathrm{x}-\mathrm{y}(\mathrm{y} \in \mathrm{x})$ (sub-evidence) given a variation follows the one defined in Axiom 1.

The reason behind the selection of the above axioms is to use the sensitivity tests to partially validate the reliability of the developed approach. It is noteworthy that it is possible to define other axioms for further research.

The synthesis of the Res of all HEs using ER can be achieved through the Intelligent Decision System software (IDS) package (Yang and Xu, 2012). The IDS selection is

attributable to its accessibility to other industries and academia. In addition, it has not only a user-friendly interface but also additional functions on knowledge management, report generation and data presentation.

# 4 A real case study on CTOS 

A large regional hub container port in the Middle East was selected to conduct a real case study to demonstrate the feasibility of the proposed ER method. The first part is to locally evaluate the RE of each HE and prioritise it accordingly by applying the FRBN introduced in Alyami et al., (2014). As a result, the outputs for the 24 HEs are obtained in terms of REs as shown in Table 1.

Table 1. Risk ranking index values of hazardous events (HEs) (Alyami et al., 2014)



The HEs associated with container terminal operations may vary, depending on the unique safety characteristics of individual container terminals. For the investigated container terminal, the FRBN deliveries the results for each HE RE locally as shown in Table 1. Consequently, using the utility calculation in Alyami et al., (2014), HE4 is the most significant event followed by HE5, HE6, HE15, and HE1, respectively.

Once the REs for individual HEs have been obtained, the second part is commencing by synthesising the REs of all HEs in the hierarchical structure to evaluate their RI to a port's safety system globally. It can be achieved by using the ER algorithm (i.e. Eqs. (1-21)) and the associated software package IDS. As a result, the RI for the investigated CTOS is described as 60.37 High, 10.56 Medium, 28.89 Low, as shown in Figure 2, and the utility value is calculated using Eq. (22) as 0.6569 .

Next step is to quantify the most significant HEs that influence the risk to a port's safety system globally by verifying the safety importance of each HE from a systematic perspective using the sensitivity analysis methods in Section 3.

![img-1.jpeg](img-1.jpeg)

Figure 2. Risk Index of container terminal operation's system (IDS) software

In this step the new sensitivity analysis approach through changing the DoBs of the risk parameters of each HE allows us to measure the TRI of each HE risk inference on the container operational system and rank them accordingly. For instance, to evaluate the TRI of HE1, the DoB belonging to the linguistic variable "High" is increased to $100 \%$ which leads to the increase of the utility value of the goal from 0.6569 to 0.662 (i.e. HRI of $0.0051=0.662-0.6569)$. Then, the DoB belonging to the linguistic variable "Low" is increased to $100 \%$ which results in the goal utility value decreases from 0.6569 to 0.636 (i.e. LRI of 0.0209 ). Next, Eq. (23) is used to calculate the TRI value of HE1 as $0.013\left(=\frac{0.0051+0.0209}{2}\right)$. Similarly, the TRI values for the 24 HEs are obtained and presented in Table 2.

Table 2: TRI for HEs on the CTOS



Accordingly, based on the results obtained in Table 2 the HEs can be prioritized in terms of their risk impact on CTOS as shown in Figure 3 and the most important events are identified as follows.

HE. 9 Ignition sources from equipment near dangerous goods premises.
HE. 8 Leakage/emission of dangerous goods from a container.
HE. 6 Crane break down due to human error.
HE. 7 Moving the crane without raising the Boom (lifting arm) of the gantry crane.
HE. 16 Person struck by falling object/s.
HE. 17 Person handling dangerous goods in containers that have not been declared.
![img-2.jpeg](img-2.jpeg)

Figure 3. The most important HEs for CTOS

In Figure 3, the risk magnitude of each HE based on their associated TRIs (i.e. the average of HRIs and LRIs).

In addition, another type of sensitivity tests in the reminder of this section has been carried out to validate the developed approach by investigating the RI magnitudes of the minor variation given to the DoB of the four risk parameters of HEs. The logicality and soundness of the results delivered in the proposed model are verified by the two axioms introduced in section 3 .

The HE of the most importance in terms of risk impact on CTOS (i.e. "HE. 9 Ignition sources from equipment near dangerous goods premises") is selected for the tests. The DoB associated with the linguistic term "High" and "Low" of the risk parameter "L" is increased and decreased by $10 \%$, respectively. Its impact is that the safety level of the CTOS increases from 0.6569 to 0.6619 . It is in a harmony with Axiom 1.

If the same DoB change (i.e. $10 \%$ increment in "High" and 10\% decrement in "Low") is applied to the other risk parameters such as "D" and "C", the combined impact of such changes on "D" and "L" is reflected by the observation that the CTOS's RI increases from 0.6619 to 0.665 . The sensitivity tests continue in the same manner. When the risk parameter " C " is combined with " L " and " D ", its impact to the CTOS' RI further increases from 0.665 to 0.6699 . When " I " is combined with " L ", " D " and " C ", the RI further increases from 0.6699 to 0.6747 as described in Table. 4. The similar sensitivity analysis was carried out to test "HE.8", and "HE.6", The obtained results are shown in Table. 4.

Table. 3: The DoB variation of the HEs


The combined variation given to the DoB associated with the linguistic term "High" (i.e. $10 \%$ increment) for the risk parameters of "HE.9", "HE.8", and "HE.6" has resulted in 125 RI values for CTOS as shown in Table. 4.

Table. 4: RI for CTOS and the variation on the HE risk parameters prior probabilities





The first row in Table 4 shows the neutral RI for CTOS with the rest of the table showing the updated RI by given variation to the DoB associated with linguistic variable "High" for "HE.9", "HE.8", and "HE.6" risk parameters locally and globally. Comparing any updated RI with the neutral RI it can be concluded that the model is validated to be in line with Axiom 1.

According to Axiom 2, if the model reflects the logical reasoning then the RI for CTOS associated with x (evidence) should be always greater than the one from $\mathrm{x}-\mathrm{y}(\mathrm{y} \in \mathrm{x})$ (subevidence). The neutral RI for CTOS is chosen as the sub-evidence to investigate the accuracy of the model. All other RIs that affected by the variation (i.e. increment) given to the DoB associated with linguistic variable "High" for "HE.9", "HE.8", and "HE.6" can be identified as the evidence. Comparing the evidence and sub-evidence (i.e. the values in the first five rows in Table 4 are gradually increasing), it can be concluded that the model is validated to be in line with Axiom 2.

# 5 Conclusion 

System safety analysis often requires the use of domain experts' knowledge when risk records are incomplete. The FRBN rationalises the DoB distribution of FRB by employing the same set of linguistic grades in both IF and THEN parts and applying them to evaluate HEs of a container terminal. It simplifies the communication between risk input and output based on DoBs and facilitates its implementation in CTOS in practice. The FRBN is integrated with the ER approach that has the ability of providing a powerful tool for aggregation calculations to synthesise the identified HEs for CTOS risk ranking. The FRBN technique is used to assess each HE locally while the ER approach is employed to take into account the risk impact of each HE to the safety of the investigated port system when evaluating their TRI globally. As a result, the integration of FRBN and ER provides an effective tool to incorporate subjective judgements for characterizing a criticality

analysis on prioritising failures in FMEA under uncertainty as well as the functional nonlinear relationship between outputs and inputs in the hierarchical evaluation process.

The HEs investigated in this study are examined through a new sensitivity analysis. The variations of TRI of the whole system due to the reallocation of DoB of any investigated HE to a level of $100 \%$ "High" (Max) and of $100 \%$ "Low" (Min) are averaged to calculate the aggregated effect of each HE to the safety performance of the whole system. The case study results confirm that the proposed method is capable of presenting sensitive and flexible risk results in real situations by simplifying the description of failure information, improving both the accuracy and visibility of FMEA, and providing a powerful risk evaluation tool for port safety management. Consequently, the ER technique determines the analysis of risk impact of each HE on the whole system. From a real case study on a large container terminal, the most significant HEs are evaluated as shown below.
HE. 9 Ignition sources from equipment near dangerous goods premises
HE. 8 Leakage/ emission of dangerous goods from a container
HE. 6 Crane break down due to human error
HE. 7 Moving the crane without raising the Boom (lifting arm) of the gantry crane
HE. 16 Person struck by falling object/s
HE. 17 Person handling dangerous goods in containers that have not been declared

In addition, the proposed method highlights its potential in facilitating risk analysis of system design and operations in a wide context when being appropriately tailored to study other seaports. However, seaports and maritime terminals (i.e. infrastructure) are facing risk challenges from various perspectives including economic, operational, technical and environmental ones. This study mainly focused on the operational aspects including technical and personal factors, leaving the other risk aspects such as managerial, policy implication, natural and political issues to be addressed in future work. Moreover, high quality representative computational modelling tools are required, not only to provide a user friendly solution in the risk evaluation process that helps to predict the risk magnitude, explain the real safety performance, and develop a continuous risk management strategy for complex systems, but also to simplify the complex risk inference processes involved in the two steps in the developed methods. Artificial Neural Networks (ANNs) seem to be a promising solution to addressing this research problem. Furthermore, a risk control option model can be developed to eliminate and/or mitigate the HEs in CTOS and to enhance the system operational efficiency.

# Acknowledgements 

The authors would like to thank the EU FP7 Marie Curie IRSES project "ENRICH" (PIRSES-GA-2013-(612546)) and the Pump Priming Fund (Pumpprime 912FET - 271002) of Faculty of Engineering and Technology at Liverpool John Moores University, UK and King Abdul-Aziz University, KSA for their financial support. They also thank the reviewers for their valuable comments to improve the quality of this paper.
