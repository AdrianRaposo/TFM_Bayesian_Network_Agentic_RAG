# STUDY ON RISK CONTROL OF WATER INRUSH IN TUNNEL CONSTRUCTION PERIOD CONSIDERING UNCERTAINTY 

Zhu WEN ${ }^{1}$, Yuanpu XIA ${ }^{2 *}$, Yuguo JI ${ }^{1}$, Yiming LIU ${ }^{2}$, Ziming XIONG ${ }^{2}$, Hao LU ${ }^{2}$<br>${ }^{1}$ School of Mechanical Engineering, Nanjing University of Science and Technology, Nanjing 210094, China<br>${ }^{2}$ State Key Laboratory of Disaster Prevention \& Mitigation of Explosion \& Impact, the Army Engineering University of PLA, Nanjing 210007, China

Received 25 January 2019; accepted 25 March 2019


#### Abstract

Water inrush risk is a bottleneck problem affecting the safety and smooth construction of tunnel engineering works, so the risk control of water inrush is important, however, geological uncertainty and artificial uncertainty always accompany tunnel construction. Uncertainty will not only affect the accuracy of water inrush risk assessment results, but also affect the reliability of water inrush risk decision-making results. How to control the influence of uncertainty on water inrush risk is key to solving the problem of water inrush risk control. Based on the definition of improved risk, a risk analysis model of water inrush based on a fuzzy Bayesian network is constructed. The main factors affecting the risk of water inrush are determined by sensitivity analysis, and possible schemes in risk control of water inrush are proposed. Based on the characteristics of risk control of water inrush in a tunnel, a multi-attribute group decision-making model is constructed to determine the optimal water inrush risk control scheme, so that the optimal scheme for reducing uncertainty in risk control of water inrush is determined. Finally, this system is applied to Shiziyuan Tunnel. The results show that the proposed risk control system for reducing uncertainty of water inrush is efficacious.


Keywords: water inrush risk, uncertainty, risk control system, fuzzy Bayesian network, multi-attribute decision making.

## Introduction

The importance of tunnel engineering for urban underground space development and infrastructure construction in remote areas is self-evident. Tunnel construction is developing in the direction of large burial depths, longer tunnel lines, more complex geological conditions (high water pressure, high stress, karst topographies, etc.), and facing the challenges of water inrush, collapse, and rock bursts under such complex conditions (S. C. Li, Wu, Xu, \& L. P. Li, 2017; Fraldi \& Guarracino, 2010; Tang, Wang, \& Zhang, 2010). Central and western China are typical areas where karst landforms and distribution of fault zones are developed and widespread. Water inrush accidents occur frequently during construction of various tunnels. It has become one of the most frequent geological disasters affecting the construction of tunnels and causes significant economic loss, therefore, it is of practical engineering significance to control water inrush risk and minimise the risk of water inrush during tunnel construction (Li et al., 2013; Staveren, 2009).

Risk control mainly includes risk assessment and risk decision-making. Risk assessment is the basis of risk control, and its purpose is to provide reliable decision support information. Traditional risk is defined as the combination of the consequences of risk events and their probability of occurrence. The risk assessment of water inrush based on traditional risk definition is equivalent to the assessment considering the risk of water inrush alone (Kaplan \& Garrick, 1981; Ale, 2002; X. Li \& Y. Li, 2014) tunnelling entails large-scale, complex geotechnical engineering operations. Geological uncertainty, artificial uncertainty, and model uncertainty always accompany tunnel construction. Due to the unreasonable disposition of uncertainty, risk control schemes may fail, which may lead to water inrush disasters: risk control schemes may be too conservative thus resulting in a waste of human resources, time, and cost. Aven and Renn (2009) discuss the essence of risk based on problems in engineering application, and conclude that both risk and uncertainty should be considered in the

[^0]
[^0]:    *Corresponding author. E-mail: xiayuanpu123@163.com

improved definition of risk. On the basis of the definition of improved risk, many scholars have proposed risk assessment methods for water inrush considering uncertainty. For example, Wang, Jing, Yu, Su, and Luo (2017) established a risk assessment model for water inrush in karst tunnels, and used the correlation coefficients therein to describe the uncertainty caused by random, fuzzy, and grey information. Hao, Rong, Ma, Fan, and Lu (2016) proposed an improved attribute recognition method based on Monte Carlo technology to evaluate the uncertainty in the process of risk analysis of tunnel water inrush, however, the aforementioned risk studies only describe the uncertainty in a qualitative manner, without considering artificial uncertainty, and without the basis, and measures, to reduce the uncertainty.

The study on risk control related to tunnel engineering provides a reference for describing, quantifying, and reducing the impact of uncertainty in risk control of water inrush. Yang and Qiu (2005) proposed an expected utilityentropy decision-making model (EU-E) to consider the effects of uncertainty. The risk attitude, expected consequences, and information uncertainty of decision makers can be taken into account in this model, but the model lacks effective judgement criteria (Yang \& Qiu, 2005; Fischer \& Kleine, 2007). Aiming at this problem in the EU-E model, Dong, Lu, Xia, and Xiong (2016) proposed an en-tropy-hazard model, which uses the concept of tolerance cost to analyse and control the impact of uncertainty on risk, however, the computational efficiency of the model is low, and it is difficult to determine a reasonable scheme of uncertainty control. Xia, Xiong, Dong, and Lu (2017) and Xia, Xiong, Wen, Lu, and Dong (2018) conducted sensitivity analysis based on the entropy-hazard model to narrow the scope of alternatives offered, improve computational efficiency, and selected the optimal risk control scheme based on stochastic decision theory; however, because the mechanism of water inrush during tunnel construction is complex and there are many factors influencing it, determining the exact relationship between risk factors and the probability of water inrush disaster is difficult, so the above method cannot be directly applied. In addition, risk assessment and decision-making usually require the participation of expert groups. It is necessary not only to quantify the initial linguistic information of experts accurately, but also to consider the subjective reliability of experts. In addition, a multi-attribute group decisionmaking process is then needed to optimise the risk control scheme of tunnel water inrush by taking into account the evaluation information of multiple experts in cost, duration, and safety terms (Kahraman, Onar, \& Oztaysi, 2015; Ying \& Rui-Hua, 2008).

In view of the lack of an advanced theoretical system with which to reduce uncertainty in risk control of water inrush during tunnel construction, we propose a risk control system for water inrush during tunnel construction to reduce uncertainty. In Section 1, based on the characteristics of water inrush risk during tunnel construction, combined with the advantages of Bayesian network (BN) and

MAGDM, the overall framework of water inrush risk control system to reduce uncertainty is proposed. In Section 2, the risk assessment theory based on Fuzzy Bayesian Network (FBN) is introduced and the multi-attribute group decision-making theory for constructing this decisionmaking system is established. In Section 3, taking Shiziyuan Tunnel of Chenglan Railway Section as the engineering background, we applied the risk control system of water inrush during tunnel construction, which was proposed in this paper, and verified the validity of the system, and last Section concludes.

## 1. Construction of water inrush risk control system

Reasonable risk assessment not only needs to reflect all initial information objectively, but also needs to consider factors conducive to decision-making and reflect the level of trust in risk analysts. In view of the fact that the risk of water inrush during tunnel construction is influenced by many factors, dynamic updating of risk information, exchange and feedback, leads us to propose the use of a risk analysis method based on a BN. As a common tool for risk assessment, BNs have been widely used to solve practical problems such as diagnosis, prediction and risk management in large-scale engineering projects. It can not only make use of existing information for forward and backward reasoning, update dynamic information in realtime, but also accurately determine the impact of different factors on the evaluation results. It is often used in decision support system and is considered as an effective risk analysis tool in the field of underground engineering. In addition, due to the scarcity of data related to water inrush disasters in tunnel engineering, it is important that a BN can effectively combine the characteristics of expert knowledge and empirical data, and has the ability to improve the model's ability to deal with uncertainties through the fuzzification and imprecision of probability (Heckerman, Mamdani, \& Wellman, 1995; Uusitalo, 2007; Špačková \& Straub, 2012; Eleyedatubo, Wall, \& Wang, 2010). Risk control is essentially a dynamic balance between control cost and risk level. Based on the improved entropy-hazard model, the concept of tolerable cost can be used to determine a possible risk control scheme for water inrush, and determine whether, or not, the final risk control scheme after reducing the aforementioned uncertainty is reasonable. Under the conditions of cost limits, time limits, and safety requirements, this becomes a multi-attribute group decision-making problem: based on the analysis of different decision models and the characteristics of water inrush risk control during tunnel construction, we believe that a reasonable and reliable multiattribute group decision-making model must solve the following basic problems:

1. Complete the description and quantification of uncertain information. The processing of initial information directly affects the construction of a decision model and the reliability of its results;

2. Provide a judgment of attribute weight under incomplete or insufficient decision information;
3. Complete the aggregation and judgment of multisource attribute information. In recent years, the use of evidence reasoning to aggregate information has also attracted increasing attention (Liu, Liao, \& Yang, 2015);
4. Consider the influence of decision maker subjectivity.

Based on the characteristics of water inrush risk during tunnel construction, considering the advantages of BN applied to risk analysis of water inrush during tunnel construction and the four basic problems of multi-attribute group decision-making models, we proposed a risk control system for water inrush to reduce uncertainty as shown in Figure 1. The decision-making system for water inrush risk control to reduce uncertainty can be divided into two parts: a decision support system and a decisionmaking system. First, we construct the risk analysis model for water inrush based on a BN, determine the risk factors that exert greatest influence on water inrush by way of a sensitivity analysis, and propose the possible uncertainty control scheme. Then, based on the improved en-tropy-hazard model, the tolerance cost shown in Figure 1 is used to judge, in which the undetermined equilibrium coefficient $\alpha \in[0,1]$ is used to indicate willingness to take measures to reduce uncertainty. If the relevant requirements are met, the corresponding preliminary risk warning will be carried out according to the risk assessment results determined by BN. To improve the decision-making quality of risk control of tunnel water inrush, based on the characteristics of tunnel engineering risk control, an intuitive fuzzy number is used to describe the initial group
decision-making information, and evidence theory is used to fuse information from different experts. Based on this triangular intuitive fuzzy multi-attribute decision-making model, a multi-attribute group decision-making model for risk control of tunnel water inrush is constructed, the optimal control scheme is finally determined, and the risk status is further clarified.

## 2. Analysis flow of water inrush risk control system

To control, economically and effectively, the risk of water inrush during tunnel construction, a decision-making system for risk control of water inrush to reduce uncertainty is established. The system can be further divided into a risk decision support system based on fuzzy Bayesian network and a risk decision system based on multi-attribute group decision-making.

### 2.1. Risk decision support system based on a fuzzy Bayesian network

BN mainly consists of directed acyclic graph (DAG) and related joint probability distribution (JPD). Building the Bayesian network model first requires construction of the DAG, which is a qualitative part of the model. There are two ways to determine the structure of the network:

1. Structured learning, which requires data samples of all variables;
2. Professional knowledge of the subject.

The relationship between variables and their corresponding states constitutes the quantitative part of Bayesian network. Each root node is appended with a prior
![img-0.jpeg](img-0.jpeg)

Figure 1. Risk control system for water inrush during tunnel construction considering uncertainty

probability table (PPT) and each non-root node is appended with a conditional probability table (CPT) to represent the relationship between the variables. There are two methods to estimate these probability distributions:

1. Parameter learning;
2. Expert judgment.

In the traditional BN model, the probability of occurrence of root nodes is an exact value, but the uncertainty of geological information, artificial data, and the model is the most significant characteristic of risk analysis of water inrush during tunnel construction. Moreover, in many cases, it is not enough to support accurate probability analysis, so non-probabilistic methods have gradually come to be regarded as an important supplement to probabilistic methods. Fuzzy Set Theory (FST) was first proposed by Zadeh (1965) and attracted wide attention. The fusion model of BN and FST is applied to the water inrush risk control system during tunnel construction, which can provide effective information for the rapid diagnosis and control of causal factors of possible water inrush accidents. This analysis method based on fuzzy probability is called a fuzzy Bayesian network (FBN).

Generally, the attribute function $F_{\hat{p}}(x) \in[0,1]$ is used to quantify the fuzzy variable $X$ and the uncertain information is transformed into a fuzzy number. However, it is usually difficult to give specific membership and nonmembership degrees in practical application. Therefore, improved interval intuitionistic fuzzy numbers and triangular intuitionistic fuzzy numbers are proposed successively (Atanassov, 1989; Chen \& Han, 2018). Among them, triangular intuitionistic fuzzy numbers have attracted more and more attention because they can give full consideration to affirmative, hesitant and negative behaviors when describing attribute information. Therefore, considering the convenience, reliability, and generality of calculation, triangular fuzzy numbers $F_{\hat{p}}(x)=(a, b, c)$ can be used, where a and c represent upper and lower boundaries, and b represents the most probable value (Li et al., 2017). Fuzzy edge rules and fuzzy Bayesian rules can be expressed by the following formulae:

$$
\begin{aligned}
& P\left(T=t_{j}\right)=\sum_{i} P\left(X=x_{i}\right) \otimes P\left(T=t_{j} \mid X=x_{i}\right) \\
& P\left(X=x_{j} \mid T=t_{j}\right)= \\
& \quad\left[P\left(X=x_{i}\right) \otimes P\left(T=t_{j} \mid X=x_{i}\right)\right] \varnothing P\left(T=t_{j}\right)
\end{aligned}
$$

where $T$ represents the leaf node, that is, the risk event, and $X$ represents the root node. The construction of a risk decision support system based on FBN includes five steps, as shown in Figure 2.

Because different units and individuals are involved, although the basic objectives of risk control of water inrush during tunnel construction are the same, the focus of each party is different, and the theoretically feasible risk control scheme often has unsatisfactory effect in the actual process. Therefore, it is necessary to unify the views of all parties and formulate clear risk control objectives.

The ALARP principle (Melchers, 2001) can effectively integrate resources, take into account the interests of all parties, and unify the risk control objectives of tunnel water inrush under the constraints of limited resources such as cost, time and operators. The greatest characteristic of ALARP is to adopt different risk control measures according to different risk levels, and to achieve the best risk control effect by introducing benefit ratio. Therefore, we refer to the risk acceptability criterion (ALARP) to establish a risk early warning response mechanism for tunnel water inrush, and classify the risk state of water inrush into four levels. It is also suggested that expert groups should be invited to participate in the formulation of risk control schemes or measures when the risk early warning of water inrush at levels III and IV is issued, as shown in Figure 2.

The risk decision support system based on FBN is shown in Figure 2. The identification of risk is mainly conducted through preliminary analysis of the occurrence mechanism of tunnelling risk events, to identify potential risks, risk factors and their causal relationship, and to identify root nodes, intermediate nodes, and leaf nodes. Then the fault tree or event tree of risk events is constructed and the Bayesian network structure of risk events is obtained by mapping. Fuzzy probability evaluation mainly estimates the fuzzy probability of the root nodes by collecting expert judgment information and fuzzification technology. Tunnelling risk control is a typical example of initial evaluation information scarcity and limited access to information. Language terminology is usually defined by group decision method; however, there are two main drawbacks in the process of fuzzy probability evaluation based on traditional group decision-making technology:

1. Not taking into account both expert ability and subjectivity;
2. Rough interval division (Zhang, Wu, Skibniewski, Zhong, \& Lu, 2014).
For the two aforementioned problems, the pre-processing of expert information is first carried out. Expert judgments (indicated by $\zeta$ ) can affect reliability: for example, project engineers with 30 years of work experience are more reliable than those with 5 years of work experience. The judgment ability level $\zeta$ mainly depends on professional level and work experience, so experts' judgment ability level is divided as shown in Table 1.

An expert's subjective reliability level (indicated by $\psi$ ) affects their reliability, therefore, the subjective reliability is divided into five levels: $\{1,0.9,0.8,0.7,0.6\}$ : the higher the score, the more reliable the judgement. The expert confidence index can be determined by considering the expert's judgment ability and subjective reliability level (Zhang, Skibniewski, Wu, Chen, \& Deng, 2014):

$$
\phi=\zeta \times \psi
$$

To facilitate expert judgment, the fuzzy probability is usually divided into intervals and the corresponding language terms are defined. In general, the smaller the interval, the higher the precision of the estimated probability, but too small an interval is not only unfavourable to

![img-1.jpeg](img-1.jpeg)

Figure 2. Flow chart through the risk decision support system based on a fuzzy Bayesian network

Table 1. Experts' judgment ability


experts' judgment, but also increases the difficulty of calculation. In addition, many risk events in tunnelling are of the "low probability and high risk" disaster type, so the low probability interval should be encrypted. After comprehensive consideration, we adopt the method of 11 interval divisions (Table 2).

In addition, only intervals $\left[a_{k}, c_{k}\right]$ are often considered in the process of judging probability intervals by experts (ignoring the possibility of other intervals results in the loss of some information) and because of the large number of root nodes of water inrush risk events during tunnel construction, the accumulation of information loss in the calculation process may have a significant effect on the predicted results, therefore, we regard the confidence index $\phi$ of experts as the possibility of choosing the interval $\left[a_{k}, c_{k}\right]$. The possibility of other intervals being selected is $1-\phi$. Ajmani (2012) suggested that the probability of occurrence of events tends to fluctuate around their expectations and gradually decreases as they move further from them:

$$
p_{i}=\left\{\begin{array}{cc}
\frac{\left(a_{k}-a_{k-i}\right)}{\sum_{j=1}^{k-1}\left(a_{k}-a_{j}\right)} \times \frac{1-\phi}{2} & , 1 \leq i \leq k-1 \\
\theta & , \quad i=k \\
\frac{\left(a_{12+k-i}-a_{k}\right)}{\sum_{j=k+1}^{11}\left(a_{j}-a_{k}\right)} \times \frac{1-\phi}{2} & , k+1 \leq i \leq 11
\end{array} .\right.
$$

As shown in Figure 2, prior probabilities of root nodes at different risk levels need to be determined before fuzzy probability analysis, therefore, it is necessary to fuse the probabilistic intervals with different possibilities into a triangular fuzzy number after obtaining the probability distribution associated with each expert. Assuming that there are $S$ experts, the average probability of each probability interval being selected is:

$$
P_{i}=\frac{\sum_{i=1}^{S} p_{i}}{S}
$$

where $p_{i}$ is the possibility of each probability interval

Table 2. Fuzzy probability interval division


calculated according to Eqn (4). Using Eqn (5) to calculate the probabilistic fuzzy numbers of different experts, combined with the confidence index of each expert, according to the operating rules between fuzzy numbers, the comprehensive fuzzy probabilities considering multiple experts can be obtained. The operation rules between fuzzy numbers are as follows:

$$
\begin{aligned}
& \phi \tilde{A}_{1}=(\phi a, \phi b, \phi c) \\
& \tilde{A}_{1}+\tilde{A}_{2}=\left(a_{1}+a_{2}, b_{1}+b_{2}, c_{1}+c_{2}\right)
\end{aligned}
$$

where $\tilde{A}_{1}=\left(a_{1}, b_{1}, c_{1}\right)$ and $\tilde{A}_{2}=\left(a_{2}, b_{2}, c_{2}\right)$.
Fuzzy probability analysis mainly involves risk analysis based on the functions of forward deductive reasoning, sensitivity analysis, and reverse fault diagnosis reasoning in the FBN model. Then, the fuzzy probability is converted to an exact value based on defuzzification technology. Finally, combined with the results of risk assessment, the sensitivity analysis of the root node is carried out as shown in the sensitivity formula in Figure 2. In the sensitivity formula, $T$ represents the risk state of leaf nodes, $x_{i}$ represents the risk influencing factors, and $Q_{i}$ represents the risk state of influencing factors. We then determine the most influential factors affecting the results of risk assessment, and further propose possible initial risk control programmes.

### 2.2. Risk decision support system based on a fuzzy

## Bayesian network

In the process of risk control analysis of water inrush during tunnel construction as shown in Figure 1, preliminary risk warning is carried out according to the calculated results from the decision support system based on a fuzzy Bayesian network. When a high-level (level III or IV) risk early warning is issued, the expert group must be invited to the scene according to the risk acceptability criteria (ALARP) and the risk early warning mechanism, as shown in Figure 2. Working out a risk control plan with construction, design, supervisor, and owner, is a multiattribute group decision-making process.

Table 3. Nine-level language description and triangular fuzzy numbers


Assuming that K experts are involved in decisionmaking, where $t_{k}$ represents the $k^{\text {th }}$ expert. Assuming that there are $m$ alternatives: $A=\left\{a_{i} \mid i=1,2, \ldots, m\right\}$. Assuming that the decision attributes are $\mathrm{n}: C=\left\{c_{j} \mid j=1,2, \ldots, n\right\}$. Due to the influence of work experience and educational background, the reliability of experts is different, and the importance of corresponding experts is different, so the weight of experts is different in the process of multiatribute group decision-making. In engineering practice, it is generally believed that with the accumulation of educational background and work experience, individual judgment ability will become more and more mature and stable, and the level of judgment ability will be improved accordingly. Therefore, in the process of expert group information fusion, we determine the weight of experts according to the level of experts' judgment ability as shown in Table 1. The weights of experts under attribute $c_{j}$ are $=\left\{\lambda_{k}^{j} \mid k=1,2, \ldots, K\right\}$, and $0<\lambda_{k}<1, \sum_{k=1}^{K} \lambda_{k}=1$. A risk decision-making system based on multi-attribute group decision-making is constructed as shown in Figure 3.

As shown in Figure 3, after preliminary warning based on risk assessment results, tolerance costs need to be calculated according to hazard entropy, and the effect of subjective factors of decision makers should be considered by utility theory (Blavatskyy, 2014). Firstly, the preliminary scheme is screened by tolerable cost considering utility theory, and then the expert group is invited to make multi-attribute group decision considering cost, duration and safety. For the multi-attribute decision-making problem of water inrush risk in tunnelling, much initial information cannot be quantified and can only be qualitatively described in linguistic terms. To quantify the fuzzy uncertain information, we construct an improved triangular intuitionistic fuzzy multi-attribute group de-cision-making model based on triangular intuitionistic fuzzy numbers. The model can solve the problem that it is difficult to quantify the fuzzy uncertain information in the decision-making process of water inrush risk during tunnel construction, and improve the decision-making quality under uncertain conditions. The relationship between linguistic variables and triangular fuzzy numbers is constructed as shown in Table 3. Assuming the triangular fuzzy number corresponding to the language variable $s_{x}$ is $\beta_{s_{x}}=\left(a_{s_{x}}, b_{s_{x}}, c_{s_{x}}\right)$. The triangular intuitive fuzzy number corresponding to the language variable $\left[s_{x}, s_{y}\right]$
is $\beta=\beta_{s_{x}}, \beta_{s_{t-y}}=\left(a_{s_{x}}, b_{s_{x}}, c_{s_{x}}\right),\left(a_{s_{t-y}}, b_{s_{t-y}}, c_{s_{t-y}}\right)$. Where $t=9$ and $s_{t-y}$ is the complement of $s_{y}$. The expert's initial language fuzzy information can be transformed into triangular intuitive fuzzy decision information in combination with the relationships listed in Table 3.

Let the triangular intuitive fuzzy number be $\tilde{\beta}=(a, b, c),(d, e, f)$. The expected values of membership degree, non-membership degree, and hesitation degree are:

$$
\begin{aligned}
E_{u}(\tilde{\beta})= & (a+2 b+c) / 4, E_{v}(\tilde{\beta})= \\
& (d+2 e+f) / 4, E_{v}(\tilde{\beta})=1-E_{u}(\tilde{\beta})-E_{v}(\tilde{\beta})
\end{aligned}
$$

In addition, the concept of score function is key to intuitive fuzzy decision-making. The final decision result can be determined according to the score function (Ye, 2007). It is suggested that the pessimistic scoring function be used as follows:

$$
S(\tilde{\beta})=E_{u}(\tilde{\beta})-E_{v}(\tilde{\beta})
$$

Combining Eqn (8), triangular intuitive fuzzy decision information can be transformed into an initial decision matrix $D=\left\{d_{i j}\right\}_{m \times n}$ where $d_{i j}=u_{i j}, v_{i j}$ represents the initial decision information of scheme $a_{i}$ under attribute $c_{j}$ : because of the complex decision-making environment of water inrush risk in tunnelling, it is difficult for experts to maintain complete rationality in the decision-making process. Generally, the initial decision matrix $D=\left\{d_{i j}\right\}_{m \times n}$ is transformed into intuitive fuzzy prospect value matrix $V=\left\{v_{i j}\right\}_{m \times n}$ by using the value function of prospect theory (Chen, Chin, Ding, \& Li, 2016). The value function expression in the intuitive fuzzy environment is as follows:

$$
v_{i j}=\left\{\begin{array}{cc}
\left(D_{I F S}\left(d_{i j}^{T}, o_{j}\right)\right)^{\alpha} & , d_{i j}^{T} \geq o_{j} \\
-\alpha\left(D_{I F S}\left(d_{i j}^{T}, o_{j}\right)\right)^{\beta} & , d_{i j}^{T}<o_{j}
\end{array}\right.
$$

where $\mathrm{o}_{j}=\left(u_{j}^{\alpha}, \mathrm{v}_{j}^{\alpha}\right)$ is the reference point. $d_{i j}^{T}$ and $\mathrm{o}_{j}$ are compared by using the scoring function and exact function (Xu, Wan, \& Dong, 2016), $D_{I F S}=\left(d_{i j}^{T}, o_{j}\right)$ is the intuitive fuzzy distance:

$$
\begin{gathered}
D_{I F S}\left(d_{i j}^{T}, o_{j}\right)=\left(1-\max \left(L\left(d_{i j}^{T}, o_{j}\right), H\left(d_{i j}^{T}, o_{j}\right)\right)\right. \\
\left.\min \left(L\left(d_{i j}^{T}, o_{j}\right), H\left(d_{i j}^{T}, o_{j}\right)\right)\right)
\end{gathered}
$$

where $L\left(d_{i j}^{T}, o_{j}\right)=\min \left(u_{i j}, u_{j}^{a}\right) / \max \left(u_{i j}, u_{j}^{n}\right)$,

![img-2.jpeg](img-2.jpeg)

Figure 3. Flow chart through the risk decision-making system based on multi-attribute group decision-making

$$
H\left(d_{i j}^{T}, o_{j}\right)=\min \left(1-v_{i j}, 1-v_{j}^{\sigma}\right) / \max \left(1-v_{i j}, 1-v_{j}^{\sigma}\right)
$$

In an intuitive fuzzy environment, $0.5,0.5$ is often used as a fixed reference point, but the fixed reference point cannot fully reflect the information of different attributes. Assuming that the triangular intuitive fuzzy number is $\bar{\alpha}_{i j}=\left(a_{i j}, b_{i j}, c_{i j}\right),\left(d_{i j}, e_{i j}, f_{i j}\right)$, the expected value range of membership degree is $\left[E_{\mu}\left(\bar{\alpha}_{i j}\right), E_{\mu}\left(\bar{\alpha}_{i j}\right)+E_{\pi}\left(\bar{\alpha}_{i j}\right)\right]$. Combining this with Eqn (8), the expectation matrix of triangular intuitive fuzzy numbers can be transformed into interval decision matrix $B=\left(\bar{\beta}_{i j}\right)_{m \times n}$. The interval information of all schemes under attribute $c_{j}$ is $\left\{\bar{\beta}_{i j}=\left[a_{i j}, b_{i j}\right] \mid i \in m\right\}$. The mean and variance of the endpoint values of each interval can be calculated by the following formula:

$$
\begin{gathered}
\bar{a}_{j}=\frac{1}{m} \sum_{i=1}^{m} a_{i j}, \bar{b}_{j}=\frac{1}{m} \sum_{i=1}^{m} b_{i j}, c_{j}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(a_{i j}-\bar{a}_{j}\right)^{2} \\
d_{j}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(b_{i j}-\bar{b}_{j}\right)^{2}
\end{gathered}
$$

Assuming that the attribute information is orthogonally distributed, the corresponding probability density function is:

$$
f_{j}(x)=\frac{1}{\sqrt{2 \pi} \sigma_{j}} \exp \left(-\frac{\left(x-\theta_{j}\right)^{2}}{2 \sigma_{j}^{2}}\right)
$$

where $\theta_{j}=\left(\bar{a}_{j}+\bar{b}_{j}\right) / 2, \sigma_{j}=\left(c_{j}+d_{j}\right) / 2$. Then the probability of occurrence of attribute interval $\left[a_{i j}, b_{i j}\right]$ is:

$$
\begin{aligned}
& p_{i j}=\int_{b_{i j}}^{a_{i j}} f_{j}(x) d x=\int_{a_{i j}}^{1-v_{i j}} f_{j}(x) d x \\
& \bar{p}_{i j}=\frac{p_{i j}}{\sum_{i=1}^{m} p_{i j}} ; i=1,2, \cdots, m ; j=1,2, \cdots, n
\end{aligned}
$$

Therefore, the reference point of intuitionistic fuzzy attribute $c_{j}$ can be determined by the following formula:

$$
\begin{aligned}
& U_{j}=\sum_{i=1}^{m} \bar{p}_{i j} \cdot u_{i j}, i=1,2, \ldots, m) \\
& V_{j}=\sum_{i=1}^{m} \bar{p}_{i j} \cdot v_{i j}, i=1,2, \ldots, m
\end{aligned}
$$

After obtaining the foreground value matrix $V=\left[v_{i j}\right]_{m \times n}$ of different experts, it is necessary to fuse the information from different experts. Evidential reasoning is commonly used in the field of multi-attribute decisionmaking at present. There are two main methods:

1. Pre-treatment of evidence sources;
2. Modification of evidence combination rules (Smarandache, Dezert \& Tacnet, 2011).
Modifying the combination rules may not only destroy the original rules, but also cause information loss, so it is more inclined to modify the sources of evidence and reasonably reduce information conflicts. Bao, Xie, Long, and Wei (2017) and Shang and Jiang (1997) find that the distance of evidence cannot represent conflict between bits
of information: using the concept of fuzzy cross-entropy, an improved conflict measurement method based on distance and divergence was proposed by using the concept of probability distribution (BPA). Firstly, assuming that the scheme set is a recognition framework, the foreground value information of attribute $c_{j}$ of expert $t_{k}$ can be regarded as evidence as shown in Figure 3.

$$
e_{j}(\delta)=\left\{\begin{array}{cl}
0 & , \delta=0 \\
\frac{u_{i j}\left(t_{k}\right)}{\sum_{i=1}^{m}\left(1-v_{i j}\left(t_{k}\right)\right)} & , \delta=a_{i} \\
1-\sum_{i=1}^{m} m_{j}\left(a_{i}\right) & , \delta=\Theta
\end{array}\right.
$$

Assuming that there are two independent pieces of evidence $e_{1}$ and $e_{2}$ in the recognition framework, the conflict measure coefficient $(C M)$ can be expressed as:

$$
C M\left(e_{1}, e_{2}\right)=S^{(r)}\left(S^{(r)}\left(d_{1}^{(F D)}, \operatorname{Diff} P^{(r)}\right), C E_{B P A}\right)
$$

where $d_{1}^{(F D)}$ is Jousselme evidence distance (Jousselme, Grenier, \& Bossé, 2001), $C E_{B P A}$ represents the cross-entropy of BPA (Zhang \& Jiang, 2008), and Diffp ${ }^{(r)}$ is an improved probabilistic distance:

$$
\operatorname{Diff} P^{(r)}\left(e_{1}, e_{2}\right)=\left[1-\sum_{\theta \in \Theta} \sqrt{P_{1}\left(\theta_{1}\right) P_{2}\left(\theta_{1}\right)}\right]^{r}
$$

where $r>0, P_{1}$ and $P_{2}$ represent the BPA transition probabilities of pieces of evidence $e_{1}$ and $e_{2}$. Specific expressions are available for reference (Ma \& Jiyao, 2015).

After determining the conflict measure coefficient $(C M)$, expert information is aggregated by evidential reasoning to calculate the mutual support between expert $t_{k}$ and expert $t_{l}$ under attribute $c_{j}$, and further calculate the reliability of information about attribute $c_{j}$ provided by expert $t_{k}$ as shown in Figure 3 (Yang \& Xu, 2013). Then, according to the information aggregation rules, the information from all experts in scheme $a_{i}$ under attribute $c_{j}$ can be fused. The decision information of the expert group, as based on evidential reasoning, can then be fused (fusion calculation formulae are available for reference Karwowski \& Mital, 1986).

Finally, multi-source information aggregation based on evidence reasoning (ER) is carried out on the basis of expert group decision information fusion. The fused intuitive fuzzy prospect value matrix is obtained: $V\left(v_{i j}\right)_{m \times n}=\left(u_{i j}^{v}, v_{i j}^{v}\right)_{m \times n}$ (Figure 3). The main process of multi-source information aggregation based on evidence reasoning is discussed elsewhere (Rassafi, Ganji, \& Pourkhani, 2017), and is not repeated here. The first-pass optimal scheme can then be determined by using the scoring function shown in Eqn (7).

## 3. Application and analysis of engineering cases

The main uncertainty of water inrush risk during tunnel construction comes from inadequate geological information. Taking Shiziyuan Tunnel of Chenglan Railway as the engineering background, based on the risk control

Table 4. Risk classification of root nodes


system of water inrush during tunnel construction proposed in Sections 2 and 3, we select chainages D3K87+440 to D3K87+550 for case analysis, and only consider hydrogeological factors when constructing the fuzzy Bayesian network.

### 3.1. Construction of the Bayesian network

Chainages D3K87+440 to D3K87+550 in Shiziyuan Tunnel on the Chenglan Railway mainly suffers karst water inrush, and is affected by the Wangjiaping fault zone. According to the pre-semi-quantitative risk assessment, the risk of water inrush in this area is grade III. The cause of tunnel water inrush disaster is analysed by accident tree, and the factors related to water inrush are determined as nodes. Combining the experience of experts in the field and historical data to determine the relationship between nodes, Bayesian network risk analysis model for water inrush is constructed as shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network model of water inrush risk during tunnel construction

The Bayesian network model consists of seven root nodes, three intermediate nodes, and one leaf node (Figure 4). Leaf node T represents tunnel water inrush, and the corresponding variables of the root node are listed in Table 4. To adapt to the risk status of tunnel water inrush, we divide the risk level of root node water inrush into four levels: the higher the level, the higher the risk.

### 3.2. Estimation of fuzzy probability

It is known that the risk level of water inrush in this area is level III. According to risk acceptability criteria (ALARP) and risk early warning mechanism, expert groups must be invited to participate in the formulation of risk control programs as shown in Figure 2. Five experts are invited to form an expert group. According to the method of Section 3, the confidence index of statistical experts is summarised in Table 5. Experts judge the possible state of root node variables based on the method of fuzzy probability interval partition shown in Table 2 and the existing data of Shiziyuan Tunnel, as shown in Figure 5.

Table 5. Expert confidence index


The probability fuzzification is performed as shown in Figure 2. Taking the root node $x_{1}$ (the scale of karst cave) as an example, the confidence index of expert A is 0.63 , which means that there is a possibility of 0.37 of choosing the 10 other probability intervals, and the possibility

![img-4.jpeg](img-4.jpeg)

Figure 5. Expert group's initial judgment information on root nodes
of each interval can be calculated by Eqn (4). Similarly, the probability distribution of root node $x_{1}$ at risk level I is calculated by four other experts. Then, the average probability of each probability interval is calculated by formula (5), and normalised as shown in Figure 6. Then according to Eqns (6) and (7), the probabilistic fuzzy number of root node $x_{1}$, which takes into account five experts' information, is obtained: $\hat{F}\left(x_{1}\right)=(0.0798,0.1063,0.1328)$. Similarly, the fuzzy probability of each root node at different
![img-5.jpeg](img-5.jpeg)

Figure 6. Possibility distribution of normalised probability interval
risk levels is calculated as shown in Figure 7 (the specific calculation process is not described here).

### 3.3. Risk assessment based on a fuzzy Bayesian network

According to the maximum likelihood estimation method, we determine the fuzzy conditional probability table (FCPT) of the intermediate nodes and leaf nodes in the Bayesian network risk assessment model for water inrush as shown in Figure 2. Taking the leaf node (water inrush event) as an example, as shown in Table 6, leaf nodes and
![img-6.jpeg](img-6.jpeg)

Figure 7. A priori probability of root nodes under all risk levels

risk factors are also divided into four states, which are compatible with the results of probability fuzzification of root nodes.

Table 6. Expert confidence index


After determining the conditional probability table of each node, the probability of each level of risk occurrence can be calculated by using BNT toolbox in MATLAB ${ }^{\text {TM }}$ according to Eqns (1) and (2): $P(T=1)=$ $(0.096,0.141,0.172), \quad P(T=2)=(0.206,0.253,0.307)$, $P(T=3)=(0.375,0.429,0.478), \quad$ and $\quad P(T=4)=$ $(0.181,0.237,0.293)$. Defuzzification and normalisation are then carried out, giving: $P(T=1)=0.112$, $P(T=2)=0.246, P(T=3)=0.413$, and $P(T=4)=0.229$. Therefore, water inrush is most likely to be a level III risk, which is consistent with previous risk assessment results: however, the possibility of other risk levels is also significant, so the results of current risk assessment of water inrush are highly uncertain. To improve the reliability of de-cision-making, it is necessary to reduce the uncertainty of evaluation results further.

Considering such factors as cost, human resources, time limitations, and so on, we first carry out information supplementation for risk factors with greater sensitivity. According to the sensitivity formula given in Figure 2, the sensitivity values of seven risk factors at three higher risk levels of II, III, and IV were calculated, and the mean values are shown in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Mean sensitivity of root node
From Figure 8, it can be seen that the scale of karst caves present $\left(\mathrm{X}_{1}\right)$ has the greatest impact on the risk of water inrush. In addition, the integrity of the surrounding rock $\left(\mathrm{X}_{3}\right)$, water pressure $\left(\mathrm{X}_{5}\right)$, water inflow $\left(\mathrm{X}_{6}\right)$, and the relative distance between any karst cave and the tunnel face $\left(\mathrm{X}_{7}\right)$ also exert a significant influence on the risk of water inrush, while the relative distance between a karst cave and a fracture zone $\left(\mathrm{X}_{2}\right)$ and the rock mass strength $\left(\mathrm{X}_{4}\right)$ have relatively low risk of water inrush.

### 3.4. Identify possible risk control schemes

Based on the sensitivity analysis results and the field investigation of the tunnel, the size, water pressure, and the distance between the cave and the face of the tunnel are the most important information. Candidates are selected based on these risk factors as shown in Table 7.

According to the hazard entropy calculation formula shown in Figure 3, combined with the calculated results from Section 4.3, we can get: $H\left(R_{1}\right)=1.293$. After standardisation: $H\left(R_{1}\right)=0.9326$. According to information from all parties, the maximum loss caused by inrush disaster is 10 million yuan (including the monetisation of direct and indirect economic losses). Water inrush risk is most likely to belong to level III risk: $P(T=3)=0.413$. The tolerable cost is $T_{H}=385.2$ thousand yuan without considering

Table 7. Candidate scheme


![img-8.jpeg](img-8.jpeg)

Figure 9. Initial fuzzy information

The risk attitude of decision makers. In addition, according to the investigation, the decision-maker at Shiziyuan Tunnel is of a risk-averse type, using the utility function to get u(TH) = 393 thousand yuan, in which α = 0.1. Therefore, according to the judgment shown in Figure 9, the possible risk control schemes are: a4 (x1, x5, x6, x7), a7 (x1, x5, x7), and a9 (x1, x6, x7).

### 3.5. Scheme optimisation based on multi-attribute decision making

The screening of tolerable cost cannot directly determine the most reasonable scheme. We make multi-attribute group decisions from five perspectives: c1 (cost), c2 (construction period), c3 (environment), c4 (safety), and c5 (implementation effect). The estimated cost of the initial information on cost factors is shown in Table 7.

Then, the initial fuzzy information is transformed into the initial decision matrix D = [dij]_{m×n} according to Table 3 and Eqn (8). The dynamic reference points are calculated by using Eqns (12) to (16) as shown in Table 8. For the convenience of subsequent calculation and expression, schemes a4, a7 and a9 are recorded as a1, a2, and a3, respectively. Then, according to Eqns (10) and (11), the intuitive prospect value decision information is calculated as shown in Figure 10.

Then, taking attribute c1 as an example, the conflict measure coefficient (CM) is calculated according to the conflict quantification method in Section 3 (Table 9), where parameters r = 0.5 and t = 1 are included. The computational process between other attributes c2 ~ c5 is similar to that described above, and is not discussed here.

The information fusion of the expert group is then carried out as shown in Table 10. The weights of experts


Table 8. Dynamic attribute reference points

![img-9.jpeg](img-9.jpeg)

Figure 10. Intuitive prospect value decision information

Table 9. Quantitative results of conflict between pieces of evidence under attribute $c_{1}$


can be determined according to the level of judgement ability of experts: $\lambda_{1}=0.2093, \lambda_{2}=0.186, \lambda_{3}=0.2093$, $\lambda_{4}=0.2093$, and $\lambda_{5}=0.186$.

The evidence reasoning method is then used as shown in Figure 3. The attribute information of each scheme in Table 10 is aggregated and sorted: $V\left(\overline{a_{1}}\right)=0.2628,0.4213$, $V\left(\overline{a_{1}}\right)=0.2628,0.4213, \quad V\left(\overline{a_{2}}\right)=0.3615,0.5895, \quad$ and $V\left(\overline{a_{3}}\right)=0.2172,0.4517$. These results arise from the use of formula (9) where: $S\left(\overline{a_{1}}\right)=-0.1585, S\left(\overline{a_{2}}\right)=-0.228$, and $S\left(\overline{a_{3}}\right)=-0.2345$. Therefore, scheme $\overline{a_{1}}$ (original alternative $a_{4}$ ) is more reasonable. The implementation of the water inrush risk control scheme $a_{4}$ is shown in Figure 1. Combined with supplementary information, the risk assessment of water inrush is carried out again by using a fuzzy Bayesian network, and the results are as follows: $P(T=1)=0.022, \quad P(T=2)=0.07, \quad P(T=3)=0.79$, and $P(T=4)=0.118$.

The probability of occurrence of each risk level before, and after, information supplementation is shown in Figure 11: the risk status of water inrush becomes clear after information supplementation, and the risk control scheme

Table 10. Integration of expert group information


![img-10.jpeg](img-10.jpeg)

Figure 11. The probability of occurrence of each risk level before and after information supplementation
of water inrush is thus elucidated. We continue to calculate the tolerance cost $T_{H}=370$ thousand yuan using the probability of occurrence of each updated risk level as shown in Figure 1: there is no need to reduce the uncertainty further.

## Conclusions

Water inrush has become a key problem affecting the safe construction of tunnels, and has received extensive attention, however, due to the uncertainties of geological and hydrological conditions and artificial uncertainties, the accuracy of water inrush risk assessment and the reliability of water inrush risk control schemes during tunnel construction are usually difficult to guarantee. Here, combined with data from an actual tunnel project, the methods of reducing uncertainty in the process of risk control of water inrush are analysed. The main conclusions are as follows:

1. Based on the characteristics of water inrush risk during tunnel construction, and the definition of improved risk, a risk control system for reducing uncertainty of tunnel water inrush is constructed by using improved entropy-hazard model, fuzzy Bayesian theory and multi-attribute group decision-making theory.
2. In this system, not only is the artificial uncertainty in the decision-making process of water inrush risk by introducing expert confidence index considered, but also the probability interval according to the characteristics of water inrush risk during tunnel construction is divided. Meanwhile, the possibility of all probability intervals is reasonably considered and the loss of judgment information is reduced in this system.
3. By constructing an improved triangular intuitive fuzzy multi-attribute group decision-making model, the decision-making quality under uncertain conditions is improved.
4. The application of a case study from the Shiziyuan tunnel project shows that the system is feasible and effective, which provides ideas and suggestions for solving the risk of water inrush in tunnel projects both economically and effectively.

## Acknowledgements

We thank the anonymous peer-reviewers for providing valuable suggestions leading to improvements in the written manuscript.

## Funding

This work was supported by the $<$ National Key Basic Research Programme> under Grant [number 2013CB036005]; <National Natural Science Fund Youth Project> under Grant [number 51608529].

## Author contributions

Zhu Wen and Yuanpu Xia conceived, designed, and performed the study. Yuguo Ji and Ziming Xiong collected and analysed the example used in the paper. Yiming Li and Hao Lu wrote and revised the paper together. The authors have read, and approved, the final published manuscript.
