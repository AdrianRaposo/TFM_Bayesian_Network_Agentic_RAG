# High-Dimensional Bayesian Network Classification with Network Global-Local Shrinkage Priors 

Sharmistha Guha* and Abel Rodriguez ${ }^{\dagger}$


#### Abstract

This article proposes a novel Bayesian binary classification framework for networks with labeled nodes. Our approach is motivated by applications in brain connectome studies, where the overarching goal is to identify both regions of interest (ROIs) in the brain and connections between ROIs that influence how study subjects are classified. We propose a novel binary logistic regression framework with the network as the predictor, and model the associated network coefficient using a novel class of global-local network shrinkage priors. We perform a theoretical analysis of a member of this class of priors (which we call the Network Lasso Prior) and show asymptotically correct classification of networks even when the number of network edges grows faster than the sample size. Two representative members from this class of priors, the Network Lasso prior and the Network Horseshoe prior, are implemented using an efficient Markov Chain Monte Carlo algorithm, and empirically evaluated through simulation studies and the analysis of a real brain connectome dataset.


Keywords: brain connectome, high-dimensional binary regression, global-local shrinkage prior, node selection, network predictor, posterior consistency.

## 1 Introduction

Statistical models for the analysis of individual networks have received substantial attention in the literature. Examples include random graph models (Erdos and Rényi, 1960), exponential random graph models (Frank and Strauss, 1986), social space models (Hoff et al., 2002; Hoff, 2005, 2009; Guhaniyogi and Rodriguez, 2020; Sosa and Rodríguez, 2021) and stochastic block models (Nowicki and Snijders, 2001; Rodriguez, 2012). However, there are many important applications in which network data is available for every individual in the sample, and interest lies in using such networks as predictors to explain an outcome of interest, rather than understanding the underlying process that drives network formation. Section 6 in this article presents one such example from a brain connectome study. In this study, brain connectome networks are available for multiple individuals who are classified as subjects with high or low IQ (Intelligence Quotient). To construct the networks, the human brain has been divided according to the Desikan Atlas (Desikan et al., 2006) that identifies 34 cortical regions of interest (ROIs), both in the left and the right hemispheres of the human brain, implying 68 cortical ROIs in all. A brain network for each subject is represented by a symmetric adjacency matrix

[^0]
[^0]:    *Department of Statistics, Texas A\&M University, College Station, TX 77843, sharmistha@tamu. edu
    ${ }^{\dagger}$ Department of Statistics, University of Washington, Seattle, WA 98195, abelrod@uw.edu

whose rows and columns correspond to the different ROIs (shared among networks for all individuals) and whose entries correspond to estimates of the number of fibers connecting pairs of brain regions. The scientific goals in this setting are (1) to develop a predictive rule for classifying a new subject as having low or high IQ based on his/her observed brain network, and (2) to identify influential brain regions (nodes in the brain network) as well as significant connections between different brain regions (links in the network) that are predictive of IQ.

Much of the early literature on network and graph classification was motivated by the problem of classification of chemical compounds, where a graph represents a compound's molecular structure. In such analyses, discriminative patterns in a graph were identified and used as features for training a standard classification method (e.g., see Srinivasan et al., 1996, Helma et al., 2001, Deshpande et al., 2005 and Fei and Huan, 2010). Similar approaches, based on summary measures such as average degree, clustering coefficient and average path length, have also been employed in the context of neuroscience applications (e.g., see Bullmore and Sporns, 2009, Olde Dubbelink et al., 2013, Daianu et al., 2013 and references therein). Alternative approaches use kernels defined on graph spaces to construct similarity metrics between two networks (e.g., see Vishwanathan et al., 2010), which in turn can be used to build, for example, nearestneighbor classifiers. While all these methods scale well with the size of the network, it is our experience that the choice of features/kernels (which is typically ad-hoc) has a dramatic influence on the results. Furthermore, these type of methods typically do not allow for a full exploration of which nodes/edges are influential on the responses. Other relevant references in this area include Vogelstein et al. (2013), who propose to look for a minimal set of nodes which best explains the difference between two groups of networks, and Durante et al. (2018), who propose a high-dimensional Bayesian tensor factorization model for a population of networks that allows to test for local edge differences between two groups of subjects. Both of these approaches tend to focus mainly on classification and are not designed to detect important nodes and edges impacting the response.

An alternate approach to constructing classifiers based on network data is to vectorize the network predictor and treat the edge weights as a long vector of predictors (e.g., see Richiardi et al., 2011, Craddock et al., 2009 and Zhang et al., 2012) in a binary regression setting. This approach can take advantage of recent developments in high-dimensional regression, either penalized likelihood estimation (e.g., see Tibshirani, 1996) or Bayesian shrinkage (e.g., see Park and Casella, 2008, Carvalho et al., 2010, Armagan et al., 2013a, and Du and Ghosal, 2018). However, such an approach treats the links of the network as exchangeable, ignoring the fact that coefficients involving common nodes can be expected to be correlated a-priori. In other words, it does not capture the fact that we expect, a priori, higher correlation among coefficients that share one node in common. Being agnostic to the structure of the network predictor, the ordinary shrinkage priors are not well adapted to node-level (as opposed to edge-level) inference.

This article develops a high-dimensional Bayesian network classifier that can identify both influential nodes and specific edges impacting classification. To achieve this goal, we formulate a high-dimensional logistic regression model with the binary response regressed on the network predictor. While the model can be represented as a linear

function of the network data, we carefully add structure to the network coefficient and design prior distributions to exploit the network topology and draw inference on influential network nodes. More concretely, the coefficients associated with the network predictor are assigned a prior from the class of network global-local shrinkage priors. In the context of linear regression, Guha and Rodriguez (2021) develop a special case of the network shrinkage prior, known as the Network Lasso prior. This article generalizes the earlier approach to develop a broader class of network shrinkage priors. In particular, this article introduces another member of this broad class of priors, called the Network Horseshoe prior, and presents a comparative study of the empirical performance of these two priors in various simulation settings and in the brain network data. Another related approach has been proposed by Reliön et al. (2019), who develop a method that relies on a combination of regular and group Lasso penalties within a logistic regression framework to carry out network classification. One key advantage of our Bayesian approach over this penalized likelihood method is our ability to fully quantify the uncertainty associated with our estimates.

A major contribution of this article is a careful study of the asymptotic properties of the resulting binary network classification framework. Theory for posterior contraction for high-dimensional regression models has gained traction over the last 10 years. For example, Castillo et al. (2012) and Belitser and Nurushev (2015) have established posterior concentration and variable selection properties for certain point-mass priors in linear regression models. The latter article also establishes asymptotically nominal coverage of Bayesian credible sets (see also Castillo et al., 2015 and Martin et al., 2017). In the same thread, Jeong and Ghosal (2021) develop posterior contraction properties for sparse generalized linear models with variable selection priors on coefficients. In contrast, the literature on posterior contraction properties for high-dimensional Bayesian shrinkage priors is less well developed. Armagan et al. (2013b) were the first to show posterior consistency in the ordinary linear regression model with shrinkage priors for low-dimensional settings under the assumption that the number of covariates does not exceed the number of observations. Using direct calculations, Van Der Pas et al. (2014) have shown that the posterior based on the ordinary horseshoe prior concentrates at the optimal rate for normal-mean problems. More recently, Song and Liang (2017) consider a general class of global-local continuous shrinkage priors and obtain posterior contraction rates in ordinary high-dimensional linear regression models. Bai and Ghosh (2018), and later Zhang and Ghosh (2019), have developed posterior contraction theory for global-local shrinkage priors in the context of multivariate regression frameworks. An insightful review on properties of the posterior distribution under global-local shrinkage priors is available in Bhadra et al. (2019). Notably, the posterior contraction literature for global-local shrinkage priors on binary logistic regression is limited, with a few exceptions, such as Wei and Ghosal (2020). In this article we develop posterior contraction theory for the Network Lasso prior. Our development requires considerably different techniques and results compared to Wei and Ghosal (2020). In fact, developing the theory for network classification with the Network Lasso prior proposed in this article faces two major challenges. First, our prior has a low-rank structure in the prior mean of the edge coefficients, based on node specific latent variables (Guha and Rodriguez, 2021), as well as an additional shrinkage structure through the variance. Second, we introduce

a variable selection prior on the node-specific latent variables. The combination of these two structures adds substantial theoretical challenges over and above Wei and Ghosal (2020), so that different proof techniques are required (see Section 1 of the Supplementary Material (Guha and Rodriguez, 2023)). Second, we aim to prove a challenging but practically desirable result of asymptotically correct classification when the number of edges in the network predictor grows at a super-linear rate as a function of the sample size. Both these features present obstacles which we overcome in this work. The theoretical results provide insights on how the number of nodes in the network predictor, the dimensions of node-specific latent variables, and the structure and sparsity in the true network predictor coefficients can vary with the sample size $n$ to achieve asymptotically correct classification.

The remainder of the manuscript is organized as follows: Section 2 develops the model and the prior distributions. Section 3 discusses theoretical developments justifying the asymptotically desirable prediction from the proposed model. Section 4 details posterior computation. Results from various simulation experiments and a brain connectome data analysis have been presented in Sections 5 and 6, respectively. Finally, Section 7 concludes the article with a brief discussion of the proposed methodology.

# 2 Model Framework 

### 2.1 Notation

For $i=1, \ldots, n$, let $\boldsymbol{A}_{i} \in \mathbb{R}^{V \times V}$ denote the weighted undirected network predictor with $V$ nodes, and $y_{i} \in\{0,1\}$ be the binary response corresponding to the $i$-th individual. The entry $a_{i, k, l} \in \mathbb{R}$ of $\boldsymbol{A}_{i}$ indicates the strength of association between the $k$-th and $l$-th nodes of the network. Our framework allows entries of $\boldsymbol{A}_{i}$ to be continuous, binary or count. In this paper, we focus on networks that have no self relationships, i.e., $a_{i, k, l} \equiv 0$ when $k=l$, and are undirected $\left(a_{i, k, l}=a_{i, l, k}\right)$, but generalizations to directed networks are straightforward.

### 2.2 Model Formulation

In the context of network classification, we propose a high-dimensional logistic regression model of the binary response $y_{i} \in\{0,1\}$ on the undirected network predictor $\boldsymbol{A}_{i}$ as

$$
y_{i} \sim \operatorname{Ber}\left(G\left(\psi_{i}\right)\right), \quad \psi_{i}=\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}
$$

where $G: \mathrm{R} \rightarrow[0,1]$ is a link function and $\boldsymbol{\Gamma}$ is a $V \times V$ symmetric network coefficient matrix whose $(k, l)$-th element is given by $\gamma_{k, l} / 2$, with $\gamma_{k, k}=0$, for all $k=1, \ldots, V$. The notation $\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}$ denotes the Frobenius inner product between the two matrices $\boldsymbol{A}_{i}$ and $\boldsymbol{\Gamma}$, defined as the sum of the element-wise product between the two matrices. For conciseness, we focus on logistic models in this paper, where $G(z)=[1+\exp \{-z\}]^{-1}$, but our prior formulation can be easily adapted to other link functions.

Model (2.1) can be expressed in the form of a generalized linear model. To be more specific, $\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}=\sum_{1 \leq k<l \leq V} a_{i, k, l} \gamma_{k, l}$, due to the symmetry and zero diagonal entries

in $\boldsymbol{A}_{i}$ and $\boldsymbol{\Gamma}$, so that

$$
\psi_{i}=\mu+\sum_{1 \leq k<l \leq V} a_{i, k, l} \gamma_{k, l}
$$

Furthermore, note that, if $\boldsymbol{x}_{i}=\left(a_{i, 1,2}, \ldots, a_{i,(V-1), V}\right)^{\prime} \in \mathbb{R}^{V(V-1) / 2}$ is the collection of all upper triangular elements of $\boldsymbol{A}_{i}$, and $\gamma=\left(\gamma_{1,2}, \ldots, \gamma_{(V-1), V}\right)^{\prime} \in \mathbb{R}^{V(V-1) / 2}$ is the vector of corresponding upper triangular elements of $2 \boldsymbol{\Gamma}$, then the linear predictor can be written as $\psi_{i}=\mu+\boldsymbol{x}_{i}^{\prime} \gamma$.

Specifying an ordinary high-dimensional shrinkage prior on $\gamma$, such as the ones described in Carvalho et al. (2010); Armagan et al. (2013a); Park and Casella (2008), is unsatisfactory in our context since (a) it loses information on network nodes and makes inference on influential network nodes (with uncertainty) difficult; and (b) it does not capture the fact that we expect, a priori, higher correlation among coefficients that share one node in common. These shortcomings motivate the development of the priors in the next Section.

# 2.3 Network Global-Local Shrinkage Priors 

Let $\boldsymbol{u}_{1}, . ., \boldsymbol{u}_{V}$ be a collection of $R$-dimensional latent variables, one for each of the $V$ nodes in the network. In this article, we consider a $N(0,1)$ prior for the common intercept parameter $\mu$ and propose a general class of network global-local shrinkage priors on the edge coefficients $\gamma_{k, l}$ 's given by,

$$
\gamma_{k, l} \mid s_{k, l}, \sigma^{2} \sim N\left(\boldsymbol{u}_{k}^{\prime} \boldsymbol{\Lambda} \boldsymbol{u}_{l}, \sigma^{2} s_{k, l}^{2}\right), \quad \sigma \sim H_{1}(\cdot), \quad s_{k, l} \sim H_{2}(\cdot)
$$

where $\boldsymbol{\Lambda}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{R}\right)$ is an $R \times R$ diagonal matrix, with the $r$-th diagonal entry $\lambda_{r}$. In this framework, $\mathrm{E}(\boldsymbol{\Gamma})=\boldsymbol{U}^{\prime} \boldsymbol{\Lambda} \boldsymbol{U}$, where $\boldsymbol{U}$ is a matrix whose $k$-th column corresponds to $\boldsymbol{u}_{k}$. This representation, related to the eigenvalue decomposition of $\boldsymbol{\Gamma}$, provides an embedding into an $R \leq V$ dimensional latent space. This kind of embedding has been widely used to construct sparse models for network data that can capture common properties such as transitivity (Hoff, 2005). Furthermore, the multiplicative structure associated with the prior variance allows for both global (controlled by $\sigma^{2}$ ) and local (controlled by the $s_{k, l}$ 's) shrinkage effects.

The formulation in (2.2) leads to a wide variety of network shrinkage priors by choosing different forms for $H_{1}(\cdot)$ and $H_{2}(\cdot)$. For example, setting $H_{1}(\sigma)$ as a point mass at 1 and $H_{2}\left(s_{k, l}^{2}\right)$ as an exponential distribution, $s_{k, l}^{2} \sim \operatorname{Exp}(\theta / 2)$ with $\theta \sim \operatorname{Gamma}(\zeta, \iota)$, corresponds to the Network Lasso prior discussed in Guha and Rodriguez (2021). Alternatively, setting both $H_{1}$ and $H_{2}$ to be half-Cauchy distributions, leads to what we call the Network Horseshoe prior (see Carvalho et al., 2010).

In order to identify which nodes are actively related to the response, we assign a zero-inflated Gaussian prior on the latent factors $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{V}$

$$
\boldsymbol{u}_{k} \mid \xi_{k}, \boldsymbol{M} \sim \xi_{k} N(\mathbf{0}, \boldsymbol{M})+\left(1-\xi_{k}\right) \delta_{\mathbf{0}}, \quad \boldsymbol{M} \sim I W(\nu, \boldsymbol{I})
$$

where $\xi_{k} \mid \Delta \sim \operatorname{Ber}(\Delta)$ and $\Delta \sim \operatorname{Beta}\left(a_{\Delta}, b_{\Delta}\right)$. Here, $\delta_{\mathbf{0}}$ is the Dirac-delta function at $\mathbf{0}$, $\boldsymbol{M}$ is a $R \times R$ covariance matrix and $I W(\nu, \boldsymbol{I})$ denotes an inverse-Wishart distribution with parameters $\nu$ and $\boldsymbol{I}$. The parameter $\Delta$ corresponds to the prior probability of the nonzero $\boldsymbol{u}_{k}$. Note that, if the $k$-th node of the network predictor is inactive in predicting the response, then a-posteriori $\xi_{k}$ should assign high probability to 0 . Thus, we can use the posterior probability of the event $\left\{\xi_{k}=0\right\}$ to identify influential nodes. Assigning a prior distribution to $\Delta$ ensures multiplicity correction in the simultaneous selection of multiple $\boldsymbol{u}_{k}$ 's (Scott and Berger, 2010).

An important aspect of these models is the selection of the model rank $R$. In order to learn the effective dimension of the latent space in which the matrix of coefficients is being embedded, we employ a hierarchical prior of the form

$$
\lambda_{r} \sim \operatorname{Ber}\left(\pi_{r}\right), \quad \pi_{r} \sim \operatorname{Beta}\left(1, r^{\eta}\right), \quad \eta>1
$$

Note that, if $\lambda_{r}=0$, the $r$-th component of the vectors $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{V}$ has no effect on the value of the regression coefficients. Hence, $R_{\text {eff }}=\sum_{r=1}^{R} \lambda_{r} \leq R$ can be interpreted as the effective dimensionality of the model. In this context, the choice of hyper-parameters of the beta distribution is crucial. In particular, note that $E\left[\lambda_{r}\right]=1 /\left(1+r^{\eta}\right) \rightarrow 0$ as $r \rightarrow \infty$ and that $\sum_{r=1}^{R} \operatorname{var}\left(\lambda_{r}\right)=\sum_{r=1}^{R} \frac{r^{\eta}}{\left(1+r^{\eta}\right)^{2}\left(2+r^{\eta}\right)}<\infty$ as $R \rightarrow \infty$. The first property provides (weak) identifiability of the different latent dimensions, while the second ensures that $\lim _{R \rightarrow \infty} \operatorname{var}\left(\boldsymbol{u}_{k}\right)<\infty$ as long as the prior for the $\boldsymbol{u}_{k}$ 's has a finite second moment. For our empirical investigations in Sections 5 and 6, we set $\eta=1.1$.

Under the previous formulation, we can think about selecting R as similar to selecting the truncation level of a large dimensional model. As long as $R$ is "large enough", the results should be robust to our choice (and further increasing $R$ would lead to negligible changes). Natural analogies are the truncation of a Dirichlet process mixture model which results in an (approximate) finite mixture model, and the truncation of the stick-breaking construction of the Indian Buffet process (Teh et al., 2007). In our illustrations, we perform sensitivity analyses to determine an optimal value of $R$ that balances computational efficiency and inferential accuracy, noting that further increases in $R$ beyond the optimal value do not lead to any significant change in model performance. Along with $R$, sensitivity analyses regarding the choice of hyper-parameters $\iota, \zeta, a_{\Delta}, b_{\Delta}$ and $\nu$ are also performed and recorded in the simulation studies.

# 3 Posterior Contraction of the Binary Network Classification Model 

This section establishes convergence results for (2.1) under the Network Lasso shrinkage prior given by $\gamma_{k, l} \mid s_{k, l} \sim N\left(\boldsymbol{u}_{k}^{\prime} \boldsymbol{\Lambda} \boldsymbol{u}_{l}, s_{k, l}^{2}\right), s_{k, l}^{2} \sim \operatorname{Exp}\left(\theta_{n} / 2\right)$. For the theoretical study, a common practice is to fix $\theta_{n}$ as a function of $n$ (Armagan et al., 2013a). Our theoretical investigations fix this function, with the exact expression given in Condition (6) in Section 3.2.

In our analysis, we consider an asymptotic setting in which the number of nodes in the network predictor, $V_{n}$, grows with the sample size $n$. This framework attempts to

capture the fact that the number of coefficients, $q_{n}=\frac{V_{n}\left(V_{n}-1\right)}{2}$, will typically be much larger than $n$. This creates theoretical challenges, which are related to (but distinct from) those faced in showing posterior consistency for high-dimensional continuous (Armagan et al., 2013a) and binary regressions (Wei and Ghosal, 2020).

# 3.1 True Data Distribution and Assumption for the True Network Coefficient 

Let $\boldsymbol{y}_{n}=\left(y_{1}, \ldots, y_{n}\right)^{\prime}$ be the vector of observations. Using the subscript 0 to indicate the true parameter values, the data generating model is assumed to be

$$
y_{i} \sim \operatorname{Ber}\left(\frac{\exp \left\{\psi_{i, 0}\right\}}{1+\exp \left\{\psi_{i, 0}\right\}}\right), \quad \psi_{i, 0}=\mu_{0}+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}_{0}\right\rangle_{F}
$$

where $\mu_{0}$ is the true intercept in the network predictor and $\boldsymbol{\Gamma}_{0}$ is the true symmetric network coefficient matrix. We assume that $\boldsymbol{\Gamma}_{0}$ can be represented by the sum of a symmetric low-dimensional matrix and a symmetric sparse matrix. Thus, we assume that $\gamma_{k, l, 0}=\boldsymbol{u}_{k, 0}^{\prime} \boldsymbol{\Lambda} \boldsymbol{u}_{l, 0}+\vartheta_{k, l, 0}$, where $\boldsymbol{u}_{k, 0}$ is a $R_{0}$ dimensional vector, $k=1, \ldots, V_{n}$. Also, $\boldsymbol{\vartheta}_{0}$ is the vector of all $\vartheta_{k, l, 0}, k<l$, and we denote the number of nonzero elements of $\boldsymbol{\vartheta}_{0}$ by $h_{n, 0}$, i.e., $\left\|\boldsymbol{\vartheta}_{0}\right\|_{0}=h_{n, 0}$.

For any $\epsilon>0$, define $\mathcal{A}_{n}=\left\{(\mu, \boldsymbol{\Gamma}): \frac{1}{n} \sum_{i=1}^{n}\left|p_{\mu, \boldsymbol{\Gamma}}\left(y_{i}=1\right)-p_{\mu_{0}, \boldsymbol{\Gamma}_{0}}\left(y_{i}=1\right)\right| \leq \epsilon\right\}$ as a neighborhood around the true density. This neighborhood construction has been used in Ghosal et al. (2006) in the context of density estimation in nonparametric binary regression with Gaussian processes. Further, let $\pi_{n}(\cdot)$ and $\Pi_{n}(\cdot)$ be the prior and posterior densities of $(\mu, \boldsymbol{\Gamma})$ based on $\boldsymbol{y}_{n}$, such that

$$
\Pi_{n}\left(\mathcal{A}_{n}^{c}\right)=\frac{\int_{\mathcal{A}_{n}^{c}} p_{\mu, \boldsymbol{\Gamma}}\left(\boldsymbol{y}_{n}\right) \pi_{n}(\mu, \boldsymbol{\Gamma}) d \mu d \boldsymbol{\Gamma}}{\int p_{\mu, \boldsymbol{\Gamma}}\left(\boldsymbol{y}_{n}\right) \pi_{n}(\mu, \boldsymbol{\Gamma}) d \mu d \boldsymbol{\Gamma}}
$$

where $p_{\mu, \boldsymbol{\Gamma}}\left(\boldsymbol{y}_{n}\right)$ denotes the likelihood of the $n$-dimensional response vector $\boldsymbol{y}_{n}$.

### 3.2 Main Results

To show the posterior contraction results, we generally follow Wei and Ghosal (2020) and Armagan et al. (2013a), but with substantial modifications required due to the nature of our proposed network lasso prior distribution. In proving the results, we make a couple of simplifications. First, it is assumed that the dimension $R_{n}$ of $\boldsymbol{u}_{k}$ is the same as $R_{0, n}$, the dimension of $\boldsymbol{u}_{k, 0}$, and that both of them increase with $n$. Consequently, the effective dimensionality of the latent space does not need to be estimated and $\boldsymbol{\Lambda}=\boldsymbol{I}$ is a non-random matrix. Second, we assume that $\boldsymbol{M}$ is non-random and $\boldsymbol{M}=\boldsymbol{I}$. Finally, we set hyper-parameters $a_{\Delta}=b_{\Delta}=1$ in proving our theoretical results. We emphasize that these assumptions are not essential for the contraction result to be true, and are only introduced in order to simplify the derivations.

For two sequences $\left\{C_{1, n}\right\}_{n \geq 1}$ and $\left\{C_{2, n}\right\}_{n \geq 1}, C_{1, n}=o\left(C_{2, n}\right)$ if $C_{1, n} / C_{2, n} \rightarrow 0$, as $n \rightarrow \infty$. The following theorem shows contraction of the posterior asymptotically under mild sufficient conditions on $V_{n}$ and $h_{n, 0}$. The proof of the theorem is provided in Section 1 of the Supplementary Material (Guha and Rodriguez, 2023).

Theorem 3.1. Assume

1. $\sup _{r=1, . ., R_{n} ; k=1, . ., V_{n}}\left|u_{k, r, 0}\right|<M_{u}<\infty$;
2. $R_{n} V_{n}=o\left(\frac{n}{\log (n)}\right) ; V_{n} \rightarrow \infty$ as $n \rightarrow \infty$.
3. $\left\|\boldsymbol{A}_{i}\right\|_{\infty}$ is bounded for all $i=1, . ., n$, w.l.o.g., assume $\left\|\boldsymbol{A}_{i}\right\|_{\infty} \leq 1$.
4. $h_{n, 0} \log \left(q_{n}\right)=o(n)$
5. $\left\|\boldsymbol{\vartheta}_{0}\right\|_{\infty}$ is bounded; w.l.g. $\left\|\boldsymbol{\vartheta}_{0}\right\|_{\infty}<1$
6. $\theta_{n}=\frac{C}{q_{n} n^{\rho / 2} \log (n)}$ for some $C>0$ and some $\rho \in(1,2)$.

Under assumptions (1)-(6) for the Network Lasso prior on $\boldsymbol{\Gamma}, \Pi_{n}\left(\mathcal{A}_{n}^{c}\right) \rightarrow 0$ as $n \rightarrow \infty$, for any $\epsilon>0$.

Conditions (1), (3) and (5) are technical conditions ensuring that each of the entries in the true network coefficient and the network predictor are bounded. Condition (2) puts an upper bound on the growth of the number of network nodes and dimensions of node specific latent variables vis-a-vis the sample size to achieve asymptotically correct classification of networks. Similarly, (4) puts a restriction on the number of nonzero elements of $\boldsymbol{\vartheta}_{0}$ with respect to $n$.

The proof bears some connections with the proofs of results in Wei and Ghosal (2020), but is significantly different from it, mainly due to the introduction of network shrinkage priors. Notably, the proof of Theorem 3.1 is built upon Lemma A. 1 and Lemma A. 2 (see Section 1 of Supplementary Material (Guha and Rodriguez, 2023)), where Lemma A. 2 is a new result specifically needed to address the network lasso prior structure in our framework. Additionally, as part of the proof of Theorem 3.1, we needed to establish that the posterior probability $-\log \Pi\left(\left\|\boldsymbol{W}-\boldsymbol{W}_{0}\right\|_{\infty}<\frac{q_{1}}{2 n^{\rho / 2}}\right)$ grows sublinearly with the sample size $n$, for a constant $\eta_{1}>0$, where $\boldsymbol{W}=\left(\boldsymbol{u}_{1}^{\prime} \boldsymbol{u}_{2}, \ldots, \boldsymbol{u}_{V_{n}-1}^{\prime} \boldsymbol{u}_{V_{n}}\right)^{\prime}$, $\boldsymbol{W}_{0}=\left(\boldsymbol{u}_{1,0}^{\prime} \boldsymbol{u}_{2,0}, \ldots, \boldsymbol{u}_{V_{n}-1,0}^{\prime} \boldsymbol{u}_{V_{n}, 0}\right)^{\prime}, \boldsymbol{u}_{k}=\left(u_{k, 1}, \ldots, u_{k, R_{n}}\right)^{\prime}$ and $\boldsymbol{u}_{k}=\left(u_{k, 1,0}, \ldots, u_{k, R_{n}, 0}\right)^{\prime}$, for $k=1, . ., V_{n}$. This result is also novel and specific to our construction of the Bayesian network lasso shrinkage prior. While the other parts in the proof of Theorem 3.1 exploit known techniques, they have been tailored specific to the result. The next few sections show empirical performance of the proposed class of priors.

# 4 Posterior Computation 

We have implemented Markov chain Monte Carlo (MCMC) samplers for posterior inference for both the Network Lasso and Network Horseshoe shrinkage priors on $\boldsymbol{\Gamma}$. We

use the result discussed in Theorem 1 of Polson et al. (2013) to obtain

$$
\begin{aligned}
p\left(y_{i} \mid \boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right) & =\frac{\exp \left\{y_{i}\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)\right\}}{1+\exp \left\{\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right\}} \\
& =\exp \left\{\left(y_{i}-0.5\right)\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)\right\} \int \exp \left(-\omega_{i}\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)^{2} / 2\right) p\left(\omega_{i}\right) d \omega_{i}
\end{aligned}
$$

where $p\left(\omega_{i}\right)$ is the density for $\mathrm{PG}(1,0)$ distribution. We exploit this result and rely on data augmentation approach as outlined in Polson et al. (2013) to introduce variables $\omega_{1}, \ldots, \omega_{n}$ in the likelihood and write the likelihood function associated with our model as

$$
\begin{aligned}
p\left(\boldsymbol{y} \mid \boldsymbol{A}_{1}, . ., \boldsymbol{A}_{n}, \boldsymbol{\Gamma}, \boldsymbol{\omega}\right) & \propto \prod_{i=1}^{n} p\left(y_{i} \mid \boldsymbol{A}_{i}, \boldsymbol{\Gamma}, \omega_{i}\right) \\
& \propto \prod_{i=1}^{n} \exp \left\{\left(y_{i}-0.5\right)\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)-\omega_{i}\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)^{2} / 2\right\} \\
& \propto \prod_{i=1}^{n} \exp \left\{-\frac{\omega_{i}}{2}\left[\frac{\left(y_{i}-0.5\right)}{\omega_{i}}-\left(\mu+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}\right\rangle_{F}\right)\right]^{2}\right\}
\end{aligned}
$$

Hence, while the original conditional posterior distributions for the parameters are not available in closed forms, the augmented full conditional distributions mostly belong to standard families. Sections 2 and 3 in the supplementary material provide details of the algorithms for the Network Lasso and Network Horseshoe priors on $\gamma$, respectively.

Let $\boldsymbol{\Gamma}^{(1)}, \ldots, \boldsymbol{\Gamma}^{(L)}$ and $\mu^{(1)}, \ldots, \mu^{(L)}$ be the $L$ MCMC samples for $\boldsymbol{\Gamma}$ and $\mu$, respectively, obtained after suitable burn-in and thinning. To classify a newly observed network $\boldsymbol{A}_{*}$ as a member of one of the two groups, we compute

$$
S^{(l)}=\frac{\exp \left(\mu^{(1)}+\left\langle\boldsymbol{A}_{*}, \boldsymbol{\Gamma}^{(l)}\right\rangle\right)}{1+\exp \left(\mu^{(1)}+\left\langle\boldsymbol{A}_{*}, \boldsymbol{\Gamma}^{(l)}\right\rangle\right)}
$$

for $l=1, \ldots, L$. Then $\boldsymbol{A}_{*}$ is classified as a member of group 'low' or 'high' if $\frac{1}{L} \sum_{l=1}^{L} S^{(l)}$ is less than or greater than a selected cut-off value $t_{c}$, respectively. Similarly, node $k$ is recognized to be influential in the classification process if $\frac{1}{L} \sum_{l=1}^{L} \xi_{k}^{(l)}>t_{n}$ for a prespecified threshold $t_{n}$, where $\xi_{k}^{(1)}, \ldots, \xi_{k}^{(L)}$ are the $L$ post burn-in MCMC samples of $\xi_{k}$. In the same spirit, we employ the algorithm described in Section 4 of the supplementary material to postprocess the posterior samples and identify the influential edges impacting the response. The algorithm takes care of multiplicity correction by controlling the false discovery rate (FDR). Finally, we obtain an estimate of the posterior distribution of the effective dimensionality, $\operatorname{Pr}\left(R_{\text {eff }}=r \mid\right.$ Data $) \approx \frac{1}{L} \sum_{l=1}^{L} I\left(\sum_{m=1}^{R} \lambda_{m}^{(l)}=r\right)$, where $I(A)$ for an event $A$ is 1 if the event $A$ happens and 0 otherwise, and $\lambda_{m}^{(1)}, \ldots, \lambda_{m}^{(L)}$ are the $L$ post burn-in MCMC samples of $\lambda_{m}$.

# 5 Simulation Studies 

This section evaluates the inferential and classification ability of two of our proposed network classification priors, the Bayesian Network Lasso classifier (BNLC) and the Bayesian Network Horseshoe classifier (BNHC), vis-a-vis a number of competitors using synthetic networks generated under various simulation settings. In each simulation, we assess the ability of the various approaches to correctly identify influential nodes and edges, to accurately estimate edge coefficients, and to classify a network with precise characterization of uncertainties.

### 5.1 Simulation Setup

For all of our simulations, data is generated from a logistic regression model of the form

$$
y_{i} \mid \boldsymbol{A}_{i}, \boldsymbol{\Gamma}_{0} \sim \operatorname{Ber}\left(\frac{\exp \left(\mu_{0}+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}_{0}\right\rangle_{F}\right)}{1+\exp \left(\mu_{0}+\left\langle\boldsymbol{A}_{i}, \boldsymbol{\Gamma}_{0}\right\rangle_{F}\right)}\right)
$$

where $\boldsymbol{\Gamma}_{0}$ is a symmetric matrix with zero diagonal entries. We fix the value of the intercept $\mu_{0}$ at 2 in all simulation scenarios, and then consider different mechanisms for constructing the matrix covariates $\boldsymbol{A}_{1}, \ldots, \boldsymbol{A}_{n}$ and the matrix of coefficients $\boldsymbol{\Gamma}_{0}$. In all of our experiments, we work with $V=25$ nodes and $n=250$ samples.

We study two different schemes for generating the network $\boldsymbol{A}_{i}$, referred to as Simulation 1 and Simulation 2, respectively. In Simulation 1, the values associated with the network edges are simulated from a standard normal distribution. In contrast, in Simulation 2, the nodes in each network are organized into communities so that nodes in the same community tend to have stronger connections than nodes belonging to different communities (i.e., the networks are generated from a blockmodel). This pattern closely mimics real brain connectome networks (Bullmore and Sporns, 2009). More specifically, in Simulation 2 we assign each node a community label, $f_{k} \in\{1,2,3\}, k=1, \ldots, V$. The node assignments are the same for all networks in the population, and the size of the communities are approximately the same. Given the community labels, the $\left(k, k^{\prime}\right)$ th element of $\boldsymbol{A}_{i}$ is simulated from $N\left(m_{f_{k}, f_{k^{\prime}}}, \sigma_{0}^{2}\right)$, where $m_{k, l}=0.5$ when $k=l$. When $k \neq l$, i.e., when the concerned edges connect nodes belonging to different communities, we sample a fixed number of edge locations randomly and simulate the values from $N(0,1)$, assigning the values at the remaining locations to be 0 . In all cases, we set $\sigma_{0}^{2}=1$.

On the other hand, the true matrix of coefficients $\boldsymbol{\Gamma}_{0}$ is constructed as the sum of a low-rank matrix $\boldsymbol{\Gamma}_{0,1}$, which provides the majority of the structure, and a sparse contamination matrix $\boldsymbol{\vartheta}_{0}$. To construct the matrix $\boldsymbol{\Gamma}_{0,1}$, we draw $V$ latent variables $\boldsymbol{u}_{k, 0}$, each of dimension $R_{0}$, from a mixture distribution given by

$$
\boldsymbol{u}_{k, 0} \sim \varrho_{0} N\left(0.5 \mathbf{1}_{R_{0}}, \boldsymbol{I}_{R_{0}}\right)+\left(1-\varrho_{0}\right) \delta_{\mathbf{0}}, \quad k \in\{1, \ldots, V\}
$$

where $\mathbf{1}_{R_{0}}$ is a vector of ones of length $R_{0}, \boldsymbol{I}_{R_{0}}$ is an identity matrix of size $R_{0} \times R_{0}$, and $\varrho_{0}$ is the probability that any $\boldsymbol{u}_{k, 0}$ is nonzero. Then, we define the $(k, l)$-th element

of $\boldsymbol{\Gamma}_{0,1}$ as $\frac{\mathbf{u}_{k, 0}^{\prime} \mathbf{u}_{l, 0}}{2}, k<l$ and as 0 if $k=l$. We refer to $\left(1-\varrho_{0}\right)$ as the node sparsity parameter in the context of the data generation mechanism.

On the other hand, the matrix $\boldsymbol{\vartheta}_{0}$ is constructed by randomly selecting a proportion $\varrho_{0,2}$ of entries to be non-zero. We refer to $\left(1-\varrho_{0,2}\right)$ as the residual edge sparsity. We consider three different strategies to generate the non-zero elements of $\boldsymbol{\vartheta}_{0}$. Under Strategy 1, the non-zero entries of $\boldsymbol{\vartheta}_{0}$ are simulated from a normal distribution with mean 1 and variance 0.1 . Under Strategy 2, they are simulated from normal distribution with mean 0.5 and variance 0.1 . Finally, under Strategy 3, the non-zero entries are fixed at 0.5 .

For each of Simulation 1 and Simulation 2 we consider four different experiments that combine different levels of node sparsity, edge sparsity, true and maximum latent dimensions $R_{0}$ and $R$, as well as different strategies for generating $\boldsymbol{\vartheta}_{0}$ (see Tables 1 and 2). In particular, note that the various experiments allow model mis-specification with unequal choices of $R$ and $R_{0}$. As competitors, we use generic variable selection and shrinkage methods that ignore the network structure in the predictor and treat edges as a long predictor vector to fit high-dimensional binary regression with a logit link function. In particular, we compare the performance of our model with a binary logistic regression with the Lasso penalty (Tibshirani, 1996) on the coefficients. With a slight abuse of terminology, we call it Lasso hereon. We also compare our approach to ordinary high-dimensional binary logistic regression with Bayesian Lasso (BLasso in short) prior (Park and Casella, 2008), and Bayesian Horseshoe (BHS in short) prior (Carvalho et al., 2010) on coefficients, which are popular Bayesian shrinkage regression methods. We used the glmnet package in R (Friedman et al., 2010) to implement the frequentist Lasso for binary logistic regression, while we have written our own codes for BLasso and BHS. A comparison with these methods will indicate any relative advantage of exploiting the structure of the network predictor. We have also compared our methods to a frequentist approach that develops network classification in the presence of a network predictor and a binary response (Relión et al., 2019). However, we find that all the competitors outperform this approach, and hence we have not included the results for the same.


Table 1: Table presents different cases for Simulation 1. The true dimension $R_{0}$ is the dimension of vector object $\boldsymbol{u}_{k, 0}$ using which data has been generated. The maximum dimension $R$ is the dimension of vector object $\boldsymbol{u}_{k}$ using which the model has been fitted. Node sparsity and residual edge sparsity are described in the text.

For all Bayesian models we generate 50,000 MCMC samples, out of which the first 30,000 are discarded as burn-ins. Convergence is assessed by comparing different simulated sequences of representative parameters starting at different initial values (Gelman


Table 2: Table presents different cases for Simulation 2. The true dimension $R_{0}$ is the dimension of vector object $\boldsymbol{u}_{k, 0}$ using which data has been generated. The maximum dimension $R$ is the dimension of vector object $\boldsymbol{u}_{k}$ using which the model has been fitted. Node sparsity and residual edge sparsity are described in the text.
et al., 2014b). We monitor the auto-correlation plots and effective sample sizes of the log likelihood function. In our analysis, we set $\nu=20$ and $a_{\Delta}=b_{\Delta}=1$. For BNLC, there are two additional hyper-parameters $\iota$ and $\zeta$, both of which are set to 1 . Note that the choice of $a_{\Delta}=b_{\Delta}=1$ ensures that the prior on models is such that we have a uniform distribution on the number of active nodes, and conditional on the size of the model, a uniform distribution on all possible models of that size. The choice of $\nu=20$ ensures that the prior distribution on $\boldsymbol{M}$ is concentrated around a scaled identity matrix. Since the model is invariant to rotations of the latent positions, we want the prior on $\boldsymbol{u}_{k}$ 's to also be invariant under rotation. This requires that we center $\boldsymbol{M}$ around a matrix that is proportional to the identity. Our choice of $\iota$ and $\zeta$ set the prior mean of $s_{k, l}$ at 0.5 , which is the suggested prior mean for the local parameters proposed in Park and Casella (2008). Sensitivity to the choice of hyper-parameters is discussed in Section 5.6 for simulation studies and in Section 6.2 for the real data analysis.

# 5.2 Classification Accuracy and Estimation of Edge Coefficients 

To evaluate the out-of-sample predictive performance of the different models, Figure 1 presents the area under the receiver operating characteristic curves (AUCs) obtained by using different classification thresholds $t_{c}$ (recall the discussion in Section 4). Under Simulation 1, BNLC consistently outperforms all other models, with BNHC a very close second. The performance is quite good for models, with AUCs above 0.9 in all four cases. On the other hand, under Simulation 2 the order appears to switch and BNHC seems to be the best performing model, closely followed by BNLC. AUC values are also high in this case, but uniformly lower than in Simulation 1. This suggests that the presence of structure in the network predictor can affect the accuracy of the classification. Among the methods that ignore the network structure associated with the predictor, BLasso tends to have the worse performance, particularly under Simulation 2.

In addition to classification rates, we also compute mean squared errors (MSE) associated with the point estimates of the edge coefficients under each model (see Tables 3 and 4). For the Bayesian approaches, point estimates are computed using the posterior means of the edge coefficients. In all cases, BNLC yields point estimates with the lowest MSE. BNHC is the second best-performing method under this metric in almost all cases, closely followed by BLasso.

![img-0.jpeg](img-0.jpeg)

Figure 1: Figure shows classification performance in the form of Area under Curve (AUC) of Receiver Operating Characteristic (ROC) curve for all cases in Simulations 1 and 2 .


Table 3: Performance of BNLC and BNHC vis-a-vis competitors for cases in Simulation 1. Parametric inference in terms of point estimation of edge coefficients has been captured through the Mean Squared Error (MSE). The minimum MSE among competitors for any case is made bold.


Table 4: Performance of BNLC and BNHC vis-a-vis competitors for cases in Simulation 2. Parametric inference in terms of point estimation of edge coefficients has been captured through the Mean Squared Error (MSE). The minimum MSE among competitors for any case is made bold.

# 5.3 Estimation of the Effective Dimensionality 

Figures 2 and 3 present posterior distribution of $R_{\text {eff }}$, the effective dimensionality of the latent space, for BNLC and BNHC in Simulations 1 and 2, respectively. In all eight experiments, the mode of the posterior distribution corresponds to the true dimension of the latent space. Furthermore, compared to BNLC, note that the posterior distribution of $R_{\text {eff }}$ under BNHC tends to concentrate more sharply around the true value.

### 5.4 Identification of Influential Nodes

Figures 4 and 5 show the posterior probability of the $k$-th node being detected as influential, i.e., $\operatorname{Pr}\left(\xi_{k}=1 \mid\right.$ Data $)$, under BNLC and BNHC for each node and each case within Simulations 1 and 2, respectively. Generally speaking, in Simulation 1, BNLC tends to outperform BNHC, with the two methods having comparable true positive rates, but BNHC having a much higher false positive rate (at the standard threshold $t_{n}=0.5)$. BNHC behaves particularly poorly in case 2 , where it identifies 4 false positive nodes and one false negative node (against a perfect separation for BNLC), and in case 3 , where it identifies all but one node as influential.

The pattern is similar for Simulation 2, with both methods having comparable true positive rates but with BNHC having consistently higher false positive rates and again performing particularly poorly in case 3 . However, there are also some notable differences. For example, the true positive rates tend to be lower in Simulation 2 than in Simulation 1 for both methods. Similarly, the false positive rate for BNHC seems to be lower in Simulation 2 than in Simulation 1. Finally, in Simulation 2 both models struggle with case 3 (which was not the case in Simulation 1), although they do it in slightly different ways. BNLC shows relatively high rates for both false positives and false negatives ( $16 \%$ in both cases), while BNHC shows a very high false positive rate $(32 \%)$ but a low false negative rate $(4 \%)$.

### 5.5 Identification of Influential Edges

We use the algorithm described in Section 4 of the Supplementary Material (Guha and Rodriguez, 2023) to estimate (local) false discovery rates (FDR) for each of the edge coefficients under the various shrinkage priors. These, in turn, can be used to identify influential edges in the network while controlling for the overall FDR of the procedure. In this section, we attempt to control FDR so that it does not exceed 0.05 .

Table 5 shows the realized FDR after applying the procedure to each simulated dataset, as well as true positive rates (TPR) and false positive rates (FPR). The best performing prior is BNLC, where our procedure seems to be well calibrated (realized FDR rates seem to be roughly consistent with the desired nominal rate of 0.05 ), FPRs tend to be quite low, and TPRs range between 0.46 and 0.72 . On the other hand, BNHC tends to yield higher TPRs (ranging between 0.59 and 0.86 ) in most cases, but at the cost of uniformly higher FPRs, which in turn lead to FDR above the nominal value. The other three variable selection procedures (Lasso, Bayesian Lasso and Horseshoe)

![img-1.jpeg](img-1.jpeg)

Figure 2: Plots showing posterior probability distribution of effective dimensionality for BNLC and BNHC models in all 4 cases in Simulation 1. Filled bullets indicate the true value of effective dimensionality.

![img-2.jpeg](img-2.jpeg)

Figure 3: Plots showing posterior probability distribution of effective dimensionality for BNLC and BNHC models in all 4 cases in Simulation 2. Filled bullets indicate the true value of effective dimensionality.

![img-3.jpeg](img-3.jpeg)

Figure 4: Simulation 1: Clear background denotes uninfluential and dark background denotes influential nodes in the truth for BNLC and BNHC models. Note that there are 25 rows (corresponding to 25 nodes) and 4 columns corresponding to 4 different cases in Simulation 1. The model-detected posterior probability of being influential has been super-imposed onto the corresponding node.


Table 5: True Positive Rates (TPR), False Positive Rates (FPR) and Realized False Discovery Rate (FDR) for edges for cases in Simulation 1 and Simulation 2.
that ignore the network structure in the predictor perform the worst, as they yield lower FPRs and higher FPRs and FDRs.

# 5.6 Sensitivity to the Choice of Hyperparameters 

This section assesses the sensitivity of the inferences from BNLC and BNHC to the choice of hyperparameters. In our sensitivity analysis for BNLC, we consider five scenarios that correspond to alternative values for various subsets of hyperparameters: (i) $a_{\Delta}=1, b_{\Delta}=9$; (ii) $\nu=20, \frac{\zeta}{\gamma}=5$ (iii) $\nu=50, \frac{\zeta}{\gamma}=5$ (iv) $\nu=20, \frac{\zeta}{\gamma}=0.2(\mathrm{v})$ $\nu=50, \frac{\zeta}{\gamma}=0.2$. Combination (i) ensures small prior mean for $\xi_{k}$ 's, while combinations (ii)-(v) allow a range of prior means for $\theta$ and $\boldsymbol{M}$. On the other hand, for BNHC we employ three different alternative combinations of hyperparameters: (i) $a_{\Delta}=1, b_{\Delta}=9$ (ii) $\nu=10$ (iii) $\nu=50$. To keep the discussion concise, we only present here results for

![img-4.jpeg](img-4.jpeg)

Figure 5: Simulation 2: Clear background denotes uninfluential and dark background denotes influential nodes in the truth for BNLC and BNHC models. Note that there are 25 rows (corresponding to 25 nodes) and 4 columns corresponding to 4 different cases in Simulation 2. The model-detected posterior probability of being influential has been super-imposed onto the corresponding node.


Table 6: Mean Squared Error (MSE) of estimating the network coefficient in BNLC and BNHC for different combinations of hyper-parameters.

Case 4 in Simulation 1, but the outcomes are similar for all other experiments.
Table 6 presents the MSE associated with the network coefficients under the different priors. There seems to be a moderate effect of the priors on the MSE, particularly for BNLC. In particular, prior (ii) under BNLC seems to perform quite poorly when compared with the rest. Figure 6 shows the posterior probabilities of a node being identified as influential under each prior. Again, there seems to be a moderate impact of the prior on the estimated posterior probabilities. Indeed, for most nodes, $\operatorname{Pr}\left(\xi_{k}=\right.$ $1 \mid$ Data) is quite comparable across all priors, and the nodes identified as influential by each model (at the standard threshold $t_{n}=0.5$ ) are almost identical across all priors. However, there are some notable exceptions. For example, $\operatorname{Pr}\left(\xi_{4}=1 \mid\right.$ Data $)$ under BNHC is estimated to be 0 under prior (i), but it is estimated to be 1 under the original specification as well as the other two alternatives. Finally, Table 7 offers TPR and FPR values corresponding to the identification of influential edges for BNLC and BNHC under various combinations of hyper-parameters. For BNLC, all alternative prior specifications lead to higher TPRs, at the cost of higher FPRs. In the case BNHC, the

![img-5.jpeg](img-5.jpeg)

Figure 6: Figure shows $P\left(\xi_{k}=1\right|$ Data $)$ for BNLC and BNHC under different hyperparameter combinations in the simulated data for Case 4 (Simulation 1). The first column in each matrix shows the values corresponding to the original prior specification.


Table 7: True Positive Rates (TPR) and False Positive Rates (FPR) of identifying influential edges in BNLC and BNHC for different combinations of hyper-parameters.
results are mixed, with prior (i) performing quite poorly (higher FPR and lower TPR than the original prior), and priors (ii) and (iii) exhibiting the same trade offs (higher TPR at the cost of also higher FDR) as the various alternative priors for BNLC.

Overall, we note that the prior can have a moderate impact on the inference. This should not be surprising. Since this is a high-dimensional regression paradigm with number of parameters far exceeding the sample size, one expects the prior hyper-parameters to have some effect on the inference.

# 6 Brain Connectome Application 

In this section, we apply the BNLC and BNHC priors to study the relationship between a subject's brain connectome and its intelligence based on a sample of $n=114$ subjects, using the MRN (Mind Research Network) dataset collected at the University of New Mexico, and available at https://neurodata.io. This dataset contains information on the full scale intelligence quotient (FSIQ) for multiple individuals. Full scale intelligence

quotient (FSIQ) is a measure of an individual's complete cognitive capacity, and is designed to provide a measure of an individual's overall level of general cognitive and intellectual functioning. FSIQ is derived by administering selected sub-tests from the Wechsler Intelligence Scales (WIS) that measure acquired knowledge, verbal reasoning, attention to verbal material, fluid reasoning, spatial processing, attention to detail and visual-motor integration (Caplan et al., 2011). A substantial body of literature has suggested that there is an IQ threshold (usually described as an IQ of approximately 120 points) that may be characterized as superior reasoning ability (Brown et al., 2009; Carson et al., 2003). Following this literature, we have converted the FSIQ scores into a binary response variable $y$, which takes value 0 if FSIQ is less or equal to 120 , and takes value 1 if FSIQ is greater than 120. Thus, we classify the subjects in our study as belonging to the low $I Q$ group if $y=0$, and the high $I Q$ group if $y=1$.

Along with FSIQ measurements, brain connectome information was gathered using weighted diffusion tensor imaging (DTI). DTI is a brain imaging technique that enables measurement of the restricted diffusion of water in tissue in order to produce neural tract images. The brain imaging data we use has been pre-processed using the NeuroData MRI to Graphs (NDMG) pipeline (Kiar et al., 2016, 2017a,b). For the purpose of our analysis, the human brain is divided according to the Desikan atlas (Desikan et al., 2006), which identifies 34 cortical regions of interest (ROIs) both in the left and right hemispheres of the human brain, implying 68 cortical ROIs in all. This results in a brain network of a $68 \times 68$ matrix for each individual. Our scientific goals in this setting include identification of brain regions or network nodes significantly related to FSIQ and classification of a subject into the low IQ or high IQ group based on his/her brain connectome information.

The analyses we present in this section use the same hyperparameters as our simulation studies. BNLC and BNHC are both fitted with $R=4$, which is found to be sufficient for this study (see sensitivity analysis in Section 6.2). The MCMC chains are run for 50,000 iterations, with the first 30,000 iterations discarded as burn-in. As before, convergence is assessed by comparing different simulated sequences of representative parameters started at different initial values (Gelman et al., 2014a). The posterior mean for the effective dimensionality of the model is 2.17 for BNLC and 2 for BNHC, and the posterior probabilities associated with 4 dimensions for BNLC and BNHC are given by 0.0082 and 0.0000 , respectively.

# 6.1 Findings from the Brain Connectome Application 

We first focus on identifying ROIs that are influential on FSIQ. At a threshold of $t_{n}=$ 0.5 , BNLC identifies 38 influential ROIs, 20 in the left and 18 in the right hemisphere. On the other hand, using the same threshold, BNHC identifies 48 influential ROIs, 26 in the left hemisphere and the rest in the right hemisphere. Table 8 lists the 29 ROIs that are identified as influential by both methods. A large number of these are part of the frontal lobes in both the hemispheres. Numerous studies have linked the frontal region to an individual's intelligence and cognitive functions (e.g., see Yoon et al., 2017; Stuss et al., 1985; Razumnikova, 2007; Miller and Milner, 1985; Kolb and Milner, 1981). The methods also agree in finding a significant association between FSIQ and ROIs in


Table 8: Nodes identified as influential by both BNLC and BNHC.
the left inferior parietal lobule, the left precuneus and the supramarginal gyri in both the hemispheres, and in the parietal lobe. These regions have also been found to be significantly related to FSIQ in Yoon et al. (2017).

Figure 7(a) shows the values of $\operatorname{Pr}\left(\xi_{k} \mid\right.$ Data $)$ under BNHC for the nine nodes that were identified as influential by BNLC but not by BNHC. Note that most of these probabilities seem to be much lower than 0.5 , indicating that BNHC is relatively confident about excluding these nodes. Similarly, Figure 7(b) shows the node inclusion probabilities under BNLC for those nodes that BNHC identified as influential but BNLC did not. In contrast to Figure 7(a), in this case the probabilities tend to be close to 0.5 , suggesting that BNLC is not very confident about excluding these nodes. These observations, together with the fact that BNHC tends to include more nodes overall, matches what we saw in our simulation studies and suggests that BNLC is more conservative in identifying influential nodes.

Figure 8 shows the significant edges identified by the BNLC and BNHC models. In this part of the analysis, we only consider edges that connect nodes that were identified as being influential by each prior. BNLC and BNHC identify 142 and 291 edges as being influential, respectively. For the most part, these significant edges are spread across the various nodes. However, we can clearly see that some nodes have no significant edges involving them. Under BNLC (which, as we discussed before, seems to be more conservative) there are only three such nodes (the frontal and temporal poles in the left hemisphere, and the temporal pole in the right hemisphere). However, under BNHC, there are 14 nodes with no significant links (including the middle temporal and parsopercularis regions of the left hemisphere and the precental and precuneus regions of the right hemisphere, among others). While this might be somewhat surprising at first sight, it is not a mistake. Recall that the edges highlighted in the plots were identified by controlling FDR, so they should be interpreted as the set of edges that are most likely to be influential, rather than as a comprehensive list. Interestingly, the sets of nodes with at least one significant edge are very similar in the two models, and both

![img-6.jpeg](img-6.jpeg)

Figure 7: Posterior probabilities of nodes selected as influential by one method, but not by another, of being active.
contain the set of 29 common influential nodes that we listed in Table 8.
Finally, in order to examine the predictive ability of the Bayesian network classification model, we carry out a 10 -fold cross validation exercise and report in Table 9 the (average) AUC for BNLC and BNHC, along with all competing methods. Overall, all AUC values are relatively low. BNLC seems to perform best, followed by BNHC and Lasso. The other two approaches (BLasso and BHS) perform quite poorly in this setting, yielding AUC values below 0.5 .


Table 9: Average AUC values for a 10 -fold cross validation exercise involving the competing approaches.

# 6.2 Sensitivity to the Choice of Hyperparameters 

In this section, we carry out a sensitivity analysis using the same alternative set of hyperparameters introduced in Section 5.6. First, we report in Table 10 the number of nodes identified as influential under each alternative hyperparameter setting, as well as the number of these nodes that intersect with those identified in the original analysis. While there is some variation in the number and exact identity of influential nodes, the different hyperparameter settings largely seem to agree with each other ( 31 nodes are common to all hyperparameter settings under BNLC, and 40 are common to all under

![img-7.jpeg](img-7.jpeg)
(a) BNLC
![img-8.jpeg](img-8.jpeg)
(b) BNHC

Figure 8: Plot showing whether an edge connecting two influential nodes is influential or not. Note that the map is a $M \times M$ symmetric matrix, where $M$ denotes the number of influential nodes, and each cell denotes an edge connecting the corresponding pair of nodes. The axis labels are the abbreviated names of the influential ROIs in the left (starting with 'lh -') and the right (starting with 'rh -') hemispheres of the brain. Full names of the ROIs can be obtained from the widely available Desikan brain atlas. A white cell represents an influential edge, while a red cell represents a non-influential edge.

BNHC). Next, we identify significant edges that connect nodes identified as influential by all sets of hyperparameters under each model (see Table 11). As before, the overlap is substantial. Finally, we investigate the sensitivity of the models to the choice of $R$. To accomplish this, we rerun each of our two models with $R=8$ and $R=10$, and report the posterior means of the effective dimensionality, along with AUC (see Table 12). While we see a small increase in $R_{\text {eff }}$ as $R$ increases (particularly for BNHC), the change has almost no effect on the AUC.


Table 10: Number of nodes identified as influential for all combinations are presented. The table also presents the number of intersections of influential nodes between different combinations and the original analysis.


Table 11: Number of edges identified as influential for all combinations are presented. The table also presents the number of intersections of influential nodes between different combinations and the original analysis.


Table 12: AUC and posterior mean of effective dimensionality for BNLC and BNHC under different choices of $R$.

# 7 Conclusion 

We have developed a binary Bayesian network regression model that enables the classification of multiple networks with labeled nodes, identifies influential network nodes and edges, and predicts the class in which a newly observed network belongs. Our contribution lies in carefully constructing a class of network global-local shrinkage priors on the network predictor coefficient while recognizing the latent network structure in the predictor variable. Our simulation studies show competitive performance in terms of inference and classification. On the other hand, the results we obtain in our application to brain connectome data both corroborate results that had already been described in the literature and suggest new relationships between brain ROIs and FSIQ scores.

There are several natural directions for future research. A major contribution of the proposed framework is a theoretical analysis of the asymptotic properties of the model under a condition in which the size of the predictor matrix increases with the sample size at a superlinear rate. Developing a similar theory for the Network Horseshoe prior proposed in this article faces more challenges due to the more complex prior structure in the parameters. We plan to tackle this problem as part of future work. It is also important to note that the theoretical results in this article hinge upon the assumption that the rank of the true network coefficient is known. As part of future work, we will investigate the model theoretically when the fitted network coefficient is low-rank but the true network coefficient is full rank. We also emphasize that Theorem 3.1 guarantees asymptotically consistent classification, but provides no consistency guarantee for the regression coefficients or their effective dimension. While Wei and Ghosal (2020) have established such a result for ordinary high-dimensional logistic regression, a similar result would be substantially more challenging to establish in our framework. We will consider this as a part of our future theoretical explorations. Finally, this article illustrates our approach on a dataset where a continuous outcome FSIQ is discretized to construct a discrete response variable. We plan to do future work emphasizing efficacy of our approach on a real data application with a network predictor and a binary outcome.

# Supplementary Material 

Supplementary Material: High-Dimensional Bayesian Network Classification with Network Global-Local Shrinkage Priors (DOI: 10.1214/23-BA1378SUPP). The supplementary material has four sections. Section 1 discusses the proof of Theorem 3.1. Section 2 discusses the MCMC algorithm for the Network Lasso Shrinkage prior. Section 3 discusses the MCMC algorithm for the Network Horsheshoe Shrinkage prior. Section 4 discusses the edge selection procedure.
