# Article 

## Reliability Analysis of Failure-Dependent System Based on Bayesian Network and Fuzzy Inference Model

Shangjia Xiang, Yaqiong Lv (1), Yifan Li * and Lu Qian

## check for updates

Citation: Xiang, S.; Lv, Y.; Li, Y.; Qian, L. Reliability Analysis of Failure-Dependent System Based on Bayesian Network and Fuzzy Inference Model. Electronics 2023, 12, 1026. https://doi.org/10.3390/ electronics12041026

Academic Editor: Martin Reisslein
Received: 21 January 2023
Revised: 10 February 2023
Accepted: 16 February 2023
Published: 18 February 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

School of Transportation and Logistics Engineering, Wuhan University of Technology, Wuhan 430063, China

* Correspondence: yifan.li@whut.edu.cn


#### Abstract

With the rapid development of information and automation technology, the manufacturing system is evolving towards more complexity and integration. The system components will inevitably suffer from degeneration, and the impact of component-level failure on the system reliability is a valuable issue to be studied, especially when failure dependence exists among the components. Thus, it is vital to construct a system reliability evaluation mechanism that helps to characterize the healthy status of the system and facilitate wise decision making. In this paper, a reliability analysis framework for a failure-dependent system is proposed, in which copula functions with optimized parameters are used for the description of different failure correlations, and a fuzzy inference model is constructed to derive the subsystem reliability based on the component-level failure correlation. Finally, a Bayesian network is applied to infer the system reliability based on the system structure combined with the impact of failure correlation inside. Simulation results of the proposed method show that the inference results of system reliability are reasonable and effective in different cases. Compared with the copula Bayesian network method, the proposed method shows better adaptability to failure-dependent systems to varying degrees. This work can provide theoretical guidance for evaluating the reliability of manufacturing systems of different types.


Keywords: reliability analysis; failure-dependent system; copula function; fuzzy inference; Bayesian network

## 1. Introduction

The industrial manufacturing system is a complex system composed of various components, which may suffer from failure during the production activities. From a system perspective, component-level failure would have some influence on system reliability, which is generally reflected by the system performance. With the rapid development of information and sensing technology, data collection from system components has become more and more convenient, and the failure model of a component can be constructed and analyzed through various technical methods. However, determining how to evaluate system reliability based on the information of component-level failure is still a challenging problem, especially when failure correlation exists between the system components, which is always referred to as a failure-dependent manufacturing system. Actually, failure dependence exists in most practical engineering applications due to reasons including, but not limited to, standby redundancy mechanisms, load sharing, failure with a common cause, and cascade. Therefore, it is necessary to consider such failure dependence in practical manufacturing systems, to therefore propose new requirements for accurate failure correlation description and inspire further research on how to embed this correlation into the framework of system reliability analysis.

Through careful study of the related literature, it can be found that different research works have their own concerns, such as failure correlation description, derivation from component-level reliability to system-level reliability, or simulation techniques for reliability evaluation. Nonetheless, few existing works focus on constructing a systematic

framework of reliability analysis for failure-dependent manufacturing systems and providing comprehensive analysis of the key functions, including failure correlation description, and reliability derivation from components to the subsystem and the whole system. This motivates us to spend effort on formulating such a reliability analysis framework. The major contributions of this paper are summarized as follows:
(1) We take advantage of both copula functions and fuzzy inference methods to model the failure correlation between the components and the impact of this failure correlation on the subsystem, respectively. Furthermore, the fuzzy inference model is integrated into the Bayesian network model to achieve rational and effective reliability evaluation results for failure-dependent manufacturing systems. In this way, a reliability analysis framework based on copula functions, a fuzzy inference model, and a Bayesian network is proposed.
(2) Specifically, the copula function is carefully selected based on the goodness of fit of each tested type of copula function, and the corresponding parameter is optimized to obtain the most appropriate characterization of the failure correlation between different system components.
(3) By introducing the fuzzy inference model into the reliability analysis framework, we can avoid the obstacles of directly deriving the reliability values without precise knowledge about the system operation mechanism, while also taking advantage of the expert knowledge and experiences. It also has advantages such as the adaptability to derive system reliability values in the cases of various degrees of failure correlation among components in manufacturing systems.
(4) Generally, a manufacturing system has four structures, namely, series, parallel, series-parallel, and cycles, which can be modeled by production lines or networks. Our case study considers a typical series-parallel system in which failure processes of some components are independent, while failure correlation can exist between a pair of components in series or in parallel. Focusing on this general scenario, we comprehensively simulate and analyze the failure correlation description, and evaluate the subsystem reliability and system reliability, as well as the machine importance in the system. The reliability evaluation results of the proposed method are also compared with the copula Bayesian network method, and the rationality and effectiveness are verified. The proposed reliability analysis method can also be extended for different cases of failure-dependent manufacturing systems.

The reminder of this paper is organized as follows. Section 2 provides a review of the related work. Section 3 introduces the proposed system reliability analysis framework for failure-dependent manufacturing systems, including the copula description of the failure correlation among the system components, the fuzzy inference model to derive the impact of component-level correlation on the subsystem reliability, and the Bayesian network for the final inference of the system reliability. To show the validity and effectiveness of the proposed method, Section 4 applies it to a typical example of a manufacturing system, and provides comprehensive simulation and analysis results. Section 5 concludes this paper and discusses some future research directions.

# 2. Literature Review 

System reliability analysis has been a popular research issue in recent years, especially for complex manufacturing systems including multiple components where failures of the components can be correlated. There is already a lot of research on component-level fault diagnosis methods. Model-based fault diagnosis methods are widely used in simple systems, while data-driven approaches are more preferred for complex systems, which are difficult to model. Thanks to the rapid development of the Internet of Things (IoT) techniques, various kinds of data can be collected from the running equipment, which can be further used to acquire accurate knowledge about the health status and the remaining useful life (RUL) of the equipment and facilitate predictive maintenance decisions. Zhao et al. provided a comprehensive review of the early fault diagnosis methods focusing on vibration signals [1]. Wu et al. delivered an effective intelligent fault diagnosis method

for rolling bearings to ensure the machinery's stability and reliability [2]. Zhou et al. applied the Adabelief-BP neural network together with fuzzy decision making to study the multi-granularity faults of the production equipment, and further designed an intelligent prediction maintenance system [3]. Zheng et al. proposed a novel maintenance decisionmaking method for equipment based on Long Short-Term Memory and Markov decision process, which can provide specific maintenance strategies in different degradation stages of the system [4]. These models always make use of the data collected from sensors or other measurement instruments, while user data are rarely used [5]. Baptista et al. used the autoregressive moving average (ARMA) model and data-driven technology to build a fault prediction framework [5]. D. Yu et al. applied the data-driven deep confidence network to realize wind turbine fault detection and diagnosis [6]. In [7], Li et al. proposed a data-driven method for fault diagnosis and isolation of wind turbines, where long-term and short-term memory networks are used for learning and a random forest algorithm is used for decision making.

With the prediction results of the component-level failure, as well as information about the RUL or mean time between failure (MTBF), a credible reliability evaluation of the component can be achieved. However, for a multi-component system, the system reliability not only depends on the reliability of the constituent components, but also the relationship among them, since failures of some components will affect the reliability of the system as a whole. For simplicity, the component-level RULs are assumed to be independent, but this assumption may not hold when considering failure-dependent manufacturing systems, resulting in unsatisfactory evaluation of the system reliability. There are some commonly used methods to consider the correlation between component life [8]: (1) multivariate distribution such as multivariate lognormal distribution [9], Marshall-Olkin Weibull distribution [10], and multivariate Birnbaum-Saunders distribution [11]; (2) combined effects of positive and negative correlations [12]; and (3) copula functions. In recent years, modeling the failure correlation between components via copula functions has attracted a lot of attention from researchers, mostly due to its advantage of flexibility. Meng et al. combined the mixed copula function and nested copula function to establish a comprehensive failure correlation analysis model of mechanical systems, and studied the time-varying reliability of mechanical structures based on performance degradation [13]. Zuo et al. combined copula theory to analyze the system reliability of gear transmissions under three failure modes [14]. In [15], Wang et al. established a reliability model of CNC lathes considering the subsystem fault correlation, and analyzed the reliability allocation method considering the fault correlation. Zhang et al. illustrated the influence of dependency structure on system reliability and component importance using a copula function and simulations [16]. Sun et al. used nonparametric copula entropy and network deconvolution methods to discover the cause and effect of complex manufacturing systems, revealing the causal relationship between the parameters of complex systems [17]. In [18], Zhang et al. applied the copula-based hierarchical correlation method to analyze the impact of a redundancy allocation strategy and statistical correlation on the reliability of typical series-parallel systems. Moreover, the copula function was used to describe the statistical correlation between external subsystems and internal components.

Some scholars use Bayesian networks to study the system reliability considering the failure correlation. Song et al. proposed an improved Bayesian network combined with the probability box copula method to evaluate the system's reliability [19]. Ding et al. used the copula function to represent the relationship between variables, introduced the copula function in the traditional Bayesian network, and used the CBN structure to infer system reliability [20]. Sun et al. used the copula Bayesian network to model and analyze the system reliability [21].

The fuzzy inference model can deal with uncertain and imprecise information while also considering the logic of human knowledge. Therefore, it is regarded as an effective tool for manufacturing systems to infer and control production information in the production planning and scheduling process. Considering energy-saving operations, Wang et al.

designed fuzzy rules based on real-time data, and applied fuzzy inference to the production information to control the production process of the manufacturing system [22]. Lu et al. proposed a dynamic scheduling strategy with a multi-performance index based on fuzzy inference [23].

The fuzzy logic approach has also been applied to other fields. Li et al. utilized a fuzzy model to predict the evolution of surface scratching in sheet metals subject to contact sliding. In order to improve the prediction accuracy, the fuzzy model was further refined by the improved quantum-behaved particle swarm optimization (QPSO) algorithm [24]. Zhang et al. proposed a fuzzy PD control scheme based on a Back-Propagation Neural Network (BPNN) for the control problem of a three degrees of freedom manipulator. Combined with the BPNN, the performance of the traditional fuzzy PD algorithm was optimized by calibrating the overlap rate of membership functions online [25].

To sum up, a large number of research works have been conducted on system reliability analysis with different concerns. Some have focused on describing failure correlation between different components, while some have been interested in the derivation from component reliability to system reliability. Simulation methods are preferred by the researchers in this area due to the limitations of acquiring system reliability data from practical manufacturing systems. However, few existing methods show their adaptability to different manufacturing systems with various degrees of failure dependency, which motivates us to take advantage of both copula functions and the fuzzy inference method, to model the failure correlation between the components and the failure impact on the system, respectively. Furthermore, the fuzzy inference model is integrated into the Bayesian network to achieve a better reliability evaluation result for failure-dependent manufacturing systems. This work aims to advance the research of system reliability evaluation, providing theoretical guidance for evaluating the reliability of manufacturing systems of different types.

# 3. The Developed Method 

### 3.1. The Proposed Framework

The proposed framework of system reliability analysis for failure-dependent manufacturing systems is shown in Figure 1. Firstly, machine reliability data are collected from the manufacturing system. Based on data preprocessing and analysis, an appropriate data distribution is used to fit the historical data and construct the failure model of the machine. Moreover, information about failure independence or correlation can be obtained. Second, we use proper copula functions to describe the failure correlation between the machines, including smart selection of copula type and parameter optimization. Based on the above two steps, a Bayesian network combined with a fuzzy inference model is constructed to evaluate the system reliability, where the fuzzy inference model is specially designed to derive the reliability values of the subsystems with different types of failure correlation. Furthermore, Birnbaum importance is introduced to evaluate the machine importance in the system characterized by the Bayesian network. The results of system reliability analysis can be compared with the actual system reliability data measured by system performance, and reliable analysis results can act as a solid basis for further system fault diagnosis and maintenance decision making. The important details of the proposed framework regarding the failure correlation description, fuzzy inference model, and Bayesian network model are described in the following sections, respectively.

![img-0.jpeg](img-0.jpeg)

Figure 1. The proposed framework of system reliability analysis for failure-dependent manufacturing systems.

# 3.2. Failure Correlation Description Based on Copula Function 

Reliability refers to the probability that a product can complete the specified function under specified conditions within a given time. Reliability can also be expressed as a function of time $t$, denoted by $R(t)$. From the definition of the failure rate and the expression of the exponential distribution, the reliability can be described as follows:

$$
R(t)=e^{-\lambda(t) t}
$$

In contrast with reliability, the cumulative failure probability refers to the probability that a product fails to complete the specified function under specified conditions within a given time, which is also known as unreliability, commonly denoted by $F(t)$ with the following expression:

$$
F(t)=1-R(t)=P(T \leq t)=\int_{0}^{t} f(t) d t
$$

where $f(t)$ is the failure probability density function.
Considering a series of random variables with different marginal distributions, modeling their joint distribution will be difficult if they are not independent. To represent the joint distribution of such random variables, the concept of the copula function was proposed by Sklar in 1959 [26]. Let $X=\left(X_{1}, X_{2}, \cdots, X_{n}\right)^{T}$ be a random vector with marginal CDFs $F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \cdots, F_{n}\left(x_{n}\right)$, define their joint distribution as $H\left(x_{1}, x_{2}, \cdots, x_{n}\right)=$ $P\left(X_{1} \leq x_{1}, X_{2} \leq x_{2}, \cdots, X_{n} \leq x_{2}\right)$. Then, according to Sklar's Theorem, there exists a copula function $C$ such that:

$$
C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \cdots, F_{n}\left(x_{n}\right)\right)=H\left(x_{1}, x_{2}, \cdots, x_{n}\right)
$$

The theorem provides a method for modeling a multivariate joint distribution by utilizing marginal distributions. Firstly, we can construct a marginal distribution for each variable; then, we try to find an appropriate copula function and determine the

corresponding parameters, as an effective tool to characterize the correlations among different variables.

There are various types of copula functions, among which Archimedes copula and Elliptic copula are the most widely used copula families in academic research. In the Elliptic copula family, commonly used copula functions include $t$ copulas and Gaussian copulas. Both $t$ copulas and Gaussian copulas have symmetric tail correlations. They seem to be similar in central areas, while the main difference exists in the thickness of the tail. For simplicity, we consider two variables $u, v$ in the copula expressions in the following.
$\boldsymbol{t}$ copula: $t$ copula function for two variables $u, v$ can be expressed by:

$$
C_{t}(u, v ; \rho, k)=\int_{-\infty}^{t_{k}^{-1}(u)} \int_{-\infty}^{t_{k}^{-1}(v)} \frac{1}{2 \pi \sqrt{1-\rho^{2}}}\left(1+\frac{s^{2}-2 \rho s t+t^{2}}{k\left(1-\rho^{2}\right)}\right)^{-\frac{k+2}{2}} d s d t
$$

where $\rho$ is the linear correlation coefficient between the variables, and $\rho \epsilon[-1,1] \cdot t_{k}^{-1}(\cdot)$ is the inverse function of the univariate $t$-distribution with the degree of freedom $k$.

Gaussian copula: Gaussian copula function for two variables $u, v$ can be expressed by:

$$
C_{G a}(u, v ; \rho)=\int_{-\infty}^{\phi^{-1}(u)} \int_{-\infty}^{\phi^{-1}(v)} \frac{1}{2 \pi \sqrt{1-\rho^{2}}} \exp \left(-\frac{s^{2}-2 \rho s t+t^{2}}{2\left(1-\rho^{2}\right)}\right) d s d t
$$

where $\rho$ is the linear correlation coefficient between the variables, and $\rho \epsilon[-1,1] \cdot \phi^{-1}(\cdot)$ is the inverse function of the standard normal distribution.

The Archimedes copula family has the uniform function expression $C(u, v)=$ $\varphi^{-1}(\varphi(u)+\varphi(v))$, where $\varphi(\cdot)$ is the generator function of the Archimedes copulas. According to different generator functions, different Archimedes copulas can be obtained, among which the most commonly used ones include Gumbel copulas, Clayton copulas, and Frank copulas.

Gumbel copula: Gumbel copula for two variables $u, v$ is expressed as:

$$
C_{G}(u, v ; \theta)=\exp \left(-\left[(-\ln u)^{\theta}+(-\ln v)^{\theta}\right]^{1 / \theta}\right)
$$

where $\theta \epsilon[1,+\infty)$. It is a preferable option when describing variables with upper-tail correlation.
Clayton copula: Clayton copula for two variables $u, v$ is expressed as:

$$
C_{C}(u, v ; \theta)=\left(u^{-\theta}+v^{-\theta}-1\right)^{-1 / \theta}
$$

where $\theta \epsilon(0,+\infty)$. It is more suitable for describing variables with lower-tail correlation.
Frank copula: Frank copula for two variables $u, v$ is expressed as:

$$
C_{F}(u, v ; \theta)=-\frac{1}{\theta} \ln \left(1+\frac{\left(e^{-\theta u}-1\right)\left(e^{-\theta v}-1\right)}{e^{-\theta}-1}\right)
$$

where $\theta \epsilon(-\infty, 0) \cup(0,+\infty)$. It is commonly used to describe variables with both upper-tail and lower-tail correlations.

Since there are various types of copula functions, and different types of copula functions are suitable for describing different kinds of correlation, smart selection of the most proper copula is of great importance for an accurate description of failure correlation.

In this paper, the Akaike information criterion (AIC) is adopted to estimate the correlation parameters between different variables and identify the most appropriate copula function. AIC is a standard means of measuring the goodness of fit of statistical models, proposed by Akaike, a Japanese statistician, in 1973, which is defined as:

$$
\mathrm{AIC}=2 k-2 \ln (L)
$$

where $k$ is the number of the unknown parameters in the model, and $L$ is the value of the maximum likelihood function. Considering a pair of machines $M_{1}, M_{2}$ in the failuredependent manufacturing system, $L$ can be expressed by:

$$
L=\sum_{i=1}^{n} \ln \left(c\left(F_{1}\left(m_{1 i}\right), F_{2}\left(m_{2 i}\right)\right) \mid \theta\right)
$$

where $F_{1}\left(m_{1}\right), F_{2}\left(m_{2}\right)$ denote the marginal CDFs of the MTBF of machines $M_{1}$ and $M_{2}$, respectively. The sample set is denoted by $\left\{m_{1 i}, m_{2 i}\right\}(i=1,2, \cdots, n)$, where $n$ is the total number of samples. In general, the difference between two statistical models is mainly reflected by $L$; however, when the difference in $L$ is insignificant, the model complexity measured by $k$ becomes dominant. When applying AIC to determine the best model, the model with the smallest AIC is usually considered to be the best among a group of available models.

# 3.3. Subsystem Reliability Evaluation Based on Fuzzy Inference Model 

In this paper, the fuzzy inference model is applied to evaluate the subsystem reliability. The structure of the fuzzy inference system is shown in Figure 2:
![img-1.jpeg](img-1.jpeg)

Figure 2. Fuzzy inference system for the evaluation of subsystem reliability.
(A) Fuzzification: In this step, the clear values of the input data are converted to fuzzy values according to the membership functions, where different forms of membership functions are able to describe different cases of fuzziness. In this paper, the Gaussian membership function is used due to its wide application and advantage in smoothness, as well as better characterization of human thinking. Moreover, the shape of the Gaussian membership function can approximate triangular, trapezoidal, and other membership functions. The Gaussian membership function is expressed by:

$$
f(x ; \sigma, c)=e^{-\frac{(x-c)^{2}}{2 \sigma^{2}}}
$$

where $c$ denotes the abscissa value corresponding to the peak value of the Gaussian membership function, and the standard deviation $\sigma$ represents the width of the Gaussian membership function curve. The double Gaussian membership function is composed of two Gaussian membership functions, where each Gaussian function defines the one-sided shape of the membership function, and the connection part between the two Gaussian membership functions is defined by $f(x)=1$. The images of the Gaussian membership function and double Gaussian membership function are shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. Gaussian membership function and double Gaussian membership function.
(B) Fuzzy rule base: Fuzzy rules play the key role in a fuzzy inference system, which are also referred to as if-then rules.
(C) Inference engine: It integrates the input fuzzy sets based on fuzzy rules and exports the integrated output fuzzy sets. Widely used fuzzy inference models include the Sugeno fuzzy inference model and the Mamdani fuzzy inference model. In this paper, the Mamdani fuzzy inference model is applied for logical inference.
(D) Defuzzification: In this step, the fuzzy value obtained by the inference engine is converted back to a clear value, acting as the inference output of the fuzzy inference system. Commonly used defuzzification methods include the maximum membership method and centroid defuzzification method. Considering that the centroid defuzzification method has better sensitivity, which can even respond to a slight change in input, and it also can achieve a smoother output, we apply the centroid defuzzification method in this paper. Specifically, the centroid of the area enclosed by the membership function curve and the horizontal axis is taken as the output value of the fuzzy inference system, which is expressed by:

$$
v_{0}=\frac{\int_{S} x \mu_{V}(x) d x}{\int_{S} \mu_{V}(x) d x}
$$

# 3.4. System Reliability Analysis Based on Bayesian Network Model 

As pointed out by Lloyd DK et al. in 1962, for a series system composed of $n$ identical components, the system reliability $R_{n}$ takes the value between the reliability of each component (denoted by $R$ ) and the product of individual reliability (denoted by $R^{n}$ ), with the assumption that the reliability of each component is the same [27]. When the failures of various components are mutually independent, the system-level reliability can be obtained directly from the product of the component-level reliability. However, in most cases, the independent property is not satisfied due to the interaction between failures, thus the effect of such failure dependency needs to be considered for the system reliability. With the assumption that the failures are positively correlated, G. Fang et al. proved that the system reliability satisfies the following properties [28].

1. For a series failure-dependent system,

$$
\prod_{i=1}^{n} R_{i} \leq R \leq \min R_{i}
$$

2. For a parallel failure-dependent system,

$$
\max R_{i} \leq R \leq 1-\prod_{i=1}^{n}\left(1-R_{i}\right)
$$

where $n$ is the number of components consisting of the series or parallel system.
Based on the above analysis of the system reliability, a Bayesian network can be used to further analyze the system performance, and is applied in this paper. The Bayesian network is a directed acyclic graph model, which is used to describe the dependence among the

variables. It is composed of a series of variable nodes and directed edges connecting these nodes, where the nodes represent the random variables, and the directed edges describe the relationship between these random variables. The strength of the relationship is measured by the conditional probability.

For subevents $A, B$ and the joint event $A B$ in a Bayesian network, the conditional probability $P(A \mid B)$ is denoted by:

$$
P(A \mid B)=\frac{P(A B)}{P(B)}
$$

The joint probability $P\left(X_{1}, X_{2}, \cdots, X_{n}\right)$ of the Bayesian network is expressed by:

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p\left(X_{i}\right)\right)
$$

where $p\left(X_{i}\right)$ denotes the parent node of the current node, and $P\left(X_{i} \mid p\left(X_{i}\right)\right)$ is the conditional probability of the current node with the specified parent node.

A Bayesian network can be used for bidirectional inference, including both causal inference and diagnostic inference. Causal inference is a forward inference procedure starting from priori probability, while diagnostic inference is helpful in dealing with a case with a known result, but where the possible reason for this result is of interest.
(A) System reliability evaluation

According to the structural relationship between the system components and their failure distributions, the nodes and edges of the Bayesian network, as well as the corresponding parameters, can be determined. Considering a typical series-parallel system consisting of 10 components, in which failure correlation exists in Machine pair 5-6 and Machine pair 7-8, while the failure distributions of the other machines are assumed to be independent, then the construction of the Bayesian network can be described in the following, as shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network construction.
After constructing the Bayesian network according to the manufacturing system, the system reliability can be obtained through Bayesian network inference based on knowledge about the reliability values of the consisting nodes. However, this inference will become quite complicated as the size of the network increases. Generally, the assumption of the

conditional independence of nodes can apparently simplify the analysis process of the Bayesian network. Let $S$ denote the event of system failure and $W_{i}$ denote the event of node failure; the probability of system failure can be obtained from Bayesian forward inference, which is expressed as:

$$
P(S)=P\left(S \mid W_{1}, W_{2}, \cdots, W_{n}\right) \cdot P\left(W_{1}\right) \cdot P\left(W_{2}\right) \cdot \cdots \cdot P\left(W_{n}\right)
$$

Combined with Equation (16), and according to the known failure probabilities of the network nodes, the inference results of the system reliability can be achieved. Considering the 10-component system shown in Figure 4, the system reliability can be obtained from the Bayesian network model:

$$
\begin{gathered}
R(S)=P\left(S=1 \mid S_{1}=1, S_{2}=1, S_{3}=1, S_{4}=1\right) \cdot P\left(S_{1}=1\right) \cdot P\left(S_{2}=1\right) \cdot P\left(S_{3}=1\right) \cdot P\left(S_{4}=1\right) \\
=R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right)
\end{gathered}
$$

For subsystems $S_{1}$ and $S_{2}$ consisting of failure-independent components, the subsystem reliability can be calculated as:

$$
\begin{gathered}
R\left(S_{1}\right)=P\left(S_{1}=1 \mid M_{1}=1\right) \cdot P\left(M_{1}=1\right) \\
=R\left(M_{1}=1\right) \\
R\left(S_{2}\right)=1-P\left(S_{2}=0 \mid M_{2}=0, M_{3}=0, M_{4}=0\right) \cdot P\left(M_{2}=0\right) \cdot P\left(M_{3}=0\right) \cdot P\left(M_{4}=0\right) \\
=1-\left(1-R\left(M_{2}\right)\right) \cdot\left(1-R\left(M_{3}\right)\right) \cdot\left(1-R\left(M_{4}\right)\right)
\end{gathered}
$$

For subsystem $S_{3}$ consisting of failure-correlated components Machine 5 and Machine 6 , where the failure correlation is descripted by copula functions, the reliability value can be calculated as:

$$
R\left(S_{3}\right)=R\left(M_{56}\right)=R\left(M_{5}\right)+R\left(M_{6}\right)-C_{56}
$$

where $C_{56}$ denotes the value of the copula function describing the failure correlation of Machine pair 5-6.

For subsystem $S_{4}$ consisting of subsystem $S_{5}$ and failure-correlated components Machine 7 and Machine 8, where the failure correlation is descripted by copula functions, the reliability of Machine pair 7-8 needs to be calculated first:

$$
R\left(M_{78}\right)=C_{78}
$$

where $C_{78}$ denotes the value of the copula function describing the failure correlation of Machine pair 7-8. Then the reliability value of subsystem $S_{4}$ can be calculated as:

$$
\begin{aligned}
R\left(S_{4}\right)=1-P\left(S_{4}=0 \mid M_{78}=0, S_{5}\right. & =0) \cdot P\left(M_{78}=0\right) \cdot\left(1-P\left(S_{5}=1 \mid M_{9}=1, M_{10}=1\right) \cdot P\left(M_{9}=1\right) \cdot P\left(M_{10}=1\right)\right) \\
& =1-\left(1-R\left(M_{78}\right)\right) \cdot\left(1-R\left(M_{9}\right) \cdot R\left(M_{10}\right)\right)
\end{aligned}
$$

(B) Component importance analysis

Moreover, by applying the reverse inference function of the Bayesian network, the node importance can be obtained, which can be used to judge which components have a vital impact on the system reliability. Birnbaum importance is used to describe the impact of a change in component reliability on the change in the system reliability. It can measure the difference in system reliability when a component in working state turns to failure. For system component $i$, the Birnbaum importance can be calculated as:

$$
I_{B}(i)=\operatorname{Pr}\left\{\phi(S)=1 \mid M_{i}=1\right\}-\operatorname{Pr}\left\{\phi(S)=1 \mid M_{i}=0\right\}
$$

Taking Machine 1 as an example, the Birnbaum importance is expressed by:

$$
\begin{aligned}
I_{B}(1)=\operatorname{Pr}\left\{\phi(S)\right. & \left.=1 \mid M_{1}=1\right\}-\operatorname{Pr}\left\{\phi(S)=1 \mid M_{1}=0\right\} \\
=P\left(S=1 \mid S_{1}=1, S_{2}=1, S_{3}=1, S_{4}=1\right) \cdot\left[P\left(S_{1}\right.\right. & \left.=1 \mid M_{1}=1\right) \cdot P\left(M_{1}=1\right) \mid \cdot P\left(S_{2}=1\right) \cdot P\left(S_{3}=1\right) \cdot P\left(S_{4}=1\right) / P\left(M_{1}=1\right) \\
& =R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right)
\end{aligned}
$$

Similarly, for each machine in the manufacturing system modeled by the Bayesian network, the corresponding Birnbaum importance can be obtained in this way:

$$
\begin{gathered}
I_{B}(2)=R\left(S_{1}\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right)-R\left(S_{1}\right) \cdot\left(1-\left(1-R\left(M_{3}\right)\right) \cdot\left(1-R\left(M_{4}\right)\right)\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right) \\
I_{B}(3)=R\left(S_{1}\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right)-R\left(S_{1}\right) \cdot\left(1-\left(1-R\left(M_{2}\right)\right) \cdot\left(1-R\left(M_{4}\right)\right)\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right) \\
I_{B}(4)=R\left(S_{1}\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right)-R\left(S_{1}\right) \cdot\left(1-\left(1-R\left(M_{2}\right)\right) \cdot\left(1-R\left(M_{3}\right)\right)\right) \cdot R\left(S_{3}\right) \cdot R\left(S_{4}\right) \\
I_{B}(56)=R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{4}\right) \\
I_{B}(78)=R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right)-R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot\left(R\left(M_{9}\right) \cdot R\left(M_{10}\right)\right) \\
I_{B}(9)=R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot\left(1-\left(1-R\left(M_{78}\right)\right) \cdot\left(1-R\left(M_{10}\right)\right)\right)-R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot R\left(M_{78}\right) \\
I_{B}(10)=R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot\left(1-\left(1-R\left(M_{78}\right)\right) \cdot\left(1-R\left(M_{9}\right)\right)\right)-R\left(S_{1}\right) \cdot R\left(S_{2}\right) \cdot R\left(S_{3}\right) \cdot R\left(M_{78}\right)
\end{gathered}
$$

Based on the analysis results of system reliability and component importance, further system fault diagnosis can be undertaken, as well as timely maintenance decisions, as shown in the proposed system reliability analysis framework in Figure 1. For maintenance decision making, an intuitive and effective solution is comparing the obtained evaluation results of system reliability to a properly pre-set threshold, and maintenance operations are recommended when the reliability evaluation result falls below the threshold. Liu et al. studied the dynamic preventive maintenance strategy of the continuous degradation system of components. When the system reliability is lower than a certain threshold, the maintenance operation is triggered [29]. D. Valis et al. modeled the field data of a drinking water distribution system, and predicted the behavior and future state of water mains, providing a reference and guidance for the maintenance model [30]. In future study, we will attempt to make full use of the system reliability evaluation results to decide the optimal time of maintenance intervention. Moreover, based on the analysis results of component importance, which can highlight the components that should be paid more attention and recommended for further diagnosis, appropriate and timely maintenance decisions can be made.

# 4. Case Study 

### 4.1. Experiment Description

In this section, we show how the proposed reliability analysis framework can be applied in a typical series-parallel manufacturing system through a 10-component system with the structure sketched in Figure 5. Note that the structure is general, and can be extended to any combinations of series, parallel, or series-parallel configurations.
![img-4.jpeg](img-4.jpeg)

Figure 5. Diagram of a typical series-parallel manufacturing system.
As shown in Figure 5, the manufacturing system consists of 10 machines numbered from 1 to 10 . To model the degradation process of the machines, data of the "Predictive Useful Life based into telemetry" project are used, which includes plentiful information,

such as the age and RUL of each machine, as well as the reasons of failures. Here, the RUL data measure the time interval between two consecutive failures of a machine, and are equivalent to the MTBF data. Part of the project data is shown in Table 1.

Table 1. Part of the project data used in our case study.


Based on the collected machine MTBF data, data analysis and data distribution fitting for each machine can be undertaken. In this paper, the widely used Weibull distribution is used to fit the MTBF data of each machine with the corresponding age, which has the following expression:

$$
f(x ; \beta, \eta)=\left\{\begin{array}{cc}
\frac{\beta}{\eta}\left(\frac{x}{\eta}\right)^{\beta-1} e^{-\left(\frac{x}{\eta}\right)^{\beta}}, & x<0 \\
0, & x \geq 0
\end{array}\right.
$$

where $\beta$ is the shape parameter and $\eta$ is the size parameter. Through investigation of the data distributions of the machines, failure-correlated machines can be identified. In this paper, due to the limit of acquiring failure-correlated machine data, we assume that prior knowledge of failure correlation is available, and parallel Machine pair 5-6 and series Machine pair 7-8 are assumed to be failure-correlated, while the failure distributions of the other machines are assumed to be independent. In this case, we also generate some MTBF data using Monte Carlo simulation and apply Weibull distributions for data distribution fitting of the failure-correlated machine pairs.

For general considerations in our case, the age of Machines 1, 2, 3, 4, 9, 10 are assumed to be 14 , while those of Machine 5 and Machine 7 are assumed to be 15 and 18, respectively.

It can be obtained from the data that the degradation of Machines 1, 2, 3, 4, 9, 10 obeys a Weibull distribution with $\beta=2.2042, \eta=58.7760$; the degradation of Machine 5 obeys a Weibull distribution with $\beta=2.4571, \eta=54.2726$; and the degradation of Machine 7 obeys a Weibull distribution with $\beta=3.6041, \eta=50.0640$. Due to the existence of fault correlation in Machine pair 5-6, as well as Machine pair 7-8, we generate the MTBF data of Machine 6 based on the data of Machine 5 using Monte Carlo simulation. Similarly, the MTBF data of Machine 8 are generated based on the data of Machine 7. After data distribution fitting by the Weibull distribution, it can be obtained that the degradation of Machine 6 obeys a Weibull distribution with $\beta=2.7815, \eta=52.0825$, and the degradation of Machine 8 follows a Weibull distribution with $\beta=3.4973, \eta=46.1239$ through Monte Carlo simulation.

According to Figure 4 regarding the Bayesian network construction in Section 3.4, a Bayesian network based on the 10 -component system can be constructed.

# 4.2. Failure Correlation Analysis 

In this section, copula functions are used to characterize the failure correlations of Machine pair 5-6 and of Machine pair 7-8. Firstly, proper types of copula functions are selected to describe the failure correlation between the machines, based on the AIC value introduced in Section 3.2. Then, the corresponding parameters of the selected copula functions are optimized to achieve more appropriate descriptions of the failure correlations.

(A) Copula function selection

Through investigating the binary histogram of reliability values of Machine pair 5-6 and of Machine pair 7-8, as shown in Figure 6, it can be seen that there exists an apparent upper-tail correlation and a less obvious correlation in both binary histograms. According to the introduction of different types of copula functions in Section 3.2, the Frank copula function, which is commonly used to describe variables with both upper-tail and lower-tail correlations, seems a suitable choice.
![img-5.jpeg](img-5.jpeg)

Figure 6. Binary histograms of reliability values: (a) Machine pair 5-6; (b) Machine pair 7-8.
To verify this hypothesis, different types of copula functions, including Clayton copula, Frank copula, Gumbel copula, Gaussian copula, and $t$ copula, are applied to describe the correlations between reliability values of Machine pair 5-6 and Machine pair 7-8. Then, the AIC values corresponding to the five types of copula functions are calculated for both machine pairs. The calculation results for Machine pair 5-6 and Machine pair 7-8 are presented in Tables 2 and 3, respectively. It can be seen that for Machine pair 5-6, the Frank copula with the smallest AIC value is considered to be the best model to describe the correlation between Machine 5 and Machine 6. Similarly, the AIC value of the Frank copula is the smallest for Machine pair 7-8, indicating that the Frank copula is the most appropriate model for describing the correlation between Machine 7 and Machine 8. The verification results coincide with our preliminary conclusions from reading the binary histograms of reliability values as shown in Figure 6.

Table 2. Parameters and AIC values of different copula functions for Machine pair 5-6.


Table 3. Parameters and AIC values of different copula functions for Machine pair 7-8.


(B) Parameter optimization of copula function

So far, the Frank copula with the form expressed by Equation (8) has been selected as the most proper type of copula function to model the failure correlation for Machine pair 5-6 and Machine pair 7-8. For the next step, the value of parameter $\theta$ in Equation (8) must be optimized for a reliable description. By applying the maximum likelihood estimation

method, we can determine that $\theta$ takes the value in the range [13.1812, 13.8507] in a $95 \%$ confidence interval for Machine pair 5-6, while for Machine pair 7-8, $\theta$ takes the value in the range [15.5882, 16.4106] in a $95 \%$ confidence interval.

With the objective of minimizing the AIC value corresponding to $\theta$, the optimal value of $\theta$ can be achieved. For Machine pair 5-6, the optimal parameter $\theta^{*}=13.5193$, while for Machine pair 7-8, the optimal parameter $\theta^{*}=15.9952$. The images of Frank copula functions with optimized parameters for Machine pair 5-6 and Machine pair 7-8 are shown in Figure 7. It can be seen that the images show apparent lower-tail correlation and uppertail correlation, which are in accordance with the binary histograms shown in Figure 6. To summarize, Frank copula functions with optimized parameters can provide an appropriate description of the failure correlations.
![img-6.jpeg](img-6.jpeg)

Figure 7. Images of Frank copula functions with optimized parameters for Machine pair 5-6 and Machine pair 7-8.

# 4.3. Construction of the Fuzzy Inference System 

According to Figure 2 regarding the fuzzy inference system for the evaluation of subsystem reliability in Section 3.3, a fuzzy inference system is constructed for the 10-component system. The details are provided in the following.
(A) Fuzzification: membership function design

In the considered system with the structure shown in Figure 5, assuming that all the machines are independent of each other, i.e., no failure correlation exists in this system, then the reliability value of the subsystem consisting of Machine 5 and Machine 6 can be obtained by:

$$
R_{56}=1-\left(1-R_{5}\right) \cdot\left(1-R_{6}\right)
$$

Under the same assumption, the reliability value of the subsystem consisting of Machine 7 and Machine 8 is given by:

$$
R_{78}=R_{7} \cdot R_{8}
$$

However, the failure correlation actually exists in the system; let $R_{56}{ }^{\prime}$ and $R_{78}{ }^{\prime}$ denote the reliability value of the failure-correlated parallel subsystem consisting of Machine 5 and Machine 6 and that of the failure-correlated series subsystem consisting of Machine 7 and Machine 8, respectively. Let $C_{56}$ and $C_{78}$ denote the value of the copula function describing the failure correlation in Machine pair 5-6 and Machine pair 7-8, respectively. In this paper, we use the Gaussian membership function and the double Gaussian membership function to describe the fuzziness of data. As introduced in Section 3.3, the Gaussian membership function has two parameters $c$ and $\sigma$, while for the double Gaussian membership function, parameters $c_{1}, \sigma_{1}$ describe the left-hand shape of the membership function, and $c_{2}, \sigma_{2}$ describe the right-hand shape of the membership function. In our case study, the

Table 4. Parameters of the membership functions designed for $C_{56}$ and $C_{78}$.


Table 5. Parameters of the membership functions designed for $R_{56}$ and $R_{78}$.


Table 6. Parameters of the membership functions designed for $R_{56}{ }^{\prime}$ and $R_{78}{ }^{\prime}$.


Table 6. Parameters of the membership functions designed for $R_{56}{ }^{\prime}$ and $R_{78}{ }^{\prime}$.


Alternatively, other types of membership functions, such as the triangular membership function and trapezoidal membership function, can be used in the fuzzification step. Taking $C_{56}$ as an example, the failure correlation description by different choices of membership functions is shown in Figure 8. Further comparison results of reliability evaluation based on different descriptions of failure correlation will be provided in Section 4.4.
![img-7.jpeg](img-7.jpeg)

Figure 8. Description of $C_{56}$ by different types of membership functions: (a) Gaussian membership function and double Gaussian membership function; (b) triangular membership function and trapezoid membership function.
(B) Fuzzy rule design

As a key part in a fuzzy inference system, fuzzy rules need to be properly designed. From Equation (13), it can be found that for a series system, the system reliability takes the

minimum value when all components are independent. When failure correlation exists in the system, the system reliability inferred by the fuzzy inference system should take a larger value than that of a failure independent system. Combined with Equation (22) introduced in Section 3.4, it can be found that as the failure correlation measured by copula function increases, the inference result of the system reliability is supposed to increase. For a parallel system, it can be seen from Equation (14) that the system reliability takes the maximum value when all components are independent. With failure correlation, the system reliability inferred by the fuzzy inference system should take a smaller value when compared with a failure independent system. Combined with Equation (21) introduced in Section 3.4, it can be concluded that the inferred value of the system reliability is supposed to decrease as the failure correlation measured by the copula function increases. Our fuzzy rule design follows these conclusions. Moreover, expert experience is integrated in fuzzy rule design, especially for practical systems.

For Machine pair 5-6 connected in parallel, the fuzzy rule has the form "if $R_{56}=A$ and $C_{56}=B$, then $R_{56}{ }^{\prime}=C$ ". Similarly, for Machine pair 7-8 connected in series, the fuzzy rule has the form "if $R_{78}=A$ and $C_{78}=B$, then $R_{78}{ }^{\prime}=C$ ". In order to model various degrees of failure correlation among components in practical systems, we take two cases as examples, namely, weak failure correlation and strong failure correlation, to show our fuzzy rule design according to different degrees of failure correlation.

The fuzzy rules designed for weak and strong failure correlation of Machine pair 5-6 are shown in Tables 7 and 8, respectively, while the fuzzy rules designed for weak and strong failure correlation of Machine pair 7-8 are shown in Tables 9 and 10, respectively.

Table 7. Fuzzy rules designed for weak failure correlation Machine pair 5-6.


Table 8. Fuzzy rules designed for strong failure correlation Machine pair 5-6.


Table 9. Fuzzy rules designed for weak failure correlation Machine pair 7-8.


Table 10. Fuzzy rules designed for strong failure correlation Machine pair 7-8.


(C) Inference engine

In this paper, the inference engine obtains the fuzzy inference results of the system reliability based on the membership function and fuzzy rule design introduced in (A) and (B).
(D) Defuzzification

In this step, the piecewise defuzzification method is applied to achieve better results for extreme cases. The steps are shown as follows:
(1) For the part with subsystem reliability $R \geq 0.98$ under the independence assumption, the maximum value of the membership function when the membership degree is 0.99 is used for defuzzification.
(2) For the part with subsystem reliability $R \leq 0.02$ under the independence assumption, the minimum value of the membership function when the membership degree is 0.99 is used for defuzzification.
(3) For the part of subsystem reliability $0.02<R<0.98$ under the independence assumption, the centroid method is used for defuzzification.

# 4.4. System Reliability Analysis 

In this section, the evaluation results of subsystem reliability for Machine pair 5-6 and Machine pair 7-8 by applying the proposed method are presented. Comparison results with the copula Bayesian network method are also provided. Based on the Bayesian network construction of the 10-component system and the subsystem reliability evaluation results for Machine pair 5-6 and Machine pair 7-8, the reliability evaluation results of the whole system in different cases are presented. Additionally, we conduct the machine importance analysis as introduced and calculated in Section 3.4.

(A) Subsystem reliability evaluation

In this section, we focus on parallel Machine pair 5-6 and series Machine pair 7-8 and make subsystem reliability inference. For the proposed method, both cases of weak failure correlation and strong failure correlation are considered.

Considering Machine pair 5-6, the subsystem reliability inference results under weak fault correlation and strong fault correlation using the Gaussian membership function and double Gaussian membership function are shown in Figure 9a, while Figure 9b presents the subsystem reliability inference results with different choices of membership functions. Similarly, for Machine pair 7-8, the subsystem reliability inference results under weak fault correlation and strong fault correlation based on different selections of membership functions are exhibited in Figure 10.
![img-8.jpeg](img-8.jpeg)

Figure 9. Subsystem reliability evaluation of Machine pair 5-6: (a) Gaussian membership function and double Gaussian membership function selected; (b) triangular membership function and trapezoid membership function selected.
![img-9.jpeg](img-9.jpeg)

Figure 10. Subsystem reliability evaluation of Machine pair 7-8: (a) Gaussian membership function and double Gaussian membership function selected; (b) triangular membership function and trapezoid membership function selected.

It can be seen from Figures 9 and 10 that the proposed method can achieve reasonable and effective inference results of system reliability under different cases. Being capable of describing different degrees of failure correlation among the components within a system, the proposed method can have wide applications in practical manufacturing systems. Moreover, by comparing Figure 9a,b, it is obvious that using the Gaussian membership function and double Gaussian membership function can achieve smoother inference results of subsystem reliability. A similar conclusion can be obtained from the comparison results presented in Figure 10a,b, which also verifies our choice of the Gaussian membership function and double Gaussian membership function in this paper.

The subsystem reliability inference results of the proposed method in different cases, i.e., weak failure correlation and strong failure correlation, are also compared with the reliability of the failure-independent subsystem, and the reliability inference results when the copula Bayesian network method is used. The comparison results are shown in Tables 11 and 12, respectively.

Table 11. Comparison of subsystem reliability of Machine pair 5-6.


Table 12. Comparison of subsystem reliability of Machine pair 7-8.


It can be seen that for parallel systems, the reliability inference results of the proposed method have lower values than the reliability values under independence assumptions, whereas for series systems, the subsystem reliability inference results of the proposed method have higher values than the reliability values under independence assumptions. This is also the case for the copula Bayesian network method. The inference results are reasonable. Moreover, we can find that the piecewise defuzzification method applied in this paper can effectively deal with the extreme cases when the reliability value approximates 1 or 0 .
(B) System reliability evaluation

In this section, the reliability inference results of the 10-component system in different cases are compared and analyzed, as shown in Figure 11. We consider the following cases:

![img-10.jpeg](img-10.jpeg)

Figure 11. Comparison of the system reliability inference results.
(1) Case 1: Failure-correlated system: Machine pair 5-6 independent, Machine pair $7-8$ completely related;
(2) Case 2: Failure-correlated system: Machine pair 5-6 completely related, Machine pair $7-8$ independent;
(3) Case 3: Failure-correlated system: copula Bayesian network;
(4) Case 4: Failure-correlated system: the proposed method (Machine pair 5-6 weakly failure-correlated, Machine pair 7-8 strongly failure-correlated);
(5) Case 5: Failure-correlated system: the proposed method (Machine pair 5-6 strongly failure-correlated, Machine pair 7-8 weakly failure-correlated).

It can be found that the system reliability inference results derived from the proposed method for both the cases of weak failure correlation and strong failure correlation are between the values in the extreme cases (Case 1 and Case 2); this is also the case for the copula Bayesian network method. The system reliability inference results are reasonable and effective. Compared with the copula Bayesian network method, which cannot distinguish different degrees of failure correlation, the proposed method is capable of describing different types of failure correlation within the system through properly adjusting the fuzzy inference model, and thus shows better adaptability to different types of failure correlation in manufacturing systems.
(C) Machine importance analysis

Based on the component importance analysis for each machine in the 10-component system, as introduced in Section 3.4, the Birnbaum importance of each machine can be obtained in different cases of weak failure correlation or strong failure correlation. Take two cases as examples: (1) Case 1: Machine pair 5-6 weakly failure-correlated, Machine pair $7-8$ strongly failure-correlated; and (2) Case 2: Machine pair 5-6 strongly failure-correlated, Machine pair 7-8 weakly failure-correlated. The corresponding Birnbaum importance results of the machines are shown in Figures 12 and 13, respectively.

It is observed that the Birnbaum importance values of each machine/machine pair are between 0 and 1. In the beginning, all machines are working normally, thus the system is in a working state with probability 1 . Therefore, the Birnbaum importance of all machines is 0 at this time. As the system operation time increases, machines in the system start to suffer from failure and finally the system fails. At this time, a single machine cannot enable the system to work again when it changes from a failure state to a working state. This is the reason why the Birnbaum importance of all machines finally returns to 0 . From Figures 12 and 13, it can be seen that Machine 1 and Machine pair 5-6 are of high importance in the system, which indicates that these machines need to be checked first in case of system failure. We also find that under different failure correlations among the components, the Birnbaum importance of each machine/machine pair is different.

![img-11.jpeg](img-11.jpeg)

Figure 12. Machine Birnbaum importance (Case 1).
![img-12.jpeg](img-12.jpeg)

Figure 13. Machine Birnbaum importance (Case 2).
To summarize, by introducing the fuzzy inference model, the proposed method can achieve effective subsystem reliability inference results and system reliability inference results, as well as the analysis results of Birnbaum importance for all machines, for different types of manufacturing systems, where the component-level failure correlation can be quite different, indicating failure-dependent systems with varying degrees.

# 5. Conclusions 

In this paper, we propose a reliability analysis method for failure-dependent systems, where copula functions with optimized parameters are used to describe the failure correlation among the system components, and a fuzzy inference model is constructed to derive the impact of the component-level failure correlation on the subsystem reliability. Finally, a Bayesian network is applied for the final inference of the system reliability, and Birnbaum importance is used for analysis of the importance of different system components, which can further facilitate maintenance decision making. Different from the existing works, we focus on constructing a systematic framework of reliability analysis for failure-dependent manufacturing systems. By creatively introducing copula functions, a fuzzy inference model, and a Bayesian network into the analysis framework, both the system structure and the failure correlation among the system components are taken into consideration to achieve rational and effective inference results of system reliability. A notable advantage of applying the fuzzy inference model in the framework is that we can avoid the obstacles

of directly deriving the reliability values without precise knowledge about the system operation mechanism, while also taking advantage of expert knowledge and experiences in practice.

We conducted a case study of a typical example of the manufacturing system including different types of component-level failure correlation, and provide comprehensive analysis of the key results including failure correlation description, and reliability derivation from component to subsystem and the whole system. Through simulations, the proposed method achieved inference results of system reliability that were reasonable and effective in different cases. The proposed method also shows better adaptability to failure-dependent systems with varying degrees, when compared with the method of the copula Bayesian network. Due to its advantages in the characterization effect of the manufacturing system reliability, the proposed method has a wide range of applications. This work aims to expand the analysis framework of system reliability, and provides theoretical guidance for evaluating reliability of manufacturing systems with different types, which is valuable for further decision making on system maintenance or scheduling. However, there are still some limitations in this paper. For instance, only the commonly used series-parallel system is investigated, and systems with more complex structures will be discussed in the future. Furthermore, determining how to make maintenance decisions based on the reliability analysis results is another concern that will be addressed in our future work.

Author Contributions: Conceptualization, S.X. and Y.L. (Yaqiong Lv); methodology, S.X., Y.L. (Yaqiong Lv) and Y.L. (Yifan Li); software, S.X.; validation, Y.L. (Yaqiong Lv) and Y.L. (Yifan Li); formal analysis, S.X. and L.Q.; investigation, S.X. and L.Q.; writing—original draft preparation, S.X.; writing—review and editing, Y.L. (Yifan Li) and Y.L. (Yaqiong Lv); visualization, S.X. and Y.L. (Yifan Li); supervision, Y.L. (Yaqiong Lv), Y.L. (Yifan Li) and L.Q.; funding acquisition, Y.L. (Yaqiong Lv) and Y.L. (Yifan Li). All authors have read and agreed to the published version of the manuscript.

Funding: This research was sponsored by the National Natural Science Foundation of China (Project No. 72101194) and the Hubei Provincial Natural Science Foundation of China (Project No. 20221j0065), and partially sponsored by the Humanities and Social Science Foundation of Ministry of Education of China (Project No. 20YJC630096) and the Independent Innovation Research Fund of Wuhan University of Technology (Project No. 2022IVA137), as well as the National Key R\&D Program of China (Project No. 2022YFE0125200) and the Natural Science Foundation of Shaanxi Province (Project No. 22020JM-187).

Conflicts of Interest: The authors declare no conflict of interest.
