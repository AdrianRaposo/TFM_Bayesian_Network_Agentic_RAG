# A discretization procedure for rare events in Bayesian networks 

## 5 Kilian Zwirglmaier \& Daniel Straub

6 Engineering Risk Analysis Group, Technische Universität München
7 (kilian.zwirglmaier@tum.de, straub@tum.de, www.era.bgu.tum.de)

## 8 Abstract

9 Discrete Bayesian networks (BNs) can be effective for risk- and reliability assessments, in which probability estimates of (rare) failure events are frequently updated with new information. To solve such reliability problems accurately in BNs, the discretization of continuous random variables must be performed carefully. To this end, we develop an efficient discretization scheme, which is based on finding an optimal discretization for the linear approximation of the reliability problem obtained from the First-Order Reliability Method (FORM). Because the probability estimate should be accurate under all possible future information scenarios, the discretization scheme is optimized with respected to the expected posterior error. To simplify application of the method, we establish parametric formulations for efficient discretization of random variables in BNs for reliability problems based on numerical investigations. The procedure is implemented into a software prototype. Finally, it is applied to a verification example and an application example, the prediction of runway overrun of a landing aircraft.

## 22 Keywords

23 Bayesian networks; discretization; near-real-time; structural reliability; updating

# 1 Introduction 

For operational risk and reliability management, it is often desirable to compute the probability of a rare event $F$ under potentially evolving information. Examples include warning systems for natural and technical hazards, or the planning of inspection and intervention actions in infrastructure systems. Ideally, this is achieved through Bayesian updating of $\operatorname{Pr}(F)$ with the new information $Z$ to the posterior probability $\operatorname{Pr}(F \mid Z)$. When physically-based or empirical models for predicting the rare event exist, such updating is possible with structural reliability methods (SRM) (Sindel and Rackwitz, 1998, Straub, 2011, Straub et al., 2016). However, it is often difficult to perform the required computations in near-real-time, due to a lack of efficiency or robustness. A modeling and computational framework that does facilitate efficient Bayesian updating is the discrete Bayesian network (BN). Hence it was proposed to combine SRMs with discrete Bayesian networks for near-real-time computations (Friis-Hansen, 2000, Straub and Der Kiureghian, 2010a, Straub and Der Kiureghian, 2010b).

BNs are based on directed acyclic graphs (DAGs), to efficiently define a joint probability distribution $p(\mathbf{Y})$ over a random vector $\mathbf{Y}$ (Jensen and Nielsen, 2007, Kjaerulff and Madsen, 2013). The DAG of a BN, which is often referred to as the qualitative part of a BN, consists of a node for each variable in $\mathbf{Y}$ and a set of directed links among nodes representing dependence among the variables. In the case of discrete BNs, conditional probability tables (CPTs) quantitatively define the type and strength of the dependence among the variables. The entries of the CPT of a variable $Y_{i}$ are the probabilities for each state of $Y_{i}$ conditional on all possible combinations of states of its parents.

For hybrid BNs, which include both discrete and continuous variables, exact inference is available only for two special cases, which are BNs with Gaussian nodes, whose means are linear functions of their parents, and BNs, whose nodes are defined as a mixture of truncated basic functions (MoTBFs) (Langseth et al., 2009, Langseth et al., 2012). Otherwise, approximate inference algorithms are available for hybrid BNs based on sampling techniques, e.g. (Lerner, 2002, Hanea et al., 2006). However, these are computationally demanding and not generally suitable for near-real-time decision support (Hanea et al., 2015). As an alternative, the continuous random variables can be discretized, which enables the use of exact inference algorithms that exist for general discrete BNs. These include the variable elimination algorithm (Zhang and Poole, 1994) and the junction tree algorithm (Lauritzen and Spiegelhalter, 1988, Jensen et al., 1990).

The size of discrete BNs, and the associated computational effort, increases approximately exponentially with the number of discrete states of its nodes, which motivates the development of efficient discretization algorithms. While efficient discretization in the context of machine learning and BNs in general has been investigated by multiple researchers (Dougherty et al., 1995, Kotsiantis and Kanellopoulos, 2006), research on efficient discretization in the context of engineering risk analysis or structural reliability has been limited. In general, it is to be distinguished between static and dynamic discretization. While

the former discretizes the BN a-priori before entering evidence (offline), the latter is based on an iterative scheme that updates the discretization scheme in function of the evidence (online).

Dynamic discretization for risk analysis applications has been developed mainly by (Neil et al., 2008), based on the work by (Kozlov and Koller, 1997). The procedure starts with an initial discretization of a hybrid BN, for which an approximate entropy error is calculated. If the error complies with a convergence criterion, the current discretization is accepted. Otherwise the discretization is iteratively altered, by splitting the intervals with the highest entropy error, until the convergence criterion is fulfilled. The approach is implemented in the software AgenaRisk (Agena, 2005). Other dynamic discretization algorithms for reliability analysis have been proposed, e.g. in (Zhu and Collette, 2015) for dynamic BNs. The advantage of dynamic discretization is its flexibility when evidence is entered in the BN, i.e. when the model is updated with new observation.

Static discretization has the advantage of being computationally faster and simple to implement. Some considerations for static discretization of BNs in reliability applications have been presented in (Friis-Hansen, 2000, Straub, 2009, Straub and Der Kiureghian, 2010a). As pointed out by (Friis-Hansen, 2000), for applications in which extreme events are important, discretization of the distribution tails should be performed with care. Static discretization facilitates a careful representation of these tails. However, the accuracy of the static discretization varies with the available evidence. The difficulty is thus to find a discretization scheme that is optimal under a wide variety of posterior distributions.

In this paper we derive a procedure for efficiently performing static discretization of continuous reliability problems. An optimal discretization scheme is sought, which minimizes the expected approximation error with respect to possible future observations (evidence). To solve this optimization problem, we propose to approximate the reliability problem by the First-Order Reliability Method (FORM). Section 2 of the paper describes the proposed methodology. Section 3 presents numerical parameter studies, and simple parametric relations for defining an efficient discretization scheme are derived. In Section 4, the procedure is applied to a set of verification examples and to the computation of the probability of runway overrun of a landing aircraft. While the theory is introduced for problems with only one design point, considerations regarding problems with multiple design points are given in the last verification example and in the discussion.

# 2 Methodology 

### 2.1 Structural reliability

Since the 1970s structural reliability methods have been developed and applied in the engineering community to estimate failure probabilities $\operatorname{Pr}(F)$ of components or systems, based on physical or empirical models. The performance of engineering components is

described by a limit state function (LSF) $g(\mathbf{x})$, where $\mathbf{X}=\left[X_{1} ; \ldots ; X_{n}\right]$ is a vector of basic random variables influencing the performance of the component. By definition, failure corresponds to $g(\mathbf{x})$ taking non-positive values, i.e. the failure event is $F=\{g(\mathbf{X}) \leq 0\}$. $g(\mathbf{x})$ includes the physical or engineering model, which is often computationally demanding. The probability of failure is calculated by integrating the probability density function (PDF) of $\mathbf{X}$, $f_{\mathbf{X}}(\mathbf{x})$, over the failure domain:
$\operatorname{Pr}(F)=\int_{g(\mathbf{x}) \leq 0} f_{\mathbf{X}}(\mathbf{x}) d \mathbf{x}$
The formulation can be extended to the reliability of general systems by defining the failure domain as a combination of series and parallel systems (Ditlevsen and Madsen, 2007). In the general case, there is no analytical solution to Eq. 2 and the integral is potentially highdimensional. For this reason, structural reliability methods (SRMs) are applied to approximate it. These include the first- and the second order reliability method (FORM and SORM) as well as a large variety of sampling methods, including importance sampling methods such as directional importance sampling, and sequential sampling methods such as subset simulation. These methods are well-documented in the literature (Au and Beck, 2001, Rackwitz, 2001, Der Kiureghian, 2005, Ditlevsen and Madsen, 2007).

# 2.2 First order reliability method (FORM) 

To obtain an approximation of the probability of failure through FORM, the LSF $g(\mathbf{X})$ is transformed to an equivalent LSF $G(\mathbf{U})$ in the space of uncorrelated standard normal random variables $\mathbf{U}=\left[U_{1} ; \ldots ; U_{n}\right]$ (Fig. 1). The transformation is probability conserving, so that $\operatorname{Pr}[g(\mathbf{X}) \leq 0]=\operatorname{Pr}[G(\mathbf{U}) \leq 0]=\operatorname{Pr}(F)$. A suitable transformation for this purpose, which is consistent with the BN, is the Rosenblatt transformation (Hohenbichler and Rackwitz, 1981). In case all basic random variables are independent, this transformation reduces to the marginal transformations: $U_{i}=\Phi^{-1}\left[F_{X_{i}}\left(X_{i}\right)\right]$, with $\Phi^{-1}$ being the inverse standard normal CDF.

![img-0.jpeg](img-0.jpeg)

Figure 1. Design point and linear approximation of the limit state surface. Left side: original random variable space; right side: standard normal space (from (Straub, 2014a)).

The FORM approximation of $\operatorname{Pr}(F)$ is obtained by substituting the LSF in U-space $G(\mathbf{U})$ by a linear function $G_{L}(\mathbf{U})$, i.e. a first-order Taylor expansion of $G(\mathbf{U})$. The key idea of FORM is to choose as the expansion point the so-called design point $\mathbf{u}^{*}$, which is the point that minimizes $\left\|\mathbf{u}^{*}\right\|$ subject to $G_{L}(\mathbf{U}) \leq 0 . \mathbf{u}^{*}$ also known as the most likely failure point, as it is the point in the failure domain with the highest probability density. Since all marginal distributions of the standard uncorrelated multinormal distribution are standard normal, it can be shown that the FORM probability of failure $\operatorname{Pr}\left[G_{L}(\mathbf{U}) \leq 0\right]$ is:

$$
\operatorname{Pr}\left[G_{L}(\mathbf{U}) \leq 0\right]=\Phi\left(-\beta_{F O R M}\right)
$$

where $\Phi$ is the standard normal CDF and $\beta_{F O R M}$ is the distance from the origin to the design point, i.e. $\beta_{F O R M}=\left\|\mathbf{u}^{*}\right\|$. The problem thus reduces to finding the design point $\mathbf{u}^{*}$. If $G(\mathbf{U})$ is linear, the FORM solution of the probability of failure is exact, otherwise it is an approximation, which however is sufficiently accurate in most practical applications with limited numbers of random variables (Rackwitz, 2001).

The linearized LSF $G_{L}(\mathbf{U})$ can be written as:
$G_{L}(\mathbf{U})=\beta_{F O R M}-\alpha^{\mathrm{T}} \mathbf{U}$
where $\boldsymbol{\alpha}=\left[\alpha_{1}, \ldots, \alpha_{\mathrm{n}}\right]$ is the vector of FORM importance measures. These importance measures are defined as:
$\alpha_{i}=\frac{u_{i}^{*}}{\beta_{F O R M}}$

where $u_{i}^{*}$ is the $i$-th component of the design point coordinates. The $\alpha_{i}$ 's take values between -1 and 1 , and it is $\|\boldsymbol{\alpha}\|=1 . \alpha_{i}$ is 0 , if the uncertainty on $U_{i}$ has no influence on $\operatorname{Pr}\left(G_{L}(\mathbf{U}) \leq\right.$ 0 ), and it is 1 or -1 , if $U_{i}$ is the only random variable affecting $\operatorname{Pr}\left(g_{L}(\mathbf{U}) \leq 0\right)$. When the original random variables $X_{i}$ are mutually independent, the $\alpha_{i}$ 's are readily applicable also in the original space, otherwise the $\alpha_{i}$ 's can be transformed as described in (Der Kiureghian, 2005).

# 2.3 Treatment of a reliability problem in a BN 

We combine discrete BNs and structural reliability concepts to facilitate updating of rare event (failure) probabilities under new observations. The general problem setting is illustrated in the BN of Fig. 2. We here limit the presentation to component reliability problems; system problems are considered later. The binary random variable 'Component performance' is described by the LSF $g(\mathbf{X})$.
![img-1.jpeg](img-1.jpeg)

Figure 2. A general BN including a component reliability problem.
The basic random variables $\mathbf{X}$ of the model are included in the BN as parents of 'Component performance'. The nodes $M_{i}$ represent measurements of individual random variables $X_{i}$, and nodes $I_{j}$ represent factors influencing the basic random variables. Dependence between the variables in $\mathbf{X}$ is modeled either directly by links among them (here $X_{2} \rightarrow X_{1}$ and $X_{4} \rightarrow X_{5}$ ) or through common influencing factors (here $I_{2} \rightarrow X_{3}$ and $I_{2} \rightarrow X_{4}$ ). The component performance node can have (multiple) child nodes, which, however, does not impact the discretization of the reliability problem.

Ultimately, the goal is to predict the component performance, i.e. $\operatorname{Pr}(F)$, conditional on other model parameters, such as measurements $M_{i}$ or influencing variables $I_{j}$. Whenever new evidence on these variables is available, the BN should be evaluated (in near-real time) utilizing exact BN inference algorithms.

To enable exact inference algorithms, all continuous random variables are discretized. These include the $\mathbf{X}$, and possibily the $M_{i}$ and $I_{j}$. In the general case, the computational effort for solving the BN is a direct function of the CPT size of 'Component performance'. The size of

this CPT is $2 \prod_{i=1}^{n} n_{i}$, where $n$ is the number of random variables in $\mathbf{X}$, and $n_{i}$ is the number of states used for discretizing $X_{i}$. In this paper we do not describe the discretization of random variables $M_{i}$ and $I_{j}$, since it is typically straightforward and does not contribute significantly to computational performance. The key parameter for computational efficiency and accuracy is the discretization scheme for $\mathbf{X}$, which is described in sections 2.5 and 2.6.

# 2.4 Simplification of BNs through node removal 

Removing random variables from a BN is one possibility to reduce the computational effort associated with a model. A formal approach for removing nodes from a BN is described in (Straub and Der Kiureghian, 2010b). In order to decide which nodes to remove from the BN the following questions should be considered:

- Which random variables are relevant for prediction? (These include 'Component performance'.)
- Which random variables can potentially be observed? (These include the measurement variables.)
- Which random variables simplify the modeling of dependencies? (These are e.g. common influencing factors such as $I_{2}$ in Fig. 2.)
- For which random variables is it desirable to explicitly show their influence on component performance?

If a random variable does not belong to any of these categories, the corresponding node in the BN can be removed. Since the computational efficiency of the model is governed by the size of the CPT of the 'Component state' node, the primary interest is in removing basic random variables $X_{i}$ from the BN. As a measure for the relevance of a basic random variable, importance measures $\alpha_{i}$ from a FORM analysis may be used. To better understand the relation between $\alpha_{i}$ and $X_{i}$ 's relevance for prediction, consider a linearized LSF $G_{L}(\mathbf{U})$. Following (Der Kiureghian, 2005), the variance of $G_{L}(\mathbf{U})$ can be decomposed as:
$\sigma_{G_{L}}^{2}=\|\nabla G\|^{2}\left(\alpha_{1}^{2}+\alpha_{2}^{2}+\cdots+\alpha_{n}^{2}\right)$
where $\nabla G$ denotes the gradient vector of the non-linearized LSF $G(\mathbf{U})$. From Eq. 6 it is seen that a random variable $X_{i}$ with corresponding $\alpha_{i}$ accounts for $\alpha_{i}^{2} \cdot 100 \%$ of the variance $\sigma_{G_{L}}^{2}$. Therefore, observing a random variable $X_{i}$ with $\alpha_{i}=0.1$ will reduce the variance $\sigma_{G_{L}}^{2}$ by $1 \%$, whereas observing $X_{j}$ with $\alpha_{j}=0.5$ will reduce $\sigma_{G_{L}}^{2}$ by $25 \%$.

### 2.5 Discretization of basic random variables

For ease of presentation, we first consider discretization of statistically independent basic random variables $\mathbf{X}$, i.e. the special case of the BN in Fig. 2 in which the $X_{i}$ 's have no parents ${ }^{1}$.

[^0]
[^0]:    ${ }^{1}$ In a BN, basic random variables $\mathbf{X}$ are independent if they are not connected through links, if they have no common (unknown) ancestors and if no evidence is available on any of their joint descendants.

204 The proposed procedure is extended to the general case of dependent basic random variables 205 thereafter.

# 2.5.1 Independent basic random variables 

207 The situation is illustrated in Fig. 3. The performance of the component depends on $n$ statistically independent random variables and is described by a LSF $g(\mathbf{X})=g\left(X_{1}, \ldots, X_{n}\right)$. For all basic random variables $X_{i}$, corresponding measurements $M_{i}$ can be performed. To obtain an equivalent discrete BN, the continuous $X_{i}$ are replaced by the discrete random variables $Y_{i}$, and the LSF is replaced by the CPT of component performance conditional on $\mathbf{Y}=\left[Y_{1} ; \ldots ; Y_{n}\right]$. For each discrete random variable $Y_{i}$ with $n_{i}$ states $1,2, \ldots, n_{i}$, we define a discretization scheme $D_{i}=\left[d_{0}, d_{1}, \ldots, d_{n_{i}-1}, d_{n_{i}}\right]$ consisting of $n_{i}+1$ interval boundaries. The first and the last interval boundaries are given by the boundaries of $X_{i}{ }^{\prime} s$ outcome space.
a) BN with continuous nodes
![img-2.jpeg](img-2.jpeg)

Figure 3. Representation of a basic reliability problem with $n$ independent basic random variables in a BN. Left: original problem with continuous basic random variables $X_{i}$, right: discrete BN, in which $X_{i} \mathrm{~s}$ are substituted with discrete nodes $Y_{i}$.

Since here the $X_{i}$, and thus the $Y_{i}$, have no parents, the PMF of $Y_{i}$ is defined as:

$$
p_{Y_{i}}(j)=F_{X_{i}}\left(d_{j}\right)-F_{X_{i}}\left(d_{j-1}\right) ; \quad \text { with } j \epsilon\left[1, \ldots, n_{i}\right]
$$

221 where $F_{X_{i}}$ denotes the cumulative distribution function (CDF) of $X_{i}$. The probability of failure corresponding to the discrete BN in Fig. 3b can be calculated as:
$\operatorname{Pr}(F)=\sum_{y_{1}=1}^{n_{1}} \ldots \sum_{y_{n}=1}^{n_{n}} p_{Y_{1}}\left(y_{1}\right) \cdot \ldots \cdot p_{\mathrm{Y}_{n}}\left(y_{n}\right) \cdot \operatorname{Pr}\left(F \mid Y_{1}=y_{1} \cap \ldots \cap Y_{n}=y_{n}\right)$
223 Note that the discretization does not introduce any approximation error here, as long as the conditional $\operatorname{Pr}\left(F \mid Y_{1}=y_{1} \cap \ldots \cap Y_{n}=y_{n}\right)$ is computed exactly.

225 Once measurements from the nodes $\mathbf{M}=\left[M_{1} ; \ldots ; M_{n}\right]$ are available, the conditional failure probability can be calculated as:

$$
\operatorname{Pr}(F \mid \mathbf{M}=\mathbf{m}) \approx \frac{1}{p_{\mathbf{M}}(\mathbf{m})} \sum_{y_{1}=1}^{n_{1}} \ldots \sum_{y_{n}=1}^{n_{n}} p_{Y_{1}}\left(y_{1}\right) \cdot p_{M_{1} \mid Y_{1}}\left(m_{1} \mid y_{1}\right) \cdot \ldots \cdot p_{Y_{n}}\left(y_{n}\right) \cdot p_{M_{n} \mid Y_{n}}\left(m_{n} \mid y_{n}\right)
$$

$\cdot \operatorname{Pr}\left(F \mid Y_{1}=y_{1} \cap \ldots \cap Y_{n}=y_{n}\right)$

where $\operatorname{Pr}\left(\mathrm{F} \mid \mathrm{Y}_{1}=\mathrm{y}_{1}, \ldots, \mathrm{Y}_{\mathrm{n}}=\mathrm{y}_{\mathrm{n}}\right)$ is the conditional probability of component failure given $\mathrm{y}_{1}, \ldots, \mathrm{y}_{\mathrm{n}}$. If no measurements are available for some of the basic random variables, the corresponding likelihood terms $\mathrm{p}_{\mathrm{M}_{\mathrm{j}} \mid \mathrm{Y}_{\mathrm{j}}}\left(\mathrm{m}_{\mathrm{j}} \mid \mathrm{y}_{\mathrm{j}}\right)$ are simply omitted in Eq. 9.
While the computation of the unconditional failure probability following Eq. 8 is exact, the computation of the conditional failure probability through Eq. 9 is only an approximation. The reason is that the dependence between the measurement variable $M_{i}$ and the 'Component performance' variable is not fully captured in the discrete BN (see also Straub and Der Kiureghian, 2010b). In Fig. 4, this is illustrated for a reliability problem with one basic random variable $X_{i}$. Both the continuous distribution (Fig. 4a) and the corresponding discretized distribution (Fig. 4b) are updated correctly after observing $M_{1}$. However, for Eq. 9 to be exact, also the conditional failure probabilities $\operatorname{Pr}\left(F \mid Y_{1}=y_{1}\right)$ would need to be updated. This can be observed in Fig. 4a: in interval $Y_{1}=3$, which is the one cut by the limit state surface, the ratio of the probability mass in the failure domain to that in the safe domain changes from the prior to the posterior case, i.e. $\operatorname{Pr}\left(F \mid Y_{1}=3\right) \neq \operatorname{Pr}\left(F \mid Y_{1}=3, M_{1}=m_{1}\right)$. Since the computation of the conditional failure probability following Eq. 9 is based on the prior probability $\operatorname{Pr}\left(F \mid Y_{1}=3\right)$, the discretization introduces an approximation in this case. The error occurs only in the intervals that are cut by the limit state surface.
![img-3.jpeg](img-3.jpeg)

Figure 4. Discretization error in 1D.
In the simple one-dimensional case of Fig. 4, an optimal discretization approach would be to discretize the whole outcome space in two intervals, one capturing the survival and one the failure domain. This discretization would have zero approximation error. However, already in a two-dimensional case, such a solution is not possible. This is illustrated in Fig. 5, where the cells cut by the limit state surface are indicated in grey. The failure probability conditional on measurements calculated according to Eq. 9 will necessarily be an approximation. The approximation error will be small, if the contribution of the cells cut by the limit state surface

(the grey cells in Fig. 5) to the total failure probability is small. An efficient discretization will
thus limit this contribution with as few intervals as possible.
![img-4.jpeg](img-4.jpeg)

Figure 5. Discretization error in 2D.

# 2.5.2 Dependent basic random variables 

259 Eqs. (7-9) must be adjusted when dependence among the $X_{i}$ 's is present, in accordance with 260 the case-specific BN structure. However, the principles outlined above for independent $X_{1}, \ldots, X_{n}$ hold equally for dependent basic random variables: The discretization error is a function of the cells cut by the limit state function.

When determining an optimal discretization, we propose in the following to find the FORM approximation of the reliability problem, which can readily account for the dependence among the random variables. Hence, there is no need to distinguish between cases with independent or dependent random variables.

### 2.6 Efficient discretization

### 2.6.1 Optimal discretization of linear problems in standard normal space

To find an efficient discretization of $\mathbf{X}$, we consider the FORM solution to the reliability problem. Evaluating the linearized FORM LSF $G_{L}(\mathbf{U})$ is computationally inexpensive once the design point $\mathbf{u}^{*}$ is known. Therefore, it is feasible to find a discretization of $\mathbf{U}$ that is optimal for the event $\left\{G_{L}(\mathbf{U}) \leq 0\right\}$ through optimization. If $G(\mathbf{U})$ is not strongly non-linear, this solution will be an efficient discretization for $\{G(\mathbf{U}) \leq 0\}$ and, after a transformation to the original space, also for $\{g(\mathbf{X}) \leq 0\}$.

As discussed in Section 2.5.1, the approximation error of the discretization is associated with the change from the prior to the posterior distribution of the basic random variables. A measure of optimality must thus consider possible measurements of $\mathbf{X}$ or $\mathbf{U}$. We consider hypothetical measurements $\bar{M}_{i}$ (this notation is used to distinguish hypothetical measurements from actual measurements $M_{i}=m_{i}$ ) of all standard normal random variables $U_{i}$ with additive measurement error $\varepsilon_{i} \sim N\left(0, \sigma_{\varepsilon_{i}}\right)$. Since both the prior distribution and the measurement error are normal distributed, the likelihood is also normal distributed:

$\bar{M}_{i} \mid\left\{U_{i}=u_{i}\right\} \sim N\left(u_{i}, \sigma_{z_{i}}\right)$
The posterior, i.e. the conditional distribution of $U_{i}$ given a measurement outcome $\bar{M}_{i}=\bar{m}_{i}$, is the normal distribution with mean $\frac{1}{1+\sigma_{z_{i}}^{2}} \bar{m}_{i}$ and standard deviation $\sqrt{\left(1-\frac{1}{1+\sigma_{z_{i}}^{2}}\right)}$.

We define an error measure based on comparing the true posterior probability of failure $\mathrm{P}_{\mathrm{F} \mid \bar{M}}(\overline{\mathbf{m}})$ with the posterior probability of failure calculated from the discretized $\mathbf{U}$, denoted by $\overline{\mathrm{P}}_{\mathrm{F} \mid \bar{M}}(\mathbf{d} ; \overline{\mathbf{m}})$. Here, $\mathbf{d}$ are the parameters defining the discretization. The proposed error measure is:

$$
e(\mathbf{d}, \overline{\mathbf{m}})=\left|\frac{\log _{10} \overline{\mathrm{P}}_{\mathrm{F} \mid \bar{M}}(\mathbf{d} ; \overline{\mathbf{m}})-\log _{10} \mathrm{P}_{\mathrm{F} \mid \bar{M}}(\overline{\mathbf{m}})}{\log _{10} \mathrm{P}_{\mathrm{F} \mid \bar{M}}(\overline{\mathbf{m}})}\right|
$$

The error measure of Eq. 11 represents a tradeoff between the absolute and the relative error. It weights the (logarithmic) relative error by the magnitude of the posterior failure probability. This ensures that the same relative error is considered worse at a higher probability level compared to an error at a lower probability level.

A-priori, the measurement outcomes are not known. Hence we define the optimal discretization as the one that minimizes the expected preposterior error $\mathrm{E}_{\bar{M}}[e(\mathbf{d}, \overline{\boldsymbol{M}})]$ :
$\mathbf{d}^{o p t}=\arg \min _{\mathbf{d}} \mathrm{E}_{\bar{M}}[e(\mathbf{d}, \bar{M})]=\arg \min _{\mathbf{d}} \int_{\bar{M}} e(\mathbf{d}, \overline{\mathbf{m}}) \mathrm{f}_{\bar{M}}(\overline{\mathbf{m}}) \mathrm{d} \overline{\mathbf{m}}$
The optimization is thus based on the computation of an expected value with respect to the possible measurements outcomes $\overline{\boldsymbol{M}}$ before having taken any measurements. This is analogous to a preposterior analysis (Raiffa and Schlaifer, 1961, Straub, 2014b). However, unlike in traditional preposterior analysis, the objective is not to identify an optimal action under future available information, but to find the optimal discretization parameters $\mathbf{d}^{o p t}$. The integral in Eq. 12 is evaluated through a simple Monte Carlo approach. All $\bar{M}_{i}$ have the normal distribution with zero mean and variance $1+\sigma_{\mathrm{e}}^{2}$.

The parameters in $\mathbf{d}$ describing the discretization scheme are:

- $n_{i}$ : number of intervals used to discretize each random variable $U_{i}$,
- $w_{i}$ : width of the discretization frame in the dimension of $U_{i}$, and
- $v_{i}$ : position of the midpoint of the discretization frame relative to the design point

These parameters are illustrated in Fig. 6. For a problem with $n$ basic random variables, the full set of optimization parameters is $\mathbf{d}=\left[w_{1}, \ldots, w_{n}, n_{1}, \ldots, n_{n-1}, v_{1}, \ldots, v_{n}\right]$.

Clearly, the discretization error reduces with increasing $n_{i}$. Because the computational efficiency of the final BN is a direct function of the size of the CPT associated with component performance, which is $\prod_{i=1}^{n} n_{i}$, we constrain its size. To this end, we define $c_{u p}$ as

the maximum allowed number of parameters of the CPT of the component state node. This puts a constraint on the optimization of Eq. 12:
$\prod_{i=1}^{n} n_{i} \leq c_{u p}$
![img-5.jpeg](img-5.jpeg)

Figure 6. Schematic representation of a discretization of a linear 2D reliability problem. $w_{i}$ is the distance between interval boundaries $\mathrm{d}_{1}^{i}$ and $\mathrm{d}_{n_{i}-1}^{i}$. All intervals between these boundaries are equi-spaced. $v_{i}$ is the position of the midpoint of the discretization frame relative to the design point $\mathbf{u}^{*}$ in dimension $i$.

The optimization is implemented through a two-level approach. The optimization of the continuous parameters width $w_{i}$ and position of the discretization frame $v_{i}$ for all $i=1, \ldots, n$ is carried out using unconstrained nonlinear optimization for fixed values of $n_{i}$. The optimization of the discrete $n_{i}$ is performed through a local search algorithm. Note that the optimization is performed offline, i.e. prior to running the BN, hence it does not affect the goal of near-real time performance of the BN. Furthermore, in section 3 a heuristic is derived that can replace the time-consuming solution of the optimization problem.

# 2.6.2 Efficient discretization of the original random variables $\mathbf{X}$ 

Since the nodes in the BN represent random variables X in their original outcome space, the discretization schemes, which are derived for the corresponding standard normal random variables U , need to be transformed to the X -space. In the case of mutually independent random variables $\mathrm{X}_{\mathrm{i}}$, any point on the i-th interval boundary in U -space - if transformed - will result in the same corresponding i-th interval boundary in X -space. This is not the case for dependent random variables $\mathrm{X}_{\mathrm{i}}$, where a mapping of the interval boundaries in U -space to X space will not lead to an orthogonal discretization scheme in X-space. To preserve orthogonality throughout the transformation, we propose to represent each interval boundary through a characteristic point and determine the boundary in X -space through a transformation of this point. For transforming the interval boundary of $\mathrm{X}_{\mathrm{i}}$, the characteristic

point is selected as the design point $u^{*}$, where the i-th element is substituted by the coordinate of the interval boundary. In Fig. 7 this is shown for an example with $\mathrm{n}=2$ random variables.
a) Discretization in U-space
![img-6.jpeg](img-6.jpeg)
b) Transformed discretization
![img-7.jpeg](img-7.jpeg)

Figure 7. Transformation of a discretization scheme from U-space to X-space. To preserve orthogonality each interval boundary in U-space is represented by a characteristic point. The random variables $X_{1}$ and $X_{2}$ are Weibull distributed with scale and shape parameter 1 and their correlation is 0.5 .

# 3 Development of an efficient discretization procedure 

### 3.1 Optimization of the FORM approximation

We present the optimal discretization for the FORM approximation $G_{L}(\mathbf{U})$ for $n=2$ and $n=3$ dimensions. Extension to higher numbers of random variables is discussed. Because the linear LSF employed in FORM is described only by the reliability index $\beta_{F O R M}$ and the vector $\boldsymbol{\alpha}$ of FORM sensitives (Eq. 4), it facilitates parametric studies.

Initially, we consider a reliability index $\beta_{F O R M}=4.26$, corresponding to a probability of failure of $10^{-5}$. The standard deviation of the additive measurement error is set to either $\sigma_{\varepsilon}=0.5$ or $\sigma_{\varepsilon}=1.0$. Different combinations of FORM sensitivity values $\alpha_{i}$ are selected, to investigate their effect on the optimal discretization. In all investigated cases, we find that the position of the midpoint of the optimal discretization frame coincides with the design point, i.e. $v_{i}^{\text {opt }}=0$. The optimal discretization widths $w_{i}^{\text {opt }}$ vary significantly with the importance measures $\alpha_{i}$, as shown in section 3.1.2. However, the optimal number of intervals $n_{i}^{\text {opt }}$ is approximately the same for all random variables in all investigated cases, independent of the $\alpha_{i}$ values, i.e. $n_{i}^{\text {opt }}=c_{u p}^{1 / n}$.

### 3.1.1 On why the optimal number of intervals $n_{i}^{\text {opt }}$ is independent of $\alpha_{i}$

To better understand why the number of intervals does not depend on $\left|\alpha_{i}\right|$ (for $\left|\alpha_{i}\right|$ that are significantly larger than 0 ), recall that an efficient discretization scheme should focus on the area around the limit state surface. More precisely, the discretization error in the posterior

case is induced by the cells that are cut by the limit state surface. Exemplarily, Fig. 8 shows a linear problem in standard normal space with two basic random variables $U_{1}$ and $U_{2}$, where $\alpha_{1}=0.45$ and $\alpha_{2}=0.89$. While Fig. 8a shows an optimal discretization with 5 intervals per dimension, Fig. 8b shows a discretization scheme, where the more important random variable $U_{2}$ is discretized with 6 intervals and $U_{1}$ with 4 intervals. In both cases, the discretization frame is centered at the design point. It is observed that the probability mass of the (grey) cells, associated with the discretization error in the posterior case, is higher in Fig. 8b than for the optimal discretion scheme in 8 a . In the example shown here it is $1.4 \cdot 10^{-3}$ compared to $2.5 \cdot 10^{-4}$.
![img-8.jpeg](img-8.jpeg)

Figure 8. Linear problem in standard normal space, with two random variables $U_{1}$ and $U_{2}$, where $\alpha_{1}=0.45$ and $\alpha_{1}=0.89$. The intervals cut by the limit state surface, i.e. those which potentially lead to a posterior discretization error are marked in grey.

For input random variables $X_{i}$ with a value of $\left|\alpha_{i}\right|$ close to zero, the above observations do not hold. Following Section 2.4, these variables should be removed from the BN prior to discretization.

# 3.1.2 Dependence of the optimal discretization width on $\alpha_{i}$ 

In the optimization, it is found that the optimal discretization width $w_{i}^{\text {opt }}$ varies strongly with the random variable's importance, expressed through $\alpha_{i}$. It is reminded that the width $w_{i}$ describes the domain in which a fine discretization mesh is applied (Fig. 6). In general, $w_{i}^{\text {opt }}$ decreases with increasing $\alpha_{i}$. This effect can be observed in Fig. 8a, where $U_{2}$ is the more important input random variable and it is $w_{2}^{\text {opt }}<w_{1}^{\text {opt }}$.

A clear relation between $w_{i}^{\text {opt }}$ and $\alpha_{i}$ can be observed by plotting the probability mass enclosed by $w_{i}^{\text {opt }}$ against $\alpha_{i}$, as shown in Fig. 9. The results of Fig. 9 indicate that the probability mass contained within this interval should be a direct function of $\alpha_{i}$. The more important the variable, the finer the discretization around the design point should become. The observed relationship between this probability mass and $\alpha_{i}$ follows a clear trend, and a function can be fitted (Fig. 9). Neither the dimensionality of the problem nor the standard

deviation of the measurement error appear to have an influence on this relation. However, as shown in the following section, it is found that the relation does depend on the prior failure probability of the problem (i.e. on $\beta_{F O R M}$ ) and on the number of intervals $n_{i}$ used to discretize the domain.
![img-9.jpeg](img-9.jpeg)

Figure 9. Logarithm of the probability mass enclosed by the discretization frame plotted against $\alpha_{i} . \Phi$ denotes the standard normal CDF and $u b_{i}$ respectively $l b_{i}$ the last (upper) and the first (lower) interval bound in dimension $i$.

To facilitate the application in practice and extending the results to larger numbers of random variables, in section 3.2 parametric functions are fitted to the optimization results to capture the dependency between the optimal discretization width $w_{i}^{\text {opt }}$ and the FORM importance measures $\alpha_{i}$.

# 3.1.3 Dependence of the optimal discretization on the reliability index $\beta$ and the number of discretization cells $c_{u p}$ 

The influence of the prior failure probability and the maximum size of the CPT, $c_{u p}$, on the optimal discretization is investigated through 10 problems with $n=2$ random variables in standard normal space. The FORM importance measures of the random variables are selected between 0.1 to 0.995 and the standard deviation of the measurement error is fixed to $\sigma_{e}=1.0$. We find that the optimal discretization frame is generally centered at the design point, i.e. $v_{i}^{\text {opt }}=0$, and that the intervals are distributed uniformly among the dimensions.

Firstly, we vary the maximum CPT size $c_{u p}$, i.e. the total number of discretization cells. The reliability index is $\beta_{F O R M}=5.2$. Fig. 10 shows the influence of $c_{u p}$ on the resulting width of the discretization frame $w_{i}$. Three cases are considered: $c_{u p}=25, c_{u p}=100$ and $c_{u p}=400$. These choices correspond to 5,10 and 20 intervals for each random variable. The left side of Fig. 10 shows the relation between the optimal $w_{i}$ and $\left|\alpha_{i}\right|$ The right side of Fig. 10 shows the same relation, where the $w_{i}$ 's are scaled as in Fig. 9, i.e. the logarithm of the probability mass enclosed by the outer interval boundaries is depicted. As in Fig. 9, there is a clear dependence between the scaled $w_{i}$ values and the $\left|\alpha_{i}\right|$ 's. The interval frames increase with increasing number of random variables.

Secondly, we vary the prior failure probability from $10^{-3}(\beta=3.1)$ to $10^{-7}(\beta=5.2)$. The results are shown in Fig. 11. Again, a distinct dependence between the scaled $w_{i}$ values and

the $\left|\alpha_{i}\right|$ 's is found. The interval frames decrease with increasing reliability index (with decreasing failure probability).

# 3.2 Parametric function of optimal discretion frame 

As evident from Fig. 10 and Fig. 11, there is a clear dependence of the probability mass enclosed by the optimal discretization frame (with width $w_{i}$ ) on the FORM sensitivity values $\left|\alpha_{i}\right|$. The following parameteric function captures this dependence:
$\log \left(\Phi\left(u b_{i}\right)-\Phi\left(l b_{i}\right)\right)=a \cdot \exp \left(b \cdot\left|\alpha_{i}\right|\right)$
$u b_{i}$ is the upper and $l b_{i}$ the lower interval boundary in dimension $i$, such that $w_{i}=u b_{i}-l b_{i}$. $a$ and $b$ are the parameters of the exponential function. This function is depicted in Figs. 10 and 11. Tab. 1 shows the parameter values $a$ and $b$ for the different combinations of the prior reliability index $\beta$ and number of intervals per dimension
Table 1. Parameters $a$ and $b$ of Eq. 14 for $\beta=3.1, \beta=4.3$ and $\beta=5.2$ as well as 5,10 and 20 intervals per dimension.


From the left sides of Fig. 10 and Fig. 11, it can be observed that the relation between $\alpha_{i}{ }^{2}$ and the optimal $w_{i}$ is fairly diffuse for random variables with $\left|\alpha_{i}\right|<0.6$. Here, the parametric relationship of Eq. 14 is less accurate. However, these random variables by definition have lower importance on the reliability estimate. Hence, the inaccuracy of Eq. 14 for random variables with $\left|\alpha_{i}\right|<0.6$ is not critical, as is confirmed by the numerical investigations performed in the remainder of the paper.

The parameter values of Tab. 1 are derived from two-dimensional problems. In Fig. 9 it is shown that there are no notable differences between two and three dimensions. On this basis, it is hypothesized that the heuristics are applicable also to problems with higher dimensions. This assumption is furthermore supported by the verification examples presented in chapter 4, where the heuristics are applied also to four-dimensional problems without any notable deterioration in the results.

a) 5 intervals per random variable
![img-10.jpeg](img-10.jpeg)
b) 10 intervals per random variable
![img-11.jpeg](img-11.jpeg)
c) 20 intervals per random variable
![img-12.jpeg](img-12.jpeg)

Figure 10. Optimization results for 10 two-dimensional, linear problems in standard normal space, which are discretized with 5, 10 and 20 intervals per dimension. In all cases the prior failure probability is $10^{-7}(\beta=5.2)$. The crosses represent the optimization results. The solid lines are the fitted parametric functions (Eq. 14). The left-hand side shows the relation between the width of a discretization frame $w_{\mathrm{i}}$ and $\left|\alpha_{\mathrm{i}}\right|$ and the right-hand side shows the relation between the probability mass enclosed by the discretization frame with width $w_{\mathrm{i}}$ and $\left|\alpha_{\mathrm{i}}\right|$.

a) $\beta=3.1, \operatorname{Pr}(F)=10^{-3}$
![img-13.jpeg](img-13.jpeg)
b) $\beta=4.3, \operatorname{Pr}(F)=10^{-5}$
![img-14.jpeg](img-14.jpeg)
c) $\beta=5.2, \operatorname{Pr}(F)=10^{-7}$
![img-15.jpeg](img-15.jpeg)

Figure 11. Optimization results for 10 two-dimensional, linear problems in standard normal space, which are discretized with 10 intervals per dimension. The prior failure probabilities are $10^{-3}(\beta=3.1), 10^{-5}(\beta=4.3)$ and $10^{-7}(\beta=5.2)$. The crosses represent the optimization results. The solid lines are the fitted parametric functions (Eq. 14). The left-hand side shows the relation between the width of a discretization frame $w_{i}$ and $\left|\alpha_{i}\right|$ and the right-hand side shows the relation between the probability mass enclosed by the discretization frame with width $w_{i}$ and $\left|\alpha_{i}\right|$.

# 3.3 Summary of the proposed procedure 

The steps of the proposed procedure are:

1. Formulate the reliability problem

2. Set up the corresponding BN
3. Perform a FORM analysis for the reliability problem
4. Simplify the BN by removing nodes based on:
a. their importance for prediction
b. their observability
c. whether or not a node simplifies modeling of dependencies
d. whether or not it is desired to explicitly show a node in the BN for communication purposes
5. Find the discretization scheme in U-space based on the proposed heuristics i.e.:
a. the discretization scheme is centered at the design point from the FORM analysis
b. the same number of intervals is used for each random variable
c. the width of the discretization frame follows Eq. 14
6. Transform the discretization scheme to X-space
7. Compute the CPTs of the component state node and the basic random variables using Monte Carlo simulation or Latin hypercube sampling

A MATLAB-based software tool performing these steps is available for download under www.era.bgu.tum.de/software.

# 4 Applications 

### 4.1 Verification example I

478 For verification purposes, we apply the proposed methodology to the discretization of a general limit state with non-normal dependent random variables. The approximation error made by this discretization is investigated for different measurement outcomes.

481 Failure is defined through the LSF $g(\mathbf{x})$ :
$g(\mathbf{x})=a-\prod_{i=1}^{n} X_{i}$
482 i.e., failure corresponds to the event $\left\{\prod_{i=1}^{n} X_{i} \geq a\right\}$.
483 The basic random variables are distributed as $X_{1} \sim L N(0,0.5)$ and $X_{2}, \ldots, X_{\mathrm{n}} \sim L N(1,0.3)$ (values in parenthesis are the parameters of the lognormal distribution). The statistical dependence among the $X_{i}$ is described through a Gaussian copula model, with pairwise correlation coefficients $\rho_{i j}$. The parameters $a$ and $\rho_{i j}$ determine the prior failure probability $P_{F}$. Measurements $M_{\mathrm{i}}=m_{\mathrm{i}}$ are available for all basic random variables; they are associated with multiplicative measurement errors $\varepsilon_{\mathrm{i}} \sim \operatorname{LN}(0,0.71)$. In Tabs. 2 and 3, different cases with 3 and 4 random variables are shown. These cases differ with respect to the prior failure

probability $P_{F}$, the correlation between the random variables $\rho_{i j}$ and the observed measurements $\mathbf{m}$. For each case, a reference solutions $P_{F \mid \mathbf{M}}$ is calculated analytically.

Table 2. Evaluation of the discretization error for different measurement outcomes $\mathbf{m}$, for problems with $n=3$ random variables. $a$ is the constant in the LSF, Eq. 15; $\rho_{i j}$ is the correlation coefficient between $X_{i}$ and $X_{j}$ for all $i \neq j ; P_{F}$ and $\mathrm{P}_{\mathrm{F} \mid \mathbf{M}}$ denote the analytically calculated prior and posterior failure probabilities; $\bar{P}_{F \mid M}$ is the conditional failure probability calculated with the discrete BN.


Table 3. Evaluation of the discretization error for different measurement outcomes $\mathbf{m}$. The number of random variables $n=4 ; a$ is the constant in the LSF, Eq. 15; $\rho_{i j}$ is the correlation coefficient between $X_{i}$ and $X_{j}$ for all $i \neq j ; P_{F}$ and $P_{F \mid M}$ denote the analytically calculated prior and posterior failure probabilities; $\bar{P}_{F \mid M}$ is the conditional failure probability calculated with the discrete BN.


503 The results in Tables 2 and 3 show that the proposed methodology for discretization leads to errors in the posterior probability estimate that are acceptably small for most engineering applications. (It is reminded that discretization does not lead to a discretization error in the prior case.) As expected, the relative error is larger when the posterior probability is low, and the absolute error is larger when the posterior probability is high. This follows from the error measure defined in Eq. 11, which balances the relative with the absolute error. In addition, the results do not display any apparent effect of correlation on the accuracy.

510 To assess the effect of the choice of the number of discretization intervals, the failure
511 probability $\widehat{\mathrm{P}}_{\mathrm{F} \mid \boldsymbol{M}}$ was calculated for a discretization scheme with up to 20 intervals per RV for
512 the fourth measurement case in Tab. 2. The estimated failure probabilities $\widehat{\mathrm{P}}_{\mathrm{F} \mid \boldsymbol{M}}$ are plotted
513 together with the exact solution in Fig. 12.
![img-16.jpeg](img-16.jpeg)

514
515 Figure 12. Posterior probability $\hat{P}_{F \mid M}$ as a function of the number of intervals per random variable together with the exact (analytical) solution $P_{F \mid M}$ for the fourth measurement case $[1.6,2.0,1.2]$ in Tab 2.

# 4.2 Verification example II 

518 The failure criterion applied in verification example I (Eq. 15) leads to a linear LSF in Uspace. To verify the accuracy of the proposed method for problems with non-linear LSFs in U-space, we additionally investigate the following LSF:
$g(\mathbf{x})=a-\sum_{i=1}^{n} X_{i}$
521 Again the basic random variables $X_{1}$ to $X_{n}$ are distributed as $X_{1} \sim L N(0,0.5)$ and $X_{2}, \ldots, X_{n} \sim L N(1,0.3)$. Different cases with $n=2,3$ and 4 random variables are investigated. Measurements $M_{\mathrm{i}}=m_{\mathrm{i}}$ are available for all basic random variables; associated to these measurement are multiplicative measurement errors $\varepsilon_{\mathrm{i}} \sim \operatorname{LN}(0,0.71)$. For independent random variables $X_{i}$ it is possible to determine posterior distributions $f_{X_{i} \mid M_{i}}\left(x_{i} \mid m_{i}\right)$ analytically. The posterior failure probabilities $P_{F \mid M}$, which are used as reference solutions, are calculated through importance sampling with $10^{7}$ samples. The results are presented in Tab. 4.

Table 4. Evaluation of the discretization error for different measurement outcomes $\mathbf{m}$. The problems have $n=2,3$ or 4 random variables; $a$ is the constant in the LSF, Eq. $16 ; \rho_{i j}$ is the correlation coefficient between $X_{i}$ and $X_{j}$ for all $i \neq j ; P_{F}$ and $P_{F \mid M}$ denote the prior respectively posterior failure probabilities, which are calculated through importance sampling with $10^{7}$ samples; $\bar{P}_{F \mid M}$ is the conditional failure probability calculated with the discrete BN. Since for correlated basic random variables there is no analytical solution, in these cases the updating of the basic random variables was performed through rejection sampling with $>5 E 7$ accepted samples.


$\underline{n=2:}$


$\underline{n=3:}$


$\underline{n=4:}$


537 The results in Tab. 4 do not differ substantially from Tabs. 2 and 3. This indicates that the (weak) non-linearity of the LSF function describing failure does not affect the accuracy 539 significantly.

# 4.3 Runway overrun 

541 Runway overrun (RWO) of a landing aircraft is one of the most critical accidents types in 542 civil aviation (IATA, 2013). A conceptual RWO warning system is developed with the

proposed discretization procedure. It provides RWO probabilities conditional on observations of the landing-weight, the headwind and the approach speed for different aircraft types and different airports. For a detailed description of how this problem can be treated in BN framework we refer to (Zwirglmaier and Straub, 2015).

RWO is the event of the operational landing distance exceeding the available runway length (Fig. 13). Correspondingly, a LSF for runway overrun can be defined as:

$$
g(\mathbf{X})=\text { Runway length }- \text { Operational landing distance }(\mathbf{X})
$$

with $\mathbf{X}$ representing the basic random variables of the problem.
(Drees and Holzapfel, 2012) proposed a model for the operational landing distance required by a landing aircraft, which is applied here. The model, as well as the basic random variables $\mathbf{X}$, are presented in (Zwirglmaier et al., 2014), which also includes a detailed description of the reliability and sensitivity analysis.

We consider two different airports (AP I and AP II) and two different aircraft types (AC A and AC B). While the aircraft type affects the landing-weight, the airport affects both the headwind and the approach speed. The distribution models for landing-weight, headwind and approach speed deviation at the different airports and with the different aircraft types are given in Tabs. 5-7. All other basic random variables of the problem are not affected by the airport and aircraft type and are as in (Zwirglmaier et al., 2014).

Tab. 8 summarizes the FORM importance measures of all random variables $\mathbf{X}$ computed for the four combinations of aircrafts and airports.
![img-17.jpeg](img-17.jpeg)

Figure 13. Runway definitions.

567 Table 5. Distribution models for landing weight conditional on the aircraft.


Table 6. Distribution models for head wind conditional on the airport.


570
Table 7. Distribution models for approach speed deviation conditional on the airport.


573
Table 8. FORM importance measures $\alpha_{i}$ for each aircraft-airport combination and every basic random variable in the RWO application.


# 4.3.1 Selection of relevant random variables 

The applied RWO model includes 10 basic random variables. However, it is sufficient to include only a selection of these explicitly in the BN. Random variables that are not relevant for the prediction of RWO in the considered scenarios can be excluded. This is the case for random variables with a low FORM importance, whose value does not depend significantly on airport and aircraft type. Here, all random variables, whose absolute value of the FORM importance measure $\left|\alpha_{i}\right|^{\prime} s$ is smaller than 0.1 , are excluded (see Tab. 8). The one exception is landing weight, since its mean value is substantially influenced by the aircraft type.

One can additionally exclude random variables that cannot be measured before the decision on whether to land or not is made. This holds for Touchdown point and the time at which the pilot initiates breaking. Since these basic random variables are also not needed to simplify the modeling of dependencies, it is not necessary to explicitly model them in the BN, as indicated in Tab. 8.

### 4.3.2 BN model

The resulting BN of the RWO warning system is shown in Fig. 14. During the aircraft approach, measurements can be obtained for the three basic random variables included in the BN.

The random variables are discretized separately for each aircraft-airport combination (joint states of discrete parents) with 8 intervals each, following the proposed discretization procedure. In a second step, the discretization schemes are merged, i.e. the regions of the outcome space, which are discretized with fine intervals for at least one of the aircraft-airport combinations, are discretized with the respective fine intervals also in the merged discretization scheme. In the end 15 (landing-weight), 10 (headwind) and 9 (approach speed deviation) intervals are used to discretize the three basic random variables.

For all observable quantities, the measurements $m_{i}$ are modeled with an additive observation error:

$$
m_{i}=x_{i}+\varepsilon_{i}
$$

$\varepsilon_{i}$ is modeled by a normal distribution with zero mean and standard deviation $\sigma_{\varepsilon_{i}}$.
For the random variable landing weight (at landing time), the standard deviation of the measurement error is $\sigma_{\varepsilon_{L W}}=0.34$ tons. Due to turbulences governing wind speeds, the measurement of the head wind speed at the time of the measurement is only an uncertain indicator for the head wind speed at landing time; we model the measurement error with a standard deviation $\sigma_{\varepsilon_{H W}}=2.88 \mathrm{kts}$. The measurement uncertainty associated with the approach speed deviation at landing has standard deviation $\sigma_{\varepsilon_{A S D}}=4.21 \mathrm{kts}$.

49 (Measurement LW), 57 (Measurement HW) and 57 (Measurement ASD) intervals are used to discretize the measurement nodes.

![img-18.jpeg](img-18.jpeg)

Figure 14. BN structure for a RWO warning system.

# 4.3.3 Results 

In Tab. 9, RWO probabilities for the different airports and aircrafts obtained with the discrete BN are compared to solutions, which were calculated by importance sampling around the design point.

Table 9. RWO probabilities for the different airports and aircrafts calculated with the discrete $\mathrm{BN} p_{B N}$, together with solutions calculated by importance sampling around the design point $p_{D S}$. The latter have a sampling error with coefficient of variation in the order of $10 \%$.


In Tab. 10, results obtained with the BN for different hypothetical cases of aircrafts approaching an airport are presented. In each of these cases, measurements associated with landing weight, headwind and the approach speed deviation are made. A threshold on the probability of RWO is used to decide, whether or not the pilot should continue landing or cancel the landing attempt. Here we assume that up to a RWO probability of $10^{-6}$ the pilot should continue landing.

Table 10. Probabilities of RWO and corresponding decision on landing, computed with the BN for different sets of observations.


# 5 Discussion 

When modeling with BNs, it is often necessary or beneficial to discretize continuous random variables. When the BN includes rare events that are a function of such random variables, the choice of the discretization scheme is non-trivial. In this contribution, we investigate this discretization based on FORM concepts, and propose a heuristic procedure for an efficient discretization in these cases. This is based on importance measures $\alpha_{i}$ obtained through a FORM analysis, which represent the influence of the uncertainty associated with a random variable $X_{i}$.

The most important finding is that discretization should focus on the area around the most likely failure point (design point), identified by a FORM analysis. Furthermore, we find that optimally all random variables should be discretized with approximately equal numbers of intervals, independent of their importance, as long as $\left|\alpha_{i}\right|$ is not close to zero. The widths of the intervals should be selected based on the FORM importance $\alpha_{i}$ of the random variables. With increasing importance, the interval width should be reduced, leading to finer discretization for larger $\left|\alpha_{i}\right|$. This relation is particularly evident for $\left|\alpha_{i}\right| \geq 0.8$. We show that it is possible to fit a parametric function to approximate the relation between $\left|\alpha_{i}\right|$ and the optimal width of the region on which the discretization should focus.

This parametric function is used to derive a heuristic procedure for finding an efficient discretization. This allows the extrapolation of the optimization results to problems with more random variables. As demonstrated by the verification examples, the heuristic procedure leads to accurate results.

This paper is restricted to static discretization. Application of the proposed procedure within dynamic discretization (e.g. (Neil et al., 2008)) should be investigated. The results of the procedure can serve as an initial discretization scheme, which is iteratively adjusted within dynamic discretization. This might strongly enhance the convergence performance of these algorithms.

The gain in computational efficiency resulting from the proposed procedure over alternative static discretization approaches is problem specific. Some insights can be gained from Figure 8. A discretization with intervals of equal width centered at the origin would require between approximately 2 to 5 times more intervals per random variable to achieve the same accuracy.

Because of the exponential increase of computational effort with number of random variables, this leads to a considerable increase in efficiency. The gain compared to discretization with equal-frequency intervals is expected to be even higher, since equal frequency intervals focuses the fine intervals on the region of high probability density rather than on the tails of the distribution.

This paper focuses on component reliability problems, which are characterized by a single design point. Nevertheless the heuristics derived can also be applied to system reliability problems. System reliability problems can in general be treated as combinations of component reliability problems. Parallel and series systems are to be distinguished. For parallel systems discretization should be performed based on the joint design point of the problem. For series systems, following the same line of thought as in the runway overrun example, discretization can be performed separately for each component problem (corresponds to the discrete cases i.e. airport- aircraft combinations in the RWO example). In a second step the discretization schemes can be merged. In the same way it is possible to apply the heuristic to multi state components. One can treat each limit state surface (LSF) defining the boundary between two states separately and merge the discretization schemes afterwards.

The number of basic random variables in a single LSF that can be modeled explicitly in a BN is limited to around 5 to 8 . This is due to the exponential growth of the target nodes CPT with increasing number of parents and is independent of the discretization method. Despite this limitation, BNs are applicable to many practical problems - particularly if one considers that usually not all basic random variables need to be modeled explicitly as nodes, as demonstrated in the presented example.

While in this paper the focus was on the discretization of the basic random variables, it is straightforward to incorporate the BNs discussed into larger models.

# 6 Conclusion 

We investigate discretization of continuous reliability problems such that they can be treated in a discrete Bayesian network framework. Reliability problems with linear LSF in standard normal space are considered. These can be seen as FORM approximations of reliability problems. For these linear LSFs, optimal discretization schemes are found, which are optimal with respect to an error measure calculated through a preposterior analysis. Since FORM is known to give good approximations also for most non-linear reliability problem, the resulting discretization schemes are efficient also for non-linear LSFs. The main findings presented in this paper are:

- An optimal discretization scheme should discretize finely the area around the FORM design point.

- The size of the sub-region of the outcome space of a random variable $X_{i}$ can be reduced significantly for random variables whose corresponding uncertainty is dominating the reliability problem
- The number of intervals used for discretization should be approximately equal for all basic random variables

701 On this basis, we propose a heuristic that can be used to find an efficient discretization scheme. In verification examples, this heuristic is found to give good accuracy and efficiency.
