# RELIABILITY-AWARE ZONOTOPIC TUBE-BASED MODEL PREDICTIVE CONTROL OF A DRINKING WATER NETWORK 

BOUTROUS KHOURY ${ }^{\text {a }}$, Fatiha NEJJARI ${ }^{\text {a }}$, Vicenç PUIG ${ }^{\text {a,* }}$<br>${ }^{a}$ Advanced Control Systems<br>Technical University of Catalonia (UPC)<br>Rambla Sant Nebridi 22, 08222 Terrassa, Spain<br>e-mail: \{khoury.boutrous, fatiha.nejjari, vicenc.puig\}@upc.edu


#### Abstract

A robust economic model predictive control approach that takes into account the reliability of actuators in a network is presented for the control of a drinking water network in the presence of uncertainties in the forecasted demands required for the predictive control design. The uncertain forecasted demand on the nominal MPC may make the optimization process intractable or, to a lesser extent, degrade the controller performance. Thus, the uncertainty on demand is taken into account and considered unknown but bounded in a zonotopic set. Based on this uncertainty description, a robust MPC is formulated to ensure robust constraint satisfaction, performance, stability as well as recursive feasibility through the formulation of an online tube-based MPC and an accompanying appropriate terminal set. Reliability is then modelled based on Bayesian networks, such that the resulting nonlinear function accommodated in the optimization setup is presented in a pseudo-linear form by means of a linear parameter varying representation, mitigating any additional computational expense thanks to the formulation as a quadratic optimization problem. With the inclusion of a reliability index to the economic dominant cost of the MPC, the network users' requirements are met whilst ensuring improved reliability, therefore decreasing short and long term operational costs for water utility operators. Capabilities of the designed controller are demonstrated with simulated scenarios on the Barcelona drinking water network.


Keywords: fault-tolerant control, reliability, robust MPC, zonotopes, Bayesian theory, drinking water network.

## 1. Introduction

Performance deterioration and faults occurring as a result of systems' component degradation has piqued the interest of researchers over the years, mainly due to its importance in maintenance planning, production scheduling and recently in the design of control laws that account for degradation. The pursuit of these interests has become more essential when dealing with critical infrastructure such as drinking water networks (DWNs), power distribution networks, among other things, that require a high level of supervision to ensure a hypothetical perpetual supply of service.

According to Zagórowska et al. (2020), control approaches that consider the tolerance or mitigation of degradation can be classified into two main groups: (i) control systems aware of degradation and (ii) control systems mitigating degradation. In the first group, controllers are designed with the ability to compensate

[^0]for the degradation of a controlled system. For example, Zagórowska et al. (2020) consider faults as a consequence of component degradation, thus classifying fault tolerant controllers as control systems aware of degradation, where there is a prerequisite for knowledge of the fault process (Isermann, 2006; Mejdi et al., 2020). However, the latter involves control frameworks that seek to mitigate the extent of degradation over a component's life time. This basically involves the integration of models of degradation in the design of controllers, predominantly linear-quadratic or model-predictive controllers. This, in turn, implies a manipulation of system variables arriving at a trade-off between satisfying primary control objectives and the mitigation of degradation.

The incorporated model may not necessarily directly include degradation models as done in numerous works (Ray and Caplin, 2000; Salazar et al., 2020; Sanchez-Sardi et al., 2018) but involve the use of characteristic quantities such as the reliability of


[^0]:    *Corresponding author

the components reflecting a trend in degradation when minimized over time. For reliability-oriented applications, control allocation of an aircraft based on actuators' reliability was done by Khelassi et al. (2010) using an LQR control. The results show an improved actuator health and thus an overall system reliability. Similarly, in the work of Chamseddine et al. (2014) control allocation was used based on an MIT-based reliability rule for an over-actuated octocopter helicopter testbed to maximize global reliability. In the area of DWNs, Salazar et al. (2017) and Pour et al. (2018) used the interconnections between the system components to model a cumulative reliability of the system, using different statistical methods (Bayesian and Markov chains). Using an MPC, the health of the actuators was included as an objective criterion. But the works on DWNs fail to consider the real life applicability of the designed controller as demands are assumed to be known a priori without considering the uncertainty derived from this assumption.

For reliability modelling of interconnected components, there exist methods based on statistical inference that constitute desirable mathematical representations of such stochastic processes. Popular amongst these are Markov chain processes, stochastic Petri nets and the use of Bayesian networks. Bayesian networks are by far the most common method applied in the literature mainly due to the fact that Markov chains lead to a combinatorial explosion of the number of states required when the number of model components increases. This makes such a method undesirable for evaluating the cumulative reliability of complex large networks such as a DWN, which contains many interacting components (Zeller and Montrone, 2018). Since stochastic Petri nets depend on Monte Carlo simulations, they may demand massive simulations for very low probability evaluations (Philippe and Lionel, 2006). Therefore, for reliability tests on a complex interconnected system of a power network, Haghifam (2015) opted for Bayesian networks leading to improved system efficiency evaluations compared with other methods. Philippe and Lionel (2006) go a step further by applying the concept of a dynamical object oriented Bayesian network (DOOBN) modelling on a moderately complex system, a water heater process. A comparison with a Markov chain method shows that DOOBNs yield good results for reliability evaluation, which is also deemed to be more compact and readable than Markov chains.

Model-based controllers such as MPC offer a suitable platform to include in its multi-objective optimization framework, a reliability index and/or reliability constraint function with the purpose of alleviating degradation against another competing criterion. Recently, the concept of incorporating directly
an economic stage cost of the industrial process in an MPC design termed economic MPC (eMPC) has attracted interest. This procedure involves an update of the generic cost function which normally involves tracking a set-point to one which explicitly involves economic terms such as energy, cost of production, etc. eMPC allows an improvement during transients and the ability to manipulate control variables to satisfy various economic requirements (Müller et al., 2013). eMPC in the area of water supply has been extensively studied (Cembrano et al., 2011; Grosso et al., 2016).

As the name suggests, the formulated control problem constituted by economic variables (e.g., cost, price or demand) which are mostly exogenous. Some of these variables are undoubtedly subject to stochastic variations, which requires further control design considerations for a suitable operation. For example and in relation to our case, in the design of an eMPC for a DWN with variable demand as done by Grosso et al. (2016), a forecast of water demands is required to enable future predictions of states in an MPC optimization loop. But the forecasted demand as a variable is subject to human behaviour which can be described as uncertain at best. Therefore, there is a need to ensure that controllers are built robust considering these design variations, which are inevitable in real life situations. Methods of stochastic MPC (Wang et al., 2017), the min-max robust formulation (Löfberg, 2003), the tree-based method (Velarde et al., 2016) and other proposed concepts have been successfully applied to problems of uncertainties in MPC. Bemporad and Morari (2007) provide a comprehensive overview of robust MPC, highlighting recent trends and limitations, and propose future research directions.

In this paper, a robust eMPC that takes into account the reliability modelled with Bayesian networks is proposed. The topology of the network showing flow relationships between actuators linked by pipes is utilized in the Bayesian probability formulations. The reliable robust eMPC is applied to a DWN, specifically in the Barcelona drinking water network, taking into account uncertainties in the forecasted demand. The variations in demands are considered unknown but bounded in zonotopic sets. Zonotopic sets show desirable characteristics of lower complexity, flexibility and reliable computation of linear transformations and Minkowski sums compared with other geometric counterparts such as interval or ellipsoidal sets (Le et al., 2013). It must be noted that even though a robust MPC (RMPC) is achieved after this procedure, there is a certain degree of robustness for some magnitude of uncertainty beyond which the optimization problem fails to be feasible.

The rest of this paper is structured as follows: A problem formulation and preliminaries featuring the model of the DWN, some concepts of zonotopes and

sets are given in Section 2. Fundamentals of tube-based MPC are then discussed in Section 3. Subsequently, in Section 4, the reliability modelling of the network is discussed. In Section 5, considering all the works in the preceding sections, the controller is presented. Finally, the paper ends with simulation results and conclusions.

## 2. Problem formulation and preliminaries

In this section, a brief description of the selected DWN model and its condensed version will be discussed. Then an account of the primary predictive control for DWNs is given. Finally, as a prerequisite to the sequel, some important mathematical preliminaries are introduced.
2.1. General description of a control oriented DWN model. There exist in the literature some models of DWNs that seek to capture key dynamics at different levels of a DWN's architecture. There are however two predominant models that are commonly used in controller design with numerous successful outcomes. Through graph theory, flow directions of water at network nodes as well as interactions at the tanks leading to a simple flow-based model description of the network were studied by Grosso et al. (2014), while Wang et al. (2017) considered both the network flow and pressure characteristics, specifically taking into account the interactions when flow and hydraulic head equations are considered in the modelling process.

Considering only the transport sub-level, the flow-based model offers an easier option to work with, largely due to its linearity, but fails to capture key pressure dynamics which is important to present a complete mathematical behaviour of the network. Inclusion of pressure in the DWN dynamics introduces non-linearity from the pressure-flow affine equality into the constrained formulation of the optimization problem, which results in a non-convex problem. Some works have been successful in designing nonlinear MPC (Wang et al., 2017); for the control of these nonlinear models. Wang et al. (2018) consider a nonlinear constraint relaxation to produce a set of linear inequality constraints for a linear eMPC formulation. Despite its complexity, the nonlinear pressure-flow model offers a more realistic case to work with. The purpose of this paper is primarily to illustrate the ability of a control law to enhance the reliability of DWNs while considering the real life scenario of demand uncertainties via a set-based method (zonotopes) of robust MPC, henceforth a comparatively less complex flow based model will be used.

Puig et al. (2015) presented a flow-based model of the Barcelona water network, which has been extensively used in the literature, primarily for control design purposes. Basic relationships between elements considering the mass balance in tanks and equilibria
of flow directions at nodes give rise to the following discrete-time invariant system:

$$
\begin{aligned}
x(k+1) & =A x(k)+B_{u} u(k)+B_{d} d(k) \\
0 & =E_{u} u(k)+E_{d} d(k)
\end{aligned}
$$

where $x(k) \in \mathbb{R}_{+}^{n_{x}}$ is the vector of system states, denoting tank volumes at each time instant $k ; u(k) \in \mathbb{R}^{n_{u}}$ denotes the manipulated input from actuators affecting changes in states in combination with the non-negative model disturbance $d(k) \in \mathbb{R}_{+}{ }^{n_{d}}$, the consumer demand; $\mathrm{A}, B_{u}$, $B_{d}, E_{u}$ and $E_{d}$ are time-invariant matrices of suitable dimensions. From (1b), it can be inferred that the control variable $u(k)$ does not take its value in the whole of $\mathbb{R}^{n_{u}}$, but in a linear variety. This inference enables an affine parameterisation of the control variables in terms of a minimum set of disturbance, mapping the control problem to a space with a smaller decision vector and with less computational burden due to the elimination of the equality constraint (1b).

Proposition 1. (Grosso et al., 2016) If there are more control variables than algebraic equations (i.e., $n_{q}<$ $n_{u}$ ), the matrix $E_{u}$ in (1b) has a maximal rank. Assuming that the equation has a solution, it can be expressed in a reduced staggered form using the Gauss-Jordan elimination.

From Preposition 1, the control variable is parameterized such that

$$
u(k)=\tilde{P} \tilde{M}_{1} \hat{u}(k)+\tilde{P} \tilde{M}_{2} d(k)
$$

The model can be represented as (3) by substituting (2) into (1a),

$$
x(k+1)=A x(k)+\hat{B} \hat{u}(k)+\hat{B}_{d} d(k)
$$

where $\hat{B}=B \tilde{P} \tilde{M}_{1}$ and $\hat{B_{d}}=B \tilde{P} \tilde{M}_{2}+B_{d}$.
From (2), $\hat{u}(k) \in \mathbb{R}^{n_{u}} \subseteq \mathbb{R}^{n_{u}}$ can be expressed as a function of the demand variable $d(k)$ and $u(k)$. Then the control invariant set from the affine relationship between the input and demand can be evaluated. The reader is referred to Grosso et al. (2016) for an in-depth description of how (3) is formulated from Proposition 1.
2.2. Conventional eMPC as applied to DWNs. The operation of a DWN is such that network elements, active (pumps and valves) or passive (pipes and tanks) interact to satisfy operational network objectives. Thus, the MPC paradigm offers a platform to introduce in a multi-objective framework, a control scheme that encompasses all these objectives whilst respecting system constraints. These control objectives include the following components.

Minimization of the operational cost (the economic term): The dominant objective index in the MPC optimization problem is the minimization of the cost of operation in relation to constant water production and a variable electricity cost used for pumping water between a source and a demand. The MPC is designed such that an optimal cost is achieved while servicing demand under process constraints. Thus, the function is given as

$$
\mathcal{J}_{E}(k)=\left(\alpha_{1}+\alpha_{2}(k)\right)^{T} u(k)
$$

where $\alpha_{1} \in \mathbb{R}^{n_{u}}$ and $\alpha_{2}(k) \in \mathbb{R}^{n_{v}}$ represent respectively the constant water production costs and variable daily electricity costs; $u(k)$ is the actuator activity at each sample time $k$.

Guarantee of safe water storage: For operational security, it is imperative to maintain a safe level of water in tanks to ensure a consistent supply of water to demand nodes between two consecutive time instants of the MPC and also to keep a safe stock of water in the event of any uncertainties related to supply availability. A penalty equal to the sum of the squares of the deviation of the volume in each tank from a predefined safety threshold is therefore formulated as

$$
\mathcal{J}_{s}(k)= \begin{cases}\left\|x(k)-x_{s}\right\|^{2} & \text { if } x(k) \leq x_{s} \\ 0 & \text { otherwise }\end{cases}
$$

A vector of safety levels of each tank is denoted by $x_{s}$. The cost function is reformulated as (6) with the inclusion of a slack variable $\varepsilon(k)$ and an introduction of constraint (7) in a bid to circumvent the occurrence of a problematic piece-wise affine cost

$$
\begin{aligned}
\mathcal{J}_{s}(k) & =\|\varepsilon(k)\|^{2} \\
x(k) & \geq x_{s}-\varepsilon(k)
\end{aligned}
$$

Penalization of the actuator slew rate: For purposes of increasing the lifespan of actuators (pumps and valves) which is generic in MPC formulations, the deviation between two consecutive time instants of control actions is penalized for a smooth operation of control:

$$
\mathcal{J}_{\triangle U}(k)=\|\triangle u(k)\|^{2}
$$

where $\triangle u(k)=u(k)-u(k-1)$.
The volume of water in the tanks, $x(k)$, and the actuator actions, $u(k)$, are constrained to be in compact polyhedral sets $\mathbb{U}$ and $\mathbb{X}$ defined by

$$
\begin{aligned}
& x(k) \in \mathbb{X}=\left\{x(k) \in \mathbb{R}^{n_{x}} \mid \underline{x} \leq x(k) \leq \bar{x}\right\} \\
& u(k) \in \mathbb{U}=\left\{u(k) \in \mathbb{R}^{n_{u}} \mid \underline{u} \leq u(k) \leq \bar{u}\right\}
\end{aligned}
$$

respectively.

With the aforementioned objectives and constraints, a finite horizon optimal control problem which minimizes the cost

$$
\mathcal{L}(k, \hat{u}, x)=\Lambda_{1} \mathcal{J}_{s}(k)+\Lambda_{2} \mathcal{J}_{\triangle \hat{U}}(k)+\Lambda_{3} \mathcal{J}_{E}(k)
$$

where $\mathcal{L}(k, \hat{u}(k), x(k)) \in \mathbb{N}_{+} \times \mathbb{R}^{n_{u}} \times \mathbb{R}^{n_{v}} \rightarrow \mathbb{R}_{+}$is formulated taking into account that $\Lambda_{1}, \Lambda_{2}$ and $\Lambda_{3}\left(\Lambda_{i}>\right.$ $0 \forall i$ ) are design weights for each objective criterion that can be tuned following the procedure presented by Toro et al. (2011). Thus, at each time instant $k$, considering the condensed dynamic equation (3), the optimization problem to be solved is

$$
\min _{\hat{\mathbf{u}}(k), \mathbf{x}(k)} \sum_{i=0}^{N_{p}-1} \mathcal{L}(k, \hat{u}(k), x(k))
$$

subject to

$$
\begin{aligned}
x(i+1 \mid k) & =A x(i \mid k)+\hat{B} \hat{u}(i \mid k)+\hat{B}_{d} d(i \mid k) \\
\hat{u}(i \mid k) & \subseteq \mathcal{U}(i \mid k) \\
x(i+1 \mid k) & \subseteq \mathbb{X} \\
x(i \mid k) & \geq x_{s}-\varepsilon(i \mid k)
\end{aligned}
$$

Remark 1. Assume that the control variable $\hat{u} \in \mathcal{U} \subseteq \mathbb{U}$ is mapped to a reduced space from Proposition 1. For the inclusion of an input constraint, a novel time-varying input domain set $\mathcal{U}(k+i \mid k)$ is introduced such that

$$
\begin{aligned}
& \left\{\hat{u}(k) \in \mathbb{R}^{n_{u}} \mid\right. \\
& \left.\quad \underline{u}-\hat{P} \hat{M}_{2} d(k) \leq \hat{P} \hat{M}_{1} \hat{u}(k) \leq \bar{u}-\hat{P} \hat{M}_{2} d(k)\right\}
\end{aligned}
$$

under the assumption that the optimization problem (2.2) is feasible, i.e., there exists a non-empty solution given by the optimal sequence of control inputs $\left(\hat{u}^{*}(0), \hat{u}^{*}(1), \ldots, \hat{u}^{*}\left(N_{p}-1\right)\right)$, where $N_{p}$ is the prediction horizon. From the principles of receding horizon, only the first control action $\hat{u}^{*}(0 \mid k)$ of the sequence of $N_{p}$ values obtained from the solution of the MPC optimization problem is applied to the plant,

$$
\hat{u}(k)=\hat{u}^{*}(0 \mid k)
$$

disregarding the rest of control actions. At the next time instant $k$, the optimization problem is solved again using the current measurements of states and disturbances, with the most recent new forecast over the next future horizon.

### 2.3. Mathematical preliminaries.

Definition 1. A zonotope can be defined as a class of geometric sets with a center $p$ and a generator matrix $H \in$ $\mathbb{R}^{n \times r}$ in a linear affine image as

$$
\mathbb{Z} \triangleq\langle p, H\rangle=p \oplus H B^{r}
$$

where $\oplus$ is the Minkowski sum, and $B^{r}=[-1,1]^{r}$ is the $r$-dimensional unit box.

The zonotopes possess the following properties:

1. The Minkowski sum of zonotopes $\mathbb{Z}_{1}=\left\langle p_{1}, H_{1}\right\rangle$ and $\mathbb{Z}_{2}=\left\langle p_{2}, H_{2}\right\rangle$ is

$$
\begin{aligned}
\mathbb{Z}_{1} \oplus \mathbb{Z}_{2} & \triangleq\left\langle p_{1}, H_{1}\right\rangle \oplus\left\langle p_{2}, H_{2}\right\rangle \\
& =\left\langle p_{1}+p_{2},\left[H_{1} H_{2}\right]\right\rangle
\end{aligned}
$$

where $\left[H_{1}, H_{2}\right]$ is the concatenation of the generator matrices.
2. The linear mapping of a zonotopic set, $\mathbb{Z}$ by a vector or a matrix $\mathcal{K}$ is given by

$$
\mathcal{K} \odot\langle p, H\rangle=\langle\mathcal{K} p, \mathcal{K} H\rangle
$$

3. The smallest box (interval hull) containing the zonotope is described by $\square \mathbb{Z}=p \oplus r s(H) B^{r}$, where $r s(H)$ is a diagonal matrix such that $r s(H)_{i, j}=$ $\sum_{j=1}^{r}\left|H_{i, j}\right|$. Hence $\mathbb{Z} \subset \square \mathbb{Z}$.

Definition 2. (Robust positive invariant (RPI) set) Assume that a solution $\varphi\left(x_{0}, k\right)$ exists for a discrete time-invariant system $x(k+1)=A x(k)+B u(k)+w(k)$, $\forall w(k) \in \mathbb{W} . \quad \Omega \subseteq \mathbb{X}$ is defined as an RPI set if $\varphi\left(x_{0}, k\right) \in \Omega \forall x_{0} \in \Omega$ for all $k=\mathbb{N}_{[1, \ldots, \infty)}$, such that $(A+B K) \Omega \oplus \mathbb{W} \subseteq \Omega$.

Definition 3. (Minimal RPI (mRPI) set) An mRPI set $\Omega_{\infty}$ is the set contained in all possible RPI sets of a system as described in Definition 2.

## 3. Tube-based MPC

The fundamental intent of designing a robust MPC controller must be such that the designed controller satisfies the tenets of robust stability and recursive feasibility, robust constraint satisfaction and robust performance for all realizations of the system behaviour $\Sigma=f(k, x(k), u(k), d(k))$, subjected to unaccounted variations in function variables; in essence, the system must operate near normal in the event of some extent of uncertainties.

Assuming an additive demand uncertainty in (3), the effects of unknown uncertainties on the exogenous known demand variable $d(k), \Delta d(k) \subseteq \delta \mathbb{D}$ result in a subsequent variation in the state $\Delta x(k) \subseteq \delta \mathbb{X}$ and input variables $\Delta u(k) \subseteq \delta \mathbb{U}$ as evidenced from the affine relationships of the variables in Eqns. (2) and (3). These variations may result in feasibility as well as stability issues. The model variables can therefore be thought of as a composition of an uncertainty-free component and an unknown uncertain component dependent on the demand uncertainty, with the latter involving a realization of variables at each time instant from bounded uncertainty sets $(\delta \mathbb{X}, \delta \mathbb{U}, \delta \mathbb{D})$ with the assumption that the uncertain demand is unknown but bounded. State and input uncertainty sets $(\delta \mathbb{X}, \delta \mathbb{U})$ are
accordingly described as zonotopes generated from the known zonotopic bounded set of the demand uncertainty $\delta \mathbb{D}$. RPI sets are subsequently utilized in the tightening of original state and input constraints. In addition to that, assuming that in the presence of uncertainty, asymptotic stability to an equilibrium point cannot be achieved like the nominal case, robust asymptotic stability is guaranteed with a terminal set $\Omega_{\infty}$. Here $\Omega_{\infty}$ signifies a suitable region of attraction for the perturbed system ensuring stability and recursive feasibility.

Assumption 1. The states $x(k)$ and demands $d(k)$ are considered known at each time instant $k$ and the pair $(A, \bar{B})$ is controllable.
$\delta \mathbb{D}(k)$ is generated from a symmetric interval set considering a bounded demand uncertainty under additive uncertainty assumptions at each time instant $k$ such that $\delta d(k)_{l} \in[-\delta d(k)_{l}, \delta d(k)_{l}]$, where $l$ denotes a particular demand node in the network. The description of the set $\delta \mathbb{D}(k)$ is chosen appropriately to ensure that $\delta \mathbb{X}(k) \subset \operatorname{interior}(\mathbb{X})$ and $\delta \mathbb{U}(k) \subset \operatorname{interior}(\mathbb{U})$ (Mayne et al., 2005). The uncertain set $\delta \mathbb{D}(k)$ can therefore be represented in a zonotopic form as

$$
\delta \mathbb{D}(k) \triangleq[0]^{n_{d}} \oplus H_{d}(k) B^{n_{d}}
$$

where $[0]^{n_{d}}$ is a column vector of dimension $n_{d}$ ( $n_{d}$ is the number of demand nodes), considered as the centre of the zonotope and $H_{d}(k)$ is a time-varying diagonal matrix of the generators representing the bounds of variations at each demand node $j$ at each time instant $k \in \mathbb{N}_{\geq 0}: B^{n_{d}}$; $B=[-1,1]$.

Consider $\tilde{x}, \tilde{\tilde{u}}$ and $\tilde{d}$ as the real dynamic state, input and demand, respectively. Taking into account the uncertainty effects, the appropriate decomposition of model variables is therefore given as $\tilde{x}=x+\Delta x, \tilde{\tilde{u}}=$ $\tilde{u}+\Delta \tilde{u}$ and $\tilde{d}=d+\Delta d$.
$\Delta(\cdot)$ is the uncertain component of each variable. From (2) and (3), the DWN model taking account of the uncertainty in the demand variable is therefore given as

$$
\begin{gathered}
\tilde{x}(k+1) \triangleq A \tilde{x}(k)+\tilde{B} \tilde{\tilde{u}}(k)+\tilde{B}_{d} \tilde{d}(k) \\
0 \triangleq E_{u} \tilde{\tilde{u}}(k)+E_{d} \tilde{d}(k)
\end{gathered}
$$

Nominal states and inputs, $x \in \mathbb{R}_{+}^{n_{x}}, \tilde{u} \in \mathbb{R}_{+}^{n_{u}}$ are assumed to be bounded in a compact polyhedron $\mathbb{X}$ and $\mathbb{U}$, containing the origin in their interiors, with $\tilde{u} \subseteq \mathbb{U}$ and $x \subseteq \mathbb{X}$. In the presence of uncertainty, it is desirable to generate a tube of trajectories, meaning a sequence of RPI reachable sets such that for every transition of states and inputs of the nominal system, the resulting states and inputs after the effect of uncertainty remain in a closed and bounded set of the system constraints $(\mathbb{X}, \mathbb{U})$ as well as is asymptotically stable with respect to an approximate equilibrium set $\bar{\Omega}$; with RPI sets

$(\delta \mathbb{X}(k) \subseteq \mathbb{X}, \delta \mathbb{U}(k) \subseteq \mathbb{U}, \tilde{\Omega} \subset \mathbb{X})$. A state RPI tube, $\hat{X}=\left\{\hat{X}_{0}, \hat{X}_{1}, \ldots, \hat{X}_{N}\right\}, \forall \hat{X}_{k}=x(k) \oplus \delta \mathbb{X}(k)$ and an accompanying control tube $\tilde{U}=\left\{\tilde{U}_{0}, \tilde{U}_{1}, \ldots, \tilde{U}_{N}\right\}, \forall$ $\tilde{U}_{k}=\hat{u}(k) \oplus \delta \mathbb{U}(k)$, is constructed online taking account of the bounded uncertainty description and the centre of measured demands at $k$. Here $x(k)$ and $\hat{u}(k)$ are the centres of the respective propagated state and control RPI tubes.

The mismatches between nominal and real states influenced by uncertainties are mitigated by a local feedback controller $K$, in our case an LQR controller, such that the selection of this feedback gain, $K$ satisfies the system equations on the assumption that $\hat{d}(k)=0$,

$$
\Delta x(k+1) \triangleq(A+\hat{B} K) \Delta x(k)
$$

with $\Delta x(k) \subseteq \delta \mathbb{X}(k)$. The local controller ensures that the deviation of the system dynamics in the closed-loop with system matrix $A+\hat{B} K$ is asymptotically stable. The primary aim is to have an optimal control problem, which keeps trajectories around the neighbourhood of the nominal optimal trajectory in the presence of uncertainties, for $\tilde{x}(0) \in x(0)+\delta \mathbb{X}$, therefore minimizing the spread of trajectories.

Remark 2. Assume that $A+\hat{B} K$ is strictly stable and $\tilde{x}=x+\Delta x$, with an uncertain dynamic part $\Delta x(k+$ $1) \triangleq(A+\hat{B} K) \Delta x(k)+\hat{B}_{d} \Delta d(k)$. Since $\delta \mathbb{X}$ is an RPI, $(A+\hat{B} K) \delta \mathbb{X} \oplus \hat{B}_{d} \delta \mathbb{D} \subseteq \delta \mathbb{X} \subset \mathbb{X}$, it can be inferred that the transition of states from one time instant to another with any control law $\pi(u(x))$ depends on the dynamics of the centres, $x(k+1)=A x(k)+\hat{B} \hat{u}(k)+\hat{B}_{d} d(k)$.

### 3.1. Online computation of zonotopic reachable sets.

The feedback gain $K$ is computed and kept constant at each time instant $k$ throughout the prediction horizon of the MPC controller to minimize the deviation of the perturbed state and ensures asymptotic stability to a predefined terminal set. An optimal local controller for state error minimization,

$$
\begin{aligned}
J_{\left[\hat{u}_{0}, \ldots, \hat{u}_{m}\right]}= & \sum_{i=0}^{m}(\tilde{x}(k)-x(k))^{T} Q(\tilde{x}(k)-x(k)) \\
& +\hat{\tilde{u}}(k)^{T} R \hat{\tilde{u}}(k)
\end{aligned}
$$

where $Q$ is semi-positive definite and $R$ positive definite, is proposed. Here $\tilde{x}(k)$ is the actual state at time $k$ from the plant under uncertainty and $\hat{\tilde{u}}$, the actual inputs, with $x(k)$ as the nominal state prediction from the MPC at time instant $k$. From the actual state, $\tilde{x}(k)$ (i.e., $\tilde{x}(k)=x(k)+$ $\Delta x(k)$ ), the uncertain dynamic part is

$$
\Delta x(k+1) \triangleq(A+\hat{B} K) \Delta x(k)+\hat{B}_{d} \Delta d(k)
$$

where $\Delta \hat{u}=K \Delta x$.

From the uncertain component, the corresponding length of the tube $N_{p} \in \mathbb{N}_{>0}$ is computed at every $k$, where $N_{p}$ is the selected prediction horizon of the MPC controller. Therefore, the set $\delta \mathbb{X}$ corresponding to the realization of the error $\Delta x$ assuming that $\Delta x(0)=0$ can be described as

$$
\delta \mathbb{X}(k+i) \subseteq \bigoplus_{j=1}^{i}(A+\hat{B} K)^{i-j} \hat{B}_{d} \delta \mathbb{D}(i)
$$

From $\delta \mathbb{D}(i)=0 \oplus H_{d}(i) B^{n d}$ and Properties 1 and 2 of zonotopes, it follows that

$$
\begin{gathered}
\delta \mathbb{X}(k+i) \subseteq 0 \oplus \Psi_{[1, i]}(i) B^{n_{d}} \\
\Psi_{[1, i]}(i)=\bigoplus_{j=1}^{i}(A+\hat{B} K)^{i-j} \hat{B}_{d} H_{d}(i)
\end{gathered}
$$

The control variable $\hat{\tilde{u}}$ at each time instant can be described as

$$
\hat{\tilde{u}}_{k}=\hat{u}_{k}+K \Delta x_{k}
$$

where $\hat{u}(k)$ is the certain control variable obtained from the nominal MPC at time instant $k$. From (2), and under decomposition into certain and uncertain parts, given that the actual control variable $\hat{\tilde{u}}_{k}, \hat{\tilde{u}} \in \delta \mathbb{U}$, the uncertain control RPI set is

$$
\delta \mathbb{U}(k+i) \subseteq \hat{P} \hat{M}_{1} K \delta \mathbb{X}(k+i) \oplus \hat{P} \hat{M}_{2} \delta \mathbb{D}(k+i)
$$

The sequence of cross-sections of the control tube can therefore be described in a zonotopic form as

$$
\begin{aligned}
\delta \mathbb{U}(k+i) \subseteq & 0 \oplus\left[\hat{P} \hat{M}_{1} K \Psi_{[1, i]}(K+i)\right. \\
& \left.\left.\hat{P} \hat{M}_{2} H_{d}(k+i)\right] B^{2 n_{d}}\right.
\end{aligned}
$$

3.2. Terminal state constraint set. For robust stability and recursive feasibility, a terminal constraint set is formulated considering an mRPI as done by Raković et al. (2005). A terminal mRPI set $\tilde{\Omega}$, which is compact and convex, is constructed as an outer approximation of the exact equilibrium state set

$$
\Omega_{\infty} \triangleq \bigoplus_{j=0}^{\infty}(A+\hat{B} K)^{j} \hat{B}_{d} \delta \mathbb{D}
$$

where $\Omega_{\infty} \subseteq \tilde{\Omega} .(A+\hat{B} K)=\hat{A}$ and $\hat{B}_{d} \delta \mathbb{D} \subseteq \mathcal{W}$, under the assumption that $\hat{A}$ is strictly stable. An outer set approximation of $\Omega_{\infty}$ is defined if there exist a certain $k$ $\in \mathbb{N}_{>0}$ such that, $(\hat{A})^{k} \mathcal{W} \subseteq \alpha \mathcal{W}, \forall \alpha=[0,1)$.

The infinite Minkowski sum of sets (22) under strict stability conditions ensures that convergence is

guaranteed. Considering the infinite Minkowski sum,

$$
\begin{aligned}
\bigoplus_{j=0}^{\infty}(\hat{A})^{j} \mathcal{W} \subseteq & \bigoplus_{j=0}^{k-1}(\hat{A})^{j} \mathcal{W} \oplus \bigoplus_{j=k}^{2 k-1}(\hat{A})^{j} \mathcal{W} \\
& \oplus \bigoplus_{j=2 k}^{3 k-1}(\hat{A})^{j} \mathcal{W} \oplus \ldots
\end{aligned}
$$

(23) can be simplified to achieve the condition $(\hat{A})^{k} \mathcal{W} \subseteq$ $\alpha \mathcal{W}$ as follows:

$$
\begin{aligned}
& \bigoplus_{j=0}^{\infty}(\hat{A})^{j} \mathcal{W} \subseteq \bigoplus_{j=0}^{k-1}(\hat{A})^{j} \mathcal{W} \oplus \bigoplus_{j=0}^{k-1}(\hat{A})^{j}(\hat{A})^{k} \mathcal{W} \\
& \oplus \bigoplus_{j=0}^{k-1}(\hat{A})^{j}(\hat{A})^{2 k} \mathcal{W} \oplus \ldots
\end{aligned}
$$

From $(\hat{A})^{k} \mathcal{W} \subseteq \alpha \mathcal{W}$, it can be stated that $(\hat{A})^{n k} \mathcal{W} \subseteq$ $\alpha^{n} \mathcal{W} . \bigoplus_{j=0}^{k-1}(\hat{A})^{j} \mathcal{W}$ is thus convex and compact since $\delta \mathbb{D}$ is assumed to have the same properties. Writing $\bigoplus_{j=0}^{k-1}(\hat{A})^{j} \mathcal{W}$ as $\zeta, \Omega_{\infty}$ is approximated from a truncation of (24) as

$$
\tilde{\Omega} \subseteq\left(1+\alpha+\alpha^{2}+\ldots\right) \zeta
$$

which results in an approximated set

$$
\tilde{\Omega} \subseteq \frac{1}{1-\alpha} \zeta
$$

The set in a zonotopic form is given as

$$
\tilde{\Omega} \subseteq 0 \oplus(1-\alpha)^{-1} \Psi_{[0, k]} B^{n_{d}}
$$

where

$$
\Psi_{[0, k]}=\bigoplus_{j=0}^{k-1}(\hat{A})^{j} \hat{B_{d}} \hat{H_{d}}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. State transition in RMPC, showing the constraint set (solid box), the $m R P I$ (dash black lines) and RPIs (interior polygons)
$\hat{H}_{d}$ is taken as the worst-case demand uncertainty in reference to the demand profile of each node. The size of the set is therefore dependent on the design parameter $\alpha$, the description of the uncertainty set $\delta \mathbb{D}$ and the appropriate selection of $k$.

Remark 3. The constructed approximated mRPI approaches the actual mRPI if, for a significantly small $\alpha \in(0,1]$, there exists a finite $k$ chosen large enough, such that $(\hat{A})^{k} \mathcal{W} \subseteq \alpha \mathcal{W}$. The appropriate selection of $\alpha$ and $k$ is discussed by Raković et al. (2005).

The constructed sequence of uncertain zonotopic sets and the terminal set will then be used in the the design of the robust eMPC by considering only alterations in the constraints and inclusion of the terminal set.

## 4. Evaluation of a DWN reliability

Definition 4. Reliability is defined as the capability of an item to perform a required function, under given environmental and operational conditions and for a stated period of time (ISO8402).

Evaluating the reliability of a system is a complex stochastic undertaking that calls for the application of appropriate statistical inference techniques in order to model such a phenomenon (Cai et al., 2020). In this section, the concept of Bayesian networks (BNs), fundamentally based on the structure of the DWN using graph theory, taking account of conditional dependencies between graph nodes (i.e., actuators in the network) related through arcs (flow in pipes) is considered.

For a BN parameter, we make use of a quantitative index of failure rate, $\lambda(t)$, which makes it possible to evaluate individual reliabilities of components, that is, the probability of each function component for a specified time. This information is then used in the broad BN modelling according to the structure of the network. Keeping in mind that the ultimate goal is to introduce the reliability in the performance index and the constraints, the dynamic nonlinear network reliability model from a dynamic BN is represented in a pseudo-linear form, avoiding any additional computational burden, basically escaping a laborious nonconvex problem.
4.1. Reliability based on the component failure rate. Consider a continuous random variable $T$ denoting the time to failure having a distribution function $F(t)$, where $F(t)$ signifies the probability of a component to fail within the time interval $(0, t]$ (Rausand and Hoyland, 2004). Then with an associated probability density function, $f(t), F(t)$ can be described as

$$
F(t)=\operatorname{Pr}(T \leq t)=\int_{0}^{t} f(u) \mathrm{d} u, \quad \forall t \geq 0
$$

Conversely, the reliability of the component $R(t)$ is accordingly represented as the probability of survival in time interval $(0, t]$ and subsequently functioning at $t$,

$$
\begin{aligned}
R(t) & =\operatorname{Pr}(T \geq t)=1-\int_{0}^{t} f(u) \mathrm{d} u \\
& =\int_{t}^{\infty} f(u) \mathrm{d} u \quad \forall t \geq 0
\end{aligned}
$$

Similarly, to evaluate the failure rate, the instance of an element functioning at $t$ is considered, such that the probability of failing in the interval $[t, t+\Delta t]$ having survived to $t$ is represented with a conditional probability as

$$
\begin{aligned}
\operatorname{Pr}(t & <T \leq t+\Delta t \mid T>t) \\
& =\frac{\operatorname{Pr}(t<T \leq t+\Delta t)}{\operatorname{Pr}(T>t)} \\
& =\frac{F(t+\Delta t)-F(t)}{R(t)}
\end{aligned}
$$

dividing both sides by $\Delta t$. As $\Delta t \rightarrow 0$, the failure rate of the component is thus

$$
\lambda(t)=\lim _{\Delta t \rightarrow 0} \frac{F(t+\Delta t)-F(t)}{\Delta t} \frac{1}{R(t)}=\frac{f(t)}{R(t)}
$$

A relationship can therefore be established between the failure rate $\lambda(t)$ and the reliability function $R(t)$ from (31) considering the probability density function of the failure distribution in (28) as

$$
f(t)=\frac{\mathrm{d} F(t)}{\mathrm{d} t}=\frac{\mathrm{d}(1-R(t))}{\mathrm{d} t}=\frac{-\mathrm{d}(R(t))}{\mathrm{d} t}
$$

From the formula for the failure rate (31) it follows that

$$
\lambda(t)=\frac{\mathrm{d} R(t)}{\mathrm{d} t} \cdot \frac{1}{R(t)}=-\frac{\mathrm{d}}{\mathrm{~d} t} \ln R(t)
$$

Note that $R(0)=1$. Therefore,

$$
\begin{gathered}
\int_{0}^{t} \lambda(t) \mathrm{d} t=-\ln R(t) \\
R(t)=e^{-\int_{0}^{t} \lambda(u) \mathrm{d} u}
\end{gathered}
$$

where (35) provides a relationship between the reliability of a component and the failure rate.

A plethora of methods have been proposed for finding a suitable function for failure rates that approximately represents a component's functional property decay over time. In this paper, we consider the effect of loadings on the failure rate as done by Karimi Pour et al. (2019) and establish a load versus failure rate relationship, such that an exponential function
establishing the relationship between each actuator, the $i$-th failure rate and their corresponding loadings is

$$
\lambda_{i}(t)=\lambda_{i}^{0} e^{\beta_{i} u_{i}(t)}
$$

where $\lambda_{i}^{0}$ is the baseline failure rate, $u_{i}(t)$, the control effort of each actuator and $\beta_{i}$ is a constant parameter that depends on the actuator characteristics. Therefore, under nominal operating conditions, the reliability is characterized as

$$
R_{0, i}(t)=e^{-\lambda_{i}^{0}(t)}
$$

The following equation therefore holds for the probability of a component avoiding failure within the time interval $(0, t]$ considering the failure rate: and the nominal failure rate:

$$
R_{i}(t)=R_{0, i} e^{-\int_{0}^{t} \lambda_{i}(u) \mathrm{d} u}
$$

Consequently, the discrete-time representation, taking into account loading at different time instances, $k$, sampled at $T_{s}$ is

$$
R_{i}(k)=R_{0, i} e^{-T_{s} \sum_{s=0}^{k} \lambda_{i}(u(s))}
$$

4.2. Bayesian network theory. Consider the triple, $B_{N}=\left(P, A_{B}, N_{B}\right)$ representing a BN. $B_{N}$ is therefore a Bayesian network, essentially a directed acyclic graph (DAG) composed of a set of nodes $N_{B}$, with the corresponding set of arcs, $A_{B}$, accounting for direct dependencies between nodes. Each node $n_{i} \in N_{B}$ is subsequently associated with a probability distribution from the set $P$. From Fig. 2, the relationship between nodes $n_{1}$ and $n_{2}$ is such that $\left(n_{1}, n_{2}\right) \in A_{B} ; n_{1}$ is therefore defined as the parent of $n_{2}$. Hence $n_{2}$ possesses a direct dependency to $n_{1}$. The set of parent nodes of each node $n_{i}$ in the network is denoted by $P_{a}\left(n_{i}\right)$. The direct dependencies of each node with its parents $P_{a}\left(n_{i}\right)$ is consequently computed considering the conditional probability distribution, $P_{r}\left(n_{i} \mid P_{a}\left(n_{i}\right)\right), P_{a}\left(n_{i}\right) \neq \emptyset$.

Assigning a discrete random variable $Y_{i}$ to each node $n_{i} \subset N_{B}$, a finite number of $m$ states set, $S^{n}$, can be established for each node such that $S^{n} \triangleq$ $\left\{s_{1}^{n}, s_{2}^{n}, \ldots, s_{m}^{n}\right\}$, under trivial Bayesian assumptions of $s_{i}^{n} \cap s_{j}^{n}=, \forall i \neq j, \operatorname{Pr}\left(s_{i}^{n}\right) \geq 0$ and $\operatorname{Pr}\left(\bigcup_{i=1}^{m} s_{i}^{n}\right)=$ 1 , where $\operatorname{Pr}\left(Y_{i}=s_{i}^{n}\right)$ is the marginal probability that the state of node $n_{i}$ is $s_{i}^{n}$. Therefore for an acyclic graph $B_{N}\left(P, A_{B}, N_{B}\right), \forall n\left(N_{B}\right)=N$ with designated probability distributions $\operatorname{Pr}\left(Y_{1}, Y_{2}, \ldots, Y_{N}\right)$, the joint probabilities of the nodes under conditional probability assumptions and using the chain rule is simplified as

$$
\operatorname{Pr}\left(n_{i}, n_{2}, \ldots, n_{N}\right)=\operatorname{Pr}\left(n_{1}\right) \prod_{i=2}^{N} \operatorname{Pr}\left(n_{i} \mid P_{a}\left(n_{i}\right)\right)
$$

where, $n_{1}$ is considered a root node, $\therefore P_{a}\left(n_{1}\right)=\emptyset$. Note that only prior probabilities are assigned to these nodes.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Two nodes in a simple acyclic graph, showing direct dependencies between nodes.
4.2.1. Dynamic Bayesian network. The Bayesian representation thus far presented in (40) is static; therefore, to successfully include the reliability dynamics in the MPC, a temporal dimension that describes the time connection between two time instances of actuator loadings is added. Thus, temporal dependencies in the modelling are introduced. For temporal dependencies in BNs, the assumption is made that the system is a first-order Markov model, that is, (i) the arcs between nodes are located in the same time period between instances or two neighbouring ones, (ii) time homogeneous parameters of the conditional probability are time invariant. Hence, the transition probability of a random variable $X_{i}$ of the reliability of each node $n_{i} \in N_{b}$ between two time instances, say, $k+1$ and $k$, with two states, $F$ as a failed state and $A$ as active, is given as

$$
\begin{aligned}
\operatorname{Pr}\left(X_{i}(k+1)\right) & =\left(A \mid X_{i}(k)=A\right) \\
& =R_{0, i} e^{-T_{s} \sum_{s=0}^{k} \lambda_{i}(u)} \\
\operatorname{Pr}\left(X_{i}(k+1)\right) & =\left(F \mid X_{i}(k)=A\right) \\
& =1-R_{0, i} e^{-T_{s} \sum_{s=0}^{k} \lambda_{i}(u)}
\end{aligned}
$$

4.3. Bayesian network structure modelling of a DWN. The procedure of BN representation of a system primarily depends on the structuring and parameter definition stages, with the latter dependent on the acyclic graphical representation of the system under study. The DWN with its modelling, as discussed in Section 2, involves a graphical representation of actuators as nodes that are linked by unidirectional flows through pipes as arcs; hence an acyclic graph is duly presented. From the graph, based on minimum path sets in the network, that is, the set of successful paths from the source to the demand, a series-parallel arrangement is attained for the network reliability model. The BN parameter definition however is defined on the pair of probabilities of the root nodes and the conditional probabilities of nodes and their parents in individual minimum paths of the network. Therefore,
the network reliability with the conditions prescribed at a certain time instant $k$ according to the structure of the network is

$$
R_{s}(k)=1-\prod_{j=1}^{s}\left(1-\prod_{i \in P_{j}} R_{i}(k)\right)
$$

where $P_{j}$ is a minimum path set and $R_{i}$ is the reliability of each node in the set taking account of prior and conditional probabilities.

The reliability term $R_{i}$ from (37) includes exponential terms from the failure rate, introducing nonlinearities. To aid in including the reliability term in the MPC, the logarithm of both sides is taken and subsequently represented in a pseudo-linear form such that

$$
\log \left(R_{s}(k)\right)=\log \left(\prod_{j=1}^{s}\left(1-\prod_{i \in P_{j}} R_{i}(k)\right)\right.
$$

Setting

$$
1-\prod_{i \in P_{j}} R_{i}(k)
$$

as $\varphi_{j}(k)$, we get

$$
\log \left(R_{s}(k)\right)=\sum_{j=1}^{s} \log \varphi_{j}(k)
$$

where

$$
\log \left(\varphi_{j}(k)\right)=\frac{\log \left(\varphi_{j}(k)\right)}{\log \left(1-\varphi_{j}(k)\right)} \sum_{i \in P_{j}} \log \left(R_{i}(k)\right)
$$

Thus, with $\frac{\log \left(\varphi_{j}(k)\right)}{\log \left(1-\varphi_{j}(k)\right)}$ as $\vartheta_{j}(k)$, the reliability of the network is given as

$$
\log \left(R_{s}(k)\right)=\sum_{i \in P_{j}}^{s} \vartheta_{j}(k) \sum_{i \in P_{j}} \log R_{i}(k)
$$

Therefore, for the DBN formulation in (41) and the baseline reliability, the dynamic model is

$$
\begin{aligned}
\log \left(R_{s}(k+1)\right)= & \log \left(R_{s}(k)\right) \\
& +\sum_{i \in P_{j}}^{s} \vartheta_{j}(k) \sum_{i \in P_{j}} \log R_{i}(k)
\end{aligned}
$$

## 5. Reliability-aware eMPC of the DWN

In this section, the reliability-aware robust control problem is discussed taking account of all procedures in the preceding sections. Since the reliability model in (47) is nonlinear, a quasi-LPV (qLPV) nonlinear representation of the nonlinear model through the

embedding of nonlinearities in scheduling parameters $(\theta(k))$ is formulated. The time-varying matrices of appropriate dimensions representing the qLPV approximate model are hence

$$
\begin{gathered}
A_{r}(\theta(k))=\left[\begin{array}{cc}
1 & \sum_{i \in P_{j}}^{s} \vartheta_{j}(k) \\
0_{n_{u} \times 1} & \mathbb{1}_{n_{u} \times n_{u}}
\end{array}\right] \\
B_{r}(\theta(k))=\left[\begin{array}{c}
0_{1 \times n_{u}} \\
-\lambda_{i}(k) \cdot \mathbb{I}_{n_{u} \times n_{u}}
\end{array}\right]
\end{gathered}
$$

where

$$
\begin{aligned}
& A_{r}(\theta(k)) \in \mathbb{R}^{\left(n_{u}+1\right) \times\left(n_{u}+1\right)} \\
& B_{r}(\theta(k)) \in \mathbb{R}^{\left(n_{u}+1\right) \times n_{u}}
\end{aligned}
$$

and with states

$$
x_{r}=\left[\log \left(R_{s}\right), \log \left(R_{1}\right), \ldots, \log \left(R_{n_{u}}\right)\right] \in \mathbb{R}^{n_{u}+1}
$$

Therefore, the reliability model (41) is included as additional dynamics in the constraints with a new performance index for the network reliability enhancement, $\mathcal{J}_{B}$. The MPC is robustified by only updating the constraints considering $\mathbb{U} \oplus \delta \mathbb{U} \subseteq \mathcal{U}$ and $\mathbb{X} \oplus \delta \mathbb{X} \subseteq \mathbb{X}$ and robust asymptotic stability with the terminal set $\tilde{\Omega}$. Thus, the complexity is similar to that for the nominal case.

The cost function with the additional term of reliability, $\mathcal{L}(k, \hat{u}, x) \in \mathbb{N}_{+} \times \mathbb{R}^{n_{u}} \times \mathbb{R}^{n_{x}} \rightarrow \mathbb{R}_{+}$

$$
\begin{aligned}
\mathcal{L}(k, \hat{u}, x)= & \Lambda_{1} \mathcal{J}_{s}(k)+\Lambda_{2} \mathcal{J}_{\triangle \hat{U}}(k)+\Lambda_{3} \mathcal{J}_{E}(k) \\
& -\Lambda_{4} \mathcal{J}_{B}(k)
\end{aligned}
$$

The reliable ReMPC controller is therefore defined as follows:

$$
\min _{\hat{\mathbf{u}}(k), \mathbf{x}(k), x_{r}(k)} \sum_{i=0}^{N_{p}-1} \mathcal{L}(k, \hat{u}(k), x(k))
$$

subject to

$$
\begin{aligned}
x(i+1 \mid k) & =A x(i \mid k)+\hat{B} \hat{u}(i \mid k)+\hat{B}_{d} d(i \mid k) \\
\hat{u}(i \mid k) & \subseteq \mathcal{U}(i \mid k) \ominus \square \delta \mathbb{U}(i \mid k) \\
x(i+1 \mid k) & \subseteq \mathbb{X} \ominus \square \delta \mathbb{X}(i \mid k) \\
x(i \mid k) & \geq x_{s}-\varepsilon(i \mid k) \\
x\left(N_{p}-1 \mid k\right) & \subseteq \tilde{\Omega} \\
x_{r}(i+1 \mid k) & =A_{r}(\theta(k)) x_{r}(i \mid k)+B_{r}(\theta(k)) u(i \mid k) \\
x_{r}(i \mid k) & \subseteq(0,1]
\end{aligned}
$$

where $\ominus$ is the Pontryagin difference of the sets. From the control parameterization, the control input to the plant at every time instance $k$ is given by

$$
u^{*}(0 \mid k)=\hat{P} \hat{M}_{1} \hat{u}^{*}(0 \mid k)+\hat{P} \hat{M}_{2} \hat{d}(k)+K \Delta x(k)
$$

where $\hat{d}(k)$ is the forecasted demand.

## 6. Application example

To demonstrate the capabilities of the proposed controller, first for robustness, an additive demand uncertainty taken as the variation around the demand profile is considered as shown in Fig. 3. This scenario of actual demand is assumed to test the level of robustness of the controller. With a prediction horizon of 24 h (a day of water supply) and a sampling time of 1 h , the robust MPC optimization problem considering reliability (5) is solved with CPLEX ${ }^{\circledR}$ QP solver using Matlab ${ }^{\circledR}$ R2019b (64 bits) and a PC with an Intel Core i7 of 8 GB RAM. An aggregate network of the Barcelona water network, Fig. 4, composed of 17 tanks, 61 actuators and 25 demand nodes is used as a case study. Tanks store water during off peak hours and supply water when demand is at peak or in the occasions of unexpected demand and supply scarcity. This presents a cyclic actuator behaviour in relation to the peak-off peak demand profile. An acyclic graph of the network showing relationships between nodes (actuators) linked by unidirectional pipes (arcs) is used for the network and reliability models. The following assumptions are made: (i) sources supply the required amount of water to demands; (ii) the pipes and tanks of the network are always reliable, and (iii) the actuators at the start of simulation correspond to a perfectly reliable value of 1 .

The minimum paths $P_{j}$, which is the set of successful paths from source to demand, through an ensemble of components (pipes, valves and tanks) evaluates the reliability of each path, considering only the actuators. The various paths are then lumped for a network reliability measure, considering their series-parallel arrangement, taking each path as a single entity. Table 1 shows some traced minimal paths in the network; there are 607 minimal paths in total.

The robustness of the designed controller is tested taking Tank 1 (d125PAL) and its associated elements as reference, as shown in the WDN network (Fig. 3). Tank 1 is directly connected to demand node c125PAL and the nearest supply actuators are CPIV and bMS. These actuators are chosen since they show major changes when there are demand alternations.

An eight-day demand profile, subdivided into an 80

Table 1. Examples of minimum cost paths in the network.


![img-2.jpeg](img-2.jpeg)

Fig. 3. 24-Hour demand profile of node C129PAL with a symmetric bounded uncertainty.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Barcelona drinking water network.
hour test scenario, is used for the simulations as shown in Fig. 5. In the first two regions, the extremities of the controller are tested. Additive uncertainty is added until the nominal controller ceases to be feasible, thus labelled as real demand. This is not shown in the plots, since the nominal MPC control is intractable in these regions. The last region is the nominal loading condition.

As shown in Figs. 6 and 7, during the first and second stages of the demand profile, the actuators work to offset
the demand variation aided by the tank in Fig. 8. Since the stored reserve in d125PAL is exhausted in the first region, the actuators function to retain supply to the demand, while respecting their own constraints, the feasibility of the control. This is especially evident considering Fig. 7 (bMS), which shows the controller just maintaining feasibility which was otherwise not the case with the nominal MPC.

![img-4.jpeg](img-4.jpeg)

Fig. 5. 80-Hour test scenarios for robust control for demand node c125PAL.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Control action of CPIV.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Control action of bMS.

In Fig. 8, the level of water in the tank in the first region is emptied to satisfy the added demand, but the stability and recursive feasibility are preserved due to the RMPC control. The tank start restocking in the second region and finally converges to the nominal conditions in the third region. Figure 9 shows that with the inclusion of the reliability cost, not only there is a short term economic gain, but also there is a safe operation of the network in the long run. Thus reliable actuators against faults minimizing downtime and maintenance costs.

But the improvement of the reliability is not cheap since the problem presented has two primary conflicting objectives of improving the reliability and minimizing the cost of operations, the short term cost of operation. A set of weights are selected to show the effect of the included reliability index on the cost of operation presented in a Pareto front presented in Fig. 11. The selection of appropriate weights is a designer discretion but an optimal solution or point on the front can be sought taking into account the long run economic gain of considering reliability in the control framework. Since the aim of the added reliability index is to achieve a long-term gain, the marginal loss in the short term economical gain, as shown in Fig. 10, can be accommodated.

## 7. Conclusion

In this paper, the improvement of the reliability of a DWN is considered through appropriate controller design that takes into account a model of the network's reliability, by means of Bayesian network modelling. The resulting nonlinear dynamic Bayesian model is represented in a pseudo-linear form, easing the computational cost. Our results show an improved reliability of the network when the reliability index is added, at the expense of a marginal cost of operation, which was seen to be minimal, thus offering a long-term economic gain. Here the forecasted demand is uncertain, which makes the control problem more realistic, and a tube based ReMPC is designed with zonotopic sets to ensure that the controller operates close to normal in the presence of an unknown but bounded uncertainty.

The robustness of the controller is tested with additive loads from a symmetric bounded demand profile on the known forecasted load. Our results demonstrate the efficacy of the designed desirable controller simultaneously with robust constraint satisfaction, recursive feasibility and robust performance. In consequence, a more realistic controller suitable for real life deployment is proposed which takes into account DWN network reliability.

Table 2. Cost and reliability for different selections of weights.


## Acknowledgment

This work has been co-financed by the Spanish State Research Agency (AEI) and the European Regional Development Fund (ERFD) through the project SaCoAV (ref. MINECO PID2020-114244RB-I00), by the European Regional Development Fund of the European Union in the framework of the ERDF Operational Program of Catalonia 2014-2020 (ref. 001-P-001643 Looming Factory), and by the DGR of Generalitat de Catalunya (SAC group ref. 2017/SGR/482).
