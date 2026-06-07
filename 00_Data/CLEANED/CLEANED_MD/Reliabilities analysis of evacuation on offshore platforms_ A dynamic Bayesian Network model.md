# LJMU Research Online 

Wang, Y, Wang, K, Wang, T, Li, XY, Khan, F, Yang, Z and Wang, J
Reliabilities analysis of evacuation on offshore platforms: A dynamic Bayesian Network model
http://researchonline.ljmu.ac.uk/id/eprint/15028/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Wang, Y, Wang, K, Wang, T, Li, XY, Khan, F, Yang, Z and Wang, J (2021) Reliabilities analysis of evacuation on offshore platforms: A dynamic Bayesian Network model. Process Safety and Environmental Protection, 150. Dd. 179-193. ISSN 0957-5820

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Reliabilities analysis of evacuation on offshore platforms: A dynamic Bayesian Network model 

Yanfu Wang ${ }^{1,2}$, Kun Wang ${ }^{1}$, Tao Wang ${ }^{1}$, Xi Yan Li ${ }^{1}$, Fasial Khan ${ }^{3}$, Zaili Yang ${ }^{2}$, Jin Wang ${ }^{2}$<br>${ }^{1}$ China University of Petroleum, College of Mechanical and Electronic Engineering, Department of Safety Science and Engineering, Qingdao, China<br>${ }^{2}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, Liverpool, UK<br>${ }^{3}$ Centre for Risk, Integrity and Safety Engineering (C-RISE), Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St. John's, NL A1B 3X5, Canada


#### Abstract

An offshore platform is naturally vulnerable to accidents, such as the leakage of dangerous chemicals, fire and explosion because there are a lot of oil and gas, where all the equipment and pipes are squeezed into a limited area. Escape, Evacuation, and Rescue (EER) plans play a vital role as the last barrier to ensure the safety of personnel in the event of a major accident. As a result, the main contributors leading to evacuation failure are analyzed in this study to prioritize technology development needed to select a robust EER strategy. The scope of this research focuses on the quantitative analysis of various EER strategies on offshore platforms. In this research, a reliability prediction model of emergency evacuation is established for offshore platforms based on the K2 structure learning algorithm and a Bayesian network parameter learning method. The conditional probability tables of each node are determined by combining the Bayesian estimation method and a junction tree reasoning engine. The reliability of emergency evacuation on a platform is predicted using a dynamic Bayesian network model. The transition probability is determined through a Markov method. The main factors leading to evacuation failure are investigated using the diagnostic reasoning method of Bayesian Network.


Key words: K2 algorithm, Dynamic Bayesian network, Reliability prediction of successful evacuation, Analysis of influencing factors.

## 1 Introduction

There are a large number of leaking sources and flammable substances on offshore platforms. In the presence of ignition, material leakage may give rise to a catastrophic fire or an explosion. After the accidents, emergency evacuation plays a vital role in safeguarding the lives of personnel ${ }^{[1]}$. Unsuccessful evacuation would cause catastrophic consequences. Examples include the Piper Alpha platform disaster, the Alexander L. Kielland accommodation platform collapse and the Ocean Ranger tragedy ${ }^{[2-4]}$. Therefore, it is necessary to investigate the main factors influencing emergency evacuation and develop a model capable of predicting the probability of successful evacuation.

The studies about evacuation on offshore platforms can be broadly divided into qualitative and quantitative analysis. In qualitative analysis, the personnel evacuation process is usually researched in terms of route selection ${ }^{[5]}$, moving speed and typical behaviors of participants ${ }^{[6]}$. The evacuation, escape and rescue (EER) system contains the entire process from the beginning of the movement due to an accident to a safe place, related works have been done to analyze the effectiveness of the system on offshore platforms ${ }^{[7-9]}$. Quantitative analysis of evacuation is also essential, mainly containing the effects of environmental conditions and human behaviors on the evacuation process. Related studies include evaluating the evacuation performance of each plan considering the total evacuation time ${ }^{[5][10]}$ or the environmental conditions influencing the evacuation, such as smoke concentration ${ }^{[6]}$, temperature, visibility and thermal radiation ${ }^{[11]}$.

It is notable that there has been a growing research interests in Human and Organization Factors (HOFs), which contribute to the success/failure of evacuation in many offshore accidents ${ }^{[12]}$. Many qualitative studies have been conducted to investigate the effects of HOFs on the evacuation operation of offshore platforms ${ }^{[12-14]}$. Human error was quantitatively analyzed considering its probabilities ${ }^{[15]}$ and risks ${ }^{[16]}$ during the evacuation process on offshore platforms. Musharraf proposed a human behavioral model to simulate the response of general personnel during emergency situations ${ }^{[17]}$. Some software tools such as Pathfinder were used to analyze the flow rate and usage of each escape stairway during the evacuation process ${ }^{[11]}$.
Among the methods used to carry out qualitative and quantitative analysis of evacuation on offshore platforms, Bayesian Network (BN) has been attracting particular attentions ${ }^{[8,18-21]}$ because of its backward diagnosis and forward prediction analysis ability ${ }^{[22]}$. Usually, BN is combined with other methods, such as HOFs ${ }^{[23]}$, Reason's "Swiss cheese" model ${ }^{[24]}$,

Binomial distribution ${ }^{[25]}$, Human Reliability Analysis ${ }^{[26]}$, or Analytic Hierarchy Process to satisfy different purposes. However, there has been no well-known approach for dealing with expert judgment ${ }^{[27]}$. This is particularly true when considering the increased complexity of systems and the subjective nature of expert opinions. Thus, it is required to deal with subjectivity during the expert elicitation process, and many researchers have made some explorations. For example, a Decision Making Trial and Evaluation Laboratory (DEMATEL) technique can deal with uncertainty during the expert elicitation process. Combining with fuzzy set theory, fuzzy DEMATEL has been used to deal with ambiguity and uncertainty of human thinking by many researchers ${ }^{[27,28]}$. A Fuzzy Bayesian Network methodology is developed to deal more effectively with uncertainty for overcoming the utilization of crisp probabilities in assessing uncertainty ${ }^{[29]}$. Usually, a Fuzzy Bayesian Network is combined with other models, such as the Human Factor Analysis and Classification System, to deal with data and model uncertainty ${ }^{[30]}$.

In this research, the K-2 structure learning algorithm is used to build a BN model to avoid the subjectivity of expert judgments. Based on the historical data, the Conditional Probability Tables of a BN are determined by integrating a Bayesian estimation method with a junction tree inference engine. The remainder of this research is organized as follows. Section 2 briefly analyzes the main influencing factors of the emergency evacuation process on offshore platforms. In Section 3, the probabilistic prediction model of successful emergency evacuation is proposed through the structure learning and parameter learning of a BN model. In Section 4, the dynamic probability of emergency evacuation is predicted using a dynamic BN model followed by an analysis to prioritize the influential factors before the conclusions in Section 5.

# 2 Main influencing factors of evacuation process 

### 2.1 Emergency evacuation process on offshore platforms

Safe and efficient evacuation on offshore platforms has been a significant concern between stakeholders and emergency professionals. Evacuation is defined as leaving an offshore installation during emergency in a systematic manner without directly entering the sea ${ }^{[31]}$. The emergency evacuation process on offshore platforms is shown in Fig. $1^{[2,15,25,31]}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1 The evacuation process on offshore platforms
After an accident happened, personnel should judge whether emergency evacuation is required and deal with accidents as quickly as possible. After the decision to muster is made, the personnel move along the egress route according to the PA instructions and assemble to the designated muster stations and register. After evaluating the state of sea and lifeboat, personnel leave the installation using the primary and preferred means, helicopter, or using the primary mainstay means.

### 2.2 Screening the factors influencing emergency evacuation

314 accidents in the Gulf of Mexico during 2003-2016 ${ }^{[32,33]}$ are statistically analyzed to identify the main factors influencing emergency evacuation. At the beginning, the influencing factors indices that affect the evacuation are selected as many as possible to make the index system comprehensive. However, too many indicators may cause redundancy and increase the model's complexity. If there is a collinearity between the indicators, it may lead to redundancy. Therefore, it

is very important to analyze the correlation and screen the primary indices. All the accidents data is analyzed using the SPSS software to determine the correlation among the factors in the first column of Table 1. Some factors are eliminated to avoid the collinear effects between the factors. The main factors affecting evacuation are classified and screened as shown in the second column of Table 1.

Table 1 Classification of factors affecting safety evacuation



# 3 Modelling approach 

The construction of a BN model usually includes three ways: (1) The structure of BN is determined subjectively according to experts' experience, which is usually called a naive Bayesian network; (2) The structure is determined by combining sample data with machine learning; (3) The structure is determined by combining the above two methods based on experts' experience. It is subjective if a BN structure is built completely relying on expert experience. The third way above is selected in this research.

### 3.1 Structure learning with K2-algorithm

A number of different methods are proposed for learning a structure of BN from a dataset, such as the Expectation-Maximization (EM) algorithm ${ }^{[35]}$, Evolutionary algorithms ${ }^{[36]}$ and Gibbs sampling-based algorithms ${ }^{[37]}$. A scored-based method proposed by Cooper et al. ${ }^{[38]}$ is wellknown as the K2 structure learning algorithm, which has become one of the most representative structural learning algorithms. The K2 algorithm ${ }^{[36]}$ is a greedy search algorithm that can be used to determine the network structure of BNs from historical accident data. It attempts to select the network structure that maximizes the network's posterior probability. The K2 algorithm reduces computational complexity by requiring a prior ordering of nodes as input, from which the network structure will be determined. In the K 2 algorithm, the candidate parent $\mathrm{Pa}_{\mathrm{i}}$ for node $\mathrm{X}_{\mathrm{i}}$ is initially set to be an empty set. Each node is visited according to the sequence specified in the prior ordering and $\mathrm{Pa}_{\mathrm{i}}$ is added as the parent node of node $\mathrm{X}_{\mathrm{i}}$ if the addition of the parent node maximizes the score of the network.

Given a database D , the K 2 algorithm searches for the BN structure G with maximal $\mathrm{P}(\mathrm{G} \mid \mathrm{D})$, where $\mathrm{P}(\mathrm{G} \mid \mathrm{D})$ is the probability of network structure G given the database D . Let $\mathrm{V}(\mathrm{G})$ be a set of $n$ random variables, where a variable $\mathrm{Vi} \in \mathrm{V}(\mathrm{G})$ has ri possible value assignments vik where $\mathrm{k}=1, \ldots, \mathrm{ri}$. Let D be a database of $m$ cases, where each case contains a value assignment for each variable. Let G denote a DAG representing the structure of a BN, and let GP be the associated set of conditional probability distributions (CPD). Each node $\mathrm{Vi} \in \mathrm{V}(\mathrm{G})$ has a set of parents $\pi(\mathrm{Vi})$. Let $\mathrm{w}_{\mathrm{ij}}$ denote the $j_{\text {th }}$ unique instantiation of $\pi\left(\mathrm{V}_{\mathrm{i}}\right)$ relative to D . Suppose there are $\mathrm{q}_{\mathrm{i}}$ unique instantiations of $\pi\left(\mathrm{V}_{\mathrm{i}}\right)$. Define $\mathrm{N}_{\mathrm{ijk}}$ to be the number of cases in D in which variable $\mathrm{V}_{\mathrm{i}}$ has the value $\mathrm{v}_{\mathrm{ik}}$ and $\pi(\mathrm{Vi})$ is instantiated as $\mathrm{w}_{\mathrm{ij}}$. Let

$$
N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}
$$

Given a BN structure G, assuming that the cases occur independently and the conditional probability density function $\mathrm{f}(\mathrm{GP} \mid \mathrm{G})$ is uniform, then it follows that ${ }^{[39]}$

$$
P(G, D)=P(G) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}}\left(r_{i}-1\right)!/\left(N_{i j}+r_{i}-1\right)!\prod_{k=1}^{r_{i}} N_{i j k}!
$$

where, n is the number of the BN's nodes;

$$
\mathrm{q}_{\mathrm{i}}=\prod_{\mathrm{j}, \mathrm{n}} \Gamma_{j}
$$

The K2 algorithm looks for a network structure G that maximizes $\mathrm{P}(\mathrm{G}, \mathrm{D})$. In particular, assuming that an ordering on the variables is available and that all structures are equally similar, it adopts a greedy method for maximizing $\mathrm{P}(\mathrm{G}, \mathrm{D})$. This method consists of, for every node $\mathrm{V}_{\mathrm{i}}$, searching for the set of parent nodes that maximizes the function ${ }^{[39]}$ :

$$
g\left(i, \pi\left(V_{i}\right)\right)=\prod_{j=1}^{q_{i}}\left(r_{i}-1\right)!/\left(N_{i j}+r_{i}-1\right)!\prod_{k=1}^{r_{i}} N_{i j k}!
$$

The K2 algorithm starts by assuming that a node lacks parents, after which in every step it adds incrementally the parent whose addition mostly increases $\mathrm{g}(\mathrm{i}, \pi(\mathrm{Vi})$ ).

The K2 algorithm stops adding parents to a node when any of the following conditions is met ${ }^{[37]}$ :

1) The maximum number of parent nodes for that particular node is reached (This number is specified for each node. A suitable number for this is " $\mathrm{n}-1$ ").
2) There are no more possible parent nodes to add.
3) The addition of a single parent cannot increase the score.

# 3.2 Learning of the structure 

The task of structure learning for BN refers to the determination of the directed acyclic graph (DAG) based on historical data. There are two major approaches for the structure learning: scorebased approach and constraint-based approach ${ }^{[40]}$. For the score-based approach, a criterion is firstly defined to evaluate how well the BN model fits the data, and then a search is conducted over the space of the DAG for a structure with a maximal score. In this way, the score-based approach essentially for solving a search problem consists of two parts: the definition of a score metric and the search algorithm ${ }^{[41]}$. Based on the statistical analysis of the historical accidents data ${ }^{[31-34]}$, the sequences of the screened factors are determined as shown in Table 2.

Table 2 Factors and their sequences


![img-1.jpeg](img-1.jpeg)

The K2 algorithm is used to carry out the structure learning of a BN model. A pseudo code representation of the K2 algorithm is shown in Appendix 1. By testing the number of parent nodes, it is found that the structure keeps stable when the maximum number of the parent nodes is larger than 10. After the sequences of the factors and the maximum number of parent nodes are determined, the structure of a BN model can be obtained using Full BNT-1.0.4 of MATLAB software as shown in Fig. 2. The number of the factors in Table 3 is the same as the one in Fig. 2.
![img-2.jpeg](img-2.jpeg)

Fig. 2 Structure learning results of K2 algorithm
Based on the above structure learning results, a reliability prediction model of the evacuation process is built using the NETICA Software tool as shown in Fig. 3. The prior probability of each

node is provided based on the statistics of the historical data ${ }^{[31-34]}$.

![img-3.jpeg](img-3.jpeg)

Fig. 3 Reliability prediction model of emergency evacuation

# 3.3 The parameter learning of BN 

In addition to the DAG structure, which is often considered as the "qualitative" part of the model, one needs to specify the "quantitative" parameters of the BN model. The parameters are described in a manner which is consistent with a Markovian property, where conditional probability distribution at each node depends only on its parents ${ }^{[42]}$. Section 3.1 describes how to build the basic structure of a BN model, that is, how to define nodes and their interdependence. This section investigates how to define the relationships between the nodes in Fig. 3.

For discrete random variables, this conditional probability is often represented by a table, listing the local probability that a child node takes on each of the feasible values for each combination of values of its parents. The joint distribution of a collection of variables can be determined uniquely by these local conditional probability tables (CPTs). Often these CPTs include parameters that are unknown and need to be estimated from historical data, e.g., via the Maximum Likelihood approach, direct maximization of the likelihood, expectation-maximization algorithm and Bayesian estimation. The Bayesian estimation method is aimed to minimize the posterior expected value of a loss function. The advantage is that good estimation results will be achieved if there is sufficient information. It can also be used when small data records are available initially as the estimation can be sequentially improved when new data becomes available. The Bayesian estimation method is therefore adopted in this research to carry out parameter learning based on the historical accident data.

A BN consists of a DAG $\mathrm{G}=(\mathrm{V}, \mathrm{E})$ whose nodes $\mathrm{V}=\{\mathrm{V} 1, \mathrm{~V} 2, \mathrm{~V} 3, \ldots, \mathrm{Vn}\}$ correspond to a set of random variables, and whose arcs E represent the direct dependencies between these variables. Let $r_{i}$ denote the cardinality of Vi , and $q_{i}$ represent the cardinality of the parent set of Vi . Let $\theta_{i j}$ denote $\mathrm{P}(\mathrm{Vi} / \mathrm{pa}(\mathrm{Vi})=\mathrm{j})$.

The k -th probability value of the conditional probability distribution of $\theta_{i j}$ can be represented as $\theta_{i j k}=P(\mathrm{Vi}=\mathrm{k} / \mathrm{pa}(\mathrm{Vi})=\mathrm{j})$, where $\theta_{i j k} \in \theta, 1 \leqslant \mathrm{i} \leqslant \mathrm{n}, 1 \leqslant \mathrm{j} \leqslant \mathrm{q}_{\mathrm{i}}$ and $1 \leqslant \mathrm{k} \leqslant \mathrm{r}_{\mathrm{i}}$. Assuming $\mathrm{D}=\{\mathrm{D} 1$, $\mathrm{D} 2, \ldots, \mathrm{DN}\}$ is a dataset of fully observable cases for a BN , then $\mathrm{D}_{\mathrm{f}}$ is the $l$-th complete case of D , which is a vector of values of each variable. The loglikelihood function of $\theta$ given data D is ${ }^{[39]}$ :

$$
l(\theta \mid D)=\log P(D \mid \theta)=\log \prod_{l} P\left(D_{l} / \theta\right)=\sum_{l} \log P\left(D_{l} / \theta\right)
$$

Before seeing any data from the dataset, the Dirichlet distribution can be applied to represent the prior distribution for parameters $\theta_{i j}$ in the BN. The hyper-parameter $\alpha_{i j k}$ of Dirichlet follows the uniform prior setting by default. It has the following equation:

$$
P\left(\theta_{i j}\right)=\frac{1}{Z_{i j}} \prod_{k=1}^{r_{i j}} \theta_{i j k}^{\left(\alpha_{i j k}-1\right)}\left(\sum_{k} \theta_{i j k}=1, \theta_{i j k} \geq 0, \forall_{k}\right)
$$

where, $Z_{i j}$ is a normalization constant to ensure that $\int_{0}^{1} P\left(\theta_{i j}\right) d \theta_{i j k}=1$.
A hyper-parameter $\alpha_{i j k}$ can be thought of as how many times the expert believes he/she will observe $\mathrm{Xi}=\mathrm{k}$ in a sample of $\alpha_{i j}$ examples drawn independently at random from distribution $\theta_{i j}$.

The maximum posteriori estimation for $\theta$ given data can be introduced ${ }^{[43]}$ :

$$
\begin{aligned}
P(\theta \mid D) \propto & P(D \mid \theta) P(\theta) \propto \prod_{i j k} \theta_{i j k}^{\left(N_{i j k}+\alpha_{i j k}-1\right)} \\
& \theta_{i j k}^{*}=\frac{N_{i j k}+\alpha_{i j k}-1}{N_{i j}+\alpha_{i j}-1}
\end{aligned}
$$

Since there are many conditional probability tables required for the associated nodes, node 27 "human behavior", is taken as an illustrative example. Node 27 "human behavior" directly depends on node 8 "personnel attitude", node 14 "lack of safety awareness" A8, node 15 "lack of training exercise", node 16 "wrong operation", node 19 "communication", node 20 " response delay", node 21 "forget", node 23 "physical quality", node 25 "misjudgment", and node 26 "improper evacuation path". Each of these nodes has two states, If the "Bad" state of node 8 "personnel attitude", node 19 "communication", node 23 "physical quality" is set as " 1 ", and the "Yes" state of other nodes are set as " 1 ", then the conditional probability of node 27 "human behavior" can be calculated. The learning process of calculated parameters is shown in Appendix 2:

After parameter learning, the probability distribution of node 27 "human behavior" is obtained as follows: ans $[:,:,:,:,:,:,:,:,:,:, 1]=0.9910$

$$
\text { ans }[: .: .: .: .: .: .: .: .2]=0.0090
$$

The above results show that when node 8 "personnel attitude", node 14 "lack of safety awareness", node 15 "lack of training exercise", Node 16 "wrong operation", Node 19 "communication"1, Node 20 "response delay", Node 21 "forget", Node 23 "physical quality", Node 25 "misjudgment", and Node 26 " improper evacuation path" are given $100 \%$, the state of "Human Behavior" of node 27 , is " 1 ", that is, the state is "Bad" and the probability of is 0.9910 . Correspondingly, the state of node 27 "human behavior" is " 2 ", that is, the state is "Good", the probability is 0.0090 .

# 4 Dynamic reliability prediction of emergency evacuation and analysis 

The dynamic probability prediction model of emergency evacuation is established as shown in Fig. 4. The proposed Dynamic Bayesian Network (DBN) model contains 10-time segments, and the time interval between two consecutive time segments is 1 year.

### 4.1 Transition probability

It is known that the key challenge for DBN is to define transition probabilities when the status values of parent nodes change over time.

Taking equipment factors as an example, there are two levels: "Yes" and "No". "Yes" represents this equipment fails. "No" indicates that this equipment is in good condition. The transition probability from "No" to "Yes" is represented by the failure probability, which can be calculated using the failure rate of this equipment $(\alpha)$. The transition from "Yes" to "No" means that the equipment is repaired. The transition probabilities can be estimated using the repair rate of this equipment $(\beta)$.

The transition probabilities of equipment factors without considering the repair rate are shown in Table 3. $\Delta t$ stands for the time interval between two consecutive time segments (1 year).

Table 3 State transition probability without considering repairs


The transition probabilities of equipment factors considering repairs is shown in Table 4.
Table 4 State transition probability considering repairs


Human error is a random variable. Assume that this random variable is a counting process which meets the Poisson distribution ${ }^{[45]}$. The average number of human errors per unit time is assumed as $\lambda$, the probability that human error occurs $n$ times during $\Delta t$ can be expressed by:

$$
P\{N(t+\Delta t)-N(t)=n\}=e^{-\lambda t} \frac{(\lambda t)^{n}}{n!}
$$

If human errors occur n times till t , the probability that human error does not occur from t to $\mathrm{t}+\Delta \mathrm{t}$ can be calculated as:

$$
\begin{aligned}
& P\{N(t, t+1)=n o \mid N(t)=y e s\}=\frac{P\{N(t)=n, N(t+\Delta t)-N(t)=0\}}{P\{N(t)=n\}} \\
& =\frac{P\{N t=n\} P\{N(t+\Delta t)-N(t)=0\}}{P\{N(t)=n\}} \\
& =P\{N(t+\Delta t)-N(t)=0\} \\
& =e^{-\lambda \Delta t}
\end{aligned}
$$

![img-4.jpeg](img-4.jpeg)

Fig. 4 Dynamic reliability prediction model of emergency evacuation on offshore platform

$$
\begin{gathered}
P\left(X_{t+1}=\text { yes } \mid X_{t}=n o\right) \\
P\left(X_{t+1}=\text { yes }, X_{t}=n o\right) \\
P\left(X_{t}=\text { no } \mid X_{t+1}=\text { yes }\right) P\left(X_{t+1}=\text { yes }\right)+P\left(X_{t}=\text { no } \mid X_{t+1}=\text { no }\right) P\left(X_{t+1}=\text { no }\right) \\
\text { Similarly, } \\
P\left(X_{t+1}=\text { no } \mid X_{t}=\text { no }\right)=1-\lambda e^{-\lambda} \\
P\left(X_{t+1}=\text { no } \mid X_{t}=\text { yes }\right)=P\left(X_{t+1}=\text { yes }, X_{t}=\text { no }\right)=e^{-\lambda} \\
P\left(X_{t+1}=\text { yes } \mid X_{t}=\text { yes }\right)=1-e^{-\lambda}
\end{gathered}
$$

For organizational and environmental factors, there are two levels: "Yes (Bad)" and "No (Good)". "Yes (Bad)" and "No (Good)" represent that organizational and environmental factors are in "Bad" and "Good" conditions respectively. The transition probabilities are shown in Table 5 where, $c$ stands for the recovery factor of the system.

Table 5 Transition probability of organizational factor


# 4.2 Reliability prediction of emergency evacuation 

In order to predict the reliability of emergency evacuation, the prior probabilities of the root nodes in the BN model should be determined firstly. According to the statistical data ${ }^{[52-33]}$ about Incidents Associated with Oil and Gas Operations of offshore platforms released on the official website of BSEE and references ${ }^{[45-46]}$, the prior probabilities of each of such nodes are generated by statistical calculations and shown in Table 6.

Table 6 the prior probabilities of all the root nodes (4 decimal places are produced by the computation)



![img-5.jpeg](img-5.jpeg)

Fig. 5 Reliability of emergency evacuation from offshore platform
From Fig. 5, the reliability of emergency evacuation shows a gradual upward trend with time because the human errors and organizational factors will be further improved through safety training and experiences in the next 10 years. The reliability of emergency evacuation is $0.956,0.96,0.963$, $0.965,0.966,0.967,0.968$ and 0.968 respectively from time t 1 to t 9 . The simulated dynamic probability of emergency evacuation is compared with the available references as shown in Table 7.

Table 7 The reliabilities of emergency evacuation in different references


![img-6.jpeg](img-6.jpeg)

Fig. 6 Diagnostic reasoning of BN model

From Table 7, it can be seen that the reliability of emergency evacuation in this research is consistent with the available references at large. The proposed dynamic BN can be used to predict the dynamic reliability of emergency evacuation from the offshore platforms when the conditions do not change drastically.

# 4.3 Analysis of the BN model 

The main causes contributing to the failure of evacuation can be determined through the diagnostic inference of BN. The posterior probabilities of the root nodes are calculated through the backward diagnosis of the BN model when the reliability of emergency evacuation is set to zero. The diagnostic reasoning results are shown in Fig. 6.

### 4.3.1. Criticality analysis

Relying on merely prior or posterior probabilities in the identification of the most critical events is very likely to lead to inaccurate results ${ }^{[50]}$. Therefore, in the present study, the ratio of variation $(\mathrm{RoV})$ is used to identify the most critical root events contributing to the occurrence of the top event. For a root event xi, the RoV can be calculated as ${ }^{[51]}$ :

$$
\operatorname{RoV}\left(X_{\mathrm{i}}\right)=\frac{\pi\left(X_{\mathrm{i}}\right)-\theta\left(X_{\mathrm{i}}\right)}{\theta\left(X_{\mathrm{i}}\right)}
$$

where $\pi\left(X_{i}\right)$ and $\theta\left(X_{i}\right)$ denote the posterior and prior probabilities of Xi.
From Fig. 6, it can be seen that the posterior probabilities of all the factors at $t_{0}$ and the main factors leading to the failure of emergency evacuation are achieved. The ratios of variation between the posterior probability and prior probability are listed for each factor in Table 8.



From Table 8, "Confusion in main control room", "Rescue equipment failure", "Heavy fog", "Lack of examination", "Communication equipment failure", "Rain" and "No evacuation to designated area" are the main contributors to the failure of emergency evacuation. Among human and organizational factors, the influence of "Confusion in main control room" is the largest, indicating that "Confusion in main control room" contributes more to the failure of emergency evacuation, compared to other factors. The posterior probabilities of equipment factors are relatively small due to the increasing reliability of equipment and technical factors.

# 4.3.2. Mutual information analysis 

One of the suitable quantities that measures how much one random variable influences another variable is mutual information. The mutual information can be considered as the reduction in uncertainty about one random variable given knowledge of another. The mutual information is a measure of the mutual dependence between two random variables. If the two random variables are dependent in any way, the information of one variable can give us knowledge about the other. The larger the mutual information is, the larger the reduction in uncertainty. It means that two random variables are independent when the mutual information is equal to zero ${ }^{[45]}$.

At time $t_{0}$ and $t_{9}$, human factors, environmental factors, organizational factors and equipment factors are analyzed in terms of the mutual information with their influencing nodes using Netica Software as shown in Fig. 7, Fig. 8, Fig. 9 and Fig. 10, respectively.
![img-7.jpeg](img-7.jpeg)

Fig. 7 Analyses of human factors
It can be seen from Fig. 7 that the mutual information of the human factors influencing the emergency evacuation is approximately the same at time $t 0$ and $t 9$, and the degree of influence is

at the same level. Among the human factors, mutual information of "Evacuation procedures were not followed" is the largest, indicating that it has the greatest influence on evacuation, followed by "Lack of safety awareness", "Communication", "Absent relevant knowledge", "Violation of rules and regulations" and "Inattention".

From the analysis results, some useful suggestions can be drawn that training, knowledge, compliance with the regulations, and adequate communication are important throughout all steps of EER. Improvement of safety awareness, communication and knowledge through safety training are the key measures of successful evacuation. Adequate communications provided with precise voice communication instructions regarding the accident event, its location and action to be undertaken will increase the probability of successful evacuation.
![img-8.jpeg](img-8.jpeg)

Fig. 8 Analysis of environmental factors
Fig. 8 shows that the mutual information of "Toxic gas" and "Strong wind" is larger than the other environmental factors. Therefore, "Toxic gas" and "Strong wind" influence evacuation more than the other environmental factors. The other main influencing factors are "Visibility", "Stampede", "There are obstacles in the helicopter area" and "Rain" in a descending order. Personal protective equipment, such as gas masks, should be equipped for each evacuee. Keeping the helicopter area clear of obstacles is also important to ensure the use of helicopter for evacuation.
![img-9.jpeg](img-9.jpeg)

Fig. 9 Analysis of organizational factors
Fig. 9 indicates that the mutual information of "Emergency procedure" is the greatest among organizational factors, which indicates that an efficient emergency procedure has the greatest impact on the evacuation process. The other main influencing factors include "Lack of training

![img-10.jpeg](img-10.jpeg)

Fig. 10 Analysis of equipment factors
From Fig. 10, it can be seen that the mutual information of "Lack of rescue equipment" is the largest among the equipment factors, followed by "Lack of protective equipment", and "Alarm failure". By comparing Fig. 7, Fig. 8 and Fig. 9 with Fig. 10, it can be observed that the mutual information of the equipment factors is smaller than the one of the other factors. The influencing factors listed in a descending order are organizational factors, human factors, environmental factors and equipment factors, respectively.

# 5 Conclusions 

Based on the K2 structure learning algorithm, the reliability prediction model of the evacuation process is constructed using BN. The conditional probabilities are obtained by combining a Bayesian estimation method and a junction tree reasoning engine. The dynamic reliability prediction model of evacuation on offshore platforms is proposed using a dynamic BN approach. The transition probability is determined through a Markov method. The reliabilities of the evacuation process are predicted.

From the analysis of the BN model, it can be seen that the significant classified influencing groups are organizational factors, human factors, environmental factors and equipment factors in a descending order. "Emergency procedure", "Lack of training exercise" "Insufficient maintenance", "Lack of examination", "Evacuation procedures were not followed", "Error indication", "Confusion in main control room", "Toxic gas" and "Strong wind" are the main contributors to the failure of emergency evacuation.

Lack of historical accidents data is a major issue to be addressed in research of offshore emergency evacuation. In future, more emergency evacuation optimization studies will be carried out on the different kinds of offshore platforms and statistical uncertainty.

## Acknowledgments

This work is supported by Shandong Provincial Natural Science Foundation (Project No. ZR2019MEE080), "Key R\&D Program in Shandong Province (Project No. 2018GSF120021) and "the Fundamental Research Funds for the Central Universities" (Project No. 17CX02062 and No.19CX02025A)". This research has received funding from the European Union's Horizon 2020 research and innovation program under the Marie Skłodowska-Curie grant agreement - 840425. This research is also partially supported by EU H2020 RISE 2016 RESET - 730888.

# Appendix 1. 

The Pseudo-code of the K2 algorithm:
For $\mathrm{i}=1$ to n do
$\pi \mathrm{i}=$ Null set;
ScoreOld $=\mathrm{f}(\mathrm{i}, \pi \mathrm{i})$;
$\mathrm{P}=1$;
While(P=1 \& $\|\pi \mathrm{i}\|$ );
$\mathrm{Z}=$ search(pred( $\mathrm{i}), \pi \mathrm{i})$;
ScoreNew=Score( $\mathrm{i}, \pi \mathrm{i} \cup\{\mathrm{R}\})$;
If(ScoreNew> ScoreOld)
ScoreOld=ScoreNew;
$\pi \mathrm{i}=\pi \mathrm{i} \cup\{\mathrm{R}\} ;$
else $\mathrm{P}=0$;
end if
end while
$\operatorname{dag}(\pi \mathrm{i}, \mathrm{i})=1$;
end for
print(dag);
end

## Appendix 2.

The Bayesian estimation method is used to determine the conditional probability table in the proposed model as shown below.

```
priors=1;
seed=0;
rand('state',seed);
for i=1:n
bnet.CPD{i}=tabular_CPD(bnet,i,'CPT','unif','prior_type','dirichlet','dirichlet_type','BDeu','dir
ichlet_weight',priors);
    end
bnet2=bayes_update_params(bnet,data');
CPT3=cell(1,n);
for i=1:n
    s=struct(bnet2.CPD{i});
    CPT3{i}=s.CPT;
end
engine = jtree_inf_engine(bnet2);
evidence = cell(1,n);
evidence{A27} = 1;
evidence{A8} = 1;
evidence{C5} = 1;
evidence{A25} = 1;
evidence{A21} = 1;
evidence{A1} = 1;
evidence{A2} = 1;
evidence{A10} = 1;
evidence{A12} = 1;
evidence{A22} = 1;
[engine, ll] = enter_evidence(engine, evidence);
marg = marginal_nodes(engine,[A27 A8 C5 A25 A21 A1 A2 A10 A12 A22,A28]);
```

Table 1 Conditional probability table of the "Human behavior" node


Table 2 Conditional probability table of the "Emergency evacuation" node


# 0.4211 

0.5789