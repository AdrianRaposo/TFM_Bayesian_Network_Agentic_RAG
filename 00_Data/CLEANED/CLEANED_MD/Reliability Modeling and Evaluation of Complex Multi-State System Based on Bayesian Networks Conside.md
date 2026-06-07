# Reliability Modeling and Evaluation of Complex Multi-State System Based on Bayesian Networks Considering Fuzzy Dynamic of Faults 

Fangjun Zuo*, Meiwei Jia, Guang Wen, Huijie Zhang and Pingping Liu<br>School of Intelligent Manufacturing, Chengdu Technological University, Chengdu, 611730, China<br>*Corresponding Author: Fangjun Zuo. Email: zuofangjun@126.com

Received: 04 April 2021 Accepted: 11 May 2021


#### Abstract

In the traditional reliability evaluation based on the Bayesian method, the failure probability of nodes is usually expressed by the average failure rate within a period of time. Aiming at the shortcomings of traditional Bayesian network reliability evaluation methods, this paper proposes a Bayesian network reliability evaluation method considering dynamics and fuzziness. The fuzzy theory and the dynamic of component failure probability are introduced to construct the dynamic fuzzy set function. Based on the solving characteristics of the dynamic fuzzy set and Bayesian network, the fuzzy dynamic probability and fuzzy dynamic importance degree of the fault state of leaf nodes are solved. Finally, through the dynamic fuzzy reliability analysis of CNC machine tool hydraulic system balance circuit, the application of this method in system reliability evaluation is verified, which provides support for fault diagnosis of CNC machine tools.


## KEYWORDS

Bayesian network (BN); dynamics; fuzzy; multi-state

## 1 Introduction

Owing to the development of mechanical products becoming increasingly complex, reliability evaluation and prediction of such systems have always focused on reliability engineering research $[1,2]$. The relationship between the faulty logic and the fault probability of each component of the system with time is more and more complex. In the reliability evaluation, whether the quantification method with uncertain parameters is close to the actual engineering conditions has an important impact on the accuracy of the evaluation [3,4]. Nowadays, the development theory of system reliability analysis in static environments has been dramatically developed. A relatively perfect theoretical system has been formed: binary decision diagram analysis method, binary decision algorithm, recursive analysis method, fault tree analysis method, and Bayesian analysis method $[4,5]$. This static system reliability of the method is based on two fundamental assumptions (probability hypothesis and binary hypothesis) and four premises (event definition exists, a large number of samples with probability repeatability and good distribution, not influenced by

human factors) [6,7]. However, due to the various performance indicators, working environments and small-batch customization of the complex system structure, the reliability state of a complex system is often associated with multiple performance indicators, and there is a specific correlation between multiple performance indicators [8]. Thus, the failure probability of a complex system has shown the characteristics of dynamic fuzziness [9-11]. The fuzziness of system and component behavior and the dynamic operating environment of the system brings additional difficulties to estimate the failure probability of important events accurately. In these cases, it is unrealistic and impossible to use determined values to represent component failure behavior.

In order to solve these problems, new theories are developed and applied to reliability analysis, including fuzzy theory [10-13], confidence interval estimation theory [14], imprecise probability theory [7], Dempster-Shafer evidence theory (DSET) [15], possibility theory [16], etc. The use of fuzzy mathematics to deal with the problem of reliability began in the mid-1970s. Kaufmann et al. [17] introduced the concept of possibility to represent the reliability of components in 1975. Yao et al. [18] proposed the concept of the structural fuzzy safety measure and proposed using fuzzy set theory to represent the reliability of structures, which made a significant development of fuzzy reliability theory. Ayyub et al. [19] reviewed the application of fuzzy mathematics to structural reliability. Spz et al. [10] used the function approximation method to estimate the random interval reliability of structures. In this work, fuzzy random variables are used for reliability analysis. Bayesian network is a standard method for system reliability analysis [16]. Compared with other reliability evaluation methods, Bayesian networks possess obvious advantages in modelling, analysis and calculation. In addition, the Bayesian network also has the advantage of reverse reasoning [5]. Considering the system's dynamic characteristics, many scholars have studied the relationship between dynamic fault trees and dynamic Bayesian networks [6]. By transforming a dynamic fault tree into a dynamic Bayesian network, the reliability modelling and evaluation of the dynamic system are realized [12]. Huang et al. [16] analyzed the reliability of fuzzy life data based on the Bayesian method. Wu [20] and Taheri et al. [21] modelled the system parameters with fuzzy random variables and established the fuzzy reliability evaluation method based on Bayesian inference with fuzzy prior distribution parameters. Zhang et al. [22] introduced variables into the construction of fuzzy support radius and proposed a Bayesian network based on fuzzy support radius for multi-state fault diagnosis. Simon et al. [23] used the Bayesian network to evaluate the reliability of complex systems with epistemic uncertainty. In a complex mechanical system, due to the influence of various factors such as its environment, its material performance, human operation and so on, its reliability index generally shows a decreasing trend with the increase of working time. The decreasing process is dynamic, so the influence of the time factor cannot be ignored in the reliability analysis of the system or components. Moreover, the failure data obtained is also discrete, so it is difficult to characterize the change rule of failure probability with a simple function [24-27]. Applying Bayesian networks to realize the reliability evaluation of such complex multi-state systems is a problem worthy of study.

In this paper, the dynamic fuzzy set theory has been proposed in the Bayesian network evaluation. The reliability of the complex multi-state system is studied by considering the fault dynamics and fuzzy. Section 1 retrospect the theoretical basis of this research. Section 2, introduces the node definition and network inference of multi-state network, section considering fault dynamics and fuzzy. Section 3, the presented method is applied to the hydraulic system balance circuit as an example, and a brief conclusion follows it in Section 4.

# 2 Modeling and Evaluation of Multi State Bayesian Networks 

### 2.1 Bayesian Network

Bayesian networks (BN) have the characteristics of bidirectional reasoning, that is, forward reasoning and reverse reasoning [28]. The inference used to judge the tendency and possibility of system failure in the system design stage is called positive reasoning, and positive reasoning is also called causal reasoning. The reasoning used to determine the main reasons for system failure after a system failure is called reverse reasoning. Reverse reasoning is also known as diagnostic reasoning, according to which reverse reasoning can find the system's weak links to provide a basis for safety management and system design improvement [29,30].

BN is a subjective view based on probability. Suppose $X$ and $Y$ are two random variables, the probability density function (PDF) is $P(Y)(P(Y)>0)$. According to the Bayesian equation, the conditional probability of $P(X \mid Y)$ can be defined:
$P(X \mid Y)=\frac{P(Y \mid X) P(X)}{P(Y)}$
where $P(X)$ is the probability prior distribution. If $P(X)$ has $n$ failure states, i.e., $x_{1}, x_{2}, \cdots x_{n}$, According to the total probability formula the full probability formula, $P(Y)$ can be given by:
$P(Y)=\sum P\left(Y \mid X=x_{i}\right) P\left(X=x_{i}\right)$
BN is a representation and reasoning model of uncertain knowledge based on probability analysis and graph theory [27]. When the probability distribution of node variables is known, the Bayesian network can realize qualitative and quantitative uncertainty representation [28]. The Directed acyclic graphs (DAG) and conditional probability tables (CPT) are two parts of the BN model. The DAG can explain the logic structure of BN, which is a part of qualitative analysis [29]. Nodes without parents are called root nodes, nodes without sub-nodes are called leaf nodes, and other nodes are called intermediate nodes. The CPT is used for conditional probabilities under different fault states. The CPT represents the strength of the relationship between nodes which is a part of the quantitative analysis of BN [30].

The BN is depicted in Fig. 1. Here, $X_{i},(i=1,2,3,4,5)$ is the root node, which has marginal prior probability. $A_{1}$ and $A_{2}$ are intermediate nodes. $M_{1}, M_{2}$ are leaf nodes. According to the conditional dependence between the events in the Bayesian network, the posterior probability can be easily derived from the prior probability to realize the system reliability evaluation [29]. Using the BN joint fault inference algorithm, the joint probability of all nodes in Fig. 1 could be expressed as Eq. (3):
$P\left(M_{1}, M_{1}, A_{1}, A_{2}, X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\right)$
$=P\left(X_{1}\right) \cdot P\left(X_{2}\right) \cdot P\left(X_{3}\right) P\left(X_{4}\right) P\left(X_{5}\right) \cdot P\left(A_{1} \mid X_{1}, X_{2}, X_{3}, X_{4}\right) \cdot$
$P\left(A_{2} \mid X_{3}, X_{4}, X_{5}\right) \cdot P\left(M_{1} \mid A_{1}, A_{2}\right) \cdot P\left(M_{2} \mid A_{2}\right)$

![img-0.jpeg](img-0.jpeg)

Figure 1: Bayesian network structure
When the node state in a Bayesian network goes out of the two-state assumption, i.e., the node has several states, the traditional Bayesian network will be extended to a multi-state Bayesian network. In practical engineering, systems and components often have various fault modes and present different fault states. Reliability modelling of multi-state systems is often based on fault tree analysis using the extended multi-state fault tree analysis method [16]. The CPT of the Bayesian network is reconstructed by using expert knowledge and practical experience so that the logic relationship, uncertainty and multi-state component fault, which traditional Bayesian networks cannot express, are reflected [21]. Therefore, when the Bayesian network is used to deal with the polymorphism of variables, different state values can be selected to represent different fault states of nodes, and only the CPT of corresponding nodes needs to be adjusted [22].

# 2.2 Definition Fuzzy Node of BN 

In order to characterize the influence of subjective uncertainty on system reliability due to the lack of system cognition and limited information, some scholars proposed to further extend the continuous node variables of Bayesian networks to fuzzy node variables [31]. When the fault probability of a Bayesian network node is difficult to express with exact value, the fault probability of the node is expressed with a fuzzy subset. The definition of a fuzzy BN node is divided into two steps. The first step is to describe the failure state of the fuzzy node, and the second step is to describe the failure rate of the fuzzy node [32].

### 2.2.1 Description of the Fault States of Fuzzy Node

In engineering, due to the limitation of objective conditions and the influence of various uncertainties, we often encounter the situation of insufficient data or incomplete information. Therefore, the failure probability of parts is difficult to obtain in the reliability analysis. The fuzzy set theory provides a suitable modelling tool for some cases where the parameters are fuzzy numbers. Zadeh put forward the definition of a fuzzy subset in 1965 [13]. Latife introduced the fuzzy set theory into Bayesian networks to evaluate the fuzzy reliability of production management systems [33]. A fuzzy set is not a single value but a set of possibilities [17]. In fuzzy BN, we usually use fuzzy language variables to describe different fault states of the root node [8]. In this paper, the language information is adopted to describe the fault state, which can be divided into no fault, half fault and complete fault.

The membership functions of fuzzy subsets are of many forms, such as trapezoidal membership function, rectangular membership function, normal distribution membership function and

lognormal membership function, etc. Because the triangle membership function is the most widely used and algebraic operation is simple, the triangular fuzzy number is considered in this paper.
$P^{L}, P^{U}$ represent the upper and lower bounds supported by $\widetilde{P}$ respectively, and $0<P^{L} \leq$ $P^{M} \leq P^{U}, P^{M}$ represents the median of $\widetilde{P}$, then $\widetilde{P}$ is a triangular fuzzy number, and its membership function is shown in Fig. 2 which expressed as [24]:
$\mu_{\widetilde{P}}(P)=\left\{\begin{array}{l}0 \quad 0<P<P^{L} \\ \frac{P-P^{L}}{P^{M}-P^{L}} \quad P^{L} \leq P \leq P^{M} \\ \frac{P^{U}-P}{P^{L}-P^{U}} \quad P^{M}<P<P^{U} \\ 0 \quad P^{U}<P\end{array}\right.$
![img-1.jpeg](img-1.jpeg)

Figure 2: The membership function of triangular fuzzy number $\widetilde{P}$

The fuzziness and multi-state of nodes are considered in the above analysis. Due to the influence of various factors such as its environment, its material performance, human operation and so on, its reliability index generally shows a decreasing trend with the increase of working time. The decreasing process is dynamic, so the influence of the time factor cannot be ignored in the reliability analysis of the system or components. When the system reliability analysis is carried out, if any system's characteristic is ignored, the analysis result will produce an enormous error [8].

# 2.2.2 Quantification of Uncertainty of Root Node 

In practice engineering, the failure probability of each component in the system varies with time, and the time variable is introduced, so the fuzzy dynamic function is used to describe the fuzzy state of each root node in this paper.

For a BN with finite nodes, the set of nodes is $X_{i}=\left\{X_{1}, X_{2}, \cdots X_{i}, \cdots, X_{n}\right\}(i=1,2, \cdots, n)$. Assuming the node $X_{i}$ have $k_{i}$ fuzzy fault state, its state space is $X_{i}=\left\{x_{i}^{1}, x_{i}^{2}, \cdots x_{i}^{j}, \cdots, x_{i}^{k_{i}}\right\}$

$\left(j=1,2, \cdots, k_{i}\right)$. Assuming the fault state of node $X_{i}$ at any time $t$ is $x_{i}^{k_{i}}$, the dynamic fuzzy set of failure possibility $\widetilde{P}_{i k_{i}}(t)$ is expressed as [26]:

$$
\left\{\begin{array}{l}
P_{i k_{i}}^{L}(t)=a_{i k_{i}}^{L} t+b_{i k_{i}}^{L} \\
P_{i k_{i}}^{M}(t)=a_{i k_{i}}^{M} t+b_{i k_{i}}^{M} \\
P_{i k_{i}}^{U}(t)=a_{i k_{i}}^{U} t+b_{i k_{i}}^{U}
\end{array}\right.
$$

where $a_{i k_{i}}^{L}, a_{i k_{i}}^{M}, a_{i k_{i}}^{U}, b_{i k_{i}}^{L}, b_{i k_{i}}^{M}, b_{i k_{i}}^{U}$ are constants, which based on data fitting to determine combined with expert experience and historical data. $\left[b_{i k_{i}}^{L}, b_{i k_{i}}^{U}\right]$ represents the fuzzy subset at time $t=0$, $P_{i k_{i}}^{M}(t)$ is the central variable of the dynamic fuzzy subset at time $t, P_{i k_{i}}^{M}(t)-P_{i k_{i}}^{L}(t)$ and $P_{i k_{i}}^{U}(t)-$ $P_{i k_{i}}^{M}(t)$ represent the left and right fuzzy regions respectively at time $t$, with the increase of the fuzzy region, the fuzziness becomes stronger and stronger. Its membership function is given by Zhang et al. [22]:

$$
\widetilde{\mu}_{\widetilde{P}_{i k_{i}}(P)}=\left\{\begin{array}{cc}
0 & 0<P<P_{i k_{i}}^{L}(t) \\
\frac{P-P_{i k_{i}}^{L}(t)}{P_{i k_{i}}^{M}(t)-P_{i k_{i}}^{L}(t)} & P_{i k_{i}}^{L}(t) \leq P \leq P_{i k_{i}}^{M}(t) \\
\frac{P_{i k_{i}}^{U}(t)-P}{P_{i k_{i}}^{U}(t)-P_{i k_{i}}^{M}(t)} & P_{i k_{i}}^{M}(t) \leq P \leq P_{i k_{i}}^{U}(t)
\end{array}\right.
$$

where $P$ represents the failure rate of nodes at any time $t$. As shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Figure 3: The membership function of $\widetilde{P}_{i k_{i}}(t)$

According to the characteristics of node failure probability changing with time and combining with the fuzzy subset of triangle membership function, a dynamic fuzzy set was established to describe the function relation of root node failure probability changing with time $t$, as shown in Fig. 4.

![img-3.jpeg](img-3.jpeg)

Figure 4: The failure probability of node with time $t$

# 2.3 Analysis of Node Failure Possibility 

In a multi-state BN system, which have $n$ root nodes $X_{i}=\left\{X_{1}, X_{2}, \cdots X_{i}, \cdots, X_{n}\right\}$ ( $i=$ $1,2, \cdots, n)$. The intermediate node is $Y_{j}=\left\{Y_{1}, Y_{2}, \cdots Y_{j}, \cdots, Y_{m}\right\}(j=1,2, \cdots, m)$. The leaf node is $T_{v}=\{v=1,2, \cdots l\}$. The fuzzy numbers $x_{i}^{k_{i}}, y_{j}^{k_{j}}$ and $T_{v}$ are used to describe the fault states of corresponding nodes at time $t$. When dynamic fuzzy set of the root node is $\widetilde{P}\left(x_{i}^{k_{i}}\right)$ at time $t$, the dynamic fuzzy possibility of the leaf node $T$ at state $T_{v}$ can be computed by:

$$
\begin{aligned}
& \widetilde{P}_{T=T_{V}}(t)=\sum X_{1}, \ldots X_{n}, Y_{1}, \ldots Y_{m} \widetilde{P}\left(X_{1}, \ldots X_{n}, Y_{1}, \ldots Y_{m}, T_{V}\right) \\
& =\sum_{\pi(T)} \widetilde{P}\left(T=T_{V} \mid \pi(T)\right) \prod_{j=1}^{m} \sum_{\pi\left(Y_{j}\right)} \widetilde{P}\left(Y_{j} \mid \pi\left(Y_{j}\right)\right) \prod_{i=1}^{n} \widetilde{P}\left(x_{i}^{k_{i}}\right) \\
& =\sum_{\pi(T)} \widetilde{P}\left(T=T_{V} \mid \pi(T)\right) \sum_{\pi\left(Y_{1}\right)} \widetilde{P}\left(Y_{1} \mid \pi\left(Y_{1}\right)\right) \times \cdots \\
& \times \sum_{\pi\left(Y_{m}\right)} \widetilde{P}\left(Y_{m} \mid \pi\left(Y_{m}\right)\right) \times \widetilde{P}\left(x_{1}^{k_{1}}\right) \times \cdots \widetilde{P}\left(x_{n}^{k_{n}}\right)
\end{aligned}
$$

in which $\pi(T)$ is the set of parents of leaf node $T . \pi\left(Y_{j}\right)$ is the set of parents of intermediate node $Y_{j}$. If the state of $X_{i}$ is $x_{i}^{k_{i}}$, the fuzzy conditional probability of leaf node $T$ at state $T_{v}$ is given by equation:
$\widetilde{P}_{\left(T=T_{v} \mid X_{i}=x_{i}^{k_{i}}\right)}(t)=\frac{\widetilde{P}\left(T=T_{v}, X_{i}=x_{i}^{k_{i}}\right)}{\widetilde{P}\left(X_{i}=x_{i}^{k_{i}}\right)}$
where $\widetilde{P}\left(T=T, X_{i}=x_{i}^{k_{i}}\right)$ is the fuzzy joint distribution when the state of $X_{i}$ is $x_{i}^{k_{i}}$ and $T$ is $T_{v}$. Bayesian network is used to calculate the posterior probability of the failure of the parent node when the failure of the child node is known. While $T=T_{v}$, the posterior probability of root $X_{i}=x_{i}^{k_{i}}$ could be concluded as follows:
$\widetilde{P}_{\left(X_{i}=x_{i}^{k_{i}} \mid T=T_{v}\right)}(t)=\frac{\widetilde{P}\left(T=T_{v}, X_{i}=x_{i}^{k_{i}}\right)}{\widetilde{P}\left(T=T_{v}\right)}$

# 2.4 Importance Analysis of Fuzzy Dynamic Root Node 

The fuzzy importance degree of BN describes the evaluation of the importance degree when the leaf node is in a certain fault state, and the root node is in different fuzzy states in the multistate system. The importance of the root node is an important part of quantitative analysis in system reliability analysis [24,27]. It represents the importance of components in the system and aims to quantify the contribution of the component failure to system failure [28]. The importance degree of the root node in the Bayesian network can be obtained by using the inference algorithms, such as graph reduction method, clique tree propagation and bucket elimination inference method [33-35]. In this paper, the clique tree reasoning method is used for calculation, and the clique tree is constructed according to the variable elimination method. According to the calculation process of variable elimination, the information is transferred to the root node for calculation [16].

If the failure state of $X_{i}$ is $x_{i}^{k_{i}}(i=1,2, \cdots, n)$ at time $t$, the probability of failure of the dynamic fuzzy subset is $\widetilde{P}_{x_{i}^{k_{i}}}(t)$, the membership function is $\widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}}}(t)$. When $T=T_{v}$, the fuzzy importance of failure state $x_{i}^{k_{i}}$ is given by equation:

$$
\begin{aligned}
I_{x_{i}^{k_{i}}}^{\mathrm{Pr}}(t) & =E\left[\widetilde{P}\left(T=T_{v} \mid X_{i}=x_{i}^{k_{i}}\right)-\widetilde{P}\left(T=T_{v} \mid X_{i}=0\right)\right] \\
& =E\left[\frac{\widetilde{P}\left(T=T_{v}, X_{i}=x_{i}^{k_{i}}\right)}{\widetilde{P}\left(X_{i}=x_{i}^{k_{i}}\right)}-\frac{\widetilde{P}\left(T=T_{v}, X_{i}=0\right)}{\widetilde{P}\left(X_{i}=0\right)}\right]
\end{aligned}
$$

in which $\widetilde{P}\left(T=T_{v}, X_{i}=x_{i}^{k_{i}}\right)$ is the fuzzy posterior probability of the leaf nodes $T$ on the state $T_{v}$, and the state of $X_{i}$ is $x_{i}^{k_{i}}$.

According to the definition of a triangular fuzzy number, each triangular fuzzy number has a non-fuzzy number corresponding to it. The process of finding a value that can best characterize this fuzzy number is called deblurring, which is also commonly called deblurring. At present, there are many methods to remove ambiguity, including the mean area method, gravity center method, integration value method, etc. In this paper, we use the center of gravity method to de-fuzzily, so the fuzzy importance $I_{x_{i}^{k_{i}}}^{\mathrm{Pr}}(t)$ can be gotten by Li et al. [28]:
$I_{x_{i}^{k_{i}}}^{\mathrm{Pr}}(t)=\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}}, T_{v}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}}, T_{v}}(t) d x}-\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, 0}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, 0}}(t) d x}$
when failure state of $T$ is $T_{v}$, The fuzzy importance of $X_{i}$ can be calculated by Eq. (12).
$I_{T_{v}}^{\mathrm{Pr}}(t)=\frac{\sum_{k_{i}=1}^{\lambda} I_{x_{i}^{k_{i}}}^{\mathrm{Pr}}(t)}{\lambda}=\frac{\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, T_{v}}(t) d x}}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, T_{v}}(t) d x}}-\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, 0}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{x_{i}^{k_{i}}, 0}}(t) d x}}{\lambda}$
where $\lambda$ is the amount of state $X_{i}$ excluding state 0 . When state of $T$ is $T_{V}$, the node fuzzy importance of BN $I_{T_{v}}^{\mathrm{Pr}}(t)$ reflects the average importance of the node $X_{i}$, the state varies from 0 to $1[30,32,33,35]$. Importance refers to the contribution of basic events to the occurrence of the

system, which reflects the important measure of basic events in the system and provides the basis for improving the reliability of the system.

# 3 Numerical Results and Comparative Analysis of Hydraulic System Balance Circuit 

Hydraulic systems are widely used in aerospace, metallurgy, machinery, engineering, machinery and other fields. This paper takes the balance circuit of a heavy CNC machine tool as the research object, and analyzes and studies the reliability of the hydraulic system [24].

### 3.1 Hydraulic System Balance Circuit

Through the reliability distribution and FMECA analysis of a heavy CNC machine, it can be seen that there are serious reliability problems in the hydraulic system of the beam moving gantry machining center. In the hydraulic system, the valve core of the one-way valve is stuck. Usually, it is not completely stuck, and there is still fluid flow. The piston of the hydraulic cylinder does not fail, and it is not that the piston cannot act completely, but that the action is often incomplete; For the system as a whole, the failure of insufficient pressure is fuzzy. Therefore, it is necessary to introduce the method of fuzzy theory when doing fault tree analysis for the system. Moreover, the faults cannot be described by two states: normal and fault, and use fuzzy probability to describe the probability of component fault (occurrence of the bottom event) and system fault (occurrence of the top event) [32-36].

The balance circuit is composed of filter (j1), motor (r), hydraulic pump (p), filter (j2), pressure indicator (n1), cut-off valve (k1), pressure reducing valve (f1), one-way valve (a1), pressure indicator (n2), pressure relay (b2), cut-off valve (k2) and (k3), relief valve (i1), accumulator group (m1) and balance cylinder (h1). Any component failure can result in a system failure.

After the system starts, the hydraulic pump (p) provides oil and pressure to the whole system. During the operation of the hydraulic pump, the system presses the accumulator group. When the pressure reaches the range set by the pressure relay (b2), the hydraulic pump stops supplying pressure. During the operation of the balancing cylinder, when the pressure decreases, the accumulator group (m1) will make up the pressure and maintain the pressure of the whole system. Here, the accumulator group is regarded as series of components for fault tree modelling analysis.

According to the FMEA analysis results of the whole machine tool and hydraulic system, "no pressure or low pressure lift in the balance circuit" has been chosen as the top event. On the basis of the modelling rules of the fault tree, the fault mode of the system is analyzed from top to bottom. Causes leading to no pressure or low pressure lift in the top event balance loop include insufficient oil supply pressure, oil filter (j2) blocking, oil branch 1 fault, hydraulic cylinder (h1) fault and energy storage system failing to store energy. Secondly, the failure mode of each hydraulic component and the failure state of the components in the hydraulic component is analyzed. The fault mode and codes of the entire balance loop are shown in Tab. 1. The fault tree is presented in Fig. 5.

Based on the characteristics of the BN, the FTA is transformed into the BN model. Fig. 6 depicts the BN model of hydraulic system balance circuit fault accident. Here $T^{\prime}$ is the leaf node, $X_{1} \sim X_{15}$ are the root nodes, $M_{1} \sim M_{4}$ are the intermediate nodes.

Table 1: The codes and names of basic events
Code Event name
$T \quad$ No pressure or pressure insufficient in the balance circuit
$M_{1} \quad$ The oil supply pressure is insufficient
$M_{2} \quad$ Oil branch failure
$M_{3} \quad$ Energy storage system failure
$M_{4} \quad$ Insufficient quantity of oil
$X_{1} \quad$ The oil filter (j2) is damaged or the outlet is blocked by dirt
$X_{2} \quad$ Hydraulic cylinder (h1) malfunction
$X_{3} \quad$ Hydraulic pump failure
$X_{4} \quad$ Fuel tank (q) is damaged and sealed loosely, resulting in leakage
$X_{5} \quad$ Motor (r) fault
$X_{6} \quad$ Pressure relay (b2) is out of order and the motor is not operating
$X_{7} \quad$ The oil temperature is too high, the viscosity decreases and the internal leakage increases
$X_{8} \quad$ The oil filter (j1) is damaged or the outlet is blocked by dirt
$X_{9} \quad$ Pressure reducing valve (f1) output pressure is insufficient
$X_{10} \quad$ The check valve (a1) malfunction, leak or plug make the oil pressure cannot rise
$X_{11} \quad$ Pressure relief valve (i1) is seriously relieved
$X_{12} \quad$ Leakage of pipes and joints
$X_{13} \quad$ Accumulator (m1) malfunction
$X_{14} \quad$ Stop valve (k2) malfunction
$X_{15} \quad$ Liquid level switch (b1) malfunction
![img-4.jpeg](img-4.jpeg)

Figure 5: The FTA of the balance circuit

![img-5.jpeg](img-5.jpeg)

Figure 6: The BN model of the balance circuit

Due to the different structure and function of each root node itself, different root nodes have different influences on the system even under the same failure state. Therefore, this paper considers nodes $X_{1} \sim X_{15}, M_{1} \sim M_{4}$ and $T$ have three failure states, respectively, normal operation, partial failure and failure. State $0,0.5$, and 1 represent normal operation, partial failure, and failure, respectively. Comprehensive historical data and expert experience, the CPT are listed in Tabs. 2$6[22-37]$.

Table 2: The CPT of node $M_{4}$


Table 3: The CPT of node $M_{1}$


Table 4: The CPT of node $M_{2}$


Table 5: The CPT of node $M_{3}$


Table 6: The CPT of node $T$


Table 6 (continued)


# 3.2 Dynamic Fuzzy Possibility Analysis of Leaf Nodes 

Due to components in the hydraulic loop system having different performance and different working environments, the failure probability of each component varies with time. The dynamic fuzzy subset of failure probability of root node is obtained when the failure state of root node is 1 and 0.5 by analyzing the historical data and expertise, as shown in Tabs. 7 and 8.

Table 7: Dynamic fuzzy possibility subset of $X_{i}$ at fault state 1


Table 8: Dynamic fuzzy possibility subset of $X_{i}$ at fault state 0.5


According to Tabs. 2-6 and Eq. (7), when $T=1$, the dynamic fuzzy possibility is calculated as shown below:

$$
\begin{aligned}
& \widetilde{P}_{T=1}(t)=\sum_{X_{1}, \ldots X_{14}} \widetilde{P}\left(X_{1}, X_{2}, X_{3} \ldots X_{14}, M_{1}, M_{2}, M_{3}, M_{4}, T=1\right) \\
& M_{1}, \ldots M_{4} \\
& =\sum_{X_{1}, X_{2}} \quad \widetilde{P}\left(T=1 \mid X_{1}, X_{2}, M_{1}, M_{2}, M_{3}\right) \times \widetilde{P}\left(X_{1}\right) \times \widetilde{P}\left(X_{2}\right) \times \\
& M_{1}, M_{2}, M_{3} \\
& \sum_{X_{3}, X_{4} \ldots X_{8}, M_{4}} \widetilde{P}\left(M_{1} \mid X_{3}, X_{4}, \cdots X_{8}, M_{4}\right) \times \widetilde{P}\left(X_{3}\right) \times \widetilde{P}\left(X_{4}\right) \times \cdots \widetilde{P}\left(X_{8}\right) \times \\
& \sum_{X_{6}, X_{15}} \widetilde{P}\left(M_{4} \mid X_{6}, X_{15}\right) \widetilde{P}\left(X_{6}\right) \times \widetilde{P}\left(X_{15}\right) \sum_{X_{9} \ldots X_{12}} \widetilde{P}\left(M_{2} \mid X_{9} \ldots X_{12}\right) \times \\
& \widetilde{P}\left(X_{9}\right) \times \cdots \widetilde{P}\left(X_{12}\right) \times \sum_{X_{13}, X_{14}} \widetilde{P}\left(M_{3} \mid X_{13}, X_{14}\right) \times \widetilde{P}\left(X_{13}\right) \times \widetilde{P}\left(X_{14}\right)
\end{aligned}
$$

when $T=0.5$, the dynamic fuzzy subset of failure probability of root node is listed in Tab. 8. The dynamic fuzzy possibility is given as follows:

$$
\begin{aligned}
& \widetilde{P}_{T=1}(t)=\sum_{X_{1}, \ldots X_{14}} \widetilde{P}\left(X_{1}, X_{2}, X_{3} \ldots X_{14}, M_{1}, M_{2}, M_{3}, M_{4}, T=0.5\right) \\
& M_{1}, \ldots M_{4} \\
& =\sum_{X_{1}, X_{2}} \quad \widetilde{P}\left(T=0.5 \mid X_{1}, X_{2}, M_{1}, M_{2}, M_{3}\right) \times \widetilde{P}\left(X_{1}\right) \times \widetilde{P}\left(X_{2}\right) \times \\
& M_{1}, M_{2}, M_{3} \\
& \sum_{X_{3}, X_{4} \ldots X_{8}, M_{4}} \widetilde{P}\left(M_{1} \mid X_{3}, X_{4}, \cdots X_{8}, M_{4}\right) \times \widetilde{P}\left(X_{3}\right) \times \widetilde{P}\left(X_{4}\right) \times \cdots \widetilde{P}\left(X_{8}\right) \times \\
& \sum_{X_{6}, X_{15}} \widetilde{P}\left(M_{4} \mid X_{6}, X_{15}\right) \widetilde{P}\left(X_{6}\right) \times \widetilde{P}\left(X_{15}\right) \sum_{X_{9} \ldots X_{12}} \widetilde{P}\left(M_{2} \mid X_{9} \ldots X_{12}\right) \times \\
& \widetilde{P}\left(X_{9}\right) \times \cdots \widetilde{P}\left(X_{12}\right) \times \sum_{X_{13}, X_{14}} \widetilde{P}\left(M_{3} \mid X_{13}, X_{14}\right) \times \widetilde{P}\left(X_{13}\right) \times \widetilde{P}\left(X_{14}\right)
\end{aligned}
$$

The comparison between the results of the method presented in this paper and the results of the fault tree analysis method is obtained by using MATLAB software simulation, as depicted in Figs. 7 and 8.
![img-6.jpeg](img-6.jpeg)

Figure 7: Comparison of the results (The state node T is 1 )
![img-7.jpeg](img-7.jpeg)

Figure 8: Comparison of the results (The state node T is 0.5 )
Based on the above system possibility analysis, it can be concluded that: the dynamical fuzzy possibility analysis results of leaf nodes include the dynamical fuzzy subsets of upper variable, center variable and lower variable. The central variable is almost the same as the one obtained by the traditional fault tree method. For a simple system with sufficient information and a clear fault logic relationship, the fault tree analysis method can be used; for the complex system with a lack of fault information and uncertain fault logic relationship, this method can clearly quantify and express the impact of cognitive uncertainty on system reliability. It does not need fault tree analysis and minimum cut set calculation, and it does not need to determine the complex algebraic expression of system reliability. It can be found that the method proposed in this paper can

effectively deal with the fuzziness caused by the lack of data or cognition in the engineering system.

# 3.3 Importance Analysis of Fuzzy Dynamic Root Node 

According to Eq. (10), when $T$ is 1 , the fuzzy importance of failure state $x_{i}^{k_{i}}=1$ is expressed by equation:

$$
\begin{aligned}
I_{11}^{\mathrm{Pr}}(t) & =E\left[\widetilde{P}\left(T=1 \mid X_{i}=1\right)-\widetilde{P}\left(T=1 \mid X_{i}=0\right)\right] \\
& =\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{11,1}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{11,0}}(t) d x}-\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{11,0}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{11,0}}(t) d x}
\end{aligned}
$$

Similarly, when $T$ is 1 , the fuzzy importance of failure state $x_{i}^{k_{i}}=0.5$ could be expressed as:

$$
\begin{aligned}
I_{11}^{\mathrm{Pr}}(t) & =E\left[\widetilde{P}\left(T=0.5 \mid X_{i}=1\right)-\widetilde{P}\left(T=0.5 \mid X_{i}=0\right)\right] \\
& =\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{11,0.5}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{11,0.5}}(t) d x}-\frac{\int_{0}^{1} x \widetilde{\mu}_{\widetilde{P}_{11,0}}(t) d x}{\int_{0}^{1} \widetilde{\mu}_{\widetilde{P}_{11,0}}(t) d x}
\end{aligned}
$$

According to Eqs. (10)-(12), when $T$ is 1 , the probability importance of $X_{i}$ can be expressed as Eq. (17):
$I_{1}^{\mathrm{Pr}}(t)=\frac{\sum_{k_{i}=1}^{2} I_{1, k_{i}}^{\mathrm{Pr}}(t)}{2}$
Similarly, when leaf node $T$ is 0.5 , the probability importance of $X_{i}$ could be concluded as Eq. (18):
$I_{0.5}^{\mathrm{Pr}}(t)=\frac{\sum_{k_{i}=1}^{2} I_{0.5, k_{i}}^{\mathrm{Pr}}(t)}{2}$
According to Eqs. (17) and (18), the fuzzy importance of root nodes at $\mathrm{t}=3000 \mathrm{~h}$ are calculated and also listed in Tab. 9.

Table 9: The fuzzy importance of $X_{i}$ at $t=3000 \mathrm{~h}$


According to the fuzzy importance of nodes, the system fault diagnosis and maintenance detection can be effectively carried out. Firstly, the most important components are inspected and maintained. The qualitative and quantitative evaluation methods proposed in this paper can also provide a theoretical basis for system fault diagnosis and maintenance strategy formulation.

According to Eqs. (17) and (18), The importance of $X_{1}$ presented in Fig. 9, while the leaf node is in state 0.5 and 1 .

It can be concluded that the system dynamic fuzzy importance analysis method is based on BN proposed in this paper. When the leaf node $T$ is in different fault states, the importance of the root node $X_{i}$ is a curve changing with time. As shown in Fig. 9, when the leaf nodes are in different fault states of 1 and 0 , the importance curves of the root nodes are different. The importance of T-S analysis is used to analyze the importance of the system, and the fixed value independent of time is obtained. When the importance of the components changes little with time, the difference between the result and the result of fault tree analysis is very small. For those with a large variation over time, if the T-S fuzzy importance analysis method is used to approximate the calculation, the results would have a large error, or even errors. Compared with the traditional reliability methods, the proposed method can make better use of the existing information and effectively deal with the fuzziness caused by a lack of data or insufficient cognition. Moreover, it can analyze the reliability of the multi-state system with dynamic problems, and the results are closer to the objective reality.
![img-8.jpeg](img-8.jpeg)

Figure 9: The importance of $X_{1}$ while $T$ is in state 0.5 and 1

# 4 Conclusion 

In this paper, the dynamic fuzzy theory is used to represent the cognitive uncertainty in the system. Combined with the advantages of the Bayesian network in system structure expression and probabilistic reasoning, fuzzy theory and the Bayesian network are integrated to realize the logical relationship expression and probabilistic reasoning of complex multi-state systems with cognitive uncertainty. The linear fuzzy subset function is introduced into the Bayesian network, and the dynamic fuzzy subset is established to describe the variety of node failure probability with time instead of the exact value, which can effectively solve the fuzziness and dynamics of fault information. The fuzzy multi-state CTP is used to describe the fault relationship between components. Compared with the traditional system reliability analysis, the multi-state of system faults

and the uncertainty of the logic relationship between faults are considered. We can apply this method to many practical problems that cannot be expressed in exact mathematics. In addition, the time-varying fault probability is considered. This method can make better use of the existing information of the system, and the analysis result is closer to the actual situation. This method makes full use of the advantages of the Bayesian network in probabilistic reasoning and can effectively represent and quantify the impact of cognitive uncertainty on system reliability without calculating the minimum cut set or determining the complex algebraic expression of system failure probability, which meets the actual needs of engineering. Therefore, the method proposed in this paper has certain significance in engineering.

Funding Statement: This research was supported by the Sichuan Science and Technology Department under Contract Nos. 2019YJ0396 and 2018JY0516, the National Natural Science Foundation of China under the Contract No. 51705041.

Conflicts of Interest: The authors declare that they have no conflicts of interest to report regarding the present study.
