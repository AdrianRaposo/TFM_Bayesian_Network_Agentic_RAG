# Article 

## The Safety Risk Assessment of Mine Metro Tunnel Construction Based on Fuzzy Bayesian Network

Qiankun Wang ${ }^{1,2}$, Jiaji Zhang ${ }^{1,2}$, Ke Zhu ${ }^{1,2, * *}$, Peiwen Guo ${ }^{2, *}$, Chuxiong Shen ${ }^{2}$ and Zhihua Xiong ${ }^{1,2}$

## check for updates

Citation: Wang, Q.; Zhang, J.; Zhu, K.; Guo, P.; Shen, C.; Xiong, Z. The Safety Risk Assessment of Mine Metro Tunnel Construction Based on Fuzzy Bayesian Network. Buildings 2023, 13, 1605. https://doi.org/ 10.3390/buildings13071605

Academic Editor: Jaewook Jeong
Received: 4 June 2023
Revised: 22 June 2023
Accepted: 23 June 2023
Published: 25 June 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Sanya Science and Education Innovation Park, Wuhan University of Technology, Sanya 572000, China; wangqk@whut.edu.cn (Q.W.); zhangiaji@whut.edu.cn (J.Z.); 335255@whut.edu.cn (Z.X.)
2 School of Civil Engineering and Architecture, Wuhan University of Technology, Wuhan 430070, China; 1378638258@whut.edu.cn

* Correspondence: zhuke2018@whut.edu.cn (K.Z.); guopeiwen@whut.edu.cn (P.G.)

Abstract: With the acceleration of urbanization, the construction of urban subway tunnel networks is advancing towards deeper, denser, and larger subterranean forms. Currently, there is a lack of systematic identification and dynamic reasoning analysis of factors throughout the entire process of subway tunnel construction using the mining method. To reduce the probability of accidents and improve safety risk management in the whole process of subway tunnel construction using the mining method, we propose a dynamic safety evaluation method based on Fuzzy Set Theory (FST) and Bayesian Network (BN). Firstly, based on the identification of main stages of the construction process using the Work Breakdown Structure, a safety risk evaluation index system for subway tunnel construction using the mining method was constructed according to the Risk Breakdown Structure. Secondly, by combining Fuzzy Set Theory, the Analytic Hierarchy Process, and the Bayesian Network, we established a dynamic safety risk evaluation model for subway tunnel construction using the mining method, based on FBN. Lastly, taking a large-section tunnel project using the mining method as an example, the effectiveness and accuracy of this model were verified. The results showed: (1) Causal reasoning analysis indicated that, under the condition of known prior probability, if the case reasoning result is greater than $5 \%$, there is a significant possibility of a safety risk incident. The evaluation results of the model are basically consistent with the actual situation. (2) Diagnostic reasoning analysis revealed that factors such as the tunnel excavation method, the quality of the main waterproof construction, the quality of the detailed construction waterproofing, the design of the monitoring and measurement plan, and the results of the monitoring and measurements, are the main influences on the safety of subway tunnel construction using the mining method. (3) Secondary diagnostic reasoning demonstrated that repeated diagnostic reasoning for the main influencing factors, leading to an investigation path dominated by critical risk factors, can effectively reduce the overall project risk. This research is expected to provide useful insights for the scientific management of safety risks in the construction of subway tunnels using the mining method.

Keywords: mining method; subway tunnel construction; safety risk analysis; fuzzy set theory; Bayesian network

## 1. Introduction

The transportation infrastructure represented by urban subways is the spatial foundation of social development [1]. Metro tunnel engineering is a large-scale civil engineering project with large investment, long construction period, and complex technology. Compared with other projects, subway tunnel engineering has the characteristics of concealment, uncertainty of geological environment, and complexity of construction technology, which inevitably leads to a large number of risks and complex types during the construction period [2]. In China, the number of construction accidents in subway tunnel projects has shown an upward trend in the past decade [3]. Therefore, it is necessary to study the construction safety risk management of subway tunnel projects [4].

As a process method for subway tunnel construction, the mining method has the advantages of no pollution, no noise, and little impact on urban traffic [5]. It is widely used in urban subway construction under the condition of loose soil surrounding rock media. Compared with the shield method [6], the tunnel construction process using the mining method is complex and involves multiple types of work, resulting in high safety risks and frequent safety accidents [7,8]. Therefore, it is of great importance to analyze and evaluate the safety risks of subway tunnel construction using mining methods in the whole construction process.

In recent years, many scholars have conducted relevant research in the field of safety risk assessment for metro tunnel engineering. Taking all factors into consideration regarding the uncertainties of urban rail transit projects construction and incompatibility of the assessment conclusion, Yan et al. (2019) [9] proposed a vague fuzzy matter-element model for the risk assessment by combining vague set and matter-element theory. Based on the Wuhan subway tunnel accident, Liu et al. (2018) [10] proposed a systematic method by integrating exploratory factor analysis (EFA) and structural equation model (SEM) to examine the risk factors for the safety of metro construction. Hai et al. (2022) [11] simulated the evolution process of utility tunnel risks based on the latent Dirichlet allocation algorithm, the NK model and the system dynamics to realize unbiased and accurate estimates. Chang et al. (2023) [12] proposed a new causality-based multi-model ensemble learning approach for the safety assessment of metro tunnel construction, and applied it to Wuhan Metro Line 6 as an example. Zhou et al. (2020) [13] presented a new method and system to assess and manage the risks during the construction process by coupling the risk management system and the quality management system and integrating jobsite monitoring data, design data, and environmental data through a study on the risks of undersea tunnel construction. Guo et al. (2020) [14] applied resilience theory in safety management to three subway construction sites: the Shuangzhai, the Sports Centre and the Sanyizhuang stations on the Xi'an Metro Line 14.

In the field of safety risk management research combining specific tunnel excavation methods, Hyun et al. (2015) [15] discussed the potential risk of undesirable events occurring during tunneling with application of a shield tunnel boring machine (TBM) method and conducted a risk analysis which can systematically assess overall risk levels. Deng (2018) [16] summarized the safety risks associated with TBM excavation of the ultra long tunnel of the northern water supply project in Xinjiang Uygur Autonomous Region, and proposed risk prevention and control measures. Sharafat et al. (2021) [17] has proposed a new risk analysis method based on the generic bow-tie method in combination with TBM tunnel engineering, which is used to systematically assess and manage the risks associated with TBM under difficult ground conditions. Vibrations during excavation must be evaluated [18]. Ou et al. (2021) [19] studied the safety risks of tunnel drilling and blasting excavation methods, proposed a new theoretical and technical system evaluation method for tunnel collapse risk control, and applied the method to the Yuxi Tunnel Project. Wu et al. (2020) [20] proposed a new risk assessment model for underwater shield tunnel construction that combines a normal cloud model with an entropy weight method. The numerical models used to assess the risk of tunnel collapse due to uplift must be in unconfined or non-oedometric conditions [21].

Based on the above literature analysis, we find that there are relatively few studies on safety risk management of subway tunnel engineering using mining methods [22]. In the era of rapid development of urban subway construction, it is necessary to conduct in-depth research on the safety risk management of this method [23]. In addition, most studies only focus on a specific construction stage, lacking systematic safety risk analysis for the entire construction process [24].

With the deep integration of research methods and the gradual expansion of application scenarios, Fuzzy Sets Theory (FST) [25] and Bayesian Network (BN) [26] have achieved significant development in the field of risk management. Wu et al. (2015) [27] introduced BN model into subway construction risk management to conduct dynamic safety analysis

for pavement damage caused by subway tunnel construction. Taylan et al. (2014) [28] used the fuzzy analytic hierarchy process and fuzzy TOPSIS method to classify engineering projects and evaluate the overall risk of the project. Wang et al. (2018) [29] took the subway deep foundation pit as the research object, and proposed a multi-source risk fusion analysis model based on T-S fuzzy neural network. Zhou et al. (2020) [30] took urban tunnel sewage pipelines as the research object and proposed a complex sewage pipeline accident risk assessment method based on BN and Dempster-Shafer evidence theory. Rostamabadi et al. (2020) [31] studied the safety production situation in the chemical processing industry and proposed a dynamic risk analysis model based on FST-BN. Mostafa et al. (2020) [32] applied FBN to study the evolution process of hydrogen leakage accidents in gas storage tanks. Zarei et al. (2019) [33] established a system process risk analysis model based on FBN to better solve the uncertainty issues. The typical application and successful demonstration of these studies provide a theoretical basis and method reference for introducing the FBN model into the safety risk assessment of subway tunnel construction using the mine method.

Based on the aforementioned, we aim to identify the primary processes involved in mining method subway tunnel construction through the utilization of the working structure decomposition method, known as the Work Breakdown Structure (WBS). Additionally, the author intends to employ the risk structure decomposition method, namely the Risk Breakdown Structure (RBS), to establish a comprehensive safety risk evaluation index system. This paper proposes a safety risk assessment model based on FBN, which integrates FST, AHP, and BN methods to explain the entire process of mining subway tunnel construction, taking a large cross-section mining method tunnel project as an example to verify the effectiveness and applicability of the model. This study will provide a reference for the safety risk assessment of similar mining subway tunnel construction.

The remainder of the research is organized as follows: Section 2 describes the research variables; Section 3 introduces FST, BN, and model integration characteristics; Section 4 presents the empirical analysis; and Section 5 summarizes the conclusions, innovations, and limitations of the research.

# 2. Construction Safety Risk Evaluation Index 

In order to identify safety risks during the entire construction process, risk identification is carried out by combining WBS-RBS and expert survey methods. After dividing the construction stages through WBS and initially identifying the risk list through RBS, experts finally determine the risk list.

### 2.1. Construction Stage Division

Based on the WBS method, the entire process of subway tunnel construction using the mining method is decomposed step by step in the order of "overall project", "unit project", "divisional and subdivisional project", and "construction process". The entire project is decomposed into manageable sub-projects using a top-down approach. The resulting sub-projects are presented in a WBS tree diagram, allowing for clear visualization of the project structure. The specific breakdown structure is shown in Figure 1.

In Figure 1, subway tunnel construction using the mining method is divided into auxiliary tunnel, tunnel construction and auxiliary construction. The basic work stages are divided into vertical shaft construction, inclined shaft construction, forepoling, surrounding rock excavation, primary lining, structural waterproofing, secondary lining, and auxiliary measures.

![img-0.jpeg](img-0.jpeg)

Figure 1. Work breakdown structure of underground tunnel construction with mining method.

# 2.2. Risk Identification List 

On the basis of dividing the main stages of the whole construction process of underground tunnel with mining method by WBS method, the RBS method can be used to construct the preliminary risk list. The study of relevant literature and consulting experts in the field completes the whole process of the mining method metro tunnel construction safety risk evaluation index system. Safety risk indicators and their connotation are shown in Table 1.

Table 1. Safety risk evaluation index system for subway tunnel construction with mining method.


Table 1. Cont.


Table 1. Cont.


# 3. Methodology 

The mechanism of safety risk in mining subway tunnel construction is uncertain, while the safety risk assessment based on expert experience is fuzzy and subjective. The FBN model introduced in this study combines FST and BN, uses FST to handle the ambiguity and uncertainty of qualitative factors, and models random and imprecise safety risk factor variables based on BN. The above methods are used to accurately analyze and scientifically control the safety risks of mining method subway tunnel construction.

### 3.1. Fuzzy Set Theory

Jardón et al. (2020) [34] introduced FST to describe the fuzzy concept of decision language, represented the inexact values of language terms through fuzzy numbers, and described the uncertainty using the membership function. Given domain $U$, suppose $\widetilde{A}$ is a fuzzy set on $U$. For any $x \in U, \mu_{\widetilde{A}}: \rightarrow[0,1]$ can be determined to indicate the degree to which $x$ belongs to $\widetilde{A}$. The mapping represented by Equation (1) is called the membership function of $\widetilde{A} . \mu_{\widetilde{A}}$ is called the membership of element $x$ in $U$ to fuzzy set $\widetilde{A}$.

$$
\begin{aligned}
\mu_{\widetilde{A}}: & U \rightarrow[0,1] \\
x & \rightarrow \mu_{\widetilde{A}}(x)
\end{aligned}
$$

Fuzzy set $\bar{A}$. is characterized by membership function $\mu_{\bar{A}}$. When $\mu_{\bar{A}}=\{0,1\}, \bar{A}$ is reduced to a general set $A$. The point $x_{0}$ of $\mu_{\bar{A}}=0.5$ is called the transition point of fuzzy set $\bar{A}$, which has the most fuzziness.

There are several common forms of fuzzy numbers, including triangular, trapezoidal and normal [35]. Among them, triangular fuzzy numbers are simple in form, reliable in results and widely used. The Equation is expressed as follows:

$$
\mu_{\bar{A}}(x)= \begin{cases}0, & x \leq m \\ \frac{x-m}{l-m}, & m<x \leq l \\ \frac{n-l}{n-l}, & l \leq x<n \\ 0, & x \geq n\end{cases}
$$

Assuming that $m<1<n$, in the above Equation (2), $m, l$, and $n$ represent the lowest possible value, the most likely value, and the highest possible value, respectively. The triangular fuzzy number can also be represented by the $m, l, n$ parameters as $(m, l, n)$. The membership function is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Membership of triangular fuzzy function.

# 3.2. Bayesian Network 

Bayesian network [36] is a probability model composed of directed acyclic graph (DAG) and conditional probability tables (CPT), which is a powerful tool for expressing uncertain knowledge and conducting knowledge reasoning. In the BN model, CPT is used to represent logical relationships between nodes. As long as the conditional probability ensures the correctness of the judgment direction, the final result will remain within the ideal deviation range.

Assume that $M$ and $E$ are two events, where $P(E)>0$. When $E$ occurs and the conditions are known, the conditional probability of $M$ occurring can be expressed as $P(M \mid E)$. The calculation Equation for $P(M \mid E)$ is:

$$
P(M \mid N)=\frac{P(M) P(N \mid M)}{P(N)}
$$

Assuming that $X_{i}(i=1,2, \ldots, n)$ is a complete event group in sample space $D, n \geq 2$ and $P\left(X_{i}\right)>0$. For the event $M$, there is the following Equation:

$$
P(M)=\sum_{i=1}^{n} P\left(X_{i}\right) P\left(M \mid X_{i}\right)
$$

In the expression of Bayesian total probability Equation, it is assumed that the sample space of random event $S$ is $D$, and $X_{i}(i=1,2, \ldots, n)$ is a complete event group of sample space $D$. Based on this total probability Equation, it can be expressed as follows:

$$
P\left(X_{i} \mid M\right)=\frac{P\left(X_{i}\right) P\left(M \mid X_{i}\right)}{\sum_{i=1}^{n} P\left(X_{i}\right) P\left(M \mid X_{i}\right)}
$$

# 4. Case Analysis 

### 4.1. Case Background

Wuhan's rail transit has developed rapidly in recent years. By the end of 2022, its total mileage ranked fifth among Chinese cities [37]. However, construction of the Wuhan rail transit has problems such as complex geological structure, small construction site, large comprehensive coordination volume and tight construction period, which increases the construction difficulty [22].

This article takes the Wuhan Rail Transit Line 8 Phase II Project as a case study. The project is an important passenger transportation corridor connecting the central urban area of Wuchang with multiple densely populated areas of Wuhan. Among them, the large section of the tunnel section is constructed using the double-sided wall heading method, which divides the large section into six small sections, with a length of 109 m , a width of 20.04 m , and a height of 12.78 m . The area where Wuhan Rail Transit Line 8 Phase II Project is located is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Area of Wuhan Rail Transit Line 8 Phase II Project.

### 4.2. FBN Model Construction

According to the construction safety risk evaluation index system constructed in Table 1, the BN initial model is constructed using NETICA, as shown in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network initial model.
In Figure 4, X1-X26 represents the root event, B1-B6 represents the intermediate event, and T represents the top event. Among them, there are three root event states (S1, S2, and S3), and two intermediate event and top event states (YES, NO). In the BN initial model, the initial probability is displayed when no calculation is performed.

# 4.3. FBN Model Evaluation 

The evaluation of the FBN model encompasses several critical operations, such as expert research and data processing. Fuzzification plays a pivotal role in streamlining the investigation process and alleviating the challenges associated with expert decisionmaking. Resolving ambiguity and normalizing calculations are fundamental prerequisites for establishing accurate prior probability values for node states within the BN model.

### 4.3.1. Fuzzification

In the field of subway construction safety risk management, the judgment ability of experts is an important factor to consider. It is observed that with the accumulation of professional education and work experience, experts' judgment ability tends to become more stable and reliable.

Therefore, in this study, the research focuses on quantifying the judgment ability of experts by considering the reliability of their assessments as a subjective indicator. This approach aims to enhance the objectivity and accuracy of the risk management process in subway construction projects. The subjective and objective attribute indicators and weighting criteria of experts are shown in Table 2.

From Table 2, it can be seen that the objective weights of experts are obtained through background investigation, while the subjective weight needs to be evaluated by experts.

According to the probability interval division theory of Dawes (2008) [38], 5-9 intervals are more suitable for expert evaluation. In this study, 7 linguistic variable intervals are selected. The division of fuzzy probability intervals is shown in Table 3.

Table 2. Expert weight weighting standard.


Table 3. Fuzzy probability interval division.


This study invites experts from four fields: construction units, design units, supervision units, and consulting units. According to the weighting and assignment criteria in Tables 2 and 3, taking root node X1 as an example. The experts weight calculation results are shown in Table 4.

Table 4. Calculation comprehensive weight of X1.


In Table 4, $\omega=\left(\omega_{1}, \omega_{2}, \omega_{3}, \ldots, \omega_{r}\right), \omega$ represents the weighted average of subjective and objective weights, $r$ represents the number of experts. To sum up, the expert assignment and weight calculation results for X1-X26 root events are shown in Table 5.

Combining Tables 4 and 5, the triangular fuzzy probability is expressed as follows:

$$
\widetilde{P}_{i j}=\widetilde{P}_{i j}^{k} \otimes \omega=\left(m_{i j}, l_{i j}, n_{i j}\right)
$$

In the above Equation (6), $i=1,2, \ldots, p, j=1,2, \ldots, q, k=1,2, \ldots, r . p$ is the number of nodes, $q$ is the node status, $r$ represents the number of experts.

Taking the root node X1 as an example, the expert comprehensive weight of X1 is $\omega$. Combining fuzzy probability distribution (FPD), the fuzzy probability value (FPV) is calculated from Equation (6). The results are shown in Table 6.

Table 5. Root event expert weight calculation.

(E1,E2,E3,E4) |  |   |

Table 6. Calculation fuzzy probability value of X 1 .


To simplify the evaluation without losing generality, this study directly gives the conditional probability values of intermediate nodes through the expert evaluation, as shown in Table 7.

Table 7. Conditional probability value of intermediate node (part).


The conditional probability evaluated by experts in this study ensures the correctness of the judgment direction. It not only meets the basic research needs, but also provides convenience for the rapid generation of conditional probabilities with more complex relationships and data.

# 4.3.2. Defuzzification 

In the defuzzification process, the maximum average method, center of gravity method, maximum center method, and specific sorting method are most commonly used [35]. Through the research, it has been found that the specific sorting method offers several advantages, such as minimal information loss and high reliability of results, when compared to other algorithms [39,40]. The specific sorting method selected for this study is shown in Equation (7):

$$
\operatorname{VAL}\left(\widetilde{P}_{j}\right)=\frac{m_{j}+2 l_{j}+n_{j}}{4}
$$

In the above Equation (7), $\operatorname{VAL}\left(\widetilde{P}_{j}\right)$ is the solution fuzzy value of $\widetilde{P}_{j}$ in the $j$ state. $m_{j}$, $l_{j}$, and $n_{j}$ are the minimum possible value, the middle possible value, and the maximum possible value of the triangular fuzzy number in the $j$ state, respectively.

### 4.3.3. Normalization

In the FBN model, the sum of the probabilities of each state of an event is 1 , and it is necessary to normalize the defuzzification probability values of nodes in each state based on defuzzification, as shown in Equation (8):

$$
P_{i j}=\frac{V A L\left(\widetilde{P}_{i j}\right)}{\sum_{j=1}^{S} V A L\left(\widetilde{P}_{i j}\right)}
$$

In the above Equation (8), $S=3, j=1,2,3 . P_{i j}$ is the clear probability value of event $i$ under state $j . \operatorname{VAL}\left(\widetilde{P}_{i j}\right)$ is the fuzzy value of event $i$ in state $j$.

Based on Equations (6)-(8), the evaluation results of four experts were fuzzed, defuzzified, and normalized. The calculation results of the Crisp Probability Value (CPV) under

different states of each event are shown in Table 8. Similarly, we can determine the edge probability value or conditional probability value of each node in the FBN.

Table 8. Root event crisp probability value calculation.


# 4.4. FBN Model Interpretation 

### 4.4.1. Causal Reasoning

In the FBN model, causal reasoning is a reasoning process that draws conclusions based on known causes. The principle is to calculate the occurrence probability of the result using the cause probability value. Using NETICA for causal reasoning, it was calculated that $\mathrm{P}(\mathrm{T}=\mathrm{YES})=9.83 \%$. The results are shown in Figure 5.

Generally speaking, small probability events refer to events whose probability of occurrence is less than $5 \%$. The analysis in Figure 5 shows that under the background of known prior probabilities, the reasoning result in this case is greater than $5 \%$, and there is a greater possibility of safety risk accidents. Therefore, decision makers can refer to the limited posterior knowledge obtained from causal reasoning to conduct overall safety status assessment and preliminary judgment on safety risk influencing factors. So as to strengthen the patrol inspection strength during the safety risk accident-prone period on-site.

### 4.4.2. Diagnostic Reasoning

In the FBN model, diagnostic reasoning is a reasoning process from results to causes, which calculates the occurrence probability value of each root event based on the known occurrence probability of the top event. Under the condition of $\mathrm{P}(\mathrm{T}=\mathrm{YES})=100 \%$, NETICA is used to calculate the posterior probability of the basic event. The results of prior probability and posterior probability are shown in Table 9 and the posterior probability is shown in Figure 6.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** Causal reasoning calculation model.

**Table 9.** Prior probability and posterior probability under the condition of P(T = YES) = 100%.


![img-5.jpeg](img-5.jpeg)

Figure 6. Initial diagnostic inference under the condition of $\mathrm{P}(\mathrm{T}=\mathrm{YES})=100 \%$.
The analysis in Table 9 and Figure 6 shows that the posterior probability of X6, X19, X20, X25, and X26 safety risk factors exceeds $20 \%$ in the S1 (severe) state. These risk factors are likely to be the direct cause of safety accidents. Therefore, all parties involved in the construction should focus on risk assessment and safety control of these factors.

At the same time, when the posterior probability of the basic event is known, FBN diagnostic inference can be used to reverse infer and analyze the accident. The second round of risk diagnosis is carried out by diagnosing and determining the cause of the accident in real time and using this as new evidence. Through research, we found that the risk diagnosis is a real-time dynamic and step-by-step implementation process because new risks may be generated in the process of risk diagnosis.

In the FBN model, we have input the parameters with adjusted probability values for X6, X19, X20, X25, and X26 (probability values are $0 \%$ in S1 and S2 states, and $100 \%$ in S3 states), and under other unchanged conditions, we obtain $\mathrm{P}(\mathrm{T}=\mathrm{YES})=4.27 \%$. The results of prior probability and posterior probability are shown in Table 10, The posterior probability is shown in Figure 7.

The analysis in Table 10 and Figure 7 shows that the project is now in a safe state. The FBN model is used for repeated diagnostic reasoning, so as to form an investigation path dominated by important risk factors and reduce the blindness of risk diagnosis. This study can implement multiple rounds of risk diagnosis for the detection path, and integrate normalized risk diagnosis and safety warnings throughout the entire construction process.

Table 10. Prior probability and posterior probability under new conditions.


![img-6.jpeg](img-6.jpeg)

Figure 7. Secondary diagnostic reasoning under new conditions.

# 5. Conclusions 

This paper takes the safety risk management of the whole process of mining method subway tunnel construction as the research object, and establishes a safety risk assessment model for mining method subway tunnel construction based on FBN. The assessment was conducted on the mining method tunnel project of Wuhan Rail Transit Line 8 using this method, and the research conclusions can be summarized into the following three points.
(1) Using WBS-RBS and expert survey methods, an initial safety risk list for subway tunnel construction using mining methods was summarized through consulting experts in the field. Based on this, an index system for safety risk assessment of the entire process of mining method subway tunnel construction is established.
(2) Combining Fuzzy Set Theory (FST), Analytic Hierarchy Process (AHP), and Bayesian Network (BN), a safety risk assessment model for mining method subway tunnel construction based on FBN was constructed. The model was empirically analyzed through the collection of construction site data in the mining method tunnel project of Wuhan Rail Transit Line 8.
(3) During the construction of subway tunnels using the mining method, reasonable excavation methods should be selected. For construction managers, they should pay close attention to the waterproof construction quality of the main body, attach importance to the waterproof construction quality of the detailed structure, formulate reasonable monitoring and measurement plans, ensure the monitoring and measurement results and strengthen geological advance prediction. At the same time, multiple rounds of risk diagnosis should be carried out, and regular on-site safety inspection and early warning should be done according to the risk detection path.

Author Contributions: Conceptualization, Q.W., K.Z., P.G. and C.S.; Methodology, J.Z., K.Z., P.G., C.S. and Z.X.; Software, J.Z., K.Z., P.G., C.S. and Z.X.; Validation, K.Z., P.G. and C.S.; Formal analysis, J.Z., K.Z., P.G., C.S. and Z.X.; Investigation, P.G.; Resources, J.Z. and P.G.; Data curation, J.Z., K.Z., P.G. and Z.X.; Writing—original draft, J.Z., K.Z. and P.G.; Writing—review \& editing, Q.W., J.Z., K.Z. and P.G.; Visualization, Q.W., K.Z. and P.G.; Supervision, Q.W.; Project administration, Q.W.; Funding acquisition, Q.W. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by Hainan Province Major Science and Technology Plan Project, grant number ZDKJ2021024, The PhD Scientific Research and Innovation Foundation of Sanya Yazhou Bay Science and Technology City, grant number HSPHDSRF-2022-03-001, The PhD Scientific Research and Innovation Foundation of Sanya Yazhou Bay Science and Technology City, grant number HSPHDSRF-2022-03-002, The PhD Scientific Research and Innovation Foundation of Sanya Yazhou Bay Science and Technology City, grant number HSPHDSRF-2023-03-001.

Conflicts of Interest: The authors declare no conflict of interest.
