# HIAL open science 

## Inferring dynamic genetic networks with low order independencies

Sophie Lèbre

## To cite this version:

Sophie Lèbre. Inferring dynamic genetic networks with low order independencies. 2009. hal00142109 v 7

## HAL Id: hal-00142109 <br> https://hal.science/hal-00142109v7

Preprint submitted on 29 May 2009

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Inferring dynamic genetic networks with low order independencies 

Sophie Lèbre*<br>s.lebre@imperial.ac.uk<br>Université d'Evry-Val-d'Essone, CNRS UMR 8071, INRA 1152,<br>Laboratoire Statistique et Génome<br>523 place des Terrasses, 91000 Evry, France.

*Current address: Centre for Bioinformatics, Division of Molecular Biosciences, Imperial College London, South Kensington Campus, SW7 2AZ London, UK.


#### Abstract

In this paper, we propose a novel inference method for dynamic genetic networks which makes it possible to deal with a number of time measurements $n$ much smaller than the number of genes $p$. The approach is based on the concept of low order conditional dependence graph which we extend here to the case of Dynamic Bayesian Networks. Most of our results are based on the theory of graphical models associated with Directed Acyclic Graphs (DAGs). In this way, we define a DAG $\hat{\mathcal{G}}$ which describes exactly the full order conditional dependencies given the past of the process. Then, to cope with the large $p$ and small $n$ estimation case, we propose to approximate DAG $\hat{\mathcal{G}}$ by considering low order conditional independencies. We introduce partial $q^{t h}$ order conditional dependence DAGs and analyze their probabilistic properties. In general, DAGs $\mathcal{G}^{(q)}$ differ from $\hat{\mathcal{G}}$ but still reflect relevant dependence facts for sparse networks such as genetic networks. By using this approximation, we set out a non-Bayesian inference method and demonstrate the effectiveness of this approach on both simulated and real data analysis. The inference procedure is implemented in the R package 'G1DBN' which is available from the CRAN archive.

Keywords: conditional independence, Dynamic Bayesian Network, Directed Acyclic Graph, networks inference, time series modelling.


## Introduction

The development of microarray technology allows to simultaneously measure the expression levels of many genes at a precise time point. Thus it has

become possible to observe gene expression levels across a whole process such as the cell cycle or response to radiation or different treatments. The objective is now to recover gene regulation phenomena from this data. We are looking for simple relationships such as "gene $i$ activates gene $j$ ". But we also want to capture more complex scenarios such as auto-regulations, feed-forward loops, multi-component loops... as described by Lee et al. [21] in the case of the transcriptional regulatory network of the yeast Saccharomyces cerevisiae.

To such an aim, we both need to accurately take into account temporal dependencies and to deal with the dimension of the problem when the number $p$ of observed genes is much higher than the number $n$ of observation time points. Moreover we know that most of the genes whose expression has been monitored using microarrays are not taking part in the temporal evolution of the system. So we want to determine the few 'active' genes that are involved in the regulatory machinery, as well as the relationships between them. In short, we want to infer a network representing the dependence relationships which govern a system composed of several agents from the observation of their activity across short time series.

Static Modelling Such gene networks were first described using static modelling and mainly non oriented networks. One of the first tools used to describe interactions between genes is the relevance network [5] or correlation network [36]. Better known as the covariance graph [7] in graphical models theory, this undirected graph describes the pair-wise correlation between genes. Its topology is derived from the covariance matrix between the gene expression levels; an undirected edge is drawn between two variables whenever they are correlated. However, the correlation between two variables may be caused by linkage with other variables. This creates spurious edges due to indirect dependence relationships.

Consequently, there has been great interest in the concentration graph [20], also called the covariance selection model, which describes the conditional dependence structure between gene expression using Graphical Gaussian Models (GGMs). Let $Y=\left(Y^{i}\right)_{1 \leq i \leq p}$ be a multivariate Gaussian vector representing the expression levels of $p$ genes. An undirected edge is drawn between two variables $Y^{i}$ and $Y^{j}$ whenever they are conditionally dependent given the remaining variables (See Figure 1B). The standard theory of estimation in GGMs [20, 46] can be exploited only when the number of measurements $n$ is much higher than the number of variables $p$. This ensures that the sample covariance matrix is positive definite with probability one. However, in most microarray gene expression datasets, we have to cope with the opposite situation $(n<<p)$. Thus, the growing interest in "small $n$, large $p$ " furthered the development of numerous alternatives (Schäfer and Strimmer [31, 32], Waddell and Kishino [44, 43],

![img-0.jpeg](img-0.jpeg)

Figure 1: (A) A biological regulation motif. (B) The concentration graph corresponding to the motif A. For all $i \geq 3, Y^{i}$ is a Gaussian variable representing the expression level of gene $G^{i}$. Some cycles cannot be represented on the concentration graph. (C) Dynamic network equivalent to the regulation motif A. Each vertex $X_{t}^{i}$ represents the expression level of gene $G^{i}$ at time $t$. This graph is acyclic and allows to define a Bayesian network.

Toh and Horimoto [40, 41], Wu et al. [50], Wang et al. [45]). Even though concentration graphs allow to point out some dependence relationships between genes, they do not offer an accurate description of the interactions. Firstly, no direction is given to the interactions. Secondly, some motifs containing cycles as in Figure 1A cannot be properly represented.

Contrary to the previous undirected graphs, Bayesian networks (BNs) [13] model directed relationships. Based on a probabilistic measure, a BN representation of a model is defined by a Directed Acyclic Graph (DAG) and the set of conditional probability distributions of each variable given its parents in the DAG [28]. The theory of graphical models [46, 9, 20] then allows to derive conditional independencies from this DAG. However, the acyclicity constraint in static BNs is a serious restriction given the expected structure of genetic networks.

Dynamic Bayesian networks This limitation can be overcome by employing Dynamic Bayesian networks (DBNs) introduced for the analysis of gene expression time series by Friedman et al. [14] and Murphy and Mian [25]. In DBNs, a gene is no longer represented by a single vertex but by as many vertices as time points in the experiment. A dynamic network (Figure 1C) can then be obtained by unfolding in time the initial cyclic motif in Figure 1A. The direction according to time guarantees the acyclicity of this dynamic network and consequently allows to define a Bayesian network. The nature of the relationships (positive/negative) does not appear in this DAG but is derived from estimates of the model parameters.

The very high number $p$ of genes simultaneously observed raises a dimension problem. Moreover, a large majority of time series gene expression data contain no or very few repeated measurements of the expression level of the same gene at a given time. Hence, we assume that the process is homogeneous across time. This means that the system is considered to be governed by the same rules during the whole experiment. Consequently, the temporal dependencies are homogeneous: any edge is present or absent during the whole process. This is a strong assumption which is not necessarily satisfied. Nevertheless, this condition is necessary to carry out estimation unless we have several measurements of each gene expression at each time point.

Up to now, various DBN representations based on different probabilistic models have been proposed (discrete models [26, 51], multivariate autoregressive process [27], State Space or Hidden Markov Models [29, 49, 30, 3], nonparametric additive regression model $[16,17,19,37])$. See also Kim et al. [18] for a review of such models. Faced with so much diversity, we introduce in this paper sufficient conditions for a model to admit a DBN representation and we set out a concrete interpretation in terms of dependencies between variables by using the theory of graphical models for DAGs.

Our DBN representation is based on a DAG $\tilde{\mathcal{G}}$ (e.g. like the DAG of Fig. 1C) which describes exactly the full order conditional dependencies given all the remaining past variables (See Section 1). This approach extends the principle of the concentration graph showing conditional independencies to the dynamic case.

Dimension reduction Even under the assumption of homogeneity, which enables to use the pairs of successive time point gene expression as repeated measurements, we have to deal with the "curse of dimensionality" when inferring the structure of DAG $\tilde{\mathcal{G}}$. The difficulty lies in coping with the large $p$ and small $n$ estimation case. Several inference methods have been proposed for the estimation of the topology of the DAG defining the various DBNs quoted above. To name a few, Murphy [24] implemented several Bayesian structure learning procedures for dynamic models in the Matlab package BNT (Bayes Net Toolbox); Ong et al. [26] reduce the dimension of the problem by considering prior knowledge; Perrin et al. [29] use an extension of the linear regression; Wu et al. [49] use factor analysis and Beal et al. [3] develop a variational Bayesian method; Zou and Conzen [51] limit potential regulators to the genes with either earlier or simultaneous expression changes and estimate the transcription time lag; Opgen-Rhein and Strimmer [27] proposed a model selection procedure based on an analytic shrinkage approach. However, a powerful approach based on the consideration of zero- and first-order conditional independencies to model

concentration graphs has gained attention. When $n<<p$, Wille et al. $[48,47]$ propose to approximate the concentration graph by the graph $\mathcal{G}_{0-1}$ describing zero- and first-order conditional independence. An edge between the variables $Y^{i}$ and $Y^{j}$ is drawn in the graph $\mathcal{G}_{0-1}$ if and only if, zero- and first-order correlations between these two variables both differ from zero, that is, if

$$
r\left(Y^{i}, Y^{j}\right) \neq 0 \quad \text { and } \quad \forall k \in\{1, \ldots, p\} \backslash\{i, j\}, r\left(Y^{i}, Y^{j} \mid Y^{k}\right) \neq 0
$$

where $r\left(Y^{i}, Y^{j} \mid Y^{k}\right)$ is the partial correlation between $Y^{i}$ and $Y^{j}$ given $Y^{k}$. Hence, whenever the correlation between two variables $Y^{i}$ and $Y^{j}$ can be entirely explained by the effect of some variable $Y^{k}$, no edge is drawn between them.

This procedure allows a drastic dimension reduction: by using first order conditional correlations, estimation can be carried out accurately even with a small number of observations. Even if the graph of zero- and first-order conditional independence differs from the concentration graph in general, it still reflects some measure of conditional independence. Wille et al. show through simulations that the graph $\mathcal{G}_{0-1}$ offers a good approximation of sparse concentration graphs and demonstrate that both graphs coincide exactly if the concentration graph is a forest ([47], Corollary 1). This approach has also been used by Magwene and Kim [22] and de la Fuente et al. [8] for estimating undirected gene networks from microarray gene expression of the yeast Saccharomyces cerevisiae. Castelo and Roverato [6] investigate such undirected $q^{t h}$ order partial independence graphs for $q \geq 1$ and present a thorough analysis of their properties. In this paper, we extend this approach by defining $q^{t h}$ order order conditional dependence DAGs $\mathcal{G}^{(q)}$ for DBN representations. Then, by basing our results on these low order conditional dependence DAGs, we propose a novel inference method for dynamic genetic networks which makes it possible to deal with the "small $n$, large $p$ " problem.

The remainder of the paper is organized as follows. In Section 1, we provide sufficient conditions for a DBN modelling of time series describing temporal dependencies. In particular, we show the existence of a minimal DAG $\hat{\mathcal{G}}$ which allows such a DBN representation. To reduce the dimension of the estimation of the topology of $\hat{\mathcal{G}}$, we propose to approximate $\hat{\mathcal{G}}$ by $q^{t h}$ order conditional dependence DAGs $\mathcal{G}^{(q)}$ and analyze their probabilistic properties in Section 2. From conditions on the topology of $\hat{\mathcal{G}}$ and the faithfulness assumption, we establish inclusion relationships between both DAGs $\hat{\mathcal{G}}$ and $\mathcal{G}^{(q)}$. In Section 3, we exploit our results on DAGs $\mathcal{G}^{(q)}$

Finally, validation is obtained on both simulated and real data in Section 4. We use our inference procedure for the analysis of two microarray time course data sets: the Spellman's yeast cell cycle data [34] and the diurnal cycle data on the starch metabolism of Arabidopsis Thaliana collected

Table 1: Notations


by Smith et al. [33].

# 1 A minimal DBN representation 

Let $P=\{1 \leq i \leq p\}$ describe the set of observed genes and $N=\{1 \leq t \leq n\}$ the set of observation times. In this paper, we consider a discrete-time stochastic process $X=\left\{X_{t}^{i} ; i \in P, t \in N\right\}$ taking real values and assume the joint probability distribution $\mathbb{P}$ of the process $X$ has density $f$ with respect to Lebesgue measure on $\mathbb{R}^{p \times n}$. We denote by $X_{t}=\left\{X_{t}^{i} ; i \in P\right\}$ the set of the $p$ random variables observed at time $t$ and $X_{1: t}=\left\{X_{s}^{i} ; i \in P, s \leq t\right\}$ the set of the random variables observed before time $t$.

The main result of this section is set out in Proposition 3; we show that process $X$ admits a DBN representation according to a minimal DAG $\tilde{\mathcal{G}}$ whose edges describe exactly the set of direct dependencies between successive variables $X_{t-1}^{j}, X_{t}^{i}$ given the past of the process. For an illustration, the minimal DAG $\tilde{\mathcal{G}}$ is given in the case of an $\operatorname{AR}(1)$ model in Subsection 1.2. Most of our results are derived from the theory of graphical models associated with DAGs [20]. Note that, even though we need to consider a homogeneous DBN for the inference of gene interaction networks, the theoretical results introduced in Sections 1 and 2 are valid without assuming homogeneity across time.

### 1.1 Background

Theory of graphical models associated with DAGs Let $\mathcal{G}=(X, E(\mathcal{G}))$ be a DAG whose vertices are the variables $X=\left\{X_{t}^{i} ; i \in P, t \in N\right\}$ and whose set of edges $E(\mathcal{G})$ is a subset of $X \times X$. We quickly recall here elements of the theory of graphical models associated with DAGs [20]. A characterization of a Bayesian Network (BN) representation for a process $X$ is given in Proposition 1.

Definition 1 (Parents, Lauritzen [20]) The parents of a vertex $X_{t}^{i}$ in $\mathcal{G}$, denoted by $p a\left(X_{t}^{i}, \mathcal{G}\right)$, are the variables having an edge pointing towards the vertex $X_{t}^{i}$ in $\mathcal{G}$,

$$
p a\left(X_{t}^{i}, \mathcal{G}\right):=\left\{X_{s}^{j} \text { such that }\left(X_{s}^{j}, X_{t}^{i}\right) \in E(\mathcal{G}) ; j \in P, s \in N\right\}
$$

Proposition 1 (BN representation, Pearl [28]) The probability distribution $\mathbb{P}$ of process $X$ admits a Bayesian Network (BN) representation according to $D A G \mathcal{G}$ whenever its density $f$ factorizes as a product of the conditional density of each variable $X_{t}^{i}$ given its parents in $\mathcal{G}$,

$$
f(X)=\prod_{i \in P} \prod_{t \in N} f\left(X_{t}^{i} \mid p a\left(X_{t}^{i}, \mathcal{G}\right)\right)
$$

Throughout this paper, a central notion is that of conditional independence of random variables. Two random variables $U$ and $V$ are conditionally independent given a third variable $W$ (and we write $U \perp V \mid W$ ) if they are independent in the joint probability distribution $\mathbb{P}_{U, V, W}$ of the three random variables $(U, V, W)$. In other words, $U$ and $V$ are conditionally independent given $W$ if for any possible value $w$ of $W$, variables $U$ and $V$ are independent given the variable $W=w$. This result generalizes to disjoint sets of variables. Such conditional independence relationships can be obtained from a BN representation by using graphical theory associated with DAGs, which is essentially based on the directed global Markov property recalled in Proposition 2.
Definition 2 (Moral graph, Lauritzen [20]) The moral graph $\mathcal{G}^{m}$ of $D A G \mathcal{G}$ is obtained from $\mathcal{G}$ by first 'marrying' the parents (draw an undirected edge between each pair of parents of each variable $X_{t}^{i}$ ) and then deleting the directions of the original edges of $\mathcal{G}$. For an illustration, Figure 2A displays the moral graph of the DAG in Figure 1C.

Definition 3 (Ancestral set, Lauritzen [20]) The subset $S$ is ancestral if and only if, for all $\alpha \in S$, the parents of $\alpha$ satisfy $p a(\alpha, \mathcal{G}) \subseteq S$. Hence, for any subset $S$ of vertices, there is a smallest ancestral set containing $S$ which is denoted by $A n(S)$. Then $\mathcal{G}_{A n(S)}$ refers to the graph of the smallest ancestral set $A n(S)$. See Figure $2 B$ for an illustration.

Proposition 2 (Directed global Markov property, Lauritzen [20], Corollary 3.23) Let $\mathbb{P}$ admit a $B N$ representation according to $\mathcal{G}$. Then,

$$
E \Perp F \mid S
$$

whenever all paths from $E$ to $F$ intersect $S$ in $\left(\mathcal{G}_{A n(E \cup F \cup S)}\right)^{m}$, the moral graph of the smallest ancestral set containing $E \cup F \cup S$. We say that $S$ separates $E$ from $F$.

![img-1.jpeg](img-1.jpeg)

Figure 2: (A) Moral graph of the DAG in Figure 1C. For all $t>1$, the parents of the variable $X_{t}^{1}$ are 'married', that is connected by an undirected edge. (B) Moral graph of the smallest ancestral set containing the variables $X_{t+1}^{1}$, its parents in the DAG in Figure 1C and $X_{t}^{3}$. As the set $\left(X_{t}^{1}, X_{t}^{2}\right)$ blocks all paths between $X_{t}^{3}$ and $X_{t+1}^{1}$, thus $\left\{X_{t}^{1}, X_{t}^{2}\right\}$ separates $X_{t+1}^{1}$ from $X_{t}^{3}$ and we have $X_{t+1}^{1} \Perp X_{t}^{3} \mid\left(X_{t}^{1}, X_{t}^{2}\right)$.

Sufficient conditions for DBNs representation We recall here sufficient conditions under which the probability distribution $\mathbb{P}$ of process $X$ admits a BN representation according to a dynamic network (e.g. in Figure 1C). We first assume that the observed process $X_{t}$ is first-order Markovian (Assumption 1). That is, the expression level of a gene at a given time $t$ only depends on the past through the gene expression levels observed at the previous time $t-1$. Then we assume that the variables observed simultaneously are conditionally independent given the past of the process (Assumption 2). In other words, we consider that time measurements are close enough so that gene expression level $X_{t}^{i}$ measured at time $t$ is better explained by the previous time expression levels $X_{t-1}$ than by some current expression level $X_{t}^{j}$.

Assumption 1 The stochastic process $X_{t}$ is first-order Markovian, that is,

$$
\forall t \geq 3, \quad X_{t} \Perp X_{1: t-2} \mid X_{t-1}
$$

Assumption 2 For all $t \geq 1$, the random variables $\left\{X_{t}^{i}\right\}_{i \in P}$ are conditionally independent given the past of the process $X_{1: t-1}$, that is,

$$
\forall t \geq 1, \forall i \neq j, \quad X_{t}^{i} \Perp X_{t}^{j} \quad X_{1: t-1}
$$

Assumptions 1 and 2 allow the existence of a DBN representation of the distribution $\mathbb{P}$ according to DAG $\mathcal{G}_{\text {full }}=\left(X,\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right)\right\}_{i, j \in P, t>1}\right)$
which contains all the edges pointing out from a variable observed at some time $t-1$ towards a variable observed at the next time $t$ (See Lemma 1 in Appendix A.1). The direction of the edges according to time guarantees the acyclicity of $\mathcal{G}_{\text {full }}$.

# 1.2 Minimal DAG $\tilde{\mathcal{G}}$ 

Existence and definition Among the DAGs included in $\mathcal{G}_{\text {full }}$, we show that the probability distribution $\mathbb{P}$ factorizes according to a minimal DAG, which we denote by $\tilde{\mathcal{G}}$ (See Lemma 2, Appendix A.1). The set of edges of $\tilde{\mathcal{G}}$ is exactly the set of full order conditional dependencies between successive variables given the past of the process as set up in the Proposition 3 (See Proof in Appendix A.2).

Proposition 3 (Existence of minimal DAG $\tilde{\mathcal{G}}$, the smallest subgraph
of $\mathcal{G}_{\text {full }}$ allowing DBN modelling) Let $P_{j}=P \backslash\{j\}$ and $X_{t}^{P_{j}}=\left\{X_{t}^{k} ; k \in\right.$ $\left.P_{j}\right\}$ refer to the set $P_{j}$ of $p-1$ variables observed at time $t$. Whenever Assumptions 1 and 2 are satisfied, the probability distribution $\mathbb{P}$ admits a $D B N$ representation according to $D A G \tilde{\mathcal{G}}$ whose edges describe exactly the full order conditional dependencies between successive variables $X_{t-1}^{j}$ and $X_{t}^{i}$ given the remaining variables $X_{t-1}^{P_{j}}$ observed at time $t-1$,

$$
\tilde{\mathcal{G}}=\left(X,\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right) ; X_{t}^{i} \not X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right\}_{i, j \in P, t \in N}\right)
$$

Moreover, $D A G \tilde{\mathcal{G}}$ is the smallest subgraph of $\mathcal{G}_{\text {full }}$ according to which $\mathbb{P}$ admits a DBN representation.

Thus in DAG $\tilde{\mathcal{G}}$, the set of parents $p a\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$ of a variable $X_{t}^{i}$ is the smallest subset of $X_{t-1}$ such that the conditional densities satisfy $f\left(X_{t}^{i} \mid p a\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)\right)=$ $f\left(X_{t}^{i} \mid X_{t-1}\right)$. The set of parents of a variable can be seen as the only variables on which this variable depends directly. So $\tilde{\mathcal{G}}$ is the DAG we want to infer in order to recover potential regulation relationships from gene expression time series. From Proposition 3, any pair of successive variables $\left(X_{t-1}^{j}, X_{t}^{i}\right)$ which are non adjacent in $\tilde{\mathcal{G}}$ are conditionally independent given the parents of $X_{t}^{i}$. In short, for all $i, j$ in $P$, for all $t>1$, we have,

$$
\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E(\tilde{\mathcal{G}}) \quad \Leftrightarrow \quad X_{t}^{i} \Perp X_{t-1}^{j} \mid p a\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)
$$

We will make use of this result in Section 2 in order to define low order conditional dependence DAGs for the inference of $\tilde{\mathcal{G}}$.

Minimal DAG $\tilde{\mathcal{G}}$ for an AR(1) process Consider the following first order auto-regressive model $(\operatorname{AR}(1))$ with a diagonal error covariance matrix $\Sigma$,

$$
\begin{aligned}
& X_{1} \sim \mathcal{N}\left(\mu_{1}, \Sigma_{1}\right) \\
& \forall t>1, \quad X_{t}=A X_{t-1}+B+\varepsilon_{t}, \quad \varepsilon_{t} \sim \mathcal{N}(0, \Sigma) \\
& \forall s, t \in N, \operatorname{Cov}\left(\varepsilon_{t}, \varepsilon_{s}\right)=\delta_{t s} \Sigma \\
& \forall s>t, \quad \operatorname{Cov}\left(X_{t}, \varepsilon_{s}\right)=0
\end{aligned}
$$

where $A=\left(a_{i j}\right)_{1 \leq i \leq p, 1 \leq j \leq p}$ is a real matrix of size $p \times p, B=\left(b_{i}\right)_{1 \leq i \leq p}$ is a real column vector, $\Sigma=\operatorname{Diag}\left(\sigma_{i t}^{2}\right)_{1 \leq i \leq p}$ is the diagonal error covariance matrix of size $p \times p$ and for all $s, t$ in $N, \delta_{t s}=\mathbf{1}_{\{s=t\}}$. Equation (5) implies that the coefficient matrices are uniquely determined from the covariance function of $X_{t}$.

This modelling assumes homogeneity across time (constant matrix $A$ ) and linearity of the dependency relationships. From (3) and (5), the model is first order Markovian (Assumption 1). From (4), Assumption 2 is satisfied whenever the error covariance matrix $\Sigma$ is diagonal. Thus from Proposition 3, the probability distribution of the $\operatorname{AR}(1)$ process defined by equations (2-5) factorizes according to the minimal DAG $\tilde{\mathcal{G}}_{A R(1)}$ whose edges correspond to the non-zero coefficients of matrix $A$. Indeed, if matrix $\Sigma$ is diagonal, each element $a_{i j}$ is the regression coefficient of the variable $X_{t}^{i}$ on $X_{t-1}^{j}$ given $X_{t-1}^{P_{j}}$, that is

$$
a_{i j}=\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right) / \operatorname{Var}\left(X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right)
$$

As process X is Gaussian, the set of null coefficients of matrix $A$ exactly describes the conditional independencies between successive variables, thus if $\Sigma$ is diagonal, we have,

$$
a_{i j}=0 \quad \Leftrightarrow \quad \forall t>1, \quad X_{t}^{i} \Perp X_{t-1}^{j} \mid X_{t-1}^{P_{j}}
$$

Finally, DAG $\tilde{\mathcal{G}}_{A R(1)}$ has an edge between two successive variables $X_{t-1}^{j}$ and $X_{t}^{i}$, for all $t>1$, whenever the coefficient $a_{i j}$ of the matrix $A$ differs from zero,

$$
\tilde{\mathcal{G}}_{A R(1)}:=\left(X,\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right) \text { such that } a_{i j} \neq 0 ; t>1, i, j \in P\right\}\right)
$$

As an illustration, any $\operatorname{AR}(1)$ process whose matrix $\Sigma$ is diagonal and matrix $A$ has the following form,

$$
A=\left(\begin{array}{ccc}
a_{11} & a_{12} & 0 \\
a_{21} & 0 & 0 \\
0 & a_{32} & 0
\end{array}\right)
$$

admits a BN representation according to the dynamic network of Fig.1C $(p=3)$.

# 2 Introducing $q^{t h}$ order dependence DAGs $\mathcal{G}^{(q)}$ for DBNs 

In this paper, we propose to use the DBN modelling according to DAG $\tilde{\mathcal{G}}$ (introduced in Proposition 3) to model genetic regulatory networks from gene expression time series. Reverse discovery of DAG $\tilde{\mathcal{G}}$ requires to determine, for each variable $X_{t}^{i}$, the set of variables $X_{t-1}^{j}$ observed at time $t-1$ on which variable $X_{t}^{i}$ is conditionally dependent given the remaining variables $X_{t-1}^{P_{j}}$. However, even under the time homogeneity assumption discussed in the introduction, standard estimation methods do not allow

us to infer the parameters of a regression model for $p$ genes (i.e. $p^{2}$ possible edges) from $n p$ measurements. We still have to face the 'curse of dimensionality' since the number of genes $p$, is much higher than the number of measurements $n$.

In order to reduce the dimension, we approximate DAG $\tilde{\mathcal{G}}$ by $q^{t h}$ order conditional dependence DAGs $\mathcal{G}^{(q)}(q<p)$. To such an end, we extend to DBNs the approach based on the consideration of low order independencies introduced by Wille et al. $[48,47]$ for GGM approximation (See more details on low order independence graphs for GGMs in Section ). After defining $q^{t h}$ order conditional dependence DAGs $\mathcal{G}^{(q)}$ for DBNs, we investigate the manner in which they allow us to approximate the DAG $\tilde{\mathcal{G}}$ describing full order conditional dependencies.

# 2.1 DAG $\mathcal{G}^{(q)}$ definition 

Let $q$ be smaller than $p$. In the $q^{t h}$ order dependence DAG $\mathcal{G}^{(q)}$, whenever there exists a subset $X_{t-1}^{Q}$ of $q$ variables among the set of $p-1$ variables $X_{t-1}^{P_{j}}$ such that $X_{t-1}^{j}$ and $X_{t}^{i}$ are conditionally independent given $X_{t-1}^{Q}$, no edge is drawn between the two successive variables $X_{t-1}^{j}$ and $X_{t}^{i}$. In short, DAGs $\mathcal{G}^{(q)}$ are defined as follows,

## Definition 4 $q^{t h}$-order conditional dependence DAG $\mathcal{G}^{(q)}$

$\forall q<p, \mathcal{G}^{(q)}=\left(X,\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right) ; \forall Q \subseteq P_{j},|Q|=q, X_{t}^{i} \not \perp X_{t-1}^{j} \mid X_{t-1}^{Q}\right\}_{i, j \in P, t \in N}\right)$.
DAGs $\mathcal{G}^{(q)}$ offer a way of producing dependence relationships between the variables, but they are no longer associated with a BN representation which would call for more global relationships. Note that the definition of $q^{t h}$ order partial dependence DAG $\mathcal{G}^{(q)}$ is based on exact $q^{t h}$ order independencies (not on all partial independencies lower than $q$ as in the partial order correlation network used by Wille and Bühlmann [47]). Indeed, we consider that including only the $q^{t h}$ order dependencies better reflects the true DAG $\tilde{\mathcal{G}}$. In particular, for $p$ variables, DAG $\mathcal{G}^{(p-1)}$ is DAG $\tilde{\mathcal{G}}$. This definition is possible for DBNs because dynamic modelling essentially differs from static correlation network modelling ${ }^{1}$.

In general, DAGs $\mathcal{G}^{(q)}$ differ from DAG $\tilde{\mathcal{G}}$. For instance, the approximation of the DAG of Figure 1C by the $1^{\text {st }}$ order conditional dependence

[^0]
[^0]:    ${ }^{1}$ In particular, contrary to the case of correlation network, the " V " structures (or structures with multiple parents) do not generate spurious edges in the case of DBN since the definition of the DAG $\tilde{\mathcal{G}}$ defining full order dependencies does not allow edges between variables observed at the same time. Thus, for instance, when considering the following " V " structure $X_{t-1}^{j} \rightarrow X_{t}^{i} \leftarrow X_{t-1}^{k}$, no spurious edge can be inferred between the variables $X_{t-1}^{j}$ and $X_{t-1}^{k}$.

![img-2.jpeg](img-2.jpeg)

Figure 3: First-order conditional dependence DAG $\mathcal{G}^{(1)}$ (obtained from the DAG in Figure 1C). The spurious dashed arrow may appear in $\mathcal{G}^{(1)}$.

DAG may give rise to the spurious edge $X_{t}^{3} \rightarrow X_{t+1}^{1}$, for all $t<n$ (See Figure 3). Indeed, $X_{t}^{1}$ (resp. $X_{t}^{2}$ ) does not separate $X_{t+1}^{1}$ from $X_{t}^{3}$ in the smallest moral graph containing the variables $X_{t+1}^{1} \cup X_{t}^{3} \cup X_{t}^{1}$ (resp. $X_{t+1}^{1} \cup X_{t}^{3} \cup X_{t}^{2}$ ) displayed in Figure 2B. Nevertheless, if the vertices of $\tilde{\mathcal{G}}$ have few parents, DAGs $\mathcal{G}^{(q)}$ bring relevant information about the topology of $\tilde{\mathcal{G}}$, even for small values of $q$. In the following, we give characterizations of low order conditional dependence DAGs $\mathcal{G}^{(q)}$ and analyze the accuracy of the approximations they offer.

# 2.2 A restricted number of parents 

In some known gene regulation mechanisms, it is the case that a few genes regulate many other genes (e.g. the single input modules in the transcriptional regulatory network of $S$. Cerevisiae [21]). However, we do not expect a single gene to be regulated by many genes at the same time. So the number of parents in gene interaction networks is expected to be relatively small. In this section, we analyze the properties of $\mathcal{G}^{(q)}$ when the number of parents in $\tilde{\mathcal{G}}$ is lower than $q$.

Let us denote by $N_{\mathrm{pa}}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$ the number of parents of $X_{t}^{i}$ in DAG $\tilde{\mathcal{G}}$ and $N_{\mathrm{pa}}^{\mathrm{Max}}(\tilde{\mathcal{G}})$ the maximal number of parents of any variable $X_{t}^{i}$ in $\tilde{\mathcal{G}}$,

$$
N_{\mathrm{pa}}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)=\left|p a\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)\right|, \quad N_{\mathrm{pa}}^{\mathrm{Max}}(\tilde{\mathcal{G}})=\operatorname{Max}_{i \in P, t \in N}\left(N_{\mathrm{pa}}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)\right)
$$

The next results hold when the number of parents in $\tilde{\mathcal{G}}$ is restricted.
Proposition 4 If $N_{p a}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right) \leq q$ then we have,

$$
\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E(\tilde{\mathcal{G}})\right\} \Rightarrow\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E\left(\mathcal{G}^{q}\right)\right\}
$$

Corollary 1 For all $q \geq N_{p a}^{\text {Max }}(\tilde{\mathcal{G}})$, we have $\tilde{\mathcal{G}} \supseteq \mathcal{G}^{(q)}$.
Proposition 5 Let $X$ be a Gaussian process. If $N_{p a}^{\text {Max }}(\tilde{\mathcal{G}}) \leq 1$ then $\tilde{\mathcal{G}}=\mathcal{G}^{(1)}$.
Consider a variable $X_{t}^{i}$ having at most $q$ parents in $\tilde{\mathcal{G}}(q<p)$. Let $X_{t-1}^{j}$ be a variable observed at the previous time $t-1$ and having no edge pointing towards $X_{t}^{i}$ in $\tilde{\mathcal{G}}$. In the moral graph of the smallest ancestral set

containing $X_{t}^{i} \cup X_{t-1}^{j} \cup \operatorname{pa}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$, the set of parents $\operatorname{pa}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$ separates $X_{t}^{i}$ from $X_{t-1}^{j}$. From Proposition 2, we have $X_{t}^{i} \perp X_{t-1}^{j} \mid \operatorname{pa}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$. The number of parents $\operatorname{pa}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right)$ is smaller than $q$, so the edge $X_{t-1}^{j} \rightarrow X_{t}^{i}$ is not in $\mathcal{G}^{(q)}$. This establishes Proposition 4. Consequently, if the maximal number of parents in $\tilde{\mathcal{G}}$ is lower than $q$, then $\mathcal{G}^{(q)}$ is included in $\tilde{\mathcal{G}}$ (Corollary 1). In this case, $\mathcal{G}^{(q)}$ does not contain spurious edges.

The converse inclusion relationship is not true in general ${ }^{2}$. Nevertheless, if each variable has at most one parent, the converse inclusion $\tilde{\mathcal{G}} \subseteq \mathcal{G}^{(1)}$ is true if the process is Gaussian and $q=1$ (Proposition 5, see proof in Appendix A.2). At a higher order, we need to assume that all conditional independencies can be derived from $\tilde{\mathcal{G}}$, that is $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$.

# 2.3 Faithfulness 

Definition 5 (faithfulness, Spirtes [35]) A distribution $\mathbb{P}$ is faithful to a $D A G \mathcal{G}$ if all and only the independence relationships true in $\mathbb{P}$ are entailed by $\mathcal{G}$ (as set up in Proposition 2).

Theorem 1 (Measure zero for unfaithful Gaussian (Spirtes [35]) and discrete (Meek [23]) distributions) Let $\pi_{\mathcal{G}}^{N}\left(\right.$ resp. $\left.\pi_{\mathcal{G}}^{N}\right)$ be the set of linearly independent parameters needed to parameterize a multivariate normal distribution (resp. discrete distribution) $\mathbb{P}$ which admits a factorization according to a $D A G \mathcal{G}$. The set of distributions which are unfaithful to $\mathcal{G}$ has measure zero with respect to Lebesgue measure over $\pi_{\mathcal{G}}^{N}$ (resp. over $\pi_{\mathcal{G}}^{P}$ ).

From Definition 5, whenever the distribution $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$, any subset $X_{t-1}^{Q} \subseteq X_{t-1}$, with respect to which $X_{t}^{i}$ and $X_{t-1}^{j}$ are conditionally independent, separates $X_{t}^{i}$ and $X_{t-1}^{j}$ in the moral graph of the smallest ancestral set containing $X_{t}^{i} \cup X_{t-1}^{j} \cup X_{t-1}^{Q}$. Under this assumption, we can derive interesting properties on $\tilde{\mathcal{G}}$ from the topology of low order dependence DAGs $\mathcal{G}^{(q)}$. As there is no way to assess a probability distribution to be faithful to a DAG, this assumption has often been criticized. However, Theorem 1, established by Spirtes [35] for the Gaussian distribution and extended to discrete distributions by Meek [23], makes this assumption

[^0]
[^0]:    ${ }^{2}$ As an illustration, let $X_{t-1}^{j} \rightarrow X_{t}^{i}$ be an edge of $\tilde{\mathcal{G}}$ then in essence (See Prop 3) $X_{t}^{i}$ and $X_{t-1}^{j}$ are conditionally dependent given the remaining variables $X_{t-1}^{P_{j}}$. There may however exist a subset of $q$ variables $X_{t-1}^{Q}$, where $Q$ is a subset of $P \backslash\{j\}$ of size $q$, such that $X_{t}^{i}$ and $X_{t-1}^{j}$ are conditionally independent with respect to this subset $X_{t-1}^{Q}$. Indeed, even though the topology of $\tilde{\mathcal{G}}$ allows us to establish some conditional independencies, DAG $\tilde{\mathcal{G}}$ does not necessarily allow to derive all of them. Two variables can be conditionally independent given a subset of variables whereas this subset does not separate these two variables in $\tilde{\mathcal{G}}$.

reasonable at least in a measure-theoretic sense. Moreover this assumption remains very reasonable in a modelling framework where the network to be inferred describes actual interaction relationships. The next propositions are derived from the faithfulness of the distribution $\mathbb{P}$ to $\tilde{\mathcal{G}}$ (See proofs in Appendix A.2).

Proposition 6 Assume $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$. For all $q<p$, we have $\tilde{\mathcal{G}} \subseteq \mathcal{G}^{(q)}$.
Corollary 2 Assume $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$. For all $q \geq N_{p a}^{\text {Max }}(\tilde{\mathcal{G}})$, we have $\tilde{\mathcal{G}}=\mathcal{G}^{(q)}$.

Proposition 7 Assume $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$.
If $N_{p a}\left(X_{t}^{i}, \mathcal{G}^{(q)}\right) \leq q$ then $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E\left(\mathcal{G}^{(q)}\right) \Rightarrow\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E(\tilde{\mathcal{G}})$.
Corollary 3 Assume $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$. For all $q \geq N_{p a}^{\text {Max }}\left(\mathcal{G}^{(q)}\right), \tilde{\mathcal{G}}=\mathcal{G}^{(q)}$.
Whenever $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}, \operatorname{DAG} \mathcal{G}^{(q)}$ contains DAG $\tilde{\mathcal{G}}$ (Proposition 6). Even though we expect the number of parents in a gene interaction networks to be bounded aboce, the exact maximal number of parents $N_{\mathrm{pa}}^{\text {Max }}(\tilde{\mathcal{G}})$ remains mostly unknown. However, we show that the edges of DAG $\mathcal{G}^{(q)}$ pointing towards a variable having less than $q$ parents in $\mathcal{G}^{(q)}$ are edges of $\tilde{\mathcal{G}}$ too (Proposition 7). Thus, if $\mathbb{P}$ is faithful to $\tilde{\mathcal{G}}$, knowledge of the topology of DAG $\mathcal{G}^{(q)}$ only allows us to ascertain some edges of DAG $\tilde{\mathcal{G}}$. From Propositions 6 and 7, we establish that both DAG $\mathcal{G}^{(q)}$ and DAG $\tilde{\mathcal{G}}$ exactly coincide if any node of $\mathcal{G}^{(q)}$ has less than $q$ parents (Corollary 3).

# $3 \quad G 1 D B N$, a procedure for DBN inference 

We introduced and characterized the $q^{t h}$ order dependence DAGs $\mathcal{G}^{(q)}$, for all $q<p$, for dynamic modelling. We now exploit our results to develop a non-Bayesian inference method for DAG $\tilde{\mathcal{G}}$ defining a DBN representation for process $X$. Let $q_{\max }$ be the maximal number of parents in $\tilde{\mathcal{G}}$. From Corollary 3, inferring $\tilde{\mathcal{G}}$ amounts to inferring $\mathcal{G}^{\left(q_{\max }\right)}$. However, the inference of $\mathcal{G}^{\left(q_{\max }\right)}$ requires to check, for each pair $(i, j)$, if there exists a subset $Q \subseteq P_{j}$ of dimension $q_{\max }$ such that $X_{t}^{i} \Perp X_{t-1}^{j} \mid X_{t-1}^{Q}$ for all $t>1$. So, for each pair $(i, j)$, there are $\binom{q_{\max }}{p-1}$ potential sets that can lead to conditional independence. To test each conditional independence given any possible subset of $q_{\max }$ variables is questionable both in terms of complexity and multiple testings.

To circumvent these issues, we propose to exploit the fact that the true DAG $\tilde{\mathcal{G}}$ is a subgraph of $\mathcal{G}^{(1)}$ (Proposition 6) in order to develop an inference procedure for $\tilde{\mathcal{G}}$. Indeed, the inference of $\mathcal{G}^{(1)}$ is both faster (complexity) and more accurate (number of tests). Thus we introduce a 2 step-procedure

for DBN inference. In the first step, we infer the $1^{\text {st }}$ order dependence DAG $\mathcal{G}^{(1)}$, then we infer DAG $\tilde{\mathcal{G}}$ from the estimated DAG $\hat{\mathcal{G}}^{(1)}$. This 2 step-procedure, summarized in Figure 4, is implemented in a R package 'G1DBN' [1] freely available from the Comprehensive R Archive Network.

# 3.1 Step 1: inferring $\mathcal{G}^{(1)}$ 

We evaluate the likelihood of an edge $\left(X_{t-1}^{j}, X_{t}^{i}\right)$ by measuring the conditional dependence between the variables $X_{t-1}^{j}$ and $X_{t}^{i}$ given any variable $X_{t-1}^{k}$. Assuming linear dependencies, we consider the partial regression coefficient $a_{i j \mid k}$ defined as follows,

$$
X_{t}^{i}=m_{i j k}+a_{i j \mid k} X_{t-1}^{j}+a_{i k \mid j} X_{t-1}^{k}+\eta_{t}^{i, j, k}
$$

where the rank of the matrix $\left(X_{t-1}^{j}, X_{t-1}^{k}\right)_{t \geq 2}$ equals 2 and the errors $\left\{\eta_{t}^{i, j, k}\right\}_{t \geq 2}$ are centered, have same variance and are not correlated.

We measure the conditional dependence between the variables $X_{t-1}^{j}$ and $X_{t}^{i}$ given any variable $X_{t-1}^{k}$ by testing the null assumption $\mathcal{H}_{0}^{i, j, k}$ : " $a_{i j \mid k}=$ $0^{\prime \prime}$. To such an aim, we use one out of three M-estimators for this coefficient: either the familiar Least Square (LS) estimator, the Huber estimator, or the Tukey bisquare (or biweight) estimator. The two latter are robust estimators [12]. Then for each $k \neq j$, we compute the estimates $\hat{a}_{i j \mid k}$ according to one of these three estimators and derive the p-value $p_{i j, k}$ from the standard significance test:

$$
\text { under }\left(\mathcal{H}_{0}^{i, j, k}\right): \text { " } a_{i j \mid k}=0 \text { ", } \quad \frac{\hat{a}_{i j \mid k}}{\hat{\sigma}\left(\hat{a}_{i j \mid k}\right)} \sim t(n-4)
$$

where $t(n-4)$ refers to a student probability distribution with $n-4$ degrees of freedom and $\hat{\sigma}\left(\hat{a}_{i j \mid k}\right)$ is the variance estimates for $\hat{a}_{i j \mid k}$.

Thus, we assign a score $S_{1}(i, j)$ to each potential edge $\left(X_{t-1}^{j}, X_{t}^{i}\right)$ equal to the maximum $\operatorname{Max}_{k \neq j}\left(p_{i j \mid k}\right)$ of the $p-1$ computed p-values, that is the most favorable result to $1^{\text {st }}$ order conditional independence. This procedure does not derive p-values for the edges but allows to order the possible edges of DAG $\mathcal{G}^{(1)}$ according to how likely they are. The smallest scores point out the most significant edges for $\mathcal{G}^{(1)}$. The inferred DAG $\hat{\mathcal{G}}^{(1)}$ contains the edges assigned a score below a chosen threshold $\alpha_{1}$.

### 3.2 Step 2: inferring $\tilde{\mathcal{G}}$ from $\mathcal{G}^{(1)}$

We use the inferred DAG $\hat{\mathcal{G}}^{(1)}$ as a reduction of the search space. Indeed, from faithfulness, we know that $\tilde{\mathcal{G}} \subseteq \mathcal{G}^{(1)}$ (Proposition 6). Moreover, when DAG $\tilde{\mathcal{G}}$ is sparse, there are far fewer edges in $\mathcal{G}^{(1)}$ than in the complete DAG $\mathcal{G}_{\text {full }}$ defined in Section 1.1. Consequently, the number of parents of each variable in $\hat{\mathcal{G}}^{(1)}$ is much smaller than $n$. Then model selection can be

```
Choose either LS, Huber or Tukey estimator and set \(\alpha_{1}\) and \(\alpha_{2}\)
thresholds.
    Step 1: inferring \(\mathcal{G}^{(1)}\).
For all \(i \in P\),
For all \(j \in P\), for all \(k \neq j\), compute the p-value \(p_{i j \mid k}\) from (7),
\(S_{1}(i, j)=\operatorname{Max}_{k \neq j}\left(p_{i j \mid k}\right)\).
\(E\left(\hat{\mathcal{G}}^{(1)}\right)=\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right)_{t>1} ; i, j \in P\right.\), such that \(S_{1}(i, j)<\alpha_{1}\right\}\).
    Step 2: inferring \(\hat{\mathcal{G}}\) from \(\hat{\mathcal{G}}^{(1)}\).
If \(N_{p a}^{M a x}\left(\hat{\mathcal{G}}^{(1)}\right) \sim n-1\), choose a higher threshold \(\alpha_{1}\) and go to Step1.
For all \(i\) such that \(N_{p a}\left(X_{t}^{i}, \hat{\mathcal{G}}^{(1)}\right) \geq 1\), compute the p-value \(p_{i j}^{(2)}\) from (9).
\(S_{2}(i, j)=\left\{\begin{array}{cl}p_{i j}^{(2)} & \text { for all } i, j \in P \text { such that }\left(X_{t-1}^{j}, X_{t}^{i}\right)_{t>1} \in \hat{\mathcal{G}}^{(1)}\right.\), \\ 1 & otherwise. \\ E(\hat{\mathcal{G}})=\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right)_{t>1} ; i \in P,(i, j) \in P\right.\) such that \(S_{2}(i, j)<\alpha_{2}\}\).
```

Figure 4: Outline of the 2 step-procedure G1DBN for DBN inference.
carried out using standard estimation and tests among the edges of $\hat{\mathcal{G}}^{(1)}$. For each pair $(i, j)$ such that the set of edges $\left(X_{t-1}^{j}, X_{t}^{i}\right)_{t>1}$ is in $\hat{\mathcal{G}}^{(1)}$, we denote by $a_{i j}^{(2)}$ the regression coefficient,

$$
X_{t}^{i}=m_{i}+\sum_{j \in \operatorname{pa}\left(X_{t}^{i}, \hat{\mathcal{G}}^{(1)}\right)} a_{i j}^{(2)} X_{t-1}^{j}+\eta_{t}^{i}
$$

where the rank of the matrix $\left(X_{t-1}^{j}\right)_{t \geq 2, j \in \operatorname{pa}\left(X_{t}^{i}, \hat{\mathcal{G}}^{(1)}\right)}$ is $\left|p a\left(X_{t}^{i}, \hat{\mathcal{G}}^{(1)}\right)\right|$ and the errors $\left\{\eta_{t}^{i}\right\}_{t \geq 2}$ are centered, have the same variance, and are not correlated. We assign to each edge of $\hat{\mathcal{G}}^{(1)}$ a score $S_{2}(i, j)$ equal to the p-value $p_{i j}^{(2)}$ derived from the significance test,

$$
\text { under }\left(\mathcal{H}_{0}^{i, j}\right): \text { " } a_{i j}^{(2)}=0 \text { ", } \quad \frac{\hat{a}_{i j}^{(2)}}{\hat{\sigma}\left(\hat{a}_{i j}^{(2)}\right)} \sim t\left(n-1-\left|p a\left(X_{t}^{i}, \hat{\mathcal{G}}^{(1)}\right)\right|\right)
$$

The score $S_{2}(i, j)=1$ is assigned to the edges that are not in $\hat{\mathcal{G}}^{(1)}$. The smallest scores indicate the most significant edges. The inferred DAG for $\hat{\mathcal{G}}$ contains those edges whose score is below a chosen threshold $\alpha_{2}$.

When $\hat{\mathcal{G}}$ is sparse, Step 1 of G1DBN inference procedure gives already a good estimation of $\hat{\mathcal{G}}$ (See Precision-Recall curves obtained for simulated data in Figure 5). Even better results can be obtained with the 2 stepprocedure which requires to tune two parameters $\alpha_{1}$ and $\alpha_{2}$. Parameter $\alpha_{1}$ is the selection threshold of the edges of $\hat{\mathcal{G}}^{(1)}$ in Step 1 (that is the dimension reduction threshold), whereas parameter $\alpha_{2}$ is the selection threshold for the edges of $\hat{\mathcal{G}}$ among the edges of $\mathrm{DAG} \hat{\mathcal{G}}^{(1)}$.

# 3.3 Choice of the thresholds 

The choice of thresholds is often something non trivial, especially when using multiple testing. However, Step 1 of the procedure is conservative by construction. Indeed, the definition of score $S_{1}$ (equal to the maximum of $p-1 p$-values computed for testing 1st-order conditional independence) clearly supports the acceptation of the null assumption, i.e. the absence of an edge. Standard approaches for multiple testing correction do not apply to choose $\alpha_{1}$ threshold. Thus we introduce a heuristic approach to choose $\alpha_{1}$ threshold which is detailed in Supplementary Material [2], Section B. Overall, $\alpha_{1}$ threshold is chosen so that, after the Step 1, the number of genes having exactly one parent in DAG $\mathcal{G}^{(1)}$ predominates.

The choice of $\alpha_{2}$ threshold is less problematic. Indeed, the second Step of the inference procedure is a standard multivariate regression. Then the usual thresholds $1 \%, 5 \%$ or $10 \%$ can be chosen or even a lower threshold when a low number of edges is wanted. However, a large number of tests are computed (as many as edges in DAG $\mathcal{G}^{(1)}$ ). In such multiple testing situations, a set of the predictions are expected to be false and it is useful to control this. We control the expected proportion of false positives edges, i.e. the False Discovery Rate (FDR) with the approach introduced by Benjamini and Hochberg ${ }^{3}$ [4].

### 3.4 Complexity of the algorithm

The complexity of this algorithm is $O\left(p^{3}\right)$. However the scores $\left(S_{1}(i, j)\right)_{j \in P}$ of the incoming edges of each target gene $i$ can be computed separately by using parallel run. This option is available in the R package G1DBN by specifying the target gene $i$ in the function DBNScoreStep1 dedicated to the Step 1 computation.

All the computations were performed on Redhat WS 4 AMD opteron 270 (2GHz). The computation time mostly depends on the number of TF genes, i.e. the genes allowed to be parents in the DAG to be inferred. For an illustration based on DBN inference performed from a real data set by Spellman [34] containing 786 target genes in Section 4.3, the computation of Step 1 required 7 minutes when the set of possible TF genes was restricted to 18 genes (resp. 4 minutes with the lasso [39] and 7 seconds with the shrinkage procedure [27], which are two alternative approaches for DBN inference introduced in Section 4.1). When all the 786 genes can be TFs,

[^0]
[^0]:    ${ }^{3}$ Let $m$ be the number of remaining edges after Step 1, then Step 2 requires to compute $m$ tests. Choose a maximal FDR level $q$ and order the set of $m$ observed $p$-values: $\quad p_{(1)} \leq \cdots \leq p_{(i)} \leq \cdots \leq p_{(m)}$. Then reject the null assumption ( $\mathrm{H}_{0}^{(i)}$ : "Edge $i$ is not DAG $\tilde{\mathcal{G}}$ ") for all $i \leq k$ where $k$ is defined as follows: $k=\max \left\{i: p_{(i)} \leq \frac{i}{m} q\right\}$. If no such $i$ exists, reject no hypothesis. Benjamini and Hochberg (1995) showed that this procedure ensures the FDR is lower than $q \frac{m_{0}}{m} \leq q$ where $m_{0}$ is the number of true null hypotheses.

the computation was parallel run and required 19 minutes by target gene with G1DBN (resp. 8 minutes by target gene with the lasso and 5 minutes for the whole set of 786 target genes with the shrinkage procedure). Step 2 of $G 1 D B N$ is very quick and requires less than 5 seconds for the 786TF study. Despite the need for more time, inference with G1DBN for a data set containing 800 genes is fully computable, especially when parallel running.

# 4 Validation 

### 4.1 Comparison with two reference methods

We compare the G1DBN inference procedure with two reference methods for model selection for multivariate AR(1) process: the shrinkage approach by Opgen-Rhein and Strimmer [27] and the lasso (Least Absolute Shrinkage and Selection Operator) introduced by Tibshirani [39]. Opgen-Rhein and Strimmer recently proposed a model selection procedure based on an analytic approach using James-Stein-Type shrinkage. The procedure consists of first computing the partial correlation coefficients, $r\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right)$, from the shrinkage estimates of the partial regression coefficients, and second, selecting the edges with a local false discovery rate approach [10]. Shrinkage inference is performed using the R code for shrinkage estimation ${ }^{4}$ by Opgen-Rhein and Strimmer.

The lasso (also called L1 shrinkage) combines shrinkage and model selection. The lasso estimates are obtained by minimizing the residual sum of squares subject to the sum of the absolute values of the coefficients being less than a constant. This approach offers the advantage that it automatically sets many regression coefficients to zero. We performed the lasso with the R package LARS developped by Efron et al. [11].

### 4.2 Simulation study

As the discovery of genetic regulatory interaction is a field in progress, validation of predictions made on real gene expression data is only partial, which may render the estimation of true and false positive detection rate not fully reliable [15]. Thus we first investigate the accuracy of G1DBN, the shrinkage and the lasso inference procedures on simulated data.

Data generation We generated 100 random time series according to a multivariate $\operatorname{AR}(1)$ model defined by parameters $\left(A_{[p \times p]}, B, \Sigma\right)$ for $p=50$

[^0]
[^0]:    ${ }^{4}$ available at http://strimmerlab.org/software.html.

genes. Since gene regulation networks are sparse, each matrix $A$ contains $5 \%$ of non zero coefficients. While keeping the number of parents low, this does not prevent a vertex from having more than one parent. Non zero regression coefficients $a_{i j}$, mean coefficients $b_{i}$ and error variances $\sigma_{i}$ were drawn from uniform distributions $\left(a_{i j}, b_{i} \sim \mathcal{U}([-0.95 ;-0.05] \cup\right.$ $[0.05 ; 0.95]), \sigma_{i} \sim \mathcal{U}[0.03,0.08])$. Time series were generated under the corresponding multivariate $\operatorname{AR}(1)$ models for $n=20$ to 50 .

Evaluation based on PR curves We evaluated the performance of DBN inference procedures using the Precision-Recall (PR) curve as plotted in Figure 5. PR curves show the precision, equal to the Positive Predictive Value (PPV) on the ordinate against the recall, equal to the power, on the abscissa. PR curves are drawn by first ordering the edges by decreasing significance, and then by computing the PPV and power for the first selected edge and for each newly included edge successively. We recall the next definitions,

$$
\begin{aligned}
\text { Positive Predictive Value (PPV) } & =\text { True Discovery Rate (TDR) } \\
& =1 \text { - False Discovery Rate (FDR) } \\
& =\frac{T P}{T P+F P} \\
\text { Recall }=\text { Sensitivity }=\text { Power } & =\frac{T P}{T P+F N}
\end{aligned}
$$

where TP refers to the number of true positive edges, i.e. the number of edges
which are selected by the inference procedure and actually belongs to the true DAG (used for simulating the data); FP refers to the number of false positive edges, i.e. the edges which are selected by the procedure but are not in the true DAG and FN refers to the number of false negative edges, i.e. the number of edges which are not selected by the procedure but are in the true DAG.

![img-3.jpeg](img-3.jpeg)

Figure 5: Precision-Recall (PR) cuppose obtained for network inference from simulated data (n = 20). (A) Comparison of the inference procedures: G1DBN (LS or Tukey), shrinkage and lasso. Step 2 of the G1DBN approach drastically improves the results (threshold α₁ = 0.7). (B) Impact of noisy data, simulated using a non-diagonal matrix Σ with either Gaussian or uniform noise, on the G1DBN procedure (Step 2) computed with LS estimates.

Simulation results We show on Figure 5 the results obtained with $n=20$, a length one can expect from existing gene expression time series. Figure 5A displays the average Precision Recall (PR) curves obtained with the various inference approaches when the error covariance matrix $\Sigma$ is diagonal and the noise distribution is Gaussian. The Step 1 of the G1DBN procedure computed either with the LS estimator or with the Tukey estimator (dashed lines) gives a very high PPV for the very first selected edges. The Step 2 of the G1DBN procedure (solid line) drastically improves the results. It allows to maintain the PPV greater than $95 \%$ while the power goes up to $50 \%$. PR curves computed with the Huber estimates (not shown) led to comparable results. The lasso (dotted line) is clearly outperformed by the other approaches and the shrinkage approach (dashed-dotted line) gives results comparable to the Step 1 of the G1DBN procedure only. The results of the three methods are naturally improved for greater values of $n$ but their relative perfomances are preserved (curves not shown).

We investigated the impact of the violation of the model assumptions. First we performed DBN inference on simulated data where the error covariance matrix $\Sigma$ is not diagonal ( $3 \%$ of the coefficients outside the diagonal differ from 0 ) and the noise distribution is either Gaussian or uniform $(\mathcal{U}[-2 ; 2])$. As shown on Figure 5B, the accuracy of the G1DBN procedure (Step 2) is not strongly affected when these assumptions on the noise distribution are not satisfied. However, it is difficult to get rid of the $1^{\text {st }}$ order Markov Assumption which was chosen in order to reduce the model dimension. When simulating an $\operatorname{AR}(2)$ model, the 2-order time dependencies existing in the model are missed. However, the 1-order time dependencies existing in the model are still recovered. Then, when considering a $2^{\text {nd }}$ order Markov process, an approximation can still be performed by successively inferring 1- and 2-order time dependencies. Note that the procedure also performs well when the number of parents in the true DAG $\hat{\mathcal{G}}$ is greater than one (See Supp. Material [2], Section A).

# 4.3 Analysis of microarray time course data sets 

Spellman's Yeast cell cycle data set We performed dynamic network inference from the Saccharomyces cerevisiae cell cycle data collected by Spellman et al. [34]. We used the $\alpha$ Factor-based synchronization data (18 time points) and we focus here on a set of 786 genes which demonstrated consistent periodic changes in transcription level (See Supplementary Material [2], Section D. 1 for more details).

A
![img-4.jpeg](img-4.jpeg)

B
![img-5.jpeg](img-5.jpeg)

Figure 6: Some results of the 18 TF-survey of $S$. cerevisiae cell cycle. (A) DAG containing the 18 first selected edges with G1DBN with LS estimates ( $\mathrm{PPV}=60 \%$ ). Colored nodes represent the TFs and the dark blue edges are validated by the Yeastract database. (B) Percentage of validated edges out of the first 5 to 1000 edges inferred with the G1DBN procedure, after Step 2 or after Step 1 only, the shrinkage or the lasso procedure. The dashed line shows the proportion of validated edges out of the $786 \times 18$ possible edges.

We carried out two surveys on this dataset. First, we allow only a subset of 18 genes $^{5}$ identified as putative TFs to be possible parent genes (i.e. to have edges pointing out towards other genes in DAG $\hat{\mathcal{G}}$ ) and look for their target genes. Then we extend the search for parent genes to the whole dataset of 786 genes in a second survey. We set $\alpha_{1}$ threshold for the G1DBN procedure according to guidelines detailed in Supplementary Material [2], Section B ( $\alpha_{1}=0.1$ for the 18 TF-survey, $\alpha_{1}=0.05$ for the 786 TF-survey).

It is somehow difficult to assert the validity of the results obtained from real data as the whole regulatory machinery is not known yet. However the yeast cell cycle has been studied a lot and many regulation relationships have been recovered. We study the consistency of the first inferred edges with annotations in the Yeastract database [38], a curated repository currently listing found regulatory associations between TFs and target genes in S. cerevisiae.

In the 18 TF-survey, the first few selected edges are biologically validated. In the DAG comprising the 18 first selected edges (Figure 6A), 11 edges refer to identified regulatory relationships (thick blue edges). The first detected TFs are the genes coding for proteins FKH2, NDD1, RAP1 and SWI4. In particular, the proteins FKH2 (known as a TF with a major role in the expression of G2/M phase genes) and SWI4 (TF regulating late G1-specific transcription of targets) are pointed out as being essential TFs; they have the most target genes and the high majority ( $73 \%$ ) of these regulatory relationships is listed in Yeastract.

As introduced in Section 3.3, we chose $\alpha_{2}$ threshold in order to keep the False Discovery Rate (FDR) smaller than $1 \%$ with the approach by Benjamini and Hochberg [4]. This lead to $\alpha_{2}=0.0059$. The corresponding inferred DAG is shown in Figure 7. The two proteins FKH2 and SWI4 are still part of the TFs having the most targets, together with NDD1, which is an essential component of the activation of the expression of a set of late-S-phase-specific genes and TEC1, a transcription factor required for full Ty1 expression and Ty1-mediated gene activation (Ty transposableelement own for causing cell-type-dependent activation of adjacent-gene expression). The set of selected TFs is listed in Supplementary Material [2], Section D.2, Table 1, where the third column indicates the number of validated edges out of the selected ones. Except for NDD1, for which no target gene is listed in yeastract, one forth of the targets genes of the top four TFs are validated.

[^0]
[^0]:    ${ }^{5}$ The 18 genes code for proteins ACE2, FKH1, FKH2, GAT3, MBP1, MCM1, MIG2, NDD1, PHD1, RAP1, RME1, STB1, SUT1, SWI4, SWI5, SWI6, TEC1 and YOX1. consist of the overlap between the 786 genes under study and the 50 genes identified as putative TFs in a recent study by Tsai et al. [42].

![img-6.jpeg](img-6.jpeg)

Figure 7: DAG inferred by G1DBN with LS estimates, using $\alpha_{1}=0.1$, $\alpha_{2}=0.0059$ (ensuring FDR $<0.01$ ), in the 18 TF -survey of the $S$. cerevisiae cell cycle. The 17 colored nodes represent the 16 TFs selected as parent node out of the 18 TFs under study, plus node FKH1 which is selected as a target of NDD1. The dark blue edges are validated by Yeastract. This network contains 286 genes and 308 edges. See the complete edges list in Supp. Material [2].

For a comparative overview, the histogram of Figure 6B displays the percentage of validated edges out of the first 5 to 1000 selected edges inferred with each inference procedure When considering the 1000 first inferred edges, the results are very similar to what could be expected by chance only. Note that, as the Step 2 of G1DBN choose 308 edges only, it is not considered when comparing the 1000 first edges.

In the second survey including all the 786 genes as putative TFs, the dimension is far higher and the results are consequently more restricted. Indeed, the proportion of validated edges doesn't exceed $12.5 \%$, obtained with the 2 nd step of G1DBN procedure among the first selected edges. However, this is still a subtantial result as compared with the proportion of validated edges (equal to $0.26 \%$ ). In order to keep the FDR smaller than 0.01 , we chose $\alpha_{2}=0.0067$ by following the Benjamini and Hochberg approach [4]. The inferred DAG for the 786 TF-survey contains 437 genes and 380 edges. The display of this DAG, as well as the list of its edges and the list of the genes selected as TFs, is available in Supplementary Material $[2]$.

Diurnal cycle on the starch metabolism of A. Thaliana We applied the G1DBN inference procedure to the expression time series data generated by Smith et al. [33] to investigate the impact of the diurnal cycle on the starch metabolism of Arabidopsis Thaliana. We restricted our study to the 800 genes selected by Opgen-Rhein and Strimmer [27] as having periodic expression profiles ${ }^{6}$.

Using the heuristic approach detailed in Supplementary Material [2], Section B, we choose threshold $\alpha_{1}=0.02$ allowing the distribution of the number of parents in the DAG $\mathcal{G}^{(1)}$ having the number of 0 -parent genes to dominate and the number of 1 -parent genes to be half as large. We set $\alpha_{2}=0.005$ in order to maintain the False Discovery Rate smaller than 0.01 by using the approach by Benjamini and Hochberg [4] (See Section 3.3 for details). We recover the DAG in Figure 8 which has a "hub" connectivity structure. This network contains 206 edges implicating 277 different genes. We may notice that this DAG differs from the one inferred by Opgen-Rhein and Strimmer [27]. However the edges selected by the three inference procedures discussed in this section differ somewhat (See the proportion of edges in common by using the various inference approaches in Supplementary Material [2], Section C) and may, in fact, yield complementary information or insights.

[^0]
[^0]:    ${ }^{6}$ The data are available in the GeneNet R package at http://strimmerlab.org/ software/genenet/html/ar th800.html or in our R package G1DBN (arth800line).

![img-7.jpeg](img-7.jpeg)

Figure 8: DAG inferred with G1DBN from the data by Smith et al. [33] in order to investigate starch metabolism of A. thaliana (LS estimates, $\alpha_{1}=0.1$, $\alpha_{2}=0.005$ such that FDR $<0.01$ ). The dark colored nodes are the 3 nodes with the most targets, 2 out of them are known for being implicated in starch metabolism. The light colored nodes are parent nodes already identified as TF or DNA binding protein (See Supp. Material[2], Section E, Table 2). This network contains 277 genes and 206 edges. See the edges list in Supp. Material.

Among the 'parent' nodes in the inferred DAG displayed in Figure 8, two nodes (799 and 628) out of the three having the most target refers to proteins that are known to be implicated in starch metabolism. Indeed, node 799, which has 14 'target' nodes, refers to DPE2 (DISPROPORTIONATING ENZYME 2), which is an essential component of the pathway from starch to sucrose and cellular metabolism in plant leaves at night. Node 628 ( 6 targets) is a transferase (At5g24300) implicated in the starch synthase. Node 702, which is an unknown protein (At5g58220), has also 6 targets. These three nodes are dark-colored in the DAG of Figure 8. Note that there is no prior knowledge regarding the role of each gene (TF or target) in this survey. As a consequence, some edges might be inferred wrong way around ${ }^{7}$. Thus node 799 , which is a gene coding for an enzyme (DPE2), is most probably not a TF for its 14 apparent target genes. However node 799 is still the gene whose expression level best explains the expression of the 14 genes. Consequently these genes might be implicated in the same pathway as DPE2. The remaining parent nodes have from 1 to 4 targets. Among them, 9 genes, which are listed in Supplementary Material [2], Section E, Table 2, have already been identified as TFs or as DNA binding proteins. These 9 nodes are light-colored in the displayed DAG. Finally a list of 37 unknown proteins have been selected as parents in the inferred DAG. Potentially implicated in the regulation machinery of starch metabolism, these proteins represent a subset of genes which is relevant for further analyses. See more details on the inferred network displayed in Figure 8 in the Supplementary Material [2].

# 5 Discussion and conclusion 

As more and more gene expression time series has become available, the need for efficient tools to analyze such data has become imperative. In this paper, we first determine sufficient conditions for Dynamic Bayesian Network modelling of gene expression time series. This type of modelling offers a straightforward interpretation: the edges of the DAG $\hat{\mathcal{G}}$ defining the DBN exactly describe the set of conditional dependencies between successive gene expression levels. Having defined and characterized low order conditional dependence DAGs for DBNs, we point out relevant characteristics for the approximation of sparse DAGs. In particular, under faithfulness assumption, DAG $\hat{\mathcal{G}}$ is included in the $1^{\text {st }}$ order conditional dependence DAG $\mathcal{G}^{(1)}$.

From these results, we develop G1DBN, a novel procedure for DBN

[^0]
[^0]:    ${ }^{7}$ In particular if some assumption of the model is not satisfied. For instance if an essential TF is missing or if the regulation is not transcriptional, i.e. does not depend on the amount of mRNA coding for the protein.

inference, which makes it possible to tackle the 'small $n$, large $p$ ' estimation case that occurs with genetic time series data. Based on the consideration of low order conditional dependencies, the G1DBN procedure proved to be powerful on both simulated and real data analysis. With respect to other methods, the shrinkage approach considerably improves the precision of the overall estimation of the partial correlation coefficients when the number of observations $n$ is small compared to the number of genes $p$. However, considering $1^{\text {st }}$ order conditional independence proved to be more efficient for DBN inference in terms of power and PPV on simulated data, and gave promising results on real data analysis. As for the lasso, one might notice that a drawback lies in the fact that the edge selection is done vertex by vertex whereas the DAG $\hat{\mathcal{G}}$ is globally sparse but not uniformally. As a consequence, the lasso tends to uniformally reduce the number of parents of each vertex instead of only keeping the total number of edges contained.

The power of the G1DBN procedure comes from the accuracy improvement of the testing made possible by the dimension reduction. Indeed, as the first step selection is based on the $1^{\text {st }}$ order conditional independence consideration, significance tests are performed in a model of dimension 4 (See Section 3.1). This represents a drastic dimension reduction compared to full order independence testing and makes the testing much more accurate. Thus, even if there are more edges in the DAG $\mathcal{G}^{(1)}$ than in the true DAG $\hat{\mathcal{G}}$ (Proposition 6), Step 1 of the procedure is already very predictive.

Throughout the analyses performed for this paper, we point out two major directions for further research. On the one hand, we noticed that the edges selected by the three inference procedures differ somewhat (See Supplementary Material [2], Section C). A further relevant study would consist of analyzing in which way these DBN inference procedures could have different strenghts and may be complementary. On the other hand, the use of robust estimators like Huber or Tukey bisquare did not allow a noticeable change of the inference approach on real data. Another interesting survey lies in the investigation of which measures of dependence, like non linear or other robust estimates, are the more pertinent to analyze gene expression data.

# APPENDIX 

## A Proofs

## A. 1 Lemmas 1 to 3 and proofs

Lemma 1 Under Assumptions 1 and 2, the probability distribution $\mathbb{P}$ admits a DBN representation according to a DAG whose edges only join nodes representing variables observed at two successive time points, at least according to $D A G \mathcal{G}_{\text {full }}=\left(X,\left\{\left(X_{t-1}^{j}, X_{t}^{i}\right)\right\}_{i, j \in P, t>1}\right)$ which has edges between any pair of successive variables.

Proof of Lemma 1. From assumption 1, the density $f$ of the joint probability distribution of process $X$ be written as the product of conditional densities,

$$
f(X)=f\left(X_{1}\right) \prod_{t=2}^{n} f\left(X_{t} \mid X_{t-1}\right)
$$

where $f\left(X_{t} \mid X_{t-1}\right)$ refers to the density of the conditional probability distribution of $X_{t}$ given $X_{t-1}$.

From Assumption 2, for all $t>1$, the conditional density $f\left(X_{t} \mid X_{t-1}\right)$ can be written as the product of the conditional density of each variable $X_{t}^{i}$ given the set of variables $X_{t-1}$ observed at the previous time,

$$
f\left(X_{t} \mid X_{t-1}\right)=\prod_{i \in P} f\left(X_{t}^{i} \mid X_{t-1}\right)
$$

From equations (10) and (11), the density $f$ writes as the product of the conditional density of each variable $X_{t}^{i}$ given its parents in $\mathcal{G}_{\text {full }}$. From Proposition 1, the probability distribution $\mathbb{P}$ admits a BN representation according to $\mathcal{G}_{\text {full }}$.

Lemma 2 Assume the joint probability distribution $\mathbb{P}$ of process $X$ has density $f$ with respect to Lebesgue measure on $\mathbb{R}^{p \times n}$. If $\mathbb{P}$ factorizes according to two different subgraphs of $\mathcal{G}_{\text {full }}, \mathcal{G}_{1}$ and $\mathcal{G}_{2}$, then $\mathbb{P}$ factorizes according to $\mathcal{G}_{1} \cap \mathcal{G}_{2}$.

From Lemma 2, it is straightforward that, among the DAGs included in $\mathcal{G}_{\text {full }}$, there exists a minimal $D A G$ (denoted by $\overline{\mathcal{G}}$ in the paper) according to which the probability distribution $\mathbb{P}$ factorizes, thus establishing a $B N$ representation of process $X$.

Proof of Lemma 2. Consider a discrete-time stochastic process $X=$ $\left\{X_{t}^{i} ; i \in P, t \in N\right\}$ whose joint probability $\mathbb{P}$ distribution has the density $f$ with respect to Lebesgue measure on $\mathbb{R}^{p \times n}$.

Let $\mathcal{G}_{1}$ and $\mathcal{G}_{2}$ be two different subgraphs of $\mathcal{G}_{\text {full }}$ according to which the joint probability distribution $\mathbb{P}$ factorizes. Let $i \in P, t \in N$, we consider the random variable $X_{t}^{i}$.

We denote as follows,

- the following subsets of $P$,

$$
\begin{aligned}
& p a_{1}=\left\{j \in P ; X_{t-1}^{j} \in p a\left(X_{t}^{i}, \mathcal{G}_{1}\right)\right\} \\
& \overline{p a}_{1}=P \backslash\left\{p a_{1}\right\} \\
& p a_{2}=\left\{j \in P ; X_{t-1}^{j} \in p a\left(X_{t}^{i}, \mathcal{G}_{2}\right)\right\} \\
& \overline{p a}_{2}=P \backslash\left\{p a_{2}\right\}
\end{aligned}
$$

- and the densities of the joint or marginal probability distributions of $\left(X_{t}^{i}, X_{t-1}\right)$,
$g: \mathbb{R}^{p+1} \rightarrow \mathbb{R}$ the density of the joint probability distribution of $\left(X_{t}^{i}, X_{t-1}\right)$
$g^{i}$ the density of the probability distribution of $X_{t}^{i}$,
$g^{P}$ the density of the joint probability distribution of $\left(X_{t-1}\right)$,
$g^{i, p a_{1}}$ the density of the joint probability distribution of $\left(X_{t}^{i}, X_{t-1}^{p a_{1}}\right)$ where,

$$
X_{t-1}^{p a_{1}}=p a\left(X_{t}^{i}, \mathcal{G}_{1}\right)
$$

$g^{i, \overline{p a}_{2}}$ the density of the joint probability distribution of $\left(X_{t}^{i}, X_{t-1}^{\overline{p a}_{2}}\right)$ where

$$
X_{t-1}^{\overline{p a}_{2}}=X_{t-1} \backslash\left\{p a\left(X_{t}^{i}, \mathcal{G}_{2}\right)\right\}
$$

etc...
In the following, $y \in \mathbb{R}, x=\left(x_{1}, \ldots, x_{p}\right) \in \mathbb{R}^{p}$ and we denote by $x_{p a_{1}}=$ $\left\{x_{j} ; j \in p a_{1}\right\} \in \mathbb{R}^{\left|p a_{1}\right|}$ (Thus $x=\left(x_{p a_{1}}, x_{\overline{p a}_{1}}\right)=\left(x_{p a_{2}}, x_{\overline{p a}_{2}}\right) \in \mathbb{R}^{p}$ ). As the probability distribution $\mathbb{P}$ factorizes according to $\mathcal{G}_{1}$, we derive from the DAG theory the conditional independence,

$$
X_{t}^{i} \pm X_{t-1}^{\overline{p a}_{1}} \mid X_{t-1}^{p a_{1}}
$$

that is,

$$
\forall y \in \mathbb{R}, \forall x \in \mathbb{R}^{p}, \quad \frac{g(y, x)}{g^{P}(x)}=\frac{g^{i, p a_{1}}\left(y, x_{p a_{1}}\right)}{g^{p a_{1}}\left(x_{p a_{1}}\right)}
$$

Equivalent results derived from the factorization according to $\mathcal{G}_{2}$ gives,

$$
\forall y \in \mathbb{R}, x \in \mathbb{R}^{p}, N g^{i, p a_{2}}\left(y, x_{p a_{2}}\right)=\frac{g^{i, p a_{1}}\left(y, x_{p a_{1}}\right)}{g^{p a_{1}}\left(x_{p a_{1}}\right)} g^{p a_{2}}\left(x_{p a_{2}}\right)
$$

By taking the integral with respect to $x_{p a_{2} \cap \overline{p a}_{1}}$, we write for all $y \in \mathbb{R}$, for all $x_{p a_{1} \cup p a_{2}} \in \mathbb{R}^{\left|p a_{1} \cup p a_{2}\right|}$,

$$
\begin{aligned}
\int g^{i, p a_{2}}\left(y, x_{p a_{2}}\right) d\left(x_{p a_{2} \cap \overline{p a}_{1}}\right) & =\int \frac{g^{i, p a_{1}}\left(y, x_{p a_{1}}\right)}{g^{p a_{1}}\left(x_{p a_{1}}\right)} g^{p a_{2}}\left(x_{p a_{2}}\right) d\left(x_{p a_{2} \cap \overline{p a}_{1}}\right) \\
g^{i, p a_{1} \cap p a_{2}}\left(y, x_{p a_{1} \cap p a_{2}}\right) & =\frac{g^{i, p a_{1}}\left(y, x_{p a_{1}}\right)}{g^{p a_{1}}\left(x_{p a_{1}}\right)} g^{p a_{1} \cap p a_{2}}\left(x_{p a_{1} \cap p a_{2}}\right)
\end{aligned}
$$

Finally we have,

$$
\forall y \in \mathbb{R}, \forall x \in \mathbb{R}^{p}, \quad \frac{g(y, x)}{g^{P}(x)}=\frac{g^{i, p a_{1} \cap p a_{2}}\left(y, x_{p a_{1} \cap p a_{2}}\right)}{g^{p a_{1} \cap p a_{2}}\left(x_{p a_{1} \cap p a_{2}}\right)}
$$

that is the conditional density of the probability distribution of $X_{t}^{i}$ given $X_{t-1}$ is the conditional density of the probability distribution of $X_{t}^{i}$ given $X_{t-1}^{p a_{1} \cap p a_{2}}$. Then $\mathbb{P}$ factorizes according to $\mathcal{G}_{1} \cap \mathcal{G}_{2}$.

Lemma 3 (Conditional independence between non adjacent successive variables) Let $\mathcal{G}$ be a subgraph of $\mathcal{G}_{\text {full }}$ according to which the probability distribution $\mathbb{P}$ admits a $B N$ representation. For any pair of successive variables $\left(X_{t-1}^{j}, X_{t}^{i}\right)$ which are non adjacent in $\mathcal{G}$, we have

$$
X_{t}^{i} \mathbb{1} X_{t-1}^{j} \mid p a\left(X_{t}^{i}, \mathcal{G}\right) \text { and } X_{t}^{i} \mathbb{1} X_{t-1}^{j} \mid p a\left(X_{t}^{i}, \mathcal{G}\right) \cup S
$$

for all $S$ subset of $\left\{X_{u}^{k} ; k \in P, u<t\right\}$.
As an illustration of Lemma 3, assume $\mathbb{P}$ admits a BN representation according to the DAG of Figure 1C. There is no edge between $X_{t}^{3}$ and $X_{t+1}^{1}$ in this DAG. Now consider in Figure 2B the moral graph of the smallest ancestral graph containing $X_{t}^{3}, X_{t+1}^{1}$ and the parents $\left(X_{t}^{1}, X_{t}^{2}\right)$ of $X_{t+1}^{1}$. The set $\left(X_{t}^{1}, X_{t}^{2}\right)$ blocks all paths between $X_{t}^{3}$ and $X_{t+1}^{1}$. From Proposition 2 , we have $X_{t+1}^{1} \mathbb{1} X_{t}^{3} \mid p a\left(X_{t+1}^{1}, \mathcal{G}\right)$.

Proof of Lemma 3. Assume $\mathbb{P}$ admits a BN representation according to $\mathcal{G}$, a subgraph of $\mathcal{G}_{\text {full }}$. Let $X_{t-1}^{j}$ and $X_{t}^{i}$ be two non adjacent vertices of $\mathcal{G}$ (there is no edge between them in $\mathcal{G}$ ) and consider the moral graph $\left(\mathcal{G}_{A n\left(X_{t}^{i} \cup X_{t-1}^{j} \cup p a\left(X_{t}^{i}, \mathcal{G}\right)\right)}\right)^{m}$ of the smallest ancestral set containing the variables $X_{t}^{i}, X_{t-1}^{j}$ and the parents $p a\left(X_{t}^{i}, \mathcal{G}\right)$ of $X_{t}^{i}$ in $\mathcal{G}$. As DAG $\mathcal{G}$ is a subgraph of $\mathcal{G}_{\text {full }}$, the set of parents $p a\left(X_{t}^{i}, \mathcal{G}\right)$ blocks all paths between $X_{t-1}^{j}$ and $X_{t}^{i}$ in the moral graph $\left(\mathcal{G}_{A n\left(X_{t}^{i} \cup X_{t-1}^{j} \cup p a\left(X_{t}^{i}, \mathcal{G}\right)\right)}\right)^{m}$. From Proposition 2, this establishes the conditional independence $X_{t}^{i} \mathbb{1} X_{t-1}^{j} \mid p a\left(X_{t}^{i}, \mathcal{G}\right)$.

This result holds for the conditioning according to any subset $S \subseteq$ $\left\{X_{u}^{k} ; k \in P, u<t\right\}$.

# A. 2 Proof of Propositions 3, 5, 6 and 7 

Proof of Proposition 3. First, we show that $\mathbb{P}$ admits a BN representation according to $\tilde{\mathcal{G}}$. Let $i, j \in P$ such that $X_{t}^{i} \mathbb{\Perp} X_{t-1}^{j} \mid X_{t-1}^{P_{j}}$, then we have,

$$
f\left(X_{t}^{i} \mid X_{t-1}\right)=f\left(X_{t}^{i} \mid X_{t-1}^{P_{j}}\right)
$$

Under Assumptions 1 and 2, from Lemma 1 (See Appendix A.1) and Prop. $1, \mathbb{P}$ admits a BN representation according to the $\operatorname{DAG}\left(X, E\left(\mathcal{G}_{\text {full }}\right) \backslash\left(X_{t-1}^{j}, X_{t}^{i}\right)\right)$ which has the edges of $\mathcal{G}_{\text {full }}$ except for the edge $\left(X_{t-1}^{j}, X_{t}^{i}\right)$. This holds for any pair of successive variables that are conditionally independent.

From Lemma 2 (See Appendix A.1), $\mathbb{P}$ admits a BN representation according to the intersection of the $\operatorname{DAG}\left(X, E\left(\mathcal{G}_{\text {full }}\right) \backslash\left(X_{t-1}^{j}, X_{t}^{i}\right)\right)$ for any pair $\left(X_{t}^{i}, X_{t-1}^{j}\right)$ such that $X_{t}^{i} \mathbb{\Perp} X_{t-1}^{j} \mid X_{t-1}^{P_{j}}$, that is DAG $\tilde{\mathcal{G}}$.

Also, DAG $\tilde{\mathcal{G}}$ cannot be reduced. Indeed, let $\left(X_{t-1}^{l}, X_{t}^{k}\right)$ be an edge of $\tilde{\mathcal{G}}$
and assume that $\mathbb{P}$ admits a BN representation according to $\tilde{\mathcal{G}} \backslash\left(X_{t-1}^{l}, X_{t}^{k}\right)$, that is DAG $\tilde{\mathcal{G}}$ with the edge $\left(X_{t-1}^{l}, X_{t}^{k}\right)$ removed. From Lemma 3 (Appendix A.1), we have $X_{t}^{k} \mathbb{\Perp} X_{t-1}^{l} \mid X_{t-1}^{P_{l}}$, which contradicts $\left(X_{t-1}^{l}, X_{t}^{k}\right) \in$ $V(\tilde{\mathcal{G}})\left(\right.$ i.e. $\left.X_{t}^{k} \mathbb{\Perp} X_{t-1}^{l} \mid X_{t-1}^{P_{1}}\right)$.

## Proof of Proposition 5.

First, from Corollary $1, \tilde{\mathcal{G}} \supseteq \mathcal{G}^{(1)}$.
Second, let $X$ be a Gaussian process and $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E(\tilde{\mathcal{G}})$, then according to Proposition 3, $X_{t}^{i} \mathbb{\Perp} X_{t-1}^{j} \mid X_{t-1}^{P_{j}}$. Since $X$ is Gaussian, this implies
$\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right) \neq 0$.
Now assume that there exists $k \neq j$, such that $X_{t}^{i} \mathbb{\Perp} X_{t-1}^{j} \mid X_{t-1}^{k}$ ie $\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E\left(\mathcal{G}^{(1)}\right)$. We are going to prove that this contradicts the nullity of covariance $\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right) \neq 0$.

Let $l$ be an element of $P \backslash\{j, k\}$. The conditional covariance $\operatorname{Cov}(i j \mid k, l)=$ $\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{k}, X_{t-1}^{l}\right)$ can be written,

$$
\begin{aligned}
& \operatorname{Cov}(i j \mid k, l)=\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{k}\right)-\frac{\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{l} \mid X_{t-1}^{k}\right) \operatorname{Cov}\left(X_{t-1}^{j}, X_{t-1}^{l} \mid X_{t-1}^{k}\right)}{\operatorname{Var}\left(X_{t-1}^{l} \mid X_{t-1}^{k}\right)} \\
& =\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{k}\right) \times\left[1-\frac{\left(\operatorname{Cov}\left(X_{t-1}^{j}, X_{t-1}^{l} \mid X_{t-1}^{k}\right)\right)^{2}}{\operatorname{Var}\left(X_{t-1}^{j} \mid X_{t-1}^{k}\right) \operatorname{Var}\left(X_{t-1}^{l} \mid X_{t-1}^{k}\right)}\right] \\
& -\frac{\operatorname{Cov}\left(X_{t-1}^{j}, X_{t-1}^{l} \mid X_{t-1}^{k}\right) \operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{l} \mid X_{t-1}^{k}, X_{t-1}^{j}\right)}{\operatorname{Var}\left(X_{t-1}^{l} \mid X_{t-1}^{k}\right)}
\end{aligned}
$$

However both terms in the latter expression of $\operatorname{Cov}(i j \mid k, l)$ are null:

- since $X_{t}^{i} \mathbb{L} X_{t-1}^{j} \mid X_{t-1}^{k}$, then $\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{k}\right)=0$,
- as $N_{p a}^{\operatorname{Max}}(\tilde{\mathcal{G}}) \leq 1, X_{t-1}^{j}$ is the only parent of $X_{t}^{i}$ in $\tilde{\mathcal{G}}$. So the variable $X_{t-1}^{j}$ and thus also the set $\left(X_{t-1}^{j}, X_{t-1}^{k}\right)$ blocks all paths between $X_{t-1}^{l}$ and $X_{t}^{i}$ in the moral graph of the smallest ancestral set containing $X_{t}^{i} \cup X_{t-1}^{j, k, l}$. Then we have, $X_{t}^{i} \mathbb{L} X_{t-1}^{l} \mid\left\{X_{t-1}^{j}, X_{t-1}^{k}\right\}$, that is $\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{i} \mid X_{t-1}^{k}, X_{t-1}^{j}\right)=0$.

Then $\operatorname{Cov}(i j \mid k, l)=0$. By induction, we obtain $\operatorname{Cov}\left(X_{t}^{i}, X_{t-1}^{j} \mid X_{t-1}^{P_{j}}\right)=$ 0 leading to a contradiction with $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E(\tilde{\mathcal{G}})$. Therefore $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in$ $\mathcal{G}^{(1)}$ and we have $\tilde{\mathcal{G}} \subseteq \mathcal{G}^{(1)}$.

# Proof of Prop 6 . 

Let $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E(\tilde{\mathcal{G}})$. Assume that $\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E\left(\mathcal{G}^{(q)}\right)$ then there exists a subset of $q$ variables $X_{t-1}^{Q}$ with respect to which $X_{t-1}^{j}$ and $X_{t}^{i}$ are conditionally independent. From faithfulness, the subset $X_{t-1}^{Q}$ separates $X_{t-1}^{j}$ and $X_{t}^{i}$ in the moral graph of the smallest ancestral set containing $X_{t}^{i} \cup X_{t-1}^{j} \cup X_{t-1}^{Q}$. This contradicts the presence of the edge $\left(X_{t-1}^{j}, X_{t}^{i}\right)$ in $\tilde{\mathcal{G}}$

## Proof of Prop 7 .

From faithfulness, $\tilde{\mathcal{G}} \subseteq \mathcal{G}^{(q)}$. Then for all $i$ in $P$, for all $t>1$, we have $N_{p a}\left(X_{t}^{i}, \tilde{\mathcal{G}}\right) \leq N_{p a}\left(X_{t}^{i}, \mathcal{G}^{(q)}\right) \leq q$.

From Proposition 4, $\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E(\tilde{\mathcal{G}}) \Rightarrow\left(X_{t-1}^{j}, X_{t}^{i}\right) \notin E\left(\mathcal{G}^{(q)}\right)$, that is $\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E\left(\mathcal{G}^{(q)}\right) \Rightarrow\left(X_{t-1}^{j}, X_{t}^{i}\right) \in E(\tilde{\mathcal{G}})$
