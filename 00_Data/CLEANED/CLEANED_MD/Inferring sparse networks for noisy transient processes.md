# Inferring sparse networks for noisy transient processes 

Hoang M. Tran ${ }^{1,2}$ \& Satish T.S. Bukkapatnam ${ }^{1}$


#### Abstract

Inferring causal structures of real world complex networks from measured time series signals remains an open issue. The current approaches are inadequate to discern between direct versus indirect influences (i.e., the presence or absence of a directed arc connecting two nodes) in the presence of noise, sparse interactions, as well as nonlinear and transient dynamics of real world processes. We report a sparse regression (referred to as the $\ell_{1}$-min) approach with theoretical bounds on the constraints on the allowable perturbation to recover the network structure that guarantees sparsity and robustness to noise. We also introduce averaging and perturbation procedures to further enhance prediction scores (i.e., reduce inference errors), and the numerical stability of $\ell_{1}$-min approach. Extensive investigations have been conducted with multiple benchmark simulated genetic regulatory network and Michaelis-Menten dynamics, as well as real world data sets from DREAM5 challenge. These investigations suggest that our approach can significantly improve, oftentimes by 5 orders of magnitude over the methods reported previously for inferring the structure of dynamic networks, such as Bayesian network, network deconvolution, silencing and modular response analysis methods based on optimizing for sparsity, transients, noise and high dimensionality issues.


Many real world processes including biological ${ }^{1,2}$, socio-economics ${ }^{3,4}$, and engineering systems ${ }^{5}$, can be represented as large scale dynamic networks ${ }^{6}$. The multitude of state variables of the process represent the network nodes and the arcs represent the dynamic coupling between pairs of state variables. Inferring the structure of these networks is critical for multiple purposes such as identifying key causal relationship, clustering, partitioning or reducing the system state space; thereby facilitating effective prediction, control and/or interventions of its underlying processes. For example, inferring the signaling pathways of the gene p53 was noted to be crucial towards advancing cancer treatment ${ }^{7}$.

Real world processes exhibit nonlinear dynamics and they almost always occur in transient conditions. Identifying the structure, especially the existence or absence of a direct dynamic coupling between the variables of such systems has been noted to be a standing challenge of modern science ${ }^{8}$, and the underlying causal mechanisms remain largely undiscovered. Most often, only noisy measurements of the network outputs in the form of a small ensemble of time series data are available for network inference ${ }^{9-13}$. The use of conventional system identification approaches can produce many spurious links due to the transitivity of influences among the nodes. Several methods for network inference notably based on Bayesian update ${ }^{14-19}$, Granger causality and multivariate autoregressive ${ }^{20-24}$, partial correlation ${ }^{25}$, network deconvolution (ND) ${ }^{26}$, network silencing ${ }^{27}$ and conditional causal relation ${ }^{28-31}$ have been investigated to filter the effect of indirect influences. When the time series gathered under transient conditions were available, a Modular Response Analysis (MRA) ${ }^{32-34}$ method was proposed to infer the network structure at each time point. However, these methods suffer from serious drawbacks such as they mostly assume the system to exhibit linear and time-invariant dynamics ${ }^{26}$, determinism (noise-free) ${ }^{33-35}$, and/or the existence of a point attractor under steady state ${ }^{27}$. While MRA method can be employed to reconstruct dynamics under transient conditions ${ }^{33}$, its performance deteriorates sharply in the presence of noise and the method encounters severe numerical stability issues, especially when the underlying dynamics is highly nonlinear. This tends to severely restrict its applicability to real world processes. Notably, the earlier methods essentially focus on dealing with each of the following scenarios including transient time series ${ }^{33}$, noisy measurements ${ }^{14-19}$, and indirect influence removal ${ }^{14-25,33}$ separately. The realistic scenario combining all these scenarios has not been considered. All available methods literally break down when presented with this scenario.

Towards addressing this gap, we introduce an approach based on modifying ND, silencing and MRA methods to account for sparsity, transients, noise and high dimensionality issues. Specifically, we have investigated a sparse

[^0]
[^0]:    ${ }^{1}$ Department of Industrial \& Systems Engineering, Texas A\&M University, College Station, TX 77840, USA. ${ }^{2}$ School of Applied Mathematics \& Informatics, Hanoi University of Science \& Technology, Hanoi, Vietnam. Correspondence and requests for materials should be addressed to S.T.S.B. (email: satish@tamu.edu)

![img-0.jpeg](img-0.jpeg)

Figure 1. Illustration of direct and total influence. The total influences in (b) are the accumulation of the influences transited through all paths in (a). For example, the total influence 1 → 4 in (b) is the accumulation of the influence transited through the paths 1 → 3 → 2 → 4 and 1 → 2 → 4.

regression (henceforth referred to as the ℓ_{1}-min) formulation to recover the structure of dynamic networks from noisy data gathered under transient conditions. Our main contribution is in providing a theoretical bound on the constraints of the ℓ_{1}-min formulation and providing stable numerical procedures that overcome effects of nonlinear couplings in large interconnected processes, availability of only a small sample of short time series ensembles, and inaccuracies in estimating noise levels. These bounds mitigate tedious trial and error procedures employed customarily as part of ℓ_{1}-min implementations1,34–36. The theoretical results and subsequent experimental studies suggest that the present ℓ_{1}-min approach is more robust to noise compared to the contemporary dynamic Bayesian network14–19 as well as NDs26,27,32. It is shown that up to 5 orders of magnitude reduction in the inference error are possible from the present approach, leading to a more accurate inference of the network structure for complex real world networks.

# Methods 

Towards a more formal treatment, we define a real world system as high dimensional coupled differential equation of the form

$$
\frac{d \mathbf{x}}{d t}=\mathbf{f}(\mathbf{x}, \mathbf{p})
$$

or

$$
\mathbf{x}(t)=\mathbf{\Phi}(t, \mathbf{x}(\tau))
$$

where $\mathbf{x} \in M \subset \mathbb{R}^n$ is a state vector, $\mathbf{p}$ is the parameter vector, $\mathbf{x}(\tau)$ is an initial condition. As noted in the foregoing, such dynamics can also be represented in form of a network37 shown in Fig. 1, where the node $i$ represents the state variable $x_{i}$ and a directed arc represents the existence and the strength of the coupling (direct influence) $s_{ij}$ between node $i$ and node $j$. In this context, the direct influence $s_{ij}(t)$ of node $j$ on node $i$ around a certain point $\mathbf{x}$ in the state space defined in Eq. (1) can be expressed as

$$
s_{ij}(t) \triangleq \frac{\partial x_{i}}{\partial x_{j}(\tau)} = \frac{\partial \Phi_i(t, \mathbf{x}(\tau))}{\partial x_{j}(\tau)}.
$$

It may be noted that, a node $j$ is connected to a node $i$ at time $t$ if $s_{ij}(t) \neq 0$. Hence, $S(t) = (s_{ij}(t))$ captures the physical structure of the dynamical system (1) at time $t$. In practice, $S(t)$ needs to be inferred from the measurements of the total influence $g_{ij}(t)$ between every pair of nodes26,27 or estimated from time series outputs of the dynamic system gathered under transient conditions33. The total influence $g_{ij}(t)$ is the sum of the direct influence of node $j$ on node $i$ and all indirect influences from node $j$ to node $i$ through other nodes connecting to both of them (see Fig. 1b). For example, total influence from 1 → 4, $g_{41}(t)$ is the sum of indirect influences along the paths 1 → 3 → 2 → 4 and 1 → 2 → 4, or $g_{41}(t) = s_{31}(t)s_{23}(t)s_{42}(t) + s_{21}(t)s_{42}(t)$. In other words, the total influence that node $j$ has on node $i$ around a certain point $\mathbf{x}$ on the state space defined in Eq. (1) is defined recursively as

$$
g_{ij}(t) \triangleq \frac{d x_i(t)}{d x_j(\tau)} = \frac{d \Phi_i(t, \mathbf{x}(\tau))}{d x_j(\tau)}
$$

$$
= \frac{\partial \Phi_i(t, \mathbf{x}(\tau))}{\partial x_j(\tau)} + \sum_{k \neq j} \frac{\partial \Phi_i(t, \mathbf{x}(\tau))}{\partial x_k(\tau)} \frac{d x_k(t)}{d x_j(\tau)}
$$

$$
=s_{i j}(t)+\sum_{k>j} s_{i k}(t) g_{k j}(t)
$$

which is similar to the expression noted in in Barzel and Barabási ${ }^{27}$. Conventionally, under stationarity assumptions, $g_{i j}(t)$ can be approximated using similarity measures, such as correlation and mutual information ${ }^{8}$ estimated from raw samples of time series. The direct and total influence matrices are related at every time $t$ by the following equation:

$$
S(t) B(t)-C(t)=0
$$

where $B(t)$ and $C(t)$ are functions (defined depending on the context) of $S(t)$ and $G(t)$, respectively. Pertinently, when the underlying dynamical system is linear and time-invariant, $S(t)$ and $G(t)$ do not depend on time. Eq. (7) generalizes previous network deconvolution formulations as follows: for Feizi et al. ${ }^{38}, B(t)=(I+G), C(t)=G$, for Barzel and Barabási ${ }^{27} B(t)=G, C(t)=G-I+D(S G)$, and for Sontag et al. ${ }^{33}, B(t)=R(t), C(t)=\Gamma(t)$, where $R_{i j}(t)=\partial x_{i}(t, \boldsymbol{p}) / \partial p_{j} ; \Gamma_{i j}(t)=\partial R_{i j}(t) / \partial t$. For simplicity of expressions, we use henceforth $S, B$ and $C$ instead of $S(t), B(t)$ and $C(t)$ in this subsection. The "true" network structure $S^{0}$ can be estimated by solving the following $\ell_{1}$-min formulation:

$$
S^{*}=\arg \min _{S}\|S\|_{1} \text { s.t. }\|S B-C\|_{F} \leq \mathcal{E}
$$

where $\|S\|_{F}=\sum_{i, j}\left|s_{i j}\right|$, and $\mathcal{E}$ is the allowable perturbation that captures the effects of noise in the measured data. We note that in the absence of noise, this formulation is equivalent to ND and MRA. In the following sections we present two alternative $\ell_{1}$-min formulations for direct influence inference. The first formulation presented in Eqs $(9,10)$ addresses the estimation of $s_{i j}$ for real world scenarios when the total influence $g_{i j}$ is directly measurable (e.g., based on the strengths of co-excitations), and the second formulation Eqs $(21,22)$ addresses the inference of the network structure (i.e., determine all node pairs where $s_{i j}(t)=0 \forall t$ ) under one of the most generic scenarios of using multiple ensembles of time series realizations of the state variables, collected under noisy and transient conditions with different parameter settings. It may be noted that inferring the network structure under such generic conditions has not been investigated to date.

Network inference when total influence matrix is available. For the case where the measurements of total influence matrix $G$ are provided ${ }^{38}$, the relaxed $\ell_{1}$-min formulation can be written as

$$
\min \|S\|_{1} \text { s.t. }\|S(G+I)-G\|_{F} \leq \mathcal{E}
$$

or in vector form as

$$
\min _{s_{i}}\left\|\boldsymbol{s}_{i}\right\|_{1} \text { s.t. }\left\|(G+I)^{T} \boldsymbol{s}_{i}-\boldsymbol{g}_{i}\right\|_{2} \leq \varepsilon_{i}, \quad \forall i
$$

where $\boldsymbol{g}_{i}$ is the $i^{\text {th }}$ column of $G$. In order to solve for an accurate estimate of $S^{0}$ from Eqs (9) or (10) using standard solvers ${ }^{38,39}$, estimation of $\mathcal{E}$ and $\varepsilon_{i}$ are crucial. Specifically, when noisy measurements of the total influence matrix differ from the "true" total influence as $G=G^{0}+\Delta G$, the estimated direct influence matrix differs from the true direct influence matrix as $S=S^{0}+\Delta S$, and

$$
\begin{gathered}
\left(S^{0}+\Delta S\right)(G+I)=G \\
\Rightarrow S^{0}(G+I)-G=-\Delta S G-\Delta S
\end{gathered}
$$

The quantity $\|\Delta S G+\Delta S\|_{F}$ is called total perturbation. In vector form, $\left(\left\|\Delta G \boldsymbol{s}_{i}^{0}\right\|_{2}+\left\|\boldsymbol{g}_{i}-\boldsymbol{g}_{i}^{0}\right\|_{1}\right)$ can represent the total perturbation for computing row $i$ of $S^{0}$. The bounds on $\mathcal{E}$ and $\varepsilon_{i}$ are as follows (See Theorem 1 in Supplementary Information):

$$
\begin{gathered}
\mathcal{E} \approx \mathcal{E}^{(1)}=\left(1+\|G\|_{F}\right) \gamma \\
\mathcal{E} \leq \mathcal{E}^{(2)}=\left.(1+\|G\|_{F}) \frac{\|\Delta G\|_{F}}{\left(1-\|G\|_{F}-\|\Delta G\|_{F}\right)\left(1-\|G\|_{F}\right)}\right. \\
\varepsilon_{i} \leq 2\left(\left\|\boldsymbol{g}_{i}-\boldsymbol{g}_{i}^{0}\right\|_{2}^{2}+\|\Delta G\|_{F} \frac{1}{\sqrt{1-\delta_{K}}}\left(\left\|\boldsymbol{g}_{i}\right\|_{2}+\left\|\boldsymbol{g}_{i}-\boldsymbol{g}_{i}^{0}\right\|_{2}\right)^{2}\right)
\end{gathered}
$$

where $\gamma$ is the largest eigenvalue of $\Delta G, \delta_{K}$ is the restricted isometry constant ${ }^{40}$ and $\|\cdot\|_{F}$ is the Frobenius norm of a matrix. By employing these bounds, we can set the values of $\mathcal{E}$ and $\varepsilon_{i}$ for effective network inference. As subsequent numerical investigations indicate, the performance of the method does not degrade significantly due to the presence of noise, and this is the major advantage of the present approach. It may be noted that our method is

designed to provide the sparsest network structure that replicates the measured total influence $G$ within a bound (specified in terms of the allowable total perturbation). This is very important because only a small set of noisy observations are available, for most real world applications. For example, in the case of genetic regulatory networks, only a subset of dynamic regimes (i.e. marked by the active degrees of freedom) of the underlying process are captured. Therefore, identification of true network structure would never be guaranteed by any approach, and among the network structures that can replicate the observed total influence within a specified bound, the sparsest network would be of the most interest. Although sparser than the network derived by ND, $\ell_{1}$-min derived structure might be adequate to uncover the total dynamic couplings of the process captured in the observed data.

In real world scenarios, $\Delta G$ is not always known. Overestimation of $\Delta G$ can lead to network structures that are sparser than the original. However, we show that the effects of under-estimation of noise can be alleviated to a great extent. When noise level is unknown but multiple realizations of the noisy measurements of $G$ are available, it is possible to further reduce the inference error by combining the estimates with different realizations of $G$ as $\hat{S}^{(N)}=\frac{1}{N} \sum_{r=1}^{N} \hat{S}^{(r)}$ (See the Proposition 1 in Supplementary Information), where $\hat{S}^{(r)}$ s are direct influence matrices computed from $\hat{G}^{(r)}$ and $\hat{G}^{(1)}, \ldots, \hat{G}^{(N)}$ are $N$ different measurements or estimates of the total influence matrix $G^{0}$. This result assumes that $\operatorname{Var}\left(\hat{S}^{(r)}\right)$ is bounded. However, it may be noted that even if $\operatorname{Var}\left(\hat{S}^{(r)}\right)$ is arbitrarily large we find that $\hat{S}^{(N)}$ is at least as good as $\hat{S}^{(r)}$. This averaging procedure allows us to improve the network inference accuracy when multiple measurements of the total influence matrix are available. For example, when the network structure does not change significantly as the system approaches a steady state, the total influence matrices can be measured multiple times, each corresponds to one time window.

Network inference when the time series under transient conditions are available (total influence matrix not given). In practice, $g_{i j}$ are often estimated using convenient similarity measures such as correlation or mutual information between the time series $x_{i}(t)$ and $x_{j}(t)$ of the nodes $i$ and $j$ as stated in the foregoing section. These estimations have a very low accuracy due to nonstationaries (transient), low sampling rates and sample size limitation; and can not capture the total influence in the system. Also, in most real world applications, only finite samples of time series $\boldsymbol{x}(t)$ are available, and the present NDs can not be employed in these scenarios. To overcome these drawbacks, we have adapted an approach to estimate the direct influence based on multiple time series ensembles obtained by perturbing parameters of the dynamical system Eq. (1) ${ }^{33}$. We first modify the perturbation procedure proposed by Sontag et al. ${ }^{33}$ to make it more robust to numerical error then further improve the accuracy of network inference by introducing a sparse regression formulation and the averaging scheme.

A robust perturbation procedure. According to Sontag et al. ${ }^{33}, s_{i j}(t)=\left[\frac{\partial f_{j}(\boldsymbol{x}, \boldsymbol{p})}{\partial x_{i}}\right]_{i, j=1 \ldots n}$ can be derived from the following equation:

$$
\Gamma(t)=S(t) R(t)
$$

where

$$
R_{i j}(t)=\frac{\partial x_{i}}{\partial p_{j}} \approx \frac{x_{i}\left(t, p_{j}+\Delta p_{j}\right)-x_{i}\left(t, p_{j}\right)}{\Delta p_{j}}, \Gamma_{i j}(t)=\frac{\partial \dot{x}_{i}}{\partial p_{j}} \approx \frac{R_{i j}(t+\Delta t)-R_{i j}(t)}{\Delta t}
$$

and

$$
i=1 . . n, p_{k} \in P_{i}=\left\{p_{k} \in \boldsymbol{p}: \partial f_{j} / \partial p_{k}(\boldsymbol{x}, \boldsymbol{p})=0\right\}
$$

Note that $\Gamma$ plays the role of the total influence matrix $G$ in the previous section. To compute the row $i$ of the matrix $S$, the parameters $p_{j}$ to be perturbed are chosen such that $p_{j} \in P_{i}{ }^{33}$. As a consequence, changes in $p_{j}$ indirectly affect $x_{i}$, and $\frac{d x_{i}}{d p_{j}}$ are much smaller than $\frac{d x_{k}}{d p_{j}}$, for $k \neq i$. As a result, the $i^{\text {th }}$ column $\left(\frac{d x_{i}}{d p_{j}}\right) \quad$ in the matrix $\left(\frac{d x_{k}}{d p_{j}}\right) \quad$ is much smaller ( 2 orders of magnitude smaller as in the Table 1 for the network studied in case study 1) compared to other columns when $p_{j} \in P_{i}$. A numerical issue this poses can be understood based on the following linear system of equations

$$
A \boldsymbol{u}=\boldsymbol{b}
$$

Here, the sensitivity of solution $\boldsymbol{u}$ to the change in $A$ can be quantified as follows ${ }^{41}$

$$
\frac{\partial u_{i}}{\partial a_{j k}}=-c_{i j} \sum_{l} c_{k l} b_{l}
$$

where $C=A^{-1}$. Whenever $A$ contains a $j$ column such that $\left\|a_{j}\right\| \ll\left\|a_{k}\right\|, \forall k \neq j, C$ contains a row $i$ such that $\left\|c_{r}\right\| \gg\left\|c_{r}\right\|, \forall r \neq i$. As a consequence, $\frac{\partial u_{i}}{\partial a_{j k}}$ becomes several magnitudes larger than other rows. Therefore, the perturbation procedure proposed by Sontag et al. ${ }^{33}$ is very unrobust to noise or numerical error in $x_{i} \mathrm{~s}$.


Table 1. The matrix $R$ for computing the first row of $S$ is estimated using Sontag et al. ${ }^{33}$ 's perturbation procedure. The first row/column of $R$ is two orders of magnitude smaller than others, which presents major numerical issues for inferring structures of large networks.

The following modification to the perturbation procedure addresses the aforementioned issue. Consider the case when $\bar{x}_{i}$ depends linearly on $x_{i}$ as in the following system ${ }^{42}$ :

$$
\bar{x}_{i}=p_{i} x_{i}+\sum_{j=1, j \neq i}^{n} s_{i j}^{0} \frac{x_{j}}{1+x_{j}}
$$

This system describes popular biochemical reactions when the activity of a chemical species is inhibited by its own concentration ${ }^{43,44}$. To compute the $i^{\text {th }}$ row of the Jacobian, the parameters $p_{i}$ is also perturbed. Note that

$$
\frac{\partial \bar{x}_{i}}{\partial p_{i}}=x_{i}+p_{i} \frac{\partial x_{i}}{\partial p_{i}}+\sum_{j=1, j \neq i}^{n} \frac{\partial f_{i}(\boldsymbol{x}, \boldsymbol{p})}{\partial x_{j}} \frac{\partial x_{j}}{\partial p_{i}}
$$

or

$$
\frac{\partial \bar{x}_{i}}{\partial p_{i}}-x_{i}=\sum_{j=1, j \neq i}^{n} \frac{\partial x_{j}}{\partial p_{j}} \frac{\partial f_{i}\left(\boldsymbol{x}, \boldsymbol{p}_{i}\right)}{\partial x_{j}}, \frac{\partial f_{i}\left(\boldsymbol{x}, \boldsymbol{p}_{i}\right)}{\partial x_{i}}=p_{i}
$$

The remaining parameters are perturbed as in Eqs $(17,18)$. Therefore, to compute $\frac{\partial f_{i}\left(\boldsymbol{x}, \boldsymbol{p}_{i}\right)}{\partial x_{k}}$, we can solve the system of equations (16) with

$$
P_{i i}(t)=\frac{\partial \bar{x}_{i}}{\partial p_{i}}-x_{i}, R_{i i}(t)=\frac{\partial x_{i}}{\partial p_{i}}
$$

and other $P_{i j} \mathrm{~s}, R_{i j} \mathrm{~s}$ are defined as in $(17,18)$.
A robust network identification approach. In addition to the perturbation procedure proposed in Eqs (17-19), we present a method to solve Eq. (16) that is more robust to the presence of noise. In the present context, the $\ell_{1}$-min formulation of Eq. (16) takes the following form:

$$
\min \|S\|_{1} \text { s.t }\|\Gamma-S R\|_{F} \leq \mathcal{E}
$$

or

$$
\min \left\|\boldsymbol{s}_{i}\right\|_{1} \text { s.t }\left\|\Gamma_{i k}(t)-\sum_{l=1}^{n} R_{i k}(t) s_{i l}(t)\right\| \leq \varepsilon_{i}, \forall i, \forall k: p_{k} \in P_{i}
$$

As noted in the foregoing section, estimation of $\mathcal{E}$ and $\varepsilon_{i}$ based on the noise levels when measuring $\boldsymbol{x}(t)$ is essential to ensure that the solution to Eq. (21) serves as a viable estimator of the "true" direct influence $S^{0}$. The following bounds and approximation allow the specification of $\mathcal{E}$ and $\varepsilon_{i}$ (Theorems 4 and 5 in Supplementary Information)

$$
\begin{gathered}
\mathcal{E} \leq\left(\|\Gamma\|_{F}+\|\Delta \Gamma\|_{F}\right) \frac{\left\|R^{-1} \Delta R\right\|_{F}}{1-\left\|R^{-1} \Delta R\right\|_{F}}+\|\Delta \Gamma\|_{F} \\
\varepsilon_{i} \leq \frac{\left\|R^{-1} \Delta R\right\|_{F}}{1-\left\|R^{-1} \Delta R\right\|_{F}}\left\|\left[(\Gamma-\Delta \Gamma)^{2}\right]_{i}\right\|+\left\|\left(\Delta \Gamma^{2}\right)_{i}\right\| \\
\varepsilon_{i} \approx\left\|R^{-1} \Delta R\right\|\left\|\left[(\Gamma-\Delta \Gamma)^{2}\right]_{i}\right\|+\left\|\left(\Delta \Gamma^{2}\right)_{i}\right\|
\end{gathered}
$$

where


Table 2. Comparison of bounds on total perturbation obtained using Eqs (13) and (14) suggests that Eq. (13) provides a good approximation and Eq. (14) serves as an upper bound of $\mathcal{E}^{(0)}$,

$$
\begin{aligned}
& (\Delta R)_{\hat{\alpha}}(t)=\left\langle e_{\hat{\alpha}}^{(1)}(t)-e_{\hat{\alpha}}^{(2)}(t)\right\rangle / \Delta p_{k} \\
& (\Delta \Gamma)_{\hat{\alpha}}(t)=\frac{\left[\left(e_{\hat{\alpha}}^{(1)}(t+\Delta t)-e_{\hat{\alpha}}^{(2)}(t+\Delta t)\right)-\left(e_{\hat{\alpha}}^{(1)}(t)-e_{\hat{\alpha}}^{(2)}(t)\right)\right]}{\Delta t \Delta p_{k}}
\end{aligned}
$$

and $e_{\hat{\alpha}}^{(1)}(t), e_{\hat{\alpha}}^{(2)}(t)$ are the errors incurred when measuring $x_{i}^{0}\left(t, p_{k}\right), x_{i}^{0}\left(t, p_{k}+\Delta p_{k}\right)$, respectively. As stated in the foregoing, noise level is not known a priori in most real world systems. In this situation, the network structure is deduced based on the entries in the estimated $S^{0}(t)$ that are equal to zero for all $t$ and can be estimated by the entries in as $\hat{S}^{(N)}=\frac{1}{\sigma} \sum_{i=1}^{N} \hat{S}\left(t_{i}\right)$ that converge to zero, where $\hat{S}\left(t_{i}\right)$ is the direct influence matrix computed from $\hat{\Gamma}\left(t_{i}\right)$, and $\hat{\Gamma}\left(t_{i}\right),(r=1 . . N)$ are measurements or approximations of the total influence matrix $\Gamma^{0}(t)$ at time $t_{i}$ (see Proposition 2 in Supplementary Information). This averaging procedure allows us to improve the accuracy to predict the pair of nodes that are not connected when the measurement noise level is not available. As a result, our method ensures low false positive rates on the "arcs". As noted in the context of Proposition 1, network inference with $\hat{S}^{(N)}$ tends to be at least as good as with $\hat{S}\left(t_{r}\right)$ even when $\operatorname{Var}\left(\hat{S}\left(t_{r}\right)\right)$ is arbitrarily large.

# Results 

We have considered two case studies to validate the theoretical results and evaluate the performance of the $\ell_{1}$-min approach. The first case study contains two simulation scenarios. The first scenario simulates a scale-free network whose structure resembles that of the genetic regulation process of E. Coli species ${ }^{45}$. Here, the challenge is to estimate the true network structure, i.e., the direct influence matrix $S^{0}$ from a noisy total influence matrix $G$. This scenario is optimal for assessing the closeness of the bounds stated in Eqs $(14,15)$ relative to the true bounds on the constraints $\mathcal{E}^{(0)}=\left\|(G+I)^{T} S^{0}-G\right\|_{F}$, and comparing the performance of the $\ell_{1}$-min formulation relative to the recent ND methods in terms of inference error and sparsity. The next scenario simulates a system of Hill-type differential equations modeling a gene interaction network. Here, the challenge is to estimate the true network structure from noisy and transient time series data. The second case study is an application of our method to infer genetic regulatory networks (GRNs) from empirical data in the context of DREAM5 challenge ${ }^{46}$. This challenge is a standard framework for evaluating GRN inference methods.

Case I: simulation studies. Inferring direct influence networks from total influence network. First, we adapted the procedure specified by Muchnik ${ }^{47}$ to generate 500 random realizations of scale-free networks consisting of $n=100$ nodes, with a degree exponent of 2.2 . In each realization, the weights of the true direct influence network, $s_{i}^{0}$ follow the distribution $\mathcal{N}\left(\mu_{S^{0}}, \sigma_{S^{0}}\right)$ with $\mu_{S^{0}} \sim \mathcal{N}(0,0.04)$, and $\sigma_{S^{0}} \sim \mathcal{N}(0,0.04)$. The true total influence matrix $G^{0}$ was obtained as $G^{0}=S^{0}\left(I-S^{0}\right)^{-1}$. The noisy total influence matrix was generated as $G=G^{0}+\Delta G$, where the contaminated noise $\Delta G$ was considered in two cases: (1) proportional, i.e., $(\Delta G)_{i j}=\alpha \mathcal{N}\left(\mu_{S^{0}}, \sigma_{S^{0}}\right)$ and (2) independent, i.e., $(\Delta G)_{i j}=\mathcal{N}\left(0, \sigma_{S^{0}}\right)$. We considered cases where the measurement noise level $\|\Delta G\|_{F}$ is known as well as those where there is uncertainty in estimating the measurement noise level.

We first compare the "true" bound $\mathcal{E}^{(0)}$ (computed using $S^{0}$ ) and the bounds for $\mathcal{E}$ estimated based on Eqs $(13,14)$. In the presence of noise, the bounds appear to be in the same order of magnitude for all simulated networks (Table 2). The results also suggest that the bound specified in Eq. (13) closely matches the "true" bound and can be used to approximate the feasible region when $\mathcal{E}^{(0)}$ is unknown with high accuracy. Although the bound in Eq. (14) tends to be loose, it can be used as an upper bound for $\mathcal{E}^{(0)}$.

We next compared the performance of ND and $\ell_{1}$-min approaches (using our bounds Eqs (13) and (14)) in terms of inference error defined as $\rho=\frac{\left\|\hat{S}-S^{0}\right\|_{F}}{\left\|S^{0}\right\|_{F}}$, where $\hat{S}$ is computed using the different methods being compared. The $\ell_{1}$-min approach with "true" constraint bound $\varepsilon_{i}=\varepsilon_{i}^{(0)}$ significantly improves the ND (the mean and the variance of the estimated $\rho$ were reduced by $45 \%$ and $99 \%$, respectively) (Fig. 2). Employing $\varepsilon_{i}=\varepsilon_{i}^{(1)}=\mathcal{E}^{(1)} / \sqrt{n}$ (based on Eq. (13)), the $\ell_{1}$-min approach performs much better than ND (the mean and variance of $\rho$ are reduced by $33.5 \%$ and $87.5 \%$, respectively). More importantly, the inference error of $\ell_{1}$-min approaches were concentrated around of 0.15 within $\pm 0.05$, while those of ND were spread over a larger range, from 0.3 to 0.6 . This suggests that $\ell_{1}$-min approach using our bound in Eq. (13) is more robust than ND to noise and approximation error incurred when measuring the total influence matrix.

We also compared the sparsity of the recovered networks measured in terms of Hoyer sparsity measure ${ }^{48}$ defined as follows

![img-1.jpeg](img-1.jpeg)

Figure 2. Histograms summarizing the relative performance of ND and ℓ₁-min approaches for the benchmark numerical case in terms of (a) inference error that quantifies the accuracy and (b) Hoyer measure that quantifies the sparsity of the solution. The solution from the ℓ₁-min approach is more precise and sparser than ND: compared to NDs, the mean and the variance of the inference error are reduced by 45% and 99%, respectively, when using ℓ₁-min with εᵢ = εᵢ^{(0)}; 33.5% and 87.5%, respectively when using ℓ₁-min with εᵢ = εᵢ^{(1)}; the mean of Hoyer measure is increased by 16.38% and variance reduced by 69% when using the ℓ₁-min with εᵢ = εᵢ^{(0)}, and is increased by 15.90% in mean, reduced by 75.69% in variance when using εᵢ = εᵢ^{(1)}.

![img-2.jpeg](img-2.jpeg)

Figure 3. Variation of inference error with total perturbation bound εᵢ. The inference error attains a minimum near the true bound εᵢ^{(0)}, and it trends almost linearly with εᵢ as it is increased beyond εᵢ^{(0)}. As εᵢ → 0, the inference error increases exponentially, which is an evidence of over fitting.

$$
\text{Hoyer}(S) = \frac{n - \left(\sum_{i,j=1}^{n} |x_{ij}|\right) / \sqrt{\sum_{i,j=1}^{n} x_{ij}^2}}{n - 1}.
$$

Note that $\text{Hoyer}(S) \in [0, 1]$. The closer it is to 1, the sparser $S$ is. In terms of this measure, the solution of the ℓ₁ -min approach is much sparser (mean is 16.38% larger, variance is 69% smaller when using the true bound εᵢ = εᵢ^{(0)}, and mean is 15.90% larger, variance is 75.69% smaller when using the approximated bound εᵢ = εᵢ^{(1)}) than solution of ND (Fig. 2b). Also, the Hoyer measure of the ℓ₁-min approach is concentrated more around a much higher value (sparse matrices) than that of ND indicating that the ℓ₁-min approach using our bound gives a significantly sparser solution than ND. As a result, this gives a more interpretable connection structure without the loss of performance.

We also studied the effects of the bounds of ℓ₁-min formulation on inference error to verify Eq. (40) numerically. When εᵢ/εᵢ^{(0)} > 1, the inference error trends almost linearly with εᵢ (see Fig. 3). This confirms the conclusion of Theorem 3. Also, when εᵢ/εᵢ^{(0)} < 1 and tends toward 0, the inference error increases. This shows an evidence of over-fitting.

Subsequently, we studied the effect of averaging (Proposition 1) in the context of the ℓ₁-min and ND methods. We conducted N = 40 simulations, in each of which, Sᵢ, Gᵢ and ∆G were generated as stated in the foregoing. We used the inference error without ρ^{(N)} and with averaging $\overline{\rho}$ as measures for comparison from each simulation defined as follows:

$$
\rho^{(N)} = \frac{1}{N} \sum_{k=1}^{N} \left\| \left| \tilde{S}^{(k)} - S^k \right| \right\|_{\mathcal{F}} / \| S^k\|_{\mathcal{F}}, \tag{26}
$$

$$
\overline{\rho} = \| S^{(N)} - S^k \|_{\mathcal{F}} / \| S^k \|_{\mathcal{F}}, \tag{27}
$$

![img-3.jpeg](img-3.jpeg)

Figure 4. Box plots summarizing the effects of averaging on (a) ND and (b) $\ell_{1}$-min with $\varepsilon_{i}=\varepsilon^{(1)}$. The inference errors were almost unchanged with $\ell_{1}$-min compared to ND. Averaging (light/red) reduced inference error further by about 8 times compared to without averaging (dark/blue). The $\bar{\rho}$ values were 0.1196 with ND and 0.0259 with $\ell_{1}$-min ( p -values of the paired t -tests between the inference error without and with averaging were $\leq 10^{-5}$ in all cases).
where $\bar{S}^{(k)}(k=1, \ldots, N)$ is the $k^{\text {th }}$ realization of $S^{(k)}$ and $\bar{S}^{(N)}$ is estimated as stated in Proposition 1. The results suggest that averaging reduces the inference error of both methods by about 8 times in all cases, thus supporting the validity of Proposition 1 (Fig. 4). The inference errors were almost the same between ND and $\ell_{1}$-min with $\varepsilon_{i}=\varepsilon^{(1)}$.

Inferring direct influence network structure from multiple time series under transient conditions. In this section we represent the performance of $\ell_{1}$-min approach in inferring network structure from transient time series with an unknown noise level. In this study we used Michaelis-Menten dynamic system given by ${ }^{27}$ :

$$
\dot{x}_{i}=p_{i} x_{i}+\sum_{j=1, j \neq i}^{N} x_{0}^{0} \frac{x_{j}}{1+x_{j}}
$$

where the "true" network defined by $\left(x_{0}^{0}\right)$ is a scale-free network ${ }^{45}$ generated randomly with degree exponent $\gamma=2.2$ consisting of $n=40$ nodes with about 70 edges, whose weights $\varepsilon_{0}^{0}$ follow the distribution $\mathcal{N}(5,0.25)$.

We obtained 30 different variants of this network. For each of these invariants (trials), a perturbed network was obtained by changing (perturbing) the parameters according to Eqs (18-20). Every solution $\boldsymbol{x}(t), t \in[0,1]$, obtained from an initial condition $\boldsymbol{x}(0)$ was contaminated with noise of the form $\mathcal{N}\left(0, \sigma^{2}\right)$ to simulate a noisy measurement $\hat{\boldsymbol{x}}(t)$. Here $\sigma^{2}$ was chosen to be $10^{-4}$. The direct influence matrix $\hat{S}\left(t_{k}\right)$ were estimated using Sontag et al.'s ${ }^{33}$ method, as well as $\ell_{1}$-min formulations, with different values of bounds. Next, $\bar{S}^{(N)}$ was estimated as in Proposition 2 by averaging over 30 time samples $t_{k} \in[0,1], k=1 . .30$ chosen randomly. For performance evaluation, we used the inference error without $\rho^{(N)}$ and with averaging $\bar{\rho}$, given by

$$
\rho^{(N)}=\sqrt{\frac{1}{N} \sum_{k=1}^{N} \sum_{i, j}\left(1-\mathcal{H}\left(\left|s_{0}^{0}\right|\right)\right)\left(\hat{s}_{0}\left(t_{k}\right)\right)^{2}}
$$

![img-4.jpeg](img-4.jpeg)

Figure 5. Box plots summarizing the inference errors without and with averaging for. (a) Sontag et al.'s ${ }^{33}$ method $\left(\rho=7.58 \times 10^{4}, \bar{\rho}=5.87 \times 10^{4}\right) ;(\mathbf{b}) \ell_{1}$-min with noise magnitude given $(\rho=7.11, \bar{\rho}=5.32)$, (c) $\ell_{1}$ -min with noise magnitude underestimated as $10 \%$ the actual $(\rho=52.50, \bar{\rho}=13.40)$, and (d) $\ell_{1}$-min with noise magnitude overestimated as 10 times the actual $(\rho=0.80, \bar{\rho}=0.60)$. The inference error was reduced by $10^{5}$ times when using the $\ell_{1}$-min approach $(21,22)$, compared to Sontag et al.'s ${ }^{33}$ method. Averaging further reduced inference error by at least $30 \%$ in all cases ( p -values of the paired t -tests consistently were below 0.0282 ).

$$
\bar{\rho}=\sqrt{\sum_{i, j}\left(1-\mathcal{H}\left(\left|s_{i j}^{0}\right|\right)\right)\left(\bar{s}_{i j}^{(N)}\right)^{2}}
$$

where $\mathcal{H}($.$) is Heaviside function. These error measures quantify the number of absent links\left(s_{i j}^{0}=0\right)$ that are correctly identified.

As summarized in Fig. 5, the $\ell_{1}$-min approach performs better than Sontag et al.'s ${ }^{33}$ method in all cases tested. In fact, $\rho, \bar{\rho}$ were reduced by $10^{3}$ times. The poor performance of Sontag et al.'s ${ }^{33}$ method is attributed to the numerical issues noted in the earlier section. A further $30 \%$ reduction in inference error resulted from averaging for both cases. Next, the cases (c) and (d) were designed to simulate the real situations where the noise magnitude is unknown. We considered cases where the noise levels are under or overestimated by 1 order of magnitude. While Sontag et al.'s ${ }^{33}$ method would not be applicable in such cases, $\ell_{1}$-min without averaging was found to lead to suboptimal inference. Under underestimation $\varepsilon_{i}<\varepsilon_{i}^{(0)} / 10$, averaging was found to further reduce the inference error by about $70 \%$, and the inference error $\bar{\rho}$ s were of the same level as one would obtain when the noise level is known. This result is consistent with and is a clear verification of Proposition 2. When the noise level is overestimated, the resulting network tends to be highly sparse, offering excellent specificity in identifying the absence of direct coupling. The inference errors are therefore low even without averaging by default. In this case averaging reduces the inference errors by $5 \%$. The p -values of the paired t -tests between the inference error with and without averaging were below 0.0282 in all cases suggesting that averaging helps improve network inference.

Case II: Application to empirical genetic regulatory network inference. Next, we applied our method to infer real world GRNs and compare its performance with other methods including ND ${ }^{26}$, Bayesian network inference, Pearson and Spearman correlation networks ${ }^{8}$ using the framework presented in DREAM5 challenge. Here, the Pearson and Spearman correlations were considered as they are the most widely used methods for network inference and can provide a reasonable estimation of the total influence matrix ${ }^{26,27}$. In addition, ND has been most effective in inferring network topology when the total influence matrix G is estimated using Person and Spearman correlations. Therefore, these serve as the challenging test cases to evaluate the performance of $\ell_{1}$-min where ND is already effective. The DREAM5 challenge contains gene-expression microarray data of three species including an in silico benchmark, a prokaryotic model organism (E. coli) and a eukaryotic model organism (S. cerevisiae). Beside $\rho$ and Hoyer metrics, we employed the following score, which was used in earlier works ${ }^{8}$ to assess the performance of a network inference method for recovering the structure underlying these data sets:

$$
\xi=-\frac{\log \left(p_{B O C}\right)+\log \left(p_{P R}\right)}{2}
$$

where $p_{B O C}$ and $p_{P R}$ are p -values computed from AUROC (area under receiver operating characteristic curve) and AUPR (area under precision-recall curve).

The results of the performance evaluation are summarized in Fig. 6. We note that for computing the performance metrics we first generated 30 different $G$ matrices with Pearson correlation, 30 others with Spearman correlation and another 30 with Mutual Information for each data set. The $G$ matrix in each case was estimated using samples of size $75 \%$ of the data set. The averaging procedure considers the $S$ matrices estimated from these $G$ matrices using different methods. In terms of $\xi$-score (Eq. (31)), which quantifies how well-in terms of having low false negative rates (FNR, related to sensitivity), and low false positive rates (FRN, related to specificity), the true positive rate (TPR) and true negative rate (TNR)-the estimated $\bar{S}$ captures $S^{8}, \ell_{1}$-min approach yields $\bar{S}$ with at least $18.53 \%$ higher than with ND in all cases tested except the in silico case (see Fig. 6). Both ND and $\ell_{1}$-min performed better than Bayesian network approach whose $\xi$-scores were $14.891,0.029,0.0001$, respectively, for the three data sets ${ }^{8}$. In terms of $\rho$-score (Eq. (29)), which quantifies the false positive rates (i. e., the specificity), $\ell_{1}$-min approach reduces $\rho$ by 2-3 orders compared to ND in all cases. These results provide a strong evidence for the relevance of the $\ell_{1}$-min approach for network structure inference. In terms of sparsity, $\ell_{1}$-min approach increased the Hoyer measure by about $20 \%$ in most cases, and were much closer to the Hoyer measures of the gold-standard network, compared to ND.

As noted earlier for in silico data, although the $\rho$-score with $\ell_{1}$-min was at least $1160 \%$ lower (i.e., higher specificity) and Hoyer was $33 \%$ higher (i.e., higher sparsity), the $\xi$-score was slightly ( $10 \%$ ) lower than with ND. The lower $\xi$ - score for $\ell_{1}$-min is perhaps a consequence of the method being susceptible to over-specification of the noise level. In this context, it must be noted that the solutions from both ND and $\ell_{1}$-min can replicate the observed total influence $G$ within a specified bound (as total perturbation). However, the solutions from $\ell_{1}$-min tend to be much sparser and have lower false positive rate. Given that there were only 805 sample measurements to reconstruct $G$ matrices for 1643 nodes in the in silico network, it is highly likely that several dynamic modes (degree of freedom) are not observable from the data. Therefore, $\ell_{1}$-min generated a much sparser network which, by formulation, is guaranteed to be adequate to capture the observed modes of the dynamics within the specified total perturbation limits. The ND derived networks for in silico and other cases that have higher $\xi$-score, intriguingly, were consistently found to have much lower Hoyer score (hence sparsity) even compared to the specified total influence matrix. Thus, $\ell_{1}$-min-generated solutions provide significant improvement in specificity, although the sensitivity at times were found to be slightly lower than with ND.

Averaging improves the $\xi$-scores (Eq. (31)) with all methods by at most $10 \%$. This is perhaps due to the near-stationarity of the total influence matrix $G$, when computed using data over long time windows that smooths out various higher order transient effects. Also, one may note that the averaging makes the network inferred from ND less sparse than without averaging. This is because under noise, transients and data sparsity, ND yields vastly different network topologies depending on the samples employed. Averaging over these vastly different networks causes a reduction in sparsity. These results, taken together suggest that the $\ell_{1}$-min approach is perhaps the best known means to provide specificity for network inference from transient and noisy data. The utility of the approach would be to provide a minimal set of arcs (dynamic couplings or direct influences) to be considered for further network dynamics reconstruction applications.

Discussion and Concluding remarks. In this paper, we have investigated a method to robustly infer the structure of a network representing a sparse dynamical system from noisy, transient time series data. When the noise level is known, the $\ell_{1}$-min formulation employing our theoretical formula for the bound on total perturbation improves the recently reported NDs in terms of both accuracy and sparsity. When the noise level is unknown, we have shown that by averaging the networks inferred from different time points or conditions, the inference of network structure of real world processes becomes highly plausible.

Pertinently, for most real world processes, the total influence is not known a priori; only the time series ensembles gathered under transient conditions are available (e.g., gene expression microarray data ${ }^{8,49}$, protein-protein interaction data ${ }^{50}$ as in the case of Michaelis-Menten dynamics). It has been noted that most of the earlier approaches present severe accuracy, noise sensitivity and/or numerically stability issues for such realistic scenarios. To overcome these limitations, we have investigated the $\ell_{1}$-min approach with a novel perturbation procedure for time series based network inference. Averaging over the solutions estimated at different time windows has

![img-5.jpeg](img-5.jpeg)

Figure 6. Performance comparison of (1) original $G$ matrix, (2) ND, (3) ND with averaging, (4) $\boldsymbol{\ell}_{1}$-min and (5) $\boldsymbol{\ell}_{1}$-min with averaging for the DREAM5 challenge datasets. The total influence $G$ matrix is estimated by Pearson correlation (blue/dark), Spearman correlation (red/light) and Mutual Information (green/light). Compared to ND, the prediction scores with $\ell_{1}$-min are increased by $23.94 \%$ (for $G$ from Pearson correlation), $53.03 \%$ (for $G$ from Spearman correlation) \& $18.53 \%$ (for $G$ from Mutual Information) for E. Coli, $89.09 \%$, $249.7 \%$ \& $116.74 \%$ for $S$. cerevisiae, respectively; the inference errors $\rho(29)$ are reduced by 2 to 3 orders of magnitude in all cases; Hoyer measures are increased by $34 \%, 36.41 \%$ \& $322.91 \%$ for E. Coli, $18.85 \%, 19.59 \%$ \& $96.65 \%$ for $S$. cerevisiae, respectively. For in silico data, ND gives a solution with $11 \%$ higher prediction score but $33 \%$ less sparse than $\ell_{1}$-min approach. Averaging slightly improves the performance of all methods $(<10 \%)$.
been shown to allow inference of the structure for complex real world networks, especially when the noise levels are unknown or cannot be accurately estimated.

Next, we have applied our method to three benchmark systems: a sparse scale-free network ${ }^{51}$ with a specified noise level and the total influence between any two nodes given, a genetic regulatory network model formulated in terms of a system of Hill-type differential equations ${ }^{27}$, and GRNs of DREAM5 challenge ${ }^{46}$. These analyses suggest that our proposed bounds on the constraints for the $\ell_{1}$-min formulation, extracted from a few time series samples acquired under transient conditions, are of the same order (i.e., they closely envelop) with the constraints estimated based on the full knowledge of the noise level. The $\ell_{1}$-min formulation reduces the inference errors defined in (31) and (29) by $18.53 \%$ and 2 to 3 orders of magnitude, respectively, and improves the sparsity of the solution (measured in terms of Hoyer sparsity measure) by $15.9 \%$, in comparison with conventional approaches including various versions of dynamic Bayesian approaches for network inference as well as ND. If instead of the total influence, only the time series gathered under transient conditions is provided, such as in the case of Michaelis-Menten dynamics, $\ell_{1}$-min approach achieves a 4 order reduction in inference error compared to MRA.

These theoretical and numerical studies suggest that our proposed method can be employed to effectively infer the presence of dynamic coupling (i.e., arc set or the direct influence in a dynamic network) based on sparse samples.

As with any network reconstruction approach, the method assumes that the time series realizations taken together can adequately mirror the salient dynamic regimes of the underlying process ${ }^{52}$, and as noted earlier, the approach is restricted to ensuring high levels of specificity and not sensitivity in identifying the direct influences. Additionally, while the approach is fairly robust to the presence of noise, the estimates $\lambda_{i j}$ from the averaging procedure for the arcs with $s_{i j}^{N}=0$ is guaranteed to converge to zero only in the presence of additive noise. More specifically, one of the following conditions need to hold for the approach to be applicable: (1) the governing equation of the process dynamics is specified, so that $G(t)$ or $R(t)$ can be constructed; (2) one or more realizations of $G(t)$ (based on ND or silencing method) or $R(t)$ (based on MRA) are given. In our experience, 30 realizations ensured the convergence of the averaging method; (3) one realization of a $n$-dimensional time series is available for estimating $G(t)$ using various alternative methods outlined in Feizi et al.'s ${ }^{26}$ or $n^{2}$ time series realizations with the same initial condition are available for estimating $R(t)$ using Eq. (17). Note that Scenario 1 is useful only for applications such as to investigate if there exists a more compact (sparser) network representation to capture the specified process dynamics. In Scenarios 2 and 3, we assume that the noise level or its lower limit is known, and adequate number of realizations are available to ensure convergence of the averaging method. In scenario 3, Eq. (17) yields a finite space-time approximation of the partial derivatives $\frac{\partial s_{i}}{\partial p_{j}}, \frac{\partial \lambda_{i}}{\partial p_{j}}$. They are estimated by perturbing the parameters $p_{j}$ and keeping the initial condition the same for two time series signals. The length of the time series in this case can be really small, or it can just be samples taken over multiple (roughly 30), short (can be even 2 samples) time windows. However, the time steps (or sampling interval) in each time window must be small enough to ensure that $R(t)$ values locally converge. Sensitivity of the network inference performance to time step size, however, needs further investigation.

Efforts are underway to address some of the $\ell_{1}$-min aforementioned limitations. We are investigating a two-stage approach to recover local nonlinear dynamics from sparse time series data. For future research, we will consider a more realistic scenario where not all state variables can be measured. In GRN inference, for example, only the outputs/activations of only those genes that have been discovered are measured. However, unknown genes might have significant influence on the network structure. Removing the effects of unmeasured variables, when combined with the method proposed in this paper, will lead to a more advanced network inference method.

# Acknowledgements 

The authors thank the anonymous reviewers for their constructive comments that have helped improve the manuscript. They also acknowledge the National Science Foundation CMMI division (Grants 1437139 and 1432914) for the generous support of this research. The open access publishing fees for this article have been covered by the Texas A\&M University Online Access to Knowledge (OAK) Fund, supported by the University Libraries and the Office of the Vice President for Research.

## Author Contributions

H.M.T. and S.T.S.B. designed and performed the research, analyzed the resutls and wrote the paper.

## Additional Information

Supplementary information accompanies this paper at http://www.nature.com/srep
Competing financial interests: The authors declare no competing financial interests.
How to cite this article: Tran, H. M. and Bukkapatnam, S. T.S. Inferring sparse networks for noisy transient processes. Sci. Rep. 6, 21963; doi: 10.1038/srep21963 (2016).

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/