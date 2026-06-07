# 6 OPEN ACCESS 

Citation: Narimani Z, Beigy H, Ahmad A, MasoudiNejad A, Fröhlich H (2017) Expectation propagation for large scale Bayesian inference of non-linear molecular networks from perturbation data. PLoS ONE 12(2): e0171240. doi:10.1371/journal. pone. 0171240

Editor: Frank Emmert-Streib, Tampere University of Technology, FINLAND

Received: November 21, 2016
Accepted: January 17, 2017
Published: February 6, 2017
Copyright: © 2017 Narimani et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data availability statement: DREAM4 challenge data can be retrieved from the Bioconductor Rpackage DREAM4 and via the DREAM challenge web page (https://www.synapse.org/#!Synapse: syn3049712/wiki/74628). DREAM 8 challenge experimental data can be retrieved from the DREAM challenge web page (https://www.synapse. org/#!Synapse:syn1720047/wiki/55342).

Funding: ZN would like to acknowledge the Deutscher Akademischer Austauschdienst (DAAD) and University of Tehran for partially supporting

## RESEARCH ARTICLE

## Expectation propagation for large scale Bayesian inference of non-linear molecular networks from perturbation data

Zahra Narimani ${ }^{1}$, Hamid Beigy ${ }^{2}$, Ashar Ahmad ${ }^{3}$, Ali Masoudi-Nejad ${ }^{1 *}$, Holger Fröhlich ${ }^{3,4 *}$<br>1 Laboratory of Systems Biology and Bioinformatics (LBB), Institute of Biochemistry and Biophysics, University of Tehran, Tehran, Iran, 2 Department of Computer Engineering, Sharif University of Technology, Tehran, Iran, 3 Algorithmic Bioinformatics, Bonn-Aachen International Center for IT, University of Bonn, Bonn, Germany, 4 UCB Biosciences GmbH, Monheim, Germany<br>* amasoudin@ut.ac.ir (AMN); frohlich@bit.uni-bonn.de (HF)

## Abstract

Inferring the structure of molecular networks from time series protein or gene expression data provides valuable information about the complex biological processes of the cell. Causal network structure inference has been approached using different methods in the past. Most causal network inference techniques, such as Dynamic Bayesian Networks and ordinary differential equations, are limited by their computational complexity and thus make large scale inference infeasible. This is specifically true if a Bayesian framework is applied in order to deal with the unavoidable uncertainty about the correct model. We devise a novel Bayesian network reverse engineering approach using ordinary differential equations with the ability to include non-linearity. Besides modeling arbitrary, possibly combinatorial and time dependent perturbations with unknown targets, one of our main contributions is the use of Expectation Propagation, an algorithm for approximate Bayesian inference over large scale network structures in short computation time. We further explore the possibility of integrating prior knowledge into network inference. We evaluate the proposed model on DREAM4 and DREAM8 data and find it competitive against several state-of-the-art existing network inference methods.

## Introduction

Cellular components function through their interaction in form of biological networks, such as regulatory and signaling pathways [1]. With the advances of experimental methods and the emergence of high-throughput techniques, such as DNA microarray and next generation sequencing, the measurement of expression values of genes on whole genome scale is now possible. These advances have motivated attempts to learn molecular networks from experimental data. However, network inference from experimental data is computationally nontrivial, because the number of variables (typically genes, or proteins) usually exceeds the number of samples. Moreover, the number of possible network structures increases super-exponentially with the number of

her visiting stay in Germany. The funder had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. UCB Biosciences GmbH partially provided support in the form of salaries for author HF, but did not have any additional role in the study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Competing interests: Holger Fröhlich is affiliated to UCB Biosciences GmbH. There are no patents, products in development or marketed products to declare. This does not alter our adherence to all the PLOS ONE policies on sharing data and materials, as detailed online in the guide for authors.
network nodes. Therefore the search space to look for the true network is very large even for small graph instances and thus prevents the use of exact methods.

With the emergence of targeted perturbation techniques such as RNAi [2] and more recently CRISPR-Cas9 [3], it becomes possible to study the effect of specific gene silencing on a whole molecular network in a systematic manner, thus enabling identification of causal networks based on multiple intervention effects. Based on this fact, several groups of researchers have focused their work on network learning from perturbation data.

A large number of network computational methods exist, ranging from purely graph based [4-6] over Bayesian Networks [7-12], factor graphs [13] and epistasis analysis [14] to mechanistic models [15, 16]. Moreover, specifically for high-dimensional indirect perturbation effects (Dynamic) Nested Effects Models [16-18] have been proposed.

In this work, we follow a mechanistic ODE modelling framework such as one described in [15, 19-21]. Molinelli et al. described an efficient inference method based on Belief Propagation (BP) and showed that their method has similar performance as exact Bayesian inference [16]. That method relies on a steady state assumption and searches over a finite set of edge weights in order to ensure convergence. The required data discretization is a principal limitation of the method and potential source of error in a practical application. Furthermore, the steady state assumption is only valid in specific applications, excluding time series data.

In contrast, the proposed method called FBISC (Fast Bayesian Inference of Sparse Causal networks), neither requires any data discretization step nor does it rely on a steady state assumption. It can be applied to time series as well as steady state data. Akin to Molinelli et al. we allow for modeling non-linear regulatory relationships between molecules. To enable causal inference we allow for arbitrary, possibly combinatorial interventions. Our method is Bayesian and thanks to the employed Expectation Propagation (EP) scheme [22] computationally attractive.

Sometimes prior information is available about the structure of the network we wish to infer. The Bayesian framework used in our method allows us to incorporate prior knowledge into the network inference procedure in a natural and flexible way. This is achieved via a "spike and slab" prior [23], which at the same time enforces sparsity of the network. The spike and slab prior is known to yield less biased estimates than lasso-type L1 penalties, as e.g. employed in the "Inferelator" [24].

## Materials and methods

### 2.1 Modeling perturbations and dynamics

To ease the representation of our model, we first assume we have time-series data. The case of steady state data will be explained later. Let $Y=\left\{Y_{1}, Y_{2}, \ldots, Y_{n}\right\}$ be the molecules (genes, proteins, etc.) for which we have available measurements at different time points $(t)$. We would like to estimate the unknown network topology underlying their interaction. The time-series dataset can be described as $D=\left\{y_{i r}^{c}(\mathrm{t}) \mid \mathrm{i}=1, \ldots, \mathrm{n}, \mathrm{r}=1, \ldots, \mathrm{q}_{i}, \mathrm{c}=1, \ldots, \mathrm{~m}\right\}$, where $\mathrm{q}_{i}$ is the number of replicate measurements for molecule $i$, and $m$ is the number of perturbations. $C=\{1,2, \ldots, \mathrm{~m}\}$ represents the set of all perturbation experiments, in which each $c \in C$ can either directly influence one molecule or a subset of molecules $Y_{c} \subseteq Y$, i.e. perturbations can be targeted or combinatorial.

We have to take into account that perturbations may not exhibit the same quantitative effect on all directly influenced molecules. For example, we can think $c$ to consist of a treatment with two ligands $A$ and $B$. At given concentrations $A$ might strongly inhibit protein $P 1$, whereas $B$ might exhibit a moderate effect on protein $P 2$. In our model, we capture this behavior by including a set of extra nodes in our network, and a set of extra edges connecting

![img-0.jpeg](img-0.jpeg)

Fig 1. An example network of 3 genes $\left(\mathbf{g}_{1}, \mathbf{g}_{2}, \mathbf{g}_{3}\right)$ and 2 perturbation nodes $\left(\mathbf{p}_{1}, \mathbf{p}_{2}\right)$ and its related weight matrix. The goal is to infer network edges (w elements). The matrix is interpreted in the sense that elements in each row represent the weights of all incoming edges to a specific node (here: g1). The last two rows are zero, because we do not have edges directed towards perturbation nodes.
doi:10.1371/journal.pone.0171240.g001
perturbations with perturbed molecules. All the edges in our network are weighted, and with our model, we will infer the difference in the perturbation strength on different target molecules based on data. In conclusion, our network is a graph $\Gamma=(\mathrm{Y} \cup \mathrm{C}, \varepsilon)$, with the set of nodes $\mathrm{Y} \cup \mathrm{C}$ and set of edges $\epsilon$. The set of edges for this graph consists of all possible connections between regular nodes (i.e. all nodes except the perturbation nodes) and also the connections from our perturbation nodes to our regular nodes. So, our adjacency matrix to be inferred is a $(n+m) \times(n+m)$ weight matrix $W=\left(w_{i j}\right)$. We do not aim to infer any edge pointing to the perturbation nodes. By means of this representation we are able to model interactions between our network nodes (genes, proteins), and also between perturbation nodes and their targets as shown in Fig 1.

In general $c \in C$ can be time dependent, represented as $x_{c}(t)$, which can be Boolean ( 1 indicating perturbation, 0 no perturbation) or fully quantitative. A special case is when $x_{c}(t)=1$ for all $t=1, \ldots, T$. Targets of perturbation nodes do not have to be fully known; they can be inferred from data with our method. The technique for that (Expectation Propagation) is described later.

We can in principle model perturbations either as perfect (ideal) interventions or as soft interventions: Perfect interventions remove the influence of any other on the perturbed node, whereas soft interventions just increase the probability of the target node to be perturbed [25]. By using explicit intervention nodes and correspondingly weighted edges we here rely on a soft intervention scheme, which we believe to be closer to biological reality.

We assume an ordinary differential equation system (ODE) for describing the dynamics of the molecular network relative to known interventions:

$$
\frac{d y}{d t}=f\left(\boldsymbol{y}(t), \mathbf{x}_{c}(t)\right)
$$

Function f can be linear or non-linear [26]. Linear ODEs are not capable of capturing important biological phenomena such as coupled perturbation effects, nonlinear interactions, and switch-like behavior [15]. Inspired by [15], we thus propose the following approach for representing the time dependent behavior of system measurements, $\left\{y_{i r}^{c}(\mathrm{t})\right\}$, via a set of coupled non-linear differential equations:

$$
\frac{d}{d t} y_{i r}^{c}=\beta_{i} \frac{1}{1+\exp \left(-\sum_{p \neq i} w_{p r} y_{p r}^{c}(\mathrm{t})\right)}-\alpha_{i} y_{i r}^{c}(\mathrm{t})
$$

Here $z_{p r}^{e}(\mathrm{t})$ represents the time series of a measurement or perturbation node. The upper and lower bounds of $\frac{d}{d t} y_{i r}^{e}$ are controlled by positive parameters $\alpha_{i}$ and $\beta_{i}$.

Eq (2) can be linearly approximated as

$$
\frac{d}{d t} y_{i r}^{e} \approx \frac{y_{i r}^{e}(t+1)-y_{i r}^{e}(t)}{\Delta t}
$$

yielding

$$
y_{i r}^{e}(t+1)=\Delta_{i} \beta_{i} \underbrace{\frac{1}{1+\exp \left(-\sum_{p \neq i} w_{p r} z_{p r}^{e}(\mathrm{t})\right)}}_{:=R_{i r}^{e}(t)}+y_{i r}^{e}(\mathrm{t})\left[1-\alpha_{i} \Delta_{i}\right]
$$

where $\Delta_{\mathrm{t}}$ is the length of the known time interval between subsequent measurements $t$ and $t$ +1 . There is no constraint on equality of interval lengths. $\Delta_{\mathrm{t}}$ weights the influence of measurements at time $t$ on those at time point $t+1$. Shorter time intervals increase the influence of $y_{i r}^{e}(\mathrm{t})$ and decrease the effect of $R_{i r}^{e}(t)$.

Under steady state conditions we have $\frac{d}{d t} y_{i r}^{e}=0$ and hence we obtain:

$$
y_{i r}^{e}=\beta_{i} \frac{1}{1+\exp \left(-\sum_{p \neq i} w_{p r} z_{p r}^{e}\right)} \cdot \frac{1}{\alpha_{i}}
$$

Notably, we have removed the dependency on time $t$ in the formula here due to the steady state condition.

# 2.2 Bayesian model fitting 

2.2.a Likelihood model. Let $\mu_{i}(\mathrm{t}):=\Delta_{i} \beta_{i} R_{i r}^{e}(t)+y_{i r}^{e}(t)\left[1-\alpha_{i} \Delta_{i}\right]$ for $\mathrm{i}=1, \ldots, \mathrm{n}$. Furthermore, let $\sigma_{i}$ denote the Gaussian measurement noise for molecule $i$. The likelihood of measured data $D$ given weight matrix $W$ and known measurement noise can then be written as:

$$
p\left(D \mid W, \sigma^{2}\right)=\prod_{c \in \mathrm{C}} \prod_{t=1}^{T-1} \prod_{n=1}^{n} \prod_{r=1}^{s_{t}} N\left(y_{i r}^{e}(t+1) \mid \mu_{i}(t), \sigma_{i}\right)
$$

Typically the number of replicate measurements $q_{i}$ per molecule is small, and thus the empirical variance is an unreliable estimate of the true $\sigma_{i}^{2}$ In order to account for this fact we assume the true noise variance $\sigma_{i}^{2}$ to be drawn from an inverse gamma distribution:

$$
\sigma_{i}^{2} \sim I G(a, b)
$$

With this setting the marginal likelihood $p\left(\gamma_{i r}^{e}(\mathrm{t}) \mid \mu_{i}(\mathrm{t})\right)$, integrating out the unknown $\sigma_{i}^{2}$, can be computed in closed analytical form [27]:

$$
p\left(\gamma_{i r}^{e}(\mathrm{t}+1) \mid \mu_{i}(\mathrm{t})\right)=\frac{\Gamma\left(\mathrm{a}+\frac{1}{2}\right)}{\Gamma(\mathrm{a})} \frac{1}{(2 \pi \mathrm{~b})^{\frac{1}{2}}} \frac{1}{\left(1+\frac{3}{2 \mathrm{~b}}\left(\mu_{i}(\mathrm{t})-y_{i r}^{e}(\mathrm{t}+1)\right)^{2}\right)^{\frac{a+\frac{1}{2}}}{}}
$$

Accordingly, the marginal likelihood of the data given weight matrix $W$ is given by

$$
p(D \mid W)=\prod_{c \in \mathrm{C}} \prod_{t=1}^{T-1} \prod_{n=1}^{n} \prod_{r=1}^{s_{t}} p\left(y_{i r}^{e}(t+1) \mid \mu_{i}(t)\right)
$$

Notably, using Eq (5) in the steady state situation Eq (6) changes into:

$$
p(D \mid W)=\prod_{v \in \mathbb{C}} \prod_{i=1}^{n} \prod_{t=1}^{T_{i}} p\left(\gamma_{i t}^{c} \mid \mu_{i}\right)
$$

Note that we dropped $t$ here to make the independence of time explicit.
In our method we use Eq (6) and Eq (7) to score weight matrices for time series and steady state data, respectively.
2.2.b Prior knowledge and network sparsity. To enforce sparsity of $W$ we use a spike-and-slab prior [23] on the edge weights: We introduce a binary latent variable, $\gamma_{i j}$, for each $w_{i j}$ indicating the presence $\left(\gamma_{i j}=1\right)$ or absence $\left(\gamma_{i j}=0\right)$ of edge $i \rightarrow j$. Given $\gamma_{i j}$ the spike-and-slab prior on is defined as:

$$
\omega_{i j} \sim \gamma_{i j} \mathcal{N}\left(0, \sigma_{1}^{2}\right)+\left(1-\gamma_{i j}\right) \mathcal{N}\left(0, \sigma_{2}^{2}\right)
$$

The variance $\sigma_{1}$ of the slab distribution can be set sufficiently large (here: 10) in order to achieve a low bias of weight estimates for present edges. On the other hand, $\sigma_{2}$ is set close to zero $\left(\sigma_{2} \rightarrow 0\right)$ to approximate a delta function centered at zero (the spike). The mixture coefficient $\gamma_{i j}$ is drawn from a Bernoulli distribution:

$$
\gamma_{i j} \sim \operatorname{Bernoulli}\left(\rho_{i j}\right)
$$

Hence, $\gamma_{i j}$ selects either the spike (if it is zero) or the slab distribution (if it is one) for $w_{i j}$. Parameter $\rho_{i j}$ reflects the prior probability for that. This allows us to incorporate prior knowledge in a similar way as e.g. described in [28].
2.2.c Bayesian model inference via expectation propagation. Expectation propagation (EP) has been introduced by [22] as a computationally efficient approximation of full Bayesian inference. It extends the technique of moment matching [29].

Let $\Theta$ denote the set of all inferable parameters $(W, \boldsymbol{\alpha}, \boldsymbol{\beta})$ of our model. Similar to Variational Bayesian methods, EP minimizes Kullback-Leibler (KL) divergence between the true joint distribution $p(\Theta, D)$ and some approximation, $q(\Theta, D)$. For that purpose it is essential to factorize the joint distribution $p(\Theta, D)$, for example as:

$$
\begin{aligned}
& p(\theta, D)=p(\theta) \prod_{v \in \theta} \frac{1}{Z_{v}} \exp \left\{-\sum_{t=1}^{T-1} \sum_{v=1}^{n} \sum_{v=1}^{\infty}\left(\gamma_{i v}^{c}(\mathrm{t}+1)-\Delta_{t} \beta_{i} \mathrm{R}_{i v}^{c}(\mathrm{t})-\gamma_{i v}^{c}(\mathrm{t})\left[1-\alpha_{i} \Delta_{t}\right]\right)^{2}\right\} \\
& =\prod_{c=0}^{\infty} f_{c}(\theta)
\end{aligned}
$$

with $f_{0}(\Theta):=p(\Theta)$. Each factor $f_{c}(\Theta)$ is approximated by a multivariate Gaussian $\tilde{f}_{c}(\theta)$. EP then iteratively minimizes the KL-divergence $K L[p \| q]=\int p(x) \log \frac{p(x)}{q(x)} d x$ between the original distribution $p(\theta, D)=\prod f_{c}(\theta)$ and the Gaussian approximation $\mathrm{q}(\theta, D)=\prod \tilde{f}_{c}(\theta)$. This is done using matching first moments, i.e. expectations. Notably, the EP algorithm always converges when the approximating factors are in the exponential family [22].
2.2.d Implementation. For the implementation of the EP algorithm we use microsoft Infer.NET [30], a framework for Bayesian inference on graphical models. Our proposed model can be interpreted as a special type of Dynamic Bayesian Network (DBN), connecting each network node to its parents i.e. the node values in previous time-step (Fig 2). The code of our model-written in C\#-is provided in the Supplemental material (S1 Code).

![img-1.jpeg](img-1.jpeg)

Fig 2. The proposed model can be interpreted as a Dynamic Bayesian Network. The network has two types of node: 1) regular nodes, demonstrated by circles, representing the genes(proteins) in the underlying biological process; 2) perturbation sources $\left(p_{1}, \ldots, p_{C}\right)$, represented as diamonds.
doi:10.1371/journal.pone.0171240.g002
The same weight matrix (or the same set of weight parameters) is used for all layers of our DBN; for example if we assume $\mathrm{w}_{12}$ as the weight of the edge from $\mathrm{g}_{1}$ at time-point 0 to $\mathrm{g}_{2}$ at time-point 1 , the edge connecting the same two nodes from time-point 1 to time-point 2 would have same weight parameter. This implies that we assume the network structure not to change over time.

# 2.3 Dealing with non-linearity within the EP framework 

The non-linear sigmoid function shown in Eq (4) yields severe convergence issues within the EP inference framework. We thus use a piece-wise approximation of the sigmoid function $g(Z)=\frac{1}{1+\exp (-Z)}$ appearing on the right hand side of Eqs (4) and (5):

$$
g(\Phi(Z))= \begin{cases}\Phi(Z): & \text { if } \min (\mathrm{y})<\Phi(Z)<\max (y) \\ \max (y): & \text { if } \Phi(Z)>\max (y) \\ \min (y): & \text { if } \Phi(Z)<\min (y)\end{cases}
$$

where $\max (y)$ and $\min (y)$ denote the maximally and minimally measured concentrations for one particular molecule (per replicate) in a certain condition over a complete time series.

Note Eq (9) provides an upper an lower bound for the concentration dependent change of each molecular in dependency of its regulators. The function $\Phi$ in the simplest case could be the identity function, as proposed in Bonneau, Reiss et al. (2006). In that case between the upper and lower bound the function $g$ is fully linear, and deviates significantly from the original sigmoid curve if the argument $Z$ is far away from 0.5 . Furthermore, a linear concentration change is principally non-physiological. In order to account for these facts we thus suggest to define $\Phi$ in Eq (9) as a non-parametric B-spline basis expansion [31]. The B-spline expansion can be computed in a pre-processing step of our method, which maps the original time-series data into a cubic B-spline space. That means we replace each $z_{p r}^{i}$ in Eqs (4) and (5) by

$$
\Phi\left(Z_{p r}^{i}\right)=\sum_{k} z_{k}^{i p r} B_{k}^{i p r}\left(x_{p r}^{i}\right)
$$

and use Eq (9) as an approximation of the sigmoid function. In Eq (10) $B_{k}^{i p r}$ denotes a (cubic) B-spline basis function and the sum runs over the different spline knots $k$. After choosing an appropriate number of spline knots, functions of the form of Eq (10) can be fitted to each measured time series (on log scale). These functions can in principle be evaluated up to every

desired resolution. Correspondingly, interpolated input data can now be fed to our model rather than the original raw data.

In practice we tried the following different spline interpolation methods here:

1. Smoothing B-splines, as implemented in the "smooth.spline" function in R [32]
2. Interpolated cubic B-splines, as implemented in the "spline" function in R [33]

# Results 

### 3.1 Simulation studies

In order to better understand the principle behavior of our method named FBISC (Fast Bayesian Inference of Sparse Causal networks) under different conditions, we performed several simulation experiments. A rigorous comparison against competing methods is shown in later Sections.

Network topologies with 10, 50 and 100 nodes and corresponding time series data with 5, 10,15 and 20 measurement time points were simulated via the GeneNetWeaver tool [34]. GeneNetWeaver samples random sub-networks from known large-scale yeast and E. coli transcriptional networks. The network topologies used in this paper are shown in the (S1 Fig). Data simulation for each of these topologies was repeated 5 times, and no perturbations were applied at first place.

The area under ROC (AUROC) and area under precision-recall curve (AUPR) are used to evaluate prediction of method. Notably, these measures are independent of a specific confidence or $p$-value cutoff. Fig 3 depicts the influence of the number of time points and the number of network nodes on reconstruction performance when using the most basic version of our method without spline interpolation (i.e. a piecewise linear approximation of the sigmoid curve). As expected, AUPR and AUROC values increase with more time points. For networks
![img-2.jpeg](img-2.jpeg)

Fig 3. Effect of number of time points and number of network nodes on network reconstruction performance with FBISC. (a) AUPR. (b) AUROC.
doi:10.1371/journal.pone.0171240.g003

with 10 nodes and 15 time points, AUROC and AUPR reach $60 \%$ and $85 \%$, respectively, while for networks with 100 nodes AUPR drops to $15 \%$, but the AUROC is still close to $60 \%$.

Next we investigated the effect of using perturbation data with the same basic version of FBISC. For that purpose, we randomly picked $20 \%$ of the nodes of the network with 100 nodes and each of them affected by a different perturbation. Perturbations were assumed to represent a constant signal over time, and ten time points were simulated for time courses of each network node. We compared three situations 1) targets of perturbations are fully known; 2) targets of perturbations are unknown; 3) purely observational data. Fig 4 represents our results for four network structures for each of these situations.

As indicated by Fig 4 perturbation data generally increased AUPR and AUROC compared to purely observational data dramatically: AUPR was at least twice as high than with purely observational data, and the AUROC increased by more than $10 \%$. If targets of individual perturbations were fully known to the algorithm (i.e. the prior probability for edges connecting perturbations to their targets was one) AUPR and AUROC values were on average $\sim 5 \%$ higher than in the case were targets of perturbations were unknown.

In the last experiment we compared the different spline methods discussed in Section 2.3 against each other and against the piecewise linear approximation of the sigmoid curve. This was done for the network with 100 nodes and 7 simulated measurement time points. No perturbations were simulated at this point. The results shown in Fig 5 indicate a significant increase of AUPR and AUROC with both spline techniques and increasing the number of interpolated measurement time points. At the same time the difference between B-spline interpolation and smooting B-splines was marginal.

In conclusion, our simulations demonstrate that our method can successfully exploit perturbation information and profits from spline interpolated time series data. Furthermore, reconstruction performance is expected to be relatively robust, even if large networks are estimated.
![img-3.jpeg](img-3.jpeg)

Fig 4. Effect of perturbation data on network reconstruction performance (a and b represent AUPR and AUROC respectively). unknownPert = targets of perturbations are not known; knownPert = targets of perturbations are fully known; observationsl = purely observational data.
doi:10.1371/journal.pone.0171240.g004

![img-4.jpeg](img-4.jpeg)

Fig 5. Effect of using spline interpolation and smoothing spline. The plot shows the AUPR and AUROC (a and b respectively) as a function of an increasing number of interpolated measurement time points. 7 time points corresponds to the original data in combination with a piecewise linear approximation of the sigmoid curve.
doi:10.1371/journal.pone.0171240.g005

# 3.2 Evaluation on DREAM challenge data and comparison against competing methods 

We downloaded data from the DREAM4 [35] and DREAM8 [36, 37] challenges for the further evaluation of our approach and comparison to competing methods (see http://dreamchallenges. org/project-list/closed/). The gold standard networks provided in these data are used for evaluation. DREAM4 provides simulated data for five networks of size 10 nodes and five networks of size 100 nodes. For each network perturbation time series and steady state data were retrieved. Time series data comprise 21 time points $\left(t_{0}=0\right.$ to $\left.t_{20}=1000\right)$ reflecting measurements of each network node. Perturbations are always applied at time 0 and removed at time 500. Information regarding to the exact targets of perturbations are not available. Each time series is measured with 5 replicates for the 10 -node network and 10 replicates for the 100 -node network. Each replicate represents a perturbation experiment in which different nodes (about one-third of the network) are perturbed.

In addition to time series different kinds of steady state data are available from DREAM4. Here we employed knock-out, knock-down, and multifactorial perturbation data. Knock-out and knock-down data reflect steady state measurements of all network nodes after perturbation of exactly one known node. Multifactorial data corresponds to combinatorial perturbations of unknown nodes in each experiment. No replicate measurements are available for steady state data.

DREAM8 provides experimental data of a signaling network with 20 nodes at 11 time points. Here the perturbations correspond to compound treatments. Exact concentrations of perturbation sources are not given but specified with qualitative values (high/low). Following Young et al. [38] we normalized each measured time series by subtracting its mean.

We compared FBISC with ScanBMA [38], iBMA [39], LASSO [40], ebdnet (Empirical Bayes Estimation of Dynamic Bayesian Networks [41], ARACNE [42], and CLR [43]. As

Table 1. Average performance results based on DREAM4 10-gene and 100-gene networks (time series data). FBISC results are shown in the last two rows; other results were taken from Young et al. (2014). FBISC-linear corresponds to the piecewise linear approximation of the sigmoid curve. FBISC-B-spline is applied with 20 and 100 interpolated time points for the 10 and 100-gene networks, respectively.


doi:10.1371/journal.pone.0171240.t001
opposed to the first three methods LASSO, ARACNE and CLR are not per se designed for time series data. In order to adapt these methods to our situation we considered for each network gene of interest all other genes as potential regulators. For each potential regulator its measurements excluding the last time point were used. We then asked, which subset of regulators could predict the measured time series of the network gene of interest excluding the first time point. This estimation procedure was repeated for all network genes.

Notably, information about perturbations was included into all methods competing with our FBISC approach. This was done by adding perturbations as additional potential "regulators" of each node (similar to the way that FBISC treats perturbations). In case that perturbation targets were known, perturbations were only considered as potential regulators of directly targeted nodes.

All tested network inference algorithms produce either a confidence measure (FBISC, ScanBMA, iBMA) or a $p$-value (ebdnet, CLR, ARACNE) for each possible edge. Correspondingly, AUROC and AUPR are used to evaluate prediction performances of methods. Notably, these measures are independent of a specific confidence or p-value cutoff.

# 3.3 Results for DREAM4 data 

Using the above described time series perturbation data we compared results obtained by our method with the ones reported in Young et al. [38]. Results generated by our method are shown in the last two rows of Table 1, indicating a higher AUROC/AUPR for 10-gene and higher AUPR for 100-gene networks than competing methods, specifically when using the B-spline method. ROC and PR curves regarding DREAM4 networks of size 100 are provided in S2 Fig.

Next we compared our method to the competing approaches on the basis of various kinds of steady state data (Table 2), showing a clear improvement compared to ARACNE, LASSO and CLR (which are the only competing methods using steady state data) in all cases. As expected, AUROC and AUPR values for steady state data are typically a bit below those observed for time series data. However, FBISC using knock-out data could still achieve an AUROC of $70 \%$ for the 100-gene network.

### 3.4 Results for DREAM8 data

Next, we focused on the DREAM8 challenge data. In contrast to before, results for this dataset were obtained by our own implementation of competing methods. More specifically, we used R package NetworkBMA [44] for ScanBMA, minet [45] for ARACNE and CLR, ebdbnet [41], and glmnet [46] for LASSO. Results are presented in Table 3, indicating a slightly better AUROC than the best competing approach (CLR).

Table 2. Average performance results based on DREAM4 10-gene and 100-gene networks with steady state knock-down, knock-out, and multifactorial data. Notably, FBISC is only applicable without spline interpolation in these situations. For the 10-gene networks LASSO failed due to low number of available samples and is thus not shown.


doi:10.1371/journal.pone.0171240.t002

### 3.5 Effect of incorporating prior knowledge

Next we tested, in how far the previously presented results would change in dependency of prior knowledge. Only time series data were used at this point. Following the approach used by Praveen et al. [47] we considered $0,5,10,25$ and 50 percent of true network edges to be known with probability of $90 \%$, and the FBISC-B-spline method with the same setting reported in Sections 3.3 and 3.4 was used. The results of this experiment (Fig 6) show an increase of AUROC and AUPR as fractions of confidently known edges increase. Notably, with $50 \%$ known edges we could achieve an AUROC of close to $75 \%$ for the 100 gene network from the DREAM4 challenge and about the same performance for the DREAM8 challenge network.

### 3.6 Run time and parallelization

FBISC is a Bayesian approach. Frequentist methods like CLR and ARACNE are based on mutual information and conceptually far simpler. They are thus computationally comparably cheap. From the practical point of view, a question is thus, how the computing time of FBISC compares to competing methods.

The run time of ScanBMA depends on the number of potential parents (nvar) per node. Here we tested ScanBMA with $n v a r=10$ and $n v a r=20$ (for larger values of $n v a r$ the run time

Table 3. Results on DREAM8 signaling data. FBISC-linear corresponds to the piecewise linear approximation of the sigmoid curve.


doi:10.1371/journal.pone.0171240.t003

![img-5.jpeg](img-5.jpeg)

Fig 6. Effect of including prior knowledge into FBISC for DREAM; AUPR and AUROC represented in a and b respectively. (10 and 100-node networks: D4-10 and D4-100) and DREAM8 (D8) data. Shown are the AUPR and AUROC for FBISC after adding a varying percentage of true edges with 90% confidence.

doi:10.1371/journal.pone.0171240.g006

increases dramatically). Results for our method compared to the competing approaches considered in this paper are reported in Table 4, indicating a good computational scalability of our FBISC approach. Notably, our algorithm can be parallelized, because the inference problem can be solved independently for each network node. This allows for an additional gain in computation time. Corresponding results shown in Table 4 (named FBISC parallel) refer to the use of 2 cores (Intel® Core™ i5-5257U dual core processor with 4 parallel threads). More cores would reduce calculation time even more. For DREAM8 and DREAM4 networks of size 100 there is speed up by factor 2 due to parallelization (Table 4). At the same time, the memory use was rather modest and allowed to run all computations on a standard laptop computer. Overall, the Bayesian inference scheme used in FBISC thus seems to be applicable even for large networks.


Table 4. Total run time (in seconds) on DREAM4 (10 and 100-node networks) and DREAM8 data.

doi:10.1371/journal.pone.0171240.t004

# Discussion 

We proposed a Bayesian approach for computationally efficient inference of large scale molecular networks from complex perturbation data. Our FBISC method is highly flexible and applicable even in situations where the exact targets of perturbations are unknown (such as stress experiments), which is frequently the case in biology. A further strength is that we consider perturbations themselves as time dependent, as e.g. reflected in the DREAM4 data. FBISC uses a biochemically inspired model to describe the non-linear dynamical behavior of molecular networks and integrates this description into a graphical modeling framework. This allows for the application of efficient approximate inference schemes, such as expectation propagation. Notably, the output of our method is a posterior distribution over edge weights, which accounts for the unavoidable uncertainty of any network inference.

We enforced sparsity of inferred networks in form of a spike and slab prior. This type of prior forces many edge weights to exactly zero and naturally allows for the integration of prior background knowledge, which demonstrated useful in our results. Altogether we see the combination of a highly flexible modeling framework (reflected by non-linear dynamics, arbitrary complex perturbation schemes and probabilistic integration of prior knowledge), which is applicable to time series as well as steady state data and uses computationally scalable Bayesian inference as differentiation of FBISC to existing techniques. The advantage for the user lies in a unified method, which allows for automatically adapting literature derived network information to experimental data and produces confidence measures. Our results showed an attractive prediction performance of our method. We thus believe that our proposed FBISC method is an attractive alternative to existing methods to learn causal network structures from complex perturbation data. The C\# code of our method is included in the supplements of this paper (S1 Code).

## Supporting information

S1 Code. Code for FBISC inference model. (c\# infer.net framework). (CS)

S1 Fig. Network structures used in simulation section. (generated by geneNetWeaver). (DOCX)

S2 Fig. ROC and PR curves for the rest of DREAM4 size 100 networks number. (DOCX)

## Acknowledgments

Authors would like to thank Dr. Mukesh Bansal for his comments and guides for the network inference evaluation methods.

## Author contributions

Conceptualization: AMN HF.
Data curation: ZN.
Formal analysis: ZN HF.
Funding acquisition: ZN HF AMN.
Investigation: ZN HF AA HB.

Methodology: ZN HF.
Project administration: HF AMN.
Resources: HF AMN.
Software: ZN.
Supervision: HF AMN.
Validation: HF AMN.
Visualization: ZN HF.
Writing - original draft: ZN HF.
Writing - review \& editing: AMN HB.
