# Article 

## Research on the Application of Fuzzy Bayesian Network in Risk Assessment of Catenary Construction

Yongjun Chen ${ }^{1}$, Xiaojian Li ${ }^{1}$ (D), Jin Wang ${ }^{2,3,4, *}$, Mei Liu ${ }^{1 *}$, Chaoxun Cai ${ }^{5,6}$ and Yuefeng Shi ${ }^{5,6}$

## check for updates

Citation: Chen, Y.; Li, X.; Wang, J.; Liu, M.; Cai, C.; Shi, Y. Research on the Application of Fuzzy Bayesian Network in Risk Assessment of Catenary Construction. Mathematics 2023, 11, 1719. https://doi.org/ 10.3390/math11071719

Academic Editor: Manuel Alberto M. Ferreira

Received: 13 March 2023
Revised: 28 March 2023
Accepted: 31 March 2023
Published: 3 April 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Urban Economics and Management, Beijing University of Civil Engineering and Architecture, Beijing 102616, China
2 School of Civil Engineering, Central South University, Changsha 410075, China
3 MOE Key Laboratory of Engineering Structures of Heavy-Haul Railway, Central South University, Changsha 410075, China
4 Center for Railway Infrastructure Smart Monitoring and Management, Central South University, Changsha 410075, China
5 State Key Laboratory for Track Technology of High-Speed Railway, China Academy of Railway Sciences Corporation Limited, Beijing 100081, China
6 Railway Engineering Research Institute, China Academy of Railway Sciences Corporation Limited, Beijing 100081, China

* Correspondence: 22020163@csu.edu.cn

Abstract: The research on risk control during the construction stage of catenary is relatively limited. Based on a comprehensive analysis of the risk factors during catenary construction, this study determined the causal relationships between the risk factors and established a risk assessment model for catenary construction that analyzed the risks from a causal logic perspective. During the evaluation process, we identified six exogenous variables and twenty-one endogenous variables for risk factors in the construction of catenary based on a literature review in the field of catenary construction and expert opinions, described the cause-and-effect relationships between variables using structural equations and causal diagrams, and established a multi-level catenary construction risks structural causal model. Based on expert fuzzy evaluation and expert experience, the occurrence probability of exogenous variables and the conditional probability of endogenous variables were determined, respectively. Then, the risk assessment model of catenary construction stage based on fuzzy Bayesian Network was constructed to analyze the risk of catenary construction process. The results showed that the personal quality of the construction personnel and the sense of responsibility of the supervision unit had a great impact on the risk level of catenary construction. The findings can help construction personnel fully consider various weak points in catenary construction, thereby ensuring efficient and high-quality catenary construction.

Keywords: catenary; fuzzy number; Bayesian Network; structural causal model; risk assessment
MSC: 62F15; 03B52

## 1. Introduction

Catenary is the main framework of the railway electrification projects, and it is a special form of transmission line erected along the railway line to supply power to electric locomotives [1,2]. Investigations showed that most faults of the traction power supply system originate from catenary [3]. However, as the core of the traction power supply system, catenary poses many challenges during its construction phase, including complex business processes and numerous factors that can impact its quality and safety. Therefore, comprehensively assess the risk of catenary construction, build a scientific, systematic and normative risk assessment model for these factors, and then, identify the weak links and key nodes that affect the construction phase of catenary, and formulating feasible economic and technological risk prevention and response plans. This can prevent and reduce

the occurrence of accidents and incidents and avoid additional costs and delays caused by risks.

As the power source of electrified railways, scholars in relevant fields conducted multilevel research on the risks associated with catenary system. Firstly, as a linear power supply project exposed to the natural environment, Wang et al. [4], Xie et al. [5], Dour et al. [6], Wu et al. [7], Panteli et al. [8], Guo et al. [9], Ma et al. [10], Yum et al. [11], and Chen et al. [12] established risk assessment models or developed fault detection methods, respectively, to study the operation and maintenance reliability of catenary and power supply system during natural disasters (such as earthquake, lightning strikes, and pollution) and harsh environments (such as typhoon, heavy rain, ice and snow, and thick fog). For the risk analysis of individual components or single fault level of catenary, Chen et al. [13] applied the deep-learning method to fault detection of the current-carrying ring of catenary system. They proposed a fault diagnosis method based on the improved CenterNet model. Through example verification, the proposed method improved the accuracy of fault diagnosis for the current-carrying ring, with higher accuracy and recall values. This provides useful help to improve the efficiency and stability of railway transportation. Ding et al. [14] analyzed the characteristics and causes of trip risks in the operation and maintenance process of catenary systems, and proposed a high-speed railway catenary risk index system that considers the characteristics of time-space difference. Based on the travel data of catenary system, an example verification revealed relevant information about the time-space difference of trip risks in catenary system, reflecting the impact of external environmental factors, and highlighting the disaster prevention and resilience of catenary system. This study is useful for comprehensively studying the operation and maintenance of catenary systems. Ding et al. [15] proposed a risk assessment method for catenary operation and maintenance under complex geographical and meteorological conditions. They evaluated the cumulative risk of catenary failure quantitatively and visualized the risk using geographic information system (GIS) technology. Chen et al. [16] and Song et al. [17] established a finite element model for the pantograph and catenary, and evaluated the interaction system's reliability considering material wear and local suspender defects. Therefore, experts in catenary risk assessment focused on the reliability analysis of the operation and maintenance process and measures to respond to operation and maintenance risks and disasters. However, research on risks and causal relationships during catenary construction phase is relatively limited. However, construction plays a crucial role in ensuring quality throughout the entire life cycle of catenary [3]. By studying the causal logic relationship between risk factors that affect the construction of catenary, and quantifying risk characteristics, it can provide decision-making and theoretical support to catenary construction project managers. This can promote standardized and streamlined project management, improve project quality and efficiency, and ultimately enhance the project's competitiveness.

Since the 20th century, the research on causality rapidly developed. Statisticians discussed various issues related to causality in statistical analysis, and research in this area became more profound, showing diversified development in various disciplines. In terms of the theoretical research level of risk and reliability assessment, Yule [18] first emphasized the difference between correlation and causality in 1900. Later, in 1961, Bell Labs [19] proposed the fault tree analysis (FTA) method to predict the failure probability of event operation, and Pearl [20] proposed the Bayesian Network (BN) theory to quantify the risk characteristics in 1985. With the deepening of theoretical research, Pearl [21] developed a formal theory of causal inference based on causal directed acyclic graph, providing a new direction for the research and application of causal inference. The fundamental theoretical research became increasingly rich, and researchers in various disciplines expanded and applied the above theoretical methods to the risk assessment of system operation. For example, Gao et al. [22] proposed a catenary operation and maintenance risk assessment model based on a multi-layer Bayesian Network to study the transmission law of catenary risk and comprehensively analyzing the weather accumulation risk of catenary from the time and space perspective; Chen et al. [23] obtained the fault rate function of catenary

components and substation equipment through field fault records. They developed the fault tree models of catenary system and traction substation to analyze the weak links of the system and guide maintenance decisions. Wang et al. [24] proposed a data-driven integrated risk analysis framework based on dynamic Bayesian networks to identify important risk factors in the dynamic risk propagation network of catenary and analyze their failure modes over time. This approach achieved dynamic modeling and analysis of operational risks in catenary. However, the above research methods were relatively weak in describing the causal reasoning logic between factors and could not directly infer a causal relationship from the structure, because the network nodes in Bayesian networks were related, but no causal relationship was found [25]. Therefore, Pearl [26,27] proposed a structural causal model (SCM) to explore the causal relationship between risk factors, which clearly described the logical implication between risk factors with structural equations and causal diagrams.

Although current research provided systematic assessments of the operation and maintenance risks of catenary system and outlined the development and application of causal reasoning in system reliability and risk assessment, there remain issues that require further refinement and in-depth study.

- The existing risk assessment for catenary system is mainly focused on the operational and maintenance stage, neglecting the risk evaluation during the construction phase. However, the quality of the construction of catenary can have a significant impact on the normal operation and maintenance during the operational stage.
- The current methods or models for assessing system risk have limited abilities in reasoning about the causal relationships between risk factors and the expression of these causal relationships is relatively simplistic.
- Currently, there is a lack of emphasis on developing targeted control measures for the construction risks of catenary, which results in ineffective and imprecise risk control.
Considering the lack of risk assessment in catenary construction, it is necessary to review and enhance the safety measures of this process. Therefore, this paper comprehensively evaluates the risks of catenary construction from the perspective of causal reasoning. In Section 2, we mainly introduce information about the sources, types, names, and explanations of risk factors related to the construction of catenary. Based on the literature and expert consultation in the field of catenary construction, this study summarizes the risk factors in catenary construction process from three dimensions, including: construction stage, participating departments, and construction elements. In Section 3, we provide a detailed introduction of our research methodology, which includes the establishment of a structural causal model and the construction and analytical applications of a fuzzy Bayesian network model. In Section 4, we conduct a detailed analysis of the risk factors related to the construction of catenary discussed in Section 2, based on the methodology presented in Section 3. Section 4 establishes a structural causal model of catenary construction risks, and the causal logic relationship between risk factors is analyzed and described using structural equations and causal diagrams. To quantify the risk of catenary construction, we utilized a combination of expert evaluations and fuzzy logic to calculate the probability of exogenous variables and determine the conditional probability of endogenous variables based on expert knowledge. A catenary fuzzy Bayesian network model was constructed to analyze the risk level and key risk factors in the construction process. Finally, we formulate risk prevention and control measures to address the weak links in catenary construction process, thereby reducing the probability and impact of risks and ensuring the timely delivery of catenary projects and efficient operation and maintenance. The discussion and conclusions are given in Section 5.


# 2. Analysis on Risk Factors of Catenary Failures 

As the key carrier for transmitting the required electrical energy to trains, catenary is mainly composed of contact suspension, support devices, positioning devices, pillars, and foundations [28]. The construction process of catenary involves three stages: construction

preparation, construction, and completion and acceptance [29]. Each construction stage has strict rules and regulations, as well as specific engineering procedures. In this study, the construction phase of catenary was divided into the pre-assembly stage and the installation stage. The pre-assembly stage includes assembling and alignment of the pillars, as well as pre-assembly of catenary arm structure and the installation stage includes installation of compensation devices, erection of supporting cable racks, and installation of hangers [30].

The risk factors in the construction process of catenary can be divided into two types: exogenous variables and endogenous variables. Exogenous variables are independent of other variables in the system and remain unaffected by any changes in other variables [31]. In contrast, endogenous variables can be determined or influenced by other variables in the system [32]. The entire process of catenary construction is affected by both internal and external factors. Ignoring the influence of these risk factors will seriously affect the construction quality and delivery schedule of catenary projects, which will create hidden dangers for the safe operation of railroad projects and increase the project maintenance costs. Based on the relevant domestic and foreign literature, this study investigated the risk factors of catenary construction process from the perspectives of construction phase, participating departments and construction elements. By summing up the expert experience, we systematically analyzed the organizations, processes, and methods involved in quality and safety management in the railroad catenary construction process, and established catenary construction process risk research model, which serves as the basis for risk identification, assessment, and control.

During the construction process of catenary, natural environmental factors such as weather and geology, as well as behavioral factors such as design, construction, supervision, and regulation, will have an impact. After consulting with experts and reviewing the literature [33,34,35,36,37,38,39,40], risk factors in the construction process of catenary were summarized, including six external variables and twenty-one internal variables. According to the time of risk occurrence, catenary construction risks were divided into four stages. The specific variable names, symbols, variable definitions, and risk stage divisions are shown in Tables 1-3.

Table 1. Exogenous variables of catenary construction risks.


Table 2. Endogenous variables of catenary construction risks.


Table 2. Cont.


Table 3. Risk stage division of catenary construction.


# 3. Materials and Methods 

In this paper, we developed a risk assessment model for catenary construction by combining the structural causal model and fuzzy Bayesian network (FBN), which can provide quantitative assessment for catenary construction risk based on expert experience and basic theoretical knowledge. Firstly, we identified the risk factors in catenary construction process by means of expert consultation and literature analysis, described the causal logic relationship between the risk factors of catenary construction in the form of structural equation and causal diagram, and mapped it to Bayesian network model. Then, the probability of occurrence of exogenous variables for catenary construction risks was calculated using expert fuzzy evaluation, and the conditional probability of endogenous variables was determined by referring to the experience of previous engineering and professional personnel. Finally, the solution for the fuzzy Bayesian network of catenary construction risks was completed. Next, we calculated the level of risk in the catenary construction process and further analyzed the critical influencing factors. A flow chart of risk assessment of catenary construction is established in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. A flow chart of risk assessment during catenary construction.

# 3.1. Overview of the Structural Causal Model 

The structural causal model is a conceptual model that describes the causal mechanism of a system. It uses precise rules to determine the variables that need to be considered or controlled, and provides detailed descriptions of the roles of these variables as well as the internal causal relationships between them [41]. The structural causal model is composed of structural equation and causal diagram [42], so we can define a structural causal model $M$, its structural equation is an ordered triplet $\langle U, V, F\rangle$, which can be expressed by Equation (1):

$$
F=\left\{f_{i}: X \rightarrow Y \mid Y \epsilon V, X \subseteq(U \cup V)\right\}
$$

where $U$ can be defined as a set of external variables; $V$ is a set of internal variables, that is, the variables that can be determined by external variables; $F$ represents the set of structural equations of the relationship between the above variables.

To clearly illustrate the causal logic relationship between factor variables in the system operation process, we can describe it by drawing the causal diagram [43]. In the theoretical system of the structural causal model, the inference of causal relationship depends on the three basic path structures of the directed acyclic graph (DAG): the chain structure, the fork structure, and the collision structure [44]. These three structures have different mathematical information transmission methods, and the causal diagram can be composed of these basic structures. By comprehensively analyzing the structural equation, we can extract all causal paths between factor variables and deduce the causal relationship between the factor variables during system operation. Then, we can draw a causal diagram to describe the causal relationship between factor variables. The causal network diagram connects risk nodes that have a causal relationship with directed edges, and the logical accuracy of the causal diagram is ensured by graphic drawing rules. These rules are as follows [45]:

- Each endogenous variable in the figure is the offspring of at least one exogenous variable;
- Exogenous variables are represented as root nodes in the diagram. They have no parent nodes and cannot be the child nodes of endogenous variables.


### 3.2. Construct a Fuzzy Bayesian Network Risk Assessment Model

### 3.2.1. Overview of Bayesian Network

Bayesian networks, also known as belief networks, are directed acyclic graphs that represent causal relationships between variables [46]. A Bayesian network is composed of a graph structure and conditional probability tables (CPT) [47]. The graph structure is a directed acyclic graph composed of nodes and directed edges. The nodes represent random variables, and the directed edges represent the causal relationships between the nodes [48]. The conditional probability table reflects the strength of causality between exogenous variables and endogenous variables, and the probability of occurrence of the variables, which is called the prior probability [49,50]. The Bayesian network structure is established by nodes and directed edges, and the mathematical meaning of the Bayesian network is given by the conditional probability table. This allows the Bayesian network model to qualitatively and quantitatively solve practical problems. Equation (2) expresses this relationship.

$$
R_{B N}=\left\langle X_{i}, P\right\rangle
$$

where $R_{B N}$ denotes the Bayesian network structure, $P$ is the set of directed edges, $X_{i}$ is the set of all nodes in the network.

The Bayesian network structure is known to contain the assumption of conditional independence, i.e., each node is independent of the nodes that are not its descendants under the condition that the parent node is known, and the expression of the conditional independence assumption is Equation (3):

$$
P\left(X_{i} \mid X_{j}, X_{n}\right)=P\left(X_{i} \mid X_{j}\right)
$$

where $X_{j}$ denotes the parent node of $X_{i}, P\left(X_{j}\right)$ represents the probability of occurrence of parent node events, $X_{n}$ represents the set of non- $X_{i}$ set of child nodes.

# 3.2.2. Solution for the Occurrence Probability of the Exogenous Variables 

In fuzzy set theory [51,52], give a universe $U$, for whatever $x \in U$, there is a corresponding $F(x) \in[0,1]$, where $F(x)$ is the membership for $x$ to $U, F$ is the membership function of $x$. In this paper, triangular fuzzy numbers are used to express the probability of occurrence of the bottom event, which is represented by $F=(a, b, c)$.

At the same time, if any $\lambda \in[0,1], F_{\lambda}=\{x \mid x \in R, F \geq \lambda\}=\left[a^{\lambda}, c^{\lambda}\right], F_{\lambda}$ is the $\lambda$ cut set of $F$, so, trigonometric ambiguity function can be expressed by Formula (4):

$$
F_{\lambda}=\left[a^{\lambda}, c^{\lambda}\right]=[(b-a) \lambda+a,(b-c) \lambda+c]
$$

The introduction of fuzzy theory can reduce the subjectivity of the expert evaluation process, improve the reliability of the calculation results, and avoid the judgment of important risk nodes due to the small difference in the risk evaluation results [53]. We can use triangular fuzzy numbers and $\lambda$ cut set to synthesize the risk state grade evaluation given by different experts, calculate the fuzzy number of the risk, and determine the prior probability of the root node of the Bayesian network. The seven-level natural language variables were introduced to make a fuzzy evaluation, including: very Low ( $V L$ ), low ( $L$ ), few low (FL), medium $(M)$, few high $(F H)$, high $(H)$, and very high $(V H)$ [54]. The corresponding triangular fuzzy numbers and $\lambda$ cut sets are shown in Table 4. The membership functions of natural language variables and triangular fuzzy numbers are shown in Figure 2.

Table 4. The corresponding relationship between natural language variables of grade 7 and triangular fuzzy numbers.


![img-1.jpeg](img-1.jpeg)

Figure 2. Membership functions of natural language variables of grade 7 and triangular fuzzy number.

Since the qualification level, work experience, and education experience of the invited experts have an impact on the consistency and accuracy of the evaluation results [55], it is necessary to calculate the weight vector $K$ of each expert. Referring to the relevant literature [45,56], the qualification scores of the experts were determined as shown in Table 5.

Table 5. Demographics of the respondents.


The calculation steps of expert weight and evaluation results were as follows:

1. Add the scores of the three items of expert's qualification level, work experience and education experience, and the evaluation weight of expert $i$ is:

$$
m_{i}=\frac{L_{i}^{q}+W_{i}^{e}+E_{i}^{e}}{\sum_{j=1}^{n}\left(L_{i}^{q}+W_{i}^{e}+E_{i}^{e}\right)}, i=1,2, \cdots, n
$$

where $L_{i}^{q}$ indicates the score of experts' qualification level; $W_{i}^{e}$ indicates the expert's work experience score; $E_{i}^{e}$ indicates the score of experts' education experience.
2. The expert's weight vector is:

$$
K=\left[m_{1}, m_{2}, \cdots, m_{n}\right]
$$

where $m_{n}$ represents the weight of the $n$th experts.
3. Let the triangular fuzzy evaluation of the occurrence probability of exogenous variables by experts be:

$$
A_{i}=\left(a_{i}, b_{i}, c_{i}\right)
$$

4. The triangle fuzzy number of the probability of risk event weighted by the expert weight is:

$$
\widetilde{A_{i}}=\frac{\sum_{i=1}^{n} m_{i} A_{i}}{n}=\left(\widetilde{a_{i}}, \widetilde{b_{i}}, \widetilde{c_{i}}\right)
$$

5. The probability value of calculating the fuzzy set is:

$$
P_{i}=\frac{\widetilde{a_{i}}+2 \widetilde{b_{i}}+\widetilde{c_{i}}}{4}
$$

6. Normalize the probability values of nodes in different states, obtain the probability of occurrence of node:

$$
\widetilde{P}_{i}=\frac{P_{i}}{\sum_{i=1}^{h} P_{i}}
$$

where $h$ represents the number of risk node states;

# 3.2.3. Solution for the Bayesian Network Model 

The Bayesian network parameter learning refers to the process of determining the conditional probability table and specific parameters of different nodes in the model using actual data and professional experience [57,58]. The two common methods of parameter learning are maximum likelihood estimation and Bayesian statistical method. Maximum likelihood estimation method identifies parameters as fixed variables, and its solution is not influenced by prior knowledge and experience [59]. On the other hand, Bayesian statistical method treats the parameters to be solved as random variables, which allows incorporating previous experience and theoretical knowledge [60]. Since analyzing the system risk involves drawing heavily from previous engineering experience and professional knowledge, the Bayesian network adopts the Bayesian statistical method for parameter learning. The process of solving the Bayesian statistical model can be described as follows.

A typical example of a Bayesian network is shown in Figure 3. Specifically, we can focus on analyzing one of the fork nodes. Let us assume that $X_{1}$ and $X_{2}$ are the two main risk factors that affect the quality and safety of the system operation. According to the logical relationships shown in Figure 3, $X_{1}$ and $X_{2}$ are the parent nodes of $Z$, which is the child node that represents the occurrence of system risk.
![img-2.jpeg](img-2.jpeg)

Figure 3. Description diagram of node relationship.
In order to simulate the calculation process of the probability of child node $Z$ occurrence clearly, we assumed that the probability of risk factors $X_{1}$ and $X_{2}$ occurring in the system was determined to be 0.12 and 0.10 , respectively. However, if we only rely on the occurrence probability of two risk factors, we are unable to perform the calculation, because the quality and safety risks of system are usually caused by many factors; therefore, it is necessary to determine the joint probability of risk factors $X_{1}$ and $X_{2}$, that is, determine the conditional probability table of node $Z$. This step generally uses the actual survey data for parameter learning and was improved through expert discussion. The conditional probability of node $Z$ is shown in Table 6.

Table 6. Conditional probability of node $Z$.


On the basis of determining the conditional probability table in Table 6, the occurrence probability of node $Z$ can be calculated by using Bayesian theorem, that is:

$$
\begin{gathered}
P(Z=Y)=P(Z=Y \mid A=Y, B=Y) * P(A=Y) * P(B=Y)+P(Z=Y \mid A=Y, B=N) \\
* P(A=Y) * P(B=N)+P(Z=Y \mid A=N, B=Y) * P(A=N) * P(B=Y)+ \\
P(Z=Y \mid A=N, B=N) * P(A=N) * P(B=N) 0.126
\end{gathered}
$$

Since $Z$ is a binary event, the occurrence probability of node $Z$ does not occur is:

$$
P(Z=N)=1-P(Z=Y)=0.874
$$

# 3.3. Risk Assessment of Catenary Construction 

### 3.3.1. Forward Reasoning

The forward reasoning of the risk network is based on the information of the cause node, and the reasoning calculation is carried out on the network node relationship to obtain the conditional probability table of the risk index node. Assume the variable to be solved be $X$, each state is $k$, and the forward reasoning formula of variable aggregation $\left[X_{1}, \cdots, X_{j-1}, X_{j+1}, \cdots, X_{n}\right]$ is as follows:

$$
P\left(X_{j}=x_{j}^{k}\right)=\sum_{x_{i}-x_{j}^{k}} \sum_{i=1}^{n} P\left(x_{i} \mid \pi\left(x_{i}\right)\right)
$$

### 3.3.2. Importance Analysis

Bayesian network analysis is to calculate the occurrence probability of the top event from the prior probability of the root node as the occurrence probability of the bottom event. Posteriori probability refers to the probability of re-correction after the occurrence of the assumed top event "system operation risk". The calculation of the posterior probability of the bottom event is based on the prior probability, and so, it is not completely reliable to take the posterior probability of the root node as a single quantitative standard for analysis. This paper comprehensively compares the probability importance degree and the critical importance degree to reflect the importance degree of accidents caused by the root node, and verifies the reliability of the posterior probability. Among them, the probability importance refers to the change value of the top event occurrence probability caused by the unit change of the bottom event occurrence probability. Critical importance refers to the ratio of the change rate of the occurrence probability of the top event to the change rate of the occurrence probability of the bottom event. The posterior probability was obtained from the prior probability and likelihood function according to the Bayesian formula. The Bayesian formula is:

$$
P\left(X_{i}=\mathrm{Y} \mid T=\mathrm{Y}\right)=\frac{P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{Y}\right) P\left(X_{i}\right)}{\sum_{i=1}^{n}\left[P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{Y}\right) P\left(X_{i}\right)\right]}
$$

where $X_{i}$ is bottom event and is binary event, when $X_{i}$ occurs, $X_{i}=\mathrm{Y}$, or $X_{i}=\mathrm{N} ; T$ is Top Event; $P\left(X_{i}\right)$ is the priori probability of the Bottom Event $X_{i} ; P(T=\mathrm{Y} \mid)$ is the conditional probability of the Top Event.

The equation for calculating the probability importance of Bayesian network is:

$$
I_{t}^{p i}=P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{Y}\right)-P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{N}\right)
$$

The calculation equation of critical importance is:

$$
I_{t}^{c i}=\frac{P\left(X_{i}=\mathrm{Y}\right)\left[P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{Y}\right)-P\left(T=\mathrm{Y} \mid X_{i}=\mathrm{N}\right)\right]}{P(T=\mathrm{Y})}
$$

# 4. Results 

### 4.1. Establish Structural Causal Model of Catenary Construction Risks

In this paper, we analyzed the risks associated with catenary construction process in Section 2 and identified six exogenous variables and twenty-one endogenous variables. By incorporating this analysis with a discussion on the application of the structural causal model in causal logic reasoning (as discussed in Section 3.1), we can establish the structural causal model for the risk factors of catenary construction, and describe the causal relationship between the risk factors of catenary construction in structural equation and causal diagram.

Based on the causal logic relationship between the exogenous and endogenous variables expressed in Equation (1), we assumed that $\left(I=\left\{C_{1}, C_{2}, \ldots, C_{n}\right\}\right.$ was the exogenous variables of the risk factors in catenary construction process, while $V=\left\{B_{1}, B_{2}, \ldots, B_{j}\right\}$ was the endogenous variables of risk factors. Thus, there exists a functional formula $f_{i}$ that can describe the causal logic relationship between the exogenous and endogenous variables of the risk factors in the catenary construction, and the set of the functional formula was $F=\left\{f_{1}, f_{2},, \ldots, f_{i}\right\}$. Based on the above setting of the variable set of risk factors in the catenary construction process, we can establish the structural equation of causal relationship among risk factors through causal reasoning.

On the basis of fully understanding the business process of catenary construction, we consulted experts in the field of railway construction, and analyzed the causal relationship between the six exogenous variables and twenty-one endogenous variables in this study based on causal theory [56]. Specifically, the behavior $X$ leads to the result $G$, which can be represented using the structural equation $G=f(X)$.

For example, according to the description of variables in Tables 1-3, we can derive the functional equation mapping relationship between exogenous and endogenous variables of risk factors in the catenary construction process. Specifically, since $C_{1}$ (the drawings are not communicated in time) can lead to $B_{1}$ (the drawings are not qualified) used in construction. The causal relationship between the risk factors can be expressed by structural equation, namely:

$$
B_{1}=f_{1}\left(C_{1}\right)
$$

Similarly, it can be reasoned that due to $C_{5}$ (poor reputation of the unit that won the tender for the materials) and the $B_{11}$ (failure of the physical and mechanical department that performs the quality inspection of incoming materials) can lead to $B_{10}$ (failure of the quality of the material) used in construction. So, the causal relationship between the risk factors is expressed in a structural equation, namely:

$$
B_{10}=f_{7}\left(C_{5}, B_{11}\right)
$$

Based on the analysis of the above examples and a thorough examination of the causal relationships between risk factors in catenary construction process, we ] deduced the causal equation that connects these variables. Consequently, we can obtain the complete structural

equation that describes the causal relationships within catenary construction process, as shown in Equation (19):

$$
\left\{\begin{array}{c}
B_{1}=f_{1}\left(C_{1}\right) \\
B_{4}=f_{4}\left(C_{4}\right) \\
\vdots \\
B_{10}=f_{7}\left(C_{5}, B_{11}\right) \\
B_{6}=f_{2}\left(C_{2}, B_{3}\right) \\
\vdots \\
B_{19}=f_{9}\left(C_{6}, B_{10}, B_{15}\right) \\
B_{18}=f_{10}\left(C_{6}, B_{10}, B_{15}\right) \\
\vdots \\
A_{3}=f_{24}\left(B_{15}, B_{17}\right) \\
A_{4}=f_{25}\left(B_{20}, B_{21}\right)
\end{array}\right.
$$

where $f_{1 \ldots 25}$ denotes the mapping of the logical relationship from cause to effect among the risk factors of catenary construction process, $C_{1 \ldots 6}$ denotes the exogenous variables of the risk factors of catenary construction process, and $B_{1 \ldots 21}$ denotes the endogenous variables of the risk factors of catenary construction process. $A_{1 \ldots 4}$ denotes the four stages of catenary construction risks divided by project type.

According to the settings and interpretations of exogenous and endogenous variables in Section 2, and with reference to the structural equation expression (19) of the causal relationships between risk factors in the catenary construction process, the three basic path structures of the directed acyclic diagram can be used to establish a multi-level (including exogenous variable layer, endogenous variable layer, stage risk layer) causal diagram of risk factors in the construction of catenary, as shown in Figure 4, which can emphasize the hierarchical logical relationship between risk factors.
![img-3.jpeg](img-3.jpeg)

Figure 4. Causal diagram of risk factors for catenary construction.

4.2. Calculate the Occurrence Probability of Exogenous Variables for Catenary Construction Risks

In order to verify the effectiveness of catenary construction risks assessment framework proposed in this paper, five experts in the field of high-speed railway construction were invited to make assessment and judgment. The specific process was as follows:

The personal information distribution of the five experts invited are shown in Table 7. Referring to the scores of the experts' qualifications in Table 5 and based on Formula (5), the weights of the experts were calculated.

Table 7. Expert personal information and weight.


The expert fuzzy evaluations of exogenous variables for catenary construction risks are shown in Table 8.

Table 8. Expert fuzzy evaluation table of exogenous variables for catenary construction risks.


According to the expert fuzzy evaluation results in Table 8, combined with Equations (8)-(10), the probability of occurrence for exogenous variables in catenary construction risks was calculated and is presented in Table 9.

Table 9. Priori probability of exogenous variables.


# 4.3. Establish a Fuzzy Bayesian Network Model for Catenary Construction Risks 

In this paper, the structural causal model of catenary construction risks was constructed in Section 4.1 to determine the causal logical relationship between risk factors. The probability of occurrence for risk endogenous variables was calculated according to the results of expert fuzzy evaluation in Section 4.2, and based on the overview in Section 3.2.2, the conditional probability of risk endogenous variables was determined by consulting the experienced personnel in catenary construction engineering for many times. Then, we can construct a Bayesian network model of catenary construction risks, as shown in Figure 5. According to the calculation results in Figure 5, the comprehensive probability of occurrence for catenary construction risks was 0.60 . Thus, it can be seen that under the background of the traditional management mode, risks were likely to occur in the process of catenary construction. Therefore, it was necessary to formulate risk control measures for the weak points and strictly abide by various engineering rules and regulations during the construction process to improve project efficiency and enhance project quality.

![img-4.jpeg](img-4.jpeg)

Figure 5. Analysis diagram of catenary construction risks Bayesian network forward inference.
Based on Equation (14), the probability of catenary construction risk occurring was assumed to be $100 \%$. The posterior probability of endogenous and exogenous variables for catenary construction risks was then obtained through reverse reasoning, as presented in Table 10 and Figure 6.

Table 10. Posterior probability of risk factors.


# 4.4. Importance Analysis of Exogenous Variables of Catenary Construction Risks 

The probability importance and critical importance of the exogenous variables are calculated according to Equations (15) and (16), and the results are shown in Table 11.

The ranking result of probability importance is:

$$
I_{C_{4}}^{p i}>I_{C_{3}}^{p i}>I_{C_{6}}^{p i}>I_{C_{5}}^{p i}>I_{C_{2}}^{p i}>I_{C_{1}}^{p i}
$$

The critical importance ranking result is:

$$
I_{C_{4}}^{c i}>I_{C_{3}}^{c i}>I_{C_{6}}^{c i}>I_{C_{5}}^{c i}>I_{C_{2}}^{c i}>I_{C_{1}}^{c i}
$$

![img-5.jpeg](img-5.jpeg)

Figure 6. Analysis diagram of catenary construction risks Bayesian network reverse inference.

Table 11. Critical importance calculation results of probability importance.


The higher the probability importance and critical importance, the more likely the exogenous variables are to cause the occurrence of catenary construction risks. By comparing and analyzing the importance of exogenous variables of catenary construction risks, the probability importance and critical importance of exogenous variables $C_{3}, C_{4}$ were relatively large, which indicates that improve the basic quality level of workers and the sense of responsibility of the supervision unit can effectively reduce the risk of catenary construction process.

# 4.5. Corresponding Measures

Based on the results of importance analysis and reverse reasoning of risk factors during the construction of catenary, the following measures for catenary construction risk management and control are proposed.

Strictly implement the engineering technical disclosure and regularly assess the skill level of construction personnel. The quality level of construction personnel is critical to the risk control of the whole process of catenary construction. The on-site construction personnel shall be strictly trained and the technical level of the construction personnel who completed the training shall be assessed to ensure that the technical level of construction personnel meets the requirements of project quality assurance.

Standardize the daily quality inspection standard of the project. The supervision unit and the Safety and Quality Department shall carefully and responsibly carry out daily quality inspection in strict accordance with the standards and specifications of catenary engineering. The owner unit can establish a daily inspection process assessment system for the inspection unit and the inspected unit, respectively, commend and reward the inspection units and personnel who pass the assessment or rank high, and punish the units who neglect their duties or rank low. In addition, the owner should establish a complete set of quality inspection-rectification-review process to realize the closed-loop treatment of daily quality inspection.

Formulate the work assessment system for supervisors. The supervisor is responsible for supervising the work of all departments at the construction site, and so, the performance appraisal system of the supervisor's personnel is established to improve the working attitude and enthusiasm of the supervision engineer and control the quality of catenary project from the root.

# 5. Discussion and Conclusions 

This paper constructed a fuzzy Bayesian network model for catenary construction risks that allows for the incorporation of expert knowledge and subjective assessments. We can obtain the data for the model simulation inference through the subjective evaluation of the experts, which cannot be obtained directly from the available materials. Firstly, a structural causal model was used to analyze and describe the causal logic relationship between risk factors in the catenary construction. Through expert fuzzy evaluation and consultation, the basic data required for risk quantification evaluation were obtained, and subsequently, a fuzzy Bayesian network model for risk assessment for catenary construction was constructed. The comprehensive risk level of catenary construction process was inferred to be 0.6 through forward reasoning analysis of the fuzzy Bayesian network, confirming that there were certain shortcomings in the current risk control of catenary construction. Therefore, this study conducted backward reasoning and importance analysis, and inferred the risk factors that had a greater influence on catenary construction risk level are "low quality of construction personnel" and "inadequate supervision by the construction unit". Based on this conclusion, this study proposed four risk control measures, which provide theoretical support for project managers, standardize catenary construction process, improve construction efficiency and quality, and ensure catenary construction safety. This research provides good guidance and reference for future catenary construction risk control and related management.

Author Contributions: Conceptualization, Y.C.; methodology, Y.C.; software, X.L.; formal analysis, J.W. and M.L.; investigation, C.C. and J.W.; resources, Y.C.; data curation, X.L.; writing—original draft, Y.C. and J.W.; writing-review and editing, M.L. and Y.S.; supervision, Y.C. All authors have read and agreed to the published version of the manuscript.
Funding: This paper was supported by Research Project of China Academy of Railway Sciences Group Co., LTD [grant number 2022YJ130-1].
Data Availability Statement: All the relevant data are already included in the main manuscript.
Acknowledgments: The authors are grateful to the anonymous referees for their constructive comments on the earlier versions of this manuscript.
Conflicts of Interest: The authors declare no conflict of interest.
