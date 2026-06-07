# Article 

## Characteristics of Chemical Accidents and Risk Assessment Method for Petrochemical Enterprises Based on Improved FBN

Lidong Pan ${ }^{1}$, Yu Zheng ${ }^{2}$, Juan Zheng ${ }^{1}$, Bin Xu ${ }^{3}$, Guangzhe Liu ${ }^{3}$, Min Wang ${ }^{1}$ and Dingding Yang ${ }^{1, *}$


#### Abstract

check for updates Citation: Pan, L.; Zheng, Y.; Zheng, J.; Xu, B.; Liu, G.; Wang, M.; Yang, D. Characteristics of Chemical Accidents and Risk Assessment Method for Petrochemical Enterprises Based on Improved FBN. Sustainability 2022, 14, 12072. https://doi.org/10.3390/ su141912072

Academic Editors: Fuqiang Yang, Hui Liu, Longxing Yu and Chao Chen

Received: 22 August 2022
Accepted: 19 September 2022
Published: 24 September 2022


#### Abstract

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.


## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 National \& Local Joint Engineering Research Center of Harbor Oil \& Gas Storage and Transportation Technology, Zhejiang Provincial Key Laboratory of Petrochemical Pollution Control, School of Petrochemical Engineering \& Environment, Zhejiang Ocean University, Zhoushan 316022, China School of Naval Architecture and Maritime, Zhejiang Ocean University, Zhoushan 316022, China Sinochem Zhoushan Dangerous Chemical Emergency Rescue Base Co., Ltd., Zhoushan 316022, China * Correspondence: yangdd@zjou.edu.cn


#### Abstract

Refining and chemical integration is the major trend in the development of the world petrochemical industry, showing intensive and large-scale development. The accident risks caused by this integration are complex and diverse, and pose new challenges to petrochemical industry safety. In order to clarify the characteristics of the accident and the risk root contained in the production process of the enterprise, avoid the risk reasonably and improve the overall safety level of the petrochemical industry, in this paper, 159 accident cases of dangerous chemicals in China from 2017-2021 were statistically analyzed. A Bayesian network (BN)-based risk analysis model was proposed to clarify the characteristics and root causes of accident risks in large refining enterprises. The prior probability parameter in the Bayesian network was replaced by the comprehensive weight, which combined subjective and objective weights. A hybrid method of fuzzy set theory and a noisy-OR gate model was employed to eliminate the problem of the conditional probability parameters being difficult to obtain and the evaluation results not being accurate in traditional BN networks. Finally, the feasibility of the methods was verified by a case study of a petrochemical enterprise in Zhoushan. The results indicated that leakage, fire and explosion were the main types of accidents in petrochemical enterprises. The human factor was the main influencing factors of the top six most critical risk root causes in the enterprise. The coupling risk has a relatively large impact on enterprise security. The research results are in line with reality and can provide a reference for the safety risk management and control of petrochemical enterprises.


Keywords: characteristics of hazardous chemical accidents; fuzzy theory set; Bayesian network; risk identification

## 1. Introduction

Hazardous chemicals are chemical substances that usually have toxic, corrosive, flammable, explosive, combustion-supporting and other properties [1]. They exist in the process of the production, storage and transportation of the petrochemical industry [2]. China is one of the largest producers and consumers of petrochemicals in the world [3]. The derivatives of hazardous chemicals have long penetrated into people's daily life and become an indispensable part of the national economy and social development. However, due to the high-risk property of hazardous chemicals, accidents that cause great damage and threat to the social economy, ecological environment and life security often occur in various stages of production in the petrochemical industry [4]. For instance, the " 8.12 Tianjin port accident" occurred in 2015, which caused 173 deaths, 798 injuries and direct economic losses of CNY 6.866 billion [5]; the " 3.12 Xiangshui accident" occurred in 2019, which caused a total of 78 losses, 76 serious injuries and direct economic losses of CNY 1.986 billion, causing serious pollution of the atmosphere and water bodies [6]. In order to reduce the number of accidents and promote the safe and healthy development

of a petrochemical plant, the structure of the petrochemical industry has been optimized and adjusted. Petrochemical production has developed in the direction of large-scale refining and chemical integration [7]. While integrated development brings high-efficiency production, it also leads to a large number of safety risks, which are mainly represented by the variety of hazardous chemicals in storage and production processes, as well as the complex and diverse potential risks [8]. Once a hazardous situation occurs, it is easy to cause a comprehensive disaster with unpredictable and uncontrollable risks, resulting in incalculable economic losses, casualties and ecological damage [9]. At present, with the construction of a considerable number of refining and chemical integration projects, plant production scale and floor space far exceed previous construction projects, which will bring serious threats to the environmental risk tolerance and emergency rescue force. Therefore, for a petrochemical factory with multiple risk sources and complex disaster types, it is necessary to adopt a suitable method to comprehensively analyze and identify the risk factors of the plant. Given the characteristics of the production process and accident characteristics of the petrochemical industry, it is necessary to complete management on a routine basis to eliminate the occurrence of potential front-end accidents.

Fault tree analysis (FTA) is an effective method for system reliability analysis [10]. However, in the application of complex systems, the traditional FTA technique has a multitude of fuzzy uncertainty problems. In response to this question, Tanaka et al. [11] first proposed the fuzzy fault tree analysis method (FFTAM) through the integration of the fuzzy set theory (FST) with the FTA, which uses fuzzy numbers instead of imprecise failure probability values to calculate system reliability. In addition, FFTAM also has the disadvantage of being computationally intensive and unable to perform reverse reasoning. Bobbio et al. [12] proposed a method to transform fault trees into Bayesian networks (BN), which successfully overcame the problems of fuzzy fault trees and obtained a more effective BN model. In view of this, the BN model has begun to be widely applied for risk analysis in various fields. Li et al. [13] presented a BN model for the explosion accident of aluminum liquid in contact with water and identified the most significant causative factors of the explosion. Li et al. [14] combined association rule mining methods with BN models to effectively improve the reliability of risk factor identification, as well as a new perspective for the study of complex interaction mechanisms and risk factor identification driven by coal mine safety data. Cui et al. [15] merged the accident tree analysis method with BN and made the assessment results of storage tank accident more effective. Yin et al. [16] applied a BN to a risk analysis for offshore blowout and identified the main factors of blowout accidents. Li et al. [17] added a fuzzy analytic hierarchy process (FAHP) to the process of the fuzzification of BN model probability determination and concluded that BN-FAHP can be used as a decision tool for preventing coal mine gas explosions. Ma et al. [18] integrated the human factors analysis and classification system into the fuzzy Bayesian network (FBN) model to identify the most critical human root cause events of laboratory fire and explosion accidents in colleges. Qiao et al. [19] applied FBN to the analysis of human factors in maritime accidents and identified the most significant human factors in sand carrier accidents. Yazdi et al. [20] combined FST and BN for the risk assessment of an ethylene transportation line unit in an ethylene oxide (EO) production plant. Santana et al. [21] combined fuzzy logic and a Bayesian network to evaluate the failure probability of thermal radiation in domino effect accidents. Lu et al. [22] evaluated the relationship between risk factors of chemical plant explosion accidents and their impact on accident consequences based on a BN model. The acquisition of basic parameters of the BN model in these studies mainly depends on expert experience, and there is a certain subjective deviation phenomenon.

This study aims to investigate the accident characteristics of petrochemical enterprises and to establish a risk analysis model of petrochemical enterprises based on FBN. Through this model, important risk factors of enterprises were identified. Considering the subjective bias of traditional methods in determining the basic data of the BN model, a hybrid method of expert research and incident analysis was employed to obtain the base data with

more accuracy. In addition, critical importance was used as the basis for the importance evaluation of root nodes. Based on the final ranks of each critical importance, the risk root causes for enterprise accidents are indicated, and some advice is provided.

# 2. Statistical Characteristics of Chemical Accidents 

### 2.1. Sources of Accident and Index Data

In order to truly reflect the current stage of China's petrochemical enterprise safety status, 159 petrochemical accidents in China from 2017-2021 were collected to be statistically analyzed. The accident data were obtained from the Ministry of Emergency Management of the People's Republic of China, the China Chemical Safety Association and the Chemical Information Network and other websites; the risk factors of petrochemical enterprises were obtained from the classification of production process hazards and harmful factors in GB/T 13861-2022 [23] on-site research. The judgment matrix and fuzzy numbers were gained from the index assignment by industry experts with the actual situation of the enterprise.

### 2.2. Accident Analysis

The accident data mainly contained hazardous chemical accidents caused by five major factors: human, material, technology, environment and management during the production process of petrochemical enterprises. Combined with the basic data of accidents, the overall characteristics of hazardous chemical accidents and the current safety situation of the petrochemical industry were acquired from two perspectives: accident time and accident type. The index data covered the expert assessment of the risk index system that consisted of five aspects-human, material, technology, environment and management-and the FBN model was applied to study the root causes of risks in the petrochemical enterprise.

### 2.3. Analysis of Overall Characteristics of Accidents

From 2017 to 2021, taking typical accidents, for instance, 159 hazardous chemical accidents and 478 deaths occurred, as shown in Figure 1. The analysis results indicated that the highest number of accidents was recorded in 2017, and that the number of accidents decreased by $41.67 \%,-21.43 \%, 14.71 \%$ and $31.03 \%$ in 2018, 2019, 2020 and 2021, respectively, compared to the previous year. Overall, the number of accidents decreased at an average annual rate of $16.50 \%$ during 2017-2021. Similarly, the number of accident fatalities decreased at an average annual rate of $15.04 \%$. The peak value of accident fatalities was located in 2019, and this anomaly was due to a particularly significant explosion accident in 2019 in Xiangshui, Jiangsu Province, which caused 78 deaths. The direct cause of the accident was the inadequate identification of hazardous chemical risks. In short, during the process of the restructuring and transformation of the petrochemical industry, the overall accident rate and severity of consequences are declining. Industrial restructuring is conducive to the steady development of the petrochemical industry, but large-scale unconventional emergencies still occur and the impact of the accident remains significant. This year (2022), the Shanghai Petrochemical accident was a consequence of poor safety risk identification and the untimely management of hidden hazards. Therefore, it is necessary to adopt reasonable and effective methods to analyze risks and avoid them.

As shown in Figure 2, explosion accidents were the main type of hazardous chemical accident, occupying $43.4 \%$ of the total number of accidents, and was the main form of accident consequences. In terms of accident consequence severity, poisoning accidents had the highest mortality rate, reaching $93.33 \%$; the average number of fatalities for each accident type during 2017-2021 was 1.78, 2.00, 3.46, 2.53 and 2.09, respectively, with the highest average number of fatalities in explosion accidents. Similarly, in terms of accident level, explosion accidents accounted for the highest proportion of accidents.

![img-0.jpeg](img-0.jpeg)

Figure 1. Overall characteristics of accidents.

# 2.4. Category Analysis of Accident 

Based on the principal characteristics of hazardous chemicals, accidents were divided into five categories: leakage accident, fire accident, explosion accident, poisoning accident and other accident [24]. The statistics of accidents are shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Category statistics of accidents. Other accidents include fall from height and asphyxiation in confined space caused by improper operation of personnel.

In summary, the severity of the accident is closely related to the type of accident. It is important for the safe and healthy development of petrochemical enterprises to study the risk factors of petrochemical enterprises in depth and to carry out improvement measures and management according to the importance of risk factors.

## 3. Risk Analysis Method

A Bayesian network, an effective risk assessment tool for complex systems, can describe the causal relationship between nodes of complex network systems in an easy-tounderstand way. In view of this, this study proposed a new method based on a fuzzy Bayesian network for the risk analysis of petrochemical enterprises. The process of the method is shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. New FBN proposed in this study used to identify risk sources in petrochemical enterprises.

# 3.1. Bayesian Network 

The network topology of a BN is a directed acyclic graph (DAG), including nodes, directed arcs and a conditional probability table (CPT), in which, the nodes represent random variables and the directed arcs and CPT reflect the causal relationships and probability distribution, respectively, between nodes. In a BN, each parent has a prior probability, and each child has a CPT conditional on the corresponding parent. Nodes are directed from parent nodes to child nodes, where the node without the parent is called the root node, and the node without child nodes is called the leaf node [25]. A diagram of the BN structure is shown in Figure 3 where B is a child node of D, C and D are root nodes and A is a leaf node.

The joint probability distribution $\mathrm{P}(\mathrm{X})$ of a set of random variables $X_{i} \approx\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$ associated with the BN can be calculated by Equation (1).

$$
P\left(X_{1}, X_{2}, \cdots X_{n}\right)=\prod_{X_{i} \in\left\{X_{1}, X_{2}, \cdots X_{n}\right\}} P\left(X_{i} \mid P_{a}\left(X_{i}\right)\right)
$$

where $P_{a}\left(X_{i}\right)$ represents the set of parent nodes in $X_{i}(i=1,2, \cdots, n)$.
Causality in BN is expressed as conditional probability. Given two variables $X$ and $Y$, the conditional probability of $X$ can then be calculated by Equation (2).

$$
P(X \mid Y)=\frac{P(Y \mid X) P(X)}{P(Y)}
$$

### 3.1.1. Prior Probability

In order to reduce the problem of subjective bias arising from expert scoring and to avoid objective bias arising from incomplete or bad quality data, a hybrid method combining a quantitative statistics method and an analytic hierarchy process was presented instead of the traditional prior probability calculation method.
(1) Quantitative statistical method

With 159 accidents as a case study, whether the cause of the accident contains the factor as the analysis criterion was noted as $y_{i}(i=1,2, \cdots, n)$; when $y_{i}=1$, the cause of the accident contains the factor; when $y_{i}=0$, the cause of the accident does not contain the factor.

The weight of the quantitative statistical method is calculated as follows.
Accidents are the result of a combination of multiple risk factors, so the $i$-th indicator can be calculated by Equation (3).

$$
\omega_{i}=\frac{\sum_{i=1}^{n} y_{i} / n}{\sum_{j=1}^{N} \sum_{i=1}^{n} y_{i} / n}
$$

where $N$ is the total number of risk factors and $n$ is the total number of accident cases.

(2) Analytic Hierarchy Process (AHP)

The AHP process is mainly divided into the following steps to determine the weight of risk factors [26].
(1) Establishing the set of risk factor indicators $\boldsymbol{A}=\left[A_{1}, A_{2}, \cdots, A_{n}\right]$.
(2) Constructing the judgement matrix $\boldsymbol{D}=\left[D_{1}, D_{2}, \cdots, D_{n}\right]$.
(3) Determining the indicator weights $\boldsymbol{W}_{i}=\left[W_{1}, W_{2}, \cdots, W_{n}\right]$.
(3) Combination weight

$$
p_{i}=\frac{W_{i}+\omega_{i}}{\sum_{i=1}^{N}\left(W_{i}+\omega_{i}\right)}
$$

The combination weight $p_{i}$ represents the prior probability.

# 3.1.2. Conditional Probability 

A combination of a Noise-OR gate model and expert experience was proposed instead of the traditional method [27].

Conditional probability is calculated by Equation (5).

$$
P\left(Y \mid X_{1}, X_{2}, \cdots X_{n}\right)=1-\prod_{i: X_{i} \in X_{T}}\left(1-P_{i}^{*}\right)
$$

where $P_{i}^{*}$ is the fuzzy probability (FP).
The steps of the algorithm are given as follows [28].
Step 1. Determining the weight of experts. As expert assessment is influenced by education, position and experience, etc., the weight of each expert is different. In this study, we mainly considered professional qualification and field experience. Finally, we obtained the expert weight by referring to reference [24]. The results are shown in Table 1.

Table 1. Expert rating weight [29].


Step 2. Mean of triangular fuzzy number. Experts give their own assessment by using a predefined set of linguistic expressions as stated in Table 2, its membership fuzzy number is shown in Figure 4, which can be converted into a triangular fuzzy number (TFN) form, $P_{i}^{k}=\left(a_{i}^{k}, b_{i}^{k}, c_{i}^{k}\right)$. Then, a triangular fuzzy number probability (TFNP), $P_{i}^{\prime \prime}=\sum_{j=1}^{n} \lambda P_{i j}^{k}=\left(a_{i}^{\prime \prime}, b_{i}^{\prime \prime}, c_{i}^{\prime \prime}\right)$, considering expert weight, can be calculated by the arithmetic average method.

Table 2. Fuzzy weight.


![img-3.jpeg](img-3.jpeg)

Figure 4. Fuzzy membership function.
Step 3. Defuzzification. The mean area method (MAM) is employed to convert the TFNP into specific probability values, $F P=\left(a_{i}^{\prime \prime}+2 b_{i}^{\prime \prime}+c_{i}^{\prime \prime}\right) / 4$, which are expressed as the fuzzy probability.

# 3.1.3. Importance Analysis of Root Node 

(1) Probability importance of root node

The contribution of the root node to the occurrence of risk events in the model is called the importance, and the probability importance is one of the instances of importance, and reflects the influence degree of the state of the root node on the leaf node [30]. The probability importance can be calculated by Equation (6).

$$
I_{i}^{P r}\left(x_{i}\right)=P\left(X=1 \mid x_{i}=1\right)-P\left(X=1 \mid x_{i}=0\right)=\frac{P\left(X=1, x_{i}=1\right)}{P\left(x_{i}=1\right)}-\frac{P\left(X=1, x_{i}=0\right)}{P\left(x_{i}=0\right)}
$$

where $I_{i}^{P r}\left(x_{i}\right)$ denotes the probability importance of $x_{i}$.
$P\left(X=1 \mid x_{i}=1\right)-P\left(X=1 \mid x_{i}=0\right)$ denotes the difference between the probability of leaf node failure under the root node failure condition and the probability of leaf node failure under the root node normal condition.
(2) Critical importance of root node

The root node critical importance indicates the rate of the probability change in the leaf node caused by the probability change in the root node [31]. The root node critical importance is calculated by Equation (7).

$$
I_{i}^{C r}\left(x_{i}\right)=\frac{P\left(x_{i}=x_{p} \mid X=X_{p}\right)}{P(X)}=\frac{P\left(x_{i}\right)}{P(X)} I_{i}^{P r}\left(x_{i}\right)
$$

where $P(X)$ and $P\left(x_{i}\right)$ denote the posterior probability of the leaf node and root nodes, respectively.

### 3.1.4. Posterior Probability of Root Node

If the probability of the leaf node is known, the posterior probability of each node can be obtained by the backward inference algorithm of BN.

Assuming that the leaf node of the BN is $X$, the root nodes are $x_{i}$. Knowing that the $X$ is $X_{i}$, then the posterior probability that the root node has a risk probability of $x_{i}^{p}$ is [32].

$$
P\left(x_{i}=x_{p} \mid X=X_{i}\right)=\frac{P\left(x_{i}=x_{p}, X=X_{i}\right)}{P\left(X=X_{i}\right)}=\frac{\sum_{x_{1}, x_{2}, \cdots x_{n}} P\left(x_{1}, x_{2}, \cdots, x_{j}=x_{p}, \cdots, x_{n}, X=X_{i}\right)}{P\left(X=X_{i}\right)}
$$

# 4. Case Study 

The Zhoushan Petrochemical Enterprise started the construction of 40 million tons/year refining and the chemical integration project in 2017, and put into operation the first phase of processing 20 million tons of crude oil, producing 5.2 million tons of aromatics and 1.4 million tons of ethylene annually in 2019. It is an important supporting project for China's (Zhejiang's) economic development. Taking the Zhoushan refinery integration project as an example, the risk analysis of petrochemical enterprises by BN is divided into the following steps [33].

### 4.1. Basic Steps of Enterprise Risk Analysis

Selecting top-events and sub-events for risk assessment and constructing a fault tree of enterprise risk.

Conversing the fault tree to the BN and forming a BN model for enterprise risk.
Quantifying enterprise risk and determining the model parameters of the BN.
Arithmetic testing and reasoning for the BN model.
The basic process of enterprise risk analysis based on the case and BN is shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Model flowchart.

### 4.2. Risk Identification Enterprise

### 4.2.1. Production Process Analysis of Enterprise

The main process of enterprise production includes equipment installation, use and maintenance. Each part of the process has its own risk factors. The risk factors involved in the installation process include the assembly, positioning and testing of the various components for the equipment. The use process comprises the sequence of operating procedures and equipment operation specifications. The maintenance process consists of daily inspection and the regular repair of equipment. In addition, it also includes subjective factors in each process of the enterprise production process, such as improper operation in human factors and inadequate firework management in management factors.

### 4.2.2. Identification of Enterprise Risk Sources

Based on the classification of production process hazards and harmful factors in GB/T 13861-2022, a comprehensive investigation and summary was conducted from the five aspects of human, material, technology, environment and management of the production of enterprises, and the production risk sources of enterprises were identified as follows.

Human factors: psychological, physiological risks and harmful factors, behavioral risks and harmful factors.

Physical factors: physical hazards and harmful factors, chemical hazards and harmful factors, biological hazards and harmful factors.

Technical factors: imperfect safety operating procedures, inadequate technical briefing and inappropriate grading risk control.

Environmental factors: operational environment risk, natural environment risk.
Management factors: inadequate establishment and staffing of safety management institutions, imperfect or unimplemented safety management system, imperfect or unimplemented safety management responsibility system, inadequate safety investment and defective emergency management.

4.3. Topology and Parameter Construction of Bayesian Network

On the premise that the enterprise does not operate illegally, the Bayesian network topology diagram in Figure 6 and the information of each node in Table 3 were established by combining the classification of production process hazards and harmful factors in GB/T 13861-2022 and the enterprise process flow.
![img-5.jpeg](img-5.jpeg)

Figure 6. Safety risk factors of petrochemical enterprise.
(1) Prior probability
(1) Subjective weight

An expert security risk questionnaire was created on the basis of identified corporate risk factors. Domain experts were consulted to assign indicators and acquire a judgment matrix as follows.

$$
\begin{aligned}
& A=\left[\begin{array}{cccc}
1 & 2 & 2 & 4 & 3 \\
1 / 2 & 1 & 1 / 2 & 3 & 2 \\
1 / 2 & 2 & 1 & 3 & 2 \\
1 / 4 & 1 / 3 & 1 / 3 & 1 & 1 / 2 \\
1 / 3 & 1 / 2 & 1 / 2 & 2 & 1
\end{array}\right] ; B_{1}=\left[\begin{array}{cccc}
1 & 1 / 2 & 2 & 2 & 2 \\
2 & 1 & 3 & 2 & 2 \\
1 / 2 & 1 / 3 & 1 & 1 / 2 & 1 / 2 \\
1 / 2 & 1 / 2 & 2 & 1 & 1 \\
1 / 2 & 1 / 2 & 2 & 1 & 1
\end{array}\right] ; B_{2}=\left[\begin{array}{cccc}
1 & 2 & 3 & 4 \\
1 / 2 & 1 & 2 & 3 \\
1 / 3 & 1 / 2 & 1 & 2 \\
1 / 4 & 1 / 3 & 1 / 2 & 1
\end{array}\right] ; \\
& C_{1}=\left[\begin{array}{ll}
1 & 1 \\
1 & 1
\end{array}\right] ; B_{3}=\left[\begin{array}{cccc}
1 & 1 & 2 & 1 & 2 \\
1 & 1 & 2 & 1 & 2 \\
1 / 2 & 1 / 2 & 1 & 1 / 2 & 1 \\
1 & 1 & 2 & 1 & 2 \\
1 / 2 & 1 / 2 & 1 & 1 / 2 & 1
\end{array}\right] ; B_{4}=\left[\begin{array}{ll}
1 & 3 \\
1 / 3 & 1
\end{array}\right] ; B_{5}=\left[\begin{array}{cccc}
1 & 1 / 2 & 1 / 3 & 2 & 1 / 4 \\
2 & 1 & 1 / 2 & 2 & 1 / 2 \\
3 & 2 & 1 & 3 & 1 \\
1 / 2 & 1 / 2 & 1 / 3 & 1 & 1 / 2 \\
4 & 2 & 1 & 2 & 1
\end{array}\right] ; \\
& C_{2}=\left[\begin{array}{cccc}
1 & 3 & 4 & 2 \\
1 / 3 & 1 & 2 & 1 / 2 \\
1 / 4 & 1 / 2 & 1 & 1 / 3 \\
1 / 2 & 2 & 3 & 1
\end{array}\right]
\end{aligned}
$$

The subjective weights of the enterprise risk evaluation indicators were calculated and are shown in Table 4.

Table 3. Bayesian network node information of petrochemical enterprise.


[^0]
[^0]:    Annotation: Technical factors: inadequate identification of production process risk, imperfect safety operation procedures, inadequate technical briefing and inadequate risk classification and control means that the enterprise has carried out the corresponding management behavior. However, unknown risks cannot be completely eliminated due to technical reasons. Natural environment: severe natural weather such as earthquakes and typhoons. Operating environment: poor safety channel, harmful gas over limit, restricted space operation, etc.

Table 4. Risk index subjective weight of petrochemical enterprises.


# (2) Objective weight

The risk factors of hazardous chemical accidents occurring in 2017-2021 were statistically analyzed, and the results are shown in Table 5. According to the statistical results, in terms of human factors, the dominant aspects are improper operation, insufficient safety awareness and improper supervision, as they account for $58.18 \%, 44.03 \%$ and $36.48 \%$, respectively. In terms of physical factors, the main manifestations are equipment design risks and inadequate equipment safety maintenance, both with the same proportion of $40.88 \%$. In terms of technical factors, imperfect safety operation procedures and the inadequate risk analysis and control constitute a large portion at approximately $40 \%$. In terms of environmental factors, the probability of accidents due to a bad operating environment is greater than the probability of accidents due to natural environmental risk, because a bad operating environment is caused by human beings, whereas natural environmental risk is unpredictable, and the latter is more uncontrollable compared to the former. In terms of management factors, the proportion of accidents involving inadequate safety education and training and the risk of a production safety responsibility system is significantly higher than other manifestations of the same category, with the proportion being above $50 \%$. (3) Combination weight

Comprehensive subjective and objective weights were used to acquire root node prior probabilities. The results are shown in Table 6.

Table 5. Factor statistics of accidents.


Table 6. Results of combined weight.


(2) Conditional probability

The conditional probability of each node can be obtained according to the established conditional probability calculation method; taking node B4 as an example, the results are shown in Table 7.

Table 7. Conditional probability of node $Z_{4}$.


(3) Posterior probability

Under the condition of leaf node failure, the posterior probability of each root node was derived by correcting the prior probability with the backward inference capability of BN, as shown in Figures 7 and 8. ![img-6.jpeg](img-6.jpeg)

Figure 7. BN risk diagnosis.

![img-7.jpeg](img-7.jpeg)

Figure 8. Posterior probability of root node.

# 4.4. Sensitivity Analysis 

In the process of enterprise production, more attention is generally paid to factors that play an important role in enterprise safety. The probability importance and critical importance of the root node to the leaf node in the model when it occurs are obtained by Equations (6) and (7), as shown in Figure 9.
![img-8.jpeg](img-8.jpeg)

Figure 9. (a) Fuzzy importance curve; (b) critical importance curve.

As can be seen from the fuzzy importance curve in Figure 9, the human factor is more likely to cause risky accidents than physical, technical, environmental and management factors. Among the management factors, the highest possibility of failure occurs in the safety production responsibility system. In addition, compared with the technical factors, physical factors and environmental factors, it is relatively difficult to improve the risk of accidents caused by human factors, which requires regular training for the personnel working in the enterprise to improve the overall quality of employees and reduce the probability of accidents.

Analyzing the weak points of enterprises according to the ranking of the critical importance of nodes is more beneficial to the improvement of enterprises, prevention of maintenance and fault diagnosis.

From the critical importance curve in Figure 9, it can be seen that the critical root nodes are $\mathrm{C} 1, \mathrm{C} 2, \mathrm{C} 5, \mathrm{C} 11, \mathrm{C} 18$ and C 21 in sequence. C 1 indicates an improper operation of personnel. In the process of enterprise production, people are the first point of contact, and improper operation can easily lead to risky accidents, thus causing losses; on the contrary, standardized operation can not only avoid risks, but can also ensure a safe and smooth development of the enterprise. C2 refers to an insufficient safety awareness of operators. A large number of risky accidents show that insufficient safety awareness is an important cause of accidents. Good safety awareness can reduce the probability of risky accidents, and, even in the event of a risky accident, can reduce the loss caused by the accident to a greater extent. C5 indicates improper supervision. For high-risk enterprises such as petrochemicals, the role of a qualified safety officer is huge, and is the last line of life in enterprise safety production. When the safety officer handles the production process, where there are safety hazards, in a timely manner, it is possible to avoid accidents. C11 indicates imperfect safety operation procedures. Many enterprises do not pay attention to the safety operation procedures, and most of them only rely on the previous operation experience to produce. However, the final result is a large number of human deaths, economic losses and environmental damage. Taking out a certain amount of manpower and material resources for correction can avoid the occurrence of accidents to a greater extent; C18 represents the risk of production safety responsibility system. An enterprise, especially a major hazard source enterprise, has a large number of people and a large number of departments. If they do not perform their respective duties and their responsibilities are unclear, the goal is unclear, the management is bound to be chaotic, the order is blocked, the execution ability is decreased and the risk of accidents is greatly increased. C21 means inadequate emergency management. When an accident occurs, the primary task is to take effective measures to reduce the impact of the accident consequences.

Therefore, it is vastly significant for an enterprise to carry out a reasonable risk analysis, identify the underlying risks and solve the existing problems. In the course of development, it can make the enterprise continuously update and perfect the security management mechanism system. Only this effective mechanism can be a reliable motivational force to promote the long-term development of the enterprise with security and health.

# 4.5. Coupling Risk Analysis 

In order to explore the impact of coupling risk on enterprise security, coupling risk analysis was carried out on the basis of the inference calculation in Section 4.3. Two risk factors, improper operation (C1) and equipment defects (C7), were studied as an example of joint occurrence.

As can be seen from Figure 10, the probability of accidents during production is $61.5 \%$, which is more than twice as high as usual, due to the improper operation of personnel and non-conformity of equipment design and quality. Thus, in the production of enterprises, coupling risk has a relatively large impact on enterprise security.

![img-9.jpeg](img-9.jpeg)

Figure 10. (a) Initial risk; (b) coupling risk.

# 5. Conclusions 

Based on the statistical analysis of 159 typical petrochemical enterprises' safety accidents in China from 2017-2021, an improved FBN model was used to analyze the characteristics of hazardous chemicals in the petrochemical industry and important risk factors of the enterprise. The following conclusions can be drawn:
(1) Petrochemical accidents in China were generally decreasing; leakage, fire and explosion were the main types of accidents; safety risk research for petrochemical enterprises had a a positive impact on enterprise risk control; and, in future enterprise safety risk research, more attention should be paid to the study of leakage, fire and explosion accident risk sources.
(2) According to the critical importance analysis of enterprise risk factors, the results indicated that improper operation, insufficient safety awareness, improper supervision, the risk of the production safety responsibility system and inadequate emergency management were the most critical root events of the enterprise, and human factors were the most important influencing factors of all factors.
(3) In the production of enterprises, coupling risk has a relatively large impact on enterprise security. Enterprises should strictly control the superposition of multiple risk factors in the production process.
Based on expert evaluation and historical accident data, this model identified the main risk sources of enterprises, which solves the subjective bias problem of traditional models to a large extent, and improves the reliability of the research. However, the model is only suitable for the identification of risk sources and cannot analyze the risk probability of enterprises, and the sample size of historical data needs to be further expanded. Further research directions may consider applying the method of combining subjectivity and objectivity to the study of enterprise risk probability, and to the navigation of how to modify the subjective probability reasonably.

Author Contributions: Conceptualization, L.P. and D.Y.; methodology, L.P. and Y.Z.; software, L.P.; formal analysis, Y.Z. and M.W.; investigation, D.Y. and B.X.; resources, B.X.; data curation, G.L.; writing—original draft preparation, L.P. and M.W.; writing—review and editing, J.Z.; visualization, J.Z.; supervision, D.Y.; funding acquisition, D.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the Zhoushan Science and Technology Project (2020C210021), Zhejiang Province Natural Science Foundation (LQ20E040004).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
