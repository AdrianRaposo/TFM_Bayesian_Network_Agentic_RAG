# HAL open science 

## An Infinite Multivariate Categorical Mixture Model for Self-Diagnosis of Telecommunication Networks

Amine Echraibi, Joachim Flocon-Cholet, Stéphane Gosselin, Sandrine Vaton

## To cite this version:

Amine Echraibi, Joachim Flocon-Cholet, Stéphane Gosselin, Sandrine Vaton. An Infinite Multivariate Categorical Mixture Model for Self-Diagnosis of Telecommunication Networks. ICIN 2020: 23rd Conference on Innovation in Clouds, Internet and Networks, Feb 2020, Paris, France. 10.1109/ICIN48450.2020.9059491 . hal-02431732v2

## HAL Id: hal-02431732 <br> https://hal.science/hal-02431732v2

Submitted on 3 Mar 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# An Infinite Multivariate Categorical Mixture Model for Self-Diagnosis of Telecommunication Networks 

Amine Echraibi, Joachim Flocon-Cholet, Stéphane Gosselin, Sandrine Vaton

## To cite this version:

Amine Echraibi, Joachim Flocon-Cholet, Stéphane Gosselin, Sandrine Vaton. An Infinite Multivariate Categorical Mixture Model for Self-Diagnosis of Telecommunication Networks. ICIN 2020: 23rd Conference on Innovation in Clouds, Internet and Networks, Feb 2020, Paris, France. hal-02431732v2

## HAL Id: hal-02431732 <br> https://hal.archives-ouvertes.fr/hal-02431732v2

Submitted on 3 Mar 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# An Infinite Multivariate Categorical Mixture Model for Self-Diagnosis of Telecommunication Networks 

Amine Echraibi, Joachim Flocon-Cholet, Stéphane Gosselin<br>Orange Labs<br>Lannion, France<br>\{amine.echraibi, joachim.floconcholet, stephane.gosselin\}@orange.com

Sandrine Vaton<br>IMT Atlantique<br>Brest, France<br>sandrine.vaton@imt-atlantique.fr


#### Abstract

The diagnosis of telecommunication networks remains a challenging task, mainly due to the large variety and volume of data from which the root causes have to be inferred. Expert systems, supervised machine learning, or Bayesian networks require expensive and time consuming data labeling or processing by experts. In this paper, we propose an Infinite Multivariate Categorical Mixture Model for clustering patterns of faults from data gathered from telecommunication networks. The model is able to automatically identify the number of clusters necessary to explain the data using the Dirichlet process prior. We show how to use Variational Inference to derive an Expectation-Maximization (EM) like algorithm to perform inference on the model. We apply our model on synthetic data generated from an expert Bayesian network of a Fiber-To-TheHome (FTTH) Gigabit capable Passive Optical Network (GPON). We show that the model discovers the patterns linked to the root causes of the faults with up to $96 \%$ accuracy in an unsupervised manner. We also apply our method on real data gathered from the FTTH network and the local area network and demonstrate how the model is able to identify known faults.


Index Terms-Infinite Mixture Models, Variational Inference, Self-Diagnosis, Access Network, Local Area Network, Pattern discovery

## I. INTRODUCTION

Identifying fault patterns in large telecommunication network and service infrastructures is a difficult t ask. M ost of the considered technical solutions rely either on rule based expert systems or hand crafted expert Bayesian networks [1]-[3]. Although these approaches have had tremendous success, one of the unsung drawbacks is the data processing and the expert knowledge required to build the diagnosis model or rules. For expert systems, for example, the rules created by the expert require knowledge of the existing fault and the identification of the variables describing the fault. This process requires data processing by hand by an expert of the domain, which is an expensive and time consuming task. Also, the maintenance of the model or rules in the long run can be a significant issue for operational teams.

Recently, machine learning techniques have been tremendously successful in the identification and the extraction of patterns in various domains. In the context of our problem, similar approaches can be used to identify patterns of faults from diagnosis data. This task is thus an unsupervised machine learning task, where labels are not available and obtaining them
is as complex as the data processing required to construct expert rules. However, unlike text data, the data gathered from various devices and services in the network is often structured in the form of a table, where each variable takes some range of values.

Clustering such data, gathered from telecommunication networks and services presents many challenges. The first and the main challenge is the unknown number of clusters of faults in the data. The second challenge is the types and multivariate nature of the data. The data is multi-dimensional and can contain categorical and continuous variables. Therefore, classical clustering algorithms where the number of clusters is to be set a priori require some form of model selection. Furthermore, classical approaches such as KMeans suppose a specific probability distribution for each cluster. These modeling assumptions, including the assumption on the number of clusters, can hurt the performance of the clustering when the data do not comply with such assumptions, which is often the case when dealing with real-world applications.

In this paper, we propose an infinite multivariate categorical mixture model to identify patterns of faults in an unsupervised setting, without any prior expert knowledge, and without the requirement to know a priori the number of different fault patterns. The model is based on the Dirichlet Process [4], which allows for learning the number of clusters from the data. However, the Dirichlet Process supposes an infinite number of clusters which translates to an intractable inference problem on the model. Our contributions are the following:

- We provide a theoretical formulation of the infinite multivariate categorical mixture model (section 2).
- We show how to perform approximate inference on the model, in order to extract the clusters from the data using Variational Inference [5] (section 3).
- We demonstrate how the model is able to identify root causes of faults in a synthetic dataset generated from a real-world expert Bayesian Network (section 4).
- We also demonstrate the clustering performance of the model on real operational data acquired from the Fixed Access Network and the Local Area Network (section 5).

Implementation of the model and synthetic data are available in: https://git.io/JejBQ

## II. The Infinite Categorical Mixture Model

## A. Notations

We introduce some notations that we will use throughout the paper. We denote by $X_{i}$ an observable random variable, describing a specific feature of a network equipment such as a status, an alarm or a physical metric. We consider only categorical random variables. Continuous variables such as optical powers or temperatures are discretized, using standard methods such as equal frequency or equal width discretization. Thus, each random variable takes values in $\operatorname{Val}\left(X_{i}\right)=\left\{v_{1 i}, \ldots, v_{\mid X_{i} \mid i}\right\}$, where $\left|X_{i}\right|$ is the number of modalities of variable $X_{i}$. We also note $\mathbb{P}\left[X_{i}=v\right]$ the probability that $X_{i}$ takes value $v$, and $\mathbb{E}\left[X_{i}\right]$ the expectation of $X_{i}$. Let $x_{1: N}$ represent $N$ samples of the vector $X=\left[X_{1}, \ldots, X_{d}\right]^{T}$ of dimension $d$. We denote by $z_{1: N} N$ random variables, where $z_{n}$ represents the diagnosis cluster of sample $x_{n}$. The Kullback-Leibler divergence between two probability distributions $q$ and $p$ is denoted by:

$$
\mathbb{D}_{K L}[q \| p]=\int q(x) \log \frac{q(x)}{p(x)} d x
$$

The entropy of a probability distribution $p$ is denoted by:

$$
\mathbb{H}[p]=-\int p(x) \log p(x) d x
$$

For discrete random variables integrals are replaced by discrete sums over the values taken by the random variable X . We denote by $\operatorname{Cat}(X \mid \pi)$ the categorical distribution of a random variable $X$ taking discrete values $\left\{x_{1}, \ldots, x_{m}\right\}$ with probabilities $\left\{\pi_{1}, \ldots, \pi_{m}\right\}$ :

$$
\operatorname{Cat}(X \mid \pi)=\prod_{k=1}^{m} \pi_{k}^{\mathbb{1}\left[X=x_{k}\right]} \quad \text { s.t } \quad \sum_{k} \pi_{k}=1
$$

where the indicator function $\mathbb{1}[\cdot]$ has a value of 1 if the bracketed condition is true and 0 otherwise. The categorical distribution is thus also defined by:

$$
\mathbb{P}\left[X=x_{k}\right]=\pi_{k} \quad \text { for all } k
$$

We denote by $\operatorname{Beta}(\beta ; 1, \eta)$ the beta distribution of parameters 1 and $\eta$, defined as:

$$
\operatorname{Beta}(\beta ; 1, \eta)=\mathrm{C}(1-\beta)^{\eta-1} \quad \text { C: normalizing constant }
$$

To simplify the notations, if a random variable $X$ has a probability distribution $p(x)$, we use the same lowercase notation $x$ for the random variable and its possible values, and simply write:

$$
x \sim p(\cdot)
$$

We denote by $x_{1: m}$ the vector of elements $\left\{x_{1}, \ldots, x_{m}\right\}$ and $x_{-i}$ the vector of all elements except the $i^{t h}$ index.

## B. The Dirichlet Process Prior

In a model-based clustering, one of the main challenges is to choose the correct number of clusters to analyze the data. In our case, the number of diagnosis clusters is unknown a priori. The Dirichlet Process (DP) [4] allows us to introduce a prior on the number of clusters, without fixing it explicitly. One way to construct the Dirichlet Process is via the stick-breaking construction [6], where $\eta$ is the concentration parameter of the DP $(\eta>0)$, and the weight $\pi_{k}$ of the $k^{t h}$ cluster is constructed from $k$ samples drawn from a beta distribution as follows:

$$
\begin{aligned}
& \beta_{k} \sim \operatorname{Beta}(\cdot ; 1, \eta) \\
& \pi_{k}=\beta_{k} \prod_{i=1}^{k-1}\left(1-\beta_{l}\right)
\end{aligned}
$$

The stick breaking construction is as follows, $\pi_{k}$ represents the length of the $k^{\text {th }}$ piece broken from a stick of length 1. If the concentration parameter is small, $\pi_{k}$ will be large (close to 1) at the first times the stick is broken, therefore the stick will be broken a small number of times (small number of clusters). If $\eta$ is large, $\pi_{k}$ will be small (close to 0 ) and the stick can be broken a large number of times (large number of clusters). The probability that the $(n+1)^{\text {th }}$ data point belongs to a new cluster $k^{*}$ or $K$ existing clusters is [7]:

$$
\mathbb{P}\left[z_{n+1}=z \mid z_{1: n}, \eta\right]=\frac{1}{\eta+n}\left[\eta \mathbb{1}\left[z=k^{*}\right]+\sum_{k=1}^{K} n_{k} \mathbb{1}[z=k]\right]
$$

where $n_{k}$ is the number of data points in cluster $k$. If $\eta \rightarrow \infty$ a new cluster would be created for each data point, and if $\eta \rightarrow 0$ all data points are concentrated in the first cluster. The intuition behind the Dirichlet process is the following: as the number of data points increases, we allow the number of clusters to grow according to the concentration parameter and the clusters already assigned. New samples are assigned to existing clusters if they match, otherwise a new cluster is created for them. Therefore the Dirichlet Process allows the mixture model to cluster the data and identify automatically the number of clusters necessary to explain the data.

## C. The Dirichlet Process Categorical Mixture Model (DPCMM)

Using the stick-breaking construction introduced in the previous section for the weights $\pi_{k}$ of the $k^{t h}$ cluster, the generative process for the model becomes:

$$
\begin{aligned}
z_{n} & \sim \operatorname{Cat}(\cdot \mid \pi)=\prod_{k=1}^{\infty} \pi_{k}^{\mathbb{1}\left[z_{n}=k\right]} \\
b_{k i} & \sim \operatorname{Dir}\left(\cdot ; \alpha_{i},\left|X_{i}\right|\right)=\prod_{v \in V a l\left(X_{i}\right)} b_{k, i, v}^{\alpha_{i v}-1} \\
& \text { s.t } \sum_{v \in V a l\left(X_{i}\right)} b_{k, i, v}=1 \\
x_{n i} \mid z_{n}=k, b & \sim \operatorname{Cat}\left(\cdot \mid b_{k i}\right)=\prod_{v \in V a l\left(X_{i}\right)} b_{k, i, v}^{\mathbb{1}\left[x_{n i}=v\right]}
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Graphical representation of the model in plate notation.

Figure 1 shows a graphical representation of the generative process of the model.

Based on the assignment of cluster $z_{n}$ a sample $x_{n i}$ is drawn based on the conditional probability distribution for variable $X_{i}$ taking a certain value $v$ under cluster $z_{n}=k$ :

$$
b_{k, i, v}=\mathbb{P}\left[x_{n i}=v \mid z_{n}=k\right]
$$

In the classical Bayesian formulation considered above, the parameters $b_{k, i}=\left[b_{k, i, v}\right]_{v \in V a l\left(X_{i}\right)}$ are themselves random variables with a conjugate prior, in this case a Dirichlet distribution with concentration parameter $\alpha_{i}$ for variable $X_{i}$. The concentration parameter allows us to inject prior knowledge about the modalities of variable $X_{i}$. $\alpha_{i v}$ thus represents a weight for modality $v$ in the Dirichlet distribution associated with variable $X_{i}$. In the case where no information is available we use an uninformative prior $\alpha_{i v} \propto \frac{1}{\left|X_{i}\right|}$.

In order to fit the model to the data and identify the clusters representing the different types of network failures, we need to compute or approximate the posterior distribution:

$$
p\left(z_{1: N}, b, \beta \mid x_{1: N}\right)=\frac{p\left(z_{1: N}, b, \beta, x_{1: N}\right)}{p\left(x_{1: N}\right)}
$$

Markov Chain Monte Carlo (MCMC) approaches are commonly used to fit such models [8]. The main idea behind these approaches is to run a Markov chain long enough (until convergence) where the stationary distribution at convergence is the posterior of interest as defined in equation (1). One major drawback of such approaches is the long burn-in time of the Markov chain that does not scale well with the number of dimensions of the data [9]. In a high dimensional space the Markov chain needs to visit a high number of states. The other drawback is that convergence of MCMC methods is hard to diagnose, due to the sampling issue in high dimensions. Although MCMC methods have had many successes in small scale problems, further research is required particularly for large scale applications.

Recently, an alternative approach emerged called Variational Inference [5], [7], [9]. The main idea behind the approach is to express the intractable inference problem as a relaxed optimization problem, where we can leverage all the tools available in the mathematical literature of optimization to solve the inference problem. In the next section, we present a brief review of variational inference, and we show how we can use it to approximate our posterior distribution of equation (1).

## III. VARIATIONAL INFERENCE

### A. Variational Inference and the mean field approximation

In order to introduce the variational inference approach, we denote by $\zeta_{1: m}=\left\{z_{1: N}, b, \beta\right\}$ the vector grouping all the hidden variables of the model. Solving the inference problem of the model amounts to determining $p\left(\zeta_{1: m} \mid x_{1: N}\right)$. As mentioned previously, close form solutions for this quantity can not be determined. Variational inference and the meanfield approximation allow us to approximate this intractable distribution by a set of distributions for which the inference is tractable, namely the mean field family. A distribution $q$ is said to be in the mean field family for variables $\zeta_{1: m}$, if it verifies:

$$
q\left(\zeta_{1: m}\right)=\prod_{l=1}^{m} q\left(\zeta_{l}\right)
$$

The main idea of variational inference is to approximate the intractable distribution (1), by finding the closest mean field family member in terms of Kullback-Leibler divergence i.e:

$$
q^{*}=\min _{q} \mathbb{D}_{K L}\left[q\left(\zeta_{1: m}\right) \| p\left(\zeta_{1: m} \mid x_{1: N}\right)\right]
$$

By exploiting the factorization in the mean field family, we can show that the solution $q^{*}$ verifies the following fixed point equations:

$$
\log q^{*}\left(\zeta_{l}\right)=\text { const }+\mathbb{E}_{\zeta_{-l} \sim q^{*}}\left[\log p\left(\zeta_{1: m}, x_{1: N}\right)\right] \quad \forall l
$$

For an explicit derivation of this criterion we refer the reader to [7]. In the case of our model, the mean-field family is defined as :

$$
q\left(z_{1: N}, b, \beta\right)=\prod_{n=1}^{N} q\left(z_{n}\right) \prod_{i=1}^{d} \prod_{k=1}^{T} q\left(b_{k, i}\right) \prod_{k=1}^{T} q\left(\beta_{k}\right)
$$

We also suppose that $q\left(\beta_{T}=1\right)=1$ hence $q\left(z_{n}>T\right)=0$, i.e the number of clusters is truncated to an upper bound on the true number of clusters [9]. A noteworthy aspect of this approach is that the true posterior given by (1) has an infinite number of factors, however the approximating distribution $q$ is constrained based on the previous conditions. Therefore, the true model is unchanged however the minimization problem is relaxed in order to be solved efficiently.

### B. Variational Inference for The DPCMM

By applying equation (2) to our Infinite Categorical Mixture Model, we obtain:

$$
\begin{aligned}
\log q^{*}\left(z_{n}\right) & =\text { const }+\mathbb{E}_{\left\{z_{-n}, \beta, b\right\} \sim q^{*}}\left[\log p\left(z_{1: N}, b, \beta, x_{1: N}\right)\right] \\
\log q^{*}\left(b_{k, i}\right) & =\text { const }+\mathbb{E}_{\left\{z_{1: N}, \beta, b_{-(k, i)}\right\} \sim q^{*}}\left[\log p\left(z_{1: N}, b, \beta, x_{1: N}\right)\right] \\
\log q^{*}\left(\beta_{k}\right) & =\text { const }+\mathbb{E}_{\left\{z_{1: N}, \beta_{-k}, b\right\} \sim q^{*}}\left[\log p\left(z_{1: N}, b, \beta, x_{1: N}\right)\right]
\end{aligned}
$$

And by substituting the expression of $p(z_{1:N},b,\beta,x_{1:N})$ resulting from the graphical representation of the model (Figure 1), we then deduce the following approximating distributions:

$$
\begin{aligned}
q^{*}\left(z_{n}\right) & =\operatorname{Cat}\left(z_{n} ; \phi_{n}\right) \\
q^{*}\left(b_{k, i}\right) & =\operatorname{Dir}\left(b_{k, i} ; \epsilon_{k, i},\left|X_{i}\right|\right) \\
q^{*}\left(\beta_{k}\right) & =\operatorname{Beta}\left(\beta_{k} ; \gamma_{1, k}, \gamma_{2, k}\right)
\end{aligned}
$$

And the mean field fixed point equations for the parameters are the following, where $\psi$ is the digamma function:

$$
\begin{aligned}
\log \phi_{n k} & =\text { const }+\sum_{i=1}^{d} \sum_{v \in V a l\left(X_{i}\right)} \mathbb{1}\left[x_{n i}=v\right]\left[\psi\left(\epsilon_{k, i, v}\right)\right. \\
& \left.-\quad \psi\left(\sum_{v^{\prime} \in V a l\left(X_{i}\right)} \epsilon_{k, i, v^{\prime}}\right)\right] \\
& +\psi\left(\gamma_{1, k}\right)-\psi\left(\gamma_{1, k}+\gamma_{2, k}\right) \\
& +\sum_{l=1}^{k-1}\left[\psi\left(\gamma_{2, l}\right)-\psi\left(\gamma_{1, l}+\gamma_{2, l}\right)\right] \quad \text { s.t } \quad \sum_{k=1}^{T} \phi_{n k}=1 \\
\gamma_{1, k} & =1+\sum_{n=1}^{N} \phi_{n k} \\
\gamma_{2, k} & =\eta+\sum_{n=1}^{N} \sum_{l=k+1}^{T} \phi_{n l} \\
\epsilon_{k, i, v} & =\alpha_{i, v}+\sum_{n=1}^{N} \phi_{n k} \mathbb{1}\left[x_{n i}=v\right]
\end{aligned}
$$

## C. Convergence and an Algorithm

In order to monitor convergence while iterating the fixed point equations, we can plot the evidence lower bound defined as:

$$
\begin{aligned}
\mathcal{L}(q) & =-\mathbb{D}_{K L}[q] \mid p\left(z_{1: N}, b, \beta, x_{1: N}\right)] \\
& =\mathbb{E}_{\left\{z_{1: N}, \beta, h\right\} \sim q}\left[\log p\left(z_{1: N}, b, \beta, x_{1: N}\right)\right]+\mathbb{H}[q]
\end{aligned}
$$

The mean field fixed point updates minimize $-\mathcal{L}(q)$, therefore across iterations the evidence lower bound should increase monotonically. Usually, we only evaluate the log predictive across iterations, which is the first term of $\mathcal{L}(q)$. This quantity is not guaranteed to increase monotonically. However, at convergence, this quantity reaches a plateau, and by evaluating convergence in this manner we can bypass the tedious calculation of different entropy terms in $\mathbb{H}[q]$.

Like the EM algorithm, the fixed point update equations only guarantee convergence to a local minimum depending on the initialization. Therefore, in order to converge to the best local minimum possible we need to initialize the parameters $\phi_{n}$ in the best way possible. One approach widely used for the initialization of mixture models is to initialize $\phi_{n}$ from a KMeans algorithm. Hence, given the centers of a fitted KMeans $\mu_{k}$ where we set the number of clusters to the upper bound $T$, we initialize $\phi_{n}$ as:

$$
\phi_{n k} \propto \exp \left(-\frac{1}{2}\left\|x_{n}-\mu_{k}\right\|\right)
$$

Algorithm 1 presents the inference process on the Dirichlet Process Categorical Mixture Model using variational inference. Similar to the EM Algorithm, we can recognize two steps in the iterative process: the update of the local variational parameters $\phi_{n}$ analogous to the E-step, and the update of the global variational parameters $\gamma_{1}, \gamma_{2}$, and $\epsilon$ analogous to the M-step.

```
Algorithm 1 Variational Inference for the DPCMM
    Input: \(x_{1: N}, T, \eta\)
    \(\left\{\mu_{k}\right\}_{k}=\operatorname{KMeans}\left(T, x_{1: N}\right)\)
    \(\phi_{n k}^{(0)} \propto \exp \left(-\frac{1}{2}\left\|x_{n}-\mu_{k}\right\|\right)\) \{Initialize \(\phi_{n} \forall k, \forall n\}
    \(\mathcal{L}^{(0)}=-\infty\)
    for \(t=1 \ldots \infty\) do
        Compute: \(\gamma_{1, k}^{(t)} \quad \forall k\) (5)
        Compute: \(\gamma_{2, k}^{(t)} \quad \forall k\) (6)
        Compute: \(\epsilon_{k, i, v}^{(t)} \quad \forall v, \forall k, \forall i\) (7)
        Compute: \(\phi_{n, k}^{(t)} \quad \forall n, \forall k\) (4)
        Compute \(\mathcal{L}^{(t)} \quad(8)\)
        if \(\left|\frac{\mathcal{L}^{(t)}-\mathcal{L}^{(t-1)}}{\mathcal{L}^{(t)}}\right| \leq 10^{-6}\) then
            break
            end if
    end for
    \(z_{n}=\underset{k}{\arg \max } \phi_{n k} \quad \forall n\)
    return \(z_{1: N}, \phi\)
```

IV. AsSESSMENT ON SYntHETIC DATA GENERATED BY AN Expert BAYESIAN NetWORK FOR FTTH DiAGNOSIS

## A. Experiment and Dataset

![img-1.jpeg](img-1.jpeg)

Fig. 3. FTTH GPON Architecture [1].

In this first experiment we assess our clustering model for the FTTH fault diagnosis. We reuse the work done by Tembo et al. [1] where the authors designed an expert Bayesian network that reflects the behaviour of a real GPON network (Figure 3). The Bayesian network is depicted on Figure 2 where the colored top nodes represent the root causes and the other nodes the observations coming from the network. Note here that the Bayesian network is only used to generate a synthetic dataset

![img-2.jpeg](img-2.jpeg)

Fig. 2. Expert Bayesian Network of the FTTH GPON [1]. Colored nodes are possible root causes whereas non-colored nodes are observations.

similar to operational data, it is not used in the clustering method assessed in this paper. The goal here is to see if our clustering model is able to automatically detect the patterns corresponding to the different root causes.

In order to generate the synthetic data for the experiment, we simulate a fault by activating the root cause for the fault, and we sample the visible variables. Here we sampled 6 uncorrelated faults (for more details on the expert bayesian network and remaining variables, we refer the reader to [1]):

- **AltONT:** highlights a problem with the power supply of the optical network termination (ONT). This hidden variable controls the current of the ONT *IONT*, the Dying Gasp alarm *DG*, and the electric voltage of the ONT *VONT*.
- **AltOLT:** describes a problem with the power supply of the optical line termination (OLT). It controls similar variables for the OLT, *VOLT* and *IOLT*.
- **FaultyONT:** denotes whether the ONT is faulty, and symbolizes the global state for an ONT. It controls the alarms TIA (Transmission Interference Alarm), DOW (Drift Of Windows), and SF (Signal Fail) or SD (Signal Degraded).
- **FiberDB:** represents the state of the drop optical fiber and controls *RxONT* the power at which the ONT receives the signal.
- **IOS:** (Image Operating System) refers to an incompatibility between the OS of an OLT and the OS of an ONT. It controls the variable *SWV* describing the software version alarm.
- **TcOLT:** represents the temperature of the OLT.

We sampled 150 data points for each fault, using the likelihood weighted sampling method, based on the conditional distribution tables of each observation given the root cause. Therefore we generate for each fault a pattern of the visible variables for a specific customer equipment (ONT). The resulting dataset contains 900 samples, where each sample presents a realisation of the 29 visible nodes of the Bayesian network. These visible nodes are referred to in our modeling by *X<sup>i</sup>*.

### *B. Evaluation Process and Results*

In order to demonstrate the value of the Dirichlet Process prior, we suppose that the number of faults is unknown, similarly to many real-world applications. As discussed in section III-A we evaluate our model with a truncation level *T* = 50 which represents an upper bound of the true number of clusters (here *K* = 6). The algorithm will build up to 50 clusters but will automatically keep the main relevant clusters. We set the concentration parameter of the Dirichlet process to *η* = 0.001. We run our model on the generated dataset multiple times and we plot the evidence lower bound defined in equation (8) in Figure 4.

The evaluation metric is the clustering accuracy. It is similar to the classification accuracy, however, in the clustering task the clusters are not identifiable with the labels, i.e the clusters can change from one run of the algorithm to another. Therefore we need to test all possible combinations and choose the best one. The clustering accuracy is defined as [10]:

$$
\text{ACC} = \max\_{m \in \mathcal{M}} \frac{\sum\_{n=1}^{N} \mathbb{1}\left[ l\_{n} = m(z\_{n}) \right]}{N}
$$

where *z<sub>n</sub>* is the cluster assignment, *l<sub>n</sub>* the true label and *M* the set of all possible one-to-one mappings.

The best run of the model was selected as the run with highest evidence lower bound (Experiment 6). It corresponds to a clustering accuracy of **0.96** as seen on the table I. We note that a comparison can be made between our model and a classical clustering algorithm such as KMeans, for which we have to set the number of clusters to the true unknown number of clusters (K=6). The KMeans algorithm has similar performance to our model in this case. However, our model

![img-3.jpeg](img-3.jpeg)

Fig. 4. The evidence lower bound for different runs of the algorithm.


TABLE I Clustering accuracy for the best model bypasses the constraint of choosing K a priori. The confusion matrix between the clusters and true labels in table II shows 6 non-empty clusters, are learned without fixing K .


TABLE II Confusion Matrix.

The confusion matrix in table II shows that each of the main clusters found by the clustering model corresponds clearly to a particular root cause, with up to $3.2 \%$ error. The Dirichlet process automatically identifies the main patterns and clusters them in 6 clusters corresponding to the true clusters. The other clusters remain empty. It shows that the number of clusters is automatically and solely estimated from the data.

## V. Extraction of Patterns of Faults in The Fixed Access Network and the Local Area Network

In this second experiment, we apply our clustering model on real operational network data. However in this setup we don't have access to a ground truth so the aim of this experiment is to demonstrate the benefit of our clustering model in a data exploration process.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Network scope for fault pattern extraction from real operational data

## A. Data Collection and Network Scope

We place our working environment on the FTTH GPON fixed access network and the local area network as represented in Figure 5. For the fixed access network we collected data describing the status of the OLT, and the status of the ONT (olt_status, ont_status, ont_download_status). For the local area network, we collected data describing the status of the router and the different services provided such as, IPTV, VOD (Video On Demand) and VOIP. We also collected data describing the account status of the client. The final dataset contains about 7000 clients who claimed to have a problem with one of their services. For each client we collect 29 variables reflecting the different aspects of the environment as described previously.

## B. Cluster Analysis

We apply the same protocol as the previous experiment described in section IV-B. We obtained 6 main clusters corresponding to known problems. We report for each cluster the number of customers assigned to the cluster and the most common pattern, i.e. characteristic values that the variables take and the counts for each variable (Figure 6). Furthermore, we give an interpretation based on network expertise to understand what kind of problem the customers are facing in each cluster.

- Cluster 37: (600 clients) This cluster gathers customers with a problem on the remote PVR for the IPTV: Remote_PVR = Missing, and all other values correspond to an operational state of the client's line: (client_account_status=1, OLT_status=OK, router_status=Enabled, ONT_status=NODEFECT...).
- Cluster 30: (> 2500 clients) In this cluster the ONT is not detected: (ONT_status = Missing), where all other services are operational (router_status=Enabled, voip_status=Ok, tv_profile_status=operational ... ).
- Cluster 43: ( $\approx 2500$ clients) This cluster corresponds to the optimal behavior of the network and services, all equipment are detected and all services are operational.
- cluster 44: ( $\approx 550$ clients) This cluster describes a problem with the router where the router is disabled (router_status=DISABLED, router_ipv6_status=DISABLED), however all other equipments are operational and client account status is activated.
- Cluster 40: ( $\approx 27$ clients) This cluster represents the case where an account is suspended and the VOIP service is down (client_account_status $=0$,

tv_profile_status=SUSPENDED, VOIP_status=KO), however all pieces of equipment are operational.

- Cluster 12: ( $\approx 130$ clients) This cluster gathers clients with deactivated WiFi (router_WiFi_status = Down, router_status=Enabled), and all other equipment is operational (ont_status $=$ NODEFECT, OLT_status $=$ OK...).
This experiment shows that our clustering method can be helpful in a data exploration process where the number of clusters is not known a priori. With a simple network expertise we can see that the clusters are relevant and describe a particular behaviour on the network.


## VI. Discussion and Related works

Machine learning techniques for fault detection in telecommunication networks are promising. Bayesian networks have been dominant in this domain [1]-[3]. The main advantage of Bayesian network modeling is their easy interpretable nature. Root causes of faults are modeled by variables of the Bayesian network and inference can be performed in order to determine the root cause from the observable variables. This approach however, requires expert knowledge of the specific domain of faults and a time consuming task to build the Bayesian network and all the dependencies between the variables. Recently, researchers have been interested in learning the structure of the Bayesian network from data [11], and such approaches have been successfully used for the self-diagnosis problem [12]. However, the main problem, in such approaches, is the loss of the interpretability. The structure learned from the data can be one of a class of equivalence of optimal structures, hence, this often results in structures that are optimal but hard to interpret. The second group of machine learning approaches, are anomaly detection based approaches [13], [14]. Although these methods allow for accurate detection of anomalies from data, their main drawback is that all anomalies identified are grouped in a single cluster. Classifying each anomaly requires either a relabeling process by hand or a clustering process. Therefore, the natural reformulation of the self-diagnosis problem is as a clustering problem. Clustering types of faults from the data has been previously proposed [15], [16]. However, most of these approaches rely on classical algorithms where the number of clusters is known a priori or estimated by model selection. On the contrary, our approach allows for automatic determination of the number of clusters and requires no intervention from an expert. A post processing of the clusters by an expert is still needed in order to identify the fault present in each cluster and the related root cause. [17] proposed a method based on decision trees to accomplish this task.

## VII. CONCLUSION AND FUTURE WORKS

In this paper, we showed how an infinite multivariate categorical mixture model can be used to analyze data gathered from telecommunication networks and services and how to discover fault patterns in an unsupervised manner. The model is capable of identifying the correct number of clusters to analyze the data using the Dirichlet process. We showed how Variational Inference can be used to perform inference on the
model. This approach allows inference to scale well with the dimensionality of the data, and the convergence of the model can be determined explicitly. In future work, we will explore how such methods can be applied to time series data. Analysis of such data gathered from telecommunication networks can also be very useful for anomaly detection and monitoring.
