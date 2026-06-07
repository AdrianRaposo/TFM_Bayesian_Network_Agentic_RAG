# Ranked Enumeration of Minimal Triangulations 

Tracks: Exploration, Experimental

Noam Ravid<br>Technion<br>Haifa, Israel<br>noamrvd@cs.technion.ac.il

## Dori Medini

Technion
Haifa, Israel
dorimedi@campus.technion.ac.il

## Benny Kimelfeld

Technion
Haifa, Israel
bennyk@cs.technion.ac.il

## ABSTRACT

A tree decomposition of a graph facilitates computations by grouping vertices into bags that are interconnected in an acyclic structure; hence their importance in a plethora of problems such as query evaluation over databases and inference over probabilistic graphical models. The relative benefit from different tree decompositions is measured by diverse (sometime complex) cost functions that vary from one application to another. For generic cost functions like width and fill-in, an optimal tree decomposition can be efficiently computed in some cases, notably when the number of minimal separators is bounded by a polynomial (due to Bouchitte and Todinca); we refer to this assumption as "poly-MS." To cover the variety of cost functions in need, it has recently been proposed to devise algorithms for enumerating many decomposition candidates for applications to choose from using specialized, or even machinelearned, cost functions.

We explore the ability to produce a large collection of "high quality" tree decompositions. We present the first algorithm for ranked enumeration of the proper (non-redundant) tree decompositions, or equivalently minimal triangulations, under a wide class of cost functions that substantially generalizes the above generic ones. On the theoretical side, we establish the guarantee of polynomial delay if poly-MS is assumed, or if we are interested in tree decompositions of a width bounded by a constant. We describe an experimental evaluation on graphs of various domains (including join queries, Bayesian networks, treewidth benchmarks and random), and explore both the applicability of the poly-MS assumption and the performance of our algorithm relative to the state of the art.

## 1 INTRODUCTION

A tree decomposition of a graph $G$ is a tree $\mathcal{T}$ such that each vertex of $\mathcal{T}$ is associated with a bag of vertices of $G$, every edge of $G$ appears in at least one bag, and every vertex of $G$ occurs in a connected subtree of $\mathcal{T}$. Tree decompositions are useful in common scenarios where problems are intractable on general structures, yet tractable on acyclic ones. A beneficial tree decomposition allows for efficient computation. This benefit is typically estimated by a cost function, most popular being the width-the cardinality of

[^0]the largest bag (minus one), and the fill in-the number of missing edges among bag neighbors. The generalization to hypergraphs, generalized hypertree decomposition, is a tree decomposition of the primal graph (consisting of an edge between hyperedge neighbors) along with a cover of each bag by hyperedges, giving rise to specialized costs [18] such as (generalized) hypertree width [20, 21], and fractional hypertree width [32]. The applications of (ordinary and generalized) tree decompositions include optimization of join queries in databases [17, 40], solvers for constraint satisfaction problems [28], RNA analysis in bioinformatics [42], computation of Nash equilibria in game theory [17], inference in probabilistic graphical models [29], and weighted model counting [26].

Computing an optimal tree decomposition is NP-hard for the classic cost measures as the aforementioned ones. Therefore, heuristic algorithms are often used [2, 4]. But even regardless of the computational hardness, applications often require specialized costs that are not covered by the classics. For instance, for weighted model counting there are costs associated with the "CNF-tree" of the formula [18, 26]. In the work of Kalinsky et al. [25] on database join optimization, the execution cost is dominated by the effectiveness of the adhesions (intersection of neighboring bags) for caching, particularly the associated skew. They show real-life scenarios where isomorphic tree decompositions (of minimum width) feature orders-of-magnitude difference in performance. Mediero [33] aims at minimizing the size of AND/OR trees by seeking decompositions of a low height. Abseher et al. [1] designed a machine-learning framework to learn the cost function of a tree decomposition in various problems, using various features of the tree decomposition.

Motivated by the above need, Carmeli et al. [10] embarked on the challenge of enumerating tree decompositions; that is, generating tree decompositions one by one so that an application can stop the enumeration at any time and select the decomposition that best suits its needs. As they point out, it is essential to avoid of redundancy. For example, if a graph is already a tree, then there is no need to further group its vertices. Hence, following Carmeli et al. [10], we consider the task of enumerating the proper tree decompositions, which are intuitively the ones that cannot be improved by splitting a bag or removing it altogether. They showed that these tree decompositions are precisely the clique trees of the minimal triangulations. A triangulation of a graph $G$ is a chordal graph $H$ obtained from $G$ by adding edges, called fill edges. A triangulation $H$ is minimal if no triangulation $H^{\prime}$ has a strict subset of the fill edges. Carmeli et al. [10] proved that for enumerating tree decompositions, it suffices to enumerate the minimal triangulations. See Mediero [33] for an application of Carmeli et al. [10].

While algorithms for generating pools of tree decompositions have been proposed in the past for small graphs (representing



database queries) [40], Carmeli et al. [10] have presented the first algorithm that has both completeness and efficiency guarantees; that is, it can generate all minimal triangulations (and by implication all proper tree decompositions), and it does so in incremental polynomial time, which means that the time taken for producing the $N$ th result is polynomial in $N$ and in the size of the input [23]. Nevertheless, there can be exponentially many minimal triangulations, and an effective enumeration needs to produce earlier the triangulations that are likely to be low cost. In other words, we would like the algorithm to enumerate the minimal triangulations by increasing relevant cost such as width (of some version) or fill-in. In turn, the application will evaluate the complex cost function on each generated triangulation, and at a point of choice it will stop the enumeration and pick the best result found. Carmeli et al. [10] use heuristics to affect the enumeration order, but provide no guarantees. Without making assumptions it is impossible to guarantee efficient ranked enumeration for costs, as it is already NP-hard to compute the first (best) triangulation.

Yet, for some classes of graphs, there is a polynomial-time algorithm for computing a tree decomposition of a minimum weight/fillin. These include the (weakly) chordal graphs, interval graphs, circular-arc graphs, and cographs. These examples have the property we refer to poly-MS: having a polynomial number of minimal separators [14]. A minimal separator of a graph is a vertex set $S$ such that some vertices $u$ and $v$ are separated by $S$, but no proper subset of $S$ separates $u$ from $v$. Various problems have been studied in the context of the poly-MS assumption [14], including graph isomorphism [36]. Assuming poly-MS, a tree decomposition of a minimum weight or fill-in can be computed in polynomial time [8, 9].

The decomposition algorithm of Bouchitté and Todinca [8, 9] consists of two main steps. First, they construct the set of minimal separators of the input graph, for example using the algorithm of Berry et al. [3], and from these compute the set of all potential maximal cliques (which are essentially the bags of the proper tree decompositions) [9]. Second, they use the potential maximal cliques in order to find an optimal triangulation. In fact, their algorithm has two variants-one for minimal width (tree-width) and one for minimal fill-in. The second step has been later generalized to allow for positive weights on bags (in the case of width) and edges (in the case of fill) by Furuse and Yamazaki [15], again presenting two corresponding variants of their algorithm.

Our first contribution is a generalization of the concepts of width and fill-in to general cost functions over tree decompositions. These cost functions satisfy two properties. First, they assign the same cost to tree decompositions with the same bags; hence, these are essentially costs over the set of bags. Second, and more importantly, they are monotonic in the following (informal) sense. Suppose that we cut a tree decomposition $\mathcal{T}$ along an edge, and replace one of the sides with an alternative subtree (which is a tree decomposition of a subgraph of the original graph), resulting in a tree decomposition $\mathcal{T}^{\prime}$; if the altenative subtree does not cost more than the one it replaced, then the cost of $\mathcal{T}^{\prime}$ is no greater than that of $\mathcal{T}$. We call such a cost function split monotone, and refer the reader to Section 3 for the precise definition. Split-monotone cost functions generalize existing costs such as fill-in, width and generalized/fractional hypertree width, as well as the weighted width and fill-in of Furuse and Yamazaki [15]. Moreover, we can come up with various motivated
split-monotone costs that are not among the classic ones, such as the sum over the (exponents of the) bag cardinalities and linear combinations of width and fill-in. We present a generalization of the algorithm of Bouchitté and Todinca [8] to general split-monotone cost functions. As we explain later, the importance of supporting general cost functions is not just for the sake of a richer costs; even if we are interested just in width or fill-in, we need the flexibility of the cost function in order to incorporate constraints that we later use to devise our algorithm for ranked enumeration.

Our main theoretical contributions are algorithms that enumerate minimal triangulations by increasing cost, for any splitmonotone cost function that is polynomial-time computable (e.g., the aforementioned ones). The first algorithm enumerates all minimal triangulations, and does so with polynomial delay if the input is from a poly-MS class of graphs. The second enumerates all minimal triangulations of a bounded width, and it does so with polynomial delay if the bound on the width is a fixed constant. Polynomial delay [23] means that the time between every two consecutive answers is polynomial in the size of the input (graph), a guarantee that is stronger than incremental polynomial time. Due to the previously discussed connection between proper tree decompositions and minimal triangulations, we get algorithms with the same guarantees for the enumeration of proper tree decompositions. Observe that these algorithms imply polynomial-time procedures for computing top- $k$ minimal triangulations and/or proper tree decompositions. To the best of our knowledge, these are the first enumeration algorithms for minimal triangulations (and proper tree decompositions) with completeness, efficiency, and order guarantees.

Our ranked enumeration algorithm adapts the generic procedure of Lawler-Murty [30, 35]. For this deployment, we use a result by Parra and Scheffler [37] who show that a minimal triangulation is fully identified by its set of minimal separators. To adopt LawlerMurty, we rephrase the task as that of enumerating the relevant sets of minimal separators. In turn, using the technique of LawlerMurty we reduce this enumeration to the task of finding an optimal minimal triangulation, under the cost function, constrained on including a given set of minimal separators and excluding a given set of other minimal separators. Towards that, we show that these constraints can be compiled into any split-monotone cost function so that the resulting cost remains split monotone. Furthermore, if the original cost function can be computed in polynomial time, then so can the new cost function with the constraints compiled in.

Finally, we describe an implementation of our algorithm and an experimental study. We conduct experiments over the datasets of Carmeli et al. [10] that consist of three types of graphs: probabilistic graphical models (from the 2011 Probabilistic Inference Challenge), database queries (TPC-H), and random (Erdős-Rényi) graphs. We also conduct experiments on graphs from the PACE 2016 competition on tree-width computation. We compare our algorithm to the enumeration of Carmeli et al. [10] on both the execution time and the quality (width/fill) of the generated triangulations. In addition, we explore the validity of the poly-MS assumption on our datasets; that is, we provide statistics on the number of minimal separators, and explore the portion of the instances where this number is "manageable."

The remainder of the paper is organized as follows. We first present preliminary definitions and terminology in Section 2. In

Section 3, we describe the notion of split monotonicity. We give our main theoretical results in Section 4, and present the algoritms that realize the results Sections 5-6. Specifically, Section 5 presents our algorithm for computing a minimum-cost minimal triangulation, and Section 6 discusses the adaptation of Lawler-Murty to our enumeration. Finally, we describe our implementation and experimental study in Section 7, and conclude in Section 8. Due to space limitation, some proofs are in the Appendix.

## 2 PRELIMINARIES

We begin by introducing the basic notation, terminology and formal concepts that we use throughout the paper. For convenience, Table 1 contains important notation that we present here and later.

Graphs and Cliques. All the graphs in this paper are undirected. We denote by $\mathrm{V}(G)$ and $\mathrm{E}(G)$ the set of vertices and edges, respectively, of a graph $G$. An edge in $\mathrm{E}(G)$ is a pair $\{u, v\}$ of distinct vertices in $\mathrm{V}(G)$. The union of two graphs $G_{1}$ ad $G_{2}$, denoted $G_{1} \cup G_{2}$, is the graph $G$ with $\mathrm{V}(G)=\mathrm{V}\left(G_{1}\right) \cup \mathrm{V}\left(G_{2}\right)$ and $\mathrm{E}(G)=\mathrm{E}\left(G_{1}\right) \cup \mathrm{E}\left(G_{2}\right)$.

A set $C$ of vertices of a graph $G$ is a clique (of $G$ ) if every two vertices in $C$ are connected by an edge of $G$. The set $C$ is a maximal clique (of $G$ ) if $C$ is not strictly contained in any other clique of $G$. We note by $\operatorname{MaxClq}(G)$ the set of all maximal cliques of $G$.

Let $G$ be a graph, and $U$ a set of vertices of $G$. We denote by $\mathcal{K}_{U}$ is the complete graph over a vertex set $U$; that is, $\mathcal{K}_{U}$ is the graph with $\mathrm{V}\left(K_{U}\right)=U$ and $\mathrm{E}\left(\mathcal{K}_{U}\right)=\{\{u, v\} \subseteq U \mid u \neq v\}$ (hence, $U$ itself is a clique of $\mathcal{K}_{U}$ ). By saturating $U$ (in $G$ ) we refer to the operation connecting every non-adjacent vertices in $U$ by a new edge, thereby making $U$ a clique of $G$. In other words, saturating $U$ refers to the operation of replacing $G$ with $G \cup \mathcal{K}_{U}$.

A subgraph of a graph $G$ is a graph $G^{\prime}$ with $\mathrm{V}\left(G^{\prime}\right) \subseteq \mathrm{V}(G)$ and $\mathrm{E}\left(G^{\prime}\right) \subseteq \mathrm{E}(G)$. Let $U \subseteq \mathrm{~V}(G)$ be a set of vertices of $G$. We denote by $G[U]$ the subgraph of $G$ that is induced by $U$; that is, $G[U]$ is the graph $G^{\prime}$ with $\mathrm{V}\left(G^{\prime}\right)=U$ and $\mathrm{E}\left(G^{\prime}\right)=\{e \in \mathrm{E}(G) \mid e \subseteq U\}$. Let $G$ be a graph, and $U$ a set of vertices of $G$. We denote by $G \backslash U$ the graph obtained from $G$ by removing all vertices in $U$ (along with their incident edges); that is, $G \backslash U$ is the graph $G[\mathrm{~V}(G) \backslash U]$.

Tree decompositions. A tree decomposition $\mathcal{T}$ of a graph $G$ is a pair $(T, \beta)$, where $T$ is a tree and $\beta: \mathrm{V}(T) \rightarrow 2^{\mathrm{V}(G)}$ is a function that maps every node of $T$ to a set of vertices of $G$, so that all of the following hold.

- Vertices are covered: for every vertex $u$ of $G$ there is a vertex $v$ of $T$ such that $u \in \beta(v)$.
- Edges are covered: for every edge $e$ of $G$ there is a vertex $v$ of $T$ such that $e \subseteq \beta(v)$.
- The junction-tree property: for all vertices $u$ and $v$ of $T$, the intersection $\beta(u) \cap \beta(v)$ is contained in every vertex along the path between $u$ and $v$.
Let $G$ be a graph, and let $\mathcal{T}=(T, \beta)$ be a tree decomposition of $G$. A set $\beta(v)$, for $v \in \mathrm{~V}(T)$, is called a bag of $\mathcal{T}$. We denote by $\operatorname{bags}(\mathcal{T})$ the set $\{\beta(v) \mid v \in \mathrm{~V}(\mathcal{T})\}$.

Let $\mathcal{T}_{1}=\left(T_{1}, \beta_{1}\right)$ and $\mathcal{T}_{2}=\left(T_{2}, \beta_{2}\right)$ be two tree decompositions of a graph $G$. We say that $\mathcal{T}_{2}$ bag-contains $\mathcal{T}_{1}$ if there is an injection $\varphi: \mathrm{V}\left(T_{1}\right) \rightarrow \mathrm{V}\left(T_{2}\right)$ such that $\beta_{1}(v)=\beta_{2}(\varphi(v))$ for all $v \in \mathrm{~V}\left(T_{1}\right)$. We say that $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are bag equivalent if $\mathcal{T}_{2}$ bag-contains $\mathcal{T}_{1}$ and vice versa. We say that $\mathcal{T}_{1}$ strictly subsumes $\mathcal{T}_{2}$ if $\mathcal{T}_{1}$ is obtained
![img-0.jpeg](img-0.jpeg)

Figure 1: A graph $G$, tree decompositions of $G$ and minimal triangulations of $G$.
from $\mathcal{T}_{2}$ by splitting a bag or removing it altogether. More formally, $\mathcal{T}_{1}$ strictly subsumes $\mathcal{T}_{2}$ if there is a mapping $\varphi: \mathrm{V}\left(T_{1}\right) \rightarrow \mathrm{V}\left(T_{2}\right)$ such that $\beta_{1}(x) \subseteq \beta_{2}(\varphi(x))$ for all $x \in \mathrm{~V}\left(T_{1}\right)$, and for at least one $y \in \mathrm{~V}\left(T_{2}\right)$ it is the case that $\beta_{1}(x) \subseteq \beta_{2}(y)$ whenever $\varphi(x)=y$ (hence, either no vertex is mapped to $y$ or a vertex that is mapped to $y$ is a strict subset of $y$ ). A tree decomposition is proper if it is not strictly subsumed by any other tree decomposition [10].1

Example 2.1. Figure 1(c) depicts five tree decompositions of the graph $G$ of Figure 1(a). Each rectangle corresponds to a vertex $x$ of the tree, and the bag $\beta(x)$ is depicted inside the rectangle. For example, if we denote $\mathcal{T}_{1}=\left(T_{1}, \beta_{1}\right)$, then $T_{1}$ is a path of three vertices (corresponding to the three rectangles), and for the top vertex $x$ we have $\beta_{1}(x)=\left\{u, w_{1}, w_{2}, w_{3}\right\}$. Note that $\mathcal{T}_{2}$ and $\mathcal{T}_{2}^{\prime \prime}$ are bag equivalent, since they have the exact same bags (though connected differently). The tree decomposition $\mathcal{T}_{1}$ strictly subsumes $\mathcal{T}_{1}^{\prime}$, as the latter is obtained from the former by adding $w_{1}$ to the bottom bag. Moreover, $\mathcal{T}_{2}$ strictly subsumes $\mathcal{T}_{2}^{\prime}$, as the former is obtained from the latter by splitting the bottom bag into two-the middle and bottom vertices fo $\mathcal{T}_{2}$. Thus, $\mathcal{T}_{1}^{\prime}$ and $\mathcal{T}_{2}^{\prime}$ are not proper. We will later show that $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ (and, hence, $\mathcal{T}_{2}^{\prime \prime}$ ) are proper.

Minimal triangulations. Let $G$ be a graph. A cycle in $G$ is a path that starts and ends with the same vertex. A chord of a cycle $C$ is an edge $e \in \mathrm{E}(G)$ that connects two vertices that are non-adjacent in $C$. We say that $G$ is chordal if every cycle of length greater than three has a chord. Whether a given graph is chordal can be decided in linear time [39].

A triangulation of a graph $G$ is a chordal graph $H$ that is obtained from $G$ by adding edges. The fill set of a triangulation $H$ of $G$ is the set of edges added to $H$, that is, $\mathrm{E}(H) \backslash \mathrm{E}(G)$. A minimal triangulation of $G$ is a triangulation $H$ of $G$ such that the fill set of $H$ is not strictly contained in the fill set of any other triangulation; that is, there is no chordal graph $G^{\prime}$ with $\mathrm{V}(G)=\mathrm{V}\left(G^{\prime}\right)$ and $\mathrm{E}(G) \subseteq \mathrm{E}\left(G^{\prime}\right) \subseteq \mathrm{E}(H)$. In particular, if $G$ is already chordal then $G$ is the only minimal triangulation of itself.

[^0]
[^0]:    ${ }^{1}$ This is a simplified, yet equivalent definition to that of Carmeli et al. [10].

Table 1: Symbol table


Clique trees. Let $G$ be a graph. A clique tree of $G$ is a tree decomposition $\mathcal{T}=(T, \beta)$ of $G$ such that $\beta$ is bijection between $\mathrm{V}(T)$ and $\operatorname{MaxClq}(G)$. In other words, $\mathcal{T}$ is a clique tree of $G$ if $\operatorname{bags}(\mathcal{T})=\operatorname{MaxClq}(G)$ and no two bags are the same. The following is known, and recorded for later use.

Theorem 2.2. ( $[6,10,38])$ Let $G$ be a graph.
(1) $G$ is chordal if and only if $G$ has a clique tree [6].
(2) If $G$ is chordal, then $|\operatorname{MaxClq}(G)|<|\mathrm{V}(G)|$ [38].
(3) A tree decomposition $\mathcal{T}$ of $G$ is proper if and only if it is a clique tree of a minimal triangulation of $G[10]$.
Example 2.3. Continuing Example 2.1, observe that the graph $G$ of Figure 1(a) is not chordal. As one evidence, it has the chordless cycle $u-w_{1}-v-w_{2}-u$. Figure 1(b) depicts two minimal triangulations, $H_{1}$ and $H_{2}$, of the graph $G$ of Figure 1(a). The reader can verify that $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ of Figure 1(c) are clique trees of $H_{1}$ and $H_{2}$, respectively. In particular, we conclude that $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are proper tree decompositions.

Minimal separators. Let $u$ and $v$ be vertices of a graph $G$. A $(u, v)$ separator (w.r.t. $G$ ) is a set $S \subseteq \mathrm{~V}(G)$ such that $u$ and $v$ belong to different connected components in $G \backslash S$; that is, $G \backslash S$ does not contain any path between $u$ and $v$ (or equivalently, every path between $u$ and $v$ visits one or more vertices of $S$ ). We say that $S$ is a minimal $(u, v)$-separator if no proper subset of $S$ is a $(u, v)$ separator. We say that $S$ is a minimal separator of $G$ if there are vertices $u$ and $v$ such that $S$ is a minimal $(u, v)$-separator. We denote by $\operatorname{MinSep}(G)$ the set of all minimal separators of $G$. A graph may have exponentially many minimal separators.

Let $G$ be a graph, and let $S$ and $T$ be two minimal separators of $G$. We say that $S$ crosses $T$ if there are vertices $u$ and $v$ in $T$ such that $S$ is a $(u, v)$-separator. Crossing is known to be a symmetric relation: if $S$ crosses $T$ then $T$ crosses $S[27,37]$. Hence, if $S$ crosses $T$ then we may also say that $S$ and $T$ are crossing. When $S$ and $T$ are non-crossing, then we also say that $S$ and $T$ are parallel.

Example 2.4. We continue with our running example. The topleft graph of Figure 2 depicts three minimal separators $S_{1}, S_{2}$ and $S_{3}$ of the graph $G$ of Figure 1(a). For instance $S_{1}=\left\{w_{1}, w_{2}, w_{3}\right\}$ is a minimal $(u, v)$-separator, $S_{2}=\{u, v\}$ is a minimal $\left(w_{1}, w_{2}\right)$ separator, and $S_{3}=\{v\}$ is a minimal $\left(u, v^{\prime}\right)$-separator. Note that $S_{2}$ is a $\left(w_{1}, v^{\prime}\right)$-separator but not a minimal $\left(w_{1}, v^{\prime}\right)$-separator, since a strict subset of $S_{2}$, namely $S_{3}$, is a $\left(w_{1}, v^{\prime}\right)$-separator. Also note that
$S_{1}$ and $S_{2}$ are crossing, since $S_{1}$ is a $(u, v)$-separator (and also $S_{2}$ is a ( $w_{1}, w_{2}$ )-separator). It can be verified that $S_{1}, S_{2}$ and $S_{3}$ are the only minimal separators of $G$. Hence $\operatorname{MinSep}(G)=\left\{S_{1}, S_{2}, S_{3}\right\}$. This example illustrates that, albeit being "minimal," a minimal separator can be a strict subset of another; for instance $S_{3} \subseteq S_{2}$.

A set of pairwise-parallel minimal separators is a set $M$ of minimal separators such that every two distinct members of $M$ are parallel. Moreover, such $M$ is said to be maximal if every minimal separator not in $M$ is crossing at least one member of $M$. Parra and Scheffler [37] established the following connection between minimal triangulations and maximal sets of pairwise-parallel minimal separators.

Theorem 2.5. (Parra and Scheffler [37]) Let $G$ be a graph.
(1) Let $M$ be a maximal set of pairwise-parallel minimal separators of $G$, and let $H$ be obtained from $G$ by saturating each member of $M$. Then $H$ is a minimal triangulation of $G$ having $\operatorname{MinSep}(H)=M$.
(2) Conversely, if $H$ is a minimal triangulation of $G$, then $M=$ $\operatorname{MinSep}(H)$ is a maximal set of pairwise-parallel minimal separators in $G$, and $H$ is obtained from $G$ by saturating each member of $M$.

Ranked enumeration. An enumeration problem P is a collection of pairs $(x, Y)$ where $x$ is an input and $Y$ is a finite set of answers for $x$, denoted by $\mathrm{P}(x)$. A solver for an enumeration problem P is an algorithm that, when given an input $x$, produces (or prints) a sequence of answers such that every answer in $\mathrm{P}(x)$ is printed precisely once. A solver for an enumeration problem is also called an enumeration algorithm. We recall several standard yardsticks of efficiency for enumeration algorithms [23]. Let P be an enumeration problem, and let $A$ be solver for P . We say that $A$ runs in (a) polynomial total time if the total execution time of $A$ is polynomial in $(|x|+|\mathrm{P}(x)|)$; (b) polynomial delay if the time between printing every two consecutive answers is polynomial in $|x|$; and (c) incremental polynomial time if, after printing a sequence $Y$ of answers, the time to print the next answer is polynomial in $(|x|+|Y|)$ where $Y$ is the size of the representation of $Y$. Observe that a solver that enumerates with polynomial delay also enumerates with incremental polynomial time, which, in turn, implies polynomial total time.

Let P be an enumeration problem. A cost function for P is a function $c$ that associates a numerical cost $c(x, y)$ to each input $x$ and answer $y$ for $x$. A solver $A$ for $P$ is said to enumerate by increasing $c$, where $c$ is cost function for P , if for every two answers $a_{1}$ and $a_{2}$ produced by $A$, if $a_{1}$ is produced before $a_{2}$ then $c\left(a_{1}\right) \leq c\left(a_{2}\right)$.

## 3 MONOTONE COST FUNCTIONS

By a cost function over tree decompositions we refer to a function $\kappa$ that maps a graph $G$ and a tree decomposition $\mathcal{T}$ for $G$ to a numerical (positive, negative or zero) value $\kappa(G, \mathcal{T})$. In this section we define a class of such cost functions that includes many of the common costs such as width and fill. This class is defined by means of monotonicity, as we formally defined next.

Let $G$ be a graph, and let $\mathcal{T}=(T, \beta)$ be a tree decomposition of $G$. Every edge $e=\left\{v_{1}, v_{2}\right\}$ of $T$ connects two unique subtrees of $T$-one connected to $v_{1}$ and one connected to $v_{2}$. Let $e$ be an edge of $T$, let $T_{1}$ and $T_{2}$ be the two subtrees connected by $e$, and let $\beta_{1}$

and $\beta_{2}$ be the restrictions of $\beta$ to $\mathrm{V}\left(T_{1}\right)$ and $\mathrm{V}\left(T_{2}\right)$, respectively. Let $\mathcal{T}_{1}=\left(T_{1}, \beta_{1}\right)$ and $\mathcal{T}_{2}=\left(T_{2}, \beta_{2}\right)$, and let $G_{1}$ and $G_{2}$ be the subgraphs of $G$ induced by the nodes in the bags of $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$, respectively. Then we say that $\mathcal{T}$ splits (by e) as $\left\langle G_{1}, \mathcal{T}_{1}, G_{2}, \mathcal{T}_{2}\right\rangle$. The following proposition is straightforward.

Proposition 3.1. Let $G$ be a graph and $\mathcal{T}=(T, \beta)$ a tree decomposition of $G$. If $\mathcal{T}$ splits as $\left\langle G_{1}, \mathcal{T}_{1}, G_{2}, \mathcal{T}_{2}\right\rangle$, then $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are tree decompositions of $G_{1}$ and $G_{2}$, respectively.

Proposition 3.1 implies that if $\kappa$ is a cost function and $\mathcal{T}$ splits as $\left\langle G_{1}, \mathcal{T}_{1}, G_{2}, \mathcal{T}_{2}\right\rangle$, then both $\kappa\left(G_{1}, \mathcal{T}_{1}\right)$ and $\kappa\left(G_{2}, \mathcal{T}_{2}\right)$ are defined. We can now define properties of cost functions.

Definition 3.2. Let $\kappa$ be a cost function over tree decompositions. We say that $\kappa$ is:
(1) invariant under bag equivalence, if for all graphs $G$ and tree decompositions $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ of $G$, if $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are bag equivalent then $\kappa\left(\mathcal{T}_{1}\right)=\kappa\left(\mathcal{T}_{2}\right)$.
(2) split monotone if for all graphs $G$ and tree decompositions $\mathcal{T}$ and $\mathcal{T}^{\prime}$ of $G$, if $\mathcal{T}$ and $\mathcal{T}^{\prime}$ split as $\left\langle G_{1}, \mathcal{T}_{1}, G_{2}, \mathcal{T}_{2}\right\rangle$ and $\left\langle G_{1}, \mathcal{T}_{1}^{\prime}, G_{2}, \mathcal{T}_{2}^{\prime}\right\rangle$, respectively, and $\kappa\left(G_{i}, \mathcal{T}_{i}\right) \leq \kappa\left(G_{i}, \mathcal{T}_{i}^{\prime}\right)$ for $i=1,2$, then $\kappa(G, \mathcal{T}) \leq \kappa\left(G, \mathcal{T}^{\prime}\right)$.

If $\kappa$ is invariant under bag equivalence, then it is essentially a scoring function over the collection of bags, and in that case we say that $\kappa$ is a bag cost.

For illustration, the following most popular cost functions $\kappa(G, \mathcal{T})$ are both split-monotone bag costs.

- $\operatorname{width}(G, \mathcal{T})$ : the maximal bag cardinality minus one.
- fill-in $(G, \mathcal{T})$ : the number of edges required to be added for saturating all bags.
Other such cost functions are the generalizations of width and fillin introduced by Furuse and Yamazaki [15], where it is assumed that each bag $b$ has a cost $c(b)$, and each edge $e$ has a cost $c(e)$. Then, they define width ${ }_{e}(G, \mathcal{T})$ to be the maximal score of a bag, and fill-in ${ }_{e}(G, \mathcal{T})$ to be the sum of costs of the edges required to saturate all bags. As a special case, if the graph $G$ is the primal graph of a hypergraph, then $c(b)$ can be the minimal number of hyperedges needed to cover $b$, or the minimal weight of a fractional edge cover of $b$, thereby establishing the popular cost functions of hypertree width [19] and fractional hypertree width [22].

Finally, another intuitive split-monotone bag costs is

$$
\kappa(G, \mathcal{T})=|\mathrm{E}(G)|^{\text {width }(G, \mathcal{T})}+\text { fill-in }(G, \mathcal{T})
$$

that effectively establishes the lexicographic ordering of the width followed by the fill-in of $G$.

We can then use a bag cost $\kappa$ as a cost function over triangulations $H$, by defining the cost as $\kappa(\mathcal{T})$ where $\mathcal{T}$ is any clique tree of $H$. Since $\kappa$ is invariant under bag equivalence (being a bag cost), then the choice of $\mathcal{T}$ does not matter. By a slight abuse of notation, we use $\kappa(G, H)$ to denote the resulting cost over triangulations $H$ of $G$.

## 4 MAIN THEORETICAL RESULTS

In this section we present our main theoretical results. These results are upper bounds (existence of algorithms) on problems of ranked enumeration of tree decompositions and minimal triangulations. In the next two sections we will describe the algorithms.

The poly-MS assumption. Recall that a graph may have an exponential number of minimal separators. Our main result holds for the case where this number is reasonable, a case that was deeply investigated in past research [9, 15, 31, 34]. Formally, we consider classes $\mathbf{G}$ of graph such that for some polynomial $p$ it is the case that $|\operatorname{MinSept}(G)| \leq p(|\mathrm{V}(G)|)$ for all $G \in \mathbf{G}$. We then say shortly that $\mathbf{G}$ is a poly-MS class of graphs (where "MS" stands for Minimal Separators). Later in this paper we empirically study the applicability of this assumption on real and synthetic datasets.

State of the art. Before presenting our results, we recall some relevant results from the literature. Carmeli et al. [10] showed that, without making any assumption, one can enumerate in incremental polynomial time the set of all proper tree decompositions and the set of all minimal triangulations. Note, however, that no guarantee is made on the order of enumeration.

Theorem 4.1. ([10]) Given a graph $G$, one can enumerate in incremental polynomial time all proper tree decompositions, and all minimal triangulations.

Parra and Scheffler [37] showed that minimal triangulations are in one-to-one correspondence with the maximal independent sets of the graph that has the minimal separators as vertices, and an edge between every two crossing separators. Combining that with results on the enumeration of maximal independent sets [11, 23], we get that that for poly-MS classes of graphs, the minimal triangulations can be enumerated with polynomial delay (again with no guarantees on the order). Moreover, Carmeli et al. [10] show that such enumeration automatically translates into an algorithm for enumerating the proper tree decompositions with polynomial delay. Hence, we get the following.

Theorem 4.2. (see [10]) If $\mathbf{G}$ is a poly-MS class of graphs, then one can enumerate with polynomial delay all proper tree decompositions, and all minimal triangulations.

Bouchitté and Todinca showed that on poly-MS classes of graphs, a tree decomposition (or triangulation) of a minimal width or fill-in can be found in polynomial time.

Theorem 4.3. ([9]) Let G be a poly-MS class of graphs. One can find in polynomial time a minimal-cost tree decomposition (or triangulation) when the cost is either the width or the fill in.

Furuse and Yamazaki [15] generalized the above result to the cost functions width ${ }_{c}$ and fill-in ${ }_{c}$ as defined in Section 3.

Main Results. We now turn to our results. The main result generalizes Theorems 4.2 and 4.3 in two directions. First, the enumeration is ranked. Second, the cost function is not just width of fill-in, but in fact every bag cost that is split monotone and computable in polynomial time.

Theorem 4.4. Let G be a poly-MS class of graphs, and let $\kappa$ be a bag cost that is split monotone and computable in polynomial time. On graphs of $\mathbf{G}$ one can enumerate with polynomial delay all:
(1) proper tree decompositions $\mathcal{T}$ by increasing $\kappa(G, \mathcal{T})$;
(2) minimal triangulations $H$ by increasing $\kappa(G, H)$.

Finally, the next result applies to general graphs, and assumes that we are interested only in tree decompositions of a bounded

![img-1.jpeg](img-1.jpeg)

Figure 2: Minimal separators and realizations of blocks of the graph $G$ of Figure 1(a).
width. In this case, we get a ranked enumeration with polynomial delay without assuming an upper bound on the number of minimal separators.

Theorem 4.5. Let $b$ be a fixed natural number, and let $\kappa$ be a bag cost that is split monotone and computable in polynomial time. Given a graph, one can enumerate with polynomial delay all:
(1) proper tree decompositions $\mathcal{T}$ of width at most $b$ by increasing $\kappa(G, \mathcal{T})$
(2) minimal triangulations $H$ of width at most $b$ by increasing $\kappa(G, H)$.

As said previously, in the next sections we prove Theorems 4.4 and 4.5 by presenting the corresponding algorithms and proving their correctness.

## 5 COMPUTING AN OPTIMAL MINIMAL TRIANGULATION

We now present an algorithm for computing a minimum-cost minimal triangulation, assuming that the cost function is a splitmonotone bag cost. Our algorithm terminates in polynomial time if the cost function can be evaluated in polynomial time, and moreover, the input graphs belong to a poly-MS class of graphs. Our algorithm generalizes an algorithm by Bouchitté and Todinca [8] for computing the minimal width (tree-width) and minimum fillin over a poly-MS class of graphs. Furthermore, we will consider restriction to triangulations of a bounded width.

### 5.1 Definitions and Notation

We first recall some concepts from the literature that our triangulation algorithm builds upon. For convenience, some of the notation is shown in Table 1.

Components and Blocks. Let $G$ be a graph, and $U$ a set of vertices of $\overline{G . \text { A } U \text {-component (of } G)}$ is a connected component of the graph
$G \backslash U$. Recall that a connected component is a subset $W$ of $\mathrm{V}(G)$ such that $G$ contains a path from each vertex of $W$ to every other vertex of $W$, and to none of the vertices outside $W$.

Let $S$ be a minimal separator of $G$. An $S$-component $C$ is full if every vertex in $S$ is connected to one or more vertices in $C$. A block (of $G$ ) is a pair $(S, C)$ where $S$ is a minimal separator and $C$ is an $S$-component. By a slight abuse of notation, we often identify the block $(S, C)$ with the vertex set $S \cup C$. A block $(S, C)$ is full if $C$ is a full component. The realization of the block $(S, C)$, denoted $\mathcal{R}_{G}(S, C)$, is the induced graph of $(S, C)$ after saturating $S$; that is:

$$
\mathcal{R}_{G}(S, C) \stackrel{\text { def }}{=} G[S \cup C] \cup \mathcal{K}_{S}
$$

When $G$ is clear from the context, we may remove it from the subscripts and write simply $\mathcal{R}(S, C)$.

Example 5.1. Recall from Example 2.4 that for the graph $G$ of our running example (Figure 1(a)) we have $\operatorname{MinSep}(G)=\left\{S_{1}, S_{2}, S_{3}\right\}$, where the $S_{i}$ are depicted in Figure 2 on the top left. The rest of Figure 2 shows the different realizations $\mathcal{R}\left(S_{i}, C_{i}^{f}\right)$ of the blocks of $G$. A rectangle marks the vertices of the minimal separator of the block, and the edges that have been added in the saturation are colored red. Note that all of the blocks are full, except for $\left(S_{2}, C_{2}^{4}\right)$ where no vertex of $C_{2}^{4}$ is connected to $u$.

Potential Maximal Cliques. Let $G$ be a graph. A vertex set $\Omega \subseteq$ $\mathrm{V}(\overline{G)}$ is a Potential Maximal Clique (PMC for short) if there is a minimal triangulation $H$ of $G$ such that $\Omega$ is a maximal clique of $H$. Due to Theorem 2.2 we conclude that a vertex set $\Omega$ is a PMC if and only if it is a bag of some proper tree decomposition of $G$. We denote by $P M C(G)$ the set of PMCs of $G$.

For $\Omega \in P M C(G)$, let $C$ be any $\Omega$-component. Let $S$ be the set of all vertices in $\Omega$ that are neighbors of vertices in $C$. It is known that $S$ is a minimal separator of $G$ and $(S, C)$ is a full block of $G$ [8], and they are said to be associated to $\Omega$ (in $G$ ). No other minimal separator of $G$ is contained in $\Omega$. We denote by $\operatorname{MinSep}_{G}(\Omega)$ and $B l c k_{G}(\Omega)$ the sets of minimal separators and blocks, respectively, associated to $\Omega$. When $G$ is clear from the context, we may omit it and write simply $\operatorname{MinSep}(\Omega)$ and $\operatorname{Blck}(\Omega)$.

Example 5.2. The PMCs of the graph $G$ of Figure 1(a) are the vertex sets in all of the bags of the proper tree decompositions in Figure 1(c). For example, $P M C(G)$ contains the sets $\left\{u_{1}, w_{1}, w_{2}, w_{3}\right\}$ and $\left\{w_{1}, u, v\right\}$. Let $\Omega$ be $\left\{w_{1}, u, v\right\}$. The minimal separators in $\operatorname{MinSep}(\Omega)$ are $S_{2}$ and $S_{3}$ of Figure 2, and the blocks in Blck( $\Omega$ ) are $\left(S_{2}, C_{2}^{2}\right)$, $\left(S_{2}, C_{2}^{3}\right),\left(S_{3}, C_{3}^{2}\right)$, all depicted in Figure 2.

### 5.2 Algorithm Description

To describe the algorithm, we first give some background. The Bouchitté-Todinca algorithm [8] is based on the observation that a minimal triangulation of a graph is composed of minimal triangulations over realizations of its blocks. This is formalized in the following theorem:

Theorem 5.3. (Bouchitté and Todinca [8]) The following hold for a graph $G$.
(1) If $H$ is a minimal triangulation, $\Omega \in \operatorname{MaxClq}(H)$, and $\left(S_{i}, C_{i}\right) \in$ Blck $_{G}(\Omega)$, then $H_{i}=H\left[S_{i} \cup C_{i}\right]$ is a minimal triangulation of the realization $\mathcal{R}_{G}\left(S_{i}, C_{i}\right)$.

```
Algorithm MinTriang \((\kappa\rangle(G)\)
1: Compute \(\operatorname{MinSep}(G)\) and \(\operatorname{PMC}(G)\)
2: \(\mathcal{B}:=\) the set of full blocks of \(G\)
3: for \((S, C) \in \mathcal{B}\) by increasing cardinality do
4: \(\quad \Omega(S, C):=\operatorname{argmin} \kappa(G[(S, C)], H_{\mathcal{R}(S, C)}(\Omega))\)
5: \(\mathcal{H}(S, C):=H_{\mathcal{R}(S, C)}(\Omega(S, C))\)
6: \(\Omega(G):=\operatorname{argmin}_{G \in P M C(G)} \kappa\left(G, H_{G}(\Omega)\right)\)
7: \(\operatorname{return}\left(H_{G}(\Omega(G))\right)\)
```

Figure 3: Computing an optimal minimal triangulation for a split-monotone bag cost.
(2) Conversely, let $\Omega \in P M C(G)$ and $k=\left|B l c k_{G}(\Omega)\right|$. For $\left(S_{i}, C_{i}\right) \in$ Blck $_{G}(\Omega)$ let $H_{i}$ be a minimal triangulation of $\mathcal{R}_{G}\left(S_{i}, C_{i}\right)$. Then $H=\bigcup_{i=1}^{k} H_{i} \cup \mathcal{K}_{\Omega}$ is a minimal triangulation of $G$.
Observe that $\Omega \in \operatorname{MaxClq}(H)$ implies that $\Omega$ is a PMC. Theorem 5.3 provides a characterization of the minimal triangulations in terms of the minimal triangulations of the block realizations. Then, how do we proceed to computing the minimal triangulations of the block realizations? This is shown in the following result.

Theorem 5.4. (Bouchitté and Todinca [8]) Let $G$ be a graph, $S \in$ MinSep $(G)$, and $(S, C)$ a full block of $G$. Let $G^{\prime}=\mathcal{R}_{G}(S, C)$. Let $H$ be a graph with $\mathrm{V}(H)=\mathrm{V}\left(G^{\prime}\right)$ and $\mathrm{E}(H) \supseteq \mathrm{E}\left(G^{\prime}\right)$. The following are equivalent.
(1) $H$ is a minimal triangulation of $G^{\prime}$.
(2) There exists $\Omega \in P M C(G)$ such that $S \subset \Omega \subseteq \mathrm{~V}\left(G^{\prime}\right)$ and $H=$ $\bigcup_{i=1}^{k} H_{i} \cup \mathcal{K}_{\Omega}$, where $\left|B l c k_{G^{\prime}}(\Omega)\right|=k$ and $H_{i}$ is a minimal triangulation of $\mathcal{R}_{G^{\prime}}\left(S_{i}, C_{i}\right)$ for all $\left(S_{i}, C_{i}\right) \in B l c k_{G^{\prime}}(\Omega)$.
For Part 2 of Theorem 5.4, it is important to note that the blocks of $\Omega$ in $G^{\prime}$ are also full blocks of $G[8]$.

Now, consider an input $G$ for our algorithm and $\Omega \in P M C(G)$. We will assume that for each $\left(S_{i}, C_{i}\right) \in B l c k_{G}(\Omega)$ our algorithm has computed a minimal triangulation $H_{i}$ for the realization $\mathcal{R}_{G}\left(S_{i}, C_{i}\right)$. We then define the following,

$$
H_{G}(\Omega) \stackrel{\text { def }}{=} \bigcup_{\left(S_{i}, C_{i}\right) \in B l c k_{G}(\Omega)} H_{i} \cup \mathcal{K}_{\Omega}
$$

Our algorithm, MinTriang, is depicted in Figure 3. It applies dynamic programming based on Equation (1). The algorithm is parameterized by a split-monotone bag cost $\kappa$, takes as input a graph $G$, and computes a minimum- $\kappa$ minimal triangulation of $G$.

The first step is to compute MinSep $(G)$ and $\operatorname{PMC}(G)$. Assuming $G$ belongs to a poly-MS class of graphs, this step can be done efficiently by combining results from Berry et al. [3] and Bouchitté and Todinca [9]. Then, the set $\mathcal{B}$ of full blocks of $G$ is computed and traversed in order of ascending cardinality (beginning with $(S, C)$ such that $|S \cup C|$ is minimal) in the loop of line 3. In the iteration of $(S, C)$, the optimal triangulation of $\mathcal{R}(S, C)$ is computed.

When processing a block $(S, C)$, the algorithm selects a PMC $\Omega \in P M C(G)$ where $S \subset \Omega \subseteq S \cup C$, to be saturated according to

Equation (1), such that the cost of the resulting triangulation of $\mathcal{R}(S, C)$ is minimized. The saturated vertex set is stored as $\Omega(S, C)$ (line 4). By a slight abuse of notation, we denote by $\operatorname{PMC}(S, C)$ the set $\left\{\Omega \in P M C(G) \mid S \subset \Omega \subseteq(S, C)\right\}$. The chosen optimal triangulation of $\mathcal{R}(S, C)$ is then stored as $\mathcal{H}(S, C)$ for later use (line 5). The processing order of the blocks allows larger blocks to evaluate each member of $\operatorname{PMC}(S, C)$ based on previously computed optimal triangulation for each of the realizations of its smaller blocks. That is, for each block $\left(S_{i}, C_{i}\right) \in B l c k_{\mathcal{R}(S, C)}(\Omega)$, the term $H_{i}$ in Equation (1) (used in lines 4 and 5) will refer to previously computed $\mathcal{H}\left(S_{i}, C_{i}\right)$.

Finally, the optimal result is selected by saturating the minimalcost PMC in the whole graph (lines 6-7). The following theorem states the correctness and efficiency of the algorithm.

Theorem 5.5. Let $\kappa$ be a split-monotone bag cost computable in polynomial time. MinTriang $(\kappa\rangle(G)$ returns an minimal triangulation of minimal cost $\kappa$ in time polynomial in the number of minimal separators of the graph. Hence, if $G$ belongs to a poly-MS class of graphs then MinTriang terminates in polynomial time.

### 5.3 Bounded Width

Another application of the algorithm is when we are interested only in tree decompositions of a bounded (constant) width $b$, without making the poly-MS assumption. Bounding the width can be accomplished by attaching a high cost ( $\infty$ ) to triangulations with maximal cliques of a larger size than $b$ (lines 4 and 6). Furthermore, any minimal separator larger than $b$ can not be saturated in our output, implying full blocks of these separators can be completely disregarded in the main loop (line 3). The limit on the width bounds the number of minimal separators and PMCs our algorithm should consider. Hence, if this limit is considered constant then we get a polynomial bound on the execution time of our algorithm, without assuming poly-MS, if we revise line 1 to compute only the minimal separators and PMCs of size at most $b$. We refer to the revised algorithm as MinTriangB $(b, \kappa\rangle(G)$. We have the following.
Theorem 5.6. Let $b$ be a fixed natural number, and $\kappa$ a split monotone bag cost computable in polynomial time. MinTriangB $(b, \kappa\rangle(G)$ returns, in polynomial time, a minimal triangulation $H$ of width at most $b$ (if one exists) with a minimal $\kappa(G, H)$.

## 6 ENUMERATION ALGORITHM

We now present our algorithm for ranked enumeration of minimal triangulations. A strong connection between minimal triangulations and proper tree decompositions is stated in Theorem 2.2. Carmeli et al. [10] show how enumeration of proper tree decompositions reduces to that of minimal triangulations. Formally, we have the following.

Proposition 6.1. Let G be class of graphs, and $\kappa$ a bag cost. If, on graphs of G, the minimal triangulations can be enumerated with polynomial delay by increasing $\kappa$, then so can the proper tree decompositions.

So, in the remainder of this section we consider only minimal triangulations. Our algorithm is an application of Lawler-Murty's procedure [30, 35], which reduces ranked enumeration to optimization under inclusion and exclusion constraints. The goal of this procedure is to enumerate sets $A$ of items $a$ by an increasing cost

function $c(A)$. Here, an item $a$ is a minimal separator of $G$ and each set $A$ is a maximal set of pairwise-parallel minimal separators. Recall from Theorem 2.5 that each such set $A$ identifies a minimal triangulation $H$. In particular, the score $c(A)$ is $\kappa(G, H)$. A constraint of both types is represented as a minimal separator $S$. A minimal triangulation $H$ satisfies sets $I$ and $X$ of inclusion and exclusion constraints, respectively, if $I \subseteq \operatorname{MinSep}(H)$ and $X \cap \operatorname{MinSep}(H)=\emptyset$. We denote such a pair as $[I, X]$, and say that $H$ satisfies $[I, X]$ if it satisfies both $I$ and $X$.

In the rest of this section we will show how MinTriang can be adapted to return a minimal triangulation satisfying input constraints, and present our algorithm for ranked enumeration. Later, we adapt the algorithm to enumerate the minimal triangulations of a bounded width.

### 6.1 Incorporating Constraints

We would like to restrict MinTriang (Figure 3) to return a minimal triangulation that satisfies a set $[I, X]$ of inclusion and exclusion constraints. Our approach is to alter our cost function $\kappa$ to assign an infinite cost to triangulations that violate the constraints. Yet, while doing so we need to verify that all needed assumptions hold.

To check constraints during the MinTriang algorithm we need to take into consideration two problems that may occure while triangulating a realization $\mathcal{R}(S, C)$ of $G$. First, $I$ may include vertices that are not in $\mathcal{R}(S, C)$, so $I$ will be violated for the wrong reasons. Second, it might be the case that a minimal separator $S$ of $G$ is not a minimal separator of $\mathcal{R}(S, C)$, but it will be a minimal separator in a triangulation that contains this triangulation. Therefore, we use the following equivalent definition (see Theorem 2.5). We say that $H$ satisfies $[I, X]$, in notation $H \models[I, X]$, if for all $S \in I \cup X$ with $S \subseteq \mathrm{~V}(H)$ it holds that $S$ is a clique of $H$ if $S \in I$ and $S$ is not a clique of $H$ if $S \in X$.

Given a constraint $[I, X]$ and a split-monotone bag cost $\kappa$ (over tree decompositions), we define the cost function $\kappa[I, X]$ as follows.

$$
\kappa[I, X](G, \mathcal{T}) \stackrel{\text { def }}{=} \begin{cases}\kappa(G, \mathcal{T}) & \text { if } H_{\mathcal{T}} \models[I, X] \\ \infty & \text { otherwise }\end{cases}
$$

where, $H_{\mathcal{T}}$ is the graph obtained from $G$ by saturating every bag of $\mathcal{T}$. A crucial lemma is the following, stating that if $\kappa$ is a splitmonotone bag cost, then so is $\kappa[I, X]$.

Lemma 6.2. Let $\kappa$ be a cost function, $G$ a graph, and $[I, X]$ a set of constraints on minimal triangulations of $G$.
(1) If $\kappa$ is a split-monotone bag cost, then so is $\kappa[I, X]$.
(2) If $\kappa$ can be computed in polynomial time in the size of $G$, then $\kappa[I, X]$ can be computed in polynomial time in the size of $G, I$ and $X$.

Combining Lemma 6.2 with Theorem 5.5, we conclude the following theorem that we will use in the next section.

Theorem 6.3. Let G be a poly-MS class of graphs and $\kappa$ a splitmonotone bag cost computable in polynomial time over G. For all $G \in \mathbf{G}$ and constraints $[I, X]$ over $G$, MinTriang $\langle\kappa[I, X]\rangle(G)$ returns a minimum $\kappa[I, X]$ minimal triangulation in polynomial time.

### 6.2 The Enumeration Algorithm

Our enumeration algorithm, RankedTriang, is depicted in Figure 4. It is parameterized by a cost function $\kappa$, takes as input a graph $G$, and enumerates (via the print command of line 6) the minimal triangulations of $G$ by increasing cost.

The algorithm maintains a priority queue $\mathcal{Q}$. Each element in $\mathcal{Q}$ represents a partition of the space of minimal triangulations. Here, a partition is associated with an inclusion-exclusion constraint $[I, X]$, and it consists of all minimal triangulations that satisfy $[I, X]$. In $\mathcal{Q}$, the partition $[I, X]$ is represented as a triple $\langle H, I, X\rangle$, where $H$ is a minimum-cost member (minimal triangulation) in the partition. Whenever we reach the loop of line $4, \mathcal{Q}$ forms a partition of the entire space of minimal triangulations that have not been printed yet. In particular, the first element inserted into $\mathcal{Q}$ (in line 3) is the triple $\langle H, \emptyset, \emptyset\rangle$, representing the entire space of minimal triangulations, where $H$ is a minimal triangulation of a minimum $\kappa$.

Priority in $\mathcal{Q}$ is determined by the cost of the minimal triangulation. In particular, the element removed in line 5 is triple $\langle H, I, X\rangle$ such that $\kappa(H) \leq \kappa\left(H^{\prime}\right)$ for all triple $\left\langle H^{\prime}, I^{\prime}, X^{\prime}\right\rangle$ in $\mathcal{Q}$. In each iteration of the while loop, such $\langle H, I, X\rangle$ is removed and printed. Then, in the rest of the iteration (lines 7-13), the remainder of the partition $[I, X]$ (that is, every minimal triangulation there except fot $H$ ) is split into new partitions, all inserted to $Q$ (line 13). The new partitions are constructed as follows. Recall that $H$ contains all of the minimal separators in $I$. Let $S_{1}, \ldots, S_{k}$ be the set of minimal separators of $H$ that are not in $I$. The first partition, $\left[I_{1}, X_{1}\right]$, is obtained from $[I, X]$ by copying $I$ and inserting $S_{1}$ into $X_{1}$. In the second partition we add $S_{1}$ to $I$, but now $X_{2}$ is $X \cup\left\{S_{2}\right\}$. We likewise continue for $i=2, \ldots i-1$, where each $I_{i}$ consists of $I$ and $S_{1}, \ldots, S_{i-1}$, and each $X_{i}$ is $X \cup\left\{S_{i}\right\}$. It is an easy observation that the $\left[I_{i}, X_{i}\right]$ form a proper partition. In particular, observe that no other minimal triangulation can contain all of the minimal separators of $H$, since no two triangulations $H$ and $H^{\prime}$ satisfy $\operatorname{MinSep}(H) \subseteq \operatorname{MinSep}\left(H^{\prime}\right)$, as implied by Theorem 2.5. For each partition $\left[I_{i}, X_{i}\right]$ a minimum-cost minimal

```
Algorithm RankedTriang \(\langle\kappa\rangle(G)\)
\(Q:=\) empty priority queue by \(\kappa\) (lowest first)
\(H:=\operatorname{MinTriang}\langle\kappa\rangle(G)\)
\(\mathcal{Q} \cdot \operatorname{push}(\langle H, \emptyset, \emptyset\rangle)\)
while \(Q \neq \emptyset\) do
    \(\langle H, I, X\rangle:=\mathcal{Q} \cdot \operatorname{pop}()\)
    print( \(H\) )
    let \(\operatorname{MinSep}(H) \backslash I\) be \(\left\{S_{1}, \ldots, S_{k}\right\}\)
    for \(i=1, \ldots, k-1\) do
        \(I_{i}:=I \cup\left\{S_{1}, \ldots, S_{i-1}\right\}\)
        \(X_{i}:=X \cup\left\{S_{i}\right\}\)
        \(H_{i}:=\operatorname{MinTriang}\left\langle\kappa\left[I_{i}, X_{i}\right]\right\rangle(G)\)
        if \(H_{i}\) satisfies \(\left[I_{i}, X_{i}\right]\) then
            \(\mathcal{Q} \cdot \operatorname{push}\left(\left\langle H_{i}, I_{i}, X_{i}\right\rangle\right)\)
```

Figure 4: Ranked enumeration of the minimal triangulations by a split-monotone bag cost $\kappa$.

triangulation $H_{I}$ w.r.t. $\kappa\left[I_{I}, X_{I}\right]$ is constructed (line 11). Observe that $H_{I}$ satisfies $\left[I_{I}, X_{I}\right]$ if and only if this partition is nonempty; hence, the test of line 12 tests whether the partition is nonempty, and if so inserts $\left\langle H_{I}, I_{I}, X_{I}\right\rangle$ to $Q$.

The correctness and efficiency of the algorithm are stated in the following theorem.

Theorem 6.4. RankedTriang $(\kappa\rangle(G)$ enumerates the minimal triangulations $H$ of $G$ by increasing $\kappa(G, H)$. Moreover, the algorithm enumerates with polynomial delay if:
(1) $\kappa$ can be computed in polynomial time, and
(2) each MinTriang $\left(\kappa\left[I_{I}, X_{I}\right]\right)(G)$ takes polynomial time.

Combined with Theorem 6.3, we conclude the following.
Corollary 6.5. Let G be a poly-MS class of graphs, and let $\kappa$ be a bag cost that is split monotone and computable in polynomial time. On graphs $G$ of G, RankedTriang $(\kappa\rangle(G)$ can enumerate the minimal triangulations of $G$ by increasing $\kappa$, with polynomial delay.

Note that Theorem 4.4 (from Section 4) is a direct consequence of Corollary 6.5.

Bounded width. We now consider the enumeration of the minimal triangulations of a width bounded by a fixed bound $b$, without masking the assumption of poly-MS, as stated in Theorem 4.5. To adjust RankedTriang $(\kappa\rangle(G)$ to this case, it suffices to replace MinTriang $(\kappa\rangle(G)$ and MinTriang $\left(\kappa\left[I_{I}, X_{I}\right]\right\rangle(G)$, in lines 2 and 11, with MinTriangB $(b, \kappa\rangle(G)$ and MinTriangB $\left.\left(b, \kappa\left[I_{I}, X_{I}\right]\right\rangle(G)\right.$, respectively, building on Theorem 5.6 instead of Theorem 5.5. (The algorithm MinTriangB is described right before Theorem 5.6.) We can show that all guarantees of the enumeration algorithm (as stated in Theorem 6.4) remain valid. Combined with Lemma 6.2 and Proposition 6.1, we then establish Theorem 4.5 (from Section 4).

## 7 EXPERIMENTAL EVALUATION

In this section, we describe our experimental study, where the goal is twofold. First and foremost, we explore the performance of our enumeration algorithm (Figures 3 and 4), namely RankedTriang. The second goal is to explore the applicability of the poly-MS assumption in reality, and particularly to get an insight on how often realistic graphs have a manageable number of minimal separators.

### 7.1 Experimental Setup

We first describe the general setup for the experiments.
Implementation. The algorithms have been implemeted in C++, with STL data structures. We used some of the code of Carmeli et al. [10]. ${ }^{2}$ Particularly, we used their implementation of the algorithm for enumerating the minimal separators by Berry et al. [3]. To compute the PMCs of a graph, we implemented the algorithm by Bouchitté and Todinca [9]. It is important to note that the implementation of these two algorithms is direct, with no special optimization. While these algorithms might take a significant portion of the time, improving their implementation is beyond the scope of this paper, and remains an important future direction. We consider the computation of the minimal separators, PMCs and blocks of each graph (lines 1-2 of MinTriang) the initialization step, as they are computed

[^0]![img-2.jpeg](img-2.jpeg)

Figure 5: Tractability of computing the minimal separators and the PMCs over PIC2011 and PACE2016 graphs.
once at the beginning of RankedTriang, instead of rerunning for each invocation of MinTriang as our algorithms state.

Hardware. We ran all experiments on a 2.5 Ghz 48 -core server with 512 GB of RAM running Ubuntu 14.04.5 LTS. The experiments ran single threaded. ${ }^{3}$

Compared algorithms. We compared our algorithm to that of Carmeli, Kenig and Kimelfeld [10], referred to as CKK, which enumerates with incremental polynomial time and has no guarantees on the order. To the best of our knowledge, no other published algorithms for enumerating minimal triangulations or tree decompositions with completeness guarantees exist, with the exception of DunceCap [40] that is designed for small query graphs; for more details about its performance we refer the reader to Carmeli et al. [10]. CKK requires a black-box minimal triangulator. In our experiments, we used the algorithm LB_TRIANG [5] for this matter, as it was found to allow for enumeration of triangulations of smaller width and fill [10]. In principle, we could also have used our MinTriang, but we chose not to do so since MinTriang requires a long initialization step, and CKK applies its triangulator to many graphs that change between execution calls (hence, the initialization cannot be shared across invocations).

Datasets. Our datasets contain those of Carmeli et al. [10]. These include graphs of three types: probabilistic graphical models from the PIC2011 challenge, ${ }^{4}$ Gaifman graphs of conjunctive queries translated from the TPC-H benchmark (see [10]), and random graphs. Random graphs were generated by the $G(n, p)$ Erdös-Rényi model, where the number of vertices is $n$ and every pair of vertices is (independently) connected by an edge with probability $p$.

Additionally, we used the dataset from the PACE2016 competition [12], where participants competed on the computation of tree decompositions (equivalently, minimal triangulations) of minimal width. These graphs ${ }^{5}$ are samples from named graphs, ${ }^{6}$ control-flow

[^1]
[^0]:    ${ }^{2}$ https://github.com/NofarCarmeli/MinTriangulationsEnumeration

[^1]:    ${ }^{3}$ In future work we will explore how RankedTriang can be parallelized for delay reduction by parallelizing the main loop or using more advanced ideas such as those of Golenberg et al. [16].
    ${ }^{4}$ http://www.cs.huji.ac.il/project/PASCAL/showNet.php
    ${ }^{5}$ The PACE2016 competition graphs can be found at http://github.com/holgerdell/ PACE-treewidth-textbed/tree/master/Instances/pace16
    ${ }^{6}$ https://github.com/freetdi/named-graphs

![img-3.jpeg](img-3.jpeg)

Figure 6: Distribution of the number of minimal separators on the MS tractable PIC2011 and PACE2016 graphs.
graphs, ${ }^{7}$ and the DIMACS graph-coloring problems. ${ }^{8}$ We used graphs from the tracks where time was limited to 100 and 1000 seconds.

### 7.2 The Poly-MS Assumption

We begin with our investigation of the poly-MS assumption, since this study is needed as context for the later evaluation of our enumeration algorithms. In this study, we attempted to generate all minimal separators, and then all PMCs, on our datasets. We describe the success rate, and for each successful case the corresponding number of results.

Real-life graphs. In Figure 5 we report, for each dataset, the number of graphs where the computation terminated in predefined time periods. The columns are as follows.

- Terminated: Graphs $G$ where the time required to compute $\operatorname{Min} S e p(G)$ is under a minute, and the time required to compute $P M C(G)$ is under 30 minutes. These graphs will be used to test our algorithm.
- MS terminated: Graphs $G$ where the time required to compute $\operatorname{Min} S e p(G)$ is under a minute, but the time to compute $P M C(G)$ is over 30 minutes.
- Not terminated: Graphs where the time to compute $\operatorname{Min} S e p(G)$ is over a minute.
As expected, graphs often violate the poly-MS assumption (otherwise the NP-hard problem of computing the tree-width and fill-in would actually be tractable in all of these graphs). In some of the datasets, all of graphs were found infeasible. Nevertheless, the positive finding is that the portion of graphs with a manageable number of minimal separators is quite substantial (around $50 \%$ ). The reader can also observe that in most cases, when we were able to compute the minimal separators, we were also able to compute the PMCs (which is consistent with known theory about the relationship between the two [9]). Figure 6 shows the distribution of the number of minimal separators (in log scale) over the terminated and MS terminated cases of the PIC2011 and PACE2016. One can observe that these numbers are quite often comparable to the number of edges, and sometimes even smaller.

[^0]![img-4.jpeg](img-4.jpeg)

Figure 7: Number of minimal separators on random graph $G(n, p)$. The bottom charts use logarithmic scale. Red marks stand for cases where the computation took over 10 minutes and then stopped.

Random graphs. We ran a similar experiment on random graphs. As said earlier, our random graphs are $G(n, p)$ from assorted $n$ and $p$. We drew graphs with $n \in\{20,30,50,70\}$ vertices, drawing three graphs for each $p \in\{1 / n, \ldots, n / n\}$. This allowed us to observe the correlation between the fraction of edges in the graph and the number of minimal separators. Figure 7 reports the result of these tests. When the computation time exceeded ten minutes, we stopped the execution and, as observed, it happened in the case of $n=50$ and $n=70$ (shown by the red marks). The reader can observe an interesting phenomenon-the number of minimal separators is small for either sparse or dense graphs. In between (around $p=0.25$ ) this number blows up.

### 7.3 Enumeration Evaluation

We now describe our evaluation of the algorithm RankedTriang, and compare it to CKK.

Real-life graphs. Table 2 compares the enumerations of the algorithms on datasets of PIC2011 and PACE2016, where we were able to compute all PMCs (i.e., "Terminated" graphs from the previous section). Each algorithm was executed twice on each graph for 30 minutes, once for minimization of width and again for fill-in. In the case of TPC-H graphs, computing all minimal triangulations is a matter of a few seconds, so we did not include those in the table. Moreover, as we look only at the set of results following a fixed execution time, RankedTriang has no apparent advantage if CKK actually terminates (computing all minimal triangulations); hence, executions where CKK terminates are excluded from the table. The table columns are as follows.

- \#trng: Number of returned minimal triangulations.
- init: For RankedTriang, the initialization time. Importantly, this time is counted into the 30 minutes of the other columns (unless stated otherwise).


[^0]:    ${ }^{7}$ https://github.com/freetdi/CFGs.git
    ${ }^{8}$ URL:http://mat.gsia.cmu.edu/COLOR/instances.html

Table 2: Results on 30-minute executions, optimizing width and fill. For each dataset, the top row relates to RankedTriang and the bottom to CKK. Numbers larger than 1000 are rounded.


- delay: The average delay between returned results.
- delay no init: The average delay between returned results, after initialization.
- min-w: Minimal width of a minimal triangulation returned by the algorithm.
- \#min-w: When the cost is width, number of triangulations returned with a minimal width.
- \# $\leq 1.1-\mathrm{min}-\mathrm{w}$ : Number of near-optimal (within 10\%) triangulations returned by the algorithm, optimizing width.
- min-f: Minimal fill-in of a minimal triangulation returned by the algorithm.
- \#min-f: When optimizing fill-in, the number of triangulations returned with minimal fill-in.
- \# $\leq 1.1-\mathrm{min}-\mathrm{f}$ : Number of near optimal triangulations returned by the algorithm, optimizing fill-in.
Next to the number of optimal (or near optimal) results returned by CKK for each cost, we also report the average percent of optimal results returned, relative to RankedTriang.

We can see that, with the exception of Promedas, the execution cost of RankedTriang is comparable to, and even lower than, CKK. Moreover, the cost of its answers are consistently lower than CKK, which returns only a fraction of the optimal triangulations. On Promedas, RankedTriang is too slow due to a high number of PMCs. For the CSP graphs, it appears as if our algorithm returns more results with a larger average delay. This is caused by two graphs where RankedTriang returns a higher number of results than CKK by an order of magnitude. This is not the case for the rest of the dataset, where the delays are longer and the number of results is smaller in RankedTriang than in CKK.

For PACE2016 100s graphs, the table shows the average percentage of optimal triangulations returned by CKK is much larger than that of RankedTriang. This is caused by only three graphs where the number of results returned by CKK is larger by several orders of magnitude than those returned by RankedTriang, due to a high initialization time and delay. The results returned by the heuristic LB_TRIANG are all optimal in fill-in for these three graphs. This is not the usual case for the graphs in this dataset, and for many of
![img-5.jpeg](img-5.jpeg)

Figure 8: Delay over random graphs $G(n, p)$, and ratio of results of CKK compared to RankedTriang,
them CKK did not generate any result of a minimum fill-in. The reader can observe that under the width cost, the advantage of RankedTriang over CKK is substantial.

Random graphs. We evaluated both algorithms on random graphs $G(n, p)$, in the same experimental setup as for the real graphs. We drew graphs with $n \in\{20,50\}$ vertices, drawing three graphs for each $p \in\{0.5,1,1.5, \ldots, 0.75,0.8\}$. Figure 8 reports the results. Figures 8 (a) and 8 (b) show the average delay between returned results, where the delay of RankedTriang is measured with and without the initialization time. Figures 8(c) and 8(d) show the relative percent of optimal cost results returned by CKK, relative to RankedTriang. We can see that for graphs where the minimal separators and PMCs can be computed, the delay of RankedTriang is smaller than that

of CKK. This occures in all graphs with 20 vertices, and some of the graphs with 50 vertices. In the case of graphs with 50 vertices, RankedTriang does not terminate initialization for probabilities 0.1 through 0.5 , implying for these graphs the number of minimal separators and PMCs is high. For graphs from probabilities closer to this range, RankedTriang has a higher delay, which is caused by a larger number of minimal separators. These results are consistent with the hardness results observed in Section 7.2.

In Appendix B, we describe case studies on two specific graphs.

## 8 CONCLUDING REMARKS

We presented an algorithm for enumerating minimal triangulations, and by implication proper tree decompositions, by increasing cost with polynomial delay, for arbitrary split-monotone (efficiently computable) bag costs. One variant of the algorithm enumerates all minimal triangulations, but requires pre-computing all minimal separators, and hence, makes the poly-MS assumption. The other variant computes all minimal triangulations of a bounded width, and does not require the poly-MS assumption. Our implementation and experimental study shows that the algorithm can lend itself to practical realization, and that the poly-MS assumption is quite often valid.

Various directions are left open for future research, beyond the ones mentioned throughout the paper. For one, it is known that computing a tree decomposition of width $w$ is Fixed-Parameter Tractable (FPT) [7] when taking $w$ as the parameter; this means that $w$ affects only the constant (and not the degree) of the polynomial [13]. Can we extend this result to the enumeration of all tree decompositions of width at most $w$ with FPT delay? Also, can we strengthen our algorithms with further diversity of results to maximize the potential value to the application? How should diversification be defined? In addition to investigating the open questions, we plan to incorporate our algorithm in the framework of Abseher et al. [1] for supervised learning of effective tree decompositions.

## A ADDITIONAL PROOFS

## A. 1 Proof of Theorem 5.5

In this section, we will prove our algorithm returns a minimal triangulation of optimal cost when $\kappa$ is a split monotone bag cost. Since $\kappa$ is a bag cost, its value is equal for all clique trees of a triangulation, and we can prove our lemma by focusing on one clique tree of the minimal triangulation.

Let $H$ be a minimal triangulation of a graph $G$ and $\Omega \in \operatorname{Max} \operatorname{Clq}(H)$. We identify a certain tree decomposition of $H$, and show it is a clique tree. Our definition is recursive over the blocks of $\Omega$, in an approach similar to the triangulation algorithm. For each block $\left(S_{i}, C_{i}\right) \in \operatorname{Blck}_{G}(\Omega)$ we note $\mathcal{T}_{t}=\left(T_{i}, \beta_{i}\right)$ a clique tree of $H_{i}=H\left[S_{i} \cup C_{i}\right]$. Note $\Omega_{i} \in \operatorname{MaxClq}\left(H_{i}\right)$ such that $S_{i} \subset \Omega_{i}$ (at least one exists by Theorem 5.4) and $v_{i} \in \mathrm{~V}\left(T_{i}\right)$ such that $\beta_{i}\left(v_{i}\right)=\Omega_{i}$.

We denote $\mathcal{T}_{H}=\left(T_{H}, \beta_{H}\right)$ a tree decomposition that is a union of all $\mathcal{T}_{i}$, connected by a node $v_{\Omega}$ representing $\Omega . \mathcal{T}_{H}$ is defined as follows:

$$
\begin{aligned}
& \mathrm{V}\left(T_{H}\right)=\bigcup_{i=1}^{p} \mathrm{~V}\left(T_{i}\right) \cup\left\{v_{\Omega}\right\} \\
& \mathrm{E}\left(T_{H}\right)=\bigcup_{i=1}^{p}\left(\mathrm{E}\left(T_{i}\right) \cup\left\{\left\{v_{\Omega}, v_{i}\right\}\right\}\right) \\
& \beta_{H}(u)=\left\{\begin{array}{ll}
\Omega & u=v_{\Omega} \\
\beta_{H_{i}}(u) & u \in \mathrm{~V}\left(T_{i}\right)
\end{array}\right.
\end{aligned}
$$

To prove $\mathcal{T}_{H}$ is a clique tree, we first characterize the maximal cliques of a minimal triangulation $H$, in the same recursive manner.

Lemma A.1. Let $H$ be a minimal triangulation of the graph $G$. Let $\Omega$ be a maximal clique of $H$ and note $H_{i}=H\left[S_{i} \cup C_{i}\right]$ for each block $\left(S_{i}, C_{i}\right) \in \operatorname{Blck}_{G}(\Omega)$ where $1 \leq i \leq p$ for $p=\left|\operatorname{Blck}_{G}(\Omega)\right|$. Then:

$$
\operatorname{MaxClq}(H)=\bigcup_{i=1}^{p} \operatorname{MaxClq}\left(H_{i}\right) \cup\{\Omega\}
$$

Proof. Theorem 5.3 directly implies:

$$
H=\bigcup_{i=1}^{p} H_{i} \cup \Omega^{*}
$$

$\mathcal{K}_{\Omega}$ and each $H_{i}$ are all subgraphs of $H$, and by Theorem 5.3 the graph $\bigcup_{i=1}^{p} H_{i} \cup \mathcal{K}_{\Omega}$ is a minimal triangulation of $G$. Therefore, if $H$ is a minimal triangulation it must hold that $H=\bigcup_{i=1}^{p} H_{i} \cup \mathcal{K}_{\Omega}$.

From equation 3 we can conclude the maximal cliques of $H$ by observing that for any block $\left(S_{i}, C_{i}\right) \in \operatorname{Blck}(\Omega)$ the maximal cliques of $H_{i}$ are maximal cliques in $H$. This is intuitively true, as the vertices of $C_{i}$ are not connected to new nodes, and by Theorem 5.4 $S_{i}$ can not be a maximal clique of $H_{i}$, implying all maximal cliques of $H_{i}$ are maximal cliques in $H$.

Due to Lemma A.1, we can now deduce that $\mathcal{T}_{H}$ is a clique tree of $H$.

Lemma A.2. $\mathcal{T}_{h}$ is a clique tree of $H$.
Proof. To prove $\mathcal{T}_{H}$ is a clique tree of $H$, we must prove:
(1) The vertices of $H$ are covered
(2) The edges of $H$ are covered
(3) The junction-tree property holds
(4) $\beta_{H}$ is a bijection between $\mathrm{V}\left(T_{H}\right)$ and $\operatorname{MaxClq}(H)$

Properties (1), (2) and (4) are directly implied from the definition of $\mathcal{T}_{H}$ and lemma A.1. We will now show that $\mathcal{T}_{H}$ upholds the junction-tree property - for each two nodes $u, v, w \in \mathrm{~V}\left(T_{H}\right)$ where $w$ is a vertex on the route from $u$ to $v$ in $T_{H}$, it holds that $\beta(u) \cap$ $\beta(v) \subseteq \beta(w)$.

We can assume there exists a block $\left(S_{i}, C_{i}\right) \in \operatorname{Blck}_{G}(\Omega)$ such that $u \in \mathrm{~V}\left(T_{i}\right)$. If $v \in \mathrm{~V}\left(T_{i}\right)$, the path between $u$ and $v$ exists in the clique tree $\mathcal{T}_{i}, w \in \mathrm{~V}\left(T_{i}\right)$, and the junction-tree property must hold.

Otherwise, note $v_{i} \in \mathrm{~V}\left(T_{i}\right)$ the node connected to $v_{\Omega}$ in the construction of $\mathcal{T}_{H}$. Since $\beta(v)$ is not contained in the block $\left(S_{i}, C_{i}\right)$, and by definition of $v_{i}$ the following must hold:

$$
\beta(u) \cap \beta(v) \subseteq S_{i}=\beta\left(v_{i}\right) \cap \Omega
$$

This implies if $\beta(w)=\Omega$, then $\beta(u) \cap \beta(v) \subseteq \beta(w)$ and the junctiontree property holds. Furthermore, if $w \in \mathrm{~V}\left(T_{i}\right)$, it must be on the path from $v_{i}$ to $u$. According to our assumption, since the clique intersection property holds in $\mathcal{T}_{i}$ it also holds in $\mathcal{T}_{H}$ :

$$
\beta(u) \cap \beta(v) \subseteq S_{i} \subseteq \beta\left(v_{i}\right) \cap \beta(u) \subseteq \beta(w)
$$

Finally, if there exists another block $\left(S_{j}, C_{j}\right) \in \operatorname{Blck}_{G}(\Omega)$ such that $w \in \mathrm{~V}\left(T_{j}\right)$, due to the structure of $\mathcal{T}_{H}$ we know $v \in \mathrm{~V}\left(T_{j}\right)$. In this case, we can switch the roles of $u$ and $v$, and we have already seen when $w$ belongs to the same block as $u$ the clique intersection property holds.

Next, we would like to clarify the implications of a split monotone bag cost, when used as a cost function over triangulations. $\mathcal{T}_{H}$ is used to prove these implications.

Lemma A.3. Let $H$ and $H^{\prime}$ be two minimal triangulations of a graph $G, \Omega$ be a maximal clique in $\operatorname{MaxClq}(H) \cap \operatorname{MaxClq}\left(H^{\prime}\right)$ and $\kappa$ a split monotone bag cost over tree decompositions. Suppose there is a block $(S, C) \in \operatorname{Blck}_{G}(\Omega)$ such that:

$$
\begin{aligned}
H[\mathrm{~V}(G) \backslash C] & =H^{\prime}[\mathrm{V}(G) \backslash C] \\
\kappa(G[(S, C)], H[(S, C)]) & \leq \kappa(G[(S, C)], H^{\prime}[(S, C)])
\end{aligned}
$$

then $\kappa(G, H) \leq \kappa\left(G, H^{\prime}\right)$.
Proof. Note $H_{1}=H[(S, C)]$ and $H_{2}=H^{\prime}[(S, C)]$.
Observe the clique tree $\mathcal{T}_{H}=\left(T_{H}, \beta_{H}\right)$. It must have a pair of nodes $u, v_{\Omega} \in \mathrm{V}\left(T_{H}\right)$ such that $\beta_{H}\left(v_{\Omega}\right)=\Omega, \beta_{H}(u) \in \operatorname{MaxClq}\left(H_{1}\right)$, the edge $e=\left\{u, v_{\Omega}\right\} \in \mathrm{E}\left(T_{H}\right)$ and $\beta_{H}(u) \cap \beta_{H}\left(v_{\Omega}\right)=S . \mathcal{T}_{H}$ splits by $e$ as $\langle G[\mathrm{~V}(G) \backslash C], \mathcal{T}_{1}, G[(S, C)], \mathcal{T}_{2}\rangle$ where $\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are clique trees of $H[\mathrm{~V}(G) \backslash C]$ and $H_{1}$, respectively. Similarly, $\mathcal{T}_{H^{\prime}}$ can be split by an edge $e^{\prime}$ as $\langle G[\mathrm{~V}(G) \backslash C], \mathcal{T}_{1}^{\prime}, G[(S, C)], \mathcal{T}_{2}^{\prime}\rangle$ where $\mathcal{T}_{1}^{\prime}$ and $\mathcal{T}_{2}^{\prime}$ are clique trees of $H^{\prime}[\mathrm{V}(G) \backslash C]$ and $H_{2}$, respectively.

Since $H^{\prime}[\mathrm{V}(G) \backslash C]=H[\mathrm{~V}(G) \backslash C]$ the clique trees $\mathcal{T}_{1}$ and $\mathcal{T}_{1}^{\prime}$ have the same bags. As $\kappa$ is a bag cost it holds that:

$$
\kappa(G[\mathrm{~V}(G) \backslash C], \mathcal{T}_{1})=\kappa\left(G[\mathrm{~V}(G) \backslash C], \mathcal{T}_{1}^{\prime}\right)
$$

By assumption:

$$
\begin{aligned}
& \kappa(G[(S, C)], T_{2})=\kappa\left(G[(S, C)], H_{1}\right)< \\
& \kappa(G[(S, C)], H_{2})=\kappa\left(G[(S, C)], T_{2}^{\prime}\right)
\end{aligned}
$$

$\kappa$ is a split monotone function and therefore:

$$
\kappa(G, H)=\kappa\left(G, \mathcal{T}_{H}\right) \leq \kappa\left(G, \mathcal{T}_{H^{\prime}}\right)=\kappa\left(G, H^{\prime}\right)
$$

as claimed.
Finally, we can prove the correctness of our algorithm.
Lemma 5.5. Let $\kappa$ be a split-monotone bag cost computable in polynomial time. MinTriang $(\kappa\rangle\langle G)$ returns an minimal triangulation of minimal cost $\kappa$ in time polynomial in the number of minimal separators of the graph. Hence, if $G$ belongs to a poly-MS class of graphs then MinTriang terminates in polynomial time.

Proof. First, we will prove that for each minimal separator $S \in \operatorname{MinSep}(G)$ and full $S$-component $C, \mathcal{H}(S, C)$ (as calculated in line 5 of MinTriang) is an optimal minimal triangulation of the realization $\mathcal{R}(S, C)$, with the cost $\kappa(G[(S, C)], \mathcal{H}(S, C))$. We assume in contradiction this is not the case, and let $(S, C)$ be the smallest block in $G$ such that there exists a minimal triangulation $H^{\prime}$ of the realization $\mathcal{R}(S, C)$ where $H^{\prime} \neq \mathcal{H}(S, C)$ and $\kappa(G[(S, C)], H^{\prime})<$ $\kappa(G[(S, C)], \mathcal{H}(S, C))$.

Notice, since $H^{\prime}$ is a minimal triangulation different from $\mathcal{H}(S, C)$, it can not be a single clique. According to theorem 5.4, there exists a maximal clique $\Omega^{\prime}$ in $H^{\prime}$ such that $S \subset \Omega^{\prime} \subset(S, C)$. For each full block $\left(S_{i}, C_{i}\right) \in \operatorname{Blck}_{\mathcal{R}(S, C)}\left(\Omega^{\prime}\right)$, we note $H_{i}^{\prime}=H^{\prime}\left[S_{i} \cup C_{i}\right]$, and by assumption the minimal triangulation $\mathcal{H}\left(S_{i}, C_{i}\right)$ is optimal (as it is of smaller cardinality than $(S, C)$ ), and the following holds:

$$
\begin{aligned}
\kappa\left(G\left[\left(S_{i}, C_{i}\right)\right], H_{i}^{\prime}\right) & \geq \kappa\left(G\left[\left(S_{i}, C_{i}\right)\right], \mathcal{H}\left(S_{i}, C_{i}\right)\right) \\
& =\kappa\left(G\left[\left(S_{i}, C_{i}\right)\right], H_{\mathcal{R}(S, C)}\left(\Omega^{\prime}\right)\left[S_{i} \cup C_{i}\right]\right)
\end{aligned}
$$

Since $\kappa$ is a split monotone bag cost we can use lemma A. 3 and by selection of $\Omega(S, C)$ (line 4 in MinTriang) this implies:

$$
\begin{aligned}
\kappa(G[(S, C)], H^{\prime}) & \geq \kappa\left(G[(S, C)], H_{\mathcal{R}(S, C)}\left(\Omega^{\prime}\right)\right) \\
& \geq \kappa\left(G[(S, C)], H_{\mathcal{R}(S, C)}(\Omega(S, C))\right) \\
& =\kappa(G[(S, C)], \mathcal{H}(S, C))
\end{aligned}
$$

in contradiction to our assumption.
We can conclude the optimality of $\mathcal{H}(G)$ in a similar manner, based on theorem 5.3. Let $\Omega^{\prime}$ be any maximal clique of $H^{\prime}$. As previously, the following inequality holds:

$$
\begin{aligned}
\kappa\left(G, H^{\prime}\right) & \geq \kappa\left(G, H_{G}\left(\Omega^{\prime}\right)\right) \\
& \geq \kappa\left(G, H_{G}(\Omega(G))\right) \\
& =\kappa(G, \mathcal{H}(G))
\end{aligned}
$$

This concludes $\mathcal{H}(G)$ is an optimal minimal triangulation of $G$.

## A. 2 Proof of Lemma 6.2

Lemma 6.2. Let $\kappa$ be a cost function, $G$ a graph, and $[I, X]$ a set of constraints on minimal triangulations of $G$.
(1) If $\kappa$ is a split-monotone bag cost, then so is $\kappa[I, X]$.
(2) If $\kappa$ can be computed in polynomial time in the size of $G$, then $\kappa[I, X]$ can be computed in polynomial time in the size of $G, I$ and $X$.

Proof. Let $H, H^{\prime}$ be two minimal triangulations of a graph $G$ and $\Omega$ be a maximal clique in $\operatorname{MaxClq}(H) \cap \operatorname{MaxClq}\left(H^{\prime}\right)$. Let $\mathcal{T}$ and $\mathcal{T}^{\prime}$ be tree decompositions of $H$ and $H^{\prime}$, respectively, such that $\mathcal{T}$ and $\mathcal{T}^{\prime}$ can be split as $\left(G_{1}, \mathcal{T}_{1}, G_{2}, \mathcal{T}_{2}\right)$ and $\left(G_{1}, \mathcal{T}_{1}^{\prime}, G_{2}, \mathcal{T}_{2}^{\prime}\right)$,
respectively. We assume (for $i=1,2$ ):

$$
\kappa[I, X]\left(G_{i}, \mathcal{T}_{i}\right) \leq \kappa[I, X]\left(G_{i}, \mathcal{T}_{i}^{\prime}\right)
$$

We would like to prove:

$$
\kappa[I, X](G, \mathcal{T}) \leq \kappa[I, X]\left(G, \mathcal{T}^{\prime}\right)
$$

By definition of $\kappa[I, X]$, if both $H$ and $H^{\prime}$ do not violate any constraints, the function $\kappa[I, X]$ if equivalent to $\kappa$, and equation 4 holds. Furthermore, if $H$ does not violate any constraint but $H^{\prime}$ does equation 4 holds trivially:

$$
\begin{aligned}
\kappa[I, X](G, \mathcal{T}) & =\kappa[I, X](G, H) \\
& \leq \kappa[I, X]\left(G, H^{\prime}\right)=\kappa[I, X]\left(G, \mathcal{T}^{\prime}\right)=\infty
\end{aligned}
$$

To complete the proof, it suffices to show that if $H$ violates some constraint, $H^{\prime}$ must violate a constraint as well, implying both their costs are $\infty$, and equation 4 holds.

Notice $\kappa[I, X]\left(G_{i}, \mathcal{T}_{i}\right)=\kappa[I, X]\left(G_{i}, H\left[\mathrm{~V}\left(G_{i}\right)\right]\right)$ and $\kappa[I, X]\left(G_{i}, \mathcal{T}_{i}^{\prime}\right)=$ $\kappa\left[I, X\right]\left(G_{i}, H^{\prime}\left[\mathrm{V}\left(G_{i}\right)\right]\right)$ for $i=1,2$. We note $H_{i}=H\left[\mathrm{~V}\left(G_{i}\right)\right]$ and $H_{i}^{\prime}=H^{\prime}\left[\mathrm{V}\left(G_{i}\right)\right] . T_{i}$ and $T_{i}^{\prime}$ are clique trees, and from the junctiontree property $S=\mathrm{V}\left(G_{1}\right) \cap \mathrm{V}\left(G_{2}\right) \in \operatorname{MinSep}(H) \operatorname{capMinSep}\left(H^{\prime}\right)$.

Assume $H$ violates some constraint $U \in I \cap X$. If $U \subseteq \mathrm{~V}\left(G_{i}\right)$ (for $\mathrm{i}=1,2$ ), $H_{i}$ must violate $U$ and:

$$
\kappa[I, X]\left(G_{i}, H_{i}^{\prime}\right) \geq \kappa[I, X]\left(G_{i}, H_{i}\right)=\infty
$$

We can see some constraint is violated in $H_{i}^{\prime}$, and therefore in $H^{\prime}$. We deduce $\kappa[I, X]\left(G, H^{\prime}\right)=\infty$, and equation 4 holds.

Otherwise, $U$ is not contained in any node of $\mathcal{T}$ or $\mathcal{T}^{\prime}$ and can not be a clique in $H$ or $H^{\prime}$. If $U$ is violated in $H$ then $U \in I$, and $U$ must be violated in $H^{\prime}$ as well.

We can conclude if $H$ violates a constraint, so does $H^{\prime}$, implying the lemma holds and the function $\kappa[I, X]$ is split monotone.

## A. 3 Proof of Proposition 6.1

Proposition 6.1. Let G be class of graphs, and $\kappa$ a bag cost. If, on graphs of G, the minimal triangulations can be enumerated with polynomial delay by increasing $\kappa$, then so can the proper tree decompositions.

Proof. Recall from Theorem 2.2 that the proper tree decompositions are precisely the cliques trees of the minimal triangulations. It is an easy observation that two minimal triangulations have disjoint sets of clique trees (since the two have different sets of edges). Since $\kappa$ is a bag cost, the cost of each of its clique trees is the same. Hence, we can enumerate the proper tree decompositions by increasing cost by enumerating the minimal triangulations by increasing cost, and for each minimal triangulations we enumerate its clique trees. So, we establish the lemma if we can enumerate with polynomial delay all of the clique trees of a minimal triangulation. As observed by Carmeli et al. [10], this can be done by a straightforward combination of past results, as explained next.

Jordan [24] shows that a tree over the maximal cliques of a chordal graph $H$ is a clique tree if and only if it is a maximal spanning tree, where the weight of an edge between two maximal cliques is the cardinality of their intersection. As the number of maximal cliques of a chordal graph is linear in the number of nodes (Theorem 2.2), this enumeration problem is reduced to enumerating

![img-6.jpeg](img-6.jpeg)

Figure 9: Number of triangulations returned and their widths on a CSP (top) and object-detection (bottom) graphs.
all maximal spanning trees, which can be solved in polynomial delay [41].

## B CASE STUDY

The experiments in Section 7 show that in most cases, CKK has a shorter delay than RankedTriang, though opposite situations exist. In this experiment, we focus on two graphs, one from the Constraint Satisfaction Problem dataset (mycie15g_3) and one from the Object Detection dataset (deer_rescaled_3020.K15.F1.75). Figure 9 shows the runtime and width of the returned triangulations throughout the execution of the algorithms. The horizontal axis represents time since the beginning of the execution, in intervals of 10 seconds. At each interval, the number of results, along with the median and minimum widths of these results, are reported.

Comparing Figures 9(a) and 9(b), we observe that CKK returns substantially more results for the CSP graph. On the other hand, the results of CKK are of higher width. Our algorithm, RankedTriang, returns a small amount of results, but they are all of optimal width. In the case of Figures 9(c) and 9(d), for the object-detection graph, we can see that CKK has a longer delay. During many intervals, CKK returned a single result. Here too, our algorithm returns only results of a minimal width. Finally, we observe that in both graphs, the delay of RankedTriang is far more stable than that of CKK.