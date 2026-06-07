# Risk Assessment of Unsafe Acts in Coal Mine Gas Explosion Accidents Based on HFACS-GE and Bayesian Networks 

Lixia Niu (1), Jin Zhao * (1) and Jinhui Yang (1)

School of Business and Management, Liaoning Technical University, Huludao 125105, China

* Correspondence: zhaojin96@outlook.com; Tel.: +86-157-3318-1336


#### Abstract

Even in the context of smart mines, unsafe human acts are still an important cause of coal mine gas explosion accidents, but there are few models to analyze unsafe human acts in coal mine gas explosion accidents. This study tries to solve this problem through a risk assessment method of unsafe acts in coal mine gas explosion accidents based on Human Factor Analysis and Classification system (HFACS-GE) and Bayesian networks (BN). After verifying the reliability of HFACS-GE framework, a BN model of risk factors of unsafe acts was established with the Chi-square test and odds ratios analysis. After reasoning analysis, risk paths and key risk factors of unsafe acts were obtained, and preventive measures were granted. Based on the analysis of 100 coal mine gas explosion cases, the maximum probability of five kinds of unsafe acts of employees is $38 \%$. Among the 22 risk factors, the mental state of employees has the greatest influence on the habitual violation of regulations, and the sensitivity value is $12.7 \%$. This study can provide technical assistance for the risk management of unsafe acts in coal mine gas explosions.


Keywords: coal mine gas explosion; human factors; unsafe acts; HFACS framework; Bayesian network

## check for updates

Citation: Niu, L.; Zhao, J.; Yang, J. Risk Assessment of Unsafe Acts in Coal Mine Gas Explosion Accidents Based on HFACS-GE and Bayesian Networks. Processes 2023, 11, 554. https://doi.org/10.3390/ pr11020554

Received: 21 January 2023
Revised: 6 February 2023
Accepted: 9 February 2023
Published: 10 February 2023

## 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

## 1. Introduction

Bringing coal mine wisdom into the coal industry creates new vitality but also brings new challenges. In recent years, the more complex operation procedures of smart mines and the inherent bad working environment of coal mines have made the coal mining industry more dangerous [1,2]. Coal mine gas explosion (i.e., coal seam gas explosion) accidents are one of the most serious disasters in coal mine accidents, which not only destroy underground roadways and coal machine equipment but also cause huge economic losses to enterprises and lead to many casualties. China, the world's largest coal producer, proposed the construction of smart mines in 2008 and made great efforts to build them [3]. However, from 2015 to 2020, 642 people died due to coal mine gas explosions in China, accounting for $26.6 \%$ of the death tolls in coal mine accidents [4]. Of the 578 people who died of underground coal mine accidents in Turkey from 2010 to 2017, $68.34 \%$ died of gas explosion-related disasters [5]. In Poland, severe gas explosions accounted for half of all coal mine accidents during the period [6]. Some studies indicate that traditional coal mine accident prevention methods have no room for improvement in safety performance, and modern analytical methods are urgently needed [7]. Therefore, in the context of global smart mine construction, it is of great significance to study the causes of coal mine gas explosion accidents to prevent gas explosions, reduce losses of coal mine enterprises, and protect workers' life safety.

At present, many scholars have studied the causes of coal mine gas explosion accidents from different angles. Patterson et al. systematically analyzed the occurrence rules of 508 coal mine accidents in Australia [8]. Due to the complex and diverse factors leading to gas explosion accidents, Cioca summarized the causes of gas explosion accidents from the aspect of methane-air mixing and ignition sources [9]. Li et al. believes that we should take the analysis of the case information of gas explosion accidents as the starting point

to explore the characteristics of the accident [10]. Zayed et al. [11] calculated the risk R coefficient through the analytic hierarchy process, and verified the accuracy of the results with practical cases. Based on the BN, Li et al. and Shi et al. quantitatively assessed the risk of coal mine gas explosions and pointed out that fan failure and electrical failure were important risks [12,13]. All the above papers believe that the occurrence of coal mine gas explosion accidents is often caused by multiple dangerous factors, and the interaction of various dangerous factors makes the accident intensity greater.

Coal mine gas explosion needs three basic conditions; the gas volume fraction within the explosion limit (5-16\%), a high-temperature ignition source with enough energy (650$750^{\circ} \mathrm{C}$ ), and an oxygen volume fraction of not less than $12 \%$. According to the relevant regulations of mine ventilation in China, the oxygen volume fraction in the underground air of a coal mine must be above $20 \%$ to meet the oxygen volume fraction conditions of a gas explosion. Therefore, whether the gas volume fraction and high-temperature ignition source reach the critical value directly affects the occurrence of gas explosion accidents. The gas accumulation and high-temperature ignition source are mainly caused by human factors. Previous studies have also confirmed that human factors are important causes of coal mine gas explosion accidents; among them, human factors account for about 85 percent of all coal mine accidents in the United States [14]. Chen et al. studied China's major coal mine accidents in 1980 and 2000 and found that human factors accounted for $97.67 \%$ of the causes of the accidents. Human factors also play an important role in coal mine gas explosion accidents [15]. According to Wang's research, $88 \%$ of coal mine gas explosion accidents were caused by human factors [16]. Yin et al. collected data on 231 gas explosions, all of which were deemed "human-factor accidents" and concluded that they could have been prevented with proper safety practices [17]. Therefore, the analysis of unsafe acts in coal mine gas explosion accidents is of great significance to preventing coal mine gas explosions and improving the safety level of coal mine production.

A HFACS framework has been established for human factor analysis of aviation safety accidents. Dekker pointed out that HFACS is a powerful tool for human factor analysis of accidents [18]. However, the standard HFACS framework is not perfectly applicable to the coal field [19]. For example, Lennè et al. [20] used the HFACS framework to analyze 263 major coal mine accidents in Australia from 2007 to 2008 and found that the violation factors by humans accounted for $61.6 \%$. Patterson et al. [8] analyzed 508 coal mine accidents in Australia from 2004 to 2007 by using the HFACS framework and found that the factor of human violation accounted for only $6.5 \%$. Although this difference is influenced by different statistical methods and analysis processes, it also reflects the poor applicability and strong subjectivity of the standard HFACS framework in the human factor analysis of coal mine accidents.

To solve this problem, this study collates relevant literature on coal mine gas accidents, collecting 100 typical cases of gas explosion accidents from 2002 to 2020 in China, the world's largest coal-producing country, and constructs a list of unsafe acts of coal mine gas explosion accidents, including 22 factors. Based on this, the HFACS framework is improved, and established a human factor analysis and classification system for the gas explosion (HFACS-GE) framework that is more suitable for human factor analysis of coal mine gas explosion is proposed, and the detailed risk factors identification is carried out. Considering the trend of intelligent coal mine construction, $68 \%$ of the collected cases occurred after the construction of smart mines. In order to ensure the reliability of the HFACS-GE framework, the reliability of the model is verified by the scorer reliability, which takes the consistency of frequency statistics as the verification index. Then, based on the HFACS-GE framework, the frequency statistics of the accident cases were carried out, and the Chi-square test and odds ratios analysis were used to construct the BN structure. In GeNIe software, the BN was drawn, the main induced path of each human risk factor was obtained through backward reasoning, and the sensitivity factor of each human risk factor was obtained through sensitivity analysis. Finally, based on the analysis results, put forward targeted risk control measures. In this study, the unsafe acts in coal mine gas

explosion accidents are evaluated, and the evaluation results provide a technical reference for the management of unsafe acts in coal mine gas explosion accidents.

# 2. Methods 

### 2.1. HFACS

HFACS is based on the Swiss cheese model and is widely used in aviation accident investigation [21,22]. The HFACS framework is shown in Figure 1. HFACS framework divides human factors into four levels: unsafe acts, prerequisite of unsafe acts, unsafe supervision, and organizational influences. In practice, the HFACS framework can be modified based on expert knowledge and actual situation, and human factors at all levels can be adjusted accordingly, which has great flexibility [23]. For example, Feng et al. analyzed coal mine accidents based on the HFACS framework by taking geological conditions and government regulation as external factor levels [24]. Li et al. [25] added inadequate legislation, design flaws, and social factors to supplement the HFACS framework to evaluate unsafe acts in university laboratories.
![img-0.jpeg](img-0.jpeg)

Figure 1. The HFACS framework.

### 2.2. Bayesian Network

The Bayesian networks were originally developed by the US Federal Aviation Administration (FAA) and NASA in the 1980s to assess safety risks in aviation systems [26]. The BN is a graphical model that describes the dependency relationship between data variables [27]. It can realize causal analysis, statistical analysis and prediction, and even in the case of incomplete data, it can still realize the above functions, which have strong practicability [25]. In the coal field, BN are often used for mine risk management. Therefore, the BN is used as a human error analysis method for coal mine gas explosion accidents. Formula (1) shows the principle of BN, namely joint probability distribution and conditional independence.

$$
\mathrm{P}(\mathrm{X})=\mathrm{P}\left(\mathrm{X}_{1}, \mathrm{X}_{2}, \cdots, \mathrm{X}_{n}\right)=\prod_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{P}\left(\mathrm{X}_{\mathrm{i}} \mid \operatorname{Parent}\left(\mathrm{X}_{\mathrm{i}}\right)\right)
$$

$\operatorname{Parent}\left(\mathrm{X}_{\mathrm{i}}\right)$ is the parent set of the variable $\mathrm{X}_{\mathrm{i}}$.
Another characteristic of BN is that the prior probabilities of variables can be dynamically updated. Set the new node evidence of the variable, and obtain the posterior probability of the variable as follows:

$$
\mathrm{P}\left(\mathrm{X}_{1}, \mathrm{X}_{2} \cdots \mathrm{X}_{\mathrm{n}} \mid \mathrm{U}\right)=\frac{\mathrm{P}(\mathrm{X}, \mathrm{U})}{\mathrm{P}(\mathrm{U})}=\frac{\mathrm{P}(\mathrm{X}, \mathrm{U})}{\sum_{\mathrm{X}} \mathrm{P}(\mathrm{X}, \mathrm{U})}
$$

2.3. Index Consistency Test

The reliability test is usually carried out after the model is established. Ergai et al. [28] concluded through experiments that the reliability of HFACS framework could be verified by rater reliability. A common measure is the percentage agreement among raters, that is, the number of results obtained by independent raters when analyzing the same data. When the agreement is higher than $70 \%$, the model used is considered reliable [29]. Considering the feasibility of the study, the reliability evaluation method of scorer for the cause of traffic line accidents proposed by Li et al. [30] in 2019 and Liu [29] in 2022 was referred to, and the consistency of the index for effectiveness evaluation of qualitative classification model proposed by Ross et al. based on frequency statistics was used as the verification index [31]. The calculation process is as follows:

$$
I O C=\frac{Y}{Y+Z}
$$

where $I O C$ is the consistency of indicators, $Y$ is the same number of judgment results between two raters, and $Z$ is the different number of judgment results. When $I O C \geq 70 \%$, it indicates that the HFACS framework has good rater reliability and high reliability.

# 3. Unsafe Acts Risk Analysis Process of Coal Mine Gas Explosion Accident 

### 3.1. Analysis Process

In order to improve the effectiveness and reliability of the risk assessment of unsafe acts in coal mine gas explosions, a new method based on the HFACS-GE framework and BN is proposed. The analysis process of this method is shown in Figure 2. The first step is to improve the traditional HFACS framework, obtain the HFACS-GE framework, identify and classify the unsafe act factors leading to coal mine gas explosion accidents, and test the reliability of the HFACS-GE framework. The second step is to construct the BN, calculate the BN parameters by accident frequency statistics, determine the structure of the BN by the Chi-square test and odds ratios analysis, and then use the BN model for reasoning analysis to get the risk path of unsafe acts and key risk factors. The third step is to formulate corresponding preventive measures according to the analysis results in achieving the purpose of risk control.
![img-1.jpeg](img-1.jpeg)

Figure 2. Unsafe acts risk analysis process of coal mine gas explosion accident.

# 3.2. The Construction of HFACS-GE Framework 

### 3.2.1. Improved HFACS Framework

The object of this study has the following differences from the aviation field that the standard HFACS framework is oriented to.

- In the coal field, the government plays an important role in the occurrence of accidents. After analyzing nearly 90 major coal mine accidents in China between 2012 and 2021, Wang found that more than 500 administrative officials in charge of safety were punished [32]. Siu found through research that government departments can effectively control coal mine gas explosion accidents by fulfilling their own regulatory obligations and strengthening the supervision of coal mine production [33].
- Enterprise managers play a small role in the occurrence of aviation accidents, so the HFACS framework does not consider the factors of enterprise management. In coal enterprises, managers directly participate in production by issuing production orders and dispatching, and their mistakes may cause huge accidents [34,35].
- Although the HFACS framework analyzes the causes of accidents from the four aspects of human, machine, environment, and management, its core is a system to analyze human errors, and the study of enterprise management is not comprehensive enough [19]. The Broad causal chain model of accidents has confirmed that management defects are important factors causing accidents. In coal enterprises, the expression of management errors is more abundant. For example, an imperfect safety management system will cause chaos in the production process, and inadequate safety training will make the employees lack self-rescue knowledge, which can lead to the occurrence or aggravation of accidents.
- Although the HFACS framework analyzes the factors that cause accidents, it does not elaborate on these factors or explain their manifestations. When different people analyze with the help of the model, the analysis results are likely to be very different. Especially in the coal mining field, gas explosion accidents are highly irregular, and there are many factors leading to gas explosion accidents, so the original HFACS framework cannot be well-applied.
Therefore, this study selected 100 typical cases of coal mine gas explosions published by the Chinese government from 2002 to 2020, analyzing the unsafe acts among the accidentcausing factors and improving the HFACS framework by combining it with the studies of other scholars [19,32]. The HFACS-GE frame is obtained, as shown in Figure 3. Compared with the original framework, the new framework highlights government factors, including the impact of policies on the accident and whether the government's supervision is in place. The new framework classifies organizational influences in more detail, and modifies organizational influencing factors from 3 to 6 , and also takes into account the influence of managers and divides the human factor into the manager factor and the operator factor.


### 3.2.2. Manifestations of the Causes of Unsafe Acts

HFACS-GE framework is summarized into four aspects: government dereliction of duty, organizational influence, prerequisites of unsafe acts, and unsafe acts, including 22 factors, as shown in Table 1.

![img-2.jpeg](img-2.jpeg)

Figure 3. The HFACS-GE framework.

Table 1. Classification categories of risk factors.


Table 1. Cont.


Table 1. Cont.


# 3.2.3. Verifying the Reliability of the HFACS-GE Framework 

Banuls et al. suggested that when the number of nodes in a BN is above medium, at least three experts should be selected in the evaluation [36]. Therefore, this study invited four coal mining industry researchers and practitioners to evaluate the reliability of the HFACS-GE framework. First of all, four evaluators were trained in the relevant contents of the model so that they could master the classification, definition and application methods of factors in the model. Then, a detailed description of the accident process is selected from 100 accident cases for the evaluator to analyze. The evaluator information is shown in Table 2.

Table 2. Information of selected evaluators of the reliability of HFACS-GE framework.


Consistency calculation is carried out on the evaluator's analysis results, and the results are shown in Table 3.

Table 3. Reliability test results of the HFACS-GE framework.


It can be seen from Table 3 that the total reliability of HFACS-GE framework evaluators reaches $82.79 \%$, greater than $70 \%$, and the reliability of all factors is greater than $70 \%$, indicating that the model has a good consistency and high reliability, which is suitable for the construction of BN and the analysis of the causes of unsafe acts in the following paper. At the same time, it can be seen that the evaluators with long working years and a high degree of professional correlation have good consistent results. Evaluator 3, with the shortest working time and the lowest degree of professional relevance, has the lowest consistency with the other three, which indicates that the user needs a high degree of professional relevance and a certain number of years of work.

# 3.3. Formatting of Mathematical Components 

### 3.3.1. Verifying the Reliability of the HFACS-GE Framework

The BN structure must be determined first to establish the BN model. The purpose of BN structure learning is to determine the correlation between each node so as to obtain the corresponding network structure. This study will jointly determine the frequency of factors causing unsafe acts in coal mine gas explosion accidents by combining accident case analysis and expert experience and then carry out a Chi-square test and odds ratios analysis to determine the correlation among all factors.
(1) Frequency statistics of unsafe acts in coal mine gas explosion accidents

At present, the investigation report of coal mine gas explosion accidents is mostly based on the identification of responsibility, and few investigations analyze and investigate the deep factors leading to the accident, so it is difficult to make statistics on the frequency of the deep factors of accidents.

Therefore, this study adopts the method of combining data statistics and expert judgment to conduct frequency statistics on the factors causing unsafe acts in accidents. Combined with expert judgment, the statistical results of 100 accident reports based on the HFACS-GE framework, are shown in Table 4.

Table 4. Risk factor frequency statistics table.


# (2) Chi-square test and odds ratios analysis 

A Chi-square test is used to analyze whether there is a causal relationship between the upper and lower levels of the HFACS-GE framework and whether the causal relationship is significant, and the correlation between the factors between the upper and lower levels is analyzed by the odds ratios [37].

It is assumed that $\mathrm{H}_{0}$ has no correlation between the upper variable and the lower variable, that is, there is no significant causal relationship between the unsafe acts factors at the upper and lower levels of HFACS-GE coal mine gas explosion accident. $\mathrm{H}_{1}$ indicates that the upper-layer variable is associated with the lower-layer variable. When $p$-value is less than 0.05 , the hypothesis that the upper variable of $\mathrm{H}_{0}$ has a significant causal relationship with the lower variable is rejected. Then, the compromise ratios are used to analyze whether the occurrence of variables at the upper level of the HFACS-GE frame will cause the change in the occurrence probability of variables at the lower level. When the odds ratio (OR) value is greater than 1 , it means that the occurrence of the upper variable will increase the possibility of the occurrence of the lower variable.

After calculation, the results of $p$-values and OR values that meet the requirements are shown in Table 5.

Two factors at different levels of correlation relationship can be used as nodes of BN. After consulting expert opinions on the results, the BBN model of unsafe acts in coal mine gas explosion accidents is constructed, as shown in Figure 4.

Table 5. Chi-square test and OR values statistics table.


![img-3.jpeg](img-3.jpeg)

Figure 4. Initial BN model for unsafe acts in gas explosion accidents.

# 3.3.2. Determination of the Network Parameters 

In the past, the probability of Bayesian nodes was often determined by expert experience, which is subjective to a certain extent [25]. The parameters in this study are derived from the statistics of the frequency of each risk factor.

As can be seen from the structure diagram of the BN, there are five root nodes: safety supervision is inadequate, insufficient crackdown on illegal activities, poor supervision of work safety, contingency measure factors, and illegal command. The prior probability

tables of the five root nodes is shown in Table 6, where "State0" means that the factor does not occur, and "State1" means that the factor does occur.

Table 6. Probability of five root nodes.


Given the value of the parent node of the risk factor, the probability of occurrence of different values of the node are calculated and taken as the conditional probability of the node. Assume that each of the risk factors have only two states, namely non-occurrence (State $=0$ ) and occurrence (State $=1$ ). Taking perceptual errors as an example, the frequency statistics and the CPT of the node are shown in Table 7. The conditional probability of BN obtained through calculation is shown in Table 8.

Table 7. Perceptual errors frequency statistics and conditional probability table.

|  Illegal
Command |  |  | State0 | State1 | Illegal
Command |  | State0 | State1  |

Table 8. Conditional probability table.

Parent
Node | Value | Probability | Nodes | Values | The
Parent
Node | Values | Probability | Nodes | Value | The
Parent
Node | Values | Probability  |

## 4. Results and Discussions

This chapter analyzes BN reasoning based on GeNle software developed by the Decision Systems Laboratory of the University of Pittsburgh [25]. The B BN parameters were imported into GeNle software, and the results are shown in Figure 5.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** BN model of unsafe acts in gas explosion accidents based on GeNle.

### 4.1. Causal Induction

According to the reasoning results shown in Figure 5, in coal mine gas explosion accidents, in the level of unsafe acts, the occurrence probability of habitual violations is the highest, which is 38%. In addition, the incidence of accidental violations was 15%, skill-based errors 10%, decision errors 8%, and perceptual errors 11%. Companies should pay more attention to violations. Specifically, at the level of government negligence, the incidence of safety supervision is inadequate, 50%; at the level of organizational influences, the security management confusion is the highest, 72%; at the level of preconditions for unsafe acts, organized production in violation of laws and regulations and illegal command is 49% and 40%, respectively. The above factors should be paid attention to and controlled through appropriate measures to reduce the occurrence of unsafe acts in gas explosion accidents.

### 4.2. Reverse Inference

Based on the established BN model, the occurrence probability of other network node factors can be deduced when each unsafe act leads to the occurrence of an accident, so as determining the main risk path of the unsafe acts according to the probability, so as pointing out the direction of accident prevention. Set the node state of skill-based errors, decision errors, perceptual errors, habitual violations, and accidental violations to "state1 = 100%", indicating that the unsafe acts factor occurs. If "state1 = 0%" is set to other nodes at this layer, no other nodes occur. The results of BN reverse reasoning are obtained after updating, as shown in Table 9.

Among them, the most likely causal chain leading to skill-based errors is illegal command → skill-based errors. The most likely causal chain leading to decision errors is safety supervision is inadequate → security management confusion → organize production in violation of laws and regulations → decision errors. The most effective causal chain leading to perceptual errors is illegal command → perceptual errors. The most likely causal chain leading to habitual violations is safety supervision is inadequate → safety education and training → mental states → habitual violations. The most likely causal law that leads to accidental violations is safety supervision is inadequate → Security management confusion → organize production in violation of laws and regulations → accidental violations.

Thus, it can be seen that the most fundamental factors leading to the occurrence of human risk factors in coal mine gas explosion accidents is where illegal command and safety supervision is inadequate, indicating these should be paid more attention.

Table 9. Summary of main induced paths of unsafe acts.


# 4.3. Sensitivity Analysis 

Sensitivity analysis is a technique used to study the effect of small changes in numerical parameters on output parameters. Parameters with high sensitivity have a more significant influence on inference results. Skill-based errors, decision errors, perceptual errors, habitual violations, and accidental violations are taken as target nodes in turn. By comparing the sensitivity coefficient of associated nodes, their influence degree on target nodes is obtained to determine the key influencing factors leading to the occurrence of target nodes. The sensitivity coefficient distribution obtained is shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Sensitivity analysis result.
As can be seen from Figure 6, when skill-based errors are the target node, illegal command, and the technical environment are highly sensitive points, while others are low sensitive points. This means that illegal command and a poor technical environment are most likely to lead to the skills of front-line miners. When decision errors are the target node, the technical environment and illegal command are highly sensitive points.

When the perceptual errors are the target node, the illegal command is highly sensitive. The illegal command is easy to disrupt the original work plan of front-line miners, and miners are prone to deviation in their perception of work, resulting in perceptual errors. When habitual violations are the target node, the mental states are highly sensitive. A poor mental state is manifested as a lack of safety awareness, crisis awareness, and vigilance of front-line miners, which is the most likely to cause habitual violation of regulations. When the accidental violations of regulations are the target node, the organized production in violation of laws and regulations is highly sensitive. The regulators should put more energy into cracking down on illegal and illegal behaviors so as to avoid the occurrence of illegal and illegal production organization.

# 4.4. Risk Control Strategy 

Based on the above analysis of the occurrence probability, causality analysis, reverse reasoning, and sensitivity of risk factors in the accident, major unsafe acts in coal mine gas explosion accidents are classified and summarized in the above ways, and 10 major risk factors are obtained, as shown in Table 10.

Table 10. Summary of major risk factors.


Among the five kinds of unsafe acts in the HFACS-GE framework, the occurrence probability of habitual violation is the largest, which is $38 \%$, and the sensitivity value of employees' mental state to habitual violation is the largest, which is $12.7 \%$. Therefore, more attention should be paid to employees' mental state, character, interests, and abilities when hiring employees. At work, we should put an end to fluke, cheating, trying to be brave, risk psychology, etc., strengthen the supervision and training of employees' mental state, and prevent habitual violations.

The five kinds of unsafe acts are divided into human errors and human violations. The probability of employee violations is $53 \%$, much higher than the probability of employee mistakes. Among them, the main inducing path of habitual violations is as follows: the government safety supervision is inadequate $\rightarrow$ the organization of safety education and training are insufficient $\rightarrow$ the employee's mental state $\rightarrow$ the employee's habitual violation. The main inducing path of employees' accidental violations is as follows: the government's safety supervision is inadequate $\rightarrow$ the organization's security management confusion $\rightarrow$ managers violate laws and regulations to organize production $\rightarrow$ employees' accidental violation. It can be seen that the government's safety supervision plays an important role in the occurrence of coal mine gas accidents. The government should strictly implement the rules and regulations, timely investigate safety hazards, crack down on illegal mining

behaviors, assign production tasks in line with coal mine production capacity, and give guidance and coordination to coal mines within the jurisdiction. For the organization, on the one hand, to eliminate the chaos of safety management, strengthen the management of mechanical and electrical equipment, mine ventilation, blasting equipment, and gas detection. On the other hand, the management of employee labor relations and labor tasks should be strengthened, and full-time inspectors should be arranged to supervise employees before they enter the mine and when they work. At the same time, all kinds of coal mines data should be tested and recorded truthfully, and dangerous information should be reported to enterprises and the government in a timely manner. Finally, regular safety training, emergency drills, and retraining should be conducted for managers, special operators (such as gas inspectors, gunners, etc.), and front-line operators. For managers, they should prevent the failure to implement the orders of government departments and organizations, not to conceal the real situation of coal mines, and not to give informal production instructions to employees. For employees, they should always pay attention to their own mental state and prevent habitual violations. Strictly abide by rules and regulations to prevent the occurrence of accidental violations.

# 5. Research Limitations and Future Prospects 

This paper puts forward a risk assessment model for the unsafe acts of coal mine gas explosions. After verifying the reliability, the feasibility of the model is verified through the analysis of 100 accidents, but there are still some limitations. First of all, although the number of gas explosion accidents is decreasing year by year, the number of samples in this study still has room to increase. Secondly, due to the setting of the standard HFACS framework, the model proposed in this paper only studies the relationship between adjacent levels, which has limitations on the study of cross-level factors. Finally, with the continuous construction of smart mines around the world, the causes of coal mine gas explosion accidents will have structural changes, which will also affect the unsafe acts of people in accidents, which may make the results of this study not applicable to all coal mine types.

Our subsequent research will focus on obtaining more data on coal mine gas explosion accidents to solve the problem of insufficient sample size; Secondly, the correlation between non-adjacent levels in the HFACS framework is studied to expand the application of the HFACS framework. Finally, we will study the unsafe acts of people in coal mines of different types and degrees of intelligence to make the research results universal. In addition, we will also combine the application of EEG experiments and machine learning to further obtain data of the physical and mental states of front-line miners, expand the human factor, and optimize the application of human risk factor research in the field of coal mine safety management.

## 6. Conclusions

Based on the coal mine gas explosion accident, this study improved the HFACS framework, analyzed the unsafe acts in coal mine gas accidents in detail from the four levels of government dereliction of duty, organizational influence, the premise of unsafe acts and unsafe acts, determined the main risk factors of unsafe acts, and tested the reliability of the framework. On this basis, combined with 100 cases of gas explosion accidents in coal mining enterprises in China, the causal relationship between different levels is determined by using the Chi-square test and concession ratios analysis, and the BN model of unsafe acts in coal mine gas explosion accidents is constructed. Risk assessment of unsafe acts in coal mine gas explosion accidents is carried out from the three aspects of causality analysis, reverse reasoning analysis, and sensitivity analysis. Finally, according to the assessment results, risk prevention and control measures are proposed for different responsible subjects.

This study uses the BN method to calculate the probability distribution of unsafe acts in coal mine gas explosion accidents in order to provide human factors risk prevention measures for Chinese coal mine enterprises. Through the model reasoning analysis, it

is known that the probability of employees violating regulations is greater than that of employees making mistakes. Among them, the probability of habitual violation is $38 \%$, and the reverse reasoning results show that mental state is the most likely factor to cause habitual violation. The most likely causal chain of habitual violations is (Safety supervision is inadequate $\rightarrow$ Safety education and training $\rightarrow$ Mental states $\rightarrow$ Habitual violations). The factors that have a great influence on the violation of regulations include inadequate government safety, insufficient organization of safety education and training are not enough, the organization of safety management disorder, the management of illegal production and the mental state of employees. Government safety supervision is inadequate is the main factor leading to unsafe acts. The results of sensitivity analysis show that bad mental states and lack of safety education and training have the greatest impact on habitual violations. Enterprises should increase the training of employees and strengthen their safety awareness. In order to avoid the occurrence of unsafe acts, risk prevention and control measures are proposed for the government, organizations, enterprise managers and employees.

Based on the current situation of coal mine gas explosion safety management in China, an improved HFACS-GE framework is established. From the perspective of practice, a feasible method is constructed to predict the probability of unsafe acts in coal mine gas explosion accidents, which is helpful for managers to grasp the key points and root causes of improvement, and has important reference value for the formulation of preventive measures. Therefore, this study explores the main human factors in coal mine gas explosion accidents, which is of great significance to ensure the safety of coal mine production and has certain enlightenment for the safety management of coal mine enterprises.

Author Contributions: All authors contributed to this work. Specifically, L.N. developed the original idea for the study and designed the methodology; J.Z. and J.Y. participated in the discussion of the feasibility of the methodology; J.Z. completed the survey and drafted the manuscript, which was revised by L.N. and J.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This study was supported by the Liaoning Provincial Social Science Planning Fund Project (No. L20BGL030) This support is gratefully acknowledged.
Institutional Review Board Statement: The study was conducted in accordance with the Declaration of Helsinki, and the protocol was approved by the Ethics Committee of Liaoning Technical University.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: Data are available from the authors upon reasonable request.
Acknowledgments: The authors appreciate all the survey participants.
Conflicts of Interest: The authors declare no conflict of interest.
