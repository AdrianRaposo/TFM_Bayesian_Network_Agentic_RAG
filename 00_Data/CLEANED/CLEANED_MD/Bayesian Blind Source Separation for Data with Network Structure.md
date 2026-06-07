# Bayesian Blind Source Separation for Data with Network Structure 

KATRIN ILLNER, CHRISTIANE FUCHS, and FABIAN J. THEIS


#### Abstract

In biology, more and more information about the interactions in regulatory systems becomes accessible, and this often leads to prior knowledge for recent data interpretations. In this work we focus on multivariate signaling data, where the structure of the data is induced by a known regulatory network. To extract signals of interest we assume a blind source separation (BSS) model, and we capture the structure of the source signals in terms of a Bayesian network. To keep the parameter space small, we consider stationary signals, and we introduce the new algorithm emGrade, where model parameters and source signals are estimated using expectation maximization. For network data, we find an improved estimation performance compared to other BSS algorithms, and the flexible Bayesian modeling enables us to deal with repeated and missing observation values. The main advantage of our method is the statistically interpretable likelihood, and we can use model selection criteria to determine the (in general unknown) number of source signals or decide between different given networks. In simulations we demonstrate the recovery of the source signals dependent on the graph structure and the dimensionality of the data.


Key words: Bayesian network, expectation maximization, linear mixing model, model selection, stationary signals.

## 1. INTRODUCTION

TThe separation of informative signals from multivariate data is a widespread task in biological applications. The data might, for example, be from gene regulatory networks or metabolomic pathways, where one is interested in the underlying processes. The aspect of separation is known as blind source separation (BSS); that is, the signals of interest and the actual experimental data are linked by a linear mixing model. In this work, we focus on signaling data, where the signals are associated with some known network structure, and we use this structure to archive a more appropriate separation of the data.

A widely used BSS approach for stationary time-series data is to diagonalize the time-delayed covariance (autocovariance) of the multivariate process. Recently in our group, Kowarsch et al. (2010) generalized this concept to signaling data. Based on stationarity assumptions for networks they introduced the graphdelayed covariance and again, diagonalization yields an estimate for the separated signals. We continue the approach of Kowarsch et al. and provide a probabilistic source separation method for network data. Parts of

[^0]
[^0]:    Institute of Computational Biology, Helmholtz Zentrum München, German Research Center for Environmental Health, Neuherberg, Germany; and Institute for Mathematical Sciences. Technische Universität München, Munich, Germany.

this method have been introduced in our earlier papers (Illner et al., 2012; 2014) but with a focus on the application to gene expression data.

The main idea is to describe the unknown signals in terms of a Bayesian network. This concept is well known for the modeling of regulatory systems. Friedman et al. (2000) and Imoto et al. (2002) used Bayesian networks to describe the dependence and interaction of genes involved in the cell cycle. In this work, we assume Gaussian random variables and a linear dependence between the variables. The strength of dependence is parameterized by the graph-delayed covariance, and we learn the mixing parameters in a Bayesian framework. The resulting algorithm is called emGrade (expectation-maximization graphdecorrelation algorithm), and in simulations with network data it leads to improved estimation results compared to other BSS algorithms. A drawback of our approach is relatively specific assumptions on the stochastic properties of the signals; on the other hand, we benefit from Bayesian modeling. Using model selection criteria we can determine the correct number of unknown source signals and identify the most appropriate network structure of these signals. Throughout the article we use bold symbols to denote random variables and solid symbols to denote parameters and realizations of random variables.

# 2. STATISTICAL MODEL FOR DATA WITH NETWORK STRUCTURE 

The signals we are interested in are associated with some known network structure. More precisely, the information of a signal propagates along the edges of the network. In the following, we assume a directed acyclic graph and define the distribution of the signals in terms of a Bayesian network.

### 2.1. A stationary Gaussian model

Let $G=(V, E)$ be a directed acyclic graph, with $V=\left\{v_{i} \mid i=1, \ldots, N\right\}$ the set of nodes and $E \subset V \times V$ the set of edges. The nodes are ordered in a way such that for each node $v_{i}$ all parent nodes have indices lower than $i$. Let $p a_{i}=\left(j_{1}<\ldots<j_{n_{i}}\right)$ index all parent nodes of $v_{i}$, and we assume that $v_{1}, \ldots, v_{n_{0}-1}$ are the root nodes of the graph, that is, $p a_{i}=\emptyset$ for $i<n_{0}$.

The associated Bayesian network (Lauritzen, 1996) is then given by a set of random variables $\boldsymbol{S}=(\boldsymbol{s}(i))_{i=1}^{N}$ such that the joint distribution decomposes as

$$
\mathrm{p}(\boldsymbol{S})=\prod_{i=n_{0}}^{N} \mathrm{p}(\boldsymbol{s}(i) \mid \mathbf{P a}(i)) \prod_{i=1}^{n_{0}-1} \mathrm{p}(\boldsymbol{s}(i))
$$

Here, $\mathbf{P a}(i)=\left(\boldsymbol{s}\left(j_{1}\right)^{\prime}, \ldots, \boldsymbol{s}\left(j_{n_{i}}\right)^{\prime}\right)^{\prime}$ with $j_{1}<\ldots<j_{n_{i}}$ denotes the vector of all random variables associated with the parent nodes of $v_{i}$.

From now we assume Gaussian random variables $(\boldsymbol{s}(i))_{i=1}^{N}$ with state space $\mathbb{R}^{q}$. We further assign edge weights $\lambda_{i j} \in \mathbb{R}$ to all edges $e_{i j} \in E$, and we denote the resulting weighted graph by $G_{\Lambda}=(V, E, \Lambda)$. Let $\boldsymbol{s}(i)$ and $\boldsymbol{s}(j)$ be random variables associated with adjacent nodes of the graph. We make the following stationarity (and scaling) assumptions:

$$
\begin{aligned}
& (\mathrm{A} 1) \mathbb{E}[\boldsymbol{s}(i)]=0_{q} \\
& (\mathrm{~A} 2) \operatorname{Cov}(\boldsymbol{s}(i), \boldsymbol{s}(i))=I_{q} \\
& (\mathrm{~A} 3) \operatorname{Cov}(\boldsymbol{s}(i), \boldsymbol{s}(j))=\lambda_{i j} D
\end{aligned}
$$

The parameter $D$ is constant over the network, and we call it the graph-delayed covariance of the stationary Gaussian model. According to our actual purpose of source separation, we assume that $D=\operatorname{diag}\left(d_{1}, \ldots, d_{q}\right)$ is a diagonal matrix. The larger an entry $d_{i}$ the larger is the (absolute) value of the covariance between two adjacent random variables in the $i$ th component.

With (A1)-(A3) and the decomposition of $\mathrm{p}(\boldsymbol{S})$ in Equation (1), all conditional distributions are uniquely defined, and we get

$$
\boldsymbol{s}(i) \mid \mathbf{P a}(i)- \begin{cases}\mathcal{N}\left(0_{q}, I_{q}\right) & \text { if } \mathbf{P a}(i)=\emptyset \\ \mathcal{N}\left(\omega_{D}(i) \mathbf{P a}(i), \Sigma_{D}(i)\right) & \text { otherwise }\end{cases}
$$

where $\omega_{D}(i) \in \mathbb{R}^{q \times q n_{i}}$ and $\Sigma_{D}(i) \in \mathbb{R}^{q \times q}$ depend only on the graph-delayed covariance $D$. If $D$ is diagonal we have that $\Sigma_{D}(i)$ is also diagonal and $\omega_{\mathrm{D}}(i)$ consists of blocks of diagonal matrices. Dependent on the

weighted graph $G_{\Lambda}$ one can determine an interval $I^{G} \subseteq \mathbb{R}$ such that all covariance matrices $\Sigma_{D}(i)$ are positive definite for diagonal $D$ with components in $I^{G}$. We refer to the Gaussian distribution $\mathrm{p}(\boldsymbol{S})$ defined (1) in Equations and (2) as source model $\mathcal{M}\left(G_{\Lambda}, q\right)$, where $q$ is the dimension of the random variables. The distribution is parameterized by the graph-delayed covariance $D$, and if samples from $\mathcal{M}\left(G_{\Lambda}, q\right)$ are given, the maximum likelihood approach naturally yields an estimate $\hat{D}^{\mathrm{ML}}$.

The concept of a graph-delayed covariance was originally introduced by Kowarsch et al. (2010). We now shortly review their definition. For a weighted directed graph $G_{\mathcal{K}}=(V, E, \mathcal{K})$ with weights $\kappa_{i j} \in \mathbb{R}$ and associated random variables $\boldsymbol{S}=(\boldsymbol{s}(i))_{i=1}^{N}$, they considered the covariance between a node and the weighted sum of its parent nodes as

$$
D^{\mathrm{Pa}}=\operatorname{Cov}\left(\sum_{i \in p o_{j}} \kappa_{i j} \boldsymbol{s}(i), \boldsymbol{s}(j)\right)
$$

and they assumed that it is independent of the index $j$. For $\kappa_{i j}=\left(|\mathbf{P a}(j)| \lambda_{i j}\right)^{-1}$ with $\lambda_{i j}$ from above we have $D^{\mathrm{Pa}}=D$, where $D$ is the graph-delayed covariance in the stationary Gaussian model. To estimate $D^{\mathrm{Pa}}$ from samples $s(1), \ldots, s(N)$ they introduced

$$
\hat{D}^{\mathrm{Pa}}=\frac{1}{N-n_{0}-1} \sum_{j=n_{0}}^{N} \sum_{i \in p o_{j}} \kappa_{i j} s(i) s(j)^{i}
$$

where $n_{0}, \ldots, N$ are all indices of nonroot nodes. According to assumption (A3), we actually have more detailed information about the covariance between adjacent variables. We therefore additionally consider the following refined edge-based estimate:

$$
\hat{D}^{\mathrm{E}}=\frac{1}{|E|-1} \sum_{(i, j) \in E} \frac{1}{\lambda_{i j}} s(i) s(j)^{i}
$$

Both estimates $\hat{D}^{\mathrm{Pa}}$ and $\hat{D}^{\mathrm{E}}$ yield nonprobabilistic algorithms to separate network data-Grade (Pa) and Grade (E). The former is the original method from Kowarsch et al. (2010), and in section 4.2 we shortly introduce both algorithms for estimation comparison.

# 2.2. Graph models for simulations 

To illustrate the covariance structure of the stationary Gaussian model we introduce three graph models. All graphs are related to biological networks, or to time-series for comparison. In section 4 we again consider these graph models in our simulations about source separation.
(CC) Cell-cycle: The estimated network for the cell-cycle pathway based on gene expression data (Imoto et al., 2002). The network consists of 81 nodes and 84 edges.
(TF) Transcription factors: Three hub nodes and each directly signals on a subset of nodes.
(LL) Line signals: Similar to time-series, we define a network that consists of two line signals sharing the middle part, and one separated line signal.

Figure 1 illustrates these networks together with the associated covariance structure, and we randomly assigned weights $\pm 1$ to the edges. Note that one can theoretically consider any weights $\lambda_{i j} \in \mathbb{R}$.

## 3. A Blind Source Separation Model for Mixed Network Data

In blind source separation (BSS) we assume that we observe a linear mixture of the actual signals of interest. The aim is to estimate the mixing as well as the underlying signals. In the following we derive a new blind source separation method for network data and decribe the unobserved (latent) signals in terms of the source model from the last section.

### 3.1. Linear Mixing Model

We consider the following mixing model: $\boldsymbol{X}=(\boldsymbol{x}(i))_{i=1}^{N}$ are observed Gaussian variables with state space $\mathbb{R}^{m}$, and we assume latent Gaussian variables $\boldsymbol{S}=(\boldsymbol{s}(i))_{i=1}^{N}$ with state space $\mathbb{R}^{q}(q \leq m)$, such that each variable $\boldsymbol{x}(i)$ is a linear mixture of the components of the latent variable $\boldsymbol{s}(i)$ :

![img-0.jpeg](img-0.jpeg)

FIG. 1. Graph models and covariance structure. The upper graphics illustrate a connected subnetwork of cell-cycle (CC), transcription factors (TF), and lines (LL). Darker nodes indicate root nodes, and we randomly assigned edge weights with values +1 (black) and -1 (red). The lower graphics show the covariance structure associated with each graph model for one-dimensional random variables. The graph-delayed covariance was set to $D=0.6$.

$$
\boldsymbol{x}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon(i), \quad i=1, \ldots, N
$$

Here, $\varepsilon(i)$ is additive noise distributed as $\varepsilon(i) \sim \mathcal{N}\left(0, \sigma^{2} I_{m}\right)$ and independent of the latent variables. $A \in \mathbb{R}^{m \times q}$ denotes the mixing matrix and $\mu \in \mathbb{R}^{m}$ is a constant mean vector for all $\boldsymbol{x}(i)$. We refer to the components of the latent variables as sources, that is, for $k=1, \ldots, q$ we have a source $\boldsymbol{s}_{k}=\left(\boldsymbol{s}_{k}(i)\right)_{i=1}^{N}$.

We now extend the Bayesian network from section 2.1. Let $\boldsymbol{S}$ be latent variables, and the dependence is given by a weighted graph $G_{\Lambda}=(V, E, \Lambda)$ as before. We additionally introduce observed variables $\boldsymbol{X}$, where $\boldsymbol{x}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon(i)$ for all $i$. The joint distribution of $\boldsymbol{X}$ and $\boldsymbol{S}$ then decomposes as

$$
\mathrm{p}(\boldsymbol{X}, \boldsymbol{S})=\prod_{i=1}^{N} \mathrm{p}(\boldsymbol{x}(i) \mid \boldsymbol{s}(i)) \prod_{i=n_{0}}^{N} \mathrm{p}(\boldsymbol{s}(i) \mid \mathbf{P a}(i)) \prod_{i=1}^{n_{0}-1} \mathrm{p}(\boldsymbol{s}(i))
$$

where $\boldsymbol{x}(i) \mid \boldsymbol{s}(i) \sim \mathcal{N}\left(A \boldsymbol{s}(i)+\mu, \sigma^{2} I_{m}\right)$ directly follows from the linear mixing. A graphical representation of this latent variable model is given in Figure 2a.

# 3.2. Parameter inference using expectation maximization 

The unknown components of our model are the parameters $\theta=(A, \mu, \sigma, D)$ and the latent variables $\boldsymbol{S}$, and we are interested in both. A widely used approach for latent variable models is expectation maximization (McLachlan and Krishnan, 2007); that is, parameters and latent variables are updated alternately and each update improves the data $\log$-likelihood $\ell(\theta ; \boldsymbol{X})=\ln \mathrm{p}(\boldsymbol{X} \mid \theta)$.

For expectation maximization we need to consider the complete data $\log$-likelihood $\ell_{c}(\theta ; \boldsymbol{X}, \boldsymbol{S})=$ $\ln \mathrm{p}(\boldsymbol{X}, \boldsymbol{S} \mid \theta)$. Let $\mathbb{E}_{S \mid X, \theta}[.]$ denote the expectation with respect to the posterior distribution $\boldsymbol{S} \mid \boldsymbol{X}, \theta$ of the latent variables $\boldsymbol{S}$ given the observable variables $\boldsymbol{X}$ and parameters $\theta$. The expectation of the complete data $\log$-likelihood is then given by

$$
\mathbb{E}_{S \mid X, \theta}[\ln \mathrm{p}(\boldsymbol{X}, \boldsymbol{S} \mid \theta)]=\mathbb{E}_{S \mid X, \theta}\left[\ln \mathrm{p}\left(\boldsymbol{X} \mid \boldsymbol{S}, A, \mu, \sigma^{2}\right)\right]+\mathbb{E}_{S \mid X, \theta}[\ln \mathrm{p}(\boldsymbol{S} \mid D)]
$$

![img-1.jpeg](img-1.jpeg)

FIG. 2. Graphical representation of emGrade. Panel (a) shows the basic model with one observed variable $\boldsymbol{x}(i)=A \boldsymbol{s}(i)$ $+\mu+\alpha i$ ) for all indices $i$. In Panel (b) we take into account multiple and/or missing observations. For all indices $i$ we either have multiple observed variables $\boldsymbol{x}^{\prime}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon^{\prime}(i)$ with $r=1, \ldots, r_{i}$, or a latent variable $\boldsymbol{x}^{\prime \prime}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon^{\prime \prime}(i)$ when the observation for index $i$ is missing. In both figures the observed part is shown in purple and the latent part in red.

For better readability we use the notations $A_{\mu}=(A, \mu)$ and $\boldsymbol{s}_{*}(i)=\left(\boldsymbol{s}(i)^{\prime}, 1\right)^{\prime}$ —both enlarged by a constant component. We then have:

$$
\begin{aligned}
\mathbb{E}_{S \mid X, 0}\left[\ln \mathrm{p}\left(\boldsymbol{X} \mid \boldsymbol{S}, A, \mu, \sigma^{2}\right)\right]= & -\frac{N m}{2} \ln (2 \pi)-\frac{N m}{2} \ln \left(\sigma^{2}\right) \\
& -\frac{1}{2 \sigma^{2}} \sum_{i=1}^{N}\left[\operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[\boldsymbol{x}(i) \boldsymbol{x}(i)^{\prime}\right]\right)\right. \\
& -2 \operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[\boldsymbol{s}_{*}(i) \boldsymbol{x}(i)^{\prime}\right] A_{\mu}\right) \\
& \left.+\operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[\boldsymbol{s}_{*}(i) \boldsymbol{s}_{*}(i)^{\prime}\right] A_{\mu}^{\prime} A_{\mu}\right)\right] \\
\mathbb{E}_{S \mid X, 0}[\ln \mathrm{p}(\boldsymbol{S} \mid D)= & -\frac{N q}{2} \ln (2 \pi)-\sum_{i=n_{0}}^{N} \ln \left(\operatorname{det}\left(\Sigma_{D}(i)\right)\right) \\
& -\frac{1}{2} \sum_{i=n_{0}}^{N}\left[\operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[s(i) s(i)^{\prime}\right] \Sigma_{D}(i)^{-1}\right)\right. \\
& -2 \operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[s(i) \mathbf{P a}(i)^{\prime}\right] \Sigma_{D}(i)^{-1} \omega_{D}(i)\right) \\
& \left.+\operatorname{Tr}\left(\mathbb{E}_{S \mid X, 0}\left[\mathbf{P a}(i) \mathbf{P a}(i)^{\prime}\right] \omega_{D}(i)^{\prime} \Sigma_{D}(i)^{-1} \omega_{D}(i)\right)\right] \\
& -\frac{1}{2} \sum_{i=1}^{n_{0}-1} \mathbb{E}_{S \mid X, 0}\left[s(i) s(i)^{\prime}\right]
\end{aligned}
$$

The EM-algorithm consists of two steps that are repeated alternately until convergence. In the E-step, we determine the posterior distribution of the latent variables which yields the expectations in (9) and (10). Here, we use the well-known property $\mathbb{E}\left[\boldsymbol{z}_{1} \boldsymbol{z}_{2}^{\prime}\right]=\operatorname{Cov}\left(\boldsymbol{z}_{1}, \boldsymbol{z}_{2}\right)+\mathbb{E}\left[\boldsymbol{z}_{1}\right] \mathbb{E}\left[\boldsymbol{z}_{2}\right]^{\prime}$ for random variables $z_{1}$ and $z_{2}$. If $\boldsymbol{z}_{2}$ or both variables are observed, the l.h.s. equals $\mathbb{E}\left[\boldsymbol{z}_{1}\right] \boldsymbol{z}_{2}^{\prime}$ and $\boldsymbol{z}_{1} \boldsymbol{z}_{2}^{\prime}$, respectively. To get these posterior estimates we use the junction tree algorithm implemented in the Bayes net toolbox for Matlab (Murphy et al., 2001). In the $M$-step, we maximize $\mathbb{E}_{S \mid X, 0}[\ln \mathrm{p}(\boldsymbol{X}, \boldsymbol{S})]$ with respect to the parameters. Due to our specific stationarity assumptions the toolbox is not applicable for parameter maximization. Let $\operatorname{Esx}=\sum_{i=1}^{N} \mathbb{E}_{S \mid X, 0}\left[s_{*}(i) \boldsymbol{x}(i)^{\prime}\right]$ and we define Ess and Exx accordingly. We have the following updates

$$
\begin{aligned}
A_{\mu} & =(\operatorname{Esx})^{\prime}(\operatorname{Esx})^{-1} \\
\sigma^{2} & =\frac{1}{N m}\left[\operatorname{Tr}(\operatorname{Exx})-2 \operatorname{Tr}\left(\operatorname{Esx} A_{\mu}\right)+\operatorname{Tr}\left(\operatorname{Ess} A_{\mu}^{\prime} A_{\mu}\right)\right] \\
D & =\text { numerical maximization }
\end{aligned}
$$

The parameter updates for $A, \mu$ (in form of $A_{\mu}$ ), and $\sigma^{2}$ can be derived directly from (9). The parameter $D$ occurs as different rational terms in all $\omega_{D}(i)$ and $\Sigma_{D}(i)$. For all source models $\mathcal{M}(G)$, with $G$ a weighted graph, one can theoretically derive formulas for the update of $D$. Since we consider many different graph models in our simulations (regarding structure, number of nodes, and egde weights), we use numerical maximization and do not provide explicit update formulas for $D$. The search space is given by the interval $f^{G}$, and since $D$, as well as $\omega_{D}(i)$ and $\Sigma_{D}(i)$, are (block-)diagonal we can maximize $\mathbb{E}_{S \mid X, \theta}[\ln \mathrm{p}(\boldsymbol{S})]$ with respect to each component of $D$ separately.

The proposed expectation-maximization scheme for the linear mixing model from section 3.1 provides a method to separate network data. Similarly to the separation assumptions of Grade (graph-decorrelation algorithm) we assume a diagonal matrix $D$, and we therefore call the new algorithm emGrade (expectation-maximization graph-decorrelation algorithm).

# 3.3. Repeated and missing observations 

In a Bayesian network a random variable is either latent or observed. To take into account repeated and/or missing observations we redefine the graphical structure in Figure 2a. In addition to the latent variables $\boldsymbol{S}$ we introduce a latent variable $\boldsymbol{x}^{0}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon^{0}(i)$ if the observation at index $i$ is missing, and we introduce observed variables $\boldsymbol{x}^{r}(i)=A \boldsymbol{s}(i)+\mu+\varepsilon^{r}(i)$ for $r=1, \ldots, r_{i}$ if we have $r_{i}$ observations for index $i$ (Fig. 2b):

$$
\begin{gathered}
\boldsymbol{X}^{0}=\left\{\boldsymbol{x}^{0}(i) \mid \text { no observations at index } i\right\} \\
\boldsymbol{X}=\left\{\boldsymbol{x}^{1}(i), \ldots, \boldsymbol{x}^{r_{i}}(i) \mid r_{i} \text { observations at index } i\right\}
\end{gathered}
$$

In the E-step we infer $\boldsymbol{S}$ and $\boldsymbol{X}^{0}$ from the posterior distribution $\boldsymbol{S}, \boldsymbol{X}^{0} \mid \boldsymbol{X}, \theta$. The expectation of the complete data log-likelihood decomposes into

$$
\mathbb{E}_{S, X^{0} \mid X, \theta}\left[\ln \mathrm{p}\left(\boldsymbol{X}, \boldsymbol{X}^{0}, \boldsymbol{S}\right)\right]=\mathbb{E}_{S, X^{0} \mid X, \theta}\left[\ln \mathrm{p}\left(\boldsymbol{X}, \boldsymbol{X}^{0} \mid \boldsymbol{S}\right)\right]+\mathbb{E}_{S, X^{0} \mid X, \theta}[\ln \mathrm{p}(\boldsymbol{S})]
$$

In the following we investigate the impact of repeated and/or missing observations on the predictive power of the latent variable model. We assign the true parameters $\theta=(A, \mu, \sigma, D)$ to the model and infer source signals (E-step) from the posterior expectation $\mathbb{E}_{S \mid X, \theta}[\ln \mathrm{p}(\boldsymbol{X}, \boldsymbol{S} \mid \theta)]$. We then compare estimated and true source signals dependent on the number of repeated and/or missing observation values and dependent on the variance of the observation noise. As a distance measure we use

$$
\operatorname{dist}(\hat{S}, S)=\frac{1}{\sqrt{q N}}\|\hat{S}-S\|_{F}
$$

where $\left\|.\right\|_{F}$ denotes the Frobenius norm of a matrix. In Figure 3 we generated data from model (CC) with weights +1 and random parameters $\theta=\left(A, \mu, \sigma^{2} D\right)$. Expectedly, we find a better source recovery if we have many repeated and no missing observations as well as a low noise level. The performance also increases if the dimension of the latent variables is smaller than the dimension of the observed variables (A-B), and disregarding the graph structure of the observations yields a worse performance (C). For the other graph models, (TF) and (LL), the results are similar.

### 3.4. Separation of subnetworks

Until now we assumed one $q$-dimensional source model $\mathcal{M}(G, q)$ to jointly model all source signals $\boldsymbol{s}_{k}=\left(\boldsymbol{s}_{k}(i)\right)_{i=1}^{N}$ for $k=1, \ldots, q$. If we have more detailed information about single components (pathways) of a larger network, and we want to separate the data according to these subnetworks, we can model the distribution of each source signal separately. Let therefore $P_{1}, \ldots, P_{q}$ be weighted graphs on the same set of nodes. For each source we consider the one-dimensional source model $\mathcal{M}\left(P_{i}, 1\right)$ with graph-delayed covariance $d_{i} \in \mathbb{R}$. We then assume that the joint distribution of $S$ decomposes as

$$
\mathrm{p}(\boldsymbol{S})=\prod_{k=1}^{q} \mathrm{p}\left(\boldsymbol{s}_{k}\right)=\prod_{k=1}^{q} \prod_{i=1}^{N} \mathrm{p}\left(\boldsymbol{s}_{k}(i) \mid \mathbf{P a}_{k}(i)\right)
$$

We denote this source model based on $q$ different pathways as $\mathcal{M}\left(P_{1}, \ldots, P_{q}\right)$. If all pathways are identical (i.e., $P_{i}=G$ for all $i$ ), the above definition yields the original source model $\mathcal{M}(G, q)$ with diagonal graphdelayed covariance $D \in \mathbb{R}^{q \times q}$. The new definition only effects the expectation step; in the graphical

![img-2.jpeg](img-2.jpeg)

FIG. 3. Source recovery from repeated observations with missing values and observation noise. We generate repeated data from model (CC). In the upper plots we then ignore up to 20 observed variables (missing values), and in the bottom plots we add noise from $\mathcal{N}\left(0, \sigma^{2}\right)$ for $\sigma^{2}=0.1,0.3,0.5, \ldots, 1.0$ to all entries. We infer the source signals from the posterior distribution, where the data and the true parameters are given. The plots show the mean difference over 100 runs between the original source signals and the estimates. In (A) we fix the dimensions at $m=4$ (observed variables) and $q=2$ (latent variables), in (B) we have $m=q=3$. In (C) for comparison, we disregard the structure of the data and consider a network without edges for source estimation.
representation we split the node for $s(i)$ into $q$ nodes representing the one-dimensional random variables $s_{1}(i), \ldots, s_{q}(i)$ for $i=1, \ldots, N$. Again, the junction tree algorithm provides posterior estimates of the latent variables $\boldsymbol{S}$. In the last section we use this proper source modeling to identify pathways that are most likely present in the data.

# 4. PERFORMANCE AND FEATURES OF EMGRADE 

In this part we evaluate the performance of emGrade and demonstrate some gains from the Bayesian modeling-we introduce a family of information criteria to determine number and structure of the unknown source signals. For all simulations we consider the graph models from section 2.2 and fix the egde weights at +1 .

### 4.1. Convergence of emGrade

We define convergence in terms of changes in the single parameter estimates rather than changes in the log-likelihood function. This approach was suggested in Abbi et al. (2008), since convergence of the single parameters usually requires more EM-iterations (when the same threshold is considered). We say that emGrade has converged if

$$
\forall i\left|\theta_{i}-\theta_{i}^{(\text {new })}\right|<10^{-8}
$$

with parameters $\theta=\left(A, \mu, \sigma^{2}, D\right)$. The current parameter values are then the estimation result, and we call a run nonconvergent if there is no convergence after 10,000 EM-iterations. To get an impression of the convergence behavior of emGrade we generated data from model (CC), and we considered different combinations of $m, q=1, \ldots, 5$ (dimension of latent/observed variables). Figure 4 shows that for $q<m$ the

![img-3.jpeg](img-3.jpeg)

FIG. 4. Number of EM-iterations. We generate data from model (CC) and consider different combinations of $m, q=1, \ldots, 5$ (dimension of observed/latent variables). The plots show the mean number of EM-iterations among all convergent runs (left) and the number of nonconvergent runs (right). For all $m / q$-combinations with $q \geq m+2$ we performed 10 runs of emGrade.
mean number of EM-steps is small, and for $q>m$ or large dimensions $q=m$ the number of EM-steps explodes and many runs do not converge at all. In blind source separation applications we usually assume $q \leq m$, and we limit ourselves to such cases in the following.

# 4.2. Algorithm comparison 

We now compare emGrade to other blind source separation algorithms. The most similar algorithm regarding model assumptions is Grade, which diagonalizes the sample graph-delayed covariance using singular value decomposition. We distinguish between two versions-Grade (Pa) and Grade (E), where the graph-delayed covariance is estimated as $\hat{D}^{\mathrm{Pa}}$ and $\hat{D}^{\mathrm{E}}$ (section 2.1). We further consider algorithms for time-series data and simply resume the order of the random variables. AMUSE (Tong et al., 1990) and SOBI (Belouchrani et al., 1997) both assume stationarity (of the time-series), i.e. the autocovariance $\operatorname{Cov}(\boldsymbol{x}(i)$, $\boldsymbol{x}(i+\tau)$ ) is independent of the index $i$ at any lag $\tau \in \mathbb{Z}$. The algorithms then diagonalize sample autocovariances at one or multiple lags, respectively. Finally, we compare our results to PCA and fastICA (Hyvärinen and Oja, 2000), both act independently of the structure of the random variables.

All algorithms provide estimates of the mixing matrix and the source signals-but unlike emGrade they do not estimate the full parameter vector. $\theta=\left(A, \mu, \sigma^{2}, D\right)$. Instead of a likelihood-based evaluation of the performance we use the distance of estimated and true mixing matrix as performance measure:

$$
\operatorname{dist}(\hat{A}, A)=\min _{p \in \mathcal{P}} \frac{1}{\sqrt{m q}}\|\hat{A} P-A\|_{F}
$$

Let $\mathcal{P} \subseteq M$ at $(q, q)$ be the set of all $q \times q$ matrices with one nonzero entry per row and column and this entry has value $\pm 1$. With this we correct for possible permutation and sign-changing of the mixing columns. If $m$ dimensional data is given all algorithms-except emGrade-estimate a mixing matrix in $\operatorname{Mat}(m, m)$. In case of $q<m$ we only use the first $q$ columns of the mixing estimates. In Figure 5 we compare the estimation performance of all algorithms, and we fix the dimensions at $m=3$ and $q=2$. For all proposed graph models emGrade outperforms the other algorithms in terms of correctness of the estimates, the drawback is a much higher run-time. In the case of $m=q$ the improvement of the estimates is less apparent.

### 4.3. Pathway identification and number of source signals

We now take full advantage of the probabilistic modeling and use model selection criteria to determine the correct number of source signals and to identify active pathways in the network. Let $\mathcal{M}(G, q)$ denote the source model with $q$ source signals, and the joint distribution is based on a weighted graph $G$. We then consider the following information criterion:

![img-4.jpeg](img-4.jpeg)

FIG. 5. Algorithm comparison. The plots show the mean performance over 50 runs of the algorithms emGrade, Grade (G), Grade (E), AMUSE, SOBI (at lag 1 and at lags 1,2), PCA, and fastICA. In (A)-(C) we generated data from models (CC), (TF), and (LL) with $m=3$ and $q=2$. In this case ( $m>q$ ) emGrade yields the best estimation performance for all graph models. In (C) where $m=q=3$ the improvement compared to the other algorithms is smaller.

$$
\mathrm{IC}(\mathcal{M}(G, q))=-2 \ell(\theta ; X, \mathcal{M}(G, q))+k c
$$

where $k$ denotes the number of model parameters, and $c$ is some constant. For $c=2$ the above equation yields the Akaike information criterion (AIC) (Akaike, 1974) and for $c=\ln (N)$ the equation yields the Bayesian information criterion (BIC) (Schwarz, 1978) with $N$ the number of observed variables. To determine the true number of source signals we fix the graph $G$ and search for the lowest IC value among different source models. Since the comparison is based on the log-likelihood value of the emGrade estimates we use $\left|\ell(\theta ; \boldsymbol{X})-\ell\left(\theta^{(\text {new })} ; \boldsymbol{X}\right)\right|<10^{-6}$ as convergence criterion. In Figure 6 we generated data from model (CC) with $q=3$ the true number of source signals (dimension of the latent variables) and $m=3$, 4,5 observations (dimension of the observed variables). We then compare the IC values of $M(\hat{q})=$ $\mathcal{M}((C C), \hat{q})$ for $\hat{q}=1, \ldots, 5$, where we consider different constant values $c$. In case of $m>q$ we find a nearly perfect estimation of the true number of source signals for $c=2$ (AIC) and $c=\ln (N)$ (BIC).

For pathway identification we divide each network from section 2.2 into three pathways (subnetworks) $P_{1}, P_{2}$, and $P_{3}$. For (CC) we define the pathways as the three connected components of the complete cellcycle network, for (TF) we consider the single hub-nodes together with their target nodes as pathways, and for (LL) we consider the two overlapping lines and the additional line as pathways. We then generate data from the pathway source model $\mathcal{M}\left(P_{i}, P_{j}\right)$ introduced in section 3.4, and we determine the lowest IC value among all source models $M(i, j)=\mathcal{M}\left(P_{i}, P_{j}\right)$ for $i, j=1,2,3$. If the edges of the pathways are nonoverlapping [models (CC) and (TF)] we observe a good pathway identification; for model (LL) often only one pathway is identified correctly (Fig. 7).
![img-5.jpeg](img-5.jpeg)

FIG. 6. Estimation of the number of source signals. We generate data from model (CC) with $q=3$ source signals (dimension of the latent variables) and $m$-dimensional observations for $m=5,4,3$ in different colors. For the graphdelayed covariance we consider $D=[0.7,-0.49,0.3]$. The plots show the IC values of all source models $M(\hat{q})=\mathcal{M}((\mathrm{CC}), \hat{q})$ for increasing $\hat{q}=1, \ldots, 5$. In each plot we consider a different constant $c$. The black vertical lines show the true number of source signals and the dots indicate the selected source model in each comparison, that is, the model with the lowest IC value. Dashed lines lead to IC values of nonconvergent runs (using the log-likelihood value after 10,000 iterations), and some IC values are $+\infty$. IC, information criterion.

![img-6.jpeg](img-6.jpeg)

FIG. 7. Pathway identification. We generate $q=2$ source signals from the respective pathways $P_{1}$ and $P_{2}$ of the models (CC), (LL), and (TF). From observations of dimension $m=4,3$ (in different colors) we calculate the BIC of all pathway source models $M(i, j)=\mathcal{M}\left(P_{i}, P_{j}\right)$, where we assume source signals from pathways $P_{i}$ and $P_{j}(i, j=1,2,3)$. The black vertical lines show the true pathway combination, and the dots indicate the selected source model in each comparison, that is, the model with the lowest BIC value. BIC, Bayesian information criterion.

# 5. DISCUSSION AND CONCLUSION 

In this work we defined the distribution of signaling data in terms of a stationary Bayesian network with Gaussian random variables. Based on this definition, we proposed the probabilistic blind source separation algorithm emGrade to determine underlying signals of interest in a multivariate mixture. The iterative expectation maximization procedure for parameter and source inference achieved good convergence in small dimensions. Moreover, we were able to determine the true number of source signals and to identify the correct active pathways (subnetworks) in simulations. The separate modeling of each source signal according to different specific pathways might be seen as a key advantage of our method. In our ongoing work we consider gene expression data in which we assume that the observations consist of a mixture of biological processes. For different combinations of literature-derived pathways we compare the BIC values of our model. With this we want to determine the active processes and compare different data sets (e.g., treatment versus control) in terms of a change in the underlying processes. In addition, we want to biologically validate our method, that is, we want to show that the literature-derived network information yields an improved separation of the data. Here, we consider knock-down experiments in which a specific known pathway is not present in the knock-down data set. Using enrichment analysis to assign biological processes to the estimated source signals we can qualify the estimation performance of different BSS methods in a biological manner. With this we want to continue the findings from Kowarsch et al. (2010) and strengthen the relevance of network-based BSS methods in biological applications.

## ACKNOWLEDGMENTS

This work was financially supported by the German Federal Ministry of Education and Research (BMBF) within the GerontoSys project "Stromal Aging" (Grant No. FKZ 0315576C), the German Research Foundation (DFG) within the project InKoMBio (Grant No. BO 3834/1-1) and the European Union within the ERC grant "LatentCauses".

## AUTHOR DISCLOSURE STATEMENT

The authors declare that no competing financial interests exist.
