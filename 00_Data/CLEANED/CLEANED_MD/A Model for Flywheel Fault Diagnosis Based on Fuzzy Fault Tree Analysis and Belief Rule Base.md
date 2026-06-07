# Article 

## A Model for Flywheel Fault Diagnosis Based on Fuzzy Fault Tree Analysis and Belief Rule Base

Xiaoyu Cheng ${ }^{1, \dagger}$, Shanshan Liu ${ }^{2, \dagger}$, Wei He ${ }^{1,3, * *}$, Peng Zhang ${ }^{3,4}$, Bing Xu ${ }^{1}$, Yawen Xie ${ }^{1}$ and Jiayuan Song ${ }^{1}$

## check for updates

Citation: Cheng, X.; Liu, S.; He, W.; Zhang, P.; Xu, B.; Xie, Y.; Song, J. A Model for Flywheel Fault Diagnosis Based on Fuzzy Fault Tree Analysis and Belief Rule Base. Machines 2022, 10, 73. https://doi.org/10.3390/ machines10020073

Academic Editors: Hongtian Chen, Kai Zhong, Guangtao Ran, Chao Cheng and Davide Astolfi

Received: 1 December 2021
Accepted: 11 January 2022
Published: 20 January 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Computer Science and Information Engineering, Harbin Normal University, Harbin 150025, China; chengxiaoyu1104@163.com (X.C.); bingxv_0227@163.com (B.X.); xie_yw@foxmail.com (Y.X.); mintpepper2216@gmail.com (J.S.)
2 School of Computer and Information Security, Guilin University of Electronic Technology, Guilin 541004, China; wxci339701@163.com
3 High-Tech Institute of Xi'an, Xi'an 710025, China; zpdyxdz@126.com
4 State Key Laboratory of Astronautic Dynamics, Xi'an Satellite Control Center, Xi'an 710043, China

* Correspondence: he_w_1980@163.com; Tel.: +189-4567-2266
+ These authors contributed equally to this work.


#### Abstract

In the fault diagnosis of the flywheel system, the input information of the system is uncertain. This uncertainty is mainly caused by the interference of environmental factors and the limited cognitive ability of experts. The BRB (belief rule base) shows a good ability for dealing with problems of information uncertainty and small sample data. However, the initialization of the BRB relies on expert knowledge, and it is difficult to obtain the accurate knowledge of flywheel faults when constructing BRB models. Therefore, this paper proposes a new BRB model, called the FFBRB (fuzzy fault tree analysis and belief rule base), which can effectively solve the problems existing in the BRB. The FFBRB uses the Bayesian network as a bridge, uses an FFTA (fuzzy fault tree analysis) mechanism to build the BRB's expert knowledge, uses ER (evidential reasoning) as its reasoning tool, and uses P-CMA-ES (projection covariance matrix adaptation evolutionary strategies) as its optimization model algorithm. The feasibility and superiority of the proposed method are verified by an example of a flywheel friction torque fault tree.


Keywords: flywheel fault diagnosis; belief rule base; fuzzy fault tree analysis; Bayesian network; evidential reasoning

## 1. Introduction

The flywheel [1] system is a key actuator for spacecraft attitude control, which is widely used in the aerospace field. The normal operation of a flywheel system is very important for spacecraft. However, the spacecraft environment where the flywheel system is located has a harsh operating environment and complex structure. Once a failure occurs, it will pose a great threat to space safety. Therefore, to ensure the reliability and orderly operation of the flywheel system, it is of great significance to diagnose the faults of the flywheel system quickly and accurately.

Many scholars have carried out a lot of research on the fault diagnosis of flywheel systems. Changrui Chen et al. [2] proposed a 3D associated dimension diagnosis method, it is improved by K-Medoids clustering technology for different typical states of satellite flywheel bearings and verified the feasibility of the method through experiments. Xinchang Zhang et al. [3] developed a set of methods for inputting correct premises, and based on consistency test results, presented a fault diagnosis model based on finite state machines, which could locate and diagnose some faults. Junweir Lin et al. [4] proposed a new fault diagnosis scheme for linear analog circuits. The author constructs a diagnostic evaluator, which can diagnose faults through digital signals and diagnose media after analyzing and

modeling the components. Bo Chen et al. [5] studied the distributed fault diagnosis technology and combined it with software technology, computer network, artificial intelligence and fault diagnosis to improve the self-fault diagnosis function of an expert system. Zijian Qiao et al. [6] proposed a second-order stochastic resonance method based on fractional derivative enhancement, which uses strong background noise to enhance the weak fault characteristics. It is used for mechanical fault diagnosis. Wenjun Sun et al. [7] studied a deep neural network based on a sparse self-code device for induction motor fault diagnosis. This method is used in the sparse automatic process to add noise encoding using the sparse automatic learning feature, which is the unsupervised feature learning that is required to measure the data without marking. Yao Cheng et al. [8] studied a set of combined fault diagnoses based on observer redundancy in the background of a satellite attitude control system. The modified scheme can solve actuator and sensor faults that are difficult to solve by traditional methods.

It can be seen from the above, most of the existing flywheel fault diagnosis schemes are designed on the basis of the data-driven method [9]. However, the current flywheel fault diagnosis still lacks an effective diagnosis scheme for the following two problems: First, the model accuracy cannot be guaranteed under small sample data. It is difficult to obtain accurate diagnosis results by using small sample data in actual fault diagnosis. This is because in the system life cycle, it is difficult to obtain a large number of flywheel fault samples, and more difficult to obtain fault samples under different fault modes; second, the black box model has the disadvantage of unexplainable diagnostic processes.

BRB (belief rule base) is a general rule-based reasoning method proposed by Yang Jianbo et al. [10] on the basis of evidentiary reasoning, which has important applications in mechanism analysis [11], health status assessment [12,13] and fault diagnosis [14]. BRB is suitable for flywheel systems, mainly reflected in three aspects: First, BRB can effectively describe the uncertainty of flywheel systems; second, the BRB modeling method is suitable for flywheel systems. It uses expert knowledge for modeling and data for model training; third, BRB has shown to be a good treatment effect for small sample problems. However, applying BRB to the actual fault diagnosis of the flywheel system cannot solve problems such as the difficulty in constructing an expert knowledge base, the unclear logical relationship between the flywheel fault events and the unclear fault index. FFTA (fuzzy fault tree analysis) $[15,16]$ enables the logical relationship between different events to be clearly expressed. This is because FFTA can present the cause of failure and events caused by this cause in the form of a fault tree from the perspective of the fault mechanism. At the same time, FFTA makes the occurrence probability of each event in the fault tree better describe the uncertainty, because it introduces the theory of fuzzy mathematics. The combination of FFTA and BRB not only enables the fault index to be clearly established and the event fuzziness to be better described, but also enables the advantages of BRB to be applied in the fault diagnosis of the flywheel system, which makes comprehensive use of the advantages of the two. Therefore, this paper establishes the FFBRB (fuzzy fault tree analysis and belief rule base) model, which makes full use of the FFTA and BRB's advantages.

The main contributions of the FFBRB model proposed in this paper are as follows: (1) The way FFTA is used to build the initial BRB model. In this paper, the FFTA mechanism is used to expand the BRB knowledge base and solve the problem of constructing an expert knowledge base of complex flywheel system; (2) A new flywheel fault diagnosis model based on BRB is proposed. This model can obtain relatively accurate data even with a small number of samples and has higher applicability. It uses expert knowledge to construct the initial parameters of the model and uses training samples to optimize the model parameters.

The main structure of this paper is as follows: In the first part, the fault diagnosis model of the original flywheel system is analyzed and discussed. On the basis of revealing the shortcomings of the original model, the fault diagnosis model of the FFBRB flywheel system is proposed; In the second part, it describes the problems that need to be solved in the process of flywheel system modeling and gives the general solution diagram; In the

third part, it defines and describes the fault diagnosis model of FFBRB flywheel system, and describes its transformation mechanism and inference optimization process in detail; In the fourth part, this paper uses a concrete example to verify the method in this paper and gives the experimental conclusion; In the fifth part, it gives the summary of this thesis.

# 2. Problem Description 

This section describes the problems and solutions encountered in the fault diagnosis of the flywheel system, and puts forward and introduces the FFBRB model.

### 2.1. Clarifying Questions

Constructing the FFBRB flywheel system fault diagnosis model needed a solution to the following problems:

Problem 1. How to use the FFTA mechanism and integrate it into the BRB knowledge base was the first problem to be solved. In the BRB, the relationship between the input and output is described by a series of belief rules, and belief rules are built based on expert knowledge. However, when the $B R B$ is applied to the practical flywheel system, expert knowledge is difficult to embed into the fault diagnosis model of the flywheel system (see Section 3.2.).

To realize the FFTA to BRB conversion, it is necessary to describe the correspondence between FFTA logic gates and BRB belief rules, and the correspondence between FFTA events and BRB input and output. The function to solve this problem is denoted as $\operatorname{CovBridge}(*)$ and $\varrho$ is the set of parameters in this process, then the process can be described by the following expression:

$$
\operatorname{BRB}(\text { BeliefRule, input/output })=\operatorname{CovBridge}(\operatorname{FFTA}(\text { LogicGate, event }), \varrho)
$$

This is a nonlinear mapping. It is not executed in a specific software language. With $\operatorname{CovBridge}(*)$, logic gates in the FFTA were converted into belief rules in the BRB, and events in the FFTA were converted into inputs and outputs in the BRB. The inputs of the $\operatorname{CovBridge}(*)$ function were logic gates, events, and parameter sets in the FFTA, and the outputs were belief rules and their inputs and outputs in the BRB.

Problem 2. How to build a reasonable and complete FFBRB model was the second problem to be solved. In order to solve the problem of how to diagnose various faults in the actual flywheel system, it is necessary to design the reasoning process and optimization process of the FFBRB model reasonably and establish a reasonable and accurate model (See Section 3.3).

The function to solve this problem is denoted as $\operatorname{FFBRB}(*) . \zeta$ is the set of parameters in this process, $y$ then the process can be described by the following expression:

$$
\mathrm{y}=\operatorname{FFBRB}(\mathrm{x}, \zeta)
$$

This is a nonlinear mapping. $x$ is the failure probability of the bottom event in the FFTA, and $y$ is the output utility value of the BRB, corresponding to the occurrence probability of the top event. $\zeta$ is the set of parameters in this process.

Remark 1. In order to solve the problem of small sample size, it could usually take two solutions. First, sample data with similar characteristics to the research question should be sought to expand the sample data volume, such as transfer learning [17,18]. Second, through the analysis of the model mechanism to expand the amount of information input. The BRB belongs to the second type of method, which can expand the model information input through expert knowledge, so as to realize model training under small samples.

# 2.2. Overview of FFBRB Fault Diagnosis Model Principle 

To solve the above problems, the FFBRB flywheel fault diagnosis model is proposed in this paper. In this model, the existing FFTA is used to construct the initial belief rules of BRB, and the transformation rules from FFTA to BRB are given. The model used the ER (evidential reasoning) algorithm to give the reasoning process of the model. In this model, the P-CMA-ES (projection covariance matrix adaptation evolutionary strategies) algorithm was used to optimize the parameters of the model, which improved the accuracy of the model. Figure 1 shows the overall transformation process of the model.
![img-0.jpeg](img-0.jpeg)

Figure 1. Fault diagnosis schematic diagram of FFBRB model.

Remark 2. The similar learning ability of the BRB and neural networks was noted in the literature [19]. Therefore, the fault diagnosis of complex systems could be achieved through constructing deep BRB or hierarchical BRB models [20].

## 3. Construction and Inference of the FFBRB Model

This section mainly introduces three parts:

- The basic structure of the FFTA flywheel system. In this part, fuzzy fault tree analysis is carried out for the flywheel system (see Section 3.1);
- The process of constructing the BRB model is based on FFTA. This part mainly describes the conversion process from FFTA to BRB (see Section 3.2);
- Reasoning and optimization process of the FFBRB model. This part is actually the reasoning and optimization process of BRB (see Section 3.3).


### 3.1. Basic Structure of the FFTA Flywheel System

In a practical flywheel system, FFTA analysis mainly depends on how the probability of each event in a fuzzy fault tree is calculated and expressed, and how to apply them to BRB. The overall fuzzy fault tree analysis structure is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. FFTA structure diagram of flywheel.
The fuzzy fault tree graph of the flywheel system is mainly composed of logic gates and related events, and its faults include sensor faults and system faults. The complete flywheel system fault tree [21] is shown in Figure 3 below:
![img-2.jpeg](img-2.jpeg)

Figure 3. Graph of flywheel system fault tree.

# 3.2. The Process of Constructing the BRB Model Based on the FFTA 

### 3.2.1. Analysis of Conversion Mechanism between FFTA and BRB

FFTA and BRB have differences in inputs and outputs. The input and output in BRB are mainly described by a series of belief rules, whereas the input and output in the FFTA are mainly described by logic gates and events. Therefore, it needed a bridge to enable the transition and transformation between the FFTA and BRB. The fault tree established in FFTA can sort out the relationship between fault events and clarify the context of different events. Bayesian networks describe the state of a part of the modeled thing and are associated with

probability, also known as reliability networks. There is a certain mapping relationship between fuzzy fault tree and Bayesian network, which is expressed as follows [22]:

- Nodes in Bayesian networks correspond to events in FFTA. Specifically, all the top events of FFTA correspond to all the leaf nodes in the Bayesian network, and all the basic events of FFTA correspond to all the root nodes in the Bayesian network.
- Conditional probability distribution of nodes in Bayesian networks is represented by logic gates in FFTA.
- The direction of node arrows in the Bayesian network also represents the logical relationship of events in the FFTA, that is, the relationship between input and output of logic gates.
In order to describe the correspondence between FFTA and Bayesian networks, an example is listed in Figure 4 for reference.
![img-3.jpeg](img-3.jpeg)

Figure 4. The corresponding expression graph between FFTA and Bayesian network graph.
BRB consists of three important parts: knowledge base, inference machine and optimization method. BRB's knowledge base is composed of a series of belief rules, which represent the relationship between input and output. ER, as the reasoning machine of BRB, is an evidential reasoning method [23]. The literature proves that the Bayesian inference can be extended to ER, where ER has weighted reliable inaccurate information, and the relationship between Bayes rules and ER rules can be revealed. The literature comes to the following conclusion: when each event is independent of the other, conditional probability is equivalent to belief degree. Therefore, it can be concluded that the Bayesian inference can be transformed into ER inference. ER [24], as the inference machine of BRB, is a part of BRB. Therefore, Bayesian inference can be transformed into BRB inference. The corresponding relationship between BRB and Bayesian network [25-27] is as follows:

- The input of the BRB corresponds to the parent node in the Bayesian network;
- The belief of the BRB can be transformed from conditional probability in the Bayesian network;
- Bayesian inference can be transformed from the ER to BRB inference.

Thus, as can be seen from the above analysis, it can conclude the complete FFTA to BRB conversion process, and the schematic conversion diagram from the FFTA to BRB is shown in Figure 5:

- The three numbers in the triangular fuzzy number of FFTA's base event failure probability are divided into three groups corresponding to the root node of the Bayesian network, respectively, which are used as the input of BRB;

- The three numbers in the triangle fuzzy number of FFTA intermediate event occurrence probability are divided into three groups corresponding to the root leaf nodes of the Bayesian network, respectively, which serve as the input and output of BRB;
- The three numbers in the triangular fuzzy number of FFTA top event occurrence probability are divided into three groups of night nodes corresponding to the Bayesian network, respectively, which are used as the output of BRB.
![img-4.jpeg](img-4.jpeg)

Figure 5. Schematic conversion diagram from FFTA to BRB.

# 3.2.2. Conversion Rules from FFTA to BRB 

It can be seen from the above that the logic gate in FFTA corresponds to the conditional probability distribution of the corresponding node in the Bayesian network. Different logic gate pairs should have different transformation rules, and this section defines the transformation process.

Probability Representation of Transformation Space Condition Corresponding to Different Logic Gates
$x_{i}$ is used to represent the i-th base event in FFTA, then the conditional probability rule in the Bayesian network corresponding to the logic gate of type "and" in FFTA can be described as expression 3, and the conditional probability rule in the Bayesian network corresponding to the logic gate of type "or" can be described as expression 4.

$$
\begin{aligned}
& p\left(\operatorname{Top}\left|x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} x_{i}\right. \\
& p\left(\operatorname{Top}\left|x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{i=1}^{n} x_{i}\right.
\end{aligned}
$$

The Belief Rule and Rule Activation Weight Representation of the BRB Corresponded to the Logic Gate

Attribute importance withdrawal in BRB is the weight of attribute, and the importance of rules is the weight of rules. In this section, this paper defined different transformation rules for different logic gates, which also correspond to different rule activation weights.

The set of input reference values in FFTA below, that is, the set of reference values of the base event is represented by $A_{i}$. Top $_{1}$, Top $_{2}, \ldots$, Top $_{n}$ represents $n$ results; under the k belief rule, the corresponding belief degree of each result is determined by $\beta_{i}(i=1 \cdots N)$, $N$ indicates the number of results; this paper used $\delta_{i}(i=1 \ldots M)$ which represents the attribute weight of each premise attribute, $M$ represents the number of attributes, and $\theta_{k}$ represents the rule weight of the belief rule in the article $k, K$ is the number of belief rules.

- Under the condition of "and" logic gates, the BRB's belief rules [28] can be described as follows:

BeliefRule ${ }_{k}$ :
If $x_{1}$ is $A_{1} \wedge x_{2}$ is $A_{2} \wedge \ldots \wedge x_{n}$ is $A_{n}$
Then result is $\left\{\left(\operatorname{Top}_{1}, \beta_{1}\right),\left(\operatorname{Top}_{2}, \beta_{2}\right), \ldots,\left(\operatorname{Top}_{n}, \beta_{N}\right)\right\}$
with rule weight $\theta_{1}, \theta_{2}, \ldots, \theta_{K}$
and attribute weight $\delta_{1}, \delta_{2}, \ldots, \delta_{M}$
where $a_{i}^{k}$ represents the rule matching degree under rule $k$ (the adaptability of input sample and belief rule), $l$ indicates two adjacent activation rules, two rules are activated when the input falls between them, and the rule activation weight calculation under the "and" gate condition is as follows:

$$
\begin{gathered}
\omega_{k}=\frac{\theta_{k} \prod_{i=1}^{M}\left(a_{i}^{k}\right)^{\delta_{i}}}{\sum_{i=1}^{K} \theta_{l} \prod_{i=1}^{M}\left(a_{i}^{l}\right)^{\delta_{i}}} \\
a_{i}^{k}= \begin{cases}\frac{A_{i}^{l+1}-x_{i}}{A_{i}^{l+1}-A_{i}^{l}} & k=l, A_{i}^{l} \leq x_{i} \leq A_{i}^{l+1} \\
1-a_{i}^{k} & k=l+1 \\
0 & k=1 \cdots K, k \neq l, l+1\end{cases}
\end{gathered}
$$

- Under the condition of "or" logic gates, the BRB's belief rules could be described as follows:

$$
\begin{aligned}
& \text { If } x_{1} \text { is } A_{1} \vee x_{2} \text { is } A_{2} \vee \ldots \vee x_{n} \text { is } A_{n} \\
& \text { Then result is }\left\{\left(\operatorname{Top}_{1}, \beta_{1}\right),\left(\operatorname{Top}_{2}, \beta_{2}\right), \ldots,\left(\operatorname{Top}_{n}, \beta_{N}\right)\right\} \\
& \text { with rule weight } \theta_{1}, \theta_{2}, \ldots, \theta_{K} \\
& \text { and attribute weight } \delta_{1}, \delta_{2}, \ldots, \delta_{M}
\end{aligned}
$$

where $a_{i}^{k}$ represents the rule matching degree (the adaptability of input sample and belief rule), the rule activation weight calculation under the "and" gate condition is as follows:

$$
\omega_{k}=\frac{\theta_{k} \sum_{i=1}^{M}\left(a_{i}^{k}\right)^{\delta_{i}}}{\sum_{l=1}^{K} \theta_{l} \sum_{i=1}^{M}\left(a_{i}^{k}\right)^{\delta_{i}}}
$$

The calculation of the rule matching degree is the same as the above "and" logic gate condition.

# 3.3. Establishment of the FFBRB Model and Inference Optimization 

The FFBRB flywheel system fault diagnosis model established in this paper is shown in Figure 6.

![img-5.jpeg](img-5.jpeg)

Figure 6. FFBRB flywheel system fault diagnosis model diagram.

# 3.3.1. Analysis of Reasoning Process from FFTA to BRB 

The reasoning process of the FFBRB model, which is actually the reasoning process of the BRB, is shown in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. Diagram of FFBRB model inference process.
In particular, this model uses the triangle fuzzy number FFTA in the probability of events, from the upper and lower bounds of the triangular fuzzy number representation and event probability values are divided into three groups, respectively, after dealing with the BRB, can go through BRB to optimize the processing of the top event probability triangle fuzzy number, see FFTA analysis of the fitting effect of the result of the probability of the top event.

FFBRB model makes the FFTA knowledge mechanism embedded in the BRB expert knowledge base, which solves the problem that it is difficult to embed BRB expert knowledge. The FFBRB model uses BRB to train a series of sample data, which further improves the accuracy of the data and solves a considerable part of the uncertainty problems of the flywheel model. This section mainly introduces the reasoning process of FFBRB model fault diagnosis, that is, the reasoning process of BRB.

The specific fault diagnosis process of the FFBRB model is as follows:
Step 1: Data preprocessing. This paper first normalized the data samples and limited the data within the range of $0-1$ to characterize the probability, so as to better describe the problem.

Step 2: Fuzzy fault tree analysis. Firstly, the logical relationship between events is sorted out and the fault tree graph of the fault diagnosis model is drawn. Then, this paper used a triangle fuzzy number to represent the failure probability of the FFTA basic event, introduce a fuzzy interval operator, calculate the triangle fuzzy number of occurrence probability of the middle event and top event and divide the data into three groups. For example, a triangle fuzzy number is used to represent the failure probability of a base event $x 1(a 1, m 1, b 1)$ and base event $x 2(a 2, m 2, b 2)$, and interval fuzzy operator formula is used to obtain the occurrence probability of an intermediate event or top event $(a, m, b)$. In order to facilitate subsequent data processing, this paper divided these data into three groups (a1, $a 2, a),(m 1, m 2, m),(b 1, b 2, b)$.

Step 3: Taking the Bayesian network as a bridge, FFTA is mapped to BRB. The equivalence of FFTA logic gate input and output and BRB input and output was explained through the bridge of the Bayesian network. According to the mapping rules mentioned above, fault tree graphs are mapped to the Bayesian network graphs and then BRB analysis is carried out, respectively, according to the graphs.

Step 4: Input the sample data integrating FFTA fault mechanism knowledge into BRB and use BRB for fault diagnosis. There are four steps to achieve concrete reasoning:

- Rule matching is calculated, that is, the degree of adaptation between input sample and belief rule. The calculation formula is shown in Formula (7).
- According to the activation weight formulas of different rules corresponding to different logic gates above (Formulas (6) and (9)), the activation weight of activation rules is calculated.
- ER analytic algorithm is used to synthesize rules and obtain the belief degree output of BRB. $L$ indicates the number of activation rules. The calculation process is as follows:

$$
\begin{gathered}
\beta_{n}=\frac{\mu \times\left[\prod_{i=1}^{L}\left(\omega_{i} \beta_{n, l}+1-\omega_{l} \sum_{i=1}^{N} \beta_{i, l}\right)-\prod_{l=1}^{L}\left(1-\omega_{l} \sum_{i=1}^{N} \beta_{i, l}\right)\right]}{1-\mu \times\left[\prod_{l=1}^{L}\left(1-\omega_{l}\right)\right]} \\
\mu=\frac{1}{\sum_{n=1}^{N} \prod_{l=1}^{L}\left(\omega_{l} \beta_{n, l}+1-\omega_{l} \sum_{i=1}^{N} \beta_{i, l}\right)-(N-1) \prod_{l=1}^{L}\left(1-\omega_{l} \sum_{i=1}^{N} \beta_{i, l}\right)}
\end{gathered}
$$

- Utility calculation, the final output.

$$
y=\sum_{n=1}^{N} u\left(\text { Top }_{n}\right) \beta_{n}
$$

Step 5: BRB optimization. In this step, the optimization algorithm is used to process the parameters to make the BRB output more accurate.

# 3.3.2. Optimization of the FFBRB Fault Diagnosis Model 

This section describes the optimization process of the FFBRB model, as shown in Figure 8 below:

![img-7.jpeg](img-7.jpeg)

Figure 8. Optimization process flow chart.
In this model, the data generated by fuzzy fault tree analysis are still uncertain after BRB processing. In order to reduce the error between the parameters processed by the initial BRB and the real data and complete the optimization of parameters, an optimization mechanism is introduced in this model. P-CMA-ES [29] algorithm is used. The optimization function can be described as follows:

$$
\begin{aligned}
& \min M S E(\varsigma) \\
& \text { s.t. } \sum_{n=1}^{N} \beta_{n, k}=1, k=1 \cdots K \\
& 0 \leq \beta_{n, k} \leq 1 \\
& 0 \leq \theta_{k} \leq 1
\end{aligned}
$$

In the upper form, the actual output of the square error is used by the $M S E(\varsigma), \varsigma$ is the parameter that appears in the process and this paper used the lower formula to represent the average error of the output of the prediction:

$$
\operatorname{MSE}(\varsigma)=\frac{1}{K} \sum_{k=1}^{K}\left(y^{*}-y\right)^{2}
$$

In the above expression, $y$ represents the actual output, $y^{*}$ represents the predicted output, and the number of training samples is expressed by $K$. The realization process of the P-CMA-ES algorithm is described in detail below:

- Set initial parameters. The number of solutions is defined as Num in the population, $P n$ in the optimal subgroup, the dimension of the problem is defined as $D$, the optimal subgroup is defined as $\mu$, the weight of the optimal subgroup is defined as $\omega_{i}$;

$$
\sum_{i=1}^{\mu} \omega_{i}=1, \quad \omega_{1} \geq \omega_{2} \geq \cdots \geq \omega_{\mu} \geq 0
$$

- Sampling. The mean value of the optimal subgroup solution is the desired output value, and the population is normally distributed. The calculation process is as follows:

$$
\varrho_{1}^{h+1}=\text { average }^{h}+\eta^{h} H\left(0, \text { To }^{h}\right)
$$

In the population of generation $h+1$, the $i(0<i<$ Num $)$ solution is represented to $\varrho_{i}^{h+1}$; average $^{h}$ is the average of optimal subgroup solutions in the population; $\eta^{h}$ is $h$ the generation of evolutionary steps; $H(*)$ is the normal distribution function representation of data; population $h$ generation covariance matrix is represented by $T o^{h}$;

- Projection. The process of performing a projection operation for each equality constraint can be described as follows:

$$
\begin{aligned}
& \zeta_{i}^{h+1}(1+m \times(\tau-1): m \times \tau) \\
& =\zeta_{i}^{h+1}(1+m \times(\tau-1): m \times \tau)-Q^{T} \times\left(Q \times Q^{T}\right)^{-1} \\
& \times \zeta_{i}^{h+1}(1+m \times(\tau-1): m \times \tau) \times Q
\end{aligned}
$$

The $m=(1 \ldots M)$, expression of the number of variables can be expressed as $m$ in the equality constraint, $m=(1 \ldots M), M$ represents the solutions in each equality constraint, and $\tau=(1 \ldots M+1)$, when the constraints are equal, its quantity can be expressed by $\tau$. In addition, $Q=[1,1, \ldots, 1]_{1 \times N}$ is the way to represent parameter vectors;

- Select and reorganize. Select the optimal subgroup and calculate the solution set of the mean. In the optimal subgroup, the weight of the $i-\operatorname{th}\left(i=1 \ldots P_{n}\right)$ solution can be expressed as $h_{i}$, which is calculated as follows:

$$
\text { average }^{h+1}=\sum_{i=1}^{P_{N}} h_{i} \zeta_{i}^{h+i}, \sum_{i=1}^{P_{H}} h_{i}=1
$$

- Update the covariance matrix. The specific calculation process is as follows:

$$
\begin{gathered}
T o^{h+1}=\left(1-e_{1}-e_{P n}\right) T^{h}+e_{1} s_{c}^{h+1}\left(s_{c}^{h+1}\right)^{T}+e_{P n} \sum_{i=1}^{P_{n}} h_{i}\left(\frac{\zeta_{1}^{h+1}-\text { average }^{h}}{\eta^{g}}\right) \times\left(\frac{\zeta_{1}^{h+1}-\text { average }^{h}}{\eta^{g}}\right)^{T} \\
s_{c}^{h+1}=\left(1-e_{c}\right) s_{c}^{h}+\sqrt{e_{c}\left(2-e_{c}\right)\left(\sum_{i=1}^{P_{n}} h_{i}^{2}\right)^{-1}} \times \frac{\text { average }^{h} \text { average }^{h+1}}{\eta^{g}} \\
\eta^{h+1}=\eta^{h} \exp \left(\frac{e_{\eta}}{o_{\eta}}\left(\frac{\left\|\left\{s_{\xi}^{h+1}\right\|\right\|}{\|H(0, J)\|}-1\right)\right) \\
s_{\eta}^{h+1}=\left(1-e_{\eta}\right) s_{\eta}^{h}+\sqrt{e_{c}\left(2-e_{c}\right)\left(\sum_{i=1}^{P_{n}} h_{i}^{2}\right)^{-1}} \times \operatorname{To}^{h-\frac{1}{2}} \times \frac{\text { average }^{h+1}-\text { average }^{h}}{\eta^{h}}
\end{gathered}
$$

In the above calculation expression, the learning rate is expressed as $e_{1}, e_{P n}, e_{c}, e_{\eta}$; The $h$ th evolutionary step is expressed as $s_{\eta}^{h}, s_{\eta}^{h}=0$; The evolution path of the $h$ th covariance matrix is expressed as $s_{c}^{h}, s_{c}^{h}=0$. In addition, $J$ is used to represent the identity matrix, and the damping coefficient is denoted by $o_{\eta}$, Normal distribution of mathematical expectation $H\left(o, T o^{h}\right)$ use $F\|N(o, I)\|$.

The above steps describe the specific calculation process of the P-CMA-ES algorithm. This algorithm was an improvement of the CMA-ES (projection covariance matrix adaptation evolutionary strategies) algorithm, which successfully solved the equality constraint problem in the BRB and was suitable for the fault diagnosis model proposed in this paper.

# 4. Case Study 

The sub-tree of friction torque fault was the research object selected in this paper. The drop of voltage and current would slow down the speed of the flywheel, which would lead to a friction torque fault. The friction torque fault is also directly related to the shaft temperature (source used in this article from NASA). There were voltage, current, speed, shaft and friction moment data in this. One group of them could be chosen for the experiment. After selecting the data, they needed to be preprocessed. After the normalization of the data, fuzzy operator formula and ER fusion were used to obtain the data as the real value.

The fault diagnosis principle of the FFBRB flywheel system proposed in this paper included four parts: First, this paper normalized the collected data to make the data more accurate in practical application. Second, the normalized data were input into the fuzzy fault tree of the flywheel system, and the fuzzy probability of the intermediate event and the top event is calculated according to the corresponding formula. Third, this paper mapped the fuzzy fault tree to the BRB through the transformation space of the Bayesian network, so that the analysis process of the fuzzy fault tree corresponded to the inference process of BRB, and the input and output of the fuzzy fault tree correspond to the input and output of BRB, respectively. Finally, the data were handed over to the BRB for processing to realize the one-to-one correspondence between the BRB optimized value and the real value.

# 4.1. Construction of the FFBRB Fault Diagnosis Model 

### 4.1.1. The Fault Tree of the Friction Torque Fault of the Flywheel System Is Constructed

In the following description, the fault tree of the flywheel friction torque fault is preliminarily constructed to sort out the logical relationship between each fault event and determine the cause of the fault. The friction torque fault tree is shown in Figure 9:
![img-8.jpeg](img-8.jpeg)

Figure 9. Friction torque fault tree.
In the fuzzy fault tree graph of the case, the triangle fuzzy number is marked to limit the probability of each event within a range. This paper marked the meanings of each symbol in the fault tree below in advance to better describe the problem. The meanings of specific symbols are shown in Table 1.

Table 1. FFTA indicates the letters in the fault tree.


4.1.2. FFTA Is Mapped to the BRB Using the Bayesian Network as a Bridge

After the establishment of the fault tree, this paper used the bridge of the Bayesian network to map the fault tree of FFTA to several different BRBS, so that the transformation from FFTA to BRB is perfectly realized, and the FFBRB model can be initially established. The relationship between the transformed Bayesian network graph and BRB is shown in Figure 10.
![img-9.jpeg](img-9.jpeg)

Figure 10. FFTA to BRB Bayesian network transformation diagram.

# 4.1.3. Determining the Fuzzy Number of Occurrence Probability of Bottom Event and Top Event 

This step first needed to determine the trigonometric fuzzy number of the occurrence probability of the bottom event, and then calculate the trigonometric fuzzy number of the occurrence probability of the top event by using the formulas of fuzzy operators under different logic gates. The failure probability of the bottom event corresponds to the input of the BRB, and the occurrence probability of the top event corresponds to the output of the BRB, which is ready for the subsequent processing of the BRB program.

According to the previous introduction, corresponding data are divided into three groups $(a 1, a 2, a),(m 1, m 2, m)$ and $(b 1, b 2, b)$ according to the rules before. The data of the three groups are carried into the subsequent BRB, respectively, for fault diagnosis.

Triangulation fuzzy numbers of event probability in the BRB2 experiment are listed in Table 2 for reference.

Remark 3. Each event in the above table only captures the data listed in article 10, from the data in the floating range there is a probability value of $10 \%$ of the incident left and if the interval data value is less than zero, the table is down to zero, if the data interval right value is greater than 1, the table down to 1, so the data that are limited to 0 to 1 can better describe probability.

### 4.1.4. Built Initial Belief Rules

$$
\begin{aligned}
& \text { If } x_{1} \text { is } A_{1} \wedge x_{2} \text { is } A_{2} \\
& \text { Then result is }\left\{\left(\text { Top }_{1}, \beta_{1}\right),\left(\text { Top }_{2}, \beta_{2}\right),\left(\text { Top }_{3}, \beta_{3}\right),\left(\text { Top }_{4}, \beta_{4}\right)\right\} \\
& \text { with rule weight } \theta_{1}, \theta_{2}, \ldots, \theta_{K} \\
& \text { and attribute weight } \delta_{1}, \delta_{2}
\end{aligned}
$$

The initialization of BRB requires belief rule construction. In this case, the belief rule construction of BRB is as above.

Table 2. Trigonometric fuzzy number of event probability in FFTA.


# 4.1.5. Set Reference Points and Values 

In the BRB, it needed to set the reasonable reference values for the program to work properly. In this case, this paper set four reference points and reference values for each attribute, noting that the first reference value is an upper bound and the last reference value is a lower bound. The setting of reference values in BRB is shown in Table 3 above. The four numbers from left to right indicate the Very High(G), High(H), Middle(M), and Low(L) possibility of an event. The reference setting of BRB is shown in Table 3.

Table 3. Reference value of data in BRB.


Remark 4. When the median value of triangle fuzzy number interval of event occurrence probability is 0 , the reference value of the lower bound of the interval is set as a number approaching 0 , because the probability of an event cannot be negative.

# 4.2. Training and Optimization of the FFBRB Model 

### 4.2.1. Optimized Parameters and Results

Data show the optimized data of BRB2 $(b 1, b 2, b)$, and the optimized parameters in BRB are shown in Table 4.

In Tables 4-6, the optimized rule weights are expressed as RuleWF and the optimized output belief degree is expressed as BeliefF. The results of the optimization of the upper and lower bounds of the interval and the median of the interval are listed.

Table 4. Optimized parameters table in BRB2r.


Table 4 is the optimal value of the upper bound of the interval, Table 5 is the optimal value of the ideal value of the interval, and Table 6 is the ideal value of the lower bound of the interval.

Table 5. Optimized parameters table in BRB2m.


To avoid data redundancy, only four bits of data are reserved in Tables 4-6. As the same, the optimized rule weights are expressed as RuleWF and the optimized output belief degree is expressed as BeliefF.

Table 6. Optimized parameters table in BRB21.


# 4.2.2. Experimental Fitting Images 

The fitting images of experimental results and real results of interval lower bound (a1, $a 2, a)$, interval median $(m 1, m 2, m)$ and interval upper bound $(b 1, b 2, b)$ are listed below. In this paper, the fitting images of the three groups are drawn, respectively, as shown in Figure 11. The results of the three groups were processed by BRB, respectively, and compared with the real value to obtain the error, and finally unified analysis and summary.
![img-10.jpeg](img-10.jpeg)

Figure 11. Cont.

![img-11.jpeg](img-11.jpeg)

Figure 11. Fitting diagram right of experimental results and real values.
It can be seen that the results of the three groups of experiments fit well with real data. It could obtain the accuracy of each group through experiments, and then obtain the fluctuation range of experimental accuracy of the case. Then, this paper performed 10 experiments to find out the accuracy and, in this experiment, the accuracy of the three groups was $97.98 \%, 98.99 \%$ and $100.00 \%$, the average accuracy of this experiment is $98.99 \%$. It can be concluded that the accuracy of this experiment fluctuates in the range of $97.98 \%$ to $100 \%$. In general, the FFBRB model established in this paper has a good processing effect. The experimental diagnosis results are shown in Figure 11.

# 4.2.3. Other Comparative Experiments 

In this paper, ELM and BP neural networks, as the other two comparison methods of this experiment, are also used in flywheel fault diagnosis. This paper also drew the fitting images of the two control experiments, and it can be seen that the ELM and BP neural network methods are feasible, but still not as accurate as the FFBRB scheme. Among them, the difference between ELM and FFBRB schemes is relatively large, and the difference between BP neural network and FFBRB is not very large.

Two other groups of comparison experiments were conducted in this paper to compare with the FFBRB model method used in this paper, and the experimental results are shown in Figure 12 below.
![img-12.jpeg](img-12.jpeg)

Figure 12. Cont.

![img-13.jpeg](img-13.jpeg)

Figure 12. Fitting diagram of experimental results by BP method.
Figure 13 shows the diagnosis results obtained in ELM mode.
![img-14.jpeg](img-14.jpeg)

Figure 13. Cont.

![img-15.jpeg](img-15.jpeg)

**Figure 13.** Fitting diagram of experimental results by ELM method.

In this experiment, the accuracy of 10 groups of data is taken, and the average of their probability is taken as the final result. The floating line chart of the accuracy of these 10 groups is shown in Figure 14.

In the three groups of the BP method, the average accuracy of the experimental fault diagnosis value compared with the real value is 85.90%, 91.30%, and 85.50%, respectively. In the three groups of the ELM method, the average accuracy of the experimental fault diagnosis value obtained by us compared with the real value is 54.40%, 63.20%, and 65.50%, respectively.

![img-16.jpeg](img-16.jpeg)

Figure 14. Comparison of experimental accuracy of different methods.
In the three groups of the FFBRB method, the average accuracy of the experimental fault diagnosis value obtained by us compared with the real value is $99.7 \%, 98.18 \%$ and $99.39 \%$, respectively. This paper took the total average accuracy of the three groups of the three methods, and after calculation, the average accuracy of the BP method is $87.57 \%$, the ELM method is $61.03 \%$, the FFBRB method is $99.09 \%$.

To facilitate intuitive observation, this paper sorted these data into a table, as shown in Table 7 below:

Table 7. Comparison of results of different methods.


# 4.3. Experimental Conclusion 

The experiment verifies the feasibility of the FFBRB model proposed in this paper, and it can be seen from the experimental results that the FFBRB model experiment is superior to the other two methods.

In particular, the BP neural network method is used to obtain the experimental diagnosis value and the real value of the image fitting, high accuracy, but there is still a little gap compared with the FFBRB method, and the BP method cannot explain its process. The experimental results obtained by the ELM method are much different from the real values, the image fitting effect of the experimental results is relatively poor, the accuracy is relatively low, and there is a big gap compared with the FFBRB scheme. The FFBRB fault diagnosis scheme in this paper is relatively optimal among the three, and its experimental results have a good image fitting effect and high accuracy, showing advantages compared with the other two schemes.

# 5. Conclusions 

Based on BRB, a new fault diagnosis model (FFBRB) based on fuzzy fault tree analysis theory is proposed. The FFBRB model expands the expert knowledge base of BRB based on the FFTA mechanism, uses the improved BRB as a fault diagnosis tool, and incorporates an optimization algorithm to further reduce the influence of uncertain factors in the model. The model has the following characteristics:

The FFBRB model has a stronger ability to acquire expert knowledge. The FFBRB model integrates an FFTA mechanism analysis into the BRB expert knowledge base, which makes the model more capable of describing problems.

The FFBRB model has stronger analytical and reasoning ability. By training and optimizing the sample data, the model further improves the accuracy of the data, and thus makes the model more accurate.

The FFBRB model has high accuracy. Compared with traditional data-driven methods the FFBRB processing results have higher accuracy.

The feasibility of the FFBRB model is verified by experiments, and its advantages are compared with the other two methods. Based on the FFBRB model proposed in this paper, the following two aspects can be further studied in the future: (a) the theoretical transformation of the FFTA and interval BRB; (b) other methods could be used to expand the expert knowledge base in the flywheel fault diagnosis; (c) the BRB is an interpretable modeling method, which provided an effective support for the construction of interpretable deep learning models. How to effectively construct a fault diagnosis model based on a deep BRB will be the main work in the next step.

Author Contributions: X.C. and S.L. contributed equally to this work. Conceptualization, X.C. and S.L.; methodology, X.C. and S.L.; software, Y.X.; validation, X.C., S.L. and W.H.; formal analysis, X.C. and S.L; investigation, J.S.; data curation, P.Z.; writing—original draft preparation, X.C.; writingreview and editing, X.C. and W.H.; visualization, X.C.; supervision, W.H. and B.X. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported in part by the Postdoctoral Science Foundation of China under grant no. 2020M683736, in part by the Natural Science Foundation of Heilongjiang Province of China under Grant No. LH2021F038, in part by the innovation practice project of college students in Heilongjiang Province under grant no. 202010231009, 202110231024, 202110231155, in part by the graduate quality training and improvement project of Harbin Normal University under grant no. 1504120015, in part by the graduate academic innovation project of Harbin Normal University under grant no. HSDSSCX2021-120, HSDSSCX2021-29.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data sharing not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
