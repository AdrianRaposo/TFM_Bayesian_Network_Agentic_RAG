# THE CHARACTERISTIC IMSET POLYTOPE OF BAYESIAN NETWORKS WITH ORDERED NODES 

JING XI* AND RURIKO YOSHIDA ${ }^{\dagger}$


#### Abstract

In 2010, M. Studený, R. Hemmecke, and S. Linder explored a new algebraic description of graphical models, called characteristic imsets. Compare with standard imsets, characteristic imsets have several advantages: they are still unique vector representative of conditional independence structures, they are $0-1$ vectors, and they are more intuitive in terms of graphs than standard imsets. After defining a characteristic imset polytope (cim-polytope) as the convex hull of all characteristic imsets with a given set of nodes, they also showed that a model selection in graphical models, which maximizes a quality criterion, can be converted into a linear programming problem over the cim-polytope. However, in general, for a fixed set of nodes, the cim-polytope can have exponentially many vertices over an exponentially high dimension. Therefore, in this paper, we focus on the family of directed acyclic graphs (DAGs) whose nodes have a fixed order. This family includes diagnosis models which can be described by Bipartite graphs with a set of $m$ nodes and a set of $n$ nodes for any $m, n \in \mathbb{Z}_{+}$. In this paper, we first consider cim-polytopes for all diagnosis models and show that these polytopes are direct products of simplices. Then we give a combinatorial description of all edges and all facets of these polytopes. Finally, we generalize these results to the cim-polytopes for all Bayesian networks with a fixed underlying ordering of nodes with or without fixed (or forbidden) edges.


Key words. graphical model, characteristic imset polytope, diagnosis model, Bipartite graph, directed acyclic graphs.

AMS subject classifications. 51M20, 52B20, 13P25.

1. Introduction. Bayesian networks (BNs), also known as belief networks, Bayes networks, Bayes(ian) models or probabilistic directed acyclic graphical models, find their applications to model knowledge in many areas, such as computational biology and bioinformatics (gene regulatory networks, protein structure, gene expression analysis [4] learning epistasis from GWAS data sets [5]) and medicine [15]. BNs are a part of the family of probabilistic graphical models (GMs). These graphical structures represent knowledge about probabilistic structures for a statistical model. More precisely, each node in the graph represents a random variable and an edge between the nodes represents probabilistic dependencies among the random variables corresponding to the nodes adjacent to the edge [7]. BNs correspond to GM structure known as a directed acyclic graph (DAG) defined by the set of nodes (vertices) and the set of directed edges.

In order to infer parameters from the observed data set, we first apply a model selection criterion called quality criterion, which provides a way to construct highly predictive BN models from data by choosing the graph which gives the given criteria, such as Bayesian Information Criteria (BIC) [10] or Akaike Information Criteria (AIC) [1], maximum (see [12] for more details on quality criterions). Intuitively a quality criterion is a function, $\mathcal{Q}(G, D)$, which takes a DAG, $G$, and an observed data set, $D$, to evaluate how good the DAG $G$ to explain the observed data $D$. Note that different DAGS, $G_{1}, G_{2}$ may have the same conditional independences (CIs). In that case we say $G_{1}, G_{2}$ are Markov equivalent. When researchers wish to infer the CIs of the BN structure from the observed data set one represents each set of Markov equivalent

[^0]
[^0]:    * Mathematics Department, North Carolina State University, 3600 Univeristy, 2108 SAS Hall, 2311 Stinson Drive Raleigh, NC 27695-8205, U.S.A. (tykiallen@gmail.com).
    ${ }^{\dagger}$ Statistics Department, University of Kentucky, 325 Multidisplinary Science Building, 725 Rose Street Lexington, KY 40536-0082, U.S.A. (ruriko.yoshida@uky.edu)

graphs by one graph called the essential graph the corresponding Markov equivalence class of DAGs [2]. In this paper we focus on quality criterions $\mathcal{Q}(G, D)$, such that $\mathcal{Q}\left(G_{1}, D\right)=\mathcal{Q}\left(G_{2}, D\right)$ if and only if $G_{1}, G_{2}$ are Markov equivalent.

Since in general there are super exponentially many essential graphs with a fixed set of nodes $N$, maximizing the quality criterion, $\mathcal{Q}(G, D)$, over all possible essential graphs with $N$ is known to be NP-hard. Studený developed an algebraic representation of each essential graph $G$ called a standard imset, of $G$, which is an integral vector representation of $G$ in $\mathbb{R}^{2^{|N|}-|N|-1}$. From the view of this setting a criterion function $\mathcal{Q}(G, D)$ is a dot product of vectors in $\mathbb{R}^{2^{|N|}-|N|-1}$. In 2010, M. Studený, J. Vomlel, and R. Hemmecke showed that maximizing the $\mathcal{Q}(G, D)$ over all essential graphs can be formulated as a linear programming problem over the convex hull of standard imsets for all possible essential graphs [14]. This gives us a systematic way to find the best criterion with the optimality certificate rather than finding the best criterion by the brute-force search. Then M. Studený, R. Hemmecke, and S. Linder explored an alternative vector representative of the BN structure, called characteristic imsets. Compare with standard imsets, characteristic imsets have several advantages: they are still unique vector representative of conditional independence structures; they are $0-1$ vectors; and they are more intuitive in terms of graphs than standard imsets [13].

In general, however, the dimension of the convex hull of the characteristic imsets with the fixed set of nodes $N$, called a characteristic imset polytope (cim-polytope), is exponentially large and there are double exponentially many vertices (cim-polytope) as well as facets of the cim-polytope. Thus it is infeasible to optimize by software if $|N|>6$. In order to solve the LP problem for a larger $|N|$, we need to understand the structure of the cim-polytope, such as combinatorial description of edges and facets of the polytope so that we might be able to apply a simplex method to find an optimal solution. However, in general, it is challenging because there are too many facets and too many edges of the polytope. Therefore here we start with a particular family of BN models, namely diagnosis models.

In medical studies, researchers are often interested in probabilistic models in order for them to correctly diagnose a disease from a patient symptoms. The diagnoses models, also known as the Quick Medical Reference (QMR) diagnostic model, is introduced in [11] to diagnose a disease from a given set of symptoms of a patient. Therefore, here we focus on diagnosis models (e.g., [9]). Under this model, a DAG representing the model is a bipartite graph with two sets of nodes, one representing $m$ diseases and one representing $n$ symptoms, and set of directed edges from nodes representing diseases to nodes representing symptoms (see Figure 2.1 for an example).

In this paper, first, we are able to find an explicit combinatorial description of all edges of the cim-polytopes for diagnosis models with fixed $m$ and $n$, that is, if $G_{1}, G_{2}$ are graphs representing two diagnosis models such that all symptoms have the same parents in $G_{1}$ and in $G_{2}$ except one symptom, then the characteristic imsets representing $G_{1}, G_{2}$ form an edge of the cim-polytope for diagnosis models. Then we prove that these cim-polytopes are direct products of $n$ many $\left(2^{m}-1\right)$ dimensional simplices, and an explicit description of all facets of them can be given based on this structure. Finally we generalize these results for the cim-polytopes for BNs with a fixed underlying ordering with or without fixed (or forbidden) edges.

This paper is organized as follows. In Section 2 we introduce notation, and we state some definitions as well as propositions and their proofs. Section 3 shows the description of the cim-polytopes for diagnosis models and Section 4 shows the description of the cim-polytopes for Bayesian networks with a fixed underlying ordering. Proofs

of some of properties, lemmas, and theorems can be found at Section 5, Section 6, and Section 7. We end with a discussion of our future work in Section 8.
2. Definitions and propositions for diagnosis models. In this section we state some notation and remind readers some definitions.

Definition 2.1. A Diagnosis Model can be described by a Bipartite Graph whose nodes $N=\left\{a_{1}, \ldots, a_{m}\right\} \cup\left\{b_{1}, \ldots, b_{n}\right\}$ can be divided into disjoint sets $A=$ $\left\{a_{1}, \ldots, a_{m}\right\}$ and $B=\left\{b_{1}, \ldots, b_{n}\right\}$. Nodes in $A$ can be interpreted as diseases and nodes in $B$ can be interpreted as symptoms. Every single edge can only be drawn from a disease to a symptom. An example is given by Figure 2.1.
For fixed $A$ and $B$, where $|A|=m$ and $|B|=n$, we define notation: $\mathcal{G}_{m, n}=\{$ All possible directed bipartite graphs defined in Definition 2.1 based on $A$ and $B\}$.
![img-0.jpeg](img-0.jpeg)

Figure 2.1. An example of Bipartite Graph, $m=3, n=6$.

Recall that we have the definition of Characteristic Imset.
Definition 2.2. Let $G$ be an acyclic directed graph over $N$. The characteristic imset for $G$ can be introduced as a zero-one vector $c_{G}$ with components $c_{G}(S)$ where $S \subseteq N,|S| \geq 2$ given by

$$
c_{G}(S)=1 \Longleftrightarrow \exists i \in S \text { such that } j \in p a_{G}(i) \text { for } \forall j \in S \backslash\{i\}
$$

where $j \in p a_{G}(i)$ means $G$ includes the edge from $j$ to $i$.
Proposition 2.1. Fix $A=\left\{a_{1}, \ldots, a_{m}\right\}$ and $B=\left\{b_{1}, \ldots, b_{n}\right\}$. Assume $G \in$ $\mathcal{G}_{m, n}$ and $|N|=m+n>2$. Then $c_{G}(T)$ is possible to take value 1 if and only if $T$ has the form of $a_{i_{1}} \ldots a_{i_{k}} b_{j}$, where $1 \leq k \leq m,\left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, m\}$ and $j \in\{1, \ldots, n\}$.

Proof. Notice that $\forall T \subseteq N,|T| \geq 2$, we can write T in the form of:

$$
\begin{aligned}
T=a_{i_{1}} \ldots a_{i_{k}} b_{j_{1}} \ldots b_{j_{l}}, \text { where } & 0 \leq k \leq m,\left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, m\} \\
& 0 \leq l \leq n,\left\{j_{1}, \ldots, j_{l}\right\} \subseteq\{1, \ldots, n\} \\
& k+l \geq 2
\end{aligned}
$$

We need to prove that $l$ can neither be 0 nor greater than 1 , i.e. $l=1$.
(a) If $l=0 . \forall s, t \in\left\{i_{1}, \ldots, i_{k}\right\}$, by Definition $2.1, a_{s} \rightarrow a_{t}$ is not in $G$. This means $a_{s} \notin p a_{G}\left(a_{t}\right)$. Hence $\forall t \in\left\{i_{1}, \ldots, i_{k}\right\}, T \backslash\left\{a_{t}\right\} \nsubseteq p a_{G}\left(a_{t}\right) . c_{G}(T)=0$.
(b) If $l>1$. Similarly with above, by Definition $2.1, \forall s^{\prime}, t^{\prime} \in\left\{j_{1}, \ldots, j_{l}\right\}, b_{s^{\prime}} \notin$ $p a_{G}\left(b_{t^{\prime}}\right)$. Moreover, $\forall t \in\left\{i_{1}, \ldots, i_{k}\right\}$ and $t^{\prime} \in\left\{j_{1}, \ldots, j_{l}\right\}, b_{t^{\prime}} \notin p a_{G}\left(a_{t}\right)$. $c_{G}(T)=0$.

Proposition 2.2. Notation is adopted from Proposition 2.1. Suppose $T$ has the form of $a_{i_{1}} \ldots a_{i_{k}} b_{j}$, where $1 \leq k \leq m,\left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, m\}$ and $j \in\{1, \ldots, n\}$, then $c_{G}(T)=\prod_{s=i_{1}, \ldots, i_{k}} c_{G}\left(a_{s} b_{j}\right)$.

Proof. Again by Definition 2.1, $\forall s, t \in\left\{i_{1}, \ldots, i_{k}\right\}, a_{s} \notin p a_{G}\left(a_{t}\right)$. Therefore:

$$
\begin{aligned}
c_{G}(T)=1 & \Longleftrightarrow\left\{a_{i_{1}} \ldots a_{i_{k}}\right\} \subseteq p a_{G}\left(b_{j}\right) \\
& \Longleftrightarrow a_{s} \in p a_{G}\left(b_{j}\right), \forall s=i_{1}, \ldots, i_{k} \\
& \Longleftrightarrow c_{G}\left(a_{s} b_{j}\right)=1, \forall s=i_{1}, \ldots, i_{k}
\end{aligned}
$$

Recall that $c_{G}(T)$ is binary. Thus $c_{G}(T)=\prod_{s=i_{1}, \ldots, i_{k}} c_{G}\left(a_{s} b_{j}\right)$.
REMARK 2.3. Proposition 2.2 implies that $\forall G \in \mathcal{G}_{m, n}, c_{G}$ is determined by only $m \cdot n$ coordinates, $\left\{c_{G}\left(a_{i} b_{j}\right): i=1, \ldots, m, j=1, \ldots, n\right\}$, i.e. the existence of directed edges $a_{i} \rightarrow b_{j}, i=1, \ldots, m$ and $j=1, \ldots, n$. Another way to see this property is that $\forall G \in \mathcal{G}_{m, n}, G$ can be determined by $p a_{G}\left(b_{j}\right), b_{j} \in B$. Thus if we consider a permutation of coordinates in $c_{G}$ that corresponds to a permutation of $T$ where $T$ has the form in Proposition 2.1, then these coordinates can be broken into $n$ parts:
$a_{1} b_{1}, \ldots, a_{m} b_{1}, \ldots, a_{1} \ldots a_{m} b_{1}, a_{1} b_{2}, \ldots, a_{m} b_{2}, \ldots, a_{1} \ldots a_{m} b_{2}, \ldots, a_{1} b_{n}, \ldots, a_{1} \ldots a_{m} b_{n}$,
where the $s$-th part of coordinations $c_{G}(T), T \in\left\{a_{1} b_{s}, \ldots, a_{m} b_{s}, a_{1} a_{2} b_{s}, \ldots, a_{1} \ldots a_{m} b_{s}\right\}$ only depend on $p a_{G}\left(b_{s}\right)$, and different parts are completely irrelevant in the sense that $p a_{G}\left(b_{s}\right), b_{s} \in B$, can be decided separately.

Proposition 2.4. Fix $m$ and $n$. The number of elements in $\mathcal{G}_{m, n}$ is $2^{m n}$.
Proof. This is trivial because of Remark 2.3 since there are $m n$ possible edges that can be assigned: $a_{i} \rightarrow b_{j}$, where $i=1, \ldots, m$ and $j=1, \ldots, n$, and there are $\sum_{k=0}^{m n}\binom{m n}{k}=2^{m n}$ many possible ways to assign the existence of these edges.

Proposition 2.5. Suppose $G \in \mathcal{G}_{m, n}$. The number of non-zero coordinates in $c_{G}$ is at most $n \cdot\left(2^{m}-1\right)$.

Proof. This result is straightforward from Proposition 2.1 by counting the number of coordinates $c_{G}(T)$, where $T$ has the form shown in Proposition 2.1. Note that when $|T|>m+1, \exists b_{j_{1}}, b_{j_{2}} \in\{1, \ldots, n\}$ s.t. $b_{j_{1}}, b_{j_{2}} \in T$, i.e. $c_{G}(T)=0$ by Proposition 2.1. When $2 \leq|T| \leq m+1$, the number of coordinates of form $c_{G}\left(a_{i_{1}} \ldots a_{i_{\mid T \mid-1}} b_{j}\right)$, where $\left\{i_{1}, \ldots, i_{\mid T \mid-1}\right\} \subseteq\{1, \ldots, m\}$ and $j \in\{1, \ldots, n\}$, is $\binom{m}{|T|-1} \cdot n$. Hence the number of possible non-zero coordinates is:

$$
\sum_{|T|=2}^{m+1}\binom{m}{|T|-1} \cdot n=n \cdot \sum_{k=1}^{m}\binom{m}{k}=n \cdot\left(2^{m}-1\right)
$$

Definition 2.3. Recall several definitions in elementary geometry (see [17] for more details on polyhedral geometry):

- a closed convex polyhedron (which will be indicated as polyhedron for short) in $\mathbb{R}^{q}$ can be defined by a system of linear inequalities:

$$
\left\{\mathbf{x} \in \mathbb{R}^{q}: A \mathbf{x} \leq \mathbf{b}\right\}
$$

where $A$ is a $p \times q$ matrix in $\mathbb{R}^{p \times q}$ and $\mathbf{b}$ is a vector in $\mathbb{R}^{p}$;

- a closed convex polytope (which will be indicated as polytope for short) is defined as the convex hull of a finite set of points;
- if a polyhedron is bounded, then it is a polytope;
- for a polytope $\mathbf{P}$, we define $\operatorname{vert}(\mathbf{P})$ as the set of vertices of $\mathbf{P}$;
- A d-simplex is a d-dimensional polytope which has exactly $d+1$ vertices. It is notated as $\Delta_{d}$.
Let $D A G s(N)$ be the set of all directed acyclic graphs over $N$, and consider a class of graphs $\mathcal{G} \subseteq D A G s(N)$ that contains all graphs which we are interested in. We call

the convex hull of $\left\{c_{G}: G \in \mathcal{G}\right\}, \mathbf{P}_{\mathcal{G}}=\operatorname{conv}\left\{c_{G}: G \in \mathcal{G}\right\}$ the characteristic imset polytope (cim-polytope) for $\mathcal{G}$. Note that it is obvious that $\operatorname{vert}\left(\mathbf{P}_{\mathcal{G}}\right)=\left\{c_{G}: G \in \mathcal{G}\right\}$.

For fixed $A$ and $B$ in Definition 2.1, define $\mathbf{P}_{m, n}:=\mathbf{P}_{\mathcal{G}_{m, n}}$. Proposition 2.5 implies that the dimension of $\mathbf{P}_{m, n}$ is at most $n \cdot\left(2^{m}-1\right)$. We will show that the dimension of $\mathbf{P}_{m, n}$ is actually exactly $n \cdot\left(2^{m}-1\right)$.

# 3. The cim-polytopes for diagnosis models. 

3.1. Combinatorial description of edges on $\mathbf{P}_{m, n}$. Definition 3.1. Consider a class of graphs $\mathcal{G} \subseteq D A G s(N) . \forall G, H \in \mathcal{G}, G$ and $H$ are called neighbors if $c_{G}$ and $c_{H}$ form an edge in $\mathbf{P}_{\mathcal{G}}$, the cim-polytope for $\mathcal{G}$.

Lemma 3.1. Fix $m$. Suppose $G_{1}, G_{2} \in \mathcal{G}_{m, 1}$ are arbitrary two distinct graphs in $\mathcal{G}_{m, 1}$. Then $G_{1}$ and $G_{2}$ are neighbors, i.e. $c_{G_{1}}$ and $c_{G_{2}}$ form an edge in $\mathbf{P}_{m, 1}$.

Proof. See Section 5.
Theorem 3.2. Fix $m$ and $n$. Two graphs, $G_{1}, G_{2} \in \mathcal{G}_{m, n}$ are neighbors if and only if $\exists b_{i} \in B$ such that $p a_{G_{1}}\left(b_{i}\right) \neq p a_{G_{2}}\left(b_{i}\right)$ and $p a_{G_{1}}\left(b_{j}\right)=p a_{G_{2}}\left(b_{j}\right), \forall b_{j} \in B$ and $b_{j} \neq b_{i}$, i.e. all nodes but one have exactly the same parent sets in $G_{1}$ and $G_{2}$.

Proof. See Section 5 .
3.2. $\mathbf{P}_{m, n}$ is a direct product of simplices. Theorem 3.3. Fix $m$ and $n$. For an arbitrary $G \in \mathcal{G}_{m, n}, G$ has $n \cdot\left(2^{m}-1\right)$ many neighbors.

Proof. See Section 5.
REMARK 3.4. Theorem 3.3 implies that every vertex of $\mathbf{P}_{m, 1}$ has $\left(2^{m}-1\right)$ neighbors. Since $\left|\operatorname{vert}\left(\mathbf{P}_{m, 1}\right)\right|=2^{m}$ (by Proposition 2.4), $\mathbf{P}_{m, 1}$ is a simplex with dimension $\left(2^{m}-1\right)$, i.e. $\mathbf{P}_{m, 1}=\Delta_{2^{m}-1}$.

THEOREM 3.5. $\mathbf{P}_{m, n}$ is the direct product of $n$ many $\Delta_{2^{m}-1}$, i.e.

$$
\mathbf{P}_{m, n}=\underbrace{\Delta_{2^{m}-1} \times \Delta_{2^{m}-1} \times \cdots \times \Delta_{2^{m}-1}}_{n \text { many }}
$$

And the $i_{t h}$ simplex is $\mathbf{P}_{m, 1}$ with the same diseases $A$ and only one symptom $\left\{b_{i}\right\}$.
Proof. Fix $m$, we are going to prove the equality by induction on $n$.

- $n=1$. See Remark 3.4;
- Fix $q \in \mathbb{Z}^{+}$. Suppose the equality holds for $\mathbf{P}_{m, n}, \forall n<q$, then we need to prove that it also holds for $\mathbf{P}_{m, q}$. Recall that for $\mathcal{G}_{m, q}$, the symptoms are: $B=\left\{b_{1}, b_{2}, \ldots, b_{q}\right\}$.
First, we need to prove: $\mathbf{P}_{m, q} \subseteq \mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1}$.
Similarly with the proof of Theorem $3.2, \forall G \in \mathcal{G}_{m, q}$, we define graphs:
$-G^{\prime} \in \mathcal{G}_{m,(q-1)}$ with symptoms $B_{m,(q-1)}=B \backslash\left\{b_{q}\right\}$ such that $p a_{G^{\prime}}\left(b_{i}\right)=$ $p a_{G}\left(b_{i}\right), \forall b_{i} \in B_{m,(q-1)}$. This implies $c_{G^{\prime}} \in \mathbf{P}_{m, q-1}$
$-G^{\prime \prime} \in \mathcal{G}_{m, 1}$ with symptom $B_{m, 1}=\left\{b_{q}\right\}$ such that $p a_{G^{\prime \prime}}\left(b_{q}\right)=p a_{G}\left(b_{q}\right)$. This implies $c_{G^{\prime \prime}} \in \mathbf{P}_{m, 1}$.
With a proper permutation of coordinates, we can write $c_{G}$ in the form of:

$$
c_{G}=\left(c_{G^{\prime}}, c_{G^{\prime \prime}}\right)
$$

Recall that $\operatorname{vert}\left(\mathbf{P}_{m, q}\right)=\left\{c_{G}: G \in \mathcal{G}_{m, q}\right\}$, so $\forall x \in \mathbf{P}_{m, q}$, with the same permutation of coordinates, we have:

$$
x=\sum_{G \in \mathcal{G}_{m, q}} \alpha_{G} c_{G}=\left(\sum_{G \in \mathcal{G}_{m, q}} \alpha_{G} c_{G^{\prime}}, \sum_{G \in \mathcal{G}_{m, q}} \alpha_{G} c_{G^{\prime \prime}}\right)
$$

where $0 \leq \alpha_{G} \leq 1, \forall G \in \mathcal{G}_{m, q}$ and $\sum_{G \in \mathcal{G}_{m, q}} \alpha_{G}=1$.

Note that $\sum_{G \in \mathcal{G}_{m, q}} \alpha_{G} c_{G^{\prime}} \in \mathbf{P}_{m, q-1}$ and $\sum_{G \in \mathcal{G}_{m, q}} \alpha_{G} c_{G^{\prime \prime}} \in \mathbf{P}_{m, 1}$, Equation (3.1) implies $x \in \mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1}$. Hence:

$$
\mathbf{P}_{m, q} \subseteq \mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1}
$$

Second, we need to prove: $\mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1} \subseteq \mathbf{P}_{m, q}$.
Let $\mathcal{G}_{m, q-1}$ has symptoms $B_{m,(q-1)}=B \backslash\left\{b_{q}\right\}$ and $\mathcal{G}_{m, 1}$ has symptom $B_{m, 1}=$ $\left\{b_{q}\right\} . \forall G^{\prime} \in \mathcal{G}_{m,(q-1)}$ and $G^{\prime \prime} \in \mathcal{G}_{m, 1}$, we can define $G \in \mathcal{G}_{m, q}$ such that $p a_{G}\left(b_{i}\right)=p a_{G^{\prime}}\left(b_{i}\right), \forall b_{i} \in B_{m,(q-1)}$, and $p a_{G}\left(b_{q}\right)=p a_{G^{\prime \prime}}\left(b_{q}\right) . c_{G}$ has the form of $c_{G}=\left(c_{G^{\prime}}, c_{G^{\prime \prime}}\right)$.
$\forall x \in \mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1}, x$ can be written as:

$$
\begin{aligned}
x & =\left(\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \beta_{G^{\prime}} c_{G^{\prime}}, \sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}} \gamma_{G^{\prime \prime}} c_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}} \beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\left(c_{G^{\prime}}, c_{G^{\prime \prime}}\right) \\
& =\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}}\left(\beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\right) c_{G}
\end{aligned}
$$

where $0 \leq \beta_{G^{\prime}}, \gamma_{G^{\prime \prime}} \leq 1, \forall G^{\prime} \in \mathcal{G}_{m, q-1}, \forall G^{\prime \prime} \in \mathcal{G}_{m, 1}$, and $\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \beta_{G^{\prime}}=1$, $\sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}} \gamma_{G^{\prime \prime}}=1$. Note that

$$
\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}}\left(\beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \beta_{G^{\prime}}\left(\sum_{G^{\prime \prime} \in \mathcal{G}_{m, 1}} \gamma_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{m, q-1}} \beta_{G^{\prime}}=1
$$

which leads to $x \in \mathbf{P}_{m, q}$. Hence:

$$
\mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1} \subseteq \mathbf{P}_{m, q}
$$

Therefore,

$$
\mathbf{P}_{m, q}=\mathbf{P}_{m, q-1} \times \mathbf{P}_{m, 1}=\underbrace{\Delta_{2^{m}-1} \times \cdots \times \Delta_{2^{m}-1}}_{\text {q-1 many }} \times \Delta_{2^{m}-1}=\underbrace{\Delta_{2^{m}-1} \times \cdots \times \Delta_{2^{m}-1}}_{\text {q many }}
$$

Theorem 3.5 implies that $\mathbf{P}_{m, n}$ is a simple polytope with dimension $n \cdot\left(2^{m}-1\right)$. In Section 6, we will give another proof which use linear algebra to show that $\mathbf{P}_{m, n}$ is simple and obtain its dimension. (cim-polytope)
3.3. Expression of facets of $\mathbf{P}_{m, n}$. Based on Theorem 3.5, we are going to show the expression of facets of $\mathbf{P}_{m, n}$ using the following lemma:

Lemma 3.6. [17] Suppose $\mathbf{P}$ is the direct product of simplices $\Delta_{\alpha_{1}}, \ldots, \Delta_{\alpha_{k}}$. Then every facet of $\mathbf{P}$ has the form of $\Delta_{\alpha_{1}} \times \ldots \times \Delta_{\alpha_{i-1}} \times F_{\alpha_{i}} \times \Delta_{\alpha_{i+1}} \times \ldots \times \Delta_{\alpha_{k}}$, where $F_{\alpha_{i}}$ is a facet of $\Delta_{\alpha_{i}}$.

Remark 3.7. Lemma 3.6 implies that in order to study the facets of a direct product of simplices, we can simply study the facets of each simplex. As by Theorem 3.5, $\mathbf{P}_{m, n}$ is a direct product of $n$ many $\mathbf{P}_{m, 1}$, our problem is simplified as studying the facets of $\mathbf{P}_{m, 1}$. Thus we assume $B=\left\{b_{1}\right\}$ in the following content of this section.

Assume $A=\left\{a_{1}, \ldots, a_{m}\right\}$ and $B=\left\{b_{1}\right\}$. By Proposition 2.5, the vertices of $\mathbf{P}_{m, 1}$ has at most $2^{m}-1$ many non-zero coordinates. We define the indeterminates, i.e. variables, $\left\{x_{s}, s \subseteq A, s \neq \emptyset\right\}$, where one indeterminate $x_{s}$ for each coordinate $c_{G}(s \cup$ $\left.\left\{b_{1}\right\}\right)$ in the characteristic imset $c_{G}, G \in \mathcal{G}_{m, 1}$. Define the vector of indeterminates $x=\left\{x_{s}, s \subseteq A, s \neq \emptyset\right\}$. Suppose $A_{m} x \leq b_{m}$ is the system of inequalities that defines $\mathbf{P}_{m, 1}$. We can define a $2^{m} \times 2^{m}$ matrix: $D_{m}=\left[b_{m}\right]-A_{m} \mid$. Denote the

elements in $D_{m}$ by $\left(d_{s t}\right)_{s \subseteq A, t \subseteq A}$ so that we can rewrite the system of inequalities as: $d_{s \emptyset}+\sum_{t \subseteq A, t \neq \emptyset} d_{s t} x_{t} \geq 0, s \subseteq A$. Then we have the expression of $2^{m}$ facets of $\mathbf{P}_{m, 1}$ as following:

$$
F_{s}=\mathbf{P}_{m, 1} \cap\left\{x: d_{s \emptyset}+\sum_{t \subseteq A, t \neq \emptyset} d_{s t} x_{t}=0\right\}, s \subseteq A
$$

where the elements $d_{s t}, s, t \subseteq A$ can be obtained using Theorem 3.8.
Theorem 3.8. The elements in matrix $D_{m}$ satisfies:

- $d_{s t} \neq 0$ if and only if $s \subseteq t$;
- if $s \subseteq t$, then $d_{s t}=(-1)^{|t|-|s|}$.

This implies that $\mathbf{P}_{m, 1}$ has $2^{m}$ facets:

$$
F_{s}=\mathbf{P}_{m, 1} \cap\left\{x: d_{s \emptyset}+\sum_{t \subseteq A, t \neq \emptyset} d_{s t} x_{t}=0\right\}, s \subseteq A
$$

What's more, $\forall s \subseteq A, \operatorname{vert}\left(\mathbf{P}_{m, 1}\right) \backslash\left\{c_{G_{s}}\right\} \subset F_{s}$, where $p a_{G_{s}}\left(b_{1}\right)=s$.
Proof. For convenience, let $x_{\emptyset} \equiv 1 . \forall s \subseteq A$, let $d_{s .}=\left(d_{s t}\right)_{t \subseteq A}$ be the corresponding row of $D_{m}$, and $G_{s}$ be the graph in $\mathcal{G}_{m, 1}$ such that $p a_{G_{s}}\left(b_{1}\right)=s$. Now we can rewrite the system of inequalities as:

$$
\sum_{t \subseteq A} d_{s t} x_{t}=d_{s \cdot}(1 x)^{T} \geq 0, \text { for } \forall s \subseteq A
$$

We are going to prove that $\forall s \subseteq A$, we can find $2^{m}-1$ vertices on $F_{s}$ that are linearly independent, and this implies that $F_{s}$ is a facet of $\mathbf{P}_{m, 1}$. In fact, we will prove that: $\left\{c_{G_{s^{\prime}}}, s^{\prime} \subseteq A, s^{\prime} \neq s\right\} \subset F_{s}$ and $c_{G_{s}} \notin F_{s}$, i.e. $d_{s \cdot}\left(1 c_{G_{s^{\prime}}}\right)^{T}=0, \forall s^{\prime} \subseteq A, s^{\prime} \neq s$ and $d_{s \cdot}\left(1 c_{G_{s}}\right)^{T}>0$.
Notice that $\forall t \subseteq A, c_{G_{s^{\prime}}}\left(t \cup\left\{b_{1}\right\}\right) \neq 0$ if and only if $t \subseteq p a_{c_{G_{s^{\prime}}}}\left(b_{1}\right)=s^{\prime}$, and $d_{s t} \neq 0$ if and only if $s \subseteq t$. So:

$$
d_{s \cdot}\left(1 c_{G_{s^{\prime}}}\right)^{T}=d_{s \emptyset}+\sum_{t \subseteq A, t \neq \emptyset} d_{s t} c_{G_{s^{\prime}}}\left(t \cup\left\{b_{1}\right\}\right)=d_{s \emptyset}+\sum_{s \subseteq t \subseteq s^{\prime}, t \neq \emptyset} d_{s t}=\sum_{s \subseteq t \subseteq s^{\prime}} d_{s t}
$$

Therefore, we have:

- if $s=s^{\prime}$, then $d_{s \cdot}\left(1 c_{G_{s^{\prime}}}\right)^{T}=d_{s s}=1>0$;
- if $s \subsetneq s^{\prime}$, then $d_{s \cdot}\left(1 c_{G_{s^{\prime}}}\right)^{T}=\sum_{s \subseteq t \subseteq s^{\prime}}(-1)^{|t|-|s|}=\sum_{t^{\prime} \subseteq s^{\prime} \backslash s}(-1)^{\left|t^{\prime}\right|}=0$;
- if $s \nsubseteq s^{\prime}$, then $d_{s \cdot}\left(1 c_{G_{s^{\prime}}}\right)^{T}=0$.

ExAmple 3.9 (Facets of $\mathbf{P}_{2,1}$ ). Notation adopted from Theorem 3.8. Fix $m=2$ and $n=1$.
![img-1.jpeg](img-1.jpeg)

All characteristic imsets are given as a matrix:

$$
\begin{aligned}
& T \quad a_{1} b_{1} \quad a_{2} b_{1} \quad a_{1} a_{2} b_{1} \\
& \left(\begin{array}{c}
c_{G_{0}} \\
c_{G_{1}} \\
c_{G_{2}} \\
c_{G_{12}}
\end{array}\right)=\left(\begin{array}{rrr}
0 & 0 & 0 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 1 & 1
\end{array}\right)
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Figure 4.1. Three graphs to illustrate the underlying ordering of graphs

The matrix $D_{2}=\left[b_{2}\left|-A_{2}\right]\right.$ :

$$
D_{2}=\begin{array}{ccccc}
s \backslash t & \emptyset & a_{1} & a_{2} & a_{1} a_{2} & s \backslash t & \emptyset & a_{1} & a_{2} & a_{1} a_{2} \\
\emptyset & \begin{array}{cccc}
1 & -1 & -1 & 1 \\
0 & 1 & 0 & -1 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 1
\end{array} \\
& a_{1} \\
& a_{2} \\
& a_{1} a_{2}
\end{array}\left(\begin{array}{ccccc}
1 & -x_{a_{1}} & -x_{a_{2}} & +x_{a_{1} a_{2}} & \geq 0 \\
& x_{a_{1}} & & -x_{a_{1} a_{2}} & \geq 0 \\
& & x_{a_{2}} & -x_{a_{1} a_{2}} & \geq 0 \\
& & & x_{a_{1} a_{2}} & \geq 0
\end{array}\right)
$$

Vertices $c_{G_{0}}, c_{G_{1}}$ and $c_{G_{12}}$ are in the facet $F_{a_{2}}$ while $c_{G_{2}}$ is not.
4. The cim-polytopes for Bayesian networks. The results in Section 3 are limited to diagnosis models. In this section, we will generalize the results to all Bayesian networks with the same underlying order.
4.1. Underlying ordering of DAGs. For a set of random variables $N=$ $\left\{a_{1}, \ldots, a_{n}\right\}$, where now $n$ is the total number of nodes in $N . \forall G \in D A G s(N)$, there exists an underlying ordering over $N,[n]_{G}=\left(a_{[1]}, \ldots, a_{[n]}\right)$, such that if $a_{[i]} \rightarrow a_{[j]}$ in $G$, then $i<j$. We are are now interested in the class of graphs which share a specific underlying ordering $[n]$, i.e. $\mathcal{G}_{[n]}=\{G \in D A G s(N):[n]_{G}=[n]\}$, and its cim-polytope $\mathbf{P}_{[n]}=\mathbf{P}_{\mathcal{G}_{[n]}}$.

Example 4.1 (Underlying ordering of graphs). Let $N=\left\{a_{1}, a_{2}, a_{3}\right\}$. Consider an ordering over $N,[n]=\left(a_{2}, a_{1}, a_{3}\right)$, i.e. $a_{[1]}=a_{2}, a_{[2]}=a_{1}$ and $a_{[3]}=a_{3}$. Then $\forall G \in \mathcal{G}_{[n]}$, the only type of directed edges allowed in $G$ are $a_{[i]} \rightarrow a_{[j]}$, where $i<j$. For instance, $a_{2} \rightarrow a_{1}$ is allowed while $a_{1} \rightarrow a_{2}$ is not. Thus graph $G_{1}$ in Figure 4.1(a) and graph $G_{2}$ in Figure 4.1(b) are both in $\mathcal{G}_{[n]}$. Graph $G_{3}$ in Figure 4.1(c) is not in $\mathcal{G}_{[n]}$ since it has arrow $a_{1} \rightarrow a_{2}$, and the underlying ordering for $G_{3}$, i.e. $[n]_{G_{3}}$, can either be $\left(a_{1}, a_{2}, a_{3}\right)$ or $\left(a_{1}, a_{3}, a_{2}\right)$.

Remark 4.2. For a specific ordering $[n]$ and an arbitrary $G \in \mathcal{G}_{[n]}$, we have the following proposition that is similar with Proposition 2.2.

- $\forall T \subseteq N,|T|=k \geq 2$, we can order the elements in $T$ according to $[n]$ and write $T$ in the form of $a_{\left[i_{1}\right]} a_{\left[i_{2}\right]} \ldots a_{\left[i_{k}\right]}$ where $i_{1}<i_{2}<\cdots<i_{k}$. Then $c_{G}(T)=\prod_{s=i_{1}, \ldots, i_{k-1}} c_{G}\left(a_{[s]} a_{\left[i_{k}\right]}\right)$. This property means that the whole $c_{G}$ is determined by $\binom{n}{2}$ coordinates, $\left\{c_{G}\left(a_{[i]} a_{[j]}\right), i<j\right\}$, which can also be interpreted as the existence of the directed edges $a_{[i]} \rightarrow a_{[j]}, i<j$.
Another way to see this property is that $\forall G \in \mathcal{G}_{[n]}, G$ can be determined by $p a_{G}\left(a_{[i]}\right)$, $i=2, \ldots, n$ since $p a_{G}\left(a_{[1]}\right)=\emptyset$. Similarly with Remark 2.3, we can consider a permutation of coordinates in $c_{G}$ that corresponds to a permutation of $T$, then these

coordinates can be broken into $n-1$ parts:
$(12),(13),(23),(123),(14),(24),(34), \ldots,(1234), \ldots,(1 n),(2 n), \ldots,((n-1) n), \ldots,(12 \ldots n)$
where $\left(i_{1} \ldots i_{k}\right)$ stands for $T=a_{\left[i_{1}\right]} a_{\left[i_{2}\right]} \ldots a_{\left[i_{k}\right]}, \left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, n\}$. The $k$-th part of the coordinations, $\left\{c_{G}(T): a_{[j]} \notin T, \forall j>k\right\}$ only depend on $p a_{G}\left(a_{[k]}\right)$, and different parts are completely irrelevant in the sense that $p a_{G}\left(a_{[k]}\right), a_{[k]} \in N$, can be decided separately.
4.2. Structure, edges and facets of $\mathbf{P}_{[n]}$. Theorem 4.3. Suppose $n \geq 2$. $\mathbf{P}_{[n]}$ is a direct product of a sequence of simplices:

$$
\mathbf{P}_{[n]}=\underbrace{\Delta_{2^{1}-1} \times \Delta_{2^{2}-1} \times \cdots \times \Delta_{2^{n-1}-1}}_{n-1 \text { simplices }}
$$

where the $i_{t h}$ simplex $\Delta_{2^{i}-1}$ is the same with the cim-polytope for diagnosis models, $\mathbf{P}_{i, 1}$, with diseases $A=\left\{a_{[1]}, \ldots, a_{[i]}\right\}$ and one symptom $\left\{a_{[i+1]}\right\}$.

Proof. See Section 7. 0
REMARK 4.4. Two immediate results from Theorem 4.3 are:

- the dimension of $\mathbf{P}_{[n]}$ is $2^{n}-(n+1)$, and it is a simple polytope;
- the facets of $\mathbf{P}_{[n]}$ can be obtained by Lemma 3.6 and Theorem 3.8.

REMARK 4.5. Note that the equality in Theorem 4.3 is actually $\mathbf{P}_{[n]}=\Delta_{2^{0}-1} \times$ $\Delta_{2^{1}-1} \times \Delta_{2^{2}-1} \times \cdots \times \Delta_{2^{n-1}-1}$, where $\Delta_{2^{0}-1}$ is omitted as it has dimension 0 (a point). Theorem 4.3 and its proof also imply that $\forall x \in \mathbf{P}_{[n]}, x \in \operatorname{vert}\left(\mathbf{P}_{[n]}\right)$ if and only if with the permutation of coordinates in Remark 4.2, $x$ can be written in the form of $x=\left(v_{1}, v_{2}, \ldots, v_{n-1}\right)$, where $v_{i}$ is the vertex of $\Delta_{2^{i}-1}, i=1, \ldots, n-1$. Suppose $x=c_{G}, G \in \mathcal{G}_{[n]}$, then $v_{i}=c_{G_{i}}$, where $G_{i}$ is in $\mathcal{G}_{i, 1}$ with diseases $N_{[i]}$ and symptom $a_{[i+1]}, i=1, \ldots, n-1$, and $p a_{G_{i}}\left(a_{[i+1]}\right)=p a_{G}\left(a_{[i+1]}\right)$.

The following theorem will be stated in two forms which are equivalent by Theorem 4.3 and Lemma 3.1.

THEOREM 4.6. Fix an underlying ordering $[n]$ over $N$.

- (From the view of graph theory.) Two graphs, $G_{1}, G_{2} \in \mathcal{G}_{[n]}$ are neighbors in $\mathcal{G}_{[n]}$ if and only if: $\exists a_{[i]} \in N$ such that $p a_{G_{1}}\left(a_{[i]}\right) \neq p a_{G_{2}}\left(a_{[i]}\right)$ and $p a_{G_{1}}\left(a_{[j]}\right)=p a_{G_{2}}\left(a_{[j]}\right), \forall a_{[j]} \in N$ and $a_{[j]} \neq a_{[i]}$, i.e., all nodes but one have exactly the same parent sets in both $G_{1}$ and $G_{2}$.
- (From the view of polyhedral geometry.) $\forall \mathbf{x} \in \mathbf{P}_{[n]}, \mathbf{x}$ is on an edge of $\mathbf{P}_{[n]}$ if and only if with the permutation of coordinates showed in Remark 4.2 $\mathbf{x}$ can be written in the form of $\mathbf{x}=\left(v_{1}, \ldots, v_{i-1}, e_{i}, v_{i+1}, \ldots, v_{n-1}\right)$, where $e_{i}$ belongs to an edge on $\Delta_{2^{i}-1}, i \in\{1, \ldots, n-1\}$, and $v_{j} \in \operatorname{vert}\left(\Delta_{2^{j}-1}\right)$, $j \in\{1, \ldots, n-1\} \backslash\{i\}$.
Proof. See Section 7. 0
4.3. Graphes with forbidden (or fixed) edges. Fix an underlying ordering of nodes $[n]$ and consider $\mathcal{G}_{[n]}$. When a specific set of directed edges are forbidden in $\mathcal{G}_{[n]}$, we can define sets of nodes $\Omega=\left\{\Omega_{i}^{0}, i=2, \ldots, n\right\} \cup\left\{\Omega_{i}^{1}, i=2, \ldots, n\right\}$ such that $\Omega_{i}^{0} \subseteq \Omega_{i}^{1} \subseteq\left\{a_{[1]}, \ldots, a_{[i-1]}\right\}$, and the class of graphs we are interested in becomes $\mathcal{G}_{[n], \Omega}=\left\{G \in D A G s(N):[n]_{G}=[n], \Omega_{i}^{0} \subseteq p a_{G}\left(a_{[i]}\right) \subseteq \Omega_{i}^{1}, i=2, \ldots, n\right\}$, i.e. edges $\left\{a_{[j]} \rightarrow a_{[i]}: a_{[j]} \in \Omega_{i}^{0}, i=2, \ldots, n\right\}$ are fixed edges, and edges $\left\{a_{[j]} \rightarrow a_{[i]}\right.$ : $\left.a_{[j]} \in\left\{a_{[1]}, \ldots, a_{[i-1]}\right\} \backslash \Omega_{i}^{1}, i=2, \ldots, n\right\}$ are forbidden edges. The cim-polytope for $\mathcal{G}_{[n], \Omega}$ is $\mathbf{P}_{\mathcal{G}_{[n], \Omega}}$. Using similar strategy, we are able to show that $\mathbf{P}_{\mathcal{G}_{[n], \Omega}}$ is a direct

product of a sequence of simplices:
THEOREM 4.7.

$$
\begin{aligned}
& \mathbf{P}_{\mathcal{G}_{[n], \Omega}}=\mathbf{P}_{a_{[2]}} \times \ldots \times \mathbf{P}_{a_{[n]}} \\
& =\underbrace{\Delta_{2^{\left|\Omega_{2}^{1}\right|-\left|\Omega_{2}^{0}\right|}-1} \times \cdots \times \Delta_{2^{\left|\Omega_{2}^{1}\right|-\left|\Omega_{2}^{0}\right|}-1}}_{\text {2 }^{\left|\Omega_{2}^{0}\right|} \text { many }} \times \ldots \times \underbrace{\Delta_{2^{\left|\Omega_{n}^{1}\right|-\left|\Omega_{n}^{0}\right|}-1} \times \cdots \times \Delta_{2^{\left|\Omega_{n}^{1}\right|-\left|\Omega_{n}^{0}\right|}-1}}_{\text {2 }^{\left|\Omega_{n}^{0}\right|} \text { many }},
\end{aligned}
$$

where the $i$-th polytope $\mathbf{P}_{a_{[i+1]}}=\underbrace{\Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1} \times \cdots \times \Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1}}_{\text {2 }^{\left|\Omega_{i+1}^{0}\right|}}$ is a $\left(2^{\left|\Omega_{i+1}^{1}\right|}-\right.$ $\left.2^{\left|\Omega_{i+1}^{0}\right|}\right)$-face of $\mathbf{P}_{\left|\Omega_{i+1}^{1}\right|, 1}=\Delta_{2^{\left|\Omega_{i+1}^{1}\right|}-1}$, where $\mathbf{P}_{\left|\Omega_{i+1}^{1}\right|, 1}$ is the cim-polytope for diagnosis models with diseases $A=\Omega_{i+1}^{1}$ and one symptom $a_{[i+1]}$.

Proof. To prove $\mathbf{P}_{a_{[i+1]}}=\underbrace{\Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1} \times \cdots \times \Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1}}_{\text {2 }^{\left|\Omega_{i+1}^{0}\right|} \text { many }}$, we permutate the coordinates in the following way:

$$
\left\{T: T \subseteq \Omega_{i+1}^{0} \cup a_{[i+1]}\right\} \cup \bigcup_{\Omega_{s} \subseteq \Omega_{i+1}^{0}}\left\{T \subseteq \Omega_{i+1}^{1} \cup a_{[i+1]}: T \cap \Omega_{i+1}^{0}=\Omega_{s}\right\}
$$

i.e. $c_{G}(T), \forall G \in \mathcal{G}_{[n], \Omega}$, can be split into the following subvectors: $\left(c_{G}(T)\right.$, where $T \subseteq \Omega_{i+1}^{0} \cup a_{[i+1]}$ ), $\left(c_{G}(T)\right.$, where $T \subseteq \Omega_{i+1}^{1} \cup a_{[i+1]}$ and $T \cap \Omega_{i+1}^{0}=\Omega_{s}$ ), $\forall \Omega_{s} \subseteq \Omega_{i+1}^{0}$.

Then use the strategy similar with the previous proofs, we can prove the following:

- $c_{G}(T), T \subseteq \Omega_{i+1}^{0} \cup a_{[i+1]}$, are all fixed;
- $\forall \Omega_{s} \subseteq \Omega_{i+1}^{0}$, the convex hull of $\left\{\left(c_{G}(T)\right.\right.$, where $T \subseteq \Omega_{i+1}^{1} \cup a_{[i+1]}$ and $T \cap$ $\left.\left.\Omega_{i+1}^{0}=\Omega_{s}\right): \forall G \in \mathcal{G}_{[n], \Omega}\right\}$ is $\Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1}$ (see Example 4.8);
- $\mathbf{P}_{a_{[i+1]}}=\underbrace{\Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1} \times \cdots \times \Delta_{2^{\left|\Omega_{i+1}^{1}\right|-\left|\Omega_{i+1}^{0}\right|}-1}}_{\text {2 }^{\left|\Omega_{i+1}^{0}\right|} \text { many }}$;
- Equation 4.1 holds.

EXAMPLE 4.8. Consider a $D A G G$ which has 7 nodes $\left\{a_{1}, \ldots, a_{7}\right\}$. After fix an underlying ordering, we can write these nodes as $\left\{a_{[1]}, \ldots, a_{[7]}\right\}$, where $a_{[i]} \rightarrow a_{[j]}$ in $G$ implies $i<j$. Suppose edges $a_{[1]} \rightarrow a_{[6]}$ and $a_{[2]} \rightarrow a_{[6]}$ are fixed and edge $a_{[5]} \rightarrow a_{[6]}$ is forbidden. Then coordinates $c_{G}(T)=0$ if $a_{[5]} \in T$, and other coordinates $c_{G}(T)$ where $a_{[j]} \notin T, \forall j>6$, can be ordered as following (values with respect to different DAGs are listed as a matrix):

$$
{ }^{T \backslash\left\{a_{[6]}\right\}}\left\{\begin{array}{l}
a_{[1]} \\
1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1 \\
\hdashline 1
\end{array}\right.
$$

where the 4 rows correspond to graphs $G_{i}, i=1, \ldots, 4$, such that $p a_{G_{1}}\left(a_{[6]}\right)=$ $\left\{a_{[1]}, a_{[2]}\right\}, p a_{G_{1}}\left(a_{[6]}\right)=\left\{a_{[1]}, a_{[2]}, a_{[3]}\right\}, p a_{G_{1}}\left(a_{[6]}\right)=\left\{a_{[1]}, a_{[2]}, a_{[4]}\right\}$ and $p a_{G_{1}}\left(a_{[6]}\right)=$ $\left\{a_{[1]}, a_{[2]}, a_{[3]}, a_{[4]}\right\}$.

It is obvious that the cim-polytope for diagnosis models, $\mathbf{P}_{m, n}$, is a special case of $\mathbf{P}_{\mathcal{G}_{[n], \Omega}}$ : the underlying ordering of nodes is $\left(a_{1}, \ldots, a_{m}, b_{1}, \ldots, b_{n}\right)$ (the ordering is not unique in the sense that the order of two diseases or two symptoms can exchange),

$\Omega_{i}^{0}=\Omega_{i}^{1}=\emptyset$ for $i=1, \ldots, m$, while $\Omega_{i}^{0}=\emptyset$ and $\Omega_{i}^{1}=\left\{a_{1}, \ldots, a_{m}\right\}$ for $i=m+$ $1, \ldots, m+n$. Note that based on Equation (4.1), all edges of $\mathbf{P}_{\mathcal{G}_{[n], 0}}$ can be found similarly with Theorem 4.6, and the its facets can also be obtained by Lemma 3.6 and Theorem 3.8.

# 5. Proofs in Section 2. 

5.1. Proof of Lemma 3.1. Proof. Let $N=A \cup B$, where $A=\left\{a_{1}, \ldots, a_{m}\right\}$ and $B=\left\{b_{1}\right\}$. We need to prove: $\exists$ a cost vector $w$, such that $w \cdot c_{G_{1}}=w \cdot c_{G_{2}}>w \cdot c_{G_{3}}$, $\forall G_{3} \in \mathcal{G}_{m, 1}$ distinct with $G_{1}$ and $G_{2}$.
By Remark 2.3, $G_{1}$ and $G_{2}$ are determined by $p a_{G_{1}}\left(b_{1}\right)$ and $p a_{G_{2}}\left(b_{1}\right)$, respectively. We will discuss by two scenarios of $p a_{G_{1}}\left(b_{1}\right)$ and $p a_{G_{2}}\left(b_{1}\right)$ : one is a subset of the other, and neither one is a subset of the other.
(1) One is a subset of the other. WLOG, suppose $p a_{G_{1}}\left(b_{1}\right) \subsetneq p a_{G_{2}}\left(b_{1}\right)$.

Define: $A_{1}=p a_{G_{1}}\left(b_{1}\right), A_{2}=p a_{G_{2}}\left(b_{1}\right), A_{2 \backslash 1}=p a_{G_{2}}\left(b_{1}\right) \backslash p a_{G_{1}}\left(b_{1}\right)$, and $A_{\text {comp }}=\left(p a_{G_{2}}\left(b_{1}\right)\right)^{\circ}$ (i.e. the complement set of $p a_{G_{2}}\left(b_{1}\right)$ ). Note that: $A_{2 \backslash 1} \neq \emptyset, A_{1}$ and $A_{\text {comp }}$ can be $\emptyset ; A_{1}, A_{2 \backslash 1}$ and $A_{\text {comp }}$ is a partition of $N$.
Consider a function $w: \mathcal{P}(N) \mapsto \mathbb{R}$ where $w(T)=0$ if $|T|<2$. Then similar with imsets, $w$ can also be considered as a vector, and we assume that the permutations of coordinates in $w$ and in characteristic imsets coincide.

- If $\left|A_{2 \backslash 1}\right|>1$, we define $w$ as:

$$
w(T)= \begin{cases}c & \text { for } \quad T=a_{i} b_{j}, a_{i} \in A_{1} \\ -c & \text { for } \quad T=a_{i} b_{j}, a_{i} \notin A_{1} \\ \left|A_{2 \backslash 1}\right| \cdot c & \text { for } \quad T=A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ 0 & \text { for } \quad T \subset N,|T|>2, \text { and } T \neq A_{2 \backslash 1} \cup\left\{b_{1}\right\}\end{cases}
$$

where $c$ is a positive number.
Then $\forall G_{3} \in \mathcal{G}_{m, 1}$, we have:

$$
\begin{aligned}
w \cdot c_{G_{3}}= & \left|A_{1} \cap p a_{G_{3}}\left(b_{1}\right)\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \backslash A_{1}\right| \cdot c+\left|A_{2 \backslash 1}\right| \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
= & \left|A_{1} \cap p a_{G_{3}}\left(b_{1}\right)\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \\
& +\left|A_{2 \backslash 1}\right| \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) .
\end{aligned}
$$

In this equation:

* $\left|A_{1} \cap p a_{G_{3}}\left(b_{1}\right)\right| \cdot c \leq\left|A_{1}\right| \cdot c$, where " $=$ " holds if and only if $A_{1} \subset$ $p a_{G_{3}}\left(b_{1}\right) ;$
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c+\left|A_{2 \backslash 1}\right| \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}=\emptyset$ or $A_{2 \backslash 1}$;
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap$ $A_{\text {comp }}=\emptyset$.
Therefore, $w \cdot c_{G_{3}} \leq\left|A_{1}\right| \cdot c$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.
- If $\left|A_{2 \backslash 1}\right|=1$, we let $A_{2 \backslash 1}=\left\{a_{q}\right\}$, and define $w$ as:

$$
w(T)= \begin{cases}c & \text { for } \quad T=a_{i} b_{j}, a_{i} \in A_{1} \\ -c & \text { for } \quad T=a_{i} b_{j}, a_{i} \notin A_{2} \\ 0 & \text { for } \quad T=a_{q} b_{1} \\ 0 & \text { for } \quad T \subset N,|T|>2, \text { and } T \neq A_{2 \backslash 1} \cup\left\{b_{1}\right\}\end{cases}
$$

where $c$ is a positive number.

Then $\forall G_{3} \in \mathcal{G}_{m, 1}$, we have:

$$
w \cdot c_{G_{3}}=\left|A_{1} \cap p a_{G_{3}}\left(b_{1}\right)\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c
$$

Again, in this equation:

* $\left|A_{1} \cap p a_{G_{3}}\left(b_{1}\right)\right| \cdot c \leq\left|A_{1}\right| \cdot c$, where " $=$ " holds if and only if $A_{1} \subset$ $p a_{G_{3}}\left(b_{1}\right)$
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap$ $A_{\text {comp }}=\emptyset$.
To satisfy the above two conditions, we must have $p a_{G_{3}}\left(b_{1}\right)=A_{1}$ or $\left(A_{1} \cup a_{q}\right)$. Therefore, again, we have: $w \cdot c_{G_{3}} \leq\left|A_{1}\right| \cdot c$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.
(2) Neither one is a subset of the other.

Define: $A_{1}=p a_{G_{1}}\left(b_{1}\right), A_{2}=p a_{G_{2}}\left(b_{1}\right), A_{1 \cap 2}=p a_{G_{1}}\left(b_{1}\right) \cap p a_{G_{2}}\left(b_{1}\right), A_{1 \backslash 2}=$ $p a_{G_{1}}\left(b_{1}\right) \backslash p a_{G_{2}}\left(b_{1}\right), A_{2 \backslash 1}=p a_{G_{2}}\left(b_{1}\right) \backslash p a_{G_{1}}\left(b_{1}\right), A_{1 \cup 2}=p a_{G_{1}}\left(b_{1}\right) \cup p a_{G_{2}}\left(b_{1}\right)$ and $A_{\text {comp }}=\left(A_{1 \cup 2}\right)^{c}$. Note that: $A_{1 \backslash 2}, A_{2 \backslash 1} \neq \emptyset, A_{1 \cap 2}$ and $A_{\text {comp }}$ can be $\emptyset$; $A_{1 \cap 2}, A_{1 \backslash 2}, A_{2 \backslash 1}$, and $A_{\text {comp }}$ is a partition of $N$.
Consider a function $w$ similar with part (1) that can also be considered as a vector such that the permutations of coordinates in $w$ and in characteristic imsets coincide.

- If $\left|A_{1 \backslash 2}\right|>1$ and $\left|A_{2 \backslash 1}\right|>1$, we define $w$ as:

$$
w(T)= \begin{cases}c & \text { for } T=a_{i} b_{j}, a_{i} \in A_{1 \cap 2} \\ -c & \text { for } T=a_{i} b_{j}, a_{i} \notin A_{1 \cap 2} \\ -2 c & \text { for } T=A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ \left(\left|A_{1 \backslash 2}\right|+1\right) \cdot c & \text { for } T=A_{1 \backslash 2} \cup\left\{b_{1}\right\} \\ \left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c & \text { for } T=A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ 0 & \text { for } & \text { other } T \subset N,|T|>2\end{cases}
$$

where c is a positive number.
Then $\forall G_{3} \in \mathcal{G}_{m, 1}$, we have:

$$
\begin{aligned}
w \cdot c_{G_{3}}= & \left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \\
& +\left(\left|A_{1 \backslash 2}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup\left\{b_{1}\right\}\right)+\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
= & \left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c+\left(\left|A_{1 \backslash 2}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup\left\{b_{1}\right\}\right) \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c+\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c
\end{aligned}
$$

In this equation:

* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \leq\left|A_{1 \cap 2}\right| \cdot c$, where " $=$ " holds if and only if $A_{1 \cap 2} \subset p a_{G_{3}}\left(b_{1}\right)$
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c+\left(\left|A_{1 \backslash 2}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup\left\{b_{1}\right\}\right) \leq c$, where " $=$ " holds if and only if $A_{1 \backslash 2} \subset p a_{G_{3}}\left(b_{1}\right)$;
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c+\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq c$, where " $=$ " holds if and only if $A_{2 \backslash 1} \subset p a_{G_{3}}\left(b_{1}\right)$;
* $-2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq 0$, where " $=$ " holds if and only if $\left(A_{1 \backslash 2} \cup A_{2 \backslash 1}\right) \nsubseteq p a_{G_{3}}\left(b_{1}\right)$;
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap$ $A_{\text {comp }}=\emptyset$.

The above conditions cannot be satisfied simultaneously, but notice that:

* when $p a_{G_{3}}\left(b_{1}\right)=A_{1 \cap 2}, w \cdot c_{G_{3}}=\left|A_{1 \cap 2}\right| \cdot c+0+0+0+0=\left|A_{1 \cap 2}\right| \cdot c$;
* when $p a_{G_{3}}\left(b_{1}\right)=A_{1}$, i.e. $G_{3}=G_{1}, w \cdot c_{G_{3}}=\left|A_{1 \cap 2}\right| \cdot c+c+0+0+0=$ $\left(\left|A_{1 \cap 2}\right|+1\right) \cdot c$
* when $p a_{G_{3}}\left(b_{1}\right)=A_{2}$, i.e. $G_{3}=G_{2}, w \cdot c_{G_{3}}=\left|A_{1 \cap 2}\right| \cdot c+0+c+0+0=$ $\left(\left|A_{1 \cap 2}\right|+1\right) \cdot c$
* when $p a_{G_{3}}\left(b_{1}\right)=A_{1 \cup 2}, w \cdot c_{G_{3}}=\left|A_{1 \cap 2}\right| \cdot c+c+c-2 c+0=\left|A_{1 \cap 2}\right| \cdot c$.

Now it is obvious that $w \cdot c_{G_{3}} \leq\left(\left|A_{1 \cap 2}\right|+1\right) \cdot c$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.

- If only one of $\left|A_{1 \backslash 2}\right|$ and $\left|A_{2 \backslash 1}\right|$ is 1 . Suppose $\left|A_{1 \backslash 2}\right|=1$ and $\left|A_{2 \backslash 1}\right|>1$. We define $w$ as:

$$
w(T)= \begin{cases}c & \text { for } T=a_{i} b_{j}, a_{i} \in A_{1} \\ -c & \text { for } T=a_{i} b_{j}, a_{i} \notin A_{1} \\ -2 c & \text { for } T=A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ \left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c & \text { for } T=A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ 0 & \text { for } \quad \text { other } T \subset N,|T|>2\end{cases}
$$

where $c$ is a positive number.
Then $\forall G_{3} \in \mathcal{G}_{m, 1}$, we have:

$$
\begin{aligned}
w \cdot c_{G_{3}}= & \left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c+\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \\
& +\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right)-2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
= & \left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \\
& +\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c+\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c
\end{aligned}
$$

In this equation:

* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \leq\left|A_{1 \cap 2}\right| \cdot c$, where " $=$ " holds if and only if $A_{1 \cap 2} \subset p a_{G_{3}}\left(b_{1}\right)$;
* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c \leq c$, where " $=$ " holds if and only if $A_{1 \backslash 2} \subset$ $p a_{G_{3}}\left(b_{1}\right)$;
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c+\left(\left|A_{2 \backslash 1}\right|+1\right) \cdot c \cdot c_{G_{3}}\left(A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq c$, where " $=$ " holds if and only if $A_{2 \backslash 1} \subset p a_{G_{3}}\left(b_{1}\right)$;
* $-2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq 0$, where " $=$ " holds if and only if $\left(A_{1 \backslash 2} \cup A_{2 \backslash 1}\right) \nsubseteq p a_{G_{3}}\left(b_{1}\right)$;
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap$ $A_{\text {comp }}=\emptyset$.
The above conditions cannot be satisfied simultaneously, but it is similar with the case of " $\left|A_{1 \backslash 2}\right|>1$ and $\left|A_{2 \backslash 1}\right|>1$ " to show that $w \cdot c_{G_{3}} \leq$ $\left(\left|A_{1 \cap 2}\right|+1\right) \cdot c$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.
- If $\left|A_{1 \backslash 2}\right|=\left|A_{2 \backslash 1}\right|=1$, we define $w$ as:

$$
w(T)= \begin{cases}c & \text { for } T=a_{i} b_{j}, a_{i} \in A_{1 \cup 2} \\ -c & \text { for } T=a_{i} b_{j}, a_{i} \notin A_{1 \cup 2} \\ -2 c & \text { for } T=A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\} \\ 0 & \text { for } \quad \text { other } T \subset N,|T|>2\end{cases}
$$

where c is a positive number.

Then $\forall G_{3} \in \mathcal{G}_{m, 1}$, we have:

$$
\begin{aligned}
w \cdot c_{G_{3}}= & \left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \\
& +\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c+\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c \\
& -2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \\
& -\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c
\end{aligned}
$$

In this equation:

* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \cap 2}\right| \cdot c \leq\left|A_{1 \cap 2}\right| \cdot c$, where " $=$ " holds if and only if $A_{1 \cap 2} \subset p a_{G_{3}}\left(b_{1}\right)$
* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{1 \backslash 2}\right| \cdot c \leq c$, where " $=$ " holds if and only if $A_{1 \backslash 2} \subset$ $p a_{G_{3}}\left(b_{1}\right)$
* $\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{2 \backslash 1}\right| \cdot c \leq c$, where " $=$ " holds if and only if $A_{2 \backslash 1} \subset$ $p a_{G_{3}}\left(b_{1}\right)$
* $-2 c \cdot c_{G_{3}}\left(A_{1 \backslash 2} \cup A_{2 \backslash 1} \cup\left\{b_{1}\right\}\right) \leq 0$, where " $=$ " holds if and only if $\left(A_{1 \backslash 2} \cup A_{2 \backslash 1}\right) \nsubseteq p a_{G_{3}}\left(b_{1}\right)$
* $-\left|p a_{G_{3}}\left(b_{1}\right) \cap A_{\text {comp }}\right| \cdot c \leq 0$, where " $=$ " holds if and only if $p a_{G_{3}}\left(b_{1}\right) \cap$ $A_{\text {comp }}=\emptyset$.
The above conditions cannot be satisfied simultaneously, but it is similar with the case of " $\left|A_{1 \backslash 2}\right|>1$ and $\left|A_{2 \backslash 1}\right|>1$ " to show that: $w \cdot c_{G_{3}} \leq$ $\left(\left|A_{1 \cap 2}\right|+1\right) \cdot c$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.
5.2. Proof of Theorem 3.2. Proof. We will prove "if" and "only if" separately.
(1) Prove "if" part.

Suppose $G_{1}, G_{2} \in \mathcal{G}_{m, n}$, and there exists $b_{i} \in B$ such that $p a_{G_{1}}\left(b_{i}\right) \neq p a_{G_{2}}\left(b_{i}\right)$ and $p a_{G_{1}}\left(b_{j}\right)=p a_{G_{2}}\left(b_{j}\right), \forall b_{j} \in B, b_{j} \neq b_{i}$. We need to prove $G_{1}$ and $G_{2}$ are neighbors.
Consider an arbitrary graph $G_{3} \in \mathcal{G}_{m, n}$. We need to prove: $\exists$ a cost vector $w$ such that $w \cdot c_{G_{1}}=w \cdot c_{G_{2}} \geq w \cdot c_{G_{3}}$, where " $=$ " holds if and only if $G_{3}=G_{1}$ or $G_{2}$.
Define the following graphs (a graphical example will be given in Remark 5.1):

- $G_{1}^{\prime}, G_{2}^{\prime}, G_{3}^{\prime} \in \mathcal{G}_{m, 1}$ with symptom $B_{m, 1}=\left\{b_{i}\right\}$ such that $p a_{G_{1}^{\prime}}\left(b_{i}\right)=$ $p a_{G_{1}}\left(b_{i}\right), p a_{G_{2}^{\prime}}\left(b_{i}\right)=p a_{G_{2}}\left(b_{i}\right)$ and $p a_{G_{3}^{\prime}}\left(b_{i}\right)=p a_{G_{3}}\left(b_{i}\right)$
- $G_{0}, G_{3}^{\prime \prime} \in \mathcal{G}_{m,(n-1)}$ with symptoms $B_{m,(n-1)}=B \backslash\left\{b_{i}\right\}$ such that $p a_{G_{0}}\left(b_{j}\right)=$ $p a_{G_{1}}\left(b_{j}\right)=p a_{G_{2}}\left(b_{j}\right)$ and $p a_{G_{3}^{\prime \prime}}\left(b_{j}\right)=p a_{G_{3}}\left(b_{j}\right), \forall b_{j} \in B_{m,(n-1)}$.
By Remark 2.3, with a proper permutation of coordinates, we can write the characteristic imsets of $G_{1}, G_{2}$ and $G_{3}$ in the form of:

$$
\begin{aligned}
& c_{G_{1}}=\left(c_{G_{1}^{\prime}}, \quad c_{G_{0}}\right) \\
& c_{G_{2}}=\left(c_{G_{2}^{\prime}}, \quad c_{G_{0}}\right) \\
& c_{G_{3}}=\left(c_{G_{3}^{\prime}}, \quad c_{G_{3}^{\prime \prime}}\right)
\end{aligned}
$$

- By Lemma 3.1, $G_{1}^{\prime}$ and $G_{2}^{\prime}$ are neighbors, i.e. $\exists$ a cost vector $w_{1}$ such that $w_{1} \cdot c_{G_{1}^{\prime}}=w_{1} \cdot c_{G_{2}^{\prime}} \geq w_{1} \cdot c_{G_{3}^{\prime}}, \forall G_{3}^{\prime} \in \mathcal{G}_{m, 1}$, where " $=$ " holds if and only if $G_{3}^{\prime}=G_{1}^{\prime}$ or $G_{2}^{\prime}$.
- Since $c_{G_{0}} \in \operatorname{vert}\left(\mathbf{P}_{\mathcal{G}_{m,(n-1)}, c}\right), \exists$ a cost vector $w_{2}$ such that $w_{2} \cdot c_{G_{0}} \geq$ $w_{2} \cdot c_{G_{2}^{\prime \prime}}, \forall G_{3}^{\prime \prime} \in \mathcal{G}_{m,(n-1)}$, where " $=$ " holds if and only if $G_{3}^{\prime \prime}=G_{0}$.

Let $w=\left(w_{1} w_{2}\right)$. We have:

$$
\begin{aligned}
w \cdot c_{G_{1}} & =w_{1} \cdot c_{G_{1}^{\prime}}+w_{2} \cdot c_{G_{0}} \\
& =w_{1} \cdot c_{G_{2}^{\prime}}+w_{2} \cdot c_{G_{0}}=w \cdot c_{G_{2}} \\
& \geq w_{1} \cdot c_{G_{3}^{\prime}}+w_{2} \cdot c_{G_{3}^{\prime \prime}}=w \cdot c_{G_{3}}
\end{aligned}
$$

where " $=$ " holds if and only if i) $G_{3}^{\prime}=G_{1}^{\prime}$ or $G_{2}^{\prime}$, and ii) $G_{3}^{\prime \prime}=G_{0}$, i.e. $G_{3}=G_{1}$ or $G_{2}$.
(2) Prove "only if" part.

Suppose $G_{1}, G_{2} \in \mathcal{G}_{m, n}$ are neighbors. i.e. $\exists$ a cost vector $w$ such that $w \cdot c_{G_{1}}=w \cdot c_{G_{2}}>w \cdot c_{G}, \forall G \in \mathcal{G}_{m, n}, G \neq G_{1}, G_{2}$. We are going to prove this part by contradiction.
Suppose $\exists b_{i}, b_{j} \in B$ distinct, $p a_{G_{1}}\left(b_{i}\right) \neq p a_{G_{2}}\left(b_{i}\right)$ and $p a_{G_{1}}\left(b_{j}\right) \neq p a_{G_{2}}\left(b_{j}\right)$.
Define the following graphs (a graphical example will be given in Remark 5.1):

- $G_{1}^{\prime}, G_{2}^{\prime} \in \mathcal{G}_{m, 1}$ with symptom $B_{m, 1}=\left\{b_{i}\right\}$ such that $p a_{G_{1}^{\prime}}\left(b_{i}\right)=p a_{G_{1}}\left(b_{i}\right)$ and $p a_{G_{2}^{\prime}}\left(b_{i}\right)=p a_{G_{2}}\left(b_{i}\right)$
- $G_{1}^{\prime \prime}, G_{2}^{\prime \prime} \in \mathcal{G}_{m, 1}$ with symptom $B_{m, 1}=\left\{b_{j}\right\}$ such that $p a_{G_{1}^{\prime \prime}}\left(b_{j}\right)=$ $p a_{G_{1}}\left(b_{j}\right)$ and $p a_{G_{2}^{\prime \prime}}\left(b_{j}\right)=p a_{G_{2}}\left(b_{j}\right)$
- $G_{1}^{\prime \prime \prime}, G_{2}^{\prime \prime \prime} \in \mathcal{G}_{m,(n-2)}$ with symptoms $B_{m,(n-2)}=B \backslash\left\{b_{i}, b_{j}\right\}$ such that $p a_{G_{1}^{\prime \prime \prime}}\left(b_{k}\right)=p a_{G_{1}}\left(b_{k}\right)$ and $p a_{G_{2}^{\prime \prime \prime}}\left(b_{k}\right)=p a_{G_{2}}\left(b_{k}\right), \forall b_{k} \in B_{m,(n-2)}$;
- $G_{3} \in \mathcal{G}_{m, n}$ is all the same with $G_{1}$ but $p a_{G_{3}}\left(b_{i}\right)=p a_{G_{3}}\left(b_{i}\right)$;
- $G_{4} \in \mathcal{G}_{m, n}$ is all the same with $G_{1}$ but $p a_{G_{4}}\left(b_{j}\right)=p a_{G_{4}}\left(b_{j}\right)$;
- $G_{5} \in \mathcal{G}_{m, n}$ is all the same with $G_{2}$ but $p a_{G_{5}}\left(b_{i}\right)=p a_{G_{1}}\left(b_{i}\right)$ and $p a_{G_{5}}\left(b_{j}\right)=$ $p a_{G_{1}}\left(b_{j}\right)$, notice that $G_{5}$ might be same with $G_{1}$.
Similarly with part (1), with a proper permutation of coordinates, we can write the characteristic imsets of $G_{1}, G_{2}, G_{3}, G_{4}$ and $G_{5}$ in the following form:

$$
\begin{aligned}
& c_{G_{1}}=\left(c_{G_{1}^{\prime}}, \quad c_{G_{1}^{\prime \prime}}, \quad c_{G_{1}^{\prime \prime \prime}}\right) \\
& c_{G_{2}}=\left(c_{G_{2}^{\prime}}, \quad c_{G_{2}^{\prime \prime}}, \quad c_{G_{2}^{\prime \prime \prime}}\right) \\
& c_{G_{3}}=\left(c_{G_{3}^{\prime}}, \quad c_{G_{1}^{\prime \prime}}, \quad c_{G_{1}^{\prime \prime \prime}}\right) \\
& c_{G_{4}}=\left(c_{G_{1}^{\prime}}, \quad c_{G_{2}^{\prime \prime}}, \quad c_{G_{1}^{\prime \prime \prime}}\right) \\
& c_{G_{5}}=\left(c_{G_{1}^{\prime}}, \quad c_{G_{1}^{\prime \prime}}, \quad c_{G_{2}^{\prime \prime \prime}}\right)
\end{aligned}
$$

With the same permutation of coordinates, $w$ can be written as $w=\left(w_{1} w_{2} w_{3}\right)$. Thus we have:
$-G_{3} \neq G_{1}$ or $G_{2}$, which implies:

$$
\begin{aligned}
& w \cdot c_{G_{1}}=w_{1} \cdot c_{G_{1}^{\prime}}+w_{2} \cdot c_{G_{1}^{\prime \prime}}+w_{3} \cdot c_{G_{1}^{\prime \prime}} \\
& >w \cdot c_{G_{3}}=w_{1} \cdot c_{G_{2}^{\prime}}+w_{2} \cdot c_{G_{1}^{\prime \prime}}+w_{3} \cdot c_{G_{1}^{\prime \prime \prime}} \\
& \Longrightarrow w_{1} \cdot c_{G_{1}^{\prime}}>w_{1} \cdot c_{G_{2}^{\prime}}:
\end{aligned}
$$

$-G_{4} \neq G_{1}$ or $G_{2}$, which implies:

$$
\begin{aligned}
& w \cdot c_{G_{1}}=w_{1} \cdot c_{G_{1}^{\prime}}+w_{2} \cdot c_{G_{1}^{\prime \prime}}+w_{3} \cdot c_{G_{1}^{\prime \prime \prime}} \\
& >w \cdot c_{G_{4}}=w_{1} \cdot c_{G_{1}^{\prime}}+w_{2} \cdot c_{G_{2}^{\prime \prime}}+w_{3} \cdot c_{G_{1}^{\prime \prime \prime}} \\
& \Longrightarrow w_{2} \cdot c_{G_{1}^{\prime \prime}}>w_{2} \cdot c_{G_{2}^{\prime \prime}}
\end{aligned}
$$

There is a contradiction:

$$
\begin{aligned}
& w \cdot c_{G_{2}}=w_{1} \cdot c_{G_{2}^{\prime}}+w_{2} \cdot c_{G_{2}^{\prime \prime}}+w_{3} \cdot c_{G_{2}^{\prime \prime \prime}} \\
& \Longrightarrow w \cdot c_{G_{2}}<w \cdot c_{G_{5}}
\end{aligned}
$$

Therefore $G_{1}$ and $G_{2}$ cannot be neighbors.
REMARK 5.1. Two graphical examples will be given for a more intuitive view of the proof of Theorem 3.2.

- Part (1), the proof of "if" statement. In Figure 5.1, $m=4, n=3$ and $b_{i}=b_{1}$.
![img-3.jpeg](img-3.jpeg)

Figure 5.1. An example for the proof of Theorem 3.2, part (1)

- Part (2), the proof of "only if" statement. In Figure 5.2, $m=4, n=3$, $b_{i}=b_{1}$ and $b_{j}=b_{2}$.
5.3. Proof of Theorem 3.3. Proof. By Theorem 3.2, $\forall H \in \mathcal{G}_{m, n}, G$ and $H$ are neighbors if and only if: $\exists b_{k} \in B$ such that $p a_{G}\left(b_{k}\right) \neq p a_{H}\left(b_{k}\right)$ and $p a_{G}\left(b_{j}\right)=$ $p a_{H}\left(b_{j}\right), \forall b_{j} \in B$ and $b_{j} \neq b_{k}$.

Now fix $b_{i} \in B$. Define graphs:

- $G^{\prime}, H^{\prime} \in \mathcal{G}_{m, 1}$ with symptom $B_{m, 1}=\left\{b_{i}\right\}$ such that $p a_{G^{\prime}}\left(b_{i}\right)=p a_{G}\left(b_{i}\right)$ and $p a_{H^{\prime}}\left(b_{i}\right)=p a_{H}\left(b_{i}\right)$
- $G^{\prime \prime}, H^{\prime \prime} \in \mathcal{G}_{m,(n-1)}$ with symptoms $B_{m,(n-1)}=B \backslash\left\{b_{i}\right\}$ such that $p a_{G^{\prime \prime}}\left(b_{j}\right)=$ $p a_{G}\left(b_{j}\right)$ and $p a_{H^{\prime \prime}}\left(b_{j}\right)=p a_{H}\left(b_{j}\right), \forall b_{j} \in B_{m,(n-1)}$.
Since $G$ and $H$ are neighbors and $G^{\prime} \neq H^{\prime}$ will lead to $G^{\prime \prime}=H^{\prime \prime}$, and by Proposition 2.4 there are $2^{m}$ graphs in $\mathcal{G}_{m, 1}$, there are $2^{m}-1$ different choices of $H^{\prime} \mathrm{s}$, and each corresponds to a different neighbor of $G$.

We can use the same strategy for every $b_{i} \in B$, i.e. we can find $2^{m}-1$ neighbors from each fixed $b_{i} \in B$. It is easy to see that these neighbors are all distinct: if $H_{1}$, $H_{2}$ are all the same with $G$ but $p a_{G}\left(b_{i}\right) \neq p a_{H_{1}}\left(b_{i}\right)$ and $p a_{G}\left(b_{j}\right) \neq p a_{H_{2}}\left(b_{j}\right)$, where $b_{i}, b_{j} \in B$ are distinct, then this implies $p a_{H_{2}}\left(b_{i}\right)=p a_{G}\left(b_{i}\right) \neq p a_{H_{1}}\left(b_{i}\right)$, i.e. $H_{1}$ and $H_{2}$ are different. Therefore the total number of neighbors for $G$ is: $n \cdot\left(2^{m}-1\right)$.

![img-4.jpeg](img-4.jpeg)

Figure 5.2. An example for the proof of Theorem 3.2, part (2)
6. Prove $\mathbf{P}_{m, n}$ is simple using linear algebra. Recall that in Section 3, we first proved that $\mathbf{P}_{m, 1}$ is a simplex $\Delta_{2^{m}-1}$, and then we proved that $\mathbf{P}_{m, n}$ is a direct product of $n$ many $\Delta_{2^{m}-1}$, which implies that $\mathbf{P}_{m, n}$ is a simple polytope with dimension $n \cdot\left(2^{m}-1\right)$. Now we are going to show another flow to prove that $\mathbf{P}_{m, n}$ is simple.

First, we will use linear algebra to show that $\mathbf{P}_{m, n}$ has dimension $n \cdot\left(2^{m}-1\right)$. We adopt the notation from Section 3. Given $N$, by Proposition 2.1 and Proposition 2.5 , we can define $\mathcal{S}_{m, n}$ as the support of $\left\{c_{G}: G \in \mathcal{G}_{m, n}\right\}$, i.e.:

$$
\mathcal{S}_{m, n}=\left\{T: \exists G \in \mathcal{G}_{m, n} \text { such that } c_{G}(T)=1\right\} \subset \mathcal{P}(N)
$$

where $\mathcal{P}(N)$ is the power set of $N$.
Theorem 6.1. Fix $m$ and $n$. The dimension of $\mathbf{P}_{m, n}$ is exactly $n \cdot\left(2^{m}-1\right)$.
Proof. Similar with imsets, we can consider the standard basis $\mathbf{e}_{\mathbf{T}}, T \subset N$, as functions $\mathbf{e}_{\mathbf{T}}: \mathcal{P}(N) \mapsto \mathbb{Z}$ such that $\forall T_{0} \subset N, \mathbf{e}_{\mathbf{T}}\left(T_{0}\right)=1$ if $T_{0}=T$, and 0 otherwise. Each $\mathbf{e}_{\mathbf{T}}$ can also be considered as a vector with coordinates $T_{0} \subset N$.

It is obvious that: 1 ) $\left\{c_{G}, G \in \mathcal{G}_{m, n}\right\} \subset \mathbb{R}^{2^{m+n}-(m+n+1)}$; 2 ) $\left\{\mathbf{e}_{\mathbf{T}}, T \in \mathcal{S}_{m, n}\right\}$ is a basis of $\mathbb{R}^{n \cdot\left(2^{m}-1\right)}$ that is embedded in $\mathbb{R}^{2^{m+n}-(m+n+1)}$ (Proposition 2.5); and 3 ) $\left\{c_{G}, G \in \mathcal{G}_{m, n}\right\}$ can be written as a linear combination of $\left\{\mathbf{e}_{\mathbf{T}}, T \in \mathcal{S}_{m, n}\right\}$. We are going to prove that $\left\{\mathbf{e}_{\mathbf{T}}, T \in \mathcal{S}_{m, n}\right\}$ can be expressed as a linear combination of $\left\{c_{G}\right.$, $\left.G \in \mathcal{G}_{m, n}\right\}$. Notice that $\left\{\mathbf{e}_{\mathbf{T}}, T \in \mathcal{S}_{m, n}\right\}$ is equivalent with $\left\{\mathbf{e}_{\mathbf{T}}, T \subset N\right.$ and $T$ has the form of $a_{i_{1}} \ldots a_{i_{k}} b_{j}$, where $1 \leq k \leq m,\left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, m\}$ and $j \in\{1, \ldots, n\}\}$ (Proposition 2.1), we can prove the statement by induction on $|T|$.

- When $|T|=2$ (i.e. $k=1$ ), i.e. $T=a_{i} b_{j}$, where $a_{i} \in A$ and $b_{j} \in B$, we know $c_{G}=\mathbf{e}_{\mathbf{T}}$, where $G \in \mathcal{G}_{m, n}$ has only one edge $a_{i} \rightarrow b_{j}$.
- Suppose $\forall T, T$ has the form in Proposition 2.1 and $|T| \leq k, \mathbf{e}_{\mathbf{T}}$ can be written as a linear combination of $\left\{c_{G}, G \in \mathcal{G}_{m, n}\right\}$. Now consider $T_{k}=a_{i_{1}} \ldots a_{i_{k}} b_{j}$, where $\left\{i_{1}, \ldots, i_{k}\right\} \subseteq\{1, \ldots, m\}$ and $j \in\{1, \ldots, n\}$.
Let $G \in \mathcal{G}_{m, n}$ have $k$ edges: $a_{i_{l}} \rightarrow b_{j}, l=1 \ldots k$. Then:

$$
\mathbf{e}_{\mathbf{T}_{\mathbf{k}}}=c_{G}-\sum_{T_{a} \subset\left\{a_{i_{1}}, \ldots, a_{i_{k}}\right\}, 0<\left|T_{a}\right|<k} \mathbf{e}_{\mathbf{T}_{\mathbf{a}} \cup\left\{\mathbf{b}_{\mathbf{j}}\right\}}
$$

Since $\forall T_{a} \subset\left\{a_{i_{1}}, \ldots, a_{i_{k}}\right\}, 0<\left|T_{a}\right|<k$ (i.e. $T_{a} \subsetneq\left\{a_{i_{1}}, \ldots, a_{i_{k}}\right\}$ ), $\left|T_{a} \cup\right.$ $\left.b_{j}\right| \leq k, \mathbf{e}_{\mathbf{T}_{\mathbf{a}} \cup \mathbf{b}_{\mathbf{j}}}$ can be expressed as a linear combination of $\left\{c_{G}, G \in \mathcal{G}_{m, n}\right\}$. Therefore, $\mathbf{e}_{\mathbf{T}_{\mathbf{k}}}$ can be written as a linear combination of $\left\{c_{G}, G \in \mathcal{G}_{m, n}\right\}$.

A special case of $n=1$ in Theorem 6.1 and Proposition 2.4 claims that $\mathbf{P}_{m, 1}$ has $2^{m}$ vertices and dimension $2^{m}-1$. This directly lead to Corollary 6.2.

Corollary 6.2. Fix $m, \mathbf{P}_{m, 1}$ is a simplex with dimension $2^{m}-1$, i.e. $\mathbf{P}_{m, 1}=$ $\Delta_{2^{m}-1}$.

Lemma 3.1 is an immediate result of Corollary 6.2, while Theorem 3.3 and Theorem 3.5 can be obtained based on Lemma 3.1 and Corollary 6.2 using the same proofs in Section 3. It is worth mentioning that Theorem 6.1 and Theorem 3.3 imply that $\mathbf{P}_{m, n}$ is a simple polytope with dimension $n \cdot\left(2^{m}-1\right)$ because the number of neighbors for each vertex equals to the dimension of the polytope. In 2000, V. Kaibel and M. Wolff proved that a zero-one polytope is simple if and only if it equals to a direct product of zero-one simplices [6]. Recall that cim-polytopes are zero-one polytopes, we are able to conclude that $\mathbf{P}_{m, n}$ is a direct product of zero-one simplices [6]. Our progress is that we proved a even strong result in Theorem 3.5 with an intuitive graphical interpretation of each simplex in the direct product.

# 7. Proofs in Section 4. 

7.1. Proof of Theorem 4.3. Proof. We are going to prove the equality by induction on $n$. Since $n \geq 2$, we start the induction from $n=2$.

- $n=2$. It is obvious since there are only two vertices in $\mathbf{P}_{[n]}$ : (1) and (0). So $\mathbf{P}_{[n]}$ is a line segment which is a simplex of dimension 1 , i.e. $\mathbf{P}_{[n]}=\Delta_{1}$.
- Fix $q \in \mathbb{Z}_{+}$. Suppose the equality holds for $\mathbf{P}_{[n]}, \forall n<q$, and we need to prove that it also holds for $\mathbf{P}_{[q]}$. Define notation $N_{[k]}=\left\{a_{[1]}, \ldots, a_{[k]}\right\}$ for $k=1, \ldots, q$.
First, we want to prove: $\mathbf{P}_{[q]} \subseteq \mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1}$.
$\forall G \in \mathcal{G}_{[q]}$, we can define graphs:
- $G^{\prime}$ is the induced subgraph of $G$ for $N_{[q-1]}$, which implies $c_{G^{\prime}} \in \mathbf{P}_{[q-1]}$;
- $G^{\prime \prime}$ is a graph over $N$ such that the only edges in $G^{\prime \prime}$ are $a_{[i]} \rightarrow a_{[q]}$, where $a_{[i]} \in p a_{G}\left(a_{[q]}\right)$. Consider a diagnosis model where $N_{[q-1]}$ is the set of diseases and $a_{[q]}$ is the symptom, then we can see that $c_{G^{\prime \prime}} \in$ $\mathbf{P}_{q-1,1}=\Delta_{2^{q-1}-1}$.
Now, with a proper permutation of coordinates (see Remark 4.2), we can write $c_{G}$ in the form of:

$$
c_{G}=\left(c_{G^{\prime}} \quad c_{G^{\prime \prime}}\right)
$$

Since $\operatorname{vert}\left(\mathbf{P}_{[q]}\right)=\left\{c_{G}: G \in \mathcal{G}_{[q]}\right\}, \forall x \in \mathbf{P}_{[q]}$, with the same permutation of

coordinates, we have:

$$
x=\sum_{G \in \mathcal{G}_{[q]}} \alpha_{G} c_{G}=\left(\sum_{G \in \mathcal{G}_{[q]}} \alpha_{G} c_{G^{\prime}}, \sum_{G \in \mathcal{G}_{[q]}} \alpha_{G} c_{G^{\prime \prime}}\right)
$$

where $0 \leq \alpha_{G} \leq 1, \forall G \in \mathcal{G}_{[q]}$ and $\sum_{G \in \mathcal{G}_{[q]}} \alpha_{G}=1$.
Notice that $\sum_{G \in \mathcal{G}_{[q]}} \alpha_{G} c_{G^{\prime}} \in \mathbf{P}_{[q-1]}$ and $\sum_{G \in \mathcal{G}_{[q]}} \alpha_{G} c_{G^{\prime \prime}} \in \Delta_{2^{q-1}-1}$, Equation (7.1) implies $x \in \mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1}$. Hence:

$$
\mathbf{P}_{[q]} \subseteq \mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1}
$$

Second, we want to prove: $\mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1} \subseteq \mathbf{P}_{[q]}$.
Let $\mathcal{G}_{[q-1]}$ has nodes $N_{[q-1]}$, and $\mathcal{G}_{q-1,1}$ has diseases $N_{[q-1]}$ and symptom $a_{[q]}$. $\forall G^{\prime} \in \mathcal{G}_{[q-1]}$ and $G^{\prime \prime} \in \mathcal{G}_{q-1,1}$, we can define $G \in \mathcal{G}_{[q]}$ by extending $G^{\prime}$ as following: add a node $a_{[q]}$ and edges $\left(a_{[i]}, a_{[q]}\right), \forall a_{[i]} \in p a_{G^{\prime \prime}}\left(a_{[q]}\right)$, to $G^{\prime}$. We can write $c_{G}$ in the form of $c_{G}=\left(c_{G^{\prime}} \quad c_{G^{\prime \prime}}\right)$.
$\forall x \in \mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1}, x$ can be written as:

$$
\begin{aligned}
x & =\left(\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \beta_{G^{\prime}} c_{G^{\prime}}, \sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}} \gamma_{G^{\prime \prime}} c_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}} \beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\left(c_{G^{\prime}}, c_{G^{\prime \prime}}\right) \\
& =\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}}\left(\beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\right) c_{G}
\end{aligned}
$$

where $0 \leq \beta_{G^{\prime}}, \gamma_{G^{\prime \prime}} \leq 1, \forall G^{\prime} \in \mathcal{G}_{[q-1]}, \forall G^{\prime \prime} \in \mathcal{G}_{q-1,1}$, and $\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \beta_{G^{\prime}}=1$, $\sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}} \gamma_{G^{\prime \prime}}=1$
Notice that

$$
\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}}\left(\beta_{G^{\prime}} \gamma_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \beta_{G^{\prime}}\left(\sum_{G^{\prime \prime} \in \mathcal{G}_{q-1,1}} \gamma_{G^{\prime \prime}}\right)=\sum_{G^{\prime} \in \mathcal{G}_{[q-1]}} \beta_{G^{\prime}}=1
$$

This leads to $x \in \mathbf{P}_{[q]}$. Hence:

$$
\mathbf{P}_{[q-1]} \times \Delta_{2^{q-1}-1}=\mathbf{P}_{[q-1]} \times \mathbf{P}_{q, 1} \subseteq \mathbf{P}_{[q]}
$$

By induction on $n$, we finish the proof by:

$$
\begin{aligned}
\mathbf{P}_{[q]}=\mathbf{P}_{[q-1]} \times \mathbf{P}_{q-1,1} & =\left(\Delta_{2^{1}-1} \times \cdots \times \Delta_{2^{q-2}-1}\right) \times \Delta_{2^{q-1}-1}= \\
& \Delta_{2^{1}-1} \times \cdots \times \Delta_{2^{q-1}-1}
\end{aligned}
$$

7.2. Proof of Theorem 4.6. Proof. The proof from the view of graph theory will be very similar with the proof of Theorem 3.2, so we are going to give a proof from the view of polyhedral geometry, i.e. prove that: " $\exists$ vertices of $v^{1}, v^{2} \in \mathbf{P}_{[n]}$ such that $\mathbf{x}=\beta v^{1}+(1-\beta) v^{2}$ where $0 \leq \beta \leq 1$, and $v^{1}, v^{2}$ form an edge in $\mathbf{P}_{[n]}$ if and only if " $\mathbf{x}$ can be written in the form of $\mathbf{x}=\left(v_{1}, \ldots, v_{i-1}, e_{i}, v_{i+1}, \ldots, v_{n-1}\right)$, $i \in\{1, \ldots, n-1\}$ ".

We will prove "if" and "only if" separately.
(1) Prove "if" part.

Suppose $\mathbf{x}$ has the form $\mathbf{x}=\left(v_{1}, \ldots, v_{i-1}, e_{i}, v_{i+1}, \ldots, v_{n-1}\right)$.
Since $e_{i}$ belongs to an edge on $\Delta_{2^{i}-1}$, we can find two vertices $v_{i}^{1}, v_{i}^{2} \in \Delta_{2^{i}-1}$ which form this edge, and this implies $e_{i}=\beta v_{i}^{1}+\left(1-\beta v_{i}^{2}\right), 0 \leq \beta \leq 1$. Suppose the cost vector for this edge is $w_{i}^{e}$, then for any $v_{i}^{3} \in \operatorname{vert}\left(\Delta_{2^{i}-1}\right)$, $w_{i}^{e} v_{i}^{3} \leq w_{i}^{e} v_{i}^{1}=w_{i}^{e} v_{i}^{2}$, where " $=$ " holds if and only if $v_{i}^{3}=v_{i}^{1}$ or $v_{i}^{3}=v_{i}^{2}$.

We can also find $w_{j}^{v}$ which is a cost vector for vertex $v_{j}$ in $\Delta_{2^{j}-1}, j \in$ $\{1, \ldots, n-1\} \backslash\{i\}$. Still, we have: $\forall v_{j}^{3} \in \operatorname{vert}\left(\Delta_{2^{j}-1}\right), w_{j}^{v} v_{j}^{3} \leq w_{j}^{v} v_{j}$, where " $=$ " holds if and only if $v_{j}^{3}=v_{j}$.
Now let $v^{1}=\left(v_{1}, \ldots, v_{i-1}, v_{i}^{1}, v_{i+1}, \ldots, v_{n-1}\right), v^{2}=\left(v_{1}, \ldots, v_{i-1}, v_{i}^{2}, v_{i+1}, \ldots, v_{n-1}\right)$ and $w=\left(w_{1}^{v}, \ldots, w_{i-1}^{v}, w_{i}^{e}, w_{i+1}^{v}, \ldots, w_{n-1}^{v}\right)$. Obviously $\mathbf{x}=\beta v^{1}+(1-\beta) v^{2}$, where $0 \leq \beta \leq 1$. In addition, $\forall v^{3}=\left(v_{1}^{3}, \ldots, v_{n-1}^{3}\right) \in \operatorname{vert}\left(\mathbf{P}_{[n]}\right)$, we have:

$$
\begin{aligned}
w v^{3}=w_{i}^{e} v_{i}^{3}+\sum_{j=1, j \neq i}^{n-1} w_{j}^{v} v_{j}^{3} & \leq w_{i}^{v} v_{i}^{1}+\sum_{j=1, j \neq i}^{n-1} w_{j}^{v} v_{j}=w v^{1} \\
& =w_{i}^{e} v_{i}^{2}+\sum_{j=1, j \neq i}^{n-1} w_{j}^{v} v_{j}=w v^{2}
\end{aligned}
$$

where " $=$ " holds if and only if $v^{3}=v^{1}$ or $v^{3}=v^{2}$, i.e. $v^{1}$ and $v^{2}$ form an edge on $\mathbf{P}_{[n]}$.
(2) Prove "only if" part.

Suppose $\exists v^{1}=\left(v_{1}^{1}, \ldots v_{n-1}^{1}\right), v^{2}=\left(v_{1}^{2}, \ldots v_{n-1}^{2}\right) \in \operatorname{vert}\left(\mathbf{P}_{[n]}\right)$ such that $\mathbf{x}=\beta v^{1}+(1-\beta) v^{2}$ where $0 \leq \beta \leq 1$, and $v^{1}, v^{2}$ form an edge in $\mathbf{P}_{[n]}$. If we can prove that $\exists i \in\{1, \ldots, n-1\}$ such that $v_{i}^{1} \neq v_{i}^{2}$ and $v_{j}^{1}=v_{j}^{2}, \forall j \in$ $\{1, \ldots, n-1\} \backslash\{i\}$, then $\mathbf{x}$ has the form $\mathbf{x}=\left(v_{1}, \ldots, v_{i-1}, e_{i}, v_{i+1}, \ldots, v_{n-1}\right)$, where $e_{i}$ is on the edge of $\Delta_{2^{i}-1}$ formed by $v_{i}^{1}$ and $v_{i}^{2}$. We are going to prove this statement by contradiction.
Suppose $\exists i, j \in\{1, \ldots, n-1\}$ distinct such that $v_{i}^{1} \neq v_{i}^{2}$ and $v_{j}^{1} \neq v_{j}^{2}$, but $v^{1}$ and $v^{2}$ still form an edge on $\mathbf{P}_{[n]}$. Let $w=\left(w_{1}, \ldots, w_{n-1}\right)$ be the cost vector for this edge, i.e. $\forall v^{3}=\left(v_{1}^{3}, \ldots v_{n-1}^{3}\right) \in \operatorname{vert}\left(\mathbf{P}_{[n]}\right), w v^{3} \leq w v^{1}=w v^{2}$ where " $=$ " holds if and only if $v^{3}=v^{1}$ or $v^{3}=v^{2}$.

- If we set $v^{3}$ as following: $v_{i}^{3}=v_{i}^{2}, v_{k}^{3}=v_{k}^{1}, \forall k \in\{1, \ldots, n-1\} \backslash\{i\}$. Obviously $v^{3} \neq v^{1}$ and $v^{3} \neq v^{2}$. Thus:

$$
\begin{aligned}
w v^{3}=w_{i} v_{i}^{2}+\sum_{\substack{k=1, k \neq i}}^{n-1} w_{k} v_{k}^{1} & <w v^{1}=\sum_{k=1}^{n-1} w_{k} v_{k}^{1}=w_{i} v_{i}^{1}+\sum_{k=1, k \neq i}^{n-1} w_{k} v_{k}^{1} \\
\Longrightarrow w_{i} v_{i}^{2} & <w_{i} v_{i}^{1}
\end{aligned}
$$

- If we set $v^{3}$ as following: $v_{j}^{3}=v_{j}^{2}, v_{k}^{3}=v_{k}^{1}, \forall k \in\{1, \ldots, n-1\} \backslash\{j\}$. Obviously $v^{3} \neq v^{1}$ and $v^{3} \neq v^{2}$. Thus:

$$
w v^{3}=w_{j} v_{j}^{2}+\sum_{\substack{k=1, k \neq j}}^{n-1} w_{k} v_{k}^{1} \quad<w v^{1}=\sum_{k=1}^{n-1} w_{k} v_{k}^{1}=w_{j} v_{j}^{1}+\sum_{k=1, k \neq j}^{n-1} w_{k} v_{k}^{1}
$$

Now we set $v^{3}$ as following: $v_{i}^{3}=v_{i}^{1}, v_{j}^{3}=v_{j}^{1}, v_{k}^{3}=v_{k}^{2}, \forall k \in\{1, \ldots, n-$ $1\} \backslash\{i, j\}$. Then we have:
$w v^{3}=w_{i} v_{i}^{1}+w_{j} v_{j}^{1}+\sum_{k=1, k \neq i, j}^{n-1} w_{k} v_{k}^{2}>w_{i} v_{i}^{2}+w_{j} v_{j}^{2}+\sum_{k=1, k \neq i, j}^{n-1} w_{k} v_{k}^{2}=\sum_{k=1}^{n-1} w_{k} v_{k}^{2}=w v^{2}$,
i.e. $w v^{3}>w v^{2}$, which is a contradiction with our assumption.

# 8. Discussion.

8.1. Connection to K2 algorithm. If we consider a criterion $\mathcal{Q}$ which is a regular criterion, then it was proved that $\mathcal{Q}$ can be written as $\mathcal{Q}(G, D)=s(D)-$ $\left\langle r_{D}, c_{G}\right\rangle$, where the entropy $s(D)$ and the data vector $r_{D}$ only depends on the data $D$ and $c_{G}$ is the characteristic imset of $G[12,8]$. Once the cim-polytope can be written as a direct product of a sequences of simplices, we are able to find the optimal BN structure by maximizing a target function in each simplex: given data $D \in$ $D A T A(N, d)$,

$$
\max _{G \in \mathcal{G}_{[n], \Omega}} \mathcal{Q}(G, D) \Longrightarrow \min _{\mathbf{x} \in \mathbf{P}_{\mathcal{G}_{[n], \Omega}, c}} r_{D}^{T} \mathbf{x}=\sum_{i=2}^{n} \min _{\mathbf{x}_{\mathbf{i}} \in \Delta_{2}\left|\Omega_{i}\right|_{-1}} r_{D, i}^{T} \mathbf{x}_{\mathbf{i}}
$$

where $\mathbf{x}_{\mathbf{i}}$ contains the coordinates $\left\{T \subseteq \Omega_{i} \cup\left\{a_{[i]}\right\}:|T| \geq 2, a_{[i]} \in T, a_{[j]} \notin T, \forall j>i\right\}$ in $\mathbf{x}$, and the coordinates of $r_{D, i}^{T}$ matches the coordinates of $\mathbf{x}_{\mathbf{i}}$. This implies that we can find the optimal parent sets of $a_{[i]}, i=2, \ldots, n$, sequentially until we obtain the whole BN structure, which will be exactly the optimal BN structure in $\mathcal{G}_{[n], \Omega}$.

Equation (8.1) gives a polyhedral geometric insight of the K2 algorithm [3], which is a well-known heuristic method in learning Bayesian networks. Recall that in K2 algorithm, an ordering on the nodes is also fixed and parent sets of $a_{[i]}, i=2, \ldots, n$, are also determined sequentially. However, in order to find the optimal BN, Equation (8.1) claims that we need to find $G_{i} \in \mathcal{G}_{\left|\Omega_{i}\right|, 1}$ such that $r_{D, i}^{T} c_{G_{i}}=\min _{\mathbf{x}_{\mathbf{i}} \in \Delta_{2}\left|\Omega_{i}\right|_{-1}} r_{D, i}^{T} \mathbf{x}_{\mathbf{i}}$, while the K2 algorithm obtain each parent set $p a_{G}\left(a_{[i]}\right)$ by adding nodes to $\emptyset$ stepwisely (or removing nodes from $\left\{a_{[1]}, \ldots, a_{[i-1]}\right\}$ stepwisely), which cannot guarantee that the resulting parent sets are optimal (see Example 8.1 for a counter-example).

Example 8.1. Consider $\mathcal{G}_{3,1}$. The characteristic imsets of all possible graphs in $\mathcal{G}_{3,1}$ is listed as a matrix:

We are going to give counter-examples that the resulting $B N$ of the K2 algorithm is not the optimal solution.

- Forward selection, i.e. each parent set $p a_{G}\left({ }_{[i]}\right)$ is obtained by adding nodes to $\emptyset$ stepwisely. Suppose $r_{D}^{T}=(-1,-2,-1,-3,-10,-4,20)$ which satisfies $r_{D}^{T} c_{G_{13}}=-12<r_{D}^{T} c_{G}, \forall G \in \mathcal{G}_{3,1}, G \neq G_{13}$, i.e. the optimal graph is $G_{13}$. In K2 algorithm, we start from $p a_{G}\left(b_{1}\right)=\emptyset$. Next, $a_{2}$ is added to $p a_{G}\left(b_{1}\right)$ because $r_{D}^{T} c_{G_{2}}=-2<r_{D}^{T} c_{G_{1}}=r_{D}^{T} c_{G_{3}}=-1$. Then $a_{3}$ is added to $p a_{G}\left(b_{1}\right)$ because $r_{D}^{T} c_{G_{23}}=-7<r_{D}^{T} c_{G_{13}}=-6$. Procedure ends here because $r_{D}^{T} c_{G_{23}}=-7<r_{D}^{T} c_{G_{123}}=-1$. The graph chosen by K2 algorithm, $G_{23}$, is not the optimal graph.
- Backward selection, i.e. each parent set $p a_{G}\left(a_{[i]}\right)$ is obtained by removing nodes from $\left\{a_{[1]}, \ldots, a_{[i-1]}\right\}$ stepwisely. Suppose $r_{D}^{T}=(-3,-1,-1,3,3,0,10)$ which satisfies $r_{D}^{T} c_{G_{1}}=-3<r_{D}^{T} c_{G}, \forall G \in \mathcal{G}_{3,1}, G \neq G_{1}$, i.e. the optimal graph is $G_{1}$. In K2 algorithm, we start from $p a_{G}\left(b_{1}\right)=\left\{a_{1}, a_{2}, a_{3}\right\}$. Next, $a_{1}$ is removed from $p a_{G}\left(b_{1}\right)$ because $r_{D}^{T} c_{G_{23}}=-2<r_{D}^{T} c_{G_{12}}=r_{D}^{T} c_{G_{13}}=-1$. Procedure ends here because $r_{D}^{T} c_{G_{23}}=-2<r_{D}^{T} c_{G_{2}}=r_{D}^{T} c_{G_{3}}=-1$. The graph chosen by K2 algorithm, $G_{23}$, is not the optimal graph.

8.2. Open problems. Further work and open problems are still left in this topic. As we mentioned before, the main purpose of studying the structure of cimpolytopes is reducing the time complexity of learning Bayesian networks by suggesting polyhedral geometry techniques. But the reality is that even we have simplified our problem of learning BNs to LP problems over each simplex (see Equation (8.1)) in the direct produce showed in Theorem 4.3 and Equation (4.1), and have described all edges and facets of these simplices (see Section 3), if the number of nodes is large, the procedure of searching the optimal solutions in each simplex may still be very timeconsuming. In this sense, simulations and analysis on real datasets are necessary to compare the solution and time complexity of our method with other existing classifiers [16]. On the other hand, we also need to study on the misspecification (i.e. the underlying ordering of nodes is misspecified) and data sensitivity problems of our method via simulations.

Another way to reduce the time complexity is considering setting up a maximum number of parents to control the model complexity, especially when the number of nodes is too large. In this case, since the underlying ordering is fixed, the cim-polytope is still a direct product of simplices. Thus all edges of the cim-polytope can be found similarly with Theorem 4.6, but the expression of facets for each simplex is not clear.

Notice that all conclusion and discussion in this paper until now are all based on a fixed underlying ordering of nodes. However, in practice, it is often hard to decide such an ordering. One way to compromise is that we can fix the ordering of some of the nodes, and consider every permutation of the rest nodes. For instance, when we use SNP data to examine phenotypes, we are more interested in how genes affect phenotypes and how phenotypes affect each other. Thus we can consider DAGs where all edges between SNPs and edges from phenotypes to SNPs are forbidden, i.e. we only need to consider the permutation of phenotypes.

This paper focuses on the case that all random variables in $N$ are finite random variables. It is still an open problem that how to generalize our method to the case that some or all of the random variables in $N$ are continuous random variables.

Acknowledgment. The authors would like to thank Drs. R. Hemmecke, M. Studený, and B. Sturmfels for their useful advise.
