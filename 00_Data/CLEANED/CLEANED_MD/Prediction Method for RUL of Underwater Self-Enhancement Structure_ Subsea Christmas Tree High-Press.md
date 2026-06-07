# Article 

## Prediction Method for RUL of Underwater Self-Enhancement Structure: Subsea Christmas Tree High-Pressure Valve Actuator as a Case Study

Peng Liu ${ }^{1,2}$ (D) Chen Dai ${ }^{1}$, Shuo Zhao ${ }^{1}$, Shuaiqiang $\mathrm{Li}^{1}$, Bilong Liu ${ }^{1}$ and Guijie Liu ${ }^{3, *}$


#### Abstract

check for updates Citation: Liu, P.; Dai, C.; Zhao, S.; Li, S.; Liu, B.; Liu, G. Prediction Method for RUL of Underwater Self-Enhancement Structure: Subsea Christmas Tree High-Pressure Valve Actuator as a Case Study. J. Mar. Sci. Eng. 2023, 11, 1065. https://doi.org/ 10.3390/jmse11051065

Academic Editor: José António Correia

Received: 24 April 2023
Revised: 9 May 2023
Accepted: 16 May 2023
Published: 17 May 2023


## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Mechanical and Automotive Engineering, Qingdao University of Technology, Qingdao 266525, China; peng_liu@qut.edu.cn (P.L.); chendai1126@163.com (C.D.); shuofengz@163.com (S.Z.); shuaiqiangli1222@126.com (S.L.); liubilong@qut.edu.cn (B.L.)
2 Key Lab of Industrial Fluid Energy Conservation and Pollution Control (Qingdao University of Technology), Ministry of Education, Qingdao 266520, China
3 Shandong Provincial Key Laboratory of Ocean Engineering, Qingdao 266100, China

* Correspondence: blue_ocean2023@126.com or liuguijie@ouc.edu.cn; Tel.: +86-15192095309


#### Abstract

Underwater pressure-bearing structures are produced in practice by means of pressure self-enhancement methods in order to improve the stress distribution and enhance the pressurebearing performance. On the other hand, the pairs equation shows that stress is an important factor influencing the degradation of the structure. In fact, improving the stress distribution will not only improve the pressure-bearing performance, but will have an impact on the life degradation trend. Thus, pressure self-enhancement affects the structural life by changing the stress distribution. With this in mind, this paper considers the effect of pressure self-enhancement on the service time of subsea structures, and a Bayesian network (BN)-based method that can be used to predict the remaining useful life (RUL) of underwater self-enhanced structures is proposed. The method also takes into account the influence of multiple sources of structural factors in order to predict the RUL of the structure more accurately. The life degradation process of an all-electric Christmas tree valve actuator is used as a case study. The prediction results are compared with data in the literature to verify the validity of the method. The results have implications for guidance on the O\&M assurance of underwater production systems.


Keywords: pressure self-enhancement; RUL; dynamic Bayesian networks; valve actuators; crack extension

## 1. Introduction

All-electric Christmas tree valve actuators need to serve in deepwater and complex environments for 20 years, but work processes, including vibration, corrosion, wear, fatigue, temperature changes and other factors, very easily cause small cracks early on; the cracks that develop, to a certain extent, lead to structural damage to the body and can cause major oil spill accidents [1]. This causes great potential harm to the offshore environment, to national defense, to maritime traffic and to fishery resources [2]. Therefore, extending the life of all-electric Christmas tree valve actuators, accurately predicting their crack extension pattern and assessing the RUL are essential in order to ensure the safe operation of all-electric valve actuators.

For underwater pressurised structures, the use of pressure self-enhancement measures in the manufacturing process can effectively increase the initial yield strength of the inner wall of the pressurised structure; this results in a certain amount of plastic deformation in the inner wall and the formation of a plastic layer of a certain thickness, while the rest of the structure remains in an elastic state [3]. After a period of pressure holding and decompression, due to the elastic contraction of the outer material of the valve body,

the inner material, which has been plastically deformed, is compressed by the elastic compression of the outer layer due to the elastic contraction of the outer material of the valve body, and the outer material produces tensile stresses. In this process, the inner wall of the valve body is plasticised, but due to the strict control of the overstrain and residual stress after decompression, the valve body is still in the elastic range during operation. For the pressure-bearing structure treated with self-enhancing technology, in the actual working process, the internal working pressure of the pipeline medium causes a large tensile stress on the inner wall of the valve body, which is offset by the residual compressive stress. In addition, the total stress value on the inner wall is reduced, while the compressive stress on the outer wall of the valve body is superimposed with the residual tensile stress when working, and the total stress value on the outer wall is increased. As a result, the difference in the stress level between the inner and outer walls of the valve body is reduced and the stresses are more evenly distributed in the direction of the valve body wall thickness, which can effectively improve the service life. On the other hand, the change in the stress and wall thickness of the structural system caused by pressure self-enhancement may directly affect the results of the RUL, so there is a need to investigate the method of predicting the RUL after pressure self-enhancement.

There are two main categories of methods used to predict the RUL of structural systems or components, namely physical model-based and data-driven methods [4]. The RUL of structures has been extensively studied by academics both nationally and internationally. For example, Eleftheroglou et al. [5] proposed a new framework by which to fuse structural health monitoring data from different in situ monitoring techniques to develop a hyper-feature and thus achieve more effective prognostics. A non-flush hidden semiMarkov model was used to simulate the accumulation of damage in composite structures under fatigue loading and to estimate the RUL using conventional, as well as fused, SHM data. The validity of the method was verified using open-cell carbon/epoxy specimens subjected to fatigue loading as an example. Morita et al. [6] investigated a method for the prediction of the fatigue crack initiation life under variable loading conditions based on the Fatigue SS Model. Barraza-Barraza et al. [7] constructed three autoregressive models with exogenous variables and evaluated their capability to estimate the RUL of the process; this was evaluated following the case of the aluminium crack extension problem. Corbetta et al. [8] proposed a particle filter-based Bayesian framework for crack damage prediction in composite laminates; the proposed prediction prognostic successfully predicted the crack damage growth and fatigue life of laminates, and discussed the filtered estimation of crack damage progression and remaining life prediction. Zhenhua Gu [9] presented a fatigue crack extension prediction and RUL prediction method based on an improved particle filtering algorithm using BAS optimisation. Using Q235 steel as the research object, the practicality and prediction accuracy of the method was verified. In addition, some researchers combined the two prediction methods and used a data-driven approach to collect data from physical models. For example, Cai et al. [10] contributed a hybrid physics-model-based and data-driven RUL estimation methodology for structure systems by using dynamic Bayesian networks (DBNs). Subsea pipelines in offshore oil and gas subsea production systems were adopted in order to demonstrate the proposed methodology. Li et al. [11] adopted a methodology typically applied in sensor fault diagnosis and developed a new hybrid prognostic model, with a bias parameter included in the measurement equation and the state vector. Using particle filtering as an estimation technique for the damage state, damage parameter and damage bias parameter, the experimental study of an aluminium lug structure subjected to fatigue crack growth and equipped with a Lamb wave monitoring system demonstrated the improved estimation and prediction performance of the new prognostic model. Although scholars at home and abroad have conducted extensive research on methods that can be used to predicting the RUL of structures, most of them are analytical studies that focus on predicting the RUL of structural materials on land [12]. There is a relative lack of research that focuses on predicting the RUL of

underwater structures, and the effect of changes in the stress distribution on the service life has not yet been considered.

Underwater structural systems are hardware systems that are closely related to the principles of structural mechanics [10]. Due to the complexity of structural systems, the factors that cause damage to structural elements are also diverse. For example, pressurebearing structural members in all-electric actuators in deep water are subject to a variety of factors, such as fatigue degradation and seawater corrosion [13], making the construction of physical models of structural systems under the influence of multiple factors very difficult.

BNs are currently one of the most effective theoretical models in the field of uncertain knowledge representation and inference. DBNs have been used for many years in the field of fault diagnosis and the lifetime prediction of structural systems [14]. Arzaghi et al. [15] proposed a probabilistic approach based on DBNs to construct an integrated model of the fatigue degradation of subsea pipelines caused by pitting and corrosion, and applied the method to estimate the RUL of high-strength steel pipelines. A hybrid multi-stage control system RUL prediction method was proposed by Liu et al. [16]. Taking the electro-hydraulic compound control of an underwater oil production tree as an example, the method was used to analyse the uncertainty in the prediction process of the Kalman filter and the RUL of a non-linear degraded system using a DBN. This method could improve the accuracy of RUL prediction and increase the robustness of the prediction model. A fracture mechanics-based fatigue reliability analysis of a submarine pipeline was investigated using the Bayesian approach by Kakaie et al. [17], and the proposed framework enabled the estimation of the reliability level of submarine pipelines based on limited experimental data. The failure load cycle distribution and the reliability-based performance assessment of API 5L X56 submarine pipelines, as a case study, were estimated for three different cases. Based on the Bayesian Regularization Artificial Neuron Network, Li et al. [18] proposed an efficient probability approach that could be used to predict the fatigue failure probability of the subsea wellhead system during its entire life. This paper takes full advantage of Bayesian inference in order to establish the causal relationship between pressure self-enhancing parameters and the structural life, and to predict the RUL of structures under complex multi-factorial underwater conditions.

The remainder of the paper is structured as follows: Section 2 details the proposed method for predicting the remaining life of self-enhanced structural components; Section 3 develops a physical model for predicting the remaining life of self-enhanced structural components using the subsea oil recovery tree valve actuator as an example; Section 4 constructs a Bayesian RUL prediction model based on the physical model; Section 5 presents the prediction results and analysis; and Section 6 is the conclusion.

# 2. Proposed Pressure Self-Enhancement and Life Prediction Method 

### 2.1. Modeling Methodology

This paper proposes a DBN-based method for predicting the RUL of pressure selfenhanced structures. The method uses a DBN to establish the relationship between the life, the influence of stress and the wall thickness of the self-enhanced structural system, which can predict the degradation process of the structural system under the influence of multiple source factors and give the RUL of the structural system more accurately. The proposed method consists of two phases: (i) A DBN-based modelling phase for the stress enhancement and life extension of compressional self-enhanced stresses. (ii) A dynamic prediction phase for the RUL under the influence of multiple source factors based on DBNs. This is illustrated in Figure 1.
(i) This phase is a DBN consisting of multiple time slices, named the structure parameter network. The structure parameter network i $(i=1,2, \ldots t)$ includes three layers of nodes: structure parameter nodes, self-enhancement excessive parameter nodes and self-enhancement parameter nodes. Structure parameter nodes are the directly relevant parameters that affect the life of a structural system, such as the material, mechanical properties, operating conditions, design criteria, etc. These parameters

must be followed in the design of the structural system, in other words, they must meet the relevant design requirements. The self-enhancement parameter nodes indicate the parameters used for the self-enhancement optimisation of a structure; these include the use of prestressing to improve the stress distribution in the structure, thereby increasing the compressive strength, optimising the thickness of the structure and increasing the service life. Alternatively, coatings can be used to improve the corrosion resistance of the structure, which can also slow down the degradation of the system. Both "pressure self-enhancement" and "coatings" are factors in the self-enhancement of excessive parameter nodes. In other words, it is the measure that can extend the service life. The optimised stress distribution and the improved corrosion protection factor are the self-enhancement parameter nodes. This paper proposes a DBN-based pressure self-enhancement method to investigate the causal relationship between the above three layers of nodes and to obtain an improved stress distribution.
(ii) This phase consists of two layers of BNs: the first layer comprises the parameters of the multi-source external factors that affect the life of the structural system, which are dynamically modified by simultaneous self-enhancement and therefore have a causal relationship with phase (i). The second layer comprises the nodes of the parameters that characterise the lifetime of the structural system, such as the wall thickness, which decreases due to wear, corrosion, cracking, etc. The change in the wall thickness can represent the degradation of the structural system. The RUL of the system is then obtained using Bayesian inference. The inference process can be based on real-time observational data, which is used as evidence, or by introducing empirical inference models in order to dynamically correct the network and thus improve the prediction accuracy.
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic diagram of the RUL prediction method for self-enhanced structures.

# 2.2. DBN RUL Prediction Framework 

BNs are a data-driven inference method widely used in the reliability assessment and fault diagnosis analysis of complex systems. It is a graphical network that applies probabilistic inference and consists of two parts: a qualitative part and a quantitative part. The qualitative part is represented by a directed acyclic graph that consists of the nodes of the system variables and directed arcs that indicate the causal relationships between the nodes. The quantitative part is a table of conditional probabilities between the child and parent nodes.

According to conditional independence and chain rule, the joint probability distribution $P(U)$ of variable $U=\left\{A_{1}, A_{2}, \cdots, A_{N}\right\}$ can be expressed as follows:

$$
P(U)=\prod_{i=1}^{N} P\left(A_{i} \mid P a\left(A_{i}\right)\right)
$$

where $P a\left(A_{i}\right)$ represents the parent node of $A_{i}$.
If there is new evidence $E$, then the posterior probability of the variable can be calculated by the Bayesian formula, as shown in Equation (2):

$$
P(U \mid E)=\frac{P(E \mid U) P(U)}{P(E)}=\frac{P(E, U)}{\sum_{U} P(E, U)}
$$

DBNs are a combination of a static BN and temporal information, forming a new stochastic model that processes temporal data. Each time step in the model is called a time slice. The basic structure of DBNs is shown in Figure 2, where $t$ represents the current time slice, $t+1$ represents the next time slice, $\Delta t$ represents the interval of time slices, the dashed directed arc in the figure represents the relationship between variables in the same time slice, and the solid directed arc represents the relationship between variables in different time slices. In order to describe the state changes in the real dynamic system, some have scholars [19] proposed the DBN theory. Similar to the calculation method of static BNs, the joint probability distribution of DBNs can be calculated as follows:

$$
P\left(A_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{N} P\left(A_{t}^{i} \mid P a\left(A_{t}^{i}\right)\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Structure of dynamic Bayesian network.
The DBN structural modelling method comprises causality, mapping algorithms and structured learning [10]. For structural systems, detailed causal relationships and sufficient training data are usually difficult to achieve due to the non-existence of a one-to-one correspondence between some primitive RUL estimation methods and the DBN model.

In this case, the structure of the DBN can be transformed from the physical model of the structural system [10], as shown in Equations (4)-(6).

$$
\begin{gathered}
E n_{n}^{t}=f_{n}\left(\lambda_{1}^{t}, \quad \lambda_{2}^{t}, \quad \ldots, \lambda_{n}^{t}, \quad \operatorname{par}_{1}^{t}, \quad \operatorname{par}_{2}^{t}, \quad \ldots, \operatorname{par}_{n}^{t}, \quad E n_{0}, t\right) \\
\delta_{n}^{t}=\xi_{n}\left(E n_{1}^{t}, \quad E n_{2}^{t}, \quad \ldots, E n_{n}^{t}, \quad \operatorname{Ipar}_{1}^{t}, \quad \operatorname{Ipar}_{2}^{t}, \quad \ldots, \operatorname{Ipar}_{n}^{t}, \quad \operatorname{par}_{1}^{t}, \quad \operatorname{par}_{2}^{t}, \quad \ldots, \operatorname{par}_{2}^{t}, t\right) \\
R U L^{t}=\psi_{n}\left(\delta_{1}^{t}, \quad \delta_{2}^{t}, \quad \ldots, \delta_{n}^{t}, \quad e v_{n}^{t}, \quad e r_{n}^{t}, \quad t\right)
\end{gathered}
$$

The dependent variables in Equations (4)-(6) correspond to the nodes shown in Figure 1, with some parameters replaced by the first letters of the node name. The subscript $n$ denotes the nth node and $n=0$ denotes the initial state of the node. The superscript $t$ indicates the current time slice. $f_{n}, \quad \xi_{n}, \quad \psi_{n}$, respectively, represent the physical model of the functional relationship between the independent variables and dependent variables at the corresponding node layer. The specific functional relationship is explained in the case study.

# 2.3. DBN Parameter Modelling 

The modelling steps for the DBN parameters are shown in Table 1, where the DBN is constructed by extending the BN, in which the prior probabilities of the parent nodes are determined, either from expert data, design manual data, experimental data, etc. The distribution can be in the form of a function, such as exponential, normal, logarithmic, Weibull, etc. The conditional probability table for the parent and child nodes is obtained by transforming the physical model and then constructing a complete conditional probability table using the discrete sampling of the parent nodes and an appropriate method (e.g., Monte Carlo). If no previous information is available, then weakly informative prior distributions should be used [20].

Table 1. DBN parameter modelling steps.


### 2.4. RUL Prediction

The RUL of a structure is the time between it comes into service and that at which a certain indicator reaches a critical value. The evolution of $\Delta \kappa$ changes dynamically due to multiple sources and is difficult to predict using a fixed function model. Especially for deepwater structures, the unpredictable environment makes predicting the RUL difficult. Especially for deepwater structures, the unpredictable deepwater environment makes predicting the RUL more difficult. The performance degradation of deepwater structures is mainly caused by the accumulation of corrosion and crack extension. This paper predicts the RUL of a specific time slice based on static BN forward inference. Extending a BN to a DBN, while considering the mechanical properties of the structural system and the structural thickness changes caused by self-enhancement methods, can a achieve a dynamic assessment of the RUL, which can provide more accurate prediction data for a structural system with an enhanced lifetime.

## 3. Case Study: Subsea Christmas Tree Valve Actuator

Subsea Christmas tree valve actuators need to serve in deep water for 20 years, and they are affected by the complex environment for a long time; however, cracks are very easily caused by vibration, corrosion, wear, fatigue, temperature, and other factors during the working process, which directly affects the actuator's life. If there is no accurate prediction of the trends observed in the development of cracks, when the accumulation of damages reaches a certain extent, the body may be destroyed and a major oil spill accident may occur. The actuator is a complex system driven by electricity that is aided by a high-pressure downhole in order to achieve pressure compensation; this uses electric power and compensation pressure to make the valve open and close, as shown in Figure 3. Such complex working conditions make the function of the structural system more demanding. An actuator is used as a case study in order to illustrate the method proposed in this paper. In this paper, based on the physical model of the actuator, the BN reasoning architecture is constructed. The theoretical reasoning is the main one, and the published experimental data are compared in order to prove the accuracy of the proposed method.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Subsea Christmas tree high-pressure valve actuator.

### 3.1. Physical Model for Predicting Wall Thickness of Structural Systems Based on Self-Enforcement Method

The wall structure thickness of the actuator can be estimated according to Equation (7):

$$R_0 = R_i \cdot \mathbf{N}[K_1] \tag{7}$$

where $R_i$ is the inside diameter at a minimum wall thickness for a given operating condition according to the design manual, $R_0$ is the outside diameter, $K_1$ is the diameter ratio of the structure, $K_2 = \mathbf{N}[K_1]$ is a positive integer that is not less than value of $K_1$ in [], and $K_1$ can be obtained according to the Faupel–Furbe formula [21], as shown in Equation (8).

$$p_b = \frac{2}{\sqrt{3}} \cdot \sigma_s \cdot \left(2 - \frac{\sigma_s}{\sigma_b}\right) \ln K_1 \tag{8}$$

where $\sigma_s$ is the yield stress of the structural material, $\sigma_b$ is the strength stress, $p_b$ is the burst pressure and should ensure that $p_b \geq n_b \cdot p_i$, $p_i$ is the internal working pressure, and $n_b$ is the safety factor, which is assumed here to be 2.6.

According to Equations (7) and (8), the following is obtained:

$$
K_{1}=\exp \left(\frac{\sqrt{3} p_{b} \sigma_{b}}{4 \sigma_{s} \sigma_{b}-2 \sigma_{s}^{2}}\right)
$$

Based on the above physical model, a BN model is constructed to predict the wall thickness of the structural system for the self-enforcement method, as shown in Figure 4. The material selected for the structural body of the actuator is ASTM A694 F65, and $\sigma_{s}, \sigma_{b}$ and $p_{b}$, all follow the law of normal distribution [22], as shown in Table 2. The discrete initial probabilities of $p_{i}$ are shown in Table 3.
![img-3.jpeg](img-3.jpeg)

Figure 4. BN model for wall thickness prediction of structural systems with self-enhancing methods.
Table 2. Probability distribution of $\sigma_{s}, \sigma_{b}, p_{b}$ and $R_{i}^{0}$ parameters.


Table 3. Discrete initial probabilities for $p_{i}$.


# 3.2. Self-Enhancement Optimal Internal Pressure Model 

The interface between the plastic and elastic layers of the structure, i.e., the radius of the optimum elastic-plastic critical surface $R_{c}$.

$$
R_{c}=R_{i} \exp \left(\frac{\sqrt{3} p_{i}}{\sigma_{s}}\right)
$$

The diameter ratio $K_{c}$ of the optimum elastic-plastic critical surface.

$$
K_{c}=\frac{R_{c}}{R_{i}}
$$

A BN model based on Equations (10) and (11) is constructed, as shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. BN of $K_{c}$.
For values of $K_{c}$ that are less than 2.21846 , no reverse yielding occurs. Therefore, after the self-enhanced treatment, the optimal internal pressure $p_{c}$ is calculated using the fourth strength theory as follows, and its BN model is shown in Figure 6.

$$
p_{c}=\frac{\sigma_{s}}{\sqrt{3}}\left[1+2 \ln K_{c}-\left(\frac{R_{c}}{R_{0}}\right)^{2}\right]
$$

![img-5.jpeg](img-5.jpeg)

Figure 6. BN model of $p_{c}$.

3.3. Residual Stress Distribution in the Self-Enhancement Structure

The stress distribution in the structural system directly affects the rate of crack expansion, which in turn has an impact on the prediction of the RUL; therefore, the stress distribution in the structural system needs to be clarified. When a self-enhancement treatment is carried out, a $p_{c}$ is applied and the residual stresses in the post-self-enhancement body at this pressure can be calculated using the following equation:
(1) Resilient areas $\left(R_{c} \leq r \leq R_{0}\right)$

$$
\sigma_{e 1}=f\left(p_{c}\right)=\left\{\begin{array}{l}
\sigma_{e r 1}=\left[1-\left(\frac{R_{0}}{r}\right)^{2}\right]\left(\frac{\sigma_{y}}{\sqrt{3}}\left(\frac{R}{R_{0}}\right)^{2}-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}} p_{c}\right) \\
\sigma_{e \theta 1}=\left[1+\left(\frac{R_{0}}{r}\right)^{2}\right]\left(\frac{\sigma_{y}}{\sqrt{3}}\left(\frac{R}{R_{0}}\right)^{2}-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}} p_{c}\right) \\
\sigma_{e z 1}=\frac{\sigma_{y}}{\sqrt{3}}\left(\frac{R}{R_{0}}\right)^{2}-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}} p_{c}
\end{array}\right.
$$

(2) Plastic areas $\left(R_{i} \leq r \leq R_{c}\right)$

$$
\sigma_{y 1}=f\left(p_{c}\right)=\left\{\begin{array}{l}
\sigma_{y r 1}=\frac{\sigma_{y}}{\sqrt{3}}\left[\left(\frac{R}{R_{0}}\right)^{2}-1+2 \ln \frac{r}{R_{c}}\right]-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}}\left[1-\left(\frac{R_{0}}{r}\right)^{2}\right] p_{c} \\
\sigma_{y \theta 1}=\frac{\sigma_{y}}{\sqrt{3}}\left[\left(\frac{R}{R_{0}}\right)^{2}+1+2 \ln \frac{r}{R_{c}}\right]-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}}\left[1+\left(\frac{R_{0}}{r}\right)^{2}\right] p_{c} \\
\sigma_{y z 1}=\frac{\sigma_{y}}{\sqrt{3}}\left[\left(\frac{R}{R_{0}}\right)^{2}+2 \ln \frac{r}{R_{c}}\right]-\frac{R_{i}^{2}}{R_{0}^{2}-R_{i}^{2}} p_{c}
\end{array}\right.
$$

The $\sigma_{e r 1}, \sigma_{e \theta 1}$ and $\sigma_{e z 1}$ represent the radial, circumferential and axial residual stress distributions in the elastic region, respectively. $\sigma_{y r 1}, \sigma_{y \theta 1}$ and $\sigma_{y z 1}$ represent the radial, circumferential and axial residual stress distributions in the plastic region, respectively. The BN of the residual stress distributions is shown in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. Residual stress distribution of BN model diagram.

# 3.4. Synthetic Stress Distribution under Working Conditions 

Equation (15) shows the radial, circumferential and axial stresses at the arbitrary radius $r$ at the working pressure.

$$
\begin{aligned}
\sigma= & \left\{\begin{array}{l}
\sigma_{r 2}=\frac{p_{i}}{K^{2}-1}\left(1-\frac{R_{i \text { oom }}^{2}}{r^{2}}\right) \\
\sigma_{\theta 2}=\frac{p_{i}}{K^{2}-1}\left(1+\frac{R_{i \text { oom }}^{2}}{r^{2}}\right) \\
\sigma_{z 2}=\frac{p_{i}}{K^{2}-1}
\end{array}\right. \\
& R_{\text {com0 }}=R_{i}(K-1)+C
\end{aligned}
$$

$$
\begin{gathered}
K=\left(\frac{[\sigma]}{[\sigma]-\sqrt{3} p_{i}}\right)^{1 / 2} \\
{[\sigma]=\min \left[\frac{\sigma_{b}}{n_{b}}, \frac{\sigma_{s}}{n_{s}}\right]}
\end{gathered}
$$

where $R_{\text {com } 0}$ is the initial wall thickness of the structure obtained using conventional design methods, $[\sigma]$ is the allowable stress for a given service condition and, $n_{b}$ and $n_{s}$ are the safety factors for the material.

During operation, the structure is subjected to a synthetic stress consisting of the working stress and residual stress, which is calculated synthetically according to Equations (19) and (20) in order to construct a BN model of the working stress distribution, as shown in Figure 8.

$$
\begin{aligned}
\sum_{R_{c} \leq r \leq R_{0}} \sigma & =\left\{\begin{array}{l}
\sum \sigma_{r}=\sigma_{e r 1}+\sigma_{r 2} \\
\sum \sigma_{\theta}=\sigma_{e \theta 1}+\sigma_{\theta 2} \\
\sum \sigma_{z}=\sigma_{e z 1}+\sigma_{z 2}
\end{array}\right. \\
\sum_{R_{i} \leq r \leq R_{c}} \sigma & =\left\{\begin{array}{l}
\sum \sigma_{r}=\sigma_{y r 1}+\sigma_{r 2} \\
\sum \sigma_{\theta}=\sigma_{y \theta 1}+\sigma_{\theta 2} \\
\sum \sigma_{z}=\sigma_{y z 1}+\sigma_{z 2}
\end{array}\right.
\end{aligned}
$$

![img-7.jpeg](img-7.jpeg)

Figure 8. BN model for stress distribution in working conditions.
According to the fourth strength theory, the equivalent force in the valve body operation is as shown in Equation (21), and the BN of the control group is constructed as shown in Figure 9, with the probability distribution of the parameters shown in Table 4.

$$
\sigma_{e q}=\sqrt{\frac{1}{2}\left[\left(\sum \sigma_{r}-\sum \sigma_{\theta}\right)^{2}+\left(\sum \sigma_{\theta}-\sum \sigma_{z}\right)^{2}+\left(\sum \sigma_{z}-\sum \sigma_{r}\right)^{2}\right]}
$$

![img-8.jpeg](img-8.jpeg)

Figure 9. BN model diagram of the control group.
Table 4. Probability distribution of $\sigma_{s}, \sigma_{b}, n_{b}, n_{s}$ and $r$ parameters.


# 4. Bayesian RUL Prediction Model 

### 4.1. Fatigue Factor Model

The physical property model for fatigue crack extension is expressed in the well-known Paris-Erdogan formula [23]. In engineering, the most widely used method for predicting the fatigue crack growth life is the Paris-Erdogan formula, which was proposed by Paris and Erdogan in 1963 on the basis of experiments. The Paris-Erdogan formula establishes the relationship between the stress intensity factor and the crack growth rate, which is the basis for predicting the fatigue crack growth life in engineering applications today.

$$
\frac{d D}{d N}=C(\Delta K)^{n}
$$

where $\Delta K$ is the stress intensity factor, which can be expressed empirically as $\Delta K=Y \Delta \sigma \sqrt{\pi D} ; Y$ is the crack shape factor and depends on the type of crack; $D$ is the crack length; $N$ is the number of stress cycles; and $C, n$ is related to the material factor and is empirically valuable. $\Delta \sigma=\sigma_{\max }-\sigma_{\min }, \Delta \sigma$ is the difference between the maximum and minimum fatigue bending stress, $\sigma_{\min }, \sigma_{\max }$ are the minimum and maximum fatigue bending stress, respectively, and $\sigma_{\min }, \sigma_{\max }$ vary with the residual stress. The BN model of stress difference is shown in Figure 10.

![img-9.jpeg](img-9.jpeg)

Figure 10. BN model diagram of stress differences.
Assuming an initial crack depth of $D_{0}$, the crack depth in the Nnd stress cycle is obtained according to Equation (23):

$$
D(N)=\left[D_{0}^{2 \frac{n}{2}}+\frac{(n-2) \times N \times C(Y \Delta \sigma \sqrt{\pi D})^{n}}{2}\right]^{\frac{n}{2-\alpha}}
$$

where $D_{0}$ is the initial crack depth and $N$ is the number of stress cycles. According to the above, the physical model is transformed into a fatigue crack expansion, as shown in Figure 11. $C, n, Y$ and $\Delta \sigma$ are variable nodes; using historical data and expert knowledge to obtain the parameter distributions and corresponding values, the initial probability distribution of each node is shown in Table 5. Since $C$ and $n$ have a clear algebraic relationship, this algebraic relationship is directly introduced into the model in the process of Bayesian network modelling. The relationship between $C$ and $n$ is as follows [10]:

$$
C=e^{(-3.34 n-15.84)}
$$

Table 5. Probability distribution of $D_{0}, n$ and $Y$ parameters.


![img-10.jpeg](img-10.jpeg)

Figure 11. BN model diagram of crack extension.

# 4.2. Corrosion Factor Model 

Corrosion is an important concern in engineering due to its effect on the through-life performance of maritime structures [24]. The corrosion loss model proposed by Soares and Garbatov (1999) has been widely accepted by scientists worldwide [25]. The model represents the corrosion depth as a non-linear function of time, which can better fit the actual corrosion loss process of marine structural components. The model is divided into four stages, as shown in Figure 12. The $O^{\prime} O$ stage is the protection stage of the coating, when the protective layer is not damaged and no corrosion loss occurs. From the second stage ( $O B$ stage), the protective layer fails, non-linear corrosion loss begins to occur, the corrosion consumption of this stage increases rapidly, and the thickness of the structural components decreases rapidly. In the $B C$ stage, corrosion is slow and the corrosion rate is slower than in the second stage. In the last stage, the corrosion consumption is at its limit, the corrosion rate decreases significantly, and the wall thickness of the structural components reaches a critical value. The mathematical expression of the corrosion model is shown in Equation (25). $d_{m}$ is the long-term corrosion wastage that corresponds to the last stage. In this paper, the limiting concept is adopted and the limiting length of $d_{m} \rightarrow R_{0}$, the depth of corrosion, is considered to be close to the wall thickness. $t_{c}$ is the coating life regarding the first stage. $\tau_{c}$ is the transition time and is deeply related to the second stage.

$$
d(t)= \begin{cases}f\left(t-t_{C} ; \emptyset\right) & t>t_{C} \\ 0 & t \leq t_{C}\end{cases}
$$

where $d(t)$ is the corrosion depth at the moment and $t_{c}$ is the coating life $\left(O^{\prime} O\right.$ stage). $t_{c}$ is modelled using a lognormal random variable with mean $\mu_{C}$ standard deviation $\delta_{C}$. The mean coating life, $\mu_{C}$, is also modelled using a lognormal random variable with mean $\mu_{\mu_{C}}$ and standard deviation $\delta_{\mu_{C}}$. The coating life of the BN is shown in Figure 13. $\chi_{\mu_{\mu_{C}}}$, $\chi_{\delta_{\mu_{C}}}$ and $\chi_{\delta_{C}}$ are the prior distributions of the $\mu_{\mu_{C}}, \delta_{\mu_{C}}$ and $\delta_{C}$, respectively. The relevant hyperparameters are taken, as shown in Table 6 [20].

Table 6. Probability distribution of $\mu_{\mu_{C}}, \delta_{\mu_{C}}$ and $\delta_{C}$ parameters.


![img-11.jpeg](img-11.jpeg)

Figure 12. Corrosion depth with a function of time.
![img-12.jpeg](img-12.jpeg)

Figure 13. Coating life of BN.
When $t>t_{C}$ (OC stage), corrosion starts to occur. $\emptyset=\left[\theta_{1}, \ldots, \theta_{t}, \theta_{t+1}\right]$ is the parameter of corrosion depth when modelled as a constant, which can be calculated using Equation (26). The corrosion depth at time $t$ is obtained by calculating Equation (27). The BN model for this process is shown in Figure 14.

$$
\begin{gathered}
\tan \theta_{t}=\frac{d_{\infty}}{\tau_{t}} \approx \frac{R_{0}}{\tau_{t}} \\
d\left(t>t_{C}\right)=d_{\infty}\left(1-e^{-\left(t-t_{C}\right) / \theta_{t}}\right) \approx R_{0}\left(1-e^{-\left(t-t_{C}\right) / \theta_{t}}\right)=R_{0}\left(1-e^{-\left(t-t_{C}\right) / \arctan \left(\frac{R_{0}}{\tau_{t}}\right)}\right) \\
\hline
\end{gathered}
$$

![img-13.jpeg](img-13.jpeg)

Figure 14. BN model diagram of corrosion depth.

### 4.3. Pressure Self-Enhancement and RUL Prediction Model for Deepwater Structures

Based on the physical model described above, a BN for predicting the RUL of underwater self-enhanced structures is constructed, as shown in Figure 15. The grey circles indicate the past time slices. When *t* < *t*_C, due to the protective effect of the coating, the structural body does not corrode and at this time *d*(*t* < *t*_C) = 0, the life loss mainly considers the cracking process. When *t* > *t*_C, the life loss of the structural body is caused by the crack extension and accumulation of corrosion together. The life loss node is ∑*D*^i, and the RUL of the structure can be estimated after determining the loss threshold, which is dynamically changed according to the wall thickness *R*_0 of the structure, i.e., the threshold is proportional to *R*_0. This paper assumes that the threshold value is 50% of *R*_0. *R*_0 is affected by the self-enhancement process and changes dynamically, which not only has a direct impact on the threshold value, but also on the residual stresses in the structure, and ultimately on the crack expansion rate.

![img-14.jpeg](img-14.jpeg)

**Figure 15.** BN model for the RUL prediction of underwater self-enhanced structures.

### 5. Results and Discussion

The BN is a graph model that represents the probabilistic correlation between variables. It is one of the most effective theoretical models in the field of uncertain knowledge representation and reasoning. BNs have been widely used in diagnosis [26], prediction, risk analysis [27–29] and ecosystem simulation. At present, there are many software platforms that can build BNs, such as BN Toolkit, Netica, BayesBuider, Hugin Expert, etc. Netica is a BN learning software developed using Java. As a fully functional BN analysis software, the key is used to carry out the system risk analysis and system software invalid simulation modelling; this is a scientific research must use special BN tools. Yuan X. et al. [30] divided the subsea tree system into three modules based on BN, namely the above-water part, the below-water part and the FPSO. They established the remaining life prediction model of the subsea tree system by using Netica software, and analysed the reliability of the corresponding modules. Combined with the failure threshold, the remaining life was predicted. In this paper, Netica is used to create a BN window, call the data set of the sample, perform the function of the network structure learning module, define the node attributes, create the BN model of the remaining useful life of crack propagation and run the corresponding BN, which is composed of nodes and directed connection lines; the node represents the influence parameter, which consists of the node name and the node probability distribution table. The directed connection line represents the relationship

between the parameters from the parent node to the child node, where the arrow represents the relationship between the parameters in the current time slice.

As shown in the upper part of Figure 16, a BN calculation model for the wall thickness R0 and the optimum internal pressure pc of the structural system for the selfenhanced method is constructed using Netica software, based on the BNs derived in Sections 3.1 and 3.2. Based on this, the BN of residual stresses in the elastic and plastic regions derived in Section 3.3 is used to construct the BN calculation model of residual stresses after self-enhancement using Netica software, as shown in Figure 16. Each node in the figure corresponds to a variable in the BN, and the probability distribution corresponding to each variable in the above section is set in the node, with the directed connecting lines indicating the action relationship between the covariates from the parent node to the child node. Different residual stress distributions are obtained based on Bayesian forward inference.
![img-15.jpeg](img-15.jpeg)

Figure 16. BN calculation model of residual stresses after self-enhancement.
Based on the stress distribution under working pressure derived in Section 3.3, the radial, circumferential and axial working stress nodes of the arbitrary radius are set up on the basis of Figure 16 and then connected to the corresponding sub-nodes. The BN calculation model for the synthetic stresses of the working and residual stresses is then set up, as shown in Figure 17, to obtain the actual stress distribution.

![img-16.jpeg](img-16.jpeg)

Figure 17. BN computational model of synthetic stress.
After constructing the synthetic stress network calculation model, the maximum and minimum stress nodes and their difference nodes ( $v$ Oeq) are set, and the corresponding nodes according to the fatigue factor model and corrosion factor model in Section 4 are set in order to construct the BN calculation model of crack extension for a single time slice, as shown in Figure 18. After extension, a DBN can be obtained. $D$ in the figure is the current time slice crack extension depth, as $t_{c}$ is a deterministic calculation method; therefore, a mathematical model directly in the node $D$ can be used to define the calculation formula, and RUL is obtained according to Equation (28), where $D_{\text {threshold }}$ indicates the life threshold, i.e., the maximum allowable value of crack. By deleting $v O e q$ and its parent node, a control group BN without pressure self-enhancement can be constructed.

$$
R U L=\frac{D_{\text {threshold }}-D}{D_{\text {threshold }}} \times 100 \%
$$

![img-17.jpeg](img-17.jpeg)

Figure 18. BN computational model of crack extension and RUL for a single time slice.

# 5.1. RUL Calculation 

The RUL prediction method proposed in this paper argues that pressure self-enhancement improves the stress distribution in the structure of the equipped parts and that stress is an important variable in the well-known Paris-Erdogan crack extension formula. By constructing a Bayesian inference model, a comparison of the results of pressure self-enhanced crack extension and the probability distribution of crack extension using conventional methods is obtained, as shown in Figure 19. From Figure 19a, it can be seen that the crack probability peaks move towards the crack expansion with time, showing an exponential growth pattern. In the first year, when the crack is 0.4418 , the probability value reaches $45.2 \%$. In the seventh year, the peak value of the crack occurrence probability moves to the right, and when the crack value is 4.7072 , the maximum probability of occurrence is $37 \%$. Similarly, Figure 19b shows the same pattern. In the first year, the probability of occurrence at a crack value of 0.4418 is about $49 \%$, and in the seventh year, when the crack value is 4.7072 , the maximum probability of occurrence is $39 \%$. However, a comparison of the two plots shows that the results using pressure self-enhancement at the same time points have slightly smaller crack lengths corresponding to the peak points compared to the conventional inference results.
![img-18.jpeg](img-18.jpeg)

Figure 19. Crack growth depth, (a) with self-enhancement, (b) without self-enhancement.

To quantify the crack values, a summation of the product of each probability and the corresponding crack value is used to represent the estimated crack values, as shown in Figure 20. During the first seven years of operation, the crack growth rate is similar. The comparison shows that the crack extension rate has slowed down with the use of pressure self-enhancement after the seventh year, indicating that the life of the component has been improved to some extent. Using a crack length of $50 \%$ in the wall thickness as the end-of-life threshold, it can be seen that the life of the structural member with selfenhancement is approximately 12.3 years compared to approximately 11 years without pressure self-enhancement. At approximately 9 years of service, the crack extension rate shows a turning point and a rapid expansion trend. Therefore, 9 years is the necessary time for maintenance and repair monitoring in order to prevent accidental damage.
![img-19.jpeg](img-19.jpeg)

Figure 20. Cumulative crack depth.

# 5.2. Effect of Different Factors on RUL 

This paper focuses on the pattern of influence of the three parent nodes of the independent variables $\left(P_{b}, P_{i}\right.$ and Fatigue) in the BN on the results. In Figure 21, in the first eight years, all three factors have little influence on the RUL. After 12 years, the fatigue factor shows obvious change, so it is suggested that the corrosion of the device is checked after 12 years or so. After 15 years, the influence of the Pi factor becomes prominent. It is suggested that the change in the internal pressure is paid attention to when the equipment is 15 years old. The results in Figure 21 show the crack extension curves when all influencing factors are considered and when only one factor is considered. It can be seen that their contribution to the impact on the life of the member is Fatigue $>P_{i}>P_{b}$, with $P_{b}$ having almost no influence on the life. The RUL is calculated according to Equation (27), and the RUL of the structure under the influence of different factors is obtained, as shown in Figure 22. Under the influence of only one of the factors $P_{i}, P_{b}$ and Fatigue, the service life is 16.8 years, 47.9 years and 12.9 years, respectively. This indicates that $P_{i}$ and Fatigue are the most important factors influencing the RUL. Therefore, increasing the RUL, improving the working internal pressure environment and enhancing anti-corrosion measures are effective methods.
![img-20.jpeg](img-20.jpeg)

Figure 21. Crack depth growth under the influences of different causes.

![img-21.jpeg](img-21.jpeg)

Figure 22. The RUL value under the influence of different causes.

# 5.3. Model Validation and RUL Updating with New Evidence 

Based on the three subsea oil pipeline crack extensions observed in the literature, three pieces of evidence are entered into the BN, as shown in Figure 23 [10]. Firstly, the annual average of the three pieces of evidential data is taken for comparison and validation, and a prediction curve of this method is made, as shown in Figure 24. In terms of upper and lower error limits, the method proposed in this paper agrees well with the observed evidence. The error of forecast data is less than $8.5 \%$ in the first 4 years, less than $20.4 \%$ in the 5th-10th years, and less than $11.3 \%$ after 10 years.
![img-22.jpeg](img-22.jpeg)

Figure 23. Three new pieces of evidence.
![img-23.jpeg](img-23.jpeg)

Figure 24. Model error graphs.
As the crack values for the first four years of the three evidence curves are close to zero, starting from year 5 , the crack values for the 5 th, 6 th, 7 th and 8 th years are chosen as evidence to replace the $D$ values for the corresponding years of the BN constructed in

this paper and to achieve network updates. After obtaining the network update, the crack extension prediction for the structure after pressure self-enhancement is shown in Figure 25. Some changes have been made to the crack extension curves due to the corrections made to the evidence, with the corresponding crack extension rates increasing and decreasing under the effect of the corrections made to Evidence 1 and Evidence 2, respectively. The curve almost coincides with the originally predicted curve after the correction of Evidence 2. More importantly, it is theoretically considered that the more evidence there is, the more accurate the prediction model is; in addition, in the actual use of the method, the monitoring data should be fed into the model in real time to improve the prediction accuracy.
![img-24.jpeg](img-24.jpeg)

Figure 25. Predicted crack extension curves of structures after pressure self-enhancement.

# 5.4. Initial Crack Factor Analysis 

Due to production and processing conditions, structural parts will inevitably have different degrees of initial crack defects. Based on the evaluation method proposed in this paper, the prediction curves for different initial crack values are obtained by varying the average value of the $D_{0}$ node in model Figure 18, as shown in Figure 26. Since the initial depth is increased, the crack depth increases rapidly. If the initial depth is increased to 1.0 mm , the crack depth increases to 38.76 mm in the 12th year, whereas the crack depth was 11.86 mm when the initial depth was 0.1 mm . If the required service life is 10 years, the initial crack value should be controlled to within 0.02748 mm using reverse derivation.
![img-25.jpeg](img-25.jpeg)

Figure 26. Initial cracking impact curve.

## 6. Conclusions

In this paper, a method that can be used to predict the RUL of underwater selfenhancement structures based on DBNs is proposed. According to the crack extension depth obtained using BNs and the threshold formula, the RUL of the structures can be obtained. Taking the subsea Christmas tree high-pressure valve actuator as an example, the accuracy of the method is verified by comparing the prediction results with the experimental data. Because the Bayesian model reasoning process adopted in this paper can take the data observed in real time as evidence or introduce the empirical reasoning model for

the dynamic correction of the network, the accuracy of predicting the RUL of underwater structures can be improved. The probability distribution of crack extension in pressure self-enhancement structures was obtained using Bayesian inference. Under the influence of multiple causes and a single cause, the crack extension probability points moved towards the direction of crack extension with the passage of time, showing an exponential growth trend. The comparison of the crack extension probability distribution between the pressure self-enhancement method and the conventional method shows that the crack length corresponding to the peak point of the conventional method is slightly smaller at the same time point. The quantified crack values show that the crack expansion rate slows down after pressure self-enhancement, which indicates that the life of the structural component is improved. The stress distribution and pressure performance of the equipment parts are improved by the pressure self-enhancement technology, thus increasing the service life of structural parts. Via an analysis of the results, it is concluded that corrosion is the most important influencing factor, and special attention should be paid to the corrosion of the structure in the first 7 years of service. Due to the limitation of the production and processing conditions, structural parts will inevitably have different degrees of initial crack defects. Based on the evaluation method proposed in this paper, the control range of the initial crack can be reversely estimated according to the RUL. This method is a guide to the operation and maintenance of deepwater pressure equipment.

Author Contributions: Conceptualization, P.L. and C.D.; methodology, P.L.; software, P.L.; validation, P.L., C.D. and B.L.; formal analysis, C.D.; investigation, S.Z.; resources, S.L.; data curation, G.L.; writing-original draft preparation, P.L.; writing-review and editing, C.D.; visualization, S.Z.; supervision, B.L.; project administration, P.L.; funding acquisition, P.L. All authors have read and agreed to the published version of the manuscript.
Funding: The authors wish to acknowledge the financial support of National Natural Science Foundation of Shandong (ZR2021QE059), Key Lab of Industrial Fluid Energy Conservation and Pollution Control (Qingdao University of Technology), Ministry of Education (2022JXGCKFKTYB01), Shandong Provincial Key Laboratory of Ocean Engineering (KLOE202204), National Natural Science Foundation (52074161).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data that support the findings of this study are available from "Remaining Useful Life Estimation of Structure Systems under the Influence of Multiple Causes: Subsea Pipelines as a Case Study", upon reasonable request.

Acknowledgments: The authors would like to thank every person/department who helped throughout the research work. The careful review and constructive suggestions made by the anonymous reviewers are gratefully acknowledged.

Conflicts of Interest: The authors declare no conflict of interest.

# Nomenclature 


