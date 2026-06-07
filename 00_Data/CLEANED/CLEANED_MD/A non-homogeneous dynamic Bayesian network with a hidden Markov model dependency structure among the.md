# A non-homogeneous dynamic Bayesian network with a hidden Markov model dependency structure among the temporal data points 

Marco Grzegorczyk ${ }^{1}$


#### Abstract

Received: 18 July 2013 / Accepted: 7 May 2015 / Published online: 28 May 2015 (C) The Author(s) 2015. This article is published with open access at Springerlink.com


#### Abstract

In the topical field of systems biology there is considerable interest in learning regulatory networks, and various probabilistic machine learning methods have been proposed to this end. Popular approaches include non-homogeneous dynamic Bayesian networks (DBNs), which can be employed to model time-varying regulatory processes. Almost all nonhomogeneous DBNs that have been proposed in the literature follow the same paradigm and relax the homogeneity assumption by complementing the standard homogeneous DBN with a multiple changepoint process. Each time series segment defined by two demarcating changepoints is associated with separate interactions, and in this way the regulatory relationships are allowed to vary over time. However, the configuration space of the data segmentations (allocations) that can be obtained by changepoints is restricted. A complementary paradigm is to combine DBNs with mixture models, which allow for free allocations of the data points to mixture components. But this extension of the configuration space comes with the disadvantage that the temporal order of the data points can no longer be taken into account. In this paper I present a novel non-homogeneous DBN model, which can be seen as a consensus between the free allocation mixture DBN model and the changepoint-segmented DBN model. The key idea is to assume that the underlying allocation of the temporal data points follows a Hidden Markov model (HMM). The novel HMM-DBN model takes the temporal structure of the time series into account without putting a restriction onto the configuration space of the data point allocations. I define the novel HMM-DBN model and the competing models such that the regulatory network structure is kept fixed among components, while the network interaction parameters are allowed to vary, and I show how the novel HMM-DBN model can be inferred with Markov Chain Monte Carlo (MCMC) simulations. For the new HMM-DBN model I also present two new pairs of MCMC moves, which can be incorporated into the recently proposed allocation sampler for mixture models to improve convergence

[^0][^1]
[^0]:    Editors: Eric Xing and Peter Flach.

    囚 Marco Grzegorczyk
    m.a.grzegorczyk@rug.nl

    1 Johann Bernoulli Institute (JBI), Rijksuniversiteit Groningen, 9747 AG Groningen, The Netherlands

of the MCMC simulations. In an extensive comparative evaluation study I systematically compare the performance of the proposed HMM-DBN model with the performances of the competing DBN models in a reverse engineering context, where the objective is to learn the structure of a network from temporal network data.

Keywords Non-homogeneous dynamic Bayesian network $\cdot$ Hidden Markov model $\cdot$ Mixture model $\cdot$ Multiple changepoint process $\cdot$ Markov Chain Monte Carlo (MCMC) $\cdot$ Allocation sampler

# 1 Introduction 

In the topical field of systems biology there is considerable interest in learning regulatory networks, such as gene regulatory transcription networks (Friedman et al. 2000), protein signal transduction cascades (Sachs et al. 2005), neural information flow networks (Smith et al. 2006), or ecological networks (Aderhold et al. 2013). In the computational biology and machine learning literature a variety of powerful probabilistic machine learning methods based on graphical models, such as Bayesian networks (Friedman et al. 2000), have been proposed to learn these networks from data. The standard assumption underlying the conventional graphical models is that the observed time series are homogeneous so that potential changes in the regulatory interactions are not taken into account. That is, the standard graphical models, e.g. the conventional homogeneous Gaussian dynamic Bayesian network (DBN) model, describe a simple homogeneous linear dynamical system. Unfortunately, the assumptions of homogeneity and linearity are unrealistic for many applications in systems biology, and thus can cause erroneous and misleading inference results. Regulatory interactions in systems biology applications tend to be non-linear and adaptive so that they vary over time, e.g. in response to changing environmental and experimental conditions.

A more appropriate approach would therefore be the deduction of a detailed mathematical description of the entire network domain in terms of mechanistic models, e.g. in the form of coupled non-linear stochastic differential equations (DEs). Seminal examples have for example been presented in Vyshemirsky and Girolami (2008) and Toni et al. (2009). Since a proper Bayesian inference for those mechanistic models is computationally expensive, usually only very small network domains with typically only 3-4 nodes are considered (Vyshemirsky and Girolami 2008) or the inference is based on approximations (Toni et al. 2009). Therefore, in standard applications of mechanistic models only a limited amount of different hypotheses about the underlying network structure is compared, and the space of network structures is not systematically searched for those networks that are most consistent with the observed data. That is, mechanistic models cannot be used to learn regulatory networks from scratch (i.e. without any prior hypotheses about potential network structures). Therefore, there have been various efforts to relax the homogeneity assumption for undirected (see, e.g., Talih and Hengartner 2005 or Xuan and Murphy 2007) and directed (see, e.g., Ahmed and Xing 2009) graphical models, as well as for dynamic Bayesian networks (see references below). The key idea is to leave the class of homogeneous linear dynamic models, and to develop novel non-homogeneous graphical models that balance between two requirements: On the one hand, those models should offer enough flexibility so that they can appropriately capture the underlying non-homogeneous biological processes, and thus become competitive to the mechanistic models. On the other hand, from a computational perspective it must be possible to use these models to systematically search the space of network structures and to learn the underlying regulatory relationships from scratch (i.e. in the absence of any hypoth-

esis about the underlying network structure). The focus of this paper is to propose a novel non-homogeneous dynamic Bayesian networks (DBN) model that fulfils both requirements.

Various DBN models have been proposed in the literature, and it can be distinguished between DBNs for which the parameters in the likelihood can be integrated out in closedform, and DBNs for which the marginal likelihood is intractable. The latter DBNs tend to have a greater flexibility, but they are more susceptible to over-fitting, since the network structures and the interaction parameters have to be estimated simultaneously. Flexible DBNs with an intractable likelihood can, for example, be constructed along the lines proposed in Imoto et al. (2003), Rogers and Girolami (2005), or Ko et al. (2007). ${ }^{1}$ Here, I concentrate on DBNs for which the network parameters can be integrated out in closed form. Although this requires certain regularity conditions, such as parameter independence and prior conjugacy, to be fulfilled, these DBNs have two attractive features: (i) The data-overfitting problem is intrinsically avoided, and (ii) "model-averaging" can be realised by efficient Reversible Jump Markov Chain Monte Carlo (RJMCMC) simulations in discrete configuration spaces (Green 1995).

To obtain a closed-form expression of the marginal likelihood in DBN models three models with their respective conjugate prior distributions have been proposed in the literature: (i) the multinomial distribution with the Dirichlet prior, leading to the BDe score (Cooper and Herskovits 1992), (ii) the linear Gaussian distribution with the normal-Wishart prior, leading to the BGe score (Geiger and Heckerman 1994), and (iii) a Bayesian linear regression model with a Gaussian prior on the regression coefficients (see, e.g., Lèbre et al. 2010). The former two approaches have originally been proposed for static Bayesian networks, but they can be extended straightforwardly to model homogeneous DBNs, as demonstrated in Friedman et al. (2000). Non-homogeneous DBNs with these two standard scores have for example been developed in Robinson and Hartemink (2009) and Robinson and Hartemink (2010) (with BDe), and in Grzegorczyk and Husmeier (2009) and Grzegorczyk and Husmeier (2011) (with BGe). The key idea behind these non-homogeneous DBNs is to relax the homogeneity assumption by complementing the standard homogeneous DBN with a Bayesian multiple changepoint process. Each time series segment defined by two demarcating changepoints is associated with separate interaction parameters, and in this way the regulatory relationships are allowed to vary over time.

Recently, the Bayesian regression model, described in Lèbre et al. (2010), has become a popular probabilistic model for non-homogeneous DBNs. A shortcoming of this "Bayesian regression" DBN (BR-DBN) model, as originally proposed by Lèbre et al. (2010), is potential model over-flexibility, as different time series segments are associated with different network structures, which for short time series will lead to over-fitting and inflated inference uncertainty. Various regularised variants of this BR-DBN model have been proposed (see, e.g., Dondelinger et al. 2010, 2012), and in other instantiations of the BR-DBN model, the authors follow Grzegorczyk and Husmeier (2011) or Grzegorczyk and Husmeier (2013) and keep the network structure fixed among segments so that only the interaction parameters vary from segment to segment. In this paper I follow the latter works and focus on applications where cellular processes take place on a short time scale so that it is not the network structure but rather the strength of the regulatory interactions that changes with time. ${ }^{2}$ For

[^0]
[^0]:    ${ }^{1}$ Rogers and Girolami (2005) propose a sparse Bayesian regression approach with a type-II maximum likelihood estimation of the parameters. The model by Imoto et al. (2003) is based on heteroscedastic regression and requires the Laplace approximation to be applied. Ko et al. (2007) propose to employ Gaussian mixture models, and the authors resort to the Bayesian BIC criterion for model selection.
    ${ }^{2}$ For example, in a gene regulatory transcription network, the ability of a transcription factor to bind to the promoter of a gene is very unlikely to change on a short time scale (i.e. the network structure stays fixed); but the extent to which binding happens (the interaction strength) may vary over time. On the other hand, for

those models, which do not allow for segment-wise network changes, various information coupling schemes with respect to the segment-specific network parameters have recently been proposed (Grzegorczyk and Husmeier 2012a, b, 2013).

All these non-homogeneous DBNs, mentioned above, follow the same paradigm and combine a classical homogeneous DBN model with a multiple changepoint process. However, the configuration space of the data segmentations that can be obtained by changepoints is restricted. Let us consider these changepoint processes in the broader context of mixture models, which are based on a free allocation of the data points to mixture components. From this perspective the changepoints divide the time series into disjunct temporal segments, and the segments (i.e. the data points within each segment) are assigned to disjunct ("mixture") components. That is, there is a one-to-one mapping between the temporal segments and the mixture components, and hence, distant segments cannot be allocated to the same component; throughout the paper I will also say: "a component once left cannot be revisited". For instance, if there are 10 temporal data points, then allocation schemes, such as [1112222211], are not part of the segmentation space of multiple changepoint processes and would have to be "approximated" by segmentations, such as [1112222233].

In earlier papers it has been proposed to combine Bayesian networks with classical mixture models (see, e.g., Ko et al. 2007 or Grzegorczyk et al. 2008). Unlike the DBNs with changepoints (CPS-DBNs), the proposed mixture DBN (MIX-DBN) allows for an unrestricted free allocation of the data points to (mixture) components, and, hence, substantially increases the configuration space of the possible data segmentations. However, for time series the temporal order of the data points is not taken into account, and this inevitably incurs an information loss, e.g. when a priori temporally neighbouring data points should be more likely to be assigned to the same component than distant ones.

In biological systems various examples for periodic gene regulatory processes can be found. E.g. plants, such as Arabidopsis thaliana, possess a circadian clock and the underlying molecular mechanisms depend on the presence/absence of light (see Sect. 3.3 for details and literature references). That is, the gene regulatory processes in Arabidopsis are diurnal and periodically depend on the daily dark:light (night:day) cycle. These daily alternations of darkness (" 1 ") and light (" 2 ") phases are caused by an external factor, namely the rotation of the earth, and they impose a periodic diurnal segmentation on the gene regulatory processes in the circadian clock, e.g. a segmentation of the form [111222111222]. ${ }^{3}$ Apart from this plant biology example, described in more detail in Sect. 3.3, circadian rhythms also play an important role in the regulatory processes in mammalian cells (see, e.g., Yan et al. 2008). Another example are the periodic regulatory processes that can be observed during the cell cycle (see, e.g., Whitfield et al. 2002 or Rustici et al. 2004). As discussed above, neither the changepoint processes (CPS-DBN) nor the free allocation mixture models (MIX-DBN) are adequate for learning periodic segmentations; the CPS-DBN model cannot revisit states once left, while the MIX-DBN model completely ignores the temporal arrangement of the data points.

In this paper I present a novel non-homogeneous dynamic Bayesian network model, which can be seen as a consensus between the free allocation mixture DBN model (MIX-DBN)

[^0]
[^0]:    Footnote 2 continued
    scenarios, such as morphogenesis, where the cellular processes take place on a long time scale, the assumption of a fixed network structure might turn out to be too restrictive.
    ${ }^{3}$ This segmentation may cover 12 equidistant time points, $t_{1}, \ldots, t_{12}$, in a period of 48 hours (h) with a daily 12 h : 12 h dark:light cycle. There is a 4 h distance between the time points and it holds: $t_{1}=4 \mathrm{~h}, t_{2}=8 \mathrm{~h}$, $t_{3}=12 \mathrm{~h}$ (dark), $t_{4}=16 \mathrm{~h}, t_{5}=20 \mathrm{~h}, t_{6}=24 \mathrm{~h}$ (light), $t=28 \mathrm{~h}, t=32 \mathrm{~h}, t=36 \mathrm{~h}$ (dark), $t_{10}=40 \mathrm{~h}$, $t_{11}=44 \mathrm{~h}, t_{12}=48 \mathrm{~h}$ (light).

and the changepoint-process-segmented DBN model (CPS-DBN). The idea is to assume that the underlying allocation of the temporal data points follows a Hidden Markov model (HMM). The novel DBN model, which I will refer to as the HMM-DBN model, does take the temporal structure of the time series into account without putting any restriction onto the configuration space of the allocations. With the HMM-DBN model, periodic segmentations, such as [111222111222], can be inferred properly. In this paper I implement the novel model with a network structure that is kept fixed among segments and I only allow the network interaction parameters to vary in time. In a comparative evaluation study I demonstrate that the novel HMM-DBN model has the attractive feature that it is competitive to both (i) the CPSDBN model for changepoint-segmented allocations and (ii) the MIX-DBN model for free mixture allocations. I also show how the allocation of the data points can be inferred with the allocation sampler (Nobile and Fearnside 2007). As the allocation sampler has been developed for classical Gaussian mixture models, it does not exploit the temporal information. I therefore propose to improve the allocation sampler by introducing two new pairs of complementary MCMC moves, which utilise the temporal arrangement of the data points. Although the key idea behind the proposed HMM-DBN model is generic, I present it in the context of the BRDBN model (Lèbre et al. 2010). With regard to the real-world applications (see Sects. 3.2 and 3.3) I follow Grzegorczyk and Husmeier (2011) and Grzegorczyk and Husmeier (2013) and keep the network structure fixed among segments (components).

This paper is organized as follows: Sect. 2 provides a comprehensive exposition of the mathematical details behind the HMM-DBN model. I also present two new pairs of moves for the MCMC inference, and I briefly summarise the competing non-homogeneous DBN models. Section 3 gives an overview to the data on which I apply and cross-compare the models. I provide the details on how I implemented the HMM-DBN model for the comparative evaluation study in Sect. 4. The results of a study, in which I systematically compare the performances of the MIX-DBN, the CPS-DBN and the HMM-DBN model, are presented in Sect. 5. A discussion of the computational costs and a brief outlook to future work is provided in Sect. 6, before I draw my final conclusions in Sect. 7. Note that mathematical details from Sect. 2 have been relegated to the Appendices 1-4.

# 2 Methodology 

### 2.1 Bayesian regression models

In this subsection I briefly summarise the non-homogeneous Bayesian regression DBN (BRDBN) model, proposed by Lèbre et al. (2010). Recently, various different variants of the original BR-DBN model have been developed, proposed and applied in the literature. Here I consider the uncoupled BR-DBN variant, which has been recently used in Grzegorczyk and Husmeier (2012a) and Grzegorczyk and Husmeier (2012b). Unlike all BR-DBN model instantiations that have been developed so far, I combine the BR-DBN model with a free allocation model rather than a multiple changepoint process. ${ }^{4}$ The free allocation BR-DBN model, considered here, allows for more flexibility with respect to the configuration space of the possible data allocations.

Consider a set of $N$ nodes, $g \in\{1, \ldots, N\}$, in a network, $\mathcal{M}=\left(\boldsymbol{\pi}_{1}(\mathcal{M}), \ldots, \boldsymbol{\pi}_{N}(\mathcal{M})\right)$, where $\boldsymbol{\pi}_{g}(\mathcal{M})$ denotes the parents of node $g$ in $\mathcal{M}$, that is the set of nodes with a directed

[^0]
[^0]:    ${ }^{4}$ Note that similar free allocation mixture DBN approaches have earlier been proposed by Ko et al. (2007) and Grzegorczyk et al. (2008).

edge pointing to node $g$. For notational convenience, I write $\boldsymbol{\pi}_{g}=\boldsymbol{\pi}_{g}(\mathcal{M})$ in the following representations; i.e. I do not indicate the dependency on $\mathcal{M}$ explicitly .

Given a $N$-by- $T$ data set matrix, $\mathcal{D}$, where the rows correspond to the $N$ nodes and the columns correspond to $T$ temporal observations, let $y_{g, t}$ denote the realisation of the random variable associated with node $g$ at time point $t \in\{1, \ldots, T\}$, and let $\mathbf{x}_{\boldsymbol{\pi}_{g}, t}$ denote the vector of realisations of the random variables associated with the parent nodes of node $g, \pi_{g}$, at the previous time point, $(t-1)$, and including a constant element equal to 1 (for the intercept). With $\left|\boldsymbol{\pi}_{g}\right|$ denoting the cardinality of the parent node set $\boldsymbol{\pi}_{g}$, the vector $\mathbf{x}_{\boldsymbol{\pi}_{g}, t}$, which also includes the element 1 for the intercept, is of size $\left|\boldsymbol{\pi}_{g}\right|+1$.

Unlike the mixture model DBN in Grzegorczyk et al. (2008) I here consider node-specific allocation vectors, $\mathbf{V}_{g}(g=1, \ldots, N)$, where each vector $\mathbf{V}_{g}$ is of size $T$ and defines a free allocation of the last $T-1$ observations, $y_{g, 2}, \ldots, y_{g, T}$, of node $g$ to $\mathcal{K}_{g}$ components. $\mathbf{V}_{g}(t)=k$ means that the observation $y_{g, t}$ is allocated to the $k$ th component $(t=2, \ldots, T$ and $k=1, \ldots, \mathcal{K}_{g}$ ). Furthermore, I define $\mathbf{y}_{g, k}$ to be the vector of observations that have been allocated to component $k$ by $\mathbf{V}_{g}\left(1 \leq k \leq \mathcal{K}_{g}\right)$. In the free allocation regression models, described below, the nodes $g=1, \ldots, N$ are considered as target variables and their regressor variables are the variables in their parent sets, namely $\boldsymbol{\pi}_{1}, \ldots, \boldsymbol{\pi}_{N}$. More precisely, $\mathbf{y}_{g, k}$ is the target vector for component $k$, and I have to arrange the corresponding observations of the parent nodes, $\boldsymbol{\pi}_{g}$, appropriately in a regressor (or design) matrix, which I denote $\mathbf{X}_{\boldsymbol{\pi}_{g}, k}$. Let the vector $\mathbf{y}_{g, k}$ be of size $n_{k}$, i.e. let $n_{k}$ observations have been allocated to component $k$, then $\mathbf{X}_{\boldsymbol{\pi}_{g}, k}$ is an $\left(\left|\boldsymbol{\pi}_{g}\right|+1\right)$-by- $n_{k}$ matrix, and if the $j$ th element of the target vector $\mathbf{y}_{g, k}$ is the observation $y_{g, t}$, then the $j$ th column of the regressor matrix, $\mathbf{X}_{\boldsymbol{\pi}_{g}, k}$, has to be the vector $\mathbf{x}_{\boldsymbol{\pi}_{g}, t}$. As each vector $\mathbf{x}_{\boldsymbol{\pi}_{g}, t}$ includes a constant element for the intercept, the first row of the design matrix, $\mathbf{X}_{\boldsymbol{\pi}_{g}, k}$, is a column vector of 1 's, which corresponds to the intercept.

Given a fixed graph topology $\mathcal{M}$, which implies the parent node sets, $\pi_{g}$, and thus the regressor variables for each node $g$, as well as fixed allocation vectors, $\mathbf{V}_{g}$, which imply the node-specific allocations, I follow Lèbre et al. (2010) and apply a linear Gaussian regression model to each target vector $\mathbf{y}_{g, k}$ using $\mathbf{X}_{\boldsymbol{\pi}_{g}, k}$ as regressor matrix:

$$
\mathbf{y}_{g, k}=\mathbf{X}_{\boldsymbol{\pi}_{g}, k}^{\top} \mathbf{w}_{g, k}+\varepsilon_{g, k}
$$

where $\mathbf{w}_{g, k}$ is the $\left(\left|\boldsymbol{\pi}_{g}\right|+1\right)$-dimensional vector of regression parameters, $\varepsilon_{g, k}$ is the noise vector, and the superscript symbol " $T$ " denotes matrix transposition. I assume that the individual elements of the noise vectors, $\varepsilon_{g, k}$, are i.i.d. Gaussian distributed with zero mean and variance $\sigma_{g}^{2}$; i.e. the noise variances are node-specific but do not depend on the component $k .{ }^{5}$ The vectors $\varepsilon_{g, k}\left(k=1, \ldots, \mathcal{K}_{g}\right)$ are then independently multivariate Gaussian distributed with zero mean vector and covariance matrix $\sigma_{g}^{2} \mathbf{I}$, where $\mathbf{I}$ denotes the unit matrix. The likelihood of the regression model is given by:

$$
P\left(\mathbf{y}_{g, k} \mid \mathbf{X}_{\boldsymbol{\pi}_{g}, k}, \mathbf{w}_{g, k}, \sigma_{g}\right)=\mathcal{N}\left(\mathbf{y}_{g, k} \mid \mathbf{X}_{\boldsymbol{\pi}_{g}, k}^{\top} \mathbf{w}_{g, k}, \sigma_{g}^{2} \mathbf{I}\right)
$$

On the component-specific regression parameter vectors, $\mathbf{w}_{g, k}$, I impose the following conjugate Gaussian priors:

$$
P\left(\mathbf{w}_{g, k} \mid \sigma_{g}^{2}, \delta_{g}\right)=\mathcal{N}\left(\mathbf{w}_{g, k} \mid \mathbf{0}, \delta_{g} \sigma_{g}^{2} \mathbf{I}\right)
$$

[^0]
[^0]:    5 This corresponds to the "noise variance hyperparameter coupling scheme" (S7) in Table 2 in Grzegorczyk and Husmeier (2013). In Grzegorczyk and Husmeier (2013) this coupling scheme lead to better results than node- and segment-specific noise variance hyperparameters, $\sigma_{g, k}^{2}$.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Compact representation of the employed free allocation Bayesian regression model. The grey circles refer to fixed (hyper-)parameters and the data ( $\mathbf{X}_{\pi_{g}, k}$ and $\mathbf{y}_{g, k}$ ), while the white circles refer to free (hyper-)parameters. A detailed model description is provided in Sect. 2.1
where $\delta_{g}$ can be interpreted as a gene-specific "signal-to-noise" (SNR) hyperparameter (Lèbre et al. 2010). On the inverse noise variances, $\sigma_{g}^{-2}$, and on the inverse SNR hyperparameters, $\delta_{g}^{-1}$, I also impose conjugate priors, i.e. Gamma priors:

$$
\begin{aligned}
P\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right) & =\operatorname{Gamma}\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right)=\frac{\left[B_{\sigma}\right]^{A_{\sigma}}}{\Gamma\left(A_{\sigma}\right)}\left[\sigma_{g}^{-2}\right]^{A_{\sigma}-1} e^{-B_{\sigma} \sigma_{g}^{-2}} \\
P\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right) & =\operatorname{Gamma}\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right)=\frac{\left[B_{\delta}\right]^{A_{\delta}}}{\Gamma\left(A_{\delta}\right)}\left[\delta_{g}^{-1}\right]^{A_{\delta}-1} e^{-B_{\delta} \delta_{g}^{-1}}
\end{aligned}
$$

with the fixed level-2 hyperparameters $A_{\sigma}, B_{\sigma}, A_{\delta}$ and $B_{\delta}$. A compact representation of the relationships among the (hyper-)parameters of the Bayesian regression models, described above, can be found in Fig. 1. The free model parameters, indicated by white circles in Fig. 1, have to be sampled from the posterior distribution. Due to standard conjugacy arguments the full conditional distributions of the free parameters can be computed in closed form, and the Gibbs-sampling scheme from Grzegorczyk and Husmeier (2012b) can be applied to generate a sample from the posterior distribution $P\left(\mathbf{w}_{g, 1}, \ldots, \mathbf{w}_{g, \mathcal{K}_{g}}, \delta_{g}, \sigma_{g}^{2} \mid \mathcal{D}\right) .{ }^{6}$

To indicate the allocations implied by the allocation vector $\mathbf{V}_{g}$, I introduce the symbols:

$$
\begin{aligned}
\mathbf{y}_{g}, \mathbf{v}_{g} & :=\left\{\mathbf{y}_{g, k}\right\}_{k=1, \ldots, \mathcal{K}_{g}} \\
\mathbf{X}_{\pi_{g}}, \mathbf{v}_{g} & :=\left\{\mathbf{X}_{\pi_{g}, k}\right\}_{k=1, \ldots, \mathcal{K}_{g}} \\
\mathbf{w}_{g}, \mathbf{v}_{g} & :=\left\{\mathbf{w}_{g, k}\right\}_{k=1, \ldots, \mathcal{K}_{g}}
\end{aligned}
$$

[^0]
[^0]:    ${ }^{6}$ Note that according to the earlier definitions the data set, $\mathcal{D}$, includes both: (i) the values of the target variable vectors, $\mathbf{y}_{g, k}$, which are here assumed to be realisations of random variables, and (ii) the values of the regressor matrices, $\mathbf{X}_{g, k}$, which are here assumed to be non-random observations.

Table 1 The MCMC sampling scheme for the free allocation Bayesian regression model shown in Fig. 1

```
For each node \(g=1, \ldots, N\)
Input: The parent node set, \(\pi_{g}\), the allocation vector, \(\mathbf{V}_{g}\), and the current SNR
    hyperparameter, \(\delta_{g}^{(i-1)}\)
MCMC iteration: \((i-1) \rightarrow i\)
    - Conditional on \(\delta_{g}^{(i-1)}\) sample a concrete variance hyperparameter, \(\sigma_{g}^{(i)}\) from
        \(P\left(\sigma_{g}^{-2} \mid \mathbf{y}_{g}, \mathbf{v}_{g}, \mathbf{X}_{\pi_{g}, \mathbf{v}_{g}}, \delta_{g}^{(i-1)}\right)\) [see Eq. (10)]
    - Afterwards sample component-specific regression parameter vectors, \(\mathbf{w}_{g, k}^{(i)}\) from
        \(P\left(\mathbf{w}_{g, k} \mid \mathbf{y}_{g, k}, \mathbf{X}_{\pi_{g}, k}, \sigma_{g}^{(i)}, \delta_{g}^{(i-1)}\right)\) [see Eq. (9)]
    Set: \(\mathbf{w}_{g, \mathbf{v}_{g}}^{(i)}:=\left(\mathbf{w}_{g, 1}^{(i)}, \ldots, \mathbf{w}_{g, \mathcal{K}_{g}}^{(i)}\right)\)
    - Sample a new SNR hyperparameter \(\delta_{g}^{(i)}\) from \(P\left(\delta_{g}^{-1} \mid \mathbf{w}_{g, \mathbf{v}_{g}}^{(i)}, \sigma_{g}^{(i)}\right)\)
    [see Eq. (8)], and output: \(\delta_{g}^{(i)}\)
```

This table provides pseudo-code only; see Sect. 2.1 for a detailed description of the MCMC sampling scheme

The full conditional distributions of $\delta_{g}^{-1}$ and $\mathbf{w}_{g, k}$ are given by:

$$
\begin{aligned}
& \delta_{g}^{-1} \mid\left(\mathbf{w}_{g, \mathbf{v}_{g}}, \sigma_{g}^{2}\right) \sim \operatorname{Gam}\left(A_{\delta}+\frac{\mathcal{K}_{g}\left(\left|\boldsymbol{\pi}_{g}\right|+1\right)}{2}, B_{\delta}+\frac{1}{2 \sigma_{g}^{2}} \sum_{k=1}^{\mathcal{K}_{g}} \mathbf{w}_{g, k}^{\top} \mathbf{w}_{g, k}\right) \\
& \mathbf{w}_{g, k} \mid\left(\mathbf{y}_{g, k}, \mathbf{X}_{\pi_{g}, k}, \sigma_{g}^{2}, \delta_{g}\right) \sim \mathcal{N}\left(\Sigma_{g, k}^{\star} \mathbf{X}_{\pi_{g}, k} \mathbf{y}_{g, k}, \sigma_{g}^{2} \Sigma_{g, k}^{\star}\right)
\end{aligned}
$$

where $\mathcal{K}_{g}$ is the number of components for node $g,\left|\boldsymbol{\pi}_{g}(\mathcal{M})\right|$ is the cardinality of the parent set, $\boldsymbol{\pi}_{g}$, and $\Sigma_{g, k}^{\star}=\left(\delta_{g}^{-1} \mathbf{I}+\mathbf{X}_{\pi_{g}, k} \mathbf{X}_{\pi_{g}, k}^{\top}\right)^{-1}$.

The inverse variance hyperparameters, $\sigma_{g}^{-2}$, could also be sampled from the full conditional distribution, but a computationally more efficient way is to to use a collapsed Gibbs sampling step, in which the regression parameter vectors, $\mathbf{w}_{g, k}$, have been integrated out. This marginalization yields:

$$
\sigma_{g}^{-2} \mid\left(\mathbf{y}_{g}, \mathbf{v}_{g}, \mathbf{X}_{\pi_{g}}, \mathbf{v}_{g}, \delta_{g}\right) \sim \operatorname{Gam}\left(A_{\sigma}+\frac{T-1}{2}, B_{\sigma}+\frac{\sum_{k=1}^{K_{g}} \Delta_{g, k}^{2}}{2}\right)
$$

with the squared Mahalanobis distance $\Delta_{g, k}^{2}=\mathbf{y}_{g, k}^{\top}\left(\mathbf{I}+\delta_{g} \mathbf{X}_{\pi_{g}, k}^{\top} \mathbf{X}_{\pi_{g}, k}\right)^{-1} \mathbf{y}_{g, k}$.
If the parent node sets, $\boldsymbol{\pi}_{g}$, and the allocation vectors, $\mathbf{V}_{g}$, are known and kept fixed, Eqs. (8-10) can be used, as indicated in Table 1, to generate a sample from the posterior distribution:

$$
P\left(\mathbf{w}_{g, \mathbf{v}_{g}}, \delta_{g}, \sigma_{g}^{2} \mid \mathcal{D}\right) \propto \prod_{g} P\left(\delta_{g}\right) P\left(\sigma_{g}^{2}\right) \prod_{k} P\left(\mathbf{w}_{g, k} \mid \delta_{g}, \sigma_{g}\right) P\left(\mathbf{y}_{g, k} \mid \mathbf{X}_{\pi_{g}, k}, \sigma_{g}, \mathbf{w}_{g, k}\right)
$$

However, in real-wold applications the allocation vectors, $\mathbf{V}_{g}$, are usually unknown and the objective is to infer the parent node sets, $\boldsymbol{\pi}_{g}$, which form the network structure, $\mathcal{M}=\left(\boldsymbol{\pi}_{1}, \ldots, \boldsymbol{\pi}_{N}\right)$. Note that the regression model is defined such that the likelihood

can be marginalized over both the regression parameters, $\mathbf{w}_{g, k}$, and the noise variance hyperparameters, $\sigma_{g, k}$. For each node $g$ the marginal likelihood is given by:

$$
P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{\pi_{g}, \mathbf{V}_{g}}, \delta_{g}\right)=\frac{\Gamma\left(\frac{T-1}{2}+A_{\sigma}\right)\left(2 B_{\sigma}\right)^{A_{\sigma}}}{\Gamma\left(A_{\sigma}\right)(\pi)^{(T-1) / 2} \prod_{k=1}^{K_{\sigma}}\left|\tilde{\boldsymbol{\Sigma}}_{g, k}\right|^{1 / 2}}\left(2 B_{\sigma}+\Delta_{g}^{2}\right)^{-\left(\frac{T-1}{2}+A_{\sigma}\right)}
$$

where $\tilde{\boldsymbol{\Sigma}}_{g, k}=\mathbf{I}+\delta_{g} \mathbf{X}_{\pi_{g}, k}^{\top} \mathbf{X}_{\pi_{g}, k}, \Delta_{g}^{2}=\sum_{k=1}^{K_{g}} \Delta_{g, k}^{2}$, and the squared Mahalanobis distance terms, $\Delta_{g, k}^{2}$, were defined below Eq. (10); for a derivation see Grzegorczyk and Husmeier (2012b). Note that the marginal likelihood in Eq. (12) is invariant with respect to a permutation of the components' labels, as I have imposed exchangeable (i.i.d.) priors on the componentspecific regression parameter vectors [see Eq. (2)].

# 2.2 Network structure inference 

I assume the allocation vectors, $\mathbf{V}_{g}$, still to be fixed, and I describe how the network structure, $\mathcal{M}$, can be inferred. For the prior on the network structures, $\mathcal{M}=\left(\pi_{1}, \ldots, \pi_{N}\right)$, I assume a modular form:

$$
P(\mathcal{M})=\prod_{g=1}^{N} P\left(\pi_{g}\right)
$$

and uniform distributions for $P\left(\pi_{g}\right)$, subject to a fan-in restriction, $\left|\pi_{g}\right| \leq \mathcal{F}$, for each $g$. The individual parent node sets, $\pi_{g}$, can then be inferred independently for each node $g$, and the collection of parent node sets forms the network structure, $\mathcal{M}=\left(\pi_{1}, \ldots, \pi_{N}\right)$. For each node $g$ the full conditional distribution is given by:

$$
P\left(\pi_{g} \mid \mathcal{D}, \mathbf{V}_{g}, \delta_{g}\right) \propto P\left(\pi_{g}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{\pi_{g}, \mathbf{V}_{g}}, \delta_{g}\right)
$$

where the expressions for $P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{\pi_{g}, \mathbf{V}_{g}}, \delta_{g}\right)$ can be computed with Eq. (12).
As the full conditional distribution of $\pi_{g}$ in Eq. (14) is not of closed form, I resort to Metropolis-Hastings sampling techniques. For each node $g$ the MCMC algorithm keeps the SNR-hyperparameter, $\delta_{g}$, and the allocation vector, $\mathbf{V}_{g}$, fixed, and proposes to move from the current parent node set, $\pi_{g}^{(i-1)}$, to a new set $\pi_{g}^{(\diamond)}$, where $\pi_{g}^{(\diamond)}$ is randomly chosen from the system $\mathcal{S}\left(\pi_{g}^{(i-1)}\right)$ of all parent sets which can be reached (i) either by removing a single parent node from $\pi_{g}^{(i-1)}$, (ii) or by adding a single parent node to $\pi_{g}^{(i-1)}$, unless the maximal fan-in, $\mathcal{F}$, is reached, (iii) or by a parent-node flip move. ${ }^{7}$ According to the Metropolis Hastings criterion, the move is accepted with probability

$$
A\left(\pi_{g}^{(i-1)} \rightarrow \pi_{g}^{(\diamond)}\right)=\min \left\{1, \frac{P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{\pi_{g}^{(\diamond)}, \mathbf{V}_{g}}, \delta_{g}\right)}{P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{\pi_{g}^{(i-1)}, \mathbf{V}_{g}}, \delta_{g}\right)} \times \frac{P\left(\pi_{g}^{(\diamond)}\right)}{P\left(\pi_{g}^{(i-1)}\right)} \times \frac{\left|\mathcal{S}\left(\pi_{g}^{(i-1)}\right)\right|}{\left|\mathcal{S}\left(\pi_{g}^{\diamond}\right)\right|}\right\}
$$

where the likelihood-ratio can be computed with Eq. (12), the prior ratio is equal to 1, and the Hastings-ratio is the ratio of the cardinalities of the two parent node set systems

[^0]
[^0]:    ${ }^{7}$ The parent-node flip move was proposed in Grzegorczyk and Husmeier (2011) and randomly chooses a parent node, $u \in \pi_{g}^{(i-1)}$, and randomly chooses a node $v \notin \pi_{g}^{(i-1)}$, and then modifies $\pi_{g}^{(i-1)}$ by substituting parent node $u$ for node $v$.

Table 2 Pseudo-code for the MCMC inference of the parent node sets, $\pi_{g}$, in the free allocation Bayesian regression model shown in Fig. 1

For each node $g=1, \ldots, N$ :
Input: The SNR hyperparameter, $\delta_{g}$, the allocation vector, $\mathbf{V}_{g}$, and the current parent node set, $\pi_{g}^{(i-1)}$
MCMC iteration: $(i-1) \rightarrow i$ :

- Determine the system of parents sets, $\mathcal{S}\left(\pi_{g}^{(i)}\right)$, that is the system of parent node sets that can be reached from $\pi_{g}^{(i-1)}$ by (i) either adding a node to $\pi_{g}^{(i-1)}$, (ii) or by deleting a node from $\pi_{g}^{(i-1)}$ or (iii) by exchanging a node $u \in \pi_{g}^{(i-1)}$ for a node $v \notin \pi_{g}^{(i-1)}$. Randomly select a new candidate parent set, $\pi_{g}^{(\diamond)}$, from $\mathcal{S}\left(\pi_{g}^{(i)}\right)$
- Accept the new parent node set, $\pi_{g}^{(\diamond)}$, with the probability given in Eq. (15). If the move is accepted, set: $\pi_{g}^{(i)}=\pi_{g}^{(\diamond)}$. Otherwise leave the parent set unchanged, i.e. set $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$. Output $\pi_{g}^{(i)}$
$\mathcal{S}\left(\pi_{g}^{(i-1)}\right)$ and $\mathcal{S}\left(\pi_{g}^{\diamond}\right) .{ }^{8}$ If the move is accepted, set: $\pi_{g}^{(i)}=\pi_{g}^{(\diamond)}$, or otherwise leave the set unchanged, $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$. Pseudo code for this Metropolis-Hastings step is given in Table 2. Given the current network, $\mathcal{M}^{(i-1)}=\left(\pi_{1}^{(i-1)}, \ldots, \pi_{N}^{(i-1)}\right)$, successively updating the parent node sets, symbolically $\pi_{g}^{(i-1)} \rightarrow \pi_{g}^{(i)}(g=1, \ldots, N)$, yields the new network $\mathcal{M}^{(i)}=\left(\pi_{1}^{(i)}, \ldots, \pi_{N}^{(i)}\right)$.


# 2.3 Modelling the allocation vectors 

In the last two subsections I have assumed that the allocation vectors are known and fixed, although they will be unknown in many real-world applications. The focus of this subsection is on inferring the allocation vectors from the data. A common choice in the context of dynamic Bayesian networks (DBNs) is the application of (node-specific) multiple changepoint processes to infer the segmentations; see references in Sect. 1.

Another approach, presented in Ko et al. (2007) and Grzegorczyk et al. (2008), is to combine DBNs with a mixture model. The mixture approach is more flexible, as it allows for a free allocation of the data points. E.g. for 11 data points and 3 mixture components the allocation scheme $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,3,2,3,1,2,2,1,1]$ for the last 10 data points is valid. The changepoint approach imposes sets of changepoints to divide the temporal data points into disjunct segments. Since temporal observations follow a natural time ordering and a priori neighbouring time points should be more likely to be allocated to the same component than distant time points, the changepoint approach includes plausible prior knowledge. However, changepoint approaches have a restricted allocation space, since data points in different segments have to be allocated to different components; i.e. "a (segment) component once left cannot be revisited". Consequently, certain allocation schemes can only be approximated by imposing additional changepoints, e.g. in this example the true allocation scheme $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,1,2,2,2,1,1,1,1]$ cannot be modelled properly with changepoints; the best changepoint set approximation might be: $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,1,2,2,2,3,3,3,3]$. The mixture model, on the other hand, can infer the correct allocation, but it ignores the temporal ordering of the data points. That is, it treats the temporal data points (time points) as interchangeable units. This information

[^0]
[^0]:    ${ }^{8}$ The prior ratio is equal to 1 , as I have imposed a uniform distribution on the parent node sets. Due to the fan-in restriction the cardinalities of the two systems of parent node sets can be different.

loss implies in this example that all $\binom{10}{3}$ allocation vectors, which allocate seven time points to component $k=1$ and three time points to component $k=2$, are a priori equally likely; including allocation schemes, such as $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,2,1,1,1,2,1,1,2,1]$, which might be very unlikely a priori.

A compromise between the mixture model and the changepoint process is a hidden Markov model (HMM). In HMMs there is a homogeneous Markovian dependency between the allocations of the data points. In a Markov chain of order $\tau=1$ the allocation (state) of the $t$ th data point given the states of all earlier time points $2,3,4, \ldots, t-1$ just depends on the state of the immediately preceding time point $t-1$. Moreover, in a homogeneous Markov chain these transition probabilities stay constant over time, i.e. they do not depend on $t$. The homogeneous state-transition probabilities can be chosen such that neighbouring points are likely to be allocated to the same state, and states once left can be revisited. In this subsection I show how to employ a HMM for the allocation vectors, $\mathbf{V}_{g}$.

I model the allocation vectors, $\mathbf{V}_{g}$, for each node, $g$, independently with a HMM. In a first step I impose a truncated Poisson distribution with parameter $\lambda$ on the number of states (components). For $\mathcal{K}_{g}=1, \ldots, \mathcal{K}_{M A X}$ this yields:

$$
P\left(\mathcal{K}_{g}\right)=\operatorname{Poi}\left(\mathcal{K}_{g} \mid \lambda, 1 \leq \mathcal{K}_{g} \leq \mathcal{K}_{M A X}\right) \propto \frac{\lambda^{\mathcal{K}_{g}} \cdot e^{-\lambda}}{\mathcal{K}_{g}!}
$$

Afterwards, I impose a HMM with $\mathcal{K}_{g}$ states on the allocation vector, $\mathbf{V}_{g}$. The allocation vector can be identified with the temporally ordered sequence $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right]$ and its probability is the probability of the sequence: $P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=P\left(\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T) \mid \mathcal{K}_{g}\right)$. Assuming a Markovian dependency of order $\tau=1$ for the state sequence, this leads to:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=P\left(\mathbf{V}_{g}(2) \mid \mathcal{K}_{g}\right) \prod_{t=3}^{T} P\left(\mathbf{V}_{g}(t) \mid \mathbf{V}_{g}(t-1), \mathcal{K}_{g}\right)
$$

For $t=3, \ldots, T$ let $p_{k, j}^{g}$ denote the probability for a transition from state $k$ to state $j$ :

$$
p_{k, j}^{g}=P\left(\mathbf{V}_{g}(t)=j \mid \mathbf{V}_{g}(t-1)=k, \mathcal{K}_{g}\right)
$$

This gives $\sum_{j=1}^{\mathcal{K}_{g}} p_{k, j}^{g}=1$ and the probability vectors $\mathbf{p}_{k}^{g}=\left(p_{k, 1}^{g}, \ldots, p_{k, \mathcal{K}_{g}}^{g}\right)^{\top}$ define categorical (or multinomial) random variables $\left(k=1, \ldots, \mathcal{K}_{g}\right)$. On $\mathbf{V}_{g}(2)$ I impose a discrete uniform distribution with the possible outcomes $\left\{1, \ldots, \mathcal{K}_{g}\right\}$. The probability of the sequence $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right]$ conditional on $\left\{\mathbf{p}_{k}^{g}\right\}_{k}=\left\{\mathbf{p}_{k}^{g}\right\}_{k=1, \ldots, \mathcal{K}_{g}}$ is then given by:

$$
P\left(\mathbf{V}_{g} \mid\left\{\mathbf{p}_{k}^{g}\right\}_{k}\right)=\frac{1}{\mathcal{K}_{g}} \prod_{k=1}^{\mathcal{K}_{g}} \prod_{j=1}^{\mathcal{K}_{g}}\left(p_{k, j}^{g}\right)^{n_{k, j}}
$$

where $n_{k, j}=\left|\left\{t \mid 3 \leq t \leq T \wedge \mathbf{V}_{g}(t)=j \wedge \mathbf{V}_{g}(t-1)=k\right\}\right|$ is the number of transitions from state $k$ to state $j$ in the sequence $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right]$. For $k=1, \ldots \mathcal{K}_{g}$ I impose a Dirichlet distribution with hyperparameter vector $\boldsymbol{\alpha}_{k}=\left(\alpha_{k, 1}, \ldots, \alpha_{k, \mathcal{K}_{g}}\right)^{\top}$ on $\mathbf{p}_{k}^{g}$ :

$$
P\left(\mathbf{p}_{k}^{g}\right)=\operatorname{Dir}\left(\mathbf{p}_{k}^{g} \mid \boldsymbol{\alpha}_{k}\right)=\frac{\prod_{j=1}^{\mathcal{K}_{g}} \Gamma\left(\alpha_{k, j}\right)}{\Gamma\left(\sum_{j=1}^{\mathcal{K}_{g}} \alpha_{k, j}\right)} \prod_{j=1}^{\mathcal{K}_{g}}\left(p_{k, j}^{g}\right)^{\alpha_{k, j}-1}
$$

Marginalizing over the set $\left\{\mathbf{p}_{k}^{g}\right\}_{k}$ in Eq. (19) gives the marginal distribution:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=\int_{\left\{\mathbf{p}_{k}^{g}\right\}_{k}} P\left(\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T) \mid\left\{\mathbf{p}_{k}^{g}\right\}\right\}_{k}\right) \cdot P\left(\left\{\mathbf{p}_{k}^{g}\right\}_{k}\right) d\left\{\mathbf{p}_{k}^{g}\right\}_{k}
$$

With independently distributed random vectors $\mathbf{p}_{k}^{g}, P\left(\left\{\mathbf{p}_{k}^{g}\right\}_{k}\right)=\prod_{k=1}^{\mathcal{K}_{g}} P\left(\mathbf{p}_{k}^{g}\right)$, where $P\left(\mathbf{p}_{k}^{g}\right)$ was defined in Eq. (20), the integral in Eq. (21) is effectively a product integral. Inserting Eq. (19) into Eq. (21) yields:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=\frac{1}{\mathcal{K}_{g}} \prod_{k=1}^{\mathcal{K}_{g}}\left(\int_{\mathbf{p}_{k}^{g}} P\left(\mathbf{p}_{k}^{g}\right) \prod_{j=1}^{\mathcal{K}_{g}}\left(p_{k, j}^{g}\right)^{n_{k, j}} d \mathbf{p}_{k}^{g}\right)
$$

The inner integrals correspond to Dirichlet-multinomial distributions, which can be computed in closed form. This yields:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=\frac{1}{\mathcal{K}_{g}} \prod_{k=1}^{\mathcal{K}_{g}} \frac{\Gamma\left(\sum_{j=1}^{\mathcal{K}_{g}} \alpha_{k, j}\right)}{\Gamma\left(\sum_{j=1}^{\mathcal{K}_{g}} n_{k, j}+\alpha_{k, j}\right)} \prod_{j=1}^{\mathcal{K}_{g}} \frac{\Gamma\left(n_{k, j}+\alpha_{k, j}\right)}{\Gamma\left(\alpha_{k, j}\right)}
$$

In the absence of any genuine prior knowledge about the state-transition probabilities, $p_{k, j}^{g}$, I set $\alpha_{k, j}=\alpha$ in Eq. (20). The marginal distribution $P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)$ in Eq. (23) is then invariant to permutations of the states' labels.

# 2.4 The proposed HMM-DBN model 

The proposed Hidden Markov model (HMM) dynamic Bayesian network (DBN) model, which I refer to as the HMM-DBN model, is now fully specified. A compact representation of the relationships among the data and all (hyper-)parameters of the HMM-DBN model is given in Fig. 2. Figure 2 adds flexible parent node sets and allocation vectors along with their prior distributions to Fig. 1. Unlike the earlier Bayesian regression DBN model, shown in Fig. 1, the parent node sets and the allocation vectors are now flexible and have to be inferred. The joint posterior distribution of the HMM-DBN model is given by:

$$
P\left(\mathcal{M}, \mathbf{V}_{1}, \ldots, \mathbf{V}_{N}, \delta_{1}, \ldots, \delta_{N}, \mathcal{K}_{1}, \ldots, \mathcal{K}_{N} \mid \mathcal{D}\right)=\prod_{g=1}^{N} P\left(\pi_{g}, \mathbf{V}_{g}, \mathcal{K}_{g}, \delta_{g} \mid \mathcal{D}\right)
$$

where $\mathcal{M}=\left(\pi_{1}, \ldots, \pi_{N}\right)$, and

$$
P\left(\pi_{g}, \mathbf{V}_{g}, \mathcal{K}_{g}, \delta_{g} \mid \mathcal{D}\right) \propto P\left(\delta_{g}\right) P\left(\pi_{g}\right) P\left(\mathcal{K}_{g}\right) P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{g, \mathbf{V}_{g}}, \delta_{g}\right)
$$

In the latter equation $\mathcal{K}_{g}$ is the number of possible states (components) for the $g$ th allocation vector, $\mathbf{V}_{g}$, which implies the target vector segmentation, $\mathbf{y}_{g, \mathbf{V}_{g}}=\left\{\mathbf{y}_{g, 1}, \ldots, \mathbf{y}_{g, \mathcal{K}_{g}}\right\}$, and the segmentation of the regressor matrices, $\mathbf{X}_{\pi_{g}, \mathbf{V}_{g}}=\left\{\mathbf{X}_{\pi_{g}, 1}, \ldots, \mathbf{X}_{\pi_{g}, \mathcal{K}_{g}}\right\}$. The marginal likelihood, $P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{g, \mathbf{V}_{g}}, \delta_{g}\right)$, can be computed with Eq. (12).

With regard to the MCMC inference, described in Sect. 2.5, note that the posterior distribution in Eq. (24) is invariant (to permutations of the states' labels), as the marginal likelihood in Eq. (12) and the priors on the allocation vector in Eq. (23) (if $\alpha_{k, j}=\alpha$ ) are invariant. For Bayesian mixture models with invariant posterior distributions it is challenging to infer the component-specific model parameters, since their marginal posterior distributions are identical. There is a so called "non-identifiability problem" with respect to the components' labels (see, e.g., Nobile and Fearnside 2007). For the HMM-DBN model the problem of

![img-1.jpeg](img-1.jpeg)

Fig. 2 Compact representation of the proposed HMM-DBN model. The graphical model in Fig. 1 has been extended by additional fixed (grey circles) and free (white circles) (hyper-)parameters. Detailed descriptions of the HMM-DBN model are provided in Sects. 2.1-2.3
non-identifiability has not be tackled, as the interest is not on state-specific parameters. Here, I am interested in the network structure, $\mathcal{M}$, and in the co-allocation of data points. ${ }^{9}$

# 2.5 Allocation vector inference 

For the allocation vector inference, in principle, two different RJMCMC sampling strategies (Green 1995) can be employed. The first technique is to implement a RJMCMC approach in a continuous configuration space, where concrete instantiations of all free parameters of the Bayesian regression model (i.e. the white circles in Fig. 1) are sampled, before the forwardbackward simulation algorithm (Boys et al. 2000) is used to sample the allocation vector from its full conditional distribution via a Gibbs sampling step. This RJMCMC approach for hidden Markov models has been proposed by Robert et al. (2000) and has become popular in various fields of applications, such as DNA sequence analysis (see, e.g., Boys and Henderson 2004). However, the disadvantage of this approach is that the variation of the number of

[^0]
[^0]:    ${ }^{9}$ For each node $g$ the allocation vector, $\mathbf{V}_{g}$, effectively defines a node-specific co-allocation matrix: $\mathbf{C}^{g}=$ $\left(C_{s, t}^{g}\right)_{s, t \in\{2, \ldots, T\}}$ with $C_{s, t}^{g}=1$ if $\mathbf{V}_{g}(s)=\mathbf{V}_{g}(t)$, and $C_{s, t}^{g}=0$ if $\mathbf{V}_{g}(s) \neq \mathbf{V}_{g}(t)$. Note that the node-specific co-allocation matrices, $\mathbf{C}^{g}$, are invariant to permutations of the states' labels. See, e.g., Jasra et al. (2005) for a detailed argumentation.

hidden states, $\mathcal{K}_{g}$, requires the implementation of efficient RJMCMC moves which switch between models with different dimensionalities in continuous parameter spaces. Otherwise, the RJMCMC simulations may become computationally inefficient (see, e.g., Nobile and Fearnside 2007).

The second sampling strategy is based on RJMCMC moves in the discrete allocation vector configuration space. In this approach the numbers of states and the allocation vectors are sampled from the posterior distribution. This strategy can be used when all state-specific parameters can be integrated out analytically so that the marginal likelihood does not depend on state-specific continuous parameters. ${ }^{10}$ The main advantage of this second RJMCMC strategy is that the resulting sampling scheme does not require any particular trans-dimensional jumping moves in continuous configuration spaces. In the present paper I resort to this second RJMCMC sampling strategy, and I employ the "allocation sampler" (Nobile and Fearnside 2007) for the allocation vector inference. The allocation sampler was proposed by Nobile and Fearnside (2007) and has already been utilised in the context of mixture dynamic Bayesian networks (MIX-DBNs) in Grzegorczyk et al. (2008). The allocation sampler consists of a simple Gibbs sampling move and various more involved Metropolis-Hastings moves. The mathematical details are briefly summarised in the "Appendix". In Appendix 1 I describe a simple Gibbs sampling move, which re-samples the allocation state of one single data point from the full conditional distribution. Since this type of move yields very small steps in the configuration space, Nobile and Fearnside (2007) proposed a set of more involved allocation sampler moves. In Appendix 2 I describe these allocation sampler moves, namely the M1, the M2, and the Ejection-Absorption (EA) move. However, the allocation sampler moves have been developed for free allocation models, where data points are treated as interchangeable units without any natural (here: temporal) arrangement. These moves are sub-optimal when a Markovian dependency structure among the (temporal) data points is given. In Sects. 2.5.1 and 2.5.2 I therefore propose two new pairs of Metropolis-Hastings moves, which exploit the temporal structure and thus improve convergence and mixing for the HMM-DBN model. While the conceptualization of the ideas behind these moves is relatively simple and intuitive, the mathematical implementation is involved, due to the need to ensure that the sampling scheme satisfies the equations of detailed balance and converges to the proper posterior distribution. In Appendices 3 and 4 I rigorously formulate the mathematical details, and I show for both pairs of moves that the two moves are complementary to each other. Hence, the acceptance probabilities can be chosen according to the Metropolis-Hastings criterion, so as to guarantee that the equation of detailed balance is fulfilled. Combining the SNR hyperparameter inference (see Table 1) and the network inference (see Table 2) with the moves on the allocation vectors yields the MCMC sampling scheme for generating a sample from the posterior distribution in Eq. (24). Table 3 shows how the sampling steps can be combined.

# 2.5.1 First pair of new HMM moves: the inclusion and the exclusion move 

In this subsection I propose and verbally describe the novel inclusion and the novel exclusion move for the HMM-DBN model. For each exclusion move there is a unique complementary inclusion move, and vice-versa. The introduction of this pair of moves can be best motivated by a simple example: Given 11 time points and the allocation $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,2,2,1,1,1,2,2,2]$ for the last 10 data points. If there is

[^0]
[^0]:    10 The proposed HMM-DBN model is based on the Bayesian regression model, shown in Fig. 1. Only the regression parameter vectors, $\mathbf{w}_{g, k}$, are state-specific. As the regression parameters can be integrated out analytically [see Eq. (10)], the marginal likelihood of the Bayesian regression model in Eq. (12) does not depend on concrete instantiations of state-specific parameters.

Table 3 Pseudo code for the MCMC sampling scheme

Input: The current state of the MCMC simulation. That is, the network:
$\mathcal{M}^{(i-1)}=\left(\pi_{1}^{(i-1)}, \ldots, \pi_{N}^{(i-1)}\right)$, the current numbers of states $\mathcal{K}_{1}^{(i-1)}, \ldots, \mathcal{K}_{N}^{(i-1)}$, the current allocation vectors, $\mathbf{V}_{1}^{(i-1)}, \ldots, \mathbf{V}_{N}^{(i-1)}$, and the current SNR hyperparameters, $\delta_{1}^{(i-1)}, \ldots, \delta_{N}^{(i-1)}$
MCMC iteration: $(i-1) \rightarrow i$ :

- Keep the network $\mathcal{M}^{(i-1)}$ and the allocation vectors, $\mathbf{V}_{g}^{(i-1)}(g=1, \ldots, N)$, fixed, and update the SNR hyperparameters with the MCMC sampling scheme described in Table 1. For each $g$ replace $\delta_{g}^{(i-1)}$ by the outputed new SNR hyperparameter, $\delta_{g}^{(i)}$
- Keep the allocation vectors $\mathbf{V}_{g}^{(i-1)}(g=1, \ldots, N)$ and the SNR hyperparameters $\delta_{g}^{(i)}$ $(g=1, \ldots, N)$ fixed, and update the network structure with the MCMC sampling scheme described in Table 2. Replace the old graph, $\mathcal{M}^{(i-1)}$, by the outputed new graph, $\mathcal{M}^{(i)}=\left(\pi_{1}^{(i)}, \ldots, \pi_{N}^{(i)}\right)$
- For $g=1, \ldots, N$ :

Keep the parent set, $\pi_{g}^{(i)}$, the number of states, $\mathcal{K}_{g}^{(i-1)}$, and the SNR hyperparameter, $\delta_{g}^{(i)}$, fixed, and perform the Gibbs sampling move, described in Appendix 1, on $\mathbf{V}_{g}^{(i-1)}$. Let $\mathbf{V}_{g}^{\dagger}$ denote the newly sampled allocation vector

- For $g=1, \ldots, N$ :

Keep the parent set, $\pi_{g}^{(i)}$, and the SNR hyperparameter, $\delta_{g}^{(i)}$, fixed. Draw a coin to decide whether an allocation sampler move (see Appendix 2) or a new HMM move (see Sects. 2.5.1 and 2.5.2 and Appendices 3 and 4) is performed on $\mathbf{V}_{g}^{\dagger}$

- If an allocation sampler move is performed, randomly draw the move type: M1, M2 or Ejection/Absorption, and perform the selected move on $\mathbf{V}_{g}^{\dagger}$. Output the new allocation vector, $\mathbf{V}_{g}^{(i)}$, and the new number of states, $\mathcal{K}_{g}^{(i)}$
- If a new HMM move is performed, randomly draw the move type: Inclusion, Exclusion, Birth or Death move, and perform the selected move on $\mathbf{V}_{g}^{\dagger}$
Output the new allocation vector, $\mathbf{V}_{g}^{(i)}$, and the new number of states, $\mathcal{K}_{g}^{(i)}$
Output: The new state of the MCMC simulation. That is, the new network structure:
$\mathcal{M}^{(i)}=\left(\pi_{1}^{(i)}, \ldots, \pi_{N}^{(i)}\right)$, the new numbers of states $\mathcal{K}_{1}^{(i)}, \ldots, \mathcal{K}_{N}^{(i)}$, the new allocation vectors, $\mathbf{V}_{1}^{(i)}, \ldots, \mathbf{V}_{N}^{(i)}$, and the new SNR hyperparameters, $\delta_{1}^{(i)}, \ldots, \delta_{N}^{(i)}$
a Markovian dependency structure, it appears to be useful to propose to re-allocate the coherent time sequence $\left[\mathbf{V}_{g}(4), \mathbf{V}_{g}(5)\right]=[2,2]$ to state $k=1$, since the surrounding earlier (lower) and later (higher) time points ( $\left[\mathbf{V}_{g}(2), \mathbf{V}_{g}(3)\right]$ and $\left[\mathbf{V}_{g}(6), \mathbf{V}_{g}(7), \mathbf{V}_{g}(8)\right]$ ) are allocated to $k=1$. The inclusion move proposes to "include" the surrounded sequence $\left[\mathbf{V}_{g}(4), \mathbf{V}_{g}(5)\right]$ into the state of the surrounding data points. This gives the new allocation $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,1,1,1,1,1,2,2,2]$. Given the new allocation, the complementary exclusion move has to cut the subsequence $\left[\mathbf{V}_{g}(4), \mathbf{V}_{g}(5)\right]$ out of the coherent sequence $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(8)\right]$ to move back to the original allocation. To this end, the exclusion move selects the coherent sequence $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(8)\right]$ of data points that are allocated to the same state $(k=1)$. Subsequently, it proposes to cut out a randomly selected subsequence, which is then "excluded", i.e. it is cut out and re-allocated to a new state (here: $k=2$ ). To guarantee that there is a complementary inclusion move for each exclusion move, it is important to impose a constraint: The randomly selected subsequence is not allowed to include the two limiting data points; i.e. the lower limit $\mathbf{V}_{g}(2)$ and the upper limit $\mathbf{V}_{g}(8)$ in

the example. In Appendix 3 I rigorously formulate the mathematical details, and I show that there is a unique exclusion move for each inclusion move, and vice-versa.

# 2.5.2 Second pair of new HMM moves: the birth and the death move 

In this subsection I propose and verbally describe the novel death and the novel birth move for the HMM-DBN model. For each birth move there is a unique complementary death move, and vice-versa. The introduction of this pair of novel Metropolis-Hastings moves can be best motivated by a simple example: Given 11 time points and the allocation vector $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,1,1,1,1,1,1,1,1]$ for the last 10 data points, then it appears to be useful to impose a changepoint, which re-allocates the last data points to a new state $k=2$. For example, re-allocating the last four data points yields the new allocation vector $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,1,1,1,1,2,2,2,2]$. The birth move randomly selects a state $k$ and re-allocates the last data points that are allocated to $k$ to a new state $k_{\text {new }}$. Thereby the novel birth move also allows for moves, such as $[1,1,2,2,1,1,2,2,1,1] \rightarrow[1,1,2,2,1,3,2,2,3,3]$, where the last two data points that were allocated to state $k=1$ have been re-allocated to a new state $k_{\text {new }}=3$.

Given the new allocation vector, $\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(11)\right]=[1,1,2,2,1,3,2,2,3,3]$ the complementary death move has to re-allocate all data points that are allocated to state $k=3$ back to state $k=1$. To this end the death move selects the two states $k=1$ and $k=3$, and then tests whether the data points allocated to state $k=1$ and the data points allocated to state $k=3$ are "separated" (do not "overlap"). Formally, I will say that the two sets $T_{1}=\{t$ : $\left.\mathbf{V}_{g}(t)=1\right\}$ and $T_{3}=\left\{t: \mathbf{V}_{g}(t)=3\right\}$ are separated if and only if: $\max \left(T_{1}\right)<\min \left(T_{3}\right)$ or $\min \left(T_{1}\right)>\max \left(T_{3}\right)$. If the "separation test" is successful, the death move is valid and can be performed. In the example, the highest time point allocated to $k=1$, namely $t=5$, precedes the lowest time point allocated to $k=3$, namely $t=6$, so that the "test for separation" is successful and the death move is valid. This formal test for separation is required, since otherwise the new allocation vector could not have been reached by the novel birth move, described above. In Appendix 4 I rigorously formulate the mathematical details, and I show that there is a unique novel death move for each novel birth move, and vice-versa.

### 2.6 Competing dynamic Bayesian network models

I will perform a systematic comparative evaluation, in which I compare the proposed HMMDBN model with three competing DBN models. The traditional homogeneous DBN model (HOM-DBN) is described in Sect. 2.6.1, and in Sects. 2.6.2 and 2.6.3 the free allocation mixture DBN model (MIX-DBN) and the changepoint-segmented DBN model (CPS-DBN) are briefly summarised. An overview to the models is given in Table 4.

### 2.6.1 The conventional homogeneous DBN model (HOM-DBN)

In the homogeneous DBN model the network interactions do not vary over time. There is only one single state, $\mathcal{K}_{g}=1$, for each node $g$ and the allocation vectors assign all data points to state $1, \mathbf{V}_{g}=(1, \ldots, 1)^{\top}$. The HOM-DBN is a special case of the HMM-DBN model, where $\mathcal{K}_{g}$ and $\mathbf{V}_{g}$ are fixed and non-adaptable. In Fig. 2 the nodes $\mathbf{V}_{g}$ and $\mathcal{K}_{g}$ become fixed (grey), and the nodes for $\alpha_{k}^{g}, \mathbf{p}_{k}^{g}, \mathcal{K}_{g}, \lambda$, and $\mathcal{K}_{M A X}$ can be removed. The HOM-DBN model can be inferred with the MCMC sampling scheme in Table 3, but the allocation vector moves have to be left out, as $\mathcal{K}_{g}^{(i)}=1$ and $\mathbf{V}_{g}^{(i)}=(1, \ldots, 1)^{\top}$ for all $i$.

Table 4 Overview to the four (non-)homogeneous dynamic Bayesian network models


Detailed explanations are given in the main text

# 2.6.2 The non-homogeneous mixture DBN model (MIX-DBN) 

The mixture DBN model (MIX-DBN) combines the traditional DBN model with a free allocation mixture model. As for the HMM-DBN model, I assume that the numbers of mixture components follow truncated Poisson distributions, $P\left(\mathcal{K}_{g}\right) \propto \operatorname{Poi}(\lambda)$ for $1 \leq \mathcal{K}_{g} \leq$ $\mathcal{K}_{\text {MAX }}$. And I impose a categorical (multinomial) distribution with hyperparameters $\mathbf{p}^{g}=$ $\left(p_{1}^{g}, \ldots, p_{\mathcal{K}_{g}}^{g}\right)^{\top}$ on the components, $p_{k}^{g}:=P\left(\mathbf{V}_{g}(t)=k \mid \mathcal{K}_{g}\right)$ for all $t>2$. The probability of the allocation vector is then given by:

$$
P\left(\mathbf{V}_{g} \mid \mathbf{p}^{g}\right)=\prod_{k=1}^{\mathcal{K}_{g}}\left(p_{k}^{g}\right)^{n_{k}}
$$

where $n_{k}=\left|\left\{t \mid 2 \leq t \leq T \wedge \mathbf{V}_{g}(t)=k\right\}\right|$ is the number of data points that are allocated to component $k$ by $\mathbf{V}_{g}$. On $\mathbf{p}^{g}$ I impose a conjugate Dirichlet distribution with hyperparameters $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{\mathcal{K}_{g}}\right)^{\top}, P\left(\mathbf{p}^{g}\right)=\operatorname{Dir}\left(\mathbf{p}^{g} \mid \boldsymbol{\alpha}\right)$. Marginalizing over $\mathbf{p}^{g}$ yields:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=\frac{\Gamma\left(\sum_{k=1}^{\mathcal{K}_{g}} \alpha_{k}\right)}{\Gamma\left(\sum_{k=1}^{\mathcal{K}_{g}}\left(n_{k}+\alpha_{k}\right)\right)} \prod_{k=1}^{\mathcal{K}_{g}} \frac{\Gamma\left(n_{k}+\alpha_{k}\right)}{\Gamma\left(\alpha_{k}\right)}
$$

For $\alpha_{k}=\alpha$ the posterior distribution of the MIX-DBN model becomes invariant to permutations of the components' labels. The MIX-DBN model can be inferred with the MCMC sampling scheme in Table 3, but exclusively allocation sampler moves can be performed on $\mathbf{V}_{g}$. The moves from Sects. 2.5.1 and 2.5.2 cannot be used, as the MIX-DBN model treats the data points as interchangeable units (without any ordering). If the allocation sampler moves, described in Appendix 2, are performed, the terms $P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)$ in the acceptance probabilities have to be computed with Eq. (27) instead of Eq. (23).

### 2.6.3 The non-homogeneous changepoint DBN model (CPS-DBN)

The changepoint DBN model (CPS-DBN) combines the traditional DBN model with a multiple changepoint process. As before, I assume that $\mathcal{K}_{g}$ follows a truncated Poisson distribution, $P\left(\mathcal{K}_{g}\right) \propto \operatorname{Poi}(\lambda)$ for $1 \leq \mathcal{K}_{g} \leq \mathcal{K}_{\text {MAX }}$. I identify $\mathcal{K}_{g}$ with $\mathcal{K}_{g}-1$ changepoints $b_{g, 1}, \ldots, b_{g, \mathcal{K}_{g}-1}$ on the set $\{2, \ldots, T-1\}$. For node $g$ this yields: $\mathbf{V}_{g}(t)=k$ if and only if $b_{g, k-1}<t \leq b_{g, k}$, where $b_{g, 0}:=1$ and $b_{g, \mathcal{K}_{g}}:=T$. Following Green (1995) I assume that the changepoints are distributed as the even-numbered order statistics of $\mathcal{L}:=2\left(\mathcal{K}_{g}-1\right)+1$ points uniformly and independently distributed on the set $\{2, \ldots, T-1\}$. This induces the following prior distribution on the allocation vectors:

$$
P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)=\frac{1}{\binom{T-2}{2\left(\mathcal{K}_{g}-1\right)+1}} \prod_{k=0}^{\mathcal{K}_{g}-1}\left(b_{g, k+1}-b_{g, k}-1\right)
$$

The allocation vectors can be inferred via changepoint birth, death and re-allocation moves along the lines of the RJMCMC algorithm of Green (1995).

The changepoint reallocation move from $\mathbf{V}_{g}^{(i-1)}$ to $\mathbf{V}_{g}^{\star}$ randomly selects one changepoint $b_{g, j}$ from the changepoint set, $\left\{b_{g, 1}, \ldots, b_{g, \mathcal{K}_{g}^{(i-1)}-1}\right\}$, induced by $\mathbf{V}_{g}^{(i-1)}$. The replacement changepoint is randomly drawn from the set $\left\{b_{g, j-1}+2, \ldots, b_{g, j+1}-2\right\}$. This yields the new candidate allocation vector $\mathbf{V}_{g}^{\star}$, and $\mathcal{K}^{\star}=\mathcal{K}^{(i-1)}$.

The changepoint birth move from $\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]$ to $\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]$ randomly draws the location of one single new changepoint from the set of all valid new changepoint locations:

$$
B^{\dagger}:=\left\{b: 2 \leq b \leq T-1 \wedge \forall j \in\left\{1, \ldots, \mathcal{K}_{g}^{(i-1)}-1\right\}:\left|b-b_{g, j}\right|>1\right\}
$$

Adding the new changepoint to the changepoint set yields $\mathbf{V}_{g}^{\star}$, and $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}+1$.
The changepoint death move from $\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]$ to $\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]$ is complementary to the birth move. It randomly selects one of the changepoints induced by $\mathbf{V}_{g}^{(i-1)}$ and delets it. $\mathbf{V}_{g}^{\star}$ is the new candidate allocation vector after deletion, and $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}-1$.

The acceptance probabilities for these moves are given by $A=\min \{1, R\}$, with

$$
R=\frac{P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}}, \delta_{g}\right)} \cdot \frac{P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}_{g}^{\star}\right) P\left(\mathcal{K}_{g}^{\star}\right)}{P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathcal{K}_{g}^{(i-1)}\right)} \cdot Q
$$

where $Q$ is the Hastings ratio, which can be computed for each of the three changepoint move types (see, e.g., Green 1995). If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{\star}$, or otherwise set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

The CPS-DBN model can be inferred with the MCMC sampling scheme described in Table 3, but the moves on the allocation vectors have to be replaced by the changepoint birth, death and re-allocation moves, described in this subsection.

I also include the globally coupled variant of the CPS-DBN model, proposed in Grzegorczyk and Husmeier (2012b) and Grzegorczyk and Husmeier (2013), in my comparative evaluation study. The key idea is to hierarchically couple the segment-specific regression parameter vectors, $\mathbf{w}_{g, k}$, in Eq. (2) to allow for information-sharing with respect to the regression parameters. In the coupled CPS-DBN model Eq. (2) is replaced by $P\left(\mathbf{w}_{g, k} \mid \sigma_{g}^{2}, \delta_{g}\right)=\mathcal{N}\left(\mathbf{w}_{g, k} \mid \mathbf{m}_{g}, \delta_{g} \sigma_{g}^{2} \mathbf{I}\right)$, and the mean vector, $\mathbf{m}_{g}$, is now a flexible hyperparameter and has a multivariate standard Gaussian distribution, symbolically: $\mathbf{m}_{g, k} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$; see, e.g., Grzegorczyk and Husmeier (2013) for the mathematical details. However, as the coupled CPS-DBN model is not in the primary scope of the present paper, I focus on the standard CPS-DBN model and discuss the results of the coupled CPS-DBN model only casually.

# 2.7 Network-wide (shared) allocation vectors 

The non-homogeneous DBN models have been formulated with node-specific allocation vectors, $\mathbf{V}_{g}(g=1, \ldots, N)$. That is, the allocations vary from node to node, and have to be inferred independently for each node $g$. This gives very flexible DBN models. For applications where all nodes are a priori expected to share the same segmentation the nodespecific allocation vectors can be replaced by a network-wide allocation vector, which is then shared by all nodes, $\mathbf{V}_{g}=\mathbf{V}$ and $\mathcal{K}_{g}=\mathcal{K}$ for all $g$. For network-wide allocation vectors the moves from Sect. 2.5 have to be adapted. The probability terms $P\left(\mathcal{K}_{g}\right)$ and $P\left(\mathbf{V}_{g} \mid \mathcal{K}_{g}\right)$ have to be replaced by $P(\mathcal{K})$ and $P(\mathbf{V} \mid \mathcal{K})$, respectively. And each allocation vector change, $\mathbf{V}^{(i-1)} \rightarrow \mathbf{V}^{\star}$, applies to all nodes. The marginal likelihood terms (e.g. in the acceptance probabilities), $P\left(\mathbf{y}_{g, \mathbf{V}_{g}} \mid \mathbf{X}_{g, \mathbf{V}_{g}}, \delta_{g}\right)$, have to be replaced by product terms: $\prod_{g=1}^{N} P\left(\mathbf{y}_{g, \mathbf{V}} \mid \mathbf{X}_{g, \mathbf{V}}, \delta_{g}\right)$.

The usage of network-wide allocation vectors imposes a substantial restriction on the configuration space of the allocations. The underlying allocation vector can then be inferred more

accurately, as conceptual problems associated with model over-flexibility (data-overfitting) are alleviated.

# 2.8 Marginal edge posterior probabilities 

The MCMC sampling scheme for the HMM-DBN model is outlined in Table 3, and in Sects. 2.6.1-2.6.3 I provide details on how to modify this scheme for the competing models. I perform 2001 iterations in total, and to avoid autocorrelations in the MCMC trajectories I take samples in equidistant intervals (every 100th iteration). From the sample of length $2 I$ I withdraw the first $I$ samples to allow for a "burn-in phase", and I keep the remaining sample of length $I:\left\{\mathcal{M}^{(i)}, \mathbf{V}_{1}^{(i)}, \ldots, \mathbf{V}_{N}^{(i)}, \delta_{1}^{(i)}, \ldots, \delta_{N}^{(i)}\right\}_{i=I+1, \ldots, 2 I}$. From the networks, $\mathcal{M}^{(I+1)}, \ldots, \mathcal{M}^{(2 I)}$, I compute marginal edge posterior probabilities. The estimated marginal posterior probability of the edge from node $n$ to node $j(n, j \in\{1, \ldots, N\})$ is:

$$
e_{n, j}=\frac{1}{I} \sum_{i=I+1}^{2 \cdot I} \mathcal{M}^{(i)}(n, j)
$$

where $\mathcal{M}^{(i)}(n, j)$ is 1 if $\mathcal{M}^{(i)}$ contains the edge $n \rightarrow j$, and 0 otherwise.
I also estimate the marginal posterior probabilities, $C_{s, t}^{g}$, of two data points $s$ and $t(s, t \in$ $\{2, \ldots, T\})$ being assigned to the same state by the allocation $\mathbf{V}_{g}$ :

$$
\widehat{C}_{s, t}^{g}=\frac{1}{I} \cdot\left|\left\{i: i \in\{I+1, \ldots, 2 I\} \wedge \mathbf{V}_{g}^{(i)}(s)=\mathbf{V}_{g}^{(i)}(t)\right\}\right|
$$

I will refer to $\widehat{\mathbf{C}}^{g}=\left(\widehat{C}_{s, t}^{g}\right)_{s, t \in\{2, \ldots, T\}}$ as the estimated connectivity (co-allocation) matrix.

### 2.9 Criterions for quantifying the network reconstruction accuracy

If the true network, $\mathcal{M}^{\ddagger}$, is known, I evaluate the network reconstruction accuracy in terms of the areas under the precision recall curve. Let $\mathcal{M}^{\ddagger}(n, j)=1$ indicate that $\mathcal{M}^{\ddagger}$ possesses the edge from node $n$ to node $j$, while $\mathcal{M}^{\ddagger}(n, j)=0$ indicates that the edge $n \rightarrow j$ is not in $\mathcal{M}^{\ddagger}$. The models yield marginal edge posterior probabilities $e_{n, j} \in[0,1]$ for every possible edge $n \rightarrow j$. For $\zeta \in[0,1]$ I define $E(\zeta)$ as the set of all edges whose posterior probabilities exceed the threshold $\zeta$. For each $E(\zeta)$ the number of true positive $T P[\zeta]$, false positive $F P[\zeta]$, and false negative $F N[\zeta]$ edges can be counted, and the recall, $\mathcal{R}[\zeta]=T P[\zeta] /(T P[\zeta]+F N[\zeta])$, and the precision, $\mathcal{P}[\zeta]=T P[\zeta] /(T P[\zeta]+F P[\zeta])$, score can be computed. ${ }^{11}$ Plotting the $\mathcal{P}[\zeta]$ values (vertical axis) against the corresponding $\mathcal{R}[\zeta]$ values (horizontal axis) and connecting neighbouring points by a nonlinear interpolation (Davis and Goadrich 2006) gives the Precision-Recall (PR) curve. The area under the PR curve (AUC-PR) is a quantitative measure, and can be obtained by numerically integrating the PR curve; larger AUC-PR values indicate a better network reconstruction accuracy. Another measure for the network reconstruction accuracy is the area under the receiver operator characteristic curve (AUC-ROC). I employ AUC-ROC values only to confirm that all trends in terms of the AUC-PR measure can also be obtained with the AUC-ROC measure; for details on AUC-ROC scores see Davis and Goadrich (2006).

[^0]
[^0]:    11 The precision is the proportion of correctly predicted interactions out of the total number of predicted interactions. The recall is the proportion of true interactions that are correctly identified.

# 2.10 Potential scale reduction factors (PSRFs) for network edges 

The diagnostic that I apply to evaluate convergence, proposed in Grzegorczyk and Husmeier (2011), is based on the potential scale reduction factors (PSRFs); see Brooks and Gelman (1998) for details. I assume that $H$ independent MCMC simulations, with $200 I$ iterations each, have been performed on the same data set. I set $I=500$, and to monitor the PSRFs for the number of MCMC iterations I compute the marginal edge posterior probabilities for each simulation $h=1, \ldots, H$ after 200s iterations $(s=1,2, \ldots, I)$. Let $e_{n, j}^{[h, s]}$ denote the probability of the edge $n \rightarrow j$ obtained with MCMC simulation $h$ after 200 s iterations, where $s$ equidistant samples (every 100th iteration) are taken after the burn in phase of length 100s. For $s=1, \ldots, I$ I compute the "between-chain" and the "within-chain" variance:

$$
\begin{aligned}
\mathcal{B}_{s}(n, j) & =\frac{1}{H-1} \sum_{h=1}^{H}\left(e_{n, j}^{[h, s]}-\bar{e}_{n, j}^{[., s]}\right)^{2} \\
\mathcal{W}_{s}(n, j) & =\frac{1}{H(s-1)} \sum_{h=1}^{H} \sum_{i=1}^{s}\left(\mathcal{M}^{(i, h)}(n, j)-e_{n, j}^{[h, s]}\right)^{2}
\end{aligned}
$$

where $\bar{e}_{n, j}^{[., s]}$ is the mean of $e_{n, j}^{[1, s]}, \ldots, e_{n, j}^{[H, s]}$, and $\mathcal{M}^{(i, h)}(n, j)$ is 1 if the $i$ th network in the sample, taken from the $h$ th simulation, contains the edge $n \rightarrow j$, and 0 otherwise. Following Brooks and Gelman (1998) the $\operatorname{PSRF}_{s}(n, j)$ of the edge $n \rightarrow j$ is given by:

$$
\operatorname{PSRF}_{s}(n, j)=\frac{\left(1-\frac{1}{s}\right) \mathcal{W}_{s}(n, j)+\left(1+\frac{1}{H}\right) \mathcal{B}_{s}(n, j)}{\mathcal{W}_{s}(n, j)}
$$

where PSRF values near 1 indicate that the MCMC simulations are close to the stationary distribution. I use as a PSRF-based convergence diagnostic the fraction of edges $\mathcal{C}(\xi, s)$ whose PSRF is lower than a threshold $\xi$ (e.g. $\xi=1.1$ and $\xi=1.01$ ). The fractions $\mathcal{C}(\xi, s)$ can be monitored against the numbers of MCMC iterations 200s.

## 3 Data

### 3.1 Simulated data from the RAF pathway

For the RAF pathway, shown in Fig. 3, I generate synthetic network data. I employ a function $V$, which assigns a state $k \in\left\{1, \ldots, \mathcal{K}_{g}\right\}$ to each temporal data point $t=2, \ldots, T$. $V(t)=k$ means that data point $t$ is assigned to the $k$ th state. For each interaction between a node, $g$, and its parent nodes, which are defined by the RAF pathway, I require regression parameter vectors, which vary over time. Data points that are assigned to the same state $k$ share the same regression parameter vectors, while the regression parameters differ among states. Let $\mathbf{w}_{g, k}$ denote the regression parameter vector (including the intercept) for the interaction between node $g$ and its parent nodes for all time points that are assigned to state $k$. I distinguish two sampling scenarios for sampling random regression parameter vector instantiations. The first sampling strategy (scenario S1) has recently been employed in Grzegorczyk and Husmeier (2012b) and Grzegorczyk and Husmeier (2013) and guarantees that all regression parameter vectors, $\mathbf{w}_{g, k}$, share the same amplitude, $\left|\mathbf{w}_{g, k}\right|_{2}=1$. The second sampling strategy (scenario S2), which has for example been employed in Werhli et al. (2006), guarantees that the absolute value of each single element of the regression coefficient vector is in between 0.5 and 2 .

![img-2.jpeg](img-2.jpeg)

Fig. 3 The topology of the RAF pathway, as reported in Sachs et al. (2005). The RAF protein signalling transduction pathway consists of 11 proteins (pip3, plcg, pip2, pkc, p38, raf, pka, jnk, mek, erk, and act) and the edges represent protein interactions

Sampling scenario (S1) For each node $g \in\{1, \ldots, N\}$ and each state $k \in\{1, \ldots, \mathcal{K}\}$, I sample random vectors from standard multivariate Gaussian distributed vectors, $\mathbf{w}_{g, k}^{\top} \sim$ $\mathcal{N}(\mathbf{0}, \mathbf{I})$, and I normalize these random vectors to obtain regression parameter vectors, $\mathbf{w}_{g, k}$ of Euclidean norm (amplitude) one: $\mathbf{w}_{g, k}=\mathbf{w}_{g, k}^{\top} /\left|\mathbf{w}_{g, k}^{\top}\right|_{2}$.

Sampling scenario (S2) For each node $g \in\{1, \ldots, N\}$ and each state $k \in\{1, \ldots, \mathcal{K}\}$, I sample each element of the regression parameter vector, $\mathbf{w}_{g, k}$, independently from a continuous uniform distribution on the interval $[0.5,2]$, and for each element (regression coefficient) I afterwards draw a coin to determine its sign.

As strategy (S2) yields higher amplitudes, $\left|\mathbf{w}_{g, k}\right|_{2}$, on average, I employ this sampling scenario when I compare the DBN models with node specific allocation vectors. For the DBN models with shared allocation vectors, $\mathbf{V}_{g}=\mathbf{V}$ for all $g$, I follow strategy (S1). ${ }^{12}$

Given the sampled regression parameter vectors, $\mathbf{w}_{g, k}$, which either stem from S 1 or from S2, concrete data set instantiations, $\mathcal{D}$, can be generated. Let $\mathcal{D}_{g, t}$ denote the observation for node $g$ at time point $t$. For the first time point, $t=1$, I sample the realisations of the $N=11$ nodes from independent univariate Gaussian distributions, $\mathcal{D}_{g, 1} \sim \mathcal{N}(0,1)$ for all $g$. Afterwards, I generate realisations for $t=2, \ldots, T$ :

$$
\mathcal{D}_{g, t}=\left(1, \mathcal{D}_{\pi_{g}, t-1}^{\top}\right) \mathbf{w}_{g, V(t)}+\epsilon_{g, t}
$$

where $\mathcal{D}_{\pi_{g}, t-1}$ is the vector of the realisations of $g$ th parent nodes at the previous time point $t-1$, the function $V($.$) assigns each data point t to a state k \in\left\{1, \ldots, \mathcal{K}_{g}\right\}$, and the noise variables $\epsilon_{g, t}$ are independently standard Gaussian distributed, $\epsilon_{g, t} \sim N(0,1)$. The element 1 is included for the intercept.

For each data set instantiation, $\mathcal{D}$, I add additive white noise in a gene-wise manner to vary the signal-to-noise ratio (SNR). For each node, $g$, I compute the standard deviation, $s_{g}$, of its $T$ realisations, $\mathcal{D}_{g, 1}, \ldots, \mathcal{D}_{g, T}$, and I add i.i.d. Gaussian noise with zero mean and standard deviation $\mathrm{SNR}^{-1} \cdot s_{g}$ to each data point, where SNR is the pre-defined signal-to-noise ratio level. That is, I substitute $\mathcal{D}_{g, t}$ for $\mathcal{D}_{g, t}+v_{g, t}(t=1, \ldots, T)$, where $v_{g, 1}, \ldots, v_{g, T}$ are

[^0]
[^0]:    12 Note that I follow an unsupervised approach in my simulation study. That is, unlike related studies in Dondelinger et al. (2010), Husmeier et al. (2010), Dondelinger et al. (2012), Grzegorczyk and Husmeier (2012a), Grzegorczyk and Husmeier (2012b), and Grzegorczyk and Husmeier (2013) I here consider the allocation vectors to be unknown. Consequently, in particular the DBN models with node-specific allocation vectors can only be inferred properly when the amplitudes of the regression parameter vectors are sufficiently high. See Sect. 2.7 for details.

Table 5 Overview to the allocation scheme of the synthetic network data sets




Detailed explanations are given in Sect. 3.1
realisations of i.i.d. $\mathcal{N}\left(0,\left(S N R^{-1} \cdot s_{g}\right)^{2}\right)$ variables. I distinguish five signal-to-noise ratio levels: $\mathrm{SNR}=16, \mathrm{SNR}=8, \mathrm{SNR}=4, \mathrm{SNR}=2$, and $\mathrm{SNR}=1$.

The focus of my study is on different allocation schemes, i.e. different functions $V$ : $\{1, \ldots, T\} \rightarrow\{1, \ldots, \mathcal{K}\}$. I assume that each data set consists of an initial first data point followed by $H$ equidistant segments, $h=1, \ldots, H$, and that each segment $h$ comprises $T_{\star}=8$ coherent time points. For example, for $H=4$ the data set contains $T=1+H \cdot T_{\star}=33$ temporal data points, and the coherent time points in $\{2, \ldots, 9\},\{10, \ldots, 17\},\{18, \ldots, 25\}$, and $\{26, \ldots, 33\}$ correspond to the four segments $h=1, \ldots, 4$. The time points belonging to the same segment are always assigned to the same state $k$, while different segments can be assigned to different states. For notational convenience, I introduce boldface-symbols to indicate the true allocation scheme. Let $\mathbf{k}$ denote the row vector $(k, \ldots, k)$ of length $H_{\star}=8$ $(k=1, \ldots, \mathcal{K})$. For example, to indicate an allocation vector $\mathbf{V}_{g}$ that assigns the segments $h=1$ and $h=3$ to state $k=1$, and the segments $h=2$ and $h=4$ to state $k=2$, it can then be written compactly:

$$
\left[\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(33)\right]=\left[\underbrace{1, \ldots, 1}_{8 \times}, \underbrace{2, \ldots, 2}_{8 \times}, \underbrace{1, \ldots, 1}_{8 \times}, \underbrace{2, \ldots, 2}_{8 \times}\right]=: \mathbf{1 2 1 2}
$$

Furthermore, let the symbol "MIX" indicate an allocation scheme that does not consist of segments, but assigns each of the states $k \in\{1, \ldots, \mathcal{K}\}$ to $T_{\star}=(T-1) / \mathcal{K}$ randomly selected data points. For example, for $T=33$ and $\mathcal{K}=2$ I divide the time point set $\{2, \ldots, T\}$ randomly into two disjunct subsets, consisting of $T_{\star}=16$ data points each. Then I assign the state $k=1$ to the data points in the first subset, and the state $k=2$ to the data points in the second subset. An overview to the allocation schemes that I employ in my study is given in Table 5. For each of the nine allocation schemes I distinguish five SNR levels, and I generate 20 independent data instantiations for each combination of allocation scheme and SNR level; i.e. $9 \times 5 \times 20=900$ data sets in total.

# 3.2 Synthetic biology in Saccharomyces cerevisiae 

A popular benchmark gene expression data set for non-homogeneous DBN models has been provided by Cantone et al. (2009). The authors synthetically designed a small network in

Saccharomyces cerevisiae (yeast). This network, consisting of $N=5$ genes, is depicted in the right panel of Fig. 10. The authors measured expression levels of these genes in vivo with quantitative real-time Polymerase Chain Reaction at 37 time points over 8 h . During the experiment Cantone et al. (2009) changed the carbon source from galactose to glucose. ${ }^{13}$ As 16 measurements were taken in galactose and 21 measurements were taken in glucose, there are the following observations for each node $g: D_{g, 1}^{g a l}, \ldots, D_{g, 16}^{g a l}, D_{g, 1}^{g l u}, \ldots, D_{g, 21}^{g l u}$. The first measurements in galactose and glucose, $D_{g, 1}^{g a l}$ and $D_{g, 1}^{g l u}$, were taken during washing steps, in which the extant glucose (galactose) was removed and new galactose (glucose) was added. Consequently, these two measurements were biased by external circumstances and have to be removed from the time series. After removal of these two measurements, the remaining time series was (i) standardized via a log transformation, before (ii) a z-score transformation over all measured expressions, $\left\{D_{g, 2}^{g a l}, \ldots, D_{g, 16}^{g a l}, D_{g, 2}^{g l u}, \ldots, D_{g, 21}^{g l u}\right\}_{g=1, \ldots, 5}$, was performed to standardize the measured data to zero mean and a standard deviation of one. With respect to the data analysis it has to be taken into account that the measurement, $D_{g, 2}^{g l u}$ is not related to the last measurement, $D_{g, 16}^{g a l}$, in galactose, since the measurement in between (during the washing period), $D_{g, 1}^{g l u}$, had to be removed. That is, neither for $D_{g, 2}^{g a l}$ nor for $D_{g, 2}^{g l u}$ are there measurements of the preceding time point. Consequently, for each gene $g$ only the data points $D_{g, 3}^{g a l}, \ldots, D_{g, 16}^{g a l}, D_{g, 3}^{g l u}, \ldots, D_{g, 21}^{g l u}$ can be used as targets in the DBN models; the corresponding values of the regressor variables (parent nodes) are given by: $D_{\pi_{g}, 2}^{g a l}, \ldots, D_{\pi_{g}, 15}^{g a l}, D_{\pi_{g}, 2}^{g l u}, \ldots, D_{\pi_{g}, 20}^{g l u}$.

# 3.3 Circadian rhythms in Arabidopsis thaliana 

Plants assimilate carbon via photosynthesis during the day, but have a negative carbon balance at night. The plants can buffer these daily carbon budget alternations by diurnal gene regulatory processes. They store some of the assimilated carbon as starch during the day (in the presence of light), and use the stored starch as a carbon supply during the night (in the absence of light). In order to synchronize this diurnal process with the external 24-h photo period, plants have a circadian clock that can potentially provide predictive, temporal regulation of metabolic processes over the day:night (light:dark) cycle. The molecular mechanisms behind this circadian regulation have not been fully elucidated yet.

I use four individual (independent) gene expression time series from Arabidopsis thaliana to study the diurnal gene regulatory processes among nine genes involved in the circadian clock. ${ }^{14}$ In the four experiments E1-E4 the Arabidopsis plants were entrained in different dark:light cycles: $12 \mathrm{~h}: 12 \mathrm{~h}$ (E1 and E2), $10 \mathrm{~h}: 10 \mathrm{~h}$ (E3), and $14 \mathrm{~h}: 14 \mathrm{~h}$ (E4). In the experiments $T=12(\mathrm{E} 1)$ or $T=13(\mathrm{E} 2-\mathrm{E} 4)$ measurements were taken either in 4-h (E1 and E2) or in 2-h (E3 and E4) intervals. After the pre-experimental dark:light entrainment, the measurements were taken under experimentally generated constant light condition. RNA amounts were extracted with Affymetrix microarrays, and the data were background-corrected and RMAnormalized. The experimental protocols as well as more details on the time series can be found in Mockler et al. (2007) (E1), Edwards et al. (2006) (E2), and Grzegorczyk et al. (2008) (E3-E4).

[^0]
[^0]:    13 While the structure of the yeast network is identical for both carbon sources, the regulatory interaction strengths depend on the carbon source (Cantone et al. 2009).
    14 These genes are: LHY, TOC1, CCA1, ELF4, ELF3, GI, PRR9, PRR5, and PRR3.

For my data analysis I merge the four time series E1-E4 into one single data set by successively arranging them, symbolically: $E 1, \ldots, E 4$. The expression values at the first time points of the time series are not related to the expression values at the last time point of the preceding time series; e.g. the value of gene $g$ at the first time point in $\mathrm{E} 2, D_{g, 1}^{E 2}$, is not related to the values of the genes at the last time point of $\mathrm{E} 1,\left\{D_{g, 1}^{E 1} \mid g=1, \ldots, N\right\}$. Therefore, the first time points, $D_{g, 1}^{E 1}, D_{g, 1}^{E 2}, D_{g, 1}^{E 3}$, and $D_{g, 1}^{E 4}$, have to be removed from the merged time series. That is, those four observations cannot be used as targets, as there are no measurements for their potential parent nodes (at the preceding time points).

My objective differs from the earlier studies. Neither do I assume the three boundaries between the four individual time series to be known (as in Grzegorczyk and Husmeier (2013)) nor do I try to infer them (as in Grzegorczyk and Husmeier (2011)). My focus is on capturing the diurnal nature (i.e. the alternating dark:light cycles) of the gene regulatory processes in the circadian clock.

# 4 Simulation study 

### 4.1 The objectives of my empirical studies

First, I want to perform a comparative evaluation study to investigate under which circumstances the proposed HMM-DBN model achieves a higher network reconstruction accuracy than the competing DBN models. Second, I want to provide empirical evidence that the new MCMC moves, proposed in Sects. 2.5.1 and 2.5.2, improve convergence and mixing of the MCMC simulations. In Sect. 5.2 I employ data from the RAF pathway to systematically compare the network reconstruction accuracies of the DBN models, shown in Table 4, for various underlying segmentation schemes, shown in Table 5. The data are generated as explained in Sect. 3.1, and I distinguish five different SNR levels. I infer the DBN models with MCMC simulations and I compute marginal edge posterior probabilities to reverseengineer the RAF pathway. As the RAF pathway does not possess self-feedback loops, i.e. edges, such as $g \rightarrow g$, I impose the constraint $g \notin \pi_{g}(g=1, \ldots, N)$. Except for a first preliminary study in Sect. 5.1 I assume the segmentations to be unknown. That is, unlike related studies (see, e.g., Dondelinger et al. 2010; Husmeier et al. 2010; Dondelinger et al. 2012; Grzegorczyk and Husmeier 2012b, a, 2013), I here follow an unsupervised approach, in which the allocation vectors have to be inferred from the data. For the RAF pathway data I also compare the inferred segmentations with the true segmentations, and I show that the new MCMC moves substantially improve convergence and mixing. In Sect. 5.4 I employ the gene expression time series from Saccharomyces cerevisiae, described in Sect. 3.2, to extend my comparative evaluation by a real-world in vivo application from synthetic biology. Again I assume the segmentations to be unknown, and I exclude self-feedback loops, as the true network does not possess self-feedback loops. Although this application is quite small, the data have been measured in a true biological system, for which the true network is known. This study allows for an objective comparison of the performances of the DBN models on real biological data. In Sect. 5.5 I analyse the four gene expression time series from Arabidopsis thaliana, described in Sect. 3.3. For the Arabidopsis data a proper evaluation in terms of the network reconstruction accuracy is infeasible owing to the absence of a gold standard. My primary focus is thus on capturing the diurnal nature of the regulatory processes. Since the true Arabidopsis network is not known, I do not rule out self-feedback loops.

# 4.2 Hyperparameter settings 

The HMM-DBN model is presented as a graphical model in Fig. 2, and values for the fix hyperparameters have to be chosen. In consistency with earlier studies on Bayesian networks I restrict the maximal cardinality of the parent node sets to $\mathcal{F}=3 .{ }^{15}$ According to Eqs. (3-4) the inverse variance hyperparameters, $\sigma_{g}^{-2}(g=1, \ldots, N)$, and the inverse SNR hyperparameters, $\delta_{g}^{-1}(g=1, \ldots, N)$, are Gamma distributed with two hyperparameters each. I again follow earlier related studies, in which the Bayesian regression DBN model from Sect. 2.1 was used, and I set: $\sigma_{g}^{-2} \sim \operatorname{Gam}\left(A_{\sigma}=0.005, B_{\sigma}=0.005\right)$ and $\delta_{g}^{-1} \sim \operatorname{Gam}\left(A_{\delta}=2, B_{\delta}=0.2\right) .{ }^{16}$ Note that an extensive study in Grzegorczyk and Husmeier (2013) has shown that there is robustness with respect to different choices of these four hyperparameters. I also have to fix the hyperparameters of the Dirichlet priors for the MIX-DBN and the HMM-DBN model. In the absence of prior knowledge I follow Nobile and Fearnside (2007) and set $\alpha_{i}=1$ in Eq. (27) and $\alpha_{k, j}=1$ in Eq. (23). For the nonhomogeneous DBN models I set $\mathcal{K}_{\text {MAX }}=10$ and $\lambda=1$ in the truncated Poisson prior on the number of states (HMM) or components (MIX) or segments (CPS); see, e.g., Eq. (16).

### 4.3 MCMC simulation lengths and convergence diagnostics

I infer the DBN models with MCMC simulations, and for each simulation I perform 2001 (with $I=500$ ) iterations. I take samples in equidistant intervals (every 100th iteration). From the resulting sample of length 1000 I withdraw the first 500 samples ("burn-in phase"), and I use the remaining sample of length 500 to compute the marginal edge posterior probabilities (see Sect. 2.8). To assess convergence and mixing I apply trace plot (Giudici and Castelo 2003) and potential scale reduction factor (Gelman and Rubin 1992) diagnostics. With respect to the PSRF based criterion, described in Sect. 2.10, I found that the PSRF's of all edges were below 1.1 for the above mentioned simulation lengths. If the true network is known, I evaluate the network reconstruction accuracy in terms of the areas under the precision recall curve (AUC-PR), as described in Sect. 2.9.

## 5 Results

### 5.1 Pre-study: the supervised approach

I start with a pre-study, in which I cross-compare the network reconstruction accuracies of the proposed HMM-DBN model and the CPS-DBN model. I generate RAF pathway data for the segmentation $\left(\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right)=\mathbf{1 2 1 2}$ and I employ strategy (S1) from Sect. 3.1 to sample the regression parameters. Unlike in the later studies (i), I here fix the noise level $(\mathrm{SNR}=16)$ and vary the numbers of data points instead, and (ii) I assume the segmentation to be known and fixed ("supervised approach"). For the proposed HMM-DBN model I can impose the true underlying allocation vectors. The CPS-DBN model employs changepoints to divide the data into disjunct segments with different states. Consequently, the true segmentation, 1212, is not a member of the allocation vector configuration space of the CPS-DBN model and has to be approximated by 1234. I vary the number of data

[^0]
[^0]:    15 See, e.g., Friedman and Koller (2003) or Grzegorczyk and Husmeier (2011).
    16 See, e.g., Lèbre et al. (2010), Grzegorczyk and Husmeier (2012a), or Grzegorczyk and Husmeier (2012b).

![img-3.jpeg](img-3.jpeg)

Fig. 4 Supervised approach: network reconstruction accuracy for RAF pathway data with the segmentation scheme 1212. Data were generated with the regression parameter sampling strategy (S1), and the allocations were assumed to be known and fixed ("supervised approach"). For the proposed HMM-DBN model the true allocation vectors, $\left(\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right)=\mathbf{1 2 1 2}$, were imposed. For the CPS-DBN model the allocation vectors $\left(\mathbf{V}_{g}(2), \ldots, \mathbf{V}_{g}(T)\right)=\mathbf{1 2 3 4}$ were used, as this model cannot revisit states once left. The left panel monitors the performances in terms of average AUC-PR scores. The horizontal axis refers to the segment sizes $T_{\bullet}$; the total number of data points is equal to $T=1+4 \cdot T_{\bullet}$. The right panel monitors the average AUC-PR score difference between the HMM-DBN and the CPS-DBN model. The AUC-PR scores and score differences are averages over 20 data instantiations, with error bars indicating two-sided $95 \% t$-test confidence intervals
points per segment, $T_{\bullet} \in\{2,4,8,16,32,64\}$, and the total number of data points is given by: $T=1+H \cdot T_{\bullet}$, where $H=4$ is the number of temporal segments. The results are shown in Fig. 4 and reveal a clear trend. The network reconstruction accuracy of both models increases in the number of data points, $T_{\bullet}$, and the proposed HMM-DBN model performs consistently better than the CPS-DBN model for $T_{\bullet} \leq 32$. The difference in favour of the HMM-DBN model peaks at $T_{\bullet}=4$ and gets lower as $T_{\bullet}$ increases. Except for $T_{\bullet}=32$ $(T=129)$ and $T_{\bullet}=64(T=257)$, where both models yield an almost perfect network reconstruction accuracy (AUC-PR $\approx 1$ ), the performance improvement of the HMM-DBN model is significant; see the $t$-test confidence intervals in the right panel of Fig. 4.

# 5.2 Network reconstruction and allocation vector accuracy for various segmentation schemes 

In this subsection I cross-compare the performances of the four DBN models from Table 4. I generate RAF pathway data for various segmentations, as listed in Table 5, and I follow an unsupervised approach, i.e. I assume the segmentations to be unknown so that the allocation vectors have to be inferred from the data. I implement the models with nodespecific and network-wide allocation vectors, and I distinguish the strategies (S1) and (S2) from Sect. 3.1 for sampling random instantiations of the regression parameters. I keep the numbers of data points per segment fixed $\left(T_{\bullet}=8\right)$ and I vary the noise level ( $\mathrm{SNR} \in$ $\{16,8,4,2,1\})$. The network reconstruction accuracy results for the models with networkwide allocations vectors, $\mathbf{V}_{g}=\mathbf{V}$, are shown in Figs. 5 and 6. The results obtained with node-specific allocation vectors, $\mathbf{V}_{g}$, are shown in Fig. 7. The results can be summarised as follows.

![img-4.jpeg](img-4.jpeg)

Fig. 5 Network reconstruction accuracy for the synthetic RAF pathway data for different segmentation schemes. Data were generated with the regression parameter sampling strategy (S1) for different allocation schemes; see Sect. 3.1 and Table 5 for details. The DBN models were implemented with network-wide allocation vectors, $\mathbf{V}_{g}=\mathbf{V}$. The three columns refer to three different segmentation schemes, 1111, 1122, and 112233. The panels in the top row monitor the network reconstruction accuracy in terms of average AUC-PR scores for the HOM-DBN, the CPS-DBN, the MIX-DBN, and the proposed HMM-DBN model. The horizontal axis refers to five different SNR levels. The following rows monitor the average AUC-PR differences between the proposed HMM-DBN model and the other three DBN models, HMM versus HOM (2nd row), HMM versus CPS (3rd row), and HMM versus MIX (4th row). The AUC-PR scores and AUC-PR score differences are averages over 20 independent data instantiations, with error bars indicating two-sided $95 \% t$-test confidence intervals. Note that identical plots with AUC-ROC scores (not provided) show very similar trends

# 5.2.1 Network reconstruction accuracies 

(1) Homogeneous data: The segmentation $\mathbf{1 1 1 1}$ in Fig. 5 refers to homogeneous data. As the number of states is equal to one, $\mathcal{K}=1$, the regression parameter vectors, $\mathbf{w}_{g, 1}$ $(g=1, \ldots, N)$, do not vary over time. Fig. 5 shows that the models perform approximately equally well for this scenario. That is, the non-homogeneous models (CPS, MIX, and HMM) do not overfit the data by inferring spurious segmentations and are thus not inferior to the homogeneous DBN (HOM).
(2) Changepoint-segmented data: The segmentations $\mathbf{1 1 2 2}$ and $\mathbf{1 1 2 2 3 3}$ in Fig. 5 and the segmentation $\mathbf{1 1 2 2}$ in Fig. 7 refer to classical changepoint-segmented time series. There are 23 different states, $\mathcal{K}_{g}$, and states once left are not revisited. Consequently, these segmentations

![img-5.jpeg](img-5.jpeg)

Fig. 6 Network reconstruction accuracy for the synthetic RAF pathway data for different segmentation schemes. This figure is identical to Fig. 5 except that the three allocation schemes, 1212, 121212, and MIX are considered. Data were generated with the regression parameter sampling strategy (S1) and the DBN models were implemented with network-wide allocation vectors. See caption of Fig. 5 for further details
can be easily inferred with the CPS-DBN model, which imposes changepoints to divide the data into disjunct segments with different states. The HOM-DBN model, which cannot segment these non-homogeneous time series, performs substantially worse than the other three models. For the MIX-DBN model, which ignores the temporal ordering of the data points, these segmentations are more difficult to learn than for the CPS-DBN and the HMMDBN model. The latter models reach the highest network reconstruction accuracies and systematically outperform the MIX-DBN model. The CPS-DBN and the HMM-DBN model perform almost equally well with two exceptions: The CPS-DBN model outperforms the HMM-DBN model on segmentation $\mathbf{1 1 2 2 3 3}$ in the right column of Fig. 5 for the two lowest SNR values ( $\mathrm{SNR}=2$ and $\mathrm{SNR}=1$ ) and on segmentation $\mathbf{1 2 1 2}$ in the left column of Fig. 7 for the noise levels $\mathrm{SNR}=4$ and $\mathrm{SNR}=2$. For noisy data, the CPS-DBN model benefits from its restricted allocation vector configuration space, which here includes the true segmentations. ${ }^{17}$
(3) Mixture data: The segmentation scheme MIX in Fig. 6 refers to mixture model data. As explained in Sect. 3.1, the data points are randomly assigned to two states $(k \in\{1,2\})$ with

[^0]
[^0]:    17 This trend cannot be observed for the highest noise level in the left column of Fig. 7. It seems that $\mathrm{SNR}=1$ makes the data too noisy for the models with node-specific allocation vectors so that the CPS-DBN model performs as worse as the other three models, i.e. all models fail at equal measure.

![img-6.jpeg](img-6.jpeg)

Fig. 7 Network reconstruction accuracy for the synthetic RAF pathway data for different segmentation schemes. This figure is similar to Figs. 5 and 6. Unlike the earlier figures, data were generated with the regression parameter sampling strategy (S2) and the DBN models were implemented with node-specific allocation vectors, $\mathbf{V}_{\mathrm{g}}$. The three columns refer to three different segmentation schemes, 1122, 1212, and 121212. See caption of Fig. 5 for further details
different regression parameter vectors. For the allocation the temporal ordering of the data points is not taken into account. For this scenario the HOM-DBN model and the CPS-DBN model both yield the lowest network reconstruction accuracies. The HOM-DBN model fails, as it cannot deal with non-homogeneity at all; the CPS-DBN model fails, as the true (mixture) allocation scheme is not included in its restricted allocation vector configuration space. The MIX-DBN model and the HMM-DBN model both perform systematically superior to the HOM-DBN and the CPS-DBN model. Only for $\mathrm{SNR}=4$ and $\mathrm{SNR}=2$ the MIX-DBN model performs slightly superior to the HMM-DBN model. For noisy data the MIX-DBN model benefits from its completely free allocation vectors. Unlike the HMM-DBN model, the MIX-DBN model employs a free allocation model, which is here in agreement with the data generating mechanism; i.e. a random free allocation of the data points. Although the HMM-DBN model can infer free allocations, it does take the temporal ordering into account by putting less prior weight onto (random) allocations (without any temporal dependencies). For noisy data the prior on the allocation vectors becomes important, and so the HMM-DBN model is disadvantaged compared to the MIX-DBN model, whose allocation vector prior ignores the temporal ordering of the data points altogether.

![img-7.jpeg](img-7.jpeg)

Fig. 8 Graphical representation of the inferred temporal connectivity matrices for the RAF pathway data with $\mathrm{SNR}=16$. The figure is arranged as a matrix, and the columns correspond to four different allocation schemes. The top row shows the true connectivity structures, and the following rows correspond to the non-homogeneous DBN models. Data were generated with sampling strategy (S2) from Sect. 3.1. The models were implemented with network-wide allocation vectors, $\mathbf{V}_{g}=\mathbf{V}$. The heatmaps in rows $2-4$ indicate the estimated posterior probability of two data points being assigned to the same state. The probabilities are represented by a grey shading, where white corresponds to 1 , and black corresponds to 0 . The axes refer to the time points. In each heatmap the probabilities are averages over 20 data instantiations
(4) Periodic data: The segmentations $\mathbf{1 2 1 2}$ and $\mathbf{1 2 1 2 1 2}$ in Figs. 6 and 7 have a temporal structure but do not correspond to changepoint-segmented data, since the states are revisited. The dependency structure behind these segmentations is compatible with a Hidden Markov model and I will refer to them as "periodic data". As for the mixture data (MIX) the HOMDBN and the CPS-DBN model cannot deal with these periodic segmentations and perform consistently and significantly worse than the HMM-DBN model unless the data are very noisy $(\mathrm{SNR}=1)$. Only for the simulations with network-wide allocation vectors on segmentation $\mathbf{1 2 1 2}$ in Fig. 6 the difference between the HMM-DBN and the CPS-DBN model are moderate only. ${ }^{18}$ The MIX-DBN model also achieves consistently lower network reconstruction accuracies than the proposed HMM-DBN model, but the differences in favour of the HMM-DBN model are less pronounced. Form the left and middle column in Fig. 6 it appears that the MIX-DBN model is outperformed for the moderate noise levels, where the network reconstruction is neither perfect (AUC-PR $\ll 1$ ) nor impossible (AUC-PR $\gg 0.5$ ).

# 5.2.2 The estimated marginal connectivity matrices 

For the non-homogeneous DBN models I estimate the marginal connectivity matrices, as described in Sect. 2.8. Figure 8 shows heatmap representations of the average connectivity

[^0]
[^0]:    18 In the middle column of Fig. 6 the CPS-DBN model tends to infer three changepoints and to approximate the allocation scheme $\mathbf{1 2 1 2}$ by $\mathbf{1 2 3 4}$. As the allocation vectors are network-wide these changepoints apply to all nodes and thus have "enough support" from the data. A similar approximation for the segmentation 121212 fails, since 5 changepoints would be required to obtain 123456. For the simulations with node-specific allocation vectors in the middle column of Fig. 7 the approximation fails, as the three changepoints would have to be learnt for each node independently; i.e. without "sufficient support" from the data.

matrices for the segmentations $\mathbf{1 1 2 2}, \mathbf{1 1 2 2 3 3}, \mathbf{1 2 1 2}$, and $\mathbf{1 2 1 2 1 2}$ of the simulations with network-wide allocation vectors and $\mathrm{SNR}=16$. Figure 8 shows that the estimated connectivity matrices are consistent with my findings for the network reconstruction accuracy. The HMM-DBN model (bottom row in Fig. 8) infers the underlying segmentations (top row in Fig. 8) more accurately than the MIX-DBN model (2nd row in Fig. 8). That is, both models detect the underlying compartments, but the components are separated substantially stronger by the proposed HMM-DBN model. The CPS-model perfectly separates the segments only for those segmentations, $\mathbf{1 1 2 2}$ and $\mathbf{1 1 2 2 3 3}$, that are in agreement with its allocation vector configuration space. The segmentations $\mathbf{1 2 1 2}$ and $\mathbf{1 2 1 2 1 2}$ can only be approximated by $\mathbf{1 2 3 4}$ and $\mathbf{1 2 3 4 5 6}$, respectively, and the segments are then separated only weakly (last two panels in the 3rd row of Fig. 8).

# 5.2.3 Summary 

The results shown in Figs. 5, 6, 7 and 8 demonstrate that the proposed HMM-DBN model is more robust than the competing DBN models with respect to a variation of the underlying allocation. The HOM-DBN model cannot deal with non-homogeneous data at all. The CPSDBN model fails when the underlying segmentation cannot be approximated properly by changepoints. The MIX-DBN model fails when the underlying segmentation has a temporal structure, which cannot be taken into account. The proposed HMM-DBN model is always among the best-scoring models, and it significantly outperforms the competing models for periodic segmentations, such as $\mathbf{1 2 1 2}$ and $\mathbf{1 2 1 2 1 2}$.

Finally, note that I also applied the coupled variant of the CPS-DBN model from Grzegorczyk and Husmeier (2013); see Sect. 2.6.3 for a brief description of the coupling scheme. However, for the RAF-pathway data I have never observed a significant difference between the AUC-PR scores of the coupled CPS-DBN model and the AUC-PR scores of the standard CPS-DBN model. This finding is not surprising and consistent with the empirical results reported in Grzegorczyk and Husmeier (2013): As described in Sect. 3.1, I here sample independent state-specific regression parameters so that coupling the regression parameters is unlikely to yield any information gain. ${ }^{19}$

### 5.3 Convergence comparison for the HMM-DBN model

In this subsection I assess the degree of convergence and mixing of three different MCMC sampling schemes for the proposed HMM-DBN model. The MCMC sampling scheme for the HMM-DBN model is outlined in Table 3. I vary the 4th sampling step, i.e. the allocation vector inference part, to demonstrate that the adoption of the new moves, proposed in Sects. 2.5.1 and 2.5.2, improves convergence. The first MCMC sampling scheme, referred to as MIX and HMM moves, is the sampling scheme provided in Table 3. That is, a coin is drawn to decide randomly whether an allocation sampler (MIX) or a new (HMM) move is performed. Both move types are equally likely ( $p_{M I X}=0.5$ and $p_{H M M}=0.5$ ). I consider two alternative schemes; each employing only one particular move-type. The second scheme, referred to as MIX moves only, performs exclusively allocation sampler (MIX) moves (i.e. I set $p_{M I X}=1$ and $p_{H M M}=0$ ). The third scheme, referred to as HMM moves only, performs only the new HMM moves (i.e. I set $p_{H M M}=1$ and $p_{M I X}=0$ ). I use the convergence criterion from Sect. 2.10, and I monitor the fractions of edges with a PSRF lower than the target values

[^0]
[^0]:    ${ }^{19}$ Similar results have been reported in Fig. 5 in Grzegorczyk and Husmeier (2013), where the amplitude $\epsilon=1$ indicates that the segment-specific regression parameter vectors are (nearly) independent.

![img-8.jpeg](img-8.jpeg)

Fig. 9 Convergence diagnostics based on potential scale reduction factors (PSRFs) of individual network edges—RAF network with SNR = 16. I compare the performance of three MCMC sampling schemes for the proposed HMM–DBN model with node-specific allocation vectors. The MCMC sampling scheme was outlined in Table 3; here I vary the 4th sampling step, i.e. the allocation vector inference part: (i) MIX and HMM: Exactly as indicated in Table 3, randomly draw an unbiased coin to decide whether an allocation sampler (MIX) or a new move (HMM) is performed. Both move types are equally likely. (ii) MIX only: Perform the allocation sampler moves (MIX) with probability 1. (iii) HMM only: Perform the new HMM moves with probability 1. With the three sampling schemes I perform 5 independent MCMC simulations for one single data set instantiation. Afterwards, for each sampling scheme the 5 independent MCMC inference results were used to compute a PSRF for each edge, and the fractions of edges whose PSRF was lower than the thresholds ξ = 1.1 (left panel) and ξ = 1.01 (right panel) were computed. This procedure was repeated for five individual data set instantiations, and the panels show overlaid trace plots of the average fractions of edges whose PSRF was lower than the threshold ξ. The data sets were generated with sampling strategy (S2) for two segmentations, 1122 (top row) and 121212 (bottom row). Details on how I defined a PSRF for an edge are given in Sect. 2.10

$\xi=1.1$ and $\xi=1.01 .{ }^{20}$ The average results for the simulations with node-specific allocation vectors for the segmentation schemes $\mathbf{1 1 2 2}$ and $\mathbf{1 2 1 2 1 2}$ are shown in Fig. 9.

A clear outcome of the convergence diagnostic is that the MCMC sampling scheme MIX and HMM moves, which combines both types of moves, yields the best convergence: About $100 \%$ of the edges satisfy the standard convergence criterion (PSRF $<1.1$ ) already after 50k iterations. For the sampling scheme new HMM moves only scheme there is considerable scope for improvement. For the segmentation scheme $\mathbf{1 2 1 2 1 2}$ on average only about $90 \%$ of the edges satisfy the convergence criterion PSRF $<1.1$ after 50k iterations. The sampling scheme old MIX moves only fails to converge properly for the segmentation scheme 1122; only about $98 \%$ ( $92 \%$ ) percent of the edges satisfy the criterion PSRF $<1.1$ (PSRF $<1.01$ ) after 50k iterations. Note that the same average percentage rates are reached with the MIX and HMM moves already after 10k (20k) iterations. This suggests that the inclusion of the new MCMC moves, proposed in Sects. 2.5.1 and 2.5.2, is advantageous. The novel moves are as straightforward to implement as the allocation sampler moves, described in Appendix 2, and yield a convergence improvement.

# 5.4 Network reconstruction in Saccharomyces cerevisiae (yeast) 

In this subsection I cross-compare the network reconstruction accuracy of the DBN models on a small but topical data set from synthetic biology. The (true) yeast network, which was synthetically designed by Cantone et al. (2009), is depicted in the right panel of Fig. 10. Gene expression time series were measured in synthetically designed yeast cells, as described in Sect. 3.2. I apply each of the non-homogeneous DBN models (CPS, coupled CPS, HMM, and MIX) with node-specific, $\mathbf{V}_{g}$ and with network-wide, $\mathbf{V}_{g}=\mathbf{V}$, allocation vectors. Hence, I compare the performances of eight non-homogeneous DBN models and the conventional homogeneous DBN model. For each of the nine DBN models I run 5 independent MCMC simulations. The network reconstruction accuracy results (in terms of mean AUC-PR scores) are represented as histograms in Fig. 10. It can be seen that the non-homogeneous DBN models consistently achieve higher AUC-PR scores when they are implemented with nodespecific allocation vectors. Two-sided Student's $t$-tests show that the improvement achieved with node-specific allocation vectors is significant for the CPS-DBN model ( $p$ value 0.015 ), the coupled CPS-DBN model $(p=0.048)$ and the HMM-DBN model ( $p$ value 0.011 ). For both allocation vector variants (node-specific and network wide) the proposed HMMDBN reaches the highest average AUC-PR scores. In terms of the $p$ values of two-sided $t$-tests the differences in favour of the proposed HMM-DBN model are significant except for the comparison with the coupled CPS-DBN model. ${ }^{21}$ When implemented with nodespecific allocation vectors the coupled CPS-DBN model and the proposed HMM-DBN model perform approximately equally well $(p=0.517)$.

This finding is in agreement with earlier results on the RAF-pathway data in Sect. 5.2. Because of the carbon source switch from galactose to glucose the true segmentation of the yeast time series should be roughly of the form $\mathbf{1 1 2 2}$. For this segmentation it was found that the MIX-DBN model, which ignores the temporal order of the time points, performs substantially worse than the CPS-DBN and the HMM-DBN model; see, e.g., the middle

[^0]
[^0]:    ${ }^{20}$ The target value $\xi=1.1$ is usually taken as an indication of "sufficient" convergence. Lower target values, such as $\xi=1.01$, indicate a better degree of convergence.
    21 I obtained the following $t$-tests $p$ values: Network-wide allocation vectors: HMM versus HOM ( $p=$ 0.002 ), HMM versus CPS ( $p=0.048$ ), HMM versus coupled CPS ( $p=0.517$ ), and HMM versus MIX ( $p=$ 0.005 ); node-specific allocation vectors: HMM versus HOM ( $p=0.008$ ), HMM versus CPS ( $p=0.020$ ), HMM versus coupled CPS $(p=0.0733)$ and HMM versus MIX $(p=0.001)$.

![img-9.jpeg](img-9.jpeg)

Fig. 10 Network reconstruction accuracy in Saccharomyces cerevisiae (yeast). Cantone et al. (2009) synthetically designed the network and measured in vivo gene expression levels with real-time polymerase chain reaction. The histograms show the network reconstruction accuracies in terms of AUC-PR scores. The left (right) histogram refers to models with network-wide (node-specific) allocation vectors. Both histograms show bars of the average AUC-PR scores obtained with the HOM-DBN (white), the CPS-DBN (light grey), the coupled CPS-DBN (grey), the proposed HMM-DBN (black), and the MIX-DBN (dark grey) model. Average AUC-PR scores are computed from five independent MCMC simulations; the error bars indicate the standard deviations
column in Fig. 5 and the left column in Fig. 7. The improved network reconstruction accuracy of the coupled CPS-DBN model is in agreement with earlier reported results (see, e.g., Fig. 12 in Grzegorczyk and Husmeier 2013). The results in Fig. 10 suggest that the same improvement (i.e. the same "regularisation effect") can also be reached by a more flexible data segmentation scheme, namely the proposed HMM-DBN model. Finally, I also applied the coupling scheme from Grzegorczyk and Husmeier (2013) to the proposed HMM-DBN model; see Sect. 2.6.3 for a brief description of this coupling scheme. For the "coupled" HMM-DBN model I have not observed further improvements, but a slight (non-significant) decrease of the average AUC-PR scores.

# 5.5 Network reconstruction in Arabidopsis thaliana 

In this subsection I compare the performances of the non-homogeneous DBN models on a merged gene expression time series from Arabidopsis thaliana. One single long Arabidopsis time series has been obtained by successively arranging four individual short gene expression time series from different experiments, as explained in more detail in Sect. 3.3. In the four individual experiments (E1-E4) the gene expressions have been measured under constant light condition, but the plants were entrained in different experimentally controlled light-dark cycles. In the first two experiments E1 and E2 the plants were entrained in a $12 \mathrm{~h}: 12 \mathrm{~h}$ light/dark-cycle and measurements were taken in 4 h intervals, and in E3 and E4 measurements were taken in 2 h intervals and the plants were entrained in the light/dark-cycles $10 \mathrm{~h}: 10 \mathrm{~h}(\mathrm{E} 3)$ and $14 \mathrm{~h}: 14 \mathrm{~h}(\mathrm{E} 4)$.

From a biological perspective the regulatory relationships among the circadian genes in Arabidopsis follow a two-stage process, which is related to the diurnal nature of the environmental dark-light cycle. Two groups of genes can be distinguished: Morning genes whose activities peak in the presence of light (i.e. in the morning), and evening genes whose activities peak in the absence of light (i.e. in the evening). Although all gene expression

measurements in E1-E4 were taken under artificially generated constant light condition, the two-stage nature of the regulatory mechanisms will be preserved by the circadian clock (see, e.g., Johnson et al. 2003; McClung 2006). That is, even under constant light condition the regulatory processes (approximately) follow the diurnal dark:light cycle, in which the plants were entrained before the experiment. Since the dark:light cycle affects the activities of both the morning and the evening genes (i.e. the whole regulatory network) rather than specific genes only (Johnson et al. 2003; McClung 2006), I implement the non-homogeneous DBN models with network-wide allocation vectors, $\mathbf{V}_{g}=\mathbf{V}$; see Sect. 2.7 for details.

Heatmap representations of the inferred connectivity matrices are shown in Fig. 11a. All the non-homogeneous models (MIX-DBN, CPS-DBN, coupled CPS-DBN, and HMMDBN) infer a two-stage process with the number of states (components) peaking at $\mathcal{K}=2$. The CPS-DBN model and the coupled CPS-DBN model (see Sect. 2.6.3) both infer the same segmentation with one single changepoint between E2 and E3 (see left panel in Fig. 11a). As the CPS-DBN models can only infer changepoint-divided segmentations, where the segments are assigned to disjunct components (i.e. a state once left cannot be revisited), they do not capture the true underlying segmentation of the Arabidopsis time series. The changepoint of the CPS-DBN models appears to be related to different experimental conditions in E1-E2 and E3-E4 (here: e.g. the distance between measurements). The inferred segmentation does not reflect the diurnal nature of the regulatory process. For the merged Arabidopsis time series the preservations of the entrained dark:light cycles corresponds to a segmentation scheme of the form " $\mathbf{1 2 1 2 1 2} \ldots$ ". Hence, the failure of the CPS-DBN model is in agreement with results observed for the synthetic RAF-pathway data. In Sect. 5.2 I found for segmentations, such as $\mathbf{1 2 1 2}$ and $\mathbf{1 2 1 2 1 2}$, that the CPS-DBN model cannot infer the correct segmentation; see, e.g., the last two panels in the third row of Fig. 8.

From the middle and the right panel in Fig. 11a it can be seen that the inferred connectivity structures of the MIX-DBN model and the proposed HMM-DBN model are (also) very similar. I now have a closer look at the connectivity structures within the four individual time series. Figure 11b shows heatmap representations of the connectivity structures within E1-E4. ${ }^{22}$ The (sub-)heatmaps in Fig. 11b confirm the conjecture that the MIX-DBN and the HMM-DBN model infer very similar connectivities; i.e. the patterns in the top row are almost identical to the patterns in the bottom row. In particular, it can also be seen that the inferred segmentations are actually related to the dark:light cycles in which the Arabidopsis plants were entrained. In the heatmaps the "white windows around the diagonal" represent connected blocks, i.e. segments of data points that are assigned to the same state (component). The "white windows" in E3 (time points $26, \ldots, 30$ ) and in E4 (time points $38, \ldots, 44$ ) represent time intervals of length $(5 \times 2 \mathrm{~h}=) 10 \mathrm{~h}$ and $(7 \times 2 \mathrm{~h}=) 14 \mathrm{~h}$, and thus are in agreement with the entrainment cycles $10 \mathrm{~h}: 10 \mathrm{~h}$ (E3) and $14 \mathrm{~h}: 14 \mathrm{~h}$ (E4), respectively. In E1 and E2 there is at least a certain tendency towards segments ("white windows") consisting of 3 data points. In E1 and E2, where measurements were taken in 4 h intervals, three neighbouring data points cover a time interval of length $(3 \times 4 \mathrm{~h}=) 12 \mathrm{~h}$, what corresponds to the entrainment cycle $12 \mathrm{~h}: 12 \mathrm{~h}$ of E1-E2. This suggests that the MIX-DBN model and the HMM-DBN model infer the same connectivity structure, which is related to the diurnal nature of the dark:light cycle and thus in agreement with biology. ${ }^{23}$

[^0]
[^0]:    22 Technically, the corresponding areas of the heatmaps in Fig. 11a have simply been cut out.
    23 I also applied the HMM-DBN model with node-specific allocation vectors to the Arabidopsis data. The results (not shown) suggest that the expected segmentation(s) cannot be inferred properly with node-specific allocation vectors. For most of the genes only one single state $\left(\mathcal{K}_{g}=1\right)$ was inferred, while for other genes with $\mathcal{K}_{g}=2$ the inferred segmentation did not seem to be properly related to the pre-entrained dark:light cycles.

![img-10.jpeg](img-10.jpeg)

Fig. 11 Inference results on the Arabidopsis gene expression data. In the heatmaps in panels (a) and (b) the grey shading indicates the posterior probability of two data points being assigned to the same state, ranging from 0 (black) to 1 (white). a Heatmaps of the connectivity matrices inferred on the merged data set. The merged data set consists of four individual time series (E1-E4), which were arranged successively; see Sect. 3.3 for details. In the three panels the axes represent the indices of the data points, and the axes are ticked at the boundaries of the four individual time series. The CPS-DBN and the coupled CPS-DBN model both infer approximately the same segmentation (see left panel) with one single changepoint in between E2 and E3. b Sub-heatmaps extracted ("cut out") from the heatmaps in panel (a). The extracted sub-heatmaps show the connectivity structures within the four individual time series E1-E4. Note that the temporal distance between neighbouring data points is 4 h in E1 and E2, while measurements in E3 and E4 have been taken in 2 h intervals. c Scatter plots of the marginal edge posterior probabilities inferred on the merged data set. In each panel the marginal edge posterior probabilities of two DBN models have been plotted against each other

Figure 11c shows scatter plots of the marginal edge posterior probabilities inferred with the non-homogeneous DBN models. As the MIX-DBN and the HMM-DBN model have inferred the same connectivity structure, it is not surprising that their marginal edge posterior

![img-11.jpeg](img-11.jpeg)

Fig. 12 Reconstructed gene regulatory network in Arabidopsis thaliana. The merged Arabidopsis data set was analysed with the proposed HMM-DBN model to reverse-engineer the interactions among the nine circadian genes. The graph shows all edges with a marginal posterior probability greater than 0.5 ; except for three sel-feedback-loops $(L H Y \rightarrow L H Y, G I \rightarrow G I$ and $P R R 9 \rightarrow P R R 9)$ which have been left out. The morning (evening) genes are represented by white (grey) circles. Edges connecting either two morning genes or two evening genes with each other are represent by thin lines, while the bold edges refer to connections between the morning and the evening genes. Moreover, each individual edge is drawn either in black or in grey to distinguish whether it originates at the morning (black edge) or at the evening (grey edge) genes
probabilities are strongly correlated (see right panel of Fig. 11c). On the other hand, the CPS-DBN models, which could not capture the underlying dark:light cycle, yield deviating marginal edge posterior probabilities. That is, despite a certain correlation in the left and middle panel of Fig. 11c there are edges for which different marginal posterior probabilities have been inferred.

Finally, I use the inferred marginal edge posterior probabilities of the proposed HMMDBN model to predict the regulatory relationships in the circadian clock. Figure 12 shows the predicted network possessing only those edges whose marginal posterior probability exceeds the threshold of 0.5 . Unfortunately, there is no gold-standard network for the circadian clock in Arabidopsis so that the network reconstruction accuracy cannot be evaluated properly. However, the reconstructed network, shown in Fig. 12, possesses several edges that are consistent with the biological literature:

According to the biological literature (see, e.g., McClung 2006) the morning genes activate the evening genes, and the evening genes inhibit the morning genes. In the predicted network there are six edges pointing from the morning genes to the evening genes and five edges pointing from the evening genes to the morning genes. McClung (2006) also reports that CCA1 and LHY are the central regulators among the morning genes. ${ }^{24}$ From Fig. 12 it can be seen that four of the six edges pointing from the morning to the evening genes actually originate from LHY and CCA1 and that four of the five evening genes are regulated either by LHY or by CCA1. In particular, the regulation of the evening genes TOC1 and ELF4 by the central regulators CCA1/LHY has already been reported in Alabadi et al. (2001) and Kikis et al. (2005). Among the edges originating from the evening genes the two edges $E L F 3 \rightarrow C C A 1$ and $E L F 3 \rightarrow L H Y$ are consistent with the biological finding in Kikis et al. (2005) that ELF3 is necessary for light-induced CCA1 and LHY expression. Moreover, the edges $E L F 3 \rightarrow T O C 1$ and $G I \rightarrow T O C 1$ are also in agreement with the literature, as

[^0]
[^0]:    ${ }^{24}$ Note that according to Miwa et al. (2007) the central regulators CCA1 and LHY are partially redundant homologues.

Table 6 Average computational costs (and standard deviations), measured for the MCMC simulations on the synthetic RAF network data with $N=11$ nodes


In these scenarios all models were implemented with network-wide (shared) segmentations. The computational costs in this table are given in seconds per simulation with 10,000 MCMC iterations. More details on the simulation settings can be found in Table 5. All simulations were run using Matlab ${ }^{\circledR}$ on a Desktop PC with 3.20 GHz Intel Core processor and 8GB RAM

Table 7 Average computational costs (and standard deviations), measured for the MCMC simulations on the synthetic RAF network data with $N=11$ nodes


In these scenarios all models were implemented with node-specific segmentations. The computational costs in this table are given in seconds per simulation with 10,000 MCMC iterations. More details on the simulation settings can be found in Table 5. All simulations were run using Matlab ${ }^{\circledR}$ on a Desktop PC with 3.20 GHz Intel Core processor and 8GB RAM

Miwa et al. (2006) found that both genes ELF3 and GI are involved in the interaction between CCA1 and TOC1. Within the group of evening genes, the reconstructed network contains one single feedback loop $G I \leftrightarrow T O C 1$ between GI and TOC1. Exactly this feedback loop has also been found in Locke et al. (2005).

# 6 Discussions 

### 6.1 Computational costs of the MCMC inference

In this subsection I briefly discuss the computational costs of the required MCMC simulations. For the proposed HMM-DBN model I used the Matlab ${ }^{\circledR}$ software to implement the MCMC algorithm, as outlined in the pseudo code, provided in Tables 1, 2 and 3, and I ran all MCMC simulations on a standard Desktop PC. For the three competing DBN models I modified the algorithm, as outlined in Sect. 2.6. Tables 6 and 7 show the measured computational costs for the MCMC simulations on the synthetic RAF network data, which were analysed in Sect. 5.2. As expected, the three non-homogeneous DBN models are associated with substantially higher computational costs than the traditional homogeneous DBN model (HOM-DBN). It can also be seen that the computational costs for the HOM-DBN model stay almost constant across all nine data scenarios. The MCMC simulations for the non-homogeneous changepoint

DBN model (CPS-DBN) are consistently cheaper than the simulations for the two free allocation models, namely the MIX-DBN model and the proposed HMM-DBN model. This is due to the fact that the CPS-DBN model works on a restricted configuration space of the allocation vectors only; see Sect. 2.3 for details. The most interesting comparison is between the MIX-DBN model and the proposed HMM-DBN model, since both models allow for unrestricted free allocations and, hence, share the same (maximal) configuration space w.r.t. the allocation vectors. It can be seen the computational costs for the MCMC simulations are increased for the proposed MIX-DBN model. The difference is due to the fact that the new MCMC moves, proposed here, are slightly more expensive than the original allocation sampler moves. Although the difference appears to be irrelevant w.r.t. practical applications, it should be noted that the increase in the computational costs could be avoided by inferring the HMM-DBN model by allocation sampler moves only.

Since all MCMC simulations on a network with $N=11$ nodes could be finished within minutes on a standard Desktop PC, I would expect that the novel HMM-DBN model can also be applied to larger network domains (e.g. with $N=100$ nodes) in reasonable time. On the other hand, it certainly has to be taken into account that the number of possible parent sets grows at least polynomially in the number of network nodes $N .{ }^{25}$ In this context it is worth mentioning that the MCMC simulations for the HMM-DBN model with network-specific allocation vectors can be run in parallel (e.g. on a computer cluster). That is, as there is no information-sharing among genes, the HMM-DBN model can be applied independently to each gene $g$ to infer its particular parent set $\pi_{g}$ and its allocation vector $\mathbf{V}_{g}$. Given the increasing availability of high-performance computer clusters, I would thus argue that it is not the number of network nodes $N$ but the number of observations $T$ which restricts the applicability of the HMM-DBN model. E.g. in modern systems biology applications the number of measured observations $T$ is usually substantially smaller than the number of variables (e.g. genes) $N$, symbolically $T<<N$, leading to diffuse posterior distributions. Hence, even if an MCMC sampling scheme guaranteed that the huge space of possible network structures could be systematically searched for those networks with "high" posterior probabilities, a lack of significance would have to be expected. I would then recommend reducing the size of the network by restricting on the most important variables (e.g. genes). Often biological prior knowledge can be exploited to reduce the network to a reasonable size; e.g. for the Arabidopsis thaliana data (see Sect. 3.3) the focus was set on the nine potentially "most important" circadian clock genes.

# 6.2 Outlook and future work 

In this article I proposed a novel non-homogeneous DBN model, namely the HMM-DBN model, for which I assumed that the regulatory network structure, $\mathcal{G}$, is identical for all components (segments). Keeping the network structure constant allows for information-sharing among components (w.r.t. the network topology), and is certainly an appropriate assumption for the two presented real-world applications: (i) cellular response to fast environmental change in yeast (see Sect. 5.4) and (ii) the circadian clock network in Arabidopis thaliana (see Sect. 5.5). For certain other scenarios, e.g. morphogenesis, where the cellular processes take place on a longer time scale, the assumption of a fixed network structure might turn out to be too restrictive. For those applications it might be interesting to allow the network structure to vary with time and to implement the HMM-DBN model with component-specific

[^0]
[^0]:    25 Note that the number of possible parent sets grows polynomially in $N$ if a fan-in restriction $\mathcal{F}$ is imposed on the cardinality of the parent sets, while it grows super-exponentially in $N$ if there is no fan-in restriction.

network structures. This can, in principle, be accomplished straightforwardly, e.g. along the lines proposed and discussed in Lèbre et al. (2010) or Dondelinger et al. (2012).

An alternative extension of the proposed HMM-DBN model can be reached by incorporating the hierarchical global information-coupling scheme, proposed in Grzegorczyk and Husmeier (2013). The implementation of a coupled version of the HMM-DBN model is straightforward, and can be beneficial for applications where the component-specific network interaction parameters are similar to each other. For the yeast data (see Sect. 5.4) I incoporated the global information-coupling scheme into the changepoint-segmented DBN model (CPS-DBN) and the proposed HMM-DBN model, and I included these two new model variants into my cross-method comparison. In both cases the coupling did not yield substantially different results: For the coupled CPS-DBN model there was a slight (significant) improvement of the network reconstruction accuracy (see Fig. 10), and for the coupled HMM-DBN model I saw a slight (non-significant) decrease in the network reconstruction accuracy (see main text in Sect. 5.4). From a more general perspective, I would expect that the improvement through information-coupling, will be less pronounced for the HMM-DBN model than for the CPS-DBN model. With the CPS-DBN model, states once left cannot be revisited so that information-coupling is required for sharing information between distant time points. Unlike the CPS-DBN model, the proposed HMM-DBN model explicitly allows distant time points to be allocated to the same component and to share the same network interaction parameters.

# 7 Conclusion 

I have proposed a novel non-homogeneous dynamic Bayesian network (DBN) model, which combines a conventional DBN with a Hidden Markov model (HMM). The key idea behind this HMM-DBN model is to assume that the temporal data points of a time series are allocated to different states (components) by a HMM. A graphical representation of the HMM-DBN model is provided in Table 2. My work complements earlier works which combined DBN models either with multiple changepoint processes (CPS-DBN) or with free allocation mixture (MIX-DBN) models; see Sect. 1 for various literature references. The CPS-DBN models, on the one hand, employ a multiple changepoint process to divide a time series into temporal segments with a one-to-one mapping between segments and states (components): All data points within a segment are assigned to the same state, but data points from different segments have to be allocated to different states; i.e. "a state (component) once left cannot be revisited". This imposes a very strong restriction onto the configuration space of the possible data segmentations. The MIX-DBN model, on the other hand, allows for an unrestricted free allocation of the data points to states (mixture components) but loses important information about the data, since it cannot take the temporal ordering of the data points into account.

The novel HMM-DBN model is a consensus between the CPS-DBN and the MIX-DBN model, as it does take the temporal structure of the data into account without putting any restriction onto the configuration space of the data segmentations. The novel HMM-DBN model can be inferred with two different Reversible Jump Markov Chain Monte Carlo (RJMCMC) techniques, as briefly discussed in Sect. 2.5. In this paper I have shown how the allocation sampler from Nobile and Fearnside (2007) can be used for inference, and in Sects. 2.5.1-2.5.2 I have proposed two new pairs of complementary moves to improve mixing and convergence of the allocation sampler. Pseudo code of the proposed MCMC sampling scheme is provided in Table 3.

In Sect. 5.2 I have performed an extensive comparative evaluation study on synthetic RAF-pathway data to provide empirical evidence that the proposed HMM-DBN model is a consensus between the MIX-DBN and the CPS-DBN model. A brief overview to the four competing DBN models, which I cross-compared in my evaluation study, is given in Table 5. In my study I considered various segmentation scenarios, as listed in Table 4. For scenarios where the CPS-DBN model performed significantly better than the MIX-DBN model and vice-versa I found that the performance of the proposed HMM-DBN model was always very close (and only rarely significantly different) to the performance of the better-scoring DBN model. For scenarios with periodic segmentations the proposed HMM-DBN model outperformed the competing MIX-DBN model and the CPS-DBN models.

I have also cross-compared the learning performances of the four DBN models on two real-world applications from systems biology (see Sects. 5.4 and 5.5). My cross-method comparison for the real-world data also confirmed that the proposed HMM-DBN model is a consensus between the CPS-DBN and the MIX-DBN model. For a non-homogeneous yeast gene expression time series, which consists of two ("changepoint-divided") temporal segments related to two different carbon sources, the free allocation MIX-DBN model has failed to reconstruct the underlying network, while the coupled CPS-DBN (Grzegorczyk and Husmeier 2013) and the proposed HMM-DBN model have performed substantially better; see Sect. 5.4 for details.

For a non-homogeneous Arabidopsis gene expression time series, in which the regulatory processes are diurnal and periodic, i.e. the processes follow recurrent entrained dark:light cycles, the CPS-DBN models have failed to capture the underlying data segmentation, while the MIX-DBN and the proposed HMM-DBN model both inferred a segmentation, which is in agreement with plant biology; see Sects. 3.3 and 5.5 for details. I have used the results of the HMM-DBN model to reconstruct the network among the circadian genes in Arabidopsis. As discussed in Sect. 5.5, the reconstructed network shows features that are consistent with the biological literature.

Acknowledgments I did this work while I was supported by the German Research Foundation (DFG), research grant GR3853/1-1. I thank Dirk Husmeier for useful discussions on the methodology as well as for proofreading this manuscript.

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

# Appendix 1: Sweep Gibbs move on the allocation vector 

The Gibbs move keeps the network $\mathcal{M}=\left(\pi_{1}, \ldots, \pi_{N}\right)$ and the SNR hyperparameters fixed, and I describe the $i$ th MCMC iteration, $(i-1) \rightarrow i$, for node $g$. The move reallocates one single data point to a new state. If the number of states is currently equal to one, $\mathcal{K}_{g}^{(i-1)}=1$, skip the move. Otherwise randomly select one single observation $t \in\{2, \ldots, T\}$. For $k=1, \ldots, \mathcal{K}_{g}^{(i-1)}$ replace the $t$ th element of the current allocation vector $\mathbf{V}_{g}^{(i-1)}$ by state $k$ to obtain the vector $\mathbf{V}_{g,\left[t_{k}\right]}$. Sample the new allocation vector $\mathbf{V}_{g}^{(i)}$ from the full conditional distribution. For $k=1, \ldots, \mathcal{K}_{g}^{(i-1)}$ :

$$
P\left(\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g,\left[t_{k}\right]}\right)=\frac{P\left(\mathbf{V}_{g,\left[t_{k}\right]} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g,\left[t_{k}\right]}} \mid \mathbf{X}_{g, \mathbf{V}_{g,\left[t_{k}\right]}}, \delta_{g}\right)}{\sum_{u=1}^{\mathcal{K}_{g}^{(i-1)}} P\left(\mathbf{V}_{g,\left[t_{u}\right]} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g,\left[t_{u}\right]}} \mid \mathbf{X}_{g, \mathbf{V}_{g,\left[t_{u}\right]}, \delta_{g}}\right)}
$$

As this move does not change the number of states, it has to be set: $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

# Appendix 2: The mixture model allocation sampler (MIX) moves 

The MIX MCMC moves, presented in this appendix, have been developed by Nobile and Fearnside (2007) for Gaussian mixture models. Nobile and Fearnside (2007) proposed the resulting "allocation sampler" as an alternative to computationally expensive Reversible Jump Markov Chain Monte Carlo sampling schemes (Green 1995); see Nobile and Fearnside (2007) for details.

## The M1 move

If the number of states is currently equal to one, $\mathcal{K}_{g}^{(i-1)}=1$, skip the move. Otherwise randomly select two states $k$ and $\tilde{k}$ among the $\mathcal{K}_{g}^{(i-1)}$ available, and draw a random number $\tilde{p}$ from a Beta(a,a) distribution with $a=1$. Consider the set $H=\left\{t: \mathbf{V}_{g}^{(i-1)}(t)=k \vee\right.$ $\left.\mathbf{V}_{g}^{(i-1)}(t)=\tilde{k}\right\}$ of all data points that are allocated either to state $k$ or to state $\tilde{k}$ by $\mathbf{V}_{g}^{(i-1)}$. Reallocate each point of the set $H$ either to component $k$ (with probability $\tilde{p}$ ) or to component $\tilde{k}$ (with probability, $1-\tilde{p}$ ). This gives a new allocation vector, $\mathbf{V}_{g}^{\star}$, which is accepted with probability:

$$
A=\min \left\{1, \frac{P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}, \delta_{g}}\right)} \cdot \frac{Q\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)}{Q\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)}\right\}
$$

The prior probabilities and the marginal likelihood terms can be computed with Eqs. (12), (23) and (16). Nobile and Fearnside (2007) show that the Hastings ratio is given by:

$$
\frac{Q\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)}{Q\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)}=\frac{\Gamma\left(a+n_{k}\right) \Gamma\left(a+n_{\tilde{k}}\right)}{\Gamma\left(a+n_{k}^{\star}\right) \Gamma\left(a+n_{\tilde{k}}^{\star}\right)}
$$

where $n_{k}$ and $n_{\tilde{k}}$ are the numbers of data points that are allocated to the states $k$ and $\tilde{k}$ by $\mathbf{V}_{g}^{(i-1)}$, and $n_{k}^{\star}$ and $n_{\tilde{k}}^{\star}$ are the numbers of data points that are allocated to the states $k$ and $\tilde{k}$ by $\mathbf{V}_{g}^{\star}$. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$, or otherwise set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$. As the move cannot change the number of states, set: $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

## The M2 move

If the number of states is currently equal to one, $\mathcal{K}_{g}^{(i-1)}=1$, skip the move. Otherwise randomly select two states $k$ and $\tilde{k}$ among the $\mathcal{K}_{g}^{(i-1)}$ available.

If the $k$ th component is empty, the move fails outright. Otherwise draw a random number $u$ from a uniform distribution on $\left\{1, \ldots, n_{k}\right\}$, where $n_{k}$ is the number of data points $t$ with $\mathbf{V}_{g}^{(i-1)}(t)=k$. Randomly select $u$ observations from the $n_{k}$ data points and re-allocate them

to state $\bar{k}$ to obtain the new candidate allocation vector $\mathbf{V}_{g}^{\star}$. The new allocation vector is accepted with the probability given in Eq. (37), except that the Hastings Ratio is different. As shown in Nobile and Fearnside (2007), the Hastings ratio is:

$$
\frac{Q\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)}{Q\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)}=\frac{n_{k}}{n_{\bar{k}}+u} \cdot \frac{n_{k}!\cdot n_{\bar{k}}!}{\left(n_{k}-u\right)!\cdot\left(n_{\bar{k}}+u\right)!}
$$

where $n_{k}$ and $n_{\bar{k}}$ are the numbers of data points allocated to the states $k$ and $\bar{k}$ by $\mathbf{V}_{g}^{(i-1)}$. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$, or otherwise set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$. As the M2 move cannot change the number of states, set: $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

# The EA (ejection/absorption) moves 

If $\mathcal{K}_{g}^{(i-1)}=1$, then an ejection move has to be performed. If $\mathcal{K}_{g}^{(i-1)}=\mathcal{K}_{M A X}$, then an absorption move has to be performed. For $\mathcal{K}_{g}^{(i-1)} \in\left\{2, \ldots, \mathcal{K}_{M A X}-1\right\}$ the move type (ejection or absorption) is randomly drawn.

## The ejection move

Randomly select a state $k \in\left\{1, \ldots, \mathcal{K}_{g}^{(i-1)}\right\}$. Make a draw $p_{E}$ from a $\operatorname{Beta}(a, a)$ distribution and re-allocate each data point allocated to component $k$ by $\mathbf{V}_{g}^{(i-1)}$ with probability $p_{E}$ to a new state with label $\mathcal{K}_{g}^{(i-1)}+1$ to obtain the new candidate allocation vector $\mathbf{V}_{g}^{\star}$. The new number of states, associated with $\mathbf{V}_{g}^{\star}$, is $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}+1$. The acceptance probability is $A=\min \{1, R\}$ where

$$
R=\frac{P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}_{g}^{\star}\right) P\left(\mathcal{K}_{g}^{\star}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}}, \delta_{g}\right)} \cdot Q
$$

and Nobile and Fearnside (2007) show that the Hastings ratio is given by:

$$
Q=\frac{Q\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right)}{Q\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right] \mid\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)}=p_{E} \cdot \frac{\Gamma(a)^{2}}{\Gamma(2 a)} \cdot \frac{\Gamma\left(2 a+n_{k}\right)}{\Gamma\left(a+n_{\bar{k}}^{*}\right) \Gamma\left(a+n_{\bar{k}}^{*}\right)}
$$

where $n_{k}$ is the number of observations allocated to the $k$ th state by $\mathbf{V}_{g}^{(i-1)}, n_{\bar{k}}^{*}$ and $n_{\bar{k}}^{*}$ are the numbers of data points allocated to the states $\bar{k}$ and $k$ by $\mathbf{V}_{g}^{\star}$. The factor $p_{E}$ is equal to one for $\mathcal{K}_{g}^{(i-1)} \in\left\{2, \ldots, \mathcal{K}_{M A X}-2\right\}$; while $p_{E}=0.5$ for $\mathcal{K}_{g}^{(i-1)}=1$, and $p_{E}=2$ for $\mathcal{K}_{g}^{(i-1)}=\mathcal{K}_{M A X}-1$. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}+1$, or otherwise set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$. As suggested by Nobile and Fearnside (2007), I select the parameter $a$ of the Beta(a,a) by numerically solving the equation:

$$
\frac{\Gamma(2 a)}{\Gamma(a)} \cdot \frac{\Gamma\left(a+n_{k}\right)}{\Gamma\left(2 a+n_{k}\right)}=0.1
$$

where $n_{k}$ is the number of data points allocated to state $k$ by $\mathbf{V}_{g}^{(i-1)}$, and I use a lookup table in my implementation. See Nobile and Fearnside (2007) for further details.

# The absorption move 

Randomly select two states $k, \tilde{k} \in\left\{1, \ldots, \mathcal{K}_{g}^{(i-1)}\right\}$ with $\tilde{k} \neq k$. Re-allocate all data points allocated to state $\tilde{k}$ by the current allocation vector, $\mathbf{V}_{g}^{(i-1)}$, to state $k$ to obtain the new allocation vector $\mathbf{V}_{g}^{\star}$. Then $\mathbf{V}_{g}^{\star}$ does not allocate data points to state $\tilde{k}$. If the (unemployed) state, $\tilde{k}$, is not equal to the maximal state, $\mathcal{K}_{g}^{(i-1)}$, swap the labels of the states $\tilde{k}$ and $\mathcal{K}_{g}^{(i-1)}$; i.e. set $\mathbf{V}_{g}^{\star}(t)=\tilde{k}$ for all $t$ with $\mathbf{V}_{g}^{(i-1)}(t)=\mathcal{K}_{g}^{(i-1)}$. Afterwards delete the (unemployed) maximal state $\mathcal{K}_{g}^{(i-1)}$, and set $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}-1$. The acceptance probability is $A=\min \{1, R\}$, where $R$ was specified in Eq. (40), and the Hastings ratio is now given by:

$$
Q_{A}=\frac{Q\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right)}{Q\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right] \mid\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)}=p_{A} \cdot \frac{\Gamma(2 a)}{\Gamma(a)^{2}} \cdot \frac{\Gamma\left(a+n_{\tilde{k}}\right) \Gamma\left(a+n_{k}\right)}{\Gamma\left(2 a+n_{k}^{*}\right)}
$$

where $n_{k}^{*}$ is the number of data points allocated to state $k$ by the new candidate vector, $\mathbf{V}_{g}^{\star}, n_{k}$ and $n_{\tilde{k}}$ are the numbers of data points allocated to the states $k$ and $\tilde{k}$ by $\mathbf{V}_{g}^{(i-1)}$, $a$ is the parameter of the Beta(a,a) distribution in the ejection move, and $p_{A}=0.5$ for $\mathcal{K}_{g}^{(i-1)}=\mathcal{K}_{\text {MAX }}, p_{A}=2$ for $\mathcal{K}_{g}^{(i-1)}=2$, while $p_{A}=1$ otherwise. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}-1$, or otherwise set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

## Appendix 3: The novel inclusion and the novel exclusion move for the proposed HMM-DBN model

The novel inclusion move and the novel exclusion move both keep the network $\mathcal{M}=$ $\left(\pi_{1}, \ldots, \pi_{N}\right)$ and the SNR hyperparameters fixed. I describe the $i$ th MCMC iteration, $(i-1) \rightarrow i$, of this pair of moves for node $g$. If the current number of states is equal to one, $\mathcal{K}_{g}^{(i-1)}=1$, skip the move. Otherwise, draw an unbiased coin to decide, whether an inclusion or an exclusion move is performed. Given the current allocation vector, $\mathbf{V}_{g}^{(i-1)}$, both moves propose a new candidate allocation vector $\mathbf{V}_{g}^{\star}$. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$, or otherwise leave the allocation vector unchanged, $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$. Since neither the inclusion nor the exclusion move changes the number of states, set $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

## The exclusion move

Randomly select one time point $t_{0} \in\{2, \ldots, T\}$, and consider the state $k:=\mathbf{V}_{g}^{(i-1)}\left(t_{0}\right)$ to which the selected time point is currently allocated to. Determine the highest time point $s_{E} \in\left\{2, \ldots, t_{0}-1\right\}$ that is not allocated to state $k$ :

$$
s_{E}=\max \left\{\tilde{t} \in\left\{2, \ldots, t_{0}-1\right\}: \mathbf{V}_{g}^{(i-1)}(\tilde{t}) \neq k\right\}
$$

If $s_{E}$ is not well-defined, set $s_{E}=1$ instead. Afterwards, determine the lowest time point $t_{E} \in\left\{t_{0}+1, \ldots, T\right\}$ that is not allocated to state $k$ :

$$
t_{E}=\min \left\{\tilde{t} \in\left\{t_{0}+1, \ldots, T\right\}: \mathbf{V}_{g}^{(i-1)}(\tilde{t}) \neq k\right\}
$$

If $t_{E}$ is not well-defined, set $t_{E}=T+1$ instead.

Consider the sequence $s_{E}+1, \ldots, t_{E}-1$. It follows from Eqs. (42-43) that all data points in the sequence are currently allocated to state $k$. The length of this sequence is $L_{E}=t_{E}-s_{E}-1$. If $L_{E}<3$, skip the move. Otherwise, draw a random number $u_{1}$ from the set $\left\{1, \ldots, L_{E}-2\right\}$, and subsequently a random number $u_{2}$ from the set $\left\{0, \ldots, L_{E}-2-u_{1}\right\} . u_{1}$ can be interpreted as the "subsequence length" and $u_{2}$ can be interpreted as the "lag", since the exclusion move proposes to re-allocate the data points $s_{E}+u_{2}+2, \ldots, s_{E}+u_{2}+1+u_{1}$ to a new state $\tilde{k}$, where $\tilde{k} \neq k$ is randomly drawn from all $\mathcal{K}_{g}^{(i-1)}-1$ states unequal to $k$. For the new candidate allocation vector, $\mathbf{V}_{g}^{\star}$, this yields: $\mathbf{V}_{g}^{\star}(t)=\tilde{k}$ if $t \in\left\{s_{E}+u_{2}+2, \ldots, s_{E}+u_{2}+1+u_{1}\right\}$, and $\mathbf{V}_{g}^{\star}(t)=\mathbf{V}_{g}^{(i-1)}(t)$ for $t \notin\left\{s_{E}+u_{2}+2, \ldots, s_{E}+u_{2}+1+u_{1}\right\}$. The Hastings is given by:

$$
Q_{E}\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)=\frac{L_{E}}{T-1} \cdot \frac{1}{L_{E}-2} \cdot \frac{1}{L_{E}-1-u_{1}} \cdot \frac{1}{\mathcal{K}_{g}^{(i-1)}-1}
$$

The first factor is the probability of selecting one point of the sequence $s_{E}+1, \ldots, t_{E}-1$ of length $L_{E}$, the second and the third factor are the probabilities for selecting $u_{1}$ and $u_{2}$, respectively, and the last factor is the probability for selecting $\tilde{k} \neq k$.

# The inclusion move 

Randomly select one time point $t_{0} \in\{2, \ldots, T\}$, and consider the state $k:=\mathbf{V}_{g}^{(i-1)}\left(t_{0}\right)$ to which the selected time point is currently allocated to. Determine the highest time point $s_{I} \in\left\{2, \ldots, t_{0}-1\right\}$ that is not allocated to state $k$ :

$$
s_{I}=\max \left\{\tilde{t} \in\left\{2, \ldots, t_{0}-1\right\}: \mathbf{V}_{g}^{(i-1)}(\tilde{t}) \neq k\right\}
$$

If $s_{I}$ is not well-defined, skip the move. Otherwise, determine the lowest time point $t_{I} \in$ $\left\{t_{0}+1, \ldots, T\right\}$ that is not allocated to state $k$ :

$$
t_{I}=\min \left\{\tilde{t} \in\left\{t_{0}+1, \ldots, T\right\}: \mathbf{V}_{g}^{(i-1)}(\tilde{t}) \neq k\right\}
$$

If $t_{I}$ is not well-defined, skip the inclusion move.
Only if $s_{I}$ and $t_{I}$ are both well-defined, test whether $\mathbf{V}_{g}^{(i-1)}\left(s_{I}\right)$ is equal to $\mathbf{V}_{g}^{(i-1)}\left(t_{I}\right)$. If this "equal boundaries" test fails, skip the inclusion move. If the test is successful it holds: $\mathbf{V}_{g}^{(i-1)}(t)=k$ for $t \in\left\{s_{I}+1, \ldots, t_{I}-1\right\}$ and $\mathbf{V}_{g}^{(i-1)}\left(s_{I}\right)=\mathbf{V}_{g}^{(i-1)}\left(t_{I}\right)=: \tilde{k}$ where $\tilde{k} \neq k$. The inclusion move proposes to re-allocate all time points $t \in\left\{s_{I}+1, \ldots, t_{I}-1\right\}$ to state $\tilde{k}$, i.e. to the state of the surrounding time points $s_{I}$ and $t_{I}$. This yields for the new candidate allocation vector, $\mathbf{V}_{g}^{\star}$ : For $t=2, \ldots, T \operatorname{set} \mathbf{V}_{g}^{\star}(t)=\tilde{k}$ if $t \in\left\{s_{I}+1, \ldots, t_{I}-1\right\}$, or otherwise set $\mathbf{V}_{g}^{\star}(t)=\mathbf{V}_{g}^{(i-1)}(t)$. The proposal probability

$$
Q_{I}\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)=\frac{L_{I}}{T-1}
$$

is the probability of selecting one point $t_{0}$ of the sequence $s_{I}+1, \ldots, t_{I}-1$ of length $L_{I}=t_{I}-s_{I}-1$.

## Complementary inclusion move for the exclusion move

Consider the exclusion move from $\mathbf{V}_{g}^{(i-1)}$ to $\mathbf{V}_{g}^{\star}$, described above. The data points in the sequence $s_{E}+u_{2}+2, \ldots, s_{E}+u_{2}+1+u_{1}$, which were originally allocated to state $k$, have been re-allocated to state $\tilde{k}$. The design of the exclusion move ensures that the new candidate

vector, $\mathbf{V}_{g}^{\star}$, still allocates the two surrounding time points to state $k, \mathbf{V}_{g}^{\star}\left(s_{E}+u_{2}+1\right)=$ $k=\mathbf{V}_{g}^{\star}\left(s_{E}+u_{2}+2+u_{1}\right)$. The complementary move, which proposes to move back from $\mathbf{V}_{g}^{\star}$ to $\mathbf{V}_{g}^{(i-1)}$, is the inclusion move, which re-allocates the sequence $s_{E}+u_{2}+2, \ldots, s_{E}+$ $u_{2}+1+u_{1}$ back to state $k$. To this end, the complementary inclusion move has to select a point $t_{0} \in\left\{s_{E}+u_{2}+2, \ldots, s_{E}+u_{2}+u_{1}+1\right\}$. It follows that $s_{I}=s_{E}+u_{2}+1$ and $t_{I}=s_{E}+u_{2}+u_{1}+2$ in Eqs. (45-46) are well-defined, and it is guaranteed that the "equal boundaries" test: $\mathbf{V}_{g}^{\star}\left(s_{E}+u_{2}+1\right)=\tilde{k}=\mathbf{V}_{g}^{\star}\left(s_{E}+u_{2}+u_{1}+2\right)$ with $\tilde{k} \neq k$ is successful. Thus, the complementary inclusion move has the proposal probability:

$$
Q_{I}^{C}\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)=\frac{L_{E}}{T-1}
$$

where $L_{E}=u_{1}$ is the subsequence length parameter, which has been randomly drawn during the exclusion move. Hence, according to the Metropolis-Hastings criterion, the exclusion move, described above, is accepted with probability $A=\min \{1, R\}$, where

$$
R=\frac{P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}}, \delta_{g}\right)} \cdot \frac{Q_{I}^{C}\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)}{Q_{E}\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)}
$$

The likelihood ratio can be computed with Eq. (12), and the Hastings ratio can be computed with Eqs. (44) and (48).

# Complementary exclusion move for the inclusion move 

Consider the inclusion move from $\mathbf{V}_{g}^{(i-1)}$ to $\mathbf{V}_{g}^{\star}$, described above. The data points in the sequence $s_{I}+1, \ldots, t_{I}-1$, which were allocated to state $k$, have been re-allocated to state $\tilde{k}$, and the design of the inclusion move ensures that the new candidate vector, $\mathbf{V}_{g}^{\star}$, allocates the surrounding time points to state $\tilde{k}$ as well: $\mathbf{V}_{g}^{\star}\left(s_{I}\right)=\tilde{k}=\mathbf{V}_{g}^{\star}\left(t_{I}\right)$.

The complementary move, which proposes to move back from $\mathbf{V}_{g}^{\star}$ to $\mathbf{V}_{g}^{(i-1)}$, is the exclusion move, which re-allocates the subsequence $s_{I}+1, \ldots, t_{I}-1$ of length $L_{I}=t_{I}-s_{I}-1$ to state $k$. To this end, the complementary exclusion move has to select one single point $t_{0}$ out of the sequence $s_{E}^{C}+1, \ldots, t_{E}^{C}-1$ where

$$
s_{E}^{C}:=\max \left\{\tilde{t} \in\left\{2, \ldots, s_{I}-1\right\} ; \mathbf{V}_{g}^{\star}(\tilde{t}) \neq \tilde{k}\right\}
$$

and $s_{E}^{C}=1$ if $s_{E}^{C}$ is not well-defined.

$$
t_{E}^{C}:=\min \left\{\tilde{t} \in\left\{t_{I}+1, \ldots, T\right\} ; \mathbf{V}_{g}^{(\star}(\tilde{t}) \neq \tilde{k}\right\}
$$

and $t_{E}^{C}=T+1$ if $t_{E}^{C}$ is not well-defined.
Having selected $t_{0}$, the "subsequence length" $u_{1}:=L_{I}$ and the "lag" $u_{2}:=s_{I}-s_{E}^{C}-1$ have to be sampled out of the sets $\left\{1, \ldots, L_{E}^{C}-2\right\}$ and $\left\{0, \ldots, L_{E}^{C}-2-u_{1}\right\}$, respectively, where $L_{E}^{C}:=t_{E}^{C}-s_{E}^{C}-1$ is the length of the sequence $s_{E}^{C}+1, \ldots, t_{E}^{C}-1$. Finally, the complementary exclusion move has to randomly draw the state $k$ from all $\mathcal{K}_{g}^{(i-1)}-1$ states unequal to $\tilde{k}$. Thus, the complementary exclusion move has the proposal probability:

$$
Q_{E}^{C}\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)=\frac{L_{E}^{C}}{T-1} \cdot \frac{1}{L_{E}^{C}-2} \cdot \frac{1}{L_{E}^{C}-1-u_{1}} \cdot \frac{1}{\mathcal{K}_{g}^{(i-1)}-1}
$$

Hence, according to the standard Metropolis-Hastings criterion, the inclusion move, described above, is accepted with probability $A=\min \{1, R\}$, where

$$
R=\frac{P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}}, \delta_{g}\right)} \cdot \frac{Q_{E}^{C}\left(\mathbf{V}_{g}^{(i-1)} \mid \mathbf{V}_{g}^{\star}\right)}{Q_{I}\left(\mathbf{V}_{g}^{\star} \mid \mathbf{V}_{g}^{(i-1)}\right)}
$$

The likelihood ratio can be computed with Eq. (12), and the Hastings ratio can be computed with Eqs. (47) and (52).

# Appendix 4: The novel birth and the novel death move for the proposed HMM-DBN model 

The novel birth and the novel death move both keep the network $\mathcal{M}=\left(\pi_{1}, \ldots, \pi_{N}\right)$ and the SNR hyperparameters fixed. I describe the $i$ th MCMC iteration, $(i-1) \rightarrow i$, of the Metropolis-Hastings Birth/Death move for node $g$. Draw an unbiased coin to decide whether a birth or a death move is performed. Given the current allocation vector, $\mathbf{V}_{g}^{(i-1)}$, the birth move proposes to increase the number of states by $1, \mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}+1$, while the death move proposes to decrease the number of states by $1, \mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}-1$. Thereby both moves propose a new candidate allocation vector $\mathbf{V}_{g}^{\star}$. If the move is accepted, set $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{\star}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{\star}$, or otherwise leave the allocation vector unchanged, i.e. set: $\mathbf{V}_{g}^{(i)}=\mathbf{V}_{g}^{(i-1)}$ and $\mathcal{K}_{g}^{(i)}=\mathcal{K}_{g}^{(i-1)}$.

## The novel birth move

If the current number of states has reached the maximum, $\mathcal{K}_{g}^{(i-1)}=\mathcal{K}_{\text {MAX }}$, skip the move. Otherwise, randomly select one state $k_{0} \in\left\{1, \ldots, \mathcal{K}_{g}^{(i-1)}\right\}$ and determine the set of all data points that are currently allocated to state $k_{0}$ :

$$
T_{0}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{(i-1)}(t)=k_{0}\right\}
$$

If the number of data points in the set $T_{0}$ is lower than $2,\left|T_{0}\right|<2$, skip the birth move. Otherwise, draw a random number $b_{1}$ from the set $\left\{1, \ldots,\left|T_{0}\right|-1\right\}$. Order the time points in the set $T_{0}$, and let $t_{1}, \ldots, t_{\left|T_{0}\right|}$ denote the ordering of the data points in the set $T_{0}$. The birth move proposes to re-allocate the last $\left|T_{0}\right|-b_{1}$ data points, $t=t_{b_{1}+1}, \ldots, t_{\left|T_{0}\right|}$, with $\mathbf{V}_{g}^{(i-1)}(t)=k_{0}$ to a new state $k_{\text {new }}:=\mathcal{K}_{g}^{(i-1)}+1$. The new candidate allocation vector is given by: $\mathbf{V}_{g}^{\star}(t)=k_{\text {new }}$ for $t=t_{b_{1}+1}, \ldots, t_{\left|T_{0}\right|}$, and $\mathbf{V}_{g}^{\star}(t)=\mathbf{V}_{g}^{(i-1)}(t)$ for all other data points $t$. The proposal probability is given by:

$$
Q_{B}\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right] \mid\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)=\frac{1}{\mathcal{K}_{g}^{(i-1)}} \cdot \frac{1}{\left|T_{0}\right|-1}
$$

## The novel death move

If the number of states is equal to one, $\mathcal{K}_{g}^{(i-1)}=1$, skip the move. Otherwise, randomly select $k_{1}$ and $k_{2}$ with $k_{1}<k_{2}$ out of the set $\left\{1, \ldots, \mathcal{K}_{g}^{(i-1)}\right\}$. Determine the sets of data points

that are currently allocated to $k_{1}$ and $k_{2}$ :

$$
\begin{aligned}
& T_{1}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{(i-1)}(t)=k_{1}\right\} \\
& T_{2}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{(i-1)}(t)=k_{2}\right\}
\end{aligned}
$$

If one of the two sets is empty, skip the move. Otherwise, order the data points in $T_{1}$ and $T_{2}$, and let $t_{1}^{[1]}, \ldots, t_{|T_{1}|}^{[1]}$ and $t_{1}^{[2]}, \ldots, t_{|T_{2}|}^{[2]}$ denote the orders of the time points in $T_{1}$ and $T_{2}$, respectively. Check whether the time points in $T_{1}$ and $T_{2}$ are "separated" (not "overlapping"), i.e. check if either $t_{1}^{[1]}>t_{|T_{2}|}^{[2]}$ or $t_{1}^{[2]}>t_{|T_{1}|}^{[1]}$. If the test fails, skip the move. Otherwise, the birth move proposes to re-allocate all time points in the set $T_{2}$ to state $k_{1}$. The new candidate allocation vector is then given by: $\mathbf{V}_{g}^{\star}(t)=k_{1}$ for $t \in T_{2}$, and $\mathbf{V}_{g}^{\star}(t)=\mathbf{V}_{g}^{(i-1)}(t)$ for $t \notin T_{2}$, and the proposal probability is:

$$
Q_{D}\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)=\frac{2}{\mathcal{K}_{g}^{(i-1)} \cdot\left(\mathcal{K}_{g}^{(i-1)}-1\right)}
$$

The new candidate allocation vector, $\mathbf{V}_{g}^{\star}$, does not allocate time points to the state $k_{2}$ anymore. If $k_{2} \neq \mathcal{K}_{g}^{(i-1)}$, perform a swap move, i.e. set $\mathbf{V}_{g}^{\star}(t)=k_{2}$ for all $t$ with $\mathbf{V}_{g}^{(i-1)}(t)=\mathcal{K}_{g}^{(i-1)}$. The last state is then obsolete and can be deleted, i.e. set: $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}-1$.

# Complementary death move for the birth move 

Consider the birth move from $\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]$ to $\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]$, described above. The data points $t_{b_{1}+1}, \ldots, t_{|T_{0}|}$, which were allocated to state $k_{0}$, have been re-allocated to the new state $k_{\text {new }}=\mathcal{K}_{g}^{(i-1)}+1$. The complementary death move has to select the states $k_{0}$ and $k_{\text {new }}$ out of the set $\left\{1, \ldots, \mathcal{K}_{g}^{\star}\right\}$, where $\mathcal{K}_{g}^{\star}=\mathcal{K}_{g}^{(i-1)}+1$, and then has to re-allocate all data points in the set

$$
T_{0}^{C}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{\star}(t)=k_{\text {new }}\right\}
$$

back to state $k_{0}$. The design of the birth move ensures that the two sets

$$
\begin{aligned}
& T_{1}^{C}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{\star}(t)=k_{0}\right\} \\
& T_{2}^{C}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{\star}(t)=k_{\text {new }}\right\}
\end{aligned}
$$

are non-empty, and that the highest time point in $T_{1}^{C}$ precedes the lowest time point in $T_{2}^{C}$, i.e. that the two sets are "separated" (non-overlapping). Hence, the complementary death move can be performed, i.e. will not be skipped, and has the proposal probability:

$$
Q_{D}^{C}\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right)=\frac{2}{\left(\mathcal{K}_{g}^{(i-1)}+1\right) \cdot \mathcal{K}_{g}^{(i-1)}}
$$

According to the standard Metropolis-Hastings criterion, the birth move, described above, is accepted with probability $A=\min \{1, R\}$, where

$$
R=\frac{P\left(\mathcal{K}_{g}^{\star}\right) P\left(\mathbf{V}_{g}^{\star} \mid \mathcal{K}_{g}^{\star}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{\star}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{\star}}, \delta_{g}\right)}{P\left(\mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{V}_{g}^{(i-1)} \mid \mathcal{K}_{g}^{(i-1)}\right) P\left(\mathbf{y}_{g, \mathbf{V}_{g}^{(i-1)}} \mid \mathbf{X}_{g, \mathbf{V}_{g}^{(i-1)}}, \delta_{g}\right)} \cdot Q
$$

and

$$
Q=\frac{Q_{D}^{C}\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right.}{\left.Q_{B}\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right] \mid\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)}
$$

The likelihood ratio can be computed with Eq. (12), and the Hastings ratio, $Q$, can be computed with Eqs. (55) and (62).

# Complementary birth move for the death move 

Consider the death move from $\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]$ to $\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]$, described above. The birth move has proposed to re-allocate all time points of the set.

$$
T_{2}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{(i-1)}(t)=k_{2}\right\}
$$

to state $k_{1}$. The complementary birth move has to select the state $k_{1} \in\left\{1, \ldots, \mathcal{K}_{g}^{\star}\right\}$, and the design of the death move guarantees that the set:

$$
T_{0}^{C}=\left\{t \in\{2, \ldots, T\} \mid \mathbf{V}_{g}^{\star}(t)=k_{1}\right\}
$$

has a cardinality greater than 2 . Subsequently, the random number $b_{1}^{C}:=\left|T_{0}^{C}\right|-\left|T_{2}\right|$ has to be drawn from the set $\left\{1, \ldots,\left|T_{0}^{C}\right|-1\right\}$. Ordering all the time points in the set $T_{0}^{C}$, yields the order $t_{1}, \ldots, t_{\left|T_{0}^{C}\right|}$, and the complementary birth move proposes to re-allocate the last $\left|T_{0}^{C}\right|-b_{1}^{C}=\left|T_{2}\right|$ time points, $t=t_{b_{1}^{C}+1}, \ldots, t_{\left|T_{0}^{C}\right|}$ to a new state $k_{\text {new }}:=\mathcal{K}_{g}^{(i-1)}+1 .{ }^{26}$ The design of the death move, i.e. the successfully passed "separation" test, guarantees that the data points $t_{b_{1}^{C}+1}, \ldots, t_{\left|T_{0}^{C}\right|}$ correspond to the data points in the set $T_{2}$. The complementary birth move has the proposal probability:

$$
Q_{B}^{C}\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right)=\frac{1}{\mathcal{K}_{g}^{\star}} \cdot \frac{1}{\left|T_{0}^{C}\right|-1}
$$

Hence, according to the standard Metropolis-Hastings criterion, the death move, described above, is accepted with probability $A=\min \{1, R\}$, where $R$ was defined in Eq. (63) and the Hastings Ratio, $Q$, is now given by:

$$
Q=\frac{Q_{B}^{C}\left(\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right] \mid\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right]\right.}{\left.Q_{D}\left(\left[\mathbf{V}_{g}^{\star}, \mathcal{K}_{g}^{\star}\right] \mid\left[\mathbf{V}_{g}^{(i-1)}, \mathcal{K}_{g}^{(i-1)}\right]\right)}\right.
$$

and can be computed with Eqs. (58) and (67).
