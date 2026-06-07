# Semidefinite tests for latent causal structures 

Aditya Kela, ${ }^{1}$ Kai von Prillwitz, ${ }^{2}$ Johan Åberg, ${ }^{1, *}$ Rafael Chaves, ${ }^{3}$ and David Gross ${ }^{1,4}$<br>${ }^{1}$ Institute for Theoretical Physics, University of Cologne, 50937 Cologne, Germany<br>${ }^{2}$ Institute for Chemistry and Biology of the Marine Environment, University of Oldenburg, 26111 Oldenburg, Germany<br>${ }^{3}$ International Institute of Physics, Federal University of Rio Grande do Norte, 59070-405 Natal, Brazil<br>${ }^{4}$ Centre for Engineered Quantum Systems, School of Physics, The University of Sydney, Sydney, NSW 2006, Australia<br>(Dated: January 4, 2017)


#### Abstract

Testing whether a probability distribution is compatible with a given Bayesian network is a fundamental task in the field of causal inference, where Bayesian networks model causal relations. Here we consider the class of causal structures where all correlations between observed quantities are solely due to the influence from latent variables. We show that each model of this type imposes a certain signature on the observable covariance matrix in terms of a particular decomposition into positive semidefinite components. This signature, and thus the underlying hypothetical latent structure, can be tested in a computationally efficient manner via semidefinite programming. This stands in stark contrast with the algebraic geometric tools required if the full observable probability distribution is taken into account. The semidefinite test is compared with tests based on entropic inequalities.


## I. INTRODUCTION

In spite of the primal importance of discovering causal relations in science, the statistical analysis of empirical data has historically shied away from causality. Only releatively recently has a rigorous theory of causality emerged (see, for instance, [1, 2]), showing that empirical data indeed can contain information about causation rather than mere correlation. Since then, causal inference has quickly become influential. Examples range from applications to the inference of genetic [3] and social networks [4], to a better understanding of the role of causality within quantum physics $[5-13]$.
To formalize causal mechanisms it has become popular to use directed acyclic graphs (DAGs) where nodes denote random variables and directed edges (arrows) account for their causal relations. Central problems within this context include inference or model selection: 'Given samples from a number of observable variables, which DAG should we associate with them?', as well as hypothesis testing: 'Can the observed data be explained in terms of an assumed DAG?' Here, we concentrate on the latter problem and propose a novel solution based on the covariances that a given causal structure gives rise to. To understand the relevance and applicability of this method it is useful to summarize the difficulties that we typically face when approaching such problems.
The most common method to infer the set of possible DAGs compatible with empirical observations is based on the Markov condition and the faithfulness assumption [1, 2]. Under these conditions, and in the case where all variables composing a given DAG can be assumed to be empirically accessible, the conditional statistical independencies implied by the graph contain all the information required to test for the compatibility of some data with the causal structure. However, for a variety of practical and fundamental reasons, we do quite generally face causal discovery in the presence of latent (hidden) variables, that is, variables that may play an important role in the causal model, but nonetheless cannot be accessed empirically. In this case we have to characterize the set of marginal probability distributions that a given DAG can give rise to. Unfortunately, as is widely recognized, generic causal models with latent variables impose highly non-trivial constraints on the possible correlations compatible with it [14-25]. Although the marginal compatibility in principle can be completely characterized in terms of semi-algebraic sets [16], it appears that the resulting tests in practice are computationally intractable beyond a few variables $[18,22]$.
One possible approach to deal with the apparent intractability is to consider relaxations of the original problem, that is, to design tests that define incomplete lists of constraints (outer approximations) to the set of compatible distributions [17-20, 26-28]. For instance, this approach has previously been considered in [27-30], with tests

[^0]
[^0]:    * johan.aberg@uni-koeln.de

based on entropic information theoretic inequalities; an idea originally conceived to tackle foundational questions in quantum mechanics [31-37]. Here we consider a relaxation in a similar spirit, but based on covariances rather than entropies.

Beyond dealing with potential computational intractabilities, an additional benefit with a relaxation based on covariances is that it at most involves bipartite marginals, and it seems reasonable to expect that this would be less data-intensive than methods based on the full multivariate distribution of the observables.
![img-0.jpeg](img-0.jpeg)

FIG. 1. Bipartite DAGs. In this investigation we focus on the class of causal models where all correlations among the observables are due to a collection of independent latent variables. This setting can be described in terms of DAGs that are bipartite, where the latter means that all edges are directed from latent variables $\left(L_{1}, L_{2}, L_{3}\right)$ to the observables $\left(O_{1}, O_{2}, O_{3}, O_{4}, O_{5}\right)$, and where there are no edges within each of these subsets.

# A. Main assumptions and results 

We focus on a particular class of latent causal structures, where we assume that there are no direct causal influences between the observables, but only from latent variables to observables (see figure 1). Hence, all correlations among the observables are due to the latent variables. This setting can be described by the class of DAGs where all edges are directed from latent vertices to observable vertices, but no edges within these two groups (see figure 1). In other words, we consider the case of DAGs that are bipartite, with the coloring 'observable' and 'latent'. Alternatively, this can be described in terms of hypergraphs, where each independent latent cause is associated with a hyperedge consisting of the affected observable vertices (see e.g. [38]).

This class of graphs has previously been considered in the context of marginalization of Bayesian networks [26, 29, 38]. They moreover provide examples of the difficulties that arise when characterizing latent structures [6, 27, 28, 39-41], where standard techniques based on the use of conditional independencies even can yield erroneous results (for a discussion, see e.g. [42]). This type of latent structures furthermore emerges in the context of Bell's theorem [43], as well as in recent generalizations [6, 23, 24, 39-41, 44, 45], where they can be used to show that quantum correlations between distant observers -thus without direct causal influences between them-are incompatible with our most basic notions of cause and effect.

Irrespective of the nature of the observables (categorical or continuous) we are free to assign vectors to each possible outcome of the observables. Our main result is to show that each bipartite DAG implies a particular decomposition of the resulting covariance matrix into positive semidefinite components. Hence, we can test whether the observed covariance matrix is compatible with a hypothetical bipartite DAG by checking whether it satisfies the corresponding positive semidefinite decomposition, and we will in the following somewhat colloquially refer to this as the 'semidefinite test'. The semidefinite test can thus be phrased as a semidefinite membership problem, which in turn can be solved via semidefinite programming. The latter is known to be computationally efficient from a theoretical point of view, and has a good track record concerning algorithms that are efficient also in practice (see discussions in [46]).

## B. Structure of the paper

In section II we derive a general decomposition of covariance matrices, which forms the basis of our semidefinite test. In section III we rephrase this general result to fit with the particular structure of observables and latent

variables that we employ, and in section IV we derive the main result, namely that every bipartite DAG implies a particular semidefinite decomposition of the observable covariance matrix. Section V focuses on the converse, namely that every covariance matrix that satisfies the decomposition of a given bipartite DAG can be realized by a corresponding causal model. Section VI relates the semidefinite decomposition to previous types of operator inequalities introduced in [47]. To obtain a covariance matrix we may be required to assign vectors to the outcomes of the random variables, and section VII discusses the dependence of the semidefinite test on this assignment. In section VIII we briefly discuss the fact that the compatibility with a given bipartite DAG is not affected if the observables are processed locally, and that the semidefinite test respects this basic property under suitable conditions. Section IX considers a specific class of distributions where it is possible to analytically determine the conditions for a semidefinite decomposition. This class of distribution does in section $X$ serve as a testbed for comparisons with the above mentioned entropic tests. We conclude with a summary and outlook in section XI.

# II. SEMIDEFINITE DECOMPOSITION OF COVARIANCE MATRICES 

In this section we develop the basic structure that forms the core of the semidefinite test. In essence it is obtained via a repeated application of a law of total variance for covariance matrices.

For a vector-valued random variable $Y$, in a real or complex inner product space $\mathcal{V}$, we define the covariance matrix of $Y$ as

$$
\operatorname{Cov}(Y):=E\left((Y-E(Y))(Y-E(Y))^{\dagger}\right)=E\left(Y Y^{\dagger}\right)-E(Y) E(Y)^{\dagger}
$$

where $E(Y)$ denotes the expectation of $Y$ and $\dagger$ denotes the transposition if the underlying vector space is real, and the Hermitian conjugation if the space is complex. One should note that $E(Y)^{\dagger}=E\left(Y^{\dagger}\right)$. We also define the cross-correlation for a pair of vector-valued variables $Y^{\prime}, Y$ (not necessarily belonging to the same vector space)

$$
\operatorname{Cov}\left(Y^{\prime}, Y\right):=E\left(Y^{\prime} Y^{\dagger}\right)-E\left(Y^{\prime}\right) E(Y)^{\dagger}
$$

where $\operatorname{Cov}(Y, Y)=\operatorname{Cov}(Y)$. For a pair of random variables $X, Y$ we denote the expectation of $Y$ conditioned on $X$ as $E(Y \mid X)$. Via the conditional expectation we can also define the conditional covariance matrix

$$
\operatorname{Cov}(Y \mid X):=E\left((Y-E(Y \mid X))(Y-E(Y \mid X))^{\dagger} \mid X\right)=E\left(Y Y^{\dagger} \mid X\right)-E(Y \mid X) E(Y \mid X)^{\dagger}
$$

In a similar manner we can also obtain a conditional cross-correlation between two random vectors $Y^{\prime}, Y$

$$
\operatorname{Cov}\left(Y^{\prime}, Y \mid X\right):=E\left(\left(Y^{\prime}-E\left(Y^{\prime} \mid X\right)\right)(Y-E(Y \mid X))^{\dagger} \mid X\right)=E\left(Y^{\prime} Y^{\dagger} \mid X\right)-E\left(Y^{\prime} \mid X\right) E(Y \mid X)^{\dagger}
$$

The starting point for our derivations is the law of total expectation

$$
E(Y)=E(E(Y \mid X))
$$

where the 'outer' expectation corresponds to the averaging over the random variable $E(Y \mid X)$. The law of total expectation can be iterated, such that for three random variables $Y, X, Z$, we have a law of total conditional expectation

$$
E(Y \mid Z)=E(E(Y \mid X, Z) \mid Z)
$$

and thus $E(Y)=E(E(Y \mid Z))=E(E(E(Y \mid X, Z) \mid Z))$.
From the law of total expectation (5) one can obtain a covariance-matrix version of the law of total variance

$$
\operatorname{Cov}(Y)=\operatorname{Cov}(E(Y \mid Z))+E(\operatorname{Cov}(Y \mid Z))
$$

which can be confirmed by expanding the two sides of the above equality and applying (5).
For three random variables $Y, W, Z$ a conditional version of the law of total covariance reads

$$
\operatorname{Cov}(Y \mid Z)=\operatorname{Cov}(E(Y \mid W, Z) \mid Z)+E(\operatorname{Cov}(Y \mid W, Z) \mid Z)
$$

which can be obtained by expanding the right hand side and applying the law of total conditional expectation (6).
The following lemma is obtained via an iterated application of the law of total covariance (7) and the law of total conditional covariance (8). One may note the similarities with the chain-rule for entropies (see e.g. chapter 2 in [48]).

Lemma 1. Let $Y$ be a vector-valued random variable on a finite-dimensional real or complex inner product space $\mathcal{V}$, let $X_{1}, \ldots, X_{N}$ be random variables over the same probability space. Assuming that the underlying measure is such that all involved conditional expectations and covariances are well defined, then

$$
\operatorname{Cov}(Y)=R+\sum_{n=1}^{N} C_{n}
$$

where $R$ and $C_{1}, \ldots, C_{N}$ are positive semidefinite operators on the space $\mathcal{V}$, defined by

$$
\begin{aligned}
C_{1} & :=\operatorname{Cov}\left(E\left(Y \mid X_{1}\right)\right) \\
C_{n} & :=E\left(\operatorname{Cov}\left(E\left(Y \mid X_{1}, \ldots, X_{n}\right) \mid X_{1}, \ldots, X_{n-1}\right)\right), \quad n=2, \ldots, N \\
R & :=E\left(\operatorname{Cov}\left(Y \mid X_{1}, \ldots, X_{N}\right)\right)
\end{aligned}
$$

One may note that the above decomposition is not necessarily unique; we could potentially obtain a new decomposition if the variables in the sequence $X_{1}, \ldots, X_{N}$ are permuted.

Proof. The law of total covariance (7) for $Z=X_{1}$, combined with the law of total conditional covariance (8) for $Z:=X_{1}, W:=X_{2}$ yields

$$
\operatorname{Cov}(Y)=\operatorname{Cov}\left(E\left(Y \mid X_{1}\right)\right)+E\left(\operatorname{Cov}\left(E\left(Y \mid X_{2}, X_{1}\right) \mid X_{1}\right)\right)+E\left(\operatorname{Cov}\left(Y \mid X_{2}, X_{1}\right)\right)
$$

Suppose that for some $j \geq 2$ it would be true that

$$
\begin{aligned}
\operatorname{Cov}(Y)= & \operatorname{Cov}\left(E\left(Y \mid X_{1}\right)\right) \\
& +\sum_{n=2}^{j} E\left(\operatorname{Cov}\left(E\left(Y \mid X_{1}, \ldots, X_{n}\right) \mid X_{1}, \ldots, X_{n-1}\right)\right) \\
& +E\left(\operatorname{Cov}\left(Y \mid X_{1}, \ldots, X_{j}\right)\right)
\end{aligned}
$$

The law of total conditional covariance (8), with $W:=X_{j+1}$ and $Z:=X_{1}, \ldots, X_{j}$, gives

$$
\operatorname{Cov}\left(Y \mid X_{1}, \ldots, X_{j}\right)=\operatorname{Cov}\left(E\left(Y \mid X_{1}, \ldots, X_{j}, X_{j+1}\right) \mid X_{1}, \ldots, X_{j}\right)+E\left(\operatorname{Cov}\left(Y \mid X_{1}, \ldots, X_{j}, X_{j+1}\right) \mid X_{1}, \ldots, X_{j}\right)
$$

By inserting this expression into the last line of (12) one does again obtain (12) but with $j$ substituted for $j+1$. By (11) we can see that (12) is true for $j=2$. Thus, by induction to $j=N$, and the identifications in (10), we obtain (9).

Note that $\operatorname{Cov}\left(E\left(Y \mid X_{1}, \ldots, X_{n-1}, X_{n}\right) \mid X_{1}=x_{1}, \ldots, X_{n-1}=x_{n-1}\right)$ is a positive semidefinite operator on $\mathcal{V}$ for each value of $x_{1}, \ldots, x_{n-1}$. Hence, by averaging over these variables, and thus implementing the expectation that yields $C_{n}$, we do still have a positive semidefinite operator on $\mathcal{V}$. The same observation applies to $R=$ $E\left(\operatorname{Cov}\left(Y \mid X_{1}, \ldots, X_{N}\right)\right)$.

# III. OBSERVABLE VS. LATENT VARIABLES, AND FEATURE MAPS 

Here we consider the decomposition developed in the previous section for the more specific setting of observable and latent variables.

We consider a collection of observable variables $O_{1}, \ldots, O_{M}$. To each of these variables $O_{m}$ we associate a mapping $Y^{(m)}$, in some contexts referred to as a 'feature map' [49], into a finite-dimensional vector space $\mathcal{V}_{m}$. We denote the resulting vector-valued random variables by $Y_{m}:=Y^{(m)}\left(O_{m}\right)$, and for the sake of simplicity we will in the following tend to abuse the terminology and refer to the vectors $Y_{m}$ themselves as feature maps. We also define the joint random vector $Y:=\sum_{m=1}^{M} Y_{m}$ on $\mathcal{V}:=\bigoplus_{m=1}^{M} \mathcal{V}_{m}$. (Hence, we can view $Y$ as the concatenation of the vectors $Y_{m}$.) One should note that while we regard the observable variables $O_{m}$ as being part of the setup that is 'given', the feature maps $Y^{(m)}$ are part of the analysis, and we are free to assign these as we see fit. (Concerning the question of how the test depends on this choice, see section VII.)

Let $P_{m}$ denote the projector onto the subspace $\mathcal{V}_{m}$ in $\mathcal{V}$. We divide the total covariance matrix $\operatorname{Cov}(Y)$ into the cross-correlations between the separate observable quantities $\operatorname{Cov}(Y)=\left[\operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}}\right)\right]_{m, m^{\prime}=1}^{M}$. One can note that $\operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}}\right)=P_{m} \operatorname{Cov}(Y) P_{m^{\prime}}$.

![img-1.jpeg](img-1.jpeg)

FIG. 2. Observables, latent variables, and feature maps. The model consists of a collection of observable variables $O_{1}, \ldots, O_{M}$ and a collection of latent variables $L_{1}, \ldots, L_{N}$. Via feature maps, each $O_{m}$ is mapped to a vector $Y_{m}$ in a vector space $\mathcal{V}_{m}$. On the vector space $\mathcal{V}=\oplus_{m=1}^{M} \mathcal{V}_{m}$ we define the joint random vector $Y:=Y_{1}+\cdots+Y_{M}$.

For a collection of latent variables $L_{1}, \ldots, L_{N}$, we make the identifications $X_{j}:=L_{j}$ in Lemma 1. Similarly as for the covariance matrix we decompose the operators $C_{n}$ and $R$ into 'block-matrices' $C_{n}=\left[C_{n}^{m, m^{\prime}}\right]_{m, m^{\prime}=1}^{M}$ and $R=\left[R^{m, m^{\prime}}\right]_{m, m^{\prime}=1}^{M}$, with $C_{n}^{m, m^{\prime}}:=P_{m} C_{n} P_{m^{\prime}}$ and $R^{m, m^{\prime}}:=P_{m} R P_{m^{\prime}}$, where we can write

$$
\begin{aligned}
C_{1}^{m, m^{\prime}} & =\operatorname{Cov}\left(E\left(Y_{m} \mid L_{1}\right), E\left(Y_{m^{\prime}} \mid L_{1}\right)\right) \\
C_{n}^{m, m^{\prime}} & =E\left(\operatorname{Cov}\left(E\left(Y_{m} \mid L_{1}, \ldots, L_{n}\right), E\left(Y_{m^{\prime}} \mid L_{1}, \ldots, L_{n}\right) \mid L_{1}, \ldots, L_{n-1}\right)\right) \\
R^{m, m^{\prime}} & =E\left(\operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}} \mid L_{1}, \ldots, L_{N}\right)\right)
\end{aligned}
$$

for $2 \leq n \leq N$. In terms of these blocks we can thus reformulate (9) as

$$
\operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}}\right)=R^{m, m^{\prime}}+\sum_{n=1}^{N} C_{n}^{m, m^{\prime}}
$$

One should keep in mind that $C_{n}^{m, m^{\prime}}$ and $R^{m, m^{\prime}}$ in the general case are matrices (rather than scalar numbers) for each single pair $m, m^{\prime}$.

# IV. DECOMPOSITION OF THE COVARIANCE MATRIX FOR BIPARTITE DAGS 

We define a bipartite DAG as a finite DAG $G=(V, E)$ with vertices $V$ and edges $E$, with a bipartition $V=O \cup L$, $O \cap L=\varnothing$ such that all edges in $E$ are directed from the elements in $L$ (the latent variables) to the elements in $O$ (the observables). Since $G$ is finite, we enumerate the elements of $O$ as $O_{1}, \ldots, O_{M}$ and the elements of $L$ as $L_{1}, \ldots, L_{N}$. One may note that we generally will overload the notation and let $O_{m}$ and $L_{n}$ denote the vertices in the underlying bipartite DAG, as well as denoting the random variables associated with these vertices.

For a vertex $v$ in a directed graph $G$ we let $\operatorname{ch}(v)$ denote the children of $v$, i.e., the set of vertices $v^{\prime}$ for which there is an edge directed from $v$ to $v^{\prime}$. We let $\mathrm{pa}(v)$ denote the parents of $v$, i.e., the set of vertices $v^{\prime}$ for which there is an edge directed from $v^{\prime}$ to $v$. For bipartite DAGs an element in $L$ can only have children in $O$ (and have no parents), and an element in $O$ can only have parents in $L$ (and no children). As an example, for the bipartite DAG in figure 1 we have $\operatorname{ch}\left(L_{1}\right)=\left\{O_{1}, O_{2}, O_{3}\right\}, \operatorname{ch}\left(L_{2}\right)=\left\{O_{2}, O_{5}\right\}$, and $\operatorname{ch}\left(L_{3}\right)=\left\{O_{3}, O_{5}\right\}$, and $\operatorname{pa}\left(O_{1}\right)=\left\{L_{1}\right\}$, $\mathrm{pa}\left(\mathrm{O}_{2}\right)=\left\{L_{1}, L_{2}\right\}, \mathrm{pa}\left(\mathrm{O}_{3}\right)=\left\{L_{1}, L_{3}\right\}, \mathrm{pa}\left(\mathrm{O}_{4}\right)=\varnothing$, and $\mathrm{pa}\left(\mathrm{O}_{5}\right)=\left\{L_{2}, L_{3}\right\}$.

For a causal model defined by a general DAG $G=(V, E)$ the underlying probability distribution can be described via the Markov condition where each edge represents a direct causal influence, and thus each vertex $v$ can only be directly influenced by its parents $\mathrm{pa}(v)$, resulting in distributions of the form $P=\prod_{v \in V} P(v \mid \mathrm{pa}(v))$. Hence, for a bipartite DAG we get $P=\prod_{m} P\left(O_{m} \mid \mathrm{pa}\left(O_{m}\right)\right) \Pi_{n} P\left(L_{n}\right)$, and thus all the latent variables are independent, and the observables are independent when conditioned on the latent variables.

As in the previous section, we map the observables $O_{1}, \ldots, O_{M}$ to vectors $Y_{1}, \ldots, Y_{M}$ in vector spaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$. For each $n$ we define the projector $P^{(n)}$ in $\mathcal{V}$ by

$$
P^{(n)}:=\sum_{m \in \operatorname{ch}\left(L_{n}\right)} P_{m}
$$

Hence, $P^{(n)}$ is the projector onto all subspaces of $\mathcal{V}$ that are associated with the children $\operatorname{ch}\left(L_{n}\right)$ of the latent variable $L_{n}$. (In the above sum we should strictly speaking write $\sum_{m \in O_{m} \in \operatorname{ch}\left(L_{n}\right)}$. However, in order to avoid a too cumbersome notation we will from time to time take the liberty of writing $m \in \operatorname{ch}\left(L_{n}\right)$ rather than $O_{m} \in \operatorname{ch}\left(L_{n}\right)$, and $n \in \mathrm{pa}\left(O_{m}\right)$ rather than $L_{n} \in \mathrm{pa}\left(O_{m}\right)$.)
![img-2.jpeg](img-2.jpeg)

FIG. 3. Example: Triangular bipartite DAG. The covariance matrix resulting from the observables in a bipartite DAG is subject to a decomposition where each latent variable gives rise to a positive semidefinite component, and where the support of that component is determined by the children of the corresponding latent variable. In the case of the 'triangular' scenario of the the bipartite DAG to the left, each of the three latent variables has two children. The covariance matrix, schematically depicted to the right, can consequently be decomposed into three positive semidefinite components, each with bipartite supports. This observation yields a method (which we refer to as the 'semidefinite test') to falsify a given bipartite DAG as an explanation of an observed covariance matrix.

Proposition 1. For a bipartite DAG with latent variables $L_{1}, \ldots, L_{N}$ and observables $O_{1}, \ldots, O_{M}$ with assigned feature maps $Y_{1}, \ldots, Y_{M}$ into finite-dimensional real or complex inner-product spaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$, the covariance matrix of $Y=\sum_{m=1}^{M} Y_{m}$ satisfies

$$
\operatorname{Cov}(Y)=R+\sum_{n=1}^{N} C_{n}, \quad R \geq 0, \quad C_{n} \geq 0
$$

where

$$
P^{(n)} C_{n} P^{(n)}=C_{n}, \quad R=\sum_{m=1}^{M} P_{m} R P_{m}
$$

and where the projectors $P^{(n)}$ are as defined in (15) with respect to the given bipartite DAG, and where $P_{m}$ is the projector onto $\mathcal{V}_{m}$ in $\bigoplus_{m=1}^{M} \mathcal{V}_{m}$.

One may note that if the span of the supports of $\left\{P^{(n)}\right\}_{n=1}^{N}$ covers $\mathcal{V}$, then we can distribute the blocks $P_{m} R P_{m}$ of $R$ and add them to the different $C_{n}$ in such a way that the new operators still are positive semidefinite and satisfy the support structure of the original $C_{n} \mathrm{~s}$. The exception is if there is some observable that has no parent (as $O_{4}$ in figure 1).

Proof. Select an enumeration $L_{1}, \ldots, L_{N}$ of the latent variables. By Lemma 1 we know that the covariance matrix $\operatorname{Cov}(Y)$ can be decomposed as in (9) with the positive semidefinite operators $R$ and $C_{n}$ as defined in (10). In the following we will make use of the block-decomposition $C_{n}=\left[C_{n}^{m, m^{\prime}}\right]_{m, m^{\prime}=1}^{M}$ and $R=\left[R^{m, m^{\prime}}\right]_{m, m^{\prime}=1}^{M}$ with respect to the subspaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$ as in (13).

If $L_{n} \notin \mathrm{pa}\left(O_{m}\right)$ then it means that $Y_{m}$ is independent of $L_{n}$ and thus

$$
E\left(Y_{m} \mid L_{1}, \ldots, L_{n}\right)=E\left(Y_{m} \mid L_{1}, \ldots, L_{n-1}\right)
$$

The analogous statement is true if $L_{n} \notin \mathrm{pa}\left(O_{m^{\prime}}\right)$. By this it follows that

$$
\operatorname{Cov}\left(E\left(Y_{m} \mid L_{1}, \ldots, L_{n}\right), E\left(Y_{m^{\prime}} \mid L_{1}, \ldots, L_{n}\right) \mid L_{1}, \ldots, L_{n-1}\right)=0, \quad \text { if } \quad L_{n} \notin \mathrm{pa}\left(O_{m}\right) \cap \mathrm{pa}\left(O_{m^{\prime}}\right)
$$

Note that $L_{n} \in \mathrm{pa}\left(O_{m}\right) \cap \mathrm{pa}\left(O_{m^{\prime}}\right) \Leftrightarrow O_{m}, O_{m^{\prime}} \in \operatorname{ch}\left(L_{n}\right)$. By comparing (18) with (13) we can conclude that $C_{n}^{m, m^{\prime}}=0$ if $O_{m} \notin \operatorname{ch}\left(L_{n}\right)$ or $O_{m^{\prime}} \notin \operatorname{ch}\left(L_{n}\right)$. The definition of the projector $P^{(n)}$ in (15) thus yields $P^{(n)} C_{n} P^{(n)}=C_{n}$. Moreover, we know from Lemma 1 that $C_{n} \geq 0$.

By construction, all the observables $O_{1}, \ldots, O_{M}$ and thus also $Y_{1}, \ldots, Y_{M}$ are independent when conditioned on the latent variables. Hence,

$$
R^{m, m^{\prime}}=E\left(\operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}} \mid L_{1}, \ldots, L_{N}\right)\right)=\delta_{m, m^{\prime}} E\left(\operatorname{Cov}\left(Y_{m} \mid L_{1}, \ldots, L_{N}\right)\right)
$$

and thus $R=\sum_{m=1}^{M} P_{m} R P_{m}$.
One may note that although the operators $C_{n}$ potentially may change if we generated them via a permutation of the sequence of latent variables $L_{1}, \ldots, L_{N}$, the resulting projectors $P^{(n)}$ would not change. Hence, the supportstructure described by (16) and (17) is stable under rearrangements of the sequence.

Deciding whether a given matrix is of the form (16) can be done via semi-definite programming (SDP). We end this section by describing an explicit SDP formulation.

The optimization will be over matrices $Z$ which can be interpreted as the direct sum of candidates for $R$ and the $C_{n}$ 's. More precisely, let

$$
\begin{aligned}
\mathcal{Z} & :=\mathcal{V}_{1} \oplus \cdots \oplus \mathcal{V}_{M} \oplus \mathcal{W}_{1} \oplus \cdots \oplus \mathcal{W}_{N} \\
\mathcal{W}_{i} & :=\bigoplus_{m \in \operatorname{ch}\left(L_{p}\right)} \mathcal{V}_{m}
\end{aligned}
$$

Let $Z$ be a matrix on $\mathcal{Z}$. According to the direct sum decomposition (19), the matrix $Z$ is a block matrix with $(M+N) \times(M+N)$ blocks. We think of the fist $M$ diagonal blocks as carrying candidates for $R_{m}=P_{m} R P_{m}$ (which completely defines $R$, according to (17)); while the rear $N$ diagonal blocks correspond to candidate $C_{n}$ 's. Note that the $N$ rear sumands in (19) are dirct sums themselves. It therefore makes sense to use double indices to refer to spaces inside the $\mathcal{W}_{i}{ }^{\prime}$ s. Concretely, the SDP includes affine constraints on the blocks $Z^{(M+n, m),\left(M+n, m^{\prime}\right)}$. The first part of the indices selects the space $\mathcal{W}_{n}$ in (19). The second part refers to the space $\mathcal{V}_{m}$ within $\mathcal{W}_{n}$ according to (20). We use the convention that $Z^{(M+n, m),\left(M+n, m^{\prime}\right)}$ denotes 0 if either $\mathcal{V}_{m}$ or $\mathcal{V}_{m^{\prime}}$ does not occur in $\mathcal{W}_{n}$.

With these definitions, the semi-definite program that verifies whether a covariance matrix $\operatorname{Cov}(Y)$ is of the form (16) reads

$$
\begin{array}{ll}
\operatorname{maximize} & 0 \\
\text { subject to } & \delta_{m, m^{\prime}} \sum_{m=1}^{M} Z^{(m),(m)}+\sum_{n=1}^{N} Z^{(M+n, m),\left(M+n, m^{\prime}\right)}=\operatorname{Cov}(Y)^{m, m^{\prime}}, \quad\left(m, m^{\prime}=1, \ldots M\right) \\
& Z \geq 0
\end{array}
$$

where the optimization is over symmetric (hermitian) matrices $Z$ on $\mathcal{Z}$. Up to a trivial re-expression of the linear functions of $Z$ in terms of trace inner products with suitable matrices $F_{i}$, the optimization problem above is in the (dual) standard form of an SDP [46, Section 3].

The left-hand side of (22) impliclity defines a linear map $\mathcal{A}$ from matrices on $\mathcal{Z}$ to matrices on $\mathcal{V}$. Explicitly, $\mathcal{A}$ maps off-diagonal blocks to 0 and acts on block-diagonal matrices as

$$
\mathcal{A}: R_{1} \oplus \cdots \oplus R_{M} \oplus C_{1} \oplus \cdots \oplus C_{N} \mapsto \sum_{m} R_{m}+\sum_{n} C_{n}
$$

The constraints of the SDP can thus be written slightly more transparently as

$$
\begin{aligned}
& \mathcal{A}(Z)=\operatorname{Cov}(Y) \\
& Z \geq 0
\end{aligned}
$$

In this language, the dual of the above SDP is

$$
\begin{array}{ll}
\operatorname{minimize} & \operatorname{tr}(X \operatorname{Cov}(Y)) \\
\text { subject to } & \mathcal{A}^{\dagger}(X) \geq 0
\end{array}
$$

Let $X^{*}$ be the optimizer of (26). If $\operatorname{tr}\left(X^{*} \operatorname{Cov}(Y)\right)<0$, then the original SDP is infeasible and therefore, $\operatorname{Cov}(Y)$ is not of the form (16). Indeed, by construction, such an $X^{*}$ has a negative trace inner product with the covariance matrix, but a positive trace inner product

$$
\operatorname{tr}(\mathcal{A}(Z) X)=\operatorname{tr}\left(Z \mathcal{A}^{\dagger}(X)\right) \geq 0 \quad \forall Z \geq 0
$$

with all matrices $\mathcal{A}(Z), Z \geq 0$ that could potentially be feasible for the primal SDP (24). Thus, the dual SDP (26) can be used to find a witness or a dual certificate $X^{*}$ for the incompatibility of a covariance matrix with a presumed causal structure. The geometry of the involved objects is shown in figure 4. We will refer to this dual construction in section XI, where we sketch possibilities to base statistical hypothesis tests such witnesses.
![img-3.jpeg](img-3.jpeg)

FIG. 4. Dual Certificates. The set of covariance matrices compatible with a certain causal structure in the sense of proposition 1 forms a convex cone $\Gamma$. The cone is the feasible set of the SDP (21). If a given covariance matrix $\operatorname{Cov}(Y)$ is not an element of that cone, then there exists a hyperplane (depicted in red) seperating the two convex sets. A normal vector $X^{*}$ for the seperating hyperplane can be found using the dual SDP (26).

# V. REALIZING A GIVEN DECOMPOSITION 

In the previous section we have shown that the observable covariance matrix associated with a given bipartite DAG always satisfies a particular semidefinite decomposition implied by that DAG. Here we show the converse, in the sense that if we have a positive semidefinite operator that satisfies the decomposition obtained from a particular bipartite DAG, then there exists a causal model associated with that DAG that has the given operator as its observable covariance matrix (see figure 5). The proof is based on the observation that each positive semidefinite operator on a vector space can be interpreted as the covariance of a vector-valued random variable on that space (e.g. as the covariance of a multivariate normal distribution, or of variable over finite alphabets, as discussed in section VB). The essential idea is that we assign an independent random variable to each component in the decomposition, and take these as the latent variables, and that the support structure of the components furthermore determines the children of the latent variables.

## A. Realization of decompositions

Let $O$ be a finite set, and let $\left\{\Omega_{n}\right\}_{n=1}^{N}$ be a collection of subsets of $O$. The collection $\left\{\Omega_{n}\right\}_{n=1}^{N}$ defines a bipartite DAG with $O$ as observable nodes, and a set of latent nodes $L_{1}, \ldots, L_{N}$, with the edges assigned by the identification $\operatorname{ch}\left(L_{n}\right):=\Omega_{n}$ for $n=1, \ldots, N$. In the following we denote this bipartite DAG by $B\left(\left\{\Omega_{n}\right\}_{n=1}^{N}\right)$.

Proposition 2. Let $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$ be finite-dimensional real or complex inner-product spaces. For a number $N$ let $\left\{\Omega_{n}\right\}_{n=1}^{N}$ be a collection of subsets $\Omega_{n} \subset\{1, \ldots, M\}$. Suppose that $Q$ is a positive semidefinite operator on the space $\mathcal{V}=\mathcal{V}_{1} \oplus \cdots \oplus \mathcal{V}_{M}$,

![img-4.jpeg](img-4.jpeg)

FIG. 5. A positive semidefinite operator on a set of selected orthogonal subspaces can be regarded as the covariance matrix of a corresponding collection of vector-valued variables. If this operator separates into positive semidefinite components (as schematically depicted to the left), then the support structures of these components define a bipartite DAG (on the right). The components in the decomposition can be interpreted as the covariance matrices of independent vector-valued latent variables. Moreover, the collection of subspaces on which such an operator has support determines the observable children of the corresponding latent variable. Each observable variable can be constructed by adding the components collected from its parents.

and that it can be written

$$
Q = R + \sum_{n=1}^{N} C_n, \quad P^{(n)}C_nP^{(n)} = C_n, \quad R \ge 0, \quad C_n \ge 0,
$$

for

$$
P^{(n)} = \sum_{m \in \Omega_n} P_m, \quad R = \sum_{m=1}^{M} P_m R P_m,
$$

with $P_m$ being the projectors onto the subspaces $V_m$. Then there exists a causal model for the bipartite DAG $B(\{\Omega_n\}_{n=1}^N)$ with vector-valued variables $Y_1, \ldots, Y_M$ in $V_1, \ldots, V_M$ such that $Y = Y_1 + \cdots + Y_M$ satisfies

$$
\text{Cov}(Y) = Q.
$$

**Proof.** Let us define the set $\Omega := \cup_{n=1}^N \Omega_n$ and its complement $\Omega^c := \{1, \ldots, M\} \setminus \Omega$. By construction, $\Omega^c$ is the set of observable nodes in the bipartite DAG $B(\{\Omega_n\}_{n=1}^N)$ that have no parents (like vertex 4 in figure 1) and thus each element in $\Omega$ has at least one parent. By the definition of $P^{(n)}$ in (29) it follows that $\sum_{m' \in \Omega^c} P_m' C_n = C_n \sum_{m' \in \Omega^c} P_m' = 0$. In other words, the operators $C_n$ have no support on the subspaces belonging to parentless observable nodes. Let us now turn to the operator $R$ and its block diagonal decomposition $R = \sum_{m=1}^M R_m$ with $R_m := P_m R P_m$. We can write $R = \sum_{m' \in \Omega^c} R_m' + \sum_{m \in \Omega} R_m$. Consequently, $Q$ can be decomposed in one operator $\sum_{m \in \Omega} R_m + \sum_{m=1}^N C_n$ on the subspace $\bigoplus_{m \in \Omega} V_m$, and a collection of blocks $\{R_{m'} \}_{m' \in \Omega^c}$ on the corresponding subspaces $V_{m'} \text{ for } m' \in \Omega^c$. Since $R_{m'}$ is positive semidefinite, it can be interpreted as the covariance matrix of some random vector $Y_{m'} \text{ in } V_{m'}$. In the following we assume that we have made such an assignment for all $m' \in \Omega^c$. We also assume that these random vectors are independent.

Each $R_m$ for $m \in \Omega$ has its support inside the support of at least one $C_n$. Hence, we can 'distribute' the operators $R_m$ for $m \in \Omega$ by forming new positive semidefinite operators $\tilde{C}_n \ge 0$ such that

$$
\sum_{m \in \Omega} R_m + \sum_{n=1}^N C_n = \sum_{n=1}^N \tilde{C}_n = \tilde{Q},
$$

where one may note that $Q = \sum_{m' \in \Omega^c} R_{m'} + \tilde{Q}$.

In the following we shall assign observable and latent random variables to the vertices of the bipartite DAG $B(\{\Omega_n\}_{n=1}^N)$. For each $n \in \{1, \ldots, N\}$ and each $m \in \Omega$, let $L_m^n$ be a vector space that is isomorphic to $V_m$, and let $\phi_m^n : L_m^n \rightarrow V_m$ be an arbitrary isomorphism. (We assume that these isomorphisms preserve the inner-product structure, such that $\phi_m^n$ maps orthonormal bases of $L_m^n$ to orthonormal bases of $V_m$.) We regard the spaces in the collection $\{L_m^n\}_{m \in \Omega, n = 1, \ldots, N}$ as being orthogonal to each other. Define $L^+ : = \bigoplus_{m \in \Omega} L_m^n$, and the corresponding isomorphism $\phi^+ := \sum_{m \in \Omega} \phi_m^n$. Since each $\tilde{C}_n$ is positive semidefinite, it can be interpreted as the covariance matrix of a vector-valued random variable on $\bigoplus_{m \in \Omega} V_m$. Consequently, we can also find a vector-valued random variable $L_n$ on $L^+$ such that

$$
\tilde{C}_n = \text{Cov}(\phi^n L_n) = \phi^n \text{Cov}(L_n) \phi^{n^\dagger}.
$$

We assume that the random variables $L_{1}, \ldots, L_{N}$ are independent of each other, and also independent of $\left\{Y_{m^{\prime}}\right\}_{m^{\prime} \in \Omega^{\prime}}$.
The variables $L_{1}, \ldots, L_{N}$ serve as the latent variables corresponding to the latent nodes in the bipartite DAG $B\left(\left\{\Omega_{n}\right\}_{n=1}^{N}\right)$. In the following we shall construct a collection of vector-valued variables $\left\{Y_{m}\right\}_{m \in \Omega}$ as deterministic functions of the latent variables $L_{1}, \ldots, L_{N}$, in such a way that these functions correspond to the arrows in $B\left(\left\{\Omega_{n}\right\}_{n=1}^{N}\right)$, thus guaranteeing a valid causal model associated with this bipartite DAG.

Let us decompose the vector $L_{n}$ into its projections $L_{m}^{n}$ onto the subspaces $\mathcal{L}_{m}^{n}$. For each $m \in \Omega_{n}=\operatorname{ch}\left(L_{n}\right)$, the vector $L_{m}^{n}$ is associated to the observable node $O_{m}$. (One can imagine it to be transferred to node $O_{m}$.) Equivalently we can say that each observable node $m \in \Omega$ receives the vector $L_{m}^{n}$ from its ancestor $n \in \mathrm{pa}\left(O_{m}\right)$. On the observable node $m \in \Omega$ we construct a new vector $Y_{m}$ by adding all the vectors 'sent to it' from its parents

$$
Y_{m}:=\sum_{n \in \mathrm{pa}\left(O_{m}\right)} \phi_{m}^{n} L_{m}^{n}=\sum_{n \in \mathrm{pa}\left(O_{m}\right)} \phi_{m}^{n} L_{n}=\sum_{n=1}^{N} \phi_{m}^{n} L_{n}
$$

where the last equality follows since $P_{m} C_{n} P_{m}=0$ if $O_{m} \notin \operatorname{ch}\left(L_{n}\right)$, or equivalently if $L_{n} \notin \mathrm{pa}\left(O_{m}\right)$, and thus $\phi_{m}^{n} L_{n}=0$ if $n \notin \mathrm{pa}\left(O_{m}\right)$. The collection $\left\{Y_{m^{\prime}}\right\}_{m^{\prime} \in \Omega^{\prime}} \cup\left\{Y_{m}\right\}_{m \in \Omega}$ we take as the observable variables, and we define $Y:=\sum_{m^{\prime} \in \Omega^{\prime}} Y_{m^{\prime}}+\sum_{m \in \Omega} Y_{m}=\sum_{m^{\prime} \in \Omega^{\prime}} Y_{m^{\prime}}+\sum_{n=1}^{N} \phi^{n} L_{n}$.

Due to the fact that all $Y_{m^{\prime}}$ for $m^{\prime} \in \Omega^{c}$ are independent, and also independent of all $L_{n}$, we get

$$
\begin{aligned}
\operatorname{Cov}(Y)= & \sum_{m^{\prime} \in \Omega^{c}} \operatorname{Cov}\left(Y_{m^{\prime}}\right)+\operatorname{Cov}\left(\sum_{n=1}^{N} \phi^{n} L_{n}, \sum_{n^{\prime}=1}^{N} \phi^{n^{\prime}} L_{n^{\prime}}\right) \\
= & \sum_{m^{\prime} \in \Omega^{c}} R_{m^{\prime}}+\sum_{n, n^{\prime}=1}^{N} \phi^{n} \operatorname{Cov}\left(L_{n}, L_{n^{\prime}}\right) \phi^{n^{\prime}} \uparrow \\
& {\left[L_{1}, \ldots, L_{N} \text { are independent }\right] } \\
= & \sum_{m^{\prime} \in \Omega^{c}} R_{m^{\prime}}+\sum_{n=1}^{N} \phi^{n} \operatorname{Cov}\left(L_{n}\right) \phi^{n^{\uparrow}} \\
& {[\text { By (32)] }} \\
= & \sum_{m^{\prime} \in \Omega^{c}} R_{m^{\prime}}+\sum_{n=1}^{N} \hat{C}_{n} \\
& {[\text { By (31)] }} \\
= & Q .
\end{aligned}
$$

# B. Positive semidefinite operators as covariance matrices of vector-valued random variables over finite alphabets 

The material in the previous section presumes the existence of realizations of positive semidefinite operators as the covariance of some vector-valued variable, without making any restriction on ther nature. As mentioned above, each positive semi-definite operator (over a finite-dimensional real or complex vector space) can be regarded as the covariance of a multivariate normal distribution. However, suppose that we would require that the variable only can take a finite number of outcomes. Here we briefly discuss the conditions for such realizations, and provide an explicit construction (in the proof of Lemma 3).

For a (possibly vector-valued) random variable over a finite alphabet, we say that that the supported alphabet size is $D$, if there are precisely $D$ outcomes that occur with a non-zero probability.

Lemma 2. If a random variable $Y$ on a finite-dimensional real or complex inner-product space has a supported alphabet size $D$, then $\operatorname{rank}(\operatorname{Cov}(Y)) \leq D-1$.

Proof. We first note that $\operatorname{Cov}(Y)=\sum_{j=1}^{D} p_{j} y_{j} y_{j}^{\dagger}-\sum_{j=1}^{D} p_{j} y_{j} \sum_{j^{\prime}=1}^{D} p_{j^{\prime}} y_{j^{\prime}}^{\dagger}$. Since $\sum_{j=1}^{D} p_{j} y_{j}$ very manifestly is a linear combination of $y_{1}, \ldots, y_{D}$, it follows that the range of $\sum_{j=1}^{D} p_{j} y_{j} \sum_{j^{\prime}=1}^{D} p_{j^{\prime}} y_{j^{\prime}}^{\dagger}$ is a subset of the range of $\sum_{j=1}^{D} p_{j} y_{j} y_{j}^{\dagger}$, and thus $\operatorname{rank}(\operatorname{Cov}(Y)) \leq \operatorname{rank}\left(\sum_{j=1}^{D} p_{j} y_{j} y_{j}^{\dagger}\right) \leq D$. However, in the following we shall show that the stronger inequality

$\operatorname{rank}(\operatorname{Cov}(Y)) \leq D-1$ holds. To see this, let us first consider the case that $y_{1}, \ldots, y_{D}$ are linearly dependent. This means that at least one of these vectors is a linear combination of the others, and thus $\operatorname{rank}(\operatorname{Cov}(Y)) \leq D-1$. Let us now instead assume that $y_{1}, \ldots, y_{D}$ is a linearly independent set. Define $Q:=\left[Q_{j, j^{\prime}}\right]_{j, j^{\prime}=1}^{D}$ by $Q_{j, j^{\prime}}:=p_{j} \delta_{j, j^{\prime}}-$ $p_{j} p_{j^{\prime}}$, then $\operatorname{Cov}(Y)=\sum_{j, j^{\prime}} y_{j} Q_{j, j^{\prime}} y_{j^{\prime}}^{\dagger}$. Hence, $Q$ is the matrix representation of $\operatorname{Cov}(Y)$ with respect to the linearly independent, but not necessarily orthonormal set $y_{1}, \ldots, y_{D}$. One can realize that due to the linear independence, it follows that $\operatorname{rank}(\operatorname{Cov}(Y))=\operatorname{rank}(Q)$. Finally, let us define the $D$-dimensional vector $\overline{1}:=(1, \ldots, 1)^{\dagger} / \sqrt{D}$. One can confirm that $Q \overline{1}=0$. Hence, $\operatorname{rank}(Q) \leq D-1$, and we can conclude that $\operatorname{rank}(\operatorname{Cov}(Y)) \leq D-1$.

Lemma 3. Let $C$ be a positive semidefinite operator on a finite-dimensional real or complex inner-product space $\mathcal{V}$. For every $D \geq \operatorname{rank}(C)+1$ there exists a vector-valued random variable $Y$ on $\mathcal{V}$ with supported alphabet size $D$, such that $C=\operatorname{Cov}(Y)$. However, $C \neq \operatorname{Cov}(Y)$ for all $Y$ with a supported alphabet size $D<\operatorname{rank}(C)+1$.

Proof. Let $D$ be the supported alphabet size of a vector-valued random variable $Y$. If $D<\operatorname{rank}(C)+1$, then we know from Lemma 2 that $C \neq \operatorname{Cov}(Y)$. Hence, it remains to show that it is possible to find a $Y$ such that $C=\operatorname{Cov}(Y)$ for every $D \geq \operatorname{rank}(C)+1$. We thus wish to find a collection of vectors $y_{1}, \ldots, y_{D} \in \mathcal{V}$, and $p_{1}, \ldots, p_{D}$ with $p_{j}>0$, and $\sum_{j=1}^{D} p_{j}=1$, such that $C=\sum_{j=1}^{D} p_{j} y_{j} y_{j}^{\dagger}-\sum_{j=1}^{D} p_{j} y_{j} \sum_{j^{\prime}=1}^{D} p_{j^{\prime}} y_{j^{\prime}}^{\dagger}$.

Let $\left\{z_{k}\right\}_{k=1}^{K}$ be an orthonormal basis of the range (support) of the operator $C$, and let $P_{C}$ be the projector onto the range. Let $U$ be a matrix in $\mathbb{R}^{D \times D}\left(\mathbb{C}^{D \times D}\right)$ if the underlying space $\mathcal{V}$ is real (complex). Since $D \geq K+1$, we can assign the $(K+1)$ th column of $U$ to be the vector $\overline{1}:=(1, \ldots, 1)^{\dagger} / \sqrt{D}$ (i.e., $U_{j, K+1}=\frac{1}{\sqrt{D}}$ for all $j=1, \ldots, D$ ) and we arbitrarily complete the rest of the matrix $U$ such that it becomes orthogonal (unitary). Since $U$ is orthogonal (unitary), it follows that its columns form an orthonormal basis of $\mathbb{R}^{D}\left(\mathbb{C}^{D}\right)$. Hence, for each $k=1, \ldots, K$ it must be the case that the vector $\left(U_{j, k}\right)_{j=1}^{D}$ is orthogonal to $\overline{1}$, and thus

$$
\sum_{j=1}^{D} U_{j, k}=0, \quad k=1, \ldots, K
$$

Next, define the set of vectors $\left\{v_{j}\right\}_{j=1}^{D} \subset \mathcal{V}$ by $v_{j}:=\sum_{k=1}^{K} U_{j, k} z_{k}$. One can confirm that $\sum_{j=1}^{D} v_{j} v_{j}^{\dagger}=P_{C}$, as well as $\sum_{j=1}^{D} v_{j}=\sum_{k=1}^{K} \sum_{j=1}^{D} U_{j, k} z_{k}=0$, where we use (34). As the final step we define $p_{j}:=\frac{1}{D}$ and $y_{j}:=\sqrt{D} \sqrt{C} v_{j}$ for $j=1, \ldots, D$. One can confirm that

$$
\sum_{j=1}^{D} p_{j} y_{j} y_{j}^{\dagger}=\sqrt{C} \sum_{j=1}^{D} v_{j} v_{j}^{\dagger} \sqrt{C}=\sqrt{C} P_{C} \sqrt{C}=C, \quad \sum_{j=1}^{D} p_{j} y_{j}=\frac{1}{\sqrt{D}} \sqrt{C} \sum_{j=1}^{D} v_{j}=0
$$

Thus, if a vector-valued random variable $Y$ takes $y_{j}$ with probability $p_{j}$, we have $\operatorname{Cov}(Y)=C$.

# VI. IMPLIED OPERATOR INEQUALITIES 

Here we show that the existence of positive semidefinite decompositions as in Proposition 1 implies operator inequalities of a type studied in [47].

Consider as usual a bipartite DAG with latent variables $L_{1}, \ldots, L_{N}$ and observables $O_{1}, \ldots, O_{M}$ with assigned feature maps $Y_{1}, \ldots, Y_{M}$ into vector spaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$. For a number $d$ (whose meaning is going to be evident shortly) we define the following map on the space of operators on $\mathcal{V}=\oplus_{m=1}^{M} \mathcal{V}_{m}$

$$
\Phi(Q):=(d-1) P_{1} Q P_{1}+\sum_{m=2}^{M}\left(P_{m} Q P_{m}+P_{1} Q P_{m}+P_{m} Q P_{1}\right)
$$

where $P_{m}$ are the projectors onto the spaces $\mathcal{V}_{m}$ as discussed in section III. Theorem 4.1 in [47] does in essence say that if all the latent variables $L_{n}$ in the given bipartite DAG have degree at most $d$, then the resulting covariance matrix $\operatorname{Cov}(Y)$ satisfies

$$
\Phi(\operatorname{Cov}(Y)) \geq 0
$$

or if one prefers matrix notation

$$
\left[\begin{array}{ccccc}
(d-1) \operatorname{Cov}\left(Y_{1}\right) & \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \cdots & \cdots & \operatorname{Cov}\left(Y_{1}, Y_{M}\right) \\
\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & 0 & \cdots & 0 \\
\vdots & 0 & \ddots & \ddots & \vdots \\
\vdots & \vdots & \ddots & \ddots & 0 \\
\operatorname{Cov}\left(Y_{M}, Y_{1}\right) & 0 & \cdots & 0 & \operatorname{Cov}\left(Y_{M}\right)
\end{array}\right] \geq 0
$$

Hence, by deleting a particular collection of blocks from the full covariance matrix $\operatorname{Cov}(Y)$, and adding copies of the diagonal block $\operatorname{Cov}\left(Y_{1}\right)$, we obtain a positive semidefinite operator. It may be worth emphasizing that mere positive semidefiniteness of $Q$ is not enough to guarantee that $\Phi(Q)$ is positive semidefinite. Hence, (36) can indeed be used as a test of the underlying latent structure. As one may note, equations (36) and (37) single out observable 1 , but by relabelling we can obtain analogous inequalities for all observables. As an example, for the triangular scenario in figure 3, the inequality (37) and its permutations take the form

$$
\left[\begin{array}{ccc}
\operatorname{Cov}\left(Y_{1}\right) & \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & 0 \\
\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
0 & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right] \geq 0, \quad\left[\begin{array}{ccc}
\operatorname{Cov}\left(Y_{1}\right) & \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & 0 \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & 0 & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right] \geq 0, \quad\left[\begin{array}{ccc}
\operatorname{Cov}\left(Y_{1}\right) & 0 & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
0 & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right] \geq 0
$$

The following proposition shows that the semidefinite decomposition implies the operator inequality (36) under the assumption that all the latent variables (regarded as vertices in a bipartite graph) have the degree at most $d$.

Proposition 3. For a bipartite $D A G$ with latent variables $L_{1}, \ldots, L_{N}$, each with degree at most $d$, and observables $O_{1}, \ldots, O_{M}$ with assigned feature maps $Y_{1}, \ldots, Y_{M}$ into finite-dimensional real or complex inner-product spaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$, the covariance matrix of $Y=\sum_{m=1}^{M} Y_{m}$ satisfies $\Phi(\operatorname{Cov}(Y)) \geq 0$, where $\Phi$ is as defined in (35).

Proof. We know from Proposition 1 that $\operatorname{Cov}(Y)=R+\sum_{n=1}^{N} C_{n}$ with $P^{(n)} C_{n} P^{(n)}=C_{n}, C_{n} \geq 0$, and where $R$ is such that $\sum_{m} P_{m} R P_{m}=R$ and $R \geq 0$. Due to this, we have

$$
\Phi(R)=(1-d) P_{1} R P_{1}+\sum_{m=2}^{M} P_{m} R P_{m} \geq 0
$$

For each $C_{n}$ we can distinguish two cases.
In the first case, $C_{n}$ has no support on $\mathcal{V}_{1}$, i.e., $P_{1} C_{n} P_{1}=0$. Due to the positive semidefiniteness of $C_{n}$ it also follows that $P_{1} C_{n} P_{j}=0$ for $j=2, \ldots, M$, and thus

$$
\Phi\left(C_{n}\right)=\sum_{m=2}^{M} P_{m} C_{n} P_{m} \geq 0
$$

In the second case, $C_{n}$ does have a support on $\mathcal{V}_{1}$, meaning that $P_{1} C_{n} P_{1} \neq 0$. By assumption, the latent variable $L_{n}$ has degree at most $d$, which means that $C_{n}$ has support on at most $d$ of the subspaces $\mathcal{V}_{1}, \ldots, \mathcal{V}_{M}$. Hence, apart form $\mathcal{V}_{1}$, there are at most $d-1$ further spaces involved. We enumerate these spaces as $\mathcal{V}_{m(2)}, \ldots, \mathcal{V}_{m(d)}$, and let $\mathcal{V}_{m(1)}=\mathcal{V}_{1}$. Hence, it may be the case that $P_{m(j)} C_{n} P_{m(j)} \neq 0$ for $j=1, \ldots, d$, while $P_{m} C_{n} P_{m}=0$ for the remaining values of $m$. Due to the positive semidefiniteness of $C_{n}$, we can analogously have $P_{1} C_{n} P_{m(j)} \neq 0$, and $P_{m(j)} C_{n} P_{1} \neq 0$, but $P_{1} C_{n} P_{m}=0$, and $P_{m} C_{n} P_{1}=0$ for the other values of $m$. We can conclude that

$$
\begin{aligned}
\Phi\left(C_{n}\right) & =(d-1) P_{1} C_{n} P_{1}+\sum_{m=2}^{M}\left(P_{m} C_{n} P_{m}+P_{1} C_{n} P_{m}+P_{m} C_{n} P_{1}\right) \\
& =(d-1) P_{1} C_{n} P_{1}+\sum_{j=2}^{d}\left(P_{m(j)} C_{n} P_{m(j)}+P_{1} C_{n} P_{m(j)}+P_{m(j)} C_{n} P_{1}\right) \\
& =\sum_{j=2}^{d}\left(P_{1}+P_{m(j)}\right) C_{n}\left(P_{1}+P_{m(j)}\right) \geq 0
\end{aligned}
$$

The combination of (38), (39) and (40) yields $\Phi(\operatorname{Cov}(Y))=\Phi(R)+\sum_{n=1}^{N} \Phi\left(C_{n}\right) \geq 0$, which proves (36).

We note that the operator inequalities derived here need not be tight in all cases. Indeed, it is not hard to verify that the maps $\Phi_{\alpha}$ defined by

$$
\Phi_{\alpha}:\left[\begin{array}{cccc}
\operatorname{Cov}\left(Y_{1}\right) & \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right] \mapsto\left[\begin{array}{cccc}
\operatorname{Cov}\left(Y_{1}\right) & e^{i \alpha} \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
e^{-i \alpha} \operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right]
$$

preserve the set of covariance matrices compatible with the triangle scenario. Here, $\alpha \in[0,2 \pi)$ is a phase factor. In particular, $\Phi_{\alpha}$ preserves positivity when acting on covariance matrices arising in this context. This is a strictly stronger result than the one we have obtained above: The map $\Phi$ treated in the proposition is just the equal-weight convex combination of $\Phi_{\pi}$ and $\Phi_{0}$ :

$$
\frac{1}{2}\left[\begin{array}{cccc}
\operatorname{Cov}\left(Y_{1}\right) & \operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right]+\frac{1}{2}\left[\begin{array}{cccc}
\operatorname{Cov}\left(Y_{1}\right) & -\operatorname{Cov}\left(Y_{1}, Y_{2}\right) & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
-\operatorname{Cov}\left(Y_{2}, Y_{1}\right) & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right]=\left[\begin{array}{cccc}
\operatorname{Cov}\left(Y_{1}\right) & 0 & \operatorname{Cov}\left(Y_{1}, Y_{3}\right) \\
0 & \operatorname{Cov}\left(Y_{2}\right) & \operatorname{Cov}\left(Y_{2}, Y_{3}\right) \\
\operatorname{Cov}\left(Y_{3}, Y_{1}\right) & \operatorname{Cov}\left(Y_{3}, Y_{2}\right) & \operatorname{Cov}\left(Y_{3}\right)
\end{array}\right]
$$

It may potentially be fruitful to consider a general theory of maps that preserve the convex cone of covariances compatible with a given causal structure.

# VII. UNIVERSAL FEATURE MAPS FOR FINITE CATEGORICAL VARIABLES 

As the reader may have realized, the choice of feature maps $Y^{(m)}$ may affect the outcome of the semidefinite test. In other words, even if we find a particular setup that is compatible with the given bipartite DAG, it may be the case that another assignment of the vectors $Y_{m}$ could yield a violation; thus potentially suggesting that we ideally should test an infinite number of choices. However, in the case of observable variables with only finite number of outcomes, we shall here see that one can make a single test, based on a sufficiently 'powerful' choice of feature maps. Suppose that the variables $O_{m}$ can only take a finite number of outcomes $o_{1}^{m}, \ldots, o_{d_{m}}^{m}$. An arbitrary assignment of a feature map would correspond to a collection of vectors $y_{1}^{m}, \ldots, y_{d_{m}}^{m} \in \mathcal{V}_{m}$ for some vector space $\mathcal{V}_{m}$. Now suppose that we make the additional restriction that $y_{1}^{m}, \ldots, y_{d_{m}}^{m}$ are linearly independent, and that $\operatorname{dim}\left(\mathcal{V}_{m}\right)=d_{m}$. Suppose that we have some other arbitrary assignment of feature map $\tilde{Y}_{m}$ given by a collection of vectors $\tilde{y}_{1}^{m}, \ldots, \tilde{y}_{d_{m}}^{m} \in \tilde{\mathcal{V}}_{m}$ for some vector space $\tilde{\mathcal{V}}_{m}$ (without any requirement of linear independence). One can realize that it is always possible to find a linear map $\phi_{m}: \mathcal{V}_{m} \rightarrow \tilde{\mathcal{V}}_{m}$ such that $\phi_{m} y_{j}^{m}=\tilde{y}_{j}^{m}$, and thus $\phi_{m} Y_{m}=\tilde{Y}_{m}$. To see this, one can note that since $y_{1}^{m}, \ldots, y_{d_{m}}^{m}$ is a linearly independent set in a $d_{m}$-dimensional space, it follows that the Gram matrix $G=\left[G_{i, j^{\prime}}\right]_{i, j^{\prime}=1}^{d_{m}}$ with $G_{i, j^{\prime}}:=\left(y_{j}^{m}, y_{j^{\prime}}^{m}\right)$ is invertible (and positive definite). One can confirm that $\phi_{m}$ defined by $\phi_{m}(v):=\sum_{j j^{\prime}} \tilde{y}_{j}^{m}\left[G^{-1}\right]_{j j^{\prime}}\left(y_{j^{\prime}}^{m}, v\right)$ satisfies $\phi_{m} y_{j}^{m}=\tilde{y}_{j}^{m}$. In other words, a feature map with linearly independent components is 'universal' in the sense that we can generate all other feature maps on all other vector spaces, and it is moreover sufficient to do this via linear transformations.

For a collection of universal feature maps $Y_{1}, \ldots, Y_{M}$ assigned to $O_{1}, \ldots, O_{M}$, we can reach all other feature maps $\tilde{Y}_{1}, \ldots, \tilde{Y}_{M}$, by linear operations $\tilde{Y}_{m}=\phi_{m} Y_{m}$. Moreover, the covariance matrix $\operatorname{Cov}(Y)$ for $Y=\sum_{m=1}^{M} Y_{m}$ and the covariance matrix $\operatorname{Cov}(\tilde{Y})$ for $\tilde{Y}=\sum_{m=1}^{M} \tilde{Y}_{m}$ are related by $\operatorname{Cov}(\tilde{Y})=\phi \operatorname{Cov}(Y) \phi^{\dagger}$ for $\phi:=\sum_{m=1}^{M} \phi_{m}$. One can realize that if $\operatorname{Cov}(Y)$ satisfies the decomposition in Proposition 1 for a given bipartite DAG, then $\operatorname{Cov}(\tilde{Y})$ also satisfies the decomposition. We can conclude that it is sufficient to apply the semidefinite test for a single collection of feature maps, where each of these have linearly independent components. (A convenient choice would be mappings to orthonormal bases.)

It is conceivable that a similar construction would hold for variables with a countably infinite number of outcomes, and it is an interesting question if one in some sense could make 'universal' assignments of feature maps also in the case of a continuum. However, we shall not consider these issues in this investigation, but leave them as open questions.

## VIII. MONOTONICITY UNDER LOCAL OPERATIONS

Suppose that we would process each observable variable in a collection $O_{1}, \ldots, O_{M}$ 'locally'. In other words, the output $\tilde{O}_{m}$ is a (possibly random) function only of $O_{m}$. If we restrict ourselves to discrete random variables, then

this type of mapping from an input distribution $P^{M}$ of the $O_{1}, \ldots, O_{M}$, to the output distribution $\tilde{P}^{M}$ of $\tilde{O}_{1}, \ldots, \tilde{O}_{M}$ can be written

$$
\tilde{P}^{M}\left(\tilde{x}_{1}, \ldots, \tilde{x}_{M}\right):=\sum_{x_{1} \ldots, x_{M}} P^{1}\left(\tilde{x}_{1} \mid x_{1}\right) \cdots P^{M}\left(\tilde{x}_{M} \mid x_{M}\right) P^{M}\left(x_{1}, \ldots, x_{M}\right)
$$

where all $P^{m}\left(\tilde{x}_{m} \mid x_{m}\right)$ are conditional distributions. From this construction it is clear that if a distribution $P^{M}$ is compatible with the given bipartite DAG, then the resulting distribution $\tilde{P}^{M}$ on $\tilde{O}_{1}, \ldots, \tilde{O}_{M}$ will also be compatible with the very same DAG. In other words, compatibility with a given bipartite DAG is in this sense a monotone with respect to local operations.

There is a priori no reason to expect that relaxations of the compatibility problem would satisfy this monotonicity. However, here we show that this property is respected by the semidefinite test, if the latter is based on universal feature maps (in the sense of the previous section). The fact that universality is needed can be seen from the following trivial special case. We assign feature maps $Y_{m}$ to $O_{m}$, and $\tilde{Y}_{m}$ to $\tilde{O}_{m}$. In principle we can for each $m$ choose all components of $Y_{m}$ to be identical, thus resulting in a zero covariance matrix that trivially satisfies all decompositions, while $\tilde{Y}_{m}$ may still result in a violation. By assuming that all the feature maps $Y_{m}$ are universal, we shall in the following see that monotonicity is guaranteed.

Let us first focus on the transformation of a single observable variable $O_{m}$ to $\tilde{O}_{m}$, and let us assume that $Y_{m}$ has the linearly independent components $y_{1}^{m}, \ldots, y_{K}^{m}$, with Gram matrix $G=\left[G_{x, x^{\prime}}\right]_{x, x^{\prime}=1}^{K}$ with $G_{x, x^{\prime}}=\left(y_{x}^{m}, y_{x^{\prime}}^{m}\right)$, in a $K$-dimensional vector space $\mathcal{V}_{m} . G$ is invertible since $y_{1}^{m}, \ldots, y_{K}^{m}$ are linearly independent. Let $\tilde{y}_{1}^{m}, \ldots, \tilde{y}_{L}^{m}$ be the components of $\tilde{Y}_{m}$ in $\tilde{\mathcal{V}}_{m}$. (If $L=K$ we can of course choose $\tilde{y}^{m}:=y^{m}$ as a special case.) Define $\psi_{m}(v):=$ $\sum_{\tilde{x}, x^{\prime}, x^{\prime \prime}} \tilde{y}_{\tilde{x}} P^{m}\left(\tilde{x} \mid x^{\prime}\right)\left[G^{-1}\right]_{x^{\prime}, x^{\prime \prime}}\left(y_{x^{\prime \prime}}, v\right)$. (Here and in the following we omit the superscript ' $m$ ' on the vectors $y$ for notational convenience.) One can confirm that $E\left(\tilde{Y}_{m}\right)=\psi_{m}\left(E\left(Y_{m}\right)\right)$, and thus with $\psi=\sum_{m} \psi_{m}$ we get $E(\tilde{Y})=$ $\psi(E(Y))$.

It may be very tempting to assume that $\operatorname{Cov}(\tilde{Y})$ would be equal to $\psi \operatorname{Cov}(Y) \psi^{\dagger}$. However, this is generally not the case. The off-diagonal blocks for $m \neq m^{\prime}$ satisfy $\operatorname{Cov}\left(\tilde{Y}_{m}, \tilde{Y}_{m^{\prime}}\right)=\psi_{m} \operatorname{Cov}\left(Y_{m}, Y_{m^{\prime}}\right) \psi_{m^{\prime}}^{\dagger}$.

However, for the diagonal blocks it is the case that

$$
\begin{aligned}
\operatorname{Cov}\left(\tilde{Y}_{m}\right) & =\psi_{m} \operatorname{Cov}\left(Y_{m}\right) \psi_{m}^{\dagger}+W_{m} \\
W_{m} & :=\sum_{\tilde{x}, x} \tilde{y}_{\tilde{x}} \tilde{y}_{\tilde{x}}^{\dagger} P^{m}(\tilde{x} \mid x) P\left(O_{m}=x\right)-\sum_{\tilde{x}, \tilde{x}^{\prime}, x} \tilde{y}_{\tilde{x}} \tilde{y}_{\tilde{x}^{\prime}}^{\dagger} P^{m}(\tilde{x} \mid x) P^{m}\left(\tilde{x}^{\prime} \mid x\right) P\left(O_{m}=x\right)
\end{aligned}
$$

One can note that each 'correction term' $W_{m}$ is supported only on the subspace $\tilde{\mathcal{V}}_{m}$, and one can moreover show that $W_{m} \geq 0$. To see the latter, let $c \in \tilde{\mathcal{V}}_{m}$, and define $z_{\tilde{x}}=\left(c, \tilde{y}_{\tilde{x}}\right)$. Then

$$
\left(c, W_{m} c\right)=\sum_{x} P\left(O_{m}=x\right)\left(\sum_{\tilde{x}}\left|z_{\tilde{x}}\right|^{2} P^{m}(\tilde{x} \mid x)-\left|\sum_{\tilde{x}} z_{\tilde{x}} P^{m}(\tilde{x} \mid x)\right|^{2}\right)=\sum_{x, \tilde{x}} P\left(O_{m}=x\right) P^{m}(\tilde{x} \mid x)\left|z_{\tilde{x}}-\sum_{\tilde{x}^{\prime}} P^{m}\left(\tilde{x}^{\prime} \mid x\right) z_{\tilde{x}^{\prime}}\right|^{2} \geq 0
$$

If $\operatorname{Cov}(Y)$ satisfies the decomposition (16) in Proposition 1 for some bipartite DAG, then one can confirm that $\psi \operatorname{Cov}(Y) \psi^{\dagger}$ also satisfies the corresponding decomposition with respect to the subspaces $\left\{\tilde{\mathcal{V}}_{m}\right\}_{m}$. Moreover, since the correction terms $W_{m}$ are positive semidefinite and block-diagonal with respect to these subspaces, it follows that $\operatorname{Cov}(\tilde{Y})=\psi \operatorname{Cov}(Y) \psi^{\dagger}+\sum_{m} W_{m}$ also satisfies the decomposition. We can thus conclude that if the initial feature maps $Y_{1}, \ldots, Y_{M}$ are universal, then the test is monotonous with respect to local operations.

As a final remark one may note that in the special case that all $P^{m}(\tilde{x} \mid x)$ correspond to deterministic mappings, i.e., when the output $\tilde{x}$ is a (deterministic) function of the input $x$, then $P^{m}(\tilde{x} \mid x) P^{m}\left(\tilde{x}^{\prime} \mid x\right)=\delta_{\tilde{x}, \tilde{x}^{\prime}} P^{m}(\tilde{x} \mid x)$, and (42) results in $W_{m}=0$, which yields $\operatorname{Cov}(\tilde{Y})=\psi \operatorname{Cov}(Y) \psi^{\dagger}$. Linear transformations $\phi^{m}: \mathcal{V}_{m} \rightarrow \tilde{\mathcal{V}}_{m}$ all result in mappings $\tilde{Y}_{m}=\phi^{m}\left(Y_{m}\right)$ that belong to this deterministic special case (presuming that the maps $\phi^{m}$ themselves are not random variables) where we let $P^{m}\left(\tilde{x} \mid x^{\prime}\right)=\delta_{\tilde{x}, x^{\prime}}$ and $\tilde{y}_{\tilde{x}}^{m}=\phi^{m}\left(y_{\tilde{x}}^{m}\right)$, thus leading to $\operatorname{Cov}(\phi Y)=\phi \operatorname{Cov}(Y) \phi^{\dagger}$ (cf. the isomorphisms in (32), or the maps $\phi$ used in section VII).

# IX. A MONOTONE FAMILY OF DISTRIBUTIONS 

Here we shall consider a specific family of multi-partite distributions that is monotone in the sense of the previous section, for which the analysis of the semidefinite decomposition simplifies. We shall in particular consider the case of the triangular scenario in figure 3, which turns out to be convenient for the comparison with the entropic tests, which we consider in section $X$.

# A. Defining the family 

Suppose that we have a collection of variables, each of which has $D \geq 2$ possible outcomes. In equation (41) we described local operations transforming an initial distribution $P^{M}$. For the local operations we do in this case choose

$$
P_{p}(\bar{x} \mid x):=(1-p) \delta_{\bar{x}, x}+p \frac{1}{D}
$$

Hence, on each variable we (independently) apply the same type of process, where with probability $p$ we replace the input with a uniformly distributed output, and with probability $1-p$ leave the input intact. Here we choose the input distribution to be $P^{M}\left(x_{1}, \ldots, x_{M}\right)=\delta_{x_{1}, \ldots, x_{M}} / D$, where the generalized Kronecker delta is such that $\delta_{x_{1}, \ldots, x_{M}}=1$ if $x_{1}=\cdots=x_{M}$, while zero otherwise. Hence, $P^{M}\left(x_{1}, \ldots, x_{M}\right)$ describes $M$ perfectly correlated variables. By applying (41) with the local operations (43) we thus obtain a new global distribution

$$
\tilde{P}_{p}^{M: D}\left(\bar{x}_{1}, \ldots, \bar{x}_{M}\right):=\frac{1}{D} \sum_{x_{1}, \ldots, x_{M}} P_{p}\left(\bar{x}_{1} \mid x_{1}\right) \cdots P_{p}\left(\bar{x}_{M} \mid x_{M}\right) \delta_{x_{1}, \ldots, x_{M}}
$$

where we have added the extra superscript $D$ to indicate the alphabet size of the local random variables. By construction, this distribution is permutation symmetric over all the variables. Moreover, one can confirm that all mono-, bi-, and higher-partite margins of $\tilde{P}_{p}^{M: D}$ are independent of how many parties $M$ the total distribution $\tilde{P}_{p}^{M: D}$ involves. For example, the bipartite margin of $\tilde{P}_{p}^{M: D}$ is equal to $\tilde{P}_{p}^{2: D}$. Generally, for $M^{\prime}<M$ it is the case that

$$
\tilde{P}_{p}^{M^{\prime}: D}\left(\bar{x}_{1}, \ldots, \bar{x}_{M^{\prime}}\right)=\sum_{\bar{x}_{M^{\prime}+1}, \ldots, \bar{x}_{M}} \tilde{P}_{p}^{M: D}\left(\bar{x}_{1}, \ldots, \bar{x}_{M}\right)
$$

Hence, every margin of every family member is another family member.
Since $\tilde{P}_{p}^{M: D}$ is a product distribution over all the observable variables, it is compatible with every bipartite DAG, while $\tilde{P}_{0}^{M: D}$ is perfectly correlated, and thus would only be compatible with bipartite DAGs where some latent variable has edges to all observable variables. One can note that the local operations in (43) are such that if $1 \geq p^{\prime} \geq p \geq 0$, then there exists a $1 \geq q \geq 0$ such that

$$
P_{p^{\prime}}(\bar{x} \mid x)=\sum_{x^{\prime}} P_{q}\left(\bar{x} \mid x^{\prime}\right) P_{p}\left(x^{\prime} \mid x\right)
$$

(Any $1 \geq q \geq 0$ is a valid choice if $p=1$, while $q=\left(p^{\prime}-p\right) /(1-p)$ if $1>p \geq 0$.) Consequently, if $p^{\prime} \geq p$, then $\tilde{P}_{p^{\prime}}^{M: D}$ can be generated from $\tilde{P}_{p}^{M: D}$ by local operations. By the reasoning in section VIII it thus follows that there is some value $p^{*}$ where $\tilde{P}_{p}^{M: D}$ switches from being incompatible to being compatible with the given bipartite DAG (and it cannot switch back again for higher values of $p$ ). From section VIII we also know that the semidefinite test also has this monotonic behavior if we choose universal feature maps, although the switch may occur at a lower value of $p$.

## B. Within the family: the existence of a semidefinite decomposition is independent of the local alphabet size

Here we show that the semidefinite test takes a particularly simple form for the family $\tilde{P}_{p}^{M: D}$. In essence we show that the test can be reduced to a test on an $M \times M$ matrix that only depends on $p$, but not on the local alphabet size $D$. A similar result was obtained in (section 4.5 of) [47], for the operator inequalities described in section VI, but for distributions of the type $v \delta_{x_{1}, \ldots, x_{M}} / D-(1-v) / D^{2}$, while we here consider the family $\tilde{P}_{p}^{M: D}$ defined by (44).

Suppose that we have an $M$-partite distribution $\tilde{P}_{p}^{M: D}$. We know from the previous section that this distribution is permutation symmetric, and in particular we know from (45) that all bipartite marginal distributions are of the form $\tilde{P}_{p}^{2: D}$, and all mono-partite marginals are of the form $\tilde{P}_{p}^{1: D}$. One can moreover confirm that

$$
\tilde{P}_{p}^{2: D}\left(\bar{x}, \bar{x}^{\prime}\right)=(1-p)^{2} \frac{1}{D} \delta_{\bar{x}, \bar{x}^{\prime}}+p(2-p) \frac{1}{D^{2}}, \quad \tilde{P}_{p}^{1: D}\left(\bar{x}_{1}\right)=\frac{1}{D}
$$

In order to construct a covariance matrix, we here assume feature maps $Y_{1}, \ldots, Y_{M}$ that have orthonormal components (i.e., feature map $Y_{m}$ maps the set of possible outcomes of the $m$ th random variable to an orthonormal

basis of $\mathcal{V}_{m}$, where $\operatorname{dim}\left(\mathcal{V}_{m}\right)=D$ ). Hence, the total space $\mathcal{V}=\mathcal{V}_{1} \oplus \cdots \oplus \mathcal{V}_{M}$ is $D M$-dimensional, and we can write it as a tensor product $\mathcal{V}=\mathcal{V}^{D} \otimes \mathcal{V}^{M}$ of a $D$-dimensional space $\mathcal{V}^{D}$ and an $M$-dimensional space $\mathcal{V}^{M}$. By choosing an orthonormal basis $\left\{e_{m}\right\}_{m=1}^{M}$ of $\mathcal{V}^{M}$, we can identify $\mathcal{V}_{m}=\mathcal{V}^{D} \otimes \operatorname{Sp}\left\{e_{m}\right\}$. In section III we defined the projectors $P_{m}$ onto the subspaces $\mathcal{V}_{m}$, and we can write these projectors as

$$
P_{m}=\hat{1}_{D} \otimes \hat{e}_{m}
$$

where $\hat{1}_{D}$ is the identity operator on $\mathcal{V}^{D}$, and $\hat{e}_{m}$ is the projector onto $e_{m}$.
The covariance matrix $\operatorname{Cov}(Y)$ for the random variable $Y=Y_{1}+\cdots+Y_{M}$ is an $M D \times M D$ matrix and takes a particularly simple form

$$
\operatorname{Cov}(Y)=\left[\begin{array}{ccccc}
Q & (1-p)^{2} Q & \cdots & (1-p)^{2} Q \\
(1-p)^{2} Q & Q & \ddots & \vdots \\
\vdots & \ddots & Q & (1-p)^{2} Q \\
(1-p)^{2} Q & \cdots & (1-p)^{2} Q & Q
\end{array}\right]=\frac{1}{D} Q \otimes C(p)
$$

where we define the $M \times M$ matrix

$$
C(p):=\left[\begin{array}{ccccc}
1 & (1-p)^{2} & \cdots & (1-p)^{2} \\
(1-p)^{2} & 1 & \ddots & \vdots \\
\vdots & \ddots & & (1-p)^{2} \\
(1-p)^{2} & \cdots & (1-p)^{2} & 1
\end{array}\right]
$$

and the $D \times D$ matrix $Q$ with elements

$$
Q_{\bar{x}, \bar{x}^{\prime}}:=\delta_{\bar{x}, \bar{x}^{\prime}}-\frac{1}{D}, \quad \bar{x}, \bar{x}^{\prime}=1, \ldots, D
$$

Note that we can write $Q=\hat{1}_{D}-c c^{\dagger}$, where $c=(1, \ldots, 1)^{\dagger} / \sqrt{D} \in \mathcal{V}^{D}$ is normalized. Hence, $Q$ is the projector onto the $(D-1)$-dimensional subspace of $\mathcal{V}^{D}$ that is the orthogonal complement to the one-dimensional subspace spanned by $c$. From $Q$ being a projector, it also follows that $Q \geq 0$.

Suppose now that we have a particular bipartite DAG $B$ with observable variables $O_{1}, \ldots, O_{M}$ and latent variables $L_{1}, \ldots, L_{N}$. As we recall from section IV, the semidefinite test is characterized via the projectors $P^{(n)}=\sum_{m \in \operatorname{ch}\left(L_{n}\right)} P_{m}$ as

$$
\operatorname{Cov}(Y)=R+\sum_{n=1}^{N} C_{n}, \quad P^{(n)} C_{n} P^{(n)}=C_{n}, \quad C_{n} \geq 0, \quad \sum_{m=1}^{M} P_{m} R P_{m}=R, \quad R \geq 0
$$

In the present case, we can write these projectors as

$$
P^{(n)}=I_{D} \otimes \bar{P}^{(n)}, \quad \bar{P}^{(n)}=\sum_{m \in \operatorname{ch}\left(L_{n}\right)} \bar{P}_{m}
$$

with $\bar{P}_{m}$ as in (48).
For each fixed number of observable variables $M$, local alphabet size $D$, and given bipartite DAG $B$, we know that the family $\bar{P}_{p}^{M: D}$ is monotone with respect to $p$, in the sense that the covariance matrix $\operatorname{Cov}(Y)$ satisfies the semidefinite decomposition for all $p$ beyond a certain threshold value, while it is violated for all values below. The following proposition shows that this threshold is independent of $D$, and that it can be determined via simplified decomposition of the matrix $C(p)$.
Proposition 4. Let $\operatorname{Cov}(Y)$ be the covariance matrix, for feature maps with orthonormal components, corresponding to the distribution $\bar{P}_{p}^{M: D}$, as defined in (44), for $M$ observable variables, and local alphabet size $D \geq 2$. For each value $1 \geq p \geq 0$ it is the case that $\operatorname{Cov}(Y)$ satisfies the semidefinite decomposition (52) with respect to a given bipartite DAG B, if and only if $C(p)$, defined in (50), satisfies the decomposition

$$
C(p)=\bar{R}+\sum_{n=1}^{N} \bar{C}_{n}, \quad \bar{P}^{(n)} C_{n} \bar{P}^{(n)}, \quad \bar{C}_{n} \geq 0, \quad \sum_{m=1}^{N} \bar{P}_{m} \bar{R} \bar{P}_{m}=\bar{R}, \quad \bar{R} \geq 0
$$

Moreover, there exists a number $1 \geq \bar{p}(B) \geq 0$ that does not depend on $D$, such that $\operatorname{Cov}(Y)$ satisfies (52) and $C(p)$ satisfies (54) for all $p>\bar{p}(B)$, while $\operatorname{Cov}(Y)$ and $C(p)$ do not satisfy the decompositions for $p<\bar{p}(B)$.

Proof. First we shall show that if $C(p)$ satisfies the decomposition, then $\operatorname{Cov}(Y)$ also satisfies the decomposition. Let $p$ be any $1 \geq p \geq 0$ such that there exists a semidefinite decomposition of $C(p)$ as in (50). Equation (54) provides $\tilde{R}$ and $\tilde{C}_{n}$. Define $R:=Q \otimes \tilde{R} / D$ and $C_{n}:=Q \otimes \tilde{C}_{n} / D$. Thus defined, it follows that

$$
R+\sum_{n} C_{n}=\frac{1}{D} Q \otimes\left(\tilde{R}+\sum_{n} \tilde{C}_{n}\right)=\frac{1}{D} Q \otimes C(p)=\operatorname{Cov}(Y)
$$

Moreover, by the conditions in (54) and the observations in (53), it follows that

$$
P^{(n)} C_{n} P^{(n)}=\left[\hat{1}_{D} \otimes \tilde{P}^{(n)}\right]\left[\frac{1}{D} Q \otimes \tilde{C}_{n}\right]\left[\hat{1}_{D} \otimes \tilde{P}^{(n)}\right]=C_{n}
$$

and $C_{n}=Q \otimes \tilde{C}_{n} / D \geq 0$.
Furthermore, by the conditions in (54) and (48), it follows that

$$
\sum_{m} P_{m} R P_{m}=\sum_{m}\left[\hat{1}_{D} \otimes \tilde{P}_{m}\right]\left[\frac{1}{D} Q \otimes \tilde{R}\right]\left[\hat{1}_{D} \otimes \tilde{P}_{m}\right]=R
$$

and $R=Q \otimes \tilde{R} / D \geq 0$. Hence, this procedure produces a valid semidefinite decomposition of $\operatorname{Cov}(Y)$. Hence, for every $p$ for which $C(p)$ has a valid decomposition, it follows that $\operatorname{Cov}(Y)$ also has a valid decomposition.

Next we prove the opposite implication, namely that the existence of a decomposition of $\operatorname{Cov}(Y)$ implies a decomposition of $C(p)$. Let us thus assume that there is a $1 \geq p \geq 0$ for which there exists a decomposition of $\operatorname{Cov}(Y)$ as in (52). Equation (52) provides $R$ and $C_{n}$. Let $v \in \mathcal{V}^{D}$ be normalized, and such that $Q v=v$. Such a $v$ always exists, since $Q$ is a projector onto a $(D-1)$-dimensional subspace of $\mathcal{V}^{D}$ and $D \geq 2$. Define $\tilde{R}:=D v^{\dagger} R v$ and $\tilde{C}_{n}:=D v^{\dagger} C_{n} v$ (where one should keep in mind that e.g. $v^{\dagger} R v$ is an operator on $\mathcal{V}^{M}$, since $v \in \mathcal{V}^{D}$ ). Hence, by (52) and (49)

$$
\tilde{R}+\sum_{n} \tilde{C}_{n}=D v^{\dagger}\left(R+\sum_{n} C_{n}\right) v=D v^{\dagger} \operatorname{Cov}(Y) v=D v^{\dagger}\left[\frac{1}{D} Q \otimes C(p)\right] v=v^{\dagger} Q v C(p)=C(p)
$$

Moreover, by the conditions in (52) and the observations in (53), it follows that

$$
\tilde{P}^{(n)} \tilde{C}_{n} \tilde{P}^{(n)}=\tilde{P}^{(n)} D v^{\dagger} C_{n} v \tilde{P}^{(n)}=D v^{\dagger}\left[\hat{1}_{D} \otimes \tilde{P}^{(n)}\right] C_{n}\left[\hat{1}_{D} \otimes \tilde{P}^{(n)}\right] v=D v^{\dagger} P^{(n)} C_{n} P^{(n)} v=D v^{\dagger} C_{n} v=\tilde{C}_{n}
$$

and $\tilde{C}_{n}:=D v^{\dagger} C_{n} v \geq 0$. Furthermore, (52) and (48) yields

$$
\sum_{m} \tilde{P}_{m} \tilde{R} \tilde{P} M=\sum_{m} \tilde{P}_{m} D v^{\dagger} R v \tilde{P}_{m}=\sum_{m} D v^{\dagger}\left[\hat{1}_{D} \otimes \tilde{P}_{m}\right] R\left[\hat{1}_{D} \otimes \tilde{P}_{m}\right] v=D v^{\dagger}\left(\sum_{m} P_{m} R P_{m}\right) v=D v^{\dagger} R v=\tilde{R}
$$

and $\tilde{R}:=D v^{\dagger} R v \geq 0$. Hence, we can conclude that the decomposition of $\operatorname{Cov}(Y)$ induces a valid decomposition of $C(p)$ as in (54).

We know from section IX A that the family $\tilde{P}_{p}^{M: D}$ is monotone, in the sense that $\operatorname{Cov}(Y)$ (since it is based on orthonormal feature maps) satisfies the semidefinite decomposition for all $p$ beyond a certain threshold value, which we can call $\bar{p}(B)$, while violating the decomposition for all $p$ below $\bar{p}(B)$. From the above equivalence we conclude that the same transition is valid for $C(p)$ with respect to the decomposition in (54).

# C. Compatibility with the triangular DAG 

Here we consider the tripartite case and determine the value of $p$ where $\tilde{P}_{p}^{3: D}$ switches from not satisfying the semidefinite decomposition, to satisfying it, with respect to the triangular scenario in figure 3. The family of distributions $\tilde{P}_{p}^{M: D}$, defined in (44), does in the tripartite case take the form

$$
\begin{aligned}
\tilde{P}_{p}^{3: D}\left(\tilde{x}_{1}, \tilde{x}_{2}, \tilde{x}_{3}\right)= & (1-p)^{3} \frac{1}{D} \delta_{\tilde{x}_{1}, \tilde{x}_{2}, \tilde{x}_{3}} \\
& +p(1-p)^{2} \frac{1}{D^{2}}\left[\delta_{\tilde{x}_{1}, \tilde{x}_{2}}+\delta_{\tilde{x}_{1}, \tilde{x}_{3}}+\delta_{\tilde{x}_{2}, \tilde{x}_{3}}\right] \\
& +p^{2}(3-2 p) \frac{1}{D^{3}}
\end{aligned}
$$

and the matrix $C(p)$ and the projectors $\hat{P}^{(1)}, \hat{P}^{(2)}$, and $\hat{P}^{(3)}$ become

$$
C(p)=\left[\begin{array}{ccc}
1 & (1-p)^{2} & (1-p)^{2} \\
(1-p)^{2} & 1 & (1-p)^{2} \\
(1-p)^{2} & (1-p)^{2} & 1
\end{array}\right], \quad \hat{P}^{(1)}=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right], \quad \hat{P}^{(2)}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1
\end{array}\right], \quad \hat{P}^{(3)}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{array}\right]
$$

As a corollary of Proposition 4 we here determine the 'transition point' $\bar{p}(B)$ for the family $\hat{P}_{p}^{M: D}$ in the triangular scenario.

Lemma 4. For $p \in \mathbb{R}$ it is the case that $\left[\begin{array}{c}\frac{1}{2} & (1-p)^{2} \\ (1-p)^{2} & \frac{1}{2}\end{array}\right] \geq 0 \Leftrightarrow 1-\frac{1}{\sqrt{2}} \leq p \leq 1+\frac{1}{\sqrt{2}}$.
Lemma 5. Let $a, b, r \in \mathbb{C}$, then $\left[\begin{array}{ll}a & r \\ r & b\end{array}\right] \geq 0 \Leftrightarrow\left[\begin{array}{ll}b & r \\ r & a\end{array}\right] \geq 0$.
Corollary 1. For the family $\hat{P}_{p}^{3: D}$ in equation (55), and for feature maps with orthonormal components, the covariance matrix $\operatorname{Cov}(Y)$ has a semidefinite decomposition with respect to the triangular bipartite DAG B in figure 3, if and only if $1-\frac{1}{\sqrt{2}} \leq p \leq 1$. Hence, $\bar{p}(B)=1-1 / \sqrt{2}$.

One may note that $\hat{P}_{p}^{3: D}$ has a semidefinite decomposition also in the case $p=1-1 / \sqrt{2}$, i.e., at the transition point. Proposition 4 does strictly speaking leave open the nature of the transition point per se.

Proof. By Proposition 4 we know that it is sufficient to determine the $p$ for which $C(p)$ decomposes as in (54). Due to Lemma 4 it follows that

$$
\tilde{R}=0, \tilde{C}_{1}=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & \frac{1}{2} & (1-p)^{2} \\
0 & (1-p)^{2} & \frac{1}{2}
\end{array}\right], \tilde{C}_{2}=\left[\begin{array}{ccc}
\frac{1}{2} & 0 & (1-p)^{2} \\
0 & 0 & 0 \\
(1-p)^{2} & 0 & \frac{1}{2}
\end{array}\right], \tilde{C}_{3}=\left[\begin{array}{ccc}
\frac{1}{2} & (1-p)^{2} & 0 \\
(1-p)^{2} & \frac{1}{2} & 0 \\
0 & 0 & 0
\end{array}\right]
$$

satisfy the decomposition (54) for all $1-1 / \sqrt{2} \leq p \leq 1$. However, this does not exclude the possibility that there exists some other decomposition that yields a smaller $p$.

Suppose that $0 \leq p^{\prime}<1-1 / \sqrt{2}$. By the structure of the triangular DAG, it follows that the most general decomposition of the form (54) possible (incorporating the diagonal matrix $\tilde{R}$ into $\tilde{C}_{1}, \tilde{C}_{2}$, and $\tilde{C}_{3}$ ) can be written $C(p)=\tilde{C}_{1}+\tilde{C}_{2}+\tilde{C}_{3}$, where

$$
\tilde{C}_{1}=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & b_{2} & (1-p^{\prime})^{2} \\
0 & (1-p^{\prime})^{2} & c_{1}
\end{array}\right], \tilde{C}_{2}=\left[\begin{array}{ccc}
a_{1} & 0 & (1-p^{\prime})^{2} \\
0 & 0 & 0 \\
(1-p^{\prime})^{2} & 0 & c_{2}
\end{array}\right], \tilde{C}_{3}=\left[\begin{array}{ccc}
a_{2} & (1-p^{\prime})^{2} & 0 \\
0 & b_{1} & 0 \\
0 & 0 & 0
\end{array}\right]
$$

and where $a_{1}, a_{2}, b_{1}, b_{2}, c_{1}, c_{2} \geq 0$ and $a_{1}+a_{2}=1, b_{1}+b_{2}=1, c_{1}+c_{2}=1$. By the assumed semidefiniteness of $\tilde{C}_{1}$, $\tilde{C}_{2}$, and $\tilde{C}_{3}$, it follows that

$$
M_{1}:=\left[\begin{array}{cc}
a_{1} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & c_{2}
\end{array}\right] \geq 0, \quad M_{2}:=\left[\begin{array}{cc}
a_{2} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & b_{1}
\end{array}\right] \geq 0, \quad M_{3}:=\left[\begin{array}{cc}
b_{2} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & c_{1}
\end{array}\right] \geq 0
$$

By Lemma 5 it follows that (56) implies

$$
M_{4}:=\left[\begin{array}{cc}
c_{2} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & a_{1}
\end{array}\right] \geq 0, \quad M_{5}:=\left[\begin{array}{cc}
b_{1} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & a_{2}
\end{array}\right] \geq 0, \quad M_{6}:=\left[\begin{array}{cc}
c_{1} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & b_{2}
\end{array}\right] \geq 0
$$

Since these matrices all are positive semidefinite, it follows that every convex combinations of them is also positive semidefinite. Thus one can confirm that

$$
\left[\begin{array}{cc}
\frac{1}{2} & (1-p^{\prime})^{2} \\
(1-p^{\prime})^{2} & \frac{1}{2}
\end{array}\right]=\frac{1}{6} M_{1}+\frac{1}{6} M_{2}+\frac{1}{6} M_{3}+\frac{1}{6} M_{4}+\frac{1}{6} M_{5}+\frac{1}{6} M_{6} \geq 0
$$

However, the positive semidefiniteness of this matrix is a contradiction to Lemma 4, since by assumption $p^{\prime}<$ $1-1 / \sqrt{2}$. Hence, $C(p)$ can only have a decomposition as in (54) if $1-1 / \sqrt{2} \leq p \leq 1$. By Proposition 4 it thus follows that $\operatorname{Cov}(Y)$ satisfies the semidefinite decomposition as in (52) if and only if $1-1 / \sqrt{2} \leq p \leq 1$.

# X. COMPARISON WITH ENTROPIC TESTS 

Outer relaxations of the compatibility set corresponding to latent variable structures, based on information theoretic inequalities, have been considered previously [27-30]. Here we make a numerical comparison of the performance of these entropic tests and the semidefinite test. A basic challenge is that we in practice do not know the true set of compatible distributions. However, since we are dealing with outer approximations, a reasonable approach is to compare how 'strict' the tests are, i.e., if one test generally tends to reject more distributions than the other.

Given the rather radical difference in appearance and functional form between the semidefinite test and tests based on entropy inequalities (described in more detail in the next section) it is far from clear how these tests relate, or if there even is a clear-cut relation in the sense that one would be systematically stronger than the other. An indication can be gained from [47], where it was found that tests based on operator inequalities, of the type described in section VI, appear to be stronger than the entropic ones for small alphabet sizes, but that there seems to be a switchover for larger alphabets (see section 4.5 of [47]). Here we confirm similar trends for the semidefinite test in comparison with the entropic test, where we focus on the 'triangular' DAG described in figure 3. In case of binary variables, we do in section $X B$ make a comparison over an ensemble of randomly constructed distributions. However, our major testbed for these comparisons (in section $X C$ ) is the family of distributions $\beta_{p}^{M: D}$ introduced in section IX.

## A. Entropy inequalities for the triangular DAG

We focus on the triangular DAG in figure 3, since this has been a rather well investigated scenario with several known entropic inequalities associated with it. For the three observable variables $O_{1}, O_{2}, O_{3}$ we let $H(1):=$ $H\left(O_{1}\right):=-\sum_{j} P\left(O_{1}=j\right) \log _{2} P\left(O_{1}=j\right)$ denote the Shannon entropy, and in a similar manner $H(12):=H\left(O_{1}, O_{2}\right)$, etc, where ' $\log _{2}$ ' denotes the base 2 logarithm. The first inequality (58) for the triangular scenario was obtained in [6] (see also [27] and [30])

$$
E_{1}:=-H(1)-H(2)-H(3)+H(13)+H(12) \geq 0
$$

The following two inequalities were derived in [27]

$$
\begin{aligned}
& E_{2}:=-3 H(1)-3 H(2)-3 H(3)+2 H(12)+2 H(13)+3 H(23)-H(123) \geq 0 \\
& E_{3}:=-5 H(1)-5 H(2)-5 H(3)+4 H(12)+4 H(13)+4 H(23)-2 H(123) \geq 0
\end{aligned}
$$

Finally, inequalities (61) to (63) were obtained in [30]

$$
\begin{aligned}
& E_{4}:=-4 H(1)-4 H(2)-4 H(3)+3 H(12)+3 H(13)+4 H(23)-2 H(123) \geq 0 \\
& E_{5}:=-2 H(1)-2 H(2)-2 H(3)+3 H(12)+3 H(13)+3 H(23)-4 H(123) \geq 0 \\
& E_{6}:=-8 H(1)-8 H(2)-8 H(3)+7 H(12)+7 H(13)+7 H(23)-5 H(123) \geq 0
\end{aligned}
$$

One should observe that the expressions in (58), (59), and (61) are not symmetric under permutations of the $O_{1}, O_{2}, O_{3}$, and thus each of these generate two more inequalities. Whenever one of these inequalities is violated we can conclude that the observable distribution cannot originate from the bipartite DAG in figure 3.

One may note that all of these entropic inequalities, apart from (58), depend on the full tripartite distribution, while the semidefinite test only takes into account the mono- and bipartite marginals. One may thus intuitively suspect that the semidefinite test would be at a disadvantage compared to these tripartite entropic tests.

## B. Rejection rates in random Ising models: The binary case

For a numerical comparison between the entropic and the semidefinite test for the triangular scenario in figure 3, we assume binary variables $O_{1}, O_{2}, O_{3} \in\{-1,1\}$, and distributions $P(\bar{x}):=P\left(O_{1}=x_{1}, O_{2}=x_{2}, O_{3}=x_{3}\right)$,

$\bar{x}:=\left(x_{1}, x_{2}, x_{3}\right)$ given by an Ising interaction model [50, 51]

$$
P(\bar{x})=\frac{e^{-\bar{x}^{\dagger} J \bar{x}}}{Z}
$$

with $Z$ being the normalization constant, and where $J$ is a real $3 \times 3$ matrix. For each single instance of this model we draw the elements of $J$ independently from a Gaussian distribution with zero mean and variance 1.

For the semidefinite test we choose (universal) feature maps that associate the outcomes of the random variables to elements of orthonormal bases, thus resulting in a $6 \times 6$ covariance matrix. The semidefinite test was implemented via a semidefinite program that minimizes a constant function, thus effectively testing whether there exist any feasible elements.

For each instance over $10^{6}$ independent repetitions of the Ising model in (64) we performed the semidefinite test, as well as tested the entropic inequalities (58) to (63) together with all their permutations.

The following table gives the approximate fraction of rejections. In the table, $E_{1}^{\prime j}$ (and analogously for $E_{2}^{\prime j}$ and $E_{4}^{\prime j}$ ) means that we test the inequality in (58) as well as its two permutations, and we count the fraction of the sample that violates any of these three inequalities, i.e., we take the union of the corresponding rejection regions. The entry 'Combined' signifies the fraction of rejections due to violations of at least one of the inequalities (58) to (63) or any of their permutations. Finally 'Semidefinite' denotes the fraction of rejections for the semidefinite test.

$$
\begin{array}{lll}
E_{1}^{\prime j}: 0.57, & E_{2}^{\prime j}: 0.60, & E_{3}: 0.54 \\
E_{4}^{\prime j}: 0.63, & E_{5}: 0.40, & E_{6}: 0.60 \\
\text { Combined : } 0.64, & \\
\text { Semidefinite : } 0.77 &
\end{array}
$$

Since the fraction of rejections is higher for the semidefinite test than for all the entropic inequalities combined, this suggests that the semidefinite test in some sense has a 'larger' region of rejection, and thus would be the stronger test. To get some information on the relation between the two regions of rejections, we checked whether we could find any case where the semidefinite test accepted an instance that had been rejected by some of the entropic inequalities. However, we could find no such case, which suggests that the region of rejection for the collection of entropic inequalities is contained in the region of rejection for the semidefinite test.

# C. Comparison on a monotone family of distributions 

In section VIII we argued that the compatibility of distributions with respect to a given bipartite DAG is monotonous under local operations, and that the semidefinite test also satisfies this property if we use universal feature maps. In section IX C we introduced a particular tripartite family of distributions $\hat{P}_{p}^{3: D}$ that can be generated from the appropriate maximally correlated distribution by local operations, and where we could show that this family cut the boundary of the semidefinite compatibility region at $p=1-1 / \sqrt{2}$. Here we compare the performance of the entropic tests with the semidefinite test on this particular family of distributions.

## 1. Binary variables

We begin in the case of three binary variables, i.e., each variable can take two possible values. In this case $\hat{P}_{p}^{3: 2}$ reduces to

$$
\hat{P}_{p}^{3: 2}\left(\bar{x}_{1}, \bar{x}_{2}, \bar{x}_{3}\right)=\left\{\begin{array}{cc}
\frac{1}{8}\left(4-6 p+3 p^{2}\right), & \text { if } \quad \bar{x}_{1}=\bar{x}_{2}=\bar{x}_{2} \\
\frac{1}{8} p(2-p), & \text { otherwise. }
\end{array}\right.
$$

In figure 6 we plot $E_{1}, \ldots, E_{6}$ as functions of the parameter $p$. The entropic test rejects the model for a given $p$ whenever one of these functions become negative. For the calculation of the covariance matrix we choose feature maps that assign orthonormal vectors to the outcomes of the three random variables, thus being universal. As one can see from figure 6, the semidefinite test starts to reject at higher values of $p$ than all the entropic tests, and is thus closer to the true value $p^{*}$ of the transition than any of the entropic tests.

![img-5.jpeg](img-5.jpeg)

FIG. 6. Entropic versus semidefinite for binary variables. For three binary variables described by the distribution $\tilde{P}_{p}^{3: 2}$ in equation (65), we calculate $E_{1}, \ldots, E_{6}$ defined in (58) to (63) as functions of the parameter $p$. When one of these functions turns negative, it implies that the distribution $\tilde{P}_{p}^{3: 2}$ is not compatible with the triangular bipartite DAG in figure 3. Moreover, we determine the $6 \times 6$ covariance matrix with respect to feature maps that assign orthogonal vectors to the outcomes. The red vertical line indicates the value $p=1-1 / \sqrt{2} \approx 0.29$, determined in section IXC, below which the semidefinite test rejects the resulting covariance matrix. As one can see, the semidefinite test has the larger region of rejection, and is in this sense the stronger test for this particular binary setup.

# 2. Asymptotics of the $E_{1}$ test 

$E_{1}$ defined in (58) is the only of the entropic quantities (58) to (63) that solely includes mono- and bipartite marginals; the others also depend on the full tripartite distribution. Since the test based on $E_{1}$ and the semidefinite test thus are on 'equal footing' in this regard, it appears relevant to pay some additional attention to the relation between these two tests. In section IXC, and in particular in Corollary 1, we proved that the distribution $\tilde{P}_{p}^{3: D}$, defined in equation (55), satisfies the semidefinite test if and only if $p \geq 1-1 / \sqrt{2}$, irrespective of the alphabet size $D$. Hence, the 'transition point' for the semidefinite test is independent of $D$ for this particular family of distributions. Here we shall show that the corresponding transition point for the test based on $E_{1}$ lies below $1-1 / \sqrt{2}$, but asymptotically approaches this value as $D$ increases.

The family of distributions $\tilde{P}_{p}^{3: D}$ in (55) is permutation symmetric with respect to the three parties, and $E_{1}$ can, via equation (47), be evaluated as

$$
\begin{aligned}
E_{1}= & -3 H(1)+2 H(12) \\
= & -3 \log D \\
& -2\left(1-\frac{1}{D}\right) p(2-p) \log \left[p(2-p) \frac{1}{D^{2}}\right] \\
& -2\left[(1-p)^{2}+p(2-p) \frac{1}{D}\right] \log \left[(1-p)^{2} \frac{1}{D}+p(2-p) \frac{1}{D^{2}}\right]
\end{aligned}
$$

One can confirm that $E_{1}(0)=-\log D, E_{1}(1)=\log D$, and

$$
\frac{d E_{1}}{d p}=4\left(1-\frac{1}{D}\right)(1-p) \log \left[1+D \frac{(1-p)^{2}}{p(2-p)}\right]
$$

which is non-negative for $0 \leq p \leq 1$. Hence, for each fixed $D$, the function $E_{1}$ is monotonically increasing for $0 \leq p \leq 1$, and thus the equation $E_{1}(p)=0$ has exactly one root, which is situated somewhere in the open interval $(0,1)$. Thus, analogous to the semidefinite test, the test based on $E_{1}$ will reject all elements in the family $\tilde{P}_{p}^{3: D}$ below a certain transition point, and accept all distributions above that value. Next one can confirm that

$$
E_{1}\left(1-\frac{1}{\sqrt{2}}\right)=\log \frac{2 D}{D+1}+\frac{1}{D} \log \frac{2^{D}}{D+1}>0, \quad D=2,3, \ldots
$$

Since $E_{1}$ thus is monotonously increasing with respect to $p$, we can conclude that the root $\tilde{p}$ of $E_{1}(\tilde{p})=0$ is such that $\tilde{p}<1-1 / \sqrt{2}$ for all $D \geq 2$. Finally we wish to the determine the asymptotic value of the root $\tilde{p}$ as $D \rightarrow \infty$.

To this end we rewrite (66) such that we highlight the different orders of dependency on $D$,

$$
\begin{aligned}
E_{1}= & 2\left[1+\frac{1}{\sqrt{2}}-p\right]\left[p-\left(1-\frac{1}{\sqrt{2}}\right)\right] \log D \\
& -2 p(2-p) \log [p(2-p)]-4(1-p)^{2} \log (1-p) \\
& -2 p(2-p) \frac{1}{D} \log D \\
& -2(1-p)^{2} \log \left[1+\frac{p(2-p)}{(1-p)^{2}} \frac{1}{D}\right] \\
& +2 p(2-p) \frac{1}{D} \log \left[\frac{p(2-p)}{(1-p)^{2}}\right] \\
& -2 p(2-p) \frac{1}{D} \log \left[1+\frac{p(2-p)}{(1-p)^{2}} \frac{1}{D}\right]
\end{aligned}
$$

On any interval $\delta \leq p \leq 1-\delta$, with $1 / 2>\delta>0$, the last four lines of (68) each approaches zero as $D \rightarrow \infty$. Moreover, one can note that the leading order term (in the first line) does for each fixed $D$ increase monotonically for $0 \leq p \leq 1$ and switches from negative to positive at $p=1-1 / \sqrt{2}$. If one fixes $\epsilon>0$, one can realize that for all sufficiently large $D$, it is the case that $E_{1}(p)>0$ for all $1-1 / \sqrt{2}+\epsilon \leq p \leq 1-\delta$, and $E_{1}(p) \leq 0$ for all $0 \leq p \leq 1-1 / \sqrt{2}-\epsilon$. We can thus conclude that the root $\tilde{p}$ of $E_{1}(\tilde{p})=0$ in the interval $0 \leq \tilde{p} \leq 1$ approaches $1-1 / \sqrt{2}$ as $D \rightarrow \infty$.
3. Comparison on increasing alphabets
![img-6.jpeg](img-6.jpeg)

FIG. 7. Entropic versus semidefinite tests for increasing alphabet sizes. For the distribution $\tilde{P}_{p}^{3: D}$ in (55) we compare the entropic and semidefinite test as functions of $D$. Here we determine the smallest value of $p$ for which the respective test accepts $\tilde{P}_{p}^{3: D}$, as a function of the local alphabet size $D$. From section IXC we know that the transition point for the semidefinite test is $p=1-1 / \sqrt{2} \approx 0.29$, independently of $D$ (the red dashed line). We also plot (blue squares) the minimal value of $p$ for which all of the entropic inequalities (58) to (63) are satisfied, as a function of $D$. The transition point for this entropic test crosses the red line at $D=32$. Hence, for the class of functions $\tilde{P}_{p}^{3: D}$, the entropic tests becomes stronger than the semidefinite test for alphabet sizes beyond 32. Finally, we plot (green circles) the minimal value of $p$ for which $E_{1}(p) \geq 0$, as a function of $D$. By section $\mathrm{XC}_{2}$ we know that this transition point asymptotically reaches $1-1 / \sqrt{2}$.

In the previous section we found that the semidefinite test is stronger than the entropic one, for testing membership of distributions of the form $\tilde{P}_{p}^{3: 2}$. Here, we investigate how these two classes of tests compare when the size $D$ of the local alphabets increases. We know from section IXC that the semidefinite test is independent of $D$ for this particular family of distributions. It could thus potentially be the case that the entropic test would become stronger than the semidefinite test for sufficiently large alphabet sizes. This is indeed what we find in the numerical evaluation of the entropic test, which we display in figure 7.

As pointed out in section X C 2, all the entropic inequalities, apart from $E_{1}$, depend on the full tripartite distribution, while $E_{1}$ and the semidefinite test only utilize the bi- and mono-partite margins. We already know from the previous section that the test based on $E_{1}$ always is weaker that the semidefinite test for the family $\tilde{P}_{p}^{3: D}$, but that it approaches the semidefinite test in the limit of large alphabet sizes $D$. As suggested by the plot in figure 7 , the convergence is very slow. As an additional indication one may note that for an alphabet size of $D=10^{7}$ the root of the equation $E_{1}(p)=0$ is $p \approx 0.26$ while the limit is $p \approx 0.29$.

# XI. SUMMARY AND OUTLOOK 

In this work we have considered the constraints imposed by a large class of causal structures on the covariance matrix of the observed variables. More specifically, we have shown that each bipartite DAG induces a decomposition that every covariance matrix resulting from the corresponding causal model has to satisfy. Such decompositions can be formulated in terms of semidefinite programs that allow for a straightforward and efficient computational treatment of the problem (as opposed to algebraic geometry solutions). A violation of the condition imposed by the bipartite DAG under test (or in other terms, the non-feasibility of the semidefinite program) thus implies that the observed covariance matrix is not compatible with it. We have also shown that every decomposition associated with a bipartite DAG can be realized by a causal model on that graph.

Furthermore, we have made comparisons between the performance of the semidefinite test and tests based on information theoretic inequalities formulated in terms of entropies, where the results indicate that the semidefinite test outperforms the entropic test for moderate alphabet sizes of the random variables, while the latter become more powerful for large alphabet sizes.

These results open several directions for future research. Here, we have restricted attention to characterising the set of covariance matrices compatible with a given causal structure. In real-world situations however, the covariance matrix is unknown and has to be estimated from a limited number of samples drawn from the underlying distribution. This raises the question of how to turn the theory developed here into statistical hypothesis tests for a presumed causal stucture. An obvious idea would be to construct a confidence region for the estimated covariance matrix and reject the hypothesis if the confidence region does not intersect the set compatible with the causal assumption. We speculate, though, that it might be simpler to obtain statistically sound results by employing convex duality, as explained in the context of figure 4. Indeed, assume that $X$ is such that all compatible covariance matrices have non-negative inner product with $X$. The inner product betweeen $X$ and the true covariance matrix is a scalar linear function of the distribution of the observable variables. A one-sided statistical hypothesis test for $\operatorname{tr}(X \operatorname{Cov}(Y)) \leq 0$ with any desired significance level is therefore easy to construct. It will automatically also test the causal hypothesis at the same significance level. While any $X$ gives rise to such a test, their power to identify a given true incompatible distribution may very wildly. One way of making an informed choice for $X$ would be as follows: Split the samples into two parts. If the empirical covariance matrix of the first part is compatible with the hypothesis, accept. If not, the dual SDP (26) will identify a witness $X^{*}$ that seperates the empirical matrix from the compatible set. Now use the test based on $X^{*}$ with the second part of the samples. We leave the details to future work.

Another immediate question is to better understand the relation between the semidefinite and the entropic tests. Similarly, it would be highly desirable to combine our results with other tools that have very recently been proposed in order to characterize complex DAGs [23-25]. On a more general level it is noteworthy that by restricting to covariance we turn a highly non-linear problem into what essentially is a convex optimization. Understanding how far this can be pushed (considering higher order moments, for instance) would certainly give us new geometric insights on the nature of this problem. Since we here have focused on a setting where all correlations of observed variables are due to latent variables, it is very reasonable to ask if tests based on covariances can be extended to more general types of DAGs that do not have this bipartite structure.

From a more fundamental perspective our work may have implications for the current research program on the foundations of quantum physics. Bayesian networks have attracted growing attention as means to understand the role of causality in quantum mechanical systems [5-13]. One may thus ask whether the methods we have employed here can be generalized to the case of quantum causal structures, where for example some nodes in the graph represent quantum states without a classical analogue. Any positive results along this line would certainly be highly relevant in the context of quantum causal modeling and once more highlight the very fruitful interplay between the fields of causal inference and foundational aspects of quantum mechanics.

# ACKNOWLEDGMENTS 

We thank Thomas Kahle and Johannes Textor for productive discussions during the early stages of this project.
This work has been supported by the Excellence Initiative of the German Federal and State Governments (Grants ZUK 43 and 81), the ARO under contract W911NF-14-1-0098 (Quantum Characterization, Verification, and Validation), and the DFG (SPP1798 CoSIP).
[1] J. Pearl, Causality (Cambridge University Press, Cambridge, 2009).
[2] P. Spirtes, N. Glymour, and R. Scheienes, Causation, Prediction, and Search, 2nd ed. (The MIT Press, 2001).
[3] Nir Friedman, "Inferring cellular networks using probabilistic graphical models," Science 303, 799-805 (2004).
[4] G. Ver Steeg and A. Galstyan, "A sequence of relaxations constraining hidden variable models," in Proceedings of the 27th conference on Uncertainty in Artificial Intelligence (2011).
[5] M. S. Leifer and Robert W. Spekkens, "Towards a formulation of quantum theory as a causally neutral theory of bayesian inference," Phys. Rev. A 88, 052130 (2013).
[6] T. Fritz, "Beyond bell's theorem: correlation scenarios," New J. Phys. 14, 103001 (2012).
[7] Tobias Fritz, "Beyond bell's theorem ii: Scenarios with arbitrary causal structure," Communications in Mathematical Physics 341, 391-434 (2016).
[8] Joe Henson, Raymond Lal, and Matthew F Pusey, "Theory-independent limits on correlations from generalized bayesian networks," New J. Phys. 16, 113043 (2014).
[9] Rafael Chaves, Christian Majenz, and David Gross, "Information-theoretic implications of quantum causal structures," Nat. Commun. 6, 5766 (2015).
[10] Jacques Pienaar and Caslav Brukner, "A graph-separation theorem for quantum causal models," New J. Phys. 17, 073020 (2015).
[11] Katja Ried, Megan Agnew, Lydia Vermeyden, Dominik Janzing, Robert W Spekkens, and Kevin J Resch, "A quantum advantage for inferring causal structure," Nature Physics 11, 414-420 (2015).
[12] Fabio Costa and Sally Shrapnel, "Quantum causal modelling," New Journal of Physics 18, 063032 (2016).
[13] Dominic Horsman, Chris Heunen, Matthew F Pusey, Jonathan Barrett, and Robert W Spekkens, "Can a quantum state over time resemble a quantum state at a single time?" arXiv preprint arXiv:1607.03637 (2016).
[14] Itamar Pitowsky, "Correlation polytopes: Their geometry and complexity," Mathematical Programming 50, 395-414 (1991).
[15] J. Pearl, "On the testability of causal models with latent and instrumental variables," in Proceedings of the 11th conference on Uncertainty in Artificial Intelligence (1995) pp. 435-443.
[16] D. Geiger and C. Meek, "Quantifier elimination for statistical problems," in Proceedings of the 15th conference on Uncertainty in Artificial Intelligence (1999) pp. 226-235.
[17] B. Bonet, "Instrumentality tests revisited," in Proceedings of the 17th Conference on Uncertainty in Artificial Intelligence (2001) pp. $48-55$.
[18] L. D. Garcia, M. Stillman, and B. Sturmfels, "Algebraic geometry of bayesian networks," Journal of Symbolic Computation 39, 331-355 (2005).
[19] C. Kang and J. Tian, "Inequality constraints in causal models with hidden variables," in Proceedings of the 22nd Conference on Uncertainty in Artificial Intelligence (2006) pp. 233-240.
[20] C. Kang and J. Tian, "Polynomial constraints in causal bayesian networks," in Proceedings of the 23rd Conference on Uncertainty in Artificial Intelligence (2007) pp. 200-208.
[21] Robin J Evans, "Graphical methods for inequality constraints in marginalized dags," in 2012 IEEE International Workshop on Machine Learning for Signal Processing (IEEE, 2012) pp. 1-6.
[22] Ciarán M Lee and Robert W Spekkens, "Causal inference via algebraic geometry: necessary and sufficient conditions for the feasibility of discrete causal models," arXiv preprint arXiv:1506.0388o (2015).
[23] Rafael Chaves, "Polynomial bell inequalities," Phys. Rev. Lett. 116, 010402 (2016).
[24] Denis Rosset, Cyril Branciard, Tomer Jack Barnea, Gilles Pütz, Nicolas Brunner, and Nicolas Gisin, "Nonlinear bell inequalities tailored for quantum networks," Phys. Rev. Lett. 116, 010403 (2016).
[25] Elle Wolfe, Robert W Spekkens, and Tobias Fritz, "The inflation technique for causal inference with latent variables," arXiv preprint arXiv:1609.00672 (2016).
[26] Philipp Moritz, Jörg Reichardt, and Nihat Ay, "Discriminating between causal structures in bayesian networks given partial observations," Kybernetika 50 (2014).
[27] Rafael Chaves, Lukas Luft, and David Gross, "Causal structures from entropic information: geometry and novel scenarios," New Journal of Physics 16, 043001 (2014).
[28] R. Chaves, L. Luft, T. O. Maciel, D. Gross, D. Janzing, and B. Schölkopf, "Inferring latent structures via information inequalities," Proceedings of the 3oth Conference on Uncertainty in Artificial Intelligence , 112-121 (2014).
[29] Bastian Steudel and Nihat Ay, "Information-theoretic inference of common ancestors," Entropy 17, 2304-2327 (2015).

[30] Mirjam Weilenmann and Roger Colbeck, "Non-shannon inequalities in the entropy vector approach to causal structures," arXiv preprint arXiv:1605.02078 (2016).
[31] Samuel L. Braunstein and Carlton M. Caves, "Information-theoretic bell inequalities," Phys. Rev. Lett. 61, 662-665 (1988).
[32] N. J. Cerf and C. Adami, "Entropic bell inequalities," Phys. Rev. A 55, 3371-3374 (1997).
[33] Rafael Chaves and Tobias Fritz, "Entropic approach to local realism and noncontextuality," Phys. Rev. A 85, 032113 (2012).
[34] T. Fritz and R. Chaves, "Entropic inequalities and marginal problems," IEEE Trans. Inform. Theory 59, 803 (2013).
[35] Rafael Chaves, "Entropic inequalities as a necessary and sufficient condition to noncontextuality and locality," Phys. Rev. A 87, 022102 (2013).
[36] Rafael Chaves, Jonatan Bohr Brask, and Nicolas Brunner, "Device-independent tests of entropy," Phys. Rev. Lett. 115, 110501 (2015).
[37] Rafael Chaves and Costantino Budroni, "Entropic nonsignaling correlations," Phys. Rev. Lett. 116, 240501 (2016).
[38] Robin J Evans, "Graphs for margins of bayesian networks," Scandinavian Journal of Statistics 3, 625-648 (2016).
[39] C. Branciard, N. Gisin, and S. Pironio, "Characterizing the nonlocal correlations created via entanglement swapping," Phys. Rev. Lett. 104, 170401 (2010).
[40] Cyril Branciard, Denis Rosset, Nicolas Gisin, and Stefano Pironio, "Bilocal versus nonbilocal correlations in entanglementswapping experiments," Phys. Rev. A 85, 032119 (2012).
[41] Armin Tavakoli, Paul Skrzypczyk, Daniel Cavalcanti, and Antonio Acín, "Nonlocal correlations in the star-network configuration," Physical Review A 90, 062109 (2014).
[42] Christopher J Wood and Robert W Spekkens, "The lesson of causal discovery algorithms for quantum correlations: causal explanations of bell-inequality violations require fine-tuning," New J. Phys. 17, 033002 (2015).
[43] J. S. Bell, "On the Einstein-Podolsky-Rosen paradox," Physics 1, 195 (1964).
[44] Dylan J Saunders, Adam J Bennet, Cyril Branciard, and Geoff J Pryde, "Experimental demonstration of non-bilocal quantum correlations," arXiv preprint arXiv:1610.08514 (2016).
[45] Gonzalo Carvacho, Francesco Andreoli, Luca Santodonato, Marco Bentivegna, Rafael Chaves, and Fabio Sciarrino, "Experimental non-locality in a quantum network," arXiv preprint arXiv:1610.03327 (2016).
[46] Lieven Vandenberghe and Stephen Boyd, "Semidefinite programming," SIAM review 38, 49-95 (1996).
[47] Kai von Prillwitz, Statistical aspects of inferring Bayesian networks from marginal observations, Master's thesis, Fakultät für Mathematik und Physik der Albert-Ludwigs-Universität Freiburg (2015).
[48] Thomas M Cover and Joy A Thomas, Elements of information theory (John Wiley \& Sons, 2012).
[49] B. Schölkopf and A. J. Smola, Learning with Kernels (MIT Press, 2002).
[50] G. Gallavotti, Statistical mechanics (Springer, 1999).
[51] D. Koller and N. Friedman, Probabilistic Graphical Models (MIT Press, 2009).