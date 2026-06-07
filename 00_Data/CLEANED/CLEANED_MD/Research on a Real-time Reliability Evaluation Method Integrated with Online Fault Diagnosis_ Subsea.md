# Research on a Real-time Reliability Evaluation Method Integrated with Online Fault Diagnosis: Subsea All-electric Christmas Tree System as a Case Study 

Peng Liu - Dagang Shen - Jinfeng Cao*<br>Qingdao University of Technology, School of Mechanical and Automotive Engineering, China


#### Abstract

The subsea all-electric Christmas tree is key equipment in subsea production systems. If a failure occurs, the marine environment will be seriously polluted. Therefore, strict reliability analysis and measures to improve reliability must be performed before such equipment is launched, which is crucial to safe subsea production. A real-time reliability evaluation method for the all-electric Christmas tree mechanical system integrated with the static Bayesian network fault diagnosis stage is proposed in this paper, which realizes the identification of the fault type of the components and the real-time reliability evaluation of the mechanical system under different failure rates of the components. As a supplement to the method, by using mutual information to conduct sensitivity analysis on the reliability of the mechanical system, the importance of the basic events of each component on the reliability of the system is finally given. The proposed method provides significant theoretical support for the maintenance of the subsea all-electric Christmas tree and can be extended to the reliability evaluation of general subsea production systems.


Keywords: reliability analysis, Bayesian network, fault diagnosis

## Highlights

- This article contributes a real-time reliability evaluation method integrated with the online fault diagnosis stage by using dynamic Bayesian networks.
- The proposed method identifies component fault types and the real-time reliability evaluation of the mechanical system under different component failure rates in a marine environment.
- The problem of inaccurate evaluation results caused by only considering component degradation rate or using sensor data as a single piece of evidence has been overcome by using this method.
- The proposed method provides important theoretical support for the maintenance of the mechanical system of the all-electric Christmas tree and can be extended to the reliability evaluation of general subsea production systems.


## 0 INTRODUCTION

Process safety, risk analysis, and reliability evaluation have paramount significance in the modern process industries for preventing fatalities and loss of assets [1] and [2]. Even certified and tested equipment may experience problems during operation due to incorrect installation, operating environment, operator error, or lack of maintenance [3] and [4]. Furthermore, once installed, the subsea equipment must be transported back to the shore for maintenance and repair, which is time and resource consuming. The best way to avoid such large maintenance costs is to improve the reliability of subsea equipment by performing a reliability evaluation before launching the equipment. Moreover, a reliability evaluation can guide the maintenance of engineering staff.

Subsea all-electric Christmas trees (XTs) are critical pieces of equipment in subsea production systems [5] and [6]. They are the only viable method for oil and gas development that can be utilized in some areas. The ecosystem is fragile, and oil spills can have irreversible effects; therefore, very reliable and
safe subsea XT systems are required [7]. Indeed, safe and reliable subsea production systems will become increasingly important. The research on the reliability evaluation method of XT is paid increasing attention by scholars. In general, reliability evaluation methods of subsea XT can be divided into three categories: model-based, signal-based, and data-driven methods [8] to [11]. The model-based methods focus on building mathematical models of complex industrial systems, while the signal-based methods compare the detected signals with prior information obtained from normal industrial systems and use the detected signals to perform real-time online reliability evaluation [12]. However, for complex industrial and process systems, accurate mathematical models and signals are difficult to obtain, and the XT is a typical complex system. Data-driven methods that rely on historical data for reliability evaluation are particularly suitable for complex industrial systems.

Data-driven methods (e.g., Bayesian Network) have been shown to solve problems in complex systems, which has been used for reliability or risk analyses of XT systems or other subsea equipment

[13]. For example, Wang et al. quantitatively analysed the reliability and availability of a subsea tree system with different repair states using the dynamic Bayesian network (DBN). In addition, the influence of failure rates and degradation probability on reliability and availability has been analysed [14]. Li et al. [15] presented a risk-based accident model to conduct quantitative risk analysis (QRA) for leakage failure of submarine pipeline by using a Bayesian network. The model can provide a more case-specific and realistic analysis consequence compared to the bow-tie method, since it could consider the common cause failures and conditional dependency in the accident evolution process of pipeline leakage. Wang et al. presented an advanced two-step approach using Bayesian networks to analyse the failure probabilities of an urban buried gas pipeline. This novel approach could better reveal the relationships among failure causal factors and could also update the failure probabilities as operational and environmental conditions evolve [16]. Cai and Liu et al. [17] proposed a reliability and resilience evaluation method by combining the Markov model with a Bayesian network and used this method to conduct a risk analysis and reliability evaluation of the subsea oil and gas pipelines. Li et al. [18] proposed a method of quantitative assessment of the risk of gas explosion in an underground coal mine using a Bayesian network. This method overcomes the shortcomings of traditional methods in quantitative evaluation, dynamic control, and dealing with uncertainty. Lyu et al. proposed a Bayesian network model for series, parallel, and voting systems by considering common cause failure (CCF) and coverage factors. The model was used to evaluate the reliability of the subsea XT control system at any time, and the difference between posterior probability and prior probability of each component in the event of system failure was obtained. The effects of CCF and single-component failure rate on system reliability were studied [19]. Zhang et al. [20] used Bayesian networks to quantitatively evaluate the reliability of subsea production systems, including the subsea XT, in the early design stages.

Recently, there has been a growing interest in data-driven and model-based methods to understand and integrate both approaches in order to provide better diagnostic systems and reliability evaluation [21]. For example, Qian et al. [22] proposed a method of integrated extreme learning machine algorithm (data-driven algorithm) and model-based (fault model) for condition monitoring of the wind turbine gearbox. Zou et al. [23] proposed a novel data-driven stochastic manufacturing system model to describe
production dynamics, and a systematic method has been developed to identify the causes of permanent production loss in both deterministic and stochastic scenarios. The proposed methods integrate available sensor data with the knowledge of production system physical properties. Simani et al. [24] studied the fault diagnosis and continuous control of wind turbines based on data-driven and model-based robust strategies. Wang et al. [25] discussed feasible integration approaches for the model-driven and datadriven methods based on the existing achievements and proposed integrating both methods for the power system online frequency stability and reliability assessment.

The above-mentioned research has found that the Bayesian method is widely used to evaluate the safety, risk, and reliability of complex system and XTs. It is worth noting that the focus of these studies is to explore the impact of some traditional factors on system reliability, especially for real-time and static evaluation of system reliability. The basic research of these methods has greatly inspired our work; to the best of our knowledge, during the working process of XT, some local faults often occur, some are intermittent, and some are permanent. These faults usually have an important impact on the real-time reliability of XT. Therefore, the real-time reliability evaluation data of the system are different under different fault rate states of the components. To study the influence of the important factor of "fault" on system reliability, a real-time reliability evaluation method integrated with online diagnosis is proposed by using Bayesian networks, and the subsea allelectric XT mechanical system is used as a case study to verify the practicability of the method. Generally, methods of obtaining data include simulation, experimental testing, data reasoning, and expert data. In this paper, an XT testing system [10] is used to collect normal working signals and fault signals of the system. The abnormal signals of the pressure sensors are used to indicate the fault signals to obtain the components' fault information. According to the Weibull distribution law, the reliability change trend of the normal degradation process of the component is obtained. These data ultimately provide probability information for the Bayesian network.

The rest of the paper is organized as follows. Section 1 introduces the basic principles of Bayesian networks. Section 2 proposes the real-time reliability evaluation method integrated with online diagnosis. Section 3 provides a case study of subsea all-electric XT mechanical systems to demonstrate the application

of the proposed approach. Section 4 summarizes the work.

## 1 BASIC THEORY BRIEF DESCRIPTION 0 F BAYESIAN NETWORK

A Bayesian network is a data-driven reasoning method, which is widely used in the reliability evaluation and fault diagnosis analysis of complex systems. It is a graphical network that uses probabilistic reasoning and includes two parts: a qualitative part and a quantitative part. The qualitative part is represented by a directed acyclic graph, including system variable nodes and directed arcs indicating the causal relationships between the nodes. The quantitative part is the conditional probability tables between child and parent nodes.

According to the conditional independence and the chain rule, $P(U)$ represents the joint probability distribution of the variables $U=\left\{A_{1}, A_{2}, \ldots, A_{N}\right\}$, which can be represented as:

$$
P(U)=\prod_{i=1}^{N} P\left(A_{i} \mid P a\left(A_{i}\right)\right)
$$

where $P a\left(A_{i}\right)$ is the parent node of $A_{i}$.
If there is new evidence $E$, then the posterior probability of the variable can be calculated by the Bayesian formula, as follows:

$$
P(U \mid E)=\frac{P(E \mid U) P(U)}{P(E)}=\frac{P(E, U)}{\sum_{U} P(E, U)}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Structure of dynamic Bayesian network
A dynamic Bayesian network is the combination of a static Bayesian network and time information to
form a new random model with the processing of time series data. Each time step in the model is called a time slice. The basic structure of a dynamic Bayesian network is shown in Fig. 1. Where $t$ is the current time slice, $t+1$ represents the next time slice, $\Delta t$ is the interval of time slices, and dotted directed arcs show the relationship between variables in the same time slice, while solid line directed arcs represent that in different time slices. Similar to the static Bayesian network calculation method, the joint probability distribution of the dynamic Bayesian network can be calculated as follows:

$$
P\left(A_{t, T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{N} P\left(A_{t}^{i} \mid P a\left(A_{i}^{i}\right)\right)
$$

## 2 RESEARCH ON REAL-TIME RELIABILITY EVALUATION METHOD OF ALL-ELECTRIC CHRISTMAS TREE

### 2.1 Theoretical Model of Bayesian Network Reliability Evaluation for All-electric Christmas Tree

The theoretical model of the real-time reliability evaluation of the all-electric Christmas tree consists of two main phases: the fault diagnosis stage based on a static Bayesian network and the real-time reliability evaluation stage based on a dynamic Bayesian network, as shown in Fig. 2. In Fig. 1, both blue and red directed solid arcs indicate the causal relationship between nodes in different time slices. The blue arcs represent the degradation trend of the same component, and the red arcs represent the influence relationship between different components in different time slices. Since this study did not consider the influence and dependency relationships between different components, there are no directed arcs between different components in Fig. 2.

The static Bayesian network fault diagnosis phase consists of three layers: the additional information layer, the fault layer, and the fault symptom layer. $\mathrm{A}_{1}, A_{2}, \ldots, A_{n}$ are parent nodes in the additional information layer and also called additional information nodes, which represent the influence of subsea environment and operator experience on the probability of failure of all-electric XT mechanical components, such as corrosion degree, well fluid temperature, operating depth, repair frequency and so on. Child nodes $F_{1}, F_{2}, \ldots, F_{n}$ are located at the fault layer, called fault nodes, which represents the probability of failure of relevant components of the all-electric Christmas tree, such as the probability of valve clogging failure and leakage failure, etc., and

![img-1.jpeg](img-1.jpeg)

Fig. 2. Theoretical model of real-time reliability evaluation
each faulty node has a corresponding fault type. Child nodes $S_{1}, S_{2}, \ldots, S_{n}$ are located in the fault symptom layer, which are called the fault symptom nodes, and mainly from the data acquired by the sensor, such as the change of pressure value of pressure sensor is the most direct characterization of component failure. The supplementary data are the real data of the sensor when the fault occurs, and these data are re-entered into the fault symptom layer to improve fault diagnosis accuracy; the probability of failure of a certain component can be deduced reversely through the static Bayesian network eventually.

The dynamic Bayesian network reliability evaluation phase is composed of multiple time slices, and each time slice includes three layers: the additional information layer, the reliability component layer, and the reliability result layer. The additional information layer is the same as the static Bayesian fault diagnosis stage, and the above additional information not only affects the failure probability of the component but also affects the reliability probability of the component. During the evaluation phase, Child nodes $F_{1}, F_{2}, \ldots, F_{n}$ are located in the reliability component layer, which are the deformation of the fault nodes in the fault diagnosis stage, and for each node, the value is the complement of the fault diagnosis result in $[0,1]$. The child node $R(x)$ is located in the reliability result layer, and the reliability data in the current time slice of the component is obtained. In each time
slice, the reliability results are obtained based on the forward derivation of the Bayesian network. Multiple time slices constitute a dynamic Bayesian network evaluation model, and the arcs between the time slices connect the layers of reliability components located in different time slices and represent the trend of interchip transfer, indicating component reliability. The time interval between adjacent time slices is denoted by $\Delta t$, which can be 1 hour, 1 day, 1 month, etc.

Based on the theoretical model of real-time reliability evaluation, recording the sensor data at a specific moment, then bringing into the fault diagnosis stage of static Bayesian network, and the real-time component fault diagnosis results can be obtained by reverse derivation. The result is numerically transformed and input into the time slice $t$ of the dynamic Bayesian network reliability evaluation stage, and the influence of additional information is considered. The forward derivation of the Bayesian network in different time intervals is carried out to obtain the component reliability probability in corresponding time slice, and finally the relationship between time and component reliability is obtained.

Previously, the author's scientific research team and CNOOC Energy Development Co., Ltd. Shenzhen Oilfield Construction Branch jointly developed the XT test system to perform fault detection on the Christmas tree, as shown in Fig. 3 [26]. The test system is connected to the Christmas tree through

hydraulic lines and communication cables to complete valve operating condition detection, production loop detection, annulus loop detection, chemical injection loop detection, and acquires sensor data in real time, as shown in Fig. 4.

In the conditional probability table, the increase in the number of parameters will lead to an exponential increase in the amount of calculation; therefore, the Noisy-OR and Noisy-MAX models are used to determine the conditional probability table. The conditional probability table can be calculated simply and quickly by using Noisy-OR when a node has two states. For the Noisy-OR model, $Y$ is considered to be the result of different causal variables, such as
$X_{1}, X_{2}, \ldots, X_{n}$, and these causal variables are considered to be Boolean values: only "true" and "false" status. A conditional probability table including n parameters (e.g., $q_{1}, q_{2}, \ldots, q_{n}$ ) can be determined with the NoisyOR model. The formula for calculating the conditional probability of a parent node being 1 is as follows [27] and [28]:

$$
P\left(Y=1 \mid X_{1}, X_{2}, \ldots, \mathrm{X}_{n}\right)=1-\prod_{i=1}^{n} q_{i}
$$

Q here $q_{i}$ is the probability that $Y$ is false when $X_{i}$ is assumed to be true, and all other parent nodes are false.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Subsea Christmas tree testing system
![img-3.jpeg](img-3.jpeg)

Fig. 4. Sensor data acquisition

If there are more than two states in a node, for example, the sensor data includes "high", "low", and "normal" states, which represent high pressure, low pressure, and normal pressure, respectively. It can be calculated simply with the Noisy-MAX model in the conditional probability table. Similarly, $Y$ is considered to be the result of different causal variables; these cause variables such as $x_{1}, x_{2}, \ldots, x_{n}$, but these causal variables are not Booleans. The calculation formula of the conditional probability table is as follows [28]:

$$
P(Y \leq y \mid X)=\prod_{\substack{i=1 \\ x_{i} \neq 0}}^{n} \sum_{i, i_{i}}^{X} q_{i, y}^{x_{i}}
$$

$P(Y=y \mid X)=$

$$
\left\{\begin{array}{cc}
P(Y \leq 0 \mid X) & \text { if } y=0 \\
P(Y \leq \mathrm{y} \mid \mathrm{X})-P(Y \leq \mathrm{y}-1 \mid \mathrm{X}) & \text { if } y>0
\end{array}\right.
$$

where $X=x_{1}, x_{2}, \ldots, x_{n}$, and $y$ is specific condition boundary.

### 2.2 Fault Diagnosis Stage Based on Static Bayesian Network

The cumulative number of various fault symptoms at different intervals such as 1,000 hours or 2,000 hours can be recorded by using the XT test system; the symptom data corresponding to these faults are then input into the fault symptom layer. Fault diagnosis is carried out by reverse derivation of static Bayesian network; the diagnosis result of the fault diagnosis method does not clearly indicate that the fault must occur, but it provides the failure probability of the component to guide the maintenance [28]. Generally, the greater the probability of failure, the greater the likelihood of failure of the corresponding component. However, there is a kind of failure. When the failure occurs, it will not cause huge economic losses or casualties but will only cause < temporary reduction in production or the XT cannot work normally. In this paper, the type of failure is defined as safety failure of the mechanical component (hereinafter: safety failure). For example, when the control signals of the surface control subsea safety valve (SCSSV), production main valve (PMV), and production wing valve (PWV) are lost, the valve cannot be closed. However, such failures can usually be resolved by restarting the subsea control module (SCM) without causing great economic losses. The priority of fault maintenance can be determined by taking different measures to deal with safety failure. Combined with the experience of engineers, three judgment rules are
defined to determine the diagnosis result, and some engineers applied similar judgment rules to the fault diagnosis of deep-water blowout preventer (BOP) systems [10].

Rule 1: If the type of failure is not a safety failure, when the difference between the posterior probability and the prior probability of the failed node is $\geq 60 \%$, the failure will be reported.

Rule 2: If the type of failure is not a safety failure, a warning will be issued when the difference between the posterior probability and the prior probability of the fault node is $\geq 30 \%$ and $\leq 60 \%$.

Rule 3: If the failure type is a safety failure, then when the difference between the posterior probability and the prior probability of the fault node is $\geq 80 \%$, an early warning will be issued.

For the convenience of analysis, the mechanical system of the all-electric XT is symbolized, as shown in Fig. 5. Its working principle is described as follows: under normal operating conditions, SCSSV continuously transports crude oil from the wellhead to the oil storage device through the production loop, and PMV, PWV, PCV (production control valve) and PIV (production isolation valve) all remain open in this case; once a problem occurs in the production loop, the signals of the corresponding sensors (such as PS11, PS12 and FS11) will change, and the signal of the sensor is used to determine whether crossover valve (XOV) needs to be turned on. If XOV is opened, the annulus loop is connected, and AMV is put into operation. At the same time, the valve of the chemical injection loop is always kept open, and the chemical is injected into the production loop.

Using Netica software [29] for Bayesian network modelling and analysis, the nodes of the additional information layer are determined as the parent nodes of the fault nodes, and each parent node has two states (i.e., a high state and a low state), indicating the degree of reasoning of the corresponding additional information. Under the influence of additional information nodes, fault diagnosis is made for the components of the system. The failure layer includes 12 nodes, which represent the failure probability of 12 components (surface control subsea safety valve (SCSSV), PMV, PWV, chemical injection valve 2 (CIV2), XOV, annular main valve (AMV), PCV, PIV, chemical injection valve 2 (CIV1), AMV (annular main valve), AAV (annulus access valve), and MIV (methanol injection valve)).

To make the analysis convenient, the components are divided into five categories according to the structure, function, and parameters of the main components of the all-electric XT. The relationship

![img-4.jpeg](img-4.jpeg)

Fig. 5. Symbolic representation of subsea all-electric XT machine system
and classification between the additional information node and the fault node are shown in Table 1. For example, "SCSSV_Failure" indicates the SCSSV fault node, "Present" indicates the probability of failure of the corresponding component of the node, and "Absent" indicates the probability of no failure.

The conditional probability tables of the additional information nodes and the fault nodes can be calculated by using the Noisy-OR model of Eq. (4) and establishing a Bayesian network of the relationship between the additional information
layer and the fault layer, as shown in Fig. 6. In the initial state, the high and low state probabilities of all additional information nodes are set to $99 \%$ and $1 \%$, respectively, and the "Absent" state probability and "Present" state probability of the fault node can be derived.

In the XT mechanical system, SCSSV, PMV, PWV, AMV and XOV are the most critical components; therefore, it is very important to guide the repair and maintenance of the XT by focusing on distinguishing the types of faults during the fault

Table 1. The relationship and classification between additional information node and the fault node


![img-5.jpeg](img-5.jpeg)

Fig. 6. Bayesian network of additional information and fault layer
![img-6.jpeg](img-6.jpeg)

Fig. 7. Fault nodes replacement
![img-7.jpeg](img-7.jpeg)

Fig. 8. Static Bayesian network fault diagnosis phase model of subsea all-electric XT
shown in Fig. 7 (Netica software figure). Based on the reverse derivation of the static Bayesian network fault diagnosis stage, the fault types of the five key components can be discriminated, according to the judgment rules to report the corresponding message. The relationship between the replaced and replaced nodes is shown in [10].

The fault diagnosis model of the all-electric XT established based on the static Bayesian network is shown in Fig. 8, the fault symptom layer includes 13 nodes (DHPT, PS11, PS12, PS13, PS14, PS21, PS22, FS11, FS12, FS21, FS22, FS31, FS32), representing the corresponding sensor data, and each node has three states, namely "normal", "high" and "low". The sensor value below $10 \%$ of the normal value is in a "low" state, while $10 \%$ above the normal value is in a "high" state. Because each fault symptom node has three states, the Nosiy-MAX model can be used to calculate the conditional probability tables of the fault node and the fault symptom node, as shown in Eqs. (5) and (6). Due to system uncertainties in the static Bayesian network fault diagnosis model, such as the detection accuracy and measurement error of the

sensor, the "Absent" state of all fault nodes is set to 99 $\%$ instead of $100 \%$ in the initial state [30].

### 2.3 Reliability Evaluation Stage Based on Dynamic Bayesian Network

The real-time reliability evaluation of the dynamic Bayesian network is carried out on the basis of the fault diagnosis of the static Bayesian network, and the evaluation model is still modelled using Netica software. The model of the dynamic Bayesian network evaluation stage is shown in Fig. 9. Each time slice Time $t$ is expanded to four layers: additional information layer, component reliability layer, loop reliability layer and Christmas tree reliability layer.

The additional information layer consists of four nodes and is consistent with the fault diagnosis stage of a static Bayesian network. The component reliability layer is the deformation of the fault node in the fault diagnosis stage and includes 12 nodes. The loop reliability layer includes three nodes: PL_R, $\mathrm{AL} \_\mathrm{R}$ and $\mathrm{CL} \_\mathrm{R}$. The XT reliability layer has only one XT reliability node $\mathrm{XT} \_\mathrm{R}$.

In the stage of reliability evaluation based on dynamic Bayesian networks, the state of the node "Re" indicates the reliability probability of the component, "Fa" means the failure rate of the component, and in the initial state, set the "Re" of all component reliability nodes to $100 \%$. All-electric Christmas tree components comply with the life
![img-8.jpeg](img-8.jpeg)

Fig. 9. Dynamic Bayesian network reliability evaluation phase model of subsea all-electric XT

![img-9.jpeg](img-9.jpeg)

Fig. 10. Real-time reliability evaluation model of subsea all-electric XT

cycle law of general electronic control components; therefore, the life cycle of each component conforms to the Weibull distribution; the probability distribution of the life cycle is shown in the following Eq. (7). The proportional parameters $\theta=6800$, and shape parameters $\beta=2.3$ [31] to [33].

$$
f(x ; \theta, \beta)=\left\{\begin{array}{cc}
\beta \theta\left(\frac{x}{\theta}\right)^{\beta-1} e^{-(x-\theta)^{\theta}} & x \geq 0 \\
0 & x \leq 0
\end{array}\right.
$$

In the reliability evaluation stage, the three loops of the all-electric XT belong to a series relationship, meaning that if any loop fails, the mechanical system fails. Therefore, the conditional probability tables of the nodes of the loop reliability layer and the Christmas tree reliability layer can be obtained, as shown in Table 2.

Table 2. CPT for the nodes of the circuit reliability layer and the tree reliability layer


![img-10.jpeg](img-10.jpeg)

Fig. 11. Bayesian network of circuit reliability layer and tree reliability layer

The real-time reliability evaluation model of the all-electric XT is shown in Fig. 10. First, the sensor state of the fault symptom layer nodes in the fault diagnosis stage of the static Bayesian network is used to deduce the nodes state of the fault layer in reverse and to obtain component failure rate (probability of "Present"), and whether the component fails is determined by the above judgment rule. Second, the complement of the failure rate of the faulty component is calculated and transformed into the reliability probability of the component and then substituted into the reliability probability of the corresponding node in the component reliability layer of the dynamic Bayesian reliability evaluation stage (probability of "Re"). The reliability probability of the specified time slice interval $\Delta t$ can be obtained by using dynamic Bayesian network forward derivation.

The probability relationships in Table 3 are substituted into the loop reliability layer and the Christmas tree reliability layer, as shown in Fig. 11. Fig. 11a shows that when the Re probability of the PL_R node, AL_R node and CL_R node are all 100 $\%$, the reliability of the Christmas tree reliability node (XT_R) is $100 \%$. As shown in Fig. 11b, the reliability probability of any node PL_R, AL_R and CL_R is 0 , meaning that when the probability of Fa is $100 \%$, the Christmas tree mechanical system will fail, meaning that the probability of Fa of XT_R node is $100 \%$. The reliability probability of the current time slice of the all-electric Christmas tree mechanical system can be derived forwardly through the Bayesian network by obtaining the reliability probability of the three loops, as shown in Fig. 11c.

## 3 RESEARCH ON REAL-TIME RELIABILITY OF DYNAMIC BAYESIAN NETWORK FOR ALL-ELECTRIC CHRISTMAS TREE

### 3.1 Verification of Bayesian network model of All-electric Christmas tree

Model verification is an important part of fault diagnosis and reliability analysis. In the static Bayesian network fault diagnosis stage, the Christmas tree test system is used to collect sensor data and determine whether the component has failed, as shown in Fig. 4, and can be compared with fault diagnosis results. The correctness of the fault diagnosis method is verified based on three examples [10], as follows:
(1) When the fault symptom nodes DHPT, PS11, PS12, and PS13 are high, low, low, and low, respectively, the remaining nodes are normal, and SCSSV has safety failure, the fault diagnosis result

is the "SFailure" state probability of SCSSV $>80 \%$, which is consistent with the actual result.
(2) When the fault symptom nodes DHPT, PS11, PS21, PS22, and FS22 are low, high, high, low and low, respectively, the remaining nodes are normal, and AMV has leakage fault, the fault diagnosis result is the "Leakage" state probability of AMV $>60 \%$. Generally, when the failure probability is greater than $50 \%$, it indicates that the component has a high risk of fault and should be shut down for maintenance. Therefore, it can be considered that the BN (Bayesian network)-based fault diagnosis method diagnoses that the AMV leakage fault probability is greater than 60 $\%$ is consistent with the actual result.
(3) When the fault symptom nodes PS13, PS14, FS11 and, FS32 are low, high, low and high, respectively, and CIV1 failed (the component does not consider safety failure), the fault diagnosis result is the "Present" state probability of CIV1 $>90 \%$, which is consistent with the actual result.

It is impractical to fully verify the results of the life cycle reliability evaluation of the all-electric XT mechanical system, but Jones et al. proposed a three-axiom-based validation method for reliability evaluation method verification [34]:

Axiom 1. A slight increase/decrease in the prior subjective probabilities of each parent node should certainly result in the effect of a relative increase/ decrease of the posterior probabilities of the child node.

Axiom 2. Given the variation of subjective probability distributions of each parent node, its influence magnitude to the child node values should keep consistency.

Axiom 3. The total influence magnitudes of the combination of the probability variations from x attributes (evidence) on the values should always be greater than the one from the set of $x-y(y \in x)$ attributes (sub-evidence).

In the initial state, the "Re" state prior probability of the 12 component reliability nodes are all set to 60 $\%$, then the "Re" of the 12 components are increased to $100 \%$ in sequence, and finally the "Re" of the XT_R node are increased in sequence; combined with the three cases in Fig. 12, the Bayesian reliability evaluation model is shown to conform to the Three-axiom-based validation method.

### 3.2 Real-time Reliability Evaluation of All-electric XT

The value of the time slice interval $\Delta t$ can be any period when no fault occurs, $\Delta t$ takes $200 \mathrm{~h}, 400$ $\mathrm{h}, 600 \mathrm{~h}, 800 \mathrm{~h}$ and 1000 h , etc. The trend of the
time slice interval and the reliability of the mechanical system is shown in Fig. 12.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Effect of $\Delta t$ on the tree reliability
It can be seen from the figure that the time slice interval has little effect on the reliability evaluation of the XT mechanical system; regardless of the value of the time slice interval, the reliability of the mechanical system will eventually become consistent, the reliability of the XT drops rapidly to around 0.958 , and then shows a slow downward trend only due to the impact of the additional information layer on the reliability of the mechanical system, and the trend is consistent with the Weibull distribution of the life cycle of the XT. Theoretically, if $\Delta t$ is reduced by one time, the reliability data points will be doubled. The more data points there are, the more accurate the degradation trend will be depicted. As the degradation curve is fitted by a computer according to the data points, and the number of data points is limited during the 20-year service life of the XT. Therefore, for computers, the impact of increasing limited data points on time costs is not obvious. In other words, the time cost is acceptable. However, the degradation trend of XT reliability is relatively slow, and the degradation trend is not obvious in a short time, so the time slice should be appropriately larger.

The larger the value of the time slice, the better in reducing time cost (although the time cost is acceptable). However, it can be inferred from Fig. 12 that if the value of $\Delta t$ is too large, the reliability probability point will be lost. If $\Delta t$ is 2000 h , then data points less than 2000 h will be lost. Therefore, the larger the $\Delta t$, the lower the resolution of the obtained reliability degradation curve. If $\Delta t$ is 10000 h , the obtained reliability curve will become a straight line in Fig. 12. In summary, considering that it can fully describe the degradation trend of system reliability

and the slowness of system degradation in a short period, $\Delta t$ is taken 1000 h in the analysis of this paper.

Evaluating the reliability of the all-electric Christmas tree mechanical system by using the three examples in the previous section, and based on the static Bayesian network fault diagnosis stage, the fault probability of three cases is reversely deduced, as shown in Table 3. The reliability probabilities of a component can be obtained by calculating the complement of component failure probabilities and then substituted into the corresponding node of the dynamic Bayesian network reliability evaluation stage. For example, case 1 in the table, the "Present" probability of the node "PMV_Failure" is 0.0933 , which indicates that the reliability probability is 0.9067 , then it is replaced to the " Re " state of the node "PMV_R" in the Bayesian network time slice Time t of the reliability evaluation stage, and the forward derivation of reliability is carried out after successive substitution.

Table 3. Fault diagnosis results of the three cases


In the state of case 1, the reliability curve of the mechanical system is obtained, as shown in Fig. 13. It is worth noting that in this case, as mentioned above, despite the fault diagnosis result is the "Sfailure" state probability of SCSSV $>80 \%$, but safety failure is not real failure (need to transfer the XT to land for repair). Safety failure is a temporary failure behaviour; for example, the system crashes due to signal interference. After the interference disappears, the problem can be solved by restarting the system without transferring the XT to land for repair. So it is a self-healing fault. The real failure rate of SCSSV is only 0.1384 , as shown in Table 3, which shows that the component still has high reliability, which effectively prevents misjudgement
of the fault and avoids the cost of salvage maintenance and detection. Time in the figures represents the time when the failure probability is input into the dynamic Bayesian network; for example, Time $=$ 200 h means that the reverse derivation of the fault diagnosis stage is performed at 200 h . It can be seen from the "no fault" curve that the safety failure of SCSSV has a certain impact on the reliability of the mechanical system, which will cause the reliability of the mechanical system to decrease slowly. When the reliability of the mechanical system drops to 95 $\%$ after continuous working for 5000 hours, adequate attention should be paid to safety failure to prevent the failure of the mechanical system. However, if a safety failure occurs, it is detected after 800 hours of system operation (the curve of Time $=800 \mathrm{~h}$ ); at this time, the safety failure has a greater impact on the reliability of the mechanical system, and if it continues to work, the reliability of the mechanical system will decline rapidly. In summary, the time when the safety failure is detected has a greater impact on the reliability evaluation results of the mechanical system. In addition, it can be seen from the figure that when the mechanical system continues to work for 8000 h , the system reliability presents a rapid decline, and the decline rate is significantly greater than the decline rate of the previous 8000 h . Therefore, when the mechanical system works normally for 8000 h , it is necessary to shut it down for maintenance in order to ensure the stable operation of the system.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Reliability evaluation results of machine system-case 1
In the state of case 2, when the failure probability of AMV is detected as high as $85.61 \%$, the reliability of the mechanical system is evaluated, as shown in Fig. 14. Due to AMV failure, the reliability of mechanical system decreases rapidly; at any values of Time ( $200 \mathrm{~h}, 400 \mathrm{~h}, 600 \mathrm{~h}, 800 \mathrm{~h}$ ), the mechanical

system reliability is less than $10 \%$, which shows that the failure probability of AMV components has an important impact on the reliability of mechanical systems.
![img-13.jpeg](img-13.jpeg)

Fig. 14. Reliability evaluation results of machine system-case 2
![img-14.jpeg](img-14.jpeg)

Fig. 15. Reliability evaluation results of machine system-case 3

In the state of case 3, when the failure probability of CIV1 is detected to be $94.11 \%$, the reliability of the mechanical system is evaluated, as shown in Fig. 15. Failure of CIV1 can also cause mechanical system reliability to drop below $10 \%$; however, the downward trend is significantly less than the impact of AMV on the reliability of mechanical systems. CIV1 is located in the chemical injection loop, and AMV is located in the annulus loop, indicating that the components on the annulus loop have a more obvious influence on the reliability of the mechanical system. In cases 2 and 3 , it can be found that if the failure rate of a certain component of the system is too high, the reliability will quickly drop to an extremely low value after the system works for 8000 h . To summarize, whether the system components are malfunctioning or not, 8000 h
of continuous system operation is the recommended limit value and should be shut down for maintenance.

### 3.3 Sensitivity Analysis of All-electric XT

The influence of components on the reliability of the mechanical system is studied by sensitivity analysis, mutual information can be used to analyse the reliability and sensitivity of the XT mechanical system, and mutual information is used to indicate the relationship between two basic events, the reliability of 12 components are considered as 12 basic events, and the reliability of a mechanical system is considered as a basic event, and the mutual information about the reliability of component basic events and mechanical system basic events are calculated in sequence [35]; the calculation formula is as follows:

$$
I(X ; Y)=\sum_{x \in X} \sum_{x \in Y} P(x, y) \log \frac{P(x, y)}{P(x) P(y)}
$$

where $X$ and $Y$ represent two basic events, $P(x, y)$ is the joint probability distribution function of $X$ and $Y$, $P(x)$ and $P(y)$ are the edge probability distribution functions of $X$ and $Y$, respectively. Figs. 16 and 17 are the mutual information values of the reliability of each component and the reliability of the mechanical system for 5,000 hours and 10,000 hours of operation of the mechanical system, respectively.

It can be seen from Fig. 16 that when the mechanical system works for 5000 hours, the SCSSV, PMV, PWV, PCV and PIV components in the production loop have a great influence on the reliability of the mechanical system, SCSSV, PMV, PWV, PCV and PIV components in the production loop have a greater impact on the reliability of the mechanical system, followed by AMV, AWV and AAV components in the annulus loop, and MIV, CIV1 and CIV2 components in the chemical agent injection loop have less impact. The components in the production loop and the annulus loop affect the reliability of the mechanical system by several orders of magnitude higher than the components in the chemical injection loop on the reliability of the mechanical system. Therefore, the reliability of the two-loop components should be guaranteed first. Fig. 17 shows that the mechanical system has the same rule when it works for 10,000 hours; however, with the increase of working time, the mutual information value of the influence of production loop components on the reliability of the mechanical system is increased to more than 0.04239 , while the mutual information value of the influence of the chemical injection loop components on the

reliability of the mechanical system is reduced to below 0.000104 , which indicates that the longer the working time of the mechanical system, the greater the influence of the components on the production loop on the reliability of the mechanical system, More attention should be paid to prevent failures from occurring, so as to avoid major safety accidents.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Mutual information value of components reliability and machine reliability ( 5000 h )
![img-16.jpeg](img-16.jpeg)

Fig. 17. Mutual information value of components reliability and machine reliability ( 10000 h )

## 4 CONCLUSION

A real-time reliability evaluation method of an allelectric XT mechanical system incorporating static Bayesian network fault diagnosis stage was proposed in this article. The reliability evaluation model was established, and the influence of the type of failure and component failure rate on the reliability evaluation results under the condition of additional information was studied. The sensitivity of mechanical system reliability was analysed by using mutual information, and the importance of the basic events of each
component on the reliability of the mechanical system was revealed. The following conclusions were obtained:

1) The time slice interval had little effect on the reliability evaluation of the XT mechanical system; regardless of the time slice interval, the reliability trend of the mechanical system was basically the same.
2) Safety failure had a certain impact on the reliability of the mechanical system, which would cause the reliability of the mechanical system to decrease slowly. After 5,000 hours of continuous operation, the reliability of mechanical system was reduced to $95 \%$. However, the time at which the safety failure was detected had a greater impact on the reliability evaluation results of the mechanical system; therefore, it was recommended to use this method to identify, diagnose and real-time reliability assessment of mechanical system faults every $1,000 \mathrm{~h}$.
3) The failure probability of components on the annulus loop included AMV components had a significant impact on the reliability of the mechanical system. If the failure rate of any component were large, it would quickly reduce the reliability of the mechanical system. However, the failure rate of components in the chemical injection loop had less influence on the reliability of the mechanical system.
4) It could be seen from the sensitivity analysis that the longer the working time of the system was, the higher the influence degree of components in the production loop on the system reliability was, while the influence degree of components in the chemical injection loop was lower. Therefore, the failure probability of components in the production loop should be paid more attention during long-term work.

## 5 ACKNOWLEDGEMENTS

The authors wish to acknowledge the financial support of Shandong Provincial Natural Science Foundation, China (ZR2021QE059), Key R\&D Program of Shandong Province (2019GGX101020).
