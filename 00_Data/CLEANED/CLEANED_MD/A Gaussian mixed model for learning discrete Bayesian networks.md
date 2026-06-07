# NIH Public Access 

Author Manuscript
Stat Probab Lett. Author manuscript; available in PMC 2012 February 1.
Published in final edited form as:
Stat Probab Lett. 2011 February 1; 81(2): 220-230. doi:10.1016/j.spl.2010.11.009.

## A Gaussian Mixed Model for Learning Discrete Bayesian Networks

Nikolay Balov ${ }^{a}$<br>${ }^{a}$ Department of Biostatistics and Computational Biology, University of Rochester Medical Center, 601 Elmwood Ave, Rochester, NY-14642


#### Abstract

In this paper we address the problem of learning discrete Bayesian networks from noisy data. Considered is a graphical model based on mixture of Gaussian distributions with categorical mixing structure coming from a discrete Bayesian network. The network learning is formulated as a Maximum Likelihood estimation problem and performed by employing an EM algorithm. The proposed approach is relevant to a variety of statistical problems for which Bayesian network models are suitable - from simple regression analysis to learning gene/protein regulatory networks from microarray data.


## Keywords

Bayesian networks; learning; mixture models; MLE; EM algorithm

## 1. Introduction

Graphical models provide a framework for representing the dependence between random variables through directed edges in graphs. Bayesian networks form a class of graphical models subject to the assumption that the variables can be ordered according to their causal relationship. They witnessed a renewed interest in recent years due to promising applications to systems biology and genetics - for example, Bayesian networks provide efficient means for describing the mechanisms of control and regulation of gene expressions.

Over the last few decades, a large amount of research and literature has been devoted to the problem of learning Bayesian networks - some main sources are Buntine (1996), Heckeman et al. (1995) and Neapolitan (2003). A typical learning is based on the so called score-based approach. It identifies a network structure according to some scoring criterion such as the $a$ posterior probability of a network given some data, or some likelihood based criteria such as AIC or BIC. Another learning approach is formed by the constraint-based algorithms that use conditional independence tests to find associations between the node-variables. Once the graphical structure of a Bayesian network is identified, in the context of a specified probability model, it is usually straightforward to estimate the parameters of the corresponding conditional probabilities. However, finding the structure of Bayesian

[^0]
[^0]:    Correspondence to: Nikolay Balov.
    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

networks with more than one parent is a NP-hard problem, Chickering (1996), which motivates the search of model constraints and assumptions to relax its general intractability.

In this paper we restrict our attention to discrete Bayesian networks with multinomial conditional distributions. The data is assumed to be observations on categorical variables plus additional Gaussian noise distributed independently among them. In other words, the nodes of the networks are assumed latent, unobserved, random variables, while the actual, observed, variables are their noisy instances. In this case, the conditional distributions of the observed continuous variables are essentially mixture of Gaussian ones and the model can be referred to as mixed Bayesian network. The model estimation is performed in a frequentist manner using the Maximum Likelihood (ML) principle. Under the assumption that the causal order of the node-variables is known, the MLE solution is approximated by employing an Expectation Maximization (EM) algorithm. The node order assumption, despite being considered unacceptable from a general learning standpoint, is the one that allows the global MLE, if exists, to be found, in contrast to many, more general but heuristic learning algorithms (see Heckeman et al. (1995) for systematical overview), which provide only 'local' solutions.

The model considered in this paper can be formulated as a special case of the Conditional Gaussian (CG) model, Lauritzen (1992), not to be mistaken with the substantially different linear Gaussian model. CG models belongs to the family of mixed graphical association models that have been first introduced by Lauritzen \& Wermuth (1984). A CG model allows both discrete and continuous variables, but the latter can have as parents only discrete ones on which they depend through conditional Gaussian distributions. CG models are well studied and efficient local procedures for calculating their marginal distributions, means and variances are available, Lauritzen (1992) and Lauritzen \& Jensen (2001). However, a method for estimating both the graphical and probability structures of a general CG model is not available.

In the context of network learning, the EM algorithm is typically applied in two settings when some of the data is missing, Lauritzen (1995), or when some of the variables are hidden. In Chickering \& Heckerman (1996), considered is a general approach to parameter estimation for networks with hidden variables that resorts to computationally intensive methods, such as Monte-Carlo, for approximation of the marginal distributions. The lack of close form expression of the marginals in a Bayesian network model limits substantially the applicability of EM.

The application of EM has been mostly limited to learning the probability model parameters of Bayesian networks. One exception is Friedman (1997), where a method for learning the structure of Discrete Bayesian networks from incomplete data is proposed. The algorithm described there is a variant of the EM in which the M-step is replaced by two alternating steps: a local structure search, similar to the greedy hill-climbing procedure, and parameter estimation. Its advantage is that it does not require the node order to be known. However, since it converges to locally optimal solutions, it is sensitive to the initial configurations, and second, requires discrete data. In contrast, the proposed here estimation procedure seamlessly combines the discretization and structure learning steps in one unified EM algorithm.

The main advantage of the framework considered in this paper is its ability to model continuous variables by unrestricted categorical distributions and thus able to express complex, non-linear relationships between them (see Example 1 below). Consequently, in appropriate settings, this approach provides greater representation power than the discrete Bayesian networks alone and parametric models such as the linear Gaussian networks.

Moreover, with close form expression for the expected sufficient statistics, our model estimation algorithm can be implemented accurately and efficiently.

The paper is organized as follows. In Section 2 we introduce the discrete Bayesian network model and in Section 3 its extension - the mixture of Gaussian Bayesian network (MGBN). In Section 4 we formulate the estimation problem for MGBN and derive an EM algorithm to solve it. Finally, in Section 5, we present simulation results and a small study for learning the interactions between some genes complicated in lung cancer.

The MGBN model inference is implemented in the mugnet R-package, which also contains code for reproducing the presented in the paper examples.

# Example 1. (Motivation Example) 

The MGBN is designed to model random vectors, which components are multi-modal continuous variables that follow some mixture of Gaussian distributions. In Table 1 we show the distribution of a random vector ( $\mathrm{X}, \mathrm{Y}$ ), such that $\mathrm{X}=\mathrm{A}+\mathrm{e}_{\mathrm{A}}$ and $\mathrm{Y}=\mathrm{B}+\mathrm{e}_{\mathrm{B}}$ for independent $\mathrm{e}_{\mathrm{A}} \sim \mathcal{N}(0,0.04)$ and $\mathrm{e}_{\mathrm{B}} \sim \mathcal{N}(0,0.08)$, and discrete random variables A and B with probability table fully specified by $\mathrm{P}(\mathrm{A})$ and $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$, shown on the left. On the right, plotted is a large sample of ( $\mathrm{X}, \mathrm{Y}$ ), which clearly shows the cluster-like structure of the joint distribution. Note that in this case fitting the linear Gaussian model $\mathrm{B} \sim \mathrm{A}$ is not appropriate. In the remainder of this paper, we present a method for recovering not only the distribution of (A, B) from a ( $\mathrm{X}, \mathrm{Y}$ )-sample, but also the dependence relations in case of many nodevariables.

## 2. Discrete Bayesian Networks

A Bayesian Network (BN) $\mathcal{G}=(G, P)$ is defined by directed acyclic graph (DAG) $G$ with random node-variables $x_{i}, i=1, . ., n$, and probability model $P$. The directed arcs of $G$ determine the parent-child relations, while the model $P$ is a set of conditional distributions, one for each node, specifying the distribution of the nodes conditional on their parents. $\mathcal{G}$ is discrete BN if each node $x$ is a discrete random variable that takes values in some finite set of categories $C_{x}$ and the conditional distributions are categorical. Let us denote with $\Pi_{i}$ the set of parent indices for node $x_{i}$ and with $P\left(x_{i} \mid x_{j}, j \in \Pi_{i}\right)$, or more concise $P\left(x_{i} \mid \Pi_{i}\right)$, its conditional probability. There is a topological order of the nodes of $\mathcal{G}$ such that the parents of each one appear always earlier in that order. To simplify the analysis, throughout this paper we will assume, without loss of generality, that the topological order of the nodes in $G$ is the same as their index order, a fact expressed symbolically as $x_{1}<x_{2}<\ldots<x_{n}$. That is, for every $i>1, \Pi_{i} \subset\{1,2, \ldots, i-1\}$ and $\Pi_{1}=\varnothing$. An application of the Bayes formula gives us the following factorization of the joint probability

$$
\log P\left(x_{1}, \ldots, x_{n} \mid \mathcal{G}\right)=\sum_{i=1}^{n} \log P\left(x_{i} \mid x_{j}, j<i\right)=\sum_{i=1}^{n} \log P\left(x_{i} \mid \Pi_{i}\right)
$$

Hereafter, we assume that the node categorical sets are $C_{i}=\left\{1, \ldots, a_{i}\right\}$ for some natural numbers $a_{i}>1$. We also denote by $C\left[\Pi_{i}\right]$ the set of possible combination of parent categories, $C\left[\Pi_{i}\right] \equiv \otimes_{j} \in \Pi_{i} C_{j}$.

Categorical distributions, also called multinomial distributions, are the most general model for the conditional probabilities $P\left(x_{i} \mid \Pi_{i}\right)$. With a slight abuse of notation, with $P\left(x_{i} \mid \Pi_{i}=C\right)$ we will denote $P\left(x_{i} \mid x_{j}=c_{j}, j \in \Pi_{i}\right)$, for a parent configuration $C=\left(c_{j}\right) \in C\left[\Pi_{i}\right]$. By definition, $\Sigma_{c \in C_{i}} P\left(x_{i}=c \mid \Pi_{i}=C\right)=1$. Hence, each conditional probability $P\left(x_{i} \mid \Pi_{i}\right)$ requires

$\alpha_{i}=\left(\alpha_{i}-1\right) \times \prod_{j \in \Pi_{i}} a_{j}$ parameters to be specified. The total number $\alpha=\sum_{i=1}^{n} \alpha_{n_{i}}$ called network complexity, gives the overall number of parameters of the discrete BN $\mathcal{G}$.

As defined, the discrete BNs have no parametric constraints on their conditional distributions except the number of node categories. However, this generality is counterbalanced by the potential information loss in the process of data categorization. In practice, most data is obtained by analogous instruments and is measured effectively in continuous form. In order to fit a discrete BN one needs, before anything else, to discretize the continuous outcome, which usually results in information loss and hampers the statistical analysis. This loss can be especially costly when dealing with small sample sizes, as it is the case with microarray data. In the existing practice, the problems of discretization and fitting a discrete BN, are considered separately, which is not a statistically satisfactory approach. The methodology we present next addresses this issue.

# 3. Mixture of Gaussian Bayesian Networks 

We consider the following model

$$
y_{i}=\beta_{i, x_{i}}+e_{i}, i=1, \ldots, n
$$

where $y=\left(y_{1}, \ldots, y_{n}\right)$ is a continuous random vector, $x=\left(x_{1}, \ldots, x_{n}\right)$ comes from a discrete BN $\mathcal{G}$, and $e_{i}$ are independent, zero mean Gaussian random variables with variances $\sigma_{i}^{2}$, i.e. $e=\left(e_{1}, \ldots, e_{n}\right) \sim \mathcal{N}\left(0, \operatorname{diag}\left(\sigma_{i}^{2}\right)\right)$. In this setting, $y$ is the observed random vector, while $x$ is unobserved, also latent, discrete random vector. The triple

$$
\theta=\left(\left\{\beta_{i}=\left(\beta_{i, k}\right)_{i \in C_{i}}\right\}\right)_{i=1}^{n},\left\{\sigma_{i}^{2}\right\}_{i=1}^{n}, \mathcal{G})
$$

constitutes the parameter set for model (2).
For given $x_{i}, y_{i}$ is a Gaussian variable with mean $\beta_{i, x_{i}}$ and variance $\sigma_{i}^{2}$. In equivalent formulation of (2), the logarithm of the density of $y_{i}$ conditional on $x_{i}$ can be written as

$$
\log \left(P\left(y_{i} \mid x_{i}, \theta\right)\right)=-\frac{1}{2}\left[\log \left(2 \pi \sigma_{i}^{2}\right)+\frac{1}{\sigma_{i}^{2}}\left(y_{i}-\beta_{i, x_{i}}\right)^{2}\right]
$$

The local Markov property implies that each $x_{i}$ depends on $x_{j<i}$ (all $x_{j}$ with $j<i$ ), only through $x_{j} \in \Pi_{i}$ (all $x_{j}$ with $j \in \Pi_{i}$ ). Moreover, $y_{i}$ depends on $x_{j \leq i}$ only through $x_{i}$. By applying these observations we obtain a convenient expression for the logarithm of the joint distribution of $x$ and $y$

$$
\log P(y, x \mid 0)=\log P\left(y_{1}, x_{1} \mid \theta\right)+\sum_{i=2}^{n} \log P\left(y_{i}, x_{i} \mid y_{j<i}, x_{j<i}, \theta\right)=\sum_{i=1}^{n}\left[\log P\left(y_{i} \mid x_{i}, \theta\right)+\log P\left(x_{i} \mid x_{j \in \Pi_{i}}, \theta\right)\right]=\sum_{i=1}^{n} \log P\left(y_{i}, x_{i} \mid x_{j \in \Pi_{i}}, \theta\right)
$$

By combining equations (1), (3) and (4), we write the log-likelihood of $\theta$ with respect to a given sample $(y, x)$ as
$l(\Theta \mid y, x)=-\frac{1}{2} \sum_{i=1}^{n}\left[\log \left(2 \pi \sigma_{i}^{2}\right)+\frac{1}{\sigma_{i}^{2}}\left(y_{i}-\beta_{i, x_{i}}\right)^{2}\right]+\log P\left(x_{1}, \ldots, x_{n} \mid \mathcal{G}\right)$.

Some of the properties of model (2) can be elucidated by deriving the conditional distributions of $y$ 's. For example, the distribution of $y_{i}$ conditional on its parents $y_{j \in \Pi_{i}}$ is given by

$$
E_{x_{i} \mid y_{j \in \Pi_{i}}} P\left(y_{i} \mid x_{i}, y_{j \in \Pi_{i}}\right)=E_{x_{i} \mid y_{j \in \Pi_{i}}} P\left(y_{i} \mid x_{i}\right)=\sum_{c \in C_{i}} P\left(y_{i} \mid x_{i}=c\right) P\left(x_{i}=c \mid y_{j \in \Pi_{i}}\right)
$$

where $P\left(y_{i} \mid x_{i}\right)$ are Gaussian distributions, and thus, is a mixture of Gaussian ones. In the light of this observation we tentatively refer to model (2) as mixture of Gaussian Bayesian network (MGBN).

The additional parameters $\beta$ and $\sigma^{2}$ increase the complexity of a MGBN network compared to its underlying discrete BN. The $i$-th node with $a_{i}$ categories contributes additional $1+a_{i}$ parameters (one for $\sigma_{i}^{2}$ and $a_{i}$ for $\left.\beta_{i, s}^{\prime} s\right)$, thus, increasing the overall complexity of $\mathcal{G}$ to

$$
\alpha(\mathcal{G})=\sum_{i=1}^{n}\left[1+a_{i}+\left(a_{i}-1\right) \prod_{j \in \Pi_{i}} a_{j}\right]
$$

# Example 2 

Here we consider the expression levels of AKT 1 and GSK3A genes from the lung cancer data described and analyzed in Section 5 below. In Fig. 1, we show the cross plot for the original sample of size 62 (left), as well as for a sample of size 200, simulated from a fitted MGBN model (right). Also shown are the $\beta$ parameters of the model corresponding to AKT 1 and GSK3A variables, drawn as vertical and horizontal lines, respectively. The cross points of the $\beta$-lines are centroids of Gaussian clusters. This is a situation where modeling continuous variables with categorical distributions, as the MGBN model does, seems appropriate.

## 4. EM Estimation

### 4.1. Problem Formulation

The main problem considered in this article is MGBN model estimation from observations on $y$. It involves learning the discrete BN $\mathcal{G}$ as well as estimating the mean parameters $\beta$ and variances $\sigma^{2}$. A standard solution is provided by the Maximum Likelihood principle. Moreover, the Expectation Maximization algorithm seems particularly well suited for the task because it can handle latent variables - in our case the discrete random vector $x$.

We assume that the network $\mathcal{G}$ has a known topological order and this is the index order, i.e. $x_{1} \prec x_{2} \prec \ldots \prec x_{n}$. In many practical problems, such as those of recovering gene regulatory networks, this assumption is a natural one if viewed from the perspective that any prior

information for the node order should come from experimental studies. For example, the gene-node order in microarray studies can be inferred using perturbed samples. Identifying the causality relations between random variables only by statistical means is rarely possible for there might be many networks with different orders that fit the data equally well. Specifying an order resolves this issue and, eventually, makes the MLE network identifiable. This is the reason why in the considered here framework we provide MLE solutions only relative to given orders.

The EM algorithm is a standard technique for finding a local ML parameter configuration (Dempster, Laird \& Rubin (1977)). It essentially requires optimization of the following score function of $\theta, r\left(\theta \mid y, \theta^{*}\right)=E l(\theta \mid y, x)$, where the expectation is taken with respect to the conditional distribution of $\left(x \mid y, \theta^{*}\right)$ for a fixed choice $\theta^{*}$ of the parameters. Starting from an initial $\theta^{1}$, a sequence $\theta^{k}$ is constructed according to $\theta^{k+1}=\arg \max _{\theta} r\left(\theta \mid \theta^{k}, y\right)$, until some convergence criteria are met.

Applying Eq. (4) we obtain $r\left(\theta \mid y, \theta^{*}\right)=\sum_{i=1}^{n} r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)$, with $r_{i}$ defined as
$r_{i}\left(\theta_{i} \mid y, \theta^{*}\right) \equiv E_{x \mid y, \theta^{*}} \log P\left(y_{i}, x_{i} \mid x_{j \in \Pi_{i}}, \theta\right)=E_{x_{i}, x_{j \in \Pi_{i}} \mid y, \theta^{*}} \log P\left(y_{i}, x_{i} \mid x_{j \in \Pi_{i}}, \theta_{i}\right)$,
where $\theta=\left(\theta_{i}\right)_{i=1}^{n}$ and $\theta_{i}=\left(\beta_{i, k}, \sigma_{i}^{2}, \Pi_{i}, P\left(x_{i} \mid \Pi_{i}\right)\right)$ is the model parameter corresponding to the $i$-th node. The last equality in (6) follows from the fact that $P\left(y_{i}, x_{i} \mid x_{j} \in \Pi_{i}\right)$ depends on $\theta$ only through $\theta_{i}$.

At the second step of EM, one needs to maximize $r\left(\theta \mid y, \theta^{*}\right)$ as a function of $\theta$.
Unfortunately, the expectations in (6) involve the calculation of the joint distribution of $y$ 's. The latter problem can easily become computationally prohibitive since it requires considering all possible configurations of $x$ 's $\left(\prod_{i=1}^{n} a_{i}\right.$ in total). Thus we exclude the possibility of a straightforward implementation of EM based on Eq. (6) as impractical.

In regard to the difficulties of finding $r\left(\theta \mid y, \theta^{*}\right)$, we observe that accessible seem to be only 'local' expectation calculations which involve distributions of limited subsets of nodes. For example, we can readily express the distribution of $x_{i}$ and its parents conditional on $y_{i}$ and $y_{j \in \Pi_{i}}$. Indeed, let us define $p_{i, c} C \equiv P\left(x_{i}=c, \Pi_{i}=C \mid \bar{\varphi}\right)$, for $c \in C_{i}$ and $C \in C\left[\Pi_{i}\right]$, to denote the joint distribution of $x_{i}$ and its parents $\Pi_{i}$ in the network $\bar{\varphi}$. Since $y_{j}$ does not depend on $\bar{\varphi}$ if the value of $x_{j}$ is known, and all $x_{j}$ depend on $\theta$ only through the network $\bar{\varphi}$, we infer that

$$
\begin{aligned}
P\left(x_{i}=c,\right. & \left.\Pi_{i}=C \mid y_{i}, y_{j \in \Pi_{i}}, \theta\right)=\frac{P\left(x_{i}=c, \Pi_{i}=C \mid \mathcal{G}\right) P\left(y_{i} \mid x_{i}=c, \theta\right) \prod_{j \in \Pi_{i}} P\left(y_{j} \mid x_{j}=c_{j}, \theta\right)}{P\left(y_{i}, y_{j \in \Pi_{i}} \mid \theta\right)} \\
& =\frac{p_{i, c} \exp \left(-\frac{1}{2 \sigma_{i}^{2}}\left(y_{i}-\beta_{i, c}\right)^{2}-\sum_{j \in \Pi_{i}} \frac{1}{2 \sigma_{i}^{2}}\left(y_{j}-\beta_{j, c_{j}}\right)^{2}\right)}{\sum_{d \in C_{i}} \sum_{D \in C\left[\Pi_{i}\right]} p_{i, d D} \exp \left(-\frac{1}{2 \sigma_{i}^{2}}\left(y_{i}-\beta_{i, d}\right)^{2}\right)-\sum_{j \in \Pi_{i}} \frac{1}{2 \sigma_{i}^{2}}\left(y_{j}-\beta_{j, d_{j}}\right)^{2} \mid \rangle}
\end{aligned}
$$

where $C=\left(c_{j}\right)_{j \in \Pi_{i}}$ and $D=\left(d_{j}\right)_{j \in \Pi_{i}}$. In addition, the conditional distribution of $x_{i}$ is

$$
P\left(x_{i}=c \mid y_{i}, y_{j \in \Pi_{i}}, \theta\right)=\sum_{C \in C\left[\Pi_{i}\right]} P\left(x_{i}=c, \Pi_{i}=C \mid y_{i}, y_{j \in \Pi_{i}}, \theta\right)
$$

Because of the additive form of the score function, the maximization of $r\left(\theta \mid y, \theta^{*}\right)$ can be split into a sequence of $n$ maximization problems, one for each $\theta_{i}$. Motivated by this observation we propose to relax the baseline EM algorithm by considering the following alternative score function $h\left(\theta \mid y, \theta^{*}\right)=\sum_{i=1}^{n} h_{i}\left(\theta_{i} \mid y, \theta^{*}\right)$, defined as
$h_{i}\left(\theta_{i} \mid y, \theta^{*}\right) \equiv E_{x_{i}, x_{j \in \Pi_{i}} \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}} \log P\left(y_{i}, x_{i} \mid x_{j \in \Pi_{i}}, \theta_{i}\right)=E_{x_{i}, x_{j \in \Pi_{i}} \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}}\left[\log P\left(y_{i} \mid x_{i}, \beta_{i}, \sigma_{i}^{2}\right)+\log P\left(x_{i} \mid x_{j \in \Pi_{i}}, \theta_{i}\right)\right]$,
instead of the original (6). For each node, we thus consider the conditional expectation involving only those $x^{\prime}$ s and $y^{\prime}$ s used in the corresponding probability term in (6). Next, we briefly comment on the validity of using $h$ instead of $r$ as an EM score function.

Let $Y=\left\{y^{1}, \ldots, y^{m}\right\}$ be a sample of $y$ coming from a MGBN model with parameter $\theta_{0}$. Denote by $\tilde{l}, \tilde{r}$ and $\tilde{h}$ the sample averages of the likelihood $l, r$ and $h$; for example, $\bar{h}_{i}\left(\theta_{i} \mid Y, \theta^{*}\right)=\frac{1}{N} \sum_{j=1}^{m} h_{i}\left(\theta_{i} \mid y^{j}, \theta^{*}\right)$. Let $\hat{\theta}_{r, m}$ be a limit point of an EM sequence $\theta^{k}, \theta^{k+1}=\arg$ $\max _{\theta} r\left(\theta \mid \theta^{k}, y\right)$, and $\hat{\theta}_{h, m}$ be a limit point of an EM sequence based on $h$. Then, it must be that $\hat{\theta}_{r, m}=\arg \max _{\theta} r\left(\theta \mid Y, \hat{\theta}_{r, m}\right)$ and $\hat{\theta}_{h, m}=\arg \max _{\theta} \tilde{h}\left(\theta \mid Y, \hat{\theta}_{h, m}\right)$. We claim that the estimations based on $r$ and $h$ are asymptotically equivalent in the following sense: if $\hat{\theta}_{r, m}$ are consistent estimators of the true parameter $\theta_{0}$, so are $\hat{\theta}_{h, m}$. A support for this claim is given in Appendix A.

# 4.2. Algorithm Derivation 

To evaluate the score function $h$, we start with the first term in (9)
$E_{x_{i} \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}} \log \left(P\left(y_{i} \mid x_{i}, \beta_{i}, \sigma_{i}^{2}\right)\right)=-\frac{1}{2}\left[\log \left(2 \pi \sigma_{i}^{2}\right)+\frac{1}{\sigma_{i}^{2}} E_{x_{i} \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}}\left(y_{i}-\beta_{i, x_{i}}\right)^{2}\right]=-\frac{1}{2}\left[\log \left(2 \pi \sigma_{i}^{2}\right)+\frac{1}{\sigma_{i}^{2}} \sum_{c \in C_{i}}\left(y_{i}-\beta_{i, c}\right)^{2} q_{i, c}^{*}\right]$,
where $q_{i, c}^{*}=P\left(x_{i}=c \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}\right)$ are the conditional probabilities defined by Eq. (8). For the second term in (9) we have
$E_{x_{i}, x_{j \in \Pi_{i}} \mid y_{i}, y_{j \in \Pi_{i}}, \theta^{*}} \log P\left(x_{i} \mid x_{j \in \Pi_{i}}\right)=\sum_{C \in C\left[\Pi_{i}\right]} \sum_{i \in C_{i}} \log P\left(x_{i}=c \mid \Pi_{i}=C\right) q_{i, c}^{*}$,
where $q_{i, c}^{*} \equiv P\left(x_{i}=c, \Pi_{i}=C \mid y_{i}, y_{j \in \Pi_{i}}, \Theta^{*}\right)$ as in Eq. (7).
At the second step of the EM algorithm, we need to maximize the sum of (10) and (11) in order to find an optimal network $\mathcal{O}$. This problem requires for each $i$ to find, first, the optimal parenthood $\Pi_{i}$ of node $x_{i}$ and second, the conditional probability $P\left(x_{i} \mid \Pi_{i}\right)$. Provided $\Pi_{i}$ is known, the optimal conditional probability can be easily derived. Indeed, by using the fact that for every fixed $C \in C\left[\Pi_{i}\right]$

$$
\arg \max _{c}\left\{\sum_{c} \log \left(v_{c}\right) q_{i, c}^{*}\left|\sum_{c} v_{c}=1\right|=\left(\frac{q_{i, c}^{*}}{\sum_{d} q_{i, d}^{*}}\right)\right.
$$

for the expectation in Eq. (11) we can write

$$
\max _{\theta} E_{x_{i}, x_{j \in \Pi_{i}}\left(y_{i}, y_{j \in \Pi_{i}}\right), \theta^{k}} \log P\left(x_{i} \mid x_{j \in \Pi_{i}}\right)=\sum_{C} \sum_{c} q_{i, c C}^{*} \log \left(q_{i, c C}^{*} / \sum_{d} q_{i, d C}^{*}\right)
$$

Recall that the EM algorithm is an iterative procedure that for a sample $Y$ and a starting triple $\theta^{0}=\left(\sigma^{0}, \beta^{0}, \sigma\right)$, constructs a sequence $\theta^{k}=\left(\sigma^{k}, \beta^{k}, \sigma\right), k=1,2 \ldots$, until a target convergence threshold for $h\left(\left.\theta^{k+1} \mid Y, \theta^{k}\right)\right)$ is achieved. To simplify the algorithm iteration equations, we introduce notations for the probabilities (7) and (8) referring to iteration index $k$ and sample instance $l$

$$
\begin{gathered}
q_{i, c C}^{k, l} \equiv \frac{p_{i, c C}^{k} \exp \left(-\frac{1}{2\left(\sigma^{k+1}\right.}\left[\left(y_{i}^{l}-\beta_{i, c}^{k}\right)^{2}+\sum_{j \in \Pi_{i}}\left(y_{j}^{l}-\beta_{j, c c}^{k}\right)^{2}\right]\right)}{\sum_{d \in C_{i}} \sum_{D \in C\left[\Pi_{i}\right]} p_{i, d D}^{k} \exp \left(-\frac{1}{2\left(\sigma^{k+1}\right.}\left[\left(y_{i}^{l}-\beta_{i, c c}^{k}\right)^{2}+\sum_{j \in \Pi_{i}}\left(y_{j}^{l}-\beta_{j, c c}^{k}\right)^{2}\right]\right)} \\
q_{i, c}^{k, l} \equiv \sum_{D \in C\left[\Pi_{i}\right]} q_{i, c D}^{k, l}, \text { and let } \bar{q}_{i, c C}^{k} \equiv \sum_{l=1}^{m} q_{i, d C}^{k, l}
\end{gathered}
$$

where $p_{i, c}^{k}$ and $p_{i, c C}^{k}$ denote the probabilities $P\left(x_{i} \mid G^{k}\right)$ and $P\left(x_{i}, \Pi_{i} \mid G^{k}\right)$, respectively. We consider $q_{i, c}^{k, l}$ and $q_{i, c C}^{k, l}$ as functions of the parent set $\Pi_{i}$.

Then, at the $k$-th iteration, the EM algorithm computes $\theta^{k+1}$ from $\theta^{k}$ as a solution of

$$
\theta^{k+1} \equiv\left(\sigma^{k+1}, \beta^{k+1}, \mathcal{G}^{k+1}\right)=\arg \max _{\theta \backslash \beta, \mathcal{G}} \sum_{i=1}^{n} H_{i}^{k}\left(Y, \theta_{i}\right)
$$

where, by utilizing Eq. (12) for the sums $\bar{q}_{i, c C}^{k}$, we define $H_{i}^{k}\left(Y, \theta_{i}\right)$ to be

$$
-\frac{m}{2} \log \left(2 \theta \sigma_{i}^{2}\right)-\frac{1}{2 \sigma_{i}^{2}} \sum_{l=1}^{m} \sum_{c \in C_{i}} q_{i, c}^{k, l}\left(y_{i}^{l}-\beta_{i, c}\right)^{2}+\sum_{C \in C\left[\Pi_{i}\right]} \sum_{j \in C_{i}} \bar{q}_{i, c C}^{k} \log \left(\bar{q}_{i, c C}^{k} / \sum_{d \in C_{i}} \bar{q}_{i, d C}^{k}\right)
$$

Note that the optimization function in (13) is additive for the nodes of the network and $\theta_{i}^{k+1}=\arg \max _{\theta_{i}} H_{i}^{k}\left(Y, \theta_{i}\right)$. This fact greatly simplifies the computation process for allowing the evaluation of $\sigma^{k+1}, \beta^{k+1}$ and $G^{k+1}$ on node by node basis.

Without imposing some restrictions on network $\sigma^{++}$, Eq. (13) will always select the maximum connected network - one for which each node has as parents all the nodes appearing earlier in the node order. This trivial solution is the least economical one and surely will over-fit any reasonable data. Apparently, some model selection restrictions on $\sigma^{++}$are necessary such as searching for networks with fixed in advance complexity. Alternatively, we may apply some standard model selection criteria such as AIC or BIC. Then the complexity of $\sigma^{2}$ may vary from iteration to iteration. Next, we write the estimation equations for these cases.

# 4.3. EM Algorithm with Model Selection 

If the parent set sizes $\left|\Pi_{i}\right|$ of the nodes are known and fixed, then it is straightforward to write the iteration equations for $\theta^{k+1}$. In this case the complexities of the resulting networks are predetermined. The optimal graph structure $\bar{v}$ in (13) can be found following the topological order of the nodes - the parenthood of the $i$-th node is a subset of size $\left|\Pi_{i}\right|$ of nodes appearing earlier in the order, that maximizes $H_{i}^{k}$ and can be searched for exhaustively. The optimal $\beta$ 's and $\sigma$ 's are the usual MLE solutions from the linear regression analysis. Specifically, the solution of (13) includes the following update rules for $\beta_{i}^{k}, \sigma_{i}^{k}$ and $\Pi_{i}^{k}$

$$
\begin{gathered}
\beta_{i, c}^{k+1}=\sum_{t=1}^{m} q_{i, c}^{k, t} \gamma_{i}^{t} / \bar{q}_{i, c}^{2} \\
\left(\sigma_{i}^{k+1}\right)^{2}=\frac{1}{m} \sum_{l=1}^{m} \sum_{c \in C_{i}} q_{i, c}^{k, l}\left(\gamma_{i}^{l}-\beta_{i, c}^{k+1}\right)^{2} \\
\Pi_{i}^{k+1}=\arg \max _{\Pi_{i}}\left\{-\frac{m}{2} \log \left(\sum_{t=1}^{m} \sum_{c \in C_{i}} q_{i, c}^{k, l}\left(\gamma_{i}^{l}-\beta_{i, c}^{k+1}\right)^{2}\right)+\sum_{C \in C\left\{\Pi_{i}\right\} \in C_{i}} \bar{q}_{i, c}^{k} \cdot \log \left(\bar{q}_{i, c}^{k} \cdot\left(\sum_{d \in C_{i}} \bar{q}_{i, d c}^{k}\right)\right\}
\end{gathered}
$$

where $\Pi_{i}$ is chosen among the subsets of $\{1, \ldots, i-1\}$ of size $\left|\Pi_{i}\right|$. At every iteration step $k$, the update equations (14)-(16) are applied in order from $x_{1}$ to $x_{n}$, or according to the node topological order if it is different from the assumed one $x_{1} \prec x_{2} \prec \ldots \prec x_{n}$.

If the parent set sizes are unknown, one needs an additional selection criterion to avoid the trivial, most connected, network as a solution of (13). This is essentially a model selection problem similar to that considered in Salzman \& Almudevar (2006). A natural choice is a network with a specified, target, complexity $A$. Then the algorithm guarantees optimally for this target complexity. To express it formally we modify Eq. (13) to

$$
\left(\sigma^{k+1}, \beta^{k+1}, \mathcal{G}^{k+1}\right)=\arg \max _{\theta}\left\{\sum_{i=1}^{n} H_{i}^{k}\left(Y, \theta_{i}\right) \mid \alpha(\mathcal{G})=A\right\}
$$

A second option is EM algorithm with AIC network selection, which replace (13) with

$$
\left(\sigma^{k+1}, \beta^{k+1}, \mathcal{G}^{k+1}\right)=\arg \max _{\theta}\left\{\sum_{i=1}^{n} H_{i}^{k}\left(Y, \theta_{i}\right)-\alpha(\mathcal{G})\right\}
$$

where, recall, $\alpha(\bar{v})$ is the network complexity. A third option is to use the BIC criterion that leads to the following iteration equation

$$
\left(\sigma^{k+1}, \beta^{k+1}, \mathcal{G}^{k+1}\right)=\arg \max _{\theta}\left\{\sum_{i=1}^{n} H_{i}^{k}\left(Y, \theta_{i}\right)-0.5 \alpha(\mathcal{G}) \log (m)\right\}
$$

If $n$ is the number of nodes and $\max c=\max _{i=1}^{n} c_{i}$ is the maximum number of categories per node, the complexity of one EM iteration is exponential to the maximum parent size $\max p=\max _{i=1}^{n}\left|\Pi_{i}\right|$ and is of order $O\left(m *(n * \max c)^{\max p+1}\right)$. Note that the computational complexity of the algorithm, both in processing time and memory, may quickly become prohibitive with the increase of maxp. Nevertheless, estimating networks with $n \leq 100$, maxc $\leq 3$ and $\max p \leq 3$ is currently quite manageable (see the simulation results in the next section) and these are sufficient for many practical problems.

# 5. Results 

### 5.1. Simulation Studies

Here we demonstrate the performance of the proposed EM learning algorithm on simulated networks. In each test trial we generate a random MGBN, serving as a ground truth network, then draw samples of varying size from it and finally, do estimation. The network structure recovery is measured by the so called $F$-score, which is the harmonic mean of the specificity $(T N /(T N+F P))$ and sensitivity $(T P /(T P+F N))$, where $T P$ (true positives) is the number of correctly found directed edges, $F P$ is the number of edges present in the estimated network but not in the original one, and $F N$ is the number of edges present in the original network but not in the estimated one. A $F$-score of 1 means perfect reconstruction. MGBN is compared to another network learning with the discretization and network fitting steps performed separately. The latter method is denoted as D+BN. Note that without some assumptions on the marginal distributions of the nodes, the probability structure of a discrete BN can not be recovered, although the edge structure eventually can. The MGBN model, being a parametric one, provides such set of assumptions. Since D+BN with a general discretization method can not be properly compared to MGBN, to place both methods on equal footing, we perform the discretization step in D+BN using the (known) node marginal distributions from the original networks.

Table 2 presents results for two networks with sizes 25 and 100, 3 categories per node and a maximum of three parents per node. The networks have $\beta$-parameters in the $[-1,1]$ range and a substantial noise level with $\sigma^{2}=0.1$. From each of the networks four samples of size 100, 200, 400 and 800 are drawn and MGBN and D+BN estimation performed. For each trial we report the $F$-scores as well as the processing times in seconds. We limit the maximum parent size of the estimated MGBN to 2, one less than that of the original, which prevent perfect reconstruction but speeds up the computations. The number of EM-steps for MGBN varies from trial to trial, but is limited to a maximum of 60 .

Based on the $F$-score numbers, MGBN performs better than D+BN, although with much higher computational cost. The results also show that the computational time of MGBN estimation is according to the theoretical $O\left(m(3 n)^{3}\right)$-complexity and is linear on the sample size. ${ }^{1}$ Note that the presented simulation results are in favor of the D+BN method, for in a real problem, the node marginal distributions will be unknown and any other discretization method will result in worse performance of D+BN.

[^0]
[^0]:    ${ }^{1}$ The simulations are run on 2.66 GHz , i5 processor. D+BN and MGBN estimations are performed using catnet and mugnet $R$ packages.

# 5.2. Data Example: Learning Gene Regulatory Network 

In this section we illustrate the application potential of the MGBN model by a small microarray data study. The renewed interest in the graphical statistical models in recent years is due to the expectation that they would help understanding the complicated mechanism of gene and protein interactions within cells. The data we have chosen is from one of the BROAD Institute GSEA's publicly available datasets ${ }^{2}$ of transcriptional profiles from lung cancer cell lines, the Boston cohort. Extensive gene expression analysis of the data is published in Beer et al. (2002) and Bhattacharjee et al. (2001). The lung dataset contains about 12600 genes and 62 samples taken from patients with similar disease condition. Furthermore, the sample is separated into two equal classes of size 31, depending on the survival status at the end of the study - 'alive' and 'deceased'.

For illustration purposes only, we concentrate attention on a small subset of genes and try to learn the interaction between them using the framework we have just presented. We select the following nine genes: IGF1, PIK3CA, PT EN, PDK1, AKT1, BAD, CASP9, GSK3A and MT OR, that play an important role in the PI3K/PT EN/AKT pathway. This pathway is believed to have a critical role in cell survival process and its activation is linked to tumor genesis, Saal et al. (2007). Briefly, IGF1 is a growth factor gene, PIK3CA encodes the protein $p 110 \alpha$ and is mutated in a range of human cancers, PT EN is another oncogene with role in tumor suppression, and $A K T 1$ plays anti-apoptic action when activated. The selected subset of genes is ordered following the available in the literature gene interaction causality.

We fit MGBN to the combined data of the two survival classes and then look at the class differences using the fitted model. To avoid over-fitting the data, we carefully choose the number of node categories and the maximum number of parents per node such that the maximum node complexity is smaller than the sample size by some factor. With 2 parents and 2 categories per node the maximum node complexity is 7 . In this case, the saturated network with 1 parent per node has complexity 44 , while that with 2 parents has complexity 58. We fit MGBN using three different network selection criteria: AIC, 1-parent saturated network and 2-parents saturated network. The found three networks, $G 1, G 2$ and $G 3$, are shown in Fig. 2.

A distinguishing feature of any graphical probability model is its accessible interpretation. For example, the AIC-selected network, $G 1$, includes the top five most significant arcs, with PIK3CA $\rightarrow$ PT EN having the highest likelihood score. $G 1$ is a sub-network of $G 2$, which is saturated with all gene-nodes, except the root, having one parent - their most significant predictors. In the third network, $G 3$, each parent pair is the most significant among the possible ones for the corresponding node. The found three networks confirm some known gene regulations such as IGF1 $\rightarrow$ PIK3CA $\rightarrow$ PT EN $\rightarrow$ PDK1 and AKT $1 \rightarrow$ GSK3A.

The conditional probabilities of the fitted networks can be used to reveal details about the difference between the two survival classes. In network $G 3, B A D$ depends on $P T E N$ and $A K T 1$. To quantify the class difference, we estimate the $B A D$ conditional distribution using the 'alive' and 'deceased' sub-samples. The obtained two empirical conditional distributions are ploted in Fig. 3. Recall that each discrete gene-node has two categories (1 and 2) and thus, the pair (PT EN, AKT1) has four possible configurations. When $A K T 1$ is downregulated $(A K T 1=1)$, the distributions of $B A D$ are essentially the same for the two classes and are not influenced by PT EN. However, when $A K T 1$ is up-regulated ( $A K T 1=2$ ), the regulation of $B A D$ depends on $P T E N$ and is different between the survival classes. If both PT EN and AKT1 are up-regulated (see the fourth column in Fig. 3), the activity of $B A D$ is

[^0]
[^0]:    2 www.broadinstitute.org/gsea/datasets.jsp

slightly disturbed in the 'deceased' class in comparison to the 'alive' one. Similar plots, Fig. 4 , show the behavior of $A K T 1$. A consistent up-regulation of $A K T 1$ is evident for class 'deceased', in contrast to class 'alive', where its activity is moderated by PIK3CA - see the second column, $I G F 1=1, P I K 3 C A=2$. These observations are consistent with the inhibiting role of $A K T 1$ in cell apoptosis, which in turn, as it is known, leads to cancer cell proliferation.

The MGBN model is implemented in the mugnet R-package and is available from CRAN repositories. The lung cancer data and analysis in this section are also available as demonstration in mugnet.

# 6. Conclusion 

We have introduced the MGBN model - a discrete Bayesian network with Gaussian errors distributed independently across its nodes. It provides a framework for representing continuous variables via unconstrained categorical probability distributions. The model allows unification of two so far independently considered problems - data discretization and network learning. We have also derived an efficient procedure for MGBN estimation based on the Expectation Maximization method. In the appendix we briefly discuss the convergence properties of our estimator, including the MLE consistency, and present directions for more detailed treatment of this important subject. We believe that the MGBN model is suited for a variety of problems that involve complicated dependencies, such as learning gene/protein interactions from microarray data, as our small study has illustrated. The framework can be further extended by replacing the Gaussian error model with other distributions from the exponential family, thus diversifying its application scope.

## Acknowledgments

This work was supported by NIH grant K99LM009477 from the National Library Of Medicine. The content is solely the responsibility of the author and does not necessarily represent the official views of the National Library Of Medicine or the National Institutes of Health.

The author thanks Peter Salzman for many valuable discussions and suggestions. The author also thanks the reviewers, whose careful reading and valuable comments have helped for the improvement of this paper.

# Appendix A 

As in the main text, let $Y=\left\{y^{1}, \ldots, y^{m}\right\}$ be a sample from a MGBN with true parameter $\theta_{0}, \bar{r}$ and $\bar{h}$ be the sample averages of $r$ and $h$, and $\bar{\theta}_{r, m}$ and $\bar{\theta}_{h, m}$ be limit points of $r$ and $h$-based EM sequences, respectively. By introducing the complement index set $\widehat{i, \Pi}_{i}=\left\{j: j \neq i\right.$ and $\left.j \notin \Pi_{i}\right\}$ and observing that

$$
h_{i}\left(\theta_{i} \mid y, \theta^{*}\right)=E_{y_{i, \Pi_{i}}\left|y_{i}, y_{j \in \Pi_{i}}\right|} r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)
$$

we immediately obtain $E_{y \mid \theta}{ }^{*} r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)=E_{y \mid \theta}{ }^{*} h_{i}\left(\theta_{i} \mid y, \theta^{*}\right)$, for all $\theta$ and $\theta^{*}$. Therefore, by the strong law of large numbers, both $\bar{r}\left(\theta \mid Y, \theta^{*}\right)$ and $\bar{h}\left(\theta \mid Y, \theta^{*}\right)$ converge to $\operatorname{Er}\left(\theta \mid y, \theta^{*}\right)$, a.s., provided the expectations with respect to $y \mid \theta^{*}$ exist. Tentatively, we expect that the estimators $\bar{\theta}_{r, m}$ and $\bar{\theta}_{h, m}$ share the same properties.

The question of consistency of MLE for the MGBN model, which does not unconditionally hold, is more involved to be discussed in details here and we will only sketch one approach to this problem. For simplicity, hereafter we will assume that the parent sizes, $\left|\Pi_{i}\right|$, of all nodes are fixed. Any other setting would involve more complex structure for the parameter space and, generally, would require more stringent conditions to guarantee the uniqueness of MLE.

In order to show the asymptotic equivalence of the $h$ and $r$-based EM estimations, we will assume the following consistency sufficient conditions on $r$ known from the general asymptotic theory. Let there be a parameter set $\Theta$, with $\theta_{0}$ in the interior of $\Theta$, such that

$$
P\left(\widehat{\theta}_{r, m} \in \Theta\right) \rightarrow 1 \text { and } P\left(\widehat{\theta}_{h, m} \in \Theta\right) \rightarrow 1, \text { as } m \rightarrow \infty
$$

$\sup _{\theta^{*} \in \Theta} E_{y \mid \theta^{*}} \sup _{\theta \in \Theta}\left|\widehat{r}_{i}\left(\theta_{i} \mid Y, \theta^{*}\right)-E_{y \mid \theta^{*}} r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)\right| \rightarrow 0$, as $m \rightarrow \infty$,

for $i=1, \ldots, n$, and that all $\operatorname{Er}_{i}\left(\theta_{i} \mid y, \theta_{0}\right)$ have well separated maximums at $\theta_{0, i}$. The latter guarantees that the system of equations $\theta_{i}^{*}=\arg \max _{\theta_{i}} E r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)$ has a unique solution for $\theta^{*}$ $=\theta_{0}$. If we let $\theta^{*}=\theta_{0}$ in condition (A.3), we obtain uniform convergence in mean of the sample log-likelihood of $y$ to the expected one, which, together with the third condition, the well separateness of the maximums, is sufficient for the MLE consistency.

Next we observe that

$$
\sup _{\theta \in \Theta}\left|\overline{h_{i}}\left(\theta_{i} \mid Y, \theta^{*}\right)-E h_{i}\left(\theta_{i} \mid y, \theta^{*}\right)\right| \leq \sup _{\theta \in \Theta} E_{y_{i} y_{i} \mid y, \bar{y}, y, \bar{y}_{i}}\left|\bar{r}_{i}\left(\theta_{i} \mid Y, \theta^{*}\right)-E r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)\right| \leq E_{y_{i} y_{i} \mid y, \bar{y}, y, \bar{y}_{i}} \sup _{\theta \in \Theta} \bar{r}_{i}\left(\theta_{i} \mid Y, \theta^{*}\right)-E r_{i}\left(\theta_{i} \mid y, \theta^{*}\right) \mid
$$

by (A.1). Then condition (A.3) holds for $h$ as well and therefore, the score function $h$ also produces consistent estimators.

Are the above consistency sufficient conditions reasonable to be assumed? Which ones are general model properties that can be induced and which ones are essential? The identifiability of MLE, guaranteed by the well separateness of the maximum of $\operatorname{Er}\left(\theta \mid y, \theta_{0}\right)$, is an essential condition and it is model specific - it can not be induced. Let $\Theta$ be a bounded compact subset of the parametric space that contains $\theta_{0}$ in its interior and that does not intersect any hyper-plane $\sigma_{i}=0$ and $P\left(x_{i}=c \mid \Pi_{i}=C, \theta_{i}\right)=0$. Such $\Theta$ exists whenever the conditional distributions in $\theta_{0}$ are away from zero. Then, it can be shown that condition (A. 2) follows from the well-separateness of the maximum of $\operatorname{Er}_{i}\left(\theta_{i} \mid y, \theta_{0}\right)$ and the compactness of $\Theta$. To show (A.3) we express (6) as

$$
r_{i}\left(\theta_{i} \mid y, \theta^{*}\right)=-\frac{1}{2} \log \left(2 \pi \sigma_{i}^{2}\right)-\frac{1}{2 \sigma_{i}^{2}} \sum_{e \in \mathcal{E}_{i}}\left(y_{i}-\beta_{i, e}\right)^{2} P\left(x_{i}=c \mid y, \theta^{*}\right)+\sum_{c \in C_{i}, C \in C\left[\Pi_{i}\right]} \log \left(P\left(x_{i}=c \mid \Pi_{i}=C, \theta_{i}\right)\right) P\left(x_{i}=c, \Pi_{i}=C \mid y, \theta^{*}\right)
$$

and observe that, because of the compactness of $\Theta$, the supremum in (A.3) is bounded by

$$
\max _{\theta^{*}} E_{y \theta^{*}} \max _{\theta}\left\{b_{1}\left|\overline{\left(y_{i}-\beta_{i}\right)^{2}}-E\left(y_{i}-\beta_{i}\right)^{2}\right|+b_{2} \overline{\left.\overline{P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)}}-E P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)\right|\right\}
$$

for $b_{1}=\max _{\Theta}\left(1 / 2 \sigma_{i}^{2}\right)<\infty$ and $b_{2}=\max _{\Theta} \log \left(P\left(x_{i}=c \mid \Pi_{i}=C, \theta_{i}\right)\right)<\infty$, where the bar denotes sample average. Further considerations show that both terms above converge to zero. The convergence of the first one can be verified using the properties of the Gaussian distribution. In the second, since there are only finitely many possible parent sets $\Pi_{i}$, in fact at most $\binom{n-1}{\left|\Pi_{i}\right|}$, we have

$$
\max _{\theta} \mid \overline{P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)}-E P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)\left|\leq \sum_{\Pi_{i}} \mid \overline{P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)}-E P\left(x_{i}, \Pi_{i} \mid y, \theta^{*}\right)\right|
$$

and the latter sum converges to zero in mean by an application of the Dominated convergence theorem. Therefore, for $\Theta$ as chosen above, (A.3) is satisfied.

![img-0.jpeg](img-0.jpeg)

Figure 1.
The cross plot of GSK3A and $A K T 1$ genes for an original (left) and simulated (right) data. The latter is obtained from a MGBN model fitted to the original sample. See Example 2 and the analysis in Section 5 for more details.

![img-1.jpeg](img-1.jpeg)

Figure 2.
Three networks representing the lung cancer data according to different selection criteria. See the main text for details.

Figure 3.
The probabilities of $B A D$ conditional on $P T E N$ and $A K T 1$ for class 'alive', first row, and 'deceased', second row. The columns in each row correspond to the four combinations of PTEN and AKT1. The largest difference is observed in the second column, corresponding to PTEN $=1$ and $A K T 1=2$. There is also a slight difference when PTEN $=2$ and $A K T 1=2$ (fourth column).

![img-2.jpeg](img-2.jpeg)

Figure 4.
The probabilities of $A K T$ conditional on IGF1 and PIK3CA for class 'alive', first row, and 'deceased', second row. For the latter we observe a consistent activity of $A K T 1$. There is an apparent class difference when IGF1 $=1$ and PIK3CA $=2$ (second column).

# Table 1 

A simple 2-node MGBN model, $A \rightarrow B$, with its discrete probability table (on the left) and a sample drawn from it (on the right).


Table 2
Performance comparison of MGBN vs. separate discretization and BN fitting ( $\mathrm{D}+\mathrm{BN}$ ), both using AIC selection. Reported are the $F$-scores and the processing time in seconds (in brackets).
