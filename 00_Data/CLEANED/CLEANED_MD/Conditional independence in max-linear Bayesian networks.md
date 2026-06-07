# CONDITIONAL INDEPENDENCE IN MAX-LINEAR BAYESIAN NETWORKS 

By Carlos Améndola and Claudia Klüppelberg<br>Technical University of Munich<br>AND<br>By Steffen Lauritzen<br>University of Copenhagen<br>AND<br>By Ngoc M. Tran<br>University of Texas at Austin


#### Abstract

Motivated by extreme value theory, max-linear Bayesian networks have been recently introduced and studied as an alternative to linear structural equation models. However, for max-linear systems the classical independence results for Bayesian networks are far from exhausting valid conditional independence statements. We use tropical linear algebra to derive a compact representation of the conditional distribution given a partial observation, and exploit this to obtain a complete description of all conditional independence relations. In the context-specific case, where conditional independence is queried relative to a specific value of the conditioning variables, we introduce the notion of a source $D A G$ to disclose the valid conditional independence relations. In the context-free case we characterize conditional independence through a modified separation concept, $*$ separation, combined with a tropical eigenvalue condition. We also introduce the notion of an impact graph which describes how extreme events spread deterministically through the network and we give a complete characterization of such impact graphs. Our analysis opens up several interesting questions concerning conditional independence and tropical geometry.


1. Introduction. Max-linear graphical models were introduced in [15] to model causal dependence between extreme events. The underlying graphical structure of the model is a directed acyclic graph (DAG) and to emphasize this aspect, we shall here use the term maxlinear Bayesian network, to allow for generalizations and extensions (see Section 7.2 at the end of this paper).

A max-linear Bayesian network is specified by a random vector $X=\left(X_{1}, \ldots, X_{d}\right)$, a directed acyclic graph $\mathcal{D}=(V, E)$ with nodes $V=\{1, \ldots, d\}$, non-negative edge weights $c_{i j} \geq 0$ for $i, j \in V$, and independent positive random variables $Z_{1}, \ldots, Z_{d}$. These, known as innovations, have support $\mathbb{R}_{>}:=(0, \infty)$ and have atom-free distributions. Then $X$ is specified
[^0]
[^0]:    MSC 2010 subject classifications: 62H22, 60G70, 14T90, 62R01
    Keywords and phrases: Bayesian network, conditional independence, directed acyclic graph, $d$-separation, faithfulness, hitting scenario, Markov properties, max-linear model, tropical geometry

![img-0.jpeg](img-0.jpeg)

Fig 1: Diamond graph with the set $K=\{2\}$ being observed, as indicated by red color. If $c_{42} c_{21} \geq c_{43} c_{31}$, it holds that $X_{1} \Perp X_{4} \mid X_{2}$.
by a recursive system of max-linear structural equations as

$$
X_{i}=\bigvee_{j \in \mathrm{pa}(i)} c_{i j} X_{j} \vee Z_{i}, \quad i=1, \ldots, d
$$

Without loss of generality, we assume that the basic probability space is $\Omega=\mathbb{R}_{>}^{V}$ equipped with the standard Borel $\sigma$-algebra, so all randomness in the system originates from the innovations $Z_{1}, \ldots, Z_{d}$. The equation system (1.1) has solution

$$
X_{i}=\bigvee_{j \in \operatorname{an}(i) \cup\{i\}} c_{i j}^{*} Z_{j}, \quad i=1, \ldots, d
$$

where an $(i)$ denotes the set of nodes $j$ where there is a directed path from $j$ to $i$, and $c_{i j}^{*}$ is a maximum taken over all the products along such paths (see [15], Theorem 2.2). Any such path that realizes this maximum is called critical (max-weighted under $C$ ). The max-linear coefficient matrix $C^{*}=\left(c_{i j}^{*}\right)$ is also known from tropical linear algebra as the Kleene star of $C=\left(c_{i j}\right)$, cf. (2.4) below.

In [21], it was observed that the conditional independence properties for max-linear Bayesian networks are very different from those in a standard Bayesian network. In particular, they are often not faithful to their underlying DAG $\mathcal{D}$. This means that the usual $d$-separation criterion ([13]) on the DAG typically will not identify all valid conditional independence relations, in contrast to the situation for most Bayesian networks based on discrete random variables or linear structural equations. Example 1.1 below gives a simple example of this phenomenon.

Example 1.1 (Diamond). Consider the DAG in Figure 1. The path $1 \rightarrow 2 \rightarrow 4$ is critical if and only if $c_{42} c_{21} \geq c_{43} c_{31}$. If this is the case, the joint distribution of $\left(X_{1}, X_{2}, X_{4}\right)$ has the representation

$$
X_{1}=Z_{1}, \quad X_{2}=c_{21} X_{1} \vee Z_{2}
$$

and

$$
\begin{aligned}
X_{4} & =c_{42} X_{2} \vee Z_{4} \vee c_{43} X_{3} \\
& =c_{42}\left(Z_{2} \vee c_{21} Z_{1}\right) \vee Z_{4} \vee c_{43}\left(Z_{3} \vee c_{31} Z_{1}\right) \\
& =c_{42} Z_{2} \vee c_{42} c_{21} Z_{1} \vee Z_{4} \vee c_{43} Z_{3} \vee c_{43} c_{31} Z_{1} \\
& =c_{42} Z_{2} \vee c_{42} c_{21} Z_{1} \vee Z_{4} \vee c_{43} Z_{3} \quad \text { since } c_{42} c_{21} \geq c_{43} c_{31} \\
& =c_{42} X_{2} \vee Z_{4} \vee c_{43} Z_{3}
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig 2: The Cassiopeia graph with observed nodes $K=\{4,5\}$. Here it holds that $X_{1} \Perp X_{3} \mid X_{\{4,5\}}$.
and hence we have $X_{1} \Perp X_{4} \mid X_{2}$ which does not follow from the $d$-separation criterion. Here, the fact that $1 \rightarrow 2 \rightarrow 4$ is critical renders the path $1 \rightarrow 3 \rightarrow 4$ unimportant for the conditional independence $X_{1} \Perp X_{4} \mid X_{2}$, even if $1 \rightarrow 3 \rightarrow 4$ were also critical (that is, even if $\left.c_{42} c_{21}=c_{43} c_{31}\right)$

In Example 1.1, the complicating issue was associated with paths being critical or not. However, this is not the only way standard $d$-separation fails. In Example 1.2 below, the complications are associated with double colliders along a path.

Example 1.2 (Cassiopeia). We shall show later (see Example 4.2) that a max-linear Bayesian network on the graph in Figure 2 will satisfy $X_{1} \Perp X_{3} \mid X_{\{4,5\}}$ for all coefficient matrices $C$. However, this conditional independence statement does not follow from the $d$ separation criterion since the path from 1 to 3 is $d$-connecting relative to $\{4,5\}$.

Example 1.2 shows that not only are max-linear Bayesian networks often not faithful to $d$-separation, but $d$-separation is also not complete in the sense of [13] for conditional independence in these networks. That is, there are conditional independence statements which are valid for any choice of coefficients $C$, but cannot be derived from $d$-separation.

Also, in contrast to standard results for Bayesian networks, some conditional independence relations are highly context-specific, i.e. depend drastically on the particular values of the conditioning variables, as in Example 1.3 below. To control this, we introduce the notion of a source $D A G \mathcal{C}\left(X_{K}=x_{K}\right)$ for a given context $\left\{X_{K}=x_{K}\right\}$, see Definition 3.16 for details.

Example 1.3 (Tent). Consider the DAG $\mathcal{D}$ to the left in Figure 3 with all edge weights $c_{i j}=1$. Let $K=\{4,5\}$ be the set of observed nodes; we seek all independence relations conditionally valid in the context $X_{4}=X_{5}=2$. Writing out the model (1.1) we find

$$
\begin{aligned}
& X_{1}=Z_{1}, \quad X_{2}=Z_{2}, \quad X_{3}=Z_{3} \vee X_{1} \vee X_{2} \\
& X_{4}=Z_{4} \vee X_{1} \vee X_{2}=2 \\
& X_{5}=Z_{5} \vee X_{1} \vee X_{2}=2
\end{aligned}
$$

Since $Z_{1}, \ldots, Z_{5}$ are a.s. different when the innovations have atom-free distributions, it holds apart from a null-set that $X_{1} \vee X_{2}=Z_{1} \vee Z_{2}=2$. This introduces bounds on the innovations; we must have $Z_{1}, Z_{2}, Z_{4}, Z_{5} \leq 2$ and it also holds that $X_{3} \geq 2$. Further, we then have

$$
\begin{aligned}
& X_{1}=Z_{1}, \quad X_{2}=Z_{2}, \quad X_{1} \vee X_{2}=2, \quad X_{3}=Z_{3} \vee 2 \\
& X_{4}=Z_{4} \vee 2=2 \\
& X_{5}=Z_{5} \vee 2=2
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig 3: The left-hand figure displays what we shall name the tent DAG $\mathcal{D}$. For all coefficients equal to 1 , the source $\operatorname{DAG} \mathcal{C}\left(X_{K}=x_{K}\right)$ when the observed nodes are $K=\{4,5\}$ with observed values $x_{4}=x_{5}=2$, is obtained from the left-hand figure by removing the edges $1 \rightarrow 3$ and $2 \rightarrow 3$, which become redundant in the context $\left\{X_{4}=X_{5}=2\right\}$, see Section 3.3.
whence we conclude that $X_{3} \Perp\left(X_{1}, X_{2}\right) \mid X_{4}=X_{5}=2$, since now the dependence of $X_{3}$ on $X_{1}, X_{2}$ has disappeared. This independence statement is reflected in the lack of edges $1 \rightarrow 3$ and $2 \rightarrow 3$ in the source $\operatorname{DAG} \mathcal{C}\left(X_{4}=X_{5}=2\right)$, shown to the right in Figure 3.

In this paper we give a complete description of valid conditional independence statements for a given matrix $C$, conditional independence statements that hold for all $C$ supported on a given $\operatorname{DAG} \mathcal{D}$, as well as those that depend on the specific values of the conditioning variables. We achieve this by introducing three separation criteria. These are less restrictive than $d$-separation, as they focus on paths that are critical (see Example 1.1), do not have multiple colliders (see Example 1.2), and, for a given context, refer to the source DAG, obtained by removing edges that are redundant in the context (see Example 1.3).

Before we state and prove results for conditional independence, we investigate how extreme events at selected nodes spread through the network. We define an impact graph as a random graph on $V$, containing the edge $j \rightarrow i \Longleftrightarrow X_{i}=c_{i j}^{*} Z_{j}$, i.e. if $X_{i}$ is realized (determined) by $Z_{j}$ (see Definition 3.1). Since the distributions of the innovations are atom-free, it holds with probability one that any node $i$ has at most one parent in such a graph. We give a complete description of all impact graphs with positive probability in Theorem 3.3. As we shall see in Remark 2, the impact graphs index partitions of the innovation space into regions of linearity for the max-linear map in (1.2).

Impact graphs can be compatible with a context $\left\{X_{K}=x_{K}\right\}$ or not, and vice versa, a context $\left\{X_{K}=x_{K}\right\}$ can be possible under a certain impact graph or not. For instance, for the Cassiopeia graph in Example 1.2, the possible impact graphs are: the empty graph, all subgraphs with a single edge, and the four subgraphs with two edges displayed in Figure 4. On the other hand, the impact graph $g_{2}$ implies that $X_{4}>X_{5}$, so only events satisfying this restriction are possible under $g_{2}$.

The union of all impact graphs compatible with a context $\left\{X_{K}=x_{K}\right\}$ describes all possible ways that an extreme innovation could spread across the network while conforming with the context. However, as seen in Example 1.3, the given context can cause max-linear combinations of variables to be constant under specific scenarios, such that they do not influence the distribution of random variables $X_{v}, v \notin K$ as expected. This effect is taken care of by the removal of edges to yield the source $D A G \mathcal{C}\left(X_{K}=x_{K}\right)$ compatible with the context.

Moreover, we classify all nodes into non-constant nodes (active) and constant nodes with specific properties (see Proposition 3.18). This classification plays an important role when

![img-3.jpeg](img-3.jpeg)

Fig 4: The four impact graphs with two edges in the Cassiopeia graph of Example 1.2 as depicted in Figure 2. Suppose all coefficients are equal to one. Then, only the impact graphs $g_{2}$ and $g_{4}$ are compatible with the context $\left\{X_{4}=3, X_{5}=2\right\}$, whereas only the impact graph $g_{3}$ is compatible with the context $\left\{X_{4}=X_{5}=2\right\}$, see Example 3.9 below.
modifying the solution in (1.2) to obtain a compact representation of the conditional distribution.

This compact representation is given in Theorem 4.3 and can be seen as a version of Theorem 6.7 in [15] and of Theorem 1 in [29]. More precisely, [29] studies a general maxlinear model where the max-linear coefficient matrix $C^{*}$ is not necessarily the Kleene star of a max-linear Bayesian network, hence not necessarily idempotent; they further give a more detailed description of the conditional distribution, using a collection of hitting scenarios, describing specific elements of $Z$ which obtain their upper bounds. An important endeavour of the present article is to further identify characteristics of the hitting scenarios, exploiting the graphical structure of the model, and this is done in Theorem 4.3.

We formulate three different theorems to clarify conditional independence for max-linear Bayesian networks. All three have the following structure, using what we shall term $*$ separation $\left(\perp_{*}\right)$ in appropriate derived DAGs.

Theorem Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$. Then for all $I, J, K \subseteq V$,

$$
I \perp_{*} J \mid K \text { in } \widetilde{\mathcal{D}} \Longrightarrow X_{I} \Perp X_{J} \mid X_{K}
$$

The DAG $\widetilde{\mathcal{D}}$ - derived from $\mathcal{D}, C$, and the specific context $\left\{X_{K}=x_{K}\right\}$ - depends on the situation and we distinguish the following three: Theorem 5.12 refers to a fixed $C$ and also a specific context $\left\{X_{K}=x_{K}\right\}$, thus yielding conditional independence relations that are valid for the particular values $x_{K}$; Theorem 5.14 considers a fixed coefficient matrix $C$ and yields independence relations that may depend on $C$ which are valid for all possible contexts; whereas in Theorem 5.15, the coefficient matrix $C$ is arbitrary with support included in $\mathcal{D}$ and this yields conditional independence relations that are universally valid under these conditions. In all three scenarios, the derived DAG $\widetilde{\mathcal{D}}$ is different, and the $*$-separation has to be considered in this derived DAG. In addition, we give conditions for these criteria to be complete in the

sense of [13], that is, they yield all conditional independence statements that are valid under the specified conditions. In Section 6 we investigate in which sense these results are as strong as possible. For a fixed matrix $C$, Theorem 5.14 may not yield all conditional independence results, as specific relations between the coefficients could imply additional independences, similar to what is known as path cancellations for linear Bayesian networks. We provide the tools to identify exactly what these are in Theorem 6.18.

The paper is organized as follows. In Section 2 we introduce basic concepts and notation. We define the impact graphs, describing how effects of extremes spread to other variables, and the source DAG, describing the possible sources for a given value of observations, in Section 3. Section 4 is devoted to deriving a compact representation of the conditional distribution and the conditional independence results are stated and proved in Section 5. Section 6 is devoted to the discussion of completeness. We conclude by indicating potential future work and research directions in Section 7.

# 2. Preliminaries. 

2.1. Graph terminology. We use the same graph notation as in [21]. A directed graph is a pair $g=(V, E)$ of a node set $V=\{1, \ldots, d\}$ and edge set $E=\{j \rightarrow i: i, j \in V, i \neq j\}$. An edge $j \rightarrow i$ points from $j$ to $i$, with $j$ called a parent of $i$ and $i$ is a child of $j$. In a graph $g$, the set of parents of $i$ is $\mathrm{pa}_{g}(i)$ and the set of children of $i$ is $\operatorname{ch}_{g}(i)$. A path from $j$ to $i$ of length $n \geq 1$ is a sequence of distinct nodes $\left[j=k_{0}, k_{1}, \ldots, k_{n}=i\right]$ such that $k_{r-1} \rightarrow k_{r} \in E$ or $k_{r} \rightarrow k_{r-1} \in E$ for all $r=1, \ldots, n$ and we say that $i$ and $j$ are connected. We also say that the path is between $i$ and $j$. A graph is connected if there is a path between any two vertices.

A directed path from $j$ to $i$ has $k_{r-1} \rightarrow k_{r} \in E$ for all $r$. If there is a directed path from $j$ to $i$ in $g$, we say that $j$ is an ancestor of $i$ and $i$ a descendant of $j$. A directed cycle is a directed path with the modification that $i=j$. A directed acyclic graph (abbreviated DAG) is a directed graph with no directed cycles. A DAG is well-ordered if all edges point from low to high, that is, $j \rightarrow i \Longrightarrow j<i$. A connected DAG is a tree if every node has at most one parent. The root of a tree is the unique node in the tree without parents. The height of a tree is the length of the longest directed path in the tree. A forest is a collection of trees. A star is a tree of height at most one, and we call a forest of stars a galaxy. For a forest $g$ on node set $V$ and $i \in V$, we let $R_{g}(i)$ denote the root of the tree containing $i$ and $R(g)$ denotes the set of roots in $g$. A matrix $A \in \mathbb{R}_{\geq}^{d \times d}$ defines a weighted directed graph $\mathcal{D}(A)$, where $j \rightarrow i \in \mathcal{D}(A)$ if and only if its edge weight $a_{i j}>0$. The weight of a path $\pi$ in $\mathcal{D}(A)$ is then the product of its edge weights.
2.2. Tropical linear algebra. A number of theorems in our paper are proved using techniques from tropical linear algebra. Here we recall some essential facts of this field. For a comprehensive text, we recommend [5] and [8]; see also [18] and [26].

Tropical linear algebra is linear algebra with arithmetic in the max-times semiring $\left(\mathbb{R}_{\geq}, \vee, \odot\right)$, defined by

$$
a \vee b:=\max (a, b), \quad a \odot b:=a b \quad \text { for } a, b \in \mathbb{R}_{\geq}:=[0, \infty)
$$

Note that many authors (including those above) use the isomorphic semirings max-plus or min-plus, but we have chosen max-times to conform with the literature on extreme value theory. The operations extend to $\mathbb{R}_{\geq}^{d}$ coordinate-wise and to corresponding matrix multiplication

for $A \in \mathbb{R}_{\geq}^{m \times n}$ and $B \in \mathbb{R}_{\geq}^{n \times p}$ as

$$
(A \odot B)_{i j}=\bigvee_{\ell=1}^{n} a_{i \ell} b_{\ell j}
$$

and we also write

$$
\lambda \odot x=\left(\lambda x_{1}, \ldots, \lambda x_{d}\right) \quad \text { for } \lambda \in \mathbb{R}_{\geq} \text { and } x \in \mathbb{R}_{\geq}^{d}
$$

For example,

$$
\left(\begin{array}{ll}
1 & 8 \\
2 & 3
\end{array}\right) \odot\binom{2}{1}=\left(\begin{array}{ll}
1 \cdot 2 & \vee 8 \cdot 1 \\
2 \cdot 2 & \vee 3 \cdot 1
\end{array}\right)=\binom{8}{4}=4 \odot\binom{2}{1}
$$

The recursive structural equation system (1.1) can be written as a tropically linear equation:

$$
X=C \odot X \vee Z
$$

where $C=\left(c_{i j}\right) \in \mathbb{R}_{\geq}^{d \times d}$ and $X, Z \in \mathbb{R}_{>}^{d}$. We consider the weak transitive closure ([8, Section 1.6.2]) $\Gamma=\Gamma(C)=\left(\gamma_{i j}\right)$ of $C$ given as

$$
\Gamma=\Gamma(C)=\bigvee_{k=1}^{d-1} C^{\odot k}
$$

Here $\gamma_{i j}>0$ if and only if there exists a directed path in $\mathcal{D}(C)$ from $j$ to $i$, and $\gamma_{i j}$ equals the maximum weight over all such paths. We name $\mathcal{D}^{*}(C)$ the weighted reachability $D A G$ of $\mathcal{D}(C)$ and $\mathcal{D}^{*}$ the unweighted counterpart. When $\mathcal{D}(C)$ is a DAG, by [5, Theorem 3.17], (2.2) can be solved uniquely for $X$ as

$$
X=C^{*} \odot Z
$$

where $C^{*}=I_{d} \vee \Gamma(C)$ is the Kleene star of $C$ and $I_{d}$ the $d \times d$ identity matrix. Since Kleene stars are idempotent, that is, $C^{*} \odot C^{*}=C^{*}$, we also have

$$
X=C^{*} \odot X
$$

If $V$ is well-ordered, the matrix $C$ is lower triangular and so are $\Gamma$ and $C^{*}$. The Kleene star $C^{*}$ corresponds to the max-linear coefficient matrix $B$ in [15], [21], and in particular, [15, Theorem 2.2] is a special instance of [5, Theorem 3.17]. For $K \subseteq V$ we let

$$
\mathcal{L}_{K}^{C}=\left\{x_{K}: \exists z \in \mathbb{R}_{>}^{V} \text { with } x_{K}=\left(C^{*} \odot z\right)_{K}\right\}
$$

denote the image of the projection to $K$-coordinates of the max-linear map determined by $C^{*}$. A matrix $A=\left(a_{i j}\right) \in \mathbb{R}_{\geq}^{d \times d}$ has tropical eigenvalue $\lambda$ and tropical eigenvector $x \in \mathbb{R}_{\geq}^{d}$ if

$$
A \odot x=\lambda \odot x
$$

For example, equation (2.1) shows that $x=(2,1)$ is a tropical eigenvector for the given matrix, with tropical eigenvalue $\lambda=4$.

The maximum geometric mean of weights along a directed cycle in $\mathcal{D}(A)$ is the maximum cycle mean of $A$, denoted $\lambda(A)$. Note that if $\mathcal{D}(A)$ is acyclic then $\lambda(A)=0$. For any matrix $A$, the number $\lambda(A) \geq 0$ is always a tropical eigenvalue, called the principal eigenvalue of $A$ [8, Theorem 4.2.4]. A cycle achieving the maximum mean is a critical cycle. Similarly, a vector $x \in \mathbb{R}_{>}^{d}$ is called a tropical subeigenvector of $A$ for $\lambda>0$ if

$$
A \odot x \leq \lambda \odot x
$$

The following fact about tropical subeigenvectors will be useful.

Proposition 2.1. Let $A \in \mathbb{R}_{\geq}^{V \times V}$. We then have
(a) There exists $x \in \mathbb{R}_{>}^{V}$ such that $A \odot x \leq x$ if and only if $\lambda(A) \leq 1$.
(b) Suppose $\lambda(A)=1, S \subseteq V$ is the union of the support of its critical cycles, and that $x \in \mathbb{R}_{>}^{V}$ satisfies $A \odot x \leq x$. Then $A_{S S} \odot x_{S}=x_{S}$.
(c) There exists $x \in \mathbb{R}_{>}^{V}$ such that $A \odot x<x$ if and only if $\lambda(A)<1$.

Proof. Statement (a) is shown in [8, Theorem 1.6.18]. Now we prove (b). First consider the case $S=V$. Let $x$ be such that $A \odot x \leq x$. Fix any $i \in V$. Then $i$ belongs to some critical cycle $\sigma$ of length $r$ that achieves the tropical eigenvalue. For each edge $v \rightarrow u$ in this cycle, $A \odot x \leq x$ implies

$$
a_{u v} x_{v} \leq x_{u}
$$

Therefore,

$$
\begin{aligned}
\prod_{v \rightarrow u \in \sigma} a_{u v} & \leq \prod_{v \rightarrow u \in \sigma} \frac{x_{u}}{x_{v}} \\
& =1 \text { since } \sigma \text { is a cycle. }
\end{aligned}
$$

But $\sigma$ is critical, so

$$
\prod_{v \rightarrow u \in \sigma} a_{u v}=c(\sigma)=\lambda^{r}=1
$$

Thus all the inequalities in (2.9) must be equalities; that is, $a_{u v} x_{v}=x_{u}$ for all nodes $u, v$ in the support of $\sigma$. In particular, this holds for $u=i$. Thus, for the edge $v \rightarrow i \in \sigma$,

$$
x_{i} \geq(A \odot x)_{i} \geq a_{i v} x_{v}=x_{i}
$$

So $(A \odot x)_{i}=x_{i}$. Since $i$ was chosen arbitrarily, it follows that $A \odot x=x$. Now suppose $S \subset V$. Let $\bar{S}=V \backslash S$. Then

$$
x_{S} \geq(A \odot x)_{S}=A_{S S} \odot x_{S} \vee A_{S \bar{S}} \odot x_{\bar{S}} \geq A_{S S} \odot x_{S}
$$

Since $\lambda\left(A_{S S}\right)=1$, applying the previous argument to $A_{S S}$ gives $A_{S S} \odot x_{S}=x_{S}$.
Now we prove (c). Suppose $\lambda(A)<1$. Let $x$ be an associated eigenvector to the principal eigenvalue of $A$. Then $A \odot x=\lambda(A) x<x$. For the converse, if $A \odot x<x$ it also satisfies $A \odot x \leq x$ so by (a) we have $\lambda(A) \leq 1$. If $\lambda(A)=1$ then by (b), there exists some $S \subseteq V$, $|S| \geq 2$, such that $A_{S S} \odot x_{S}=x_{S}$. But then

$$
x_{S}=A_{S S} \odot x_{S} \leq(A \odot x)_{S}<x_{S}
$$

a contradiction. Thus we conclude that $\lambda(A)<1$ and the proof is complete.
We recall one more useful fact from tropical linear algebra:
Lemma 2.2 ([8], Lemma 1.6.19). Let $A \in \mathbb{R}_{\geq}^{V \times V}$ with $\lambda(A)=1$ and eigenvector $x \in \mathbb{R}_{>}^{V}$. Let $\sigma$ be a critical cycle in $A$. Then for all edges $v \rightarrow u \in \sigma$,

$$
a_{u v} x_{v}=x_{u}
$$

2.3. Conditional independence. Conditional independence is concerned with probability distributions on product spaces $\mathcal{X}=\prod_{i \in V} \mathcal{X}_{i}$, where $\mathcal{X}_{i}$ are measurable spaces. For $I \subseteq V$ we write $x_{I}=\left(x_{v}, v \in I\right)$ to denote a generic element in $\mathcal{X}_{I}=\prod_{v \in I} \mathcal{X}_{v}$, and similarly $X_{I}=\left(X_{v}\right)_{v \in I}$. If $\mathbb{P}$ is a probability distribution on $\mathcal{X}$, we use the short notation

$$
I \Perp J \mid K \Longleftrightarrow X_{I} \Perp X_{J} \mid X_{K}
$$

where $\Perp$ denotes probabilistic conditional independence w.r.t. $\mathbb{P}$.
Graphical models identify conditional independence relations through a separation criterion $\perp_{\sigma}$ applied to a graph. Such a separation criterion is, for example, given by $d$-separation $\perp_{\mathcal{D}}$ ([13]) for a given DAG $\mathcal{D}$; see for example [22], [24], or [25] for further details. A separation criterion $\perp_{\sigma}$ is complete relative to a family $\mathcal{P}$ of probability distributions if

$$
I \Perp J \mid K \text { for all } \mathbb{P} \in \mathcal{P} \Longleftrightarrow I \perp_{\sigma} J \mid K
$$

A probability distribution $\mathbb{P}$ of $X$ is faithful to $\perp_{\sigma}$ if for all disjoint subsets $I, J, K$ of $V$ and that specific $\mathbb{P}$ it holds that

$$
I \Perp J \mid K \Longleftrightarrow I \perp_{\sigma} J \mid K
$$

Thus the distribution of $X$ is in particular Markov w.r.t. $\perp_{\sigma}$. If there exists a faithful distribution $\mathbb{P} \in \mathcal{P}$ for $\perp_{\sigma}$, the separation criterion is obviously complete.
3. Auxiliary graphs. In this section we introduce the concept of an impact graph, an impact graph compatible with a context, and a source DAG. These are devices that translate probabilistic statements to graph-theoretic and algebraic statements, and at the same time keep track of all deterministic relationships in a max-linear Bayesian network.

# 3.1. The context-free impact graph. 

Definition 3.1. Consider the max-linear Bayesian network (2.2) with fixed coefficient matrix $C$. The (context-free) impact graph is a random graph $G=G(Z)$ on $V$ consisting of the following edges:

$$
j \rightarrow i \Longleftrightarrow X_{i}=c_{i j}^{*} Z_{j}
$$

and we let $\mathcal{E}(g)=\left\{z \in \mathbb{R}_{>}^{V}: G(z)=g\right\}$ denote the event that $\{G=g\}$.
In the following, we let $\mathfrak{G}=\mathfrak{G}(C)$ denote the set of impact graphs that have positive probability for a given coefficient matrix $C$.

Remark 1. Since the distributions of the $Z_{j}$ are atom-free, it holds with probability one that any node $i$ has at most one parent and thus if $\mathbb{P}(\mathcal{E}(g)>0)$, i.e. $g \in \mathfrak{G}, g$ will be a forest. We shall only consider configurations of $Z$ that conform with this and we emphasize that we are only ignoring a null-set in $\Omega=\mathbb{R}_{>}^{V}$.

REMARK 2. Define the restricted Kleene star $C_{g}^{*}$ as

$$
\left(C_{g}^{*}\right)_{i j}= \begin{cases}1 & \text { if } i=j \in R(g) \\ c_{i j}^{*} & \text { if } j \rightarrow i \in g \\ 0 & \text { otherwise }\end{cases}
$$

The impact graphs induce a partition of $\mathbb{R}_{>}^{V}$ into regions where the map $Z \rightarrow X$ is linear with matrix $C_{g}^{*}$. In other words, we have an alternative representation of $X$ as

$$
X=C^{*} \odot Z \stackrel{\text { a.s. }}{=} C_{G}^{*} \odot Z=C_{G}^{*} Z
$$

where the product in the rightmost expression is a standard linear matrix product as $C_{G}^{*}$ has exactly one positive number in each row. See also Example 3.7 below.

The main result of this section is Theorem 3.3, which gives a precise and complete characterization of all impact graphs $\mathfrak{G}$ in a max-linear Bayesian network (2.2). To establish this characterization, we need to define the impact exchange matrix of a given forest $g$. Recall that $\operatorname{ch}_{g}(i)$ denotes the set of children of $i$ in $g$ (Section 2.1).

Definition 3.2. Consider a DAG $\mathcal{D}$ with coefficient matrix $C$ and Kleene star $C^{*}$ and let $g$ be a forest with root set $R=R(g)$. The impact exchange matrix $M(g)=M\left(g, C^{*}\right)$ of $g$ with respect to $C^{*}$ is an $|R| \times|R|$ matrix with entries defined by $m_{r r}=0$ for all $r \in R$, and for $r \neq r^{\prime}$ :

$$
m_{r r^{\prime}}:=\max _{i \in \operatorname{ch}_{g}(r)} \frac{c_{i r^{\prime}}^{*}}{c_{i r}^{*}}
$$

Note that $m_{r r^{\prime}}=0$ if $\operatorname{ch}_{g}(r)=\emptyset$. Finally, recall from Section 2.2 that $\mathcal{D}^{*}$ is the reachability DAG and $\lambda(M(g))$ is the principal eigenvalue of $M(g)$. We now have the following fundamental theorem:

THEOREM 3.3. Consider a max-linear Bayesian network with coefficient matrix $C$ and Kleene star $C^{*}$. Then $g \in \mathfrak{G}$ if and only if the following four conditions hold:
(a) $g$ is a subgraph of $\mathcal{D}^{*}$.
(b) $g$ is a galaxy, i.e. a forest of stars.
(c) If $j \rightarrow i$ in $g$ and $c_{i j}^{*}=c_{i k}^{*} c_{k j}^{*}$ then $k \nrightarrow i$ and $j \rightarrow k$ in $g$.
(d) $\lambda(M(g))<1$.

Before we proceed to the proof of this result, some explanation of the elements of the theorem might be appropriate. Theorem 3.3 describes all possible impact scenarios. With probability one, any outcome of the max-linear Bayesian network has a system of (extreme) root variables $Z_{R}$ and the value at all other nodes will be a.s. constant and appropriate multiples of these, their impact spreading across the network as determined by the galaxy $g \in \mathfrak{G}$.

The conditions (a) and (b) in Theorem 3.3 are necessary, but not sufficient. To understand condition (d), consider the definition of the impact exchange matrix $M(g)$. Intuitively, the entry $m_{r r^{\prime}}$ measures the worst possible relative cost for a node $i$ to be reassigned from root $r$ to root $r^{\prime}$ in $g$. The graph induced by positive entries of $M(g)$ may have directed cycles. A directed cycle in this graph starting at a root $r$ creates an inequality involving $Z_{r}$. Condition (d) of Theorem 3.3 ensures that this inequality can be satisfied. Example 3.4 below shows that a violation of the condition on the principal eigenvalue $\lambda(M(g))$ of the impact exchange matrix $M(g)$ yields an inconsistency, even if the other conditions are satisfied. The argument in Example 3.4 below illustrates the key step in the proof that establishes the necessity of condition (d).

![img-4.jpeg](img-4.jpeg)
![img-5.jpeg](img-5.jpeg)

Fig 5: Bipartite DAG: The subgraph $g$ to the right is not an impact graph for the weighted DAG $\mathcal{D}(C)$ to the left as it violates the principal eigenvalue condition (d) in Theorem 3.3.

Example 3.4 (Bipartite). Consider the weighted graph $\mathcal{D}$ with weights given in Figure 5. The subgraph $g$ to the right in Figure 5 satisfies conditions (a)-(c) of Theorem 3.3. However, it fails to satisfy condition (d) because

$$
M(g)=\left[\begin{array}{ll}
0 & 2 \\
2 & 0
\end{array}\right]
$$

since

$$
m_{12}=\max _{i \in \operatorname{ch}_{g}(1)=\{3\}} \frac{c_{i 2}^{*}}{c_{i 1}^{*}}=\frac{c_{32}^{*}}{c_{31}^{*}}=\frac{1}{1 / 2}=2, \quad m_{21}=\max _{i \in \operatorname{ch}_{g}(2)=\{4\}} \frac{c_{i 1}^{*}}{c_{i 2}^{*}}=\frac{c_{41}^{*}}{c_{42}^{*}}=\frac{1}{1 / 2}=2
$$

Then $\lambda(M(g))=\sqrt{2 \cdot 2}=2>1$, so $g$ is not an impact graph. Indeed if it were, $1 \rightarrow 3$ would imply $X_{3}=\frac{1}{2} Z_{1}>Z_{2}$ but $2 \rightarrow 4$ would imply $X_{4}=\frac{1}{2} Z_{2}>Z_{1}$ and thus $Z_{1}>2 Z_{2}>4 Z_{1}$, which is inconsistent since $Z_{1}>0$.

Proof of Theorem 3.3. First we show that all conditions are necessary.
To prove (a), let $g \in \mathfrak{G}$. If $c_{i j}^{*}=0$, then $X_{i}>0=c_{i j}^{*} Z_{j}$, which means that $j \rightarrow i \notin g$. So $g$ is a subgraph of $\mathcal{D}^{*}$ which proves (a).

To establish (b) we first note that $g$ must be a forest from Remark 1. We shall then argue that any tree in the forest has height at most one. Suppose $j \rightarrow i \in g$. Then

$$
X_{i}=c_{i j}^{*} Z_{j}>Z_{i} \text { on } \mathcal{E}(g)
$$

Now, for any $k \in V$, either $c_{k i}^{*}=0$ so $i \rightarrow k \notin g$ by (a), or we have by the idempotency of $C^{*}$ and (2.5) that

$$
X_{k} \geq c_{k i}^{*} c_{i j}^{*} Z_{j}>c_{k i}^{*} Z_{i} \text { on } \mathcal{E}(g)
$$

and therefore there is no edge $i \rightarrow k$ in $g$ which proves (b).
Next we establish (c). Consider a triple of nodes $i, j, k$ with $j \rightarrow i$ and $c_{i j}^{*}=c_{i k}^{*} c_{k j}^{*}$. Since $g$ is a forest and $j \rightarrow i$, we must have $k \rightarrow i \notin g$. Also, since $j \rightarrow i$ we have as before

$$
X_{i}=c_{i j}^{*} Z_{j} \text { on } \mathcal{E}(g)
$$

Using (2.5) again, we know that $X_{i} \geq c_{i k}^{*} X_{k}$. Then the relation $c_{i j}^{*}=c_{i k}^{*} c_{k j}^{*}$ yields

$$
X_{k} \geq c_{k j}^{*} Z_{j}=\frac{c_{i j}^{*}}{c_{i k}^{*}} Z_{j}=\frac{X_{i}}{c_{i k}^{*}} \geq X_{k} \text { on } \mathcal{E}(g)
$$

and hence we must have equality so $X_{k}=c_{k j}^{*} Z_{j}$ on $\mathcal{E}(g)$. This proves (c).

For condition (d) we first note that if $\lambda(M)=0$ then it is certainly less than 1 . So assume $\lambda(M)>0$. Then there exists a critical cycle $r_{1} \leftarrow r_{2} \cdots \leftarrow r_{k} \leftarrow r_{1}$ with $r_{1}, \ldots, r_{k} \in R$ such that

$$
0<(\lambda(M))^{k}=m_{r_{1} r_{2}} m_{r_{2} r_{3}} \ldots m_{r_{k} r_{1}}
$$

In particular, this implies each edge in the cycle is not 0 , so for each edge, say, $r_{2} \rightarrow r_{1}$, there exists a node $i \in V$ that achieves this maximum so that $r_{1} \rightarrow i$ in $g$ and

$$
\frac{c_{i r_{2}}^{*}}{c_{i r_{1}}^{*}}=m_{r_{1} r_{2}}
$$

Now, since $r_{1} \rightarrow i$ in $g$ and $i$ has at most one parent, this implies $c_{i r_{1}}^{*} Z_{r_{1}}>c_{i r_{2}}^{*} Z_{r_{2}}$, whereby $Z_{r_{1}}>m_{r_{1} r_{2}} Z_{r_{2}}$ by rearranging. Tracing this cycle, we obtain the equation

$$
Z_{r_{1}}>\left(m_{r_{1} r_{2}} m_{r_{2} r_{3}} \ldots m_{r_{k} r_{1}}\right) Z_{r_{1}}
$$

Dividing by $Z_{r_{1}}>0$, we obtain from (3.4) that $\lambda(M)<1$. Thus, all four conditions are necessary.

To see that the conditions are sufficient, let $g$ be a graph that satisfies all four conditions. Let $\epsilon>0$ be an arbitrarily small constant, and

$$
\alpha=\max _{i, j, k, l: c_{j i}^{*}, c_{l k}^{*}>0} \frac{c_{l k}^{*}}{c_{j i}^{*}}
$$

Let $v$ be a tropical eigenvector of $M$ for $\lambda(M)<1$. This means

$$
(M \odot v)_{r}=\lambda(M) v_{r}<v_{r}
$$

for $v_{r}>0$, so that the event

$$
\begin{aligned}
\mathcal{E}=\{ & v_{r}>Z_{r}>(M \odot v)_{r} \text { for } r \in R \text { s.t. } v_{r}>0, Z_{r}>\alpha \epsilon \text { for } r \in R \text { s.t. } v_{r}=0 \\
& \text { and } Z_{j}<\epsilon \text { for } j \notin R\}
\end{aligned}
$$

satisfies $\mathbb{P}(\mathcal{E})>0$. We now argue that $\mathcal{E}$ is a subevent of $\mathcal{E}(g)$. Since the collection of events $\{\mathcal{E}(g): g \in \mathfrak{G}\}$ partitions the innovation space $\mathcal{E}$, the event $\mathcal{E}$ must be partitioned into finitely many events, each with positive probability, which we denote $\mathcal{E} \cap \mathcal{E}\left(g_{1}^{\prime}\right), \cdots, \mathcal{E} \cap \mathcal{E}\left(g_{s}^{\prime}\right)$. By definition of $g$, each $i$ belongs to a unique star with root $r$. Under the event $\mathcal{E}$, for all $r^{\prime} \in R$, $r^{\prime} \neq r$,

$$
Z_{r}>\max _{r^{\prime}} m_{r r^{\prime}} v_{r^{\prime}}>\max _{r^{\prime}} m_{r r^{\prime}} Z_{r^{\prime}}
$$

therefore, $Z_{r}>m_{r r^{\prime}} Z_{r^{\prime}}$ that is, $c_{i r}^{*} Z_{r}>c_{i r^{\prime}}^{*} Z_{r^{\prime}}$ whence $r^{\prime} \nrightarrow i$ for all $g^{\prime} \in\left\{g_{1}^{\prime}, \ldots, g_{s}^{\prime}\right\}$. Similarly, for any $r^{\prime} \notin R$ with $c_{i r^{\prime}}^{*}>0$,

$$
c_{i r}^{*} Z_{i}>c_{i r}^{*} \alpha \geq c_{i r}^{*} \frac{c_{i r^{\prime}}^{*}}{c_{i r}^{*}} \epsilon>c_{i r^{\prime}}^{*} Z_{r^{\prime}}
$$

and hence $r^{\prime} \nrightarrow i$ in any of $g^{\prime} \in\left\{g_{1}^{\prime}, \ldots, g_{s}^{\prime}\right\}$. Thus $r \rightarrow i$ in any $g^{\prime}$ and we must have $\mathcal{E} \subseteq \mathcal{E}(g)$, so $\mathbb{P}(\mathcal{E}(g)) \geq \mathbb{P}(\mathcal{E})>0$, as needed.

![img-6.jpeg](img-6.jpeg)

Fig 6: The half-butterfly graph $\mathcal{D}(C)$ and its weighted reachability DAG $\mathcal{D}^{*}(C)$ where only edge weights for additional edges are indicated. The galaxy $g_{1}$ is not an impact graph for this DAG as it violated the as it violates the triangle condition (c) in Theorem 3.3, while the galaxy $g_{2}$ is.

Example 3.5 (Half-butterfly). Let $\mathcal{D}$ be the weighted DAG given in the leftmost part of Figure 6. Its weighted reachability DAG $\mathcal{D}^{*}(C)$ is shown to its right. For example, we have $c_{41}^{*}=c_{43}^{*} c_{31}^{*}=3$. Now consider the two different subgalaxies $g_{1}$ and $g_{2}$ shown to the right in Figure 6. We shall see that $g_{2}$ is an impact graph for the given coefficient matrix $C$ while $g_{1}$ is not. Indeed, $g_{1} \notin \mathfrak{G}$ as it violates the triangle condition (c) in Theorem 3.3: $1 \rightarrow 4 \in g_{1}$ and $c_{41}^{*}=c_{43}^{*} c_{31}^{*}$ but $1 \rightarrow 3 \notin g_{1}$. On the other hand, $1 \rightarrow 3 \in g_{2}$ as required. Furthermore, $g_{2}$ has impact exchange matrix given by

$$
M\left(g_{2}\right)=\left[\begin{array}{ll}
0 & \frac{1}{2} \\
\frac{3}{4} & 0
\end{array}\right]
$$

because

$$
m_{12}=\max _{i \in \operatorname{ch}_{g_{2}}(1)=\{3,4\}} \frac{c_{i 2}^{*}}{c_{i 1}^{*}}=\max \left\{\frac{1 / 2}{1}, \frac{3 / 2}{3}\right\}=\frac{1}{2}, \quad m_{21}=\max _{i \in \operatorname{ch}_{g_{2}}(2)=\{5\}} \frac{c_{i 1}^{*}}{c_{i 2}^{*}}=\frac{c_{51}^{*}}{c_{52}^{*}}=\frac{3}{4}
$$

We have then $\lambda\left(M\left(g_{2}\right)\right)=\sqrt{\frac{1}{2} \cdot \frac{3}{4}}=\sqrt{\frac{3}{8}}<1$ and so condition (d) also holds. We conclude by Theorem 3.3 that $g_{2} \in \mathfrak{G}$. A possible realization in terms of $Z$ is given by $Z=$ $\left(z_{1}, z_{2}, z_{3}, z_{4}, z_{5}\right)=(2,3,0.1,0.4,0.2)$ leading to $X=\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right)=(2,3,2,6,12)$.

The following simple lemma shall be used in the subsequent analysis.
Lemma 3.6. Consider the max-linear Bayesian network (2.2) with fixed coefficient matrix $C$. Let $g \in \mathfrak{G}$ be an impact graph with root set $R=R(g)$. Then it holds for all $z \in \mathcal{E}(g)$ that

$$
M \odot z_{R} \leq z_{R}
$$

where $M=M(g, C)$ is the impact exchange matrix of $g$ and $z_{R}=\left(z_{r}\right)_{r \in R}$ is the truncation of $z$ to the root set.

Proof. Let $\mathcal{E}^{\prime}=\{z: z$ does not satisfy (3.6) $\}$. Note that $\mathcal{E}^{\prime}$ decomposes as the union of $R(R-1)$ sub-events $\mathcal{E}_{r r^{\prime}}^{\prime}$, where

$$
\mathcal{E}_{r r^{\prime}}^{\prime}=\left\{m_{r r^{\prime}} z_{r^{\prime}}>z_{r}\right\}
$$

![img-7.jpeg](img-7.jpeg)

Fig 7: Impact graphs $\mathfrak{G}$ for the bipartite DAG in Figure 5. There are a total of eight such graphs, the remaining three $\left(g_{3}, g_{5}\right.$, and $\left.g_{7}\right)$ obtained by the reflection $(1,3) \leftrightarrow(2,4)$ of $g_{2}, g_{4}$, and $g_{6}$.

We shall next show that $\mathcal{E}(g) \cap \mathcal{E}_{r r^{\prime}}^{\prime}=\emptyset$ for each pair $r, r^{\prime} \in R$ with $r \neq r^{\prime}$. Suppose for contradiction that there exists some $z \in \mathcal{E}(g) \cap \mathcal{E}_{r r^{\prime}}^{\prime}$. By definition, $m_{r r^{\prime}}=\max _{i \in \operatorname{ch}_{g}(r)} \frac{c_{i r^{\prime}}^{*}}{c_{i r}^{*}}$. Let $i \in \operatorname{ch}_{g}(r)$ be a node that achieves this maximum. Then $z \in \mathcal{E}_{r r^{\prime}}^{\prime}$ implies

$$
c_{i r^{\prime}}^{*} z_{r^{\prime}}>c_{i r}^{*} z_{r}
$$

But now the max-linear representation of $X$ implies that on $\mathcal{E}_{r r^{\prime}}^{\prime}$,

$$
x_{i} \neq c_{i r}^{*} z_{r}
$$

which contradicts that $r \rightarrow i$ in $g$. Hence we conclude that $\mathcal{E}(g) \cap \mathcal{E}_{r r^{\prime}}^{\prime}=\emptyset$ and thus further that

$$
\mathcal{E}(g) \cap \mathcal{E}^{\prime}=\mathcal{E}(g) \cap \bigcup_{r r^{\prime}} \mathcal{E}_{r r^{\prime}}^{\prime}=\emptyset
$$

as needed.
3.2. Impact graphs compatible with a context. As mentioned in Remark 2, the impact graphs represent a partition of the innovation space $\mathcal{E}=\mathbb{R}_{>}^{V}$ into regions of linearity. We can also represent these as linear maps $L_{g}: z \in \mathbb{R}_{>}^{R(g)} \mapsto x \in \mathbb{R}_{>}^{V}$ via

$$
L_{g}(z)_{r}=z_{r}, \quad L_{g}(z)_{i}=c_{i r}^{*} z_{r} \quad \text { iff } \quad r \rightarrow i \text { in } g
$$

We shall illustrate this in a small example.
Example 3.7 (Bipartite). Consider again the DAG and coefficient matrix of Example 3.4 as depicted in Figure 5. Figure 7 displays all impact graphs for this DAG, save for their symmetric counterparts.

Of the 16 edge-induced subgraphs of the DAG $\mathcal{D}$, only nine are forests and one of them, displayed to the right in Figure 5, violates the principal eigenvalue condition; so there are eight valid galaxies left, five of which are displayed in Figure 7, and the remaining three obtained by appropriate relabeling. The max-linear map is

$$
C^{*} \odot z=\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
\frac{1}{2} & 1 & 1 & 0 \\
1 & \frac{1}{2} & 0 & 1
\end{array}\right] \odot\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3} \\
z_{4}
\end{array}\right]=\left[\begin{array}{c}
z_{1} \\
z_{2} \\
\frac{1}{2} z_{1} \vee z_{2} \vee z_{3} \\
z_{1} \vee \frac{1}{2} z_{2} \vee z_{4}
\end{array}\right]
$$

and the corresponding matrices $C_{g}^{*}$ for the pieces of linearity are

$$
\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \quad\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
\frac{1}{2} & 0 & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \quad\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0
\end{array}\right] \quad\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
\frac{1}{2} & 0 & 0 & 0 \\
1 & 0 & 0 & 0
\end{array}\right] \quad\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0
\end{array}\right]
$$

mapping $z$ respectively into

$$
\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3} \\
z_{4}
\end{array}\right] \quad\left[\begin{array}{l}
z_{1} \\
z_{2} \\
\frac{1}{2} z_{1} \\
z_{4}
\end{array}\right] \quad\left[\begin{array}{l}
z_{1} \\
z_{2} \\
\frac{1}{2} z_{1} \\
z_{1}
\end{array}\right] \quad\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{2} \\
z_{1}
\end{array}\right]
$$

These maps can also be considered as maps $L_{g}$ from the root set to the node set and would then have matrices

$$
\left[\begin{array}{lllll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \quad\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
\frac{1}{2} & 0 & 0 \\
0 & 0 & 1
\end{array}\right] \quad\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{array}\right] \quad\left[\begin{array}{ll}
1 & 0 \\
0 & 1 \\
\frac{1}{2} & 0 \\
1 & 0
\end{array}\right] \quad\left[\begin{array}{ll}
1 & 0 \\
0 & 1 \\
0 & 1 \\
1 & 0
\end{array}\right]
$$

where the roots $(1,2,4)$ in $g_{2}$ have been renumbered as $(1,2,3)$. Indeed these matrices are simply obtained by removing zero-columns in the first set of matrices. Note that the rank $r_{g}$ of the maps are all equal to $r_{g}=|R(g)|$, the number of stars in the galaxy, i.e. $4,3,3,2,2$ in these cases.

Definition 3.8. Let $K \subseteq V$ and $\Pi_{K}(x)=x_{K}$ be the projection onto coordinates in $K$. For $x_{K} \in \mathcal{L}_{K}^{C}$ as defined in (2.6), we define
(a) A graph $g \in \mathfrak{G}$ is compatible with the context $\left\{X_{K}=x_{K}\right\}$ if the following are true:
(i) $\mathcal{E}(g) \cap\left\{X_{K}=x_{K}\right\} \neq \emptyset$,
(ii) the rank of $\Pi_{K} \circ L_{g}$ is minimal among those $g \in \mathfrak{G}$ which satisfy (i).
(b) The set of compatible graphs $g$ is called the impact graphs for the context $\left\{X_{K}=x_{K}\right\}$, denoted $\mathfrak{G}\left(X_{K}=x_{K}\right)$.
(c) We further say that the context $\left\{X_{K}=x_{K}\right\}$ is possible if $\mathfrak{G}\left(X_{K}=x_{K}\right) \neq \emptyset$ and possible under $g$ if $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. Else the context $\left\{X_{K}=x_{K}\right\}$ is said to be impossible or impossible under $g$ respectively. For brevity we shall also use the expression that $x_{K}$ is possible.

Note that although all events of the form $\left\{X_{K}=x_{K}\right\}$ have probability zero, we are now distinguishing between those that are exceptions from events of the form $\mathcal{E}(g)$ (impossible contexts) and those that are not (possible contexts). In other words, $x_{K}$ might still satisfy $x_{K} \in \mathcal{L}_{K}^{C}$ without being possible. In the following we shall only pay attention to possible contexts. Furthermore, this definition also applies to the special case $K=V$ so we now can speak about $\{X=x\}$ being possible or impossible under $g \in \mathfrak{G}$.

The rank condition (a) (ii) ensures that if any subevent $\mathcal{E}\left(g^{*}\right)$ includes $x_{K}$ and the map $\Pi_{K} \circ L_{g^{*}}$ has higher rank than $\Pi_{K} \circ L_{g}$, then the entire collection of contexts $\left\{X_{K}=x_{K}\right\}$ in the image of $\Pi_{K} \circ L_{g}$ is a null-set in $\mathcal{E}\left(g^{*}\right)$. Therefore, the set of points in $\mathcal{L}_{K}^{C}$ that are not possible has measure zero and can be ignored when discussing conditional distributions.

Example 3.9. Consider the Cassiopeia graph in Example 1.2 with all coefficients equal to one and the event $\left\{X_{4}=X_{5}=2\right\}$. The impact graphs $g_{3}$ and $g_{4}$ are the only impact graphs among those in Figure 4 that satisfy condition (i) in Definition 3.8, as the other impact graphs imply strict inequalities between $x_{4}$ and $x_{5}$. In addition, the empty galaxy, and all galaxies with a single edge satisfy condition (i). However, the rank of $\Pi_{K} \circ L_{g_{3}}$ is one, whereas the rank of all other maps $\Pi_{K} \circ L_{g}$ is two. Hence only $g_{3}$ is compatible with $\left\{X_{4}=X_{5}=2\right\}$.

Definition 3.10. Suppose $\left\{X_{K}=x_{K}\right\}$ is possible. We say that $X_{j}$ is constant on $\left\{X_{K}=\right.$ $\left.x_{K}\right\}$ if there exists $x_{j}^{*} \in \mathbb{R}_{>}$such that

$$
\left\{X_{K \cup j}=x_{K \cup j}\right\} \text { is possible if and only if } x_{j}=x_{j}^{*}
$$

Similarly, $X_{j}$ is constant on $\left\{X_{K}=x_{K}\right\} \cap \mathcal{E}(g)$ if there exists $x_{j}^{*} \in \mathbb{R}_{>}$such that

$$
\left\{X_{K \cup j}=x_{K \cup j}\right\} \text { is possible under } g \text { if and only if } x_{j}=x_{j}^{*}
$$

Define the set of constant nodes on $\left\{X_{K}=x_{K}\right\}$ as

$$
K^{*}:=K^{*}\left(X_{K}=x_{K}\right):=\left\{j \in V: X_{j} \text { is constant on }\left\{X_{K}=x_{K}\right\}\right\}
$$

and nodes that are constant under $g$ as

$$
K^{*}(g):=K^{*}\left(X_{K}=x_{K}, g\right):=\left\{j \in V: X_{j} \text { is constant on }\left\{X_{K}=x_{K}\right\} \cap \mathcal{E}(g)\right\}
$$

Note that $K \subseteq K^{*} \subseteq K^{*}(g)$ for specific $g \in \mathfrak{G}$. Often these inclusions can be strict (see Example 3.14). The following lemma characterizes these sets. Recall from Theorem 3.3 that each impact graph $g \in \mathfrak{G}$ is a galaxy.

Lemma 3.11. Suppose $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ and $S=V(\sigma)$ is the node set of a star $\sigma$ in the galaxy $g$. Then, either
(a) $S \cap K \neq \emptyset$, in which case $S \subseteq K^{*}(g)$ and we call $S$ a constant star; or
(b) $S \cap K=\emptyset$, in which case $S \cap K^{*}(g)=\emptyset$.

In particular,

$$
K^{*}(g)=\bigcup_{\sigma \in g: S \cap K \neq \emptyset} V(\sigma)
$$

Proof. We first consider (a): Note that if $j \rightarrow i \in g$, then on $\mathcal{E}(g), X_{i}=c_{i j}^{*} Z_{j}$ and thus $X_{i}=c_{i j}^{*} X_{j}$. Therefore, if either $X_{i}$ or $X_{j}$ is constant on $\left\{X_{K}=x_{K}\right\} \cap \mathcal{E}(g)$, then both must be constant. So if one node in $S$ is in $K$, all nodes in $S$ must be in $K^{*}(g)$. This proves (a).

Next we show (b): Let $R$ be the set of root nodes in $g, R^{1} \subset R$ be the set of root nodes for all stars $S$ in $g$ such that $S \cap K=\emptyset$, and $R^{c}=R \backslash R^{1}$ be the set of roots of the constant stars. By the first statement, $X_{r}$ is constant for all $r \in R^{c}$ on $\mathcal{E}(g) \cap\left\{X_{K} \in x_{K}\right\}$. Indeed, on $\mathcal{E}(g) \cap\left\{X_{K}=x_{K}\right\}, M \odot z_{R} \leq z_{R}$ by Lemma 3.6. Furthermore, by the minimal rank condition, we must have strict inequality, that is, $M \odot z_{R}<z_{R}$. This equation splits up into the following lower and upper-bounds for $z_{R^{1}}$ in terms of $z_{R^{c}}$ :

$$
\begin{aligned}
& M_{R^{1} R^{c}} \odot z_{R^{c}}<z_{R^{1}} \\
& M_{R^{c} R^{1}} \odot z_{R^{1}}<z_{R^{c}}
\end{aligned}
$$

Since $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$, the upper and lower bounds cannot coincide. In particular, there exist two values of $x_{r}$ such that $\left\{X_{K \cup r}=x_{K \cup r}\right\}$ is possible under $g$. This implies that $R^{1} \cap K^{*}(g)=\emptyset$, and since $R^{1}$ are the roots, none of their children can be in $K^{*}(g)$. This completes the proof.

Example 3.12 (Bipartite). Consider again the DAG and coefficient matrix of Example 3.4 and let $K=\{3\}$. Figure 8 again displays impact graphs for this DAG, now with the constant nodes shaded. Nodes are constant in the context $\left\{X_{3}=x_{3}\right\}$ if and only if they belong to the same star as the node 3 .

![img-8.jpeg](img-8.jpeg)

Fig 8: Impact graphs in $\mathfrak{G}\left(X_{3}=x_{3}\right)$ for the bipartite DAG in Figures 5 and 7. Red nodes are constant under $g$ for the context $\left\{X_{3}=x_{3}\right\}$, i.e. elements of $K^{*}(g)$. These are nodes that are in the same star as the node 3 .

Lemma 3.13 below identifies a crucial property of a compatible impact graph.
Lemma 3.13. Let $g \in \mathfrak{G}$ be an impact graph. If $g$ is compatible with $\left\{X_{K}=x_{K}\right\}$, we have for all $i, j, h \in V$ that

$$
\begin{aligned}
& \frac{x_{h}}{c_{h j}^{*}}<\frac{x_{i}}{c_{i j}^{*}}, \quad h, i \in K^{*}(g) \quad \Longrightarrow \quad j \neq R_{g}(i) \\
& \exists j \in V: \quad \frac{x_{h}}{c_{h j}^{*}}=\frac{x_{i}}{c_{i j}^{*}}, \quad h, i \in K^{*}(g) \quad \Longrightarrow \quad R_{g}(i)=R_{g}(h)
\end{aligned}
$$

Proof. Consider (3.9). Clearly $j \neq i$; suppose then for contradiction that $j \rightarrow i$. Since $i \in K^{*}(g)$, Lemma 3.11 implies that $j \in K^{*}(g)$. Then $x_{i}=c_{i j}^{*} x_{j}$, so (3.9) implies that $x_{h} / c_{h j}^{*}<x_{i} / c_{i j}^{*}=x_{j}$, so $x_{h}<c_{h j}^{*} x_{j}$. But this contradicts that $x_{h} \geq c_{h j}^{*} x_{j}$. Now consider (3.10). Write $r=R_{g}(i)$ and $r^{\prime}=R_{g}(h)$. Then $x_{i}=c_{i r}^{*} x_{r}$ and $x_{h}=c_{h r^{\prime}}^{*} x_{r^{\prime}}$. Suppose for contradiction that $r \neq r^{\prime}$. Substituting into the hypothesis of (3.10) we get

$$
\frac{c_{h r^{\prime}}^{*}}{c_{h j}^{*}} x_{r^{\prime}}=\frac{c_{i r}^{*}}{c_{i j}^{*}} x_{r}
$$

which is a linear relation on the roots $x_{r}$ and $x_{r^{\prime}}$ of two different stars in $g$. But this contradicts that $g$ has minimal rank according to Definition 3.8 and thus $\left\{X_{K}=x_{K}\right\}$ is not possible under $g$. Hence (3.10) must hold.

Example 3.14 (Half-butterfly). To illustrate Lemma 3.13 we again consider the DAG and coefficient matrix $C$ of Example 3.5, depicted in Figure 6 and the context $\left\{X_{K}=x_{K}\right\}$ where $K=\{4,5\}$ and $x_{4}=x_{5}=1$. We claim that the set of constant nodes is $K^{*}=\{3,4,5\}$ because the events $\left\{X_{4}=X_{5}=1\right\}$ and $\left\{X_{4}=X_{5}=1, X_{3}=1 / 3\right\}$ are almost surely identical, and that there are exactly two impact graphs compatible with this context, depicted in Figure 9.

To see this, let $g$ be a compatible impact graph in $\mathfrak{G}\left(X_{4}=X_{5}=1\right)$. Since $x_{4} / c_{43}^{*}=1 / 3=$ $x_{5} / c_{53}^{*}$ we may apply (3.10) with $i=4, h=5, j=3$ to conclude that 4 and 5 belong to the same star in $g$, with common root $R_{g}(4)=R_{g}(5)$.

By Theorem 3.3(a), $g$ is a subgraph of $\mathcal{D}^{*}(C)$ and hence the roots must be parents in this graph, i.e. we have $R_{g}(4) \in\{1,2,3,4\}$, and $R_{g}(5) \in\{1,2,3,5\}$. So $R_{g}(4)=R_{g}(5)$ implies $R_{g}(4)=R_{g}(5) \in\{1,2,3\}$. On the other hand, it also holds that $x_{5} / c_{52}^{*}=1 / 4<1 / 1.5=$ $x_{4} / c_{42}^{*}$. Then (3.9) implies that $2 \notin \mathrm{pa}_{g}(4)$, so $R_{g}(4)=R_{g}(5) \in\{1,3\}$. By Theorem 3.3(b), $g$ is a star so each node can not have more than one parent. So either it must hold that $R_{g}(4)=R_{g}(5)=1$, or that $R_{g}(4)=R_{g}(5)=3$. In the second case, 1 and 2 are left as isolated roots. In the first case, $1 \rightarrow 4 \in g$ implies that we also have $1 \rightarrow 3 \in g$ by Theorem 3.3(c),

![img-9.jpeg](img-9.jpeg)

Fig 9: Impact graphs $g_{3}$ and $g_{4}$ for the half-butterfly compatible with the context $\left\{X_{4}=X_{5}=1\right\}$ are displayed to the right. To the left, the original $\operatorname{DAG} \mathcal{D}(C)$ and its weighted reachability DAG $\mathcal{D}^{*}(C)$ are shown.
that is, 3 must belong to the same star as 4 with 1 as a root. This gives the two impact graphs to the right in Figure 9. In both cases, there is at most one non-isolated root, so $M(g)$ has no cycles and thus $\lambda(M(g))=0<1$ required for $g$ to be an impact graph. Thus both graphs are in $\mathfrak{G}\left(X_{4}=X_{5}=1\right)$. By Definition 3.10 the constant nodes are those that are in the same star as 4,5 in the compatible impact graphs, so $K^{*}=\{3,4,5\}$ as we then have $X_{3}=1 / 3$ on $\left\{X_{4}=X_{5}=1\right\}$, so $\left\{X_{4}=X_{5}=1\right\}=\left\{X_{4}=X_{5}=1, X_{3}=1 / 3\right\}$.

We can double-check that $\mathfrak{G}\left(X_{4}=X_{5}=1\right)=\mathfrak{G}\left(X_{4}=X_{5}=1, X_{3}=1 / 3\right)$ by computing the latter set of graphs directly. Let $g \in \mathfrak{G}\left(X_{4}=X_{5}=1, X_{3}=1 / 3\right)$. Now we first apply (3.10) with $i=j=3$ and $h=5$ to conclude that $R_{g}(3)=R_{g}(5)$. Thus again we have by Theorem 3.3(a) that $R_{g}(3) \in\{1,2,3\}$ and $R_{g}(5) \in\{1,2,3,5\}$. Therefore, $R_{g}(5) \neq 5$. Apply again (3.9) with $j=2, i=3$ and $h=5$ to conclude that $2 \neq R_{g}(3)$. So $R_{g}(3) \in\{1,3\}$. The two cases $R_{g}(3)=1$ and $R_{g}(3)=3$ yield the two impact graphs to the right in Figure 9 as expected.

Remark 3. Although in Definition 3.1 we have defined the impact graph $G=G(Z)$ (for almost all $Z), G$ can also be expressed in terms of $X$, as we indeed have for any $g \in \mathfrak{G}$ which is compatible with $\{X=x\}$ that

$$
j \rightarrow i \in g \Longrightarrow x_{i} / x_{j}=c_{i j}^{*} \text { on } \mathcal{E}(g)
$$

since on $\mathcal{E}(g)$ we must have $j \in R(g)$ and thus $X_{j}=Z_{j}$. Hence with probability one there is a unique $g \in \mathfrak{G}$ that is compatible with $\{X=x\}$. Another way of expressing this is to say that the map $z \rightarrow g$ is almost surely $\sigma(X)$-measurable, where $\sigma(X)$ is the $\sigma$-algebra generated by the max-linear map $z \rightarrow x$ given by $x=C^{*} \odot z$.
3.3. The source $D A G$. Impact graphs describe how extreme events at their roots spread deterministically to other nodes. In this section we shall capitalize on this, but from the perspective of identifying which are the possible sources of extreme values responsible for a given possible context of the form $\left\{X_{K}=x_{K}\right\}$ (see Definition 3.8(c)). This will eventually make it possible for us to answer interesting queries concerning conditional independence.

We first let $\mathcal{I}\left(X_{K}=x_{K}\right)$ denote the union of impact graphs which are compatible with the context:

$$
\mathcal{I}\left(X_{K}=x_{K}\right)=\bigcup_{g \in \mathfrak{G}\left(X_{K}=x_{K}\right)} g
$$

![img-10.jpeg](img-10.jpeg)

Fig 10: Tent graph: To the left, this displays $\mathcal{D}(C)=\mathcal{D}^{*}(C)=\mathcal{I}\left(X_{K}=x_{K}\right)$ when all coefficients are equal to 1 . To the right, the source $\operatorname{DAG} \mathcal{C}\left(X_{K}=x_{K}\right)$ for $K=\{4,5\}$ and $x_{4}=x_{5}=2$ is obtained by removing the dashed edges, which are redundant as each of the dotted nodes is constant in any impact graph containing the edge.
and we shall refer to this as the total impact graph and note that it is a subgraph of the reachability DAG $\mathcal{D}^{*}$. In other words, this graph yields all possible ways that impact could have spread across the network in a way that conforms with the observation $\left\{X_{K}=x_{K}\right\}$.

Definition 3.15. Let $K \subset V$ and $K^{*}(g)$ be the set of constant nodes under $g$ as in Definition 3.10. An edge $j \rightarrow i$ in $\mathcal{I}\left(X_{K}=x_{K}\right)$ is redundant in the context $\left\{X_{K}=x_{K}\right\}$ if either

- $j \in K^{*}$, or
- $i \notin K^{*}$ and $X_{j}$ is constant under all $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ that contain the edge.

The set of redundant edges is denoted $E^{-}=E^{-}\left(X_{K}=x_{K}\right)$.
Definition 3.16. The source $D A G \mathcal{C}\left(X_{K}=x_{K}\right)$ of a possible context $\left\{X_{K}=x_{K}\right\}$ is the graph obtained from $\mathcal{I}\left(X_{K}=x_{K}\right)$ by removing redundant edges; see Definition 3.15.

Example 3.17 (Tent). Consider the DAG $\mathcal{D}$ to the left in Figure 10 with all edge weights $c_{i j}=1$. Let $K=\{4,5\}$ and $x_{4}=x_{5}=2$. Note that $\mathcal{I}\left(X_{K}=x_{K}\right)=\mathcal{D}(C)$. However, $\mathcal{C}\left(X_{K}=x_{K}\right)$ is the strict subgraph of $\mathcal{I}\left(X_{K}=x_{K}\right)$ obtained by removing the dashed edges from the graph to the right in Figure 10.

The edge $1 \rightarrow 3$ is in $E^{-}$since 1 is constant under all impact graphs containing this edge, and similarly with the edge $2 \rightarrow 3$. To see this, note that $1 \rightarrow 3 \in g \in \mathfrak{G}\left(X_{4}=X_{5}=2\right)$ if and only if $1 \rightarrow 4,1 \rightarrow 5 \in g$, which then implies $1 \in K^{*}(g)$. Therefore, $1 \rightarrow 3$ is a redundant edge and not included in $\mathcal{C}\left(X_{4}=X_{5}=2\right)$. A similar argument applies to the edge $2 \rightarrow 3$. From the node partition of Proposition 3.18 below we see that the active nodes are $A=\{1,2,3\}$ and the constant nodes $K^{*}=K=L=\{4,5\}$.

We first prove some results on the structure of the source DAG before linking it up to probabilistic statements. In particular we establish that the source DAG admits a nice partition structure, see Figure 11 for an illustration.

Proposition 3.18. Fix a possible context $\left\{X_{K}=x_{K}\right\}$, let $\mathcal{I}=\mathcal{I}\left(X_{K}=x_{K}\right)$ and $\mathcal{C}=$ $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the corresponding total impact graph and source DAG, respectively. Then for either of these graphs, its node set $V$ can be partitioned into disjoint sets $A \cup U \cup H \cup L$, where
(a) $A: a \in A \Longleftrightarrow a \notin K^{*}$ is the set of active nodes (non-constant);

(b) $U: u \in U \Longleftrightarrow u \in K^{*}$ and $\exists k \in K^{*}, k \neq u$ such that $x_{u}=c_{u k}^{*} x_{k}$
(c) $H: h \in H \Longleftrightarrow h \in K^{*}$ and $\exists g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $h \in R(g)$, and
(d) $L: \ell \in L \Longleftrightarrow \ell \in K^{*} \backslash(H \cup U)$

In addition, we have the following.
(e) For all $k \in H \cup L, \mathrm{pa}_{\mathcal{C}}(k)=\mathrm{pa}_{\mathcal{I}}(k)$.
(f) For $k, k^{\prime} \in H \cup L, k \neq k^{\prime}$, either $\mathrm{pa}_{\mathcal{C}}(k) \cap \mathrm{pa}_{\mathcal{C}}\left(k^{\prime}\right)=\emptyset$ or $\mathrm{pa}_{\mathcal{C}}(k)=\mathrm{pa}_{\mathcal{C}}\left(k^{\prime}\right) \neq \emptyset$.
(g) If $h \in H$, then $\mathrm{pa}_{\mathcal{C}}(h) \cap \mathrm{pa}_{\mathcal{C}}(k)=\emptyset$ for all $k \in H \cup L, k \neq h$.
(h) The set $H \cup L$ can be partitioned into equivalence classes where $k \equiv k^{\prime} \Longleftrightarrow \mathrm{pa}_{\mathcal{C}}(k)=$ $\mathrm{pa}_{\mathcal{C}}\left(k^{\prime}\right)$. Under this equivalence relation, elements of $H$ are singletons, and $L$ is partitioned into disjoint subsets $L=L_{1} \cup \cdots \cup L_{m}$.
(i) Any $\ell \in L$ has at least two parents.
(j) For all $a \in A$ and $\ell \in L$, there exists some $i \in \mathrm{pa}_{\mathcal{C}}(\ell)$ such that $i \notin \mathrm{pa}_{\mathcal{C}}(a)$.

Proof. By definition, $V=A \cup U \cup H \cup L$, and all pairs are mutually disjoint except for possibly $U$ and $H$. Indeed, suppose $u \in U$. Let $k \in K^{*}$ be such that $x_{u}=c_{u k}^{*} x_{k}, k \neq u$. Let $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. By (3.10), $R_{g}(u)=R_{g}(k)$. But $\mathcal{D}$ is a DAG, so $c_{u k}^{*}>0$ implies $c_{k u}^{*}=0$, so in particular, $u \neq R_{g}(k)$, hence, $u$ cannot be a root in $g$. Thus $u \notin H$, so $U \cap H=\emptyset$. This proves (a) to (d). Consider (e). By definition, $\mathrm{pa}_{\mathcal{C}}(k) \subseteq \mathrm{pa}_{\mathcal{I}}(k)$. Suppose for contradiction that the containment is strict, that is, there exists some $i \in V$ such that $i \rightarrow k \in \mathcal{I}$ but $i \rightarrow k \notin \mathcal{C}$. Then $i \rightarrow k \in E^{-}$. Since $k \in K^{*}$, we must have $i \in K^{*}$. Then $k \in U$, so $k \notin H \cup L$, a contradiction. This proves (e). Consider (f). Let $k, k^{\prime}$ be two such nodes. Let $i \in \mathrm{pa}_{\mathcal{C}}(k) \cap \mathrm{pa}_{\mathcal{C}}\left(k^{\prime}\right)$. If this set is empty then we are done. Otherwise, consider $x_{k} / c_{k i}^{*}$ and $x_{k^{\prime}} / c_{k^{\prime} i}^{*}$. If one of these two quantities are bigger, then either $i \rightarrow k$ or $i \rightarrow k^{\prime}$ is not in $g$ for all $g \in \mathfrak{G}\left(X_{K}=x_{k}\right)$ by (3.9), so $i \notin \mathrm{pa}_{\mathcal{C}}(k) \cap \mathrm{pa}_{\mathcal{C}}\left(k^{\prime}\right)$. So these two quantities must be equal. By (3.10), for all $g \in \mathfrak{G}\left(X_{K}=x_{K}\right), \mathrm{pa}_{g}(k)=\mathrm{pa}_{g}\left(k^{\prime}\right)$. Thus $\mathrm{pa}_{\mathcal{I}}(k)=\mathrm{pa}_{\mathcal{I}}\left(k^{\prime}\right)$. Since $k, k^{\prime} \in H \cup L$, (e) then implies (f). Now consider (g). Suppose for contradiction that there exists some $k \in H \cup L$ such that $\mathrm{pa}_{\mathcal{C}}(h)=\mathrm{pa}_{\mathcal{C}}(k)$. As argued previously, this implies $h$ and $k$ cannot be the root of any $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. So in particular, $h \notin H$, and we obtain the desired contradiction. Statement (h) follows immediately from (f) and (g). Now we prove (i). Suppose for contradiction that $\ell \in L$ has only one parent $i \in V$. Since $i \rightarrow \ell \notin E^{-}$, $i \rightarrow \ell \in \mathcal{I}\left(X_{K}=x_{K}\right)$. In other words, for all $g \in \mathfrak{G}\left(X_{K}=x_{K}\right), R_{g}(\ell)=i$. By Lemma 3.11(a), this implies $i \in K^{*}$, so $\ell \in U$, a contradiction, as desired. Now we prove (j). Suppose for contradiction that there exists some $a \in A$ and $\ell \in L$ such that $\mathrm{pa}_{\mathcal{C}}(\ell) \subseteq \mathrm{pa}_{\mathcal{C}}(a)$. Let $r \in \mathrm{pa}_{\mathcal{C}}(\ell)$ be a node with smallest coefficient $c_{a j}^{*} x_{\ell} / c_{\ell j}^{*}$ among $j \in \mathrm{pa}_{\mathcal{C}}(\ell)$, that is,

$$
c_{a r}^{*} \frac{x_{\ell}}{c_{\ell r}^{*}} \leq c_{a j}^{*} \frac{x_{\ell}}{c_{\ell j}^{*}} \text { for all } j \in \mathrm{pa}_{\mathcal{C}}(\ell)
$$

Since $r \rightarrow a \in \mathcal{C}\left(X_{K}=x_{K}\right)$, there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $r \rightarrow a \in g$ and $r \notin K^{*}(g)$. Thus this implies $r \rightarrow \ell \notin g$, so there exists some $j \in \mathrm{pa}_{\mathcal{C}}(\ell)$ with $j \rightarrow \ell \in g$. Since $g$ is a galaxy, $j \rightarrow a \notin g$. Then by definition, on the event $\mathcal{E}(g), j \rightarrow \ell \in g$ and $r \rightarrow \ell \notin g$ together imply

$$
x_{\ell}=c_{\ell j}^{*} Z_{j}>c_{\ell r}^{*} Z_{r}
$$

Rearranging gives

$$
c_{a j}^{*} Z_{j}=c_{a j}^{*} \frac{x_{\ell}}{c_{\ell j}^{*}} \geq c_{a r}^{*} \frac{x_{\ell}}{c_{\ell r}^{*}}>c_{a r}^{*} Z_{r}
$$

![img-11.jpeg](img-11.jpeg)

Fig 11: Illustration of the partition in Proposition 3.18. Nodes in $H$ and $L$ are gray, nodes in $U$ are filled with blue lines. Active nodes $A$ are white or dotted burgundy, where the dotted nodes are parents of constant nodes in $K=H \cup L \cup U$. All edges, including the dashed edges, are in $\mathcal{I}\left(X_{K}=x_{K}\right)$, while only the solid edges are in $\mathcal{C}\left(X_{K}=x_{K}\right)$.
but this contradicts the fact that $j \rightarrow a \notin g$ and $r \rightarrow a \notin g$, since these two imply

$$
X_{a}=c_{a j^{\prime}}^{*} Z_{j^{\prime}}<c_{a r}^{*} Z_{r}
$$

So we have a contradiction, as needed.
The nodes in $U$ have no direct effect on the conditional distribution, as their effect is mitigated through their (constant) parents. Proposition 3.18 is illustrated in Figure 11.

Corollary 3.19. Let $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the source $D A G$ of a possible context $\left\{X_{K}=x_{K}\right\}$ and consider the node partition $V=A \cup K^{*}=A \cup H \cup L \cup U$ as given by Proposition 3.18. If $j \rightarrow i \in g$ for some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right), j, i \notin K^{*}$ and $j \in K^{*}(g)$, then $j \rightarrow h \in g$ for some $h \in H \cup L$.

Proof. Let $S=V(\sigma) \subseteq V$ be the set of nodes in the star $\sigma$ with root $j$ in the galaxy $g$. Since $\mathfrak{G}\left(X_{K}=x_{K}\right)=\mathfrak{G}\left(X_{K^{*}}=x_{K^{*}}\right)$, apply Lemma 3.11(a) to $\mathfrak{G}\left(X_{K^{*}}=x_{K^{*}}\right)$ giving $S \cap K^{*} \neq \emptyset$. Let $u \in S \cap K^{*}$. If $u \notin U$, then take $h=u$ and we are done. Else, by Proposition 3.18, there exist some $h \neq u, h \in K^{*}$ such that $x_{u}=c_{u h}^{*} x_{h}$. By Theorem 3.3(c), $j \rightarrow h \in g$, so $h \in S \cap K^{*}$. If $h \notin U$ then we are done, else we repeat the above argument once more to find another node in $S \cap K^{*}$. Since $\mathcal{D}$ is a DAG, every time we repeat this argument we obtain a new node. Since the graph is finite, this procedure eventually terminates and returns some node $h \in S \cap K^{*}$ and $h \notin U$. By Proposition 3.18, $h \in K \cup L$.
4. Representing the conditional distribution. Before we derive conditional independence results, we need to have a good control of conditional distributions in a max-linear Bayesian network. We first derive a basic representation in Section 4.1 and subsequently a more compact representation without redundancy in Section 4.2.

4.1. Basic representation. Let $K \subset V$ and $\bar{K}=V \backslash K$. The conditional distribution of $X_{\bar{K}} \mid X_{K}=x_{K}$ can be represented by a system of max-linear equations in the $Z_{\bar{K}}$ variables; more precisely, we have:

Proposition 4.1. The following is a representation for $X \mid X_{K}=x_{K}$ with respect to the innovations $Z$

$$
X_{\bar{K}}=C_{\bar{K} K}^{*} \odot x_{K} \vee C_{\overline{K K}}^{*} \odot Z_{\bar{K}}
$$

where the distribution of $Z$ is that of independent components, conditioned to satisfy

$$
x_{K}=C_{K K}^{*} \odot Z_{K} \vee C_{K \bar{K}}^{*} \odot Z_{\bar{K}}
$$

Proof. By (2.5) we have $X=C^{*} \odot X$ so

$$
X \geq\left[\begin{array}{cc}
0 & 0 \\
C_{\bar{K} K}^{*} & 0
\end{array}\right] \odot\left[\begin{array}{l}
X_{K} \\
X_{\bar{K}}
\end{array}\right]
$$

Now, $X=C^{*} \odot Z$, therefore,

$$
X=\left[\begin{array}{cc}
0 & 0 \\
C_{\bar{K} K}^{*} & 0
\end{array}\right] \odot\left[\begin{array}{l}
X_{K} \\
X_{\bar{K}}
\end{array}\right] \vee C^{*} \odot Z \quad \text { and } \quad X=\left[\begin{array}{ll}
C_{K K}^{*} & C_{K \bar{K}}^{*} \\
C_{\bar{K} K}^{*} & C_{\bar{K} \bar{K}}^{*}
\end{array}\right] \odot\left[\begin{array}{l}
Z_{K} \\
Z_{\bar{K}}
\end{array}\right]
$$

Writing out these equations, we obtain

$$
\begin{aligned}
X_{\bar{K}} & =C_{\bar{K} K}^{*} \odot x_{K} \vee C_{\bar{K} K}^{*} \odot Z_{K} \vee C_{\overline{K K}}^{*} \odot Z_{\bar{K}} \\
x_{K} & =C_{K K}^{*} \odot Z_{K} \vee C_{K \bar{K}}^{*} \odot Z_{\bar{K}}
\end{aligned}
$$

The second equation is (4.2). For the first equation, note that $c_{i i}^{*}=1$ for all $i$, so $x_{K} \geq Z_{K}$. Thus $C_{\bar{K} K}^{*} \odot x_{K} \vee C_{\bar{K} K}^{*} \odot Z_{K}=C_{\bar{K} K}^{*} \odot x_{K}$, so (4.3) is equivalent to (4.1). Thus the context $\left\{X_{K}=x_{K}\right\}$ is equal to the conjunction of the events (4.2) and (4.4). The result follows.

Example 4.2. We shall illustrate Proposition 4.1 for the Cassiopeia graph of Figure 2 in Example 1.2. Assume that we have $c_{j i}=c_{j i}^{*}=1$ for all edges in this DAG and let $x_{K}=\left(x_{4}, x_{5}\right)$. Then (4.1) becomes

$$
\left[\begin{array}{l}
X_{1} \\
X_{2} \\
X_{3}
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0 \\
0 & 0
\end{array}\right] \odot\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right] \vee I_{3} \odot\left[\begin{array}{l}
Z_{1} \\
Z_{2} \\
Z_{3}
\end{array}\right]=\left[\begin{array}{l}
Z_{1} \\
Z_{2} \\
Z_{3}
\end{array}\right]
$$

whereas (4.2) becomes

$$
\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right] \odot\left[\begin{array}{l}
Z_{4} \\
Z_{5}
\end{array}\right] \vee\left[\begin{array}{lll}
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right] \odot\left[\begin{array}{l}
Z_{1} \\
Z_{2} \\
Z_{3}
\end{array}\right]
$$

This means that $x_{4} \geq Z_{4}, x_{5} \geq Z_{5}$ and

$$
\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right] \geq\left[\begin{array}{lll}
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right] \odot\left[\begin{array}{l}
Z_{1} \\
Z_{2} \\
Z_{3}
\end{array}\right]=\left[\begin{array}{l}
Z_{1} \vee Z_{2} \\
Z_{2} \vee Z_{3}
\end{array}\right]
$$

Depending on whether $x_{4}<x_{5}, x_{4}>x_{5}$, or $x_{4}=x_{5}$, these inequalities are a.s. equivalent to respectively

$$
\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right] \geq\left[\begin{array}{c}
Z_{1} \vee Z_{2} \\
Z_{3}
\end{array}\right], \quad\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right] \geq\left[\begin{array}{c}
Z_{1} \\
Z_{2} \vee Z_{3}
\end{array}\right], \quad\left[\begin{array}{l}
x_{4} \\
x_{5}
\end{array}\right] \geq\left[\begin{array}{l}
Z_{1} \\
Z_{3}
\end{array}\right] \text { and } Z_{2}=x_{4}=x_{5}
$$

Thus the conditioning under this restriction renders $Z_{i}$ bounded in all cases, and in the third case $Z_{2}$ becomes constant. Note also that in these reduced inequalities, $Z_{1}$ and $Z_{3}$ never occur together in any inequality, rendering $X_{1} \Perp X_{3} \mid X_{\{4,5\}}$.
4.2. Compact representation. The main result of this section, Theorem 4.3, states that the source DAG gives a representation of the active nodes $X_{A} \mid X_{K}=x_{K}$ with respect to the innovations $Z$. Compared to the representation of the conditional distribution in Proposition 4.1, this is a representation with fewer terms. Most importantly, we shall show below that the system of equations involving $Z$ can be separated into blocks where no terms are redundant.

THEOREM 4.3. Let $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the source $D A G$ of a possible context $\left\{X_{K}=x_{K}\right\}$, with node partition $V=A \cup H \cup L \cup U=A \cup H \cup\left(L_{1} \cdots \cup L_{m}\right) \cup U$ as in Proposition 3.18. For each $t=1, \ldots, m$, select a node $\ell_{t} \in L_{t}$. Then the following system of equations yields a representation for $X_{A} \mid X_{K}=x_{K}$ with respect to $Z$ :

$$
X_{a}=\alpha_{a} \vee Z_{a} \vee \bigvee_{j \in \mathrm{pac}(a)} c_{a j}^{*} Z_{j}, \quad a \in A
$$

where the constants $\alpha_{a}$ are given by

$$
\alpha_{a}=\bigvee_{k \in K^{*}} c_{a k}^{*} x_{k} \vee\left(\bigvee_{\substack{j \in A \\ j \rightarrow a \in E^{-}}} \bigvee_{k \in \operatorname{ch}_{\mathcal{D}}(j) \cap(H \cup L)} c_{a j}^{*} \frac{x_{k}}{c_{k j}^{*}}\right), \quad a \in A
$$

and the distribution of $Z$ is that of independent components, conditioned to satisfy the bounds

$$
Z_{i} \leq \bigwedge_{k \in K^{*} ; c_{k i}^{*}>0} \frac{x_{k}}{c_{k i}^{*}}, \quad i \in V
$$

as well as the equations

$$
\begin{aligned}
& x_{h}=Z_{h} \vee \bigvee_{j \in \mathrm{pac}(h)} c_{h j}^{*} Z_{j}, \quad h \in H \\
& x_{\ell_{t}}=\bigvee_{j \in \mathrm{pac}_{\mathcal{C}}\left(\ell_{t}\right)} c_{\ell_{t} j}^{*} Z_{j}, \quad t=1, \ldots, m
\end{aligned}
$$

Furthermore, each innovation term on the right-hand side of (4.5), (4.8) and (4.9) has positive probability of being the term that achieves equality.

Proof. We shall begin with the representation of $X \mid X_{K}=x_{K}$ given by Proposition 4.1 and then simplify terms until we obtain the representation above. The contexts $\left\{X_{K}=x_{K}\right\}$

and $\left\{X_{K^{*}}=x_{K^{*}}\right\}$ are clearly equivalent, so we may without loss of generality assume that $K=K^{*}$ and $A=\bar{K}$. This gives for (4.1) and (4.2) the representations

$$
\begin{aligned}
X_{A} & =C_{A K^{*}}^{*} \odot x_{K^{*}} \vee C_{A A}^{*} \odot Z_{A} \\
x_{K^{*}} & =C_{K^{*} K^{*}}^{*} \odot Z_{K^{*}} \vee C_{K^{*} A}^{*} \odot Z_{A}
\end{aligned}
$$

First we simplify (4.11). With $K^{*}=H \cup L \cup U$ we expand this system of equations as follows:

$$
\begin{aligned}
x_{H} & =C_{H K^{*}}^{*} \odot Z_{K^{*}} \vee C_{H A}^{*} \odot Z_{A} \\
x_{L} & =C_{L K^{*}}^{*} \odot Z_{K^{*}} \vee C_{L A}^{*} \odot Z_{A} \\
x_{U} & =C_{U K^{*}}^{*} \odot Z_{K^{*}} \vee C_{U A}^{*} \odot Z_{A}
\end{aligned}
$$

For each $i \in V$ and each $k \in K^{*}$, all inequalities on $Z_{i}$ implied by (4.11) are

$$
x_{k} \geq c_{k i}^{*} Z_{i}
$$

whenever $c_{k i}^{*}>0$, and in particular this is equivalent to (4.7).
Next we keep track of the equalities. For $u \in U$, by Proposition 3.18, $x_{u}=c_{u k}^{*} x_{k}$ for some $k \in K^{*}, k \neq u$. We have

$$
\begin{aligned}
x_{u} & =c_{u k}^{*} x_{k} \\
& =c_{u k}^{*} C_{k K^{*}}^{*} \odot Z_{K^{*}} \vee c_{u k}^{*} C_{k A}^{*} \odot Z_{A} \quad \text { by (4.11) } \\
& \leq C_{u K^{*}}^{*} \odot Z_{K^{*}} \vee C_{u A}^{*} \odot Z_{A} \\
& =x_{u} \quad \text { by }(4.11)
\end{aligned}
$$

Thus we conclude

$$
C_{u K^{*}}^{*} \odot Z_{K^{*}} \vee C_{u A}^{*} \odot Z_{A}=c_{u k}^{*}\left(C_{k K^{*}}^{*} \odot Z_{K^{*}} \vee C_{k A}^{*} \odot Z_{A}\right), \quad k \in K^{*}, k \neq u
$$

whence the constraint imposed upon $Z$ by $x_{u}$ is identical to the constraint imposed upon $Z$ by $x_{k}$. Therefore all equations in (4.14) are redundant. So (4.11) is equivalent to the conjunction of (4.12) and (4.13).

Next we simplify the terms that appear on the right-hand side of (4.12) and (4.13). Fix $k \in H \cup L$. By definition of the source DAG, we keep a term $c_{k i}^{*} Z_{i}$ for $i \neq k$ if and only if $i \rightarrow k \in g$ for some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$, and we keep the term $c_{k k}^{*} Z_{k}=Z_{k}$ if and only if $k \in R(g)$ for some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. Since each $g$ is a galaxy, each remaining term has a positive probability of achieving the maximum. Since each event under $\mathfrak{G}\left(X_{K}=x_{K}\right)$ with positive probability must correspond to some $g$, there is always one that achieves the maximum among the remaining terms. Since $k \in K^{*}$, it holds that $i \rightarrow k \in g$ for some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ if and only if we also have $i \rightarrow k \in \mathcal{C}\left(X_{K}=x_{K}\right)$. Therefore, by Proposition 3.18, (4.12) simplifies to (4.8), and (4.13) simplifies to

$$
x_{\ell}=\bigvee_{j \in \mathrm{pa}_{\mathcal{C}}(\ell)} c_{\ell j}^{*} Z_{j}
$$

Write $L=L_{1} \cup \cdots \cup L_{m}$ as given by Proposition 3.18. If $\ell, \ell^{\prime} \in L_{t}$ for some $t=1, \ldots, m$, then they share the same set of parents. By Lemma 3.13, this implies

$$
\frac{x_{\ell}}{c_{\ell j}^{*}}=\frac{x_{\ell^{\prime}}}{c_{\ell^{\prime} j}^{*}}
$$

for all $j \in \mathrm{pa}_{\mathcal{C}}(\ell)=\mathrm{pa}_{\mathcal{C}}\left(\ell^{\prime}\right)$. So (4.15) for $x_{\ell}$ and $x_{\ell^{\prime}}$ are constant multiples of each other. So for each $t=1, \ldots, m(4.15)$ for all $\ell \in L_{t}$ is equivalent to the single equation (4.9).

Now we simplify (4.10). Like in the previous step, we can for $a, j \in A$ drop terms $c_{a j}^{*} Z_{j}$ where $j \rightarrow a \notin g$ for every $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. This gives

$$
X_{a}=C_{a K^{*}}^{*} \odot x_{K^{*}} \vee\left(\bigvee_{j \in A, j \rightarrow a \in E^{-}} c_{a j}^{*} Z_{j}\right) \vee Z_{a} \vee \bigvee_{j \in \mathrm{pa}_{\mathcal{C}}(a)} c_{a j}^{*} Z_{j}, \quad a \in A
$$

Now we argue that each term in $\bigvee_{j \in A, j \rightarrow a \in E^{-}} c_{a j}^{*} Z_{j}$ can be replaced by an appropriate constant. Let $j \in A$ be a node with $j \rightarrow a \in E^{-}$. Let $\mathcal{E}$ be the sub-event of $\mathfrak{G}\left(X_{K}=x_{K}\right)$ where $j$ is the root of $a$, that is,

$$
\mathcal{E}=\bigcup\left\{\mathcal{E}(g): g \in \mathfrak{G}\left(X_{K}=x_{K}\right), j \rightarrow a \in g\right\}
$$

By definition, for each $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j \rightarrow a \in g$, we have that $a, j \in K^{*}(g)$. Since $a, j \notin K^{*}(g)$, it follows that there exists some $k=k(g) \in K^{*}(g)$ such that $j \rightarrow k \in g$. Thus, on the event $\mathcal{E}(g) \cap\left\{X_{K}=x_{K}\right\}$, we have

$$
X_{a}=c_{a j}^{*} Z_{j}=c_{a j}^{*} \frac{x_{k(g)}}{c_{k(g) j}^{*}}, \quad a \in A
$$

By Corollary 3.19, we may assume that $k(g) \in H \cup L$. Therefore, on $\mathcal{E}$,

$$
X_{a}=\bigvee_{k \in \operatorname{ch}_{\mathcal{D}}(j) \cap(H \cup L)} c_{a j}^{*} \frac{x_{k}}{c_{k j}^{*}}, \quad a \in A
$$

By definition of $\mathcal{E}$, on the complement $\left\{X_{K}=x_{K}\right\} \backslash \mathcal{E}, X_{a}>c_{a j}^{*} Z_{j}$. Therefore, the term $c_{a j}^{*} Z_{j}$ can be dropped from the representation of $X_{a}$ and be replaced by the right-hand side of (4.16). This gives

$$
X_{a}=C_{a K^{*}}^{*} \odot x_{K^{*}} \vee\left(\bigvee_{j \in A, j \rightarrow a \in E^{-}} \bigvee_{k \in \operatorname{ch}_{\mathcal{D}}(j) \cap(H \cup L)} c_{a j}^{*} \frac{x_{k}}{c_{k j}^{*}}\right) \vee Z_{a} \vee \bigvee_{j \in \mathrm{pa}_{\mathcal{C}}(a)} c_{a j}^{*} Z_{j}, \quad a \in A
$$

This is (4.5), with $\alpha_{a}$ equal to the constant terms in the equation above, which is the formula in (4.6). Finally, by definition of $\mathcal{C}\left(X_{K}=x_{K}\right)$, for each $j \in \mathrm{pa}_{\mathcal{C}}(i)$ there exists some $g \in$ $\mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j \rightarrow i$ and $j \notin K^{*}(g)$. Since $g$ is a galaxy and $X_{i}$ is not constant on the event $\mathcal{E}(g) \cap\left\{X_{K}=x_{K}\right\}$, on this event, $c_{i j}^{*} Z_{j}$ is the unique term that achieves the maximum in (4.5).

Remark 4. We note that in (4.7), only the bounds for the variables $Z_{A \cup H}$ are directly relevant for the conditional distribution of $X_{A}$ given $X_{K}=x_{K}$, as the variables $Z_{L \cup U}$ do not enter into any of the equations (4.5), (4.6), (4.8), or (4.9). However, we have included these in Theorem 4.3 to provide a full description of the conditional distribution of $Z$ given $X_{K}=x_{K}$, which may be of interest for other purposes.

The following example of an umbrella graph illustrates some aspects of this representation.

![img-12.jpeg](img-12.jpeg)

Fig 12: The umbrella graph: To the left, $\mathcal{D}(C)=\mathcal{D}^{*}(C)=\mathcal{D}_{K}^{*}(C)$; to the right: the source DAG $\mathcal{C}\left(X_{K}=x_{K}\right)$ for $K=\{6,7\}$ and $x_{6}=x_{7}=3$. Black edges have weights 1 , dash-dotted blue edges have weights 2 .

Example 4.4 (Umbrella). Consider the graph to the left in Figure 12 where solid black edges have weights 1 and dash-dotted blue edges have weights 2 . The partition in Theorem 4.3 yields nodes $A=V \backslash K^{*}=V \backslash K=\{1,2,3,4,5\}$, and $K=L=\{6,7\}$. The non-zero constants (4.6) in the representation of the active variables are $\alpha_{2}=\alpha_{3}=3$, calculated as

$$
\alpha_{2}=0 \vee \bigvee_{5: 5 \rightarrow 2} \bigvee_{k \in\{6,7\}} c_{25}^{*} \frac{x_{k}}{c_{k 5}^{*}}=\max (3,3)=3
$$

since $c_{2 k}^{*}=0$ for $k=6,7$ and there is only one edge $5 \rightarrow 2 \in E^{-}$pointing to 2 . A similar calculation yields $\alpha_{3}=3$. The full representation (4.5) then becomes

$$
\begin{aligned}
& X_{1}=Z_{1}, \quad X_{4}=Z_{4}, \quad X_{5}=Z_{5} \\
& X_{2}=3 \vee Z_{2} \vee 2 Z_{1} \vee 2 Z_{4} \\
& X_{3}=3 \vee Z_{3} \vee 2 Z_{1} \vee 2 Z_{5}
\end{aligned}
$$

with inequalities from (4.7) yielding the bounds $Z_{1}, Z_{4}, Z_{5} \leq 3$ (and $Z_{6}, Z_{7} \leq 3$ ). Further, we have the equality (4.9) yielding

$$
x_{6}=x_{7}=3=Z_{4} \vee Z_{5}
$$

whereas (4.8) is void.
For $Z_{1}$, we claim that it cannot simultaneously achieve the bound in both of the equations for $X_{2}$ and $X_{3}$, illustrating Proposition 3.18(g). In fact, if $X_{2}=2 Z_{1}$ then $3<2 Z_{1} \leq 6$, so that $2 Z_{4}<2 Z_{1} \leq 6$. Then (4.17) yields that $Z_{4}<3$ and thus $Z_{5}=3$, but then $X_{3}=$ $6>2 Z_{1}$. Moreover, since $Z_{4}$ and $Z_{5}$ both enter into the equation (4.17) we conclude that $X_{2} \Perp X_{3} \mid X_{\{6,7\}}=(3,3)$.

We next present some important consequences of Theorem 4.3, enabling us to identify conditional independencies.

Corollary 4.5. For each pair $i, j \in V$, either $Z_{i}, Z_{j}$ appear together in exactly one equation among those in (4.8) and (4.9), or they do not appear together in any of those equations. In the first case they are conditionally dependent, i.e. $Z_{i} \Perp Z_{j} \mid X_{K}=x_{K}$. In the second case they are conditionally independent, i.e. $Z_{i} \Perp Z_{j} \mid X_{K}=x_{K}$.

Proof. By Theorem 4.3, the distribution of $Z \mid X_{K}=x_{K}$ is the distribution of $Z$ given the events defined by (4.7), (4.8), and (4.9). The bounds (4.7) only involve one variable at a time and thus play no role for independence issues. Groups of $Z$ 's that appear in different equations in (4.8) and (4.9) are independent. It remains to show that, if $Z_{i}, Z_{j}$ appear in the same equation, then they are dependent. Indeed, suppose that $Z_{i}, Z_{j}$ appear in (4.8) for some $h \in H$, with coefficients $a_{i}, a_{j}>0$. The event $\mathcal{E}_{h}$ defined by this equation can be rewritten as

$$
a_{i} Z_{i} \leq x_{h}, a_{j} Z_{j} \leq x_{h} \quad \text { or } \quad a_{i} Z_{i} \leq x_{h}, a_{j} Z_{j} \leq x_{h}, a_{j^{\prime}} Z_{j^{\prime}} \leq x_{h} \text { for some other } j^{\prime} \in \mathrm{pa}_{\mathcal{C}}(h)
$$

and exactly one of these terms achieves equality. Further, each term has a positive probability of achieving equality. That is,

$$
\mathbb{P}\left(a_{i} Z_{i}=x_{h} \mid \mathcal{E}_{h}\right)>0 \text { and } \mathbb{P}\left(a_{j} Z_{j}=x_{h} \mid \mathcal{E}_{h}\right)>0
$$

but

$$
\mathbb{P}\left(a_{j} Z_{j}=x_{h} \mid a_{i} Z_{i}=x_{h}, \mathcal{E}_{h}\right)=0
$$

Therefore, $Z_{i} \not \perp Z_{j} \mid \mathcal{E}_{h}$. A similar argument applies for the equation (4.9).
Corollary 4.6. For $i, j \in A, j \rightarrow i \in \mathcal{C}\left(X_{K}=x_{K}\right)$, suppose that $j \rightarrow k \in \mathcal{C}\left(X_{K}=x_{K}\right)$ for some $k \in H \cup L$. Then there exists $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j \rightarrow i, j \rightarrow k \in g$. In other words,

$$
\mathbb{P}\left(X_{i}=c_{i j}^{*} Z_{j}, Z_{j}=x_{k} / c_{k j}^{*} \mid X_{K}=x_{K}\right)>0
$$

Proof. Since $j \rightarrow i \in \mathcal{C}\left(X_{K}=x_{K}\right)$, there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j \rightarrow i \in g$ and $j \notin K^{*}(g)$, so in particular, $j \rightarrow k \notin g$. Let $\mathcal{E}(g)$ as usual denote the $Z$-values corresponding to the impact graph $g$. Since $j \rightarrow k \notin g$, there exists some other $j^{\prime} \neq j$ such that $z_{j^{\prime}}=x_{k} / c_{k j^{\prime}}^{*}$ and $z_{j}<x_{k} / c_{k j}^{*}$ for all $z \in \mathcal{E}(g)$. Transform the region $\mathcal{E}(g)$ to another region $\phi(\mathcal{E}(g))$ via the following linear map $\phi$, where

$$
\phi(z)_{j}=x_{k} / c_{k j}^{*}, \phi(z)_{j^{\prime}}=z_{j}, \phi(z)_{j^{\prime \prime}}=z_{j^{\prime \prime}} \text { for all } j^{\prime \prime} \neq j, j^{\prime}
$$

Since this is an invertible map and $\mathbb{P}\left(\mathcal{E}(g) \mid X_{K}=x_{K}\right)>0$, we have $\mathbb{P}\left(\phi(\mathcal{E}(g)) \mid X_{K}=x_{K}\right)>$ 0 . Thus there exists some $g^{\prime} \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $\mathbb{P}\left(\mathcal{E}\left(g^{\prime}\right) \cap\left\{X_{K}=x_{K}\right\} \cap \phi(\mathcal{E}(g))\right)>0$. By definition of $\phi$, for such $g^{\prime}$ we must have $j \rightarrow i, j \rightarrow k \in g^{\prime}$. This concludes the proof.

Corollary 4.7. For each $a \in A$, the atomic component of the distribution of $X_{a}$ is supported precisely on the following points:
(a) $\alpha_{a}$ defined by (4.6) if $\alpha_{a}>0$
(b) $c_{a j}^{*} x_{k} / c_{k j}^{*}$ for each $j \in \mathrm{pa}_{\mathcal{C}}(a) \cap \mathrm{pa}_{\mathcal{C}}(k)$ for some $k \in H \cup L$

Proof. Suppose $X_{a}$ has an atomic component at some $c \in \mathbb{R}_{>}$. This happens if and only if there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $X_{a}=c$ on $\mathcal{E}(g) \cap\left\{X_{K}=x_{K}\right\}$. In particular, we must have $a \in K^{*}(g)$. Since $a \notin K^{*}, a \in K^{*}(g)$ if and only if $j \rightarrow a \in g$ for some $j \in V$, and either $j \in K^{*}$ or $\operatorname{ch}_{g}(j) \cap K^{*} \neq \emptyset$. We consider these two cases separately.
(a) Suppose $j \in K^{*}$. Then $c=c_{a j}^{*} x_{j} \leq \alpha_{a}$ by (4.6). If $c<\alpha_{a}$ then $\mathbb{P}\left(X_{a}=c \mid X_{K}=x_{K}\right)=0$ by (4.5), a contradiction. So $c=\alpha_{a}$.
(b) Suppose $j \notin K^{*}$. By Corollary 3.19, there exists some $k \in \operatorname{ch}_{g}(j) \cap H \cap L$. By Corollary 4.6, $\mathbb{P}\left(X_{a}=c_{a j}^{*} Z_{j}, Z_{j}=x_{k} / c_{j k}^{*} \mid X_{K}=x_{K}\right)>0$, so the distribution of $X_{a}$ has an atom at $c_{a j}^{*} x_{k} / c_{k j}^{*}$.
So all the atomic components of the distribution of $X_{a}$ must be of the form given.

5. Markov properties of max-linear Bayesian networks. In this section we introduce the relevant separation criteria and state and prove the three conditional independence theorems. We first consider the most difficult context-specific case and then use the results for this case to derive the more generic results which are valid in all contexts.
5.1. Graphs and separation. In addition to the source DAG as defined in Definition 3.16, we shall need the following graphs to identify Markov properties of a max-linear Bayesian network.

Definition 5.1. Fix a DAG $\mathcal{D}$ on $V$ and $K \subset V$. Say that a directed path $\pi$ from $j$ to $i$ factors through $K$ if there exists a node $k \in \pi, k \neq i, j$ such that $k \in K$. The conditional reachability $D A G \mathcal{D}_{K}^{*}$ is the graph on $V$ consisting of the following edges: $j \rightarrow i \in \mathcal{D}_{K}^{*}$ if and only if there exists a directed path from $j$ to $i$ that does not factor through $K$.

Definition 5.2. Fix a DAG $\mathcal{D}$ on $V, K \subset V$ and a coefficient matrix $C$ supported by $\mathcal{D}$. The critical $D A G \mathcal{D}_{K}^{*}(C)$ is the graph on $V$ consisting of the following edges: $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$ if and only if $c_{i j}^{*}>0$ and no critical directed path from $j$ to $i$ factors through $K$.

Note that in contrast to Definition 5.1 the existence of a single critical path through $K$ removes the corresponding edge in the critical DAG $\mathcal{D}_{K}^{*}(C)$; this conforms with Example 1.1 in the introduction where it is sufficient to block a single critical path to obtain conditional independence.

When $K=\emptyset$, we write $\mathcal{D}^{*}=\mathcal{D}_{\emptyset}^{*}$ for the reachability DAG of $\mathcal{D}$, and $\mathcal{D}^{*}(C)=\mathcal{D}_{\emptyset}^{*}(C)$ if the support of $C$ is $\mathcal{D}$. The source DAG $\mathcal{C}\left(X_{K}=x_{K}\right)$ for $K=\emptyset$ does not have a direct meaning, but by convention we let this be $\mathcal{C}\left(X_{\emptyset}=x_{\emptyset}\right)=\mathcal{D}^{*}$.

Lemma 5.3. Let $C$ be a coefficient matrix with support $\mathcal{D}$. Furthermore, let $K \subset V$ and let $\left\{X_{K}=x_{K}\right\}$ be a possible context. Then

$$
\mathcal{D}_{K}^{*} \supseteq \mathcal{D}_{K}^{*}(C) \supseteq \mathcal{C}\left(X_{K}=x_{K}\right)
$$

Proof. First we prove that $\mathcal{D}_{K}^{*}(C) \subseteq \mathcal{D}_{K}^{*}$. Let $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$. Since $c_{j i}^{*}>0$ and no critical directed paths from $j$ to $i$ factor through $K$, there exists at least one critical directed path from $j$ to $i$ that does not factor through $K$. Therefore, $j \rightarrow i \in \mathcal{D}_{K}^{*}$. Now we prove that $\mathcal{C}\left(X_{K}=x_{K}\right) \subseteq \mathcal{D}_{K}^{*}(C)$. Suppose $j \rightarrow i \in \mathcal{C}\left(X_{K}=x_{K}\right)$. Clearly we must have $c_{j i}^{*}>0$. Suppose for contradiction that $j \rightarrow k \rightarrow i$ is critical for some $k \in K$. Then on $\left\{X_{K}=x_{K}\right\}$,

$$
c_{i j}^{*} Z_{j}=c_{i k}^{*} c_{k j}^{*} Z_{j} \leq c_{i k}^{*} x_{k}
$$

So $j \rightarrow k \notin \mathcal{C}\left(X_{K}=x_{K}\right)$, a contradiction. Therefore all critical paths from $j$ to $i$ do not factor through $K$, so $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$ by definition.

Definition 5.4. An undirected path $\pi$ between $j$ and $i$ in a DAG is $*$-connecting relative to $K$ if and only if it is one of the paths in Figure 13.

We shall consider $*$-connecting paths in the conditional reachability DAG $\mathcal{D}_{K}^{*}$, in the critical DAG $\mathcal{D}_{K}^{*}(C)$, and in the source DAG $\mathcal{C}\left(X_{K}=x_{K}\right)$. Edges in these DAGs represent directed paths in the original DAG $\mathcal{D}$ and each of the paths in Figure 13 may represent longer paths

![img-13.jpeg](img-13.jpeg)

Fig 13: Types of $*$-connecting paths between $i$ and $j$. Nodes that are colored red are in $K$.
in the original DAG $\mathcal{D}$. Note also that any $*$-connecting path in a derived DAG corresponds to a $d$-connecting path in $\mathcal{D}$, but not vice versa, as illustrated in Example 5.8 below.

We now define three independence models by applying $*$-separation to $\mathcal{D}_{K}^{*}, \mathcal{D}_{K}^{*}(C)$ and the source DAG $\mathcal{C}\left(X_{K}=x_{K}\right)$, respectively.

Definition 5.5. For three disjoint subsets $I, J$, and $K$ of the node set $V$ we say that $I$ and $J$ are $\mathcal{D}^{*}$-separated by $K$ in $\mathcal{D}$ if there are no $*$-connecting paths from $I$ to $J$ in $\mathcal{D}_{K}^{*}$ and we then write $I \perp_{\mathcal{D}^{*}} J \mid K$ or $I \perp_{*} J \mid K$ in $\mathcal{D}_{K}^{*}$.

Definition 5.6. For three disjoint subsets $I, J$, and $K$ of the node set $V$ we say that $I$ and $J$ are critically separated by $K$ in $\mathcal{D}$ if there is no $*$-connecting path $\pi$ from $I$ to $J$ in $\mathcal{D}_{K}^{*}(C)$. We then write $I \perp_{C^{*}} J \mid K$ or $I \perp_{*} J \mid K$ in $\mathcal{D}_{K}^{*}(C)$.

Definition 5.7. For three disjoint subsets $I, J$, and $K$ of the node set $V$ we say that $I$ and $J$ are source separated by $X_{K}=x_{K}$ in $\mathcal{D}$ if there are no $*$-connecting paths from $I$ to $J$ in $\mathcal{C}\left(X_{K}=x_{K}\right)$. We then write $I \perp_{\left(C^{*}, x_{K}\right)} J \mid K$ or $I \perp_{*} J \mid K$ in $\mathcal{C}\left(X_{k}=x_{k}\right)$.

Example 5.8 (Cassiopeia). Example 1.2 illustrates that $\mathcal{D}^{*}$-separation is strictly weaker than $d$-separation. Here $\mathcal{D}=\mathcal{D}_{K}^{*}=\mathcal{D}_{K}^{*}(C)$ for any $C$ with support $\mathcal{D}$. The path between 1 and 3 is $d$-connecting, but it is not $*$-connecting.

We emphasize that our separation criteria follow the form of the moralization procedure in [25], which is not stated in a directly path-based form. Rather, we check for separation by constructing derived graphs $-\mathcal{D}_{K}^{*}, \mathcal{D}_{K}^{*}(C)$, and $\mathcal{C}\left(X_{k}=x_{k}\right)$ - and then use a single common separation criteria for all of these. This formulation shall simplify some of the proofs. As a consequence of Lemma 5.3 we get:

Corollary 5.9. For $I, J, K$ disjoint subsets of $V$ and any possible context $\left\{X_{K}=x_{K}\right\}$, it holds that

$$
I \perp_{\mathcal{D}} J|K \Longrightarrow I \perp_{\mathcal{D}^{*}} J| K \Longrightarrow I \perp_{C^{*}} J|K \Longrightarrow I \perp_{\left(C^{*}, x_{K}\right)} J \mid K
$$

where $\perp_{\mathcal{D}}$ denotes $d$-separation.
We note that these implications are strict, as illustrated in the next example and other examples further below.

![img-14.jpeg](img-14.jpeg)
$\mathcal{D}_{K}(C)$ if $c_{42} c_{21} \geq c_{43} c_{31}$

Fig 14: Diamond graph with $K=\{2\}$. The conditional reachability DAG (middle figure) is equal to the reachability DAG $\mathcal{D}^{*}$, whereas the edge $1 \rightarrow 4$ is missing in the critical DAG (right-hand figure) since the path $1 \rightarrow 2 \rightarrow 4$ is critical and factors through $K$. Note that the path $1 \rightarrow 3 \rightarrow 4$ in $\mathcal{D}_{K}^{*}(C)$ is not $*$-connecting as it is not one of the configurations in Figure 13.

Example 5.10 (Diamond). Consider the DAG in Figure 14 in a situation where the path $1 \rightarrow 2 \rightarrow 4$ is critical: $c_{42} c_{21} \geq c_{43} c_{31}$. It then holds that $1 \Perp 4 \mid 2$ even though there is a $d$-connecting path $1 \rightarrow 3 \rightarrow 4$. By Definition 5.4, this path is not $*$-connecting in $\mathcal{D}_{K}^{*}(C)$ so $1 \perp_{C^{*}} 4 \mid 2$. Note also that $\perp_{\mathcal{D}^{*}}$ is strictly weaker than $\perp_{C^{*}}$, as $1 \perp_{C^{*}} 4 \mid 2$ if $c_{21} c_{42} \geq c_{31} c_{43}$, but it holds that $\neg\left(1 \perp_{\mathcal{D}^{*}} 4 \mid 2\right)$ since $1 \rightarrow 3 \rightarrow 4$ is $*$-connecting in $\mathcal{D}_{K}^{*}$.
5.2. The context-specific case. We first consider the case of a specific context and a fixed coefficient matrix $C$. To prove our main Theorem 5.12 we need the following lemma.

Lemma 5.11. Let $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the source $D A G$ of a possible context $\left\{X_{K}=x_{K}\right\}$. Then $i, j \in A$ (the active nodes of Proposition 3.18) are source separated if and only if

$$
\left(\{i\} \cup \mathrm{pa}_{\mathcal{C}}(i)\right) \cap\left(\{j\} \cup \mathrm{pa}_{\mathcal{C}}(j)\right)=\emptyset
$$

and that there is no triple of nodes $i^{\prime}, j^{\prime}, k$ such that

$$
i^{\prime} \in\left(\{i\} \cup \mathrm{pa}_{\mathcal{C}}(i)\right), \quad j^{\prime} \in\left(\{j\} \cup \mathrm{pa}_{\mathcal{C}}(j)\right), \quad k \in H \cup L \text { and } i^{\prime}, j^{\prime} \in \mathrm{pa}_{\mathcal{C}}(k)
$$

Proof. The nodes $i$ and $j$ are $*$-connected if and only if there is a path $\pi$ in $\mathcal{C}\left(X_{K}=x_{K}\right)$ that matches one of the five configurations in Figure 13. One can choose a path $\pi$ of type (a) or (b) if and only if (5.2) does not hold. For types (c) to (e), let $j^{\prime}=j, i^{\prime}=i$ for case (c), $j^{\prime}=j$ for case (d), and $j^{\prime}, i^{\prime}$ be as-is for case (e). By definition of $\mathcal{C}\left(X_{K}=x_{K}\right)$, it holds that $\pi \subset \mathcal{C}\left(X_{K}=x_{K}\right)$ if and only if (5.3) holds for this particular triple of nodes $i^{\prime}, j^{\prime}, k$.

We are now ready for the proof of the main theorem of this section.
Theorem 5.12 (Context-specific, fixed $C$ ). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ with fixed coefficient matrix $C$. Let $K \subseteq V$ and $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the source $D A G$ of the possible context $\left\{X_{K}=x_{K}\right\}$. Then for all $I, J \subseteq V$,

$$
I \perp_{*} J \mid K \text { in } \mathcal{C}\left(X_{K}=x_{K}\right) \Longrightarrow X_{I} \Perp X_{J} \mid X_{K}=x_{K}
$$

Proof. Suppose that $I$ and $J$ are source separated by $\left\{X_{K}=x_{K}\right\}$. By Lemma 5.11, this implies that

$$
\left(I \cup \mathrm{pa}_{\mathcal{C}}(I)\right) \cap\left(J \cup \mathrm{pa}_{\mathcal{C}}(J)\right)=\emptyset
$$

and that there are no pairs $i^{\prime} \in I \cup \mathrm{pa}_{\mathcal{C}}(I), j^{\prime} \in J \cup \mathrm{pa}_{\mathcal{C}}(J)$ that simultaneously appear in the same equation among those in (4.8) and (4.9). By Corollary 4.5, this implies

$$
\left\{Z_{i}: i \in I \cup \mathrm{pa}_{\mathcal{C}}(I)\right\} \Perp\left\{Z_{j}: j \in J \cup \mathrm{pa}_{\mathcal{C}}(J)\right\} \mid X_{K}=x_{K}
$$

and by the representation (4.5), this implies $X_{I} \Perp X_{J} \mid X_{K}=x_{K}$.
Example 5.13 (Tent). Applying Theorem 5.12 to the source DAG in Figure 10 of Example 3.17 yields the conditional independence statement $X_{3} \Perp\left(X_{1}, X_{2}\right) \mid X_{4}=X_{5}=2$, as also stated in the introduction, see Example 1.2.
5.3. The context-free cases. In the previous subsection we identified sufficient conditions for conditional independence given a specific possible context $\left\{X_{K}=x_{K}\right\}$. We now exploit this result to derive conditions for independence that are valid in any context.

THEOREM 5.14 (Context-free, fixed $C$ ). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ with fixed coefficient matrix $C$. Then for all $I, J, K \subseteq V$,

$$
I \perp_{*} J \mid K \text { in } \mathcal{D}_{K}^{*}(C) \Longrightarrow X_{I} \Perp X_{J} \mid X_{K}
$$

Proof. It is enough to prove the result for $K \neq \emptyset$. Suppose that there are no $*$-connecting paths in $\mathcal{D}_{K}^{*}(C)$. For any possible context $\left\{X_{K}=x_{K}\right\}$, by Lemma 5.3, $\mathcal{D}_{K}^{*}(C) \supseteq \mathcal{C}\left(X_{K}=x_{K}\right)$, therefore there is no $*$-connecting path in $\mathcal{C}\left(X_{K}=x_{K}\right)$. Thus we have $X_{i} \Perp X_{j} \mid X_{K}$ by Theorem 5.12.

Finally, we can give the generic Markov condition which does not involve knowledge of the coefficient matrix $C$ :

Theorem 5.15 (Context-free, independent of $C$ ). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$. Then for all $I, J, K \subseteq V$,

$$
I \perp_{*} J \mid K \text { in } \mathcal{D}_{K}^{*} \Longrightarrow X_{I} \Perp X_{J} \mid X_{K} \text { for all } C \text { with support included in } \mathcal{D}
$$

Proof. By Lemma 5.3, $\mathcal{D}_{K}^{*} \supseteq \mathcal{D}_{K}^{*}(C)$, so if there are no $*$-connecting paths in $\mathcal{D}_{K}^{*}$, then there are also no $*$-connecting paths in $\mathcal{D}_{K}^{*}(C)$ for all $C$ supported by $\mathcal{D}$. Thus $X_{i} \Perp X_{j} \mid X_{K}$ for all such $C$ by Theorem 5.14.

Remark 5. We note that Theorem 5.15 is corresponding to what is known as the global Markov property for Bayesian networks, i.e. it establishes that separation in a suitable graph always implies conditional independence simultaneously for all possible values of the conditioning variables, and this statement holds for any choice of coefficient matrix $C$.
6. Completeness. In this section, we shall investigate to what extent the separation criteria developed in Section 5 are complete for conditional independence in max-linear Bayesian networks, i.e. yield all conditional independence relations that are valid. As before, we divide the discussion into the context-specific and context-free cases.

6.1. The context-specific case. We first establish the converse to Theorem 5.12 in the context-specific case. The next lemma is used several times in the proof.

Lemma 6.1. Suppose there is a *-connecting path between $i$ and $j$ in $\mathcal{C}\left(X_{K}=x_{K}\right)$ of types (a) or (b) in Figure 13. Suppose further for type (b) that there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j^{\prime} \rightarrow i, j^{\prime} \rightarrow j \in g$ and $j^{\prime} \notin K^{*}(g)$. Then $X_{i} \Perp X_{j} \mid X_{K}=x_{K}$.

Proof. By Corollary 4.7(b), type (b) implies

$$
\mathbb{P}\left\{\left.\frac{X_{i}}{c_{i j^{\prime}}^{*}}=\frac{X_{j}}{c_{j j^{\prime}}^{*}} \neq \text { an atomic value of } X_{i} \text { or } X_{j} \right\rvert\, X_{K}=x_{K}\right\} \geq \mathbb{P}\left(g \mid X_{K}=x_{K}\right)>0
$$

and in type (a), we have the same inequality with $j=j^{\prime}$. In either case, $X_{i} \Perp X_{j} \mid X_{K}=x_{K}$, as claimed.

The main difficulty in proving Theorem 6.2 below is that having two edges $j^{\prime} \rightarrow i, j^{\prime} \rightarrow$ $j \in \mathcal{C}\left(X_{K}=x_{K}\right)$ does not in general (as in the above Lemma 6.1) imply that there exists a compatible impact graph $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$, where both of these edges appear simultaneously. Indeed, Example 4.4 above shows that this need not be the case, whereas Corollary 4.6 establishes this fact in a specific case.

THEOREM 6.2 (Context-specific completeness). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ with fixed coefficient matrix $C$. Let $K \subseteq V$ and $\mathcal{C}\left(X_{K}=x_{K}\right)$ be the source $D A G$ of a possible context $\left\{X_{K}=x_{K}\right\}$. For all subsets $I, J \subseteq V$ it holds that

$$
X_{I} \Perp X_{J} \mid X_{K}=x_{K} \Longrightarrow I \perp_{*} J \mid K \text { in } \mathcal{C}\left(X_{K}=x_{K}\right)
$$

Proof. To prove this, we separately consider the five different types of $*$-connectivity in Figure 13 and in each of them establish that the variables are dependent, using the node partition $V \backslash U=A \cup H \cup L$ and the representation as in Theorem 4.3 and its corollaries.

First we claim that it is sufficient to consider the case where $I=\{i\}$ and $J=\{j\}$ are singletons with $i, j \in A$. For if $I$ and $J$ are $*$-connected, there must be $i \in I, j \in J$ such that $i$ and $j$ are $*$-connected, so if $i$ and $j$ are dependent, so are $I$ and $J$.

Suppose then that $i$ and $j$ are $*$-connected, i.e. there is a path $\pi$ of the types shown in Figure 13. The proof considers the five different cases (a)-(e) of this figure in turn and gives an appropriate event for each one to establish conditional dependence.

Case (a): This follows directly from Lemma 6.1.
Case (b): For each $t=1, \ldots, m$, let

$$
\tilde{I}_{t}=\operatorname{pa}_{\mathcal{C}}\left(\ell_{t}\right) \cap \operatorname{pa}_{\mathcal{C}}(i), \tilde{J}_{t}=\operatorname{pa}_{\mathcal{C}}\left(\ell_{t}\right) \cap \operatorname{pa}_{\mathcal{C}}(j)
$$

There are two mutually exclusive subcases.
Case (b)I. For each $t=1, \ldots, m$ we have $\tilde{I}_{t} \cup \tilde{J}_{t} \subsetneq \operatorname{pa}_{\mathcal{C}}\left(\ell_{t}\right)$.
In particular, for each such $t$, there exists some $r_{t} \in \operatorname{pa}_{\mathcal{C}}\left(\ell_{t}\right)$ such that

$$
r_{t} \notin \operatorname{pa}_{\mathcal{C}}(i) \cup \operatorname{pa}_{\mathcal{C}}(j)
$$

Our goal is to construct an appropriate $g$ and appeal to Lemma 6.1. Apply (4.7) to $j^{\prime}$, let $\beta_{j^{\prime}}$ be the constant on the right-hand side of this inequality. For a sufficiently small constant $\epsilon>0$, consider the event $\mathcal{E}$ defined by

- $\beta_{j^{\prime}}-\epsilon<Z_{j^{\prime}}<\beta_{j^{\prime}}$ ( $Z_{j^{\prime}}$ is only slightly smaller than the largest value possible in the context $\left\{X_{K}=x_{K}\right\}$ )
- $Z_{r}<\epsilon$ for all $r \in \mathrm{pa}_{\mathcal{C}}(i) \cup \mathrm{pa}_{\mathcal{C}}(j) \backslash\left\{j^{\prime}\right\}$ (any other parent of $i$ or $j$, except $j^{\prime}$, has very small $Z$-value)
- $Z_{i}, Z_{j}<\epsilon$ ( $i$ and $j$ also have very small $Z$ values)
- for each $h \in H$, set $Z_{r^{\prime}}<\epsilon$ for all $r^{\prime} \in \mathrm{pa}_{\mathcal{C}}(h) \backslash\left\{j^{\prime}\right\}$, and $Z_{h}=x_{h}$ (any node in $h$ realizes itself: its parents have small $Z$-values, and its own $Z$-value is $x_{h}$.)
- for each $\ell_{t}$ for $t=1, \ldots, m$, let $r_{t}$ satisfy (6.1), and set it to achieve the maximum in (4.9). (Each block $L_{t}$ gets a parent whose $Z$-value is not already constrained by the previous conditions).
In the above, the only nodes that were mentioned but did not get set to be less than $\epsilon$ are $Z_{j^{\prime}}, Z_{r_{t}}$ for $t=1, \ldots, m$ and $Z_{h}$ for $h \in H$. By Proposition 3.18 and (6.1), these nodes are all distinct, so the event $\mathcal{E}$ is well-defined. Furthermore, by Proposition 3.18 and Corollary 4.5, $\left\{Z_{r_{t}}, Z_{h}: t=1, \ldots, m, h \in H\right\}$ are independent, and either $Z_{j^{\prime}}$ is independent of $\left\{Z_{r_{t}}, Z_{h}\right.$ : $t=1, \ldots, m, h \in H\}$, or it is independent of all but exactly one of them, say, $Z_{u}$ for $u \in\left\{r_{t}\right.$ : $t=1, \ldots, m\} \cup H$. In both cases, by Theorem 4.3 and Corollary 4.5, $\mathbb{P}\left(\mathcal{E} \mid X_{K}=x_{K}\right)>0$. So there exists at least one $g \in \mathcal{C}\left(X_{K}=x_{K}\right)$ such that $\mathbb{P}\left(\mathcal{E}(g) \cap \mathcal{E} \mid X_{K}=x_{K}\right)>0$. By construction of this event, $j^{\prime} \rightarrow i, j^{\prime} \rightarrow j \in g$ and $j^{\prime} \notin K^{*}(g)$. Hence $X_{i} \Perp X_{j} \mid X_{K}=x_{K}$ by Lemma 6.1.
Case (b)II. There exists at least one $t=1, \ldots, m$ such that

$$
\tilde{I}_{t} \cup \tilde{J}_{t}=\operatorname{pa}_{\mathcal{C}}\left(\ell_{t}\right)
$$

Fix such a $t$. Define

$$
\mathcal{E}_{1}=\left\{X_{i}<\min _{r \in \tilde{I}_{t}} \frac{c_{i r}^{*} x_{\ell_{t}}}{c_{\ell_{t} r}^{*}}\right\} \quad \text { and } \quad \mathcal{E}_{2}=\left\{X_{j}<\min _{r \in \tilde{J}_{t}} \frac{c_{j r}^{*} x_{\ell_{t}}}{c_{\ell_{t} r}^{*}}\right\}
$$

By Proposition 3.18(j), $\tilde{I}_{t}, \tilde{J}_{t} \neq \emptyset$, so the above events are well-defined. Let $r_{0}$ denote a node $r \in \tilde{J}_{t}$ that achieves the minimum in $\mathcal{E}_{2}$ above. Since $r_{0} \rightarrow j \in \mathcal{C}\left(X_{K}=x_{K}\right)$, there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $r_{0} \rightarrow j, r_{0} \notin K^{*}(g)$. This implies that on $\mathcal{E}(g)$,

$$
Z_{r_{0}}<x_{\ell_{t}} / c_{\ell_{t} r_{0}}^{*}, \quad X_{j}=c_{j r_{0}}^{*} Z_{r_{0}}
$$

Together these imply that on $\mathcal{E}(g)$,

$$
X_{j}<\frac{c_{j r_{0}}^{*} x_{\ell_{t}}}{c_{\ell_{t} r_{0}}^{*}}=\min _{r \in \tilde{J}_{t}} \frac{c_{j r}^{*} x_{\ell_{t}}}{c_{\ell_{t} r}^{*}}
$$

So $\mathcal{E}(g) \subseteq \mathcal{E}_{2}$. Therefore, $\mathbb{P}\left(\mathcal{E}_{2} \mid X_{K}=x_{K}\right)>0$ and, by symmetry, $\mathbb{P}\left(\mathcal{E}_{1} \mid X_{K}=x_{K}\right)>0$.
By (4.9) in Theorem 4.3, for each $g \in \mathfrak{G}\left(X_{K}=x_{K}\right), \mathrm{pa}_{g}\left(\ell_{t}\right) \in \mathrm{pa}_{\mathcal{C}}\left(\ell_{t}\right)$. By (6.2), either $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{I}_{t}$ or $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{J}_{t}$; note that both can occur simultaneously as we are not claiming that $\tilde{I}_{t} \cap \tilde{J}_{t}=\emptyset$. Consider all $g$ such that $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{J}_{t}$. Let $r=\mathrm{pa}_{g}\left(\ell_{t}\right)$. By definition of the max-linear model,

$$
X_{j} \geq c_{j r}^{*} Z_{r}=\frac{c_{j r}^{*} x_{\ell_{t}}}{c_{\ell_{t} r}^{*}} \text { on } \mathcal{E}(g) \text { for any } g \text { s.t. } \quad r=\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{J}_{t}
$$

In particular, for any $g$ such that $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{J}_{t}$,

$$
\mathbb{P}\left(\mathcal{E}(g) \cap \mathcal{E}_{2} \mid X_{K}=x_{K}\right)=0
$$

By the same argument, for any $g$ such that $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{I}_{t}$,

$$
\mathbb{P}\left(\mathcal{E}(g) \cap \mathcal{E}_{1} \mid X_{K}=x_{K}\right)=0
$$

But $\mathrm{pa}_{g}\left(\ell_{t}\right) \in \tilde{I}_{t} \cup \tilde{J}_{t}$ for all $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ as mentioned above. Therefore, there is no $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $\mathcal{E}(g) \subseteq \mathcal{E}_{1} \cap \mathcal{E}_{2}$. That is,

$$
\mathbb{P}\left(\mathcal{E}_{1} \cap \mathcal{E}_{2} \mid X_{K}=x_{K}\right)=0
$$

But $\mathbb{P}\left(\mathcal{E}_{1} \mid X_{K}=x_{K}\right)>0, \mathbb{P}\left(\mathcal{E}_{2} \mid X_{K}=x_{K}\right)>0$, so the events $\mathcal{E}_{1}$ and $\mathcal{E}_{2}$ are not independent conditioned on $\left\{X_{K}=x_{K}\right\}$. Therefore, $X_{i} \not \mathcal{L} X_{j} \mid X_{K}=x_{K}$.
Cases (c), (d) and (e): We may assume that cases (a) and (b) do not apply. In particular, (5.2) holds. For case (c), let

$$
\mathcal{E}_{1}=\left\{X_{i}=\frac{x_{k}}{c_{k i}^{*}}, X_{K}=x_{K}\right\}, \quad \mathcal{E}_{2}=\left\{X_{j}=\frac{x_{k}}{c_{k j}^{*}}, X_{K}=x_{K}\right\}
$$

For case (d), let

$$
\mathcal{E}_{1}=\left\{X_{i}=\frac{x_{k}}{c_{k i}^{*}}, X_{K}=x_{K}\right\}, \quad \mathcal{E}_{2}=\left\{X_{j}=\frac{c_{j j^{\prime}}^{*} x_{k}}{c_{k j^{\prime}}^{*}}, X_{K}=x_{K}\right\}
$$

For case (e), let

$$
\mathcal{E}_{1}=\left\{X_{i}=\frac{c_{i i^{\prime}}^{*} x_{k}}{c_{k i^{\prime}}^{*}}, X_{K}=x_{K}\right\}, \quad \mathcal{E}_{2}=\left\{X_{j}=\frac{c_{j j^{\prime}}^{*} x_{k}}{c_{k j^{\prime}}^{*}}, X_{K}=x_{K}\right\}
$$

We now claim that in all three cases we have

$$
\mathbb{P}\left(\mathcal{E}_{1} \mid X_{K}=x_{K}\right)>0 \text { and } \mathbb{P}\left(\mathcal{E}_{2} \mid X_{K}=x_{K}\right)>0
$$

Indeed, these follow in case (c) from $i \rightarrow k, j \rightarrow k \in \mathcal{C}\left(X_{K}=x_{K}\right)$, and in cases (d) and (e) from Corollary 4.6 applied to the triples $k \leftarrow j^{\prime} \rightarrow j$ and $k \leftarrow i^{\prime} \rightarrow i$. By (3.10) in Lemma 3.13, any $g \in \mathfrak{G}\left(\mathcal{E}_{1}\right)$ must have $R_{g}(k)=R_{g}(i)$. Similarly, any $g \in \mathfrak{G}\left(\mathcal{E}_{2}\right)$ must have $R_{g}(k)=R_{g}(j)$. But (5.2) implies $R_{g}(i) \neq R_{g}(j)$ for all $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$. Therefore,

$$
\mathbb{P}\left(\mathcal{E}_{1} \mid \mathcal{E}_{2}, X_{K}=x_{K}\right)=\mathbb{P}\left(\mathcal{E}_{2} \mid \mathcal{E}_{1}, X_{K}=x_{K}\right)=0
$$

So $X_{i} \not X_{j} \mid X_{K}=x_{K}$ in each of the three cases, as needed. Since all cases have been considered, this concludes the proof.
6.2. The context-free cases. Next we consider the context-free case for a given coefficient matrix $C$. We begin by showing that the direct converse to Theorem 5.14 is false, as demonstrated in the following example.

![img-15.jpeg](img-15.jpeg)

Fig 15: The counterexample with $\mathcal{D}=\mathcal{D}_{K}^{*}$ and observed nodes $K=\{4,5\}$. Here it holds that $X_{1} \Perp X_{2} \mid X_{\{4,5\}}$ even though 1 and 2 are $*$-connected relative to $K$ with the path $1 \rightarrow 4 \leftarrow 3 \rightarrow 2$.
![img-16.jpeg](img-16.jpeg)

Fig 16: The source $\operatorname{DAG} \mathcal{C}\left(x_{4}, x_{5}\right)$ in a context satisfying $\left\{x_{5} \geq x_{4}\right\}$ is a subgraph of the graph to the left and of the graph to the right if $\left\{x_{5}<x_{4}\right\}$.

Example 6.3. Consider the graph in Figure 15 with all edge weights equal to one. We have

$$
\begin{aligned}
& X_{5}=Z_{5} \vee Z_{1} \\
& X_{4}=Z_{4} \vee Z_{1} \vee Z_{3} \\
& X_{2}=Z_{2} \vee Z_{3} \vee Z_{5}
\end{aligned}
$$

The important feature of this example is that $c_{21}^{*}=c_{25}^{*} c_{51}^{*}$, i.e. there is a critical directed path from 1 to 2 that factors through $K$, so $1 \rightarrow 2 \notin \mathcal{D}_{K}^{*}(C)$ and $1 \rightarrow 2 \notin \mathcal{D}_{K}^{*}$. On the other hand, $\pi=1 \rightarrow 4 \leftarrow 3 \rightarrow 2$ is a $*$-connecting path. Nevertheless, we claim below that $X_{1} \Perp X_{2} \mid X_{4,5}$.

Indeed, if $x_{5} \geq x_{4}$, then also $x_{5} \geq Z_{3}$ so $\mathcal{C}\left(x_{4}, x_{5}\right)$ is a subgraph of the graph to the left in Figure 16 On the other hand, if $x_{5}<x_{4}$, then $1 \rightarrow 4 \notin \mathcal{C}\left(x_{4}, x_{5}\right)$ so that $\mathcal{C}\left(x_{4}, x_{5}\right)$ is a subgraph of the graph to the right in Figure 16.

In both cases there is no $*$-connecting path between 1 and 2, hence by Theorem 5.12 we have $X_{1} \Perp X_{2} \mid X_{\{4,5\}}$.

We note that the phenomenon here has some similarity to 'path cancellations' in standard linear Bayesian networks, where specific values of the coefficients may allow dependence relations to cancel and yield conditional independence which does not follow from the separation criterion. Below we shall discuss and resolve this type of problem. Here the set of coefficients corresponding to such a phenomenon may have positive Lebesgue measure, in contrast to the standard case, which makes this discussion necessary. The key concept is that of an effective edge or path, as further described below.
6.2.1. Effective edges and paths. To obtain converses for the context-free cases, we wish to construct a possible context $\left\{X_{K}=x_{K}\right\}$ that violates the context-specific Markov condition. However, Example 6.3 above shows that this is not always possible. We need to ensure that no inequalities along $*$-connecting paths imply further equalities and to control this we need the following concept.

Definition 6.4. Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ with fixed coefficient matrix $C$ and $K \subset V$. For an edge $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$, the substitution matrix $\Xi_{K}^{i j}$ of this edge relative to $K$ is a $|K| \times|K|$ matrix with the following non-zero entries:

$$
\left(\xi_{K}^{i j}\right)_{k \ell}=\frac{c_{k j}^{*} c_{i \ell}^{*}}{c_{i j}^{*}} \text { for } k \in K \cap \operatorname{ch}_{\mathcal{D}^{*}}(j), \ell \in K \cap\left(\operatorname{pa}_{\mathcal{D}^{*}}(i) \cup\{i\}\right), k \neq \ell
$$

If $\pi$ is a $*$-connecting path between $i$ and $j$, then its substitution matrix $\Xi_{K}^{\pi}$ relative to $K$ is defined as

$$
\Xi_{K}^{\pi}=\bigvee_{v \rightarrow u \in \pi} \Xi_{K}^{u v}
$$

REMARK 6. Example 6.3 above features a path $\pi=1 \rightarrow 4 \leftarrow 3 \rightarrow 2$ in $\mathcal{D}_{K}^{*}(C)$, but there is no $x_{K}$ such that $\pi \subset \mathcal{C}\left(X_{K}=x_{K}\right)$. More importantly, as we show in Proposition 6.14 below, existence of such an $x_{K}$ is equivalent to the additional condition (6.4) ensuring that the path is effective, as defined below.

Definition 6.5. A $*$-connecting path $\pi$ from $I$ to $J$ in $\mathcal{D}_{K}^{*}(C)$ is said to be effective if it satisfies the tropical eigenvalue condition

$$
\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)<1
$$

where $\Xi_{K}^{\pi}$ is the substitution matrix of $\pi$ with respect to $K$ and $\Gamma_{K K}$ is the restriction of the weak transitive closure $\Gamma(C)$ as in (2.3) to the components in $K$.

Example 6.6. The condition (6.4) is necessary in general. In Example 6.3 we have a single $*$-connecting path $\pi$ in $\mathcal{D}_{K}^{*}(C)$ between 1 and 2 and for this path (6.4) fails, as we shall now show. The substitution matrix for the path $\pi=1 \rightarrow 4 \leftarrow 3 \rightarrow 2$ is

$$
\Xi_{K}^{\pi}=\Xi_{K}^{41} \vee \Xi_{K}^{43} \vee \Xi_{K}^{23}
$$

We find positive entries

$$
b_{54}^{41}=\frac{c_{51}^{*}}{c_{41}^{*}}=1 \quad \text { and } \quad b_{45}^{23}=\frac{c_{43}^{*} c_{25}^{*}}{c_{23}^{*}}=1
$$

so

$$
\Gamma_{K K} \vee \Xi_{K}^{\pi}=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right) \vee\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)
$$

and hence we get

$$
\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)=1
$$

which violates (6.4). Here, as noticed in Example 6.3, $X_{i} \Perp X_{j} \mid X_{K}$ despite the existence of a $*$-connecting path.

It turns out that condition (6.4) is often automatically satisfied. As we shall study effective edges in a specific context, we need the following concept.

Definition 6.7. The completion of the coefficient matrix $C$ with respect to a possible context $\left\{X_{K}=x_{K}\right\}$ is the $|V| \times|V|$ coefficient matrix $\bar{C}$, with

$$
\bar{c}_{i j}=\left\{\begin{array}{cc}
x_{i} / x_{j} & \text { if } i, j \in K^{*} \\
c_{i j} & \text { else. }
\end{array}\right.
$$

We write $\bar{C}^{*}=\left(\bar{c}_{k h}^{*}\right)$ for the Kleene star of $\bar{C}$ and note that all cycles in $\mathcal{D}(\bar{C})$ that only involve nodes in $K^{*}$ have weight equal to one:

$$
\bar{c}_{i_{1} i_{2}} \bar{c}_{i_{2} i_{3}} \cdots \bar{c}_{i_{k} i_{1}}=\frac{x_{i_{1}}}{x_{i_{2}}} \frac{x_{i_{2}}}{x_{i_{3}}} \cdots \frac{x_{i_{k}}}{x_{i_{1}}}=1
$$

Lemma 6.8. Let $\bar{C}$ be the completion of $C$ with respect to a possible context $\left\{X_{K}=x_{K}\right\}$. Then $\lambda(\bar{C})=1$.

Proof. If $|K|=1$ this is obviously true for a self-loop. Assume that $|K| \geq 2$. Since $\mathcal{D}(C)$ is acyclic and all cycles in $\mathcal{D}(\bar{C})$ involving only nodes in $K^{*}$ have length 1 , it is sufficient to consider simple cycles $\pi=1 \rightarrow 2 \cdots \rightarrow r \rightarrow 1$, with $1, r \in K^{*}$ and other nodes not in $K^{*}$. Write $\bar{c}(\pi)$ for the product of the edge weights of this cycle in $\bar{C}$. We claim that $\bar{c}(\pi) \leq 1$. Indeed,

$$
\bar{c}(\pi) \leq c_{r 2}^{*} c_{21}^{*} \bar{c}_{1 r}=c_{r 2}^{*} c_{21}^{*} \frac{x_{1}}{x_{r}} \leq \frac{c_{r 1}^{*} x_{1}}{x_{r}} \leq 1
$$

where we have used that $c_{r 1}^{*} \geq c_{21}^{*} c_{r 2}^{*}$ and the context $\left\{X_{K}=x_{K}\right\}$ is possible, so $x_{r} \geq c_{r 1}^{*} x_{1}$. Hence the maximum cycle mean is $\lambda(\bar{C})=1$, as desired.

Corollary 6.9. For $k, h \in K^{*}$ we have that $\bar{c}_{k h}^{*}=\bar{c}_{k h}=x_{k} / x_{h}$.
Proof. If $h=k$ this is obviously true. Now assume $h \neq k$. By definition of the Kleene star, $\bar{c}_{k h}^{*} \geq \bar{c}_{k h}$ and since $\lambda(\bar{C})=1$, we also have $\lambda\left(\bar{C}^{*}\right)=1$. Since $k \rightarrow h$ and $h \rightarrow k$ are edges in $\bar{C}$, we may consider the cycle $k \rightarrow h \rightarrow k$ and get

$$
1=\lambda\left(\bar{C}^{*}\right) \geq \bar{c}_{k h}^{*} \bar{c}_{h k}^{*} \geq \bar{c}_{k h} \bar{c}_{h k}=\frac{x_{k}}{x_{h}} \frac{x_{h}}{x_{k}}=1
$$

Thus we must have equalities; that is $\bar{c}_{k h}^{*}=\bar{c}_{k h}$ and $\bar{c}_{h k}^{*}=\bar{c}_{h k}$.
Definition 6.10. Say that an edge $j \rightarrow i$ in $\mathcal{D}_{K}^{*}(C)$ is effective in the possible context $\left\{X_{K}=x_{K}\right\}$ if $j \notin K^{*}$, no critical directed paths from $j$ to $i$ factor through $K^{*}$, and $c_{i j}^{*}=\bar{c}_{i j}^{*}$. Let $E^{+}\left(X_{K}=x_{K}\right)$ denote the set of effective edges in the context $\left\{X_{K}=x_{K}\right\}$. Edges in $\mathcal{D}_{K}^{*}(C)$ which are not effective are ineffective. Finally, a path $\pi$ is effective in a context if all its edges are.

Now we give an algebraic characterization of edges that are effective in a context.
Lemma 6.11. Let $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$ and consider a possible context $\left\{X_{K}=x_{K}\right\}$. Then $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$ if and only if for all $k \in K^{*} \cap \operatorname{ch}_{\mathcal{D}^{*}}(j), \ell \in K^{*} \cap\left(\mathrm{pa}_{\mathcal{D}^{*}}(i) \cup\{i\}\right)$, it holds that

$$
\left(\xi_{K^{*}}^{i j}\right)_{k \ell} x_{\ell}<x_{k}
$$

for $\Xi_{K^{*}}^{i j}$ being the substition matrix relative to $K^{*}$ as defined in (6.3).

Proof. Suppose $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$. For each $k \in K^{*} \cap \operatorname{ch}_{\mathcal{D}^{*}}(j)$ and $\ell \in K^{*} \cap$ $\left(\mathrm{pa}_{\mathcal{D}^{*}}(i) \cup\{i\}\right)$, the path $j \rightarrow k \rightarrow \ell \rightarrow i$ (or $j \rightarrow k \rightarrow i$ if $i=\ell$ ) has $\bar{C}$-weight

$$
c_{i \ell}^{*} \frac{x_{\ell}}{x_{k}} c_{k j}^{*}
$$

Since this path factors through $K^{*}$, it is not critical, so

$$
c_{i \ell}^{*} \frac{x_{\ell}}{x_{k}} c_{k j}^{*}<c_{i j}^{*}
$$

Rearranging gives (6.5). Conversely, suppose that (6.5) holds. Let $\pi$ be a path from $j$ to $i$ in $\mathcal{D}(\bar{C})$ that factors through $K^{*}$. If it only goes through one node of $K^{*}$, then it is also a path in $C$ that factors through $K^{*}$, so $\bar{c}^{*}(\pi)=c^{*}(\pi)$. Since $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$, by definition of $\mathcal{D}_{K}^{*}(C)$, we have

$$
\bar{c}^{*}(\pi)=c^{*}(\pi)<c_{i j}^{*}
$$

If $\pi$ goes through two or more nodes of $K^{*}$, then without loss of generality we can assume

$$
\pi=j \rightarrow \cdots \rightarrow k_{1} \rightarrow \cdots \rightarrow k_{2} \rightarrow \cdots \rightarrow k_{r} \rightarrow \cdots \rightarrow i
$$

where $r \geq 2, k_{1}, \ldots, k_{r} \in K^{*}$, and $\rightarrow \cdots \rightarrow$ are sequences of critical edges that do not go through $K^{*}$. By this criticality assumption, we get the equality

$$
\bar{c}^{*}(\pi)=c_{k_{1} j}^{*} \bar{c}_{k_{2} k_{1}}^{*} \ldots \bar{c}_{k_{r} k_{r-1}}^{*} c_{i k_{r}}^{*}
$$

By Corollary 6.9,

$$
\bar{c}_{k_{2} k_{1}}^{*} \ldots \bar{c}_{k_{r} k_{r-1}}^{*}=\bar{c}_{k_{r} k_{1}}^{*}=\frac{x_{k_{1}}}{x_{k_{r}}}
$$

Note that $k_{1} \in \operatorname{ch}_{\mathcal{D}^{*}}(j)$ and $k_{r} \in \mathrm{pa}_{\mathcal{D}^{*}}(i)$. Apply (6.5) with $k_{1}=k$ and $k_{r}=\ell$ yields

$$
\frac{c_{k j}^{*} c_{i \ell}^{*}}{c_{i j}^{*}} x_{\ell}<x_{k}
$$

Rearranging, we get

$$
\bar{c}^{*}(\pi)=c_{k j}^{*} \frac{x_{\ell}}{x_{r}} c_{i \ell}^{*}<c_{i j}^{*}
$$

This shows that any critical path $\pi$ that factors through $K^{*}$ has weight strictly less than $c_{i j}^{*}$, as desired.

A simple corollary is the following, showing that all edges in the source DAG for a given context are indeed effective in that context.

Corollary 6.12. If $j \rightarrow i$ is an edge in $\mathcal{C}\left(X_{K}=x_{K}\right)$ then $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$.
Proof. Assume that $j \rightarrow i \in \mathcal{C}\left(X_{K}=x_{K}\right)$ so we have $j \notin K^{*}$ and $c_{i j}^{*}>0$. First we claim that $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$. Indeed, suppose for contradiction that a critical path from $j$ to $i$ in $\mathcal{D}$ factors through some node $k \in K$, then

$$
c_{i j}^{*} Z_{j}=c_{i k}^{*} c_{k j}^{*} Z_{j} \leq c_{i k}^{*} x_{k}
$$

![img-17.jpeg](img-17.jpeg)

Fig 17: The graph to the left displays $\mathcal{D}(C)=\mathcal{D}\left(C^{*}\right)$ with coefficients. The impact graph $g$ in the middle is not compatible with $\left\{X_{K}=x_{K}\right\}$ if $c_{43} c_{21} x_{3} \geq c_{41} x_{2}$, as shown in Example 6.13, thus rendering the edge $1 \rightarrow 4$ ineffective. The graph to the right is the completion $\mathcal{D}\left(\bar{C}^{*}\right)$.

Since

$$
X_{i}=c_{i k}^{*} x_{k} \vee c_{i j}^{*} Z_{j} \vee \ldots
$$

this implies that $j \rightarrow i \notin \mathcal{C}\left(X_{K}=x_{K}\right)$, a contradiction as needed. Hence $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$.
Next suppose for contradiction that $j \rightarrow i \notin E^{+}\left(X_{K}=x_{K}\right)$. By Lemma 6.11, this implies for some $k \in K^{*} \cap \operatorname{ch}_{\mathcal{D}^{*}}(j)$ and $\ell \in K^{*} \cap\left(\operatorname{pa}_{\mathcal{D}^{*}}(i) \cup\{i\}\right)$,

$$
\left(\xi_{K^{*}}^{i j}\right)_{k \ell} x_{\ell} \geq x_{k}
$$

We apply the definition of the substitution matrix $\Xi_{K^{*}}^{i j}$ in (6.3) and rearrange; then we get

$$
c_{i \ell}^{*} x_{\ell} \geq \frac{c_{i j}^{*}}{c_{k j}^{*}} x_{k}
$$

Since $j \rightarrow k \in \mathcal{D}_{K}^{*}(C)$, it holds that $x_{k} \geq c_{k j}^{*} Z_{j}$ so

$$
\frac{c_{i j}^{*}}{c_{k j}^{*}} x_{k} \geq c_{i j}^{*} Z_{j}
$$

Since

$$
X_{i}=c_{i \ell}^{*} x_{\ell} \vee c_{i j}^{*} Z_{j} \vee \ldots
$$

it follows that $j \rightarrow i \notin \mathcal{C}\left(X_{K}=x_{K}\right)$, a contradiction as needed. The proof is complete.
Example 6.13. Consider the graph to the left in Figure 17. Here $C=C^{*}$. In this case we have $X_{1} \Perp X_{4} \mid X_{2}, X_{3}$ although this is not true in all contexts. We first show that the graph $g$ in the middle is not compatible with $\left\{X_{K}=x_{K}\right\}$ if $c_{43} c_{21} x_{3} \geq c_{41} x_{2}$. We thus write out the max-linear model:

$$
\begin{aligned}
X_{1} & =Z_{1} \\
x_{3} & =Z_{3} \\
x_{2} & =c_{21} Z_{1} \vee Z_{2} \\
X_{4} & =c_{43} x_{3} \vee c_{41} Z_{1} \vee Z_{4}
\end{aligned}
$$

From (6.6), we have that $Z_{1} \leq x_{2} / c_{21}$, so $c_{41} Z_{1} \leq c_{41} x_{2} / c_{21}$. Thus, if $c_{41} x_{2} / c_{21} \leq c_{43} x_{3}$, or equivalently, $c_{41} x_{2} \leq c_{43} c_{21} x_{3}$, we also have $c_{41} Z_{1}<c_{43} x_{3}$ and hence $\left(x_{2}, x_{3}\right)$ is not in the image of $L_{g}$ so $g$ is not compatible with the context.

Further, the support of $\tilde{C}^{*}$ is shown to the right of Figure 17. With the addition of the edges $\bar{c}_{23}=x_{2} / x_{3}$ and $\bar{c}_{32}=x_{3} / x_{2}$, we have

$$
\bar{c}_{41}^{*}=c_{41} \vee c_{43} \bar{c}_{32} c_{21}=c_{41} \vee c_{43} \frac{x_{3}}{x_{2}} c_{21}
$$

In particular, $1 \rightarrow 4$ is not effective w.r.t. $\left\{X_{K}=x_{K}\right\}$ if $c_{41}<c_{43}\left(x_{3} / x_{2}\right) c_{21}$.
REMARK 7. By definition of $\tilde{C}$ and the critical graph $\mathcal{D}_{K^{*}}^{*}(C)$, if $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$, then it holds that $j \rightarrow i \in \mathcal{D}_{K^{*}}^{*}(C) \subseteq \mathcal{D}_{K}^{*}(C)$. But the converse fails. That is, $E^{+}\left(X_{K}=x_{K}\right)$ can be a strictly smaller set of edges than those in $\mathcal{D}_{K}^{*}(C)$ or $\mathcal{D}_{K^{*}}^{*}(C)$.

The following says that if a path is effective in a context, it is effective in the sense of Definition 6.5. Note that, crucially, Definition 6.5 refers to the original set of conditioned variables $K$, while being effective in a given context $\left\{X_{K}=x_{K}\right\}$ is a property that involves the potentially bigger set $K^{*}$ of variables which are constant in this context.

Proposition 6.14. Let $\pi$ be a *-connecting path in $\mathcal{D}_{K}^{*}(C)$. If $\pi$ is effective in a possible context $\left\{X_{K}=x_{K}\right\}$, then $\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)<1$.

Proof. For each edge $j \rightarrow i \in \pi$, let $\Xi_{K}^{i j}$ be the substitution matrix of this edge with respect to $K$ (cf. Definition 6.4). Since $K \subseteq K^{*}\left(X_{K}=x_{K}\right)$, by Lemma 6.11,

$$
\Xi_{K}^{i j} \odot x_{K}<x_{K}
$$

Thus

$$
\left(\bigvee_{j \rightarrow i \in \pi} \Xi_{K}^{i j}\right) \odot x_{K}=\Xi_{K}^{\pi} \odot x_{K} \leq x_{K}
$$

Since $x_{K}$ satisfies the max-linear model, we have

$$
x_{K}=\left(C^{*} \odot x\right)_{K} \geq \Gamma_{K K} \odot x_{K}
$$

So

$$
\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right) \odot x_{K}=\Gamma_{K K} \odot x_{K} \vee \Xi_{K}^{\pi} \odot x_{K} \leq x_{K}
$$

By Proposition 2.1(a), this implies $\lambda\left(\Gamma_{K K} \vee \Xi^{\pi}\right) \leq 1$. Now we want to argue that this eigenvalue must be strictly less than 1. By Proposition 2.1(b), it is sufficient to show that there does not exist a cycle in $\mathcal{D}\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)$ with weight 1 .

Suppose then for contradiction that there exists a cycle $\sigma$ with weight $w(\sigma)=1$, let $S$ be its support, and let $A_{S S}=\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)_{S S}$. Since $\mathcal{D}\left(\Gamma_{K K}\right)$ is a DAG and $\Xi_{K}^{\pi}$ has zero diagonal, we must have $|S| \geq 2$. Again by Proposition 2.1(b) we have

$$
A_{S S} \odot x_{S}=x_{S}
$$

Now consider an edge $v \rightarrow u \in \sigma$; by definition of $A_{S S}$ we have

$$
a_{u v}=c_{u v}^{*} \vee \bigvee_{j \rightarrow i \in \pi, i \notin K}\left(\xi_{K}^{i j}\right)_{u v} \vee \bigvee_{j \rightarrow i \in \pi, i \in K}\left(\xi_{K}^{i j}\right)_{u v}
$$

By Lemma 2.2 we further have $a_{u v} x_{v}=x_{u}$ and by (6.3)

$$
\bigvee_{j \rightarrow i \in \pi, i \notin K}\left(\xi_{K}^{i j}\right)_{u v} x_{v}<x_{u}
$$

Thus

$$
a_{u v}=c_{u v}^{*} \vee \bigvee_{j \rightarrow i \in \pi, i \in K}\left(\xi_{K}^{i j}\right)_{u v}
$$

for all edges $v \rightarrow u \in \sigma$. By definition, for $i \in K,\left(\xi_{K}^{i j}\right)_{u v}>0$ if and only if $v=i$. In other words, for each edge $v \rightarrow u \in \sigma$ such that $a_{u v}>c_{u v}^{*}$ it holds that $v \in K \cap \pi$. Since $\pi$ is a $*$ connecting path, $|K \cap \pi| \leq 1$, there is at most one edge $v \rightarrow u$ of $\sigma$ where $a_{u v}=\left(\xi_{K}^{v j}\right)_{u v}>c_{u v}^{*}$, while for all other edges $v^{\prime} \rightarrow u^{\prime}$ of $\sigma, a_{u^{\prime} v^{\prime}}=c_{u^{\prime} v^{\prime}}^{*}$. Since $\mathcal{D}(C)$ is a DAG, there must be exactly one such edge. Therefore,

$$
w(\sigma)=\left(\xi_{K}^{v j}\right)_{u v} c_{v u_{1}}^{*} c_{u_{1} u_{2}}^{*} \ldots c_{u_{r} u}^{*}=\left(\xi_{K}^{v j}\right)_{u v} c_{v u}^{*}=\frac{c_{u j}^{*} c_{v u}^{*}}{c_{v j}^{*}}
$$

with $v, u \in K, c_{v u}^{*}>0$ and $j \rightarrow v, j \rightarrow u \in \mathcal{D}_{K}^{*}(C)$. But $j \rightarrow u \rightarrow v$ is a path from $j$ to $v$ that factors through $K$. Since $j \rightarrow v \in \mathcal{D}_{K}^{*}(C)$, we have

$$
c_{v u}^{*} c_{u j}^{*}<c_{v j}^{*}
$$

Rearranging gives $w(\sigma)<1$, which is our desired contradiction.
6.2.2. Context-free completeness. To establish context-free completeness, we must understand the geometry of the set $\mathcal{L}_{K}^{C}$ defined in (2.6). For an edge $j \rightarrow i \in \mathcal{D}_{K}^{*}(C)$ we let $x_{K}(j \rightarrow i)$ be the set of $x_{K}$ such that $j \rightarrow i$ is an effective edge in the possible context $\left\{X_{K}=x_{K}\right\}$. That is, we abbreviate

$$
x_{K}(j \rightarrow i)=\left\{x_{K}: j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)\right\}
$$

and for a path $\pi$ we similarly write

$$
x_{K}(\pi)=\bigcap_{v \rightarrow u \in \pi} x_{K}(v \rightarrow u)
$$

Now consider a $*$-connecting path $\pi$ in $\mathcal{D}_{K}^{*}(C)$ and let

$$
\Sigma(\pi)=\left\{x_{K} \in \mathcal{L}_{K}^{C}:\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right) \odot x_{K}<x_{K}\right\}
$$

Lemma 6.15. Let $\pi$ be a $*$-connecting path in $\mathcal{D}_{K}^{*}(C)$. Suppose there exists $x_{K}$ such that all edges of $\pi$ are effective in the possible context $\left\{X_{K}=x_{K}\right\}$. Then $\Sigma(\pi)$ is a non-empty full-dimensional subset of $\mathbb{R}_{>}^{K}$.

Proof. By Proposition 6.14, $\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)<1$ so $\Sigma(\pi) \neq \emptyset$ by Proposition 2.1(c). Now, the smooth and invertible map $x \mapsto \log (x)$ has a regular total derivative and maps $\Sigma(\pi)$ to the relative interior of a classical polyhedron $Q$ defined by strict inequalities of the form

$$
y \in Q \Longleftrightarrow \text { for all } u, v \in V: y_{v}-y_{u}>\log \left(\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)_{u v}\right)
$$

where we have let $\log (0)=-\infty$. Thus, $Q$ is an intersection of finitely many open half-spaces. Since $\Sigma(\pi) \neq \emptyset$ we have $Q \neq \emptyset$ and $Q$ is open and full-dimensional. So $\Sigma(\pi)$ is open and full-dimensional.

Proposition 6.16. Consider a *-connecting path $\pi$ in $\mathcal{D}_{K}^{*}(C)$ with $\Sigma(\pi) \neq \emptyset$. Then there exists some $x_{K} \in \Sigma(\pi)$ such that in the possible context $\left\{X_{K}=x_{K}\right\}$ with corresponding node partition $V=A \cup H \cup L \cup U$, we have $L=\emptyset, K^{*}=K$, and all edges of $\pi$ are effective with respect to $\left\{X_{K}=x_{K}\right\}$.

Proof. For each $v \in V$ and each pair $h, k \in K$ such that $c_{h v}^{*}, c_{k v}^{*}>0$, let

$$
\mathcal{L}_{h k v}=\left\{x_{K}: \frac{x_{h}}{c_{h i}^{*}}=\frac{x_{k}}{c_{k i}^{*}} \text { for some } i \in V\right\} \quad \text { and } \quad \mathcal{L}=\bigcup_{h, k, v: \mathcal{L}_{h k v} \neq \emptyset} \mathcal{L}_{h k v}
$$

Note that $\mathcal{L}$ is a finite union of subspaces, each of codimension 1 in $\mathbb{R}_{>}^{V}$. By Lemma 6.15, $\Sigma(\pi)$ is full-dimensional and non-empty, so $\Sigma(\pi) \backslash(\mathcal{L} \cap \Sigma(\pi))$ is non-empty. Let $x_{K}$ be in this set. Write $V=A \cup H \cup L \cup U$ w.r.t. the context $\left\{X_{K}=x_{K}\right\}$. Since $x_{K} \in \Sigma(\pi)$,

$$
\Gamma_{K K} \odot x_{K} \leq\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right) \odot x_{K}<x_{K}
$$

Thus there are no pairs $h, k \in K$ with $h \neq k$ such that $x_{h}=c_{h k}^{*} x_{k}$. So $U=\emptyset$. In addition, $x_{K} \notin \mathcal{L}$. Thus by definition, $L=\emptyset$. So $K^{*}\left(X_{K}=x_{K}\right)=H$. Define the event $\mathcal{E} \subset \mathbb{R}_{>}^{V}$ via

- $Z_{k}=x_{k}$ for all $k \in K$
- $\max _{k \in K: c_{i k}^{*}>0} c_{i k}^{*} x_{k}<Z_{i}<\min _{k \in K: c_{k i}^{*}>0} x_{k} / c_{k i}^{*}$ for all remaining $i \in V$ (where the minimum over an empty set is 0 and the maximum over an empty set is $\infty$ ).
Since $U=\emptyset$, for each $i, \max _{k \in K: c_{i k}^{*}>0} c_{i k}^{*} x_{k}<\min _{k \in K: c_{k i}^{*}>0} x_{k} / c_{k i}^{*}$. Thus $\mathcal{E}$ is well-defined. By construction, $\mathcal{E} \subset\left\{X_{K}=x_{K}\right\}$ and it is full-dimensional w.r.t. this set. Thus there exists at least one $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $\mathcal{E}(g) \cap \mathcal{E} \neq \emptyset$. For this $g$, the only constant stars of $g$ have roots in $K$ and have no children. Thus $K^{*}(g)=K$. Since $K \subseteq K^{*} \subseteq K^{*}(g)$, it follows that $K^{*}=K$. Finally, since $x_{K} \in \Sigma(\pi)$,

$$
\Xi_{K}^{\pi} \odot x_{K} \leq\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right) \odot x_{K}<x_{K}
$$

So in particular, for each edge $j \rightarrow i \in \pi$,

$$
\Xi_{K}^{i j} \odot x_{K}<x_{K}
$$

Since $K=K^{*}\left(X_{K}=x_{K}\right)$, (6.5) holds. Lemma 6.11 then implies $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$.
Lemma 6.17. Let $\pi$ be a *-connecting path in $\mathcal{D}_{K}^{*}(C)$ with $\Sigma(\pi) \neq \emptyset$. Let $x_{K} \in \Sigma(\pi)$ that satisfies the conclusion of Proposition 6.16. Then $\pi \subseteq \mathcal{C}\left(X_{K}=x_{K}\right)$.

Proof. Fix an edge $j \rightarrow i$ of $\pi$ and $x_{K}$ as above. Since $\pi$ is $*$-connecting, $j \notin K$. There are two cases.
Case 1. $i \notin K$. We shall show that there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ that contains the edge $j \rightarrow i$, and that this edge is not part of a constant star of $g$. To do this, we construct a region $\mathcal{E}$ in the manner similar to the proof of Theorem 6.2, case b(I). Apply (4.7) to $j$ and let $\beta_{j}$ be the constant on the right-hand side of this inequality. That is,

$$
\beta_{j}=\min _{k \in K: k \in \mathrm{ch}_{K}^{*}(j)} \frac{x_{k}}{c_{k j}^{*}}
$$

Let

$$
\gamma_{j}=\frac{1}{c_{i j}^{*}} \max _{\ell \in \mathrm{pa}_{K}^{*}(i)} x_{\ell} c_{i \ell}^{*}
$$

Since $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$ and $i \notin K$, by (6.5) we have

$$
\left(\xi_{K}^{i j}\right)_{k \ell} x_{\ell}<x_{k}
$$

for all $k \in \operatorname{ch}_{\mathcal{D}^{*}}(j)$ and $\ell \in \mathrm{pa}_{\mathcal{D}^{*}}(i)$. Rearranging gives

$$
\frac{x_{k}}{c_{k j}^{*}}>\frac{x_{\ell} c_{i \ell}^{*}}{c_{i j}^{*}} \text { for all } k \in \operatorname{ch}_{K}^{*}(j), \ell \in \mathrm{pa}_{K}^{*}(i)
$$

or equivalently, $\beta_{j}>\gamma_{j}$. For a sufficiently small constant $\epsilon>0$, consider the region $\mathcal{E}$ defined by

- $\gamma_{j}<Z_{j}<\beta_{j}$
- for each $h \in H$, set $Z_{h}=x_{h}$
- $Z_{r}<\epsilon$ for all other nodes.

In the above, the only nodes that were mentioned but did not get set to be less than $\epsilon$ are $Z_{j}$ and $Z_{h}$ for $h \in H$. By Proposition 3.18 and (6.1), these nodes are all distinct. Since $\beta_{j}>\gamma_{j}$, $Z_{j}$ is well-defined. Since $L=\emptyset, \mathcal{E}$ is a non-empty polyhedron in $\mathbb{R}_{>}^{V}, \mathcal{E} \subseteq\left\{X_{K}=x_{K}\right\}$, and $\mathcal{E}$ is full-dimensional relative to the region $\left\{X_{K}=x_{K}\right\}$. Therefore, there exists at least one $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ with $\mathcal{E}(g) \cap \mathcal{E} \neq \emptyset$. Now suppose $Z \in \mathcal{E}$. Then $Z_{j}>\gamma_{j}$ implies

$$
c_{i j}^{*} Z_{j}>c_{i \ell}^{*} x_{\ell}
$$

for all $\ell \in K$. In addition, $Z_{j} \gg \epsilon>Z_{r}, Z_{i}$ implies

$$
c_{i j}^{*} Z_{j}>c_{i r}^{*} x_{r}
$$

for all $r \neq j, r \notin K$ such that $c_{i r}^{*}>0$. Thus $R_{g}(i)=j$, so in particular, $j \rightarrow i \in g$.
Since $Z_{j}<\beta_{j}$, it follows that

$$
c_{k i}^{*} Z_{j}<x_{k}
$$

for all $k \in K \cap \operatorname{ch}_{K}^{*}(j)$. Since $K^{*}=K, j \notin K^{*}(g)$, so $j \rightarrow i \notin E^{-}\left(X_{K}=x_{K}\right)$. Thus $j \rightarrow i \in \mathcal{C}\left(X_{K}=x_{K}\right)$. We are done.
Case 2. $i \in K$. Since $j \rightarrow i \in E^{+}\left(X_{K}=x_{K}\right)$, we can rearrange (6.5) to obtain

$$
\min _{k \in \operatorname{ch}_{G}(j), k \neq i} \frac{x_{k}}{c_{k j}^{*}} \geq \frac{x_{i}}{c_{i j}^{*}}
$$

As $L=\emptyset$, by definition of $L, x_{K}$ satisfies the stronger inequality

$$
\min _{k \in \operatorname{ch}_{G}(j), k \neq i} \frac{x_{k}}{c_{k j}^{*}}>\frac{x_{i}}{c_{i j}^{*}}
$$

Since $i \in K$, it is sufficient to show that $j \rightarrow i \in \mathcal{I}\left(X_{K}=x_{K}\right)$. That is, we need to construct $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $j \rightarrow i \in g$. For a very small constant $\epsilon>0$, consider the region $\mathcal{E}_{1}$ defined by

- for each $h \in H, h \neq i$, set $Z_{h}=x_{h}$

- $Z_{j}=x_{j} / c_{i j}^{*}$
- $Z_{r}<\epsilon$ for all other nodes.

Since $L=\emptyset, \mathcal{E}$ is well-defined and is full-dimensional relative to the region $\left\{X_{K}=x_{K}\right\}$. By (6.9), $Z_{j}$ satisfies (4.7), so $\mathcal{E} \subset\left\{X_{K}=x_{K}\right\}$. Therefore, there exists some $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ such that $\mathcal{E}(g) \cap \mathcal{E}_{1} \neq \emptyset$. On $\mathcal{E}_{1}$, by construction, $j \rightarrow i \in g$ and the proof is complete.

For given matrix $C$ we now have the following result. This implies that $\perp_{C^{*}}$ is not fully complete w.r.t. conditional independence for a given matrix $C$, as not all $*$-connecting critical paths may be effective, as seen in Example 6.3.

THEOREM 6.18 (Context-free completeness). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ with fixed coefficient matrix $C$. It then holds that

$$
X_{I} \not \perp X_{J} \mid X_{K}
$$

if and only if there is an effective *-connecting path in the critical $D A G \mathcal{D}_{K}^{*}(C)$.
Proof. By Theorem 5.14 and Theorem 6.2, $X_{I} \not \perp X_{J} \mid X_{K}$ if and only if there exists some $i \in I, j \in J$, some possible $x_{K}$, and some $*$-connecting path $\pi$ between $i$ and $j$ such that $\pi \subseteq \mathcal{C}\left(X_{K}=x_{K}\right)$. Thus the statement in the proposition is equivalent to the claim that (6.4) holds if and only if there exists $x_{K}$ such that $\pi \subseteq \mathcal{C}\left(X_{K}=x_{K}\right)$.

So suppose (6.4) holds. By Proposition 2.1(c), $\Sigma(\pi) \neq \emptyset$. By Proposition 6.16, we can pick a special $x_{K}$. Applying Lemma 6.17 to this special $x_{K}$, we conclude that $\pi \subseteq \mathcal{C}\left(X_{K}=x_{K}\right)$.

For the converse, suppose $x_{K}$ is such that $\pi \subseteq \mathcal{C}\left(X_{K}=x_{K}\right)$. By Corollary 6.12, each edge of $\pi$ is in $E^{+}\left(X_{K}=x_{K}\right)$. By Proposition 6.14, this implies that $\pi_{K}$ is effective.

REMARK 8. We note that we now could define yet another form of separation which we could name effective *-separation and by Theorem 6.18 this would now be strongly complete for conditional independence for a given $C$ or, in other words, any max-linear Bayesian network would be faithful to this criterion. However, whereas checking critical separation is a simple task, checking effective $*$-separation would involve calculating $\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{a}\right)$ for all $*$-connecting paths $\pi$, so we have preferred not to introduce this variant of separation in this article.

Finally we are able to establish full completeness of $\perp_{\mathcal{D}^{*}}$-separation for an unspecified coefficient matrix $C$.

THEOREM 6.19 (Completeness of $\perp_{\mathcal{D}^{*}}$-separation). Let $X$ be a max-linear Bayesian network over a directed acyclic graph $\mathcal{D}=(V, E)$ and assume there is a $*$-connecting path in $\mathcal{D}_{K}^{*}$ between $I$ and $J$. Then there is a coefficient matrix $C$ with support included in $\mathcal{D}$ such that the corresponding max-linear Bayesian network satisfies

$$
X_{I} \not \perp X_{J} \mid X_{K}
$$

Proof. Let $\pi$ be a $*$-connecting path in $\mathcal{D}_{K}^{*}$ between $I$ and $J$. For each of the five types, our goal is to construct a $C$ such that $\pi \subset \mathcal{D}_{K}^{*}(C)$ and that (6.4) holds, i.e. the path $\pi$ is effective.

For each edge $v \rightarrow u \in \pi$, let $\pi_{u v} \subset \mathcal{D}$ be a path in $\mathcal{D}$ from $v$ to $u$ that does not factor through $K$. Define $C=C(\pi)$ as follows.

- If $a \rightarrow b \in \bigcup_{v \rightarrow u \in \pi} \pi_{u v}$, set $c_{b a}=1$
- Otherwise, set $c_{b a}$ to be some constant such that $c_{b a}<1$.

First we claim that for this choice of $C, \pi \subset \mathcal{D}_{K}^{*}(C)$. That is, for each edge $a \rightarrow b \in \pi$, no critical paths from $a$ to $b$ on $C$ factor through $K$. Indeed, fix such an edge $a \rightarrow b \in \pi$. Let $\pi_{b a}^{\prime}$ be another path in $\mathcal{D}$. Then either $\pi_{b a}^{\prime}$ contains an edge not in $\bigcup_{u \rightarrow v \in \pi} \pi_{v u}$, in which case

$$
c\left(\pi_{b a}^{\prime}\right)<c\left(\pi_{b a}\right)=1
$$

or that it only uses edges in $\bigcup_{v \rightarrow u \in \pi} \pi_{u v}$ and

$$
c\left(\pi_{b a}^{\prime}\right)=c\left(\pi_{b a}\right)=1
$$

But in this case, since none of the paths $\pi_{v u}$ factor through $K, \pi_{b a}^{\prime}$ does not factor through $K$. This establishes our first claim.

We now prove (6.4). Note that all relevant substitution matrices are formed by combining substitution matrices for single edges $\Xi_{K}^{i j}$ for $j \notin K$ and we now claim that each entry of such a matrix is strictly less than 1 .

As shown above, we must have $c_{i j}^{*}=1$. Let $k \in K \cap \operatorname{ch}_{\mathcal{D}^{*}}(j), \ell \in K \cap\left(\operatorname{pa}_{\mathcal{D}^{*}}(i) \cup\{i\}\right), k \neq \ell$ so we again have $c_{i \ell}^{*}=1$. Since $k \notin \pi$, any path in $\mathcal{D}$ from $j$ to $k$ must utilize an edge of $C$ whose weight is strictly less than 1 with the choice of $C$ made above. Thus $c_{k j}^{*}<1$. By (6.3),

$$
\left(\Xi_{K}^{i j}\right)_{k \ell}=\frac{c_{k j}^{*} c_{i \ell}^{*}}{c_{i j}^{*}}=c_{k j}^{*} c_{i \ell}^{*}=c_{i \ell}^{*}<1
$$

So each entry of $\Xi_{K}^{i j}$ is strictly less than 1 , as claimed, and hence this also holds for $\Xi_{K}^{\pi}$. Since $c_{u v} \leq 1$ for all edges $v \rightarrow u \in \mathcal{D}$, we have $\gamma_{u v}=c_{u v}^{*} \leq 1$ for all edges $v \rightarrow u \in \mathcal{D}^{*}$. Thus

$$
\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right) \leq 1
$$

Suppose now for contradiction that $\lambda\left(\Gamma_{K K} \vee \Xi_{K}^{\pi}\right)=1$. Since all entries of $\Xi_{K}^{\pi}$ are strictly less than 1 , a critical cycle of $\Gamma_{K K} \vee \Xi_{K}^{\pi}$ must only involve edges in $\Gamma_{K K}$. But $\mathcal{D}$ is a DAG, so $\mathcal{D}\left(\Gamma_{K K}\right)$ is cycle-free, yielding a contradiction. This concludes the proof.

# 7. Outlook. 

7.1. Properties of max-linear independence. In the previous section we have defined two abstract independence models $\perp_{\mathcal{D}^{*}}$ and $\perp_{C^{*}}$ in the sense of [27] and showed that they are sound and the former of them is also complete, whereas the latter needs additional conditions for completeness.

One can show without too much effort that these are both compositional graphoids (we refrain from giving the details) as also holds for most other graphical separation criteria (see e.g. [23]). However, we should emphasize that $\perp_{\mathcal{D}^{*}}$ is not strongly complete as the Diamond example shows: in this example the classical $d$-separation $\perp_{\mathcal{D}}$ and $\perp_{\mathcal{D}^{*}}$ coincide and there is no single coefficient matrix $C$ such that the corresponding max-linear Bayesian network is faithful to $\perp_{\mathcal{D}^{*}}$, i.e. in that case $\perp_{\mathcal{D}^{*}}$ is strictly weaker than critical separation $\perp_{C^{*}}$, and the same will happen for DAGs with more than a single directed path between any two points. But even in this case, the context-specific analysis typically yields further valid conditional independence statements.

Generally, the study of properties of conditional independence for max-linear models opens up several new avenues: concerning e.g. Markov equivalence as in [28, 12], or the algebraic properties of maxoids as an analogue of gaussoids; see, for example [6].

7.2. Extensions and special cases. We have so far in this article not discussed identifiability, estimation, or any other statistical issues associated with these models. These have been briefly considered in [16]; see also [14]. This work was extended to a recursive max-linear model with propagating noise in [7], but we are not considering models with noise in this article.

Extreme value models often rely on regular variation and several publications have combined Bayesian networks with such heavy-tailed innovations. In [17] and [20], algorithms have been proposed for statistically learning the model based on the estimated tail dependence matrix and on a scaling method, respectively. In [11] for undirected graphs the authors apply a peaks-over-threshold approach giving a multivariate generalized Pareto distribution for exceedances such that a density exists. For a decomposable graph, this density factorizes into lower dimensional marginal densities, whereas [9] deals with conditional densities.

Natural extensions in the framework of recursive max-linear models are based on making dependent innovations $\left(Z_{1}, \ldots, Z_{d}\right)$, thus defining the analogue of classical path analysis ([30, 31]), or recursive causal models; see [19]. The models introduced by [11] could be interesting candidates for this.

An alternative for an appropriate model may originate from multivariate max-stable Fréchet distributions with distribution function (see e.g. [10], Section 6.1.4 and in particular Remark 6.1.16 with parametrization given in Theorem 1.1.3)

$$
F(z)=\exp \left\{-\int_{\mathcal{S}^{d-1}} \bigvee_{1 \leq i \leq d} \frac{\omega_{i}}{z_{i}} \Theta(d \omega)\right\}, \quad z=\left(z_{1}, \ldots, z_{d}\right)
$$

where $\omega=\left(\omega_{1}, \ldots, \omega_{d}\right) \in \mathcal{S}^{d-1}$, the unit sphere in $\mathbb{R}_{+}^{d}$ (with respect to any norm), and $\Theta$ is a finite measure on $S^{d-1}$, called the spectral measure. Then the innovation vector $\left(Z_{1}, \ldots, Z_{d}\right)$ has Fréchet margins with algebraically decreasing tails. If the spectral measure has a Lebesgue density, then the above integral becomes a Lebesgue integral. Then a large jump can happen in every direction with some probability. The Bayesian network introduces additional dependence into the model, which directs the large jumps in special directions.
7.3. Some open problems. Proposition 3.18 gives some necessary conditions for a graph to be the source DAG for some context $\left\{X_{K}=x_{K}\right\}$. It would be of interest to know whether these are also sufficient. Formally this is stated as Problem 1 below:

Problem 1. Fix $\mathcal{D}$. Find a characterization for all possible source DAGs.
Further, even though we have a full characterization of situations with conditional independence, there is still an issue about how to verify conditional independence from a computational point of view. Formally, we state this as

Problem 2. Give an efficient algorithm to compute the source DAG $\mathcal{C}\left(X_{K}=x_{K}\right)$ and analyze its complexity.

Critical directed paths in a graph can be computed with tropical matrix multiplication [8, $\S 3]$, and thus $\mathcal{D}_{K}^{*}$ and $\mathcal{D}_{K}^{*}(C)$ can both easily be computed in time at most $O\left(d^{4}\right)$. However, computing the source DAG is harder. A straight-forward algorithm using the characterization of the impact graphs $\mathfrak{G}\left(X_{K}=x_{K}\right)$ in Lemma 3.13 goes as follows.

1. Enumerate all elements in $\mathfrak{G}\left(X_{K}=x_{K}\right)$ using the system of equations and inequalities given in Theorem 3.3 and Lemma 3.13, with $K^{*}(g)$ characterized by Lemma 3.11.
2. Compute $K^{*}=K^{*}\left(X_{K}=x_{K}\right)$ from $\mathfrak{G}\left(X_{K}=x_{K}\right)$ via Definition 3.10.
3. Compute the source DAG via Theorem 4.3.

Of these steps, step 1 is the most computationally intensive. The set $\mathfrak{G}\left(X_{K}=x_{K}\right)$ represents all possible hitting scenarios in [29]. For general $C$ (not necessarily supported on a DAG), [29] noted that enumerating $\mathfrak{G}\left(X_{K}=x_{K}\right)$ is related to the NP-hard set covering problem. For our case, $C$ is a DAG, so we were able to characterize $\mathfrak{G}\left(X_{K}=x_{K}\right)$ in much greater detail than [29]. However, it is unclear what is the complexity of enumerating this set. The difficulty is that the inequalities corresponding to (3.3), (3.9) and (3.10) depend on $g$. So while it is easy to check whether $g \in \mathfrak{G}\left(X_{K}=x_{K}\right)$ for a given $g$, there are exponentially many impact graphs $g$ one needs to consider.

We remark that Problem 2 can be seen as finding the tropical analogue of Gaussian elimination. While there has been work on the tropical Fourier-Motzkin elimination [1], we are not aware of algorithms to solve tropical Gaussian elimination. The geometric relative of this problem is to find minimal external representations of tropical polyhedra, to which algorithms and characterizations in terms of hypergraphs have been developed e.g. in [2, 3, 4]. It would be interesting to deepen these connections between extreme value theory and tropical convex geometry. A related problem is the following:

Problem 3. Give an efficient algorithm to simulate from the conditional distribution of $X$, given a context $\left\{X_{K}=x_{K}\right\}$.

This problem was also considered by [29] and has particular interest for Bayesian inference about the unknown parameters of a max-linear Bayesian network. Most Markov chain Monte Carlo (MCMC) algorithms will have such a simulation step built in at some point. In addition, this could be of interest if an unknown source for an observed extreme event should be identified, potentially of interest in environmental science.

Acknowledgements. Carlos Améndola was partially supported by the Deutsche Forschungsgemeinschaft (DFG) in the context of the Emmy Noether junior research group KR 4512/1-1. Steffen Lauritzen has benefited from financial support from the Alexander von Humboldt Stiftung. Ngoc Tran would like to thank the Hausdorff Center for Mathematics for making her summer research visits to Germany possible.

# References. 

[1] X. Allamigeon, U. Fahrenberg, S. Gaubert, R. D. Katz, and A. Legay. Tropical Fourier-Motzkin elimination, with an application to real-time verification. International Journal of Algebra and Computation, 24(05):569-607, 2014.
[2] X. Allamigeon, S. Gaubert, and É. Goubault. Computing the vertices of tropical polyhedra using directed hypergraphs. Discrete $\mathcal{G}$ Computational Geometry, 49(2):247-279, 2013.
[3] X. Allamigeon, S. Gaubert, and R. D. Katz. Tropical polar cones, hypergraph transversals, and mean payoff games. Linear algebra and its Applications, 435(7):1549-1574, 2011.
[4] X. Allamigeon and R. D. Katz. Minimal external representations of tropical polyhedra. Journal of Combinatorial Theory, Series A, 120(4):907-940, 2013.
[5] F. Baccelli, G. Cohen, G. J. Olsder, and J-P. Quadrat. Synchronization and Linearity: An Algebra for Discrete Event Systems. John Wiley \& Sons Ltd, 1993.
[6] T. Boege, A. D'Alí, T. Kahle, and B. Sturmfels. The geometry of gaussoids. Foundations of Computational Mathematics, 19:775-812, 2019.

[7] J. Buck and C. Klüppelberg. Recursive max-linear models with propagating noise. arXiv:2003.00362, 2020 .
[8] P. Butkovič. Max-linear Systems: Theory and Algorithms. Springer, London, 2010.
[9] D. Cooley, R.A. Davis, and P. Naveau. Approximating the conditional density given large observed values via a multivariate extremes framework, with application to environmental data. Annals of Applied Statistics, 6:1406-1429, 2012.
[10] L. de Haan and A. Ferreira. Extreme Value Theory: An Introduction. Springer, New York, 2006.
[11] S. Engelke and A. Hitz. Graphical models for extremes. J. Roy. Statist. Soc. Ser. B, 82:871-932, 2020.
[12] M. Frydenberg. The chain graph Markov property. Scandinavian Journal of Statistics, 17:333-353, 1990.
[13] D. Geiger, T. S. Verma, and J. Pearl. Identifying independence in Bayesian networks. Networks, 20(5):507534, 1990.
[14] N. Gissibl. Graphical Modeling of Extremes: Max-linear models on directed acyclic graphs. Ph.D. thesis, Technical University of Munich, 2018.
[15] N. Gissibl and C. Klüppelberg. Max-linear models on directed acyclic graphs. Bernoulli, 24(4A):26932720, 2018.
[16] N. Gissibl, C. Klüppelberg, and S. L. Lauritzen. Estimation, identifiability, and structure learning of recursive max-linear models. Scand. J. Statist., 47:To appear, 2020. https://doi.org/10.1111/sjos. 12446.
[17] N. Gissibl, C. Klüppelberg, and M. Otto. Tail dependence of recursive max-linear models with regularly varying noise variables. Econometrics and Statistics, 6:149 - 167, 2018.
[18] M. Joswig. Essentials of Tropical Combinatorics. Springer, Heidelberg, 2020.
[19] H. Kiiveri, T. P. Speed, and J. B. Carlin. Recursive causal models. Journal of the Australian Mathematical Society, 36:30-52, 1984.
[20] C. Klüppelberg and M. Krali. Estimating an extreme Bayesian network via scalings. Journal of Multivariate Analysis, to appear; arXiv:1912.03968, 2020.
[21] C. Klüppelberg and S. Lauritzen. Bayesian networks for max-linear models. In F. Biagini, G. Kauermann, and T. Meyer-Brandis, editors, Network Science - An Aerial View, pages 79-97. Springer Nature, 2019.
[22] D. Koller and N. Friedman. Probabilistic Graphical Models: Principles and Techniques. MIT Press, Cambridge, Mass., 2009.
[23] S. Lauritzen and K. Sadeghi. Unifying Markov properties for graphical models. Annals of Statistics, $46: 2251-2278,2018$.
[24] S. L. Lauritzen. Graphical Models. Oxford University Press, Oxford, 1996.
[25] S. L. Lauritzen, A. P. Dawid, B. N. Larsen, and H-G. Leimer. Independence properties of directed Markov fields. Networks, 20(5):491-505, 1990.
[26] D. Maclagan and B. Sturmfels. Introduction to Tropical Geometry. Graduate Studies in Mathematics, Vol. 161. American Mathematical Society, Providence, Rhode Island, 2015.
[27] M. Studený. Probabilistic Conditional Independence Structures. Information Science and Statistics. Springer, London, 2005.
[28] T. Verma and J. Pearl. Equivalence and synthesis of causal models. In Proceedings of the 6th Conference on Uncertainty in Artifical Intelligence, pages 220-227, Cambridge, Mass., 1990. MIT Press.
[29] Y. Wang and S. A. Stoev. Conditional sampling for spectrally discrete max-stable random fields. Advances in Applied Probability, 43(2):461-483, 2011.
[30] S. Wright. Correlation and causation. Journal of Agricultural Research, 20:557-585, 1921.
[31] S. Wright. The method of path coefficients. Annals of Mathematical Statistics, 5:161-215, 1934.

Center for Mathematical Sciences
Technical University of Munich
Boltzmanstrasse 3
85748 Garching, Germany
E-MAIL: carlos.amendola@tum.de
Department of Mathematical Sciences
University of Copenhagen
Universitetsparken 5
2100 Copenhagen, Denmark
E-MAIL: lauritzen@math.ku.dk

Center for Mathematical Sciences
Technical University of Munich
Boltzmanstrasse 3
85748 Garching, Germany
E-MAIL: cklu@tum.de
Department of Mathematics
University of Texas at Austin
Speedway 2515 Stop C1200
Austin TX 78712, USA
E-MAIL: ntran@math.utexas.edu