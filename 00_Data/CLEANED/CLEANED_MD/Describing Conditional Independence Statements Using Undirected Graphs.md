# Article 

## Describing Conditional Independence Statements Using Undirected Graphs

Dhafer Malouche (D)

## check for updates

Citation: Malouche, D. Describing Conditional Independence Statements Using Undirected Graphs. Axioms 2023, 12, 1109. https:// doi.org/10.3390/axioms12121109

Academic Editors: Salvatore Sessa and Xueliang Li

Received: 1 November 2023
Revised: 28 November 2023
Accepted: 1 December 2023
Published: 8 December 2023

## (0)

Copyright: (c) 2023 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Statistics Program, Department of Mathematics, Statistics and Physics, College of Arts and Sciences, Qatar University, Doha 2713, Qatar; dhafer.malouche@qu.edu.qa


#### Abstract

This paper investigates the capability of undirected graphs (UGs) to represent a set of Conditional Independence (CI) statements derived from a given probability distribution of a random vector. While it is established that certain axioms can govern this set, providing sufficient conditions for UGs to capture specific CI statements, our focus is on covariance and concentration graphs. These remain the only known families of UGs capable of describing CI statements. We explore the issue of complete representation of CI statements through their corresponding covariance and concentration graphs. Two parameters are defined, one each from the covariance and concentration graphs, to determine the limitations concerning the cardinality of the conditioning subset that the graph can represent. We establish a relationship between these parameters and the cardinality of the separators in each graph, providing a straightforward computational method to evaluate them. In conclusion, we enhance the aforementioned procedure and introduce criteria to ascertain, without additional computations, whether the graphs can fully represent a given set of CI statements. We demonstrate that either the concentration or the covariance graph forms a cycle, and when considered in conjunction, they can represent the entire relation. These criteria also enable us, in specific cases, to deduce the covariance graph from the concentration graph and vice versa.


Keywords: graphical models; multivariate gaussian distribution; conditional independences
MSC: 62H05; 05C90; 60E05; 62H20; 05C75

## 1. Introduction

In the realm of statistics and graphical estimation, conditional independence is fundamental in simplifying complex multivariate relationships and plays a crucial role in the construction and interpretation of graphical models, including Bayesian networks and Markov random fields. These models, which are pivotal in fields such as bioinformatics, epidemiology, and machine learning, leverage conditional independence to efficiently represent variable dependencies, thus enabling a more intuitive understanding of the underlying data structure and facilitating model simplification by reducing the number of parameters required (see [1-3]). This approach is particularly valuable in high-dimensional data analysis for identifying relevant variables and constructing sparse models, essential for effective prediction and inference. In the estimation of these models, learning conditional independence relationships directly from data is a key aspect, especially in high-dimensional settings with complex mean structures and random effects, where constraint-based methods are employed to estimate these relationships and form Bayesian networks [4]. The use of Bayesian networks in analyzing gene expression data underscores the connection between these networks and the concept of direct causal influence, characterized by probabilities and conditional independence statements [5]. Furthermore, in epidemiology, Bayesian network modeling is recognized as a well-suited approach for studying messy and highly correlated datasets typical in systems epidemiology, while the application of probabilistic graphical models, such as conditional random fields, hypergraph convolution networks,

and large margin models, highlights the prevalence of these methods in learning with graphical structure $[6-8]$.

This paper uses undirected graphs as a mathematical framework for representing sets of Conditional Independence (CI) statements. These graphs, commonly called graphical models, have been extensively studied in [9-11]. A central question in this field is whether a simple mathematical surrogate, like a graph, can effectively represent most of the CI statements associated with a random vector without requiring additional computations. Given the simplicity and mathematical rigor of graphs (see [12]), they appear to be suitable candidates for this role.

Graphical models are constructed according to specific rules, associating them with a probability distribution. These models are derived from a subset of the CI statements and can subsequently be used to infer additional CI statements within the distribution. To formalize this, consider a finite set $V$ and denote $u v$ as the pair $(u, v)$ of two elements in $\mathbf{V}=V \times V \backslash\{(u, u) \in V \times V ; u \in V\}$.

Given a random vector $\mathbf{X}_{V}=\left(X_{v}, v \in V\right)^{\prime}$ indexed by $V$ and associated with a probability distribution $P$, we can define an undirected graph $G=(V, E)$ based on $P$ and a fixed family $\mathcal{P}$ of subsets of $V$. Here, $V$ serves as the set of vertices, and the set of edges $E$ is a subset of $\mathbf{V}$ as defined in Equation (1).

$$
E \subseteq \mathbf{V}=V \times V \backslash\{(u, u) \in V \times V ; u \in V\}
$$

The graph $G$ satisfies the following condition:

$$
u v \notin E \Longleftrightarrow \exists S \in \mathcal{P} \text { such that } u \Perp v \mid S
$$

Here, $u \Perp v \mid S$ is shorthand for the statement " $X_{u}$ is independent of $X_{v}$ given the random vector $\mathbf{X}_{S}$ indexed by $S$, i.e., $\mathbf{X}_{S}=\left(X_{s}, s \in S\right)^{\prime \prime}$. When this property (2) is met, we say that $P$ is pairwise Markov to $G$ according to $\mathcal{P}$.

This paper focuses on two well-known types of undirected graphical models. The first type is the concentration graph, denoted by $G=(V, E)$, which is constructed from $P$ when the family $\mathcal{P}=\mathcal{P}_{|V|-2}=\{S \subseteq V$ such that $|S|=|V|-2\}$. The second type is the covariance graph, denoted by $H=(V, F)$, and is constructed from $P$ when the family $\mathcal{P}=\mathcal{P}_{0}=\{\varnothing\}$

Under certain conditions satisfied by the probability distribution $P$ [10,13-15], both types of graphs can be used to infer a wide range of CI statements, although not exhaustively. Specifically, for a triplet $(A, B, C)$ of pairwise disjoint subsets of $V$, if $A$ is separated from $B$ by $C$ in $G$, then $A \Perp B \mid C$. In this context, $P$ is said to be globally Markov to $G$.

To formalize, consider the following sets of triplets $(A, B, S)$ of pairwise disjoint subsets of $V$ :

$$
\mathbf{S}(G)=\{(A, B, S) \mid S \text { separates } A \text { and } B \text { in } G\}
$$

and

$$
\mathbf{C}(P)=\{(A, B, S) \mid A \Perp B \mid S\}
$$

$P$ is globally Markov to $G$ if and only if $\mathbf{S}(G) \subseteq \mathbf{C}(P)$.
Similarly, for the covariance graph $H$, if $A$ and $B$ are separated by $V \backslash(A \cup B \cup C)$ in $H$, then $A \Perp B \mid C$ in $P$ (see [15-17]). In this case, $P$ is also considered globally Markov to $H$. Therefore, consider the following set:

$$
\overline{\mathbf{S}}(H)=\{(A, B, S) \mid V \backslash(A \cup B \cup S) \text { separates } A \text { and } B \text { in } H\}
$$

$P$ is globally Markov to $H$ if and only if $\overline{\mathbf{S}}(H) \subseteq \mathbf{C}(P)$.
In this paper, we aim to identify the families of probability distributions that the concentration and covariance graphs can fully represent. The central question is to ascertain the conditions on $P$ such that

$$
\mathbf{C}(P)=\mathbf{S}(G) \cup \overline{\mathbf{S}}(H)
$$

where $G$ and $H$ are the concentration and covariance graphs associated with $P$, respectively.
It has been previously established in [18] that when the CI statements are fully captured by the concentration graph, i.e., $\mathbf{S}(G)=\mathbf{C}(P)$, the covariance graph must be a union of complete connected graphs. In such cases, $P$ is said to be faithful to its concentration graph. Conversely, using a dual argument, it was shown that if the covariance graph can fully represent the CI statements, i.e., $\overline{\mathbf{S}}(H)=\mathbf{C}(P)$, then the concentration graph must also be a union of complete connected graphs. Under these conditions, $P$ is faithful to its covariance graph (see [19]).

In [19], the authors provided a sufficient condition for $P$ to be faithful to its concentration graph. They demonstrated that if all connected components of a concentration graph are trees and $P$ satisfies certain conditions, then the graph can fully represent the CI statements. This result holds when all connected components of the covariance graph are also trees. In the Gaussian case, it was further established in [20] and generalized in [17] that these graphs represent all sets of CI statements.

In this paper, we investigate whether the concentration and covariance graphs, when considered together, can fully describe a set of Conditional Independence (CI) statements. We introduce the term CC-faithful to describe a probability distribution $P$ that can be completely represented by these graphs when considered in tandem. While it is unlikely that this holds universally, we aim to identify necessary conditions for $P$ to be CC-faithful.

Our first main result reveals that the conditions depend on the size of the separators in both the covariance and concentration graphs. We then proceed to identify families of probability distributions that are CC-faithful, working within a general framework that utilizes the set of relations previously defined in [14,21].

We show that the study of CI statements can be restricted to those of the form $u \Perp v \mid S$, where $u, v \in V$ and $S \subseteq V \backslash\{u, v\}$. These CI statements, denoted by $(u v \mid S)$, are termed couples. We then consider the set of such couples as a relation on $V$.

We demonstrate that when a given relation $\mathcal{L}$ satisfies an axiom known as the pseudographoid axiom, a global Markov property holds. This implies that the set of relations constructed from the covariance and concentration graphs are subsets of $\mathcal{L}$. We also establish a one-to-one mapping between the covariance and concentration graphs, simplifying many proofs. For instance, we show that less restrictive conditions are needed for the global Markov property on the covariance graph, contrary to the assumptions made in [17].

In the final section, we introduce a graphical criterion for identifying new dependencies from the covariance and/or concentration graphs, extending the work in [17]. We provide examples of CC-faithful probability distributions, showing that when either the covariance or concentration graph forms a cycle, $P$ is CC-faithful.

The paper is organized as follows: Section 2 introduces the notations and is divided into two subsections focusing on basic graph theory and properties of relations, respectively. Section 3 discusses how relations derived from the concentration and covariance graphs are subsets of the originating relation, provided they satisfy the pseudographoid axiom. Section 4 introduces separatoids, a generalization of separators. Section 5 examines the role of separator size in the ability of the graphs to describe CI statements. Finally, Section 6 presents a graphical criterion for reading dependencies and provides examples of CC-faithful distributions.

# 2. Preliminaries 

In this section, we delineate the essential notations utilized throughout this paper. It is systematically segmented into two subsections: the first focuses on the characteristics and nuances of undirected graphs, while the second meticulously details the assembly of relations, representing a comprehensive method to articulate the set of Conditional Independence (CI) statements within a specified probability distribution.

### 2.1. Undirected Graphs

An undirected graph $G=(V, E)$ consists of sets $V$ representing the set of vertices and $E \subseteq \mathbf{V}$ where $\mathbf{V}$ is the set defined in (1).

$$
\forall u v \in E \Longleftrightarrow v u \in E
$$

For $u, v \in V$, we write $u \sim_{G} v$ when $u v \in E$ and we say that $u$ and $v$ are adjacent in $G$. Let us first recall some basic definitions of undirected graphs.

- A path connecting two distinct vertices $u$ and $v$ in a graph $G$ is a sequence of distinct vertices $\left(u_{0}, \ldots, u_{n}\right)$, where $u_{0}=u$ and $u_{n}=v$ and, for each $i \in\{0, \ldots, n-1\}, u_{i} \sim_{G}$ $u_{i+1}$. Such a path is denoted by $p=p(u, v, G)$, establishing that $p(u, v, G)$ connects $u_{0}$ and $u_{n}$. Alternatively, we can state that $u_{0}$ and $u_{n}$ are connected by $p(u, v, G)$. The length of this path, denoted by $|p(u, v, G)|$, is defined as the number of edges connecting the vertices within $p,|p(u, v, G)|=n$. Moreover, we denote by $\mathcal{P}(u, v, G)$ the set of all possible paths between $u$ and $v$. Furthermore, we define two paths $p_{1}$ and $p_{2}$ in $\mathcal{P}(u, v, G)$ to be disjoint if their intersection is $u, v$, clearly indicating that $u$ and $v$ are the sole common vertices between $p_{1}$ and $p_{2}$.
- A subgraph of $G$ induced graph by a subset $U \subseteq V$ is denoted by $G_{U}=\left(U, E_{U}\right), U \subseteq V$ and $E_{U}=E \cap(U \times U)$
- A connected component of $G$ is the largest subgraph $G_{U}=\left(U, E_{U}\right)$ of $G$ such that each pair of vertices can be connected by at least one path in $G_{U}$. Equivalently we can define $G_{U}$ to be a connected component of $G$ if and only if $G_{U}$ satisfies the following two conditions
i. $\forall u v \in U \times U, \mathcal{P}\left(u, v, G_{U}\right) \neq \varnothing$.
ii. $\forall u \in U \forall w \in V \backslash U, \mathcal{P}(u, w, G)=\varnothing$.

It is straightforward to see that the two definitions above are equivalent.

- For a connected graph, a separator is a subset $S$ of $V$ such that there exists a pair of non-adjacent vertices $u$ and $v$ such that $u, v \notin S$ and

$$
\forall p \in \mathcal{P}(u, v, G), \quad p \cap S \neq \varnothing
$$

In that case, we write $u \perp_{G} v \mid S$. It is also easily verified that every $S^{\prime} \supseteq S$ such that $S^{\prime} \subseteq V \backslash\{u, v\}$ is also a separator. We are thus led to the notion of minimal separator. The separator $S$ is defined to be a minimal separator between two non-adjacent vertices $u$ and $v$ if for any $w \in S$, the subsets $S \backslash\{w\}$ is not a separator of $u$ and $v$.

- For any triplet $(A, B, S)$ of pairwise disjoint subsets of $V$, we say that $S$ separates $A$ and $B$ in $G$ and we denote by $A \perp_{G} B \mid S$ if for any pair of vertices $u v \in A \times B$ we have $u \perp_{G} v \mid S$.


# 2.2. The Set of Relations 

Let $V$ be a finite set. We don't distinguish in the next of this paper between singletons and elements and we denote by $A B$ a union of two subsets $A$ and $B$ of $V$. We call a couple an object $(u v \mid S)$ where $u$ and $v$ are two distincts elements of $V$ and $S \subseteq V \backslash u v$. We denote by $\mathcal{C}(V)$ the set of all the couples

$$
\mathcal{C}(V)=\{(u v \mid S) \text { where } u v \in V \times V, u \neq v \text { and } S \subseteq V \backslash u v\}
$$

where $V \backslash u v=V \backslash\{u, v\}$.
Any subset of $\mathcal{C}(V)$ will be called a relation, and it will be generally denoted by $\mathcal{L}$. We associate a given relation $\mathcal{L}$ the set $\mathcal{V}(\mathcal{L})$ the of subsets of $V$ defined as follows

$$
\mathcal{V}(\mathcal{L})=\{S \subseteq V \text { such that } \exists u v \in \mathbf{V} \text { and }(u v \mid S) \in \mathcal{L}\}
$$

Let us now give three examples of well-known relations. We will see later that these relations satisfy the pseudographoid axiom.

Example 1. Let $\boldsymbol{X}_{V}=\left(X_{v}, v \in V\right)^{\prime}$ be a random vector with a probability distribution $P$. Let us define the relation $\mathbf{c}(P)$ as follows

$$
\mathbf{c}(P)=\{(u v \mid S) \in \mathcal{C}(V) \text { such that } u \Perp v \mid S\}
$$

where $u \Perp v \mid S$ denotes that the variables $X_{u}$ and $X_{v}$ are independent given the sub-random vector $\boldsymbol{X}_{S}$ indexed by $S$.

Example 2. Let $G=(V, E)$ be an undirected graph and where we denote by $u \perp_{G} v \mid S$ when the set $S \subseteq V \backslash u v$ separates $u$ and $v$ in $G$.

$$
\mathbf{s}(G)=\left\{(u v \mid S) \in \mathcal{C}(V) \text { such that } u \perp_{G} v \mid S\right\}
$$

Let us notice the following remarks
i. $G$ is complete if and only if $\mathbf{s}(G)=\varnothing$.
ii. $G$ is connected if and only if $\mathcal{V}(\mathbf{s}(G)) \not \equiv \varnothing$, where $\mathcal{V}(\mathbf{s}(G))$ is the set associated with $\mathbf{s}(G)$ according to (6).
iii. Ghas $n$ connected components $U_{1}, \ldots, U_{n}$ then $\mathbf{s}(G)=\left(\bigcup_{i=1}^{n} \mathbf{s}\left(G_{U_{i}}\right)\right) \cup \mathbf{s}_{\varnothing}(G)$ where for $i=1 \ldots n$ the graph $G_{U_{i}}$ is the subgraph induced from $U_{i}$ on $G$ and $\mathbf{s}_{\varnothing}$ is the relation defined as follows

$$
(u v \mid S) \in \mathbf{s}_{\varnothing}(G) \Longleftrightarrow S=\varnothing \text { and } \exists i \neq j \in\{1, \ldots, n\} \text { s.t. } u \in U_{i} \text { and } v \in U_{j}
$$

Example 3. Let us consider $\Sigma$ a positive definite matrix, i.e., $\Sigma=\left(\sigma_{u v}\right)_{u, v \in V}$. We denote by $\Sigma_{u S, v S}$ the sub-matrix of $\Sigma$ with rows in $u S$ and columns in $v S$. We denote then the following relation

$$
\mathbf{d}(\Sigma)=\left\{(u v \mid S) \in \mathcal{C}(V) \text { such that } \operatorname{det}\left(\Sigma_{u S, v S}\right)=0\right\}
$$

Note that if $\Sigma$ is considered as the covariance matrix of the probability distribution $P$ then the relations $\mathbf{d}(\Sigma)$ and $\mathbf{c}(P)$ defined respectively (9) and in (7) are equal.

We also know that from any probability distribution $P$ we can define two undirected graphs called covariance and concentration graphs. We will show in the next section that the set of relations constructed from these two graphs is included in the set of relations composed from the probability distribution. We will prove this result remains true for any relation satisfying an axiom called the pseudographoid relation. This fact is known for concentration graphs (see [14]). However, by using a dual relationship between the covariance and the concentration graph, we show that this inclusion can also be satisfied by covariance graphs, unlike what is proved in [17] where the author assumes a further axiom called the weak transitivity axiom.

# 3. Markov Relations 

Let us denote by $\mathcal{R}(V)$ the set of relations defined on $V$ and we define on $\mathcal{R}(V)$ the application $\mathcal{T}: \mathcal{R}(V) \longrightarrow \mathcal{R}(V)$ such that the relation $\mathcal{T}(\mathcal{L})$ is defined as follows

$$
\mathcal{T}(\mathcal{L})=\{(u v \mid S) \text { such that }(u v \mid V \backslash S u v) \in \mathcal{L}\}
$$

The relation $\mathcal{T}(\mathcal{L})$ will be called the dual of $\mathcal{L}$. It is easily seen that for any $\mathcal{L} \in \mathcal{R}(V)$ we have $\mathcal{T}(\mathcal{T}(\mathcal{L}))=\mathcal{L}$, i.e., $\mathcal{T} \circ \mathcal{T}=\operatorname{id}_{\mathcal{R}(V)}$. In this section and in the next of this paper, we say that $\mathcal{L}$ satisfies the pseudogrphoid axiom if the following axiom is satisfied: for any $\{u, v, w\} \subseteq V$ and $S \subseteq V \backslash u v w$ the following axiom

$$
\{(u v \mid S w),(u w \mid S v)\} \subseteq \mathcal{L} \text { then }\{(u v \mid S),(u w \mid S)\} \subseteq \mathcal{L}
$$

It was proved in [21] that all the relations $\mathbf{c}(P), \mathbf{s}(G)$ and $\mathbf{d}(\Sigma)$ defined in the Examples 1-3 satisfy the pseudographoid axiom (11).

Lemma 1. Let $\mathcal{L}$ and $\mathcal{L}^{\prime}$ be two relations in $\mathcal{R}(V)$. The following assertions are then satisfied
i. If $\mathcal{L}$ is satisfying (11) then $\mathcal{T}(\mathcal{L})$ is a pseudographoid too.
ii. If $\mathcal{L} \subseteq \mathcal{L}^{\prime}$ then $\mathcal{T}(\mathcal{L}) \subseteq \mathcal{T}\left(\mathcal{L}^{\prime}\right)$.

Proof. The proof of (i) can be found in [21] (see Lemma 2).
Let us now prove (ii). We have

$$
\begin{aligned}
& (u v \mid S) \in \mathcal{T}(\mathcal{L}) \Longleftrightarrow(u v \mid V \backslash S u v) \in \mathcal{L} \subseteq \mathcal{L}^{\prime} \\
& \Longrightarrow(u v \mid V \backslash S u v) \in \mathcal{L}^{\prime} \\
& \Longrightarrow(u v \mid S) \in \mathcal{T}\left(\mathcal{L}^{\prime}\right)
\end{aligned}
$$

Let us now show how to associate to any relation $\mathcal{L}$ and a fixed set $\mathcal{P}$ of subsets of $V$, i.e.,

$$
\mathcal{P}=\{S, S \subseteq V\}
$$

We will see later two kinds of such graphs constructed using pairwise relationships but their role will be larger. Indeed, they will help us determine all the elements of $\mathcal{L}$ from reading separation statements on those graphs. Let us consider the following application $\mathcal{G}: \mathcal{R}(V) \times \mathcal{P}^{2}(V) \longrightarrow \mathcal{G}(V)$ such that if $G=\mathcal{G}(\mathcal{L}, \mathcal{P})$ then

$$
u \nprec_{G} v \Longleftrightarrow \exists S \in \mathcal{P} \text { such that }(u v \mid S) \in \mathcal{L}
$$

We denote here by $\mathcal{P}^{2}(V)$ the power set of the power set $\mathcal{P}(V)$ of $V$, i.e.,

$$
\mathcal{P}^{2}(V)=\{\mathcal{P} \text { such that } \mathcal{P} \subseteq \mathcal{P}(V)\}
$$

Let us fix $k \in\{0, \ldots,|V|-2\}$ and consider the following family of subsets of $V$, $\mathcal{P}_{k} \in \mathcal{P}^{2}(V)$, i.e.,

$$
\mathcal{P}_{k}=\{S \subseteq V \text { such that }|S|=k\}
$$

and we consider then the following pair of undirected graphs $\left(G_{k}, H_{k}\right)$ defined as follows

$$
G_{k}=\mathcal{G}\left(\mathcal{L}, \mathcal{P}_{k}\right) \text { and } H_{k}=\mathcal{G}\left(\mathcal{L}, \mathcal{P}_{|V|-k-2}\right)
$$

We are now interested in the special case where $k=|V|-2$
Case $1 G=G_{|V|-2}=\mathcal{G}\left(\mathcal{L}, \mathcal{P}_{|V|-2}\right)$ where $\mathcal{P}_{|V|-2}=\{S \subseteq V$ such that $|S|=|V|-2\}$ we say that $G$ is the concentration graph associated with $\mathcal{L}$.
Case $2 H=H_{|V|-2}=\mathcal{G}\left(\mathcal{L}, \mathcal{P}_{0}\right)$ where $\mathcal{P}_{0}=\{\varnothing\}$. We say that $H$ is the covariance graph associated with $\mathcal{L}$.
Instead of considering the application $\mathcal{G}(\cdot, \cdot)$ we will rather consider the following two applications $\mathbf{g}$ and $\mathbf{h}$ and defined as follows

$$
\mathbf{g}=\mathcal{G}\left(\cdot, \mathcal{P}_{|V|-2}\right) \text { and } \mathbf{h}=\mathcal{G}\left(\cdot, \mathcal{P}_{0}\right)
$$

The applications $\mathbf{g}$ and $\mathbf{h}$ will be called respectively that concentration and the covariance map. It is easily seen that $\mathbf{g}=\mathbf{h} \circ \mathcal{T}$ and $\mathbf{h}=\mathbf{g} \circ \mathcal{T}$. It is easily seen then that $G$ can be viewed as the covariance graph of the dual of $\mathcal{L}$, i.e., $\mathcal{T}(\mathcal{L})$ and vis versa for the graph $H$.

This section aims to show that a part of the element of a given relation can be described using the concentration and the covariance graphs. The theorem that will be proved below is a generalization of a result well known as the global Markov property to a distribution probability to its covariance or concentration graph.

Theorem 1. Let $\mathcal{L} \in \mathcal{R}(V)$ a pseudographoid. Let $G=\mathbf{g}(\mathcal{L})$ and $H=\mathbf{h}(\mathcal{L})$ be respectively the concentration and the covariance graphs associated with $\mathcal{L}$. Then if $\mathcal{L}$ is a pseudographoid then

$$
\mathbf{s}(G) \subseteq \mathcal{L}
$$

and

$$
\mathcal{T}(\mathbf{s}(H)) \subseteq \mathcal{L}
$$

Before we begin the proof of Theorem 1, it is important to note that the equalities $\mathbf{s}(G) \subseteq \mathcal{L}$ and $\mathcal{T}(\mathbf{s}(H)) \subseteq \mathcal{L}$ may occur. These are related to the concept of faithfulness of the graphical structure to the pseudographoid structure. The definition of faithfulness will be discussed later in Definition 3.

Proof. Let us first proof (16). The proof below can also be found in [10,13,21].
Let then $(u v \mid S) \in \mathcal{S}(G)$, i.e., $u \perp_{G} v \mid S$ and let us show that $(u v \mid S) \in \mathcal{L}$. Let us prove this by backward induction on $n=|S|$. If $n=|V|-2$ there is nothing to prove.

Assume now that $|S|=n<|V|-2$ and that relations in $\mathbf{s}(G)$ are contained in $\mathcal{L}$ when $|S|>n$.

Since $S u v \varsubsetneqq V$, let $w \in V \backslash S u v$. Hence $(u v \mid S w) \in \mathbf{s}(G)$ and by induction we can say that $(u v \mid S w) \in \mathcal{L}$. Further more since $\{(u v \mid S),(u v \mid S w)\} \in \mathbf{s}(G)$ then either $(u w \mid S v) \in \mathbf{s}(G)$ or $(v w \mid S u) \in \mathbf{s}(G)$. Otherwise, a path exists between $u$ and $w$ that does not intersect $S v$, and another one between $v$ and $w$ that does not intersect $S u$. Hence we can construct a path between $u$ and $v$ that contains $w$ and does not intersect $S$. It is a contradiction with $(u v \mid S) \in \mathbf{s}(G)$.

Let us then assume that $(u w \mid S v) \in \mathbf{s}(G)$. Hence $(u w \mid S v) \in \mathcal{L}$. Since $\mathcal{L}$ is a pseudographoid we can deduce from $\{(u v \mid S w),(u w \mid S v)\} \subseteq \mathcal{L}$ that $(u v \mid S) \in \mathcal{L}$.

To prove (17) it will be enough to apply (16) to the relation $\mathcal{T}(\mathcal{L})$. According to Lemma 1 the relation $\mathcal{T}(\mathcal{L})$ satisfyies the pseudographoid axiom (see (11)). Then

$$
\mathbf{s}(\mathbf{g}(\mathcal{T}(\mathcal{L})) \subseteq \mathcal{T}(\mathcal{L}) \Longleftrightarrow \mathbf{s}(\mathbf{h}(\mathcal{L})) \subseteq \mathcal{T}(\mathcal{L}) \Longleftrightarrow \quad \Longrightarrow \quad \Longrightarrow \quad \Longrightarrow \quad \Longrightarrow
$$

We can deduce then from Theorem 1 that if $\mathcal{L}$ is a pseudographoid the following inclusion holds

$$
\mathbf{s}(G) \cup \mathcal{T}(\mathbf{s}(H)) \subseteq \mathcal{L}
$$

Since it is well known that the relation defined from a given probability distribution $P$ as in Example 1 is also satisfying the pseudographoid axiom (11). Let us then define the CC-faithful probability distributions.

Definition 1. Let $P$ be a probability distribution of a random vector $\mathbf{X}=\left(X_{v}, v \in V\right)^{\prime}$ and let
i. $\quad \mathbf{c}(P)$ be the relation associated to $P$ according to (7)
ii. $\quad G=\mathbf{g}(\mathbf{c}(P))$ be the concentration associated with $P$.
iii. $H=\mathbf{h}(\mathbf{c}(P))$ be the covariance associated with $P$.

We say that $P$ is a CC-faithful if $\mathbf{c}(P)=\mathbf{s}(G) \cup \mathcal{T}(\mathbf{s}(H))$.
Our main question now for the next of this paper is to determine which conditions should be satisfied by the undirected graph $G$ and/or $H$ to obtain the equality in (18)?

# 4. Separatoids on $\mathcal{L}$ 

Let $\mathcal{L}$ be a non empty relation in $\mathcal{R}(V)$ and let us denote by $\mathcal{V}(\mathcal{L})$ the subset of pairs $u v$ belonging in $V \times V$ such that $u \neq v$ and there exists at least one $S \subseteq V \backslash u v$ such that $(u v \mid S) \in \mathcal{L}$. Let us consider the following definition

Definition 2. Let $u$ and $v$ be two distincts elements of $V$. Let $S$ and $T$ be two subsets of $V \backslash u v$ such that $(u v \mid S)$ and $(u v \mid T)$ in $\mathcal{L}$. We say that
i. $\quad S$ is a minimum separatoid between $u$ and $v$ if either $S=\varnothing$ or $\forall w \in S,(u v \mid S \backslash w) \notin \mathcal{L}$.
ii. $T$ is a maximum separatoid between $u$ and $v$ if either $T=V \backslash u v$ or $\forall w \in V \backslash T u v$, $(u v \mid T w) \notin \mathcal{L}$.

Let us then denote by $\mathbf{S}(u, v, \mathcal{L})$ and by $\mathbf{T}(u, v, \mathcal{L})$ be respectively the set of all the minimal and maximal separatoids defined between $u$ and $v$. We define the following two parameters

$$
s(u, v, \mathcal{L})=\min _{S \in \mathbf{S}(u, v, \mathcal{L})}|S|
$$

and

$$
t(u, v, \mathcal{L})=\max _{T \in \mathbf{T}(u, v, \mathcal{L})}|T|
$$

Lemma 2. Let $\mathcal{L} \in \mathcal{R}(V)$ and let $u v \in \mathcal{V}$ and $\mathbf{S}(u, v, \mathcal{L})$ and $\mathbf{S}(u, v, \mathcal{T}(\mathcal{L}))$ be the set of minimal separatoids associated respectively to $\mathcal{L}$ and $\mathcal{T}(\mathcal{L})$. Then

$$
S \in \mathbf{S}(u, v, \mathcal{L}) \Longleftrightarrow V \backslash S u v \in \mathbf{T}(u, v, \mathcal{T}(\mathcal{L}))
$$

Furthermore, we have

$$
s(u, v, \mathcal{L})+t(u, v, \mathcal{T}(\mathcal{L}))=|V|-2
$$

Proof. Let $S \in \mathbf{S}(u, v, \mathcal{L})$ and let us prove that $T=V \backslash S u v \in \mathbf{T}(u, v, \mathcal{T}(\mathcal{L}))$. It is equivalent to show the following statements
i. $\quad(u v \mid T) \in \mathcal{T}(\mathcal{L})$
ii. either $T=V \backslash u v$ or $\forall w \in V \backslash T u v,(u v \mid T w) \notin \mathcal{L}$

Since $(u v \mid S) \in \mathcal{L}$, then $(u v \mid V \backslash S u v) \in \mathcal{T}(\mathcal{L})$. Hence $(u v \mid T)=(u v \mid V \backslash S u v) \in \mathcal{T}(\mathcal{L})$. Then (i) is proved.

Let us show (ii). If $S=\varnothing$, then $T=V \backslash u v$. Let $w \in V \backslash T u v$ we know that $(u v \mid$ $S \backslash w) \notin \mathcal{L}$. Hence $(u v \mid V \backslash((S \backslash w) u v) \notin \mathcal{T}(\mathcal{L})$ since $V \backslash((S \backslash w) u v)=(V \backslash S u v) w=T w$. Hence, (ii) is completely proved.

We can use the same argument to show the other way in the equivalence (21).
Let us now prove the equality (22). Let $s=s(u, v, \mathcal{L})$ and $t=t(u, v, \mathcal{T}(\mathcal{L}))$. let us show that $s+t=|V|-2$.

Let $S \in \mathbf{S}(u, v, \mathcal{L})$, then $|S| \geq s$. Since $V \backslash S u v \in \mathbf{T}(u, v, \mathcal{T}(\mathcal{L}))$, then $|V \backslash S u v| \leq t$. Hence $|S| \geq|V|-t-2$. Then $s \geq|V|-t-2$ and $s+t \geq|V|-2$.

Let now $T \in \mathbf{T}(u, v, \mathcal{T}(\mathcal{L}))$, then $|T| \leq t$. Since $V \backslash T u v \in \mathbf{S}(u, v, \mathcal{L})$, then $|V \backslash T u v| \geq s$. Hence $|T| \leq|V|-s-2$. Then $t \leq|V|-s-2$ and $t+s \leq|V|-2$.

We deduce then that $s+t=|V|-2$.
Let us consider the case of a relation a type $\mathbf{s}(G)$ where $G$ is an undirected graph. Since $(u v \mid S)$ belongs to $\mathcal{S}(G)$ means that $S$ separates $u$ and $v$ in $G$ then for any $w \in V \backslash S u v$ we have also $(u v \mid S w) \in \mathbf{s}(G)$. Let us recall that if $S$ separates $u$ and $v$ in $G$, then any subset containing $S$ is also a separator of $u$ and $v$ in $G$. Then it is easily seen that the set $\mathbf{T}(u, v, \mathbf{s}(G))=\{V \backslash u v\}$ and consequently by applying Lemma 2 we deduce that $t(u, v, \mathbf{s}(G))=|V|-2, \mathbf{S}(u, v, \mathcal{T}(\mathbf{s}(G)))=\{\varnothing\}$ and $s(u, v, \mathcal{T}(\mathbf{s}(G)))=0$.

We have then proved the lemma below.
Lemma 3. Let $G$ be an undirected graph and let $\mathbf{s}(G)$ be the relation associated with $G$ according to (2). Then $\mathbf{T}(u, v, \mathbf{s}(G))=\{V \backslash u v\}, \mathbf{S}(u, v, \mathcal{T}(\mathbf{s}(G)))=\{\varnothing\}, t(u, v, \mathbf{s}(G))=|V|-2$ and $s(u, v, \mathcal{T}(\mathbf{s}(G)))=0$.

Let us define then the separability of an undirected graph.

Definition 3. Let $G=(V, E)$ be an undirected graph. If $G$ is not complete, we define for any non adjacent pair of vertices $u v$ in $G$ the separability order of $u v$ as

$$
\operatorname{so}(u, v, G)=s(u, v, \mathbf{s}(G))
$$

we define the separability of $G$ by

$$
\operatorname{so}(G)=\max _{u \neq_{G} v} \operatorname{so}(u, v, G)
$$

if $G$ is not-complete and equal to $+\infty$ is $G$ is complete.
In the following section, we will explore how understanding the separability order of the covariance graph aids in determining the capacity of the concentration graph to represent the elements of $\mathcal{L}$, and vice versa. We will revisit a finding from a previous paper (see [18]), which elucidates the effects on the covariance graph when the concentration graph fully represents $\mathcal{L}$. This was initially demonstrated for concentration and covariance graphs under specific conditions in [18]. Here, we expand upon this result under much broader conditions.

However, let's make some remarks about the parameters introduced in Definition 3. Indeed, this parameter was defined and used in [22]. But determining the value of so $(u, v, G)$ for a given non-adjacent vertices are known to be called Menger's problem (see [23]), and it was proved in many references (see [24-26]), and many others) this number equals the maximal number of disjoint paths between $u$ and $v$.

Hence if $u$ and $v$ are note belonging to the same connected component of $G$, then $\operatorname{so}(u, v, G)=0$. Furthermore, so $(G)=0$ if and only if $G$ comprises complete connected components and if so $(G)=+\infty$ if and only if $G$ is complete.

# 5. Ability of the Concentration and the Covariance Graphs to Represent $\mathcal{L}$ 

In this section, we are interested in showing how much-undirected graphs can describe a pseudographoid relation $\mathcal{L}$. We have already seen in Theorem 1 that the concentration graph $G=\mathbf{g}(\mathcal{L})$ and the covariance graph $H=\mathbf{h}(\mathcal{L})$ are both of them able to determine elements of $\mathcal{L}$ by reading separation statements on $G$ and $H$. Our main question in this section is which of the elements of $\mathcal{L}$ can be missed by $G$ and $H$. We will show that the couples $(u v \mid S) \in \mathcal{L}$ that $G$ can miss having necessary an $S$ with a cardinality smaller than a number depending on the separability order of $H$. By using a "dual technique", we show that the couples $(u v \mid S) \in \mathcal{L}$ that $H$ can miss having necessary an $S$ with a cardinality smaller than a number depending on the separability order of $G$.

Before giving the proof of the main result of this section, we would like to introduce some notations. Let us recall that by the construction of $G$, the following equivalence is satisfied for any pair $u v$ of non-adjacent vertices in $G$

$$
(u v \mid V \backslash u v) \in \mathbf{s}(G) \Longleftrightarrow(u v \mid V \backslash u v) \in \mathcal{L}
$$

Hence if we denote for any $l \in\{0, \ldots,|V|-2\}$ an application $\phi_{l}: \mathcal{R}(V) \longrightarrow \mathcal{R}(V)$ such that for any relation $\mathcal{L}$

$$
\phi_{l}(\mathcal{L})=\left\{(u v \mid S) \in \mathcal{L} \text { such that }|S|=l\right\}
$$

From the equivalence in (25) it can be easily deduced that $\phi_{|V|-2}(\mathcal{L})=\phi_{|V|-2}(\mathbf{s}(G))$. Let us thus define the integer $\mu=\mu(\mathcal{L})$ as the smallest integer such that

$$
\phi_{l}(\mathcal{L})=\phi_{l}(\mathbf{s}(G))
$$

is satisfied. Hence we deduce that when $\mu$ is known, the undirected graph $G$ allows us to determine all the couples $(u v \mid S)$ of $\mathcal{L}$ where $|S| \geq \mu$.

Similarly and by construction of $H$, the following equivalence is satisfied for any pair $u v$ of non-adjacent vertices in $G$

$$
(u v \mid \varnothing) \in \mathcal{T}(\mathbf{s}(H)) \Longleftrightarrow(u v \mid \varnothing) \in \mathcal{L}
$$

Hence the equivalence in (28) can be written $\phi_{0}(\mathcal{L})=\phi_{0}(\mathcal{T}(\mathbf{s}(H)))$. We can also define the integer $v=v(\mathcal{L})$ as the largest integer such that

$$
\phi_{l}(\mathcal{L})=\phi_{l}(\mathcal{T}(\mathbf{s}(H)))
$$

Hence we deduce that when $v$ is known, the undirected graph $H$ allows us to determine the couples $(u v \mid S)$ of $\mathcal{L}$ where $|S| \leq v$.

The two lemma below help us to give a relationship between $\mu(\mathcal{L})$ and $v(\mathcal{T}(\mathcal{L}))$.
Lemma 4. Let $\mathcal{L}$ be a relation in $\mathcal{R}(V)$ and $\phi_{l}$ an application defined as in (26) where $l \in\{0, \ldots,|V|-2\}$. Then

$$
\mathcal{T} \circ \phi_{l}=\phi_{|V|-l-2} \circ \mathcal{T}
$$

Proof. Let $\mathcal{L} \in \mathcal{L}$,

$$
\begin{aligned}
\mathcal{T}\left(\phi_{l}(\mathcal{L})\right) & =\left\{(u v \mid S) \text { such that }(u v \mid V \backslash S u v) \in \phi_{l}(\mathcal{L})\right\} \\
& =\left\{(u v \mid S) \text { such that }(u v \mid V \backslash S u v) \in \mathcal{L} \text { and }|V \backslash S u v|=l\right\} \\
& =\left\{(u v \mid S) \text { such that }(u v \mid S) \in \mathcal{T}(\mathcal{L}) \text { and }|V|-|S|-2=l\right\} \\
& =\left\{(u v \mid S) \text { such that }(u v \mid S) \in \mathcal{T}(\mathcal{L}) \text { and }|S|=|V|-l-2\right\} \\
& =\phi_{|V|-l-2}(\mathcal{T}(\mathcal{L}))
\end{aligned}
$$

Lemma 5. Let $\mathcal{L} \in \mathcal{R}(V)$ a pseudographoid and let $G$ and $H$ be, respectively the concentration and the covariance graph associated to $\mathcal{L}$. Then

$$
\mu(\mathcal{L})=|V|-v(\mathcal{T}(\mathcal{L}))-2
$$

Proof. Let $l \geq \mu(\mathcal{L})$, then

$$
\phi_{l}(\mathcal{L})=\phi_{l}(\mathbf{s}(G))
$$

But $\phi_{l}(\mathcal{L})=\phi_{|V|-l-2}(\mathcal{T}(\mathcal{L}))$ according to Lemma 4 and to the fact that $G$ is the covariance graph associated with $\mathcal{T}(\mathcal{L})$. Then

$$
\begin{aligned}
\phi_{|V|-l-2}(\mathcal{T}(\mathcal{L})) & =\phi_{l}(\mathbf{s}(\mathbf{h}(\mathcal{T}(\mathcal{L})))) \\
& =\phi_{|V|-l-2}(\mathcal{T}(\mathbf{s}(\mathbf{h}(\mathcal{T}(\mathcal{L})))))
\end{aligned}
$$

Hence if we denote $\mathcal{L}^{\tau}=\mathcal{T}(\mathcal{L})$ and, we have

$$
\phi_{|V|-l-2}\left(\mathcal{L}^{\tau}\right)=\phi_{|V|-l-2}\left(\mathcal{T}\left(\mathbf{s}\left(\mathbf{h}\left(\mathcal{L}^{\tau}\right)\right)\right)\right)
$$

Hence $|V|-l-2 \leq v\left(\mathcal{L}^{\tau}\right) \Longleftrightarrow l \geq|V|-v\left(\mathcal{L}^{\tau}\right)-2$. Since $\mu$ is the smallest $l$ satisfying (30) then

$$
|V|-v\left(\mathcal{L}^{\top}\right)-2 \leq \mu(\mathcal{L}) \Longleftrightarrow v\left(\mathcal{L}^{\top}\right) \geq|V|-\mu(\mathcal{L})-2
$$

Similarly if we consider $l \leq v\left(\mathcal{L}^{\mathrm{T}}\right)$ and let us write $H^{\mathrm{T}}=\mathbf{h}\left(\mathcal{L}^{\mathrm{T}}\right)=G$ which is the covariance graph associated to $\mathcal{L}^{\mathrm{T}}$. Then

$$
\phi_{l}\left(\mathcal{L}^{\mathrm{T}}\right)=\phi_{l}\left(\mathcal{T}\left(\mathbf{s}\left(H^{\mathrm{T}}\right)\right)\right)
$$

But $\phi_{l}\left(\mathcal{L}^{\mathrm{T}}\right)=\phi_{|V|-l-2}(\mathcal{L})$ and

$$
\phi_{l}\left(\mathcal{T}\left(\mathbf{s}\left(H^{\mathrm{T}}\right)\right)\right)=\phi_{|V|-l-2}\left(\mathbf{s}\left(H^{\mathrm{T}}\right)\right)=\phi_{|V|-l-2}(\mathbf{s}(G))
$$

Hence (32) becomes

$$
\phi_{|V|-l-2}(\mathcal{L})=\phi_{|V|-l-2}(\mathbf{s}(G))
$$

This implies that $|V|-l-2 \geq \mu(\mathcal{L}) \Longleftrightarrow l \leq|V|-\mu(\mathcal{L})-2$. Since $v\left(\mathcal{L}^{\mathrm{T}}\right)$ is the largest integer. Then

$$
v\left(\mathcal{L}^{\mathrm{T}}\right) \leq|V|-\mu(\mathcal{L})-2
$$

Hence the Lemma is proved by combining (31) and (33).
Let us then prove the main result of this section.
Theorem 2. Let $\mathcal{L} \in \mathcal{R}(V)$ be a pseudographoid. Let $G=\mathbf{g}(\mathcal{L})$ and $H=\mathbf{h}(\mathcal{L})$ be respectively the concentration and the covariance graph associated with $\mathcal{L}$. Let $\mu=\mu(\mathcal{L}), v=\mu(\mathcal{L}), s_{G}=\operatorname{so}(G)$ and $s_{H}=\operatorname{so}(H)$. Assume that $G$ and $H$ are connected. Then, the following two inequalities hold

$$
\begin{gathered}
\mu \geq|V|-s_{H}-1 \\
v \leq s_{G}-1
\end{gathered}
$$

Before starting the proof of Theorem 2, we must first prove the following lemma.
Lemma 6. Let $\mathcal{L} \in \mathcal{R}(V)$ be a pseudographoid. Let $G=\mathbf{g}(\mathcal{L})$ and $H=\mathbf{h}(\mathcal{L})$ be the concentration and the covariance graph associated with $\mathcal{L}$. Let $\mu=\mu(\mathcal{L})$ and $s_{H}=\operatorname{so}(H)$. Assume that

$$
\operatorname{so}(H) \leq|V|-\mu(\mathcal{L})-2
$$

then $E \subseteq F$ and for any $u v \notin F$ there exists $S \subseteq V \backslash u v$ such that $(u v \mid S) \in \mathbf{s}(H)$ and $(u v \mid V \backslash S u v) \in \mathbf{s}(G)$.

Proof. Let us assume that (36) holds. Since $\mu(\mathcal{L})$ is an integer that belongs to $\{0, \ldots,|V|-2\}$ then (36) implies that $H$ is necessarily not complete and the set of pairs on non-adjacent vertices in $H \mathcal{V} \backslash F$ is not empty. Let $u v$ be a pair of non-adjacent vertices in $H$, i.e., $u v \notin F$. According to (36) there exists a subset $S \subseteq V$ such that $(u v \mid S) \in \mathbf{s}(H)$ and $|S| \leq|V|-\mu(\mathcal{L})-2$.

We can also write $S$ as follows

$$
S=V \backslash(T u v)
$$

where $T=V \backslash S u v$. By applying the Markov property (17) in Theorem 1, we deduce that $(u v \mid T) \in \mathcal{L}$. Secondly as $|S| \leq|V|-\mu-2$ and $|T|=|V|-|S|-2$, then $|T|=l \geq \mu$ and by using the definition of $\mu$ we deduce that $(u v \mid T) \in \phi_{l}(\mathcal{L})=\phi_{l}(\mathbf{s}(G)))$. Hence $(u v \mid T) \in \mathbf{s}(G)$. So $u \perp_{G} v \mid T$ and then $u \nprec_{G} v$.

We can deduce then that $E \subseteq F$.
We have also proved that for any non-adjacent pair of vertices $u v$ in $H$ we can find a subset $S \subseteq V \backslash u v$ such that $(u v \mid S) \in \mathbf{s}(H)$ and $(u v \mid V \backslash S u v) \in \mathbf{s}(G)$.

Lemma 7. Let $\mathcal{L} \in \mathcal{R}(V)$ be a pseudographoid. Let $G=\mathbf{g}(\mathcal{L})$ and $H=\mathbf{h}(\mathcal{L})$ be respectively the concentration and the covariance graph associated with $\mathcal{L}$. Let $v=\mu(\mathcal{L})$ and $s_{G}=\operatorname{so}(G)$. Assume that

$$
s_{G} \leq v
$$

then $F \subseteq E$ and for any $u v \notin E$ there exists $S \subseteq V \backslash u v$ such that $(u v \mid S) \in \mathbf{s}(G)$ and $(u v \mid V \backslash S u v) \in \mathbf{s}(H)$.

Proof. We will show that the proof of Lemma 7 can be obtained by Lemma 6 to $\mathcal{L}^{\top}=\mathcal{T}(\mathcal{L})$. Let us first assume that (36) holds.

Let us remaind that $\mathbf{g}\left(\mathcal{L}^{\top}\right)=\mathbf{g}(\mathcal{T}(\mathcal{L}))=\mathbf{h}(\mathcal{L})$. By using also Lemma 5 we have $\mu(\mathcal{L})=|V|-\mu\left(\mathcal{L}^{\top}\right)-2$. Hence

$$
\begin{aligned}
\operatorname{so}(G) \leq v(\mathcal{L}) & \Longleftrightarrow \operatorname{so}\left(\mathbf{h}\left(\mathcal{L}^{\top}\right)\right) \leq v\left(\mathcal{T}\left(\mathcal{L}^{\top}\right)\right) \\
& \Longleftrightarrow \operatorname{so}\left(\mathbf{h}\left(\mathcal{L}^{\top}\right)\right) \leq|V|-\mu\left(\mathcal{L}^{\top}\right)-2
\end{aligned}
$$

Hence (36) holds for $\mathcal{L}^{\top}$. By applying Lemma 6 for $\mathcal{L}^{\top}$ we deduce that $H=\mathbf{g}\left(\mathcal{L}^{\top}\right)$ is an undirected graph where the set of edges $F$ is included in $E$ the set of edges of $G=\mathbf{h}\left(\mathcal{L}^{\top}\right)$. The remaining conclusion of the lemma and can be obtained obviously.

Proof of Theorem 2. Note that if $G$ and/or $H$ are complete, there is nothing to prove since in that case, the separability order is equal to $+\infty$, and the inequalities remain satisfied in that case.

Let us first prove that (34) and (35) are equivalent.
Assume that (34) is true for any relation $\mathcal{L}$. Since for any pseudographoid $\mathcal{L}$, the dual of $\mathcal{L}$ which is $\mathcal{T}(\mathcal{L})$ is also a pseudographoid and Hence it satisfies (34):

$$
\mu(\mathcal{T}(\mathcal{L})) \geq|V|-\operatorname{so}(\mathbf{h}(\mathcal{T}(\mathcal{L}))-1
$$

Bu using Lemma 5 we deduce that

$$
=\mu(\mathcal{T}(\mathcal{L}))=|V|-v(\mathcal{T}(\mathcal{T}(\mathcal{L}))-2=|V|-v-2
$$

Then by using (40) and as $\mathbf{h} \circ \mathcal{T}=\mathbf{g}$ the inequality (39) becomes

$$
|V|-v-2 \geq|V|-\operatorname{so}(\mathbf{g}(\mathcal{L}))-1=|V|-\operatorname{so}(G)-1=|V|-s-1 \Rightarrow v \leq s-1
$$

Hence we obtain (35). We have proved that (39) $\Rightarrow$ (40). We similarly also prove that $(40) \Rightarrow(39)$.

Let us now assume that (34) does not hold. Then by equivalence (35) does not hold. We can then assume that (36) and (38). Note that once (36) is satisfied by equivalence (38) is also satisfied. These former inequalities are the principal hypothesis in Lemmas 6 and 7. Let us then apply these lemmas. We deduce that $H=G$ and for any non-adjacent pair of vertices $u v$ in $G$ there exists $S \subseteq V \backslash u v$ where $(u v \mid S)$ and $(u v \mid V \backslash S u v)$ are in $\mathcal{S}(G)$ and where neither $S$ is empty nor $V \backslash S u v$.

Hence we can find four vertices $u_{1}, u_{2}, u_{3}$ and $u_{4}$ in $G$ such that $u_{1} \sim_{G} \sim_{G} u_{2} \sim_{G}$ $u_{3} \sim_{G} u_{4}$ where $u_{2} \in S, u_{3} \in V \backslash S u_{1} u_{4}$ and $u_{1} \nless_{G} u_{4}$. The vertices $u_{1}$ and $u_{3}$ are also not adjacent in $G$. Otherwise, a path exists between $u_{1}$ and $u_{4}$ which is $u_{1} \sim_{G} u_{3} \sim u_{4}$ that does not intersect $S$. Similarly, we can say that $u_{2}$ and $u_{4}$ are not adjacent in $G$. Hence, $\left(u_{1}, u_{3}\right)$ is a pair of non-adjacent vertices in $G$ such that $u_{1} \sim_{G} u_{2} \sim_{G} u_{3}$ is a path connecting these two vertices. Hence any subset $T$ separating $u_{1}$ and $u_{3}$ contains $u_{2}$. However, it will not be possible to $V \backslash T u v$ to separate $u_{1}$ and $u_{3}$ in $G$. We obtain then a contradiction.

The second part now of this section is devoted to device an algorithm allowing us to compute the parameters $\mu$ and $v$ for a giving $\mathcal{L}$. It will then be an algorithm that may help us to verify if a given $\mathcal{L}$ is at the same satisfying the pseudographoid axiom.

The following result concerns relations that satisfy the following two axioms:

1. the semigraphoid axiom: for any triplet $(u, v, w)$ of distinct elements of $V$ and $S \subseteq V \backslash u v w$ such that

$$
\{(u w \mid S),(u v \mid S w)\} \subseteq \mathcal{L} \Longrightarrow\{(u v \mid S),(u w \mid S v)\} \subseteq \mathcal{L}
$$

2. the weak transitive axiom: for any triplet $(u, v, w)$ of distinct elements of $V$ and $S \subseteq V \backslash u v w$ such that

$$
\{(u v \mid S),(u v \mid S w)\} \subseteq \mathcal{L} \Longrightarrow(u w \mid S) \in \mathcal{L} \text { or }(v w \mid S) \in \mathcal{L}
$$

Lemma 8. Let $\mathcal{L} \in \mathcal{R}(V)$ be a relation satisfying the axioms (11), (42) and (41). Let $l \in\{0, \ldots,|V|-2\}$. Let $(u v \mid S) \in \mathcal{L}$. Then the following assertions hold
i. Assume that $\phi_{l+1}(\mathcal{L})=\phi_{l+1}(\mathbf{s}(G))$ and $|S|=l$. Then

$$
(u v \mid S) \in \mathbf{s}(G) \Longleftrightarrow \exists w \in V \backslash S u v \text { such that }(u v \mid S w) \in \mathbf{s}(G)
$$

ii. Assume that $\phi_{l}(\mathcal{L})=\phi_{l}(\mathcal{T}(\mathbf{s}(H)))$ and $|S|=l+1$. Then

$$
(u v \mid S) \in \mathcal{T}(\mathbf{s}(H)) \Longleftrightarrow \exists w \in S \text { such that }(u v \mid S \backslash w) \in \mathbf{s}(H)
$$

Proof. Let us start by proving (i). The left-to-right of the equivalence (43) is indeed obvious. Let us now show the right-to-left way. Hence assume that there exists $w \in V \backslash S u v$ such that $(u v \mid S) \in \mathbf{s}(G)$. Since $|S w|=l+1$ and $\phi_{l+1}(\mathcal{L})=\phi_{l+1}(\mathbf{s}(G))$ then

$$
(u v \mid S) \in \mathcal{L} \text { and }(u v \mid S w) \in \mathcal{L}
$$

Since $\mathcal{L}$ satisfies the weak transitivity axiom (42) we deduce that

$$
(u w \mid S) \in \mathcal{L} \text { or }(v w \mid S) \in \mathcal{L}
$$

Assume that $(u w \mid S) \in \mathcal{L}$. Since $(u v \mid S w) \in \mathcal{L}$ and by applying (41) we deduce that $(u w \mid S v) \in \mathcal{L}$. Since also that $\phi_{l+1}(\mathcal{L})=\phi_{l+1}(\mathbf{s}(G))$ we deduce that $u \perp_{G} w \mid S v$.

As $u \perp_{G} v \mid S w$ and $u \perp_{G} w \mid S v$ then by applying (11) we have $u \perp_{G} v \mid S$.
Let us now prove (ii). We will indeed apply (i) to the relation $\mathcal{T}(\mathcal{L})$, which also satisfies the axioms (11), (42) and (41), and to its concentration graph which is $H$.

Since the equality $\phi_{l}(\mathcal{L})=\phi_{l}(\mathcal{T}(\mathbf{s}(H)))$ and by applying Lemma 4 we obtain

$$
\phi_{|V|-l-2}(\mathcal{T}(\mathcal{L}))=\phi_{|V|-l-2}(\mathbf{s}(H))
$$

Let $l^{\prime}=|V|-l-3$. Then (45) is equivalent to $\phi_{l^{\prime}+1}(\mathcal{T}(\mathcal{L}))=\phi_{l^{\prime}+1}(\mathbf{s}(H))$. Let us then apply (i) to $H$ and $\mathcal{T}(\mathcal{L})$. Then

$$
\begin{aligned}
(u v \mid S) \in \mathcal{T}(\mathbf{s}(H)) & \Longleftrightarrow(u v \mid V \backslash S u v) \in \mathbf{s}(H) \\
& \Longleftrightarrow \quad \exists w \in V \backslash((V \backslash S u v) u v)=S \text { such that }(u v \mid(V \backslash S u v) w) \in \mathbf{s}(H)
\end{aligned}
$$

Since $|V \backslash S u v|=|V|-(l+1)-2=l^{\prime}$. Furthermore the fact that $(u v \mid(V \backslash S u v) w) \in$ $\mathbf{s}(H)$ is equivalent to $(u v \mid S \backslash w) \in \mathcal{T}(\mathbf{s}(H))$. Hence, (ii) is proved.

Lemma 9. Let $\mathcal{L} \in \mathcal{R}(V)$ be a relation satisfying the axioms (11), (42) and (41). Let $\mu$ and $v$ are parameters associated with $\mathcal{L}$. Let $l \in\{0, \ldots,|V|-2\}$.
i. Assume that $l \leq|V|-3$. Assumes that $\phi_{l+1}(\mathcal{L})=\phi_{l+1}(\mathbf{s}(G))$ and let $(u v \mid S) \in \mathcal{L}$ where $|S|=l$, then

$$
(u v \mid S) \in \mathbf{s}(G) \quad \Longleftrightarrow \quad u \nless_{G} v
$$

ii. Assume that $l \geq 1$. Assumes that $\phi_{l-1}(\mathcal{L})=\phi_{l-1}(\mathbf{s}(G))$ and let $(u v \mid S) \in \mathcal{L}$ where $|S|=l$, then

$$
(u v \mid S) \in \mathcal{T}(\mathbf{s}(H)) \Longleftrightarrow u \nrightarrow_{G} v
$$

Proof of Lemma 9. First, we prove (ii) by induction on $l \leq v$.
If $l=1$, then $|S|=1$ and $S=\{w\}$ where $w \in V \backslash u v$. By applying (44) in Lemma 8 we deduce that

$$
\begin{aligned}
(u v \mid S)=(u v \mid w) \in \mathcal{T}(\mathbf{s}(H)) & \Longleftrightarrow(u v \mid \varnothing) \in \mathcal{T}(\mathbf{s}(H)) \\
& \Longleftrightarrow u \nrightarrow_{H} v
\end{aligned}
$$

Assume now that (49) is satisfied for any subset $S$ with cardinality $l$. Let us prove it for $|S|=l+1, \leq v$.

Let us then apply (44) since the hypothesis of Lemma 8 are still satisfied :

$$
(u v \mid S) \in \mathcal{T}(\mathbf{s}(H)) \quad \Longleftrightarrow \quad \exists w \in S \text { such that }(u v \mid S \backslash w) \in \mathbf{s}(H)
$$

Since $|S \backslash w|=l$ and the hypothesis of Lemma 8 are still satisfied. Hence, by applying the induction hypothesis, we can deduce that (49) is still satisfied for $|S|=l+1$. Hence, (ii) is proved.

The proof of (ii) is easily deduced from $(i)$. It is obtained by applying (i) to $G$, which is the covariance associated with $\mathcal{T}(\mathcal{L})$.

Lemma 10. Let $\mathcal{L} \in \mathcal{R}(V)$ be a relation satisfying the axioms (11), (42) and (41). Let $\mu$ and $\nu$ are parameters associated with $\mathcal{L}$. Let $l \in\{0, \ldots,|V|-2\}$.
i. Assume that $l \leq|V|-3$. If $\phi_{l+1}(\mathcal{L})=\phi_{l+1}(\mathbf{s}(G))$. Then

$$
\phi_{l}(\mathcal{L})=\phi_{l}(\mathbf{s}(G)) \quad \Longleftrightarrow \quad \mathbf{V}(\mathbf{s}(G), l)=\mathbf{V}(\mathcal{L}, l) \cap \bar{E}
$$

ii. Assume that $l \geq 1$. If $\phi_{l-1}(\mathcal{L})=\phi_{l-1}(\mathcal{T}(\mathbf{s}(H)))$. Then

$$
\phi_{l}(\mathcal{L})=\phi_{l}(\mathcal{T}(\mathbf{s}(H))) \quad \Longleftrightarrow \quad \mathbf{V}(\mathcal{T}(\mathbf{s}(H)), l)=\mathbf{V}(\mathcal{L}, l) \cap \bar{E}
$$

# 6. Graphical Criteria for Not Belonging to $\mathcal{L}$ 

In this section, we give a graphical criterion from either the concentration and/or the covariance graphs that can be used to determine now which of the couples in $\mathcal{C}(V)$ could not be in the relation $\mathcal{L}$. In other terms, we are giving here the reciprocal way of the global Markov property. If $\mathcal{L}$ is, for example, a relation as the one associated with a random vector and defined in Example 1 this criteria will allow us to read now dependencies statements between a triplet of sub-random vectors. This criterion was also used in [17] but to read dependencies only from covariance graphs.

Definition 4. Let $u v$ be a pair of vertices in an undirected graph $G$ and $n \in \mathbb{N}^{*}$. We say that $u$ and $v$ are $n$-connected given $S$ if there exists exactly $n$ paths $p_{1}, \ldots, p_{n}$ in $\mathcal{P}(u, v, G)$ pairwise disjoints, i.e., $\forall i \neq j\left(p_{i} \cap p_{j}\right) \backslash\{u, v\}=\varnothing$ such that $\forall i=1, \ldots, n p_{i} \subseteq$ Suv. We denote then that $u \sim_{G}^{n} v \mid S$.

The lemma below is needed for the proof of the main result in this paper.
Lemma 11. Let $\mathcal{L} \in \mathcal{R}(V)$ be a pseudographoid. Let $U \subseteq V$. Let us denote by $\mathcal{L}_{U}$ the relation deduced from as following

$$
\mathcal{L}_{U}=\{(u v \mid S) \in \mathcal{L} \text { and } S u v \subseteq U\}
$$

Let us denote by $H$ and $H(U)$ be the covariance graph associated respectively with $\mathcal{L}$ and $\mathcal{L}_{U}$. Then $H(U)=H_{U}$ where $H_{U}$ is the subgraph of $H$ induced on $U$.

Proof. We know that the graph $H(U)$ is defined as follows

$$
u \nless_{H(U)} v \Longleftrightarrow(u v \mid \varnothing) \in \mathcal{L}_{U} \Longleftrightarrow(u v \mid \varnothing) \in \mathcal{L} \Longleftrightarrow u \nless_{H_{U}} v
$$

Hence, the lemma is proved.
The following statements are all the possible contrapositive of the semigrpahoid axiom. Some of them will be needed in the proof of the main result. If $\mathcal{L}$ is a semigraphoid then it satisfies the following statements

$$
\begin{aligned}
& (u w \mid S) \notin \mathcal{L} \text { and }(u v \mid S) \in \mathcal{L} \Longrightarrow,(u w \mid S v) \notin \mathcal{L} \\
& (u w \mid S) \notin \mathcal{L} \text { and }(u w \mid S v) \in \mathcal{L} \Longrightarrow,(u v \mid S) \notin \mathcal{L} \\
& (u v \mid S w) \notin \mathcal{L} \text { and }(u v \mid S) \in \mathcal{L} \Longrightarrow,(u w \mid S v) \notin \mathcal{L} \\
& (u v \mid S w) \notin \mathcal{L} \text { and }(u w \mid S v) \in \mathcal{L} \Longrightarrow,(u v \mid S) \notin \mathcal{L}
\end{aligned}
$$

We now define another family of relations: the graphoids.
Definition 5. A relation $\mathcal{L}$ is called a graphoid if it is at the same a pseudographoid and a semigraphoid.

As we see in the prove above, we will rather use the contrepositive of the weak transitive axiom defined (42).

$$
\begin{aligned}
& \text { If }(u w \mid S) \notin \mathcal{L},(v w \mid S) \notin \mathcal{L} \text { and }(u v \mid S) \in \mathcal{L} \\
& \text { then }(u v \mid S w)\} \notin \mathcal{L}
\end{aligned}
$$

Here is now the last lemma before giving the proof of the main result of this section.
Lemma 12. Let $\mathcal{L} \in \mathcal{R}(V)$ be a graphoid. Let $H$ be the covariance associated with $\mathcal{L}$. Let $u, v \in V$ and $S \subseteq V \backslash u v$. Assume that the following two hypotheses are satisfied
A. $i / \forall w \in S$, any path between $w$ and $v$ contains $u$ and ii/ $u \sim_{H} v$. Then $(u v \mid S) \notin \mathcal{L}$
B. $i / \forall w \in V \backslash S u v$, any path between $w$ and $v$ contains $u$ and ii/ $u \sim_{G} v$. Then $(u v \mid S) \notin \mathcal{L}$

Proof. Let us prove (A).
Let us first deduce from (i) that $\forall w \in S$ the vertices $v$ and $w$ can not be adjacent in $H$ then $(v w \mid \varnothing) \in \mathcal{L}$. We can also deduce from the condition (i) that $(u v \mid \varnothing) \notin \mathcal{L}$.

Secondly, according to (ii), we can deduce that the subset $V \backslash((S \backslash w) w v)=V \backslash S v$ contains $u$ since $u \notin S$ and this later subset intersects any path between $v$ and $w$. Then by using Theorem 1 we deduce that $(v w \mid S \backslash w) \in \mathcal{L}$.

Let prove Lemma 12 by induction on $n=|S|$.
Let us prove the lemma for $n=1$. Let us note that $(u v \mid \varnothing) \notin \mathcal{L}$ and $(v w \mid \varnothing) \in \mathcal{L}$. Hence by applying (50) we deduce that $(u v \mid w) \notin \mathcal{L}$.

Let us assume that the lemma is true for subsets $S$ with cardinality $n$. Let us prove it for $n+1$. Hence assume that $|S|=n+1$. Using the induction hypothesis for all $w \in S$, $(u v \mid S \backslash w) \notin \mathcal{L}$. Assume that $(u v \mid S) \in \mathcal{L}$. Since $S=(S \backslash w) w$. Then by using the induction hypothesis we have $(u v \mid S \backslash w) \notin \mathcal{L}$. Since we have already proved that $(v w \mid S \backslash w) \in \mathcal{L}$, then by using (50) we deduce that $(u v \mid(S \backslash w) w) \notin \mathcal{L}$. Hence $(u w \mid S) \notin \mathcal{L}$.

The part (B) of the lemma is deduced by applying (A) to $\mathcal{T}(\mathcal{L})$ and $G$ which is the covariance graph associated with $\mathcal{T}(\mathcal{L})$.

Let us now give the criteria needed to determine if a couple $(u v \mid S)$ can not be in a relation $\mathcal{L}$. Considering the relations that are derived from probability distributions, we can then be able to determine which relations do not correspond to Conditional Independence statements.

Theorem 3. Let $\mathcal{L} \in \mathcal{R}(V)$ be a relation satisfying the axioms (11), (41) and (42). Let $G$ and $H$ be the concentration and the covariance graph associated with $\mathcal{L}$. Then
i. if $u \sim_{H}^{1} v \mid S$ then $(u v \mid S) \notin \mathcal{L}$
ii. if $u \sim_{G}^{1} v \mid S$ then $(u v \mid V \backslash S u v) \notin \mathcal{L}$

Proof of Theorem 3. Let us first prove (i).
Since $u \sim_{H}^{1} v \mid S$ then there exists a unique path between $u$ and $v$ such that $p \subseteq S \cup\{u, v\}$. Let us prove (i) by induction on $n=|p|$ the length of $p$.

If $n=1$ then $u \sim_{H} v$. We have to prove that

$$
(u v \mid S) \notin \mathcal{L}
$$

Let us now prove (55) by induction on $n=|S|$.
When $|S|=1, S=\{w\}$. Hence, two cases are possible :

$$
w \sim_{H} u \sim_{H} v \text { or } u \sim_{H} v \sim_{H} u
$$

Let us consider the case where $w \sim_{H} u \sim_{H} v$. Note that $w \nless_{H} v$ otherwise it exists another path between $u$ and $v$ different from the path-edge $u \sim_{H} v$. Hence

$$
(u v \mid \varnothing) \notin \mathcal{L} \text { and }(w v \mid \varnothing) \in \mathcal{L}
$$

Let us then apply (50) in the case where $(u, w, v, S=\varnothing)$ then $(u v \mid w) \notin \mathcal{L}$. Then the statement is proved when $|S|=1$.

Let us assume that $(u v \mid S) \notin \mathcal{L}$ when $|S|=n$ and satisfies the hypothesis of Theorem 3. Let us assume now that $|S|=n+1$. Let us denote by $H_{S u v}$ the induced graph of $H$ on $S u v$. Let us then define the following two subsets of $S$ :

$$
S(u)=\left\{w \in S \backslash p \text { such that } \mathcal{P}\left(w, u, H_{S u v}\right) \neq \varnothing \text { and } \mathcal{P}\left(w, v, H_{S}\right)=\varnothing\right\}
$$

and

$$
S(v)=\left\{w \in S \backslash p \text { such that } \mathcal{P}\left(w, u, H_{S u v}\right)=\varnothing \text { and } \mathcal{P}\left(w, v, H_{S}\right) \neq \varnothing\right\}
$$

First we claim that $S=S(u) \cup S(v)$ and that $S(u) \cap S(v)=\varnothing$.
The second statement in our claim is obvious, i.e., $S(u) \cap S(v)=\varnothing$. let us show that $S=S(u) \cup S(v)$.

Let $w \in S$. If $\mathcal{P}\left(u, w, H_{S u v}\right) \neq \varnothing$ and $\mathcal{P}\left(v, w, H_{S u v}\right) \neq \varnothing$ then there exists $p^{\prime} \in \mathcal{P}\left(u, w, H_{S u v}\right)$ and $p^{\prime \prime} \in \mathcal{P}\left(v, w, H_{S u v}\right)$, both of them are included in $H_{S u v}$ and $p=p^{\prime} p^{\prime \prime}$ which is the union of $p^{\prime}$ and $p^{\prime \prime}$ is a path connecting $u$ and $v$ different from the edge path $u \sim_{H} v$. We obtain a contradiction with the fact that a single path exists between $u$ and $v$ in $H$.

Since $S \neq \varnothing$ then either $S(u) \neq \varnothing$ or $S(v) \neq \varnothing$.
Let us assume then that $S(u) \neq \varnothing$. Since for any $w \in S(u), w \nless_{H} v$, then for all $w \in S(u)$ we have $(v w \mid \varnothing) \in \mathcal{L}$. However $(u v \mid \varnothing) \notin \mathcal{L}$. Hence by using Lemma 12 we deduce that

$$
(u v \mid S(u)) \notin \mathcal{L}
$$

Similarly if we assume that $S(v) \neq \varnothing$ we deduce that $(u v \mid S(u)) \notin \mathcal{L}$.
Let $w \in S$. It is easily seen that $S \backslash w$ is a set with cardinality $n$ and satisfying the hypothesis of Theorem 3. Hence, by using the induction hypothesis, we deduce that $(u v \mid S \backslash w) \notin \mathcal{L}$. Assume that $w \in S(u)$. Since there is no path between $w$ and $v$ that does not intersect $u$ then $V \backslash((S \backslash w) w v)$ contains $u$. Hence any path between $w$ and $v$ intersect $V \backslash((S \backslash w) u v)$ in $u$. Then $(v w \mid S \backslash w) \in \mathcal{L}$. We have shown then that

$$
(v w \mid S \backslash w) \in \mathcal{L} \text { and }(u v \mid S \backslash w) \notin \mathcal{L}
$$

Hence by using (50) we deduce that $(u v \mid S) \in \mathcal{L}$ since $S=(S \backslash w) w$.

Let us assume that the result remains true when $p$ is a path with length $n$. Assume now that $|p|=n+1$. Let then $w \in p \backslash u v$. The vertex $w \in S$ as $p \backslash u v \subseteq S$. As

$$
V \backslash((S \backslash w) u v)=(V \backslash(S u v)) w
$$

Hence $p \cap V \backslash((S \backslash w) u v)=w$. Since $p$ is the unique path between $u$ and $v$ then

$$
(u v \mid S \backslash w) \in \mathcal{L}
$$

Since $u \sim_{H}^{1} w \mid S \backslash w$ and $v \sim_{H}^{1} w \mid S \backslash w$ then by applying the induction hypothesis we deduce that $(u w \mid S \backslash w) \notin \mathcal{L}$ and $(v w \mid S \backslash w) \notin \mathcal{L}$.

As $\mathcal{L}$ is a relation satisfying the weak transitivity axiom (42), then by applying (54) we deduce that $(u v \mid S) \notin \mathcal{L}$.

Finally, (ii) is deduced by applying (i) to $\mathcal{T}(\mathcal{L})$.
Let us now consider the following axiom

$$
\{(u v \mid S),(u w \mid S)\} \in \mathcal{L} \Longrightarrow\{(u v \mid S w),(u w \mid S v)\} \in \mathcal{L}
$$

where $u, v, w \in V$ and $S \subseteq V \backslash u v w$. We will say that a relation $\mathcal{L}$ is a gaussoid if it is relation satisfying (11), (41), (42) and (57).

Let us now show there is also another criterion as the one shown in Theorem 3 that can help us to determine elements of $\mathcal{L}$.

Theorem 4. Let $\mathcal{L} \in \mathcal{R}(V)$ be a gaussoid. Let $u, v$ in $V$ and $S \subseteq V \backslash S$. Let us assume that there exists $w \in S$ such that $w \sim_{H}^{1} v \mid S$ and let $p$ be the single path between $v$ and $w$ Then

$$
(u v \mid S) \in \mathcal{L} \Longleftrightarrow(u v \mid S \backslash p) \in \mathcal{L}
$$

Proof. Let us write the proof by induction $n=|p|$.
Let $n=1$ then $w \sim_{H} v$ and $S \backslash p=S \backslash v w=S \backslash w$. We have then to prove (58).
Since any path between $w$ and $u$ should contain $v$ and $S \backslash w$ does not contain $v$. Since $p$ is the only path between $v$ and $w$. Then any path between $w$ and $v$ intersects $S \backslash w$ in $v$. Then, by using Theorem 1 we deduce that $(u w \mid S \backslash w) \in \mathcal{L}$.

Let us assume that $(u v \mid S \backslash w) \notin \mathcal{L}$ and since $(u w \mid S \backslash w) \in \mathcal{L}$ we apply (50) to $(u, w, v, S \backslash w)$ we deduce that $(u v \mid S) \notin \mathcal{L}$.

If we assume now that $(u v \mid S \backslash w) \in \mathcal{L}$ and since $\mathcal{L}$ is a gaussoid then by applying (57) we deduce that $(u v \mid S) \in \mathcal{L}$. Hence the equivalence (58) is proved.

Let us assume that Theorem 4 is true when $p$ is with length equal to $n$, i.e., $|p|=n$ : there are $n$ edges in the path $p$. Assume now that $|p|=n+1$.

Let $w^{\prime} \in p, w \sim_{H} w^{\prime}$. We have also easily noted that $w^{\prime} \sim_{H}^{1} v \mid S \backslash w$. Since $p^{\prime}=p \backslash w$ is a path with $n$ vertices we can apply (58) to $S \backslash w$ and $p^{\prime}$ :

$$
(u v \mid S \backslash w) \in \mathcal{L} \Longleftrightarrow(u v \mid S \backslash w \backslash p^{\prime}) \in \mathcal{L}
$$

However let us note that $(S \backslash w) \backslash p^{\prime}=(S \backslash p) \backslash w$. By induction hypothesis, any path between $w$ and $u$ should contain $\{v\}$. Then $S u v \backslash(S \backslash w) u w=\{v\}$ seprates $u$ and $v$ in $H_{S u v}$. Hence by applying Theorem 1 and Lemma 11, we deduce that $(u w \mid S \backslash w) \in \mathcal{L}$.

Let us assume that $(u v \mid S \backslash w) \notin \mathcal{L}$ and since $(u w \mid S \backslash w) \in \mathcal{L}$, we apply (50) to $(u, w, v, S \backslash w)$ and we deduce that $(u v \mid S) \notin \mathcal{L}$.

If we assume now that $(u v \mid S \backslash w) \in \mathcal{L}$ and since $\mathcal{L}$ is a gaussoid then by applying (57) we deduce that $(u v \mid S) \in \mathcal{L}$.

Hence we have shown that

$$
(u v \mid S \backslash w) \Longleftrightarrow(u v \mid S) \in \mathcal{L}
$$

Hence by using (59) we deduce also that

$$
(u v \mid S) \in \mathcal{L} \Longleftrightarrow(u v \mid(S \backslash p) \backslash w) \in \mathcal{L}
$$

We can also note that $S u v \backslash(((S \backslash p) \backslash w) w u)=p \backslash w u$. Then this former set separates $u$ and $w$ in $H_{S w u}$. Hence $(u w \mid(S \backslash p) \backslash w) \in \mathcal{L}$.

Let us assume that $(u v \mid(S \backslash p) \backslash w) \notin \mathcal{L}$ and since $(u w \mid(S \backslash p) \backslash w) \in \mathcal{L}$ we can apply (50) to $(u, w, v,(S \backslash p) \backslash w)$ we deduce then that $(u v \mid S \backslash p) \notin \mathcal{L}$.

If we assume now that $(u v \mid(S \backslash p) \backslash w) \in \mathcal{L}$ and since $\mathcal{L}$ is a gaussoid then by applying (57) we deduce that $(u v \mid S \backslash p)$. Hence the equivalence (58) is proved.

Corollary 1. Let $\mathcal{L} \in \mathcal{R}(V)$ be a gaussoid and let $G$ and $H$ be respectively the concentration and the covariance graph associated with $\mathcal{L}$. Let $\mu=\mu(\mathcal{L}), v=v(\mathcal{L}), s=\operatorname{so}(G)$ and $t=\operatorname{so}(H)$. Then
i. if $H$ is a cycle, then $v=|V|-3, s_{G} \geq|V|-2, \mu=|V|-2$ and $\mathcal{L}=\mathcal{S}(G) \cup \mathcal{T}(\mathcal{S}(H))$.
ii. if $G$ is a cycle, then $\mu=1, s_{H} \geq|V|-2, v=0$ and $\mathcal{L}=\mathcal{S}(G) \cup \mathcal{T}(\mathcal{S}(H))$.

Proof. Let us prove (i). Assume that $H$ is a cycle. Let $u$ and $v$ two vertices in $H$ and $S \subseteq V \backslash u v$ such $|S|=l \leq|V|-3$ and let us show that

$$
(u v \mid S) \in \mathcal{L} \Longrightarrow u \perp_{H} v \mid V \backslash S u v
$$

Firstly that note that if $l \leq|V|-3$ then the cardinality of $|V \backslash S u v|=|V|-l-2 \geq 1$. Then $V \backslash S u v \neq \varnothing$.

Let us assume, to the contrary, that $u \nmid_{H} v \mid V \backslash S u v$. Then, there exists a path between $u$ and $v$ that does not intersect $V \backslash S u v$. Given that $H$ is a cycle, this path $p$ is unique and is contained within $S u v$. Consequently, $u \sim_{H}^{1} v \mid S$. According to Theorem 3, this implies that $(u v \mid S) \notin \mathcal{L}$, leading to a contradiction. Since $v$ is defined as the largest integer for which $\phi_{l}(\mathcal{L})=\phi_{l}(\mathcal{T}(\mathbf{s}(H)))$, it follows that $v \geq|V|-3$.

Let us denote $\phi_{|V|-2}(\mathcal{T}(\mathbf{s}(H))) \neq \varnothing$, given that $H$ is connected. It is important to note that $v \neq|V|-2$, as $H$ is a connected graph. This means that we cannot find edges that an empty set can separate.

Since $v \leq s_{G}-1$ (as stated in Theorem 2), and we have proven that $v \geq|V|-3$, it follows that $s_{G} \geq|V|-2$. Consequently, if $G$ is not a complete graph, then all separators in $G$ have a cardinality equal to $|V|-2$. Therefore, for all $l=0, \ldots,|V|-3, \phi_{l}(\mathbf{s}(G))=\varnothing$, and $\mathcal{L}$ can include pairs $(u v \mid S) \in \mathcal{L}$ where $|S|=|V|-3$. To establish this, it suffices to select $u$ and $v$ as non-adjacent in $H$. By applying Theorem 3, we can deduce that $(u v \mid S)$ must belong to $\mathcal{L}$.

Let us now prove that $\mathcal{L}=\mathbf{s}(G) \cup \mathcal{T}(\mathbf{s}(H))$. Consider $(u v \mid S) \in \mathcal{L}$. If $|S|=|V|-2$, then $(u v \mid S) \in \phi_{|V|-2}(\mathcal{L})=\phi_{|V|-2}(\mathbf{s}(G)) \subseteq \mathbf{s}(G)$. Given that $s_{G} \geq|V|-2$, it follows that for all $l=0, \ldots,|V|-3, \phi_{l}(\mathbf{s}(G))=\varnothing$. Furthermore, as demonstrated in the first part of this proof, if $(u v \mid S)$ is valid, then $(u v \mid V \backslash S u v) \in \mathbf{s}(H)$. Consequently, we conclude that $\mathcal{L}=\mathbf{s}(G) \cup \mathcal{T}(\mathbf{s}(H))$.

# 7. A Discussion about the Gieger and Pearl Conjecture 

Geiger and Pearl conjectured that for any undirected graph GG, it is possible to construct a probability distribution PP such that

$$
\mathbf{c}(P)=\mathcal{L}
$$

(see [10,27]). This conjecture is particularly relevant in the context of concentration graphical models, where the faithfulness assumption plays a pivotal role. The concept of faithfulness in these models, as defined in relation to Equation (61), is critical, especially when considering the PC algorithms (see [18]). In faithful graphical models, the $0-1$ graph is expected to include, at a minimum, all the edges present in the full conditional independence graph, also known as the concentration graph (see [28]). This relationship underscores the importance

of the faithfulness assumption in accurately representing and analyzing the underlying probabilistic structures in graphical models.

It was also proved in [21] that from any undirected graph $H=(V, F)$ and for a fixed non-negative $\epsilon$ "sufficiently close de zero" we can construct a real positive definite matrix $A^{H, \epsilon}=\left(a_{u v}\right)_{u v \in V \times V}$ as follows

$$
a_{u v}= \begin{cases}1 & \text { if } u=v \\ \epsilon & \text { if } u v \in E \\ 0 & \text { otherwise }\end{cases}
$$

and they showed (see Corollaries $2 \& 3$ in [21]) that $\mathcal{T}(\mathbf{s}(H))=\mathbf{d}\left(A^{H, \epsilon}\right)$. Hence if we consider a random vector $\mathbf{X}$ with Gaussian distribution having $A^{H, \epsilon}$ as a covariance matrix the undirected graph $H$ is then the covariance graph associated with $P$ the probability distribution of $\mathbf{X}$. According to Theorem 2, the separability order of the concentration graph $G$ associated with $P$ is a complete graph, and then $\mathbf{s}(G)=\varnothing$.

On the other hand let now consider an undirected graph $G$ and let us consider $B^{G, \epsilon}=\left(A^{G, \epsilon}\right)^{-1}$ where $\left(A^{G, \epsilon}\right)^{-1}$ is constructed as in (62) and let us consider the random vector $\mathbf{Y}$ as a Gaussian vector with covariance matrix $B^{G, \epsilon}$. According to the construction of $A^{G, \epsilon}$, the undirected graph $G$ is the concentration graph associated to $Q$, the probability distribution of $\mathbf{Y}$. Since $\mathcal{T}(\mathbf{s}(G))=\mathbf{d}\left(A^{H, \epsilon}\right)$, then $\mathbf{s}(G)=\mathcal{T}\left(\mathbf{d}\left(A^{G, \epsilon}\right)\right)=\mathbf{d}\left(B^{G, \epsilon}\right)$. We have applied here Lemma 1 in [21]). By applying also 2 the covariance graph $H$ associated to $Q$ is complete and hence $\mathcal{T}(\mathbf{s}(H))=\varnothing$.

We think then that Geiger and Pearl's conjecture is completely proved.

# 8. Conclusions 

In conclusion, this paper has comprehensively examined the role of undirected graphs in representing sets of Conditional Independence (CI) statements. Through rigorous exploration of properties and implications, we have established that specific axioms govern these sets, providing a mathematical framework for their representation. Our investigation has focused on covariance and concentration graphs, the only known families of undirected graphs capable of comprehensively describing CI statements. We have introduced parameters to assess the limitations of these graphs and provided a computational method for their evaluation. Additionally, we have offered criteria to ascertain the complete representation of CI statements through their corresponding graphs. These findings advance the theoretical understanding of graph theory in statistical contexts and offer practical tools for researchers in related fields. Future work could extend these insights to more complex graph structures or apply them in empirical network data studies. Overall, this research significantly enhances our understanding of the capabilities and limitations of undirected graphs in representing CI statements, making a substantial contribution to the field of graphical models.

## 9. Notations

- $V$ is a finite set
- $|V|$ is the cardinality of $V$
- $E$ is a subset of $V \times V \backslash\{(u, u), u \in V\}$
- $u v$ is the couple $(u, v)$ in $V \times V$
- $G=(V, E)$ is an undirected graph where $V$ is the set of vertices and $E$ is the set of edges that satisfies $u v \in E \Longleftrightarrow v u \in E$
- $\mathcal{P}=\{S, S \subseteq V\}$
- $\mathcal{P}_{k}=\{S, S \subseteq V$ and $|S|=k\}$
- $\mathbf{X}_{V}=\left(X_{v}, v \in V\right)^{\prime}$ is a random vector with values in $\mathbb{R}^{|V|}$
- $X_{S}=\left(X_{s}, s \in V\right)^{\prime}$ is sub-random-vector of $\mathbf{X}_{V}$
- $u \Perp v \mid S$ means that $X_{u} \Perp X_{v} \mid X_{S}$
- $A, B$ and $S$ disjoint subsets of $V, A \Perp B \mid S$ means that $X_{A} \Perp X_{B} \mid X_{S}$
- $\mathbf{S}(G)=\{(A, B, S), S$ separates $A$ and $B$ in $G\}$

- $\quad \mathbf{C}(P)=\{(A, B, S), A \Perp B \mid S\}$
- $(u v \mid S)$ is a couple
- A set of couples $\mathcal{L}$ is called a relation
- If $G=(V, E)$ is an undirect graph $u \sim_{G} v$ means that $u v \in E$ is an edge in $E$.

Funding: This research received no external funding.
Data Availability Statement: No data was used for this research.
Conflicts of Interest: The authors declare no conflict of interest.
