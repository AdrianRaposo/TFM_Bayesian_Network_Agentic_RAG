# Article 

## A Bayesian Network Model for Risk Management during Hydraulic Fracturing Process

Mohammed Ali Badjadi ${ }^{1, *}$, Hanhua Zhu ${ }^{2, *}$, Cunquan Zhang ${ }^{2}$ and Muhammad Safdar ${ }^{1,3}$ (D)<br>check for updates

Citation: Badjadi, M.A.; Zhu, H.; Zhang, C.; Safdar, M. A Bayesian Network Model for Risk Management during Hydraulic Fracturing Process. Water 2023, 15, 4159. https://doi.org/10.3390/ w15234159

Academic Editor: Helena M. Ramos
Received: 18 October 2023
Revised: 17 November 2023
Accepted: 26 November 2023
Published: 30 November 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Transportation and Logistics Engineering, Wuhan University of Technology, Wuhan 430063, China; safdar@whut.edu.cn
2 School of Ocean \& Energy Power Engineering, Wuhan University of Technology, Wuhan 430063, China; zhangcqbox_whut@126.com
3 Intelligent Transportation Systems Research Center, Wuhan University of Technology, Wuhan 430063, China

* Correspondence: alibadjadi@whut.edu.cn (M.A.B.); hh.zhu@163.com (H.Z.)

Abstract: The escalating production of shale gas and oil, witnessed prominently in developed nations over the past decade, has sparked interest in prospective development, even in developing countries like Algeria. However, this growth is accompanied by significant opposition, particularly concerning the method of extraction: hydraulic fracturing, or 'fracking'. Concerns regarding its environmental impact, water contamination, greenhouse gas emissions, and potential health effects have sparked widespread debate. This study thoroughly examines these concerns, employing an innovative approach to assess the risks associated with hydraulic fracturing operations in shale gas reservoirs. Through the integration of diverse data sources, including quantitative and qualitative data, observational records, expert judgments, and global sensitivity analysis using the Sobol method, a comprehensive risk assessment model, was developed. This model carefully considered multiple condition indicators and extreme working conditions, such as pressures exceeding 110 MPa and temperatures surpassing $180^{\circ} \mathrm{F}$. The integration of these varied data streams enabled the development of a robust Bayesian belief network. This network served as a powerful tool for the accurate identification of process vulnerabilities and the formulation of optimal development strategies. Remarkably, this study's results showed that this approach led to a notable $12 \%$ reduction in operational costs, demonstrating its practical efficacy. Moreover, this study subjected its model to rigorous uncertainty and sensitivity analyses, pinpointing the most severe risks and outlining optimal measures for their reduction. By empowering decision-makers to make informed choices, this methodology not only enhances environmental sustainability and safety standards but also ensures prolonged well longevity while maximizing productivity in hydraulic fracturing operations.

Keywords: shale gas reservoirs; hydraulic fracturing; risk assessment; Bayesian belief network; sensitivity analysis; enhanced oil recovery

## 1. Introduction

Commercial production of shale gas dates back to the 1970s in the United States and Canada, and more recently, in 2016, it began in the United Kingdom. The estimated technically recoverable shale gas resources in the UK stand at approximately 0.57 trillion cubic meters. Other countries, including China, Argentina, and Algeria, possess substantial technically recoverable shale gas reserves, with estimated volumes of 31,22 , and 11 trillion cubic meters, respectively, positioning them as potential future contributors to global shale gas production. However, the comprehensive impacts of widespread shale gas utilization remain contentious, sparking intense debates among stakeholders. Opponents contend that potential environmental repercussions, such as drinking water contamination, and challenges in wastewater management could outweigh the perceived benefits, especially in areas that suffer from water scarcity. It is especially in the realm of water-related concerns that special attention is warranted. Extensive research on shale gas exploration has

been conducted in various developed and developing countries, shedding light on shared challenges and deficiencies. These studies span diverse geographical regions, consistently highlighting environmental risks, regulatory insufficiencies, and social consequences associated with shale gas operations. Over the past five years, global research efforts have intensified, leading to advancements in best practices and innovative technologies for shale gas extraction. Turning our attention to Algeria, an emerging player in the shale gas arena, offers valuable insights into this nation's unique context and potential within the dynamic shale gas sector (Figure 1) [1–6].

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Algeria's oil and gas resources [7].

This research work involves attending field operations and conducting quantitative analyses through various tools used in the oil and gas field. Starting from hazard identification using HAZOP analysis, a fault tree analysis (FTA) is created, and initial results are analyzed to determine the level of risks through an event tree (ET). This approach allows for linking the causes and consequences of the operation, including failure or destruction of the well and reservoir. BBN models have been proposed as an approach to analyze risks associated with hydraulic fracturing system accidents. BBN facilitates the modeling of complex and dynamic behavior of real-world systems by structuring the integrated simulation based on input nodes and resultant nodes. One useful approach for providing input data to BBN models is the use of matrices generating Conditional Probability Tables (CPT). The results obtained from a BBN model enable the creation of CPTs, which can be used to evaluate the model and calculate sensitivity through large-scale analyses of uncertainty to attain more accurate results. The primary goals of hydraulic fracturing operations include increasing oil and gas flow, eliminating formation damage near the borehole wall, and interconnecting high-permeability zones. Success in hydraulic fracturing depends on selecting the appropriate hydraulic penetration technology, creating complex gel-fracture volumes with higher flow conductivity, and deploying fracture volumes rationally along the hole section. The process includes preflight, gel injection, and over flush stages. Overall, viscous slick water is used in the perforation stage; meanwhile, pads and gels are injected in different stages to propagate and etch fractures. Over flush is used to enhance gels' penetration distance. Figure 2 illustrates the intricate process of hydraulic fracturing operations. In this detailed visual representation, key elements of the fracturing process come to life. In recent years, the rapid expansion of hydraulic fracturing, or 'fracking', for shale gas and oil extraction

has sparked global interest and debate. While developed nations have embraced this technology, concerns regarding its environmental impact, water contamination, and potential health risks have raised significant opposition. Moreover, there is a lack of comprehensive studies that address these concerns using innovative and integrative approaches, especially in the context of developing countries like Algeria. Recognizing these gaps, this study aims to bridge the existing knowledge deficit by conducting a thorough examination of the risks associated with hydraulic fracturing operations in shale gas reservoirs. By integrating diverse data sources, employing advanced analytical methods, and conducting rigorous sensitivity analyses, this research endeavors to provide a nuanced understanding of the challenges posed by hydraulic fracturing [3,4,5,8].
![img-1.jpeg](img-1.jpeg)

Figure 2. Hydraulic fracturing operation [8].
In contrast to conventional techniques such as manual calibration and heuristic approaches, Bayesian networks offer a superior methodology for evaluating hydraulic fracturing risks. Manual methods, often lacking precision and time efficiency, are eclipsed by Bayesian networks' structured and automated approach. With the advent of artificial intelligence technologies, leveraging extensive data processing capacities, reliance on sensors for real-time data transmission and Bayesian network processing has become integral. This establishes Bayesian networks as a preferred choice for assessing potential risks in hydraulic fracturing, particularly in challenging shale gas reservoir conditions. This shift towards automated and sophisticated approaches ensures more accurate and efficient decision-making, ultimately contributing to the sustainable and effective exploitation of shale gas resources $[8,9]$.

This paper focuses on assessing the potential risks associated with hydraulic fracturing in a shale reservoir located in Algeria, which is an area grappling with water scarcity. The reservoir's unique characteristics, including low permeability and narrow dimensions, present challenges typical of such formations. Employing a Bayesian network, the study explores various scenarios and uncertainties that could lead to operational failures or increased environmental risks. The goal is to enhance the management of the hydraulic

fracturing process, mitigating these risks while optimizing costs. By doing so, the paper aims to contribute to the sustainability and effectiveness of shale gas exploitation in this region. Through rigorous analysis and innovative techniques, this research endeavors to pave the way for more efficient and responsible practices in the realm of hydraulic fracturing [4,10,11,12,13].

This paper is organized into six sections. Sections 1 and 2 set out the introduction and methodology of the work, which formulates hazard identification and development of an event tree (ET) and determines the quantitative assessment of potential risks using BBN. Section 3 demonstrates the results and main findings of the hydraulic fracturing process with the elicitation of the BBN model, an evaluation of sensitivity analyses and validation of the BBN model. Section 4, provides a discussion of the analyses and Finally, Section 5 delineates summary of paper, limitation, and future recommendations.

## 2. Methodology

### 2.1. Case Study

This study delves into the intricacies of hydraulic fracturing in different shale gas wells located in the In Salah region of Algeria. The reservoir at a depth of 3600 m is characterized by its heterogeneous clayey nature. Geographical details of this location are depicted in Figure 3. This paper systematically explores various catastrophic scenarios inherent in the hydraulic fracturing process, meticulously analyzing results to mitigate risks and enhance professional implementation [7,9,14].

![img-2.jpeg](img-2.jpeg)

Figure 3. The upstream hydrocarbon in the In Salah region of Algeria.

### 2.2. Formulation, Hazard Identification, and Development of an Fault Tree

In this study, a fault tree (FT) model is employed for system safety analysis within hydraulic fracturing operations, integrating hazard identification and an event tree setup based on field data. The methodology enables a comprehensive assessment of qualitative risks by utilizing the combined fault tree and event tree to represent various scenarios. Figure 4 illustrates the actual hydraulic fracturing process and the equipment used at the surface level for this operation. The necessary field data, crucial for this study, were obtained from different shale gas wells related to this process. Expert opinions in the field were collected, translated, and analyzed through the error tree, with the assistance of the Top Event FTA program. The methodology allows for a comprehensive assessment of qualitative risks, using the combined fault tree and event tree to represent multiple scenarios. The risk assessments rely on the Bayesian belief network (see Figure 5) [15,16,17,18].

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Real equipment employed in a hydraulic fracturing operation for study modeling.

The process involves two key steps: hazard identification, which evaluates risk factors and potential hazards that could cause harm, and fault tree development, which is a systematic quantitative analysis that is conducted through the development of a fault tree (Figure 6). The proposed framework integrates results from both fault tree and event tree analyses, establishing links between causes and results for scenario analysis during the hydraulic fracturing process. This integrated approach forms the foundation for Bayesian belief network (BBN) modeling, as demonstrated in Table 1, which serves as the basis for linkage in this study [9,10,19,20].

![img-4.jpeg](img-4.jpeg)

Figure 5. Flowchart of the study model.

![img-5.jpeg](img-5.jpeg)

Figure 6. Hydraulic fracturing fault tree diagram by using TopEvent FTA Express Fault Tree Analysis Software Version 1.2.3 Copyright 2019 Reliotech S.A.S de C.V.

Table 1. Integrating results from fault tree and event tree analyses.


Table 1. Cont.


# 2.3. Building a BBN Model 

A Bayesian belief network (BBN) emerges as a potent diagnostic tool for identifying system faults in the context of hydraulic fracturing. Utilizing hierarchical graphs, the BBN adeptly captures probabilistic causal relationships among uncertain variables, which are crucial when confronted with limited data. This dynamic model learns continuously from both historical and real-time data, adapting its understanding during hydraulic fracturing processes based on observed changes [6,12,21]. The categorization of nodes into root nodes (RN), consequence nodes (CN), and safety nodes (SN) enhances the system's fault identification capabilities. Links in the BBN symbolize associations, reflecting variable states and conditional probabilities for consequence nodes. When safety or consequence nodes lack root nodes, probabilities are considered unconditional. A fault tree, visually represented in Figure 6, encapsulates this hierarchical structure, aiding in the comprehension of fault scenarios. This adaptive model, tailored for hydraulic fracturing intricacies, ensures continual learning and updates, contributing to effective fault identification and, consequently, heightened system safety and performance. In essence, the BBN model provides a comprehensive framework that amalgamates historical and real-time data, categorizes nodes meaningfully, and utilizes conditional probabilities to evaluate fault scenarios, ultimately enhancing system resilience in hydraulic fracturing [12,14,22].

In Figure 7, the initiation of modeling and probabilistic programming is demonstrated using Software GeNIe Academic Version 4.0.1922.0, which is specifically tailored for Bayesian belief networks (BBN) in the context of real-time hydraulic fracturing process data. The model's beliefs align with fault tree analysis and event tree, while the links signify causal connections between them. Notably, the model encapsulates intricate relationships, such as the consequence node linking strata with high in situ stress in shale gas reservoirs to high permeability zones and near-wellbore friction. This representation, as depicted in Figure 8, provides a visual roadmap for understanding the interplay of variables, facilitating effective fault analysis and enhancing the system's adaptive learning in hydraulic fracturing scenarios $[6,13,15,23]$. In addition, Figure 7 illustrates a Bayesian network model through groups defined as $\mathrm{G}=\mathrm{RN}, \mathrm{SN}, \mathrm{CN}$, which correspond to FTA and ET. It can be simplified into variables and expressed in the results as $G=V, A$, where $V$ refers to node groups of different variables and the group of their related A , giving $\mathrm{V}=\{1, \ldots . . n\}$ and $A=\{(i, j) i, j \in V, i=j\}$. Meanwhile, the output result node i relates to the value of the variable and root nodes. The equation $R(i)=\{j \in V \mid(j, i) \in A\} R(i)$ represents the root nodes for each of the consequence nodes, and the safety node is represented as $i$.

![img-6.jpeg](img-6.jpeg)

Figure 7. Selecting node types and building a BBN model.
A path $D=\left(d_{1} \ldots . . d_{n}\right)$ is a link vector for each state of $d_{i} \in D_{i}$ for each variable $\in V$ that has the same probability distribution:

$$
P(d) \prod_{i=1}^{n} P\left(\frac{d_{i}}{D_{R(i)}}\right)
$$

This is given if the probability of the variable is without a root $\left(D_{R(i)}=\varnothing\right)$ and the negligible probabilities are $P\left(D_{i}\right)=P\left(X_{i}=d_{i}\right)$.

Equation (2) expresses the state of variables with the root of each variable through conditional probabilities

$$
P\left(\frac{d_{i}}{D_{I}}\right)=P\left(X_{i}=d_{i} \mid X_{j}=D_{j}, j \in R_{(i)}\right)
$$

where $D R_{(i)}$ represents the situation group of root nodes of $i$.

![img-7.jpeg](img-7.jpeg)

Figure 8. The likelihood probability of high permeability zones and near-wellbore friction estimation for a BBN model using MATLAB software Version information for MathWorks R2022b.

# 2.4. A BBN for Hydraulic Fracturing 

The Bayesian belief network (BBN) model for hydraulic fracturing intricately connects nodes through probability distributions, articulating the maximum likelihood of various scenarios. Non-root nodes are characterized by continuous probability distributions, while conditional probabilities govern other nodes. Given the specificity and complexity of shale gas exploitation, extensive research and fieldwork are undertaken, as are collaborations with experts to collect and analyze data. This comprehensive approach, integrating artificial intelligence, focuses on developing a Bayesian belief network (BBN) capable of modeling and real-time prediction. Particularly, the model focuses on the propagation of Pressure Wave Peaks (PWPs) within coal rock fissures during hydraulic fracturing, as illustrated in Figure 8. The utilization of MATLAB software for modeling estimates the likelihood probability of high permeability zones and near-wellbore friction, showcasing the BBN model's predictive capabilities in this intricate process [24,25,26].

These pressure waves are pivotal in assessing the effectiveness of the fracturing process [27]. To model PWP propagation, we utilize the following equations:

Equation (1)—original pressure wave equation:

$$
P=A \sin (h) 2 \pi f\left(\frac{x}{c} t\right)+4 i
$$

where
$P$ represents the transient pressure loaded on the coal in kPa ;
$A$ is the PWP peak in kPa ;
$f$ is the PWP frequency in Hz ;
$c$ is the velocity of the wave in $\mathrm{m} / \mathrm{s}$;
$p$ is the position in m ; and
$t$ is the transient time in s .
Equation (2)—corrected pressure wave equation:

$$
P=P_{0}+\mathrm{A} \sin (h) 2 \pi f\left(\frac{x}{c} t\right)+4 i
$$

$P_{0}$ represents the average of the PWP that did not change during the PWP propagation period. Equation (1) represents the initial pressure wave equation, while Equation (2) corrects it by accounting for a constant offset represented as $P_{0}$ [18]. Additionally, we examine the synthesized wave resulting from incident and reflected waves using Equation (3)Synthesized Wave Equation:

$$
A_{0}=\sqrt{A_{1}^{2}+A_{2}^{2}+2 A_{1} A_{2} \cos (4 \theta)}
$$

where
$A_{0}$ is the PWP peak of the synthesized wave;
$A_{1}$ and $A_{2}$ are the amplitudes of the incident and reflected waves, respectively; and
$\theta$ is the phase difference between the incident and reflected waves.
This equation helps us understand how incident and reflected waves interact constructively, providing insights into the PWP peak at the fissure end [19].

In the context of the Bayesian belief network (BBN) model for hydraulic fracturing, nodes are interconnected using probability distributions to express the scenario likelihood. Continuous probability distributions are used for non-root nodes, while conditional probabilities are applied to other nodes. Since the model often deals with qualitative data, expert elicitation is preferred when no quantitative data is available [20,27,28].

Hazard identification, fault analysis, and expert opinions contribute to constructing the Conditional Probability Table (CPT), ensuring the model's credibility and realism [21]. Integrating these mathematical equations into our BBN model enhances our ability to predict and effectively manage the hydraulic fracturing process.

Furthermore, the relative weight values of each node play a vital role. Root formations are compatible with each state of nodes, such as reservoir contamination, fluid efficiency, exceeding equipment loading capacity, error in the hydraulic system, near-wellbore friction, damage in the reservoir, and shortening the well's life. The relative weight of the node varies between one and zero, expressing the value of the weight in the node and the mutual effects between the root node and the consequence node [22,28,29].

To develop the hybrid Bayesian network (HBN), we utilize the fault tree model from the second section. The CPT is defined according to the location and function of nodes and their influence on the states of consequence nodes. In the BBN, nodes are categorized into pivot nodes with respect to sample sizes of root nodes, safety nodes, and consequence nodes $[22,27,30]$.

Table 2 summarizes the scenario analysis for hydraulic fracturing failure using three methods: likelihood, EBBN, and Weighted Sum Algorithm. These methods calculate the likelihood of failure scenarios related to the propagation of Pressure Wave Peaks (PWPs), providing valuable insights for risk management and decision-making [19,20,21,22]. These methods are essential for risk assessment in hydraulic fracturing.

Table 2. Scenario analysis of the BBN obtained from the three-method framework.


# 3. The Main Results of Bayesian Belief Networks 

The primary outcomes of Bayesian belief networks (BBNs) hinge on a judicious assignment of a priori probabilities, expert input, and the application of artificial intelligence algorithms, particularly in scenarios with limited data. Sensitivity analysis becomes crucial in contexts of restricted data to pinpoint influential input parameters that significantly

affect the output results. The BBN model relies heavily on nodes, shaping its structure through conditional probabilities in both inputs and outputs. The strategic setting of probabilities serves the dual purpose of exploring sensitivity and facilitating analysis-assisted optimization through model calibration. To enhance the integrity of the BBN model, which deals with both discrete and continuous values of input parameters, a variance reduction method is employed. This method allows for an in-depth assessment of the BBN model's sensitivity to variations in specific input parameters, contributing to the model's overall optimization [6,8,22,24,31].

### 3.1. Finding Sensitivity Parameters

The Sobol indices are utilized for global sensitivity analysis, providing a robust method to assess the relative significance of input parameters on model outputs. This analysis reveals the extent to which interactions between specific inputs influence the overall output. For instance, it might indicate that 90% of the output is due to the interaction between two inputs, with one contributing 8% of the variance and the other 2% (see Figure 9). This approach is applied to characterize the dynamic system of the environment impacted by hydraulic fracturing, incorporating changes and developments expressed within the BBN model for shale gas reservoir hydraulic fracturing [21,25,26].

![img-8.jpeg](img-8.jpeg)

**Figure 9.** Diagnostic BBN for hydraulic fracturing using GeNIe academic software version 4.0.1922.0.

The variance-based Sobol sensitivity method explores the multidimensional space of the unknown input parameters $X$ with a certain number of Monte Carlo samples. The sensitivity indices, both first order and the higher interactions between the unknown input parameters, are generated by a decomposition of the BBN model function $Y=f(X)$ in a d-dimensional factor space into summands of increasing dimensionality [30,32,33]:

$$
\gamma=f_{0}+\sum_{i=1}^{d} f_{i j}\left(X_{i}\right)+\sum_{i<j}^{d} f_{i j}\left(\mathrm{X}_{i}, \mathrm{X}_{j}\right) \ldots \ldots .+f_{1,2}, \ldots ., d\left(\mathrm{X}_{1}, \mathrm{X}_{2}, \ldots \ldots, \mathrm{X}_{d}\right)
$$

where the constant $f_{i}$ is a function of $X_{i}$ and $f_{i j}$ is a function $\left(X_{i}, X_{J}, \ldots .\right) d x_{i k}=0.1 \leq k \leq$ $S_{i}, S_{i j}=1, \ldots d$, etc. A condition of this decomposition is the total number of summands in Equation (2).

$$
\int_{0}^{1} f_{i_{1} i_{2} \ldots \ldots i_{s}}\left(\mathrm{X}_{i_{1}} \mathrm{X}_{i_{2}}, \ldots \ldots \mathrm{X}_{i_{s}}\right) d X_{K}=0, \text { for } \mathrm{K}=i_{1} \ldots \ldots . . i_{s}
$$

Functional elements are expressed by conditional probability values,

$$
\begin{gathered}
f_{0}=E(Y) \\
f_{i}\left(X_{i}\right)=E\left(\frac{Y}{X_{i}}\right)-f_{0} \\
f_{i j}\left(X_{i}, X_{j}\right)=E\left(Y / X_{i} X_{j}\right)-f_{0}-f_{i}-f_{j}
\end{gathered}
$$

We develop the function $f\left(X_{i}\right)$ to become of the second degree so that the function $f_{i j}$ can be defined by the terms $i j$ and the main variables $X_{i}$ and $X_{j}$. This assumes that the factorization results from the integral of the function $(X)$ are squared as follows:

$$
f^{2}(X) d x-f_{0}^{2} \sum_{s=0}^{d} \sum_{i_{1}<\cdots<i_{s}}^{d} \int f_{i=1}^{2} \ldots . . i_{s} d\left(X_{i_{1}}\right) \ldots \ldots d(X)_{i_{s}}
$$

The following properties hold for variance expression indices:

$$
\operatorname{Var}(Y)=\sum_{i_{1}}^{d} V_{i}+\sum_{i<j}^{d} V_{i j}+\cdots . . V_{12} \ldots \ldots . . d
$$

where

$$
\begin{gathered}
V_{i}=\operatorname{Var} X_{i}\left(E_{X_{-i}}\left(\frac{Y}{X_{i}}\right)\right. \\
V_{i j}=\operatorname{Var} X_{i j}\left(E_{X_{-i j}}\left(\frac{Y}{X_{i} X_{j}}\right)\right)-V_{i}-V_{j}
\end{gathered}
$$

Based on the total conditions of variance, the outputs are explained through the analysis of variance according to the condition of each input. $X \sim i$ stands for variables excluding the value of $X_{i}$, which is the main sensitivity indicator.
$S_{i}$ is an indicator of sensitivity called the first order of sensitivity and is given as follows:

$$
S_{i}=V_{i} / \operatorname{Var}(Y)=d_{i} / D(Y)
$$

It is considered that the main outputs of the variables $X_{i}$ express the state of variable $X_{i}$ alone in order to calculate the mean value of the various inputs through the total variance, which in turn enables the formation of additional indicators, $S_{i j}$ and $S_{i j k}$. Depending on $(Y)$, the outputs are expressed as follows:

$$
\sum_{i=1}^{d} S_{i}+\sum_{i<j}^{d} S_{i j}+\cdots \ldots . . S_{12} \ldots . . d=1
$$

Since the model contains a large number of variables, the indicators are computationally expensive, so the total order index $S_{T_{i}}$ that is used to measure all the variance outputs for $X_{i}$ is not given here.

# 3.2. Calculation of Indices 

In examining the statistical dependencies and their implications for the performance of the Bayesian belief network (BBN) in hydraulic fracturing, we employ Monte Carlo integrations and Sobol's estimation. This methodology unveils crucial parameters within the BBN framework, facilitating a comprehensive assessment of system behavior. By integrating Sobol's variance-based method with Monte Carlo simulations, primary order and total sensitivity indices are evaluated. Utilizing the BN Toolbox© in Matlab ${ }^{\circledR}$, these analyses reinforce the robustness of the model for risk assessment in hydraulic fracturing processes, contributing to improved risk diagnosis [20,22,34].

Table 3 illustrates the results of a simulation with over 5000 iterations using Matlab, displaying calculated sensitivity indicators for the BBN model. These outcomes underscore the model's reliability and its potential to optimize decision-making in hydraulic fracturing scenarios, aligning with the objective of ensuring safer and more efficient operations. To quantitatively compare the prediction accuracy of the order index, two evaluation indexes-root mean square error (RMSE), mean absolute error (MAE), and coefficient of determination $\left(R^{2}\right)$-are introduced. RMSE and MAE reflect the predictive error, with lower values indicating better algorithm performance. $R^{2}$, assessing goodness of fit, ranges from 0 to 1 , with a score closer to 1 indicating a superior model fit [35-37].

Table 3. The sensitivity analysis results for the BBN by Sobol's estimation based on Monte Carlo integrations.


Root mean square error $(R M S E)$ :

$$
R M S E=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(\hat{y}_{i}-y_{i}\right)^{2}}
$$

Mean absolute error $(M A E)$ :

$$
M A E=\frac{1}{n} \sum_{i=1}^{n}\left|\hat{y}_{i}-y_{i}\right|^{2}
$$

Goodness of fit $\left(R^{2}\right)$ :

$$
R^{2}=1-\frac{\sum_{i=1}^{n}\left(\hat{y}_{i}-y_{i}\right)^{2}}{\sum_{i=1}^{n}\left(y_{i}-\hat{Y}_{i}\right)^{2}}
$$

# 4. Discussion 

### 4.1. Analysis of the Most Important Scenarios Proposed from the BBN Framework

During the well hydraulic fracturing, Bayesian network-driven intelligent artificial analysis explores scenarios, identifying components causing process failure or undesired outcomes. Utilizing a purpose function measures the risk score ( $R S$ ), enabling precise risk assessment. The function is combined with Bayesian network probabilities to evaluate failure consequences through a sorting probability calculation, as depicted in the Equation below [37-39].

$$
R S(S e)=\frac{E\left[\frac{U}{S e} \right] P(S e)}{E[U]}
$$

where
$S e$ is the scenario exclusion;
$P(S e)$ is the probability of scenario $\mathrm{Se} ;$
$E[U]$ is the expected disutility where $E[U]=\sum_{u \in S^{+}} P(S) U\left[X_{u}\left(S_{I(u)}\right)\right]$;
$X_{u}\left(S_{I(u)}\right)$ is the function of combinations of parent states of the value for 1 , which belongs to components that fail in the system, and 0 , which presents them otherwise;
$R S(S e)$ is the risk share; and
$E\left[\frac{U}{S e}\right]$ is the conditional expected disutility function for scenario $S e$.
Table 4 outlines the outcomes of the sensitivity analysis, emphasizing the most critical scenarios in hydraulic fracturing that pose a potential risk of process failure. Significantly higher probability rates are observed for CN1, CN10, and RN8, signaling heightened risks to the well and reservoir. In contrast, lower rates are attributed to RN12. These results underscore the substantial influence of specific crucial variables, especially inherent factors that are challenging to control. Effectively addressing factors like rock-gel friction in diverse reservoirs becomes essential for enhancing fracture conductivity and projecting fracture pressure to achieve desired operational results [19,26,40].

Table 4. The four riskiest scenarios based on the consequence framework.


The findings reveal substantial variations between scenarios, notably indicating a heightened failure rate in the fourth scenario. This emphasizes the critical need to prevent non-homogeneous tank pressure surges as they can significantly jeopardize well performance and overall results. Industry experts in oil and gas, particularly those focused on engineering and production, are urged to reassess the most perilous scenarios, particularly involving CN1, RN8, and factors influencing the RN12 node, such as temperature and unfavorable physical properties [29,40,41].

### 4.2. The Results of Sensitivity Analysis and Partial Validation

This section consolidates previous efforts and outcomes in constructing an integrated model aimed at averting failures in hydraulic fracturing processes within non-conventional reservoirs. Failures in such processes can result in diminished production, shortened well lifespan, and increased financial and environmental losses. The fault tree was initially developed, followed by the creation of the Bayesian belief network (BBN) model (Figure 10). The MATLAB simulations in Figure 11 provide a real-time, quantitative comparison of prediction accuracy within the BBN modeling framework. This crucial analysis focuses on three specific scenarios: RN1, RN8, and RN10. Two evaluation indices—root mean square error (RMSE), mean absolute error (MAE), and coefficient of determination (R²)—were employed to quantitatively compare predictive accuracy. These results, validated through expert consultation, offer insights into mitigating the most perilous scenarios and conducting simulations to minimize failure risks based on artificial intelligence technology [18,30,35]. The network, depicted in Figures 12 and 13, calculates probabilities based on expert opinions from the shale gas industry, integrating the predictive capabilities of artificial intelligence technology [18,35].

developing control models for operators and engineers to avert failures and achieve desired outcomes [8,30,42].![img-9.jpeg](img-9.jpeg)

Figure 11. Real-time quantitative comparison of prediction accuracy for scenarios RN1, RN8, and RN10 using Matlab in Bayesian belief network modeling.

![img-10.jpeg](img-10.jpeg)

Figure 12. The probability parameters for consequence nodes.

![img-11.jpeg](img-11.jpeg)

**Figure 13.** The probability parameters for root nodes.

![img-12.jpeg](img-12.jpeg)

**Figure 14.** *Cont*.

![img-13.jpeg](img-13.jpeg)

Figure 14. Simulation of calculating sensitivity indices using MATLAB software with a number of runs between 100 and 1000.

![img-14.jpeg](img-14.jpeg)

Figure 15. Cont.

![img-15.jpeg](img-15.jpeg)

Figure 15. Simulation of calculating sensitivity indices using MATLAB software with a number of runs between 5000 and 10,000.

# 4.3. The Cost-Benefit Analysis 

To assess the economic feasibility of the proposed risk management approach using the BBN model, a cost-benefit analysis was conducted [7,10,31,33]. This study has presented a comprehensive analysis of the hydraulic fracturing process in hydrocarbon reservoirs, specifically focusing on identifying potential failure scenarios and the factors contributing to these failures. This study adopted a Bayesian belief network (BBN) model to effectively predict risks and enable informed decision-making to avoid failures in advance. It also involved experts to help identify the most influential scenarios and calculate the probability of failure using sensitivity analysis techniques. A critical aspect of the present study was the cost-benefit analysis, which allowed the evaluation of the effectiveness of various mitigation plans in reducing the probability of failure and their associated costs. This analysis aimed to provide a comprehensive understanding of the balance between the costs of implementing mitigation measures and the benefits of reduced failure probabilities [7,8]. The cost-benefit analysis, based on the mitigation plans and associated costs of the hydraulic fracturing process, is outlined in Table 5 and can be summarized as follows.

Table 5. Mitigation plans (based on nodes), associated costs, and reduction of probability of failure in the hydraulic fracturing process.


The total cost of implementing all the proposed mitigation plans is USD 175,000.
Implementing these mitigation plans can significantly reduce the risks associated with hydraulic fracturing operations by leading to more efficient and reliable processes, increased production, and extended lifespan of the wells. The cost-benefit analysis highlights the importance of investing in mitigation measures to minimize the risks of failure in hydraulic fracturing processes, which can ultimately result in significant economic and environmental benefits.

# 5. Conclusions 

The hydraulic fracturing process plays a pivotal role in enhancing production and prolonging well life in shale gas reservoirs. Adopting a dynamic Bayesian belief network (BBN) model becomes imperative to comprehend the multifaceted factors influencing well cracking processes and reservoir dynamics. This model facilitates risk prediction and informed decision-making, steering clear of potential failures. Field studies and expert insights contribute to scenario identification, and a resulting event tree model transforms into a BBN model, depicting causal relationships between factors.

Conducting sensitivity analysis techniques on this dynamic BBN model achieves an impressive $85 \%$ accuracy in predicting failure scenarios. Beyond cost savings, the model's risk management capabilities potentially extend well life by up to $20 \%$, translating into substantial yearly revenue. The BBN model emerges as a financial boon while significantly enhancing operational sustainability and longevity. Its precision in predictions and risk mitigation strategies serves as a linchpin for the success and economic viability of hydraulic fracturing operations.

To enhance the BBN model's effectiveness in mitigating hydraulic fracturing failures, crucial strategic measures are imperative. Collaboration with industry stakeholders is essential for comprehensive data collection, reinforcing the model's accuracy with precise datasets. Advanced machine learning and additional data refinement can ensure high accuracy, even in scenarios with limited information like S1 and S4, preventing the risk prevalence probability rate from exceeding 0.01 after model adoption. This strategic enhancement has the potential to elevate prediction accuracy beyond $96 \%$, transforming decision-making. Regular assessment of mitigation plans prioritizes cost-effectiveness, minimizing operational costs while maintaining safety and fostering environmental and financial sustainability in the shale gas sector. This comprehensive approach underscores the pivotal role of the BBN model in revolutionizing hydraulic fracturing operations, providing a pathway to economic success, safety, and environmental responsibility.

Author Contributions: M.A.B.: conceptualization, formal analysis, investigation, methodology, resources, software, project administration, validation, visualization, writing, original draft, and writing, reviewing, and editing. H.Z.: supervision, funding acquisition, project administration, and resources. C.Z.: supervision and investigation. M.S.: writing, reviewing, and editing and visualization. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: Data is contained within the article.
Acknowledgments: The authors wish to convey their heartfelt thanks to Wuhan University of Technology for granting the valuable opportunity to undertake and present this research study. Furthermore, the authors express gratitude to their fellow researchers who contributed to the preparation of this manuscript. Special appreciation is extended to Sonatrach Company's IAP (Algerian Petroleum Institute), Sonatrach CRD (Center for Research and Development), and Sonatrach DP (production division) for furnishing the essential data needed to finalize this research. The generous support and collaborative efforts of these entities have played a crucial role in the accomplishment of this investigation.

Conflicts of Interest: The authors declare no conflict of interest.

