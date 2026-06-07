# The YODO algorithm: An efficient computational framework for sensitivity analysis in Bayesian networks 

Rafael Ballester-Ripoll<br>RAFAEL.BALLESTER@IE.EDU<br>Manuele Leonelli<br>MANUELE.LEONELLI@IE.EDU<br>School of Science and Technology, IE University, Madrid, Spain


#### Abstract

Sensitivity analysis measures the influence of a Bayesian network's parameters on a quantity of interest defined by the network, such as the probability of a variable taking a specific value. Various sensitivity measures have been defined to quantify such influence, most commonly some function of the quantity of interest's partial derivative with respect to the network's conditional probabilities. However, computing these measures in large networks with thousands of parameters can become computationally very expensive. We propose an algorithm combining automatic differentiation and exact inference to efficiently calculate the sensitivity measures in a single pass. It first marginalizes the whole network once, using e.g. variable elimination, and then backpropagates this operation to obtain the gradient with respect to all input parameters. Our method can be used for one-way and multi-way sensitivity analysis and the derivation of admissible regions. Simulation studies highlight the efficiency of our algorithm by scaling it to massive networks with up to 100'000 parameters and investigate the feasibility of generic multi-way analyses. Our routines are also showcased over two medium-sized Bayesian networks: the first modeling the country-risks of a humanitarian crisis, the second studying the relationship between the use of technology and the psychological effects of forced social isolation during the COVID-19 pandemic. An implementation of the methods using the popular machine learning library PyTorch is freely available.


Keywords: Automatic differentiation; Bayesian networks; COVID-19; PyTorch; Sensitivity analysis.

## 1. Introduction

Probabilistic graphical models, and specifically Bayesian networks (BNs), are a class of models that are widely used for risk assessment of complex operational systems in a variety of domains. The main reason for their success is that they provide an efficient and intuitive framework to represent the joint probability of a vector of variables of interest using a simple graph. Their use to assess the reliability of engineering, medical and ecological systems, among many others, is becoming increasingly popular. Sensitivity analysis is a critical step for any applied real-world analysis to assess the importance of various risk factors and to evaluate the overall safety of the system under study (see e.g. Goerlandt and Islam, 2021; Makaba et al., 2021; Zio et al., 2022, for some recent examples).

As noticed by Rohmer (2020), sensitivity analysis in BNs is usually local, in the sense that it measures the effect of a small number of parameter variations on output probabilities of interest, while other parameters are kept fixed. In the case of a single parameter variation, sensitivity analysis is usually referred to as one-way; otherwise, when more than one parameter is varied, it is called multi-way. Although recently there has been an increasing interest in proposing global sensitivity methods for BNs measuring how different factors jointly influence some function of the model's output (see e.g. Ballester-Ripoll and Leonelli, 2022a; Li and Mahadevan, 2018), the focus of this paper still lies in local sensitivity methods.

Local sensitivity analysis in BNs can be broken down into two main steps. First, some parameters of the model are varied, and the effect of these variations on output probabilities of interest is investigated. For this purpose, a simple mathematical function, usually termed sensitivity function, describes an output probability of interest as a function of the BN parameters (Castillo et al., 1997; Coupé and van der Gaag, 2002). Furthermore, some specific properties of such a function can be computed, for instance, the sensitivity value or the vertex proximity, which give an overview of how sensitive the probability of interest is to variations of the associated parameter (van der Gaag et al., 2007). Second, once parameter variations are identified, their effect is summarized by a distance or divergence measure between the original and the varied distributions underlying the BN, most commonly the Chan-Darwiche distance (Chan and Darwiche, 2005) or the well-known Kullback-Leibler divergence.

As demonstrated by Kwisthout and van der Gaag (2008), the derivation of both the sensitivity function and its associated properties is computationally very demanding. In Ballester-Ripoll and Leonelli (2022b), we introduced a novel, computationally highlyefficient method to compute all sensitivity measures of interest in one-way sensitivity analysis, which takes advantage of backpropagation and is easy to compute thanks to automatic differentiation. We now also demonstrate how the algorithm can be utilized for more generic multi-way sensitivity analyses and for deriving admissible regions (van der Gaag and Renooij, 2001). Simulation studies show the efficiency of the approach by processing massive networks in a few seconds and demonstrate when multi-way analyses are computationally feasible. Two practical applications from real-world datasets further showcase the insights sensitivity measures can provide and the efficiency of the implemented routines.

We have open-sourced a Python implementation using the popular machine learning library PyTorch ${ }^{1}$, contributing to the recent effort of promoting sensitivity analysis (Douglas-Smith et al., 2020).

[^0]
[^0]:    1. Available at https://github.com/rballester/yodo.

# 2. Bayesian networks and sensitivity analysis 

A BN is a probabilistic graphical model defining a factorization of the probability mass function (pmf) of a random vector using a directed acyclic graph (DAG) (Darwiche, 2009b; Pearl, 1988). More formally, let $[p]=\{1, \ldots, p\}$ and $\boldsymbol{Y}=\left(Y_{i}\right)_{i \in[p]}$ be a random vector of interest with sample space $\mathbb{Y}=\times_{i \in[p]} \mathbb{Y}_{i}$. A BN defines the pmf $P(\boldsymbol{Y}=\boldsymbol{y})$, for $\boldsymbol{y} \in \mathbb{Y}$, as a product of simpler conditional pmfs as follows:

$$
P(\boldsymbol{Y}=\boldsymbol{y})=\prod_{i \in[p]} P\left(Y_{i}=y_{i} \mid \boldsymbol{Y}_{\Pi_{i}}=\boldsymbol{y}_{\Pi_{i}}\right)
$$

where $\boldsymbol{Y}_{\Pi_{i}}$ are the parents of $Y_{i}$ in the DAG associated to the BN.
The definition of the pmf over $\boldsymbol{Y}$, which would require defining $\# \mathbb{Y}-1$ probabilities, is thus simplified in terms of one-dimensional conditional pmfs. The coefficients of these functions are henceforth referred to as the parameters $\boldsymbol{\theta}$ of the model. The DAG structure may be either expert-elicited or learned from data using structural learning algorithms, and the associated parameters $\boldsymbol{\theta}$ can be either expert-elicited or learned using frequentist or Bayesian approaches. No matter the method used, we assume that a value for these parameters $\boldsymbol{\theta}$ has been chosen, which we refer to as the original value and denote it as $\boldsymbol{\theta}^{0}$.

The DAG associated with a BN provides an intuitive overview of the relationships between variables of interest. However, it does also provide a framework to assess if any generic conditional independence holds for a specific subset of the variables via the socalled d-separation criterion (see e.g. Pearl, 1988). Furthermore, the DAG provides a framework for the efficient propagation of probabilities and evidence via algorithms that take advantage of the structure of the underlying DAG.

### 2.1 One-way sensitivity analysis

In practical applications, it is fundamental to extensively assess the implications of the chosen parameter values $\boldsymbol{\theta}^{0}$ to outputs of the model. In the context of BNs, this study is usually referred to as sensitivity analysis, which can be further used during the modelbuilding process as showcased by Coupé et al. (2000). Let $Y_{O}$ be an output variable of interest and $\boldsymbol{Y}_{E}$ be evidential variables, those that may be observed. The interest is in then studying how $P\left(Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$ varies when a parameter $\theta_{i}$ is varied. In particular, $P\left(Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$ seen as a function of $\theta_{i}$ is called sensitivity function and denoted as $f\left(\theta_{i}\right)$.

### 2.2 Proportional covariation

Notice that when an input $\theta_{i}$ is varied from its original value $\theta_{i}^{0}$, the parameters from the same conditional pmf need to covary to respect the sum-to-one condition of probabilities. When variables are binary, this is automatic since one parameter must be equal to one minus the other. However, for variables taking more than two levels, this covariation can

be done in several ways (Renooij, 2014). We henceforth assume that whenever a parameter is varied from its original value $\theta_{i}^{0}$ to a new value $\theta_{i}$, then every parameter $\theta_{j}$ from the same conditional pmf is proportionally covaried (Laskey, 1995) from its original value $\theta_{j}^{0}$ :

$$
\theta_{j}\left(\theta_{i}\right)=\frac{1-\theta_{i}}{1-\theta_{i}^{0}} \theta_{j}^{0}
$$

Proportional covariation has been studied extensively, and its choice is motivated by a wide array of theoretical properties (Chan and Darwiche, 2005; Leonelli et al., 2017; Leonelli and Riccomagno, 2022; Renooij, 2014).

Under the assumption of proportional covariation, Castillo et al. (1997) and Coupé and van der Gaag (2002) demonstrated that the sensitivity function is the ratio of two linear functions:

$$
f\left(\theta_{i}\right)=\frac{c_{0}+c_{i} \theta_{i}}{d_{0}+d_{i} \theta_{i}}
$$

where $c_{0}, c_{i}, d_{0}, d_{i} \in \mathbb{R}_{+}$. van der Gaag et al. (2007) noticed that the above expression coincides with the fragment of a rectangular hyperbola, which can be generally written as

$$
f\left(\theta_{i}\right)=\frac{r}{\theta_{i}-s}+t
$$

where

$$
s=-\frac{d_{0}}{d_{i}}, \quad t=\frac{c_{i}}{d_{i}}, \quad r=\frac{c_{0}}{d_{i}}+s t
$$

# 2.2.1 SENSITIVITY VALUES 

The sensitivity value describes the effect of infinitesimally small shifts in the parameter's original value on the probability of interest and is defined as the absolute value of the first derivative of the sensitivity function at the original value of the parameter, i.e. $\left|f^{\prime}\left(\theta_{i}^{0}\right)\right|$. This can be found by simply differentiating the sensitivity function as

$$
\left|f^{\prime}\left(\theta_{i}^{0}\right)\right|=\frac{\left|c_{i} d_{0}-c_{0} d_{i}\right|}{\left(d_{i} \theta_{i}^{0}+d_{0}\right)^{2}}
$$

The higher the sensitivity value, the more sensitive the output probability to small changes in the parameter's original value. As a rule of thumb, parameters having a sensitivity value larger than one may require further investigation.

Notice that when $\boldsymbol{Y}_{E}$ is empty, i.e. the output probability of interest is marginal, the sensitivity function is linear in $\theta_{i}$. The sensitivity value is the same regardless of the original $\theta_{i}^{0}$. Therefore, in this case, the absolute value of the gradient is sufficient to quantify the effect of a parameter on an output probability of interest.

# 2.2.2 VERTEX PROXIMITY 

van der Gaag et al. (2007) further noticed that parameters for which the sensitivity value is small may still be such that the conditional output probability of interest is very sensitive to their variations. This happens when the original parameter value is close to the vertex of the sensitivity function, defined as the point $\theta_{i}^{v}$ at which the sensitivity value is equal to one, i.e.

$$
\left|f^{\prime}\left(\theta_{i}^{v}\right)\right|=1
$$

The vertex can be derived from the equation of the sensitivity function as

$$
\theta_{i}^{v}= \begin{cases}s+\sqrt{|r|}, & \text { if } s<0 \\ s-\sqrt{|r|}, & \text { if } s>0\end{cases}
$$

Notice that the case $s=0$ is not contemplated since it would coincide with a linear sensitivity function, not a hyperbolic one.

Vertex proximity is defined as the absolute difference $\left|\theta_{i}^{0}-\theta_{i}^{v}\right|$. The smaller the vertex proximity, the more sensitive the output probabilities may be to parameter variations, even when the sensitivity value is small.

### 2.2.3 Other metrics

Given the coefficients $c_{0}, c_{i}, d_{0}, d_{i}$ of Equation (3), it is straightforward to derive any property of the sensitivity function besides the sensitivity value and the vertex proximity. Here we propose the use of two additional metrics. The first is the absolute value of the second derivative of the sensitivity function at the original parameter value, which can be easily computed as:

$$
\left|f^{\prime \prime}\left(\theta_{i}^{0}\right)\right|=\frac{2 d_{i}\left|c_{i} d_{0}-c_{0} d_{i}\right|}{\left(d_{i} \theta_{i}^{0}+d_{0}\right)^{3}}
$$

Similarly to the sensitivity value, high values of the second derivative at $\theta_{i}^{0}$ indicate parameters that could highly impact the probability of interest.

The second measure is the maximum of the first derivative of the sensitivity function over the interval $[0,1]$ in absolute value, which we find easily by noting that the denominator of Equation (6) is a parabola:

$$
\max _{\theta_{i} \in[0,1]}\left|f^{\prime}\left(\theta_{i}\right)\right|= \begin{cases}\infty & \text { if }-d_{0} / d_{i} \in[0,1] \\ \max \left\{\left|c_{i} d_{0}-c_{0} d_{i}\right| / d_{0}^{2},\left|c_{i} d_{0}-c_{0} d_{i}\right| /\left(d_{i}+d_{0}\right)^{2}\right\} & \text { otherwise }\end{cases}
$$

Again high values indicate parameters whose variations can lead to a significant change in the output probability of interest.

# 2.3 Multi-way sensitivity analysis 

In many practical applications, there is interest in assessing the effect of simultaneous variations of multiple parameters on the output of interest. This is called a multi-way sensitivity analysis. Although there have been some attempts to study the theoretical properties and computational efficiency of these more generic analyses (see e.g. Bolt and Renooij, 2014; Chan and Darwiche, 2004; Kjaerulff and van der Gaag, 2000; Leonelli et al., 2017; Leonelli and Riccomagno, 2022), in practice, they are not as common as one-way analyses.

### 2.3.1 GENERAL FORMULATION

Suppose now that $n$ parameters $\boldsymbol{\theta}_{n}=\left(\theta_{1}, \ldots, \theta_{n}\right)$ are simultaneously varied. By default, these parameters are taken from different conditional pmfs so that they are independent of each other (van der Gaag et al., 2007). In the binary case, this is natural since only one parameter per pmf can be varied since the other is functionally related. The other parameters from conditional pmfs including $\theta_{1}, \ldots, \theta_{n}$, are proportionally covaried, as for the one-way analysis (see Leonelli and Riccomagno, 2022, for a formal discussion). The effect of varying the parameters $\boldsymbol{\theta}_{n}$ on a probability of interest $P\left(Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$ is captured by the n-way sensitivity function, which is equal to

$$
f\left(\boldsymbol{\theta}_{n}\right)=\frac{\sum_{K \in \mathcal{P}([n])} c_{K} \prod_{i \in K} \theta_{i}}{\sum_{K \in \mathcal{P}([n])} d_{K} \prod_{i \in K} \theta_{i}}
$$

where $\mathcal{P}$ denotes the power set and $c_{K}, d_{K} \in \mathbb{R}, K \in \mathcal{P}([n])$, are constants computed from the non-varied parameters. For instance, a 2-way sensitivity function can be written as:

$$
f\left(\theta_{1}, \theta_{2}\right)=\frac{c_{0}+c_{1} \theta_{1}+c_{2} \theta_{2}+c_{12} \theta_{1} \theta_{2}}{d_{0}+d_{1} \theta_{1}+d_{2} \theta_{2}+d_{12} \theta_{1} \theta_{2}}
$$

An n-way sensitivity function, in general, requires the computation of $2^{n+1}$ constants and is thus computationally expensive. Furthermore, the number of combinations of parameters for which the sensitivity function has to be constructed increases: see Section 3.2 for a discussion.

### 2.3.2 MAXIMUM N-WAY SENSITIVITY VALUES

While for one-way sensitivity analysis, one can uniquely talk about the derivative of the sensitivity function, for multi-valued functions, there are multiple directions at which the derivative could be computed, as noted by (Bolt and Renooij, 2014), and hence the notion of directional derivative. However, basic calculus tells us that the maximum directional derivative of a function $f$ at a point $\boldsymbol{\theta}_{n}$ equals the length of the gradient vector at $\boldsymbol{\theta}_{n}$, i.e. $\left|\Delta f\left(\boldsymbol{\theta}_{n}\right)\right|$. This observation led to the definition of the sensitivity value for an n-way sensitivity function as the maximum one out of all possible directional derivatives (Bolt

and Renooij, 2014). For a vector of parameters $\boldsymbol{\theta}_{n}$ with original values $\boldsymbol{\theta}_{n}^{0}$ the maximum n-way sensitivity value is defined as

$$
s v_{\max }^{\boldsymbol{\theta}_{n}}=\left|\Delta f\left(\boldsymbol{\theta}_{n}^{0}\right)\right|
$$

where $f$ is the associated n-way sensitivity function.
By definition, the maximum n-way sensitivity value would first require the derivation of the n-way sensitivity function and, subsequently, the computation of its gradient. As noticed already, this direct approach would be computationally too expensive. However, Bolt and Renooij (2014) demonstrated that $s v_{\max }^{\boldsymbol{\theta}_{n}}$ could be easily computed from the sensitivity values of one-way sensitivity functions. Let $c_{0}^{i}, c_{i}, d_{0}^{i}, d_{i}$ be the coefficients of the one-way sensitivity function for the variation of the parameter $\theta_{i}$ in $\boldsymbol{\theta}_{n}$. Then:

$$
s v_{\max }^{\theta_{n}}=\frac{1}{P\left(\boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)^{2}} \sqrt{\sum_{i \in[n]}\left(c_{i} d_{0}^{i}-c_{0}^{i} d_{i}\right)^{2}}
$$

Therefore if an efficient method for computing the coefficients of one-way sensitivity functions exists, then maximum n-way sensitivity values can be equally efficiently derived.

# 2.4 Admissible regions 

In many applied situations, the object of interest is not a probability per se, but rather the most likely value of a variable, possibly conditional on a specific subset of evidence. This is the case for classification problems where a Bayes classifier is used: an unlabeled observation exhibiting a specific evidence pattern is classified according to the most likely value. BNs designed explicitly for this task are usually called Bayesian network classifiers (Bielza and Larranaga, 2014; Friedman et al., 1997).

Although sensitivity methods for this type of classification problem have been discussed (Bolt and van der Gaag, 2017), sensitivity values and related measures are often not particularly useful. van der Gaag and Renooij (2001) demonstrated that parameters with a small sensitivity value might induce a change in the classification rule, or equally in the most likely value, for just a slight deviation from its original value. For this reason, they introduced the concept of admissible region, which captures the extent to which a parameter can be varied without inducing a change in the most likely value for the variable of interest.

For ease of notation, we consider here a variable of interest $Y_{O}$ taking two possible levels $y_{O}$ and $y_{O}^{\prime}$ (thus, we consider the most common binary classification problem). Consider also possible evidence $\boldsymbol{Y}_{E}=\boldsymbol{y}_{E}$, a perturbed parameter $\theta_{i}$ and suppose that $P\left(Y_{O}=\right.$ $\left.y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)>P\left(Y_{O}=y_{O}^{\prime} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$, without loss of generality. The admissible region $R_{i}$ is formally defined as the interval of values for $\theta_{i}$

$$
\left(\max \left\{\theta_{i}^{0}-r, 0\right\}, \min \left\{\theta_{i}^{0}+s, 1\right\}\right), \quad r, s, \in \mathbb{R}
$$

for which $P\left(Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)>P\left(Y_{O}=y_{O}^{\prime} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$. The wider the interval $R_{i}$, the less influential the parameter is for the most likely value.
van der Gaag and Renooij (2001) and van der Gaag et al. (2007) already demonstrated that such regions could be computed from the one-way sensitivity functions by identifying the points at which the sensitivity functions intersect. However, they did not explicitly write the admissible regions as a function of the sensitivity functions' coefficients to our knowledge. Let $c_{0}, c_{i}, d_{0}, d_{i}$ be the coefficients of the sensitivity function for the event $Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}$. It follows that the sensitivity function for $Y_{O}=y_{O}^{\prime} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}$ must be equal to

$$
\frac{\left(d_{0}-c_{0}\right)+\left(d_{i}-c_{i}\right) \theta_{i}}{d_{0}+d_{i} \theta_{i}}
$$

By equating the two sensitivity functions, we find that

$$
R_{i}= \begin{cases}\left(0, \min \left\{\frac{d_{0}-2 c_{0}}{2 c_{i}-d_{i}}, 1\right\}\right) & \text { if } \theta_{i}^{0} \leq \frac{d_{0}-2 c_{0}}{2 c_{i}-d_{i}} \\ \left(\max \left\{0, \frac{d_{0}-2 c_{0}}{2 c_{i}-d_{i}}\right\}, 1\right) & \text { otherwise }\end{cases}
$$

In the case of $E=\emptyset$, i.e. no evidence, the expression for the admissible regions simplifies to:

$$
R_{i}= \begin{cases}\left(0, \min \left\{\frac{1-2 c_{0}}{2 c_{i}}, 1\right\}\right) & \text { if } \theta_{i}^{0} \leq \frac{1-2 c_{0}}{2 c_{i}} \\ \left(\max \left\{0, \frac{1-2 c_{0}}{2 c_{i}}\right\}, 1\right) & \text { otherwise }\end{cases}
$$

Therefore, given an efficient method to compute one-way sensitivity functions, admissible regions for all individual parameters can be equally efficiently derived.

# 3. The YODO method 

The YODO (You Only Derive Once) method was first introduced in Ballester-Ripoll and Leonelli (2022b) to compute the one-way sensitivity measures discussed in Sections 2.2.12.2.3. We first review it and then discuss its use in multi-way sensitivity analysis.

### 3.1 YODO for one-way sensitivity analysis

### 3.1.1 First case: Marginal probability as a function of interest

Suppose $f\left(\theta_{i}\right)=P\left(Y_{O}=y_{O}\right)=c_{0}+c_{i} \theta_{i}$ assuming proportional covariation as $\theta_{i}$ varies. Let $\theta_{j_{1}}, \ldots, \theta_{j_{n}}$ be the other parameters of the same conditional pmf as $\theta_{i}$, i.e. they are all bound by the sum-to-one constraint $\theta_{i}+\theta_{j_{1}}+\cdots+\theta_{j_{n}}=1$. First, we rewrite $f$ as

$$
f\left(\theta_{i}\right)=g\left(\theta_{i}, \theta_{j_{1}}\left(\theta_{i}\right), \ldots, \theta_{j_{n}}\left(\theta_{i}\right)\right)
$$

and we show how to obtain $f^{\prime}\left(\theta_{i}\right)$ provided that we can compute the gradient $\nabla g$ with respect to symbols $\theta_{i}, \theta_{j_{1}}, \ldots, \theta_{j_{n}}$ (see Section 3.1.3 for details on the latter).

By the generalized chain rule, it holds that

$$
f^{\prime}\left(\theta_{i}\right)=\frac{\partial g}{\partial \theta_{i}} \cdot 1+\frac{\partial g}{\partial \theta_{j_{1}}} \cdot \frac{d \theta_{j_{1}}}{d \theta_{i}}+\cdots+\frac{\partial g}{\partial \theta_{j_{n}}} \cdot \frac{d \theta_{j_{n}}}{d \theta_{i}}
$$

By deriving Equation (2), we have that for all $1 \leq m \leq n$ :

$$
\frac{d \theta_{j_{m}}}{d \theta_{i}}=\frac{-\theta_{j_{m}}^{0}}{1-\theta_{i}^{0}}
$$

and, therefore,

$$
f^{\prime}\left(\theta_{i}\right)=\frac{\partial g}{\partial \theta_{i}}-\frac{\left(\partial g / \partial \theta_{j_{1}}\right) \cdot \theta_{j_{1}}^{0}+\cdots+\left(\partial g / \partial \theta_{j_{n}}\right) \cdot \theta_{j_{n}}^{0}}{1-\theta_{i}^{0}}
$$

Last, since $f\left(\theta_{i}\right)=P\left(\boldsymbol{Y}_{O}=\boldsymbol{y}_{O}\right)=c_{0}+c_{i} \theta_{i}$, we easily find the parameters $c_{0}, c_{i}$ :

$$
\left\{\begin{array}{l}
c_{i}=f^{\prime}\left(\theta_{i}^{0}\right) \\
c_{0}=P\left(\boldsymbol{Y}_{O}=\boldsymbol{y}_{O}\right)-c_{i} \theta_{i}^{0}
\end{array}\right.
$$

# 3.1.2 SECOND CASE: CONDITIONAL PROBABILITY AS A FUNCTION OF INTEREST 

When $f\left(\theta_{i}\right)=P\left(Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)=P\left(Y_{O}=y_{O}, \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right) / P\left(\boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$, we simply repeat the procedure from Sec. 3.1.1 twice:

1. We first apply it to $P\left(Y_{O}=y_{O}, \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$ to obtain $c_{0}$ and $c_{i}$;
2. we then apply it to $P\left(\boldsymbol{Y}_{E}=\boldsymbol{y}_{E}\right)$ to obtain $d_{0}$ and $d_{i}$.

### 3.1.3 COMPUTING THE GRADIENT $\nabla g$

Let $\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}$ be a subset of the network variables taking some evidence values (this could be $K=O$ or $K=O \cup E$; hence we cover the two cases above).

We start by moralizing the BN into a Markov random field (MRF) $\mathcal{M}$. This marries all variable parents together and, for each conditional probability table (now called potential), drops the sum-to-one constraint; see e.g. (Darwiche, 2009a) for more details. Next, we impose the evidence $\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}$ by defining $\mathcal{M}^{\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}}$ as a new MRF that results from substituting each potential $\Phi_{i_{1}, \ldots, i_{M}}\left(x_{i_{1}}, \ldots, x_{i_{M}}\right)$ by a new potential $\widehat{\Phi}_{i_{1}, \ldots, i_{M}}$ defined as follows:

$$
\begin{gathered}
\widehat{\Phi}_{i_{1}, \ldots, i_{M}}\left(Y_{i_{1}}=x_{i_{1}}, \ldots, Y_{i_{M}}=x_{i_{M}}\right)= \\
\left\{\begin{array}{ll}
0 & \text { if } \exists m, k \mid i_{m}=k \wedge x_{i_{m}} \neq y_{i_{m}} \\
\Phi_{i_{1}, \ldots, i_{M}}\left(Y_{i_{1}}=x_{i_{1}}, \ldots, Y_{i_{M}}=x_{i_{M}}\right) & \text { otherwise }
\end{array}\right.
\end{gathered}
$$


(a) $\Phi_{1,2}\left(y_{1}, y_{2}\right)$


(b) $\tilde{\Phi}_{1,2}\left(y_{1}, y_{2}\right)$

Table 1: Left: example potential of an MRF $\mathcal{M}$ for variables $Y_{1}$ and $Y_{2}$, each with three levels $\{1,2,3\}$. Right: corresponding potential for $\mathcal{M}^{Y_{2}=3}$.

In other words, we copy the original potential but zero-out all entries that do not honor the assignment of values $\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}$. See Table 1 for an example using a bivariate potential.

Intuitively, the modified MRF $\mathcal{M}^{\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}}$ represents the unnormalized probability for all variable assignments that are compatible with $\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}$. In particular, if $\mathcal{M}_{\boldsymbol{Y}_{K}}$ denotes the marginalization of a network $\mathcal{M}$ over all variables in $\boldsymbol{Y}_{K}$, we have that $\left(\mathcal{M}^{\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}}\right)_{\boldsymbol{Y}}=$ $P\left(\boldsymbol{Y}_{K}=\boldsymbol{y}_{K}\right)$. In other words, computing $g$ reduces to marginalizing our MRF. In this paper, we marginalize it exactly using the variable elimination (VE) algorithm (see e.g Darwiche, 2009a). This method is differentiable w.r.t. all parameters $\boldsymbol{\theta}$ since VE only relies on variable summation and factor multiplication. Any other differentiable inference algorithm could be used as well (for instance, the junction tree algorithm as in Kjaerulff and van der Gaag, 2000). This step, evaluating the function $g$, is known as the forward pass in the neural network literature. Next, we backpropagate the previous operation (a step known as the backward pass) to build the gradient $\nabla g$. Crucially, note that backpropagation yields $\partial g / \partial \theta$ for every parameter $\theta \in \boldsymbol{\theta}$ of the network at once, not just an individual $\theta_{i}$. Last, we obtain parameters $c_{0}, c_{i}, d_{0}, d_{i}$ as detailed before, and use them to compute the metrics of Sections 2.2.1-2.2.3 for each $\theta_{i}$.

Note the advantages of this approach as compared to other alternatives. For example, symbolically deriving the gradient of $g$ would be cumbersome and depend on the target network topology and definition of the probability of interest (Darwiche, 2003). Automatic differentiation avoids this by evaluating the gradient numerically using the chain rule. Furthermore, finding the gradient using finite differences would require evaluating $g$ twice per parameter $\theta_{i}$. In contrast, automatic differentiation only requires a forward and backward pass to find the entire gradient -in our experiments, roughly the time of just two marginalization operations (see below).

# 3.1.4 Additional one-way information 

Although YODO is specifically designed to compute the coefficients of the one-way sensitivity function of Equation (3), it further provides all the information to answer additional sensitivity questions:

- It provides the admissible regions for every parameter in $\boldsymbol{\theta}$ concerning the event of interest $Y_{O}=y_{O} \mid \boldsymbol{Y}_{E}=\boldsymbol{y}_{E}$, since they formally only depend on the coefficients $c_{0}, c_{i}, d_{0}, d_{i}$ as shown in Equations (17) and (18).
- It can quickly find the parameters that do not affect the output probability of interest. This set is usually called the parameter sensitivity set (Coupé and van der Gaag, 2002). This consists of the parameters $\theta_{i}$ for which $c_{i}$ and/or $d_{i}$ are non-zero.
- It identifies whether a parameter change leads to a monotonically increasing or decreasing sensitivity function, as already addressed in Bolt and Renooij (2017). Again this can be straightforwardly derived by checking the sign of $c_{i} d_{0}-c_{0} d_{i}$ : see Equation (6).


### 3.2 YODO for multi-way sensitivity analysis

Although there would be no difficulty in conceptually considering simultaneous variations of multiple parameters, we restrict our attention to 2-way sensitivity analyses where only pairs of parameters are varied. This is because: (i) sensitivity functions cannot be visualized in higher dimensions; (ii) the number of groups of parameters grows exponentially; (iii) most critically, the associated measures are challenging to interpret, similar to higher-order interactions in standard statistical models (see e.g. Hayes et al., 2012).

The 2-way version of the sensitivity function considered before would entail computing the unknowns $c_{12}$ and $d_{12}$ from Equation 12. This can be achieved by computing the Hessian, rather than the gradient, in the previous calculations, which is supported in most modern autodifferentiation packages. However, the sheer size of the Hessian (up to $10^{10}$ in the networks considered in Sec. 4.1) would make the interpretation of such indices a challenge of its own.

Therefore, we advocate that the maximum n-way sensitivity value is the most valuable and versatile tool for multi-way sensitivity analysis. From its definition in Equation (13), it is clear that it can be instantaneously computed for a specific combination of parameters $\boldsymbol{\theta}_{n}$ once the YODO algorithm has been run. Still, even when focusing on $n=2$, the possible $\boldsymbol{\theta}_{n}$ can become overwhelmingly large for medium-sized BNs. To address this, we introduce an algorithm to obtain the top $K s v_{\max }$ pairs efficiently by noting that parameters $\boldsymbol{\theta}$ contribute to Equation (14) independently from each other. We use a priority queue and proceed in a dynamic programming fashion, whereby we start with a pool $\mathcal{P}$ of $K$ best candidates and keep track of $\max _{j} s v_{\max }^{\theta_{i}, \theta_{j}}$ for all $i \in \mathcal{P}$. The top $K$ pairs are guaranteed to be found after $K$ steps. The algorithm relies on sorting $n$ elements and on $K$ insertions

and deletions on the queue and runs in $O\left(n \log n+K^{2} \log K\right)$ operations. See Algorithm 1 for all details.

```
Algorithm 1: Algorithm to find the top \(K\) maximum 2-way sensitivity values
\(\theta_{i}, \theta_{j}\) for any \(i, j \in[n]\).
    // Gather contributions to Eq. 14 from every BN parameter \(\theta_{i}\)
    \(v \leftarrow\) empty vector
    for \(i \leftarrow 1\) to \(n\) do
        \(v_{i} \leftarrow\left(c_{i} d_{0}^{i}-c_{0}^{i} d_{i}\right)^{2}\)
    end for
    \(v \leftarrow \operatorname{sortDescending}(v)\)
    // Populate the queue with \(K\) initial candidates
    \(q \leftarrow\) empty priority queue
    for \(i \leftarrow 1\) to \(K\) do
        \(q \cdot \operatorname{put}\left(\frac{1}{p\left(\boldsymbol{V}_{E}=\boldsymbol{y}_{E}\right)^{2}} \sqrt{v_{i}+v_{i+1}}, i, i+1\right) / /\) First element acts as queue's key
    end for
    // Read the queue's largest \(K\) keys while updating it
    \(w \leftarrow\) empty vector
    for \(k \leftarrow 1\) to \(K\) do
        \((v, i, j) \leftarrow q . \operatorname{get}()\)
        \(w_{k} \leftarrow v\)
        if \(j<n\) then
            // Insert next pair candidate
            \(q \cdot \operatorname{put}\left(\frac{1}{p\left(\boldsymbol{V}_{E}=\boldsymbol{y}_{E}\right)^{2}} \sqrt{v_{i}+v_{j+1}}, i, j+1\right)\)
        end if
    end for
    return \(w\)
```


# 3.3 Implementation 

In order to perform variable elimination efficiently, we note that the problem of graphical model marginalization is equivalent to that of tensor network contraction (Robeva and Seigal, 2018), and use the library opt_einsum (Smith and Gray, 2018) which offers optimized heuristics for the latter. As backend, we use the state-of-the-art machine learning library PyTorch (Paszke et al., 2019), version 1.13.1, to do all operations between tensors and then perform backpropagation on them. We use pgmpy (Ankan and Panda, 2015) for reading and moralizing BNs.

## 4. Results

We first study the method's scalability by testing it on large networks with hundreds of nodes and arcs and up to $10^{5}$ parameters; we then overview the insights revealed by our


Table 2: Our method was applied to 10 Bayesian networks, here sorted by the number of nodes. All times are in seconds. The times for the baseline (third-to-last column) were estimated as the total number of parameters in the network and the time needed to estimate one sensitivity value numerically. Treewidths were found with the NetworkX graph library Hagberg et al. (2008). The last column reports the time needed to find the top $20 \mathrm{sv}_{\text {max }}$ pairs based on existing YODO gradients.
method when applied to two Bayesian networks. All experiments were run on a 4-core i5-6600 3.3GHz Intel workstation with 16GB RAM.

# 4.1 Simulation study 

First, we run our method over the 10 Bayesian networks considered in Scutari et al. (2019). As a baseline, we use the numerical estimation of each sensitivity value via finite differences, whereby we slightly perturb each parameter $\theta_{i}$ and measure the impact on $f$. As a probability of interest, we set $P(A=a \mid B=b)$, where $A, B, a, b$ were two variables, and two levels picked randomly, respectively. Each timing is the average of three independent runs. Results are reported in Table 2, which shows that YODO outperforms the baseline by several orders of magnitude and that computing the most relevant 2-way sensitivity values takes in the order of 2 s at most.

### 4.2 Risk assessment for humanitarian crises and disasters

We next extend the analysis of Ballester-Ripoll and Leonelli (2022b), which only focused on one-way indices, to assess the country-level risk associated with humanitarian crises and disasters. The data was collected from INFORM (INFORM, 2022) and consists of 20 drivers of disaster risk covering natural, human, socio-economic, institutional, and infrastructure factors that influence the country-level risk of a disaster, together with a final country risk index which summarizes how exposed a country is to the possibility of a humanitarian disaster. Table 3 reports an overview of the twenty drivers considered, which cover three main risk dimensions: Hazard and exposure (natural/human); Vulnerability (Socioeconomic/Vulnerable groups); Lack of coping capacity (institutional/infrastructure). All


Table 3: Variables considered for the humanitarian network from the INFORM (2022) dataset.
![img-0.jpeg](img-0.jpeg)

Figure 1: BN learned over the INFORM (2022) dataset for country-level disaster risk.
variables take values between zero and ten. Using the equal-length method, they have been discretized into three categories (low/0, medium/1, high/2). The dataset comprises 190 countries.


Table 4: Four sensitivity metrics for the top 20 parameters of the humanitarian crisis network, when the probability of interest is $P(\operatorname{RISK}=$ high $|\mathrm{FLOOD}=$ high $)$.

Similar to Qazi and Simsekler (2021), a BN is learned using the hc function of the bnlearn package and is reported in Figure 1. A complete interpretation of the learned DAG is beyond the scope of this paper. However, it can be noticed that most risk factors are independent of the overall country-risk given the development and deprivation index (D AND D).

As an illustration of the YODO method, we compute here all sensitivity measures for the conditional probability of a high risk of disaster ( $\operatorname{RISK}=2$ ) conditional on a high risk of flooding $(\mathrm{FLOOD}=2)$. Computing all metrics for all 183 network parameters with our method took only 0.055 seconds. The results are reported in Table 4 for the 20 most influential parameters according to the sensitivity value. It can be noticed that the most influential parameters come from the conditional distributions of the overall risk given the development and deprivation index (D AND D), as well as from the conditional distribution of the flooding index given a projected conflict risk index (PCR) equal to low.

As an additional illustration, Figure 2 reports the sensitivity value of the parameters for the output conditional probability of an overall high risk given a high earthquake risk. Blue is associated with positive sensitivity values, and red with negative ones. Out of 183 network parameters, 30 have a sensitivity value of zero, meaning that they do not affect the probability of interest. It can be noticed that the most influential parameters have a positive relationship with the output probability, and almost all are associated with the development and deprivation index.

We further investigate in a 2-way sensitivity analysis the effect of parameters' variations over the same probability $P(\operatorname{RISK}=$ high $\mid \operatorname{EARTHQUAKE}=$ high). The 15 largest maximum 2-way sensitivity values are reported in Figure 3. Since these are vector norms, they are always positive irrespective of the relationship between the parameters and the probability of interest. Thus, the coloring should not be interpreted as in Figure 2. Again

![img-1.jpeg](img-1.jpeg)

Figure 2: Top 20 most influential parameters for the humanitarian crisis network, color-coded by the sign of $f^{\prime}\left(\theta_{i}\right)$. The probability of interest is $P(\operatorname{RISK}=$ high $\mid$ EARTHQUAKE $=$ high $)$. Total computation time: 0.038 s .
all parameters associated with the development and deprivation index are the ones that have the most substantial effect on the probability of a country having a high overall risk. Thanks to the efficiency of YODO, these indices are almost instantaneously computed with a total computation time of just 0.047 s .

# 4.3 The role of technology during COVID-19 isolation 

The second BN investigates the role of digital communication technology in facilitating the maintenance of meaningful social relationships and promoting the perception of social support during the COVID-19 lockdown. As reported by Gabbiadini et al. (2020), the data was collected through an online questionnaire in March 2020 in Italy, about two weeks from the beginning of the lockdown that the Italian Government adopted for the urgent containment and management of the COVID-19 epidemiological emergency. The data can be downloaded from Gabbiadini (2020) and includes demographic information about 464 individuals, their use of digital communication technologies, and various psychological measures characterizing their emotional status. Each variable is discretized into either two, three, or four levels using either the equal frequency method or some ad-hoc thresholds to optimize the meaning of the levels. Details are reported in Table 5.

A BN is learned for this dataset using 1000 bootstrap repetitions of a tabu search algorithm and keeping the edges that have appeared more than $50 \%$ of the times. Furthermore, edges from the psychological measures to the technological and demographic variables were

![img-2.jpeg](img-2.jpeg)

Figure 3: Top 15 most influential pairs of parameters for the humanitarian crisis network according to svmax. The probability of interest is $P(\operatorname{RISK}=$ high $\mid \operatorname{EARTHQUAKE}=$ high). Total computation time: 0.033 s .


Table 5: Variables considered for the COVID-19 network from Gabbiadini et al. (2020).

![img-3.jpeg](img-3.jpeg)

Figure 4: BN learned over the COVID-19 dataset from Gabbiadini et al. (2020).
forbidden. Similarly, no edges from the technological to the demographic variables were allowed. These choices were motivated by learning a network whose connections could have a more natural, causal interpretation. Figure 4 reports the learned BN. The two variables connected with psychological measures are age and gender. In particular, given the age of an individual, all other demographic characteristics (except gender) are irrelevant to predict his psychological status. The network, therefore, seems to suggest that age was the main driver for the psychological status of individuals in lockdown.

In this second application, we showcase the computation of the admissible regions using the YODO algorithm. Given a low level of the loneliness index, individuals were most likely spending much time interacting remotely for work during the quarantine (TECH_WORK_Q). Table 6 reports the limits of the admissible regions and other measures ordered from the narrowest interval. The admissible region does not have width one in six cases, all coming from the pmf of TECH_WORK_Q or OCCUPATION. This suggests that the data strongly supports the hypothesis that individuals who did not feel lonely had many online work connections during the lockdown.

As a second illustration, we consider an individual's age, given that he felt very lonely during the lockdown. The BN suggests the most likely value was of individuals older than 24 years old. Table 7 shows the admissible regions for the network parameters and shows that the network is way less robust for this hypothesis. Admissible regions are much narrower, having a width equal to 0.04 for two parameters. It can also be noticed that


Table 6: COVID network for the probability of interest $P($ TECH_WORK_Q $=$ high $\mid$ LONELINESS $=$ low): sensitivity metrics for the 15 parameters with the smallest admissible region. Total computation time: 0.071 s .


Table 7: COVID network for the probability of interest $P(\mathrm{AGE}=\geq 25 \mid$ LONELINESS $=$ high): sensitivity metrics for the 15 parameters with the smallest admissible region. Total computation time: 0.11 s .
parameters with narrow admissible regions come from many different PMFs. Therefore, minor variations in the network parameters would make individuals with less than 25 years more likely to have high levels of loneliness.

# 5. Discussion 

We demonstrated the use of automatic differentiation in BNs and, more specifically, in studying how sensitive they are to parameter variations. The novel algorithms are freely available in Python and are planned to be included in the next release of the bnmonitor R package (Leonelli et al., 2021). Their efficiency was demonstrated through a simulation study. Two critical applications in humanitarian crises and studying the psychological effects of isolation during the COVID-19 pandemic illustrate their use in practice.

Although YODO is specifically designed to compute the coefficients of the one-way sensitivity function in Equation 3, we demonstrated in this paper how it could be used to answer a variety of sensitivity queries, for instance, admissible regions and the identification of the parameter sensitivity set. Importantly, YODO also provides the basis for multi-way sensitivity analyses, and we demonstrated their feasibility in practice.

# Future Work 

The YODO algorithm introduced here is designed explicitly for BN models, but it could also be adapted to work with other graphical models. The study of context-specific independence has been shown to increase the efficiency of various inferential tasks often, and thus we may expect that it could also speed up YODO. Therefore, we plan to adapt it to work over graphical models embedding non-symmetric types of independence, as, for instance, staged trees (Carli et al., 2022; Smith and Anderson, 2008), whose sensitivity functions have also been studied (Leonelli, 2019). Another avenue of research is the adaptation of YODO to work for sum-product networks (Poon and Domingos, 2011; Sánchez-Cauce et al., 2021), a different representation of a factorization of a joint probability distribution, which has become increasingly popular in the past few years.

Although YODO makes various types of multi-way sensitivity analysis feasible, they are still a local approach to investigate the combined effect of parameters' variations on probabilities of interest. Recently, it has been shown that the computation of Sobol indices, a global sensitivity index, is feasible in sensitivity to evidence analyses (Ballester-Ripoll and Leonelli, 2022a). We are currently investigating algorithms to globally assess the effect of the various parameters of a BN and consequently compute their associated Sobol indices.
