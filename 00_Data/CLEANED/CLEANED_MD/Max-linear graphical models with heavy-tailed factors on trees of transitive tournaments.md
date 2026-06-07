# Max-linear graphical models with heavy-tailed factors on trees of transitive tournaments 

Stefka Asenova* Johan Segers ${ }^{\dagger}$

June 8, 2023


#### Abstract

Graphical models with heavy-tailed factors can be used to model extremal dependence or causality between extreme events. In a Bayesian network, variables are recursively defined in terms of their parents according to a directed acyclic graph (DAG). We focus on max-linear graphical models with respect to a special type of graphs, which we call a tree of transitive tournaments. The latter are block graphs combining in a tree-like structure a finite number of transitive tournaments, each of which is a DAG in which every two nodes are connected. We study the limit of the joint tails of the max-linear model conditionally on the event that a given variable exceeds a high threshold. Under a suitable condition, the limiting distribution involves the factorization into independent increments along the shortest trail between two variables, thereby imitating the behavior of a Markov random field. We are also interested in the identifiability of the model parameters in case some variables are latent and only a subvector is observed. It turns out that the parameters are identifiable under a criterion on the nodes carrying the latent variables which is easy and quick to check.


Keywords - max-linear model, heavy tails, extremal dependence, conditional dependence, probabilistic graphical model, directed acyclic graph, tournaments, extremes

## 1 Introduction

Dependence in multivariate linear factor models is determined by a collection of independent random variables, called factors, which are shared by the modelled variables. In extreme value analysis there are the max-linear and the additive factor models with heavy-tailed factors. In Einmahl et al. (2012), it is shown that both have the same max-domain of attraction.

In Gissibl and Klüppelberg (2018), a link is made between such factor models and probabilistic graphical models via a max-linear recursively defined structural equation model on a directed acyclic graph (DAG). Each node carries a variable defined as a weighted maximum of its parent variables and an independent factor. This leads to a representation of the graphical model as a (max-)factor model as in Einmahl et al. (2012), the factors relevant for a given variable being limited to the set of its ancestors. More recent is the linear causally structured model in Gnecco et al. (2021): each variable is the weighted sum of the variables on all its parent nodes plus an independent factor. This leads to a representation where a single variable is a weighted sum of all its ancestral factors.

In this paper, we study a type of graph that, to the best of our knowledge, is not yet known and which we gave a name that reflects its most important properties: a tree of transitive tournaments $(t t t)$, denoted by $\mathcal{T}$. A tournament is a graph obtained by directing a complete graph, while a tournament is said to be transitive if it has no directed cycles. The name reflects the interpretation

[^0]
[^0]:    *Corresponding author. UCLouvain, LIDAM/ISBA, Voie du Roman Pays 20, 1348 Louvain-la-Neuve, Belgium. E-mail: stefka.asenova@uclouvain.be
    ${ }^{\dagger}$ UCLouvain, LIDAM/ISBA, Voie du Roman Pays 20, 1348 Louvain-la-Neuve, Belgium. E-mail: johan.segers@uclouvain.be

of such a graph as a competition where every node is a player and a directed edge points from the winner to the loser. Some examples are hierarchical relations between members of animal and bird societies, brand preferences, and votes between two alternative policies (Harary and Moser, 1966). A ttt links up several such transitive tournaments in a tree-like structure. It is acyclic by construction. If there is a directed path from one node to another one, there is a unique shortest such path. Moreover, between any pair of nodes, there is a unique shortest undirected path.

In this paper, we study max-linear graphical models with respect to a ttt as defined in (2) below. In particular, for a max-linear random vector $X=\left(X_{v}, v \in V\right)$ with node set $V$, we study the limit in distribution

$$
\left(X_{v} / X_{u}, v \in V \backslash u \mid X_{u}>t\right) \xrightarrow{d}\left(A_{u v}, v \in V\right), \quad t \rightarrow \infty
$$

It is not hard to show that the limit distribution in (1) is discrete (Segers, 2020b, Example 1). We show that if the ttt has a unique node without parents, a so-called source node, the joint distribution of $\left(A_{u v}, v \in V\right)$ is determined by products of independent multiplicative increments along the unique shortest undirected paths between the node $u$ at which the high threshold is exceeded on the one hand and the rest of the nodes on the other hand. Such behaviour is analogous to that of Markov random fields on block graphs in Asenova and Segers (2023) and of Markov trees in Segers (2020b, Theorem 1). In turn, these results go back to the extensive literature on the additive or multiplicative structure of extremes for Markov chains (e.g. Smith, 1992; Yun, 1998; Segers, 2007; Janssen and Segers, 2014; Resnick and Zeber, 2013).

An underlying reason for the factorization into independent increments is the fact that a maxlinear graphical model with respect to a ttt is a Markov random field with respect to the undirected graph associated to the original, directed graph when the ttt has a unique source. A ttt with unique source has no v-structures, that is, no nodes with non-adjacent parents. Both properties, the factorization of the limiting variables and the Markovianity with respect to the undirected graph, are lost if the graph contains v-structures. To show this, we rely on recent theory of conditional independence in max-linear Bayesian networks based on the notion of $*$-connectedness (Améndola et al., 2021; Améndola et al., 2022). This theory diverges from classical results on conditional independence in Bayesian networks based on the notion of d-separation (Lauritzen, 1996; Koller and Friedman, 2009).

In our paper the graph is given. A significant line of research in the context of extremal dependence is graph discovery. Given observations on a number of variables represented as nodes in a graph, the task is to estimate the edges. For Bayesian networks we can also talk about causality discovery because directed edges show the direction of influence. A first attempt to identify the DAG in the context of max-linear models is Gissibl et al. (2018), followed by several papers focusing on this topic: Klüppelberg and Krali (2021), Buck and Klüppelberg (2021), Gissibl et al. (2021), Tran et al. (2021a) and Tran et al. (2021b). The problems related to identifiability of the true graph and to the estimation of the edge weights are discussed in Klüppelberg and Lauritzen (2019). Gnecco et al. (2021) study a new metric called causal tail coefficient which is shown to reveal the structure of a linear causal recursive model with heavy-tailed noise. Graph discovery for non-directed graphs is studied in Engelke and Hitz (2020), Engelke and Volgushev (2022) and Hu et al. (2022).

Inspired from practice, and more specifically river network applications (Asenova et al., 2021), we study a different identifiability problem. If the structure of the graph is known, it may happen that on some nodes the variables are latent, i.e., unobserved. The identifiability problem in this case is whether two different parameter vectors can still generate the same distribution of the observable part of the model. If this is possible then we cannot uniquely identify all tail dependence parameters that characterize the full distribution. Similarly to Asenova and Segers (2023), the identifiability criterion involves properties of the nodes with latent variables. The criterion is specific for a ttt with unique source and is easy to check. Our identifiability problem resembles the "method of path coefficients" of Sewall Wright which uses a system of equations involving correlations to solve for the edge coefficients (Wright, 1934).

The novelty of the paper lies in several directions. First, a new class of graphs is introduced, called a tree of transitive tournaments (ttt), which is the directed acyclic analogue of a block graph. It can be seen as a generalization of a directed tree, where edges are replaced by transitive tournaments. Second, we show that a max-linear graphical model over a ttt with unique source exhibits properties known for other graphical models, namely Markov trees (Segers, 2020b) and Markov block graphs (Asenova and Segers, 2023). In particular, when the ttt has a unique source, the model is Markov with respect to the skeleton of the graph. This property underlies the factorization of the tail limit into independent increments along the unique shortest trails. Finally, we study a problem of

identifiability of the edge weights from the angular measure both when all variables are observed and also when some of them are latent.

The structure of the paper is as follows. In Section 2 we introduce the ttt, the max-linear model, and its angular measure, which plays a key role in almost all proofs. In Section 3 we discuss the limiting distribution of (1) and give four equivalent characterizations of a max-linear graphical model with respect to a ttt with unique source. The identifiability problem is covered in Section 4. The discussion summarizes the main points of the paper. The appendices contain some additional lemmas and the proofs that are not presented in the main text.

# 2 Notions and definitions 

### 2.1 Directed graphs

Let $\mathcal{T}=(V, E)$ be a directed acyclic graph (DAG) with finite vertex (node) set $V$ and edge set $E \subset V \times V$. An edge $e:=(u, v) \in E$ is directed meaning $(u, v) \neq(v, u)$; it is outgoing with respect to the parent node $u$ and incoming with respect to the child node $v$. The graph $\mathcal{T}$ excludes loops, i.e., edges of the form $(u, u)$, and as $\mathcal{T}$ is directed, we cannot have both $(u, v) \in E$ and $(v, u) \in E$. Two nodes $u$ and $v$ are adjacent if $(u, v)$ or $(v, u)$ is an edge. A cycle is a sequence of edges $e_{1}, \ldots, e_{n}$ with $e_{k}=\left(u_{k}, u_{k+1}\right)$ and $u_{1}=u_{n+1}$ for some nodes $u_{1}, \ldots, u_{n}$. The property that $\mathcal{T}$ is acyclic means that it does not contain any cycle. The graph $\mathcal{T}$ is assumed connected, i.e., for any two distinct nodes $u$ and $v$ we can find nodes $u_{1}=u, u_{2}, \ldots, u_{n+1}=v$ such that $u_{k}$ and $u_{k+1}$ are adjacent for every $k=1, \ldots, n$; we call the associated edge sequence an undirected path or a trail between $u$ and $v$. If all edges are directed in the same sense, i.e., $\left(u_{k}, u_{k+1}\right) \in E$ for all $k=1, \ldots, n$, we talk about a (directed) path from the ancestor $u$ to the descendant $v$. Recall that a path is directed by convention, so when we need non-directed paths this will be indicated explicitly. Between a pair of nodes there may be several paths. The set of all paths between two nodes $u, v \in V$ is denoted by $\pi(u, v)$. An element, say $p$, of $\pi(u, v)$ is a collection of edges, $\left\{\left(v_{1}, v_{2}\right),\left(v_{2}, v_{3}\right), \ldots,\left(v_{n-1}, v_{n}\right)\right\}$ for a path that involves the non-repeating nodes $\left\{v_{1}=u, v_{2}, \ldots, v_{n-1}, v_{n}=v\right\}$. Note that $\pi(u, u)=\varnothing$ in an acyclic graph.

A source is a node without parents. If a DAG has a unique source, this node is an ancestor of every other node. This property follows from the following reasoning: let $u_{0}$ denote the unique source node of the DAG, and let $v$ be any other node different from $u_{0}$. Then $v$ must have a parent, say $u$. If $u=u_{0}$, we are done. Otherwise, replace $v$ by $u$ and restart. Since the graph is finite and has no cycles, this chain must stop at some moment at a node without parents. But this node is necessarily equal to $u_{0}$ by assumption.

A graph, directed or not, is complete if there is an edge between any pair of distinct nodes. A subgraph of a graph is biconnected if the removal of any of its nodes will not disconnect the subgraph. A maximal biconnected subgraph, also known as a biconnected component, is a subgraph that cannot be extended by adding one adjacent node without violating this principle.

A directed complete graph is called a tournament. A tournament $\tau=\left(V_{\tau}, E_{\tau}\right)$ is transitive if $(u, v),(v, w) \in E_{\tau}$ implies $(u, w) \in E_{\tau}$. A transitive tournament is necessarily acyclic. The graph-theoretic properties of transitive tournaments are studied in Harary and Moser (1966). The property most used here is that the set of out-degrees of the $d$ nodes of a transitive tournament is $\{d-1, d-2, \ldots, 0\}$; the in- and out-degrees of a node are the numbers of incoming and outgoing edges, respectively.

A subgraph of a graph is a maximal transitive tournament if it is not properly contained in another subgraph which is also a transitive tournament. The set of maximal transitive tournaments that are subgraphs of a DAG $\mathcal{T}$ will be denoted by $\mathbb{T}$. For brevity we will just write tournament when we mean a maximal transitive tournament and denote it by $\tau$.

### 2.2 Tree of transitive tournaments

A block graph is an undirected graph where every maximal biconnected subgraph is a complete graph (Le and Tuy, 2010). Let $T$ denote the non-directed version of $\mathcal{T}$, also called the skeleton of $\mathcal{T}$. It shares the same node set as $\mathcal{T}$, and for every edge $(u, v)$ in the original graph $\mathcal{T}$, the reverse edge $(v, u)$ is added to form the edge set of the skeleton graph $T$, after which each pair of edges $\{(u, v),(v, u)\}$ is identified with the undirected edge $\{u, v\}$ of $T$.

![img-0.jpeg](img-0.jpeg)

Figure 1: A tree of four maximal transitive tournaments: $\tau_{1}, \tau_{2}, \tau_{3}$, and $\tau_{4}$. The skeleton graph is the same, but with arrow heads removed. Node 3 is a separator node between tournaments $\tau_{1}$, $\tau_{2}$ and $\tau_{3}$, while node 7 is a separator node between tournaments $\tau_{3}$ and $\tau_{4}$. Nodes 1, 4 and 8 are source nodes, i.e., have no parents. The subgraph with node set $\{1,3,4\}$ is a v-structure: node 3 has non-adjacent parents 1 and 4 . Other v-structures within the ttt are the subgraphs with node sets $\{3,7,8\}$ and $\{5,7,8\}$. Between any pair of distinct nodes there is a unique shortest trail; for instance, nodes 4 and 8 are connected by the trail passing through nodes 3 and 7 . There is no undirected cycle encompassing several tournaments.

Definition 2.1 (Tree of transitive tournaments (ttt)). A tree of transitive tournaments is a connected directed acyclic graph whose skeleton is a block graph.

A ttt enjoys three key properties. They all follow from the link with block graphs, whose characteristics can be found in Le and Tuy (2010).

Lemma 2.2 (Properties I). For a ttt, the following properties hold:
(P1) two or more maximal transitive tournaments can have at most one common node, referred to as a separator node;
(P2) there is no undirected cycle that passes through nodes in different maximal transitive tournaments;
(P3) between every pair of nodes there is a unique shortest trail (undirected path).
Proof. All properties are direct consequences of the fact that removing directions from the ttt we obtain a block graph. In a block graph the minimal separators sets are singletons (Harary, 1963, Theorem B); there is a unique shortest path between two nodes (Behtoei et al., 2010, Theorem 1.a)); and the graph is acyclic up to blocks, a property that follows from the first one.

Similarly to block graphs (Le and Tuy, 2010) a ttt can be seen as a tree whose edges are replaced by transitive tournaments.

In a ttt, if there is at least one (directed) path between distinct nodes $u$ and $v$, there is a unique shortest path (see Lemma 2.3-1) between them, which we denote by $p(u, v)$, and which belongs to $\pi(u, v)$. We also set $p(u, u)=\varnothing$ by convention.

A key object in the paper is a ttt with unique source. In Lemma 2.3-2 below it is shown that in this case there are no nodes with parents that are not adjacent or 'married', also known as a v-structure (Koller and Friedman, 2009).

Consider the ttt in Figure 1, which presents some of the notions introduced above. Each tournament is acyclic and we cannot find a cycle passing through different tournaments either. This is why we call such a graph a tree of transitive tournaments. There are three v-structures: one on nodes $1,3,4$, one on $3,7,8$ and one on $5,7,8$. The main results in this paper require a ttt without v-structures. According to Lemma 2.3, there are no v-structures in a ttt with unique source. This is illustrated in Figure 2.

Considered on its own, every tournament in a ttt has a unique source; this follows from the ordering of the out-degrees due to Harary and Moser (1966) mentioned earlier. When we talk about a source node, we will always state if we refer to the whole graph or with respect to a particular tournament.

In a general directed graph $(V, E)$, let $\mathrm{pa}(v) \in V$ denote the set of parents of $v \in V$ and put $\mathrm{Pa}(v)=\mathrm{pa}(v) \cup\{v\}$. In a similar way let $\operatorname{an}(v), \operatorname{desc}(v)$, and $\operatorname{ch}(v)$ denote the sets of ancestors,

![img-1.jpeg](img-1.jpeg)Figure 2: A tree of four maximal transitive tournaments. The skeleton graph is the same as the one in Figure 1, but the graph here has a single source, on node 4. We see that there are no v-structures anymore in the graph.

descendants, and children, respectively, excluding $v$, while $\operatorname{An}(v)$, $\operatorname{Desc}(v)$, and $\operatorname{Ch}(v)$ denote the same sets but including $v$.

Below we present some additional properties used often in the paper.
Lemma 2.3 (Properties II). Let $\mathcal{T}$ be a tree of transitive tournaments as in Definition 2.1. We have the following statements:

1. If there is a path between two nodes, then there is a unique shortest path between them.
2. The ttt $\mathcal{T}$ has a unique source if and only if it possesses no v-structures.
3. If $\mathcal{T}$ has a unique source, then for any two nodes $i \neq j$, the sets $\operatorname{Desc}(i)$ and $\operatorname{Desc}(j)$ are either disjoint or one contains the other, that is, $i$ is an ancestor of $j$ or vice versa.

Lemma 2.4 (Properties III). Consider a ttt $\mathcal{T}=(V, E)$ as in Definition 2.1 with unique source.

1. If $\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$ is the node sequence of a unique shortest path between nodes $v_{1}$ and $v_{n}$, then all nodes except for possibly $v_{1}$ and $v_{n}$ are the source node of the tournament shared with the next node in the sequence.
2. Between any two distinct nodes $u, v$ in $\mathcal{T}$ the unique shortest trail between them is either $p(u, v)$ or $p(v, u)$ or there exists a node $w \in V \backslash\{u, v\}$ such that the trail is composed of the two shortest paths $p(w, u)$ and $p(w, v)$.

# 2.3 Max-linear structural equation model on a ttt 

Consider a directed graph, $(V, E)$. To each edge $e=(i, j) \in E$ we associate a weight $c_{e}=c_{i j} \in[0, \infty)$. The product of the edge parameters over a directed path $p=\left\{e_{1}, \ldots, e_{m}\right\}$ is denoted by

$$
c_{p}=\prod_{r=1}^{m} c_{v_{r}}
$$

When the product is over the unique shortest path from $u$ to $v$, we write $c_{p(u, v)}$. The product over the empty set being one by convention, we have $c_{p(i, i)}=1$.

Let $\left(Z_{i}, i \in V\right)$ be a vector of independent unit-Fréchet random variables, i.e., $\mathbb{P}\left(Z_{i} \leq z\right)=$ $\exp (-1 / z)$ for $z>0$. In the spirit of (Gissibl and Klüppelberg, 2018), a recursive max-linear model on a ttt, $\mathcal{T}$, is defined by

$$
X_{v}=\bigvee_{i \in \mathrm{pa}(v)} c_{i v} X_{i} \vee c_{v v} Z_{v}, \quad v \in V
$$

where the parameters $c_{e}$, for $e \in E$, and $c_{v v}$, for $v \in V$, are positive. We interpret this constraint as follows: if $c_{i j}=0$, the variable $X_{j}$ cannot be influenced by $X_{i}$ through edge $(i, j)$, and the edge could be removed from the graph. If $c_{v v}=0$, the factor variable $Z_{v}$ does not influence $X_{v}$. We don't want to deal with such border cases, so we assume that all parameters in the model definition (2) are positive. According to Gissibl and Klüppelberg (2018, Theorem 2.2) the expression in (2) is equal also to

$$
X_{v}=\bigvee_{i \in V} b_{v i} Z_{i}
$$

with

$$
b_{v i}= \begin{cases}0 & \text { if } i \notin \operatorname{An}(v) \\ c_{v v} & \text { if } i=v \\ c_{i i} \max _{p \in \pi(i, v)} c_{p} & \text { if } i \in \operatorname{an}(v)\end{cases}
$$

The cumulative distribution function (cdf) of $X_{v}$ is $\mathbb{P}\left(X_{v} \leq x\right)=\exp \left(-\sum_{i \in V} b_{v i} / x\right)$ for $x>0$. We assume that $\left(X_{v}, v \in V\right)$ are unit-Fréchet, yielding the constraint

$$
\sum_{i \in V} b_{v i}=\sum_{i \in \operatorname{An}(v)} b_{v i}=1, \quad \forall v \in V
$$

since $b_{v i}=0$ whenever $i \notin \operatorname{An}(v)$. It is thus necessary and sufficient to have

$$
c_{v v}=1-\sum_{i \in \operatorname{an}(v)} c_{i i} \max _{p \in \pi(i, v)} c_{p}
$$

with $c_{v v}=1$ if $\operatorname{an}(v)=\varnothing$. By (6), the coefficients $c_{v v}$ for $v \in V$ are determined recursively by the edge weights $c_{e}$ for $e \in E$. If $c_{i v} \geq 1$ for some $(i, v) \in E$, then (2) implies that $X_{v} \geq X_{i} \vee c_{v v} Z_{v}$, and the constraint that $X_{i}$ and $X_{v}$ are unit-Fréchet distributed implies that $c_{v v}=0$, a case we want to exclude, as explained above. This is why we impose $0<c_{e}<1$ for all $e \in E$ from the start, yielding the parameter space

$$
\hat{\Theta}=\left\{\theta=\left(c_{e}, e \in E\right) \in(0,1)^{E}: \forall v \in V, c_{v v}>0\right\}
$$

The notion of criticality is important for max-linear structural equation models. We refer to Gissibl and Klüppelberg (2018), Améndola, Klüppelberg, Lauritzen, and Tran (2022), Gissibl, Klüppelberg, and Lauri (2021) and Klüppelberg and Lauritzen (2019) for examples where different conditional independence relations arise depending on which path is critical, or for illustrations in the context of graph learning. According to Gissibl and Klüppelberg (2018, Definition 3.1), a path $p \in \pi(i, v)$ is max-weighted under $\theta \in \Theta$ if it realizes the maximum $\max _{p^{\prime} \in \pi(i, v)} c_{p^{\prime}}$, where $p^{\prime}$ is any path in $\pi(i, v)$. In Améndola et al. (2022) the term critical is preferred.

If there is a (directed) path between two nodes, there is a unique shortest (directed) path between them (Lemma 2.3-1). This is crucial for our parametric model. We define the critical parameter space $\Theta_{*} \subset(0,1)^{E}$ as the set of parameters $\theta=\left(c_{e}, e \in E\right)$, such that for every $v \in V$ and every $i \in \operatorname{an}(v)$, the unique shortest directed path from $i$ to $v$ is the only critical path. Therefore we have $c_{p(i, v)}>c_{p}$, with strict inequality for any $p \in \pi(i, v)$ different from $p(i, v)$. Formally,

$$
\Theta_{*}=\left\{\theta \in(0,1)^{E}: \forall v \in V, \forall i \in \operatorname{an}(v), \forall p \in \pi(i, v) \backslash\{p(i, v)\}, c_{p(i, v)}>c_{p}\right\}
$$

Next, we consider the intersection of the two spaces as an appropriate parameter space for our max-linear structural equation model:

$$
\hat{\Theta}_{*}=\hat{\Theta} \cap \Theta_{*}
$$

For $\theta \in \hat{\Theta}_{*}$, every element of the max-linear coefficient matrix $B_{\theta}=\left(b_{v i}\right)_{v, i \in V}$ can be rewritten using an edge weight product over the unique shortest path $p(i, v)$ via

$$
b_{v i}= \begin{cases}0 & \text { if } i \notin \operatorname{An}(v) \\ c_{v v} & \text { if } i=v \\ c_{i i} c_{p(i, v)} & \text { if } i \in \operatorname{an}(v)\end{cases} \quad \text { and } \quad c_{v v}=1-\sum_{i \in \operatorname{an}(v)} c_{i i} c_{p(i, v)}
$$

Also, note that $b_{i i}=c_{i i}$, leading to the frequently used expression

$$
b_{v i}=c_{p(i, v)} b_{i i}, \quad i \in \operatorname{an}(v)
$$

Example 1 (Criticality). The following example shows what happens if the assumption that all shortest paths are critical is omitted. Consider a max-linear model on three nodes $\{1,2,3\}$ and three edges $\{(1,2),(2,3),(1,3)\}$. The corresponding edge weights are $c_{12}, c_{23}, c_{13}$. We have

$$
X_{1}=c_{11} Z_{1}, \quad X_{2}=c_{12} X_{1} \vee c_{22} Z_{2}, \quad X_{3}=c_{13} X_{1} \vee c_{23} X_{2} \vee c_{33} Z_{3}
$$

The coefficient matrix $B=\left\{b_{i v}\right\}$ from (4) together with (5) and (6) is

$$
B=\left[\begin{array}{ccc}
1 & 0 & 0 \\
c_{12} & \left(1-c_{12}\right) & 0 \\
c_{12} c_{23} \vee c_{13} & c_{23}\left(1-c_{12}\right) & 1-c_{12} c_{23} \vee c_{13}-c_{23}\left(1-c_{12}\right)
\end{array}\right]
$$

If the shortest path $p=\{(1,3)\}$ from node 1 to node 3 is not critical then we have $b_{31}=c_{12} c_{23}$ and also $b_{33}=1-c_{23}$. In this way the coefficient $c_{13}$ has completely left the model. When considering the identifiability problem, we cannot hope to identify a coefficient from some marginal distribution if it is not even identifiable from the full one.

Now, all elements are in place to describe our main object of interest.
Assumption 2.1 (Max-linear structural equation model on a ttt). The random vector $X=\left(X_{v}, v \in\right.$ $V)$ has the max-linear representation in (3) and (8) with respect to the ttt $\mathcal{T}=(V, E)$ (Definition 2.1) where $\left(Z_{v}, v \in V\right)$ is a vector of independent unit-Fréchet random variables and the edge weight vector $\theta=\left(c_{v}, e \in E\right)$ belongs to $\hat{\Theta}_{*}$ in (7).

The following identity for nodes with a unique parent will be useful:

$$
\operatorname{pa}(v)=\{i\} \Longrightarrow b_{v v}=1-c_{i v}
$$

Indeed, if $i$ is the only parent of $v$, then $X_{v}=c_{i v} X_{i} \vee c_{v v} Z_{v}$ by (2). The variables $X_{v}, X_{i}, Z_{v}$ are unit-Fréchet distributed and $X_{i}$ is independent of $Z_{v}$, since $X_{i}$ is a function of $\left(Z_{u}, u \in \operatorname{An}(i)\right)$ and $v \notin \operatorname{An}(i)$. Hence $c_{i v}+c_{v v}=1$, and because $c_{v v}=b_{v v}$, Eq. (9) follows.

A notational convention: in case of double subscripts, we may also write $x_{i_{1}, i_{2}}$ instead of $x_{i_{1} i_{2}}$.

# 2.4 The angular measure 

Let $X$ follow a max-linear model with parameter vector $\theta$ as in Assumption 2.1. The joint distribution $P_{\theta}$ of $X$ on $[0, \infty)^{V}$ is max-stable and has unit-Fréchet margins. It is determined by

$$
P_{\theta}([0, z])=\mathbb{P}(X \leq z)=\exp \left(-l_{\theta}\left(\left(1 / z_{v}\right)_{v \in V}\right)\right), \quad z \in(0, \infty]^{V}
$$

where the stable tail dependence function (stdf) $l_{\theta}:[0, \infty)^{V} \rightarrow[0, \infty)$ is

$$
l_{\theta}(x)=\sum_{i \in V} \max _{v \in V}\left(b_{v i} x_{v}\right)
$$

for $x=\left(x_{v}\right)_{v \in V} \in[0, \infty)^{V}$ (Einmahl et al., 2012).
Let $H_{\theta}$ be the angular measure on the unit simplex $\Delta_{V}=\left\{a \in[0,1]^{V}: \sum_{v \in V} a^{(v)}=1\right\}$ corresponding to the stdf $l_{\theta}$. The link between the stdf and the angular measure is detailed in de Haan and Ferreira (2007) for the bivariate case and in Resnick (1987, Chapter 5) and Beirlant et al. (2004, Chapters $7-8$ ) for higher dimensions: we have

$$
l_{\theta}(x)=\int_{\Delta_{V}} \max _{v \in V}\left(a^{(v)} x_{v}\right) \mathrm{d} H_{\theta}(a)
$$

In view of the expression of $l_{\theta}$ in (10), the angular measure is discrete and satisfies

$$
H_{\theta}=\sum_{i \in V} m_{i} \delta_{a_{i}}
$$

with masses $m_{i}=\sum_{v \in V} b_{v i}$ and atoms $a_{i}=\left(b_{v i} / m_{i}\right)_{v \in V} \in \Delta_{V}$ for $i \in V$ (Einmahl, Krajina, and Segers, 2012, page 1779). The notation $\delta_{x}$ refers to a unit point mass at $x$.

If $X$ follows a max-linear model, the angular measure of $X$ is identifiable from its distribution $P_{\theta}$ via the limit relation

$$
t \mathbb{P}\left(\frac{1}{\|X\|_{1}} X \in \cdot,\|X\|_{1}>t\right) \xrightarrow{w} H_{\theta}(\cdot), \quad t \rightarrow \infty
$$

where $\|x\|_{1}=\sum_{i}\left|x_{i}\right|$ for a vector $x$ in Euclidean space, while the arrow $\xrightarrow{w}$ denotes weak convergence of finite Borel measures, in this case on $\Delta_{V}$.

When we discuss latent variables and identifiability in Section 4, we have to deal with the angular measure of a subvector of $X$, say $X_{U}=\left(X_{v}\right)_{v \in U}$, for non-empty $U \subset V$. Its stdf $l_{\theta, U}$ arises from $l_{\theta}$ by setting $x_{v}=0$ for all $v \notin U$ : for $x \in[0, \infty)^{U}$ we have

$$
l_{\theta, U}(x)=\sum_{i \in V} \max _{v \in U}\left(b_{v i} x_{v}\right)=\int_{\Delta_{U}} \max _{v \in U}\left(a^{(v)} x_{v}\right) \mathrm{d} H_{\theta, U}(a)
$$

The distribution of $X_{U}$ is max-linear too, so that its angular measure $H_{\theta, U}$ on $\Delta_{U}$ has a similar form as the one of $X$ :

$$
H_{\theta, U}=\sum_{i \in V} m_{i, U} \delta_{a_{i, U}}
$$

with masses $m_{i, U}=\sum_{v \in U} b_{v i}$ and atoms $a_{i, U}=\left(b_{v i} / m_{i, U}\right)_{v \in U} \in \Delta_{U}$ for $i \in V$.

# 3 Conditional tail limit and the ttt with unique source 

Here we study the limit distribution of

$$
\left(\frac{X_{v}}{X_{u}}, v \in V \mid X_{u}>t\right), \quad t \rightarrow \infty
$$

when $X$ is a max-linear model with respect to a ttt $\mathcal{T}=(V, E)$ as in Assumption 2.1. In particular, we are interested to know whether the elements of the limiting vector of (13) can be factorized into products of independent increments, similarly to other models with this property as in Segers (2020a) and Asenova and Segers (2023). In Proposition 3.1 below, we show that the limit variables factorize according to the unique shortest trails under the condition that the ttt has a unique source (node without parents). Moreover, by Proposition 3.3, the latter criterion is necessary and sufficient for $X$ to satisfy the global Markov property with respect to the skeleton graph associated to $\mathcal{T}$, i.e., the undirected counterpart of $\mathcal{T}$.

Even though Proposition 3.1 below looks similar to Theorem 3.5 in Asenova and Segers (2023), it does not follow from it. The reason is that we have not been able to verify Assumptions 3.1 and 3.4 in that article for the recursive max-linear model. In these assumptions, the conditioning event involves equality, i.e., $\left\{X_{u}=t\right\}$, and calculating the conditional distributions and their limits is not easy. This is why we have opted here for a different route: in (13), the conditioning event is $\left\{X_{u}>t\right\}$ and the limit conditional distribution as $t \rightarrow \infty$ is found from Segers (2020b, Example 1).

According to property (P3), any pair of distinct nodes in a ttt is connected by a unique shortest trail. Let $t(u, v)$ denote the set of edges along the unique shortest trail between two distinct nodes $u$ and $v$. Consider for instance the shortest trail between nodes 2 and 8 on Figure 2: $t(2,8)=$ $\{(3,7),(7,8),(3,2)\}$. In contrast, let $t_{u}(u, v)$ be the set of edges incident to the same node set but directed from $u$ to $v$, irrespective of their original directions, e.g., $t_{2}(2,8)=\{(2,3),(3,7),(7,8)\}$.

For a given node $u \in V$, let $E_{u}$ be the set of all edges in such unique shortest paths directed away from $u$, that is,

$$
E_{u}=\bigcup_{v \in V \backslash u} t_{u}(u, v)
$$

Recall from Section 2 that $\mathbb{T}$ denotes the set of tournaments within the ttt $\mathcal{T}$. For fixed $u \in V$ there is for every tournament $\tau=\left(V_{\tau}, E_{\tau}\right) \in \mathbb{T}$ a node, say $w_{u, \tau}$, which is the unique node in $V_{\tau}$ such that the trail $t\left(u, w_{u, \tau}\right)$ is the shortest one among all trails between $u$ and a node $v$ in $V_{\tau}$. As an example, consider Figure 3: starting from node $u=8$, the closest node from the node set $V_{\tau_{1}}=\{1,2,3\}$ is 3 , hence $w_{8, \tau_{1}}=3$.

With these definitions we are ready to state the condition under which the limiting variables factorize into independent increments.

Proposition 3.1 (Factorization in max-linear model). Let $\left(X_{v}, v \in V\right)$ follow a max-linear model as in Assumption 2.1. Fix $u \in V$. Let $E_{u}$ be as in (14) and let $\left(M_{e}, e \in E_{u}\right)$ be a random vector composed of mutually independent subvectors $M^{(u, \tau)}=\left(M_{w_{u, \tau}}, j: j \in V_{\tau},\left(w_{u, \tau}, j\right) \in E_{u}\right)$, one for every transitive tournament $\tau \in \mathbb{T}$, and with marginal distribution as in Lemma 3.2.

The following statements are equivalent:
(i) $\mathcal{T}$ has a unique source.
(ii) For every $u \in V$, we have, as $t \rightarrow \infty$, the weak convergence P5Ttk2JNYkwUnwBcR6bu

$$
\mathcal{L}\left(X_{v} / X_{u}, v \in V \mid X_{u}>t\right) \xrightarrow{d} \mathcal{L}\left(A^{(u)}\right)=\mathcal{L}\left(A_{u v}, v \in V\right)
$$

with

$$
A_{u v}=\prod_{e \in t_{u}(u, v)} M_{e}, \quad v \in V
$$

![img-2.jpeg](img-2.jpeg)

Figure 3: A ttt on four tournaments: $\tau_{1}$ on node set $\{1,2,3\}$, $\tau_{2}$ on $\{3,4\}$, $\tau_{3}$ on $\{3,5,6,7\}$ and $\tau_{4}$ on $\{8,7\}$. The variable exceeding a high threshold is at node 8. The set $E_{u}$ is composed of the coloured edges which do not necessarily have the same directions in the original graph. On the nodes we have $A^{(8)}=\left(A_{8i}, i=1, \ldots, 7\right)$ and on the edges we have the multiplicative increments $\left(M_{e}, e \in E_{u}\right)$. Increments in different colours are mutually independent, while those in the same color are dependent according to Lemma 3.2.
(iii) There exists $u \in V$ such that the limit in (15) and (16) holds.

The following lemma provides the distribution of $M^{(u, \tau)}$ in Proposition 3.1.
Lemma 3.2. Let $\left(X_{v}, v \in V\right)$ follow a max-linear model as in Assumption 2.1.Let $\tau \in \mathbb{T}$ be a transitive tournament on nodes $V_{\tau}$. Then for $u \in V_{\tau}$, we have

$$
\mathcal{L}\left(\frac{X_{v}}{X_{u}}, v \in V_{\tau} \mid X_{u}>t\right) \xrightarrow{d} \mathcal{L}\left(M^{(u, \tau)}\right)=\mathcal{L}\left(M_{u v}, v \in V_{\tau}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}}: v \in V_{\tau}\right\}}
$$

The vector $M^{(u, \tau)}=\left(M_{u v}, v \in V_{\tau}\right)$ has dependent variables and the distribution of a single element is as follows.

1. The distribution of $M_{u v}$ when $(u, v) \in E$.
(a) If $u$ is the source node of $\tau$, the distribution is given by $\mathcal{L}\left(M_{u v}\right)=\delta_{\left\{c_{u v}\right\}}$.
(b) If $u$ is not the source node of $\tau$, the distribution is given by

$$
\mathcal{L}\left(M_{u v}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}}\right\}}
$$

2. The distribution of $M_{u v}$ when $(v, u) \in E$.
(a) If $v$ is the source node of $\tau$, the distribution is given by

$$
\mathcal{L}\left(M_{u v}\right)=c_{v u} \delta_{\left\{1 / c_{v u}\right\}}+\left(1-c_{v u}\right) \delta_{\{0\}}
$$

(b) If $v$ is not the source node of $\tau$, the distribution is given by

$$
\mathcal{L}\left(M_{u v}\right)=\sum_{j \in \operatorname{An}(v)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}}\right\}}+\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j} \delta_{\{0\}}
$$

According to Proposition 3.1, the factorization property (16) holds either for all nodes or for no node at all, a necessary and sufficient condition being that the ttt has a unique source. The principle of (16) is illustrated in Figure 3 for $u=8$. The limit $A^{(u)}=\left(A_{u v}, v \in V \backslash u\right)$ is given by

$$
\begin{aligned}
A_{87}=M_{87}, & A_{83}=M_{87} M_{73}, & A_{82}=M_{87} M_{73} M_{32} \\
& A_{86}=M_{87} M_{76}, & A_{81}=M_{87} M_{73} M_{31} \\
& A_{85}=M_{87} M_{75}, & A_{84}=M_{87} M_{73} M_{34}
\end{aligned}
$$

where $M^{\left(8, \tau_{4}\right)}=M_{87}, M^{\left(8, \tau_{3}\right)}=\left(M_{76}, M_{73}, M_{75}\right), M^{\left(8, \tau_{2}\right)}=M_{34}$ and $M^{\left(8, \tau_{1}\right)}=\left(M_{31}, M_{32}\right)$ are independent sub-vectors by construction.

What underlies the link between the factorization of the limiting variables from Proposition 3.1 on the one hand and the uniqueness of the source of the ttt on the other hand is the Markovianity of $X$ with respect to the skeleton graph $T$. The Markov property states that for any three non-empty and disjoint sets $A, B, C \subset V$ such that in the graph $T$ the nodes in $A$ are separated from the nodes in $B$ by the nodes in $C$, the vector $X_{A}=\left(X_{v}, v \in A\right)$ is conditionally independent from $X_{B}$ given $X_{C}$ (Lauritzen, 1996). Another equivalence condition can be added to the list in Proposition 3.1.

Proposition 3.3. Let $X$ follow a max-linear model with respect to the ttt $\mathcal{T}$ as in Assumption 2.1. Then $X$ satisfies the global Markov property with respect to the skeleton graph $T$ if and only if $\mathcal{T}$ has a unique source.

Even though in Proposition 3.3 we consider the undirected graph $T$ associated to the ttt $\mathcal{T}$, the recursive max-linear specification of $X$ is still with respect to the directed graph $\mathcal{T}$ itself. Indeed, the latter edges' directions are intrinsically determined by the recursive max-linear model specification of $X=\left(X_{v}\right)_{v \in V}$. When we also consider the associated skeleton graph $T$, i.e., without directions, it is because, in view of the factorization property in Proposition 3.1, we are interested in whether the global Markov property holds, a property which is most easily described in terms of the skeleton graph $T$.

The proof of Proposition 3.3 is based on notions and results from Améndola et al. (2022) which provides an extensive study of conditional independence properties of max-linear models. In particular, the notion of $*$-connecting path between two nodes in a DAG is introduced, a notion which is similar to the one of an active path (Koller and Friedman, 2009, Definition 3.6) between two nodes.

# 4 Latent variables and parameter identifiability 

In practice, it is possible that on some of the nodes, the variables of interest are not observed (latent). Examples from the literature are water heights on certain locations on the river networks of the Danube in Asadi et al. (2015) and the Seine in Asenova et al. (2021). We look at the problem of recovering all parameters of the distribution of the complete vector, based on the distribution of the observed variables only. If this is possible, we can study the parametric model as if all variables were observed: in particular, we are able to compute measures of tail dependence for sets including the unobserved variables. The latter is important as it may be the only possible way to quantify tail dependence, because non-parametric estimates are not available when dealing with unobserved variables.

Consider for instance the network in Figure 4. The max-linear model on $\mathcal{T}=(V, E)$ has eight variables and eleven parameters $\theta=\left(c_{e}, e \in E\right)$. By Proposition 4.2 below, the parameter $\theta \in \hat{\Theta}_{*}$ can be uniquely identified in case $X_{1}, X_{3}, X_{7}$ are not observed on the basis of the joint distribution of the remaining five variables, $X_{U}=\left(X_{2}, X_{4}, X_{5}, X_{6}, X_{8}\right)$.

The problem of parameter identifiability will be formalized on the level of the angular measure $H_{\theta}$ and is presented in detail in the next two subsections.

### 4.1 Graph-induced characteristics of the angular measure

In this subsection, we argue that the condition $\theta=\left(c_{e}, e \in E\right) \in \hat{\Theta}_{*}$ guarantees that all edge weights in $\theta$ are uniquely identifiable from the angular measure $H_{\theta}$ of $X=\left(X_{v}, v \in V\right)$ and thus from the distribution $P_{\theta}$ of $X$. Recall from (11) that $H_{\theta}$ is discrete with atoms $a_{i}=\left(a_{v i}\right)_{v \in V} \in \Delta_{V}$ and masses $m_{i}>0$.

Thanks to the assumption $\theta \in \hat{\Theta}_{*}$, we have

$$
a_{v i}>0 \Longleftrightarrow b_{v i}>0 \Longleftrightarrow i \in \operatorname{An}(v) \Longleftrightarrow v \in \operatorname{Desc}(i)
$$

For any DAG, all nodes have a different set of descendants, i.e.,

$$
\forall i, j \in V: i \neq j \Longrightarrow \operatorname{Desc}(i) \neq \operatorname{Desc}(j)
$$

Indeed, if $i \neq j$ and $\operatorname{Desc}(i) \subseteq \operatorname{Desc}(j)$, then $i \in \operatorname{desc}(j)$ and hence $j \notin \operatorname{desc}(i)$, so that $\operatorname{Desc}(j) \nsubseteq$ $\operatorname{Desc}(i)$.

Lemma 4.1. Let $\left(X_{v}, v \in V\right)$ follow a max-linear model as in Assumption 2.1, with parameter vector $\theta \in \hat{\Theta}_{*}$ and induced coefficient matrix $\left(b_{v i}\right)_{i, v \in V}$. Let $H_{\theta}=\sum_{i \in V} m_{i} \delta_{a_{i}}$ in (11) be its angular measure. Then
(1) $m_{i}>0$ for all $i \in V$;
(2) for any atom $a_{i}=\left(a_{v i}\right)_{v \in V}$, we have $a_{v i}>0$ if and only if $v \in \operatorname{Desc}(i)$. Specifically, all $|V|$ vectors $a_{i}$ are different and every atom can be matched uniquely to a node in $V$;
(3) for each edge $(i, v) \in E$, we have $c_{i v}=b_{v i} / b_{i i}=a_{v i} / a_{i i}$.

In particular, $\theta \in \hat{\Theta}_{*}$ is identifiable from $H_{\theta}$ and thus from $P_{\theta}$, i.e., for $\theta_{1} \neq \theta_{2} \in \hat{\Theta}_{*}$ we have $H_{\theta_{1}} \neq H_{\theta_{2}}$ and thus $P_{\theta_{1}} \neq P_{\theta_{2}}$.

In Lemma 4.1, if the edge $(i, v)$ is not critical, then there is another path, say $p^{\prime}$, from $i$ to $v$ with path product $c_{p^{\prime}} \geq c_{i v}$, and then we can further lower the value of $c_{i v}$ without changing the coefficients in (4), because they involve $c_{p^{\prime}}$ rather than $c_{i v}$, thus yielding the same measure $H_{\theta}$. This shows that without the criticality assumption, some edge weights may not be identifiable from $H_{\theta}$.

Example 2 (Unique zero patterns). In dimension $d=3$, consider an angular measure given by the following atoms and masses:

$$
\omega_{1}=\frac{1}{2.2}\left[\begin{array}{l}
0.8 \\
1 \\
0.4
\end{array}\right], \mu_{1}=2.2, \quad \omega_{2}=\frac{1}{0.5}\left[\begin{array}{c}
0 \\
0 \\
0.5
\end{array}\right], \mu_{2}=0.5, \quad \omega_{3}=\frac{1}{0.3}\left[\begin{array}{l}
0.2 \\
0 \\
0.1
\end{array}\right], \mu_{3}=0.3
$$

Consider the vectors $\beta_{j}=\mu_{j} \omega_{j}$ for $j \in\{1,2,3\}$. By Lemma 4.1, the unordered collection $\left\{\beta_{1}, \beta_{2}, \beta_{3}\right\}=$ $\left\{(0.8,1,0.4)^{\top},(0,0,0.5)^{\top},(0.2,0,0.1)^{\top}\right\}$ permits to recover the values of the coefficients in the maxlinear model

$$
X_{1}=c_{11} Z \vee c_{21} c_{22} Y, \quad X_{2}=c_{22} Y, \quad X_{3}=c_{13} c_{11} Z \vee c_{13} c_{21} c_{22} Y \vee c_{33} T
$$

with (known) edge set $E=\{(2,1),(1,3)\}$, and this due the presence of zeroes in the vectors. For the current example, argue as follows. The angular measure $H_{\theta}$ of $\left(X_{1}, X_{2}, X_{3}\right)$ has three atoms: atom $a_{Z}=b_{Z} / m_{Z}$ with $b_{Z}=\left(c_{11}, 0, c_{13} c_{11}\right)^{\top}$, atom $a_{Y}=b_{Y} / m_{Y}$ with $b_{Y}=\left(c_{21} c_{22}, c_{22}, c_{13} c_{21} c_{22}\right)^{\top}$, and atom $a_{T}=b_{T} / m_{T}$ with $b_{T}=\left(0,0, c_{33}\right)^{\top}$. As unordered sets, $\left\{\beta_{1}, \beta_{2}, \beta_{3}\right\}$ and $\left\{b_{Z}, b_{Y}, b_{T}\right\}$ are equal, but the question is which vector $\beta_{j}$ corresponds to which vector $b_{*}$. From an inspection of the zero entries of the vectors, it is easily seen that the only possibility to identify the three coefficient vectors $\beta_{1}, \beta_{2}, \beta_{3}$ with the vectors $b_{Z}, b_{Y}, b_{T}$ of the angular measure $H_{\theta}$ is

$$
\beta_{1}=\left[\begin{array}{l}
0.8 \\
1 \\
0.4
\end{array}\right]=\left[\begin{array}{c}
c_{21} c_{22} \\
c_{22} \\
c_{13} c_{21} c_{22}
\end{array}\right]=b_{Y}, \quad \beta_{2}=\left[\begin{array}{c}
0 \\
0 \\
0.5
\end{array}\right]=\left[\begin{array}{c}
0 \\
0 \\
c_{33}
\end{array}\right]=b_{T}, \quad \beta_{3}=\left[\begin{array}{l}
0.2 \\
0 \\
0.1
\end{array}\right]=\left[\begin{array}{c}
c_{11} \\
0 \\
c_{13} c_{11}
\end{array}\right]=b_{Z}
$$

Solving the equations yields $\left(c_{11}, c_{21}, c_{22}, c_{13}, c_{33}\right)=(0.2,0.8,1,0.5,0.5)$.

# 4.2 Identifiability issues with the angular measure of a subvector 

When we deal with latent variables, we know the distribution of the observable variables only, $X_{U}=\left(X_{v}, v \in U\right)$ for non-empty $U \subset V$. The angular measure, say $H_{\theta, U}$, of $X_{U}$ in (12) is discrete and takes the form

$$
H_{\theta, U}=\sum_{r=1}^{s} \mu_{r} \delta_{\omega_{r}}
$$

with masses $\mu_{r}>0$ and $s$ distinct atoms $\omega_{r} \in \Delta_{U}$. Combining (12) and (20), we should have

$$
\sum_{r=1}^{s} \mu_{r} \delta_{\omega_{r}}=\sum_{i \in V} m_{i, U} \delta_{a_{i, U}}
$$

which means that, as sets, we should have $\left\{\omega_{1}, \ldots, \omega_{s}\right\}=\left\{a_{i, U}: i \in V\right\}$. In contrast to the situation in Lemma 4.1, the subvectors $a_{i, U}$ for $i \in V$ are not necessarily all different. Any atom $\omega_{r}$ of $H_{\theta, U}$

![img-3.jpeg](img-3.jpeg)

Figure 4: In the following ttt, the nodes that are allowed to contain a latent variable while the edge parameters remain identifiable are $1,3,7$. These are the only nodes where each of them satisfies both (I1) and (I2). For instance, if node 2 has unobserved variables, the parameters attached to edges $(1,2),(3,2)$ are not identifiable. This is because the edge weights $c_{12}, c_{32}$ take part only in products over paths ending at 2. But if $2 \in \bar{U}$ these coefficients disappear from the atoms of the angular measure $a_{i, U}=\left(b_{v i} / m_{i, U}, v \in U\right)$ and accordingly from the collection of vectors $\mathcal{B}_{\theta, U}$.
is of the form $a_{i, U}=\left(b_{v i} / m_{i, U}\right)_{v \in U}$ for one or possibly several indices $i \in V$. For $r=1, \ldots, s$ and $i \in V$ such that $\omega_{r}=a_{i, U}$, we know from (18) that

$$
\left\{v \in U: \omega_{r, v}>0\right\}=\operatorname{Desc}(i) \cap U
$$

The (unordered) collection of vectors $\left\{\left(b_{v i}\right)_{v \in U}: i \in V\right\}$ will be denoted by $\mathcal{B}_{\theta, U}$.
With unobservable variables, there are several issues with the angular measure and its expression on the right hand-side of (21).

- Zero masses. We have $m_{i, U}=\sum_{v \in U} b_{v i}$, so that if all components of $\left(b_{v i}\right)_{v \in U}$ are zero, then $m_{i, U}=0$. This happens when $\operatorname{Desc}(i) \cap U=\varnothing$. In this case, we have $s<|V|$, i.e., $H_{\theta, U}$ has less atoms than $H_{\theta}$.
- Equal atoms. We may have $a_{i, U}=a_{j, U}$ for some indices $i, j \in V$ and $i \neq j$. In this case, the terms $i$ and $j$ in (12) are to be aggregated and again, $H_{\theta, U}$ has less than $|V|$ atoms, $s<|V|$. This happens when the vectors $\left(b_{v i}, v \in U\right)$ and $\left(b_{v j}, v \in U\right)$ are proportional for some distinct $i, j \in V$.
- Zeroes on the same positions. A more subtle problem occurs when for two distinct vectors $b, b^{\prime} \in \mathcal{B}_{\theta, U}$, the supports $\left\{v \in U: b_{v}>0\right\}$ and $\left\{v \in U: b_{v}^{\prime}>0\right\}$ are equal. Such a situation arises when two distinct nodes $i, j \in V$ satisfy $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$. The latter equality is only possible in the presence of latent variables and is to be contrasted with property (19) when all variables are observable.


# 4.3 Identifiability criterion 

For a max-linear model with respect to a ttt $\mathcal{T}=(V, E)$ with unique source, we need conditions that ensure that the minimal representation of the angular measure of $X_{U}$ is the one in (12). Consider the following two conditions for the set of nodes $\bar{U}=V \backslash U$ carrying latent variables:
(I1) any $u \in \bar{U}$ has at least two children;
(I2) any $u \in \bar{U}$ is the source of some tournament in $\mathcal{T}$.
Proposition 4.2. Let $X$ follow a max-linear model as in Assumption 2.1 with respect to a ttt $\mathcal{T}=(V, E)$ with unique source. For a non-empty node set $U \subset V$, the parameter $\theta \in \bar{\Theta}_{*}$ is uniquely identifiable from the distribution of $\left(X_{v}, v \in U\right)$ if and only if conditions (I1) and (I2) are satisfied.

Figure 4 illustrates the identifiability criterion.

## 5 Discussion

In this paper we have considered a Bayesian max-linear network over a special type of graph which we called a tree of transitive tournaments (ttt). It is a graph which collects in an acyclic manner transitive tournaments which are themselves complete DAGs. The max-linear model is defined on

a particular parameter space which ensures that the impact from one variable to another takes place along the shortest path, a consideration that has been defined in the literature as the path's criticality. It turns out that a ttt with unique source leads to a graph without v-structures, that is, no node has non-adjacent parents. The limit of the scaled random vector, conditional on the event that a high threshold is exceeded at a particular node, is shown to be factorizable in independent multiplicative increments if and only if the ttt has a unique source. This result is analogous to that for Markov trees in Segers (2020b) and for Markov random fields on undirected block graphs in Asenova and Segers (2023). The property that the Bayesian max-linear model on a ttt with unique source shares with these two other models is that it satisfies the global Markov property with respect to the undirected counterpart or skeleton graph of the ttt.

In addition, we have provided a simple necessary and sufficient criterion guaranteeing the identifiability of the edge coefficients in case some variables are latent. As suggested by a Reviewer, it may be possible to extend the criterion to partial identifiability of some edge weights in case the criterion is fulfilled only locally.

Upon appropriate modifications, we expect the results presented in this paper to hold equally for the linear additive causal model introduced in Gnecco et al. (2021). One of the reasons is that the max-domain of attraction of a linear model with heavy-tailed factors is the same as that of a max-linear one (Einmahl et al., 2012). However, the relation between the edge weights $\theta=\left(c_{e}\right)_{e \in E}$ and the coefficient matrix $B_{\theta}=\left(b_{i j}\right)_{i, j \in V}$ is different between the max-linear and additive linear versions, and this may ask for different approaches in showing the same properties for the additive version.

# A Trees of transitive tournaments 

Recall that in a directed acyclic graph, a v-structure refers to a node with parents that are not adjacent, see Figure 1.

## A. 1 Proof of Lemma 2.3

Proof. 1. Let $a, b \in V$. If $a$ and $b$ share the same tournament, they must be connected by an arrow, which is then the unique shortest path between them, since all other possible paths have length larger than one.

Let $a, b$ be nonadjacent. If there is a unique directed path between $a$ and $b$ then this is the unique shortest path. Suppose now there are two shortest paths: $p_{1}, p_{2} \in \pi(a, b)$. Let the path $p_{1}$ be along the vertices $\left\{v_{1}=a, v_{2}, \ldots, v_{n}=b\right\}$ and the path $p_{2}$ on along the vertices $\left\{u_{1}=a, u_{2}, \ldots, u_{n}=b\right\}$.

We will proceed by contradiction. Assume $v_{2} \neq u_{2}$. If $v_{2}$ and $u_{2}$ belong to two different tournaments, then there exists a non-directed cycle through nodes in different tournaments, namely $\left\{a, v_{2}, \ldots, b, \ldots, u_{2}, a\right\}$. But this is impossible by property (P2) of a ttt. Hence, $v_{2}$ and $u_{2}$ must belong to the same tournament, say $\tau_{a}$, because $a$ is part of the same tournament too. Now consider $u_{3}$ and $v_{3}$. Then either $u_{3}=v_{3}$ or they share a tournament, say $\tau_{3}$, because otherwise there exists a non-directed cycle through nodes in different tournaments. Since $\left(v_{2}, v_{3}\right) \in E$ and $\left(u_{2}, u_{3}\right) \in E$ and by the assumption that $v_{2} \neq u_{2}$, all four nodes $\left\{a, v_{2}, u_{2}, v_{3}=u_{3}\right\}$ or all five nodes $\left\{a, v_{2}, u_{2}, v_{3}, u_{3}\right\}$ belong to $\tau_{a}$. This is because by property (P1), two tournaments can share only one node, hence it is impossible to have $\tau_{3} \cap \tau_{a}=\left\{v_{2}, u_{2}\right\}$. Because all four or five nodes belong to the same tournaments and since $\left(a, v_{2}\right),\left(v_{2}, v_{3}\right),\left(a, u_{2}\right),\left(u_{2}, u_{3}\right) \in E$ we must have $\left(a, v_{3}\right) \in E$ and $\left(a, u_{3}\right) \in E$ to avoid intertournament undirected cycles. Hence the paths $\left\{a=v_{1}, v_{3}, \ldots, v_{n}=b\right\}$ and $\left\{u_{1}=a, u_{3}, \ldots, u_{n}=b\right\}$ are shorter then $p_{1}$ and $p_{2}$, a contradiction. Hence we must have $v_{2}=u_{2}$.

We apply the same strategy to the nodes $v_{3}, u_{3}$ and $v_{4}, u_{4}$ to find that $v_{3}=u_{3}$. Proceeding recursively, we conclude that $p_{1}=p_{2}$.
2. First we show that if the ttt has a unique source, there cannot be a v-structure. We proceed by contraposition. Assume that there is a node, $v$, with parents in two different tournaments $\tau_{a}$ and $\tau_{b}$. Let $a$ and $b$ be the sources of $\tau_{a}$ and $\tau_{b}$ respectively (Harary and Moser, 1966, Corollary 5a). Note that we definitely have $v \neq a$ and $v \neq b$. From node $v$ go to node $a$. If $a$ doesn't have a parent from another tournament we have found one node with zero in-degree with respect to the whole graph. If $a$ has parent(s) from another tournament, say $\tau_{a}^{\prime}$, then go to the node that within $\tau_{a}^{\prime}$ has in-degree zero, say node $a^{\prime}$. Keep on going until you find a node with in-degree zero within the whole

graph - such a node must exist because the graph is finite. Repeat the same for $\tau_{b}$, yielding two different nodes having zero in-degree with respect to whole graph. These nodes must be different because of the definition of $\mathcal{T}$ : since we have started in two different tournaments $\tau_{a}$ and $\tau_{b}$ we cannot end up in the same node, or otherwise there would be a non-directed cycle passing through $v$ and that node. Hence we have found two nodes with zero in-degree, hence $\mathcal{T}$ does not have a unique source node.

Next we show that if $\mathcal{T}$ has two or more source nodes, $u$ and $v$, then there is a v-structure. Because $u$ and $v$ are sources they have in-degree zero, so that they cannot belong to the same tournament, and thus they belong to two different tournaments. Consider the unique shortest trail between $u, v$ on a sequence of nodes $\left\{u=v_{1}, v_{2}, \ldots, v_{n}=v\right\}$. Such a trail exists as, by definition of a ttt, the skeleton of $\mathcal{T}$ is a block graph and the fact that in a block graph there is a unique shortest path between every two nodes (Behtoei et al., 2010, Theorem 1). For every two consecutive nodes in the shortest path, $v_{i}, v_{i+1}$, we have either $\left(v_{i}, v_{i+1}\right) \in E$ or $\left(v_{i+1}, v_{i}\right) \in E$. Because $u$ and $v$ are sources of $\mathcal{T}$, we have $\left(u, v_{2}\right) \in E$ and $\left(v, v_{n-1}\right) \in E$. Note that $n \geq 3$, since $u$ and $v$ cannot be adjacent. We need three nodes $v_{i}, v_{i+1}, v_{i+2}$ such that $\left(v_{i}, v_{i+1}\right) \in E$ and $\left(v_{i+2}, v_{i+1}\right) \in E$. If $n=3$, then the triple $\left(u, v_{2}, v\right)$ already fulfils the requirement. If $n \geq 4$, then continue from $v_{2}$ as follows. Let $i=\max \left\{j=1, \ldots, n-2:\left(v_{j}, v_{j+1}\right) \in E\right\}$; then $\left(v_{i}, v_{i+1}\right) \in E$ and $\left(v_{i+2}, v_{i+1}\right) \in E$, as required. Because this is the shortest trail, $v_{i}$ and $v_{i+2}$ cannot belong to the same tournament, since otherwise there would exist a shorter trail passing only through $v_{i}$ and $v_{i+2}$.
3. Suppose that $v \in \operatorname{Desc}(i) \cap \operatorname{Desc}(j)$ but also both $i \notin \operatorname{an}(j)$ and $j \notin \operatorname{an}(i)$; in particular, $i$ and $j$ do not belong to the same tournament. Consider the paths $p(i, v)$ and $p(j, v)$. Along each path, continue walking upwards considering successive parents. Since the graph is finite, this walk must end for both paths to a node without parents. By assumption, this must be the same unique source node of the ttt, say $u_{0}$. We will thus have found two different paths from $u_{0}$ to $v$, one passing via $i$ and the other one via $j$. However, as $i$ and $j$ do not belong to the same tournament, this is in contradiction to property (P2) of a ttt.

# A. 2 Proof of Lemma 2.4 

Proof. 1. Suppose that there is a node $v_{r}$, for $r \in\{2, \ldots, n-1\}$, which is not the source node in the tournament shared with $v_{r+1}$, say $\tau$. Let $\bar{v}$ be a parent of $v_{r}$ in $\tau$. Note that $\bar{v}$ must be a parent of $v_{r+1}$ too, because of the out-degree ordering in a tournament. Because $v_{r-1}$ is a parent of $v_{r}$ too, both $v_{r-1}$ and $\bar{v}$ must belong to $\tau$, since otherwise $v_{r}$ would have parents from different tournaments, which is impossible according to Lemma 2.3-2. Hence $v_{r-1}, v_{r}, \bar{v}, v_{r+1}$ all belong to the same tournament, i.e., to $\tau$. Necessarily $v_{r-1}$ is a parent of $v_{r+1}$, because otherwise there would be a directed cycle $\left\{v_{r-1}, v_{r}, v_{r+1}, v_{r-1}\right\}$. But then $\left\{v_{1}, \ldots, v_{r-1}, v_{r+1}, \ldots, v_{n}\right\}$ is a shorter path between $v_{1}$ and $v_{n}$, in contradiction to the hypothesis.
2. Let the shortest trail between $u$ and $v$ be the one along the node sequence $\left\{v_{1}=u, \ldots, v_{n}=v\right\}$. It is sufficient to show that there cannot exist a node $v_{r}$ for $r \in\{2, \ldots, n-1\}$ such that $\left(v_{r-1}, v_{r}\right) \in E$ and $\left(v_{r+1}, v_{r}\right) \in E$. Suppose indeed that the converse were true, i.e., there exists $r \in\{2, \ldots, n-1\}$ such that both $v_{r-1}$ and $v_{r+1}$ are parents of $v_{r}$. Then $v_{r-1}$ and $v_{r+1}$ must be adjacent because v-structures are excluded by statement 2 of Lemma 2.3. But then $\left\{v_{1}, \ldots, v_{r-1}, v_{r+1}, \ldots, v_{n}\right\}$ is a shorter trail between $u$ and $v$, yielding a contradiction.

## B Proofs and additional results for Section 3

Proof. From Segers (2020b, Example 1) we have the limit

$$
\sum_{j \in V} b_{u j} \delta_{\left\{\frac{b_{u j}}{b_{u j}}, v \in V_{r}\right\}}
$$

Adapting this representation to a model where we have $b_{u j}=0$ for $j \notin \operatorname{An}(u)$ and $b_{i j}=c_{p(j, i)} b_{j j}$ for $j \in \operatorname{An}(i)$ we obtain

$$
\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, u)} b_{j j}}{c_{p(j, u)} b_{j j}}, v \in V_{r}\right\}}
$$

Recall that $c_{p(i, i)}=1$ and $c_{p(i, j)}=0$ if $i \notin \operatorname{An}(j)$.

Next we show that $\left(M_{u v}, v \in V_{\tau}\right)$ are mutually dependent. When $u$ is the source of $\tau$ then for every $j \in \operatorname{An}(u)$ the atom

$$
\left(\frac{c_{p(j, u)}}{c_{p(j, u)}}, v \in V_{\tau}\right)=\left(\frac{c_{p(j, u)} c_{u v}}{c_{p(j, u)}}, v \in V_{\tau}\right)=\left(1 ; c_{u v}, v \in V_{\tau} \backslash u\right)
$$

gets probability $\sum_{j \in \operatorname{An}(u)} b_{u j}=1$. Hence $\left(M_{u v}, v \in V_{\tau}\right)$ are at the same time perfectly dependent and independent.

For $u$ which is not the source node the general idea is to take a collection of coordinates with joint probability zero, and positive product of the marginal probabilities, thus showing that the joint probability does not equal the product of marginal probabilities for selected possible value of the random vector.

Let for brevity $V_{\tau}=\{1,2, \ldots, m\}$ : the nodes are labelled according to their order of out-degrees within $\tau$ : the source node of $\tau$ has $m-1$ (largest) out-degree and is labelled by 1 , the node with out-degree $m-2$ is labelled as 2 , etc.

Consider $u$ being the node 2. We have, thanks to the no-cycle property within a tournament $\operatorname{An}(2)=\operatorname{An}(1) \cup\{2\}$. For all $j \in \operatorname{An}(1)$ we have

$$
\left(\frac{c_{p(j, v)}}{c_{p(j, 2)}}, v=1, \ldots, m\right)=\left(\frac{1}{c_{12}} ; 1 ; \frac{c_{p(j, 1)} c_{1 v}}{c_{p(j, 1)} c_{12}}, v=3, \ldots, m\right)
$$

which is an atom of $\left(M_{2 v}, v=1, \ldots, m\right)$ with mass $\sum_{j \in \operatorname{An}(1)} b_{2 j}$. This means that for the marginal distribution of $M_{21}$ we have $\mathbb{P}\left(M_{21}=1 / c_{12}\right) \geq \sum_{j \in \operatorname{An}(1)} b_{2 j}$. For $j=2$ we have an atom $\left(0,1, c_{23}, \ldots, c_{2 m}\right)$ with mass $b_{22}$. This means that for the marginal probabilities of $\left(M_{23}, \ldots, M_{2 m}\right)$ we have $\mathbb{P}\left(M_{2 v}=c_{2 v}\right) \geq b_{22}$ for all $v=3, \ldots, m$. Take a vector of coordinates $\left(1 / c_{12}, 1, c_{23}, \ldots, c_{2 m}\right)$. Note that this vector cannot be the same as the one in (23). For any $v=3, \ldots, m$ we cannot have $c_{1 v} / c_{12}=c_{2 v}$ because of the criticality assumption, according to which $c_{1 v}>c_{12} c_{2 v}$ for any $v=3, \ldots, m$. The joint probability of this vector of coordinates is

$$
\mathbb{P}\left(M_{21}=1 / c_{12}, M_{22}=1, M_{23}=c_{23}, \ldots, M_{2 m}=c_{2 m}\right)=0
$$

However the product of marginal probabilities is positive:

$$
\mathbb{P}\left(M_{21}=1 / c_{12}\right) \mathbb{P}\left(M_{22}=1\right) \prod_{v=3}^{m} \mathbb{P}\left(M_{2 v}=c_{2 v}\right) \geq \sum_{j \in \operatorname{An}(1)} b_{2 j} \times b_{22}^{m-1}>0
$$

Now let $u \geq 3$. Take the vector of coordinates in (17) corresponding to $j=1$ which is equal to $\left(1 / c_{1 u}, c_{12} / c_{1 u}, \ldots, c_{1 m} / c_{1 u}\right)$ and has probability at least $b_{u 1}$. Consider also the vector of coordinates for $j=u$ which is $\left(0, \ldots, 0,1 ; c_{u v}, v=u+1, \ldots, m\right)$ with mass at least $b_{u u}$. Replace the first coordinate by $1 / c_{1 u}$. The vector obtained in this way has joint probability zero. For every $j \in \mathrm{pa}(u)$ we have $b_{v j} / b_{u j}=0$ when $v$ is not child of $j$ or equivalently, given the order in the node labelling, when $v<j$. So for fixed $u \geq 3$, for $j=1$ the vector $\left(b_{v j} / b_{u j}, v=1, \ldots, m\right)$ has no zeros. For $j=2$ the vector $\left(b_{v j} / b_{u j}, v=1, \ldots, m\right)$ has one zero, namely $\left(0 ; b_{v j} / b_{u j}, v=2, \ldots, m\right)$, for $j=3$ the vector $\left(b_{v j} / b_{u j}, v=1, \ldots, m\right)$ has two zeros, namely $\left(0,0 ; b_{v j} / b_{u j}, v=3, \ldots, m\right)$ and so on until $j=u$ with the corresponding vector $\left(b_{v j} / b_{u j}, v=1, \ldots, m\right)=\left(0, \ldots, 0 ; b_{v j} / b_{u j}, v=u, \ldots, m\right)$. By replacing the first coordinate by a non-zero value in this vector we get an impossible value for the random vector $\left(M_{u v}, v=1, \ldots, m\right)$ or a value with probability zero. Considering the univariate marginal distributions of $\left(M_{u v}, v=1, \ldots, m\right)$ we obtain for the product of marginal probabilities a positive value:

$$
\mathbb{P}\left(M_{u 1}=1 / c_{1 u}\right)\left[\prod_{v=2}^{u-1} \mathbb{P}\left(M_{u v}=0\right)\right] \mathbb{P}\left(M_{u u}=1\right) \prod_{v=u+1}^{m} \mathbb{P}\left(M_{u v}=c_{u v}\right) \geq b_{u 1} \times b_{u u}^{m-1}>0
$$

This shows that for any $u \in V_{\tau}$ the vector $\left(M_{u 1}, \ldots, M_{u m}\right)$ has jointly dependent elements.
Next we show the distribution of a single element $M_{u v}, v \in V_{\tau} \backslash u$.

1. Consider first when $u$ is the source node in $\tau$. Since $(u, v) \in E$, we have $\operatorname{An}(u) \subset \operatorname{An}(v)$ and thus $\operatorname{An}(v) \cap \operatorname{An}(u)=\operatorname{An}(u)$. We have $b_{v j}>0, j \in \operatorname{An}(u)$, hence zero is not a possible value of $M_{u v}$. For $j \in \operatorname{An}(u)$

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, u)} c_{u v} b_{j j}}{c_{p(j, u)} b_{j j}}=c_{u v}
$$

and since $\sum_{j \in \operatorname{An}(u)} b_{u j}=1$ we obtain the desired result under 1.(a).
When $u$ is not the source node in $\tau$ not all shortest paths to $v$ pass through $u$ hence for $j \in \operatorname{An}(u)$ we have

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, u)}}>0
$$

with mass $b_{u j}$. Hence the result in 1.(b). Note that zero is not possible value as we still have $\operatorname{An}(u) \subset \operatorname{An}(v)$. Also $c_{p(u, u)}=1$ by convention.
2. Let us have now $(v, u) \in E$. In this case $\operatorname{An}(u) \backslash \operatorname{An}(v)$ is not empty because it contains at least the node $u$, so zero is a possible value of $M_{u v}$. We need to distinguish only the zero atoms from the non-zero ones. When $v$ is a source node in $\tau$, we have, for $j \in \operatorname{An}(v)$

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, v)} c_{v u}}=\frac{1}{c_{v u}}>0
$$

which is an atom with probability

$$
\sum_{j \in \operatorname{An}(v)} b_{u j}=\sum_{j \in \operatorname{An}(v)} c_{p(j, v)} c_{v u} b_{j j}=c_{v u} \sum_{j \in \operatorname{An}(v)} c_{p(j, v)} b_{j j}=c_{v u} \sum_{j \in \operatorname{An}(v)} b_{v j}=c_{v u}
$$

The probability of the zero atom is $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(v)} b_{u j}=1-c_{v u}$. This shows 2.(a).

When $v$ is not a source node of $\tau$ we have for $j \in \operatorname{An}(v)$

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, u)}}>0
$$

an atom with mass $b_{u j}$ and zero atom with probability $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j}$. This shows 2.(b).

Remark. From the results in Lemma 3.2 we see that a multiplicative increment does not have a degenerate distribution at zero, so that a product of several such multiplicative increments cannot be degenerate at zero either. This is an important observation that we will use in further proofs.

Lemma B.1. Let $\left(X_{v}, v \in V\right)$ follow a max-linear model as in Assumption 2.1. Let $\mathcal{T}$ have a unique source. For any $u \in V$ we have

$$
\mathcal{L}\left(\frac{X_{v}}{X_{u}}, v \in V \mid X_{u}>t\right) \xrightarrow{d} \mathcal{L}\left(A_{u v}, v \in V\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}, v \in V}\right\}}
$$

The distribution of $A_{u v}$ depends on the three types of possible trails according to Lemma 2.4-2. In what follows we assume $(u, v) \notin E$. For the case $(u, v) \in E$ see Lemma 3.2.

1. Distribution of $A_{u v}$ on a path $\left\{u=v_{1}, r=v_{2}, \ldots, v=v_{n}\right\}$ with $u, r \in \tau$, one of the tournaments of $\mathcal{T}$.
(a) If $u$ is a source node in $\tau$ then $\mathcal{L}\left(A_{u v}\right)=\delta_{\left\{c_{p(u, v)}\right\}}$.
(b) If $u$ is not a source node in $\tau$ we have

$$
\mathcal{L}\left(A_{u v}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}, c_{p(r, v)}}\right\}}
$$

2. Distribution of $A_{u v}$ on a path $\left\{v=v_{1}, r=v_{2}, \ldots, u=v_{n}\right\}$ with $v, r \in \tau$.
(a) If $v$ is a source node in $\tau$ then

$$
\mathcal{L}\left(A_{u v}\right)=c_{p(v, u)} \delta_{\left\{\frac{1}{c_{p(v, u)}}\right\}}+\left(1-c_{p(v, u)}\right) \delta_{\{0\}}
$$

(b) If $v$ is not a source node in $\tau$ then

$$
\mathcal{L}\left(A_{u v}\right)=\sum_{j \in \operatorname{An}(v)} c_{p(r, u)} b_{r j} \delta_{\left\{\frac{c_{p(j, u)}}{c_{p(j, r)} c_{p(r, u)}}\right\}}+\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j} \delta_{\{0\}}
$$

3. The distribution of $A_{u v}$ on a trail composed of two paths $p(r, u)$ and $p(r, v)$. Let the trail be on nodes $\{u, \ldots, m, r, n, \ldots, v\}$. Let also $\tau_{m}, \tau_{n}$ be two tournaments with $r, m \in \tau_{m}$ and $r, n \in \tau_{n}$.
(a) If $r$ is source in both $\tau_{m}$ and $\tau_{n}$, then

$$
\mathcal{L}\left(A_{u v}\right)=c_{p(r, u)} \delta_{\left\{\frac{c_{p(r, u)}}{c_{p(r, u)}}\right\}}+\left(1-c_{p(r, u)}\right) \delta_{\{0\}}
$$

(b) If $r$ is source in $\tau_{m}$, but not in $\tau_{n}$, then

$$
\mathcal{L}\left(A_{u v}\right)=\sum_{j \in \operatorname{An}(r)} c_{p(r, u)} b_{r j} \delta_{\left\{\frac{c_{p(j, u)} c_{p(r, u)}}{c_{p(j, r)} c_{p(r, u)}}\right\}}+\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j} \delta_{\{0\}}
$$

(c) If $r$ is source in $\tau_{n}$, but not in $\tau_{m}$, then

$$
\mathcal{L}\left(A_{u v}\right)=\sum_{j \in \operatorname{An}(r)} c_{p(m, u)} b_{m j} \delta_{\left\{\frac{c_{p(j, v)} c_{p(r, v)}}{c_{p(j, m)} c_{p(m, u)}}\right\}}+\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j} \delta_{\{0\}}
$$

Proof. We have already seen that from Segers (2020b, Example 1) we have the limit

$$
\mathcal{L}\left(\frac{X_{v}}{X_{u}}, v \in V \mid X_{u}>t\right) \xrightarrow{d} \sum_{j \in V} b_{u j} \delta_{\left\{\frac{b_{v j}}{b_{u j}}, v \in V\right\}}
$$

Adapting this representation to a model where we have $b_{u j}=0$ for $j \notin \operatorname{An}(u)$ and $b_{i j}=c_{p(j, i)} b_{j j}$ for $j \in \operatorname{An}(i)$ we obtain

$$
\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, u)}}{c_{p(j, u)}}, v \in V\right\}}
$$

Recall that $c_{p(i, i)}=1$ and $c_{p(i, j)}=0$ if $i \notin \operatorname{An}(j)$. For a single $v \in V \backslash u$ we have the marginal distribution

$$
\mathcal{L}\left(A_{u v}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{b_{v j}}{b_{u j}}\right\}}
$$

The distribution of $A_{u v}$ depends deterministically on properties of the ttt. When $\mathcal{T}$ has a unique source, according to Lemma 2.4-2 there are three possible shortest trails between two nodes. In addition we have also the property under Lemma 2.4-1. We look at the different distributions of $A_{u v}$ that arise due to these two properties of the ttt.

First we deal with 1.(a). Since $\operatorname{An}(u) \subset \operatorname{An}(v)$ all atoms in (25) are positive and zero is not a possible value of $A_{u v}$. All paths from $\operatorname{An}(u)$ to $v$ pass through $u$ because $u$ is source in $\tau$ and because by property (P2) of a ttt no cycle involving several tournaments is allowed. The case is illustrated by the graph below.
![img-4.jpeg](img-4.jpeg)

Hence for all $j \in \operatorname{An}(u)$ we have

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, u)} c_{p(u, v)}}{c_{p(j, u)}}=c_{p(u, v)}>0
$$

with mass $\sum_{j \in \operatorname{An}(u)} b_{u j}=1$.
Next we show 1.(b). Because $\operatorname{An}(u) \subset \operatorname{An}(v)$, zero is not possible value of $A_{u v}$. Not all shortest paths from $\operatorname{An}(u)$ to $v$ pass through $u$ because $u$ is not source in $\tau$. However all paths from $\operatorname{An}(u)$ to $v$ pass through $r$, as shown in the picture. Paths from $\operatorname{An}(u)$ to $v$ other than these passing through $u$ or $r$ are impossible because of the property (P2) of a ttt.

![img-5.jpeg](img-5.jpeg)

We have for $j \in \operatorname{An}(u)$

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, u)}} c_{p(r, v)}>0
$$

with mass $b_{u j}$, hence the expression in 1.(b).
Next we show 2.(a). When the directed path is from $v$ to $u$ the set $\operatorname{An}(u) \backslash \operatorname{An}(v)$ contains at least $u$ hence we have $b_{v j}=0$ for all $j \in \operatorname{An}(u) \backslash \operatorname{An}(v)$. This means that zero is a possible value of $A_{u v}$. All shortest paths from $j \in \operatorname{An}(v)$ to $u$ pass through $v$ as $v$ is source in $\tau$. Otherwise, there would be cycle encompassing multiple tournaments, which is not allowed under property (P2) of a ttt.
![img-6.jpeg](img-6.jpeg)

For $j \in \operatorname{An}(v)$ the non-zero atom is given by

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, v)} c_{p(v, u)}}=\frac{1}{c_{p(v, u)}}>0, \quad j \in \operatorname{An}(v)
$$

with mass

$$
\sum_{j \in \operatorname{An}(v)} b_{u j}=\sum_{j \in \operatorname{An}(v)} c_{p(j, v)} c_{p(v, u)} b_{j j}=c_{p(v, u)} \sum_{j \in \operatorname{An}(v)} c_{p(j, v)} b_{j j}=c_{p(v, u)} \sum_{j \in \operatorname{An}(v)} b_{v j}=c_{p(v, u)}
$$

For the zero atom we have probability $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(v)} b_{u j}=1-c_{p(v, u)}$. This shows 2.(a).

To show 2.(b) we note that when $v$ is not a source node of $\tau$ not all shortest paths from $j \in \operatorname{An}(v)$ to $u$ pass through $v$. However all paths from $j \in \operatorname{An}(v)$ to $u$ pass through $r$, as it can be seen from the figure here.
![img-7.jpeg](img-7.jpeg)

Hence for $j \in \operatorname{An}(v)$ we have

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, v)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, v)}}{c_{p(j, r)} c_{p(r, u)}}>0
$$

which is an atom with mass $b_{u j}=c_{p(j, r)} c_{p(r, u)} b_{j j}=c_{p(r, u)} b_{r j}$. The zero atom comes from the fact that $b_{v j}=0$ for all $j \in \operatorname{An}(u) \backslash \operatorname{An}(v)$, and it has probability $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j}$. This shows the distribution under 2.(b).

By Lemma 2.4-1 the node $r$, as part of the paths $p(r, u)$ is allowed not be a source node in $\tau_{m}$. Similarly considering the path $p(r, v)$. However when we combine $p(r, u)$ and $p(r, v)$ in one trail $t(u, v)$ the node $r$ should be a source in at least one of $\tau_{m}$ and $\tau_{n}$. If $r$ is not source of both $\tau_{m}$ and $\tau_{n}$ then there would be indeed a v-structure. However, Lemma 2.3-2 excludes v-structures when $\mathcal{T}$ has a unique source, hence node $r$ should be source in at least one tournament, $\tau_{m}$ and/or $\tau_{n}$.

To show 3.(a) we note that all paths from $j \in \operatorname{An}(r)$ to $u$ and to $v$ pass through $r$, as $r$ is source in both $\tau_{n}$ and $\tau_{m}$. The case is depicted in the following picture.

![img-8.jpeg](img-8.jpeg)

Also we have $b_{v j}=0$ for all $j \in \operatorname{An}(u) \backslash \operatorname{An}(r)$. For $j \in \operatorname{An}(r)$ we have

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, r)} c_{p(r, v)} b_{j j}}{c_{p(j, r)} c_{p(r, u)} b_{j j}}=\frac{c_{p(r, v)}}{c_{p(r, u)}}>0
$$

with probability

$$
\sum_{j \in \operatorname{An}(r)} b_{u j}=\sum_{j \in \operatorname{An}(r)} c_{p(j, r)} c_{p(r, u)} b_{j j}=c_{p(r, u)} \sum_{j \in \operatorname{An}(r)} c_{p(j, r)} b_{j j}=c_{p(r, u)} \sum_{j \in \operatorname{An}(r)} b_{r j}=c_{p(r, u)}
$$

The probability of the zero atom is $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(r)} b_{u j}=1-c_{p(r, u)}$.
Next we show 3.(b). Because $r$ is not a source in $\tau_{n}$ not all paths from $\operatorname{An}(r)$ to $v$ pass through $r$, but they do all pass through $n$. Also all paths from $\operatorname{An}(r)$ to $u$ pass through $r$ because $r$ is source in $\tau_{m}$.
![img-9.jpeg](img-9.jpeg)

Hence for $j \in \operatorname{An}(r)$

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, u)} c_{p(n, v)} b_{j j}}{c_{p(j, r)} c_{p(r, u)} b_{j j}}=\frac{c_{p(j, u)} c_{p(n, v)}}{c_{p(j, r)} c_{p(r, u)}}>0
$$

which is an atom with mass $b_{u j}=c_{p(j, r)} c_{p(r, u)} b_{j j}=b_{r j} c_{p(r, u)}$. The zero atom has probability equal to $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j}$.

Next we show 3.(c). When $r$ is source in $\tau_{n}$ it means that all paths from $\operatorname{An}(r)$ to $v$ pass through $r$. Because $r$ is not source in $\tau_{m}$ not all paths from $\operatorname{An}(r)$ to $u$ pass through $r$, but they do all pass through $m$.
![img-10.jpeg](img-10.jpeg)

For $j \in \operatorname{An}(r)$ we have

$$
\frac{b_{v j}}{b_{u j}}=\frac{c_{p(j, r)} c_{p(r, v)} b_{j j}}{c_{p(j, m)} c_{p(m, u)} b_{j j}}=\frac{c_{p(j, r)} c_{p(r, v)}}{c_{p(j, m)} c_{p(m, u)}}>0
$$

which is an atom with mass $b_{u j}=c_{p(j, m)} c_{p(m, u)} b_{j j}=b_{m j} c_{p(m, u)}$. The zero atom comes from $b_{u j}=0$ for all $j \in \operatorname{An}(u) \backslash \operatorname{An}(r)$. It gets probability $\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j}$.

# Proof of Proposition 3.1 

Proof. First we prove that (i) implies (ii). Assume $\mathcal{T}$ has a unique source. We have to prove that for any $u \in V$ an element from the limiting vector in (15) is given by (16).

In Lemma B. 1 we have seen a number of cases for the distribution of $A_{u v}$ depending on deterministic properties of the trail between $u$ and $v$. Below we consider each of these cases again.

Case 1. Let the unique shortest trail between $u$ and $v$ be a path on node sequence $\left\{u=v_{1}, r=\right.$ $\left.v_{2}, \ldots, v_{n}=v\right\}$. Let $\tau$ be the tournament containing $u, r$.

Case 1.(a). - Let $u$ be source in $\tau$. From Lemma B.1-1.(a) we have $P\left(A_{u v}=c_{p(u, v)}\right)=1$. Consider the variables $\left(M_{e}, e \in p(u, v)\right)$ which are by construction independent between each other because they belong to different tournaments. Note that in this case all nodes $v_{1}, \ldots, v_{n-1}$ are source nodes in the tournament containing that node and the next one in the sequence. This follows from Lemma 2.4-1. Then according to Lemma 3.2 1.(a) for every $M_{e}, e \in p(u, v)$ we have $\mathbb{P}\left(M_{e}=c_{e}\right)=1$ and hence

$$
\mathbb{P}\left(\prod_{e \in p(u, v)} M_{e}=c_{p(u, v)}\right)=\prod_{e \in p(u, v)} \mathbb{P}\left(M_{e}=c_{e}\right)=1
$$

which shows $A_{u v}=\prod_{e \in p(u, v)} M_{e}$.
Case 1.(b). - If $u$ is not the source in $\tau$, the distribution of $M_{u r}$ is as in Lemma 3.2-1.(b). As in the case 1.(a) all nodes $r=v_{2}, v_{3}, \ldots, v_{n-1}$ are source nodes in the tournament containing that node and the next one in the sequence. The variables $M_{e}, e \in p(r, v)$ are degenerate at $c_{e}$. As the case 1.(a) above the variables $\left(M_{e}, e \in p(u, v)\right)$ are by construction independent between each other because they are indexed by edges which belong to different tournaments. Then we have

$$
\begin{aligned}
\mathcal{L}\left(\prod_{e \in p(u, v)} M_{e}\right)=\mathcal{L}\left(M_{u r} \prod_{e \in p(r, v)} M_{e}\right) & =\left(\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}}\right\}}\right) \otimes \delta_{\left\{c_{p(r, v)}\right\}} \\
& =\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, u)}} c_{p(r, v)}\right\}}
\end{aligned}
$$

The sign $\otimes$ denotes multiplication between two discrete probability measures, say $\mu$ and $\nu$ of two independent variables, say $\xi_{1}, \xi_{2}$ respectively. For two possible values $a_{1}, a_{2}$ of $\xi_{1}, \xi_{2}$ respectively we have $\mu\left(\left\{a_{1}\right\}\right) \nu\left(\left\{a_{1}\right\}\right)$ as a measure of the event $\left\{\xi_{1} \xi_{2}=a_{1} a_{2}\right\}=\left\{\xi_{1}=a_{1}, \xi_{2}=a_{2}\right\}$. The last one expression in (26) is the distribution of $A_{u v}$ in Lemma B.1-1.(b).

Case 2. Let the unique shortest trail between $u$ and $v$ be a path from $v$ to $u$ on the node sequence $\left\{v=v_{1}, r=v_{2}, \ldots, v_{n}=u\right\}$. Let $\tau$ be the tournament containing $v, r$.

Case 2.(a). - Let $v$ be source in $\tau$. Consider the random variables $M_{v_{i+1} v_{i}}, i=1, \ldots, n-1$ whose distributions are as in Lemma 3.2-2.(a). Since this is the unique shortest trail from $v$ to $u$, all edges on it belong to different tournaments and the vector $\left(M_{v_{i+1} v_{i}}, i=1, \ldots, n-1\right)$ contains independent variables by definition. Then

$$
\mathbb{P}\left(\prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}=\frac{1}{c_{p(v, u)}}\right)=\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}=\frac{1}{c_{v_{i} v_{i+1}}}\right)=\prod_{i=1}^{n-1} c_{v_{i} v_{i+1}}=c_{p(v, u)}
$$

For the zero atom we have

$$
\mathbb{P}\left(\prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}=0\right)=1-\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}>0\right)=1-\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}=\frac{1}{c_{v_{i} v_{i+1}}}\right)=1-c_{p(v, u)}
$$

The expressions in (27) and (28) represent indeed the distribution of $A_{u v}$ in Lemma B.1-2.(a).
Case 2.(b). - If $v$ is not the source in $\tau$, consider a random variable $M_{r v}$ with distribution as in Lemma 3.2-2.(b) and a random variable $A_{u r}$ constructed as in 2.(a) here above, i.e., as the product $\prod_{i=2}^{n-1} M_{v_{i+1} v_{i}}$. By construction $M_{r v}$ is independent from $A_{u r}$ with the same argument as above. We have

$$
\begin{aligned}
\mathcal{L}\left(A_{u r} M_{r v}\right) & =\left(c_{p(r, u)} \delta_{\left\{\frac{1}{c_{p(r, u)}}\right\}}+\left(1-c_{p(r, u)}\right) \delta_{\{0\}}\right) \\
& \otimes\left(\sum_{j \in \operatorname{An}(v)} b_{r j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, r)}}\right\}}+\sum_{j \in \operatorname{An}(r) \backslash \operatorname{An}(v)} b_{r j} \delta_{\{0\}}\right)
\end{aligned}
$$

which gives non-zero atoms $c_{p(j, v)} /\left(c_{p(j, r)} c_{p(r, u)}\right), j \in \operatorname{An}(v)$ with masses $b_{r j} c_{p(r, u)}, j \in \operatorname{An}(v)$. To show the probability of the zero atom, consider

$$
\mathbb{P}\left(A_{u r} M_{r v}=0\right)=1-\mathbb{P}\left(A_{u r}>0\right) \cdot \mathbb{P}\left(M_{r v}>0\right)=1-c_{p(r, u)} \sum_{j \in \operatorname{An}(v)} b_{r j}
$$

$$
=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(v)} c_{p(j, r)} b_{j j} c_{p(r, u)}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(v)} b_{u j}=\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(v)} b_{u j}
$$

which is what we need to confirm $A_{u v}=A_{u r} M_{r v}$ where $A_{u v}$ is as in Lemma B.1-2.(b).
Case 3. In the three cases that follow let the unique shortest trail from $u$ to $v$ be given by two paths $p(r, u)$ and $p(r, v)$. Let the trail be on nodes $\{u, \ldots, m, r, n, \ldots, v\}$. Let also $\tau_{m}, \tau_{n}$ be two tournaments with $r, m \in \tau_{m}$ and $r, n \in \tau_{n}$.

Case 3.(a). - Let $r$ be source in both $\tau_{m}$ and $\tau_{n}$. Consider random variables $A_{r v}$ as in Lemma B.11.1.(a) and $A_{u r}$ as in Lemma B.1-2.(a). Above we have shown in cases 1.(a) and 2.(a) that $A_{r v}$ and $A_{u r}$ are factorizable in independent multiplicative increments. By construction $A_{r v}$ and $A_{u r}$ are independent from each other, because the multiplicative increments are independent. We have

$$
\mathbb{P}\left(A_{u r} A_{r v}=\frac{c_{p(r, v)}}{c_{p(r, u)}}\right)=\mathbb{P}\left(A_{u r}=\frac{1}{c_{p(r, u)}}\right) \mathbb{P}\left(A_{r v}=c_{p(r, v)}\right)=c_{p(r, u)}
$$

For the probability of the zero atom we have

$$
\mathbb{P}\left(A_{u r} A_{r v}=0\right)=P\left(A_{u r}=0\right)=\left(1-c_{p(r, u)}\right)
$$

The two displays above represent indeed the distribution of $A_{u v}$ in Lemma B.1-3.(a).
Case 3.(b). - Let $r$ be source in $\tau_{m}$, but not source in $\tau_{n}$. Consider three random variables $A_{u r}, M_{r n}, A_{n v}$ with distributions as in Lemma B.1-2.(a), Lemma 3.2-1.(b) and Lemma B.1-1.(a) respectively. For $A_{u r}$ and $A_{n v}$ we have shown in cases 2.(a) and 1.(a) in this proof that they are factorizable in independent multiplicative increments. By construction $M_{r n}$ is independent from the increments in $A_{u r}$ and $A_{n v}$. Then

$$
\begin{aligned}
\mathcal{L}\left(A_{u r} M_{r n} A_{n v}\right) & =\left(c_{p(r, u)} \delta_{\left\{\frac{1}{c_{p(r, u)}}\right\}}+\left(1-c_{p(r, u)}\right) \delta_{\{0\}}\right) \otimes\left(\sum_{j \in \operatorname{An}(r)} b_{r j} \delta_{\left\{\frac{c_{p(j, u)}}{c_{p(j, r)}}\right\}}\right) \otimes \delta_{\left\{c_{p(n, v)}\right\}} \\
& =\sum_{j \in \operatorname{An}(r)} b_{r j} c_{p(r, u)} \delta_{\left\{\frac{c_{p(j, u)} c_{p(n, v)}}{c_{p(j, r)} c_{p(r, u)}}\right\}}+\left(1-c_{p(r, u)}\right) \delta_{\{0\}}
\end{aligned}
$$

Note that

$$
\begin{aligned}
\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(r)} b_{u j}=1-\sum_{j \in \operatorname{An}(r)} c_{p(j, r)} c_{p(r, u)} b_{j j} & =1-c_{p(r, u)} \sum_{j \in \operatorname{An}(r)} b_{r j} \\
& =1-c_{p(r, u)}
\end{aligned}
$$

This shows that the distribution of $A_{u r} M_{r n} A_{n v}$ is the one of $A_{u v}$ in Lemma B.1-3.(b).
Case 3.(c). - Let $r$ be source in $\tau_{n}$, but not in $\tau_{m}$. Consider variables $A_{u m}, M_{m r}, A_{r v}$ with distributions as in Lemma B.1-2.(a), Lemma 3.2-2.(b) and Lemma B.1-1.(a) respectively. The variables $A_{u m}$ and $A_{r v}$ have been shown to factorize in independent increments in cases 2.(a) and 1.(a) of this proof respectively, hence they are independent from each other too. By construction $M_{m r}$ is independent from $A_{u m}$ and $A_{r v}$. Then we have

$$
\begin{aligned}
\mathcal{L}\left(A_{u m} M_{m r} A_{r v}\right) & =\left(c_{p(m, u)} \delta_{\left\{\frac{1}{c_{p(m, u)}}\right\}}+\left(1-c_{p(m, u)}\right) \delta_{\{0\}}\right) \\
& \otimes\left(\sum_{j \in \operatorname{An}(r)} b_{m j} \delta_{\left\{\frac{c_{p(j, v)}}{c_{p(j, m)}}\right\}}+\sum_{j \in \operatorname{An}(m) \backslash \operatorname{An}(r)} b_{m j} \delta_{\{0\}}\right) \otimes \delta_{\left\{c_{p(r, v)}\right\}}
\end{aligned}
$$

The non-zero atoms are $c_{p(j, r)} c_{p(r, v)} /\left(c_{p(j, m)} c_{p(m, u)}\right)$ for $j \in \operatorname{An}(r)$ with masses $c_{p(m, u)} b_{m j}=c_{p(j, m)} c_{p(m, u)} b_{j j}=$ $b_{u j}$ for $j \in \operatorname{An}(r)$. The probability of the zero atom is given by

$$
\mathbb{P}\left(A_{u m} M_{m r} A_{r v}=0\right)=1-\mathbb{P}\left(A_{u m}>0\right) \mathbb{P}\left(M_{m r}>0\right)=1-c_{p(m, u)} \sum_{j \in \operatorname{An}(r)} b_{m j}
$$

![img-11.jpeg](img-11.jpeg)
(a) When the v-structure belongs to only one of the two trails $t(u, 1)$ or $t(u, 2)$.
![img-12.jpeg](img-12.jpeg)
(b) When each node of the v-structure belongs to one of the two trails $t(u, 1)$ and $t(u, 2)$.

Figure 5: The two possible configurations of the trails $t(u, 1)$ and $t(u, 2)$ when nodes $1,2,3$ form a v-structure.

$$
=1-\sum_{j \in \operatorname{An}(r)} c_{p(j, m)} c_{p(m, u)} b_{j j}=\sum_{j \in \operatorname{An}(u)} b_{u j}-\sum_{j \in \operatorname{An}(r)} b_{u j}=\sum_{j \in \operatorname{An}(u) \backslash \operatorname{An}(r)} b_{u j}
$$

Hence the distribution of $A_{u m} M_{m r} A_{r v}$ is the one of $A_{u v}$ in Lemma B.1-3.(c). This completes the proof that the statement in (i) implies (ii).

The statement in (iii) holds trivially from (ii).
Next we prove that (iii) implies (i) by contraposition: we assume that $\mathcal{T}$ has at least two sources and we will show that it is not possible to obtain the factorization in (16). If $\mathcal{T}$ has at least two sources, then by Lemma 2.3-2 there is at least one v-structure, say on nodes $1,2,3$ and involving edges $(1,3),(2,3) \in E$. Consider the nodes 1,2 . For every $u \in V$ we have two possibilities:
(a) the v-structure belongs to only one of the trails $t(u, 1)$ and $t(u, 2)$ : w.l.o.g. $(1,3),(2,3) \in t(u, 2)$ and $(1,3),(2,3) \notin t(u, 1)$;
(b) each trail $t(u, 1)$ and $t(u, 2)$ contains one edge of the v-structure: w.l.o.g. $(1,3) \in t(u, 1)$ and $(2,3) \in t(u, 2)$.
If $u \in\{1,2\}$, then we are in case 1 , while if $u=3$, we are in case 2 . If $u \notin\{1,2,3\}$, then node 3 must belong to at least one of the two trails $t(u, 1)$ or $t(u, 2)$, because otherwise the skeleton graph would have a cycle connecting nodes $u, 1,2,3$ and passing through more than one block. The latter is impossible according to property (P2). The two possibilities are illustrated in Figure 5.

Case 3.(c-i). Consider first the case when, w.l.o.g., the v-structure belongs to $t(u, 2)$ but not to $t(u, 1)$, see Figure 5(a). Let the trail from 1 to $u$ be on nodes $\left\{v_{1}=1, v_{2}, \ldots, v_{n}=u\right\}$. We can have any direction on the edges of $t(1, u)$. Recall the distribution of $A_{u 2}$ :

$$
\mathcal{L}\left(A_{u 2}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{b_{2 j} / b_{u j}\right\}}
$$

We have $b_{2 j}=0$ for all $j \notin \operatorname{An}(2)$. We claim that $\operatorname{An}(u) \cap \operatorname{An}(2)=\varnothing$. According to property (P2) of a ttt, $\mathcal{T}$ does not contain an undirected cycle involving several tournaments. This means that it is impossible to find a node from which there leave paths to $u$ and to 2 . Also it is not possible to find a path passing through 3 and going to 2 , because otherwise there would be either an undirected cycle involving several tournaments, or a cycle within a tournament. Both are impossible for a ttt. This leads to the conclusion that $A_{u 2}$ is degenerate at zero. Now we look at the variables $\left(M_{v_{i+1} v_{i}}, i=n-1, \ldots, 1 ; M_{13}, M_{32}\right)$ which we take by construction to be independent as they belong to different tournaments. Each of them is one of the variables in Lemma 3.2, and none of these is degenerate at zero. Hence their product cannot be degenerate at zero too.

Case 3.(c-ii). Next we consider the second case, when w.l.o.g. $(1,3) \in t(u, 1)$ and $(2,3) \in t(u, 2)$, see Figure 5(b). Let the trail from node 3 to $u$ be on nodes $\left\{v_{1}=3, v_{2}, \ldots, v_{n}=u\right\}$. First we consider the case when we have at least one $i=1, \ldots, n-1$ for which $\left(v_{i+1}, v_{i}\right) \in E$, i.e., we have at least one edge with direction from $u$ to 3 . Because $t(u, 3)$ is a shortest trail, the edges incident to the nodes on the trail belong to different tournaments. The distribution of $\left(A_{u 1}, A_{u 2}\right)$ is given by

$$
\mathcal{L}\left(A_{u 1}, A_{u 2}\right)=\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{b_{1 j}}{b_{u j}}, \frac{b_{2 j}}{b_{u j}}\right\}}
$$

where $b_{1 j}=0$ and $b_{2 j}=0$ if $j \notin \operatorname{An}(1)$ and $j \notin \operatorname{An}(2)$ respectively. When for some $i=1, \ldots, n-1$ we have $\left(v_{i+1}, v_{i}\right) \in E$ then necessarily $\operatorname{An}(1) \cap \operatorname{An}(u)=\varnothing$ and $\operatorname{An}(2) \cap \operatorname{An}(u)=\varnothing$. There cannot be a path from $\operatorname{An}(1)$ or $\operatorname{An}(2)$ to any of the nodes $\left\{v_{2}, \ldots, v_{n}=u\right\}$, because otherwise there would be a cycle involving several tournaments in contradiction to the definition of a ttt. Because of the edge $\left(v_{i+1}, v_{i}\right) \in E$ all nodes in $\operatorname{An}(1) \cup \operatorname{An}(2)$ are not ancestors of $u$. And also because of the edges $(1,3),(2,3) \in E$ all nodes in $\operatorname{An}(u)$ cannot be ancestors of nodes 1 or 2 . Thus when for some $i=1, \ldots, n-1$ there is a directed edge $\left(v_{i+1}, v_{i}\right) \in E$ we have $\mathcal{L}\left(A_{u 1}, A_{u 2}\right)=\delta_{\{0,0\}}$. We have found a node $v \in V$ such that $A_{u v}=0$ almost surely, but then the factorisation (15)-(16) cannot hold, because these never degenerate at zero.

Now let the trail from node 3 to $u$ be actually a path. Let also nodes 1 and 2 be sources with respect to the tournaments shared with node 3 , say $1,3 \in V_{\tau_{1}}$ and $2,3 \in V_{\tau_{2}}$. It is always possible to choose 1 and 2 in such a way they are the sources of $\tau_{1}$ and $\tau_{2}$. This is because node 3 obviously is not a source in $\tau_{1}$ and $\tau_{2}$, so the sources of these must point to 3 . We can decompose $\operatorname{An}(u)$ into three disjoint sets, $\operatorname{An}(1), \operatorname{An}(2)$ and the rest, $\operatorname{An}(u) \backslash\{\operatorname{An}(1) \cup \operatorname{An}(2)\}$. For the distribution of $\left(A_{u 1}, A_{u 2}\right)$ we have

$$
\begin{aligned}
\mathcal{L}\left(A_{u 1}, A_{u 2}\right) & =\sum_{j \in \operatorname{An}(u)} b_{u j} \delta_{\left\{\frac{b_{1 j}}{b_{u j}}, \frac{b_{2 j}}{b_{u j}}\right\}} \\
& =\sum_{j \in \operatorname{An}(1)} b_{u j} \delta_{\left\{\frac{b_{1 j}}{b_{u j}}, \frac{b_{2 j}}{b_{u j}}\right\}}+\sum_{j \in \operatorname{An}(2)} b_{u j} \delta_{\left\{\frac{b_{1 j}}{b_{u j}}, \frac{b_{2 j}}{b_{u j}}\right\}}+\sum_{j \in \operatorname{An}(u) \backslash\{\operatorname{An}(1) \cup \operatorname{An}(2)\}} b_{u j} \delta_{\left\{\frac{b_{1 j}}{b_{u j}}, \frac{b_{2 j}}{b_{u j}}\right\}}
\end{aligned}
$$

For the atoms in the first summation we have

$$
\frac{b_{1 j}}{b_{u j}}=\frac{c_{p(j, 1)} b_{j j}}{c_{p(j, u)} b_{j j}}=\frac{c_{p(j, 1)}}{c_{p(j, 1)} c_{13} c_{p(3, u)}}=\frac{1}{c_{13} c_{p(3, u)}}
$$

and $b_{2 j} / b_{u j}=0$ as $b_{2 j}=0$ for all $j \in \operatorname{An}(1)$. Hence we have an atom that does not depend on $j \in \operatorname{An}(1)$, i.e., $\left(1 /\left(c_{13} c_{p(3, u)}\right), 0\right)$ and its mass is

$$
\sum_{j \in \operatorname{An}(1)} b_{u j}=\sum_{j \in \operatorname{An}(1)} c_{p(j, 1)} c_{13} c_{p(3, u)} b_{j j}=c_{13} c_{p(3, u)}=c_{p(1, u)}
$$

In a similar way, from the second summation in the last display we have an atom $\left(0,1 /\left(c_{23} c_{p(3, u)}\right)\right)$ with mass $c_{23} c_{p(3, u)}=c_{p(2, u)}$. In the third summation term the atom is $(0,0)$ as $b_{1 j}=b_{2 j}=0$ for all $j \in \operatorname{An}(u) \backslash\{\operatorname{An}(1) \cup \operatorname{An}(2)\}$ and its mass is $1-c_{13} c_{p(3, u)}-c_{23} c_{p(3, u)}=1-c_{p(3, u)}\left(c_{13}+c_{23}\right)$. Consider now the multiplicative increments $\left(M_{31} ; M_{32}, M_{v_{i+1} v_{i}} i=1, \ldots, n-1\right)$ which are mutually independent since they belong to different tournaments. Because node 1 is a source node in the tournament $\tau_{1}$ the distribution of $M_{31}$ is $c_{13} \delta_{\left\{1 / c_{13}\right\}}+\left(1-c_{13}\right) \delta_{\{0\}}$ by Lemma 3.2-2.(a). Similarly for $M_{32}$. We have

$$
\begin{aligned}
& \mathbb{P}\left(M_{31} \prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}=0, M_{32} \prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}=0\right)=1-\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}>0\right) \\
& +\mathbb{P}\left(M_{31}=0\right) \mathbb{P}\left(M_{32}=0\right)-\left(1-\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}>0\right)\right) \mathbb{P}\left(M_{31}=0\right) \mathbb{P}\left(M_{32}=0\right)
\end{aligned}
$$

After some rearranging of the expression above we obtain

$$
1-\prod_{i=1}^{n-1} \mathbb{P}\left(M_{v_{i+1} v_{i}}>0\right)\left(c_{13}+c_{23}-c_{13} c_{23}\right)
$$

There are two further sub-cases: either all nodes $v_{1}, \ldots, v_{n-1}$ are source nodes with respect to the tournament involving the next node in the sequence, or not. In the first sub-case, namely when all nodes in $\left\{v_{1}=3, v_{2}, \ldots, v_{n-1}\right\}$ are source nodes with respect to the tournament involving the next node in the sequence, then $\mathbb{P}\left(M_{v_{i+1} v_{i}}>0\right)=c_{v_{i} v_{i+1}}$ for $i=1, \ldots, n-1$. This means that the probability in (30) and accordingly in (29) equals $1-c_{p(3, u)}\left(c_{13}+c_{23}-c_{13} c_{23}\right)$, which is different than $\mathbb{P}\left(A_{u 1}=0, A_{u 2}=0\right)=1-c_{p(3, u)}\left(c_{13}+c_{23}\right)$. In the second sub-case, i.e., if at least one node from $\left\{v_{1}=3, v_{2}, \ldots, v_{n-1}\right\}$ is not source with respect to the tournament involving the next node in

the sequence then the possible values for $M_{31} \prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}$ are not only $\left\{0,1 / c_{p(1, n)}\right\}$, which are the only possible values of $A_{u 1}$ as we showed in the previous paragraph. Let $i \in\{1, \ldots, n-1\}$ be such that node $v_{i}$ is not the source node in the tournament shared with $v_{i+1}$, say $\tau_{i}$. This is depicted in the following graph:
![img-13.jpeg](img-13.jpeg)

Recall the distribution of $M_{v_{i+1} v_{i}}$ from Lemma 3.2-2.(b):

$$
\mathcal{L}\left(M_{v_{i+1} v_{i}}\right)=\sum_{j \in \operatorname{An}\left(v_{i}\right)} b_{v_{i+1} j} \delta_{\left\{b_{v_{i} j} / b_{v_{i+1} j}\right\}}+\sum_{j \in \operatorname{An}\left(v_{i+1}\right) \backslash \operatorname{An}\left(v_{i}\right)} \delta_{\{0\}}
$$

Take for instance a node, say $s$, a parent of $v_{i}$ and accordingly in $\operatorname{An}\left(v_{i}\right)$. Then

$$
\frac{b_{v_{i} s}}{b_{v_{i+1} s}}=\frac{c_{s v_{i}}}{c_{s v_{i+1}}}
$$

is a possible value of $M_{v_{i+1} v_{i}}$ with positive probability, namely at least $b_{v_{i+1} s}$. Another possible positive value is for $j=v_{i} \in \operatorname{An}\left(v_{i}\right)$, namely

$$
\frac{b_{v_{i} v_{i}}}{b_{v_{i+1} v_{i}}}=\frac{1}{c_{v_{i} v_{i+1}}}
$$

with probability at least $b_{v_{i+1} v_{i}}$. The criticality assumption on edge weights guarantees $\frac{c_{s v_{i}}}{c_{s v_{i+1}}} \neq$ $1 / c_{v_{i} v_{i+1}}$. This means that the product $M_{31} \prod_{i=1}^{n-1} M_{v_{i+1} v_{i}}$ has at least two different positive values - one involving $\frac{c_{s v_{i}}}{c_{s v_{i+1}}}$ and another $1 / c_{v_{i} v_{i+1}}$. However $A_{u 1}$ has only one possible positive value.

# Proof of Proposition 3.3 

Proof. Sufficiency. Assume $\mathcal{T}$ has a unique source. We need to show that, for any disjoint and nonempty sets $A, B, S$, we have $X_{A} \Perp X_{B} \mid X_{S}$, whenever $S$ is a separator of $A$ and $B$ in the skeleton $T$ of $\mathcal{T}$. We would like to use Theorem 5.15 in Améndola, Klüppelberg, Lauritzen, and Tran (2022), by which we need to show $A \perp_{*} B \mid S$ in $\mathcal{D}_{S}^{*}$, that is, there are no $*$-connecting paths between any pair of nodes in $A$ and $B$ in the conditional reachability $\mathrm{DAG} \mathcal{D}_{S}^{*}$. We will explain these notions further.

Let $A, B, S \subset V$ be nonempty disjoint node sets, such that $S$ is a separator of $A$ and $B$ in the skeleton $T$. Consider Figure 6. According to Definition 5.4 of Améndola et al. (2022), a $*$-connecting path between $a \in A$ and $b \in B$ is one of the five configurations therein. Our goal is to show that for $a \in A$ and $b \in B$ it is impossible to find a $*$-connecting path in a certain graph $\mathcal{D}_{S}^{*}$, which is not $\mathcal{T}$, neither $T$, but constructed under particular rules given in Améndola et al. (2022, Definition 5.1).
![img-14.jpeg](img-14.jpeg)

Figure 6: According to Definition 5.4 of Améndola et al. (2022), a $*$-connected path between $a$ and $b$ relative to $S$ is one of the five configurations above. In the last three graphs we have $s \in S$.

According to this definition, the conditional reachability graph $\mathcal{D}_{S}^{*}$ is on the same vertex set, $V$. Between two nodes $i$ and $j$ in $V$ there is an edge $(i, j)$ in $\mathcal{D}_{S}^{*}$ if and only if there is a directed path from $i$ to $j$ in $\mathcal{T}$ such that no node on that path belongs to $S$, except possibly for $i$ and $j$ themselves.

Consider Figure 6. We need to show that in the conditional reachability graph $\mathcal{D}_{S}^{*}$, there is no $*$-connecting path between a node $a \in A$ and a node $b \in B$.

To obtain the first configuration in $\mathcal{D}_{S}^{*}$, there must be, in the skeleton $T$, nodes $a \in A$ and $b \in B$ such that no node on the path from $a$ to $b$ passes through $S$. But this is impossible, because we assumed that $S$ is a separator of $A$ and $B$ in $T$. Similarly for the second configuration.

For the other three configurations in Figure 6 consider Figure 7.
In Figure 7, the left-hand and right-hand trails in the original graph $\mathcal{T}$ are the only possible one that give rise to the middle path in Figure 6 with respect to the graph $\mathcal{D}_{S}^{*}$ : both the left-hand and right-hand graphs in Figure 7 show existing trails between $a$ and $b$ in $\mathcal{T}$, trails composed of a directed path from $a$ to $s$, and a directed path from $b$ to $s$. The only node on these trails which belongs to $S$ is $s$. Hence in $\mathcal{D}_{S}^{*}$ we put a directed edge from $a$ to $s$ and from $b$ to $s$. This gives the third $*$-connecting path in Figure 6. But this configuration cannot occur, for the following reason. On the left-hand trail in Figure 7, the separator node $s$ has parents $u_{r}$ and $v_{q}$ in different tournaments. This leads to a v-structure between the nodes $u_{r}, s, v_{q}$, in contradiction to Lemma 2.3-2 and the hypothesis that $\mathcal{T}$ has a unique source.

On the right-hand trail in Figure 7, the node $s$ shares a tournament with its parents $u_{r}$ and $v_{q}$, but only $s$ belongs to $S$; on the trail $\left\{a=u_{1}, u_{2}, \ldots, u_{r}, v_{q}, \ldots, v_{2}, v_{1}=b\right\}$ none of the nodes are in $S$. In $T$, this means that there is a path between $A$ and $B$ that does not pass through $S$. This is in contradiction to the assumption that $S$ separates $A$ and $B$ in $T$.

To show that the fourth type of $*$-connecting path in Figure 6 cannot occur, we can use the reasoning used for the third one by setting $a=a^{\prime}$ in Figure 7. Then either $s$ has parents from two different tournaments or there is a non-directed path from $a^{\prime}$ to $b$ which does not pass through $S$. The first case is excluded by Lemma 2.3-2 and the assumption that $\mathcal{T}$ has a unique source, and the second one by the assumption that $S$ is a separator of $A$ and $B$ in $T$. The impossibility of the fifth $*$-connected configuration follows analogously.
![img-15.jpeg](img-15.jpeg)

Figure 7: The left and right trails in the original graph $\mathcal{T}$ are the only possible trails that give rise to the middle path in the graph $\mathcal{D}_{S}^{*}$.

Necessity. We will show that if $\mathcal{T}$ has multiple source nodes, there is a triple of disjoint, nonempty sets $A, B, S \subset V$ such that $S$ is a separator of $A$ and $B$ in $T$, but $X_{A}$ and $X_{B}$ are conditionally dependent given $X_{S}$. In case $\mathcal{T}$ has at least two sources, we have at least one v-structure in $\mathcal{T}$ by Lemma 2.3-2. Take a triple of nodes in a v-structure, say $u, v, w$, with $u$ and $w$ being parents of $v$. Then node $v$ separates nodes $u$ and $w$ in $T$, i.e., $S=\{v\}$ is a separator of $A=\{u\}$ and $B=\{w\}$ in $T$. All references below are from Améndola et al. (2022).

To show $X_{u} \not \perp X_{w} \mid X_{v}$ we will use Theorem 6.18 (Context free completeness) of Améndola et al. (2022). We need to show that there is an effective $*$-connecting path in the critical DAG $\mathcal{D}_{S}^{*}(\theta)$ between nodes $u$ and $w$ as in their Definitions 5.2 and 6.5 .

The subgraph on nodes $u, v, w$ of $\mathcal{D}_{S}^{*}(\theta)$ is a v-structure, $u \longrightarrow v \leftarrow w$, according to the definition of $\mathcal{D}_{S}^{*}(\theta)$. According to Definition 6.4, the $|S| \times|S|$ substitution matrix of $(u, v) \in E$ relative to $S=\{v\}$ is zero, because $S$ is a singleton and by definition all diagonal entries of the substitution matrix are zero, i.e., $\Xi_{S}^{v u}=0$. Similarly, $\Xi_{S}^{v w}=0$. Because the edges $(u, v),(w, v)$ form a $*$-connecting path between $u, w$ in $\mathcal{D}_{S}^{*}(\theta)$, the substitution matrix of this path relative to $S$, say $\Xi_{S}$, is zero too:

$$
\Xi_{S}=\max \left(\Xi_{S}^{v u}, \Xi_{S}^{v w}\right)=0
$$

To find out if the edges $(u, v),(w, v)$ form an effective $*$-connecting path between $u, w$, we need to compute the tropical eigenvalue of $\max \left(\Gamma_{S S}, \Xi_{S}\right)$ where $\Gamma$ is as in Equation (2.3) in Améndola et al. (2022) and $\Gamma_{S S}$ is the $v v$-element of $\Gamma$, i.e., $\{\Gamma\}_{v v}$. Because $\{\Gamma\}_{i j}>0$ if and only if there is a directed

![img-16.jpeg](img-16.jpeg)

Figure 8: A unique path on nodes $\left\{\bar{u}=v_{1}, v_{2}, v_{3}, \ldots, s=v_{n}\right\}$ under Lemma C.1.1. Each of the nodes $\bar{u}, v_{2}, \ldots, v_{n-1}$ belongs to $\bar{U}$. Each of the nodes $v_{2}, \ldots, v_{n-1}, s$ has a unique parent. The node $\bar{u} \in \bar{U}$ may have parents as illustrated here, but then there is at least one tournament with respect to which it is a source node, e.g., $\tau_{1}$. Let $v_{2}$ be the node with unique parent $\bar{u}$ in $\tau_{1}$. When $v_{2}$ belongs to $\bar{U}$, it must participate in at least one another tournament, say $\tau_{2}$. In $\tau_{2}$ the node with unique parent $v_{2}$ is $v_{3}$. In this principle the path continues until we find a node in $U$, which is $v_{n}=s$ in this case.
path from $j$ to $i$, we have $\Gamma_{S S}=\{\Gamma\}_{v v}=0$ and so

$$
\max \left(\Gamma_{S S}, \Xi_{S}\right)=0
$$

The tropical eigenvalue (Améndola et al., 2022, Equation (2.7)) of the above matrix is trivially equal to zero and thus smaller than one. By Definition 6.5 in the cited reference, there is indeed an effective $*$-connecting path between $u, w$ in $\mathcal{D}_{S}^{*}(\theta)$. In view of their Theorem 6.18, we conclude $X_{u} \not \models X_{w} \mid X_{v}$.

# C Proofs and additional results for Section 4 

## C. 1 Auxiliary results

Proof of Lemma 4.1. The point masses satisfy $m_{i}>0$ for all $i \in V$ because we have $m_{i}=0$ if and only if $c_{i i}=0$. However $c_{i i}=0$ is impossible in view of the definition in (6). Therefore we cannot have undefined atoms, which would happen when $m_{i}=0$. This shows (i).

Next we show (ii). To see why $a_{i} \neq a_{j}$ for $i \neq j$, let $i, v \in V$ and recall $b_{v i}$ in (8). From the line below (11), recall that we also have $b_{v i}=m_{i} a_{v i}$ for $i, v \in V$. Thanks to the assumption $\theta \in \tilde{\Theta}_{*}$, we have (18). We also have for any DAG (19).

The combination of the last two equations implies that in (11), all vectors $a_{i}$ for $i \in V$ are different and thus that $H_{\theta}$ has $|V|$ distinct atoms. Also, for every node $i \in V$, we can find out which of the $|V|$ atoms of $H_{\theta}$ is $a_{i}$ because it is the unique one that satisfies $\operatorname{Desc}(i)=\left\{v \in V: a_{v i}>0\right\}$. Note that similarly, among the $|V|$ vectors in the set $\mathcal{B}_{\theta}=\left\{\left(b_{v j}\right)_{v \in V}: j \in V\right\}$, the vector $b_{i}$ is the unique one such that $\operatorname{Desc}(i)=\left\{v \in V: b_{v i}>0\right\}$.

Finally consider (iii). By the criticality assumption, every edge is critical, because it is the shortest path between any pair of adjacent nodes. Since $(i, v) \in E$ is critical, we have $b_{v i}=b_{i i} c_{i v}$ and thus $c_{i v}=b_{v i} / b_{i i}=a_{v i} / a_{i i}$.

In summary, the angular measure $H_{\theta}$ possesses $|V|$ distinct atoms that can be uniquely matched to the nodes. As a consequence, we can reconstruct the matrix $\left(b_{v i}\right)_{i, v \in V}$. Thanks to (iii), this matrix allows us to recover all edge weights $c_{v i}$.

Lemma C.1.1. Let $\mathcal{T}=(V, E)$ be a ttt as in Definition 2.1 and let $\mathcal{T}$ have a unique source, $u_{0}$. Let $U \subset V$ be non-empty and suppose that $\bar{U}=V \backslash U$ satisfies conditions (I1) and (I2). For every $\bar{u} \in \bar{U}$ there exists $s \in \operatorname{desc}(\bar{u}) \cap U$ such that $\pi(\bar{u}, s)$ is a singleton and the unique path $p$ from $\bar{u}$ to $s$ satisfies the following two properties:

1. all nodes on $p$ except for $s$ are in $\bar{U}$;
2. all nodes on $p$ except possibly for $\bar{u}$ have only one parent.

As a consequence, any path with destination $s$ must either start in one of the nodes of $p$ or contain $p$ as a sub-path.

Proof. Let $\bar{u} \in \bar{U}$ and suppose $\bar{u}$ has no parents, so $\bar{u}=u_{0}$. Take a node whose unique parent is $\bar{u}$, say $v_{2}$. By Harary and Moser (1966, Corollary 5.a) such a node exists in every tournament in which $\bar{u}$ takes part. If $v_{2} \in U$ then $s=v_{2}$ and we are done. If $v_{2} \in \bar{U}$ then by (I2) $v_{2}$ must be a source of at least one another tournament. In each of these, there is a node whose only parent is $v_{2}$. Take such a node, say $v_{3}$. If $v_{3} \in U$ then $v_{3}=s$ and we are done; otherwise continue in the same way until we find a node which is in $U$. Because the graph is finite and because of condition (I2) such a node must exist. It is clear that the path constructed in this way has the stated properties.

Next suppose that $\bar{u}$ belongs to $\bar{U}$ and that $\bar{u}$ has at least one parent. By (I2) it must be a source of at least one tournament In each of these tournaments there is a node with single parent $\bar{u}$. Take one of them, say $v_{2}$, and if $v_{2} \in U$ then we are done, otherwise repeat the same procedure as above until we find a node which is in $U$. Because the graph is finite and because of condition (I2) such a node must exist. It is clear that the path constructed in this way has the stated properties too.

Lemma C.1.2. Let $\mathcal{T}=(V, E)$ be a ttt as in Definition 2.1 and let $\mathcal{T}$ have a unique source, $u_{0}$. Let $U \subset V$ be non-empty and suppose that $\bar{U}=V \backslash U$ satisfies conditions (I1) and (I2). Let $i, j \in V$ be two distinct nodes. Upon switching the roles of $i$ and $j$ if needed, the equality $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$ implies the following properties:

1. $i \in \bar{U}$;
2. $\operatorname{desc}(i)=\operatorname{Desc}(j)$;
3. $\{i\}=\operatorname{pa}(j)$;
4. there exists $u \in V$ such that $i, j \in \mathrm{pa}(u)$;
5. for $k \in V \backslash\{i, j\}$, the set $\operatorname{Desc}(k) \cap U$ is different from $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap V$;
6. $|\operatorname{Desc}(i) \cap U|=|\operatorname{Desc}(j) \cap U| \geq 2$.

Proof. 1. Note first that $\operatorname{Desc}(i) \cap U$ cannot be empty, for otherwise, we would have $\operatorname{Desc}(i) \subseteq \bar{U}$, but this is impossible, since $\operatorname{Desc}(i)$ contains at least one leaf node (a node without children), in contradiction to (I1).

Since $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$ and since this set is non-empty, the intersection $\operatorname{Desc}(i) \cap \operatorname{Desc}(j)$ is not empty too. In relation to Lemma 2.3-3 this means either $\operatorname{Desc}(i) \subseteq \operatorname{Desc}(j)$ or $\operatorname{Desc}(j) \subseteq$ $\operatorname{Desc}(i)$. In the remainder of the proof, we suppose $\operatorname{Desc}(j) \subseteq \operatorname{Desc}(i)$. Then we must have $i \notin$ $\operatorname{Desc}(j)$, since otherwise also $\operatorname{Desc}(i) \subseteq \operatorname{Desc}(j)$ and thus $\operatorname{Desc}(i)=\operatorname{Desc}(j)$, which is impossible since $i$ and $j$ are distinct; see (19). From $\operatorname{Desc}(j) \subseteq \operatorname{Desc}(i)$ and $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$ it follows that

$$
\operatorname{Desc}(i) \backslash \operatorname{Desc}(j) \subseteq \bar{U}
$$

Because $i \notin \operatorname{Desc}(j)$ we get $i \in \bar{U}$.
2-4. First we show that all elements in $\operatorname{Desc}(i) \backslash \operatorname{Desc}(j)$ are ancestors of $j$. Let $v \in \operatorname{Desc}(i) \backslash$ $\operatorname{Desc}(j)$. Because $j$ and $v$ are two different nodes, Lemma 2.3-3 implies that one of three cases must occur: $\operatorname{Desc}(v) \subset \operatorname{Desc}(j) ; \operatorname{Desc}(j) \subset \operatorname{Desc}(v)$; or $\operatorname{Desc}(j) \cap \operatorname{Desc}(v)=\varnothing$. The first case, $\operatorname{Desc}(v) \subset \operatorname{Desc}(j)$, is impossible, since $v \notin \operatorname{Desc}(j)$. The third case, $\operatorname{Desc}(j) \cap \operatorname{Desc}(v)=\varnothing$, is impossible too, since it would imply that $\operatorname{Desc}(v) \subseteq \operatorname{Desc}(i) \backslash \operatorname{Desc}(j) \subseteq \bar{U}$, but this cannot happen since $\operatorname{Desc}(v)$ contains at least one leaf node while $\bar{U}$ does not contain any. Only the second case, $\operatorname{Desc}(j) \subset \operatorname{Desc}(v)$, remains. As a consequence, $v$ is an ancestor of $j$, and so all nodes of $\operatorname{Desc}(i) \backslash \operatorname{Desc}(j)$ are ancestors of $j$. By the proof of point 1 , we get

$$
\operatorname{Desc}(i) \backslash \operatorname{Desc}(j) \subseteq \operatorname{an}(j) \cap \bar{U}
$$

Let again $v \in \operatorname{Desc}(i) \backslash \operatorname{Desc}(j)$. We show that there exists a unique path from $v$ to $j$ and that $j$ has only a single parent. Since $v \in \bar{U}$, there exists, by Lemma C.1.1, a node $s(v) \in U$ such that there is only directed path $p(v, s(v))$ from $v$ to $s(v)$; moreover, this path satisfies properties 1 and 2 of the statement. Necessarily,

$$
s(v) \in \operatorname{Desc}(v) \cap U \subseteq \operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U
$$

As $s(v)$ is a descendant of $j$ while $j$ is a descendant of $v$, the path $p(v, s(v))$ passes by $j$. As a consequence, there is a unique path $p(v, j)$ from $v$ to $j$; otherwise, there would be more than one path from $v$ to $s(v)$. Moreover, by Lemma C.1.1-2, all nodes on the path $p(v, s(v))$, except possibly for $v$, have only one parent. In particular, $j$ has only one parent.

Take again any $v \in \operatorname{Desc}(i) \backslash \operatorname{Desc}(j)$. By (I1), $v$ has at least two children. They cannot both be ancestors of $j$, since then there would be two paths from $v$ to $j$, in contradiction to the previous paragraph. Let $u$ be a child of $v$ that is not an ancestor of $j$; then $u \in \operatorname{Desc}(j)$ because of (31). This means there are two paths from $v$ to $u$ : the edge $(v, u)$ and a path passing through $j$. These paths must belong to the same tournament, as the skeleton of $\mathcal{T}$ is a block graph. But then $v$ and $j$ are adjacent, and thus $v$, which we already knew to be an ancestor of $j$, is actually a parent of $j$. But $j$ has only one parent, and so the set $\operatorname{Desc}(i) \backslash \operatorname{Desc}(j)$ must be a singleton. As this set obviously contains node $i$, we get $v=i$ and thus $\operatorname{Desc}(i) \backslash \operatorname{Desc}(j)=\operatorname{pa}(j)=\{i\}$. Since $\operatorname{Desc}(i)=\{i\} \cup \operatorname{desc}(i)$ and $\operatorname{Desc}(j) \subset \operatorname{Desc}(i)$, it follows that $\operatorname{desc}(i)=\operatorname{Desc}(j)=\operatorname{Desc}(i) \backslash\{i\}$.
5. Let $k \in V \backslash\{i, j\}$ be such that $\operatorname{Desc}(k) \cap U=\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$. By point 3 we have $\{i\}=\operatorname{pa}(j)$. From $\operatorname{Desc}(k) \cap U=\operatorname{Desc}(i) \cap U$ we can have either $\{k\}=\operatorname{pa}(i)$ or $\{i\}=\operatorname{pa}(k)$, while from $\operatorname{Desc}(k) \cap U=\operatorname{Desc}(j) \cap U$ we have either $\{k\}=\operatorname{pa}(j)$ or $\{j\}=\operatorname{pa}(k)$. Because already $\{i\}=\operatorname{pa}(j)$, we cannot also have $\{k\}=\operatorname{pa}(j)$, whence we must have $\{j\}=\operatorname{pa}(k)$. But then $\{i\}=\operatorname{pa}(k)$ is impossible, so that necessarily $\{k\}=\operatorname{pa}(i)$. From $\{i\}=\operatorname{pa}(j),\{j\}=\operatorname{pa}(k)$, and $\{k\}=\operatorname{pa}(i)$ we get a cycle between the three nodes $i, j, k$ which is a contradiction to the definition of a DAG.
6. We already know that $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$. We need to show that this set contains at least two elements. Consider the triple $\{i, j, u\}$ from point 4 that forms a triangle with directed edges $(i, j),(i, u)$, and $(j, u)$. By point 1 we have also $i \in \bar{U}$. There are four cases, according to whether $j$ and $u$ belong to $U$ or not.

- If $j, u \in U$, they are two distinct elements of $\operatorname{Desc}(j) \cap U$.
- If $j \in U$ but $u \in \bar{U}$, then take $r \in \operatorname{Desc}(u) \cap U$ [which is non-empty by (I1): all leaf nodes in $\operatorname{Desc}(u)$ are in $U]$, and note that $j$ and $r$ are two distinct elements in $\operatorname{Desc}(j) \cap U$.
- If $j \in \bar{U}$ and $u \in U$, then, as in Lemma C.1.1, let $s \in U$ be such that there is unique path $p(j, s)$ from $j$ to $s$, this path satisfying properties $1-2$ in the same lemma. Then $u$ does not belong to that path (since $u \in U$ and $u$ has at least two parents, $i$ and $j$ ), so that $s$ is different from $u$, and both are members of $\operatorname{Desc}(j) \cap U$.
- If $j, u \in \bar{U}$, then we can find by Lemma C.1.1 nodes $s \in \operatorname{desc}(j) \cap U$ and $r \in \operatorname{desc}(u) \cap U$ with paths $p(j, s)$ and $p(u, r)$ which satisfy the characteristics in this lemma. Nodes $s, r$ clearly belong to $\operatorname{Desc}(j) \cap U$. Moreover, they are distinct: node $u$, having at least two parents, cannot belong to the unique path $p(j, s)$ between $j$ and $s$, while by construction, there is a directed path from $j$ to $r$ that passes along $u$.

Lemma C.1.3. Let $X$ be a max-linear model with respect to a ttt with unique source. The coefficient $b_{v v}$ depends only on the edge weights of the tournament shared by node $v \in V$ and its parents, and it is given by

$$
b_{v v}=1+\sum_{u \in \operatorname{pa}(v)} \sum_{p \in \pi(u, v)}(-1)^{|p|} c_{p}
$$

Proof. Consider the node $v$. If $v$ has no parents we have $\operatorname{an}(v)=\varnothing$ and by (6) we have $b_{v v}=1$. If $v$ has at least one parent then there is a tournament which contains the parents, say, $\tau=\left(V_{\tau}, E_{\tau}\right)$. Let the nodes in $\tau$ be labelled according to their in-/out-degree ordering in $\tau$ : the node with $\left|V_{\tau}\right|-1$ children in $\tau$ (the source of $\tau$ ) has index 1 , the node with $\left|V_{\tau}\right|-2$ children in $\tau$ has index 2 , and so on. We can partition the set $\operatorname{an}(v)$ into $\operatorname{An}(1)$ and $\operatorname{pa}(v) \backslash\{1\}$. For $i \in \operatorname{An}(1)$ the shortest path from $i$ to $v$ passes necessarily through 1 , so $b_{v i}=c_{p(i, 1)} c_{1 v} b_{i i}$. Then we have by (4) and (6)

$$
b_{v v}=1-\sum_{i \in \operatorname{an}(v)} b_{v i}=1-\sum_{i \in \operatorname{An}(1)} c_{p(i, 1)} c_{1 v} b_{i i}-\sum_{i \in \operatorname{pa}(v) \backslash 1} b_{v i}=1-c_{1 v}-\sum_{i \in \operatorname{pa}(v) \backslash 1} c_{i v} b_{i i}
$$

Let $C=\left\{c_{i j}\right\}_{i, j \in V_{\tau}, i<j}$ be the matrix of edge weights within $\tau$ : it is lower triangular and has zero diagonal. Let $I_{m}$ denote the $m \times m$ identity matrix, write $\boldsymbol{b}=\left(1, b_{22}, \ldots, b_{\left|V_{\tau}\right|,\left|V_{\tau}\right|}\right)^{\top}$ (a column vector) and let $1_{\left|V_{\tau}\right|}$ be a column vector of ones of length $\left|V_{\tau}\right|$. Consider the system of linear equations

$$
\left(I_{\left|V_{\tau}\right|}+C\right) \boldsymbol{b}=1_{\left|V_{\tau}\right|}
$$

For $v \geq 2$ the expression in (33) is equivalent to the $v$-th equation in (34). A solution for $\boldsymbol{b}$ is

$$
\boldsymbol{b}=\left(I_{\left|V_{\tau}\right|}+C\right)^{-1} 1_{\left|V_{\tau}\right|}=\left(I_{\left|V_{\tau}\right|}-(-C)\right)^{-1} 1_{\left|V_{\tau}\right|}
$$

From the equality

$$
\left(I_{\left|V_{\tau}\right|}+(-C)+(-C)^{2}+\cdots+(-C)^{k}\right)\left(I_{\left|V_{\tau}\right|}-(-C)\right)=I_{\left|V_{\tau}\right|}-(-C)^{k+1}
$$

and the fact that for $\left|V_{\tau}\right|$-square lower triangular matrix with zero diagonal powers of $k \geq\left|V_{\tau}\right|$ are zero matrices we obtain

$$
\left(I_{\left|V_{\tau}\right|}+(-C)+(-C)^{2}+\cdots+(-C)^{\left|V_{\tau}\right|-1}\right)=\left(I_{\left|V_{\tau}\right|}-(-C)\right)^{-1}
$$

If the matrix on the left is denoted by $K$ we have as solution $\boldsymbol{b}=K 1_{\left|V_{\tau}\right|}$. For all $b_{v v}, v \geq 2$, it can be shown that (32) equals the $v v$-th element of this solution for $\boldsymbol{b}$. For $b_{11}$ consider the corresponding solution when the tournament $\tau$ is the one which node 1 shares with its parents. If node 1 has no parents in the ttt, then we have the solution $b_{11}=1$ which is indeed the case.

Lemma C.1.4. Let $X$ follow a max-linear model as in Assumption 2.1 with respect to a ttt $\mathcal{T}$ consisting of a single tournament $\tau=(V, E)$. If the node $v \in V$ has at least one parent, then the parameter vector $\theta=\left(c_{v}\right)_{v \in E} \in \tilde{\Theta}_{*}$ is not identifiable from the distribution of $X_{V \backslash v}$. Specifically, there exists $\theta^{\prime}=\left(c_{v}^{\prime}\right)_{v \in E} \in \tilde{\Theta}_{*}$ such that $\theta^{\prime} \neq \theta$ and the distribution of $X_{V \backslash v}$ is the same under $\theta^{\prime}$ as under $\theta$.

Proof. Let $n=|V|$ denote the number of nodes. For convenience, rename the nodes to $V=$ $\{1, \ldots, n\}$ in the ordering induced by the DAG, i.e., node $i$ has $i-1$ parents, for $i \in V$. The number of edges is $|E|=n(n-1) / 2=: m$, and the parameter set $\tilde{\Theta}_{*}$ is an open subset of $\mathbb{R}^{E}$. The distribution of $X$ is max-linear and is given by

$$
X_{j}=\bigvee_{i=1}^{j} b_{j i} Z_{i}, \quad j \in V
$$

where $b_{11}=1, b_{j j}=1-\sum_{i=1}^{j-1} b_{j i}$ for $j \in V \backslash 1$, and where the $m$ coefficients $b=\left(b_{j i}: 1 \leq i<j \leq n\right)$ are determined by the edge parameters $\theta=\left(c_{i j}: 1 \leq i<j \leq n\right)$.

Discarding the variable $X_{v}$ for some $v \in V \backslash 1$ yields the vector $X_{V \backslash v}$, the distribution of which is determined by the $m-(v-1)$ coefficients $\left(b_{j i}: 1 \leq i<j \leq n, j \neq v\right)$. For convenience, identify $\mathbb{R}^{E}$ with $\mathbb{R}^{m}$. Let $\pi: \mathbb{R}^{m} \rightarrow \mathbb{R}^{m-v+1}$ be the projection that sends $x=\left(x_{i j}: 1 \leq i<j \leq m\right)$ to $\pi(x)=\left(x_{i j}: 1 \leq i<j \leq m, j \neq v\right)$, i.e., the effect of $\pi$ is to leave out the coordinates $(i, v)$ with $i=1, \ldots, v-1$. By (35) with $j=v$ removed, the distribution of $X_{V \backslash v}$ is determined by $\pi(b)$.

The max-linear coefficients $b$ are a function of the edge parameters $\theta$. Formally, there exists a map $f: \tilde{\Theta}_{*} \rightarrow \mathbb{R}^{m}$ such that

$$
b=f(\theta)
$$

The function $f$ can be reconstructed from (8) with $p(i, j)=(i, j)$ for $1 \leq i<j \leq n$. Clearly, $f$ is continuous. Since the parameter $\theta$ is identifiable from the distribution of $X$ (Lemma 4.1), the function $f$ is also injective, i.e., $\theta \neq \theta^{\prime}$ implies $f(\theta) \neq f\left(\theta^{\prime}\right)$. By the Invariance of Domain Theorem (see, e.g. Kulpa, 1998), the image $f\left(\tilde{\Theta}_{*}\right)$ is therefore an open subset of $\mathbb{R}^{m}$. But then, for any coefficient vector $b \in f\left(\tilde{\Theta}_{*}\right)$, there exists another coefficient vector $b^{\prime} \in f\left(\tilde{\Theta}_{*}\right)$ such that $b^{\prime} \neq b$ but still $b_{j i}=b_{j i}^{\prime}$ for all $1 \leq i<j \leq n$ and $j \neq v-$ in other words, such that $\pi(b)=\pi\left(b^{\prime}\right)$. Since $f$ is injective, the vectors $b$ and $b^{\prime}$ originate from different edge parameter vectors $\theta=f^{-1}(b)$ and $\theta^{\prime}=f^{-1}\left(b^{\prime}\right)$ in $\tilde{\Theta}_{*}$. But

$$
\pi(f(\theta))=\pi(b)=\pi\left(b^{\prime}\right)=\pi\left(f\left(\theta^{\prime}\right)\right)
$$

so that the edge weight vectors $\theta$ and $\theta^{\prime}$ induce the same distribution of $X_{V \backslash v}$. We conclude that the parameter $\theta$ is not identifiable from the distribution of $X_{V \backslash v}$.

# C. 2 Proof of Proposition 4.2 

When reading the proof, the following perspective may help. Recall the notation in equations (12) and (20). The knowledge of the (simple max-stable) distribution of $X_{U}$ implies the knowledge of its angular measure $H_{U}$ and thus of the unordered collection of pairs of atoms and masses $\left(\omega_{r}, \mu_{r}\right)$ for $r=1, \ldots, s$. The vector $X_{U}$ can itself be represented as a max-linear model with $s$ independent factors and coefficient vectors $\beta_{r}=\mu_{r} \omega_{r}$ for $r=1, \ldots, s$. We first need to ensure that we can match

those vectors $\beta_{r}$ in a unique way to the max-linear coefficient vectors $\left(b_{v i}\right)_{v \in U}$ for $i \in V$; note that the coordinates $v$ of those vectors are restricted to $U$. Next, from the latter vectors, we need to recover the edge coefficients $\theta=\left(c_{v}\right)_{v \in E}$.

Proof of sufficiency (if) part of Proposition 4.2. We assume (I1) and (I2). In the first step of the proof we show that the angular measure of $X_{U}$ in (20) is composed of $|V|$ distinct atoms and that we can associate every atom in $\left\{\omega_{r}: r=1, \ldots,|V|\right\}$ to some node $v \in V$ and accordingly be able to associate it to one of the atoms $a_{i, U}=\left(b_{v i} / m_{i, U}\right)_{v \in U}$ for $i \in V$. For this, we focus on the nature of the atoms $\left\{a_{i, U}\right\}$, given the conditions (I1) and (I2). As a consequence, the max-linear coefficient matrix $b_{U \times V}=\left(b_{v i}\right)_{v \in U, i \in V}$ can be recovered from the distribution of $X_{U}$. In Step 2, we show how to recover from this matrix the edge parameters $\theta=\left(c_{v}\right)_{v \in E}$.
Step 1. Recall the representation $H_{U}=\sum_{i \in V} m_{i, U} \delta_{a_{i, U}}$ in (12) of the angular measure of $X_{U}$. We shall show that all $|V|$ masses $m_{i, U}$ are positive and that all $|V|$ atoms $a_{i, U}$ are distinct. Moreover, we will show how to match the atoms to the nodes, that is, given an atom $\omega \in\left\{\omega_{r}: r=1, \ldots,|V|\right\}$ how to identify the node $i \in V$ such that $\omega=a_{i, U}$.
All $|V|$ vectors $\left\{a_{i, U}\right\}$ have positive masses $\left\{m_{i, U}\right\}$. Recall $m_{i, U}=\sum_{v \in U} b_{v i}$ and recall from (18) that $b_{v i}>0$ if and only if $v \in \operatorname{Desc}(i)$. It follows that $m_{i, U}=0$ if and only if $\operatorname{Desc}(i) \cap U=\varnothing$ or, in other words, $\operatorname{Desc}(i) \subseteq \bar{U}$. But this is impossible since $\operatorname{Desc}(i)$ contains at least one leaf node, that is, a node without children, and such a node belongs to $U$ by (I1). We conclude that $m_{i, U}>0$ for all $i \in V$.
All $|V|$ vectors $\left\{a_{i, U}\right\}$ are distinct. By (22) it follows that whenever for two different nodes $i, j \in V$ we have $\operatorname{Desc}(i) \cap U \neq \operatorname{Desc}(j) \cap U$ then we can find two atoms, say $\omega^{\prime}$ and $\omega^{\prime \prime}$, within the set $\left\{\omega_{r}\right\}$ such that $\omega^{\prime}=a_{i, U}$ and $\omega^{\prime \prime}=a_{j, U}$. Because $\operatorname{Desc}(i) \cap U \neq \operatorname{Desc}(j) \cap U$ then necessarily $a_{i, U} \neq a_{j, U}$. Suppose however for two different nodes $i, j \in V$ we have $a_{i, U}=a_{j, U}$. This means that for the $u$-th and $j$-th elements of these vectors we have

$$
a_{i, u ; U}=a_{j, u ; U} \Longleftrightarrow \frac{b_{u i}}{m_{i}}=\frac{b_{u j}}{m_{j}} \quad \text { and } \quad a_{i, j ; U}=a_{j, j ; U} \Longleftrightarrow \frac{b_{j i}}{m_{i}}=\frac{b_{j j}}{m_{j}}
$$

Considering the ratios above, we should also have

$$
\frac{a_{i, u ; U}}{a_{i, j ; U}}=\frac{a_{j, u ; U}}{a_{j, j ; U}} \quad \Longleftrightarrow \quad \frac{b_{u i}}{b_{j i}}=\frac{b_{u j}}{b_{j j}}
$$

Because $a_{i, U}=a_{j, U}$ necessarily $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$. By Lemma C.1.2 there exists a node $u$ such that one of the edge sets $\{(i, j),(i, u),(j, u)\}$ or $\{(j, i),(i, u),(j, u)\}$ is contained in $E$. Without loss of generality, suppose this holds for the first triple. Also, by Lemma C.1.2 there cannot be another node $k$ with $\operatorname{Desc}(k) \cap U=\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$.

Suppose first $j, u \in U$. From the identities

$$
b_{j i}=c_{i j} b_{i i}, \quad b_{u i}=c_{i u} b_{i i}, \quad b_{u j}=c_{j u} b_{j j}
$$

and the criticality requirement

$$
c_{i u}>c_{i j} c_{j u}
$$

we have

$$
\frac{b_{u i}}{b_{j i}}>\frac{b_{u j}}{b_{j j}}
$$

This inequality shows that (36) cannot happen, hence we cannot have $a_{i, U}=a_{j, U}$. This means that all $|V|$ atoms are distinct.

Next suppose $j, u \in \bar{U}$. By Lemma C.1.1, there exist nodes $j^{\prime}, u^{\prime} \in U$ such that $j^{\prime} \in \operatorname{desc}(j)$ and $u^{\prime} \in \operatorname{desc}(u)$ and the paths $p\left(j, j^{\prime}\right)$ and $p\left(u, u^{\prime}\right)$ satisfy the properties in the said lemma. Because all nodes on the path $p\left(j, j^{\prime}\right)$ except possibly for $j$ have a unique parent, the path $p\left(j, j^{\prime}\right)$ cannot pass through $u$ (which has parents $i$ and $j$ ), and thus $j^{\prime} \neq u^{\prime}$. As $i$ is a parent of $j$, the shortest (and in fact the only) path from $i$ to $j^{\prime}$ is the one that concatenates the edge $(i, j)$ with $p\left(j, j^{\prime}\right)$ (Lemma C.1.1). It follows that

$$
b_{j^{\prime} i}=c_{p\left(j, j^{\prime}\right)} c_{i j} b_{i i} \quad \text { and } \quad b_{j^{\prime} j}=c_{p\left(j, j^{\prime}\right)} b_{j j}
$$

By a similar argument, the path that concatenates the edge $(i, u)$ with the path $p\left(u, u^{\prime}\right)$ is the unique shortest path from $i$ to $u^{\prime}$, while the path that concatenates $(j, u)$ with $p\left(u, u^{\prime}\right)$ is the unique shortest path from $j$ to $u^{\prime}$. It follows that

$$
b_{u^{\prime} i}=c_{p\left(u, u^{\prime}\right)} c_{i u} b_{i i} \quad \text { and } \quad b_{u^{\prime} j}=c_{p\left(u, u^{\prime}\right)} c_{j u} b_{j j}
$$

Combining these equalities, $c_{i u}>c_{i j} c_{j u}$ implies that we should have

$$
\frac{b_{u^{\prime} i}}{b_{u^{\prime} j}}>\frac{b_{j^{\prime} i}}{b_{j^{\prime} j}}
$$

However from $a_{i, U}=a_{j, U}$ we have for the $u^{\prime}$-th and $j^{\prime}$-th elements of these vectors

$$
a_{i, u^{\prime} ; U}=a_{j, u^{\prime} ; U} \Longleftrightarrow \frac{b_{u^{\prime} i}}{m_{i}}=\frac{b_{u^{\prime} j}}{m_{j}} \quad \text { and } \quad a_{i, j^{\prime} ; U}=a_{j, j^{\prime} ; U} \Longleftrightarrow \frac{b_{j^{\prime} i}}{m_{i}}=\frac{b_{j^{\prime} j}}{m_{j}}
$$

Considering the ratios above, we should also have

$$
\frac{a_{i, u^{\prime} ; U}}{a_{i, j^{\prime} ; U}}=\frac{a_{j, u^{\prime} ; U}}{a_{j, j^{\prime} ; U}} \quad \Longleftrightarrow \quad \frac{b_{u^{\prime} i}}{b_{u^{\prime} j}}=\frac{b_{j^{\prime} i}}{b_{j^{\prime} j}}
$$

Because of (41) the equalities in (42) cannot happen, hence we cannot have $a_{i, U}=a_{j, U}$.
The analysis of the cases $(j, s) \in U \times \bar{U}$ and $(j, s) \in \bar{U} \times U$ is similar. This shows that all $|V|$ vectors $a_{i, U}$ for $i \in V$ are different and because of (21), all vectors $\omega_{r}$ for $r \in\{1, \ldots,|V|\}$ are different too.
Distinguishing all atoms $a_{i, U}$ with zeroes on the same positions. For two different nodes $i, j \in V$, the atoms $a_{i, U}$ and $a_{j, U}$ have the same supports $\left\{v \in U: a_{v i}>0\right\}=\left\{v \in U: a_{v j}>0\right\}$ when $\operatorname{Desc}(i) \cap U=\operatorname{Desc}(j) \cap U$. By Lemma C.1.2-5 there cannot be any other node $k \in V \backslash\{i, j\}$ with the same descendants in $U$. In the representation

$$
H_{\theta, U}=\sum_{t \in V} m_{t, U} \delta_{a_{t, U}}=\sum_{r=1}^{|V|} \mu_{r} \delta_{\omega_{r}}
$$

there are thus exactly two atoms, $\omega$ and $\omega^{\prime}$, say, with the same indices of non-zero coordinates as $a_{i, U}=\left(b_{v i} / m_{i, U}\right)_{v \in V}$ and $a_{j, U}=\left(b_{v j} / m_{j, U}\right)_{v \in V}$. The question is then how to know whether $\omega=a_{i, U}$ and $\omega^{\prime}=a_{j, U}$ or vice versa, $\omega=a_{j, U}$ and $\omega^{\prime}=a_{i, U}$. Let $\mu$ and $\mu^{\prime}$ be the masses of $\omega$ and $\omega^{\prime}$, respectively, and consider the vectors $\beta=\mu \omega$ and $\beta^{\prime}=\mu^{\prime} \omega^{\prime}$. An equivalent question is then how to identify $\beta$ and $\beta^{\prime}$ with the two max-linear coefficient vectors $\left(b_{v i}\right)_{v \in U}$ and $\left(b_{v j}\right)_{v \in U}$.

By Lemma C.1.2-2 to 4, we can suppose that $i$ is the unique parent of $j$ and that $i$ and $j$ have a common child $u$. The analysis is now to be split up into different cases, according to whether $j$ and $u$ belong to $U$ or not. Recall that $b_{v i}=c_{p(i, v)} b_{i i}$ and $b_{v j}=c_{p(j, v)} b_{j j}$ for $v \in \operatorname{Desc}(j) \subset \operatorname{Desc}(i)$.

Suppose first that $j, u \in U$. From (37) we deduce (38) thanks to the criticality assumption. In order to make the correct assignment of the two vectors $\beta=\left(\beta_{v}\right)_{v \in U}$ and $\beta^{\prime}=\left(\beta_{v}^{\prime}\right)_{v \in U}$ to the nodes $i$ and $j$, we need to check the inequality (38). If $\beta_{u} / \beta_{j}>\beta_{u}^{\prime} / \beta_{j}^{\prime}$ then we assign the vector $\beta$ to the node $i$ and the vector $\beta^{\prime}$ to the node $j$. If the equality is reversed, we do the assignment the other way around.

Next suppose that $j, u \in \bar{U}$. According to Lemma C.1.1, there exist nodes $j^{\prime}, u^{\prime} \in U$ so that there is a unique path from $j$ to $j^{\prime}$ and from $u$ to $u^{\prime}$. By Lemma C.1.1, the paths from $i$ to $u^{\prime}$ and $j^{\prime}$ and from $j$ to $j$ to $u^{\prime}$ are

$$
p\left(i, u^{\prime}\right)=\{(i, u)\} \cup p\left(u, u^{\prime}\right), \quad p\left(i, j^{\prime}\right)=\{(i, j)\} \cup p\left(j, j^{\prime}\right), \quad p\left(j, u^{\prime}\right)=\{(j, u)\} \cup p\left(u, u^{\prime}\right)
$$

We have the same identities in (39) and (40) which, together with the criticality assumption, lead to the inequality (41). In order to make the correct assignment of the two vectors $\beta=\left(\beta_{v}\right)_{v \in U}$ and $\beta^{\prime}=\left(\beta_{v}^{\prime}\right)_{v \in U}$ we do as above for the case $j, u \in U$.

For the cases $(j, u) \in U \times \bar{U}$ and $(j, u) \in \bar{U} \times U$, we combine methods from the cases $(j, u) \in U \times U$ and $(j, u) \in \bar{U} \times \bar{U}$.

With this we finish the proof that we can learn the structure of every atom $\left\{\omega_{r}: r=1, \ldots,|V|\right\}$, i.e., for every $r=1, \ldots,|V|$ we can identify the unique node $i \in V$ such that $\omega_{r}=a_{i, U}=$ $\left(b_{v i} / m_{i, U}\right)_{v \in U}$. This means that we can also match every element $\beta$ in the collection of vectors $\left\{\beta_{r}: r=1, \ldots,|V|\right\}$ to the correct node $i \in V$ such that $\beta=\left(b_{v i}\right)_{v \in U}$.

Step 2. In the previous step, we have shown that the distribution of $X_{U}$ (together with the knowledge of the graph structure) determines the max-linear coefficient matrix $b_{U \times V}=\left(b_{v i}\right)_{v \in U, i \in V}$. Here, we show that this matrix suffices to reconstruct the vector of edge coefficients $\theta=\left(c_{v}\right)_{v \in E}$.

If $v$ is a child of $i$, then $p(i, v)=\{(i, v)\}$ and thus $b_{v i}=c_{i v} b_{i i}$. If both $i$ and $v$ belong to $U$, then, clearly, we can identify $c_{i v}=b_{v i} / b_{i i}$.

Let $i \in U$ with child $v \in \operatorname{ch}(i) \cap \bar{U}$. By Lemma C.1.1 there exists a node $v^{\prime} \in U$ such that there is a unique path from $v$ to $v^{\prime}$. Rewrite $v=v_{1}$ and $v^{\prime}=v_{n}$ and consider the node set $\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$ on that unique path. Using the fact that if a node $\ell$ has a single parent $k$, then $b_{\ell \ell}=1-c_{k \ell}$ (see (9)), we find the following identities for the max-linear coefficients $b_{v_{n} j}$ for $j \in\left\{v_{n}, \ldots, v_{2}, i\right\}$ :

$$
\begin{aligned}
b_{v_{n} v_{n}} & =1-c_{v_{n-1} v_{n}} \\
b_{v_{n} v_{n-1}} & =c_{p\left(v_{n-1}, v_{n}\right)} b_{v_{n-1} v_{n-1}}=c_{v_{n-1} v_{n}}\left(1-c_{v_{n-2} v_{n-1}}\right) \\
& \vdots \\
b_{v_{n} v_{2}} & =c_{p\left(v_{2}, v_{n}\right)} b_{v_{2} v_{2}}=c_{v_{2} v_{3}} \cdots c_{v_{n-1} v_{n}}\left(1-c_{v_{1} v_{2}}\right) \\
b_{v_{n} i} & =c_{p\left(i, v_{n}\right)} b_{i i}=c_{i v_{1}} c_{v_{1} v_{2}} c_{v_{2} v_{3}} \cdots c_{v_{n-1} v_{n}} b_{i i}
\end{aligned}
$$

From the first equation we identify $c_{v_{n-1} v_{n}}$, from the second $c_{v_{n-2} v_{n-1}}$ and so on until we identify $c_{v_{1} v_{2}}$ from the penultimate equation. From the last equation we can identify $c_{i v_{1}}$ because $b_{i i}$ is available from $b_{U \times V}$ in view of $i \in U$.

The next step of the proof is to extract the edge parameters between a node with latent variable and its children.

Let $i \in \bar{U}$. We will show that we can identify all edge weights $c_{i j}$ for $j \in \operatorname{ch}(i)$. Because $i$ belongs to $\bar{U}$, it should have at least two children, say $v$ and $\bar{v}$. Take $v$ to be a node whose only parent is $i$. Note that we can always find such a node by Lemma C.1.1. Let us first assume $v, \bar{v} \in U$. Because $v$ has only one parent, we have $b_{v v}=1-c_{i v}$ and thus $c_{i v}=1-b_{v v}$. We also know $b_{v i}=c_{i v} b_{i i}$ and from here $b_{i i}=b_{v i} / c_{i v}=b_{v i} /\left(1-b_{v v}\right)$. From $b_{\bar{v} i}=c_{i \bar{v}} b_{i i}$ we deduce $c_{i \bar{v}}=b_{\bar{v} i}\left(1-b_{v v}\right) / b_{v i}$. Hence we have identified all the edge parameters related to children of $i$ which are observable, provided $i$ has two or more children in $U$.

Next assume that both $v, \bar{v} \in \bar{U}$. By Lemma C.1.1, there exists a node $v^{\prime} \in \operatorname{desc}(v) \cap U$ such that there is a unique path from $v$ to $v^{\prime}$ and which has the properties in the cited statement. Let the sequence of nodes along which the path passes be denoted by $\left\{v_{1}=v, v_{2}, \ldots, v_{n}=v^{\prime}\right\}$. Using again that for a node $\ell$ with single parent $k, b_{\ell \ell}=1-c_{k \ell}$ (see (9)), we find the same identities as in (43) for the max-linear coefficients $b_{v_{n} j}$ for $j \in\left\{v_{n}, \ldots, v_{2}\right\}$. From the first equation we obtain $c_{v_{n-1} v_{n}}=1-b_{v_{n} v_{n}}$, from the second equation $c_{v_{n-2} v_{n-1}}=1-b_{v_{n} v_{n-1}} /\left(1-b_{v_{n} v_{n}}\right)$ and so on until we obtain $c_{v_{1} v_{2}}$ from the penultimate equation in (43). Because we assumed $\mathrm{pa}\left(v_{1}\right)=\{i\}$ we have $b_{v_{1} v_{1}}=1-c_{i v_{1}}$ and thus

$$
b_{v_{n} v_{1}}=c_{p\left(v_{1}, v_{n}\right)} b_{v_{1} v_{1}}=c_{v_{1} v_{2}} c_{v_{2} v_{3}} \cdots c_{v_{n-1} v_{n}}\left(1-c_{i v_{1}}\right)
$$

from where we identify $c_{i v_{1}}$. Since $v_{n} \in U$, all coefficients $b_{v_{n} j}$ for $j \in V$ are contained in the max-linear coefficient matrix $b_{U \times V}$. The procedure just described thus allows us to compute all edge coefficients $c_{i v_{1}}, c_{v_{1} v_{2}}, \ldots, c_{v_{n-1} v_{n}}$.

Because the path $p\left(v_{1}, v_{n}\right)$ satisfies the properties in Lemma C.1.1, and in view of the same lemma, plus the fact that the only parent of $v_{1}=v$ is $i$, it follows that the path $\left\{\left(i, v_{1}\right)\right\} \cup p\left(v_{1}, v_{n}\right)$ is the unique path between $i$ and $v_{n}$. Hence we have also

$$
b_{v_{n} i}=c_{p\left(i, v_{n}\right)} b_{i i}=c_{i v_{1}} c_{v_{1} v_{2}} c_{v_{2} v_{3}} \cdots c_{v_{n-1} v_{n}} b_{i i}
$$

As $v_{n} \in U$, the value of $b_{v_{n} i}$ is known from $b_{U \times V}$. The edge coefficients on the right-hand side were expressed in terms of $b_{U \times V}$ in the previous paragraph. From there, we obtain the value of $b_{i i}$, which will be used next.

Now consider the node $\bar{v}$, renamed to $\bar{v}_{1}$, which was an arbitrary child of $i$. For $\bar{v}=\bar{v}_{1}$ too, we can find a node $\bar{v}_{m} \in U$ and a sequence of nodes $\left\{\bar{v}_{2}, \ldots, \bar{v}_{m}\right\}$ according to Lemma C.1.1 satisfying the properties stated there. For all $r \in\{2, \ldots, m\}$, the node $\bar{v}_{r}$ has a unique parent, $\bar{v}_{r-1}$. We have

the following equalities, using again by $b_{\ell \ell}=1-c_{k \ell}$ for a node $\ell$ with unique parent $k$

$$
\begin{aligned}
b_{\bar{v}_{m} \bar{v}_{m}} & =1-c_{\bar{v}_{m-1} \bar{v}_{m}} \\
b_{\bar{v}_{m} \bar{v}_{m-1}} & =c_{p\left(\bar{v}_{m-1}, \bar{v}_{m}\right)} b_{\bar{v}_{m-1} \bar{v}_{m-1}}=c_{\bar{v}_{m-1} \bar{v}_{m}}\left(1-c_{\bar{v}_{m-2} \bar{v}_{m-1}}\right) \\
\vdots & \\
b_{\bar{v}_{m} \bar{v}_{2}} & =c_{p\left(\bar{v}_{2}, \bar{v}_{m}\right)} b_{\bar{v}_{2} \bar{v}_{2}}=c_{\bar{v}_{2} \bar{v}_{3}} \cdots c_{\bar{v}_{m-1} \bar{v}_{m}}\left(1-c_{\bar{v}_{1} \bar{v}_{2}}\right) \\
b_{\bar{v}_{m} i} & =c_{p\left(i, \bar{v}_{m}\right)} b_{i i}=c_{i \bar{v}_{1}} c_{\bar{v}_{1} \bar{v}_{2}} c_{\bar{v}_{2} \bar{v}_{3}} \cdots c_{\bar{v}_{m-1} \bar{v}_{m}} b_{i i}
\end{aligned}
$$

In the last equality we used that the path $\left\{\left(i, \bar{v}_{1}\right)\right\} \cup p\left(\bar{v}_{1}, \bar{v}_{m}\right)$ is the unique shortest one between $i$ and $\bar{v}_{m}$, because of Lemma C.1.1 and because $p\left(\bar{v}_{1}, \bar{v}_{m}\right)$ satisfies the properties 1-2 of the same lemma. Since $\bar{v}_{m} \in U$, the values of the left-hand sides in the previous equations are contained in the given matrix $b_{U \times V}$. From the first equality we obtain $c_{\bar{v}_{m-1} \bar{v}_{m}}$, from the second one $c_{\bar{v}_{m-2} \bar{v}_{m-1}}$ and so on until we identify $c_{\bar{v}_{1} \bar{v}_{2}}$ from the penultimate equality, i.e., all edge parameters linked to $p\left(\bar{v}_{1}, \bar{v}_{m}\right)$. In the last equation above we replace $b_{i i}$ with the expression derived from (44) and we obtain the parameter $c_{i \bar{v}_{1}}$.

If some of the children of $i$ are in $U$ and some others are in $\bar{U}$, we apply a combination of the techniques used in the two cases described above - when two children are in $U$ or when two children are in $\bar{U}$.

This concludes the proof of the sufficiency (if) part.
Proof of necessity (only if) part in Proposition 4.2. Let $\bar{U} \subset V$ be such that at least one of the two conditions (I1) and (I2) is not satisfied and let $\theta=\left(c_{e}\right)_{e \in E} \in \hat{\Theta}_{*}$. We will show that there exists another parameter $\theta^{\prime}=\left(c_{e}^{\prime}\right)_{e \in E} \in \hat{\Theta}_{*}$ such that $\theta^{\prime} \neq \theta$ but the distribution of $X_{V \backslash u}$ under $\theta^{\prime}$ is the same as the one under $\theta$.

We consider two cases: case (1) (I2) does not hold, i.e., there exists $u \in \bar{U}$ which is not the source of any tournament in $\mathcal{T}$; case (2) (I2) holds but not (I1), i.e., every $u \in \bar{U}$ is the source of some tournament in $\mathcal{T}$ but there exists $u \in \bar{U}$ with less than two children.
Case (1): there exists $u \in \bar{U}$ which is not the source of any tournament in $\mathcal{T}$. Then $u$ belongs to only a single tournament, say $\tau=\left(V_{\tau}, E_{\tau}\right)$; indeed, a node that belongs to two different tournaments must be the source of at least one of them, because otherwise it would have parents from two different tournaments, yielding a forbidden v-structure.

Let $X_{V_{\tau}}$ be a max-linear model restricted to a single tournament, $\tau$. The coefficients associated to $X_{V_{e}}$, denote by $b_{\epsilon i}^{*}$ for $v, i \in V_{\tau}$, are determined by the weights of the edges $e \in E_{\tau}$. By Lemma C.1.4, we can modify the edge weights $c_{e}$ for $e \in E_{\tau}$ in such a way that the max-linear coefficients $b_{\epsilon i}^{*}$ for $v \in V_{\tau} \backslash u$ and $i \in V_{\tau}$ remain unaffected. Let $\tilde{c}_{e}$ for $e \in E_{\tau}$ denote such a modified vector of edge weights. Define $\theta^{\prime}=\left(c_{e}^{\prime}\right)_{e \in E} \in \hat{\Theta}_{*}$ by

$$
c_{e}^{\prime}= \begin{cases}\tilde{c}_{e} & \text { if } e \in E_{\tau} \\ c_{e} & \text { if } e \in E \backslash E_{\tau}\end{cases}
$$

Then $\theta^{\prime} \in \hat{\Theta}_{*}$ too: indeed, $c_{i i}^{\prime}>0$ for all $i \in V$ by assumption on $\theta$ and the fact the vector $\left(\tilde{c}_{e}: e \in E_{\tau}\right)$ satisfies $\tilde{c}_{i i}>0$ for $i \in V_{\tau}$. By construction, the distribution of $X_{V_{e} \backslash u}$ is the same under $\theta^{\prime}$ as under $\theta$.

We show that the distribution of $X_{V \backslash u}$ under $\theta^{\prime}$ is the same as the one under $\theta$. We proceed by induction on the number of tournaments.

If $\mathcal{T}$ consists of a single tournament, then $\mathcal{T}=\tau$ and there is nothing more to show.
So suppose $\mathcal{T}$ consists of $m \geq 2$ tournaments. The skeleton graph of $\mathcal{T}$ is a block graph and thus a decomposable graph. By the running intersection property, we can order the tournaments $\tau_{1}, \ldots, \tau_{m}$ with node sets $V_{1}, \ldots, V_{m}$ in such a way that $\tau_{1}=\tau$, the tournament containing $u$, and such that $V_{m} \cap\left(V_{1} \cup \ldots \cup V_{m-1}\right)$ is a a singleton, say $\{s\}$. Then $s \neq u$ since $u$ belongs to only a single tournament.

Write $W=V_{1} \cup \ldots \cup V_{m-1} \backslash u$. The joint distribution of $X_{V \backslash u}$ can be factorized into two parts: first, the distribution of $X_{W}$ and second, the conditional distribution of $X_{V_{m} \backslash s}$ given $X_{W}$. It is sufficient to show that both parts remain the same when $\theta$ is replaced by $\theta^{\prime}$.

- By the induction hypothesis, the distribution of $X_{W}$ is the same under $\theta^{\prime}$ as under $\theta$.

- By the global Markov property (Proposition 3.3), the conditional distribution of $X_{V_{m} \backslash s}$ given $X_{W}$ is the same as the conditional distribution of $X_{V_{m} \backslash s}$ given $X_{s}$. But the latter is determined by the joint distribution of $X_{V_{m}}$, which, in turn, only depends on the weights of the edges $e$ in $\tau_{m}$. By construction, these edge weights are the same under $\theta$ as under $\theta^{\prime}$. It follows that the conditional distribution of $X_{V_{m} \backslash u}$ given $X_{W}$ is the same under $\theta^{\prime}$ as under $\theta$.

We conclude that the distribution of $X_{V \backslash u}$ is the same under $\theta^{\prime}$ as under $\theta$. Since $\theta \neq \theta^{\prime}$, the parameter is not identifiable.

Case (2): any $u \in \bar{U}$ is the source of some tournament in $\mathcal{T}$ but there exists $u \in \bar{U}$ with less than two children. Any $u \in \bar{U}$ must have at least one child (a node without children cannot be the source of a tournament). But then there exists $u \in \bar{U}$ with exactly one child: $\operatorname{ch}(u)=\{w\}$. The tournament of which $u$ is the source can only consist of the nodes $u$ and $w$ and the edge $(u, w)$. Now there are two subcases, depending on whether $u$ has any parents or not.

Case (2).a: $u$ has no parents. Then $u$ is the source node of $\mathcal{T}$ with a single child $w$. Removing the node $u$ yields the ttt $\mathcal{T}_{\backslash u}:=(V \backslash u, E \backslash\{(u, w)\})$ with single source $w$. The random vector $X_{V \backslash u}$ follows the recursive max-linear model (2) with respect to $\mathcal{T}_{\backslash u}$. Its distribution is determined by the coefficients $c_{e}$ for $e \in E \backslash\{(u, w)\}$. The value of $c_{u w}$ can thus be chosen arbitrarily in $(0,1)$ without affecting the distribution of $X_{V \backslash u}$.

Case (2).b: $u$ has parents. Any ancestor of $w$ different from $u$ must be an ancestor of $u$ too, since otherwise there would be a v-structure at $w$; therefore,

$$
\operatorname{An}(w)=\operatorname{an}(u) \cup\{u, w\}
$$

Let $\lambda>0$ and close enough to 1 (as specified below). Define $\theta^{\prime}=\left(c_{e}^{\prime}\right)_{e \in E}$ by modifying the weights of edges adjacent to $u$ : specifically,

$$
\begin{aligned}
c_{j u}^{\prime} & =\lambda c_{j u}, \quad j \in \operatorname{pa}(u) \\
c_{u w}^{\prime} & =\lambda^{-1} c_{u w} \\
c_{e}^{\prime} & =c_{e}, \quad e \in E \backslash[\{(j, u): j \in \operatorname{pa}(u)\} \cup\{(u, w)\}]
\end{aligned}
$$

In words, $\theta^{\prime}$ coincides with $\theta$ for edges $e$ that do not involve $u$, and $\theta^{\prime}=\theta$ if and only if $\lambda=1$. Since the parameter space $\hat{\Theta}_{*}$ is open, $\theta^{\prime}$ belongs to $\hat{\Theta}_{*}$ for $\lambda$ sufficiently close to 1 . We claim that the distribution of $X_{V \backslash u}$ is invariant under $\lambda$. Hence, for $\lambda$ different from but sufficiently close to 1 , we have found a parameter $\theta^{\prime} \neq \theta$ producing the same distribution of $X_{V \backslash u}$ as $\theta$.

Under $\theta^{\prime}$, the random vector $X_{V \backslash u}$ follows the max-linear model

$$
X_{v}=\bigvee_{i \in \operatorname{An}(v)} b_{v i}^{\prime} Z_{i}, \quad v \in V \backslash u
$$

where $\left(Z_{i}\right)_{i \in V}$ is a vector of independent unit-Fréchet random variables and where the coefficients $b_{v i}^{\prime}$ are given by equations (4), (5) and (6) with $c_{e}$ replaced by $c_{e}^{\prime}$.

First, suppose $v \in V \backslash u$ is not a descendant of $u$. Then for any $i \in \operatorname{An}(v)$, the coefficient $b_{v i}^{\prime}$ is a function of edge weights $c_{e}^{\prime}$ for edges $e \in E$ different from $(u, w)$ and from $(j, u)$ for $j \in \mathrm{pa}(u)$. It follows that $c_{e}^{\prime}=c_{e}$ for such edges and thus $b_{v i}^{\prime}=b_{v i}$ for $v \in V \backslash \operatorname{Desc}(u)$ and $i \in \operatorname{An}(v)$.

Second, suppose $v \in \operatorname{desc}(u)$. Then necessarily $v \in \operatorname{Desc}(w)$ too and for any $i \in \operatorname{An}(u)$, the path $p(i, v)$ passes by (or arrives in) $w$. Furthermore, any ancestor of $v$ not in $\operatorname{An}(w)$ is a descendant of $w$ :

$$
\operatorname{An}(v)=\operatorname{an}(u) \cup\{u, w\} \cup[\operatorname{desc}(w) \cap \operatorname{An}(v)]
$$

It follows that

$$
X_{v}=\bigvee_{i \in \operatorname{an}(u)} b_{v i}^{\prime} Z_{i} \vee\left(b_{v u}^{\prime} Z_{u} \vee b_{v w}^{\prime} Z_{w}\right) \vee \bigvee_{i \in \operatorname{desc}(w) \cap \operatorname{An}(v)} b_{v i}^{\prime} Z_{i}
$$

where the last term on the right-hand side is to be omitted if $v=w$. We treat each of the three terms on the right-hand side separately.

- For $i \in \operatorname{an}(u)$, we have

$$
b_{v i}^{\prime}=c_{i i}^{\prime} c_{p(i, v)}^{\prime}=c_{i i}^{\prime} c_{p(i, u)}^{\prime} c_{u w}^{\prime} c_{p(w, v)}^{\prime}
$$

where $c_{p(w, v)}^{\prime}=1$ if $v=w$. The coefficients $c_{i i}^{\prime}$ and $c_{p(w, v)}^{\prime}$ only involve weights $c_{e}^{\prime}$ for edges $e \in E$ different from $(u, w)$ and $(j, u)$ for $j \in \mathrm{pa}(u)$; it follows that $c_{i i}^{\prime}=c_{i i}$ and $c_{p(w, v)}^{\prime}=c_{p(w, v)}$. Further, given $i \in \operatorname{an}(u)$ there exists $j \in \mathrm{pa}(u)$ such that $p(i, u)$ passes by $j$ right before reaching $u$ (with $i=j$ if $i \in \mathrm{pa}(u)$ ), and then

$$
c_{p(i, u)}^{\prime} c_{u w}^{\prime}=c_{p(i, j)}^{\prime} c_{j u}^{\prime} c_{u w}^{\prime}=c_{p(i, j)}^{\prime}\left(\lambda c_{j u}\right)\left(\lambda^{-1} c_{u w}\right)
$$

Since $p(i, j)$ does not involve edges meeting $u$, we find that $c_{p(i, j)}^{\prime}=c_{p(i, j)}$, so that the above expression does not depend on $\lambda$. We conclude that $b_{v i}^{\prime}=b_{v i}$ for $i \in \operatorname{an}(u)$.

- If $v \in \operatorname{desc}(w)$ and $i \in \operatorname{desc}(w) \cap \operatorname{An}(v)$, the coefficient $b_{v i}^{\prime}$ is

$$
b_{v i}^{\prime}=c_{i i}^{\prime} c_{p(i, v)}^{\prime}
$$

The path $p(i, v)$ does not involve edges touching $u$, so $c_{p(i, v)^{\prime}}=c_{p(i, v)}$. By Lemma C.1.3, the coefficient $c_{i i}^{\prime}=b_{i i}^{\prime}$ is a function of the edge weights $c_{e}^{\prime}$ for edges $e$ in the tournament shared by $i$ and its parents. Since $i \in \operatorname{desc}(w)$ and since $w$ is the only child of $u$, none of these edges touches $u$, and thus $c_{e}^{\prime}=c_{e}$ for all such edges. It follows that $c_{i i}^{\prime}=c_{i i}$ too. We conclude that $b_{v i}^{\prime}=b_{v i}$ for $v \in \operatorname{desc}(w)$ and $i \in \operatorname{desc}(w) \cap \operatorname{An}(v)$.

- The random variable $b_{v u}^{\prime} Z_{u} \vee b_{v w}^{\prime} Z_{w}$ is independent of all other variables $Z_{i}$ for $i \in V \backslash\{u, w\}$ and its distribution is equal to $\left(b_{v u}^{\prime}+b_{v w}^{\prime}\right) Z$ for $Z$ a unit-Fréchet variable. We will show that $b_{v u}^{\prime}+b_{v w}^{\prime}$ does not depend on $\lambda$. Since $1=\sum_{i \in \operatorname{An}(v)} b_{v i}^{\prime}$, the partition (45) yields

$$
b_{v u}^{\prime}+b_{v w}^{\prime}=1-\sum_{i \in \operatorname{an}(u)} b_{v i}^{\prime}-\sum_{i \in \operatorname{desc}(w) \cap \operatorname{An}(v)} b_{v i}^{\prime}
$$

(The last sum on the right-hand side is zero if $v$ is not a descendant of $w$.) In the two previous bullet points, we have already shown that the coefficients $b_{v i}^{\prime}$ for $i$ in an $(u)$ or $\operatorname{desc}(w) \cap \operatorname{An}(v)$ do not depend on $\lambda$. By the stated identity, the sum $b_{v u}^{\prime}+b_{v w}^{\prime}$ then does not depend on $\lambda$ either.

We have thus shown that if $\bar{U}$ does not satisfy (I1)-(I2), then we can find $u \in \bar{U}$ such that the distribution of $X_{V \backslash u}$ is the same under $\theta^{\prime}$ as under $\theta$. As $\theta^{\prime} \neq \theta$ by construction, this means that the parameter $\theta$ is not identifiable from the distribution of $X_{V \backslash u}$. But as $U=V \backslash \bar{U} \subseteq V \backslash\{u\}$, the parameter $\theta$ is not identifiable from the distribution of $X_{U}$ either. This confirms the necessity of (I1)-(I2) for the identifiability of $\theta$ from the distribution of $X_{U}$.

# Acknowledgements 

The comments and suggestions by two anonymous Reviewers have been greatly helpful in the preparation of the final version of the manuscript. Stefka Asenova is particularly grateful to Eugen Pircalabelu and Ngoc Tran for their availability and precious help.
