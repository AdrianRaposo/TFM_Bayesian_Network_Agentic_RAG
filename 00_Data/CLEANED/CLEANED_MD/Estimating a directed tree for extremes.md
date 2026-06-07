# Estimating a Directed Tree for Extremes 

Ngoc Mai Tran $\dagger$<br>Department of Mathematics, University of Texas at Austin, Speedway 2515 Stop C1200, Austin TX 78712, USA, email: ntran@math.utexas.edu<br>Johannes Buck $\ddagger$ and Claudia Klüppelberg§<br>Department of Mathematics, Technical University of Munich, 85748 Garching, Boltzmannstr. 3, Germany, emails: j.buck@tum.de, cklu@cit.tum.de


#### Abstract

Summary. We propose a new method to estimate a root-directed spanning tree from extreme data. A prominent example is a river network, to be discovered from extreme flow measured at a set of stations. Our new algorithm utilizes qualitative aspects of a max-linear Bayesian network, which has been designed for modelling causality in extremes. The algorithm estimates bivariate scores and returns a root-directed spanning tree. It performs extremely well on benchmark data and new data. We prove that the new estimator is consistent under a max-linear Bayesian network model with noise. We also assess its strengths and limitations in a small simulation study.


Keywords: Bayesian network, causal inference, directed acyclic graph, extreme value analysis, graphical model, max-linear model.

## 1. Introduction

Graphical models can represent multivariate distributions in an intuitive way and, hence, facilitate statistical analyses of high-dimensional data. Traditionally, such models are linear and distributions are Gaussian; see e.g. Bühlmann and Geer (2011); Drton and Maathuis (2017); Lauritzen (1996); Maathuis et al. (2019). In recent years, extensions to non-Gaussian linear models have been proposed with statistical methods focusing on second order properties of their distributions, which estimate the graph structure for observations in the center of the distribution.

Gaussian models and correlations are inappropriate for assessing high risks, where the extreme observations contain the relevant information. For such problems extreme value distributions provide natural models. Whereas Gaussian distributions arise as limit distributions of normalized sums, extreme value distributions arise as limit distributions of normalized maxima, thus, being natural candidates for modelling high risks. Gaussian distributions are sum-stable (closed with respect to sums) and extreme value distributions are max-stable (closed with respect to maxima). This duality and more relations between sums and maxima are presented for dimension $d=1$ in Embrechts et al. (1997).

[^0]
[^0]:    $\dagger$ Supported by NSF Grant DMS-2113468 and NSF IFML 2019844 Award.
    $\ddagger$ Supported by the Hanns Seidel Foundation
    §Corresponding author

![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of a root-directed spanning tree with root 1. It is a simple directed acyclic graph, where each node has exactly one child, except the root, which has none. Moreover, there is exactly one path from every node to the root.

For dimension $d \geq 2$ max-stable distributions also arise as limits of componentwise normalized maxima of independent copies of a random vector $X$, and the dependence structure between components of the limit vector has been extensively studied and applied in multivariate risk problems. Textbook treatments can be found in Beirlant et al. (2004); Coles (2001); de Haan and Ferreira (2007); Resnick (1987, 2007). A very readable review paper is Davison and Huser (2015). For statistical applications, correlations or other bivariate measures of dependence in the center of the distribution are replaced by extreme dependence measures (Coles et al. (1999); Engelke and Volgushev (2022); Larsson and Resnick (2012); Sibuya (1960)).

This paper focuses on causal interpretation and is motivated by the fact that rare events like environmental or financial risks are often cascading through a network. For instance, pollutants can propagate through an unseen underground waterway, causing extreme measurements at multiple locations (Leigh et al. (2019)), or credit markets can fail due to some endogenous systemic risk propagation (Rochet and Tirole (1996)).

Graphical models can allow for causal interpretation, however, it is not immediately obvious how to extend the past decades of work on causal inference (Bollen (1989); Drton and Maathuis (2017); Lauritzen (1996); Maathuis et al. (2019); Pearl (2009); Spirtes et al. (2000)) for Gaussian and discrete distributions to an extreme value setting.

We approach this problem from two directions.
Firstly, we follow the general idea (see e.g. Pearl (2009)) that causality is often provided through a recursive system on a directed acyclic graph. Prominent examples in the literature are linear recursive systems, where each node represents a random variable defined as a weighted sum of its parent variables and an independent random variable. But instead of such classical linear causal graphical models or linear Bayesian networks, we use max-linear causal graphical models or max-linear Bayesian networks. Introduced in Gissibl and Klüppelberg (2018), they are defined via max-linear recursive structural equation models on a directed acyclic graph.

In a max-linear Bayesian network, each node represents a positive random variable defined as a weighted maximum of its parent variables and an independent random variable, called innovation. Although motivated by extreme value theory, the multivariate distribution of a max-linear vector is not restricted to an extreme value distribution; the emphasis of the model is on its structure given by a directed acyclic graph. We relax the strict max-linear Bayesian network model by allowing for an independent noise variable. Nonparametric statistical inference aims at identifying the directed graphical structure regardless of the node distributions under weak conditions on the noise distributions.

Secondly, we propose a new algorithm, QTree, motivated by qualitative aspects of a max-linear Bayesian network to estimate a root-directed spanning tree (see Figure 1)

as a simple directed acyclic graph. QTree uses pairwise dependence, handles missing data, and has an automated parameter tuning procedure. Here we use the fact that the non-noisy model has a left-sided atom for the distribution of a ratio of marginal random variables, when there is a directed edge between the nodes. We also show that, under a max-linear Bayesian network model with noise and natural distributional assumptions, the QTree algorithm returns asymptotically almost surely the correct tree.

Max-linear Bayesian networks have recently emerged as suitable directed graphical models for causality in extremes (Améndola et al. (2022); Buck and Klüppelberg (2021); Gissibl (2018); Gissibl and Klüppelberg (2018)), however, existing methods for learning them aim to learn the model parameters and, thus, are highly sensitive to model misspecifications; see Buck and Klüppelberg (2021); Gissibl (2018); Gissibl et al. (2021); Gissibl et al. (2018); Klüppelberg and Krali (2021); Klüppelberg and Lauritzen (2020).

Motivated by extreme value theory, it is not surprising that max-linear Bayesian networks have been mostly investigated for heavy-tailed innovations: Einmahl et al. (2018, Section 3.3) consider tail dependence functions for i.i.d. Fréchet innovations. Gissibl et al. (2018) investigate tail dependence for i.i.d. regularly varying innovations, and Klüppelberg and Krali (2021) the scaling properties of the same model. Asenova et al. (2021) and Segers (2020) investigate regularly varying Markov trees, and more recently, Asenova and Segers (2024) investigate a new max-linear graphical model on trees of transitive turnaments.

Graphical models for extremes have also been proposed in Engelke and Hitz (2020) based on a different concept. They define a new extreme conditional dependence concept for multivariate Pareto distributions (which have Lebesgue densities) and use this concept to define extreme undirected graphical models similarly to the classical concept. The multivariate distribution determines the model and has in general to be specified for statistical inference. Here the multivariate Hüsler-Reiss distribution plays a prominent role; see Asenova et al. (2021); Asenova and Segers (2024); Engelke and Volgushev (2022); Engelke et al. (2022); Hu et al. (2022); Rötter et al. (2023).

# 1.1. The Extremal River Problem 

The relevance of extremal graphical models for multivariate distributions has been validated on several data sets, prominently on the Upper Danube river network. The goal is to recover a river network from only extreme flow measured at a set $V$ of stations, without any information on the stations' location. We refer to it as the Extremal River Problem. Here, the true river network is known and serves as the 'gold standard', allowing one to verify the performance of a proposed estimator. Success in solving the Extreme River Problem can translate to new solutions to the contaminant tracing challenge in hydrology (Leigh et al. (2019); McGrane (2016); Rodriguez-Perez et al. (2020); Ver Hoef and Peterson (2010); Ver Hoef et al. (2006); Wolf et al. (2012)). There, one needs an inexpensive method to trace pollutants or chemical constituents transported by a complex and unknown underground waterway that is prohibitive to model or survey with traditional fluid mechanics methods (Anderson et al. (2015)). Recent advances point towards an imminent data explosion (Bartos et al. (2018); Mao et al. (2019)), where pollutants exceeding certain thresholds can be detected via a sensor network. Thus, contaminant

tracing with sensors data is a version of the Extremal River Problem without the gold standard, where the network is truly unknown.

A solution to the Extremal River Problem requires an algorithm to recover the true river network using test data given by river discharges, the volume of water flowing through a river channel, measured at any given point in cubic metres or cubic feet per second. The Extremal River Problem for the Upper Danube river network with measurements collected at $d=31$ stations has proven to be challenging and very stimulating for extreme value theory, with each paper taking a different technique. The data have been preprocessed in Asadi et al. (2015) and are available in the R package graphicalExtremes (Engelke et al. (2019)).

The preprocessed data have been analysed in a number of publications with focus on modelling extreme dependence: flow- and spatial dependence (Asadi et al. (2015)) and undirected graphical models for extremes (Engelke and Hitz (2020); Engelke et al. (2022); Hu et al. (2022); Gong et al. (2022); Rötter et al. (2023)). In a first paper, Engelke and Hitz (2020) returned a highly accurate but undirected graph, followed by publications using new models and applying different methods for reconstructing the undirected graph.

Our focus is on causality in extremes, modelled by the edges of a root-directed tree: a large value at node $j$ causes a large value at node $i$, whenever there is an edge from $j$ to $i$. For a river network the causal structure in the extremes is the same as for average values and in this case the tree can be learned with methods for extremes and averages. However, it may well happen that causality is stronger in the extremes than in average values. Indeed, in Tran (2022), Section 2.1 it is shown that for the Upper Danube data also a naive algorithm based on the pairwise correlation matrix as score matrix performs well, whereas for Lower Colorado data it returns a less precise tree. So this is an example, where the extremes contain more causal information than the average observations.

Causal dependence models for extremes have also been considered using expected quantile scores (Mhalla et al. (2020)) and causal dependence coefficients (Gnecco et al. (2021)). Gnecco et al. (2021) correctly recovered the causal order of 12 nodes out of 31, but did not learn the entire river network, while Mhalla et al. (2020) focused on flowconnections and did well at detecting nodes connected by a directed path; see Figure 7 in Mhalla et al. (2020). These two publications have slightly different notions of causality. We give more details and compare our method with theirs in Section 4.

# 1.2. Main contributions and structure of the paper 

Below, we explain the novel aspects of our paper, summarize the organisation of our paper, and define the standard metrics to assess the quality of an estimated graph.

Most prominently, we suggest a new algorithm QTree to recover causality in extremes, where causality is modelled by the edges of a root-directed tree. This algorithm relies on qualitative aspects of a max-linear Bayesian network model and is as such a structural model, which does not require to specify a distribution family. Moreover, no normalization of the data to standard Fréchet or Gumbel distribution is needed.

The QTree Algorithm 1 estimates a score matrix $W$, giving a score for each potential edge independently, and applies a standard algorithm to output a root-directed spanning tree of optimum score. Algorithm 1 runs in time $O\left(n|V|^{2}\right)$, where $n$ is the number of

observations and $|V|$ is the number of nodes. Moreover, it maximizes the information available from missing data, since at each step it only utilizes the data projected onto two coordinates. QTree needs sufficiently many extreme observations and relies on the signal to have heavier tail than the noise.

We improve this simple algorithm by an optimization procedure to find the best model parameters using a grid search in combination with a stabilizing subsampling procedure that is based on bootstrap aggregation. This QTree Algorithm 2 is very flexible, has at most two tuning parameters, and proves to be very efficient.

Besides the Upper Danube data set, which serves as benchmark set for comparison to other methods, we analyse three new data sets from the Lower Colorado river network in Texas. We also show by a small simulation study that QTree is robust with respect to different dependence structures (given by edge-weights) and different node distributions entailed from different innovations distributions.

QTree is implemented as a plug-and-play package in Python (Tran (2021)) at https://github.com/princengoc/qtree
which includes all data and codes to produce the results and figures in this paper.
Beyond hydrology, QTree can be applied to cause and effect detection in every high risk problem assuming that the network is a root-directed tree. QTree can, however, also solve a slightly more general problem. Assume that the tree structure is only in the extremes, whereas "average" data follow a different model. For instance, it can happen that only data from certain nodes follow a heavy-tailed distribution (able to model extreme events, while other nodes are negligible from an extreme value point of view; see e.g. de Haan and Ferreira (2007) or Resnick (1987, 2007)). Then it may be possible that causality in the extremes can be modelled by a tree on a subset of nodes.

Assuming that the data come from a noisy max-linear Bayesian network, under distributional assumptions with appropriate signal-to-noise ratio, we prove in Theorem 1 that the tree output by QTree is strongly consistent as the sample size tends to infinity. This proof is based on a new variational argument to account for noise in the data.

Our paper is organized as follows. We introduce QTree (Algorithm 1) and auto-tuned QTree (Algorithm 2) in Section 2 and give some intuition supported by preliminary simulation results. In Section 3, we present the data sets, discuss their specific challenges and describe the data preprocessing steps. In Section 4, we present the estimation results of QTree and analyse the performance of the automated parameter selection. Here we also compare different algorithms in the literature with ours. In Section 5, we test the limits of QTree by a small simulation study. Section 6 concludes with a summary. The Supplementary Material includes the proof of the Consistency Theorem (Theorem 1) in its Section S3.

Notations. Estimators are compared based on standard performance metrics in causal inference (Zheng et al. (2018)): normalized structural Hamming distance (nSHD), false dicovery rate (FDR), false positive rate (FPR), and true positive rate (TPR). We recall their definitions here: Let $\mathcal{G}$ be the true graph on a node set $V$ and $\hat{\mathcal{G}}$ an estimated graph. The structural Hamming distance $\operatorname{SHD}(\mathcal{G}, \hat{\mathcal{G}})$ between $\mathcal{G}$ and $\hat{\mathcal{G}}$ is the minimum number of edge additions, deletions and reversals to obtain $\mathcal{G}$ from $\hat{\mathcal{G}}$. Denote $E(\mathcal{G})$ and $E(\hat{\mathcal{G}})$ the set of edges in $\mathcal{G}$ and $\hat{\mathcal{G}}$, respectively. Note that $|E(\hat{\mathcal{G}}) \backslash E(\mathcal{G})|$ is the number of edges in $\hat{\mathcal{G}}$ that are not in $\mathcal{G}$, while $|E(\hat{\mathcal{G}}) \cap E(\mathcal{G})|$ is the number of correctly estimated

edges. We then have

$$
\begin{aligned}
& \operatorname{nSHD}(\hat{\mathcal{G}}, \mathcal{G}):=\frac{\operatorname{SHD}(\hat{\mathcal{G}}, \mathcal{G})}{|E(\hat{\mathcal{G}})|+|E(\mathcal{G})|}, \quad \operatorname{FDR}(\hat{\mathcal{G}}, \mathcal{G}):=\frac{|E(\hat{\mathcal{G}}) \backslash E(\mathcal{G})|}{|E(\hat{\mathcal{G}})|}, \\
& \operatorname{FPR}(\hat{\mathcal{G}}, \mathcal{G}):=\frac{|E(\hat{\mathcal{G}}) \backslash E(\mathcal{G})|}{|V| \times(|V|-1)-|E(\mathcal{G})|}, \quad \operatorname{TPR}(\hat{\mathcal{G}}, \mathcal{G}):=\frac{|E(\hat{\mathcal{G}}) \cap E(\mathcal{G})|}{|E(\mathcal{G})|}
\end{aligned}
$$

All metrics lie in $[0,1]$ and the performance of an algorithm is better the smaller the first three metrics are and the larger TPR is. We shall use this throughout Section 4.

# 2. The algorithm 

### 2.1. The data generation model

Throughout we assume data $X \in \mathbb{R}^{V}$ with causal dependence structure modelled by a root-directed spanning tree $\mathcal{T}$ on $V$ nodes. In such a tree, each node $i \in V$ except the root $r$ has exactly one child, the root $r$ has none, and there is a path from every node $i \neq r$ to $r$. An example of such a tree is given in Figure 1. We solve the Extremal River Problem by estimating $\mathcal{T}$ from extreme river discharges $X_{i}$ at nodes $i \in V$. Here a river discharge is the volume of water flowing through a river channel, measured at any given point in cubic metres or cubic feet per second.

Extreme value models have a long tradition in hydrology as the ample references in the Introduction show. River networks are prominent examples for root-directed trees. As the water direction determines the flow, the root-directed tree is known and an ideal test case for a new extreme value model and a new algorithm.

Our starting point is the max-linear Bayesian network (Gissibl and Klüppelberg (2018)), a model for risk propagation in a directed acyclic graph. When the graph is a tree $\mathcal{T}$, then the model is defined as

$$
X_{i}=\bigvee_{j: j \rightarrow i \in \mathcal{T}} c_{i j} X_{j} \vee Z_{i}, \quad c_{i j}, Z_{i}>0, \quad i \in V
$$

The $Z_{i}$, called innovations, are independent with support $\mathbb{R}_{\geq 0}$ and have atom-free distributions. Each edge $j \rightarrow i$ in $\mathcal{T}$ has a weight $c_{i j}>0$, interpreted as some measure of the flow rate from $j$ to $i$, and an extreme discharge at $i$ is either the result of an unknown external input $Z_{i}$ (e.g. heavy rainfall), or it is the maximum of weighted discharges coming by recursion from an ancestral node of $i$.

For numerical stability, we prefer to work with the logarithm of the data. To avoid new symbols, we keep the same notation, so the max-linear Bayesian tree becomes

$$
X_{i}=\bigvee_{j: j \rightarrow i \in \mathcal{T}}\left(c_{i j}+X_{j}\right) \vee Z_{i}, \quad c_{i j}, Z_{i} \in \mathbb{R}, \quad i \in V
$$

Our approach to the Extremal River Problem is to assume that the observations follow approximately a max-linear model. This means that we assume that data is corrupted with independent noise in each coordinate such that the problem we want to solve in this paper is the following.

Extremal River Problem. Assume i.i.d. observations

$$
\mathcal{X}=\left\{x^{1}+\varepsilon^{1}, \ldots, x^{n}+\varepsilon^{n}\right\} \in \mathbb{R}^{V}
$$

where for $k=1, \ldots, n$, the components of $x^{k}$ are generated via (3) and the components of the noise vectors $\varepsilon^{k}$ are independent in $\mathbb{R}$, find $\mathcal{T}$.
We stress that the root-directed tree assumption is different from the usual tree in Bayesian networks, where each child has at most one parent. Learning the single-parent tree can be done with the message passing algorithm, which recursively identifies the parent of a node through likelihood calculations (Wainwright and Jordan (2008)). This strategy does not work for the root-directed tree, since each child can have multiple parents.

# 2.2. Intuition of QTree 

In general, learning Bayesian networks with more than one parent is NP-hard (Chickering (1996)). However, learning a max-linear root-directed tree from i.i.d. noise-free observations is solvable in time $O\left(|V|^{2} n\right)$ with $O\left(|V|(\log (|V|))^{2}\right)$ observations (cf. Section S2 in the Supplementary Material). Here is the intuition.

Fix an edge $j \rightarrow i$ and consider the noise-free model (3). If for an observation $x \in \mathbb{R}^{V}$ the components $i$ and $j$ satisfy $x_{i}=c_{i j}+x_{j}$, then we say $j$ drives $i$. If $j$ does not drive $i$, then $x_{i}>c_{i j}+x_{j}$. Over $n$ independent observations, if the value at $j$ drives the value at $i$ at least twice, then the distribution of $x_{i}-x_{j}$ has an atom at its left endpoint. Repeating this argument shows that if $j$ drives $k$ and $k$ drives $i$, then $x_{i}-x_{j}=c_{i k}+c_{k j}$. That is, if the sample $\mathcal{X}$ is noise-free, the empirical distribution of

$$
\mathcal{X}_{i j}:=\left\{x_{i}-x_{j}: x \in \mathcal{X}\right\}
$$

has for sufficiently many observations multiple values at the minimum of its support if and only if $j \rightsquigarrow i$; i.e., if there is a path from $j$ to $i$. Thus, with enough observations, one can recover the directed path $j \rightsquigarrow i$, from which the graph $\mathcal{T}$ can be uniquely constructed as it is a root-directed tree; this is depicted in the histograms of the first row of Figure 2.

Under the presence of noise, max-linear models can no longer be recovered by means of an atom. However, QTree exploits the above intuition. Consider an ordered pair of nodes $(j, i) \in V$. If the noise at $i$ is small relative to the signal at $j$, one can expect a concentration of observations near the minimum of $\mathcal{X}_{i j}$ if and only if $j \rightsquigarrow i$. This is the intuition of QTree. Throughout, for simplicity, we use the notation $x \in \mathcal{X}$ for possibly noisy observations.

While we have no control over the noise, one way to obtain 'strong signals $x_{j}$ ' is to replace (5) by the set

$$
\mathcal{X}_{i j}(\alpha):=\left\{x_{i}-x_{j}: x \in \mathcal{X}, x_{j}>Q_{\mathcal{X}_{i}}(\alpha)\right\}
$$

where $Q_{\mathcal{X}_{i}}(\alpha)$ is the $\alpha$-quantile of the empirical distribution of $\mathcal{X}$ in the $j$-th coordinate. For $\alpha>0$, this amounts to a transformation of $\mathcal{X}_{i j}$ that amplifies its concentration near the minimum, at the cost of keeping only a fraction of the available observations (cf. Figure 2). We can then compute empirical scores for every pair $(j, i)$ of vertices based on the concentration of observations around a small quantile. Finally, since the data is supported on a root-directed tree, we can use the scores to estimate a root-directed tree.

![img-1.jpeg](img-1.jpeg)

Fig. 2. For the simple graph $1 \rightarrow 2$ with $c_{21}=\log (0.5)=-0.69$ and normal centered noise with standard deviation 0.5 , the first column depicts histograms with red vertical line giving the position of the atom $\log (0.5)$ of $\mathcal{X}_{21}$ in the noise-free distribution. The upper figure shows the noise-free observations and the middle figure the noisy observations for $\mathcal{X}_{21}$ as in (5); the lower figure shows the histogram of the noisy, truncated observations $\mathcal{X}_{21}(0.8)$ as in (6). The second column shows the same histograms, however, for reversely directed edges, i.e. histograms of $\mathcal{X}_{12}$ and $\mathcal{X}_{12}(0.8)$. In the first column, the lower figure shows a substantial increase of symmetry around $c_{21}$. This is because for $\mathcal{X}_{21}(0.8)$, a large value $x_{2}$ has a high chance of being realised from a large value of $x_{1}$, increasing the symmetry around $c_{21}$. In the lower figure of the second column, a large value $x_{2}$ is realised either from large $x_{1}$ or from a large innovation $Z_{2}$, giving the bimodal distribution.

# 2.3. The QTree Algorithm 

The QTree Algorithm 1 computes independently for each potential edge $j \rightarrow i$ a score $w_{i j}$, seen as a measure of concentration of $\mathcal{X}_{i j}(\alpha)$ near its minimum, then outputs a minimum directed spanning tree of the graph $\mathcal{G}$ with scores $W=\left(w_{i j}\right)$. The idea is that at each node $i$, data would show the highest concentration at the true edge among all edges from some parent of $i$ to $i$. Theorem 1 proves this for the Gumbel-Gaussian noise

model; see (9) and below. The default concentration measure for QTree is the empirical quantile-to-mean gap

$$
w_{i j}(\underline{r}):=\frac{1}{n_{i j}}\left(\mathbb{E}\left(\mathcal{X}_{i j}(\alpha)\right)-Q_{\mathcal{X}_{i j}(\alpha)}(\underline{r})\right)^{2}
$$

where $\mathbb{E}$ is the empirical mean, $Q$ the empirical quantile, $\underline{r} \in(0,1)$ is a small quantile level and $n_{i j}=\left|\mathcal{X}_{i j}(\alpha)\right|$ is the number of observations in the set $\mathcal{X}_{i j}(\alpha)$ defined in (6).

The normalization factor $n_{i j}$ only matters when missing values are unevenly distributed across pairs, such as for the Lower Colorado network (cf. Section 3.2). Then, pairs with fewer observations get a relative penalty in the concentration estimate to account for larger variability in sample quantile estimates due to a small sample size. If no missing values are present, as is the case with the Upper Danube network, then $n_{i j}=n \cdot(1-\alpha)$ for all pairs $(j, i)$ and the algorithm would return the exact same tree $\hat{\mathcal{T}}$ as if the concentration measure was defined without dividing by $n_{i j}$.

We note that there are other choices for a concentration measure, such as the empirical lower quantile gap,

$$
w_{i j}(\underline{r}, \bar{r}):=\frac{1}{n_{i j}}\left(Q_{\mathcal{X}_{i j}(\alpha)}(\bar{r})-Q_{\mathcal{X}_{i j}(\alpha)}(\underline{r})\right)^{2}
$$

where $0<\underline{r}<\bar{r}<1$ is a fixed pair of quantile levels. If $\bar{r}$ is small, then $w_{i j}(\underline{r}, \bar{r})$ is a local measure of concentration in the lower tail of $\mathcal{X}_{i j}(\alpha)$. Note that, if the number of observations is small, then $\bar{r}$ cannot be too small, so the two empirical concentration measures are in fact rather similar on a real data set. In practice, the lower quantile gap has one more parameter to tune, and thus we choose the quantile-to-mean gap as our default.

```
Algorithm 1 QTree for fixed parameters
Parameters: \(\underline{r} \in(0,1), \alpha \in[0,1)\).
Input: data \(\mathcal{X}=\left\{x^{1}, \ldots, x^{n}\right\} \subset \mathbb{R}^{V}\).
Output: a root-directed spanning tree \(\hat{\mathcal{T}}\) on \(V\).
    for \(j \rightarrow i, j, i \in V, j \neq i\) do
        Compute \(w_{i j}(\underline{r})\) by \((7)\).
    Compute \(\hat{\mathcal{T}}:=\) minimum root-directed spanning tree on the directed graph \((V, \mathcal{G})\)
        with score matrix \(W=\left(w_{i j}(\underline{r})\right) \in \mathbb{R}^{V \times V}\) with Chu-Liu/Edmonds' algorithm with
        variable root.
    Return \(\hat{\mathcal{T}}\)
```

Remark 1. Given a score matrix $W$ (equivalently a bidirected graph) and a unique root (the initial node), Chu-Liu/Edmonds' algorithm (see Gabow et al. (1986), and Grötschel et al. (1988), Sections 7.2 and 8.4 for more background) finds a minimum directed spanning tree; i.e., a network of minimum score with $\sum_{j: j \rightarrow i \in \hat{\mathcal{T}}} w_{i j}(\underline{r})$ as small as possible. As we want a minimum root-directed spanning tree, we simply reverse edge directions. Moreover, we run the algorithm for every possible node as root, and take a tree with minimum score. Finally, provided that all scores are different, the algorithm finds a unique minimum root-directed spanning tree.

Remark 2. For a given root, the QTree Algorithm 1 has complexity $O\left(|V|^{2} n\right)$. For a proof we refer to Lemma S3 of the Supplementary Material.

# 2.3.1. Theoretical properties of QTree 

We prove consistency of the QTree Algorithm 1 under natural conditions on the distribution of the innovations. We focus on the structural tree model of a max-linear Bayesian network as defined in (2) taking i.i.d. innovations with Frechét distribution function $P\left(Z_{i} \leq x\right)=e^{-x^{-\alpha}}, x>0$, for $\alpha>0$. Then, using the solution $X$ of (2) given in Theorem 2.2 of Gissibl and Klüppelberg (2018), by max-stability (e.g. Embrechts et al. (1997), Section 3.2), $X$ is multivariate Fréchet distributed with marginals as in Proposition A. 2 of Gissibl et al. (2018):

$$
P\left(X_{i} \leq x\right)=\exp \left\{-\left(x_{i} \mu_{i}\right)^{-\alpha}\right\}, \quad x>0
$$

for $\mu_{i}=\left(\sum_{j: j \rightarrow i} c_{j i}{ }^{\alpha}\right)^{-1 / \alpha}$. Taking logarithms of the $X_{i}$, leading to model (3), is equivalent to taking logarithms of the innovations $Z_{i}$ with $P\left(\log \left(Z_{i}\right) \leq x\right)=\exp \left\{-e^{-x / \beta}\right\}, x \in$ $\mathbb{R}$, for $\beta:=1 / \alpha>0$. This results in a Gumbel model with

$$
P\left(X_{i} \leq x\right)=\exp \left\{-e^{-\left(x-\mu_{i}\right) / \beta}\right\}, \quad x \in \mathbb{R}
$$

Therefore, for log-data, the $X_{i}$ are $\operatorname{Gumbel}\left(\beta, \mu_{i}\right)$ distributed with scale $\beta:=1 / \alpha$ and location parameter $\mu_{i}$.

Instead of taking the logarithmic analog of a Generalised Fréchet model as often done in the literature, we prefer instead to add a small independent noise to the max-linear Bayesian tree model (3) with Gumbel $(\beta, 0)$ innovations. This motivates the noise model

$$
X_{i}=\left(\bigvee_{j: j \rightarrow i \in \mathcal{T}}\left(c_{i j}+X_{j}\right) \vee Z_{i}\right)+\varepsilon_{i}, \quad c_{i j}, Z_{i}, \varepsilon_{i} \in \mathbb{R}, \quad i \in V
$$

with the following innovation-noise distributions:
Gumbel-Gaussian noise model. For $i \in V$, the innovations $Z_{i}$ are i.i.d. Gumbel $(\beta, 0)$, the noise variables $\varepsilon_{i}$ are i.i.d. with symmetric, light-tailed density $f_{\varepsilon}$ satisfying

$$
f_{\varepsilon}(x) \sim e^{-K x^{p}} \text { as } x \rightarrow \infty
$$

for some $p>1, K>0$ and such that the derivative of $f_{\varepsilon}$ exists in the tail region. Throughout, for two functions $a, b$, positive in their right tails, we write $a(x) \sim b(x)$ as $x \rightarrow \infty$ for $\lim _{x \rightarrow \infty} a(x) / b(x)=c$, where $c>0$ is some arbitrary constant.

Remark 3. The density $f_{\varepsilon}$ in (10) belongs to a special class of light-tailed densities whose convolution tail can be derived asymptotically (Balkema et al. (1993)). The family includes the Gaussian $(p=2)$, and though it is strictly more general than the Gaussian, we follow Balkema et al. (1993), and call our noise model Gumbel-Gaussian for ease of reference. Condition (10) guarantees that the upper tail of $\varepsilon_{i}-\varepsilon_{j}$ is lighter than that of $Z_{i}-Z_{j}$ (cf. Lemma S6 in the Supplementary Material).

Theorem 1 below, proved in Section S3 of the Supplementary Material, says that under the Gumbel-Gaussian noise model, both quantile-to-mean and lower quantile gap produce together with Chu-Liu/Edmonds' algorithm strongly consistent estimators for the true root-directed spanning tree $\mathcal{T}$ for appropriate choice of parameters. Simulation results (cf. Figure 3) indicate that the error scales as $O(1 / n)$ for any fixed graph size $|V|=d$. In particular, for a large graph with $d=100$, QTree only needs $n=200$ observations to bring the metrics nSHD to less than $5 \%$ and TPR to more than $95 \%$; see definitions in (1).

We are now ready to state our main theorem. Observe that, while $\alpha$ as in (6) is an important tuning parameter, we prove the theorem for $\alpha=0$; i.e., by taking the full set of observations.

Theorem 1 (Consistency Theorem). Assume the Gumbel-Gaussian noise model (9) with distributions specified there.
(a) There exists an $r^{*}>0$ such that for any pair $0<\underline{r}<\bar{r}<r^{*}$, the QTree Algorithm 1 with score matrix $W=\left(w_{i j}\right)$ defined by the lower quantile gap $w_{i j}(\underline{r}, \bar{r})$ in (8) returns a strongly consistent estimator for the tree $\mathcal{T}$ as the sample size $n \rightarrow \infty$.
(b) There exists an $r^{*}>0$ such that for any $0<\underline{r}<r^{*}$, the QTree Algorithm 1 with score matrix $W=\left(w_{i j}\right)$ defined by the quantile-to-mean gap $w_{i j}(\underline{r})$ in (7) returns a strongly consistent estimator for the tree $\mathcal{T}$ as the sample size $n \rightarrow \infty$.

Remark 4. To understand why a condition like (10) is necessary, suppose that $V=$ $\{1,2\}(d=2)$ and that the true graph is $1 \rightarrow 2$. Let $F_{21}$ be the distribution function of $\left(\varepsilon_{2}-\varepsilon_{1}\right)+\left(Z_{2}-Z_{1}\right) \vee c_{21}$. The lower tail of $F_{21}$ essentially is the lower tail of $\left(\varepsilon_{2}-\varepsilon_{1}\right)$, while the upper tail is essentially the upper tail of the convolution $\left(\varepsilon_{2}-\varepsilon_{1}\right)+\left(Z_{2}-Z_{1}\right)$, which is dominated by the signal $\left(Z_{2}-Z_{1}\right)$ if it has the heavier tail, and otherwise it is dominated by the noise $\left(\varepsilon_{2}-\varepsilon_{1}\right)$. Since $\left(\varepsilon_{2}-\varepsilon_{1}\right)$ has symmetric distribution, if the noise term dominates the distribution, $w_{12} \approx w_{21}$ and it would be impossible to distinguish the edge $1 \rightarrow 2$ from the edge $2 \rightarrow 1$. If the signal dominates, the asymmetry between the lower and upper tails of $F_{12}$ lends us the crucial inequality to distinct between the two graphs as illustrated in Figure 2.

The argument extends to $d>2$ for a graph with only one directed path. For a realistic matrix with real-valued entries, Chu-Liu/Edmonds' algorithm outputs an approximately correct root-directed tree. Intuitively, reversing every edge direction gives the same score but is generally not a root-directed tree.

# 2.4. Parameter tuning by bootstrap aggegation 

The QTree Algorithm 1 has two parameters: the quantile level $\underline{r} \in(0,1)$ and the cutoff level $\alpha \in[0,1)$. If data came from a noise-free max-linear Bayesian tree, then we should select $\underline{r}$ as small as possible and $\alpha=0$, and fit QTree on all of the available data $\mathcal{X}$. However, due to the presence of noise, setting $\underline{r}$ and $\alpha$ too small would make the estimator volatile to large values of the noise variables.

In this section, we propose in a first step a subsampling procedure to stabilize QTree Algorithm 1 and, in a second step, automatically choose $\underline{r}$ and $\alpha$ in QTree. This results in Algorithm 2, which we also refer to as auto-tuned QTree.

![img-2.jpeg](img-2.jpeg)

Fig. 3. 1/(mean errors) vs. number of observations $n$ for different graph sizes $d=30,50,100$. We simulated 100 root-directed spanning trees as described in Section 5 below, where we use the Gumbel-Gaussian noise model. Then we applied QTree Algorithm 1 with quantile-to-mean gap (7) with $\underline{r}=0.05$ and $\alpha=0$ to estimate the true (simulated) tree, and computed the average error measured by 1-TPR (left) and nSHD (right) given in (1).

The basic idea is to run an algorithm on multiple subsets of the data, and then average the resulting estimators. This subsampling approach is also called bootstrap aggregation or bagging; see James et al. (2013, Section 8.2.1) and Politis et al. (1999) for a variety of subsampling procedures. Since QTree outputs a root-directed tree as its estimator, which is a combinatorial object, one cannot simply take the average of their adjacency matrices, as that would not produce a tree. Instead, we see the set of output trees as a distribution over trees. Then, we solve a second problem, namely, to find the centroid tree $\mathrm{E}(\mathrm{T})$ of this distribution, defined as that tree which minimizes the expected Hamming distance to a typical tree (cf. Definition 1). Lemma 1 below proves that the centroid can be computed with another application of Chu-Liu/Edmonds' algorithm. This ensures that the estimator produced by auto-tuned QTree can be computed quickly (cf. Lemma S4).

Our key indicator for model performance is variability in the estimated tree, that is, whether the tree $\hat{\mathcal{T}}$ and its reachability graph $\hat{\mathcal{R}}$ output by QTree would change significantly if we fit it to different subsamples of the data. Here, we denote the reachability graph $\hat{\mathcal{R}}$ of $\hat{\mathcal{T}}$ as the graph that results from drawing an edge between a pair $(j, i)$ whenever there is path from $j$ to $i$ in $\hat{\mathcal{T}}$. We propose the following definition of variability for a distribution of root-directed spanning trees.

Definition 1. Let $V$ be a set of nodes and $\mathrm{T}=\left\{\mathcal{T}^{1}, \ldots, \mathcal{T}^{m}\right\}$ a collection of root-directed spanning trees on $V$, and let $\mathrm{R}=\left\{\mathcal{R}^{1}, \ldots, \mathcal{R}^{m}\right\}$ be their corresponding reachability graphs. The centroid of T , denoted $E(\mathrm{~T})$, is the root-directed spanning tree on $V$ that minimizes the sum of normalized structural Hamming distances defined in (1) as follows:

$$
E(\mathrm{~T}):=\arg \min _{\mathcal{T} \in \Psi} \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}, \mathcal{T}^{i}\right)
$$

where $\Psi$ is the space of root-directed spanning trees on $V$.
Let $E(\mathrm{R})$ denote the reachability graph of $E(\mathrm{~T})$. Let $e_{\mathrm{T}}$ be the number of edges of $E(\mathrm{~T})$, and $e_{\mathrm{R}}$ be the number of edges of $E(\mathrm{R})$, respectively. We define the variability of

# Algorithm 2 Auto-tuned QTree 

Parameters: subsampling fraction $f \in[0,1]$, number of subsamples $m \in \mathbb{N}$, a set of parameters $\Theta=\left\{(\underline{r}, \alpha)\right\} \subset[0,1)^{2}$ to search over.
Input: data $\mathcal{X}=\left\{x^{1}, \ldots, x^{n}\right\} \subset \mathbb{R}^{V}$.
Output: the optimal parameter $\left(\underline{r}^{*}, \alpha^{*}\right) \in \Theta$ and the corresponding root-directed spanning tree $\mathcal{T}_{\text {max }}$ on $V$.
for $(\underline{r}, \alpha) \in \Theta$ do
for $\ell=1, \ldots, m$ do
Sample without replacement a random subset $\mathcal{X}^{\ell}$ of $n \cdot f$ observations from $\mathcal{X}$.

Let $\mathcal{T}^{\ell}(\underline{r}, \alpha)$ be the output of QTree Algorithm 1 fitted on $\mathcal{X}^{\ell}$.
Let $\mathrm{T}(\underline{r}, \alpha)=\left\{\mathcal{T}^{\ell}(\underline{r}, \alpha)): \ell=1, \ldots, m\right\}$
Compute $S(\mathrm{~T}(\underline{r}, \alpha))$ by (S1).
Compute $E(\mathrm{~T}(\underline{r}, \alpha))$ as the maximum root-directed spanning tree of $S(\mathrm{~T}(\underline{r}, \alpha))$ per Lemma 1.
Compute $\operatorname{Var}(\mathrm{T}(\underline{r}, \alpha))$ by (12)
Define $\left(\underline{r}^{*}, \alpha^{*}\right):=\arg \min \{\operatorname{Var}(\mathrm{T}(\underline{r}, \alpha)):(\underline{r}, \alpha) \in \Theta\}$.
10: Return the optimal pair $\left(\underline{r}^{*}, \alpha^{*}\right)$ and $\mathcal{T}_{\max }:=E\left(\mathrm{~T}\left(\underline{r}^{*}, \alpha^{*}\right)\right)$.
$\mathrm{T}$, denoted $\operatorname{Var}(\mathrm{T})$, as

$$
\operatorname{Var}(\mathrm{T}):=\frac{1}{e_{\mathrm{T}}} \frac{1}{m} \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}^{i}, E(\mathrm{~T})\right)+\frac{1}{e_{\mathrm{R}}} \frac{1}{m} \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{R}^{i}, E(\mathrm{R})\right)
$$

Involving the Hamming distance of the reachability graphs in (12) penalizes the situation where $\mathcal{T}^{i}$ and $E(\mathrm{~T})$ differ in a few edges low down in the tree, for example, if they have different roots. Such a difference would lead to a small structural Hamming distance between the two trees, but a large structural Hamming distance between their reachability graphs, and in particular, very different river networks.

The following lemma says that $E(\mathrm{~T})$ is a maximum root-directed spanning tree of a particular graph with score matrix $S(\mathrm{~T})$ that measures the stability among the trees in T. In particular, $E(\mathrm{~T})$ can be computed using Chu-Liu/Edmonds' algorithm (choosing the root realizing the minimum score), and thus $\operatorname{Var}(\mathrm{T})$ can be computed in polynomial time. The proof can be found in Section S2.

Lemma 1. Let $V$ be a set of nodes and $\mathrm{T}=\left\{\mathcal{T}^{1}, \ldots, \mathcal{T}^{m}\right\}$ a collection of root-directed spanning trees on $V$. Define the stability score matrix $S:=S(\mathrm{~T}) \in \mathbb{R}_{\geq 0}^{V \times V}$ by

$$
s_{i j}:=S(\mathrm{~T})_{i j}:=\#\{\mathcal{T} \in \mathrm{~T}: j \rightarrow i \in \mathcal{T}\}
$$

Suppose that the maximum root-directed spanning tree $\mathcal{T}_{\text {max }}$ of the graph on $V$ with score matrix $S(\mathrm{~T})$ is unique. Then $E(\mathrm{~T})=\mathcal{T}_{\text {max }}$.

Remark 5. The auto-tuned QTree Algorithm 2 has complexity $O\left(|V|^{2} n m|\Theta|\right)$. For a proof we refer to Lemma S4.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Topographic map of the Upper Danube Basin, showing the sites of 31 gauging stations along the Danube and its tributaries.

# 3. Data description 

We focus on river discharge data in two river networks, the Upper Danube network with data from Bavaria, Germany, and the Lower Colorado network in Texas, USA. Large flood events are classical examples for high risk analysis. The Danube data as well as the data of all three sectors of the Colorado are available in the Python package QTree (Tran (2021)). The Danube data are available in the R package graphicalExtremes (Engelke et al. (2019)).

In general, river discharges across a set of stations is recorded multiple times per hour and some preprocessing is needed to turn the raw data into independent data. This was detailed in Asadi et al. (2015) for the Danube data. We follow their procedure (described in Section 3.1) with slight modifications for the Colorado data (described in Section 3.2).

### 3.1. The Upper Danube network

The Danube network data consist of measurements collected at $d=31$ gauging stations over 50 years from 1960 to 2009 by the Bavarian Environmental Agency (http:www.gkd. bayern.de); see Figure 4. Preprocessing the data, Asadi et al. (2015) first take daily mean values in each time series. Their idea is to find non-overlapping time windows of $p$ days, centered around the observation of maximal rank across all time series. For the Danube, the authors choose $p=9$ days ( $\pm 4$ days around the observation of maximal rank). For each time series, they then take the maximum within the given time window, delete the data of this window, and proceed until no window of $p$ consecutive days remains. In order to reduce temporal non-stationarity, in particular, the effect of snow melt, only the months June, July and August are considered. This results in $n=428$ observations from a 31-dimensional random vector whose $i$-th entry corresponds to the maximum water discharge at the $i$-th station, observed within a 9-day window, where

![img-4.jpeg](img-4.jpeg)

Fig. 5. Topographic maps of the Top, Middle and Bottom sectors (arranged clockwise) of the Lower Colorado network, showing sites of the gauging stations along the Colorado River and its tributaries. We treat them as three unrelated data sets.
at least one station witnessed a large discharge value; these observations are assumed to be independent.

# 3.2. The Lower Colorado network in Texas 

This section describes the new data set of the Lower Colorado river network in Texas collected by the Lower Colorado River Authority (LCRA, https://www.lcra.org/) and details their preprocessing.

The Lower Colorado is one of the major rivers in Texas. Flowing through major population centers such as Austin, the state capital of Texas, flood and drought mitigation in the Lower Colorado Basin is of prominent interest. A particularly challenging feature of the Lower Colorado network is prolonged drought (discharge of 0 ) followed by flash flooding which can damage sensors, resulting in loss of data over multiple days. This makes the Colorado data much more challenging than the Danube data.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Typical discharge at various gauging stations around one flood event in the Lower Colorado network. The vertical lines mark a time window of $p=17 \times 12 h$ or $p=8.5$ days. Dots denote the 12-hour maximum water discharges. At stations 3,4 and 6, the bold dot denotes the peak discharge during this window. For station 5, the sensor did not function during this entire time period, so the peak for station 5 is recorded as missing. Station 3 has a median discharge of only 15 cfs and is hence mostly drained over the measurement period, but the water flow regularly aggregates to over 16,000 cfs within a very short period of time.

The river discharges at the Lower Colorado network, measured in cubic feet per second (cfs), are collected multiple times per day at a total of 104 stations around the Colorado River and its tributaries in Texas from the 1st of December 1991 to the 14th of April 2020 (10,363 days). We do not take into account 5 nodes of the Blanco River and San Bernand River, which are not flow-connected to the Colorado River, and also 21 nodes with zero observations. Moreover, we exclude the nodes $5476,5634,5635,6397$, and 6533 as they are located close to hydropower plants. This gives a total of 73 nodes.

Another problem occurs, because in the Lower Colorado Basin, multiple dams cut off the river into disjoint sectors (Lower Colorado River Authority (LCRA) (2020a)). Thus, we split the river network such that in each section, we get the largest set of nodes where (i) no node is within 10 km of a major dam, (ii) all nodes are connected, and (iii) for each pair $(j, i)$ of this subset, there are at least 1000 pairwise daily observations, which is $9.6 \%$ of the total amount of 10,363 days available. Criterion (iii) ensures that among the given pairs of nodes, any possible causal relation can be discovered, and not be affected by the lack of concurrent data. This results in 42 nodes divided into three sectors, which we call the Top, Middle and Bottom sectors of the Lower Colorado (cf. Figure 5) with 9,12 and 21 nodes, respectively. From here on we treat these three sectors as three separated, unrelated data sets.

In contrast to the Danube network with snow melt and seasonal periodicity, we can and do take all Colorado data of a year into account. We observe further that, by the special weather conditions, flood events can last as little as a few hours. Therefore, in contrast to Asadi et al. (2015), who take daily time slots, we take 12-hour time slots. As a first step, we take maxima of each 12 -hour time slot to retain the knowledge about large possible peaks and such periods where no data are collected. In a second step we then take non-overlapping time windows of $p=8.5$ days ( $\pm 812$-hour slots around the observation of maximal rank); see Figure 6.

Table 1. Number of nodes $d$, number of observations $n$ and percentage of missing data used for the algorithmic reconstruction of the river network.


Table 2. Optimal parameters $\alpha^{*}$ selected by auto-tuned QTree with $\underline{r}=0.05$ using grid search with bootstrap aggregation.


We take the most conservative approach to missing data, namely, if node $i$ has any missing data during the considered time window, then its maximum discharge over this window is labeled as missing (cf. Figure 6). This is because a sensor can break before the river reaches peak discharge and for practical reasons can only be replaced after the flood event is over (Lower Colorado River Authority (LCRA) (2020b)), and thus the sensor potentially did not measure the largest water discharge that occurred at node $i$. This results in the Top sector having 9 nodes, 975 observations, $18 \%$ missing data; the Middle sector has 12 nodes, 972 observations, $27 \%$ missing data. The Bottom sector is most challenging, for it has the most nodes ( 21 nodes), 961 observations, the highest amount of missing data ( $37 \%$ ), and many nodes around the city of Austin with only a few miles apart from each other. The close proximity of nodes induces strong spatial dependence even among nodes that are not flow-connected, making it potentially more challenging to recover the true network. Moroever, in the Bottom sector there are many nodes with a very small number of observations due to the many missing observations, and we create a new data set by excluding all nodes with less than 150 observations and refer to them as Bottom150. A summary of the available data for each data set is given in Table 1.

# 4. Results 

### 4.1. Results of auto-tuned QTree for all river networks

For each of the four river networks Danube, Top, Middle and Bottom sectors of the Colorado, we ran auto-tuned QTree (Algorithm 2) with fixed $\underline{r}=0.05$, subsampling rate $f=0.75$, and number of repetitions $m=1000$ to choose the tuning parameter $\alpha$ automatically from $\{0.7,0.725,0.75, \ldots, 0.9\}$. The optimal parameters $\alpha^{*}$ selected by auto-tuned QTree for these networks are shown in Table 2.

Figures 7, 8, and 9(top) show the estimated trees of the Danube, Top, Middle and Bottom sectors of the Colorado, respectively. We do two estimated-vs-true comparisons: one for the tree, and one for its reachability graph. The four performance metrics we use are those defined in (1). Table 3 gives all metrics over all data sets. We recall that the performance of an algorithm is better the smaller the first three metrics are and the larger TPR is. QTree performs very well across all data sets except for the Bottom sector of the Colorado. For the reachability graph, the statistics are even better, indicating that a wrongly estimated edge directs rather from an ancestor (which is not a parent) to a child (flow-connection is preserved), than a spurious edge (an edge which contradicts

Table 3. Metrics nSHD, FPR, FDR and TPR for auto-tuned QTree. Numbers display the metrics for the pairs $(\mathcal{T}, \mathcal{T})$ and numbers in brackets for the pairs $(\mathcal{R}, \mathcal{R})$ of their respective reachability graphs.


flow-connection). The number of missing edges are determined by the fact that a tree has exactly $d-1$ edges.

Figure 9(top) visualizes the estimation of the Bottom sector of the Colorado. This data set is the most challenging due to large portions of missing data and the clustering of nodes around the city of Austin. Nevertheless, even for this data set the estimated tree has only two spurious edges, between 6537 and 24 and between 42 and 5525 . Both of these node pairs are physically close. All the remaining wrongly estimated edges are flow-connected.

We note that the majority of errors made by QTree involves nodes with less than 150 observations (which are the nodes $5525,5450,5423,5435$ and 5524). This is not at all surprising. The model was fitted to only $75 \%$ of the data, and the optimally chosen $\alpha^{*}$ is 0.85 , which means that for each edge involving one of the above nodes, the number of observations available to QTree is at most $150 \times 0.75 \times 0.15=14$. To check the hypothesis that this number is too small for QTree to perform reliably, we excluded all nodes with less than 150 observations and refitted QTree on the remaining 16 nodes (Bottom150), resulting in an optimal $\alpha^{*}=0.725$. The result depicted in Figure 9(bottom) shows significant improvements. This manifests another desirable feature of QTree, namely, that it relies on local (pairwise) estimation, and thus changes to the node set in one part of the tree do not affect the estimated network elsewhere.

We present details of the parameter selection procedure of auto-tuned QTree for the Danube in Figure 11. The respective figures for the Colorado data sets can be found in Figures S4-S7 of the Supplementary Material. As expected from a statistical estimation procedure, the statistical choice of the parameter selection by auto-tuned QTree does not always output the best result on every data set. However, it fails only by very few edges to the graph estimated with the best choice of parameters. For example, for the Danube the parameter $\alpha=0.75$ (instead of the estimated optimal $\alpha^{*}=0.775$ ) would have lead to a better result (cf. Figure 10). Also for the Top sector of the Colorado, $\alpha=0.9$ would have given perfect recovery of the true network; this is clear as all four metrics become optimal (see Figure S4).

In summary, on all four data sets considered, auto-tuned QTree performed well for nodes with a sufficient number of observations as is obvious from Figure 9(top and bottom). The estimated optimal parameter $\alpha^{*}$ is either the best one (i.e., the corresponding estimated tree is best across all $\alpha$ as for the Middle and Bottom sectors of the Colorado), or such that it is within one to two wrong edges of the best one (Danube and Top sector of the Colorado). The method can handle data with missing observations and close spatial proximity between nodes.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Danube river network, estimated by auto-tuned QTree vs. true. Solid (green) edges are correct. Dashed (green) edges are not in the tree but in the reachability graph, that is, the causal direction or flow-connection is correct. Squiggly (red) edges are spurious (neither in the tree nor in the reachability graph). Dotted (black) edges are in the true tree, but not in the estimated tree. QTree outputs a tree with only six wrongly estimated edges, four of them flow-connected and one path skipping a single node (the edge $8 \rightarrow 6$ skips node 7 ). Two edges are spurious.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Top (left) and Middle (right) sectors of the Colorado network, estimated by auto-tuned QTree vs. true. Node colors represent the amount of available data after taking care of missing data. Edges are as described in Figure 7. Both estimated networks only contain one single wrongly estimated edge. Top: one edge wrong but flow-connected; Middle: one edge spurious.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Bottom sector of the Colorado network (Bottom and Bottom150), estimated by auto-tuned QTree vs. true. Top Figure: Bottom, based on all 21 nodes, QTree outputs a tree with ten wrongly estimated edges, eight of them flow-connected, two spurious edges pointing in the wrong direction. Bottom Figure: Bottom150, based on 16 nodes, after removing nodes with less than 150 observations. There are only two wrongly estimated edges, one flow-connected, one spurious edge pointing in the wrong direction. Compared to the Bottom sector, this is a significant improvement. Node colors represent the amount of available data after taking care of missing data. Edges are as described in Figure 7.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Danube river network, estimated by QTree vs. true for $\alpha=0.75$. Compared to Figure 7, the edges $15 \rightarrow 14$ and $14 \rightarrow 2$ are here correctly estimated. Also the performance measures at the right bottom of the figure compare favourably to those in the first column of Table 3.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Metrics nSHD, TPR, FDR and FPR for the output $\hat{\mathcal{T}}_{\alpha}$ of the steps of auto-tuned QTree for varying parameter $\alpha$ for the Danube network. We subsample $75 \%$ of the data 1000 times (Step 3 of Algorithm 2). For each $\alpha$ we fit QTree on these subsamples to obtain 1000 estimated trees $\mathrm{T}_{\alpha}:=\left\{\hat{\mathcal{T}}_{\alpha}^{\dagger}, \ldots, \hat{\mathcal{T}}_{\alpha}^{1000}\right\}$ (Step 4 of Algorithm 2). The metrics of $\left(\hat{\mathcal{T}}_{\alpha}^{\dagger}, \mathcal{T}\right)$ and $\left(\mathcal{R}_{\alpha}^{\dagger}, \mathcal{R}\right)$ are represented in boxplots, one for the tree (blue) and one for the reachability graph (green). The blue and green dots present the four metrics for the centroid $E\left(\mathrm{~T}_{\alpha}\right)$ (Step 7 of Algorithm 2) and its reachability graph. The lines are interpolations for better visibility, solid blue for the tree and dashed green for the reachability graph. The chosen $\alpha^{*}$ is the parameter with the least variablity in $\mathrm{T}_{\alpha}$ (Step 9 of Algorithm 2), indicated by a red vertical line.

# 4.2. Comparison to other scores in the literature 

We compare QTree and auto-tuned QTree with existing algorithms for extremal causal estimation in the literature. They are all based on pairwise extreme dependence measures, which we define below. We then consider their empirical versions as scores and also include the quantile-to-mean gap for comparison:
(a) The empirical quantile-to-mean gap as in (7) for fixed $(\underline{r}, \alpha)=(0.05,0.9)$. We fix $\underline{r}=0.05$ as we have used this throughout, and $\alpha=0.9$ as an arbitrary parameter.
(b) The causal tail coefficient $\Gamma_{i j}=\lim _{u \rightarrow 1} \mathbb{E}\left[F_{i}\left(X_{i}\right) \mid F_{j}\left(X_{j}\right)>u\right]$ (Gnecco et al. (2021), eq. (3)). Observe that in Gnecco et al. (2021), the algorithm EASE outputs from the estimated score matrix $\Gamma$ an estimated causal order of the set of nodes, not a directed graph.
(c) The causal score $S_{i j}^{\text {ext }}$ is based on expected quantile scores (Mhalla et al. (2020), eq. (15)). The goal of the authors is to discover causality in a directed graph modelled by flow-connection. The scores $S_{i j}^{\text {ext }}$ satisfy $S_{j i}^{\text {ext }}+S_{i j}^{\text {ext }}=1$ and an extreme observation at node $j$ causes an extreme observation at node $i$, whenever $S_{i j}^{\text {ext }}>0.5$. The authors propose a bootstrap method to generate $95 \%$ confidence bounds to guarantee that the score is larger than 0.5 . All these scores are interpreted as directed edges between nodes. The algorithm CausEV outputs flow-connections induced by all scores larger than 0.5 . Thus, their causal edges rather resemble the edges in the reachability graph of the tree. The paper also treats the example of the Danube data in its Section 5 (see also its Figure 7).
(d) The tail dependence coefficient $\chi_{i j}=\lim _{u \rightarrow 1} P\left(F_{i}\left(X_{i}\right)>u \mid F_{j}\left(X_{j}\right)>u\right)$, also called extremal correlation. It goes back to Sibuya (1960); see also Coles et al. (1999). We add this dependence measure in our comparison as it is the classic one, having been used for more than 60 years in multivariate extreme value statistics. Theoretical properties of the tail dependence coefficient in a max-linear Bayesian network have been investigated in Gissibl et al. (2018). It has values in $[0,1]$ and a large value of $\chi_{i j}$ indicates strong extreme dependence. Its empirical estimator takes $u$ large, but finite, and the estimator is based on $10 \%$ of the data. The paper Engelke and Volgushev (2022) uses $\chi$ and related measures on p. 14: the extremal correlation, the extremal variogram, and the combined extremal variogram for estimating undirected trees with Prim's algorithm (Prim (1957)). While the matrix $\chi$ is symmetric, causal inference is possible with Chu-Liu/Edmonds' algorithm; see Remark 4.

The scores discussed in (b)-(d) have not been used to estimate a directed tree, but as they are all pairwise scores, their respective estimated matrices can serve as input for Chu-Liu/Edmonds' algorithm. This gives a fair comparison, as we use then for all scores the knowledge that the true graph is a root-directed spanning tree. We keep all tuning parameters used for $\Gamma_{i j}$ and $S_{i j}^{\text {ext }}$ the same as in the respective papers.

Our comparison is two-fold.
(i) We compare the new score of a quantile-to-mean gap with other scores from the literature.
IWe want to thank Linda Mhalla for helping us to set up the CausEv implementation.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Performance metric nSHD for all five data sets on the horizontal axis. Solid lines display the metrics for the pairs $(\mathcal{T}, \mathcal{T})$ and dashed lines for the pairs $(\mathcal{R}, \mathcal{R})$ of their respective reachability graphs. Black lines are used for auto-tuned QTree, magenta lines for QTree (both based on the score in (a)), blue lines for $\Gamma$ as in (b), red lines for $S^{\text {ext }}$ as in (c), and green lines for $\chi$ as in (d).
(ii) We compare QTree with auto-tuned QTree assessing the benefit of the stabilizing subsampling procedure.

Tables 5, 6 and 7 present the metrics nSHD, FPR, FDR and TPR based on the three scores (b), (c), and (d) for each data set previously considered. Comparing the metrics with those of QTree in Table 4, we find for the Danube network a comparably weak performance for all three alternative scores. Among the three scores, $\chi$ performs best, followed by $\Gamma$. We visualize our findings from Table 3 and Tables $4-7$ for nSHD in Figure 12 .

Solid lines present nSHD for the estimated tree vs. true tree. We find that auto-tuned QTree (black line) is uniformly best over all data sets, followed by QTree. We conclude that the stabilizing subsampling procedure of auto-tuned QTree improves the estimation. Even for the Top sector of the Colorado, where $\alpha=0.9$ is optimal, the nSHD is still positive for QTree whereas for auto-tuned QTree, nSHD is equal to zero and the estimated tree is equal to the true one. For all Colorado sectors, $\Gamma$ follows next, $\chi$ is surprisingly successful for the Danube, but not for any of the Colorado sectors. $S^{\text {ext }}$ does not perform well in any tree recovery, but this was also not the goal of Mhalla et al. (2020).

Dashed lines present nSHD for the reachability graphs of the estimated trees vs. true. Here auto-tuned QTree and QTree give the same answers as for the trees above. The blue dashed line representing $\Gamma$ is only moderately worse than the magenta line for QTree for the Middle and Bottom sectors of the Colorado. The score $\chi$ is worst for the Middle Colorado; for the Danube and the other sectors of the Colorado it performs better than $\Gamma$ and $S^{\text {ext }}$.

We conclude that for the Danube as well as for the various sectors of the Colorado, auto-tuned QTree outperforms uniformly all algorithms without the stabilizing subsampling procedure; see Figure 12. Moreover, the quantile-to-mean gap score outperforms

Table 4. Metrics nSHD, FPR, FDR and TPR for QTree Algorithm 1 with $\alpha=0.9$. Numbers display the metrics for the pairs $(\mathcal{T}, \mathcal{T})$ and numbers in brackets for the pairs $(\mathcal{R}, \mathcal{R})$ of their respective reachability graphs.


Table 5. Metrics nSHD, FPR, FDR and TPR for the maximum root-directed spanning tree estimated by Chu-Liu/Edmonds' algorithm with score matrix $\Gamma$ as in Gnecco et al. (2021), eq. (8).


Table 6. Metrics nSHD, FPR, FDR and TPR for the maximum root-directed spanning tree estimated by Chu-Liu/Edmonds' algorithm with score matrix $S^{\text {est }}$ as in Mhalla et al. (2020), eq. (15).


Table 7. Metrics nSHD, FPR, FDR and TPR for the maximum root-directed spanning tree estimated by Chu-Liu/Edmonds' algorithm with score matrix $\chi$ as in Sibuya (1960) or Coles et al. (1999).


the other scores when applying Chu-Liu/Edmonds' algorithm; therefore, we conclude that the quantile-to-mean gap (7) is superior to the other scores on all data sets considered.

# 5. A small simulation study 

Theorem 1 ensures strong consistency of the output trees of QTree, when the sample size $n$ tends to infinity. In this section we show the quality of QTree through the two performance metrics nSHD and TPR as defined in (1) for varying number of observations $n$ and graph sizes $d$ by a small simulation study.

We generate data $\mathcal{X}$ from a max-linear Bayesian tree as defined in equation (3) with $|V|=d$ nodes. For each node $i \in V$, we calculate the sample standard deviation $\hat{\sigma}_{X_{i}}$ of $\left(X_{i}^{1}, \ldots, X_{i}^{n}\right)$ and take the sample median $\hat{\sigma}$ over all nodes in $V$. We then generate i.i.d. normally distributed noise variables $\varepsilon_{i}^{t}$ with mean zero and standard deviation $k \cdot \hat{\sigma}$ for $i \in V$ and $t=1, \ldots, n$. For the noise-to-signal ratio $k$, we choose $k=30 \%$.

We generate root-directed spanning trees as follows. We first generate a random undirected spanning tree of size $d$ using the graph generators module networkX (Release 2.8.8) in Python (Hagberg et al. (2008)). We then choose the root uniformly at random, which uniquely determines the root-directed spanning tree.

For the distributions of the innovations $Z_{1}, \ldots, Z_{d}$ and the choice of independent edge weights $c_{i j}$, we consider the following three settings:
(1) Innovations $Z_{1}, \ldots, Z_{d}$ are independent $\operatorname{Gumbel}(1,0)$ distributed and for every edge, we draw an edge weight $c_{i j}$ from the interval $[\log (0.1), \log (1)]$ uniformly. We refer to this as the standard Gumbel setting.
(2) Innovations $Z_{1}, \ldots, Z_{d}$ are independent $\operatorname{Gumbel}(1,0)$ distributed and for every edge, we draw an edge weight $c_{i j}$ from the interval $[\log (0.1), \log (0.3)]$ uniformly. We refer to this as the weak dependence setting.
(3) $50 \%$ of the innovations $Z_{1}, \ldots, Z_{d}$ are $\operatorname{Gumbel}(1,0)$ and $50 \%$ are standard normally distributed. For every edge, we draw an edge weight $c_{i j}$ from the interval $[\log (0.1), \log (1)]$ uniformly. We refer to this as the mixed distribution setting.

For the score, we take the quantile-to-mean gap as in (7) (normalization by $n_{i j}$ is not needed in this simulation setting) given by

$$
w_{i j}(\underline{r}):=\left(\mathbb{E}\left(\mathcal{X}_{i j}(\alpha)\right)-Q_{\chi_{i j(\alpha)}}(\underline{r})\right)^{2}
$$

and apply the QTree Algorithm 1 with parameters $\underline{r}=0.05$ and $\alpha=0$; we remark that a sensitivity analysis has shown that altering $\underline{r}$ influences the results only insignificantly.

We use graph sizes $d=10,30,50,100$ and 100 repetitions. For each repetition, we calculate nSHD and TPR, and then take the mean over all 100 repetitions.

Since QTree performs so well not only on simple data like those from the Danube network, but also on all sectors of the Colorado network, we guess that it is fairly robust towards the strength of dependence, given by the $c_{i j}$ and even different node distributions. The weak dependence setting (2) should manifest whether QTree is also able to recover the underlying network if the dependence given by the weights $c_{i j}$ is

substantially smaller. We want to quantify robustness towards node distributions with the mixed distribution setting (3).

Figures 13 and 14 depict the mean nSHD and TPR for the standard Gumbel setting (1) and all four graph sizes. Both metrics quickly tend to zero, respectively one, as the sample size $n$ increases. Moreover, comparing the four subfigures for a fixed sample size $n$, the metrics perform only slightly worse for increasing graph size $d$.

Figures S8 and S9 in Section S5 of the Supplementary Material depict the mean nSHD and TPR for the weak dependence setting (2) and all four graph sizes. Again, both metrics quickly tend to zero, respectively one. In comparison to the previous setting (1), the performance is slightly worse.

Figures S10 and S11 depict the mean nSHD and TPR for the mixed distribution setting (3) and all four graph sizes. Despite the different distributions of the innovations, both metrics quickly tend to zero, respectively one. The performance compared to settings (1) and (2) is expectedly worse, however, less than perhaps could be expected.

The decrease in performance for increasing graph size $d$ is presented in Figure 15, where we plot the minimum number $n$ of data needed to reach a mean nSHD of $10 \%$. The first observation is that larger networks need a larger sample size to reach a lower bound of $10 \%$. Since larger networks have more opportunities for a wrongly estimated causal influence, this is in line with what we expect. Moreover, the standard Gumbel setting (1) reaches the goal much faster than both other settings. Although the weights $c_{i j}$ of setting (2) are in general much smaller than the weights of setting (1), only for a very large graph, substantially more data are needed for the nSHD to fall below $10 \%$. This implies that the smaller dependence impacts the estimation for a small graph only moderately, but for a larger graph more data are required. The mixed distribution setting (3), however, requires for increasing graph size substantially more data. This is also in line with our expectation as this scenario makes the discrimination between signal and noise more difficult.

To summarize the results of our simulation study, QTree is sensitive to weaker dependence, but much more sensitive to the tail behavior of innovations/noise distributions.

# 6. Summary 

In this paper, we proposed auto-tuned QTree, a new algorithmic solution to the Extremal River Problem-a benchmark problem for causal inference in extremes- combining the benefits of a new score matrix as input to Chu-Liu/Edmonds' algorithm with a stabilizing subsampling procedure. We also presented three new data sets of the Lower Colorado network for the Extremal River Problem, which are more challenging than the by now classic Upper Danube network data due to a large fraction of missing data and close spatial proximity between nodes. Across all four data sets, auto-tuned QTree performed very well. Our plug-and-play Python implementation in Tran (2021) can fit QTree on ten thousand observations in the range of 10 to 30 nodes on a personal laptop within half an hour. We proved that for a max-linear Bayesian network with Gumbel-Gaussian distributions for innovations and noise, the tree outputs of QTree are strongly consistent as the number of observations tends to infinity. Open research directions include (i) generalizations to learning directed acyclic graphs, (ii) better sub-

![img-12.jpeg](img-12.jpeg)

Fig. 13. Mean nSHD for the standard Gumbel setting (1) and graph sizes $d=10$ (top left), $d=30$ (top right), $d=50$ (bottom left), $d=100$ (bottom right) and noise-to-signal ratio $k=30 \%$. Dots on solid lines display the metrics for the pairs $(\mathcal{T}, \mathcal{T})$ and on dashed lines for the pairs $(\mathcal{R}, \mathcal{R})$ of their respective reachability graphs. For all graph sizes, the nSHD quickly converges to 0 as $n$ increases. Increasing the graph size decreases the metric only moderately.
sampling procedures with theoretical guarantees, and (iii) have the algorithm output a distribution over possible root-directed trees instead of a single best tree.

# Acknowledgements 

We thank the Lower Colorado River Authority for providing the original data. We are also grateful to Sebastian Engelke for providing Figure 4 of the Upper Danube Basin as well as the declustered data, now available at Engelke et al. (2019). We also thank two unknown referees, whose comments, criticism and suggestions improved our paper considerably. Ngoc Tran gratefully acknowledges support by the Hausdorff Center for Mathematics and the University of Bonn, Germany.

![img-13.jpeg](img-13.jpeg)

Fig. 14. Mean TPR for the standard Gumbel setting (1) and graph sizes $d=10$ (top left), $d=30$ (top right), $d=50$ (bottom left), $d=100$ (bottom right) and noise-to-signal ratio $k=30 \%$. Dots on solid lines display the metrics for the pairs $(\mathcal{T}, \mathcal{T})$ and on dashed lines for the pairs $(\mathcal{R}, \mathcal{R})$ of their respective reachability graphs. For all graph sizes, the TPR quickly converges to 1 as $n$ increases. Increasing the graph size decreases the metric only moderately.
![img-14.jpeg](img-14.jpeg)

Fig. 15. Minimum number of observations needed for the mean nSHD to fall below $10 \%$ : the blue line is for the standard Gumbel setting (1), the green line for the weak dependence setting (2), and the red line for the mixed distribution setting (3). For the standard Gumbel setting (1) and its weak dependence version (2), increasing the graph size $d$, the number of observations needs only a moderate increase to reach the same quality in performance. The mixed distribution setting (2) requires for increasing graph size substantially more data to reach the same quality of performance.

# Supplementary Material 

In Section S1 we prove Lemma 1 of the Paper, Section S2 gives proofs of the complexity of Algorithms 1 and 2. In Section S3 we prove the Consistency Theorem 1 of the Paper for the two scores, the lower quantile gap and the quantile-to-mean gap. Section S4 provides supplemental figures for Section 4.2, and Section S5 for Section 5.

## S1. Proof of Lemma 1 of the Paper

We state the lemma again and give a proof.
Lemma S1. Let $V$ be a set of nodes and $\mathrm{T}=\left\{\mathcal{T}^{1}, \ldots, \mathcal{T}^{m}\right\}$ a collection of root-directed spanning trees on $V$. Define the stability score matrix $S:=S(\mathrm{~T}) \in \mathbb{R}_{\geq 0}^{V \times V}$ by

$$
s_{i j}:=S(\mathrm{~T})_{i j}:=\#\{\mathcal{T} \in \mathrm{~T}: j \rightarrow i \in \mathcal{T}\}
$$

Suppose that the maximum root-directed spanning tree $\mathcal{T}_{\max }$ of the graph on $V$ with score matrix $S(\mathrm{~T})$ is unique. Then $E(\mathrm{~T})=\mathcal{T}_{\max }$.

Proof. Identify any root-directed tree $\mathcal{T}$ with the matrix $T=\left(T_{u v}\right) \in\{0,1\}^{|V| \times|V|}$. Write $\mathbf{1}=\left(\mathbf{1}_{u v}\right)$ for the all-one matrix of the same dimension. Let $\mathcal{T}^{\prime} \in \Psi$ be an arbitrary root-directed spanning tree on $V$. Our goal is to show that

$$
\sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}^{\prime}, \mathcal{T}^{i}\right) \geq \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}_{\max }, \mathcal{T}^{i}\right)
$$

which would establish that $\mathcal{T}_{\max }=E(\mathrm{~T})$ by eq. (11) of the Paper. Indeed,

$$
\begin{aligned}
& \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}^{\prime}, \mathcal{T}^{i}\right)=\sum_{i=1}^{m} \sum_{u, v \in V: u \neq v} \mathbf{1}\left\{T_{u v}^{\prime} \neq T_{u v}^{i}\right\}=\sum_{u, v \in V: u \neq v} \sum_{i=1}^{m} \mathbf{1}\left\{T_{u v}^{\prime} \neq T_{u v}^{i}\right\} \\
= & \sum_{u, v \in V: u \neq v}\left(s_{u v} \mathbf{1}_{u \rightarrow v \notin \mathcal{T}^{\prime}}+\left(m-s_{u v}\right) \mathbf{1}_{u \rightarrow v \in \mathcal{T}^{\prime}}\right) \\
= & -2\left\langle S, T^{\prime}\right\rangle+\langle S, \mathbf{1}\rangle+\left\langle m \mathbf{1}, T^{\prime}\right\rangle \quad \text { where }\langle\cdot, \cdot\rangle \text { denotes the Frobenius inner product } \\
= & -2\left\langle S, T^{\prime}\right\rangle+\langle S, \mathbf{1}\rangle+m(d-1) \quad \text { since } \mathcal{T}^{\prime} \text { as root-directed spanning tree has } d-1 \text { edges } \\
\geq & -2\left\langle S, T_{\max }\right\rangle+\langle S, \mathbf{1}\rangle+m(d-1)\rangle \quad \text { by definition of } \mathcal{T}_{\max } \\
= & -2\left\langle S, T_{\max }\right\rangle+\langle S, \mathbf{1}\rangle+\left\langle m \mathbf{1}, T_{\max }\right\rangle\rangle \quad \text { since } \mathcal{T}_{\max } \text { is a spanning tree on } V \\
= & \sum_{i=1}^{m} \mathrm{nSHD}\left(\mathcal{T}_{\max }, \mathcal{T}^{i}\right)
\end{aligned}
$$

## S2. Proof of the Complexity of QTree

We work with the solution of the max-linear Bayesian network on a tree $\mathcal{T}=(V, E)$ defined in eq. (3) of the Paper; see e.g. (Baccelli et al., 1992, §3) or (Gissibl and

Klüppelberg, 2018, Theorem 2.2). Let $C^{*}=\left(c_{i j}^{*}\right)$ be the matrix of longest paths, also known as the Kleene star of $C=\left(c_{i j}\right)$. Then

$$
X_{i}=\bigvee_{j: j \rightsquigarrow i \in \mathcal{T}}\left(c_{i j}^{*}+Z_{j}\right), \quad c_{i j}^{*}, Z_{i j} \in \mathbb{R}, \quad i \in V
$$

If there is no path $j \rightsquigarrow i$, then, by definition, $c_{i j}^{*}:=-\infty$.
Lemma S2 concerns the noise-free case, Lemma S3 gives the complexity of Algorithm 1 and Lemma S4 that of Algorithm 2.

Lemma S2. Let $\mathcal{X}=\left\{x^{1}, \ldots, x^{n}\right\}$ be i.i.d observations from the max-linear model given by (S2), not corrupted with noise. Assume that the $Z_{i}$ are independent and have continuous distributions. Define

$$
\hat{c}_{i j}=\min _{x \in \mathcal{X}}\left(x_{i}-x_{j}\right)
$$

Suppose that for each edge $j \rightarrow i$ such that $c_{i j}>-\infty$, there exist at least two observations $x \in \mathcal{X}$ where $j$ drives $i$. Then $C^{*}$ can be uniquely recovered from $\hat{C}$ since

$$
\hat{c}_{i j}=c_{i j}^{*} \Longleftrightarrow \min \text { in (S3) is achieved at least twice. }
$$

In particular, $C^{*}$ can be computed in time $O\left(|V|^{2} n\right)$. If all nodes are equally likely to be candidate parents, then the matrix $C^{*}$ is recovered exactly for $n=O\left(|V|(\log (|V|))^{2}\right)$.
Proof. Since a root-directed spanning tree has at most one path between any pair of nodes $(j, i)$ we have for an edge $j \rightarrow i$ that $c_{i j}^{*}=c_{i j}$. Furthermore, as indicated at the beginning of Section 2.2 in the Paper, if for an observation $x$ the value at $j$ drives that at $i$, then $x_{i}=c_{i j}^{*}+x_{j}$. If $j$ does not drive $i$, then $x_{i}>c_{i j}^{*}+x_{j}$. Rearranging motivates the estimator (S3) with properties as stated in (Gissibl et al., 2021, Proposition 1). Equation (S4) follows from (Gissibl et al., 2021, Lemma 1).

Now we prove the complexity claim. Since there are $O\left(|V|^{2}\right)$ many edges, and for each edge we need $O(n)$ operations to compute the minimum in (S3), the complexity is $O\left(|V|^{2} n\right)$. The number of observations needed, so that each edge is seen at least twice, is a variant of coupon-collecting (Boneh and Hofri, 1997; Boneh and Papanicolaou, 1996), where each node must collect two coupons (parents) among its set of parents. Since the nodes are collecting the coupons simultaneously, by the union bound, the number of observations needed is at most $\log (|V|)$ times the number of observations needed for the node with highest degree to collect all of its coupons, which in turn is $O(|V| \log (|V|))$.

The following lemmas allow for noisy observations as detailed in (4).
Lemma S3. The QTree Algorithm 1 runs in time $O\left(|V|^{2} n\right)$.
Proof. For each pair $i, j \in V, i \neq j$, to estimate $w_{i j}$, one needs to compute the $\alpha$-quantile of $\mathcal{X}_{j}$, the $\underline{r}$-quantile and the mean of $\mathcal{X}_{i j}(\alpha)$. Since $\alpha$ and $\underline{r}$ are fixed in advance, the empirical quantiles can be computed in time $O(n)$, see Musser (1997). As there are $O\left(|V|^{2}\right)$ pairs, computing $W=\left(w_{i j}\right)$ takes $O\left(|V|^{2} n\right)$. Chu-Liu/Edmonds' algorithm runs on the complete bidirected graph supported by $W$, and thus takes $O\left(|V|^{2}\right)$, see Gabow et al. (1986). So the complexity of QTree is $O\left(|V|^{2} n+|V|^{2}\right)=O\left(|V|^{2} n\right)$.

The quadratic dependence on $|V|$ and linear dependence on $n$ in Lemma S3 is optimal, since it takes $O\left(|V|^{2} n\right)$ just to compute pairwise statistics such as the concentration measures in (7) or (8) for every pair of nodes. Similarly, the runtime of Algorithm 2 (auto-tuned QTree) also has optimal runtime, which scales linearly with the number of repetitions $m$ and the size of the parameter grid $|\Theta|$.

Lemma S4. The auto-tuned QTree Algorithm 2 has complexity $O\left(|V|^{2} n m|\Theta|\right)$.
Proof. For each pair $(\underline{r}, \alpha) \in \Theta$, step 3 takes $O(m n)$ and step 4 takes $O\left(|V|^{2} n m\right)$ by Lemma S3. Step 6 takes $O\left(m|V|^{2}\right)$, and step 7 takes $O\left(|V|^{2}\right)$ by Chu-Liu/Edmonds' Algorithm. Computing the reachability graph for a root-directed tree on $|V|$ nodes takes $O(|V|)$, so step 8 takes $O\left(m|V|^{2}\right)$, since for each of the $m$ trees in $T$ we need to compute its structural Hamming distance from the estimated tree $E(\top)$. So, for each pair $(\underline{r}, \alpha) \in \Theta$, steps 3 to 8 take $O\left(|V|^{2} n m\right)$ time. Thus overall, the algorithmic complexity is $O\left(|V|^{2} n m|\Theta|\right)$.

# S3. Proof of the Consistency Theorem 

In this section, we prove Theorem 1 of the Paper, which we recall here for ease of reference.

Gumbel-Gaussian noise model. For $i \in V$, the innovations $Z_{i}$ are i.i.d. $\operatorname{Gumbel}(\beta, 0)$ (location 0 and scale $\beta$ ), the independent noise variables $\varepsilon_{i}$ are i.i.d with symmetric, light-tailed density $f_{\varepsilon}$ satisfying

$$
f_{\varepsilon}(x) \sim e^{-K x^{p}} \text { as } x \rightarrow \infty
$$

for some $p>1$ and $K>0$ and the derivative of $f_{\varepsilon}$ exists in the tail region. Throughout, for two functions $a, b$, positive in their right tails, we write $a(x) \sim$ $b(x)$ as $x \rightarrow \infty$ for $\lim _{x \rightarrow \infty} a(x) / b(x)=c$, where $c>0$ is some arbitrary constant.

Theorem S1 (Theorem 1 of the Paper). Assume the Gumbel-Gaussian noise model. (a) There exists an $r^{*}>0$ such that for any pair $0<\underline{r}<\bar{r}<r^{*}$, the QTree Algorithm 1 with score matrix $W=\left(w_{i j}\right)$ defined as the lower quantile gap

$$
w_{i j}(\underline{r}, \bar{r}):=\frac{1}{n_{i j}}\left(Q_{\mathcal{X}_{i j}(\alpha)}(\bar{r})-Q_{\mathcal{X}_{i j}(\alpha)}(\underline{r})\right)^{2}
$$

returns a strongly consistent estimator for the tree $\mathcal{T}$ as the sample size $n \rightarrow \infty$.
(b) There exists an $r^{*}>0$ such that for any $0<\underline{r}<r^{*}$, the QTree Algorithm 1 with score matrix $W=\left(w_{i j}\right)$ defined as the quantile-to-mean gap

$$
w_{i j}(\underline{r}):=\frac{1}{n_{i j}}\left(\mathbb{E}\left(\mathcal{X}_{i j}(\alpha)\right)-Q_{\mathcal{X}_{i j}(\alpha)}(\underline{r})\right)^{2}
$$

returns a strongly consistent estimator for the tree $\mathcal{T}$ as the sample size $n \rightarrow \infty$.

The proof of this theorem comes in a series of steps. Moreover, for simplicity, we omit the normalization by $n_{i j}$ and the squaring in (S6) and (S7) as this leaves the proof unchanged. Also we set in the proof $\alpha=0$.

As a preliminary result, Lemma S5 identifies a set of 'good' deterministic input matrices $W=\left(w_{i j}\right)$, where if we apply the QTree algorithm to such an input, then it returns the true tree $\mathcal{T}$ exactly. The proof then reduces to the problem of proving that as $n \rightarrow \infty$, the matrices $W_{n}$ derived from data converge a.s. to a 'good' $W$. Intuitively, $W$ is 'good' if for each node $j$, the weight $w_{i j}$ is smallest when $i$ is the child of $j$. For the root we have a special explicit condition. For each fixed $j$, we split the set of node pairs $\{(j, i): j, i \in V, i \neq j\}$ into three scenarios:

- $j \rightsquigarrow i$, that is, $i$ is a descendant $j$ in the true tree,
- $i \rightsquigarrow j$, that is, $i$ is an ancestor of $j$ in the true tree, and
- $i \not j$, that is, $i$ is neither of the above.

We first consider the case where $W=\left(w_{i j}\right)$ is the matrix of lower quantile gaps (S6) of the true distribution. Note that this $W$ is no longer random. The goal is to show that if the true quantiles are known, then one can choose the parameters $(\underline{r}, \bar{r})$ such that $W$ is good.

Next, Proposition S1 gives an explicit representation for $w_{i j}$ in each of the three scenarios above as the lower quantile gap of a certain family of distributions $\left(F^{b}: b \in \mathbb{R}\right)$, parametrized by a single parameter $b$, one value for each edge $j \rightarrow i$. Then, we use a calculus of variation argument to detail how $w_{i j}$ changes as $b$ varies. This allows us to show (cf. Corollary S1 and Lemma S8) that among the three scenarios above, there exist some choices of quantile levels $(\underline{r}, \bar{r})$ such that for any fixed $j, w_{i j}$ is smallest when $i$ is the child of $j$ in the true tree. A separate argument is made for the root. Thus, this proves that if the true quantiles are known, then the resulting $W$ is good.

Finally, we invoke the fact that the empirical quantiles converge a.s. to the true quantiles as $n \rightarrow \infty$, and thus the empirical $w_{i j}$ are a.s. close to the true ones. A union bound over the $d$ nodes of the graph thus says that, the empirical $W_{n}$ is a.s. 'good' as $n \rightarrow \infty$, and thus proves the Consistency Theorem for the lower quantile gap.

The proof for the quantile-to-mean gap is similar, with Proposition S2 playing the role of Proposition S1.

Lemma S5 (A criterion for 'good' inputs $W$ ). Let $W=\left(w_{i j}\right)$ be a score matrix such that each true edge $j \rightarrow i \in \mathcal{T}$ satisfies

$$
w_{i j}<w_{i^{\prime} j} \text { for all } i^{\prime} \in V, i^{\prime} \neq i, j
$$

and in addition, the true root $i^{*}$ satisfies

$$
\min _{i^{\prime}} w_{i^{\prime} i^{*}}>\max _{i, j: j \rightarrow i} w_{i j}
$$

Then the QTree Algorithm 1 applied to input $W$ returns the true tree $\mathcal{T}$.
Proof. QTree applies Chu-Liu/Edmonds' algorithm to find a minimum directed spanning tree from the complete graph with score matrix $W$, and returns that tree. We shall prove

that under the conditions (S8) and (S9) on $W$, Chu-Liu/Edmonds' algorithm would converge after one iteration and returns the true tree $\mathcal{T}$. Indeed, let $\mathcal{G}$ denote the graph that consists of the smallest outgoing edge at each node. By (S8), $\mathcal{G}=\mathcal{T} \cup i^{*} \rightarrow i^{\prime}$ for some node $i^{\prime} \in V$. By Chu-Liu/Edmonds' algorithm, the minimum spanning tree $\mathcal{T}_{w}$ is a subset of $\mathcal{G}$. In particular, $\mathcal{T}_{w}$ is a minimum spanning tree of $\mathcal{G}$. By (S9), edge $i^{*} \rightarrow i^{\prime}$ is the maximal edge. Since it belongs to the unique cycle in $\mathcal{G}$, deleting this edge would yield the minimum directed spanning tree of $\mathcal{G}$. Therefore $\mathcal{T}_{w}=\mathcal{T}$.

# S3.1. Proof of Theorem 1 for the lower quantile gap 

S3.1.1. For known quantiles, $W$ is 'good' for appropriate choices of $(\underline{r}, \bar{r})$
In this subsection we work with the lower quantile gap matrix $W=\left(w_{i j}\right)$ derived from the true quantiles of the distributions of $X_{i}-X_{j}$ under the Gumbel-Gaussian noise model, for some quantile levels $(\underline{r}, \bar{r})$. The goal is to show that there exist some appropriate choices of $(\underline{r}, \bar{r})$ such that the resulting $W$ is 'good', that is, it satisfies Lemma S5.

The first main result is Proposition S1, which gives an explicit representation for $w_{i j}$ in the three scenarios. We start with the necessary definitions to state it.

Recall the definition of $C^{*}$ from (S2). Since the true graph is a tree, if $j \rightsquigarrow i$, there is a unique directed path from $j$ to $i$. Let $\bar{c}_{i j}$ denote the sum of all the edges along this unique path. Path uniqueness implies that $\bar{c}_{i j}=c_{i j}^{*}$ and $C^{*}$ is transitive, i.e. $c_{i j}^{*}=c_{i k}^{*}+c_{k j}^{*}$ if $j \rightsquigarrow k \rightsquigarrow i$. Thus, by the Helmholtz decomposition on graphs (Lim, 2015, eq. (2.6)), $c_{i j}^{*}$ is an edge flow. That is, there exists a unique $t^{*} \in \mathbb{R}^{V}$ with $t_{1}^{*}=0$ such that for all $j \rightarrow i \in \mathcal{G}$,

$$
c_{i j}^{*}=t_{i}^{*}-t_{j}^{*}
$$

For each $i \in V$, define the constant

$$
\theta_{i}:=\sum_{k \rightsquigarrow i} \exp \left(-t_{k}^{*} / \beta\right)
$$

For $b \in \mathbb{R} \cup\{-\infty\}$, define the random variable

$$
\xi_{b}:=\left(\varepsilon_{i}-\varepsilon_{j}\right)+\left(\left(Z_{i}-Z_{j}\right) \vee b\right)
$$

with the convention that $\xi_{-\infty}:=\left(\varepsilon_{i}-\varepsilon_{j}\right)+\left(Z_{i}-Z_{j}\right)$. Let $F^{b}$ denote the distribution function of $\xi_{b}$ and $q_{r}\left(F^{b}\right)$ the $r$-quantile of $F^{b}$ for $r \in(0,1)$. These quantities are deterministic and do not depend on $i, j$ since by assumption, $\varepsilon_{i}, \varepsilon_{j}$ are i.i.d and $Z_{i}, Z_{j}$ are i.i.d.

Proposition S1. Assume the Gumbel-Gaussian noise model. Fix $0<\underline{r}<\bar{r}<1$. Let $w_{i j}=w_{i j}(\underline{r}, \bar{r})$ be the lower quantile gap (S6). Fix $j \in V$. For $i \in V, i \neq j$, we have three cases.
(1) If $j \rightsquigarrow i$, then $w_{i j}=q_{\bar{r}}\left(F^{b}\right)-q_{\underline{r}}\left(F^{b}\right)$ for $b=\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)$.
(2) If $j \nprec i$, then $w_{i j}=q_{\bar{r}}\left(F^{b}\right)-q_{\underline{r}}\left(F^{b}\right)$ for $b=-\infty$.
(3) If $i \rightsquigarrow j$, then $w_{i j}=q_{1-\underline{r}}\left(F^{b}\right)-q_{1-\bar{r}}\left(F^{b}\right)$ for $b=\beta\left(\log \theta_{i}-\log \left(\theta_{j}-\theta_{i}\right)\right)$.

Proof. We first consider the noise-free case. Observe that by (S12) $\xi_{b}$ simplifies to $\left(Z_{i}-Z_{j}\right) \vee b$. Therefore, it is sufficient to prove that $w_{i j}$ equals the lower quantile gap

of $\left(Z_{i}-Z_{j}\right) \vee b$. For $i \in V$, let $\bar{X}_{i}:=X_{i}-t_{i}^{*}$. Then $\bar{X}_{i}-\bar{X}_{j}$ is a constant translation of $X_{i}-X_{j}$, so the lower quantile gap of the two corresponding distributions are the same. In other words, it is sufficient to prove the Proposition for $\bar{X}$ instead of $X$. Let $\bar{Z}_{i}:=Z_{i}-t_{i}^{*}$. Then

$$
\begin{aligned}
\bar{X}_{i}=X_{i}-t_{i}^{*} & =\bigvee_{j: j \rightsquigarrow i}\left(c_{i j}^{*}+Z_{j}\right)-t_{i}^{*} & & \text { by (S2) } \\
& =\bigvee_{j: j \rightsquigarrow i}\left(t_{i}^{*}-t_{j}^{*}+Z_{j}\right)-t_{i}^{*} & & \text { by (S10) } \\
& =\bigvee_{j: j \rightsquigarrow i} \bar{Z}_{j} & &
\end{aligned}
$$

For each ordered pair $(i, j)$, define

$$
S_{i}=\bar{Z}_{i} \vee \bigvee_{i^{\prime} \neq i, i^{\prime} \rightsquigarrow i, i^{\prime} \neq j} \bar{Z}_{i^{\prime}} \quad S_{j}=\bar{Z}_{j} \vee \bigvee_{j^{\prime} \neq j, j^{\prime} \rightsquigarrow j} \bar{Z}_{i^{\prime}}
$$

In Figure S1 we illustrate the two index sets of the random variables $S_{i}$ and $S_{j}$.
![img-15.jpeg](img-15.jpeg)

Fig. S1. Illustration of the index sets of $S_{i}$ and $S_{j}$ for an ordered pair $(i, j)$. The index set for $S_{i}$ includes besides $i$ also $i_{1}^{\prime}, i_{2}^{\prime}, i_{3}^{\prime}$ and all nodes on the paths $j \rightsquigarrow i$ (excluding $j$ ), $i_{k}^{\prime} \rightsquigarrow i$ for $k=1,2,3$, while the index set for $S_{j}$ includes $j, j_{1}^{\prime}, j_{2}^{\prime}, j_{3}^{\prime}$ and all nodes on the paths $j_{k}^{\prime} \rightsquigarrow j$ for $k=1,2,3$.

By definition, $S_{i}$ and $S_{j}$ are independent. Since the $Z_{i}$ are $\operatorname{Gumbel}(\beta, 0)$ distributed, abbreviated $\operatorname{Gumbel}(\beta)$, the $\bar{Z}_{i}$ are translated independent $\operatorname{Gumbel}(\beta)$ by definition, standard properties of the $\operatorname{Gumbel}(\beta)$ distribution yield that $S_{i}$ and $S_{j}$ are also translated independent $\operatorname{Gumbel}(\beta)$. The exact constants of translation depend on the relation between $i$ and $j$, as this dictates the definition of $S_{i}$ and $S_{j}$. Now we consider the three cases. In the first case, $j \rightsquigarrow i$. Then, (S13) implies $\bar{X}_{i}=S_{i} \vee S_{j}$ and $\bar{X}_{j}=S_{j}$.

A short computation yields $S_{i} \stackrel{d}{=} Z_{i}+\beta \log \left(\theta_{i}-\theta_{j}\right), S_{j} \stackrel{d}{=} Z_{j}+\beta \log \theta_{j}$. Therefore, denoting $\stackrel{\mathrm{d}}{=}$ equality in distribution,

$$
\begin{aligned}
\bar{X}_{i}-\bar{X}_{j} & =\left(S_{i} \vee S_{j}\right)-S_{j}=\left(S_{i}-S_{j}\right) \vee 0 \\
& \stackrel{d}{=}\left(Z_{i}-Z_{j}-\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)\right) \vee 0 \\
& =\left(\left(Z_{i}-Z_{j}\right) \vee \beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)\right)-\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right) \\
& =\left(\left(Z_{i}-Z_{j}\right) \vee b\right)-\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)
\end{aligned}
$$

where $b=\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)$. Since $\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)$ is a translation constant, the quantile gap of $\bar{X}_{i}-\bar{X}_{j}$ is equal to the quantile gap of $\left(Z_{i}-Z_{j}\right) \vee b$. This concludes the case $j \rightsquigarrow i$. Computations for the third case, $i \rightsquigarrow j$, is similar, with the role of $i$ and $j$ reversed, $\underline{r}$ is replaced by $1-\bar{r}$, and $\bar{r}$ is replaced by $1-\underline{r}$. For the second case, $i \neq j$, then $\bar{X}_{i}=S_{i}, \bar{X}_{j}=S_{j}$, where $S_{j} \stackrel{d}{=} \beta \log \theta_{j}+Z_{j}$ and $S_{i} \stackrel{d}{=} \beta \log \theta_{i}+Z_{i}$. Then

$$
\bar{X}_{i}-\bar{X}_{j}=S_{i}-S_{j} \stackrel{d}{=} Z_{i}-Z_{j}+\beta\left(\log \theta_{i}-\log \theta_{j}\right)
$$

Since $\beta\left(\log \theta_{i}-\log \theta_{j}\right)$ is a translation constant, the quantile gap of $\bar{X}_{i}-\bar{X}_{j}$ is equal to the quantile gap of $Z_{i}-Z_{j}$, as claimed.

S3.1.2. How the lower quantile gap $w_{i j}$ varies with $b$
Now, we aim to show through a variational argument that under the Gumbel-Gaussian assumption, among the three scenarios of Proposition S1, $w_{i j}$ is smallest when it falls in a subset of case (1), namely, $j \rightarrow i$. We first give an overview. By Proposition S1, the lower quantile gaps $w_{i j}$ in cases (1) and (2) are all of the form $q(b, \bar{r})-q(b, \underline{r})$ for some constant $b=b(i, j)$. In particular, for fixed $j, b(i, j)$ is largest when $j \rightarrow i$. Lemma S7 says that one can choose the quantile levels $(\underline{r}, \bar{r})$ such that $q(b, \bar{r})-q(b, \underline{r})$ is monotone increasing as a function of $b$ on a large interval. Corollary S1 then shows that a good choice can be made so that for each fixed $j$, the quantile gap is smallest for the edge from $j$ to its child $c h(j)$. Case (3) of Proposition S1, where $i$ is an ancestor of $j$, is handled by Lemma S8. The Gumbel-Gaussian assumption comes in through Lemma S6, which is a technical result that gives an explicit form for the density of the noise differences $\eta:=\varepsilon_{i}-\varepsilon_{j}$. Intuitively, it shows that under the Gumbel-Gaussian noise model, the tail of $\eta$ is lighter than the tail of the signal differences $Z_{i}-Z_{j}$. This is a key observation exploited in the proofs.
Lemma S6. Under the Gumbel-Gaussian noise model, for any pair of nodes $i, j \in V, i \neq$ $j, \xi:=Z_{i}-Z_{j}$ has density

$$
f_{\xi}(x)=\frac{e^{x / \beta}}{\beta\left(1+e^{x / \beta}\right)^{2}} \sim \frac{1}{\beta} e^{-x / \beta} \text { as } x \rightarrow \infty
$$

and $\eta:=\varepsilon_{i}-\varepsilon_{j}$ has density

$$
f_{\eta}(x) \sim x^{1-p / 2} e^{-K x^{p}} \text { as } x \rightarrow \infty
$$

Proof. Computing the convolution integral yields

$$
\mathbb{P}\left(Z_{i}-Z_{j}>x\right)=\frac{1}{1+e^{x / \beta}}, \quad x \in \mathbb{R}
$$

and taking the derivative gives the first statement. For the second statement, the density $f_{\varepsilon}$ is a density with Gaussian tail in the sense of Balkema et al. (1993):

$$
f(x) \sim \gamma(x) e^{-\psi(x)} \text { as } x \rightarrow \infty
$$

for constant $\gamma$ and $\psi(x)=K x^{p}$. The asymptotic form of $f_{\eta}$ follows by Laplace's integration principle as shown in (Balkema et al., 1993, page 2).

Since $f_{\varepsilon}$ is differentiable in the tail, $f_{\eta}$ is also differentiable in the tail, and differentiation of (S16) yields the following formula for the derivative:

$$
f_{\eta}^{\prime}(x) \sim f_{\eta}(x)\left(-K p x^{p-1}+(1-p / 2) x^{-1}\right)
$$

For functions with two arguments, let $\partial_{1}$ denotes the derivative in the first argument, $\partial_{2}$ denotes the derivative in the second argument, $\partial_{12}^{2}:=\partial_{1} \partial_{2}$ denote the mixed second derivatives and so forth. Define the functions $H: \mathbb{R} \times \mathbb{R} \rightarrow[0,1], q: \mathbb{R} \times[0,1] \rightarrow \mathbb{R}$ by

$$
H(b, a)=P\left(\xi_{b} \leq a\right), \quad q(b, r)=r \text {-quantile of } \xi_{b}
$$

Lemma S7. Under the Gumbel-Gaussian noise model, for each finite constant B, there exists some $r^{*}=r^{*}(B) \in(0,1)$ such that

$$
\partial_{12}^{2} q(b, r)<0 \quad \text { for all } r \in\left(0, r^{*}\right), b \leq B
$$

Equivalently, for any pair $(\underline{r}, \bar{r})$ such that $0<\underline{r}<\bar{r}<r^{*}$ and any pair $\left(b^{\prime}, b\right)$ such that $b^{\prime}<b \leq B$,

$$
q(b, \bar{r})-q(b, \underline{r})<q\left(b^{\prime}, \bar{r}\right)-q\left(b^{\prime}, \underline{r}\right)
$$

Proof. By definition,

$$
H(b, q(b, r))=r
$$

We take derivatives of both sides, first with respect to $r$, then to $b$. Note that functions and derivatives of $H$ are always evaluated at $(b, q(b, r))$ while those of $q$ are evaluated at $(b, r)$, so we suppress them in the notations. Differentiate both sides sof (S20) with respect to $r$ gives

$$
\partial_{2} H \cdot \partial_{2} q=1
$$

Now, differentiating both sides of (S20) with respect to $b$, we get

$$
\frac{\partial}{\partial b} H_{1}(b, q(b, r))=\partial_{1} H+\partial_{2} H \cdot \partial_{1} q=0
$$

therefore,

$$
\partial_{1} q=\frac{-\partial_{1} H}{\partial_{2} H}
$$

Differentiate (S21) with respect to $b$ using implicit differentiation and chain rules, we get

$$
\begin{aligned}
0=\frac{\partial}{\partial b}\left(\partial_{2} H \cdot \partial_{2} q\right) & =\frac{\partial}{\partial b}\left(\partial_{2} H(b, q(b, r)) \cdot \partial_{2} q+\partial_{2} H \cdot \partial_{12}^{2} q\right. \\
& =\left(\partial_{12}^{2} H+\partial_{22}^{2} H \cdot \partial_{1} q\right) \cdot \partial_{2} q+\partial_{2} H \cdot \partial_{12}^{2} q \\
& =\frac{\partial_{12}^{2} H-\partial_{22}^{2} H \cdot \frac{\partial_{1} H}{\partial_{2} H}}{\partial_{2} H}+\partial_{2} H \cdot \partial_{12}^{2} q \quad \text { by (S21) and (S22) }
\end{aligned}
$$

Rearranging the last equation gives

$$
\partial_{12}^{2} q=\frac{\partial_{22}^{2} H \cdot \partial_{1} H-\partial_{12}^{2} H \cdot \partial_{2} H}{\left(\partial_{2} H\right)^{3}}
$$

For fixed $b$, by definition of $H, \partial_{2} H$ is the density of $\xi_{b}$, so $\partial_{2} H>0$. So $\partial_{12}^{2} q(b, r)<0$ if and only if

$$
\left(\partial_{22}^{2} H \partial_{1} H-\partial_{12}^{2} H \partial_{2} H\right)(b, q(b, r))<0
$$

Now we compute each of the terms $\partial_{2} H, \partial_{1} H, \partial_{12}^{2} H$ and $\partial_{22}^{2} H$ in the left hand side of (S25) explicitly in terms of the density $f_{\eta}$ of the noise difference $\eta=\varepsilon_{i}-\varepsilon_{j}$. Note that $\xi_{b}=\eta+(\xi \vee b)$ where $\xi:=Z_{i}-Z_{j}$. Then we have for $\varepsilon>0$ (see Figure S2)

$$
\begin{aligned}
& H(b+\varepsilon, a)-H(b, a)=\mathbb{P}(\eta+\xi \vee(b+\varepsilon) \leq a)-\mathbb{P}(\eta+\xi \vee b \leq a) \\
& =\left\{\begin{array}{ll}
0 & \text { if } \xi>b+\varepsilon \\
\mathbb{P}(\eta+b+\varepsilon \leq a)-\mathbb{P}(\eta+b \leq a) & \text { if } \xi \leq b \\
\mathbb{P}(\eta+b+\varepsilon \leq a)-\mathbb{P}(\eta+\xi \leq a) & \text { if } b \leq \xi \leq b+\varepsilon
\end{array}\right.
\end{aligned}
$$

Since $\eta$ and $\xi$ are independent, this implies

$$
H(b+\varepsilon, a)-H(b, a)=-\mathbb{P}(\xi \leq b) \mathbb{P}(a-b-\varepsilon \leq \eta \leq a-b)+O\left(\varepsilon^{2}\right)
$$

Hence,

$$
\partial_{1} H(b, a)=\lim _{\varepsilon \downarrow 0} \frac{H(b+\varepsilon, a)-H(b, a)}{\varepsilon}=-\mathbb{P}(\xi \leq b) f_{\eta}(a-b)
$$

A similar calculation gives (see Figure S3)

$$
\begin{aligned}
\partial_{2} H(b, a) & =\lim _{\varepsilon \downarrow 0} \frac{H(b, a+\varepsilon)-H(b, a)}{\varepsilon}=\mathbb{P}(\xi \leq b) f_{\eta}(a-b)+\int_{b}^{\infty} f_{\eta}(a-x) f_{\xi}(x) d x \\
& =\left(-\partial_{1} H+A\right)(b, a)
\end{aligned}
$$

![img-16.jpeg](img-16.jpeg)

Fig. S2. $H(b+\varepsilon, a)-H(b, a)$ is the probability that $(\xi, \eta)$ lies in the shaded regions (light and dark shaded)
![img-17.jpeg](img-17.jpeg)

Fig. S3. $H(b, a+\varepsilon)-H(b, a)$ is the probability that $(\xi, \eta)$ lies in the shaded region (light and dark shaded)

Thus,

$$
\begin{aligned}
\partial_{12}^{2} H(b, a) & =-\mathbb{P}(\xi \leq b) f_{\eta}^{\prime}(a-b) \\
\partial_{22}^{2} H(b, a) & =\mathbb{P}(\xi \leq b) f_{\eta}^{\prime}(a-b)+\int_{b}^{\infty} f_{\eta}^{\prime}(a-x) f_{\xi}(x) d x \\
& =-\partial_{12}^{2} H(b, a)+\int_{b}^{\infty} f_{\eta}^{\prime}(a-x) f_{\xi}(x) d x \\
& =\left(-\partial_{12}^{2} H+A_{a}\right)(b, a)
\end{aligned}
$$

Now we have

$$
\begin{aligned}
& \left(\partial_{22}^{2} H \partial_{1} H-\partial_{12}^{2} H \partial_{2} H\right)(b, a)=\left(A_{a} \partial_{1} H-A \partial_{12}^{2} H\right)(b, a) \\
= & \mathbb{P}(\xi \leq b)\left(-f_{\eta}(a-b) \int_{b}^{\infty} f_{\eta}^{\prime}(a-x) f_{\xi}(x) d x+f_{\eta}^{\prime}(a-b) \int_{b}^{\infty} f_{\eta}(a-x) f_{\xi}(x) d x\right)
\end{aligned}
$$

Thus, (S25) holds if and only if
$-f_{\eta}(q(b, r)-b) \int_{b}^{\infty} f_{\eta}^{\prime}(q(b, r)-x) f_{\xi}(x) d x+f_{\eta}^{\prime}(q(b, r)-b) \int_{b}^{\infty} f_{\eta}(q(b, r)-x) f_{\xi}(x) d x<0$.
Now we need to show that for each constant $B$, there exists an $r^{*}(B)>0$ such that for all $r<r^{*}$ and $b \leq B$, (S29) holds. Fix the constant $B$. Since the noise $\varepsilon$ has no upper bound, $\eta$ and hence $\xi_{b}$ have unbounded support below. For each fixed $b, q(b, r) \rightarrow-\infty$ as $r \downarrow 0$. Therefore, there exists some sufficiently small $r^{*}>0$ such that for all $r<r^{*}$, $q(b, r)-b$ is a large negative number. Fix such an $r^{*}$. Therefore, for all $x>b, q(b, r)-x$ is a large negative number. This allows us to use Lemma S6 to make the left hand side of (S29) explicit. In particular, by (S16), as $t \rightarrow \infty$,

$$
f_{\eta}(t)=K_{1} t^{1-p / 2} e^{-K t^{p}}(1+o(1)), \quad f_{\eta}^{\prime}(t)=f_{\eta}(t)\left(-K p t^{p-1}+(1-p / 2) t^{-1}\right)(1+o(1))
$$

Setting $t=|x-q(b, r)|$ and use the fact that $f_{\eta}$ is symmetric, $f_{\eta}(q(b, r)-x)=f_{\eta}(|x-$ $q(b, r) \mid)$, we have

$$
\begin{aligned}
& -f_{\eta}(q(b, r)-b) \int_{b}^{\infty} f_{\eta}^{\prime}(q(b, r)-x) f_{\xi}(x) d x+f_{\eta}^{\prime}(q(b, r)-b) \int_{b}^{\infty} f_{\eta}(q(b, r)-x) f_{\xi}(x) d x \\
= & f_{\eta}(q(b, r)-b) \int_{b}^{\infty}\left[-K p(x-q(b, r))^{p-1}+\left(1-\frac{p}{2}\right)(x-q(b, r))^{-1}\right] f_{\eta}(q(b, r)-x) f_{\xi}(x) d x \\
& +\left[K p(b-q(b, r))^{p-1}-\left(1-\frac{p}{2}\right)(b-q(b, r))^{-1}\right] f_{\eta}(q(b, r)-b) \int_{b}^{\infty} f_{\eta}(q(b, r)-x) f_{\xi}(x) d x \\
= & f_{\eta}(q(b, r)-b) \int_{b}^{\infty} A(x) f_{\eta}(q(b, r)-x) f_{\xi}(x) d x
\end{aligned}
$$

where
$A(x)=\left(K p\left[(b-q(b, r))^{p-1}-(x-q(b, r))^{p-1}\right]-(1-p / 2)\left[(b-q(b, r))^{-1}-(x-q(b, r))^{-1}\right]\right)$.
If $p \in(1,2]$, since $x>b$, the first term $(b-q(b, r))^{p-1}-(x-q(b, r))^{p-1}$ and the second term $-(1-p / 2)\left[(b-q(b, r))^{-1}-(x-q(b, r))^{-1}\right]$ are both negative. If $p>2$, since $x>b \gg q(b, r)$ the first term $(b-q(b, r))^{p-1}-(x-q(b, r))^{p-1}$ is a large negative number. Since $q(b, r)$ is a large negative number, $b-q(b, r)$ is a large positive number, so $(b-q(b, r))^{-1},(x-q(b, r))^{p-1}<1$. Thus $\left|(1-p / 2)\left[(b-q(b, r))^{-1}-(x-q(b, r))^{-1}\right]\right| \leq$ $|1-p / 2|$. For this reason, $A(x)<0$ for all $p>1, x>b$, while $f_{\eta}, f_{\xi}>0$ everywhere as they are densities. Thus the integral is negative, that is, (S29) holds for all $r \in\left(0, r^{*}\right)$ and $b \leq B$, as needed.

Below we denote $c h(j)$ the child of node $j$.
Corollary S1. Under the Gumbel-Gaussian noise model, there exists an $r_{1}^{*}>0$ such that: for all $0<\underline{r}<\bar{r}<r_{1}^{*}$, for all $j \in V$ and for all $i^{\prime} \in V, i^{\prime} \neq j, c h(j)$ and either $j \rightsquigarrow i^{\prime}$ or $j \not i^{\prime}$, then

$$
w_{c h(j) j}<w_{i^{\prime} j}
$$

Proof. It is sufficient to show that the above holds with some constant $r^{*}(j)$ for each fixed $j$, then set $r_{1}^{*}=\min _{j} r^{*}(j)$. Fix $j$ and $i^{\prime}$ as stated. Let $b^{*}:=\beta\left(\log \theta_{j}-\log \left(\theta_{c h(j)}-\theta_{j}\right)\right)$, and let $r^{*}(j)$ be the constant $r^{*}$ that works for $B=b^{*}$ in Lemma S7. By Proposition S1,

$$
w_{c h(j) j}=q\left(b^{*}, \bar{r}\right)-q\left(b^{*}, \underline{r}\right)
$$

Now we consider two cases.
Case 1: $i^{\prime}$ is a descendant of $j$, that is, $j \rightsquigarrow i^{\prime}$. Then by Proposition S1,

$$
w_{j i^{\prime}}=q(b, \bar{r})-q(b, \underline{r})
$$

where $b=\beta\left(\log \theta_{j}-\log \left(\theta_{i^{\prime}}-\theta_{j}\right)\right)$. But since $i^{\prime} \neq c h(j), i^{\prime}$ must be a descendant of $i$ as well. By definition (S11), $i \rightsquigarrow i^{\prime}$ implies $\theta_{i^{\prime}}>\theta_{i}$. Therefore, $b<b^{*}$, so by (S19), $w_{i j}<w_{i^{\prime} j}$. This concludes case 1.
Case 2: $j \not i^{\prime}$. Then by Proposition S1,

$$
w_{i^{\prime} j}=q(-\infty, \bar{r})-q(-\infty, \underline{r})
$$

Since $-\infty<b^{*}$, so by (S19), $w_{i j}<w_{i^{\prime} j}$. This concludes case 2 .
Lemma S8. There exists some $r_{2}^{*}>0$ such that for all $0<\underline{r}<\bar{r}<r_{2}^{*}$, for all $j \in V$, $i^{\prime} \rightsquigarrow j$ implies

$$
q(b, \bar{r})-q(b, \underline{r})<q\left(b^{\prime}, 1-\underline{r}\right)-q\left(b^{\prime}, 1-\bar{r}\right)
$$

where $b=\beta\left(\log \theta_{j}-\log \left(\theta_{c h(j)}-\theta_{j}\right)\right)$ and $b^{\prime}=\beta\left(\log \theta_{i^{\prime}}-\log \left(\theta_{j}-\theta_{i^{\prime}}\right)\right)$. In particular, if $i^{\prime} \rightsquigarrow j$, then for all quantile levels $\underline{r}, \bar{r}$ such that $0<\underline{r}<\bar{r}<r_{2}^{*}$,

$$
w_{c h(j) j}<w_{i^{\prime} j}
$$

Proof. It is sufficient to prove that (S31) holds for each fixed $j$ with some constant $r_{2}^{*}(j)$, and then set $r_{2}^{*}=\min _{j} r_{2}^{*}(j)$. Fix $j$. First, we do some manipulations on (S31) to relate it to the partial derivatives of $H$. Define

$$
\mathcal{B}:=\left\{\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right): i, j \in V, j \rightsquigarrow i\right\}
$$

Note that (S31) is equivalent to

$$
\partial_{2} q(b, r)<\partial_{2} q\left(b^{\prime}, 1-r\right) \quad \text { for all } r \in\left(0, r_{2}^{*}\right) \text { and for all } b, b^{\prime} \in \mathcal{B}
$$

By (S21), we have

$$
\partial_{2} q(b, r)-\partial_{2} q\left(b^{\prime}, 1-r\right)=\frac{1}{\partial_{2} H(b, q(b, r))}-\frac{1}{\partial_{2} H\left(b^{\prime}, q\left(b^{\prime}, 1-r\right)\right)}
$$

By (S28), $\partial_{2} H>0$ point-wise, thus our goal now is to show that for sufficiently small $r$,

$$
\partial_{2} H\left(b^{\prime}, q\left(b^{\prime}, 1-r\right)\right)-\partial_{2} H(b, q(b, r))<0
$$

for all $b, b^{\prime} \in \mathcal{B}$, that is, some finite set of constants. We shall do this by writing $\partial_{2} H$ in terms of the tail densities $f_{\eta}$ and $f_{\xi}$ using (S28), then apply Lemma S6. Indeed, by (S28),

$$
\partial_{2} H\left(b^{\prime}, a\right)=\mathbb{P}\left(\xi \leq b^{\prime}\right) f_{\eta}\left(a-b^{\prime}\right)+\int_{b^{\prime}}^{\infty} f_{\eta}(a-x) f_{\xi}(x) d x
$$

By Lemma S6, $f_{\xi}$ has heavier tail than $f_{\eta}$, so for $a \rightarrow \infty$, the main contribution from $\int_{b^{\prime}}^{\infty} f_{\eta}(a-x) f_{\xi}(x) d x$ comes from $f_{\xi}(a)$. That is, for large $a$, there exists some constant $b_{1}>0$ such that

$$
\partial_{2} H\left(b^{\prime}, a\right)>b_{1} f_{\xi}(a)
$$

Now we consider $\partial_{2} H(b,-a)$. From (S28),

$$
\partial_{2} H(b,-a)=\mathbb{P}(\xi \leq b) f_{\eta}(-a-b)+\int_{b}^{\infty} f_{\eta}(-a-x) f_{\xi}(x) d x
$$

Again, for large $a$

$$
f_{\eta}(-a-x)<f_{\eta}(-a-b) \text { for all } x>b
$$

Therefore, we can bound the second term above as

$$
\int_{b}^{\infty} f_{\eta}(-a-x) f_{\xi}(x) d x<f_{\eta}(-a-b) \int_{b}^{\infty} f_{\xi}(x) d x=f_{\eta}(-a-b) \mathbb{P}(\xi>b)
$$

Adding in the first term, we get that for large $a$,

$$
\partial_{2} H(b,-a)<f_{\eta}(-a-b)
$$

Combining this with (S36) and noting that $\partial_{2} H(b, a)$ is just the density $f_{\xi_{b}}(a)$ of $\xi_{b}$, we get

$$
f_{\xi_{b}}(-a)=O\left(f_{\xi_{b^{\prime}}}(a)\right)
$$

for all $b, b^{\prime} \in \mathcal{B}$ and $a$ large. Now $\partial_{2} H(b, q(b, r))$ is just the slope of the cdf of $f_{\xi_{b}}$ at its $r$-quantile. Therefore, for $r$ small, by (S37), $\partial_{2} H\left(b^{\prime}, q\left(b^{\prime}, 1-r\right)\right)<\partial_{2} H(b, q(b, r))$ which proves (S35) and thus completes the proof of (S31). The last statement follows from Proposition S1, case (3).

Corollary S2. If the true quantiles are known, then there exist some choices of $(\underline{r}, \bar{r})$ such that the lower quantile gap matrix $W$ satisfies the conditions of Lemma S5, that is, (S8) and (S9).

Proof. Set $r^{*}=\min \left(r_{1}^{*}, r_{2}^{*}\right)$ where $r_{1}^{*}$ comes from Corollary S1, and $r_{2}^{*}$ comes from Lemma S8. Let $(\underline{r}, \bar{r})$ be any pair such that $0<\underline{r}<\bar{r}<r^{*}$, and let $W$ be the corresponding lower quantile gap matrix with the true quantiles. Then (S9) holds because of (S32) and the fact that for the root $r$ of the root-directed spanning tree, $i^{\prime} \rightsquigarrow r$ holds for every $i^{\prime} \neq r$. Corollary S1 and Lemma S8 together guarantee that (S8) is satisfied for $W$.

# Proof of Theorem 1 for the lower quantile gap 

Fix $(\underline{r}, \bar{r})$ such that Corollary S2 holds, and let $W$ be the corresponding lower quantile gap matrix derived from the true quantiles. Let $W_{n}$ be the lower quantile gap matrix derived from an empirical distribution with sample size $n$. Note that the set of 'good' matrices, that is, those that satisfy Lemma S5, is an open polyhedral cone in the space of matrices $\mathbb{R}^{V \times V}$, since the conditions of 'goodness' is a set of linear inequalities. By Corollary S2, $W$ is a point inside this cone. Recall that empirical quantiles converge a.s. as $n \rightarrow \infty$ to the true ones for continuous limit distributions, hence, also the empirically-derived lower quantile gap converges a.s.. By a union bound over the $d^{2}-d$ possible edge pairs $(i, j)$, for any metric $D$ (e.g. induced by a matrix norm), we thus have $D\left(W_{n}, W\right) \rightarrow 0$ a.s. The Consistency Theorem then follows from Lemma S5.

## S3.2. Proof of Theorem 1 for the quantile-to-mean gap

Our proof follows the same structure as the previous proof, but the calculations in all steps are a bit simpler, since there is only one quantile parameter to deal with. First, expectation is linear, so we work with empirical means $\bar{X}_{i}$ for $i \in V$ and mention in passing that they converge a.s. to the true mean as $n \rightarrow \infty$. The analogue of Proposition S1 is the following.

Proposition S2. Fix $\underline{r} \in[0,1)$, and let $w_{i j}$ be the quantile-to-mean gap (S7). Assume the Gumbel-Gaussian noise model. Then
(1) If $j \rightsquigarrow i$, then $w_{i j}=-q_{\underline{r}}\left(\xi^{b}\right)$ where $b=\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)$.
(2) If $j \not i$, then $w_{i j}=-q_{\underline{r}}\left(\xi^{b}\right)$ where $b=-\infty$.
(3) If $i \rightsquigarrow j$, then $w_{i j}=q_{1-\underline{r}}\left(\xi^{b}\right)$ where $b=\beta\left(\log \theta_{i}-\log \left(\theta_{j}-\theta_{i}\right)\right)$.

Instead of a lengthy proof of the analog of Proposition S1 by duplicating arguments, we provide some informal reasoning. We check that our quantile-to-mean gaps $w_{i j}$ satisfy the inequalities of Corollary S1 and Lemma S8 by first checking the noise-free case, where $\varepsilon_{i} \equiv \varepsilon_{j} \equiv 0$. We consider the three cases of Proposition S2.
(a) If $j \rightsquigarrow i$. Then $\xi^{b}$ has a left-most atom at $b=\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)$, so for sufficiently small $r, w_{i j}=-b$. This is minimal when $i$ is a direct descendant of $j$. So Corollary S1 for the case $j \rightsquigarrow i$ holds in the noise-free case.
(b) If $j \not i$. Then $\xi^{b}$ has no left-most atom, so as $\underline{r} \downarrow 0, q_{\underline{r}}\left(\xi^{b}\right) \rightarrow-\infty$, so $w_{i j} \rightarrow \infty$. So Corollary S1 also holds in the noise-free case for the remaining case, $j \not i$.
(c) If $i \rightsquigarrow j$. Then $\xi^{b}$ has a left-most atom, but no right-most atom. Again, as $\underline{r} \downarrow 0$, $q_{1-\underline{r}}\left(\xi^{b}\right) \rightarrow \infty$, so $w_{i j} \rightarrow \infty$. Thus, Lemma S8 holds in the noise-free case.

Now we consider the effect of noise. We send $\underline{r} \downarrow 0$. As long as $\eta:=\varepsilon_{i}-\varepsilon_{j}$ has lighter tail than $Z_{i}-Z_{j}$, as guaranteed by Lemma S6, we have the following:

- In case (1), $q_{\underline{r}}\left(\xi^{b}\right)$ is dominated by the lower tail of $\eta$.
- In case (2), $q_{\underline{r}}\left(\xi^{b}\right)$ is dominated by the lower tail of $Z_{i}-Z_{j}$ and, in particular, is going to $-\infty$ at a faster rate than case (1).

- In case (3), $q_{1-\underline{r}}\left(\xi^{b}\right)$ is dominated by the upper tail of $Z_{i}-Z_{j}$, and in particular, is going to $\infty$ at a faster rate than case (1).

This domination calculation is the same calculation done in the proof of Lemma S8. The above says that for fixed $j$, for small enough $\underline{r}$, the minimum of $\left\{w_{i j}: i \neq j, i \in V\right\}$ lies in case (1). Within case (1), we want to make sure that, if $w_{i j}$ is smallest, then $i$ is the child of $j$. Indeed, write

$$
\xi^{b}=\varepsilon_{i}-\varepsilon_{j}+\xi_{i j}^{\prime}
$$

where $\xi_{i j}^{\prime}=\left(Z_{i}-Z_{j}\right) \vee\left(\beta\left(\log \theta_{j}-\log \left(\theta_{i}-\theta_{j}\right)\right)\right)$. For fixed $j,\left(\xi_{i j}^{\prime}: j \rightsquigarrow i\right)$ is a particular family of distribution indexed by $i$. By a decoupling argument, it is sufficient to show that $q_{\underline{r}}\left(\xi_{i j}^{\prime}\right)$ is smallest when $i$ is the child of $j$. But this reduces to the noise-free case, which we already proved above. This finishes the proof of Theorem 1 for the quantile-to-mean gap.

# S4. Supplemental Figures for Section 4.2 

Below we present the figures analogous to Figure 11 of the Paper for the different data sets of the Colorado river network. For certain values $\alpha$, the boxplots in Figures S4 and S5 degenerate, indicating that the $25 \%$ and $75 \%$ quantiles of the resampled data match, i.e. $50 \%$ of the data settle upon the same value of the metric. The very large boxes for high $\alpha$ indicate the uncertainty in the small data sets for computations of the metrics.
![img-18.jpeg](img-18.jpeg)

Fig. S4. Metrics nSHD, TPR, FDR and FPR for the Top sector of the Colorado network and varying parameters $\alpha$. For detailed explanations see Figure 11 of the Paper.

![img-19.jpeg](img-19.jpeg)

Fig. S5. Metrics nSHD, TPR, FDR and FPR for the Middle sector of the Colorado network and varying parameters $\alpha$. For detailed explanations see Figure 11 of the Paper.

![img-20.jpeg](img-20.jpeg)

Fig. S6. Metrics nSHD, TPR, FDR and FPR for the Bottom sector of the Colorado network and varying parameters $\alpha$. For detailed explanations see Figure 11 of the Paper.

![img-21.jpeg](img-21.jpeg)

Fig. S7. Metrics nSHD, TPR, FDR and FPR for Bottom150 of the Colorado network and varying parameters $\alpha$. For detailed explanations see Figure 11 of the Paper.

# S5. Supplemental Figures for Section 5 

Below we visualize the performance measures nSHD and TPR as defined in equation (1) of the Paper from simulations of settings (2) and (3) of Section 5 of the Paper.
![img-22.jpeg](img-22.jpeg)

Fig. S8. Mean nSHD for the weak dependence setting (2) and different graph sizes. For detailed explanations, see Figure 13 of the Paper.
![img-23.jpeg](img-23.jpeg)

Fig. S9. Mean TPR for the weak dependence setting (2) and different graph sizes. For detailed explanations, see Figure 13 of the Paper.

![img-24.jpeg](img-24.jpeg)

Fig. S10. Mean nSHD for the mixed distribution setting (3) and different graph sizes. For detailed explanations, see Figure 13 of the Paper.
![img-25.jpeg](img-25.jpeg)

Fig. S11. Mean TPR for the mixed distribution setting (3) and different graph sizes. For detailed explanations, see Figure 13 of the Paper.
