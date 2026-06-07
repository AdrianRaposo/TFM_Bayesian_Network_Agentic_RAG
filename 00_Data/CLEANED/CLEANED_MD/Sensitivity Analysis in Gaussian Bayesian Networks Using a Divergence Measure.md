# Sensitivity Analysis in Gaussian Bayesian Networks Using a Divergence Measure 

MIGUEL A. GÓMEZ-VILLEGAS ${ }^{1}$, PALOMA MAÍN ${ }^{1}$, AND ROSARIO SUSI ${ }^{2}$<br>${ }^{1}$ Department of Statistics and Operational Research, University Complutense of Madrid, Madrid, Spain<br>${ }^{2}$ Department of Statistics and Operational Research III, University Complutense of Madrid, Madrid, Spain


#### Abstract

This article develops a method for computing the sensitivity analysis in a Gaussian Bayesian network. The measure presented is based on the Kullback-Leibler divergence and is useful to evaluate the impact of prior changes over the posterior marginal density of the target variable in the network. We find that some changes do not disturb the posterior marginal density of interest. Finally, we describe a method to compare different sensitivity measures obtained depending on where the inaccuracy was. An example is used to illustrate the concepts and methods presented.


Keywords Gaussian Bayesian network; Kullback-Leibler divergence; Sensitivity analysis.

Mathematics Subject Classification Primary 62F15; Secondary 62F03.

## 1. Introduction

Bayesian network is a graphical probabilistic model that provides a graphical framework of complex domains with lots of inter-related variables. Graphical probabilistic models are used in some different fields like planning and control, medical diagnosis, dynamic systems, and time-series, to name a few.

Bayesian networks have been studied by Pearl (1988), Lauritzen (1996), Castillo et al. (1997a), Heckerman (1998), Jensen (2001) among others.

A Bayesian network is composed of two parts: a qualitative and quantitative part. The qualitative part is a directed acyclical graph (DAG) where the nodes

Address correspondence to Miguel A. Gómez-Villegas, Department of Statistics and Operational Research, University Complutense of Madrid, Madrid, Spain; E-mail: ma.gv@mat.ucm.es

represent variables under study and the arcs represent relations or dependences between variables. The quantitative part of the Bayesian network is a joint probability distribution written as a product of conditional probabilities that describes the dependences between the variables shown in the qualitative part. Variables can be discrete, continuous, or both, forming, respectively, a Discrete Bayesian network, a Continuous Bayesian network, or a Mixed Bayesian network. With both qualitative and quantitative parts we can compute, within a problem, any prior or posterior probability of interest. Some authors like Lauritzen and Spiegelhalter (1988) or Cowell et al. (1999) have presented efficient algorithms to compute any probability of interest in a Bayesian network.

In order to construct the quantitative part of the Bayesian network, the help of domain experts or available data to estimate the parameters is necessary. Generally, this is a hard task because of the great number of parameters involved in the problem, the partial knowledge of the problem, or the incompleteness of data, and sometimes the assessment obtained is inaccurate. This inaccuracy has influence on the network's output.

To evaluate the Bayesian network's output we can study the robustness of the network with a sensitivity analysis, which is useful to know the impact of changes on a network's results. In general, sensitivity analysis of a mathematical model amounts to investigating the effects of the inaccuracy in the model parameters on its output (Coupé and van der Gaag, 2002).

In recent years, some sensitivity analysis techniques for Bayesian networks have been developed. Among other authors, in Discrete Bayesian networks, Laskey (1995) presents a sensitivity analysis based on computing the partial derivative of a posterior marginal probability with respect to a given parameter, Coupé et al. (2000) develop efficient sensitivity analysis based on inference algorithms, and Chan and Darwiche (2005) introduce a sensitivity analysis based on a distance measure. In Gaussian Bayesian networks, Castillo and Kjaerulff (2003) present a sensitivity analysis based on symbolic propagation.

In this article, we utilize the Kullback-Leibler divergence as a sensitivity measure to compute the sensitivity analysis in a Gaussian Bayesian network, and we show how changes in the model parameters influence the posterior marginal or conditional probability distributions after introducing evidence in the Gaussian network. Moreover, we have developed a graphical method and an algorithm to compare different values of the sensitivity measure obtained, to decide which parameters are most influential.

The article is organized as follows. In Sec. 2 we briefly introduce definitions of Bayesian networks and Gaussian Bayesian networks and present our working example. In Sec. 3, we review how propagation in Gaussian Bayesian networks can be performed. In Sec. 4, we explain the sensitivity analysis based on the Kullback-Leibler divergence in the Gaussian Bayesian network, and study the parameters which have no influence on the output network. In Sec. 5, we run the sensitivity analysis over the working example and present a method to determine the most influential parameters. Finally, the article ends with some conclusions.

# 2. Gaussian Bayesian Networks 

Formally, Bayesian networks can be defined as the following.

Definition 2.1 (Bayesian Network). A Bayesian network is a couple ( $\mathscr{G}, \mathscr{P}$ ) where $\mathscr{G}$ is a directed acyclic graph (DAG), which nodes represent random variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ and edges represent probabilistic dependences, $\mathscr{P}=\left\{p\left(x_{1} \mid p a\left(x_{1}\right)\right), \ldots, p\left(x_{n} \mid p a\left(x_{n}\right)\right)\right\}$ is a set of conditional probability densities (one for each variable) and $p a\left(x_{i}\right)$ is the set of parents of node $X_{i}$ in $\mathscr{G}$. The set $\mathscr{P}$ defines the associated joint probability density as

$$
p(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

Gaussian Bayesian networks have been treated by Shachter and Kenley (1989), Castillo et al. (1997a), and Cowell et al. (1999), among others, and can be defined by the following.

Definition 2.2 (Gaussian Bayesian Network). A Gaussian Bayesian network is a Bayesian network with the joint probability density associated with its variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ being multivariate normal distribution $N(\mu, \Sigma)$, given by

$$
f(\mathbf{x})=(2 \pi)^{-n / 2}|\Sigma|^{-1 / 2} \exp \left\{-\frac{1}{2}(\mathbf{x}-\mu)^{\prime} \Sigma^{-1}(\mathbf{x}-\mu)\right\}
$$

with $\mu$ the $n$-dimensional mean vector and $\Sigma$ the $n \times n$ covariance matrix.
Let $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ be a set of $n$ continuous variables with a multivariate normal distribution $N(\mu, \Sigma)$ as the model before propagating the evidence, with parameters $\mu$ a $n$-dimensional mean vector and $\Sigma$ a $n \times n$ positive definite covariance matrix. The conditional density associated with $X_{i}$ for $i=1, \ldots, n$ verifying Eq. (1), is the univariate normal distribution, given by

$$
f\left(x_{i} \mid p a\left(x_{i}\right)\right) \sim N\left(\mu_{i}+\sum_{j=1}^{i-1} \beta_{i j}\left(x_{j}-\mu_{j}\right), v_{i}\right)
$$

where $\beta_{i j}$ is the regression coefficient of $X_{j}$ on its parents, and $v_{i}=\Sigma_{i}-\Sigma_{i P a\left(x_{i}\right)} \Sigma_{P a\left(x_{i}\right)}^{-1} \Sigma_{i P a\left(x_{i}\right)}^{i}$ is the conditional variance of $X_{i}$ given its parents. Shachter and Kenley (1989) describe the transformation from $v_{i}$ and $\beta_{i j}$ to the precision matrix $W=\Sigma^{-1}$.

Remark that $\beta_{i j}=0$ if and only if there is no link from $X_{j}$ to $X_{i}$.
The concept of Gaussian Bayesian network is illustrated with an example presented by Castillo and Kjaerulff (2003) and that will be used throughout the paper to illustrate the sensitivity analysis.

Example 2.1. The qualitative part of the network is the DAG reproduced in Fig. 1; the node of interest, $X_{4}$, is indicated by a double circle and the quantitative part of the network is given by a multivariate normal distribution with two vector-valued parameters, the mean vector $\mu$, and the covariance matrix $\Sigma$, that compose the joint probability density.

![img-0.jpeg](img-0.jpeg)

Figure 1. DAG of the Gaussian Bayesian network.

The random variable $\left\{X_{1}, X_{2}, X_{3}, X_{4}\right\} \sim N(\mu, \Sigma)$ with parameters

$$
\mu=\left(\begin{array}{c}
3 \\
4 \\
9 \\
14
\end{array}\right) \text { and } \Sigma=\left(\begin{array}{cccc}
4 & 4 & 8 & 12 \\
4 & 5 & 8 & 13 \\
8 & 8 & 20 & 28 \\
12 & 13 & 28 & 42
\end{array}\right)
$$

In this case, Eq. (1) is given by

$$
f\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=f\left(x_{1}\right) f\left(x_{2} \mid x_{1}\right) f\left(x_{3} \mid x_{1}\right) f\left(x_{4} \mid x_{2}, x_{3}\right)
$$

With the set of conditional probability densities defined by Eq. (3), $f\left(x_{1}\right) \sim N(3,4), f\left(x_{2} \mid x_{1}\right) \sim N\left(1+x_{1}, 1\right), f\left(x_{3} \mid x_{1}\right) \sim N\left(3+2 x_{1}, 4\right), f\left(x_{4} \mid x_{2}, x_{3}\right) \sim$ $N\left(1+x_{2}+x_{3}, 1\right)$.

# 3. Evidence Propagation in Gaussian Bayesian Networks 

Different algorithms have been presented to propagate evidence in Gaussian Bayesian networks (Castillo et al., 1977b; Normand and Tritchler, 1992). We are going to work with the propagation model presented by Castillo et al. (1977b) based on computing the conditional probability density of a multivariate normal distribution given the set of evidential variables. Therefore, considering the partition $\mathbf{X}=(\mathbf{Y}, \mathbf{E})^{\prime}$, the conditional probability distribution of $\mathbf{Y}$, given the evidence $\mathbf{E}=\mathbf{e}$, is multivariate normal with parameters

$$
\mu^{\mathbf{Y} \mid \mathbf{E}=\mathbf{e}}=\mu_{\mathbf{Y}}+\Sigma_{\mathbf{Y E}} \Sigma_{\mathbf{E E}}^{-1}\left(\mathbf{e}-\mu_{\mathbf{E}}\right) \text { and } \Sigma^{\mathbf{Y} \mid \mathbf{E}=\mathbf{e}}=\Sigma_{\mathbf{Y Y}}-\Sigma_{\mathbf{Y E}} \Sigma_{\mathbf{E E}}^{-1} \Sigma_{\mathbf{E Y}}
$$

After propagation, the set of nonevidential variables is $\mathbf{Y}=\mathbf{X} \backslash \mathbf{E}$. Considering the set $E$ with only one element, $\mathbf{Y}$ has $n-1$ elements and the notation used will be $\mathbf{Y}=\left\{X_{1}, \ldots, X_{n-1}\right\}$, although $X_{n} \neq X_{e}$. Moreover, $\mathbf{Y} \mid E=e \sim N\left(\mu^{\mathbf{Y} \mid E=e}, \Sigma^{\mathbf{Y} \mid E=e}\right)$

where the parameters are computed using the equations in (4), that is,

$$
\mu^{\mathbf{Y} \mid E=e}=\left(\begin{array}{c}
\mu_{1}^{Y \mid E=e} \\
\vdots \\
\mu_{n-1}^{Y \mid E=e}
\end{array}\right) \text { and } \Sigma^{\mathbf{Y} \mid E=e}=\left(\begin{array}{cccc}
\sigma_{11}^{Y \mid E=e} & \sigma_{12}^{Y \mid E=e} & \ldots & \sigma_{1 n-1}^{Y \mid E=e} \\
\sigma_{21}^{Y \mid E=e} & \sigma_{22}^{Y \mid E=e} & \ldots & \sigma_{2 n-1}^{Y \mid E=e} \\
\vdots & \vdots & & \vdots \\
\sigma_{n-11}^{Y \mid E=e} & \sigma_{n-12}^{Y \mid E=e} & \ldots & \sigma_{n-1 n-1}^{Y \mid E=e}
\end{array}\right)
$$

Working with this incremental method, i.e., updating one evidential variable at a time, and with a target variable $X_{i} \in Y$, the posterior marginal density of the variable of interest, $X_{i}$, knowing the evidence, is given by

$$
X_{i} \mid E=e \sim N\left(\mu_{i}^{Y \mid E=e}, \sigma_{i i}^{Y \mid E=e}\right)=N\left(\mu_{i}+\frac{\sigma_{i e}}{\sigma_{e e}}\left(e-\mu_{e}\right), \sigma_{i i}-\frac{\sigma_{i e}^{2}}{\sigma_{e e}}\right)
$$

Thus, in Example 2.1 the posterior marginal density of the variable of interest $X_{4}$, given the evidence $E \equiv\left\{X_{2}=9\right\}$, is

$$
X_{4} \mid X_{2}=9 \sim N\left(27, \frac{41}{5}\right)
$$

And the joint density of the variables in $\mathbf{Y}=\left\{X_{1}, X_{3}, X_{4}\right\}$, given the evidence $E \equiv\left\{X_{2}=9\right\}$, is multivariate normal $\mathbf{Y} \mid X_{2}=9 \sim N\left(\mu^{\mathbf{Y} \mid X_{2}=9}, \Sigma^{\mathbf{Y} \mid X_{2}=9}\right)$ with parameters

$$
\mu^{\mathbf{Y} \mid X_{2}=9}=\left(\begin{array}{l}
7 \\
17 \\
27
\end{array}\right) \text { and } \Sigma^{\mathbf{Y} \mid X_{2}=9}=\frac{1}{5}\left(\begin{array}{llll}
4 & 8 & 8 \\
8 & 36 & 36 \\
8 & 36 & 41
\end{array}\right)
$$

# 4. Sensitivity Analysis and Non-Influential Parameters 

When dealing with Gaussian Bayesian networks one is usually interested in the conditional probability density, given the evidence, of the target variable, that is the posterior probability density of the variable of interest $f\left(x_{i} \mid e\right)$.

A key question with respect to Gaussian Bayesian networks is what is the effect of changing a parameter $\mu_{i}, \sigma_{i i}$, or $\sigma_{i j}$ for all $i, j$.

To give an initial answer to this question, we add a perturbation $\delta \in \mathbb{R}$ to the original parameter, so that the new value of the parameter becomes $\mu_{i}+\delta, \sigma_{i i}+\delta$ or $\sigma_{i j}+\delta$. The perturbation is incorporated into the network before the evidence propagation, i.e., to the prior distribution of the network. To evaluate the effect of this change we work with the posterior marginal density of interest, thus, the effect is evaluated after the propagation, comparing the posterior marginal density of the target variable $X_{i}$ before and after being perturbed.

Our aim is to know if this change has a large or a small influence or if it has no influence on the distribution of interest. To compute this effect, we work with the Kullback-Leibler (KL) divergence. This is one of the most common discrepancy

measures for comparing probability distributions (Kullback and Leibler, 1951), and it is given by

$$
K L\left(f(w), f^{\prime}(w)\right)=\int_{-\infty}^{\infty} f(w) \ln \frac{f(w)}{f^{\prime}(w)} d w
$$

when $f(w)$ and $f^{\prime}(w)$ are two probability densities with the same support.
Therefore, to study the sensitivity in a Gaussian Bayesian network, we define the sensitivity measure as the KL-divergence between the target posterior marginal density before and after perturbation of the Gaussian Bayesian network, that is the following.

Definition 4.1 (Sensitivity Measure). Let $(\mathscr{G}, \mathscr{P})$ be a Gaussian Bayesian network $N(\mu, \Sigma)$. Let $f\left(x_{i} \mid e\right)$ be the posterior marginal density of interest and $f\left(x_{i} \mid e, \delta\right)$ the same density after perturbation $\delta$ is added to one parameter of the model. The sensitivity measure is defined by

$$
S^{p_{j}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\int_{-\infty}^{\infty} f\left(x_{i} \mid e\right) \ln \frac{f\left(x_{i} \mid e\right)}{f\left(x_{i} \mid e, \delta\right)} d x_{i}
$$

where the subscript $p_{j}$ is parameter being changed and $\delta$ the proposed perturbation, that is, the new value of the parameter is $p_{j}^{\delta}=p_{j}+\delta$.

The process for studying the sensitivity of the network consists of the following. First, the network starts with $n$ variables with parameters $\mu$ and $\Sigma$. One of these variables has a known value, that is the evidential variable $X_{e}$. With this information, the propagation is performed and $f\left(x_{i} \mid e\right)$ is obtained. Then, adding a perturbation $\delta$ to the candidate parameter, the propagation is repeated updating $X_{e}$ again, and $f\left(x_{i} \mid e, \delta\right)$ is obtained. The effect of the change is obtained comparing those density functions by means of the sensitivity measure.

Repeating the process with all candidate parameters, we obtain different sensitivity measures and with this information we know which parameters have no influence on the posterior distribution of interest, which ones have small influence, and which parameters produce a large posterior perturbation. If the resulting sensitivity measure is large, other experts opinions or new available data are necessary to estimate the parameters more accurately.

To compute the sensitivity measure, we have to distinguish two different cases, depending on the parameter, $\mu$ or $\Sigma$, being considered.

# 4.1. Changes in the Mean Vector $\mu$ 

Three different situations are possible depending on the element of $\mu$ being changed. The perturbation can affect $\mu_{i}$, i.e., the mean of the variable of interest $X_{i} \in \mathbf{Y}$, the mean of the evidence variable $\mu_{e}$ with $E \equiv\left\{X_{e}\right\}$, or the mean $\mu_{j}$ of any other variable $X_{j} \in \mathbf{Y}$ with $j \neq i$.

In those cases, the parameters of the model with $\delta$ will be denoted $\mu^{\delta}$ (different in each situation) and $\Sigma^{\delta}=\Sigma$ the covariance matrix in the original model.
4.1.1. Changes in the Mean of the Variable of Interest $\left(\mu_{i}\right)$. In the model with $\delta$, the perturbation is added to the mean of the variable of interest $X_{i}$, i.e.,

$\mu^{\delta}=\left(\mu_{1}, \ldots, \mu_{i}+\delta, \ldots, \mu_{n}\right)^{\prime}$ with $\delta \in \mathbb{R}$. Remember that the model with $\delta$ is defined before evidence propagation.

After making the propagation $E \equiv\left\{X_{e}=e\right\}$, only the $i$ th element of the posterior mean vector depends on $\delta$. Therefore, the probability of interest associated with the target variable is (see (5)):

$$
X_{i} \mid E=e, \quad \delta \sim N\left(\mu_{i}^{Y \mid E=e}+\delta, \sigma_{i i}^{Y \mid E=e}\right)
$$

The sensitivity measure due to a perturbation $\delta$ in the variable of interest is given by

$$
S^{p_{i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{\delta^{2}}{2 \sigma_{i i}^{Y \mid E=e}}
$$

where $\sigma_{i i}^{Y \mid E=e}=\sigma_{i i}-\frac{\sigma_{i i}^{2}}{\sigma_{e e}}$.
4.1.2. Changes in the Mean of the Evidence Variable $\left(\mu_{e}\right)$. In this situation, $\mu^{\delta}=\left(\mu_{1}, \ldots, \mu_{i}, \ldots, \mu_{e}+\delta, \ldots, \mu_{n}\right)^{\prime}$. With the evidence propagation presented in (4), we can see that this change will affect all the elements of the posterior mean vector $\mu^{Y \mid E=e, \delta}$ and will not affect the posterior covariance matrix. Then, the posterior distribution of $X_{i} \in \mathbf{Y}$ is

$$
X_{i} \mid E=e, \quad \delta \sim N\left(\mu_{i}^{Y \mid E=e}-\frac{\sigma_{i e}}{\sigma_{e e}} \delta, \quad \sigma_{i i}^{Y \mid E=e}\right)
$$

The sensitivity due to a perturbation $\delta$ in the evidence variable depends on $\delta$, the posterior variance of the variable of interest $\sigma_{i i}^{Y \mid E=e}$, the variance of the evidence variable $\sigma_{e e}$, and the covariance between the variable of interest and the evidence variable $\sigma_{i e}$, and is given by

$$
S^{p_{e}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{\delta^{2}}{2 \sigma_{i i}^{Y \mid E=e}}\left(\frac{\sigma_{i e}}{\sigma_{e e}}\right)^{2}
$$

where $\sigma_{i i}^{Y \mid E=e}=\sigma_{i i}-\frac{\sigma_{i e}^{2}}{\sigma_{e e}}$.
4.1.3. Changes in the Mean of any Non Evidential Variable ( $\mu_{j}$ with $j \neq i$ ). Taking into account the evidence propagation (4), we can see that if the inaccuracy is in the mean of any non evidential variable $X_{j} \in \mathbf{Y}$, this lack of precision will only affect the variable $X_{j}$ involved in this inaccuracy. Therefore, in this case where the perturbation is added to the mean of $X_{j} \in \mathbf{Y}$ with $j \neq i$, the change will not affect the variable of interest $X_{i}$.

Now, the mean vector $\mu^{\delta}=\left(\mu_{1}, \ldots, \mu_{j}+\delta, \ldots, \mu_{i}, \ldots, \mu_{e}, \ldots, \mu_{n}\right)^{\prime}$.
After propagating the evidence $E \equiv\left\{X_{e}=e\right\}$, only the $j$ th element of the posterior mean vector depends on $\delta$. Thus, the posterior probability density of the variable of interest $X_{i}$ is the same as the original model, because $\delta$ has no influence over $X_{i}$, being the density of $X_{i} \mid E=e, \delta$ the same as $X_{i} \mid E=e \sim N\left(\mu_{i}^{Y \mid E=e}, \sigma_{i}^{Y \mid E=e}\right)$, and obviously, the sensitivity measure is zero.

Thus, we can conclude that, if there exists an interest in a specific variable $X_{i}$ and the mean of other non evidential variable $X_{j}$ is inaccurate, after the evidence

propagation, this lack of precision will not have influence over the variable of interest $X_{i}$ and will only affect the variable $X_{j}$.

# 4.2. Changes in the Covariance Matrix $\boldsymbol{\Sigma}$ 

There are six possible different situations, depending on the parameter of the covariance matrix $\Sigma$ being changed; three if the perturbation is added to the variances (elements in the diagonal of $\Sigma$ ) and another three if the perturbation is added to the covariances of $\Sigma$.

In those cases, the parameters of the perturbed model will be $\mu^{\delta}=\mu$, mean vector of the original model, and $\Sigma^{\delta}$ different in each situation.

When the covariance matrix is perturbed, the structure of the network can change. Those changes are presented in the precision matrix of the perturbed network, that is, the inverse of the covariance matrix with perturbation $\delta$. The sensitivity analysis is done by comparing the posterior information about the variable of interest $X_{i}$ with and without $\delta$, studying all possible situations.
4.2.1. Changes in the Variance of the Variable of Interest $\left(\sigma_{i i}\right)$. The variance of the variable of interest $X_{i}$ is perturbed, i.e., $\sigma_{i i}^{\delta}=\sigma_{i i}+\delta$ with $\delta>-\sigma_{i i}+\frac{\sigma_{i i}^{2}}{\sigma_{e e}}$ and the rest of elements remain as in the original model.

After the evidence propagation, only the $i$ th element in the diagonal of the covariance matrix depends on $\delta$. Then,

$$
X_{i} \mid E=e, \quad \delta \sim N\left(\mu_{i}+\frac{\sigma_{i i}}{\sigma_{e e}}\left(e-\mu_{e}\right),\left(\sigma_{i i}+\delta\right)-\frac{\sigma_{i e}^{2}}{\sigma_{e e}}\right)
$$

The sensitivity measure depends on $\delta$ and $\sigma_{i i}^{Y \mid E=e}$, and is given by

$$
S^{\sigma_{i i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{1}{2}\left[\ln \left(1+\frac{\delta}{\sigma_{i i}^{Y \mid E=e}}\right)-\frac{\delta}{\sigma_{i i}^{Y \mid E=e, \delta}}\right]
$$

where $\sigma_{i i}^{Y \mid E=e, \delta}$ is the posterior variance of $X_{i}$ in the model with $\delta$.
The model and the result of the sensitivity measure show that it is necessary to impose the restriction $\delta>-\sigma_{i i}+\frac{\sigma_{i i}^{2}}{\sigma_{e e}}$.
4.2.2. Changes in the Variance of the Evidence Variable $\left(\sigma_{e e}\right)$. In this case, $\delta$ is added to the variance of the evidence variable $X_{e}$.

After the evidence propagation, the perturbation $\delta$ affects all the elements of the mean vector and the covariance matrix. Therefore, the model is $\mathbf{Y} \mid E=e$, $\delta \sim N\left(\mu^{\mathbf{Y} \mid E=e, \delta}, \Sigma^{\mathbf{Y} \mid E=e, \delta}\right)$ being $\mu^{\mathbf{Y} \mid E=e, \delta}$ such that $\mu_{j}^{\mathbf{Y} \mid E=e, \delta}=\mu_{j}+\frac{\sigma_{j i}}{\sigma_{e e}+\delta}\left(e-\mu_{e}\right)$ with $j=1, \ldots, n-1$ and $\Sigma^{\mathbf{Y} \mid E=e, \delta}$ with $\sigma_{j k}^{\mathbf{Y} \mid E=e, \delta}=\sigma_{j k}-\frac{\sigma_{j i} \sigma_{e k}}{\sigma_{e e}+\delta}$ to all possible values of $j, k$.

The posterior distribution of the variable of interest is

$$
X_{i} \mid E=e, \quad \delta \sim N\left(\mu_{i}+\frac{\sigma_{i e}}{\sigma_{e e}+\delta}\left(e-\mu_{e}\right), \quad \sigma_{i i}-\frac{\sigma_{i e}^{2}}{\sigma_{e e}+\delta}\right)
$$

The sensitivity measure with respect to a perturbation of the evidence variable variance is given by

$$
S^{\sigma_{e e}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{1}{2}\left[\ln \left(\frac{\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}}{\sigma_{i i}^{\mathrm{Y} \mid E=e}}\right)+\frac{\frac{\sigma_{i i}^{2}}{\sigma_{e e}}\left(\frac{-\delta}{\sigma_{e e}+\delta}\right)\left(1+\left(e-\mu_{e}\right)^{2}\left(\frac{-\delta}{\left(\sigma_{e e}+\delta\right) \sigma_{e e}}\right)\right)}{\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}}\right]
$$

To guarantee the structure of the network it is necessary that $\Sigma^{\mathrm{Y} \mid E=e, \delta}$ be a positive definite matrix.
4.2.3. Changes in the Variance of Any Non Evidential Variable ( $\sigma_{i j}$ with $j \neq i$ ). In the last case of variances, the variance of any non evidential variable $X_{j} \in \mathbf{Y}$ different from the target variable is perturbed, i.e., $\sigma_{i j}^{\delta}=\sigma_{j}+\delta$.

After the propagation, the change introduced only affects the variance of $X_{j}$. Then, the posterior probability density of $X_{i}$ is the same as the original model in (6), because $\delta$ has no influence over $X_{i}$, being $f\left(x_{i} \mid e, \delta\right)=f\left(x_{i} \mid e\right)$.

Clearly in this case the sensitivity measure is zero.
We can conclude that, if a non evidential variable $X_{j}$ with the prior variance inaccurate exists, this inaccuracy will not affect the results over the variable of interest $X_{i}$ and will only affect the posterior results about $X_{j}$.
4.2.4. Changes in the Covariance Between the Variable of Interest and the Evidence Variable $\left(\sigma_{i e}\right)$. In this case the covariance between the variable of interest $X_{i} \in \mathbf{Y}$ and the evidential variable $X_{e}$ is perturbed, i.e., $\sigma_{i e}^{\delta}=\sigma_{i e}+\delta=\sigma_{e i}^{\delta}$.

After the evidence propagation, $\delta$ only affects the parameters related with $X_{i}$, being the posterior mean $\mu_{i}^{\mathrm{Y} \mid E=e, \delta}=\mu_{i}^{\mathrm{Y} \mid E=e}+\frac{\delta}{\sigma_{e e}}\left(e-\mu_{e}\right)$, the posterior variance $\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}=\sigma_{i i}^{\mathrm{Y} \mid E=e}-\frac{\delta^{2}+2 \sigma_{i e} \delta}{\sigma_{e e}}$, and the posterior covariance between $X_{i}$ and the rest of non evidential variables $\sigma_{i j}^{\mathrm{Y} \mid E=e, \delta}=\sigma_{i j}^{\mathrm{Y} \mid E=e}-\frac{\sigma_{i e} \delta}{\sigma_{e e}}=\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}$ where $i \neq j$. The model obtained is a multivariate normal distribution with the rest of elements in the mean vector given by $\mu_{i}^{\mathrm{Y} \mid E=e, \delta}=\mu_{i}^{\mathrm{Y} \mid E=e}$ with $j \neq i$ and variances and covariances not related to $X_{i}$ given by $\sigma_{i j}^{\mathrm{Y} \mid E=e, \delta}=\sigma_{i j}^{\mathrm{Y} \mid E=e}$ where $j \neq i$ and $\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}=\sigma_{i i}^{\mathrm{Y} \mid E=e}$ with $j \neq i$ and $k \neq i$. Then, the posterior distribution of the variable of interest is

$$
X_{i} \mid E=e, \quad \delta \sim N\left(\mu_{i}+\frac{\left(\sigma_{i e}+\delta\right)}{\sigma_{e e}}\left(e-\mu_{e}\right), \sigma_{i i}-\frac{\left(\sigma_{i e}+\delta\right)^{2}}{\sigma_{e e}}\right)
$$

The sensitivity measure depends on $\delta, \sigma_{i e}, \sigma_{e e}, e, \mu_{e}$, and $\sigma_{i}^{\mathrm{Y} \mid E=e}$ and is given by

$$
S^{\sigma_{i e}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{1}{2}\left[\ln \left(1-\frac{\delta^{2}+2 \sigma_{i e} \delta}{\sigma_{e e} \sigma_{i i}^{\mathrm{Y} \mid E=e}}\right)+\frac{\sigma_{i i}^{\mathrm{Y} \mid E=e}+\left(\frac{\delta}{\sigma_{e e}}\left(e-\mu_{e}\right)\right)^{2}}{\sigma_{i i}^{\mathrm{Y} \mid E=e, \delta}}-1\right]
$$

To guarantee the description of the network it is necessary to impose that $\Sigma^{\mathrm{Y} \mid E=e, \delta}$ be a positive definite matrix.

4.2.5. Changes in the Covariance Between the Variable of Interest and Other Non Evidential Variable $\left(\sigma_{i j}\right)$. In this case, the covariance between the variable of interest $X_{i} \in \mathbf{Y}$ and other non evidential variable $X_{j} \in \mathbf{Y}$ is perturbed, i.e., $\sigma_{i j}^{\delta}=\sigma_{i j}+\delta=\sigma_{j i}^{\delta}$.

After the evidence propagation, only the posterior covariance between $X_{i}$ and $X_{j}$ is effected by the change, being $\sigma_{i j}^{Y \mid E=e, \delta}=\sigma_{i j}^{Y \mid E=e}+\delta=\sigma_{j i}^{Y \mid E=e, \delta}$. Then, the posterior probability density of $X_{i}$ is $f\left(x_{i} \mid e, \delta\right)=f\left(x_{i} \mid e\right)$ with $X_{i} \mid E=e \sim N\left(\mu_{i}^{Y \mid E=e}, \sigma_{i}^{Y \mid E=e}\right)$, which implies a null sensitivity measure.

If the interest is in the posterior density of $X_{i}$, the inaccuracy in $\sigma_{i j}$ does not affect the mean and the variance of $X_{i}$ although $\delta$ appears in the posterior covariance between $X_{i}$ and $X_{j}$.
4.2.6. Changes in the Covariance Between the Evidence Variable and Other Non Evidential Variable $\left(\sigma_{e j}\right)$. The covariance between $X_{e}$ and $X_{j} \in \mathbf{Y}$ with $j \neq i$ is perturbed, i.e., $\sigma_{e j}^{\delta}=\sigma_{e j}+\delta=\sigma_{j e}^{\delta}$.

After the propagation, the perturbation appears only in the parameters related to $X_{j}$, being the network multivariate normal with the posterior mean vector $\mu^{\mathbf{Y} \mid E=e, \delta}$ such that $\mu_{j}^{\mathbf{Y} \mid E=e, \delta}=\mu_{j}^{Y \mid E=e}+\frac{\delta}{\sigma_{e e}}\left(e-\mu_{e}\right)$ and $\mu_{k}^{\mathbf{Y} \mid E=e, \delta}=\mu_{k}^{\mathbf{Y} \mid E=e}$ where $k \neq j$; and the covariance matrix $\Sigma^{\mathbf{Y} \mid E=e, \delta}$ such that the posterior variance of $X_{j}$ is given by $\sigma_{j j}^{\mathbf{Y} \mid E=e, \delta}=\sigma_{j j}^{Y \mid E=e}-\frac{\delta^{2}+2 \sigma_{j e} \delta}{\sigma_{e e}}$ and the covariances between $X_{j}$ and any other variable in $\mathbf{Y}$ are $\sigma_{j k}^{\mathbf{Y} \mid E=e, \delta}=\sigma_{j k}^{\mathbf{Y} \mid E=e}-\frac{\sigma_{j e} \delta}{\sigma_{e e}}=\sigma_{k j}^{\mathbf{Y} \mid E=e, \delta}$ where $k \neq j$; the rest of the elements of $\Sigma^{\mathbf{Y} \mid E=e, \delta}$ are the same as the model without $\delta$. Therefore, the posterior probability density of the variable of interest $X_{i}$ is the same as the model without perturbation, i.e., the sensitivity measure is zero.

With those results associated with inexact elements in the mean vector and in the covariance matrix, we can conclude that if we are interested in the posterior density of the target variable $X_{i}$, inaccuracy in an element of any non evidential variable $X_{j} \in \mathbf{Y}$ with $j \neq i$ will not affect the results about $X_{i}$, being the sensitivity measure zero.

Moreover, changes in the mean vector only affects the posterior mean $\mu^{\mathbf{Y} \mid E=e}$ (not to $\Sigma^{\mathbf{Y} \mid E=e}$ ), therefore, the sensitivity measure can be large because we are comparing two densities with different mean and the same variance. However, changes in the covariance matrix can affect only the posterior variance of $X_{i}$, or the posterior mean and variance of $X_{i}$.

# 5. Experimental Results and Selection of the Most Influential Parameter 

Next, we use Example 2.1 to illustrate the results presented in the previous section.
Example 5.1. Consider the Gaussian Bayesian network given in Example 2.1. Experts disagree with the mean $\mu_{4}$ of the variable of interest $X_{4}$, that could be $\mu_{4}^{\delta_{1}}=10=\mu_{4}+\delta_{1}$ (with $\delta_{1}=-4$ ); There are different opinions about the evidential variable $X_{2}$, because they think that $\mu_{2}$ could be $\mu_{2}^{\delta_{2}}=6=\mu_{2}+\delta_{2}$ (with $\delta_{2}=2$ ), and that $\sigma_{22}$ could be $\sigma_{22}^{\delta_{2}}=6$ with $\delta_{3}=1$; moreover, $\sigma_{23}$ could be $\sigma_{23}^{\delta_{3}}=9$ with $\delta_{4}=1$ (the same to $\sigma_{32}$ ) and $\sigma_{24}$ could be $\sigma_{24}^{\delta_{2}}=11$ with $\delta_{5}=-2$ (the same as $\sigma_{42}$ ).

To know how this inaccuracy can influence the posterior marginal density of the target variable $X_{4}$, we study those changes one by one computing the sensitivity

measure in each case, that is, comparing the posterior density presented in (7) with the posterior density when $\delta_{i}$ is introduced in the model, with $i=1, \ldots, 5$.

First, it is necessary to verify the proposed values of $\delta_{i}$, because after the evidence propagation the covariance matrix must be a positive definite matrix. This restriction only affects $\delta_{3}, \delta_{4}$, and $\delta_{5}$. Checking the restriction over the obtained posterior covariance matrix, $\Sigma^{Y \mid X_{2}=9, \delta_{i}}$ with $i=\{3,4,5\}$, we can compute the sensitivity measures as

- If the inaccuracy is in the variable of interest $X_{4}$, given by $\mu_{4}=14+\delta_{1}=10$ $\left(\delta_{1}=-4\right)$, after the evidence propagation, the posterior marginal mean decreases and the variance is the same as the one obtained in the model without $\delta_{1}$. The sensitivity measure is

$$
S^{\mu_{4}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta_{1}\right)\right)=\frac{\delta_{1}^{2}}{2 \sigma_{44}^{Y \mid X_{2}=9}}=0.9756
$$

- If the mean of the evidential variable is $\mu_{2}=4+\delta_{2}=6\left(\delta_{2}=2\right)$, after the evidence propagation the posterior mean of $X_{4}$ changes. The sensitivity measure, comparing the posterior density of the variable of interest in the network with and without $\delta_{2}$, is

$$
S^{\mu_{2}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta_{2}\right)\right)=\frac{\delta_{2}^{2}}{2 \sigma_{44}^{Y \mid X_{2}=9}}\left(\frac{\sigma_{42}}{\sigma_{22}}\right)^{2}=1.6488
$$

- With $\sigma_{22}=5+\delta_{3}=6\left(\delta_{3}=1\right)$, after the evidence propagation, the mean decreases and the variance increases. Studying the inverse of the new covariance matrix, we see that the independence relations have changed, changing the structure of the network. The sensitivity measure is

$$
\begin{aligned}
& S^{\sigma_{22}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta_{3}\right)\right) \\
& \quad=\frac{1}{2}\left[\ln \left(\frac{\sigma_{44}^{Y \mid X_{2}=9, \delta_{3}}}{\sigma_{44}^{Y \mid X_{2}=9}}\right)+\frac{\frac{\sigma_{42}^{2}}{\sigma_{22}}\left(\frac{-\delta_{3}}{\sigma_{22}+\delta_{3}}\right)\left(1+\left(e-\mu_{2}\right)^{2}\left(\frac{-\delta_{3}}{\left(\sigma_{22}+\delta_{3}\right) \sigma_{22}}\right)\right)}{\sigma_{44}^{Y \mid X_{2}=9, \delta_{3}}}\right]=0.2275
\end{aligned}
$$

- Being $\sigma_{23}=8+\delta_{4}=9\left(\delta_{4}=1\right)$ the posterior distribution of $X_{4}$ is not influenced by this change, although the design of the network changes. Comparing the posterior density of $X_{4}$ with and without $\delta_{4}$ the sensitivity measure is zero, that is,

$$
S^{\sigma_{23}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta_{4}\right)\right)=0
$$

- The last change is to consider $\sigma_{24}=13+\delta_{5}=11\left(\delta_{5}=-2\right)$, that produces changes in the network. In the resulting model of $X_{4} \mid X_{2}$ the mean decreases and the variance increases. The sensitivity measure is given by

$$
\begin{aligned}
& S^{\sigma_{24}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta_{5}\right)\right) \\
& \quad=\frac{1}{2}\left[\ln \left(1-\frac{\delta_{5}^{2}+2 \sigma_{24} \delta_{5}}{\sigma_{22} \sigma_{44}^{Y \mid X_{2}=9}}\right)+\frac{\sigma_{44}^{Y \mid X_{2}=9}+\left(\frac{\delta_{5}}{\sigma_{22}}\left(e-\mu_{2}\right)\right)^{2}}{\sigma_{44}^{Y \mid X_{2}=9, \delta_{5}}}-1\right]=0.2302
\end{aligned}
$$

Comparing the different sensitivity measures obtained (without consideration of the zero measure), we have

$$
\begin{aligned}
S^{\sigma_{22}}\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta_{3}\right)\right) & <S^{\sigma_{24}}\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta_{3}\right)\right)<S^{\mu_{4}}\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta_{1}\right)\right) \\
& <S^{\mu_{2}}\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta_{2}\right)\right)
\end{aligned}
$$

In this example we can see that when an element of the covariance matrix is perturbed, the parameters of the posterior marginal density of $X_{4}$ change, obtaining a different mean and a larger variance than the posterior variance obtained for the unperturbed model, therefore, when those densities are compared, the sensitivity measure obtained is small, because the model with $\delta$ contains the posterior model without $\delta$. However, if an element of the mean vector, only the mean of the posterior marginal density of $X_{4}$ changes, then the mean in the new distribution is moved to the left or to the right, depending the sign of $\delta$, and the variance is the same as the one in the posterior model without $\delta$; therefore in those cases, the sensitivity measure obtained is larger than in the other cases.

With those results, experts should review the information about the mean of the evidence variable $\mu_{2}$ because the change proposed gives the bigger sensitivity measure obtained $\left(S^{\mu_{2}}\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta_{2}\right)\right)=1.6488\right)$. Moreover, the change proposed to $\sigma_{23}$ does not disturb the posterior marginal density of interest. In the remaining cases, the sensitivity measures obtained are small $\left(S\left(f\left(x_{4} \mid e\right), f\left(x_{4} \mid e, \delta\right)\right) \in(0,1)\right)$, therefore, experts can decide if it is necessary to review the information about $X_{2}$ and the mean about $X_{4}$.

If we suppose that there exist some inaccuracies in the model that are not defined, we can draw the different sensitivity measures obtained for all possible values of $\delta$, considering the sensitivity measure as a function of $\delta$ :

$$
\begin{aligned}
& S^{\mu_{4}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta\right)\right)=\frac{5}{82} \delta^{2} \\
& S^{\mu_{2}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta\right)\right)=\frac{169}{410} \delta^{2} \\
& S^{\sigma_{22}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta\right)\right) \\
& \quad=\frac{1}{2}\left[\ln \left(\frac{5}{41}\left(42-\frac{13^{2}}{5+\delta}\right)\right)+\frac{\frac{13^{2}}{5}\left(\frac{-\delta}{5+\delta}\right)\left(1+25\left(\frac{-\delta}{5(5+\delta)}\right)\right)}{42-\frac{13^{2}}{5+\delta}}\right] \\
& S^{\sigma_{24}}\left(f\left(x_{4} \mid X_{2}=9\right), f\left(x_{4} \mid X_{2}=9, \delta\right)\right) \\
& \quad=\frac{1}{2}\left[\ln \left(1-\frac{\delta^{2}+26 \delta}{41}\right)+\frac{\frac{41}{5}+\delta^{2}}{42-\frac{(13+\delta)^{2}}{5}}-1\right]
\end{aligned}
$$

In Fig. 2 the resulting sensitivity measures are shown. We must take into account that a restriction over the values of $\delta$ exists because the posterior covariance matrix must be positive definite, for that reason not all the values of $\delta$ plotted could be considered in the model. However, Fig. 2 is useful to know how the sensitivity measure depends on $\delta$.

In Fig. 2 we see that if the perturbation of the variance of the evidential variable $\left(\sigma_{22}\right)$ is small and $\delta<0$, it produces a large divergence, then this parameter must be reviewed before changing it to another smaller value. If the value of the $\delta$ introduced

![img-1.jpeg](img-1.jpeg)

Figure 2. Sensitivity measures obtained in the example for any $\delta$ value.
in the covariance between the evidential variable and the variable of interest is small and $\delta>0$, then the sensitivity measure is large.

We can repeat the process to study all the parameters with influence over $X_{4}$ given $E \equiv\left\{X_{2}=9\right\}$. Plotting the sensitivity measures we can find the parameter that produces the largest change in the posterior density of interest.

With this graphical method we can study the influence of $\delta$ on the posterior marginal density of $X_{4}$ by means of the sensitivity measures.

To know what happens when the perturbation $\delta$ is small, we can plot the sensitivity measures delimiting the values of $\delta$. In Fig. 3 we plot the sensitivity measures when $\delta$ and the sensitivity measure are small, that is when $\delta \in[-3,3]$ and $S^{p_{j}}<10$. We delimit the sensitivity measures of $S^{\sigma_{22}}$ and $S^{\sigma_{24}}$ because without this constraint in the plot, we can not see what is happening with small values of the sensitivity measures, that is with $S^{p_{2}}$ and $S^{p_{4}}$.

In this plot, experts can formulate their different values to $\delta$ and observe the associated divergences. If the sensitivity measure is large and the value of $\delta$ is valid, the parameter must be reviewed with new available data or with some other experts' information.

Next, we have implemented an algorithm (see Appendix 2) that will be useful to know which elements of $\mu$ or $\Sigma$ should be reviewed again. The method consists of computing all the sensitivity measures that can influence the target variable $X_{i}$ and comparing their values with a threshold $s$, fixed by the experts. If the sensitivity measure is larger than the threshold $s$, then the parameter should be reviewed.

Before executing the algorithm, it is necessary to prove that the posterior covariance matrix with $\delta$, for every $\delta$ cases associated with inaccuracy in the covariance matrix, is positive definite.

In the algorithm the sensitivity measure is first computed for $\delta$ introduced in the mean vector and later, in the covariance matrix. All the perturbations of the

![img-2.jpeg](img-2.jpeg)

Figure 3. Sensitivity measures when $S^{p j} \leq 10$ and $\delta \in[-3,3]$.
problem are introduced in one step, having a vector with all $\delta$ values to be added to the mean vector and a matrix with all $\delta$ values to be added to the covariance matrix. If a parameter is accurately defined, then the element with this position in the $\delta$ vector or in the $\delta$ matrix will be zero. Likewise, the sensitivity measure is defined with a vector for the sensitivity measures associated with inaccuracy in the mean vector and with a matrix for the sensitivity measures associated with inaccuracy in the covariance matrix. Therefore, if the sensitivity measure is zero, the parameter with that position does not present inaccuracy. To compute any sensitivity value, we work with the parameters of the initial model, the evidence $e$ and the values of $\delta$.

Developing the algorithm with Example 5.1 and introducing a threshold value $s=1$ : first, the sensitivity values related with elements of the mean vector will be computed; later, the sensitivity values related with elements of the covariance matrix will be computed. Finally, all the sensitivity measures are compared with the threshold $s=1$, obtaining "the mean in the position 2 should be reviewed; $S_{-} M[2]=1.6488$ ", that is $S^{\mu_{2}}>1$, thus the parameter $\mu_{2}$ should be studied again.

# 6. Conclusions 

The method developed in this article is useful to compute the sensitivity measure of the elements that characterize the Gaussian Bayesian network, quantifying numerically the inaccuracies presented in the network.

The method is based on perturbing the parameters of the model and, after the evidence propagation, computing the sensitivity measure, given by the KL-divergence between the posterior density of interest computed before and after perturbation. This is a simple method easy to perform a sensitivity analysis in a Gaussian Bayesian network.

We find that only changes relative to the variable of interest and to the evidence variable have influence on the posterior marginal density of the target variable. Then, we described some changes in the mean vector and in the covariance matrix, related to other non evidential variables, that do not affect the result of the posterior marginal density of interest.

Finally, some values of the sensitivity measures are compared. With this aim, we have developed a graphical method and an algorithm. Therefore, we can study which parameter gives the largest sensitivity measure. If the sensitivity measure is large then it is necessary to evaluate again the information about the variable with this parameter, with more available data or with some other experts' information. However, if this measure is small we can conclude that the network is robust and that changes presented do not affect the final result over the variable of interest.

# Appendix 1 

In order to provide a proof of the sensitivity measures in all cases, it is proved (Kullback and Leibler, 1951) that the KL-divergence, when the compared probability densities are Gaussian, is

$$
K L\left(f(w), f^{\prime}(w)\right)=\frac{1}{2}\left[\ln \left(\frac{\sigma^{2 \prime}}{\sigma^{2}}\right)+\frac{\sigma^{2}}{\sigma^{2 \prime}}+\frac{\left(\mu^{\prime}-\mu\right)^{2}}{\sigma^{2 \prime}}-1\right]
$$

with $f(w)$ as $N\left(\mu, \sigma^{2}\right)$ and $f^{\prime}(w)$ as $N\left(\mu^{\prime}, \sigma^{2 \prime}\right)$. Then,

$$
\begin{aligned}
S^{\mu_{i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right) & =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right] \\
S^{\mu_{i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right) & =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right] \\
& =\frac{\delta^{2}}{2 \sigma_{i}^{Y \mid E=e}}
\end{aligned}
$$

with $\mu_{i}^{Y \mid E=e, \delta}=\mu_{i}^{Y \mid E=e}+\delta$ and $\sigma_{i}^{Y \mid E=e, \delta}=\sigma_{i}^{Y \mid E=e}$

$$
(12) S^{\mu_{e}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)=\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right]
$$

with $\mu_{i}^{Y \mid E=e, \delta}=\mu_{i}^{Y \mid E=e}-\frac{\sigma_{i e}}{\sigma_{e e}} \delta$ and $\sigma_{i}^{Y \mid E=e, \delta}=\sigma_{i}^{Y \mid E=e}$

$$
\begin{aligned}
& =\frac{1}{2}\left[\frac{\left(-\frac{\sigma_{i e}}{\sigma_{e e}} \delta\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}\right]=\frac{\delta^{2}}{2 \sigma_{i}^{Y \mid E=e}}\left(\frac{\sigma_{i e}}{\sigma_{e e}}\right)^{2} \\
(14) S^{\sigma_{i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right) & =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right]
\end{aligned}
$$

with $\mu_{i}^{Y \mid E=e, \delta}=\mu_{i}^{Y \mid E=e}$ and

$$
\begin{aligned}
\sigma_{i}^{Y \mid E=e, \delta}=\sigma_{i}^{Y \mid E=e}+\delta & =\frac{1}{2}\left[\ln \left(1+\frac{\delta}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}}{\sigma_{i}^{Y \mid E=e}+\delta}-1\right] \\
& =\frac{1}{2}\left[\ln \left(1+\frac{\delta}{\sigma_{i}^{Y \mid E=e}}\right)-\frac{\delta}{\sigma_{i}^{Y \mid E=e, \delta}}\right]
\end{aligned}
$$

$$
\begin{aligned}
S^{\sigma_{e e}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right) & =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right] \\
& =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\frac{-\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e, \delta}}}\right]
\end{aligned}
$$

with posterior parameters

$$
\begin{aligned}
& \mu_{i}^{Y \mid E=e, \delta}=\mu_{i}+\frac{\sigma_{i e}}{\sigma_{e e}+\delta}(e-\mu e) \\
& \sigma_{i}^{Y \mid E=e, \delta}=\sigma_{i i}-\frac{\sigma_{i e}^{2}}{\sigma_{e e}+\delta}
\end{aligned}
$$

and

$$
\begin{aligned}
\mu_{i}^{Y \mid E=e} & =\mu_{i}+\frac{\sigma_{i e}}{\sigma_{e e}}(e-\mu e) \\
\sigma_{i}^{Y \mid E=e} & =\sigma_{i}-\frac{\sigma_{i e}^{2}}{\sigma_{e e}} \\
& =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{-\frac{\sigma_{i e}^{2}}{\sigma_{e e}}+\frac{\sigma_{i e}^{2}}{\sigma_{e e}+\delta}+\left(\frac{\sigma_{i e}}{\sigma_{e e}+\delta}(e-\mu e)-\frac{\sigma_{i e}}{\sigma_{e e}}(e-\mu e)\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}\right] \\
& =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\frac{\sigma_{i e}^{2}}{\sigma_{e e}}\left(\frac{-\delta}{\sigma_{e e}+\delta}\right)+\left(\sigma_{i e}(e-\mu e)\left(\frac{-\delta}{\left(\sigma_{e e}+\delta\right) \sigma_{e e}}\right)\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}\right] \\
& =\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\frac{\sigma_{i e}^{2}}{\sigma_{e e}}\left(\frac{-\delta}{\sigma_{e e}+\delta}\right)\left(1+\left(e-\mu_{e}\right)^{2}\left(\frac{-\delta}{\left(\sigma_{e e}+\delta\right) \sigma_{e e}}\right)\right)}{\sigma_{i}^{Y \mid E=e, \delta}}\right]
\end{aligned}
$$

(18) $S^{\sigma_{i i}}\left(f\left(x_{i} \mid e\right), f\left(x_{i} \mid e, \delta\right)\right)$

$$
=\frac{1}{2}\left[\ln \left(\frac{\sigma_{i}^{Y \mid E=e, \delta}}{\sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\mu_{i}^{Y \mid E=e, \delta}-\mu_{i}^{Y \mid E=e}\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right]
$$

with $\mu_{i}^{Y \mid E=e, \delta}=\mu_{i}^{Y \mid E=e}+\frac{\delta}{\sigma_{e e}}\left(e-\mu_{e}\right)$ and

$$
\begin{aligned}
\sigma_{i}^{Y \mid E=e, \delta} & =\sigma_{i}^{Y \mid E=e}-\frac{\delta^{2}+2 \sigma_{i i} \delta}{\sigma_{e e}} \\
& =\frac{1}{2}\left[\ln \left(1-\frac{\delta^{2}+2 \sigma_{i i} \delta}{\sigma_{e e} \sigma_{i}^{Y \mid E=e}}\right)+\frac{\sigma_{i}^{Y \mid E=e}+\left(\frac{\delta}{\sigma_{e e}}\left(e-\mu_{e}\right)\right)^{2}}{\sigma_{i}^{Y \mid E=e, \delta}}-1\right]
\end{aligned}
$$

# Appendix 2 

The algorithm that computes the sensitivity measures and determines the parameters in the network is available at the URL: http://www.ucm.es/info/eue/ pagina/APOYO/RosarioSusiGarcia/S_algorithm.pdf

## Acknowledgments

The authors are grateful to the editor and referee for their suggestions that greatly improved the article. This research was supported by the MEC from Spain Grant MTM2005-05462 and Complutense University-Community of Madrid Grant UCM2005-910395.
