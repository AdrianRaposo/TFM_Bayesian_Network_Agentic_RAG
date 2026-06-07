# High-order dynamic Bayesian Network learning with hidden common causes for causal gene regulatory network 

Leung-Yau Lo ${ }^{1 *}$, Man-Leung Wong ${ }^{2}$, Kin-Hong Lee ${ }^{1}$ and Kwong-Sak Leung ${ }^{1}$


#### Abstract

Background: Inferring gene regulatory network (GRN) has been an important topic in Bioinformatics. Many computational methods infer the GRN from high-throughput expression data. Due to the presence of time delays in the regulatory relationships, High-Order Dynamic Bayesian Network (HO-DBN) is a good model of GRN. However, previous GRN inference methods assume causal sufficiency, i.e. no unobserved common cause. This assumption is convenient but unrealistic, because it is possible that relevant factors have not even been conceived of and therefore un-measured. Therefore an inference method that also handles hidden common cause(s) is highly desirable. Also, previous methods for discovering hidden common causes either do not handle multi-step time delays or restrict that the parents of hidden common causes are not observed genes.


Results: We have developed a discrete HO-DBN learning algorithm that can infer also hidden common cause(s) from discrete time series expression data, with some assumptions on the conditional distribution, but is less restrictive than previous methods. We assume that each hidden variable has only observed variables as children and parents, with at least two children and possibly no parents. We also make the simplifying assumption that children of hidden variable(s) are not linked to each other. Moreover, our proposed algorithm can also utilize multiple short time series (not necessarily of the same length), as long time series are difficult to obtain.
Conclusions: We have performed extensive experiments using synthetic data on GRNs of size up to 100, with up to 10 hidden nodes. Experiment results show that our proposed algorithm can recover the causal GRNs adequately given the incomplete data. Using the limited real expression data and small subnetworks of the YEASTRACT network, we have also demonstrated the potential of our algorithm on real data, though more time series expression data is needed.

Keywords: Gene regulatory network, High-order dynamic Bayesian Network, Hidden common cause, Causality inference

## Background

Inferring gene regulatory network (GRN) has been an important topic in Bioinformatics, owing to the important role it plays in the functioning of the cell. In the cell, genes are transcribed and subsequently translated into proteins, some of which are transcription factors (TFs) which trigger or inhibit the transcription of other gene(s). The transcription and translation, however, take time and

[^0]may have delays due to other reasons [1-4]. These delays have been known to affect the network stability, or cause oscillations [5-8]. Therefore, the GRN could be modeled as a directed network where each directed link is labeled with the delay, representing the regulation of a gene to a target gene.
Rather than experimentally determining the regulatory targets of each Transcription Factor (TF) in an expensive and time-consuming way, many computational methods attempt to infer the GRN from high-throughput microarray or RNA-seq gene expression data, which can measure the expression of thousands of genes at the same time, and


[^0]:    *Correspondence: lylo@cse.cuhk.edu.hk
    ${ }^{1}$ Department of Computer Science and Engineering, The Chinese University of Hong Kong, Shatin, Hong Kong
    Full list of author information is available at the end of the article

allow time series expression data to be obtained when this is done for a number of time points.

However, to our knowledge, the previous GRN inference methods all implicitly make the assumption of *causal sufficiency*, i.e. there are no unobserved common cause, which is convenient but unrealistic. For example, miRNAs were previously not thought to take important roles in gene regulation. It is in principle impossible to be certain that all relevant factors or common causes have been measured, because factors that are not even conceived of cannot be measured. Therefore an inference method that also handles hidden common cause(s) is highly desirable.

### Gene network inference

Many GRN inference algorithms and models have been proposed, with different levels of details by labeling the edges with different information, see [9, 10] for surveys of GRN modelling and [11] for a survey on GRN inference algorithms for microarray expression data.

Some methods infer only an undirected network, for example Relevance network [12], ARACNE [13] and C3NET [14], all of which use mutual information as a measure of association between genes. Some infer a directed network, but without labeling the edges with time delays, e.g. [15]. Static Bayesian Network (BN) is sometimes used to model GRN, e.g. in [16]. But the downside of static BN is that no cycles are allowed, and no time delays are taken into account.

Some algorithms consider delay of only one time step, e.g. [17] which uses association rule mining; [18] which uses the classical Boolean network; [19] which uses Gaussian process for Bayesian inference of an Ordinary Differential Equation (ODE) model discretized in time; and DELDBN [20], which combines ODE model with local Bayesian analysis. In contrast to static BN, dynamic Bayesian Network (DBN) models the joint distribution of some random variables at different time points, and allows time delays. First-Order DBN allows time delays of only one time step, e.g. [21] and GlobalMIT [22].

On the other hand, High-Order DBN (HO-DBN) allows delays of multiple time steps. Many HO-DBN models are discrete and ignore intra-slice edges (i.e. no instantaneous effects), and are learnt by optimizing a score on candidate structure. Since BN learning is NP-hard [23], some DBN learning algorithms use heuristic or stochastic optimization such as simulated annealing, as in Banjo [24] (updated version allows multi-step delays); genetic algorithm, as in [25]; and greedy heuristic search in MMHO-DBN [26] (in case the number of parents is large, and exhaustive search is used otherwise). After [27] had shown it is possible to globally optimize Minimum Description Length (MDL) score [28] and Bayesian-Dirichlet equivalent (BDe) score [29] in polynomial time for certain BN and DBN model, the technique has been adapted to globally optimize the MIT score [30] in GlobalMIT for FO-DBN and GlobalMIT+ [31] for HO-DBN. GlobalMIT* is a heuristic and faster version of GlobalMIT+. Although for small or medium sized networks, GlobalMIT+ and GlobalMIT* could globally optimize the score in reasonable time, when the number of genes and time points increase, the practical time needed could still be long, as the order of the polynomial depends on the number of time points. Therefore, a good heuristic HO-DBN learning method that strikes a good balance between effectiveness and efficiency is still a useful complement.

On the continuous side, there are not many algorithms that handle multi-step delays, examples are TD-ARACNE [32], which is an extension of ARACNE; DD-lasso [33], which uses lasso [34]; and CLINDE [35], which extends the PC algorithm [36] with time delays.

### Hidden common cause

The above methods ignore the issue of hidden common cause(s) by (implicitly) assuming *causal sufficiency*, i.e. all common causes have been observed. Inferring hidden common cause(s) is an important topic in causality inference, because ignoring them may result in misleading causal relationships, as illustrated in Fig. 1, where some nodes are wrongly thought to be causally linked.

An early work is [37], which formulates the problem as determining the constraints on the variance-covariance matrix of observed data, and then searching for a causal structure to explain the constraints. Some works assume the presence of hidden common cause of observed variables, but only indicate that some *may* have hidden common cause, and focus on the relationships between observed variables instead. The Causal Inference (CI) and Fast Causal Inference (FCI) algorithms [36] are extensions of the PC algorithm to handle the causally insufficient case; similarly the IC* algorithm [38] is an extension of the IC algorithm. Both CI, FCI and IC* give only a partially ordered graph, where some edges may remain undirected, and some are labeled to mean the two genes may have

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Illustration of possible misleading causal relationships if hidden common cause is ignored. The numbers are the delays. The grey circle is the hidden common cause. Since the children and parents of the hidden common cause are associated, they may be mistakenly thought to be directly linked

hidden common cause. Eichler [39] is a Granger-causality based method that learns a mixed graph from time series data, where directed edges represent direct causal relationship, and dashed edges represent relationship due to hidden common cause. Pellet and Elisseeff [40] is an extension of the FCI algorithm and does not use time series data. Stochastic differential equation model (discretized in time) is used in [41], where hidden variables are assumed only to more accurately estimate the relationship between observed variables, using a convex optimization based method. In [42], a Satisfiability problem is formulated from the d-separation and d-connection information as provided by conditional tests, which is then incrementally solved to attempt to recover the dependency structure between observed variables, and some may be indicated to have latent variables, and some edges may be marked as "unknown" if the given information is insufficient for determining whether it is present or not.

While the above do not have any hidden common cause in the output, some works label predicted hidden common cause(s), but any hidden common cause can only have other hidden variables, but not observed variables as parents. Silva [43, 44] are examples in this direction, where observed variables depend linearly on its parents (either hidden or observed), and hidden variables can depend nonlinearly on its parents (only hidden variables). In [45], a linear Bayesian Network is learnt, but it is assumed that there are no edges among observed variables, and that the hidden variables are linearly independent.

Some works are less restrictive and allow the hidden variables to have observed variables as parents. Boyen et al. [46] uses a FO-DBN model, and is based on the observation that ignoring hidden variable in DBN usually results in violation of Markov property. The algorithm therefore tries to find non-markovian correlations (those across more than one time step) and try to explain them by introducing hidden variable. This work, however, evaluates the likelihood on the testing set rather than how close the resulting dependency structure is to the assumed true causal structure.

In [47], a discrete BN with hidden variables without time delays is learnt, where hidden variables are assumed to have observed variables as parents and children. It is closer to the work in this paper in that it has less restriction on the parents of the hidden common cause(s) than previously mentioned methods, but it does not handle time delays. It is motivated with the observation that the inferred dependency of the observed variables (the parents and children of the hidden variable) will usually be overly complicated, with many connections, when the hidden variable is not taken into account (see Fig. 1). Therefore, they guess the position of the hidden variable(s) and its local structure by finding semi-clique(s). A semi-clique
is a subset of nodes where each node in the subset is connected to more than half of the nodes in the subset. After that adjustments are made by explicitly linking the variables of the semi-clique with the introduced hidden variable and this local structure is then fine-tuned by Structural-EM (SEM) [48]. This work also focuses on the likelihood in the evaluation instead of the inferred structure. The use of semi-clique as structural signature also places some restrictions on the subnetwork surrounding the hidden variable(s), e.g. a hidden variable must have parent(s), which are observed variable(s), and the total number of parents and children of a hidden variable must be at least three, because the smallest semi-clique has size three. Elidan and Friedman [49] complements [47] and focuses on learning the dimensionality (the number of states) of hidden variables.

In short, HO-DBN learning methods that can handle multi-step time delays such as GlobalMIT* do not handle hidden common cause(s), and hidden common cause learning algorithms do not handle multi-step time delays, and those without time delays are restricted to acyclic networks. In other words, to our knowledge, no previous methods handle multi-step time delay and learn hidden common cause(s) at the same time.

## Objective

In this paper, we want to develop a HO-DBN learning algorithm that can infer also hidden common cause(s) from discrete time series expression data, with some assumptions on the conditional distribution, but is less restrictive than the above mentioned methods. Here, we focus on the discrete case, because combinatorial regulation could be easily modeled by HO-DBN.

We assume that there is a $d$-th order (the maximum delay is $d$ ) stationary HO-DBN that is of interest, where a small but unknown number of common cause(s) are not observed. Each hidden variable has only observed variables as children and parents, with at least two children and possibly no parents. We also make the simplifying assumption that the children of unobserved variable(s) are not linked to each other, because it is difficult to differentiate whether the high association between two children are solely due to the hidden common cause, or due to both the hidden common cause and direct link between the two children. As the prior network is difficult to learn, and the transition network is of the main interest, our objective is to infer the transition network of the HO-DBN from the discrete time series of the observed variables. Moreover, it is desirable that the algorithm be capable of utilizing multiple short time series (not necessarily of the same length), as long time series are difficult to obtain. To our knowledge, previous works either make much more restrictive assumptions or ignore time delays.

## Methods

The motivating idea of our proposed method is that when a common cause is hidden, the parents of its children will not be determined correctly, and will probably be wrongly predicted to be the parent(s) of the hidden cause, or other children of the hidden cause, as illustrated in Fig. 1. In order to remedy this, the "anomaly" has to be recognized first. The overall strategy is to first learn an initial GRN while ignoring possible hidden common cause, then to detect the presence of hidden common cause(s), and estimate any detected hidden common cause. This overall strategy is similar to that of [47]. But while [47] uses semiclique as structural signature, and [46] uses correlation across more than one time step as clue of "anomaly", in this paper, we propose to make assumption on the conditional distribution for this purpose. The idea is that when the parents of a gene are wrongly determined, the conditional distribution will be different from expected. We could predict the genes with hidden common cause using this clue. After that, by the fact that genes with common parent should have high association, the suspected genes could be clustered, and one hidden common cause could be estimated for each cluster with size at least two. Unlike [47], we estimate hidden common cause(s) with simple EM, instead of Structural-EM.

The overall flow of the proposed method is given in Fig. 2. The steps are 1) infer an initial GRN of the observed genes, 2) determine the genes with hidden common cause(s) by the estimated conditional distributions, 3) estimate the hidden common cause(s), 4) re-learn the GRN after estimation of hidden common cause(s). The program code can be obtained at https://github.com/ peter19852001/hcc_dclinde. We first describe the data and model assumed in this paper, then describe each step in more details, where we first describe the case with one time series, and later we describe the case of multiple time series in a separate subsection.

## Model and data

The GRN model used in this paper is High-Order Dynamic Bayesian Network (HO-DBN) on $n+n_{h}$ random variables $\mathbf{X}_{t}=\left\{X_{1, t}, \ldots, X_{n+n_{h}, t}\right\}$ at different time points $t=1, \ldots, T$. Each $X_{i, t}$ represents the expression of gene $i$ at time $t$, where $n$ of them are observed, and $n_{h}$ are hidden. We assume that the DBN satisfies the $d$-th order Markov property:

$$
\mathrm{P}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}, \mathbf{X}_{t-2}, \ldots, \mathbf{X}_{1}\right)=\mathrm{P}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}, \ldots, \mathbf{X}_{t-d}\right) \text { for any } t
$$

The order $d>1$ is the maximum delay. We also assume that the DBN is stationary, i.e. the dependency $\mathrm{P}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}, \ldots, \mathbf{X}_{t-d}\right)$ is independent of $t$. Therefore, the joint distribution can be factorized as:

$$
\mathrm{P}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{T}\right)=\mathrm{P}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{d}\right) \prod_{t=d+1}^{T} \mathrm{P}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}, \ldots, \mathbf{X}_{t-d}\right)
$$

The $\mathrm{P}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{d}\right)$ is the prior network, which needs many independent samples to estimate, so the focus is usually on the transition network $\mathrm{P}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}, \ldots, \mathbf{X}_{t-d}\right)$. Assuming stationary DBN, the transition network could
![img-1.jpeg](img-1.jpeg)

Fig. 2 Overall Flow of the Proposed Algorithm. The steps are: 1) infer an initial GRN, 2) identify the genes with hidden common cause, 3) estimate the hidden common cause(s), which involves clustering and EM, 4) re-learn the GRN after estimation of the hidden common cause(s)

be represented as a multi-graph of $n+n_{h}$ nodes (representing the $n+n_{h}$ genes), where an edge $i \rightarrow j$ is labeled with a delay $\tau_{i j} \geq 0$, meaning that $X_{j, t}$ depends on $X_{i, t-\tau_{i j}}$. Note that there may be multiple edges from node $i$ to node $j$, but with different delays.

We make the following assumptions on the structure of the transition network:

- there are $n$ observed genes and $n_{h}$ hidden variable(s).
- $n_{h}$ is unknown, but $0 \leq n_{h}<n$ and $n_{h}$ is small.
- We also assume that the subgraph for which $\tau_{i j}=0$ (the instantaneous effects or intra-slice edges) is empty. This is commonly assumed, e.g. in [25], MMHO-DBN [26] and GlobalMIT+ [31]. This assumption is quite reasonable in GRN modeling, as the regulatory relationships invariably have delays. I.e. we assume that $\tau_{i j}>0$.
- each hidden variable has at least two observed genes as children.
- if a gene has a hidden parent, it has no other parents.
- children with the same hidden parent are not linked with each other.
- for each conditional distribution with $n_{s}$ states, one of the states has probability $p_{\text {bias }}$, and the other states each has probability of $\frac{1-p_{\text {bias }}}{n_{s}-1}$. That is, the dependency of a gene on its parent(s) is mostly a function, with some "noise" added. A higher value of $p_{\text {bias }}$ means a lower "noise" level.

The given data consists of $K$ discrete time series $\left\{x_{i}^{(k)}(t): 1 \leq i \leq n, 1 \leq t \leq T_{k}\right\}$ with equidistant time points for $1 \leq k \leq K$. The $K$ time series should be discretized in the same way, so that the states (e.g. 0,1 and 2 for low, average and high expression) are consistent in different time series.

## Initial GRN

For the purpose of identifying genes with hidden common cause(s), the first step is to obtain an initial GRN. In principle, any HO-DBN learning algorithm could be used. In our preliminary test (unpublished), we have adapted CLINDE [35] to discrete data to give D-CLINDE, which is a constraint-based method extending the PC algorithm [36] (in a similar way to CLINDE). We have shown that for large number of genes and time points, DCLINDE can be orders of magnitude faster than MMHODBN and GlobalMIT* (and consequently GlobalMIT+), while achieving slightly better learning performance than MMHO-DBN, and achieving $70-80 \%$ of the learning performance of GlobalMIT*. Therefore, D-CLINDE is a good complement to GlobalMIT* (and GlobalMIT+) for large networks and time points, when even GlobalMIT* would be too slow. Also, both D-CLINDE, GlobalMIT* and GlobalMIT+ can handle multiple time series, while

MMHO-DBN cannot. Therefore, in our current program, we allow the use of GlobalMIT*, GlobalMIT+ or DCLINDE for inferring the initial GRN. We briefly describe D-CLINDE, GlobalMIT+ and GlobalMIT* in the following.

## D-CLINDE

D-CLINDE is a constraint-based method, where conditional independence tests on the data constrain the possible causal structure. It consists of two stages. In stage 1 , independence tests ( $G^{2}$ test) are conducted on all gene pairs $i \rightarrow j$ for all possible delays up to a maximum delay. If the null hypothesis of the independence test is rejected (the score of the test is $-\log _{10}(p$-value), and the null hypothesis is rejected if the score is larger than a score threshold), the link with the associated delay is kept for stage 2. The default value for score threshold is 2 , corresponding to a $p$-value threshold of 0.01 . Note that there may be multiple delays for $i \rightarrow j$ after stage 1 . Stage 2 attempts to eliminate indirect effects based on the fact that if $x$ and $y$ are conditionally independent given a set of variable(s) $Z$ (not containing either $x$ or $y$ ), then there should not be a link between $x$ and $y$. So in stage 2 , we iteratively condition on $h=1$ neighbor for each link to see if a link could be pruned, then condition on $h=2$ neighbors for any remaining links, and so on up to $h=N_{0}$ for a given parameter $N_{0}$, with a default value of 2 . When performing a conditional test, the neighbors to be conditioned on are shifted using the delays estimated in stage 1 , and if the null hypothesis is not rejected (based on score and score threshold, and is similar to stage 1), the link is pruned.

## GlobalMIT+ and GlobalMIT*

GlobalMIT+ [31] is a method that globally maximizes the MIT score [30], which measures the mutual information between a gene and its parents (with delay), together with a penalty on the number of parents. The basic idea is that for each gene, we enumerate the parents (with the delays), starting from zero parents, then one parent, then two and so on, but with pruning to avoid having to enumerate all possible subsets.

The characteristics of the score (to be minimized) that allows effective optimization (in polynomial time) and pruning are:

- No need to check acyclicity: this allows the score to be calculated separately for each variable. Since GlobalMIT+ ignores instantaneous effects, so the network is always acyclic.
- Additivity: the score of a candidate network can be decomposed into the sum of the score of each gene. This greatly simplifies the search, and allows easy parallelization.
- Splitting: the score for each gene could be decomposed into a sum of complexity and accuracy

parts as $s(\mathbf{P a})=u(\mathbf{P a})+v(\mathbf{P a})$, where both $u(.) \geq 0$ and $v(.) \geq 0$, and that the complexity part is "non-decreasing": $u\left(\mathbf{P a}_{1}\right) \leq u\left(\mathbf{P a}_{2}\right)$ for $\mathbf{P a}_{1} \subseteq \mathbf{P a}_{2}$.

- Uniformity: the complexity is only a function of the number of parents, i.e. $u\left(\mathbf{P a}_{1}\right)=u\left(\mathbf{P a}_{2}\right)$ whenever $\left|\mathbf{P a}_{1}\right|=\left|\mathbf{P a}_{2}\right|$.

In minimizing the score, if the complexity alone exceeds the best score so far, it is safe to prune the search, as adding more parents could only worsen the score. The key to the proof of polynomial time is a logarithmic bound $p^{*}$ on the number of parents to consider (e.g. by finding a $p^{*}$ for which $u(\mathbf{P a}) \geq u(\emptyset)$ if $|\mathbf{P a}|=p^{*}$ ), so that there are $\mathcal{O}\left((n d)^{p^{*}}\right)$ sets of parents with delays to consider, and each could be done in $\mathcal{O}\left(p^{*} T\right)$ time, making the whole global search polynomial.

In the case of GlobalMIT+, with a simple trick the maximization is turned into minimization, and by assuming that all variables have the same number of states $k$ (for uniformity), all of the above conditions are satisfied, so the MIT score could be optimized in polynomial time with $p^{*} \approx \log _{k}\left(N_{e}\right)$ where $N_{e}$ is $\sum_{i=1}^{k}\left(T_{i}-d\right)$. However, the order of the polynomial depends on the number of time points, and for large networks and large number of time points, the practical running time could still be long.

Recognizing this shortcoming, GlobalMIT* is a heuristic and faster version of GlobalMIT+ with the additional assumption that for each pair of genes $i \rightarrow j$, there is only one delay, and that delay has the best MIT score. So GlobalMIT* first finds the best delay individually for each pair $i \rightarrow j$, and need not try the delays in subsequent optimization. This substantially reduces the search space, speeding up the search greatly. However, in our preliminary test, the practical running time could still be long for large number of genes and time points.

## Identification of genes with hidden common cause

Having obtained the initial GRN of the observed genes, we can estimate the conditional distribution of each gene by maximum likelihood, and then estimate the $\hat{p}_{\text {bias }}$ of each gene, to compare with the expected bias. In this paper, we use a simple method to estimate the bias. For each gene $g$, for each configuration $Q_{i}$ of its parent(s) $\mathbf{P a}_{g}$, we calculate the maximum probability of the conditional distribution as $\max _{j} \mathrm{P}\left(g=j \mid \mathbf{P a}_{g}=Q_{i}\right)$, and we use the median of the maximum probability over the parent configurations $Q_{i}$ 's as the estimate $\hat{p}_{\text {bias }}$ of the bias for gene $g$.

For each gene, we compare the estimated bias $\hat{p}_{\text {bias }}$ with the expected bias $p_{\text {bias }}$, if $\left|\hat{p}_{\text {bias }}-p_{\text {bias }}\right|>\rho$ we predict the gene to have hidden common cause, where $\rho$ is the tolerance with a default value of 0.05 . The idea is that if a gene has no hidden common cause, we expect its parents (and delays) to be correctly determined (given sufficient data), so the estimated bias should be close to expected.

On the other hand, if a gene has hidden common cause, its true parents could not be determined correctly, and we expect the estimated bias to be different from expected. Those genes determined to have hidden parents are called candidates.

If the number of observed genes $n$ is small, we assume that the expected bias is known and given. On the other hand, when $n$ is larger, by the assumption that there are only a small number of hidden variables, we could attempt to estimate the expected bias from the estimated biases of the the observed genes. We simply use the median of the estimated biases as the expected bias for this study, if it is not given. We discuss a possible alternative strategy for estimating the expected bias as future works in the conclusions.

## Estimation of hidden common cause(s) Clustering the candidates

We simply output the initial GRN as the final GRN if there are no candidates. Otherwise, based on the fact that genes with common parent are associated, we cluster the candidates to determine which genes have a common parent, and also to estimate their relative delays for estimating the hidden common cause(s).

Although there are many different clustering algorithms, we found that even a simple greedy clustering algorithm works adequately from our preliminary tests. The idea is that we consider each candidate in turn, and find the cluster center that is closest to it, and if it is close enough, it is added to that cluster; otherwise, the candidate forms a new cluster. The steps are:

1. Let the $k$ candidates be $\left\{g_{1}, g_{2}, \ldots, g_{k}\right\}$
2. Set $n_{c} \leftarrow 1, c_{1} \leftarrow g_{1}, \tau_{1} \leftarrow 0, C_{1} \leftarrow\left\{g_{1}\right\}$
3. For $i=2, \ldots, k$
(a) Let $d_{i}=\operatorname{argmax}_{1 \leq j \leq n_{c}} d\left(c_{j}, g_{i}\right)$, and set $\tau_{i}$ be the associated time shift of $g_{i}$ relative to $c_{d_{i}}$
(b) If $d\left(c_{d_{i}}, g_{i}\right) \geq S_{0}$, update $C_{d_{i}} \leftarrow C_{d_{i}} \cup\left\{g_{i}\right\}$
(c) Otherwise, set $n_{c} \leftarrow n_{c}+1$, then set $C_{n_{c}} \leftarrow\left\{g_{i}\right\}, c_{n_{c}} \leftarrow g_{i}, \tau_{i} \leftarrow 0$
4. Output the $n_{c}$ clusters $\left\{C_{j}: 1 \leq j \leq n_{c}\right\}$, and the time shifts $\left\{\tau_{i}: 1 \leq i \leq k\right\}$
$c_{i}$ is the center of cluster $i . C_{i}$ is cluster $i . \tau_{i}$ is the time shift of candidate $g_{i}$ relative to its cluster center. $d(x, y)$ measures the similarity of two time series $x$ and $y$, here we use the maximum $-\log _{10}(p$-value) of $G^{2}$ tests of the shifted time series (shift $y$ relative to $x$, from $-d$ to $d$, where $d$ is the maximum delay). $S_{0}$ is the threshold for a series to be included in a cluster, with a default value of 2.3 (from our preliminary tests, this value seems to work well, although a value of 1.3 also seems to work adequately).

## Estimating the hidden common cause by expectation maximization

After the clustering, we would estimate a hidden common cause (estimating its time series) for each cluster with two or more members. If no cluster has size at least two, we simply output the initial GRN as the final GRN. For each cluster with size at least two, we perform up to two rounds of EM. The first round estimates a hidden common cause (as parent) of the genes in the cluster without considering potential parents of the hidden common cause. The second round uses the estimated time series of the hidden common cause to find potential parents from all observed genes (not limited to the cluster under consideration) by picking those with high associations with the estimated hidden common cause, and re-estimate the hidden common cause treating the found (if any) potential parents as parents of the hidden common cause. But note that any identified potential parents of a hidden common cause may not be the true parents of the hidden common cause, as they are found by only considering pairwise associations but not possible indirect effects. So we still rely on the relearning of the GRN after estimating hidden common cause(s) to more accurately identify the parents of the hidden common cause(s), if any. However, we expect the identified potential parents to contain useful information for the estimation of the hidden common cause.

We use simple Expectation Maximization (EM) [50] to optimize the log-likelihood, where the states of the hidden common cause at the time points are the latent variables. Let the hidden common cause to be estimated be $h$. The number of states of $h$ is either given as a parameter, or the maximum of the number of states of the children if not given. We perform two rounds of EM, each with a default of 100 iterations, and with restarts. Below we briefly describe the EM steps.

Suppose for cluster $C=\left\{g_{1}, g_{2}, \ldots, g_{|C|}\right\}$ with $|C|>1$ that we want to estimate a hidden common cause $h$ with $n_{s}$ states, which may have potential parents identified (for the second round). We first note that the different series may not be aligned because of different time shifts, as illustrated in Fig. 3. Suppose the time points of interest are $t_{s} \leq t \leq t_{e}$, we denote the state of $h$ at time $t$ as $h_{t}$, which are the latent variables in the EM. Let the configuration of the potential parents of $h$ be denoted by $Q$, and the value of $Q$ at time $t$ be denoted by $Q_{t}$, and let $x_{i, t}$ be the value of $g_{i}$ at time $t$ (if available). Our goal is to estimate the most probable $h_{t}$ for $t_{s} \leq t \leq t_{e}$ given $\mathbf{D}=\left\{Q_{t}\right\} \cup\left\{x_{i, t}\right\}$. The parameter of the likelihood is $\theta=\{\mathrm{P}(h \mid Q)\} \cup\left\{\mathrm{P}\left(g_{i} \mid h\right)\right\}$, where $\mathrm{P}(h \mid Q)$ becomes $\mathrm{P}(h)$ if $h$ has no potential parents.

We first randomly initialize the parameter $\theta^{(0)}=\left\{\mathrm{P}^{(0)}(h \mid Q)\right\} \cup\left\{\mathrm{P}^{(0)}\left(g_{i} \mid h\right)\right\}$, then repeat the E-step and the M-step for a default of 100 iterations:

- E-step: at iteration $k$, for each time $t$, and for $0 \leq j<n_{s}$, calculate

$$
\begin{aligned}
A_{j, t}^{(k)} & =\mathrm{P}\left(h_{t}=j,\left\{g_{i}=x_{i, t}\right\} \mid \theta^{(k)}, \mathbf{D}\right) \\
& =\mathrm{P}^{(k)}(h=j \mid Q_{t}) \prod_{i} \mathrm{P}^{(k)}\left(g_{i}=x_{i, t} \mid h=j\right) \\
B_{j, t}^{(k)} & =\mathrm{P}\left(h_{t}=j \mid \theta^{(k)}, \mathbf{D}\right)=\frac{A_{j, t}^{(k)}}{\sum_{\alpha} A_{\alpha, t}^{(k)}}
\end{aligned}
$$

where $i$ is over the values for which $x_{i, t}$ has value. The $\log$-likelihood is $L\left(\theta^{(k)}\right)=\sum_{t} \log \left(\sum_{j} A_{j, t}^{(k)}\right)$. We also estimate the most probable $h_{t}$ at iteration $k$ as $h_{t}^{(k)}=\arg \max _{j} B_{j, t}^{(k)}$ for each $t$. If the most probable states are not changed in 3 iterations, we re-initialize $\theta$ randomly for the next iterations instead of performing the M-step.

- M-step: we update the parameter for the next iteration as follows.

![img-2.jpeg](img-2.jpeg)

$$\begin{aligned} \mathbf{P}^{(k+1)}(h = j \mid Q = q) &= \frac{\sum_{t:Q_i = q} B_{j,t}^{(k)}}{\sum_{\alpha} \sum_{t:Q_i = q} B_{\alpha,t}^{(k)}} \\ \mathbf{P}^{(k+1)}(g_i = x \mid h = j) &= \frac{\sum_{t:x_{i,t} = x} B_{j,t}^{(k)}}{\sum_{\alpha} \sum_{t:x_{i,t} = \alpha} B_{j,t}^{(k)}} \\ \theta^{(k+1)} &= \left\{\mathbf{P}^{(k+1)}(h \mid Q)\right\} \cup \left\{\mathbf{P}^{(k+1)}(g_i \mid h)\right\} \end{aligned}$$

After the iterations, we output the $h_t^{(k)}$ for which $L(\theta^{(k)})$ is maximum as the estimate of the most probable $h_t$ for this round of EM.

After the first round, we use the estimated most probable $h_t$ to find potential parents of $h$, by performing $G^2$ tests with all observed genes with different time shifts, using a score of $-\log_{10}(p- value)$. A gene (with a particular time shift) could be a potential parent of $h$ if the score is at least 2, and we take only 3 potential parents with the highest scores if there are more than 3. If any potential parent is found, we perform the second round of EM with the parents properly shifted to re-estimate the most probable $h_t$.

Lastly, we take $h_t' = h_{\alpha}$ where $\alpha = t + \max\{\max_{1 \leq k \leq |C_i|} \tau_{i,k}, d\} + 1$ for $1 \leq t \leq T - 1$ and $h't' = 0$ as the estimate of the hidden common cause of cluster $C_i$, i.e. take the suffix of $h_t$ and shift it so that $h_t'$ precedes all the genes in $C$ in time.

### Re-learn the GRN after estimation of hidden common cause(s)

If there are no estimated hidden common cause(s), we simply output the initial GRN as the final GRN. Otherwise we re-learn the GRN using the original observed expression together with the estimated hidden time series of the common cause(s) to give the final GRN, but we disallow any links between the candidates in the same cluster. Similar to inferring the initial GRN, either GlobalMIT+, GlobalMIT+ or D-CLINDE could be used (can be chosen independently from the choice of initial GRN).

### Handling multiple time series data

The above describe the steps of the proposed algorithm when one time series data is provided, we now describe the case where multiple time series data are provided, where the series are not necessarily of the same length. The main idea is that when shifting the time series by a delay (e.g. for $G^2$ test), all the time series are shifted, and the overlapping parts are concatenated for the calculation. This is illustrated in Fig. 4.

Since D-CLINDE, GlobalMIT+ and GlobalMIT+ can handle multiple time series, inferring the initial GRN and re-learning the GRN after estimation of hidden common cause(s) pose no difficulty.

For estimating the hidden common cause(s) using EM, for each time series, we shift according to estimated delay, and instead of only taking the overlapping parts, we "expand" each time series, and concatenate them, as illustrated in Fig. 3.

### Results and discussion

In this section, we assess the effectiveness of the proposed algorithm. Since both long time series expression of large GRN and the knowledge of true GRN are lacking, we mainly use synthetic data for evaluation. Moreover, to our knowledge, there are no previous work that infers hidden common cause(s) for HO-DBN, so we only compare our algorithm on incomplete data, with D-CLINDE and GlobalMIT+ on incomplete and complete data.

We have generated three types of synthetic data for evaluation: case I) small GRN with one hidden variable and the bias is known; case II: small GRN without hidden variable and the bias is known; case III: large GRN (50 and 100 observed genes) with more than one hidden node and the bias is unknown. For each case, we generate two types of data: one long time series where we take prefixes of different lengths; and multiple short time series where we use different number of time series for different total number of time points. For cases I and II, since the networks are small, we use GlobalMIT+ and D-CLINDE for inferring initial GRN and re-learning the final GRN; but for case III, since the networks are large and the number of time points required for decent performance is also large, we use only D-CLINDE to avoid long running time. In all three cases, our proposed algorithm is not given the number of hidden variables. The parameters for generating the synthetic data are summarized in Table 1, and we describe the three cases in the following sections.

![img-3.jpeg](img-3.jpeg)

**Fig. 4** Illustration of shifting the multiple time series

Table 1 Parameter settings of synthetic data generation


We also attempt to evaluate on real data, but as mentioned, due to the lack of long time series expression real data, it is infeasible to test our algorithm on large GRN, so we could only demonstrate our algorithm on small GRNs, but the expression data is still insufficient, so this cannot be regarded as a thorough evaluation. For this purpose, we use expression data from [51], which measures the expression of over 6,000 genes of Saccharomyces cerevisiae using DNA microarrays, with three different methods of synchronization for studying yeast cell cycle. Together with previous data from [52] (also included in [51]), there are 4 time series with information shown in Table 2. And we use YEASTRACT [53] for the GRN. YEASTRACT is a curated database of over 200,000 transcription regulatory associations in Saccharomyces cerevisiae. Since the GRN is far too large for the available expression data, we extract a small number of small subnetworks for the demonstration instead.

In the following, we first describe the performance metrics, and then the generation of synthetic expression data once the GRN is given, and then describe the generation of the synthetic GRN for the different

Table 2 Information of the real data time series


cases, and the results on the three types of synthetic data. After that, we describe the preprocessing of the YEASTRACT subnetworks and the expression data, and then present the results of our algorithm on the real data.

## Performance metrics

We assess the performance of the inference algorithm on Links (which is considered correct if and only if both the gene pair and the direction are correct) and Delays (which is considered correct if and only if both the link and the time delay $\tau_{i j}$ are correct). For each aspect, we mainly look at $F$-score as an overall measure of performance, given by $F$-score $=\frac{2 * \text { Recall } * \text { Precision }}{T}$ where Recall $=\frac{T P}{T P+F N}$, Precision $=\frac{T P}{T P+F P}$, and $T P$ is the number of true positives, $F P$ is the number of false positives, $F N$ is the number of false negatives. From our experience, usually the Links and Delays are inferred correctly at the same time, rather than getting one correct but missing the other. This is quite reasonable, as having a wrong delay may result in totally different associations, so the link is unlikely to be correct. Therefore, we focus on Delays, as it implies the Links.

We still need to address the issue of comparing a predicted GRN with hidden variables against the true GRN with hidden variables, because while the hidden variables in the true GRN are labeled, the indices of the predicted hidden variable(s) may not be the same as that in the true GRN. We therefore need to map the predicted hidden variables to the true GRN before calculating the performance using the above metrics. In addition, note that for the links to/from a hidden variable, the delays cannot be completely determined. This is illustrated in Fig. 5, where the delays of links out of a hidden variable can be increased/decreased, and be compensated by the same decrease/increase in links into the hidden variable. Therefore, we may need to try different delay shifts in mapping a predicted hidden variable to true hidden variable, for useful calculation of the performance.

We try to align each predicted hidden variable to each of the true hidden nodes, and choose the one with the most matched links (to/from observed genes only) and delays (after shifting). And in case of ties, we arbitrarily choose the true hidden variable with the lowest index. After the mapping of predicted hidden variable(s), the performance of the predicted GRN is calculated as described above.

## Generation of synthetic expression data

Given a HO-DBN (the transition network), we generate expression data by using uniform independent distribution for the prior network to generate $d$ (the maximum

![img-4.jpeg](img-4.jpeg)

**Fig. 5** Illustration of shifting the delays for hidden variable

Delay) time points (not included in the final expression data), then generate a time series of the required length using the conditional distributions in the *transition network*. For generating multiple short time series, the length of each series is uniformly chosen from 20 to 35.

### Case I: synthetic small GRN with one hidden node

We first test our proposed algorithm on small GRN where there is only one hidden node, and the bias *p_bias* is assumed known.

#### *Network generation*

The GRN in this case is illustrated in Fig. 6, where there is one hidden variable, which has *p* ≥ 0 parents and *c* ≥ 2 children. But the algorithm is not given the number of hidden variables. For each link, the delay is uniformly chosen from {1, . . . , *d*}, where *d* = 4. Each variable has 3 states (including the hidden variables), and the inference algorithm uses the maximum number of states of the children as the estimate of the number of states of any hidden common cause, so the predicted hidden variables also have 3 states. For each configuration of the parent(s), one state is

![img-5.jpeg](img-5.jpeg)

**Fig. 6** Illustration of the small synthetic network for case I. The hidden variable has *p* ≥ 0 parents and *c* ≥ 2 children

randomly chosen as the dominant state in the conditional distribution and receives a probability of *p_bias*, and the remaining states share the probability of 1 − *p_bias* equally.

The different values of the parameters we have tested are shown in the column *Case I, II* of Table 1. For each setting of *p*, *c* and *p_bias*, we generate 20 replicates, for a total of 960 GRNs. For the one long time series case, for each replicate, we generate expression data with 800 time points, and then take prefix to get *T* time points, and output only the expression of the observed genes. And for the multiple short time series case, for each replicate, we generate 32 time series, we test using *K* time series at a time.

#### *Results*

Table 3 shows the median *Delays F-score* of our proposed algorithm on case I with D-CLINDE and GlobalMIT* (for initial GRN and re-learning of the final GRN) using one long time series of different lengths, and Table 4 shows the results for using different number of short time series, where the medians are taken over the 20 replicates in each setting.

First of all, we see that even for these relatively small networks, the number of time points required for decent performance is quite large. This may be due to that the algorithm does not assume that the number of hidden common cause is known. Besides, since the dependency in HO-DBN can be combinatorial (different configurations of the parents have different conditional distributions for a node), which may also be the reason that a large sample is needed.

For large *T* or *K*, our proposed algorithm can perform adequately (with either D-CLINDE or GlobalMIT*), except for *c* = 2, where the performance is more erratic (e.g. *p* = 2, *c* = 2 and *p_bias* = 0.85) and may be poor even when *T* = 800. One possible reason is that when *c* = 2, there is less information for estimating the hidden common cause.

Also, the performance of *p* = 3 is worse than the corresponding result in *p* = 2. One possible reason is that with more parents, it is more difficult to identify all the *potential parents* of a hidden common cause after the first round of EM, because only pairwise association is used in the identification. Moreover, even if the *potential parents* have been correctly identified, the estimation of the hidden common cause in the second round is difficult, because there are more configurations for the parents, and consequently more conditional distributions for the hidden common cause, and therefore there are less samples in each cell of the contingency table.

Comparing using D-CLINDE and GlobalMIT* for our proposed algorithm, the difference in the performance is small when *T* or *K* is large, but usually D-CLINDE

Table 3 Median delays F-scores of case I using long time series with D-CLINDE and GlobalMIT*


Table 3 Median delays F-scores of case I using long time series with D-CLINDE and GlobalMIT* (Continued)


is slightly worse, which is quite reasonable because DCLINDE is a simple heuristic.

In short, the results show that our proposed algorithm can adequately recover hidden common cause in small GRN, with large enough number of time points.

## Case II: synthetic small GRN without hidden node

We also test on small GRN without any hidden variables, where the algorithm is not given the number of hidden variables, but the bias $p_{\text {bias }}$ is known. The parameters are the same as in case I, which are shown in the column Case I, II of Table 1.

## Network generation

For each GRN ( $p, c, p_{\text {bias }}$ and replicate) in case I, we use GlobalMIT* alone on the (incomplete) data of 800 time points to infer an GRN, which is definitely wrong as all true links are to/from the hidden variable. If the inferred GRN is non-empty, it is used; otherwise, a small GRN of a node in the middle with $p$ parents, and $c-$ 1 children is generated as in case I, but all genes are labeled as observed. Having obtained the 960 GRNs without hidden nodes, the time series are generated as in case I.

## Results

Table 5 shows the median Delays F-score of our proposed algorithm on case II with D-CLINDE and GlobalMIT* (for initial GRN and re-learning of the final GRN) using one long time series, and Table 6 shows the corresponding results using multiple short time series.

The performance of our algorithm using either DCLINDE or GlobalMIT* is good when $T \geq 400$ or $K \geq 16$, and sometimes it is good even with $T \geq 200$ or $K \geq 8$. Also, in many settings, the $F$-score of using GlobalMIT* can reach 1, while D-CLINDE can sometimes reach 1. Similar to case I, using D-CLINDE is slightly worse than using GlobalMIT*.

The results show that with adequate number of time points, our proposed algorithm can infer the GRN correctly when there are no hidden common cause, and does not introduce hidden common cause needlessly.

## Case III: synthetic large GRN with more than one hidden node

Besides the above two cases for small GRN, we also test the more realistic case of larger GRN with more than one hidden node (but the number is unknown), and that the

Table 4 Median delays F-scores of case I using multiple short time series with D-CLINDE and GlobalMIT*


Table 4 Median delays F-scores of case I using multiple short time series with D-CLINDE and GlobalMIT* (Continued)


bias $p_{\text {bias }}$ is unknown. For a network with $n$ observed genes, we would generate $n_{h}=\left\lceil\frac{n}{10}\right\rceil$ hidden variables.

## Network generation

For $n$ observed genes and $n_{h}$ hidden nodes, a maximum of $M_{0}$ parents for observed genes, a maximum of $d$ as delay, we generate a GRN with the structure shown in Fig. 7, where there are four types of nodes: hidden, parents of hidden, children of hidden, and other. The hidden nodes have a random number of distinct parents and children. Parents of hidden take (either 1 or 2 of) other as parents; other take (either 1 or 2 of) any observed genes as parents. After generating the links, the delays and conditional distributions are generated as in cases I and II. The parameters that we have tested are listed in column Case III of Table 1. For each setting of $n$ and $p_{\text {bias }}, 40$ replicates are randomly generated, for a total of 240 GRNs. For the expression data, we generate up to 1600 time points for the long time series case, and up to 64 time series for the multiple short time series case, to assess the time points needed for decent performance for networks of size 50 and 100 .

## Results

Tables 7 and 8 show the median Delays F-score on case III using one long time series and multiple short time series respectively, where complete is D-CLINDE alone on the complete data, which is the unrealistic case that the expression of all the $n+n_{h}$ nodes are given; hidden is our proposed algorithm using D-CLINDE on the incomplete data, which is the more realistic case that the expression of the $n_{h}$ hidden nodes are not given; and ignoreHidden is D-CLINDE alone on the incomplete data, which does not infer hidden common causes. The medians are taken over the 40 replicates in each setting. We also show the ratio of hidden over complete as percentage. We have also performed one-sided Wilcoxon signed rank tests on whether the median $F$-score of hidden is better than ignoreHidden, and show the $p$-values which are smaller than 0.1 . First of all, note that complete can achieve good performance when $T$ or $K$ is large, even though D-CLINDE is only a heuristic. When $T \geq 800$ or $K \geq 32$, the performance of complete is better than hidden which in turn is better than ignoreHidden, which is as expected. Also, hidden can achieve more than $80 \%$ of the performance of complete. But since having complete data is quite unrealistic in a real world setting, the main comparison of interest is between hidden and ignoreHidden, i.e. between handling or not handling hidden common cause. We see that hidden is significantly (with low $p$-value) better than ignoreHidden once $T \geq 800$ and $K \geq 32$. These results show that our proposed algorithm can recover hidden common causes, for larger GRN, and

Table 5 Median delays F-scores of case II using long time series with D-CLINDE and GlobalMIT*


Table 5 Median delays F-scores of case II using long time series with D-CLINDE and GlobalMIT® (Continued)


where the number of hidden common causes and the bias in the conditional distributions are unknown.

## Random candidate order in clustering

By default, when clustering the candidates, they are considered sequentially from smaller index to larger index. As currently the clustering is a simple greedy algorithm, this raises the question of whether the order affects the resulting networks inferred. For this, we have added the option of using random order, and for the GRNs in case III, for each setting of $n, p_{\text {bias }}, T$ for one long time series and $K$ for multiple short time series. We arbitrarily choose replicate 1 out of the 40 replicates, and repeat the inference using 100 random clustering order. Tables 9 and 10 show the mean and standard deviation of the Links and Delays $F$-score using one long time series and multiple short time series, respectively. From the results, we see that the $F$ scores of using different clustering order are very similar, and the standard deviations are all less than 0.06 . This suggests that the clustering order does not have great effects on the quality of the resulting networks.

## Different number of iterations in EM

The time series of hidden common causes are estimated using Expectation Maximization (EM) with random initial parameters and restarts, but EM may be sensitive to the initialization. In this subsection we repeat the experiment in case III using different number of EM iterations, namely $100,200,500,1000,2000$ and 5000 , to assess the effect of different number of EM iterations. Tables 11 and 12 show the median Delays F-score of our proposed algorithm using D-CLINDE on case III with incomplete data using one long time series and multiple short time series respectively, where the number of EM iterations is varied. From the results, we can see that the median $F$-scores are very similar when using different number of EM iterations, suggesting that EM has effectively converged. In addition, as mentioned in the previous subsections, our algorithm on incomplete data (hidden) has decent performance, which suggests that EM has converged to a reasonably good (local) solution.

## Small YEASTRACT subnetworks with real data Preprocessing of subnetworks

YEASTRACT [53] (http://www.yeastract.com/formfind regulators.php) is accessed to get the regulating TFs of a list of 149 TFs using the "DNA binding and expression evidence" option. 392 links involving only 129 TFs are obtained and we use the "ORF List $\Leftrightarrow$ Gene List" utility

Table 6 Median delays F-scores of case II using multiple short time series with D-CLINDE and GlobalMIT*


Table 6 Median delays F-scores of case II using multiple short time series with D-CLINDE and GlobalMIT* (Continued)


of YEASTRACT to convert the gene names into ORF id's, and all 129 id's appear in the yeast cell cycle [51] data.

For the limited data the GRN is still too large, so we have chosen 22 subnetworks with sizes and constituent TFs shown in Table 13. A TF (which has children in the subnetwork) is chosen to be the hidden variable in each subnetwork. Since the delays in the links are not

![img-6.jpeg](img-6.jpeg)

Fig. 7 Illustration of the large synthetic network for case III. Each hidden variable has up to 3 parents, and up to 5 distinct children. The parents of hidden variables can only have other genes as parents, while the other genes can have any observed gene as parents known, we focus on the performance on Links for the demonstration.

## Preprocessing of expression data

The yeast cell cycle [51] data (http://genome-www. stanford.edu/cellcycle/) contains 4 time series: alpha, $c d c 15, c d c 28$ and $e l u$, with different lengths and time points, as shown in the second column of Table 2. We perform spline interpolation (using the spline () function in R) to the time points shown in the third column of Table 2 to make the time points equidistant. Some TFs in some series are entirely missing, and we fill in with zero. We rely on the spline interpolation to fill in the value for other missing values.

Since we are learning discrete HO-DBN, we perform quantile discretization to discretize the expression data into 3 states, and have prepared two sets for each subnetwork and each time series: complete which contains expression of all TFs of the subnetwork; and incomplete which omits the expression of the chosen hidden variable. Therefore, there are 8 expression datasets for each subnetwork.

## Results

Since the subnetworks are not large, time is not a major concern, we use our proposed algorithm with D-CLINDE and GlobalMIT+. We test using one of alpha, $c d c 15, c d c 28$ and $e l u$, and also using all 4 series. The number of EM

Table 7 Median delays F-scores of case III using long time series with D-CLINDE


Complete is D-CLINDE on the complete data. hidden is our proposed algorithm with D-CLINDE on the incomplete data. ignoreHidden is D-CLINDE on the incomplete data. $p$-value is for one-sided Wilcoxon signed rank test on whether the median F-score of hidden is better than ignoreHidden, and entries larger than 0.1 are omitted. H/C is the ratio of hidden over complete as percentage.

Table 8 Median Delays F-scores of Case III using Multiple Short Time Series with D-CLINDE


Complete is D-CLINDE on the complete data. hidden is our proposed algorithm with D-CLINDE on the incomplete data. ignoreHidden is D-CLINDE on the incomplete data. $p$-value is for one-sided Wilcoxon signed rank test on whether the median F-score of hidden is better than ignoreHidden, and entries larger than 0.1 are omitted. H/C is the ratio of hidden over complete as percentage.

Table 9 Mean and standard deviation of links and delays F-scores of case III using long time series with the proposed algorithm with D-CLINDE


The results are on the incomplete data, using replicate 1 for each setting of $n, p_{\text {bias }}$ and $T$, with 100 random orders in clustering the candidates. $L F$ is the Links F-score, and DF is the Delays F-score.

Table 10 Mean and standard deviation of links and delays F-scores of case III using multiple short time series with the proposed algorithm with D-CLINDE


The results are on the incomplete data, using replicate 1 for each setting of $n, p_{\text {bias }}$ and $K$, with 100 random orders in clustering the candidates. $L F$ is the Links F-score, and DF is the Delays F-score.

Table 11 Median delays F-scores of case III using long time series with the proposed algorithm with D-CLINDE


The results are on the incomplete data, with different number of iterations for the EM. em100 is using 100 EM iterations, em200 is using 200 EM iterations and so on.

Table 12 Median delays F-scores of case III using multiple short time series with the proposed algorithm with D-CLINDE


The results are on the incomplete data, with different number of iterations for the EM. em100 is using 100 EM iterations, em200 is using 200 EM iterations and so on.

Table 13 YEASTRACT Subnetworks


$s n$ is the subnetwork. $n$ is the number of TFs in the subnetwork, $n_{\mathrm{L}}$ is the number of links in the subnetwork. The hidden TF is the one with expression hidden in incomplete setting of the experiments. iterations is 1000 . The maximum delay is 4 . The bias $p_{\text {bias }}$ is unknown. For D-CLINDE, we have tried the score thresholds $1,1.3,2,2.3$ and 3 . For GlobalMIT+, we have tried the $\alpha$ values $0.9,0.95,0.99,0.995$ and 0.999 .

Table 14 shows the best Links F-score over series used and parameters tested, where complete is D-CLINDE or GlobalMIT+ alone on the complete data, hidden is our proposed algorithm on incomplete data, and ignoreHidden is D-CLINDE or GlobalMIT+ alone on the incomplete data.

When using D-CLINDE, hidden is better than ignoreHidden in 19 out of 22 subnetworks, has ties in 2 subnetworks, and is worse in 1 . When using GlobalMIT+, hidden is better than ignoreHidden in 21 out of 22 subnetworks, and worse in 1 . This shows that our proposed algorithm helps to infer more accurate GRN from limited data, because it considers the possibility of hidden common cause.

Also note that hidden is sometimes even better than complete, which is counter-intuitive. This suggests that the given data is insufficient to enable robust GRN inference even given the complete data. Another possible reason is that our algorithm makes the assumption that the children of a predicted hidden common cause are not linked to each other, which may help the GRN inference in the limited data case. If more time points are available, we would expect the situation to be more like the synthetic data case, where complete has slightly better performance than hidden.

As mentioned before, since the real data is very limited, we cannot draw strong conclusion for the YEASTRACT subnetworks, but the results suggest that our proposed algorithm has potential in helping to recover hidden common causes in real GRN, but likely more data is needed.

## Conclusions

In this paper, we have developed an algorithm to infer from expression data the transition network of a discrete HO-DBN which may have a small but unknown number of hidden common causes, with some assumptions on the conditional distributions in the HO-DBN. We have tested our algorithm on 3 types of synthetic data: small GRN with one hidden node, small GRN with no hidden node, and large GRN with a small but unknown number of hidden nodes. Experiment results show that our proposed algorithm can recover the causal GRN adequately given

Table 14 Best links F-scores of YEASTRACT subnetworks using our proposed algorithm with D-CLINDE and GlobalMIT+


Complete is D-CLINDE or GlobalMIT+ on the complete data. hidden is our proposed algorithm on the incomplete data (without the hidden node). ignoreHidden is D-CLINDE or GlobalMIT+ on the incomplete data. the incomplete data. Using the limited real expression data and small YEASTRACT subnetworks, we have also demonstrated the potential of our algorithm to recover hidden common causes in real data, but more time series expression data is needed.

## Future works

For future work, we intend to develop more sophisticated clustering of candidate genes with hidden common cause(s), instead of using the simple greedy heuristic. In addition, we intend to investigate different methods of specifying the similarity threshold $S_{0}$. Currently the similarity of two time series is measured by the maximum $-\log _{10}(p-$ value $)$ of $G^{2}$ tests of the two shifted time series. Therefore, the threshold $S_{0}$ is already related to $p$-value, and this helps to set an appropriate value for $S_{0}$. In order to more formally set the threshold $S_{0}$, one way would be to obtain the distribution of the similarity score when two time series are unrelated, and then a threshold could be set such that the probability of incorrectly putting two unrelated time series into the same cluster is controlled.

However, obtaining the theoretical distribution may not be straightforward. Alternatively, the empirical distribution of the similarity score could be used. For example, first randomly choose two time series, then randomly permute the time points of one series, and calculate the similarity score. This could be repeated a large number of times to give an empirical distribution of the similarity score, and an appropriate threshold could be set accordingly.

Also, we intend to study how to relax the assumptions on the conditional distributions. Another issue worth pursuing is to better decide the number of states of hidden common causes, for example, the techniques in [49] could be incorporated.

Also, estimating the bias in the conditional distributions is an important part of the proposed algorithm, as we rely on this to predict the genes with hidden common causes. In this study, we use the maximum probability as the estimate of the bias for each conditional distribution (conditional on one configuration of the parent(s)), and use the median of the estimated biases as the estimate of

the bias of a gene. If a gene has many configurations of parents, some cells in the contingency table may not have enough data points for proper estimation of the conditional distribution, and consequently the estimation of the bias may be affected. We use median as a simple strategy alleviate this problem, in the hope that more than half of the conditional distributions of a gene have proper estimation of bias. One possible alternative strategy is to use a Bayesian model, where there is an overall unknown parameter $p_{\text {bias }}$ with a prior distribution; and given this parameter, for each gene and each configuration of the gene's parent(s), the condition distribution has a (possibly different) dominate state which has probability $p_{\text {bias }}$, and other states share the remaining $1-p_{\text {bias }}$ equally; and these conditional distributions produce the observed time series expression data. Under this model, we may attempt to estimate the posterior distribution of the parameter $p_{\text {bias }}$, given the observed time series expression. This may better solve the issue of insufficient data points in some cells of the contingency table for the estimation of the bias. We intend to study this in more depth as future work.

In this study, we learn an initial GRN, estimate the hidden common cause(s), and re-learn the GRN to give the final GRN if any hidden common cause is learnt (steps 1 to 4 in Fig. 2). It would be interesting to see if iterating the steps 2 to 4 would allow more hidden nodes to be estimated. If the hidden common causes of the observed genes are estimated sufficiently well after the first iteration, the hidden common cause(s) (if any) of these hidden common causes might be estimated in the next iteration. However, this may be difficult, because we do not expect the true hidden time series of common causes to be recovered from the estimation. More realistically, the estimated time series may have discrepancy with the true time series, though may still allow the causal relationships of the hidden variable with other observed variables to be recovered adequately. Consequently, further estimating the hidden common causes of estimated hidden common causes would be more difficult. This is an interesting direction to investigate as future work.

## Availability of supporting data

The data set(s) supporting the results of this article is(are) included within the article (and its additional file(s)).

## Abbreviations

GRN: gene regulatory network; TF: transcription factor; BN: bayesian Network; ODE: ordinary differential equation; DBN: dynamic Bayesian Network; HO-DBN: high-order DBN; MDL: minimum description length; BDe: Bayesian-Dirichlet equivalent; CI: causal inference; FCI: fast causal inference; EM: expectation maximization; SEM: structural-EM.

## Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

LYL conceived of the initial algorithm for recovering hidden common cause for HO-DBN, and implemented the algorithm. LYL wrote the first draft of this paper. MLW, KHL and KSL suggested important refinements to the basic idea, and helped revise the paper. All authors read and approved the final manuscript.

## Acknowledgements

We thank the anonymous reviewers for their thoughtful comments. This research is partially supported by GRF Grant (Project References 414413) and GRF grant (LU310111) from the Research Grant Council of the Hong Kong Special Administrative Region.

## Author details

${ }^{1}$ Department of Computer Science and Engineering, The Chinese University of Hong Kong, Shatin, Hong Kong. ${ }^{2}$ Department of Computing and Decision Sciences, Lingnan University, Tuen Mun, Hong Kong.

Received: 23 May 2015 Accepted: 11 November 2015
Published online: 25 November 2015

## Submit your next manuscript to BioMed Central and we will help you at every step:

- We accept pre-submission inquiries
- Our selector tool helps you to find the most relevant journal
- We provide round the clock customer support
- Convenient online submission
- Thorough peer review
- Inclusion in PubMed and all major indexing services
- Maximum visibility for your research

Submit your manuscript at
www.biomedcentral.com/submit
BioMed Central