# DECOMPOSABLE CONTEXT-SPECIFIC MODELS 

YULIA ALEXANDR, ELIANA DUARTE, AND JULIAN VILL


#### Abstract

We introduce a family of discrete context-specific models, which we call decomposable. We construct this family from the subclass of staged tree models known as CStree models. We give an algebraic and combinatorial characterization of all context-specific independence relations that hold in a decomposable context-specific model, which yields a Markov basis. We prove that a directed version of the moralization operation applied to the graphical representation of a context-specific model does not affect the implied independence relations, thus affirming that these models are algebraically described by a finite collection of decomposable graphical models. More generally, we establish that several algebraic, combinatorial, and geometric properties of decomposable context-specific models generalize those of decomposable graphical models to the context-specific setting.


## 1. INTRODUCTION

A discrete graphical model $\mathcal{M}(G)$ associated to a graph $G$ with $p$ nodes is a set of joint probability distributions for a vector of discrete random variables $\left(X_{1}, \ldots, X_{p}\right)$. The distributions in $\mathcal{M}(G)$ satisfy conditional independence (CI) relations according to the nonadjacencies of the graph $G$. The type of graph used to encode CI relations is typically a directed acyclic graph (DAG) or an undirected graph (UG), although other kinds of graphs are possible [Lau96].

Graphical models are widely used in several fields of science, such as artificial intelligence, biology, and epidemiology [KF09, Pea88, MDLW18]. However, in some applications it is useful to consider models that encode a finer form of independence. Context-specific independence (CSI) is a generalization of conditional independence where the conditional independence between the random variables only holds for particular outcomes of the variables in the conditioning set. The classical graphical models based on DAGs or UGs are no longer able to capture these more refined relations. Several extended graphical representations of CSI models have been proposed in the literature, [BFGK96, PZ03, CHM97, PNKC15, SA08]. Apart from its usage to encode model assumptions more accurately, context-specific independence is also important in the study of structural causal models because the presence of more refined independence can improve the identifiability of causal links [THK19].

A graphical model $\mathcal{M}(G)$ associated to an undirected graph $G$ is called decomposable if $G$ is chordal. Decomposable graphical models play a prominent role among graphical models because they exhibit optimal properties for probabilistic inference [KF09, Ch. 9]. There are several characterizations of decomposable models in terms of their algebraic, combinatorial, and geometric properties [GMS06, Lau96, GHKM01, DS23]. In this article we generalize this class of models to the context-specific setting, by defining decomposable context-specific models (see Section 3) and prove that they mirror many of the properties that characterize

[^0]
[^0]:    2020 Mathematics Subject Classification. 62R01, 62A09, 13P10, 13P25.
    Key words and phrases. decomposable models, context-specific independence, Bayesian network, directed acyclic graph, toric ideal, algebraic statistics, probability trees.

decomposable graphical models. For brevity, we will refer to these models as decomposable CSmodels. These models will be constructed from a subclass of staged tree models, first introduced in [SA08]. Staged tree models are a very general class of discrete (categorical) multivariate statistical models whose applications, causal interpretation, and learning is a topic of interest in recent statistical literature [LV22, LV23, GBRS18a, CLRV22]. The distributions that belong to a staged tree model $\mathcal{M}(\mathcal{T})$ are determined by a directed tree $\mathcal{T}$. The inner nodes of the tree are partitioned into sets called stages, and the leaves correspond to the state space of the model. The key feature of the stages is that they efficiently encode context-specific independence statements. In particular, every discrete DAG model can be represented using a staged tree model because any conditional independence statement is the union of several context-specific independence statements.

Previous work on context-specific versions of decomposable models defines them by associating labels to the edges of a decomposable undirected graph and preserving the properties such as perfect elimination ordering and clique factorization [JGR ${ }^{+} 17$, Cor03, NPKC14]. Our approach here is different in that we define decomposable CSmodels to be staged tree models that satisfy two conditions. The first one is that the staged tree is balanced (Section 2.6), this property implies that the model is log-linear; the second one is that the staged tree is a CStree (Section 2.4, [DS22]), this means that the stages satisfy additional properties which imply that the context-specific independence statements that hold for the model can be represented using a collection of DAGs. Thus each decomposable CSmodel is represented by a CStree.

Similar to discrete DAG models, there are two ways to define a CStree model $\mathcal{M}(\mathcal{T})$, associated to the CStree $\mathcal{T}$. The first approach uses a recursive factorization property according to $\mathcal{T}$, while the second one uses the local CSI relations implied by $\mathcal{T}$. From an algebrogeometric point of view, the recursive factorization property is a polynomial parametrization of $\mathcal{M}(\mathcal{T})$, while the polynomials associated to the local CSI statements in $\mathcal{T}$ define the model $\mathcal{M}(\mathcal{T})$ implicitly. An important open problem that arises in the study of context-specific models is characterizing the set of all CSI statements implied by the local CSI statements defining the model [BFGK96, $\mathrm{CHK}^{+} 16$ ]. Such a problem is especially amenable to algebraic techniques because any CSI relation that holds in the model can be represented by a collection of polynomials. Algebraically, this problem can be solved by finding a prime polynomial ideal that defines $\mathcal{M}(\mathcal{T})$ implicitly [GSS05]. Moreover, for log-linear models, the generators of the ideal that defines $\mathcal{M}(\mathcal{T})$ form a Markov basis [DS98]. Our first main theorem is an algebraic characterization of the distributions that belong to a decomposable CSmodel. This theorem is similar to the Hammersley-Clifford theorem for undirected graphical models and its generalization [GMS06, Theorem 4.2].
Theorem 1.1 (Context-specific Hammersley-Clifford). A distribution $f$ factorizes according to $\mathcal{T}$ if and only if the polynomials associated to saturated CSI statements in $\mathcal{T}$ vanish at $f$. Moreover, the polynomials associated to the saturated CSI statements of a decomposable CSmodel form its Markov basis.

Every decomposable CSmodel $\mathcal{M}(\mathcal{T})$ is a CStree model, therefore it can be represented by a collection of minimal context DAGs. We also prove that the saturated CSI statements (i.e. statements that involve all of the variables in the DAG) in Theorem 1.1 are obtained as the union of saturated $d$-separation statements that hold in each of the minimal context DAGs that represent the model $\mathcal{M}(\mathcal{T})$ (Corollary 5.5). As a consequence of our algebraic characterization of decomposable CSmodels, we obtain the next two theorems.

The directed moralization of a DAG is constructed by moralizing the DAG but keeping all edges directed and directing the new edges (see Definition 5.9).

Theorem 1.2. In a decomposable CSmodel, the directed moralizations of the minimal context DAGs imply the same CSI statements as the model itself. In particular, one can apply the directed moralization operation until all context DAGs are perfect.

Theorem 1.3. Every decomposable CSmodel is an intersection of a finite number of decomposable DAG models.

Our work also contributes to understanding the set of CSI statements that hold for certain context-specific models known as LDAGs [PNKC15]. Briefly, an LDAG is a context-specific model represented by a DAG with edge labels, these labels encode the extra CSI relations that hold for the model. Every CStree is an LDAG, and every LDAG is a staged tree [DS22]. Whenever the LDAG is represented by a balanced CStree, Theorem 1.1 gives a complete characterization of the CSI statements that hold for the LDAG. In general, however, describing all CSI statements that hold for LDAGs is coNP-hard [CHK+16]. The decomposable models studied in [JGR+17, Cor03, NPKC14] are defined in a similar fashion as the LDAGs, except their starting point is a decomposable undirected graph. We leave it as a direction for future research to establish the relation between these context specific decomposable models and the decomposable CSmodels we define.

This paper is organized as follows. In Section 2 we present the necessary background on DAG models, staged tree models and CStree models. Decomposable CSmodels are defined in Section 3 where we illustrate the nature of CStrees and decomposable CSmodels by presenting a classification of all CStree models in three random variables. A highlight from this section is Theorem 3.2, which states that if the number $p$ of random variables equals 3 then $\mathcal{M}(\mathcal{T})$ is a decomposable CSmodel if and only if all of its minimal context DAGs are perfect. This is no longer true for $p=4$ by Example 3.6. In Section 4, we establish several combinatorial properties for balanced CStrees. Finally, Section 5 contains the proofs of our main results.

We assume the reader has some familiarity with polynomial ideals at the level of [CLO15]. Although we introduce the basics of graphical models, we refer the reader to [Lau96, Ch. 3,4], [KF09, Ch. 3,4,5], [MDLW18, Ch. 1,2,3] for a more detailed presentation. For a unified algebraic statistics perspective we suggest the book by Sullivant [Sul18, Ch.013]. Our methods rely heavily on properties of staged tree models. The reader may refer to [CGS18] for a comprehensive introduction to this class of models.

# 2. Preliminaries 

A discrete statistical model is a subset of the probability simplex. We consider models that are algebraic varieties intersected with the simplex. We are interested in finding their defining equations. We use the combinatorial properties of the equations to gain insight into the statistical properties of the model.
2.1. Notation. For any natural number $d$ we define $[d]:=\{1,2, \ldots, d\}$. Consider a vector of discrete random variables $X_{[p]}=\left(X_{1}, \ldots, X_{p}\right)$ where $p \in \mathbb{N}$ and for each $i \in[p], d_{i} \in \mathbb{N}$, $\left[d_{i}\right]$ is the state space of $X_{i}$ and $\mathcal{R}=\prod_{i \in[p]}\left[d_{i}\right]$ is the state space of $X_{[p]}$. Elements in $\mathcal{R}$ are sequences $\mathbf{x}=\left(x_{1}, \ldots, x_{p}\right)=x_{1} \cdots x_{p}$ where $x_{k} \in\left[d_{k}\right]$ for every $k \in[p]$. For $A \subseteq[p]$, $X_{A}$ is a subvector of discrete random variables with indices in $A$, and $\mathcal{R}_{A}=\prod_{i \in A}\left[d_{i}\right]$ is

the state space of $X_{A}$. We also use the bold notation $\mathbf{x}$ or $\mathbf{y}$ to denote elements in any marginal space $\mathcal{R}_{A}$ to avoid the excessive use of subscripts. At times it is useful to recall which marginal space the outcome belongs to, in this case we write $\mathbf{x}_{A}$ or $\mathbf{y}_{A}$ for elements in $\mathcal{R}_{A}$. We shall use the three notations $\mathbf{x},\left(x_{1}, \ldots, x_{p}\right)$, or $x_{1} \cdots x_{p}$ throughout this article depending on whether it is necessary to emphasize the outcomes $x_{i} \in \mathcal{R}_{\{i\}}$ or not. Whenever $\mathbf{x}=\left(x_{1}, \ldots, x_{p}\right) \in \mathcal{R}$, the element $\mathbf{x}_{A}$ is the subvector $\left(x_{i}\right)_{i \in A}$ of $\mathbf{x}$. For two disjoint subsets $A, B \subseteq[p]$ and $\mathbf{x} \in \mathcal{R}$, the element $\mathbf{x}_{A} \mathbf{x}_{B}=\mathbf{x}_{A \cup B}$ is the subvector $\left(x_{i}\right)_{i \in A \cup B}$. The notation $\mathbf{x}_{A} \mathbf{x}_{B}$ is reminiscent of concatenation of strings, nevertheless we use it to denote the element $\mathbf{x}_{A \cup B}$ in $\mathcal{R}_{A \cup B}$ so the order of $A \cup B$ is important. A probability distribution $f$ for $X_{[p]}$ is a tuple $(f(\mathbf{x}): \mathbf{x} \in \mathcal{R})$ where $f(\mathbf{x})>0$ and $\sum_{\mathbf{x} \in \mathcal{R}} f(\mathbf{x})=1, f(\mathbf{x})$ is the probability of the outcome $\mathbf{x} \in \mathcal{R}$. The $|\mathcal{R}|-1$ dimensional open probability simplex, denoted by $\Delta_{|\mathcal{R}|-1}^{\circ}$ consists of all possible positive probability distributions for $X_{[p]}$.

To define a subvariety of the probability simplex we use the polynomial ring $\mathbb{R}[D]:=$ $\mathbb{R}\left[p_{\mathbf{x}}: \mathbf{x} \in \mathcal{R}\right]$. For any subset $H \subseteq \mathbb{R}[D]$ we denote the algebraic variety $\mathcal{V}(H)=\{x \in$ $\left.\mathbb{C}^{|\mathcal{R}|}: g(x)=0 \text { for all } g \in H\right\}$. The intersection $\mathcal{V}(H) \cap \Delta_{|\mathcal{R}|-1}^{\circ}$ is a statistical model. In our situation, statistical models can also be defined as closed images of rational maps intersected with the probability simplex. A main question in algebraic statistics is to find the implicit equations that define the parametrized model. In this statistical setting, the defining algebraic equations translate into restrictions on the distributions, these encode model assumptions.

Example 2.1. Consider the case where $p=3$ and $X_{1}, X_{2}, X_{3}$ are binary random variables. The graph $G=([3], 1 \rightarrow 2 \rightarrow 3)$ imposes conditional independence relations among the $X_{i}$, $i \in[3]$. The state space of $\left(X_{1}, X_{2}, X_{3}\right)$ is $\mathcal{R}=\{0,1\}^{3}$ because all random variables are binary, hence $|\mathcal{R}|=8$. The polynomial ring is $\mathbb{R}[D]=\mathbb{R}\left[p_{000}, p_{001}, p_{010}, p_{011}, p_{100}, p_{101}, p_{110}, p_{111}\right]$. As we will see in the next section, $G$ tells us that $X_{1}$ is independent of $X_{3}$, given $X_{2}$, as there is no edge from 1 to 3 . This CI relation translates into two equations, one for each outcome of the conditioning variable $X_{2}$ :

$$
p_{100} p_{001}-p_{101} p_{000}=0, \quad p_{110} p_{011}-p_{111} p_{010}=0
$$

These two equations, together with the hyperplane $\sum_{\mathbf{x} \in \mathcal{R}} p_{\mathbf{x}}=1$, define a variety in the affine 8 -dimensional space. Taking into account positivity conditions yields the model inside $\Delta_{7}^{\circ}$. By ignoring the sum-to-one hyperplane we immediately see that this model defines a toric variety in $\mathbb{P}^{7}$ as it is cut out by a prime binomial ideal.

We now introduce the formal setup for context-specific independence.
2.2. Context-specific conditional independence statements. Let $A, B, C, S$ be disjoint subsets of $[p]$ and let $\mathbf{x}_{C} \in \mathcal{R}_{C}$. A distribution $f \in \Delta_{|\mathcal{R}|-1}^{\circ}$ satisfies the context-specific conditional independence statement (CSI statement) $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}$ if for all outcomes $\left(\mathbf{x}_{A}, \mathbf{x}_{B}, \mathbf{x}_{S}\right) \in \mathcal{R}_{A} \times \mathcal{R}_{B} \times \mathcal{R}_{S}$

$$
f\left(\mathbf{x}_{A} \mid \mathbf{x}_{B}, \mathbf{x}_{S}, \mathbf{x}_{C}\right)=f\left(\mathbf{x}_{A} \mid \mathbf{x}_{S}, \mathbf{x}_{C}\right)
$$

To each CSI statement $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}$ we associate the collection of polynomials

$$
p_{\mathbf{x}_{A} \mathbf{x}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+} p_{\mathbf{y}_{A} \mathbf{y}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+}-p_{\mathbf{x}_{A} \mathbf{y}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+} p_{\mathbf{y}_{A} \mathbf{x}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+}
$$

for every $\mathbf{x}_{A}, \mathbf{y}_{A} \in \mathcal{R}_{A}, \mathbf{x}_{B}, \mathbf{y}_{B} \in \mathcal{R}_{B}$ and $\mathbf{x}_{S} \in \mathcal{R}_{S}$ where

$$
p_{\mathbf{x}_{A} \mathbf{x}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+}=\sum_{\mathbf{z} \in \mathcal{R}_{[p] \backslash(A \cup B \cup C \cup S)}} p_{\mathbf{x}_{A} \mathbf{x}_{B} \mathbf{x}_{S} \mathbf{x}_{C} \mathbf{z}}
$$

Note that these polynomials are the $2 \times 2$ minors of the matrix $\left(p_{\mathbf{x}_{A} \mathbf{x}_{B} \mathbf{x}_{S} \mathbf{x}_{C}+}\right)_{\mathbf{x}_{A} \in \mathcal{R}_{A}, \mathbf{x}_{B} \in \mathcal{R}_{B}}$ for all outcomes $\mathbf{x}_{S} \in \mathcal{R}_{S}$. We define the ideal $I_{X_{A} \perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}}$ in $\mathbb{R}[D]$ to be the ideal generated by all the polynomials in (1).

Given a collection $\mathcal{C}$ of CSI statements, we define the CSI ideal generated by the polynomials associated to all CSI statements in $\mathcal{C}$, i.e.

$$
I_{\mathcal{C}}=\sum_{X_{A} \perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{X_{A} \perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}}
$$

When the set $C$ in the conditioning of a CSI statement is empty, we recover the notion of conditional independence (CI) which are statements of the form $X_{A} \perp X_{B} \mid X_{S}$. In this case $I_{\mathcal{C}}$ is a conditional independence ideal, see [Sul18, Ch.4]. Graphical models are a widely used class of CI models where the CI statements among random variables are captured by a graph. More general CSI statements cannot be easily encoded using a single graph, to encode these, the staged tree model is more suitable. We define discrete graphical models associated to DAGs (also known as Bayesian networks) and staged tree models in the next section.
2.3. DAGs and staged trees. A directed acyclic graph (DAG) $G$ is a pair $([p], E)$ where $[p]$ is the set of vertices and $E$ the set of directed edges such that there is no directed loop in $G$. For any DAG $G$, we fix a topological ordering on its vertices, which means if $i \rightarrow j$ is an edge in $G$, then $i<j$. The DAG model $\mathcal{M}(G)$ is the set of all the distributions $f \in \Delta_{|\mathcal{R}|-1}^{a}$ that satisfy the recursive factorization property according to $G$. That is, for all $\mathbf{x} \in \mathcal{R}$ we have

$$
p_{\mathbf{x}}=f(\mathbf{x})=\prod_{v \in[p]} f\left(\mathbf{x}_{v} \mid \mathbf{x}_{\mathrm{pa}(v)}\right)
$$

On the other hand, DAG models can also be defined implicitly by using the polynomials associated to the CI statements via different Markov properties [MDLW18, Section 1.8]. The local Markov property of a DAG $G$ is the collection of CI statements

$$
\operatorname{local}(G)=\left\{X_{v} \perp X_{\operatorname{nd}(v)} \mid X_{\mathrm{pa}(v)}: v \in V\right\}
$$

where $\operatorname{nd}(v)$ denotes the set of all non-descendants of the node $v$ and $\mathrm{pa}(v)$ denotes the set of its parents in $G$. While these local constraints contain information about independence relationships, they are often not enough to fully describe the set of all CI statements that hold in $G$. Via the axioms of conditional independence, [Sul18, Prop. 4.1.4], these local constraints may imply other CI statements. Hence, it is necessary to introduce the global Markov property. Any CI relation that holds for the model $\mathcal{M}(G)$ is obtained from $G$ via the technical notion of $d$-separation statements [Lau96, Section 3.2.2]. The set of all $d$ separation statements, denoted by global $(G)$, defines the global Markov property on $G$. The corresponding ideal $I_{\text {global }(G)}$ is not prime in general. It is, however, prime and generated by binomials if the graph is perfect (see Definition 2.12). In Example 2.1, the local Markov property and the global Markov property of $G$ coincide and the ideal $I_{\text {local }(G)}=I_{\text {global }(G)}$ is prime and binomial.

While DAG models are well-suited to encode CI statements, they cannot encode CSI statements. There are several models one could use instead to encode CSI statements. In

![img-0.jpeg](img-0.jpeg)

Figure 1. A CStree for $p=3$ and its minimal context DAGs.

This paper, we focus on staged tree models. The definition of staged tree model we present here is not as general as in [SA08]. The reason for this choice is that we are interested only in representing CSI statements that hold for a vector of discrete random variables $X_{[p]}$. Thus the staged trees we consider represent the outcome space of $X_{[p]}$ as an event tree and we construct them as follows.

Let $\pi_{1} \cdots \pi_{p}$ be an ordering of $[p]$ and let $\mathcal{T}=(V, E)$ be a rooted tree with $V:=\{\operatorname{root}\} \cup$ $\bigcup_{j \in[p]} \mathcal{R}_{\left\{\pi_{1} \cdots \pi_{j}\right\}}$ and set of edges

$$
\begin{aligned}
E:= & \left\{\text { root } \rightarrow x_{\pi_{1}}: x_{\pi_{1}} \in\left[d_{\pi_{1}}\right]\right\} \cup \\
& \left\{x_{\pi_{1}} \cdots x_{\pi_{k-1}} \rightarrow x_{\pi_{1}} \cdots x_{\pi_{k}}: x_{\pi_{1}} \cdots x_{\pi_{k-1}} \in \mathcal{R}_{\pi_{1}, \ldots, \pi_{k-1}}, x_{k} \in\left[d_{k}\right], k \in[p]\right\}
\end{aligned}
$$

Note that elements in the set of vertices $V$ of $\mathcal{T}$ are outcomes in the marginal outcome spaces $\mathcal{R}_{\pi_{1} \cdots \pi_{j}}$ for $j \in[p]$. For several of the definitions and proofs we shall present, when considering an element $v \in V$, it is not always necessary to specify which marginal outcome space contains $v$. Thus we simply write $v$ for an arbitrary element in $V$.

The level of a node $v \in V$ is the number of edges in the unique path in $\mathcal{T}$ from the root to $v$. The $k$ th level of $\mathcal{T}$ is the set of all nodes in $\mathcal{T}$ at level $k$ and is denoted by $L_{k}$. For $\mathcal{T}$ as defined, we see that $L_{k}$ is in bijection with the outcome space $\mathcal{R}_{\left\{\pi_{1}, \ldots, \pi_{k}\right\}}$ of the random vector $X_{\left\{\pi_{1}, \ldots, \pi_{k}\right\}}$. Hence we identify the outcomes of the variable $X_{\pi_{k}}$ with the level $L_{k}$, and we denote this association by $\left(L_{1}, \ldots, L_{p}\right) \sim\left(X_{\pi_{1}}, \ldots, X_{\pi_{p}}\right)$. For any tree $\mathcal{T}$ we write $V_{\mathcal{T}}$ and $E_{\mathcal{T}}$ for its sets of vertices and edges, respectively. We write $E(v)$ to denote the set of all outgoing edges from $v$. Without loss of generality, throughout this paper we will assume $\pi_{i}=i$ for all $i \in[p]$. In particular, this implies $\left(L_{1}, \ldots, L_{p}\right) \sim\left(X_{1}, \ldots, X_{p}\right)$. The tree in Figure 1 represents an event tree for a vector $\left(X_{1}, X_{2}, X_{3}\right)$ of binary random variables. To illustrate part of the notation, in this tree we have $L_{2}=\{00,01,10,11\}$, which is exactly the marginal outcome space $\mathcal{R}_{\{1,2\}}$ and $E(0):=\{0 \rightarrow 00,0 \rightarrow 01\}$.

Let $\mathcal{T}=(V, E)$ be a rooted tree with levels $\left(L_{1}, \cdots, L_{p}\right) \sim\left(X_{1}, \ldots, X_{p}\right), \mathcal{L}$ a finite set of labels and $\theta: E \rightarrow \mathcal{L}$ a labeling of the edges. The pair $(\mathcal{T}, \theta)$ is a staged tree if
(1) $|\theta(E(v))|=|E(v)|$ for all $v \in V$, and
(2) for any pair $v, w \in V, \theta(E(v))$ and $\theta(E(w))$ are either equal or disjoint.

Two vertices $v, w$ in $(\mathcal{T}, \theta)$ are in the same stage if and only if $\theta(E(v))=\theta(E(w))$. In this case we write $v \sim w$. The equivalence relation $\sim$ on the set $V$ induces a partition of $V$ called the staging of $\mathcal{T}$. We refer to each set in this partition as a stage. When depicting staged trees, such as in Figure 1, we use colors in the vertices to indicate that two vertices are in the same stage, except for white vertices which always represent singleton stages. Intuitively, the vertices in a stage $S$ in level $L_{k-1}$ represent outcomes $x_{1} \cdots x_{k-1}$ for which the conditional distributions $f\left(X_{k} \mid x_{1} \cdots x_{k-1}\right), x_{1} \cdots x_{k-1} \in S$ are all equal. In all staged trees we consider,

the leaves of the tree and the root of the tree are always singleton stages, thus we often omit them when talking about the partition of $V$ into stages.

Definition 2.2. Let $\mathcal{T}$ be a staged tree. The staged tree model $\mathcal{M}(\mathcal{T})$ has the space of parameters

$$
\Theta_{\mathcal{T}}=\left\{x \in \mathbb{R}^{|\mathcal{L}|}: \forall e \in E, x_{\theta(e)} \in(0,1) \text { and } \forall v \in V, \sum_{e \in E(v)} x_{\theta(e)}=1\right\}
$$

and is defined to be the image of the map

$$
\Psi_{\mathcal{T}}: \Theta_{\mathcal{T}} \rightarrow \Delta_{|\mathcal{R}|-1}^{\circ}, \quad x \mapsto\left(\prod_{e \in E(\text { root } \rightarrow \mathbf{x})} x_{\theta(e)}\right)_{\mathbf{x} \in \mathcal{R}}
$$

where $E(\operatorname{root} \rightarrow \mathbf{x})$ denotes the set of all edges on the path from the root to $\mathbf{x} \in \mathcal{R}$. We say a distribution $f \in \Delta_{|\mathcal{R}|-1}^{\circ}$ factors according to $\mathcal{T}$ if $f \in \operatorname{im}\left(\Psi_{\mathcal{T}}\right)$.

Example 2.3. Consider the staged tree depicted in Figure 1 (left) with levels $\left(L_{1}, L_{2}, L_{3}\right) \sim$ $\left(X_{1}, X_{2}, X_{3}\right)$. It represents the event tree for a vector $\left(X_{1}, X_{2}, X_{3}\right)$ of binary random variables with ordering $\pi=123$. The set of stages in this tree is $\{\{0,1\},\{00,10\},\{01\},\{11\}\}$. The stage $\{0,1\}$ is the set of blue nodes and the stage $\{00,10\}$ is the set of green nodes in Figure 1. The blue stage encodes the equality $f\left(X_{2} \mid X_{1}=0\right)=f\left(X_{2} \mid X_{1}=1\right)$ and the green stage encodes the equality $f\left(X_{3} \mid X_{12}=00\right)=f\left(X_{3} \mid X_{12}=10\right)$. These equalities of conditional probabilities correspond to the set of CSI statements $\mathcal{C}=\left\{X_{2} \Perp X_{1}, X_{3} \Perp X_{1} \mid X_{2}=0\right\}$. In this case $\mathcal{M}(\mathcal{T})=\mathcal{V}\left(I_{\mathcal{C}}\right) \cap \Delta_{7}^{\circ}$.

Since CI statements are collections of CSI statements when the context $C$ in Eq. (1) is empty, it is natural to see that DAG models are a particular type of staged tree model. In particular, every DAG model has a staged tree representation; see Example 2.5 and [DS23, Section 2.1]. The Definition 2.2 of staged tree model allows for very flexible types of stagings. In the next section we define CStree models which are a class of staged tree models for which the staging has to satisfy additional conditions.
2.4. CStrees. In this section we introduce CStree models as a subclass of staged tree models.

Definition 2.4. The staged tree $(\mathcal{T}, \theta)$ is a CStree if
(1) $\theta(E(v)) \neq \theta(E(w))$ if $v, w$ are in different levels,
(2) $\theta\left(x_{1} \cdots x_{k-1} \rightarrow x_{1} \cdots x_{k-1} x_{k}\right)=\theta\left(y_{1} \cdots y_{k-1} \rightarrow y_{1} \cdots y_{k-1} x_{k}\right)$ whenever the nodes $x_{1} \cdots x_{k-1}$ and $y_{1} \cdots y_{k-1}$ are in the same stage.
(3) For every stage $S \subseteq L_{k-1}, k \in[p]$, there exists $C \subseteq[k-1]$ and $\mathbf{x}_{C} \in \mathcal{R}_{C}$ such that

$$
S=\bigcup_{\mathbf{y} \in \mathcal{R}_{[k-1] \backslash C}}\left\{\mathbf{x}_{C} \mathbf{y}\right\}
$$

Condition (1) ensures that two nodes in different levels do not share the same conditional distribution. Condition (2) forces that edges with the same label must point to the same outcome of $X_{k}$. Condition (3) restricts the types of CSI statements that can be encoded simultaneously in a CStree to be those described in Lemma 2.7.

To describe a CStree model $\mathcal{M}(\mathcal{T})$ as an algebraic variety intersected with the open probability simplex we consider the ring homomorphism

$$
\psi_{\mathcal{T}}: \mathbb{R}[D] \rightarrow \mathbb{R}\left[\Theta_{\mathcal{T}}\right], \quad p_{\mathbf{x}} \mapsto \prod_{e \in E(\text { root } \rightarrow \mathbf{x})} \theta(e)
$$

where $\mathbb{R}\left[\Theta_{\mathcal{T}}\right]:=\mathbb{R}[\theta(e): e \in E] /\langle\theta-1\rangle$ and $\langle\theta-1\rangle:=\left\langle\sum_{e \in E(v)} \theta(e)-1: v \in V\right\rangle$ is the ideal representing the sum-to-one conditions on the parameter space. The ring map $\psi_{\mathcal{T}}$ is the pullback of the parametrization $\Psi_{\mathcal{T}}$ of the model $\mathcal{M}(\mathcal{T})$ in Definition 2.2. Using $\psi_{\mathcal{T}}$, we can write the CStree model as

$$
\mathcal{M}(\mathcal{T})=\mathcal{V}\left(\operatorname{ker}\left(\psi_{\mathcal{T}}\right)\right) \cap \Delta_{\mid \mathcal{R} \mid-1}^{\circ}
$$

Example 2.5. (CStree representation of a DAG model) Let $G=([p], E)$ be a DAG. The model $\mathcal{M}(G)$ is the set of all distributions in $\Delta_{\mid \mathcal{R} \mid-1}^{\circ}$ that satisfy the recursive factorization property according to $G$. Following [DS22, Section 2.1], to represent $\mathcal{M}(G)$ as a CStree model we first fix an ordering $\pi$ of $[p]$ and then consider the tree $\mathcal{T}_{G}$ with levels $\left(L_{1}, \ldots, L_{p}\right) \sim$ $\left(X_{\pi_{1}}, \ldots, X_{\pi_{p}}\right)$. It remains to specify the labelling of $\left(\mathcal{T}_{G}, \theta\right)$. The labelling is completely determined by the staging, hence we specify the stages for each level $L_{k-1}$ where $k \in[p]$. Fix $k \in[p]$, then $L_{k-1}$ has one stage $S_{\mathbf{x}_{\mathrm{pa}(k)}}=\left\{\mathbf{x}_{\mathrm{pa}(k)} \mathbf{y}: \mathbf{y} \in \mathcal{R}_{[k-1] \backslash \mathrm{pa}(k)}\right\}$ for each outcome $\mathbf{x}_{\mathrm{pa}(k)} \in \mathcal{R}_{\mathrm{pa}(k)}$. Note that for each $k \in[p]$, and for each $\mathbf{x}_{\mathrm{pa}(k)} \in \mathcal{R}_{\mathrm{pa}(k)}, S_{\mathbf{x}_{\mathrm{pa}(k)}}$ satisfies condition (3) in the definition of a CStree, hence $\left(\mathcal{T}_{G}, \theta\right)$ is a CStree and $\mathcal{M}(G)=\mathcal{M}\left(\mathcal{T}_{G}\right)$. We highlight the difference between these two combinatorial representations of the same model; while $G$ is a DAG whose vertices are random variables, $\mathcal{T}_{G}$ is a directed tree whose leaves are the outcome space of the joint distribution of the random variables, which are the nodes, in $G$. The model restrictions in $G$ are encoded via absence of edges, the same model restrictions in $\mathcal{T}_{G}$ are encoded via stages. The map $\Psi_{\mathcal{T}_{G}}$ from Definition 2.2 is equal to the recursive factorization according to $G$ in the beginning of Section 2.3. To illustrate this construction, consider the DAG model from Example 2.1. In this case the ordering of the binary random variables is $\left(X_{1}, X_{2}, X_{3}\right)$ and the tree $\mathcal{T}_{G}$ (disregarding the coloring of the vertices) is represented in Figure 1. The stages of $\mathcal{T}_{G}$ in level $L_{1}$ are $\{0\},\{1\}$ and in $L_{2}$ two these are $\{00,10\},\{01,11\}$.

Remark 2.6. For a DAG $G$, the map $\psi_{\mathcal{T}_{G}}$ is the algebraic version of the well-known recursive factorization according to $G$. It is important to note that the ideal $I_{\text {global }(G)}$ is not always equal to the prime ideal $\operatorname{ker}\left(\psi_{\mathcal{T}_{G}}\right)$. The article [GSS05] contains several examples where equality holds as well as numerous counterexamples. The strongest possible algebraic characterization of a model is to find the generators for $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$. For most graphical models, discrete and Gaussian, it is an open question to find generators of $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$. A recent overview of the state of the art is presented in [MDLW18, Chapter 3]. For discrete decomposable DAG models such a characterization can be found in [GMS06, Theorem 4.4]. Our Theorem 5.3 characterizes $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ in terms of CSI statements for all balanced CStree models as defined in 2.13 .

The next lemma describes the type of CSI statements encoded by a CStree; they are a consequence of condition (3) in Definition 2.4.

Lemma 2.7. [DS22, Lemma 3.1] Let $\mathcal{T}$ be a CStree with levels $\left(L_{1}, \ldots, L_{p}\right)$ $\sim\left(X_{1}, \ldots, X_{p}\right)$. Then for any $f \in \mathcal{M}(\mathcal{T})$ and stage $S \subseteq L_{k-1}$, condition (3) in Definition 2.4 implies that $f$ entails the CSI statement $X_{k} \mathbb{1} X_{[k-1] \backslash C} \mid X_{C}=\mathbf{x}_{C}$ where $C$ is the set of all

indices $\ell$ such that all elements in $S$ have the same outcome for $X_{\ell}$. Hence, $\mathbf{x}_{C}=\mathbf{y}_{C}$ for any $\mathbf{y} \in S$.

For any stage $S$ the context $X_{C}=\mathbf{x}_{C}$ in Lemma 2.7 is called the stage-defining context of the stage $S$. Given a stage defining context $X_{C}=\mathbf{x}_{C}$ for a stage $S$ in level $L_{k-1}$ we recover the stage from the statement $X_{k} \Perp X_{[k-1] \backslash C} \mid X_{C}=\mathbf{x}_{C}$ as $S=\bigcup_{\mathbf{y} \in \mathcal{R}_{[k-1] \backslash C}}\left\{\mathbf{x}_{C} \mathbf{y}\right\}$.
2.5. CStrees as collections of context DAGs. An important question in the study of conditional independence statements is to understand when a combination of CI statements implies additional CI statements. The rules to deduce new statements are called conditional independence axioms [Sul18, Ch.4]. For instance, applying these axioms to the local Markov property that holds for a DAG $G$ results in new CI statements that hold for $G$ and the global Markov property encompasses all CI statements that hold for $G$. The same question arises in the study of CSI statements. Namely, what are all CSI statements that are implied by a given set of CSI statements? The rules to deduce new CSI statements from existing ones are the context-specific independence axioms, or CSI axioms for short. We use here the CSI axioms presented in [DS22, Section 3.2] and point out that an axiomatic study of CSI statements was carried out before in $\left[\right.$ CHK $\left.^{+} 16\right]$.
(1) symmetry. $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C} \Longrightarrow X_{B} \Perp X_{A} \mid X_{S}, X_{C}=\mathbf{x}_{C}$.
(2) decomposition. $X_{A} \Perp X_{B \cup D} \mid X_{S}, X_{C}=\mathbf{x}_{C} \Longrightarrow X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}$.
(3) weak union. If $X_{A} \Perp X_{B \cup D} \mid X_{S}, X_{C}=\mathbf{x}_{C} \Longrightarrow X_{A} \Perp X_{B} \mid X_{S \cup D}, X_{C}=\mathbf{x}_{C}$.
(4) contraction. If $X_{A} \Perp X_{B} \mid X_{S \cup D}, X_{C}=\mathbf{x}_{C}$ and $X_{A} \Perp X_{D} \mid X_{S}, X_{C}=\mathbf{x}_{C} \Longrightarrow$ $X_{A} \Perp X_{B \cup D} \mid X_{S}, X_{C}=\mathbf{x}_{C}$.
(5) intersection. If $X_{A} \Perp X_{B} \mid X_{S \cup D}, X_{C}=\mathbf{x}_{C}$ and $X_{A} \Perp X_{S} \mid X_{B \cup D}, X_{C}=\mathbf{x}_{C} \Longrightarrow$ $X_{A} \Perp X_{B \cup S} \mid X_{D}, X_{C}=\mathbf{x}_{C}$.
(6) specialization. If $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}, T \subseteq X_{S}$ and $\mathbf{x}_{T} \in \mathcal{R}_{T}, \Longrightarrow X_{A} \Perp X_{B} \mid$ $X_{S \backslash T}, X_{T \cup C}=\mathbf{x}_{T \cup C}$.
(7) absorption. If $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}$, and there exists $T \subseteq C$ for which $X_{A} \Perp X_{B} \mid$ $X_{S}, X_{C \backslash T}=\mathbf{x}_{C \backslash T}, X_{T}=\mathbf{x}_{T}$ for all $\mathbf{x}_{T} \in \mathcal{R}_{T}, \Longrightarrow X_{A} \Perp X_{B} \mid X_{S \cup T}, X_{C \backslash T}=\mathbf{x}_{C \backslash T}$.
The first five axioms are a direct generalization of the CI axioms. The specialization axiom (6) says that whenever you have a vector $X_{S}$ in the conditioning set you can specialize it to a CSI relation by choosing an outcome $\mathbf{x}_{T} \in \mathcal{R}_{T}$. The absorption axiom (7) is the opposite of specialization, it says that if you have a collection of CSI statements such that, in the conditioning contexts, for a certain subset $T$, all outcomes of $X_{T}$ are present, then this turns into a CSI statement including the vector $X_{T}$ in the conditioning set.
Example 2.8. Consider a DAG $G=([p], E)$ and $k \in[p]$. In the staged tree representation $\mathcal{T}_{G}$ of $G$ presented in Example 2.5, for each $k \in[p]$ there is one stage in level $L_{k-1}$ for each outcome $\mathbf{x}_{\mathrm{pa}(k)} \in X_{\mathrm{pa}(k)}$. Using Lemma 2.7, such stage entails the CSI statement $X_{k} \Perp X_{[k-1] \backslash \mathrm{pa}(k)} \mid X_{\mathrm{pa}(k)}=\mathbf{x}_{\mathrm{pa}(k)}$. Thus the stages of $\mathcal{T}_{G}$ in level $L_{k-1}$ correspond to the set of CSI statements $\left\{X_{k} \Perp X_{[k-1] \backslash \mathrm{pa}(k)} \mid X_{\mathrm{pa}(k)}=\mathbf{x}_{\mathrm{pa}(k)}: \mathbf{x}_{\mathrm{pa}(k)} \in \mathcal{R}_{\mathrm{pa}(k)}\right\}$. Using the absorption axiom this implies the CI statement $X_{k} \Perp X_{[k-1] \backslash \mathrm{pa}(k)} \mid X_{\mathrm{pa}(k)}$. Note that in turn, each statement of the form $X_{k} \Perp X_{[k-1] \backslash \mathrm{pa}(k)} \mid X_{\mathrm{pa}(k)}=\mathbf{x}_{\mathrm{pa}(k)}$ is a specialization of $X_{k} \Perp X_{[k-1] \backslash \mathrm{pa}(k)} \mid X_{\mathrm{pa}(k)}$.

Let $\mathcal{J}(\mathcal{T})$ be the set of all CSI statements implied by applying the CSI axioms [DS22, Section 3.2] to the statements in Lemma 2.7. By the absorption axiom [DS22, Lemma 3.2], there exists a collection $\mathcal{C}_{\mathcal{T}}:=\left\{X_{C}=\mathbf{x}_{C}\right\}$ of contexts such that for any $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=$

$\mathbf{x}_{C} \in \mathcal{J}(\mathcal{T})$ with $X_{C}=\mathbf{x}_{C} \in \mathcal{C}_{\mathcal{T}}$, there is no subset $T \subseteq C$ for which $X_{A} \Perp X_{B} \mid X_{S \cup T}, X_{C \backslash T}=$ $\mathbf{x}_{C \backslash T} \in \mathcal{J}(\mathcal{T})$. We call such $X_{C}=\mathbf{x}_{C} \in \mathcal{C}_{\mathcal{T}}$ a minimal context of $\mathcal{T}$. Also, from [DS22, Lemma 3.2], it follows that

$$
\mathcal{J}(\mathcal{T})=\bigcup_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}_{\mathcal{T}}} \mathcal{J}\left(X_{C}=\mathbf{x}_{C}\right)
$$

where $\mathcal{J}\left(X_{C}=\mathbf{x}_{C}\right)$ is the set of all CI statements of the form $X_{A} \Perp X_{B} \mid X_{S}$ that hold in the context $X_{C}=\mathbf{x}_{C}$. This equality establishes that the set of all CSI statements that are implied by $\mathcal{T}$ using the CSI axioms, is equal to the union of all the statements that are implied, using the CSI axioms, by the set of statements in each of the minimal contexts.

We now construct a DAG associated to each minimal context $X_{C}=\mathbf{x}_{C} \in \mathcal{C}_{\mathcal{T}}$ using a minimal I-MAP [KF09, Section 3.4.1]. We say that a DAG $H$ is an I-MAP for a set of CI statements $\mathcal{I}$ if the set of all CI statements implied by $G$, denoted $\mathcal{I}(G)$, is contained in $\mathcal{I}$, [KF09, Section 3.2.3]. A DAG $H$ is a minimal I-MAP for $\mathcal{I}$ if $H$ is an I-MAP of $\mathcal{I}$ and if the removal of a single edge from $H$ renders it not an I-MAP. To each such $X_{C}=\mathbf{x}_{C} \in \mathcal{C}_{\mathcal{T}}$, we can associate a minimal context $D A G$ with set of ordered nodes $[p] \backslash C$, denoted by $G_{X_{C}=\mathbf{x}_{C}}$, via a minimal I-MAP of $\mathcal{J}\left(X_{C}=\mathbf{x}_{C}\right)$ [DS22, Section 3.2]; this ordering should be a restriction of the ordering of the variables $X_{[p]}$ in $\mathcal{T}$. A construction of a minimal I-MAP is explained in [KF09, Algorithm 3.2].

Example 2.9. Consider the binary CStree $\mathcal{T}$ on three random variables with ordering 123 given in Figure 1. Since the two nodes in level $L_{1}$ are in the same stage (represented by the same colors), this CStree implies the CI statement $X_{1} \Perp X_{2}$. As the nodes 00 and 10 are in the same stage in level $L_{2}$, but 01 and 11 are not, we get the CSI statement $X_{3} \Perp X_{1} \mid X_{2}=0$. Therefore, $\mathcal{J}(\mathcal{T})=\left\{X_{1} \Perp X_{2}, X_{1} \Perp X_{3} \mid X_{2}=0\right\}$. Especially, we see that the set of minimal contexts $\mathcal{C}$ is $\left\{\varnothing, X_{2}=0\right\}$ and $\mathcal{J}(\mathcal{T})=\mathcal{J}(\varnothing) \cup \mathcal{J}\left(X_{2}=0\right)$ where $\mathcal{J}(\varnothing)=\left\{X_{1} \Perp X_{2}\right\}$ and $\mathcal{J}\left(X_{2}=0\right)=\left\{X_{1} \Perp X_{3} \mid X_{2}=0\right\}$. The minimal I-MAP of $\mathcal{J}(\varnothing)$ is a DAG with nodes $\{1,2,3\}$ and ordering 123 which entails $X_{1} \Perp X_{2}$. This is exactly the DAG $G_{\varnothing}$ in Figure 1. Similarly, the minimal I-MAP of $\mathcal{J}\left(X_{2}=0\right)$ is a DAG on the set of nodes $\{1,3\}$, with ordering 13, that entails $X_{1} \Perp X_{3}$; this DAG has two nodes and no edge between them and is displayed as $G_{X_{2}=0}$ in Figure 1.

Each context DAG $G_{X_{C}=\mathbf{x}_{C}}$ is in particular a DAG, thus by Example 2.5, it has a staged tree representation which we denote by $\mathcal{T}_{G_{X_{C}=\mathbf{x}_{C}}}$. To relate $\mathcal{T}_{G_{X_{C}=\mathbf{x}_{C}}}$ to the original tree $\mathcal{T}$, we define a context subtree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ for each context $X_{C}=\mathbf{x}_{C}$. Let $x_{1} \cdots x_{k} \in \mathcal{T}$ and denote by $\mathcal{T}_{x_{1} \cdots x_{k}}$ the directed subtree of $\mathcal{T}$ with root node $x_{1} \cdots x_{k}$. For $C \subseteq[p]$ and $\mathbf{x}_{C} \in \mathcal{R}_{C}$ we construct the context subtree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}=\left(V_{X_{C}=\mathbf{x}_{C}}, E_{X_{C}=\mathbf{x}_{C}}\right)$ by deleting all subtrees $\mathcal{T}_{x_{1} \cdots x_{k}}$ and all edges $x_{1} \cdots x_{k-1} \rightarrow x_{1} \cdots x_{k}$ with $x_{k} \neq \mathbf{x}_{C \cap k}$, and then contracting the edges $x_{1} \cdots x_{k-1} \rightarrow x_{1} \cdots x_{k-1}\left(\mathbf{x}_{C}\right)_{k}$ for all $x_{1} \cdots x_{k-1} \in \mathcal{R}_{[k-1]}$, for all $k \in C$. The single node resulting from this contraction is labeled $x_{1} \cdots x_{k-1}\left(\mathbf{x}_{C}\right)_{k}$ and it is in the same stage as $x_{1} \cdots x_{k-1} \mathbf{x}_{C \cap\{k\}}$ in $\mathcal{T}$. All of the other nodes in $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ inherit their staging from $\mathcal{T}$. Note that the context subtree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ is itself a CStree and $\mathcal{T}_{x_{1} \cdots x_{k}}$ is the context subtree $\mathcal{T}_{X_{[k]}=x_{1} \cdots x_{k}}$.

Moreover, let $X_{C}=\mathbf{x}_{C}$ be a minimal context of $\mathcal{T}$. Then by the construction of $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ the CSI statements that hold in $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ are given as

$$
\mathcal{J}\left(\mathcal{T}_{X_{C}=\mathbf{x}_{C}}\right)=\left\{X_{A} \Perp X_{B} \mid X_{S}, X_{D}=\mathbf{x}_{D}: X_{A} \Perp X_{B} \mid X_{S}, X_{D}=\mathbf{x}_{D}, X_{C}=\mathbf{x}_{C} \in \mathcal{J}(\mathcal{T})\right\}
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Staged tree that is not a CStree.

with $A, B, S, D \subseteq[p] \backslash C$. Similarly, the CI statements on $X_{[p] \backslash C}$ implied by the DAG $G_{X_{C}=\mathbf{x}_{C}}$ are

$$
\mathcal{J}\left(X_{C}=\mathbf{x}_{C}\right)=\left\{X_{A} \Perp X_{B} \mid X_{S}: X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C} \in \mathcal{J}(\mathcal{T})\right\}
$$

which are precisely the CI statements valid in $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$. This shows that the CI statements implied by the DAG $G_{X_{C}=\mathbf{x}_{C}}$ are exactly the CI statements implied by the CStree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$. In general, the CStrees $\mathcal{T}_{G_{X_{C}=\mathbf{x}_{C}}}$ and $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ are different, since the CStree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ may imply more CSI statements, see Example 2.10 and Example 4.1. If $\varnothing \in \mathcal{C}_{\mathcal{T}}$ then $G_{\varnothing}$ is a DAG that captures the CI relations implied by $\mathcal{T}$. When $\varnothing \notin C_{\mathcal{T}}$, then $\mathcal{T}$ entails no CI relations, in this case we associate to $\mathcal{T}$ the complete DAG on $[p]$ nodes whose directed arrows are in agreement with the causal ordering of $\mathcal{T}$, we also denote this DAG by $G_{\varnothing}$.
Example 2.10. We illustrate the construction of the context subtree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ and the staged tree representation of a context DAG $\mathcal{T}_{G_{X_{C}=\mathbf{x}_{C}}}$ using the CStree in Example 2.9. For the empty minimal context, $\mathcal{T}_{\varnothing}$ is equal to the original tree $\mathcal{T}$. However, $\mathcal{T}_{G_{\varnothing}}$ is a CStree with the same vertices and edges of $\mathcal{T}$ but with set of stages equal to $\{\{0,1\},\{00\},\{01\},\{10\},\{11\}\}$. Importantly, $\mathcal{T}_{\varnothing} \neq \mathcal{T}_{G_{\varnothing}}$. For the minimal context $X_{2}=0, \mathcal{T}_{X_{2}=0}$ is a staged tree with two levels whose staging is the same as the staging of the tree $\mathcal{T}_{G_{X_{2}=0}}$ on two levels associated to $G_{X_{2}=0}$.
Example 2.11. For the sake of intuition we present an example in Figure 2 of a collection of context DAGs that do not define a CStree. Consider the two DAGs $G_{\varnothing}=([3],\{2 \rightarrow 3\})$ and $G_{X_{1}=0}=(\{2,3\}, \varnothing)$ and assume all random variables are binary. These two DAGs imply the CI relation $X_{1} \Perp X_{2,3}$ and the CSI relation $X_{2} \Perp X_{3} \mid X_{1}=0$.

Let $\mathcal{T}$ be a staged tree with levels $\left(L_{1}, L_{2}, L_{3}\right) \sim\left(X_{1}, X_{2}, X_{3}\right)$. We will see that the staging of $\mathcal{T}$ cannot be a CStree. The vertices 10 and 00 are in the same stage because in the empty context DAG, $G_{\varnothing}, f\left(X_{3} \mid X_{1,2}=10\right)=f\left(X_{3} \mid X_{1,2}=00\right)$. Moreover, since $X_{2} \Perp X_{3} \mid X_{1}=0$, we also have $f\left(X_{3} \mid X_{1,2}=00\right)=f\left(X_{3} \mid X_{1,2}=01\right)$, thus 00 and 01 are also in the same stage. This implies $10,00,01$ are all in the same stage, which by definition of CStree implies that so are all vertices $00,01,10,11$. Thus the CI statement $X_{3} \Perp X_{1,2}$ holds in the CStree. However, this statement is not implied by the two DAGs.
2.6. Balanced CStrees. Decomposable graphical models are a set of graphical models for which the undirected and directed Markov properties coincide. These are characterized in many different ways: combinatorially as chordal UGs or as perfect DAGs, and geometrically as those DAG models that are discrete exponential families [GHKM01], also known as toric models in the algebraic statistics literature [Sul18]. The article [DS22] suggests the family of balanced staged tree models as a suitable generalization of decomposable DAG models because these models are discrete exponential families. Furthermore, a DAG is perfect if and only if its CStree representation is balanced. Thus we identify the class of balanced CStrees

as a good candidate for decomposable models in the context-specific setting. Our main goal is to explore to which extent the properties of decomposable DAG models carry over to the context-specific case.

Definition 2.12. A DAG $G=([p], E)$ is perfect if the skeleton of the induced subgraph on the vertices $\mathrm{pa}(k)$ is a complete graph for all $k \in[p]$.

There are several equivalent ways to define a perfect DAG. Another way to characterize a perfect DAG $G$ is to require that its skeleton is chordal and there is no triple $u, v, w$ of vertices such that $u \rightarrow w, v \rightarrow w$ are edges in $G$ but $u$ and $v$ are not adjacent. One can also characterize a perfect DAG via its moral graph, see [Lau96].

Let $G$ be a DAG and let $\mathcal{T}_{G}$ be the staged tree representation of $G$. A characterization of perfect DAGs is also available via balanced CStrees.

Definition 2.13. Let $\mathcal{T}$ be a CStree. For any vertex $v=x_{1} \cdots x_{k-1} \in \mathcal{T}$ we define the interpolating polynomial at $v$ by

$$
t(v):=\sum_{\mathbf{z} \in \mathcal{R}_{[p] \backslash[k-1]}}\left(\prod_{e \in E(v \rightarrow v \mathbf{z})} \theta(e)\right) \in \mathbb{R}[\theta(e): e \in E]
$$

A pair of vertices $v=x_{1} \cdots x_{k-1}$ and $w=y_{1} \cdots y_{k-1}$ in the same stage is balanced if for all $s, r \in\left[d_{k}\right]$, we have the equality

$$
t(v s) t(w r)=t(v r) t(w s)
$$

in the polynomial ring $\mathbb{R}[\theta(e): e \in E]$. The tree $\mathcal{T}$ is balanced if every pair of vertices in the same stage is balanced.

Remark 2.14. The polynomial $t$ (root) in the previous definition is called the interpolating polynomial of $\mathcal{T}$. Such polynomial is useful to study equivalence classes of staged tree models [GS18] and enumerating the trees in the equivalence class [GBRS18b] of any given staged tree.

Theorem 2.15. [DS23, Theorem 3.1] The DAG $G$ is perfect if and only if $\mathcal{T}_{G}$ is balanced if and only if $\mathcal{M}(G)$ is decomposable.

One could hope that the direct generalization of Theorem 2.15 is true for balanced CStrees. Namely that a CStree $\mathcal{T}$ is balanced if and only all of its minimal context DAGs are perfect. This equivalence only holds for three random variables $(p=3)$. For $p=4$, Example 3.6 provides a counterexample. In general, only one implication holds, namely, the CStree model $\mathcal{M}(\mathcal{T})$ is balanced whenever all minimal contexts are perfect (Theorem 4.5).

# 3. Decomposable CSmodels in three Variables 

Our subject of study from this point forward are balanced CStree models, the combinatorics of their context-specific DAG representations and the properties of their defining equations. Our results in Section 5 show that the properties of these models closely mirror those of decomposable DAG models. Therefore we introduce the following definition.

Definition 3.1. A decomposable context-specific model (decomposable CSmodel) is a balanced CStree model.

![img-2.jpeg](img-2.jpeg)

Figure 3. All CStrees with $p=3$ and variable ordering 123 which do not represent a DAG.

Consistent with our previous notation, we will denote such a model by $\mathcal{M}(\mathcal{T})$, where $\mathcal{T}$ denotes the associated balanced CStree. The goal of this section is to provide a complete description of CStree models in three random variables, with fixed variable ordering 123, and to prove the generalization of Theorem 2.15 for $p=3$. That is, we prove the following result.

Theorem 3.2. A CStree $\mathcal{T}$ with $p=3$ is balanced, i.e. $\mathcal{M}(\mathcal{T})$ is a decomposable CSmodel, if and only if all minimal context DAGs of $\mathcal{T}$ are perfect.

Before proving the above theorem, we classify all possible CStrees on three random variables along with their minimal contexts, taking advantage of the small value of $p$.

Example 3.3. We provide a list of all CStrees which are not staged tree representations of a DAG with causal ordering 123 (see Figure 3). In this case there are four families of CStrees.

Consider the two pairs of DAGs $\{([3],\{1 \rightarrow 2,1 \rightarrow 3,2 \rightarrow 3\}),([3],\{1 \rightarrow 3,2 \rightarrow 3\})\}$ and $\{(\{1,3\}, \varnothing),(\{2,3\}, \varnothing)\}$. Each of the four families is defined as follows: Choose two graphs $G_{1}, G_{2}$, one from each pair. Let $i \in\{1,2\}$ such that $i$ does not appear in the vertex set of $G_{2}$ and let $I \subsetneq\left[d_{i}\right]$. Now, consider the CStree defined by taking $G_{1}$ as its empty context DAG and $G_{2}$ as the minimal context DAG for the contexts $X_{i}=j$ for every $j \in I$. Depending on the choice of $G_{1}, G_{2}$ we get exactly the four families in Figure 3. The first family for example corresponds to choosing $G_{1}$ to be the complete graph, $G_{2}=(\{1,3\}, \varnothing)$ and some $I \subsetneq\left[d_{2}\right]$.

Note that any such choice does define a CStree and all contexts will be minimal contexts (except the empty context if the DAG is chosen to be the complete graph). If one would take $I=\left[d_{i}\right]$ this would no longer be true and the CStree would in fact be the staged tree representation of a DAG. The staged trees on the left of Figure 3 are examples in which all random variables are binary and such that the minimal context which is not the empty context is either $X_{1}=x_{1}^{1}$ or $X_{2}=x_{2}^{1}$.

In the first two families the empty context is not a minimal context as there are no CI relations that hold. We still draw the complete graph in this example for consistency.

Moreover, we can check that the first two families are balanced CStrees whereas the latter two are not. In the first two cases we also see that all minimal context DAGs are perfect which again is not the case for the latter two (cf. Theorems 4.5, 3.2).

Proposition 3.4. The list of CStrees in Example 3.3 is a complete list of CStrees with levels $\left(L_{1}, L_{2}, L_{3}\right) \sim\left(X_{1}, X_{2}, X_{3}\right)$ that are not staged tree representations of a DAG.

The proof can be found at the end of Section 4.
Lemma 3.5. Let $\mathcal{T}$ be a balanced CStree with $p=3$. If $X_{1} \perp X_{2}$, then $\mathcal{T}$ represents a $D A G$.
Proof. Since $X_{1} \perp X_{2}$, all vertices in the first level of $\mathcal{T}$ are in the same stage and $\varnothing \in \mathcal{C}_{\mathcal{T}}$. We claim that there are no other minimal contexts, besides the empty one. Since $\mathcal{T}$ is balanced by assumption, for any two vertices $v$ and $u$ in level 1 and $v_{i}, v_{j} \in \operatorname{ch}_{\mathcal{T}}(v), u_{i}, u_{j} \in \operatorname{ch}_{\mathcal{T}}(u)$ with $\theta\left(u \rightarrow u_{\ell}\right)=\theta\left(v \rightarrow v_{\ell}\right)$ for $\ell \in\left[d_{2}\right]$, we have $t\left(v_{i}\right) t\left(u_{j}\right)=t\left(v_{j}\right) t\left(u_{i}\right)$. Since $p=3$, we have one of the following cases:

$$
\begin{aligned}
& \text { 1) } t\left(v_{i}\right)=t\left(v_{j}\right) \Longrightarrow v_{i} \sim v_{j} \text { and } u_{i} \sim u_{j} \\
& \text { 2) } t\left(v_{i}\right) \neq t\left(v_{j}\right) \Longrightarrow u_{i} \sim v_{i} \text { and } u_{j} \sim v_{j}
\end{aligned}
$$

where $\sim$ denotes the equivalence relation of being in the same stage. Since $\mathcal{T}$ is a CStree, the first case implies that all children of any vertex $v$ in level 1 are in the same stage. But then $X_{2} \perp X_{3} \mid X_{1}$, so $X_{1}=\ell$ is not a minimal context for any $\ell \in\left[d_{1}\right]$. In the second case, we get that for any two vertices $v$ and $u$ in level 1 , we have $v^{\prime} \sim w^{\prime}$ for some $v^{\prime} \in \operatorname{ch}_{\mathcal{T}}(v)$ and $w^{\prime} \in \operatorname{ch}_{\mathcal{T}}(w)$. But then $X_{1} \perp X_{3} \mid X_{2}$, so again $X_{2}=\ell \notin \mathcal{C}_{\mathcal{T}}$ for any $\ell \in\left[d_{2}\right]$. We conclude $\mathcal{C}_{\mathcal{T}}=\{\varnothing\}$, so indeed $\mathcal{T}$ represents a DAG.

We are now ready to prove Theorem 3.2.
Proof of Theorem 3.2. We show in Theorem 4.5 that (for any $p$ ) if all minimal context DAGs of $\mathcal{T}$ are perfect, then $\mathcal{T}$ is balanced. Hence, it suffices to show the other implication. Let $\mathcal{T}$ be a balanced CStree with $p=3$. Assume there exists a minimal context DAG $G$ that is not perfect. This has to be the empty context DAG as other minimal context DAGs can only have two vertices. Hence, the empty minimal context DAG is $1 \rightarrow 3 \leftarrow 2$ which implies $X_{1} \perp X_{2}$. Using Lemma 3.5 it follows that $\mathcal{T}=\mathcal{T}_{G}$ is the staged tree representation of $G$. However, such a CStree is unbalanced by Theorem 2.15.

We have just observed that every balanced CStree has only perfect minimal contexts DAGs when $p=3$. This is no longer true for $p \geq 4$, as illustrated by the next example.

Example 3.6. We consider the binary CStree in Figure 4 on $p=4$ binary random variables which is equivalently given by its three minimal context DAGs. This CStree is balanced as one can check using Definition 2.13, but the empty minimal context DAG $G_{\varnothing}$ is not perfect

![img-3.jpeg](img-3.jpeg)

Figure 4. A balanced CStree with a non-perfect minimal context.
as the parents of 4 do not form a complete graph. Therefore, a straightforward generalization of Theorem 3.2 is not true.

This example can also be generalized to get more counterexamples for any $p \geq 4$ and with an arbitrarily large number of minimal context. We may note that the statement $X_{2} \pm X_{3} \mid X_{1}$ (which prevents the parents of 4 from forming a complete graph) is implied by the other two minimal contexts using absorption. We reveal why this happens in Section 5.

Remark 3.7. In the case $p=4$ the CStree in Figure 4 is essentially the only binary balanced CStree with a non-perfect minimal context (up to swapping the outcomes of $X_{1}$ in the minimal contexts). If we do not restrict to binary CStrees there exists a family of such CStrees with a non-perfect context DAG, it can be constructed similarly to Example 3.3.

Remark 3.8. Another characterizing property of decomposable graphical models is in terms of its maximum likelihood estimator (MLE). Decomposable graphical models are the only class of undirected graphical models whose MLE is a rational function [GMS06, Theorem 4.4]. The MLE of a Decomposable CSmodel is also a rational function, this follows from the fact that they are a subclass of staged tree models and staged tree models always have this property [DMS21].

# 4. Combinatorial Properties of balanced CStrees 

First, we study context subtrees of CStrees to understand which properties of CStrees are preserved when restricting to specific contexts. It turns out that any context subtree of a balanced CStree is itself balanced (Theorem 4.4) which can be seen as a generalization of the fact that removing a vertex from a perfect DAG results in a perfect DAG.

Second, we saw in Example 3.6 that a CStree can be balanced without its minimal context DAGs being perfect. The reverse implication does hold, i.e. if all minimal context DAGs are perfect, then the CStree is balanced (Theorem 4.5). The proof is mostly combinatorial in nature and does not make use of algebraic methods other than the definition of balancedness. Lastly, we establish Proposition 4.6 which will be used in the main proof of the last section. It gives an interpretation of the staging of a CStree in terms of CSI statements, as well as combinatorial conditions on minimal context DAGs for stagings to exist.
4.1. Context subtrees. We refer the reader back to Section 2.5 for the formal definition of a context subtree and give an illustrative example here. For any context $X_{C}=\mathbf{x}_{C}$, the subtree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ is a CStree, the DAG $G_{X_{C}=\mathbf{x}_{C}, \varnothing}$ denotes the empty context DAG of $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$.

![img-4.jpeg](img-4.jpeg)

Figure 5. The context subtree of the tree in Figure 6 for the context $X_{3}=0$, and its minimal context DAGs.

Example 4.1. We consider the CStree $\mathcal{T}$ in Figure 6 and construct the context subtree $\mathcal{T}_{X_{3}=0}$ given in Figure 5. We remove all subtrees with root $x_{1} x_{2} 1$ and $x_{1}, x_{2} \in\{0,1\}$ and contract the edges $x_{1} x_{2} \rightarrow x_{1} x_{2} 0$. The stage of the node resulting from this contraction is the stage of the node $x_{1} x_{2} 1$. The stages of level 2 do not exist anymore and they do not have any meaning in the construction of the context subtree. We could now construct the minimal context DAGs from this CStree. However, we will instead do this from the minimal context DAGs of the full tree. We check if any minimal context is invalid in the case $X_{3}=0$, i.e. is only valid for $X_{3}=1$, and discard this DAG. This however is not the case here. Now we remove the node 3 from any minimal context DAG, resulting in the collection of DAGs in Figure 5. In this case all non-empty contexts are in fact minimal contexts of the context subtree $\mathcal{T}_{X_{3}=0}$, however this is not true in general.

Moreover, we see that this context subtree $\mathcal{T}_{X_{3}=0}$ is different from the tree $\mathcal{T}_{G_{X_{3}=0, \varnothing}}$ (the staged tree representation of the empty context DAG) of which every stage is a singleton.

Lemma 4.2. Suppose $\mathcal{T}$ is a CStree with levels $\left(L_{1}, \ldots, L_{p}\right) \sim\left(X_{1}, \ldots, X_{p}\right)$.
(1) Every stage in $\mathcal{T}_{G_{\varnothing}}$ is a subset of a stage in $\mathcal{T}$.
(2) Suppose $C \subseteq[p]$ is a context with maximum index $k$ and let $v=x_{1} \ldots x_{q} \in V_{\mathcal{T}}$ be a vertex of $\mathcal{T}$ with $k \leq q$. Then for any $\mathbf{x}_{C} \in \mathcal{R}_{C}$ such that $\left(\mathbf{x}_{C}\right)_{i}=x_{i}$, we have the equality $\mathcal{T}_{v}=\left(\mathcal{T}_{X_{C}=\mathbf{x}_{C}}\right)_{v}$. Since $t_{\mathcal{T}}(v)$ only depends on the subtree $\mathcal{T}_{v}$, it follows that $t_{\mathcal{T}}(v)=t_{\mathcal{T}_{X_{C^{\prime}}}=\mathbf{x}_{C^{\prime}}}(v) \in \mathbb{R}\left[\Theta_{\mathcal{T}_{v}}\right]$.

Proof. (1) Let $S$ be a stage in $\mathcal{T}_{G_{\varnothing}}$ immediately preceding the level of the variable $X_{k}, k \in[p]$. Since $\mathcal{T}_{G_{\varnothing}}$ represents a DAG, the stage defining context $X_{A}=\mathbf{x}_{A}$ of $S$ satisfies $A=\mathrm{pa}_{G_{\varnothing}}(k)$ and $\mathbf{x}_{A} \in \mathcal{R}_{A}$. Thus, as a subset of vertices in $\mathcal{T}$,

$$
S=\bigcup_{\mathbf{y} \in \mathcal{R}_{[k-1] \backslash A}}\left\{\mathbf{x}_{A} \mathbf{y}\right\}
$$

for some $\mathbf{x}_{A} \in \mathcal{R}_{A}$. By the ordered Markov property in $G_{\varnothing}, G_{\varnothing}$ encodes the CI relation $X_{k} \mathbb{L}$ $X_{[k-1] \backslash A} \mid X_{A}$. This CI statement in $G_{\varnothing}$ corresponds to the CI statement $X_{k} \mathbb{L} X_{[k-1] \backslash A} \mid X_{A}$ in $\mathcal{T}$. Thus, by [DS22, Theorem 3.3] $X_{k} \mathbb{L} X_{[k-1] \backslash A} \mid X_{A}$ holds in $\mathcal{T}$. By specialization to $X_{A}=\mathbf{x}_{A}$, the statement $X_{k} \mathbb{L} X_{[k-1] \backslash A} \mid X_{A}=\mathbf{x}_{A}$ holds in $\mathcal{T}$. The fact that this latter statement holds in $\mathcal{T}$, implies that the nodes in $S$ must be a subset of a stage in $\mathcal{T}$.

(2) The vertices of the two trees are the same. A stage in the tree $\mathcal{T}_{v}$ is defined by a statement $X_{j} \mathbb{L} X_{[j-1] \backslash([q], D)} \mid X_{D}=\mathbf{x}_{D}$ for some $j>q$ and $D \subseteq[j-1] \backslash[q]$. A stage in the tree $\left(\mathcal{T}_{X_{C}=\mathbf{x}_{C}}\right)_{v}$ is defined by exactly the same kind of statement since $C \subseteq[k] \subseteq[q]$.

Lemma 4.2 (1) says that every CStree $\mathcal{T}$ is a coarsening of the CStree $\mathcal{T}_{G_{\varnothing}}$, as every stage of $\mathcal{T}$ is the union of possibly several stages in $\mathcal{T}_{G_{\varnothing}}$. This coarsening is a result of other minimal context DAGs entailing more CSI statements. Hence, if $\mathcal{T}=\mathcal{T}_{G_{\varnothing}}$ all CSI statements implied by $\mathcal{T}$ are specializations of CI statements also implied by $\mathcal{T}$.

We recall a useful lemma to prove balancedness.
Lemma 4.3 ([DS23, Lemma 3.2]). Let $G=([p], E)$ be a $D A G$ and assume $\pi=12 \cdots p$ is a linear extension of $G$. Then $\mathcal{T}_{G}$ is balanced if and only if for every pair of vertices in the same stage with $v=x_{1} \cdots x_{i}, w=x_{1}^{\prime} \cdots x_{i}^{\prime} \in \mathcal{R}_{\{i\}}$, there exists a bijection

$$
\begin{aligned}
\Phi: \mathcal{R}_{[p] \backslash[i+1]} \times \mathcal{R}_{[p] \backslash[i+1]} & \rightarrow \mathcal{R}_{[p] \backslash[i+1]} \times \mathcal{R}_{[p] \backslash[i+1]} \\
\left(y_{i+2} \cdots y_{p}, y_{i+2}^{\prime} \cdots y_{p}^{\prime}\right) & \mapsto\left(z_{i+2} \cdots z_{p}, z_{i+2}^{\prime} \cdots z_{p}^{\prime}\right)
\end{aligned}
$$

such that for all $k \geq i+2$ and all $s \neq r \in\left[d_{i+1}\right]$

$$
\begin{aligned}
& f\left(y_{k} \mid\left(x_{1} \cdots x_{i}, s, y_{i+2} \cdots y_{p}\right)_{\mathrm{pa}(k)}\right) f\left(y_{k}^{\prime} \mid\left(x_{1}^{\prime} \cdots x_{i}^{\prime}, r, y_{i+2}^{\prime} \cdots y_{p}^{\prime}\right)_{\mathrm{pa}(k)}\right) \\
& \quad=f\left(z_{k} \mid\left(x_{1}^{\prime} \cdots x_{i}^{\prime}, s, z_{i+2} \cdots z_{p}\right)_{\mathrm{pa}(k)}\right) f\left(z_{k}^{\prime} \mid\left(x_{1} \cdots x_{i}, r, z_{i+2}^{\prime} \cdots z_{p}^{\prime}\right)_{\mathrm{pa}(k)}\right)
\end{aligned}
$$

Theorem 4.4. If a CStree $\mathcal{T}$ is balanced, then so is $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ for every context $X_{C}=\mathbf{x}_{C}$.
Proof. Let $\overline{\mathcal{T}}:=\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$. Let $k \in[p] \backslash C$ and suppose $v=x_{1} \ldots x_{k-1}$ and $w=y_{1} \cdots y_{k-1}$ are two vertices in the same stage in $\overline{\mathcal{T}}$ with $x_{i}=y_{i}$ for $i \in C \cap[k-1]$. Note that $v, w$ are also in the same stage in $\mathcal{T}$ since $k \notin C$.

Then their children in $\mathcal{T}$ and $\overline{\mathcal{T}}$ are

$$
\begin{aligned}
\operatorname{ch}(v) & =\left\{x_{1} \cdots x_{k-1} s: s \in\left[d_{k}\right]\right\} \\
\operatorname{ch}(w) & =\left\{y_{1} \cdots y_{k-1} s: s \in\left[d_{k}\right]\right\}
\end{aligned}
$$

Let $v_{1}, v_{2} \in \operatorname{ch}(v)$ and $w_{1}, w_{2} \in \operatorname{ch}(w)$ be such that $\theta\left(v \rightarrow v_{i}\right)=\theta\left(w \rightarrow w_{i}\right),(i=1,2)$. Since CStrees are compatibly labeled, then

$$
\begin{array}{ll}
v_{1}=x_{1} \cdots x_{k-1} s, & v_{2}=x_{1} \cdots x_{k-1} r \\
w_{1}=y_{1} \cdots y_{k-1} s, & w_{2}=y_{1} \cdots y_{k-1} r
\end{array}
$$

for some $s, r \in\left[d_{k}\right]$. We want to show $t_{\overline{\mathcal{T}}}\left(v_{1}\right) t_{\overline{\mathcal{T}}}\left(w_{2}\right)=t_{\overline{\mathcal{T}}}\left(w_{1}\right) t_{\overline{\mathcal{T}}}\left(v_{2}\right)$. Choose a monomial on the left-hand-side. This corresponds to a product of edge labels of two paths $\lambda_{1}^{\prime}$ and $\lambda_{2}^{\prime}$ in $\overline{\mathcal{T}}, \lambda_{1}^{\prime}$ is a path from $v_{1}$ to a leaf and $\lambda_{2}^{\prime}$ is a path from $w_{2}$ to a leaf. Each leaf in $\overline{\mathcal{T}}$ is also a leaf in $\mathcal{T}$ (Section 2.4). In $\mathcal{T}$ there exists a directed path $\lambda_{1}$ from $v_{1}$ to the leaf using all edges in $\lambda_{1}^{\prime}$ and a directed path $\lambda_{2}$ from $w_{2}$ to the other leaf using $\lambda_{2}^{\prime}$.

Since $v, w$ are in the same stage in $\overline{\mathcal{T}}$, they are also in the same stage in $\mathcal{T}$. The balanced condition in $\mathcal{T}$ implies

$$
t_{\mathcal{T}}\left(x_{1} \cdots x_{k-1} s\right) t_{\mathcal{T}}\left(y_{1} \cdots y_{k-1} r\right)=t_{\mathcal{T}}\left(x_{1} \cdots x_{k-1} r\right) t_{\mathcal{T}}\left(y_{1} \cdots y_{k-1} s\right)
$$

Choose the product of monomials on the left hand side of this equation that is the product of the edge labels in the concatenation of paths $\lambda_{1} \lambda_{2}$ and denote it by $\theta\left(\lambda_{1}\right) \theta\left(\lambda_{2}\right)$. Since $\mathcal{T}$ is balanced, it follows from the bijection in Lemma 4.3 that there exists a product $\theta\left(\lambda_{3}\right) \theta\left(\lambda_{4}\right)$

corresponding to paths $\lambda_{3}, \lambda_{4}$ in $\mathcal{T}$ from $v_{2}$ to a leaf and $w_{1}$ to a leaf on the right-hand side of (3) such that

$$
\theta\left(\lambda_{1}\right) \theta\left(\lambda_{2}\right)=\theta\left(\lambda_{3}\right) \theta\left(\lambda_{4}\right)
$$

We claim that the paths $\lambda_{3}, \lambda_{4}$ are paths in $\overline{\mathcal{T}}$, i.e. the nodes in the paths $\lambda_{3}, \lambda_{4}$ contract to nodes in $\overline{\mathcal{T}}$. Let $j \in[p] \backslash[k]$ and denote by $e_{i, j}$ the edge of the path $i,(i=1,2,3,4)$ from level $j$ to level $j+1$. The fact that $\mathcal{T}$ is stratified and (4) holds, implies

$$
\theta\left(e_{1, j}\right) \theta\left(e_{2, j}\right)=\theta\left(e_{3, j}\right) \theta\left(e_{4, j}\right) \text { for all } j \in[p] \backslash[k]
$$

If $j+1 \in C$ then the edges $e_{1, j}, e_{2, j}$ point to the same outcome $\left(\mathrm{x}_{C}\right)_{j+1}$. From (5) and since $\mathcal{T}$ is compatibly labeled, different outcomes can never have equal edge labels, thus $e_{3, j}, e_{4, j}$ must also point to the outcome $\left(\mathrm{x}_{C}\right)_{j+1}$. This shows $\lambda_{3}, \lambda_{4}$ are paths in $\overline{\mathcal{T}}$.

Finally, if $j+1 \notin C$ then (5) implies that the product of the edge labels of the restrictions $\lambda_{3}^{\prime}, \lambda_{4}^{\prime}$ of $\lambda_{3}, \lambda_{4}$ to paths in $\overline{\mathcal{T}}$ is equal to the product of the edge labels of $\lambda_{1}^{\prime}, \lambda_{2}^{\prime}$. This establishes a bijection between terms on the right-hand side and the left-hand side of $t_{\bar{T}}\left(v_{1}\right) t_{\bar{T}}\left(w_{2}\right)=t_{\bar{T}}\left(w_{1}\right) t_{\bar{T}}\left(v_{2}\right)$, which means $\overline{\mathcal{T}}$ is balanced.
4.2. Decomposable DAG models and decomposable CSmodels. We start by proving the one-sided generalization of Theorem 3.2 and Theorem 2.15 to CStrees.

Theorem 4.5. Let $\mathcal{T}$ be a CStree with only perfect minimal contexts. Then $\mathcal{T}$ is balanced.
Proof. Let $v=x_{1} \ldots x_{k-1}, w=y_{1} \ldots y_{k-1} \in V_{\mathcal{T}}$ be two vertices in the same stage $S$ in $\mathcal{T}$. Then $S$ has a stage defining context $C$ that entails the CSI relation

$$
X_{k} \Perp X_{[k-1 \backslash C} \mid X_{C}=\mathrm{x}_{C}
$$

for some $\mathbf{x}_{C} \in \mathcal{R}_{C}$. By definition $C \subseteq[k-1]$, and from [DS22, Lemma 3.2] there exists a minimal context $C^{\prime} \subseteq C$ such that

$$
X_{k} \Perp X_{[k-1] \backslash C} \mid X_{C \backslash C^{\prime}}, X_{C^{\prime}}=\mathrm{x}_{C^{\prime}}
$$

holds with $\mathbf{x}_{C^{\prime}}=\left(\mathbf{x}_{C}\right)_{C^{\prime}}$. Every node in $S$ contains the context $\mathbf{x}_{C^{\prime}}$, hence every node in $S$ appears in $\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}$ and by construction $S$ is a stage in $\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}$. We claim that $v$ and $w$ are also in the same stage in $\mathcal{T}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}$ :

By [DS23, Proposition 2.2], this holds if and only if $(v)_{\mathrm{pa}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}(k)}=(w)_{\mathrm{pa}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}(k)}$. That is, the entries of $v$ and $w$ agree for the indices in $\mathrm{pa}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}(k)$. Let $i \in \mathrm{pa}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}(k)$ then $X_{k} \Perp X_{i} \mid X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}$. Therefore $i \notin[k-1] \backslash C$, i.e. $i \in C \backslash C^{\prime}$ because we are in the context $X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}$. Since $C$ is the stage defining context of $S$, we have $x_{i}=y_{i}$.

Since $G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}$ is perfect by assumption, the nodes $v, w$ are balanced in the CStree $\overline{\mathcal{T}}:=$ $\mathcal{T}_{G_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}$ by [DS23, Theorem 3.1]. This means that for any $v_{1}, v_{2} \in \operatorname{ch}_{\bar{T}}(v)$ and $w_{1}, w_{2} \in$ $\operatorname{ch}_{\bar{T}}(w)$ with $\theta_{\bar{T}}\left(v \rightarrow v_{i}\right)=\theta_{\bar{T}}\left(w \rightarrow w_{i}\right),(i=1,2)$ the following equation holds

$$
t_{\bar{T}}\left(v_{1}\right) t_{\bar{T}}\left(w_{2}\right)=t_{\bar{T}}\left(v_{2}\right) t_{\bar{T}}\left(w_{1}\right)
$$

in $\mathbb{R}\left[\Theta_{\bar{T}}\right]$. Since there is a surjective ring homomorphism $\mathbb{R}\left[\Theta_{\bar{T}}\right] \rightarrow \mathbb{R}\left[\Theta_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\right]$ the same equation

$$
t_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\left(v_{1}\right) t_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\left(w_{2}\right)=t_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\left(v_{2}\right) t_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\left(w_{1}\right)
$$

holds in $\mathbb{R}\left[\Theta_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}\right]$. By Lemma 4.2 (ii) we have $t_{\mathcal{T}}(v)=t_{\mathcal{T}_{X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}}}(v)$ and hence the equality

$$
t_{\mathcal{T}}\left(v_{1}\right) t_{\mathcal{T}}\left(w_{2}\right)=t_{\mathcal{T}}\left(v_{2}\right) t_{\mathcal{T}}\left(w_{1}\right)
$$

holds in $\mathbb{R}\left[\Theta_{\mathcal{T}}\right]$, i.e. the nodes $v, w$ are balanced.
Proposition 4.6. Let $\mathcal{T}$ be a CStree. Let $A, B, C \subseteq[p]$ be pairwise disjoint with $A \cup B \cup C=$ $[k-1]$ and fix $\mathbf{x}_{A} \in \mathcal{R}_{A}, \mathbf{x}_{B} \in \mathcal{R}_{B}, \mathbf{x}_{C} \in \mathcal{R}_{C}$. Then the following rule holds for the CSI statements in $\mathcal{T}$ :

$$
X_{k} \mathbb{1} X_{A} \mid X_{B \cup C}=\mathbf{x}_{B} \mathbf{x}_{C} \text { and } X_{k} \mathbb{1} X_{B} \mid X_{A \cup C}=\mathbf{x}_{A} \mathbf{x}_{C} \Rightarrow X_{k} \mathbb{1} X_{A \cup B} \mid X_{C}=\mathbf{x}_{C}
$$

Proof. In level $k-1$ we have the two stages

$$
S_{1}=\bigcup_{\mathbf{y}_{A} \in \mathcal{R}_{A}}\left\{\mathbf{y}_{A} \mathbf{x}_{B} \mathbf{x}_{C}\right\}, \quad S_{2}=\bigcup_{\mathbf{y}_{B} \in \mathcal{R}_{B}}\left\{\mathbf{x}_{A} \mathbf{y}_{B} \mathbf{x}_{C}\right\}
$$

However, these are both contained in a single stage: Both contain the element $\mathbf{x}_{A} \mathbf{x}_{B} \mathbf{x}_{C}$. But different stages cannot intersect, hence the two are contained in a single stage $S$.

Let $\mathbf{y}_{A} \neq \mathbf{x}_{A}$ and $\mathbf{y}_{B} \neq \mathbf{x}_{B}$. The elements $\mathbf{x}_{A} \mathbf{y}_{B} \mathbf{x}_{C}$ and $\mathbf{y}_{A} \mathbf{x}_{B} \mathbf{x}_{C}$ are contained in $S$ and therefore $\mathbf{z}_{A} \mathbf{z}_{B} \mathbf{x}_{C} \in S$ for every $\mathbf{z}_{A} \in \mathcal{R}_{A}, \mathbf{z}_{B} \in \mathcal{R}_{B}$. But this means $X_{k} \mathbb{1} X_{A \cup B} \mid X_{C}=$ $\mathbf{x}_{C}$.

In terms of context DAGs the last lemma says the following: If in a context DAG $G_{X_{C}=\mathbf{x}_{C}, \varnothing}$ there is an edge $i \rightarrow j$, i.e. $X_{i} \mathbb{1} X_{j} \mid X_{C}=\mathbf{x}_{C}$, but $X_{i} \mathbb{1} X_{j} \mid X_{C}=\mathbf{x}_{C}, X_{C^{\prime}}=\mathbf{x}_{C^{\prime}}$, then for every $v \in C^{\prime}$ there is an edge $v \rightarrow j$. The lemma can also be understood as a stronger but slightly different version in CStrees of the intersection axiom

$$
X_{A} \mathbb{1} X_{B} \mid X_{S \cup D}, X_{C}=\mathbf{x}_{C}, X_{A} \mathbb{1} X_{D} \mid X_{S \cup B}, X_{C}=\mathbf{x}_{C} \Rightarrow X_{A} \mathbb{1} X_{B \cup D} \mid X_{S}, X_{C}=\mathbf{x}_{C}
$$

as it only requires the first two CSI statements to each hold in one context $X_{D}=\mathbf{x}_{D}$ and $X_{B}=\mathbf{x}_{B}$.
Example 4.7. Consider a CStree $\mathcal{T}$ with empty minimal context DAG $G_{\varnothing}=([4],\{1 \rightarrow$ $2,2 \rightarrow 3,2 \rightarrow 4\})$. Lemma 4.6 implies that this CStree is in fact the staged tree representation of the DAG $G_{\varnothing}$. Indeed, there is no vertex with at least two incoming edges which implies that any CSI statement in $\mathcal{T}$ is already a specialization of a CI statement.

Using these observations, one can see that the CStrees given in Example 3.3 are in fact all CStrees on $p=3$ variables.
Proof of Proposition 3.4. Let $G$ be the empty context DAG of the CStree $\mathcal{T}$. If there is no vertex with two incoming edges, the CStree is the staged tree representation of a DAG by Proposition 4.6. Thus either the empty context DAG ist $1 \rightarrow 3 \leftarrow 2$ or the complete graph on three vertices. In either case by the same observation, the only other context DAGs are DAGs on the two vertices 1,3 or 2,3 . In order to imply a CSI statement they cannot contain the edge.

Assume there is a CStree with edges $1 \rightarrow 3,2 \rightarrow 3$ in the empty context DAG and at least two more minimal contexts $X_{1}=x_{1}^{i}$ and $X_{2}=x_{2}^{j}$ for some outcomes of $X_{1}$ and $X_{2}$. We claim that this is impossible. Indeed, we have the following CSI statements in $\mathcal{T}$ :

$$
X_{3} \mathbb{1} X_{2} \mid X_{1}=x_{1}^{i} \quad \text { and } \quad X_{3} \mathbb{1} X_{1} \mid X_{2}=x_{2}^{j}
$$

Using Proposition 4.6 again, we see that the CSI statement $X_{3} \mathbb{1} X_{1,2}$ holds, i.e. the empty context DAG does not have the edges $1 \rightarrow 3,2 \rightarrow 3$, a contradiction. Thus either all minimal contexts fix outcomes of $X_{1}$ or all fix outcomes of $X_{2}$.

To generalize the other implication of Theorem 2.15 we use an algebraic approach presented in the next section.

# 5. Algebraic characterization of decomposable context-specific models 

The core of this paper is Theorem 5.3 as it provides a complete characterization of the CSI statements that hold in a decomposable CSmodel. From this theorem we deduce the main properties of decomposable CSmodels stated in the introduction. In particular, it lays down the technical foundation upon which we build our main algebraic result, Theorem 5.13, which shows that every decomposable CSmodel can be defined by a collection of perfect DAGs. Theorem 5.3 states that for a balanced CStree $\mathcal{T}$, the polynomials associated to saturated CSI statements are a generating set of the prime ideal $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ that defines $\mathcal{M}(\mathcal{T})$ implicitly. This is precisely the case for perfect DAG models, see [GMS06, Theorem 4.4], which once again highlights the important role that decomposable CSmodels play in generalizing the algebraic properties of single DAGs to collections of DAGs in the context-specific setting. The proof of this result uses the algebraic notion of the toric fiber product, first introduced in [Sul07].

For any collection $\mathcal{C}$ of CSI statements in a CStree $\mathcal{T}$, we define the ideal $I_{\mathcal{C}}$ to be the ideal generated by the polynomials associated to all CSI statements in $\mathcal{C}$ as defined in Section 2.2.
5.1. Setup. Let $\mathcal{T}$ be a balanced CStree, $\overline{\mathcal{T}}$ the subtree of $\mathcal{T}$ up to level $p-1$ and $S_{1}, \ldots, S_{r}$ the stages in $\mathcal{T}$ in level $p-1$. Let $\mathcal{T}_{p}=\bigcup_{i \in[r]} \mathcal{B}_{i}$, where each $\mathcal{B}_{i}$ is a one-level tree together with its edge labels as in [AD21, Section 3]. Consider the rings

$$
\begin{aligned}
& \mathbb{R}[\overline{\mathcal{T}}]:=\mathbb{R}\left[p_{\mathbf{x}}^{i}: i \in[r], \mathbf{x} \in S_{i}\right], \\
& \mathbb{R}\left[\mathcal{T}_{p}\right]:=\mathbb{R}\left[p_{k}^{i}: i \in[r], k \in\left[d_{p}\right]\right], \\
& \mathbb{R}[\mathcal{T}]:=\mathbb{R}\left[p_{\mathbf{x} k}^{i}: i \in[r], \mathbf{x} \in S_{i}, k \in\left[d_{p}\right]\right]
\end{aligned}
$$

with multigrading $\operatorname{deg}\left(p_{\mathbf{x}}^{i}\right)=\operatorname{deg}\left(p_{k}^{i}\right)=\operatorname{deg}\left(p_{\mathbf{x} k}^{i}\right), i \in[r], \mathbf{x} \in S_{i}, k \in\left[d_{p}\right]$ where $\mathcal{A}=$ $\left\{e_{1}, \ldots, e_{r}\right\}$ and $e_{i}$ is the $i$-th standard unit vector in $\mathbb{Z}^{r}$. Note that the rings $\mathbb{R}[\mathcal{T}]$ and $\mathbb{R}[D]$ are the same, except the former is multigraded. Consider the ring homomorphism

$$
\mathbb{R}[\mathcal{T}] \rightarrow \mathbb{R}[\overline{\mathcal{T}}] \otimes \mathbb{R}\left[\mathcal{T}_{p}\right], \quad p_{\mathbf{x} k}^{i} \mapsto p_{\mathbf{x}}^{i} \otimes p_{k}^{i} \quad\left(i \in[r], \mathbf{x} \in S_{i}, k \in\left[d_{p}\right]\right)
$$

Following [Sul07], we call the kernel of this map Quad. It is given by

$$
\text { Quad }=\left\langle p_{\mathbf{x} k_{1}}^{i} p_{\mathbf{y} k_{2}}^{i}-p_{\mathbf{x} k_{2}}^{i} p_{\mathbf{y} k_{1}}^{i}: k_{1} \neq k_{2} \in\left[d_{p}\right], \mathbf{x}, \mathbf{y} \in S_{i}, i \in[r]\right\rangle
$$

Note that the generators of Quad are the $2 \times 2$ minors of the matrices $\left(p_{\mathbf{x} k}^{i}\right)_{\mathbf{x} \in S_{i}, k \in\left[d_{p}\right]}$ for all $i \in[r]$. Now, consider the ring homomorphism

$$
\mathbb{R}[\mathcal{T}] \rightarrow \mathbb{R}[\overline{\mathcal{T}}] / \operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right) \otimes \mathbb{R}\left[\mathcal{T}_{p}\right], \quad p_{\mathbf{x} k}^{i} \mapsto p_{\mathbf{x}}^{i} \otimes p_{k}^{i} \quad\left(i \in[r], \mathbf{x} \in S_{i}, k \in\left[d_{p}\right]\right)
$$

where $\psi_{\mathcal{T}}$ is the homomorphism defined in (2). The kernel of this map is the toric fiber product of $\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right)$ and the zero ideal $\langle 0\rangle \subseteq \mathbb{R}\left[\mathcal{T}_{p}\right]$, and is denoted by $\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right) \times_{\mathcal{A}}\langle 0\rangle$. By [AD21, Proposition 3.5], this toric fiber product is equal to $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ when $\mathcal{T}$ is balanced. The generators of $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ are obtained from two sets, namely $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\langle$ Quad, $\operatorname{Lift}(F)\rangle$, where $F$ is a set of generators of $\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right)$ and
$\operatorname{Lift}(F):=\left\{p_{\mathbf{x}_{1} k_{1}}^{i} p_{\mathbf{y}_{1} k_{2}}^{j}-p_{\mathbf{x}_{2} k_{1}}^{i} p_{\mathbf{y}_{2} k_{2}}^{j}: \mathbf{x}_{1}, \mathbf{x}_{2} \in S_{i}, \mathbf{y}_{1}, \mathbf{y}_{2} \in S_{j}, k_{1}, k_{2} \in\left[d_{p}\right], p_{\mathbf{x}_{1}}^{i} p_{\mathbf{y}_{1}}^{j}-p_{\mathbf{x}_{2}}^{i} p_{\mathbf{y}_{2}}^{j} \in F\right\}$.
Note that the construction above relies heavily on the fact that $\mathcal{T}$ is balanced since this is the only case in which $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ and $\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right)$ are toric and $\mathcal{A}$-homogeneous.

![img-5.jpeg](img-5.jpeg)

Figure 6. Balanced CStree on five binary random variables whose empty context DAG is not perfect.
5.2. Main results. In what follows saturated CSI statements will be the main actors. Let $\mathcal{T}$ be a CStree with $p$ levels and let $\mathcal{M}(\mathcal{T})$ be the associated model. A saturated CSI statement is a CSI statement of the form $X_{A} \Perp X_{B} \mid X_{S}, X_{C}=\mathbf{x}_{C}$, where $A \cup B \cup C \cup S=[p]$. If $\mathcal{C}$ is a collection of saturated CSI statements then the ideal $I_{\mathcal{C}}$ is generated by binomials. Any ideal that is generated by binomials and in addition is prime is a toric ideal.
Definition 5.1. Let $\mathcal{C}$ be any collection of CSI statements of random variables $X_{1}, \ldots, X_{p}$. We define $\operatorname{Sat}(\mathcal{C})$ to be the set of all saturated CSI statements in $\mathcal{C}$. For a CStree $\mathcal{T}$ let $\operatorname{Sat}(\mathcal{T}):=\operatorname{Sat}(\mathcal{J}(\mathcal{T}))$ where $\mathcal{J}(\mathcal{T})$ denotes the set of all CSI statements that hold in $\mathcal{T}$. For a DAG $G$ we define $\operatorname{Sat}(G):=\operatorname{Sat}\left(\mathcal{T}_{G}\right)$. Since $\mathcal{J}\left(\mathcal{T}_{G}\right)=\operatorname{global}(G)$, we also get $\operatorname{Sat}(G)=\operatorname{Sat}(\operatorname{global}(G))$.

The proofs of the results in this section rely heavily on the toric fiber product construction. We motivate these results with the following concrete example.
Example 5.2 (Decomposable CSmodel with a non-perfect empty context). Consider the decomposable CSmodel given by the CStree in Figure 6 for $p=5$. It has four minimal contexts, namely,

$$
\mathcal{C}_{\mathcal{T}}=\left\{\varnothing, X_{1}=1, X_{1} X_{2}=01, X_{2}=0\right\}
$$

Only the non-empty minimal contexts are perfect, yet the tree is balanced. The CSI statements corresponding to the four minimal contexts are, respectively,

$$
\begin{array}{ll}
X_{3} \Perp X_{4} \mid X_{1} X_{2}, & X_{4} \Perp X_{5} \mid X_{2} X_{3}, X_{1}=1 \\
X_{4} \Perp X_{5} \mid X_{3}, X_{1} X_{2}=01, & X_{4} \Perp X_{5} \mid X_{1} X_{3}, X_{2}=0
\end{array}
$$

The last three statements, corresponding to the three perfect minimal contexts, are saturated. Applying the contraction axiom to each of these statements together with the appropriate specialization of the statement $X_{3} \Perp X_{4} \mid X_{1} X_{2}$ (corresponding to the empty context), we get the following three saturated statements

$$
X_{3} X_{5} \Perp X_{4} \mid X_{2}, X_{1}=1, X_{3} X_{5} \Perp X_{4} \mid X_{1} X_{2}=01, X_{3} X_{5} \Perp X_{4} \mid X_{1}, X_{2}=0
$$

These three saturated statements give rise to 24 polynomials, 8 of which coincide with stagedefining statements for level 5 . These 8 polynomials, one of which is

$$
p_{00000}^{1} p_{00011}^{1}-p_{00001}^{1} p_{00010}^{1}
$$

are precisely the polynomials in Quad. The remaining 16 polynomials, one of which is

$$
p_{00000}^{1} p_{00110}^{2}-p_{00010}^{1} p_{00100}^{2}
$$

are the polynomials in $\operatorname{Lift}(F)$, defined above. Hence, the 24 polynomials associated to the saturated statements are precisely the generators of $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$.

Turns out, the phenomenon in the example above can be generalized to all decomposable CSmodels. The next theorem is the technical foundation of this paper. It demonstrates the important role that saturated CSI statements play in the algebra of decomposable CSmodels and it also contains most of the technical work in its proof.

Theorem 5.3. If $\mathcal{M}(\mathcal{T})$ is a decomposable CSmodel, then $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ is generated by the quadratic binomials associated to all saturated CSI statements in $\mathcal{J}(\mathcal{T})$, i.e.

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=I_{\operatorname{Sat}(\mathcal{T})}
$$

Proof. The containment $I_{\operatorname{Sat}(\mathcal{T})} \subseteq \operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ holds because all polynomials associated to statements in $\mathcal{J}(\mathcal{T})$ belong to $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$. In particular, all binomials coming from saturated CSI statements are in $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$.

For the other containment we proceed by induction on the number of random variables in $\mathcal{T}$. The statement is trivially true for $p=1,2$. Suppose that $\mathcal{T}$ has $p$ levels, and any balanced CStree with less than $p$ levels satisfies the statement. Let $\overline{\mathcal{T}}$ be the subtree of $\mathcal{T}$ up to level $p-1$. Then $\overline{\mathcal{T}}$ is balanced, thus by induction hypothesis $\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right)$ is generated by a set $F$ of binomials associated to saturated CSI statements in the variables $X_{[p-1]}$. Moreover,

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\operatorname{ker}\left(\psi_{\overline{\mathcal{T}}}\right) \times_{\mathcal{A}}\langle 0\rangle=\langle\operatorname{Quad}, \operatorname{Lift}(F)\rangle
$$

Hence, it suffices to prove that Quad and $\operatorname{Lift}(F)$ are polynomials associated to saturated CSI statements in the variables $X_{[p]}$. Let $S_{1}, \ldots, S_{r}$ be the stages of level $p-1$ in $\mathcal{T}$. For all $i \in[r]$, let $X_{C_{i}}=\mathbf{x}_{C_{i}}$ be the stage defining context of the stage $S_{i}$. Recall that

$$
\text { Quad }=\left\langle p_{\mathbf{x} k_{1}}^{i} p_{\mathbf{y} k_{2}}^{i}-p_{\mathbf{x} k_{2}}^{i} p_{\mathbf{y} k_{1}}^{i}: k_{1} \neq k_{2} \in\left[d_{p}\right], \mathbf{x}, \mathbf{y} \in S_{i}, i \in[r]\right\rangle
$$

which, by (1), is precisely the set of binomials associated to the saturated CSI statements $X_{p} \Perp X_{[p-1] \backslash C_{i}} \mid X_{C_{i}}=\mathbf{x}_{C_{i}}$ for all $i \in[r]$.

Since $\mathcal{T}$ is balanced, $F$ is a set of $\mathcal{A}$-homogeneous binomials. Let $g \in F$, then it is associated to a CSI statement $X_{A} \Perp X_{B} \mid X_{D}, X_{C}=\mathbf{x}_{C}$ with $A \cup B \cup C \cup D=[p-1]$ and $\mathbf{x}_{C} \in \mathcal{R}_{C}$ as in (1).

Choose $\mathbf{y}_{A}, \mathbf{y}_{A}^{\prime} \in \mathcal{R}_{A}$ and $\mathbf{y}_{B}, \mathbf{y}_{B}^{\prime} \in \mathcal{R}_{B}$ such that for all $i \in A,\left(\mathbf{y}_{A}\right)_{i} \neq\left(\mathbf{y}_{A}^{\prime}\right)_{i}$, and for all $i \in B,\left(\mathbf{y}_{B}\right)_{i} \neq\left(\mathbf{y}_{B}^{\prime}\right)_{i}$. Consider the polynomial

$$
h=p_{\mathbf{y}_{A} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D}}^{k} p_{\mathbf{y}_{A}^{\prime} \mathbf{y}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D}}^{t}-p_{\mathbf{y}_{A}^{\prime} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D}}^{m} p_{\mathbf{y}_{A} \mathbf{y}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D}}^{n}
$$

associated to the same CSI statement as $g$ and its lift

$$
h_{z_{1}, z_{2}}=p_{\mathbf{y}_{A} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{k} p_{\mathbf{y}_{A}^{\prime} \mathbf{y}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{t}-p_{\mathbf{y}_{A}^{\prime} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{m} p_{\mathbf{y}_{A} \mathbf{y}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{n}, \quad z_{1}, z_{2} \in\left[d_{p}\right]
$$

Since $h$ is $\mathcal{A}$-homogeneous, either $(k, \ell)=(m, n)$ or $(k, \ell)=(n, m)$. Assume it is the former. By the assignment of the grading, it follows that $\left(\mathbf{y}_{A} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}\right)_{C_{k}}=\left(\mathbf{y}_{A}^{\prime} \mathbf{y}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}\right)_{C_{k}}$ because they are in the same stage, therefore $C_{k} \cap A=\varnothing$. The CSI statement associated to the stage $S_{k}$ is $X_{p} \Perp X_{[p-1] \backslash C_{k}} \mid X_{C_{k}}=\mathbf{x}_{C_{k}}$, this entails $X_{p} \Perp X_{A} \mid X_{B}=\mathbf{y}_{B}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}$ because $C_{k} \cap A=\varnothing$.

For every $\mathbf{z}_{B}, \mathbf{z}_{B}^{\prime} \in \mathcal{R}_{B}$ there exist $\alpha, \beta \in[r]$ such that the binomial is either

$$
p_{\mathbf{y}_{A} \mathbf{z}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{\alpha} p_{\mathbf{y}_{A}^{\prime} \mathbf{z}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{\beta}-p_{\mathbf{y}_{A}^{\prime} \mathbf{z}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{\alpha} p_{\mathbf{y}_{A} \mathbf{z}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{\beta}
$$

or

$$
p_{\mathbf{y}_{A} \mathbf{z}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{\alpha} p_{\mathbf{y}_{A}^{\prime} \mathbf{z}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{\beta}-p_{\mathbf{y}_{A}^{\prime} \mathbf{z}_{B} \mathbf{x}_{C} \mathbf{x}_{D} z_{1}}^{\beta} p_{\mathbf{y}_{A} \mathbf{z}_{B}^{\prime} \mathbf{x}_{C} \mathbf{x}_{D} z_{2}}^{\alpha}
$$

depending on which variables have the same degree.
Case 1: For every $\mathbf{z}_{B}$ and $\mathbf{z}_{B}^{\prime}$ entry-wise different, we have the first grading. Then by the same argument as for $\mathbf{y}_{B}, \mathbf{y}_{B}^{\prime}$ we get the saturated CSI statement $X_{p} \Perp X_{A} \mid X_{B}=$ $\mathbf{z}_{B}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}$ for all $\mathbf{z}_{B}$. Hence, by absorption we get

$$
X_{p} \Perp X_{A} \mid X_{B}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}
$$

Applying the contraction axiom to this statement and to $X_{A} \Perp X_{B} \mid X_{D}, X_{C}=\mathbf{x}_{C}$ we get the saturated CSI statement

$$
X_{A} \Perp X_{B \cup\{p\}} \mid X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}
$$

This statement entails all binomials in $\operatorname{Lift}(g)$, equivalently $\operatorname{Lift}(g) \subseteq I_{X_{A} \Perp X_{B \cup\{p\}} \mid X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}}$.
Case 2: There exists a pair $\mathbf{z}_{B}, \mathbf{z}_{B}^{\prime}$, entry-wise different, such that the binomial has the second grading. Using the same argument as above with $B$ instead of $A$, this implies the statement $X_{p} \Perp X_{B} \mid X_{A}=\mathbf{y}_{A}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}$. Combining this statement with $X_{p} \Perp$ $X_{A} \mid X_{B}=\mathbf{y}_{B}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}$ and Proposition 4.6 we get

$$
X_{p} \Perp X_{A \cup B} \mid X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}
$$

By the weak union axiom, we get $X_{p} \Perp X_{A} \mid X_{B}, X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}$. As in Case 1, we obtain the CSI statement

$$
X_{A} \Perp X_{B \cup\{p\}} \mid X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}
$$

and the conclusion $\operatorname{Lift}(g) \subseteq I_{X_{A} \Perp X_{B \cup\{p\}} \mid X_{C \cup D}=\mathbf{x}_{C} \mathbf{x}_{D}}$ follows. The proof for the second choice of grading $(k, \ell)=(n, m)$ of $h$ is analogous, by swapping the roles of $A$ and $B$ in the above arguments.

Remark 5.4. The Theorem 5.3 implies that $\mathcal{V}\left(\operatorname{ker}\left(\psi_{\mathcal{T}}\right)\right)$ is the Zariski closure of $\mathcal{M}(\mathcal{T})$. Therefore Theorem 1.1 is also valid for distributions in the boundary of the probability simplex.

For the rest of this section, we can relax the assumption of working with minimal contexts. Let $\mathcal{T}$ be a CStree and $\mathcal{C}$ be any collection of contexts with associated DAGs $G_{X_{C}=\mathbf{x}_{C}}$, $X_{C}=\mathbf{x}_{C} \in \mathcal{C}$, such that $\mathcal{J}(\mathcal{T})=\cup_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}}$ global $\left(G_{X_{C}=\mathbf{x}_{C}}\right)$. That is, assume that the CSI statements that hold in $\mathcal{C}$ are the same CSI statements that hold in $\mathcal{T}$. The collection of minimal contexts is one such choice for $\mathcal{C}$.

Corollary 5.5. Let $\mathcal{M}(\mathcal{T})$ be a decomposable CSmodel. The ideal $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ is generated by the binomials associated to all saturated CSI statements that hold in the context DAGs $G_{X_{C}=\mathbf{x}_{C}}, X_{C}=\mathbf{x}_{C} \in \mathcal{C}$, i.e.

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{Sat}\left(G_{X_{C}=\mathbf{x}_{C}}\right)}
$$

Proof. This follows from the fact that $\mathcal{J}(\mathcal{T})=\cup_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} \mathcal{J}\left(X_{C}=\mathbf{x}_{C}\right)$ and Theorem 5.3.

Corollary 5.6. Let $\mathcal{M}(\mathcal{T})$ be a decomposable CSmodel. Then

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{global}\left(G_{X_{C}=\mathbf{x}_{C}}\right)}
$$

Proof. We show the following chain of inclusions

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{Sat}\left(G_{X_{C}=\mathbf{x}_{C}}\right)} \subseteq \sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{global}\left(G_{X_{C}=\mathbf{x}_{C}}\right)} \subseteq \operatorname{ker}\left(\psi_{\mathcal{T}}\right)
$$

which implies the theorem. The equality follows from Corollary 5.5 and the middle inclusion follows from the containment $\operatorname{Sat}\left(G_{X_{C}=\mathbf{x}_{C}}\right) \subseteq \operatorname{global}\left(G_{X_{C}=\mathbf{x}_{C}}\right)$ for all $X_{C}=\mathbf{x}_{C} \in \mathcal{C}$. For the last inclusion, let $J:=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\text {global }\left(G_{X_{C}=\mathbf{x}_{C}}\right)}$. From [DS22, Theorem 3.3], we know the equality

$$
\mathcal{V}(J) \cap \Delta_{\mid \mathcal{R} \mid-1}^{\circ}=\mathcal{V}\left(\operatorname{ker}\left(\psi_{\mathcal{T}}\right)\right) \cap \Delta_{\mid \mathcal{R} \mid-1}^{\circ}=\mathcal{M}(\mathcal{T})
$$

Since $\operatorname{ker} \psi_{\mathcal{T}}$ is a prime ideal, this implies that

$$
\begin{aligned}
J & \subseteq \mathcal{I}\left(\mathcal{V}(J) \cap \Delta_{\mid \mathcal{R} \mid-1}^{\circ}\right) \cap \mathbb{R}[D] \\
& =\mathcal{I}\left(\mathcal{V}\left(\operatorname{ker}\left(\psi_{\mathcal{T}}\right)\right) \cap \Delta_{\mid \mathcal{R} \mid-1}^{\circ}\right) \cap \mathbb{R}[D] \\
& =\mathcal{I}\left(\mathcal{V}\left(\operatorname{ker} \psi_{\mathcal{T}}\right)\right) \cap \mathbb{R}[D]=\operatorname{ker} \psi_{\mathcal{T}}
\end{aligned}
$$

where $\mathcal{I}(V)$ denotes the set of polynomials in $\mathbb{C}[D]$ that vanish on a set $V \subseteq \mathbb{C}^{|\mathcal{R}|}$.
5.3. Directed moralization for decomposable CSmodels. To create perfect DAGs from non-perfect ones we define a directed version of the moralization operation. We use this operation to show that decomposable CSmodels can be described by perfect DAGs. We start by recalling the definition of moralization and its connection to d-separation.
Definition 5.7. Let $G=([p], E)$ be a DAG. The moralization of $G$, denoted by $G^{m}$, is the undirected graph with the vertex set $[p]$ that has an undirected edge for every directed edge in $E$, and an undirected edge $(u, v)$ whenever $u \rightarrow w, v \rightarrow w$ are edges in $G$.
Proposition 5.8 ([Lau96, Proposition 3.25]). Let $G=([p], E)$ be a $D A G$ and $A, B, C$ be disjoint subsets of $[p]$. Then $C d$-separates $A$ and $B$ in $G$ if and only if $C$ separates $A$ and $B$ in the moralization $\left(G_{\operatorname{an}(A \cup B \cup C)}\right)^{m}$, where $G_{\operatorname{an}(A \cup B \cup C)}$ is the induced subgraph on the ancestors of $A \cup B \cup C$.
Definition 5.9. Let $G=([p], E)$ be a DAG. The directed moralization of $G$, denoted by $G^{d m}$, is the directed graph with the vertex set $[p]$ that has a directed edge for every directed edge in $E$, and a directed edge $u \rightarrow v$ whenever $u \rightarrow w, v \rightarrow w$ are edges in $G$ and $u<v$.
Remark 5.10. Note that the directed moralization of every DAG $G$ is indeed a DAG since our variables are topologically ordered, i.e. if $i \rightarrow j$ is an edge in $G$, then $i<j$. In case one wants to use directed moralization on a DAG $(V, E)$ with vertices $V$ and edges $E$ one has to fix an ordering of the variables.

Moreover, directed moralization produces a perfect DAG after applying the operation sufficiently many times. Since we can only add edges, applying the directed moralization $\binom{p}{2}$ times results in a perfect DAG.
Definition 5.11. Let $G=([p], E)$ be a DAG. We denote by $G^{\text {per }}$ the perfect DAG created from $G$ after applying the directed moralization $\binom{p}{2}$ times.

Remark 5.12. To produce a chordal graph to which a distribution in a DAG model $G$ is Markov, one can moralize $G$ and then take a triangulation of the resulting undirected graph. If an ordering of the vertices is fixed, this undirected graph can then be directed according to this ordering.

The graph $G^{\text {per }}$ is one possible perfect graph one may produce using a particular triangulation. Iterating directed moralizations in Definition 5.9 produces this triangulation on the skeleton of $G^{\text {per }}$.

The goal is to prove the following theorem about the generators of $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$. It implies that in any balanced CStree $\mathcal{T}$ we may replace all context DAGs $H$ by $H^{\text {per }}$ without changing the model.

Theorem 5.13. A CStree $\mathcal{T}$ is balanced if and only if

$$
\operatorname{ker}\left(\psi_{\mathcal{T}}\right)=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{Sat}\left(\left(G_{X_{C}}=\mathbf{x}_{C}\right)^{\text {per }}\right)}
$$

In particular, every decomposable CSmodel can be described by a collection of perfect DAGs.
Lemma 5.14. Let $G=([p], E)$ be a $D A G$ and let $S=X_{i} \mathbb{1} X_{j} \mid X_{[p] \backslash\{i, j\}}$ be a saturated CI statement entailed by $G$. Then $S \in \operatorname{Sat}(G) \backslash \operatorname{Sat}\left(G^{d m}\right)$ if and only if at least one of the following two statements holds.
(1) There exist $k, l \in[p]$ with $k>i, j$ and $l>k$ such that $G$ contains one of the following two graphs on the vertices $\{i, j, k, l\}$ as an induced subgraph.
![img-6.jpeg](img-6.jpeg)
(2) There exist $l_{1}, l_{2}, k \in[p]$ with $k>i, j$ and $l_{1}, l_{2}>k$ such that $G$ contains the following graph on the vertices $\left\{i, j, k, l_{1}, l_{2}\right\}$ as an induced subgraph.
![img-7.jpeg](img-7.jpeg)

Proof. Since $S$ holds in $G$, the vertices $i$ and $j$ do not have a common child by Proposition 5.8. However, they do have a common child after directed moralization. Assume this child is labeled $k$ with $k \in[p], k>i, j$. If $k$ is a child of one of $i$ or $j$ and the other edge is added by the directed moralization we have one of the graphs in (1) as a subgraph of $G$. Moreover, no other edge can exist in the induced subgraph on these four vertices since then $i, j$ would have a common child or be connected via an edge. If $k$ is not a child of either $i$ or $j$ in $G$ then the graph in (2) is a subgraph of $G$. Again other edges cannot exist for the same reason, hence this graph is the induced subgraph on these five vertices.

For the other direction note that if any of these graphs is an induced subgraph of $G$, then $\left(G^{d m}\right)^{m}$ has an edge between $i$ and $j$. Thus $S \notin \operatorname{Sat}\left(G^{d m}\right)$ by Proposition 5.8.

Let $G=([p], E)$ be a DAG and let $i, j \in[p]$ with no common child and not adjacent. We denote the number of pairs $k, l$ as in Lemma 5.14(1) by $n_{1}^{i, j}(G)$ and by $n_{2}^{i, j}(G)$ the number of triples $k, l_{1}, l_{2}$ as in Lemma $5.14(2)$.

Lemma 5.15. Let $G=([p], E)$ be a $D A G$ and let $i, j \in[p]$ with no common child and not adjacent. Let $k, l$ as in Lemma 5.14(1). Let $H$ be a subgraph of $G$ obtained by removing at least one of the edges in the induced subgraph on $\{i, j, k, l\}$. Then
(1) $n_{1}^{i, j}(H)<n_{1}^{i, j}(G)$ and
(2) $n_{1}^{i, j}(H)+n_{2}^{i, j}(H) \leq n_{1}^{i, j}(G)+n_{2}^{i, j}(G)$.

Assume $n_{1}^{i, j}(G)=0$. Let $k, l_{1}, l_{2}$ as in Lemma 5.14(2). Let $H$ be a subgraph of $G$ obtained by removing at least one of the edges in the induced subgraph on $\left\{i, j, k, l_{1}, l_{2}\right\}$. Then
(3) $n_{1}^{i, j}(H)=0$ and
(4) $n_{2}^{i, j}(H)<n_{2}^{i, j}(G)$.

Proof. (1): Assume there is a pair $k, l$ such that the induced subgraph on $\{i, j, k, l\}$ in $G$ is not of the form in Lemma 5.14(1) but the induced subgraph on these vertices in $H$ does have that form. Then the induced subgraph on $\{i, j, k, l\}$ in $G$ has at least one more edge. Since $i, j$ are not adjacent in $G$ by assumption, it has to be one of the edges $i \rightarrow l, j \rightarrow k$. But in both cases $i, j$ have a common child. When removing an edge contained in an induced subgraph on vertices $\{i, j, k, l\}$ as in Lemma 5.14(1) then the total number of such pairs in $H$ is strictly smaller.
(2) Assume we have a triple $k, l_{1}, l_{2}$ such that the induced subgraph on $\{i, j, k, l\}$ in $G$ is not of the form in Lemma 5.14(2) but the induced subgraph on these vertices in $H$ does have that form. With the same reasoning as above, exactly one of the two edges $i \rightarrow k$ or $j \rightarrow k$ must have been removed. Therefore, either the induced subgraph on $\left\{i, j, k, l_{1}\right\}$ or on $\left\{i, j, k, l_{2}\right\}$ in $G$ is of the form in Lemma 5.14(1). This shows that $n_{2}^{i, j}(H)-n_{2}^{i, j}(G)$ is at most $n_{1}^{i, j}(G)-n_{1}^{i, j}(H)$.
(3) We already saw in the proof of (1) that no new pair $k, l$ can emerge.
(4) If there was a triple $\left\{k, l_{1}, l_{2}\right\}$ in $H$ that has the form in Lemma 5.14(2), then it was already there in $G$ as the only edges that can be added to this subgraph not leading to a common child are $i \rightarrow k$ or $j \rightarrow k$. However, both imply $n_{1}^{i, j}(G) \geq 1$, a contradiction.

Proposition 5.16. Let $\mathcal{T}$ be a balanced CStree and let $X_{i} \perp X_{j}\left|X_{[p] \backslash\{i, j\}} \in \operatorname{Sat}\left(G_{\varnothing}\right) \backslash\right.$ $\operatorname{Sat}\left(\left(G_{\varnothing}\right)^{d m}\right)$. For every $\mathbf{x}_{[p] \backslash\{i, j\}} \in \mathcal{R}_{[p] \backslash\{i, j\}}$ the CSI statement $X_{i} \perp X_{j}\left|X_{[p] \backslash\{i, j\}}=\mathbf{x}_{[p] \backslash\{i, j\}}\right.$ is implied by some context $D A G G_{X_{D}=\mathbf{x}_{D}}$ with $D \neq \varnothing$.

Proof. By Lemma 5.14 one of the graphs in Lemma 5.14 is contained in $G$ as a subgraph. Assume first we are in case (1). By changing the roles of $i$ and $j$ we can assume the graph is
![img-8.jpeg](img-8.jpeg)

Let $C:=[p] \backslash\{i, j, k, l\}$ and let $\mathbf{x}_{C} \in \mathcal{R}_{C}$ be arbitrary. By Theorem 4.4 the CStree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ is still balanced. Let $G$ be the empty context DAG of this CStree, i.e. $G:=G_{\mathcal{T}_{X_{C}=\mathbf{x}_{C}}, \varnothing}$. We claim that at least one of the three edges is missing in $G$ :

Proof of claim: Let $\mathbf{x}_{i} \in \mathcal{R}_{i}$ be any outcome and consider the balanced CStree $\mathcal{T}_{X_{C}=\mathbf{x}_{C}, X_{i}=\mathbf{x}_{i}}$. By Theorem 3.2 its empty context DAG is perfect and thus one of the edges $j \rightarrow l$ or $k \rightarrow l$ is missing in $G_{\mathcal{T}_{X_{C}=\mathbf{x}_{C}}, X_{i}=\mathbf{x}_{i}, \varnothing}$. The argument for both cases is analogous, thus we do the proof for $j \rightarrow l$ only. In this case the CSI statements $X_{l} \perp X_{j} \mid X_{k}, X_{C}=\mathbf{x}_{C}, X_{i}=\mathbf{x}_{i}$

and $X_{l} \Perp X_{i} \mid X_{\{j, k\}}, X_{C}=\mathbf{x}_{C}$ hold. Using Proposition 4.6 these imply the statement $X_{l} \Perp X_{i, j} \mid X_{k}, X_{C}=\mathbf{x}_{C}$ which is not true as there is an edge $j \rightarrow l$.

Depending on which edge is missing, one of the CSI statements $X_{i} \Perp X_{k} \mid X_{j, l}, X_{C}=\mathbf{x}_{C}$, $X_{k} \Perp X_{l} \mid X_{i, j}, X_{C}=\mathbf{x}_{C}, X_{j} \Perp X_{l} \mid X_{i, k}, X_{C}=\mathbf{x}_{C}$ holds in $\mathcal{T}$. We do the proof for the first one, the other two work analogously. The statement $X_{i} \Perp X_{k} \mid X_{C \cup\{j, l\}}$ does not hold in $G_{\varnothing}$ therefore there is a context DAG $G_{X_{D}=\mathbf{x}_{D}}$ with $D \subseteq C,\left(\mathbf{x}_{C}\right)_{D}=\mathbf{x}_{D}$ and $D \neq \varnothing$ such that the CSI statement $X_{i} \Perp X_{k} \mid X_{C \backslash D \cup\{j, l\}}, X_{D}=\mathbf{x}_{D}$ is entailed by $G_{X_{D}=\mathbf{x}_{D}}$. There is now at least one less subgraph of type (1) in the empty context DAG of $\mathcal{T}_{X_{D}=\mathbf{x}_{D}}$ by Lemma 5.15. Continuing this process will result in a $D$ with no subgraphs of type (1) and only subgraphs of type (2).

The argument for (2) works similarly. To receive a DAG on three vertices as in the argument above we fix $X_{j}$ and $X_{l_{2}}$. In the end, again by Lemma 5.15 there are no such induced subgraphs at all and thus the CSI statement $X_{i} \Perp X_{j} \mid X_{C \backslash D \cup\{j, l\}}, X_{D}=\mathbf{x}_{D}$ holds in $G_{X_{D}=\mathbf{x}_{D}}$, hence also $X_{i} \Perp X_{j} \mid X_{k, l}, X_{C}=\mathbf{x}_{C}$.

Proof of 5.13. Assume the equality holds. Since $G_{X_{C}=\mathbf{x}_{C}}^{\text {per }}$ is perfect, the ideal $I_{\operatorname{Sat}\left(G_{X_{C}=\mathbf{x}_{C}}^{\text {per }}\right)}$ is a toric ideal for each context $X_{C}=\mathbf{x}_{C} \in \mathcal{C}$. Therefore, $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ is a binomial ideal. Since it is also prime, we conclude that $\operatorname{ker}\left(\psi_{\mathcal{T}}\right)$ is toric. This is equivalent to $\mathcal{T}$ being balanced by [DG20, Theorem 10]. For the additional statement we note that we may take $\mathcal{C}:=\mathcal{C}_{\mathcal{T}}$ and by moralizing we find a collection as required.

For the other direction it suffices to prove that using directed moralization once on an arbitrary context DAG does not alter the set of saturated CSI statements in $\mathcal{T}$. Let $X_{C}=$ $\mathbf{x}_{C} \in \mathcal{C}$. By replacing $\mathcal{T}$ with $\mathcal{T}_{X_{C}=\mathbf{x}_{C}}$ which is still balanced by Theorem 4.4 we may assume that we applied directed moralization to the empty context DAG. We want to prove

$$
\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C}} I_{\operatorname{Sat}\left(\left(G_{X_{C}=\mathbf{x}_{C}}\right)\right)}=\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C} \backslash\{\varnothing\}} I_{\operatorname{Sat}\left(\left(G_{X_{C}=\mathbf{x}_{C}}\right)\right)}+I_{\operatorname{Sat}\left(\left(G_{\varnothing}\right)^{d m}\right)}
$$

Let $X_{A} \Perp X_{B} \mid X_{S}$ be a saturated CSI statement implied by $G_{\varnothing}$ but not by $\left(G_{\varnothing}\right)^{d m}$. It suffices to show that $X_{i} \Perp X_{j} \mid X_{[p] \backslash\{i, j\}}$ is implied by some other context DAG for every $i \in A, j \in B$ by using the intersection axiom.

By Proposition 5.16 for every $\mathbf{x}_{[p] \backslash\{i, j\}} \in \mathcal{R}_{[p] \backslash\{i, j\}}$ the CSI statement $X_{i} \Perp X_{j} \mid X_{[p] \backslash\{i, j\}}=$ $\mathbf{x}_{[p] \backslash\{i, j\}}$ is implied by some context DAG $G_{X_{F}=\mathbf{x}_{F}}$ with $X_{F}=\mathbf{x}_{F} \in \mathcal{C}$ and $F \neq \varnothing$. Using absorption we see that all polynomials associated to the statement $X_{A} \Perp X_{B} \mid X_{S}$ are contained in $\sum_{X_{C}=\mathbf{x}_{C} \in \mathcal{C} \backslash\{\varnothing\}} I_{\operatorname{Sat}\left(\left(G_{X_{C}=\mathbf{x}_{C}}\right)\right)}$.

Example 5.17. In Figure 7 we give an example of a binary, balanced CStree where we can use directed moralization on the empty context DAG twice to obtain a perfect DAG. First, the edge $3 \rightarrow 4$ is added and then the edge $2 \rightarrow 3$ is added. This example can easily be generalized to obtain a DAG on $p$ vertices where we can apply directed moralization $p-3$ times and obtain an additional edge each time. For this we pick a path ending in $p$ and starting with 2 , and omitting 3 . The edge $3 \rightarrow p$ is then added. Lastly, we connect 1 to everything. The two other context contexts should remove the edges $3 \rightarrow 5$ and $p-1 \rightarrow p$ respectively.

![img-9.jpeg](img-9.jpeg)

Figure 7. A balanced CStree on whose empty context DAG we have to use directed moralization twice to receive a perfect DAG.

Acknowledgements. The authors thank the editors and the anonymous referees for the careful reading of the manuscript and their many insightful comments and suggestions. In particular, we thank Referee \#2 for Remark 5.12. The authors also thank the Max-PlanckInstitute for Mathematics in the Sciences in Leipzig for their hospitality in the Summer of 2022 .

YA was supported by the National Science Foundation Graduate Research Fellowship Grant No. DGE 2146752. ED was supported by the FCT grant 2020.01933.CEECIND, and partially supported by CMUP under the FCT grant UIDB/00144/2020.
