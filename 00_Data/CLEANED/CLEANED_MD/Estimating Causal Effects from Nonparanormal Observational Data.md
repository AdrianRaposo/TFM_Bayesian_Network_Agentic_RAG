# Steyed Mahdi Mahmoudi ${ }^{1}$ / Ernst C. Wit ${ }^{2}$ 

## Estimating Causal Effects from Nonparanormal Observational Data

${ }^{1}$ Department of Statistics, Faculty of Mathematics, Statistics and Computer Science, Semnan University, Semnan, Iran, E-mail: mahmoudi@semnan.ac.ir<br>${ }^{2}$ Johann Bernoulli Institute (FWN), Rijksuniversiteit Groningen Faculteit voor Wiskunde en Natuurwetenschappen, Groningen, Netherlands, E-mail: e.c.wit@rug.nl


#### Abstract

: One of the basic aims of science is to unravel the chain of cause and effect of particular systems. Especially for large systems, this can be a daunting task. Detailed interventional and randomized data sampling approaches can be used to resolve the causality question, but for many systems, such interventions are impossible or too costly to obtain. Recently, Maathuis et al. (2010), following ideas from Spirtes et al. (2000), introduced a framework to estimate causal effects in large scale Gaussian systems. By describing the causal network as a directed acyclic graph it is a possible to estimate a class of Markov equivalent systems that describe the underlying causal interactions consistently, even for non-Gaussian systems. In these systems, causal effects stop being linear and cannot be described any more by a single coefficient. In this paper, we derive the general functional form of a causal effect in a large subclass of non-Gaussian distributions, called the non-paranormal. We also derive a convenient approximation, which can be used effectively in estimation. We show that the estimate is consistent under certain conditions and we apply the method to an observational gene expression dataset of the Arabidopsis thaliana circadian clock system.


Keywords: causal effects, directed acyclic graph (DAG), nonparanormal distribution, PC-algorithm, Gaussian copula
DOI: $10.1515 /$ ijb-2018-0030
Received: August 16, 2017; Revised: June 19, 2018; Accepted: July 26, 2018

## 1 Introduction

Inferring cause-and-effect relationships between variables is of primary importance in many fields of science. The classical approach for determining such relationships uses randomized experiments where a single or few variables are perturbed. Such intervention experiments, however, can be very expensive, unethical (e.g. one cannot force a randomly selected person to smoke many cigarettes a day) or even infeasible. Hence, it is desirable to infer causal effects from so-called observational data obtained by observing a system without subjecting it to interventions. Although some important concepts and ideas have been worked out [1-3], estimating causal effects for non-Gaussian observational systems is still in its infancy.

Pearl [4, 5] described a do-calculus of causal effects, if the underlying causal diagram is known. In practice, though, the influence diagram is often not known and one would like to infer causal effects from observational data together with the influence diagram. Spirtes et al. [6] introduced methods to estimate causal graphs from observational data. Verma and Pearl [7] found that typically groups of causal graphs give rise to the same distribution of the data, which implies that the generating causal DAG is typically unidentifiable from the data. This Markov equivalence class of causal DAGs has been called completed partially directed acyclic graph (CPDAG). A CPDAG can be estimated in various ways, including the PC-algorithm [6], search and score methods [7-9] and Bayesian methods $[10,11]$.

The PC-algorithm uses conditional independence tests to infer a CPDAG from data [6]. Sample partial correlations derived from independent multivariate normal observations have favourable distributional properties [12], Chapter 4], which form the basis for the work of [13], who treat the PC-algorithm in the Gaussian context with conditional independence tests based on sample partial correlations. They prove the high-dimensional consistency of the PC-algorithm, when the observations form a sample of independent normal random vectors that are faithful to a suitably sparse DAG. Maathuis et al. [14] propose a method that combines the estimation of the causal structure and the interventional distribution in the Gaussian case. Due to the Gaussian structure, they find that the causal effects can be described by a set of regression coefficients. Harris and Drton

[15] show that the PC-algorithm has high-dimensional consistency properties for a broader class of distributions, when standard Pearson-type empirical correlations are replaced by rank-based measures of correlations in tests of conditional independence, such as Spearman's rank correlation and Kendall's tau. A special class of non-Gaussian distributions is constituted by the Gaussian copula, or, in the terminology of [16], the so-called "nonparanormal distributions." Teramoto et al. [17] uses this class to estimate the underlying causal DAG for the design of efficient intervention experiments. Nandy et al. [18] applied Intervention-calculus when the DAG is Absent (IDA) to nonparanormal distributions, and summarize the causal effects among the underlying Gaussian random variables. What is missing up until now is a way to describe and estimate the causal effects in such nonparanormal scenarios. The main difficulty is that causal effects in non-Gaussian scenarios stop being constant and become functions of the intervention variables.

In the remainder of the paper, we will consider an observational setting of a nonparanormal system. We assume the causal CPDAG has been estimated by, e.g. the Rank PC (RPC) algorithm [15], i.e. the PC-algorithm in the nonparanormal context. Based on the estimated CPDAG, it is our aim to derive an expression for the causal effect in this system and to find a consistent way to estimate them. In Section 2, we introduce the causal graph terminology, a short description of the intervention calculus and the definition of a causal effect. In Section 3, we derive the structure of a causal effect of a nonparanormal causal effect and in Section 4, we define a convenient estimator. In Section 5, we evaluate the performance of our method in a simulation study. Finally, in Section 6, we illustrate the method in a real data example.

# 2 Causal effects in causal graphs 

In this section we describe the background needed in order to define the notion of a causal effect. We begin by defining causal models through directed graphical models.

A graph is a pair $G=(V, E)$, where $V$ is a finite set of vertices $V=\{1,2, \ldots, p\}$, also called nodes, of $G$ and $E$ is a subset of $(V \times V)$ of ordered pairs of vertices, called the edges or links of $G$. We consider $p$ random variables $X_{1}, \ldots, X_{p}$, associated to the vertices. If edge $\left(X_{i}, X_{j}\right) \in E$ but $\left(X_{j}, X_{i}\right) \notin E$, we call the edge directed or an arrow, denoted by $X_{i} \rightarrow X_{j}$. In that case, we also say that $X_{i}$ is a parent of $X_{j}$, and that $X_{j}$ is a child of $X_{i}$. The set of parents of a vertex $X_{j}$ is denoted by $\mathrm{pa}(j)$. We use the short-hand notation $X_{i}-X_{j}$ that is undirected edge to denote $\left(X_{i}, X_{j}\right) \in E$ and $\left(X_{j}, X_{i}\right) \in E$. A graph containing only directed edges $(\rightarrow)$ is directed, one containing only undirected edges $(-)$ is undirected. A directed graph is called a directed acyclic graph (DAG) if it does not contain directed cycles. A DAG of $p$ random variables $X_{1}, \ldots, X_{p}$ can be interpreted as a Markov independence graph, describing a multivariate distribution. Various DAGs can lead to the same distribution. A common tool for describing such Markov equivalence class of DAGs are completed partially directed acyclic graphs (CPDAGs).

Pearl [5] defined causality through intervention, whereby variables are externally manipulated to take certain values. This intervention changes the underlying distribution $P$ and can be expressed by adapting the DAG. The new distribution is called the intervention distribution and we say that the variables, whose structural equations we have replaced have been "intervened on." The intervention distribution of $Y$ when doing an intervention and setting the variable $X_{i}$ to a value $x_{i}^{\prime}$ is denoted by $P\left(Y \mid \operatorname{do}\left(X_{i}=x_{i}^{\prime}\right)\right)$. The intervention on variable $X_{i}$ is characterized by a truncated factorization, in which an intervention DAG $G$, arising from the non-intervention DAG $G$ can be defined by deleting all edges which point into the node $X_{i}$. Consider the example graph below, a DAG $G$ and its corresponding intervention graphs $(G)$ are shown.
![img-0.jpeg](img-0.jpeg)

Figure 1: (a) A DAG $G$ and (b) its corresponding intervention graph $G^{\prime}$. The intervention is do $\left(X_{z}=x\right)$, described by the red label in the graph. The parental set of $i=2$ is $\mathrm{pa}(2)=\{1\}$ which appears in (3) for computing the causal effect $\beta_{2}$ of $X_{2}$ on $Y$.

The total causal effect of $X_{i}$ on $Y$ at $x_{i}$ is the relative amount $Y$ is expected to change as a result from a small interventional change of $X_{i}$ at $x_{i}$,

$$
\operatorname{CE}\left(Y \mid X_{i}=x_{i}\right)=\left.\frac{\partial}{\partial x} E\left[Y \mid \operatorname{do}\left(X_{i}=x\right)\right]\right|_{x=x_{i}}
$$

where we have that if $Y \notin X_{\mathrm{pa}(i)}$,

$$
E\left(Y \mid \operatorname{do}\left(X_{i}=x\right)\right)=\int E\left(Y \mid X_{i}=x, X_{\mathrm{pa}(i)}=x_{\mathrm{pa}(i)}\right) P\left(x_{\mathrm{pa}(i)}\right) d\left(x_{\mathrm{pa}(i)}\right)
$$

If $\left(X_{1}, \ldots, X_{p-1}, Y\right)$ has a multivariate Gaussian distribution, then using the fact that the conditional expectation $E\left(Y \mid X_{i}=x, X_{\mathrm{pa}(i)}=x_{\mathrm{pa}(i)}\right)$ is linear in $x_{i}$ and $x_{\mathrm{pa}(i)}$ if $Y \notin X_{\mathrm{pa}(i)}$, it is straightforward to see that

$$
E\left(Y \mid \operatorname{do}\left(X_{i}=x_{i}\right)\right)=\beta_{i} x_{i}+\int \beta_{\mathrm{pa}(i)}^{T} x_{\mathrm{pa}(i)} P\left(x_{\mathrm{pa}(i)}\right) d\left(x_{\mathrm{pa}(i)}\right)
$$

for some coefficients $\beta_{i}$ and $\beta_{\mathrm{pa}(i)}$. Therefore, the causal effect is given by

$$
\left.\mathrm{CE}\left(Y \mid X_{i}=x_{i}\right)=\frac{\partial}{\partial x} E\left[Y \mid \operatorname{do}\left(X_{i}=x\right)\right]\right|_{x=x_{i}}=\beta_{i}
$$

From eq. (3), it follows that the total causal effect of $X_{i}$ on $Y$ with $Y \notin X_{\mathrm{pa}(i)}$ is given by the regression coefficient of $X_{i}$ in the regression of $Y$ on $X_{i}$ and $\mathrm{pa}(i)$. Note that if $Y \in X_{\mathrm{pa}(i)}$, the total causal effect from $X_{i}$ to $Y$ is, obviously, zero. Our aim is to generalize this to a wider class of distributions.

# 3 Causal effect for nonparanormal graphical models 

Spirtes et al. [6] introduced the PC-algorithm to estimate causal graph from observational data. Kalisch and Bühlmann [13] proved consistency of the PC-algorithm in a Gaussian setting for estimating the causal skeleton and, subsequently, the Markov equivalence class of high-dimensional causal graphs. The algorithm is based on a clever hierarchical scheme for testing conditional independence among pairs of variables $X_{j}, X_{k}$ (for all $j \neq k$ ) in the DAG. In Gaussian models, tests of conditional independence can be based on Pearson correlations and high-dimensional consistency results have been obtained for the PC-algorithm in this setting. Harris and Drton [15] proved high-dimensional consistency properties for a broader class of nonparanormal models when using rank-based measures of correlation. They showed that the Rank PC-algorithm (RPC) works as well as the Pearson PC-algorithm for normal data and considerably better for non-Gaussian data. If one assumes to know all conditional independencies exactly - the oracle setting- then the RPC-algorithm yields the "true" CPDAG, i.e. the Markov equivalence class of DAGs that contains the true causal DAG.

Building on this work in the Gaussian setting, [14] derived an expression for and an estimator of the total causal effect of a covariate $X_{i}$ on a response $Y$ in a Gaussian causal graph. After obtaining the CPDAG Markov equivalence class of, say, $m$ causal DAGs, they apply for each DAG $G_{j}$ in this class the intervention calculus to obtain the total causal effect $\beta_{i j}$ of $X_{i}$ on $Y$. Then they define multi-sets $\Theta_{i}=\left(\beta_{i j}\right)_{j \in\{1, \ldots, m\rangle}$ containing the estimated possible causal effects of $X_{i}$ on $Y$.

In this section, we derive the analogous multi-set of causal effects the nonparanormal setting. In practice, the conditional independences have to be inferred from the data as well and we show how using our main result in combination with the RPC-algorithm we are able to define an convenient estimator for the causal effect for such data, which stops being linear and needs to be estimated functionally.

### 3.1 General expression of nonparanormal causal effect

Liu et al. [16] define the nonparanormal distribution. Let $f=\left\langle f_{i}\right\rangle_{i \in \mathbf{V}}$ be a set of monotone, univariate functions and let $\Sigma \in \mathbb{R}^{\mathbf{V} \times \mathbf{V}}$ be a positive definite covariance matrix. We say a $p$-dimensional random variable $X=\left(X_{1}, \ldots, X_{p}\right)^{\mathrm{T}}$ has a nonparanormal distribution,

$$
X \sim \operatorname{NPN}(\mu, \Sigma, f)
$$

if $f^{-1}(X)=\left\langle f_{1}^{-1}\left(X_{1}\right), \ldots, f_{p}^{-1}\left(X_{p}\right)\right\rangle \sim N(\mu, \Sigma)$. If $X \sim \operatorname{NPN}(\mu, \Sigma, f)$, then the univariate marginal distribution for a coordinate, say $X_{i}$, can have any distribution $F_{i}$, as we can take $f_{i}=F_{i}^{-1} \circ \Phi_{\mu_{i}, \sigma_{i}^{2}}$, where $\Phi_{\mu_{i}, \sigma_{i}^{2}}$ is the normal distribution function with mean $\mu_{i}$ and variance $\sigma_{i}^{2}=\Sigma_{i i}$. Note that, in general, $f_{i}$ need not be continuous. However, in this paper, we deal with monotone and differentiable $f$. Liu et al. [16] show that in that case the nonparanormal distribution $\operatorname{NPN}(\mu, \Sigma, f)$ is a Gaussian copula.

In the remainder of the paper, we assume that $\left(X_{1}, \ldots, X_{p-1}, Y\right) \sim \operatorname{NPN}(0, \Sigma, f)$, where $\Sigma$ is a correlation matrix. We will refer to the latent standard normally distributed variables as $Z_{i}=f_{i}^{-1}\left(X_{i}\right)=\Phi^{-1} \circ F_{i}\left(X_{i}\right)$ and $Z=f_{y}^{-1}(Y)=\Phi^{-1} \circ F_{y}(Y)$. We are interested in the total causal effect of $X_{i}$ on $Y$ for $i \in(1, \ldots, p-1)$. We know from Section 2 that for Gaussian data it is very simple to compute the total causal effect, since Gaussianity implies that $E\left(Y \mid X_{i}=x_{i} ; X_{-i}=x_{-i}\right)$ is linear in $x_{i}$. Unfortunately, this is no longer true for non-Gaussian random variables. In Theorem 1 we derive the explicit functional form for the total causal effect in the entire class of nonparanormal distributions.

# Theorem 1. 

Let $\left(X_{1}, \ldots, X_{p-1}, Y\right) \sim N P N\left(0, \Sigma, f\right)$ and $f_{i}(i=1, \ldots, p-1)$ is differentiable and $f_{y}$ is infinitely differentiable, then the total causal effect of $X_{i}$ on $Y$ in causal graph $G$ is given by

$$
\begin{aligned}
\mathrm{CE}\left(Y \mid X_{i}=x_{i}\right) & =\sum_{k=1}^{\infty} \sum_{r=0}^{\lfloor\frac{k-1}{2}\rfloor} \sum_{s=1}^{k-2 r} f_{y}^{(k)}\left(z_{0}\right) \frac{1}{k!}\left(\frac{k-2 r}{s}\right)\left(\frac{k}{2 r}\right) s \beta_{i} \\
& \times\left(-z_{0}+\beta_{i} z_{i}\right)^{s-1} E\left[\left(\beta_{p a(i)}^{T} Z_{p a(i)}\right)^{k-2 r-s}\right] \\
& \times(2 r+1) \times \ldots \times 3 \times 1 \times\left[\left(1-\rho^{2}\right)\right]^{r}\left(f_{i}^{-1}\right)^{\prime}\left(x_{i}\right)
\end{aligned}
$$

for every $z_{0} \in \mathbb{R}$, where $f_{y}^{(k)}$ is the $k$ th derivative of $f_{y}, z_{i}=f_{i}^{-1}\left(x_{i}\right), Z_{p a(i)}=f_{p a(i)}^{-1}\left(X_{p a(i)}\right),\left(\beta_{i}, \beta_{p a(i)}\right)=$ $\Sigma_{p,(i, p a(i))} \Sigma_{(i, p a(i)),(i, p a(i))}^{-1}$ and $\rho=\left(\beta_{i}, \beta_{p a(i)}\right) \Sigma_{(i, p a(i)), p}$.

The proof of the theorem is given in the appendix. We have obtained the general expression eq. (4) for a nonparanormal causal effect. The value of this theorem is that it gives us insight in how higher order moments of the effect $Y$, captured in the higher order derivatives of $f_{y}$, affect the causal effect, whereas higher order moments of the cause $X_{i}$ do not. In practice, this formula is not very helpful as it contains information about the system that we typically do not possess, such as the correlation structure of the latent normal variable. However, this formula can inspire practical estimation procedures of the causal effects in nonparanormal systems. Whereas this is in principle possible, we restrict our attention in this paper to a lower order Taylor approximations. A first and second order Taylor expansion are given by

$$
\begin{aligned}
& C E_{1, z_{0}}\left(Y \mid X_{i}=x_{i}\right)=f_{y}^{\prime}\left(z_{0}\right) \beta_{i}\left(f_{i}^{-1}\right)^{\prime}\left(x_{i}\right) \\
& C E_{2, z_{0}}\left(Y \mid X_{i}=x_{i}\right)=\left[f_{y}^{\prime}\left(z_{0}\right) \beta_{i}+f_{y}^{\prime \prime}\left(z_{0}\right) \beta_{i}\left(\beta_{i} z_{i}-z_{0}\right)\right] \times\left(f_{i}^{-1}\right)^{\prime}\left(x_{i}\right)
\end{aligned}
$$

If median and mode of $Y$ coincide, then it is easy to show that the second order Taylor expansion collapses to the first order by taking $z_{0}=0$, i.e. $C E_{2,0}\left(Y \mid X_{i}=x_{i}\right)=\left(F^{-1}\right)^{\prime}(0.5) \beta_{i}\left(f_{i}^{-1}\right)^{\prime}\left(x_{i}\right)$. Higher order expansions become quickly more intricate. Moreover, especially when it comes to estimation in Section 4, the estimates involved in lower order expansions tend to be intrinsically more stable.

### 3.2 Special case

We consider the special case of the above theorem for the situation that only $Y$ is normally distributed, and the $X_{i} \mathrm{~s}$ are still nonparanormal.

## Corollary 1.

Let $\left(X_{1}, \ldots, X_{p-1}\right) \sim N P N(0, \Sigma, f)$ and $f_{i}(i=1, \ldots, p-1)$ is differentiable and $Y \sim N\left(\mu, \sigma^{2}\right)$, then the total causal effect of $X_{i}$ on $Y$ in causal graph $G$ is given by

$$
\mathrm{CE}\left(Y \mid X_{i}=x_{i}\right)=\sigma \beta_{i}\left(f_{i}^{-1}\right)^{\prime}\left(x_{i}\right)
$$

where $\beta_{i}$ is defined as in Theorem 1.
The result simply follows from $f_{y}(Z)=\mu+\sigma Z$ for $Z$ standard normal. This special case both inspires an estimator for the causal effect and gives some hope for obtaining some consistency results.

## 4 NCE: Nonparanormal causal effect estimator

In this section, we propose a simple estimator for the causal effect that is able to capture non-linear effects for a wide-ranging collection of distributions. Furthermore, we show that under some conditions, this estimator is consistent.

# 4.1 First order estimator 

![img-1.jpeg](img-1.jpeg)

Figure 2: (a) the derivative of monotone increasing spline $\overline{F_{Y, \text { sm }}}$ for estimate $\frac{\partial}{\partial x} F_{Y}^{-1}$. (b) the derivative of the monotone increasing estimating spline $\tilde{F}_{i, \text { sm }}$ for estimate $\frac{\partial}{\partial x} F_{i}$.

In Section 3.2, we derived a one-term expression that is used as inspiration for a first-order Taylor estimator of the general causal effect of $X_{i}=x$ on $Y$, i.e.,

$$
\widehat{\mathrm{NCE}}_{z_{0}}(x)=\hat{f}_{y}^{\prime}\left(z_{0}\right) \hat{\beta}_{i}\left(\widehat{f_{i}^{-1}}\right)^{\prime}(x)
$$

for some $z_{0}, x \in \mathbb{R}$ and where $\hat{\beta}_{i}$ is the linear regression coefficient of $\widehat{f_{y}^{-1}}(Y)$ on $\widehat{f_{i}^{-1}}\left(X_{i}\right)$, while controlling for the parents $f_{\mathrm{pa}(i)}^{-1}\left(X_{\mathrm{pa}(i)}\right)$ of $i$, given some estimators for the various functions $f^{-1}$ and $f_{y}$. We will show in the next section that in order to obtain consistency, we trim the data for each variable below its $\alpha / p$ and above $1-\alpha / p$ quantiles, where $p$ is the number of random variables $(X, Y)$. When an observation has been trimmed for one variable, it is removed in its entirety for all variables. This means that in the worst case scenario, $1-2 \alpha$ of the observations remain. In practice, we will often use $\alpha=0.05$.

We can simplify expression eq. (6) by considering the case that $z_{0}=0$. Note that it is straightforward to obtain

$$
\begin{aligned}
f_{y}^{\prime}(0) & =\left.\frac{\partial}{\partial u} F_{Y}^{-1}(u)\right|_{u=0.5} \phi(0) \\
\left(f_{i}^{-1}\right)^{\prime}(x) & =\left[\phi\left(f_{i}^{-1}(x)\right)\right]^{-1} \frac{\partial}{\partial x} F_{i}(x)
\end{aligned}
$$

where $\varphi$ is the density function of a standard normal distribution. Considering Figure 2, $F_{Y}^{-1}$ will be estimated via a monotone increasing smoother $\overline{F_{Y, \text { sm }}^{-1}}$, which gives us direct access to its derivative. Similarly, $\frac{\partial}{\partial x} F_{i}$ will be estimated by taking the derivative of the monotone increasing estimating smoother $\tilde{F}_{i, \text { sm }}$. Finally, $\hat{f}_{i}^{-1}(x)$ will be estimated as $\hat{z}=\Phi^{-1}\left(\tilde{F}_{i, \operatorname{sm}}(x)\right)$. Putting this together, we obtain a simplified and explicit estimator of a non-paranormal causal effect,

$$
\widehat{\mathrm{NCE}}_{0}(x)=\hat{\beta}_{i} \frac{\phi(0)}{\phi(\hat{z})} \frac{\partial F_{Y, \text { sm }}^{-1}}{\partial u}(0.5) \frac{\partial \tilde{F}_{i, \text { sm }}}{\partial x}(x)
$$

In the following section, we will show that under certain conditions the above estimator is consistent. In particular, we show that estimating $F_{Y}^{-1}$ and $F_{i}$ with a particular kind of kernel smoother works. Nevertheless, in practice any slightly stiff smoother will result in almost the same estimates. A natural cubic spline is easy to implement and can be easily differentiated, which is needed for the causal effect estimator $\widehat{\mathrm{NCE}}_{0}(x)$.

### 4.2 Consistency

In this section we will be concerned with the asymptotic behaviour of our estimator in eq. (7) under the assumption of normality of $Y$, but no such assumption on the $X_{i}$. We first show that the random, but not necessarily independent, sampling scheme of $\left(X_{1}, \ldots, X_{p-1}\right) \sim N P N(0, \Sigma, f)$ and $Y \sim N\left(\mu, \sigma^{2}\right)$ combined with our lower and upper $\alpha / p$ trimming scheme will eventually fill up the $p$-dimensional cube $\left[L_{\alpha}, U_{\alpha}\right]$, where $L_{\alpha}=\left(L_{\alpha}^{1}, \ldots, L_{\alpha}^{p-1}, L_{\alpha}^{p}\right)$ and $U_{\alpha}=\left(U_{\alpha}^{1}, \ldots, U_{\alpha}^{p-1}, U_{\alpha}^{p}\right)$ are the $\alpha$ - and $(1-\alpha)$-quantiles, respectively, for each of the variables $\left(X_{1}, \ldots, X_{p-1}, Y\right)$. From the original sample size $n$ approximately $(1-2 \alpha) n$ will fall in this cube.

Then we show that the kernel estimators of the functions used in the NCE estimators and their derivatives converge fast to their true values in probability. Together with the fact that products of consistent estimators are consistent, this proves the consistency of the estimator $\widetilde{\mathrm{NCE}}_{0}(x)$.

# Proposition 1. 

Consider any absolutely continuous random variableXwith loweraquantile $L_{\alpha}$ and upperaquantile $U_{\alpha}$. For the $N \asymp(1-$ $2 \alpha)$ nordered observations of Xin the finite interval $\left[L_{\alpha}, U_{\alpha}\right]$, the following property holds

$$
\max _{z \leq i \leq N}\left|X_{(i)}-X_{(i-1)}\right|=O_{P}(1 / N)
$$

The symbol $=$ denotes that two sequences of real numbers are asymptotically of the same order. The proof of this Proposition is a simple exercise and will not be given here.

Our goal is first to estimate the function $F_{i}$ and its derivative $\frac{\partial}{\partial x} F_{i}$. Similarly, we aim to estimate $F_{i}^{-1}$ and its derivative. In order to derive asymptotic properties, we will be using kernel estimators for $\hat{F}_{i, \text { sm }}$ and $\widehat{F_{i, \text { sm }}}^{(1)}(x)$, respectively,

$$
\begin{gathered}
\hat{F}_{i, n}(x)=\sum_{j=2}^{N}\left(x_{i(j)}-x_{i(j-1)}\right) \frac{1}{b_{n}} K\left(\frac{x-x_{i(j)}}{b_{n}}\right)\left(\alpha+\frac{j-1}{n}\right) \\
\widehat{F_{i, n}^{-1}}(u)=\sum_{j=1}^{N} \frac{1-2 \alpha}{N} \frac{1}{b_{n}} K\left(\frac{u-\left(\alpha+\frac{j(1-2 \alpha)}{N}\right)}{b_{n}}\right) x_{i(j)}
\end{gathered}
$$

for $x \in\left[L_{\alpha}^{i}, U_{\alpha}^{i}\right]$ and $u \in[\alpha, 1-\alpha]$, where $K$ is a kernel function, [19], $b_{n}<0$ denotes the bandwidth that we take to depend on the sample size $n$ in such a way that $b_{n} \rightarrow 0$ as $n \rightarrow \infty$ and $x_{i(1)}, x_{i(2)}, \ldots, x_{i(N)}$ denote the order statistics of that part that for the $i$ variable that falls within $\left[L_{\alpha}^{i}, U_{\alpha}^{i}\right]$. Note that we have selected the same bandwidth for the quantile function and the CDF, even though they could live on completely different domains. In practice, it may be sensible to scale the bandwidth by some constant depending on the domain. However, for proving consistency we do not need it. We define an estimator of $\frac{\partial}{\partial x} F_{i}$ by taking the derivative of the kernel smoother $\frac{\partial}{\partial x} \overline{F_{i, n}}=\frac{\partial}{\partial x} \hat{F}_{i, n}=\hat{F}_{i, n}^{\prime}$.

## Proposition 2.

If the kernel $K$ is symmetric and twice continuously differentiable with support in $[-1,1]$ and if it satisfies the integrability conditions (a) $\int_{-1}^{1} K(u) \mathrm{d} u=1$ and (b) $\int_{-1}^{1} u^{\mathrm{t}} K(u) \mathrm{d} u=0$ for $\ell=1, \ldots, \gamma-1$, then for a fixed number $\delta$, such that $\alpha<\delta<1 / 2$ :
(i) if $F$ and $F^{-1}$ are $\gamma \geq 1$ times continuously differentiable and $b_{n} \rightarrow 0$ as $n \rightarrow \infty$, then

$$
\begin{aligned}
\sup _{x \in\left[L_{\alpha}^{i}, U_{\alpha}^{i}\right]}\left|\hat{F}_{i, n}(x)-F_{i}(x)\right| & =\mathrm{O}_{P}\left(b_{n}^{\gamma}+\frac{1}{n b_{n}^{\delta}}+\sqrt{\frac{\log n}{n b_{n}}}\right) \\
\sup _{u \in[\delta, 1-\delta]}\left|\widehat{F_{i, n}^{-1}}(u)-F_{i}^{-1}(u)\right| & =\mathrm{O}_{P}\left(b_{n}^{\gamma}+\frac{1}{n b_{n}^{\delta}}+\sqrt{\frac{\log n}{n b_{n}}}\right)
\end{aligned}
$$

(ii) If $F$ and $F^{-1}$ are $\gamma \geq 2$ times continuously differentiable and $b_{n} \rightarrow 0$ as $n \rightarrow \infty$, then

$$
\begin{aligned}
\sup _{x \in\left[L_{\alpha}^{i}, U_{\alpha}^{i}\right]}\left|\hat{F}_{i, n}^{\prime}(x)-F_{i}^{\prime}(x)\right| & =\mathrm{O}_{P}\left(b_{n}^{\gamma-1}+\frac{1}{n b_{n}^{\delta}}+\sqrt{\frac{\log n}{n b_{n}^{\delta}}}\right) \\
\sup _{u \in[\delta, 1-\delta]}\left|\widehat{F_{i, n}^{-1}}(u)-F_{i}^{-1^{\prime}}(u)\right| & =\mathrm{O}_{P}\left(b_{n}^{\gamma-1}+\frac{1}{n b_{n}^{\delta}}+\sqrt{\frac{\log n}{n b_{n}^{\delta}}}\right)
\end{aligned}
$$

In particular, $\hat{F}_{i, n}(x)$ and $\hat{F}_{i, n}^{\prime}(x)$ are consistent on $\left[L_{\alpha}^{i}, U_{\alpha}^{i}\right]$ and $\overline{F_{i, n}^{-1}}(x)$ and $\overline{F_{i, n}^{-1}}(x)$ are consistent on $[\delta, 1-\delta]$, if $n b_{n}^{\delta} / \log n \rightarrow \infty$ holds additionally.

The proof is given in [20], Proposition 3.1]. The estimator $\widehat{\mathrm{NCE}}_{0}(x)$ in eq. (7) contains four terms. Based on Proposition 2 the two terms $\hat{F}_{i, n}^{\prime}(x)$ and $\widehat{F_{i, n}^{-1}}^{\prime}(x)$ are consistent. As any continuous function of a consistent estimator is consistent [21], also $\hat{z}=\Phi^{-1}\left(\hat{F}_{i, \mathrm{n}}(x)\right)$ is consistent. In order to proof consistency of $\widehat{\mathrm{NCE}}_{0}(x)$ we still need to show that $\hat{\beta}_{i}$ is consistent, where $\hat{\beta}_{i}$ is the linear regression coefficient of $\widehat{f_{y}^{-1}}(Y)$ on $\widehat{f_{i}^{-1}}\left(X_{i}\right)$, while controlling for the parents $f_{\mathrm{pa}(i)}^{-1}\left(X_{\mathrm{pa}(i)}\right)$ of $i$. The following proposition shows the consistency of $\hat{\beta}_{i}$.

# Proposition 3. 

Let $\hat{\beta}_{i}$ be the linear regression coefficient of $\widehat{f_{y}^{-1}}(Y)$ on $\widehat{f_{i}^{-1}}\left(X_{i}\right)$, while controlling for the parents $f_{\mathrm{pa}(i)}^{-1}\left(X_{p a(i)}\right)$ of $i$, then

$$
\hat{\beta}_{i}^{n} \xrightarrow{p} \beta_{i}
$$

where $\beta_{i}$ is the true regression coefficient as defined in Theorem 1.
The formal proof is given in the appendix and is again based on the fact that $\widehat{f_{y}^{-1}}(Y), \widehat{f_{i}^{-1}}\left(X_{i}\right)$ and $f_{\mathrm{pa}(i)}^{-1}\left(X_{\mathrm{pa}(i)}\right)$ are consistent estimators and $\hat{\beta}_{i}^{n}$ is a continuous function of these consistent estimators and, therefore, consistent. Putting the previous results together we can now show that our estimator $\widehat{\mathrm{NCE}}_{0}(x)$ in eq. (7) is consistent. The proof is given in the appendix.

## Proposition 4.

Consider the estimator of $\mathrm{NCE}_{0}(x)$ in eq. (7), for which we consider the component estimators eqs (8), (9) and (10). For the kernel estimators, we assume that the conditions of Proposition 2 are satisfied and, furthermore, the bandwidth $b_{n} \rightarrow 0$, but not too fast so that $n b_{n}^{3} / \log n \rightarrow \infty$. Then we have

$$
\widehat{\mathrm{NCE}}_{0, n} \xrightarrow{\mathrm{P}} \mathrm{NCE}_{0}
$$

## 5 Simulation studies

In this section, we test our NCE estimation method for two different types of distributions, to wit, Gaussian and standard Cauchy. For Gaussian data, the method should find constant causal effects and can be compared directly with the IDA method [14]. We consider two scenarios: (i) in which the underlying causal graph is known and (ii) where it is unknown and needs to be estimated via the RPC-algorithm. Secondly, we show how our NCE method captures the non-linear nature of causal effects for a bivariate exponential system. Finally, we compare the NCE causal graph reconstruction method, based on the RPC algorithm, with the nonparanormal (NPN) method by [17] in a system with Cauchy distributed data.

### 5.1 Gaussian data

Following [13], we simulate random DAGs and sample from probability distributions faithful to them. For convenience, we fix an increasing ordering of the variables $\left(X_{1}, \ldots, X_{p}\right)$, meaning that for a vector of independent Gaussian variables $\varepsilon=\left(\varepsilon_{1}, \ldots, \varepsilon_{p}\right)$

$$
X=B X+\varepsilon
$$

where the lower diagonal coefficient matrix $B$ has entries $\beta_{i j}$ that are zero for $i<j$ and $\beta_{j i} \neq 0$ if the corresponding DAG has a directed edge from node $i$ to node $j$ for some $i>j$. The entries $\beta_{i j}$ are by definition the causal effects of $X_{j}$ on $X_{i}$. We create a DAG $G$ with an expected vertex degree of three by drawing edges $(i, j)$ for $i>j$ independently with probability $3 / p$. The nonzero entries of $B$ are drawn from independent standard normal distributions. Then, with probability one, the vector $X$ solving eq. (11) is Markov and faithful with respect to $G$. We consider two different size graphs: a small graph with $p=10$ vertices and a larger graph with $p=50$ vertices. For each $n \in\{100,1000\}$ and each of the two types of graphs, we repeat the simulation 100 times.

### 5.1.1 Causal DAG known

If we assume that the causal DAG is known, then for estimating the causal effects we apply both our NCE algorithm, described in Section 4 and the IDA algorithm by [14], which estimates $\beta_{i j}$ via least squares linear

regression,

$$
x_{t}=\beta_{t 0}+\beta_{t j} x_{j}+\beta_{t, \mathrm{pa}(j)} x_{\mathrm{pa}(j)}
$$

Given that the IDA algorithm is made for these Gaussian data, the method should outperform the NCE method, which is agnostic about the underlying distributional assumptions. We apply the methods to the four data scenarios and the results are presented in the last column of Table 1 as mean absolute deviations. The mean absolute deviation is a robust version of the mean squared error and smaller values refer to better estimates of the causal effects. Table 1 shows that when the number of observations are increasing, the mean absolute deviation for causal effect estimates for both IDA and NCE methods is decreasing. Furthermore, the NCE method, as expected, is somewhat more variable. This variation is mostly the result from the poorer estimates of the distributional shape in the tails of the distribution.

# 5.1.2 Causal DAG unknown 

If the underlying causal DAG is considered unknown, then the CPDAG and associated DAGs need to be estimated. For each simulation, we run both the standard PC-algorithm and the robust RPC-algorithm on a grid of significance levels $\alpha$ ranging from $10^{-10}$ to 0.5 . For each estimated DAG, we compute the causal effects of each node according to the NCE method and the compare the results with the IDA method.
![img-2.jpeg](img-2.jpeg)

Figure 3: Simulation study for Gaussian data from a causal graph ( $p=10$ vertices with $n=100$ observations). The red lines are the true (constant) causal effects. The blue lines are the causal effect estimates from the IDA methods and black lines show the functional causal effect estimates from our NCE method. The dashed lines show the confidence intervals for functional NCE causal effect estimates.

Figure 3 show the causal effects between the chosen nodes for small graph on ten vertices $p=10$ with $n=100$. In these figures the red line show the real causal effect between two chosen nodes. The blue line shows the average estimated causal effect from the IDA method. The black line show the average functional causal effect estimate eq. (7) proposed by our NCE method across the DAGs consistent with the inferred CPDAG. The dashed lines express the average standard deviation of our functional causal effect estimate. A clear message emerges from plots: whereas the IDA method is exactly matched for this simulation scenario, our nonparanormal causal effects estimates are quite stable. Moreover, the confidence intervals calculated by our method typically contain the true effect.

In Table 1 provide numerical comparisons of both methods on data sets with different transformations, where we repeat the experiments 100 times and report the mean absolute deviation for causal effect estimates on each pair nodes in both IDA and NCE methods. Even though the simulation method is precisely suited for the IDA method, our NCE method is highly competitive.

Table 1: Comparison of mean absolute deviations (smaller is better) for causal effect estimates between our NCE and IDA [14] methods for small graphs $(p=10)$ and large graphs $(p=50)$ when the data is Gaussian.



# 5.2 Exponential data 

Only in a few special non-Gaussian distributional examples can we calculate the causal effects exactly. This makes large scale simulation studies difficult. Therefore, in this section we consider the causal effects in a bivariate exponential distribution. We assume only two nodes with exponential marginal distributions and then apply [22] to find the closed form for conditional expectation formula for Gaussian copula. We derive the causal effect for the bivariate Gaussian copula. If we have a bivariate Gaussian copula, with dependence parameter $\rho$, we have

$$
E(Y \mid X=x)=\int_{\mathbb{R}} y \frac{\partial}{\partial y} \Phi\left(\frac{\Phi^{-1}(F(y))-\rho \Phi^{-1}(G(x))}{\sqrt{1-\rho^{2}}}\right) d y
$$

If both marginal distributions $F$ and $G$ were $N(0,1)$, the copula would revert back to the bivariate normal distribution. The Gaussian copula, however, gives us more flexibility, as it can accommodate any type of univariate distributions, $F$ and $G$. In eq. (12), we choose two marginal distributions that are exponential with parameter $\lambda_{x}, \lambda_{y}>0$. Thus, eq. (12) reduces to

$$
\begin{aligned}
& E(Y \mid X=x) \quad=\frac{1}{\sqrt{1-\rho^{2}}} \\
& \int_{\mathbb{R}} y \phi\left(\frac{\Phi^{-1}\left(1-\exp \left(-\lambda_{y} y\right)\right)-\rho \Phi^{-1}\left(1-\exp \left(-\lambda_{x} x\right)\right)}{\sqrt{1-\rho^{2}}}\right) \\
& \times \frac{\lambda_{y} \exp \left(-\lambda_{y} y\right)}{\phi\left(\Phi^{-1}\left(1-\exp \left(-\lambda_{y} y\right)\right)\right)} d y
\end{aligned}
$$

where $\varphi(x)=\Phi(x)$ is the standard normal density. Therefore, for a bivariate nonparanormal with exponential marginals, we obtain the following causal effect,

$$
\begin{gathered}
\mathrm{CE}(Y \mid X=x)=-\frac{\rho}{1-\rho^{2}} \int_{\mathbb{R}} y \phi^{\prime}(t) \frac{\lambda_{x} \exp \left(-\lambda_{x} x\right)}{\phi\left(\Phi^{-1}\left(1-\exp \left(-\lambda_{x} x\right)\right)\right)} \\
\times \frac{\lambda_{y} \exp \left(-\lambda_{y} y\right)}{\phi\left(\Phi^{-1}\left(1-\exp \left(-\lambda_{y} y\right)\right)\right)} d y
\end{gathered}
$$

where $t=\frac{\Phi^{-1}\left(1-\exp \left(-\lambda_{y} y\right)\right)-\rho \Phi^{-1}\left(1-\exp \left(-\lambda_{x} x\right)\right)}{\sqrt{1-\rho^{2}}}$.
In the simulation study we assume that node $X$ affects node $Y$, in the following fashion,

$$
\begin{aligned}
& X \quad=F^{-1}\left(\Phi\left(Z_{1}\right)\right) \\
& Y \quad=F^{-1}\left(\Phi\left(\frac{Z_{1}+Z_{2}}{\sqrt{2}}\right)\right)
\end{aligned}
$$

where $F$ is the CDF of an Exponential(1) distribution and $Z_{1}, Z_{2} \quad$ i.t.d. $N(0,1)$. This falls under the usual nonparanormal scenario. The explicit expression for the causal effect in Theorem 1 is very involved, but we derived in eq. (14) a simplified expression. We evaluated this expression numerically to obtain the true causal effect, expressed as the solid black line in Figure 4. Then we simulated $n=1,000$ observations from the above model for inferring the causal effect.

We assume that the underlying causal graph, $X \rightarrow Y$, is known and used the NCE method to infer the non-linear causal effect. The blue line Figure 5.2 shows the functional causal effect estimate from NCE method. It matches very well the true causal effect. Clearly, had IDA been applied in this scenario, it would have come up with a nonsensical constant causal effect.

![img-3.jpeg](img-3.jpeg)

Figure 4: Exponential nonparanormal simulation: black line shows the true causal effect and the blue line represents the causal effect estimated by our NCE method.

# 5.3 Cauchy data 

Although not the primary aim of our NCE method, it also consists of the RPC causal graph reconstruction method and can therefore be compared to the NPN method by [17]. We evaluated the performance of our NCE and the NPN methods for two different graph sizes: with 20 vertices and 200 vertices. We repeated this experiment 50 times for $n \in[10,100]$.

We consider distributional systems whereby the underlying marginal distributions are mixtures of normal and Cauchy distributions. The mixing rate indicates the percentage of samples whose error distribution was drawn from the standard Cauchy distribution. We chose mixing rate $0.1,0.5$ and 1 . The higher the mixing rate, the less accurate is the Gaussianity assumption. We averaged the values of true positive rate (TPR), false positive rate (FPR), true discovery rate (TDR) in the reconstruction of the causal graph. To compare NCE method with NPN method, we show the representative results of setting for $\alpha=10^{-4}$ in Table 2. It is clear that the NCE method, with its underlying RPC causal reconstruction method, always outperforms the NPN method.

Table 2: Mean true positive, false positive and true discovery rates for the comparison of our NCE and NPN [17] methods for small graph $(p=20)$ and large graph $(p=200)$ when the data is Cauchy.


## 6 TiMet: Circadian regulation in Arabidopsis Thaliana

In this section, we illustrate our proposed approach by applying it to a time course gene expression dataset related to the study of circadian regulation in plants. The data used in our study come from the EU project TiMet (FP7-245143, 2014), whose objective is the elucidation of the interaction between circadian regulation and metabolism in plants.

![img-4.jpeg](img-4.jpeg)

Figure 5: The inferred causal network among the circadian clock genes for Arabidopsis thaliana. The representation is inspired by Figure 1 in [29], showing significant overlap in topology.

The data consist of transcription profiles for the core clock genes from the leaves of various genetic variants of Arabidopsis Thaliana. The transcription profiles of the core clock genes [23-25] were recorded: LHY, CCA1, PRR3, NI (PRR5), PRR9, TOC1, ELF3, ELF4 and GI. The plants were grown in the following 3 light conditions: a diurnal cycle with 12 hour light and 12 hour darkness (12L/12D), an extended night with full darkness for 24 hours, and an extended light with constant light for 24 hours. An exception is the ELF3 mutant, which was grown only in 12L/12D condition. Samples were taken every 2 hours to measure mRNA concentrations. We consider the same group of nine genes, which from previous studies are known to be involved in circadian regulation [26-29]. They consist of two groups of genes: "Morning genes", which are LHY, CCA1, PRR9, and PRR5, whose expression peaks in the morning, and "Evening genes", including TOC1, ELF4, ELF3, GI, and PRR3, whose expression peaks in the evening. The expressions for all the genes are strictly positive and highly right-skewed.

In traditional analysis of microarray studies, data are typically log-transformed. Especially when using the data for prediction, such transformations are sensible as they typically stabilize variances and make downstream analyses more robust. In our case, however, our aim is to describe the system. We are not interested in the causal effect of the log-transformed variables, but we are interested in the causal effects of the original variables. For this reason, we consider the raw data directly, since this is the scale on which we would like to evaluate the system.

For inferring the underlying causal CPDAG, we considered the RPC-algorithm in the version that uses the Kendall's tau - results using Spearman's rho were almost the same. The CPDAG contains three Markov equivalence DAGs. One of these three causal networks among the genes is displayed in Figure 5. For all three causal DAGs, we infer the causal effects between the genes and these are shown as lines in Figure 6. A striking feature is that most of the causal effects shrink towards zero for large values of the cause, possibly indicating saturation. Moreover, this effect seems stronger for the morning genes on the evening genes than vice versa.

The morning gene CCA1 was found to repress the evening genes EFL3 and NI. Among the evening genes, EFL4 and TOC1 have the strongest effect on both other evening and morning genes. The evening gene ELF positively affects CCA1. It also has a negative effect on LHY. Moreover, the evening genes ELF3, GI and TOC1 are involved in the activation of the morning gene PRR. The morning gene LHY has an almost constant effect on the evening genes ELF4, TOC1 and EFL4. In particular ELF4 interacts positively with NI and CCA1 and negatively with LHY. Many of these results are consistent with the findings in [26, 27], [23] and references therein.

Furthermore, we compare our network with the biological network referred to in [29], which is based on the work of [30] and [31]. The most striking difference is that we have found evidence that the GI and ELF3 genes interact directly with the Pseudo-Response Regulators (PRR9 and PRR5 module). Chow et al. [32] suggest that this may be explained by the fact that another protein, LUX, which is not considered in this study, creates a complex with ELF3 that is required to regulate PRR9. This is an interesting methodological issue: studies based on lab-based pairwise interaction studies or studies looking for structural evidence of binding between proteins will not find links between proteins that are not directly interacting, whereas studies such as ours that perform network based analysis on a limited number of proteins will typically infer links between proteins that in reality require an intermediary not considered in the study.

![img-5.jpeg](img-5.jpeg)

Figure 6: Causal effects for the circadian gene interaction network in Arabidopsis thaliana. Whereas ELF3 and ELF4 have almost constant causal effects, most of the others have a distinctive shrinkage in their causal effects for larger values of the cause, indicating saturation.

# 7 Conclusion 

In this paper, we have derived an explicit formula for causal effects in a flexible class of distributions, the so-called nonparanormal. These distributions are especially useful for real-life observational studies, where normality assumptions are often not warranted. We presented a simple method, NCE, to estimate these causal effects nonparametrically, based on a first order approximation of the general causal effect formula. It is able to capture a large range of non-linear causal effects and is shown to be consistent under certain conditions. In a simulation study, we have shown that the estimation method works well, particularly away from the tails of the data. We have also applied the method to an Arabidopsis Thaliana circadian clock network. The estimated causal effects reveal a tendency for some of the causal effects to shrink to zero for large values of the cause, which means that gene regulation shows effect saturation for high levels of the regulator. This is in correspondence with simple Michaelis-Menten kinetic models, often used to model gene regulation.

## Funding

This work was supported by The European Cooperation in Science and Technology, Funder Id: 10.13039/501100000921,Grant Number: CA15109

## Appendix: Proofs

## Proof of Theorem 1

## Proof 1

We follow three steps for proving this theorem. First, we find a closed form expression for $E\left[Y \mid X_{i}=x_{i} ; X_{\text {pa }(i)}=x_{\text {pa }(i)}\right]$. After that we connect this to the do-operator as is done in eq. (2). Finally, taking the derivative in the way that the total causal effect is defined in eq. (1) will complete the proof. From the differentiability of $f_{i}$ it follows that the marginal distributions $F_{i}$ are one-to-one, where $f_{i}^{-1}\left(x_{i}\right)=z_{i}$ and $Z_{i}=f_{i}^{-1}\left(X_{i}\right)=\Phi^{-1} \circ F_{i}\left(X_{i}\right)$ and $Z=f_{y}^{-1}(Y)=\Phi^{-1} \circ F_{y}(Y)$. Using the Taylor expansion,

$$
\begin{aligned}
E\left[Y \mid X_{i}=x_{i} ; X_{\operatorname{pa}(i)}=x_{\operatorname{pa}(i)}\right] \quad & =E\left(F_{y}^{-1}(\Phi(Z)) \mid X_{i}=x_{i} ; X_{\operatorname{pa}(i)}=x_{\operatorname{pa}(i)}\right) \\
& =E\left(F_{y}^{-1}(\Phi(Z)) \mid Z_{i}=z_{i} ; Z_{\operatorname{pa}(i)}=z_{\operatorname{pa}(i)}\right) \\
& =E\left(f_{y}(Z) \mid Z_{i}=z_{i} ; Z_{\operatorname{pa}(i)}=z_{\operatorname{pa}(i)}\right) \\
= & E\left(\sum_{k=1}^{\infty} f_{y}^{(k)}\left(z_{0}\right) \frac{\left(Z-z_{k}\right)^{k}}{k!} \mid Z_{i}=z_{i} ; Z_{\operatorname{pa}(i)}=z_{\operatorname{pa}(i)}\right) \\
= & \sum_{k=1}^{\infty} f_{y}^{(k)}\left(z_{0}\right) \frac{1}{k!} E\left(Z^{* k} \mid Z_{i}=z_{i} ; Z_{\operatorname{pa}(i)}=z_{\operatorname{pa}(i)}\right)
\end{aligned}
$$

where $Z^{*}=Z-z_{0}$ for any $z_{0} \in \mathbb{R}$. From the conditional normal distribution, we know that

$$
Z^{*} \mid Z_{i}=z_{i} ; Z_{\mathrm{pa}(i)}=z_{\mathrm{pa}(i)} \sim N\left(-z_{0}+\left(\beta_{i}, \beta_{\mathrm{pa}(i)}\right)\left(z_{i}, z_{\mathrm{pa}(i)}\right)^{T},\left(1-\rho^{2}\right)\right)
$$

where $\left(\beta_{i}, \beta_{\mathrm{pa}(i)}\right)=\Sigma_{p,(i, \mathrm{pa}(i))} \Sigma_{(i, \mathrm{pa}(i)),(i, \mathrm{pa}(i))}^{-1}$ and $\rho=\Sigma_{p,(i, \mathrm{pa}(i))} \Sigma_{(i, \mathrm{pa}(i)),(i, \mathrm{pa}(i))}^{-1} \Sigma_{(i, \mathrm{pa}(i)), p}$.
Following [33] page 132, we get for $k \in \mathbb{N}$

$$
\begin{aligned}
E\left(Z^{* k} \mid Z_{i}=z_{i} ; Z_{\mathrm{pa}(i)}=z_{\mathrm{pa}(i)}\right)=\sum_{r=0}^{\left\lfloor\frac{k}{2}\right\rfloor}\left(\frac{k}{2 r}\right)\left(-z_{0}+\beta_{i} z_{i}+\beta_{\mathrm{pa}(i)}^{T} z_{\mathrm{pa}(i)}\right)^{k-2 r} \\
\times(2 r-1) \ldots 3 \times 1 \times\left[\left(1-\rho^{2}\right)\right]^{r}
\end{aligned}
$$

Plugging eqs (16) into (15), we have

$$
\begin{aligned}
E\left(Y \mid X_{i}=x_{i} ; X_{\mathrm{pa}(i)}=x_{\mathrm{pa}(i)}\right) & =\sum_{k=1}^{\infty} \sum_{r=0}^{\left\lfloor\frac{k}{2}\right\rfloor} f_{y}^{(k)}\left(z_{0}\right) \frac{1}{k!}\left(\frac{k}{2 r}\right) \\
& \times\left(-z_{0}+\beta_{i} z_{i}+\beta_{\mathrm{pa}(i)}^{T} z_{\mathrm{pa}(i)}\right)^{k-2 r} \\
& \times(2 r-1) \ldots \times 3 \times 1 \times\left[\left(1-\rho^{2}\right)\right]^{r}
\end{aligned}
$$

Now we use eq. (17) for finding the intervention effect for nonparanormal variable. That is,

$$
\begin{aligned}
E\left(Y \mid \operatorname{do}\left(X_{i}=x_{i}\right)\right)= & \int E\left(Y \mid X_{i}=x_{i} ; X_{\mathrm{pa}(i)}=x_{\mathrm{pa}(i)}\right) P\left(x_{\mathrm{pa}(i)}\right) d\left(x_{\mathrm{pa}(i)}\right) \\
= & \sum_{k=1}^{\infty} \sum_{r=0}^{\left\lfloor\frac{k}{2}\right\rfloor} f_{y}^{(k)}\left(z_{0}\right) \frac{1}{k!}\left(\frac{k}{2 r}\right)(2 r-1) \ldots 3.1 \times\left[\left(1-\rho^{2}\right)\right]^{r} \\
& \times \sum_{s=0}^{k-2 r}\left({ }^{k-2 r}\right)\left(-z_{0}+\beta_{i} z_{i}\right)^{s} \\
& \times \int\left(\beta_{\mathrm{pa}(i)}^{T} z_{\mathrm{pa}(i)}\right)^{k-2 r-s} P\left(z_{\mathrm{pa}(i)}\right) d\left(z_{\mathrm{pa}(i)}\right) \\
= & \sum_{k=1}^{\infty} \sum_{r=0}^{\left\lfloor\frac{k}{2}\right\rfloor} f_{y}^{(k)}\left(z_{0}\right) \frac{1}{k!}\left(\frac{k}{2 r}\right) \times(2 r-1) \ldots 3.1 \times\left[\left(1-\rho^{2}\right)\right]^{r} \\
& \times \sum_{s=0}^{k-2 r}\left[{ }^{k-2 r}\right)\left(-z_{0}+\beta_{i} z_{i}\right)^{s} E\left[\left(\beta_{2}^{T}{ }_{\mathrm{pa}(i)} Z_{\mathrm{pa}(i)}\right)^{k-2 r-s}\right]
\end{aligned}
$$

We get the following expression for the total causal effect,

$$
\left.\frac{\partial}{\partial x_{i}} E\left[Y \mid \operatorname{do}\left(X_{i}=x_{i}\right)\right]=\frac{\partial}{\partial z_{i}} E\left[Y \mid \operatorname{do}\left(X_{i}=x_{i}\right)\right] \frac{\partial z_{i}}{\partial x_{i}}
$$

where $\frac{\partial z_{i}}{\partial x_{i}}=\left\langle f_{i}^{-1}\right\rangle^{\prime}\left(x_{i}\right)$. Therefore, with plugging eqs (18) into (19), the proof is completed.

# Proof of Proposition 3 

## Proof 2

Define

$$
\hat{Z}_{n}=\left(\begin{array}{cccc}
\hat{z}_{1, i} & \hat{z}_{1, \mathrm{pa}(i)_{1}} & \cdots & \hat{z}_{1, \mathrm{pa}(i)_{k}} \\
\hat{z}_{2, i} & \hat{z}_{2, \mathrm{pa}(i)_{1}} & \cdots & \hat{z}_{2, \mathrm{pa}(i)_{k}} \\
\vdots & \vdots & \ddots & \vdots \\
\hat{z}_{N, i} & \hat{z}_{N, \mathrm{pa}(i)_{1}} & \cdots & \hat{z}_{N, \mathrm{pa}(i)_{k}}
\end{array}\right)
$$

such that $\hat{z}_{j, l}=\Phi^{-1}\left(\hat{F}_{l, \mathrm{n}}\left(x_{j l}\right)\right)$ where $x_{j l}$ is the non-ordered $j$ th sample of variable $l$ and $\mathrm{pa}(i)$ is the index set of $k$ parents of $i$.Let

$$
\hat{Y}_{n}^{T}=\left(\Phi^{-1}\left(\hat{F}_{y, \mathrm{n}}\left(y_{1}\right)\right), \Phi^{-1}\left(\hat{F}_{y, \mathrm{n}}\left(y_{2}\right)\right), \cdots, \Phi^{-1}\left(\hat{F}_{y, \mathrm{n}}\left(y_{N}\right)\right)\right)
$$

The coefficient $\hat{\beta}_{i}^{n}$ is defined as the first element of the vector,

$$
\hat{\beta}^{n}=\left(\hat{Z}_{n}^{t} \hat{Z}_{n}\right)^{-1} \hat{Z}_{n}^{t} \hat{Y}_{n}
$$

We can also define the oracle estimator $\hat{B}_{i}^{n}$ as the first element of

$$
\hat{B}^{n}=\left(Z_{n}^{t} Z_{n}\right)^{-1} Z^{t} \mathrm{Y}_{n}
$$

where $Z_{n}$ and $\mathrm{Y}_{n}$ are obtained by replacing the marginal $\tilde{F}$ s by the true $F$ s. Consider an arbitrary $\varepsilon, \delta>0$,

$$
\begin{aligned}
& P\left(\left|\tilde{\beta}_{i}^{n}-\beta_{i}\right|>\epsilon\right) \quad P\left(\left|\tilde{\beta}_{i}^{n}-\bar{B}_{i}^{n}+\bar{B}_{i}^{n}-\beta_{i}\right|>\epsilon\right) \\
& \leq P\left(\left(\left|\tilde{\beta}_{i}^{n}-\bar{B}_{i}^{n}\right|+\left|\bar{B}_{i}^{n}-\beta_{i}\right|\right)>\epsilon\right) \\
& \leq P\left(\left(\left|\tilde{\beta}_{i}^{n}-\bar{B}_{i}^{n}\right|>\epsilon / 2\right)+P\left(\left|\bar{B}_{i}^{n}-\beta_{i}\right|\right)>\epsilon / 2\right) .
\end{aligned}
$$

We first consider the first right hand side term of eq. (20). Let's define $\tilde{A}_{n}=\frac{Z_{n}^{t} Z_{n}}{n}, A_{n}=\frac{Z_{n}^{t} Z_{n}}{n}$ and $\tilde{b}_{n}=\frac{Z_{n}^{t} \bar{Y}_{n}}{n}$ and $b_{n}=\frac{Z_{n}^{t} \bar{Y}_{n}}{n}$. Then,

$$
\begin{aligned}
P\left(\left|\tilde{\beta}_{i}^{n}-\bar{B}_{i}^{n}\right|>\frac{\epsilon}{2}\right) \leq & P\left(\left\|\tilde{A}_{n}^{-1} \tilde{b}_{n}-A_{n}^{-1} b_{n}\right\|^{2}>\frac{\epsilon}{2}\right) \\
& \leq P\left(\left\|\tilde{A}_{n}^{-1}\left(\tilde{b}_{n}-b_{n}\right)\right\|^{2}\right. \\
& \left.+\left\|\left(\tilde{A}_{n}^{-1}-A_{n}^{-1}\right) b_{n}\right\|^{2}>\frac{\epsilon}{2}\right) \\
& \leq P\left(\left\|\tilde{A}_{n}^{-1}\left(\tilde{b}_{n}-b_{n}\right)\right\|^{2}>\frac{\epsilon}{4}\right) \\
& +P\left(\left\|\left(\tilde{A}_{n}^{-1}-A_{n}^{-1}\right) b_{n}\right\|^{2}>\frac{\epsilon}{4}\right)
\end{aligned}
$$

By the consistency of $\tilde{z}$, we have that both $\tilde{b}_{n}$ and $b_{n}$ converge in probability to some $b=\Sigma_{(i, \mathrm{pa}(i)), p}$ and both $\tilde{A}_{n}^{-1}$ and $A_{n}^{-1}$ converge in probability to some $A^{-1}=\Sigma_{(i,}^{-1} \mathrm{pa}(i)),(i, \mathrm{pa}(i))$, where $\Sigma$ is defined in the body of Theorem Theorem 1. Therefore, there is a $n^{*}$, such that for all $n \geq n^{*}$, both terms on the right hand side of eq. (21) are less than $\delta / 4$. So for all $n \geq n^{*}$,

$$
P\left(\left|\tilde{\beta}_{i}^{n}-\bar{B}_{i}^{n}\right|>\frac{\epsilon}{2}\right)<\frac{\delta}{2}
$$

For the second term of the right hand side of eq. (20), it is sufficient to use the fact that in the latent normal space a regression estimate is consistent and therefore, there exist a $n^{\perp}$, such that any $n>n^{\perp}$,

$$
P\left(\left|\tilde{B}_{i}^{n}-\beta_{i}\right|>\epsilon / 2\right)<\delta / 2
$$

Putting both results together, we now have that for any $n \geq \max \left(n^{*}, n^{\perp}\right)$,

$$
P\left(\left|\tilde{\beta}_{i}^{n}-\beta_{i}\right|>\epsilon\right)<\delta
$$

Thus we get the desired result.

# Proof of Proposition 4 

## Proof 3

For two sequences of random variables $Z_{n}$ and $W_{n}$ and two random variables $Z, W$, such that $Z_{n}$ converges in probability to $Z$ and $W_{n}$ converges in probability to $W$, then it is a standard result that $Z_{n} W_{n}$ converges in probability to $Z W$ [21]. As all the components of $\widetilde{\mathrm{NCE}}_{0}(x)$ have been shown to be consistent, then the estimator is consistent.
