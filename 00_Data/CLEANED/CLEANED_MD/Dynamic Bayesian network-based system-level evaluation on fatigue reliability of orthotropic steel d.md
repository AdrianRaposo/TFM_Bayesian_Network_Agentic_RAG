# UNIVERSITYOF BIRMINGHAM University of Birmingham Research at Birmingham 

## Dynamic Bayesian network-based system-level evaluation on fatigue reliability of orthotropic steel decks

Heng, Junlin; Zheng, Kaifeng; Kaewunruen, Sakdirat; Zhu, Jin; Baniotopoulos, Charalampos

DOI:
10.1016/j.engfailanal.2019.06.092

License:
Creative Commons: Attribution-NonCommercial-NoDerivs (CC BY-NC-ND)

Document Version
Peer reviewed version
Citation for published version (Harvard):
Heng, J, Zheng, K, Kaewunruen, S, Zhu, J \& Baniotopoulos, C 2019, 'Dynamic Bayesian network-based systemlevel evaluation on fatigue reliability of orthotropic steel decks', Engineering Failure Analysis, vol. 105, pp. 12121228. https://doi.org/10.1016/j.engfailanal.2019.06.092

Link to publication on Research at Birmingham portal

## Publisher Rights Statement:

Heng, J, Zheng, K, Kaewunruen, S, Zhu, J \& Baniotopoulos, C. (2019) 'Dynamic Bayesian network-based systemlevel evaluation on fatigue reliability of orthotropic steel decks', Engineering Failure Analysis, vol. 105, pp. 1212-1228. https://doi.org/10.1016/j.engfailanal.2019.06.092

## General rights

Unless a licence is specified above, all rights (including copyright and moral rights) in this document are retained by the authors and/or the copyright holders. The express permission of the copyright holder must be obtained for any use of this material other than for purposes permitted by law.
-Users may freely distribute the URL that is used to identify this publication.
-Users may download and/or print one copy of the publication from the University of Birmingham research portal for the purpose of private study or non-commercial research.
-User may use extracts from the document in line with the concept of 'fair dealing' under the Copyright, Designs and Patents Act 1988 (?) -Users may not further distribute the material nor use it for the purposes of commercial gain.

Where a licence is displayed above, please note the terms and conditions of the licence govern your use of this document.
When citing, please reference the published version.

## Take down policy

While the University of Birmingham exercises care and attention in making items available there are rare occasions when an item has been uploaded in error or has been deemed to be commercially or otherwise sensitive.

If you believe that this is the case for this document, please contact UBIRA@lists.bham.ac.uk providing details and we will remove access to the work immediately and investigate.

# Dynamic Bayesian network-based system-level evaluation on fatigue 

## reliability of orthotropic steel decks

Junlin Heng ${ }^{1,2}$, Kaifeng Zheng ${ }^{1}$, Sakdirat Kaewunruen ${ }^{2}$, Jin Zhu ${ }^{1}$ and Charalampos Baniotopoulos ${ }^{2}$


#### Abstract

${ }^{1}$ Department of Bridge Engineering, School of Civil Engineering, Southwest Jiaotong University, Chengdu 610031, China ${ }^{2}$ Department of Civil Engineering, School of Engineering, University of Birmingham, Birmingham B152TT, United Kingdom


#### Abstract

Fatigue fractures can be frequently observed in welded joints in orthotropic steel decks (OSDs) after just a few decades of operation, which become the major deterioration mechanism deterring the serviceability of OSDs. In this paper, a novel dynamic Bayesian network (DBN) model has been established for the fatigue reliability analysis of OSDs at system-level. The exact inference algorithm is applied in the DBN model with discrete variables. Special modifications have been made on the existing algorithm to improve the computational efficiency in dealing with the deck system which consists of a considerable number of joints. Using the DBN model, the fatigue reliability of welded joints can be predicted and updated with the inspection and monitoring results at system-level. At the same time, a framework is established for the system-level reliability considering the fatigue fracture of rib-to-deck (RD) joints, the dominant cracking pattern affecting the serviceability of OSDs. For illustration, a typical OSD bridge in China has been selected to carry out a case study. To derive the stress spectrum required by the DBN model, the stochastic traffic model is employed, and the influence-based Monte Carlo simulations have been carried out. As a result, the fatigue reliability can be predicted at both component- and system-levels. Meanwhile, the observation of the traffic and the inspection result has been fused into the DBN model to update the deteriorating state of the deck system. Besides, the effect of enhancement and maintenance has been highlighted, including the

enhancement in fatigue strength at the construction stage, and the repair and traffic control during the operation stage.

Keywords: orthotropic steel deck; fatigue reliability; system-level evaluation; dynamic Bayesian network; stochastic traffic model.

# 1. Introduction 

Orthotropic steel decks (OSDs) have been extensively used in modern steel bridges, because of their advantages such as light self-weight, speedy construction and so on [1]. Under the continuous loading of vehicles passing through the deck, fatigue damage will accumulate in welded joints of OSDs and eventually lead to fatigue fractures, which is the critical deterioration mechanism of OSDs [2]. Besides, due to the large number of welded joints adopted in OSDs, the fatigue-induced deterioration has become the major cause degrading the serviceability of OSDs.

Generally, the fatigue damage is highly stochastic, due to the significant uncertainties in fatigue strength (resistance) and vehicle loads (loading effects). Thus, if fatigue evaluation is performed in a deterministic manner, it may deviate from the stochastic nature and lead to inaccurate results [3]. A feasible way is to evaluate fatigue performance in a probabilistic way, i.e., fatigue reliability analysis [4]. In recent years, extensive efforts have been conducted by many researchers on the aspect. Kwon and Frangopol [3] proposed a method for fatigue reliability assessment of steel bridges incorporating the field-measured stress spectrum, in which fatigue strength and stress ranges were treated as random variables. Case studies were performed for the critical details in two bridges, and the remaining life was estimated by setting target reliability. Guo et al. [5] proposed a probabilistic traffic model through the statistics on the measured data. Finite element model was established to transfer the traffic model into the stress ranges of critical details, which were then used in the reliability analysis. Lu et al. [6] employed the machine learning method to derive the stress spectrum using the stochastic traffic model. Monte Carlo simulations were then applied to calculate the fatigue reliability of critical details. Zhou et al. [7] conducted statistics on the vehicle loads collecting from four bridges in different regions of France. The lateral position of vehicles was measured and analysed. Based on that, probabilistic traffic model was established, and stress spectra were derived.

As stated above, these studies mainly focused on the fatigue reliability analysis at component-level, in which the number of details has been ignored. However, this may lead to inaccurate results, since the deck system consists of various details. For instance, fatigue fractures are more likely to be observed in a structural system consisting of 1,000 fatigue-critical details than the one with only one fatigue-critical detail. Currently, few publications could be found on the fatigue reliability of OSDs at the system-level. Maljaars and Vrouwenvelder [8] established a probabilistic fatigue damage model for the critical detail in OSDs, using the presumed stress spectra. The multiple presences of similar details were considered by treating the OSD as a pure series system consisting of components with the same failure rate. The results suggested that the reliability of 100 similar details was significantly lower than that of a single detail.

Usually, the crude Monte Carlo method is used in the reliability analysis due to its concision and flexibility [6][9]. However, its computational efforts would gradually become intractable when the failure rate reaches a small value. The problem can be ameliorated to some extent by using the advanced Monte Carlo methods such as importance sampling, directional sampling, and adaptive sampling. However, these methods also have their limitations and sometimes become infeasible [10]. Alternatively, approximation methods such as first/second order reliability methods (FORM/SORM) can be employed [11]. Nonetheless, when the limit state function is highly nonlinear, the accuracy and computational efficiency of these methods will significantly decrease [12]. Also, the above methods are unable to perform reliability updating and information fusion, which further restrict their applications. Even if these tasks could be partly performed by Monte Carlo simulations with conditional probability, the computational cost would become incredibly high [8].

Recently, to overcome the above difficulties, the Bayesian network (BN) methodology has been proposed as an effective framework for reliability assessment at system-level. The BN is particularly suitable for system reliability assessment because it enables the uncertainty propagation and updating through nodes/components in the network that allows the transformation of information from the system-level to component-level. Straub [13] proposed a general dynamic Bayesian network (DBN) framework for the reliability analysis of deterioration processes. The study suggested that the computational efficiency and robustness in prediction and updating made the DBN particularly

suitable for the reliability analysis of deterioration processes. In the next, Luque and Straub [14] extended the general framework to the system-level reliability analysis of deteriorating systems. Zhu et al. [15] established a DBN model for the fatigue assessment of a single detail in OSDs. The particle filer-based approximation inference algorithm was used, and the result showed that the DBN model is capable to predict and calibrate the fatigue damage of OSDs.

The objective of this paper is to evaluate the fatigue reliability of orthotropic steel decks (OSDs) at system-level. A DBN model has been established for the system-level fatigue reliability of OSDs, aimed at the prediction, information-based fusion and evidence-based update. In the model, the exact inference algorithm has been employed with discrete variables. Special modifications have been made on the existing algorithm to improve the computational efficiency in dealing with the large-scale deck system consisting of massive fatigue-critical details. Meanwhile, a framework of system-level reliability has been established for OSDs basing on the serviceability. In the DBN model, the fatigue action is considered by the combination of random traffic volume and deterministic stress spectrum. In deriving stress spectra, the stochastic traffic model has been employed incorporating with the multi-scale finite element model. Through employing the influence-surface technology, samplingbased analysis has been performed with a large sample-size to obtain comprehensive stress spectra.

Based on the established method, a typical OSD bridge in China has been selected to carry out a case study. At first, the fatigue reliability of the deck is predicted without monitoring results, and the effect of strength enhancement has been analysed. Meanwhile, the fusion of observed traffic information has also been illustrated with the model. After that, two types of inspection results have been considered to update the model, i.e., the non-detection and the detection of fatigue cracks. Finally, the effect of treatment approaches on the deteriorated deck system has been investigated, including the maintenance and traffic control.

## 2. Development of DBN for OSDs at system-level

### 2.1 Capability of DBN in modelling the deteriorating process

The dynamic Bayesian network (DBN) is a powerful probabilistic tool originated in computer science [16], which is naturally suitable for modelling the deterioration process in structures. Fig. 1

shows a simple model of DBN, in which X stands for the variables in the state space, such as material properties and loading effects; Z stands for the evidence of current states, e.g. damage state.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Constructed mesh of sample model.
With the DBN model, several probabilistic tasks could be conducted using various algorithms [17]. Among them, the following three tasks are commonly involved in the deterioration analysis:
(1) prediction: the task is to predict the possible state of the system in the future time slice $t$, as shown in Eq. 1.

$$
\operatorname{Pr}\left(\boldsymbol{X}_{t}\right)=O\left(\operatorname{Pr}\left(\boldsymbol{X}_{t-1}\right)\right)=\cdots=O^{t}\left(\operatorname{Pr}\left(\boldsymbol{X}_{0}\right)\right) \#(1)
$$

where the symbol $O$ stands for the operation function of state transition between time slices; the symbol $O^{t}$ indicates the state transition is repeated for $t$ times.
(2) information-based fusion: the task is to fuse the new information about the state space (e.g. the new physical model or probabilistic model) into the DBN model at the specific time slice, based on the previous state, as shown in Eq. 2.

$$
\operatorname{Pr}\left(\boldsymbol{X}_{t+1}\right)=O^{\prime}\left(\operatorname{Pr}\left(\boldsymbol{X}_{t}\right)\right) \#(2)
$$

Where the symbol $O^{\prime}$ represents the state transition using the fused model.
(3) evidence-based updating: the task is to update the probability distribution of the state space with the evidence, as shown in Eq. 3.

$$
\operatorname{Pr}\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{t}\right) \propto \operatorname{Pr}\left(\boldsymbol{X}_{t}\right) * \operatorname{Pr}\left(\boldsymbol{Z}_{t} \mid \boldsymbol{X}_{t}\right) \#(3)
$$

Where symbol $\propto$ stands for similarity between the two ends of the equation, and the exact value could be solved by normalization; $\operatorname{Pr}\left(\boldsymbol{Z}_{t} \mid \boldsymbol{X}_{t}\right)$ is the likelihood factor representing the possibility of evidence $\boldsymbol{Z}_{t}$ under the assumed state $\boldsymbol{X}_{t}$.

By performing the Eq. 3 recursively, the updated probability distribution of state space could be obtained basing on evidence over the past time slices from 0 to $t$, i.e., $\operatorname{Pr}\left(\boldsymbol{X}_{t} \mid \boldsymbol{Z}_{0: t}\right)$. In addition, performing the Eq. 1 on this basis, the prediction at the future time slice $T$ could be made with the updated model, i.e., $\operatorname{Pr}\left(\boldsymbol{X}_{T} \mid \boldsymbol{Z}_{0: t}\right)$, where $t<T$.

# 2.2 Construction of the DBN model for OSDs 

### 2.2.1 Deterioration model of fatigue damage

Several approaches are available for fatigue assessment of welded joints, which could be classified into two categories: damage factor-based stress-life (S-N) approach and crack size-based fracture mechanics (FM) approach [18][19]. The FM approach is close to the cracking nature and able to consider the sequence effect of loads. However, high computational efforts are usually required in FM approaches, which makes it somehow intractable for the system-level reliability problem. Meanwhile, with the well-established database, the S-N approach could also generate satisfactory results in engineering problems. Thus, an advanced S-N approach, the hot spot stress approach, has been applied [20]. The two-stage model proposed by Eurocode 3 [21] has been applied, and the fatigue deterioration model is derived, as shown in Eqs. 4a and b.

$$
\begin{gathered}
D_{i, t}=\left\{\begin{array}{lll}
\left(\frac{\Delta \sigma_{i}}{\Delta \sigma_{D}}\right)^{m_{1}} \cdot \frac{n_{i, t}}{N_{D}}, & \Delta \sigma_{i} \leq \Delta \sigma_{D} \\
\left(\frac{\Delta \sigma_{i}}{\Delta \sigma_{C}}\right)^{m_{2}} \cdot \frac{n_{i, t}}{N_{C}}, & \Delta \sigma_{i}>\Delta \sigma_{D}
\end{array} \#(4 a)\right. \\
D_{\text {sum }}(t)=\sum_{t} \sum_{i} D_{i, t} \#(4 b)
\end{gathered}
$$

where $D_{i, t}$ is the damage increment induced by the stress block $\Delta \sigma_{i}$ at the time slice $t ; n_{i, t}$ is the corresponding number of cycles; $\Delta \sigma_{C}$ and $\Delta \sigma_{D}$ are respectively fatigue strength at 2 million cycles and 5 million cycles; $m_{1}$ and $m_{2}$ are the power indexes for the stage 1 and the stage 2 , which equal to 3 and 5 , respectively; $N_{C}$ and $N_{D}$ equal to 2 million and 5 million, respectively; $D_{\text {sum }}(t)$ is the total damage factor at the time slice $t$.

In the model, the stress block $\Delta \sigma_{i}$ and corresponding cycle $n_{i, t}$ represent the vehicle-induced stress ranges, which will be discussed later in the derivation of stress spectra. The fatigue strength parameters $\Delta \sigma_{C}$ and $\Delta \sigma_{D}$ can be determined by the strength model in the design code [21] or the numerical analysis [22]. In the S-N approach, failure is achieved when the damage factor reaches a specific value. To this end, the limit state function could be established, as shown in Eq. 5.

$$
g(D, t)=\Delta-D_{\text {sum }}(t) \#(5)
$$

where $\Delta$ is the accumulation factor and assumed as 1.0 in this study.

In the deterioration model, the uncertainties originate from both the resistance (i.e. the fatigue strength) and action (i.e. the stress ranges induced by vehicle loads). The fatigue strength is treated as a time-invariant random variable $R$. In the case of fatigue action, a high traffic volume is generally expected over the time slice (e.g. half million per year per lane). Due to Borel's law of large numbers [23], the proportion of each stress range approximates to the actual probability with the increase in traffic volume. On this basis, the fatigue action is represented by the deterministic stress spectrum and the random traffic volume. Meanwhile, the stress spectrum is solved under the stochastic model with a large sample-size to reflect the diversity of stress ranges, which will be illustrated in detail later. The traffic volume is represented by the average daily traffic (ADT), derived from the traffic model in codes or by observation.

# 2.2.3 Hyper parameter-based correlation 

The welded joints in OSDs are usually fabricated by the steel in the same grade (or even the same production batch) by the same manufacturer, using similar welding technology and quality assurance. Meanwhile, those joints will experience the same traffic during the operation. Due to the above factors, it will result in the correlation between state variables of joints. Two types of correlations have been considered: (1) the correlation in fatigue strength; (2) the correlation in ADT. To simulate the correlations, the hierarchical model with hyper-parameters has been applied [14]. The variables are considered as equally correlated, which have the mutual correlation coefficient $\rho_{X}$ and identical marginal distribution. To interrelate the variables statistically, an uncertain common hyperparameter $\alpha$ has been introduced, which follows the standard normal distribution. Basing on that, the cumulative distribution function (CDF) of each variable is assumed to be conditional on the hyperparameter, as shown in Eq. 6.

$$
F_{X \mid \alpha}(x)=\Phi\left(\frac{\Phi^{-1}\left[F_{X}(x)\right]-\sqrt{\rho_{U}} * \alpha}{\sqrt{1-\rho_{U}}}\right) \#(6)
$$

where $\Phi$ and $\Phi^{-1}$ are respectively the CDF and inverse CDF of the standard normal distribution; $F_{X}(x)$ is the marginal CDF of the variables in the correlated set; $\rho_{U}$ is the correlation coefficient in the standard normal space.

The coefficient $\rho_{U}$ could be determined from the marginal $\operatorname{CDF} F_{X}(x)$ and the original coefficient $\rho_{X}$, as shown in the literature [24]. In the case of ADT, the condition $\rho_{X}=1$ could be assumed, i.e., perfectly correlated.

# 2.2.4 Construction of the DBN for OSDs 

Basing on the above analysis, the DBN model has been constructed for the system-level fatigue reliability of OSDs, as shown in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Fig. 2. DBN model for fatigue damage of joints in OSDs.

Two types of nodes have been employed in modelling: (1) the random node with an elliptical box; (2) the deterministic node with a rectangular box. The notations of nodes are summarised in Table 1. Meanwhile, the solid arrow represents the inner-relation between different nodes in the same time slice, while the dashed arrow stands for the inter-relation between the same nodes in two adjacent time slices.

Table 1 Notations in the DBN model


# 2.3 Computation algorithm of the proposed DBN model 

### 2.3.1 Discrete DBN with exact inference

Generally, DBNs could be classified into two categories by the type of nodes: (1) continuous DBN consisting of continuous variables; (2) discrete DBN consisting of discrete variables. Meanwhile, various algorithms have been proposed for the two types of DBNs [25]. Obviously, the continuous DBN is perfectly suitable for fatigue deterioration since most of the variables are naturally continuous. However, the inference algorithms developed for continuous DBNs are generally sampling-based [17], in which the computational efficiency decreases rapidly with the increase in the number of nodes and the decrease in the probability of interest (e.g. the probability of failure). The OSD system consists of a considerable number of joints with a low failure rate, for which the continuous DBN is not feasible. Alternatively, the discrete DBN with the more efficient exact inference has been applied in this study, whose feasibility has already been proved in literature $[14][26]$.

### 2.3.2 Likelihood-based parallel updating method

In the discrete DBN, the frontier algorithm is extensively used due to its concision and flexibility [16]. In the method, the state transition is conducted through sweeping the joint probability, called as the frontier, across the network. When evidence is available, e.g. the observation of cracks in structural members, the DBN model can be automatically updated as shown in Eq. 3. A notable feature of the method is that the joint probability of the entire state space will be constructed during the transition, which makes it computationally intractable in dealing with the large-scale system. Take a system consisting of $m$ components as an example. If each component has $N$ possible states, the computational complexity could be regarded as $O(N)$. Moreover, the system will approximately have a complexity of $O\left(N^{m}\right)$, which will increase exponentially with the number of components $m$. Thus, the frontier algorithm has been modified according to the features of the established DBN.

Since the joint probabilities of the components are connected through the shared hyperparameters only, the original frontier algorithm could be adapted to a parallel-solving way. To achieve that, the concept of the component-level frontier is introduced: the frontier containing only the state of one component and the shared hyper-parameters. At the beginning of each solving step, these

frontiers are parallelly transferred. During the transition, the component-level likelihood could be solved for the hyper-parameters, based on the evidence of the $i$ th component, as shown in Eq. 7,

$$
L_{i, t}=\operatorname{Pr}\left(F_{i, t}^{\prime} \mid \boldsymbol{\alpha}\right)=\frac{\operatorname{Pr}\left(\boldsymbol{\alpha} \mid F_{i, t}^{\prime}\right)}{\operatorname{Pr}(\boldsymbol{\alpha})} \#(7)
$$

where $L_{i, t}$ stands for the component-level likelihood of the $i$ th component; $\boldsymbol{\alpha}$ is the vector of hyperparameters, which are $\left(\alpha_{R}, \alpha_{N}\right)$ in this study; $F_{i, t}^{\prime}$ denotes the evidence of the failure state of the $i$ th component.

After that, the component-level frontiers could be parallelly updated by the evidence of other components, as shown in Eq. 8,

$$
\operatorname{Pr}\left(\boldsymbol{X}, \boldsymbol{\alpha} \mid F_{1: m, t}^{\prime}\right) \propto \prod_{\{1: m\} /\{i\}} L_{i, t} * \operatorname{Pr}\left(\boldsymbol{X}, \boldsymbol{\alpha} \mid F_{i, t}^{\prime}\right) \#(8)
$$

where $\boldsymbol{X}$ is the vector of state space, including the nodes $R_{i, t}, N_{i, t}, D_{i, t}, F_{i, t}$ in this study; $m$ is the number of components in the system; $\{1: m\} /\{i\}$ means the assemble from 1 to $m$ except $i$.

# 3. System-level framework for fatigue reliability of OSDs 

### 3.1 Case study: a typical OSD bridge in China

Among all the welded joints, fatigue fracture is frequently observed in the rib-to-deck (RD) joints. Two primary reasons could be attributed to: (1) the wheel loads directly acting on the deck will cause high-level local stresses in the joints; (2) the RD joint accounts for the largest proportion of welded joints in OSDs. Meanwhile, the fatigue cracking in RD joints may lead to severe consequences: the serviceability of the bridge would be directly affected, and it may even pose a threat to the safety of passing vehicles. From the perspective of serviceability, the fatigue cracking of RD joints could be regarded as the dominated cracking pattern of OSDs [27]. To this end, the RD joint is focused when establishing the framework of system-level fatigue reliability for OSDs. For illustration, a typical OSD bridge in China has been selected to carry out a case study, which is called as the prototype bridge, as shown in Fig. 3.

The prototype bridge has a total length of 158 m , consisting of a middle-span of 68 m and two side-spans of 45 m . The deck system of the bridge is divided into 112 segments, carrying three lanes

with 15 U-ribs. The details about the bridge are shown in Table 2. For illustration, the U-ribs are named as U1 U15 with a footnote of ' $L$ ' or ' $R$ ' representing the left or right joint of the U-rib.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Fatigue cracking pattern of the prototype bridge

Table 2 Basic parameters of the object bridge


# 3.2 Development of the system-level framework 

As aforementioned, the deck system consists of considerable RD joints. Thus, the state of all the joints should be considered in describing the state of the system. However, the combination of component states will become incredibly large, which makes the system-level analysis almost impossible. Take a deck system consisting of $N$ joints as an example. If each joint has two states (i.e., $0=$ not failure, $1=$ failure), the deck system will have $2^{N}$ possible states, which is an intractable NPhard problem. Thus, it is essential to find out a more efficient way to represent the fatigue deterioration state of the deck system. Two unique features of the deck system could be utilized: (1) the deck is able to work with the presence of limited cracks due to the high redundancy [28]; (2) fatigue cracking of RD joints is more of a serviceability problem rather than the safety issue, which will not cause catastrophic structural failures directly. Thus, the conception of Daniel system has been

applied, in which the number of failed components in the system is employed to represent the state of the system [29].

Generally, the deck system is divided into a series of segments by the floor beams. Thus, the deck system can be idealised as a multi-level framework, as shown in Fig. 4. By assuming that cracking in any joint will cause misfunction of the entire segment, the segment is modelled as a series system consisting of several RD joints. As a result, the failure of segments is achieved after the failure of any RD joint. Meanwhile, the cracking in one segment will have little influence on other segments as the deck system is highly redundant [28][30]. On this basis, the deck system is modelled as a parallel system of the segments, whose deterioration state is represented by the number of failed segments.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Framework of the system-level reliability
Basing on the limit state function shown in Eq. 5, the probability of failure of the $m$ th joint could be expressed as Eq. 9,

$$
\operatorname{Pr}\left[F_{J, m}(t)=1\right]=\operatorname{Pr}\left[g_{J, m}(D, t) \leq 0\right] \#(9)
$$

where the subscript ' $J$ ' is abbreviated for joint while the subscript ' $m$ ' is the sequence number of the joint; $F_{J, m}(t)$ stands for the fatigue damage state of the $m$ th joint in the segment at time $t$, with the value of 1 or 0 representing failure or not failure respectively; $g_{J, m}(D, t)$ is the limit state function of the $m$ th joint at time $t$.

After that, the failure probability of the segments could be derived under the assumption of the series system, as shown in Eq. 10.

$$
\operatorname{Pr}\left[F_{\text {seg }, n}(t)=1\right]=\operatorname{Pr}\left[\bigcup_{m} F_{f, m}(t)=1\right]=1-\prod_{m}\left(1-\operatorname{Pr}\left[F_{f, m}(t)=1\right]\right) \#(10)
$$

where $F_{\text {seg }, n}$ stands for the failure state of the $n$th segment, in which value 0 or 1 stands for not failure and failure respectively.

Above all, the failure probability of the system is defined as the probability that the number of failed segments is no less than a specific value, as shown in Eq. 11,

$$
P_{f, x y s}(t, k)=\operatorname{Pr}\left[N_{f, \operatorname{seg}}(\mathrm{t}) \geq k\right]=\operatorname{Pr}\left[\sum_{n} F_{s e g, n}(t) \geq k\right] \#(11)
$$

where $N_{f, \text { seg }}$ stands for the number of failed segments; $k$ is the number of expected failed segments.
Correspondingly, the system-level reliability also reflects the probability that the number of failed segments is no more than $k$. It is worth stating that the value $k$ should be determined based on the expectation on the serviceability of bridges. It also associates with the decision-making process of the inspection and maintenance plan [31], which is outside the scope of this study. Alternatively, an empirical failure percentage $k / n$ of $30 \%$ has been used in this study, after consulting both the senior structural engineers, manufacturers and bridge management authorities.

# 4. Stress spectrum analysis using stochastic traffic model 

### 4.1 Stochastic traffic model

### 4.1.1 Framework of the stochastic traffic model

As stated before, the stress spectrum is crucial information in the fatigue analysis. With the help of advanced monitoring systems, the stress spectrum could be established directly by monitoring [3][32]. However, because of the limitation on budget and feasibility, the monitoring system could not be extensively applied. Alternatively, the structural analysis with traffic models could be employed. Under this approach, the accuracy of spectra dependents on the rationality of the applied traffic model. In the code-specific design, the stress spectrum is represented by the effective stress range solved with the deterministic truck model [21][33]. Meanwhile, a series of correction factors are used to consider the uncertainties in traffic [34][35][36]. Obviously, this deviates from the stochastic nature of the traffic loads and may lead to inaccurate results [3] [37].

To overcome the problem, the stochastic traffic model has been applied to derive stress spectra. The traffic could be considered as the assembly of random vehicles passing through the bridge in various lateral positions stochastically. On this basis, the framework of the stochastic traffic model could be established, including both the model of vehicles and their lateral distribution. Since the stress of RD joints is directly determined by vehicles [1], the model is parametrised in detail with axle numbers, axle spacing, wheel tracks, axle weights, and footprints. Meanwhile, the lateral distribution of vehicles is described by lane occupancy rates and the in-lane position. Besides, the traffic volume is described by the average daily traffic (ADT). The parameters in the framework are summarised in Table 3. The distribution of parameters could be determined after either codes and specifications, or field observation, which will be discussed later.

Table 3 Parameters in the framework of the stochastic traffic model


# 4.1.2 Data source of the stochastic traffic model 

After the innovative framework of stochastic traffic is established, the parameters could be determined from two main sources: (1) the existing data in publications such as codes and specifications; (2) direct measurements by monitoring systems. Obviously, the data from the sitespecific measurements could reflect the real traffic on the specific bridge more accurately, which could in turn narrow down the uncertainties. However, this type of data is unavailable before the implementation of monitoring systems. Besides that, the availability of data is also associated with the number of sensors in the monitoring system. In this case, the capability of DBNs in information-based fusion could be utilised. At first, the default traffic model could be established based on existing data, which is subsequently used to derive the original stress spectra. Whenever more data are available, the traffic model could be easily updated to obtain the new stress spectra. Then the new spectra could be fused into the DBN model to evaluate time-dependent fatigue reliability.

In the study, the default model is first established with the standard truck model defined in Eurocode (EC) 1 [34], as shown in Fig. 5. In the model, a deterministic 4 -axle truck is used as the representative of vehicles, in which the impact factor has been already included. Meanwhile, EC1 suggests that in the lanes predominantly used by cars (i.e. the fast lane and middle lane), the truck traffic number could be considered as $10 \%$ of the number in the slow lane. On this basis, the occupancy rate of the standard truck could be determined, which is also included in Fig. 5.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Standard truck model proposed in Eurocode 1
As aforementioned, the lateral position associates with both the occupancy rate and the in-lane position. In the study, the distribution proposed in EC1 is used for the in-lane lateral position. To facilitate its application in numerical simulation, the discrete distribution has been transformed into a normal distribution, as shown in Fig. 6.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Distribution of the in-lane lateral position
When the new traffic model is available, the new stress spectra can be derived and fused into the DBN model. For illustration purpose, an observed traffic model measured in another typical OSD bridge in China has been considered. Table 4 shows some basic information about the model, while details could be found in the article [38].

Table 4 Vehicle types and occupancy in the observed model


Since the in-lane position was not provided in the observed model, it keeps the same with the one depicted in Fig. 6. Meanwhile, the footprints of tire have been adjusted as per the Chinese code [39], which are respectively $0.3 \times 0.2 \mathrm{~m}$ for front axles and $0.6 \times 0.2 \mathrm{~m}$ for rear axles. Besides, an impactor factor of 1.15 is considered [33].

# 4.2 Influence surface-based stress spectrum analysis 

### 4.2.1 Multi-scale finite element model

To transfer the traffic model into stress spectra, a multi-scale finite element (FE) model has been established for the prototype bridge in ANSYS software [40], as shown in Fig. 7.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Multi-scale finite element model of the prototype bridge
Generally, fatigue cracking of RD joints is mainly induced by the transverse stress, on which the longitudinal location of segments has little influence [1]. Since all the segments of the OSD have identical geometry, the joints in the same lateral position of different segments will have similar stress spectra. Thus, the segment in the midspan is selected as the representative to derive the spectra. The FE model consists of three parts in different meshing sizes: (1) the global model of the bridge structure, simulating the boundary condition of the selected segment; (2) the sub-model of the selected segment, served as a link between the relatively coarse global model and the highly refined detail model; (3) the detail model of RD joints, in which the minimum element size is gradually refined to 1

mm near the joints. The 3-dimensional shell element is used, and only half of the joints are refined with the detail model due to the symmetry of the deck.

# 4.2.2 Influence surface-based calculation 

Based on the established model, Monte Carlo (MC) simulations are employed to derive the stress spectrum from the traffic model. To obtain the comprehensive spectra, a large sample-size, e.g. $10^{5}$, is required even if stratified sampling is used. Besides, the computational cost is relatively high to derive the vehicle-induced stress history from the FE model directly. For instance, it may require 100 or more solving steps to calculate the stress history induced by just one vehicle. Thus, it becomes computationally intractable with the large sample size. Thus, the influence-surface technology has been used. Through a series of FE analysis, the influence-surface of RD joints could be established. Fig. 8 shows the result of the joint $\mathrm{U} 12_{\mathrm{L}}$, which is unitized after the maximum response for better illustration. In the next, the stress history could be solved by direct superposition of the influencesurface according to the configuration of vehicles, which is much more computationally efficient.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Influence-surface of the rib-to-deck joint $\mathrm{U} 12_{\mathrm{L}}$
The calculation process is shown in Fig. 9. At first, a large-size database of vehicles, i.e. $10^{7}$ in this study, can be established through sampling according to the stochastic traffic model. FE analysis is then performed to generate the influence-surface of each joint. After that, a Monte Carlo-based program has been coded in MATLAB [41] to solve the stress history from the traffic data using the influence-surface. Finally, the database of stress history is transformed into stress spectra using cyclecounting methods such as the rain flow approach [42].

![img-8.jpeg](img-8.jpeg)

Fig. 9. Calculation process of the stress spectrum
The stress spectrum of the RD joint U12L in the slow lane has been shown in Figs. 10a and b, which are respectively solved under the standard truck model and the observed model.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Stress spectra of the joint $\mathrm{U} 12_{\mathrm{L}}$ : (a) standard truck model; (2) observed model.
For better demonstration, the stress ranges with a small possibility are truncated in Fig. 10b. The result shows that under both models, the low-level stress ranges (less than 15 MPa ) account for the largest proportion. Meanwhile, the observed model could generate a more even and continuous spectrum, compared with that induced by the standard truck model. This is because the standard truck model only considers the lateral position as the random variable, while the observed truck model includes many other random variables such as the vehicle type, axle weight, etc. Obviously, the observed model can provide an in-depth consideration of the randomness in the traffic at the site.

# 5. Reliability analysis using the established DBN model 

### 5.1 Distributions of input random variables

In the DBN model, the fatigue strength and traffic volume are input random variables, and the correlation between joints should be considered. As a common practice [3][5][38][43], the fatigue strength $R$ is assumed to follow the lognormal distribution. According to Eurocode 3 [21], the design strength at two million cycles could be considered as 100 MPa for RD joints, which is derived under the $97.7 \%$ survival rate. Meanwhile, the coefficient of variation (COV) of $R$ could be derived after the COV of the material constant proposed in [44]. Through the COV, the relation between the mean and standard deviation could be established, as shown in Eq. 12 .

$$
\sigma_{X}=\mu_{X} \cdot V_{X} \#(12)
$$

Where $\sigma_{X}$ stands for the standard deviation of the variable $X ; \mu_{X}$ and $V_{X}$ are respectively mean value and COV of $X$.

Basing on the above data, the mean value and standard deviation of $R$ could be solved. The detailed procedures could be referred to literature [18]. Meanwhile, the correlation coefficient could be determined by Eq. 13.

$$
\rho_{X}=1-\frac{V_{X, f}^{2}}{V_{X, p}^{2}} \#(13)
$$

Where $\rho_{X}$ is the mutual correlation coefficient of variable $X ; V_{X, f}$ and $V_{X, p}$ are respectively the COV of the entire distribution and the distribution within one deck.

In this study, the $V_{X, f}$ of fatigue strength is determined after the model in Eurocode 3 [21] since it is established on a large-scale testing database. Meanwhile, the testing data from the article [27] are used to calculate the $V_{X, p}$, in which the specimens are fabricated by the same manufacturer with the steel in the same grade.

As aforementioned, the average daily traffic (ADT) is used to represent the traffic volume. For the standard traffic model, the mean value of ADT is determined after the estimation of traffic category 2 in Eurocode 1 [34], i.e. $0.5 \times 10^{6}$ per slow lane per year, representing the highway with a medium rate of trucks.

426 At the same time, a COV of 0.2 is determined after the article [45] and then used to calculate the standard deviation, as shown in Eq. 12. In the case of the observed model, the mean value is solved after the measured data [38], while the same COV is applied to derive the standard deviation. As stated before, the ADT of each joint is assumed to be perfectly correlated. Thus, the value 1.0 is used for the correlation coefficient of the ADT. The input random variables are summarised in Table 5.

Table 5 Distribution of input random variables


*: ST and OB respectively stand for the standard truck model and the observed model

# 5.2 Results and discussions 

### 5.2.1 Prediction using the standard truck and observed model

According to codes of practice [21][39], a design life of 100 years has been considered in the study. The prediction has been made using both the standard truck model and the observed model for comparison purpose. Figs. 11a and b show the results of component-level reliabilities, which only include the joints with initial reliability less than 8 for better illustration. According to JCSS [46], targeting reliability indexes of 2.3 and 1.3 could be used for the service limit state when the costs of enhancement are respectively high and low. Thus, two lines have also been used as the safety lines in the comparison of component-level reliability (denoted as the upper and lower safety line for distinction), below which the component is considered unreliable.

In the case of the standard truck model, only the curve of the most critical joint $\mathrm{U} 12_{\mathrm{L}}$ crosses the upper line after 37 years and then the lower line after 92 years. In the case of the observed model, despite that the curve of $\mathrm{U} 12_{\mathrm{L}}$ crosses the lines at similar times, the curve of $\mathrm{U} 9_{\mathrm{R}}$ also crosses the upper line after 63 years but remains above the lower line until the end of design life. Meanwhile, the curves solved with the observed model are more scattered than those solved with the standard truck model, since the consideration of randomness in vehicles is more comprehensive in the former model.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Component-level reliability: (a) standard truck model; (b) observed model.
The system-level reliability has also been calculated using the framework established in section 3. As stated before, an empirical value of failure percentage $k / n=30 \%$ is used. For comparison, analysis has also been made for the situation $k=1$, i.e., failure of the system occurs after the first cracking in any segment. The results are shown in Figs. 12a and b. Contrary to the comparison of componentlevel reliability, $\beta=2.3$ is used as the only safety line in the comparison of system-level reliability.
![img-11.jpeg](img-11.jpeg)

Fig. 12. System-level reliability solved with two different assumptions: (a) first cracking in any segment; (b) failure percentage of $30 \%$.

Under both assumptions of failure, the reliability solved by the observed model is slightly lower than the one solved by the standard truck at the beginning. Then, the difference in the two curves increases with time and reaches its peak at the end of design life. In the case of the first cracking, the two curves cross the safety line before 20 years and then gradually decrease to minus after around 40 years. Thus, it suggests that fatigue cracking is highly possible to occur in OSDs during the service life due to the considerable number of RD joints, especially under the heavy truck traffic. In the latter

assumption, the lower curve solved by the observed model is still above the safety line at the end of design life, illustrating that it is reliable that the proportion of failure segments will not exceed $30 \%$. Meanwhile, the observed model demonstrates the conservativeness in the system-level analysis and is then employed as the default model in the following analysis if not specified.

# 5.2.2 Enhancement of fatigue strength 

According to Eqs. 4 and 5, the fatigue reliability of the OSDs can be improved by enhancing the fatigue strength. To achieve that, innovative details and fabrication technologies could be employed [47][48]. In the study, the application of an innovative U-rib, named thickened edge U-rib (TEU), has been investigated [48]. According to the test results, the strength of RD joints could be enhanced by $20 \%$ by using TEUs. On this basis, the analysis is made with improved strength, and the results are compared in Figs. 13a and b.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Reliability with and without strength enhancement: (a) component-level; (b) system-level.
Two critical joints, $\mathrm{U} 9_{\mathrm{R}}$ and $\mathrm{U} 12_{\mathrm{L}}$, are selected for the comparison of component-level reliability. With the enhancement, the reliability curves move up significantly. As a result, only the reliability curve of $\mathrm{U} 9_{\mathrm{R}}$ becomes slightly lower than the upper safety line after almost 90 years. At the end of design life, the two reliability indexes are increased by about $50 \%$. In the case of system-level reliability, at first, the difference is relatively small between the two curves, while it increases rapidly with time. At the end of design life, the system-level reliability index is increased by more than $100 \%$. To summarise, a moderate enhancement in fatigue strength, i.e. $20 \%$, could lead to significant improvement in fatigue reliability at both component- and system-level. Thus, proper design and fabrication are vital to the fatigue reliability of OSDs.

As aforementioned, the established DBN can fuse new information into the evaluation model at any time when it is available. The investigation has been made on the fusion of traffic models, in which the standard truck model and the observed model are used. In the analysis, the observed model is assumed to be available after ten years and then fused into the model basing on the previous state. The reliability index solved with information fusion is plotted against the one without information fusion in Fig. 14. The result shows that after the fusion, a significant increase could be found in the deterioration rate, i.e. the gradient of reliability curve. As a result, the reliability index finally reaches a lower value at the end of design life. Thus, it is vital to consider the up-to-date traffic model to obtain an accurate reliability index.
![img-13.jpeg](img-13.jpeg)

Fig. 14. System-level reliability with the information-based fusion.

# 5.2.4 Evidence-based updating 

The most important feature of the DBN lies in the capability in automatic evidence-based updating, i.e., to calibrate the model using inspection results. Since the partial inspection has been proved to have little effect [8], the full inspection is considered in the study, i.e., all the RD joints are checked in one inspection. The deck system is assumed to be inspected three times at the 30th, 50th and 70th years. Two scenes of inspection results are considered, i.e., non-detection and detection of cracks.

The reliability index updated with the non-detection results (i.e. fatigue crack is not detected in all the three inspection) has been plotted against the index without inspection in Fig. 15. The reliability index is increased after each inspection since no crack is detected. Meanwhile, the

deterioration rate (i.e. the gradient of the curve) increases suddenly after the inspection and gradually decreases to the normal level. It is worth noting that after the last two inspections, the reliability becomes higher than the value after the first inspection. This can be attributed to the updating in the posterior distributions of fatigue strength and ADT.
![img-14.jpeg](img-14.jpeg)

Fig. 15. System-level reliability with the information-based fusion.
The posterior distributions of the fatigue strength and ADT after inspections are derived, as shown in Fig. 16a and b. The result shows that after each inspection, the distribution of strength will move to the right side while that of ADT will move to the left side.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Posterior distribution updated with no detection of cracks: (a) fatigue strength; (b) average daily traffic (ADT).

Thus, the non-detection results indicate a higher value of strength and a lower value of ADT. In other word, the strength is underestimated while the ADT is overestimated in the prior distributions. Since the fatigue deterioration is an accumulation process, the update in posterior distribution will

have effects throughout the whole time slices. As a result, it can lead to a reliability index much higher than the one previously predicted, as is the case in Fig. 15.

The situation that fatigue cracks are detected has also been analysed. The cracks are assumed to be observed in different segments, to account for the most critical situation. Table 6 shows the considered inspection results.

Table 6 Inspection results considered in the case of detection


Based on the results, the updated reliability index can be calculated, as shown in Fig. 17. Before the second inspection, the reliability is the same as the one with the non-detection results, since no crack is observed until then. After the second inspection, the reliability only slightly increases since crack is observed in several joints, while the deterioration rate increases significantly. After the third inspection, the reliability experiences a slight increase while the deterioration rate becomes even higher. As a result, the inspected curve decreases below the uninspected curve and safety line after 75 years and 85 years, respectively. Finally, the reliability index decreases to almost zero at the end of design life. 536 537

Fig. 17. System-level reliability updated with the detection of cracks. Similarly, the posterior distributions are also derived, as shown in Fig. 18a and b. After the first inspection, the changes in the distributions are identical to the previous result with the non-detection results. However, since cracks are found in the next two inspections, the distribution of strength

moves to the left while that of ADT moves to the right. These changes indicate the overestimation in strength and the underestimation in ADT. At the same time, the change in the reliability could also be explained by the updated posterior distributions: (1) the reliability increases since most of the joints are not cracked when inspected; (2) the deterioration rate rises since the lower strength and high traffic volume are expected.
![img-16.jpeg](img-16.jpeg)

Fig. 18. Posterior distribution updated with the detection of cracks: (a) fatigue strength; (b) ADT. Based on the above analysis, the DBN model is capable of self-calibration through inspection results. Even if the prior distributions are not well established, they could be gradually adjusted with the input of inspection results. As a result, a good accuracy could be still reached for the reliability prediction.

# 5.2.5 Effects of treatment approaches 

After the cracking problem becomes significant, treatment approaches can be employed to maintain the reliability of OSDs. Two general treatments are investigated, including maintenance and traffic control. At first, maintenance is assumed to be carried out after the last inspection when the cracking problem affects the safety risk after the last inspection. In the assumption, the cracked joint can be fully repaired after the maintenance, i.e., recovered to the initial state. On this basis, the reliability has been solved, as shown in Fig. 19. The reliability increases significantly after the maintenance. At the end of design life, the reliability index is much higher than the safety line. Meanwhile, the two curves are almost parallel, indicating that the maintenance has little influence on the deterioration rate. This could be attributed to the following factors: (1) only the cracked joints are

manipulated through the maintenance; (2) the maintenance will not change the distributions of strength and ADT, which determine the deterioration rate.
![img-17.jpeg](img-17.jpeg)

Fig. 19. System-level reliability with and without maintenance.
In the engineering practice, there are cases that maintenance cannot be carried out due to various reasons such as the lack of budget, the difficulties in maintenance, the disturbance on daily traffic, and so on. Alternatively, traffic control could be applied as a backup approach. Two types of controls have been investigated, including the control on the vehicle weight and the control on the traffic volume.

At first, the average vehicle weight is assumed to be reduced by $10 \%$ due to the weight control. Analysis has been made using the information-based fusion of the DBN model, as shown in Fig. 20. It could be found that the deterioration rate significantly decreases after weight control. As a result, the reliability curve finally reaches a value above the safety line at the end of design life.
![img-18.jpeg](img-18.jpeg)

Fig. 20. System-level reliability with and without weight control
Analysis has also been made on the situation when the traffic volume is reduced by $20 \%$ due to the traffic volume control, as shown in Fig. 21. A similar trend could be found, and the reliability curve also reaches the value above the safety line at the end of design life.

![img-19.jpeg](img-19.jpeg)

Fig. 21. System-level reliability with and without traffic volume control
However, traffic control should only be considered the second choice even if the reliability could be maintained at an acceptable level. To some extent, it could also be seen as a special type of degradation of serviceability, since the function of the bridge is intendedly restricted. Instead, the maintenance seems to be a suitable choice. However, as aforementioned, maintenance does not affect the uncracked joint and the deterioration rate. Thus, if the deck system is poorly designed and fabricated, extensive efforts of maintenance are required to keep the reliability at a satisfied level. Recalling the investigation on the enhancement in fatigue strength, an important conclusion could be drawn here: it is crucial to prevent the fatigue cracking by the reasonable design and elaborate fabrication, instead of the maintenance and traffic control conducted after significant cracking.

# 6. Concluding remarks 

In this paper, a novel dynamic Bayesian network (DBN) model has been proposed for the systemlevel evaluation on the fatigue reliability of orthotropic steel decks (OSDs). With the model, three major tasks could be facilitated: prediction, information-based fusion, and evidence-based updating. The inference algorithm used in the model has been adapted to enable the analysis of the large-scale deck system with a considerable number of joints. After that, a system-level framework is established for the fatigue reliability of OSDs, based on the serviceability of the deck system. For illustration, a typical OSD bridge in China has been selected to carry out a case study. To derive stress spectra required by the reliability analysis, the stochastic traffic model is employed with Monte Carlo simulations. Two types of traffic models have been considered, the standard truck model and the observed model, which respectively stand for the prior and posterior knowledge about the traffic.

Finally, the selected bridge has been investigated using the proposed approach. According to the analyses, some important conclusions could be drawn as follows:

- Fatigue fracture is highly possible to occur in OSDs during the service life because a considerable number of welded joints are adopted, especially under the heavy truck traffic. However, OSDs can work with the presence of limited cracks because of their high redundancy. Thus, a framework of fatigue reliability at system-level is established basing on the number of cracked segments of OSDs, to reflect the serviceability of the deck system.
- A moderate enhancement in fatigue strength of rib-to-deck joints may lead to significant improvement in the fatigue reliability at both the component-level and system-level. As discussed in the study, if the strength has been increased by $20 \%$, the system-level reliability will be increased to more than two times at the end of design life, while the component-level reliability of two critical joints will be increased to around $150 \%$ at the end. Compared with the treatments such as maintenance and traffic control, special cares should be taken at the design and fabrication stage to improve the fatigue reliability.
- Through the information fusion of the observed traffic model, it demonstrates the importance of considering the real-time change in the traffic model. Meanwhile, the DBN model has been updated with the two types of inspection results. The analysis indicates that reliability could change significantly with the inspection results. Thus, proper inspections should be carried out for OSDs, through which the prediction could be auto-calibrated.
- Maintenance could be performed to maintain the reliability of OSDs after significant cracking has been found. After the proper maintenance, the reliability could be notably increased. However, the effort of maintenance has little influence on the deterioration rate, which is determined by fatigue strength and traffic volume. Thus, if the deck system is poorly designed and fabricated, extensive efforts must be made to keep its reliability at a satisfied level.
- Traffic control could be applied as an alternative approach when maintenance is difficult to be conducted. Two types of controls have been considered, including the control on vehicle weight and the control on traffic volume. As a result of controls, the deterioration rate decreases, and the

reliability could be maintained at an acceptable level. However, traffic control should be treated as a backup approach only, since the function of the bridge is intendedly restricted.

- Of the most engineering concerns, the OSD can provide a 100-year service life with the proper design, fabrication, inspection and maintenance during the whole lifetime.


# Acknowledgements 

633 The study is supported by the National Natural Science Foundation of China (grant number: 51778536, Doctoral Innovation Fund Program of Southwest Jiaotong University (grant number: DCX201701), the Zhejiang Department of Transportation (grant number: 10115066), China Scholarship Council and British Council through the Newton Fund. Special thanks to European Commission for H2020-MSCA-RISE Project No. 691135 "RISEN: Rail Infrastructure Systems Engineering Net-work" (www.risen2rail.eu).
