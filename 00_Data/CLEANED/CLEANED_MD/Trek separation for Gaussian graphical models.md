# TREK SEPARATION FOR GAUSSIAN GRAPHICAL MODELS 

By Seth SulliVANT ${ }^{1}$, Kelli Talaska ${ }^{2}$ and Jan Draisma ${ }^{3}$<br>North Carolina State University, University of Michigan and Technische Universiteit Eindhoven


#### Abstract

Gaussian graphical models are semi-algebraic subsets of the cone of positive definite covariance matrices. Submatrices with low rank correspond to generalizations of conditional independence constraints on collections of random variables. We give a precise graph-theoretic characterization of when submatrices of the covariance matrix have small rank for a general class of mixed graphs that includes directed acyclic and undirected graphs as special cases. Our new trek separation criterion generalizes the familiar $d$-separation criterion. Proofs are based on the trek rule, the resulting matrix factorizations and classical theorems of algebraic combinatorics on the expansions of determinants of path polynomials.


1. Introduction. Given a graph $G$, a graphical model is a family of probability distributions that satisfy some conditional independence constraints which are determined by separation criteria in terms of the graph. In the case of normal random variables, conditional independence constraints correspond to low rank submatrices of the covariance matrix $\Sigma$ of a special type. Thus for Gaussian graphical models, the graphical separation criteria correspond to special submatrices of the covariance matrix having low rank.

Consider first the case where $G$ is a directed acyclic graph. In this case, a conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for every distribution consistent with the graphical model if and only if $C d$-separates $A$ from $B$ in $G$. For normal random variables the conditional independence constraint $X_{A} \Perp X_{B} \mid X_{C}$ is equivalent to the condition $\operatorname{rank} \Sigma_{A \cup C, B \cup C}=\# C$ where $\Sigma_{A \cup C, B \cup C}$ is the submatrix of the covariance matrix $\Sigma$ with row indices $A \cup C$ and column indices $B \cup C$. However, the drop of rank of a general submatrix $\Sigma_{A, B}$ does not necessarily correspond to a conditional independence statement that is valid for the graph, and will not, in general, come from a $d$-separation criterion. Our main result for directed graphical models is a new separation criterion ( $t$-separation) which gives a complete characterization of when submatrices of the covariance matrix will drop rank and what the generic lower rank of that matrix will be.

[^0]
[^0]:    Received December 2008; revised September 2009.
    ${ }^{1}$ Supported by NSF Grant DMS-08-40795.
    ${ }^{2}$ Supported by NSF Grants DMS-05-02170 and DMS-05-55880.
    ${ }^{3}$ Supported by DIAMANT, an NWO mathematics cluster.
    AMS 2000 subject classifications. Primary 62H99, 62J05; secondary 05A15.
    Key words and phrases. Graphical model, Bayesian network, Gessel-Viennot-Lindström lemma, trek rule, linear regression, conditional independence.

One of the main reasons for searching for necessary and sufficient conditions for matrices to drop rank comes from the search for a unified perspective on rank conditions implied by the $d$-separation criterion and the tetrad representation theorem [12], which characterizes $2 \times 2$ vanishing determinants in directed acyclic graphs. The $t$-separation criterion unifies both of these results under a simple and more general umbrella.

A second reason for introducing $t$-separation is that it provides a new set of tools for performing constraint-based inference in Gaussian graphical models. This approach was pioneered by the TETRAD program [10] where vanishing tetrad constraints are used to infer the structure of hidden variable graphical models. The mathematical underpinning of the TETRAD program is the above-mentioned tetrad representation theorem [12]. In fact, the impetus for this project was a desire to develop a better understanding of the tetrad representation theorem. The original proof of the tetrad representation theorem is lengthy and complicated, and some simplifications appear in subsequent work [11, 13]. Our result has the advantage of being considerably broader, while our proof is more elementary. The notion that algebraic determinantal constraints could be useful for inferring graphical structures is further supported by recent results on the distribution of the evaluation of determinants of Wishart matrices [4] which would be an essential tool for developing Wald-type tests in this setting.

Section 2 gives the setup of Gaussian graphical models and states the main results on $t$-separation. To describe the main result we need to recall the notion of treks which are special paths in the graph $G$. These are the main objects used in the trek rule, a combinatorial parametrization of covariance matrices that belong to the Gaussian graphical model. We make a special distinction between general treks and simple treks and introduce two trek rules. These results are probably well known to experts but are difficult to find in the literature. Then we make precise the $t$-separation criterion and state our main results about it. This section is divided into subsections: stating our results first for directed graphical models, then undirected graphical models and finally the more general mixed graphs. The purpose for this division is twofold: it extracts the two most common classes of graphical models and it mirrors the structure of the proof of the main results.

Section 3 is concerned with the proofs of the main results. The main idea is to exploit the trek rule which expresses covariances as polynomials in terms of treks in the graph $G$. The expansion of determinants of matrices of path polynomials is a classical problem in algebraic combinatorics covered by the Gessel-ViennotLindström lemma, which we exploit in our proof. The final tool is Menger's theorem on flows in graphs.
2. Treks and $\boldsymbol{t}$-separation. This section provides background on and definitions of treks as well as the statements of our main results on $t$-separation for Gaussian graphical models. We describe necessary and sufficient conditions for directed and undirected graphs first, and then address the general case of mixed graphs. The proofs in Section 3 also follow the same basic format.

2.1. Directed graphs. Let $G$ be a directed acyclic graph with vertex set $V(G)=[m]:=\{1,2, \ldots, m\}$. We assume $G$ is topologically ordered, that is, we have $i<j$ whenever $i \rightarrow j \in E(G)$. A parent of a vertex $j$ is a node $i \in V(G)$ such that $i \rightarrow j$ is an edge in $G$. The set of all parents of a vertex $j$ is denoted $\mathrm{pa}(j)$. Given such a directed acyclic graph, one introduces a family of normal random variables that are related to each other by recursive regressions.

To each node $i$ in the graph, we introduce a random variable $X_{i}$ and a random variable $\varepsilon_{i}$. The $\varepsilon_{i}$ are independent normal random variables $\varepsilon_{i} \sim \mathcal{N}\left(0, \phi_{i}\right)$ with $\phi_{i}>0$. We assume that all our random variables have mean zero for simplicity. The recursive regression property of the DAG gives an expression for each $X_{j}$ in terms of $\varepsilon_{j}$, those $X_{i}$ with $i<j$ and some regression parameters $\lambda_{i j}$ assigned to the edges $i \rightarrow j$ in the graph

$$
X_{j}=\sum_{i \in \mathrm{pa}(j)} \lambda_{i j} X_{i}+\varepsilon_{j}
$$

From this recursive sequence of regressions, one can solve for the covariance matrix $\Sigma$ of the jointly normal random vector $X$. This covariance matrix is given by a simple matrix factorization in terms of the regression parameters and the variance parameters $\phi_{i}$. Let $\Phi$ be the diagonal matrix $\Phi=\operatorname{diag}\left(\phi_{1}, \ldots, \phi_{m}\right)$. Let $L$ be the $m \times m$ upper triangular matrix with $L_{i j}=\lambda_{i j}$ if $i \rightarrow j$ is an edge in $G$, and $L_{i j}=0$ otherwise. Set $\Lambda=I-L$ where $I$ is the $m \times m$ identity matrix.

Proposition 2.1 ([9], Section 8). The variance-covariance matrix of the normal random variable $X=\mathcal{N}(0, \Sigma)$ is given by the matrix factorization

$$
\Sigma=\Lambda^{-\top} \Phi \Lambda^{-1}
$$

Given two subsets $A, B \subset[m]$, we let $\Sigma_{A, B}=\left(\sigma_{a b}\right)_{a \in A, b \in B}$ be the submatrix of covariances with row index set $A$ and column index set $B$. If $A=B=[m]$, we abbreviate and say that $\Sigma_{[m],[m]}=\Sigma$. Conditional independence statements for normal random variables can be detected by investigating the determinants of submatrices of the covariance matrix [13].

Proposition 2.2. Let $X \sim \mathcal{N}(\mu, \Sigma)$ be a normal random variable, and let $A, B$, and $C$ be disjoint subsets of $[m]$. Then the conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for $X$, if and only if $\Sigma_{A \cup C, B \cup C}$ has rank $C$.

Often in the statistical literature, the conditional independence conditions of a normal random variable are specified by saying that partial correlations are equal to zero. Proposition 2.2 is just an algebraic reformulation of that standard characterization.

A classic result of the graphical models literature is the characterization of precisely which conditional independence statements hold for all densities that belong to the graphical model. This characterization is determined by the $d$-separation criterion.

Definition 2.3. Let $A, B$ and $C$ be disjoint subsets of $[m]$. The set $C d i$ rected separates or $d$-separates $A$ and $B$ if every path (not necessarily directed) in $G$ connecting a vertex $i \in A$ to a vertex $j \in B$ contains a vertex $k$ that is either:

1. a noncollider that belongs to $C$ or
2. a collider that does not belong to $C$ and has no descendants that belong to $C$, where $k$ is a collider if there exist two edges $a \rightarrow k$ and $b \rightarrow k$ on the path and a noncollider otherwise.

THEOREM 2.4 (Conditional independence for directed graphical models [7]). A set $C d$-separates $A$ and $B$ in $G$ if and only if the conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for every distribution in the graphical model associated to $G$.

Combining Proposition 2.2 and Theorem 2.4 gives a characterization of when all the $(\# C+1) \times(\# C+1)$ minors of a submatrix $\Sigma_{A \cup C, B \cup C}$ must vanish. However, not every vanishing subdeterminant of a covariance matrix in a Gaussian graphical model comes from a $d$-separation criterion, as the following example illustrates.

Example 2.5 (Choke point). Consider the graph in Figure 1 with five vertices and five edges. In this graph, the determinant $\left|\Sigma_{13,45}\right|=0$ for any choice of model parameters. However, this vanishing rank condition does not follow from any single $d$-separation criterion/conditional independence statement that is implied by the graph.

Our main result is an explanation of where these extra vanishing determinants come from, for Gaussian directed graphical models. Before we give the precise explanation in terms of treks, we want to first explain how they enter the story.

DEFINITION 2.6. A trek in $G$ from $i$ to $j$ is an ordered pair of directed paths $\left(P_{1}, P_{2}\right)$ where $P_{1}$ has sink $i, P_{2}$ has sink $j$, and both $P_{1}$ and $P_{2}$ have the same source $k$. The common source $k$ is called the top of the trek, denoted $\operatorname{top}\left(P_{1}, P_{2}\right)$. Note that one or both of $P_{1}$ and $P_{2}$ may consist of a single vertex, that is, a path with no edges. A trek $\left(P_{1}, P_{2}\right)$ is simple if the only common vertex among $P_{1}$ and
![img-0.jpeg](img-0.jpeg)

Fig. 1.

$P_{2}$ is the common source $\operatorname{top}\left(P_{1}, P_{2}\right)$. We let $\mathcal{T}(i, j)$ and $\mathcal{S}(i, j)$ denote the sets of all treks and all simple treks from $i$ to $j$, respectively.

Expanding the matrix product for $\Sigma$ in Proposition 2.1 gives the following trek rule for the covariance $\sigma_{i j}$ :

$$
\sigma_{i j}=\sum_{\left(P_{1}, P_{2}\right) \in \mathcal{T}(i, j)} \phi_{\operatorname{top}\left(P_{1}, P_{2}\right)} \lambda^{P_{1}} \lambda^{P_{2}}
$$

where for each path $P, \lambda^{P}$ is the path monomial of $P$ defined by

$$
\lambda^{P}:=\prod_{k \rightarrow l \in P} \lambda_{k l}
$$

There is another rule for parameterizing the covariance matrices which involves sums over only the set $\mathcal{S}(i, j)$ of simple treks. To describe this, we introduce an alternate parameter $a_{i}$ associated to each node $i$ in the graph and defined by the rule

$$
a_{i}=\sigma_{i i}=\sum_{\left(P_{1}, P_{2}\right) \in \mathcal{T}(i, i)} \phi_{\operatorname{top}\left(P_{1}, P_{2}\right)} \lambda^{P_{1}} \lambda^{P_{2}}
$$

With the definition of the alternate parameter $a_{i}$, this leads to the parametrization, called the simple trek rule,

$$
\sigma_{i j}=\sum_{\left(P_{1}, P_{2}\right) \in \mathcal{S}(i, j)} a_{\operatorname{top}\left(P_{1}, P_{2}\right)} \lambda^{P_{1}} \lambda^{P_{2}}
$$

The simple trek rule is also known as Wright's method of path analysis [14]. While we will depend most heavily on the trek rule in this paper, the simple trek rule also has its uses. In particular, the simple trek rule played an important role in the study of Gaussian tree models in [13].

The fact that treks arise in the expressions for $\sigma_{i j}$ suggests that any combinatorial rule for the vanishing of a determinant $\Sigma_{A, B}$ should depend on treks in some way. This leads us to introduce the following separation criterion that involves treks.

DEFINITION 2.7. Let $A, B, C_{A}$, and $C_{B}$ be four subsets of $V(G)$ which need not be disjoint. We say that the pair $\left(C_{A}, C_{B}\right)$ trek separates (or $t$-separates) $A$ from $B$ if for every trek $\left(P_{1}, P_{2}\right)$ from a vertex in $A$ to a vertex in $B$, either $P_{1}$ contains a vertex in $C_{A}$ or $P_{2}$ contains a vertex in $C_{B}$.

REMARK. The following facts follow immediately from Definition 2.7:

1. Since a trek may consist of a single vertex $v$, or more precisely a pair of paths with zero edges, we must have $A \cap B \subset C_{A} \cup C_{B}$ whenever $\left(C_{A}, C_{B}\right)$ $t$-separates $A$ from $B$.

2. The pair $\left(C_{A}, C_{B}\right) t$-separates $A$ from $B$ if and only if the pair $\left(C_{B}, C_{A}\right)$ $t$-separates $B$ from $A$.
3. Each of the pairs $(A, \varnothing)$ and $(\varnothing, B)$ always $t$-separate $A$ from $B$, so we can always find a $t$-separating set of size $\min (\# A, \# B)$. Our results in this paper will show that $t$-separation gives nontrivial restrictions on the covariance matrix when $\# C_{A}+\# C_{B}<\min (\# A, \# B)$.

The combinatorial notion of $t$-separation allows us to give a complete characterization of when submatrices of the covariance matrix can drop rank. This is the main result for Gaussian directed graphical models; it will be proved in Section 3.1.

THEOREM 2.8 (Trek separation for directed graphical models). The submatrix $\Sigma_{A, B}$ has rank less than or equal to $r$ for all covariance matrices consistent with the graph $G$ if and only if there exist subsets $C_{A}, C_{B} \subset V(G)$ with $\# C_{A}+\# C_{B} \leq r$ such that $\left(C_{A}, C_{B}\right) t$-separates $A$ from $B$. Consequently,

$$
\operatorname{rk}\left(\Sigma_{A, B}\right) \leq \min \left\{\# C_{A}+\# C_{B}:\left(C_{A}, C_{B}\right) t \text {-separates } A \text { from } B\right\}
$$

and equality holds for generic covariance matrices consistent with $G$.
Here and throughout the paper, the term generic means that the condition holds on a dense open subset of the parameter space. Since rank conditions are algebraic, this means that the set where the inequality is strict is an algebraic subset of parameter space with positive codimension (see [2] for background on this algebraic terminology).

EXAMPLE 2.9 (Choke point, continued). Returning to the graph from Example 2.5 , we see that $(\varnothing,\{4\}) t$-separates $\{1,3\}$ from $\{4,5\}$ which implies that the submatrix $\Sigma_{13,45}$ has rank at most one for every matrix that belongs to the model. Thus $t$-separation explains this extra vanishing minor that $d$-separation misses.

Readers familiar with the tetrad representation theorem will recognize that $\{4\}$ is a choke point between $\{1,3\}$ and $\{4,5\}$ in $G$. In particular, Theorem 2.8 includes the tetrad representation theorem as a special case.

COROLLARY 2.10 (Tetrad representation Theorem [12]). The tetrad $\sigma_{i k} \sigma_{j l}-$ $\sigma_{i l} \sigma_{j k}$ is zero for all covariance matrices consistent with the graph $G$ if and only if there is a node $c$ in the graph such that either $(\{c\}, \varnothing)$ or $(\varnothing,\{c\})$ t-separates $\{i, j\}$ from $\{k, l\}$.

Since conditional independence in a directed graphical model corresponds to the vanishing of subdeterminants of the covariance matrix, the $t$-separation criterion can be used to characterize these conditional independence statements, as well.

THEOREM 2.11. The conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for the graph $G$ if and only if there is a partition $C_{A} \cup C_{B}=C$ of $C$ such that $\left(C_{A}, C_{B}\right)$ t-separates $A \cup C$ from $B \cup C$ in $G$.

Proof. The conditional independence statement holds for the graph $G$ if and only if the submatrix of the covariance matrix $\Sigma_{A \cup C, B \cup C}$ has rank $\# C$. By trek separation for directed graphical models, this holds if and only if there exists a pair of sets $D_{A}$ and $D_{B}$, with $\# D_{A}+\# D_{B}=\# C$ such that $\left(D_{A}, D_{B}\right) t$-separates $A \cup C$ from $B \cup C$. Among the treks from $A \cup C$ to $B \cup C$ are the lone vertices $c \in C$. Hence $C \subseteq D_{A} \cup D_{B}$. Since $\# D_{A}+\# D_{B}=\# C$, we must have $D_{A} \cup D_{B}=C$ and these two sets form a partition of $C$.

Theorem 2.11 immediately implies that $d$-separation is a special case of $t$-separation. Yanming Di [3] found a direct combinatorial proof of this fact after we made a preliminary version of this paper available.

Corollary 2.12. A set $C d$-separates $A$ and $B$ in $G$ if and only if there is a partition $C=C_{A} \cup C_{B}$ such that $\left(C_{A}, C_{B}\right) t$-separates $A \cup C$ from $B \cup C$.

While $t$-separation includes $d$-separation, and the vanishing minors of conditional independence, as a special case, it also seems to capture some new vanishing minor conditions that do not follow from $d$-separation. The most interesting cases of this seem to occur when $C_{A} \cap C_{B} \neq \varnothing$.

Example 2.13 (Spiders). Consider the graph in Figure 2 which we call a spider.

Clearly, we have that $(\{c\},\{c\}) t$-separates $A$ from $B$, so that the submatrix $\Sigma_{A, B}$ has rank at most 2 . Although this rank condition must be implied by CI rank constraints on $\Sigma$ and the fact that $\Sigma$ is positive definite, it does not appear to be easily derivable from these constraints.
![img-1.jpeg](img-1.jpeg)

Fig. 2.

2.2. Undirected graphs. For Gaussian undirected graphical models, the allowable covariance matrices are specified by placing restrictions on the entries of the concentration matrix. In particular, let $G$ be an undirected graph, with edge set $E$. We consider all covariance matrices $\Sigma$ such that $\left(\Sigma^{-1}\right)_{i j}=0$ for all $i-j \notin E(G)$.

As in the case of directed acyclic graphs, it is known that conditional independence constraints characterize the possible probability distributions for positive densities [7]. Indeed, in the Gaussian case, the pairwise constraints $X_{i} \Perp$ $X_{j} \mid X_{[m] \backslash\{i, j\}}$ for $i-j \notin E(G)$ characterize the distributions that belong to the model. As in the case of directed graphical models, general conditional independence constraints $X_{A} \Perp X_{B} \mid X_{C}$ are characterized by a separation criterion.

If $A, B$ and $C$ are three subsets of vertices of an undirected graph $G$, not necessarily disjoint, we say that $C$ separates $A$ and $B$ if every path from a vertex in $A$ to a vertex in $B$ contains some vertex of $C$.

THEOREM 2.14 (Conditional independence for undirected graphical models [7]). For disjoint subsets $A, B$, and $C \subseteq[m]$ the conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for the graph $G$ if and only if $C$ separates $A$ and $B$.

Since conditional independence for normal random variables corresponds to the vanishing of the minors of submatrices of the form $\Sigma_{A \cup C, B \cup C}$ it is natural to ask what conditions determine the vanishing of an arbitrary minor $\Sigma_{A, B}$. We will show that the path separation criterion also characterizes the vanishing of arbitrary minors for the undirected graphical model.

THEOREM 2.15. The submatrix $\Sigma_{A, B}$ has rank less than or equal to $r$ for all covariance matrices consistent with the graph $G$ if and only if there is a set $C \subseteq V(G)$ with $\# C \leq r$ such that $C$ separates $A$ and $B$. Consequently,

$$
\operatorname{rk}\left(\Sigma_{A, B}\right) \leq \min \{\# C: C \text { separates } A \text { and } B\}
$$

and equality holds for generic covariance matrices consistent with $G$.
Note that the sets $A, B$ and $C$ need not be disjoint in Theorem 2.15. We will provide a proof of Theorem 2.15 in Section 3.2, using the combinatorial expansions of determinants. Unlike in the case of directed acyclic graphs, we do not find any new constraints that were not trivially implied by conditional independence.
2.3. Mixed graphs. In this section, we describe our results for general classes of mixed graphs, that is, graphs that can involve directed edges $i \rightarrow j$, undirected edges $i-j$ and bidirected edges $i \leftrightarrow j$. We assume that in our mixed graphs there is a partition of the vertices of the graph $U \cup W=V(G)$, such that all undirected edges have their vertices in $U$, all bidirected edges have their vertices in $W$ and any directed edge with a vertex in $U$ and a vertex in $W$ must be of the form $u \rightarrow w$

where $u \in U$ and $w \in W$. With all of these assumptions on our mixed graph, we can order the vertices in such a way that all vertices in $U$ come before the vertices in $W$, and whenever $i \rightarrow j$ is a directed edge, we have $i<j$. We assume that the subgraph on directed edges in acyclic. Note that we allow a pair of vertices to be connected by both a directed edge $i \rightarrow j$ and a bidirected edge $i \leftrightarrow j$ or undirected edge $i-j$. With this setup, both ancestral graphs [9] and chain graphs [1] occur as special cases.

Now we introduce three matrices which are determined by the three different types of edges in the graph. We first let $\Lambda$ be the matrix with rows and columns indexed by $V(G)$ which is defined by $\Lambda_{i i}=1, \Lambda_{i j}=-\lambda_{i j}$ if $i \rightarrow j \in E(G)$ and $\Lambda_{i j}=0$ otherwise. Each $\lambda_{i j}$ is a real parameter associated to a directed edge in $G$, though they no longer necessarily have the interpretation of regression coefficients. Next, we let $K$ be a symmetric positive definite matrix, with rows and columns indexed by $U$, such that $K_{i j}=0$ if $i-j \notin E(G)$. Each entry $K_{i j}$ with $i \neq j$ is a parameter associated to an undirected edge in $G$. Finally, we let $\Phi=\left(\phi_{i j}\right)$ be a symmetric positive definite matrix, with rows and columns indexed by $W$, such that $\phi_{i j}=0$ if $i \leftrightarrow j \notin E(G)$. Each $\phi_{i j}$ with $i \neq j$ is a parameter associated to a bidirected edge in $G$.

From the three matrices $\Lambda, K$ and $\Phi$, defined as above, we obtain the following covariance matrix of our mixed graphical model:

$$
\Sigma=\Lambda^{-\top}\left(\begin{array}{cc}
K^{-1} & 0 \\
0 & \Phi
\end{array}\right) \Lambda^{-1}
$$

Note that this representation parametrizes the Gaussian ancestral graph model in the case where $G$ is an ancestral graph [9], and chain graph models under the alternative Markov property [1], when $G$ is a chain graph.

We use a path expansion in Section 3.3 to express this factorization as a power series of sums of paths, analogous to the polynomial expressions in terms of treks that appeared in the purely directed case in Section 2.1. In the precise formulation given in Section 3.3, we will need the following generalized notion of a trek.

A trek between vertices $i$ and $j$ in a mixed graph $G$ is a triple $\left(P_{L}, P_{M}, P_{R}\right)$ of paths where:

1. $P_{L}$ is a directed path of directed edges with sink $i$;
2. $P_{R}$ is a directed path of directed edges with sink $j$;
3. $P_{M}$ is either:

- a path consisting of zero or more undirected edges connecting the source of $P_{L}$ to the source of $P_{R}$, or
- a single bidirected edge connecting the source of $P_{L}$ to the source of $P_{R}$.

A trek $\left(P_{L}, P_{M}, P_{R}\right)$ is called simple if each of $P_{L}, P_{M}$ and $P_{R}$ is self-avoiding, and the only vertices which appear in more than one of the segments $P_{L}, P_{M}$, and $P_{R}$ are the sources of $P_{L}$ and $P_{R}$.

The set of all treks between $i$ and $j$ is denoted by $\mathcal{T}(i, j)$ and the set of all simple treks is $\mathcal{S}(i, j)$. Note that $\mathcal{T}(i, j)$ might be infinite because we allow the path $P_{M}$ to have cycles. On the other hand, $\mathcal{S}(i, j)$ is always finite.

Definition 2.16. A triple of sets of vertices $\left(C_{L}, C_{M}, C_{R}\right)$ t-separates $A$ from $B$ in the mixed graph $G$ if for every simple trek $\left(P_{L}, P_{M}, P_{R}\right)$ with the sink of $P_{L}$ in $A$ and the sink of $P_{R}$ in $B$, we have that $P_{L}$ contains a vertex in $C_{L}, P_{R}$ contains a vertex in $C_{R}$ or $P_{M}$ is an undirected path that contains a vertex in $C_{M}$.

Note that the mixed graph definition of $t$-separation reduces to the directed acyclic graph version of $t$-separation when $G$ is a DAG and reduces to ordinary graph separation when $G$ is an undirected graph.

THEOREM 2.17 ( $t$-separation for mixed graphs). The matrix $\Sigma_{A, B}$ has rank at most $r$ for all covariance matrices consistent with the mixed graph $G$ if and only if there exist three subsets $C_{L}, C_{M}, C_{R}$ with $\# C_{L}+\# C_{M}+\# C_{R} \leq r$ such that $\left(C_{L}, C_{M}, C_{R}\right) t$-separates $A$ from $B$. Consequently,

$$
\operatorname{rk}\left(\Sigma_{A, B}\right) \leq \min \left\{\# C_{L}+\# C_{M}+\# C_{R}:\left(C_{L}, C_{M}, C_{R}\right) t \text {-separates } A \text { from } B\right\}
$$

and equality holds for generic covariance matrices consistent with $G$.

Since conditional independence statements for Gaussian graphical models correspond to special low rank submatrices of the covariance matrix, Theorem 2.17 also gives a characterization of when conditional independence statements for these mixed graph models hold.

Corollary 2.18. The conditional independence statement $X_{A} \Perp X_{B} \mid X_{C}$ holds for the Gaussian graphical model associated to the mixed graph $G$, if and only if there is a partition $C=C_{L} \cup C_{M} \cup C_{R}$ such that $\left(C_{L}, C_{M}, C_{R}\right) t$-separates $A \cup C$ from $B \cup C$.

Proof. The conditional independence statement holds if and only if $\Sigma_{A \cup C, B \cup C}$ has rank $\# C$. By Theorem 2.17 this happens if and only there exists $\left(D_{L}, D_{M}, D_{R}\right)$ with $\# D_{L}+\# D_{M}+\# D_{R} \leq \# C$ that $t$-separate $A \cup C$ and $B \cup C$. But since $C \subseteq D_{L} \cup D_{M} \cup D_{R}$, this occurs if and only if $C=D_{L} \cup D_{M} \cup D_{R}$ is a partition of $C$.

It is worth noting, however, that unlike in the case of directed acyclic graphs and undirected graphs, conditional independence statements and vanishing minors are not enough to characterize the covariance matrices that come from the model. See the example in Section 8.3.1 of [9].

3. Proofs. In this section, we consider the elements $\lambda_{i j}, \phi_{i j}$ and $k_{i j}$ as polynomial variables or indeterminates. When we speak about $\operatorname{det} \Sigma_{A, B}$ we mean to speak of this polynomial as an algebraic object without reference to its evaluation at specific values of $\lambda_{i j}, \phi_{i j}$ and $k_{i j}$. Thus the statement that $\operatorname{det} \Sigma_{A, B}$ is identically equal to zero means that the determinant is equal to the zero polynomial or power series.
3.1. Proof of Theorem 2.8 (directed graphs). Let $G$ be a directed acyclic graph with vertex set $V(G)=[m]$. We assign to each edge $i \rightarrow j$ in $G$ the parameter $\lambda_{i j}$. Let $L$ be the $m \times m$ matrix given by $L_{i j}=\lambda_{i j}$ if $i \rightarrow j$ is an edge in $G$ and $L_{i j}=0$ otherwise. Set $\Lambda=I-L$, where $I$ is the $m \times m$ identity matrix. We assign to each vertex $i \in[m]$ the parameter $\phi_{i}$, and let $\Phi$ be the diagonal matrix $\Phi=\operatorname{diag}\left(\phi_{1}, \ldots, \phi_{m}\right)$.

The entries of the matrix $\Lambda^{-1}$ have a well-known combinatorial interpretation in terms of the directed acyclic graph $G$.

Proposition 3.1. For each path $P$ in the directed acyclic graph $G$, set $\lambda^{P}=$ $\prod_{k \rightarrow l \in P} \lambda_{k l}$. Then

$$
\left(\Lambda^{-1}\right)_{i j}=\sum_{P \in \mathcal{P}(i, j)} \lambda^{P}
$$

where $\mathcal{P}(i, j)$ is the set of all directed paths from $i$ to $j$.
Lemma 3.2. Suppose that $A, B \subseteq[m]$ with $\# A=\# B$. Then $\operatorname{det} \Sigma_{A, B}$ is identically zero if and only if for every set $S \subset[m]$ with $\# S=\# A=\# B$, either $\operatorname{det}\left(\Lambda^{-1}\right)_{S, A}=0$ or $\operatorname{det}\left(\Lambda^{-1}\right)_{S, B}=0$.

Proof. Since $\Sigma=\Lambda^{-\top} \Phi \Lambda^{-1}$, we have $\Sigma_{A, B}=\left(\Lambda^{-\top}\right)_{A,[m]} \Phi\left(\Lambda^{-1}\right)_{[m], B}$. We can calculate $\operatorname{det} \Sigma_{A, B}$ by applying the Cauchy-Binet determinant expansion formula twice on this product. In particular, we obtain

$$
\operatorname{det} \Sigma_{A, B}=\sum_{R, S \subseteq[m]} \operatorname{det}\left(\Lambda^{-\top}\right)_{A, R} \operatorname{det} \Phi_{R, S} \operatorname{det}\left(\Lambda^{-1}\right)_{S, B}
$$

where the sum runs over subsets $R$ and $S$ of cardinality $\# A=\# B$. Since $\Phi$ is a diagonal matrix, $\operatorname{det} \Phi_{R, S}=0$ unless $R=S$, in which case we let $\phi_{S}$ denote $\operatorname{det} \Phi_{S, S}=\prod_{s \in S} \phi_{s}$.

Thus we have the following expansion of $\operatorname{det} \Sigma_{A, B}$ :

$$
\begin{aligned}
\operatorname{det} \Sigma_{A, B} & =\sum_{S \subseteq[m]} \operatorname{det}\left(\Lambda^{-\top}\right)_{A, S} \operatorname{det}\left(\Lambda^{-1}\right)_{S, B} \phi_{S} \\
& =\sum_{S \subseteq[m]} \operatorname{det}\left(\Lambda^{-1}\right)_{S, A} \operatorname{det}\left(\Lambda^{-1}\right)_{S, B} \phi_{S}
\end{aligned}
$$

Since each monomial $\phi_{S}$ appears in only one term in this expansion, the result follows.

To prove the main theorem, we need two classical results from combinatorics. The first is Lemma 3.3, the Gessel-Viennot-Linström lemma, which gives a combinatorial expression for expansions of subdeterminants of the matrix $\Lambda^{-1}$. The second is Theorem 3.6, Menger's theorem, which describes a relationship between nonintersecting path families and blocking sets in a graph.

LEMMA 3.3 (Gessel-Viennot-Lindström lemma [6, 8]). Suppose $G$ is a directed acyclic graph with vertex set $[m]$. Let $R$ and $S$ be subsets of $[m]$ with $\# R=\# S=\ell$. Then

$$
\operatorname{det}\left(\Lambda^{-1}\right)_{R, S}=\sum_{\mathbf{P} \in N(R, S)}(-1)^{\mathbf{P}} \lambda^{\mathbf{P}}
$$

where $N(R, S)$ is the set of all collections of nonintersecting systems of $\ell$ directed paths in $G$ from $R$ to $S$, and $(-1)^{\mathbf{P}}$ is the sign of the induced permutation of elements from $R$ to $S$. In particular, $\operatorname{det}\left(\Lambda^{-1}\right)_{R, S}=0$ if and only if every system of $\ell$ directed paths from $R$ to $S$ has two paths which share a vertex.

Consider a system $\mathbf{T}=\left\{T_{1}, \ldots, T_{\ell}\right\}$ of $\ell$ treks from $A$ to $B$, connecting $\ell$ distinct vertices $a_{i} \in A$ to $\ell$ distinct vertices $b_{j} \in B$. Let $\operatorname{top}(\mathbf{T})$ denote the multiset $\left\{\operatorname{top}\left(T_{1}\right), \ldots, \operatorname{top}\left(T_{\ell}\right)\right\}$. Note that $\mathbf{T}$ consists of two systems of directed paths, a path system $\mathbf{P}_{A}$ from $\operatorname{top}(\mathbf{T})$ to $A$ and a path system $\mathbf{P}_{B}$ from $\operatorname{top}(\mathbf{T})$ to $B$. We say that $\mathbf{T}$ has a sided intersection if two paths in $\mathbf{P}_{A}$ share a vertex or if two paths in $\mathbf{P}_{B}$ share a vertex.

Proposition 3.4. Let $A$ and $B$ be subsets of $[m]$ with $\# A=\# B$. Then

$$
\operatorname{det} \Sigma_{A, B}=0
$$

if and only if every system of (simple) treks from $A$ to $B$ has a sided intersection.
Proof. Suppose that $\operatorname{det} \Sigma_{A, B}=0$, and let $\mathbf{T}$ be a trek system from $A$ to $B$. If all elements of the multiset $\operatorname{top}(\mathbf{T})$ are distinct, then Lemma 3.2 implies that either $\operatorname{det}\left(\Lambda^{-1}\right)_{\operatorname{top}(\mathbf{T}), A}=0$ or $\operatorname{det}\left(\Lambda^{-1}\right)_{\operatorname{top}(\mathbf{T}), B}=0$. If $\operatorname{top}(\mathbf{T})$ has repeated elements, then these determinants are zero, since there are repeated rows. Then Lemma 3.3 implies that there is an intersection in the path system from $\operatorname{top}(\mathbf{T})$ to $A$ or in the path system from $\operatorname{top}(\mathbf{T})$ to $B$ which means that $\mathbf{T}$ has a sided intersection.

Conversely, suppose that every trek system $\mathbf{T}$ from $A$ to $B$ has a sided intersection, and let $R \subseteq[m]$ with $\# R=\# A=\# B$. If $R=\operatorname{top}(\mathbf{T})$ for some trek system $\mathbf{T}$ from $A$ to $B$, then either the path system from $\operatorname{top}(\mathbf{T})$ to $A$ or the path system from $\operatorname{top}(\mathbf{T})$ to $B$ has an intersection. If $R$ is not the set of top elements for some trek system $\mathbf{T}$, then there is no path system connecting $R$ to $A$ or there is no path system

connecting $R$ to $B$. In both cases, Lemma 3.3 implies that either $\operatorname{det}\left(\Lambda^{-1}\right)_{R, A}=0$ or $\operatorname{det}\left(\Lambda^{-1}\right)_{R, B}=0$. Lemma 3.2 then implies that $\operatorname{det} \Sigma_{A, B}=0$.

We note that it is sufficient to check the systems of simple treks. Given a trek $T$ from $i$ to $j$, let $\mathrm{LE}(T)$ denote the unique simple trek from $i$ to $j$ whose edge set is a subset of the edge set of $T$. Now if each simple trek system $\mathbf{T}$ has a sided intersection, then every trek system does, namely the intersection coming from $\operatorname{LE}(\mathbf{T})$.

We define a new DAG associated to $G$, denoted $\bar{G}$, which has $2 m$ vertices $\{1,2, \ldots, m\} \cup\left\{1^{\prime}, 2^{\prime}, \ldots, m^{\prime}\right\}$ and edges $i \rightarrow j$ if $i \rightarrow j$ is an edge in $G, j^{\prime} \rightarrow i^{\prime}$ if $i \rightarrow j$ is an edge in $G$ and $i^{\prime} \rightarrow i$ for each $i \in[m]$.

Proposition 3.5. Treks in $G$ from $i$ to $j$ are in bijective correspondence with directed paths from $i^{\prime}$ to $j$ in $\bar{G}$. Simple treks in $G$ from $i$ to $j$ are in bijective correspondence with directed paths from $i^{\prime}$ to $j$ in $\bar{G}$ that use at most one edge from any pair $a \rightarrow b$ and $b^{\prime} \rightarrow c^{\prime}$ where $a, b, c \in[m]$.

Proof. Every trek is the union of two paths with a common top. The part of the trek from the top to $i$ corresponds to the subpath with only vertices in $\left\{1^{\prime}, \ldots, m^{\prime}\right\}$, and the part of the trek from the top to $j$ corresponds to the subpath with only vertices in $\{1, \ldots, m\}$. The unique edge of the form $k^{\prime} \rightarrow k$ corresponds to the top of the trek. Excluding pairs $a \rightarrow b$ and $b^{\prime} \rightarrow c^{\prime}$ implies that a trek never visits the same vertex $b$ twice.

Menger's theorem (or, more generally, the Max-Flow-Min-Cut theorem) now allows us to turn our sided crossing result on $G$ into a blocking characterization on $\bar{G}$.

THEOREM 3.6 (Vertex version of Menger's theorem). The cardinality of the largest set of vertex disjoint directed paths between two nonadjacent vertices $u$ and $v$ in a directed graph is equal to the cardinality of the smallest blocking set where a blocking set is a set of vertices whose removal from the graph ensures that there is no directed path from $u$ from $v$.

Proof OF THEOREM 2.8. We first focus on the case where $\operatorname{det} \Sigma_{A, B}=0$ so that the rank is at most $k-1$ where $k=\# A=\# B$. According to Proposition 3.4, every system of $k$ treks from $A$ to $B$ must have a sided intersection. That is, the number of vertex disjoint paths from $A^{\prime}$ to $B$ is at most $k-1$ in the graph $\bar{G}$. We add two new vertices to $\bar{G}$, one vertex $u$ that points to each vertex in $A^{\prime}$ and one vertex $v$ such that each vertex in $B$ points to $v$. Thus there are at most $k-1$ vertex disjoint paths from $u$ to $v$. Applying Menger's theorem, there is a blocking set $W$ in $\bar{G}$ of cardinality $k-1$ or less. Set $C_{A}=\{i \in[m]: i^{\prime} \in W\}$ and $C_{B}=\{i \in$

$[m]: i \in W\}$. Then it is clear that $\# C_{A}+\# C_{B} \leq k-1$, and these two sets $t$-separate $A$ from $B$.

Conversely, suppose there exist sets $C_{A}$ and $C_{B}$ with $\# C_{A}+\# C_{B} \leq k-1$ which $t$-separate $A$ from $B$. Then $W=\left\{i: i \in C_{B}\right\} \cup\left\{i^{\prime}: i \in C_{A}\right\}$ is a blocking set between $u$ and $v$ as above. Applying Menger's theorem, since $\# W \leq k-1$, there is no vertex disjoint system of $k$ paths from $A^{\prime}$ to $B$. Thus every trek system from $A$ to $B$ will have a sided intersection, so that $\operatorname{det} \Sigma_{A, B}=0$ by Proposition 3.4.

From the special case of determinants, we deduce the general result, because if the smallest blocking set has size $r$, there exists a collection of $r$ disjoint paths between any subset of $A$ and any subset of $B$, and this is the largest possible number of paths in such a collection. This means that all $(r+1) \times(r+1)$ minors of $\Sigma_{A, B}$ are zero, but at least one $r \times r$ minor is not zero. Hence $\Sigma_{A, B}$ has rank $r$ for generic choices of the $\lambda$ and $\phi$ parameters.
3.2. Proof of Theorem 2.15 (undirected graphs). To prove Theorem 2.15, we will introduce Lemma 3.7, a limited analogue of the Gessel-Viennot-Lindström lemma for graphs which are not necessarily acyclic. This version is a direct corollary of Theorem 6.1 in [5] which, for the sake of simplicity, we do not state in full generality.

Let $G$ be a directed graph, not necessarily acyclic. Let $W$ be the matrix given by $W_{i j}=w_{i j}$ if $i \rightarrow j$ is an edge in $G$ and $W_{i j}=0$ otherwise. By standard notions in algebraic graph theory, we can expand the matrix $(I-W)^{-1}$ as a formal power series in terms of the $w_{i j}$. In particular,

$$
(I-W)_{i j}^{-1}=\sum_{P \in \mathcal{P}(i, j)} w^{P}
$$

where $\mathcal{P}(i, j)$ is the set of all (possibly infinitely many) paths from $i$ to $j$ in $G$. This is just Proposition 3.1 in the general case.

Let $A=\left\{a_{1}, \ldots, a_{\ell}\right\}$ and $B=\left\{b_{1}, \ldots, b_{\ell}\right\}$ be subsets of $[m]$ with the same cardinality. The determinant $\operatorname{det}\left((I-W)^{-1}\right)_{A, B}$ can be written simply in an expression that involves cancelation as

$$
\operatorname{det}\left((I-W)^{-1}\right)_{A, B}=\sum_{\tau \in S_{\ell}, P_{i} \in \mathcal{P}\left(a_{i}, b_{\tau(i)}\right)} \operatorname{sign}(\tau) \prod_{i=1}^{\ell} w^{P_{i}}
$$

Deciding whether this formula is nonzero amounts to showing whether or not all terms cancel in this formula. This leads to the following version of the Gessel-Viennot-Lindström lemma [5].

Lemma 3.7. Let $G$ be a directed graph. Let $A=\left\{a_{1}, \ldots, a_{\ell}\right\}$ and $B=$ $\left\{b_{1}, \ldots, b_{\ell}\right\}$ be subsets of $[m]$ with the same cardinality. Then $\left(\operatorname{det}(I-W)^{-1}\right)_{A, B}$ is identically zero if and only if every system of $\ell$ directed paths from $A$ to $B$ has two paths which share a vertex. Further, if there is a set of $\ell$ paths

$P_{1}, \ldots, P_{\ell}$ from $A$ to $B$ which do not have a common vertex, then $w^{P_{1}} \cdots w^{P_{\ell}}$ appears as a monomial with a nonzero coefficient in the power series expansion of $\operatorname{det}\left((I-W)^{-1}\right)_{A, B}$.

For an undirected graph $G$, we associate to each edge $i-j$ in $G$ a parameter $\psi_{i j}$. Then let $\Psi_{i j}=\psi_{i j}$ if $i-j$ is an edge in $G$ and $\Psi_{i j}=0$ otherwise. Let $\widehat{G}$ be the directed graph formed by replacing each undirected edge in $G$ with two directed edges of weight $\psi_{i j}$, one in each direction.

Corollary 3.8. For this symmetric matrix $\Psi$, the determinant $\operatorname{det}((I-$ $\Psi)^{-1}{ }_{A, B}$ is identically zero if and only if every system of $\ell=\# A=\# B$ directed paths from $A$ to $B$ in $\widehat{G}$ has two paths which share a vertex.

Proof. Lemma 3.7 immediately implies that if every system of directed paths in $\widehat{G}$ has a crossing, then $\operatorname{det}\left((I-\Psi)^{-1}\right)_{A, B}$ is identically zero, by specialization.

To show the converse, we need to verify that, for a fixed $A$ and $B$, each system $\mathbf{P}$ consisting of self-avoiding paths, no two of which intersect, is the unique system of its weight $\psi^{\mathbf{P}}$. While $\widehat{G}$ may have multiple path systems of the same weight $\psi^{\mathbf{P}}$, they must all consist of the same undirected edges in $G$, and any such system in $\widehat{G}$ can be obtained from any other by switching the directions of some of the paths. Then, since no two of the paths intersect, we see that there is only one such system with the correct orientation of paths, since $A$ and $B$ are fixed.

Proof of Theorem 2.15. We write $\Sigma=K^{-1}=D^{-1}(I-\Psi)^{-1} D^{-1}$ where $D$ is the diagonal matrix of standard deviations, $D=\operatorname{diag}\left(\sqrt{\sigma_{11}}, \ldots, \sqrt{\sigma_{m m}}\right)$. We can treat the entries $\Psi_{i j}=k_{i j} \cdot \sqrt{\sigma_{i i} \sigma_{j j}}$ as free parameters. It suffices to prove a vanishing determinant condition locally near a single point in the parametrization, so we assume that $\Psi$ is small so that we can use the power series expansion, $(I-\Psi)^{-1}=I+\Psi+\Psi^{2}+\Psi^{3}+\cdots$. Applying Cauchy-Binet as before, we obtain

$$
\begin{aligned}
\operatorname{det} \Sigma_{A, B} & =\sum_{R, S \subseteq[m]} \operatorname{det}\left(D^{-1}\right)_{A, R} \operatorname{det}\left((I-\Psi)^{-1}\right)_{R, S} \operatorname{det}\left(D^{-1}\right)_{S, B} \\
& =\operatorname{det}\left(D^{-1}\right)_{A, A} \operatorname{det}\left((I-\Psi)^{-1}\right)_{A, B} \operatorname{det}\left(D^{-1}\right)_{B, B}
\end{aligned}
$$

since $\operatorname{det}\left(D^{-1}\right)_{A, R}=0$ if $A \neq R$ and $\operatorname{det}\left(D^{-1}\right)_{S, B}=0$ if $B \neq S$. Now, $\operatorname{det}\left(D^{-1}\right)_{A, A} \neq 0$ and $\operatorname{det}\left(D^{-1}\right)_{B, B} \neq 0$, and Corollary 3.8 completes the proof.
3.3. Proof of Theorem 2.17 (mixed graphs). Recall that covariance matrices consistent with a mixed graph $G$ all have the form

$$
\Sigma=\Lambda^{-\top}\left(\begin{array}{cc}
K^{-1} & 0 \\
0 & \Phi
\end{array}\right) \Lambda^{-1}
$$

Our first step is a standard argument in the graphical models literature, which allows us to reduce to the case where there are no bidirected edges in the graph. This can be achieved by subdividing the bidirected edges; that is, for each bidirected edge $i \leftrightarrow j$ in the graph, where $i \leq j$, we replace $i \leftrightarrow j$ with a vertex $v_{i, j}$, directed edges $v_{i, j} \rightarrow i$ and $v_{i, j} \rightarrow j$. The graph $\widetilde{G}$ obtained from $G$ by subdividing all of its bidirected edges is called the bidirected subdivision of $G$. If $G$ has only directed and bidirected edges, then $\widetilde{G}$ is called the canonical DAG associated to $G$.

Proposition 3.9. Let $A, B \subset V(G)$ be two sets of vertices such that $\# A=$ $\# B$.

1. The generic rank of $\Sigma_{A, B}$ is the same for matrices compatible with $G$ or $\widetilde{G}$.
2. There exists a triple $\left(C_{L}, C_{M}, C_{R}\right)$ with $\# C_{L}+\# C_{M}+\# C_{R}=r$ that $t$-separates $A$ from $B$ in $G$ if and only if there is a triple $\left(D_{L}, D_{M}, D_{R}\right)$ with $\# D_{L}+\# D_{M}+$ $\# D_{R}=r$ that $t$-separates $A$ from $B$ in $\widetilde{G}$.

Proof. (1) It suffices to prove that the two parametrizations have the same Zariski closure (see [2] for the definition and background). This will follow by showing that near the identity matrix, the two parameterizations give the same family of matrices. Locally near the identity matrix, the matrix expansion for $\Sigma$ can be expanded as a formal power series in the entries of $K, \Phi$ and $\Lambda$. The expansion for $\sigma_{i j}$ can be expressed as a sum over all treks $\mathcal{T}(i, j)$ between $i$ and $j$ in $G$. This follows by using the matrix expansions for paths in $\Lambda^{-1}$ and $K^{-1}$ as we have used in Sections 3.1 and 3.2.

Similarly, the expansion for $\widetilde{\sigma}_{i j}$ is the sum over all treks in $\widetilde{G}$. Now set

$$
\phi_{i j}=\widetilde{\phi}_{v_{i, j}, v_{i, j}} \widetilde{\lambda}_{v_{i, j}, i} \widetilde{\lambda}_{v_{i, j}, j} \quad \text { and } \quad \phi_{i i}=\widetilde{\phi}_{i i}+\sum_{j \leftrightarrow i} \widetilde{\phi}_{v_{i, j}, v_{i, j}} \widetilde{\lambda}_{v_{i, j}, i}^{2}
$$

This transformation shows that these two parametrizations have the same Zariski closure, since they yield the same formula via sums over the treks in $G$ and $\widetilde{G}$, respectively. The point is that since we assume that we are close to the identity matrix, it is also possible to go back and forth between $G$ and $\widetilde{G}$ parameters. In particular, since we are close to the identity matrix, $\phi_{i j}$ is small. So we can choose $\widetilde{\phi}_{v_{i, j}, v_{i, j}}=\varepsilon>0$ and set $\widetilde{\lambda}_{v_{i, j}, i}=\sqrt{\left|\phi_{i j}\right| \varepsilon}$ and $\widetilde{\lambda}_{v_{i, j}, j}=\operatorname{sign}\left(\phi_{i j}\right) \sqrt{\left|\phi_{i j}\right| \varepsilon}$. The small size of the $\phi_{i j}$ guarantee that we can find a positive $\phi_{i i}$ satisfying the second equation. The smallness of $\varepsilon$ guarantees that $\Phi$ is positive definite.
(2) Any $t$-separating set in $G$ is clearly a $t$-separating set in $\widetilde{G}$. Suppose that $\left(D_{L}, D_{M}, D_{R}\right)$ is a minimal $t$-separating set in $\widetilde{G}$; that is, if any vertex is deleted from $\left(D_{L}, D_{M}, D_{R}\right)$ we no longer have a $t$-separating set. It is easy to see that $D_{M}$ will not contain any vertices $v_{i, j}$ in a minimal $t$-separating set of $\widetilde{G}$, so that $D_{M} \subset V(G)$. It clearly suffices to show that each minimal $t$-separating set in $\widetilde{G}$ is

a $t$-separating set in $G$. We define

$$
\begin{aligned}
C_{L} & =\left(D_{L} \cap V(G)\right) \cup\left\{i: v_{i, j} \in D_{L}\right\} \\
C_{M} & =D_{M} \\
C_{R} & =\left(D_{R} \cap V(G)\right) \cup\left\{j: v_{i, j} \in D_{R}\right\}
\end{aligned}
$$

If our $t$-separating set in $\widetilde{G}$ contains none of the vertices $v_{i, j}$, then it is clearly a $t$-separating set in $G$; otherwise, the way that $i$ and $j$ are chosen in $\left\{i: v_{i, j} \in D_{L}\right\}$ and $\left\{j: v_{i, j} \in D_{R}\right\}$ is important. Given a vertex $v_{i, j}$ in the $t$-separating set, let $\mathcal{T}\left(v_{i, j}\right)$ denote the set of treks $T=\left(T_{L}, T_{M}, T_{R}\right)$ from $A$ to $B$ such that $T_{L} \cap D_{L}=$ $\left\{v_{i, j}\right\}$ or $T_{R} \cap D_{R}=\left\{v_{i, j}\right\}$. Since $\left(D_{L}, D_{M}, D_{R}\right)$ is minimal, we see that $\mathcal{T}\left(v_{i, j}\right)$ must be nonempty. This implies that in every trek $T=\left(T_{L}, T_{M}, T_{R}\right) \in \mathcal{T}\left(v_{i, j}\right)$, up to relabeling, $i$ occurs in $T_{L}$, whose sink lies in $A$, and $j$ occurs in $T_{R}$, whose sink lies in $B$. For if there were a trek from $A$ to $B$ in $\mathcal{T}\left(v_{i, j}\right)$ that had $j$ in $T_{L}$ or $i$ in $T_{R}$, we could patch two halves of these treks together to find a trek from $A$ to $B$ that did not have a sided intersection with $\left(D_{L}, D_{M}, D_{R}\right)$. If $i$ lies in $T_{L}$ and $j$ lies in $T_{R}$ in such treks, then we add $i$ to $C_{L}$ when $v_{i, j} \in D_{L}$, and we add $j$ to $C_{R}$ when $v_{i, j} \in D_{R}$. Then the triple $\left(C_{L}, C_{M}, C_{R}\right)$ has $\# C_{L}+\# C_{M}+\# C_{R} \leq$ $\# D_{L}+\# D_{M}+\# D_{R}$ and also $t$-separates $A$ from $B$.

REMARK. The parameterization using the bidirected subdivision $\widetilde{G}$ typically yields a smaller set of covariance matrices than the original graph $G$. However, these sets have the same dimension and the same Zariski closure.

Before getting to the general case of mixed graphs, we first need to handle the special case of mixed graphs that do not have undirected edges.

Lemma 3.10. Suppose that $G$ is a mixed graph without undirected edges. The matrix $\Sigma_{A, B}$ has rank at most $r$ for all covariance matrices consistent with the mixed graph $G$ if and only if there exist subsets $C_{L}, C_{R} \subset V(G)$ with $\# C_{L}+\# C_{R} \leq$ $r$ such that $\left(C_{L}, \varnothing, C_{R}\right)$ t-separates $A$ from $B$.

Proof. Due to Proposition 3.9, this immediately reduces to the case of directed acyclic graphs, so that we may apply Theorem 2.8.

Now that we have removed the bidirected edges, we assume that our matrix factorization has the following form:

$$
\Sigma=\Lambda^{-\top} K^{-1} \Lambda^{-1}
$$

and we prepare to apply the Cauchy-Binet determinant expansion formula. That is, for two subsets $A, B \subseteq[m]$, with $\# A=\# B$, we have

$$
\operatorname{det} \Sigma_{A, B}=\sum_{S \subseteq[m]} \sum_{T \subseteq[n]} \operatorname{det}\left(\Lambda^{-\top}\right)_{A, S} \cdot \operatorname{det}\left(K^{-1}\right)_{S, T} \cdot \operatorname{det}\left(\Lambda^{-1}\right)_{T, B}
$$

where the sums range over the sets $S, T \subset[m]$ with $\# S=\# T=\# A=\# B$.
We say that a set of treks $\left\{\left(P_{L_{i}}, P_{M_{i}}, P_{R_{i}}\right): i \in[\ell]\right\}$ has a sided-crossing if there are indices $i_{1} \neq i_{2} \in[\ell]$ such that either $P_{L_{i_{1}}}$ and $P_{L_{i_{2}}}$ share a vertex, $P_{M_{i_{1}}}$ and $P_{M_{i_{2}}}$ share a vertex or $P_{R_{i_{1}}}$ and $P_{R_{i_{2}}}$ share a vertex.

LEMMA 3.11. Let $\# A=\# B=r$. Suppose that every system of $r$ treks from $A$ to $B$ in a mixed graph $G$ (consisting of directed and undirected edges) has a sided crossing. Then for every $S, T \subset V(G)$ with $\# S=\# T=r$, we have $\operatorname{det}\left(\Lambda^{-\top}\right)_{A, S}$. $\operatorname{det}\left(K^{-1}\right)_{S, T} \cdot \operatorname{det}\left(\Lambda^{-1}\right)_{T, B}=0$.

Proof. Consider the trek systems from $A$ to $B$ that consist of a directed path system $\mathbf{P}_{L}$ from $S$ to $A$, an undirected path system $\mathbf{P}_{M}$ from $S$ to $T$ and a directed path system $\mathbf{P}_{R}$ from $T$ to $B$. We call such a system of treks an $(S, T)$-trek system from $A$ to $B$.

We claim that if every trek system from $A$ to $B$ has a sided crossing, then either all $(S, T)$-trek systems have a crossing in $\mathbf{P}_{L}$, all $(S, T)$-trek systems have a crossing in $\mathbf{P}_{M}$ or all $(S, T)$-trek systems have a crossing in $\mathbf{P}_{R}$. Suppose this is not the case; then there is a directed path system from $S$ to $A$ with no crossing, an undirected path system from $S$ to $T$ with no crossing and a directed path system from $T$ to $B$ with no crossing, yielding an $(S, T)$-trek system from $A$ to $B$ with no sided crossing.

Applying the claim, along with the directed and undirected versions of the Gessel-Viennot-Lindström lemma (Lemma 3.3 and Corollary 3.8), we deduce that one of $\operatorname{det}\left(\Lambda^{-\top}\right)_{A, S}, \operatorname{det}\left(K^{-1}\right)_{S, T}$, or $\operatorname{det}\left(\Lambda^{-1}\right)_{T, B}$ is identically zero. This implies that their product is zero.

Lemma 3.11 is enough to handle one direction of Theorem 2.17. For the other direction, we need slightly more machinery. Using our presentation for undirected graphs, we can write

$$
K^{-1}=D^{-1}(I-W)^{-1} D^{-1}
$$

where $D$ is the diagonal matrix of standard deviations, and $W_{i j}=w_{i j}=w_{j i}$ if $i-j \in E(G)$, and $W_{i j}=0$ otherwise. Thus,

$$
\Sigma=\Lambda^{-\top} D^{-1}(I-W)^{-1} D^{-1} \Lambda^{-1}
$$

Using the standard argument of algebraic graph theory, we can expand this near the identity matrix as a power series,

$$
\sigma_{i j}=\sum_{\left(P_{L}, P_{M}, P_{R}\right) \in \mathcal{T}(i, j)} \lambda^{P_{L}} d_{s\left(P_{L}\right)}^{-1} w^{P_{M}} d_{s\left(P_{R}\right)}^{-1} \lambda^{P_{R}}
$$

where $s(P)$ denotes the source of the directed path $P$. Thus if $A=\left\{a_{1}, \ldots, a_{\ell}\right\}$ and $B=\left\{b_{1}, \ldots, b_{\ell}\right\}$,

$$
\begin{aligned}
\operatorname{det} \Sigma_{A, B}= & \sum_{\tau \in S_{\ell},\left(P_{L_{i}}, P_{M_{i}}, P_{R_{i}}\right) \in \mathcal{T}\left(a_{i}, b_{\tau(i)}\right)} \operatorname{sign}(\tau) \\
& \times \prod_{i=1}^{\ell} \lambda^{P_{L_{i}}} d_{s\left(P_{L_{i}}\right)}^{-1} w^{P_{M_{i}}} d_{s\left(P_{R_{i}}\right)}^{-1} \lambda^{P_{R_{i}}}
\end{aligned}
$$

LEMMA 3.12. Suppose that there exists a system of treks from $A=\left\{a_{1}, \ldots\right.$, $\left.a_{\ell}\right\}$ to $B=\left\{b_{1}, \ldots, b_{\ell}\right\}$ without sided crossing. Then $\operatorname{det} \Sigma_{A, B}$ is not zero.

Proof. If such a system of treks exists, then there also exists a $\tau \in S_{\ell}$ and a system of simple treks $T_{i}=\left(P_{L_{i}}, P_{M_{i}}, P_{R_{i}}\right) \in \mathcal{S}\left(a_{i}, b_{\tau(i)}\right), i=1, \ldots, \ell$ without sided intersection. Let $G^{\prime}$ be the graph obtained from $G$ by deleting all edges that do not appear in any of the $T_{i}$. The determinant of the matrix obtained from $\Sigma_{A, B}$ by setting all parameters corresponding to edges outside $G^{\prime}$ equal to zero is exactly the determinant of the corresponding matrix $\Sigma_{A, B}^{\prime}$ for $G^{\prime}$; it suffices to show that this latter determinant is nonzero.

To do this, we construct a third graph $G^{\prime \prime}$ from $G^{\prime}$ by introducing, for each $i$ for which $P_{M_{i}}$ is not empty, a bidirected edge $s\left(P_{L_{i}}\right) \leftrightarrow s\left(P_{R_{i}}\right)$ with label $\phi_{s\left(P_{L_{i}}\right), s\left(P_{M_{i}}\right)}$ and deleting all undirected edges. By Lemma 3.10 we have $\operatorname{det} \Sigma_{A, B}^{\prime \prime} \neq 0$. But then this determinant remains nonzero after specialising the parameters $\phi_{s\left(P_{L_{i}}\right), s\left(P_{M_{i}}\right)}$ to the monomials $d_{s\left(P_{L_{i}}\right)}^{-1} w^{P_{M_{i}}} d_{s\left(P_{R_{i}}\right)}^{-1}$; here we use that, as the $P_{M_{i}}$ are disjoint, these $\ell$ monomials contain disjoint sets of variables. The resulting nonzero expression is the subsum of the $G^{\prime}$-analogue of (5) over all terms for which the $W$-part of the monomial equals $\prod_{i=1}^{\ell}\left(w^{P_{M_{i}}}\right)^{\varepsilon_{i}}$ for some exponents $\varepsilon_{1}, \ldots, \varepsilon_{\ell} \in\{0,1\}$. Indeed, if a system of treks $\left(T_{i}^{\prime}=\left(P_{L_{i}}^{\prime}, P_{M_{i}}^{\prime}, P_{R_{i}}^{\prime}\right)\right)_{i}$ from $A$ to $B$ in $G^{\prime}$ has $\prod_{i=1}^{\ell}\left(w^{P_{M_{i}}}\right)^{\varepsilon_{i}}$ as the $W$-part of its monomial, then since the $P_{M_{i}}$ are self-avoiding and mutually disjoint, the nonempty middle parts $P_{M_{i}}^{\prime}$ form the subset of the nonempty $P_{M_{i}}$ for which $\varepsilon_{i}$ equals 1 (potentially up to traversing some of these paths in the opposite direction). Hence the trek monomial of $\left(T_{1}^{\prime}, \ldots, T_{\ell}^{\prime}\right)$ comes, under the specialization above, from the monomial of a unique trek in $G^{\prime \prime}$ of the same sign. This proves that $\operatorname{det} \Sigma_{A, B}^{\prime}$ is nonzero, whence the lemma follows.

Proof of ThEOREM 2.17. By Proposition 3.9 we can assume that there are no bidirected edges in $G$. It suffices to handle the case where $\# A=\# B=r+1$. Lemmas 3.11 and 3.12 imply that $\operatorname{det} \Sigma_{A, B}=0$ if and only if every system of $\ell$ treks from $A$ to $B$ has a sided intersection. We wish to apply Menger's theorem. To do this, we introduce a new graph $\widetilde{G}$ with $3 m$ vertices, namely $\{1, \ldots, m\} \cup$ $\left\{1^{\prime}, \ldots, m^{\prime}\right\} \cup\left\{1^{\prime \prime}, \ldots, m^{\prime \prime}\right\}$. This is analogous to our previous definitions of $\widetilde{G}$, but

accounts for both directed and undirected edges. The edge set of $\widetilde{G}$ consists of precisely those edges,

- $i \rightarrow j$ and $j^{\prime} \rightarrow i^{\prime}$, where $i \rightarrow j$ is a directed edge of $G$,
- $i^{\prime \prime} \rightarrow j^{\prime \prime}$ and $j^{\prime \prime} \rightarrow i^{\prime \prime}$, where $i-j$ is an undirected edge of $G$ and
- $i^{\prime} \rightarrow i^{\prime \prime}$ and $i^{\prime \prime} \rightarrow i$, where $i \in[m]$ is a vertex of $G$.

Treks between $i$ and $j$ in $G$ are in bijective correspondence with directed paths between $i^{\prime}$ and $j$ in $\widetilde{G}$. Thus, the vertex version of Menger's theorem implies that there must exist $C_{L}^{\prime} \subseteq\left\{1^{\prime}, \ldots, m^{\prime}\right\}, C_{M}^{\prime \prime} \subseteq\left\{1^{\prime \prime}, \ldots, m^{\prime \prime}\right\}$ and $C_{R} \subseteq\{1, \ldots, m\}$ such that every path from $A^{\prime}$ to $B$ in $G^{\prime \prime}$ intersects one of these sets, and such that $\# C_{L}^{\prime}+\# C_{M}^{\prime \prime}+\# C_{R} \leq r$. But then the triple $\left(C_{L}, C_{M}, C_{R}\right) t$-separates $A$ from $B$ in $\widetilde{G}$ where $C_{L}=\left\{c: c^{\prime} \in C_{L}^{\prime}\right\}$ and $C_{M}=\left\{c: c^{\prime \prime} \in C_{M}^{\prime \prime}\right\}$.
4. Conclusions and open problems. We have shown that the $t$-separation criterion can be used to characterize vanishing determinants of the covariance matrix in Gaussian directed and undirected graphical models and mixed graph models. These results have potential uses in inferential procedures with Gaussian graphical models, generalizing procedures based on the tetrad constraints [10] in directed graphical models. The tetrad constraints are the special case of $2 \times 2$ determinants. Both referees have pointed out that these results also extend to graphical models with cycles, by applications of the more general version of the Gessel-ViennotLindström lemma for general graphs [5]. We have focused on the case of directed acyclic graphs because these are the most familiar in the graphical models literature.

Our results suggest a number of different research directions. For example, for which mixed graphs is it true that vanishing low rank submatrices characterize the distributions that belong to the model? This is known to hold for both acyclic directed graphs and undirected graphs, but can fail in general mixed graphs.

Another open problem is to determine what significance the $t$-separation criterion has for graphical models with not necessarily normal random variables, in particular, for discrete variables. It would be worthwhile to determine whether $t$ separation can be translated into constraints on probability densities for graphical models with more general random variables.

Acknowledgments. We thank Mathias Drton for suggesting this problem to us. The referees and associate editor provided many useful comments which have led to this improved version. Jan Draisma, who was originally an anonymous referee on this paper, provided the first proof of Theorem 2.17 which was a conjecture in an earlier version of the paper.
