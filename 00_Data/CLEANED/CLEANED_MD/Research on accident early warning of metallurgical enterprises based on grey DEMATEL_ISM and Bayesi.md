# scientific reports 

## OPEN

## Research on accident early warning of metallurgical enterprises based on grey DEMATEL/ISM and Bayesian network

Minghui Yan ${ }^{1,2,3}$, Jinzhang Jia ${ }^{1,2,3}$ \& Yinuo Chen ${ }^{3}$


#### Abstract

To clarify the complex relationship between the factors causing safety accidents in metallurgical enterprises and predict the risk of accidents in enterprises, a correlation analysis model of the factors causing safety accidents in metallurgical enterprises based on grey Decision-Making Trial and Evaluation Laboratory/Interpretative Structural Modeling (DEMATEL/ISM) was established, and a Bayesian network early warning model was constructed on this basis. The relationship and action path of accident-causing factors in metallurgical enterprises were clarified. The factors were hierarchically divided and a multi-layer hierarchical structure model was established to obtain the neighboring cause, transitional cause, and essential cause of the accident. The results showed that the employee violation rate, the hazardous substances reserves, the toxic gas and dust pollution control compliance rate, the pass rate for equipment maintenance, and the qualification rate of special equipment were the neighboring causes of the accident. The perfection of the safety production management system was the essential cause. The Bayesian network early warning model was applied to the Fuxin Jiuxing Titanium work site. The expected risk probability of an accident was $17.9 \%$, which was in a comparatively safe state (State2). The results obtained by the Bayesian model are consistent with those obtained by AHP and fuzzy comprehensive evaluation method, which proved the accuracy of the early warning model. The Bayesian model can give the risk probability value of the accident and the risk probability value of the accident cause factors at the same time, and include the causal relationship and conditional correlation relationship among the indicator variables in the reasoning process, which can provide targeted technical support for the construction of the emergency system of risk classification management and control.


Keywords Grey DEMATEL/ISM, Safety management and control, Metal smelting enterprises, Bayesian network, Early warning

The construction of a safety risk classification control system is an important measure to ensure the safety production of enterprises. The safety production accident risk early warning system is an important part of the safety risk classification management and control system. The prevention and control of accidents should be changed from post-punishment to pre-prevention. The metal smelting industry plays an important role in the national economy of many countries, and it is also one of the high-risk industries. The construction of a risk early warning system for safety production accidents in metallurgical enterprises can reduce the incidence of emergencies, property losses, and casualties ${ }^{1,2}$.

Scholars use various methods to conduct risk assessments and build an early warning system for enterprise safety production. For metallurgical enterprises, Shen ${ }^{3}$ established an index risk evaluation method combining weight analysis and risk membership function, constructed a safety early warning method based on the support vector machine model, and obtained the index that had the greatest impact on safety production. According to the production layout, personnel, and equipment of metallurgical enterprises, Miao ${ }^{3}$ used the risk assessment method of operating conditions to carry out a safety assessment and determined the risk level of the main hazard sources. For the screening of early warning indicators, the Decision-Making Trial and Evaluation Laboratory/ Interpretative Structural Modeling (DEMATEL/ISM) has been employed to probe the determinants of various

[^0]
[^0]:    ${ }^{1}$ School of Safety Science and Engineering, Liaoning Technical University, Fuxin 123000, China. ${ }^{2}$ Key Laboratory of Mine Thermal Disaster and Prevention, Ministry of Education, Huludao 125105, China. ${ }^{3}$ School of Civil Engineering, Liaoning Technical University, Fuxin 123000, China. ${ }^{1,2}$ email: jiajinzhang@163.com

nsafe factors and the mechanisms underpinning these interactions^{3--9}. The Bayesian network can reason about uncertain information and has great advantages in solving the faults caused by the uncertainty and relevance of complex problems which has been applied to risk assessment systems in various fields. The improved Dempster/ Shafer (DS) evidence theory-Bayesian network method has been used to establish a risk assessment system for the hazardous chemicals transportation system and the coal mine ventilation system to determine the evaluation system at all levels^{10,11}. Wang^{12} constructed a railway accident prediction model by combining the ISM with the Bayesian network which was applied to the shunting accident in Chengdu to obtain the core factors of the accident and the early warning threshold of the derailment accident. To quantify the risk factors of fire accidents in chemical industrial parks, Song^{13} constructed a fire and explosion accident deduction model from the perspective of scenario response, using expert knowledge combined with the fuzzy Bayesian method. According to the four elements of scenario-behavior-carrier-emergency management, a real explosion accident was used for verification and analysis, and the deduction results were consistent with the actual evolution results. Wu et al.^{14} proposed an integrated risk assessment method based on Dynamic Hazard Scenarios Identification (DHSI), Bayesian network (BN), and risk analysis to evaluate and manage the safety of underground utility tunnels. Based on the most dangerous accident scenarios identified by DHSI, a Bayesian network was constructed for risk analysis.

Scholars in the preceding works focused on the identification of major risk sources, the evaluation of core risk factors, and the risk assessment and early warning of major accidents. There are few studies on the Comprehensive risk factor evaluation and the comprehensive accident early warning model of large-sized industrial enterprises. We use the combination of grey DEMATEL/ISM and Bayesian network to study the relationship and action path of accident-causing factors in metallurgical enterprises, establish a multi-level hierarchical structure model of them, and based on this establish a Bayesian network early warning model. The causal relationship and risk probability between risk factors are quantitatively analyzed.

## Construction of an early warning indicator system

The construction of an early warning system is an indispensable part of emergency management. The early warning model can identify the risk source, control the risk before the hidden danger is formed by adopting risk control measures, and provide decision-making for the response, implementation, and post-disaster recovery of the emergency planning in the disaster. The early warning indicator system is a system composed of various interrelated and mutually restricted factors of metallurgical enterprises, which should be determined on the basis of systematic theoretical analysis, and follow the five principles of scientific, practical, comprehensive and representative combination, qualitative and quantitative combination, timeliness and dynamic combination. After full systematic theoretical analysis, combined with relevant safety production regulations such as “Safety Production Regulations of Metallurgical Enterprises and Non-ferrous Metal Enterprises”^{15}, “Regulations on Safety Production Supervision and Management of Metallurgical Enterprises”^{16}, “Identification of Major Hazard Installations for Hazardous Chemicals” (GB18218-2018)^{17} and “Classification and Code for the Hazardous and Harmful Factors in Process” (GB/T13861-2022)^{18}, the main influencing factors leading to safety production accidents in metallurgical enterprises were summarized. The indicators were selected from four aspects: human, material, environment and management, a hierarchical set of early warning indicators was determined, as shown in Fig. 1.

## Method

The DEMATEL method calculates the influence degree and the influenced degree of each factor on other factors by determining the size of the direct influence relationship between the factors in the system and then obtains the centre degree and cause degree of each factor, and then determines the cause factor and result factor. The role of the ISM method is to decompose the complex system into several subsystems, and finally form a multi-layer hierarchical interpretative structural model. DEMATEL analysis is based on expert judgment, but the value given by expert judgment is difficult to reflect the fuzziness of the influence relationship between factors. The grey system theory is a method to solve the fuzzy problem of the system. Its core idea is to use the grey number interval instead of the specific value in the decision-making process so that the result is closer to the actual situation. For this reason, the grey system theory can be combined with DEMATEL, and the specific value of expert judgment can be converted into a grey number interval to deal with the fuzziness in the decision-making process^{9}.

## Procedure

The grey DEMATEL/ISM analysis steps are as follows^{19--21}.

Step 1: Determine the set of causal factors. C = {C_{1}, C_{2},...,C_{n}};

Step 2: Construct the initial direct influence correlation matrix;

K experts are invited to score the influence between the causal factors selected above. The 5-level grey language type of 0--4 is adopted. The influence is divided into five levels, and the expert scoring is transformed into a grey evaluation variable. The initial direct influence correlation matrix Z^{k} of the causal factor set is obtained by clarifying the grey evaluation variables. See Table 1.

The specific steps are as follows:(a) Standardize the grey evaluation variable^{21}, see Eq. (1):$$z=\frac{1}{N}\sum_{i=1}^{N}\left(\frac{1}{C}\sum_{i=1}^{N}\left(\frac{1}{C}\sum_{i=1}^{N}\left(\frac{1}{C}\right)\right)\right)$$

![img-0.jpeg](img-0.jpeg)

Figure 1. The safety early warning indicator system for metallurgical enterprises.


Table 1. Expert rating grey language scale.

$$ \begin{aligned} & \text { ㅇ } \bar{x}*{i j}^{k}=\left(\text { ㅇ } x_{i j}^{k}-\min \text { ㅇ } x_{i j}^{k}\right) / \Delta*{\min }^{\max } \ & \text { ㅇ } \bar{x}*{i j}^{k}=\left(\text { ㅇ } x_{i j}^{k}-\min \text { ㅇ } x_{i j}^{k}\right) / \Delta*{\min }^{\max },(i, j=1,2, \cdots, n) \ & \Delta*{\min }^{\max }=\max \text { ㅇ } x_{i j}^{k}-\min \text { ㅇ } x_{i j}^{k} \end{aligned} $$

where $k$ is the number of experts, $k=1,2,3, \ldots, \mathrm{n}, \otimes x_{i j}^{k}$ is the score value of the influence between the factor $C_{i}$ and $C_{i}, \otimes x_{i j}^{k}$ and $\otimes x_{i j}^{k}$ are the upper limit and lower limit of the grey interval variable, $\otimes \bar{x}_{i j}^{k}$ and $\otimes \bar{x}_{i j}^{k}$ are

the standard value of the upper limit and lower limit of the grey interval variable, $\Delta_{\min }^{\max }$ is the difference between the maximum upper limit and the minimum lower limit of the grey variable.
(b) Clear processing, see Eq. (2):

$$
Y_{i j}^{k}=\frac{\left\{\otimes \bar{x}_{i j}^{k}\left(1-\otimes \bar{x}_{i j}^{k}\right)+\left(\otimes \bar{x}_{i j}^{k} \times \otimes \bar{x}_{i j}^{k}\right)\right\}}{\left(1-\otimes \bar{x}_{i j}^{k}+\otimes \bar{x}_{i j}^{k}\right)}
$$

c. Calculate the clear value, see Eq. (3)

$$
Z_{i j}^{k}=\min \otimes x_{i j}^{k}+Y_{i j}^{k} \cdot \Delta_{\min }^{\max }
$$

where $Z_{i j}^{k}$ is the initial influence relation matrix $Z^{k}$ of the $k$ th expert.
Step 3: Calculate the weighted influence relation matrix $Z$, see Eq. (4)

$$
z_{i j}=\omega_{1} z_{i j}^{1}+\omega_{2} z_{i j}^{2}+\cdots+\omega_{k} z_{i j}^{k}
$$

where $z_{i j}$ is the element in the weighted influence relation matrix $Z, w_{i}$ is the expert weight ratio of the matrix element $z_{i j}$, and the sum of the expert weights is 1 .

Step 4: Calculate the standardized influence correlation matrix $C$, see Eqs. (5) and (6):

$$
\begin{gathered}
S=\frac{1}{\max _{1 \leq i \leq n} \sum_{j=1}^{n} z_{i j}},(i, j=1,2, \cdots, n) \\
C=S \cdot Z
\end{gathered}
$$

where $S$ is the reciprocal of the sum of the maximum row vectors in matrix $Z$.
Step 5: Calculate the comprehensive influence correlation matrix $T$, see Eq. (7)

$$
T=C(I-C)^{-1}
$$

where $I$ is the unit matrix.
Step 6: Calculate the influence degree $R_{i}$, the influenced degree $D_{i}$, the centre degree $P_{i}$, and the cause degree $E_{i}$ of each factor, and draw the cause-result figure. The calculation formulas are shown in (8)-(11).

$$
\begin{gathered}
R_{i}=\sum_{j=1}^{n} t_{i j},(i=1,2, \cdots, n) \\
D_{j}=\sum_{i=1}^{n} t_{i j},(i=1,2, \cdots, n) \\
P_{i}=R_{i}+D_{j},(i=j) \\
E_{i}=R_{i}-D_{j},(i=j)
\end{gathered}
$$

where $t_{i j}$ is the element in matrix $T$.
Step 7: Calculate the overall influence relation matrix $H$, see Eq. (12)

$$
H=I+T
$$

where $I$ is the unit matrix.
Step 8: Establish the reachable matrix $K$, which is obtained by Eqs. (13) and (14).

$$
\begin{gathered}
k_{i j}=\left\{\begin{array}{l}
1, h_{i j} \geq \lambda(i, j=1,2, \cdots n) \\
0, h_{i j}<\lambda(i, j=1,2, \cdots n)
\end{array}\right. \\
\lambda=\alpha+\beta
\end{gathered}
$$

where $k_{i j}$ is the element in matrix $K, h_{i j}$ is the element in matrix $H$.
The reachable matrix $K$ is calculated by the overall influence relation matrix $H$. If $k_{i j}=1$, the factor $C_{i}$ can affect the factor $C_{i}$ and if $k_{i j}=0$, the factor $C_{i}$ does not affect $C_{i}$. The element value of the reachable matrix $K$ is determined by the threshold $\lambda . \alpha$ is the variance of the comprehensive influence correlation matrix $T$, and $\beta$ is the standard deviation of the comprehensive influence correlation matrix $T$.

Step 9: According to the reachable matrix $K$, the hierarchical partition is carried out, and the multi-level hierarchical model diagram is drawn.

The reachable set *P_{i}* and the current set *Q_{i}* are calculated by formulas (15) and (16). If *P_{i}* = *P_{i}*∩*Q_{i}*, (*i*=1,2,...*n*), factor *C_{i}* is the bottom factor. The row and column of the Ci factor are deleted from the reachable matrix *K*, and the above operations are repeated to obtain a multi-level hierarchical model diagram between the factors.

$$P_i = \left{ c_j \left| c_j \in C, k_{ij} \neq 0 \right} \right},(i = 1, 2, \dotsb n) $$$$Q_i = \left{ c_i \left| c_i \in C, k_{ij} \neq 0 \right} \right},(i = 1, 2, \dotsb n)$$

### **Grey DEMATEL/ISM results and analysis**

### **Cause-result diagram**

Ten experts were selected for scoring, and the weight of each expert was 0.1. The influence degree *R_{i}*, the influenced degree *D_{i}*, the centre degree *P_{i}*, and the cause degree *E_{i}* of the safety accident-causing factors in metallurgical enterprises are calculated. The results are shown in Table 2. The Cartesian coordinate system is established according to the values of the centre degree and cause degree, and the cause-result figure of the safety accident-causing factors in metallurgical enterprises is drawn, as shown in Fig. 2.


**Table 2.** Influence degree *R_{i}*, influenced degree *D_{i}*, centre degree *P_{i}*, and cause degree *E_{i}* of each causal factor.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** The cause-result figure of the safety accident-causing factors in metallurgical enterprises.

The centre degree P_{i} represents the influence degree of each causal factor on the safety accident in metallurgical enterprises, that is, the larger the value of a centre degree is, the stronger influence the causal factor has. The centre degree is sorted from large to small as follows D4 > D3 > D1 > D2 > B5 > D5 > C1 > B4 > C5 > C2 > C3 > C4 > A2 > A3 > A5 > A4 > A1 > B3 > B1 > B2. The top six indicators by centre degree are the safety investment compliance rate (D4), the perfection of the safety production management system (D3), the regulatory agencies and personnel allocation (D1), the individual protection measures(D2), the completeness of fire prevention and firefighting facilities(B5), the improvement of emergency rescue mechanism (D5) which have an important impact on the safety accidents of metallurgical enterprises and should be focused on in the investigation and rectification of hidden dangers.

# Cause degree 

The cause degree represents the influence degree of the causal factor on other factors. The larger the value is, the greater the influence on other factors is. The cause degree is divided into two cases: causative factor $(E_{i}>0)$ and resultant factor $\left(E_{i}<0\right)$. The order of the causative factors from large to small is A3 > A5 > B3 > B2 > D5 > B1 $>$ B5 > C5. The employee violation rate(A3), the physical and mental health of employees (A5), the pass rate for equipment maintenance (B3), the qualification rate of special equipment (B2) these four factors are easy to affect other factors. The resultant factors are sorted according to the absolute value: A2 > A1 > D4 > C1 > D2 > A4 > D3 $>$ B4 > D1 > C4 > C3 > C2. The average monthly training time for employees (A2), the employee education level (A1), the safety investment compliance rate (D4), and the conformity of workspace arrangement (C1) are easily affected by other factors. The resultant factor is the result of the synergistic effect of various causative factors, which leads to the complexity of the safety state of metallurgical enterprises.

## Multi-level hierarchical model

The MATLAB software is used to divide the reachable matrix into levels, to construct the 3-order 6-layer hierarchical model of safety accidents in metallurgical enterprises, as shown in Fig. 3.

The neighboring causes are located in the first level of the ISM model, which includes the employee violation rate (A3), the hazardous substances reserves (B1), the toxic gas and dust pollution control compliance rate (C5), the pass rate for equipment maintenance (B3), and the qualification rate of special equipment (B2). These five causal factors are the most direct causes of safety accidents in metallurgical enterprises, which are the grass-roots causes and should be highly valued.

The transitional causes are located in the second to fifth levels of the ISM model, including the employee education level (A1), the employee technical level compliance rate (A4), the physical and mental health of employees (A5), the safety investment compliance rate (D4), the lighting compliance rate (C2), the noise control compliance rate (C3), the temperature and humidity regulation pass rate (C4), the toxic gas and dust pollution control compliance rate (C5), the average monthly training time for employees (A2), the completeness of fire prevention and firefighting facilities (B5), the conformity of workspace arrangement (C1), the hazardous substances reserves (B1), the improvement of emergency rescue mechanism (D5), and the regulatory agencies and personnel allocation (D1). These factors play a role in connecting the essential cause and the neighboring cause and are the indirect factors that lead to accidents. They are mostly management causes, which play a connecting role in the interaction between the causes of the physical level, the grass-roots level, and the government level.

The essential cause is located in the sixth level of the ISM model, including the perfection of safety production management system (D3) which is a deep-seated cause factor and can affect the neighboring cause factors by affecting the transitional cause factors. It is the cause of government level and has strong influence and control on the middle order, management level, and grass-roots level. The perfection of the safety production management system (D3) is the basis and key to ensuring the safety production of metal smelting enterprises, and it is also the basis for ensuring the smooth implementation of emergency management in metallurgical enterprises. Based on the supervision and management system of metallurgical enterprises, the risk management evaluation mechanism should be constantly improved and the emergency management system should be strengthened.

## Safety accident early warning model of metallurgical enterprises based on Bayesian network

## Construction of Bayesian network

The early warning of enterprise safety accident risk is to analyze and evaluate the factors affecting enterprise safety comprehensively and to predict and alarm the possible accident risk ${ }^{22}$. The difficulty of early warning lies in the complexity and uncertainty of risk factors. Bayesian network can reason about uncertain information and has great advantages in solving the faults caused by the uncertainty and relevance of complex problems. It is often used to study and solve uncertain problem ${ }^{23}$. Based on the correlation analysis of the above accident-causing factors, the Bayesian network early warning model is constructed and applied to the safety inspection of the Fuxin Jiuxing Titanium work site for example verification. To avoid data errors caused by different indicator dimensions, the inspection data is normalized as a 'minimal' indicator and transformed into standardized data between $[0,1]$. The membership function of minimal indicators ${ }^{24,25}$ is shown in Eq. (17).

$$
u(x)= \begin{cases}1 & x \geq x_{\max }-1 \\ \frac{x_{\max }-x_{\min }}{0} & x_{\min } \leq x<x_{\max } \\ 0 & x<x_{\min }\end{cases}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. Multi-level hierarchical model of safety accident-causing factors in metallurgical enterprises.

The setting of warning alertness is shown in Table 3. The data on safety accident-causing factors of metallurgical enterprises are discretized. According to "Technical Standard for Safety Production Early Warning System of Enterprises in Metallurgy and Other Industrial and Trade Industries (Trial)" (General Office of Safety Supervision No.4 [2014] No.63)26 the early warning level is divided into five levels. The national standard and production process requirements are taken as the initial warning threshold which is adjusted after the enterprise runs for some time.

The construction procedures of the Bayesian network are as follows:

(1) Establish a network topology27. The multi-level hierarchical model based on grey DEMATEL/ISM correlation analysis is transformed into each node of the Bayesian network structure, and the Bayesian network is constructed according to expert knowledge and internal causal relationships.


Table 3. The setting of warning alertness.

(2) Define the node state. Taking the national standard and production process requirements as the early warning threshold, each node has five states.
(3) Determine the structural parameters. Find the optimal network structure by using machine learning and setting a threshold. And further, improve the Bayesian network structure through Bayesian inference, and then the conditional probability between variables is determined ${ }^{28}$. Finally, the Bayesian network structure is obtained as shown in Fig. 4.

## Safety accident early warning example of metallurgical enterprise

According to the threshold of each early warning state obtained in Table 3, the inspection data of the Jiuxing Titanium work site are discretized, and the numbers $1,2,3,4,5$ are used to represent the risk state level of causal factors. Based on statistical data, the Bayesian network model of safety accidents in metallurgical enterprises is used for parameter learning. The data saved in Excel software is imported into Access software to establish the Open Database Connectivity (ODBC)database. The ODBC data is imported into GeNle2.0 software to match with the safety early warning Bayesian network diagram of metallurgical enterprises.

The maximum likelihood estimation method is used to learn the parameters of the Bayesian network model of safety accidents in metallurgical enterprises ${ }^{29}$, and the conditional probability distribution diagram of each cause factor is obtained, see Fig. 5. The probabilities of the warning alertness node are: safe state (State = 1) is $25 \%$, comparatively safe state(State $=2$ ) is $16 \%$, attention state (State $=3$ )is $26 \%$, warning state (State $=4$ )is $16 \%$, dangerous state(State $=5$ )is $16 \%$. It shows that the attention state has the highest probability which is $26 \%$, and the lowest probability of State $2,4,5$ is $16 \%$. The risk expectation value is used to measure the accident level. In the calculation of the risk expectation value of the Jiuxing Titanium work site, State $1=10 \%$, State $2=30 \%$, State $3=10 \%$, State $4=30 \%$, and State $5=20 \%$. The accident level and early warning signal are determined according to the risk expectation value. The risk expectation probability of the recent accident of the Jiuxing Titanium Material (Fuxin) Co., Ltd. is $10 \% \times 25 \%+30 \% \times 16 \%+10 \% \times 26 \%+30 \% \times 16 \%+20 \% \times 16 \%=17.9 \%$. The risk expectation result is in a comparatively safe state (State2). Based on the field data of the example, Analytic Hierarchy Process (AHP) and fuzzy comprehensive evaluation method are applied to obtain the early warning level of the enterprise as state2. The comparison between the two methods shows that the early warning level is consistent, which indicates the feasibility and accuracy of the Bayesian early warning model. The Bayesian model not only gives the quantified value of the accident risk probability, but also gives the probability quantified value of the five early warning states of each indicator. At the same time, the causal relationship and conditional correlation
![img-3.jpeg](img-3.jpeg)

Figure 4. Structure of optimized Bayesian network.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** Node probability of Bayesian network for the Jiuxing titanium work site early warning.

relationship between each indicator variable are included in the reasoning process, which can provide more targeted guidance for the formulation of preventive measures.

# Conclusions

In this paper, the grey DEMATEL-ISM method is used to establish the correlation analysis model of accident-causing factors, clarify the relationship and action path among them, divide the factors into different levels, establish a multi-level hierarchical structure model, and build a metallurgical enterprise accident early warning model based on Bayesian network. The main conclusions are as follows:

1. According to the centre degrees ranking of early warning indicators, the degree of influence of all early warning indicators on safety accidents in metallurgical enterprises is obtained. The top six indicators are the safety investment compliance rate (D4), the perfection of the safety production management system (D3), the regulatory agencies and personnel allocation (D1), the individual protection measures (D2), the completeness of fire prevention and firefighting facilities (B5), the improvement of emergency rescue mechanism (D5). In the process of safety risk classification control of metallurgical enterprises, the above factors should be the focus of accident hidden danger investigation.

2. Based on grey DEMATEL/ISM, a 3-order 6-layer hierarchical model of safety accident-causing factors in metallurgical enterprises is constructed, and the essential cause, transitional cause, and neighboring cause of the accident are clarified. The employee violation rate (A3), the hazardous substances reserves (B1), the toxic gas and dust pollution control compliance rate (C5), the pass rate for equipment maintenance (B3), and the qualification rate of special equipment (B2) are neighboring causes, are the most direct causes of safety accidents in metallurgical enterprises. In the process, monitoring should be strengthened. The perfection of the safety production management system (D3) is the essential cause, and it is the basis and key to ensuring the safety production of metallurgical enterprises.

3. The risk early warning model is obtained by combining the 3-order 6-layer hierarchical model of the accident-causing factors with the Bayesian network. The risk expectation probability of the accident in the Jiuxing Titanium Material (Fuxin) Co., Ltd. is calculated to be 17.9% by using the model. The risk expectation result is in a comparatively safe state (State2). The results obtained by the Bayesian model are consistent with those obtained by AHP and fuzzy comprehensive evaluation method, which indicates that this early warning model is feasible. The Bayesian model can give the risk probability value of the accident and the risk probability value of the accident cause factors at the same time, and include the causal relationship and conditional correlation relationship among the indicator variables in the reasoning process, which can provide targeted technical support for the construction of the emergency system of risk classification management and control.

The establishment of the early warning model is aimed at the macro level of enterprise production. The next step can be aimed at each production process in the enterprise, and the essential characteristics of the alarm source and the crisis are analyzed in depth, and a detailed early warning index system and early warning model

are established to provide more detailed and more operable risk prevention and control measures for the construction of the risk classification management and control emergency system.

# Data availability 

The data that support the findings of this study are available from the corresponding author upon reasonable request.

Received: 10 May 2024; Accepted: 29 July 2024
Published online: 07 August 2024

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (Project No. 52374203, 52174183).

## Author contributions

Y.M.H., Conceptualization, Methodology, Formal analysis, Writing-original draft, Editing. J.J.Z., Conceptualization, Methodology, Funding acquisition. C.Y.N., Investigation, Data curation, Visualization. All authors have read and agreed to the published version of the manuscript.

# Competing interests 

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to J.J.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024