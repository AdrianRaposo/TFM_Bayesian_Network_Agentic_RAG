# Impact of Noise on Molecular Network Inference 

Radhakrishnan Nagarajan ${ }^{1 *}$, Marco Scutari ${ }^{2}$<br>1 Division of Biomedical Informatics, Department of Biostatistics, University of Kentucky, United States of America, 2 UCL Genetics Institute, University College London, London, United Kingdom


#### Abstract

Molecular entities work in concert as a system and mediate phenotypic outcomes and disease states. There has been recent interest in modelling the associations between molecular entities from their observed expression profiles as networks using a battery of algorithms. These networks have proven to be useful abstractions of the underlying pathways and signalling mechanisms. Noise is ubiquitous in molecular data and can have a pronounced effect on the inferred network. Noise can be an outcome of several factors including: inherent stochastic mechanisms at the molecular level, variation in the abundance of molecules, heterogeneity, sensitivity of the biological assay or measurement artefacts prevalent especially in highthroughput settings. The present study investigates the impact of discrepancies in noise variance on pair-wise dependencies, conditional dependencies and constraint-based Bayesian network structure learning algorithms that incorporate conditional independence tests as a part of the learning process. Popular network motifs and fundamental connections, namely: (a) common-effect, (b) three-chain, and (c) coherent type-I feed-forward loop (FFL) are investigated. The choice of these elementary networks can be attributed to their prevalence across more complex networks. Analytical expressions elucidating the impact of discrepancies in noise variance on pairwise dependencies and conditional dependencies for special cases of these motifs are presented. Subsequently, the impact of noise on two popular constraintbased Bayesian network structure learning algorithms such as Grow-Shrink (GS) and Incremental Association Markov Blanket (IAMB) that implicitly incorporate tests for conditional independence is investigated. Finally, the impact of noise on networks inferred from publicly available single cell molecular expression profiles is investigated. While discrepancies in noise variance are overlooked in routine molecular network inference, the results presented clearly elucidate their nontrivial impact on the conclusions that in turn can challenge the biological significance of the findings. The analytical treatment and arguments presented are generic and not restricted to molecular data sets.


Citation: Nagarajan R, Scutari M (2013) Impact of Noise on Molecular Network Inference. PLoS ONE 8(12): e80735. doi:10.1371/journal.pone. 0080735
Editor: Alberto de la Fuente, Leibniz-Institute for Farm Animal Biology (FBN), Germany
Received July 8, 2013; Accepted October 7, 2013; Published December 5, 2013
Copyright: © 2013 Nagarajan, Scutari. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Funding: RN acknowledges support from Kentucky Center for Clinical and Translational Science, UL1TR000117. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Competing Interests: The authors have declared that no competing interests exist.
* E-mail: magarajani@uky.edu

## Introduction

Identifying associations and network structures from observational data sets obtained across a given set of entities is a challenging problem and of great interest across a spectrum of disciplines including molecular biology [1-8]. While the molecular entities of interest are represented by the nodes, their associations are represented by the edges. Such networks can prove to be convenient abstractions of the underlying pathways and signalling mechanisms across distinct phenotypes and disease states. [1,2,7]. They can reveal interesting characteristics including repetitive structures, dominant players, community structures and generative mechanism [9-11] that can assist in developing meaningful interventions.

Molecular data obtained from biological systems may or may not have explicit temporal information. While the former explicitly captures the evolution of the molecular activity as a function of time (dynamic), the latter represents a snapshot of the biological activity in a given window of time (static). Dynamic data sets are rare and challenging to generate since they demand controlling a number of factors. Static data sets in conjunction with multiple independent realizations are relatively easier to generate. Their prevalence may also be attributed to the tradition of generating replicate measurements in molecular biology in order to
demonstrate reproducibility of the findings. Prior studies on static data sets used pairwise dependency measures to capture the associations between a given set of molecules in the form of relevance networks [1]. The underlying hypothesis being that correlated genes are likely to be co-regulated or functionally related [12]. However, pairwise dependency measures by definition are symmetric measures resulting in undirected graphs. It is also known that the dependency between a given pair of genes may not necessarily be direct and possibly mediated by other gene(s). This possibly motivated the choice of conditional dependencies as opposed to pairwise dependencies for molecular network inference. Subsequently, probabilistic approaches such as Bayesian network structure learning techniques that model the conditional dependencies across a larger number of variables in an automated manner were proposed to infer molecular networks from static data sets $[3,6,7]$. The resulting networks of constraint-based structure learning are typically in the form of directed acyclic graphs (DAGs) or partially directed acyclic graphs (PDAGs). While DAGs have directed edges, PDAGs have directed as well as undirected edges and accommodate the presence of equivalent classes [13,14]. Constraint-based structure-learning algorithms by their very nature do not accommodate the presence of cycles and feedback between the molecules of interest which is an inherent limitation. They have nevertheless proven to be useful approximations of

pathways and signalling mechanisms [6,7,13]. The DAGs (PDAGs) may also reveal possible causal relationships between the nodes under certain implicit assumptions [15].

Of interest, is to note that these molecular data sets are inherently noisy [16,17,18]. Noise and its variation across molecular entities may have contributions from several factors including stochastic mechanisms coupled to the systems dynamics, sensitivity and precision of the measurement device, variations in abundance of specific molecules, preferential binding affinities and experimental artefacts that are an outcome of the estimation process $[7,19,20,21]$. While identifying the source of noise is a challenging problem in its own merit, understanding its impact on network inference procedure is especially critical in order to avoid identification of spurious associations. In a recent study, we elucidated the non-trivial impact of noise and auto-regulatory feedback on networks inferred using Granger causality tests. The results were established on multivariate time series generated using gene network motifs modelled as vector auto-regressive processes (VAR) [22], as well as those inferred from cell-cycle microarray temporal gene expression profiles [23,24]. The present study investigates the impact of noise on pair-wise correlation, partial correlation and constraint-based structure learning algorithms by considering static data sets generated from linear models of popular network motifs and publicly available molecular expression data [7]. Network motifs are repetitive atomic structures that have been found to be prevalent across more complex networks [9]. In the present study, we consider three popular three-node motifs, namely: common-effect, three-chain and the coherent type-I feed-forward loop (FFL) [9,25,26]. The common-effect motif and the three-chain motif represent the convergent and serial connection respectively. These connections comprise the fundamental connections in Bayesian networks [27]. Furthermore, the conditional independence relationships represented by these motifs are usually among the first to be examined in any constraint-based structure learning algorithm justifying their choice. Common-effect motif is also an essential ingredient in identifying equivalent classes and PDAGs [13]. The coherent type-I FFL has been shown to persist across a number of organisms including E. Coli and S. Cerivisiae [25,26]. Of interest, is to note that three-chain and common-effect motifs are an integral part of a type-I coherent FFL. Analytical expressions for large discrepancies in noise variance on pairwise (correlation coefficient) and conditional dependencies (partial correlation) are investigated. The impact of such discrepancies on constraintbased Bayesian network structure learning is also investigated. Finally, the presence of significant discrepancies in noise variance and its impact on network inference from experimental molecular expression profiles [7] is investigated.

## Methods and Results

Prior to investigating the impact of noise on the constraintbased Bayesian network structure learning algorithms, its impact on pairwise and conditional dependencies across the three network motifs is investigated.

### 2.1 Pairwise and Conditional Dependencies

Network Motif Parameters. In the following discussion, $\left(x_{t}, y_{t}, z_{t}\right)$ represent the molecular expression of the three genes $(x, y, z)$ respectively in a small time window $(T, T+t)$. The terms $\left(\epsilon_{t}, \eta_{t}, \delta_{t}\right)$ represent zero-mean, unit-variance uncorrelated noise attributed to inherent uncertainties and artifacts prevalent in molecular expression studies. Parameter $(\alpha>0)$ represents the transcriptional coupling strengths between the genes and is constrained to be equal across the genes, since the impact of variations in $\alpha$ on pairwise and conditional dependencies is expected and not the goal of the present study. Discrepancies in the noise variances across the nodes are represented by parameters $\gamma_{i}>0, i=1,2$.

Case 1: Common-effect network motif. The communeffect network motif ( $z$-structure) [13] is a fundamental connection, Fig. 1a, discussed widely within the context of Bayesian network structure learning algorithms. For this motif, $z$ is regulated by $x$ and $y$ given by the linear model,

$$
\left[\begin{array}{l}
x_{t} \\
y_{t} \\
z_{t}
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
\alpha & \alpha & 0
\end{array}\right] \cdot\left[\begin{array}{l}
x_{t} \\
y_{t} \\
z_{t}
\end{array}\right]+\left[\begin{array}{c}
\epsilon_{t} \\
\gamma_{1} \cdot \eta_{t} \\
\gamma_{2} \cdot \delta_{t}
\end{array}\right]
$$

The correlation coefficients are given by

$$
\begin{aligned}
& \rho_{x y}=\frac{E(x y)}{\sigma_{x} \sigma_{y}}=0 \\
& \rho_{x z . y}=\frac{E(x z)}{\sigma_{x} \sigma_{y}}=\frac{\alpha}{\sqrt{\left(\alpha^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}\right)}} \\
& \rho_{y z}=\frac{E(y z)}{\sigma_{y} \sigma_{z}}=\frac{\alpha \gamma_{1}}{\sqrt{\alpha^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}}} \cdot \gamma_{1} \neq 0
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \rho_{x y . z}=-\frac{\alpha^{2} \gamma_{1}}{\sqrt{\left(\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}\right)} \sqrt{\left(\alpha^{2}+\gamma_{2}^{2}\right)}} \\
& \rho_{x z . y}=\frac{\alpha}{\sqrt{\left(\alpha^{2}+\gamma_{2}^{2}\right)}} \\
& \rho_{y z . x}=\frac{\alpha \gamma_{1}}{\sqrt{\left(\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}\right)}}
\end{aligned}
$$

For large noise limit at $z\left(\gamma_{2} \rightarrow \infty\right)$ with finite noise at $y\left(\gamma_{1} \ll \gamma_{2}\right)$, the correlation coefficients are given by

$$
\begin{aligned}
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x y}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x z}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{y z}=0
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x y . z}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x z . y}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{y z . x}=0
\end{aligned}
$$

For large noise limit at y(γ1→∞) with finite noise at z(γ2≪γ1), the correlation coefficients are given by

$$\lim_{\gamma_1 \rightarrow \infty} \rho_{xy} = 0$$

$$\lim_{\gamma_1 \rightarrow \infty} \rho_{xz} = 0$$

$$\lim_{\gamma_1 \rightarrow \infty} \rho_{yz} = 1$$

The partial correlations are given by

$$\lim_{\gamma_1 \rightarrow \infty} \rho_{xy.z} = \frac{-\alpha}{\sqrt{\left(\alpha^2 + \gamma_2^2\right)}}$$
$$\lim_{\gamma_1 \rightarrow \infty} \rho_{xz.y} = \frac{\alpha}{\sqrt{\left(\alpha^2 + \gamma_2^2\right)}}$$
$$\lim_{\gamma_1 \rightarrow \infty} \rho_{yz.x} = 1$$

**Remark 1.** *Correlation coefficient estimates reveal significant pairwise dependencies across (x,z) and (y,z) in contrast to (x,y) resulting in the undirected graph x − z, y − z. As expected, conditioning the marginally independent nodes (x,y) on z renders them dependent (i.e. ρ_{xy.z} ≠ 0).*

- *(i) Large noise limit at the common-effect node z(γ2→∞,γ1≪γ2): Pairwise as well as conditional dependencies vanish (4, 5) challenging any reliable conclusion on the network structure in the large noise limit when (γ2→∞,γ1≪γ2) preventing any reliable inference of the network. More importantly, conditioning on the common-effect node at large noise levels did not render x and y dependent as expected (5).*
- *(ii) Large noise limit at one of the causes z(γ2→∞,γ1≪γ2): Pairwise dependencies (x,y) as well as (x,z) disappear (6). Interestingly, conditional dependencies ρ_{xy.z} and ρ_{xz.y} are equal in magnitude with opposite signs and function of γ2 (7). Pairwise as well as conditional dependencies ρ_{yz} and ρ_{yz.x} have maximal values of unity in the large noise limit at y.*

### Case 2. *Three-chain network motif*

Consider the three-chain network motif [9], Fig. 1b, where y mediates the activity between (x,z) given by the linear model

$$\begin{bmatrix} x_t \\ y_t \\ z_t \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ \alpha & 0 & 0 \\ 0 & \alpha & 0 \end{bmatrix} \cdot \begin{bmatrix} x_t \\ y_t \\ z_t \end{bmatrix} + \begin{bmatrix} \epsilon_t \\ \gamma_1 \cdot \eta_t \\ \gamma_2 \cdot \delta_t \end{bmatrix} \tag{8}$$

The correlation coefficients are given by

$$\rho_{xy} = \frac{E(xy)}{\sigma_x \sigma_y} = \frac{\alpha}{\sqrt{\alpha^2 + \gamma_1^2}}$$
$$\rho_{xz} = \frac{E(xz)}{\sigma_x \sigma_z} = \frac{\alpha^2}{\sqrt{\alpha^2 + \gamma_1^2 + \gamma_2^2}}$$
$$\rho_{yz} = \frac{E(yz)}{\sigma_y \sigma_z} = \frac{\alpha \sqrt{\alpha^2 + \gamma_1^2}}{\sqrt{\alpha^2 + \gamma_1^2 + \gamma_2^2}} \tag{9}$$

The partial correlations are given by

$$\rho_{xy.z} = \frac{\alpha \gamma_2}{\sqrt{\left(\alpha^2 \gamma_1^2 + \gamma_2^2\right)\left(\alpha^2 + \gamma_1^2\right)}} \cdot \gamma_2 \neq 0$$
$$\rho_{xz.y} = 0$$
$$\rho_{yz.x} = \frac{\alpha \gamma_1}{\sqrt{\left(\alpha^2 \gamma_1^2 + \gamma_2^2\right)}} \cdot \gamma_1 \neq 0$$

For large noise limit at z(γ2→∞) with finite noise at y(γ1≪γ2), the correlation coefficients are given by

$$\lim_{\gamma_2 \rightarrow \infty} \rho_{xy} = \frac{\alpha}{\sqrt{\alpha^2 + \gamma_1^2}}$$
$$\lim_{\gamma_2 \rightarrow \infty} \rho_{xz} = 0$$
$$\lim_{\gamma_2 \rightarrow \infty} \rho_{yz} = 0$$

The partial correlations are given by

$$\lim_{\gamma_2 \rightarrow \infty} \rho_{xy.z} = \frac{\alpha}{\sqrt{\alpha^2 + \gamma_1^2}}$$
$$\lim_{\gamma_2 \rightarrow \infty} \rho_{xz.y} = 0$$
$$\lim_{\gamma_2 \rightarrow \infty} \rho_{yz.x} = 0$$

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Popular three-gene network motifs: common-effect, three-chain and coherent type-I feed-forward loop are shown in (a), (b) and (c) respectively. doi:10.1371/journal.pone.0080735.g001

For large noise limit at $\mathrm{y}\left(\gamma_{1} \rightarrow \infty\right)$ with finite noise at $\mathrm{z}\left(\gamma_{2} \ll \gamma_{1}\right)$, the correlation coefficients are given by

$$
\begin{aligned}
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x y}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x z}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{y z}=1
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x y . z}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x z . y}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{y z . x}=1
\end{aligned}
$$

Remark 2. Correlation coefficient estimates reveal significant pairwise dependencies across $(\mathrm{x}, \mathrm{y}),(\mathrm{y}, \mathrm{z})$ and $(\mathrm{x}, \mathrm{z})$ resulting in the undirected graph $x-y, y-z, x-z$. As expected, conditioning the marginally dependent nodes $(\mathrm{x}, \mathrm{z})$ on y renders them independent (i.e. $\rho_{x z . y}=0$ ). This result is immune to the choice of the linear model parameters and reflects possible directed acyclic graph of the form $x \rightarrow y \rightarrow z$.

- (i). Large noise limit at the node $\mathrm{z}\left(\gamma_{2} \rightarrow \infty\right)$ : Pairwise dependencies (11), $\left(\rho_{x y}, \rho_{x z}, \rho_{y z}\right)$ are identical to the conditional dependencies in (12), $\left(\rho_{x y . z}, \rho_{x z . y}, \rho_{y z . x}\right)$. Of interest is to note that pairwise dependencies $\rho_{x y}$ and conditional dependency $\rho_{x y . z}$ have identical non-zero magnitude.
- (ii). Large noise limit at the node $\mathrm{y}\left(\gamma_{1} \rightarrow \infty\right)$ : Pairwise dependencies (13), $\left(\rho_{x y}, \rho_{x z}, \rho_{y z}\right)$ are identical to those of conditional dependencies (14), $\left(\rho_{x y . z}, \rho_{x z . y}, \rho_{y z . x}\right)$ similar to what was observed for $\left(\gamma_{2} \rightarrow \infty\right)$. However, in contrast to $\left(\gamma_{2} \rightarrow \infty\right)$, pairwise $\left(\rho_{y z}\right)$ and conditional dependencies $\left(\rho_{y z . x}\right)$ are identical with a maximum value similar to that of the common-effect network motif. Also, pair-wise dependencies $\left(\rho_{x y}, \rho_{x z}, \rho_{y z}\right)$ (13) are identical to those obtained for the common-effect motif (6) failing to distinguish these two structures.

Case 3. Coherent Type-I feed-forward loop network motif
Consider the coherent type-I feed-forward loop [25,26], Fig. 1c, where the expression of y is regulated by x whereas those of z is regulated by x as well as z given by the linear model

$$
\left[\begin{array}{l}
x_{t} \\
y_{t} \\
z_{t}
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0 & 0 \\
\alpha & 0 & 0 \\
\alpha & \alpha & 0
\end{array}\right] \cdot\left[\begin{array}{l}
x_{t} \\
y_{t} \\
z_{t}
\end{array}\right]+\left[\begin{array}{c}
\epsilon_{t} \\
\gamma_{1} \cdot \eta_{t} \\
\gamma_{2} \cdot \delta_{t}
\end{array}\right]
$$

The correlation coefficients are given by

$$
\begin{aligned}
& \rho_{x y}=\frac{E(x y)}{\sigma_{x} \sigma_{y}}=\frac{\alpha}{\sqrt{\alpha^{2}+\gamma_{1}^{2}}} \\
& \rho_{x z}=\frac{E(x z)}{\sigma_{x} \sigma_{z}}=\frac{\alpha^{2}+\alpha}{\sqrt{\alpha^{4}+2 \alpha^{3}+\alpha^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}}} \\
& \rho_{y z}=\frac{E(y z)}{\sigma_{y} \sigma_{z}}=\frac{\alpha^{3}+\alpha^{2}+\alpha \gamma_{1}^{2}}{\sqrt{\alpha^{2}+\gamma_{1}^{2}} \sqrt{\alpha^{4}+2 \alpha^{3}+\alpha^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}}}
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \rho_{x y . z}=\frac{\alpha\left(\gamma_{2}^{2}-\alpha \gamma_{1}^{2}\right)}{\sqrt{\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}} \sqrt{\alpha^{2} \gamma_{2}^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{1}^{2} \gamma_{2}^{2}}} \\
& \rho_{x z . y}=\frac{\alpha \gamma_{1}}{\sqrt{\alpha^{2} \gamma_{2}^{2}+\alpha^{2} \gamma_{1}^{2}+\gamma_{1}^{2} \gamma_{2}^{2}}} ; \gamma_{1} \neq 0 \\
& \rho_{y z . x}=\frac{\alpha \gamma_{1}}{\sqrt{\alpha^{2} \gamma_{1}^{2}+\gamma_{2}^{2}}} ; \gamma_{1} \neq 0
\end{aligned}
$$

For large noise limit at $\mathrm{z}\left(\gamma_{2} \rightarrow \infty\right)$ with finite noise at $\mathrm{y}\left(\gamma_{1} \ll \gamma_{2}\right)$, the correlation coefficients and partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x y}=\frac{\alpha}{\sqrt{\alpha^{2}+\gamma_{1}^{2}}} \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x z}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{y z}=0
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x y . z}=\frac{\alpha}{\sqrt{\alpha^{2}+\gamma_{1}^{2}}} \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{x z . y}=0 \\
& \lim _{\gamma_{2} \rightarrow \infty} \rho_{y z . x}=0
\end{aligned}
$$

For large noise limit at $\mathrm{y}\left(\gamma_{1} \rightarrow \infty\right)$ with finite noise at $\mathrm{z}\left(\gamma_{2} \ll \gamma_{1}\right)$, the correlation coefficients and partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x y}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x z}=0 \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{y z}=1
\end{aligned}
$$

The partial correlations are given by

$$
\begin{aligned}
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x y . z}=\frac{-\alpha}{\sqrt{\alpha^{2}+\gamma_{2}^{2}}} \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{x z . y}=\frac{\alpha}{\sqrt{\alpha^{2}+\gamma_{2}^{2}}} \\
& \lim _{\gamma_{1} \rightarrow \infty} \rho_{y z . x}=1
\end{aligned}
$$

Remark 3. Correlation coefficient estimates reveal significant pairwise dependencies across $(\mathrm{x}, \mathrm{y}),(\mathrm{y}, \mathrm{z})$ and $(\mathrm{x}, \mathrm{z})$ indicating a possible undirected

Table 1. Pair-wise and conditional dependencies across the three network motifs in the asymptotic noise limits.


I doi:10.1371/journal.pone. 0080735 .t001 graph of the form $x-y-z$. Unlike the three-chain, conditioning $(\mathrm{x}, \mathrm{z})$ on y does not render them independent.

- (i). Large noise limit at $\mathrm{z}\left(\gamma_{2} \rightarrow \infty\right)$ : Pairwise dependencies (18) and conditional dependencies (19) are identical to those obtained for the threechain motif (11, 12) failing to distinguish these structures for relatively large noise variance at z, Table 1.
- (ii). Large noise limit at $\mathrm{y}\left(\gamma_{1} \rightarrow \infty\right)$ : Pairwise dependencies (20) and conditional dependencies (21) are identical to those obtained for the common-effect motif (6), (7) failing to distinguish these structures for relatively large noise variance at y, Table 1. Also, the pairwise dependencies for $\left(\gamma_{1} \rightarrow \infty\right)$ is identical for the coherent Type I FFL, threechain as well as the common-effect motif.

### 2.2 Constraint-based Bayesian Network Structure Learning

Bayesian network structure learning algorithms have been used successfully to infer the associations between a large numbers of variables. Several such algorithms have been proposed in literature, a partial list of contributions include [28,29,30,31,32]. In the present discussion, we focus on constraint-based structure learning algorithms that infer the network structure using tests for conditional independence, namely: the Grow-Shrink (GS) algorithm [30] and the Incremental Association Markov Blanket (IAMB) [31].

GS was the first algorithm that learned the Markov blanket of each node as an intermediate step to speed up structure learning process. The Markov blanket $B l(X)$ of a node $X$ is defined as the set of nodes that makes $X$ independent from all the other nodes in the domain. In a Bayesian network, it is formed by the parents of $X$, its children, and the other parents of its children [15]. Therefore, the search for the neighbors of each node can be restricted to its Markov blanket, which in most cases contains a limited number of nodes. GS learns Markov blankets using a forward selection (Growing Phase) followed by a backward selection (Shrinking Phase). Conditional independence tests are performed in order of increasing complexity (i.e. with respect to the number of nodes involved in the test) in order to maximize the overall power of the structure learning algorithm. Markov blankets are then reduced to the corresponding set of neighbors by an additional backward selection. Arc directions are established starting from $z$ structures, which can be identified by the interplay of the causes conditional on their common effect, and then propagated to prevent the formation of further $z$-structures and enforce acyclicity. This is achieved using the heuristics described elsewhere [30,33]. IAMB introduces relatively better heuristics to identify Markov blankets while improving on GS by using a forward stepwise regression. However, IAMB in contrast to GS is designed to identify the Markov blanket of each node and not the complete network structure. Essentially, it performs the same task as the first step of GS but the forward stepwise selection in IAMB reduces the number of nodes incorrectly included in the Markov blankets. In the context of Bayesian network structure learning, IAMB is extended to a complete learning algorithm by adding steps 2 to 4 of GS. While both algorithms have been shown to be formally correct, IAMB has been recently supported by more extensive proofs and simulations [34,35]. Of interest is to note that GS as well as IAMB are highly dependent on the ability of the conditional independence tests to correctly identify dependence relationships. In fact, the proofs of correctness of both structure learning algorithms implicitly assume absence of type I or type II errors. Such an assumption can especially be violated in the presence of noise that may accentuate false-positives as well as false-negatives challenging the biological significance of the results. This in turn justifies investigating the impact of discrepancies in noise variance across the nodes on network inference using GS and IAMB. Since the conditional independence tests increase in complexity during the structure learning process across GS and IAMB [36] the present study is restricted to well-established network motifs that are prevalent across more complex structures. The concerns presented across these motifs are expected to be aggravated across more complex network topologies.

## Common-effect network motif

For large noise limit at $\mathrm{z}\left(\gamma_{2} \rightarrow \infty\right)$ with finite noise at $\mathrm{y}\left(\gamma_{1} \ll \gamma_{2}\right)$ : For relatively large noise variance at z , the pairwise as well as conditional dependencies $(4,5)$ vanish across GS as well as IAMB resulting in an empty network. This happens regardless of the values of $\left(\rho_{X Z, Z}, \rho_{X Z, Y}, \rho_{Z Z, X}\right)$ because both GS and IAMB test for significant pairwise dependencies $\left(\rho_{X Z}, \rho_{X Z}, \rho_{Z Z}\right)$ first and conclude the Markov blankets of $\mathrm{x}, \mathrm{y}$ and z to be empty sets. As a consequence, none of the nodes have any neighbours resulting in an empty graph.

For large noise limit at $\mathrm{y}\left(\gamma_{1} \rightarrow \infty\right)$ with finite noise at $\mathrm{z}\left(\gamma_{2} \ll \gamma_{1}\right)$ :

For relatively large noise variance at $y$, GS was able to retrieve a part of the network structure as discussed below. The Markov blankets inferred by GS are as follows:

- For $B l(x)$ from (6) we have $x \perp y$, i.e. $\rho_{x y}=0$ and $x \perp z$, i.e. $\rho_{x z}=0$ resulting in $B l(x)=\varnothing$.
- For $B l(y)$, from (6) we have $y \perp x$, i.e. $\rho_{x y}=0$ and $y z$, i.e. $\rho_{y z}=1$. As a result, $z$ is added to $B l(y)$. Also from (7), yx given $z$, i.e. $\rho_{x y . z} \neq 0$ since $\alpha>0$. Therefore, $x$ is added to $B l(y)$ for suitable values of $\alpha$ resulting in $B l(y)=\{x, z\}$ characteristic of the motif (1).
- For $B l(z)$, from (6) we have $z \perp x$, i.e. $\rho_{x z}=0$ but $z y$,i.e. $\rho_{y z}=1$. As a result, $y$ is added to $B l(z)$. Also from (7) $\rho_{x z . y} \neq 0$, since $\alpha>0$. Therefore, a suitable choice of $\alpha$ results in the Markov blanket $B l(z)=\{x, y\}$ characteristic of the motif (1).

For IAMB, the conditional independence tests are performed in a different order since the nodes are included in the Markov blankets in decreasing order of association. However, the resulting Markov blankets $B l(x), B l(y)$ and $B l(z)$ are same as those of GS. The impact of discrepancies in noise variance across the nodes on structure learning is especially elucidated by the asymmetry of the Markov blankets $B l(x)$ and $B l(y)$ as well as $B l(x)$ and $B l(z)$. Markov blankets are symmetric by definition, i.e. $x \in B l(y)$ then $y \in B l(x)$ and vice versa. However, for the present case we have following asymmetries $\langle x \in B l(y)$ while $y \notin B l(x)\rangle$ and $\langle x \in B l(z)$ while $z \notin B l(x)\rangle$ violating the definition of Markov blanket. For consistency, a symmetry correction [34,35] may be applied either by removing $x$ from $B l(y)$ and $B l(z)$, or adding $y$ and $z$ to $B l(x)$. The latter correction enables faithful reproduction of the motif while the former does not.

## Three-Chain network motif

For large noise limit at $\mathbf{z}\left(\gamma_{2} \rightarrow \infty\right)$ with finite noise at $\mathbf{y}\left(\gamma_{1} \ll \gamma_{2}\right): z$
For relatively larger noise variance at z , the Markov blankets inferred by GS are given as follows:

- For $B l(x)$, from (11) we know that $x y$, i.e. $\rho_{x y} \neq 0$ since $\alpha>0$. For suitable choice of $\alpha$, we may correctly infer $B l(x)=\{y\}$. Also, from (11, 12) we have $x \perp z$, i.e. $\rho_{x z}=0$ and $x \perp z \mid y$, i.e. $\rho_{x z . y}=0$ so $z \notin B l(x)$. Therefore, the ability to infer $B l(x)$ depends on $\alpha$.
- For $B l(y)$, from $(11,12)$ we have $y \perp z$, i.e. $\rho_{y z}=0$ and $y \perp z \mid x$, i.e. $\rho_{y z . x}=0$ resulting in either $B l(y)=\{x\}$ or $B l(y)=\varnothing$ markedly different from $B l(y)=\{x, z\}$ characteristic of the motif (8).
- For $B l(z)$, from (11) we have $z \perp x$, i.e. $\rho_{x z}=0$ and $y \perp z$, i.e. $\rho_{y z}=0$ resulting in $B l(z)=\varnothing$ in contrast to $B l(z)=\{y\}$ characteristic of the motif (8).

As in the case of common-effect network motif, reordering of the conditional independence tests in IAMB does not result in Markov blankets different from those inferred by GS. Unlike common-effect motif, no asymmetry between the Markov blankets is observed for the three-chain, since $x \in B l(y)$ and $y \in B l(x)$ are established using the same correlation coefficient $\rho_{x y}$. Given these set of Markov blankets, identifying the correct network structure is impossible. Since for large values of $\alpha$, both GS and IAMB learn $\langle x-y, z\rangle$, while for small values of $\alpha$ both GS and IAMB are unable to identify any of the arcs present in the true motif structure. The presence of at most a single arc $x-y$ makes it impossible to infer its direction, since both GS and IAMB use $v$-structures to infer directions and the learned motif structure contains none.

For large noise limit at $\mathbf{y}\left(\gamma_{1} \rightarrow \infty\right)$ with finite noise at $\mathbf{z}\left(\gamma_{2} \ll \gamma_{1}\right)$ :

For relatively large noise variance at $y$, no reliable conclusion of the motif is possible across GS as well as IAMB. The Markov blankets are as follows:

- For $B l(x)$, from (13) we have $x \perp y$, i.e. $\rho_{x y}=0$ and $x \perp z, \rho_{x z}=0$. As a result, $B l(x)=\varnothing$ in contrast to $B l(x)=\{y\}$ characteristic of the motif (8).
- For $B l(y)$, from (13) we have $y \perp x$, i.e. $\rho_{x y}=0$ but $y z$, i.e. $\rho_{y z}=1$. Even after updating the Markov blanket to $B l(y)=\{z\}$, the dependence between $x$ and $y$ is obscured by noise as $\rho_{x y . z}=0$. Therefore, the Markov blanket $B l(y)=\{z\}$.
- For $B l(z)$, from (13) we have that $z \perp x$, i.e. $\rho_{x z}=0$ but $z y$, i.e. $\rho_{y z}=1$. Also, from (14) we have $x \perp z \mid y$, i.e. $\rho_{x z . y}=0$. This results in the Markov blanket $B l(z)=\{y\}$ characteristic of the motif (8).

In this case, no asymmetry is observed despite the effects of noise. Nevertheless, neither GS nor IAMB was able to learn the motif for relatively large noise variance.

## Coherent Type-I Feed-Forward Loop motif

For large noise limit at $\mathbf{z}\left(\gamma_{2} \rightarrow \infty\right)$ with finite noise at $\mathbf{y}\left(\gamma_{1} \ll \gamma_{2}\right)$ :
For relatively large noise variance at z , the Markov blankets determined by GS and IAMB are as follows:

- For $B l(x)$, from (18), $x$ y i.e. $\rho_{x y} \neq 0$, since $\alpha>0$. Also from $(18,19)$ we note that $x \perp z$, i.e. $\rho_{x z}=0$ and $x \perp z \mid y$, i.e. $\rho_{x z . y}=0$. Therefore, $z$ is not included in $B l(x)$. Thus, GS and IAMB return either $B l(x)=\varnothing$ or $B l(x)=\{y\}$ for suitable choice of $\alpha$ in contrast to $B l(x)=\{y, z\}$ characteristic of the motif (15).
- For $B l(y)$, from (18) $x y$, i.e. $\rho_{x y} \neq 0$, since $\alpha>0$. Also, from $(18,19)$ we have $y \perp z$, i.e. $\rho_{y z}=0$ and $y \perp z \mid x$, i.e. $\rho_{y z . x}=0$. Therefore, $z$ is not included in $B l(y)$. Thus, GS and IAMB return either $B l(y)=\varnothing$ or $B l(y)=\{x\}$ for suitable choice of $\alpha$ as opposed to $B l(y)=\{x, z\}$ characteristic of the motif (15).
- For $B l(z)$, it is impossible to learn the correct Markov blanket $B l(z)=\{x, y\}$ since $z \perp x$,i.e. $\rho_{x z}=0$ as well as $z \perp y$,i.e. $\rho_{y z}=0$ from (18). As a result, $B l(z)=\varnothing$.

In the present case, discrepancy in noise variance does not result in asymmetry in the Markov blankets. Thus, symmetry correction may not alleviate the impact of noise. Possible motif structures corresponding to large discrepancies at z are either an empty structure or $(x-y, z)$. This is problematic for two reasons. First, only one arc out of three is correctly identified and its direction cannot be determined by the learning algorithm. Second, the motif structures above are indistinguishable from those obtained for the three-chain network motif.

For large noise limit at $\mathbf{z}\left(\gamma_{1} \rightarrow \infty\right)$ with finite noise at $\mathbf{z}\left(\gamma_{2} \ll \gamma_{1}\right)$ :
For relatively large noise variance y , again neither GS nor IAMB was able to infer the motif. The Markov blankets are given as follows:

- For $B l(x)$, from (20) we have $x \perp y$, i.e. $\rho_{x y}=0$ and $x \perp z$, i.e. $\rho_{y z}=0$. This results in Markov blanket $B l(x)=\varnothing$ in contrast to $B l(x)=\{y, z\}$ For $B l(y)$, from (20) we have $y \perp x$, i.e. $\rho_{x y}=0$. However, $y$ is dependent on $z$, i.e. $\rho_{y z}=1$. Also, from (21) we have $\rho_{x y . z} \neq 0$, since $\alpha>0$. This results in Markov blanket $B l(y)=\{x, z\}$ characteristic of the motif (15) for suitable choice of parameter $\alpha$ characteristic of the motif (15).
- For $B l(z)$, from (20) we have $z \perp x$,i.e. $\rho_{x z}=0$. However, $z$ is dependent on $y$, i.e. $\rho_{y z}=1$. Also, from (21) $\rho_{x y . z} \neq 0$, since $\alpha>0$. These results in turn result in $B l(z)=\{x, y\}$ for suitably large values of $\alpha$.

Asymmetry between the Markov blankets is observed across $B l(x)$ and $B l(y)$ as well as between $B l(x)$ and $B l(z)$. This can be attributed to the fact that $x \in B l(y)$ while $y \notin B l(x)$ and $x \in B l(z)$ while $z \notin B l(x)$ for suitably large values of $\alpha$. Correcting this asymmetry by adding $y$ and $z$ to $B l(x)$ results in the Markov blankets characteristic of the motif. However, establishing their directions is not possible since the presence of an arc between $x$ and $y$ prevents both GS and IAMB from identifying $x \rightarrow y \leftarrow z$. As a result, all possible configurations of the arcs' directions are probabilistically equivalent resulting in an undirected graph. This is phenomenon is known as the shielded collider identification problem and affects all constraint-based learning algorithms [37].

### 2.3 Simulation Results

In the following discussion, the three gene network motifs are generated using $(1,8,15)$ with parameter $(\alpha=0.5)$ and normally distributed noise. Since the objective is to demonstrate the impact of noise as opposed to the other parameter, $(\alpha=0.5)$, is held constant across all the simulations. The noise variance at the node $x$ is fixed at unit variance whereas those at $y\left(\gamma_{1}>0\right)$ and $z\left(\gamma_{2}>0\right)$ are varied systematically in order to understand the impact of discrepancy in noise variance on the conclusions. Three distinct cases of noise variances, namely: $\left(\gamma_{1}=1, \gamma_{2}=1\right)$, $\left(\gamma_{1}=10, \gamma_{2}=1\right)$ and $\left(\gamma_{1}=1, \gamma_{2}=10\right)$ are considered. The cases $\left(\gamma_{1}=10, \gamma_{2}=1\right)$ and $\left(\gamma_{1}=1, \gamma_{2}=10\right)$ correspond to large noise variance limits as discussed under (Cases 1, 2 and 3) whereas $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ corresponds to absence of discrepancies in noise variance. The conditional independence tests used in the following discussion is exact t-test for Pearson correlation as implemented in the R package bnlearn [38]. A description of the functions in bnlearn can be found in the accompanying manual with applications to molecular expression profiles in [39].

Results generated using constraint-based structure learning algorithms GS and IAMB were quite similar consistent with their expected behaviour, Section 2.2. Therefore, we discuss only the results from the GS algorithm. The networks were learned across 200 independent realizations of the data (sample size $=2000$ ) and Friedman's confidence $(\psi)$ [3] was computed for each of the edges. Friedman's confidence essentially represents the percentage of times an edge shows up across networks learnt independently from bootstrapped realizations. In the case of observational data sets, confidences are estimated from networks learned from nonparametric bootstraps of the given empirical sample. In the present study, the underlying model generating the networks is known a priori. Therefore, parametric bootstrap is used where independent realizations of the data were generated from the model in contrast to non-parametric bootstrap [40]. Also, in the present study, confidence estimates of edges known to be present in the given graph a priori essentially represent their statistical power. As a rule of thumb [3], edges with confidence at least $(\psi \geq 0.8)$ were deemed significant. In a recent study [41], we proposed a noise floor approach in order to avoid the ad-hoc choice of $\psi$, and subsequently a statistically motivated approach that estimates optimal $\psi$ from the cumulative distribution of the confidence values [42]. However, in the present study the actual confidence values are presented for enhanced clarity.

Common-effect network motif. The common-effect network motif, Fig. 1a, was generated using (1) with $(\alpha=0.5)$ and normally distributed noise $\left(\epsilon_{t}, \eta_{t}, \delta_{t}\right)$. For finite and equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ at $(\mathrm{y}, \mathrm{z})$ the correlation coefficients $\rho_{x y}, \rho_{y z}$ were similar and relatively higher than $\rho_{x y}(\sim 0)$ as expected (2),

Fig. 2a. In order to investigate the impact of large discrepancies in the noise variances, the noise variance across y was increased relative to $\mathrm{z}\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$. This resulted in small values of $\rho_{x y}, \rho_{x y}$ relative to $\rho_{y z}$, Fig. 2a and resembled (6) as expected. A similar analysis with $\left(\gamma_{1}=1 \ll \gamma_{2}=10\right)$ across y and z resulted in small correlation coefficients across the board similar to (4), Fig. 2a. Therefore, large discrepancies in noise variances across the nodes can have a pronounced effect on the pair-wise dependencies. The corresponding partial correlations for the three choices of noise variance $\left(\gamma_{1}, \gamma_{2}\right)$ are shown in Fig. 2d. For finite equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ at $(\mathrm{y}, \mathrm{z})$, the partial correlation $\rho_{x y, z}<0$ (3) was non-zero in contrast to $\rho_{x y}=0$, rendering the marginally independent nodes ( $\mathrm{x}, \mathrm{y}$ ) dependent. Increasing the noise variance across y relative to $\mathrm{z}\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$ resulted in a significant increase in $\rho_{y z, x}$ (7) whereas for $\left(\gamma_{1}=1 \ll \gamma_{2}=10\right)$, all the conditional dependencies were rendered negligible (5) preventing any reliable conclusion of the network structure, Fig. 2d. For finite equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ at $(\mathrm{y}, \mathrm{z})$, GS was able to faithfully retrieve the structure of the common-effect motif, Fig. 3a. Increasing the noise variance across $\mathrm{y}\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$ relative to z , also retrieved the structure faithfully, Fig. 3c. However, increasing the noise variance on the common effect node $\mathrm{z}\left(\gamma_{1}=1 \gg \gamma_{2}=10\right)$ resulted in low confidence values of the edges challenging any reliable inference of the network, Fig. 3b. Thus the magnitude of the noise variance at the nodes can have a pronounced effect on constraint-based structure learning of a common-effect network motif.

Three-chain network motif. The three-chain network motif, Fig. 1b, was generated using (8) with $(\alpha=0.5)$ and normally distributed noise $\left(\epsilon_{t}, \eta_{t}, \delta_{t}\right)$. For finite and equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ at the nodes $(\mathrm{y}, \mathrm{z})$ the correlation coefficients $\rho_{x y}, \rho_{x y}, \rho_{y z}, \rho_{y z}$ were significant as expected (9) with $\rho_{x y}$ representing the transitive dependency between x and z , Fig. 2 b . In order to investigate the impact of large noise variance, the noise variance on the mediating node y was increased relative to z $\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$. This resulted in small values of $\rho_{x y}, \rho_{x z}$ relative to $\rho_{y z}$ (13) similar to what was observed for the common-effect network motif (6) failing to distinguish these structures. On the other hand, large noise variance on the terminal node z relative to $\mathrm{y}\left(\gamma_{1}=1 \ll \gamma_{2}=10\right)$ resulted in $\rho_{x y}$ values relatively higher than that of $\rho_{x y}$ and $\rho_{y z}$, as expected from Fig. 2b. These results clearly demonstrate the non-trivial impact of noise strengths on network inference on pairwise dependencies. Partial correlations $\rho_{x y, z}$ and $\rho_{y z, x}$ for finite equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ were considerably higher than that of $\rho_{x z, y}(\overline{0})$ as expected, since conditioning on the mediator y should render marginally dependent nodes ( $\mathrm{x}, \mathrm{z}$ ) independent. Increasing the noise variance at y relative to z $\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$ and at z relative to $\mathrm{y}\left(\gamma_{1}=1 \gg \gamma_{2}=10\right)$, rendered the pairwise and conditional dependencies similar. This is reflected by the similar profiles, Figs. 2b and 2e respectively. For finite equal noise variance $\left(\gamma_{1}=1, \gamma_{2}=1\right)$ at $(\mathrm{y}, \mathrm{z})$, GS was able to faithfully retrieve the underlying undirected graph, Fig. 3d. This is to be expected since the Markov equivalent structure of the three-chain network motif is the undirected graph $(\mathrm{x}-\mathrm{y}-\mathrm{z})$. Increasing the noise variance across the mediator y relative to $\mathrm{z}\left(\gamma_{1}=10 \gg \gamma_{2}=1\right)$ resulted in low confidence along $(\mathrm{y}-\mathrm{z})$ preventing any reliable inference of possible association between these nodes, Fig. 3e. Interestingly, increasing the noise variance on the terminal node z relative to $\mathrm{y}\left(\gamma_{1}=1 \ll \gamma_{2}=10\right)$ resulted in low confidence along $(\mathrm{x}-\mathrm{y})$ preventing any reliable inference of possible association between these nodes, Fig. 3f.

Coherent Type-I feed-forward loop network motif. The coherent Type-I feed-forward loop network motif, Fig. 1c, was

generated using (15) with (α=0.5) and normally distributed noise (ε_{t},η_{t},δ_{t}). While one part of the Type-I FFL resembles the common-effect motif (x→z←y), the other part resembles a three-chain (x→y→z), Fig. 1b. For finite and equal noise variance (γ_{1}=1,γ_{2}=1) at (y,z) the pairwise (16) and conditional dependencies (17) were non-zero. Increasing the noise variance across yrelativetoz(γ_{1}=10≫γ_{2}=1) resulted in pairwise (20) identical to those of the common-effect (6) and three-chain motifs (13) failing to distinguish these network structures. This is reflected by similar profiles across Figs. 2a, 2b and 2c. On a related note, increasing the noise variance across z relative to y(γ_{2}=10≫γ_{1}=1) resulted in pairwise (18) and conditional dependencies (19) identical to those of the three-chain motif (11, 12) failing to distinguish these two distinct network structures. Similarities in the pairwise and conditional dependencies across these motifs are also reflected by similar profiles between Figs. 2b and 2c and between Figs. 2e and 2f respectively. For finite equal noise variance (γ_{1}=1,γ_{2}=1) at (y,z) GS was able to retrieve the undirected edges (x→y→z), Fig. 3g. Failure to retrieve the exact structure, Fig. 1c, can be attributed to the presence of equivalent classes. Increasing the noise variance across z relative to y(γ_{1}=1≫γ_{2}=10) resulted in low confidences along (x→z) and (y→z) relative to (x→y) preventing any reliable inference of possible associations along (x→z) and (y→z), Fig. 3h. Thus for these choices of noise variances it is possible the results of GS for Type I FFL resembles the structure of the three-chain failing to distinguish them. In contrast, increasing the noise variance at y relative to z(γ_{1}=10≪γ_{2}=1) resulted in large edge confidence only along y→z and x→z with low edge confidence along (x→y) Fig. 3i preventing any reliable inference of the network structure.

### 2.4 Application to Molecular Expression Profiles

$$
\begin{bmatrix}
Plc\gamma_t \\
PIP3_t \\
PIP2_t
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 0 \\
α_1 & 0 & 0 \\
α_2 & α_3 & 0
\end{bmatrix}.
\begin{bmatrix}
Plc\gamma_t \\
PIP3_t \\
PIP2_t
\end{bmatrix} + \begin{bmatrix}
\gamma_{0}.ε_t \\
\gamma_{1}.η_t \\
\gamma_{2}.δ_t
\end{bmatrix} \tag{22}
$$

In a recent study [7], signalling mechanisms between 11 molecules were inferred from single-cell data using flow-cytometry in conjunction with Bayesian network structure learning algorithms. The resulting network was shown to validate existing associations as well as discovering novel undocumented associations. Of interest, was the sub-network consisting of three molecules (PIP2, PIP3, Plcγ) weakly connected to the rest of the molecules in the network (see Fig. 3 in [7]). The network structure inferred from the molecular expression data between these three molecules (PIP2, PIP3, Plcγ) consisted of the following directed edges PIP3→PIP2, Plcγ→PIP3 and Plcγ→PIP2. A quick inspection would reveal the resemblance of the relationships between these three molecules (22) to that of coherent Type-I FFL motif (Fig. 1c, Case 3) discussed earlier. The expected and the inferred relationships along with the influence paths for these three molecules can be found in (Table 3, Sachs et al., 2005). While the authors acknowledged that the directionality between (Plcγ→PIP3, recruitment leading to phosphorylation) inferred from the data was opposite to that established in the literature [43] (see Supplementary Material, Table I, Sachs et al., 2005), they successfully validated (PIP3→PIP2, precursor-product) and (Plcγ→PIP2, direct hydrolysis to IP3) [44,45] (see Supplementary Material, Table I, Sachs et al., 2005). While several data sets were

![img-1.jpeg](img-1.jpeg)

Figure 2. The average correlation coefficient and partial correlation estimates across 200 independent realizations of the common-effect, three-chain and coherent Type I feed-forward loop network motifs for various choices of noise variances (γ_{1},γ_{2}) are shown in (a, d), (b, e) and (c, f) respectively. The x-axis labels correspond to the correlation coefficients (ρ_{xy-z},ρ_{xz-z},ρ_{yzz}) in (a, b, c) and partial correlations (ρ_{xy-z},ρ_{xz-z},ρ_{yz-z}) in (d, e, f) respectively. The (circles, squares and triangles) in each of the subplots correspond to noise variances with magnitudes (γ_{1}=1,γ_{2}=1), (γ_{1}=1,γ_{2}=10) and (γ_{1}=10,γ_{2}=1) respectively. The points bounded by the dotted rectangle represent cases that occurred much lesser than 80% of the time as significant (α' = 0.001) across 200 independent realizations. doi:10.1371/journal.pone.0080735.g002

![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian networks inferred using Grow-Shrink algorithm along with Pearson correlation (σ² = 0.01) for the three-gene network motifs, namely: common-effect (a-c), three-chain (d-f) and coherent type-I feed-forward loop (g-i) for various choices of noise variances: (γ₁ = 1,γ₂ = 1), (γ₁ = 1,γ₂ = 10), and (γ₁ = 10,γ₂ = 1). The confidences of the edges (ψ) are represented as percentage of the edges that persisted across 200 independent realizations. Edges with (ψ ≥ 0.80) are shown by solid arrows whereas others (ψ ≤ 0.80) are shown by dotted arrows. Edges with confidence (ψ ≤ 0.05) are deemed noisy and excluded for clarity. doi:10.1371/journal.pone.0080735.g003

investigated in [7], we restrict the present study to the unperturbed data set comprising the expression of (PIP2, PIP3, Plcγ) across 853 single cells. Prior to investigating the impact of noise on the network inference between the three molecules, we found the distribution of the expression levels across the single-cells to be positively skewed, indicating large variations in the expression estimates across the cells. Interestingly, we also found the variance in the expression levels proportional to their average value across the molecules (PIP2, PIP3, Plcγ). Box-Cox [46] transforms are widely used in literature to minimize the skew in the distribution and suppress non-constant variance as a function of magnitude. In the present study, we used the log-transform which is the limiting case of the classical Box-Cox transform to minimize the skew in the distribution of the expression across these three molecules. Therefore, the results across the raw as well as the log-transformed data are presented.

Three different networks (Πₕₛₛₛ = 1,2,3) were investigated. Π₁: Network inferred from the given data; Π₂: Network inferred from data generated from the linear model (22) fit to the given data without any constraints on the model parameters; Π₃: network inferred from data generated by the linear model fit (22) to the given data with constraint on the noise variance to be equal (i.e. γ₀ = γ₁ = γ₂). The above exercise was repeated for the raw as well as the log-transformed protein expression data and the corresponding edge confidences were estimated. The approach is outlined below.

- Step 1: Given the expression Xₘₛ₃ of the three molecules across n = 853 cells.
- Step 2: Generate independent realizations X′ₘₛ₃, i = 1 ... p by resampling Xₘₛ₃ (m < n) with replacement. In the present study, we set (m = 800, p = 200). Set each column in X′ₘₛ₃ to zero-mean.
- Step 3: Set i ← 1.
- Step 4: Infer the network structure from X′ₘₛ₃ using the GS algorithm. Let the resulting network be Π′₁.
- Step 5: Estimate the parameters (i.e. regression coefficients and noise variances (γ₀, γ₁, γ₂) by fitting the linear model (22) to X′ₘₛ₃). Generate Y′ₘₛ₃, using the estimated model parameters and zero-mean i.i.d. noise terms (εᵣ, ηᵣ, δᵣ) sampled from a log-normally distributed noise to accommodate for the positiveskew in the distribution. Infer the network structure from Y′ₘₛ₃ using the GS algorithm. Let the resulting network be Π′₂.
- Step 6: Generate data Z′ₘₛ₃, using the linear model in Step 5 with the additional constraint on equal noise variance (i.e. γ₁ = γ₀; γ₂ = γ₀) in (22). Infer the network structure from Z′ₘₛ₃ using the GS algorithm. Let the resulting network be Π′₃.
- Step 7: Set i ← i + 1.
- Step 8: Repeat Steps 4–7 till i > p.
- Step 9: Estimate the confidences of the edges for each of the networks (Πₕₛₛₛ = 1,2,3).
- Step 10: Repeat Steps 1–9 for the log-transformed data with normally distributed noise as opposed to log-normally distributed noise in Steps 5 and 6.

Raw Data. The networks (Πₕₛₛₛ = 1,2,3) inferred using the raw data for the molecules (PIP2, PIP3, Plcγ) are shown in

![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian networks inferred using Grow-Shrink algorithm from the molecular expression data (PIP2, PIP3, Plcγ) with sample-size 800 and Pearson correlation (ρ = 0.01) are shown in (a–f). Confidences estimated from 200 independent bootstrap realizations are shown along the edges. Edges with (ψ > 0.80) are shown by solid arrows whereas others (ψ ≤ 0.80) are shown by dotted arrows. Edges with confidence (ψ ≤ 0.05) are deemed noisy and excluded for clarity. The edge confidences of the networks (Π1, Π2, Π3) inferred from the raw data are shown in (a), (b) and (c) respectively. Those inferred on the log-transformed data are shown in (d), (e) and (f) respectively. doi:10.1371/journal.pone.0080735.g004

Figs. 4a–4c respectively. Network structures inferred from the raw data (Π1, Step 4) and those of the linear model fit (Π2, Step 5) exhibited considerable similarity as reflected by their edge confidences, Figs. 4a and 4b. The confidence was high along PIP2→PIP3 and Plcγ→PIP3, and markedly low along Plcγ→PIP2, Figs. 4a, 4b. Noise variance estimated from the linear model fit (Step 5) of the raw data revealed around a two-fold difference (i.e. (γ1/γ2) ~ 2.7 ± 0.3). Constraining the noise variance to be equal (i.e. γ1/γ2 = γ0) had a marked effect on the resulting network (Step 6) Π3, Fig. 4c. The edge confidences were considerably high along PIP2→PIP3 as seen earlier (Π1 and Π2), Figs. 4a, 4b. However, relatively smaller edge confidence along between (Plcγ, PIP3) along either directions, Fig. 4c, in contrast to Figs. 4a or 4b was also observed. More importantly, constraining the noise variance also increased the edge confidences between (Plcγ, PIP2) along either directions in contrast to those shown in Figs. 4a and 4b (i.e. Π1, Π2). Thus forcing the noise variance to be equal had a pronounced effect on the inferred network.

**Log-transformed Data.** In order to minimize the impact of skewness on the conclusions, the entire exercise was repeated on the log-transformed data. The resulting networks along with confidence of the edges are shown in Figs. 4d–4f. The networks (Πk, k = 1,2) inferred from the log-transformed data (Π1, Step 4) and those from data generated on the linear model fit (Π2, Step 5) along with the edge confidences are shown in Figs. 4d–4e respectively. The noise variance estimates from the linear model fit to the log-transformed data revealed no marked difference (i.e. (γ1/γ2) ~ 1.1 ± 0.01) in contrast to what was observed in the raw data. Since there were no marked discrepancies in noise variance, forcing the noise variance to be equal (i.e. γ1/γ2 = γ0) had no profound effect on the resulting network (Π3, Step 6) Fig. 4f as expected. This was revealed by the similar edge confidences across Π2 and Π3. Furthermore, it is important to note that the networks (Πk, k = 1,2,3) inferred from the log-transformed data unlike those from raw data, failed to capture any relationship Plcγ and PIP2.

# Discussion

Real-world entities work in concert as a system and not in isolation. Associations between such entities are usually unknown. Inferring associations and network structure from data obtained across the entities is of great interest across a number of disciplines. The recent surge of high-throughput molecular assays in conjunction with a battery of algorithms has facilitated validating established associations while discovering new ones with the potential to assist in novel hypothesis generation. These associations and networks have been shown to capture possible causal relationships under certain implicit assumptions and proven to be useful abstractions of the underlying signaling mechanism. Such an understanding can provide system level insights and often precedes developing meaningful interventions. Several network inference algorithms have been proposed in literature including those that depend on pairwise and conditional dependencies. However, little attention has been given to the impact of possible discrepancies in noise variance across the data obtained across the molecular entities. In molecular settings, such discrepancies can be attributed to several factors including inherent stochastic mechanisms, heterogeneity in cell populations, variations in abundance of the molecules, variation in binding affinities, sensitivity of the measurement device and other experimental artifacts. Understanding the discrepancies in noise variance is critical in order to avoid spurious conclusions and an important step prior to identifying the source of the noise.

The present study clearly elucidated the non-trivial impact of discrepancies in noise variance on associations and network inference algorithms across synthetic as well as experimental data. The impact of large discrepancies in noise variance on associations and network structure inferred from data generated using linear models of popular network motifs and fundamental connections as well as those from experimental protein expression profiles were investigated. Analytical expressions and simulations were presented elucidating the non-trivial impact of noise on three popular molecular network motifs and fundamental connections (common effect, three-chain and coherent Type-I feed-forward loop). It was

shown that discrepancies in noise variance can significantly alter the results of pairwise dependencies, conditional dependencies as well as constraint-based Bayesian network structure learning techniques that implicitly rely on tests for conditional independence. As expected, the discrepancies in noise variances was found to result in markedly different topologies from those of their noise free counterpart challenging reliable inference of the underlying network topology. Such discrepancies were also shown to result in spurious conclusion of similar structures across markedly distinct network topologies. The impact of discrepancies in noise variance were also investigated on publicly available single-cell molecular expression profiles of a sub-network comprising of three molecules (PIP2, PIP3, Plcy) involved in human T-cell signaling. The subnetwork shared considerable resemblance to the coherent Type-I feed-forward loop. The distribution of the raw expression estimates across these three molecules was positively skewed indicating large variations in the expression estimates across the single-cells. Variance about the average expression across the three molecules was found to be markedly different and proportional to their average values. Several factors can contribute to such discrepancies including: abundance of these molecules, antibody binding characteristics, uncertainty due to possible overlap in the wavelengths corresponding to the colors tagged to the molecules. In the present study, a linear model was fit to the molecular expression data. Parameter estimates from the linear model indicated significant discrepancies in the noise variances across the molecules. Adjusting for these discrepancies in the model was shown to significantly affect the edge confidences of the resulting networks, hence the topology. The results were presented on the raw molecular expression data as well as its log-transformed

## Author Contributions

Conceived and designed the experiments: RN. Performed the experiments: RN. Analyzed the data: RN MS. Contributed reagents/materials/analysis tools: RN MS. Wrote the paper: RN MS.

## References

1. Kaern M, Elston TC, Blake WJ, Collins JJ (2005) Stochasticity in gene expression: from theories to phenotypes. Nat Rev Genet 6: 451-464.
2. Okoniewski MJ, Miller CJ (2006) Hybridization interactions between probesets in short oligo microarrays lead to spurious correlations. BMC Bioinf 7: 276.
3. Steen HB (1992) Noise, Sensitivity and Resolution of Flow Cytometers. Cytometry 15: 822-830.
4. Welch CM, Elliott H, Danuser G, Hahn KM (2011) Imaging the coordination of multiple signalling activities in living cells. Nat Rev Mol Cell Biol 12: 749-756.
5. Nagarajan R (2009) A note on inferring acyclic network structures using Granger causality tests. Int. J. Biostatistics 5(1): 10.
6. Nagarajan R, Upreti M (2010) Granger causality analysis of human cell-cycle gene expression profiles. Stat Appl Genet Mol Biol 9(1): 31.
7. Nagarajan R, Upreti M (2011) Inferring functional relationships and causal network structure from gene expression profiles. Meth in Enzymol 487: 133-46.
8. Shen-Orr SS, Milo R, Mangan S, Alon U (2002) Network motifs in the transcriptional regulation network of Escherichia coli. Nat Genet 31(1): 64-8.
9. Mangan S, Alon U (2003) Structure and function of the feed-forward loop network motif. Proc Nat Acad Sci USA 100: 11980-11985.
10. Jensen PV (2001). Bayesian Networks and Decision Graphs. Springer-Verlag.
11. Friedman N, Nachman I, Pe'er D (1999) Learning Bayesian Network Structure from Massive Datasets: The Sparse Candidate Algorithm. Proceedings of the Fifteenth Conference on Uncertainty in Artificial Intelligence (UAI-99), 206215 .
12. Spirtes P, Glymour C, Scheines R (2000) Causation, Prediction and Search. MIT Press.
13. Margaritis D (2003). Learning Bayesian Network Model Structure from Data. Ph.D. thesis, School of Computer Science, Carnegie-Mellon University, Pittsburgh, PA. Available as Technical Report CMU-CS-03-153.
14. Tsamardinos I, Aliferis CF, Statnikov A (2003a) Algorithms for Large Scale Markov Blanket Discovery. In Proceedings of the Sixteenth International Florida Artificial Intelligence Research Society Conference, 376-381.
15. Tsamardinos I, Aliferis CF, Statnikov A (2003b) Time and Sample Efficient Discovery of Markov Blankets and Direct Causal Relations. In KDD '03: Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 673-678.
16. Mock C (1995). Causal Inference and Causal Explanation with Background Knowledge. Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence (UAI-95). 403-410.
17. Aliferis CF, Statnikov A, Tsamardinos I, Mani S, Koutvokos XD (2010a) Local Causal and Markov Blanket Induction for Causal Discovery and Feature

Selection for Classification Part I: Algorithms and Empirical Evaluation. Journal of Machine Learning Research 11: 171-234.
35. Aliferis CF, Statnikov A, Tsamardinos I, Mani S, Kouttukos XD (2010b) Local Causal and Markov Blanket Induction for Causal Discovery and Feature Selection for Classification Part II: Analysis and Extensions. Journal of Machine Learning Research 11: 235-284.
36. Tsamardinos I, Aliferis CF, Statnikov A, Brown LE (2003c). Scaling-Up Bayesian Network Learning to Thousands of Variables using Local Learning Techniques. Technical Report DSL 03-02, 2003, DBMI, Vanderbilt University.
37. Castillo E, Gutiérrez J, Hadi AS (1997). Expert Systems and Probabilistic Network Models. Springer-Verlag.
38. Scutari M (2010) Learning Bayesian Networks with the bulearn R Package. Journal of Statistical Software 35(3): 1-22.
39. Nagarajan R, Lebre S, Scutari M (2013) Bayesian Networks in R: with applications in Systems Biology. Springer-Verlag, NY.
40. Efron B, Tibshirani R (1993). An Introduction to the Bootstrap. Chapman \& Hall.
41. Nagarajan R, Dutta S, Scutari M, Beggs ML, Nolen GT, et al. (2010). Functional Relationships Between Genes Associated with Differentiation Potential of Aged Myogenic Progenitors. Frontiers in Physiology 1(21): 1-8.
42. Scutari M, Nagarajan R (2013) Identifying significant edges in graphical models of molecular networks. Artif Intell Med 57(3): 207-17.
43. Alberts B (2002) Molecular biology of the cell, Garland Science, New York.
44. Soltoniew MV, Howe CL, Mobley WC (2001) Nerve growth factor signaling, neuroprotection and neural repair. Ann Rev Neurosci 24: 1217-81.
45. Lee SB, Rhee SG (1995) Significance of PIP2 hydrolysis and regulation of phospholipase C isozymes. Curr Opin Cell Biol 7: 183-9.
46. Box GEP, Cox DR (1964) An analysis of transformations. J Royal Stat Soc Series B 26 (2): 211-252.
47. Li Y, Tesson BM, Churchill GA, Jansen RC (2010) Critical reasoning on causal inference in genome-wide linkage and association studies. Trends in Genet 26(12): 493-498.