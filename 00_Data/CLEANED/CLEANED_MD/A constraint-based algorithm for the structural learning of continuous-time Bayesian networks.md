# A Constraint-Based Algorithm for the Structural Learning of Continuous-Time Bayesian Networks 

Alessandro Bregoli ${ }^{\dagger \mathrm{a}}$, Marco Scutari ${ }^{\mathrm{b}}$, Fabio Stella ${ }^{\mathrm{a}}$<br>${ }^{a}$ Department of Informatics, Systems and Communication, University of Milan-Bicocca, Milan, Italy<br>${ }^{b}$ Istituto Dalle Molle di Studi sull'Intelligenza Artificiale (IDSIA), Lugano, Switzerland


#### Abstract

Dynamic Bayesian networks have been well explored in the literature as discretetime models: however, their continuous-time extensions have seen comparatively little attention. In this paper, we propose the first constraint-based algorithm for learning the structure of continuous-time Bayesian networks. We discuss the different statistical tests and the underlying hypotheses used by our proposal to establish conditional independence. Furthermore, we analyze and discuss the computational complexity of the best and worst cases for the proposed algorithm. Finally, we validate its performance using synthetic data, and we discuss its strengths and limitations comparing it with the score-based structure learning algorithm from Nodelman et al. (2003). We find the latter to be more accurate in learning networks with binary variables, while our constraint-based approach is more accurate with variables assuming more than two values. Numerical experiments confirm that score-based and constraintbased algorithms are comparable in terms of computation time.


Keywords: Continuous-time, Bayesian networks, structure learning, constraint-based algorithm.

## 1. Introduction

Multivariate time-series data are becoming increasingly common in many domains such as healthcare, medicine, biology, finance, telecommunications, social networks, e-commerce, and homeland security. Their size, (the number of observations), and dimensionality, (the number of variables), are set to continue to increase in the future, requiring automated algorithms to discover the probabilistic structure of the underlying data-generating process and to predict their trajectories over time.

[^0]
[^0]:    Email addresses: a.bregoli1@campus.unimib.it (Alessandro Bregoli ${ }^{\dagger}$ ), scutari@idsia.ch (Marco Scutari), fabio.stella@unimib.it (Fabio Stella)
    $\dagger$ Corresponding author

In this paper we focus on the problem of learning the structure of continuoustime Bayesian networks (CTBNs; Nodelman et al., 2002) from data. This type of probabilistic graphical model has been successfully used to reconstruct transcriptional regulatory networks from time-course gene expression data (Acerbi et al., 2016), to model the presence of people at their computers (Nodelman and Horvitz, 2003), and to detect network intrusion (Xu and Shelton, 2008). Recently CTBNs have been extended to model; non-stationary time series (Villa and Stella, 2016), survival times with arbitrary distributions (Engelmann et al., 2020), and situations where a system's state variables could be influenced by occurrences of external events such as interventions (Bhattacharjya et al., 2020). The literature implements CTBN structure learning using score-based algorithms that maximize the Bayesian-Dirichlet equivalent (BDe) metric.

The main contributions of this paper are:

- the design of the first constraint-based algorithm for the structure learning of CTBNs, which we call Continuous-Time PC (CTPC);
- the definition of suitable test statistics to assess conditional independence in CTBNs;
- the time complexity analysis of best and worst cases of the CTPC algorithm;
- an empirical performance comparison between score-based algorithm and our proposal.

The rest of the paper is organized as follows. We introduce CTBNs and the associated score-based structure learning algorithms in Section 2. After a brief introduction to constraint-based learning for BNs (Section 3.1), we propose a constraint-based algorithm and the associated conditional independence tests for CTBNs in Section 3.2, followed an analysis of their time complexity analysis in Section 3.3. We then compare score-based and constraint-based approaches in Section 4, summarizing our conclusions in Section 5.

# 2. Continuous-Time Bayesian Networks 

CTBNs are a class of probabilistic graphical models that combines Bayesian networks (BNs; Koller and Friedman, 2009) and homogeneous Markov processes to model discrete-state continuous-time dynamical systems (Nodelman et al., 2002). Compared to their discrete-time counterpart, dynamic Bayesian networks (DBNs), they can efficiently model domains like those mentioned above in which variables evolve at different time granularities.

Several approximate inference algorithms for filtering and smoothing in CTBNs have been proposed in the literature (Celikkaya et al., 2012; El-Hay et al., 2010; Nodelman et al., 2012a; Fan et al., 2010), while complexity of exact and approximate inference in CTBNs has been shown to be NP-hard (Sturlaugson and Sheppard, 2014). .

CTBNs are particularly interesting because they allow us to discuss and reason more naturally about systems in which: $i$ ) events, measurements, or durations are irregularly spaced, ii) rates vary by orders of magnitude, or iii) the duration of continuous measurements need to be expressed explicitly. Other models that can represent discrete-state continuous time processes include Poisson networks (Rajaram et al., 2005), cascade of Poisson process model (Simma and Jordan, 2010), piecewise-constant intensity models (Gunawardana et al., 2011), forest-based point processes (Weiss and Page, 2013), and graphical models for marked point processes (Didelez, 2008).

The main advantages of CTBNs, when compared to the models above, are:

- their graphical structure makes it possible to understand and explain the underlying stochastic process they model,
- prior knowledge from domain experts can be integrated in structure learning by blacklisting and whitelisting arcs.

However, CTBNs have a number of limitations: they do not allow modeling continuous state variables; they do not model point events very well, particularly if there are non-temporal values associated with the events; and structure learning is computationally challenging.

# 2.1. Definitions and Notations 

CTBNs are based on finite-state continuous-time homogeneous Markov processes, that is, stochastic processes in which the transition intensities do not depend on time. Let $X$ be a random variable whose state can take $m$ discrete values $\operatorname{Val}(X)=\left\{x_{1}, \ldots, x_{m}\right\} . X$ changes its state continuously over time $t$. A homogeneous Markov process $X(t)$ is described with its intensity matrix:

$$
\mathbf{Q}_{X}=\left[\begin{array}{cccc}
-q_{x_{1}} & q_{x_{1} x_{2}} & \cdots & q_{x_{1} x_{m}} \\
q_{x_{2} x_{1}} & -q_{x_{2}} & \cdots & q_{x_{2} x_{m}} \\
\vdots & \vdots & \ddots & \vdots \\
q_{x_{m} x_{1}} & q_{x_{m} x_{2}} & \cdots & -q_{x_{m}}
\end{array}\right]
$$

The matrix $\mathbf{Q}_{X}$ allows us to describe the transient behaviour of the random variable $X$. If at time $t=0$ the random variable is in state $x_{i}$, then it stays there for an amount of time that is distributed as an exponential random variable with parameter $q_{x_{i}}$. Therefore, the probability density function $f(t)$ and the distribution function $F(t)$ for the random variable $X(t)$ to remain in state $x_{i}$ are

$$
f(t)=q_{x_{i}} \exp \left(-q_{x_{i}} t\right) \quad \text { and } \quad F(t)=1-\exp \left(-q_{x_{i}} t\right)
$$

where $t \geq 0$. The expected time of transitioning from state $x_{i}$ is $1 / q_{x_{i}}$; when transitioning from state $x_{i}$ the random variable $X$ shifts to state $x_{j}$ with probability $q_{x_{i} x_{j}} / q_{x_{i}}$.

However, the size of the intensity matrix $\mathbf{Q}_{X}$, which corresponds to the state space of the Markov process, grows exponentially with the number of variables and with their cardinality. This makes the above representation infeasible for models including more than a very small number of variables. Therefore, we introduce conditional Markov processes in order to model larger Markov processes as CTBNs.

A conditional Markov process is an inhomogeneous Markov process in which, for any given random variable, the intensities are a function of the current values of a particular set of other variables, which also evolve as Markov processes. Therefore, intensities vary over time but not as a function of time. To clarify how a conditional Markov process is described, let $X$ be a random variable whose domain is $\operatorname{Val}(X)=\left\{x_{1}, \ldots, x_{m}\right\}$ and assume that it evolves as a Markov process $X(t)$. Furthermore, assume that the dynamics of $X(t)$ are conditionally dependent from a set $\mathbf{U}$ of random variables evolving over time. Then the dynamics of $X(t)$ can be fully described by means of a conditional intensity matrix (CIM), which can be written as follows:

$$
\mathbf{Q}_{X \mid \mathbf{U}}=\left[\begin{array}{cccc|c}
-q_{x_{1} \mid \mathbf{u}} & q_{x_{1} x_{2} \mid \mathbf{u}} & \cdots & q_{x_{1} x_{m} \mid \mathbf{u}} \\
q_{x_{2} x_{1} \mid \mathbf{u}} & -q_{x_{2} \mid \mathbf{u}} & \cdots & q_{x_{2} x_{m} \mid \mathbf{u}} \\
\vdots & \vdots & \ddots & \vdots \\
q_{x_{m} x_{1} \mid \mathbf{u}} & q_{x_{m} x_{2} \mid \mathbf{u}} & \cdots & -q_{x_{m} \mid \mathbf{u}}
\end{array}\right]
$$

A CIM is a set of intensity matrices, one intensity matrix for each instance of values $\mathbf{u}$ to the set of variables $\mathbf{U}$.

A CTBN models a stochastic process over a structured state space for a set of random variables $\mathbf{X}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$, where each $X_{k} \in \mathbf{X}$ takes values over a finite domain $\operatorname{Val}\left(X_{k}\right)$. It encodes such a process in a compact form by factorizing its dynamics into local continuous-time Markov processes that depend on a limited set of states.

Definition 1. (Nodelman et al., 2002) A CTBN $\mathcal{N}$ over $\mathbf{X}$ is characterized by two components:

- An initial distribution $\mathrm{P}^{0}(\mathbf{X})$, specified as a BN over $\mathbf{X}$.
- A continuous-time transition model specified as:
- a directed (possibly cyclic) graph $\mathcal{G}$ whose nodes correspond to the $X_{k} \in \mathbf{X}$
- a conditional intensity matrix $\mathbf{Q}_{X_{k} \mid \mathbf{U}}$ for each $X_{k}$.

The conditional intensity matrix (CIM) $\mathbf{Q}_{X_{k} \mid \mathbf{U}}$ consists of the set of intensity matrices

$$
\mathbf{Q}_{X_{k} \mid \mathbf{u}}=\left[\begin{array}{cccc|c}
-q_{x_{1} \mid \mathbf{u}} & q_{x_{1} x_{2} \mid \mathbf{u}} & \cdots & q_{x_{1} x_{m} \mid \mathbf{u}} \\
q_{x_{2} x_{1} \mid \mathbf{u}} & -q_{x_{2} \mid \mathbf{u}} & \cdots & q_{x_{2} x_{m} \mid \mathbf{u}} \\
\vdots & \vdots & \ddots & \vdots \\
q_{x_{m} x_{1} \mid \mathbf{u}} & q_{x_{m} x_{2} \mid \mathbf{u}} & \cdots & -q_{x_{m} \mid \mathbf{u}}
\end{array}\right], \quad m=\left|\operatorname{Val}\left(X_{k}\right)\right|,{ }^{3}
$$

one for each possible configuration $\mathbf{u}$ of the parents $\mathbf{U}$ of $X_{k}$ in $\mathcal{G}$.
The diagonal elements of $\mathbf{Q}_{X_{k} \mid \mathbf{u}}$ are such that $q_{x_{i} \mid \mathbf{u}}=\sum_{x_{j} \neq x_{i}} q_{x_{i} x_{j} \mid \mathbf{u}}$, where $q_{x_{i} \mid \mathbf{u}}$ is the parameter of the exponential distribution associated with state $x_{i}$ of variable $X_{k}$. Therefore, $1 / q_{x_{i} \mid \mathbf{u}}$ is the expected time that variable $X_{k}$ stays in state $x_{i}$ before transitioning to a different state $x_{j}$ when $\mathbf{U}=\mathbf{u}$. The off-diagonal elements $q_{x_{i} x_{j} \mid \mathbf{u}}$ are proportional to the probability that $X_{k}$ transitions from state $x_{i}$ to state $x_{j}$ when $\mathbf{U}=\mathbf{u}$.

Note that, conditional on $X_{k}, \mathbf{Q}_{X_{k} \mid \mathbf{u}}$ can be equivalently summarized with two independent sets of parameters:

- $\mathbf{q}_{X_{k} \mid \mathbf{u}}=\left\{q_{x_{i} \mid \mathbf{u}}, \forall x_{i} \in \operatorname{Val}\left(X_{k}\right)\right\}$, the set of intensities of the exponential distributions of the waits until the next transition; and
- $\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}=\left\{\theta_{x_{i} x_{j} \mid \mathbf{u}}=q_{x_{i} x_{j} \mid \mathbf{u}} / q_{x_{i} \mid \mathbf{u}}, \forall x_{i}, x_{j} \in \operatorname{Val}\left(X_{k}\right), x_{i} \neq x_{j}\right\}$, the probabilities of transitioning to specific states.

Therefore, a CTBN $\mathcal{N}$ over $\mathbf{X}$ can be equivalently described by a graph $\mathcal{G}$ together with the corresponding sets of parameters

$$
\mathbf{q}=\left\{\mathbf{q}_{X_{k} \mid \mathbf{u}}: \forall X_{k} \in \mathbf{X}, x_{i} \in \operatorname{Val}\left(X_{k}\right), \mathbf{u} \in \operatorname{Val}(\mathbf{U})\right\}
$$

and

$$
\boldsymbol{\Theta}=\left\{\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}: \forall X_{k} \in \mathbf{X}, x_{i} \in \operatorname{Val}\left(X_{k}\right), \mathbf{u} \in \operatorname{Val}(\mathbf{U})\right\}
$$

We assume that only one variable in the CTBN can change state at any specific instant; and that its transition dynamics are specified by its parents via the CIM, while being independent of all other variables given its Markov Blanket. ${ }^{4}$

Figure 1 shows a CTBN which models the effect that eating (Eating?) has on the content of the stomach (Full Stomach?) of an individual. Furthermore, the content of the stomach has an effect on whether the individual is hungry or not (Hungry?), which is turn has an effect on the individual to start eating (Eating?).

The CTBN contains a cycle,

$$
\text { Eating? } \rightarrow \text { Full Stomach? } \rightarrow \text { Hungry? } \rightarrow \text { Eating?, }
$$

which implies that whether a person is hungry or not (Hungry?) depends on whether the person's stomach is full or not (Full Stomach?), which depends on whether the person is eating or not (Eating?), which in turn depends on whether the person is hungry or not (Hungry?).

[^0]
[^0]:    ${ }^{3}$ For simplicity of notation, and without loss of generality, we omit the $k$ subscript from $m$ that implies that each $X_{k}$ may have a different domain.
    ${ }^{4}$ The definition of Markov blankets in CTBNs is the same as in BNs: a Markov blanket comprises the parents, the children and the spouses of the target node; and it graphically separates the target node from the rest of the network.

![img-0.jpeg](img-0.jpeg)

Figure 1: The Eating?, Full Stomach?, Hungry? CTBN.

Therefore, the CTBN consists of three nodes, that is, Eating?, Full Stomach? and Hungry?, associated with three binary random variables taking value on the sets $\operatorname{Val}($ Eating? $)=\operatorname{Val}($ Full Stomach? $)=\operatorname{Val}($ Hungry? $)$ $=\{n o$, yes $\}$.

The CIM for Eating? shown in Figure 1 means that we expect that a person who is hungry (Hungry? $=$ yes) and not eating (Eating? $=n o$ ), to begin eating, on average, in $1 / 2$ hours ( -2 in the filled cell), while we expect a person who is not hungry (Hungry? $=n o$ ) and who is eating (Eating? $=$ yes), on average, to stop eating in $1 / 10$ hours ( -10 in the filled cell), that is, in 6 minutes. ${ }^{5}$

# 2.2. Structure Learning 

Let $\mathcal{D}=\left\{\sigma_{1}, \ldots, \sigma_{h}\right\}$ be a sample consisting of $h$ trajectories denoted as $\sigma_{j}=\left\{\left\langle t_{1}, X_{t_{1}}\right\rangle, \ldots,\left\langle T_{j}, X_{T_{j}}\right\rangle\right\}$, where $T_{j}$ represents the length of trajectory $\sigma_{j}$, that is, the number of transitions. For each pair $\left\langle t_{i}, X_{t_{i}}\right\rangle$, we denote the time of the $i$ th transition as $t_{i}$ and the variable that leaves its current state at that time as $X_{t_{i}}$.

Learning the structure of a CTBN from $\mathcal{D}$ can be cast as an optimization problem (Nodelman et al., 2003) in which we would like to find the graph $\mathcal{G}^{*}$ with the highest posterior log-probability given $\mathcal{D}$ :

$$
\ln \mathrm{P}(\mathcal{G} \mid \mathcal{D})=\ln \mathrm{P}(\mathcal{G})+\ln \mathrm{P}(\mathcal{D} \mid \mathcal{G})
$$

where $\mathrm{P}(\mathcal{G})$ is the prior distribution over the space of graphs spanning $\mathbf{X}$ and $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ is the marginal likelihood of the data given $\mathcal{G}$ averaged over all possible parameter sets.

[^0]
[^0]:    ${ }^{5}$ The CIMS for the other two nodes are available in Appendix A.

The prior $\mathrm{P}(\mathcal{G})$ is usually assumed to satisfy the structure modularity property (Friedman and Koller, 2000), so that it decomposes as

$$
\mathrm{P}(\mathcal{G})=\prod_{X_{k} \in \mathbf{X}} \mathrm{P}\left(P a\left(X_{k}\right)=\mathbf{U}\right)
$$

For simplicity, the literature often assumes a uniform prior, that is, $\mathrm{P}(\mathcal{G}) \propto 1$.
The marginal likelihood $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ depends on the parameter prior $\mathrm{P}(\mathbf{q}, \boldsymbol{\Theta} \mid \mathcal{G})$, which is usually assumed to satisfy the global parameter independence, the local parameter independence and the parameter modularity properties (Heckerman et al., 1995) outlined below.

- Global parameter independence: the parameters $\mathbf{q}_{X_{k} \mid \mathbf{U}}$ and $\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}$ associated with each variable $X_{k}$ in a graph $\mathcal{G}$ are independent:

$$
\mathrm{P}(\mathbf{q}, \boldsymbol{\Theta} \mid \mathcal{G})=\prod_{X_{k} \in \mathbf{X}} \mathrm{P}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}, \boldsymbol{\theta}_{X_{k} \mid \mathbf{U}} \mid \mathcal{G}\right)
$$

- Local parameter independence: for each variable $X_{k}$, the parameters associated with each configuration $\mathbf{u}$ of parent set $\mathbf{U}$ are independent:

$$
\mathrm{P}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}, \boldsymbol{\theta}_{X_{k} \mid \mathbf{U}} \mid \mathcal{G}\right)=\prod_{\mathbf{u} \in \operatorname{Val}(\mathbf{U})} \prod_{x_{i} \in \operatorname{Val}\left(X_{k}\right)} \mathrm{P}\left(\mathbf{q}_{x_{i} \mid \mathbf{u}}, \boldsymbol{\theta}_{x_{i} \mid \mathbf{u}} \mid \mathcal{G}\right)
$$

- Parameter modularity: if variable $X_{k}$ has the same parent set in two distinct graphs $\mathcal{G}$ and $\mathcal{G}^{\prime}$, then the prior probability for the parameters associated with $X_{k}$ should also be the same:

$$
\mathrm{P}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}, \boldsymbol{\theta}_{X_{k} \mid \mathbf{U}} \mid \mathcal{G}\right)=\mathrm{P}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}, \boldsymbol{\theta}_{X_{k} \mid \mathbf{U}} \mid \mathcal{G}^{\prime}\right)
$$

In the context of CTBNs, we assume that the priors over the waiting times and over the transition probabilities are independent as well:

$$
\mathrm{P}(\mathbf{q}, \boldsymbol{\Theta} \mid \mathcal{G})=\mathrm{P}(\mathbf{q} \mid \mathcal{G}) \mathrm{P}(\boldsymbol{\Theta} \mid \mathcal{G})
$$

Nodelman et al. (2003) suggested conjugate priors for both $\mathbf{q}$ and $\boldsymbol{\Theta}$ in the form of

$$
\begin{aligned}
& \mathrm{P}\left(\mathbf{q}_{x_{i} \mid \mathbf{u}}\right) \sim \operatorname{Gamma}\left(\alpha_{x_{i} \mid \mathbf{u}}, \tau_{x_{i} \mid \mathbf{u}}\right) \\
& \mathrm{P}\left(\boldsymbol{\theta}_{x_{i} \mid \mathbf{u}}\right) \sim \operatorname{Dir}\left(\alpha_{x_{i} x_{1} \mid \mathbf{u}}, \ldots, \alpha_{x_{i} x_{m} \mid \mathbf{u}}\right)
\end{aligned}
$$

where $\alpha_{x_{i} \mid \mathbf{u}}, \tau_{x_{i} \mid \mathbf{u}}, \alpha_{x_{i} x_{1} \mid \mathbf{u}}, \ldots, \alpha_{x_{i} x_{m} \mid \mathbf{u}}$ are the priors' hyperparameters.
In particular, for any $X_{k} \mid \mathbf{U}=\mathbf{u}, \alpha_{x_{i} \mid \mathbf{u}}$ and $\alpha_{x_{i} x_{j} \mid \mathbf{u}}$ represent the pseudocounts for the number of transitions from state $x_{i}$ to state $x_{j}$; and $\tau_{x_{i} \mid \mathbf{u}}$ represents the imaginary amount of time spent in each state $x_{i}$ before any data is observed. Note that $\alpha_{x_{i} \mid \mathbf{u}}$ is inversely proportional to the number of joint

states of the parents of $X_{i}$. After conditioning on the dataset $\mathcal{D}$, we obtain the following posterior distributions:

$$
\begin{aligned}
& \mathrm{P}\left(\mathbf{q}_{x_{i} \mid \mathbf{u}} \mid \mathcal{D}\right) \sim \operatorname{Gamma}\left(\alpha_{x_{i} \mid \mathbf{u}}+M_{x_{i} \mid \mathbf{u}}, \tau_{x_{i} \mid \mathbf{u}}+T_{x_{i} \mid \mathbf{u}}\right) \\
& \mathrm{P}\left(\boldsymbol{\theta}_{x_{i} \mid \mathbf{u}} \mid \mathcal{D}\right) \sim \operatorname{Dir}\left(\alpha_{x_{i} x_{1} \mid \mathbf{u}}+M_{x_{i} x_{1} \mid \mathbf{u}}, \ldots, \alpha_{x_{i} x_{m} \mid \mathbf{u}}+M_{x_{i} x_{m} \mid \mathbf{u}}\right)
\end{aligned}
$$

where $T_{x_{i} \mid \mathbf{u}}$ and $M_{x_{i} x_{j} \mid \mathbf{u}}$ are the sufficient statistics of the CTBN.
In particular, $T_{x_{i} \mid \mathbf{u}}$ is the amount of time spent by $X_{k}$ in the state $x_{i}$ and $M_{x_{i} x_{j} \mid \mathbf{u}}$ is the number of times that $X_{k}$ transitions from the state $x_{i}$ to the state $x_{j}$, given $\mathbf{U}=\mathbf{u} .^{6}$

The marginal likelihood $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ arising from these posteriors can be written as

$$
\mathrm{P}(\mathcal{D} \mid \mathcal{G})=\prod_{X_{k} \in \mathbf{X}} \operatorname{ML}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right) \operatorname{ML}\left(\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)
$$

due to (3) and (6). $\operatorname{ML}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)$ is the marginal likelihood of $\mathbf{q}_{X_{k} \mid \mathbf{U}}$,

$$
\operatorname{ML}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)=\prod_{\mathbf{u} \in \operatorname{Val}(\mathbf{U})} \prod_{x_{i} \in \operatorname{Val}\left(X_{k}\right)} \frac{\Gamma\left(\alpha_{x_{i} \mid \mathbf{u}}+M_{x_{i} \mid \mathbf{u}}+1\right)\left(\tau_{x_{i} \mid \mathbf{u}}\right)^{\alpha_{x_{i} \mid \mathbf{u}}+1}}{\Gamma\left(\alpha_{x_{i} \mid \mathbf{u}}+1\right)\left(\tau_{x_{i} \mid \mathbf{u}}+T_{x_{i} \mid \mathbf{u}}\right)^{\alpha_{x_{i} \mid \mathbf{u}}+M_{x_{i} \mid \mathbf{u}}+1}}
$$

and $\operatorname{ML}\left(\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)$ is the marginal likelihood of $\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}$,

$$
\operatorname{ML}\left(\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)=\prod_{\mathbf{u} \in \operatorname{Val}(\mathbf{U})} \prod_{x_{i} \in \operatorname{Val}\left(X_{k}\right)} \frac{\Gamma\left(\alpha_{x_{i} \mid \mathbf{u}}\right)}{\Gamma\left(\alpha_{x_{i} \mid \mathbf{u}}+M_{x_{i} \mid \mathbf{u}}\right)} \prod_{x_{j} \in \operatorname{Val}\left(X_{k}\right)} \frac{\Gamma\left(\alpha_{x_{i} x_{j} \mid \mathbf{u}}+M_{x_{i} x_{j} \mid \mathbf{u}}\right)}{\Gamma\left(\alpha_{x_{i} x_{j} \mid \mathbf{u}}\right)}
$$

The resulting $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ is the Bayesian-Dirichlet equivalent (BDe) metric for CTBNs (Nodelman, 2007) based on the priors (7) and (8), which satisfies assumptions (3), (4), and (5) by construction.

The posterior in (1) can then be written in closed form as

$$
\mathrm{P}(\mathcal{G} \mid \mathcal{D})=\sum_{X_{k} \in \mathbf{X}} \log \mathrm{P}\left(P a\left(X_{k}\right)=\mathbf{U}\right)+\log \operatorname{ML}\left(\mathbf{q}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)+\log \operatorname{ML}\left(\boldsymbol{\theta}_{X_{k} \mid \mathbf{U}}: \mathcal{D}\right)
$$

assuming that (2) is satisfied. Since $\mathcal{G}$ does not have acyclicity constraints in a CTBN, it is possible to maximize (14) by independently scoring the possible parent sets of each $X_{k}$. Therefore, if we bound the maximum number of parents we can find the optimal $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$ in polynomial time either by enumerating all possible parent sets or by using hill-climbing to add, delete or reverse arcs (Nodelman et al., 2003). The author didn't give a proper name to this algorithm. However we decided to call it $\mathbf{C}$ ontinous-Time $\mathbf{S e a r c h}$ and $\mathbf{S c o r e}$ (CTSS).

[^0]
[^0]:    ${ }^{6}$ The number of times $X_{k}$ leaves the state $x_{i}$ when $\mathbf{U}=\mathbf{u}$ is $M_{x_{i} \mid \mathbf{u}}=\sum_{x_{j} \neq x_{i}} M_{x_{i} x_{j} \mid \mathbf{u}}$.

# 3. A Constraint-Based Algorithm for Structure Learning 

Learning the structure of a BN is a problem that is well explored in the literature. Several approaches have been proposed spanning score-based, constraint-based and hybrid algorithms; recent reviews are available from Scutari et al. (2019); Scanagatta et al. (2019). Score-based algorithms find the BN structure that maximizes a given score function, while constraint-based algorithms use statistical tests to learn conditional independence relationships (called constraints) from the data and infer the presence or absence of particular arcs. Hybrid algorithms combine aspects of both score-based and constraintbased algorithms.

On the other hand, the only structure learning algorithm proposed for CTBNs is the CTSS algorithm from Nodelman et al. (2003) we described in the previous section: to the best of our knowledge no constraint-based algorithm exists in the literature. It is worthwhile to note that CTBNs are a special case of the local independence model (Didelez, 2008, 2012; Meek, 2014) for which a general structure learning algorithm has been made available. In particular, (Mogensen et al., 2018) proposed a structure learning algorithm for local independence graphs. In their work, the authors studied independence models induced by directed graphs (DGs) by formalizing the properties of abstract graphoids that ensure that the global Markov property holds for a given directed graph. Mogensen et al. (2018) applied their theoretical arguments to the Ito diffusion as well as the event process, which are both related to CTBNs. Therefore, the algorithm we propose here can be considered as an instance of that presented by Mogensen et al. (2018), even if we independently formulated and developed our structure learning algorithm that is specifically designed for CTBNs. After a brief introduction to constraint-based algorithms for BNs, we propose such an algorithm for CTBNs.

### 3.1. Constraint-Based Algorithms for BNs

Constraint-based algorithms for BN structure learning originate from the Inductive Causation (IC) algorithm from Pearl and Verma (1991) for learning causal networks. IC starts (step 1) by finding pairs of nodes connected by an undirected arc as those are not independent given any other subset of variables. The second step (step 2) identifies the v-structures $X_{i} \rightarrow X_{k} \leftarrow X_{j}$ among all pairs $X_{i}$ and $X_{j}$ of non-adjacent nodes which share a common neighbour $X_{k}$. Finally, step 3 and 4 of IC identify compelled arcs and orient them to build the completed partially oriented DAG (CPDAG) that describes the equivalence class the BN falls into.

However, steps 1 and 2 of the IC algorithm are computationally unfeasible for non-trivial problems due to the exponential number of conditional independence relationships to be tested.

The $P C$ algorithm, which is briefly illustrated in Algorithm 1, was the first proposal addressing this issue; its modern incarnation is described in Colombo and Maathuis (2014), and we will use it as the foundation for CTBN structure learning below. PC starts from a fully-connected undirected graph. Then, for

# Algorithm 1 PC Algorithm 

1. Form the complete undirected graph $\mathcal{G}$ on the vertex set $\mathbf{X}$.
2. For each pair of variables $X_{i}, X_{j} \in \mathbf{X}$, consider all the possible separating set from the smallest $\left(\mathbf{S}_{X_{i} X_{j}}=\varnothing\right)$ to the largest $\left(\mathbf{S}_{X_{i} X_{j}}=\mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}\right)$. If there isn't any set $\mathbf{S}_{X_{i} X_{j}}$ such that $X_{i} \Perp X_{j} \mid \mathbf{S}_{X_{i} X_{j}}$ then the edge $X_{i}-X_{j}$ is removed from $\mathcal{G}$.
3. For each triple $X_{i}, X_{j}, X_{k} \in \mathcal{G}$ such that $X_{i}-X_{j}, X_{j}-X_{k}$, and $X_{i}, X_{j}$ are not connected, orient the edges into $X_{i} \rightarrow X_{j} \leftarrow X_{k}$ if and only if $X_{j} \notin \mathbf{S}_{X_{i} X_{j}}$ for every $\mathbf{S}_{X_{i} X_{j}}$ that makes $X_{i}$ and $X_{k}$ independent.
4. The algorithm identifies the compelled directed arcs by iteratively applying the following two rules:
(a) if $X_{i}$ is adjacent to $X_{j}$ and there is a strictly directed path from $X_{i}$ to $X_{j}$ then replace $X_{i}-X_{j}$ with $X_{i} \rightarrow X_{j}$ (to avoid introducing cycles);
(b) if $X_{i}$ and $X_{j}$ are not adjacent but $X_{i} \rightarrow X_{k}$ and $X_{k}-X_{j}$, then replace the latter with $X_{k} \rightarrow X_{j}$ (to avoid introducing new vstructures).
5. Return the resulting CPDAG $\mathcal{G}$.
each pair of variables $X_{i}, X_{j}$ it proceeds by gradually increasing the cardinality of the set of conditioning nodes $\mathbf{S}_{X_{i} X_{j}}$ until $X_{i}$ and $X_{j}$ are found to be independent or $\mathbf{S}_{X_{i} X_{j}}=\mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}$. The remaining steps are identical to those of IC.

Neither IC nor PC (or other constraint-based algorithms, for that matter) require a specific test statistic to test conditional independence, making them independent from the distributional assumptions we make on the data.

### 3.2. The CTPC Structure Learning Algorithm

CTBNs differ from BNs in three fundamental ways: BNs do not model time, while CTBNs do; BNs are based on DAGs, while CTBNs allow cycles; and BNs model the dependence of a node on its parents using a conditional probability distribution, while CTBNs model it using a CIM. These differences make structure learning a simpler problem for CTBNs than it is for BNs.

Firstly, learning arc directions is an issue in BNs but not in CTBNs, where arcs are required to follow the arrow of time. Unlike BNs, which can be grouped into equivalence classes that are probabilistically indistinguishable, each CTBN has a unique minimal graphical representation (Nodelman et al., 2003). For instance, let a CTBN $\mathcal{N}$ have graph $\mathcal{G}=\{X \rightarrow Y\}$ : unless trivially $X$ and $Y$ are marginally independent, $\mathcal{G}$ cannot generate the same transition probabilities as any CTBN $\mathcal{N}^{\prime}$ with graph $\mathcal{G}^{\prime}=\{X \leftarrow Y\}$.

Secondly, in CTBNs we can learn each parent set $P a\left(X_{k}\right)$ in isolation, thus making any structure learning algorithm embarrassingly parallel. Acyclicity imposes a global constraint on $\mathcal{G}$ that makes it impossible to do the same in BNs.

Thirdly, each variable $X_{k}$ is modelled conditional on a given function of its parent set $P a\left(X_{k}\right)$ : a conditional probability table for (discrete) BNs, a CIM for CTBNs.

However, a CIM $\mathbf{Q}_{X_{k} \mid \mathbf{U}}$ describes the temporal evolution of the state of variable $X_{k}$ conditionally on the state of its parent set $\mathbf{U}$. Hence we can not test conditional independence by using classical test statistics like the mutual information or Pearson's $\chi^{2}$ that assume observations are independent (Koller and Friedman, 2009). Instead we need to adapt our definition of conditional independence to CTBNs in order to design a constraint-based algorithm for structure learning.

Definition 2. Conditional Independence in a CTBN
Let $\mathcal{N}$ be a CTBN with graph $\mathcal{G}$ over a set of variables $\mathbf{X}$. We say that $X_{i}$ is conditionally independent from $X_{j}$ given $\mathbf{S}_{X_{i} X_{j}} \subseteq \mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}$ if

$$
\mathbf{Q}_{X_{i} \mid x, \mathbf{s}}=\mathbf{Q}_{X_{i} \mid \mathbf{s}} \quad \forall x \in \operatorname{Val}\left(X_{j}\right), \forall \mathbf{s} \in \operatorname{Val}\left(\mathbf{S}_{X_{i} X_{j}}\right)
$$

If $\mathbf{S}_{X_{i} X_{j}}=\varnothing$, then $X_{i}$ is said to be marginally independent from $X_{j}$.
It is important to note that Definition 2 is not symmetric: it is perfectly possible for $X_{i}$ to be conditionally or marginally independent from $X_{j}$, while $X_{j}$ is not conditionally or marginally independent from $X_{i}$. This discrepancy is, however, not a practical or theoretical concern because arcs are already non-symmetric (they must follow the direction of time) and therefore we only test whether $X_{i}$ depends on $X_{j}$ if $X_{j}$ precedes $X_{i}$ and not the other way round.

As for the test statistics, we can test for conditional independence using $\mathbf{q}_{X_{k} \mid \mathbf{u}}$ (the waiting times) and, if we do not reject the null hypothesis of conditional independence, we can perform a further test using $\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}$ (the transitions): $\mathbf{q}_{X_{k} \mid \mathbf{u}}$ and $\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}$ have been defined to be independent in Section 2.1 so they can be tested separately.

Note that conditional independence can be established by testing only the waiting times $\mathbf{q}_{X_{k} \mid \mathbf{u}}$ if the CTBN contains only binary variables because the transition is deterministic for a binary node. However, testing for conditional independence involves both waiting times and transitions in the general case in which variables can take more than two values.

Since we consider that rates are the most important characteristic to assess in a stochastic process, we decide without loss of generality to test $\mathbf{q}_{X_{k} \mid \mathbf{u}}$ first, and then $\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}$.

For $\mathbf{q}_{X_{k} \mid \mathbf{u}}$, we define the null time to transition hypothesis as follows.
Definition 3. Null Time To Transition Hypothesis
Given $X_{i}, X_{j}$ and the conditioning set $\mathbf{S}_{X_{i} X_{j}} \subseteq \mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}$, the null time to transition hypothesis of $X_{j}$ over $X_{i}$ is

$$
q_{x \mid y, \mathbf{s}}=q_{x \mid \mathbf{s}} \quad \forall x \in \operatorname{Val}\left(X_{i}\right), \forall y \in \operatorname{Val}\left(X_{j}\right), \forall \mathbf{s} \in \operatorname{Val}\left(\mathbf{S}_{X_{i} X_{j}}\right)
$$

For $\boldsymbol{\theta}_{X_{k} \mid \mathbf{u}}$, we define the null state-to-state transition hypothesis as follows.
Definition 4. Null State-To-State Transition Hypothesis
Given $X_{i}, X_{j}$ and the conditioning set $\mathbf{S}_{X_{i} X_{j}} \subseteq \mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}$, the null state-to-state transition hypothesis of $X_{j}$ over $X_{i}$ is

$$
\theta_{x \cdot \mid y, \mathbf{s}}=\theta_{x \cdot \mid \mathbf{s}} \quad \forall x \in \operatorname{Val}\left(X_{i}\right), \forall y \in \operatorname{Val}\left(X_{j}\right), \forall \mathbf{s} \in \operatorname{Val}\left(\mathbf{S}_{X_{i} X_{j}}\right)
$$

where we let $\theta_{x \cdot \mid y, \mathbf{s}}$ be off diagonal elements of matrix $\mathbf{Q}_{X_{i} \mid y, \mathbf{s}}$ divided by $q_{x \mid y, \mathbf{s}}$ corresponding to assignment $X_{i}=x$. It is worthwhile to mention that equality $\theta_{x \mid y, \mathbf{s}}=\theta_{x \cdot \mid \mathbf{s}}$ has to be understood in terms of corresponding components of vectors $\theta_{x \cdot \mid y, \mathbf{s}}$ and $\theta_{x \cdot \mid \mathbf{s}}$.

Definition 3 characterizes conditional independence for the times to transition for variable $X_{i}$ when adding (or not) $X_{j}$ to its parents; Definition 4 characterizes conditional independence for the transitions of $X_{i}$ when adding (or not) $X_{j}$ to its parents.

To test the null time to transition hypothesis, we use the $F$ test to compare two exponential distributions from Lee and Wang (2003). In the case of CTBNs, the test statistic and the degrees of freedom take form

$$
F_{r_{1}, r_{2}}=\frac{q_{x \mid \mathbf{s}}}{q_{x \mid y, \mathbf{s}}}, \quad \text { with } \quad r_{1}=\sum_{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)} M_{x x^{\prime} \mid y, \mathbf{s}}, \quad r_{2}=\sum_{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)} M_{x x^{\prime} \mid \mathbf{s}}
$$

To test the null state-to-state transition hypothesis, we investigated the use of the two-sample chi-square and Kolmogorov-Smirnov tests (Mitchell, 1971). For CTBNs the former takes form:

$$
\begin{aligned}
& \chi^{2}=\sum_{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)} \frac{\left(K \cdot M_{x x^{\prime} \mid y, \mathbf{s}}-L \cdot M_{x x^{\prime} \mid \mathbf{s}}\right)^{2}}{M_{x x^{\prime} \mid y, \mathbf{s}}+M_{x x^{\prime} \mid \mathbf{s}}} \\
& K=\sqrt{\frac{\sum_{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)} M_{x x^{\prime} \mid \mathbf{s}}}{\sum_{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)} M_{x x^{\prime} \mid y, \mathbf{s}}}}, L=\frac{1}{K}
\end{aligned}
$$

and is asymptotically distributed as a $\chi_{\left|\operatorname{Val}\left(X_{i}\right)\right|-1}^{2}$. The latter is defined as

$$
D_{r_{1}, r_{2}}=\sup _{x^{\prime} \in \operatorname{Val}\left(X_{i}\right)}\left|\Theta_{x x^{\prime} \mid \mathbf{s}}-\Theta_{x x^{\prime} \mid y, \mathbf{s}}\right|, \quad \Theta_{x x^{\prime}}=\sum_{\substack{x^{\prime \prime} \in \operatorname{Val}\left(X_{i}\right) \\ x^{\prime \prime} \leq x^{\prime}}} \theta_{x x^{\prime \prime}}
$$

After characterising conditional independence, we can now introduce our constraint-based algorithm for structure learning in CTBNs. The algorithm, which we call Continuous-Time PC (CTPC), is shown in Algorithm 2.

The first step is the same as the corresponding step of the PC algorithm in that it determines the same pattern of conditional independence tests. However,

```
Algorithm 2 Continuous-time PC Algorithm
    Form the complete directed graph \(\mathcal{G}\) on the vertex set \(\mathbf{X}\).
    For each variable \(X_{i} \in \mathbf{X}\):
        2.1 Set \(\mathbf{U}=\left\{X_{j} \in \mathbf{X}: X_{j} \rightarrow X_{i}\right\}\), the current parent set.
        2.2 For increasing values \(b=0, \ldots, n\), until \(b=|\mathbf{U}|\):
            2.2.1 For each \(X_{j} \in \mathbf{U}\), test \(X_{i} \Perp X_{j} \mid \mathbf{S}_{X_{i} X_{j}}\) for all possible subsets
                of size \(b\) of \(\mathbf{U} \backslash X_{j}\).
            2.2.2 As soon as \(X_{i} \Perp X_{j} \mid \mathbf{S}_{X_{i} X_{j}}\) for some \(\mathbf{S}_{X_{i} X_{j}}, \operatorname{remove} X_{j} \rightarrow X_{i}\)
                from \(\mathcal{G}\) and \(X_{j}\) from \(\mathbf{U}\).
    Return directed graph \(\mathcal{G}\).
```

as discussed above, the hypotheses being tested are the null time to transition hypothesis and the null state-to-state transition hypothesis.

The second step of CTPC differs from that in the PC algorithm. Since independence relationships are not symmetric in CTBNs, we can find the graph $\mathcal{G}$ of the CTBN without indentifying and then refining a CPDAG representing an equivalence class. Therefore, steps 3 and 4 of the PC algorithm are not needed in the case of CTBNs.

CTPC starts by initializing the complete directed graph $\mathcal{G}$ without loops (step 1). Note that while loops (that is, arcs like $X_{i} \rightarrow X_{i}$ ) are not included, cycles of length two (that is, $X_{i} \rightarrow X_{j}$ and $X_{j} \rightarrow X_{i}$ ) are, as well as cycles of length tree or more.

Step 2 iterates over the $X_{i}$ to identify their parents $\mathbf{U}$. This is achieved in step 2.2.1 by first testing for unconditional independence, then by testing for conditional independence gradually increasing the cardinality $b$ of the considered separating sets.

Each time Algorithm 2 concludes that $X_{i}$ is independent from $X_{j}$ given some separating set, we remove the arc from node $X_{j}$ to node $X_{i}$ in step 2.2.2. At the same time, we also remove $X_{j}$ from the current parent set $\mathbf{U}$. The iteration for $X_{i}, X_{j}$ terminates either when $X_{j}$ is found to be independent from $X_{i}$ or when there are no more larger separating sets to try because $b=|U|$; and the iteration over $X_{i}$ terminates when there are no more $X_{j}$ to test.

CTPC checks the null time to transition hypothesis (Definition 3) by applying the test for two exponential means in (16). On the contrary, the null state-to-state transition hypothesis (Definition 4) can be tested using two different tests: the two sample chi-square test in (18) and the two sample Kolmogorov-Smirnov test in (19). We call these two options $\mathrm{CTPC}_{\chi^{2}}$ and $\mathrm{CTPC}_{\mathrm{KS}}$, respectively.

The proposed algorithm is able to recover the true graph under the standard assumptions of the PC algorithm: i) the faithfulness assumption; ii) the database consists of a set of independent and identically distributed cases; iii) the database of cases is infinitely large; $i v$ ) the causal sufficiency assumption, that is, no hidden (latent) variables are involved; $v$ ) the statistical tests make

no type-I or type-II errors (Kjærulff and Madsen, 2013).
CTPC can be also extended to account for hidden variables. In the case of score-based structure learning, Nodelman et al. (2012b) used the Structural Expectation Maximization algorithm for this purpose, while Linzner et al. (2019) developed a novel gradient-based approach to structure learning which makes it possible to learn structures of previously inaccessible sizes. However, to the best of our knowledge no constraint-based algorithm for learning the structure of CTBNs with latent variables has been presented in the literature. The results presented and discussed in Mogensen et al. (2018) may allow the CTPC to be extended to handle hidden variables.

# 3.3. CTPC computational complexity 

The computational complexity of estimating the network structure of a CTBN from data using the CTPC algorithm depends on the following quantities: the number of nodes, the number of parents of each node and the number of transitions.

In Appendix B we presented the computational complexity of learning the stucture of a CTBN using CTPC summarized in the following table:


where $n$ is the number of nodes, $\gamma$ is the maximum node cardinality present in the network, $\psi$ is the number of transitions occurring in the dataset and $\rho$ is the maximum parent set size presente in the network.

Nodelman (2007) states that the CTSS algorithm for CTBNs is polynomial in the number of variables $(n)$ and in the size of the dataset $(\psi)$ when a maximum number of parents is given. The CTPC algorithm is also polynomial in the number of nodes and the size of the dataset in the general case. However, in the CTPC algorithm it is natural to bound the size of the separating sets in the conditional independence tests but not the size of the parent sets because CTPC does not operate on parent sets explicitly. Bounding the size of the separating sets can reduce the execution time, but has the drawback of producing denser networks because it potentially makes some independence relationships impossible to establish.

## 4. Numerical Experiments

We now assess the performance of CTPC against that of the CTSS algorithm from Nodelman et al. (2003) using synthetic data. In particular, we generate random CTBNs as the combinations of directed graphs and the associated CIMs; and we generate random trajectories from each CTBN.

Note that we only generate connected networks, hence absolute density ${ }^{7}$ is bounded below by $n-1$.

We measure the performance of the learning algorithms using the F1 score over the arcs, which is defined as

$$
F_{1}=2 \cdot \frac{\text { precision } \times \text { recall }}{\text { precision }+ \text { recall }}
$$

Since there is no score equivalence in CTBNs, nor are networks constrained to be acyclic, comparing graphs is equivalent to evaluating a binary classification problem.

Furthermore, we compare the two algorithms by their scaled difference in Bayesian Information Criterion (BIC), the latter defined as in Koller and Friedman (2009):

$$
\Delta B I C \%=\frac{B I C_{C T S S}-B I C_{C T C P}}{B I C_{C T S S}} \cdot 100
$$

with

$$
B I C=\ln (\hat{L})-\frac{1}{2} k \ln (\psi)
$$

and where $k$ is the number of parameters in the learned CTBN model, $\psi$ is the number of transitions while $\hat{L}$ is the corresponding data likelihood.

After a first set of experiments (Appendix C) we found that the $\mathrm{CTPC}_{\chi^{2}}$ performs marginally better than $\mathrm{CTPC}_{K S}$. Then we set up a full factorial experimental design over different numbers of nodes $n=\{5,10,15,20\}$, network densities ${ }^{8}\{0.1,0.2,0.3,0.4\}$, number of states for the nodes $\left|\operatorname{Val}\left(X_{i}\right)\right|=\{2,3,4\}$. For each network, we generate 300 trajectories that last on average 100 units of time each. We perform 10 replicates for each simulation configuration except for the networks with 20 ternary nodes and network density equal to 0.4 , for which we only perform 3 replicates. We did not consider quaternary networks with 20 nodes because it is unfeasible to learn them on the available hardware.

We perform the experiments using new, optimized implementations of the CTSS algorithm and of the $\mathrm{CTPC}_{\chi^{2}}$ algorithm ${ }^{9}$ that can handle larger networks and that can learn the parent set of each node in parallel. Those implementations are parallelized but use more memory, requiring a more powerful machine with 8 cores and 64 GB of memory.

The results of our simulation study are summarized in Figure 2, in Figure 3, in Figure 4 and in Figure 5.

[^0]
[^0]:    ${ }^{7}$ absolute density $=$ Number of edges in a network
    ${ }^{8}$ network density $=\frac{\text { absolute density }}{n \cdot(n-1)}$
    ${ }^{9}$ The new implementations provided by Filippo Martini and Luca Moretti are available at https://github.com/madlabunimib/PyCTBN.

![img-1.jpeg](img-1.jpeg)

Figure 2: Each of the plots on this figure represents the average F1 score and the standard deviation of the constraint-based algorithm and the CTSS one, against the number of nodes for a specific combination of network density and node cardinality.
![img-2.jpeg](img-2.jpeg)

Figure 3: Each of the plots on this figure represents the average $\Delta B I C \%$ and the standard deviation against the number of nodes for a specific combination of network density and node cardinality.

Figure 2 shows that the CTSS algorithm is the best choice for networks consisting of binary nodes. However, the $\mathrm{CTPC}_{\chi^{2}}$ and the CTSS perform similarly for networks with ternary and quaternary nodes. Furthermore, the performance of the CTPC algorithm, if compared with the CTSS one, seems to improve with the increase in the number of nodes and in the network density.

We can see from Figure 2 and Figure 4 that the execution time increases when the network density increases, and that both algorithms perform poorly for dense networks. This behaviour may be attributed to the method used to generate the trajectories that doesn't increase their size when the network density increases.

Figure 3 shows something different. Indeed, if we consider the $\Delta B I C \%$ as an evaluation metric, we note the CTSS algorithm to be at least as good as the CTPC algorithm in almost every experiment.

Figure 5 shows an important difference between the two algorithms; the CTSS algorithm achieves a precision of 1 in almost all simulations. However, the constraint-based algorithm has a better recall for the networks with ternary and quaternary nodes ${ }^{10}$.

[^0]![img-3.jpeg](img-3.jpeg)

Figure 4: Each of the plots on this figure represents the average execution time in seconds and the standard deviation of the constraint-based algorithm and the CTSS one, against the number of nodes for a specific combination of network density and node cardinality.


[^0]:    ${ }^{10}$ The tables with all the results can be found in the Appendix D

![img-4.jpeg](img-4.jpeg)

Figure 5: Each of the plots on this figure represents the average Precision, Recall and their respective standard deviations of the constraint-based algorithm and the CTSS one, against the number of nodes for a specific combination of network density and node cardinality.

Until now, we tested the CTPC algorithm with small to medium networks consisting of up to 20 nodes. To evaluate the execution time of CTPC with larger networks, we combined up to 5 networks with 20 binary nodes and network density 0.1 . The results presented in Table 1 show that CTPC is able to learn networks with up to 100 nodes in a reasonable amount of time. It is important to note that the tested networks are scattered. ${ }^{11}$ It was also necessary to use a machine with 256 GB of memory to carry out the experiments. The huge memory requirement is closely related to our implementation. In fact, each process is independent and requires a copy of the dataset to be loaded into the ram.

[^0]
[^0]:    ${ }^{11}$ Networks composed by disjoint sub-networks that are collated together in such a way to maintain sparsity
    ${ }^{12}$ This value was estimated as it was not possible to perform the experiment with the amount of memory available to us.


Table 1: Execution time of the CTPC on big, sparse networks

# 5. Conclusions 

In this paper we introduced the first constraint-based algorithm for structure learning in CTBNs, which we called CTPC, comprising both a suitable set of statistics for testing conditional independence and a heuristic algorithm based on PC. We also derived the complexity of this new algorithm finding that it is similar to the CTSS one.

CTPC has better structural reconstruction accuracy, compared to the only CTSS algorithm previously available in the literature (Nodelman et al., 2003), when variables in the CTBN can assume more than two values. For binary variables, that CTSS algorithm performs well, but its performance rapidly degrades as variables are allowed to have increasingly more states. Simulation experiments also showed that the $\chi^{2}$ test for the null state-to-state transition hypothesis has a marginally better performance than the Kolmogorov-Smirnov test. However, if we compare the two algorithms in terms of BIC the CTSS is the best option in all the performed experiments. A major limitation of the proposed constraint-based algorithm is the computational cost which becomes problematic in domains with more than 20 variables. However, the the CTSS algorithm has the same limitation.

It would be important to validate the performance of CTPC on real-world data. Unfortunately, we are not aware of any suitable real-world data set where ground truth is available, and thus we were unable to pursue this line of investigation. Furthermore, we are planning additional numerical experiments to evaluate the impact of the type-I-error threshold for the tests to better understand how to calibrate constraint-based algorithms.

## Acknowledgement

The authors acknowledge the many helpful suggestions of anonymous referees which helped to improve the paper clarity and quality. The authors are indebted to all reviewers for providing extremely useful references to the specialized literature which could impact their future research activity.

# Appendices 

## A. CTBN Example: additional cims




Table 2: $Q_{\text {Full-Stomach } \mid \text { Eating }}$




Table 3: $Q_{\text {Hungry|Full-Stomach }}$

## B. CTPC computational complexity

To compute the time complexity of CTPC, first recall that:

- $\psi$ is the number of transitions occurring in the data set;
- $\mathbf{X}$ is the set of nodes of the CTBN;
- $n$ is the number of nodes of the CTBN;
- $X_{k} \in \mathbf{X}$ is the node associated with the $k-t h$ random variable;
- $\left|X_{k}\right|$ is the cardinality of the node $X_{k}$;
- $\gamma=\max \left(\left\{\left|X_{k}\right|: X_{k} \in \mathbf{X}\right\}\right)$ is the maximum node cardinality present in the network;
- $\operatorname{Pa}\left(X_{k}\right) \subset \mathbf{X}$ is the parent set of node $X_{k}$;
- $\left|\operatorname{Pa}\left(X_{k}\right)\right|$ is the size of the paret set $\operatorname{Pa}\left(X_{k}\right)$;
- $\rho=\max \left(\left\{\left|\operatorname{Pa}\left(X_{k}\right)\right|: X_{k} \in \mathbf{X}\right\}\right)$ it the maximum parent set size present in the network;
- $T, M$ : are the sets of sufficient statistics $T_{x_{i} \mid \mathbf{u}}$ and $M_{x_{i} x_{m} \mid \mathbf{u}}$ for a specific node and parent set.

The structure of the CTPC algorithm can be represented with a series of blocks nested within each other (Figure 6):

1. Compute the CIM: learn the CIM of a node from a data set given a separating set.
2. Test Independence: test the independence between two nodes given a separating set.
3. Learn the parent set (one node): learn the parent set of a node.
4. Learn the network's structure: learn the parent set for each node in the network.

We derive the complexity of the CTPC algorithm in a bottom-up fashion, that is, by using the complexity of the inner blocks to derive the complexity of the outer blocks.

# B.1. Compute the CIM 

This is the innermost box in Figure 6. The tasks requiring the largest number of operations, which determine the leading terms of the computational complexity, are the following:

- Computing the sufficient statistics $T$ and $M$ over the subset of the dataset containing the analyzed node and its parent set: $O((\rho+1) \cdot \psi)$.
- Computing the CIM Q, given the sufficient statistics $T$ and $M$. For this task we need to compute a matrix of dimension $\gamma^{2}$ for each combination of the parent set: $O\left(\gamma^{\rho+2}\right)$.

Overall, the time complexity of this box is $O((\rho+1) \cdot \psi)+\gamma^{\rho+2})$.

## B.1.1. Test Independence

For this box, we characterise separately the best case and the worst case computational complexity. Recall that we perform two tests to assess whether two variables are independent: one for the null time to transition hypothesis and one for the null state-to-state transition hypothesis. If at least one of these tests fails, we conclude that the two nodes are not independent.
![img-5.jpeg](img-5.jpeg)

Figure 6: Conceptual model of the CTPC algorithm.

- Best Case: when the first hypothesis test fails. The most complex operations are:
- The computation of the CIM: $O\left((\rho+1) \cdot \psi+\gamma^{\rho+2}\right)$.
- The computation of one test: $O(1)$.

Since the computational complexity of one test is $O(1)$ we can ignore it in the overall complexity of this case.

- Worst Case: when no hypothesis test fails. The most complex operations are:
- The computation of the CIM: $O\left((\rho+1) \cdot \psi+\gamma^{\rho+2}\right)$.
- Performing all the hypothesis tests, $\gamma$ t-tests (each with complexity $O(1))$ and $\gamma$ chi-square tests (each with complexity $O(\gamma)$ ) for each possible value of the parent set $\gamma^{\rho}: O\left(\gamma^{\rho+1}+\gamma^{\rho+2}\right)=O\left(\gamma^{\rho+2}\right)$.

These two operations are performed in sequence. It follows that to identify the overall complexity of this case it is sufficient to add the complexities of the two operations.

Therefore, the complexity of the independence test can be summarized as:


# B.2. Learn the parent set (one node) 

For this box of the algorithm, we distinguish three cases:

- Best Case: the target node has no parents, thus the most complex operation is:
- The independence test (worst case): $O\left(2 \cdot \gamma^{\rho+2}+(\rho+1) \cdot \psi\right)$.

If the node under analysis has no parents it follows that $\rho=0$ from the definition of $\rho$. We need to test all the possible parent set with size $1(\rho+1)$, hence we perform $n-1 \rightarrow O(n)$ tests for an overall complexity of $O\left(n \cdot\left(2 \cdot \gamma^{3}+2 \cdot \psi\right)\right)$.

- Worst case: all nodes are parents of the current node, thus the most complex operation is:
- The independence test (best case): $O\left((\rho+1) \cdot \tau+\gamma^{\rho+2}\right)$. The target node depends on all other nodes $(\rho=n-1)$ and therefore the first independence test always fail. The algorithm computes all potential parent sets, for an overall complexity of

$$
O\left(\sum_{r=1}^{n-1} \frac{(n-1)!}{r!\cdot(n-1-r)!} \cdot\left(\gamma^{r+2}+(r+1) \cdot \psi\right)\right)
$$

which simplifies to $O\left(2^{n} \cdot\left(\gamma^{n+1}+n \cdot \psi\right)\right)$ since

$$
O\left(\gamma^{r+2}+r \cdot \psi\right) \sim O\left(\gamma^{n}+n \cdot \psi\right)
$$

and

$$
\sum_{r=1}^{n-1} \frac{(n-1)!}{r!\cdot(n-1-r)!} \rightarrow O\left(2^{n}\right)
$$

- General case: The General case is similar to the worst case with one important difference: $\rho<n-1$ instead of $\rho=n-1$. The most complex operations are:
- Independence test (best case): $O\left((\rho+1) \cdot \psi+\gamma^{\rho+2}\right)$. All the tests until that conditional on the true parent set of size $\rho$ fail. Therefore, the algorithm evaluates all possible parent sets of size $\leq \rho+1$, resulting in the following complexity:

$$
O\left(\sum_{r=1}^{\rho+1} \frac{(n-1)!}{r!\cdot(n-1-r)!} \cdot\left(\gamma^{r+2}+(r+1) \cdot \psi\right)\right)
$$

Noting that:

$$
\begin{gathered}
O\left(\gamma^{r+2}+(r+1) \cdot \psi\right) \rightarrow O\left(\gamma^{\rho+3}+(\rho+2) \cdot \psi\right) \\
O\left(\sum_{r=1}^{\rho+1} \frac{(n-1)!}{r!\cdot(n-1-r)!}\right) \rightarrow O\left(\frac{n^{\rho+1}}{(\rho+1)!}\right)
\end{gathered}
$$

the computational complexity in (21) simplifies to:

$$
O\left(\frac{n^{\rho+1}}{(\rho+1)!} \cdot\left(\gamma^{\rho+3}+(\rho+2) \cdot \psi\right)\right)
$$

In conclusion, the complexity of the three cases can be summarized as follows:


# B.2.1. Learn the network's structure 

In Section B. 2 we presented the computational complexity of learning the parent set of a single node. In order to have the complexity of the CTPC algorithm we just need to multiply those equations by $n$. The computational complexity of the CTPC algorithm can be summarized as follows:


# C. Experiments: comparison between differet hypothesis tests 

We perform a simulation study using a full factorial experimental design over different numbers of nodes $n=\{5,10,15,20\}$, network densities $\{0.1,0.2,0.3\}$, number of states for the nodes $\left|\operatorname{Val}\left(X_{i}\right)\right|=\{2,3\}$ and different numbers of trajectories $h=\{100,200,300\}$. Each trajectory lasts on average for 100 units of time. We generate 10 replicates for each simulation configuration with $n<10$ and 3 replicates for configurations with $n \geqslant 10 .{ }^{13}$

Results are summarized in Table 4 (for the CTSS algorithm in Nodelman et al., 2003), Table 5 (for $\mathrm{CTPC}_{\chi^{2}}$ ) and Table 6 (for $\mathrm{CTPC}_{\mathrm{KS}}$ ). In the case of binary variables, the CTSS algorithm performs better than the proposed constraint-based algorithms for any combination of network density, number of trajectories and number of nodes. $\mathrm{CTPC}_{\chi^{2}}$ and $\mathrm{CTPC}_{\mathrm{KS}}$ have comparable performance, which is expected since in this case the two algorithms are identical (because the tests are identical, that is, we only test waiting times). However, $\mathrm{CTPC}_{\chi^{2}}$ and $\mathrm{CTPC}_{\mathrm{KS}}$ have better F1 scores than the CTSS algorithm for ternary variables.
$\mathrm{CTPC}_{\chi^{2}}$ appears to perform marginally better than $\mathrm{CTPC}_{\mathrm{KS}}$ when $n<20$, but the two algorithms are again comparable when $n=20$ and $h=300$. This suggests that $\mathrm{CTPC}_{\chi^{2}}$ is more sample-efficient than $\mathrm{CTPC}_{\mathrm{KS}}$ with respect to the number of trajectories.

However, $\mathrm{CTPC}_{\chi^{2}}$ and $\mathrm{CTPC}_{\mathrm{KS}}$ scale better than the available CTSS implementation for the algorithm from Nodelman et al. (2003), which exhausts the 24 GiB of memory allocated for the experiment and fails to complete the execution as shown in the last line of Table 4.

[^0]
[^0]:    ${ }^{13}$ We use the CTBN-RLE package (Shelton et al., 2010) for CTSS learning. We provide a Python implementation of CTPC, which is available at https://github.com/ AlessandroBregoli/ctbn_cba. CTBN-RLE uses the Bayesian Score with a Gamma prior for the parameters of the exponential distributions and with a Dirichlet prior for the transition probabilities. Hyperparameters are set to their default value, that is, $\tau=1$ for the Gamma prior and $\alpha=1$ for the Dirichlet prior.


Table 4: $\mathrm{F}_{1}$-score for the CTSS algorithm.


Table 5: $\mathrm{F}_{1}$-score for the $\mathrm{CTPC}_{\chi^{2}}$ algorithm.


Table 6: $\mathrm{F}_{1}$-score for the $\mathrm{PC}_{K S}$ CTBN algorithm.

# D. Experiment: full tables 


Table 7: $\mathrm{F}_{1}$-score for the CTSS algorithm.


Table 8: $\mathrm{F}_{1}$-score for the $\mathrm{CTPC}_{\mathrm{x}^{2}}$ algorithm.