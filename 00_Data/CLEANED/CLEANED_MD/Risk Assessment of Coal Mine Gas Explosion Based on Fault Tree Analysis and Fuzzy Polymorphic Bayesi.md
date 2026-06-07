# Risk Assessment of Coal Mine Gas Explosion Based on Fault Tree Analysis and Fuzzy Polymorphic Bayesian Network: A Case Study of Wangzhuang Coal Mine 

Jinhui Yang ${ }^{1}$ (D) Jin Zhao ${ }^{2, *}$ and Liangshan Shao ${ }^{1,3}$

## check for updates

Citation: Yang, J.; Zhao, J.; Shao, L. Risk Assessment of Coal Mine Gas Explosion Based on Fault Tree Analysis and Fuzzy Polymorphic Bayesian Network: A Case Study of Wangzhuang Coal Mine. Processes 2023, 11, 2619. https://doi.org/ 10.3390/pr11092619

Academic Editor: Carlos Sierra Fernández

Received: 9 August 2023
Revised: 22 August 2023
Accepted: 28 August 2023
Published: 2 September 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Business Administration, Liaoning Technical University, Huludao 125105, China; 472121243@stu.lntu.edu.cn (J.Y.)
2 School of Management, Tianjin University of Technology, Tianjin 300384, China
3 School of Management Engineering, Liaoning Institute of Science and Engineering, Jinzhou 121010, China

* Correspondence: 472021286@stu.lntu.edu.cn; Tel.: +86-157-3318-1336


#### Abstract

The prevention and control of gas explosion accidents are important means to improving the level of coal mine safety, and risk assessment has a positive effect on eliminating the risk of gas explosions. Aiming at the shortcomings of current risk assessment methods in dynamic control, state expression and handling uncertainty, this study proposes a method combining fault tree analysis and fuzzy polymorphic Bayesian networks. The risk factors are divided into multiple states, the concept of accuracy is proposed to correct the subjectivity of fuzzy theory and Bayesian networks are relied on to calculate the risk probability and risk distribution in real time and to propose targeted prevention and control measures. The results show that the current risk probability of a gas explosion accident in Wangzhuang coal mine is as high as $35 \%$, and among the risk factors, excessive ventilation resistance and spontaneous combustion of coal are sources of induced risk, and the sensitivity value of electric sparks is the largest, and the prevention and control of the key factors can significantly reduce the risk. This study can provide technical support to coal mine gas explosion risk management.


Keywords: coal mine gas explosion; polymorphic Bayesian network; fault tree analysis; fuzzy theory; risk assessment

## 1. Introduction

Coal is widely used in the fuel, power generation and chemical industries and remains one of the world's most important energy sources [1]. China is the world's largest producer of coal, which is also the country's main energy supply [2]. However, with the development of China's mining industry, the complexity of coal mine systems is increasing, and the probability of systemic risk events is also increasing [3]. Among all the types of coal mine accidents in China, gas explosions are the most harmful [4]. Gas explosions have accounted for more than 25 percent of all deaths in coal mine accidents in China since 2015 [5]. Tong et al. [6] point out that after 2017, China has encountered technical and management bottlenecks in the field of coal mine gas explosion prevention, and the number of accidents and fatalities is difficult to hit a new low. At present, China's coal mining is in a critical period of transformation to intelligent construction. In order to prevent and control gas explosion accidents, many coal mining enterprises have taken measures such as upgrading equipment and improving mining automation level. These measures have played a positive role in eliminating potential risks but still cannot completely avoid coal mine gas explosions.

Risk assessment is one of the common theoretical methods used to cope with coal mine accidents, potential mining risk factors through risk identification, explore the key factors causing accidents and critical accident paths and propose targeted measures toward risk management. Methods of risk assessment and analysis can be categorized into qualitative

and quantitative methods according to their presentation [7], and both types of methods have achieved practical results in coal mine accident risk assessment. In terms of qualitative methods, Bagherpour et al. [8] classified and assessed coal mine accidents in Iran from the perspective of preventive measures based on expert experience. Kasap et al. [9] used the hierarchical analysis method to assess the risks in the production process of surface coal mines and explored the greatest risks among them. Domínguez et al. [10] adopted the decision matrix method to explore the risk assessment and analysis of underground mining in Guanajuato, Mexico. In terms of quantitative methods, Mottahedi et al. [11] took a fault tree analysis approach to assess the risk of impact ground pressure accidents in coal mines and explored the probability of occurrence through the minimum cut set. Pejic et al. [12] proposed the operating condition risk assessment method for assessing the occurrence of explosions in coal mines based on the risk index, and the probability of risk was found through the scenario frequency, consequence and time. The advancement of digital technology and the development of computers have enabled the emergence of many new risk assessment methods, such as Monte Carlo simulation and machine learning methods [6,13]. Among them, Bayesian networks are widely used to reason about uncertain events [14], which breaks through the limitations of static assessment and can be used to superimpose risks through inference techniques to more realistically express the relationship between risk factors. However, Bayesian networks need accurate parameters to carry out risk assessment, and the results derived from insufficiently accurate parameters are worthy of questioning [15]. In addition, in most cases, risk factors are dynamic, not black or white. Many studies simply divide risk factors into "true" and "false" when applying Bayesian networks, so risk assessment results deviate from the actual situation. In order to solve the problem of high parameter accuracy requirements of Bayesian networks, Tong et al. and Zarei et al. proposed using the Delphi method to integrate expert knowledge to calculate Bayesian network parameters, which provides a new idea for exploring precise Bayesian network parameters but ignores the subjective factors brought by an expert's own knowledge background and work experience, which affects the accuracy of the risk assessment results [16,17]. Fuzzy theory is a method used to accurately assign values to uncertain things, and the combination of Bayesian networks and fuzzy theory is a worthwhile tool to be applied [18], but it is also necessary to correct the subjective influence of the evaluators involved in the judgment.

Aiming at the above problems, this study was carried out as follows: Firstly, coal mine gas explosion accident cases in China since 2011 are organized and combined with the existing literature; the fault tree analysis method is used to identify the risk factors of coal mine gas explosions from the perspectives of the gas concentration exceeding limit and the appearance of ignition sources to obtain a fault tree containing 30 bottom events and 12 intermediate events, and the fault tree mapping is transformed into a Bayesian network. For each specific Bayesian network node, As Low As Reasonably Practicable (ALARP) is utilized to classify the state of the node into three kinds: High, Moderate and Low, which avoids classifying the state of the node into "true" or "false" and makes the state of the risk factors closer to the actual situation and makes the results of the risk assessment of the Bayesian network more diversified. Secondly, taking Wangzhuang coal mine as an example for Bayesian network parameter learning, a more accurate trapezoidal fuzzy number of seven levels of language variables is adopted, so that the evaluator has more space in the process of assigning values to the judgment of each risk factor, and a method of calculating the evaluation accuracy from four perspectives of degree, years of working, professional relevance and judging confidence is proposed to correct the subjective influence of the evaluator. In order to minimize the error caused by subjective factors, the case resource advantage is also considered in the parameter determination process, and the conditional probability is statistically calculated from numerous cases, so as to perform parameter learning from both subjective and objective perspectives. Finally, the established Bayesian network and the calculated parameters were imported into GeNIe software (developed by the decision systems laboratory at University of Pittsburgh, version 2.3 of GeNle) to

assess the risk probability of gas explosions in Wangzhuang coal mine through causal reasoning, derive the induced paths of the gas concentration exceeding the limit and the appearance of ignition sources through diagnostic reasoning, derive the key sensitivity factors of gas explosions through sensitivity analysis and put forward the targeted measures for preventing and controlling the risk of gas explosions in regard to the actual situation of Wangzhuang coal mine. This study can provide a reference for the risk management of gas explosions in coal mines.

# 2. Materials and Methods 

The first step of this study was to use a fault tree to analyze coal mine gas explosion accident cases, determine the risk factors of coal mine gas explosions and carry out the structure learning of Bayesian networks. The second step was to learn the parameters of the Bayesian network through fuzzy comprehensive evaluation and statistical analysis. Finally, the risk of gas explosions in Wangzhuang coal mine was assessed by GeNIe software. The analysis process is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Risk assessment process of coal mine gas explosion.

### 2.1. Bayesian Network Structure Learning

### 2.1.1. Establishment of Fault Tree of Coal Mine Gas Explosion

The premise of risk assessment is the accurate identification of risks [19]. In the process of specific risk identification, risks are often identified as specific risk factors [20]. When identifying the risk factors of coal mine safety, the existing research usually divides the risk factors into four categories, including: human factor, machine factor, environmental factor, and management factor [21]. However, this is not fully applicable to the identification of risk factors of coal mine gas explosions [22]. On the one hand, the extraction and quantification of management factors are usually accompanied by the evaluator's subjective judgment, which affects the accuracy of risk assessment results. On the other hand, human factors overlap with management factors and machine factors, making the same risk factors repeat. Considering the above problems, this study starts by considering the conditions causing coal mine gas explosion accidents, that is, from the perspective of the gas concentration exceeding the limit and the appearance of ignition sources, to identify risk factors. Because risk factors affecting oxygen concentration are difficult to extract and quantify, oxygen was not taken into account in this study.

Reasonable use of prior knowledge is of great significance to the structure learning of Bayesian networks, and fault tree analysis is one of the important methods in accumulating empirical knowledge in engineering fields. Fault tree analysis can identify and evaluate the risk factors of the research object; it is simple and intuitive in qualitative analysis and is an important system safety analysis method. It takes the cause-and-effect tree as the concrete form [23]. We collected investigation reports on 82 coal mine gas explosions in China since 2011, which resulted in more than 700 deaths. Ten coal mine gas explosion researchers and mine ventilation practitioners were invited to conduct a detailed analysis of the accident causes in the accident investigation report and, combined with the existing research on the causes of coal mine gas explosions [22,24], the risk factors of coal mine gas explosions were obtained, and the coal mine gas explosion risk fault tree was drawn, as shown in Figure 2. The fault tree analysis method was used to identify the risk factors of coal mine gas explosions, improve the efficiency of Bayesian network structure learning, avoid the shortcomings of hasty classification of risk factors and give full attention to historical experience.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Coal mine gas explosion risk fault tree.

In the coal mine gas explosion risk fault tree, 30 bottom events such as fan failure are represented as *B*1, *B*2, ..., *B*30, representing 14 intermediate events such as abnormal fan operation represented as *A*1, *A*2, ..., *A*14. The risk factors are summarized in Table 1.

Table 1. Coal mine gas explosion risk factors.


# 2.1.2. Polymorphism Classification of Risk Factors Based on ALARP 

As Low As Reasonably Practicable (ALARP) is a method used to divide research objects into different intervals by dividing acceptability and tolerance thresholds; it has

been widely used in medicine and investment fields [25,26]. Referring to ALARP's thought process, this study set "Unacceptable level of risk" and "Negligible level of risk" for the risk factors of coal mine gas explosions and divided the risk factors into three states of "High", "Moderate" and "Low". The three states indicate "The risk is too high and measures must be taken immediately" and "The risk is acceptable but it is better to take measures to deal with it" and "The risk is negligible". As shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Three risk states of risk factors.
Compared with the way of dividing risk factors into "true" and "false" in existing studies, this study divides risk factors into three states to create more judgment space and make the description of risk factors more accurate.

# 2.1.3. Determination of Bayesian Network Structure 

Since the coal mine gas explosion fault tree is determined by the logical relationship between various risk factors, the Bayesian network structure of coal mine gas explosions should also be established by the same logical relationship. Therefore, the structure and events of the coal mine gas explosion fault tree are mapped to the structure and nodes of the Bayesian network of coal mine gas explosions. The bottom events of the coal mine gas explosion fault tree are mapped as the root nodes of the Bayesian network of coal mine gas explosions, the intermediate events are mapped as the intermediate nodes and the top event is mapped as the final target node, and the structure of the Bayesian network of coal mine gas explosions is determined, as shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network structure of coal mine gas explosions.

2.2. Bayesian Network Parameter Learning

This study takes Wangzhuang coal mine as an example to assess the risk of gas explosions. Wangzhuang coal mine is a key state-owned coal mine located in Shanxi Province, China. The well field covers an area of $79.6806 \mathrm{~km}^{2}$ and has an annual production capacity of 7.1 million tons. The mine development mode is vertical shaft and inclined shaft mixed development, the mining object is the 3# coal seam and there are 4 return air shafts and 7 air inlet shafts, forming a relatively perfect mine ventilation system. In order to ensure the safety of production, Wangzhuang coal mine has arranged a number of methane detection devices and wind speed detection equipment in the mine and established a ventilation management information system. However, Wangzhuang coal mine is a highgas mine, coal dust is explosive and coal seams' spontaneous combustion tendency is toward spontaneous combustion, so Wangzhuang coal mine has the basic conditions for coal mine gas explosions; thus, it is necessary to carry out risk assessment.

# 2.2.1. The Prior Probability Determination of Root Nodes Based on Fuzzy Theory 

Fuzzy theory is a method of using fuzzy numbers to represent uncertain values and calculating uncertain values through membership functions. This theory was first proposed by Zadeh [27]. At present, most applications of fuzzy theory are applied using the triangular fuzzy theory with 5 levels of language variables. Considering that the great harm of coal mine gas explosions needs accurate assessment and that the judgment ability of experts is usually within 5-9 intervals [28], this study adopts the trapezoidal fuzzy theory with 7 levels of language variables, which is more accurate.

Assume that $a, b, c$ and $d$ are four values in the trapezoidal fuzzy number interval, then the trapezoidal fuzzy number is $\widetilde{C}=(a, b, c, d)$, and its membership function $\mu \widetilde{C}(x)$ is shown in Equation (1) and Figure 5.

$$
\mu \widetilde{C}(x)=\left\{\begin{array}{cc}
0 & x<a \\
\frac{x-a}{b-a} & a \leq x<b \\
1 & b \leq x<c \\
\frac{x-d}{c-d} & c \leq x<d \\
0 & x \geq d
\end{array}\right.
$$

![img-4.jpeg](img-4.jpeg)

Figure 5. Membership function of language variable.

In order to make the calculation process more concise and intuitive, the abbreviated form of each language variable is proposed, and the seven levels of language variables and their abbreviations and fuzzy intervals are organized as shown in Table 2.

Table 2. Language variables and fuzzy intervals.


When assessing the risk of coal mine gas explosions in Wangzhuang coal mine, the parameters of each root node of the Bayesian network should be determined first. Ten experts were invited as evaluators to judge the parameters of each root node according to the trapezoidal fuzzy number of the 7 levels of language variables. All 10 evaluators were from Wangzhuang coal mine or researchers related to coal mine gas explosions. The evaluation process was as follows: 10 evaluators conducted field research on Wangzhuang coal mine, combined with relevant data of Wangzhuang coal mine, and judged the three states of "High", "Moderate" and "Low" of the risk factors represented by 30 root nodes according to the 7 levels of language variables after mastering the situation of Wangzhuang coal mine. Due to the different knowledge background, professional experience and working time of each evaluator, the accuracy of each evaluator's judgment was different. Therefore, in order to correct the judgment accuracy, the calculation method of the evaluator's judgment accuracy was proposed considering four perspectives: degree, years of working, professional relevance and judging confidence, as shown in Table 3.

Table 3. The accuracy of the evaluators' judgment.


The accuracy of an evaluator's judgment can be obtained by summing the scores of the evaluator's degree, years of working, professional relevance and judging confidence. Assuming that $D_{e}{ }^{\prime}$ is the judgment accuracy of the $e$-th evaluator, the judgment accuracy of 10 evaluators is calculated successively and normalized. The calculation formula is as follows:

$$
D_{e}=\frac{D_{e}^{\prime}}{\sum_{1}^{10} D_{e}^{\prime}}
$$

According to Equation (2), the judgment accuracy of 10 evaluators is calculated successively, as shown in Table 4.

Table 4. The evaluator evaluates accuracy.


We assumed that the $e$-th evaluator judges the $j$ state of the risk factor represented by the $i$ root node and judges that the $a$ value corresponding to the given language variable is $a_{e i j}^{\prime}(i \leq 30, j \leq 3)$. After all evaluators had made judgments, the calculation formula for the value of a judged by all evaluators was implemented as follows:

$$
a_{i j}=\sum_{e=1}^{10} D_{e} a_{e i j}^{\prime}
$$

In a similar fashion, $b_{i j}, c_{i j}$ and $d_{i j}$ can be calculated. At this time, the gravity center method is adopted to de-fuzzify the fuzzy interval values [28], and the calculation formula is as follows:

$$
F_{i j}^{\prime}=\frac{\left(c_{i j}+d_{i j}\right)^{2}-c_{i j} d_{i j}-\left(a_{i j}+b_{i j}\right)^{2}+a_{i j} b_{i j}}{3\left(c_{i j}+d_{i j}-a_{i j}-b_{i j}\right)}
$$

$F_{i j}^{\prime}$ represents the defuzzification value of the prior probability of the $j$ state of the $i$ root node. Each root node has a total of 3 states: High, Moderate and Low, but the sum of the defuzzification values of the probability values of the 3 states is usually not 1 . In order to satisfy the requirement that the sum of state probabilities of the Bayesian network is 1, we normalized $F_{i j}^{\prime}$ with reference to Formula (2) and calculated the prior probability of the $j$ state of the $i$ root node as $F_{i j}$.

# 2.2.2. Determination of Intermediate Node Conditional Probability 

In Bayesian networks, the conditional probability of intermediate nodes is more complex than the prior probability of root nodes. This study uses the subjective method of evaluator judgment and the objective method of case statistics to determine the prior probability of intermediate nodes. The occurrence of accidents is a random event with complex coupled causes, but there are still statistical characteristics to follow, which can provide reference for risk assessment and prevention [24]. Regulatory norms and the development of the Internet enable a large number of coal mine gas explosion accident cases to be saved. Statistical analysis of a large number of coal mine gas explosion cases can obtain the statistical characteristics of risk factors and provide objective data support. Therefore, in terms of determining the conditional probability of intermediate nodes in Bayesian networks, based on the evaluators' subjective fuzzy evaluation, we further consider the objective data and comprehensively determine the conditional probability of intermediate nodes from both subjective and objective perspectives.
$B_{23}, B_{24}$ and $A_{14}$ nodes were selected from the Bayesian network, and the three nodes were taken as examples to explain the process of determining the conditional probability of intermediate nodes combining subjective and objective perspectives. $B_{23}$ and $B_{24}$ are the root nodes of the Bayesian network and the parent nodes of $A_{14} . A_{14}$ is the middle node of the Bayesian network, and only $B_{23}$ and $B_{24}$ are parent nodes. The three nodes are shown in Figure 6.

(1) Objective assignment
![img-5.jpeg](img-5.jpeg)

Figure 6. Nodes $B_{23}, B_{24}$ and $A_{14}$.
Each node has three states: High, Moderate and Low. According to the statistics of 82 coal mine gas explosion accidents, the occurrence frequency of $A_{14}$ states under the combination of $B_{23}$ and $B_{24}$ states is shown in Table 5.

Table 5. $A_{14}$ frequency statistics table.


For each combination of the two parent nodes of $A_{14}$, the probability sum of the three states of $A_{14}$ is 1 .
(2) Combination of subjective and objective assignment

According to the above method of determining the root node according to the ladder fuzzy theory of the 7 levels of language variables, the conditional probability of the intermediate node $A_{14}$ is determined, which is a subjective assignment. Therefore, the conditional probability based on the subjective judgment of 10 evaluators based on the actual situation of Wangzhuang coal mine and the conditional probability based on the objective statistics of a large number of coal mine gas explosion accidents can be obtained. In order to comprehensively consider subjective opinions and objective data, according to the suggestions of 10 evaluators, the conditional probability obtained from subjective evaluation and the conditional probability obtained from objective data statistics are both given a weight of $50 \%$; the conditional probability of the intermediate nodes is then obtained through weighted calculation, as shown in Table 6.

Table 6. $A_{14}$ table of subjective and objective conditional probabilities.


# 2.3. Construction and Analysis of Polymorphic Bayesian Networks 

Bayesian networks represent a common method used to analyze coal mine risk accidents and can build directed acyclic graphs and analyze and predict research objects according to the quantitative relationship between nodes [5]. In a polymorphic Bayesian network, each node has three states, the node represents the variable and the arc represents the relationship between the nodes [7]. Assuming that the variables of a polymorphic Bayesian network are $G=\left(g_{1}, g_{2}, \ldots, g_{n}\right)$ and that $P_{h}\left(g_{i}\right)$ is the set of parent nodes of variable $g_{i}$, then the joint probability distribution $P(G)$ of $G$ can be expressed as:

$$
P(G)=\prod_{i=1}^{n} P\left(g_{i} \mid P_{h}\left(g_{i}\right)\right)
$$

When the evidence is updated to $E$, the posterior probability $P(G \mid E)$ of the variable is:

$$
P(K \mid F)=\frac{P(G, E)}{\sum_{G} P(G, E)}
$$

(1) Causal reasoning

Causal reasoning is the use of Bayesian network forward reasoning technology to calculate the probability of each risk state of a research object, to achieve the purpose of risk assessment with probability. Assuming that the risk occurrence probability of the research object is $P(K), K_{l}$ is the $l$ risk state of the research object node $(l \leq 3), O_{m}$ is the m root node of the research object node $(m \leq 30), o_{q}$ is the q risk state of the root node $(q \leq 3)$ and $P\left(O_{m}=o_{q}\right)$ is the joint probability of the root node, $P\left(K=K_{l} \mid O_{m}=o_{q}\right)$ is the conditional probability table of the forward conduction of the object node; thus, the causal reasoning formula is as follows:

$$
P\left(K=K_{l}\right)=P\left(O_{m}=o_{q}\right) P\left(K=K_{l} \mid O_{m}=o_{q}\right)
$$

(2) Diagnostic reasoning

Based on the established multistate Bayesian network, the probability of each state of other nodes can be deduced when the object node of the study is in a specified state, and the induced path of the result can be determined according to the probability, providing a basis for risk prevention and control. We assumed $K_{l}$ as the $l$ risk state of the research object node $(l \leq 3)$ and set the probability of $P\left(K=K_{l}\right)$ as $100 \%$. The posterior probability calculation formula of the $m$ root node of the research object node obtained by diagnostic reasoning is as follows:

$$
P\left(O_{m}=o_{q} \mid K=K_{l}\right)=\frac{P\left(O_{m}=o_{q}\right) P\left(K=K_{l} \mid O_{m}=o_{q}\right)}{P\left(K=K_{l}\right)}
$$

(3) Sensitivity analysis

Sensitivity analysis can explore the sensitivity value of nodes, and the higher the sensitivity value of nodes, the more significant the impact on the inference result, which is an important basis for risk prevention and control. Assuming that $H\left(O_{m}\right)$ is the sensitivity value of the m root node $(m \leq 30)$ to the object node of the study, the calculation formula of $H\left(O_{m}\right)$ is as follows:

$$
H\left(O_{m}\right)=\frac{\max \left\{P\left(K=K_{l} \mid O_{m}=o_{q}\right)\right\}-\min \left\{P\left(K=K_{l} \mid O_{m}=o_{q}\right)\right\}}{2 P\left(K=K_{l}\right)}
$$

## 3. Results

### 3.1. Bayesian Network Parameters

(1) Prior probability of root node

Ten evaluators conducted field research in Wangzhuang coal mine. After fully grasping the situation of Wangzhuang coal mine, they judged the risk factors according to the

trapezoidal fuzzy theory of seven levels of language variables and calculated the prior probabilities of each root node of the Bayesian network, as shown in Table 7.

Table 7. The prior probabilities of the root nodes.


As can be seen from Table 7, the risk of spontaneous combustion of coal is the highest, the probability of the High risk state is $39.7 \%$ and the probability of the Low risk state is only $14.8 \%$. In addition, excessive ventilation resistance, accumulation of gas in the roof collapse area, accumulation of gas in the blind alley and friction and collision between metals and rocks also have greater risks.
(2) Conditional probability of intermediate nodes

According to the survey results in Wangzhuang coal mine, 10 evaluators gave subjective judgment on the conditional probability of the intermediate nodes and calculated the conditional probability of the intermediate node in the subjective dimension according to the ladder fuzzy theory of seven levels of language variables. The occurrence frequency of each risk factor in 82 coal mine gas explosion accidents was counted, and the conditional probability of each intermediate node was calculated in turn to obtain the conditional probability of the intermediate node from an objective perspective. The subjective and objective conditional probabilities of intermediate nodes are both given a weight of $50 \%$ and the conditional probabilities of intermediate nodes are calculated by weighting. Limited by space, Table 8 shows the conditional probability table of the intermediate node $A_{14}$.

Table 8. The conditional probability of node $A_{14}$.


# 3.2. Causal Reasoning 

GeNle software developed by the Decision Systems Laboratory of the University of Pittsburgh is used for Bayesian network reasoning [29]. The polymorphic Bayesian network structure of coal mine gas explosions is imported into GeNle software, and the Bayesian network parameters obtained according to the actual situation of Wangzhuang coal mine and a large number of accident cases are imported into GeNle software. After causal reasoning, the Bayesian network diagram of Wangzhuang coal mine gas explosion risk is obtained, as shown in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. Bayesian network diagram of coal mine gas explosions in Wangzhuang Coal mine.
As can be seen from Figure 7, the probability of coal mine gas explosions in Wangzhuang coal mine is as high as $35 \%$. The probability of the gas concentration exceeding the limit is as high as $48 \%$, and the probability of the gas concentration exceeding the limit being negligible is only $26 \%$. The probability of the appearance of ignition sources is as high as $52 \%$, and the probability of the appearance of ignition sources being negligible is only $27 \%$. Therefore, it is necessary to continue to explore the induced path and key sensitive factors

of gas explosion risk in Wangzhuang coal mine, so as to provide a basis for the prevention and control of gas explosion risk.

# 3.3. Diagnostic Reasoning 

In GeNle software, the High state of probability of two nodes of the gas concentration exceeding the limit and the appearance of ignition sources is set to $100 \%$, and diagnostic inference is carried out. After sorting out the diagnostic reasoning results, the maximum induced path corresponding to each intermediate node is shown in Table 9.

Table 9. Summary of main induced paths of gas explosion in Wangzhuang Coal mine.


At present, the main path leading to the gas concentration exceeding the limit in Wangzhuang coal mine is as follows: excessive ventilation resistance ( $39 \%$ ) $\rightarrow$ the mine ventilation system is unreasonable $(50 \%) \rightarrow$ poor ventilation and wind supply in the mine $(61 \%) \rightarrow$ the gas concentration exceeds the limit ( $100 \%$ ). Wangzhuang coal mine began planning and construction in the 1970s and has been in production for more than 50 years. Some old roadways are deformed, so the air volume is more concentrated, resulting in greater resistance in the return air section of the ventilation system, which is not conducive to the ventilation and wind supply of the mine. After more than 50 years of development, the mine field area of Wangzhuang coal mine has reached more than 70 square kilometers, and the development scope is large, which aggravates the problem of excessive ventilation resistance. At present, the main path of the appearance of ignition sources in Wangzhuang Coal mine is as follows: spontaneous combustion of coal $(41 \%) \rightarrow$ spontaneous combustion $(21 \%) \rightarrow$ flame $(49 \%) \rightarrow$ the appearance of ignition source $(100 \%)$. The spontaneous combustion tendency of the coal seam in Wangzhuang coal mine is toward spontaneous combustion, and the ignition source caused by the spontaneous combustion of coal provides the basic conditions for coal mine gas explosions.

### 3.4. Sensitivity Analysis

In GeNle software, the node representing the gas concentration exceeding the limit and the node representing the appearance of ignition sources of the multistate Bayesian network of coal mine gas explosions are set as target nodes successively, and the sensitivity values of related nodes are deduced, as shown in Figure 8.

Among the 30 root nodes, $B_{1}, B_{2}, \ldots, B_{19}$ represent the gas concentration exceeding the limit and $B_{20}, B_{21}, \ldots, B_{30}$ represent the risk factors of the appearance of ignition sources. Among the 12 intermediate nodes, $A_{1}, A_{2}, \ldots, A_{9}$ represent the risk factors of the gas concentration exceeding the limit and $A_{10}, A_{11}$ and $A_{12}$ represent the risk factors of the appearance of ignition sources. As can be seen from Figure 8, when the gas concentration exceeding the limit is the target node, the sensitivity values of nodes such as excessive ventilation resistance, the gas not being pumped as required and gas accumulation are high. When the appearance of ignition sources is the target node, the sensitivity values

of electrical failure, the device out of explosion and electric spark are higher. From an overall point of view, the sensitivity values of risk factors causing the appearance of ignition sources are higher than that of risk factors causing the gas concentration exceeding the limit.

![img-7.jpeg](img-7.jpeg)

**Figure 8.** Distribution of sensitivity values for risk factors.

### 3.5. Risk Prevention and Control

Control of key risk factors, including excessive ventilation resistance and spontaneous combustion of coal obtained by diagnostic reasoning, as well as excessive ventilation resistance, the gas not being pumped as required, electrical failure and the device out of explosion, is obtained by sensitivity analysis. The High state of risk probability of the above four key risk factors is reduced by 50%. In addition, the High state of risk probability of the remaining root nodes is reduced by 20% to achieve the simulation of proper control of each risk factor. Performing causal reasoning is shown in Figure 9.

As can be seen in Figure 9, the probability of the gas concentration exceeding the limit decreases from 48% to 41%, a decrease of 14.6%, after targeted risk control is carried out based on the risk assessment results. The probability of the appearance of ignition sources decreased from 52% to 42%, a reduction of 19.2%. The probability of a gas explosion in the Wangzhuang coal mine decreased from 35% to 27%, a decrease of 22.9%.

It can be seen that Wangzhuang coal mine has carried out targeted prevention and control of key induced paths and highly sensitive nodes derived from the Bayesian network, so as to reduce the risk of gas explosions. In actual production, Wangzhuang coal mine can reduce the ventilation resistance by reducing the accumulation of materials in the mine roadway, repairing the roadway to improve the roadway to avoid smoothness and other measures. After more than 50 years of development, Wangzhuang coal mine has created a number of abandoned roadways, which can be reused for parallel ventilation, which can not only reduce the economic investment but can also reduce the ventilation resistance and prevent gas from accumulating in the abandoned roadways, reducing the risk of gas explosions [30]. To address the problem of spontaneous coal combustion, Wangzhuang coal mine can take measures from the perspective of endogenous fires, including strict adherence to the mining sequence, reducing the fragmentation of the coal body, hanging curtains.

along the empty roadways and utilizing malleable mastic to plug air leaks. Preventive grouting and retardant fire prevention methods can also be adopted to reduce the impact of spontaneous coal combustion on gas explosions [31]. In addition, there is a risk of electrical failure and equipment failure in Wangzhuang coal mine, which should be strictly controlled through the procurement of equipment and other aspects and enhancement of daily maintenance and management of electrical equipment.
![img-8.jpeg](img-8.jpeg)

Figure 9. Bayesian network diagram after risk prevention and control.

# 4. Discussion 

In the past, when Bayesian networks were used for risk prediction and assessment, after establishing Bayesian network nodes, the state of each node was often divided into "true" and "false", and the parameters of root nodes and intermediate nodes (if there were intermediate nodes) were determined in the same way. This research method not only ignores the polymorphism of risk factors represented by nodes but also ignores the characteristics of different contributions of root nodes and intermediate nodes to inference results. This paper presents a probabilistic method to evaluate the risk of coal mine gas explosions and takes Wangzhuang coal mine as an example to verify it. After establishing the risk factors and Bayesian network structure by fault tree analysis, the ALARP criterion is used to express the polymorphism of risk factors, that is, the risk is not only present or non-existent, but it is completely possible that the risk exists but has no impact. In addition, based on numerous accident cases and the judgment of several experts, this study determined node parameters from both subjective and objective perspectives, which not only made full use of case resources and respected the objective facts of the past but also made full use of expert experience and respected the actual situation of Wangzhuang coal mine to ensure the accuracy of risk assessment.

However, there are still some limitations in this study. First, in order to ensure the timeliness of the case, this study only collected information from 82 coal mine gas explosion accidents since 2011. From the perspective of statistical testing, the number of samples still has room to increase. The samples in this study are all from China, which has started large-scale intelligent coal mine construction, so the samples include both traditional coal mines and intelligent coal mines, which reduces the accuracy of the samples. In addition, China has long realized mechanized mining of coal mines, which makes the technical level of coal mines included in the samples inconsistent with those in some less developed areas, reducing the applicability of the method. Second, although this study proposed the method of considering evaluators' judgment accuracy to correct the judgment results when experts make judgments based on experience, the subjectivity of expert judgment cannot be completely avoided. Third, the results of this study have the characteristics of timeliness. With the development of intelligent construction in coal mines, the risk factors affecting coal mine gas explosions are bound to change, so the risk factor system obtained by fault tree analysis in this study will change accordingly. In the follow-up study, we will look at the world, collect accident cases from coal mines around the world and classify the cases according to the technical level of coal mines, in order to improve the universality of the study. In addition, we will explore other better ways to reduce the subjective influence of evaluators and interview front-line miners, especially those who have experienced accidents, to ask them how to reduce the risk of accidents, which will improve the accuracy of the research.

# 5. Conclusions 

This paper presents a method of gas explosion risk assessment based on fault tree analysis and fuzzy polymorphic Bayesian networks. Firstly, fault tree analysis was used to identify the risk factors of coal mine gas explosions, and a Bayesian network structure was determined according to the causal logic relationship, and risk factors were divided into High, Moderate and Low through the ALARP criterion, so that the Bayesian network was more in line with the actual situation. Second, Bayesian network nodes were divided into root nodes and intermediate nodes. For the determination of the prior probability of root nodes, the trapezoidal fuzzy theory of seven levels of language variables was adopted, which is more rigorous than the triangular fuzzy theory. Ten experts were invited to conduct field research on Wangzhuang coal mine, and their subjective influence was corrected from the perspective of their degrees and work experience. For the conditional probability of intermediate nodes, in addition to the method of subjective determination of conditional probability by fuzzy theory, the conditional probability of each intermediate factor in 82 gas explosion accidents was counted, and the limitation of determining conditional probability by a single method was avoided through the subjective and objective assignment method. Finally, risk assessment was carried out through our Bayesian network. According to causal reasoning, the probability of gas explosions in Wangzhuang coal mine is $35 \%$. According to the diagnostic reasoning, the main induced path of the gas concentration exceeding the limit is as follows: excessive ventilation resistance $\rightarrow$ the mine ventilation system is unreasonable $\rightarrow$ poor ventilation and wind supply in the mine $\rightarrow$ the gas concentration exceeds the limit. The main induced path of the appearance of ignition sources is as follows: spontaneous combustion of coal $\rightarrow$ spontaneous combustion $\rightarrow$ flame $\rightarrow$ the appearance of ignition source. The sensitivity analysis yields high sensitivity values for nodes such as excessive ventilation resistance, the gas not being pumped as required, gas accumulation, electrical failure, the device out of explosion and electrical sparks. According to the prevention and control of the above nodes and paths, the risks of the gas concentration exceeding the limit, the appearance of ignition sources and gas explosions are reduced by $14.6 \%, 19.2 \%$ and $22.9 \%$, respectively, indicating that gas explosions in Wangzhuang coal mine can be prevented and controlled using the results of this study.

From the theoretical point of view, this study divides the node states by the ALARP criterion, expands the node states of Bayesian networks, builds a polymorphic Bayesian

network, explores a new method of Bayesian network application and broadens the new idea of risk assessment from the perspective of probability. From the perspective of practical application, this study combines the actual situation of Wangzhuang coal mine and expert experience to build a polymorphic Bayesian network to evaluate Wangzhuang coal mine, obtain the probability of gas explosions, deduce the key nodes and main induced path of accidents and propose targeted control measures, which has important reference significance for the mine safety management of Wangzhuang coal mine.

Author Contributions: All authors contributed to this work. Specifically, J.Y. developed the original idea for the study and designed the methodology, J.Y., J.Z. and L.S. participated in the discussion of the feasibility of the methodology. J.Y. completed the survey and drafted the manuscript, which was revised by J.Y. and J.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This study was supported by the National Natural Science Foundation of China (No.71771111).
Institutional Review Board Statement: The study was conducted in accordance with the Declaration of Helsinki, and the protocol was approved by the Ethics Committee of Liaoning Technical University.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: Data are available from the authors upon reasonable request.
Acknowledgments: The authors appreciate all the survey participants.
Conflicts of Interest: The authors declare no conflict of interest.
