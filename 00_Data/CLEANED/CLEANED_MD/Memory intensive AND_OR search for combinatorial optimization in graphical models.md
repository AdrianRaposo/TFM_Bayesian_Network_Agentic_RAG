# Memory Intensive AND/OR Search for Combinatorial Optimization in Graphical Models 

Radu Marinescu ${ }^{\mathrm{a}, *, 1}$, Rina Dechter ${ }^{\mathrm{b}}$<br>${ }^{a}$ Cork Constraint Computation Centre, University College Cork, Ireland<br>${ }^{\mathrm{b}}$ Donald Bren School of Information and Computer Science, University of California, Irvine, CA 92697, USA


#### Abstract

In this paper we explore the impact of caching during search in the context of the recent framework of AND/OR search in graphical models. Specifically, we extend the depth-first AND/OR Branch-and-Bound tree search algorithm to explore an AND/OR search graph by equipping it with an adaptive caching scheme similar to good and no-good recording. Furthermore, we present best-first search algorithms for traversing the same underlying AND/OR search graph and compare both algorithms empirically. We focus on two common optimization problems in graphical models: finding the Most Probable Explanation (MPE) in belief networks and solving Weighted CSPs (WCSP). In an extensive empirical evaluation we demonstrate conclusively the superiority of the memory intensive AND/OR search algorithms on a variety of benchmarks.


Key words: search, AND/OR search, decomposition, graphical models, Bayesian networks, constraint networks, constraint optimization

## 1 Introduction

This is the second of two articles describing and evaluating the power of AND/OR search spaces for combinatorial optimization in graphical models. The first paper [1] focused on extending Branch-and-Bound algorithms to AND/OR search spaces which have no cycles, namely to AND/OR search trees. The virtue of the AND/OR

[^0]
[^0]:    * Corresponding author.

    Email addresses: r.marinescu@4c.ucc.ie (Radu Marinescu), dechter@ics.uci.edu (Rina Dechter).
    ${ }^{1}$ This work was done while at the University of California, Irvine.

representation is that the search space size may be far smaller than that of a traditional OR representation which often translates to significant time savings. In the current paper we improve efficiency further by using more memory, exploring what we refer to as the context minimal AND/OR search graph.

Specifically, we extend the AND/OR Branch-and-Bound tree search algorithm introduced in [1-3] to explore the context minimal AND/OR search graph using a flexible caching mechanism that can adapt to memory limitations. The caching scheme is similar to good and no-good recording [4,5] which were used in several recent schemes such as Recursive Conditioning [6], Valued Backtracking [7] and Backtracking with Tree Decompositions [8]. Our contributions beyond those schemes is in presenting these ideas in an independent manner using the notion of AND/OR search spaces and extending optimization techniques to this framework. Finally, we carried out an extensive empirical study on which we report.

Clearly, the AND/OR search space can be explored by any traversal algorithm. So we next investigated the other most common search approach which is BestFirst search. Best-First search is known to be superior among memory intensive search algorithms [9]. We therefore present a new AND/OR search algorithm that explores the context minimal AND/OR search graph in a best-first manner. Under conditions of admissibility and monotonicity of the heuristic function, best-first search is known to expand the minimal number of nodes, at the expense of using additional memory [9]. We will show that these savings in number of nodes often translate into significant time savings.

The efficiency of both depth-first and best-first AND/OR search methods also depends on the accuracy of the guiding heuristic function. We used the Mini-Bucket heuristic [10] which is extracted from the functional specification of the graphical model using the Mini-Bucket approximation algorithm [11]. These heuristics were explored in [1] in the context of AND/OR search trees. Following [1,2], we continue to explore empirically the efficiency of static and dynamic mini-bucket heuristics within the cache-based search spaces.

As in our earlier work [1-3], we apply the algorithms to finding the Most Probable Explanation (MPE) in belief networks [12] and to solving Weighted CSPs [13]. Our results show conclusively that the memory intensive AND/OR search algorithms improve dramatically over competitive approaches, especially when the heuristic estimates are less accurate and do not prune the search space effectively. We demonstrate the impact of caching, the impact of the strength of the guiding evaluation function, as well as the impact of best-first versus depth-first search regimes. We also investigate other factors that impact the performance of any search algorithm such as: the availability of hard constraints (i.e., determinism), the availability of good initial upper bounds, and the availability of good ordering schemes (e.g., pseudo trees).

The paper is organized as follows. Sections 2 and 3 provide background on graphical models and on the AND/OR search spaces. Sections 4 and 5 present the new depth-first and best-first AND/OR search algorithms exploring the context minimal AND/OR graph. Section 6 reviews the mini-bucket heuristics for AND/OR search. In Section 7 we present an extensive empirical evaluation of the proposed memory intensive search methods, while Section 8 provides concluding remarks and directions of future research. The relevant related work is discussed in detail in [1]. This paper is based in part on [14-16].

# 2 Background 

### 2.1 Preliminaries

A reasoning problem is defined in terms of a set of variables taking values on finite domains and a set of functions defined over these variables. We denote variables by uppercase letters (e.g., $X, Y, Z, \ldots$ ), subsets of variables by bold faced uppercase letters (e.g., $\mathbf{X}, \mathbf{Y}, \mathbf{Z}, \ldots$ ) and values of variables by lower case letters (e.g., $x, y, z, \ldots$ ). An assignment $\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)$ can be abbreviated as $x=\left(\left\langle X_{1}, x_{1}\right\rangle, \ldots,\left\langle X_{n}, x_{n}\right\rangle\right)$ or $x=\left(x_{1}, \ldots, x_{n}\right)$. For a subset of variables $\mathbf{Y}, D_{\mathbf{Y}}$ denotes the Cartesian product of the domains of variables in $\mathbf{Y} . x_{\mathbf{Y}}$ and $x[\mathbf{Y}]$ are both used as the projection of $x=\left(x_{1}, \ldots, x_{n}\right)$ over a subset $\mathbf{Y}$. We denote functions by letters $f, h, g$ etc., and the scope (set of arguments) of a function $f$ by $\operatorname{scope}(f)$.

DEFINITION 1 (directed, undirected graphs) $A$ directed graph is defined by a pair $G=\{\mathbf{V}, \mathbf{E}\}$, where $\mathbf{V}=\left\{X_{1}, \ldots, X_{n}\right\}$ is a set of vertices (nodes), and $\mathbf{E}=$ $\left\{\left(X_{i}, X_{j}\right) \mid X_{i}, X_{j} \in V\right\}$ is a set of edges (arcs). If $\left(X_{i}, X_{j}\right) \in \mathbf{E}$, we say that $X_{i}$ points to $X_{j}$. The degree of a vertex is the number of incident arcs to it. For each vertex $X_{i}$, pa $\left(X_{i}\right)$ or $p a_{i}$, is the set of vertices pointing to $X_{i}$ in $G$, while the set of child vertices of $X_{i}$, denoted $\operatorname{ch}\left(X_{i}\right)$, comprises the variables that $X_{i}$ points to. The family of $X_{i}$, denoted $F_{i}$, includes $X_{i}$ and its parent vertices. A directed graph is acyclic if it has no directed cycles. An undirected graph is defined similarly to a directed graph, but there is no directionality associated with the edges.

DEFINITION 2 (induced graph, induced width) The induced graph of a graph $G$ relative to an ordering $d$ of its nodes, denoted $G^{*}(d)$, is obtained as follows: nodes are processed from last to first; when node $X$ is processed, all its preceding neighbors are connected. A new edge that is added to the graph by this procedure is called an induced edge. Given a graph and an ordering of its nodes, the width of a node is the number of edges connecting it to nodes lower in the ordering. The induced width (or treewidth) of a graph, denoted $w^{*}(d)$, is the maximum width of nodes in the induced graph.

# 2.2 Graphical Models 

A graphical model is defined by a collection of functions $\mathbf{F}$, over a set of variables $\mathbf{X}$, conveying probabilistic or deterministic information, whose structure is captured by a graph. We used the formalism presented in [17].

Definition 3 (graphical model, primal graph) A graphical model is a 4-tuple $\mathcal{R}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}, \otimes\rangle$, where: 1. $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ is a set of variables; 2. $\mathbf{D}=$ $\left\{D_{1}, \ldots, D_{n}\right\}$ is a set of finite domains of values; 3. $\mathbf{F}=\left\{f_{1}, \ldots, f_{r}\right\}$ is a set of real valued functions, each defined over a subset of variables $S_{i} \subseteq \mathbf{X}$ (i.e., the scope); 4. $\otimes_{i} f_{i} \in\left\{\prod_{i} f_{i}, \sum_{i} f_{i}\right\}$ is a combination operator. The graphical model represents the combination of all its functions, namely $\otimes_{i=1}^{r} f_{i}$. When the combination operator is irrelevant we denote $\mathcal{R}$ by $\langle\mathbf{X}, \mathbf{D}, \mathbf{F}\rangle$. The primal graph of a graphical model is an undirected graph that has the variables as its vertices and edges connecting any two variables that appear in the scope of the same function.

There are various queries (tasks) that can be posed over graphical models. We refer to all as automated reasoning problems. In general, an optimization task is a reasoning problem defined as a function from a graphical model to a set of elements, most commonly, the real numbers.

DEFINITION 4 (constraint optimization problem) $A$ constraint optimization problem is a pair $\mathcal{P}=\left\langle\mathcal{R}, \Downarrow_{\mathbf{X}}\right\rangle$, where $\mathcal{R}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}, \otimes\rangle$ is a graphical model. If $S$ is the scope of function $f \in \mathbf{F}$ then $\Downarrow_{S} f \in\left\{\max _{S} f, \min _{S} f\right\}$. The optimization problem is to compute $\Downarrow_{\mathbf{X}} \otimes_{i=1}^{r} f_{i}$. The min/max ( $\Downarrow$ ) operator is called an elimination operator because it removes the arguments from the input functions' scopes.

For a detailed description and examples of graphical models such as constraint networks, cost networks and belief networks we refer the reader to [17,18,1].

## 3 AND/OR Search Spaces for Graphical Models

The usual way to do search in graphical models is to instantiate variables in turn, following a static or dynamic variable ordering. In the simplest case, this process defines a search tree (called here OR search tree), whose nodes represent states in the state of partial assignments. This search space does not capture the structure of the underlying graphical model. To remedy this problem, an AND/OR search space was recently introduced in the context of general graphical models [18]. It specializes the AND/OR space introduced in [19] to graphical models. The AND/OR search space is defined using a backbone pseudo tree [20,5]. In subsections 3.1 and 3.2 we will give a brief overview of searching the AND/OR search trees by Branch-and-Bound, which was presented in detail in [1].

Definition 5 (pseudo tree, extended graph) Given an undirected graph $G=$ $(\mathbf{V}, \mathbf{E})$, a directed rooted tree $\mathcal{T}=\left(\mathbf{V}, \mathbf{E}^{\prime}\right)$ defined on all its nodes is called pseudo tree if any arc of $G$ which is not included in $\mathbf{E}^{\prime}$ is a back-arc, namely it connects a node to an ancestor in $\mathcal{T}$. The arcs in $\mathbf{E}^{\prime}$ may not all be included in $\mathbf{E}$. Given a pseudo tree $\mathcal{T}$ of $G$, the extended graph of $G$ relative to $\mathcal{T}$ is defined as $G^{\mathcal{T}}=$ $\left(\mathbf{V}, \mathbf{E} \cup \mathbf{E}^{\prime}\right)$.

As in [1], we consider in the remainder of the paper an optimization problem $\mathcal{P}=$ $\langle\mathcal{R}, \min \rangle$ over a graphical model $\mathcal{R}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}, \Sigma\rangle$ for which the combination and elimination operators are summation and minimization, respectively.

# 3.1 AND/OR Search Trees for Graphical Models 

In this subsection we overview briefly the AND/OR search tree for graphical models which was introduced in [18,1]. Given a graphical model $\mathcal{R}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}\rangle$, its primal graph $G$ and a pseudo tree $\mathcal{T}$ of $G$, the associated AND/OR search tree, denoted $S_{\mathcal{T}}(\mathcal{R})$, has alternating levels of OR and AND nodes. The OR nodes are labeled $X_{i}$ and correspond to the variables. The AND nodes are labeled $\left\langle X_{i}, x_{i}\right\rangle$ and correspond to the values in the domains of the variables. The structure of the AND/OR search tree is based on the underlying pseudo tree. The root of $S_{\mathcal{T}}(\mathcal{R})$ is an OR node labeled with the root of $\mathcal{T}$. The children of an OR node $X_{i}$ are AND nodes labeled with assignments $\left\langle X_{i}, x_{i}\right\rangle$. The children of an AND node $\left\langle X_{i}, x_{i}\right\rangle$ are OR nodes labeled with the children of variable $X_{i}$ in the pseudo tree $\mathcal{T}$. A path from the root of the search tree $S_{\mathcal{T}}(\mathcal{R})$ to a node $n$ is denoted by $\pi_{n}$. The assignment sequence along $\pi_{n}$, denoted $\operatorname{asgn}\left(\pi_{n}\right)$, is the set of value assignments associated with the AND nodes along $\pi_{n}$ (see Fig. 1 in [1] for an example of an AND/OR tree).

A solution tree of an AND/OR search tree $S_{\mathcal{T}}(\mathcal{R})$ is an AND/OR subtree $T$ such that: 1) it contains the root $s$ of $S_{\mathcal{T}}(\mathcal{R}) ; 2$ ) if a non-terminal AND node $n \in S_{\mathcal{T}}(\mathcal{R})$ is in $T$ then all of its children are in $T ; 3$ ) if a non-terminal OR node $n \in S_{\mathcal{T}}(\mathcal{R})$ is in $T$ then exactly one of its children is in $T ; 4$ ) all its leaf (terminal) nodes are consistent.

Based on earlier work [18], it can be shown that given a graphical model $\mathcal{R}$ and a pseudo tree $\mathcal{T}$, the size of the AND/OR search tree $S_{\mathcal{T}}(\mathcal{R})$ is $O\left(n \cdot k^{m}\right)$ where $m$ is the depth of the pseudo tree, $n$ is the number of variables, and $k$ bounds the domain size. Moreover, a graphical model that has treewidth $w^{*}$ has an AND/OR search tree whose size is $O\left(n \cdot k^{w^{*} \cdot \log n}\right)$.

The arcs from nodes $X_{i}$ to $\left\langle X_{i}, x_{i}\right\rangle$ in an AND/OR search tree are annotated by weights derived from the cost functions in $\mathbf{F}$.

Definition 6 (arc weight) The weight $w_{(n, m)}\left(X_{i}, x_{i}\right)$ (or simply $w(n, m)$ ) of the $\operatorname{arc}(n, m)$, where $X_{i}$ labels $n$ and $\left\langle X_{i}, x_{i}\right\rangle$ labels $m$, is the combination (i.e., sum)

of all the functions whose scope includes $X_{i}$ and is fully assigned along the path from the root to $m$, evaluated at the values along the path.

With each node $n$ of the weighted AND/OR search tree we can associate a value $v(n)$ which stands for the optimal solution cost of the subproblem below $n$, conditioned on the assignment on the path leading to it [18,1]. It was shown that $v(n)$ obeys the following recursive definition:

Definition 7 (node value) The value $v(n)$ of a node $n$ in a weighted AND/OR tree is defined recursively as follows (where $\operatorname{succ}(n)$ are the children of $n$ ):
$v(n)= \begin{cases}0 & , \text { if } n=\langle X, x\rangle \text { is a terminal AND node } \\ \infty & , \text { if } n=X \text { is a terminal OR node } \\ \sum_{m \in \operatorname{succ}(n)} v(m) & , \text { if } n=\langle X, x\rangle \text { is an AND node } \\ \min _{m \in \operatorname{succ}(n)}(w(n, m)+v(m)) & , \text { if } n=X \text { is an OR node }\end{cases}$

Clearly, the value of the root node $s$ is the minimal cost solution to the initial problem, namely $v(s)=\min _{\mathbf{X}} \sum_{i=1}^{r} f_{i}(\mathbf{X})$.

# 3.2 AND/OR Branch-and-Bound Search on AND/OR Trees 

In [1-3] we introduced a new generation of linear space Branch-and-Bound search algorithms that exploit the underlying structure of the graphical model by traversing in a depth-first manner an AND/OR search tree associated with the graphical model. During search, the algorithm maintains the cost of the best solution found so far, which is an upper bound $u b$ on the minimal cost solution. In addition, each node $n$ in the search tree is also associated with a static heuristic function $h(n)$ that underestimates the minimal cost solution $v(n)$ to the subproblem below $n$, and it can be either pre-compiled or computed during search. The current partial solution being pursued is represented by a partial solution tree, $T^{\prime}$. Given the current $T^{\prime}$, the algorithm then computes a heuristic lower bounding estimate $f\left(T^{\prime}\right)$ on the optimal extension of $T^{\prime}$ to a complete solution tree and, if $f\left(T^{\prime}\right) \geq u b$, it prunes the search space below the current tip node.

The efficiency of the algorithm depends heavily on its guiding heuristic function. In [1,2] we investigated the power of a heuristic generation scheme based on the Mini-Bucket approximation [11], in both static and dynamic setups. Since the MiniBucket algorithm is controlled by a bounding parameter, it allows heuristics having varying degrees of accuracy and results in a spectrum of search algorithms that can trade off heuristic computation and search.

We evaluated empirically the AND/OR Branch-and-Bound algorithm with the minibucket heuristics for probabilistic and deterministic optimization tasks [1,2]. The results showed conclusively that the scheme improves dramatically over the traditional OR approaches, in many cases yielding several orders of magnitude improvements in time and size of the search space explored.

In the following subsection we overview the notion of AND/OR search graph for general graphical models, which was presented in [18].

# 3.3 AND/OR Search Graphs for Graphical Models 

It is often the case that a search space that is a tree can become a graph if identical nodes that root identical search subspaces and which correspond to identical reasoning subproblems are identified. Any two identical nodes can be merged, thus reducing the size of the search space. Some of these nodes can be identified based on graph-based contexts.

First, we present the notion of induced width of a pseudo tree of a graph $G$ [18] which is necessary for bounding the size of the AND/OR search graphs. We denote by $d_{D F S}(\mathcal{T})$ a linear DFS ordering of a tree $\mathcal{T}$.

DEFINITION 8 (induced width of a pseudo tree) Given a graph $G$, the induced width of $G$ relative to a pseudo tree $\mathcal{T}, w_{\mathcal{T}}(G)$, is the induced width along the $d_{D F S}(\mathcal{T})$ ordering of $G^{\mathcal{T}}$, the extended graph of $G$ relative to $\mathcal{T}$.

We next provide definitions which allow identifying nodes that can be merged. The idea is to determine a minimal set of predecessor variables to $X_{i}$, whose assignment completely determines the subproblem below $X_{i}$ along the current path. Since a path to an OR node $X_{i}$ and to an AND node $\left\langle X_{i}, x_{i}\right\rangle$ differs by the assignment $x_{i}$ to $X_{i}$, these minimal assignments that we seek can differ. Indeed, the following definitions distinguish between two types of context-based caching which are quite subtle. In these definitions, ancestors and descendants are with respect to the pseudo tree $\mathcal{T}$, while the connectivity is with respect to the primal graph $G$.

DEFINITION 9 (parents) Given a primal graph $G$ and a pseudo tree $\mathcal{T}$ of a reasoning problem $\mathcal{P}$, the parents of an OR node $X_{i}$, denoted by $p a_{i}$ or $p a_{X_{i}}$, are the ancestors of $X_{i}$ which are connected to $X_{i}$ or to descendants of $X_{i}$ in $G$.

DEFINITION 10 (parent-separators) Given a primal graph $G$ and a pseudo tree $\mathcal{T}$ of a reasoning problem $\mathcal{P}$, the parent-separators of $X_{i}$ (or of $\left\langle X_{i}, x_{i}\right\rangle$ ), denoted by pas $a_{i}$ or pas $x_{i}$, are formed by $X_{i}$ and its ancestors that are connected in $G$ to descendants of $X_{i}$ (not only to $X_{i}$ ).

It follows from these definitions that the parents of $X_{i}, p a_{i}$, separate in the primal

![img-0.jpeg](img-0.jpeg)

Fig. 1. AND/OR search graph for graphical models.
graph $G$ (and also in the extended graph $G^{\mathcal{T}}$ and in the induced extended graph $\left.G^{\mathcal{T}^{*}}\right)$ the ancestors of $X_{i}$ from its descendants. Similarly, the parent-separators set of $X_{i}$, pas $_{i}$, separate the ancestors of $X_{i}$ from its descendants. It is also easy to see that each variable $X_{i}$ and its parents $p a_{i}$ form a clique in the induced graph $G^{\mathcal{T}^{*}}$. As was shown in [18], there exists the following relation between $p a_{i}$ and $p a s_{i}$ : (1) if $Y$ is the single child of $X$ in $\mathcal{T}$, then $p a s_{X}=p a_{Y}$; (2) if $X$ has children $Y_{1}, \ldots, Y_{k}$ in $\mathcal{T}$, then $p a s_{X}=\cup_{i=1}^{k} p a_{Y_{i}}$.

THEOREM 1 (context based merge [18]) Given $G^{\mathcal{T}^{*}}$, let $\pi_{n_{1}}$ and $\pi_{n_{2}}$ be any two paths in an AND/OR search graph, ending with two nodes, $n_{1}$ and $n_{2}$.
(1) If $n_{1}$ and $n_{2}$ are AND nodes labeled by $\left\langle X_{i}, x_{i}\right\rangle$ and $\operatorname{asgn}\left(\pi_{n_{1}}\right)\left[p a s_{X_{i}}\right]=$ $\operatorname{asgn}\left(\pi_{n_{2}}\right)\left[p a s_{X_{i}}\right]$ then the AND/OR search subtrees rooted by $n_{1}$ and $n_{2}$ are identical. The $\operatorname{asgn}\left(\pi_{n_{i}}\right)\left[p a s_{X_{i}}\right]$ is called the AND context of $n_{i}$.
(2) If $n_{1}$ and $n_{2}$ are OR nodes labeled by $X_{i}$ and $\operatorname{asgn}\left(\pi_{n_{1}}\right)\left[p a_{X_{i}}\right]=\operatorname{asgn}\left(\pi_{n_{2}}\right)\left[p a_{X_{i}}\right]$ then the AND/OR search subtrees rooted by $n_{1}$ and $n_{2}$ are identical. The $\operatorname{asgn}\left(\pi_{n_{i}}\right)\left[p a_{X_{i}}\right]$ is called the OR context of $n_{i}$.

DEFINITION 11 (context minimal AND/OR search graph [18]) The AND/OR search graph of $\mathcal{R}$ based on the backbone pseudo tree $\mathcal{T}$ that is closed under the contextbased merge operator is called the context minimal AND/OR search graph and is

denoted by $C_{\mathcal{T}}(\mathcal{R})$.
We should note that we can in general merge nodes based both on AND and OR contexts. However, it was shown in [18] that doing just one of them renders the other unnecessary (namely, yielding a small constant factor only). In this paper we will use AND context based merging.

THEOREM 2 (size of context minimal AND/OR search graphs [18]) Given a graphical model $\mathcal{R}$, its primal graph $G$, and a pseudo tree $\mathcal{T}$ having induced width $w^{*}=w_{\mathcal{T}}(G)$, the size of the context minimal AND/OR search graph based on $\mathcal{T}, C_{\mathcal{T}}(\mathcal{R})$, is $O\left(n \cdot k^{w^{*}}\right)$, where $k$ bounds the domain size.

Example 1 Consider the example given in Fig. 1 which is based on Example 1 from [1]. The AND contexts of each node in the pseudo tree is given in square brackets in Fig. 1(a). The context minimal AND/OR search graph (based on AND merging) is given in Fig. 1(b). Its size is far smaller than that of the AND/OR search tree from Fig. 1 in [1] (16 vs. 54 AND nodes). Similarly, Fig. 1(d) shows the context minimal AND/OR graph based on the OR contexts given in Fig. 1(c). Its size is larger than that of the AND based graph (38 vs. 16 AND nodes) in this case. Consider for example variable $C$ with AND-context $\{B, C\}$ from Fig. 1(a). In Fig. 1 from [1], the search subtrees below any appearance of $(B=0, C=0)$ (i.e., corresponding to the subproblems below the AND nodes labeled $\langle C, 0\rangle$ along the paths containing the assignments $B=0$ and $C=0$, respectively) are all identical, and therefore can be merged, as shown in the search graph from Fig. 1(b).

# 4 AND/OR Branch-and-Bound with Caching 

Traversing AND/OR search spaces by depth-first Branch-and-Bound or by bestfirst search algorithms was described as early as [19,21,22] in the context of general search spaces. In the following two sections we revisit the definitions needed to describe the algorithms. We will then introduce two classes of memory intensive search algorithms that explore the context minimal AND/OR search graph of graphical models, in either a depth-first or best-first manner, for finding optimal solution trees. The algorithms extend those presented in [1] for exploring AND/OR search trees to algorithms exploring AND/OR search graphs.

DEFINITION 12 (partial solution tree) $A$ partial solution tree $T^{\prime}$ of a context minimal AND/OR search graph $C_{\mathcal{T}}(\mathcal{R})$ is a subtree which: (1) contains the root node $s$ of $C_{\mathcal{T}}(\mathcal{R})$; (2) if $n$ in $T^{\prime}$ is an OR node then it contains one of its AND child nodes in $C_{\mathcal{T}}(\mathcal{R})$, and if $n$ is an AND node it contains all its OR children in $C_{\mathcal{T}}(\mathcal{R})$. A node in $T^{\prime}$ is called a tip node if it has no children in $T^{\prime}$. A tip node is either a terminal node (if it has no children in $C_{\mathcal{T}}(\mathcal{R})$ ), or a non-terminal node (if it has children in $\left.C_{\mathcal{T}}(\mathcal{R})\right)$.

A partial solution tree represents extension $\left(T^{\prime}\right)$, the set of all full solution trees which can extend it. A partial solution tree whose all tip nodes are terminal in $C_{\mathcal{T}}(\mathcal{R})$ is a solution tree.

In general, Branch-and-Bound algorithms are guided by a lower bound heuristic function. The extension of heuristic evaluation functions to subtrees in an AND/OR search space for graphical models was elaborated in [1]. We briefly introduce here the main elements and refer the reader for further details to the earlier references.

Heuristic Lower Bounds on Partial Solution Trees. We start with the notions of exact heuristic evaluation functions of a partial solution tree [1,2], which will be used to guide the AND/OR Branch-and-Bound.

The exact evaluation function $f^{*}\left(T^{\prime}\right)$ of a partial solution tree $T^{\prime}$ is the minimum of the costs of all solution trees extending $T^{\prime}$, namely: $f^{*}\left(T^{\prime}\right)=\min \{f(T) \mid T \in$ extension $\left.\left(T^{\prime}\right)\right\}$. If $f^{*}\left(T_{n}^{\prime}\right)$ is the exact evaluation function of a partial solution tree rooted at node $n$, then $f^{*}\left(T_{n}^{\prime}\right)$ can be computed recursively, as follows:

1. If $T_{n}^{\prime}$ consists of a single node $n$ then $f^{*}\left(T_{n}^{\prime}\right)=v(n)$.
2. If $n$ is an OR node having the AND child $m$ in $T_{n}^{\prime}$, then $f^{*}\left(T_{n}^{\prime}\right)=w(n, m)+$ $f^{*}\left(T_{m}^{\prime}\right)$.
3. If $n$ is an AND node having OR children $m_{1}, \ldots, m_{k}$ in $T_{n}^{\prime}$, then $f^{*}\left(T_{n}^{\prime}\right)=$ $\sum_{i=1}^{k} f^{*}\left(T_{m_{i}}^{\prime}\right)$.

If each non-terminal tip node $m$ of $T^{\prime}$ is assigned a heuristic lower bound estimate $h(m)$ of $v(m)$, then it induces a heuristic evaluation function on the minimal cost extension of $T^{\prime}$. Given a partial solution tree $T_{n}^{\prime}$ rooted at $n$ in the AND/OR graph $\mathcal{C}_{\mathcal{T}}(\mathcal{R})$, the tree-based heuristic evaluation function $f\left(T_{n}^{\prime}\right)$, is defined recursively by:

1. If $T_{n}^{\prime}$ consists of a single node $n$, then $f\left(T_{n}^{\prime}\right)=h(n)$.
2. If $n$ is an OR node having the AND child $m$ in $T_{n}^{\prime}$, then $f\left(T_{n}^{\prime}\right)=w(n, m)+$ $f\left(T_{m}^{\prime}\right)$.
3. If $n$ is an AND node having OR children $m_{1}, \ldots, m_{k}$ in $T_{n}^{\prime}$, then $f\left(T_{n}^{\prime}\right)=$ $\sum_{i=1}^{k} f\left(T_{m_{i}}^{\prime}\right)$.

Clearly, by definition, $f\left(T_{n}^{\prime}\right) \leq f^{*}\left(T_{n}^{\prime}\right)$, and if $n$ is the root of the context minimal AND/OR search graph, then $f\left(T^{\prime}\right) \leq f^{*}\left(T^{\prime}\right)[1]$.

During search, the algorithm maintains both an upper bound $u b(s)$ on the optimal solution $v(s)$ as well as the heuristic evaluation function $f\left(T^{\prime}\right)$ of the current partial solution tree $T^{\prime}$ being explored, and whenever $f\left(T^{\prime}\right) \geq u b(s)$, searching below the current tip node $t$ of $T^{\prime}$ is guaranteed not to yield a better solution cost than $u b(s)$ and therefore, search below $t$ can be terminated.

```
Algorithm 1: AOBB-C: AND/OR Branch-and-Bound Graph Search
Input: An optimization problem \(\mathcal{P}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}, \sum_{s} \min \rangle\), pseudo-tree \(\mathcal{T}\) rooted at \(X_{1}\), parent separator sets \(\operatorname{pas}_{i}\)
    (AND-context) for every variable \(X_{i}\), heuristic function \(h(n)\).
Output: Minimal cost solution and an optimal solution assignment.
1 create an OR node \(s\) labeled \(X_{1} \quad / /\) Create and initialize the root node
2 \(v(s) \leftarrow \infty ; S T(s) \leftarrow \emptyset ; O P E N \leftarrow\{s\}\)
3 Initialize cache tables with entries "NULL"
// Initialize cache tables
4 while \(O P E N \neq \emptyset\) do
    \(n \leftarrow \operatorname{top}(O P E N) ;\) remove \(n\) from \(O P E N \quad / /\) EXPAND
5 if \(n\) is an OR node, labeled \(X_{i}\) then
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
```

else if $n$ is an $A N D$ node, labeled $\left\langle X_{i}, x_{i}\right\rangle$ then
cached $\leftarrow$ false; deadend $\leftarrow$ false
if Cache $\left(\right.$ asgn $\left.\left(\pi_{n}\right)\left[\right.$ pas $\left._{i}\right]\right) \neq$ NULL then
$v(n) \leftarrow \operatorname{Cache}\left(\right.$ asgn $\left.\left(\pi_{n}\right)\left[p a s_{i}\right]\right)$.value
// Retrieve value
$S T(n) \leftarrow \operatorname{Cache}\left(\operatorname{asg}\left(\pi_{n}\right)\left[\right.\right.$ pas $\left._{i}\right]$ ).assignment;
cached $\leftarrow$ true
// No need to expand below
foreach $O R$ ancestor $m$ of $n$ do
$f\left(T_{m}^{\prime}\right) \leftarrow$ evalPartialSolutionTree $\left(T_{m}^{\prime}\right)$
if $f\left(T_{m}^{\prime}\right) \geq v(m)$ then
deadend $\leftarrow$ true
break
if deadend $==$ false and cached $==$ false then
foreach $X_{j} \in$ children $\left.\gamma\left(X_{i}\right)\right.$ do
create an OR node $n^{\prime}$ labeled $X_{j}$
$v\left(n^{\prime}\right) \leftarrow \infty ; S T\left(n^{\prime}\right) \leftarrow \emptyset$
$\operatorname{succ}(n) \leftarrow \operatorname{succ}(n) \cup\left\{n^{\prime}\right\}$
else if deadend $==$ true then
$\operatorname{succ}(p) \leftarrow \operatorname{succ}(p)-\{n\}$
Add $\operatorname{succ}(n)$ on top of $O P E N$
while $\operatorname{succ}(n)==\emptyset$ do
if $n$ is an OR node, labeled $X_{i}$ then
if $X_{i}==X_{1}$ then
return $(v(n), S T(n))$
// Search is complete
$v(p) \leftarrow v(p)+v(n) \quad$// Update AND node value (summation)
$S T(p) \leftarrow S T(p) \cup S T(n) \quad$// Update solution tree below AND node
else if $n$ is an $A N D$ node, labeled $\left\langle X_{i}, x_{i}\right\rangle$ then
$\operatorname{Cache}\left(\operatorname{asgn}\left(\pi_{n}\right)\left[\operatorname{pas}_{i}\right]\right)$.value $\leftarrow v(n) \quad$// Save AND node value in cache Cache $\left(\operatorname{asgn}\left(\pi_{n}\right)\left[\right.\right.$ pas $\left._{i}\right]$ ).assignment $\leftarrow S T(n) ; \quad / /$ Save optimal assignment if $v(p)>(w(p, n)+v(n))$ then
$v(p) \leftarrow w(p, n)+v(n) \quad$// Update OR node value (minimization)
$S T(p) \leftarrow S T(n) \cup\left\{\left(X_{i}, x_{i}\right)\right\} \quad / /$ Update solution tree below OR node
remove $n$ from $\operatorname{succ}(p)$
$n \leftarrow p$

In [1] we also showed that the pruning test can be sped up if we associate upper bounds with internal nodes as well. Specifically, if $m$ is an OR ancestor of $t$ in $T^{\prime}$ and $T_{m}^{\prime}$ is the subtree of $T^{\prime}$ rooted at $m$, then it is also safe to prune the search tree below $t$, if $f\left(T_{m}^{\prime}\right) \geq u b(m)$. For illustration, see also Section 6 in [1].

```
Algorithm 2: Recursive computation of the heuristic evaluation function.
function: evalPartialSolutionTree \(\left(T_{n}^{\prime}, h(n)\right)\)
Input: Partial solution subtree \(T_{n}^{\prime}\) rooted at node \(n\), heuristic function \(h(n)\).
Output: Heuristic evaluation function \(f\left(T_{n}^{\prime}\right)\).
if \(\operatorname{succ}(n)==\emptyset\) then
        return \(h(n)\)
    else
        if \(n\) is an \(A N D\) node then
            let \(m_{1}, \ldots, m_{k}\) be the OR children of \(n\) in \(T_{n}^{\prime}\)
            return \(\sum_{i=1}^{k} \operatorname{evalPartialSolutionTree}\left(T_{m_{i}}^{\prime}, h\left(m_{i}\right)\right)\)
    else if \(n\) is an \(O R\) node then
            let \(m\) be the AND child of \(n\) in \(T_{n}^{\prime}\)
            return \(w(n, m)+\) evalPartialSolutionTree \(\left(T_{m}^{\prime}, h\left(m_{i}\right)\right)\)
```

The Depth-First AND/OR Branch-and-Bound algorithm, AOBB-C, for searching AND/OR graphs for graphical models, is described by Algorithm 1. It interleaves a forward expansion step of the current partial solution tree (EXPAND) with a backward propagation step (PROPAGATE) that updates the node values. This part is identical to the tree-based variant [1] and we describe it here for completeness.

The context-based caching uses a table representation. For each variable $X_{i}$, a table is reserved in memory for each possible assignment to its parent-separator set $p a s_{i}$ (i.e., AND context). During search, each table entry records the optimal solution (both the cost and an optimal solution tree) to the subproblem below the corresponding AND node. Initially, each entry has a predefined value, in our case NULL. The fringe of the search is maintained by a stack called OPEN. The current node is denoted by $n$, its parent by $p$, and the current path by $\pi_{n}$. The children of the current node are denoted by $\operatorname{succ}(n)$.

Each node $n$ in the search graph maintains its current value $v(n)$, which is updated based on the values of its children. For OR nodes, the current $v(n)$ is an upper bound on the optimal solution cost below $n$. Initially, $v(n)$ is set to $\infty$ if $n$ is OR, and 0 if $n$ is AND, respectively. A data structure $S T(n)$ maintains the actual best solution tree found in the subgraph rooted at $n$. The node based heuristic function $h(n)$ of $v(n)$ is assumed to be available to the algorithm, either retrieved from a cache or computed during search.

Since we use AND caching, before expanding the current AND node $n$, its cache table is checked (line 14). If the same context was encountered before, it is retrieved from the cache, and $\operatorname{succ}(n)$ is set to the empty set, which will trigger the PROPAGATE step. The algorithm also computes the heuristic evaluation function for every partial solution subtree rooted at the OR ancestors of $n$ along the path from the root (lines 18-22). The search below $n$ is terminated if, for some OR ancestor $m, f\left(T_{m}^{\prime}\right) \geq v(m)$, where $v(m)$ is the current upper bound on the optimal cost below $m$. The recursive computation of $f\left(T_{m}^{\prime}\right)$ is described in Algorithm 2.

If a node is not found in cache, it is expanded in the usual way, depending on whether it is an AND or OR node (lines 6-29). If $n$ is an OR node, labeled $X_{i}$,

then its successors are AND nodes represented by the values $x_{i}$ in variable $X_{i}$ 's domain (lines 6-11). Each OR-to-AND arc is associated with the appropriate weight. Similarly, if $n$ is an AND node, labeled $\left\langle X_{i}, x_{i}\right\rangle$, then its successors are OR nodes labeled by the child variables of $X_{i}$ in $\mathcal{T}$ (lines 23-27). There are no weights associated with AND-to-OR arcs.

The node values are updated by the PROPAGATE step (lines 31-44). It is triggered when a node value has an empty set of descendants (note that as each successor is evaluated, it is removed from the set of successors in line 43). This means that all its children have been evaluated, and their final values are already determined. If the current node is the root, then the search terminates with its value and an optimal solution tree (line 34). If $n$ is an OR node, then its parent $p$ is an AND node, and $p$ updates its current value $v(p)$ by summation with the value of $n$ (line 35). An AND node $n$ propagates its value to its parent $p$ in a similar way, by minimization (lines 37-42). It also saves in cache the value and optimal solution subtree below it (lines 38-39). Finally, the current node $n$ is set to its parent $p$ (line 44), because $n$ was completely evaluated. Each node in the search graph also records the current best assignment to the variables of the subproblem below it. Specifically, if $n$ is an AND node, then $S T(n)$ is the union of the optimal trees propagated from $n$ 's OR children (line 36). Alternatively, if $n$ is an OR node and $n^{\prime}$ is its AND child such that $n^{\prime}=\operatorname{argmin}_{m \in \operatorname{succ}(n)}(w(n, m)+v(m))$, then $S T(n)$ is obtained from the label of $n^{\prime}$ combined with the optimal solution tree below $n^{\prime}$ (line 42). Search continues either with a propagation step (if conditions are met) or with an expansion step. Clearly, since the size of the context minimal AND/OR search graph is bounded exponentially by the induced width of the primal graph, it follows that:

THEOREM 3 (complexity) AOB B-C traversing the context minimal AND/OR search graph relative to a pseudo tree $\mathcal{T}$ is sound and complete. Its time and space complexity is $O\left(n \cdot k^{w^{*}}\right)$, where $w^{*}$ is the induced width of the pseudo tree and $k$ bounds the domain size.

The space required by AOB B-C can sometimes be prohibitive. We next present two caching schemes that can adapt to the memory limitations. They use a parameter called cache bound (or simply $j$-bound) to control the amount of memory used for storing identical nodes.

# 4.1 Naive Caching 

The first scheme, called naive caching and denoted by $\mathrm{AOBB}-\mathrm{C}(j)$, stores nodes at the variables whose context size is smaller than or equal to the cache bound $j$. It is easy to see that, when $j$ equals the induced width of the pseudo tree, the algorithm explores the context minimal AND/OR graph via full caching.

As we mentioned earlier, a straightforward way of implementing the caching scheme

![img-1.jpeg](img-1.jpeg)

Fig. 2. An example of a primal graph and its pseudo tree.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of naive caching used by AOBB-C (2) on the problem from Fig. 2.
is to have a cache table for each variable $X_{k}$ recording the context. Specifically, lets assume that the context of $X_{k}$ is context $\left(X_{k}\right)=\left\{X_{1}, \ldots, X_{k}\right\}$ and $\mid$ context $\left(X_{k}\right) \mid \leq$ $j$. A cache table entry corresponds to a particular instantiation $\left\{x_{1}, \ldots, x_{k}\right\}$ of the variables in context $\left(X_{k}\right)$ and records the minimal cost solution to the subproblem rooted at the AND node labeled $\left\langle X_{k}, x_{k}\right\rangle$.

However, some tables might never get cache hits. These dead-caches [6,18] appear at nodes that have only one incoming arc in the context minimal graph. $\mathrm{AOBB}-\mathrm{C}(j)$ needs to record only nodes that are likely to have additional incoming arcs, and some of these nodes can be determined by inspecting the pseudo tree (for example, when the context of a node does not include that of its parent).

Example 2 Figure 3 displays the AND/OR search graph obtained with the naive caching scheme $A O B B-C$ (2), relative to the pseudo tree given in Figure 2(b). Notice that there is no need to create cache tables for variables $H$ and $B$, because their $A N D$ contexts include those of their respective parents in the pseudo tree, namely

![img-3.jpeg](img-3.jpeg)

Fig. 4. Illustration of adaptive caching used by AOBB-AC (2) on the problem from Fig. 2. $\operatorname{context}(A) \subseteq \operatorname{context}(H) \subseteq \operatorname{context}(B)$, respectively. Moreover, $A O B B-C$ (2) does not cache any of the AND nodes corresponding to variable $C$ because its corresponding cache table, which is defined on 3 variables (e.g., $A, B$ and $C$ ), cannot be stored in memory.

# 4.2 Adaptive Caching 

The second scheme, called adaptive caching and denoted by $\operatorname{AOBB}-\mathrm{AC}(j)$, is inspired by the AND/OR cutset conditioning scheme and was first explored in [23]. It extends the naive scheme by allowing caching even at nodes with contexts larger than the given cache bound, based on adjusted contexts.

Specifically, consider the node $X_{k}$ in the pseudo tree $\mathcal{T}$ with $\operatorname{context}\left(X_{k}\right)=$ $\left\{X_{1}, \ldots, X_{k}\right\}$, where $k>j$. During search, when variables $\left\{X_{1}, \ldots, X_{k-j}\right\}$ are instantiated, they can be viewed as part of a cutset. The problem rooted by $X_{k-j+1}$ can be solved in isolation, like a subproblem in the cutset scheme, after variables $X_{1}, \ldots, X_{k-j}$ are assigned their current values in all the functions. In this subproblem, conditioned on the values $\left\{x_{1}, \ldots, x_{k-j}\right\}, \operatorname{context}\left(X_{k}\right)=\left\{X_{k-j+1}, \ldots, X_{k}\right\}$ (we call this the adjusted context of $X_{k}$ ), so it can be cached within $j$-bounded space. However, when $\operatorname{AOBB}-\mathrm{AC}(j)$ retracts to variable $X_{k-j}$ or above, the cache table for variable $X_{k}$ needs to be purged, and will be used again when a new subproblem rooted at $X_{k-j+1}$ is solved. This caching scheme requires only a linear increase in additional memory, compared to the naive $\operatorname{AOBB}-\mathrm{C}(j)$, but it has the potential of exponential time savings, as shown in [23].

Example 3 Figure 4 shows the AND/OR graph traversed using the adaptive caching

scheme $A O B B-A C$ (2). In contrast to the naive scheme displayed in Figure 3, $A O B B-A C$ (2) caches the AND level corresponding to variable $C$ based on its adjusted context. The adjusted AND context of $C$ is $\{C, B\}$ and a flag is installed at variable $A$, indicating that the cache table must be purged whenever $A$ is instantiated to a different value.

# 5 Best-First AND/OR Search 

We now direct our attention to a best-first control strategy for traversing the context minimal AND/OR graph. The best-first search algorithm uses similar amounts of memory as the depth-first AND/OR Branch-and-Bound with full caching and therefore the comparison is warranted.

Best-first search expands the nodes in order of their heuristic evaluation function. Its main virtue is that it never expands nodes whose cost is beyond the optimal one, unlike depth-first search algorithms, and therefore is superior among memory intensive algorithms employing the same heuristic evaluation function [9].

Best-First AND/OR search, denoted by AOBF-C, that traverses the context minimal AND/OR search graph is described in Algorithm 3. It specializes Nilsson's AO* algorithm [19] to AND/OR search spaces for graphical models and interleaves forward expansion of the best partial solution tree (EXPAND) with a cost revision step (REVISE) that updates node values, as detailed in [19]. The explicated AND/OR search graph is maintained by a data structure called $C_{T}^{\prime}$, the current node is $n, s$ is the root of the search graph and the current best partial solution subtree is denoted by $T^{\prime}$. The children of the current node are denoted by $\operatorname{succ}(n)$.

First, a top-down, graph-growing operation finds the best partial solution tree by tracing down through the marked arcs of the explicit AND/OR search graph $C_{T}^{\prime}$ (lines 4-10). These previously computed marks indicate the current best partial solution tree from each node in $C_{T}^{\prime}$. Before the algorithm terminates, the best partial solution tree, $T^{\prime}$, does not yet have all of its leaf nodes terminal. One of its nonterminal leaf nodes $n$ is then expanded by generating its successors, depending on whether it is an OR or an AND node. If $n$ is an OR node, labeled $X_{i}$, then its successors are AND nodes represented by the values $x_{i}$ in variable $X_{i}$ 's domain (lines 12-21). Notice that when expanding an OR node, the algorithm does not generate AND children that are already present in the explicit search graph $C_{T}^{\prime}$, but rather links to them. All these identical AND nodes in $C_{T}^{\prime}$ are easily recognized based on their contexts. Each OR-to-AND arc is associated with the appropriate weight (see Definition 6). Similarly, if $n$ is an AND node, labeled $\left\langle X_{i}, x_{i}\right\rangle$, then its successors are OR nodes labeled by the child variables of $X_{i}$ in $\mathcal{T}$ (lines 2226). There are no weights associated with AND-to-OR arcs. Moreover, a heuristic underestimate $h\left(n^{\prime}\right)$ of $v\left(n^{\prime}\right)$ is assigned to each of $n$ 's successors $n^{\prime} \in \operatorname{succ}(n)$.

```
Algorithm 3: AOBF-C: Best-First AND/OR Graph Search
Input: An optimization problem \(\mathcal{P}=\langle\mathbf{X}, \mathbf{D}, \mathbf{F}, \sum_{i} \min \rangle\), pseudo tree \(\mathcal{T}\) rooted at \(X_{1}\), parent separator sets \(\operatorname{pas}_{i}\)
    (AND-context) for every variable \(X_{i}\), heuristic function \(h(n)\).
Output: Minimal cost solution and an optimal solution assignment.
1 create an OR node \(s\) labeled \(X_{1} \quad / /\) Initialize
2 \(v(s) \leftarrow h(s) ; C_{T}^{\prime} \leftarrow\{s\}\)
3 while \(s\) is not labeled SOLVED do
    \(S \leftarrow\{s\} ; T^{\prime} \leftarrow\{ \} ; \quad / /\) Create the marked partial solution tree
    while \(S \neq \emptyset\) do
        \(n \leftarrow \operatorname{top}(S)\); remove \(n\) from \(S\)
        \(T^{\prime} \leftarrow T^{\prime} \cup\{n\}\)
        let \(L\) be the set of marked successors of \(n\)
        if \(L \neq \emptyset\) then
            add \(L\) on top of \(S\)
    let \(n\) be any nonterminal tip node of the marked \(T^{\prime}\) (rooted at \(s\) )
    if \(n\) is an OR node, labeled \(X_{i}\) then
        foreach \(x_{i} \in D_{i}\) do
            let \(n^{\prime}\) be the AND node in \(C_{T}^{\prime}\) having context equal to \(\operatorname{pas}_{i}\)
            if \(n^{\prime}==N U L L\) then
                create an AND node \(n^{\prime}\) labeled \(\left\langle X_{i}, x_{i}\right\rangle\)
                \(v\left(n^{\prime}\right) \leftarrow h\left(n^{\prime}\right)\)
                \(w\left(n, n^{\prime}\right) \leftarrow \sum_{f \in B_{T}\left(X_{i}\right)} f\left(\operatorname{asgn}\left(\pi_{n}\right)\right)\)
                if \(n^{\prime}\) is TERMINAL then
                    label \(n^{\prime}\) as SOLVED
            \(\operatorname{succ}(n) \leftarrow \operatorname{succ}(n) \cup\left\{n^{\prime}\right\}\)
    else if \(n\) is an AND node, labeled \(\left\langle X_{i}, x_{i}\right\rangle\) then
        foreach \(X_{j} \in \operatorname{children}_{T}\left(X_{i}\right)\) do
            create an OR node \(n^{\prime}\) labeled \(X_{j}\)
            \(v\left(n^{\prime}\right) \leftarrow h\left(n^{\prime}\right)\)
            \(\operatorname{succ}(n) \leftarrow \operatorname{succ}(n) \cup\left\{n^{\prime}\right\}\)
    \(C_{T}^{\prime} \leftarrow C_{T}^{\prime} \cup\{\operatorname{succ}(n)\}\)
    \(S \leftarrow\{n\} \quad / /\) REVISE
    while \(S \neq \emptyset\) do
        let \(m\) be a node in \(S\) such that \(m\) has no descendants in \(C_{T}^{\prime}\) still in \(S\); remove \(m\) from \(S\)
        if \(m\) is an AND node, labeled \(\left\langle X_{i}, x_{i}\right\rangle\) then
            \(v(m) \leftarrow \sum_{m_{j} \in \operatorname{succ}(m)} v\left(m_{j}\right)\)
            mark all arcs to the successors
            label \(m\) as SOLVED if all its children are labeled SOLVED
            else if \(m\) is an OR node, labeled \(X_{i}\) then
                \(v(m)=\min _{m_{j} \in \operatorname{succ}(m)}\left(w_{\left(m, m_{j}\right)}+v\left(m_{j}\right)\right)\)
                mark the arc through which this minimum is achieved
            label \(m\) as SOLVED if the marked successor is labeled SOLVED
            if \(m\) changes its value or \(m\) is labeled SOLVED then
                add to \(S\) all those parents of \(m\) such that \(m\) is one of their successors through a marked arc.
    return \(v(s) \quad / /\) Search terminates
```

The second operation in AOBF-C is a bottom-up, cost revision, arc marking, SOLVElabeling procedure (lines 28-40). It aims at updating the evaluation function of any subtree that might be affected, and marks the best one. Starting with the node just expanded $n$, the procedure revises its value $v(n)$, using the newly computed values of its successors, and marks the outgoing arcs on the estimated best path to terminal nodes. This revised value is then propagated upwards in the graph. The revised value $v(n)$ is an updated lower bound on the cost of an optimal solution to the subproblem rooted at $n$. If we assume the monotone restriction on $h$, cost revisions can

only be cost increases [24,19]. Therefore, not all ancestors need have cost revisions, but only those ancestors having best partial solution trees containing descendants with revised values (lines 39-40). During the bottom-up step, AOBF-C labels an AND node as SOLVED if all of its OR child nodes are solved, and labels an OR node as SOLVED if its marked AND child is also solved. The algorithm terminates with the optimal solution when the root node $s$ is labeled SOLVED.

If $h(n) \leq v(n)$, the exact cost at $n$, for all nodes, and if $h$ satisfies the monotone restriction, then algorithm AOBF-C will terminate with an optimal solution tree [24,19]. The optimal solution tree can be obtained by tracing down from $s$ through the marked connectors at termination and its optimal cost is equal to the value $v(s)$ of $s$ at termination. Since the algorithm explores every node in the context minimal graph just once, it is the case that:

THEOREM 4 (complexity) The best-first AND/OR search algorithm traversing the context minimal AND/OR graph has time and space complexity of $O\left(n \cdot k^{w^{*}}\right)$, where $w^{*}$ is the induced width of the pseudo tree and $k$ bounds the domain size.

AOBB versus AOBF. We highlight next the main differences between depth-first AND/OR Branch-and-Bound (AOBB-C) and best-first AND/OR search (AOBF-C) traversing the context minimal AND/OR search graph.

First, AOBF-C with the same heuristic function as AOBB-C is likely to expand the smallest number of nodes [9], but empirically this depends on how quickly AOBB-C will find an optimal solution that it will use as upper bound. Secondly, $A O B B-C$ can use far less memory by avoiding dead-caches for example (e.g., when the search graph is a tree), while AOBF-C has to keep the explicated search graph in memory. Third, $A O B B-C$ can be used as an anytime scheme, namely whenever interrupted, the algorithm outputs the best solution found so far, unlike AOBF-C which outputs a complete solution upon termination only. All the above points show that the relative merit of best-first versus depth-first over context minimal AND/OR search spaces cannot be determined by sheer theory [9] and therefore empirical evaluation is essential.

# 6 Overview of the Mini-Bucket Lower Bound Heuristics for AND/OR Search 

The effectiveness of both depth-first AND/OR Branch-and-Bound and best-first AND/OR search algorithms greatly depends on the quality of the heuristic evaluation functions. The primary heuristic that we used in our experiments is the Mini-Bucket heuristic, which we presented in [1,2]. For completeness, we review it briefly next.

Mini-Bucket Elimination $(\operatorname{MBE}(i))$ [11] is an approximation algorithm designed

to avoid the high time and space complexity of Bucket Elimination (BE) [25], by partitioning large buckets into smaller subsets, called mini-buckets, each containing at most $i$ (called $i$-bound) distinct variables. The mini-buckets are then processed separately. The algorithm outputs not only a bound on the optimal solution cost, but also a collection of augmented buckets, which form the basis for the heuristics generated. The complexity is time and space $O(\exp (i))$. Both Bucket and MiniBucket Elimination can also be viewed as message passing from leaves to root along a bucket tree [17].

Static Mini-Bucket Heuristics. In [1,2,10] we showed that the intermediate functions generated by MBE $(i)$ can be used to compute a heuristic function that underestimates the minimal cost solution to the current subproblem. Specifically, given an ordered set of augmented buckets $\left\{B\left(X_{1}\right), \ldots, B\left(X_{n}\right)\right\}$ generated by MBE $(i)$ along the bucket tree $\mathcal{T}$ (which is also a pseudo tree [18]), and given a node $n$ in the AND/OR search tree, the static mini-bucket heuristic function $h(n)$ is computed as follows: (1) if $n$ is an AND node labeled $\left\langle X_{p}, x_{p}\right\rangle$, then $h(n)$ is the sum of all intermediate functions that were generated in buckets corresponding to the descendents of $X_{p}$ in $\mathcal{T}$ and reside in bucket $B\left(X_{p}\right)$ or the buckets corresponding to the ancestors of $X_{p}$ in $\mathcal{T}$; (2) if $n$ is an OR node labeled by $X_{p}$, then $h(n)=\min _{m}(w(n, m)+h(m))$, where $m$ is the AND child of $n$ labeled with value $x_{p}$ of $X_{p}$.

Dynamic Mini-Bucket Heuristics. It is also possible to generate the mini-bucket heuristic information dynamically, during search. The idea is to compute MBE( $i$ ) conditioned on the current partial assignment [1,2]. Specifically, given a bucket tree $\mathcal{T}$, with buckets $\left\{B\left(X_{1}\right), \ldots, B\left(X_{n}\right)\right\}$, a node $n$ in the AND/OR search tree and given the current partial assignment $\operatorname{asgn}\left(\pi_{n}\right)$ along the path to $n$, the dynamic mini-bucket heuristic function $h(n)$ is computed as follows: (1) if $n$ is an AND node labeled $\left\langle X_{p}, x_{p}\right\rangle$, then $h(n)$ is the sum of the intermediate functions that reside in bucket $B\left(X_{p}\right)$ and were generated by MBE $(i)$, conditioned on $\operatorname{asgn}\left(\pi_{n}\right)$, in the buckets corresponding to the descendants of $X_{p}$ in $\mathcal{T}$; (2) if $n$ is an OR node labeled $X_{p}$, then $h(n)=\min _{m}(w(n, m)+h(m))$, where $m$ is the AND child of $n$ labeled with value $x_{p}$ of $X_{p}$. Given an $i$-bound, the dynamic mini-bucket heuristic implies a much higher computational overhead compared with the static version. However, the bounds generated dynamically may be far more accurate since some of the variables are assigned and will therefore yield smaller functions and less partitioning.

# 7 Experimental Results 

In [1,2] we evaluated empirically AND/OR search algorithms for AND/OR trees only. We now extend this evaluation to algorithms presented in this paper exploring the context minimal AND/OR search graphs. As in [1,2], we have conducted a num-

ber of experiments on the two common optimization problems classes in graphical models: finding the Most Probable Explanation in Bayesian networks and solving Weighted CSPs. We implemented our algorithms in C++ and ran all experiments on a 2.4 GHz Pentium IV with 2GB of RAM, running Windows XP.

# 7.1 Overview and Methodology 

Algorithms We evaluated the following classes of memory intensive AND/OR search algorithms:

- Depth-first AND/OR Branch-and-Bound search algorithms with full caching, using static and dynamic mini-bucket heuristics, denoted by AOBB-C+SMB (i) and AOBB-C+DMB (i), respectively.
- Best-first AND/OR search algorithms using static and dynamic mini-bucket heuristics, denoted by AOBF-C+SMB (i) and AOBF-C+DMB (i), respectively.

We compare these algorithms with those traversing the AND/OR search tree (without caching), denoted by AOBB+SMB (i) and AOBB+DMB (i), introduced in [1,2]. In addition, we also ran the traditional OR Branch-and-Bound search algorithms with full caching, denoted by $\mathrm{BB}-\mathrm{C}+\mathrm{SMB}(i)$ and $\mathrm{BB}-\mathrm{C}+\mathrm{DMB}(i)$, respectively. In all cases, the parameter $i$ represents the mini-bucket $i$-bound and controls the accuracy of the heuristic.

Throughout our empirical evaluation we will address the following aspects that govern the performance of the proposed algorithms:

1 The impact of graph versus tree on AND/OR Branch-and-Bound search.
2 The impact of best-first versus depth-first AND/OR search regimes.
3 The impact of the mini-bucket $i$-bound.
4 The impact of the cache bound $j$ on naive and adaptive caching.
5 The impact of the pseudo tree quality on AND/OR search.
6 The impact of determinism present in the network.
7 The impact of non-trivial initial upper bounds.

MPE Task for Bayesian Networks We tested the performance of the depthfirst AND/OR Branch-and-Bound and best-first AND/OR search algorithms on the following types of problems ${ }^{2}$ : random coding networks, grid networks, Bayesian networks derived from the ISCAS'89 digital circuits benchmark, genetic linkage analysis networks and Bayesian networks used in the UAI'06 Inference Evaluation contest. We report here in detail the results obtained for grid networks and genetic

[^0]
[^0]:    2 Available online at http://graphmod.ics.uci.edu/group/Repository

linkage analysis networks only, but we summarize the results over the entire set of benchmarks, and refer the reader to $[26,27]$ for additional details.

In our experiments, we also consider an extension of the AND/OR Branch-andBound with caching that exploits the determinism present in the Bayesian network by constraint propagation. For reference, we also compared with the SAMIAM version 2.3.2 software package ${ }^{3}$. SAMIAM contains an implementation of Recursive Conditioning [6] which can also be viewed as an AND/OR search algorithm. It uses a context-based caching mechanism similar to our scheme. This version of recursive conditioning also explores a context minimal AND/OR search graph [18] and therefore its space complexity is exponential in the treewidth. Note that when we use mini-bucket heuristics with high values of $i$, we use space exponential in $i$ for the heuristic calculation and storing, in addition to the space required for caching.

Weighted CSPs We evaluated the algorithms on: scheduling problems from the SPOT5 benchmark, networks derived from the ISCAS'89 digital circuits and instances of the popular game of Mastermind. We report here detailed results for SPOT5 problem instances and Mastermind game instances only. We also provide a summary of the results obtained on the other types of problems, and refer the reader to $[26,27]$ for the full results.

For reference, we also report results obtained with the state-of-the-art solvers called toolbar [28] and toolbar-BTD [29] ${ }^{4}$. toolbar is an OR Branch-and-Bound algorithm that maintains during search a form of soft local consistency called Existential Directional Arc Consistency (EDAC). toolbar-BTD extends the Backtracking with Tree Decomposition (BTD) algorithm [8] and computes the guiding heuristic information as well by enforcing EDAC during search. It can be shown that BTD explores a context minimal AND/OR search graph, relative to a pseudo tree corresponding to the given tree decomposition. In addition, we also compare with the depth-first AND/OR Branch-and-Bound tree search algorithms with EDAC heuristics and with variable orderings such as: AOEDAC+PVO using partial variable orderings, DVO+AOEDAC using full dynamic variable ordering, and AOEDAC+DSO using dynamic separator orderings, respectively. For a detailed description of these ordering heuristics and their evaluation, see [1,3].

The dynamic variable ordering heuristic used by the OR and AND/OR Branch-andBound algorithms with EDAC heuristics was the min-dom/ddeg heuristic, which selects the variable with the smallest ratio of the domain size divided by the future degree. Ties were broken lexicographically.

[^0]
[^0]:    ${ }^{3}$ Available at http://reasoning.cs.ucla.edu/samiam. We used the batchtool 1.5 provided with the package.
    4 Available at: http://carlit.toulouse.inra.fr/cgi-bin/awki.cgi/SoftCSP

Measures of Performance In all our experiments we report the CPU time in seconds and the number of nodes visited for solving the problems. We also specify the problems' parameters such as the number of variables $(n)$, number of evidence variables $(e)$, maximum domain size $(k)$, the induced width $\left(w^{*}\right)$ and depth $(h)$ of the pseudo trees. When evidence is asserted in the network, $w^{*}$ and $h$ are computed after the evidence nodes were removed from the graph. We also report the time required by the Mini-Bucket algorithm $\operatorname{MBE}(i)$ to pre-compile the heuristic information. The pseudo trees that guide the AND/OR search algorithms were generated using the min-fill and hypergraph partitioning heuristics described in [1,6]. In our experiments we ran the min-fill heuristic just once and broke the ties lexicographically. The best performance points are highlighted. In each table, "-" denotes that the respective algorithm exceeded the time limit. Similarly, "out" indicates that the 2GB memory limit was exceeded.

# 7.2 Results for Empirical Evaluation of Bayesian Networks 

Our results reported in [1] demonstrated conclusively that the AND/OR Branch-and-Bound tree search algorithms with static mini-bucket heuristics were the best performing algorithms on this domain when compared with traditional OR search algorithms. The difference between $A O B B+S M B(i)$ and the OR tree search counterpart $\mathrm{BB}+\mathrm{SMB}(i)$ was more pronounced at relatively small $i$-bounds (corresponding to relatively weak heuristic estimates) and amounted to two orders of magnitude in terms of both running time and size of the search space explored. For larger $i$-bounds, when the heuristic estimates are strong enough to prune the search space substantially, the difference between AND/OR and OR Branch-and-Bound tree search decreased. We also showed that $A O B B+S M B(i)$ was in many cases able to outperform dramatically the current state-of-the-art solvers for belief networks such as SAMIAM and SUPERLINK (for genetic linkage analysis). The AND/OR Branch-and-Bound with dynamic mini-bucket heuristics AOBB+DMB (i) proved competitive only for relatively small $i$-bounds due to the computational overhead. In this section we extend the empirical evaluation to memory intensive depth-first and best-first AND/OR search algorithms.

### 7.2.1 Grid Networks

In random grid networks, the nodes are arranged in an $N \times N$ square and each CPT is generated uniformly randomly. We experimented with problem instances initially developed by [30] for the task of weighted model counting. For these problems $N$ ranges between 10 and 38, and, for each instance, $90 \%$ of the CPTs are deterministic, namely they contain only 0 and 1 probability entries. All the variables are bi-valued.

Table 1
CPU time in seconds and nodes visited for solving grid networks using static mini-bucket heuristics and min-fill based pseudo trees. Time limit 1 hour. The two horizontal blocks of the table show different ranges of the mini-bucket $i$-bounds.


Table 2
CPU time in seconds and nodes visited for solving grid networks using dynamic minibucket heuristics and min-fill based pseudo trees. Time limit 1 hour. The two horizontal blocks of the table show different ranges of the mini-bucket $i$-bounds. Grid instances $\mathbf{9 0 -}$ 30-1. 90-34-1 and 90-38-1 could not be solved within the time limit.


Tables 1 and 2 show detailed results for experiments with 8 grids of increasing difficulty, using static and dynamic mini-bucket heuristics. The columns are indexed by the mini-bucket $i$-bound. Each table is organized into two horizontal blocks, each corresponding to a different range of $i$-bound values. For each instance we ran a single MPE query with $e$ nodes picked randomly and instantiated as evidence. The guiding pseudo trees were generated using the min-fill heuristic.

Tree vs. graph AOBB. First, we observe that $A O B B-C+S M B(i)$ using full caching improves significantly over the tree version of the algorithm, especially for relatively small $i$-bounds which generate relatively weak heuristic estimates. For example, on the 90-16-1 grid in Table 1, $A O B B-C+S M B(8)$ is 3 times faster than $A O B B+S M B(8)$ and explores a search space 5 times smaller. Notice also the significant additional reduction produced by the best-first search algorithm AOBF-C+SMB (8). While overall AOBF-C+SMB ( $i$ ) is superior to $A O B B-C+S M B(i)$ with the same $i$ bound, the best performance on this network is obtained by $A O B B-C+S M B(16)$.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparison of the impact of static and dynamic mini-bucket heuristics. Shown are the CPU time in seconds (a) and the number of nodes visited (b) on the 90-14-1 grid network from Tables 1 and 2, respectively.

The algorithm is two times faster than the cache-less $A O B B+S M B$ (16), and 155 times faster than SAMIAM, respectively. When looking at the algorithms using dynamic mini-bucket heuristics (Table 2) we observe a similar pattern, namely the graph search AND/OR Branch-and-Bound algorithm improves sometimes significantly over the tree search one. For instance, on the 90-24-1 grid, AOBB-C+DMB (16) is about two times faster than $A O B B+D M B(16)$. Notice also that the AND/OR algorithms with dynamic mini-buckets could not solve the last 3 test instances due to exceeding the time limit. The OR Branch-and-Bound search algorithms with caching $\mathrm{BB}-\mathrm{C}+\mathrm{SMB}(i)$ (resp. $\mathrm{BB}-\mathrm{C}+\mathrm{DMB}(i)$ ) are inferior to the AND/OR Branch-and-Bound graph search, especially on the harder instances (e.g., 90-30-1).

AOBF vs. AOBB. When comparing further the best-first and depth-first search algorithms, we see again the superiority of $\mathrm{AOBF}-\mathrm{C}+\mathrm{SMB}(i)$ over $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$, especially for relatively weak heuristic estimates (see also Figure 5). For example, on the 90-38-1 grid, one of the hardest instances, best-first search with the smallest reported $i$-bound $(i=12)$ is 9 times faster than $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(12)$ and visits 15 times less nodes. The difference between best-first and depth-first search is not too prominent when using dynamic mini-bucket heuristics, perhaps because these heuristics are far more accurate than the pre-compiled ones yielding a small enough search space.

Static vs. dynamic mini-bucket heuristics. When comparing the static versus dynamic mini-bucket heuristics, we see as before, that the former are more powerful for relatively large $i$-bounds, whereas the latter are cost effective only for relatively small $i$-bounds. Figures 5(a) and 5(b) plot the CPU time and size of the search space explored, as a function of the mini-bucket $i$-bound, on the 90-14-1 grid from Tables 1 and 2, respectively. Focusing on $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$, for example, we see that its running time, as a function of $i$, forms a U-shaped curve. At first $(i=4)$ it is high, then as the $i$-bound increases the total time decreases (when $i=14$ the time is 0.23 ), but then as $i$ increases further the time starts to increase again because the

![img-5.jpeg](img-5.jpeg)

Fig. 6. Naive versus adaptive caching schemes for AND/OR Branch-and-Bound with static mini-bucket heuristics on grid networks. Shown is the CPU time in seconds.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Min-fill versus hypergraph partitioning heuristics. CPU time in seconds for solving grid networks with $A O B B-C+S M B(i)$ (left) and $A O B F-C+S M B(i)$ (right). The header of each plot records the average induced width $\left(w^{*}\right)$ and pseudo tree depth (h) obtained with the hypergraph partitioning heuristic. We also show the induced width and pseudo tree depth for the min-fill heuristic.
pre-processing time of the mini-bucket heuristic outweighs the search time. The same behavior can be observed in the case of dynamic mini-buckets as well.

Impact of the caching level. Figure 6 compares the naive (AOBB-C+SMB $(i, j)$ ) and adaptive (AOBB-AC+SMB $(i, j)$ ) caching schemes, in terms of CPU time, on two grid networks from Table 1. In each test case we chose a relatively small mini-

![img-7.jpeg](img-7.jpeg)

Fig. 8. Memory usage by $A O B B-C+S M B(i)$ and $A O B F-C+S M B(i)$ on grid networks.
bucket $i$-bound and varied the cache bound $j$ (the X axis) from 2 to 20 . We see that adaptive caching improves significantly over the naive scheme especially for relatively small $j$-bounds. This may be important because small $j$-bounds mean restricted space. For large $j$-bounds the two schemes are identical and approach full caching.

Impact of the pseudo tree. Since the hypergraph partitioning heuristic uses a nondeterministic algorithm, the runtime of the AND/OR search algorithms guided by the resulting pseudo trees may vary significantly from one run to the next. In Figure 7 we display the running time distribution of $A O B B-C+S M B(i)$ (left side of the figure) and $A O B F-C+S M B(i)$ (right side of the figure) using hypergraph based pseudo trees on grids $90-24-1$ and $90-26-1$, respectively. For each reported $i$-bound (the X axis), the corresponding data point and error bar represent the average as well as the minimum and maximum running times obtained over 20 independent runs. We also record the average induced width and depth obtained for the hypergraph pseudo trees (see the header of each plot in Figure 7). We see that the hypergraph based pseudo trees, which have far smaller depths, are sometimes able to improve the performance of $A O B B-C+S M B(i)$, especially for relatively small $i$-bounds (e.g., 90-24-1). For larger $i$-bounds, the pre-compiled mini-bucket heuristic benefits from the small induced widths obtained with the min-fill ordering. Therefore, $A O B B-C+S M B(i)$ using min-fill based pseudo trees is generally faster (see the different Y scale). We also see that on average $A O B F-C+S M B(i)$ is faster when it is guided by min-fill rather than hypergraph based pseudo trees. This verifies our hypothesis that memory intensive algorithms exploring the AND/OR graph are more sensitive to the context size (which is smaller for min-fill orderings), rather than the depth of the pseudo tree. These results were typical to other instances as well.

Memory usage of AND/OR graph search. Figure 8 displays the memory usage of $A O B B-C+S M B(i)$ and $A O B F-C+S M B(i)$ on grids $90-30-1$ and $90-38-1$, respectively. We see that the memory requirements of the depth-first algorithm are significantly smaller than those of best-first search. This is because $A O B F-C+S M B(i)$ has to keep in memory the entire search space, unlike $A O B B-C+S M B(i)$ which can

Table 3
CPU time and nodes visited for solving genetic linkage networks using static minibucket heuristics. Time limit 3 hours. Top part of the table shows results for $i$-bounds between 6 and 14, while the bottom part shows $i$-bounds between 10 and 18.


save space by avoiding dead-caches for example. Moreover, the nodes cached by $A O B B-C+S M B(i)$ require far less memory because they only record the optimal solution cost below them, whereas the nodes cached by AOBF-C+SMB (i) must store, in addition, the lists of their children in the search graph. For these reasons, we were able throughout the evaluation to run full caching with depth-first search.

# 7.2.2 Genetic Linkage Analysis 

In human genetic linkage analysis [31], the haplotype is the sequence of alleles at different loci inherited by an individual from one parent, and the two haplo-

Table 4
CPU time in seconds and nodes visited for solving genetic linkage networks using static mini-bucket heuristics and min-fill based pseudo trees. Time limit 3 hours.


types (maternal and paternal) of an individual constitute this individual's genotype. When genotypes are measured by standard procedures, the result is a list of unordered pairs of alleles, one pair for each locus. The maximum likelihood haplotype problem consists of finding a joint haplotype configuration for all members of the pedigree which maximizes the probability of data. It can be shown that given the pedigree data, the haplotyping problem is equivalent to computing the most probable explanation of a Bayesian network that represents the pedigree [32,33].

Tables 3 and 4 display the results obtained for 12 hard linkage analysis networks ${ }^{5}$. We report only on search guided by static mini-bucket heuristics. The dynamic mini-bucket heuristics performed very poorly on this domain because of their prohibitively high computational overhead at large $i$-bounds. For comparison, we include results obtained with SUPERLINK 1.6. SUPERLINK is currently one the most efficient solvers for genetic linkage analysis, is dedicated to this domain, uses a combination of variable elimination and conditioning, and takes advantage of the determinism in the network.

Tree versus graph AOBB. We observe that $A O B B-C+S M B(i)$ improves significantly over $A O B B+S M B(i)$, especially for relatively small $i$-bounds for which the heuristic estimates are less accurate. On ped25, for example, $A O B B-C+S M B$ (18) is 15 times faster than $A O B B+S M B$ (18) and expands about 20 times fewer nodes. As the $i$-bound increases the difference between $A O B B-C+S M B(i)$ and $A O B B+S M B(i)$ decreases, as we saw before. Notice that the OR Branch-and-Bound with caching $\mathrm{BB}-\mathrm{C}+\mathrm{SMB}(i)$ and SAMIAM were able to solve only one instance (e.g., ped18).

AOBB vs. AOBF. The overall best performing algorithm on this dataset is bestfirst AOBF-C+SMB ( $i$ ), outperforming its competitors on 5 out of the 7 test cases. On ped42, for instance, AOBF-C+SMB (16) is 18 times faster than the depthfirst Branch-and-Bound AOBB-C+SMB (16) and explores a search space 240 times smaller. In some test cases (e.g., ped30) the best-first search algorithm was up to 3 orders of magnitude faster than SUPERLINK.

Impact of the pseudo tree. Figure 9 plots the running time distribution of depthfirst $A O B B-C+S M B(i)$ (left side of the figure) and best-first $A O B F-C+S M B(i)$ (right side of the figure), guided by hypergraph based pseudo trees, over 20 independent runs on the ped1 and ped33 networks, respectively. In this case, we see that both algorithms perform much better when guided by hypergraph based pseudo trees, especially on harder instances. For instance, on the ped33 network, $A O B B-C+S M B(16)$ using a hypergraph based pseudo tree was able to outperform $A O B B-C+S M B(16)$ guided by a min-fill tree by almost two orders of magnitude. Similarly, AOBF-C+SMB ( $i$ ) with hypergraph trees was able to solve the problem instance across all $i$-bounds, unlike $A O B B-C+S M B(i)$ with a min-fill tree which succeeded only for $i \in\{14,18\}$. Notice that the induced width of this problem along the min-fill order is very large $\left(w^{*}=37\right)$ which causes the mini-bucket heuristics to be relatively weak and implies a large number of dead caches. The results on other problem instances displayed a similar pattern.

Table 5 displays the results obtained for 6 additional linkage analysis networks using hypergraph partitioning based pseudo trees and the min-fill ones. We selected the hypergraph tree having the smallest depth over 100 independent runs. To the best of our knowledge, these networks were never before solved for the maximum

[^0]
[^0]:    ${ }^{5}$ http://bioinfo.cs.technion.ac.il/superlink/

![img-8.jpeg](img-8.jpeg)

Fig. 9. Min-fill versus hypergraph partitioning heuristics. CPU time in seconds for solving genetic linkage networks with $A O B B-C+S M B(i)$ (left side) and $A O B F-C+S M B(i)$ (right side). The header of each plot records the average induced width $\left(w^{*}\right)$ and pseudo tree depth (h) obtained with the hypergraph partitioning heuristic. We also show the induced width and pseudo tree depth for the min-fill heuristic.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Naive versus adaptive caching schemes for AND/OR Branch-and-Bound with static mini-bucket heuristics on genetic linkage networks. Shown is CPU time in seconds.
likelihood haplotype task. We see that the hypergraph pseudo trees offer the overall best performance as well. This can be explained by the large induced width which in this case renders most of the cache entries dead (see for instance that the difference between $A O B B+S M B(i)$ and $A O B B-C+S M B(i)$ is not too prominent). Therefore, the AND/OR graph explored effectively is very close to a tree and the dominant factor that impacts the search performance is then the depth of the guiding

Table 5
Impact of the pseudo tree quality on genetic linkage networks. Time limit 24 hours. We show results for the hypergraph partitioning heuristic (left) and the min-fill heuristic (right).


pseudo tree, which is far smaller for hypergraph trees compared with min-fill based ones. Notice also that best-first search could not solve any of these networks due to memory issues. The AND/OR Branch-and-Bound algorithms with min-fill based pseudo trees could only solve two of the test instances (e.g., ped9 and ped44) whose induced widths were small enough. These experiments demonstrate that the selection of the pseudo tree can have an enormous impact, especially if the $i$-bound that can be afforded is not large enough.

Impact of the caching level. Figure 10 plots the CPU time, as a function of the cache bound $j$, for two linkage networks using $A O B B-C+S M B(i, j)$ (naive caching) and $A O B B-A C+S M B(i, j)$ (adaptive caching), respectively. In each test case we varied the cache bound $j$ (the X axis) from 2 to 20 , and fixed the minibucket $i$-bound to a relatively small value. We see again that adaptive caching is more powerful than the naive scheme especially, for relatively small $j$-bounds,

![img-10.jpeg](img-10.jpeg)

Fig. 11. Anytime behavior of $A O B B-C+S M B(i)$ on ped42 and ped50 linkage networks. Number of flips for GLS is 50,000 . GLS running time is less than 1 second.
which require restricted space. As the $j$-bound increases, the two schemes approach gradually full caching.

# 7.2.3 The Anytime Behavior of AND/OR Branch-and-Bound Search and the Impact of Good Initial Bounds 

As mentioned earlier, the virtue of AND/OR Branch-and-Bound search is that, unlike best-first AND/OR search, it is an anytime algorithm. Namely, whenever interrupted, $A O B B-C$ outputs the best solution found far, which yields a lower bound on the most probable explanation. On the other hand, AOBF-C outputs a complete solution only upon termination. In this section we evaluate the anytime behavior of $A O B B-C+S M B(i)$. We compare it against the state-of-the-art local search algorithm for Bayesian MPE, called Guided Local Search (GLS) first introduced in [34], and improved more recently by [35].

GLS [36] is a penalty-based meta-heuristic, which works by augmenting the objective function of a local search algorithm (e.g. hill climbing) with penalties, to help guide them out of local minima. GLS has been shown to be successful in solving a number of practical real life problems, such as the traveling salesman problem, radio link frequency assignment problem and vehicle routing. It was also applied to the MPE task $[34,35]$ as well as weighted MAX-SAT problems [37].

In addition to comparing against GLS, we also considered a hybrid of AOBB with GLS, as follows. The AND/OR Branch-and-Bound algorithms assumed a trivial initial lower bound (i.e., 0 ), which effectively guarantees that the MPE will be computed, however it provides limited pruning. We therefore extended $A O B B-C+S M B(i)$ to exploit a non-trivial initial lower bound computed by GLS. The algorithm is denoted by $A O B B-C+G L S+S M B(i)$. For comparison, we also ran the OR version of the algorithm, denoted by $B B-C+G L S+S M B(i)$

Figure 11 displays the search trace of the OR and AND/OR algorithms on two genetic linkage networks presented earlier in Tables 3 and 4, respectively. We chose

Table 6
CPU time and nodes visited for solving genetic linkage analysis networks with static mini-bucket heuristics. Number of flips for GLS was set to 250,000. Time limit 3 hours.


the mini-bucket $i$-bound that offered the best performance and show the first 50 seconds of the search. We ran GLS for a fixed number of flips. We see that including the GLS lower bound in AND/OR Branch-and-Bound improves performance throughout. In all these test cases, the initial lower bound was in fact the optimal solution (we did not plot the GLS running time because it was less than 1 second). Therefore, AOBB-C+GLS+SMB (i) and BB-C+GLS+SMB (i) were able to output the optimal solution quite early in the search, unlike AOBB-C+SMB (i) and BB-C+SMB (i). For instance, on the ped50 network, AOBB-C+GLS+SMB (12) and BB-C+GLS+SMB (12) found the optimal solution within the first second of search. AOBB-C+SMB (12), on the other hand, finds the optimal solution after 8 seconds, whereas BB-C+SMB (12) reaches a flat (suboptimal) region after 18 seconds. In this case, AOBF-C+SMB (12) finds the optimal solution after 25 seconds. The same behavior was observed on other instances as well.

Table 6 compares the OR and AND/OR search algorithms with and without an initial lower bound, as complete algorithms. Algorithms AOBB-C+GLS+SMB (i) and

Table 7
CPU time and nodes visited for solving deterministic grid networks with static minibucket heuristics. Number of flips for GLS was set to 100,000. Time limit 1 hour.


$\mathrm{BB}-\mathrm{C}+\mathrm{GLS}+\mathrm{SMB}(i)$ do not include the GLS time, because GLS can be tuned independently for each problem instance to minimize its running time, so we report its time separately (as before, GLS ran for a fixed number of flips). The "*" by the GLS running time indicates that it found the optimal solution to the respective problem instance. We see that $\mathrm{BB}-\mathrm{C}+\mathrm{GLS}+\mathrm{SMB}(i)$ and $\mathrm{AOBB}-\mathrm{C}+\mathrm{GLS}+\mathrm{SMB}(i)$ are sometimes able to improve significantly over $\mathrm{BB}-\mathrm{C}+\mathrm{SMB}(i)$ and $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$, especially at relatively small $i$-bounds. For example, on the ped37 linkage instance, AOBB-C+GLS+SMB (12) achieves almost an order of magnitude speedup over AOBB-C+SMB (12). Similarly, BB-C+GLS+SMB (12) finds the optimal solution to ped37 in about 35 minutes, whereas $\mathrm{BB}-\mathrm{C}+\mathrm{SMB}(12)$ exceeds the 3 hour time limit.

# 7.2.4 The Impact of Determinism in Bayesian Networks 

In general, when the functions of the graphical model express both hard constraints and general cost functions, it is beneficial to exploit the computational power of the

constraints explicitly via constraint propagation [38-41]. For Bayesian networks, the hard constraints are represented by the zero probability tuples of the CPTs. We note that the use of constraint propagation via directional resolution [42] or generalized arc consistency has been explored in [38,39], in the context of variable elimination algorithms where the constraints are also extracted based on the zero probabilities in the network. The approach we take for handling the determinism in Bayesian networks is based on unit resolution for Boolean Satisfiability (SAT). The idea of using unit resolution during search for Bayesian networks was first explored in [40]. One common way which we used for encoding hard constraints as a CNF formula is the direct encoding [43].

We evaluated the AND/OR Branch-and-Bound algorithm with static mini-bucket heuristics on selected classes of Bayesian networks containing zero probability tuples. The algorithm, denoted by AOBB-C+SAT+SMB (i) exploits the determinism present in the networks by applying unit resolution over the CNF encoding of the zero-probability tuples, at each node in the search tree. We used a unit resolution scheme similar to the one employed by zChaff, a state-of-the-art SAT solver introduced by [44]. We also consider the extension called AOBB-C+SAT+GLS+SMB (i) which uses GLS to compute the initial lower bound, in addition to the constraint propagation scheme.

Table 7 shows the results for 5 deterministic grid networks presented earlier. We observe that $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{SMB}(i)$ improves significantly over $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$, especially at relatively small $i$-bounds. On grid $90-30-1, \mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{SMB}(12)$ is 6 times faster than $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(12)$. As the $i$-bound increases and the search space is pruned more effectively, the difference between $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$ and $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{SMB}(i)$ decreases because the heuristics are strong enough to cut the search space significantly and it already does some level of constraint propagation. When focusing on the impact of the initial lower bound on $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{SMB}(i)$ through algorithm $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{GLS}+\mathrm{SMB}(i)$ we see that the latter is sometimes able to improve even more. On the $90-34-1$ grid, $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{GLS}+\mathrm{SMB}(16)$ finds the optimal solution in about 9 minutes whereas $\mathrm{AOBB}-\mathrm{C}+\mathrm{SAT}+\mathrm{SMB}(16)$ exceeds the 1 hour time limit. We should note that best-first search does not employ a constraint propagation scheme.

# 7.2.5 Summary of Empirical Results on Bayesian Networks 

Our extensive empirical evaluation on Bayesian networks demonstrated conclusively that the memory intensive AND/OR search algorithms guided by static minibucket heuristics were the best performing algorithms overall. The difference between $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$ and the cache-less $\mathrm{AOBB}+\mathrm{SMB}(i)$ was more pronounced at relatively small $i$-bounds which correspond to relatively weak heuristic estimates (e.g., ISCAS'89 networks, grid networks, genetic linkage analysis, instances from the UAI'06 Inference Evaluation contest). For larger $i$-bounds, when the heuristic

estimates are stronger, the difference between graph search $A O B B-C+S M B(i)$ and tree search $A O B B+S M B(i)$ decreased. Best-first search $A O B F-C+S M B(i)$ offered the best performance amongst the memory intensive AND/OR algorithms. We showed that in many cases $A O B F-C+S M B(i)$ was able to outperform dramatically the current state-of-the-art solver for Bayesian networks such as SAMIAM and SUPERLINK (for genetic linkage analysis). However, on very large problem instances, $A O B F-C+S M B(i)$ was outperformed by the depth-first $A O B B-C+S M B(i)$ because of its prohibitive memory requirements. With dynamic mini-bucket heuristics both $A O B B-C+D M B(i)$ and $A O B F-C+D M B(i)$ proved competitive only for relatively small $i$-bounds, due to computational overhead. We also evaluated the impact of determinism and good initial lower bounds on depth-first AND/OR Branch-andBound search, over grid networks, ISCAS'89 networks, genetic linkage analysis networks and instances from the UAI'06 Inference Evaluation dataset. These empirical results, also available in [27,26], showed that applying unit resolution and starting the search with a good initial lower bound caused significant savings on those benchmark networks.

# 7.3 Results for Empirical Evaluation of Weighted CSPs 

Let us first recap the results obtained for Weighted CSPs with our various cache-less algorithms [1]. We showed that the best performance on Weighted CSPs was obtained by the AND/OR Branch-and-Bound tree search algorithm with static minibucket heuristics, at relatively large $i$-bounds, especially for non-binary WCSPs with relatively small domain sizes (e.g., SPOT5 networks, ISCAS'89 circuits, Mastermind game instances). The cache-less $A O B B+S M B(i)$ dominated all its competitors, including the classic OR Branch-and-Bound BB+SMB (i) as well as the OR and AND/OR algorithms that enforce EDAC during search, namely toolbar and the AOEDAC family of algorithms, such as AOEDAC+PVO, DVO+AOEDAC and AOEDAC+DSO, respectively [1]. The AND/OR Branch-and-Bound with dynamic mini-bucket heuristics $A O B B+D M B(i)$ was shown to be competitive only for relatively small $i$-bounds.

In this section we extend the evaluation to memory intensive depth-first and bestfirst search.

### 7.3.1 SPOT5 Benchmark

SPOT5 benchmark contains a collection of large real scheduling problems for the daily management of Earth observing satellites [45]. They can be easily formulated as WCSPs with binary and ternary constraints, as described in [1,3].

Tables 8 and 9 show detailed results on experiments with 7 SPOT5 networks using min-fill pseudo trees, as well as static and dynamic mini-bucket heuristics. The

Table 8
CPU time in seconds and number of nodes visited for solving the SPOT5 benchmarks, using static mini-bucket heuristics and min-fill based pseudo trees. Time limit 3 hours.


networks $42 \mathrm{~b}, 408 \mathrm{~b}$ and 505 b are sub-networks of the original ones and contain only binary constraints.

Tree vs. graph AOBB. As before, the differences in running time and number of nodes visited, between $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}(i)$ and $\mathrm{AOBB}+\mathrm{SMB}(i)$ are more prominent at relatively small $i$-bounds. For example, on the 408 b network, $\mathrm{AOBB}-\mathrm{C}+\mathrm{SMB}$ (12) outperforms $\mathrm{AOBB}+\mathrm{SMB}$ (12) by one order of magnitude. The impact of caching when using dynamic mini-bucket heuristics (Table 9) is again not that pronounced, across $i$-bounds. Notice that toolbar and DVO+AOEDAC (rightmost column in Table 8) are able to solve relatively efficiently only the first 3 test instances. On the

Table 9
CPU time in seconds and number of nodes visited for solving the SPOT5 benchmarks, using dynamic mini-bucket heuristics and min-fill based pseudo trees. Time limit 3 hours.


other hand, toolbar-BTD fails only on the 408 b instance and is overall quite competitive.

AOBB vs. AOBF. When comparing best-first against depth-first AND/OR search we see again that AOBF-C+SMB (i) improves significantly (up to several orders of magnitude), especially for relatively small $i$-bounds. For example, on 505 b , one of the hardest instances, AOBF-C+SMB (8) finds the optimal solution in less than 30 seconds, whereas AOBB-C+SMB (8) exceeds the 3 hour time limit.

Static vs. dynamic mini-bucket heuristics. Figures 12(a) and 12(b) display the running time and number of nodes, as a function of the mini-bucket $i$-bound, on the 404 network (i.e., corresponding to the fourth horizontal block from Tables 8 and 9 , respectively). We see that the power of the dynamic mini-bucket heuristics is visible only for depth-first search and only for small $i$-bounds (e.g., $i=2$ ). At larger $i$-bounds, the static mini-bucket heuristics are cost effective. For instance, the difference in running time between AOBB-C+SMB (10) and AOBB-C+DMB (10)

![img-11.jpeg](img-11.jpeg)

Fig. 12. Comparison of the impact of static and dynamic mini-bucket heuristics. Shown are the CPU time in seconds (a) and number of nodes visited (b) on the 404 SPOT5 network from Tables 8 and 9 , respectively.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Min-fill versus hypergraph partitioning heuristics. CPU time in seconds for solving SPOT5 networks with AOBB-C+SMB (i) (left side) and AOBF-C+SMB (i) (right side). The header of each plot records the average induced width $\left(w^{*}\right)$ and pseudo tree depth (h) obtained with the hypergraph partitioning heuristic. We also show the induced width and pseudo tree depth for the min-fill heuristic.

is about 2 orders of magnitude. Notice that in this case, AOBF-C+SMB (i) outperforms AOBF-C+DMB (i) across all reported $i$-bounds.

Impact of the pseudo tree. In Figure 13 we show the running time distribution of the algorithms using hypergraph and min-fill based pseudo trees, over 20 independent runs, for the 404 and 503 networks. We see again that the hypergraph based pseudo trees are sometimes able to improve performance, especially for relatively small $i$-bounds for which the heuristic estimates are less accurate. For best-first search however, the min-fill based pseudo trees offer the best performance.

# 7.3.2 Mastermind Game Instances 

Table 10 shows the results for experiments with 6 networks corresponding to Mastermind game instances of increasing difficulty. Each of the networks is a ground instance of a relational Bayesian network that models different sizes of the popular game of Mastermind. These networks were produced by the Primula System ${ }^{6}$ and used in experimental results in [46]. For our purpose, we converted these networks into equivalent WCSP instances by taking the negative log probability of each conditional probability table entry. The table has two horizontal blocks, each showing a different range of $i$-bounds.

Tree vs. graph AOBB. We see again that using caching improves considerably the performance of AND/OR Branch-and-Bound search (e.g., see mm-03-08-05). We also note that toolbar and toolbar-BTD were not able to solve any of these instances within the time limit (the results are not displayed).

AOBB vs. AOBF. We see that the best-first search algorithm AOBF-C+SMB (i) offers the overall best performance on this domain. On the mm-03-08-05 instance, for example, AOBF-C+SMB (18) is about 3 times faster than AOBB-C+SMB (18) and about 30 times faster than $A O B B+S M B(18)$, a further demonstration of the power of caching.

Impact of the caching level. Figure 14 illustrates the CPU time, as a function of the cache bound $j$, on two problem instances from Table 10. We notice again the superiority of adaptive caching at relatively small $j$-bounds.

Impact of the pseudo tree. The running time distribution of $A O B B-C+S M B(i)$ and AOBF-C+SMB ( $i$ ) guided by hypergraph and min-fill based pseudo trees over 20 independent runs of each problem instance is displayed in Figure 15. The hypergraph trees are sometimes able to improve slightly the performance of AND/OR Branch-and-Bound, at relatively small $i$-bounds (e.g., mm-04-08-04). For bestfirst search however, the min-fill based pseudo trees offer the best performance. The results on other instances were similar.

[^0]
[^0]:    ${ }^{6}$ http://www.cs.auc.dk/jaeger/Primula

Table 10
CPU time and number of nodes visited for solving Mastermind game instances, using static mini-bucket heuristics and min-fill based pseudo trees. Time limit 1 hour. toolbar and toolbar-BTD were not able to solve any of the test instances within the time limit. The top part of the table shows the results for $i$-bounds between 8 and 18, while the bottom part shows $i$-bounds between 12 and 22.


Memory usage of AND/OR graph search. In Figure 16 we demonstrate again the significant memory requirements of best-first AND/OR search compared with those of the depth-first AND/OR Branch-and-Bound search with full caching on two problem instances.

![img-13.jpeg](img-13.jpeg)

Fig. 14. Naive versus adaptive caching schemes for AND/OR Branch-and-Bound with static mini-bucket heuristics on Mastermind networks. Shown is CPU time in seconds.
![img-14.jpeg](img-14.jpeg)

Fig. 15. Min-fill versus hypergraph partitioning heuristics. CPU time in seconds for solving Mastermind networks with $A O B B-C+S M B(i)$ (left side) and $A O B F-C+S M B(i)$ (right side). The header of each plot records the average induced width $\left(w^{*}\right)$ and pseudo tree depth (h) obtained with the hypergraph partitioning heuristic. We also show the induced width and pseudo tree depth for the min-fill heuristic.

# 7.3.3 Summary of Empirical Results on Weighted CSPs 

Our extensive empirical evaluation on WCSPs demonstrated that the best performance on this domain was obtained by best-first AND/OR search with static minibucket heuristics, for large $i$-bounds, especially on non-binary WCSPs with relatively small domain sizes (e.g., Mastermind game instances, ISCAS'89 networks,

![img-15.jpeg](img-15.jpeg)

Fig. 16. Memory usage of the $A O B B-C+S M B(i)$ and $A O B F-C+S M B(i)$ algorithms on two Mastermind networks from Table 10.
instances from the SPOT5 benchmark). AOBF-C+SMB (i) dominated all its competitors, including the depth-first AOBB-C+SMB (i) as well as OR and AND/OR algorithms that enforce EDAC during search, namely toolbar, toolbar-BTD and the AOEDAC family of algorithms. Best-first AND/OR search with dynamic mini-bucket heuristics AOBF-C+DMB (i) was competitive only for relatively small $i$-bounds (e.g., ISCAS'89 networks [26,27]). We also observed that the depthfirst AND/OR Branch-and-Bound with caching and static mini-bucket heuristics $A O B B-C+S M B(i)$ improved considerably over the cache-less version of the algorithm, namely $A O B B+S M B(i)$. For dynamic mini-bucket heuristics, the difference between $A O B B-C+D M B(i)$ and $A O B B+D M B(i)$ was less prominent.

# 8 Summary and Conclusion 

The paper extends the study of the impact of AND/OR search in graphical models from linear space search of the AND/OR tree to cache-based search of the AND/OR graph. In contrast to the traditional OR space, the AND/OR search space is sensitive to problem decomposition yielding the AND/OR search tree which can be bounded exponentially by the depth of its guiding pseudo tree. Specifically, if the graphical model has treewidth $w^{*}$, the size of the AND/OR search tree is bounded by $O\left(k^{w^{*}} \log n\right)[2,18,1]$. By recognizing identical subtrees, the AND/OR search tree can be extended into a graph yielding the context minimal AND/OR search graph whose size is exponential in the treewidth. The size of the context minimal OR search graph is exponential in the pathwidth. Since for some graphs the difference between treewidth and pathwidth is substantial (e.g., balanced pseudo trees) the AND/OR representation implies substantial time and space savings for memory intensive algorithms traversing the AND/OR graph.

In this paper we extended the AND/OR Branch-and-Bound algorithm to traversing an AND/OR search graph by equipping it with an efficient caching mechanism. We investigated two flexible context-based caching schemes that can adapt to memory

restrictions. Since best-first search strategies are known to be superior to depthfirst ones when memory is utilized, we also introduced a best-first AND/OR search algorithm that traverses the same context minimal AND/OR search graph.

All these algorithms can be guided by any heuristic function. We investigated extensively the mini-bucket heuristics introduced earlier [10] and shown to be effective in the context of the traditional OR search trees [10]. The mini-bucket heuristics can be either pre-compiled (static mini-buckets) or generated dynamically during search at each node in the search space (dynamic mini-buckets). They are parameterized by an $i$-bound which allows to control trade-off between heuristic strength and computational overhead.

We focused our empirical evaluation on two common optimization problems in graphical models: finding the MPE in Bayesian networks and solving combinatorial problems expressed as Weighted CSPs. Our results showed conclusively that the depth-first and best-first memory intensive AND/OR search algorithms guided by mini-bucket heuristics improve dramatically over traditional memory intensive OR search as well as over AND/OR search without caching. We summarize next the most important aspects reflecting the better performance of AND/OR graph search, such as the impact of the level of caching, the mini-bucket $i$-bound, constraint propagation, informed initial upper bounds and the quality of the guiding pseudo trees.

- Impact of the caching level. We proposed two parameterized context-based caching schemes that can adapt to the memory limitations. The naive caching records contexts with size smaller or equal to a cache bound $j$, while the adaptive caching saves also nodes whose context size is beyond $j$, based on adjusted contexts. Our results showed that for small $j$-bounds, adaptive caching is more powerful than the naive scheme (e.g., grid networks from Figure 6, genetic linkage networks from Figure 10). As more space becomes available and as the $j$ bound increases, the two schemes gradually approach full caching. The savings in number of nodes due to both caching schemes are more pronounced at relatively small $i$-bounds of the mini-bucket heuristics. When the heuristics are strong enough to prune the search space substantially (i.e., large $i$-bounds), the context minimal graph traversed by AND/OR Branch-and-Bound is very close to a tree and the effect of caching is reduced.
- Impact of the mini-bucket $i$-bound. Our results show conclusively that when enough memory is available the static mini-bucket heuristics with relatively large $i$-bounds are cost effective (e.g., genetic linkage analysis networks from Tables 3 and 4, Mastermind game instances from Table 10). However, if the space is severely restricted, dynamic mini-bucket heuristics appear to be the preferred choice, especially for relatively small $i$-bounds. These heuristics are far more accurate for the same $i$-bound than the pre-compiled ones.
- Impact of determinism. When the graphical model contains both deterministic information (hard constraints) as well as general cost functions, we demon-

strated that it is beneficial to exploit the computational power of the constraints via constraint propagation. Our experiments on selected classes of deterministic Bayesian networks showed that enforcing unit resolution over the CNF encoding of the determinism present in the network yielded a tremendous reduction in running time (e.g., deterministic grid networks from Table 7).

- Impact of good initial upper bounds. The AND/OR Branch-and-Bound algorithm assumed a trivial initial upper bound (resp. initial lower bound for maximization tasks). We incorporated a more informed upper bound (resp. lower bound for maximization), obtained by first solving the initial problem via local search. Our results showed a tremendous speed-up in some cases (see for example the grid network from Table 7).
- Impact of pseudo tree quality. The performance of the depth-first and bestfirst memory intensive AND/OR search algorithms is influenced significantly by the quality of the guiding pseudo tree. We investigated two heuristics for generating small induced width and/or depth pseudo trees. The min-fill based pseudo trees usually have smaller induced width but significantly larger depth, whereas the hypergraph partitioning heuristic produces much smaller depth trees but yields larger induced widths. Our experiments demonstrated that when the induced width is small enough, which is more typical for min-fill based pseudo trees, the strength of the mini-bucket heuristics compiled along these orderings determines the performance of the AND/OR search algorithms (e.g., SPOT5 networks from Figure 13). However, when the graph is highly connected, the relatively large induced width causes the AND/OR algorithms to traverse a search space that is very close to a tree and, therefore, the hypergraph partitioning based pseudo trees, which tend to have smaller depths, improve performance substantially (e.g., genetic linkage networks from Figure 9 and Table 5).

Our depth-first and best-first AND/OR graph search approaches leave room for future improvements, which are likely to make them more efficient in practice. The space required by AOBB-C and AOBF-C can be enormous, due to the fact that all nodes generated by the algorithms have to be stored in memory. Therefore, memory bounding strategies can be used for context minimal AND/OR graphs, as previously suggested in [19,21,47,48]. Alternatively, we can extend the AND/OR graph search algorithms to greatly expand the amount of available memory by utilizing external disk storage, as described in [49,50].

# Acknowledgments 

This work was partially supported by the NSF grants IIS-0086529 and IIS-0412854, the MURI ONR award N00014-00-1-0617, the NIH grant R01-HG004175-02, the Marie Curie Transfer of Knowledge grant MTKD-CT-2006-042563 and by an IRCSET post-doctoral fellowship.
