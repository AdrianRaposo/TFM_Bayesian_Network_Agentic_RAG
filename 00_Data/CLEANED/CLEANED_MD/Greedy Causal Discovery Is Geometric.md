# GREEDY CAUSAL DISCOVERY IS GEOMETRIC 

SVANTE LINUSSON, PETTER RESTADH, AND LIAM SOLUS


#### Abstract

Finding a directed acyclic graph (DAG) that best encodes the conditional independence statements observable from data is a central question within causality. Algorithms that greedily transform one candidate DAG into another given a fixed set of moves have been particularly successful, for example the GES, GIES, and MMHC algorithms. In 2010, Studený, Hemmecke and Lindner introduced the characteristic imset polytope, $\mathrm{CIM}_{p}$, whose vertices correspond to Markov equivalence classes, as a way of transforming causal discovery into a linear optimization problem. We show that the moves of the aforementioned algorithms are included within classes of edges of $\mathrm{CIM}_{p}$ and that restrictions placed on the skeleton of the candidate DAGs correspond to faces of $\mathrm{CIM}_{p}$. Thus, we observe that GES, GIES, and MMHC all have geometric realizations as greedy edge-walks along $\mathrm{CIM}_{p}$. Furthermore, the identified edges of $\mathrm{CIM}_{p}$ strictly generalize the moves of these algorithms. Exploiting this generalization, we introduce a greedy simplex-type algorithm called greedy CIM, and a hybrid variant, skeletal greedy CIM, that outperforms current competitors among hybrid and constraint-based algorithms.


## 1. INTRODUCTION

The use of directed acyclic graphs (DAGs) to model complex systems has increased rapidly during the last thirty years, and today they are used in a wide variety of fields $[5,11,14,16]$. Given a positive integer $p$ we let $[p]:=\{1,2, \ldots, p\}$. To each DAG $\mathcal{G}=([p], E)$ we associate a set of random variables $X_{1}, \ldots, X_{p}$, and the conditional independence (CI) statements $X_{i} \Perp X_{\operatorname{nd} \mathcal{G}(i) \backslash \mathrm{pa}_{\mathcal{G}}(i)} \mid X_{\mathrm{pa}_{\mathcal{G}}(i)}$ for all $i \in[p]$. Here, $\mathrm{pa}_{\mathcal{G}}(i)$ denotes the parents and $\operatorname{nd} \mathcal{G}(i)$ denotes the non-descendants of $i$ in $\mathcal{G}$. A joint probability distribution $P\left(X_{1}, \ldots, X_{p}\right)$ is Markov to a DAG $\mathcal{G}$ if it entails all such CI statements. The goal of causal discovery is to learn an unknown DAG $\mathcal{G}=([p], E)$ from samples drawn from a joint distribution $P$ over $\left(X_{1}, \ldots, X_{p}\right)$ that is assumed to be Markov to $\mathcal{G}$. Unfortunately, this cannot generally be done as multiple DAGs can encode the same set of CI statements. Two such DAGs are called Markov equivalent, and they belong to the same Markov equivalence class (MEC). Thus, the basic problem of causal discovery is to identify the MEC of $\mathcal{G}$, and a variety of causal discovery algorithms for doing so have been proposed $[4,7,17,22]$.

Many of the more competitive algorithms are score-based and greedy, like the Greedy Equivalence Search (GES) [4], or the Greedy Interventional Equivalence Search (GIES) applied to only observational data [7]. These algorithms aim to maximize a score function, such as the Bayesian Information Criterion (BIC). Others aim to recover the MEC from a collection of CI statements by treating causal discovery as a constraint-satisfaction problem, like the PC algorithm [17, 22]. While the score-based methods tend to be more accurate on both simulated and real data, the constraint-based algorithms are usually faster. More recent algorithms have tried

using a hybrid approach, like Max-Min Hill Climbing (MMHC) [23], where the authors restrict the search space by using CI tests and then take a greedy score-based approach. In the hybrid setting, one can leverage the speed of constraint-based methods versus the accuracy of score-based methods.

Alternatively, Studený, Hemmecke and Lindner gave a geometric interpretation of MECs by realizing them as $0 / 1$-vectors called characteristic imsets [20]. Maximizing a score equivalent and (additive) decomposable function over the MECs of DAGs on $p$ nodes then becomes equivalent to maximizing a linear function over these vectors. Thus, finding the BIC-optimal MEC can be seen as a linear optimization problem over the characteristic imset (CIM) polytope, $\mathrm{CIM}_{p}$. This approach has also been used to learn decomposable models, with promising results [21]. While most research on these polytopes has focused on the identification of facets, our main focus will be their edges and other lower-dimensional faces.

We begin by showing that the reduced search space of the aforementioned popular hybrid and constraint-based algorithms are realized as faces of $\mathrm{CIM}_{p}$ (see Proposition 2.4). In Section 3, we then identify classes of edges corresponding to, and strictly generalizing, the moves of GES, GIES, and MMHC. Thus, we obtain a geometric interpretation of these algorithms as edge-walks along faces of a convex polytope. A more recent hybrid algorithm called greedy SP [15] also admits a geometric interpretation as an edge-walk along a convex polytope. Since GES, GIES, MMHC, and greedy SP are currently the benchmark standards for greedy causal discovery algorithms based solely on observational data, we can then view greedy causal discovery as a purely geometric process; i.e., as an edge-walk along a convex polytope (see Theorem 3.10). Furthermore, as the characterized edges of $\mathrm{CIM}_{p}$ strictly generalize the moves of GES, GIES, and MMHC, we propose a hybrid algorithm that we call skeletal greedy CIM (Algorithm 1) and a greedy score-based algorithm that we call greedy CIM (Algorithm 2).

In Section 4, we study how greedy CIM and skeletal greedy CIM perform on simulated data and compare their performance with the state-of-the-art. We observe that the additional moves given by the classified edges of $\mathrm{CIM}_{p}$ result in both the hybrid and purely score-based algorithms performing at least as well as all (respective) benchmark standards. In the case of hybrid algorithms, skeletal greedy CIM consistently outperforms all other hybrid alternatives. These observations purport the edges of the characteristic imset polytope as the natural object of study in efforts to improve the accuracy of modern causal discovery algorithms. The more technical proofs of the main theorems in Section 3 can be found in Appendix A.

# 2. Preliminaries 

For an introduction to the theory of convex polytopes, see for example [26]. We start with a brief summary of the graph theory notation used in the paper. All graphs are assumed to be simple.

Let $G=([p], E)$ be an undirected graph. For a pair of distinct nodes $i, j \in[p]$ we write $i-j \in G$ if $\{i, j\} \in E$. We denote the set of neighbors of $i$ in $G$ by $\operatorname{ne}_{G}(i)$. For a directed graph $\mathcal{G}=([p], E)$ we likewise write $i \rightarrow k \in \mathcal{G}$ if $(i, k) \in E$. Then $i$ is said to be a parent of $k$ and $k$ a child of $i$. The sets of parents and children of $k$ in $\mathcal{G}$ are denoted by $\mathrm{pa}_{\mathcal{G}}(k)$ and $\operatorname{ch}_{\mathcal{G}}(k)$ respectively. The skeleton of a directed graph $\mathcal{G}$ is the undirected graph $G$ where we replace $k \rightarrow i \in \mathcal{G}$ with $k-i \in G$. We say that two nodes are neighbors in $\mathcal{G}$ if they are neighbors in the skeleton of

$\mathcal{G}$. For a directed graph $\mathcal{G}$ we say that $\left\langle k_{0}, k_{1}, \ldots, k_{n}\right\rangle$ is a directed path from $k_{0}$ to $k_{n}$ in $\mathcal{G}$ if $k_{i} \rightarrow k_{i+1} \in \mathcal{G}$ for all $0 \leq i \leq n-1$ and all $k_{i}$ different. We say that $\left\langle k_{0}, k_{1}, \ldots, k_{n}\right\rangle$ is a path in $\mathcal{G}$ if it is a path in the skeleton of $G$. Then a directed cycle is a directed path with an extra edge $k_{n} \rightarrow k_{0}$ and a directed graph $\mathcal{G}$ is a directed acyclic graph (DAG) if $\mathcal{G}$ does not have a directed cycle. A node $i$ is a descendant of $k$ if there exists a directed path from $k$ to $i$, and $i \neq k$. The set of descendants is denoted $\operatorname{de}_{\mathcal{G}}(k)$, and, by definition, does not include $k$. Every node that is not $k$, nor a descendant of $k$, is a non-descendant, and the set of all such nodes is denoted $\operatorname{nd}_{\mathcal{G}}(k)$. The induced subgraph on $A \subseteq[p]$ is denoted $\left.\mathcal{G}\right|_{A}$. We recommend [9] for a background on graphs and DAG models.

A $v$-structure is an induced subgraph of the form $i \rightarrow j \leftarrow k$. The following is a classical result of Verma and Pearl.

Theorem 2.1. [25] Two DAGs are Markov equivalent if and only if they have the same skeleton and the same $v$-structures.

Let $\mathcal{G}=([p], E)$ be a DAG. It is well-known that a joint distribution over $\left(X_{1}, \ldots, X_{p}\right)$ is Markov to $\mathcal{G}$ if and only if its probability density function $P$ factorizes as

$$
P\left(X_{1}, \ldots, X_{p}\right)=\prod_{i \in[p]} P\left(X_{i} \mid X_{\mathrm{pa}_{\mathcal{G}}(i)}\right)
$$

To obtain a unique graphical representation of each MEC, Andersson, Madigan, and Perlman proposed and gave a complete characterization of essential graphs [1]. Studený proposed a more geometric interpretation of Markov equivalence via vectors that encode the CI statements, called the standard imset [18, 19]. Following this idea, in [20] Studený, Hemmecke, and Lindner introduced the characteristic imset, $c_{\mathcal{G}}$, of a DAG $\mathcal{G}$ that encodes the factorization of Equation (1). As the factorization determines the MEC, this gives us a unique representation of each MEC. Formally it is a function $c_{\mathcal{G}}:\{S \subseteq[p]:|S| \geq 2\} \rightarrow\{0,1\}$ defined as

$$
c_{\mathcal{G}}(S):= \begin{cases}1 & \text { if there exists } i \in S \text { such that for all } j \in S \backslash\{i\}, j \in \mathrm{pa}_{\mathcal{G}}(i) \\ 0 & \text { otherwise }\end{cases}
$$

As $c_{\mathcal{G}}$ is a function from a finite set we can identify it with a vector in $\mathbb{R}^{2^{p}-p-1}$ where the basis vectors, $e_{S}$, are indexed by the sets in $\{S \subseteq[p]:|S| \geq 2\}$. Similar to essential graphs, characteristic imsets then give us a unique representation for each MEC.

Theorem 2.2. [20] Two DAGs $\mathcal{G}$ and $\mathcal{H}$ are Markov equivalent if and only if $c_{\mathcal{G}}=c_{\mathcal{H}}$

The next lemma follows from the definition of characteristic imsets and provides a way to recover the structure of the graph from this vector encoding.

Lemma 2.3. [20] Let $\mathcal{G}$ be a $D A G$ on $[p]$. Then for any distinct nodes $i, j$, and $k$ we have
(1) $i \rightarrow j$ or $i \leftarrow j$ in $\mathcal{G}$ if and only if $c_{\mathcal{G}}(\{i, j\})=1$.
(2) $i \rightarrow j \leftarrow k$ is a $v$-structure in $\mathcal{G}$ if and only of $c_{\mathcal{G}}(\{i, j, k\})=1$ and $c_{\mathcal{G}}(\{i, k\})=0$

As we can see, the characteristic imset encodes the skeleton and the v-structures in the 2- and 3-sets. Any (additive) decomposable and score equivalent function can be seen as an affine linear function over the vectors $c_{\mathcal{G}}$ [20]. An important example of such a function is the Bayesian Information Criterion (BIC). Given $n$ independent samples, $\mathbf{D}$, drawn from the joint distribution of $\left(X_{1}, \ldots, X_{p}\right)$, the BIC is defined as

$$
\operatorname{BIC}(\mathcal{G}, \mathbf{D})=\log P\left(\mathbf{D} \mid \hat{\theta}, \mathcal{G}^{h}\right)-\frac{d}{2} \log (n)
$$

Here $\hat{\theta}$ is the maximum-likelihood estimate for the network parameters, $d$ denotes the number of free parameters of $\mathcal{G}$, and $\mathcal{G}^{h}$ denotes the hypothesis that $\mathbf{D}$ are i.i.d samples from a distribution that entails exactly the CI statements encoded by $\mathcal{G}$ [4]. Thus, the question of learning the BIC-optimal MEC can be stated as finding the maximum of an affine linear function over a finite set of vectors in a finitedimensional real vector space. This motivates the definition of the characteristic imset polytope (CIM polytope) for DAGs on $p$ nodes:

$$
\operatorname{CIM}_{p}:=\operatorname{conv}\left(c_{\mathcal{G}} \in \mathbb{R}^{2^{p}-p-1}: \mathcal{G}=([p], E) \text { a DAG }\right)
$$

As $\mathrm{CIM}_{p}$ is defined as a $0 / 1$-polytope (that is, the convex hull of vectors with entries that are either 0 or 1 ) the vertices of $\mathrm{CIM}_{p}$ are precisely $\left\{c_{\mathcal{G}}: \mathcal{G}=([p], E)\right.$ a DAG $\}$ [26].

A classic constraint-based causal discovery algorithm is the PC algorithm [17, 22]. It first utilizes CI tests to learn a skeleton $G$ and then to orient v-structures. The Max-Min Hill Climbing (MMHC) algorithm [23] utilizes CI tests to learn possible edges in the skeleton, and then uses a score-based method to construct a DAG restricted to using only these edges. Following the idea of utilizing CI tests to obtain a skeleton, we consider another polytope, closely related to $\mathrm{CIM}_{p}$. Let $G=([p], E)$ be an undirected graph and define the CIM polytope for $G$ to be

$$
\operatorname{CIM}_{G}:=\operatorname{conv}\left(c_{\mathcal{G}} \in \mathbb{R}^{2^{p}-p-1}: \mathcal{G}=([p], E) \text { a DAG with skeleton } G\right)
$$

Thus, like the PC algorithm, we can learn an undirected skeleton, $G$, via CI tests, and then take a score-based approach via an edge-walk on $\mathrm{CIM}_{G}$ optimizing the BIC. Such a method is called a hybrid algorithm as it first uses a constraint-based approach to restrict the search space, and then uses a score-based approach to find the optimal DAG. An immediate question is then: what is the relationship between $\mathrm{CIM}_{p}$ and $\mathrm{CIM}_{G}$ ? To this end we have the following proposition:

Proposition 2.4. Let $H=([p], E)$ and $H^{\prime}=\left([p], E^{\prime}\right)$ be two undirected graphs such that $E \subseteq E^{\prime}$. Then

$$
\operatorname{conv}\left(c_{\mathcal{G}} \in \mathbb{R}^{2^{p}-p-1}: \mathcal{G} \text { a DAG with skeleton } G=([p], D) \text { where } E \subseteq D \subseteq E^{\prime}\right)
$$

is a face of $\mathrm{CIM}_{p}$.
Proof. It is enough to find a cost function, $w_{H, H^{\prime}}$, which maximizes precisely over the set

$$
\left\{c_{\mathcal{G}} \in \mathbb{R}^{2^{p}-p-1}: \mathcal{G} \text { a DAG with skeleton } G=([p], D) \text { where } E \subseteq D \subseteq E^{\prime}\right\}
$$

out of all characteristic imsets. So define

$$
w_{H, H^{\prime}}(S):= \begin{cases}0 & \text { if }|S| \neq 2 \text { or } S \in E^{\prime} \backslash E \\ 1 & \text { if } S \in E \\ -1 & \text { otherwise }\end{cases}
$$

Notice that $w_{H, H^{\prime}}$ is only non-zero for sets with cardinality 2. Then if we have $\mathcal{G}$ with skeleton $G=([p], D)$ we get via Lemma 2.3

$$
\begin{aligned}
w_{H, H^{\prime}}^{T} c_{\mathcal{G}} & =\sum_{S \subseteq[p],|S| \geq 2} w_{H, H^{\prime}}(S) c_{\mathcal{G}}(S) \\
& =|D \cap E|-\left|D \backslash E^{\prime}\right|
\end{aligned}
$$

The right-hand-side is maximized exactly when $E \subseteq D \subseteq E^{\prime}$. Thus $w_{H, H^{\prime}}$ maximizes exactly over the given set.

Taking $H=H^{\prime}=G$, we get the following corollary.
Corollary 2.5. Let $G=([p], E)$ be an undirected graph. Then $\mathrm{CIM}_{G}$ is a face of $\mathrm{CIM}_{p}$.

# 3. Edges of the CIM Polytope 

To construct efficient algorithms for finding the maximum of a linear score function over a polytope, we need some description of the polytope. Assume we are given an arbitrary polytope $Q$ and a linear function $s$. It is immediate that the set maximizing $s^{T} q$ for $q \in Q$ is a face of $Q$. Thus, any linear function assumes its maximum value over $Q$ at at least one vertex of $Q$. An edge-walk on $Q$ to maximize a linear function $s$ is done in the following way: Start at any vertex $q_{0}$ of $q$, and set $i:=0$. At each step, choose $q_{i+1}$ such that $\operatorname{conv}\left(q_{i}, q_{i+1}\right)$ is an edge of the polytope and $s^{T} q_{i}<s^{T} q_{i+1}$. If no such edges exist, return $q_{i}$.

Assuming that we know every edge of $Q$, such an edge-walk will always return a vertex maximizing $s$. Making additional assumptions on the score function or looking for edges in a certain order can sometimes give us similar guarantees. For example, see [15]. As a direct computation of all edges of $\mathrm{CIM}_{p}$ and $\mathrm{CIM}_{G}$ is not feasible for large $p$, we will instead identify edges of these polytopes in terms of relations between the characteristic imsets they connect. As the characteristic imsets are the vertices of these polytopes we will see how these relations label edges of the polytope.

We will define two relations, one on $\mathrm{CIM}_{G}$ and one on $\mathrm{CIM}_{p}$. Utilizing the first one we propose a hybrid algorithm that first learns an undirected skeleton via conditional independence tests and then performs an edge-walk along $\mathrm{CIM}_{G}$, greedily optimizing BIC. Then using both we also define a purely score-based algorithm that performs an edge-walk on $\mathrm{CIM}_{p}$, again greedily optimizing the BIC.

The edges we identify will include, as a special case, the moves of Greedy Equivalence Search (GES) [4]. This positively answers a question raised by Steffen Lauritzen at the Workshop on Graphical Models: Conditional Independence and Algebraic Structures, TU Munich, 2019: Do the moves of GES have a geometric interpretation in terms of the $\mathrm{CIM}_{p}$ polytope? More generally, we recover a geometric interpretation of the GIES algorithm [7] in the case of purely observational data, as well as the hybrid MMHC algorithm.

To this end, we will begin by defining relations between imsets. These relations are motivated by our graphical understanding of Markov equivalence, but also turn out to generalize our intuition.

Definition 3.1 (Turn pair). Let $\mathcal{G}$ and $\mathcal{H}$ be two DAGs on node set $[p]$ and with skeleton $G$. Suppose there exist $i, j, S_{i} \subseteq[p] \backslash\{i, j\}$ and $S_{j} \subseteq[p] \backslash\{i, j\}$ such that
(1) $c_{\mathcal{G}}(\{i, j\})=1$;
(2) $c_{\mathcal{G}}(S \cup\{i\})=1$ for all $S \subseteq S_{i}$ with $|S| \geq 1$;
(3) $c_{\mathcal{G}}(S \cup\{j\})=1$ for all $S \subseteq S_{j}$ with $|S| \geq 1$;
(4) either $S_{i} \nsubseteq \mathrm{ne}_{G}(j)$ or $S_{j} \nsubseteq \mathrm{ne}_{G}(i)$.

Then we say that $\{\mathcal{G}, \mathcal{H}\}$ is a turn pair with respect to $\left(i, j, S_{i}, S_{j}\right)$ if

$$
c_{\mathcal{H}}=c_{\mathcal{G}}+\sum_{S \in \mathcal{S}^{+}} e_{S}-\sum_{S \in \mathcal{S}^{-}} e_{S}
$$

where $\mathcal{S}^{+}:=\{T \cup\{i, j\}: T \subseteq S_{i}, T \nsubseteq \mathrm{ne}_{G}(j)\}$ and $\mathcal{S}^{-}:=\{T \cup\{i, j\}: T \subseteq S_{j}, T \nsubseteq$ $\left.\operatorname{ne}_{G}(i)\right\}$.

Note that one of $S_{i}$ and $S_{j}$ can may be empty, but not both by (4). The name "turn pair" is explained via the next proposition. We observe that $\{\mathcal{G}, \mathcal{H}\}$ is a turn pair with respect to $\left(i, j, S_{i}, S_{j}\right)$ if and only if $\{\mathcal{H}, \mathcal{G}\}$ is a turn pair with respect to $\left(j, i, S_{j}, S_{i}\right)$. Moreover, as the edges of a polytope lack orientation, a greedy edgewalk may walk in either direction along a given edge. Thus we view our relations between characteristic imsets and their corresponding DAGs as unordered pairs, as opposed to ordered pairs.

If $\mathcal{G}$ is a directed graph with $i \rightarrow j \in \mathcal{G}$ we denote by $\mathcal{G}_{i \leftarrow j}$ the directed graph identical to $\mathcal{G}$ except that the edge $i \rightarrow j$ is replaced with $i \leftarrow j$.

Proposition 3.2. Let $\mathcal{G}$ be a $D A G$ with $i \rightarrow j \in \mathcal{G}$. If $\mathcal{G}_{i \leftarrow j}$ is a $D A G$, then either $\mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ are Markov equivalent, or $\left\{\mathcal{G}, \mathcal{G}_{i \leftarrow j}\right\}$ is a turn pair.

The case in which $\mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ are Markov equivalent is characterized in [3]. Hauser and Bühlmann define a collection of turning moves in terms of the essential graph (see [7, Propositions 31 and 34]). They characterize when $\mathcal{G}_{i \leftarrow j}$ is a DAG and the relation between the essential graphs of $\mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ when this is the case. The above proposition shows that in the case of no interventions, their turning moves are turn pairs. The converse is not true, as shown in Example 3.3.

Example 3.3. By Proposition 3.2, turn pairs capture whenever we turn an edge in a DAG, transforming it into another (non-Markov equivalent) DAG, in terms of characteristic imsets. The converse of Proposition 3.2 is, on the other hand, not true. That is, there exists a turn pair $\{\mathcal{G}, \mathcal{H}\}$ for which there is no DAG $\mathcal{D}$ Markov equivalent to $\mathcal{G}$ such that $\mathcal{D}_{i \leftarrow j}$ is Markov equivalent to $\mathcal{H}$. As an example of this, take $\mathcal{G}$ and $\mathcal{H}$ as in Figure 1. It can be checked that $\{\mathcal{G}, \mathcal{H}\}$ is a turn pair with respect to $\left(i, j,\left\{s_{1}, s_{2}\right\}, \emptyset\right)$, but it follows from Theorem 2.1 that $i \leftarrow j \in \mathcal{D}$ for all DAGs $\mathcal{D}$ Markov equivalent to $\mathcal{G}$ or $\mathcal{H}$.

By Proposition 3.2, turn pairs arise naturally from an intuitive graphical interpretation of reversing an edge and, as Example 3.3 shows, strictly generalize this intuition.

Theorem 3.4. If $\{\mathcal{G}, \mathcal{H}\}$ is a turn pair, then $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge of $\mathrm{CIM}_{G}$ where $G$ is the skeleton of $\mathcal{G}$ and $\mathcal{H}$.

![img-0.jpeg](img-0.jpeg)

Figure 1. An example of a turn pair not arising from changing the direction of any one edge in any DAG in the MEC.

```
Algorithm 1 Skeletal Greedy CIM
    Input: Data D.
    Output: A characteristic imset \(c_{\mathcal{G}}\).
    Perform CI tests to find the underlying skeleton \(G^{1}\)
    Let \(\mathcal{G}\) a DAG with skeleton \(G\)
    \(c_{\mathcal{D}} \leftarrow\) null
    while \(c_{\mathcal{D}} \neq c_{\mathcal{G}}\) do
        \(c_{\mathcal{G}} \leftarrow c_{\mathcal{D}}\)
        \(c_{\mathcal{D}} \leftarrow\) turn phase (Algorithm 4 in Appendix B with \(c_{\mathcal{D}}\) as input.)
    end whilereturn \(c_{\mathcal{G}}\)
```

The above theorem tells us that moving via turn pairs is in fact an edge-walk along $\mathrm{CIM}_{G}$. For algorithms based on such edge-walks to be able to perform well we would like to move around $\mathrm{CIM}_{G}$ relatively freely. In the following proposition we show that the edges labeled by turn pairs are enough to traverse the polytope $\mathrm{CIM}_{G}$.

Proposition 3.5. Let $G$ be a graph and $\mathcal{G}$ and $\mathcal{H}$ two DAGs with skeleton $G$. Then there exists a sequence of edges $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{D}_{1}}\right), \operatorname{conv}\left(c_{\mathcal{D}_{1}}, c_{\mathcal{D}_{2}}\right), \ldots, \operatorname{conv}\left(c_{\mathcal{D}_{m-1}}, c_{\mathcal{D}_{m}}\right), \operatorname{conv}\left(c_{\mathcal{D}_{m}}, c_{\mathcal{H}}\right)$, of $\mathrm{CIM}_{G}$ such that each pair $\left\{\mathcal{G}, \mathcal{D}_{1}\right\},\left\{\mathcal{D}_{1}, \mathcal{D}_{2}\right\}, \ldots,\left\{\mathcal{D}_{m-1}, \mathcal{D}_{m}\right\}$, and $\left\{\mathcal{D}_{m}, \mathcal{H}\right\}$ is a turn pair.

Proof. By Proposition 3.2 it is enough to show that there exists a sequence of DAGs $\mathcal{G}=\mathcal{D}_{0}, \ldots, \mathcal{D}_{n}=\mathcal{H}$ such that $\mathcal{D}_{i}$ and $\mathcal{D}_{i+1}$ differ by the direction of a single edge. To find such a sequence it is enough to show that for any two DAGs, $\mathcal{G}$ and $\mathcal{H}$, that share the same skeleton, there exists an edge $i-j \in G$ such that $i \rightarrow j \in \mathcal{G}$, $i \leftarrow j \in \mathcal{H}$, and $\mathcal{G}_{i \leftarrow j}$ is a DAG.

We can partially order all edges via $i^{\prime} \rightarrow j^{\prime} \preceq i \rightarrow j$ if and only if $j^{\prime} \in \operatorname{de}_{\mathcal{G}}(j)$ or, if $j^{\prime}=j, i \in \operatorname{de}\left(i^{\prime}\right)$. Note that we sort the children according to $\mathcal{G}$ and the parents in reverse. Consider all edges that differ between $\mathcal{G}$ and $\mathcal{H}$ and consider such an edge $i \rightarrow j$ that is maximal in the prescribed order. For the sake of contradiction assume there is a cycle in $\mathcal{G}_{i \leftarrow j}$. Then there is a directed path $i \rightarrow \cdots \rightarrow j$ different from the edge $i \rightarrow j$. However, every edge in this path is bigger in the order $\preceq$, and hence this path is present in $\mathcal{H}$ as well. This gives us a directed cycle in $\mathcal{H}$, a contradiction. Hence, with this choice of the edge $i \rightarrow j, \mathcal{G}_{i \leftarrow j}$ will be a DAG and the result follows.

The edges labeled by turn pairs thus connect the polytope $\mathrm{CIM}_{G}$ in the sense that for any two DAGs, $\mathcal{G}$ and $\mathcal{H}$, with skeleton $G$, there exists a sequence of turn pairs that begins at $c_{\mathcal{G}}$ and ends at $c_{\mathcal{H}}$. Thus we can take a simplex-type approach to finding the BIC-optimal MEC. To this end, we propose a hybrid greedy causal discovery algorithm in which we first learn the skeleton $G$ via CI tests, similar to the PC algorithm, and then perform a restricted edge-walk on $\mathrm{CIM}_{G}$ utilizing the edges labeled by turn pairs, which we call the turn phase. We call this algorithm skeletal greedy CIM (see Algorithm 1).

Up until now we have primarily studied $\mathrm{CIM}_{G}$, but we would like to move between vertices of $\mathrm{CIM}_{G}$ and $\mathrm{CIM}_{H}$ when $G$ and $H$ are not equal. A direct consequence of Proposition 3.2 and Theorem 3.4 is that the turning phase of GIES [7] is a type of edge-walk over $\mathrm{CIM}_{G}$. The question then arises whether it holds for the forward and backward phases as well. Thus, we would like a definition similar to Definition 3.1 but for adding an edge.

Definition 3.6 (Edge pair). Let $\mathcal{G}$ and $\mathcal{H}$ be two DAGs on node set $[p]$. Suppose there exists distinct nodes $i, j$ and a set $S^{*} \subseteq[p] \backslash\{i, j\}$ such that
(1) $c_{\mathcal{G}}(\{i, j\})=0$,
(2) $c_{\mathcal{G}}(S \cup\{i\})=1$ for all $S \subseteq S^{*}$ with $|S| \geq 1$.

Then we say that $\{\mathcal{G}, \mathcal{H}\}$ is an edge pair with respect to $\left(i, j, S^{*}\right)$ if

$$
c_{\mathcal{H}}=c_{\mathcal{G}}+\sum_{S \in \mathcal{S}_{+i \leftarrow j}} e_{S}
$$

where $\mathcal{S}_{+i \leftarrow j}:=\{S \cup\{i, j\}: S \subseteq S^{*}\}$.
Let $\mathcal{G}$ be a DAG and assume $i$ and $j$ are not adjacent in the skeleton of $\mathcal{G}$. We denote by $\mathcal{G}_{+i \leftarrow j}$ the directed graph identical to $\mathcal{G}$ with the edge $i \leftarrow j \in \mathcal{G}_{+i \leftarrow j}$. Then, similar to Proposition 3.2, we have the following:

Proposition 3.7. Let $\mathcal{G}$ be a $D A G$ and assume $i$ and $j$ are not adjacent in the skeleton of $\mathcal{G}$. If $\mathcal{G}_{+i \leftarrow j}$ is a $D A G$, then $\left\{\mathcal{G}, \mathcal{G}_{+i \leftarrow j}\right\}$ is an edge pair.

Thus edge pairs give an interpretation, in terms of characteristic imsets, of adding an edge to a graph the same way as turn pairs give an interpretation of changing the direction of an edge. However, in this case we believe that the converse holds.

Conjecture 3.8. Let $\{\mathcal{G}, \mathcal{H}\}$ be an edge pair with respect to $\left(i, j, S^{*}\right)$. Then there exists a $D A G \mathcal{G}^{\prime}$ Markov equivalent to $\mathcal{G}$ such that $\mathcal{G}_{+i \leftarrow j}^{\prime}$ is a $D A G$ Markov equivalent to $\mathcal{H}$.

Similar to turn pairs, edge pairs constitute edges of $\mathrm{CIM}_{p}$.
Theorem 3.9. If $\{\mathcal{G}, \mathcal{H}\}$ is an edge pair, then $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge of $\mathrm{CIM}_{p}$ where $p$ is the number of nodes in $\mathcal{G}$ and $\mathcal{H}$.

By combining Proposition 3.7 with Theorem 3.9 we obtain a positive answer to the aforementioned question by Steffen Lauritzen; namely, we see that the moves of GES have a geometric interpretation as edges of $\mathrm{CIM}_{p}$. Going even further, by combining this observation with Proposition 3.2 and Theorem 3.4, we see that the moves of the GIES algorithm, which (in the case of purely observational data) extends GES with an additional turn phase, also admit a geometric interpretation

[^0]
[^0]:    ${ }^{1}$ For example we can use the skeleton algorithm from the pcalg package in $\mathrm{R}[7,8]$.

```
Algorithm 2 Greedy CIM
Input: Data D.
Output: A characteristic imset \(c_{\mathcal{G}}\).
    Let \(\mathcal{G}\) be the DAG without any edges
    \(c_{\mathcal{D}} \leftarrow\) null
    while \(c_{\mathcal{D}} \neq c_{\mathcal{G}}\) do
        \(c_{\mathcal{G}} \leftarrow c_{\mathcal{D}}\)
        \(c_{\mathcal{D}} \leftarrow\) edge phase (Algorithm 3 in Appendix B with \(c_{\mathcal{D}}\) as input.)
        \(c_{\mathcal{D}} \leftarrow\) turn phase (Algorithm 4 in Appendix B with \(c_{\mathcal{D}}\) as input.)
    end while
    return \(c_{\mathcal{G}}\)
```

as edges of $\mathrm{CIM}_{p}$. Similarly, the MMHC algorithm performs a greedy search akin to that of GES, but it first restricts the search space to a subset of edges that are allowed to appear in the skeleton. An application of Proposition 2.4 with $H=([p], \emptyset)$ thus extends these results to the MMHC algorithm. Since greedy SP [15] is defined as an edge-walk along another family of convex polytopes (called DAG associahedra [10]), these observations imply that the popular greedy scorebased and hybrid causal discovery algorithms (GES, GIES, MMHC, and greedy SP) can all be viewed as edge-walks along a convex polytope. Thus greedy causal discovery is, in a sense, geometric. We summarize this observation in the following theorem:

Theorem 3.10. The following causal discovery algorithms are greedy edge-walks along a convex polytope:
(1) GES,
(2) GIES with purely observational data,
(3) MMHC, and
(4) Greedy SP.

Example 3.3 further shows that the edges of $\mathrm{CIM}_{p}$ labeled by turn and edge pairs are a strict generalization of the moves of GES and GIES. Hence, any edgewalk that greedily optimizes BIC over $\mathrm{CIM}_{p}$ can be viewed as an extension of these causal discovery algorithms.

In regards to Theorem 3.9, we propose the purely score-based algorithm greedy CIM (Algorithm 2) which extends GES and GIES. This algorithm is, as opposed to skeletal greedy CIM (Algorithm 1), not a hybrid algorithm, as we do not rely on conditional independence tests to find the skeleton. Instead it relies on an edge phase that consists of a restricted edge-walk, utilizing the edges of $\mathrm{CIM}_{p}$ determined by edge pairs. Due to Theorem 3.9, the greedy CIM algorithm consists solely of an edge-walk on $\mathrm{CIM}_{p}$. In Section 4 we analyze how greedy CIM and skeletal greedy CIM perform on simulated data relative to GES, GIES, MMHC, greedy SP, and the PC algorithm.

# 4. Simulations 

In Section 3 we proposed two algorithms, skeletal greedy CIM (Algorithm 1), and greedy CIM (Algorithm 2). Here we compare the performance of these algorithms on simulated data with the state-of-the-art.

An implementation of all algorithms discussed in this section is available at [13]. The simulated data was produced in $R$ [12] using linear structural equation models with Gaussian noise. The true underlying DAG $\mathcal{G}^{*}$ was chosen randomly using an Erdős-Rényi model on $p=8$ vertices and expected neighborhood size $d$, which we varied over the interval $[0.5,7]$. Each edge $i \rightarrow j$ was given an edge-weight $w_{i, j}$ chosen uniformly from $[-1,-0.25] \cup[0.25,1]$. The direction of the edges were given by a linear order of the vertices, sampled uniformly from all linear orders. We then sampled from a multivariate Gaussian distribution over the random variables $X_{1}, \ldots, X_{p}$ where $X_{i}=\varepsilon_{i}+\sum_{k \in \mathrm{pa}_{0^{+}}(i)} w_{k, i} X_{k}$. Here, the $\varepsilon_{i}$ are independent and normally distributed random variables with mean 0 and variance 1 . We produced 100 models for each $d$ and from each model we drew $n=10,000$ samples. This was done via the MASS library [24]. As the implementation of greedy CIM and skeletal greedy CIM available at [13] is done in Python, we used the rpy2 module for the $R$-to-Python conversions.

To produce the undirected skeleton in Algorithm 1 we used the skeleton algorithm in the pcalg package [7, 8]. The algorithm skeleton requires a significance level $\alpha$ for the CI tests, which we varied over $\{0.01,0.001,0.0001\}$. Skeletal greedy CIM, greedy CIM, GES, and GIES all aim to optimize BIC (see Equation (2)) which we computed for our models via the GaussLOpenObsScore-class from the pcalg package. In order to fairly compare the different algorithms that are each a single edge-walk along a convex polytope (according to Theorem 3.10) we ran greedy SP with no restarts and unbounded search depth $(r=1, d=\infty)$ [15]. (Note this choice of parameter settings results in greedy SP performing worse than it did for the same simulations in [15, Figure 5], as the parameter settings used to generate [15, Figure 5] were $r=10$ and $d=4$.) In Figure 2 we see the ratio of models recovered from the samples versus the expected neighborhood size $d$. In Figure 3 we compare the model recovery rate and the average Structural Hamming Distance (SHD) (see [23] for a definition) to the true model versus the average expected neighborhood size $d$.

In Figure 2a, Figure 2b, and Figure 2c we compared all algorithms relying on CI tests (i.e., all constraint-based and hybrid algorithms). We see that skeletal greedy CIM has a higher recovery rate than greedy SP, MMHC and the PC algorithm. Note that both skeletal greedy CIM and PC are restricted by the performance of the skeleton algorithm, which is the algorithm used to identify the skeleton of the learned DAG. Thus, we have also included how often skeleton finds the true skeleton. We see that, if the correct skeleton is identified, skeletal greedy CIM almost always learns the true MEC. However, the same is not true for the PC algorithm. Based on this near optimality of skeletal greedy CIM, we cannot expect the performance of skeletal greedy CIM to increase by much, even if more edges of $\mathrm{CIM}_{G}$ are identified and added to the implementation. The main difference of skeletal greedy CIM and MMHC is that skeletal greedy CIM relies on CI tests to determine the skeleton, as opposed to MMHC, which only restricts to a set of possible skeletons. The fact that skeletal greedy CIM outperforms MMHC in Figure 2 suggests that the set of moves used by skeletal greedy CIM, given by turn pairs, is diverse enough that there is no advantage of hybrid methods that rely on score-based edge specification from a restricted set compared to methods that fully specify a skeleton and then rely on turning edges. Computational results regarding $\mathrm{CIM}_{4}$ also suggest that the number of turn pairs make up for a significant part of

![img-1.jpeg](img-1.jpeg)
(A) $p=8, n=10,000, \alpha=0.01$
![img-2.jpeg](img-2.jpeg)
(C) $p=8, n=10,000, \alpha=0.0001$
![img-3.jpeg](img-3.jpeg)
(B) $p=8, n=10,000, \alpha=0.001$
![img-4.jpeg](img-4.jpeg)
(D) $p=8, n=10,000$

Figure 2. Ratio of models recovered versus the expected neighborhood size of the true graph. In Fig. 2a-Fig. 2c we ran PC, MMHC, and skeletal greedy CIM on 100 models. Each model had $p=8$ nodes and the weights of the edges were sampled uniformly in $[-1,-0.25] \cup[0.25,1]$. We used a sample size of $n=10,000$, and varied $\alpha$ in $\{0.01,0.001,0.0001\}$. In Figure 2d we see how GES, GIES, and greedy CIM perfomed on the same data.
the edges of $\mathrm{CIM}_{G}$, but edge pairs make up for a small part of edges of $\mathrm{CIM}_{p}$ (less than a quarter for $p=4$ ). Thus MMHC might be rather restricted when moving between MECs with different skeletons, which is a non-issue for skeletal greedy CIM.

In Figure 2d we compared the purely score-based algorithms. By Proposition 3.2 and Proposition 3.7, greedy CIM can do all moves of GES and GIES, and more. Recall that greedy CIM was implemented using edge pairs and turn pairs, performing only a depth-first search, whereas GES and GIES perform recurrent phased, breadth-first searches. To estimate the extent to which turn pairs and edge pairs generalize the moves of GES and GIES, we also implemented a recurrent phased breadth-first version of greedy CIM. That is, we first only consider edge pairs that increase the number of edges, then the ones that decrease the number of edges, then we enter the turn phase. We then cycle through these three phases, analogous to GIES. We call this algorithm recurrent phased breadth-first greedy CIM. As can be seen in Figure 2d, this version of greedy CIM replicates the output of GIES. On the other hand, GES and GIES perform better than greedy CIM. This suggests

![img-5.jpeg](img-5.jpeg)
(A) The ratio of models recovered.
![img-6.jpeg](img-6.jpeg)
(B) The average SHD between the true model and the result of different algorithms.

Figure 3. A comparison between all algorithms discussed based on 100 simulations. Each model had $p=8$ nodes and the weights of the edges were sampled uniformly in $[-1,-0.25] \cup[0.25,1]$. We used a sample size of $n=10,000$, and $\alpha=0.0001$.
that recurrent phased approaches to optimizing BIC will typically yield better results. Moreover, the fact that recurrent phased breadth-first greedy CIM matches the best performing algorithm (GIES) suggests that characterizing more edges of $\mathrm{CIM}_{p}$ and incorporating them into the implementation of greedy CIM could yield even better performing greedy score-based causal discovery algorithms. The previously mentioned computational results for $\mathrm{CIM}_{4}$ suggest that there is much room for improvement in this direction as the turn pairs and edge pairs make up less than a quarter of the edges for $\mathrm{CIM}_{4}$.

In Figure 3 we give a complete comparison of the recovery ratios of all algorithms discussed as well as the SHD between the result for each algorithm and the true model. Even though greedy CIM has a higher recovery ratio than the PC algorithm and MMHC, the average SHD is higher as well. This indicates that, while greedy CIM typically succeeds in finding the true DAG more often than these algorithms, when it fails to do so it returns a less accurate MEC than the other algorithms. Thus, greedy CIM likely does a move early on from which it cannot move towards the optimal imset, since we do not have access to all edges of $\mathrm{CIM}_{p}$. (Note that, as BIC is linear over $\mathrm{CIM}_{p}$, this would never happen given a complete characterization of the edges of $\mathrm{CIM}_{p}$.) On the other hand, skeletal greedy CIM is one of the top performers in regards to average SHD. As opposed to skeletal greedy CIM, greedy CIM will probably improve if more edges of $\mathrm{CIM}_{p}$ are identified.

# 5. Discussion 

In this paper, we have studied the characteristic imset polytope $\mathrm{CIM}_{p}$ and its faces $\mathrm{CIM}_{G}$. We have shown that most common moves utilized in greedy causal discovery algorithms, such as reversing or adding an edge, correspond to edges of $\mathrm{CIM}_{p}$. Utilizing this, we introduced skeletal greedy CIM (Algorithm 1) and greedy CIM (Algorithm 2). These algorithms are greedy depth-first search edge-walks over the $\mathrm{CIM}_{G}$ and $\mathrm{CIM}_{p}$ polytopes, respectively. Skeletal greedy CIM is a hybrid algorithm that first does CI tests to learn a skeleton $G$, and then passes to

a restricted edge-walk over $\mathrm{CIM}_{G}$, attempting to maximize the BIC by walking along edges labeled by turn pairs or edge pairs. Greedy CIM performs a similar restricted edge-walk over $\mathrm{CIM}_{p}$. Both algorithms could likewise be implemented using any score-equivalent and decomposable score function. We showed that (recurrent phased breadth-first) greedy CIM is a geometric generalization of GES and GIES in the case of purely observational data. Consequently, GES and GIES admit a geometric interpretation as edge-walks along a convex polytope. It further follows that MMHC has a similar interpretation. As greedy SP already has such an interpretation in terms of the DAG associahedron [10] it follows that all greedy algorithms discussed in this paper have a geometric interpretation as an edge-walk along a convex polytope. In this sense, we have observed that greedy causal discovery is geometric.

An implementation of skeletal greedy CIM and greedy CIM is available at [13]. Given data drawn from a joint distribution on 8 variables, these implementations return a graph in approximately 1 and 10 seconds on average, respectively. We believe that a more efficient implementation is possible, but we leave that for future work.

Skeletal greedy CIM was shown to outperform the other hybrid algorithms such as MMHC and greedy SP on simulated Gaussian data. The main difference between these algorithms is that skeletal greedy CIM relies on CI tests to determine the skeleton, while MMHC only utilizes the CI tests to restrict the set of possible skeletons. Thus it is probable that turn pairs capture many edges of $\mathrm{CIM}_{G}$, while turn and edge pairs capture relatively few edges of $\mathrm{CIM}_{p}$. So while skeletal greedy CIM appears to be a near optimal hybrid algorithm given its constraint-based bounds, identifying more edges of $\mathrm{CIM}_{p}$ to extend the moves used by MMHC between skeleta could lead to an algorithm capable of outperforming both skeletal greedy CIM and MMHC. Given that one can use polymake [2, 6] to compute all edges of $\mathrm{CIM}_{4}$, a natural first step would be to try to generalize some of these edges not captured by edge pairs or turn pairs to higher values of $p$.

Finally, recall that GIES first adds in edges without considering the deletion of edges, then deletes edges without considering the addition of edges, then reverses edges, and then cycles through each of these phases. GIES also does a breadthfirst search. Thus, we believe that the depth-first nature of greedy CIM induces a preference on the edges which is avoided by GIES via a breadth-first search. A recurrent phased breadth-first version of greedy CIM was implemented and performed identically, in terms of accuracy, with GIES in our simulations. A natural follow-up question is then: how often, if ever, does recurrent phased breadth-first search greedy CIM utilize the extra moves to which it has access? Presently, what we can surmise is that finding and implementing more edges of the $\mathrm{CIM}_{p}$ polytope could lead to even better greedy causal discovery algorithms than the current front-runners (GIES and recurrent phased breadth-first greedy CIM).

# 6. Acknowledgements 

All three authors were partially supported by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by the Knut and Alice Wallenberg Foundation. Svante Linusson was partially supported by Grant (No. 2018-05218) from Vetenskapsrådet (The Swedish Research Council). Liam Solus was partially supported by Starting Grant (No. 2019-05195) from Vetenskapsrådet (The Swedish

Research Council). The authors thank an anonymous reviewer for helpful suggestions that greatly improved the presentation of the paper.

# Appendix A. Proofs of Theorems in Section 3 

Proof of Proposition 3.2. We have the following equality

$$
c_{\mathcal{G}_{i \leftarrow j}}=c_{\mathcal{G}}+\sum_{S \in \mathcal{A}^{+}} e_{S}-\sum_{S \in \mathcal{A}^{-}} e_{S}
$$

for some $\mathcal{A}^{+}$and $\mathcal{A}^{-}$. We begin by giving a possible description of $\mathcal{A}^{+}$and $\mathcal{A}^{-}$. If we have a set $S$ such that $\{i, j\} \nsubseteq S$, then the graphs induced by $\mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ on $S$ are identical and we can assume that no such $S$ is in either $\mathcal{A}^{+}$or $\mathcal{A}^{-}$. We only changed the edge $i \rightarrow j$. So for any set $S$, the only node that could have become the child of every other node in $S$ upon reversing $i \rightarrow j$ is $i$. Taking this as a definition of $\mathcal{A}^{+}$we get that $\mathcal{A}^{+}$is all sets $S$ such that $\{i, j\} \subseteq S \subseteq \mathrm{pa}_{\mathcal{G}_{i \leftarrow j}}(i) \cup\{i\}$ and $\{i, j\} \subseteq S \nsubseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i\}$. That gives us $\mathcal{A}^{+}=\{S:\{i, j\} \subseteq S \subseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i, j\}\}=\{S \cup\{i, j\}: S \subseteq \mathrm{pa}_{\mathcal{G}}(i)\}$. Similar reasoning gives us $\mathcal{A}^{-}=\{S \cup\{i, j\}: S \subseteq \mathrm{pa}_{\mathcal{G}}(j)\}$. Note that $\mathcal{A}^{+} \cap \mathcal{A}^{-}=$ $\{S \cup\{i, j\}: S \subseteq \mathrm{pa}_{\mathcal{G}}(i) \cap \mathrm{pa}_{\mathcal{G}}(j)\}$.

Let $S_{i}=\operatorname{pa}_{\mathcal{G}}(i)$ and let $S_{j}=\operatorname{pa}_{\mathcal{G}}(j) \backslash\{i\}$. We will now check the conditions in Definition 3.1 with respect to $\left(i, j, S_{i}, S_{j}\right) . \mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ have the same skeleton, say $G$. Conditions (1)-(3) are direct from the definition of characteristic imset as $i$ is the child of every node in $S_{i}=\operatorname{pa}_{\mathcal{G}}(i)$, and similarly with $j$. If $S_{i} \subseteq \operatorname{ne}_{G}(j)$ we have $S_{i} \subseteq \operatorname{pa}_{\mathcal{G}}(j)$, indeed otherwise we would have $k \in S_{i}=\operatorname{pa}_{\mathcal{G}}(i)$ such that $k \in \operatorname{ch}_{\mathcal{G}}(j)$. This gives us the edges $i \rightarrow j \rightarrow k \rightarrow i$ in $\mathcal{G}$, a contradiction as $\mathcal{G}$ is a DAG.

Case I, $S_{i} \subseteq \operatorname{ne}_{G}(j)$ and $S_{j} \subseteq \operatorname{ne}_{G}(i)$ : We have $i \notin S_{i}$. As argued above, if $S_{i} \subseteq \operatorname{ne}_{G}(j)$ and $S_{j} \subseteq \operatorname{ne}_{G}(i)$ we get $S_{i} \subseteq \operatorname{pa}_{\mathcal{G}}(j) \backslash\{i\}=S_{j} \subseteq \operatorname{pa}_{\mathcal{G}}(i)=S_{i}$. In particular $\operatorname{pa}_{\mathcal{G}}(j) \backslash\{i\}=\operatorname{pa}_{\mathcal{G}}(i)$. Thus $\mathcal{G}$ and $\mathcal{G}_{i \leftarrow j}$ are Markov equivalent. This was first proved by Chickering in [3]. From the viewpoint of imsets, we get $\mathcal{A}^{+}=\mathcal{A}^{-}$ and thus $c_{\mathcal{G}}=c_{\mathcal{G}_{i \leftarrow j}}$.

Case II, $S_{i} \nsubseteq \operatorname{ne}_{G}(j)$ or $S_{j} \nsubseteq \operatorname{ne}_{G}(i)$ : Condition (4) in Definition 3.1 holds by assumption. Thus what is left is to check that $\mathcal{S}^{+}=\mathcal{A}^{+} \backslash \mathcal{A}^{-}$and $\mathcal{S}^{-}=\mathcal{A}^{-} \backslash \mathcal{A}^{+}$. Then by our above reasoning we get

$$
\begin{aligned}
\mathcal{A}^{+} \backslash \mathcal{A}^{-} & =\left\{S \cup\{i, j\}: S \subseteq \operatorname{pa}_{\mathcal{G}}(i), S \nsubseteq \operatorname{pa}_{\mathcal{G}}(j)\right\} \\
& =\left\{S \cup\{i, j\}: S \subseteq S_{i}, S \nsubseteq \operatorname{ne}_{G}(j)\right\}=\mathcal{S}^{+}
\end{aligned}
$$

Similar reasoning gives us $\mathcal{S}^{-}=\mathcal{A}^{-} \backslash \mathcal{A}^{+}$.
For the following proofs we will use the following well-known fact.
Lemma A.1. Let $P$ be a 0/1-polytope. If $u$ and $v$ are two vertices of $P$ such that $u$ and $v$ differ by a single value. Then $\operatorname{conv}(u, v)$ is an edge of $P$.

Proof of Theorem 3.4. By definition we have $c_{\mathcal{G}}(\{k, i\})=1$ for all $k \in S_{i}$, thus $S_{i} \subseteq \operatorname{ne}_{G}(i)$ and similar for $S_{j}$. Note that this implies that $\mathcal{S}^{+}$and $\mathcal{S}^{-}$are disjoint. If $S_{i}=S_{j}$ we have that $S_{i}=S_{j} \subseteq \operatorname{ne}_{G}(j)$, and vice versa, thus this is not a turn pair. By symmetry in the definition we get two cases.

Case I, $S_{j} \subsetneq S_{i}$ : If $\left|S_{i}\right|=|\{k\}|=1$ we get that $c_{\mathcal{H}}=c_{\mathcal{G}}+e_{\{i, j, k\}}$, and thus this follows by Lemma A.1. To prove the claim when $\left|S_{i}\right| \geq 2$, it suffices to find a cost vector $w \in \mathbb{R}^{2^{p}-p-1}$ such that $w^{T} x$ is maximized at exactly $c_{\mathcal{G}}$ and $c_{\mathcal{H}}$ over the vertices of $\mathrm{CIM}_{G}$. Since $c_{\mathcal{G}}(\{i, k\})=1$ for all $k \in S_{j}$ we have $S_{i} \subseteq \operatorname{ne}_{G}(i)$. Thus $S_{j} \subseteq S_{i} \subseteq \operatorname{ne}_{G}(i)$ and we get that $\mathcal{S}^{-}=\emptyset$, by definition of $\mathcal{S}^{-}$. Moreover, by (4) in Definition 3.1, $S_{i} \nsubseteq \operatorname{ne}_{G}(j)$. Let $m:=\left|\mathcal{S}^{+}\right|$and define the cost vector $w$ such that for $S \subseteq[p]$, with $|S| \geq 2, w$ satisfies

$$
w(S)= \begin{cases}2 & \text { if } c_{\mathcal{G}}(S)=1 \\ 1 & \text { if } S=S_{i} \cup\{i, j\} \\ \frac{-1}{m-1} & \text { if } S \in \mathcal{S}^{+} \backslash\left\{S_{i} \cup\{i, j\}\right\} \\ -2 & \text { otherwise }\end{cases}
$$

Notice that since $\left|S_{i}\right| \geq 2$ we have $m \geq 2$ so this is indeed well defined. Then we have $w^{T} c_{\mathcal{G}}=w^{T} c_{\mathcal{H}}$ since

$$
\begin{aligned}
w^{T} c_{\mathcal{H}} & =w^{T}\left(c_{\mathcal{G}}+\sum_{S \in \mathcal{S}^{+}} e_{S}-\sum_{S \in \mathcal{S}^{-}} e_{S}\right) \\
& =w^{T} c_{\mathcal{G}}+w\left(S_{i} \cup\{i, j\}\right)(1)+\sum_{S \in \mathcal{S}^{+} \backslash\left\{S_{i} \cup\{i, j\}\right\}} w(S)=w^{T} c_{\mathcal{G}}
\end{aligned}
$$

It then remains to check that $w^{T} c_{\mathcal{D}}<w^{T} c_{\mathcal{G}}$ for any DAG $\mathcal{D}$ with skeleton $G$ and $\mathcal{D}$ not Markov equivalent to $\mathcal{G}$ or $\mathcal{H}$.

Let us denote $\mathcal{A}^{+}:=\{S: w(S)=2\}$ and $\mathcal{A}^{-}:=\{S: w(S)=-2\}$. For all $0 / 1$-vectors $v$ we have

$$
\begin{aligned}
w^{T} v & =w^{T} \sum_{S \in \mathcal{A}^{+}: v(S)=1} e_{S}+w^{T} \sum_{S \in \mathcal{A}^{-}: v(S)=1} e_{S}+w^{T} \sum_{S \in \mathcal{S}^{+}: v(S)=1} e_{S} \\
& =2\left|\left\{S \in \mathcal{A}^{+}: v(S)=1\right\}\right|-2\left|\left\{S \in \mathcal{A}^{-}: v(S)=1\right\}\right|+w^{T} \sum_{S \in \mathcal{S}^{+}: v(S)=1} e_{S}
\end{aligned}
$$

Noting that $c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=1$ for all $S \in \mathcal{A}^{+}, c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=0$ for all $S \in \mathcal{A}^{-}$ and that $-1 \leq w^{T} \sum_{S \in \mathcal{S}^{+}: v(S)=1} e_{S} \leq 1$ we immediately get that $w^{T} v<w^{T} c_{\mathcal{G}}$ whenever we have that $\left\{S \in \mathcal{A}^{+}: v(S)=1\right\} \neq \mathcal{A}^{+}$or $\left\{S \in \mathcal{A}^{-}: v(S)=0\right\} \neq \mathcal{A}^{-}$. Then as $\{S \subseteq[p]:|S| \geq 2\}=\mathcal{A}^{+} \cup \mathcal{A}^{-} \cup \mathcal{S}^{+}$we can assume that $c_{\mathcal{D}}(S)=c_{\mathcal{G}}(S)$ whenever $S \notin \mathcal{S}^{+}$. In particular $\mathcal{D}$ must have the same skeleton as $\mathcal{G}$ and $\mathcal{H}$.

Since $\mathcal{D}$ was assumed to not be Markov equivalent to $\mathcal{G}$ we have the following cases:
(1) $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=0$ and for some set $S \in \mathcal{S}^{+} \backslash\left\{S_{i} \cup\{i, j\}\right\}$ we have $c_{\mathcal{D}}(S)=1$, or

(2) $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$.

In case (1) it follows immediately that $w^{T} c_{\mathcal{D}} \leq w^{T} c_{\mathcal{G}}+\frac{-1}{m-1}<w^{T} c_{\mathcal{G}}$.
As for case (2), by definition of the characteristic imset we have a node $n$ such that $x \rightarrow n$ in $\mathcal{D}$ for all $x \in\left(S_{i} \cup\{i, j\}\right) \backslash\{n\}$. If $n=j$ we get $S_{i} \subseteq \operatorname{ne}_{G}(j)$, but this cannot happen by (4) in Definition 3.1. If $n=i$ we get that $c_{\mathcal{D}}(S)=1$ for all $S \in \mathcal{S}^{+}$, and thus $\mathcal{D}$ is Markov equivalent to $\mathcal{H}$. Thus the only case left is that $n \in S_{i}$.

As $S_{i} \nsubseteq \operatorname{ne}_{G}(j)$ we have $S_{i} \cup\{i, j\} \in \mathcal{S}^{+}$. Then, as $j \rightarrow n$ in $\mathcal{D}$, there must exist a node $k \notin\{i, j, n\}$ such that $k$ is not a neighbour of $j$ in $G$. Since $\{j, k\} \subseteq$ $S_{i} \cup\{i, j\} \subseteq \operatorname{pa}_{\mathcal{D}}(n) \cup\{n\}$ we get $c_{\mathcal{D}}(\{j, n, k\})=1$. As $i \notin\{j, n, k\},\{j, n, k\} \notin \mathcal{S}^{+}$. Thus we must have that $1=c_{\mathcal{D}}(\{j, n, k\})=c_{\mathcal{G}}(\{j, n, k\})=c_{\mathcal{H}}(\{j, n, k\})$. That is $\{j, n, k\}$ is a v-structure in $\mathcal{D}, \mathcal{G}$ and $\mathcal{H}$. We have that $c_{\mathcal{G}}(\{i, j, k\})=0$ since $\{i, j, k\} \in \mathcal{S}^{+}$. Thus, since $\mathcal{G}$ is acyclic, it follows that $i \rightarrow n$ in $\mathcal{G}$ as well. In the terminology used in [1], $i \rightarrow n$ will be strongly protected in $\mathcal{G}$. Hence $n$ is a child of $i, j$ and $k$ in $\mathcal{G}$, so $c_{\mathcal{G}}(\{i, j, n, k\})=1$. But $\{i, j, n, k\} \in \mathcal{S}^{+}$, a contradiction.

Case II, $S_{i} \nsubseteq S_{j}$ and $S_{j} \nsubseteq S_{i}$ : Here we will use a different cost vector. Let $m^{+}:=\left|\mathcal{S}^{+}\right|$and $m^{-}:=\left|\mathcal{S}^{-}\right|$. If $m^{+}, m^{-} \geq 2$ define

$$
w(S)= \begin{cases}5 & \text { if } c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=1 \\ 2 & \text { if } S=S_{i} \cup\{i, j\} \text { or } S=S_{j} \cup\{i, j\} \\ \frac{-1}{m^{+}-1} & \text { if } S \in \mathcal{S}^{+} \backslash\left\{S_{i} \cup\{i, j\}\right\} \\ \frac{-1}{m^{-}-1} & \text { if } S \in \mathcal{S}^{-} \backslash\left\{S_{j} \cup\{i, j\}\right\} \\ -5 & \text { if } c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=0\end{cases}
$$

If $\left|\mathcal{S}^{+}\right|=1$ we have that $\mathcal{S}^{+}=\left\{S_{i} \cup\{i, j\}\right\}$, and thus we let $w\left(S_{i} \cup\{i, j\}\right)=1$. Likewise, if $\left|\mathcal{S}^{-}\right|=1$ we have that $\mathcal{S}^{-}=\left\{S_{j} \cup\{i, j\}\right\}$, and we let $w\left(S_{j} \cup\{i, j\}\right)=1$. Otherwise let $w$ be as above. Thus, by definition of $w$, we have $\sum_{S \in \mathcal{S}^{+}} w(S)=$ $\sum_{S \in \mathcal{S}^{-}} w(S)=1$. To see $w^{T} c_{\mathcal{H}}=w^{T} c_{\mathcal{G}}$, note that

$$
\begin{aligned}
w^{T} c_{\mathcal{H}}-w^{T} c_{\mathcal{G}} & =w^{T}\left(c_{\mathcal{G}}+\sum_{S \in \mathcal{S}^{+}} e_{S}-\sum_{S \in \mathcal{S}^{-}} e_{S}\right)-w^{T} c_{\mathcal{G}} \\
& =\sum_{S \in \mathcal{S}^{+} \backslash \mathcal{S}^{-}} w(S)-\sum_{S \in S \in \mathcal{S}^{-} \backslash \mathcal{S}^{+}} w(S)=0
\end{aligned}
$$

So left to show is that for any $\mathrm{DAG} \mathcal{D}$ with skeleton $G$ we have $w^{T} c_{\mathcal{D}}<w^{T} c_{\mathcal{G}}$ if $c_{\mathcal{D}}$ is neither $c_{\mathcal{G}}$ or $c_{\mathcal{H}}$.

As in case I we let $\mathcal{A}^{+}:=\{S: w(S)=5\}=\left\{S: c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=1\right\}$ and $\mathcal{A}^{-}:=\{S: w(S)=-5\}=\left\{S: c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)=0\right\}$. As in case I we have for any $0 / 1$ vector $v$

$$
\begin{aligned}
w^{T} v= & 5\left|\left\{S \in \mathcal{A}^{+}: v(S)=1\right\}\right|-5\left|\left\{S \in \mathcal{A}^{-}: v(S)=1\right\}\right| \\
& +w^{T} \sum_{S \in \mathcal{S}^{+}: v(S)=1} e_{S}+w^{T} \sum_{S \in \mathcal{S}^{-}: v(S)=1} e_{S}
\end{aligned}
$$

We also have that $-1 \leq w^{T} \sum_{S \in \mathcal{S}^{+}: v(S)=1} e_{S} \leq 2$ and $-1 \leq w^{T} \sum_{S \in \mathcal{S}^{-}: v(S)=1} e_{S} \leq$ 2. We immediately get that $w^{T} v<w^{T} c_{\mathcal{G}}$ whenever we have that $\left\{S \in \mathcal{A}^{+}: v(S)=1\right\} \neq$ $\mathcal{A}^{+}$or $\left\{S \in \mathcal{A}^{-}: v(S)=0\right\} \neq \mathcal{A}^{-}$. Thus we can assume that $c_{\mathcal{D}}(S)=c_{\mathcal{G}}(S)$ whenever $c_{\mathcal{G}}(S)=c_{\mathcal{H}}(S)$.

If $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=0$ then it follows that $w^{T} c_{\mathcal{D}} \leq 5\left|\mathcal{A}^{+}\right|<$ $5\left|\mathcal{A}^{+}\right|+1=c_{\mathcal{G}}$. Thus for $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$ to be true we must have $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$ or $c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=1$. By symmetry we can assume $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$.

Thus there exists $n_{i} \in S_{i}$ such that $S_{i} \cup\{i, j\} \subseteq \mathrm{pa}_{\mathcal{D}}\left(n_{i}\right) \cup\left\{n_{i}\right\}$. We cannot have $n_{i}=j$ as that would give us $S_{i} \subseteq \operatorname{ne}_{G}(j)$, and by the same reasoning there must exist a node $k_{i} \in S_{i} \backslash \operatorname{ne}_{G}(j)$. Then we have two cases $n_{i} \neq i$ and $n_{i}=i$.

If $n_{i} \neq i$ we have that $c_{\mathcal{D}}\left(\left\{n_{i}, k_{i}, j\right\}\right)=1$. As $\left\{n_{i}, k_{i}, j\right\} \notin \mathcal{S}^{+} \cup \mathcal{S}^{-}$we get $c_{\mathcal{D}}\left(\left\{n_{i}, k_{i}, j\right\}\right)=c_{\mathcal{G}}\left(\left\{n_{i}, k_{i}, j\right\}\right)=c_{\mathcal{H}}\left(\left\{n_{i}, k_{i}, j\right\}\right)=1$. Then by acyclicity we get $c_{\mathcal{G}}\left(\left\{n_{i}, k_{i}, i, j\right\}\right)=1$. But as $\left\{n_{i}, k_{i}, i, j\right\} \in \mathcal{S}^{+} \backslash \mathcal{S}^{-}$we get $c_{\mathcal{G}}\left(\left\{n_{i}, k_{i}, i, j\right\}\right)=0$, a contradiction.

Thus $n_{i}=i$. Then, by definition, it follows that $c_{\mathcal{D}}(S)=1$ for all $S \in \mathcal{S}^{+}$. If $c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=1$ we can in the same way argue that the corresponding $n_{j}=j$ and thus that $c_{\mathcal{D}}(S)=1$ for all $S \in \mathcal{S}^{-}$. More specifically we get that we have the following two graphs induced in $\mathcal{D}, i \rightarrow j \leftarrow k_{j}$ and $k_{i} \rightarrow i \leftarrow j$. A contradiction, thus if $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$ we have $c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=0$.

In conclusion, we assumed that $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$ and deduced that we cannot have both $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$ and $c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=1$. With that assumption it also followed that if $c_{\mathcal{D}}\left(S_{i} \cup\{i, j\}\right)=1$ then $c_{\mathcal{D}}(S)=c_{\mathcal{G}}(S)$ for all $S$. By symmetry, if $c_{\mathcal{D}}\left(S_{j} \cup\{i, j\}\right)=1$ then $c_{\mathcal{D}}(S)=c_{\mathcal{H}}(S)$ for all $S$. The result follows.

Proof of Proposition 3.7. We begin to characterize all sets $S$ such that $c_{\mathcal{G}}(S) \neq$ $c_{\mathcal{G}_{+i \leftarrow j}}(S)$. For any $S \subseteq[p]$ and $k \neq i$ we have that $k \in S \subseteq \mathrm{pa}_{\mathcal{G}}(k) \cup\{k\}$ if and only if $k \in S \subseteq \mathrm{pa}_{\mathcal{G}_{+i \leftarrow j}}(k) \cup\{k\}$. This is because $\mathrm{pa}_{\mathcal{G}}(k)=\mathrm{pa}_{\mathcal{G}_{+i \leftarrow j}}(k)$ for all such $k$. As the value of $c_{\mathcal{G}}(S)$ and $c_{\mathcal{G}_{+i \leftarrow j}}(S)$ is determined by this property the only case where we can have $c_{\mathcal{G}}(S) \neq c_{\mathcal{G}_{+i \leftarrow j}}(S)$ is for sets such that $i \in S \nsubseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i\}$ or $i \in S \subseteq \mathrm{pa}_{\mathcal{G}_{+i \leftarrow j}}(i) \cup\{i\}$.

Moreover, for any $S$ such that $\{i, j\} \nsubseteq S$ we have that the induced subgraphs of $\mathcal{G}$ and $\mathcal{G}_{+i \leftarrow j}$ are identical. Thus $c_{\mathcal{G}}(S)=c_{\mathcal{G}_{+i \leftarrow j}}(S)$ for all such $S$. This together with the fact that $\mathrm{pa}_{\mathcal{G}}(i) \cup\{j\}=\mathrm{pa}_{\mathcal{G}_{+i \leftarrow j}}(i)$ tells us that the only sets of interest are $\{i, j\} \subseteq S \subseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i, j\}$.

We claim that $c_{\mathcal{G}_{+i \leftarrow j}}(S)=1$ and $c_{\mathcal{G}}(S)=0$ for all $S$ such that $\{i, j\} \subseteq S \subseteq$ $\mathrm{pa}_{\mathcal{G}}(i) \cup\{i, j\}$, making this an edge pair with respect to $\left(i, j, S^{*}\right)$ where $S^{*}=\mathrm{pa}_{\mathcal{G}}(i)$. It follows that $c_{\mathcal{G}_{+i \leftarrow j}}(S)=1$ for all such $S$ since $i \in S \subseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i, j\}=$ $\mathrm{pa}_{\mathcal{G}_{+i \leftarrow j}}(i) \cup\{i\}$. Suppose $S$ is such that $\{i, j\} \subseteq S \subseteq \mathrm{pa}_{\mathcal{G}}(i) \cup\{i, j\}$. Any $k \in$ $S \backslash\{i, j\}$ must be a parent of $i$ in $\mathcal{G}$, since we cannot have $i \in S \subseteq \mathrm{pa}_{\mathcal{G}}(k) \cup\{k\}$. As $i$ and $j$ are not adjacent neither can be the parent of the other. Hence no node in $S$ can be the parent of all other nodes in $S$, and it follows that $c_{\mathcal{G}}(S)=0$. Condition (1) in Definition 3.6 follows since $i$ was not a neighbor of $j$ in $\mathcal{G}$, and condition (2) follows since we choose $S^{*}$ to be $\mathrm{pa}_{\mathcal{G}}(i)$.

Proof of Theorem 3.9. If $\left|S^{*}\right|=0$ we get $\left|\mathcal{S}_{+i \leftarrow j}\right|=1$, thus this follows by Lemma A.1. Hence we can assume that $\left|S^{*}\right|>0$. We partition the elements in $S^{*}$ based on if they are adjacent to $j$ in $\mathcal{G}$ or not. So let $X=\left\{x \in S^{*}: c_{\mathcal{G}}(\{x, j\})=0\right\}$ and $Y=\left\{y \in S^{*}: c_{\mathcal{G}}(\{y, j\})=1\right\}$. Define $s:=|X|$ and $t:=|Y|$. We treat the cases when $X \neq \emptyset$ and $X=\emptyset$ separately.
Case I, $X \neq \emptyset$ : Let $M:=2^{s+t}-(s+t+1)$ and notice that $\left|\left\{S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4\right\}\right|=$ $M$. If $M=0$ we get $s=1$ and $t=0$ as $|X|=s$. In this case $c_{\mathcal{G}}$ and $c_{\mathcal{H}}$ only differ in the coordinates $\{i, j\}$ and $\{i, j\} \cup X$. We claim that $c_{\mathcal{G}}+e_{\{i, j\} \cup X}$ is not a valid imset as $\{i, j\} \cup X$ is not connected in the skeleton of $\mathcal{G}$. Hence $c_{\mathcal{G}}(S), c_{\mathcal{H}}(S)$ and

at most one more vertex in $\mathrm{CIM}_{p}$ form a face of $\mathrm{CIM}_{p}$. It follows that $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge in this case.

If $M>0$ we can define the following objective function $w$ to prove that $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge of $\mathrm{CIM}_{p}$ :

$$
w(S)= \begin{cases}t+2 & \text { if } c_{\mathcal{G}}(S)=1 \\ -1 & \text { if } S=\{i, j\} \\ -1 & \text { if } S=\{i, j, y\}, \text { some } y \in Y \\ \frac{1}{2}\left(t+\frac{1}{2}\right) & \text { if } S=\{i, j, x\}, \text { some } x \in X \\ \frac{1}{2 M} & \text { if } S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4 \\ -(t+2) & \text { otherwise }\end{cases}
$$

The negative weights for $S \in \mathcal{S}_{+i \leftarrow j}$ sum to $-(t+1)$ and the positive to $t+1$. Since the imsets differ exactly on $\mathcal{S}_{+i \leftarrow j}$, for which $w$ sum to 0 , we get $w^{T} c_{\mathcal{H}}=w^{T} c_{\mathcal{G}}$. Assume we have a DAG $\mathcal{D}$ such that $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$. Then it must be that $c_{\mathcal{D}}(S)=1$ if $c_{\mathcal{G}}(S)=1$ and $c_{\mathcal{D}}(S)=0$ if $c_{\mathcal{H}}(S)=0$. If $c_{\mathcal{D}}(S)=0$ for all $S \in \mathcal{S}_{+i \leftarrow j}$ then $c_{\mathcal{D}}=c_{\mathcal{G}}$, so we can assume that is not the case. Such a DAG $\mathcal{D}$ must thus pick up some of the positive weights in $\mathcal{S}_{+i \leftarrow j}$. There are two possibilities to consider. First, if $c_{\mathcal{D}}(\{i, j, x\})=1$ for some $x \in X$, then, by definition of $c_{\mathcal{D}}, \mathcal{D}$ must have v-structure $x \rightarrow i \leftarrow j$, since we know there is no edge between $x$ and $j$. Therefore we must have $c_{\mathcal{D}}(\{i, j\})=1$, and it follows that $c_{\mathcal{D}}(\{i, j, y\})=1$, for all $y \in Y$, since $y$ is adjacent to both $i$ and $j$. Thus $w^{T} c_{\mathcal{D}}$ picks up all the negative weights in $\mathcal{S}_{+i \leftarrow j}$. To then get $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$, we must have $c_{\mathcal{D}}(S)=c_{\mathcal{H}}(S)$ for all $S$. Therefore, $\mathcal{D}$ is Markov equivalent to $\mathcal{H}$ by Theorem 2.2.

Second, if $c_{\mathcal{D}}(\{i, j, x\})=0$ for all $x \in X$, but $c_{\mathcal{D}}(S)=1$, for some $S \in$ $\mathcal{S}_{+i \leftarrow j},|S| \geq 4$, then by definition there exists $k \in S$ with $S \subseteq \mathrm{pa}_{\mathcal{D}}(k) \cup\{k\}$. If $k \in\{i, j\}$ we immediately get $c_{\mathcal{D}}(\{i, j\})=1$. Otherwise we have $c_{\mathcal{D}}(\{i, j, k\})=1$, and since there is no edge between $j$ and elements in $X$ we know that $k \in Y$. In either case $w^{T} c_{\mathcal{D}}$ picks up a -1 . The sum of the positive weights $w(S)$ for $S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4$ is only $\frac{1}{2} / 2$ and we cannot have $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$.
Case II, $X=\emptyset$ : If $M=0$, either $s+t=1$ or $s+t=0$. The latter implies $S^{*}=\emptyset$, which is dealt with above. For the former, we get $s=0$ and $t=1$. We claim that $c_{\mathcal{G}}+e_{\{i, j\}}$ is not a valid characteristic imset for any DAG, since $\{i, j\} \cup Y$ is complete in the skeleton of $\mathcal{H}$. Similar to Case I it follows $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge.

If $M>0$ we now use the following objective function $w$ in order to prove that $\operatorname{conv}\left(c_{\mathcal{G}}, c_{\mathcal{H}}\right)$ is an edge of $\mathrm{CIM}_{p}$ :

$$
w(S)= \begin{cases}t+1 & \text { if } c_{\mathcal{G}}(S)=1 \\ t-\frac{1}{2} & \text { if } S=\{i, j\} \\ -1 & \text { if } S=\{i, j, y\}, \text { some } y \in Y \\ \frac{1}{2 M} & \text { if } S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4 \\ -(t+1) & \text { otherwise }\end{cases}
$$

Here $s=0$, so $M=2^{t}-t-1$. The reasoning is very similar to Case I. The negative weights for $S \in \mathcal{S}_{+i \leftarrow j}$ sum to $-t$ and the positive to $t$. Thus, $w^{T} c_{\mathcal{H}}=w^{T} c_{\mathcal{G}}$, and again if another DAG $\mathcal{D}$ were to have $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$, then it must have $c_{\mathcal{D}}(S)=1$ if $c_{\mathcal{G}}(S)=1$ and $c_{\mathcal{D}}(S)=0$ if $c_{\mathcal{H}}(S)=0$. There are two possibilities to consider. First, if $c_{\mathcal{D}}(\{i, j\})=1$, then $\mathcal{D}$ has triangles on every $\{i, j, y\}$ and therefore $c_{\mathcal{D}}(\{i, j, y\})=1$, for all $y \in Y$. Thus $\mathcal{D}$ picks up all the $-t$ negative weights and

```
Algorithm 3 Edge phase
Input: An imset \(c_{\mathcal{G}}\) corresponding to a DAG \(\mathcal{G}\). Data D.
Output: A characteristic imset \(c_{\mathcal{G}}\) where \(\mathcal{G}\) is a DAG.
    Let \(G\) be the skeleton of \(\mathcal{G}\)
    check \(\leftarrow\) true
    while check do
        check \(\leftarrow\) false
        for \(i, j \in[p]\) do
            for \(S^{*} \subseteq \operatorname{ne}_{G}(i)\) do
                if We have a DAG \(\mathcal{H}\) such that \(\{\mathcal{G}, \mathcal{H}\}\) is an edge pair with respect to
    \(\left(i, j, S^{*}\right)\) then
        if \(\operatorname{BIC}(\mathcal{H}, \mathbf{D})>\operatorname{BIC}(\mathcal{G}, \mathbf{D})\) then
                \(c_{\mathcal{G}} \leftarrow c_{\mathcal{H}}\)
                Let \(G\) be the skeleton of \(\mathcal{G}\)
                check \(\leftarrow\) true
                break
                end if
            end if
            end for
        end for
    end while
    return \(c_{\mathcal{D}}\)
```

the only possibility is $c_{\mathcal{D}}=c_{\mathcal{H}}$. The second possibility is that $c_{\mathcal{D}}(\{i, j\})=0$ but $c_{\mathcal{D}}(S)=1$, for some $S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4$, then by definition there exists $k \in S$ with $S \subseteq \operatorname{pa}_{\mathcal{D}}(k) \cup\{k\}$. As $i$ and $j$ are not adjacent we get $k \notin\{i, j\}$. This implies that $c_{\mathcal{D}}(\{i, j, k\})=1$, for $k \in Y$, which gives a -1 in $w^{T} c_{\mathcal{D}}$. The sum of the positive weights $w(S)$ for $S \in \mathcal{S}_{+i \leftarrow j},|S| \geq 4$ is $1 / 2$ and thus we cannot have $w^{T} c_{\mathcal{D}} \geq w^{T} c_{\mathcal{G}}$.

# Appendix B. The Turn Phase and the Edge Phase Algorithms 

Here we present the pseudocode for the edge phase and turn phase used in Algorithm 1 and Algorithm 2. The edge phase and turn phase algorithms are presented in Algorithm 3 and Algorithm 4, respectively.

Email address, Svante Linusson: linusson@math.kth.se
Email address, Petter Restadh: petterre@kth.se
Email address, Liam Solus: solus@kth.se
Department of Mathematics, KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden

```
Algorithm 4 Turn phase
Input: An imset \(c_{\mathcal{G}}\) corresponding to a DAG \(\mathcal{G}\). Data D.
Output: A characteristic imset \(c_{\mathcal{G}}\) where \(\mathcal{G}\) is a DAG.
    \(c_{\mathcal{D}} \leftarrow c_{\mathcal{G}}\)
    Let \(G\) be the skeleton of \(\mathcal{G}\)
    check \(\leftarrow\) true
    while check do
        check \(\leftarrow\) false
        for \(i, j \in[p]\) do
            for \(S_{i} \subseteq \operatorname{ne}_{G}(i)\) and \(S_{j} \subseteq \operatorname{ne}_{G}(j)\) do
                if We have a DAG \(\mathcal{H}\) such that \(\{\mathcal{D}, \mathcal{H}\}\) is an turn pair with respect
    to \(\left(i, j, S_{i}, S_{j}\right)\) then
        if \(\operatorname{BIC}(\mathcal{H}, \mathbf{D})>\operatorname{BIC}(\mathcal{D}, \mathbf{D})\) then
                \(c_{\mathcal{D}} \leftarrow c_{\mathcal{H}}\)
                check \(\leftarrow\) true
            end if
            end if
            end for
        end for
    end while
    return \(c_{\mathcal{G}}\)
```