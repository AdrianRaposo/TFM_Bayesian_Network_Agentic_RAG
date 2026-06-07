# Research Article 

## Uncovering Gene Regulatory Networks from Time-Series Microarray Data with Variational Bayesian Structural Expectation Maximization

Isabel Tienda Luna, ${ }^{1}$ Yufei Huang, ${ }^{2}$ Yufang Yin, ${ }^{2}$ Diego P. Ruiz Padillo, ${ }^{1}$ and M. Carmen Carrion Perez ${ }^{1}$<br>${ }^{1}$ Department of Applied Physics, University of Granada, 18071 Granada, Spain<br>${ }^{2}$ Department of Electrical and Computer Engineering, University of Texas at San Antonio (UTSA), San Antonio, TX 78249-0669, USA

Received 1 July 2006; Revised 4 December 2006; Accepted 11 May 2007
Recommended by Ahmed H. Tewfik
We investigate in this paper reverse engineering of gene regulatory networks from time-series microarray data. We apply dynamic Bayesian networks (DBNs) for modeling cell cycle regulations. In developing a network inference algorithm, we focus on soft solutions that can provide a posteriori probability (APP) of network topology. In particular, we propose a variational Bayesian structural expectation maximization algorithm that can learn the posterior distribution of the network model parameters and topology jointly. We also show how the obtained APPs of the network topology can be used in a Bayesian data integration strategy to integrate two different microarray data sets. The proposed VBSEM algorithm has been tested on yeast cell cycle data sets. To evaluate the confidence of the inferred networks, we apply a moving block bootstrap method. The inferred network is validated by comparing it to the KEGG pathway map.

Copyright © 2007 Isabel Tienda Luna et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

## 1. INTRODUCTION

With the completion of the human genome project and successful sequencing genomes of many other organisms, emphasis of postgenomic research has been shifted to the understanding of functions of genes [1]. We investigate in this paper reverse engineering gene regulatory networks (GRNs) based on time-series microarray data. GRNs are the functioning circuitry in living organisms at the gene level. They display the regulatory relationships among genes in a cellular system. These regulatory relationships are involved directly and indirectly in controlling the production of protein and in mediating metabolic processes. Understanding GRNs can provide new ideas for treating complex diseases and breakthroughs for designing new drugs.

GRNs cannot be measured directly but can be inferred based on their inputs and outputs. This process of recovering GRNs from their inputs and outputs is referred to as reverse engineering GRNs [2]. The inputs of GRNs are a sequence of signals and the outputs are gene expressions at either the mRNA level or the protein level. One popular technology
that measures expressions of a large amount of gene at the mRNA levels is microarray. It is not surprising that microarray data have been a popular source for uncovering GRNs $[3,4]$. Of particular interest to this paper are time-series microarray data, which are generated from a cell cycle process. Using the time-series microarray data, we aim to uncover the underlying GRNs that govern the process of cell cycles.

Mathematically, reverse engineering GRNs are a traditional inverse problem, whose solutions require proper modeling and learning from data. Despite many existing methods for solving inverse problems, solutions to the GRNs problem are however not trivial. Special attention must be paid to the enormously large scale of the unknowns and the difficulty from the small sample size, not to mention the inherent experimental defects, noisy readings, and so forth. These call for powerful mathematic modeling together with reliable inference. At the same time, approaches for integrating different types of relevant data are desirable. In the literature, many different models have been proposed for both static, cell cycle networks including probabilistic Boolean networks [5, 6], (dynamic) Bayesian networks [7-9], differential

equations [10], and others [11, 12]. Unlike in the case of static experiments, extra effort is needed to model temporal dependency between samples for the time-series experiments. Such time-series models can in turn complicate the inference, thus making the task of reverse engineering even tougher than it already is.

In this paper, we apply dynamic Bayesian networks (DBNs) to model time-series microarray data. DBNs have been applied to reverse engineering GRNs in the past [1318]. Differences among the existing work are the specific models used for gene regulations and the detailed inference objectives and algorithms. These existing models include discrete binomial models [14, 17], linear Gaussian models [16, 17], and spline function with Gaussian noise [18]. We choose to use the linear Gaussian regulatory model in this paper. Linear Gaussian models model the continuous gene expression level directly, thus preventing loss of information in using discrete models. Even though linear Gaussian models could be less realistic, network inference over linear Gaussian models is relatively easier than that for nonlinear and/or non Gaussian models, therefore leading to more robust results. It has been shown in [19] that if taking both computational complexity and inference accuracy into consideration, linear Gaussian models are favored over nonlinear regulatory models. In addition, this model actually models the joint effect of gene regulation and microarray experiments and the model validity is better evaluated from the data directly. In this paper, we provide the statistical test of the validity of the linear Gaussian model.

To learn the proposed DBNs from time-series data, we aim at soft Bayesian solutions, that is, the solutions that provide the a posteriori probabilities (APPs) of the network topology. This requirement separates the proposed solutions with most of the existing approaches such as greedy search and simulated-annealing-based algorithms, all of which produce only point estimates of the networks and are considered as "hard" solutions. The advantage of soft solutions has been demonstrated in digital communications [20]. In the context of GRNs, the APPs from the soft solutions provide valuable measurements of confidence on inference, which is difficult with hard solutions. Moreover, the obtained APPs can be used for Bayesian data integration, which will be demonstrated in the paper. Soft solutions including Markov chain Monte Carlo (MCMC) sampling [21, 22] and variational Bayesian expectation maximization (VBEM) [16] have been proposed for learning the GRNs. However, MCMC sampling is only feasible for small networks due to its high complexity. In contrast, VBEM has been shown to be much more efficient. However, the VBEM algorithm in [16] was developed only for parameter learning. It therefore cannot provide the desired APPs of topology. In this paper, we propose a new variational Bayesian structural EM (VBSEM) algorithm that can learn both parameters and topology of a network. The algorithm still maintains the general feature of VBEM for having low complexity, thus it is appropriate for learning large networks. In addition, it estimates the APPs of topology directly and is suitable for Bayesian data integration. To this end, we discuss a simple Bayesian strategy for integrating two
microarray data sets by using the APPs obtained from VBSEM.

We apply the VBSEM algorithm to uncover the yeast cell cycle networks. To obtain the statistics of the VBSEM inference results and to overcome the difficulty of the small sample size, we apply a moving block bootstrap method. Unlike conventional bootstrap strategy, this method is specifically designed for time-series data. In particular, we propose a practical strategy for determining the block length. Also, to serve our objective of obtaining soft solutions, we apply the bootstrap samples for estimating the desired APPs. Instead of making a decision of the network from each bootstrapped data set, we make a decision based on the bootstrapped APPs. This practice relieves the problem of small sample size, making the solution more robust.

The rest of the paper is organized as follows. In Section 2, DBNs modeling of the time-series data is discussed. The detailed linear Gaussian model for gene regulation is also provided. In Section 3, objectives on learning the networks are discussed and the VBSEM algorithm is developed. In Section 4, a Bayesian integration strategy is illustrated. In Section 5, the test results of the proposed VBEM on the simulated networks and yeast cell cycle data are provided. A bootstrap method for estimating the APPs is also discussed. The paper concludes in Section 6.

## 2. MODELING WITH DYNAMIC BAYESIAN NETWORKS

Like all graphical models, a DBN is a marriage of graphical and probabilistic theories. In particular, DBNs are a class of directed acyclic graphs (DAGs) that model probabilistic distributions of stochastic dynamic processes. DBNs enable easy factorization on joint distributions of dynamic processes into products of simpler conditional distributions according to the inherent Markov properties, and thus greatly facilitate the task of inference. DBNs are shown to be a generalization of a wide range of popular models, which include hidden Markov models (HMMs) and Kalman filtering models, or state-space models. They have been successfully applied in computer vision, speech processing, target tracking, and wireless communications. Refer to [23] for a comprehensive discussion on DBNs.

A DBN consists of nodes and directed edges. Each node represents a variable in the problem while a directed edge indicates the direct association between the two connected nodes. In a DBN, the direction of an edge can carry the temporal information. To model the gene regulation from cell cycle using DBNs, we assume to have a microarray that measures the expression levels of $G$ genes at $N+1$ evenly sampled consecutive time instances. We then define a random variable matrix $\mathbf{Y} \in \mathcal{R}^{G \times(N+1)}$ with the $(i, n)$ th element $\gamma_{i}(n-1)$ denoting the expression level of gene $i$ measured at time $n-1$ (see Figure 1). We further assume that the gene regulation follows a first-order time-homogeneous Markov process. As a result, we need only to consider regulatory relationships between two consecutive time instances and this relationship remains unchanged over the course of the microarray experiment. This assumption may be insufficient, but it will

![img-0.jpeg](img-0.jpeg)

Figure 1: A dynamic Bayesian network modeling of time-series expression data.

facilitate the modeling and inference. Also, we call the regulating genes the "parent genes," or "parents" for short.

Based on these definitions and assumptions, the joint probability \( p(\mathbf{Y}) \) can be factorized as \( p(\mathbf{Y}) = \prod_{1 \leq n \leq N} p(\mathbf{y}(n) \mid \mathbf{y}(n-1)) \), where \( \mathbf{y}(n) \) is the vector of expression levels of all genes at time \( n \). In addition, we assume that given \( \mathbf{y}(n-1) \), the expression levels at \( n \) become independent. As a result, \( p(\mathbf{y}(n) \mid \mathbf{y}(n-1)) \), for all \( n \), can be further factorized as \( p(\mathbf{y}(n) \mid \mathbf{y}(n-1)) = \prod_{1 \leq i \leq G} p(y_{i}(n) \mid \mathbf{y}(n-1)) \). These factorizations suggest the structure of the proposed DBNs illustrated in Figure 1 for modeling the cell cycle regulations. In this DBN, each node denotes a random variable in \( \mathbf{Y} \) and all the nodes are arranged the same way as the corresponding variables in the matrix \( \mathbf{Y} \). An edge between two nodes denotes the regulatory relationship between the two associated genes and the arrow indicates the direction of regulation. For example, we see from Figure 1 that genes 1, 3, and \( G \) regulate gene \( i \). Even though, like all Bayesian networks, DBNs do not allow circles in the graph, they, however, are capable of modeling circular regulatory relationship, an important property that is not possessed by regular Bayesian networks. As an example, a circular regulation can be seen in Figure 1 between genes 1 and 2 even though no circular loops are used in the graph.

To complete modeling with DBNs, we need to define the conditional distributions of each child node over the graph. Then the desired joint distribution can be represented as a product of these conditional distributions. To define the conditional distributions, we let \( \mathbf{p}_{\mathbf{a}_i}(n) \) denote a column vector of the expression levels of all the parent genes that regulate gene \( i \) measured at time \( n \). As an example in Figure 1, \( \mathbf{p}_{\mathbf{a}_i}(n)^T = [y_{1}(n), y_{3}(n), y_{G}(n)] \). Then, the conditional distribution of each child node over the DBNs can be expressed as \( p(y_i(n) \mid \mathbf{p}_{\mathbf{a}_i}(n-1)) \), for all \( i \). To determine the expression of the distributions, we assume linear regulatory relationship, that is, the expression level of gene \( i \) is the result of linear combination of the expression levels of the regulating genes at the previous sample time. To make further simplification, we assume the regulation is a time-homogeneous process.

Mathematically, we have the following expression:

$$y_i(n) = \mathbf{w}_i^T \mathbf{p}_{\mathbf{a}_i}(n-1) + e_i(n), \quad n = 1, 2, \dots, N,\tag{1}$$

where \( \mathbf{w}_i \in \mathcal{R} \) is the weight vector independent of time \( n \) and \( e_i(n) \) is assumed to be white Gaussian noise with variance \( \sigma_i^2 \). We provide in Section 5 the statistical test of the validity of white Gaussian noise. The weight vector is indicative of the degree and the types of the regulation [16]. A gene is upregulated if the weight is positive and is down-regulated otherwise. The magnitude (absolute value) of the weight indicates the degree of regulation. The noise variable is introduced to account for modeling and experimental errors. From (1), we obtain that the conditional distribution is a Gaussian distribution, that is,

$$p(y_i(n) \mid \mathbf{p}_{\mathbf{a}_i}(n-1)) = \mathcal{N}\left(\mathbf{w}_i^T \mathbf{p}_{\mathbf{a}_i}(n-1), \sigma_i^2\right). \tag{2}$$

In (1), the weight vector \( \mathbf{w}_i \) and the noise variance \( \sigma_i^2 \) are the unknown parameters to be determined.

### 2.1. Objectives

Based on the above dynamic Bayesian networks formulation, our work has two objectives. First, given a set of time-series data from a single experiment, we aim at uncovering the underlying gene regulatory networks. This is equivalent to learning the structure of the DBNs. In specific, if we can determine that genes 2 and 3 are the parents of gene 1 in the DBNs, there will be directed links going from gene 2 and 3 to gene 1 in the uncovered GRNs. Second, we are also concerned with integrating two data sets of the same network from different experiments. Through integrating the two data sets, we expect to improve the confidence of the inferred networks obtained from a single experiment. To achieve these two objectives, we propose in the following an efficient variational Bayesian structural EM algorithm to learn the network and a Bayesian approach for data integration.

## 3. LEARNING THE DBN WITH VBSEM

Given a set of microarray measurements on the expression levels in cell cycles, the task of learning the above DBN consists of two parts: structure learning and parameter learning. The objective of structure learning is to determine the topology of the network or the parents of each gene. This is essentially a problem of model or variable selection. Under a given structure, parameter learning involves the estimation of the unknown model coefficients of each gene: the weight vector $\mathbf{w}_{i}$ and the noise variance $\sigma_{i}^{2}$, for all $i$. Since the network is fully observed and, given parent genes, the gene expression levels at any given time are independent, we can learn the parents and the associated model parameters of each gene separately. Thus we only discuss in the following the learning process on gene $i$.

### 3.1. A Bayesian criterion for network structural learning

Let $\mathcal{S}_{i}=\left\{S_{i}^{(1)}, S_{i}^{(2)}, \ldots, S_{i}^{(K)}\right\}$ denote a set of $K$ possible network topologies for gene $i$, where each element represents a topology derived from a possible combination of the parents of gene $i$. The problem of structure learning is to select the topology from $\mathcal{S}_{i}$ that is best supported by the microarray data.

For a particular topology $S_{i}^{(k)}$, we use $\mathbf{w}_{i}^{(k)}, \mathbf{p a}_{i}^{(k)}, \mathbf{e}_{i}^{(k)}$ and $\sigma_{\Delta}^{2}$ to denote the associated model variables. We can then express (1) for $S_{i}^{(k)}$ in a more compact matrix-vector form

$$
\mathbf{y}_{i}=\mathbf{P a}_{i}^{(k)} \mathbf{w}_{i}^{(k)}+\mathbf{e}_{i}^{(k)}
$$

where $\mathbf{y}_{i}=\left[y_{i}(1), \ldots, y_{i}(N)\right]^{T}, \mathbf{P a}_{i}^{(k)}=\left[\mathbf{p a}_{i}^{(k)}(0), \mathbf{p a}_{i}^{(k)}(1)\right.$, $\left.\ldots, \mathbf{p a}_{i}^{(k)}(N-1)\right]^{+}, \mathbf{e}_{i}^{(k)}=\left[e_{i}^{(k)}(1), e_{i}^{(k)}(2), \ldots, e_{i}^{(k)}(N)\right]^{+}$, and $\mathbf{w}_{i}^{(k)}$ is independent of time $n$.

The structural learning can be performed under the Bayesian paradigm. In particular, we are interested in calculating the a posteriori probabilities of the network topology $p\left(S_{i}^{(k)} \mid \mathbf{Y}\right)$, for all $k$. The APPs will be important for the data integration tasks. They also provide a measurement of confidence on inferred networks. Once we obtain the APPs, we can select the most probable topology $\bar{S}_{i}$ according to the maximum a posteriori (MAP) criterion [24], that is,

$$
\bar{S}_{i}=\arg \max _{S_{i}^{(k)} \in \mathcal{S}_{i}} p\left(S_{i}^{(k)} \mid \mathbf{Y}\right)
$$

The APPs are calculated according to the Bayes theorem,

$$
\begin{aligned}
p\left(S_{i}^{(k)} \mid \mathbf{Y}\right) & =\frac{p\left(\mathbf{y}_{i} \mid S_{i}^{(k)}, \mathbf{Y}_{-i}\right) p\left(S_{i}^{(k)} \mid \mathbf{Y}_{-i}\right)}{p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)} \\
& =\frac{p\left(\mathbf{y}_{i} \mid \mathbf{P a}_{i}^{(k)}\right) p\left(S_{i}^{(k)}\right)}{p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)}
\end{aligned}
$$

where $\mathbf{Y}_{-i}$ represents a matrix obtained by removing $\mathbf{y}_{i}$ from $\mathbf{Y}$, the second equality is arrived at from the fact that given $S_{i}^{(k)}, \mathbf{y}_{i}$ depends on $\mathbf{Y}_{-i}$ only through $\mathbf{P a}_{i}^{(k)}$, and the last equation is due to that given $\mathbf{P a}_{i}^{(k)}, S_{i}^{(k)}$ is known automatically
but $S_{i}^{(k)}$ cannot be determined from $\mathbf{Y}_{-i}$. Note also that there is a slight abuse of notation in (4). $\mathbf{Y}$ in $p\left(S_{i}^{(k)} \mid \mathbf{Y}\right)$ denotes a realization of expression levels measured from a microarray experiment.

To calculate the APPs according to (5), the marginal likelihood $p\left(\mathbf{y}_{i} \mid \mathbf{P a}_{i}^{(k)}\right)$ and the marginalization constant $p\left(\mathbf{y}_{i}\right)$ $\mathbf{Y}_{-i}$ ) need to be determined. It has been shown that with conjugate priors on the parameters, we can obtain $p\left(\mathbf{y}_{i} \mid \mathbf{P a}_{i}^{(k)}\right)$ analytically [21]. However, $p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)$ becomes computationally prohibited for large networks because computing $p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)$ involves summation over $2^{G}$ terms. This difficulty with $p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)$ makes the exact calculation of the APPs infeasible. Numerical approximation must be therefore employed to estimate the APPs instead. Monte Carlo samplingbased algorithms have been reported in the literature for this approximation [21]. They are however computationally very expensive and do not scale well with the size of networks. In what follows, we propose a much more efficient solution based on variational Bayesian EM.

### 3.2. Variational Bayesian structural expectation maximization

To develop the VBSEM algorithm, we define a $G$-dimensional binary vector $\mathbf{b}_{i} \in\{0,1\}^{G}$, where $b_{i}(j)=1$ if gene $j$ is a parent of gene $i$ in the topology $S_{i}$ and $b_{i}(j)=0$ otherwise. We can actually consider $\mathbf{b}_{i}$ as an equivalent representation of $S_{i}$ and finding the structure $S_{i}$ can thus equate to determining the values of $\mathbf{b}_{i}$. Consequently, we can replace $S_{i}$ in all the above expressions by $\mathbf{b}_{i}$ and turn our attention to estimate the equivalent APPs $p\left(\mathbf{b}_{i} \mid \mathbf{Y}\right)$.

The basic idea behind VBSEM is to approximate the intractable APPs of topology with a tractable distribution $q\left(\mathbf{b}_{i}\right)$. To do so, we start with a lower bound on the normalizing constant $p\left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right)$ based on Jensen's inequality

$$
\begin{aligned}
\ln p & \left(\mathbf{y}_{i} \mid \mathbf{Y}_{-i}\right) \\
& =\ln \sum_{\mathbf{b}_{i}} \int d \boldsymbol{\theta}_{i} p\left(\mathbf{y}_{i} \mid \mathbf{b}_{i}, \boldsymbol{\theta}_{i}\right) p\left(\mathbf{b}_{i}\right) p\left(\boldsymbol{\theta}_{i}\right) \\
& \geq \int d \boldsymbol{\theta}_{i} q\left(\boldsymbol{\theta}_{i}\right)\left[\sum_{\mathbf{b}_{i}} q\left(\mathbf{b}_{i}\right) \ln \frac{p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)}{q\left(\mathbf{b}_{i}\right)}+\ln \frac{p\left(\boldsymbol{\theta}_{i}\right)}{q\left(\boldsymbol{\theta}_{i}\right)}\right]
\end{aligned}
$$

where $\boldsymbol{\theta}_{i}=\left\{\mathbf{w}_{i}, \sigma_{i}^{2}\right\}$ and $q\left(\boldsymbol{\theta}_{i}\right)$ is a distribution introduced for approximating the also intractable marginal posterior distribution of parameters $p\left(\boldsymbol{\theta}_{i} \mid \mathbf{Y}\right)$. The lower bound in (7) can serve as a cost function for determining the approximate distributions $q\left(\mathbf{b}_{i}\right)$ and $q\left(\boldsymbol{\theta}_{i}\right)$, that is, we choose $q\left(\mathbf{b}_{i}\right)$ and $q\left(\boldsymbol{\theta}_{i}\right)$ such that the lower bound in (7) is maximized. The solution can be obtained by variational derivatives and a coordinate ascent iterative procedure and is shown to include the following two steps in each iteration:

VBE step:

$$
q^{(t+1)}\left(\mathbf{b}_{i}\right)=\frac{1}{Z_{\mathbf{b}_{i}}} \exp \left[\int d \boldsymbol{\theta}_{i} q^{(t)}\left(\boldsymbol{\theta}_{i}\right) \ln p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)\right]
$$

The VBSEM algorithm
(1) Initialization

Initialize the mean and the covariance matrices of the approximate distributions as described in Appendix A.
(2) VBE step: structural learning

Calculate the approximate posterior distributions of topology $q\left(\mathbf{b}_{i}\right)$ using (B.1)
(3) VBM step: parameter learning

Calculate the approximate parameter posterior distributions $q\left(\boldsymbol{\theta}_{i}\right)$ using (B.5)
(4) Compute $\mathcal{F}$

Compute the lower bound as described in Appendix A. If $\mathcal{F}$ increases, go to (2). Otherwise, terminate the algorithm.

Algorithm 1: The summary of VBSEM algorithm

VBM step:
$q^{(t+1)}\left(\boldsymbol{\theta}_{i}\right)=\frac{1}{Z_{\theta_{i}}} p\left(\boldsymbol{\theta}_{i}\right) \exp \left[\sum_{\mathbf{b}_{i}} q^{(t+1)}\left(\mathbf{b}_{i}\right) \ln p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)\right]$,
where $t$ and $t+1$ are iteration numbers and $Z_{\mathbf{b}_{i}}$ and $Z_{\theta_{i}}$ are the normalizing constants to be determined. The above procedure is commonly referred to as variational Bayesian expectation maximization algorithm [25]. The VBEM can be considered as a probabilistic version of the popular EM algorithm in the sense that it learns the distribution instead of finding a point solution as in EM. Apparently, to carry out this iterative approximation, analytical expressions must exist in both VBE and VBM steps. However, it is difficult to come up with an analytical expression at least in the VBM step since the summation is NP hard. To overcome this problem, we enforce the approximation $q\left(\mathbf{b}_{i}\right)$ to be a multivariate Gaussian distribution. The Gaussian assumption on the discrete variable $\mathbf{b}_{i}$ facilitates the computation in the VBEM algorithm, circumventing the $2^{\text {G }}$ summations. Although $p\left(\mathbf{b}_{i} \mid \mathbf{Y}\right)$ is a high-dimensional discrete distribution, the defined Gaussian approximation will guarantee the approximations to fall in the exponential family, and as a result the subsequent computations in the VBEM iterations can be carried out exactly [25]. In specific, by choosing conjugate priors for both $\boldsymbol{\theta}_{i}$ and $\mathbf{b}_{i}$ as described in Appendix A, we can show that the calculations in both VBE and VBM steps can be performed analytically. The detailed derivations are included in Appendix B. Unlike the common VBEM algorithm, which learns only the distributions of parameters, the proposed VBEM learns the distributions of both structure and parameters. We, therefore, call the algorithm VB structural EM (VBSEM). The algorithm of VBSEM for learning the DBNs under study is summarized in Algorithm 1.

When the algorithm converges, we obtain $q\left(\mathbf{b}_{i}\right)$, a multivariate Gaussian distribution and $q\left(\boldsymbol{\theta}_{i}\right)$. Based on $q\left(\mathbf{b}_{i}\right)$, we need then to produce a discrete distribution as a final estimate of $p\left(\mathbf{b}_{i}\right)$. Direct discretization in the variable space is computationally difficult. Instead, we propose to work with the marginal APPs from model averaging. To this end, we
first obtain $q\left(b_{i}(l)\right)$, for all $l$ from $q\left(\mathbf{b}_{i}\right)$ and then approximate the marginal APPs $p\left(b_{i}(l) \mid \mathbf{Y}\right)$, for all $l$, by

$$
p\left(b_{i}(l)=1 \mid \mathbf{Y}\right)=\frac{q\left(b_{i}(l)=1\right)}{q\left(b_{i}(l)=1\right)+q\left(b_{i}(l)=0\right)}
$$

Instead of the MAP criterion, decisions on $\mathbf{b}_{i}$ can be then made in a bitwise fashion based on the marginal APPs. In specific, we have

$$
\tilde{b}_{i}(l)= \begin{cases}1 & \text { if } p\left(b_{i}(l) \mid \mathbf{Y}\right) \geq \rho \\ 0 & \text { otherwise }\end{cases}
$$

where $\rho$ is a threshold. When $\tilde{b}_{i}(l)=1$, it implies that gene $l$ is a regulator of gene $i$ in the topology of gene $i$. Meanwhile, parameters can be learned from $q\left(\boldsymbol{\theta}_{i}\right)$ easily based on the minimum mean-squared-error criterion (MMSE) and they are

$$
\tilde{\mathbf{w}}_{i}=\mathbf{m}_{\mathbf{w}_{i}}, \quad \tilde{\sigma}_{i}^{2}=\frac{\beta}{\alpha-2}
$$

where $\mathbf{m}_{\mathbf{w}_{i}}, \beta$, and $\alpha$ are defined in Appendix B according to (B.5).

## 4. BAYESIAN INTEGRATION OF TWO DATA SETS

A major task of the gene network research is to integrate all prevalent data sets about the same network from different sources so as to improve the confidence of inference. As indicated before, the values of $\mathbf{b}_{i}$ define the parent sets of gene $i$, and thus the topology of the network. The APPs obtained from the VBSEM algorithm provide us with an avenue to pursue Bayesian data integration.

We illustrate here an approach for integrating two microarray data sets $\mathbf{Y}^{1}$ and $\mathbf{Y}^{2}$, each produced from an experiment under possibly different conditions. The premise for combining the two data sets is that they are the experimental outcomes of the same underlying gene network, that is, the topologies $S_{i}$ or $\mathbf{b}_{i}$, for all $i$ are the same in the respective data models. Direct combination of the two data sets at the data level requires many preprocesses including scaling, alignment, and so forth. The preprocessing steps introduce noise and potential errors to the original data sets. Instead, we propose to perform data integration at the topology level. The objective of topology-level data integration is to obtain the APPs of $\mathbf{b}_{i}$ from the combined data sets $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}, \mathbf{Y}^{2}\right)$ and then make inference on the gene network structures accordingly.

To obtain $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}, \mathbf{Y}^{2}\right)$, we factor it according to the Bayes rule as

$$
\begin{aligned}
p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}, \mathbf{Y}^{2}\right) & =\frac{p\left(\mathbf{Y}^{2} \mid \mathbf{b}_{i}\right) p\left(\mathbf{Y}^{1} \mid \mathbf{b}_{i}\right) p\left(\mathbf{b}_{i}\right)}{p\left(\mathbf{Y}^{1}\right) p\left(\mathbf{Y}^{2}\right)} \\
& =\frac{p\left(\mathbf{Y}^{2} \mid \mathbf{b}_{i}\right) p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}\right)}{p\left(\mathbf{Y}^{2}\right)}
\end{aligned}
$$

where $p\left(\mathbf{Y}^{2} \mid \mathbf{b}_{i}\right)$ is the marginalized likelihood functions of data set 2 and $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}\right)$ is the APPs obtained from data set 1 .

The above equation suggests a simple scheme to integrate the two data sets: we start with a data set, say $\mathbf{Y}_{1}$, and calculate the APPs $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}\right)$; then by considering $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}\right)$ as the prior distribution, the data set $\mathbf{Y}^{1}$ is integrated with $\mathbf{Y}_{i}^{2}$ according to (13). By this way, we obtain the desired APPs $p\left(\mathbf{b}_{i} \mid \mathbf{Y}^{1}, \mathbf{Y}^{2}\right)$ from the combined data sets. To implement this scheme, the APPs of the topology must be computed and the proposed VBSEM can be applied for the task. This new scheme provides a viable and efficient framework for Bayesian data integration.

## 5. RESULTS

### 5.1. Test on simulated systems

### 5.1.1. Study based on precision-recall curves

In this section, we validate the performance of the proposed VBSEM algorithm using synthetic networks whose characteristics are as realistic as possible. This study was accomplished through the calculation of the precision-recall curves. Among the scientific community in this field, it is common to employ the ROC analysis to study the performance of a proposed algorithm. However, since genetic networks are sparse, the number of false positives far exceeds the number of true positives. Thus, the specificity is inappropriate as even small deviation from a value of 1 will result in a large number of false positives. Therefore, we choose the precision-recall curves in evaluating the performance. Precision corresponds to the expected success rate in the experimental validation of the predicted interactions and it is calculated as $T_{P} /\left(T_{P}+F_{P}\right)$, where $T_{P}$ is the number of true positives and $F_{P}$ is the number of false positives. Recall, on the other hand, indicates the probability of correctly detecting a true positive and it is calculated as $T_{P} /\left(T_{P}+F_{N}\right)$, where $F_{N}$ is the number of false negatives. In a good system, precision decreases as recall increases and the higher the area under the curve is the better the system is.

To accomplish our objective, we simulated 4 networks with $30,100,150$, and 200 genes, respectively. For each tested network, we collected only 30 time samples for each gene, which mimics the realistic small sample scenario. Regarding the regulation process, each gene had either none, one, two, or three parents. Besides, the number of parents was selected randomly for each gene. The weights associated to each regulation process were also chosen randomly from an interval that contains the typical estimated values when working with the real microarray data. As for the nature of regulation, the signs of the weights were selected randomly as well. Finally, the data values of the network outputs were calculated using the linear Gaussian model proposed in (1). These data values were taken after the system had reached stationarity and they were in the range of the observations corresponding to real microarray data.

In Figure 2, the precision-recall curves are plotted for different settings. In order to construct these curves, we started by setting a threshold $\rho$ for the APPs. This threshold $\rho$ is between 0 to 1 and it was used as in (11): for each possible regulation relationship between two genes, if its APP is greater

Table 1: Area under each curve.


![img-1.jpeg](img-1.jpeg)

Figure 2: Precision-recall curve. than $\rho$, then the link is considered to exist, whereas if the APP is lower than $\rho$, the link is not considered. We calculated the precision and the recall for each selected threshold between 0 and 1 . We plotted the results in blue for the case with $G=30$, black for $G=100$, red for $G=150$, and green for $G=200$. As expected, the performance got worse as the number of genes increases. One measure of this degradation is shown in Table 1 where we calculated the area under each curve (AUC).

To further quantify the performance of the algorithms, we calculated the $F$-score. $F$-score constitutes an evaluation measure that combines precision and recall and it can be calculated as

$$
F_{\alpha}=\frac{1}{\alpha(1 / \text { precision })+(1-\alpha)(1 / \text { recall })}
$$

where $\alpha$ is a weighting factor and a large $\alpha$ means that the recall is more important, whereas a small $\alpha$ means that precision is more important. In general, $\alpha=0.5$ is used, where the importance of precision and the importance of recall are even and $F_{\alpha}$ is called harmonic mean. This value is equal to 1 when both precision and recall are $100 \%$, and 0 when one of them is close to 0 . Figure 3 depicts the value of the harmonic mean as a function of the APP threshold $\rho$ for the VBSEM algorithm. As it can be seen, the performance of the algorithm for $G=30$ is better than the performance for any other setting. However, we can also see that there is almost no performance degradation between the curve corresponding to $G=30$ and the one for $G=100$ in the APP threshold interval from 0.5 to 0.7 . The same observation can be obtained for

Table 2: Computation time for different sizes of networks.


Table 3: Number of errors in 100 Monte Carlo trials.


curves $G=150$ and $G=200$ in the interval from 0.5 to 0.6 . In general, in the interval from 0.5 to 0.7 , the degradation of the algorithm performance is small for reasonable harmonic mean values (i.e., $>0.5$ ).

To demonstrate the scalability of the VBSEM algorithm, we have studied the harmonic mean for simulated networks characterized by the following settings: $\left(G_{1}=1000, N_{1}=\right.$ 400), $\left(G_{2}=500, N_{2}=200\right),\left(G_{3}=200, N_{3}=80\right)$, and $\left(G_{4}=100, N_{4}=40\right)$. As it can be noticed, the ratio $G_{i} / N_{i}$ has been kept constant in order to maintain the proportion between the amount of nodes in the network and the amount of information (samples). The results were plotted in Figure 4 where we have represented the harmonic mean as a function of the APP threshold. The closeness of the curves at APP threshold equal to 0.5 supports the good scalability of the proposed algorithm. We have also recorded the computation time of VBSEM for each network and listed them in Table 2. The results were obtained with a standard PC with 3.4 GHz and 2 GB RAM.

### 5.1.2. Comparison with the Gibbs sampling

We tested in this subsection the VBSEM algorithm on a simulated network in order to compare it with the Gibbs sampling [26]. We simulated a network of 20 genes and generated their expressions based on the proposed DBNs and the linear Gaussian regulatory model with Gaussian distributed weights. We focused on a particular gene in the simulated networks. The gene was assumed to have two parents. We compared the performance of VBSEM and Gibbs sampling in recovering the true networks. In Table 3, we present the number of errors in 100 Monte Carlo tests. For the Gibbs sampling, 500 Monte Carlo samples were used. We tested the algorithms under different settings. In the table, $N$ stands for the number of time samples and $G$ is the number of genes. As it can be seen, the VBSEM outperforms Gibbs sampling even in an underdetermined system. Since the VBSEM has much lower complexity than Gibbs sampling, the proposed VBSEM algorithm is better suited for uncovering large networks.
![img-2.jpeg](img-2.jpeg)

Figure 3: Harmonic mean as a function of the APP threshold.
![img-3.jpeg](img-3.jpeg)

Figure 4: Harmonic mean as a function of the APP threshold to proof scalability.

### 5.2. Test on real data

We applied the proposed VBSEM algorithm on cDNA microarray data sets of 62 genes in the yeast cell cycle reported in [27, 28]. The data set 1 [27] contains 18 samples evenly measured over a period of 119 minutes where a synchronization treatment based on $\alpha$ mating factor was used. On the other hand, the data set 2 [28] contains 17 samples evenly measured over 160 minutes and a temperaturesensitive CDC15 mutant was used for synchronization. For each gene, the data is represented as the $\log _{2}\{($ expression at time $t) /($ expression in mixture of control cells) $\}$. Missing

![img-4.jpeg](img-4.jpeg)

Figure 5: Inferred network using the $\alpha$ data set of [27].
values exist in both data sets, which indicate that there was no strong enough signal in the spot. In this case, simple spline interpolation was used to fill in the missing data. Note the time step that differs in each data set can be neglected since we assume a time-homogeneous regulating process.

When validating the results, the main objective is to determine the level of confidence of the connections in the inferred network. The underlying intuition is that we should be more confident on features that would still be inferred when we perturb the data. Intuitively, this can be performed on multiple independent data sets generated from repeated experiments. However, in this case and many other practical scenarios, only one or very limited data replicates are available and the sample size in each data set is small. The question is then how to produce the perturbed data from the limited available data sets and at the same time maintain the underlying statistical features of the data set. One way to achieve it is to apply the bootstrap method [29]. Through bootstrapping the data set, we can generate multiple pseudoindependent data sets, each of which still maintains the statistics of the original data. The bootstrap methods have been used extensively for static data sets. When applied to time-series data, an additional requirement is to maintain as much as possible the inherent time dependency between samples in the bootstrapped data sets. This is important since the proposed DBNs modeling and VBSEM algorithm exploit this time dependency. Approaches have been studied in the bootstrap literatures to handle time-dependent samples and we adopt the popular moving block bootstrap method [30]. In moving block bootstrap, we created pseudo-data sets from
the original data set by first randomly sampling blocks of sub-data sets and then putting them together to generate a new data set. The detailed steps can be summarized as follows.
(1) Select the length of the block $L$.
(2) Create the set of possible $n=N-L+1$ blocks from data. These blocks are created in the followingway:

$$
\mathbf{Z}_{i}=\mathbf{Y}(:, i: i+L-1)
$$

(3) Randomly sample with replacement $[N / L]$ blocks from the set of blocks $\left\{\mathbf{Z}_{i}\right\}_{i=1}^{N-L+1}$.
(4) Create the pseudo-data set by putting all the sampled blocks together and trim the size to $N$ by removing the extra data samples.

A key issue in moving block bootstrap is to determine the block length $L$. The idea is to choose a large enough block length $L$ so that observations more than $L$ time units apart will be nearly independent. Many theoretical and applicable results have been developed on choosing the block length. However, they rely on large size of data samples and are computationally intensive. Here, we develop an easy and practical approach to determine the block length. We compute the autocorrelation function on data and choose the block length as the delay, at which the ACF becomes the smallest. The ACF in this case may not be reliable but it provides at least some measures of independence.

In Figure 5, we show the inferred network when the data set from [27] was considered and the moving block bootstrap

![img-5.jpeg](img-5.jpeg)

Figure 6: Inferred network using the CDC28 data set of [28].

was used to resample the observations. The total number of re-sample data sets was 500. In this plot, we only drew those links with the estimated APP higher than 0.6. We used the solid lines to represent those links with weights between 0 and 0.4, the dotted lines for the links with weights between 0.4 and 0.8, and the lines with dashes and dots for those with weights higher than 0.8. The red color was used to represent downregulation. A circle enclosing some genes means that those corresponding proteins compose a complex. The edges inside these circles are considered as correct edges since genes inside the same circle will coexpress with some delay. In Table 4, we show the connections with some of the highest APPs found from the α data set of [27]. We compared them with the links in the KEGG pathway [31], and some of the links inferred by the proposed algorithm are predicted in it. We considered a connection as predicted when the parent is in the upper stream of the child in the KEGG. Furthermore, the proposed algorithm is also capable of predicting the nature of the relationship represented by the link through the weight. For example, the connection between CDC5 and CLB1 has a weight equal to 0.6568, positive, so it represents an upregulation as predicted in the KEGG pathway. Another example is the connection from CLB1 to CDC20; its APP is 0.6069 and its weight is 0.4505, again positive, so it stands for an up-regulation as predicted by the KEGG pathway.

In Figure 6, we depict the inferred network when the CDC28 data set of [28] was used. A moving block bootstrap was also used with the number of the bootstrap data sets equal to 500 again. Still, the links presented in this plots are those with the APP higher than 0.6. In Table 5, we show some of the connections with some of the highest APPs. We also compared them with the links in the KEGG pathway, and some of the links inferred by the proposed algorithm are also predicted in it. Furthermore, the proposed algorithm is

Table 4: Links with higher APPs obtained from the α data set of [27].


also capable of predicting the nature of the relationship represented by the link through the weight. For example, the connection between TEM1 and *DDC1* has a weight equal to -0.3034; the negative sign represents a downregulation as predicted in the KEGG pathway. Another example is the connection from *CLB2* to *CDC20*, its APP is 0.6069 and its weight is 0.7763, this time positive, so it stands for an up-regulation as predicted by the KEGG pathway.

### Model validation

To validate the proposed linear Gaussian model, we tested the normality of the prediction errors. If the prediction errors

![img-6.jpeg](img-6.jpeg)

Figure 7: Histogram of prediction error in the $\alpha$ data set.
![img-7.jpeg](img-7.jpeg)

Figure 8: Histogram of prediction error in the CDC28 data set.
yield Gaussian distributions as in the linear model (1), it then proves the feasibility of linear Gaussian assumption on data.

Given the estimated $\widehat{\mathbf{b}}_{i}$ and $\widehat{\mathbf{w}}_{i}$ of gene $i$, the prediction error $\widehat{\mathbf{e}}_{i}$ is obtained as

$$
\widehat{\mathbf{e}}_{i}=\mathbf{R} \widehat{\mathbf{W}}_{i} \widehat{\mathbf{b}}_{i}-\mathbf{y}_{i}
$$

where $\widehat{\mathbf{W}}_{i}=\operatorname{diag}\left(\widehat{\mathbf{w}}_{i}\right)$ and $\mathbf{R}=\mathbf{T Y}^{\top}$, with

$$
\mathbf{T}=\left(\begin{array}{cccc}
1 & & & 0 \\
& \ddots & & \vdots \\
& & 1 & 0
\end{array}\right)
$$

We show in Figures 7 and 8 examples of the histograms of the prediction errors for genes $D D C 1, M E C 3$, and GRF10 in the $\alpha$ and CDC28 data sets.

Those histograms exhibit the bell shape for the distribution of the prediction errors and such pattern is constant
over all the genes. To examine the normality, we performed Kolmogorov-Smirnov goodness-of-fit hypothesis test (KSTEST) of the prediction errors for each gene. All the prediction errors pass the normality test at the significance level of 0.05 , and therefore it demonstrates the validity of the proposed linear Gaussian assumption.

## Results validation

To systematically present the results, we treated the KEGG map as the ground truth and calculated the statistics of the results. Even though there are still uncertainties, the KEGG map represents up-to-date knowledge about the dynamics of gene interaction and it should be reasonable to serve as a benchmark of results validation. In Tables 6 and 7, we enlisted the number of true positives (tp), true negatives (tn), false positives (fp), and false negative (fn) for the $\alpha$ and CDC28 data sets, respectively. We also varied the

![img-8.jpeg](img-8.jpeg)

Figure 9: Inferred network by integrating the $\alpha$ and CDC28 data sets.

Table 5: Links with higher APPs obtained from the CDC28 data set of [28].


APP threshold for decision. (The thresholds are listed in the threshold column of the tables.) A general observation is that we do not have high confidence about the inference results since high tp cannot be achieved at low fp. Since the VBSEM algorithm has been tested with acceptable performance on simulated networks and the model has also been vali-

Table 6: The $\alpha$ data set.


Table 7: The CDC28 data set.


dated, this can very well indicate that the two data sets were not quite informative about the causal relationship between genes.

## Data integration

In order to improvethe accuracy of the inference, we applied the Bayesian integration scheme described in Section 4 to combine the two data sets, trying to use information provided from both data sets to improve the inference confidence. The Bayesian integration includes two stages. In the first stage, the proposed VBSEM algorithm is run on the data set 1 that contains larger number of samples. In the second

Table 8: Links with higher APPs obtained based on the integrated data set.


stage, the APPs of the latent variables $\mathbf{b}_{i}$ obtained in the first stage are used as the priors in the VBSEM algorithm run on the second data set from [28]. In Figure 9, we plot the inferred network obtained from the integration process. We also performed bootstrap resampling in the integration process: we first obtained a sampled data set from the data set 1 and then we use its calculated APPs as the prior to integrate a bootstrap sampled data from set 2 .

In Table 8, we present the links with the higher APPs inferred performing integration of the data sets. We made a comparison between these links and the ones shown in the KEGG pathway map again. As it can be seen, the proposed algorithm is able to predict many relationships. For instance, the link between CDC5 and CLB1 is predicted correctly by our algorithm with a posteriori probability of 0.7454 . The weight associated to this connection is -0.1245 , which is negative, and so there is a downregulation relationship confirmed in the KEGG pathway. We also observed improvements from integrating the two data sets. Regarding the link between CDC5 and CLB1, if we compare the result obtained from the integrated data set, with that shown in Table 4, we see that this relationship was not predicted when using the CDC28 data set 2. Even though this link was predicted by the $\alpha$ data set its APP is however lower and the weight is positive indicating an inconsistency with the KEGG map. The inconsistency has been fixed by data integration. As another example, the relationship between HSL7 and CLB1 was predicted based on the integrated data sets but it was not predicted from the CDC28 data set. This link was predicted when only the $\alpha$ data set was used but its APP is 0.6108 , lower than the APP obtained performing integration. Similar phenomenon can be observed for the link between FAR1 to SIC1 again.

Table 9: Integrated data set.


We also listed the statistics of the results when compared with the KEGG map in Table 9. We can see that when compared with Tables 6 and 7, data integration almost halved the fp at the thresholds 0.4 and 0.5 and also reduced the fp at 0.6. Meanwhile, tp increased. This implies the increased confidence on the results after data integration, which demonstrates the advantages of the Bayesian data integration.

Another way of looking at the benefits of the integration process is by examining the lower bound of the VBSEM. If the data integration process benefits the performance of the algorithm, we must see higher lower bound values than those of single data set. This happens because if the data contains more information after integration, the lower bound should be closer to the value it is approximating. In Figure 10, we plot the evolution of lower bound over the VBSEM iterations for each gene from the $\alpha$ data set, the CDC28 data set, and the integrated data sets. The increase of the lower bound, when the integrated data sets were used, supports the advantages of Bayesian data integration.

## 6. CONCLUSION

We investigated the DBNs modeling of cell cycle GRNs and the VBSEM learning of network topology. The proposed VBSEM solution is able to estimate the APPs of topology. We showed how the estimated APPs can be used in a Bayesian data integration strategy. The low complexity of the VBSEM algorithm shows its potential to work with large networks. We also showed how the bootstrap method can be used to obtain the confidence of the inferred networks. This approach has been approved very useful in the case of small data size, a common case in computational biology research.

## APPENDICES

## A. CONJUGATE PRIORS OF TOPOLOGY AND PARAMETERS

We choose the conjugate priors for topology and the parameters and they are

$$
\begin{aligned}
p\left(\mathbf{b}_{i}\right) & =\mathcal{N}\left(\mathbf{b}_{i} \mid \boldsymbol{\mu}_{0}, \mathbf{C}_{0}\right) \\
p\left(\boldsymbol{\theta}_{i}\right) & =p\left(\mathbf{w}_{i}, \sigma_{i}^{2}\right)=p\left(\mathbf{w}_{i} \mid \sigma_{i}^{2}\right) p\left(\sigma_{i}^{2}\right) \\
& =\mathcal{N}\left(\mathbf{w}_{i} \mid \boldsymbol{\mu}_{\mathbf{w}_{i}}, \sigma_{i}^{2} \mathbf{I}_{G}\right) I \mathcal{G}\left(\frac{\gamma_{0}}{2}, \frac{\nu_{0}}{2}\right)
\end{aligned}
$$

where $\boldsymbol{\mu}_{0}$ and $\mathbf{C}_{0}$ are the mean and the covariance of the prior probability density $p\left(\mathbf{b}_{i}\right)$. In general, $\boldsymbol{\mu}_{\mathbf{w}_{i}}$ and $\boldsymbol{\mu}_{0}$ are simply set as zero vectors, and meanwhile $\nu_{0}$ and $\gamma_{0}$ are set equal to small positive real values. Moreover, covariance matrix $\mathbf{C}_{0}$

![img-9.jpeg](img-9.jpeg)

Figure 10: Evolution of the VBSEM lower bound.
needs to be checked carefully and is usually set as a diagonal matrix with a relatively large constant at each diagonal element.

These priors satisfy the conditions for conjugate exponential (CE) models [25]. For conjugate exponential models, formulae exist in [25] for solving analytically the integrals in the VBE and VBM steps.

## B. DERIVATION OF VBE AND VBM STEPS

Let us first start with VBE step. Suppose that $q\left(\boldsymbol{\theta}_{i}\right)$ obtained in the previous VBM step follows a Gaussian-inverse-gamma distribution and has the expression (B.5). The VBE step calculates the approximation on the APPs of topology $p\left(\mathbf{b}_{i}\right)$. By applying the theorems of the CE model [25], $q\left(\mathbf{b}_{i}\right)$ can be shown to have the following expression:

$$
q\left(\mathbf{b}_{i}\right)=\mathcal{N}\left(\mathbf{b}_{i} \mid \mathbf{m}_{\mathbf{b}_{i}}, \Sigma_{\mathbf{b}_{i}}\right)
$$

where

$$
\mathbf{m}_{\mathbf{b}_{i}}=\Sigma_{\mathbf{b}_{i}}\left(\mathbf{C}_{0}^{-1}+\mathbf{f}\right) \quad \Sigma_{\mathbf{b}_{i}}=\left(\mathbf{C}_{0}^{-1}+\mathbf{D}\right)^{-1}
$$

with

$$
\begin{aligned}
\mathbf{D} & =\mathbf{B} \otimes\left[\left(\mathbf{m}_{\mathbf{w}_{i}} \mathbf{m}_{\mathbf{w}_{i}}\right)^{T}\left\langle\sigma_{i}^{-2}\right\rangle_{q\left(\theta_{i}\right)}+\mathbf{A}^{-1}\right] \\
\mathbf{f}^{\top} & =\mathbf{y}_{i}^{\top} \mathbf{R} \operatorname{diag}\left(\mathbf{m}_{\mathbf{w}_{i}}\right)\left\langle\sigma_{i}^{-2}\right\rangle_{q\left(\theta_{i}\right)} \\
\mathbf{B} & =\mathbf{R}^{\top} \mathbf{R} \\
\mathbf{A} & =\mathbf{I}_{G}+\mathbf{K} \\
\mathbf{K} & =\mathbf{B} \otimes\left(\Sigma_{\mathbf{b}_{i}}+\mathbf{m}_{\mathbf{b}_{i}} \mathbf{m}_{\mathbf{b}_{i}}^{T}\right)
\end{aligned}
$$

and $\mathbf{R}=\mathbf{T Y}^{\top}$, with

$$
\mathbf{T}=\left(\begin{array}{cccc}
1 & & & 0 \\
& \ddots & & \vdots \\
& & 1 & 0
\end{array}\right)
$$

being an $N \times(N+1)$ matrix.
We now turn to the VBM step in which we compute $q\left(\boldsymbol{\theta}_{i}\right)$. Again, from the CE model and $q\left(\mathbf{b}_{i}\right)$ obtained in (B.1), we have

$$
q\left(\boldsymbol{\theta}_{i}\right)=\mathcal{N}\left(\mathbf{w}_{i} \mid \mathbf{m}_{\mathbf{w}_{i}}, \Sigma_{\mathbf{w}_{i}}\right) \mathbb{1}_{g}\left(\frac{\alpha}{2}, \frac{\beta}{2}\right)
$$

where

$$
\begin{gathered}
\mathbf{m}_{\mathbf{w}_{i}}=\left(\mathbf{I}_{G}+\mathbf{K}\right)^{-1}\left(\mathbf{y}_{i}^{T} \mathbf{R} \mathbf{M}_{x}\right)^{T} \\
\Sigma_{\mathbf{w}_{i}}=\sigma_{i}^{2}\left(\mathbf{I}_{G}+\mathbf{K}\right)^{-1} \\
\alpha=N(\eta+1)-G-2 \\
\beta=-c
\end{gathered}
$$

with

$$
\begin{gathered}
\mathbf{M}_{x}=\operatorname{diag}\left(\mathbf{m}_{\mathbf{b}_{i}}\right) \\
c=\mathbf{y}_{i}^{\top} \mathbf{R} \mathbf{M}_{x} \mathbf{m}_{\mathbf{w}_{i}}-\mathbf{y}_{i}^{\top} \mathbf{y}_{i}-v_{0}
\end{gathered}
$$

and $\eta$ is a hyperparameter of the parameter prior $p\left(\boldsymbol{\theta}_{i}\right)$ based on CE models (A.2).

## 1. Computation of the lower bound $\mathcal{F}$

The convergence of the VBEM algorithm is tested using a lower bound of $\ln p\left(\mathbf{y}_{i}\right)$. In this paper, we use $\mathcal{F}$ to denote this lower bound and we calculate it using the newest $q\left(\mathbf{b}_{i}\right)$ and $q\left(\boldsymbol{\theta}_{i}\right)$ obtained in the iterative process. $\mathcal{F}$ can be written more succinctly using the definition of the KL divergence. Let us first review the definition of the KL divergence and then derive an analytical expression for $\mathcal{F}$.

The KL divergence measures the difference between two probability distributions and it is also termed relative entropy. Thus, using this definition we can write the difference between the real and the approximate distributions in the following way:

$$
\begin{gathered}
\mathrm{KL}\left[q\left(\mathbf{b}_{i}\right) \| p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)\right]=-\int d \mathbf{b}_{i} q\left(\mathbf{b}_{i}\right) \ln \frac{p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)}{q\left(\mathbf{b}_{i}\right)} \\
\mathrm{KL}\left[q\left(\boldsymbol{\theta}_{i}\right) \| p\left(\boldsymbol{\theta}_{i}\right)\right]=-\int d \boldsymbol{\theta}_{i} \ln \frac{p\left(\boldsymbol{\theta}_{i}\right)}{q\left(\boldsymbol{\theta}_{i}\right)}
\end{gathered}
$$

And finally, the lower bound $\mathcal{F}$ can be written in terms of the previous definitions as

$$
\begin{aligned}
\mathcal{F}= & \int d \boldsymbol{\theta}_{i} q\left(\boldsymbol{\theta}_{i}\right)\left[\int d \mathbf{b}_{i} q\left(\mathbf{b}_{i}\right) \ln \frac{p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)}{q\left(\mathbf{b}_{i}\right)}+\ln \frac{p\left(\boldsymbol{\theta}_{i}\right)}{q\left(\boldsymbol{\theta}_{i}\right)}\right] \\
= & -\int d \boldsymbol{\theta}_{i} q\left(\boldsymbol{\theta}_{i}\right) \mathrm{KL}\left[q\left(\mathbf{b}_{i}\right) \| p\left(\mathbf{b}_{i}, \mathbf{y}_{i} \mid \boldsymbol{\theta}_{i}\right)\right] \\
& -\mathrm{KL}\left[q\left(\boldsymbol{\theta}_{i}\right) \| p\left(\boldsymbol{\theta}_{i}\right)\right]
\end{aligned}
$$

## ACKNOWLEDGMENTS

Yufei Huang is supported by an NSF Grant CCF-0546345. Also M. Carmen Carrion Perez thanks MCyT under project TEC 2004-06096-C03-02/TCM forfunding.
