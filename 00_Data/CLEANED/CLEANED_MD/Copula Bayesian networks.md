# Pair-copula Bayesian networks 

Alexander Bauer* ${ }^{* \dagger}$ Claudia Czado*


#### Abstract

Pair-copula Bayesian networks (PCBNs) are a novel class of multivariate statistical models, which combine the distributional flexibility of pair-copula constructions (PCCs) with the parsimony of conditional independence models associated with directed acyclic graphs (DAG). We are first to provide generic algorithms for random sampling and likelihood inference in arbitrary PCBNs as well as for selecting orderings of the parents of the vertices in the underlying graphs. Model selection of the DAG is facilitated using a version of the well-known PC algorithm which is based on a novel test for conditional independence of random variables tailored to the PCC framework. A simulation study shows the PC algorithm's high aptitude for structure estimation in non-Gaussian PCBNs. The proposed methods are finally applied to modelling financial return data.


Key words: Conditional independence test; copulas; directed acyclic graphs; graphical models; likelihood inference; PC algorithm; regular vines; structure estimation.

## 1. Introduction

Graphical models provide a powerful tool in multivariate statistical analysis aimed at modelling the conditional independence structure of a family of random variables. The conditional independence restrictions observed by a graphical model can be conveniently summarised in a graph whose vertices represent the variables and whose edges indicate interrelations between these variables, see Lauritzen (1996). We are particularly interested in the graphical models known as Bayesian networks, whose Markov properties can be represented by a directed acyclic graph (DAG). Areas of applications for these Bayesian networks range from artificial intelligence, decision support systems, and engineering to genetics, geology, medicine, and finance, see Pourret et al. (2008). Despite the broad scope of applicability, however, graphical

[^0]
[^0]:    *Department of Mathematics, Technische Universität München, Boltzmannstr. 3, 85748 Garching, Germany. E-mail: alexander.bauer@tum.de, cczado@ma.tum.de.
    ${ }^{\dagger}$ Corresponding author.

# 1. Introduction 

modelling of continuous random variables has mainly been limited to the multivariate normal distribution. Accordingly, available structure estimation algorithms for the DAG underlying a Bayesian network are mainly confined to discrete or Gaussian models. We address both the problems of constructing Bayesian networks with non-Gaussian continuous joint distributions, and of estimating the Markov structure underlying such a non-Gaussian Bayesian network.

Our solution to the first problem of deriving non-Gaussian distributions with pre-specified conditional independence properties is based on so-called pair-copula constructions (PCCs). By iterated application of Sklar's theorem on copulas (Sklar, 1959), Kurowicka and Cooke (2005) and Bauer et al. (2012) have shown that every continuous multivariate distribution associated with a DAG can be decomposed into a family of bivariate, potentially conditional distributions, which correspond to the edges of the underlying graph. An explicit representation of the respective probability density function (pdf) was, however, only derived in examples. We provide a novel algorithm for evaluating the pdf of an arbitrary Bayesian network PCC.

The flexibility of these pair-copula Bayesian networks (PCBNs) allows for the capturing of a wide range of distributional features to be modelled such as heavy-tailedness, tail dependence, and non-linear, asymmetric dependence. Further investigations on PCBNs include Hanea et al. $(2006,2010)$ and Hanea and Kurowicka (2008). While these authors concentrate on nonparametric statistical inference and elicited expert knowledge, we focus attention to parametric likelihood inference and data-driven structure estimation. We also provide routines for copula selection and enumeration of the parents of the vertices of the underlying DAG.

When expert knowledge on the underlying Markov structure is unavailable, data-driven structure estimation algorithms are frequently used. Two approaches are predominantly found in the literature: the constraint-based and the score-and-search-based approach (Koller and Friedman, 2009, Chapter 18). In the former, the DAG is inferred from a series of conditional independence tests, while in the latter, the DAG is found by optimising a given scoring function. We concentrate on the popular constraint-based PC algorithm by Spirtes and Glymour (1991), and demonstrate its aptitude for structure estimation in non-Gaussian PCBNs in an extensive simulation study. In particular, we introduce a novel test for conditional independence of continuous random variables which is based on the closely related regular-vine copula models (Bedford and Cooke, 2001, 2002), and which is of interest on its own merits. This novel test will prove to outperform a standard test for zero partial correlation used in the Gaussian setting.

With their focus on conditional independence, PCBNs are generally more parsimonious than regular-vine copula models. Another copula decomposition of a joint distribution associated with a DAG which uses generally higher-variate copulas-and therefore lacks the flexibility of the pair-copula approach-was investigated by Elidan (2010, 2012).

# 2. Bayesian networks 

The paper is organised as follows. In Section 2, we give a short review of Bayesian networks, followed by a review of vine copula models in Section 3. In Section 4, we provide an algorithm for evaluating the pdf of a PCC associated with a DAG as well as routines for simulation, model selection, and likelihood inference in PCBNs. We review the PC algorithm in Section 5 and introduce a novel test for conditional independence of continuous random variables. The PC algorithm's aptitude for structure estimation in non-Gaussian PCBNs is explored in a simulation study in Section 6. Section 7 presents an application of PCBNs to financial return data, and the paper concludes with a brief discussion in Section 8. The paper is designed to be self-contained and to unify the various non-standard notations on Bayesian networks found in the literature.

## 2. Bayesian networks

We begin by fixing some graph theoretical terminology. Let $V \neq \emptyset$ be a finite set and let $E \subseteq \mathcal{E}:=\{(v, w) \in V \times V \mid v \neq w\}$. Then $\mathcal{G}=(V, E)$ denotes a graph with vertex set $V$ and edge set $E$. We say that $\mathcal{G}$ contains the undirected edge $v-w$ if $(v, w) \in E$ and $(w, v) \in E$. Similarly, we say that $V$ contains the directed edge $v \rightarrow w$ if $(v, w) \in E$ but $(w, v) \notin E$. A graph containing only undirected edges is called an undirected graph (UG). If $E \equiv \mathcal{E}$, we call $\mathcal{G}$ the complete $U G$ on $V$. A graph containing only directed edges is called a directed graph. By replacing all directed edges of $\mathcal{G}$ with undirected edges, we obtain the skeleton $\mathcal{G}^{s}$ of $\mathcal{G}$. We write $v \multimap w$ whenever $(v, w) \in E$, that is $\mathcal{G}$ contains either the directed edge $v \rightarrow w$ or the undirected edge $v-w$. A sequence of distinct vertices $v_{1}, \ldots, v_{k} \in V, k \geq 2$, is called a path from $v_{1}$ to $v_{k}$ if $\mathcal{G}$ contains $v_{i} \multimap v_{i+1}$ for all $i \in\{1, \ldots, k-1\}$. A path from $v_{1}$ to $v_{k}$ is called directed if at least one of the connecting edges is directed. We call a path from $v_{1}$ to $v_{k}$ a cycle if $v_{1}=v_{k}$. In particular, we call a directed path from $v_{1}$ to $v_{k}$ a directed cycle if $v_{1}=v_{k}$. A graph without directed cycles is called a chain graph (CG). A CG containing only directed edges is known as a directed acyclic graph (DAG). We define the adjacency set of a vertex $v \in V$ as $\operatorname{ad}(v):=\{w \in V \mid(v, w) \in E$ or $(w, v) \in E\}$. If $w \notin \operatorname{ad}(v)$, we say that $v$ and $w$ are non-adjacent. A triple of vertices $(u, v, w)$ is called a $v$-structure if $\mathcal{G}$ contains $u \rightarrow v \leftarrow w$ and if $u$ and $w$ are non-adjacent.

Now let $\mathcal{G}$ be a DAG. The moral graph $\mathcal{G}^{m}$ of $\mathcal{G}$ is defined as the skeleton of the graph obtained from $\mathcal{G}$ by introducing an undirected edge $u-w$ whenever $\mathcal{G}$ contains a v-structure $(u, v, w)$ for $u, v, w \in V$. Since all edges of $\mathcal{G}$ are directed, we can speak of paths instead of directed paths. For $v \in V$, we call $\mathrm{pa}(v):=\{w \in V \mid \mathcal{G}$ contains $w \rightarrow v\}$ the parents of $v, \operatorname{an}(v):=\{w \in V \mid \mathcal{G}$ contains a path from $w$ to $v\}$ the ancestors of $v, \operatorname{de}(v):=\{w \in$ $V \mid \mathcal{G}$ contains a path from $v$ to $w\}$ the descendants of $v$, and $\operatorname{nd}(v):=V \backslash(\{v\} \cup \operatorname{de}(v))$ the nondescendants of $v$. A set $I \subseteq V$ is called ancestral if $\mathrm{pa}(v) \subseteq I$ for all $v \in I$. The smallest ancestral set containing $I$ is denoted by $\operatorname{An}(I)$. As is readily verified, $\operatorname{An}(I)=I \cup \bigcup_{v \in I} \operatorname{an}(v)$. The graph

# 2. Bayesian networks 

$\mathcal{G}_{I}=(I, E \cap(I \times I))$ is called the subgraph of $\mathcal{G}$ induced by $I$. A bijection $v_{\bullet}:\{1, \ldots,|V|\} \rightarrow V$, $i \mapsto v_{i}$, satisfying $i<j$ whenever $\mathcal{G}$ contains $v_{i} \rightarrow v_{j}$ for some $i, j \leq|V|$ is called a well-ordering of $\mathcal{G}$. Note that in a well-ordered DAG the set $\left\{v_{1}, \ldots, v_{k}\right\}$ is ancestral for all $k \leq|V|$.

Finally, let $\mathcal{G}$ be a UG and let $I, J, K \subseteq V$ be pairwise disjoint. A path from $I$ to $J$ is a path from a vertex $v \in I$ to a vertex $w \in J$. We say that $K$ separates $I$ from $J$ in $\mathcal{G}$, and write $I \perp J \mid K[\mathcal{G}]$, if every path from $I$ to $J$ contains a vertex in $K$. In particular, we write $I \perp J \mid \emptyset[\mathcal{G}]$, or shortly $I \perp J[\mathcal{G}]$, if there exists no path between $I$ and $J$. We call $\mathcal{G}$ connected if for every distinct $v, w \in V$ there is a path from $v$ to $w$. A connected UG without cycles is a tree. If there is a vertex $w \in V$ such that $\operatorname{ad}(w)=V \backslash\{w\}$ and $\operatorname{ad}(v)=\{w\}$ for all $v \in V \backslash\{w\}$, that is all vertices are solely adjacent to $w$, then $\mathcal{G}$ is called a star and $w$ is called its root vertex. Note that above terminology is not used consistently throughout the literature.

## Markovian probability measures

In graphical probability modelling, graphs are used to represent conditional independence properties of corresponding families of probability measures. Let $\mathcal{D}=(V, E)$ be a DAG on $d:=|V|$ vertices and let $P$ be a probability measure on $\mathbb{R}^{d}$. Moreover, let $\boldsymbol{X}$ be an $\mathbb{R}^{d}$-valued random variable distributed as $P$. For $I \subseteq V$, we write $\boldsymbol{X}_{I}:=\left(X_{v}\right)_{v \in I}$ and denote the corresponding $I$-margin of $P$ by $P_{I}$. If $I=\{v\}$ for some $v \in V$, we write $X_{v}$ and $P_{v}$ instead of $X_{\{v\}}$ and $P_{\{v\}}$. Furthermore, we write $\boldsymbol{X}_{I} \Perp \boldsymbol{X}_{J} \mid \boldsymbol{X}_{K}$ whenever $\boldsymbol{X}_{I}$ and $\boldsymbol{X}_{J}$ are conditionally independent given $\boldsymbol{X}_{K}$ for pairwise disjoint sets $I, J, K \subseteq V$. By convention, $\boldsymbol{X}_{I} \Perp \boldsymbol{X}_{J} \mid \boldsymbol{X}_{\emptyset}$ is understood as $\boldsymbol{X}_{I} \Perp \boldsymbol{X}_{J} . P$ is said to possess the local $\mathcal{D}$-Markov property if

$$
X_{v} \Perp \boldsymbol{X}_{\operatorname{nd}(v) \backslash \operatorname{pa}(v)} \mid \boldsymbol{X}_{\operatorname{pa}(v)} \quad \text { for all } v \in V
$$

Correspondingly, $P$ is said to possess the global $\mathcal{D}$-Markov property if

$$
I \perp J\left|K\left[\left(\mathcal{D}_{\operatorname{An}(I \cup J \cup K)}\right)^{m}\right] \Rightarrow \boldsymbol{X}_{I} \Perp \boldsymbol{X}_{J}\right| \boldsymbol{X}_{K} \quad \text { for all pairwise disjoint } I, J, K \subseteq V
$$

Equations (2.1) and (2.2) relate (conditional) independence properties of $P$ to graph separation properties of $\mathcal{D}$. Since $\operatorname{ad}(v) \cap(\operatorname{nd}(v) \backslash \operatorname{pa}(v))=\emptyset$ for every $v \in V$, it can be easily seen that the conditional independence restrictions obtained from Equation (2.1) correspond to missing edges in $\mathcal{D}$. One can show that $P$ has the local $\mathcal{D}$-Markov property if and only if $P$ has the global $\mathcal{D}$-Markov property, see Lauritzen (1996, p. 51). A probability measure satisfying Equations (2.1) and (2.2) is thus simply called $\mathcal{D}$-Markovian. Despite the aforementioned equivalence, the lists of explicit conditional independence restrictions obtained from Equations (2.1) and (2.2) may, however, be of different lengths. Note that a $\mathcal{D}$-Markovian probability measure can exhibit further conditional independence properties apart from those represented by $\mathcal{D}$. If, however, $P$ exhibits no conditional independence properties other than those represented by $\mathcal{D}$, then $P$ is

# 2. Bayesian networks 

called faithful to $\mathcal{D}$. Now let $P$ have Lebesgue-density $f$. One can show that $P$ is $\mathcal{D}$-Markovian if and only if $f$ has a so-called $\mathcal{D}$-recursive factorisation, that is

$$
f(\boldsymbol{x})=\prod_{v \in V} f_{v \mid \operatorname{pa}(v)}\left(x_{v} \mid \boldsymbol{x}_{\operatorname{pa}(v)}\right) \quad \text { for all } \boldsymbol{x}=\left(x_{1}, \ldots, x_{d}\right) \in \mathbb{R}^{d}
$$

where $f_{v \mid \operatorname{pa}(v)}\left(\cdot \mid \boldsymbol{x}_{\operatorname{pa}(v)}\right)$ denotes the conditional probability density function (pdf) of $X_{v}$ given $\boldsymbol{X}_{\operatorname{pa}(v)}=\boldsymbol{x}_{\operatorname{pa}(v)}$, see again Lauritzen (1996, p. 51). Note that there may be more than one DAG representing the same set of conditional independence restrictions. We call the set of DAGs representing the same conditional independence restrictions as $\mathcal{D}$ the Markov-equivalence class of $\mathcal{D}$, and denote it by $[\mathcal{D}]$. Two DAGs $\mathcal{D}_{1}=\left(V, E_{1}\right)$ and $\mathcal{D}_{2}=\left(V, E_{2}\right)$ are called Markov equivalent if $\left[\mathcal{D}_{1}\right]=\left[\mathcal{D}_{2}\right]$. By Verma and Pearl (1991), $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$ are Markov equivalent if and only if they have the same skeleton and the same v-structures. The Markov-equivalence class of $\mathcal{D}$ can be represented by a CG, the so-called essential graph $\mathcal{D}^{e}$ associated with $[\mathcal{D}]$, which has the same skeleton as $\mathcal{D}$ and contains a directed edge $v \rightarrow w$ if and only if all members of $[\mathcal{D}]$ contain $v \rightarrow w$, see Andersson et al. (1997). A DAG in $[\mathcal{D}]$ can be obtained from $\mathcal{D}^{e}$ by directing all undirected edges of $\mathcal{D}^{e}$ such that no new v-structures and no directed cycles are introduced. Figure 1 gives an example of a DAG on four vertices together with the essential graph associated with the corresponding Markov-equivalence class.
![img-0.jpeg](img-0.jpeg)

Figure 1: A DAG $\mathcal{D}$ (left) specifying the conditional independence restrictions $X_{1} \Perp X_{4} \mid \boldsymbol{X}_{23}$ and $X_{2} \Perp X_{3} \mid X_{1}$, and the essential graph $\mathcal{D}^{e}$ (right) associated with the corresponding Markov-equivalence class $[\mathcal{D}]$.

## Graphical models

A Bayesian network or (directed) graphical model based on $\mathcal{D}$ is a family of $\mathcal{D}$-Markovian probability measures. A comprehensive introduction to graphical models, and Bayesian networks in particular, is found in Lauritzen (1996) and Cowell et al. (2003), see also Pourret et al. (2008) for examples of applications. For lack of tractable continuous probability measures, statistical modelling with Bayesian networks has mostly been limited to multivariate discrete or normal distributions. Kurowicka and Cooke (2005) therefore used copulas to derive a rich and tractable class of continuous Bayesian networks, which we will investigate in Section 4.

# 3. Vine copula models 

## 3. Vine copula models

A $d$-variate copula, $d \in \mathbb{N}$, is a cumulative distribution function (cdf) on $[0,1]^{d}$ such that all univariate marginals are uniform on the interval $[0,1]$. By Sklar's theorem (Sklar, 1959), every $\operatorname{cdf} F$ on $\mathbb{R}^{d}$ with marginals $F_{1}, \ldots, F_{d}$ can be written as

$$
F(\boldsymbol{x})=C\left(F_{1}\left(x_{1}\right), \ldots, F_{d}\left(x_{d}\right)\right), \quad \boldsymbol{x}=\left(x_{1}, \ldots, x_{d}\right) \in \mathbb{R}^{d}
$$

for some suitable copula $C$. If $F$ is absolutely continuous and $F_{1}, \ldots, F_{d}$ are strictly increasing, a similar relationship holds for the pdf $f$ of $F$, namely

$$
f(\boldsymbol{x})=c\left(F_{1}\left(x_{1}\right), \ldots, F_{d}\left(x_{d}\right)\right) \prod_{i=1}^{d} f_{i}\left(x_{i}\right), \quad \boldsymbol{x}=\left(x_{1}, \ldots, x_{d}\right) \in \mathbb{R}^{d}
$$

where the copula density $c$ is uniquely determined. A comprehensive introduction to copulas is found in Joe (1997) and Nelsen (2006).

### 3.1. Pair-copula constructions and regular vines

While in recent years a vast catalogue of bivariate copula families (also known as pair-copula families) has accumulated in the literature, many of these bivariate families have no straightforward multivariate extension. Based on Joe (1996), Bedford and Cooke $(2001,2002)$ introduced a rich and flexible class of multivariate copulas that uses bivariate (conditional) copulas as building blocks only. The corresponding decomposition of a multivariate copula into bivariate copulas is called a pair-copula construction (PCC). The most widely researched copulas arising from PCCs are the vine copulas. These vine copulas admit a graphical representation called a regular vine (R-vine), which essentially consists of a sequence of trees, each edge of which is associated with a certain pair copula in the corresponding PCC. More precisely, let $V \neq \emptyset$ be a finite set and let $d:=|V|$. An R-vine on $V$ is a sequence $\mathcal{V}:=\left(T_{1}, \ldots, T_{d-1}\right)$ of trees $T_{1}=\left(V_{1}, E_{1}\right), \ldots, T_{d-1}=\left(V_{d-1}, E_{d-1}\right)$ such that $V_{1}=V$ and $V_{i}=E_{i-1}$ for $i \geq 2$, that is the vertices of tree $T_{i}$ are the edges of tree $T_{i-1}$. We here represent an edge $v-w$ in tree $T_{i}$, $i \in\{1, \ldots, d-1\}$, by the doubleton $\{v, w\}$ instead of by the pairs $(v, w)$ and $(w, v)$, that is $E_{i} \subseteq\{\{v, w\} \mid v \neq w \in V_{i}\}$. Moreover, every tree $T_{i}, i \geq 2$, of $\mathcal{V}$ has to satisfy a proximity condition requiring that $|v \Delta w|=2$ for every edge $\{v, w\} \in E_{i}$, where $u \Delta v=(u \cup v) \backslash(u \cap v)$. Two vertices in tree $T_{i}, i \geq 2$, can hence only be adjacent if the corresponding edges in tree $T_{i-1}$ share a common vertex. Last, every edge $\{v, w\} \in E:=E_{1} \cup \cdots \cup E_{d-1}$ carries a label $v \Delta w \mid v \cap w$ representing the (conditional) pair copula $C_{v \Delta w \mid v \cap w}$, where $v \Delta w \mid \emptyset$ is conveniently replaced by $v \Delta w$. Instead of $C_{v \Delta w \mid v \cap w}$ we also write $C_{v_{\Delta}, w_{\Delta} \mid v \cap w}$, where $v_{\Delta}:=v \backslash(v \cap w)$ and $w_{\Delta}:=w \backslash(v \cap w)$. The pdf $f$ of a $d$-variate probability measure with univariate marginals $F_{v}$,

$v \in V$, and copula $C_{\mathcal{V}}$ corresponding to $\mathcal{V}$ then takes the form

$$
f(\boldsymbol{x})=\prod_{\{v, w\} \in E} c_{v_{\Delta}, w_{\Delta} \mid v \cap w}\left(F_{v_{\Delta} \mid v \cap w}\left(x_{v_{\Delta}} \mid \boldsymbol{x}_{v \cap w}\right), F_{w_{\Delta} \mid v \cap w}\left(x_{w_{\Delta}} \mid \boldsymbol{x}_{v \cap w}\right) \mid \boldsymbol{x}_{v \cap w}\right) \prod_{v \in V} f_{v}\left(x_{v}\right)
$$

where $\boldsymbol{x}=\left(x_{v}\right)_{v \in V} \in \mathbb{R}^{d}$. Note that - similar to DAGs - the vertices in the first tree of $\mathcal{V}$ represent the univariate margins of $C_{\mathcal{V}}$. In contrast to DAGs, however, $\mathcal{V}$ does not have an interpretation in terms of Markov properties of $C_{\mathcal{V}}$. An example of an R -vine representing a five-variate vine copula is given in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: An R-vine specifying the pair copulas $C_{12}, C_{23}, C_{25}, C_{34}, C_{13 \mid 2}, C_{24 \mid 3}, C_{35 \mid 2}, C_{14 \mid 23}$, $C_{45 \mid 23}$, and $C_{15 \mid 234}$ (edge labels). Boundaries of vertices including either 1 or 5 appear in bold, see Section 5 .

For every $K \subseteq V$ and $v \in K$, we define $K_{-v}:=K \backslash\{v\}$. The conditional cdfs in Equation (3.1) can be evaluated tree-by-tree using a recursive formula derived in Joe (1996), which says that for every $v \in V$, every $K \subseteq V_{-v}$, and an arbitrary $w \in K$

$$
F_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right)=\frac{\partial C_{v, w \mid K_{-w}}\left(F_{v \mid K_{-w}}\left(x_{v} \mid \boldsymbol{x}_{K_{-w}}\right), F_{w \mid K_{-w}}\left(x_{w} \mid \boldsymbol{x}_{K_{-w}}\right) \mid \boldsymbol{x}_{K_{-w}}\right)}{\partial F_{w \mid K_{-w}}\left(x_{w} \mid \boldsymbol{x}_{K_{-w}}\right)}
$$

An iterative algorithm for evaluating the pdf in Equation (3.1) under a simplifying assumption of constant conditional copulas introduced below is given in Dißmann et al. (2012). The first partial derivatives of a pair copula $C_{v, w}$ are also known as $h$-functions. We write

$$
h_{\underline{v}, w}\left(u_{v}, u_{w}\right):=\frac{\partial C_{v, w}\left(u_{v}, u_{w}\right)}{\partial u_{w}} \quad \text { and } \quad h_{v, \underline{w}}\left(u_{v}, u_{w}\right):=\frac{\partial C_{v, w}\left(u_{v}, u_{w}\right)}{\partial u_{v}}, \quad\left(u_{v}, u_{w}\right) \in[0,1]^{2}
$$

Many popular pair-copula families exhibit closed-form expressions for these h-functions, see for instance Aas et al. (2009). Note that by Equation (3.2) we have

$$
h_{\underline{v}, w}\left(F_{v}\left(x_{v}\right), F_{w}\left(x_{w}\right)\right)=F_{v \mid w}\left(x_{v} \mid x_{w}\right) \quad \text { and } \quad h_{v, \underline{w}}\left(F_{v}\left(x_{v}\right), F_{w}\left(x_{w}\right)\right)=F_{w \mid v}\left(x_{w} \mid x_{v}\right)
$$

where $\left(x_{v}, x_{w}\right) \in \mathbb{R}^{2}$. Hence, we can extend the notion of h-functions to conditional pair copulas,

# 3.2. ML estimation and model selection in vine copula models 

and express the right hand side of Equation (3.2) by

$$
h_{\underline{v}, w \mid K_{-w}}\left(F_{v \mid K_{-w}}\left(x_{v} \mid \boldsymbol{x}_{K_{-w}}\right), F_{w \mid K_{-w}}\left(x_{w} \mid \boldsymbol{x}_{K_{-w}}\right) \mid \boldsymbol{x}_{K_{-w}}\right)
$$

Assume $p:=|K| \geq 1$, and write $K=\left\{w_{1}, \ldots, w_{p}\right\}$ such that $w_{i} \neq w_{j}$ for $i \neq j$. We define $K_{-i}:=$ $\left\{w_{i+1}, \ldots, w_{p}\right\}$ for every $i \in\{1, \ldots, p\}$. Observing that $f_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right)=\frac{\mathrm{d}}{\mathrm{d} x_{v}} F_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right)$, we obtain by the chain rule of differentiation

$$
f_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right)=f_{v}\left(x_{v}\right) \prod_{i=1}^{p} c_{v, w_{i} \mid K_{-i}}\left(F_{v \mid K_{-i}}\left(x_{v} \mid \boldsymbol{x}_{K_{-i}}\right), F_{w_{i} \mid K_{-i}}\left(x_{w_{i}} \mid \boldsymbol{x}_{K_{-i}}\right) \mid \boldsymbol{x}_{K_{-i}}\right)
$$

### 3.2. ML estimation and model selection in vine copula models

A vine copula model is a family of vine copulas together with families of univariate marginals. Maximum likelihood (ML) estimation in vine copula models was first considered in Aas et al. (2009). The findings therein were, however, restricted to vine copula models represented by Cand D-vines. A $C$-vine is an R-vine whose trees are all stars. Conversely, an R-vine is called a $D$-vine if all vertices in tree $T_{1}$ are adjacent to at most two other vertices. ML estimation in vine copula models based on general R-vines was considered in Dißmann et al. (2012).

Let $\mathcal{V}$ be an R-vine on $V$ with edge set $E$, and let $C_{v_{ \pm}, w_{ \pm} \mid v \cap w}\left(\cdot, \cdot ; \boldsymbol{\theta}_{v_{ \pm}, w_{ \pm} \mid v \cap w}\right),\{v, w\} \in E$, be given (conditional) pair copulas with joint parameter vector $\boldsymbol{\theta}:=\left(\boldsymbol{\theta}_{v_{ \pm}, w_{ \pm} \mid v \cap w}\right)_{\{v, w\} \in E} \in \boldsymbol{\Theta}$. We denote the corresponding vine copula family by $\left\{C_{\mathcal{V}, \boldsymbol{\theta}} \mid \boldsymbol{\theta} \in \boldsymbol{\Theta}\right\}$. Note that we dropped the values $\boldsymbol{x}_{u \cap v}$ of the conditioning variables from the pair copulas $C_{v_{ \pm}, w_{ \pm} \mid v \cap w}$, thus assuming that the corresponding copula family and parameter vector $\boldsymbol{\theta}_{v_{ \pm}, w_{ \pm} \mid v \cap w}$ remain constant for all $\boldsymbol{x}_{u \cap v} \in \mathbb{R}^{|u \cap v|}$. This simplifying assumption is made for computational convenience and has become common practice in likelihood inference for vine copula models, see Hobæk Haff et al. (2010) and Acar et al. (2012) for a critical assessment. Furthermore, let $\boldsymbol{u}=\left(\boldsymbol{u}^{1}, \ldots, \boldsymbol{u}^{n}\right)$, $n \in \mathbb{N}$, be a realisation of a sample of i.i.d. observations $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ from a random variable $\boldsymbol{U}$ on $[0,1]^{d}$ with copula family $\left\{C_{\mathcal{V}, \boldsymbol{\theta}} \mid \boldsymbol{\theta} \in \boldsymbol{\Theta}\right\}$ and uniform univariate margins. Equation (3.1) yields the log-likelihood function

$$
l(\boldsymbol{\theta} ; \boldsymbol{u})=\sum_{k=1}^{n} \sum_{\{v, w\} \in E} \log c_{v_{ \pm}, w_{ \pm} \mid v \cap w}\left(F_{v_{ \pm} \mid v \cap w}\left(u_{v_{ \pm}}^{k} \mid \boldsymbol{u}_{v \cap w}^{k} ; \boldsymbol{\theta}\right), F_{w_{ \pm} \mid v \cap w}\left(u_{w_{ \pm}}^{k} \mid \boldsymbol{u}_{v \cap w}^{k} ; \boldsymbol{\theta}\right) ; \boldsymbol{\theta}\right)
$$

The restriction to uniform univariate margins is made for computational convenience, see below.

## ML estimation

Since a joint estimation of the parameters of the univariate marginal distributions and the copula can become computationally demanding in high dimensions, a two-step estimation approach known as the inference functions for margins method (Joe and Xu, 1996) is frequently applied.

# 3.2. ML estimation and model selection in vine copula models 

First, the marginal parameters are estimated and second, given the estimates of the marginal parameters, the copula parameters are inferred. In a similar vein, Genest et al. (1995) proposed a semiparametric approach in which the empirical cdf is used to transform the univariate marginals to uniform $[0,1]$ distributions before estimating the parameters of the copula model, see Kim et al. (2007) for a comparison. ML estimation of the parameters in Equation (3.4) is frequently performed using a stepwise approach as first described in Aas et al. (2009). In a first step, ML estimates of the parameters of each pair-copula family are computed separately. Due to the recursive structure of the log-likelihood function outlined above, this estimation step is carried out tree-by-tree. We refer to the obtained parameter estimates as sequential ML estimates. In a second step, the full log-likelihood function is maximised jointly using the sequential ML estimates as starting values, yielding the so-called joint ML estimates $\widehat{\boldsymbol{\theta}}_{v_{z}, w_{z} \mid v \cap w},\{v, w\} \in E$. Large and small sample applications of the stepwise estimation procedure have shown that the sequential ML estimates also provide a good approximation of their joint counterparts, see Hobæk Haff (2012a,b) for consistency results and a simulation study. One might hence consider omitting the second estimation step in a given situation to reduce computational complexity.

## Model selection

Model selection for vine copula models comprises an estimation of the R-vine $\mathcal{V}$ and a selection of the pair-copula families for $C_{v_{z}, w_{z} \mid v \cap w},\{v, w\} \in E$. Given $\mathcal{V}$, the latter task of selecting pair-copula families can be performed tree-by-tree, choosing for each edge $\{v, w\} \in E$ the one pair-copula family among a given set of candidate families that optimises a given selection criterion like Akaike's information criterion (AIC) or the Bayesian information criterion (BIC). Dißmann et al. (2012) presented a greedy-type algorithm for the estimation of $\mathcal{V}$, which estimates the trees $T_{1}, \ldots, T_{d-2}$ sequentially, that is again tree-by-tree. Note that estimating tree $T_{d-2}$ also fixes tree $T_{d-1}$. Structure estimation for tree $T_{i}=\left(V_{i}, E_{i}\right), i \in\{1, \ldots, d-2\}$, is carried out in three steps. In a first step, a weight $\omega_{v, w}$ is assigned to every pair of vertices $v, w \in V_{i}$ with $|v \Delta w|=2$. Suitable weights given the data are, for instance, the absolute values of estimates of Kendall's $\tau$, or AIC or BIC values of selected pair-copula families with estimated parameters. In a second step, $T_{i}$ is set to be a tree on $V_{i}$ optimising the sum of edge weights $\sum_{\{v, w\} \in E_{i}} \omega_{v, w}$, where $|v \Delta w|=2$ for all $\{v, w\} \in E_{i}$ to ensure the proximity condition. Such an optimal spanning tree can be found using the algorithms by Kruskal (1956) or Prim (1957). In a last step, a pair-copula family is assigned to each edge $\{v, w\} \in E_{i}$, as described above, and an ML estimate of the corresponding parameter(s) is computed. This last step may have already been performed when computing the edge weights $\omega_{v, w}$. Note that due to the greedy nature of the algorithm, the resulting R-vine need not optimise the sum of all edge weights $\sum_{\{v, w\} \in E} \omega_{v, w}$. The search for optimal spanning trees reduces to a search for root vertices when only considering C-vines instead of the more general R-vines, cf. Czado et al. (2012). Since a D-vine is completely determined by tree $T_{1}$, only one tree has to be specified when restricting the class of R-vines

# 4. Pair-copula Bayesian networks (PCBNs) 

to D-vines. Due to the particular structure of D-vines, however, finding tree $T_{1}$ by the above method leads to a travelling salesman problem (TSP) (Applegate et al., 2007), which is NP-hard. Kurowicka (2011) proposed an alternative structure selection algorithm, in which $\mathcal{V}$ is built in reverse order from tree $T_{d-1}$ to tree $T_{1}$ using partial correlation estimates as weights. Bayesian approaches to structure estimation have been considered in Smith et al. (2010), Min and Czado (2011), and Gruber et al. (2012). A more detailed exposition of vine copula models is found in Kurowicka and Joe (2011). Implementations of model selection and ML estimation procedures for vine copula models are available in the R package VineCopula (Schepsmeier et al., 2012).

The construction of a $d$-variate vine copula model requires the specification of $\binom{d}{2}$ pair-copula families, a number growing quadratically in $d$. The actual number of decisions to make in practical applications may, however, be lower if we happen to discover (conditional) independences in the analysed data. In that case, the corresponding pair copulas are set to be independence copulas. Since above structure estimation algorithm is based on the idea of modelling strongest dependences in the first trees, Brechmann et al. (2012) proposed to set all pair copulas in the later trees to independence copulas, which leads to so-called truncated $R$-vines. Instead of leaving the detection of (conditional) independences to chance, one may, however, consider modelling these independences in the first place to obtain more parsimonious models. Unfortunately, the construction of vine copula models satisfying pre-specified conditional independence restrictions is a hard problem in general. A class of models suited for this task are the Bayesian networks discussed in Section 2. Kurowicka and Cooke (2005) hence joined graphical and copula modelling to introduce PCCs for Bayesian networks, which we will investigate in the next section.

## 4. Pair-copula Bayesian networks (PCBNs)

Let $\mathcal{D}=(V, E)$ be a DAG, and let $P$ be an absolutely continuous $\mathcal{D}$-Markovian probability measure on $\mathbb{R}^{d}, d:=|V|$, with strictly increasing univariate marginal cdfs. Moreover, let $w_{v}:\{1, \ldots,|\mathrm{pa}(v)|\} \rightarrow \mathrm{pa}(v), i \mapsto w_{i}:=w_{v}(i)$, be a bijection for every $v \in V$ with $|\mathrm{pa}(v)| \geq 1$. We introduce a total order $<_{v}$ on $\mathrm{pa}(v)$ for every $v \in V$ such that whenever $|\mathrm{pa}(v)| \geq 1$ we have $w_{i}<_{v} w_{j}$ if and only if $i<j$ for all $i, j \in\{1, \ldots,|\mathrm{pa}(v)|\}$. Note that there are $|\mathrm{pa}(v)|$ ! permutations of $\mathrm{pa}(v)$ (up to isomorphism). We call $\mathcal{O}:=\left\{<_{v} \mid v \in V\right\}$ a set of parent orderings for $\mathcal{D}$. For every $v \in V$ and $w \in \mathrm{pa}(v)$, we set

$$
\mathrm{pa}(v ; w):=\left\{u \in \mathrm{pa}(v) \mid u<_{v} w\right\}=\left\{w_{i} \in \mathrm{pa}(v) \mid i<w_{v}^{-1}(w)\right\}
$$

By Sklar's theorem, we know that the cdf of $P$ can be uniquely decomposed into the univariate marginals $F_{1}, \ldots, F_{d}$ and a copula $C$. Bauer et al. (2012) have shown that $C$ can be further decomposed into the (conditional) pair copulas $C_{v, w \mid \mathrm{pa}(v ; w)}, v \in V, w \in \mathrm{pa}(v)$, which yields a PCC for $C$ in which each (conditional) pair copula corresponds to exactly one edge $w \rightarrow v$ in

# 4.1. Evaluating conditional cdfs in PCBNs 

$\mathcal{D}$. The pdf $f$ of $P$ can hence be written as

$$
f(\boldsymbol{x})=\prod_{v \in V} f_{v}\left(x_{v}\right) \prod_{w \in \mathrm{pa}(v)} c_{v, w \mid \mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(x_{w} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right)
$$

where $\boldsymbol{x}=\left(x_{v}\right)_{v \in V} \in \mathbb{R}^{d}$. As an example consider the DAG in Figure 1 with ordering $2<_{4} 3$ of $\mathrm{pa}(4)=\{2,3\}$. Equation (4.1) yields

$$
\begin{aligned}
f(\boldsymbol{x})= & f_{1}\left(x_{1}\right) \cdots f_{4}\left(x_{4}\right) \cdot c_{21}\left(F_{2}\left(x_{2}\right), F_{1}\left(x_{1}\right)\right) \cdot c_{31}\left(F_{3}\left(x_{3}\right), F_{1}\left(x_{1}\right)\right) \cdot c_{42}\left(F_{4}\left(x_{4}\right), F_{2}\left(x_{2}\right)\right) \\
& \cdot c_{43 \mid 2}\left(F_{4 \mid 2}\left(x_{4} \mid x_{2}\right), F_{3 \mid 2}\left(x_{3} \mid x_{2}\right) \mid x_{2}\right), \quad \boldsymbol{x}=\left(x_{1}, \ldots, x_{4}\right) \in \mathbb{R}^{4}
\end{aligned}
$$

where $F_{4 \mid 2}\left(x_{4} \mid x_{2}\right)=h_{32}\left(F_{4}\left(x_{4}\right), F_{2}\left(x_{2}\right)\right)$ by Equation (3.2) and

$$
F_{3 \mid 2}\left(x_{3} \mid x_{2}\right)=\int_{0}^{1} c_{21}\left(F_{2}\left(x_{2}\right), u_{1}\right) h_{31}\left(F_{3}\left(x_{3}\right), u_{1}\right) \mathrm{d} u_{1}
$$

see Bauer et al. (2012) for details. If we instead choose the ordering $3<_{4} 2$ for $\mathrm{pa}(4)=\{2,3\}$, we obtain the same decomposition as above with the roles of vertices 2 and 3 interchanged. Due to the appearing integral, the pair-copula decomposition in the example cannot be represented by an R-vine. There are, however, DAG PCCs representable by R-vines, see for instance Bauer et al. (2012) for a four-variate DAG PCC which coincides with a D-vine PCC.

### 4.1. Evaluating conditional cdfs in PCBNs

Similar to vine copulas, the challenge in Equation (4.1) lies in the evaluation of the conditional cdfs. Assume without loss of generality that $\mathcal{D}$ is well-ordered. Let $v \in V$ and let $J \subseteq V \backslash\{v\}$ be non-empty. We will now derive a pair-copula decomposition for the conditional cdf $F_{v \mid J}\left(\cdot \mid \boldsymbol{x}_{J}\right)$. We begin by exploiting the (conditional) independence restrictions represented by $\mathcal{D}$. To this end, consider the moral graph $\mathcal{G}:=\left(\mathcal{D}_{\mathrm{An}(\{v\} \cup J)}\right)^{m}$. If $\{v\} \perp I \mid(J \backslash I)[\mathcal{G}]$ for some non-empty $I \subseteq J$, then the global $\mathcal{D}$-Markov property in Equation (2.2) yields with $K:=J \backslash I$

$$
f_{v \mid J}\left(x_{v} \mid \boldsymbol{x}_{J}\right)=\frac{f_{\{v\} \cup J}\left(\boldsymbol{x}_{\{v\} \cup J}\right)}{f_{J}\left(\boldsymbol{x}_{J}\right)}=\frac{f_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right) f_{I \mid K}\left(\boldsymbol{x}_{I} \mid \boldsymbol{x}_{K}\right) f_{K}\left(\boldsymbol{x}_{K}\right)}{f_{I \mid K}\left(\boldsymbol{x}_{I} \mid \boldsymbol{x}_{K}\right) f_{K}\left(\boldsymbol{x}_{K}\right)}=f_{v \mid K}\left(x_{v} \mid \boldsymbol{x}_{K}\right)
$$

where by convention $f_{W \mid \emptyset}\left(\boldsymbol{x}_{W} \mid \boldsymbol{x}_{\emptyset}\right):=f_{W}\left(\boldsymbol{x}_{W}\right)$ for every $W \subseteq V$, and $f_{\emptyset}\left(\boldsymbol{x}_{\emptyset}\right):=1$. Thus, $F_{v \mid J}\left(\cdot \mid \boldsymbol{x}_{J}\right)=F_{v \mid K}\left(\cdot \mid \boldsymbol{x}_{K}\right)$, and we can continue with the conditioning set $K$. The case $K=\emptyset$ is trivial. Assume $K \neq \emptyset$. Observing that

$$
F_{v \mid K}\left(y \mid \boldsymbol{x}_{K}\right)=\frac{\int_{-\infty}^{y} f_{\{v\} \cup K}\left(\boldsymbol{x}_{\{v\} \cup K}\right) \mathrm{d} x_{v}}{f_{K}\left(\boldsymbol{x}_{K}\right)}
$$

we next need to find pair-copula decompositions for $f_{\{v\} \cup K}$ and $f_{K}$.

# 4.1. Evaluating conditional cdfs in PCBNs 

## Pair-copula decompositions for marginal pdfs

More generally, let $I \subseteq V$ be non-empty and consider the (marginal) pdf $f_{I}$. For every $v \in I$, we set $I_{-v}:=I \backslash\{v\}$ and obtain the following lemma.

Lemma 4.1. Let $\mathcal{D}=(V, E)$ be a well-ordered $D A G$ on $d:=|V|$ vertices, and let $P$ be an absolutely continuous $\mathcal{D}$-Markovian probability measure on $\mathbb{R}^{d}$ with pdf $f$. Let $I \subseteq V$ be nonempty and let $v$ denote the maximal vertex in $I$ by the well-ordering of $\mathcal{D}$. Moreover, define $S_{v}:=\left\{u \in \mathrm{pa}(v) \mid\{u\} \perp I_{-v}\left[\left(\mathcal{D}_{\mathrm{An}\left(\{u\} \cup I_{-v}\}\right)^{m}\right]\right\}\right.$ and

$$
W_{v}:= \begin{cases}\emptyset & \text { if } I_{-v}=\emptyset \text { or } S_{v}=\mathrm{pa}(v) \\ \left\{w_{1}\right\} \cup \mathrm{pa}\left(v ; w_{1}\right) & \text { if } I_{-v} \subseteq \mathrm{pa}(v) \text { and } I_{-v} \neq \emptyset \\ \left\{w_{2}\right\} \cup \mathrm{pa}\left(v ; w_{2}\right) & \text { else }\end{cases}
$$

where $w_{1}$ and $w_{2}$ denote the maximal vertices in $I_{-v}$ and $\mathrm{pa}(v) \backslash S_{v}$, respectively, by a given parent ordering $<_{v}$. Then for all $\boldsymbol{x}_{I}=\left(x_{u}\right)_{u \in I} \in R^{|I|}$,

$$
f_{I}\left(\boldsymbol{x}_{I}\right)=\int_{\mathbb{R}^{|W_{v} \backslash I|}} f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v} \cup I_{-v}}\left(\boldsymbol{x}_{W_{v} \cup I_{-v}}\right) \mathrm{d} \boldsymbol{x}_{W_{v} \backslash I}
$$

Note that by convention, $\int_{\mathbb{R}^{0}} g(\boldsymbol{x}) \mathrm{d} \boldsymbol{x}_{\emptyset}:=g(\boldsymbol{x})$ for every integrable function $g: \mathbb{R}^{k} \rightarrow \mathbb{R}, k \in \mathbb{N}$. Also note that the parent ordering $<_{v}$ need not concur with the well-ordering of $\mathcal{D}$.

Proof. As can be seen from the definition of $W_{v}$, the decomposition of $f_{I}$ in the lemma's claim depends on the relation between the sets $I_{-v}$ and $\mathrm{pa}(v)$. Assume first that $I_{-v}=\emptyset$. Then $f_{I}=f_{v}$ and the claim is trivial.

Next, assume $I_{-v} \neq \emptyset$ but $\mathrm{pa}(v)=\emptyset$. Then $S_{v}=\emptyset$. Since $v$ is maximal in $I$ by the well-ordering of $\mathcal{D}, v$ has no descendants in $I_{-v}$, and we have $\{v\} \perp I_{-v}\left[\left(\mathcal{D}_{\mathrm{An}(I)}\right)^{m}\right]$. The global $\mathcal{D}$-Markov property thus yields $f_{I}\left(\boldsymbol{x}_{I}\right)=f_{v}\left(x_{v}\right) f_{I_{-v}}\left(\boldsymbol{x}_{I_{-v}}\right)$, that is Equation (4.3) for $W_{v}:=\emptyset$.

From now on assume $I_{-v} \neq \emptyset$ and $\mathrm{pa}(v) \neq \emptyset$. The possible relations between $I_{-v}$ and $\mathrm{pa}(v)$ are illustrated in Figure 3. If $I_{-v} \subseteq \mathrm{pa}(v)$ (Figure 3a), we extend $I_{-v}$ to $W_{v}:=\left\{w_{1}\right\} \cup \mathrm{pa}\left(v ; w_{1}\right) \supseteq I_{-v}$ and obtain as claimed

$$
f_{I}\left(\boldsymbol{x}_{I}\right)=\int_{\mathbb{R}^{|W_{v} \backslash I|}} f_{\{v\} \cup W_{v}}\left(\boldsymbol{x}_{\{v\} \cup W_{v}}\right) \mathrm{d} \boldsymbol{x}_{W_{v} \backslash I}=\int_{\mathbb{R}^{|W_{v} \backslash I|}} f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v}}\left(\boldsymbol{x}_{W_{v}}\right) \mathrm{d} \boldsymbol{x}_{W_{v} \backslash I}
$$

Note that in case $I_{-v}=\left\{w_{1}\right\} \cup \mathrm{pa}\left(v ; w_{1}\right)$, no integration is required since then $W_{v} \backslash I=\emptyset$.
Next, let $I_{-v} \cap \mathrm{pa}(v)=\emptyset$ (Figure 3b). If $S_{v}=\mathrm{pa}(v)$, then $\{v\} \perp I_{-v}\left[\left(\mathcal{D}_{\mathrm{An}(I)}\right)^{m}\right]$ since $v$ has no descendants in $I_{-v}$. Hence, we again have $f_{I}\left(\boldsymbol{x}_{I}\right)=f_{v}\left(x_{v}\right) f_{I_{-v}}\left(\boldsymbol{x}_{I_{-v}}\right)$, that is Equation (4.3)

![img-2.jpeg](img-2.jpeg)

Figure 3: Venn diagrams of the sets $I_{-v} \neq \emptyset$ and $\mathrm{pa}(v) \neq \emptyset$, and corresponding definitions of $W_{v}$ (see lower captions).
for $W_{v}:=\emptyset$. If, however, $S_{v} \neq \mathrm{pa}(v)$, then $\{v\} \perp I_{-v} \mid \mathrm{pa}\left(v ; w_{2}\right)\left[\left(\mathcal{D}_{\mathrm{An}\left(\mathrm{pa}\left(v ; w_{2}\right) \cup I\right)}\right)^{m}\right]$, and with $W_{v}:=\left\{w_{2}\right\} \cup \mathrm{pa}\left(v ; w_{2}\right)$ the global $\mathcal{D}$-Markov property yields

$$
f_{I \cup W_{v}}\left(\boldsymbol{x}_{I \cup W_{v}}\right)=f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{I_{-v} \mid W_{v}}\left(\boldsymbol{x}_{I_{-v}} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v}}\left(\boldsymbol{x}_{W_{v}}\right)
$$

Since $I_{-v} \cap W_{v}=\emptyset$, we thus get

$$
f_{I}\left(\boldsymbol{x}_{I}\right)=\int_{\mathbb{R}^{|W_{v}|}} f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v} \cup I_{-v}}\left(\boldsymbol{x}_{W_{v} \cup I_{-v}}\right) \mathrm{d} \boldsymbol{x}_{W_{v}}
$$

Note that in case $S_{v}=\emptyset$, we have $W_{v}=\mathrm{pa}(v)$.
Finally, assume $I_{-v} \cap \mathrm{pa}(v) \neq \emptyset$ such that $I_{-v} \not \leq \mathrm{pa}(v)$ (Figure 3c). Similarly to Equation (4.4), we obtain with $W_{v}:=\left\{w_{2}\right\} \cup \mathrm{pa}\left(v ; w_{2}\right)$

$$
f_{I \cup W_{v}}\left(\boldsymbol{x}_{I \cup W_{v}}\right)=f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{\left(I_{-v} \backslash W_{v}\right) \mid W_{v}}\left(\boldsymbol{x}_{I_{-v} \backslash W_{v}} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v}}\left(\boldsymbol{x}_{W_{v}}\right)
$$

by the global $\mathcal{D}$-Markov property, and hence

$$
f_{I}\left(\boldsymbol{x}_{I}\right)=\int_{\mathbb{R}^{|W_{v} \backslash I|}} f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right) f_{W_{v} \cup I_{-v}}\left(\boldsymbol{x}_{W_{v} \cup I_{-v}}\right) \mathrm{d} \boldsymbol{x}_{W_{v} \backslash I}
$$

Note again that in case $S_{v}=\emptyset$, we have $W_{v}=\mathrm{pa}(v)$. Also, note that in case $\mathrm{pa}(v) \subseteq I_{-v}$ (Figure 3d), no integration is required. This establishes the claim.

The set $W_{v}$ in Lemma 4.1 is either empty or of the form $\{w\} \cup \mathrm{pa}(v ; w)$ for some $w \in \mathrm{pa}(v)$. In the latter case, we can express the conditional pdf $f_{v \mid\{w\} \cup \mathrm{pa}(v ; w)}\left(\cdot \mid \boldsymbol{x}_{\{w\} \cup \mathrm{pa}(v ; w)}\right)$ on the right hand side of Equation (4.3) in terms of the univariate marginals $F_{u}, u \in V$, and the (conditional) pair copulas $C_{v, u \mid \mathrm{pa}(v ; u)}, u \in \mathrm{pa}(v)$, as follows.

Lemma 4.2. Let the notation be as in Lemma 4.1 and let $P$ have strictly increasing univariate marginal cdfs. Let $I_{-v} \neq \emptyset$ and let $S_{v} \neq \mathrm{pa}(v)$. Then

$$
f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right)=f_{v}\left(x_{v}\right) \prod_{w \in W_{v}} c_{v, w \mid \mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(x_{w} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right)
$$

for all $x_{v} \in \mathbb{R}$ and $\boldsymbol{x}_{W_{v}}=\left(x_{w}\right)_{w \in W_{v}} \in \mathbb{R}^{\left|W_{v}\right|}$.
Proof. Since $I_{-v} \neq \emptyset$ and $S_{v} \neq \mathrm{pa}(v), W_{v}$ is non-empty and thus $W_{v}=\{u\} \cup \mathrm{pa}(v ; u)$ for some $u \in \mathrm{pa}(v)$. By Equation (3.3), we can hence write
$f_{v \mid W_{v}}\left(x_{v} \mid \boldsymbol{x}_{W_{v}}\right)=f_{v}\left(x_{v}\right) \prod_{w \in W_{v}} c_{v, w \mid \mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(x_{w} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right)$,
and the claim is proven.

Algorithm 1 Pair-copula decomposition of a (marginal) pdf.
Input Well-ordered DAG $\mathcal{D}$; set of parent orderings $\mathcal{O}$; non-empty vertex set $I \subseteq V$.
Output Factorisation $f . \%$ (marginal) pdf $f_{I}\left(\boldsymbol{x}_{I}\right)$
$f \leftarrow 1$;
$J \leftarrow \emptyset ; \%$ indices of integration variables
while $|I| \geq 1$ do
$\%$ Select maximal vertex:
$v \leftarrow$ maximal vertex in $I$ by the well-ordering of $\mathcal{D}$;
$f \leftarrow f \cdot f_{v}\left(x_{v}\right)$
$I \leftarrow I_{-v} ;$
$\%$ Determine the set $W_{v}$ :
$W \leftarrow \emptyset ;$
$S \leftarrow\left\{w \in \mathrm{pa}(v) \mid\{w\} \perp I\left[\left(\mathcal{D}_{\operatorname{An}(\{w\} \cup I\}})^{m}\right]\right\}\right.$
if $I \neq \emptyset$ and $S \neq p a(v)$ then
if $I \subseteq \mathrm{pa}(v)$ then
$w \leftarrow$ maximal vertex in $I$ by the parent ordering $<_{v}$;
$W \leftarrow\{w\} \cup \mathrm{pa}(v ; w)$
else
$w \leftarrow$ maximal vertex in $\mathrm{pa}(v) \backslash S$ by the parent ordering $<_{v}$;
$W \leftarrow\{w\} \cup \mathrm{pa}(v ; w)$
end if
end if
$\%$ Introduce corresponding pair copulas and integration variables:
for $w \in W$ do
$f \leftarrow f \cdot c_{v, w \mid \mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(x_{w} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right)$;
if $w \notin I$ then
$I \leftarrow I \cup\{w\} ;$
$J \leftarrow J \cup\{w\} ;$
end if
end for
end while
$f \leftarrow \int_{\mathbb{R}^{|J|}} f \mathrm{~d} \boldsymbol{x}_{J} ;$

Since all vertices in $W_{v} \cup I_{-v}$ are smaller than $v$ by the well-ordering of $\mathcal{D}$ and since $V$ is finite, we can inductively apply Lemmas 4.1 and 4.2 to the pdf $f_{W_{v} \cup I_{-v}}$ in Equation (4.3) until

no unconditional pdfs of dimension higher than one remain. Let $J$ denote the set of vertices corresponding to the integration variables added during this iterative procedure (and including $W_{v} \backslash I)$. Given a set $\mathcal{O}$ of parent orderings for $\mathcal{D}$, Lemma 4.1 yields a set $W_{u}$ for every $u \in I \cup J$. We have hence established the following theorem.

Theorem 4.3. Let the notation be as in Lemma 4.2. Then $f_{I}\left(\boldsymbol{x}_{I}\right)$ takes the form

$$
\int_{\mathbb{R}^{|J|}} \prod_{v \in(I \cup J)} f_{v}\left(x_{v}\right) \prod_{w \in W_{v}} c_{v, w|\mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(x_{w} \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mid \boldsymbol{x}_{\mathrm{pa}(v ; w)}\right) \mathrm{d} \boldsymbol{x}_{J}
$$

for all $\boldsymbol{x}_{I}=\left(x_{v}\right)_{v \in I} \in R^{|I|}$.
Note that in the special case $I=V$, Theorem 4.3 yields Equation (4.1). Above procedure for deriving a pair-copula decomposition of $f_{I}$ as given in Theorem 4.3 is summarised in Algorithm 1.

Example. We consider the well-ordered DAG $\mathcal{D}$ in Figure 4. The edges and parent orderings of $\mathcal{D}$ can be summarised in a matrix $A_{\mathcal{D}}=\left(a_{i j}\right)_{1 \leq i, j \leq 7}$ whose elements satisfy $a_{i j}=k, k \leq|\mathrm{pa}(j)|$, if $\mathcal{D}$ contains the edge $i \rightarrow j$ and if $i$ is the $k$-th smallest parent of $j$ by $<_{j}$, and $a_{i j}=0$ otherwise, see Figure 4. For the reader's convenience we will omit function arguments. Equation (4.1) yields

$$
\begin{aligned}
f= & f_{1} \cdots f_{7} c_{21}\left(F_{2}, F_{1}\right) c_{31}\left(F_{3}, F_{1}\right) c_{42}\left(F_{4}, F_{2}\right) c_{41 \mid 2}\left(F_{4 \mid 2}, F_{1 \mid 2}\right) c_{54}\left(F_{5}, F_{4}\right) c_{53 \mid 4}\left(F_{5 \mid 4}, F_{3 \mid 4}\right) \\
& \cdot c_{65}\left(F_{6}, F_{5}\right) c_{64 \mid 5}\left(F_{6 \mid 5}, F_{4 \mid 5}\right) c_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{62 \mid 543}\left(F_{6 \mid 543}, F_{2 \mid 543}\right) c_{75}\left(F_{7}, F_{5}\right) \\
& \cdot c_{76 \mid 5}\left(F_{7 \mid 5}, F_{6 \mid 5}\right) c_{73 \mid 56}\left(F_{7 \mid 56}, F_{3 \mid 56}\right) .
\end{aligned}
$$

We will later derive a pair-copula decomposition for $F_{3 \mid 56}$. In preparation, we now use Algorithm 1 to derive pair-copula decompositions for $f_{356}$ and $f_{56}$.
![img-3.jpeg](img-3.jpeg)


Figure 4: A well-ordered (vertex labels) DAG $\mathcal{D}$ (left) with parent orderings $2<_{4} 1,4<_{5} 3$, $5<_{6} 4<_{6} 3<_{6} 2,5<_{7} 6<_{7} 3$ specifying the pair copulas $C_{21}, C_{31}, C_{42}, C_{41 \mid 2}, C_{54}$, $C_{53 \mid 4}, C_{65}, C_{64 \mid 5}, C_{63 \mid 54}, C_{62 \mid 542}, C_{75}, C_{76 \mid 5}, C_{73 \mid 56}$ (edge labels), and corresponding representation matrix $A_{\mathcal{D}}$ (right).

# 4.1. Evaluating conditional cdfs in PCBNs 

As a result of applying Algorithm 1 to $f_{356}$ and $f_{56}$, we obtain

$$
\begin{aligned}
f_{356}= & \int_{\mathbb{R}^{3}} f_{6|543} f_{5|43} f_{4|21} f_{3|1} f_{2|1} f_{1} \mathrm{~d} \boldsymbol{x}_{124} \\
= & \int_{\mathbb{R}^{3}} f_{6} c_{63|54}\left(F_{6|54}, F_{3|54}\right) c_{64|5}\left(F_{6|5}, F_{4|5}\right) c_{65}\left(F_{6}, F_{5}\right) f_{5} c_{53|4}\left(F_{5|4}, F_{3|4}\right) c_{54}\left(F_{5}, F_{4}\right) \\
& \cdot f_{4} c_{41|2}\left(F_{4|2}, F_{1|2}\right) c_{42}\left(F_{4}, F_{2}\right) f_{3} c_{31}\left(F_{3}, F_{1}\right) f_{2} c_{21}\left(F_{2}, F_{1}\right) f_{1} \mathrm{~d} \boldsymbol{x}_{124}
\end{aligned}
$$

and $f_{56}=f_{6|5} f_{5}=f_{6} c_{65}\left(F_{6}, F_{5}\right) f_{5}$, respectively, see Table 1.


Table 1: Vertices and vertex sets obtained during the application of Algorithm 1 to the pdfs $f_{356}$ and $f_{56}$ corresponding to the DAG $\mathcal{D}$ in Figure 4.

## When can $\int_{-\infty}^{y} f_{\{v\} \cup K}\left(\boldsymbol{x}_{\{v\} \cup K}\right) \mathrm{d} x_{v}$ in Equation (4.2) be further simplified?

Let us now return to the conditional cdf in Equation (4.2). Setting $I:=\{v\} \cup K$, the numerator on the right hand side of Equation (4.2) takes the form $\int_{-\infty}^{y} f_{I}\left(\boldsymbol{x}_{I}\right) \mathrm{d} x_{v}$. Decompose $f_{I}\left(\boldsymbol{x}_{I}\right)$ according to Theorem 4.3, and let $J$ denote the set of vertices corresponding to the newly added integration variables. Clearly, $J \subseteq \operatorname{An}(I) \backslash I$. If the old integration variable $x_{v}$ does not appear as a conditioning variable in one of the pair copulas $C_{v, w \mid \operatorname{pa}(v ; w)}, v \in I \cup J, w \in W_{v}$, in the decomposition of $f_{I}$, it may be possible to solve the integral with respect to $x_{v}$ analytically. More precisely, let $J^{\prime} \subseteq J$ and let $W^{\prime} \subseteq W:=I_{-v} \cup J^{\prime}$ be non-empty. Let $k:=\left|W^{\prime}\right|$ and write $W^{\prime}=\left\{w_{1}, \ldots, w_{k}\right\}$. Moreover, set $W_{-i}^{\prime}:=\left\{w_{1}, \ldots, w_{i-1}\right\}$ for all $i \in\{1, \ldots k\}$. Assume that the pair copula $C_{v, w_{k} \mid W_{-k}^{\prime}}$ is available in the pair-copula decomposition of $f$, that is $W_{-k}^{\prime}=\operatorname{pa}\left(v ; w_{k}\right)$ or $W_{-k}^{\prime}=\operatorname{pa}\left(w_{k} ; v\right)$, and that (after possible algebraic manipulation) $f_{I}$ takes the form

$$
\int_{\mathbb{R}\left|J^{\prime}\right|} f_{v}\left(x_{v}\right) \prod_{i=1}^{k} c_{v, w_{i} \mid W_{-i}^{\prime}}\left(F_{v \mid W_{-i}^{\prime}}\left(x_{v} \mid \boldsymbol{x}_{W_{-i}^{\prime}}\right), F_{w_{i} \mid W_{-i}^{\prime}}\left(x_{w_{i}} \mid \boldsymbol{x}_{W_{-i}^{\prime}}\right) \mid \boldsymbol{x}_{W_{-i}^{\prime}}\right) f_{W}\left(\boldsymbol{x}_{W}\right) \mathrm{d} \boldsymbol{x}_{J^{\prime}}
$$

# 4.1. Evaluating conditional cdfs in PCBNs 

Then Fubini's theorem and Equation (3.3) yield that $\int_{-\infty}^{y} f_{I}\left(\boldsymbol{x}_{I}\right) \mathrm{d} x_{v}$ takes the form

$$
\int_{\mathbb{R}\left[J^{\prime}\right]} h_{v, w_{k} \mid W_{-k}^{\prime}}\left(F_{v \mid W_{-k}^{\prime}}\left(y \mid \boldsymbol{x}_{W_{-k}^{\prime}}\right), F_{w_{k} \mid W_{-k}^{\prime}}\left(x_{w_{k}} \mid \boldsymbol{x}_{W_{-k}^{\prime}}\right) \mid \boldsymbol{x}_{W_{-k}^{\prime}}\right) f_{W}\left(\boldsymbol{x}_{W}\right) \mathrm{d} \boldsymbol{x}_{J^{\prime}}
$$

where the integral with respect to $x_{v}$ was replaced by an h-function which, by assumption, is available in the pair-copula decomposition of $f$. Note that some of the copula pdfs $c_{v, w_{i} \mid W_{-i}^{\prime}}$, $i \in\{1, \ldots, k-1\}$, in Equation (4.6) may not correspond to an edge in $\mathcal{D}$, but may instead be given implicitly by an integral over further variables, or may be equal to 1 due to a related Markov property of $P$, see also the example below. We need to take these special cases into account when checking the applicability of the inverse chain rule algorithmically.

It may sometimes also be useful to substitute $u_{w}:=F_{w}\left(x_{w}\right)$, that is $\mathrm{d} u_{w}=f_{w}\left(x_{w}\right) \mathrm{d} x_{w}$, for all $w \in J$ in the pair-copula decomposition of $f_{I}$, and thus to write

$$
f_{I}\left(\boldsymbol{x}_{I}\right)=\int_{[0,1]^{|J|}} c_{I \cup J}\left(\left(F_{w}\left(x_{w}\right)\right)_{w \in I}, \boldsymbol{u}_{J}\right) \prod_{w \in I} f_{w}\left(x_{w}\right) \mathrm{d} \boldsymbol{u}_{J}
$$

A similar transformation can be applied to the denominator in Equation (4.2) if integration variables are present.

Example (continued). Consider the integral $\int_{-\infty} f_{356} \mathrm{~d} x_{3}$ associated to the DAG $\mathcal{D}$ in Figure 4, which will later appear when deriving a pair-copula decomposition for $F_{3 \mid 56}$. Observing that

$$
\begin{aligned}
\int_{\mathbb{R}^{2}} f_{4} c_{41 \mid 2}\left(F_{4 \mid 2}, F_{1 \mid 2}\right) c_{42}\left(F_{4}, F_{2}\right) f_{3} c_{31}\left(F_{3}, F_{1}\right) f_{2} c_{21}\left(F_{2}, F_{1}\right) f_{1} \mathrm{~d} \boldsymbol{x}_{12} & =\int_{\mathbb{R}^{2}} f_{1234} \mathrm{~d} \boldsymbol{x}_{12}=f_{34} \\
& =f_{4} f_{3} c_{43}\left(F_{4}, F_{3}\right)
\end{aligned}
$$

Equation (4.5) yields

$$
\begin{aligned}
\int_{-\infty} f_{356} \mathrm{~d} x_{3}= & \int_{-\infty} \int_{\mathbb{R}} f_{3} c_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{53 \mid 4}\left(F_{5 \mid 4}, F_{3 \mid 4}\right) c_{43}\left(F_{4}, F_{3}\right) \\
& \cdot f_{6} c_{64 \mid 5}\left(F_{6 \mid 5}, F_{4 \mid 5}\right) c_{65}\left(F_{6}, F_{5}\right) f_{5} c_{54}\left(F_{5}, F_{4}\right) f_{4} \mathrm{~d} x_{4} \mathrm{~d} x_{3}
\end{aligned}
$$

Note that $c_{43}$ is not available in the pair-copula decomposition of $f$. Since by Equation (3.3)

$$
\int_{-\infty} f_{3} c_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{53 \mid 4}\left(F_{5 \mid 4}, F_{3 \mid 4}\right) c_{43}\left(F_{4}, F_{3}\right) \mathrm{d} x_{3}=h_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right)
$$

we can, however, simplify the integral with respect to $x_{3}$, and $c_{43}$ vanishes. We obtain

$$
\int_{-\infty} f_{356} \mathrm{~d} x_{3}=\int_{\mathbb{R}} f_{6} h_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{64 \mid 5}\left(F_{6 \mid 5}, F_{4 \mid 5}\right) c_{65}\left(F_{6}, F_{5}\right) f_{5} c_{54}\left(F_{5}, F_{4}\right) f_{4} \mathrm{~d} x_{4}
$$

# 4.1. Evaluating conditional cdfs in PCBNs 

## Pair-copula decompositions for conditional cdfs

Summing up, a pair-copula decomposition for the conditional cdf $F_{v \mid K}\left(\cdot \mid \boldsymbol{x}_{K}\right)$ in Equation (4.2) is obtained in three steps. First, we apply Theorem 4.3 to $f_{\{v\} \cup K}$ and $f_{K}$. Second, we possibly apply the inverse chain rule to the integral with respect to $x_{v}$ in the numerator. Last, we cancel common factors like $\prod_{w \in K} f_{w}\left(x_{w}\right)$ in the numerator and the denominator. The procedure is summarised in Algorithm 2.

```
Algorithm 2 Pair-copula decomposition of a conditional cdf.
Input Well-ordered DAG \(\mathcal{D}\); set of parent orderings \(\mathcal{O}\); vertex \(v \in V\) (conditioned variable),
    vertex set \(K \subseteq V_{-v}\) (conditioning variables).
Output Factorisation \(F\). \% conditional cdf \(F_{v \mid K}\left(y \mid \boldsymbol{x}_{K}\right)\)
    \% Exploit global \(\mathcal{D}\)-Markov property:
    while \(\exists w \in K:\{v\} \perp\{w\} \mid K_{-w}\left[\left(\mathcal{D}_{\operatorname{An}(\{v\} \cup K)}\right)^{m}\right]\) do
        \(K \leftarrow K_{-w}\);
    end while
    \% Numerator:
    \(n \leftarrow \operatorname{Algorithm} .1(\mathcal{D}, \mathcal{O},\{v\} \cup K)\);
    \(n \leftarrow \int_{-\infty}^{y} n \mathrm{~d} x_{v}\);
    simplify \(n\) with inverse chain rule for variable \(x_{v}\) if possible;
    \(\%\) Denominator:
    \(d \leftarrow \operatorname{Algorithm} .1(\mathcal{D}, \mathcal{O}, K)\);
    \% Conditional cdf \(F_{v \mid K}\left(y \mid \boldsymbol{x}_{K}\right)\);
    cancel common factors in \(n\) and \(d\);
    \(F \leftarrow \frac{n}{d}\);
```

As can be seen from Theorem 4.3 and Equation (4.7), the factorisation for $F_{v \mid K}\left(\cdot \mid \boldsymbol{x}_{K}\right)$ obtained from Algorithm 2 may contain some new conditional cdfs. This problem can, however, be solved inductively. Let $w$ denote the maximal vertex in $\{v\} \cup K$ by the well-ordering of $\mathcal{D}$. Since Algorithm 2 only adds ancestors of $\{v\} \cup K$ as integration variables, all vertices involved in the new conditional cdfs are smaller than or equal to $w$ by the well-ordering of $\mathcal{D}$. In particular, those conditional cdfs involving $w$ are of the special form $F_{w \mid \operatorname{pa}(w ; u)}\left(\cdot \mid \boldsymbol{x}_{\operatorname{pa}(w ; u)}\right)$ for some $u \in \operatorname{pa}(w)$, and can by Equation (3.2) iteratively be expressed as

$$
F_{v \mid \operatorname{pa}(w ; u)}\left(x_{v} \mid \boldsymbol{x}_{\operatorname{pa}(w ; u)}\right)=h_{\underline{v}, u \mid \operatorname{pa}(v ; u)}\left(F_{v \mid \operatorname{pa}(v ; u)}\left(x_{v} \mid \boldsymbol{x}_{\operatorname{pa}(v ; u)}\right), F_{u \mid \operatorname{pa}(v ; u)}\left(x_{u} \mid \boldsymbol{x}_{\operatorname{pa}(v ; u)}\right) \mid \boldsymbol{x}_{\operatorname{pa}(v ; u)}\right)
$$

Hence, all vertices involved in the algorithmically more demanding new conditional cdfs are strictly smaller than $w$ by the well-ordering of $\mathcal{D}$. Corresponding pair-copula decompositions for the new conditional cdfs can thus be computed inductively by again applying Algorithm 2. Since $V$ is finite, the whole procedure terminates after finitely many steps, and the desired decomposition in terms of only univariate marginals and (conditional) pair copulas is obtained.

# 4.2. Simulation, ML estimation, and model selection in PCBNs 

Overall, we observed that the problems of deriving pair-copula decompositions for a conditional cdf and a marginal pdf are deeply intertwined and can be solved by alternating iteration. Note that it is sufficient for our purposes to exploit only those conditional independence properties of $P$ which follow directly from graph separation in $\mathcal{D}$ via the global $\mathcal{D}$-Markov property. Once a complete decomposition for $f$ is obtained, the evaluation at $\boldsymbol{x} \in \mathbb{R}^{d}$ can be performed vertex-byvertex and parent-by-parent along the well-ordering of $\mathcal{D}$. That is, given $v^{*} \in V$ and $w^{*} \in \mathrm{pa}\left(v^{*}\right)$, we first evaluate all terms corresponding to the marginals $F_{v}$ and the pair copulas $C_{v, w \mid \mathrm{pa}(v ; w)}$ for $v$ smaller than $v^{*}$ by the well-ordering of $\mathcal{D}$ and $w<_{v} w^{*}$ if $w^{*} \in \mathrm{pa}(v)$, before evaluating the terms corresponding to $F_{v^{*}}$ and $C_{v^{*}, w^{*} \mid \mathrm{pa}\left(v^{*} ; w^{*}\right)}$.

Example (continued). For the DAG $\mathcal{D}$ in Figure 4, we sketch how to apply Algorithm 2 to obtain a pair-copula decomposition for $F_{3 \mid 56}$. Note that $\mathcal{D}$ contains the edges $3 \rightarrow 5$ and $3 \rightarrow 6$, which is why neither 5 nor 6 can be removed from the conditioning set. We get $F_{3 \mid 56}=\int_{-\infty} \frac{f_{356}}{f_{56}} \mathrm{~d} x_{3}$. Applying our previous results for $f_{356}$ and $f_{56}$, respectively, we further have

$$
F_{3 \mid 56}=\frac{\int_{\mathbb{R}} f_{6} h_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{64 \mid 5}\left(F_{6 \mid 5}, F_{4 \mid 5}\right) c_{65}\left(F_{6}, F_{5}\right) f_{5} c_{54}\left(F_{5}, F_{4}\right) f_{4} \mathrm{~d} x_{4}}{f_{6} c_{65}\left(F_{6}, F_{5}\right) f_{5}}
$$

see Equation (4.8). Thus, by cancelling common factors, we finally obtain

$$
F_{3 \mid 56}=\int_{\mathbb{R}} h_{63 \mid 54}\left(F_{6 \mid 54}, F_{3 \mid 54}\right) c_{64 \mid 5}\left(F_{6 \mid 5}, F_{4 \mid 5}\right) c_{54}\left(F_{5}, F_{4}\right) f_{4} \mathrm{~d} x_{4}
$$

### 4.2. Simulation, ML estimation, and model selection in PCBNs

Given (conditional) pair copulas $C_{v, w \mid \mathrm{pa}(v ; w)}\left(\cdot, \cdot ; \boldsymbol{\theta}_{v, w \mid \mathrm{pa}(v ; w)}\right), v \in V, w \in \mathrm{pa}(v)$, with joint parameter vector $\boldsymbol{\theta}:=\left(\boldsymbol{\theta}_{v, w \mid \mathrm{pa}(v ; w)}\right)_{v \in V, w \in \mathrm{pa}(v)} \in \boldsymbol{\Theta}$, above construction yields a $d$-variate copula model, which we will denote by $\left\{C_{\mathcal{D}, \mathcal{O}, \boldsymbol{\theta}} \mid \boldsymbol{\theta} \in \boldsymbol{\Theta}\right\}$. Note that for computational convenience, we again make the simplifying assumption of constant conditional copulas described in Section 3.2. Together with families of univariate marginals, $\left\{C_{\mathcal{D}, \mathcal{O}, \boldsymbol{\theta}} \mid \boldsymbol{\theta} \in \boldsymbol{\Theta}\right\}$ constitutes a statistical model which merges the advantages of graphical Markov modelling with the distributional flexibility of the pair-copula approach. We will refer to such a model as a pair-copula Bayesian network (PCBN). We want to mention that PCBNs were first introduced in Kurowicka and Cooke (2005). The analyses therein were, however, restricted to pair-copula families with the property that zero rank correlation implies independence.

## Simulation

Write $V=\left\{v_{1}, \ldots, v_{d}\right\}$ according to the well-ordering of $\mathcal{D}$ and set $V_{-i}:=\left\{v_{1}, \ldots, v_{i-1}\right\}$ for all $i \in\{1, \ldots, d\}$. A sample $\boldsymbol{u}=\left(u_{v_{1}}, \ldots, u_{v_{d}}\right) \in[0,1]^{d}$ from a fully specified PCBN with uniform $[0,1]$ univariate margins is obtained by simulating $d$ independent uniform $[0,1]$ variables

$x_{1}, \ldots, x_{d}$ and applying the quantile transformations

$$
\begin{aligned}
u_{v_{1}} & :=x_{1} \\
u_{v_{2}} & :=F_{v_{2} \mid v_{1}}^{-1}\left(x_{2} \mid u_{v_{1}} ; \boldsymbol{\theta}\right) \\
u_{v_{3}} & :=F_{v_{3} \mid V_{-3}}^{-1}\left(x_{3} \mid \boldsymbol{u}_{V_{-3}} ; \boldsymbol{\theta}\right) \\
& \vdots \\
u_{v_{d}} & :=F_{v_{d} \mid V_{-d}}^{-1}\left(x_{d} \mid \boldsymbol{u}_{V_{-d}} ; \boldsymbol{\theta}\right)
\end{aligned}
$$

The order in which the components of $\boldsymbol{u}$ are generated is given by the well-ordering of $\mathcal{D}$. Solving transformation equation $i$ for $x_{i}$, we have by the local $\mathcal{D}$-Markov property in Equation (2.1)

$$
x_{i}=F_{v_{i} \mid V_{-i}}\left(u_{v_{i}} \mid \boldsymbol{u}_{V_{-i}} ; \boldsymbol{\theta}\right)=F_{v_{i} \mid \mathrm{pa}\left(v_{i}\right)}\left(u_{v_{i}} \mid \boldsymbol{u}_{\mathrm{pa}\left(v_{i}\right)} ; \boldsymbol{\theta}\right), \quad i \in\{1, \ldots, d\}
$$

Now assume that $\mathrm{pa}\left(v_{i}\right) \neq \emptyset$, and let $w$ denote the largest vertex in $\mathrm{pa}\left(v_{i}\right)$ by the parent ordering $<_{v_{i}}$. Then Equations (4.9) and (3.2) yield

$$
x_{i}=h_{\underline{v}_{i}, w \mid \mathrm{pa}\left(v_{i} ; w\right)}\left(F_{v_{i} \mid \mathrm{pa}\left(v_{i} ; w\right)}\left(u_{v_{i}} \mid \boldsymbol{u}_{\mathrm{pa}\left(v_{i} ; w\right)} ; \boldsymbol{\theta}\right), F_{w \mid \mathrm{pa}\left(v_{i} ; w\right)}\left(u_{w} \mid \boldsymbol{u}_{\mathrm{pa}\left(v_{i} ; w\right)} ; \boldsymbol{\theta}\right) ; \boldsymbol{\theta}\right)
$$

Since $u_{v_{i}}$ is only contained in the first h-function argument $F_{v_{i} \mid \mathrm{pa}\left(v_{i} ; w\right)}\left(u_{v_{i}} \mid \boldsymbol{u}_{\mathrm{pa}\left(v_{i} ; w\right)} ; \boldsymbol{\theta}\right)$ on the right hand side of Equation (4.10), we obtain by induction that the only inverse functions needed in the computation of $u_{v_{i}}$ are the inverse h-functions $h_{\underline{v}_{i}, w^{*} \mid \mathrm{pa}\left(v_{i}, w^{*}\right)}^{-1}, w^{*} \in \mathrm{pa}\left(v_{i}\right)$.

# ML estimation 

ML estimation for PCBNs was first considered in Bauer et al. (2012). Let $\boldsymbol{u}=\left(\boldsymbol{u}^{1}, \ldots, \boldsymbol{u}^{n}\right)$, $n \in \mathbb{N}$, be a realisation of a sample of i.i.d. observations $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ from a random variable $\boldsymbol{U}$ on $[0,1]^{d}$ with copula family $\left\{C_{\mathcal{D}, \mathcal{O}, \boldsymbol{\theta}} \mid \boldsymbol{\theta} \in \boldsymbol{\Theta}\right\}$ and uniform univariate margins. The restriction to uniform univariate margins is made along the same lines as in Section 3.2 for vine copula models. Equation (4.1) yields the log-likelihood function
$l(\boldsymbol{\theta} ; \boldsymbol{u})=\sum_{k=1}^{n} \sum_{v \in V} \sum_{w \in \mathrm{pa}(v)} \log c_{v, w \mid \mathrm{pa}(v ; w)}\left(F_{v \mid \mathrm{pa}(v ; w)}\left(u_{v}^{k} \mid \boldsymbol{u}_{\mathrm{pa}(v ; w)}^{k} ; \boldsymbol{\theta}\right), F_{w \mid \mathrm{pa}(v ; w)}\left(u_{w}^{k} \mid \boldsymbol{u}_{\mathrm{pa}(v ; w)}^{k} ; \boldsymbol{\theta}\right) ; \boldsymbol{\theta}\right)$.
ML estimation of the parameters in Equation (4.11) can be performed using a stepwise approach similar to the one discussed in Section 3.2 for vine copula models. The only difference to vine copula models is that we iterate over the vertices of $\mathcal{D}$ and their respective parents instead of over the trees of an R-vine. Hence again, in a first step, sequential ML estimates are computed and in a second step, using the sequential ML estimates as starting values, joint ML estimates $\widehat{\boldsymbol{\theta}}_{v, w \mid \mathrm{pa}(v ; w)}, v \in V, w \in \mathrm{pa}(v)$, are inferred.

# 5. Structure estimation in Bayesian networks using the PC algorithm 

## Model selection

Model selection for PCBNs involves estimation of the DAG $\mathcal{D}$, selection of the set $\mathcal{O}$ of parent orderings, and selection of the pair-copula families for $C_{v, w \mid \mathrm{pa}(v ; w)}, v \in V, w \in \mathrm{pa}(v)$. Estimation of $\mathcal{D}$ will be the subject of Section 5. Given $\mathcal{D}$ and $\mathcal{O}$, the selection of pair-copula families can be performed in a similar way as in Section 3.2 for vine copula models, again with the difference that the iteration is vertex-by-vertex and parent-by-parent instead of tree-by-tree.

For the selection of $\mathcal{O}$ we propose a greedy-type procedure inspired by the structure selection algorithm for vine copula models outlined in Section 3.2. Clearly, an ordering of the parents of a vertex $v \in V$ is only required if $\mathrm{pa}(v) \neq \emptyset$. We assume $\mathcal{D}$ is well-ordered. Let $v \in V$ and assume that $k:=\|\mathrm{pa}(v)\| \geq 1$. Moreover, let $i \in\{1, \ldots, k\}$ and assume that we have already selected the $i-1$ smallest parents of $v$, denoted by $w_{1}<_{v} \cdots<_{v} w_{i-1}$. This implies that we have already selected pair-copula families for $C_{v^{*}, w \mid \mathrm{pa}\left(v^{*} ; w\right)}, v^{*}$ smaller than $v$ by the well-ordering of $\mathcal{D}, w \in \mathrm{pa}\left(v^{*}\right)$, and $C_{v, w_{j} \mid \mathrm{pa}\left(v ; w_{j}\right)}, j<i$. Also, this implies that we have inferred corresponding ML parameter estimates, which we summarise in the vector $\widehat{\boldsymbol{\theta}}$. Let $W_{-i}:=\left\{w_{1}, \ldots, w_{i-1}\right\}$. The selection of $w_{i}$ is performed in three steps. First, we compute the pseudo-observations $F_{v \mid W_{-i}}\left(u_{v}^{k} \mid \boldsymbol{u}_{W_{-i}}^{k} ; \widehat{\boldsymbol{\theta}}\right)$ and $F_{w \mid W_{-i}}\left(u_{w}^{k} \mid \boldsymbol{u}_{W_{-i}}^{k} ; \widehat{\boldsymbol{\theta}}\right), k \in\{1, \ldots, n\}$, for all $w \in \mathrm{pa}(v) \backslash W_{-i}$. Note that for $i=1$, nothing needs to be done since all univariate marginals are uniform on $[0,1]$. Second, we assign a weight $\omega_{v, w}$ to every edge $w \rightarrow v, w \in \mathrm{pa}(v) \backslash W_{-i}$, based on the previously calculated pseudo-observations, and choose $w_{i}$ such that $w_{i} \rightarrow v$ has optimal edge weight. Suitable weights are, for instance, the absolute values of estimates of Kendall's $\tau$, or AIC or BIC values of selected pair-copula families with estimated parameters. Last, we select a pair-copula family for $C_{v, w_{i} \mid \mathrm{pa}\left(v ; w_{i}\right)}$ and compute an ML estimate of the corresponding parameter(s). Again, this last step may have already been performed when computing the edge weights $\omega_{v, w}$.

## 5. Structure estimation in Bayesian networks using the PC algorithm

The first task of modelling the joint distribution of a given set of variables with a Bayesian network is to identify the DAG $\mathcal{D}=(V, E)$ specifying the Markov structure of the variables. A convenient approach to defining $\mathcal{D}$ is the use of expert knowledge. However, the scope of this approach is rather limited since expert knowledge is often incomplete or unavailable. Datadriven structure estimation algorithms provide a computer-based alternative to elicited expert knowledge. Robinson (1973) has shown that the number $n_{d}$ of DAGs on $d:=|V|$ labelled vertices is given by the recurrence equation

$$
n_{0}=1, \quad n_{d}=\sum_{k=1}^{d}(-1)^{k-1}\binom{d}{k} 2^{k(d-k)} n_{d-k}
$$

# 5.1. The PC algorithm 

Since $n_{d}$ grows super-exponentially in $d$, a systematic trial of all possible DAGs on $V$ is infeasible, and thus efficient searching algorithms are required. A considerable number of structure estimation algorithms has been proposed over the last two decades, see Neapolitan (2003, Chapters $8-11)$ and Koller and Friedman (2009, Chapter 18) for an overview. The majority of these algorithms follow one of the two estimation approaches predominant in the literature: the constraint-based and the score-and-search-based approach. In the constraint-based approach, $\mathcal{D}$ is inferred from a series of conditional independence tests. In the score-and-search-based approach, $\mathcal{D}$ is found by optimising a given scoring function-like AIC or BIC-over a suitable search space, for instance the space of all DAGs or the space of all Markov-equivalence classes. Besides, there exist hybrid algorithms which combine both approaches. Unfortunately, available implementations of aforementioned algorithms are mainly confined to discrete or Gaussian models and are hence not suited for our non-Gaussian continuous Bayesian networks.

### 5.1. The PC algorithm

We will provide a structure estimation algorithm that is particularly suited to finding the DAG $\mathcal{D}=(V, E)$ underlying a non-Gaussian continuous Bayesian network. Our algorithm is a version of one of the most popular constraint-based estimation algorithms, the PC algorithm (named after its inventors Peter Spirtes and Clark Glymour), see Spirtes and Glymour (1991) and Spirtes et al. (2000, Section 5.4.2). To fix notation and for the reader's convenience, we will now recall the PC algorithm. Let $P$ be an absolutely continuous $\mathcal{D}$-Markovian probability measure on $[0,1]^{d}$ with uniform univariate margins. The restriction to uniform univariate margins is made along the same lines as in Section 4.2. Moreover, let $\boldsymbol{u}=\left(\boldsymbol{u}^{1}, \ldots, \boldsymbol{u}^{n}\right), n \in \mathbb{N}$, be a realisation of a sample of i.i.d. observations $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ from a random variable $\boldsymbol{U}$ distributed as $P$. The PC algorithm for estimating $\mathcal{D}$ from $\boldsymbol{u}$ involves three major steps in which the complete UG $\mathcal{G}$ on $V$ is gradually transformed into a CG $\mathcal{G}^{*}$ on $V$, which is supposed to be the essential graph $\mathcal{D}^{e}$ corresponding to the Markov-equivalence class $[\mathcal{D}]$ of $\mathcal{D}$. The resulting CG $\mathcal{G}^{*}$ can then be extended to a DAG as outlined in Section 2.

In the first step of the PC algorithm, a series of tests for conditional independence is performed on $\boldsymbol{u}$. More precisely, for all distinct vertices $i, j \in V$ and chosen vertex sets $K \subseteq V \backslash\{i, j\}$, the null hypothesis $\mathrm{H}_{0}: U_{i} \Perp U_{j} \mid \boldsymbol{U}_{K}$ is tested against the general alternative $\mathrm{H}_{1}: U_{i} \Perp U_{j} \mid \boldsymbol{U}_{K}$ of conditional dependence. Given a suitable independence test of choice, we denote the test decision at significance level $\alpha \in(0,1)$ by $T_{\alpha}\left(\boldsymbol{u}_{i}, \boldsymbol{u}_{j} ; \boldsymbol{u}_{K}\right) \in\left\{\mathrm{H}_{0}, \mathrm{H}_{1}\right\}$. We will later introduce a novel class of conditional independence tests that is particularly tailored to the algorithm and applicable to non-Gaussian continuous data. If $T_{\alpha}\left(\boldsymbol{u}_{i}, \boldsymbol{u}_{j} ; \boldsymbol{u}_{K}\right)=\mathrm{H}_{0}$, the edge $i-j$ is removed from $\mathcal{G}$ and the conditioning set $K$ is stored in two variables $S_{i j}$ and $S_{j i}$ for later use. As a result of the first step, $\mathcal{G}$ is turned into the skeleton of $\mathcal{G}^{*}$. Step one is given in Algorithm 3.

# 5.1. The PC algorithm 

```
Algorithm 3 PC algorithm: finding the skeleton.
Input Data set \(\boldsymbol{u} ;\) significance level \(\alpha \in(0,1)\); conditional independence test with test decision
    \(T_{\alpha}\left(\boldsymbol{u}_{i}, \boldsymbol{u}_{j} ; \boldsymbol{u}_{K}\right)\) for the null hypothesis \(\mathrm{H}_{0}: U_{i} \Perp U_{j} \mid \boldsymbol{U}_{K}, i \neq j \in V, K \subseteq V \backslash\{i, j\}\).
Output Skeleton \(\mathcal{G}=\left(V, E_{\mathcal{G}}\right)\); separation sets \(S_{i j}, i \neq j \in V,(i, j) \notin E_{\mathcal{G}},(j, i) \notin E_{\mathcal{G}}\).
    \(\mathcal{G} \leftarrow\) complete UG on \(V\);
    \(k \leftarrow 0\);
repeat
    for \(i \in V\) and \(j \in \operatorname{ad}(i)\) do \(\% i\) and \(j\) are adjacent in \(\mathcal{G}\)
        if \(T_{\alpha}\left(\boldsymbol{u}_{i}, \boldsymbol{u}_{j} ; \boldsymbol{u}_{K}\right)=\mathrm{H}_{0}\) for any \(K \subseteq \operatorname{ad}(i) \backslash\{j\}\) with \(\left|K^{\prime}\right|=k\) then
            delete \(i-j\) from \(\mathcal{G}\);
            \(S_{i j} \leftarrow K\);
            \(S_{j i} \leftarrow K\)
        end if
    end for
    \(k \leftarrow k+1\).
until \(\left|\operatorname{ad}(i)\right| \leq k\) for all \(i \in V\).
```

In the second step, $\mathcal{G}$ is transformed into a CG by introducing a v-structure $i \rightarrow k \leftarrow j$ whenever $i$ and $j$ are non-adjacent, $k \in \operatorname{ad}(i) \cap \operatorname{ad}(j)$, and $k \notin S_{i j}$. In the last step, $\mathcal{G}$ is transformed into $\mathcal{G}^{*}$ by directing further edges of $\mathcal{G}$ to prevent new v-structures and directed cycles, until no more edges need direction. Steps two and three are given in Algorithm 4, where the third step was taken from Pearl (2009, Section 2.5). If $P$ is faithful to $\mathcal{D}$ and if all statistical test decisions made in Algorithm 3 are correct, then Algorithm 4 will return the correct graph $\mathcal{D}^{c}$, see Meek (1995). Due to the finite sample size or the existence of hidden variables, the application of Algorithm 3 to empirical data may sometimes, however, lead to conflicting information about edge directions. That is, it may be possible in a given situation that Algorithm 4, while introducing v-structures, first orients an undirected edge $i-j$ into $i \rightarrow j$, and later tries to introduce $i \leftarrow j$. In such a situation, we keep $i \rightarrow j$ and skip the new v-structure including $i \leftarrow j$. We can test whether the resulting CG can still be extended to a DAG without introducing new v-structures or directed cycles using the algorithm by Dor and Tarsi (1992). The PC algorithm can also be adapted to incorporate existing expert knowledge, see Meek (1995) and Moole and Valtorta (2004). We will henceforth assume that $P$ is faithful to $\mathcal{D}$ and that there are no hidden variables.

## Testing conditional independence using partial correlations

The centrepiece of the PC algorithm-as of any constraint-based estimation algorithm-is the test for conditional independence. In a Gaussian framework, the test of choice is usually a test for zero partial correlation $\rho_{i j \cdot K}$, see, for instance, Anderson (2003, Section 4.3). The null hypothesis then translates into $\mathrm{H}_{0}: \rho_{i j \cdot K}\left(X_{i}, X_{j} ; X_{K}\right)=0$, where $X_{k}:=\Phi^{-1}\left(U_{k}\right)$ for all $k \in V$, and $\Phi$ denotes the univariate standard normal cdf. Here, the quantile function $\Phi^{-1}$ is applied to $U$ in order to transform the uniform univariate copula margins to standard normal margins.

# 5.2. Testing conditional independence using vine copulas and the Rosenblatt transform 

```
Algorithm 4 PC algorithm: introducing edge directions
Input Skeleton \(\mathcal{G}=\left(V, E_{\mathcal{G}}\right)\); separation sets \(S_{i j}, i \neq j \in V,(i, j) \notin E_{\mathcal{G}},(j, i) \notin E_{\mathcal{G}}\).
Output Chain graph \(\mathcal{G}\).
    \% Introduce v-structures:
    for \(i \in V\) and \(j \notin \operatorname{ad}(i)\) and \(k \in \operatorname{ad}(i) \cap \operatorname{ad}(j)\) do
        if \(k \notin S_{i j}\) then
            replace \(i-k-j\) by \(i \rightarrow k \leftarrow j\) in \(\mathcal{G}\);
        end if
    end for
    \% Orient as many undirected edges as possible by repeated application of the following rules:
    repeat
        R1 orient \(j-k\) into \(j \rightarrow k\) whenever \(\mathcal{G}\) contains \(i \rightarrow j\) and \(k \notin \operatorname{ad}(i)\);
        R2 orient \(i-j\) into \(i \rightarrow j\) whenever \(\mathcal{G}\) contains \(i \rightarrow k \rightarrow j\);
        R3 orient \(i-j\) into \(i \rightarrow j\) whenever \(\mathcal{G}\) contains \(i-k \rightarrow j\) and \(i-l \rightarrow j\), and \(l \notin \operatorname{ad}(k)\);
    until no more edges can be directed;
```

The conditional independence test is based on the asymptotic normality

$$
\sqrt{d-|K|-3} \widehat{z}_{n} \xrightarrow[n \rightarrow \infty]{c} \mathrm{~N}(0,1), \quad \widehat{z}_{n}:=\frac{1}{2} \log \left(\frac{1+\widehat{\rho}_{i j \cdot K}\left(\boldsymbol{X}_{i}^{n}, \boldsymbol{X}_{j}^{n} ; \boldsymbol{X}_{K}^{n}\right)}{1-\widehat{\rho}_{i j \cdot K}\left(\boldsymbol{X}_{i}^{n}, \boldsymbol{X}_{j}^{n} ; \boldsymbol{X}_{K}^{n}\right)}\right)
$$

of the Fisher's $z$-transformed partial-correlation estimator $\widehat{\rho}_{i j \cdot K}$ under $\mathrm{H}_{0}$, see again Anderson (2003, Section 4.3). Here, $\xrightarrow{\mathcal{E}}$ denotes convergence in distribution, $\mathrm{N}(0,1)$ is the univariate standard normal distribution, and $\boldsymbol{X}_{k}^{n}:=\left(\Phi^{-1}\left(U_{k}^{1}\right), \ldots, \Phi^{-1}\left(U_{k}^{n}\right)\right)$ for all $k \in V$. Kalisch and Bühlmann (2007) have proven uniform convergence of the PC algorithm under joint normality and a mild sparsity assumption for the underlying DAG, cf. also Harris and Drton (2012). An implementation of the PC algorithm with above partial correlation test is available in the R package pcalg (Kalisch et al., 2012). The pcalg package also provides an interface for selfimplemented conditional independence tests.

### 5.2. Testing conditional independence using vine copulas and the Rosenblatt transform

Above test for zero partial correlation was derived under the assumption of joint normality. We will now introduce a copula-based alternative test for conditional independence that is also applicable to non-Gaussian continuous data. Assume $K \neq \emptyset$. Otherwise, the problem reduces to testing ordinary (unconditional) stochastic independence. Let $F_{i, j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ denote the conditional cdf of $U_{i}$ and $U_{j}$ given $\boldsymbol{U}_{K}=\boldsymbol{v}_{K}$, and let $C_{i, j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ be the corresponding conditional copula. Moreover, let $C_{\Perp}$ denote the independence copula on $[0,1]^{2}$. The conditional independence $U_{i} \Perp U_{j} \mid \boldsymbol{U}_{K}$ holds if and only if

$$
F_{i, j \mid K}\left(v_{i}, v_{j} \mid \boldsymbol{v}_{K}\right)=C_{i, j \mid K}\left(F_{i \mid K}\left(v_{i} \mid \boldsymbol{v}_{K}\right), F_{j \mid K}\left(v_{j} \mid \boldsymbol{v}_{K}\right) \mid \boldsymbol{v}_{K}\right)=F_{i \mid K}\left(v_{i} \mid \boldsymbol{v}_{K}\right) F_{j \mid K}\left(v_{j} \mid \boldsymbol{v}_{K}\right)
$$

# 5.2. Testing conditional independence using vine copulas and the Rosenblatt transform 

for all $v_{i}, v_{j} \in[0,1]$ and $P_{K}$-almost all $\boldsymbol{v}_{K} \in[0,1]^{|K|}$, where $\boldsymbol{U}_{K} \sim P_{K}$. Hence, the null hypothesis of the conditional independence test can be stated as $H_{0}: C_{i, j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)=C_{\perp}(\cdot, \cdot)$ for $P_{K}$-almost all $\boldsymbol{v}_{K} \in[0,1]^{|K|}$. Using the simplifying assumption that $C_{i, j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ depends on $\boldsymbol{v}_{K}$ only through $F_{i \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ and $F_{j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ discussed in Section 3.2, we drop $\boldsymbol{v}_{K}$ from $C_{i, j \mid K}\left(\cdot, \cdot \mid \boldsymbol{v}_{K}\right)$ and approximate $H_{0}$ by the more accessible null hypothesis $H_{0}^{*}: C_{i, j \mid K}(\cdot, \cdot)=$ $C_{\perp}(\cdot, \cdot)$. The new null hypothesis $H_{0}^{*}$ can be tested using any test for ordinary (unconditional) stochastic independence of two continuous random variables applied to the transformed observations $W_{i \mid K}^{1}, \ldots, W_{i \mid K}^{n}$ and $W_{j \mid K}^{1}, \ldots, W_{j \mid K}^{n}$, where

$$
W_{i \mid K}^{k}:=F_{i \mid K}\left(U_{i}^{k} \mid \boldsymbol{U}_{K}^{k}\right) \quad \text { and } \quad W_{j \mid K}^{k}:=F_{j \mid K}\left(U_{j}^{k} \mid \boldsymbol{U}_{K}^{k}\right)
$$

for all $k \in\{1, \ldots, n\}$. Song (2009) called Equation (5.1) the Rosenblatt transform after Rosenblatt (1952), while Bergsma (2011) called it the partial copula transform. Given a realisation $\boldsymbol{u}$ of $\left(\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}\right)$, the difficulty of this approach lies in the computation of the transformed realisations $\boldsymbol{w}_{i \mid K}$ and $\boldsymbol{w}_{j \mid K}$, where $w_{i \mid K}^{k}:=F_{i \mid K}\left(u_{i}^{k} \mid \boldsymbol{u}_{K}^{k}\right)$ and $w_{j \mid K}^{k}:=F_{j \mid K}\left(u_{j}^{k} \mid \boldsymbol{u}_{K}^{k}\right)$ for all $k \in\{1, \ldots, n\}$. Note that the conditional cdfs $F_{i \mid K}\left(\cdot \mid \boldsymbol{v}_{K}\right)$ and $F_{j \mid K}\left(\cdot \mid \boldsymbol{v}_{K}\right)$ are typically unknown and need to be estimated in the course of the testing procedure. Bergsma (2011) suggested the use of non-parametric kernel estimators for this task. By contrast, we propose a parametric estimation method that is based on vine copula models.

## Estimating conditional cdfs using vine copula models

Taking another look at vine copula models as described in Section 3.2, we observe that transformed realisations like $\boldsymbol{w}_{i \mid K}$ and $\boldsymbol{w}_{j \mid K}$ naturally emerge in the log-likelihood function. In fact, given any distinct $i, j \in V$ and $K \subseteq V \backslash\{i, j\}$, it is always possible to construct a regular vine $\mathcal{V}=\left(T_{1}, \ldots, T_{p}\right), p:=1+|K|$, in which tree $T_{1}$ has vertex set $V_{1}=\{i\} \cup\{j\} \cup K$ and tree $T_{p}$ is of the form $i, l \mid K_{-l} \stackrel{i, j \mid K}{ } j, m \mid K_{-m}$ for some $l, m \in K$. The corresponding loglikelihood function $l\left(\boldsymbol{\theta} ; \boldsymbol{u}_{\{i\} \cup\{j\} \cup K}\right), \boldsymbol{\theta} \in \Theta$, contains the pair-copula pdf $c_{i, j \mid K}$ with arguments $F_{i \mid K}\left(u_{i}^{k} \mid \boldsymbol{u}_{K}^{k} ; \boldsymbol{\theta}\right)$ and $F_{j \mid K}\left(u_{i}^{k} \mid \boldsymbol{u}_{K}^{k} ; \boldsymbol{\theta}\right)$ for all $k \in\{1, \ldots, n\}$. Thus, by computing an ML estimate $\widehat{\boldsymbol{\theta}}$ of $\boldsymbol{\theta}$ and subsequently evaluating $l$ at $\widehat{\boldsymbol{\theta}}$, we obtain estimates $\widehat{w}_{i \mid K}^{k}:=F_{i \mid K}\left(u_{i}^{k} \mid \boldsymbol{u}_{K}^{k} ; \widehat{\boldsymbol{\theta}}\right)$ and $\widehat{w}_{j \mid K}^{k}:=F_{j \mid K}\left(u_{j}^{k} \mid \boldsymbol{u}_{K}^{k} ; \widehat{\boldsymbol{\theta}}\right)$ of $w_{i \mid K}^{k}$ and $w_{j \mid K}^{k}$, respectively, as a welcome side effect.

We call a vertex $v$ in Tree $T_{q}, q \in\{1, \ldots, p-1\}$, an inner vertex if $|\operatorname{ad}(v)| \geq 2$. In order to construct such a vine $\mathcal{V}$, we have to follow one simple rule:
$\mathbf{R} \quad$ Neither $i$ nor $j$ may be part of an inner vertex in the trees $T_{1}, \ldots, T_{p-1}$ of $\mathcal{V}$.
Following $\mathbf{R}$, it is even possible to restrict the class of R -vines to C - or D -vines. The only inner vertices of a C -vine are the root vertices of the trees $T_{1}, \ldots, T_{p-1}$. Thus, in a C -vine obeying $\mathbf{R}$, $i$ and $j$ do not appear in the root vertices of the respective trees. Similarly, in a D-vine obeying

# 5.2. Testing conditional independence using vine copulas and the Rosenblatt transform 

$\mathbf{R}, i$ and $j$ only appear in the boundary vertices of trees $T_{1}, \ldots, T_{p-1}$. Figures 2 and 5 give an example of a C-, a D-, and an R-vine, respectively, having the same edge label in tree $T_{p}$.
![img-4.jpeg](img-4.jpeg)

Figure 5: A C- (left) and a D-vine (right) on five vertices having the same edge label 15|234 in tree $T_{4}$. A corresponding R-vine is given in Figure 2. The three vines were constructed according to rule $\mathbf{R}$ with $i=1$ and $j=5$. Boundaries of nodes including either 1 or 5 appear in bold.

The tree structure of $\mathcal{V}$ can be estimated from $\boldsymbol{u}_{\{i\} \cup\{j\} \cup K}$ by adapting the greedy search strategies described in Section 3.2 to the new constraint R. An optimal C-vine obeying $\mathbf{R}$ is found by restricting the sets of possible root vertices for trees $T_{1}, \ldots, T_{p-1}$ to vertices containing neither $i$ nor $j$, respectively. In order to find an optimal D-vine obeying $\mathbf{R}$, the unconstrained TSP usually solved has to be replaced by a constrained TSP with fixed source vertex $i$ and destination vertex $j$. Finally, an optimal R-vine obeying $\mathbf{R}$ is found by first estimating a smaller R-vine $\mathcal{V}_{K}$ with first tree vertices $K$. Having found $\mathcal{V}_{K}$, vertex $i$ is then connected to a vertex $l \in K$ in tree $T_{1}$ such that the new edge $i-l$ has optimal edge weight amongst all possible edges $i-m$ for $m \in K$. The same is done for vertex $j$. Note that this way, $j$ cannot be connected to $i$. The newly formed structure is then sequentially transformed into $\mathcal{V}$ by analogously extending the remaining trees $T_{2}, \ldots, T_{p}$, such that the proximity condition and $\mathbf{R}$ are always satisfied and the corresponding edge weights are optimised. Copula selection and ML estimation in the resulting vine copula model is then performed as usual, see Section 3.2.

## Vine-copula-based conditional independence tests

Summing up, we test the conditional independence $U_{i} \Perp U_{j} \mid \boldsymbol{U}_{K}$ in three steps. In the first step, we construct a vine $\mathcal{V}$ on the vertices $\{i\} \cup\{j\} \cup K$ by applying a modified version of one of the structure estimation algorithms described in Section 3.2 to $\boldsymbol{u}_{\{i\} \cup\{j\} \cup K}$. In the second step, we select corresponding pair-copula families, perform ML estimation in the resulting model, and evaluate the log-likelihood function $l$ at the estimated parameter vector $\widehat{\boldsymbol{\theta}}$ to obtain transformed realisations $\widehat{\boldsymbol{w}}_{i \mid K}:=\left(\tilde{w}_{i \mid K}^{k}\right)_{1 \leq k \leq n}$ and $\widehat{\boldsymbol{w}}_{j \mid K}:=\left(\tilde{w}_{j \mid K}^{k}\right)_{1 \leq k \leq n}$, respectively. In the last step, we apply a test for ordinary stochastic independence of two continuous random variables to $\widehat{\boldsymbol{w}}_{i \mid K}$

# 6. Simulation study 

and $\widehat{\boldsymbol{w}}_{j \mid K}$. Note that in the first iteration step of Algorithm 3, only unconditional independences, that is $K=\emptyset$, are tested, and thus the independence test of choice is directly applied to $\boldsymbol{u}$.

We will examine the performance of our novel testing procedure in a simulation study in Section 6 using three different tests for ordinary stochastic independence. Recycling notation, consider the null hypothesis $H_{0}: U_{i} \Perp U_{j}$ vs. $H_{1}: U_{i} \Perp U_{j}$. The first test used is a test for zero Kendall's $\tau$ with null hypothesis $H_{0}^{*}: \tau\left(U_{i}, U_{j}\right)=0$ vs. $H_{1}^{*}: \tau\left(U_{i}, U_{j}\right) \neq 0$. Under $H_{0}$, the Kendall's $\tau$ estimator $\widehat{\tau}_{n}$ exhibits the asymptotic normality

$$
\sqrt{\frac{9 n(n-1)}{2(2 n+5)}} \widehat{\tau}_{n}\left(\boldsymbol{U}_{i}, \boldsymbol{U}_{j}\right) \xrightarrow[n \rightarrow \infty]{ } \mathrm{N}(0,1)
$$

where $\boldsymbol{U}_{i}:=\left(U_{i}^{1}, \ldots, U_{i}^{n}\right)$ and $\boldsymbol{U}_{j}:=\left(U_{j}^{1}, \ldots, U_{j}^{n}\right)$, see Hollander and Wolfe (1999, Section 8.1). In general, $\tau\left(U_{i}, U_{j}\right)=0$ does not imply $U_{i} \Perp U_{j}$. However, for many popular copula families like the Clayton, the Gaussian, and the Gumbel copula families, $H_{0}$ and $H_{0}^{*}$ are equivalent. The family of Student's t copulas serves as a counterexample. We then consider $H_{0}^{*}$ an approximation for $H_{0}$. The other two independence tests used in Section 6 are of Cramér-von Mises type. More precisely, independence test number two is the test for zero Hoeffding's $D$ proposed by Hoeffding (1948). P-values of the sample test statistic $\widetilde{D}_{n}$ are computed using the asymptotically equivalent sample test statistic $\widetilde{B}_{n}$ by Blum et al. (1961), see also Hollander and Wolfe (1999, Section 8.6). Independence test number three is the test by Genest and Rémillard (2004) based on the empirical copula process.

## 6. Simulation study

We conducted an extensive simulation study to examine the small sample performance of the PC algorithm in finding the true Markov structure underlying a PCBN. To this end, we drew samples from various PCBNs based on the conditional independence properties represented by the DAG $\mathcal{D}=(V, E)$ in Figure 1. These PCBNs emerged from various choices of paircopula families for $C_{12}, C_{13}, C_{24}$, and $C_{34 \mid 2}$, cf. Section 4. More precisely, we chose from the Clayton, Gumbel, Gaussian, and Student's t pair-copula families. These copula families exhibit considerable differences in their dependence structures and tail behaviours, see the simulation study in Bauer et al. (2012) for an overview. We considered four PCBNs with all four pair copulas $C_{12}, C_{13}, C_{24}$, and $C_{34 \mid 2}$ coming from the same copula family, respectively. Additionally, we considered 24 PCBNs with each pair copula $C_{12}, C_{13}, C_{24}$, and $C_{34 \mid 2}$ coming from a different copula family. Our choices of pair-copula families are given in Table 2. For each choice of paircopula families we then considered 16 different parameter configurations arising from a selection of two different parameter values for each pair copula. The parameter values for each pair copula were chosen to correspond to values of Kendall's $\tau$ of 0.25 and 0.75 , that is one low and one high

# 6. Simulation study 

rank-correlation specification. These Kendall's $\tau$ configurations are summarised in Table 3.


Table 2: Selected pair-copula families for $C_{12}, C_{13}, C_{24}, C_{34 \mid 2}$. Copulas were chosen from the Clayton (C), Gumbel (G), Gaussian (N), and Student's t (t) pair-copula families. See Tables 3 and 4 for further details on the pair-copula families used.


Table 3: Selected values of Kendall's $\tau$ for each choice of pair-copula families for $C_{12}, C_{13}, C_{24}$, $C_{34 \mid 2}$. See Tables 2 and 4 for further details on the pair-copula families used.

Our selection of copula parameters is based on the bijective relationship between the parameters of the Clayton, Gumbel, and Gaussian pair-copula families and the corresponding Kendall's $\tau$. For the Student's t copula, such a bijective relationship exists only between the correlation parameter and Kendall's $\tau$, which is why we set the degrees-of-freedom parameter of each Student's t copula to $\nu=5$ in order to allow for heavy-tailed dependence. Table 4 summarises the parameters $\theta$, the corresponding Kendall's correlation coefficients $\tau(\theta)$, and the respective taildependence coefficients $\lambda_{\mathrm{L}}(\theta)=\lim _{u \rightarrow 0} \frac{C_{\theta}(u, u)}{u}$ and $\lambda_{\mathrm{U}}(\theta)=\lim _{u \rightarrow 1} \frac{1-2 u+C_{\theta}(u, u)}{1-u}$ for each pair copula $C_{\theta}, \theta \in \Theta$, used in the simulation study.

Summing up, we have 28 different PCBNs with 16 different parameter configurations each, that is 448 simulation scenarios. In each of the 448 simulation scenarios we performed $N=100$ simulation runs, and in each simulation run we generated $n=1,000$ i.i.d. observations. The sampling procedure used was described in Section 4.2.

For each of the 44,800 runs we applied the PC algorithm with the ten different conditional independence tests described in Section 5. Those were the widely used test for zero partial

# 6. Simulation study 


Table 4: Parameters, Kendall's correlation coefficients, and tail-dependence coefficients (TDCs) of the pair copulas used in the simulation study.
correlation (COR) and our novel vine-copula-based tests using either only C-vines (C), or only D-vines (D), or more generally R-vines (R), respectively, together with one of the Kendall's $\tau(\mathrm{K})$, Hoeffding's $D(\mathrm{H})$, or Genest and Rémillard (GR) tests for ordinary stochastic independence. Since zero partial correlation is generally a weaker property than conditional independence, we consider COR only an approximate conditional independence test serving as a benchmark. In a Gaussian framework, however, zero partial correlation is equivalent to conditional independence. This equivalence holds in particular in the scenarios featuring only Gaussian pair copulas, in which case the respective joint copula families are also Gaussian. The corresponding correlation matrices were derived in Bauer et al. (2012). Each test was performed at the $5 \%$ significance level.

## Results

Let $\mathcal{G}_{f, p, r, t}$ denote the CG obtained from applying the PC algorithm with conditional-independence test $t \in\{\mathrm{COR}, \mathrm{C}-\mathrm{GR}, \mathrm{C}-\mathrm{H}, \mathrm{C}-\mathrm{K}, \mathrm{D}-\mathrm{GR}, \mathrm{D}-\mathrm{H}, \mathrm{D}-\mathrm{K}, \mathrm{R}-\mathrm{GR}, \mathrm{R}-\mathrm{H}, \mathrm{R}-\mathrm{K}\}$ to the data simulated in run $r \in\{1, \ldots, 100\}$ of pair-copula scenario $f \in\{1, \ldots, 28\}$ (see Table 2) and parameter configuration $p \in\{1, \ldots, 16\}$ (see Tables 3 and 4 ). We compared each CG $\mathcal{G}_{f, p, r, t}$ to the true essential graph $\mathcal{D}^{e}$ in Figure 1, and set $\pi_{f, p, r, t}:=1$ if $\mathcal{G}_{f, p, r, t}$ equalled $\mathcal{D}^{e}$ and $\pi_{f, p, r, t}:=0$ otherwise. For each pair-copula scenario $f$ and each conditional independence test $t$, we then computed the relative frequency of recovering the correct structure over all parameter configurations $p$ and all runs $r$, which we will denote by $\pi_{f, t}:=\frac{1}{1600} \sum_{p=1}^{16} \sum_{r=1}^{100} \pi_{f, p, r, t}$. Moreover, we determined the structural Hamming distance (SHD) (Tsamardinos et al., 2006) $\delta_{f, p, r, t}$ between each CG $\mathcal{G}_{f, p, r, t}$ and $\mathcal{D}^{e}$. In short, $\delta_{f, p, r, t}$ counts the number of edges that need to be added to, removed from, directed in, or flipped in $\mathcal{G}_{f, p, r, t}$ in order to obtain $\mathcal{D}^{e}$. Hence, $\delta_{f, p, r, t}$ takes a value between zero and $\left(\frac{|V|}{2}\right)=6$. We again took the average over all parameter configurations $p$ and all runs $r$, yielding the mean SHD $\delta_{f, t}:=\frac{1}{1600} \sum_{p=1}^{16} \sum_{r=1}^{100} \delta_{f, p, r, t}$ for each pair-copula scenario $f$ and each conditional independence test $t$. The results are given in Figures 6 and 7, respectively.

Let us first consider Figure 6. The relative frequencies $\pi_{f, \mathrm{COR}}$ range between $14 \%$ and $63 \%$, whereas for the vine-copula-based tests, $\pi_{f, t}$ ranges between $40 \%$ and $64 \%$. COR was outperformed by at least one vine-copula-based test in 18, and by all vine-copula-based tests in 15 out of the 28 copula scenarios. The lowest frequency of $14 \%$ was obtained when applying the PC

# 6. Simulation study 

![img-5.jpeg](img-5.jpeg)

Figure 6: Percentage $\pi_{f, t}$ of runs in which the PC algorithm returned the correct Markov structure for each choice $f$ of pair-copula families for $C_{12}, C_{13}, C_{24}, C_{34 \mid 2}$ (legends) and each conditional independence test $t$ (horizontal axes) (1600 runs each). Copulas were chosen from the Clayton (C), Gumbel (G), Gaussian (N), and Student's t (t) paircopula families. The percentage of correct recoveries out of all 28 copula scenarios is given in solid grey.
algorithm with COR to the data sets generated in copula scenario 1 (numbering as in Table 2), which features only Clayton, that is non-elliptical, copulas. By contrast, COR showed a solid performance in the elliptical-copulas-only scenarios 3 and 4 , which is not surprising given that COR is based on the partial correlation. In 9 out of the 28 copula scenarios, $\pi_{f, \mathrm{COR}}$ is lower

# 6. Simulation study 

![img-6.jpeg](img-6.jpeg)

Figure 7: Average structural Hamming distance (SHD) $\delta_{f, t}$ between the true essential graph $\mathcal{D}^{e}$ and the chain graph $\mathcal{G}_{f, p, r, t}$ returned by the PC algorithm for each choice $f$ of paircopula families for $C_{12}, C_{13}, C_{24}, C_{34 \mid 2}$ (legends) and each conditional independence test $t$ (horizontal axes) ( 1600 runs each). Copulas were chosen from the Clayton (C), Gumbel (G), Gaussian (N), and Student's t (t) pair-copula families. The average SHD over all 28 copula scenarios is given in solid grey.
than $40 \%$, which is the minimum frequency obtained for the vine-copula-based tests. Also, in these 9 scenarios, the difference in relative frequencies between COR and the vine-copula-based tests ranges between 9 and 33 percentage points. The highest frequency of $64 \%$ was obtained in copula scenario 15 both for the PC algorithm with C-GR and C-H, respectively. Taking means

# 6. Simulation study 

over all 28 copula scenarios, we obtain the overall relative frequencies $\pi_{t}:=\frac{1}{28} \sum_{f=1}^{28} \pi_{f, t}$ for all tests $t$. These overall frequencies range between $50 \%$ and $53 \%$ for the vine-copula-based tests, while $\pi_{\mathrm{COR}}=45 \%$. The best performances were again achieved by C-GR and C-H. However, we recommend using the R-vine-based conditional independence tests in higher dimensions since these offer more general tree structures than their C- and D-vine counterparts. Moreover, we observe that choosing H instead of GR as test for unconditional stochastic independence has only little effect on the performance of the vine-copula-based tests. By contrast, relative frequencies were, on average, slightly worse when using K instead of GR and H , respectively. Since zero Kendall's $\tau$ is generally also not equivalent to stochastic independence, we recommend using GR and H. Note that in a given copula scenario $f$ and a given parameter scenario $p$, the relative frequencies $\pi_{f, p, t}:=\frac{1}{100} \sum_{r=1}^{100} \pi_{f, p, r, t}$ can be a lot higher than the averages displayed in Figure 6. We observed frequencies $\pi_{f, p, t}$ of up to $98 \%$. To sum up, using a vine-copula-based conditional independence test instead of COR leads to more reliable structure estimates, in particular when the data exhibit non-Gaussian, asymmetric dependence.

Considering only the correctly recovered Markov structures may be a too crude performance measure. Hence, the mean SHDs $\delta_{f, t}$ in Figure 7 illustrate how much the results of the PC algorithm differ from the true essential graph $\mathcal{D}^{e}$. For the vine-copula-based tests, $\delta_{f, t}$ ranges between 0.62 and 1.03. The respective overall means $\delta_{t}:=\frac{1}{28} \sum_{f=1}^{28} \delta_{f, t}$ lie between 0.79 and 0.84 . Thus, on average, the results of the PC algorithm differ by less than one edge from $\mathcal{D}^{e}$. That is, if the PC algorithm yields a CG that is not equivalent to $\mathcal{D}^{e}$, then, with a high probability, CG and $\mathcal{D}^{e}$ are not too different. The lowest values of $\delta_{t}$ were again obtained for C-GR and C-H. Similarly, $\delta_{f, \mathrm{COR}}$ ranges between 0.63 and 2.44 , and $\delta_{\mathrm{COR}}=0.98$, which again shows the superiority of the vine copula approach. The worst mean SHD of 2.44 was obtained in copula scenario 1. Overall, we can say that the PC algorithm with either of the 9 vine-copula-based conditional independence tests provides a suitable procedure for structure estimation in PCBNs.

We repeated the simulation study both for a significance level $\alpha$ of $1 \%$ and for a sample size $n$ of 500 . For $\alpha=1 \%$, we obtained results similar to the ones described above for $\alpha=5 \%$. The overall relative frequencies $\pi_{t}$ were slightly lower, ranging from $44 \%$ to $47 \%$ for the vine-copulabased tests, while $\pi_{\mathrm{COR}}$ was $43 \%$. Also, the overall mean SHDs $\delta_{t}$ ranged between 0.86 and 0.94 for the vine-copula-based tests, while $\pi_{\mathrm{COR}}$ was 0.99 . The reduction in sample size to $n=500$, on the other hand, lead to a slightly stronger decrease in the overall relative frequencies $\pi_{t}$, which then ranged between $39 \%$ and $41 \%$ for the vine-copula-based tests, while $\pi_{\mathrm{COR}}$ was $37 \%$. Similarly, the overall mean SHDs $\delta_{t}$ ranged between 1.07 and 1.11 for the vine-copula-based tests, while $\pi_{\mathrm{COR}}$ was 1.17. Yet, both for $\alpha=1 \%$ and for $n=500$, the CGs returned by the PC algorithm differed on average from $\mathcal{D}^{e}$ by only one edge. The performance of the PC algorithm can thus be deemed reliable and robust.

# 7. Application: Stock market indices 

As a real-world application, we applied PCBNs to a financial data set comprising ten major international stock market indices. More precisely, we modelled the joint distribution of a portfolio of daily log-returns of the Australian All Ordinaries (AUS), the Canadian S\&P/TSX Composite Index (CAN), the Swiss Market Index (CH), the German DAX (DEU), the French CAC 40 (FRA), the Hong Kong Hang Seng Index (HK), the Japanese Nikkei 225 (JPN), the Singapore Straits Times Index (SGP), the UK's FTSE 100 (UK), and the US S\&P 500 (USA) from 1 April 2008 to 29 July 2011 ( $n=733$ observations).

## Univariate time series models

Using the inference functions for margins method outlined in Section 3.2, we modelled univariate marginal distributions without regard to the dependence structure between variables. We first removed serial correlation in the ten time series of log-returns by applying an $\operatorname{AR}(1)-\operatorname{GARCH}(1,1)$ filter, which accounts for conditional heteroskedasticity present in the data, see Bollerslev (1986). The log-return $r_{i, t}$ of stock index $i \in\{\mathrm{AUS}, \mathrm{CAN}, \mathrm{CH}, \mathrm{DEU}, \mathrm{FRA}, \mathrm{HK}, \mathrm{JPN}, \mathrm{SGP}, \mathrm{UK}, \mathrm{USA}\}$ at time $t$ can thus be written as

$$
r_{i, t}=\mu_{i}+a_{i} r_{i, t-1}+\varepsilon_{i, t}, \quad \varepsilon_{i, t}=\sigma_{i, t} z_{i, t}, \quad \sigma_{i, t}^{2}=\omega_{i}+\alpha_{i} \varepsilon_{i, t-1}^{2}+\beta_{i} \sigma_{i, t-1}^{2}
$$

with parameters $\omega_{i}>0, \alpha_{i}, \beta_{i} \geq 0$ such that $\alpha_{i}+\beta_{i}<1,\left|a_{i}\right|<1$, and $\mu_{i} \in \mathbb{R}$, where $\mathbb{E}\left[z_{t, i}\right]=0$ and $\operatorname{Var}\left[z_{t, i}\right]=1$. The standardised residuals $z_{i, t}$ are assumed to follow a skewed Student's t distribution with $\nu_{i}$ degrees of freedom and skewness parameter $\gamma_{i}$, see McNeil et al. (2005, Section 3.2). The corresponding cdf will be denoted by $\mathrm{t}_{\nu_{i}, \gamma_{i}}$. ML parameter estimates and corresponding standard errors derived from numerical evaluation of the Hessian of the AR(1)$G A R C H(1,1)$ parameters are given in Appendix A. We assessed model fit using the following statistical tests: the Ljung-Box test (Ljung and Box, 1978) with null hypothesis that there is no autocorrelation left in the residuals and squared residuals, the Langrange-multiplier ARCH test (Engle, 1982) with null hypothesis that the residuals exhibit no conditional heteroskedasticity, and the Kolmogorov-Smirnov test (Conover, 1999, Section 6.2) with null hypothesis that the residuals follow a skewed Student's t distribution. None of these null hypotheses could be rejected at the $5 \%$ significance level. We then transformed the standardised residuals to uniformly distributed observations $u_{i, t}:=\mathrm{t}_{\nu_{i}, \gamma_{i}}\left(\sqrt{\frac{\nu_{i}}{\nu_{i}-2}+\frac{2 \nu_{i}^{2} \gamma_{i}^{2}}{\left(\nu_{i}-2\right)^{2}\left(\nu_{i}-4\right)} z_{i, t}}\right)$, before modelling the joint dependence structure of the ten time series of log-returns by a PCBN.

## Estimating the conditional independence structure with the PC algorithm

We estimated the conditional independence structure of the ten time series of log-returns by applying the PC algorithm with either of the ten conditional independence tests COR, C-GR,

# 7. Application: Stock market indices 

C-H, C-K, D-GR, D-H, D-K, R-GR, R-H, and R-K described in Section 5 (with notation as in Section 6) to the transformed observations $u_{i, t}$. All tests were performed at the $5 \%$ significance level. As a result, we obtained three different essential graphs $\mathcal{D}_{\mathrm{COR}}^{e}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}^{e}$, and $\mathcal{D}_{\mathrm{K}}^{e}$, of which the first was returned by the PC algorithm with COR, the second was returned by the PC algorithm with either of C-GR, C-H, D-GR, D-H, R-GR, and R-H, and the third was returned by the PC algorithm with either of C-K, D-K, and R-K, respectively. Obviously, a restriction of the class of R-vines to C- or D-vines had not influence on the resulting essential graph. We then oriented undirected edges in the obtained essential graphs, as described in Section 2, in order to obtain DAGs $\mathcal{D}_{\mathrm{COR}}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}$, and $\mathcal{D}_{\mathrm{K}}$ from the Markov-equivalence classes represented by $\mathcal{D}_{\mathrm{COR}}^{e}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}^{e}$, and $\mathcal{D}_{\mathrm{K}}^{e}$, respectively. More precisely, $\mathcal{D}_{\mathrm{COR}}^{e}$ contained the two undirected edges AUS - HK and CH - DEU, which we replaced by AUS $\rightarrow \mathrm{HK}$ and $\mathrm{CH} \rightarrow \mathrm{DEU}$, respectively, based on the heuristic rule that $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}^{e}$ and $\mathcal{D}_{\mathrm{K}}^{e}$ already contained AUS $\rightarrow \mathrm{HK}$ and $\mathrm{CH} \rightarrow \mathrm{DEU}$. Similarly, we oriented AUS - JPN into AUS $\leftarrow$ JPN in $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}$ and $\mathcal{D}_{\mathrm{K}}$ since $\mathcal{D}_{\mathrm{COR}}^{e}$ already contained AUS $\leftarrow$ JPN. The DAGs $\mathcal{D}_{\mathrm{COR}}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}$, and $\mathcal{D}_{\mathrm{K}}$ are given in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8: DAGs $\mathcal{D}_{\text {COR }}$ (top left), $\mathcal{D}_{\text {GR,H }}$ (top right), $\mathcal{D}_{\mathrm{K}}$ (bottom) returned by the PC algorithm with different conditional independence tests when estimating the Markov structure of the ten time series AUS, CAN, CH, DEU, FRA, HK, JPN, SGP, UK, USA of daily log-returns. Solid edges appear in all three DAGs. Edge labels indicate parent orderings, that is, for instance, CAN $<_{\text {USA }} \mathrm{DEU}<_{\text {USA }} \mathrm{FRA}$ in $\mathcal{D}_{\text {COR }}$.

In all three DAGs in Figure 8, the Asian-Pacific indices AUS, HK, JPN, and SGP are mutually adjacent, and so are the two North American indices CAN and USA. The same holds true for the European indices CH, DEU, FRA, and UK in DAG $\mathcal{D}_{\text {COR }}$, while DEU and UK are nonadjacent in $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}$ and $\mathcal{D}_{\mathrm{K}}$. A probability measure satisfying the Markov properties represented by either $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}$ or $\mathcal{D}_{\mathrm{K}}$, respectively, observes the conditional independence restriction DEU $\Perp$ UK $|\{\mathrm{CH}, \mathrm{FRA}\}$. All further conditional independence restrictions represented by the DAGs in Figure 8 involve indices in at least two of the above given regions Asia-Pacific, Europe, and North

# 7. Application: Stock market indices 

America. We hence observe a strong geographical clustering of dependences. Moreover, all three DAGs in Figure 8 represent the conditional independence restriction $\{\mathrm{AUS}, \mathrm{HK}, \mathrm{JPN}, \mathrm{SGP}\} \Perp$ \{CAN, USA\} | \{CH, DEU, FRA, UK\}, that is, Asia-Pacific $\Perp$ North America | Europe. Note that Markov properties alone are not sufficient for deriving causal relations within the analysed data (see, for instance, the undirected edges in an essential graph), but they can be used as a starting point for further research in that direction.

A well-ordering for $\mathcal{D}_{\text {COR }}$ is given by $1 \mapsto \mathrm{CAN}, 2 \mapsto \mathrm{CH}, 3 \mapsto \mathrm{DEU}, 4 \mapsto \mathrm{UK}, 5 \mapsto \mathrm{FRA}$, $6 \mapsto$ USA, $7 \mapsto$ JPN, $8 \mapsto$ SGP, $9 \mapsto$ AUS, $10 \mapsto \mathrm{HK}$. Similarly, we obtain a well-ordering for $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}$ and $\mathcal{D}_{\mathrm{K}}$, respectively, by mapping $1 \mapsto \mathrm{CAN}, 2 \mapsto \mathrm{CH}, 3 \mapsto \mathrm{UK}, 4 \mapsto \mathrm{FRA}, 5 \mapsto \mathrm{DEU}$, $6 \mapsto$ USA, $7 \mapsto$ JPN, $8 \mapsto$ AUS, $9 \mapsto$ SGP, $10 \mapsto \mathrm{HK}$. We determined parent orderings for the three DAGs in Figure 8 in two steps. First, we applied the greedy-type procedure with Kendall's $\tau$ edge weights described in Section 4.2, and second, we permuted some of the orderings obtained in step one to reduce the number of integrals in the corresponding paircopula decompositions and thus the computational complexity. More precisely, we changed $\mathrm{JPN}<_{\text {AUS }} \mathrm{SGP}$ and $\mathrm{CAN}<_{\text {USA }} \mathrm{DEU}<_{\text {USA }} \mathrm{FRA}$ in $\mathrm{DAG} \mathcal{D}_{\text {COR }}$ into $\mathrm{SGP}<_{\text {AUS }} \mathrm{JPN}$ and $\mathrm{DEU}<_{\text {USA }} \mathrm{FRA}<_{\text {USA }} \mathrm{CAN}$, respectively, and $\mathrm{CAN}<_{\text {USA }} \mathrm{DEU}<_{\text {USA }} \mathrm{FRA}$ in $\mathrm{DAG} \mathcal{D}_{\mathrm{K}}$ into $\mathrm{DEU}<_{\text {USA }} \mathrm{FRA}<_{\text {USA }} \mathrm{CAN}$. The resulting parent orderings for $\mathcal{D}_{\mathrm{COR}}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}$, and $\mathcal{D}_{\mathrm{K}}$, respectively, are displayed in Figure 8.

## Pair-copula selection and ML estimation

Having fixed the parent orderings for the three PCBNs corresponding to $\mathcal{D}_{\mathrm{COR}}, \mathcal{D}_{\mathrm{GR}, \mathrm{H}}$, and $\mathcal{D}_{\mathrm{K}}$, respectively, we next selected parametric copula families using the AIC as a selection criterion. We considered the Clayton, Frank, Gaussian, Gumbel, and Student's t copula families as well as reflected versions of the Clayton and Gumbel copula families in order to account for negative correlations. We then computed sequential ML estimates of the parameters of the so specified PCBNs. Selected pair-copula families, corresponding sequential ML estimates, bootstrapped standard errors, and estimates of Kendall's $\tau$ are given in Table 5. The respective maximised log-likelihoods and AIC values are summarised in Table 6. Moreover, we compared model fit to the respective Gaussian PCBNs comprising only Gaussian pair copulas. Corresponding ML estimates, standard errors, and estimates of Kendall's $\tau$ are again found in Table 5, while maximised log-likelihoods and AIC values are given in Table 6.

According to the AIC, the best fit was obtained by the non-Gaussian PCBN with DAG $\mathcal{D}_{\mathrm{GR}, \mathrm{H}}$, followed by the non-Gaussian PCBNs associated to $\mathcal{D}_{\mathrm{K}}$ and $\mathcal{D}_{\mathrm{COR}}$, respectively. Applying the Vuong test with AIC correction (Vuong, 1989) to the non-Gaussian PCBNs at the $5 \%$ level, we cannot reject the null hypothesis that all three models are equally close to the true model. A similar statement holds for the Gaussian PCBNs. However, using the Vuong test for model

7. Application: Stock market indices


Table 5: Selected pair-copula families, sequential ML estimates, standard errors (parentheses), and estimates of Kendall's $\tau$ for the Gaussian $(\mathcal{G})$ and non-Gaussian (n $\mathcal{G}$ ) PCBNs corresponding to the DAGs in Figure 8. Copulas include the Frank (F), Gaussian (N), Survival-Gumbel (SG), and Student's t (t) pair-copula families.
selection between a Gaussian and a non-Gaussian PCBN will always decide in favor of the nonGaussian model, which again shows the latter models' superiority. This is, of course, to be expected since financial returns often exhibit heavy-tailed dependence, which is validated here by the low estimates of the degrees-of-freedom parameters of the Student's t copulas.


Table 6: Maximised log-likelihoods, numbers of parameters, and AIC values for the Gaussian $(\mathcal{G})$ and non-Gaussian (nG) PCBNs corresponding to the DAGs in Figure 8. Sequential ML estimates of the corresponding parameters are given in Table 5.

# 8. Conclusion 

We have investigated a novel procedure for constructing non-Gaussian continuous Bayesian networks that uses bivariate copulas as building blocks. The resulting models can accommodate a great variety of distributional features to be modelled such as tail-dependence and non-linear, asymmetric dependence. We have provided an algorithm for deriving explicit representations of the corresponding log-likelihoods, as well as routines for random sampling and model selection.

Depending on the underlying DAG and the corresponding parent orderings, the evaluation of the log-likelihood of a PCBN may involve high-dimensional numerical integration and hence considerable computational effort. We have presented a greedy procedure for selecting the parent orderings of the vertices of the underlying DAG, which is based on the idea of modelling strongest dependences in the unconditional pair-copulas. In Section 7, we introduced an additional selection step, in which some of the parent sets were rearranged in order to reduce the number of integrals in the corresponding likelihood decompositions. It would be desirable to have theoretical results on the relationship between parent orderings and the number and complexity of integrals. Bauer et al. (2012) suggested to replace some or all of the integrals by non-parametric kernel conditional cdf estimators. Another way of reducing computational complexity is to consider sequential instead of joint ML estimates.

We used vine copula models to derive a novel test for conditional independence of continuous random variables. The quality of the test, by design, greatly benefits from the ongoing research on vine copulas. In combination with the PC algorithm, we obtained a structure estimation procedure for non-Gaussian PCBNs, which proved to be reliable in the simulation study in Section 6. One may investigate the performance of other conditional independence tests like Zhang et al. (2011), as well as of other structure estimation algorithms. Also, recall that by Meek (1995), constraint-based estimation algorithms can be adapted to incorporate existing expert knowledge. The distributional flexibility of pair-copula Bayesian networks may become even more apparent in application areas other than finance.

# Acknowledgements 

The authors are very grateful to Peter Hepperger for his help in implementing the algorithms of Section 4 in C++. The computer programs were tested on a Linux cluster supported by the DFG (German Research Foundation). Alexander Bauer acknowledges the support of the TUM Graduate School's Faculty Graduate Center ISAM (International School of Applied Mathematics) at the Technische Universität München.

# A. Estimated AR-GARCH parameters and standard errors 


Table 7: ML estimates and standard errors (in parentheses) of $\operatorname{AR}(1)-\operatorname{GARCH}(1,1)$ parameters for the ten time series of daily log-returns analysed in Section 7.