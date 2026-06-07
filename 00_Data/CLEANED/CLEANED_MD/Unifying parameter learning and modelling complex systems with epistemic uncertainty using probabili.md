# HIAL open science 

## Unifying parameter learning and modelling complex systems with epistemic uncertainty using probability interval

C. Baudrit, S. Destercke, Pierre-Henri Wuillemin

## To cite this version:

C. Baudrit, S. Destercke, Pierre-Henri Wuillemin. Unifying parameter learning and modelling complex systems with epistemic uncertainty using probability interval. Information Sciences, 2016, 367-368, pp.630-647. 10.1016/j.ins.2016.07.003 . hal-01346202

## HAL Id: hal-01346202 <br> https://hal.sorbonne-universite.fr/hal-01346202v1

Submitted on 18 Jul 2016

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Unifying parameter learning and modelling complex systems with epistemic uncertainty using probability interval 

C. Baudrit ${ }^{\mathrm{a}, *}$, S. Destercke ${ }^{\mathrm{b}}$, P.H. Wuillemin ${ }^{\mathrm{c}}$<br>${ }^{a}$ INRA, I2M, USC 1368, F-33400 Talence, France.<br>${ }^{b}$ UTC, HEUDIASYC, UMR6599, F-60205 Compiègne cedex, France<br>${ }^{c}$ Sorbonne Universites, UPMC, Univ Paris 06, UMR 7606, LIP6, Paris, France<br>CNRS, UMR 7606, CNRS, Paris, France


#### Abstract

Modeling complex dynamical systems from heterogeneous pieces of knowledge varying in precision and reliability is a challenging task. We propose the combination of dynamical Bayesian networks and of imprecise probabilities to solve it. In order to limit the computational burden and to make interpretation easier, we also propose to encode pieces of (numerical) knowledge as probability intervals, which are then used in an imprecise Dirichlet model to update our knowledge. The idea is to obtain a model flexible enough so that it can easily cope with different uncertainties (i.e., stochastic and epistemic), integrate new pieces of knowledge as they arrive and be of limited computational complexity.


Keywords: Dynamic credal networks, imprecise probability, Dirichlet model, knowledge integration, uncertainty, modelling.

## 1. Introduction

Firms and industrials of all sectors have to face up new challenging situations. On the one hand, citizens as well as public authorities have stronger demands in terms of quality, safety, ... and on the other hand, they must adapt to the increase of population, global warming and the depletion of fossil resources. This means, among other things, that industrial projects have/to integrate sustainability from local to world scale in their conception. Possessing adequate tools to model their systems is likely to make the task easier.

In order to provide relevant conclusions and recommendations, such tools should be able to integrate as much available knowledge as possible, however heterogeneous it is, both in terms of nature (e.g., qualitative expert knowledge vs statistical data) and quality (different precision or degrees of reliability). Such systems are also complex, meaning that the modeling tool

[^0]
[^0]:    *Corresponding author

    PresEinh@ubiblio.fr d'̄̄rge haudrit@u-bordeaux.fr (C. Baudrit), July 4, 2016
    sebastien.destercke@hds.utc.fr (S. Destercke), pierre-henri.wuillemin@lip6.fr (P.H. Wuillemin)

must be able to cope with different scales (e.g., molecular to macroscopic) and with dynamic, time-varying processes. Current researches rely on the development of mathematical tools [53, 6] capable of helping decision-makers to deal with uncertainties, linked for instance to meteorological variations, to expert reliability, etc. To summarize, ideal modeling tools should be able to deal with:

- heterogeneous sources of knowledge (Web, data warehouse, experts, ...)
- mathematical formalisms used by different disciplines (differential equations, graphs, cognitive maps, ...)
- various manipulated scales (molecular, cellular, population, ...)
- different forms of uncertainty $[32,36,40]$ (natural randomness, imprecision in expert opinions, data scarcity, vagueness, ...)

In this paper, we propose dynamic credal networks as a possible answer to these challenging tasks to describe complex dynamical systems tainted with stochastic and epistemic uncertainty. As an extension of dynamic Bayesian networks (DBNs) [51], their network structure provides an intuitively appealing interface for human experts to model highly-interacting sets of variables, resulting in a qualitative representation of knowledge. Stochastic and epistemic uncertainties pertaining to the system are then taken into account by quantifying dependence between variables by means of convex sets of conditional probability distributions. The concept of DCNs makes it possible to combine different sources of information, from qualitative expert knowledge to experimental data.

In this paper, we are specifically interested in the problem of parameter learning for a given network structure (assumed to be known), when faced with heterogeneous knowledge. Indeed, while DCN are very attractive modeling tools, they also come with a number of challenges, such as how to control their computational tractability, or how to combine efficiently and easily various pieces of information. For example, how to combine simulations coming from stochastic differential equations with an experimental database, both offering information for the same parameters? We propose to use an imprecise Dirichlet model [7] as a model of the conditional probabilities, and probability intervals as a common uncertainty model to treat different pieces of knowledge. Once transformed, these information pieces gradually increment the set of prior distributions according to the received knowledge, using the Generalized Bayes rule each time additional information arrives. Lower and upper expected a posteriori (EAP) are then used as probability bounds to draw inferences from the network. The combination of information is done through a weighted average, allowing us to weigh the importance of the different sources of knowledge.

Section 2 details the material regarding imprecise probabilities as well as the proposed updating scheme of a given parameter set. We then describe in Section 3 how various common sources of information can be transformed into probability intervals. Section 4 presents how we extend Dynamic Bayesian Networks to sets of conditional probabilities, while Section 5 illustrates the whole approach on a real-case scenario involving cheese ripening.

# 2. Imprecise probabilities and Dirichlet model 

Let $X$ be a variable ${ }^{1}$ taking its values on the finite set $\mathcal{X}=\{x_{1}, \ldots, x_{n}\}$, and $p: \mathcal{X} \mapsto[0,1], \sum_{x \in \mathcal{X}} p(x)=1$ be a probability mass function over $\mathcal{X}$. $p(X)$ will denote the vector mass function, while $p(x)$ will denote the value taken by $p$ for $X=x$. Such a mass function defines a measure $P_{X}(A)=$ $\sum_{x \in A} p(x)$ for all $A \subseteq \mathcal{X}$.

### 2.1. Imprecise probability and credal sets

In general, identifying a single probability modelling our uncertainty about some variable $X$ requires a lot of data and/or knowledge. When such knowledge is not available, a safer option is to model our uncertainty by convex sets of probabilities, often called credal sets [47, 61, 2]. A credal set associated with $X$, denoted $K(X)$, is a convex set of probability masses over $\mathcal{X} . K(X)$ represents the uncertainty about the unknown value of the variable $X$. From $K(X)$ are defined upper and lower probability measures of an event $A \subseteq \mathcal{X}$ as

$$
\overline{P_{X}}(A)=\sup _{p \in K(X)} \sum_{x \in A} p(x), \underline{P_{X}}(A)=\inf _{p \in K(X)} \sum_{x \in A} p(x)
$$

and, in particular, for any element $x \in \mathcal{X}$ we will have that the upper and lower probabilities are given by

$$
\begin{aligned}
\bar{p}(x) & =\sup _{p \in K(X)} p(x) \\
\underline{p}(x) & =\inf _{p \in K(X)} p(x)
\end{aligned}
$$

In a subjectivist tradition, the lower probability $\underline{P_{X}}(A)$ can be interpreted as the maximal price one would be willing to pay for the gamble which pays 1 unit if event $A$ occurs (and nothing otherwise) [61]. $\underline{P_{X}}(A)$ is therefore a measure of evidence in favour of event $A$, or in other words how much $K(X)$ supports event $A$, while $\overline{P_{X}}(A)$ measures the lack of evidence against $A$. $K(X)$ can also be given a robust interpretation, in which it models imperfect

[^0]
[^0]:    ${ }^{1}$ We adopt notations similar to those of [2, Ch.9] and [24].

knowledge of a precise, possibly frequentist, probability $p$. A credal set $K(X)$ contains a set $\mathcal{E} x t(K(X))$ of extreme probability masses, always finite in this paper, corresponding to the vertices of $K(X)$. Geometrically, $K(X)$ may be equivalently specified by the convex hull (denoted $C H$ ) of the set $\mathcal{E} x t(K(X))$, i.e.

$$
K(X)=C H\{\mathcal{E} x t(K(X))\}
$$

The vacuous credal set

$$
K_{v}(X)=\left\{p(X): p(x) \geq 0, \forall x \in \mathcal{X}, \sum_{x \in \mathcal{X}} p(x)=1\right\}
$$

that includes all probability masses over $\mathcal{X}$ plays an important role, as it models total ignorance, and should be the starting point of any model. We refer to Walley [61, Sec. 5.5.] for a discussion about uniform probability distribution not being a good model of ignorance.

In this paper, we will also be especially interested in particular credal sets $K(X)$ specified by means of interval probability

$$
K(X)=\left\{p(X): p(x) \in\left[l_{x}, u_{x}\right], 0 \leq l_{x} \leq u_{x} \leq 1, \sum_{x \in \mathcal{X}} p(x)=1\right\}
$$

Indeed, such credal sets that focus over bounds of singletons have the advantage to be easier to manipulate, simulate and represent than general ones, while remaining expressive enough (they include both the vacuous and the precise models). We refer to De Campos et al. [11] for a detailed exposition, and will only limits ourselves to necessary elements in this paper.
Example 1. Consider an example with three possibilities $\mathcal{X}=\left\{x_{1}, x_{2}, x_{3}\right\}$ (e.g., the working states of a system such as "failing", "degraded functioning", "fully functioning"), and assume that previous experiments result in the following intervals

$$
p\left(x_{1}\right)=[0 ; 0.2], \quad p\left(x_{2}\right)=[0.3 ; 0.4], \quad p\left(x_{3}\right)=[0.4 ; 0.6]
$$

The credal set $K(X)$ is the set of all precise probabilities $P(X)=\left(p\left(x_{1}\right), p\left(x_{2}\right),\left(p\left(x_{3}\right)\right)\right.$ within these interval bounds. Here $K(X)$ is a polytope defined by the convex hull of its four vertices in a three dimensional space:

$$
K(X)=C H\{(0,0.4,0.6) ;(0.2,0.3,0.5) ;(0.2,0.4 ; 0.4) ;(0.1,0.3,0.6)\}
$$

Finding these vertices can be done by using classical tools of convex geometry [39], or by using algorithms proper to a given representation (an Algorithm is provided by De Campos et al. [11]). The set $K(X)$ is represented in Figure 1 in barycentric coordinates.

![img-0.jpeg](img-0.jpeg)

Figure 1: Example 1 credal set in Barycentric coordinates.

# 2.2. Robust Dirichlet model to learn $K(X)$ 

An important question is how the credal set $K(X)$ can be instantiated from actual evidence, or in other words how can we go from an initially vacuous knowledge towards a more precise state of knowledge. An instrumental tool to do that is to use a robustified version of the Dirichlet model, also commonly referred to as the Imprecise Dirichlet Model (IDM) $[62,7,8,60]$. The basic model is based on two hyper-parameters: a positive real value $s_{0}$ associated to the strength of prior knowledge, and a vector $\epsilon_{0}=\left(\epsilon_{0}\left(x_{1}\right), \ldots, \epsilon_{0}\left(x_{n}\right)\right)$ associated to our initial beliefs about the probabilities of occurrence of elements $x_{i}$.

Let $\boldsymbol{\theta}=\left(\theta_{1}, \ldots, \theta_{n}\right)$ be a vector of chances such that $\theta_{i}$ corresponds to the chance that $X=x_{i}$. The prior distribution of vectors $\boldsymbol{\theta}$ given by a Dirichlet model is then

$$
\operatorname{Dir}\left(s_{0} ; \xi_{0}\right)(\boldsymbol{\theta})=\frac{\Gamma\left(s_{0}\right)}{\prod_{i=1}^{n} \Gamma\left(s_{0} \xi_{0}\left(x_{i}\right)\right)} \prod_{i=1}^{n} \theta_{i}^{s_{0} \xi_{0}\left(x_{i}\right)-1}
$$

where $\Gamma$ is the gamma function. A very easy way to make this model imprecise is to let the vector $\epsilon_{0}$ become imprecise, and more precisely to consider the set of Dirichlet models

$$
\mathcal{M}_{\left(s_{0} ; \xi_{0}\right)}=\left\{\operatorname{Dir}\left(s_{0} ; \xi_{0}\right)(\boldsymbol{\theta}): \xi_{0} \in \mathcal{T}\right\}
$$

with

$$
\mathcal{T}=\left\{\xi_{0}: 0<\xi_{0}\left(x_{i}\right)<1, \sum_{i=1}^{n} \xi_{0}\left(x_{i}\right)=1\right\}
$$

the open $(n-1)$-dimensional unit simplex. When $\xi_{0}$ is precise, the first moments of $\operatorname{Dir}\left(s_{0} ; \xi_{0}\right)$ are given by $E\left(\theta_{i} \mid\left(s_{0} ; \xi_{0}\right)\right)=\xi_{0}\left(x_{i}\right)$, and they can be used as estimates of $p\left(x_{i}\right)$, i.e.

$$
E\left(\theta_{i} \mid\left(s_{0} ; \xi_{0}\right)\right)=\xi_{0}\left(x_{i}\right)=p\left(x_{i}\right)
$$

When starting from a vacuous prior knowledge $\xi_{0} \in \mathcal{T}$, the bounds over the first moments become

$$
\underline{E}\left(\theta_{i} \mid\left(s_{0} ; \xi_{0}\right)\right)=\min _{\xi_{0} \in \mathcal{T}} \xi_{0}\left(x_{i}\right)=0
$$

and

$$
\bar{E}\left(\theta_{i} \mid\left(s_{0} ; \xi_{0}\right)\right)=\max _{\xi_{0} \in \mathcal{T}} \xi_{0}\left(x_{i}\right)=1
$$

The credal set corresponding to these bounds is then the vacuous one (5).
We may then receive additional information from various $m$ sources. A convenient way to encode this information is as a couple $s_{k}, \mathcal{P}_{k}, k=1, \ldots, m$, with $\mathcal{P}_{k} \subseteq \mathcal{T}$ a convex polytope providing information about the possible chances $\theta_{i}$, and $s_{k} \in \mathbb{R}^{+}$modelling the strength of the information. We can then update the Dirichlet modelling our uncertainty about $\theta_{i}\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}$ into

$$
\mathcal{M}_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}=\left\{\operatorname{Dir}\left(\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}\right)(\boldsymbol{\theta}): \xi_{k} \in \overline{\mathcal{P}}_{k}, 2 k\right\}
$$

We can then use the posterior first moments to make inferences on chances $\theta_{i}$

$$
\mathrm{E}\left(\theta_{i} \mid\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}\right)=p\left(x_{i}\right)=\frac{\sum_{k=0}^{m} s_{k} \xi_{k}\left(x_{i}\right)}{\sum_{k=0}^{m} s_{k}}
$$

As information $\mathcal{P}_{k}$ are imprecise, we again obtain bounds in the form

$$
\begin{aligned}
& \underline{E}\left(\theta_{i} \mid\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}\right)=p\left(x_{i}\right)=\frac{\sum_{k=0}^{m} s_{k} \xi_{k}\left(x_{i}\right)}{\sum_{k=0}^{m} s_{k}} \\
& \bar{E}\left(\theta_{i} \mid\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}\right)=\bar{p}\left(x_{i}\right)=\frac{\sum_{k=0}^{m} s_{k} \bar{\xi}_{k}\left(x_{i}\right)}{\sum_{k=0}^{m} s_{k}}
\end{aligned}
$$

where

$$
\begin{aligned}
\xi_{k}\left(x_{i}\right) & =\inf _{\xi_{k} \in \mathcal{P}_{k}} \xi_{k}\left(x_{i}\right) \\
\bar{\xi}_{k}\left(x_{i}\right) & =\sup _{\xi_{k} \in \mathcal{P}_{k}} \xi_{k}\left(x_{i}\right)
\end{aligned}
$$

These bounds then induce an updated credal set

$$
K_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)=\left\{p: p\left(x_{i}\right) \in\left[\frac{\sum_{k=0}^{m} s_{k} \xi_{k}\left(x_{i}\right)}{\sum_{k=0}^{m} s_{k}}, \frac{\sum_{k=0}^{m} s_{k} \bar{\xi}_{k}\left(x_{i}\right)}{\sum_{k=0}^{m} s_{k}}\right]\right\}
$$

that we can use as new knowledge. In practice, $s_{0}$ can be interpreted as the number of "unseen" data, and $s_{k}=s_{0}$ means that the $k$ th information source has as much importance as our initial uncertainty.

Remark 1. The exact updated credal set

$$
\check{K}_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)=\left\{\frac{\sum_{k=0}^{m} s_{k} \xi_{k}}{\sum_{k=0}^{m} s_{k}}: \xi_{k} \in \mathcal{P}_{k}, \forall k=1, \ldots, m\right\}
$$

is a subset of $K_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)$, i.e., $\check{K}_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X) \subseteq K_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)$. The set (19) is thus an outer-approximation. Yet, the main advantages of using probability bounds as a basic representation are that

- their number of extreme points is bounded and relatively low, even when combining them through a weighted average. This is in general not the case if we consider averaging of heterogeneous simple representations: if we denote $\left|\mathcal{E} x t\left(\mathcal{P}_{k}\right)\right|$ the number of extreme points of the $k$ th item of information, then their (Minkowsky) sum $\sum_{k=0}^{m} s_{k} \mathcal{P}_{k}$ may have as much as $\prod_{k=0}^{m}\left|\mathcal{E} x t\left(\mathcal{P}_{k}\right)\right|$ extreme points, an exponentially growing number;
- they are easy to explain and to represent graphically (e.g., as imprecise histograms), therefore offering a convenient way to communicate with domain experts or users not specialized in mathematics or computer science. This is not the case of more complex representations such as belief functions (Section 3.4);
- except for requiring a finite space, they do not require specific assumptions, such as the existence of an ordering between elements;
- they are expressive enough so that they can go from a fully precise probability to the complete ignorance model.

None of the other common practical models of information reviewed in Section 3 have all these advantages at once, making probability bounds a quite convenient model. Given this, using probability bounds seem a good general starting point in applications, not preventing one from investigating refined solutions if the results are unsatisfactory.

Of course, in some cases $K_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)$ may be a poor outer-approximation, however we shall see in Section 5 that it does not necessarily lead to completely void conclusions. Previous studies [1] also suggest that this kind of approximation may be in average reasonable.
Example 2. Let $\mathcal{X}=\left\{x_{1}, x_{2}, x_{3}\right\}$ and $\mathcal{P}=\left\{\xi: \xi\left(x_{2}\right) \geq \xi\left(x_{1}\right), 1 / 2 \geq\right.$ $\left.\xi\left(x_{3}\right), \sum_{i=1}^{3} \xi\left(x_{i}\right)=1\right\}$ be an item of information. The credal set $\check{K}_{\xi}(X)$ over $\left\{x_{1}, x_{2}, x_{3}\right\}$ obtained by (20) has four extreme points $\{(0,1,0),(0,0.5,0.5)$, $(0.5,0.5,0),(0.25,0.25,0.5)\}$ that are also extreme points of $K_{\xi}(X)=\{p$ : $\left.p\left(x_{i}\right) \leq \max _{\epsilon \in \mathcal{P}} \epsilon\left(x_{i}\right)\right\}$. However, the probability $(0.5,0.25,0.25)$ is an extreme point of $K_{\xi}(X)$ but not of $\check{K}_{\xi}(X)$.

# 3. Review of practical sources of information 

Building $K_{\left(s_{k} ; \xi_{k}\right)_{k=0}^{m}}(X)$ requires to obtain elements of information $\mathcal{P}_{k}$. In this section, we review different practical models and the bounds they induce over $\xi_{k}\left(x_{i}\right)$. We will also provide small examples illustrating what kind of information they can model. For the sake of brevity, we will denote $\xi\left(x_{i}\right)$ by $\xi^{i}$ in this section. Note that our information is initially queried on observed values $x_{i}$, to be then transferred as knowledge on the parameters $\xi^{i}$. Hence we will consistently refer to knowledge about $\xi^{i}$, and to observation or information about $x_{i}$.

### 3.1. Precise evaluations

The most simple models is when the knowledge $\mathcal{P}$ is given by a precise vector, in which case $\xi^{i}=f_{i}$ is a precise number, and we have

$$
\overline{\xi^{i}}=\underline{\xi}^{i}=f_{i}
$$

A classical way to obtain such precise evaluations is when observing $\boldsymbol{m}=$ $\left(m_{1}, \ldots, m_{n}\right)$ experiments, where $m_{i}$ is the number of times $x_{i}$ was observed. In such a case, a classical choice is to take as strength $s=m=\sum_{i=1}^{n} m_{i}$ and $\mathcal{P}$ is the vector $\boldsymbol{f}=\left(f_{1}, \ldots, f_{n}\right)$ where $f_{i} \geq m_{i} / m$.
Example 3. Assume we can observe three possibilities $x_{1}, x_{2}, x_{3}$ (e.g., severity of a disease, importance of a bacterial population), and we observed 3 times $x_{1}, 6$ times $x_{2}$ and one time $x_{3}$. We then have

$$
f_{1}=0.3, f_{2}=0.6, f_{3}=0.1 \text { and } s=m=10
$$

Note that the more observations we accumulate, the stronger becomes this piece of knowledge. $s$ can also be modulated to reflect the reliability of data. Note that this model is a degenerated case of probability intervals, and can therefore be exactly represented in our framework.

### 3.2. Numerical possibility distributions and fuzzy subsets

A possibility distribution $\pi$ is simply a mapping from $\left\{\xi^{1}, \ldots, \xi^{n}\right\}$ to $[0,1]$, with at least one element $\xi^{i}$ such that $\pi\left(\xi^{i}\right)=1$ [33]. In practice, we can see distribution $\pi$ as an ordering $1=\pi\left(\xi^{(1)}\right) \geq \ldots \geq \pi\left(\xi^{(n)}\right)$ of the elements $x_{1}, \ldots, x_{n}$, from the most plausible to the least plausible one.

Another instrumental way is to encode the possibility distribution through the necessity measure $N$. This necessity measure $N$ is such that

$$
N\left(A_{(i)}=\left\{\xi^{(1)}, \ldots, \xi^{(i)}\right\}\right)=1-\pi\left(\xi^{(i+1)}\right)
$$

with $\pi\left(\xi^{(n+1)}\right)=0 . N\left(A_{(i)}\right)$ can be associated to a lower probability bound of event $A_{(i)}$. In particular, the sets $A_{(i)}$ can be interpreted as nested sets with an associated lower confidence, these nested sets being built by starting

from the most plausible element $\xi^{(1)}$ and incrementally including the less plausible ones. Note that we may have $\pi\left(\xi^{(i)}\right)=\pi\left(\xi^{(i+1)}\right)$, in which case elements $x_{(i-1)}$ and $x_{(i)}$ would be in the same confidence set.

In practice, an expert can provide a possibilistic information by giving confidence bounds over a collection of nested sets. Let $A_{1} \subseteq \ldots \subseteq A_{m}$ be such sets with associated confidence levels $\alpha_{1} \leq \ldots \leq \alpha_{m}$, then it encodes the knowledge $\mathcal{P}_{\pi}=\left\{\xi: \sum_{k=1}^{i} \xi^{(k)} \geq \alpha_{i}, \forall i\right\}$. From the knowledge on sets $A_{1}, \ldots, A_{m}$, one can always come back to an associated distribution $\pi$ using

$$
\pi\left(\xi^{k}\right)=\min _{i: \xi^{k} \in A_{i}} 1-\alpha_{i-1}
$$

with $\alpha_{0}=0$.
Another possibility is to use the formal equivalence between a possibility distribution $\pi$ and a fuzzy set having $\pi$ for membership function. This means that an expert conveying information in the form of linguistic assessment [64] can also be modelled by possibility distributions. Derivine bounds on $\xi^{i}$ from $\mathcal{P}_{\pi}$ using the possibility distribution $\pi$ is very easy, as

$$
\begin{gathered}
\xi^{i}=1-\max _{\xi \neq \xi^{i}} \pi(\xi) \\
\bar{\xi}^{i}=\pi(\xi)
\end{gathered}
$$

Example 4. Assume that an expert is interrogated about the temperature in a room that can be in three states $x_{1}, x_{2}, x_{3}$. Expert judges that $x_{2}$ is the most plausible state, then $x_{3}$ and $x_{1}$, meaning that $\xi^{(1)}=\xi^{2}, \xi^{(2)}=$ $\xi^{3}, \xi^{(3)}=\xi^{1}$. The expert provides the following confidence values:

$$
\begin{gathered}
N\left(\left\{\xi^{2}\right\}\right)=0.5 \\
N\left(\left\{\xi^{2}, \xi^{3}\right\}\right)=0.8 \\
N\left(\left\{\xi^{2}, \xi^{3}, \xi^{1}\right\}\right)=1
\end{gathered}
$$

which means that the expert has a confidence 0.5 that $x_{2}$ will be the observed state, a confidence 0.8 that the observed state will be either $x_{2}$ or $x_{3}$, and finally is certain that the only observable states are $x_{1}, x_{2}, x_{3}$. From these values can be deduced the values of the corresponding possibility distribution $\pi(\xi)^{1}=0.2, \pi\left(\xi^{2}\right)=1, \pi\left(\xi^{3}\right)=0.5$.

Alone, possibility distributions will often be simpler than probability intervals: they require less information (one value per element) and will have a maximal number of $2^{|\mathcal{X}|-1}$ extreme points [56]. Yet the average of multiple sets $\mathcal{P}_{\pi_{1}}, \ldots, \mathcal{P}_{\pi_{m}}$ would no longer be a possibility distribution, and the corresponding number of extreme points could explode. Also, possibility distributions cannot model precise probabilities, unless they are degenerate ones.

# 3.3. Probability boxes and clouds 

A probability box [35] $\underline{F}, \bar{F}$ is an imprecise cumulative distribution. It can be modelled by two discrete non-decreasing functions $\underline{F}$ and $\bar{F}$ from $\left(\xi^{1}, \ldots, \xi^{n}\right)$ to $[0,1]$ such that $\underline{F}\left(\xi^{i}\right) \leq \bar{F}\left(\xi^{i}\right)$ for all $i$ in $\{1, \ldots, n\}$ and $\underline{F}\left(\xi^{n}\right)=\bar{F}\left(\xi^{n}\right)=1$. The values $\underline{F}\left(\xi^{i}\right), \bar{F}\left(\xi^{i}\right)$ are interpreted as the following bounds

$$
\underline{F}\left(\xi^{i}\right) \leq \sum_{i=1}^{n} \xi^{i} \leq \bar{F}\left(\xi^{i}\right)
$$

and we can denote by $\mathcal{P}_{\underline{F} \leq \bar{F}}$ the knowledge modelled by a p-box. A p-box information provides us with estimates about the cumulated probabilities of events of the kind $\left\{x_{1}, \ldots, x_{i}\right\}$, hence assuming that the ordering induced by the indices do make sense.

In the case of p-boxes, the bounds over $\xi^{i}$ are very easy to determine [59], and are equal to

$$
\begin{gathered}
\xi^{i}=\max \left(0, \underline{F}\left(\xi^{i}\right)-\bar{F}\left(\xi_{i}^{i} \xi^{1}\right)\right) \\
\bar{\xi}^{i}=\bar{F}\left(\xi^{i}\right)-\underline{F}\left(\xi^{i-1}\right)
\end{gathered}
$$

with the convention $\underline{F}\left(\xi^{0}\right)=\bar{F}\left(\xi^{0}\right)=0$.
Example 5. Assume we have to assess the how likely it is that a bacterial population is below some threshold, or how likely it is that a component may function for a given period of time. The population sizes or time intervals may be discretized into $x_{1}, x_{2}, x_{3}$. Assume the following p-box has been given as information

$$
\underline{F}\left(\xi^{1}\right)=0.2, \underline{F}\left(\xi^{2}\right)=0.7 \text { and } \bar{F}\left(\xi^{1}\right)=0.5, \bar{F}\left(\xi^{2}\right)=0.9
$$

From it we can deduce the bounds

$$
\xi^{1}=0.2, \xi^{2}=0.2, \xi^{3}=0.1 \text { and } \bar{\xi}^{1}=0.5, \bar{\xi}^{2}=0.7, \bar{\xi}^{3}=0.3
$$

P-boxes usually rely on the fact that the set $\left(\xi^{1}, \ldots, \xi^{n}\right)$ is naturally ordered, and provide confidence bounds over sets of the kind $\left\{\xi^{1}, \ldots, \xi^{i}\right\}$. However, one possibility is to extend this notion by considering that values $\xi^{i}$ follows an arbitrary ordering $\xi^{(1)} \leq \ldots \leq \xi^{(n)}$ (for example, from the least to the most plausible element) and to ask to the expert to provide upper and lower confidence bounds about the fact that the truth lies in $\left\{x_{(1)}, \ldots, x_{(i)}\right\}$, thus obtaining $\underline{F}\left(\xi^{(i)}\right)$ and $\bar{F}\left(\xi^{(i)}\right)$. As in principle any ordering can be used, this is indeed a generalization of p-boxes, known as comonotonic clouds [31]. In particular, in the case where $\underline{F}\left(\xi^{(i)}\right)=0$ for any $i$, we retrieve the notion of possibility distribution as a special case.

Up to now, what is the maximal number of extreme points of a p-box structure and how to efficiently enumerate them remains an open problem. However, as p-boxes are a special case of belief functions, one can

use (potentially sub-optimal) algorithms and methods applicable to belief functions [17]. It is also clear that the maximal number of such points is bounded above by the maximal number of extreme point of a belief function $(n!)$. Classical p-boxes suffer from the fact that a natural order must exist on $\mathcal{X}$, and when no such order exists, then the average of generalized p-boxes relying on different orders will not be a p-box.

# 3.4. Belief functions and random sets 

Formally, a random set or belief function, initially introduced by Dempster [30] and Shafer [57], is defined as a positive mapping $\nu: 2^{\left\{\xi^{1} \in \mathbb{Z}\right\}} \rightarrow$ $[0,1]$ from the power set of $\left\{\xi^{1}, \ldots, \xi^{n}\right\}$ to the unit interval, such that $\nu(\emptyset)=0$ and $\sum_{E} \nu(E)=1$. From this mapping can then be defined probability bounds $\operatorname{Bel}(A), \operatorname{Pl}(A)$ for any event that are equal to

$$
\operatorname{Bel}(A)=\sum_{E, E \subseteq A} \nu(E) \text { and } \operatorname{Pl}(A)=\sum_{E, E \cap A \neq \emptyset} \nu(E)=1 \quad \operatorname{Bel}\left(A^{c}\right)
$$

that induce an information $\mathcal{P}_{\nu}$ such that

$$
\mathcal{P}_{\nu}=\left\{\xi: \sum_{E \subseteq A} \nu(E) \leq \sum_{E \in A} \xi: \sum_{E \cap A \neq \emptyset} \nu(E), \forall A\right\}
$$

In particular, this means that given a function $\nu$, the bounds over elementary events are given by

$$
\begin{aligned}
& \xi^{i}=\operatorname{Bel}\left(\left\{\xi^{i}\right\}\right)=\nu\left(\left\{\xi^{i}\right\}\right) \\
& \xi=\operatorname{Pl}\left(\left\{\xi^{i}\right\}\right)=\sum_{\xi^{i} \in E} \nu(E)
\end{aligned}
$$

Belief functions are instrumental to model frequencies of imprecise observations, for example when multiple exclusive options can be chosen in surveys, or when some sensors sometimes send back imprecise observations. They also include p-boxes, comonotonic clouds and possibilities as special cases.
Example 6. Assume again that we can meet four different situations $x_{1}, x_{2}, x_{3}$ or $\xi$. Out of 20 observations, $x_{1}, x_{2}, x_{3}, x_{4}$ were each perfectly observed respectively $3,2,5,6$ times, we observed 3 times the set $\left\{x_{2}, x_{3}, x_{4}\right\}$ (excluding $x_{1}$ ) and 2 times the set $\left\{x_{1}, x_{2}, x_{3}\right\}$. Such observations can be modelled on $\xi^{1}, \xi^{2}, \xi^{3}, \xi^{4}$ by the mass

$$
\begin{gathered}
\nu\left(\left\{\xi^{1}\right\}\right)=3 / 20, \nu\left(\left\{\xi^{2}\right\}\right)=2 / 20, \nu\left(\left\{\xi^{3}\right\}\right)=5 / 20, \nu\left(\left\{\xi^{4}\right\}\right)=6 / 20 \\
\nu\left(\left\{\xi^{1}, \xi^{2}, \xi^{3}\right\}\right)=2 / 20, \nu\left(\left\{\xi^{2}, \xi^{3}, \xi^{4}\right\}\right)=3 / 20
\end{gathered}
$$

From this, we can for example deduce $\underline{\xi}^{3}=0.25$ and $\bar{\xi}^{3}=0.5$.

Belief functions are general enough to deal with a lot of practical assessments, and share the properties of probability intervals that an average of belief functions is still a belief function. However, providing an intuitive graphical representation of a belief function is challenging, and their use may quickly lead to computational issues (e.g., their number of extreme points can be as high as $\mathcal{X}$ ! [50])
3.5. Fuzzy random variables

Fuzzy random variables have been given different interpretations in the literature, depending on the nature of the fuzzy elements. For example, a fuzzy random variable can be seen as a random phenomenon with precise observations that are fuzzy in nature, or as a random phenomenon with imprecise observations. We refer to $[19,21,22]$ for a detailed discussion. In this paper, Fuzzy random variables are interpreted as conditional possibility measures $[4,21]$, which consist in putting positive masses, not on subsets, but on possibility distributions. They can be modelled by a set $\pi_{1}, \ldots, \pi_{k}$ where each distribution receives probability mass $p\left(\pi_{i}\right)$. As each $\pi_{i}$ can in turn be turned into a mass function $\nu_{\pi_{i}}$ defined this time over subsets, it is always possible to come back from a fuzzy random variable to a classical mass function, simply by computing for any subset $E$ the value

$$
\nu(E)=\sum_{i} p\left(\pi_{i}\right) \nu_{\pi_{i}}(E)
$$

We obtain a weighted random sampling of subset $E$ defining a belief function $\nu$. Fuzzy random variables in this context may be cast into the framework of belief functions leading to the same formal advantages and disadvantages of them (see Section 3.4). Fuzzy random variables can result, for instance, from Monte-Carlo simulations of physical models mixing possibilistic and probabilistic uncertainty [4], or from the random observation of fuzzy sets (modelling an all-calibrated scale, for instance [18]).

# 3.6. Summary of types of knowledge 

A final type of knowledge simply consists in directly providing bounds over the values of possible observations $x_{i}$. This means specifying, for each $\xi^{i}$, the bounds $\underline{f}_{i}=\xi^{i}$ and $\bar{f}_{i}=\bar{\xi}^{i}$. Such bounds are formally equivalent to probability intervals [11].

There are multiple ways to derive such bounds: for instance by instantiating multinomial confidence intervals over observations, by requiring linguistic opinions of the type "probable", "very probable" from the experts and then translating them into numerical evaluations [54], by simply requiring numerical evaluations from the experts, when having imprecise histograms, $\ldots$

Table 1 summarises the most common type of practical information one can meet, to what type of information they correspond and how can be computed the lower/upper values $\xi^{i}$ and $\bar{\xi}^{i}$. These are the values (used as a common mathematical tool) that are then combined and integrated into the learning process developed in Section 2.2.


Table 1: Summary of the different types of collectible information

# 4. Robust dynamic probabilistic graphical models 

When modeling complex systems, we are not interested in a single variable, but in multiple variables interacting with each others and evolving over time. In theory, our knowledge about these variables, their interaction and evolution can be represented by a credal set defined over the Cartesian product of the corresponding spaces.

In practice, we need tool to represent these interactions, and to simplify the daunting task of specifying a full joint model. Credal networks are graphical (directed) models that aims at encoding our knowledge about variable interactions and at splitting the full joint into multiple, simple conditional models. This section introduces them, as well as their dynamical extension.

### 4.1. Credal networks

Let $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ be a discrete random vector associated with the joint probability mass function $p(\mathbf{X})$ defined over $\prod_{i=1}^{n} \mathbf{U}_{i}$. Let $K(\mathbf{X})$ be the closed convex set of multivariate probability mass functions describing our knowledge of $\mathbf{X}$.

A credal network (CN) [24, 23] is an extension of Bayesian networks (BNs) where imprecision is introduced in probabilities by means of credal sets [47]. When working with probability sets rather than precise probabilities, the notion of stochastic independence can be extended in several ways [20]. Within graphical models, the most commonly used extension is strong independence (also called a type 1 product of the marginals in [61]), that induces the strong extension. It can be interpreted as a robust model of a precise yet ill-known BN. Under the strong extension [23] hypothesis, the joint credal set $K(\mathbf{X})$ over $\Omega_{\mathbf{X}}$ may be formulated as:

$$
K(\mathbf{X})=C H\left\{p(\mathbf{X}): p(\mathbf{X})=\prod_{i=1}^{n} p_{i}, p_{i} \in K_{i}\right\}
$$

where $p_{i}=p\left(X_{i} \mid \mathbf{U}_{i}\right), \mathbf{U}_{i}$ denotes the set of parent nodes of the node $X_{i}$ and $K_{i}=K\left(X_{i} \mid \mathbf{U}_{i}\right)$ is the closed convex set of probability mass function for the random variable $X_{i}$ given $\mathbf{U}_{i}$. As mentioned in Section 2, it is sufficient to focus on $\mathcal{E} x t\left(K\left(X_{i} \mid \mathbf{U}_{i}\right)\right)$ in Eq. (33).

In this work, we focus on the notion of strong independence and its extension to dynamical models, as this is the most widely used independence notion within graphical models and the one that fits the best with a robust interpretation of probability sets. Other independence notions that may even have asymmetrical versions such as epistemic irrelevance remain computationally intractable [25, 49], except for specific network structures [9] that are usually less complex than the one generally considered here.

# 4.2. Dynamic credal networks 

Let $\mathbf{X}(\mathbf{t})=\left(X_{1}(1), \ldots, X_{n}(1), \ldots, X_{1}(\tau), \ldots, X_{n}(\tau)\right)$ be a discrete random vector process associated with the joint probability function $p(\mathbf{X}(\mathbf{t}))$ defined over $\prod_{t=1}^{\tau} \prod_{i=1}^{t} \mathcal{X}_{i}(t)$. Let $K(\mathbf{X}(\mathbf{t}))$ be the closed convex set of multivariate probability mass functions for $\mathbf{X}(\mathbf{t})$.

A dynamic credal network (CDN) [41] is a dynamic Bayesian network (DBNs) [51] where conditional probabilities $p\left(X_{i}(t) \mid \mathbf{U}_{i}(t)\right)$ (noted $p_{i}^{t}$ ) are replaced by credal sets $K\left(X_{i}(t) \mid \mathbf{U}_{i}(t)\right)$ (noted $K_{i}^{t}$ ). It is therefore a timesliced model that can be used to describe a dynamic process or system.

We assume the same first-order Markov property as for DBN, meaning that parents only originate from the same or previous time slice, and also that conditional models remain the same at each times slice, that is

$$
K\left(X_{i}(t) \mid \mathbf{U}_{i}(t)\right)=K\left(X_{i}(2) \mid \mathbf{U}_{i}(2)\right), \forall t \in[2, \tau]
$$

Therefore, specifying the graphical structure of a DCN requires the same effort as the one of a DBN (that is, specifying only two consecutive time slices) but allows the user to provide conditional credal sets rather than probabilities if these latter cannot be reliably estimated (from data and/or experts).

### 4.2.1. Independence in DCN

Extending DBN to DCN requires to specify which kind of independence we consider within and also between each time-slice. We remind that we will only consider extensions relying on the strong independence (33). The most straightforward extension is to simply apply strong independence to the whole network, i.e.

$$
K\left(\mathbf{X}(\mathbf{t}) \mid \mathbf{s}=C H\left\{p(\mathbf{X}(\mathbf{t})): p(\mathbf{X}(\mathbf{t}))=\prod_{i=1}^{n} \prod_{t=1}^{\tau} p_{i}^{t}, p_{i}^{t} \in K_{i}^{t}\right\}\right.
$$

We call this extension the dynamic strong extension and it is worth noticing that we can have $p_{i}^{t} \neq p_{i}^{t^{\prime}}$ for $t, t^{\prime} \in[2, \tau]$. That is, we do not assume probabilities within each time-slice to be identical. However, when stepping to dynamic models, Condition (34) allows us to use the notion of repetitive independence (also called a type 2 product of the marginals in [61]). This condition states that if two variables $X, Y$ have the same set of possible outcomes, that is $\mathcal{X}=\mathcal{Y}$, and can be assumed to be governed by the same probability distribution belonging to $K(X)$, then the joint credal set $K(X, Y)$ is :

$$
K(X, Y)=C H\{p(X) p(X): p(X) \in K(X)\}
$$

[^0]
[^0]:    ${ }^{2}$ It should be noted that the network itself is static, but is used to represent a dynamic process.

![img-1.jpeg](img-1.jpeg)

Figure 2: A simple dynamical graphical model

Adapting this notion of independence to DCN, so that probabilities of each time slice are assumed to be identical, leads to a second extension, i.e.,

$$
K(\mathbf{X}(\mathbf{t}))_{r p}=C H\left\{\begin{array}{l}
p(\mathbf{X}(\mathbf{t})): p(\mathbf{X}(\mathbf{t}))=\prod_{i=1}^{n} \prod_{i=1}^{r} p_{i}, \\
p_{i}^{2} \in K_{i}^{2} \text { and } p_{i}^{t}=p_{i}^{2} \forall t \in[2, \tau]
\end{array}\right\}
$$

that we call the dynamic repetitive extension. We have $K(\mathbf{X}(\mathbf{t}))_{r p} \subseteq K(\mathbf{X}(\mathbf{t}))_{s t}$, as $K(\mathbf{X}(\mathbf{t}))_{r p}$ is more constrained. In practice, the strong extension assumes that the dynamic network is ill-defined and that its behaviour can change between time slices, while the repetitive extension assumes that we seek a precise classical DBN who is partially known.
Example 7. Consider the very simple example where $\mathcal{X}=\{0,1\}$ and the 2-slice network given in Figure 2, which is nothing else than a two-state imprecise Markov chain, and an observed value $X(1)=1$. Assume furthermore that we have three time slices $(\tau=3)$, that $X(1)=1$ is observed, and that

$$
\begin{gathered}
p(X(t)=1 \mid X(t-1)=0)=0.8 \\
p(X(t)=1 \mid X(t-1)=1) \in[0.2,0.5]
\end{gathered}
$$

That is, the transition rates from state 0 are precisely known, but not the one from state 1 (although staying in state 1 is clearly less likely). The different extreme points over $(X(1), X(2), X(3))$ resulting from the strong and repetitive extension are summarized in Table 2, in which we adopt the notation $x(t)$ for $X(t)=1$ for simplification purposes. Each cell of the table corresponds to a precise network obtained by a specific selection of extreme points. The non-specified transition probabilities can be retrieved by the formula $p(X(t)=1 \mid X(t-1)=1)=1-p(X(t)=0 \mid X(t-1)=1)$.

# 4.2.2. Inference algorithms in $D C N$ 

(D)CNs can be queried as in (D)BNs to get information about the state of a variable given evidence about other variables, with respect to the chosen network extension. However, the use of credal sets makes the updating problem much harder, as it becomes an optimization problem. As such, the computation of the lower bound on $p\left(\mathbf{X}_{Q} \mid \mathbf{X}_{E}\right)$ requires to minimize a fraction containing polynomials :


Table 2: Simple DCN extreme probabilities

$$
\underline{p}\left(\mathbf{X}_{Q}(t) \mid \mathbf{X}_{E}(t)\right)=\min _{p(\mathbf{X}(\mathbf{t})) \in K(\mathbf{X}(\mathbf{t}))_{\omega}} \frac{X_{i}(t) \in \mathbf{X}_{i}(\mathbf{t}), \mathbf{X}_{i} \mid t \in \mathbf{X}_{E}(t)}{\prod_{i=1}^{n} \prod_{t=1}^{i} p_{i}^{t}}
$$

with $p(\mathbf{X}(\mathbf{t})) \in K(\mathbf{X})_{\omega}$ belonging to the dynamic strong extension $(\omega=s t)$ or dynamic repetitive extension $(\omega \rightarrow r p)$ of the network. An upper bound can be obtained by maximizing (38). It is known that such a minimum (or maximum) is obtained at a vertex of the dynamic strong/repetitive extension. Depending on (1) the structure of network, (2) the number of modality of variables and (3) the chosen extension (strong/repetitive), the updating problem will be more of less complex to solve. Because inferences are already hard in static credal networks, little work has been done on DCNs [41]. By unrolling a two-time slice network over $T$ time steps, the number of possible vertex combinations goes from $\prod_{i, t=0} \# \mathcal{E} x t\left(K_{i}^{t}\right) \prod_{i, t=1} \# \mathcal{E} x t\left(K_{i}^{t}\right)$ in the case of repetitive independence, to $\prod_{i, t=0} \# \mathcal{E} x t\left(K_{i}^{t}\right) \prod_{i, t=1} \# \mathcal{E} x t\left(K_{i}^{t}\right)^{\tau-1}$ in the case of strong independence. Given the potential number of vertices, approximate algorithms seem more appropriate regarding DCNs.

Many algorithms, exact and approximate, have been proposed to deal with CN. Some are generalizations of well known (D)BNs algorithms. Among the approximate algorithms, there are those that compute inner bounds, i.e. bounds that are enclosed by the exact ones, outer bounds, which enclose the exact ones, and those that perform randomly. The 2 U algorithm [34] performs an exact rapid inference in the case of binary tree-shaped (D)CNs with the assumption of strong independence. The CCM transformation [15] turns a (D)CN into a (D)BN by adding transparent nodes before performing an Maximum A Posteriori (MAP) estimation over the latter to find the best combination of vertices. It has the same complexity as credal network in-

ference, that is $N P^{P P}$ Complete, and performs poorly with separately specified credal networks such as the one we used during our trials (because of the sheer number of vertices). Optimization techniques such as branch and bound over local vertices of credal sets [27, 13] are also well suited to medium-sized networks and can be stopped at any time to give an approximate answer. Other algorithms are based on a variable elimination scheme from (D)BNs, such as Separable Variable Evaluation [26, 55] which keeps the separately specified credal sets as separated as possible during propagation, and can be mapped to an integer or a multi-linear program [29, 28]. Regarding binary and DAG-shaped (DAG : Directed Acyclic Graph) credal networks, algorithm L2U (Loopy 2U) [44] (similar to LBP (Loopy Belief Propagation) [63]) produces either inner or outer approximations. Its efficiency is due both to the bounded cardinality of variables and to ignoring loops. Another way to handle credal sets complexity is to represent them by simpler means. Variational methods [43, 42] choose a family of functions to approximate the exact combination of credal sets to decrease computational costs. Those functions are optimized according to some criteria until convergence and the inference is then realized in the network with the original credal sets replaced by the new found functions. The $\mathrm{A} \backslash \mathrm{R}(+)$ algorithm [27] uses interval probability arithmetic to approximate credal sets in a propagation scheme in tree-shaped networks (with the use of some additional constraints limiting the information loss in its enhanced version). The intervals produced are outer bounds of the real ones. Although those algorithms are fast in medium-sized network, they either produce too many approximations or are too complex to work with DCNs. Another popular family of approximate algorithms producing inner bounds is based on MonteCarlo sampling [38]. Several methods have been proposed to better guide the search (simulated annealing [12], genetic algorithms [14]) among the vertices of the (conditional) local credal sets, but they require some tuning for more accurate results, otherwise they can lead to poor approximations.

Although there exist several inference algorithms, none allows to do inference in a realistic and practical way, on networks capable of representing global complex system of Life Sciences. In further inferences, we used a simple Monte-Carlo sampling algorithm [38] which has the advantage to be a good starting point, as it applies with the same easiness to dynamic repetitive and strong extensions (with a faster convergence for dynamic repetitive extension).

# 4.2.3. Robust parameter learning 

Let $p_{i j k}^{t}$ be the probability that $X_{i}(t)=x_{k}$, given that its parents have instantiation ${ }^{3} x_{j}$ (corresponding itself to a vector where $j$ represents the

[^0]
[^0]:    ${ }^{3}$ Possible values of variables according to its discretization.

vector of parents of $i$ ), i.e.

$$
\begin{array}{ll}
p_{i j k}^{t}=p\left(X_{i}(t)=x_{k} \mid \mathbf{U}_{i}(t)=x_{j}\right) & i=1, \ldots, n \\
& j=1, \ldots, c_{i} \\
& k=1, \ldots, r_{i}
\end{array}
$$

where $r_{i}$ is the number of values that node $i$ can take and $c_{i}$ is the number of distinct configurations of $\mathbf{U}_{i}(t)$. Parameter learning consists in estimating $p_{i j}^{t}$ faced with available information [45, 10]. For the sake of clarity, parameters $p_{i j}^{t}$ will be denoted $p_{i j}$ since parameters $p_{i j}^{t}$ are time-invariant in the case of repetitive extension assumption and it is sufficient to only consider information limited to each time slice in the case of strong extension assumption. According to section 2.2 , for all $i \in\{1, \ldots, n\}, j \in\{1, \ldots, c_{i}\}$ the credal set $\widetilde{K}_{\left(s_{l} ; \xi_{l}\right)_{l=0}^{m}}\left(X_{i} \mid \mathbf{U}_{i}=x_{j}\right)$ may be approximated by using the outer credal set $K_{\left(s_{l} ; \xi_{l}\right)_{l=0}^{m}}\left(X_{i} \mid \mathbf{U}_{i}=x_{j}\right)$ defined by

$$
K_{\left(s_{l} ; \xi_{l}\right)_{l=0}^{m}}\left(X_{i} \mid \mathbf{U}_{i}=x_{j}\right)=\left\{p_{i j}: p_{i j k} \in\left[\underline{p}_{i j k}, \bar{p}_{i j k}\right], \sum_{k} p_{i j k}=1\right\}
$$

where $\left[\underline{p}_{i j k}, \bar{p}_{i j k}\right]$ is estimated and updated from Eq. (19) according to the available sources of knowledge $\left(S_{0}, \ldots, S_{m}\right)$.

# 4.3. Practical robust parameter learning example 

Wood is essentially composed of cellulose (denoted $C$ ) that is a polymer whose quantity characterizes the nature of wood (denoted $T$ ) namely hardwood or softwood. Imagine that we want to determine the kind of wood according to its chemical composition tainted with uncertainties, that is we are interested in, $P(T \mid C)$. For the sake of clarity, we choose $C=\left\{x_{1}=\right.$ $\left.20 \%, x_{2}=40 \%(x)=60 \%\right\}$ meaning that there is $20 \%, 40 \%$ or $60 \%$ of cellulose inside wood, $P=\left\{x_{1}=\right.$ Soft, $\left.x_{2}=\mathrm{Hard}\right\}$ and all sources $s_{i}$ have the same confidence level, i.e. $s_{i}=1$ for all $i$. We thus need to estimate the following parameters:

$$
p_{j k}=p\left(T=x_{k} \mid C=x_{j}\right)
$$

according to the available knowledge described in the following. The credal sets $K\left(T \mid C=x_{j}\right)$ are initialized by

$$
K_{s_{0}}\left(T \mid C=x_{j}\right)=\left\{p_{j .}: p_{j k} \geq 0, \sum_{k} p_{j k}=1\right\}, \forall j=1, \ldots, 3
$$

1. Precise measures are provided $\{(20$, Soft $),(20$, Hard $),(40$, Hard $),(60$, Soft $)\}$ leading to update by Eq. (19)

- $K_{\left(s_{0}, s_{1}\right)}\left(T \mid C=20\right)=\left\{p_{1 .}: \frac{1}{4} \leq p_{11} \leq \frac{3}{4}, p_{12}=1-p_{11}\right\}$,

- $K_{\left(s_{0}, s_{1}\right)}(T \mid C=40)=\left\{p_{2 .}: 0 \leq p_{21} \leq \frac{1}{2}, p_{22}=1-p_{21}\right\}$,
- $K_{\left(s_{0}, s_{1}\right)}(T \mid C=60)=\left\{p_{3 .}: \frac{1}{2} \leq p_{31} \leq 1, p_{32}=1-p_{31}\right\}$.
2. A first expert says that the more cellulose there is, the harder the wood. This information may be formalized by means of the following fuzzy numbers or possibility distribution (see Section 3.2):
- $\pi(T=\operatorname{Hard} \mid C=20)=0.5, \quad \pi(T=\operatorname{Soft} \mid C=20)=1$
- $\pi(T=\operatorname{Hard} \mid C=40)=\pi(T=\operatorname{Soft} \mid C=40)=1$
- $\pi(T=\operatorname{Hard} \mid C=20)=1, \quad \pi(T=\operatorname{Soft} \mid C=20)=0.5$
meaning for instance that $P(T=\operatorname{Hard} \mid C=20) \leq 0.5$ leading to update
- $K_{\left(s_{0}, s_{1}, s_{2}\right)}(T \mid C=20)=\left\{p_{1 .}: \frac{1}{3} \leq p_{11} \leq \frac{5}{6}, p_{12}=1-p_{11}\right\}$,
- $K_{\left(s_{0}, s_{1}, s_{2}\right)}(T \mid C=40)=\left\{p_{2 .}: 0 \leq p_{21} \leq \frac{5}{3}, p_{22}=1-p_{21}\right\}$,
- $K_{\left(s_{0}, s_{1}, s_{2}\right)}(T \mid C=60)=\left\{p_{3 .}: \frac{1}{3} \leq p_{31} \leq \frac{5}{6}, p_{32}=1-p_{31}\right\}$.
3. A second expert provides more accurate estimation in terms of confidence
- $P(T=\operatorname{Soft} \mid C=20) \geq 95 \%$
- $P(T=\operatorname{Hard} \mid C=40) \geq 60 \%$
- $P(T=\operatorname{Hard} \mid C=60) \geq 95 \%$
which can be modeled again by a possibility distribution. This leads to update
- $K_{\left(s_{0}, s_{1}\right)}(T \mid C=20)=\left\{p_{1 .}: 0.49 \leq p_{11} \leq 0.875, p_{12}=1-p_{11}\right\}$,
- $K_{\left(s_{0}, s_{1}, s_{2}\right)}(T \mid C=40)=\left\{p_{2 .}: 0 \leq p_{21} \leq 0.6, p_{22}=1-p_{21}\right\}$,
- $K_{\left(s_{0}, s_{1}, s_{3}\right)}(T \mid C=60)=\left\{p_{3 .}: 0.25 \leq p_{31} \leq 0.64, p_{32}=1-p_{31}\right\}$.
4. Defective sensors and measurements provide joint imprecise observations, summarized in Table 3 and producing a joint belief function (Section 3.4).
From this information lower and upper probability bounds over parameters are given by

$$
\begin{aligned}
& \operatorname{Bel}(T=t \mid C=c)=\frac{\operatorname{Bel}(T=t, C=c)}{\operatorname{Bel}(T=t, C=c)+\sum_{t^{\prime} \neq t} \operatorname{Pl}\left(T=t^{\prime}, C=c\right)} \\
& \operatorname{Pl}(T=t \mid C=c)=\frac{\operatorname{Pl}(T=t, C=c)}{\operatorname{Pl}(T=t, C=c)+\sum_{t^{\prime} \neq t} \operatorname{Bel}\left(T=t^{\prime}, C=c\right)}
\end{aligned}
$$


Table 3: Focal sets occurrences

For example

$$
\begin{aligned}
& \operatorname{Bel}(T=\operatorname{Soft} \mid C=20)=\frac{1 / 68}{1 / 68+21 / 68}=0.045 \\
& \operatorname{Pl}(T=\operatorname{Soft} \mid C=20)=\frac{24 / 48}{24 / 48+2 / 48}=0.926
\end{aligned}
$$

Credal set $K_{\left(s_{0}, \ldots, s_{4}\right)}$ is then updated by

- $K_{\left(s_{0}, \ldots, s_{4}\right)}(T \mid C=20)=\left\{p_{1}: 0.1 \leq p_{11} \leq 0.89, p_{12}=1-p_{11}\right\}$,
- $K_{\left(s_{0}, \ldots, s_{4}\right)}(T \mid C=40)=\left\{p_{2}: 0.021 \leq p_{21} \leq 0.65, p_{22}=1-p_{21}\right\}$,
- $K_{\left(s_{0}, \ldots, s_{4}\right)}(T \mid C=60)=\left\{p_{3}: 0.2 \leq p_{31} \leq 0.67, p_{32}=1-p_{31}\right\}$.

5. Real-life case study

To illustrate the feasibility and practical use of our approach in a real case, we have focused on the ripening process of the Camembert type soft mould chees, that represents an ecosystem and a bioreactor difficult to apprehend from a global point of view [37, 52]. Based on recent works carried out by Baudrit et al. [5]; Sicard et al. [48], a simplified sub-structure of dynamic Bayesian networks has been extracted (see Figure 3) providing a qualitative representation of the coupled dynamics of yeast behaviour Kluyveromyces marxianus ( $K m$, colony forming unit/g of Fresh Cheese in decimal logarithmic scale) with its lactose substrate ( $l o, \mathrm{~g} / \mathrm{Kg}$ of Fresh Cheese) influenced by temperature $\left(T,{ }^{\circ} \mathrm{C}\right)$ inside the ripening chamber and involving odour changes ( $O d=\{$ Fresh,Mushroom,Camembert $\}$ ).

![img-2.jpeg](img-2.jpeg)

Figure 3: Structure of the dynamic credal network and the values of each variables representing the coupled dynamics Km growth versus lo consumptions influenced by temperature involving odour changes during the cheese ripening process ( $\mathrm{F}=\mathrm{Fresh}, \mathrm{M}=$ Mushroom, $\mathrm{C}=$ Camembert).

# 5.1. Parameter learning 

Assuming repetitive extension for computational reason mentioned in Section 4.2.2, we present, in the following, how parameters

$$
\begin{aligned}
& \boldsymbol{p}_{1}=p(K m(1)) \\
& \boldsymbol{p}_{2}=p(\text { lo }(1)) \\
& \boldsymbol{p}_{3}=p(T(1)) \\
& \boldsymbol{p}_{4}=p(\operatorname{Km}(2)|(\operatorname{Km}(1), l o(1), T(1))), \\
& \boldsymbol{p}_{5}=p(\text { lo }(2)|(\operatorname{Km}(1), l o(1), T(1))), \\
& \boldsymbol{p}_{6}=p(\operatorname{Od}(1)|(\operatorname{Km}(1), l o(1)))
\end{aligned}
$$

may be estimated by using the robust hybrid parameter learning when we have several sources of knowledge (denoted $S_{i}$ ) tainted with stochastic and epistemic uncertainty.

1. Initialization $\left(S_{1}\right)$.

All $\mathrm{OCN}^{-}$parameters are initialized by:

- An experimental database $S_{\text {experiments }}$ of six cheese ripening trials carried out for temperatures varying from $\mathrm{T}=8$ to $16{ }^{\circ} \mathrm{C}$ is available.
- the vacuous credal sets leading to bracket parameters by $[0,1]$ when no information is available.

With $s_{1}$ corresponding to the confidence level about experimental trials $S_{\text {experiments }}$, according to (19) we have:

$$
p_{i j k} \in\left[\frac{s_{1} f_{i j k}}{s_{0}+s_{1}}, \frac{s_{0}+s_{1} f_{i j k}}{s_{0}+s_{1}}\right]
$$

where $f_{i j k}$ represents the observed frequency corresponding to sample information in Table 1 and linked to Section 3.1.
2. Integration of partial mechanistic model tainted with uncertainties $\left(S_{2}\right)$. The yeast $K m$ is one of the dominant species in the yeast flora of Camembert cheeses and its principal activity is the consumption of lactose (lo) [46]. Models to determine the growth of microorganisms have been studied in the fermentation industry [58], and the description of the growth of $K m$ is obtained by performing material balances on biomass $K m$ and lactose $l o$ [3]:

$$
(S)\left\{\begin{array}{l}
\frac{d K m}{d t}=\mu \frac{l o}{K_{l o}+l o} K m-b \cdot K m \\
\frac{d l o}{d t}=-\frac{\mu}{l o} \frac{l o}{l o} K m
\end{array}\right.
$$

where $\mu$ (the maximum specific growth rate of $K m$ ), $K_{l o}(T)$ (the half saturation constant for growth), $b$ (the decay coefficient) and $\beta$ (the yield coefficient for $K m$ on lactose), depending on temperature, are tainted with stochastic and epistemic uncertainties, due to the natural variability of yeast population and the imperfection of the model. The background knowledge about parameters $\boldsymbol{p}_{\mathbf{1}}, \boldsymbol{p}_{\mathbf{2}}, \boldsymbol{p}_{\mathbf{4}}$ and $\boldsymbol{p}_{\mathbf{5}}$ are then updated regardless of the rest of network by using a simulated database $S_{\text {simulated }}$ resulting from Monte Carlo simulation coupled to interval analysis [4] leading to manage a joint random set $\left([\underline{K m}(t), \overline{K m}(t),[\underline{l o}(t), \overline{l o}(t)], T(t)\right)_{l}$ associated with mass $\nu_{l}=$ $1 / \# S_{\text {simulated }}$ such that for instance

$$
l_{4 j k}=\left[\frac{s_{1} f_{4 j k}+s_{2} \xi_{4 j k}}{s_{0}+s_{1}+s_{2}}, \frac{s_{0}+s_{1} f_{4 j k}+s_{2} \bar{\xi}_{4 j k}}{s_{0}+s_{1}+s_{2}}\right]
$$

where

$$
\xi_{4 j k}=\frac{b e l(j, k)}{b e l(j, k)+\sum_{l \neq k} p l(l, j)} \text { and } \bar{\xi}_{4 j k}=\frac{p l(j, k)}{p l(j, k)+\sum_{l \neq k} b e l(l, j)}
$$

and

$$
p l(j, k)=\sum_{l,\left[\underline{k m}(t+1), \overline{k m}(t+1)\right]_{l} \cap\left\{k m_{k}\right\} \neq \emptyset} \nu_{l}
$$

$\left[\underline{k m}(t), \overline{k m}(t)\right]_{l} \cap\left\{k m_{j}\right\} \neq \emptyset$
$\left[\underline{l o}(t), \overline{l o}(t)\right]_{l} \cap\left\{l o_{j}\right\} \neq \emptyset$
$T_{l}(t)=T_{j}$

and

$$
\begin{aligned}
& \operatorname{bel}(j, k)=\sum_{\substack{l,\left\{k m_{k}\right\} \subseteq[\underline{k m}(t+1), \overline{k m}(t+1)]_{l} \\
\left\{k m_{j}\right\} \subseteq[\underline{k m}(t), \overline{k m}(t)]_{l} \\
&\left\{l o_{j}\right\} \subseteq[\underline{l o}(t), \overline{l o}(t)]_{l} \\
& T_{l}(t)=T_{j}
\end{aligned}
$$

This kind information is linked to Sections 3.4, 4.3 and corresponds to Belief functions in Table 1.
3. Integration of expert knowledge, $\left(S_{3}\right)$.

In cheese ripening, as in every complex food process, most of the control measures are performed on the basis of the expert's sensory perceptions. Indeed, experts have in mind the ripening process that they oversee and they are able to explain part of the complex reactions through their perception of quality changes [10]. Expert elicitation [48] informs us that during the exponential growing of the yeast $K m$, a characteristic fresh or lactic odour is released. Mushroom odour appears when the concentration of the yeast $K m$ begins to stabilize and typical Camembert odour appears when the population of $K m$ begins to decay. From this qualitative information, general rules may be deduced such as "it is impossible to have a Camembert odour with a weak (resp. high) concentrations of $K m$ (resp. lo)". That means for several combinations of $K m$ and $l o$ concentrations, likely values about variable Odour may be formalized by means of possibility distributions $\pi_{\text {Odour }}(. \mid K m, l o)$. That is:

- When there is a high (resp. weak) concentration of lactose (resp. the yeast $K m$ ), having a fresh odour is the most plausible state, followed by Mushroom and Camembert odours, which can be formalized as the following possibility distribution:

$$
\begin{gathered}
\pi_{\text {Odour }}(\operatorname{Fresh} \mid j)=1 \\
\pi_{\text {Odour }}(\text { Mushroom } \mid j)=0.8 \\
\pi_{\text {Odour }}(\text { Camembert } \mid j)=0.2
\end{gathered}
$$

where $j=(K m \leq 6.5, l o \geq 8)$.

- When there is a medium concentration of lactose and $K m$, the Mushroom odour is the most plausible state but we cannot exclude having Fresh or Camembert odours, formalized by:

$$
\begin{gathered}
\pi_{\text {Odour }}(\text { Fresh } \mid j)=0.2 \\
\pi_{\text {Odour }}(\text { Mushroom } \mid j)=1 \\
\pi_{\text {Odour }}(\text { Camembert } \mid j)=0.2
\end{gathered}
$$

where $j=(K m=7,2<l o<8)$.

- When having very weak (resp. high) concentration of lactose (resp. the yeast $K m$ ), the Camembert odour is the most plausible state, followed by Mushroom and Fresh odours, formalized by:

$$
\begin{gathered}
\pi_{\text {Odour }}(\text { Fresh }|j)=0.2 \\
\pi_{\text {Odour }}(\text { Mushroom }|j)=0.8 \\
\pi_{\text {Odour }}(\text { Camembert }|j)=1
\end{gathered}
$$

where $j=(K m>7, l o<2)$.
Parameter $\boldsymbol{p}_{6}$ is then updated by using

$$
p_{6 j k} \in\left[\frac{s_{1} f_{6 j k}+s_{3} \xi_{6 j k}}{s_{0}+s_{1}+s_{3}}, \frac{s_{0}+s_{1} f_{6 j k}+s_{3} \xi_{6 j k}}{s_{0}+s_{1}+s_{3}}\right]
$$

where

$$
\bar{\xi}_{6 j k}=\pi_{\text {Odour }}(k \mid j) \text { and } \xi_{6 j k}=1-\max _{l \neq k} \pi_{\text {Odour }}(l \mid j)
$$

This kind of information is linked to the Section 3.2 and corresponds to possibilistic model in Table 4.

# 5.2. Inference results and discussion 

We attempt to estimate the lower and upper mean time evolution of $K m$, $l o$ and Odour for a temperature control according to the previous parameter learning. That is

$$
E(X(t) \mid \mathbf{U}(t))=\sum_{k} x_{k} p\left(X(t)=x_{k} \mid \mathbf{U}(t)\right)
$$

for the lower bounds where $X$ may be $K m, l o$, Odour; $\mathbf{U}(t)=(\operatorname{lo}(0), K m(0)$ , $T(0), \ldots, T(t)$ and

$$
p\left(X(t)=x_{k} \mid \mathbf{U}(t)\right)=\inf _{p \in K(X(t) \mid \mathbf{U}(t))} p\left(X(t)=x_{k} \mid \mathbf{U}(t)\right)
$$

by assuming $s_{0}=s_{1}=s_{2}=s_{3}=1$ and the repetitive independence, since we assume that transition probabilities remain the same along the process (there is no reason to assume a change in the bacteria population behaviour), but are ill-known due to insufficient experiments and information. Figure 4 displays the lower and upper simulated mean evolution of $K m, l o$, Odour versus experimental data over the cheese ripening carried out at $12^{\circ} \mathrm{C}$ each time a source of information is added. Supported by Table 4, we may observe that the imprecision of simulated results well decreases (characterized by the surface in gray).

![img-3.jpeg](img-3.jpeg)

Figure 4: Incremental DCN average simulation versus raw data (dotted) of $K m$, lactose (lo) and Odour for a ripening carried out at and $\mathrm{T}=12^{\circ} \mathrm{C}$ each time a new source of information is integrated.


Table 4: Area between the lower and upper bounds of the simulated mean time evolution

# 6. Conclusion 

There are complex dynamical processes for which no deterministic model describing the complete process exists. In such cases, dynamic credal networks are convenient models that allow to include expert knowledge, data and variable interaction in a single framework. They allow a faithful representation of incomplete knowledge or scarce data, that are inherent to the complexity of bio-physicochemical phenomena occurring in Life Sciences. In this paper, we attempted to implement a practical methodology coupling interval analysis and Dirichlet model in the framework of dynamical credal networks for building mathematical model capable of representing complex systems. Moreover, the concepts of dynamic repetitive and strong extensions have been proposed. While the latter can be seen as a straightforward extension of classical credal networks, the former considers repetitive independence to allow the model to preserve a temporal regularity. Methodology has been applied to a simplified real-case study concerning microbial population growth involving sensory evolution during cheese ripening. These experiments have shown that including information reduces imprecision about result simulations. Next tools should consider to manipulate, to combine convex sets in order to not lose information during incremental parameter learning. In further works, DCNs should enable us to determine the contribution of imprecision and/or incompleteness on the outcomes of a model in order to know if an ambiguous answer is due to a lack of information or due to a random phenomenon. That is, we plan to develop refined sensitivity analysis techniques based on their use. They should thus determine key variables and/or key phenomena for which it will be necessary to acquire more information. Finally, we also plan to investigate their usefulness in determining optimal commands.
