# A review of Gaussian Markov models for conditional independence 

Irene Córdoba*, Concha Bielza, Pedro Larrañaga<br>Universidad Politécnica de Madrid, Madrid, Spain


#### Abstract

Markov models lie at the interface between statistical independence in a probability distribution and graph separation properties. We review model selection and estimation in directed and undirected Markov models with Gaussian parametrization, emphasizing the main similarities and differences. These two model classes are similar but not equivalent, although they share a common intersection. We present the existing results from a historical perspective, taking into account the amount of literature existing from both the artificial intelligence and statistics research communities, where these models were originated. We cover classical topics such as maximum likelihood estimation and model selection via hypothesis testing, but also more modern approaches like regularization and Bayesian methods. We also discuss how the Markov models reviewed fit in the rich hierarchy of other, higher level Markov model classes. Finally, we close the paper overviewing relaxations of the Gaussian assumption and pointing out the main areas of application where these Markov models are nowadays used.


Keywords: Gaussian Markov model, Conditional independence, Model selection, Parameter estimation

## 1. Introduction

Markov models, or probabilistic graphical models, explicitly establish a correspondence between statistical independence in a probability distribution and certain separation criteria holding in a graph. They were originated at the interface between statistics, where Markov random fields were predominant (Darroch et al., 1980), and artificial intelligence, with a focus on Bayesian networks (Pearl, 1985, 1986). These two model classes are now considered the traditional ones, but still are widely applied and nowadays there is a significant amount of research devoted to them (Daly et al., 2011; Uhler, 2012). They both share the modelling of conditional independences: Bayesian networks relate them with acyclic directed graphs, whereas in Markov fields they are associated with undirected graphs. However, the models they represent are only equivalent under additional assumptions on the respective graphs.

[^0]
[^0]:    *Corresponding author
    Email addresses: irene.cordoba@upm.es (Irene Córdoba), mcbielza@fi.upm.es (Concha Bielza), pedro.larranaga@fi.upm.es (Pedro Larrañaga)
    Preprint submitted to Elsevier
    October 3, 2019

In this paper, we review the existing methods for model selection and estimation in undirected and acyclic directed Markov models with a Gaussian parametrization. The multivariate Gaussian distribution is among the most widely developed and applied statistical family in this context (Werhli et al., 2006; Ibáñez et al., 2016), and allows for an explicit parametric comparison of their similarities and differences. The highly interdisciplinary nature of these Markov model classes has led to a wide range of terminology in methodological developments and theoretical results. They have usually been studied separately, with some exceptions (Wermuth, 1980; Pearl, 1988), and most unifying works (Sadeghi and Lauritzen, 2014; Wermuth, 2015) are characterized by a high-level view, where the models are embedded in other, more expressive classes, and the focus is on the properties of these container classes. By contrast, in this paper we review them from a low-level perspective. In doing so, we use a unified notation that allows for a direct comparison between the two types of classes. Furthermore, throughout each section we explicitly compare them, in terms of both methodological and theoretical developments.

The paper is structured as follows. A historical introduction to Markov models is presented in Section 2, emphasizing the different research areas that contributed to their birth. Afterwards, preliminary concepts from graph theory are presented in Section 3. In Section 4, undirected and acyclic directed Markov model classes are introduced, under no distributional assumptions. This is because many foundational relationships between them can already be established from this general perspective. Next, we restrict their parametrization to multivariate Gaussian distributions, and explore the main derived properties from this in Section 5. We review maximum likelihood estimation in Section 6. These estimates are used for model selection via hypothesis testing, as we present in Section 7. When maximum likelihood estimators are not guaranteed to exist, a popular technique is to employ regularization, which we overview in Section 8. Finally, the alternative Bayesian approach for model selection and estimation is treated in Section 9. We explore the relationship of Gaussian acyclic directed and undirected Markov models with other, higher level model classes in Section 10. Alternatives to the Gaussian distribution are discussed in Section 11. We close the paper discussing the main real applications of the Gaussian Markov model classes reviewed in Section 12.

# 2. A historical perspective 

We will now introduce the main terminology for Gaussian Markov models that can be found nowadays, from a historical perspective. In Figure 1 we have depicted a timeline on the origins of Markov models, containing most of the key works we will refer to in this section.

Undirected Markov models for conditional independence are the oldest type of Markov models, preceded only by special cases such as the Ising model for ferromagnetic materials (Kindermann and Snell, 1980; Isham, 1981). In fact, they are a generalization of the Ising model, which is at the same time a generalization of Markov chains. Originally, undirected Markov models were called Markov random fields (Grimmett, 1973), since they generalized the correspondence between Gibbs measures (Besag, 1974) and Markov properties. The terminology graphical model was not introduced until Darroch et al. (1980) linked the graphical ideas for contingency tables with Markov properties of discrete Markov fields. Furthermore, we also find them called Markov networks (Pearl,

![img-0.jpeg](img-0.jpeg)

Figure 1: Timeline on the origins of Gaussian Markov models. Papers from the statistical community appear at the top, while papers from other research areas appear below. Thematically, gray filled squares are papers about acyclic directed Markov models, the white ones are about the undirected case, and those gradient filled treat both classes.

1988), from researchers in artificial intelligence, as a parallel to the terminology *Bayesian networks*, used for acyclic directed Markov fields.

Regarding the Gaussian parametrization, we can find that one of the first works to impose some structure on the covariance matrix of a multivariate Gaussian distribution, in order to reduce the number of parameters to be estimated, was Anderson (1973). He considered the mean vector and covariance matrix to be linear combinations of known linearly independent vectors and matrices, respectively. Closely following this work was Dempster (1972), who suggested to estimate the inverse of the covariance matrix (concentration matrix) by assuming certain entries equal to zero, motivated by the representation of the multivariate Gaussian distribution as an exponential family. His work was later referred to as *covariance selection* models. Interestingly, although Dempster did not have any graphical interpretation in mind, such zero entries in the concentration matrix are directly associated with missing edges in an undirected Gaussian Markov models, and these correspondence was analysed some years later in Wermuth (1976a). This is why, even nowadays, these Markov models with a Gaussian parameterization are sometimes called covariance selection models.

Acyclic digraphs, in contrast, were intensely used as models for multivariate probability distributions after the definition of *influence diagrams*. These are used to model decision-making processes, and were introduced by Howard and Matheson in 1981 (article reprinted in Howard and Matheson (2005)). Their probabilistic reduction coincides with acyclic directed Markov models, and was subsequently extensively studied by Pearl (Pearl, 1988), who renamed probabilistic influence diagrams as *Bayesian networks* or *influence networks* (Pearl, 1985). Some researchers working on Markov fields also developed theory regarding these directed counterparts, calling them *directed Markov fields* (Lauritzen et al., 1990).

Earlier works than the previously outlined, employing or referencing acyclic directed Markov models, are available. Wermuth (1980) implicitly studied them in the Gaus-

sian case as linear recursive regression systems, although the main focus was rather on covariance selection models. In fact, we can trace the use of directed graphs as graphical models for dependencies among random variables at least to the work of geneticist Sewall Wright in 1918, who developed the method of path coefficients (Wright, 1934), nowadays known as path analysis. Linearly related variables were represented using a directed acyclic graph, whereas their correlation was represented by bi-directed edges joining them.

# 3. Graph preliminaries 

A graph is defined as a pair $\mathcal{G}=(V, E)$ where $V$ is the vertex set and $E$ is the edge set. Throughout all the paper, and unless otherwise stated, the graphs will be labelled and simple, which means that the elements in $V$ are labelled, for example, as $1, \ldots, p$; and $E$ is formed by pairs of distinct elements in $V$. A graph is called undirected if these latter pairs are unordered $\left(E \subseteq\{\{u, v\}: u, v \in V\}\right)$, and directed or digraph otherwise $\left(E \subseteq\{(u, v): u, v \in V\}\right)$. Edges $\{u, v\}$ in an undirected graph are usually denoted as $u v$ and graphically represented as a line (see Figure 2a); while in a digraph they are called arcs or directed edges and represented as arrows (Figure 2b and 2c).
![img-1.jpeg](img-1.jpeg)

Figure 2: Examples of an undirected graph and two digraphs.

### 3.1. Undirected graphs

In an undirected graph $\mathcal{G}=(V, E)$, if $u v \in E, u$ and $v$ are called neighbours. For $v \in$ $V$, the set of its neighbours is denoted as $\operatorname{ne}(v)$, and the closure of $v$ is $\operatorname{cl}(v):=\{v\} \cup \operatorname{ne}(v)$. $\mathcal{G}$ is called complete if for every $u, v \in V, u v \in E$. A maximal $C \subseteq V$ such that $\mathcal{G}_{C}$ is complete is called a clique. Let $\mathcal{H}=\left(V_{\mathcal{H}}, E_{\mathcal{H}}\right)$ be another undirected graph. $\mathcal{H}$ is a subgraph of $\mathcal{G}$ (written as $\mathcal{H} \subseteq \mathcal{G}$ ) if $V_{\mathcal{H}} \subseteq V$ and $E_{\mathcal{H}} \subseteq E$. If $E_{\mathcal{H}}=\left\{u v \in E: u, v \in V_{\mathcal{H}}\right\}$, then $\mathcal{H}$ is called the induced sub-graph and denoted $\mathcal{G}_{V_{\mathcal{H}}}$.

A walk between $u$ and $v$ is an ordered sequence of vertices $(u=) u_{0}, u_{1}, \ldots, u_{k-1}, u_{k}(=$ $v)$ where $u_{i-1} u_{i} \in E$ for $i \in\{1, \ldots, k\}$. The number $k$ is called the length of the walk. If $u=v$ the walk is closed, and when $u_{0}, \ldots, u_{k-1}$ are distinct, the walk is called a path. A closed path of length $k \geq 3$ is called a cycle or $k$-cycle. $\mathcal{G}$ is called chordal or triangulated if all minimal $k$-cycles are of length $k=3$. A chordal cover of a graph $\mathcal{G}$ is a graph $\mathcal{G}^{*}$ such that $\mathcal{G} \subseteq \mathcal{G}^{*}$ and $\mathcal{G}^{*}$ is chordal.
$S \subseteq V$ separates $u$ and $v$ in $\mathcal{G}=(V, E)$ if there is no path between $u$ and $v$ in the sub-graph $\mathcal{G}_{V \backslash S}$. If we consider $A, B, S \subseteq V, A$ and $B$ are said to be separated by $S$ if $u$ and $v$ are separated by $S$ for all $u \in A, v \in B$. Let $V$ be partitioned into

disjoint sets $A, B, S \subseteq V . \quad(A, B, S)$ is called a decomposition of $\mathcal{G}$ if $S$ separates $A$ and $B$ in $\mathcal{G}$ and $\mathcal{G}_{S}$ is complete. If $A \neq \emptyset$ and $B \neq \emptyset$ the decomposition is said to be proper. An undirected graph is decomposable if (i) it is complete or (ii) it admits a proper decomposition into decomposable sub-graphs. An undirected graph is decomposable if and only if it is chordal.

# 3.2. Acyclic digraphs 

In a digraph $\mathcal{D}=(V, A)$ the definitions of (induced) sub-graph, walk, path, and cycle are analogous to the undirected case. The undirected graph $\mathcal{D}^{U}:=\left(V, A^{U}\right)$ with $A^{U}:=\{u v:(u, v) \in A\}$ is called the skeleton of $\mathcal{D}$, and $\mathcal{D}$ is one of its orientations. A digraph $\mathcal{D}$ is said to be complete when $\mathcal{D}^{U}$ is complete.

In the following, assume that $\mathcal{D}$ is acyclic (see Figure 2b for a cyclic digraph, and Figure 2c for an acyclic one). The parent set of $v \in V$ is $\mathrm{pa}(v):=\{u \in V:(u, v) \in A\}$; conversely, the child set is $\operatorname{ch}(v):=\{u \in V:(v, u) \in A\}$. The ancestors of $v, \operatorname{an}(v)$, are those $u \in V$ such that there exists a directed path from $u$ to $v$; the descendants of $v, \operatorname{de}(v)$, are those $u \in V$ such that there exists a directed path from $v$ to $u$. We will let $\operatorname{nd}(v):=V \backslash(\{v\} \cup \operatorname{de}(v))$ be the set of non-descendants of $v \in V$, and $\operatorname{An}(A):=$ $A \cup\left(\cup_{a \in A} \operatorname{an}(a)\right)$ the ancestral set of $A \subseteq V$. Note that a total order $\prec$ can be defined over the set of vertices $V$ in an acyclic digraph $\mathcal{D}=(V, A)$, such that if $(u, v) \in A$, then $u \prec v$. This ordering is usually called ancestral, and it is a linear extension of the partial order naturally defined as $u \preceq v$ if $u \in \operatorname{an}(v)$. For $v \in V$, the set of successors of $v$ with respect to $\prec$ is $\operatorname{su}(v)=\{u \in V: u \succ v\}$; the set of predecessors of $v$ is $\operatorname{pr}(v)=\{u \in V: u \prec v\}$.

Finally, let $u, w_{1}, w_{2} \in V$ with $\left(w_{1}, u\right),\left(w_{2}, u\right) \in A$ and $\left(w_{1}, w_{2}\right),\left(w_{2}, w_{1}\right) \notin A$ (see vertices 1, 2 and 3 in Figure 2c). Such configurations are usually called $v$-structures and denoted as $w_{1} \rightarrow u \leftarrow w_{2}$. The moral graph of $\mathcal{D}$ is defined as the undirected graph $\mathcal{D}^{m}=\left(V, A^{m}\right)$ with $A^{m}:=A^{U} \cup\left\{w_{1} w_{2}: w_{1} \rightarrow u \leftarrow w_{2}\right.$ for some $\left.u \in V\right\}$.

## 4. Undirected and acyclic directed Markov model classes

The Markov model classes we will review associate conditional independences in random vectors $\boldsymbol{X}=\left(X_{1}, \ldots, X_{p}\right)^{t}$ with undirected graph and acyclic digraph separation properties. This is made explicit via the Markov properties of the distribution of $\boldsymbol{X}$, which are in turn based on what are known as independence relations.

In the following, for arbitrary $I \subseteq\{1, \ldots, p\}$, we will denote the $|I|$-dimensional subvector of $\boldsymbol{X}$ as $\boldsymbol{X}_{I}:=\left(X_{i}\right)_{i \in I}$. Conditional independence will be expressed as in Dawid (1979): $\boldsymbol{X}_{I} \Perp \boldsymbol{X}_{J} \mid \boldsymbol{X}_{K}$ represents the statement ' $\boldsymbol{X}_{I}$ is conditionally independent from $\boldsymbol{X}_{J}$ given $\boldsymbol{X}_{K}$ ' (see, e.g. Studený, 2018, §1.3).

### 4.1. Independence relations

An independence relation over a set $V=\{1, \ldots, p\}$ is a collection $\mathcal{I}$ of triples $(A, B, C)$ where $A, B$ and $C$ are pairwise disjoint subsets of $V$. It is called a semi-graphoid when the following conditions are met,

$$
\begin{aligned}
& \text { if }(A, B, C) \in \mathcal{I} \text { then }(B, A, C) \in \mathcal{I} \\
& \text { if }(A, B \cup C, D) \in \mathcal{I} \text { then }(A, C, D) \in \mathcal{I} \text { and }(A, B, C \cup D) \in \mathcal{I} \\
& \text { if }(A, B, C \cup D) \in \mathcal{I} \text { and }(A, C, D) \in \mathcal{I} \text { then }(A, B \cup C, D) \in \mathcal{I}
\end{aligned}
$$

and a graphoid when it additionally satisfies that if $(A, B, C \cup D) \in \mathcal{I}$ and $(A, C, B \cup D) \in$ $\mathcal{I}$ then $(A, B \cup C, D) \in \mathcal{I}$ (Pearl and Paz, 1987).

Independence relations arise in different contexts relevant for Markov models. Specifically, an independence relation $\mathcal{I}$ over $V=\{1, \ldots, p\}$ is said to be induced by

- an undirected graph $\mathcal{G}=(V, E)$ if $(A, B, S) \in \mathcal{I} \Longleftrightarrow A$ and $B$ are separated by $S$ in $\mathcal{G}$,
- an acyclic digraph $\mathcal{D}=(V, A)$ if $(A, B, S) \in \mathcal{I} \Longleftrightarrow A$ and $B$ are separated by $S$ in $\left(\mathcal{D}_{\mathrm{An}(A \cup B \cup S)}\right)^{m}$,
- a $p$-dimensional random vector $\boldsymbol{X}$ if $(A, B, S) \in \mathcal{I} \Longleftrightarrow \boldsymbol{X}_{A} \Perp \boldsymbol{X}_{B} \mid \boldsymbol{X}_{S}$.

Graph-induced independence relations are always graphoids, while probabilistic ones are always semi-graphoids and require additional assumptions on the probability spaces involved to be graphoids (Dawid, 1980). See Studený (2018) $\S 1.5$ and $\S 1.11$ for a detailed exposition of graphoid theory and how to compute and represent their closures, that is, all the triplets that can be derived from a given independence relation by using the graphoid axioms.

The core of Markov model classes is the relationship between induced independence relations, which we will denote as $\mathcal{I}(\cdot)$ with the argument being the inducing element. Specifically, if $\mathcal{G}$ is an undirected (acyclic directed) graph, an undirected (directed) Markov model is defined as

$$
\boldsymbol{\mathcal { M }}(\mathcal{G}):=\left\{P_{\boldsymbol{X}}: \mathcal{I}(\mathcal{G}) \subseteq \mathcal{I}(\boldsymbol{X})\right\}
$$

where the random vectors $\boldsymbol{X}$ are defined over the same probability space and $P_{\boldsymbol{X}}$ denotes their distribution. These classes are non-empty (Geiger and Pearl, 1990, 1993); that is, for any undirected or acyclic directed graph, we can always find a probability distribution whose independence model contains the one generated by the graph.

Graphoids can be generalised to what are known as separoids (Dawid, 2001), which are algebraic structures usually appearing whenever a notion of 'irrelevance' is being mathematically treated (see, e.g. Studený, 2018, §1.1.3). Further research on these axiom systems from an abstract point of view could shed more light on how the apparently different mathematical contexts in which such structures arise are related, and also provide an explicit bridge between them and the recently defined independence logic (Grädel and Väänänen, 2013), closely related.

# 4.2. Markov properties 

When a distribution $P_{\boldsymbol{X}}$ belongs to $\boldsymbol{\mathcal { M }}(\mathcal{G})$ for an undirected or acyclic directed graph $\mathcal{G}$, it is said that $P_{\boldsymbol{X}}$ is globally $\mathcal{G}$-Markov or satisfies the global Markov property with respect to $\mathcal{G}$. There are other weaker Markov properties that usually allow to simplify the model. Specifically, if $\mathcal{G}=(V, E)$ is an undirected graph, then the probability distribution $P_{\boldsymbol{X}}$ of $\boldsymbol{X}$ is said to be

- pairwise $\mathcal{G}$-Markov if $X_{u} \Perp X_{v} \mid \boldsymbol{X}_{V \backslash\{u, v\}}$ for all $u v \notin E$,
- locally $\mathcal{G}$-Markov if $X_{v} \Perp \boldsymbol{X}_{V \backslash \mathrm{cl}(v)} \mid \boldsymbol{X}_{\mathrm{ne}(v)}$ for all $v \in V$;
whereas if $\mathcal{G}$ is an acyclic digraph, then $P_{\boldsymbol{X}}$ is called

- pairwise $\mathcal{G}$-Markov if $X_{u} \Perp X_{v} \mid \boldsymbol{X}_{\operatorname{nd}(u) \backslash\{v\}}$ for all $u \in V, v \in \operatorname{nd}(u) \backslash \operatorname{pa}(u)$;
- locally $\mathcal{G}$-Markov if $X_{v} \Perp \boldsymbol{X}_{\operatorname{nd}(v) \backslash \operatorname{pa}(v)} \mid \boldsymbol{X}_{\operatorname{pa}(v)}$ for all $v \in V$.

The three Markov properties are equivalent when $\mathcal{G}$ is acyclic directed (Lauritzen et al., 1990), while if $\mathcal{G}$ is undirected this equivalence is only guaranteed when $\mathcal{I}(\boldsymbol{X})$ is a graphoid (Pearl, 1988). A sufficient condition for this to happen is that $P_{\boldsymbol{X}}$ admits a continuous and strictly positive density. This result was proved in different forms by several authors, but it is usually attributed to Hammersley and Clifford (1971), who were the first to outline the proof for the discrete case (Speed, 1979). It relies on an additional characterization of a probability distribution with respect to $\mathcal{G}$ : denoting as $\mathfrak{C}(\mathcal{G})$ the class of cliques of $\mathcal{G}$, the density function $f$ of $P_{\boldsymbol{X}}$ is said to factorize according to $\mathcal{G}$ when there exists a set $\left\{\psi_{C}\left(\boldsymbol{x}_{C}\right): C \in \mathfrak{C}(\mathcal{G}), \psi_{C} \geq 0\right\}$ such that

$$
f(\boldsymbol{x})=\prod_{C \in \mathfrak{C}(\mathcal{G})} \psi_{C}\left(\boldsymbol{x}_{C}\right)
$$

When (1) holds, then $P_{\boldsymbol{X}}$ is globally $\mathcal{G}$-Markov, while if $f$ is continuous and strictly positive, the pairwise Markov property implies (1), which gives the equivalence of Markov properties. Positivity is a straightforward sufficient condition for checking whether an independence model originated from a distribution is a graphoid. Necessary and sufficient conditions are given in measure theoretic terms by Dawid (1980), and recently by Peters (2014) in terms of special functions over the sample space.

Finally, recall that the nodes of an acyclic digraph $\mathcal{D}=(V, A)$ can be totally ordered such that if $(u, v) \in A$, then $u \in \operatorname{pr}(v)$. This gives rise to another Markov property, exclusive for acyclic digraphs: $P_{\boldsymbol{X}}$ is said to be ordered $\mathcal{D}$-Markov if $X_{v} \Perp \boldsymbol{X}_{\operatorname{pr}(v) \backslash \operatorname{pa}(v)} \mid$ $\boldsymbol{X}_{\operatorname{pa}(v)}$ for all $v \in V$. This property is also equivalent to the global, local and pairwise Markov properties (Lauritzen et al., 1990). The classical theory of undirected and acyclic directed Markov properties can be found in Lauritzen (1996), whereas Studený (2018) $\S 1.7$ and $\S 1.8$ provides a recent overview.

# 4.3. Independence and Markov equivalence 

When the Markov models defined by two graphs $\mathcal{G}$ and $\tilde{\mathcal{G}}$, with the same vertex set $V$, coincide, such graphs are said to be Markov equivalent. A simpler notion, which implies Markov equivalence, is independence equivalence, holding when $\mathcal{I}(\mathcal{G})=\mathcal{I}(\tilde{\mathcal{G}})$. Independence equivalence is implied by Markov equivalence under fairly general circumstances (Studený, 2005, §6.1), which is why most authors treat them as the same notion. These equivalences allow to choose the most suited graph for the Markov model.

We will first characterize equivalence within undirected graphs. For each graphoid $\mathcal{I}$ over $V$ there exists a unique edge-minimal undirected graph $\mathcal{G}$ such that $\mathcal{I}(\mathcal{G}) \subseteq \mathcal{I}$ (Pearl and Paz, 1987). It follows that $\mathcal{I}(\mathcal{G})=\mathcal{I}(\tilde{\mathcal{G}})$ (independence equivalence) if and only if $\mathcal{G}$ and $\tilde{\mathcal{G}}$ are identical. Furthermore, if we assume that $\mathcal{I}(\boldsymbol{X})$ is a graphoid for all $P_{\boldsymbol{X}} \in \mathcal{M}(\mathcal{G})$, then a unique edge-minimal $\tilde{\mathcal{G}}$ exists, with $\tilde{\mathcal{G}} \subseteq \mathcal{G}$, such that $\boldsymbol{M}(\mathcal{G})=\mathcal{M}(\tilde{\mathcal{G}})$ (Markov equivalence); that is, a unique undirected graph can be chosen as representative of each undirected Markov model.

In contrast, acyclic digraphs are not, in general, unique representations of a Markov model, since $\mathcal{I}(\mathcal{D})=\mathcal{I}(\tilde{\mathcal{D}})$ if and only if $\mathcal{D}$ and $\tilde{\mathcal{D}}$ have the same skeleton and the same v-structures (Verma and Pearl, 1991). However, unique representatives can be

constructed: let $\mathfrak{D}_{p}$ be the set of acyclic digraphs over $V=\{1, \ldots, p\}$ and define an equivalence relation $\sim$ in $\mathfrak{D}_{p}$ as $\mathcal{D} \sim \tilde{\mathcal{D}} \Longleftrightarrow \mathcal{I}(\mathcal{D})=\mathcal{I}(\tilde{\mathcal{D}})$. The quotient space of $\sim$ is $\mathfrak{D}_{p} / \sim=\left\{[\mathcal{D}]: \mathcal{D} \in \mathfrak{D}_{p}\right\}$, where $[\mathcal{D}] \models\left\{\tilde{\mathcal{D}} \in \mathfrak{D}_{p}: \tilde{\mathcal{D}} \sim \mathcal{D}\right\}$ is the Markov equivalence class; indeed, $\boldsymbol{\mathcal { M }}(\tilde{\mathcal{D}})=\boldsymbol{\mathcal { M }}(\mathcal{D})$ for all $\tilde{\mathcal{D}} \in[\mathcal{D}]$, that is, $[\mathcal{D}]$ is the unique representative of the directed Markov model.

The asymptotic ratio $l=\lim _{p \rightarrow \infty}\left|\mathfrak{D}_{p}\right| /\left|\mathfrak{D}_{p} / \sim\right|$ influences the computational gain obtained by using $\mathfrak{D}_{p} / \sim$ instead of $\mathfrak{D}_{p}$ as a search space for model selection. Steinsky (2004) analytically calculates an upper bound of $l$ as 13.65. Exact computations by Gillispie and Perlman (2002), for $p \leq 10$, and approximations by Sonntag et al. (2015), up to $p=31$, seem to indicate that $l \sim 3.7$. However, its analytical deduction remains an open problem. Note that the computational gain is not only influenced by $l$, but also by other factors, such as how the element size in $\mathfrak{D}_{p} / \sim$ is distributed. An algorithm to compute such sizes can be found in He et al. (2015). Recently, Radhakrishnan et al. (2018) have provided tight lower and upper bounds on the number and size of Markov equivalence classes when $\mathcal{D}$ is a tree.

Finally, we will characterize equivalence between directed and undirected graphs, firstly obtained by Wermuth (1980) for multivariate Gaussian distributions, Wermuth and Lauritzen (1983) for contingency tables, and generalized in Frydenberg (1990) for graphoid-inducing distributions. When $\mathcal{G}$ is an undirected graph, $\boldsymbol{\mathcal { M }}(\mathcal{G})=\boldsymbol{\mathcal { M }}(\mathcal{D})$ for some acyclic digraph $\mathcal{D}$ if and only if $\mathcal{G}$ is chordal. Conversely, an acyclic digraph $\mathcal{D}$ is Markov equivalent to its skeleton $\mathcal{D}^{U}$ if and only if $\mathcal{D}$ contains no v-structures. Furthermore, a relation with the moral graph can be established, which requires an analogous to (1): a density function $f$ is said to recursively factorize according to $\mathcal{D}$ when

$$
f(\boldsymbol{x})=\prod_{v \in V} f\left(x_{v} \mid \boldsymbol{x}_{\mathrm{pa}(v)}\right)
$$

This characterization is equivalent to the Markov properties, and also implies that $f$ factorizes as in (1) with respect to the moral graph $\mathcal{D}^{m}$ (Lauritzen et al., 1990). This means that $P_{\boldsymbol{X}}$ is always globally $\mathcal{D}^{m}$-Markov for continuous $\boldsymbol{X}$, and thus $\boldsymbol{\mathcal { M }}(\mathcal{D}) \subseteq$ $\boldsymbol{\mathcal { M }}\left(\mathcal{D}^{m}\right)$, with the equality only holding when $\mathcal{D}^{m}=\mathcal{D}^{U}$.

Example 1. An illustration of the previous concepts can be found in Figure 3. The graph in 3 a is not chordal, and thus there is no Markov equivalent acyclic digraph. 3 b is a chordal cover of 3a, and a Markov equivalent orientation is depicted in 3c. The acyclic digraph in 3 d has v-structures, emphasized in dark grey, and thus cannot be Markov equivalent to its skeleton (3a). The moral graph of 3 d is 3 e , which in fact is another chordal cover of 3 a , and thus none of its orientations will be Markov equivalent to 3 c .

# 5. Gaussian parametrization 

When restricting to multivariate Gaussian distributions, we find connections between conditional and vanishing parameters. This correspondence can be used for providing a direct interpretation of Markov properties, both in the undirected and directed case, allowing an enhanced manipulation of these Markov models.

In the following, the elements of a real $q \times r$ matrix $\mathbf{M} \in \mathbb{M}_{q \times r}(\mathbb{R})$ will be denoted as $m_{i j}$, where $i \in\{1, \ldots, q\}$ and $j \in\{1, \ldots, r\} . \mathbf{M}_{I J}$ will be the $|I| \times|J|$ sub-matrix

![img-2.jpeg](img-2.jpeg)

Figure 3: Markov equivalence.
of $\mathbf{M}$, where $I \subseteq\{1, \ldots, q\}$ and $J \subseteq\{1, \ldots, r\}$; and we will use $\mathbf{M}_{I J}^{-1}$ as $\left(\mathbf{M}_{I J}\right)^{-1} . \mathbb{S}^{>0}$ and $\mathbb{S}^{\succeq 0}$ will represent the sets of positive and semi-positive definite symmetric matrices, respectively. The $p$-variate Gaussian distributions is denoted as $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\boldsymbol{\mu} \in \mathbb{R}^{p}$ is the mean vector and $\boldsymbol{\Sigma} \in \mathbb{S}^{>0}$ is the covariance matrix. $\mathbf{I}_{p}$ will denote the identity $p$-dimensional square matrix, whereas $\mathbf{1}_{p}$ will denote the $p$-vector with all entries equal to 1 ; many times, dimensionality sub-scripts will be dropped if the dimension of the respective object is clear from the context.

# 5.1. Conditional independence and the multivariate Gaussian distribution 

Let $V=\{1, \ldots, p\}$. When a random vector $\boldsymbol{X}$ is distributed as $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then for $i, j \in V, X_{i} \Perp X_{j}$ is equivalent to $\sigma_{i j}=0$. If we consider a partition $(I, J)$ of $V$, then $\boldsymbol{X}_{I} \mid \boldsymbol{x}_{J}$ is distributed as $\mathcal{N}_{\mid I \mid}\left(\boldsymbol{\mu}_{I}, \boldsymbol{\Sigma}_{I \cdot J}\right)$, where $\boldsymbol{\Sigma}_{I \cdot J}=\boldsymbol{\Sigma}_{I I}-\boldsymbol{\Sigma}_{I J} \boldsymbol{\Sigma}_{J J}^{-1} \boldsymbol{\Sigma}_{J I}$ (Anderson, 2003). Thus, for $i, k \in I$, we have that $X_{i} \Perp X_{k} \mid \boldsymbol{x}_{J}$ is equivalent to $\sigma_{i k \cdot J}=0$, the $(i, k)$ element in the conditional covariance matrix $\boldsymbol{\Sigma}_{I \cdot J}$.

A correspondence can be established between the zeros in $\boldsymbol{\Sigma}_{I \cdot J}$ and zero patterns in other representative matrices (Wermuth, 1976a, 1980; Uhler, 2018, §9.1), as follows. Let the concentration matrix of $\boldsymbol{X}$ be $\boldsymbol{\Omega}=\boldsymbol{\Sigma}^{-1}$, with elements $\omega_{u v}$ for $u, v \in V$. The matrix $\boldsymbol{\Sigma}_{I J} \boldsymbol{\Sigma}_{J J}^{-1}$ is usually denoted as $\mathbf{B}_{I \cdot J}$ and called the matrix of regression coefficients of $\boldsymbol{X}_{I}$ on $\boldsymbol{X}_{J}$. Letting $\boldsymbol{\Omega}_{I \cdot J}:=\boldsymbol{\Sigma}_{J J}^{-1}$, we have the following matrix identity (Horn and Johnson, 2012)

$$
\boldsymbol{\Omega}=\left(\begin{array}{ll}
\boldsymbol{\Sigma}_{I I} & \boldsymbol{\Sigma}_{I J} \\
\boldsymbol{\Sigma}_{J I} & \boldsymbol{\Sigma}_{J J}
\end{array}\right)^{-1}=\left(\begin{array}{cc}
\boldsymbol{\Sigma}_{I \cdot J}^{-1} & -\boldsymbol{\Sigma}_{I \cdot J}^{-1} \mathbf{B}_{I \cdot J} \\
-\mathbf{B}_{I \cdot J}^{\mathrm{t}} \boldsymbol{\Sigma}_{I \cdot J}^{-1} & \boldsymbol{\Omega}_{I \cdot J}+\mathbf{B}_{I \cdot J}^{\mathrm{t}} \boldsymbol{\Sigma}_{I \cdot J}^{-1} \mathbf{B}_{I \cdot J}
\end{array}\right)
$$

This allows us to relate $\boldsymbol{\Sigma}_{I \cdot J}$ with $\boldsymbol{\Omega}$ and $\mathbf{B}_{I \cdot J}$ as

$$
\begin{aligned}
& \boldsymbol{\Sigma}_{I \cdot J}=\boldsymbol{\Omega}_{I I}^{-1} \\
& \mathbf{B}_{I \cdot J}=-\boldsymbol{\Omega}_{I I}^{-1} \boldsymbol{\Omega}_{I J}
\end{aligned}
$$

which implies that, dually, $\boldsymbol{\Omega}_{I I}$ is identically equal to the concentration matrix of $\boldsymbol{X}_{I} \mid \boldsymbol{x}_{J}$, while $\boldsymbol{\Omega}_{I \cdot J}$ is the concentration matrix of $\boldsymbol{X}_{J}$. Finally, from (2) we get, for $i, k \in V$,

$$
X_{i} \Perp X_{j} \mid \boldsymbol{X}_{V \backslash\{i, k\}} \Longleftrightarrow \omega_{i k}=0
$$

whereas from (3) it follows that, for $J \subseteq V, i, k \in V \backslash J$,

$$
X_{i} \Perp X_{k} \mid \boldsymbol{X}_{J} \Longleftrightarrow \beta_{i k \cdot J \cup\{k\}}=0
$$

where $\beta_{i k \cdot J \cup\{k\}}$ is the $v$ entry in the vector $\boldsymbol{\beta}_{i \cdot J \cup\{k\}}^{t}$, that is, the coefficient of $X_{k}$ on the regression of $X_{i}$ on $\boldsymbol{x}_{J \cup\{k\}}$. The original notation for this, introduced in Yule (1907), was $\beta_{i k \cdot J}$; that is, $k$ is implicitly considered as included in the conditioning indexes. We have however chosen the alternative, explicit notation $\beta_{i k \cdot J \cup\{k\}}$, since it provides more notational simplicity in later sections.

# 5.2. Gaussian Markov models 

In the Gaussian case, undirected Markov models are in correspondence with the concentration matrix, while for acyclic digraphs this correspondence is with the regression coefficients. Both rely on the auxiliary Markov properties that we presented in Section 4.2 .

Let $\mathcal{G}=(V, E)$ be an undirected graph and consider $\boldsymbol{X}$ distributed as $P_{\boldsymbol{X}} \equiv \mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $P_{\boldsymbol{X}} \in \mathcal{M}(\mathcal{G})$. Since $P_{\boldsymbol{X}}$ is globally $\mathcal{G}$-Markov, it is also pairwise $\mathcal{G}$-Markov, and thus (4) directly gives that $\omega_{u v}=0$ for all $u, v \in V$ such that $u v \in E$. This means that, if we define the set $\mathbb{S}^{>0}(\mathcal{G}):=\left\{\mathbf{M} \in \mathbb{S}^{>0}: m_{u v}=0\right.$ for all $\left.u v \notin E\right\}$, we have $\boldsymbol{\Omega} \in \mathbb{S}^{>0}(\mathcal{G})$ if and only if $P_{\boldsymbol{X}}$ is pairwise $\mathcal{G}$-Markov. Furthermore, since the multivariate Gaussian distribution has positive density, $\mathcal{I}(\boldsymbol{X})$ is a graphoid and thus the three Markov properties are equivalent. This allows us to redefine the Gaussian undirected Markov model as

$$
\mathcal{N}(\mathcal{G})=\left\{\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma}): \boldsymbol{\Sigma}^{-1} \in \mathbb{S}^{>0}(\mathcal{G}), \boldsymbol{\mu} \in \mathbb{R}^{p}\right\}
$$

In the directed case, the redefinition is not so direct. Let $\mathcal{D}=(V, A)$ be an acyclic digraph, and assume, for notational simplicity, that the nodes are already ancestrally ordered as $1 \preceq \cdots \preceq p$. If $\boldsymbol{X}$ is distributed as $P_{\boldsymbol{X}} \equiv \mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $P_{\boldsymbol{X}} \in \mathcal{M}(\mathcal{D})$, it satisfies the ordered Markov property. Thus, whenever $v \in \operatorname{pr}(u) \backslash \mathrm{pa}(u)$, we have $X_{u} \Perp$ $X_{v} \mid \boldsymbol{X}_{\mathrm{pa}(u)}$, which is equivalent to $\beta_{u v \cdot \mathrm{pa}(u) \cup\{v\}}=0$ as in (5). Since we have assumed an ancestral order, $\beta_{u v \cdot \mathrm{pa}(u) \cup\{v\}}=\beta_{u v \cdot \mathrm{pr}(u)}$ for all $u \in V, v \in \operatorname{pr}(u) \backslash \mathrm{pa}(u)$, which leads to $P_{\boldsymbol{X}}$ being ordered $\mathcal{D}$-Markov if and only if $\beta_{u v \cdot \operatorname{pr}(u)}=0$ for all $u \in V, v \in \operatorname{pr}(u) \backslash \mathrm{pa}(u)$. Such triangular requirement on the regression coefficients can be expressed with the matrix $\mathbf{B}$ defined, for $v<u$ as $b_{u v}=0$ if $v \notin \mathrm{pa}(u)$, and $b_{u v}=\beta_{u v \cdot \mathrm{pa}(u)} \equiv \beta_{u v \cdot \operatorname{pr}(u)}$ otherwise.

If we let $v_{u}:=\sigma_{u u \cdot \operatorname{pr}(u)}$, the previous characterization leads to a matrix form of the linear regressions involved as

$$
\boldsymbol{X}=\boldsymbol{\mu}+\mathbf{B}(\boldsymbol{X}-\boldsymbol{\mu})+\boldsymbol{E}
$$

where $E_{u} \sim \mathcal{N}\left(0, v_{u}\right)$. We can rearrange it as $\boldsymbol{X}=\mathbf{U}^{-1} \boldsymbol{\xi}+\mathbf{U}^{-1} \boldsymbol{E}$, where $\boldsymbol{\xi}:=\mathbf{U} \boldsymbol{\mu}$ and $\mathbf{U}:=\mathbf{I}_{p}-\mathbf{B}$, since $\mathbf{U}$ is invertible. Let $\mathbf{V}$ be the diagonal matrix of conditional variances $\boldsymbol{v}$. Sometimes $\boldsymbol{\xi}, \mathbf{B}$ and $\mathbf{V}$ are called the $\mathcal{D}$-parameters of $(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ (Andersson and Perlman, 1998). In fact, $\mathbf{U}$ and $\mathbf{V}$ allow a decomposition of $\boldsymbol{\Sigma}$ (and $\boldsymbol{\Sigma}^{-1}$ ) as $\boldsymbol{\Sigma}=\mathbf{U}^{-1} \mathbf{V U}^{-t}$. Furthermore, this decomposition uniquely determines $\boldsymbol{\Sigma}$ via $\mathbf{U} / \mathbf{B}$ and $\mathbf{V}$ (Horn and Johnson, 2012). Thus, in analogy with (6), if we define the set

$$
\mathbb{M}(\mathcal{D}):=\left\{\mathbf{M} \in \mathbb{M}_{p \times p}(\mathbb{R}): m_{u v}=0 \text { for all }(u, v) \notin A\right\}
$$

and the set $\boldsymbol{\Delta}_{p}$ of $p \times p$ diagonal matrices, we can redefine the Gaussian directed Markov model as

$$
\mathcal{N}(\mathcal{D})=\left\{\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma}): \boldsymbol{\Sigma}^{-1}=\left(\mathbf{I}_{p}-\mathbf{B}\right)^{t} \mathbf{V}^{-1}\left(\mathbf{I}_{p}-\mathbf{B}\right), \mathbf{B} \in \mathbb{M}(\mathcal{D}), \mathbf{V} \in \boldsymbol{\Delta}_{p}\right\}
$$

# 6. Maximum likelihood estimation 

Maximum likelihood estimation is greatly simplified in exponential family theory (Barndorff-Nielsen, 1978). The multivariate Gaussian distribution is a regular exponential family, and thus both undirected and directed Gaussian Markov models can be expressed as special subfamilies of it.

### 6.1. The Gaussian family and maximum likelihood

In the multivariate Gaussian family the canonical parameter is $\boldsymbol{\eta}=(\boldsymbol{\Omega} \boldsymbol{\mu},-\boldsymbol{\Omega} / 2)$, over the space $\mathcal{H}=\left\{\left(\boldsymbol{\eta}_{1}, \boldsymbol{\eta}_{2}\right): \boldsymbol{\eta}_{1} \in \mathbb{R}^{p},-\boldsymbol{\eta}_{2} \in \mathbb{S}^{>0}\right\}$ and the sufficient statistics are $\boldsymbol{t}(\boldsymbol{X})=\left(\boldsymbol{X}, \boldsymbol{X} \boldsymbol{X}^{t}\right)$. Let $\left\{\boldsymbol{x}^{(n)}: 1 \leq n \leq N\right\}$ be $N$ independent observations, where $\boldsymbol{X}^{(n)} \sim \mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ for each $n \in\{1, \ldots, N\}$, arranged in $\mathbf{x} \in \mathbb{M}_{p \times N}(\mathbb{R})$, the respective random matrix being $\mathbf{X}$. The random sample is also a regular exponential family with canonical parameter $\boldsymbol{\eta}=(\boldsymbol{\Omega} \boldsymbol{\mu},-\boldsymbol{\Omega} / 2)$ over the space $\mathcal{H}$. The sufficient statistics in this case are $\boldsymbol{t}(\mathbf{X})=\left(N \overline{\mathbf{X}}, \mathbf{X X}^{t}\right)$ with $N \overline{\mathbf{X}}=\sum_{n=1}^{N} \boldsymbol{X}^{(n)}$.

In a regular exponential family $\mathcal{F}_{\mathcal{H}}$, a maximum of the likelihood function, $\mathcal{L}(\boldsymbol{\eta})$, given a random sample $\mathbf{X}=\mathbf{x}$, is reached in $\mathcal{H}$ if and only if $\boldsymbol{t}(\mathbf{x})$ belongs to the interior of $\mathcal{C}(\boldsymbol{t})$, the closed convex hull of the support of the distribution of $\boldsymbol{t}$, denoted as $\operatorname{int}(\mathcal{C}(\boldsymbol{t}))$. In such case, it is unique and given by the $\boldsymbol{\eta} \in \mathcal{H}$ satisfying $\mathbb{E}[\boldsymbol{t}(\mathbf{X})]=\boldsymbol{t}(\mathbf{x})$.

For the multivariate Gaussian random sample, we have that $\mathbb{E}[N \overline{\mathbf{X}}]=N \boldsymbol{\mu}$ and $\mathbb{E}\left[\mathbf{X X}^{t}\right]=N \boldsymbol{\Sigma}+N \boldsymbol{\mu} \boldsymbol{\mu}^{t}$, thus the convex support of $\boldsymbol{t}(\mathbf{X})=\left(N \overline{\mathbf{X}}, \mathbf{X X}^{t}\right)$ is $\mathcal{C}(\boldsymbol{t})=$ $\left\{(\boldsymbol{v}, \mathbf{M}) \in \mathbb{R}^{p} \times \mathbb{S}_{p}: \mathbf{M}-\boldsymbol{v} \boldsymbol{v}^{t} / N \in \mathbb{S}^{\succeq 0}\right\}$. This gives that the maximum likelihood estimator for $(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ exists if and only if $\mathbf{x x}^{t}-N \overline{\mathbf{x}} \overline{\mathbf{x}}^{t} \in \mathbb{S}^{>0}$, which happens with probability one whenever $N>p$ and never otherwise. The solution in such case is $(\overline{\mathbf{x}}, \mathbf{Q} / N)$, where

$$
\mathbf{Q}=\sum_{n=1}^{N}\left(\boldsymbol{X}^{(n)}-\overline{\mathbf{X}}\right)\left(\boldsymbol{X}^{(n)}-\overline{\mathbf{X}}\right)^{t}=\mathbf{X X}^{t}-N \overline{\mathbf{X}} \overline{\mathbf{X}}^{t}
$$

A particular situation, usually assumed, is when $\boldsymbol{\mu}=\mathbf{0}$. The canonical parameter now is $\boldsymbol{\eta}=-\boldsymbol{\Omega} / 2$ in the space $\left\{\boldsymbol{\eta}:-\boldsymbol{\eta} \in \mathbb{S}^{>0}\right\}$, and the sufficient statistic is $\boldsymbol{t}(\mathbf{X})=\mathbf{X X}^{t}$. The maximum likelihood estimator exists if and only if $\mathbf{x x}^{t} \in \mathbb{S}^{>0}$, and in such case it is $\mathbf{X X}^{t} / N=\mathbf{Q} / N$

### 6.2. Gaussian Markov models as exponential families

When $\mathcal{G}$ is an undirected graph, the set $\mathbb{S}^{>0}(\mathcal{G})$ is a convex (linear) cone inside the positive definite cone $\mathbb{S}^{>0}$ (e.g. Uhler, 2018, §9.2), which means that $\mathbb{R}^{p} \times \mathbb{S}^{>0}(\mathcal{G})$ is an affine subspace of $\mathbb{R}^{p} \times \mathbb{S}^{>0}$, and thus $\mathcal{N}(\mathcal{G})$ is also a regular exponential family (Barndorff-Nielsen, 1978). Assume that $\boldsymbol{\mu}=\mathbf{0}$ and let $\mathbf{Q}^{\mathcal{G}}$ be the projection of $\mathbf{Q}$ on $E \cup\{u u: u \in V\}$, that is, such that $q_{u v}^{\mathcal{G}}=0$ for all $u v \notin E$ with $u \neq v$. Since $\mathcal{L}(\boldsymbol{\Omega}) \propto \operatorname{det}(\boldsymbol{\Omega})^{\frac{1}{2}} \exp (-\operatorname{tr}(\boldsymbol{\Omega} \mathbf{Q}))$ and $\boldsymbol{\Omega} \in \mathbb{S}^{>0}(\mathcal{G})$, we have $\operatorname{tr}(\boldsymbol{\Omega} \mathbf{Q})=\operatorname{tr}\left(\boldsymbol{\Omega} \mathbf{Q}^{\mathcal{G}}\right)$ and the sufficient statistic for $\mathcal{N}(\mathcal{G})$ is $\boldsymbol{t}(\mathbf{x})=\mathbf{Q}^{\mathcal{G}}$ (Lauritzen, 1996). Its convex support is $\mathcal{C}(\boldsymbol{t})=\left\{\mathbf{P}^{\mathcal{G}}: \mathbf{P} \in \mathbb{S}^{\succeq 0}\right\}$, equivalently called the set of projections extendible to full positive definite matrices. Thus, the maximum likelihood estimator for $\boldsymbol{\Sigma}$ exists if and only if $\mathbf{Q}^{\mathcal{G}} \in \operatorname{int}(\mathcal{C}(\boldsymbol{t}))$, which is equivalent to say that $\mathbf{Q}^{\mathcal{G}}$ is extendible to a full positive definite matrix. Whenever it exists, it is the only extendible matrix $\tilde{\boldsymbol{\Sigma}}$ that also satisfies the model restriction $\tilde{\boldsymbol{\Sigma}}^{-1} \in \mathbb{S}^{>0}(\mathcal{G})$. A sufficient condition thus is that $\mathbf{Q} \in \mathbb{S}^{>0}$, which

happens almost surely for $N \geq p$. Recovering $\widetilde{\boldsymbol{\Sigma}}$ is a convex optimization problem, Uhler (2018) $\S 9.6$ overviews some of the algorithms available for its computation. Note however that if $\mathcal{G}$ is chordal, then there is a closed form expression for $\widetilde{\boldsymbol{\Omega}}$ (Lauritzen, 1996)

The existence of $\widetilde{\boldsymbol{\Sigma}}$ has been completely characterized when $\mathcal{G}$ is chordal by Grone et al. (1984) and Frydenberg and Lauritzen (1989), independently. Since finding $\widetilde{\boldsymbol{\Sigma}}$ is equivalent to a positive definite matrix completion problem (Uhler, 2018, §9.3), the problem lies at the interface between statistics and linear algebra. Therefore, this problem has been solved from an algebraic (Sturmfels and Uhler, 2010; Uhler, 2012, 2018, §9.4) viewpoint for a general, non-chordal $\mathcal{G}$. However, the conditions on the sample size $N$ are still unknown except for certain non-chordal graph types, see Uhler (2018) $\S 9.5$ for an up-to-date overview of the advances made so far.

Now we turn on the case where the random sample $\mathbf{X}$ is assumed to a follow multivariate Gaussian distribution constrained by the separation properties in an acyclic digraph. The restriction in (8), however, is not linear in the canonical parameter; in fact, Spirtes et al. (1997) show that they are curved exponential families. To obtain the maximum likelihood estimates, theory from multivariate linear regression can be applied (Andersson and Perlman, 1998). Recall that if $\boldsymbol{X} \sim \mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \in \boldsymbol{\mathcal { N }}(\mathcal{D})$, then $\boldsymbol{X}$ can be expressed as (7). Thus, we can estimate the $\mathcal{D}$-parameters for $(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ as the usual least squares estimators,

$$
\begin{aligned}
& \widehat{\boldsymbol{\beta}}_{u \cdot \mathrm{pa}(u)}^{t}=\mathbf{Q}_{u \mathrm{pa}(u)} \mathbf{Q}_{\mathrm{pa}(u) \mathrm{pa}(u)^{-1}} \\
& \widehat{\xi}_{u}=\bar{x}_{u}-\widehat{\boldsymbol{\beta}}_{u \cdot \mathrm{pa}(u)}^{t} \overline{\mathbf{x}}_{\mathrm{pa}(u)} \\
& N \widehat{v}_{u u}=q_{u u}-\widehat{\boldsymbol{\beta}}_{u \cdot \mathrm{pa}(u)}^{t} \mathbf{Q}_{u \mathrm{pa}(u)}^{t}
\end{aligned}
$$

respectively for each $u \in V$, where $q_{u u}$ is the $u$-th diagonal entry in $\mathbf{Q}$. We can then obtain directly the maximum likelihood estimator for $(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ from their respective $\mathcal{D}$ parameter estimators (see Andersson and Perlman, 1998, for an algorithm). As opposed to the undirected case, $(\widehat{\boldsymbol{\mu}}, \widetilde{\boldsymbol{\Sigma}})$ exist with probability one if and only if $N \geq$ $p+\max \{|\mathrm{pa}(u)|: u \in V\}$ (Anderson, 2003). Recently, Ben-David and Rajaratnam (2012) analyze in detail the relationship between the $\mathcal{D}$-parameters and $\boldsymbol{\Sigma}$ as a positive definite matrix completion problem, in analogy with the undirected case.

# 7. Model selection via hypothesis testing 

Maximum likelihood estimators, presented in the previous section, can be used to address the problem of model estimation, and require either prior knowledge or a statistical procedure that allows model selection; that is, selecting the graph that will define the Markov model. In this section we will review the main hypothesis testing methods for such task.

Throughout the section, for $u, v \in V=\{1, \ldots, p\}$ and $U \subseteq V \backslash\{u, v\}$, we will denote as $\rho_{u v \cdot U}$ the partial correlation coefficient between $u$ and $v$ given the variables in $U$, and as $r_{u v \cdot U}$ its maximum likelihood estimator, the sample partial correlation (see e.g. Anderson, 2003, $\S 4.3$ for an introduction to partial correlation theory).

### 7.1. Stepwise selection

In the undirected case, we are interested in testing the hypothesis $H_{0}: \boldsymbol{\Omega} \in \mathbb{S}^{>0}\left(\mathcal{G}_{0}\right)$ against $H_{1}: \boldsymbol{\Omega} \in \mathbb{S}^{>0}(\mathcal{G})$, where $\mathcal{G}_{0}=\left(V, E_{\mathcal{G}_{0}}\right) \subseteq \mathcal{G}=\left(V, E_{\mathcal{G}}\right)$. The result of such test

determines whether the edges in $E_{\mathcal{G}} \backslash E_{\mathcal{G}_{0}}$ should be excluded from the selected model; that is why these tests are usually known as edge exclusion tests. Note also that this is backward model selection, since our null hypothesis consists on a subgraph. Let $\widehat{\mathfrak{\Sigma}}_{0}$ and $\widehat{\mathfrak{\Sigma}}$ be the maximum likelihood estimators for a covariance matrix in the Markov model determined by $\mathcal{G}_{0}$ and $\mathcal{G}$, respectively. The likelihood ratio statistic is

$$
T_{L}=\frac{\operatorname{det}(\widehat{\mathfrak{\Sigma}})^{N / 2}}{\operatorname{det}\left(\widehat{\mathfrak{\Sigma}}_{0}\right)^{N / 2}}=\left(\frac{\operatorname{det}\left(\widehat{\mathbf{\Omega}}_{0}\right)}{\operatorname{det}(\widehat{\mathbf{\Omega}})}\right)^{N / 2}
$$

Under $H_{0},-2 \log \left(T_{L}\right)=N\left(\log \operatorname{det}(\widehat{\mathbf{\Omega}})-\log \operatorname{det} \widehat{\mathbf{\Omega}}_{0}\right)$ is asymptotically distributed as a $\chi^{2}$ distribution with $\left|E_{\mathcal{G}}\right|-\left|E_{\mathcal{G}_{0}}\right|$ degrees of freedom; however, this is a poor approximation in many cases (Porteous, 1989). More accurate distributional results have been derived by Eriksen (1996), as follows. Let $\mathcal{G}_{0} \subset \ldots \subset \mathcal{G}_{k}(=\mathcal{G})$ be a sequence of graphs where, for $1 \leq i \leq k, E_{\mathcal{G}_{i-1}}=E_{\mathcal{G}_{i}} \backslash\left\{e_{i}\right\}$ for some $e_{i}=u_{i} v_{i} \in E_{\mathcal{G}_{i}}$ (sequence of edge deletions). Then, under $H_{0}, T_{L}^{2 / N}$ is distributed as the product $\prod_{i=1}^{k} B_{i}$ of univariate Beta variables, where, for $1 \leq i \leq k$,

$$
B_{i} \sim \mathcal{B}\left(\frac{1}{2}\left(N-\left|\operatorname{ne}_{\mathcal{G}_{i}}\left(u_{i}\right) \cap \operatorname{ne}_{\mathcal{G}_{i}}\left(v_{i}\right)\right|-2\right), \frac{1}{2}\right)
$$

The above result is exact whenever $\mathcal{G}$ and $\mathcal{G}_{0}$ are chordal or share the same non-chordal maximal subgraphs (Eriksen, 1996). Specifically, denote as $C_{i}^{*}=\operatorname{ne}\left(u_{i}\right) \cap \operatorname{ne}\left(v_{i}\right)$ the unique clique in $\mathcal{G}_{i}$ of which edge $e_{i}$ is a member. Then, under $H_{0}$ (see e.g. Lauritzen, 1996, Proposition 5.14)

$$
T_{L}^{2 / N}=\prod_{i=1}^{k}\left(1-r_{u_{i} v_{i} \cdot C_{i}^{*} \backslash\left\{u_{i} v_{i}\right\}}^{2}\right)
$$

giving that $T_{L}^{2 / N}$ is distributed as $\prod_{i=1}^{k} \mathcal{B}\left(\left(N-\left|C_{i}^{*}\right|\right) / 2,1 / 2\right)$. Note that in this decomposable case one avoids to actually compute $\widehat{\mathbf{\Omega}}$ and $\widehat{\mathbf{\Omega}}_{0}$. The statistic $T_{L}$ has been used for model selection in undirected Gaussian Markov models by Wermuth (1976b).

In the case of a directed Gaussian Markov model over an acyclic digraph $\mathcal{D}=(V, A)$, most of the results are adaptations from analogues in multivariate linear Gaussian models. The likelihood ratio, whose moments are also characterized in Andersson and Perlman (1998), is

$$
T_{L}=\frac{\operatorname{det}(\widehat{\mathfrak{\Sigma}})^{\frac{N}{2}}}{\operatorname{det}(\widehat{\mathfrak{\Sigma}})^{\frac{N}{2}}}=\frac{\prod_{v \in V}\left|\widehat{\sigma}_{v v}-\widehat{\boldsymbol{\sigma}}_{v \cdot \mathrm{pa}(v)}^{t} \widehat{\mathfrak{\Sigma}}_{\mathrm{pa}(v)}^{-1} \widehat{\boldsymbol{\sigma}}_{v \cdot \mathrm{pa}(v)}\right|}{\prod_{v \in V}\left|\hat{\sigma}_{v v}-\hat{\boldsymbol{\sigma}}_{v \cdot \mathrm{pa}(v)}^{t} \widehat{\mathfrak{\Sigma}}_{\mathrm{pa}(v)}^{-1} \widehat{\boldsymbol{\sigma}}_{v \cdot \mathrm{pa}(v)}\right|}
$$

where $\widehat{\mathfrak{\Sigma}}$ and $\widehat{\mathfrak{\Sigma}}$ are the respective maximum likelihood estimators for $\hat{\mathcal{D}}$ and $\mathcal{D}, \hat{\mathcal{D}} \subseteq \mathcal{D}$.
A backward stepwise method has become popular for selecting $\mathcal{D}$, commonly called the PC algorithm (Spirtes et al., 2000). This method proceeds by first finding an estimator of the skeleton, $\widehat{\mathcal{D}^{U}}$, from a complete undirected graph, and then orienting it. At iteration $i$ of the first step (finding $\widehat{\mathcal{D}^{U}}$ ), $H_{0}: X_{u} \Perp X_{v} \mid X_{C}$ is tested, with $C=\overline{\operatorname{ne}}(u) \backslash\{v\}$ and $|C|=i$. The edge $u v$ is removed from $\widehat{\mathcal{D}^{U}}$ if $H_{0}$ is not rejected. Note that $\widehat{\mathcal{D}^{U}}$ depends on the order in which $H_{0}$ is tested at each iteration, problem circumvented in the

modification by Colombo and Maathuis (2014). Assuming that $\mathcal{I}(\boldsymbol{X})=\mathcal{I}(\mathcal{D})$ (see Section 4), commonly called the faithfulness assumption, Robins et al. (2003) showed that the PC algorithm is pointwise consistent but may not be uniformly consistent, regardless of the method used for testing $H_{0}$. Zhang and Spirtes (2003) approached this problem by introducing a stronger condition, called strong faithfulness, which, by requiring nonzero partial correlations to have a common lower bound, gives uniform consistency, even in a high-dimensional setting (Kalisch and Bühlmann, 2007). However, despite the set of 'unfaithful' distributions has Lebesgue measure zero (Meek, 1995), those 'strongly unfaithful' constitute a non-zero Lebesgue measure set, which can in some cases be very large (Uhler et al., 2013; Lin et al., 2014).

# 7.2. Multiple testing 

When performing model selection with these tests, multiple testing error rates need to be controlled. For overcoming this, Drton and Perlman (2004) propose an alternative to the previous stepwise methods. First, note that both acyclic directed and undirected Gaussian Markov models over $V=\{1, \ldots, p\}$ are characterized by certain partial correlation coefficients, since for $u, v \in V$ and $U \subseteq V \backslash\{u, v\}$, we have $X_{u} \Perp X_{v} \mid \boldsymbol{X}_{U} \Longleftrightarrow \rho_{u v \cdot U}=0$. Assuming conditional independence, that is, $\rho_{u v \cdot U}=0$, then $\sqrt{N-|U|-2} r_{u v \cdot U} / \sqrt{1-r_{u v \cdot U}^{2}}$ has a $t$ distribution with $N-|U|-2$ degrees of freedom. However, a faster Gaussian approximation can be obtained using Fisher's $Z$ transform,

$$
Z(x)=\frac{1}{2} \log \left(\frac{1+x}{1-x}\right)=\tanh ^{-1}(x)
$$

In such case the distribution of $\sqrt{N-|U|-3} Z\left(r_{u v \cdot U}\right)$ tends to a standard Gaussian.
Based on the above discussion, Drton and Perlman (2004) propose a method where a set of simultaneous $p$-values and confidence intervals is obtained such that the edge set is estimated, for a significance level $\alpha$ and using Sidak (1967) inequality, as

$$
\widehat{E}^{\alpha}:=\left\{u v: \sqrt{N-p-1}\left|Z\left(r_{u v \cdot V \backslash\{u, v\}}\right)\right|>\Phi^{-1}\left(\frac{1}{2}(1-\alpha)^{\frac{2}{p(p-1)}}+\frac{1}{2}\right)\right\}
$$

where $\Phi$ is the cumulative distribution function of a standard Gaussian. Denoting as $\widehat{\mathcal{G}}^{\alpha}=\left(V, \widehat{E}^{\alpha}\right)$, it holds $\liminf _{N \rightarrow \infty} P\left(\widehat{\mathcal{G}}^{\alpha}=\mathcal{G}\right) \geq 1-\alpha$ if the distribution under consideration $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \in \boldsymbol{\mathcal { N }}(\mathcal{G})$ is faithful to $\mathcal{G}$, that is, if $\omega_{u v}=0 \Longleftrightarrow u v \notin E$. If faithfulness is not satisfied, then the result holds with respect to the smallest graph $\mathcal{H}$ such that $\mathcal{G} \subseteq \mathcal{H}$ and $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is faithful to $\mathcal{H}$.

The multiple testing procedure in (9) has also been extended in Drton and Perlman (2008), obtaining an estimate of the arc set as
$\widehat{A}^{\alpha}:=\left\{(v, u): v<u\right.$ and $\left.\sqrt{N-u-1}\left|Z\left(r_{u v \cdot \operatorname{pr}(u) \backslash\{v\}}\right)\right|>\Phi^{-1}\left(\frac{1}{2}(1-\alpha)^{\frac{2}{p(p-1)}}+\frac{1}{2}\right)\right\}$,
where an ancestral ordering $\prec$ is being assumed in $V$ such that the resulting permutation is the identity; that is, such that $v \prec u \Longleftrightarrow v<u$. Consistency is established as in the undirected case; note the symmetry with (9). See Drton and Perlman (2007) for a general discussion on some variations of (9) and (10) and their impact on overall error control.

Recently, Liu (2013) has extended the methodology of Drton and Perlman (2004) to the high dimensional scenario, with $p>N$.

A related testing procedure has emerged motivated by the field of gene network learning from microarray data. Instead of testing full partial correlations $\rho_{u v \cdot V \backslash\{u, v\}}$ in an undirected model, only limited $q$-order partial correlations $\rho_{u v \cdot U}=0$, where $U \subseteq$ $V \backslash\{u, v\}$ and $|U|=q$, are tested (Castelo and Roverato, 2006). An edge is added to the resulting graph, called $q$-partial graph, only when all of the $q$-partial correlations are rejected to be zero. This procedure is specially suited for situations where the number of variables is substantially larger than the number of instances, as happens in the case of microarray data, where low order conditional independence relationships (up to $q \leq 3$ ) have been popular (Wille and Bühlmann, 2006; de la Fuente et al., 2004; Magwene and Kim, 2004). Castelo and Roverato (2006) generalize and formalize these approaches, and provide a robust model selection procedure for $q$-partial graphs. This is intended to serve as an intermediate step for model selection of a classical undirected Markov model $\boldsymbol{\mathcal { N }}(\mathcal{G})$, and yields to a great simplification when $\mathcal{G}$ is sparse (Castelo and Roverato, 2006).

# 8. Regularization 

Regularization approaches, which perform model selection and estimation in a simultaneous way, have become popular in the context of Markov models. They are usually applied when $N<p$, and thus the existence of the maximum likelihood estimator is not guaranteed. The main consistency results available for both the directed and undirected cases share sparseness and high-dimensionality assumptions, as we will see below. There are two different approaches, those that penalize the likelihood and those that instead focus on the regression coefficients.

Througout this section, we will employ the asymptotic notation, specifically symbols $O(\cdot)$ and $\Theta(\cdot)$, asymptotic inferiority and equivalence, respectively. For $\mathbf{M} \in \mathbb{M}_{q \times r}(\mathbb{R})$, $\operatorname{vec}(\mathbf{M})$ will denote the vectorized function of $\mathbf{M},\left(m_{11}, \ldots, m_{q 1}, \ldots, m_{1 r}, \ldots, m_{q r}\right)^{t}$. This way, the operator norm of $\mathbf{M}$ will be denoted as $\|\mathbf{M}\|$; whereas $\|\mathbf{M}\|_{q \times r}$ will be used to denote $\|\operatorname{vec}(\mathbf{M})\|_{q \times r}$, being $\|\cdot\|_{p}$ the $p$-norm function. If $\boldsymbol{v}$ is a $p$-vector, $\operatorname{diag}(\boldsymbol{v})$ will denote the matrix $\mathbf{M}$ in $\boldsymbol{\Delta}_{p}$ with main diagonal $\boldsymbol{v}$; analogously, $\operatorname{diag}(\mathbf{M}) \in \boldsymbol{\Delta}_{p}$ will have the same diagonal as $\mathbf{M}$, and $\mathbf{M}^{-}$will be used for $\mathbf{M}-\operatorname{diag}(\mathbf{M})$.

### 8.1. Node-wise regression

Let $\mathcal{G}=(V, E)$ be an undirected graph, with $V=\{1, \ldots, p\}$. Let $X$ be a random vector whose distribution $\mathcal{N}_{p}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ belongs to the undirected Gaussian Markov model $\mathcal{N}(\mathcal{G})$. Assume, for notational simplicity, that $\boldsymbol{\mu}=\mathbf{0}$, and, following the notation of Section 6 , let $\mathbf{X}=\mathbf{x}$ be a $p \times N$ random sample from $\mathcal{N}_{p}(\mathbf{0}, \boldsymbol{\Sigma})$. Since for each $u, v \in V$, $\beta_{u v \cdot V \backslash\{u\}}=-\omega_{u v} / \omega_{u u}$ (Equation (3)), then

$$
X_{u} \Perp X_{v} \mid \boldsymbol{X}_{V \backslash\{u, v\}} \Longleftrightarrow \omega_{u v}=0 \Longleftrightarrow \beta_{u v \cdot V \backslash\{u\}}=\beta_{v u \cdot V \backslash\{v\}}=0
$$

This means that an analogue of the matrix $\mathbf{B}$ in directed Gaussian Markov models (Equation (7)) can be used for determining the missing edges in the undirected case. In Meinshausen and Bühlmann (2006), this is done in the regression function, as

$$
\widehat{\boldsymbol{b}}_{u}^{\lambda}:=\underset{\boldsymbol{b}_{u} \in \mathbb{R}^{p}, b_{u u}=0}{\arg \min }\left(\frac{1}{N}\left\|\mathbf{x}_{u}^{t}-\mathbf{x}^{t} \boldsymbol{b}_{u}\right\|_{2}^{2}+\lambda f\left(\boldsymbol{b}_{u}\right)\right)
$$

where $\lambda \geq 0, \mathbf{x}_{u}$ is the $u$-the row vector of $\mathbf{x}$ and $f(\cdot)$ is the penalty function. For each $v \in V \backslash\{u\}, \widehat{b}_{u v}^{\lambda}$ gives an estimate of $\beta_{u v \cdot V \backslash\{v\}}$. Let $\widehat{\operatorname{ne}}(v):=\{u \in V: \widehat{b}_{v u}^{\lambda} \neq 0\}$. while $u \in \operatorname{ne}(v) \Longleftrightarrow v \in \operatorname{ne}(u)$ for all $u, v \in V$, this may not be true for $\widehat{\operatorname{ne}}(u)$ and $\widehat{\operatorname{ne}}(v)$. Hence, two different estimators for the edge set $E$ may be defined

$$
\begin{aligned}
& \widehat{E}_{\wedge}:=\{u v: u \in \widehat{\operatorname{ne}}(v) \text { and } v \in \widehat{\operatorname{ne}}(u)\} \\
& \widehat{E}_{\vee}:=\{u v: u \in \widehat{\operatorname{ne}}(v) \text { or } v \in \widehat{\operatorname{ne}}(u)\}
\end{aligned}
$$

Let $f(\cdot)=\|\cdot\|_{1}$, commonly known as the lasso penalty (Tibshirani, 1996) or $l_{1}$ regularization. Then both estimators $\widehat{E}_{\wedge}$ and $\widehat{E}_{\vee}$ are consistent for certain choice of $\lambda$. This result was independently discovered by Meinshausen and Bühlmann (2006), Zhao and Yu (2006), Zou (2006) and Yuan and Lin (2007b). It relies on the following almost necessary and sufficient condition

$$
\left|\sum_{v \in \operatorname{ne}(v)} \operatorname{sign}\left(\beta_{v z \cdot \operatorname{ne}(v)}\right) \beta_{u z \cdot \operatorname{ne}(v)}\right|<1
$$

This node-wise regression approach may also be used to perform model selection for acyclic directed Gaussian Markov models if there is a known order among the variables, see for example Shojaie and Michailidis (2010) or Yu and Bien (2017) and references therein. From Equation (7), the regression function to penalize in this case would be, for each $u \in V$,

$$
X_{u}=\mu_{u}+\sum_{v \in \operatorname{pr}(u)} \beta_{u v \cdot \operatorname{pr}(u)}\left(X_{v}-\mu_{v}\right)+E_{u}
$$

The condition of Equation (12), commonly called the 'irrepresentable condition' (Zhao and Yu, 2006) or 'neighbourhood stability' (Meinshausen and Bühlmann, 2006), is inherent to model selection in linear regression with $l_{1}$ regularization, and thus it also holds when penalizing (13) with the $l_{1}$ penalty. However, some variants have been proposed because it is rather restrictive. These alternatives usually rely on thresholding the regression coefficients or adding weights in the $l_{1}$ penalty, that under milder assumptions still achieve model selection consistency (Meinshausen and Yu, 2009) or other attractive, 'oracle' properties (van de Geer and Bühlmann, 2009); see Bühlmann and van de Geer (2011), $\S 7$ for a review. van de Geer and Bühlmann (2009) show that although model selection consistency for neighbourhood selection may be restrictive, sufficient conditions for such oracle properties hold fairly generally.

# 8.2. Penalized likelihood 

In van de Geer and Bühlmann (2013), $l_{0}$ regularization is alternatively used in the context of directed Gaussian Markov models, without assuming a known order. As in Meinshausen and Bühlmann (2006), the regression coefficients are penalized in their approach, more generally, the $\mathcal{D}$-parameters in the likelihood function (assuming $\boldsymbol{\mu}=$ 0). As such, the assumptions required for the consistency of both methods share some symmetry, as we have outlined in Table 1. The estimators in this case are obtained as

$$
\left(\widehat{\mathbf{V}}^{\lambda}, \widehat{\mathbf{B}}^{\lambda}\right)=\underset{\boldsymbol{\Omega}=\left(\mathbf{I}_{p}-\mathbf{B}\right)^{\mathbf{t}} \mathbf{V}^{-1}\left(\mathbf{I}_{p}-\mathbf{B}\right), \mathbf{B} \in \mathbb{M}(\mathcal{D}), \mathbf{V} \in \Delta_{p}}{\arg \min }(\operatorname{tr}(\boldsymbol{\Omega} \mathbf{S})-N \log \operatorname{det}(\boldsymbol{\Omega})+\lambda f(\boldsymbol{\Omega}))
$$


Table 1: Comparison of assumptions for consistency results on regression based penalized estimation in acyclic directed and undirected Gaussian Markov models.
where $\lambda \geq 0, \mathbb{M}(\mathcal{D}), \boldsymbol{\Delta}_{p}$ are as in Equation (8) and $\mathbf{S}=\mathbf{x x}^{t} / N$. When $f(\boldsymbol{\Omega})=$ $\left|\left\{(u, v): b_{u v} \neq 0\right\}\right|$ ( $l_{0}$ regularization), $\widehat{\mathbf{V}}^{\lambda}$ and $\widehat{\mathbf{B}}^{\lambda}$ are equal among Markov equivalent models and the resulting estimator of the concentration matrix $\widehat{\boldsymbol{\Omega}}^{\lambda}$ is consistent for certain choice of $\lambda$ (van de Geer and Bühlmann, 2013). The strong faithfulness condition for the PC algorithm, bounding nonzero partial correlations, resembles the assumptions for regularization methods (Table 1). In fact, $l_{0}$ regularization has been suggested as an alternative for the PC, in order to avoid the restrictive strong faithfulness assumption (Uhler et al., 2013); however, it is unclear how the assumptions of both methods are related. For recent extensions of the work by van de Geer and Bühlmann (2013), see Aragam and Zhou (2015) and Aragam et al. (2017).

In undirected Gaussian Markov models conditional independences can be read from $\boldsymbol{\Omega}$. Therefore, the penalized likelihood approach can be formulated more directly, for $\lambda \geq 0$, as

$$
\widehat{\boldsymbol{\Omega}}^{\lambda}=\underset{\boldsymbol{\Omega} \in \mathbb{S}^{=0}(\mathcal{G})}{\arg \min }(\operatorname{tr}(\boldsymbol{\Omega S})-N \log \operatorname{det}(\boldsymbol{\Omega})+\lambda f(\boldsymbol{\Omega}))
$$

Yuan and Lin (2007a) were the first to pursue this approach, and they chose $f(\boldsymbol{\Omega})=$ $\left\|\boldsymbol{\Omega}^{-}\right\|_{1}$, that is, the off-diagonal elements in $\boldsymbol{\Omega}$, which determine the edges of the resulting undirected graph, are penalized. Later, in Banerjee et al. (2008) the diagonal elements are included in the regularization function, that is, $f(\boldsymbol{\Omega})=\|\boldsymbol{\Omega}\|_{1}$; however, since $1 / \omega_{u u}=\sigma_{u u \cdot V \backslash\{u\}}$, this choice for the penalty favours larger values for the error variances in the regression of $X_{u}$ on the rest of variables (Bühlmann and van de Geer, 2011). Nonetheless, this estimator is the one chosen in the extensively used algorithm Graphical Lasso of Friedman et al. (2008), although model selection consistency has only been proved for $f(\boldsymbol{\Omega})=\left\|\boldsymbol{\Omega}^{-}\right\|_{1}$ (Lam and Fan, 2009; Ravikumar et al., 2011). It is not known whether the sufficient conditions required for this consistency are strictly stronger than the irrepresentable condition, as some examples (Meinshausen, 2008) seem to indicate.

For the penalization of Yuan and Lin (2007a) $\left(f(\boldsymbol{\Omega})=\left\|\boldsymbol{\Omega}^{-}\right\|_{1}\right)$, the convergence rate is (Rothman et al., 2008)

$$
\left\|\widehat{\boldsymbol{\Omega}}^{\lambda}-\boldsymbol{\Omega}\right\|_{2} \in O\left(\sqrt{\frac{(|E|+p) \log (p)}{N}}\right) \text { as } N \rightarrow \infty
$$

A relaxation of this rate can be obtained based on the correlation matrix, as follows. Since $\boldsymbol{\Sigma}=\mathbf{D P D}$ with $\mathbf{P}$ the correlation matrix and $\mathbf{D}$ the diagonal matrix of standard deviations, if we let the corresponding sample estimates be $\widehat{\mathbf{D}}^{2}=\operatorname{diag}(\widehat{\boldsymbol{\Sigma}})$ and $\widehat{\mathbf{P}}=$

$\widehat{\mathbf{D}}^{-1} \widehat{\boldsymbol{\Sigma}} \widehat{\mathbf{D}}^{-1}$, we can then estimate $\mathbf{K}=\mathbf{P}^{-1}$ as

$$
\widehat{\mathbf{K}}^{\lambda}=\underset{\mathbf{K} \in \mathbb{S}^{+} \in(\mathcal{G})}{\arg \min }\left(\operatorname{tr}(\mathbf{K} \widehat{\mathbf{P}})-N \log \operatorname{det}(\mathbf{K})+\lambda f(\mathbf{K})\right)
$$

for $\lambda \geq 0$. The concentration matrix can then be alternatively estimated as $\hat{\boldsymbol{\Omega}}^{\lambda}=$ $\widehat{\mathbf{D}}^{-1} \widehat{\mathbf{K}}^{\lambda} \widehat{\mathbf{D}}^{-1}$, yielding a convergence rate of (Rothman et al., 2008)

$$
\left\|\hat{\boldsymbol{\Omega}}^{\lambda}-\boldsymbol{\Omega}\right\| \in O\left(\sqrt{\frac{(|E|+1) \log (p)}{N}}\right) \text { as } N \rightarrow \infty
$$

Convergence rates in other norms are provided in Ravikumar et al. (2011), and they have been generalized by Lam and Fan (2009) for other penalty functions.

# 9. Bayesian model selection and estimation 

Consider a continuous multivariate family $\mathcal{F}_{\boldsymbol{\theta}}$ parametrized by $\boldsymbol{\theta}$, and denote as $f(\mathbf{x} \mid$ $\boldsymbol{\theta})$ the density function of a random sample $\mathbf{X}$ from $P \in \mathcal{F}_{\boldsymbol{\theta}}$ for a given value of $\boldsymbol{\theta}$. In Bayesian statistics, $\boldsymbol{\theta}$ is treated as a random variable with known distribution, $f(\boldsymbol{\theta})$, usually called the prior distribution of $\boldsymbol{\theta}$. Inference is then performed based on the value of $f(\boldsymbol{\theta} \mid \mathbf{x}) \propto f(\boldsymbol{\theta}) f(\mathbf{x} \mid \boldsymbol{\theta})$, the posterior distribution of $\boldsymbol{\theta}$ given the information in $\mathbf{X}=\mathbf{x}$.

In Gaussian Markov models, $\boldsymbol{\theta}=(\boldsymbol{\mu}, \boldsymbol{\Omega}, \mathcal{G})$, where in our case $\mathcal{G}$ is either undirected or acyclic directed. Therefore the target probability is $f(\mathcal{G}, \boldsymbol{\mu}, \boldsymbol{\Omega} \mid \mathbf{x}) \propto f(\mathbf{x} \mid$ $\boldsymbol{\mu}, \boldsymbol{\Omega}, \mathcal{G}) f(\boldsymbol{\mu}, \boldsymbol{\Omega} \mid \mathcal{G}) f(\mathcal{G})$. Integrating out $\boldsymbol{\mu}$ and $\boldsymbol{\Omega}$, we obtain the posterior density of model $\mathcal{G}, f(\mathcal{G} \mid \mathbf{x}) \propto f(\mathbf{x} \mid \mathcal{G}) f(\mathcal{G})$. The prior for the graph space, $f(\mathcal{G})$, is usually set as uniform. However, this choice is biased towards middle size graphs, and thus other prior distributions (Scutari, 2013, e.g.) have been proposed; see Massam (2018) $\S 10.4 .1$ and references therein for a recent detailed overview. Bayesian inference for Gaussian graphical models, is usually meant for moderate sample sizes, since it relies on sampling from the resulting posterior distribution, which becomes infeasible in high dimensions (see e.g. Jones et al., 2005 or Massam, 2018).

In the following, the $p$-variate Wishart distribution will be denoted as $\mathcal{W}_{p}(n, \boldsymbol{\Lambda})$ with $n \in \mathbb{R}, n>p-1$ and $\boldsymbol{\Lambda} \in \mathbb{M}_{p \times p}(\mathbb{R}), \boldsymbol{\Lambda} \succ 0$; analogously, the $p$-variate inverse Wishart distribution will be $\mathcal{W}_{p}^{-1}(\nu, \boldsymbol{\Psi})$ with $\nu \in \mathbb{R}, \nu>p-1$ and $\boldsymbol{\Psi} \in \mathbb{M}_{p \times p}(\mathbb{R}), \boldsymbol{\Psi} \succ 0$.

### 9.1. Hyper Markov laws

When $\mathcal{G}$ is undirected and decomposable, and assuming $\boldsymbol{\mu}=\mathbf{0}$, Dawid and Lauritzen (1993) proposed for $f(\boldsymbol{\Omega} \mid \mathcal{G})$ what are known as the hyper Markov laws. These are defined in terms of properties of the graph associated with the Markov model, mimicking Markov properties. Specifically, let $\boldsymbol{\theta}$ be a random variable taking values over $\boldsymbol{\mathcal { N }}(\mathcal{G})$ and for subsets $A, B \subseteq V$, denote as $\boldsymbol{\theta}_{A}$ and $\boldsymbol{\theta}_{B \mid A}$ the parameters of the marginal distribution of $\boldsymbol{X}_{A}$ and the conditional distribution of $\boldsymbol{X}_{A}$ given values of $\boldsymbol{X}_{B}$, respectively. The probability distribution of $\boldsymbol{\theta}$ is said to be (weakly) hyper $\mathcal{G}$ - Markov if, for any decomposition $(A, B, S)$ of $\mathcal{G}$, it holds that $\boldsymbol{\theta}_{A \cup S} \Perp \boldsymbol{\theta}_{B \cup S} \mid \boldsymbol{\theta}_{S}$; if it further holds $\boldsymbol{\theta}_{B \cup S \mid A \cup S} \Perp \boldsymbol{\theta}_{A \cup S}$, it is called strongly hyper $\mathcal{G}$-Markov. For chordal graphs, if

the probability distribution of $\boldsymbol{\theta}$ is strongly hyper $\mathcal{G}$-Markov with respect to $\mathcal{G}$, then the probability distribution of $\boldsymbol{\theta} \mid \mathbf{x}$ is the unique (strong) hyper $\mathcal{G}$-Markov distribution specified by the clique-marginal distributions $\left\{\mathbb{P}\left(\boldsymbol{\theta}_{C} \mid \mathbf{x}_{C}\right): C \in \mathfrak{C}(\mathcal{G})\right\}$; and, when densities exist, $f\left(\boldsymbol{\theta}_{C} \mid \mathbf{x}\right) \propto f\left(\mathbf{x}_{C} \mid \boldsymbol{\theta}_{C}\right) f\left(\boldsymbol{\theta}_{C}\right)$ (Dawid and Lauritzen, 1993), where $\mathbf{x}_{C}$ stands for all the observations in $\mathbf{x}$ corresponding to the variables in $C$. That is, under these assumptions, it is possible to localize computations over the graph cliques when performing Bayesian inference.

In a multivariate Gaussian distribution $\mathcal{N}_{p}(\mathbf{0}, \boldsymbol{\Sigma})$, the inverse Wishart is a conjugate prior for $\boldsymbol{\Sigma}$; that is, if $\boldsymbol{\Sigma} \sim \mathcal{W}_{p}^{-1}(\nu, \boldsymbol{\Psi})$, then $\boldsymbol{\Sigma} \mid \mathbf{Q} / N \sim \mathcal{W}_{p}^{-1}(N+\nu, \mathbf{Q}+\boldsymbol{\Psi})$ (recall $\mathbf{Q}=\mathbf{x x}^{t}$ ). We can thus construct the hyper inverse Wishart distribution, as the unique hyper Markov distribution associated with inverse Wishart clique marginals: $\boldsymbol{\Sigma}_{C C} \sim$ $\mathcal{W}_{|C|}^{-1}\left(\nu, \boldsymbol{\Psi}^{C}\right)$, for each clique $C \in \mathfrak{C}(\mathcal{G})$. This hyper Markov distribution is denoted as $\mathcal{H} \mathcal{W}_{p}^{-1}(\nu, \boldsymbol{\Psi})$, where $\boldsymbol{\Psi} \in \mathbb{S}^{>0}$ such that $\boldsymbol{\Psi}_{C C}=\boldsymbol{\Psi}^{C}$ for each clique $C \in \mathfrak{C}(\mathcal{G})$. From the discussion above, we know that this distribution is strongly hyper $\mathcal{G}$-Markov. The main advantage of this prior is that it has many properties that mirror those for Markov models, since hyper Markov distributions are also defined in terms of an underlying graph.

Since its introduction, the hyper inverse Wishart prior for decomposable graphs has been extensively studied. The explicit expression for its density is devised in, e.g., Giudici (1996) or Roverato (2000). In order to set its parameters, a hierarchical approach such as in Giudici and Green (1999) can be followed, where $\nu$ and $\boldsymbol{\Psi}$ are assumed to have a Gamma and Wishart distribution, respectively. Since the absent edges of $\mathcal{G}$ correspond to zeros in $\boldsymbol{\Omega}$ (Equation (4)), Roverato (2000) derives the distribution induced on $\boldsymbol{\Omega}$ by assuming $f(\boldsymbol{\Sigma} \mid \mathcal{G})=\mathcal{H} \mathcal{W}_{p}^{-1}(\nu, \boldsymbol{\Psi})$. He shows that in that case, the density is proportional to that of a Wishart matrix conditioned on the event $\boldsymbol{\Omega} \in \mathbb{S}^{>0}(\mathcal{G})$, and calls such prior distribution on $\boldsymbol{\Omega}$ the $\mathcal{G}$-conditional Wishart. Recently, Massam (2018) $\S 10.3 .2$ has provided a detailed overview of the properties of the hyper inverse Wishart, and technical considerations as how to sample from it or perform Bayesian model selection using Bayes factors. Letac and Massam (2007) generalize both the $\mathcal{G}$-conditional and hyper inverse Wishart to a broader conjugate family, allowing for more than one shape parameter, which is used for model selection by Rajaratnam et al. (2008) (see also Massam, 2018, $\S 10.3 .3)$.

The hyper inverse Wishart has been extended to non-chordal graphs by Roverato (2002), based on properties of the Isserlis matrix of $\boldsymbol{\Sigma}$ (Roverato and Whittaker, 1998). However, Bayesian model selection in this scenario requires the evaluation of the $\mathcal{G}$ conditional Wishart normalizing constant, which becomes a problem since it did not have a known closed-form expression for a general non-chordal $\mathcal{G}$ until very recently (Uhler et al., 2018). Much of the literature therefore has been devoted to this issue: Atay-Kayis and Massam (2005) analysed the Cholesky decomposition of $\boldsymbol{\Omega}$ and its relation with the cone $\mathbb{S}^{>0}(\mathcal{G})$ and positive definite matrix completions (Section 6), Carvalho et al. (2007) and Wang and Carvalho (2010) used such theoretical analysis to provide a direct sampler from the hyper inverse Wishart prior, etc. A recent detailed presentation of this computational body of research can be found in Massam (2018), §10.4. Note that, although Uhler et al. (2018) provide exact formulas and examples for special types of graphs, it still remains to find efficient methods for their computation.

# 9.2. Priors for acyclic directed models 

The methodology by Geiger and Heckerman (2002) for acyclic directed Gaussian Markov models can be seen as an extension of hyper Markov distributions to such context, since they both coincide for chordal skeletons.

If $\mathcal{D}_{c}$ is an arbitrary complete digraph, then, under some assumptions on $f(\boldsymbol{\mu}, \boldsymbol{\Omega} \mid \mathcal{D})$ and $f(\mathbf{x} \mid \mathcal{D}, \boldsymbol{\mu}, \boldsymbol{\Omega})$, computations can be localized as

$$
f(\mathbf{x} \mid \mathcal{D})=\prod_{v \in V} \frac{f\left(\mathbf{x}_{\{v\} \cup \mathrm{pa}_{\mathcal{D}}(v)} \mid \mathcal{D}_{c}\right)}{f\left(\mathbf{x}_{\mathrm{pa}_{\mathcal{D}}(v)} \mid \mathcal{D}_{c}\right)}
$$

The posterior in Equation (15) is equal among Markov equivalent acyclic digraphs (Geiger and Heckerman, 2002).

The conjugate prior for $(\boldsymbol{\mu}, \boldsymbol{\Omega})$ is the normal-Wishart distribution, where $\boldsymbol{\Omega} \sim \mathcal{W}_{p}\left(\alpha_{\boldsymbol{\Omega}}, \boldsymbol{\Lambda}\right)$ and $\boldsymbol{\mu} \mid \boldsymbol{\Omega} \sim \mathcal{N}_{p}\left(\boldsymbol{\mu}_{0},\left(\alpha_{\boldsymbol{\mu}} \boldsymbol{\Omega}\right)^{-1}\right)$. This yields a normal-Wishart posterior distribution for $(\boldsymbol{\mu}, \boldsymbol{\Omega}) \mid \mathcal{D}_{c}$. Using this, Geiger and Heckerman (1994), obtain an explicit expression for each factor in Equation (15): for $U \subseteq V$,

$$
f\left(\mathbf{x}_{U} \mid \mathcal{D}_{c}\right)=\left(\frac{\alpha_{\boldsymbol{\mu}}}{\alpha_{\boldsymbol{\mu}}+N}\right)^{\frac{|U|}{2}} 2 \pi^{-\frac{i N}{2}} \frac{\Gamma_{|U|}\left(\frac{N+\alpha_{\boldsymbol{\Omega}}-p+|U|}{2}\right)}{\Gamma_{|U|}\left(\frac{\alpha_{\boldsymbol{\Omega}}-p+|U|}{2}\right)} \frac{\left|\mathbf{\Lambda}_{U U}\right|^{\frac{\alpha_{\boldsymbol{\Omega}}-p+|U|}{2}}}{|\mathbf{R}_{U U}|^{\frac{\alpha_{\boldsymbol{\Omega}}-p+|U|+N}{2}}}
$$

where $\Gamma_{p}(\cdot)$ is the $p$-dimensional Gamma function, and

$$
\mathbf{R}=\boldsymbol{\Lambda}+\mathbf{Q}+\frac{N \alpha_{\boldsymbol{\Omega}}}{N+\alpha_{\boldsymbol{\Omega}}}\left(\boldsymbol{\mu}_{0}-\overline{\mathbf{x}}\right)\left(\boldsymbol{\mu}_{0}-\overline{\mathbf{x}}\right)^{t}
$$

Furthermore, Geiger and Heckerman (2002) characterize the normal-Wishart prior for $(\boldsymbol{\mu}, \boldsymbol{\Omega})$ as the only distribution satisfying the global parameter independence assumption,

$$
f(\boldsymbol{\theta} \mid \mathcal{D})=\prod_{v \in V} f\left(\theta_{v} \mid \mathcal{D}\right)
$$

for every $P_{\boldsymbol{X}} \in \boldsymbol{\mathcal { N }}(\mathcal{D})$. This condition is required for Equation (15) to hold.
The above priors have been used by Consonni and Rocca (2012) and Altomare et al. (2013) for objective Bayesian model selection, where $f(\boldsymbol{\theta} \mid \mathcal{D})$ might be improper. For overcoming this, they use fractional Bayes factors (O'Hagan, 1995), which had been also previously used by Carvalho and Scott (2009) for chordal undirected models (see Massam, 2018, $\S 10.6$ and references therein for more details). Recently, Ben-David et al. (2016) have proposed a family of priors extending those by Geiger and Heckerman (2002) but including more shape parameters, that is, mimicking those in Letac and Massam (2007) for undirected models. See Rajaratnam (2012) and Cao et al. (2019) for further discussion on these priors.

## 10. Higher level Markov model classes with mixed graphs

As we have seen throughout this review, the classes of acyclic directed and undirected Markov models are intimately related. Therefore, one approach for their unified treatment could be to step to a higher level, and define new Markov model classes containing

them as subclasses. In this section we will overview this approach, which has been particularly active in the past few years. The graphs used for these new Markov models are usually called mixed graphs, because unlike purely undirected or acyclic directed graphs, they allow for more than one edge type. We do not aim in this section for a thorough account of the achievements and drawbacks of the different developments since that would take another full paper.

Chain graphs are the first higher level attempt at this unification: they allow two edge types, directed and undirected, and forbid semi-directed cycles. Drton (2009) provides a unifying view of these model classes, focusing on their discrete parametrization: both the undirected and directed edges can have two different interpretations, thus giving rise to four different chain graph model classes. Among them, AMP chain graphs (Andersson et al., 2001), and LWF chain graphs (Lauritzen and Wermuth, 1989; Frydenberg, 1990), named in such way because of the respective paper authors, contain both acyclic directed and undirected Markov model classes.

Multivariate regression (MVR) chain graphs (Cox and Wermuth, 1993, 1996), or Type IV in Drton (2009), are possibly the most traditional ones and can be viewed as a special case of the path diagrams by Wright (1934). Although they do not contain undirected models, their extension, regression graphs (Wermuth and Sadeghi, 2012; Wermuth, 2011), do contain both classes treated in this review, by allowing up to three edge types. The class of regression graphs allows to represent additional relationships in classical sequences of multivariate regressions by means of a bi-directed edge, which could not be otherwise modelled using only the acyclic directed or undirected graphs. These bi-directed edges represent interactions with latent variables. The recovery of latent variables is specially relevant in social studies, where the presence of these confounding variables may affect the prediction. It has been recently shown that a Gaussian MVR chain graph is Markov equivalent to an acyclic directed Gaussian Markov model with latent variables when its bidirected part is chordal (Fox et al., 2015). Pure Gaussian bidirected graphs represent marginal independences among variables, therefore they impose zero constraints directly in the covariance $\boldsymbol{\Sigma}$.

Finally, the Type III chain graph so far has not been devoted much attention (Lauritzen and Sadeghi, 2018). All of the mentioned chain graph model classes are smooth, whereas for their discrete counterparts only the classes of LWF and multivariate regression chain graphs consist of smooth models (Drton, 2009).

The semi-directed cycle constraint on chain graphs can be relaxed, and new graphical model classes are obtained by forbidding only directed cycles. By doing so, we arrive at three different classes of what are called acyclic directed mixed graphs: the so-called original acyclic directed mixed graph (oADMG, Richardson, 2003), the alternative (aADMG, Peña, 2016a), and $U D A G s$ (Peña, 2018), which relax MVR, AMP and LWF chain graphs, respectively. Each oADMG model contains a model obtained from a Bayesian network after marginalizing some of its nodes, (the latent variables). However, other constraints may arise after marginalizing that cannot be represented in terms of conditional independence with this class, for example, the Verma constraints (Richardson and Spirtes, 2002, §7.3.1) and inequality constraints (Drton et al., 2012). In order to deal with these, Richardson et al. (2012) introduced nested Markov models which also allow for hyper-edges between more than two nodes; however, we are not aware of any Gaussian parametrization.

The classes of both oADMGs and aADMGs are subsumed by the class of $A D M$

graphs (Peña, 2018), consisting, naturally, of three edge types. When parametrized with the Gaussian distribution, ADM graph models can be represented as recursive linear equations with two blocks of variables and possibly correlated errors (Koster, 1999; Spirtes, 1995; Peña, 2016a,b). Bidirected edges in these models represent latent confounding effects, whereas undirected edges account for dependence between the errors. Note that, although the classes of ADM graphs and regression graphs allow the same edge types, they are not equivalent since the former contains AMP chain graph models, while the latter doesn't.

There are other models allowing for up to three edge types, besides the already mentioned ADM and regression graphs: anterial and chain mixed graphs (Sadeghi, 2016), ribbonless graphs (Sadeghi, 2013), MC graphs (Koster, 2002), summary graphs (Wermuth, 2011; Cox and Wermuth, 1996), ancestral graphs (Richardson and Spirtes, 2002), etc. These model classes share rich relationships, which have been recently discussed by Lauritzen and Sadeghi (2018). Ancestral graphs extend regression graphs by relaxing the cycle constraint, but they are not a maximal class; that is, if an edge is removed from the graph, we may remain on the same Markov model. Maximality is convenient because it is what allows to define pairwise Markov properties, so that each edge absent implies a conditional independence. Fortunately, for an arbitrary ancestral graph we may always find a maximal one which is Markov equivalent to it, therefore many times authors speak of the class of maximal ancestral graphs (MAGs). This class is closed under marginalization and conditioning, and every MAG can be obtained from an acyclic digraph after performing such operations on its nodes. Just as marginalization leads to latent confounders, conditioning is sometimes called selection bias in the literature on social sciences.

The class of summary graphs, although in correspondence with ancestral graphs, is not easily parameterized. One of the main drawbacks is that they allow more than one edge type between the nodes, which means that in principle more than one parameter can be associated between a pair of variables. Furthermore, they are not maximal and thus cannot have a pairwise Markov property, which implies that fewer independences can be deduced from the model. Most of the other three-edge-type models mentioned share these drawbacks for defining a parametrization (Richardson and Spirtes, 2002; Sadeghi and Marchetti, 2012).

The proliferation of higher level Markov model classes has led Lauritzen and Sadeghi (2018) to recently propose a class of mixed graphs consisting of up to four edge types, in an attempt to unify most of them under a unique Markov property (see also Sadeghi and Lauritzen, 2014; Evans, 2018). Nowadays, a great amount of research is focused on characterizing basic foundational properties for these higher level models: for example, Markov equivalence, definition and equivalence of Markov properties, factorization properties, etc.

# 11. Relaxing the Gaussian assumption 

In some real problems, the Gaussian assumption is too restrictive, and thus some alternative models to overcome this have been proposed. Although these are outside the scope of this review, we will survey here the main proposals to relax the Gaussian assumption.

As we have seen, Gaussian Bayesian networks are equivalent to a set of recursive regressions where the errors are Gaussian. In Shimizu et al. (2006), an analogous model is proposed, called LiNGAM, where the errors are assumed to be non Gaussian. The work by Loh and Bühlmann (2014) generalizes further generalizes this by not making distributional assumptions on the errors. As an alternative, Peters et al. (2014) and Bühlmann et al. (2014) maintain Gaussian errors but the additive regression is now assumed to be non linear. Other families of continuous distributions that have been used for parametrizing Markov and Bayesian networks are nonparametric Gaussian copulas (Liu et al., 2009) and elliptical distributions (Vogel and Fried, 2011), both of which generalize the Gaussian distribution. Copula graphical models are usually referred to as 'nonparanormal' models, and model selection and estimation have been researched by Harris and Drton (2013), Xue and Zou (2012) and Liu et al. (2012), including high-dimensional scenarios. Estimation results for elliptical graphical models have been obtained by Vogel and Tyler (2014).

Another approach is to extend the model and allow for both discrete and continuous variables. In such case, a challenge is posed specially on inference in Bayesian networks, where the usual operations may not allow for a direct and efficient implementation as in the pure cases. The main source of this problem is the integration that appears in marginalization of continuous variables. To overcome this, the classical approach is to use the conditional Gaussian distribution (Olkin and Tate, 1961). It is characterized by a multinomial distribution on the discrete variables and a Gaussian distribution for the continuous variables when conditioned on the discrete ones. Therefore, it contains the pure multinomial and Gaussian models as particular cases. Markov properties of this distribution with respect to an undirected graph were defined by Lauritzen and Wermuth (1989). With respect to an acyclic digraph, a further assumption is that no discrete variable may have continuous parents, which leads to conditional linear Gaussian Bayesian networks (Lauritzen, 1992). Exact inference in these networks is applicable thanks to these constraints imposed on the network topology.

In order to avoid the structural constraints of conditional linear Gaussian Bayesian networks, nonparametric density estimation techniques have been proposed. Moral et al. (2001) approximated the joint density by mixtures of truncated exponentials. In this model, discrete nodes with continuous parents are allowed, while exact inference remains possible. A similar approach is that of Shenoy and West (2011), where mixtures of polynomials are used instead for approximating the joint density. These two models have been generalized by Langseth et al. (2012) as mixtures of truncated basis functions. However, there are limited results about maximum likelihood estimation and model selection for these models (Langseth et al., 2010, 2014; Varando et al., 2015).

# 12. Main application areas 

Graphical or Markov models have been widely applied since their conception and continue to be nowadays an essential tool in many fields, since they are intuitive for visualizing the associations between the components in a system. We will first outline applications of Gaussian Markov and Gaussian Bayesian networks and then illustrate other areas where graphical models have played an important role.

Markov and Bayesian networks with Gaussian parametrization have been specially useful in biomedical sciences. For example, Gaussian Bayesian networks have been used

for extracting knowledge from fMRI studies (Mumford and Ramsey, 2014; Zhou et al., 2016), where nodes are identified with brain regions, and arrows are interpreted as direct influences between the respective regions. Another example where both models have been applied is the modelling of gene regulatory networks, which are high-dimensional and complex by nature. In fact, the challenge posed by this problem has served as an impulse for methodological developments in both models. A vast amount of literature can be found regarding the main computational aspects involved on this subject, as well as interpretability issues, see Lauritzen and Sheehan (2003), Friedman (2004), Markowetz and Spang (2007) and Ness et al. (2016) for reviews.

In social sciences, Bayesian networks have been used since their conception, in fact, we could say that research in this application area helped to settle the foundations of graphical models (Kiiveri and Speed, 1982). In terms of interpretability, the directed arcs in Bayesian networks are usually given a causal interpretation (Pearl, 2000; Cox and Wermuth, 1996), since ultimately the main goal of social studies is to identify the causes of a resulting event of interest. In recent years, graphical models have found a natural area of application which is social network analysis (Farasat et al., 2015), which include problems such as influence analysis, privacy protection, web browsing, etc.

Some other traditional models from bioinformatics can also be seen as graphical models. These include phylogenetic trees, which model evolutionary relationships between different species or organisms, and pedigrees, which are diagrams showing the occurrence and variants of a gene from one generation of organisms to the next (Jordan, 2004). Apart from fMRI studies, Bayesian networks have also been applied in different subareas of neuroscience (Bielza and Larrañaga, 2014), such as morphological and electrophysiological studies. Finally, other, more technical application areas include information retrieval (de Campos et al., 2004), where relevant documents about some matter are collected from an available set of sources, and linguistics, with subfields such as speech recognition (Deng and Li, 2013), and natural language processing (Cambria and White, 2014).

# Acknowledgements 

This work has been supported by the Spanish Ministry of Science, Innovation and Universities through the predoctoral grant FPU15/03797 holded by Irene Córdoba, and through the TIN2016-79684-P project.
