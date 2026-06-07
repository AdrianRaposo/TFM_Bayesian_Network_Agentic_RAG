# Original citation: 

Chatrabgoun, O., Hosseinian-Far, A., Chang, V., Stocks, Nigel G. and Daneshkhah, Alireza. (2017) Approximating non-gaussian bayesian networks using minimum information vine model with applications in financial modelling. Journal of Computational Science. Permanent WRAP URL:
http://wrap.warwick.ac.uk/93677

## Copyright and reuse:

The Warwick Research Archive Portal (WRAP) makes this work by researchers of the University of Warwick available open access under the following conditions. Copyright © and all moral rights to the version of the paper presented here belong to the individual author(s) and/or other copyright owners. To the extent reasonable and practicable the material made available in WRAP has been checked for eligibility before being made available.

Copies of full items can be used for personal research or study, educational, or not-for-profit purposes without prior permission or charge. Provided that the authors, title and full bibliographic details are credited, a hyperlink and/or URL is given for the original metadata page and the content is not changed in any way.

## Publisher's statement:

© 2017, Elsevier. Licensed under the Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International http://creativecommons.org/licenses/by-nc-nd/4.0/

## A note on versions:

The version presented here may differ from the published version or, version of record, if you wish to cite this item you are advised to consult the publisher's version. Please see the 'permanent WRAP URL' above for details on accessing the published version and note that access may require a subscription.

For more information, please contact the WRAP Team at: wrap@warwick.ac.uk

# Approximating Non-Gaussian Bayesian Networks using Minimum Information Vine Model with Applications in Financial Modelling 

O. Chatrabgoun ${ }^{\mathrm{a}}$, A. Hosseinian-Far ${ }^{\mathrm{b}}$, V. Chang ${ }^{\mathrm{c}}$, N. G. Stocks ${ }^{\mathrm{d}}$, A. Daneshkhah ${ }^{\text {e,* }}$<br>${ }^{a}$ Department of Statistics, Faculty of Mathematical Sciences $\mathcal{G}$ Statistics, Malayer University, Malayer, Iran<br>${ }^{b}$ School of Computing, Creative Engineering $\mathcal{G}$ Engineering, Leeds Beckett University, Leeds, LS6 3QR, UK<br>${ }^{c}$ Xi'an Jiaotong-Liverpool University, Suzhou, China<br>${ }^{d}$ School of Engineering, University of Warwick, Covetry CV4 7AL, UK<br>${ }^{e}$ Warwick Centre for Predictive Modelling, School of Engineering, University of Warwick, Coventry CV4 7AL, UK


#### Abstract

Many applications of financial modelling require to jointly model multiple uncertain quantities to present more accurate, near future probabilistic predictions required in decision making. Bayesian networks (BNs) and copulas are two common approaches to modelling joint uncertainties with probability distributions in financial and bushiness professions. In particular, the copulas have attracted more attentions due to their nice property of approximating the probability distribution of the data with heavy tail which is very common in financial applications (e.g., financial asset returns, risk analysis of capital allocation within a financial ordination). The standard multivariate copulae suffer from some serious limitations which made then unsuitable for multivariate modelling of the financial data. An alternative copula model is the pair-copula construction (PCC) model which is more flexible and efficient for multivariate modelling of financial data. The only restriction of PCC model is that selecting the best model when the number of variables increases becomes a computationally a challenging problem. Bauer et al. [3] address this issue by capturing conditional independences in the data, and propose a new model called Bayesian network PCC (BN-PCC) which provides more parsimonious models in different settings. This new model is structurally more flexible than PCC due to the benefit of including conditional independences by the data structure. In addition, the difficulty of computing conditional distributions in graphical models for non-Gaussian distributions can be eased using bivariate copulas. In this paper, we extend this approach further using the minimum information vine model which results in a more flexible and efficient approach


[^0]
[^0]:    *Corresponding author

    Email address: A.Daneshkhah@warwick.ac.uk (A. Daneshkhah)

in modelling multivariate dependencies of heavy-tailed distribution and tail dependence as observed in the financial data. We demonstrate that the extended model based on minimum information PCC can approximate any given non-Gaussian BN to any required degree of approximation. Unlike the method developed by Bauer et al. [3], the proposed model is more flexible and is not restricted to use the parametric pair-copula models, but pair-copulas can be approximated using the maximum entropy (or minimum information) concept given the limited observed data by truncating the corresponding polynomials/bases after $k$ terms to meet the restrictions imposed by the data and problem under study. We examine three different bases including ordinary polynomial, orthonormal and Fourier series and propose the best fitting model among them based on a goodness-of-fit criteria. Finally, we apply our method to modelling the global portfolio data from the perspective of an emerging market investor located in Brazil. The results show that the multivariate distribution approximated based on the proposed model in this paper is fitted far better other previously published methods.

# Keywords: 

Bayesian Network, Copula, Directed Acyclic Graph, Entropy, Orthonormal Series, Probabilistic Financial Modelling, Vine.

## 1. Introduction

Soft computing is a collection of methodologies, which aim to exploit uncertainty. Modelling multiple uncertainties using multivariate distributions is required in real life problems as a soft computing methods. Construction of multivariate distribution would help us to appropriately examine dependencies between multivariate data in the real world complexities. A natural way to model multivariate data is to use the method proposed in [24] which is known as Norta method (normal to anything). Norta transforms the marginal distribution function of the variable to normal, induces a dependence structure and then transforms back. This method ignores the difference between product moment and rank correlation matrices of the joint normal and for higher dimensions, the set of rank correlation matrices may not be positive definite.

In recent years, copulas have gained popularity in constructing multivariate distributions and survey dependency structures. In the well known Sklar's theorem [41], univariate distributions link to each other to construct multivariate distribution i.e. copula function is a multivariate distribution

function which is marginally distributed on the interval $[0,1]$ uniformly. One of the main advantages of the copula function is to separate dependency structure from marginal distributions. Moreover, by using copula function, some quantities such as tail dependency which is the dependency between extreme values of the variables, can be obtained. This kind of dependency in particular is very important in real life problems.

Unfortunately, multivariate copulas are not as rich as bivariate copula. Building higher dimensional copula is generally a challenging task, and choosing a parametric family for the given higher dimensional copula is rather more difficult and limited (see [19]). This drawback in modelling of multivariate data by using copula, motivated statisticians to apply a flexible multivariate copulas known as pair copula for modelling multivariate dependency. This graphical model which can be seen as a classical hierarchical model was firstly introduced by Joe [25] and was later formulated by Bedford and Cooke [6, 7]. Aas et al. [1] developed and called it pair copula or vine and also decomposed a general multivariate distribution based on it and proposed a method to perform inferences. This modelling structure is based on a decomposition of a multivariate density into a cascade of bivariate copula. Pair copula construction solves the limitation in construction of multivariate copula and also considers the dependency between pair of variables. Two common forms of the pair copula are D-vine and C-vine, (for more information see [31]).

Using vine to model multivariate distribution apart from the advantages mentioned above is suffering from this drawback that when the number of variables increases, the number of bivariate copulas increases by quadratic rate (i.e., as for $n$ variables we should use $n(n-1) / 2$ bivariate copula), and this is against parsimonious axiom in modelling.

To overcome these vine modelling challenges, Bauer et al. [3] and later Bauer and Czado [4] proposed the pair-copula construction for modelling multivariate distribution represented by a Bayesian network (BN) for non-Gaussian distributions. Their method also permits to include the conditional independence assumptions induced by a BN. This approach is very useful to construct non-Gaussian distribution in order to capture features such as tail behaviour and non-linear, asymmetric dependency. In order to tackle these challenges and for modelling non-Gaussian multivariate distribution, it is more plausible to represent the pair-copula construction model in terms of a DAG [3, 4]. The method addressed in $[3,4]$ also permits to include the conditional independence assumptions induced by a BN. This approach is very useful to construct non-Gaussian distribution in order to

capture features such as tail behaviour and non-linear, asymmetric dependency.
Bedford et al. [8] stated that the use of a parametric copula to model dependency is simply a translation of one difficult problem into another: instead of the difficulty of specifying the full joint distribution, we have the difficulty of specifying the copula. The only and main advantage is the technical one that copulas are normalized to have support on the unit square and uniform marginal distributions. As a result, restricting copula functions to a particular parametric class (Gaussian, multivariate $t$, etc.) makes the potential flexibility of the copula approach not being realized in practice.

To settle this concern, there have been recently several studies proposing various non-parametric methods to tackle the issues mentioned above. For instance, Kauermann et al. [28] proposed a semiparametric method by using the spline to estimate multivariate copula density. In order to achieve a good and smooth fit, the spline coefficients are first penalized, and uniform marginals of the copula density is then approximated by placing linear constraints on the spline coefficients which quadratic programming is then required to derive the fitted model. However, the main purpose of the method proposed in $[28,38]$ was to tackle the curse of dimensionality using a semi-parametric approach, but it was not fully successful in achieving it. It was shown that the proposed method shifts the problem a little bit so that computation on 3,4 (or 5) dimensions could be possible. In order to tackle the curse of dimensionality [38], the methodology was then applied to D-vines with penalized Bernstein polynomials or penalized B-splines, to estimate the bivariate copula density in each knot of the selected D-vine model [27]. However, the reported results are very promising, but there is no clear model selection algorithm. In addition, when there is weak dependency they do not perform well. Nagler et al. [39] extended the above approaches by applying them on the simplified vine copula models. Simplified vine copula models give rise to very flexible models which are often found to be superior to other multivariate copula models [1]. In order to make the model more tractable, one usually makes the simplifying assumption that the pair-copula densities do not change with conditional assumption [39]. There are several interesting factors driving the relative performance of the non-parametric estimators. The most important one is the strength of dependence. They concluded that the kernel estimators performed best, but do worse than penalized B-spline estimators when there is weak dependence or tail dependence.

Bedford et al. [8] proposed an alternative method based on using entropy copula (also known

as minimum information copula) that can be determined to any required degree of precision based on the available data (or expert judgements). The approach used in this paper, by contrast, allows a lot of flexibility in copula specification. It can be easily implemented in practice and it is only required to assume that the copula density of interest must be continuous and non-zero. Our constructive approach involves the use of entropy copulas that can be specified to any required degree of precision based on the data available. We illustrate properly that good approximation locally guarantees globally good approximation.

A natural way to build a minimum information copula or specifying dependency constraints is through the use of moments [8]. These can be specified either on the copula or on the underlying bivariate density. These moment constraints are considered as real-valued functions $\phi_{1}, \ldots, \phi_{k}$ which are required to take expected values $e_{1}, \ldots, e_{k}$, respectively. The expected values are either computed from the available data or specified based on the experts' beliefs.

In this paper, we improve the fitted multivariate density approximation proposed in $[3,4]$ using a newly developed approximation method based on the entropy method (see also [22]). The conditional and joint probabilities of the selected DAG structure can be specified by constructing a minimum information copula between the nodes of interests given their parents' sets. In this study, we assume that the DAG structure is learned using either search and score methods (Sparse Candidate Algorithm; and Greedy Search methods) or constraint based methods, including PC, MMPC algorithms, Fast algorithm, etc (e.g., see [14, 29, 22]). A minimum information copula can be represented in terms of Polynomial Series (PS), and more flexible ones including Orthonormal Polynomial Series (OPS) and Orthonormal Fourier Series (OFS). We demonstrate that the approximation accuracy will be notably increased using the minimum information copula. We verify our claim by comparing our approximation with the results illustrated in $[3,4]$ to model the global portfolio data from the perspective of an emerging market investor located in Brazil.

The present paper is organised as follows. In Section 2, we introduce the pair-copula decomposition associated with the non-Gaussian BN of multivariate data. In Section 3, we first briefly study the entropy copula and show that how it can be used to approximate a bivariate copula density. We then develop it further to approximate the multivariate distribution associated with the given non-Gaussian BN. We improve this approximation in Section 4, using PS and OPS basis functions and OFS. In Section 5, we apply our method for modelling the global portfolio data from

the perspective of an emerging market investor located in Brazil. We then exhibit our approximation flexibility by comparing it with the method presented in [3, 4]. Section 6 is dedicated to a simulation study. We finally conclude our study in Section 7.

# 2. Pair-copula construction for non-Gaussian Bayesian Networks 

Considering the above-mentioned vine's drawbacks in modelling multivariate data, it has been tried to develop a method through using the nice properties of graphical model and pair-copula, simultaneously. Hanea et al. [23] provided an opportunity to exploit the advantages of both worlds. Indeed, the purpose is to apply the conditional independence in graphs and the simplified vine structure. Simplified vine copula models give rise to very flexible models which are often found to be superior to other multivariate copula models [1]. In order to make the model more tractable, one usually makes the simplifying assumption that the pair-copula densities do not change with conditional assumption [39].

Graphical models [33] are probabilistic models in which conditional independence between variables can be shown using a simple graph, i.e. in a graphical model, vertex are the variables, and the conditional and the causal relationships between variables are shown by edges. Let's introduce the conditional independence concept as:
$X_{1}$ is said to be conditionally independent of $X_{2}$ given $X_{3}$, denoted by $\left(X_{1} \perp X_{2} \mid X_{3}\right)$, if for all configuration $x_{1}, x_{2}, x_{3}$ of the variable in $X_{1}, X_{2}, X_{3}$ satisfying $p\left(X_{3}=x_{3}\right)$, it holds

$$
p\left(X_{1}=x_{1} \mid X_{2}=x_{2}, X_{3}=x_{3}\right)=p\left(X_{1}=x_{1} \mid X_{3}=x_{3}\right)
$$

Equivalent definition for conditional independence can be stated as follow:

$$
p\left(X_{1}=x_{1}, X_{2}=x_{2} \mid X_{3}=x_{3}\right)=p\left(X_{1}=x_{1} \mid X_{3}=x_{3}\right) p\left(X_{2}=x_{2} \mid X_{3}=x_{3}\right)
$$

Bayesian networks models known as Directed acyclic graphical (hereafter DAG) and are certainly the most common and perhaps the most applicable version of a graphical model. The construction of the Bayesian networks was based on the assumption of a joint Gaussian distribution, however this approach lacks the necessary performance for capturing the features of real world data such as tail behaviour and non-linear, asymmetric dependencies. Bauer et al. [3] filled this gap and introduced non-Gaussian graphical model by combining useful properties of both pair-copula and

![img-0.jpeg](img-0.jpeg)

Figure 1: A DAG with 4 elements
DAG, and named it non-Gaussian DAG-PCC. Elidan [17, 18] gives another copula decomposition of distributions associated with a DAG that is based on generally higher variate copulas, and therefore lacks the flexibility of the pair-copula approach.

First, let us introduce some of the preliminary notations associated with graphical models, and also some of the basic concepts related to Bayesian networks. Further details on Bayesian network can be found in [14]. Applications of Bayesian networks range from artificial intelligence, decision support systems, and engineering to genetics, geology, medicine, and finance, see [40].

A graph is a pair $G=(V, E)$ where $V$ is the set of vertices (or nodes) and $E$ is the set of edges. The set of edges $E$ is a subset of the set $V \times V$ of ordered pair of nodes. It is assumed that $E$ contains only distinct pair of nodes so that there exists no loops, that is, $(x, y) \in E \Longrightarrow x \neq y$. Given two nodes $x$ and $y$, the edge between them is said to be directed if $(x, y) \in E$ but $(x, y) \notin E$, and written $x \longrightarrow y$. If the edges in each graph are all directed, such graph is called a directed one. Figure 1 illustrates a directed graph with vertices $V=\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}$. A cycle of length $n$ is a path (i.e. a path of length $n$ form $x$ to $y$ is a sequence $x=x_{0}=x_{1}=\ldots=x_{n}=y$ of distinct vertices such that $\left(x_{i-1}, x_{i}\right) \epsilon E$ for all $\left.i=1,2, \ldots, n\right)$ with the modification that the first and the last vertex are identical $x_{0}=x_{n}$. A directed graph $G=(V, E)$ is acyclic if it contains no directed cycle.

Given a DAG D, we define the set of descendants $d e(x)$ of $x$ are the vertices $y$ such that $x \longrightarrow y$ but not $y \longrightarrow x$ and the descendants of $x$ are the nodes $y$ such that there is a path from $x$ to $y$, but not from $y$ to $x$, and by similar definition non-descendants of $x$ or $n d(x)$ defined as

$n d(x)=V \backslash(d e(x) \bigcup x)$. For $x \longrightarrow y ; x$ is a parent of $y$ and $y$ is a child of $x$. The set of parents of a vertex $y$ is denoted by $p a(y)$, and the set of children of a vertex $x$ represented by $c h(x)$. For example in Figure 1, the set of parents of $X_{4}$ is $p a\left(X_{4}\right)=\left\{X_{2}, X_{3}\right\}$ and the set of children of $X_{3}$ is given by $c h\left(X_{3}\right)=\left\{X_{4}\right\}$.

We only consider the density decomposition related to DAG. Factorization of the multivariate density can be done by using the conditional independence concept. The basic decomposition scheme offered by a DAG can be explained based on the conditional independence. Consider a joint density function $f$ defined over $n$ variables $X_{1}, \ldots, X_{n}$. The multivariate density function $f$ can be decomposed as a product of $n$ conditional density functions as follows:

If $X_{i}$ is independent of all other predecessors given its parent then, we can write

$$
f\left(x_{1}, \ldots, x_{3}\right)=\prod_{i=1}^{n} f\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

i.e. once we know the value of $p a\left(x_{i}\right)$, knowing the value of the other preceding variables is redundant . This property of $f$ is known as Markovian or local Markov properties in the literature. We illustrate briefly that the density decomposition scheme associated with 4 random variables $X=\left(X_{1}, \ldots, X_{4}\right)$ with a joint density function $f\left(x_{1}, \ldots, x_{4}\right)$ are satisfying a DAG shown in Figure 1 and the marginal densities $f\left(x_{1}\right), \ldots, f\left(x_{4}\right)$. We make use of the expression

$$
f\left(x_{1}, \ldots, x_{4}\right)=f\left(x_{1}\right) f\left(x_{1} \mid x_{2}\right) f\left(x_{3} \mid x_{1}, x_{2}\right) f\left(x_{4} \mid x_{1}, x_{2}, x_{3}\right)
$$

The marginal distribution of $X_{1}$ is known, therefore $f_{1}$ is also known. The marginals of $X_{1}$ and $X_{2}$ are known, and the copula of $X_{1}, X_{2}$ is also known; therefore by applying Sklar's theorem we can get $f\left(x_{1}, x_{2}\right)$, and hence

$$
f\left(x_{1} \mid x_{2}\right)=c_{12}\left(F\left(x_{1}\right), F\left(x_{2}\right)\right) f_{2}\left(x_{2}\right)
$$

In order to get $f\left(X_{3} \mid X_{1}, X_{2}\right)$, based on the conditional independence $X_{2}$ and $X_{3}$ given $X_{1}$, we can write

$$
f\left(x_{3} \mid x_{1}, x_{2}\right)=f\left(x_{3} \mid x_{1}\right)=c_{13}\left(F\left(x_{1}\right), F\left(x_{3}\right)\right) f_{3}\left(x_{3}\right)
$$

Similarly, by using conditional independence between $X_{1}$ and $X_{4}$ given $X_{2}$ and $X_{3}$, holds that

$$
f\left(x_{4} \mid x_{1}, x_{2}, x_{3}\right)=f\left(x_{4} \mid x_{2}, x_{3}\right)
$$

Now, for $v \in V$, we order the elements of $p a(v)$ increasingly (with respect to some strict total order $<_{v}$ on $p a(x)$ ) and set

$$
p a(v, w)=\left\{u \in p a(v) \mid u<_{v} w\right\}, \quad w \in p a(v)
$$

These orders can be determined based on the Kendall's $\tau$ rank correlation between variable $v$ and $p a(v)$. For example, for $p a(4,3)=\{2\}$, we can write

$$
f\left(x_{4} \mid x_{2}, x_{3}\right)=c_{34 \mid 2}\left(F_{4 \mid 2}\left(x_{4} \mid x_{2}\right), F_{3 \mid 2}\left(x_{3} \mid x_{2}\right)\right) f_{4 \mid 2}\left(x_{4} \mid x_{2}\right)
$$

We can determine $f_{4 \mid 2}\left(x_{4} \mid x_{2}\right)$ in a similar way as $f_{2 \mid 1}\left(x_{2} \mid x_{1}\right)$ or $f_{3 \mid 1}\left(x_{3} \mid x_{1}\right)$. Therefore, $f$ can be decomposed as:

$$
\begin{aligned}
f\left(x_{1}, \ldots, x_{4}\right)=\prod_{i=1}^{4} f\left(x_{i}\right) & \times c_{12}\left(F\left(x_{1}\right), F\left(x_{2}\right)\right) \times c_{13}\left(F\left(x_{1}\right), F\left(x_{3}\right)\right) \\
& \times c_{24}\left(F\left(x_{2}\right), F\left(x_{4}\right)\right) \times c_{34 \mid 2}\left(F_{4 \mid 2}\left(x_{4} \mid x_{2}\right), F_{3 \mid 2}\left(x_{3} \mid x_{2}\right)\right)
\end{aligned}
$$

As a result, we can state the following theorem.
Theorem 1. . Let $D=(V, E)$ be a $D A G$ and let $f$ be a multivariate density function on $n$ variables with marginal density $f_{i}$ and corresponding cumulative distribution function $F_{i}, i=1,2, \ldots, n$. Then $f$ is uniquely determined by its univariate margins $f_{i}, \quad i=1,2, \ldots, n$ and its conditional pair-copula $c_{v w \mid p a(v, w)}, v \in V, w \in p a(v)$ and $f$ can be decomposed as follows:

$$
f\left(x_{1}, \ldots, x_{n}\right)=\prod_{v=1}^{n} f\left(x_{v}\right) \prod_{w \in p a(v)} c_{v w \mid p a(x, w)}\left(F_{v \mid p a(v, w)}, F_{w \mid p a(v, w)}\right)
$$

Proof. The proof of this theorem relies on graph theoretical considerations only (see [3] and references therein).

The above theorem gives us a constructive approach to build a multivariate distribution given a DAG: If we make choices of marginal densities and copula, then the above formula gives us a multivariate density. Hence, PCC-DAG can be used to model general multivariate densities. However, in practice, we have to use copula from a convenient class, and this class should ideally be the one that allows us to approximate any given copula to an arbitrary degree. In the following sections, we address this issue in more details. By having this class of copula, we can then approximate any multivariate distribution using a DAG.

When we apply Non Gaussian PCC-DAG for decomposing multivariate density $f$ as seen in Theorem 1, some of the copula may not exist as $C_{23}$ in Figure 1 and decomposition (1), i.e. since

the copula $C_{23}$ is not available in the decomposition of the $f$, Bauer et al. (2012) exploited the conditional independence property $\left(X_{2} \perp X_{3} \mid X_{1}\right)$ to get $F_{3 \mid 2}\left(x_{3} \mid x_{2}\right)$. This method proposed in [3] requires quite complex numerical computation, and there is no general closed-form solution for it. To overcome this challenge, we divide the support of $X_{2}$ to some bins and in each bin we calculate $F_{3 \mid 2}\left(x_{3} \mid x_{2}\right)$. Complete discussion are provided on the Brazilian case.

# 3. Approximating Multivariate Density: A minimum information copula approach 

This section outlines an approach based on using the entropy techniques originated from [9] in conjunction with the observed data or expert elicitation of observables. This is used to define a copula that can help to build the joint distribution of two random variables. It can also be used to develop it further for constructing a multivariate distribution using a Non-Gaussian PCCDAG model. The method that will be described below is based on using the $D_{1} A D_{2}$ algorithm to determine the copula in terms of potentially asymmetric information about two variables of interests.

### 3.1. The $D_{1} A D_{2}$ algorithm and minimum information copula

Bedford and Meeuwissen [9] applied a so-called $D A D$ algorithm to produce discretized entropy copula between two variables with given rank correlation. This approach relies on the fact that the correlation is determined by means of the symmetric function $U V$. The same approach can be used whenever we wish to specify the expectation of any symmetric function of $U$ and $V([5,34])$.

This method can be developed further using Borwein et al.'s idea [11] which enables us to have asymmetric specifications. In the revised method, we first determine a positive square matrix $A$, also called a kernel; two diagonal matrices $D_{1}$ and $D_{2}$ should be then found in such a way that the following product, $D_{1} A D_{2}$ is doubly stochastic. The theory can be easily generalised for continuous functions $[8,15]$.

Now, suppose there are two random variables $X$ and $Y$, with cumulative distribution functions $F_{X}$ and $F_{Y}$, respectively. These are the variables of interest that we would like to correlate by introducing constraints, based on some knowledge about functions of these variables. Suppose there are $k$ of these functions, namely $h_{1}^{\prime}(X, Y), h_{2}^{\prime}(X, Y), \ldots, h_{k}^{\prime}(X, Y)$, and that we wish either to calculate their mean values in terms of the observed data, or the expert wishes to specify mean

values $\alpha_{1}, \ldots, \alpha_{k}$ for all these functions, respectively. We can simply specify corresponding functions of the copula variables $U$ and $V$, defined by $h_{i}(U, V)=h_{i}^{\prime}\left(F_{1}^{-1}(U) ; F_{2}^{-1}(V)\right), \quad i=1,2, \ldots, k$, where $h_{i}:[0,1]^{2} \rightarrow \mathbb{R}$, at which we can specify the mean values $\alpha_{1}, \ldots, \alpha_{k}$ that these functions should simultaneously take. Further suppose that $h_{i}, h_{j}$ are linearly independent for $i \neq j$. We seek a copula that has these mean values, a problem which is usually either infeasible or undetermined. Hence, assuming feasibility for the moment, we also consider the copula to be maximum entropy (with respect to the uniform distribution), which guarantees a unique and reasonable solution. We form the kernel

$$
A(u, v)=\exp \left(\lambda_{1} h_{1}(u, v)+\ldots+\lambda_{k} h_{k}(u, v)\right)
$$

where $u$ denotes the realization of $U$ and $v$ the realization of $V$.
For practical implementations, we use the same method as proposed by [8], and later by [15] to discretize the set of $(u, v)$ values such that the whole domain of the copula is covered. Thus, the aforementioned kernel $A$ becomes a 2-dimensional matrix, and two matrices $D_{1}$ and $D_{2}$ should be then determined. As a result, the following product denoted by $P$ over $[0,1]^{2}$ becomes a doubly stochastic matrix which represents a discretized copula density

$$
P=D_{1} A D_{2}
$$

The $D_{1} A D_{2}$ algorithm can be used to generate a unique joint density with uniform marginals for each vector $\left(\lambda_{1}, \ldots, \lambda_{k}\right)$. The set of all possible expectation vectors $\left(\alpha_{1}, \ldots, \alpha_{k}\right)$ that could be taken by $\left(h_{1}, h_{2}, \ldots, h_{k}\right)$ under some probability distribution is convex, and that for every $\left(\alpha_{1}, \ldots, \alpha_{k}\right)$ in the interior of that convex set, there is a density with parameters $\left(\lambda_{1}, \ldots, \lambda_{k}\right)$ for which $\left(h_{1}, h_{2}, \ldots, h_{k}\right)$ take these values $[11,8,15]$.

We now explain the iterative algorithm required to approximate the mentioned copula density by this algorithm. Suppose that both $(u, v)$ are discretized into $n$ points, as $u_{i}$, and $v_{j}, \quad i, j=1, \ldots, n$ respectively. Then, we write $A=\left(a_{i j}\right), D_{1}=\operatorname{diag}\left(d_{1}^{(1)}, \ldots, d_{n}^{(1)}\right), D_{2}=\operatorname{diag}\left(d_{1}^{(2)}, \ldots, d_{n}^{(2)}\right)$, where $a_{i j}=A\left(u_{i}, v_{j}\right), d_{i}^{(1)}=D_{1}\left(u_{i}\right), d_{j}^{(2)}=D_{2}\left(v_{j}\right)$. We define the doubly stochastic matrix, $D_{1} A D_{2}$ with the uniform marginals as follows

$$
\begin{gathered}
\forall i=1, \ldots n \sum_{j} d_{i}^{(1)} d_{j}^{(2)} a_{i j}=1 / n, \quad \text { and } \\
\forall j=1, \ldots n \sum_{i} d_{i}^{(1)} d_{j}^{(2)} a_{i j}=1 / n
\end{gathered}
$$

The idea behind $D_{1} A D_{2}$ algorithm is simple. It starts with arbitrary positive initial matrices for $D_{1}$ and $D_{2}$, and the new vectors will be then successively defined by iterating the following maps

$$
d_{i}^{(1)} \mapsto \frac{1}{n \sum_{j} d_{j}^{(2)} a_{i j}}(i=1, \ldots, n), \quad d_{j}^{(2)} \mapsto \frac{1}{n \sum_{i} d_{i}^{(1)} a_{i j}}, \quad(j=1, \ldots, n)
$$

It can be shown that this iteration scheme converges geometrically to the requested vectors [11].
Note that to compare different discretizations (for different $n$ 's) we should multiply each cell weight $d_{i}(1) d_{j}(2) a_{i j}$ by $n^{2}$ as this quantity approximates the continuous copula density with respect to the uniform distributions.

The mapping from the set of vectors of $\lambda$ 's onto the set of vectors of the resulting expectations of functions $\left(h_{1}, \ldots, h_{k}\right)$ has to be found numerically. Bedford et al. [8] proposed the optimization techniques for determining the $\lambda_{i}$ 's and the corresponding copula. The expectations $\alpha_{i}$ of $k$ functions of variables $X$ and $Y$ are given by

$$
E\left[h_{i}^{\prime}(X, Y)\right]=E\left[h_{i}(U, V)\right]=\alpha_{i}, \quad i=1, \ldots, k
$$

We now wish to determine the appropriate set of $\lambda$ 's for the given expectations $\alpha_{i}$, where the expectations have been calculated using the discrete copula density $D_{1} A D_{2}$ given in (4). Hence, to determine $\lambda_{i}$ 's satisfying the constraints, the following set of equations has to be solved

$$
L_{l}\left(\lambda_{1}, \ldots, \lambda_{k}\right)=\frac{1}{n^{2}} \sum_{i=1}^{n} \sum_{j=1}^{n} P\left(u_{i}, v_{j}\right) h_{l}\left(u_{i}, v_{j}\right)-\alpha_{l}, \quad l=1,2, \ldots, k
$$

The left hand sides of the above equations are just functions of $\lambda$ 's and with optimization algorithms their roots can be found. One of the possible solvers for this task would be FSOLVE - MATLAB's optimization routine. An alternative method is to use another MATLAB's optimization procedure called FMINSEARCH, which implements the Nelder-Mead simplex method [32]. The minimized function is then

$$
L_{\text {sum }}\left(\lambda_{1}, \ldots, \lambda_{k}\right)=\sum_{l=1}^{k} L_{l}^{2}\left(\lambda_{1}, \ldots, \lambda_{k}\right)
$$

We refer the interested readers to $[8,34]$ to show how an expert could specify a copula through defining expected values.

# 3.2. Approximating Multivariate Density by Non-Gaussian PCC-DAG 

In this section, we use techniques from approximation theory to show that any $n$-dimensional multivariate density which is $C^{2}$ (that is, twice differentiable, with continuous second derivatives)

can be approximated arbitrarily well pointwise using a finite parameter set of 2-dimensional copulas in a PCC-DAG construction. The basic idea is that we can use a series expansion, like a twodimensional Ordinary Polynomial Series (PS), Orthonormal Polynomial Series (OPS) and Fourier Series (OFS) , to approximate any log-density function by truncating the series at an appropriate point. What is non-trivial, however, about this method, is that the same truncation can be used everywhere in a PCC-DAG construction giving an overall uniform pointwise approximation. Hence our method allows the use of a fixed finite dimensional family of copulas to be used in a PCC-DAG construction, with the promise of a uniform level of approximation. Since the approximations we make of copula densities might not be quite copula densities themselves, we need to transform them to make them copulas.

To demonstrate this, we first should show that the family of bivariate (conditional) copula densities contained in a given multivariate distribution forms a compact set in the space of continuous functions on $[0,1]^{2}$. Then, it can be shown that the same finite parameter family of copulae can be used to derive a given level of approximation to all conditional copulae simultaneously.

Here, we develop the approximation method used in $[8,15]$ to approximate any log-density function at a desired level of approximation which is more accurate and exhibits better properties. We first introduce the notations. The basic assumption is that all densities are continuous. We denote $\mathcal{C}(Z)$ as the space of continuous real valued functions on a space $Z$, where $Z=[0,1]^{r}$ for some $r$, and the corresponding norm on $\mathcal{C}(Z)$ is given by

$$
\left\|f_{1 \ldots r}\right\|=\sup \left|f_{1 \ldots r}\left(x_{1}, \ldots, x_{r}\right)\right|
$$

The set of all possible 2-dimensional (conditional) copulae is denoted by

$$
\mathcal{C}(f)=\left\{c_{i j \mid i_{1} \ldots i_{r}}: 1 \leq i, j, i_{1}, \ldots, i_{r} \leq n, i, j \neq i_{1}, \ldots, i_{r}\right\}
$$

where $c_{i j \mid i_{1} \ldots i_{r}}$ is the copula of the conditional density of $X_{i}, X_{j}$ given $X_{i_{1}}, \ldots, X_{i_{r}}$.
The famous Arzela-Ascoli theorem can be used to check the compactness of the following function space, $K \subset C\left([0,1]^{2}\right)$. This space is relatively compact, if the functions in $K$ are equicontinuous and pointwise bounded. Further details about equicontinuous and pointwise bounded of the minimum information copula density can be found in [8].

It can be shown that the following two spaces are relatively compact (Theorem 3 in [8]).

$$
\mathcal{M}(f)=\left\{f_{i \mid i_{1} \ldots i_{r}}: 1 \leq i, i_{1}, \ldots, i_{r} \leq n, i \neq i_{1}, \ldots, i_{r}\right\}
$$

and

$$
\mathcal{B}(f)=\left\{f_{i j \mid i_{1} \ldots i_{r}}: 1 \leq i, j, i_{1}, \ldots, i_{r} \leq n, i, j \neq i_{1}, \ldots, i_{r}\right\}
$$

where $f_{i \mid i_{1} \ldots i_{r}}$ is the conditional density of $X_{i}$ given $X_{i_{1}}, \ldots, X_{i_{r}}$, and $f_{i j \mid i_{1} \ldots i_{r}}$ is the conditional density of $X_{i}, X_{j}$ given $X_{i_{1}}, \ldots, X_{i_{r}}$.

It is then straightforward to show that the set $\mathcal{C}(f) \subset C\left([0,1]^{2}\right)$ is relatively compact. In addition, since all the functions in $\mathcal{C}(f)$ are positive and uniformly bounded away from 0 , the set $\mathcal{L N C}(f)=\{\ln (g): g \in \mathcal{C}(f)\} \subset C\left([0,1]^{2}\right)$ is also relatively compact (see [8] for details and proofs).

As a result, the set $C\left([0,1]^{2}\right)$ can be considered as a vector space, and in this context a base is simply a sequence of functions $h_{1}, h_{2}, \cdots \in C\left([0,1]^{2}\right)$ such that any function $g \in C\left([0,1]^{2}\right)$ can be written as $g=\sum_{i=1}^{\infty} \lambda_{i} h_{i}$. In other words, it can be shown that given $\epsilon>0$, there is a $k$ such that any member of $\mathcal{L N C}(f)($ or $\mathcal{C}(f))$ can be approximated to within error $\epsilon>0$ by a linear combination of $h_{1}, h_{2}, \ldots, h_{k}$. There are lots of possible bases. We introduce three of these bases, PS, OPS and OFS in the next three subsections with some nice properties in their density approximation.

It should be noticed that the copula density approximated by the method described above might not be a copula density itself. Therefore,the resulting approximation needs to be transformed in such a way to obtain a copula. This can be done by weighting the approximated density. One of the most effective weighting schemes is the $D_{1} A D_{2}$ algorithm mentioned in the previous section. If we have a continuous positive real valued function $A(u, v)$ on $[0,1]^{2}$, then there are continuous positive functions $d_{1}(u)$ and $d_{2}(v)$, such that $d_{1} . d_{2} . A$ is a copula density, that is, it has uniform marginal distributions. This density is called $C$-Projection of $A$ and denoted by $\mathcal{C}(A)$. Bedford et al. [8] present the following lemma in which it allows us to control the error made when approximating a copula by another function.

Lemma 1. Let $g$ be a non-negative continuous copula density. Given $\epsilon>0$, there is a $\delta$ such that if $\|g-f\|<\delta$ then $\|g-C(f)\|<\epsilon$.

Note that these reweighting functions have the same differentiability properties as the function $f$ being reweighted. This can be seen from the integral equation that they satisfy:

$$
d^{(1)}(u)=\frac{1}{\int d^{(2)}(v) f(u, v) d v} \quad \text { and } \quad d^{(2)}(v)=\frac{1}{\int d^{(1)}(u) f(u, v) d u}
$$

Eventually, the term given in (2) can be used to show that good approximation of each conditional copula would result in a good approximation of the multivariate density of interest by using PCCDAG.

# 4. Building approximations using maximum entropy distributions 

In this section, we provide a practical guide for building a maximum entropy PCC-DAG structure to approximate any multivariate distribution. In the previous section, we presented a method proposed in [8] that all conditional copulae can be approximated using linear combinations of basis functions. In this section, we are going to address the issue of how the appropriate parameter values can be chosen. We will also introduce a practical and efficient alternative, based on using the entropy criterion that lies very close to the approach described above. In other words, given the basis functions $\left\{1, h_{1}, \ldots, h_{k}\right\}:[0,1]^{2} \rightarrow \mathbb{R}$, we seek values $\lambda_{1}, \ldots, \lambda_{k}$ so that $\exp \left(\sum_{1}^{k} \lambda_{i} h_{i}\right)$ is close to the approximated copula density. This can be done by fitting the moments of $h_{i}$ in the entropy framework. Therefore, if $E_{y}\left[h_{i}(u, v)\right]=\alpha_{i}$, we seek for the entropy copula density that also has these moments. This copula density can be uniquely determined, using the $D_{1} A D_{2}$ algorithm, hence

$$
d^{1}(u) d^{2}(v) \exp \left(\sum_{1}^{k} \lambda_{i} h_{i}(u, v)\right)
$$

As mentioned above, a multivariate distribution can be modelled by a PCC-DAG structure where it can be defined as a decomposition of the given multivariate distribution into certain conditional copulae. The following algorithm has summarised the steps for approximating the given multivariate distribution associated with a PCC-DAG structure:

1. Specify a basis family, denoted by $\mathcal{S}(k)=\left\{h_{1}, h_{2}, \ldots\right\}$,
2. Specify a DAG structure,
3. For each part of the DAG, the bivariate copulae, specify either

- mean $\alpha_{1}, \ldots, \alpha_{k}$ for $h_{1}, \ldots, h_{k}$ on each pairwise copula;
- functions $\alpha_{m}\left(j i \mid D_{e}\right)$ for the mean values as functions of the conditioning variables, for $m=1, \ldots, k$.

One of the main aspect that would effect the aforementioned approximation is the basis family. Here, we examine the impact of three basis families, the ordinary polynomial series, the orthonormal

polynomial series and Fourier on approximating the entropy copulae and the multivariate distribution associated with the chosen DAG structure. We first briefly introduce these three basis functions.

# 4.1. Ordinary Polynomial base 

One of the simple basis that can be applied in entropy copula is ordinary polynomial basis. These basis were mainly used in [8] and can be defined simply as follows:

$$
\psi_{0}(u)=1, \psi_{1}(u)=u, \psi_{2}(u)=u^{2}, \psi_{3}(u)=u^{3}, \psi_{4}(u)=u^{4}, \ldots
$$

PS basis are so easy to determine and selecting it by expert judgement can be easier than other basis.

### 4.2. Orthonormal polynomial base

In mathematics, particularly numerical analysis, a basis function is an element of the basis for a function space. The term is a degeneration of the term basis vector for a more general vector space; that is, each function in the function space can be represented as a linear combination of the basis functions. We say two polynomial functions $g_{1}$ and $g_{2}$ are orthonormal in the interval $[0,1]$, if

$$
\int_{0}^{1} g_{1}(u) g_{2}(u) d u= \begin{cases}1 & \text { for } \quad g_{1}(u)=g_{2}(u) \\ 0 & \text { for } \quad g_{1}(u) \neq g_{2}(u)\end{cases}
$$

The OPS base can be calculated more conveniently than some natural basis. In fact, if the basis is an OPS basis, adding a new item to the expansion does not change the coefficient of the already found shorter expansion [21]. But, if the basis is not orthonormal, any new item in general has a nonzero projection on previous items. It means that the already found coefficients of the expansion would have to be changed. That is one of the reasons for using OPS basis functions as the basis family, $\mathcal{S}(k)$. It is reasonable to consider Gram-Schmidt OPS basis which is one of the famous OPS basis functions on $[0,1]$.

To construct this OP basis over the interval $[0,1]$, we use the Gram-Schmidt process as follows

$$
\begin{gathered}
\varphi_{0}(u)=1 \\
\varphi_{n}(u)=\frac{u^{n}-\sum_{j=0}^{n-1} \frac{\int_{0}^{1} u^{n} \varphi_{j}(u) d u}{\int_{0}^{1} \varphi_{j}^{2}(u) d u} \varphi_{j}(u)}{\left\|u^{n}-\sum_{j=0}^{n-1} \frac{\int_{0}^{1} u^{n} \varphi_{j}(u) d u}{\int_{0}^{1} \varphi_{j}^{2}(u) d u} \varphi_{j}(u)\right\|} \quad n \geq 1
\end{gathered}
$$

The first few functions are

$$
\begin{gathered}
\varphi_{0}(u)=1 \\
\varphi_{1}(u)=\sqrt{3}(-1+u) \\
\varphi_{2}(u)=\sqrt{5}\left(1-6 u+6 u^{2}\right) \\
\varphi_{3}(u)=\sqrt{7}\left(-1+12 u-30 u^{2}+20 u^{3}\right) \\
\varphi_{4}(u)=\sqrt{9}\left(1-20 u+90 u^{2}-140 u^{3}+70 u^{4}\right) \\
\varphi_{5}(u)=\sqrt{11}\left(-1+30 u-210 u^{2}+560 u^{3}-630 u^{4}+252 u^{5}\right)
\end{gathered}
$$

# 4.3. Fourier base 

Trigonometric or Fourier basis is the other type of orthonormal basis. Computational speed of these basis for some data is considerable. Especially, these basis function present appropriate fit in the peridic data. The first functions are

$$
\begin{array}{ll}
\phi_{0}(u)=1, & \phi_{1}(u)=\sqrt{2} \cos (2 \pi u), \quad \phi_{2}(u)=\sqrt{2} \sin (2 \pi u) \\
\phi_{3}(u)=\sqrt{2} \cos (4 \pi u), & \phi_{4}(u)=\sqrt{2} \sin (4 \pi u) \\
\phi_{5}(u)=\sqrt{2} \cos (6 \pi u), & \phi_{6}(u)=\sqrt{2} \sin (6 \pi u)
\end{array}
$$

## 5. Application: Global portfolio data from the perspective of an emerging market investor located in Brazil

In this section, we apply the approximation method presented in this paper using OP, OPS and OFS basis families, $\mathcal{S}(k)$ (as mentioned in the first step in the algorithm above) to approximate the multivariate distribution associated with the selected PCC-DAG structure corresponding to the global portfolio data from the perspective of an emerging market investor located in Brazil. We then exhibit the potential flexibility of our approach by comparing it with the method cited in $[3,4]$.

![img-1.jpeg](img-1.jpeg)

Figure 2: Selected DAG structure for six dimensional contemporaneous daily log-returns of the global portfolio data from the perspective of an emerging market investor located in Brazil.

Example: In this example, we use the same data set as previously studied in [37] to illustrate the approximation method introduced in this paper. The data consists of six dimensional contemporaneous daily log-returns: Brazilian composite hedge fund index (the ACI, Arsenal Composite Index), a long-term inflation-indexed Brazilian treasury bonds index (the IMA-C index, computed by the Brazilian Association of Financial Institutions, Andima), Brazilian stock index with the 100 largest capitalization companies (IBRX), Index of large world stocks computed by MSCI (WLDLg), Index of small capitalization world companies computed by MSCI (WLDSm), and index of total returns on US treasury bonds computed by Lehman Brothers Barra (LBTBond). They are recorded over the period January 2, 2002 to October 20, 2008 in which 1629 data are collected. We denote these six variables ACI, IMA, IBrX, Wldlg, WLdSm and LBIBond, respectively.

We shall first remove serial correlation in these six time series, that is, the observation of each variable must be independent over time. Hence, the serial correlation in the conditional mean and the conditional variance are modelled by an $\operatorname{AR}(1)$ and a $\operatorname{GARCH}(1,1)$ model (see [10]), respectively. Thus, the following model for log-return $x_{i}$ is considered for the $i^{t h}$ time series

$$
\begin{gathered}
x_{i, t}=c_{i}+\alpha_{i} x_{i, t-1}+\sigma_{i, t} z_{i, t} \\
E\left[z_{i, t}\right]=0 \quad \text { and } \quad \operatorname{Var}\left[z_{i, t}\right]=1 \\
\sigma_{i, t}^{2}=\alpha_{i, 0}+a_{i} \epsilon_{i, t-1}^{2}+b_{i} a \sigma_{i, t-1}^{2}
\end{gathered}
$$

where $\epsilon_{i, t-1}=\sigma_{i, t}+z_{i, t}[1]$.
The further analysis is performed on the standardized residuals $z_{i}$. If the $\operatorname{AR}(1)-\operatorname{GARCH}(1,1)$ models are successful at modelling the serial correlation in the conditional mean and the conditional variance, there should be no autocorrelation left in the standardized residuals and squared standardized residuals. We can use the modified Q-statistic and the Lagrange multiplier test, respectively, to confirm this [1]. For all series, the null hypothesis, 'no autocorrelation left for the both tests', cannot be rejected with $\% 5$ significance. Since, we are mainly interested in estimating the dependence structure of the risk factor, the standardized residual vectors are converted to the uniform variables using the kernel method before further modeling. We denote the converted time series of ACI, IMA, IBrX, Wldlg, WLdSm and LBIBond by 1,2,3,4,5 and 6, respectively.

Here, we want to generate a PCC-DAG approximation fitted to this data set using entropy distributions based on the different basis. Indeed, the real challenge is in connecting DAG models to vines. We try to specify DAG structure in our data. One approach is to apply structure learning algorithms such as the PC algorithm (see [42], Section 5.4.2) to the data $\Phi^{-1}$ (.), where $\Phi$ denotes the standard normal cdf. This transformation is needed, since the tests for conditional independence performed by the PC algorithm(at the $\% 5$ significance level) are based on the assumption of normality. As an alternative approach, expert knowledge is frequently exploited to define the DAG (see [30], Chapter 5). Moreover, there are structure selection algorithms for Non Gaussian DAG's available in Bauer and Czado (2016) which are similarly based on the PC algorithm. We adopt the DAG structure presented in Figure 2 by applying the PC algorithm. Furthermore, the presented structure for non Gaussian DAG available in Bauer and Czado (2016) produces the same results. According to the presented DAG, we decompose the multivariate density of our data by applying Theorem 1 in order to derive PCC-DAG structure i.e. given the presented DAG, Theorem 1 prescribes which pair copulas are required to be specified in the definition of our model. Note that variable 1(ACI) has three parents (2(IMA), 3(IBrX), and 5(WldSm)) as the order of the parents based on the heuristic rule of modelling strong bivariate dependences prior to weak dependences. Our decision was based on estimates $\widehat{\tau}$ of kendall's $\tau$ variable 1,5 $(\widehat{\tau}=0.209)$, variable 1,3 $(\widehat{\tau}=0.197)$, and variable 1,2 $(\widehat{\tau}=0.127)$, respectively. Similar rule can be applied for variables 3 (IBrX) and its parents (2(IMA) and 4(WLdLg) based on $\widehat{\tau}$ as $\widehat{\tau}_{32}=0.0858$, and $\widehat{\tau}_{34}=0.424$. Moreover, variable 5 has two parents (3(IBrX) and 4(WIdIg)) which are $\widehat{\tau}_{53}=0.402$ and $\widehat{\tau}_{54}=0.75$.

Based on these ordering, and according to the measure of dependencies kendall's $\tau$, the resulting multivariate density decomposition is:

$$
\begin{gathered}
f_{1, \ldots, 6}\left(x_{1}, \ldots, x_{6}\right)=\prod_{i=1}^{6} f_{i}\left(x_{i}\right) \times c_{15}\left(F_{1}\left(x_{1}\right), F_{5}\left(x_{5}\right)\right) \times c_{45}\left(F_{4}\left(x_{4}\right), F_{5}\left(x_{5}\right)\right) \times c_{46}\left(F_{4}\left(x_{4}\right), F_{6}\left(x_{6}\right)\right) \\
\times c_{34}\left(F_{3}\left(x_{3}\right), F_{4}\left(x_{4}\right)\right) \times c_{13 \mid 5}\left(F_{1 \mid 5}\left(x_{1} \mid x_{5}\right), F_{3 \mid 5}\left(x_{3} \mid x_{5}\right)\right) \times c_{23 \mid 4}\left(F_{2 \mid 4}\left(x_{2} \mid x_{4}\right), F_{3 \mid 4}\left(x_{3} \mid x_{4}\right)\right) \\
\times c_{35 \mid 4}\left(F_{3 \mid 4}\left(x_{3} \mid x_{4}\right), F_{5 \mid 4}\left(x_{5} \mid x_{4}\right)\right) \times c_{12 \mid 35}\left(F_{1 \mid 35}\left(x_{1} \mid x_{3}, x_{5}\right), F_{2 \mid 35}\left(x_{2} \mid x_{3}, x_{5}\right)\right)
\end{gathered}
$$

We now derive the entropy copulae in association with some moment constraints between copula variables $1,2,3,4,5,6$ in the density decomposition (7). We initially construct maximum entropy copulas for unconditional copula $c_{15}, c_{46}, c_{34}, c_{45}$. Now, is essential to decide which bases should be taken and how many discretization points should be used in each case. We start to outline our procedure for the unconditional copula $c_{15}$. Other unconditional copula $c_{46}, c_{34}, c_{45}$ can be followed in a similar way.

We could simply choose basis functions based on the method described in [15] i.e. starting with simple bases, and moving to more complex ones, and including them until we are satisfied with our approximation. Our OP basis functions are as follows,

$$
\begin{gathered}
\psi_{1}(.) \psi_{1}(.), \psi_{1}(.) \psi_{2}(.), \psi_{2}(.) \psi_{1}(.), \psi_{1}(.) \psi_{3}(.), \psi_{3}(.) \psi_{1}(.) \\
\psi_{2}(.) \psi_{2}(.), \psi_{2}(.) \psi_{3}(.), \psi_{3}(.) \psi_{2}(.), \psi_{1}(.) \psi_{4}(.), \psi_{4}(.) \psi_{1}(.) \\
\psi_{1}(.) \psi_{5}(.), \psi_{5}(.) \psi_{1}(.), \psi_{2}(.) \psi_{4}(.), \psi_{4}(.) \psi_{2}(.), \psi_{3}(.) \psi_{3}(.), \ldots
\end{gathered}
$$

OPS basis function constructed using Gram-Schmidt process

$$
\begin{gathered}
\varphi_{1}(.) \varphi_{1}(.), \varphi_{1}(.) \varphi_{2}(.), \varphi_{2}(.) \varphi_{1}(.), \varphi_{1}(.) \varphi_{3}(.), \varphi_{3}(.) \varphi_{1}(.) \\
\varphi_{2}(.) \varphi_{2}(.), \varphi_{2}(.) \varphi_{3}(.), \varphi_{3}(.) \varphi_{2}(.), \varphi_{1}(.) \varphi_{4}(.), \varphi_{4}(.) \varphi_{1}(.) \\
\varphi_{1}(.) \varphi_{5}(.), \varphi_{5}(.) \varphi_{1}(.), \varphi_{2}(.) \varphi_{4}(.), \varphi_{4}(.) \varphi_{2}(.), \varphi_{3}(.) \varphi_{3}(.), \ldots
\end{gathered}
$$

and then considered OFS basis functions are:

$$
\begin{gathered}
\phi_{1}(.) \phi_{1}(.), \phi_{1}(.) \phi_{2}(.), \phi_{2}(.) \phi_{1}(.), \phi_{1}(.) \phi_{3}(.), \phi_{3}(.) \phi_{1}(.) \\
\phi_{2}(.) \phi_{2}(.), \phi_{2}(.) \phi_{3}(.), \phi_{3}(.) \phi_{2}(.), \phi_{1}(.) \phi_{4}(.), \phi_{4}(.) \phi_{1}(.) \\
\phi_{1}(.) \phi_{5}(.), \phi_{5}(.) \phi_{1}(.), \phi_{2}(.) \phi_{4}(.), \phi_{4}(.) \phi_{2}(.), \phi_{3}(.) \phi_{3}(.), \ldots
\end{gathered}
$$

Following the explanations to select basis function in an optimal manner, we add the basis functions by using stepwise method in [15]. In this method, at each stage, we propose to assess the loglikelihood of adding each additional basis function. We then include the function which produces the largest increase in the log-likelihood. Also, according to [15], in order to get optimal results, first four bases have been considered.

We are now able to construct the entropy copula density $C_{15}$ with respect to the uniform distributions given the corresponding OP, OPS and OFS constraints above, using the method described in this paper. We are initially required to determine the number of discretization points (grid size). Clearly, a larger grid size will provide a better approximation to the continuous copula, however more computation time will be required. Similarly, the approximation will become more precise, if we run the $D_{1} A D_{2}$ algorithm with more iterations, and therefore, this would cost us more computation time. It can be concluded that the number of iterations will depend on the grid size. We consider the approximation errors in the range $1 \times 10^{-1}$ to $1 \times 10^{-24}$. Thus, the larger the number of grid points used, the larger the number of iterations required for convergence; which is true at all error levels. For all grid sizes, a higher of number of iterations are required initially for improving the accuracy of computation; once the error is reduced, the number of iterations can be decreased. In this example, we choose a grid size of $200 \times 200$ throughout.

Based on the information given above regarding the grid size, number of iterations and error size, we can derive the entropy copula $C_{15}$ associated with the chosen constraints. Expectations $\alpha$ of the selected basis, Lagrange multiplies values (parameter values) $\lambda$ and Log-Likelihood are summarized in Table 3. Log-Likelihood (L) for PS, OPS, and OFS basis are 93.49, 98.59, and 38.76 , respectively. The corresponding copulas in terms of the OP, OPS and OFS bases are plotted in Panels (a), (b), and (c) in Figure 3 respectively.


Table 1: The minimally informative copula given moment constraints for OP, OPS, and OFS bases between 1 and 5

![img-2.jpeg](img-2.jpeg)

Figure 3: The minimally informative copula given moment constraints between variable 1 and 5; Panel (a): PS basis, Panel (b): OPS basis, and Panel (c): OFS basis

Consider the minimum information copula computation in PCC-DAG structure such that instead of choosing the grid equidistant (or uniform grid), we could choose points where more points are included in the tail of the distribution. This could result in outperforming of Gaussian models by non-Gaussian models approximated based on the method described in this paper. However, we have used Chebyshev points for copula approximation in our grid using minimum information method instead of uniform grid, since they allow for more points in the tail or boundaries of our approximation. This is very important especially in financial applications. Chebyshev points are roots of Chebyshev Polynomial; the discussion and some details are presented in [36]. In order to compare uniform grid and Chebyshev, we consider the above discussion with respect to the uniform grid size deriving the minimum information copula $C_{15}$ which is associated with the previous chosen constraints. Figure (4) illustrates the entropy copula $C_{15}$ Chebyshev grid which allow for more points in the tail.

![img-3.jpeg](img-3.jpeg)

Figure 4: Entropy copula $C_{15}$ using Chebyshev grid.

One of the main advantages of using OPS and OFS bases over the ordinary polynomial series (considered in Bedford et al., 2015) is that the $D_{1} A D_{2}$ algorithm converges much faster using these bases. This is because of the following nice property of these two bases that adding a new basis to the kernel defined in (3) and used to construct the entropy copula, does not change the Lagrange multipliers of the already used in the kernel. But, this is not the case when one is applying the PS bases (as proposed in [8]) to calculate the entropy copula. In this situation, we need to run the $D_{1} A D_{2}$ algorithm each time a new basis is added to the already chosen bases, and the parameter values are changing accordingly. Therefore, more iterations are required for the $D_{1} A D_{2}$ algorithm to converge. The optimisation time required for the $D_{1} A D_{2}$ algorithm using the OPS bases is 9.83 seconds and for the OFS bases is 8.89 , while this time for the PS bases is 29.87 seconds which is almost twofold of the former one and almost two and half times more than the latter one.

The other unconditional copula in the decomposition (7) i.e. $C_{46}, C_{34}$, and $C_{45}$ could be calculated in the similar way. Using the step-wise method, we select the four PS, OPS and OFS bases that along with their corresponding constraints, resulting Lagrange multipliers, and Log-Likelihood (L) are given in Table 2. The approximated maximum entropy copula for these unconditional copula in terms of the PS, OPS and OFS bases is shown in Panels of Figure 5.

Now, the conditional copulas $C_{13 \mid 5}, C_{23 \mid 4}$ and $C_{35 \mid 4}$ can similarly be approximated using the entropy approach. We only illustrate construction of the conditional maximum entropy copula between $C_{13 \mid 5} . C_{23 \mid 4}$ and $C_{35 \mid 4}$ can be similarly approximated in a similar way. In order to calculate this copula, we divide the support of 5 into some arbitrary sub- intervals or bins and then construct

![img-4.jpeg](img-4.jpeg)

Figure 5: The minimally informative copula given moment constraints, Panel (a): $C_{46}$ for PS basis, Panel (b): $C_{46}$ for OPS basis, Panel (c): $C_{46}$ for OFS basis, Panel (d): $C_{34}$ for PS basis, Panel (e): $C_{34}$ for OPS basis, Panel (f): $C_{34}$ for OFS basis, Panel (g): $C_{45}$ for PS basis, Panel (h): $C_{45}$ for OPS basis, and Panel (i): $C_{45}$ for OFS basis.


Table 2: The minimally informative copula given moment constraints for $C_{46}, C_{34}$, and $C_{45}$
the conditional copula within each bin. To do so, we select bases in the same way as for the unconditional copulas and fit the copula to the calculated mean values or constraints. In this case, we use four bins so that the first copula is for $13 \mid 5 \in(0,0.25)$. The other bins are $13 \mid 5 \in$ $(0.25,0.5), 13 \mid 5 \in(0.5,0.75)$, and $13 \mid 5 \in(0.75,1)$. We can follow this process again for the remaining bins. Table 3 shows the mean values or constraints (denoted by $\alpha_{i}$ ) and corresponding Lagrange multipliers $\left(\lambda_{i}\right)$ required to build the conditional entropy copula between $1 \mid 5$ and $3 \mid 5$ for PS, OPS and OFS bases, respectively. The log-likelihood of the approximated copula in each bin is also reported in these tables. The Log-Likelihood over all bins for $C_{23 \mid 4}$ and $C_{35 \mid 4}$ for (PS, OPS, OFS) basis are $(16.13,39.1,38.63)$ and $(223.69,345.15,246.99)$, respectively.

We can obtain the conditional maximum entropy copula, $C_{12 \mid 35}$, similarly by dividing each of the conditioning variables' supports into four bins. Then the entropy copulas for $1 \mid 35$ and $2 \mid 35$ are calculated on each combination of bins for 3 and 5 which makes 16 bins altogether for it. The bins, bases and log-likelihoods associated with each copula based on the PS, OPS and OFS basis are given in Table 4.

The log-likelihood of the overall non-Gaussian PCC-DAG model using the PS, OPS and OFS bases are $2390.44,2669.69$ and 2093.75 , respectively. The use of log-likelihood as a goodness-of-fit criterion is not inconsistent with minimum information modeling. Jaynes [26] uses the parameter


Table 3: Minimaly informative copula given moment constraints between 1 and 3 given 5
maximum likelihood estimates associated with the form of the minimum information distribution to justify the connection in the constraint rule of expectations and frequencies. The use of loglikelihood is also recommended as a plausible model selection tool within minimum information framework [8].

However, the best model should be typically selected by trading-off between the goodness of fit of the candidate models and their model complexity. When there are several competing copulas, and one wishes to know which copula fits the data best. The selected copula model should be the one that minimizes the Kullback-Leibler information between the copula model and the true unknown copula. The Akaike information criteria (AIC) can be thus considered as a plausible tool, which also minimizes the information between the candidate models, to select the best model from the parametric families and non-parametric candidate models [20]. In this regard, the AIC is first computed for each model with the same data, then the "best" model is the one with the least AIC value. It is claimed that AIC is also more computationally efficient than other copula selection methods [20]. Since, the comparison of the log-likelihood of the proposed non-parametric model and the parametric model $[3,4]$ is not conclusive, as the model complexity measured by the number of parameters is not considered. As suggested above, we compare these models based on the AIC


Table 4: entropy copula for given moment constraints between 1 and 2 given 3 and 5


Table 5: Comparison between different models.
which includes the model complexity for the parametric method. The AIC of the overall NonGaussian PCC-DAG model using the PS, OPS and OFS bases are -4780.88, -5339.38 and -4187.24 , respectively. These values are considerably less than the AIC of the parametric non-Gaussian PCCDAG models using Bauer et al. (2012) method, (as the AIC equals to -3078.62). We illustrate the corresponding results in Table 5.

The size of observed data could be considered as a source of potential error when the minimum information vine model is applied for modeling a high-dimensional problem. As the dimensionality (or number of uncertain variables) increases, the number of trees representing the structure of pair-copula model will also increase (see also [12]). The conditional distributions/expectations at lower levels of a deeper vine model must then be estimated based on fewer data points which can be then less accurate and noisier (see also [16] for further details with an application in modelling flood events with the limited data). This problem could be resolved by ignoring some unnecessary conditional dependencies (the so-called simplifying assumption) in the sense discussed in[2, 43]. An alternative method is to approximate fully conditional pair-copula models using Gaussian processes [35]. This model shows promising results with better predictive performance than the method that ignores conditional dependencies. This simplifying pair-copula model is more appropriate for high-dimensional problems.

In this paper, the conditional independence statements play a crucial role in simplifying the model structure [22]. Thus, the computation of the conditional probabilities in practice could not

be complex unless the parent set is considerably large. In the case that the parent set of a variable of interest is very large, the corresponding conditional probability could be estimated using the Gaussian process emulators as suggested in [35].

# 6. Simulation study 

We can now discuss the data simulations derived from the presented minimum information PCC-DAG in order to provide comparisons between correlations in the simulated data and in the observed data. This is based on 2000 simulations. We follow the simulation method proposed by [30] subjected to sampling from the cumulative distributions. This simulation method has been followed by Daneshkhah et al. [15] references cited therein. Moreover, this simulation has been updated using provided simulation method from PCC-DAG in parametric status in [4, 3]. Their sampling strategy is as follows: sample two independent variables distributed uniformly on intervals $[0,1]$, denoted by $U_{1}, U_{2}$, and calculate values of the original variables using the following equations:

$$
x_{1}=u_{1}, \quad x_{2}=F_{2 \mid 1}^{-1}\left(u_{2} \mid x_{1}\right)
$$

where $x_{i}$ is realization values of $X_{i}$, and $u_{i}$ is realization values of $U_{i}$. Finally, this has been applied to all variables in PCC-DAG. Please note that the order of variables for childs and parents in this simulation is important.

It can be observed that the simulated data and the original data have similar dependency patterns. Table 6 shows the rank correlations between the variables of interest calculated from the original observed data, that are based on the simulated data taken from the fitted PCC-DAG through entropy copula on OPS basis. Other bases can be similarly simulated, however they are not reported and considered here. By comparing these correlations, we can conclude that the results show strong consistency and the estimated correlations based on the entropy PCC-DAG are closer to the ones that are originated from the observed data. Furthermore, we can compare entropy PCC-DAG and parametric PCC-DAG which estimated correlations based on the entropy PCCDAG using OPS basis are closer to the ones that are derived from the observed data rather than the parametric PCC-DAG.

Table 6: Correlation coefficients of the original data and the simulated data


Parametric PCC-DAG


Entropy PCC-DAG


# 7. Discussion and Conclusions 

Gaussian distributions are generally used for modelling and computing financial asset returns, risk assessment of capital allocation by banks, and estimating risks associated with financial portfolios in actuarial science. However, the existing internal Gaussian models are limited when it comes to inference from tails. As opposed to normal Gaussian distributions, copulae are known to be a suitable and powerful means for overcoming the flaws in the existing techniques. An example for the application of copulae in the above-mentioned areas, would be the claim allocations and fees' assignments for investigators, experts, etc. as part of allocated loss adjustment expense processes. An additional case for the application of copulae, would be risk assessments conducted by banks and credit institutions for credit and market evaluations and judgements; an existing flaw with many of the existing techniques, known to be internal bottom-up approaches, for such risks assessments, as such techniques are incapable of modelling joint distribution of non-identical risks.

There are non-identical approaches to inference in multivariate distributions. Bayesian networks and copulae are generally very suitable for modelling such probability distributions. In the applications where tail properties are important for predictive probabilistic modelling, many of the existing techniques are limited and inadequate. One of the well-known techniques that can conveniently infer from tail properties is the multivariate Gaussian copula. As stated above, many of the current techniques used for financial application modelling, assume a normal Gaussian distribution of events for simplifying the complex nature of the financial scenarios (as discussed in $[8,13]$ ). The proposed methodology for utilising vine structure for approximation, would enable the modeller to simply establish non-constant conditional correlations, and minimise the chance of risk underestimation.

In this paper, we extended the novel method originally presented by $[3,4]$ to approximate a multivariate distribution by any Non-Gaussian PCC-DAG structure. The main idea to implement this approximation method is to use the entropy copulae that can be determined to any required degree of precision, based on the available data. The approximation method used in this paper is flexible and easy to implement. The standing technical assumptions we require is that the multivariate density of DAG under study is continuous and is non-zero. In order to approximate a multivariate distribution for the observed data, one only needs to specify a DAG structure, a basis family, and the expected values for the certain functions associated with some constraints on each pairwise copula. Our focus in this paper was to introduce pair-copula structure that can

be approximated by any given non-Gaussian DAG to any required degree of approximation with different bases family. We concentrated on the PS, OPS and OFS bases. The OPS and OFS bases exhibit an appropriate property, which makes the distribution approximation faster in the sense that adding a new element to their expansion does not change coefficient of the already found shorter expansion, where any new item has in general non-zero projection on previous items.

Any functions can be used to create the minimum information copulas used here, and in some applications it may be natural to use functions that are themselves computed in computer codes. Because of the frequent evaluation calls needed to determine the minimum information model, it then makes sense to use emulators (particularly, Gaussian process as proposed in [43]) or Kriging models as a way to speed up the computations.

As a future work, we wish to extend the methodologies presented in [39] to estimate the nonGaussian DAG model and compare it with the proposed method in this paper. It would be compelling to investigate how the model can be simplified further using the approaches presented in [39] and considering the conditional independence statements. Furthermore, it would be desired to extend the modified AIC given in Nagler et al. [39] to a more comprehensive model selection tool so that the non-parametric model presented in this paper could be compared with other nonparametric/parametric model candidates.

# ACKNOWLEDGMENTS 

This research was supported by funding from the UK Engineering \& Physical Sciences Research Council (Strategic Package: Centre for Predictive Modelling in Science and Engineering - Grant No. EP/L027682/1).
