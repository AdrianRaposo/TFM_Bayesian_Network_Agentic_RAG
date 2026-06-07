# Complexity-driven Risk Decision Framework for Cost Overrun using Fuzzy-Bayesian Network 

Farman Afzal ( $\boldsymbol{\square}$ farmanafzal@gmail.com)
University of Engineering and Technology https://orcid.org/0000-0001-8637-9741
Fahim Afzal
University of Sialkot
Danish Junaid
Bahria University
Imran Ahmed Shah
Shah Abdul Latif University
Shao Yunfei
UESTC: University of Electronic Science and Technology of China

## Research Article

Keywords: Risk assessment, cost overrun, complexity-risk interdependency, fuzzy logic, Bayesian network, construction projects
Posted Date: November 17th, 2022
DOI: https://doi.org/10.21203/rs.3.rs-2216201/v1
License: $\odot$ (1) This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

Version of Record: A version of this preprint was published at Soft Computing on March 12th, 2023. See the published version at https://doi.org/10.1007/s00500-023-07983-7.

## Abstract

This study adheres to find important complexity-risk interdependent causes of cost overrun in infrastructure transport projects rather considering an independent state of project risk. Aiming for addressing cost overrun problem to facilitate decision-makers, a hierarchical breakdown structure of complex elements and complexity-driven risk factors at different levels of severity is conceptualized along with their interdependency network of key relationships. In this work, an integrated approach of fuzzy logic with the Bayesian belief network is employed for cost-risk assessment while assuming linguistic scales of likelihood and consequences parameters. The simulated results of cost-risk decision framework imply that poor design issues, increase in material prices and delay in relocating facilities show higher complexity-risk dependency and increase the risk of cost overrun in complex projects. This study contributes to the body of knowledge by providing a practical hybrid risk decision framework to identify and evaluate the key complexity-risk interdependencies in underline relations to the cost overrun problem in construction.

## 1. Introduction

Complex and dynamic nature of construction projects encountered a series of cost overrun issues over the years (Lee 2008; Eybpoosh et al. 2011; Cantarelli et al. 2012; Qazi et al. 2016; Sarmento and Renneboog 2017). This cost failure is because of the presence of uncertainty (Sadeghi et al. 2010) and the dynamic nature of a project (Pehlivan and Öztemir 2018). By definition, larger infrastructure projects are complex (Fang et al. 2012) and dynamic (Cheng et al. 2010), often encounter cost overrun problem (Love et al. 2014). Lee (2008) has presented the causes of cost overrun in Korean mega capital projects. The results of his study have shown that 95 to 100\% of transport construction projects have the likelihood of cost overrun over 50\%. Like in the other regions, Asian international Infrastructure Transport Projects (ITPs) have also been confronting huge pressure concerning baseline cost divergence due to its chaotic market structure (Liu et al. 2016). Similarly, Al-Hazim et al. (2017) have documented that almost 76\% of large ITPs in Asia have cost underestimation problems. In addition, various other studies have also discussed the phenomenon of cost overrun in ITPs and employed various risk assessment models to find out the unique causes of cost overrun (Hastak and Shaked 2000; Dikmen et al. 2007; Doloi 2011; Eybpoosh et al. 2011; Cantarelli et al. 2012; Fang and Marle 2013; Love et al. 2014; Samantra et al. 2017; Olaniran et al. 2017), but the issue remains static due to the unique dynamic nature of each construction project (Yuan et al. 2018; Tabei et al. 2019). This all happened because of the complex relationship between complexity and complexity-driven risk factors (Qazi et al. 2016). Therefore, baseline cost escalation adheres to the implementation of contingency plans for project progress in managing complexity and complexity-driven risk within an uncertain environment (Khodakarami and Abdi 2014; Islam and Nepal 2016; Love et al. 2016).

A growing number of studies have been found in the literature containing hybrid methods in measuring the causes of cost overrun under high uncertainty (Sadeghi et al. 2010; Shafiee 2015; Kabir et al. 2016; Islam et al. 2017; Yazdi and Kabir 2017). The use of fuzzy hybrid methods, such as fuzzy analytical network processing (Shafiee 2015), Fuzzy Bayesian Belief Networks (Fuzzy-BBNs) (Kabir et al. 2016), fuzzy neural networks (Chan et al. 2009) and fuzzy Monte Carlo simulation (Sadeghi et al. 2010), appear to be superior over multi-criteria decision models (Hastak and Shaked 2000; Li et al. 2013; Valipour et al. 2015; Shariat et al. 2019) to evaluate the interdependencies between the events under high uncertainty (Shafiee 2015; Mehlawat and Gupta 2016; Islam et al. 2017). In order to better evaluate the vulnerability exist in subjective risk information (Yildiz et al. 2014) and addressing the range of probabilities in the form of membership functions rather in absolute crisp values (Islam and Nepal 2016; Kabir et al. 2016), an integrated approach of Fuzzy Set Theory (FST) (Karimiazari et al. 2011; Islam et al. 2017) and Bayesian Network (BN) (Qazi et al. 2016; Islam et al. 2017; Yazdi and Kabir 2017) is used. The approach appears to be effective in order to find the causes of cost overrun with limited information under high complexity (Fang et al. 2012; Fang and Marle 2012; Cheng and Lu 2015) and uncertainty (Chan et al. 2009; Sadeghi et al. 2010; Cárdenas et al. 2013; Salling and Leleur 2015).

In the past, various risk assessment frameworks are formulated to assess the causes of cost overrun, but these frameworks did not reflect the complexity-risk interdependencies phenomenon in order to find the causes particularly in risk assessment process (Dikmen et al. 2007; Fang and Marle 2013; Qazi et al. 2016; Samantra et al. 2017). Limited studies are found in the literature that have emphasized on the complex relationship between complexity drivers and risk factors (Marle and Vidal 2016; Qazi et al. 2016). Prior research has addressed two schools of thought with regards to the risk as an element of complexity (Fang et al. 2012; Fang and Marle 2013) or having the distinct characteristic of defining cost overrun (Hastak and Shaked 2000; Samantra et al. 2017). This study focusses on the fact that in dynamic conditions where uncertainty is high, the presence of complexity usually instigates the impact of risk in a project. Therefore, project complexity and complexity-driven risk factors cannot be evaluated separately in order to find the

causes of cost overrun. Subsequently, the main aim of this research is to find the important hierarchical break-down structure of complexity-risk interdependent causes of cost overrun in ITPs and to propose a risk assessment framework considering complex complexity-risk interdependencies that escalate the project cost. The proposed framework has employed 'trapezoidal fuzzy membership function' to quantify the equivalent linguistic terminologies against rating for complexity elements and risk factors and a Bayesian inference approach of Directed Acyclic Graph (DAG) to measure and find important interdependencies within a structured framework between complexity and complexity-driven risk factors for cost overrun.

The critical risk factors such as 'inappropriate project designing and poor engineering process', 'increase in the price of construction material' and 'delay in transferring existing facilities' show a high dependency on other complexity elements. The unique contribution of the present work is to articulate an efficient hybrid approach of fuzzy logic and Bayesian inference for developing structured priority of potential complexity-driven risks related causes of cost overrun and designing interdependency network for cost overrun in ITPs.

The procedural steps of the following sections of the paper have been described below. Section 2 has illustrated the preliminaries of Bayesian inference and FST. Section 3 has explained the procedural steps taken to define complexity and risk network with empirical evidence in ITPs. The study findings and implications have been discussed in Section 4. Finally, conclusions, research limitations and future directions have been delineated in Section 5.

# 2. The Construction Of Multi-state Fuzzy Bayesian Network 

Bayesian Belief Network (BBN) is a graphically designed method called DAG, where nodes denote prior probabilities of risk events and arrows denote the conditional probabilities between the risk events (Liu 2010). The arrows signify the dependency between mutually exclusive risk elements inside the risk network (Weber et al. 2012). Thus, the combined effect of prior and conditional probabilities computes the probability of dependent risk event in a network. In addition, one of the benefits of BBN is that it can update the probabilities frequently in the system when new information for the input factors become available (Khodakarami and Abdi 2014; Wang et al. 2016). BBN has the ability of back-propagation that helps in measuring the probability of events that may not be observed directly (Islam et al. 2017).

With the Fuzzy-BBN hybrid approach, fuzzy logic initially characterizes and measures assessment criteria (i.e., likelihood and consequences of risk) as per the subjective evaluation of Decision Makers (DMs) on a linguistic scale and then transforms them into fuzzy membership functions (Kimiagari and Keivanpour 2018). Fuzzy arithmetic-mean has been employed herein to compute aggregate fuzzy membership results in absolute value (Mehlawat and Gupta 2016). For BN these absolute values are further transformed in three-point estimates according to the experts' mental state.

### 2.1. Bayesian Inference

A general form of BN can be stated as $D=\langle(X, E), P\rangle$, where $(X, E)$ form shows a DAG with $n$ number of nodes. $X$ represents random nodes $\mathrm{X}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ and $E$ represents directed edges of these nodes. $P$ states the conditional probabilities of each node and a set of joint probabilities. In BN parameters, the conditional probability of the child node $X_{i}$ is expressed quantitatively under all the combinations of values of its father node $\pi\left(X_{i}\right)$. However, the prior probability value of the root node is expressed in a different probability state. Conditional probability inference of node $X_{i}$ is independent of other nodes in the same DAG network except for its father node $\pi\left(X_{i}\right)$. Therefore, under the same inference of $\pi\left(X_{i}\right)$, other nodes, except $X_{i}$, are expressed in $A\left(X_{i}\right)$, this is also stated in Eq. 1.

$$
P\left(X_{i} \mid \pi\left(X_{i}\right), A\left(X_{i}\right)\right)=P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

BN expresses the joint probability distribution of events using conditional probabilities between child and father nodes. The joint probability distribution for BN inference is given as:

$$
P(X)=P\left(X_{1}, X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

Normalized probability of each risk event can be expressed as follows:

$$
P\left(X_{i}^{n}\right)=\frac{\left(P X_{i}\right)}{\sum_{i=1}^{n} P\left(X_{i}\right)}
$$

The prior probabilities of the independent risk events can also be expressed as:

$$
\sum_{i=1}^{n} P\left(X_{i}^{n}\right)=1, i=1,2,3, \ldots, n
$$

# 2.2. Fuzzy Logic 

A well-recognized decision tool for uncertainty measurement called fuzzy logic allows the vulnerability of the risk events based on subjective evaluation. FST exclusively addresses an issue in the form of a full or non-membership function. Construction risks are not normally characterized due to the complex and uncertain nature of the problems (Lin and Jianping 2011). Conversely, FST adjusts basic binary logic to catch vagueness and uncertainty in characterizing risk data (Zhang et al. 2017). Fuzziness is a transformation process of an element in a set of non-membership and membership state (Kabir et al. 2016). However, the basic limitation of the fuzzy model is that it does not consider the complex interrelationship effects of risks within or beyond the group (Jin 2010; Karimiazari et al. 2011). Consequently, fuzzy models can only treat the independent state of risk under high uncertainty in a system. Thus, to overcome this limitation, other methods are applied in a combination of fuzzy logic to address the complexity and uncertainty of interdependent risk events in a system (Islam et al. 2017). Because of the limitations of risk data availability and vagueness in experts' judgment, it is rather difficult to find accuracy in risk calculation. Therefore, in this work, a fuzzy membership function is developed to transform the linguistic evaluation of the likelihood and consequences of complexity and risk.

Generalized trapezoidal fuzzy membership function has been defined as a fuzzy function $\vec{F}=(a, b, c, d ; \omega)$, which belongs to real field $R$, defined as a membership function $\delta_{\bar{A}}(Z): \rightarrow[0,1], z \in R$. Therefore, the trapezoidal fuzzy membership function $\delta_{\bar{A}}(Z)$ is expressed as follows:

$$
\delta_{\vec{F}}(Z)=\left\{\begin{array}{c}
0, y<0 \\
\frac{y-a}{b-a} \omega, a \leq y<b \\
\omega, b \leq y \leq c \\
\frac{d-y}{d-a} \omega, c<y \leq d \\
0, y>0
\end{array}\right.
$$

5
Similarly, $a \leq b \leq c \leq d$ and $b \leq y \leq c$ is the cross over distribution interval in $\vec{F}$. Weight $[\omega=1]$ belongs to the maximum height of $\delta_{\vec{F}}(Z), \vec{F}$ is defined as a regular trapezoid fuzzy membership function, expressed as $\vec{F}=(a, b, c, d ; 1)$.

## 3. Methodology: Procedural Steps

This section follows the steps taken to collect the data for assessing the likelihood and consequences of complexity drivers and risk factors in relation to the cost overrun. In this study, experts' subjective judgment is recorded through personal interviews from construction experts, who have been associated with metropolitan construction projects in under-developing countries. For the recording of subjective judgments, ten experts as DMs from a different area of expertise with more than fifteen years' construction experience have been nominated to participate in the decision-making process by the project authorities. Subjective evaluation of complexity and risk related to cost overrun has been recorded in three rounds according to the requirement of the designed method. In

the first round, data is collected to develop a hierarchical breakdown structure of potential complexity drivers and risk factors for cost overrun on a binary scale. In the second round, the linguistic scale is used to record the likelihood and occurrence of complexity and risk events. In the last round, prior and conditional probabilities are recorded for developing Bayesian inference of complexity-risk interdependencies along with the expected variation in project cost.

This research process contains the following steps in order to find complexity-risk breakdown structure and development of Bayesian inference for cost overrun.

Step 1: Identification of potential complexity and risk factors to form a hierarchical complexity-risk breakdown structure for cost overrun.

Step 2: Selection of suitable linguistic scales to record experts' subjective judgments for both likelihood and consequences of complexity-risk events.

Step 3: Transformation of linguistic data into an appropriate trapezoidal fuzzy function in accordance with a recommended fuzzy scale set by the DMs. In the fuzzy decision matrix process, a collective opinion of DMs is obtained using fuzzy aggregation rule and fuzzy control.

Step 4: Development of BBN for complexity-risk interdependencies based on the fuzzy triangular distribution probability values of key prior complexity and conditional risk factors.

Step 5: For the analysis and re-evaluation process, project cost data against each complexity-driven risk criteria is collected across different construction projects, for sensitivity measurement. Three-point joint estimates of cost overrun (i.e., low, medium, and high) are determined against three estimates (i.e., pessimistic, most likely, and optimistic) of important risks that directly impact on cost overrun assuming complexity-risk interdependences.

The specific identity of experts involved in the decision-making process is not supposed to reveal due to the reason of anonymity. During the interview session, experts have been requested to record their judgments on a prescribed format of the questions. After getting an initial response on a binary scale, a structured framework of complexity drivers and risk factors is drawn for further work.

# 3.1. Identification of Complexity and Risk Breakdown Structure 

After intensive literature review, different complexity elements and complexity-driven risk factors have been transformed into binary states of 'True (T)' or 'False (F)' for selection during interview process (Qazi et al. 2016). Afterwards, based on the experts' aggregate opinion, a breakdown structure of complexity-risk elements is obtained for the prioritization process. Tables 1 and 2 present a total sixteen complexity elements and twenty risk factors from five different risk sources, i.e., engineering design, construction management, construction safety-related, natural hazards, and social and economic, as defined by Hastak and Shaked (2000), Dikmen et al. (2007), Fang et al. (2012), Qazi et al. (2016) and Samantra et al. (2017).

Table 1
List of Complexity Elements for Cost Chaos in Mega Construction Projects


Table 2
List of Risk Factors for Cost Chaos in Mega Construction Projects


[Insert Table 1]
[Insert Table 2]

# 3.2. Linguistic Scales and Fuzzy Membership Function 

Under the condition of uncertainty in subjective risk information, getting exact data of likelihood of occurrence and consequences in relations with the complexity and risk events, the study necessitates the support of group decision to record experts' subjective judgments on a linguistic scale (Kabir et al. 2016; Mehlawat and Gupta 2016). For the effectiveness of subjective judgments in the assessment process, a linguistic scale has been designed to measure the semantic strength of an event, as suggested by Rezakhani et al. (2014) and Samantra et al. (2017). In addition, by following Eq. 5, fuzzy numbers have been developed to represent a set of linguistic measurement values for each property of complexity and risk event (Fouladgar et al. 2012; Zhang et al. 2017).

Although many studies have followed different types of fuzzy membership functions for solving linguistic-based problems (Chang 2014; Russo and Camanho 2015), generalized fuzzy trapezoidal membership function has been selected for subjective assessments due to the possible optimized constraints of other fuzzy functions (Prascevic and Prascevic 2017). In this research, the likelihood and consequences for both complexity and risk events have been quantified by using linguistic scales of seven attributes (Samantra et al. 2017) and five attributes (Amiri and Golozari 2011), respectively, with corresponding fuzzy membership function (Prascevic and Prascevic 2017), as labelled in Tables 3 and 4, and in Fig. 1 as well.

Table 3
Fuzzy Linguistic Scale for Assessing Likelihood of Risk or Complexity


Table 4
Fuzzy Linguistic Scale for Assessing Occurrence of Risk or Complexity


[Insert Table 3]
[Insert Table 4]
[Insert Fig. 1]

# 3.3. Fuzzy Decision Matrix Process 

1. During the decision-making process, using linguistic information of Tables 3 and 4, a fuzzy decision matrix, $D M_{C-R L / C}^{h}$ for an individual expert $h(1,2,3, \ldots, g)$ regarding the likelihood (L) and consequences (C) of complexity-risk elements is constructed separately as articulated in Eq. 6. Decision matrix addresses the states of $n$ complexity influencing factors $\left(C_{1}, C_{2, \ldots}, C_{n}\right)$ and $k$ risk factors $\left(R_{1}, R_{2, \ldots}, R_{k}\right)$ under $m$ number of dimensions $\left(D_{1}, D_{2, \ldots}, D_{m}\right)$ by a group of $g$ number of experts $H_{g}$. In complexity decision matrix $D M_{C L / C}^{h}, \tilde{F}_{i j}(i=1,2, \ldots, m$ and $j=1,2, \ldots, n)$ is specified separately like comparing the states of $L$ and $C$ for each criterion $C_{m}$ against a group of $D M_{g}$. Similarly, in the risk matrix $D M_{R L / C}^{h}, \tilde{F}_{i j}(i=1,2, \ldots, m$ and $j=1,2, \ldots, n)$ is specified separately for both states $L$ and $C$ for each criterion $C_{m}$ against a group of $D M_{g}$. Decision matrices $D M_{C-R L / C}^{r}$ for likelihood and consequence of complexity-risk criteria against individual DM have been expressed herein in Eq. 6, as recommended by Islam and Nepal (2016), Kabir et al. (2016) and Khodakarami and Abdi (2014).
$D M_{1} \quad D M_{2} \quad \cdots \quad D M_{g}$

$$
D M_{C-R L / C}^{r}=\begin{gathered}
C_{1 \times 1} \\
C_{2 \times 1} \\
\vdots \\
C_{m \times 1}
\end{gathered}\left[\begin{array}{cccc}
\widetilde{F}_{1 \times 1} & \widetilde{F}_{1 \times 2} & \cdots & \widetilde{F}_{1 \times g} \\
\widetilde{F}_{2 \times 1} & \widetilde{F}_{2 \times 2} & \cdots & \widetilde{F}_{2 \times g} \\
\vdots & \cdots & \ddots & \vdots \\
\widetilde{F}_{m \times 1} & \widetilde{F}_{m \times 2} & \cdots & \widetilde{F}_{m \times g}
\end{array}\right]
$$

6

1. Involving multiple experts create the decision-making process more complex and uncertain (Islam and Nepal 2016; Kabir et al. 2016). As the DMs belong to different designations, experience and qualification, therefore, their opinion holds different weight credibility in the decision process. The expert's credibility factor is measured using $W_{h}$ as discussed by Kabir et al. (2016) and based on an expert's experience $E_{h} \in[0,1]$, qualification $Q_{h} \in[0,1]$, and designation $D_{h} \in[0,1]$, particularly at risk management in the construction domain. In this paper, the formulation is modified using a normalization factor $\operatorname{MAX}_{h=1}^{H}\left(D_{h} Q_{h} E_{h}\right)^{\beta}$. Table 5 describes the general profile of the experts and their weight criteria involved in the decisionmaking process. The normalization weight vector is computed such that the total credible weight of an expert is considered as 1 and remaining weights of DMs are $W_{k} \leq 1$. Therefore, for $K$ number of experts, the credibility factor $\left(W_{k}\right)$ is derived as:

Table 5
General Profile of Experts and their Weight Criteria


$$
W_{h}=\frac{\left(D_{k} Q_{k} E_{k}\right)^{\beta}}{M A X_{k=1}^{K}\left(D_{k} Q_{k} E_{k}\right)^{\beta}}
$$

Where $\beta$ is a weight vector used to assign the weight of individual DM; therefore, the higher $\beta$ value shows the dominance of $D M_{g}$ in assessment with higher $D_{h}, Q_{h}$ and $E_{h}$.
[Insert Table 5]

1. The fuzzy numbers in the decision matrix $D M_{C-R L / C}^{c}$ are multiplied by the weight score of the respective individual expert $\left(w_{h}\right)$. Afterwards, fuzzy multiplication rule as shown in Eq. 8 has been applied to get weighted elements of the matrix.

$$
\left(D M_{C-R L / C}^{h}\right)_{w}=w_{i} \otimes\left(\bar{F}_{i j}^{h}\right)_{L}, w_{i} \otimes\left(\bar{F}_{i j}^{h}\right)_{M} w_{i} \otimes\left(\bar{F}_{i j}^{h}\right)_{N} w_{i} \otimes\left(\bar{F}_{i j}^{h}\right)_{U}
$$

8

Here, $L, M, N$ and $U$ mean the lowest, low moderate, moderate and highest possible number of fuzzy trapezoidal function, respectively, and the symbol $\otimes$ indicates fuzzy multiplication rule. All the matrices of individual DMs are transformed into one single matrix following the fuzzy arithmetic average (Islam and Nepal 2016) by using Eq. 9.

Elements of group matrix $=$
$\bar{F}_{i j}^{G}=\frac{1}{k} \sum_{h=g}^{k-1} \bar{F}_{i j}^{h} \otimes w_{h}=\left(\frac{1}{k} \sum_{h=1}^{k} \bar{F}_{i j}^{h} \otimes w_{h}\right)_{L},\left(\frac{1}{k} \sum_{h=1}^{k} \bar{F}_{i j}^{h} \otimes w_{h}\right)_{M}\left(\frac{1}{k} \sum_{h=1}^{k} \bar{F}_{i j}^{h} \otimes w_{h}\right)_{N}\left(\frac{1}{k} \sum_{h=1}^{k} \bar{F}_{i j}^{h} \otimes w_{h}\right)_{U}$
9

1. The elements of the group matrix are defuzzified using the following Eq. 10. The defuzzification method-Center of Area (Hefei 2017; Yazdi and Kabir 2017)-is used to calculate the absolute values of likelihood and consequences.

$$
\text { Center of Area }(C O A)=w_{i}=\left(\frac{a+b+c+d}{4}\right)
$$

1. Finally, fuzzy if-then rules between the likelihood and consequence presented in Table 6 are applied to finding the probability level of risk for Bayesian inference (Cárdenas et al. 2014; Kabir et al. 2016; Yazdi and Kabir 2017).

Table 6
Fuzzy Control Rules between Likelihood and Consequence


[Insert Table 6]

Furthermore, Bayesian inference is developed to find out the entire posterior probabilities of the complexity event and all intermediaterisk nodes of cost overrun.

# 3.4. Development of DAG Bayesian Belief Network 

It is obvious that decision outcomes are dependent on the risk-bearing attitude of the domain experts. Though the linguistic probability scores of each identified complexity-risk factors may tend to alter when experts' mental attitude is considered (Islam and Nepal 2016; Kabir et al. 2016). Therefore, considering experts' different risk-bearing attitudes, i.e., pessimistic (P), most likely (ML) and optimistic ( 0 ), the integration of fuzzy scores into Bayesian inference has become an effective approach in order to analyze complexity-risk interdependencies (Islam et al. 2017; Yazdi and Kabir 2017). Tables 7 and 8 show the computation of linguistic probability scores of each identified complexity-risk factors with experts' different risk-bearing attitudes.

Table 7
Prior Probabilities Scores of Complexity Elements along with Fuzzy Values


Table 8
Prior Probabilities Scores of Risk Factors along with Fuzzy Values


In order to design a DAG-based Bayesian inference, the judgments of DMs are first transformed into fuzzy numbers, which provide a probability of risk occurrence. These probabilities are the input variables of BBN for representing the causal relationships among the complexity-risk elements of cost overrun.
[Insert Table 7]
[Insert Table 8]
The conditional probabilities of complexity-risk interdependencies have been recorded through the above-mentioned decision-making process along with the triangular distribution of cost data, i.e., low, medium and high. During the decision process, experts have been asked to first define complexity-risk interdependencies and then record conditional probability values directly into the network following the prior probability values of complexity elements.
[Insert Fig. 2]

The DAG in Fig. 2 presents interrelationships within complexity elements and risk factors, where complexity is considered as a parent node and risk as a child node, respectively. Consequently, risk factors, such as inappropriate project designing and poor engineering process $\left(\mathrm{PD}_{1}\right)$, delay in relocating existing facilities $\left(\mathrm{DF}_{7}\right)$ and increases in prices of critical construction materials $\left(\mathrm{PM}_{18}\right)$, show high dependency in a network that directly impacts on the cost behaviour.

Bayesian inference in Fig. 3 shows normalized joint probability with complexity-risk interdependencies for cost overrun function calculated by using Equations 2 and 3 on three-point estimations. Utility node shows to address the cost overrun causes that can be controlled because of this complex relationship. Finally, three main risk factors, $\mathrm{PD}_{1}, \mathrm{PM}_{18}$ and $\mathrm{DF}_{7}$, are found to be important that reflect the direct impact on cost overrun depending on other posterior complexity elements and risk factors in a network.
[Insert Fig. 3]
[Insert Table 9]
Table 9
Cost Variation against the Probability States of Key Risk Sources (amount in million dollar)


Three-point joint estimates of cost overrun (i.e., low, medium, and high) are determined against three estimates (i.e., pessimistic, most likely, and optimistic) of important risks that directly impact on cost overrun assuming complexity-risk interdependences. Table 9 illustrates the variation of cost in dollars against important risk factors that have been found through Bayesian inference. Additional cost required to manage risk within the complexity-risk network in ITPs has found between 1.7 million (in case of pessimistic approach of risk probability) to 78.6 million dollar (in case of optimistic approach of risk probability).

# 3.5. Simulation Modelling for Cost-Risk Re-evaluation 

Risk analysis and re-evaluation

Right after taking the risk circulation conduct into view, the probability of risk is reconsidered and displayed as a numerical risk frequency (Afzal et al. 2020), for a thorough description of the methodology used for simulation modelling. The outcomes of Monte Carlo simulation are useful to estimate the cost-risk for the project, grounded on historic cost data and to calculate the entire costs. In order to re-evaluate the Fuzzy-BBN results, real cost data or each important risk factor is collected from different construction projects and there simulated values are used for further analysis. The overall cost of the project is calculated by the merge of base and risk costs of all several components. The supplementary cost vital for allay of the risk is estimated through a contingency model, for the timely completion of the project (Afzal et al. 2021).

The importance of the highlighted analysis is to know the risk factors of cost overrun that propagate a project into chaos and calculate the necessary amount of the additional cost needed to handle cot-chaos. In the next phase, specialists were requested to measure the total cost of risk for each identified risk in a network. It is clear that risk scores differ based on the experience of the specialist. In addition to this, the cost of a project is based on the risk level.

Furthermore, the present study aimed to evaluate the run over of cost while keeping the risk score into consideration that shows that how much risk is taken by a specialist like pessimistic, most likely, and optimistic. By applying a three-point calculation approach, cost variation has been designated for virtual decision-making (Afzal et al. 2020). Through revaluation process of model, it is validated that the maximum project cost flow is coming from the factors of inappropriate project designing and poor engineering process, delay in relocating existing facilities have caused improper cost management and increases in prices of critical construction materials.

Table 10 summarises cost-benefit contingency values created by each risk factor's simulated scoring and the corresponding cost to ameliorate each risk. The contingency index determines the budgetary allocation needed to reduce the project's risk impact despite of concluding prior to its accomplishment.

Table 10 Simulated Results of Cost-Risk Comparative Analysis


[Insert Table 10]

# 4. Study Findings And Discussions 

Probabilistic causal inferences about cost overruns in relation with complexity-risk interdependencies are acquired from a combination of assumptions, experiments and data. While addressing the prevalent and complex cost problem, Fuzzy-BBN is applied to explicate, determine and predict probabilities within a structured framework of complexity-risk interdependencies. Fuzzy-BBN approach presented herein in a model for assessing dependency between complexity-risk related causes of cost overrun under uncertainty (Islam and Nepal 2016).

An empirical study of metropolitan ITPs in Pakistan is presented herein on the important issue of cost overrun and its potential control measures have been acquired through a decision process. In consideration of past literature and experts' opinion, the study

has assessed complexity-risk interdependencies by considering sixteen potential complexity elements and twenty risk factors from different indigenous and exogenous sources, such as technical, managerial and environmental (Valipour et al. 2016; Zhang et al. 2016; Liu et al. 2016; Samantra et al. 2017). In this work, important dependencies are identified and subsequent risk management plan is also suggested for mitigating or controlling the risks leading to project cost overrun.

The findings of Bayesian inference show that three important interdependent risks, namely 'inappropriate project design and poor engineering process', 'increase in the price of construction material' and 'delay in relocating existing pipelines and facilities', directly effect on project cost and found very significant in the context of ITPs in Pakistan. The maximum variation in project cost reflected by complexity-risk interdependencies is around 78.6 million dollars and the maximum risk appears in 'delay in relocating existing pipelines and facilities' with a joint probability value is $41.11 \%$.

The key findings of this research have suggested that risk cannot be considered independently to find the causes of cost overrun in constructions. Risk is derived through the existence of complexity in any project. Consequently, if the complexity level is low in a project then the probability of risk occurrence is low. Similarly, if system complexity is high then the probability of risk occurrence is high. Some risk events show high joint network dependency and some with low dependency. Such hidden complexity-risk interdependencies are important in risk assessment of mega-projects where complexity and uncertainty are always high that usually instigate the cost escalation. These findings are consistent with the studies of Qazi et al. (2016), Love et al. (2014) and Fang et al. (2012), who advocate that the risk is derived through system complexity.

An additional contribution of this research is viewed as to suggest a necessary risk control plan for timely managing construction project risks to avoid cost escalation. This plan consists of the guidelines for effectively monitoring and controlling critical causes of cost overrun in relation to complexity-risk interdependencies associated with the ITPs (as shown in Table 11).

Table 11
Required Action Plan for Different Dimensions to Avoid Cost Escalation


# [Insert Table 11] 

From a risk mitigating and controlling point of view, the present research has explored that 'policy decisions regarding investment preferences from the local government' have been found a major hurdle in determining the project cost over a project life cycle. This increases the urgency of having competent managers who could deal effectively with public authorities. Secondly, 'political instability', 'poor economic situation' and 'law and order problems' also instigate the issues related to construction designing, planning and material prices. Before to initiate such mega-projects, standard technical and construction management related expertise are required domestically to avoid the potential risk of cost overrun. Similarly, appropriate planning of cash flows over a project life is mandatory for timely completion of a project rather facing cost overrun problem later that may drift a project into failure.

The unique contribution of the present work is to articulate an efficient hybrid approach of fuzzy logic and Bayesian inference for developing structured priority of potential complexity-driven risks related causes of cost overrun and designing interdependency network for cost overrun in ITPs. The fuzzy concept has been empowered herewith to assist in converting the linguistic data of probability into fuzzy scores that have been further employed in Bayesian inference. In addition, the application of FST and BBN have

successfully tackled the system complexity and uncertainty as well as vagueness arising in the expert's perception during the subjective judgment decision process. It has been observed that the computation of interdependencies has supported to perceive the degree of severity that requires being controlled for effective cost management in construction. The risk factors with high interdependencies should be immediately controlled. Simulated results of cost-risk data of different projects also validate the findings generated through Fuzzy-BBN modeling.

Theoretically, this study contributes in a way by providing a practical approach to evaluate the complexity and risks in construction using five simple steps: (1) Developing a structured hierarchical breakdown structure of potential complexity and risk factors in complex infrastructure projects (see Tables 1 and 2); (2) To transform a linguistic scale into a fuzzy trapezoidal function for accessing uncertainty or vulnerability in subjective risk data during the decision-making process; (3) To calculate the probabilities of each identified complexity-risk factors using fuzzy decision-making process; (4) To develop a unique complexity-risk interdependency network to find cost overrun causes and measure tentative variation in project cost considering complex interdependencies within a system using Bayesian inference with three-point estimates; (5)Suggesting a required action plan against important risk dimensions for cost overrun (see Table 10). Even more, this methodology may be used by experts from other engineering industries by replacing and considering the complex relationship between complexity elements and risk factors and following the same steps presented here.

For a practical point of view, this study is subjected to introduce a decision-making framework that permits construction experts and other engineering related project managers in a way: (1) to provide an approximation of the most frequent and critical complexitydriven risks in large construction projects particularly in unstable economies; (2) to quantify uncertainty exists in risk information and designing interdependency network of complexity-risk oriented causes of cost overrun. The chosen risk assessment process may provide multiple benefits to managers in larger picture: (1) to implement proposed approach for finding the causes of cost overrun in dynamic construction projects; (2) to foresee the consideration of the required technical capabilities in construction; (3) effective cost allocation in the project plan while considering the critical associated risks; (4) the suggested action plans and early detection of risk could improve the project delivery process within predetermined project cost while addressing expensive weaknesses in construction.

As likely, the critical risk factors such as 'inappropriate project designing and poor engineering process', 'increase in the price of construction material' and 'delay in transferring existing facilities' show a high dependency on other complexity elements. Therefore, in consideration of this, project managers should emphasize on the above-mentioned risks during cost estimation while assuming a risk dependency on complexity. In summary, the above-mentioned suggestions for project and engineering managers can be potentially achieved by considering the complexity-risk interdependency network under high uncertainty of cost found in this research.

# 5. Conclusions 

Cost overruns that are experienced in large infrastructure projects usually have an adverse impact on an economy and its taxpayers, particularly in under-developing economies. To improve decision-making, implementation of effective risk mitigation strategies and reduce the likelihood of cost overrun being experienced, the undertaken study has been able to redress this prevalent cost problem under high uncertainty. In this work, a practical risk assessment framework is developed as a reliable tool; since it has established risk as a source of complexity network. In the present paper, Fuzzy-BBN approach is embedded for designing complexity-risk interdependency network of cost overrun. Subsequently, this study has used experts' tolerance level like optimistic, most likely and pessimistic as input values for parents (complexity) and child (risk) nodes in Bayesian-DAG network. More precisely, the uncertainty in the linguistic evaluation and experts' mental state are overcome through fuzzy logic, and complexity in a structured framework of cost overrun measured by using Bayesian inference.

While exploring the procedure of complexity and risk network identification, the study has articulated a hierarchical structure of complexity and risk factors in relation to ITPs. The hierarchy has been constructed with sixteen complexity elements and twenty potential risk factors classified into five distinct risk dimensions. Further, for the DAG network, the probability values of important complexity and risk factors obtained using the fuzzy decision-making process. Similarly, three important risk factors, namely 'inappropriate design and poor engineering', 'increase in the price of construction material' and 'delay in transferring existing facilities', are found in a an interdependency network with their joint probabilities that have directly linked with project cost overrun and show high severity level in a network.

The key findings of this study have suggested that the independent nature of project risk cannot be assumed in ITPs rather it shows high dependency on project complexity. Therefore, risk should always be considered in relation to project complexity, particularly in

complex and dynamic nature of projects. In this decision-making process, subsequent risk control plan of actions have also been suggested for mitigating the risks leading to project cost overrun issues.

Since the presented cost risk assessment approach and findings described herein are explicitly a problem-oriented, a proposed framework may be adapted to evade cost overrun issues in other engineering management related domain. To employ the said risk assessment framework in context to the specific problem, a clear understanding and knowledge of probable complexity and risks are required. While assuming the limitations, this integrated fuzzy-based risk assessment framework does not consider the sensitivity of other types of fuzzy membership functions, because a scale for this study has been adopted from past literature. Further study can be extended to check the sensitivity and applications of different fuzzy membership scales, such as continues function in regard to the aforementioned risk assessment framework. This study follows simple DAG in Bayesian inference for the complexity-risk network while assuming three-point estimates. For better cost estimation in complex interdependencies, future research can be extended using a credal network or dynamic Bayesian belief network which can be run in support of continues function. In addition, a similar approach can also be applied in measuring the causes of schedule delays in the dynamic nature of projects. Finally, this article also contributes to the body of knowledge by providing new generation framework for cost risk assessment under high uncertainty and complexity in the construction industry.

# Declarations 

## Data Availability

Some or all data, models, or code generated or used during the study are available from the corresponding author by request.

- Project complexity and risk probabilities
- Project complexity-risk conditional probabilities
- Project cost data against risk probabilities


## Acknowledgement

The authors would like to acknowledge the financial support provided by the National Natural Science Foundation of China under grant No. 71572028 and 71872027.

# Figures 

![img-0.jpeg](img-0.jpeg)

Figure 1

![img-1.jpeg](img-1.jpeg)

Figure 2

# Directed acyclic graph for complexity-risk interdependencies 

![img-2.jpeg](img-2.jpeg)

Figure 3

Posterior and joint probabilities of important complexity-risk interdependencies