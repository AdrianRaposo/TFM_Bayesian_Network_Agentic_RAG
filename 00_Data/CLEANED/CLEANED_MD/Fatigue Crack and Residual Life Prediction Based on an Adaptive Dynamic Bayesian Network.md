# Article 

## Fatigue Crack and Residual Life Prediction Based on an Adaptive Dynamic Bayesian Network

Shuai Chen ${ }^{1}$ (D) Yinwei Ma ${ }^{2}$, Zhongshu Wang ${ }^{2}$, Minjing Liu ${ }^{1, *}$ and Zhanjun Wu ${ }^{3, *}$


#### Abstract

check for updates Citation: Chen, S.; Ma, Y.; Wang, Z.; Liu, M.; Wu, Z. Fatigue Crack and Residual Life Prediction Based on an Adaptive Dynamic Bayesian Network. Appl. Sci. 2024, 14, 3808. https:// doi.org/10.3390/app14093808

Academic Editor: Andrea Prati

Received: 18 February 2024
Revised: 13 April 2024
Accepted: 22 April 2024
Published: 29 April 2024


## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Mechanics and Aerospace Engineering, Dalian University of Technology, Dalian 116024, China
2 Beijing Aerospace Technology Institution, Beijing 116024, China; wangzhongshu@buaa.edu.cn (Z.W.)
3 School of Materials Science and Engineering, Dalian University of Technology, Dalian 116024, China

* Correspondence: liumj@dlut.edu.cn (M.L.); wuzhj@dlut.edu.cn (Z.W.)

Abstract: Monitoring the health status of aerospace structures during their service lives is a critical endeavor, aimed at precisely evaluating their operational condition through observation data and physical modeling. This study proposes a probabilistic assessment approach utilizing Dynamic Bayesian Networks (DBNs), enhanced by an improved adaptive particle filtering technique. This approach combines physical modeling with various predictive sources, encompassing cognitive uncertainties inherent in stochastic predictions and crack propagation forecasts. By employing crack observation data, it facilitates predictions of crack growth and the residual life of metal structure. To demonstrate the efficacy of this method, the research leverages data from three-point bending and single-edge tension fatigue tests. It gathers data on crack length during the fatigue crack progression, integrating these findings with digital twin theory to forecast the residual fatigue life of the specimens. The outcomes show that the adaptive DBN model can precisely predict fatigue crack propagation in test specimens, offering a potential tool for the online health assessment and life evaluation for aerospace structures.

Keywords: dynamic Bayesian network; structural health monitoring; particle filter; fatigue crack growth

## 1. Introduction

Modern aerospace vehicles must withstand complex service environments, posing an increasingly strict requirement for structural performance. As the service load condition becomes severer, coupled with inevitable defects and residual stresses from manufacturing processes, the degradation of material and structural performance is an issue that cannot be ignored. The harsh service environment can generate structural damage in terms of cracks, delamination, etc., which poses a serious threat to structural safety and integrity. On the other hand, the reusability of aerospace structures has been a core concern in recent years [1]. Reusability is achieved through a combination of a "safety factor + regular maintenance" approach, that is, by increasing the safety margin to enhance structural durability and ensuring reliability through inspections and maintenance [2]. This challenge necessitates a deep understanding of the service environment and load-bearing capacity of structures, as well as effective prediction and management of potential damages. To further enhance the confidence in structural integrity assessments, structural health monitoring technologies for real-time monitoring and evaluation of the service state of structures play a significant role in improving structural performance, ensuring service safety, and reducing maintenance costs [3].

Currently, there are two main methods for structural health monitoring [4]: one is based on artificial intelligence data analysis, and the other is based on physical models (PMs). However, the use of pure data-driven models can be expensive, as it requires costly experiments to obtain data. Meanwhile, simulation-driven PM/FEM models have modeling errors that deviate from actual structures. Practical systems inevitably encounter

uncertainties [5], such as sensor noise, material defects, mechanical damage, vibration, and load interference, which can interfere with their diagnostic reasoning and health assessment. Additionally, real-world systems are dynamic and change over time with their health status. Therefore, there is a crucial need to combine physical models with data-driven models to solve health monitoring problems.

Recently, the concept of digital twins has gained widespread attention in the field of intelligent manufacturing due to the development of communication technology in intelligent algorithms [6,7]. Digital twins establish an interactive relationship between the physical and digital worlds. They provide simulation models based on physical mechanisms and health monitoring services for data obtained in the physical world. Complex systems collect sensor data from the physical world and send them to digital twin virtual models through communication technology. The digital twin virtual model processes these data, updates the simulated physical model in real time, and sends control commands to provide optimization and decision support for physical systems.

The U.S. Air Force adopted the "Airframe Digital Twin" (ADT) for aircraft design, maintenance, and performance prediction. It employs digital twins to replicate the physical and mechanical attributes of aircraft, enabling the prediction of structural fatigue cracks and extension of the aircraft's remaining service life [8-10]. The ADT encompasses three core modules: online monitoring, condition assessment, and lifespan prediction. It integrates aerodynamic and finite element analyses along with other structural models, which monitor the evolution of fatigue, vibration, and other material states in flight structures. Through dynamic updates incorporating specific geometry, material properties, flight history, and maintenance data, the ADT precisely forecasts aircraft behavior. This allows decisionmakers to tailor personalized management strategies for each aircraft, thereby prolonging service life and reducing maintenance expenses.

Various types of sensors are utilized within the monitoring data collection module of ADT systems for the identification of damage, including ultrasonic sensors, X-ray devices, piezoelectric sensors, fiber Bragg gratings, and distributed fiber optics [11-15]. These sophisticated sensing devices enable the timely detection of crack damages, thus providing a robust guarantee for the safety assessment of structures.

However, due to uncertainties associated with, e.g., material geometry, internal defects, irregular damages, and mechanical environments, the prediction of damage evolution in aerospace structures exhibits unsatisfactory accuracy. Therefore, it is necessary to establish a probabilistic model that integrates diagnosis and prediction, which can reduce the uncertainty of time-independent state variables through continuous observation (diagnosis) and probabilistically predicts the evolution of future crack damages (prognosis), thereby obtaining a more accurate assessment of the structural health state with multiple sources of uncertainty.

Within the digital twin framework, the Dynamic Bayesian Network (DBN) is among the most widely applied probabilistic methods [16,17]. Its robust system reliability framework makes it a primary method for representing and managing uncertainties in physical models (related to geometry, materials, connection stiffness, etc.) in digital twins. DBNs excel at providing direct representations of complex systems and are highly effective in identifying inter-component relationships, making them suitable for monitoring, diagnosis, and prediction tasks in uncertain environments. A unique advantage of DBNs is their ability to integrate a wide range of information sources, including experimental data, historical records, and expert opinions, which is particularly valuable in fault-tolerant systems where data are often sparse and varied. Additionally, DBNs stand out for their capability to model the temporal dynamics of cascading events, offering a more accurate description of how systems evolve over time. This enhances prediction accuracy and aids in better decision-making, resource planning, and allocation in complex and evolving systems.

Wei et al. [18] proposed an object-oriented modeling approach, building a DBN for the entire aviation system health in a bottom-up manner based on Bayesian theory, and validated its effectiveness and robustness through experiments on a specific aviation fuel

delivery system. Yu et al. [19] introduced a digital twin health monitoring method based on non-parametric Bayesian networks, combining an improved Gaussian particle filter and a Dirichlet process mixture model for real-time model updating, significantly enhancing monitoring accuracy. Karve et al. [20] developed an intelligent task planning method based on digital twins, employing a DBN to predict the probability distribution of crack propagation, considering the quantification of uncertainties and encompassing damage diagnosis, prediction, and task optimization, to optimize fatigue crack growth and maintenance intervals. Rabiei et al. [21] proposed a DBN framework for the online integration of health assessment information from empirical crack growth models, structural health monitoring, and regular inspections, updating crack size distribution and model parameters for prediction. Boris et al. [22] introduced a framework utilizing a DBN with MCMC for predicting and updating crack length in fatigued structural components, including parameter probability density identification and updating. Lee et al. [23] proposed a Bayesian method to estimate initial crack length distribution for PRA of repaired structures, improving parameter selection and analyzing KT-1 aircraft repair risk.

However, Bayesian networks have some defects. For instance, they are highly dependent on prior probabilities, and prior probabilities often depend on assumptions, leading to poor prediction results. Moreover, the large noise of dynamic measurement data acquisition and the calculation time cost of Bayesian distribution steps make online real-time Bayesian network systems less accurate and precise than offline Bayesian monitoring systems [24], especially for data that are more dependent on manual observation, such as cracks, which are often scarce, and it is challenging to meet the needs of Bayesian networks for a large amount of observation data.

To overcome existing limitations, this study introduces an innovative adaptive DBN model aimed at crafting a predictive module for tracking the evolution of fatigue crack damage in the digital twin systems of aerospace structures. This sophisticated model merges adaptive particle filtering with a comprehensive range of cognitive uncertainties found in crack propagation equations, spanning material characteristics, geometric configurations, model parameters, measurements, and load conditions. It adeptly monitors the progression of time-variant state variables while minimizing uncertainties in time-invariant states (diagnosis). Moreover, the model leverages real-time updates, drawing from calibrated probability distributions of parameters and forecasts, to provide probabilistic estimates of fatigue crack growth and the remaining lifespan (prognosis). Each update introduces new particles to mitigate particle impoverishment, thus ensuring more accurate predictions. The validity and applicability of this model were confirmed using data from three-point bending and single-edge crack fatigue experiments. The findings reveal that the model precisely forecasts the velocity of damage crack progression, offering a feasible tool for the real-time evaluation of structural health and lifespan assessment.

# 2. Principle and Methods 

### 2.1. Fatigue Crack Growth Theory

In general, the fatigue failure of materials will go through three stages: crack initiation, stable expansion, and rapid unstable failure of cracks. Due to the relatively short time of rapid unstable failure of cracks, the fatigue life is often calculated by selecting the crack initiation life (from the beginning of use to the appearance of engineering detectable cracks) and the crack expansion life (from detectable cracks to critical crack size), as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. The cross-scale propagation of cracks.

The mechanism of crack formation life is quite complex. From the beginning of crack nucleation to the point where microscopic cracks expand into macroscopic cracks, it accounts for the largest proportion of fatigue life. Crack nucleation is mainly caused by local stress and strain concentration, and the existence of tiny inclusions or voids in engineering materials has a great influence on the crack nucleation process, resulting in a large degree of discreteness in crack formation life. The length range of microscopic cracks is generally $10-100 \mu \mathrm{~m}$, which is at the same order of magnitude as the size of the plastic zone at the crack tip. Currently, there are two commonly used methods for estimating crack formation life without obvious macroscopic cracks. The first method is to use the relationship curve between external constant amplitude cyclic stress amplitude $S$ and fatigue life $N$ (referred to as $S-N$ curve) as the main design basis for anti-fatigue design methods. This method has a long history and is still adopted by many anti-fatigue design specifications today. The other method is to assume a reasonable microscopic crack size based on experience (such as a microscopic crack length of 0.0588 inches commonly used in flight structures as the minimum observation size) and use the formula for macroscopic crack extension in fracture mechanics to calculate residual life.

Therefore, whether it is the fatigue life prediction of cracks that assumes reasonable microcrack sizes or the prediction of macroscopic crack fatigue life, it ultimately comes down to the study of the crack propagation rate. Currently, within the category of online elastic fracture mechanics, the strength of the crack tip singularity is characterized by a single parameter, stress intensity factor $K$. Therefore, many scholars consider linking the fatigue crack propagation rate with $K$ and then propose a series of fatigue crack propagation rate formulas, such as the most basic and commonly used Paris' law [25], the Forman law [26], and the Walker law [27] that considers the influence of stress ratio $R$ and strength factor threshold $K_{t \mathrm{~B}}$, as well as the full crack propagation formula and Nasgro law [28] that integrates simulation software.

According to Paris' law [25], the crack growth is described by the following:

$$
\frac{d a}{d N}=\mathrm{C}(\Delta K)^{m}
$$

where $K=F \sigma \sqrt{\pi a}$ is the stress intensity factor. $F$ is the shape factor. $\sigma$ is the equivalent stress, which is the stress at the crack location calculated without cracks. $a$ is the crack length. $C$ and $m$ are material parameters determined by experiments. $d a / d N$ is the fatigue crack propagation rate. This formula expresses the fatigue crack propagation rate in the form of a power function of the stress intensity factor amplitude $\Delta K$, which describes the law of crack propagation well and has the advantage of convenient calculation. Therefore, it is still widely used in engineering structural fatigue life prediction.

Fatigue crack growth life is the total number of load cycles from the initial crack $a_{0}$ to the critical crack length $a_{c}$. First, Equation (2) is used to obtain the size of critical crack size $a_{c}$.

$$
a_{c}=\frac{1}{\pi}\left(\frac{K_{C}}{F \sigma_{\max }}\right)^{2}
$$

where $\sigma_{\max }$ is the maximum cyclic stress. $K_{C}$ is the fracture toughness of the material.
According to crack growth Equation (1), the theoretical formula for predicting residual life is as follows:

$$
N=\int_{a_{0}}^{a_{c}} \frac{d a}{C(\Delta K)^{m}}
$$

Walker considered the influence of stress amplitude on crack propagation and incorporated the stress ratio $R$ into the Paris' law, referred to as the Walker law [27], as follows:

$$
\frac{d a}{d N}=\mathrm{C}\left((1-R)^{a} \Delta K\right)^{m}
$$

However, these laws have some limitations, and the accuracy is different under different crack conditions. For the complex crack conditions in practice, which law can obtain more accurate results is a problem to be solved.

# 2.2. Brief Introduction to Dynamic Bayesian Network 

Figure 2 illustrates a simple example of a DBN. Nodes $A_{i}$ and $C_{i}$ represent hidden variables, indicating states that cannot be directly observed. In some cases, the variable $C_{i}$ corresponds to a physical model, and $A_{i}$ represents parameters of $C_{i}$. The node $D_{i}$ denotes observed variables. The subscripts correspond to different moments. The arrows between nodes describe the conditional dependencies between variables, pointing from parent nodes to child nodes. This directionality from "cause" to "effect" signifies a causal relationship or non-conditional independence between parent and child nodes, which is mathematically characterized by conditional probability distributions (CPDs). Variables with the same subscript form an independent BN, and BNs across different time slices are also connected by arrows, depicting the influence of variables from one moment to the next.
![img-1.jpeg](img-1.jpeg)

Figure 2. A simple example of a DBN.
According to Figure 2, a DBN consists of two parts [29]: prior network B and transition network B... . The prior network defines the joint probability distribution $C_{1}$ of the initial state $B_{1}$ at $t=1$. According to Bayesian inference, the probability formula for the hidden variable $C$ can be written on the prior network as follows:

$$
\mathrm{P}(C \mid A, D)=\frac{\mathrm{P}(D \mid C, A) \mathrm{P}(A \mid C)}{\mathrm{P}(D \mid A)}
$$

The transition network defines the transition probability between $C_{t}$ and $C_{t+1}$ at $t$ and $t+1$, respectively. That is to say, the DBN composed of ( $\mathrm{B} \mid \mathrm{B}_{-t}$ ) is a semi-infinite network structure on $B_{1}, B_{2}, \ldots, B_{t}(t=1,2, \ldots \infty)$. Based on the first-order Markov assumption, the probability of variable $C$ at the next moment only depends on the current moment and is independent of the past moments, that is, $\mathrm{P}\left(C_{t+1} \mid C_{1: t}\right)=\mathrm{P}\left(C_{t+1} \mid C_{t}\right)$. The probability formula for variable a on the transition network can be articulated as follows:

$$
\mathrm{P}\left(C_{1: t}\right)=\prod_{t=2}^{T} \mathrm{P}\left(C_{t} \mid C_{t-1}\right)
$$

The predictive probability distribution of the hidden variable $C$ at cycles $T$ can be obtained by applying the total probability theorem as follows:

$$
P\left(\hat{C}_{T} \mid D_{1: T}\right)=\int P\left(\hat{C}_{T} \mid A_{1: T}, D_{1: T}\right) P\left(A_{1: T} \mid D_{1: T}\right) d A
$$

After obtaining the posterior probability distribution of the variable $C$, posterior updating and prediction of the parameter variable $A$ can be carried out. Within a DBN, the EM algorithm, Monte Carlo method, or the Metropolis-Hastings algorithm is commonly

used for sample parameter selection. However, for models involving long-term observation and updates, multiple iterations might lead to sample impoverishment, resulting in a decrease in accuracy. Therefore, this paper employs a particle filtering algorithm, replacing the backward propagation inference and the update and prediction of parameter $A$, as shown in Equation (7).

In DBNs, the joint probability density function across the time dimension $T$ can be constructed by combining the prior network probability distribution Equation (6) at the beginning of the time series and the state transition network probability distribution Equation (7) between subsequent time points.

$$
\mathrm{P}\left(A \mid C_{1: T}, D\right)=\mathrm{P}(A) \times \mathrm{P}\left(C_{1} \mid A\right) \times \prod_{t=2}^{T} \mathrm{P}\left(C_{t} \mid C_{t-1}\right) \times \mathrm{P}\left(D \mid C_{T}\right)
$$

As shown, it is possible to compute the joint distribution probability of any node in the DBN.

# 2.3. Introduction to Particle Filter 

### 2.3.1. Dynamic Time-Varying System Evolution Equation

Particle filtering (PF), also known as Sequential Monte Carlo, is a general algorithm for the evolution of state variables in DBNs [30]. Particle filtering approximates probability distributions by sampling a set of random samples and then performs statistical calculations on these samples to obtain the minimum variance estimation of the state; these samples are referred to as "particles". As the number of particles increases, the probability density function described by all particles gradually approximates the true probability distribution of the state, achieving the effect of optimal Bayesian estimation.

Assume there is a system, as shown in Figure 3, whose state variable $\boldsymbol{X}_{t} \in R^{m}$ at time $t$ evolves from the state variable $\boldsymbol{X}_{t-1} \in R^{m}$ at time $t-1$ according to the following state function:

$$
\boldsymbol{X}_{t}=f\left(\boldsymbol{X}_{t}, \boldsymbol{v}_{t-1}\right)
$$

where the vector $\boldsymbol{v}_{t-1} \in R^{m}$ represents the noise in the state function.
The observed data $\boldsymbol{Z}_{t} \in R_{n}$ can be obtained via the following measurement function:

$$
\boldsymbol{Z}_{t}=h\left(\boldsymbol{X}_{t}, \boldsymbol{n}_{t}\right)
$$

From the perspective of Bayesian theory, the state estimation problem is to calculate the credibility of the current state $\boldsymbol{X}_{t}$ based on a series of previously available data $\boldsymbol{Z}_{1: t}$ (posterior knowledge) through recursive calculation. This credibility is the probability formula $P\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{1: t}\right)$, which needs to be calculated recursively through prediction and update steps.
![img-2.jpeg](img-2.jpeg)

Figure 3. A state evolution system with noise.
The prediction process uses the system model (i.e., state Equation (9)) to predict the prior probability density of the state, which is to guess the future state through existing prior knowledge, that is, $P(\boldsymbol{X}(t) \mid \boldsymbol{X}(t-1))$. The update process uses the latest measurement value to correct the prior probability density and obtain the posterior probability density, which is to correct the previous guess.

It is assumed that the system's state transition follows a first-order Martov model, that is, the current state $\boldsymbol{X}(t)$ at time $t$ is only related to the previous state $\boldsymbol{X}(t-1)$. At the same time, it is assumed that the data $\boldsymbol{Z}(t)$ measured at time $t$ are only related to the current state $X(t)$, as shown in measurement equation 10 above.

Assuming that the probability density function $P\left(\boldsymbol{X}_{t-1} \mid \boldsymbol{Z}_{1: t-1}\right)$ of time $t-1$ is known, the prediction of the probability of the next state $\boldsymbol{X}(t)$ can be written as follows:

$$
p\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{1: t-1}\right)=\int p\left(\boldsymbol{X}_{t} \mid \boldsymbol{X}_{t-1}\right) p\left(\boldsymbol{X}_{t-1} \mid \boldsymbol{Z}_{1: t-1}\right) d X_{t-1}
$$

where state $\boldsymbol{X}(t)$ is exclusively determined by $\boldsymbol{X}(t-1)$ due to the assumption of first-order Markov processes, i.e., $p\left(\boldsymbol{X}_{t} \mid \boldsymbol{X}_{t-1}, \boldsymbol{Z}_{1: t-1}\right)=p\left(\boldsymbol{X}_{t} \mid \boldsymbol{X}_{t-1}\right)$.

After obtaining the new measurement data $\boldsymbol{Z}_{t}$ at time $t$, the correction of the prediction of formula 10 based on the measurement data can be stated as follows:

$$
p\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{1: t}\right)=\frac{p\left(\boldsymbol{Z}_{t} \mid \boldsymbol{X}_{t}\right) p\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{1: t-1}\right)}{p\left(\boldsymbol{Z}_{t} \mid \boldsymbol{Z}_{1: t-1}\right)}
$$

where $p\left(\boldsymbol{Z}_{k} \mid \boldsymbol{Z}_{1: k-1}\right)=\int p\left(\boldsymbol{Z}_{k} \mid \boldsymbol{X}_{k}\right) p\left(\boldsymbol{X}_{k} \mid \boldsymbol{Z}_{1: k-1}\right) d X_{t}$. The filtering update is now complete.
For generic nonlinear and non-Gaussian systems, it is challenging to arrive at the analytical solution of the posterior probability because the derivation above involves integration for continuous variables. Monte Carlo sampling must be used to address this issue.

# 2.3.2. Monte Carlo Sampling 

The goal of Monte Carlo sampling is to sample the target probability distribution and calculate the target's expected value. When the number of samples $N$ is large enough, the above formula approximates the true probability of winning. The Monte Carlo method is a mathematical method for calculating the odds of multiple possible outcomes occurring in an uncertain process through repeated random sampling.

$$
E\left(f\left(\boldsymbol{X}_{N}\right)\right) \approx \frac{1}{N} \sum_{i=1}^{N} \int f\left(\boldsymbol{X}_{N}\right) \delta\left(\boldsymbol{X}_{N}-\boldsymbol{X}_{N}^{i}\right) d X_{N}
$$

### 2.3.3. Sequential Importance Sampling

The most basic particle filtering algorithm for sampling in posterior probability distribution is Sequential Importance Sampling (SIS) [31]. Assuming that $N$ samples can be sampled from the posterior probability, the calculation of posterior probability can be represented as follows:

$$
P\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{1: t}\right)=\frac{1}{N} \sum_{i=1}^{N} w_{t}^{i} \delta\left(\boldsymbol{X}_{t}-\boldsymbol{X}_{t}^{i}\right)
$$

where $\delta$ is the Dirac function. $w_{t}^{i}$ is the weight of the particle.
In other words, the new state $\boldsymbol{X}_{t}^{i}$ of the $i$ th particle at the time step $t$ is sampled from the distribution with the current state and the observed value $\boldsymbol{Z}_{1: t}$ as parameters.

At time step $t$, the weight $w_{t}^{i}$ is updated from $w_{t-1}^{i}$ to the following:

$$
w_{t}^{i} \propto w_{t-1}^{i} \frac{\mathrm{P}\left(\boldsymbol{Z}_{t} \mid \boldsymbol{X}_{t}^{i}\right) \mathrm{P}\left(\boldsymbol{X}_{t}^{i} \mid \boldsymbol{X}_{t-1}^{i}\right)}{q\left(\boldsymbol{X}_{t}^{i} \mid \boldsymbol{X}_{t-1}^{i}, \boldsymbol{Z}_{t}\right)}
$$

The SIS algorithm has a problem where the variance in the weights $w$ increases with multiple iterations, and it is even possible for one weight to approach 1 while the others tend toward 0 , a phenomenon known as particle degeneracy. This leads to a substantial waste of computational time on the majority of particles with excessively small weights. An effective method to mitigate particle degeneracy is through resampling [32], which involves randomly replicating particles with higher weights and eliminating those with lower weights, thereby focusing the computation as much as possible on particles that have a greater impact on the posterior probability density. In addition, the initial state $\boldsymbol{X}_{0}^{i}$ is sampled from the joint prior distribution of the state variables, and the initial weight $w_{0}^{i}$

of each particle is $1 / N$. The pseudocode for the standard particle filter algorithm flow is as follows:
(1) Particle set initialization, $T=0$ :

For $i=1,2, \ldots, N$. Generate sampling particle $\left\{x_{0}^{i}\right\}_{i=1}^{N}$ from prior $\mathrm{p}\left(x_{0}\right)$.
(2) For $T=1,2, \ldots, t$. Cycle through the following steps:
(1) Importance sampling for $i=1,2, \ldots, N$. The sampling particle $\left\{x_{t}^{i}\right\}_{i=1}^{N}$ is generated from the importance probability density; the particle weight $w_{t}^{i}$ is calculated and normalized.
(2) Resample: Resample the particle set $\left\{x_{t}^{i}, w_{t}^{i}\right\}$. The resampled particle set is $\left\{\widetilde{x}_{t}^{i}, 1 / N\right\}$. The conversion weight $\widetilde{w}_{t}$ is recorded as $\sum_{i=1}^{N} \widetilde{w}_{t}^{i} x_{t}^{i}=\sum_{i=1}^{N} \widetilde{x}_{t}^{i}$.
(3) Output: calculate the state estimation value at time $t, \hat{x}_{t}=\sum_{i=1}^{N} \widetilde{x}_{t}^{i}$.

The process of multiple resamplings tends to replicate particles with higher weights excessively, culminating in a final collection largely made up of identical particles. Such a reduction in the diversity of particles can lead to diminished predictive accuracy, a scenario referred to as particle impoverishment. The conventional approach to mitigate this involves augmenting the initial pool of particles and incorporating new particles throughout the filtering process. However, an increase in the initial particle count significantly escalates computational load, adversely affecting time efficiency. Additionally, the indiscriminate introduction of new particles can infuse the model with fresh uncertainties, impairing its convergence. To address these issues, this study introduces an adaptive strategy for the inclusion of new particles. This strategy leverages the Monte Carlo method to intersperse new particles in every filtering iteration, thereby preserving the diversity of the particle ensemble.

# 2.4. Dynamic Bayesian Network for Fatigue Crack Growth 

Figure 4 shows the structure of a Bayesian network for one time step. The nodes in the figure are all random nodes, indicating that the variable is random given the value of the parent node; therefore, the arrow pointing to it represents the conditional probability distribution (CPD). The variable names and value ranges of the node symbols in Figure 4 are shown in Table 1. Diamond nodes are function nodes, which means that the variable is a deterministic formula calculation result given the value of the parent node; therefore, the arrow pointing to it represents a deterministic function. In addition, elliptical nodes represent continuous variables. Rectangular nodes represent observed variables (such as load and crack length), where $\Theta$ refers to all uncertain material fatigue parameter variables considered in the crack propagation formula.
![img-3.jpeg](img-3.jpeg)

Figure 4. A single-step Bayesian network for crack propagation.

For ease of calculation, all uncertain factors above, except for the initial prior values of fracture toughness, tensile strength, and damage initiation displacement, are assumed to be normal distribution continuous nodes. Usually, load $P$ and crack length $a$ are observable nodes.

Table 1. Bayesian network node variables.


# 2.5. Particle Filter (PF) Equation for Crack Propagation 

### 2.5.1. PF State Equation

The final predicted residual life in the crack propagation model is obtained by the cyclic time at which the crack with initial length $a_{0}$ reaches the critical length $a_{c}$, which can be regarded as a function of $a$. Therefore, the goal of particle filtering is to correct the theoretical value of the accumulated crack length output by the crack propagation formula with experimental data $a_{\text {obs }}$. The estimated crack length in the model is the theoretical length obtained by the crack propagation formula, and $\Theta$ refers to all parameters of the crack propagation formula. The process error is denoted as $v_{a}$, which is zero-mean Gaussian noise from model error. The formula for the state equation can be expressed as follows:

$$
a_{t}=f(\Theta)+v_{a}
$$

This error $v_{a}$ is added after each theoretical crack length at output by the crack propagation formula.

### 2.5.2. PF Measurement Equation

The uncertainty of crack observation data depends on the instrument error of the crack observation and the influence of the simplified conversion of irregular crack shape. It is assumed that the measurement error is zero-mean Gaussian white noise, that is, $\varepsilon_{a} \sim N\left(0, \sigma_{a}^{2}\right)$. The observation data can also be written as $a_{o b s}=a+N\left(0, \sigma_{a}^{2}\right)$, which can prove the following:

$$
p\left(a_{o b s} \mid a\right)=p\left(a \mid a_{o b s}\right)=\frac{1}{\sigma_{a} \sqrt{2 \pi}} \exp \left(-\frac{\left(a-a_{o b s}\right)^{2}}{2 \sigma_{a}^{2}}\right)
$$

Equation (17) is equivalent to

$$
p\left(a_{o b s} \mid a\right) p(a) \propto p\left(a \mid a_{o b s}\right)
$$

Among them, $a$ is the real length of the crack, which is an unknown value. This error is included in the crack measurement data, that is, the real length of the crack $a=a_{o b s}-\varepsilon_{a}$.
$\varepsilon_{a}$ is the measurement error of the crack observation data, which reflects the error between the true value and the measured value of the crack. $v_{a}$ is the model error of the crack propagation formula, which reflects the error between the true value and the simulated value of the crack. Particle filtering selects whether to rely more on measurement data or model data based on their magnitude.

The crack length data are obtained from fiber optic data and experimental annotations, which brings two sources of uncertainty: measurement error and data sparsity. Similar to the uncertainty of the load, the measurement error in the crack length data depends on the accuracy of the annotation and the processing of the non-uniform crack equivalent length on the layered surface, usually assumed to have a zero-mean Gaussian distribution $\varepsilon_{a} \sim N\left(0, \sigma_{a}^{2}\right)$. This method can also handle other measurement error distributions. Since crack observation requires manual collection by instruments, crack length data are rarely applicable for every time step. Even if a data point is obtained after each observation and applied to the DBN for diagnosis and prediction, data sparsity introduces data uncertainty.

# 2.6. Adaptive Particle Filter Correction Method Based on DBN Reasoning 

In traditional filtering processes, state equations are often invariant. However, when there is a substantial error between the state equation and the actual state, the predictive accuracy and convergence speed of the filtering may not be ideal. This difference becomes minimal with continuous experimental data input, but in the absence of such data, predictions still exhibit a certain level of deviation. This deviation is particularly noticeable when experimental data are scarce. Additionally, traditional filtering fails to derive correction coefficients for the theoretical formulas associated with the filtering outcomes. To ensure the state equation is continuously updated during the filtering process, it is essential to adjust the parameters of the state equation using the filtering results from each time step. Moreover, to overcome the issue of particle depletion seen in traditional particle filtering, an adaptive sampling approach is introduced.

Assuming the use of Paris' law, the specific state evolution Equation (9) and observation Equation (10) in Section 2.3.1's particle filtering formula can be respectively represented as follows:

$$
\begin{gathered}
a_{t}=a_{t-1}+C(\Delta K)^{m} \cdot \Delta N+v_{a}^{t} \\
a_{t}^{o b s}=a_{t}+\varepsilon_{a}^{t}
\end{gathered}
$$

where $a_{t}$ represents the calculated crack length at time $t$, and $a_{t}^{o b s}$ is the observed crack length at number of cycles $t . v_{a}^{t}$ and $\varepsilon_{a}^{t}$ denote the model error and measurement error at number of cycles $t$, respectively.

Then, through the SIS sampling and resampling described in Section 2.3.3, we can obtain the posterior estimate of the crack length at number of cycles $t$ as $\hat{a}_{t}=\sum_{i=1}^{N} \widetilde{w}_{t}^{i} a_{t}^{i}$, where $a_{t}^{i}$ represents the sample values from particle filtering and $\widetilde{w}_{t}^{i}$ denotes the resample weights of the samples. Similarly, we can obtain the posterior estimate of the parameter $\hat{\Theta}_{t}$ as $\hat{\Theta}_{t}=\sum_{i=1}^{N} \widetilde{w}_{t}^{i} \Theta_{t}^{i}$, where $\Theta_{t}^{i}$ is the parameter corresponding to the particle filtering crack length samples $a_{t}^{i}$.

Utilizing the kernel density estimation approach enables us to derive the probability distributions of the posterior estimates for $\hat{a}_{t}$ and $\hat{\Theta}_{t}$, thus facilitating the DBN model's update. Following this, the refreshed posterior parameters $\hat{\Theta}_{t}$ will act as the preceding parameters $\Theta_{t+1}$ for the forthcoming DBN filtering stage in the crack propagation equation. In accordance with their probability distribution, new samples for the time $t+1$ are recreated using the Monte Carlo method, paving the way for subsequent updates to the model.
$f(\cdot)$ represents the crack propagation formula. The whole process is shown in Figure 5:

![img-4.jpeg](img-4.jpeg)

Figure 5. The DBN filter inference iteration.

# 2.7. DBN Whole Frame 

This paper proposes an adaptive DBN particle filter, which uses a crack propagation formula as the system state equation of particle filtering and uses material parameters, observed cracks, and loads as input continuous node random variables. The steps of the DBN can be represented as follows:

Step 1. Through the examination of accessible materials (for instance, simulations of identical structures or fatigue expansion formulas), extensive prior data on lifespan under diverse conditions of load, stress ratio, and fracture toughness among other parameters are acquired. These data act as the preliminary parameters $\Theta_{0}$ for the crack propagation equation. Subsequently, initial particles are generated from the prior probability distribution $P(\Theta)$ associated with these parameters by employing the Monte Carlo method, which initiates the values for each node within the DBN.

Step 2. Once the monitoring of crack propagation in structures commences, the equivalent stress $\Delta \sigma$ at the crack tip is determined from the observed load $P_{o b x}^{t}$. This value, together with additional prior parameters $\Theta^{t}$, is incorporated into the crack propagation equation to derive the theoretical crack length at present, $a_{t}$. Subsequently, this theoretical figure and the observed experimental data also serve as the basis for the state and measurement equations in particle filtering. Employing the adaptive particle filtering technique outlined in Section 2.6, particle filtering facilitates the acquisition of the posterior estimates for the current crack extension length $\hat{a}_{t}$ and the parameters $\hat{\Theta}_{t}$.

Step 3. Following the acquisition of posterior parameter samples $\hat{\Theta}_{t}$ at moment $t$, the probability distribution of $\hat{\Theta}_{t}$ undergoes sampling via kernel density estimation. This process inputs the derived samples into crack propagation, serving as the prior update for the crack length particles at the forthcoming moment $t+1$. This step facilitates the retrieval of the next posterior filtering values $a_{t+1}$.

The structure of the overall DBN is shown in Figure 6. The uncertainties mentioned above in the DBN are represented by the nodes in the figure. Nodes are connected by arrows representing conditional probability distributions or deterministic functional relationships. The subscript $t-1$ or $t$ represents the time step.

In this section, the DBN model for crack propagation is validated using both single and multiple adaptive variable datasets. Section 3.1 describes the DBN model for crack propagation with a single adaptive variable. In contrast, Section 3.2 presents the DBN model for crack propagation incorporating multiple adaptive variables.

![img-5.jpeg](img-5.jpeg)

Figure 6. The framework of the DBN for the prediction of fatigue crack propagation.

# 3. Fatigue Crack Propagation Experiment Verification 

### 3.1. Single Adaptive Variable DBN Model

To validate the feasibility of the proposed method, three-point bending fatigue experiments were conducted using three specimens, as shown in Figure 7a. The dimensions of the specimens are $120 \times 30 \times 15 \mathrm{~mm}^{3}, 160 \times 40 \times 15 \mathrm{~mm}^{3}$, and $240 \times 60 \times 15 \mathrm{~mm}^{3}$, with the support span $S$ being $L-0.4 \times W$. The material of the specimens is AL6061 aluminum alloy, with an elastic modulus, $E$, and Poisson's ratio, $v$, of 69.6 GPa and 0.33 , respectively. The bending fatigue limit of the material is around 100 MPa . The initial crack length, $a_{0}$, is 10 mm , where the length of the prefabricated notch is 9 mm , and the crack length initiated by cyclic loadings, according to ASTM E1820, is 1 mm . According to ASTM E399 standards [33], the material's fracture toughness $K_{I C}$ was measured to be 34 MPa . The stress ratio $R$ is 0.2 , with maximum loads of $4500 \mathrm{~N}, 6000 \mathrm{~N}$, and 9000 N . The load magnitudes make the maximum stresses at the lower sides of the specimens (without considering the crack) nearly equal (around 54 MPa ).
![img-6.jpeg](img-6.jpeg)

Figure 7. (a) Specimen dimensions; (b) picture of the actual specimens; (c) picture of three-point bending fatigue experiment.

3.1.1. Data Analysis

The crack propagation a-N curves [34] for the three specimens are shown in Figure 8. According to ASTM E399, the stress intensity factor, $K$, for three-point bending specimens is calculated using

$$
K=\frac{3 P S}{2 B W^{2}} \sqrt{a} \frac{1.99-\xi(1-\xi)\left(2.15-3.93 \xi+2.7 \xi^{2}\right)}{(1+2 \xi)(1-\xi)^{\frac{3}{2}}}
$$

where $\xi=a / W$ with $a$ as the crack length; $P$ is the load amplitude. Letting $K=K_{\mathrm{IC}}$, the critical crack lengths, $a_{\mathrm{C}}$, of the three specimens were calculated as $20.6,26.2$, and 36.3 mm , respectively. And the measured values of $a_{\mathrm{C}}$ are $20.5,25.9$, and 36 mm . It can be seen that the measured critical crack lengths in Figure 8 are highly consistent with those calculated theoretically.
![img-7.jpeg](img-7.jpeg)

Figure 8. Three-point bending fatigue $a-N$ curve.
In addition, fractographs were taken of the fracture sections of the three specimens and are shown in Figure $9 \mathrm{a}-\mathrm{c}$. The areas indicating the stages of steady crack propagation and sudden specimen fracture can be well distinguished from the figures, and the regions with the distance of $a_{\mathrm{c}}$ from the lower edge of the specimens exactly locate the transition between these two stages.
![img-8.jpeg](img-8.jpeg)

Figure 9. Fractographs of the three specimens with dimensions of (a) $120 \times 30 \times 15 \mathrm{~mm}^{3}$, (b) $160 \times 40 \times 15 \mathrm{~mm}^{3}$ and (c) $240 \times 60 \times 15 \mathrm{~mm}^{3}$.

Paris' law was used as the state equation for particle filtering. Based on the experimental data, the parameters of Paris' law were obtained based on data fitting. Specifically, the value of $m$ in Paris' law is approximately 3.34 , and $C$ ranges from $5 \times 10^{-11}$ to $7 \times 10^{-11}$. Within the context of the DBN, the logarithmic of parameter $C$ is treated as a variable subject to uncertainty. For particle filtering purposes, it is initially represented by a set of uniformly distributed particles. These particles are then subject to passive, adaptive updates in sync with the revisions of the DBN model. To verify the correction ability of the method, observation was started after several cycles and DBN tracking instead of starting from scratch.

# 3.1.2. Uncertainty Sources Considerations 

In the DBN, the error analysis of crack propagation is focused on two primary aspects: model errors and measurement errors. The model errors, particularly those arising from the limitations of Paris' law, are identified as the core of the analysis. This includes the intrinsic limitations of the formula and the effects of structural defects on the accuracy of material parameter estimations and equivalent stress calculations, which together lead to deviations in performance evaluation. The measurement errors, such as noise from measuring instruments, irregularities in crack paths and shapes, and non-standard operations during the loading process, also significantly impact the accuracy of the assessment. To address these challenges, the DBN in this study considers the following main uncertainty factors:

1. Equivalent stress at crack tip.

The equivalent stress is obtained from the calculation of alternating load, and there are errors in the selection of stress intensity criteria, structural defects, and load observation noise. According to experience, it is assumed that the variance of this error is within $10 \%$, so the normal distribution of $10 \%$ variance is taken in this paper.
2. The error of the parameter $m$ for Paris' law.

The parameter $m$ in Paris' law is influenced by geometric defects in the structure and material properties, leading to significant variability even within the same material and structure [35]. Therefore, in this study, based on the variability observed in experiments, the initial values of several specimens were averaged and subjected to a Gaussian distribution [36]. Subsequently, after applying filtering and DBN inference, the distribution range of the modified samples was determined through kernel density estimation.
3. Uncertainty of crack length.

The length of the crack mainly exists in the measurement error of the crack increment in the experiment and the numerical calculation error caused by the non-uniform crack length on the left and right sides as well as the internal crack length. This error is fitted to the binary curve in line with its own trend according to the data, and the fitting variance of the measured data points is taken as $4.6 \%$ [37].

The parameter $m$, serving as a parameter variable within the DBN, undergoes adaptive updates following each round of filtering, whereas other uncertain elements remain unchanged, manifesting merely as errors within the particle filtering process. An initial measurement error is presumed to be $10 \%$. Due to the incremental growth of the crack per cycle being considerably minor in comparison to the initial crack, each subsequent crack increment incorporates an additional $5 \%$ measurement error and system process error.

### 3.1.3. Model Results and Data Graphs

The first $90 \%$ of the cycle times are taken as the observation data of this method, and the last $10 \%$ are taken as the verification of accuracy. The change in the uncertainty parameters obtained according to DBN reasoning after filtering is shown in Figure 10. The notation "log $(\cdot)$ " denotes an operation using the natural logarithm.

As can be observed from Figure 10, the uncertainty range of parameter $C$ is quickly narrowed after the first filtering. This demonstrates the efficacy of the DBN in facilitating node adjustment. With the model being updated step by step, the uncertainty range of $C$ steadily decreased, converging after approximately $4-5$ iterations. The updated value was very close to the measured data.
![img-9.jpeg](img-9.jpeg)

Figure 10. Prediction results of parameter $m$ for the spcimens with dimensions of (a) $120 \times 30 \times 15 \mathrm{~mm}^{3}$, (b) $160 \times 40 \times 15 \mathrm{~mm}^{3}$ and (c) $240 \times 60 \times 15 \mathrm{~mm}^{3}$.

The final crack propagation prediction of the DBN particle filter is shown in Figure 11. Due to the scarcity of crack observation data, if there is no observation value in the current time step, the prediction value will be used instead.
![img-10.jpeg](img-10.jpeg)

Figure 11. Prediction results of fatigue crack propagation for the spcimens with dimensions of (a) $120 \times 30 \times 15 \mathrm{~mm}^{3}$, (b) $160 \times 40 \times 15 \mathrm{~mm}^{3}$ and (c) $240 \times 60 \times 15 \mathrm{~mm}^{3}$.

As shown in Figures 11 and 12, due to the lack of observational data, the fatigue crack growth and remaining life were significantly underestimated in the first 2-3 filtering processes, with prediction errors reaching as high as $20 \%$ to $30 \%$. With the continuous collection of observational data, the uncertainty in the DBN was updated, thereby gradually improving the prediction accuracy. Especially when the filtering process exceeded six iterations, the prediction error for the residual life of specimens could be maintained below $5 \%$, which has practical implications for the safety assessment and maintenance of structures.

![img-11.jpeg](img-11.jpeg)

Figure 12. Prediction results of residual lives for the spcimens with dimensions of (a) $120 \times 30 \times 15 \mathrm{~mm}^{3}$, (b) $160 \times 40 \times 15 \mathrm{~mm}^{3}$ and (c) $240 \times 60 \times 15 \mathrm{~mm}^{3}$.

# 3.2. Multiple Adaptive Variables DBN Model 

To provide additional evidence regarding the effectiveness of the DBN particle filter, experiments from Zheng [38] were utilized to continue the validation process.

The single-edge crack growth test material is domestically sourced commercial galvanized high-strength steel wire, with a diameter of 7 mm .

For finite-width, equal-thickness strip specimens with unilateral cracks, the calculation formula for the crack form factor $F$ can be obtained from the Stress Intensity Factor Manual, as shown below:

$$
F=1.12-0.234\left(\frac{a}{b}\right)+10.55\left(\frac{a}{b}\right)^{2}-21.72\left(\frac{a}{b}\right)^{3}+30.39\left(\frac{a}{b}\right)^{4}
$$

where $a$ is the crack length and $b$ is the specimen width.
Zheng adopts the Walker law as the prediction formula for crack propagation [27].

$$
\frac{d a}{d N}=C\left[(1-R)^{a} \Delta K\right]^{m}
$$

The experiment collected separate data on crack propagation at stress ratios $R=0.1$, $R=0.5$, and $R=0.7$. The parameter $m$ of Paris' law is 3.3. The crack propagation data under a 220 MPa load were utilized as the validation dataset for the DBN model, as depicted in Figure 13. The author performed a parameter fitting process to determine the values of parameters $C$ and $\alpha$; the obtained values were approximately $7 \times 10^{-13}$ and -0.3 , respectively, with a survival rate of $95 \%$.
![img-12.jpeg](img-12.jpeg)

Figure 13. Single-edge crack growth test specimen.

The parameters in Table 2 are utilized as sources of uncertainty for the DBN particle filter. The parameters $C$ and $m$ are adaptively updated in the DBN model update. The mean and variance of sampling for other uncertain variables remain unchanged.

Table 2. DBN uncertain variables.


The prediction results of the DBN particle filter are shown in Figure 14.
![img-13.jpeg](img-13.jpeg)

Figure 14. Crack propagation $d a / d N$ curves under different stress ratios $R$.
Figure 15 demonstrates that the adaptive DBN model is equally capable of accurately forecasting the actual progression of crack expansion across varying stress ratios. In comparison to the three-point bend model examined in Section 3.1, there are less observational data available for this section's single-edge crack model. Additionally, the uncertain variable parameter $\Theta$ within the Walker law is not linear but includes a power exponent variable, which magnifies the errors. When utilizing the initial model to predict crack expansion reliability, the overlapping uncertainties of various model parameters $\Theta$ lead to a wider range of predicted crack intervals. This range only narrows, adopting a "trumpet" shape, after incorporating the next batch of observational data, which prompt an update in the model's state. Following this update, the precision of crack predictions improves, and the uncertainty interval diminishes, demonstrating that the update enables the particles to more closely mimic the true probability distribution between two observational points. As predictions advance, the estimates increasingly diverge from the actual conditions, and the uncertainty interval expands accordingly. This expansion results from the model's uncertainty propagation, which continually escalates the prediction errors, highlighting the importance of ongoing crack monitoring and frequent updates to the model's state.

Figures 16 and 17 showcase the variations in the probability distribution of Walker model parameters.

![img-14.jpeg](img-14.jpeg)

Figure 15. Crack propagation prediction under different stress ratios (a) $R=0.1$; (b) $R=0.5$; (c) $R=0.7$ [38].
![img-15.jpeg](img-15.jpeg)

Figure 16. Updated parameters $C$ under different stress ratios (a) $R=0.1$; (b) $R=0.5$; (c) $R=0.7$ [38].
![img-16.jpeg](img-16.jpeg)

Figure 17. Updated parameters $\alpha$ under different stress ratios (a) $R=0.1$; (b) $R=0.5$; (c) $R=0.7$ [38].
As depicted in Figure 16, the values of $C$ predicted by the DBN and given in [38] are slightly different, where the predicted values are lower at $R=0.5$ and 0.7 and higher at $R=0.1$. This is because the $C$ value in [38] was averaged among three experiments with different stress ratios, whereas the predicted values based on the DBN are obtained based on each individual experiment. The deviation in $C$ is mainly attributed to the dispersion in material properties. In general, the average of the predicted values is consistent with that in [38]. For $\alpha$, the predicted value is basically consistent with that in [38], as can be seen in Figure 17.

# 4. Discussion 

This paper presents a crack propagation prediction model using a DBN, suitable for effective tracking of damage evolution in aerospace structures. The method is validated

using experimental data from three-point bending and single-edge crack tension tests. The results show that through DBN particle filtering, the uncertainty interval for crack propagation in the three-point bending specimen decreased from $24 \%$ to $6 \%$, as shown in Figure 11, and the prediction error for the lifespan was also reduced from over $30 \%$ to lower than $5 \%$, as shown in Figure 12. In the single-edge crack experiment, although multi-source uncertain variables increased the uncertainty interval of crack propagation, the error range of the filtered uncertainty interval gradually decreased, and the prediction error for the uncertain variables, $\Theta$, also exhibited the trend of gradual decrease and convergence. This indicates that the DBN filtering can track and correct time-dependent variables (crack length) and reduce the uncertainty of time-independent variables (parameter $\Theta$ ).

By comparing the single adaptive variables and multiple adaptive variables in the two examples, it is evident that the convergence of the variables in particle filtering decreases along with the enlarged dimension of the uncertain variable space. One potential reason for this is that the interdependence and nonlinear effects among parameters increase the complexity of the system. With multiple parameters involved, the update of each parameter depends not only on its own observed data but may also be influenced by the states of other parameters. This leads to multiple possible solutions within the parameter space. A possible solution includes the improvement method of marginalizing some uncertain variables (such as the Rao-Blackwellized particle filtering method), which is a direction for future research.

As the model is continuously updated, both the parameter variables and the predicted cracks will gradually converge. However, when new uncertainties suddenly emerge, causing significant changes in the prediction outcomes, the variation in parameter means and uncertainty intervals will increase sharply until the new factors stabilize. Subsequently, the uncertainty interval gradually decreases to a new state of convergence.

# 5. Conclusions 

This study introduces a probabilistic approach for health diagnosis and prognosis through an adaptive DBN framework. This framework employs DBNs to predict health conditions and is characterized by its capability to adaptively update parameter probability distributions and regenerate new particle samples, while integrating various sources of inference and cognitive uncertainty. It is suitable for structural health diagnosis and fatigue crack growth prediction under uncertain conditions. The particle filtering algorithm is utilized within the DBN for Bayesian inference to calibrate the physical model. The proposed method has been validated through two experimental data examples, confirming its advantages: (1) It can track the evolution of time-related state variables and reduce uncertainty variables in time-independent states (diagnosis). (2) It allows for the selfcalibration of parameter probability distributions and prediction structures through realtime updates, forecasting fatigue crack growth and residual life probabilistically (prognosis), demonstrating excellent stability and robustness. (3) Adaptive updating and regeneration of particles prevent particle depletion, rendering the model's outcomes more realistic compared to traditional particle filtering results.

In addition, the current model also has some limitations for future enhancement. Firstly, the model's capability is limited to tracking single crack damage, overlooking the interaction and combined effects of multiple crack damages. Secondly, the experimental scenarios used in the model are relatively simple. In contrast, the operational environment of aerospace structures is evidently more complex, posing challenges for accurate simulation and prediction.

Author Contributions: Conceptualization, S.C. and M.L.; methodology, S.C. and Z.W. (Zhanjun Wu); validation, S.C. and Z.W. (Zhongshu Wang); formal analysis, Y.M. and Z.W. (Zhongshu Wang); investigation, S.C.; resources, Y.M. and Z.W. (Zhanjun Wu); data curation, S.C.; writing—original draft preparation, S.C.; writing-review and editing, M.L. and Z.W. (Zhanjun Wu); visualization, S.C. and Z.W. (Zhongshu Wang); supervision, Y.M. and Z.W. (Zhanjun Wu); project administration, Y.M.

and Z.W. (Zhanjun Wu); funding acquisition, Y.M. and Z.W. (Zhanjun Wu). All authors have read and agreed to the published version of the manuscript.

Funding: The authors received funding for this study from the National Key R\&D Program of China (2018YFA0702800) and the National Natural Science Foundation of China (12072056). This study is also supported by the National Defense Fundamental Scientific Research Project (XXXX2018204BXXX).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflicts of interest.
