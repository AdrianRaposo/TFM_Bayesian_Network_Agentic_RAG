# Article 

## Optimal Sensor Deployment for Parameter Estimation Precision by Integrating Bayesian Networks in Wet-Grinding Systems

Kang $\mathrm{He}^{1}$, Bo Wu ${ }^{1}$, Fei Sun ${ }^{1}$, Quan Yang ${ }^{1}$ and Huichao Yang ${ }^{2, *}$


#### Abstract

check for updates Citation: He, K.; Wu, B.; Sun, F.; Yang, Q.; Yang, H. Optimal Sensor Deployment for Parameter Estimation Precision by Integrating Bayesian Networks in Wet-Grinding Systems. Appl. Sci. 2023, 13, 7140. https://doi.org/10.3390/ app13127140

Received: 14 April 2023
Revised: 8 June 2023
Accepted: 12 June 2023
Published: 14 June 2023


## (0) 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /)$.


#### Abstract

1 High-end Micro-nano Grinding Equipment School—Enterprise Collaborative Innovation Engineering Center, Suzhou University, Suzhou 234000, China; szuhek@ahszu.edu.cn (K.H.); szxywb@ahszu.edu.cn (B.W.); sunfly@ahszu.edu.cn (F.S.); szxyyq@ahszu.edu.cn (Q.Y.) ${ }^{2}$ Kangni Research Institute of Technology, Nanjing Institute of Technology, Nanjing 211167, China * Correspondence: hcyang@njit.edu.cn


#### Abstract

Accurately and efficiently determining a system's physical variables is crucial for precise product-quality control. This study proposes a novel method for optimal sensor deployment to increase the accuracy of sensing data for physical variables and ensure the timely detection of the product's particle size in a wet-grinding system. This approach involves three steps. First, a Bayesian network (BN) is designed to model the cause-effect relationship between the physical variables by applying the path model. The detectability is determined to confirm that the mean shifts of all the physical variables are identifiable using sensor sets in the wet-grinding system. Second, the sensing location of accelerometers mounted on the chamber shell is determined according to the coupled computational fluid dynamics-discrete element method simulations. Third, the shuffled frog leaping algorithm is developed by combining the BN to minimize the maximum data output deviation index among all sensor sets and sensory costs; this is achieved under the constraints of the mean shift detectability, achieving optimum sensor allocation. Subsequently, a case study is performed on a zirconia powder production process to demonstrate that the proposed approach minimizes the requirements of the data output deviation index, sensory costs, and detectability. The proposed approach is systematic and universal; it can be integrated into monitor architecture for parameter estimation in other complex production systems.


Keywords: sensor deployment; Bayesian network; parameter estimation precision; wet-grinding system

## 1. Introduction

Advances in sensing and computing technologies have led to the widespread application of sensor deployment in numerous fields, such as structural health monitoring, environmental protection, and the manufacturing industry, particularly for the control, optimization, and estimation of parameters [1]. Good-quality data are crucial to the performance evaluation of such plants. Although redundantly sensing every physical parameter of a system can minimize information loss, the resulting sensor network could become overloaded with data communication and analysis. This action is especially crucial when a real-time decision is required for the remote diagnosis of disasters [2] or wireless sensor networks (WSNs) [3]. The complexity of data analysis increases exponentially with the number of sensors, resulting in deleterious consequences for data analysis and processing [4].

Therefore, appropriate sensor deployment is crucial for efficient data acquisition. The processing industry has become increasingly reliant on data to achieve the maximum precision of selected parameters and gross errors related to screening [5]. The sensor-deployment issues investigated in recent years usually cover two common problems: deciding where to physically install the sensors and determining the type, number, and location of sensors required to accurately monitor or diagnose faults at a critical point in an industrial system [6]. Wu et al. [4] designed a quantitative fuzzy graph technique to model the cause-effect

relationship between system faults and sensor measurements. The sensor's detectability for faults is determined quantitatively using the single-edge values in a fuzzy graph obtained by an analytic hierarchy process. This ensures the sensor signal acquisition's reliability by minimizing the system's unobservability. Singhania et al. [7] proposed a multi-objective formulation for optimal sensor deployment in large-scale manufacturing systems in terms of the sensor costs, system reliability, and stability in WSNs. They created a convergence trajectory-controlled ant colony system to perform sensor deployment in a case study on an automated assembly robot. Lu et al. [8] used physics-based compressive sensing (PBCS) to enhance the traditional compressed-sensing approach based on the physical knowledge of a given phenomenon to monitor the temperature field of additive manufacturing processes. Their experimental study demonstrated that only a few thermal readings are needed to reconstruct the three-dimensional temperature field using the PBCS approach for the additive manufacturing processes. Using glowworm swarm optimization, Liao et al. [9] presented a sensor-deployment scheme to enhance the coverage in WSNs. In their method, each sensor node, being an individual glowworm, is attracted toward its neighbors with a lower intensity of luciferin and moves toward one of them to maximize the coverage of the sensing field. Another specific application area is computer vision for the traffic sensor location problem (TSLP), which must fulfill two typical requirements: the number of sensors needed and the best locations for their deployment. Owais presented a review article summarizing the research contributions for solving the TSLP over nearly three decades, analyzing most TSLP studies using a new categorization system [10]. Furthermore, another application area includes WSNs, which have helped improve smart environments in various fields, such as intelligent manufacturing, structural health monitoring, smart transport and cities, and energy consumption [11]. Their review focuses on where to locate the sensors in every physical area to increase the sensing coverage [12,13], lifetime, and energy savings [14,15] at minimum costs [16].

Other sensor-deployment research focuses on the location of an estimated product feature or parameter that a sensor measures instead of the place where the sensor is physically installed. Therefore, the number and location of sensors must be based on the product features or parameters to be measured [6]. From this perspective, the challenge of designing a sensor system is selecting product features or parameters to measure in different industrial application scenarios [17]. Ding et al. [18] suggested a sensor distribution for variation diagnosis in a multistation assembly process. Using a state-space model, a diagnosability index was developed to quantify the effectiveness of the sensor distribution. The variational transmissibility between stations was considered, and a backward propagation strategy was designed to determine the measurement stations. Shukla et al. [19] created an optimal sensor allocation for root-cause analysis that maximizes the number of measurement points placed at key characteristics (KCs). The critical product and process design features are considered, and a feature-based procedure is presented to include arbitrary locations and KCs in the final sensor layout. He et al. [20] proposed a quantitative cause-effect graph (QCEG) to handle the heterogeneity among the properties of sensors and faults. The QCEG models the cause-effect relationship between the system faults and sensor readings. Based on minimizing the fault unobservability, sensor deployment is performed to facilitate singlestation multistep manufacturing process monitoring. Sun et al. [21] investigated the effects of sensor allocation optimization on the diagnosability of a multistation manufacturing system (MMS). They proposed three indices (detectability, locatability, and isolatability) to measure the system's diagnosability. A two-step process is presented to specify the variable transmission between stations and variation diagnosis within a station. Based on an established definition of sensor allocation in a Bayesian network (BN), Liu et al. [22] developed a "best allocation subsets by intelligent search" (BASIS) algorithm to identify the optimal sensor allocation at minimum cost under different specified average run length (ARL) requirements. They designed a diagnosis ranking method to determine the root cause by ranking all the identified potential faults in a manufacturing system. Considering the effects of the propagation of fault risks, Li et al. [23] proposed a gray relational analysis

(GRA)-based quantitative causal diagram (QCD) sensor allocation strategy to describe the fault-sensor and fault-to-fault causal relationships. The data-driven-based GRA calculates the coefficients of the fault risk propagation. Mehrjoo et al. [24] proposed an information theory-based optimal sensor placement (OSP) framework for parameter estimation and strain estimation considering sensor costs. A Bayesian OSP method combined with modal expansion is used to minimize the information entropy regarding the strain time histories at critical locations of an offshore wind turbine. A multi-objective function is proposed to balance sensor costs and information entropy balanced by the weight factor. It was found that the OSP results are sensitive to the weight factor; the Pareto solutions for OSP are also presented.

From this literature review, it is clear that previous studies in this area do not address certain key concerns:
(1) Although many papers describe the causal model between faults and sensors for variation diagnosis in complex manufacturing systems based on the sensor distribution, they lack a causal analysis of the key physical parameters closely related to fault characteristics and their critical quantitative representation.
(2) Currently, the objective of the optimal sensor distribution for variation diagnosis in complex manufacturing systems primarily focuses on system observability, system diagnosability, system reliability, the coverage of the sensing field, and sensor system costs. Few attempts have been made considering the precision of the physical parameters obtained from the sensor distribution.
(3) The metaheuristic algorithm is more advantageous than traditional mathematical programming methods for multi-objective optimization (MOO) problems. It is considered a potential and powerful tool for solving the MOO problem. However, its application in the field of sensor layouts is still minimal.
These three issues are the research questions discussed in the following sections.

# 2. System Detectability Based on Bayesian Networks 

Optimal sensor deployment is "mission-specific," meaning that the sensor-deployment strategy is closely related to specific objectives, such as decision-making and knowledge discovery [25]. This article focuses on the crucial issue of parameter estimation precision in wet-grinding systems. Wet grinding performance evaluation relies on estimating specific variables, such as model parameters or performance indicators. These particular variables can be determined via data reconciliation and monitoring; that is, adequate sensors must be allocated at the right places to guarantee the precision of the variables involved in the estimation scheme. Having all physical parameters sensed in a wet-grinding system is unnecessary and impossible because of their intrinsic dependence/correlation relationships.

An effective method to represent the causality between physical parameters in a system for wet grinding performance evaluation is to create probabilistic networks or probabilistic graphical models, which are increasingly being viewed as a convenient highlevel language for structuring a complex system of equations and an explicit representation of dependence/correlation between variables that ignores the specific functional details. BNs are a popular probabilistic network-a powerful method for presenting and reasoning with uncertainty. A valuable technique for BNs is to assume that the arcs represent causality.

A BN is a directed acyclic graph that facilitates the representation of the causal relationships among physical variables in the wet-grinding system. A BN has two components: its structure and parameters. The structure, or topology, of a BN should capture qualitative relationships between physical variables. The design of a BN can be obtained from learned data or engineering knowledge. The former uses a series of statistical significance tests of conditional independence for structure learning [26]. The latter primarily depends on domain knowledge from human experts. In light of the practical experience of professional technicians in the field of wet grinding, the latter was adopted in this study to build the topology of the BN. In particular, two nodes should be connected directly with the arc, indicating the direction if one affects or causes the other. The nodes in a BN represent

a set of physical variables, $\mathcal{F}=\left\{F_{1}, F_{2}, \ldots, F_{n}\right\}$, from the wet-grinding system. A set of directed arcs connects the pairs of nodes, $F_{i} \rightarrow F_{j}$, representing the direct dependencies between variables. If there is a directed arc from $F_{i}$ to $F_{j}$, then $F_{i}$ is a direct cause (called a parent) of $F_{j}$, denoted by $\Re_{k}\left(F_{j}\right), k \in Z^{+}$. Otherwise, if there is an indirect path from $F_{i}$ to $F_{j}$, that is, $F_{i} \rightarrow \cdots \rightarrow F_{j}$, then $F_{i}$ is an indirect cause (called an ancestor) of $F_{j}$, denoted by $\mathfrak{R}_{k}\left(F_{j}\right), k \in Z^{+}$. The parameters of a BN are a set of conditional probability distributions to quantify the relationships between connected nodes. When the wet-grinding system runs under normal conditions, all physical variables are assumed to adhere to the standard normal distribution. Here, a linear Gaussian parameterization of the BN is employed to represent the relationship between the various physical variables [27], that is:

$$
F_{j}=\sum_{k=1}^{m_{j}} \delta\left(\Re_{k}\left(F_{j}\right), F_{j}\right) \cdot \Re_{k}\left(F_{j}\right)+\vartheta_{j}
$$

where $\delta(\cdot, \cdot)$ is a path coefficient. All the physical variables follow the standard normal distribution; thus, $\vartheta_{j}$ and $\Re_{k}\left(F_{j}\right)$ are independent of each other, $\vartheta_{j} \sim \mathrm{~N}\left(0, \sigma_{j}^{2}\right)$; here, $\sigma_{j}^{2}=1-\sum_{k=1}^{m_{j}} \delta\left(\Re_{k}\left(F_{j}\right), F_{j}\right) \cdot \rho\left(\Re_{k}\left(F_{j}\right), F_{j}\right)$, and $\rho(\cdot, \cdot)$ is the Pearson correlation. The parameterization in Equation (1) has also been applied to path modeling by Wright [28]. The graphical model is developed to portray linear causal relationships based on sample correlations. Path modeling is preferable because it concisely illustrates the causal features of BNs.

Let $\Omega_{k}$ be an active path between $F_{i}$ and $F_{j}$, where $k$ is the number of active paths between $F_{i}$ and $F_{j}$. Such an active path does not go against the direction of an arc after having gone forward. Next, the path coefficient, $\delta(\cdot, \cdot)$, can be expressed as follows:

$$
\delta\left(F_{i}, F_{j}\right)= \begin{cases}\rho_{i \rightarrow j} & \text { if }\left\{F_{i} \rightarrow F_{j}\right\}=\Omega_{k} \\ \sum_{k} f_{k}^{-1}\left(\rho_{q \rightarrow r}\right) & \text { for } \quad \text { other }\left\{F_{q} \rightarrow F_{r}\right\} \in \Omega_{k}\end{cases}
$$

where $\rho_{q \rightarrow r}=\prod_{v} \delta\left(F_{q}, F_{r}\right)$ is the Pearson correlation along the incoming paths from $F_{q}$ to $F_{r}$, and $v$ is the number of directed arcs in an active path from $F_{q}$ to $F_{r}$. The causal influences represented by a path coefficient can easily be read from the graph illustrating that model. Under the linear Gaussian parameterization of the BN in Equation (1), the causal impacts between two physical variables, $F_{i}$ and $F_{j}$, can be determined. Specifically, if there is one directed path from $F_{i}$ to $F_{j}$, it is easy to derive that the causal influence is equal to the product of all path coefficients on the corresponding directed path. Otherwise, the causal effect of $F_{i}$ on $F_{j}$ is the sum of all directed paths from $F_{i}$ to $F_{j}$. That is, the causal influences of $F_{i}$ on $F_{j}$, denoted by $\pi_{i \rightarrow j}$, can be expressed as follows:

$$
\pi_{i \rightarrow j}= \begin{cases}\prod_{\lambda} \delta\left(F_{i}, F_{j}\right) & , k=1 \\ \sum_{k}\left\{\prod_{\lambda} \delta\left(F_{i}, F_{j}\right)\right\} & , k \geq 2 \\ 1 & , i=j \\ 0 & , \text { otherwise }\end{cases}
$$

where $k$ is the number of active paths, $\Omega_{k} ; \lambda$ is the number of directed arcs in an active path from $F_{i}$ to $F_{j}$. To achieve the target product quality, the wet grinding process is always kept under control. An effective method for this is to build monitoring control charts on sensor outputs to detect abnormalities, known as assignable variation, as abnormalities are often relatively high in magnitude. Letting $\mathcal{S}=\left\{S_{1}, S_{2}, \ldots, S_{m}\right\}$ be the sensor set to detect the assignable variation in the series of physical variables, $\mathcal{F}=\left\{F_{1}, F_{2}, \ldots, F_{n}\right\}(m \leq n)$, then control charts can be built for the output of each sensor to flag and identify the occurrence points of system abnormalities. The single mean shift of physical parameters sensed is conducted to improve the wet-grinding system's detection accuracy. Assuming a single

mean shift in $F_{i}$ is $\varepsilon_{i}$, the causal effect of an ancestor, $F_{j}$, on this variable, $F_{i}$, can be obtained as Equation (4); here, $\varepsilon_{i}$ is the single mean shift in $F_{j}$ induced by $\varepsilon_{i}$.

$$
\varepsilon_{j}=\pi_{i \rightarrow j} \varepsilon_{i}
$$

Equation (4) shows how the mean shift $\varepsilon_{i}$ in a variable $F_{i}$ propagates to any variable $F_{j}$ in the BN. The ARL of a Shewhart control chart on $F_{j}$, in terms of detecting the mean shift in $F_{i}$, denoted by $\Phi_{1, \varepsilon_{j}}$, is defined as follows [29]:

$$
\Phi_{1, \varepsilon_{j}}=\sum_{r=1}^{\infty} r \cdot\left[1-\psi\left(z_{\alpha / 2}-\varepsilon_{j}\right)+\psi\left(-z_{\alpha / 2}-\varepsilon_{j}\right)\right] \cdot\left[\psi\left(z_{\alpha / 2}-\varepsilon_{j}\right)-\psi\left(-z_{\alpha / 2}-\varepsilon_{j}\right)\right]^{r-1}
$$

where $\psi(\cdot)$ is the cumulative distribution function, $z_{\alpha / 2}$ is the upper $\alpha / 2$ percentile of the standard normal distribution, and $\alpha$ is a type-I error of the Shewhart control chart. The simplified mathematical expression can be obtained for Equation (5) through integral calculation. Mathematically, this equation can be expressed as

$$
\Phi_{1, \varepsilon_{j}}=\frac{1}{1-\psi\left(z_{\alpha / 2}-\varepsilon_{j}\right)+\psi\left(-z_{\alpha / 2}-\varepsilon_{j}\right)}
$$

Assuming that the set of sensors used to detect the single mean shift of the group of physical variables $\mathcal{F}=\left\{F_{1}, F_{2}, \ldots, F_{n}\right\}$ is $\mathcal{S}=\left\{S_{k}\right\}, k \in\{1,2, \ldots, n\}$, the mean shift $\varepsilon_{k}$ of $F_{k}$ is monitored by sensor $S_{k}$. If $S_{k} \in \mathcal{S}$ is the sensor such that the causal effects of $F_{i}$ on $S_{k}$ are the largest among all the sensors in $\mathcal{S}, F_{k}=\operatorname{argmax}_{S k \in \mathrm{~S}}\left(\pi_{i \rightarrow j}\right)$; then, the control chart on $F_{k}$ has the minimum ARL for detecting $\varepsilon_{k}$. Therefore, the following proposition can be given under a BN framework to ensure the inclusion of all the physical variables, $\mathcal{F}$, whose mean shifts are detectable by $\mathcal{S}$.

Proposition. Given the sensor set $\mathcal{S}=\left\{S_{1}, S_{2}, \ldots, S_{m}\right\}$ to detect the assignable variation in the series of physical variables, $\mathcal{F}=\left\{F_{1}, F_{2}, \ldots, F_{n}\right\}(m \leq n)$, a mean shift $\varepsilon_{i}$ in $F_{i} \in \mathcal{F}$ can be detected by $\mathcal{S}$, if the following conditions are fulfilled:

$$
\varepsilon_{j} \geq z_{\alpha / 2}-\psi^{-1}\left(1-\left(\Phi_{1, \varepsilon_{i}}^{U}\right)^{-1}\right)
$$

where $\Phi_{1, \varepsilon_{i}}^{U}$ is an upper bound according to specific domain standards of Shewhart control charts.
Proof of Proposition. As shown in the control chart, $F_{k}$ has the minimum ARL in detecting $\varepsilon_{k}$, and $\Phi_{1, \varepsilon_{i}}^{U} \geq \Phi_{1, \varepsilon_{j}}$ can be obtained, meaning that

$$
\psi\left(z_{\alpha / 2}-\varepsilon_{j}\right)-\psi\left(-z_{\alpha / 2}-\varepsilon_{j}\right) \leq 1-\left(\Phi_{1, \varepsilon_{i}}^{U}\right)^{-1}
$$

For both the positive and negative mean shift $\varepsilon_{i}, \psi\left(-z_{\alpha / 2}-\varepsilon_{j}\right) \approx 0$, the above equations can be summarized as $\psi\left(z_{\alpha / 2}-\varepsilon_{j}\right) \leq 1-\left(\Phi_{1, \varepsilon_{i}}^{U}\right)^{-1}$. Taking the inverse function of $\psi(\cdot)$ on both sides of the above equation and reorganizing the abovementioned equations results in Equation (7). Therefore, the detectability of the set of physical parameters can be determined according to Equation (7) when the average running length and the range of a single mean shift are specified.

# 3. Accelerometer Allocation Based on Coupled Computational Fluid Dynamics-Discrete Element Method (CFD-DEM) Simulations 

The wet stirred-media mill is more efficient than conventional grinding techniques, such as tumbling mills, for fine and ultra-fine grinding. There is a dearth of online internal

state information for the manufacturer to effectively optimize the grinding process. Computer simulations based on the CFD-DEM coupling method provide a means to estimate hidden process variables online, such as the bead-bead impact energy, which cannot be directly measured during the operation of an actual wet stirred-media mill. Experimental studies and computer simulations have demonstrated that the impact energy among beads is related to the grinding rate [30,31]. Moreover, it has been recently reported that the impact energy among beads in a wet-stirred mill can be determined through the impact energy of the bead wall, which can be detected by accelerometers mounted on the mill's shell via proper signal processing [32]. Although the CFD-DEM coupling method allows a massive amount of bead-wall impact data to be collected over the entire wet-stirred mill boundary, data collection must be constrained in a systematic approach that is generally only sensitive to bead-wall impact events on the mill's shell. This action can ensure that accelerometers are placed at the positions of strong surface vibrations generated by repeated bead-wall impacts.

The comminution process in wet stirred-media mills is a time-varying dynamic process. Two conditions must be fulfilled to fully break product particles in a specific time. The first is that the number of bead-wall collisions per unit time must be sufficient, and the second is that the intensity of each bead-wall collision must be sufficiently high. To meet these conditions, a stress model is developed to better describe the grinding mechanism in a wetstirred media mill [33]. Two parameters can demonstrate the basic concept underlying the stress model: the first is the stress number, $S N_{b w}$, which denotes the number of bead-wall collisions per unit time, where every bead-wall collision is called a stress event. The second is the stress intensity, $S I_{b w}$, which denotes the magnitude of the bead-wall impact energy or force at each stress event. Thus, a measure for $S N_{b w}$ can be derived according to Equation (9):

$$
S N_{b w}=\alpha_{n} \cdot n_{s} \cdot N_{b} \cdot t_{g}
$$

where $\alpha_{n}, n_{s}, N_{b}$, and $t_{g}$ are the scale factor, rotation speed of the stirrer, number of beads in the chamber, and grinding time, respectively. Derived from the kinetic energy of the beads, the stress intensity $S I_{b w}$ is the other essential parameter that characterizes a comminution process, and it can be represented as follows:

$$
S I_{b w}=\beta_{n} \cdot d_{b}^{3} \cdot v_{b}^{2} \cdot \rho_{b} \cdot\left(1+\frac{Y_{p}}{Y_{b}}\right)^{-1}
$$

where $\beta_{n}, d_{b}, v_{b}$, and $\rho_{b}$ are the scale factor, the bead's diameter, the bead's absolute velocity, and the bead's density, respectively. $Y_{p}$ and $Y_{b}$ are the Young's moduli of the product particles and the bead material, respectively. Therefore, the impact energy of the beads to the chamber wall, $E_{b w}$, can be described by the product of the stress number, $S N_{b w}$, and the stress intensity, $S I_{b w}$, which can be determined using Equations (9) and (10), respectively:

$$
E_{b w}=S N_{b w} \cdot S I_{b w}
$$

The selected measurement parameter is the impact energy of the beads on the chamber wall, which can be detected using proper signal processing by accelerometers mounted on the chamber shell. The zones where the accelerometers are installed must be constrained systematically and are generally only sensitive to bead-wall impact events under certain operating conditions. Therefore, the following definitions can be given under the bead-wall impact events used to identify the sensitive areas on the chamber wall under different operating conditions.

Definition. Supposing that the accelerometers are mounted on $n$ zones of the chamber shell, under $m$ disparate operating conditions, the sensing data are detected by accelerometers in the $n$ zones of the chamber shell, and the average impact energy, $\overline{E_{b w, j}^{i}}(1 \leq i \leq m, 1 \leq j \leq n)$, is obtained

via proper signal processing. Next, the sensitivity index of each zone on the chamber shell, $S T_{j}$, $1 \leq j \leq n$, can be defined as follows:

$$
S T_{j}=\frac{\left\{\sum_{i=1}^{m}\left(\bar{E}_{b w, j}^{i}-\bar{E}_{b w, j}\right)^{2}\right\}^{3}}{m^{3} \bar{E}_{b w}^{6}}
$$

where $\bar{E}_{b w, j}=\frac{1}{m} \sum_{i=1}^{m} \bar{E}_{b w, j}^{i}$ and $\bar{E}_{b w}=\operatorname{argmax}_{1 \leq i \leq m}\left\{\bar{E}_{b w, j}^{i}\right\}$.
The sensitivity index $S T$ describes the extent of sensitivity of each zone of the chamber shell to changes in the operating conditions. The larger the value, the more sensitive the zones are to changes in the operating conditions. Allocating sensors in this area is more economical and efficient.

To assist in sensor allocation by determining desirable physical sensor locations that are generally sensitive to the bead-wall impact zone surrounding the chamber wall, the chamber shell of the wet stirred-media mill is split into 30 zones of different sizes (I-1, I-2, ..., V-6), which produces 30 individual bead-wall impact time series data sets for each simulation. Therefore, the different zones of impact energy along the length of the chamber shell can be identified via proper signal processing. Figure 1 shows these zones.
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic plot of the chamber shell and monitoring zones.
Coupled CFD-DEM simulations were performed to collect the bead-wall impact event data over the entire boundary of the wet stirred-media mill. The software packages used were EDEM2018 (version 4.0.0, academic adaption, released by the UK DEM Solutions) for the DEM simulations and Workbench (version 19.1, academic adaption released by the ANSYS, Inc., Canonsburg, PA, USA) for the CFD simulations, which were coupled using the EDEM2018-Fluent19.1 compile interface files. The degree of filling investigated for the beads ranged from $70 \%$ to $90 \%$, the bead diameter ranged from 0.8 mm to 1.6 mm , and the stirrer speed ranged from 1000 rpm to 1400 rpm , determined in accordance with the recommendations of Root Industrial Co., Ltd. (Coimbatore, India). A set of seven simulations were completed under different loading and rotation speed combinations. The 30 zones were analyzed to determine the zones generally sensitive to the fluctuations in bead-wall impact energies, which are characterized by the aforementioned sensitivity index ST. With reference to Figure 1, Figure 2 shows that Zones I-5, I-6, III-4, and III-6 are the most sensitive to changes in the operating conditions of the wet stirred-media mill. Under normal circumstances, Zone II is affected by the local filling rate of the beads and the dynamic balance of the internal bead cycle [32]. Therefore, the bead-wall impact energy

of this area is insensitive to different operating conditions. Zones IV and V are the areas where the diffusion wheel is located and are mainly applied for product particle dispersion, rather than crushing. This action also directly leads to the insensitivity of these areas to changes in the operating conditions. Therefore, considering the limited sensor location space, the cost constraints, and the goal of eliminating redundant sensing data as much as possible, the sensor layout is only performed in Zones I-5, I-6, III-4, and III-6.
![img-1.jpeg](img-1.jpeg)

Figure 2. Sensitivity index to the bead-wall impact energy fluctuation in 30 boundary zones.

# 4. Sensor Allocation Model and Algorithm 

The optimal sensor-deployment problem is a "minimum set covering problem", meaning that the optimized sensor set will contain the minimum number of sensors to meet certain restrictions. To maximize the precision of the sensor network for the physical parameter estimation of the wet-grinding system, the model developed for sensor allocation design comprises a measurement of the estimation quality of physical parameters or state variables in the objective function. The precision of the sensor network for physical parameter estimation mainly depends on two factors: the first is the reasonable arrangement of the sensor, and the second is the data-acquisition accuracy of the sensor set. The latter is contingent on the precision of the sensor itself. Here, the detection accuracy of the sensor network is indicated by the data output deviation index, $\gamma_{i \rightarrow j}$, which represents the data output precision of the $i$ th type sensor used to observe the $j$ th type physical parameters; that is,

$$
\gamma_{i \rightarrow j}=\frac{\sigma_{i}}{x_{i}}\left\{1+\left(C_{i}\right)^{d_{i, j} \times x_{i}}\right\}
$$

where $\sigma_{i} \in \delta$ is the measurement deviation of the sensor itself, $x_{i}$ is the number of the $i$ th type sensor placed to monitor the system operations, and $C_{i} \in \phi$ is the $i$ th type sensor failure probability. $d_{i, j}$ is a binary bipartite variable that indicates the cause-effect information between parameters and sensors, which has the following characteristics:

$$
\left(d_{i, j}\right)_{F \times \mathcal{S}}= \begin{cases}1 & S_{i} \text { to observe } F_{j} \\ 0 & \text { otherwise }\end{cases}
$$

Equation (13) shows that the data output deviation index of the sensor set, $\gamma_{i \rightarrow j}$, is decided by the measurement deviation of the sensor itself, and it considers the influence of the sensor failure rate. $d_{i, j}=1$ means that the physical parameter $F_{j}$ can be observed by sensor $S_{i}$. In this case, the data output deviation index, $\gamma_{i \rightarrow j}$, is the superposition of the measurement deviation of the sensor itself and the deviation caused by the sensor failure. Examples of this include the non-linearization of the sensor data output generated by the

external environment or sensor aging. Similarly, $d_{i, j}=0$ means that no sensor is arranged at the position to observe the physical parameter $F_{j}$, that is, $x_{i}=0$. In this case, the data output deviation index, $\gamma_{i \rightarrow j}$, is considered to be infinite, which becomes meaningless in industrial applications. Sensor deployment aims to achieve the minimum data output deviation index and sensor costs under the constraints of the mean shift detectability. Mathematically, this can be expressed as

$$
\begin{aligned}
& \operatorname{Min}: \max \left(\gamma_{i \rightarrow j}\right)=\max \left\{\frac{\sigma_{i}}{x_{i}}\left(1+\left(C_{i}\right)^{d_{i, j} \times x_{i}}\right)\right\} \\
& \operatorname{Min}: \sum_{i}\left(C_{i} \times \sum_{j}\left(d_{i, j} \sum x_{i}\right)\right) \\
& \text { Subject to }: \varepsilon_{j} \geq z_{\alpha / 2}-\psi^{-1}\left(1-\left(\Phi_{1, \varepsilon_{i}}^{1 I}\right)^{-1}\right) \\
& x_{i} \in Z^{+}
\end{aligned}
$$

The abovementioned formulation is based on minimizing the maximum data output deviation index $\gamma_{i \rightarrow j}$ among all of the sensor sets. This outcome is based on the philosophy that a chain can be no stronger than its weakest link. Equation (15) achieves overall minimum data output deviation and sensor costs under the mean shift detectability of the physical variable. Sensor allocation was formulated as multiple objectives on the data output deviation index (primary) and sensor costs (secondary) under the constraints of the mean shift detectability. Under MOO conditions, the minimum sensor covering set is, in fact, a Pareto optimal set. An exhaustive search algorithm is a possible solution, which enumerates and tests the candidate solutions one-by-one in a certain order to determine the solutions that meet the requirements. However, it is almost impossible to obtain the optimal solution in polynomial time [25]. Mathematical programming can also be employed to achieve a good solution. However, it is sensitive to the shape of the Pareto frontier and must be differentiable for the objective function and the constraints. Comparatively, the metaheuristic algorithm is not subject to such restrictions and is considered a potential and powerful tool to solve MOO problems. Therefore, this work uses the shuffled frog leaping algorithm (SFLA) for sensor-deployment optimization in a wet-grinding system [34].

# 5. Case Study 

The zirconia powder production line of Root Industrial Co., Ltd. was used to validate the precision of the sensor-deployment approach proposed for parameter estimation in the wet-grinding system. Figure 3 shows the zirconia powder production process flowsheet. Zirconia powder and deionized water are first ground in a vertical ball mill to reach a certain initial product particle size, thoroughly mixed in a stirring tank, cooled by a heat exchanger, and pumped into a sand mill for grinding. After grinding, the slurry is returned to the stirring tank for mixing, and then to the grinding mill for circulating grinding after passing through the heat exchanger. When the product particle size meets the requirements, the slurry is sent to the drying tower for drying and storage. To provide high-precision, reliable, and relevant parameters for the online prediction of slurry product particle size, considering the causal relationship between the parameters and the spatial arrangement of the sensors, a total of 12 sensing stations are set up for the effective acquisition of these physical parameters (Figure 4).

The graphical model of BNs is developed to portray linear causal relationships between the physical parameters. The path coefficient is calculated according to Equation (2), which illustrates the causal features of BNs (Figure 4). Due to the product particle size (F18) being a variable that must be predicted, there is no need to calculate the path coefficient. Table 1 presents the features of the sensors and the physical parameters. Sensor information about the wet-grinding system is taken from the accumulation of empirical data for actual industrial production at Root Industrial Co., Ltd. The table also shows that not every physical parameter requires a sensor to pick up relevant information owing to the inherent causal relationships among them.

![img-2.jpeg](img-2.jpeg)

Figure 3. Zirconia powder production process flowsheet and sensing locations.
![img-3.jpeg](img-3.jpeg)

Figure 4. Causal features of Bayesian networks for the wet-grinding system.

Table 1. Sensors and physical parameters for the wet-grinding system.


The performance evaluation of a multi-objective optimized sensor layout requires further research. A systematic analysis should consider operability and economics [35]. Therefore, the data output deviation index and sensor cost are proposed as the optimization targets under the constraints of the mean shift detectability for each physical parameter in BNs. The aforementioned SFLA is used to accomplish this task, which is compared with two sensing layouts: the directed graph (DG), with a greedy-based approach, and saturated sensing. According to the actual industrial application monitoring requirements, the level of significance $\alpha=0.05$, the mean shift $\varepsilon_{i}=3$, and the upper bound for $\varepsilon_{i}, \Phi_{1, \varepsilon_{i}}^{U}=4$, are recommended by Root Industrial Co., Ltd. The basic parameters of SFLA are selected as follows. The number of memeplexes is 40 , the number of frogs in each memeplex is 80 , the number of frogs selected from each memeplex is 40 , the local iteration number within each memeplex is 20 , the maximum step size allowed to be adopted by a frog after being infected is 1 , and the convergence criteria of SFLA are satisfied if at least one frog would carry the "best memetic pattern thus far" for 15 consecutive shuffles. Table 2 presents the results for all three sensing layouts.

Table 2. Results comparison for the wet-grinding system.

Sensors | Maximum Data
Output Deviation
Index | Average
Deviation Index | Cost Utilized  |

Comparisons are conducted from the perspectives of the maximum data output deviation index, the total cost of the selected sensors, and the average deviation index in the wet-grinding system. The cost utilized is simply a summation of all the sensor costs chosen in the deployment. The average deviation index is the data output deviation index per sensing location selected to arrange the sensors. Table 2 shows that the maximum data output deviation index in the wet-grinding system fell from the saturated sensing's and DG's value of 1.1, to the BN's value of 0.505 ; the average deviation index decreased from the saturated sensing's value of 0.4321 and DG's value of 0.6018 to the BN's value of 0.2827 . The total cost of the sensory system also reduced from the saturated sensing's value of 3020 and DG's value of 1810 to the BN's value of 1740. Thus, it is concluded that, with the inclusion of the causal features of BNs and quantitative information of the sensory system, BNs with SFLA-based sensor deployment modeling effectively enhance the accuracy of parameter estimation and the economy of sensor layout. The following reasons could account for this: while allocating the sensors, the DG with greedy-based

sensor deployment always tries to select the sensor node with the most edge connections with the physical parameter nodes. If the other sensors also cover the physical parameter nodes, the arcs connected to these sensors must be deleted. The traversal is continued until the sensor with the lowest number of arcs is selected to cover all the physical parameter nodes. It is observed that the greedy DG does not consider the causal relationship between physical parameters and the quantitative features of sensor nodes. Hence, a DG with a greedy-based approach has a higher data output deviation (DG's value of $0.6018>$ BN's value of 0.2827 ) and higher sensor costs (DG's value of $1810>$ BN's value of 1740). In industrial practice, the number of sensors tends to increase at every sensing location to further reduce the data output deviation, resulting in saturated sensing. Redundant sensing can effectively reduce the data output deviation (saturated sensing's value of $0.4321<$ DG's value of 0.6018 ). However, it also dramatically increases the cost of the sensing system (saturated sensing's value of $3020>$ DG's value of 1810); it may be cursed with overload on the post-processing data, which is also one of the main reasons why the sensor deployment needs to be optimized.

# 6. Conclusions 

Optimal sensor deployment is essential for system abnormality detection in quality engineering. This paper aims to develop a BN with an SFLA-based sensor deployment methodology that can process the cause-effect relationship between physical variables, the quantitative heterogeneous properties of sensors, and multiple-objective optimization in a wet-grinding system. A BN is created to represent the causal relationships among the physical variables by employing the path model in the wet-grinding system. A prescribed detectability requirement is developed as a constraint for MOO to ensure all the physical variables whose mean shifts are detectable by the sensor set. To facilitate the identification of sensitive areas of the chamber wall under the bead-wall impact events for various disparate operating conditions, coupled CFD-DEM simulations are performed to collect the beadwall impact event data. The sensing location of accelerometers mounted on the chamber shell is determined using proper signal processing. By introducing the SFLA, a strategy of optimal sensor placement is proposed to minimize the maximum data output deviation index among all sensor sets and minimize the sensory cost under the constraints of the mean shift detectability, thus achieving optimum sensor deployment. The performance of the proposed strategy was tested and validated for the zirconia powder production process. The results illustrate that, in comparison to a DG with greedy and saturated sensing, a BN with an SFLA-based strategy can acquire a lower maximum data output deviation index, average deviation index, and sensory costs. It can be easily integrated into monitoring architecture for parameter estimation in complex systems such as drum-grinding systems, cutting processing systems, and multistation assembly processes. Future research should focus on integrating the proposed sensor-deployment strategy into wet-grinding systems and adaptively adjusting the sensor deployment according to the data output accuracy of physical variables, creating a dynamic framework between the sensor deployment and the performance metrics of the wet-grinding system.

Author Contributions: Conceptualization, H.Y. and K.H.; methodology, K.H. and F.S.; software and data curation, F.S. and Q.Y.; investigation, K.H. and B.W.; draft preparation, K.H. and Q.Y. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded in part by the Natural Science Foundation of Anhui Province, grant number 2108085ME172; in part by the Suzhou University key project, grant numbers 2021yzd02, 2022yzd08, and 2022yzd09; in part by corporate-funded R\&D projects, grant numbers 2021xhx023, 2021xhx022, 2021xhx024, and 2022xhx122; in part by the Suzhou College Teacher Application Ability Development Workstation, grant number 2020XJYY03; in part by the Suzhou University Professor (Ph.D.) Scientific Research Foundation, grant number 2016JB09; in part by the Natural Science Research Project of Anhui Educational Committee: Research on Particle Size Distribution of Wet Grinding Products based on optimized sensor data fusion; and in part by the Suzhou University Scientific Research Platform Project, grant number 2020ykf14.

Institutional Review Board Statement: Ethical review and approval were waived for this study due to this study not involving humans or animals.

Informed Consent Statement: Not applicable.
Data Availability Statement: Data is contained within the article.
Acknowledgments: This work was carried out at the High-End Micro-Nano Grinding Equipment School-Enterprise Collaborative Innovation Engineering Center, which is the School-Enterprise Joint Laboratory at Suzhou University-Anhui Root Industrial Co., Ltd. We sincerely thank Chengcai Xi and Biaoxiao Li for their technical support.

Conflicts of Interest: The authors declare no conflict of interest.
