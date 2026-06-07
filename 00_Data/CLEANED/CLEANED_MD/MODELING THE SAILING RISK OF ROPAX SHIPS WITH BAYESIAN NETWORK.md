# MODELING THE SAILING RISK OF RoPax SHIPS WITH BAYESIAN NETWORK 

Qingcheng Zeng, Luyan Yang, Qian Zhang<br>School of Transportation Management, Dalian Maritime University, China

Submitted 8 February 2013; resubmitted 21 March 2013; accepted 17 July 2013;
first publiched online 10 September 2014


#### Abstract

In this paper, a methodology based on Bayesian Network (BN) was proposed to deal with the difficulty of risk analysis in RoPax transport. Based on data collection and expert survey, BN model for RoPax sailing risk analysis was constructed first. Then the Expectation Maximization (EM) algorithm for parameter learning and Evidence Prepropagation Importance Sampling (EPIS) algorithm for reasoning were designed. Finally, a sensitivity analysis was conducted. To validate the model algorithms, a case study on the RoPax system of Bohai gulf in China was provided. Results indicate that the BN model can effectively address the problem of data deficiency and mutual dependency of incidents in risk analysis. It can also model the development process of unexpected hazards and provide decision support for risk mitigation.


Keywords: RoPax ships; risk analysis; sailing risk; Bayesian Network; accident.

## Introduction

RoPax ships have the roll-on and roll-off facilities for carrying private or commercial vehicles. Additionally, large accommodation space is designed for passengers (IMO 2008). RoPax ships usually sail on short voyages, shuttled in strait and gulf. Since the 1950s, RoPax transport has been developed rapidly. Meanwhile, RoPax ships face serious maritime transport risk. In case of an accident, it will result in enormous personal injury and severe social impact. Therefore, enhancing safety management of RoPax transport is becoming an urgent issue in maritime industry.

In order to improve the safety of RoPax transport, extensive studies have been carried out over the past few decades. Some researchers investigated the overall risk level of RoPax transport with fault tree and event tree. The relationship between ship design and accidents were also studied thoroughly. However, RoPax transport is a complicated system with data deficiency and uncertainties of incident rate. It is mainly due to the complex dynamic environment of maritime transportation. Moreover, complex dependency of various risk factors is also an important issue has not been addressed well till now. The complexity of RoPax transport brings difficulties to quantitative risk analysis. Thus, it is essential to propose a realistic and effective model reflecting up-to-date case.

In this paper, a methodology based on Bayesian Network (BN) is proposed to deal with the difficulty of sailing risk analysis in RoPax transport. The paper is organized as follows. A literature review of previous studies is presented in Section 1 and the framework of BN is provided in Section 2. Methodology based on BN for RoPax sailing risk analysis is developed in Section 3, including network construction, parameter learning, network inference and sensitivity analysis. Numerical experiments on RoPax transportation system of Bohai gulf in China is conducted in Section 4 and conclusions are provided in final section.

## 1. Literature Review

Ever since RoPax transport became part of the maritime industry, the issue of safety operation has received considerable attention. Extensive studies have been carried out for RoPax ships risk analysis (Konovessis et al. 2008; Konovessis, Vassalos 2008). As the sailing risk is related to ship structure, some researchers investigated the relationship between ship design and accidents (Konovessis, Vassalos 2007). Spanos and Papanikolaou (2012) also investigated the time dependence of survivability of RoPax ships. Santos and Soares (2002) proposed a Monte Carlo simulation method to generate the RoPax loading parameters, such as draught, centre of gravity

and permeability of deck. Based on these parameters, the ranking of ship survivability under different damage conditions was arranged and the most influential factors of ship survivability were evaluated.

As for the sailing risk, Vanem and Skjong (2004), Vanem et al. (2009) analyzed the probability of collision, grounding based on event tree method. A critical evaluation of emergency evacuation measures was performed subsequently. Furthermore, fault tree was also a frequently-used method in risk analysis (Antão, Guedes Soares 2006). For the losses assessment, Otto et al. (2002) took a specific Ro-Ro passenger ship as example to calculate the monetary loss in collision and grounding scenarios. As for the damage survivability, Konovessis and Vassalos (2007) designed a sequence of accident scenarios. In applying first-principle and lifecycle approach, the damage survivability of RoPax ships was evaluated. In addition, Guarin et al. (2009) modeled the safety level of damaged RoPax ships and the costeffectiveness of risk control measures. Existing studies on risk evaluation of RoPax transport contributes greatly to improve the overall safety, while the high uncertainty in risk analysis has not been well addressed yet.

BN is a methodology that has been widely used in fault diagnosis, reliability analysis and economic forecasting, etc. Since 2001, the application of BN is expanded to risk analysis (Weber et al. 2012). For example, Norrington et al. (2008) studied the network construction procedures intensively to improve the reliability of risk analysis. By applying the probability inference theory to the network topology, BN can be used to identify the most influential factors (Hänninen, Kujala 2012; Zhao et al. 2012). All of these indicate that BN is a powerful decision-support tool (Eleye-Datubo et al. 2006). Specifically, the application of BN in maritime industry is also promising (Montewka 2012). For example, BN has been used to evaluate the overall transportation risk of dangerous goods (Zhao et al. 2012) and oil tanker (Martins, Maturana 2013). The consequence assessment of maritime accident was also conducted by Montewka et al. (2011). Trucco et al. (2008) further integrated the Bayesian Belief Network (BBN) with fault tree by a dummy variable. The model proposed is to evaluate the effect of Human and Organizational Factors (HOF) on maritime risks.

As a powerful probabilistic inference tool in artificial intelligence, BN can be used to the comprehensive risk evaluation of RoPax transportation system. Although the application of BN in maritime sector is still at its initial stage, extensive studies have highlighted that the BN can effectively evaluate the critical event occurrence under high uncertainty.

## 2. Bayesian Network

BN, also called Bayesian Belief Network (BBN), is a power tool in risk inference. It can properly overcome the difficulty of data deficiency and high uncertainty. It can serve as a suitable tool for risk analysis.

The principle of BN can be illustrated as a Directed Acyclic Graph (DAG). The DAG consists of nodes set
and directed edges. The nodes are a set of state variables. The directed edges represent the interdependent relationship between variables, which are indicated by Conditional Probability Table (CPT). CPT is the quantitative part of BN.

A simple example of BN is given in Fig. 1, where, $X_{1}$ is the 'parent' node of $X_{3} ; X_{3}$ is the 'child' node of $X_{1}$ and $X_{2} ; X_{2}$ is the 'root' node.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Sample of BN
Let $\mathrm{X}=\left(X_{1}, X_{2}, \cdots, X_{n}\right)$ be the variable set in BN. Then the joint probability distribution of random variable set $X$ can be expressed as:

$$
\begin{aligned}
& P\left(X_{1}, X_{2}, \cdots, X_{n}\right)= \\
& \prod_{i=1}^{n} P\left(X_{i} \mid X_{1}, X_{2}, \cdots, X_{i-1}\right)= \\
& \prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
\end{aligned}
$$

where: $p a\left(X_{i}\right)$ is the parent node of $X_{i} ; P\left(X_{1}, X_{2}\right.$, $\left.\cdots, X_{n}\right)$ reflects the properties of BN. To capture the information for every possible combination of variable $P\left(X_{1}, X_{2}, \cdots, X_{n}\right)$, it can be calculated by computing the marginal probability and conditional probability. This is the noted chain rule of BN.

With limited, incomplete and uncertain information, the posterior probability of random nodes in BN can be updated given an observation variable. Hence, BN is also known as belief network. According to Thomas Bias theorem, the posterior probability can be calculated in Eq. (2):

$$
P(H \mid e)=\frac{P(e \mid H) P(H)}{P(e)}
$$

where: $e$ is an evidence, that is, a new information received from external observation. Evidence information of a random variable could cause a value change in posterior probability $P(H \mid e)$ through network propagation. $P(H)$ is the prior probability of target node, usually based on historical data and expert experience. The conditional probability density function $H$ is expressed as $P(e \mid H)$, usually a likelihood function.

## 3. Methodology

RoPax ships frequently operate in narrow coastal waters and sail at night. The specific navigation characteristic increases the sailing risk to some extent. Therefore, it is crucial to perform a risk analysis towards RoPax sailing stage. On the basis of these considerations, we define the scope of this study. In this paper, we focus on the sailing

risk during the transition and navigation in coastal waters. The loading and unloading process is out of scope.

The BN based methodology used in this paper is composed of three major modules (Fig. 2), namely: 1) BN construction, based on historical data and expert judgement; 2) Network updating, including parameter learning and network inference; 3) Risk analysis, aimed at estimating the most influential risk factors.

Details are given in Sections 3.1-3.3.

### 3.1. Bayesian Network Construction

In this paper, the RoPax sailing risk is addressed. Accident database is established according to historical accidents. For factors such as human and organizational factor, the statistical data are not sufficient. Thus, experts experience is essential. With expert judgement, the Bayesian model can lay a more accurate foundation for the relations and dependencies between incidents.

The IMO (2008) survey report on RoPax ships indicates that collision, fire/explosion, grounding and capsizing are the most serious accident scenarios of RoPax ships. Thus, these four accident categories are selected for further risk analysis. Based on data collection, the influencing factors and their relations with accident scenarios are primarily determined. Then expert judgements are used to examine the structure of BN. Experts are organized in a Delphi session to judge the logical relations among different factors. After the Delphi session, a list of 30 scenarios or failures is selected as causes of the sailing risk. Fig. 3 shows the graphical network of BN. The structure can be divided into three levels. The top-level node is total sailing risk of RoPax. The most
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flow chart of BN risk analysis
![img-2.jpeg](img-2.jpeg)

Fig. 3. Graphical network of BN for RoPax sailing risk analysis

sensitive risk factor to sailing risk of RoPax is the ultimate goal we expect to achieve. The second-level nodes are about the accident scenarios. This level consists of four types of accident, i.e. grounding, fire/explosion, collision and capsizing. This level is built for accident identification. Moreover, the third-level includes all the failures and dangerous scenarios. The failures and dangerous scenarios are exactly the basic events which result in the complexity of BN. Additionally, conditional probability which indicates the dependency correlation of variables (nodes in Fig. 3) is calculated based on historical data and expert judgements. The CPT is obtained afterwards.

### 3.2. Network Updating

Since the CPT is obtained from historical data and expert judgment, subjectivity and uncertainty exist. Thus, the conditional probability should be updated according to the real truth. At this stage, parameter learning and network inference is conducted to acquire more accurate posterior probability distribution.

### 3.2.1. Parameter Learning

Parameter learning of BN is mainly based on the existing training data. But in practice, there is hardly any complete data used for learning. Therefore, modifications based on mathematical method are essential to improve the accuracy of network parameters. Here, Expectation Maximization (EM) algorithm (Kjærulff, Madsen 2012) is applied. As an algorithm for parameter adjustment, algorithm can be used to maximise the likelihood estimation with incomplete data. By iterating the expectation step and maximization step, the EM algorithm can repair missing data and refine it gradually until the data likelihood value reaches a local optimal. The process is given in Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Flow of EM algorithm
Given the BN structure $S$; the incomplete data variable set $X, X=\left\{X_{1}, X_{2}, \cdots, X_{N}\right\}, X_{1}$ is the first incomplete data variable set; $D=\left\{D_{1}, D_{2}, \cdots, D_{N}\right\}$ is the complete data set, $D \in X$.

Step 1: Expectation step:

$$
\begin{aligned}
& N_{i j k}^{t}=E\left[N_{i j k} \mid X, \theta, S\right]= \\
& \sum_{1}^{N} p\left(v_{i}=k, p a\left(v_{i}\right)=j \mid X, \theta, S\right)
\end{aligned}
$$

where: $\theta$ is the parameter to be estimated; $v_{i}$ is the child node $i, i=\{1,2,3, \cdots, k\} ; p a\left(v_{i}\right)$ is the parent node of $v_{i}, p a\left(v_{i}\right)=\{1,2,3, \cdots, j\} ; N_{i j k}$ is the count of $\left(v_{i}, p a\left(v_{i}\right)\right)=(k, j)$. The $E$-step of the EM algorithm is to calculate the expected sufficient statistics for a complete database.

Step 2: Maximization step:

$$
\begin{aligned}
& \theta^{t}=\arg _{\theta f} \max Q\left(\theta^{t} \mid \theta\right)= \\
& \arg _{\theta^{t}} \max E\left[p(D \mid \theta) \mid X, \theta^{t}, S\right]=\frac{N_{i j k}^{t}}{\sum_{i=1}^{N_{i j k}} N_{i j k}^{t}}
\end{aligned}
$$

where: $\theta^{t}$ is the new parameter. The maximization step is to compute the maximum likelihood estimate of $\theta^{t}$, expressed by $N_{i j k}$.

### 3.2.2. Network Inference

BN inference is event-triggered. Once there is evidence or observation input, the value of the observation node will be modified. The value change can pass updating information on to other nodes. Generally speaking, the updating information is up to the mutual relations between adjacent nodes. Hence, it can extensively reflect the correlations of various nodes. Here, an Evidence Pre-propagation Importance Sampling (EPIS) algorithm proposed by Yuan and Druzdzel (2003) is used. The inference mechanism can be described as follows:

On receiving information from external sources, the evidence node will propagate the change to its adjacent nodes, by means of sending message $\lambda, \pi$. With the message $\lambda, \pi$ receiving from child nodes and parent nodes respectively, all the random variables will recalculate their confidence level, and subsequently propagate this change to their own child and parent nodes. Based on the CPT and information $\lambda, \pi$ received from adjacent nodes, all the random nodes can update its belief. This continuous propagating process will repeat until all nodes are updated, i.e. the posterior probability is equal to priori probability.

Assuming evidence $e$ is observed, the posterior probability $P(Y \mid E)$ of non-evidence nodes $Y$ is $\operatorname{Bel}(Y)$. According to the characteristic of BN inference, $\operatorname{Bel}(Y)$ can be calculated by Eq. (5):

$$
\operatorname{Bel}\left(Y_{i}\right)=\alpha \lambda\left(Y_{i}\right) \pi\left(Y_{i}\right)
$$

where: $\alpha$ is a normalization factor; $\lambda\left(Y_{i}\right)$ is the information obtained from the child nodes; $\pi\left(Y_{i}\right)$ is the information obtained from parent nodes;

$$
\lambda\left(Y_{i}\right)=\prod_{j} \lambda_{j}\left(Y_{i}\right)
$$

where: $\lambda_{j}\left(Y_{i}\right)$ is the information transferred from the $j$-th child node to node $Y_{i}$;

$$
\pi\left(Y_{i}\right)=\sum_{j} P\left(Y_{i} \mid X_{j}\right) P\left(X_{j}\right)
$$

where: $P\left(Y_{i} \mid X_{j}\right)$ is the conditional probability of $Y_{i}$ given parent nodes $X_{j} ; P\left(X_{j}\right)$ is the probability of parent nodes $X_{j}$.

### 3.3. Risk Analysis

During the risk analysis process, marginal and joint probability of all random variables are obtained, on the basis of network construction and network updating. Since the exact probability of an accident scenario can-

not be predicted precisely, due to uncertainty, investigating the cause of hazards is a reasonable and feasible approach to manage risks. Thus, a sensitivity analysis is carried out. By changing the confidence level of observed or evidence nodes uniformly, the posterior probability of target nodes (i.e. the sailing risk of RoPax) is obtained. Under this high-level and generic risk analysis, preventive measures can be proposed pertinently for de-cision-makers, and thus improve risk defence capabilities of RoPax transport.

## 4. Numerical Experiments

The RoPax transport of Bohai gulf in China is selected to illustrate the validity of proposed method in this paper. The Bohai gulf has a northern climate. Rough seas conditions, fleet aging and other complex causes result in high accident frequency. Since 1989, there is a total of 16 major accidents happened, as presented in Table 1.

With high accident frequency and high losses, the RoPax shipping safety in Bohai gulf is receiving increasing attention.

Based on data collection and expert survey, the qualitative model and quantitative models of BN are developed. Then the key factors affecting the sailing risk of RoPax ships in Bohai gulf are provided. Details are given as follows.

### 4.1. Data Collection

Data such as the meteorological and hydrological conditions, port conditions, fleet conditions, accident situations etc. are collected first. Then the database of Bohai gulf RoPax transport is established. The main data sources are China Maritime Safety Administration, IMO report, statistical yearbook and relevant accident reports. Part of the data is presented in Table 1. According to the database, the initial BN model is developed.

Table 1. 1989-2010 RoPax ship's accidents in Bohai gulf ${ }^{1}$


Notes: 1 - part of the collected data is included in the Table; 2 - incomplete statistical data.

### 4.2. Expert Judgement

For data which is not available, a Delphi session is organized to modify the initial model. Firstly, on-the-spot investigation is implemented to get information of the RoPax sailing circumstances in Bohai gulf. A total of 10 RoPax shipping companies are in the investigation list, such as Shandong Bohai Ferry Co., Ltd.; Dalian Port group and Dalian Shipping Group Co., Ltd. and China shipping liner Company Limited etc. Secondly, specialized staffs such as captains and mates are surveyed by interview and questionnaire. A few possible conditional probability of every node is given to be discussed. The reasonability of CPT is judged as well. If the experts do not think the probability is reasonable, then we will get a new one by discussing. Subsequently, the possible consequence of every incident is obtained.

### 4.3. Model Calculation

The software package of Genie 2.0 (Decision Systems Laboratory 2006) is used to construct the network and update belief. Based on expert suggestions and node information, the qualitative model for BN of RoPax sailing risk in Bohai gulf is developed (Fig. 3). Then the sample data getting from the accident database and expert questionnaires are input into Genie 2.0. The values in CPT are set manually, which is the quantitative model of BN. Considering the complexity of the CPT, detailed description is not possible within the scope of this paper, thus only part of the CPT is presented (Table 2). All random variables are discretized to be used in parameter learning procedure. The EM and EPIS algorithm in Genie 2.0 are applied for network updating. All these work is done to lay foundation for further sensitivity analysis.

### 4.4. Result Analysis

In order to evaluate the sailing risk level of RoPax transport in Bohai gulf, appropriate risk acceptance criteria should be established prior to any actual risk analysis. According to MSC 72/16 (IMO 2000) and SAFEDOR-D-4.5.2-2005-10-21-DNV (Skjong et al. 2005; SAFEDOR 2005), the risk acceptance criteria for RoPax ships can be divided into three categories (Fig. 5): Negligible, ALARP (As Low As Reasonably Practicable), Intolerable. The negligible risk can be broadly acceptable, while the intolerable risk must be reduced irrespectively of cost. In addition, the ALARP (As Low As Reasonably Practicable) risk should be reduced as long as the risk reduction is not disproportionate to the cost. In gen-
![img-4.jpeg](img-4.jpeg)

Fig. 5. 1989-2010 RoPax F-N curve of Bohai gulf
eral, the ALARP principle is found to be in reasonable agreement.

The Bohai RoPax historical sailing risk is illustrated in the $\mathrm{F}-\mathrm{N}$ curve in Fig. 5. $\mathrm{F}-\mathrm{N}$ curve is a graph that plots the number of fatalities, N , towards the probability of accidents with N or more fatalities. Fig. 5. shows the F-N data of Bohai RoPax sailing risk during 1989-2010. Apparently, the FN curve is in the high ALARP and Intolerable risk region. Some preventative or risk control measures should be taken to reduce the potential risk.

Generally, a preliminary survey into the cause of accident is more important than taking exclusively risk control measures. Thus, a further sensitivity analysis is carried out for hazards identification. In this paper, grounding, fire/explosion, collision and capsizing are set as observation nodes respectively. Change their prior probability from 0 to 1 uniformly and update the posterior probability of RoPax sailing risk node. Then the overall risk level can be estimated with its posterior probability multiplied by consequences. The risk level is expressed by the potential loss of lives. Results are given in Fig. 6.

Results indicate that fire and explosion is the most sensitive risk factor to RoPax sailing risk, compared to grounding, collision and capsizing. That is, it is most likely to result in high RoPax sailing risk when exposed to high fire and explosion risk. The result is consistent with the fact that fire accident of Bohai RoPax transport happened more frequently and severely in the last two decades. Due to RoPax's dual characteristics of passenger and cargo carrier, RoPax has specific fire risks compared to other ship types. With a large number of passengers on board, there is little activity space in cargo

Table 2. Sample of the CPTs in the BN model


and accommodation compartment. In case of fire or explosion, passengers can easily get panic. Subsequently, the evacuation cannot be preceded successfully.

To effectively reduce the fire and explosion risk, a further sensitivity analysis is conducted to identify the major hazards or failures (Fig. 7). Similarly, the potential loss of lives can be calculated. It can be seen that potential loss of lives fluctuates remarkably when the probability of leakage of dangerous goods changes uniformly. Thus, leakage of dangerous goods is the major sensitive hazard to the fire or explosion accident. Therefore, strengthening safety management, especially the management of dangerous goods on RoPax, is the main guidance for RoPax sailing risk mitigation.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Sensitivity analysis of four risk factors over the probability of RoPax risk
![img-6.jpeg](img-6.jpeg)

Fig. 7. Sensitivity analysis of hazards over the probability of fire/explosion risk

## Conclusions

In this paper, a BN-based methodology for RoPax sailing risk analysis is developed. Numerical experiments on Bohai gulf RoPax transport illustrate the efficiency of the proposed BN-based methodology. By systematically describing the relationship between random variables, BN can make the utmost of the insufficient historical data for risk calculation. It is a supportive tool in decision making.

The valuable output of this paper is the most sensitive hazards contribute to the total risk level rather than the value of exact risk level. Thus, the model proposed in this paper enables a better understanding of the failure mechanism of RoPax transportation system. It can guide the decision-makers to take relevant risk control measures for safety management.

Finally, in addition to the sailing process, the roll on and roll off process of RoPax transport also have potential risks, but is out the scope of this study. Hence, a further study of dynamic BN applied to the whole process of RoPax shipping should be considered.

## Acknowledgements

This work is supported by the National Natural Science Foundation of China (Grant No 71001012), the Program for New Century Excellent Talents in the University of China (Grant No NCET-11-0859), and the Program for Excellent Talents in the University of Liaoning (Grant No LJQ2013057).
