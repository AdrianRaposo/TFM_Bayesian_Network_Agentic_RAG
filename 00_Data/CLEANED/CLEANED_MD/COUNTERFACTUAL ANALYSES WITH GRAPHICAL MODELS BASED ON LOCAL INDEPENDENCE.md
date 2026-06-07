# COUNTERFACTUAL ANALYSES WITH GRAPHICAL MODELS BASED ON LOCAL INDEPENDENCE ${ }^{1}$ 

By Kjetil Røysland<br>University of Oslo

We show that one can perform causal inference in a natural way for continuous-time scenarios using tools from stochastic analysis. This provides new alternatives to the positivity condition for inverse probability weighting. The probability distribution that would govern the frequency of observations in the counterfactual scenario can be characterized in terms of a so-called martingale problem. The counterfactual and factual probability distributions may be related through a likelihood ratio given by a stochastic differential equation. We can perform inference for counterfactual scenarios based on the original observations, re-weighted according to this likelihood ratio. This is possible if the solution of the stochastic differential equation is uniformly integrable, a property that can be determined by comparing the corresponding factual and counterfactual short-term predictions.

Local independence graphs are directed, possibly cyclic, graphs that represent short-term prediction among sufficiently autonomous stochastic processes. We show through an example that these graphs can be used to identify and provide consistent estimators for counterfactual parameters in continuous time. This is analogous to how Judea Pearl uses graphical information to identify causal effects in finite state Bayesian networks.

1. Introduction. While randomized controlled trials are the gold standard for determining the effects of public health interventions or medical treatments, there are many situations where such trials are unethical, and it is tempting to turn to registry data or observational studies for quality assessment of treatments. However, data from such sources is subject to
[^0]
[^0]:    Received December 2011; revised July 2012.
    ${ }^{1}$ Supported by The Research Council of Norway, Project: 191460/V50, and The Norwegian Cancer Society, Project 2197685.

    AMS 2000 subject classifications. 92D30, 62N04, 60G44, 60G55.
    Key words and phrases. Causal inference, stochastic analysis, event history analysis, marked point processes, change of probability measures, local independence.

    This is an electronic reprint of the original article published by the Institute of Mathematical Statistics in The Annals of Statistics, 2012, Vol. 40, No. 4, 2162-2194. This reprint differs from the original in pagination and typographic detail.

various selection effects from drop-out due to underlying health problems to selection of the treatment itself. These problems have motivated the development of the field of causal inference, including in particular the area of marginal structural models [24, 25] which have seen applications, for instance, in HIV cohort studies [28]. The underlying idea is that observational data can be used to mimic a relevant hypothetical controlled trial or counterfactual scenario.

In this paper, our primary concern is the possibility of estimating parameters in a model for the observations from a counterfactual scenario involving a relevant hypothetical randomized controlled trial. While the specification of an appropriate model for the counterfactual observations is an important topic in itself, we will focus solely on a situation in which such a counterfactual model has been specified correctly. It is common to re-weight the observational data in order to mimic observations coming from the counterfactual scenario. This is usually referred to as inverse probability weighting. Such re-weighting has occasionally been reported to be too unstable, even inconsistent, for various purposes; see [7]. It is therefore of great interest to understand when this strategy actually works. We will provide some rigorous conditions for such re-weighting to be achievable. A similar exposition has not been carried out in the literature before, except partly in [25] and [7].

A probability distribution on the underlying sample space that would govern the frequency of observations in the counterfactual scenario can be characterized in terms of a so-called martingale problem. Short-term predictions provide dynamical characterizations of the various involved modules. A hypothetical direct intervention on a module would change its dynamics. The nondirectly intervened modules on the other hand, should have the same dynamical characterization as in the factual scenario. Martingale problems have been thoroughly studied in stochastic analysis; to us one would mean that there would exist well-developed tools for determining the feasibility of the previous re-weighting methods. An immediate application of these tools yields, for instance, that the probability distribution that would govern the frequencies of events in the counterfactual situation is unique if it exists; see Theorem 4 in the Appendix.

If the re-weighting is feasible, is it then at all possible to estimate the parameters of interest in the counterfactual model from the re-weighted observations? In other words, are these parameters identifiable? Pearl's strategy [21] is to take advantage of graphical structure, in terms of conditional independences, for identification of causal effects. It was shown in [12, 27] and [10] that this strategy gives a complete theory in the simpler setting of finite state or Gaussian-Bayesian networks. For more complicated settings, this problem is far from solved. Some results in this direction for time series were given in [11]. We show that it is possible to take advantage of local independence graphs for identification of causal effects in continuous-time

settings. Note, as this general problem is very hard, we do not provide a complete theory for identification of causal effects, only an example which slightly extends [19].

The idea that the counterfactual situation can be assigned probabilities in a way that is consistent with a purely observational scheme, is not new. It has also been considered in the general context of marked point processes in [[3, 4, 8], [20]] and [25]. We choose a martingale-based approach, similar to [25]. Note also that graphical models based on local independence and doubly stochastic Poisson processes were studied thoroughly in [9]. Continuoustime counterfactual interventions were also considered by Lok in [18]. She considered structural nested models in continuous time and applied ideas from structural equation modeling to survival data. Her strategy differs from ours in that we take a purely nonparametric point of view, through change of probability measures.

In Section 2 we describe models for the factual scenario. We then proceed in Section 3 with a description of counterfactual variables and distributions. In Section 4, we give a sufficient condition for such a counterfactual distribution to exist, and also a construction based on martingale methods. In Section 5, we introduce local independence graphs that play the same role as directed acyclic graphs usually do in the literature on causal inference. In Section 6, we consider an example where we can identify consistently estimate controlled direct effects in event history analysis. Finally, in the Appendix, we summarize some properties of dual predictable projections and consider uniqueness of counterfactual distributions.
2. The observational regime and autonomous modules. Eventually, we will consider statistical analyses based on observations of several i.i.d. individuals, but first we will consider models for one "generic" individual. We aim to investigate complex systems for each individual formed by finitely many autonomous modules that develop and influence each other throughout time. We will not provide a detailed recipe for building appropriate models, but simply assume a stochastic model for a generic individual that has some specific properties.
2.1. The underlying probability space and marked point processes. We let $\mathcal{V}$ denote the finite set of modules that form the system of interest. The possible outcomes of these modules are supposed to be realized on a probability space $(\Omega, \mathcal{F}, Q)$ with some additional structure that we will now describe. Note that we do not assume that the actual frequencies of outcomes will be governed by the probability measure $Q$. This measure will only play a role as a "reference measure." The possible "initial" outcomes of each module $V$ are given by the outcomes of a corresponding random variable $V_{0}$. The random variables in this family, which we denote by $\mathcal{V}_{0}$, are

mutually independent with respect to $Q$. The intital outcome of each $V \in \mathcal{V}$ occurs at a, possibly unknown, time point $T\left(V_{0}\right) \leq 0$. The ordering of these time points is assumed to be known. We moreover let

$$
p\left(V_{0}\right):=\left\{V_{0}^{\prime} \in \mathcal{V}_{0} \mid T\left(V_{0}^{\prime}\right)<T\left(V_{0}\right)\right\}
$$

and sometimes refer to this set as the past of $V_{0}$.
The outcomes in the follow-up are driven by a multivariate point process $N$ [13] on a finite time interval $[0, T]$. Let $J$ denote the mark space of $N$. This space is supposed to be Lusin, that is, a Borel subset in a compact metric space, and equipped with the Borel $\sigma$-algebra $\mathcal{J}$. We assume that for every module $V$, there exists a $J_{V} \in \mathcal{J}$ such that

$$
V_{t}(\omega)=V_{0}(\omega)+\int_{J_{V}} \int_{0}^{t} h(\omega, s, x) N(\omega, d s, d x)
$$

where $h$ is a bounded process on $[0, T] \times J$ that is predictable with respect to the filtration generated by $\left.N\right|_{J_{V}}$ and $V_{0}$. We also assume that $\mathcal{V}_{0} \Perp_{Q} N$ and that $\coprod_{V \in \mathcal{V}} J_{V}$ defines a partition of $J$ such that the restricted point processes $\left\{\left.N\right|_{J_{V}}\right\}_{V \in \mathcal{V}}$ are mutually independent with respect to $Q$.

For each subset $\mathcal{W}:=\left\{V^{1}, \ldots, V^{d}\right\} \subset \mathcal{V}$, let $\mathcal{F}_{t}^{\mathcal{W}}$ denote the filtration that is generated by $V_{0}$ and $\left.N\right|_{J_{V}}$ for every $V \in \mathcal{W}$ and also satisfies the usual conditions; see [14]. We let $\mathscr{P}^{\mathcal{W}}$ denote the predictable $\sigma$-algebra generated by $\mathcal{F}_{t}^{\mathcal{W}}$ [14]. For notational simplicity, we will also write $\mathcal{F}_{t}^{V}$ or $\mathscr{P}^{V}$ instead of $\mathcal{F}_{t}^{\{V\}}$ or $\mathscr{P}^{\{V\}}$, as well as $\mathcal{F}_{t}$ or $\mathscr{P}$ instead of $\mathcal{F}_{t}^{\mathcal{V}}$ or $\mathscr{P}^{\mathcal{V}}$.
2.2. The factual distribution. The actual frequencies of outcomes in the model are not assumed to be governed by $Q$, but another probability measure $P$ such that $P \ll Q$ and

$$
V_{0} \Perp_{P} T^{-1} T\left(V_{0}\right) \backslash\left\{V_{0}\right\}\left|p\left(V_{0}\right)\right.
$$

for every $V_{0} \in \mathcal{V}_{0}$, that is, every $V_{0}$ is independent w.r.t. its simultaneous variables, conditionally on the past. We will refer to property (2.3) as contemporaneous independence; see [11]. This is useful to us since it provides at least one enumeration $\left\{V_{0}^{1}, \ldots, V_{0}^{n}\right\}=\mathcal{V}_{0}$ such that $T\left(V_{0}^{i}\right) \geq T\left(V_{0}^{j}\right)$ whenever $i>j$ and

$$
E_{P}\left[f\left(V_{0}^{k}\right) \mid V_{0}^{k-1}, \ldots, V_{0}^{1}\right]=E_{P}\left[f\left(V_{0}^{k}\right) \mid p\left(V_{0}^{k}\right)\right]
$$

whenever $f$ is a bounded and measurable function and $1 \leq k \leq n$.
The processes in $\mathcal{V}$ are not necessarily mutually independent with respect to $P$, but are still sufficiently autonomous for our purpose. As an immediate manifestation of this autonomy, note that the modules may not "switch" states simultaneously $P$-a.s. The reason is that the processes in $\mathcal{V}$ are associated to disjoint subsets in the mark space $J$, which cannot occur simultaneously. We will refer to $P$ as the factual measure. Note, however, as some of the processes in $\mathcal{V}$ may be latent, the factual measure $P$ is also assumed to govern the frequency of events that may be unobserved.

2.3. The factual likelihood ratio and its factorization. The autonomy imposes a factorization of the likelihood ratio $\frac{d P}{d Q}$ that will prove to be important to us. First note that a repeated use of the Radon-Nikodym theorem provides a family $\left\{Z_{0}^{V}\right\}_{V \in \mathcal{V}}$ of nonnegative random variables such that each $Z_{0}^{V}$ is $\mathcal{F}_{0}^{p(V) \cup\{V\}}$-measurable and

$$
E_{Q}\left[Z_{0}^{V} \mid \mathcal{F}_{0}^{p(V)}\right]=1 \quad \text { and } \quad \frac{d P\left|\mathcal{F}_{0}\right.}{d Q\left|\mathcal{F}_{0}\right.}=\prod_{V \in \mathcal{V}} Z_{0}^{V}, \quad Q \text {-a.s. }
$$

There is a similar factorization of $\frac{d P}{d Q}$. Let $U$ denote the dual predictable projection of $N$ with respect to $Q$ onto the filtration $\mathcal{F}_{t}$ as in [13]. By Lemma A. 2 in the Appendix there exists a nonnegative and $\mathscr{P} \otimes \mathcal{J}$-measurable process $\lambda$ such that

$$
E_{P}\left[\int_{\mathcal{J}} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P}\left[\int_{\mathcal{J}} \int_{0}^{T} h(s, x) \lambda(s, x) U(d s, d x)\right]
$$

for every bounded and $\mathscr{P} \otimes \mathcal{J}$-measurable process $h$. As common practice, we mostly omit $\omega$ from equations in order to be notationally less overwhelming.

We now define the processes

$$
H^{V}(t):=1+\frac{U\left(\{t\}, J_{V}\right)-\int_{\mathcal{J}_{V}} \lambda(t, x) U(\{t\}, d x)}{1-U\left(\{t\}, J_{V}\right)}
$$

and

$$
K_{t}^{V}:=\int_{\mathcal{J}_{V}} \int_{0}^{t} \lambda(s, x)-H^{V}(s)(N(d s, d x)-U(d s, d x))
$$

By (A.3), we see that that $\left\{K^{V}\right\}_{V \in \mathcal{V}}$ defines a family of local $Q$-martingales with respect to the filtration $\mathcal{F}_{t}$ such that

$$
\left[K^{V}, K^{V^{\prime}}\right]=0, \quad Q \text {-a.s. for } V \neq V^{\prime}
$$

The solution of the SDE

$$
Z_{t}=Z_{0}+\sum_{V \in \mathcal{V}} \int_{0}^{t} Z_{s-} d K_{s}^{V}
$$

defines a $Q$-martingale with respect to the filtration $\mathcal{F}_{t}$ such that

$$
Z_{t}=\frac{d P\left|\mathcal{F}_{t}\right.}{d Q\left|\mathcal{F}_{t}\right.}, \quad Q \text {-a.s. }
$$

for every $t \in[0, T]$. This follows directly from [13], Theorem 5.1.
We now obtain directly from Yor's additive formula [23], Theorem II 38, that

$$
Z_{t}=\prod_{V \in \mathcal{V}} Z_{t}^{V}
$$

where each $Z^{V}$ solves an SDE

$$
Z_{t}^{V}:=Z_{0}^{V}+\int_{0}^{t} Z_{s-}^{V} d K_{s}^{V}
$$

3. Actions and counterfactual distributions. We assume that we may directly intervene on a subset of modules $\mathcal{A} \subset \mathcal{V}$ such that their outcomes are changed. This intervention does not directly affect the outcomes of the modules in $\mathcal{X}:=\mathcal{V} \backslash \mathcal{A}$. The latter set of modules will only be affected indirectly: The conditional distributions of their short-term behavior, given the past, will remain the same, while the change of previous outcomes yields a change of the background these distributions depend on. We will limit our discussion to actions that are deterministically dependent on the past. These are sometimes referred to as conditional actions. Every conditional action will be represented by a measurable transformation $\theta$ of the generic state space $(\Omega, \mathcal{F})$. We think of $\theta(\omega)$ as the direct consequence in the "counterfactual universe" where the action $\theta$ was performed.

Whenever $P^{\prime}$ is a probability measure on $(\Omega, \mathcal{F})$, we let $\theta P^{\prime}$ denote the push-forward measure over $\theta$, that is, $\theta P^{\prime}(F):=P^{\prime}\left(\theta^{-1}(F)\right)$ for every $F \in \mathcal{F}$. Whenever $H$ is an $\mathcal{F}$-measurable random variable, we let $\theta^{*} H$ denote the transformed variable, where $\theta^{*} H(\omega):=H(\theta(\omega))$ for every $\omega \in \Omega$. We assume that $\theta$ is "continuous" in the sense that the reference measure $Q$ is quasiinvariant with respect to $\theta$, that is,

$$
\theta Q \ll Q
$$

3.1. Actions and counterfactual distributions at baseline. Let $V \in \mathcal{V}$ and suppose $\eta$ is an $\mathcal{F}_{0}^{V}$-measurable random variable, and $h$ is a bounded and $\mathcal{F}_{0}^{p(V)}$-measurable random variable. We assume that the outcomes of the not directly intervened part of the system are left invariant by the transformation at baseline, that is,

$$
\theta^{*} \eta=\eta
$$

for every $\eta$ and every $V \in \mathcal{X}$. We furthermore assume that the action depends deterministically on the past outcomes in the nonintervened system, that is, whenever $V \in \mathcal{A}$, then

$$
\theta^{*} \eta \text { is } \mathcal{F}_{0}^{p(V) \cap \mathcal{X}} \text {-measurable }
$$

for every $\eta$.
A probability distribution $P_{\theta}$ on $(\Omega, \mathcal{F})$ defines a counterfactual distribution at baseline if, whenever $V \in \mathcal{A}$, then

$$
E_{P_{\theta}}[h \eta]=E_{P_{\theta}}\left[h \theta^{*} \eta\right]
$$

and, whenever $V \in \mathcal{X}$, then

$$
E_{P_{\theta}}[h \eta]=E_{P_{\theta}}\left[h \theta^{*} E_{P}\left[\eta \mid \mathcal{F}_{0}^{p(V)}\right]\right]
$$

for every $\eta$.
Equation (3.5) means that the short-term behavior of a directly intervened variable is simply given by the transformed variable. Its outcome is deterministically regulated by the past. Equation (3.5) means that the conditional distribution of an outcome of a not directly intervened variable in the counterfactual scenario, given its past, coincides with the corresponding distribution from the factual scenario.

Note that Pearl's do $(X=x)$ may also be interpreted as a transformation on sample space that fixes $X$ constantly equal to $x$ and leaves the remaining variables invariant. This means that our characterization of probability measures on $(\Omega, \mathcal{F})$ that would govern the frequencies of events in our system if we, contrary to the fact, had applied the hypothetical intervention strategy, is a reformulation of Pearl's do-operator on Bayesian networks [21]. The present approach, however, translates more or less directly to continuoustime settings.
3.2. Actions and counterfactual distributions in the follow-up period. Whenever $Z$ is a stochastic process on $\Omega$, we let $\theta^{*} Z$ denote the process given by the transformed variables $\left\{\theta^{*} Z_{t}\right\}_{t \in[0, T]}$. We assume that $\theta^{*} N$ defines a marked point process that is adapted to the history $\left\{\mathcal{F}_{t}\right\}_{t \in[0, T]}$. The action $\theta$ is thought to force the outcomes $\left.N\right|_{[0, T] \times J_{\mathcal{A}}}$ into the outcomes of $\left.\theta^{*} N\right|_{[0, T] \times J_{\mathcal{A}}}$, which will only depend on the strictly previous behavior of the not directly intervened system, that is, whenever $B \in J_{\mathcal{A}}$, then

$$
\theta^{*} N_{t}(B) \quad \text { is predictable w.r.t. } \mathcal{F}_{t}{ }^{\mathcal{X}}
$$

The outcomes of the not directly intervened part of the system are left invariant by the transformation during follow-up, that is,

$$
\left.\theta^{*} N\right|_{[0, T] \times J_{X}}=\left.N\right|_{[0, T] \times J_{X}}
$$

We will say that $P_{\theta}$ defines a counterfactual distribution if it defines a counterfactual distribution at baseline, and if whenever $X$ is process on the form (2.2) and $\Lambda$ is an $\mathcal{F}_{t}$-predictable process of finite variation such that

$$
E_{P}\left[\int_{0}^{T} h_{s} d X_{s}\right]=E_{P}\left[\int_{0}^{T} h_{s} d \Lambda_{s}\right]
$$

for every bounded and $\mathcal{F}_{t}$-predictable process $h$, then

$$
E_{P_{\theta}}\left[\int_{0}^{T} h_{s} d X_{s}\right]=E_{P_{\theta}}\left[\int_{0}^{T} h_{s} d \theta^{*} \Lambda_{s}\right] \quad \text { if } V \in \mathcal{X}
$$

and

$$
E_{P_{\theta}}\left[\int_{0}^{T} h_{s} d X_{s}\right]=E_{P_{\theta}}\left[\int_{0}^{T} h_{s} d \theta^{*} X_{s}\right] \quad \text { if } V \in \mathcal{A}
$$

Note that (3.8) means that $\theta^{*} \Lambda$ defines the compensator of $X$ if $V \in \mathcal{X}$, and (3.9) means that $\theta^{*} X$ defines the compensator of $X$, otherwise. This offers an analogous interpretation as in the baseline setting. Compensators provide a notion of short-term behavior, analogously to the previous conditional distributions. The short-term behavior of a not directly intervened process in the counterfactual scenario, based on the past, coincides with the transformed short-term behavior from the factual scenario. The short-term behavior of a directly intervened process is given entirely by the transformation.

Following [22], we will say that a model consisting of a factual scenario, an action and a corresponding counterfactual distribution, defines a causal model if the counterfactual distribution would fit the actual corresponding counterfactual scenario. That $P_{\theta}$ actually would govern the frequency of observations for this hypothetical scenario is generally not testable, and mostly comes down to the question of no unmeasured confounding [22].

# 4. Construction of counterfactual distributions. 

4.1. Construction at baseline. We will now construct the counterfactual distribution in a situation with no follow-up period. The construction is then closely related to Pearl's framework [21]. The next result is important and says heuristically that if the conditional probability, given the past, of observing outcomes that coincide with counterfactually enforced ones are not too small, then there exists a counterfactual distribution. Equation (4.2) then offers a useful description of the distribution. Note that this is a measure theoretical version of the truncated factorization formula from [21], (3.10).

THEOREM 1. If there exists a nonnegative $K \in L^{1}\left(\mathcal{F}_{0}, P\right)$ such that

$$
\frac{d \theta Q_{\mathcal{F}_{0}}}{d Q_{\mathcal{F}_{0}}} \leq K \prod_{V \in \mathcal{A}} Z_{0}^{V}, \quad P \text {-a.s. }
$$

then

$$
\prod_{V \in \mathcal{X}} Z_{0}^{V} \cdot \theta Q_{\mathcal{F}_{0}}
$$

defines a counterfactual distribution on $\mathcal{F}_{0}$ that is absolutely continuous with respect to $\left.P\right|_{\mathcal{F}_{0}}$ and imposes contemporaneously independent outcomes.

Proof. First note that for every bounded $\mathcal{F}_{0}$-measurable random variable $\eta$,

$$
\begin{aligned}
E_{P}\left[\eta \frac{d \theta Q\left|\mathcal{F}_{0}\right.}{d Q\left|\mathcal{F}_{0}\right.} \prod_{V \in \mathcal{A}} \frac{1}{Z_{0}^{V}}\right] & =E_{Q}\left[\eta \frac{d \theta Q\left|\mathcal{F}_{0}\right.}{d Q\left|\mathcal{F}_{0}\right.} \prod_{V \in \mathcal{X}} Z_{0}^{V}\right]=E_{\theta Q}\left[\eta \prod_{V \in \mathcal{X}} Z_{0}^{V}\right] \\
& \leq E_{P}[\eta K]
\end{aligned}
$$

This shows that (4.2) defines a finite measure $P_{\theta}$ on $\mathcal{F}_{0}$ such that $P_{\theta} \ll P \mid \mathcal{F}_{0}$.
We choose an enumeration $V_{1}, \ldots, V_{m}$ of the variables in $\mathcal{X}$ such that $j<k$ implies that $T\left(V_{j}\right) \leq T\left(V_{k}\right)$. If $V_{k} \in \mathcal{X}$ and $\eta$ is a bounded $\mathcal{F}_{0}^{\left\{V_{k}\right\} \cup p\left(V_{k}\right)}-$ measurable random variable, then

$$
E_{Q}\left[\theta^{*} \eta \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right]=\theta^{*} E_{Q}\left[\eta \mid \mathcal{F}_{0}^{p(V)}\right], \quad Q \text {-a.s. }
$$

To see this, we let $\eta_{1}$ be an $\mathcal{F}_{0}^{V_{k}}$-measurable and bounded random variable and let $\eta_{2}$ be an $\mathcal{F}_{0}^{p\left(V_{k}\right)}$-measurable and bounded variable and compute

$$
\begin{aligned}
E_{Q}\left[\theta^{*}\left(\eta_{1} \eta_{2}\right) \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right] & =E_{Q}\left[\eta_{1} \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right] \theta^{*} \eta_{2} \\
& =\theta^{*}\left(E_{Q}\left[\eta_{1} \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right] \eta_{2}\right) \\
& =\theta^{*}\left(E_{Q}\left[\eta_{1} \mid \mathcal{F}_{0}^{p\left(V_{k}\right)}\right] \eta_{2}\right) \\
& =\theta^{*} E_{Q}\left[\eta_{1} \eta_{2} \mid \mathcal{F}_{0}^{p\left(V_{k}\right)}\right], \quad Q \text {-a.s. }
\end{aligned}
$$

Equation (4.3) now follows from the monotone class lemma. Especially, this means that for every $k \leq m$,

$$
E_{Q}\left[\theta^{*} Z_{0}^{V_{k}} \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right]=\theta^{*} E_{Q}\left[Z_{0}^{V_{k}} \mid \mathcal{F}_{0}^{p\left(V_{k}\right)}\right]=1, \quad Q \text {-a.s. }
$$

and

$$
\begin{aligned}
E_{\theta Q}\left[Z_{0}^{V_{1}} \cdots Z_{0}^{V_{k}}\right] & =E_{Q}\left[\theta^{*} Z_{0}^{V_{1}} \cdots \theta^{*} Z_{0}^{V_{k-1}} E_{Q}\left[\theta^{*} Z_{0}^{V_{k}} \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right]\right] \\
& =E_{Q}\left[\theta^{*} Z_{0}^{V_{1}} \cdots \theta^{*} Z_{0}^{V_{k-1}}\right]=E_{\theta Q}\left[Z_{0}^{V_{1}} \cdots Z_{0}^{V_{k-1}}\right]
\end{aligned}
$$

That $P_{\theta}$ defines a probability measure on $\mathcal{F}_{0}$ follows by induction.
To see that (3.5) and (3.4) are satisfied, suppose $V_{k} \in \mathcal{X}$, and let $\eta, h$ be bounded random variables such that $\eta$ is $\mathcal{F}_{0}^{V_{k}}$-measurable and $h$ is $\mathcal{F}_{0}^{p\left(V_{k}\right)}$ measurable. We see that

$$
\begin{aligned}
E_{P_{\theta}}[\eta h] & =E_{\theta Q}\left[\left(\prod_{j=1}^{k-1} Z_{0}^{V_{j}}\right) \eta h Z_{0}^{V_{j}}\right] \\
& =E_{Q}\left[\left(\prod_{j=1}^{k-1} \theta^{*} Z_{0}^{V_{j}}\right) \theta^{*} h E_{Q}\left[\theta^{*} \eta Z_{0}^{V_{k}} \mid \mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right]\right]
\end{aligned}
$$

$$
\begin{aligned}
& =E_{Q}\left[\left(\prod_{j=1}^{k-1} \theta^{*} Z_{0}^{V_{j}}\right) \theta^{*} h \theta^{*} E_{Q}\left[\eta Z_{0}^{V_{k}}\left|\mathcal{F}_{0}^{p\left(V_{k}\right)}\right]\right]\right. \\
& =E_{P_{\theta}}\left[h \theta^{*} E_{P}\left[\eta\left|\mathcal{F}_{0}^{p(V)}\right|\right]\right.
\end{aligned}
$$

If $V_{k} \in \mathcal{A}$, then

$$
\begin{aligned}
E_{P_{\theta}}[\eta h] & =E_{\theta Q}\left[\left(\prod_{j=1}^{k-1} Z_{0}^{V_{j}}\right) \eta h Z_{0}^{V_{j}}\right] \\
& =E_{Q}\left[\left(\prod_{j=1}^{k-1} \theta^{*} Z_{0}^{V_{j}}\right) \theta^{*} h \theta^{*} \eta E_{Q}\left[Z_{0}^{V_{k}}\left|\mathcal{F}_{0}^{\left\{V_{1}, \ldots, V_{k-1}\right\}}\right]\right]\right. \\
& =E_{Q}\left[\left(\prod_{j=1}^{k-1} \theta^{*} Z_{0}^{V_{j}}\right) \theta^{*} h \theta^{*} \eta\right] \\
& =E_{P_{\theta}}\left[h \theta^{*} \eta\right]
\end{aligned}
$$

4.2. Construction for the follow-up period. Condition (3.1) can be made somewhat more concrete if the processes, that may be directly intervened on, only are allowed to jump at a given finite sequence of predictable times. This behavior is very different from that of Poisson processes. More formally, we assume that there exists a bounded and $\mathcal{F}_{t}$-predictable multivariate counting measure $\tilde{U}^{A}$ on $[0, T] \times J_{A}$ such that

$$
\left.N\right|_{[0, T] \times J_{A}} \ll \tilde{U}^{A}
$$

for every $A \in \mathcal{A}$. We can now show the reference measure $Q$ is quasi-invariant if the probability of an outcome that coincides with the counterfactually enforced outcome at short-term is not too small.

Proposition 1. Suppose that $\theta$ is an $\mathcal{F}$-measurable transformation on $\Omega$ that satisfies (3.2)-(3.6) and assume (4.5). If there exists a bounded and $\mathscr{P}$-measurable process $\tilde{Y}$ such that:
(1) $\left.\theta Q\right|_{\mathcal{F}_{0}} \ll Q\left|_{\mathcal{F}_{0}}\right.$;
(2) 

$$
\int_{J_{A}} \int_{0}^{T} h(s, x) \theta^{*} N(d s, d x)=\int_{J_{A}} \int_{0}^{T} h(s, x) \tilde{Y}(s, x) U^{A}(d s, d x)
$$

$Q$-a.s. for every $A \in \mathcal{A}$ and bounded and $\mathscr{P}$-measurable process $h$;
(3) there exists a constant $c>0$ such that

$$
1-\theta^{*} N\left(\{s\}, J_{A}\right) \leq c \cdot\left(1-U^{A}\left(\{s\}, J_{A}\right)\right), \quad Q \text {-a.s. }
$$

for every $s \in[0, T]$,
then $\theta Q \ll Q$.

Proof.
The integral equation

$$
\begin{aligned}
& \int_{J} \int_{0}^{T} h(s, x) U^{\theta}(d s, d x) \\
& \quad=\sum_{A \in \mathcal{A}} \int_{J_{A}} \int_{0}^{T} h(s, x) \theta^{*} N(d s, d x)+\sum_{V \in \mathcal{X}} \int_{J_{A}} \int_{0}^{T} h(s, x) U^{V}(d s, d x)
\end{aligned}
$$

defines an $\mathcal{F}_{t}$ - predictable random measure $U^{\theta}$ on $[0, T] \times J$.
Let $B \subset J$ be a measurable subset, and define $N_{t}^{B}:=\int_{0}^{t} \int_{B} N(d s, d x)$. If $B \subset J_{A}$ for an $A \in \mathcal{A}$ and $S$ is a $\mathcal{F}_{t}$-adapted stopping time, then

$$
E_{\theta Q}\left[N_{S}^{B}-U_{S}^{\theta}(B,[0, t])\right]=E_{\theta Q}\left[N_{S}^{B}-\theta^{*} N_{S}^{B}\right]=E_{\theta Q}\left[\theta^{*} N_{S}^{B}-\theta^{*} N_{S}^{B}\right]=0
$$

This means that $N_{t}-U_{t}^{\theta}(B,[0, t])$ defines a local $Q$-martingale with respect to the filtration $\mathcal{F}_{t}$. Similarly, if $B \subset J_{\mathcal{X}}$, note that

$$
\begin{aligned}
E_{\theta Q}\left[\int_{0}^{T} h_{s} d N_{s}^{B}\right] & =E_{Q}\left[\int_{0}^{T} \theta^{*} h_{s} d N_{s}^{B}\right] \\
& =E_{Q}\left[\int_{0}^{T} \theta^{*} h_{s} d U(d s, B)\right] \\
& =E_{\theta Q}\left[\int_{0}^{T} h_{s} d U^{\theta}(d s, B)\right]
\end{aligned}
$$

for every bounded and $\mathcal{F}$-predictable process $h$. Now, $N([0, t], B)-U^{\theta}([0, t]$, $B)$ defines a local $\theta Q$-martingale with respect to the filtration $\left\{\mathcal{F}_{t}\right\}_{t \in[0, T]}$. This means that

$$
E_{\theta Q}\left[\int_{J} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{\theta Q}\left[\int_{J} \int_{0}^{T} h(s, x) U^{\theta}(d s, d x)\right]
$$

for every bounded and $\mathscr{P} \otimes \mathcal{J}$-measurable process $h$.
We define the processes

$$
\begin{aligned}
H^{A}(t, x) & :=\tilde{Y}(t, x)-1-\frac{U\left(\{t\}, J_{A}\right)-\theta^{*} N\left(\{t\}, J_{A}\right)}{1-U\left(\{t\}, J_{A}\right)} I\left(U\left(\{t\}, J_{A}\right) \neq 1\right) \\
\zeta_{t}^{A} & :=\int_{J_{A}} \int_{0}^{t} H^{A}(s, x)(N(d s, d x)-U(d s, d x))
\end{aligned}
$$

and let $\zeta:=\sum_{A \in \mathcal{A}} \zeta^{A}$.
By [14], Proposition I 3.13, there exists a $\mathscr{P}$-measurable and nonnegative stochastic process $\gamma^{A}$ such that $\gamma^{A} \leq 1$ and

$$
\int_{J_{A}} \int_{0}^{T} h(s, x) U^{A}(d s, d x)=\int_{J_{A}} \int_{0}^{T} h(s, x) \gamma^{A}(s, x) \tilde{U}^{A}(d s, d x)
$$

$Q$-a.s. for every bounded and $\mathscr{P}$-measurable stochastic process $h$.

A computation shows that the predictable variation process for $\zeta$ with respect to $Q$ satisfies

$$
\begin{aligned}
\langle\zeta, \zeta\rangle_{t} & =\sum_{A \in \mathcal{A}}\left\langle\zeta^{A}, \zeta^{A}\right\rangle_{t} \\
& =\sum_{A \in \mathcal{A}} \int_{J_{A}} \int_{0}^{t} H^{A}(s, x)^{2} \gamma^{A}(s, x)\left(1-\gamma^{A}(s, x)\right) \tilde{U}^{A}(d s, d x)
\end{aligned}
$$

which is $Q$-a.s. uniformly bounded. Now, [17], Theorem II.1, implies that the SDE

$$
\rho_{t}=\left.\frac{d \theta Q\right|_{\mathcal{F}_{0}}}{\left.d Q\right|_{\mathcal{F}_{0}}}+\int_{0}^{t} \rho_{s-} d \zeta_{s}
$$

defines a uniformly integrable $Q$-martingale with respect to the filtration $\mathcal{F}_{t}$. This means that

$$
\tilde{Q}:=\rho_{T} \cdot Q
$$

defines a probability measure on $(\Omega, \mathcal{F})$.
A computation shows that if $B \subset J_{V}$ for some $V \in \mathcal{V}$, then

$$
N_{t}^{B}-U_{t}([0, t], B)-\int_{0}^{t} \rho_{s-}^{-1} d\left\langle N^{B}-U^{B}, \rho\right\rangle_{s}=N_{t}^{B}-U^{\theta}([0, t], B)
$$

Girsanov's Theorem [14], Theorem III 1.21, implies that

$$
E_{\tilde{Q}}\left[\int_{J} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{\tilde{Q}}\left[\int_{J} \int_{0}^{T} h(s, x) U^{\theta}(d s, d x)\right]
$$

for every bounded and $\mathscr{P} \otimes \mathcal{J}$-measurable process $h$. Finally, [13], Theorem 3.4, implies that there exists only one probability measure which has $U^{\theta}$ as a dual predictable projection for $N$. Therefore $\theta Q=\tilde{Q} \ll Q$.

The next result is important and says that if the probability of observing an outcome that coincides with the counterfactually enforced outcome at short-term is not too small, then there exists a counterfactual distribution for the follow-up period. The counterfactual distribution can then be obtained by re-weighting the factual distribution, that is, $P_{\theta} \ll P$. Note that (4.12) provides a continuous-time analogy of the truncated factorization formula for Bayesian networks [21], (3.10).

Theorem 2. Suppose that the conditions of Theorem 1 are satisfied and that there exists a bounded and $\mathscr{P}$-measurable process $Y$ such that:
(4.10) $\int_{J_{A}} \int_{0}^{T} h(s, x) \theta^{*} N(d s, d x)=\int_{J_{A}} \int_{0}^{T} h(s, x) Y(s, x) \lambda(s, x) U(d s, d x)$
$P$-a.s. for every $A \in \mathcal{A}$ and bounded and $\mathscr{P}$-measurable process $h$;

(2) there exists a constant $c>0$ such that

$$
1-\theta^{*} N\left(\{s\}, J_{A}\right) \leq c\left(1-\lambda \cdot U\left(\{s\}, J_{A}\right)\right), \quad P \text {-a.s. }
$$

for every $s \in[0, T]$.
Then there exists a counterfactual distribution $P_{\theta}$ such that $P_{\theta} \ll P$. We also have that $P_{\theta} \ll \theta Q$ and

$$
X_{t}:=\prod_{V \in \mathcal{X}} Z_{t}^{V}
$$

where $Z^{V}$ is the process defined in (2.10), defines a $\theta Q$-martingale with respect to the filtration $\left\{\mathcal{F}_{t}\right\}$ that satisfies the SDE

$$
X_{t}=\prod_{V \in \mathcal{X}} Z_{0}^{V}+\sum_{V \in \mathcal{X}} \int_{0}^{t} X_{s-} d K_{s}^{V}
$$

and

$$
\frac{d P_{\theta}}{d \theta Q}=X_{T}
$$

Proof. We follow the proof of Proposition 1 and define the processes

$$
\begin{aligned}
G^{A}(t, x) & :=Y(t, x)-1-\frac{\lambda \cdot U\left(\{t\}, J_{A}\right)-\theta^{*} N\left(\{t\}, J_{A}\right)}{1-\lambda \cdot U\left(\{t\}, J_{A}\right)} I\left(\lambda \cdot U\left(\{t\}, J_{A}\right) \neq 1\right) \\
\xi_{t}^{A} & :=\int_{J_{A}} \int_{0}^{t} G^{A}(s, x)(N(d s, d x)-\lambda \cdot U(d s, d x)) \\
\xi & :=\sum_{A \in \mathcal{A}} \xi^{A}
\end{aligned}
$$

By [14], Proposition I 3.13, there exists a $\mathscr{P}$-measurable and nonnegative stochastic process $\gamma^{A}$ such that $\gamma^{A} \leq 1$ and

$$
\int_{J_{A}} \int_{0}^{T} h(s, x) \lambda(s, x) U(d s, d x)=\int_{J_{A}} \int_{0}^{T} h(s, x) \gamma^{A}(s, x) \tilde{U}^{A}(d s, d x)
$$

$Q$-a.s. for every bounded and $\mathscr{P}$-measurable stochastic process $h$.
A computation shows that the predictable variation process for $\xi$ with respect to $P$ satisfies

$$
\begin{aligned}
\langle\xi, \xi\rangle_{t} & =\sum_{A \in \mathcal{A}}\left\langle\xi^{A}, \xi^{A}\right\rangle_{t} \\
& =\sum_{A \in \mathcal{A}} \int_{J_{A}} \int_{0}^{t} G^{A}(s, x)^{2} \gamma^{A}(s, x)\left(1-\gamma^{A}(s, x)\right) \tilde{U}^{A}(d s, d x)
\end{aligned}
$$

which is $Q$-a.s uniformly bounded. Now, [17], Theorem II.1, implies that the SDE

$$
W_{t}=\left.\frac{d P_{\theta}\right|_{\mathcal{F}_{0}}}{\left.d P\right|_{\mathcal{F}_{0}}}+\int_{0}^{t} W_{s-} d \xi_{s}
$$

defines a uniformly integrable $P$-martingale with respect to the filtration $\mathcal{F}_{t}$. This means that

$$
P_{\theta}:=Z_{T} \cdot P
$$

defines a probability measure on $(\Omega, \mathcal{F})$.
The integral equation

$$
\begin{aligned}
& \int_{J} \int_{0}^{T} h(s, x) \nu^{\theta}(d s, d x) \\
& =\int_{J_{X}} \int_{0}^{T} h(s, x) \lambda(s, x) U(d s, d x)+\int_{J_{A}} \int_{0}^{T} h(s, x) \theta^{*} N(d s, d x)
\end{aligned}
$$

defines a predictable and nonnegative random measure $\nu^{\theta}$ on $[0, T] \times J$ such that

$$
\begin{aligned}
\xi_{t}=\int_{J} \int_{0}^{t}(Y(s, x)-1- & \frac{U \lambda \cdot(\{s\}, J)-\nu^{\theta}(\{s\}, J)}{1-\lambda \cdot U(\{s\}, J)} \\
& \times I(\lambda \cdot U(\{s\}, J) \neq 1)) N(d s, d x)-\lambda \cdot U(d s, d x)
\end{aligned}
$$

We obtain from [13], Theorem 5.2, that

$$
E_{P_{\theta}}\left[\int_{J} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P_{\theta}}\left[\int_{J} \int_{0}^{T} h(s, x) \nu^{\theta}(d s, d x)\right]
$$

for every bounded and $\mathscr{P} \otimes \mathcal{J}$-measurable process $h$; that is, $P_{\theta}$ defines a counterfactual distribution.

We may compute that

$$
\begin{aligned}
\Delta \zeta_{s}^{A}= & \int_{J_{A}} \tilde{Y}(s, x) N(\{s\}, d x)-\theta^{*} N\left(\{s\}, J_{A}\right) \\
& +\left(\tilde{U}\left(\{s\}, J_{A}\right)-\theta^{*} N\left(\{s\}, J_{A}\right) I\left(U\left(\{s\}, J_{A}\right) \neq 1\right)\right) \\
& \times\left(\tilde{U}\left(\{s\}, J_{A}\right)-N\left(\{s\}, J_{A}\right)\right)
\end{aligned}
$$

and that

$$
\begin{aligned}
\Delta \xi_{s}^{A}= & \int_{J_{A}} Y(s, x) N(\{s\}, d x)-\theta^{*} N\left(\{s\}, J_{A}\right) \\
& +\left(\tilde{U}\left(\{s\}, J_{A}\right)-\theta^{*} N\left(\{s\}, J_{A}\right) I\left(\lambda \cdot U\left(\{s\}, J_{A}\right) \neq 1\right)\right) \\
& \times\left(\tilde{U}\left(\{s\}, J_{A}\right)-N\left(\{s\}, J_{A}\right)\right)
\end{aligned}
$$

We moreover define a process $\chi$ as follows:

$$
\chi_{t}:=\sum_{s \leq t} \frac{\Delta \xi_{s}-\Delta \zeta_{s}}{\Delta \zeta_{s}+1} I\left(\Delta \zeta_{s} \neq-1\right)
$$

One can show that $\chi$ only jumps at the jump times of $\hat{U}$ and that $\Delta \chi$ is uniformly bounded. This means that the SDE

$$
\pi_{t}:=\frac{d \theta Q|_{\mathcal{F}_{0}}}{d Q|_{\mathcal{F}_{0}}} \prod_{A \in \mathcal{A}} \frac{1}{Z_{0}^{A}}+\int_{0}^{t} \pi_{s-} d \chi_{s}
$$

defines a $P$ semi-martingale with respect to the filtration $\mathcal{F}_{t}$. Note that $\Delta \zeta_{s}=-1$ implies that $\Delta \xi_{s}=-1$, so

$$
\zeta+[\zeta, \chi]+\chi=\xi, \quad P \text {-a.s. }
$$

Yor's additive formula [23], Theorem II 38, then implies that

$$
\pi_{t} \rho_{t}=\frac{d P_{\theta}|_{\mathcal{F}_{0}}}{d P|_{\mathcal{F}_{0}}}+\int_{0}^{t} \pi_{s-} \rho_{s-} d \xi_{s}
$$

This implies that $W=\rho \pi$, and hence

$$
E_{P_{\theta}}[h]=E_{P}\left[h W_{T}\right]=E_{Q}\left[h Z_{T} \rho_{T} \pi_{T}\right]=E_{\theta Q}\left[h Z_{T} \pi_{T}\right]
$$

for every bounded and $\mathcal{F}_{T}$-measurable random variable $h$, so $P_{\theta} \ll \theta Q$. Finally [13], Theorem 5.1, shows that the likelihood ratio $\frac{d P_{\theta}}{d \theta Q}$ is given by the SDE (4.13), and hence Yor's additive formula provides identity (4.12).

Note that since $P_{\theta} \ll \theta Q=\theta^{2} Q$, the counterfactual distribution $P_{\theta}$ is actually invariant with respect to the action $\theta$, that is,

$$
\theta P_{\theta}=P_{\theta}
$$

# 5. Local independence. 

5.1. Identifiability and short-term dependence. A causal effect is identifiable if it can be uniquely obtained from the factual distribution of the observable variables. This is generally very hard to determine and may also require further parametric assumptions. We show that it is possible to take advantage of graphical structure, in terms of local independence graphs, to do this. Such graphs are useful when deciding in which situations causal effects are identifiable, and also which factors we might adjust for.

We will say that $V \in \mathcal{V}$ is locally independent of a subset $\mathcal{B} \subset \mathcal{V}$ at baseline, conditionally on $\mathcal{V}^{\prime} \subset \mathcal{V}$, if the conditional density of $V_{0}$, given the past, does not depend on the baseline information from $\mathcal{B}$. More precisely, for every integrable and $\mathcal{F}_{0}^{V}$-measurable random variable $\eta$, there exists a random variable $\tilde{\eta}$ that is $\mathcal{F}_{0}^{p(V) \cap\left(\mathcal{V}^{\prime} \backslash \mathcal{B}\right)}$-measurable and such that if $h$ is $\mathcal{F}_{0}^{p(V) \cap \mathcal{V}^{\prime}}$ -

measurable, then

$$
E_{P}[\eta h]=E_{P}[\tilde{\eta} h]
$$

A process $V \in \mathcal{V}$ is locally independent of $\mathcal{B} \subset \mathcal{V}$ during follow-up, conditionally on $\mathcal{V}^{\prime}$, if for every process $X$ on the form (2.2), there exists an $\mathcal{F}_{t}^{\{V\} \cup \mathcal{V}^{\prime} \backslash \mathcal{B}}$-predictable process $\Lambda$ with finite variation such that

$$
E_{P}\left[\int_{0}^{T} h_{s} d X_{s}\right]=E_{P}\left[\int_{0}^{T} h_{s} d \Lambda_{s}\right]
$$

for every bounded and $\mathcal{F}_{t}^{\{V\} \cup \mathcal{V}^{\prime}}$-predictable process $h$. If $V$ is locally independent of $\mathcal{B}$, conditionally on $\mathcal{V}^{\prime}$, both at baseline and during follow-up, we will say that $V$ is locally independent of $\mathcal{B}$, conditionally on $\mathcal{V}^{\prime}$. This will sometimes be written $\mathcal{B} \nrightarrow V \mid \mathcal{V}^{\prime}$. A local independence graph is a directed graph $G=\left(\mathcal{V}^{\prime}, \mathcal{E}\right)$ for $\mathcal{V}^{\prime} \subset \mathcal{V}$ such that the absence of an arrow from a subset $\mathcal{B} \subset \mathcal{V}^{\prime}$ to a process $V \in \mathcal{V}^{\prime}$ means that $\mathcal{B} \nrightarrow V \mid \mathcal{V}^{\prime}$. Note that local independence graphs are also refered to as local independence graphs (see $[1,9]$ ) and were introduced in [26].

Given time points $\left\{T\left(V_{0}\right)\right\}_{V \in \mathcal{V}}$ at baseline and a local independence graph $G=(\mathcal{V}, \mathcal{E})$, we can pick a linear ordering of $\mathcal{V}_{0}$ that satisfies (2.4) and therefore yields

$$
V_{0}^{i} \Perp_{P}\left\{V_{0}^{1}, V_{0}^{2}, \ldots, V_{0}^{i-1}\right\} \mid \mathcal{F}_{0}^{\mathrm{pa}\left(V^{i}\right)}
$$

for every $i \leq n$. Property (5.3) is known as the ordered directed Markov Property and was shown to be equivalent to the local directed Markov property in [16], Theorem 2.11. This means that Bayesian networks and local independence graphs are two descriptions of the same structure when the nodes correspond to single variables. Note that local independence graphs, where the nodes are allowed to be families of variables or processes, are allowed to be cyclic.
5.2. Measurability of intensities. Local independence during the followup is closely related to the measurability of intensities.

Lemma 1. Suppose that $V$ is locally independent of $\mathcal{B}$ at baseline, conditionally on $\mathcal{V}^{\prime}$, then $\mathcal{B} \nrightarrow V \mid \mathcal{V}^{\prime}$ if and only if there exists a nonnegative and $\mathscr{P}^{\{V\} \cup \mathcal{V}^{\prime} \backslash \mathcal{B}}$-measurable process $\lambda^{V}$ such that

$$
E_{P}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) \lambda^{V}(s, x) U(d s, d x)\right]
$$

for every bounded and $\mathscr{P}^{\{V\} \cup \mathcal{V}^{\prime}}$-measurable process $h$.
Proof. If there exists a process $\lambda^{V}$ as in (5.4), then $\mathcal{B} \nrightarrow V \mid \mathcal{V}^{\prime}$ follows directly. Conversely, suppose that $\mathcal{B} \nrightarrow V \mid \mathcal{V}^{\prime}$ and let $D \subset J_{V}$ be a measurable subset. Now, $N_{t}^{D}:=N([0, t], D)$ defines a processes on the form (2.2), so

there must exist a corresponding predictable increasing process $\Lambda^{D}$ of finite variation such that

$$
E_{P}\left[\int_{0}^{T} h_{s} d N_{s}^{D}\right]=E_{P}\left[\int_{0}^{T} h_{s} d \Lambda_{s}^{D}\right]
$$

for every bounded and $\mathcal{F}_{t}^{\{V\} \cup \mathcal{V}^{\prime}}$-predictable process $h$.
The Radon-Nikodym theorem now provides an $\mathcal{F}^{\{V\} \cup \mathcal{V}^{\prime} \backslash \mathcal{B}}$-measurable and nonnegative process $\lambda^{(D)}$ such that

$$
E_{P}\left[\int_{0}^{T} h_{s} d N_{s}^{D}\right]=E_{P}\left[\int_{0}^{T} h_{s} \lambda_{s}^{(D)} U(d s, D)\right]
$$

for every bounded and $\mathcal{F}_{t}^{\{V\} \cup \mathcal{V}^{\prime}}$-measurable process $h$.
Since $J$ is a Lusin space, we may construct a nonnegative and $\mathscr{P}^{\{V\} \cup \mathcal{V}^{\prime}}-$ measurable process $\lambda^{V}$ that satisfies (5.4) as a limit of processes that are finite linear combinations of processes on the form $f \cdot J_{D}$, where $D$ is a measurable subset in $J_{V}$, and $f$ is a bounded $\mathcal{F}_{t}^{\{V\} \cup \mathcal{V}^{\prime} \backslash \mathcal{B}}$-measurable process.
5.3. Markovian factorization property. The local Markov property implies the Markovian factorization property; see [21], (1.33) and [16], (2.10). We will now see that a local independence graph yields a similar factorization for the follow-up period. We use the following notation from graph theory: whenever $V \in \mathcal{V}$, let $c l(V) \subset \mathcal{V}$ denote the set formed by $V$ and its parents in $G$.

THEOREM 3. If $G=(\mathcal{V}, \mathcal{E})$ is a local independence graph with respect to $P$, then there exists an $\mathcal{F}_{t}^{\mathrm{cl}(V)}$-adapted $P$-indistinguishable version of each process $Z^{V}$ from Theorem 2.9 where

$$
Z=\prod_{V \in \mathcal{V}} Z^{V}, \quad P \text {-a.s. }
$$

Proof. Let $\mathcal{F}_{0}^{\mathrm{pa}(V)}:=\bigvee_{V^{\prime} \in \mathrm{pa}(V)} \mathcal{F}_{0}^{V^{\prime}}$ and $\mathcal{F}_{0}^{\mathrm{cl}(V)}:=\bigvee_{V^{\prime} \in \mathrm{cl}(V)} \mathcal{F}_{0}^{V^{\prime}}$ and let

$$
Y^{V}:=\frac{d P_{\mid \mathcal{F}_{0}^{\mathrm{pa}(V)}}}}{d Q_{\mathcal{F}_{0}^{\mathrm{pa}(V)}}}
$$

Now

$$
P_{\mathcal{F}_{0}^{\mathrm{cl}(V)}} \ll Y^{V} \cdot Q_{\mathcal{F}_{0}^{\mathrm{cl}(V)}}
$$

so there exists, by the Radon-Nikodym theorem, an $\mathcal{F}_{0}^{\mathrm{cl}(V)}$-measurable random variable $\hat{Z}_{0}^{V}$ such that

$$
P_{\mathcal{F}_{0}^{\mathrm{cl}(V)}}=\hat{Z}_{0}^{V} Y^{V} \cdot Q_{\mathcal{F}_{0}^{\mathrm{cl}(V)}}
$$

We then have, for every bounded and measurable function $h$, that

$$
\begin{aligned}
E_{P}\left[h\left(V_{0}\right) \mid \mathcal{F}_{0}^{p(V)}\right] & =E_{P}\left[h\left(V_{0}\right) \mid \mathcal{F}_{0}^{\mathrm{pa}(V)}\right]=E_{Q}\left[h\left(V_{0}\right) \tilde{Z}_{0}^{V} \mid \mathcal{F}_{0}^{\mathrm{pa}(V)}\right] \\
& =E_{Q}\left[h\left(V_{0}\right) \tilde{Z}_{0}^{V} \mid \mathcal{F}_{0}^{p(V)}\right]
\end{aligned}
$$

The contemporaneous independence at baseline and a simple monotone class argument shows that

$$
E_{P}[\eta]=E_{Z}\left[\eta \prod_{V \in \mathcal{V}} \tilde{Z}_{0}^{V}\right]
$$

for every bounded and $\mathcal{F}_{0}$-measurable random variable $\eta$.
For the follow-up, note that by Lemma 1 there exists a nonnegative and $\mathscr{P}^{\mathrm{cl}(V)}$-measurable process $\lambda^{V}$ such that

$$
E_{P}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) \lambda^{V}(s, x) U(d s, d x)\right]
$$

for every bounded and $\mathscr{P}$-measurable process $h$.
We may now form $K^{V}, Z^{V}$ and $Z$ as in Theorem 2.9 using $\lambda^{V}$ instead of $\lambda$. Following the short argument in [6], Theorem II T12, we see that any other choice of a nonnegative and $\mathscr{P}$-measurable process $\lambda$ that satisfies the previous equation would necessarily give

$$
\int_{J_{V}} \int_{0}^{T} I(\lambda(s, x) \neq \lambda^{V}(s, x)) N(d s, d x)=0, \quad P \text {-a.s. }
$$

This means that the corresponding versions of the process $K^{V}$ from (2.6) would be $P$ indistinguishable. Furthermore, this also means that the version corresponding to $\lambda^{V}$ provides an $\mathcal{F}_{t}^{\mathrm{cl}(V)}$-adapted solution of the SDE (2.10) which is $P$-indistinguishable version from $Z^{V}$.
6. An example: Controlled direct effects. We now illustrate how local independence graphs can be used to identify causal effects by an example with cancer patients. Suppose each patient is offered one of two different surgical treatments, $a_{1}$ or $a_{2}$. The patient is subject to an examination after surgery where some measurements are taken. These measurements might depend on the chosen surgical procedure and some underlying health condition that is not directly observed. After the surgery, the patient is given further treatment in order to prevent relapse. The chosen post surgery treatment strategy might depend on the surgical procedure and the measurements.

We consider a generic model for the patients in this scenario. The relevant outcomes are provided by the family of random variables $\mathcal{V}=\{W, A, L, K, B\}$. As in Section 2, we consider a probability measure $Q$ such that these variables are independent and a probability measure $P$ that governs the frequency of outcomes in the factual scenario and such that $P \ll Q$. Let the

random variable $A$ denote the choice of surgery, let $W$ denote the latent health condition, let $L$ take the value of the measurements after surgery, let $K$ denote the post surgery treatment strategy and let $B$ denote the status of relapse. We furthermore assume that $T(W)<T(A)<T(L)<T(K)<T(B)$ and that the following local independencies are satisfied:
![img-0.jpeg](img-0.jpeg)

How much of the treatment effect is due to the choice of surgical procedure alone, that is, not due to the choice of post surgery treatment? Pearl [21], Section 4.5.3, showed that it is possible to identify the controlled direct effect from surgery on the risk of relapse, even without any observations of $W$. We rephrase his argument slightly:

Proposition 2. If $\theta^{*} K$ is $\mathcal{F}_{0}^{L}$-measurable, $\theta^{*} A$ is constant, $L, W$ and $B$ are $\theta$-invariant, there exists a constant $c>0$ such that
(6.1) $P\left(A=\theta^{*} A\right)>0 \quad$ and $\quad P\left(K=\theta^{*} K \mid A=\theta^{*} A, L\right) \geq c, \quad P$-a.s
and $h$ is a bounded and measurable function, then there exists a unique counterfactual distribution $P_{\theta}$ such that $P_{\theta} \ll P$ and

$$
E_{P_{\theta}}[h(B)]=\theta^{*} E_{P}\left[\theta^{*} E_{P}[h(B) \mid \mathcal{F}_{0}^{\{L, A, K\}}\right] \mid \mathcal{F}_{0}^{A}], \quad P_{\theta} \text {-a.s. }
$$

Let $\tilde{\mathcal{F}}_{0}:=\mathcal{F}_{0}^{\{L, A, K, B\}}$ and suppose that $\tilde{Z}^{B}$ is a nonnegative and $\tilde{\mathcal{F}}_{0}$ measurable random variable and $\tilde{Z}^{L}$ is a nonnegative $\mathcal{F}_{0}^{A}$-measurable random variable such that

$$
\begin{aligned}
E_{P}[h(B) \mid \mathcal{F}_{0}^{\{A, L, K\}}] & =E_{Q}[h(B) \tilde{Z}^{B} \mid \mathcal{F}_{0}^{\{A, L, K\}}] \\
E_{P}[h(L) \mid \mathcal{F}_{0}^{A}] & =E_{Q}\left[h(L) \tilde{Z}^{L} \mid \mathcal{F}_{0}^{A}\right]
\end{aligned}
$$

$P$-a.s. Now,

$$
E_{P_{\theta}}[H]=E_{\theta Q}\left[H \tilde{Z}^{L} \tilde{Z}^{B}\right]
$$

for every $\tilde{\mathcal{F}}_{0}$-measurable random variable $H$, that is,

$$
\left.\frac{d P_{\theta}}{d \theta Q}\right|_{\tilde{\mathcal{F}}_{0}}=\tilde{Z}^{L} \tilde{Z}^{B}
$$

Proof. Note that (6.1) means that (4.1) is satisfied, that is, we obtain a counterfactual distribution $P_{\theta}$ from Theorem 1.

Whenever $h_{1}, h_{2}$ are bounded and measurable functions, then

$$
\begin{aligned}
E_{P_{\theta}}\left[h_{1}(B) h_{2}(L)\right] & =E_{P}\left[W_{0} h_{1}(B) h_{2}(L)\right] \\
& =E_{P}\left[W_{0} E_{P}\left[h(B)\left|\mathcal{F}_{0}^{A, K, L}\right| h(L)\right]\right. \\
& =E_{P_{\theta}}\left[E_{P}\left[h(B)\left|\mathcal{F}_{0}^{A, K, L}\right| h(L)\right]\right. \\
& \left.=E_{P_{\theta}}\left[\theta^{*} E_{P}\left[h(B)\left|\mathcal{F}_{0}^{A, K, L}\right| h(L)\right]\right] \quad \text { by }(4.21) .\right.
\end{aligned}
$$

This shows that $E_{P_{\theta}}\left[h_{1}(B)\left|\mathcal{F}_{0}^{L}\right|=\theta^{*} E_{P}\left[h_{1}(B)\left|\mathcal{F}_{0}^{\{A, L, K\}}\right|\right] P_{\theta}$-a.s. Moreover, note that

$$
\begin{aligned}
E_{P_{\theta}}\left[h_{2}(L)\right] & =E_{P_{\theta}}\left[\theta^{*} E_{P}\left[h_{2}(L)\left|\mathcal{F}_{0}^{A, W}\right|\right]\right] \\
& =E_{P_{\theta}}\left[\theta^{*} E_{P}\left[h_{2}(L)\left|\mathcal{F}_{0}^{A}\right|\right]\right] \\
& =\theta^{*} E_{P}\left[h_{2}(L)\left|\mathcal{F}_{0}^{A}\right|\right, \quad P_{\theta} \text {-a.s. }
\end{aligned}
$$

Combining these computations, we obtain

$$
\begin{aligned}
E_{P_{\theta}}[h(B)] & =E_{P_{\theta}}\left[E_{P_{\theta}}\left[h(B)\left|\mathcal{F}_{0}^{L}\right|\right]\right. \\
& =E_{P_{\theta}}\left[\theta^{*} E_{P}\left[h(B)\left|\mathcal{F}_{0}^{L, A, K}\right|\right]\right] \\
& \left.=\theta^{*} E_{P}\left[\theta^{*} E_{P}\left[h(B)\left|\mathcal{F}_{0}^{L, A, K}\right|\right| A\right]\right.
\end{aligned}
$$

$P_{\theta}$-a.s. for every bounded and measurable function $h$.
To see that equation (6.3) is satisfied, note that by the monotone class lemma,

$$
\begin{aligned}
E_{P_{\theta}}[H] & =\theta^{*} E_{P}\left[\theta^{*} E_{P}\left[H\left|\mathcal{F}_{0}^{\{A, L, K\}}\right|\right| \mathcal{F}_{0}^{A}\right] \\
& =\theta^{*} E_{Q}\left[\theta^{*} E_{Q}\left[H \tilde{Z}^{B}\left|\mathcal{F}_{0}^{\{A, L, K\}}\right| \tilde{Z}^{L}\left|\mathcal{F}_{0}^{A}\right|\right]\right. \\
& =E_{\theta Q}\left[E_{Q}\left[H \tilde{Z}^{B}\left|\mathcal{F}_{0}^{\{A, L, K\}}\right| \tilde{Z}^{L}\right]\right. \\
& =E_{\theta Q}\left[H \tilde{Z}^{B} \tilde{Z}^{L}\right] .
\end{aligned}
$$

If we consider actions $\theta_{1}$ and $\theta_{2}$ such that $\theta_{i}^{*} A=a_{i}$ and $\theta_{1}^{*} K=\theta_{2}^{*} K, Q$-a.s. then the relative direct risk of relapse is given by

$$
\frac{P_{\theta_{1}}(B=1)}{P_{\theta_{2}}(B=1)}=\frac{E_{P}\left[\theta_{1}^{*} E_{P}\left[h(B)\left|\mathcal{F}_{0}^{\{A, L, K\}}\right|\right| A=a_{1}\right]}{E_{P}\left[\theta_{2}^{*} E_{P}[h(B)\left|\mathcal{F}_{0}^{\{A, L, K\}}\right|\right| A=a_{2}\right]}
$$

6.1. Incomplete observations and time dependent treatments. We have not yet taken into account that the patient observations could be censored during the follow-up period. There might be several reasons for such censoring. This might be due to the end of study period, drop-out due to the

underlying health or because of other reasons. The risk of having an observed relapse will typically be smaller than the risk of having a relapse. We will work in the framework of event history analysis in order to provide a reasonable effect measure subject to such incomplete observations. This will also allow us to consider time dependent post surgery strategies $K$.
6.1.1. A dynamic model. We proceed with the previous setup, but where $B$ and $K$ are represented by processes and every patient may be censored during the follow-up period. The factors $A, L$ and $W$ are as in the previous example. $B$ is represented by a counting process that jumps from 0 to 1 at the time of the event. The censoring of the individual is represented by a counting process $C$ that jumps from 0 to 1 at the time of censoring.

We suppose that the baseline treatment $A$ may be of two different types; hence $A$ takes value in $\{0,1\}$. Moreover, we suppose that additional postsurgery treatment is given to the patient at the jumps of the counting process $K$. This treatment may be given recursively, but only at a series of $\mathcal{F}_{t^{-}}$ predictable times; that is, (4.5) must be satisfied. We furthermore suppose that $\theta^{*} K_{s}$ is constant for every $s P$-a.s. and suppose that $B_{0}=0, K_{0}=0$ and $C_{0}=0 P$-a.s.

Let $T_{1}, \ldots, T_{n}$ denote the potential post-treatment times, and let $U_{t}^{K}:=$ $\sum_{i} I\left(T_{i} \leq t\right)$. The counting process $U^{K}$ is predictable and $\nu_{t}^{K}=\int_{0}^{t} P\left(\Delta K_{s} \neq\right.$ $\left.0 \mid \mathcal{F}_{s-}\right) d U_{s}^{K}$. By Theorem 2, we see that there exists a counterfactual distribution if $P\left(A=\theta^{*} A\right)>0$ and there exist $c_{1}, c_{2}>0$ such that

$$
1-c_{1} P\left(\Delta K_{s}=0 \mid \mathcal{F}_{s-}\right) \leq \Delta \theta^{*} K_{s} \leq c_{2} P\left(\Delta K_{s} \neq 0 \mid \mathcal{F}_{s-}\right)
$$

for every $s P$-a.s.
We suppose that the following local independence graph is satisfied with respect to the factual distribution $P$ :
![img-1.jpeg](img-1.jpeg)

Especially, this means that the short-term behavior of the censoring may not depend on other variables than $A$.
6.1.2. Restriction to Aalen's additive hazard model. If we assume that the event process satisfies Aalens's additive hazard model [2], it is actually possible to identify, and also consistently estimate the direct effect from

surgery. Every outcome after the time of censoring is supposed to be unobserved. In addition, we assume that we are not able to observe the variable $W$.

We consider the censored process

$$
\tilde{B}_{t}:=B_{0}+\int_{0}^{t}\left(1-C_{s-}\right) d B_{s}
$$

and let $\tilde{\mathcal{F}}_{t}$ denote the filtration that is generated by $A, K, L, C$ and $B$. Furthermore let $Y_{t}$ denote the factual "at-risk" process, that is, $Y_{t}=I\left(B_{t-}=\right.$ $\left.C_{t-}=0\right)$. We assume that there exist measurable and bounded functions $\psi^{0}, \psi^{K}, \psi^{L}$ and $\psi^{A}$ such that

$$
E_{P}\left[\int_{0}^{T} h_{s} d \tilde{B}_{s}\right]=E_{P}\left[\int_{0}^{T} h_{s} Y_{s}\left(\psi_{s}^{0}+A \psi_{s}^{A}+L \psi_{s}^{L}+\tilde{K}_{s-} \psi_{s}^{K}\right) d s\right]
$$

for every bounded and $\tilde{\mathcal{F}}_{t}$-predictable process $h$.
We are now able to identify the controlled direct effect from surgery. Note that this is just a slight variation of the model considered in [19].

Lemma 2. If $\sigma^{1}$ and $\sigma^{2}$ are two $\mathcal{F}_{0}^{A} \vee \mathcal{F}_{t}^{\tilde{B}}$-predictable processes such that

$$
\begin{aligned}
E_{P}\left[L \int_{0}^{T} h_{t} Y_{t} \exp \left(\int_{0}^{t} K_{-s} \psi_{s}^{K} d s\right) d t\right] & =E_{P}\left[\int_{0}^{T} h_{t} \sigma_{t}^{1} d t\right] \\
E_{P}\left[\int_{0}^{T} h_{t} Y_{t} \exp \left(\int_{0}^{t} K_{-s} \psi_{s}^{K} d s\right) d t\right] & =E_{P}\left[\int_{0}^{T} h_{t} \sigma_{t}^{2} d t\right]
\end{aligned}
$$

for every $\mathcal{F}_{0}^{A, B, C}$-predictable and bounded process $h$, then

$$
\begin{aligned}
& E_{P_{\theta}}\left[\int_{0}^{T} g_{t} Y_{t} d B_{t}\right] \\
& \quad=E_{P_{\theta}}\left[\int_{0}^{T} g_{t} Y_{t}\left(\psi_{t}^{0}+\psi_{t}^{L} \theta^{*} \frac{\sigma_{t}^{1}}{\sigma_{t}^{2}}+\theta^{*} A \psi_{t}^{A}+\theta^{*} K_{t-} \psi_{t}^{K}\right) d t\right]
\end{aligned}
$$

for every $\mathcal{F}_{t}^{B, C}$-predictable and bounded process $g$.
Sketch of Proof. By Theorem 1, there exist an $\mathcal{F}_{0}^{A}$-measurable random variable $W_{0}^{1}$ and an $\mathcal{F}_{0}^{A, K, L}$-measurable random variable $W_{0}^{2}$ such that

$$
\left.\frac{d P_{\theta}\right|_{\mathcal{F}_{0}}}{\left.d P\right|_{\mathcal{F}_{0}}}=W_{0}^{1} W_{0}^{2} \quad \text { and } \quad \frac{d P_{\theta} \right|_{\mathcal{F}_{0}^{L, A}}}{\left.d P\right|_{\mathcal{F}_{0}^{L, A}}}=W_{0}^{1}
$$

If $H_{1}$ is $\mathcal{F}_{0}^{L}$-measurable, $\tilde{H}_{1}:=E_{P}\left[H_{1} \mid \mathcal{F}_{0}^{A}\right]$ and $H_{2}$ is $\mathcal{F}_{0}^{A}$-measurable, then

$$
E_{P_{\theta}}\left[H_{1} H_{2}\right]=E_{P}\left[H_{1} H_{2} W_{0}^{1}\right]=E_{P}\left[\tilde{H}_{1} H_{2} W_{0}^{1}\right]=E_{P_{\theta}}\left[\tilde{H}_{1} H_{2}\right]
$$

Similarly, let $h$ be a bounded and $\tilde{\mathcal{F}}_{\mathrm{f}}$-predictable process, and let $\mu_{s}^{B}:=$ $\tilde{Y}_{s}\left(\psi_{s}^{0}+A \psi_{s}^{A}+L \psi_{s}^{L}+K_{s-} \psi_{s}^{K}\right)$, and note that

$$
\begin{aligned}
E_{P_{\theta}}\left[\int_{0}^{T} h_{s} d B_{s}\right] & =E_{P}\left[\int_{0}^{T} h_{s} d B_{s} W_{T}\right] \\
& =E_{P}\left[\int_{0}^{T} h_{s} W_{s-} d B_{s}\right]+E_{P}\left[\int_{0}^{T} h_{s} d[B, W]_{s}\right] \\
& =E_{P}\left[\int_{0}^{T} h_{s} W_{s-} d B_{s}\right] \\
& =E_{P}\left[\int_{0}^{T} h_{s} W_{s-} \mu_{s}^{B} d s\right] \\
& =E_{P}\left[\int_{0}^{T} h_{s} \mu_{s}^{B} d s W_{T}\right] \quad \text { by [14], Proposition I } 3.14 \\
& =E_{P_{\theta}}\left[\int_{0}^{T} h_{s} \mu_{s}^{B} d s\right]
\end{aligned}
$$

One can show that there exists an intermediate probability measure $\tilde{P}$ on $\tilde{\mathcal{F}}_{T}$ such that:

$$
P_{\theta} \mid_{\tilde{\mathcal{F}}_{T}} \ll \tilde{P} \ll P_{\tilde{\mathcal{F}}_{T}}
$$

(2) For every bounded and Borel-measurable function $h$ :

- $E_{\tilde{P}}[h(A)]=h\left(\theta^{*} A\right), \tilde{P}$-a.s.;
- $E_{\tilde{P}}\left[h(L) \mid \mathcal{F}_{0}^{A},\right]=E_{P}\left[h(L) \mid \mathcal{F}_{0}^{A}\right]$;
- $E_{\tilde{P}}\left[h\left(K_{0}\right) \mid \mathcal{F}_{0}^{A, L}\right]=E_{P}\left[h\left(K_{0}\right) \mid \mathcal{F}_{0}^{A, L}\right]$;
- $E_{\tilde{P}}\left[h\left(B_{0}\right) \mid \mathcal{F}_{0}^{A, L, K}\right]=E_{P}\left[h\left(B_{0}\right) \mid \mathcal{F}_{0}^{A, L, K}\right]$.
(3) Whenever $h$ is a bounded and $\tilde{\mathcal{F}}_{\mathrm{f}}$-predictable process, then:
- 

$$
E_{\tilde{P}}\left[\int_{0}^{T} h_{s} d B_{s}\right]=E_{\tilde{P}}\left[\int_{0}^{T} h_{s} \mu_{s}^{B} d s\right]
$$

- if $\mu^{K}$ and $\mu^{C}$ are $\tilde{\mathcal{F}}_{\mathrm{f}}$-predictable processes such that

$$
\begin{aligned}
& E_{P}\left[\int_{0}^{T} h_{s} d K_{s}\right]=E_{P}\left[\int_{0}^{T} h_{s} \mu_{s}^{K} d U_{s}^{K}\right] \\
& E_{P}\left[\int_{0}^{T} h_{s} d C_{s}\right]=E_{P}\left[\int_{0}^{T} h_{s} \mu_{s}^{C} d U_{s}^{C}\right]
\end{aligned}
$$

then

$$
\begin{aligned}
& E_{\tilde{P}}\left[\int_{0}^{T} h_{s} d K_{s}\right]=E_{\tilde{P}}\left[\int_{0}^{T} h_{s} \mu_{s}^{K} d U_{s}^{K}\right] \\
& E_{\tilde{P}}\left[\int_{0}^{T} h_{s} d C_{s}\right]=E_{\tilde{P}}\left[\int_{0}^{T} h_{s} \mu_{s}^{C} d U_{s}^{C}\right]
\end{aligned}
$$

Note that by [13], Proposition 4.3, there exists an $\mathcal{F}_{t}^{A, L, B}$-adapted $\tilde{P}$-martingale $\Xi$ such that

$$
\Xi_{T}=\left.\frac{d P_{\theta}}{\mathcal{F}_{T}^{A, L, B, C}}\right|_{\mathcal{F}_{T}^{A, L, B, C}}, \quad[B, \Xi]=0
$$

and

$$
Y \Xi_{-}=Y \exp \left(-\int_{0}^{\cdot} \theta^{*} K_{r} \psi_{r}^{K} d r\right)
$$

Bayes's formula with predictable projections shows that

$$
E_{\tilde{P}}\left[L \int_{0}^{T} Y_{s} h_{s} d s\right]=E_{\tilde{P}}\left[\int_{0}^{T} Y_{s} h_{s} \frac{\sigma_{s}^{1}}{\sigma_{s}^{2}} d s\right]
$$

for every bounded and $\mathcal{F}_{t}^{A, B, C}$-predictable process $h$. Now,

$$
\begin{aligned}
E_{P_{\theta}}\left[\int_{0}^{T} L h_{s} Y_{s} d s\right] & =E_{\tilde{P}}\left[\int_{0}^{T} L h_{s} Y_{s} d s \Xi_{T}\right] \\
& =E_{\tilde{P}}\left[\int_{0}^{T} \Xi_{s-} L h_{s} Y_{s} d s\right] \\
& =E_{\tilde{P}}\left[\int_{0}^{T} \Xi_{s-} h_{s} Y_{s} \frac{\sigma_{s}^{1}}{\sigma_{s}^{2}} d s\right] \quad \text { by }(6.10) \\
& =E_{\tilde{P}}\left[\int_{0}^{T} h_{s} Y_{s} \frac{\sigma_{s}^{1}}{\sigma_{s}^{2}} d s \Xi_{T}\right] \\
& =E_{P_{\theta}}\left[\int_{0}^{T} h_{s} Y_{s} \frac{\sigma_{s}^{1}}{\sigma_{s}^{2}} d s\right]
\end{aligned}
$$

for every bounded $\mathcal{F}_{t}^{A, B, C}$-predictable process $h$, which implies that (6.9) holds.
6.1.3. Consistency of the modified sequential $G$-estimator. We are now able to show that the modified sequential $G$-estimator suggested in [19] is uniformly consistent, also when we consider a time-dependent mediating treatment $K$. Let $\theta_{1}, \theta_{2}$ be two actions as in the previous proposition, but where $\theta_{1}^{*} A=0$ and $\theta_{2}^{*} A=1$ and consider corresponding $\mathcal{F}_{t}^{A, B, C}$-predictable processes $\gamma^{1}$ and $\gamma^{2}$ as the fractions in (6.11). Furthermore, we assume that

our observations consist of the event histories for $n$ independent equally distributed individuals, following the current generic model. We will also slightly misuse the notation and let $N$, from now on, denote the corresponding counting process that is aggregated over the $n$ independent individuals.

Lemma 3. Let $\widehat{\Psi}^{0}, \widehat{\Psi}^{A}, \widehat{\Psi}^{L}$ and $\widehat{\Psi}^{K}$ denote the usual additive regression estimators of Aalen, let $\tilde{Y}:=Y_{t}^{B} Y_{t}^{C}$ and define

$$
\begin{aligned}
& \tilde{M}_{t}:=N_{t}^{B}-\int_{0}^{t} \mu_{s}^{B} d s, \bar{\gamma}_{t}:=\binom{\gamma_{t}^{1}}{\gamma_{t}^{2}}, \quad \Gamma_{t}:=\binom{\Psi_{t}^{0}+\int_{0}^{t} \rho_{s}^{1} d \Psi_{s}^{L}}{\Psi_{t}^{A}+\int_{0}^{t} \rho_{s}^{2}-\rho_{s}^{1} d \Psi_{s}^{L}}, \\
& \widehat{H}_{t}:=\operatorname{diag}\binom{\tilde{Y}_{t}^{1} \exp \left(\int_{0}^{t} K_{s-}^{1} d \widehat{\Psi}_{s}^{K}\right)}{\tilde{Y}_{t}^{n} \exp \left(\int_{0}^{t} K_{s-}^{n} d \widehat{\Psi}_{s}^{K}\right)}, \\
& H_{t}:=\operatorname{diag}\binom{\tilde{Y}_{t}^{1} \exp \left(\int_{0}^{t} K_{s-}^{1} d \Psi_{s}^{K}\right)}{\tilde{Y}_{t}^{n} \exp \left(\int_{0}^{t} K_{s-}^{n} d \Psi_{s}^{K}\right)}, \\
& Z_{t}:=\tilde{Y}_{t} \cdot\left(\begin{array}{ll}
1 & A_{1} \\
\vdots & \\
1 & A_{n}
\end{array}\right), \quad Z_{s-}^{\widehat{H}}:=\left(Z_{s-}^{T} \widehat{H}_{s-} Z_{s-}\right)^{-1} Z_{s-}^{T} \widehat{H}_{s-}, \\
& Z_{s-}^{H}:=\left(Z_{s-}^{T} H_{s-} Z_{s-}\right)^{-1} Z_{s-}^{T} H_{s-} \quad \text { and } \\
& \widehat{\Gamma}_{t}:=\int_{0}^{t} Z_{s-}^{\widehat{H}} d N_{s}-\int_{0}^{t} Z_{s-}^{\widehat{H}} K_{s-} d \widehat{\Psi}_{s}^{K} .
\end{aligned}
$$

We have that

$$
\lim _{n \rightarrow \infty} P\left(\sup _{t \leq T}\left|\widehat{\Gamma}_{t}-\Gamma_{t}\right| \geq \delta\right)=0
$$

for every $\delta>0$.
Proof. Note that

$$
\widehat{\Gamma}_{t}-\Gamma_{t}=\int_{0}^{t} Z_{s-}^{\widehat{H}} d N_{s}-\int_{0}^{t} Z_{s-}^{\widehat{H}} K_{s-} d \widehat{\Psi}_{s}^{K}-\Gamma_{t}
$$

$$
=\int_{0}^{t} Z_{s-}^{\widehat{H}}-Z_{s-}^{H} d N_{s}+\int_{0}^{t}\left(Z_{s-}^{H}-Z_{s-}^{\widehat{H}}\right) K_{s-} d \Psi_{s}^{K}
$$

$$
\begin{aligned}
& +\int_{0}^{t} Z_{s-}^{H} d \tilde{M}_{s}+\int_{0}^{t} Z_{s-}^{\widetilde{H}} K_{s-} d\left(\Psi_{s}^{K}-\widetilde{\Psi}_{s}^{K}\right) \\
& +\int_{0}^{t} Z_{s-}^{H}\left(Z_{s-} \quad L_{s-}\right) d\left(\begin{array}{c}
\Psi_{s}^{0} \\
\Psi_{s}^{A} \\
\Psi_{s}^{L}
\end{array}\right)-\Gamma_{t}
\end{aligned}
$$

Let

$$
V=\left(\begin{array}{cc}
1 & 0 \\
-1 & 1
\end{array}\right)
$$

We have that $V^{T} Z_{s-}^{T} H_{s-} Z_{s-} V=S_{t-}$ where $S_{t-}$ is a $2 \times 2$-diagonal matrix. Moreover, $\left(Z_{s-}^{T} H_{s-} Z_{s-}\right)^{-1}=V S_{t-} V^{T}$.

Note that $\left|\int_{0}^{\cdot} Z_{s-}^{H} d \tilde{M}_{s}\right|_{2}^{2}$ is Lenglart dominated by $\operatorname{Tr}\left\langle\int_{0}^{\cdot} Z_{s-}^{H} d \tilde{M}_{s}\right\rangle$ and

$$
\begin{aligned}
& \operatorname{Tr}\left\langle\int_{0}^{\cdot} Z_{s-}^{H} d \tilde{M}_{s}\right\rangle_{T} \\
& \quad=\int_{0}^{T} \operatorname{Tr}\left(Z_{s-}^{T} H_{s-} Z_{s-}\right)^{-1} Z_{s-}^{T} H_{s-} \operatorname{diag} \mu H_{s-} Z_{s-}\left(Z_{s-}^{T} H_{s-} Z_{s-}\right)^{-1} d s \\
& \quad \leq \int_{0}^{T} \operatorname{Tr}\left(Z_{s-}^{T} H_{s-} Z_{s-}\right)^{-1}\left\|\operatorname{diag} \mu H_{s-}\right\|_{\mathrm{op}} d s
\end{aligned}
$$

which converges in probability to 0 . By Lenglart's inequality [14], we obtain that $\int_{0}^{\cdot} Z_{s-}^{H} d \tilde{M}_{s}$ converges uniformly to 0 in probability with respect to $P$.

Since

$$
\lim _{\delta \rightarrow \infty} P\left(\sup _{s}\left|Z_{s} K_{s}\right| \geq \delta\right)=0 \quad \text { and } \quad \lim _{\delta \rightarrow \infty} P\left(\sup _{s}\left|\widetilde{Z}_{s} K_{s}\right| \geq \delta\right)=0
$$

and $\widetilde{\Psi}^{K}$ converges uniformly in probability to $\Psi^{K}$, we also have that

$$
\int_{0}^{t} Z_{s-}^{\widetilde{H}} K_{s-} d\left(\Psi_{s}^{K}-\widetilde{\Psi}_{s}^{K}\right) \quad \text { and } \quad \int_{0}^{t}\left(Z_{s-}^{H}-Z_{s-}^{\widetilde{H}}\right) K_{s-} d \Psi_{s}^{K}
$$

converge uniformly in probability to 0 w.r.t. $P$. This shows that (6.15) converges uniformly in probability to 0 w.r.t. $P$ as well.

We have that

$$
Z_{s-}^{H} L_{s-}=V S_{s-}^{-1}\left(\begin{array}{c}
\sum_{i=1}^{n} H_{s-}^{i} L_{s-}^{i}\left(1-A^{i}\right) \\
\sum_{i=1}^{n} H_{s-}^{i} L_{s-}^{i} A^{i}
\end{array}\right)=V\left(\begin{array}{c}
\frac{\sum_{i=1}^{n} H_{s-}^{i} L_{s-}^{i}\left(1-A^{i}\right)}{\sum_{i=1}^{n} H_{s-}^{i}\left(1-A^{i}\right)} \\
\frac{\sum_{i=1}^{n} H_{s-}^{i} L_{s-}^{i} A^{i}}{\sum_{i=1}^{n} H_{s-}^{i} A^{i}}
\end{array}\right)
$$

The law of large numbers implies that $Z_{s-}^{H} L_{s-}$ converges in $P$-probability to $V \bar{\gamma}(s)$. Now, (6.16) equals

$$
\int_{0}^{t} Z_{s-}^{H} L_{s-}-V \gamma(s) d \Psi_{s}^{L}
$$

and

$$
\begin{aligned}
E_{P} & {\left[\sup _{t}\left|\int_{0}^{t} Z_{s-}^{H} L_{s-}-V \gamma(s) d \Psi_{s}^{L}\right|\right] } \\
& \leq \int_{0}^{T} E_{P}\left[\left|\left(Z_{s-}^{H} L_{s-}-V \gamma(s-)\right)\right|\right]\left|\psi_{s}^{L}\right| d s
\end{aligned}
$$

Therefore (6.16) converges uniformly in probability w.r.t. $P$.
A computation shows that $\left|\int_{0}^{\cdot} Z_{s-}^{\widetilde{H}}-Z_{s-}^{H} d N_{s}\right|_{1}$ is Lenglart dominated by

$$
\begin{gathered}
\|V\|_{1} \int_{0} \sum_{j}\left|\frac{\widehat{H}_{s-}^{j}\left(1-A_{j}\right) \mu_{s}^{j}}{\sum_{i} \widehat{H}_{s-}^{i}\left(1-A_{i}\right)}-\frac{H_{s-}^{j}\left(1-A_{j}\right) \mu_{s}^{j}}{\sum_{i} H_{s-}^{i}\left(1-A_{i}\right)}\right| \\
+\left|\frac{\widehat{H}_{s-}^{j} A_{j} \mu_{s}^{j}}{\sum_{i} \widehat{H}_{s-}^{i} A_{i}}-\frac{H_{s-}^{j} A_{j} \mu_{s}^{j}}{\sum_{i} H_{s-}^{i} A_{i}}\right| d s
\end{gathered}
$$

This process converges uniformly in probability to 0 , so we see that (6.14) also converges uniformly in probability to 0 . This means that $\widehat{\Gamma}-\Gamma$ converges uniformly in probability to 0 , so $\widehat{\Gamma}$ actually converges to $\Gamma$ in the similar sense.

The cumulative $P_{\theta_{t}}$-hazard of $\hat{B}$ is given by

$$
\Lambda_{t}^{\theta_{t}}=\int_{0}^{t} \psi_{s}^{0}+\theta_{t}^{*} A \psi_{s}^{A}+\theta_{t}^{*} K_{s} \psi_{s}^{K}+\gamma_{s} \psi_{s}^{L} d s
$$

Since stochastic integrals are continuous with respect to uniform convergence on compacts in probability, we see that

$$
\lim _{\delta \rightarrow 0} P\left(\sup _{t}\left|\int_{0}^{t}\left(1, \quad \theta_{i}^{*} A, \quad \theta_{i}^{*} K_{s-}\right)\binom{d \widehat{\Gamma}_{s}}{d \widehat{\Psi}_{s}^{K}}-\Lambda_{t}^{\theta_{t}}\right| \geq \delta\right)=0
$$

that is, we obtain a consistent estimator of $\Lambda_{t}^{\theta_{t}}$. A consistent estimator for the controlled direct effect of $A$ on $B$ is given by the second component of $\widehat{\Gamma}$.
7. Discussion. The primary concern in this paper is the possibility of estimating parameters for the counterfactual situation from the observational data, given that the counterfactual model is correct. This comes mainly down to whether the counterfactual probability is absolutely continuous with respect to the factual probability and whether the counterfactual parameters of interest are identifiable. The previously mentioned related works by Arjas and Parner, [3] and [4], construct counterfactual probability distributions by piecing stochastic intervals together as in [13], Section 3. Unlike Parner and Arjas, we take a more martingale oriented approach, also based on the seminal paper [13]. This enables us to apply directly already well-established

methods from stochastic analysis and martingale theory. In fact, surprisingly much causal inference can be well understood in terms of martingale measures, Bayes's rule and Girsanov's theorem. This approach translates directly the problem about data re-weighting into a thoroughly studied problem in the literature, that is, whether the stochastic exponential of a local martingale defines a martingale, see [17] and [15].

Another difference from the work of Arjas and Parner is that we consider an explicit intervention in terms of a transformation $\theta$ on sample space. While not being absolutely necessary, it still provides additional clarification, as it makes the notion of counterfactual outcomes more explicit, or perhaps even demystified. The notation do $(X=x)$, [21], is simply interpreted as the measurable transformation on the sample space that forces every outcome of $X$ into $x$ and leaves the remaining observations unchanged. When the action becomes more complex than just forcing a variable into a fixed value, this interpretation becomes even more appealing.

The introduction of the transformation $\theta$ sheds some light on another aspect: One may in fact think of a causal inference problem as a stochastic control problem, or a decision problem, where the assumptions about the model are kept as modest as possible. The main objective in stochastic control theory is to find an optimal intervention strategy and compute the corresponding expected payoff. Causal inference appears as a special case of this, in the sense that there one mostly considers only one intervention strategy, namely the transformation $\theta$, and aims to compute the expected payoff.

One is often confronted with latent factors in epidemiological settings. This lack of information typically yields nonidentifiable effects. In special situations, one can use graphical arguments to ensure identifiability of counterfactual parameters and also provide exact formulas for these. Such examples are the back-door formula, front-door formula and sequential back-door formula [21], Section 3.3.1, 3.3.2, 4.4.3 and [11]. We show that we may take advantage of the local independence graphs to identify causal effects in event-history analysis.

When the counterfactual effect is possibly unidentifiable, one may try to compute upper and lower bounds for this. This can also be thought of as a control problem where "the nature" is allowed to control the latent factors in order to maximize or minimize counterfactual effects. This corresponds to an optimization problem under constraints. The latent variables may only be altered in such a way that the observable factors maintain the same joint distribution and also such that some given directed graph constantly defines a local independence graph. Let $\mathcal{S}$ denote the set of counterfactual distributions corresponding to these constraints. The "causal effect" would then be sandwiched by $\inf _{P^{\prime} \in \mathcal{S}} E_{P^{\prime}}[\eta] \leq E_{P_{\theta}}[\eta] \leq \sup _{P^{\prime \prime} \in \mathcal{S}} E_{P^{\prime \prime}}[\eta]$.

The set $\mathcal{S}$ may have a somewhat complicated geometry. If one instead considers the convex hull, we obtain other, not necessarily, tight bounds.

$$
\inf _{P^{\prime} \in \operatorname{conv}(\mathcal{S})} E_{P^{\prime}}[\eta] \leq E_{P_{\theta}}[\eta] \leq \sup _{P^{\prime \prime} \in \operatorname{conv}(\mathcal{S})} E_{P^{\prime \prime}}[\eta]
$$

These bounds may be computed by allready developed linear programing techniques. This approach was for instance taken in [5], but is likely to generalize to more complicated continuous-time scenarios as well.

# APPENDIX 

## Uniqueness of counterfactual distributions.

Lemma A.1. There exists at most one counterfactual distribution $P_{\theta}$ on $\mathcal{F}_{0}$ that imposes contemporaneously independent outcomes.

Proof. Let $T_{1}, \ldots, T_{m}$ be an enumeration of $\{T(V)\}_{V \in \mathcal{V}}$ such that $j<k$ implies $T_{j}<T_{k}$.

Assume that $P^{\prime}$ and $P^{\prime \prime}$ are two counterfactual distributions that have contemporaneously independent outcomes and $\eta$ is an $\mathcal{F}_{0}^{V_{k}}$-measurable random variable. Let $\left\{X_{i}\right\}_{i}$ be an enumeration of $\left\{V \in \mathcal{X} \mid T(V)=T_{1}\right\}$ and let $\left\{A_{j}\right\}_{j}$ be an enumeration of $\left\{V \in \mathcal{A} \mid T(V)=T_{1}\right\}$. Whenever $\left\{h_{i}\right\}_{i}$ and $\left\{g_{j}\right\}_{j}$ are two families of bounded and measurable functions, then

$$
\begin{aligned}
E_{P^{\prime}}\left[\prod_{i} h_{i}\left(X_{i}\right) \prod_{j} g_{l}\left(A_{j}\right)\right] & =E_{P^{\prime}}\left[\prod_{i} h_{i}\left(X_{i}\right)\right] E_{P^{\prime}}\left[\prod_{j} g_{j}\left(A_{j}\right)\right] \\
& =\prod_{i} E_{P^{\prime}}\left[h_{i}\left(X_{i}\right)\right] E_{P^{\prime}}\left[\prod_{j} g_{j}\left(A_{j}\right)\right] \\
& =\prod_{i} E_{P^{\prime \prime}}\left[h_{i}\left(X_{i}\right)\right] E_{P^{\prime \prime}}\left[\prod_{j} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime \prime}}\left[\prod_{i} h_{i}\left(X_{i}\right)\right] E_{P^{\prime \prime}}\left[\prod_{j} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime \prime}}\left[\prod_{i} h_{i}\left(X_{i}\right) \prod_{j} g_{j}\left(A_{j}\right)\right]
\end{aligned}
$$

This shows that if $\eta$ is a bounded random variable that only depends on the information at $T_{1}$, then $E_{P^{\prime}}[\eta]=E_{P^{\prime \prime}}[\eta]$. We continue with an induction argument and assume that $E_{P^{\prime}}[\eta]=E_{P^{\prime \prime}}[\eta]$ for every bounded and random variable $\eta$ that only depends on $\left\{V \in \mathcal{V} \mid T(V)<T_{k}\right\}$ and aim to prove that this also holds if $\eta$ depends on the information at time $T_{k}$. Let $\left\{X_{i}\right\}_{i}$ be

an enumeration of $\left\{V \in \mathcal{X} \mid T(V)=T_{k}\right\}$, and let $\left\{A_{j}\right\}_{j}$ be an enumeration of $\left\{V \in \mathcal{A} \mid T(V)=T_{k}\right\}$. Whenever $\left\{h_{i}\right\}_{i}$ and $\left\{g_{j}\right\}_{j}$ are two families of bounded and measurable functions, then

$$
\begin{aligned}
E_{P^{\prime}} & {\left[\eta \prod_{i} h_{i}\left(X_{i}\right) \prod_{j} g_{j}\left(A_{j}\right)\right] } \\
& =E_{P^{\prime}}\left[\eta E_{P^{\prime}}\left[\prod_{i} h_{i}\left(X_{i}\right) \mid \mathcal{F}_{0}^{p\left(V_{1}\right)}\right] \prod_{j} \theta^{*} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime}}\left[\eta \prod_{i} E_{P^{\prime}}\left[h_{i}\left(X_{i}\right) \mid \mathcal{F}_{0}^{p\left(V_{1}\right)}\right] \prod_{j} \theta^{*} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime \prime}}\left[\eta \prod_{i} E_{P^{\prime \prime}}\left[h_{i}\left(X_{i}\right) \mid \mathcal{F}_{0}^{p\left(V_{1}\right)}\right] \prod_{j} \theta^{*} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime \prime}}\left[\eta E_{P^{\prime \prime}}\left[\prod_{i} h_{i}\left(X_{i}\right) \mid \mathcal{F}_{0}^{p\left(V_{1}\right)}\right] \prod_{j} \theta^{*} g_{j}\left(A_{j}\right)\right] \\
& =E_{P^{\prime \prime}}\left[\eta \prod_{i} h_{i}\left(X_{i}\right) \prod_{j} g_{j}\left(A_{j}\right)\right]
\end{aligned}
$$

This proves the induction hypothesis, that is, $E_{P^{\prime}}[\eta]=E_{P^{\prime \prime}}[\eta]$ whenever $\eta$ depends on $\left\{V \in \mathcal{A} \mid T(V) \leq T_{k}\right\}$.

THEOREM 4. There exists at most one probability measure on $\mathcal{F}_{T}$ that simultaneously satisfies (3.4), (3.5), (3.8) and (3.9).

Proof. Recall definition (4.16). (3.8) and (3.9) imply that
(A.1) $E_{P_{\theta}}\left[\int_{J} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P_{\theta}}\left[\int_{J} \int_{0}^{T} h(s, x) \nu^{\theta}(d s, d x)\right]$.

Now [13], Theorem 3.4, implies that there exists at most one probability measure on $\mathcal{F}_{T}$ that coincides with $P_{\theta}$ on $\mathcal{F}_{0}$ and satisfies (A.1).

# Dual predictable projections. 

Lemma A.2. Let $U$ denote the dual predictable projection of $N$ with respect to $Q$ onto the filtration $\mathcal{F}_{t}$.
(1) If $h$ is a bounded and $\mathscr{P}^{V}$ measurable processes, then

$$
\int_{J_{V}} \int_{0} h(s, x) U(d s, d x)
$$

defines an $\mathcal{F}_{t}^{V}$-predictable process of finite variation.

(2) If $h$ and $h^{\prime}$ are bounded and $\mathscr{P} \otimes \mathcal{J}$ measurable processes, then

$$
\begin{aligned}
& {\left[\int_{J_{V}} \int_{0} h(s, x) U(d s, d x), \int_{J_{V^{\prime}}} \int_{0} h^{\prime}(s, x) U(d s, d x)\right]=0} \\
& {\left[\int_{J_{V}} \int_{0} h(s, x) U(d s, d x), \int_{J_{V^{\prime}}} \int_{0} h^{\prime}(s, x) N(d s, d x)\right]=0}
\end{aligned}
$$

$Q$-a.s. whenever $V \neq V^{\prime}$.
(3) There exists a nonnegative and $\mathscr{P} \otimes \mathcal{J}$-measurable process $\lambda$ such that

$$
E_{P}\left[\int_{J} \int_{0}^{T} h(s, x) N(d s, d x)\right]=E_{P}\left[\int_{J} \int_{0}^{T} h(s, x) \lambda(s, x) U(d s, d x)\right]
$$

for every bounded and $\mathscr{P} \otimes \mathcal{J}$-measurable process $h$.
Proof. The integral equation

$$
\int_{J} \int_{0}^{T} h(s, x) N^{V}(d s, d x)=\int_{J_{V}} \int_{0}^{T} h(s, x) N(d s, d x)
$$

defines a multivariate point process $N^{V}$ with mark space $J$ which only jumps at marks in $J_{V}$. [13], Theorem 2.1, provides a dual predictable projection $U^{V}$ of $N^{V}$ with respect to the reference measure $Q$ onto the filtration $\mathcal{F}_{t}^{V}$.

Let $h$ be a bounded and $\mathscr{P} \otimes \mathcal{J}$ measurable process. [14], Theorem I 2.2.ii and a monotone class argument provides a bounded and $\mathscr{P}^{V}$-measurable process $h^{V}$ such that

$$
\tilde{h}(\cdot, \cdot)=E_{Q}\left[h(\cdot, \cdot) \mid \mathcal{F}_{T}^{V}\right], \quad Q \text {-a.s. }
$$

Now,

$$
\begin{aligned}
E_{Q}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) U(d s, d x)\right] & =E_{Q}\left[\int_{J_{V}} \int_{0}^{T} h(s, x) N(d s, d x)\right] \\
& =E_{Q}\left[\int_{J} \int_{0}^{T} h(s, x) N^{V}(d s, d x)\right] \\
& =E_{Q}\left[\int_{J} \int_{0}^{T} \tilde{h}(s, x) N^{V}(d s, d x)\right] \\
& =E_{Q}\left[\int_{J} \int_{0}^{T} \tilde{h}(s, x) U^{V}(d s, d x)\right] \\
& =E_{Q}\left[\int_{J} \int_{0}^{T} h(s, x) U^{V}(d s, d x)\right]
\end{aligned}
$$

which proves the first claim.

To prove (A.2), let $W \subset J_{V}$ and $W^{\prime} \subset J_{V^{\prime}}$ be measurable subsets and consider the corresponding counting processes

$$
N_{t}^{W}:=N([0, t], W) \quad \text { and } \quad N_{t}^{W^{\prime}}:=N\left([0, t], W^{\prime}\right)
$$

and let

$$
U_{t}^{W}:=U([0, t], W) \quad \text { and } \quad U_{t}^{W^{\prime}}:=U\left([0, t], W^{\prime}\right)
$$

Following [13], Proposition 2.3, we see that

$$
\Delta U_{s}^{W}=E_{Q}\left[\Delta N_{s}^{W} \mid \mathcal{F}_{s-}\right] \quad \text { and } \quad \Delta U_{s}^{W^{\prime}}=E_{Q}\left[\Delta N_{s}^{W^{\prime}} \mid \mathcal{F}_{s-}\right], \quad Q \text {-a.s. }
$$

Now,

$$
\begin{aligned}
0 \leq E_{Q}\left[\left[U^{W}, U^{W^{\prime}}\right]_{T}\right] & =E_{Q}\left[\sum_{s \leq T} \Delta U_{s}^{W} \Delta U_{s}^{W^{\prime}}\right] \\
& \leq \sum_{s \leq T} E_{Q}\left[\Delta U_{s}^{W} \Delta U_{s}^{W^{\prime}}\right] \quad \text { by Fatou's lemma } \\
& =\sum_{s \leq T} E_{Q}\left[E_{Q}\left[\Delta N_{s}^{W} \mid \mathcal{F}_{s-}\right] E_{Q}\left[\Delta N_{s}^{W^{\prime}} \mid \mathcal{F}_{s-}\right]\right] \\
& =\sum_{s \leq T} E_{Q}\left[\Delta N_{s}^{W} \Delta N_{s}^{W^{\prime}}\right] \\
& =0
\end{aligned}
$$

so $\left[U^{W}, U^{W^{\prime}}\right]=0, Q$-a.s.
Whenever $f$ and $f^{\prime}$ are bounded and $\mathcal{F}_{t}$-predictable processes, we have

$$
\left[\int_{0} f_{s} d U_{s}^{W}, \int_{0} f_{s}^{\prime} d U_{s}^{W^{\prime}}\right]=\int_{0} f_{s} f_{s}^{\prime} d\left[U^{W}, U^{W^{\prime}}\right]_{s}=0, \quad Q \text {-a.s. }
$$

Equation (A.2) is therefore satisfied in the special case with $h=f \cdot \chi_{W}$ and $h^{\prime}=f^{\prime} \cdot \chi_{W^{\prime}}$. The general case now follows from an application of the Monotone class theorem. Equation (A.3) follows from an almost similar argument.

For the last claim, let $\nu$ denote the dual predictable projection of $N$ with respect to $P$ onto the filtration $\mathcal{F}_{t}$ and note that $\nu \ll U$ since $P \ll Q$. The existence of $\lambda$ then follows directly from [13], Theorem 4.1.

Acknowledgments. The author would like to thank Prof. Odd O. Aalen and Prof. Torben Martinussen for very helpful discussions on this project.
