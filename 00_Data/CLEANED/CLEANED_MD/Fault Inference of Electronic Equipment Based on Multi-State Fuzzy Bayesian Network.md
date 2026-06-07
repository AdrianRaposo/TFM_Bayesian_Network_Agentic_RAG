# Article 

## Fault Inference of Electronic Equipment Based on Multi-State Fuzzy Bayesian Network

Ling Wang ${ }^{1}$ (D) Dongfang Zhou ${ }^{2}$, Hao Zhang ${ }^{1}$, Hui Tian ${ }^{1}$, Caihong Zou ${ }^{1}$ and Xiushan Wang ${ }^{1, *}$<br>1 College of Mechanical and Electrical Engineering, Henan Agricultural University, Zhengzhou 450002, China; wangling0351@126.com (L.W.); hao.zhang@henau.edu.cn (H.Z.); th407@163.com (H.T.); zch651221@126.com (C.Z.)<br>2 Department of Communication, National Digital Switching System Engineering and Technology R\&D Center (NDSC), Zhengzhou 450002, China; 13598028188@139.com<br>* Correspondence: xswang@henau.edu.cn; Tel.: +86-371-6355-8040

Received: 1 August 2019; Accepted: 29 September 2019; Published: 11 October 2019


#### Abstract

The aim of this study is to extend the directive function of fault inference in test and diagnosis system for electronic equipment. There are many problems, such as presence of various types of uncertain information in test set of electronic equipment, frequent degenerative faults, complex relationships of modules, multiple fault modes, existence of fuzzy interval in fault state, and interaction of each module. In view of these problems, the total membership degree of faults is commonly synthesized based on weights of multiple test indicators and normal membership degree of a single indicator. On this basis, this study builds the model for inferring fault states of leaf and root nodes based on multi-state triangular fuzzy Bayesian network (BN). Finally, this research carried out feasibility analysis on fault inference of a super-heterodyne receiver, thus verifying the efficiency and applicability of the method proposed in the study.


Keywords: multi-state Bayesian network; electronic equipment; fault inference; membership degree of fault

## 1. Introduction

Electronic equipment has been widely used in industrial, military, and civil systems. Faults in electronic equipment degrade the performance of systems greatly. In order to guarantee normal operation and repair faults quickly, fault diagnosis and fault prognosis of electronic equipment have become a major topic of research [1,2]. Fault inference refers to knowledge-based approaches of fault diagnosis [3,4], which based on the fault state, correlation relationship, and fault propagation mode of modules of electronic equipment-the model is established to express the variable state, and then the correlation relationship is described. Multi-source information were fused, forward reliability and inverse module fault probability inference are carried out. Fault inference is employed to estimate the health of the whole system and circuit module by collecting and processing the necessary data information of electronic equipment, and instructing the tester to carry out condition based maintenance.

In engineering applications, the automatic test and diagnosis system (ATDS) of the electronic equipment has been developing rapidly. High system integration and having overlapping modules, presents great difficulties for ATDS [5]. In the existing test program set, bootstrap program for fault test developed based on logic relationship of electric modules and on account of graph theory by integrating diagnose technology of fault tree, which is a graphical method for developing hierarchical relationships of parent-child nodes of electronic modules. This provides guidance of expert-type tests for non-expert engineering technicians, so as to rapidly locate faults and improve efficiency of diagnosis.

Because of adverse operating environment of electronic equipment, presence of various types of uncertain information in the test and multiple fault modes, the traditional qualitative and quantitative fault inference methods are not suitable for fault inference of complex electronic equipment.

The inference algorithm of the Bayesian network (BN) based on graph theory and probability theory can be used for bidirectional inference [6], namely, it can reason reliability of the system from root nodes to leaf nodes and weak linkage of the system from leaf nodes to root nodes. Therefore, it is widely used in fields such as cancer prediction [7], travel planning [8], classification of traditional Chinese medicine [9], and fault diagnosis [10-14]. In practical engineering applications, a system not only shows two states, i.e., normal or fault state, but also generally includes multiple fuzzy states. For this reason, BN is promoted and applied in reliability analysis on multi-state systems [15,16].

In the circuit system, there may be a large parameter, a smaller parameter soft fault or a short-circuit, open-circuit hard fault, which is to say, the fault state is a multi-state system. The study of multi-state Bayesian inference is a necessary path for the practical application of circuit fault diagnosis. BN has been used in transient and intermittent fault diagnosis of electronic equipment [17,18], the application of multi-state BN inference in fault diagnosis of electronic equipment is not found in the relevant literature, especially the research of the multi-state BN with fuzziness in the test diagnostic process of electronic equipment. Because there are multiple test indicators with different membership degrees of states for electronic modules and test samples are limited, statistical data are fuzzy.

This paper is motivated by the problem of electronic equipment multi-state fault inference. Existing approaches do not involve the fuzziness in multi-test indicators of test points, prior probability, and conditional probability of electronic equipment. This paper suggests a multi-state fault inference model (FRM) of electronic modules based on fuzzy BN, so as to extend the bootstrap program for testing fault probability in the existing test program set. Firstly, each of test indicators is divided five fault states base on the normal membership function, the expert gives the weight of test indicator, and then we can calculate the membership degree of test point. Secondly, the prior probability and conditional probability are performed by using triangular membership function. Finally, through fuzzy multi-state BN inference, we can speculate on the fault state of leaf nodes and calculate posterior fault probability of root nodes. Moreover, the model was verified to be effective through examples.

The structure of the research is arranged as follows: Section 2 establishes FRM and elaborated definitions of each variable and process in detail. Section 3 conducts inference based on multi-state fuzzy BN. The verification is carried out through examples in Section 4, and the conclusions are made in Section 5.

# 2. Module-Level FRM 

### 2.1. Definition of Variable Set of FRM

Based on fault inference process of electronic equipment and characteristics of the model based on BN, the FRM based on fuzzy BN was proposed to express fault states and correlations of modules in electronic equipment and transmission modes of faults. FRM includes relevant parameter and test information, such as topological structure of network, and probability distribution in graph theory. The model of electronic equipment is expressed through a five-element group $<S, F, A, P, T>$ of a variable set, where $S=\left\{S_{1}, S_{2}, \ldots, S_{n}\right\}$ indicates the node set in fuzzy BN, which represents fault set of each function or circuit module in electronic equipment. Each node shows $S=\left\{F_{1}, F_{2}, \ldots, F_{m}\right\} m$ fault states. If there are two fault states, namely $F=\{$ normal, fault $\}$, for the convenience of modeling, it is designated that $F=\{0,1\}$, that is, normal state and fault state are represented by 0 and 1 . This research discusses multi-state systems, that is $F=\{0,1,2, \ldots, i, \ldots\}$. In other words, normal state represents zero state and faults 1 and 2 separately indicate states 1 and 2 .
$A=\left\{\left|a_{i j}\right|, i=1,2, \ldots, n ; j=1,2, \ldots, n\right\}$ represents the set of directed edges between nodes, showing the correlations between faults of modules. If there is no directed edge between two modules,

it means that they are independent in fault inference. Moreover, $a_{i j}$ denotes a directed edge from node $a_{i}$ to node $a_{j}$, and demonstrates that the state of node $a_{i}$ influences fault state of node $a_{j}$.
$P=\left\{P\left(S_{i} \mid p a\left(S_{i}\right)\right), S_{i} \in S\right\}$ stands for the conditional probability table (CPT) of variables in BN; $p a\left(S_{i}\right)$ is the father node of $S_{i}$; that is, $P=\left\{P\left(S_{i} \mid p a\left(S_{i}\right)\right), S_{i} \in S\right\}$ refers to the conditional probability for the occurrence of event $S_{i}$ in premise of knowing fault of the father node. For electronic equipment, owing to interference of operating environment of electronic system to test data and limited recognition on expert knowledge of complex system, the CPT shows fuzziness. In other words, the probability $\hat{p_{i j}}$ of node $S_{i}(1 \leq i \leq n)$ in fault $F_{j}(1 \leq j \leq m)$ is a fuzzy number.
$T=\left\{t_{1}, t_{2}, \ldots, t_{k}\right\}$ represents the set of test indicators of node $S$. For electronic equipment, due to limited test points and different types of output signals of each module, different test and measurement instruments are needed which also have distinct test indicators. For example, direct-current voltage and current can be measured by using a universal meter, while signal frequency is obtained through a spectrum analyzer. Sometimes, different indicators with non-unified units and large ranges need to be tested at a point simultaneously, so they are required further processing.

# 2.2. Variable $F$ is Associated with Fault States of FRM 

Because of different function and effects of each module of electronic equipment in the system, the definitions of variable $F$ associated with fault state are different. The fault states of a two-state (normal and fault states) system are easily distinguished, while intermediate state of a multi-state system needs to be reasoned by experts based on fuzzy theory and fault causes for its fuzziness. Therefore, it needs to consider fault causes and fault test indicators.

### 2.2.1. Fault Causes

Faults are mainly from degenerative fault and sudden fault, which are also known as 'soft fault' and 'hard fault'. Of them, parametric fault is inevitable for electronic equipment because the performance parameters of electronic elements gradually decrease with the passage of time and worsening of the operating environment. While it does not change the topological structure of circuits and slightly reduces performance of electronic equipment, so fault states are defined according to influences on subsequent nodes. Hard fault is the extreme form of soft fault, that is, there are two probabilities, i.e., short circuit and open circuit. Owing to their changing the topological structure of circuits, they are uniformly defined as fault state.

### 2.2.2. Indicator $T$ for Fault Detection

Indicators for fault detection, as the objective detection results of automatically testing and diagnosing equipment when fault appears, can be used for probabilistic inference of fault causes and modes. For a two-state system, the indicators for fault detection tend to be fixed values, while in a multi-state system, indicators for fault detection theoretically are values continuously changing in a certain interval, that is, test indicators change with operating environment and age of electronic equipment.

In order to comprehensively show fault states of electronic equipment, multiple examples of test equipment are generally used for testing multiple indicators. In addition, due to application of complex and multiple test parameters with different units, expected outputs of each parameter are different when a circuit is in different states. For the convenience of modeling, all indicators are unified into a framework. After calculating membership degrees of faults of each parameter, experts calculate the synthesized membership degree of all test parameters according to importance weights of parameters.

### 2.3. Directed Edge A of FRM

The directed edges of fuzzy BN can be established by analyzing fault causes and modes. At present, BN for fault inference is generally established by combining structured analysis and design technology (SADT) and failure mode, effects, and criticality analysis (FMECA). By utilizing SADT method, function modules of the system and SADT model can be obtained. The FMECA method is used to analyze

fault modes of function modules or parts of the system obtained by employing SADT method, which provides bases for states of variables in BN model. The specific establishment method can refer to [19,20,21].

# 2.4. Fuzzy Membership Degree of Nodes in Fault State with Multiple Test Indicators 

The evaluation on fault state $F, F=\left\{f_{1}, f_{2}, \ldots, f_{m}\right\}$ of electronic equipment generally involves the set $T=\left\{t_{1}, t_{2}, \ldots, t_{k}\right\}$ ( $k$ represents the total number of evaluation sets) including multiple test indicators. Under different fault states $F$, the response is a different test index set $T$, and the response function $L_{f}$ is a matrix of $k \times m$ order. Fuzziness is shown from test indicator set $T$ to fault state set $F$, that is, there is a fuzzy relationship $R_{f}$. The element $r_{i j}$ of $R_{f}$ is the membership degree, which indicates the membership degree of an indicator to a certain fault; $r(x)$ demonstrates the membership function for evaluating membership degree of the test indicator set to the set of fault states.

$$
\begin{aligned}
& F \stackrel{L_{f}}{\Rightarrow} T, L_{f}=\left[\alpha_{i j}\right]_{k \times m} \\
& T \stackrel{R_{f}}{\Rightarrow} F, R_{f}=\left[r_{i j}\right]_{m \times k}
\end{aligned}
$$

Due to random and normal distribution of parameters of electronic elements, the density function complying with fuzzy normal distribution-namely, Gaussian function-is selected to calculate membership degrees of each parameter.

$$
r_{i j}(x)=e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
$$

where, $r_{i j}(x)$ is the membership degree of parameter $x$ and $\mu$ represents the expected value of distribution, that is, the value in this evaluating interval when membership degree is $1 ; \sigma$ indicates the width of the Gaussian function.

The membership function of a certain eigenvalue is shown in the Figure 1. According to the simulation results and test experience, experts can provide the center eigenvalue is $t_{0}$ in normal operating state and the minimum and maximum allowable indicators are $t_{L}$ and $t_{U}$. Therefore, the minimum and maximum indicators for judging a system in fault state are $t_{L F}$ and $t_{U F}$. The parameter relationship is demonstrated as above, namely $t_{L F}<t_{L}<t_{0}<t_{U}<t_{U F}$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Membership degrees corresponding to eigenvalues.
$r_{4 j}(t), r_{2 j}(t), r_{3 j}(t), r_{4 j}(t)$, and $r_{8 j}(t)$ are membership degrees of test indicators subjected to open-circuit fault, fault induced by smaller parameters, normal state, fault induced by large parameter, and short-circuit fault.

$$
\begin{aligned}
& r_{1 j}(t)=\left\{\begin{array}{ll}
1 & t \leq t_{L F} \\
e^{-\frac{\left(t-t_{L F}\right)^{2}}{2 \sigma_{1}{ }^{2}}} & t_{L F}<t \leq t_{L}, \sigma_{1}=\frac{t_{L}-t_{L F}}{3}
\end{array}\right. \\
& r_{2 j}(t)=\left\{\begin{array}{ll}
e^{-\frac{\left(t-t_{L}\right)^{2}}{2 \sigma_{21}{ }^{2}}} & t_{L F}<t \leq t_{L}, \sigma_{21}=\frac{t_{L}-t_{L F}}{3} \\
e^{-\frac{\left(t-t_{L}\right)^{2}}{2 \sigma_{22}{ }^{2}}} & t_{L}<t \leq t_{0}, \sigma_{22}=\frac{t_{0}-t_{L}}{3}
\end{array}\right. \\
& r_{3 j}(t)=\left\{\begin{array}{ll}
e^{-\frac{\left(t-t_{3}\right)^{2}}{2 \sigma_{31}{ }^{2}}} & t_{L}<t \leq t_{0}, \sigma_{31}=\frac{t_{0}-t_{L}}{3} \\
e^{-\frac{\left(t-t_{3}\right)^{2}}{2 \sigma_{32}{ }^{2}}} & t_{0}<t \leq t_{U}, \sigma_{32}=\frac{t_{U}-t_{0}}{3}
\end{array}\right. \\
& r_{4 j}(t)=\left\{\begin{array}{ll}
e^{-\frac{\left(t-t_{4}\right)^{2}}{2 \sigma_{41}{ }^{2}}} & t_{0}<t \leq t_{U}, \sigma_{41}=\frac{t_{U}-t_{0}}{3} \\
e^{-\frac{\left(t-t_{4}\right)^{2}}{2 \sigma_{42}{ }^{2}}} & t_{U}<t \leq t_{U F}, \sigma_{42}=\frac{t_{U F}-t_{U}}{3}
\end{array}\right. \\
& r_{5 j}(t)=\left\{\begin{array}{ll}
e^{-\frac{\left(t-t_{U F}\right)^{2}}{2 \sigma_{5}{ }^{2}}} & t_{U}<t \leq t_{U F}, \sigma_{5}=\frac{t_{U F}-t_{U}}{3} \\
1 & t>t_{U F}
\end{array}\right.
\end{aligned}
$$

$r_{1 j}(t), r_{2 j}(t), r_{3 j}(t), r_{4 j}(t)$, and $r_{5 j}(t)$ indicate the membership degrees of test indicators in the inference of the five fault states.

The weight of each test indicators, namely weigh of membership degree, which is given by expert experience, affects the total membership degree. Based on the signal transmission relationship and fault propagation relationship of electronic equipment, each of experts gave the weights $\left\{A_{1}{ }^{(e)}, A_{2}{ }^{(e)}, \cdots, A_{k}{ }^{(e)}\right\}, A_{1}{ }^{(e)}+A_{2}{ }^{(e)}+\cdots+A_{k}{ }^{(e)}=1, e=1,2, \ldots, e_{n}$ ( $e_{n}$ is the total of experts) of each indicator, and then the average weigh $\left\{A_{1}, A_{2}, \cdots, A_{k}\right\}$ is obtained.

The total membership degree of synthesized states and levels is $r_{i}(t)=A_{1} r_{j 1}(t)+A_{2} r_{j 2}(t)+\cdots+$ $A_{k} r_{i k}(t)$. The specific flow chart for calculating the total membership degree synthesized by multiple test indicators is displayed in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Flow chart of fault inference of multiple test indicators.

# 3. Multi-State Fuzzy BN 

The traditional Bayesian formula is shown as

$$
P\left(B_{i} \mid A\right)=\frac{P\left(B_{i}\right) P\left(A \mid B_{i}\right)}{\sum_{j=1}^{n} P\left(B_{j}\right) P\left(A \mid B_{j}\right)}
$$

where, $B_{i}$ is the cause for event $A$ and $P\left(A \mid B_{i}\right)$ is also known as the condition probability of $A$ when event $B_{i}$ occurs. $P\left(B_{i}\right)(i=1,2, \ldots)$ indicates the probability of cause $B_{i}$, which is called prior probability, while $P\left(B_{i} \mid A\right)(i=1,2, \ldots)$ shows the new understanding on cause $B_{i}$ after event $A$ occurs, which is known as posteriori probability.

As a graphic network for probability inference based on Bayesian formula, BN is proposed to solve uncertainty of complex problems and incomplete problems [22,23]. It has great advantages in solving faults caused by uncertainty and correlation of complex electronic equipment system [24]. Inference based on BN is to speculate the occurrence probability of some events at network nodes according to the structure of BN and CPT [25-27]. BN is used for bidirectional fault inference. In other words, it can evaluate reliability of a system from top to bottom and find the fault probability at source of the system through posteriori probability from bottom to top, so as to guide test personnel to find and rapidly locate faults based on modules or elements with large fault probability. In inference process, accurate inference algorithms-such as bucket-elimination algorithm, junction tree algorithm, and approximate calculation and inference algorithms, like search method and Gibbs sampling algorithm-are generally used. The former suits for inference based on BN with simple structure and small scale, while the latter is suitable for inference based on BN with complex structure and large amount of calculation [28,29].

The bucket-elimination algorithm solves the problem of joint probability distribution based on the idea of combinatorial optimization. The solving idea is to decompose joint probability into the product of CPTs through chain product for calculating joint probability and conditional independent characteristics [30,31]. Binary nodes determined by fault probability include joint probability distribution $P\left(S_{1}, S_{2}, \ldots, S_{n}\right)$ of $n$ nodes $\left(S_{1}, S_{2}, \ldots, S_{n}\right)$.

$$
P\left(S_{1}, S_{2}, \ldots, S_{n}\right)=\prod_{i=1}^{n} P\left(S_{i} \mid S_{1}, S_{2}, \ldots, S_{i-1}\right)
$$

After considering the conditional independence, that is, only taking into account of father node $p a\left(S_{i}\right)$ of node $S_{i}$, the joint probability distribution can be simplified as

$$
P\left(S_{1}, S_{2}, \ldots, S_{n}\right)=\prod_{i=1}^{n} P\left(S_{i} \mid p a\left(S_{i}\right)\right)
$$

By performing factorization $P\left(S_{i} \mid p a\left(S_{i}\right)\right)$ on joint probability distribution, the node $S_{j}$ without father node can be directly expressed as $P\left(S_{j}\right)$. According to elimination order, the nodes in the network are successively placed into a bucket and then the newly generated function factors are put into the next bucket to combine with the original variables. Such a process continues until the last bucket. Based on this, the obtained function factor is the calculated joint probability distribution.

# 3.1. Fuzziness of Prior Probability of Faults of Nodes 

Prior probability of nodes in fault inference is generally obtained based on statistical data of historical maintenance. However, due to small statistical magnitude or extreme operating environment of electronic equipment, certain fuzziness is inevitable in values of prior probability. According to a small amount of statistical information, the central value $p_{0}$ of fault probability is given and the interval $\left[p_{1}, p_{2}\right]$ of fault probability is presented based on experts' experience. After that, the simple triangular membership function is used to represent fuzzy number of probability, referring to [32,33], Membership function of triangular fuzzy number shown as Figure 3, that is, the fuzzy set of faults of node $F_{i}$ in the fault state $F_{i}{ }^{a_{i}}$ is expressed as $\widetilde{P}\left(S_{i}{ }^{j}\right)$, namely $\widetilde{P}\left(S_{i}{ }^{j}\right)=\left\{p_{1}, p_{0}, p_{2}\right\}$.

![img-2.jpeg](img-2.jpeg)

Figure 3. Membership function of triangular fuzzy number.
The fuzzy membership degree can be expressed as

$$
\mu(p)= \begin{cases}0 & 0<p<p_{1} \\ \frac{p-p_{1}}{p_{0}-p_{1}} & p_{1} \leq p \leq p_{0} \\ \frac{p_{2}-p}{p_{2}-p_{0}} & p_{0}<p \leq p_{2} \\ 0 & p_{2}<p\end{cases}
$$

where, $p_{0}$ indicates the central value of fault probability; $p_{1}$ and $p_{2}$ separately represent the upper and lower limits of fault probability.

# 3.2. CPT of Fuzzy BN 

Assuming that there are $\left\{S_{1}, S_{2}, \ldots, S_{n}\right\} n$ root nodes each of which has $m$ fault states, then root nodes totally show $m^{n}$ fault combinations, while leaf nodes demonstrate $\left\{F_{1}, F_{2}, \ldots, F_{k}\right\} k$ fault states. The conditional probability table (CPT) of multi-state fuzzy BN is shown as Table 1 and $P_{i}{ }^{1}+P_{i}{ }^{2}+\ldots+P_{i}{ }^{k}=1, i=1,2, \ldots, m^{n}$.

Table 1. CPT of multi-state fuzzy BN.


CPT can be given based on the previous experience summarized by experts and can be obtained on account of statistics of a lot of sample data through the formula of conditional probability. Some fault transmissions show fuzziness. By combining with statistical samples, the fuzzy interval of conditional probability can be presented by experts and expressed by using triangular fuzzy numbers.

### 3.3. Inference Based on Fuzzy BN

## (1) Inference of Fuzzy Fault State of Leaf Nodes

If interval probability of root nodes is fuzzy, the probability of node $S_{i}$ in fault state $F_{k}$ is recorded as $\widetilde{P}\left(S_{i, F_{k}}\right)$, while interval fuzziness of leaf node $L$ in fault state $F_{k}$ is

$$
\begin{aligned}
\widetilde{P}\left(L=F_{k}\right)= & \sum_{x_{1}, \ldots, x_{n}} \widetilde{P}\left(S_{1}, \ldots, S_{n}, Y_{1}, \ldots, Y_{m}, F_{k}\right) \\
& y_{1}, \ldots, y_{m} \\
= & \sum_{p a(L)} \widetilde{P}\left(L=F_{k} \mid p a(L)\right) \prod_{j=1}^{m} \sum_{p a\left(Y_{j}\right)} \widetilde{P}\left(Y_{j} \mid p a\left(Y_{j}\right)\right) \prod_{i=1}^{n} \widetilde{P}\left(S_{i, F_{k}}\right)
\end{aligned}
$$

where, $p a(L)$ represents the father node of leaf node $L$ and $p a\left(Y_{j}\right)$ indicates the father node of intermediate node $Y_{j}$.
(2) Fuzzy fault inference of faults of root nodes

The inference of fuzzy state of root nodes is to calculate posteriori probability of BN according to the state of leaf nodes. It is also known as backward inference based on BN, that is, the fuzzy interval of probability of leaf node is solved by calculating the obtained posteriori probability of BN.

If leaf node $L$ is in the fault state $F_{k}$, the posteriori probability of root node $S_{i}$ in the fault state $F_{k}$ is shown as

$$
\widetilde{P}\left(S_{i}=S_{i, F_{k}} \mid L=F_{k}\right)=\frac{\widetilde{P}\left(S_{i}=S_{i, F_{k}}, L=F_{k}\right)}{\widetilde{P}\left(L=F_{k}\right)}
$$

where, $\widetilde{P}\left(S_{i}=S_{i, F_{k}}, L=F_{k}\right)$ is the fuzzy joint probability of root node $S_{i}=S_{i, F_{k}}, L=F_{k}$. Because of

$$
\widetilde{P}\left(L=T_{k} \mid S_{i}=S_{i, F_{k}}\right)=\frac{\widetilde{P}\left(S_{i}=S_{i, F_{k}}, L=T_{k}\right)}{\widetilde{P}\left(S_{i}=S_{i, F_{k}}\right)}
$$

Therefore, by combining with Formulas (9) and (10), the following formula is obtained.

$$
\widetilde{P}\left(S_{i}=S_{i, F_{k}} \mid L=T_{k}\right)=\frac{\widetilde{P}\left(S_{i}=S_{i, F_{k}}\right)}{\widetilde{P}\left(L=T_{k}\right)} \widetilde{P}\left(L=T_{k} \mid S_{i}=S_{i, F_{k}}\right)
$$

# 4. Example Analysis 

A digital super heterodyne receiver is taken as an example and its functional block diagram is shown as Figure 4. Owing to the faults of power supply unit, microcomputer unit, and panel unit belong to hard faults, the multi-state fuzzy sub-frequency-doubled unit, short-wave mixing unit, frequency synthesizer unit, and medium- and low-frequency units are mainly considered. Of them, the frequency synthesizer unit provides three local oscillator signals, i.e., local oscillator signals 1, 2, and 3 required by receiver. Local oscillator signals 1 and 2 act on the first and second frequency mixing modules of short-wave mixing unit, while local oscillator signal 3 acts on the third frequency mixing module of medium- and low-frequency units. Therefore, local oscillator signals 1 and 2 commonly acting on short-wave mixing unit are regarded as a node $x_{2}$ of BN, while the local oscillator signal 3 is seen as a node $x_{3}$ of BN. Based on SDT and FMECA, BN of leaf nodes is established by selecting faults of medium- and low-frequency units, as shown in Figure 5.
![img-3.jpeg](img-3.jpeg)

Figure 4. Block diagram of principle of the super heterodyne receiver.

![img-4.jpeg](img-4.jpeg)

Figure 5. BN of faults of medium- and low-frequency units.
Where, $x_{1}, x_{2}, x_{3}, y_{1}$, and $T$ represent the sub-frequency doubled unit, the local oscillator signals 1 and 2 of frequency synthesizer, local oscillator signal 3 of frequency synthesizer, short-wave mixing unit and medium- and low-frequency units, respectively. In $\mathrm{BN}, x_{1}, x_{2}$, and $x_{3}$ are regarded as variables of root nodes; $T$ indicates the variable of leaf nodes and $y_{1}$ denotes the variable of intermediate node.

Each module shows three operating states-i.e., normal state, slight (sub-health) fault, and fault-and they are supposed to be relatively independent.

In order to simplify the process of fault inference, the faults induced by parameters smaller or larger than the normal ones are uniformly defined as sub-health faults, while the open-circuit and short-circuit faults are defined as faults. Moreover, $u_{0}(\mathrm{t}), u_{0.5}(\mathrm{t})$ and $u_{1}(\mathrm{t})$ are used as the membership degrees in normal state, sub-health state and fault state. The corresponding relationship of these membership degrees with Formula (3) is shown as

$$
\begin{gathered}
u_{0}(\mathrm{t})=r_{3}(\mathrm{t}) \\
u_{0.5}(\mathrm{t})=r_{2}(\mathrm{t}) \text { or } r_{4}(\mathrm{t}) \\
u_{1}(\mathrm{t})=r_{1}(\mathrm{t}) \text { or } r_{5}(\mathrm{t})
\end{gathered}
$$

In Table 2, $\widetilde{P}\left(y_{1}=0 \mid x_{1}=0, x_{2}=0.5\right)+\widetilde{P}\left(y_{1}=0.5 \mid x_{1}=0, x_{2}=0.5\right)=0.5, \widetilde{P}\left(y_{1}=\right.$ $\left.0 \mid x_{1}=0.5, x_{2}=0\right)+\widetilde{P}\left(y_{1}=0.5 \mid x_{1}=0.5, x_{2}=0\right)+\widetilde{P}\left(y_{1}=1 \mid x_{1}=0.5, x_{2}=0\right)=1$ and $\widetilde{P}\left(y_{1}=\right.$ $\left.0 \mid x_{1}=0.5, x_{2}=0.5\right)+\widetilde{P}\left(y_{1}=0.5 \mid x_{1}=0.5, x_{2}=0.5\right)=0.3$.

Table 2. CPT of intermediate node $y_{1}$.


In Table 3, $\widetilde{P}(T=0 \mid y_{1}=0, x_{3}=0.5)+\widetilde{P}(T=0.5 \mid y_{1}=0, x_{3}=0.5)=0.8, \widetilde{P}(T=$ $\left.0 \mid y_{1}=0.5, x_{3}=0\right)+\widetilde{P}(T=0.5 \mid y_{1}=0.5, x_{3}=0)+\widetilde{P}(T=1 \mid y_{1}=0.5, x_{3}=0)=1$ and $\widetilde{P}(T=$ $\left.0.5 \mid y_{1}=0.5, x_{3}=0.5\right)+\widetilde{P}\left(T=1 \mid y_{1}=0.5, x_{3}=0.5\right)=0.7$.

Table 3. CPT of leaf node $T$.


Based on historical data of faults and experts' experience, the priori probability of faults of root nodes can be evaluated and shown in the following Table 4.

Table 4. Fuzzy numbers of fault states of root node T.


Where, owing to the center value $p_{0}$ of fuzzy state is the historical statistical data of faults, the sum of fault probability $p_{0}$ of each node equals 1 . By taking node $x_{1}$ as an example, $p_{0}\left(x_{1}=0\right)+p_{0}\left(x_{1}=\right.$ $0.5)+p_{0}\left(x_{1}=1\right)=1$, where $p_{1}$ and $p_{2}$ are estimated by experts according to experience and reliability of circuits under the condition of limited sample data.

# 4.1. Calculation of Interval of Fault Probability of Leaf Nodes 

According to the fault state of root nodes, the fault state of leaf nodes is speculated. In accordance with bucket-elimination method and Formula (7), $\widetilde{P}(T=1)>\widetilde{P}(T=0)>\widetilde{P}(T=0.5)$. Moreover, it is known that the fault probability of leaf nodes is the largest and the probability in the normal state is slightly larger than that under soft fault.

$$
\begin{aligned}
\widetilde{P}(T=0) & =\widetilde{P}\left(x_{3}\right) \sum_{y_{1}, x_{3}} \widetilde{P}\left(T=0 \mid y_{1}, x_{3}\right) \sum_{x_{1}, x_{2}} \widetilde{P}\left(y_{1} \mid x_{1}, x_{2}\right) \widetilde{P}\left(x_{1}\right) \widetilde{P}\left(x_{2}\right) \\
& =\{0.00072,0.09612,0.13765\} \\
\widetilde{P}(T=0.5) & =\widetilde{P}\left(x_{3}\right) \sum_{y_{1}, x_{3}} \widetilde{P}\left(T=0.5 \mid y_{1}, x_{3}\right) \sum_{x_{1}, x_{2}} \widetilde{P}\left(y_{1} \mid x_{1}, x_{2}\right) \widetilde{P}\left(x_{1}\right) \widetilde{P}\left(x_{2}\right) \\
& =\{0.00039,0.07712,0.08677\} \\
\widetilde{P}(T=1) & =\widetilde{P}\left(x_{3}\right) \sum_{y_{1}, x_{3}} \widetilde{P}\left(T=1 \mid y_{1}, x_{3}\right) \sum_{x_{1}, x_{2}} \widetilde{P}\left(y_{1} \mid x_{1}, x_{2}\right) \widetilde{P}\left(x_{1}\right) \widetilde{P}\left(x_{2}\right) \\
& =\{0.20221,0.62680,1\}
\end{aligned}
$$

# 4.2. Calculation of Posteriori Probability of Root Nodes 

Based on Formula (10), the fuzzy posteriori probability can be calculated and only indicates the occurrence probability of a fault. For instance, when comparing $\widetilde{P}\left(x_{1}=1 \mid T=0.5\right), \widetilde{P}\left(x_{2}=1 \mid T=0.5\right)$, and $\widetilde{P}\left(x_{3}=1 \mid T=0.5\right)$, the common factor $\widetilde{P}(T=0.5)$ can be eliminated, so fault probability is more readable. To clearly indicate fault probability, the defuzzification is conducted on fuzzy probability by using the centroid method. The defuzzified fault probability is displayed in Table 5. The calculation of posteriori probability is mainly used in fault maintenance of root nodes when faults occur on leaf nodes, so there is no need to calculate probability of leaf nodes in normal state.

Table 5. Posteriori probability of leaf nodes when fault state is 0.5 and 1 .


As shown in the Table 5, $P\left(x_{1}=0.5 \mid T=0.5\right)>P\left(x_{2}=0.5 \mid T=0.5\right)>P\left(x_{3}=0.5 \mid T=0.5\right)$. If fault of leaf node occurs at 0.5 , the probability of root node $x_{1}$ with fault occurring at 0.5 being the maximum, followed by nodes $x_{2}$ and $x_{3}$. If fault 1 occurs in root nodes, fault 1 of each module is eliminated, so $P\left(x_{2}=0.5 \mid T=1\right)>P\left(x_{1}=0.5 \mid T=1\right)>P\left(x_{3}=0.5 \mid T=1\right)$. Fault at 0.5 should be looked up from root node $x_{2}$, and then $x_{1}$ and $x_{3}$. In the example, in order to simplify calculation process, the simple known condition is set for fault 1 in the CPT, so only $p\left(x_{i}=1 \mid T=0.5\right)=0$ and $p\left(x_{i}=1 \mid T=1\right)=1$ can be deduced. That is, two conclusions-i.e., minimum and maximum fault probability can only be made-while more delicate differences of them cannot be specifically distinguished. As CPT data become more complete, more detailed results can be obtained.

## 5. Conclusions

In the inference of fault diagnosis of electronic equipment, because there are many test parameters between modules and presence of overlapping fuzzy intervals in fault states, this study carries out fault inference based on multi-state fuzzy BN. Moreover, the FRM is built so as to guide test program set to rapidly locate faults. Because there is a combination explosion in the multi-state fuzzy system, this inference method is suitable for the circuit modules or circuit systems. The innovations of this research can mainly be stated as:
(1) In view of how to determine fault state through multiple test indicators of test modules, the normal membership function of a single parameter is proposed; Experts assign the weights of test indicators for normalization of membership degree. In order to assist test personnel in understanding and programming, five fault states are divided according to test indicators.
(2) In inference based on BN, due to limited samples of electronic modules, according to statistical values of the samples and experts' experience and tables of prior probability and conditional probability, fuzzy inference was performed by using triangular membership function.
(3) Based on multi-state fuzzy BN, the bidirectional inference of faults could be conducted to speculate fault state of leaf nodes for fault verification and calculate posterior probability of fault of root nodes, so as to find fault source and rapidly locate faults.

Author Contributions: Conceptualization, L.W. and D.Z.; experiment design, H.Z. and H.T.; experiment operation, C.Z. and X.W.; data analysis, L.W.; writing-original draft preparation, L.W.; writing-review and editing, X.W. and H.Z.

Funding: This research was supported by the China Postdoctoral Science Foundation (2017M612399), the Science and Technology Innovation Project of Henan Agricultural University (KJCX2018A09), the National Natural Science Foundation of China (31671581).

Conflicts of Interest: The authors declare no conflict of interest.
