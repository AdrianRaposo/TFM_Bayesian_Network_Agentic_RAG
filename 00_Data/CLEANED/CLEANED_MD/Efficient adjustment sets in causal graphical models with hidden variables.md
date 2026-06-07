# Efficient adjustment sets in causal graphical models with hidden variables 

Ezequiel Smucler ${ }^{* 1}$, Facundo Sapienza ${ }^{\dagger 2}$, and Andrea Rotnitzky ${ }^{\ddagger 3}$<br>${ }^{1}$ Department of Mathematics and Statistics, Universidad Torcuato Di Tella<br>${ }^{3}$ Department of Statistics, University of California, Berkeley<br>${ }^{3}$ Department of Economics, Universidad Torcuato Di Tella, CONICET and Department of Biostatistics, Harvard T.H. Chan School of Public Health

May 27, 2020


#### Abstract

We study the selection of covariate adjustment sets for estimating the value of point exposure dynamic policies, also known as dynamic treatment regimes, assuming a non-parametric causal graphical model with hidden variables, in which at least one adjustment set is fully observable. We show that recently developed criteria, for graphs without hidden variables, to compare the asymptotic variance of non-parametric estimators of static policy values that control for certain adjustment sets, are also valid under dynamic policies and graphs with hidden variables. We show that there exist adjustment sets that are optimal minimal (minimum), in the sense of yielding estimators with the smallest variance among those that control for adjustment sets that are minimal (of minimum cardinality). Moreover, we show that if either no variables are hidden or if all the observable variables are ancestors of either treatment, outcome, or the variables that are used to decide treatment, a globally optimal adjustment set exists. We provide polynomial time algorithms to compute the globally optimal (when it exists), optimal minimal, and optimal minimum adjustment sets. Our results are based on the construction of an undirected graph in which vertex cuts between the treatment and outcome variables correspond to adjustment sets. In this undirected graph, a partial order between minimal vertex cuts can be defined that makes the set of minimal cuts a lattice. This partial order corresponds directly to the ordering of the asymptotic variances of the corresponding non-parametrically adjusted estimators.


## 1 Introduction

In this paper we consider the selection of covariate adjustment variables for off-policy evaluation (Precup et al., 2000) in single time contextual decision making problems. Specifically, we consider the choice of variables that suffice for estimating the value of a point exposure contextual policy by the method of covariate adjustment, when the available data come from a different policy. We assume a causal graphical model with, possibly, hidden variables in which at least one valid adjustment set is fully observable. The value of a policy, also known as the interventional mean, is defined as the mean of an outcome (reward) under the policy. In the statistics literature, a policy is referred to as a dynamic treatment regime (Robins, 1993; Murphy et al., 2001; Robins, 2004; Schulte et al., 2014).

A practical application of the methods described in this paper is in the design of planned observational studies. Investigators designing such study might use the existing graphical criteria for identifying the class of candidate valid covariate adjustment sets (Pearl, 2000; Kuroki and Miyakawa, 2003; Shpitser et al., 2010), and then apply the methods described in this paper to select an adjustment set that satisfies one of three optimality criteria that we consider here. Each criterion is defined by selecting the observable adjustment set that yields the non-parametrically adjusted estimator with smallest asymptotic variance among those that control for observable adjustment sets in a given class, specifically the class of (i) all adjustment sets, (ii) all minimal adjustment sets, or (iii) all adjustment sets that have minimum cardinality. We refer to adjustment sets satisfying criterion (i) as globally optimal, (ii)

[^0]
[^0]:    *esmucler@utdt.edu
    ${ }^{\dagger}$ fsapienza@berkeley.edu
    $\ddagger$ arotnitzky@utdt.edu

as optimal minimal and (iii) as optimal minimum. A minimal adjustment set is such that removal of any variable from it results in an invalid adjustment set.

Our proposal extends existing methods for selecting covariate adjustment sets in a number of ways. Specifically, Kuroki and Miyakawa (2003) proposed a graphical criteria for comparing the asymptotic variance of estimators of the value of a point exposure policy that control for two different adjustment sets, under the following assumptions: (i) a linear causal graphical model with no hidden variables, (ii) a policy that is an affine function of a single covariate $L$, (iii) estimators obtained by ordinary least squares, and (iv) adjustment sets that consist only on $L$ and another single variable. More recently, assuming (i) and (iii) as in Kuroki and Miyakawa (2003), but restricting attention to static policies, i.e. those that do not depend on covariates, Henckel et al. (2019) derived a general graphical characterization of the globally optimal adjustment set. Witte et al. (2020) derived an alternative graphical characterization of this set. Henckel et al. (2019) additionally provided a criterion for comparing adjustment sets that is more widely applicable than earlier existing criteria (Kuroki and Cai, 2004; Kuroki and Miyakawa, 2003). They also showed, by means of a counter-example, that in graphs with hidden variables with observable adjustment sets there may not exist a globally optimal adjustment set. Rotnitzky and Smucler (2019) extended the results of Henckel et al. (2019) to non-parametric causal graphical models and non-parametrically adjusted estimators. Moreover, they provided a graphical characterization of the optimal minimal adjustment set.

The contributions of this paper are:

1. We show that the criteria of Henckel et al. (2019) for comparing certain pairs of adjustment sets remains valid for point exposure dynamic treatment regimes in non-parametric causal graphical models with hidden variables.
2. We show that if either no variables are hidden, or if all the observable variables are ancestors of either treatment, outcome, or the variables that are used to decide treatment, a globally optimal adjustment set exists, and we provide a graphical characterization of it.
3. We show that in graphs with hidden variables that admit at least one observable adjustment set there always exist optimal minimal and optimal minimum adjustment sets and we provide graphical characterizations of them.
4. We provide polynomial time algorithms to compute the globally optimal (when it exists), optimal minimal, and optimal minimum adjustment sets.

The formulation of our computational algorithms builds on previous work regarding graphical characterizations of adjustment sets and algorithms to compute them developed in Acid and De Campos (1996), Tian et al. (1998), Textor and Liskiewicz (2011), van der Zander et al. (2014) and van der Zander et al. (2019). Specifically, Acid and De Campos (1996) and Tian et al. (1998) proposed polynomial time algorithms for finding minimal dseparators and minimum size d-separators for a given pair of vertices on a directed acyclic graph. Building on the work of these authors, van der Zander et al. (2019) (see also the earlier papers Textor and Liskiewicz (2011); van der Zander et al. (2014)) provided a constructive graphical characterization of adjustments sets for static interventions, and also polynomial time algorithms to compute adjustment sets, minimal adjustment sets, and minimum size adjustments, possibly under constraints on which some variables must be included and others must not be included in the desired adjustment set.

The rest of the paper is organized as follows. In Section 2 we review basic results and definitions regarding causal graphical models. Next, in Section 3, we extend the definition of adjustment sets of Shpitser et al. (2010) and Maathuis and Colombo (2015) to dynamic treatment regimes. In Section 4 we review non-parametric estimation of policy values. Section 5 extends the criteria of Rotnitzky and Smucler (2019) to compare certain adjustment sets to dynamic interventions in graphs with hidden variables. In Section 6 we provide graphical characterizations of globally optimal (when it exists), optimal minimal, and optimal minimum adjustment sets and in Section 7 we provide polynomial time algorithms to compute them. Finally in Section 8 we conclude with a discussion of open problems. The proofs of all the results stated in the main paper are available in the Supplementary Material.

# 2 Background 

We now review some basic definitions and results of the theory of graphical models.

# 2.1 Definitions and notation 

### 2.1.1 Undirected graphs

Undirected graphs. An undirected graph $\mathcal{H}=(\mathbf{V}, \mathbf{E})$ consists of a finite vertex set $\mathbf{V}$ and a set undirected edges E. An undirected edge between two vertices $V, W$ is represented by $V-W$. Given a set of vertices $\mathbf{Z} \subset \mathbf{V}$ the induced subgraph $\mathcal{H}_{\mathbf{Z}}=\left(\mathbf{Z}, \mathbf{E}_{Z}\right)$ is the graph obtained by considering only vertices in $\mathbf{Z}$ and edges between vertices in $\mathbf{Z}$. We will sometimes use the notation $\mathbf{V}(\mathcal{H})$ and $\mathbf{E}(\mathcal{H})$ to refer to the vertex and edge sets respectively of an undirected graph $\mathcal{H}$.
Paths. If $V-W$ is an edge in $\mathcal{H}$ then we say that $V$ and $W$ are adjacent. A path from a vertex $V$ to a vertex $W$ in graph $\mathcal{H}$ is a sequence of vertices $\left(V_{1}, \ldots, V_{j}\right)$ such that $V_{1}=V, V_{j}=W$ and $V_{i}$ and $V_{i+1}$ are adjacent in $\mathcal{H}$ for all $i \in\{1, \ldots, j-1\}$. We define the set of neighbors of a vertex $V$ as the set of vertices adjacent to $V$ and use the notation $\mathrm{nb}_{\mathcal{H}}(V)$ for this set. For a set of vertices $\mathbf{Z} \subset \mathbf{V}$ we let $\operatorname{nb}_{\mathcal{H}}(\mathbf{Z}) \equiv \cup_{Z \in \mathbf{Z}} \operatorname{nb}_{\mathcal{H}}(Z)$.
Connected components. If there exists a path from a vertex $V$ to a vertex $W$ in graph $\mathcal{H}$ we say that $V$ and $W$ are connected. A connected component of $\mathcal{H}$ is a maximal subset of vertices $\mathbf{U}$ such that for all $V, W \in \mathbf{U}, V$ and $W$ are connected in $\mathcal{H}$ by a path that goes only through vertices in $\mathbf{U}$. For $\mathcal{H}=(\mathbf{V}, \mathbf{E})$ and $\mathbf{U} \subset \mathbf{V}, \partial_{\mathcal{H}} \mathbf{U}$ denotes the set of vertices in $\mathbf{V} \backslash \mathbf{U}$ which are adjacent to at least one vertex in $\mathbf{U}$. If moreover $Y \in \mathbf{V} \backslash \mathbf{U}$, then $\mathrm{cc}(\mathbf{U}, Y, \mathcal{H})$ will denote the connected component of $\mathcal{H}_{\mathbf{V} \backslash \mathbf{U}}$ which contains $Y$.
Vertex cuts. Consider an undirected graph $\mathcal{H}=(\mathbf{V}, \mathbf{E})$. Let $A, Y \in \mathbf{V}$ and $\mathbf{Z} \subset \mathbf{V}$ such that $\mathbf{Z} \cap\{A, Y\}=\emptyset$. We say that $\mathbf{Z}$ is an $A-Y$ cut or that $A$ and $Y$ are separated by $\mathbf{Z}$ if all paths between $A$ and $Y$ intersect a vertex in $\mathbf{Z}$. If $\mathbf{Z}$ is an $A-Y$ cut we write $A \perp_{\mathcal{H}} Y \mid \mathbf{Z} . \mathbf{Z}$ is a minimal $A-Y$ cut if it is an $A-Y$ cut and no proper subset of $\mathbf{Z}$ is an $A-Y$ cut. $\mathbf{Z}$ is a minimum $A-Y$ cut if it is an $A-Y$ cut and there exists no $A-Y$ cut with a cardinality smaller than the cardinality of $\mathbf{Z}$. Note that every minimum $A-Y$ cut is also minimal, but the reciprocal is false in general.
Lattices. A lattice $\mathcal{L}=(L, \unlhd)$ is a set $L$ together with a relation $\unlhd$ that is reflexive, anti-symmetric and transitive such that for all $a, b \in L$ there exists a greatest lower bound for $a, b$ in $L$, called the inf of $a, b$, and a smallest upper bound for $a, b$ in $L$, called the sup of $a, b$.

### 2.1.2 Directed graphs

Directed graphs. A directed graph $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ consists of a finite vertex (also called node) set $\mathbf{V}$ and a set of directed edges $\mathbf{E} \subset \mathbf{V} \times \mathbf{V}$. We represent a directed edge between two vertices $V, W$ by $V \rightarrow W$. Given a set of vertices $\mathbf{Z} \subset \mathbf{V}$ the induced subgraph $\mathcal{G}_{\mathbf{Z}}=\left(\mathbf{Z}, \mathbf{E}_{Z}\right)$ is defined as the graph obtained by considering only vertices in $\mathbf{Z}$ and edges between vertices in $\mathbf{Z}$. We will sometimes use the notation $\mathbf{V}(\mathcal{G})$ and $\mathbf{E}(\mathcal{G})$ to refer to the vertex and edge sets respectively of the directed graph $\mathcal{G}$.
Paths. We say that two vertices are adjacent if there is an edge between them. A path from a vertex $V$ to a vertex $W$ in graph $\mathcal{G}$ is a sequence of vertices $\left(V_{1}, \ldots, V_{j}\right)$ such that $V_{1}=V, V_{j}=W$ and $V_{i}$ and $V_{i+1}$ are adjacent in $\mathcal{G}$ for all $i \in\{1, \ldots, j-1\}$. $V$ and $W$ are the endpoints of the path. A path $\left(V_{1}, \ldots, V_{j}\right)$ is called directed or causal if $V_{i} \rightarrow V_{i+1}$ for all $i \in\{1, \ldots, j-1\}$.
Ancestry. If $V \rightarrow W$, then $V$ is a parent of $W$ and $W$ is a child of $V$. If there is a directed path from $V$ to $W$, then $V$ is an ancestor of $W$ and $W$ a descendant of $V$. We follow the convention that very vertex is an ancestor and a descendant of itself. The sets of parents, children, ancestors and descendants of $V$ in $\mathcal{G}$ are denoted by $\mathrm{pa}_{\mathcal{G}}(V), \operatorname{ch}_{\mathcal{G}}(V), \operatorname{an}_{\mathcal{G}}(V)$ and $\operatorname{de}_{\mathcal{G}}(V)$ respectively. The set of non-descendants of a vertex $V$ is defined as $\operatorname{nd}_{\mathcal{G}}(V) \equiv \mathbf{V} \backslash \operatorname{de}_{\mathcal{G}}(V)$. For a set of vertices $\mathbf{Z}$ we define $\operatorname{an}_{\mathcal{G}}(\mathbf{Z})=\cup_{Z \in \mathbf{Z}} \operatorname{an}_{\mathcal{G}}(Z)$.
Colliders and forks. If $\delta$ is a path on a directed graph $\mathcal{G}$, a vertex $V$ on $\delta$ is a collider on that path if $\delta$ contains a subpath $(U, V, W)$ such that $U \rightarrow V \leftarrow W$. A vertex $V$ is a fork on the path $\delta$ if $\delta$ contains a subpath $(U, V, W)$ such that $U \leftarrow V \rightarrow W$.
Directed cycles, DAGs. A directed cycle is a directed path from $V$ to $W$, together with the edge $W \rightarrow V$. A directed graph without directed cycles is called a directed acyclic graph (DAG).
d-separation (Verma and Pearl, 1990). Let $\mathcal{G}$ be a DAG with vertex set V. Let $\mathbf{U}, \mathbf{W}, \mathbf{Z}$ be distinct subsets of V. A path $\delta$ in $\mathcal{G}$ between $U \in \mathbf{U}$ and $W \in \mathbf{W}$ is blocked by $\mathbf{Z}$ if at least one of the following holds:

1. There exists a vertex on $\delta$ that is not a collider and is an element of $\mathbf{Z}$, or
2. There exists a vertex $C$ that is a collider on $\delta$ such that neither $C$ nor its descendants are elements of $\mathbf{Z}$.

Two sets of vertices $\mathbf{U}, \mathbf{W}$ are d-separated by $\mathbf{Z}$ in $\mathcal{G}$ if for any $U \in \mathbf{U}$ and $W \in \mathbf{W}$, all paths between $U$ and $W$ are blocked by $\mathbf{Z}$. If $\mathbf{U}, \mathbf{W}$ are d-separated by $\mathbf{Z}$ we write $\mathbf{U} \Perp_{\mathcal{G}} \mathbf{W} \mid \mathbf{Z}$.

Moral graph. Given a DAG $\mathcal{G}$ with vertex set $\mathbf{V}$, the associated moral graph $\mathcal{G}^{m}$ is an undirected graph with the same vertex set as $\mathcal{G}$ and an edge $U-V$ if any of the following hold in $\mathcal{G}: U \rightarrow V, V \rightarrow U$, or there exists a vertex $W$ such that $U \rightarrow W \leftarrow V$. Lauritzen (1996), Proposition 3.25 establishes that

$$
\mathbf{U} \Perp_{\mathcal{G}} \mathbf{W} \mid \mathbf{Z} \Leftrightarrow \mathbf{U} \perp_{\left\{\mathcal{G}_{\text {no }_{\mathcal{G}}(\mathbf{U} \cup \mathbf{W} \cup \mathbf{Z})}\right\}^{m}} \mathbf{W} \mid \mathbf{Z}
$$

# 2.2 Causal graphical models 

A Bayesian Network $\mathcal{M}(\mathcal{G})$ represented by a DAG $\mathcal{G}$ is a statistical model that identifies the vertex set $\mathbf{V}$ with a random vector and assumes that the law $P$ of $\mathbf{V}$ satisfies the Local Markov Property: $V \Perp \operatorname{nd}_{\mathcal{G}}(V) \mid \mathrm{pa}_{\mathcal{G}}(V)$ under $P$ for all $V \in \mathbf{V}$, where $A \Perp B \mid C$ stands for conditional independence of $A$ and $B$ given $C$. Assuming, as we will throughout, that $P$ admits a density $f$ with respect to some dominating measure, the Local Markov Property implies that

$$
f(\mathbf{v})=\prod_{V_{j} \in \mathbf{V}} f\left\{v_{j} \mid \mathrm{pa}_{\mathcal{G}}\left(v_{j}\right)\right\}
$$

where $\mathrm{pa}_{\mathcal{G}}\left(v_{j}\right)$ is the value taken by $\mathrm{pa}_{\mathcal{G}}\left(V_{j}\right)$ when $\mathbf{V}=\mathbf{v}$.
Throughout the paper we will assume a causal agnostic graphical model (Spirtes et al., 2000; Robins and Richardson, 2010) represented by a DAG $\mathcal{G}$. The model identifies the vertex set of $\mathcal{G}$ with a factual random vector $\mathbf{V} \equiv\left(V_{1}, \ldots, V_{s}\right)$ and assumes that: (i) the law $P$ of $\mathbf{V}$ follows model $\mathcal{M}(\mathcal{G})$ and (ii) for any $A \in \mathbf{V}, \mathbf{L} \subset \operatorname{nd}_{\mathcal{G}}(A)$ and $\pi(A \mid \mathbf{L})$ a conditional law for $A$ given $\mathbf{L}$, the intervention density $f_{\pi}(\mathbf{v})$ of the variables in the graph when, possibly contrary to fact, the value of $A$ is drawn from the law $\pi(A \mid \mathbf{L})$ is given by

$$
f_{\pi}(\mathbf{v})=\pi(a \mid \mathbf{l}) \prod_{V_{j} \in \mathbf{V} \backslash\{A\}} f\left\{v_{j} \mid \mathrm{pa}_{\mathcal{G}}\left(v_{j}\right)\right\}
$$

where $a$ and $\mathbf{l}$ are the values taken by $A$ and $\mathbf{L}$ when $\mathbf{V}$ is equal to $\mathbf{v}$. Formula (3) is known as the g-formula (Robins, 1986), the manipulated density formula (Scheines et al., 1998) or the truncated factorization formula (Pearl, 2000). The conditional law $\pi$ designates the, possibly random, policy or dynamic treatment regime. A non-random regime that assigns the value $d(\mathbf{L})$ to $A$ corresponds to the point mass conditional law $\pi(a \mid \mathbf{l})=I_{d(\mathbf{l})}(a)$. In particular, a constant function $d(\mathbf{L})=a$ corresponds to a non-random static regime that sets $A$ to $a$.

Associating a given vertex $Y \in \operatorname{de}_{\mathcal{G}}(A)$ with the outcome or reward of interest, the value of the policy $\pi$, denoted throughout as $\chi_{\pi}(P ; \mathcal{G})$, is defined as the mean of the outcome under the intervention law $f_{\pi}$. By the factorizations (2) and (3), the Radom-Nykodim theorem gives

$$
\chi_{\pi}(P ; \mathcal{G})=E_{P}\left\{\frac{\pi(A \mid \mathbf{L})}{f\left\{A \mid \mathrm{pa}_{\mathcal{G}}(A)\right\}} Y\right\}
$$

Furthermore, the Local Markov property implies that

$$
\begin{aligned}
\chi_{\pi}(P ; \mathcal{G}) & =\int y \pi(a \mid \mathbf{l}) f(y \mid a, \mathbf{l}, \mathrm{pa}) f(\mathbf{l}, \mathrm{pa}) d(y, a, \mathrm{pa}, \mathbf{l} \backslash \mathrm{pa}) \\
& =E_{P}\left(E_{\pi^{*}}\left[E_{P}\left\{Y \mid A, \mathrm{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \mid \mathrm{pa}_{\mathcal{G}}(A), \mathbf{L}\right]\right)
\end{aligned}
$$

where $E_{P}(\cdot \mid \cdot)$ stands for conditional mean under $P$ and $E_{\pi^{*}}(\cdot \mid \cdot)$ stands for conditional mean under the conditional law of $A$ given $\mathbf{L}$ and $\mathrm{pa}_{\mathcal{G}}(A)$ defined as $\pi^{*}\left\{A \mid \mathrm{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \equiv \pi(A \mid \mathbf{L})$.

In this article we study inference about $\chi_{\pi}(P ; \mathcal{G})$ when only a subset $\mathbf{N}$ of $\mathbf{V}$ is observable. The inferential problem is thus defined by the following three assumptions: (i) the law $P$ follows the Bayesian Network $\mathcal{M}(\mathcal{G})$, (ii) only the sub-vector $\mathbf{N}$ of $\mathbf{V}$ is observable on a random sample from the marginal law of $\mathbf{N}$ under $P$ and (iii) the parameter of interest is the functional $\chi_{\pi}(P ; \mathcal{G})$. We have motivated this inferential task with the causal agnostic model but we could as well have motivated it with any other existing causal graphical model in which the law $P$ of $\mathbf{V}$ is restricted only by the Local Markov Property and the parameter representing the value under the intervention $\pi$ coincides with the functional $\chi_{\pi}(P ; \mathcal{G})$. Two such models are the non-parametric structural equation model with independent errors (Pearl, 2000) and the finest fully randomized causally interpreted tree structured graph model (Robins, 1986).

Throughout the paper we will assume that both $A$ and $Y$ are observable, that $A$ is an ancestor of $Y$, and that we are interested in estimating the value of policies $\pi(A \mid \mathbf{L})$ that depend on a, possibly empty, vector $\mathbf{L}$ of observable

non-descendants of $A$. That is, we assume (i) $A \in \operatorname{an}_{\mathcal{G}}(Y)$, (ii) $\{A, Y\} \cup \mathbf{L} \subset \mathbf{N}$ and (iiii) $\mathbf{L} \subset \operatorname{nd}_{\mathcal{G}}(A)$. For ease of reference we refer to (i), (ii) and (iii) as the inclusion assumptions. In all the definitions and results that follow in the rest of the paper we will assume that that $\mathcal{G}$ is a DAG with vertex set $\mathbf{V}$, and that $(A, Y, \mathbf{L}, \mathbf{N})$ satisfy the inclusion assumptions. Moreover, to avoid distracting measure theoretic complications, we will assume throughout that $A$ takes values in a finite set $\mathcal{A}$.

# 3 Adjustment sets 

Shpitser et al. (2010) and Maathuis and Colombo (2015) gave the following definition of adjustment set for static regime. We add the appellative static to the name adjustment set to distinguish this set from adjustment sets for, possibly random, dynamic regimes that we will define subsequently.

Definition 1. A set $\mathbf{Z} \subset \mathbf{V} \backslash\{A, Y\}$ is a static adjustment set relative to $A, Y$ in $\mathcal{G}$ if for all fixed $a$, under all $P \in \mathcal{M}(\mathcal{G})$

$$
E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \operatorname{pa}_{\mathcal{G}}(A)\right\}\right]=E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{Z}\right\}\right] \quad \text { for all } y \in \mathbb{R}
$$

The definition implies that for a static adjustment set $\mathbf{Z}$, the value function $\chi_{\pi_{a}}(P ; \mathcal{G})$ of the non-random static regime $\pi_{a}(A) \equiv I_{a}(A)$ that sets $a$ to $A$ admits a representation as the iterated conditional expectation $E_{P}\left\{E_{P}(Y \mid A=a, \mathbf{Z})\right\}$. The back-door criterion (Pearl, 2000) is a well known graphical condition that is sufficient, but not necessary, for $\mathbf{Z}$ to be a static adjustment set. Shpitser et al. (2010) gave a necessary and sufficient graphical condition for $\mathbf{Z}$ to be a static adjustment set. van der Zander et al. (2019) provide an alternative, constructive, graphical characterization of static adjustment sets.

We now extend the preceding definition to accommodate, possibly random, $\mathbf{L}$-dependent policies.
Definition 2. Let $\mathbf{L} \subset \operatorname{nd}_{\mathcal{G}}(A)$. A set $\mathbf{Z} \subset \mathbf{V} \backslash\{A, Y\}$ is an $\mathbf{L}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if $\mathbf{L} \subset \mathbf{Z}$ and for all conditional laws $\pi(A \mid \mathbf{L})$ for $A$ given $\mathbf{L}$, all $P \in \mathcal{M}(\mathcal{G})$ and all $y \in \mathbb{R}$.

$$
E_{P}\left(E_{\pi^{*}}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right]\right)=E_{P}\left(E_{\pi_{\mathbf{Z}}^{*}}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \mathbf{Z}\right\} \mid \mathbf{Z}\right]\right)
$$

where $\pi_{\mathbf{Z}}^{*}(A \mid \mathbf{Z}) \equiv \pi(A \mid \mathbf{L})$ and, recall, $\pi^{*}\left\{A \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \equiv \pi(A \mid \mathbf{L})$.
Suppose that at the stage of planning a study aimed at estimating different $\mathbf{L}-$ dependent policies, and having postulated a causal graphical model, the investigator acknowledges that due to practical, ethical or cost reasons, she can only hope to observe a subset $\mathbf{N}$ of the variables in $\mathcal{G}$. Furthermore, suppose that $\mathbf{N}$ includes at least one $\mathbf{L}$ dynamic adjustment set $\mathbf{Z}$. She may then choose to measure, in addition to $A$ and $Y$, solely the variables $\mathbf{Z}$, as these variables suffice to identify the policy value $\chi_{\pi}(P ; \mathcal{G})$ with the functional

$$
\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G}) \equiv E_{P}\left[E_{\pi_{\mathbf{Z}}^{*}}\left\{E_{P}(Y \mid A, \mathbf{Z}) \mid \mathbf{Z}\right\}\right]
$$

and subsequently proceed to estimate $\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G})$ non-parametrically as further explained in Section 4. Note that this strategy effectively uses the causal graphical model solely as an aid to identify adjustment sets at the design stage, but for robustness against model misspecification, it avoids exploiting the restrictions implied by the Bayesian Network $\mathcal{M}(\mathcal{G})$ to either identify $\chi_{\pi}(P ; \mathcal{G})$ with a formula different from adjustment formula (4) or to improve efficiency in the estimation of the functionals $\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G})$.

The preceding formulation raises the following questions: (1) given a graph $\mathcal{G}$ and a subset $\mathbf{N}$ of its vertices, how can we tell if an $\mathbf{L}$ dynamic adjustment set that is a subset of $\mathbf{N}$ exists? and (2) if several different observable $\mathbf{L}$ dynamic adjustment sets exist, which one should one measure? Our goal is to answer these question assuming that the basis for comparing adjustment sets $\mathbf{Z}$ is the variance of the limiting distribution of the non-parametric estimators of $\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G})$. To formally study these problems, we start with the following definitions.

Definition 3. The pair $(\mathbf{L}, \mathbf{N})$ is said to be an admissible pair with respect to $A, Y$ in $\mathcal{G}$ if there exists an adjustment set $\mathbf{Z}$ with respect to $A, Y$ in $\mathcal{G}$ such that $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$.

Definition 4. An $\mathbf{L}$ dynamic adjustment set $\mathbf{Z}$ with respect to $A, Y$ in $\mathcal{G}$ that is a subset of $\mathbf{N}$ is said to be an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. An $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ is said to be minimal if no strict subset of $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. An $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ is said to be minimum if there exists no $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with cardinality strictly smaller than the cardinality of $\mathbf{Z}$.

Definition 5. $A n \mathbf{L}-\mathbf{N}$ static adjustment set $\mathbf{Z}$ with respect to $A, Y$ in $\mathcal{G}$ is a static adjustment set with respect to $A, Y$ in $\mathcal{G}$ that satisfies $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$. An $\mathbf{L}-\mathbf{N}$ static adjustment set $\mathbf{Z}$ is said to be minimal if no strict subset of $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set. $A n \mathbf{L}-\mathbf{N}$ static adjustment set $\mathbf{Z}$ is said to be minimum if there exists no $\mathbf{L}-\mathbf{N}$ static adjustment set of cardinality strictly smaller than the cardinality of $\mathbf{Z}$.

The following proposition establishes that the class of $\mathbf{L}-\mathbf{N}$ static (minimal, minimum) adjustment sets and the class of $\mathbf{L}-\mathbf{N}$ (minimal, minimum) dynamic adjustment sets coincide. Additionally, it establishes that minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets are subsets of the set of ancestors of $\{A, Y\} \cup \mathbf{L}$.

# Proposition 1. 

1. $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.
2. If $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ then $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$.
3. $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.
4. $\mathbf{Z}$ is a minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimum $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.

Part 1) of Proposition 1 strengthens Theorem 2 of Kuroki and Miyakawa (2003) which establishes that if $\mathbf{Z}$ satisfies the back-door criterion (Pearl, 2000) and $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$ then $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ non-random dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if by such adjustment sets we mean those that satisfy (4) for any point mass probability $\pi(A \mid \mathbf{L})=I_{d(\mathbf{L})}(A)$ and any given $d$.

Combining Part 1) of Proposition 1 and a result by van der Zander et al. (2019) we can also give an answer to the first question raised above. Specifically, there exists an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set if and only if there exists an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$, i.e. if and only if the pair $(\mathbf{L}, \mathbf{N})$ is admissible. van der Zander et al. (2019) gave the following necessary and sufficient graphical condition for the pair $(\mathbf{L}, \mathbf{N})$ to be admissible: the set $\left[\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}\right] \backslash \operatorname{forb}(A, Y, \mathcal{G})$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set, where the so-called forbidden set is defined as $\operatorname{forb}(A, Y, \mathcal{G}) \equiv \operatorname{de}_{\mathcal{G}}(\operatorname{cn}(A, Y, \mathcal{G})) \cup\{A\}$ with $\operatorname{cn}(A, Y, \mathcal{G})$ defined as the set of all vertices that lie on a causal path between a vertex in $A$ and $Y$ and are not equal to $A$. van der Zander et al. (2019) additionally provided a polynomial time algorithm to test this condition.

In addition to providing a graphical test of $(\mathbf{L}, \mathbf{N})$ admissibility, van der Zander et al. (2019) provided a constructive graphical characterization of $\mathbf{L}-\mathbf{N}$ static adjustment sets when these exist. Moreover, they provided a polynomial time algorithm to find one $\mathbf{L}-\mathbf{N}$ static adjustment set, one minimal $\mathbf{L}-\mathbf{N}$ static adjustment sets and one minimum $\mathbf{L}-\mathbf{N}$ static adjustment set and an algorithm with polynomial time latency to list all minimal $\mathbf{L}-\mathbf{N}$ static adjustment sets and all minimum $\mathbf{L}-\mathbf{N}$ static adjustment sets. Proposition 1 implies that the results of van der Zander et al. (2019) are equally applicable to find $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets.

## 4 Non-parametric estimation of a policy value

We begin this section highlighting the elements of the asymptotic theory for non-parametric estimators of $\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G})$ that are relevant to our derivations. An estimator $\widehat{\gamma}$ of a parameter $\gamma(P)$ based on $n$ independent identically distributed random variables $\mathbf{V}_{1}, \ldots, \mathbf{V}_{n}$ of $\mathbf{V}$ is said to be asymptotically linear at $P$ if there exists a random variable $\varphi_{P}(\mathbf{V})$, called the influence function of $\gamma(P)$ at $P$, which when $\mathbf{V} \sim P$, has mean zero and finite variance and is such that $n^{1 / 2}\{\widehat{\gamma}-\gamma(P)\}=n^{-1 / 2} \sum_{i=1}^{n} \varphi_{P}\left(\mathbf{V}_{i}\right)+o_{p}(1)$. By the Central Limit Theorem, for any asymptotically linear estimator $\widehat{\gamma}$, it holds that $n^{1 / 2}\{\widehat{\gamma}-\gamma(P)\}$ converges in distribution to a mean zero Normal distribution with variance $\operatorname{var}_{P}\left\{\varphi_{P}\left(\mathbf{V}_{i}\right)\right\}$. Given a collection of probability laws $\mathcal{P}$ for $\mathbf{V}$, an estimator of $\widehat{\gamma}$ of $\gamma(P)$ is said to be regular at one $P$ if its convergence to $\gamma(P)$ is locally uniform at $P$ in $\mathcal{P}$ (Van der Vaart, 2000).

It is well known that estimators of $\chi_{\pi, \mathbf{Z}}(P ; \mathcal{G})$ that are regular and asymptotically linear at all $P$ in any given model $\mathcal{P}$ that makes at most 'complexity' type assumptions on

$$
b(A, \mathbf{Z} ; P) \equiv E_{P}(Y \mid A, \mathbf{Z}) \quad \text { and } / \text { or } \quad f(A \mid \mathbf{Z})
$$

have the influence function $\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})$ given by

$$
\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G}) \equiv \frac{\pi(A \mid \mathbf{L})}{f(A \mid \mathbf{Z})}\{Y-b(A, \mathbf{Z} ; P)\}+E_{\pi_{\mathbf{Z}}^{\circ}}\{b(A, \mathbf{Z} ; P) \mid \mathbf{Z}\}-\chi_{\pi}(P, \mathcal{G})
$$

Here and throughout, for conciseness, we avoid writing the arguments $A$ and $Y$ in the function $\psi_{P, \pi}(\cdot, P)$. Examples of complexity type assumptions are the assumptions that the functions $b(A, \mathbf{Z} ; P)$ and/or $f(A \mid \mathbf{Z})$ belong to some smooth function class such as a Holder ball, or to a function class with a Rademacher complexity that satisfies certain bounds. Examples of estimation strategies that make complexity type assumptions include: the inverse probability weighted estimator $\widetilde{\chi}_{\pi, I P W}=\mathbb{P}_{n}\left\{\widehat{f}(A \mid \mathbf{Z})^{-1} \pi(A \mid \mathbf{L}) Y\right\}$, where $\widehat{f}(A \mid Z)$ is a non-parametric smoothing type, e.g. series or kernel based, estimator of $f(A \mid \mathbf{Z})$ (Hirano et al., 2003), the outcome regression estimator $\mathbb{P}_{n}\left[E_{\pi_{\mathbf{Z}}}^{*}\{\widehat{b}(A, \mathbf{Z}) \mid \mathbf{Z}\}\right]$ where $\widehat{b}$ is a non-parametric smoothing type estimator of $b$ (Hahn, 1998) and the doublyrobust estimator (Van der Laan and Robins, 2003; Dudík et al., 2015; Chernozhukov et al., 2018; Smucler et al., 2019) with both $f(A \mid \mathbf{Z})$ and $b(A, \mathbf{Z})$ estimated via smoothing techniques. Note that models that only place complexity type assumptions on $f(A \mid \mathbf{Z})$ and/or $b(A, \mathbf{Z})$, ignore any restriction that could be possibly implied on the law of $(A, \mathbf{Z}, Y)$ by the Bayesian Network $\mathcal{M}(\mathcal{G})$. We will refer to estimators that are regular and asymptotically linear with influence function $\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})$ defined in (5) as non-parametric estimators and, for brevity, we will designate them as NP-Z estimators. It follows from the discussion above that all NP-Z estimators $\widetilde{\chi}_{\pi, \mathbf{Z}}$ satisfy that $\sqrt{n}\left\{\widetilde{\chi}_{\pi, \mathbf{Z}}-\chi_{\pi}(P ; \mathcal{G})\right\}$ converges in distribution to $N\left\{0, \sigma_{\pi, \mathbf{Z}}^{2}(P)\right\}$ where $\sigma_{\pi, \mathbf{Z}}^{2}(P) \equiv \operatorname{var}_{P}\left\{\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})\right\}$.

On the class of static adjustment sets we define the preorder (a reflexive and transitive binary relation) $\preceq$ as follows

$$
\mathbf{Z}^{\prime} \preceq \mathbf{Z} \text { if and only if } \sigma_{\pi, \mathbf{Z}^{\prime}}^{2}(P) \leq \sigma_{\pi, \mathbf{Z}}^{2}(P) \text { for all } P \in \mathcal{M}(\mathcal{G}) \text { and all } \pi(A \mid \mathbf{L})=I_{a}(A) \text { for some } a
$$

and on the class of $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets we define the preorder $\preceq_{\mathbf{L}}$ as follows

$$
\mathbf{Z}^{\prime} \preceq_{\mathbf{L}} \mathbf{Z} \text { if and only if } \sigma_{\pi, \mathbf{Z}^{\prime}}^{2}(P) \leq \sigma_{\pi, \mathbf{Z}}^{2}(P) \text { for all } P \in \mathcal{M}(\mathcal{G}) \text { and all } \pi(A \mid \mathbf{L})
$$

Rotnitzky and Smucler (2019) showed that $\preceq$ is not a total preorder because there exist graphs $\mathcal{G}$ and vertices $A, Y$ such that for some static adjustment sets relative to $A$ and $Y$ in $\mathcal{G}$, say $\mathbf{Z}^{\prime}$ and $\mathbf{Z}$, it holds that $\sigma_{\pi, \mathbf{Z}}^{2}(P) \leq$ $\sigma_{\pi, \mathbf{Z}^{\prime}}^{2}(P)$ for some $P \in \mathcal{M}(\mathcal{G})$ but $\sigma_{\pi, \mathbf{Z}}^{2}\left(P^{\prime}\right)>\sigma_{\pi, \mathbf{Z}^{\prime}}^{2}\left(P^{\prime}\right)$ for some other $P^{\prime} \in \mathcal{M}(\mathcal{G})$. A similar negative result was derived earlier by Henckel et al. (2019) for comparing the variances of ordinary least squares estimators of the coefficient of $A$ in the regression of $Y$ with covariates $A$ and the adjustment set in question under the assumption that the causal graphical model is linear, that is, that $\mathbf{V}=\left(V_{1}, \ldots, V_{s}\right)$ satisfies $V_{i}=\sum_{V_{j} \in \mathrm{pag}\left(V_{i}\right)} \alpha_{i j} V_{j}+\varepsilon_{i}$, for $i \in\{1, \ldots, s\}$, where $\alpha_{i j} \in \mathbb{R}$ and $\varepsilon_{1}, \ldots, \varepsilon_{s}$ are jointly independent random variables with zero mean and finite variance. However, Henckel et al. (2019) gave two graphical criteria for ordering certain pairs of static adjustment sets in the aforementioned linear setting. Rotnitzky and Smucler (2019) proved that the same graphical criterion applies in the non-parametric setting. The preorder $\preceq_{\mathbf{L}}$ is not a total preorder because $\mathbf{Z}^{\prime} \preceq_{\mathbf{L}} \mathbf{Z}$ for some $\mathbf{L}$ implies $\mathbf{Z}^{\prime} \preceq \mathbf{Z}$. Our first result, formalized in Lemmas 1 and 2, and in Proposition 2 in the next section extends the graphical criteria of Henckel et al. (2019) and Rotnitzky and Smucler (2019) to $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets.

Henckel et al. (2019) and Rotnitzky and Smucler (2019) in the linear and non-parametric settings respectively showed that a globally optimal adjustment set $\mathbf{O}$ satisfying $\mathbf{O} \preceq \mathbf{Z}$ for any other static adjustment set $\mathbf{Z}$ always exists and they provided a graphical characterization of it. They also showed, by exhibiting counterexamples, that in graphs with hidden variables which admit observable static adjustment sets there may not exist an optimal static adjustment set among the observable ones. Because static interventions are a special of dynamic interventions with $\mathbf{L}=\emptyset$, the same assertions hold for $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets. In Section 6 we will provide a sufficient graphical condition for a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set to exist in graphs with hidden variables. Subsequently, we will demonstrate that for $(\mathbf{L}, \mathbf{N})$ admissible pairs, an optimal adjustment set always exists among minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets and we will provide a graphical characterization of it. Our results extend the results of Rotnitzky and Smucler (2019) who gave a graphical characterization of the minimal optimal static adjustment set in graphs without hidden variables. Finally, we will show that, for $(\mathbf{L}, \mathbf{N})$ admissible pairs, in the class of minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets there always exists an optimal one and we will provide a graphical characterization of it. Our results can be applied, in particular, to determine the optimal static adjustment set among the minimum static adjustment sets. To our knowledge neither the proof of the existence of an optimal minimum static or $\mathbf{L}-\mathbf{N}$ dynamic adjustment set nor a graphical characterization of it are available in the existing literature.

# 5 Comparing dynamic adjustment sets 

We start this section by establishing two Lemmas which entail the possibility of ordering certain pairs of $\mathbf{L}-$ N dynamic adjustment sets as indicated in the preceding section. These Lemmas extend Lemmas 1 and 2 of

Rotnitzky and Smucler (2019) from static to $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets. Throughout this section all results assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Also, all adjustment sets, static or dynamic are with respect to $A, Y$ in $\mathcal{G}$.
Lemma 1 (Supplementation with precision variables). Let $\mathbf{B}$ be an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set and let $\mathbf{G} \subset \mathbf{V}$ satisfy

$$
A \Perp_{\mathcal{G}} \mathbf{G} \mid \mathbf{B}
$$

Then $\mathbf{G} \cup \mathbf{B}$ is also an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set and for any $\pi(A \mid \mathbf{L})$ and all $P \in \mathcal{M}(\mathcal{G})$

$$
\sigma_{\pi, \mathbf{B}}^{2}(P)-\sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P)=\mathbf{1}^{\top} \operatorname{var}_{P}(\mathbf{S}) \mathbf{1} \geq 0
$$

where $\mathbf{S}=\left(S_{a}\right)_{a \in \mathcal{A}}$,

$$
S_{a} \equiv\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}
$$

and $\mathbf{1}$ is a vector of ones with dimension equal to $\# \mathcal{A}$. Moreover,

$$
\begin{aligned}
& \operatorname{var}_{P}\left(S_{a}\right)=E_{P}\left\{\operatorname{var}_{P}[b(a, \mathbf{G}, \mathbf{B} ; P) \mid \mathbf{B}] \pi(a \mid \mathbf{L})^{2}\left[\frac{1}{f(a \mid \mathbf{B})}-1\right]\right\} \\
& \operatorname{cov}_{P}\left(S_{a}, S_{a^{\prime}}\right)=-E_{P}\left[\pi(a \mid \mathbf{L}) \pi\left(a^{\prime} \mid \mathbf{L}\right) \operatorname{cov}_{P}\{b(a, \mathbf{G}, \mathbf{B} ; P), b\left(a^{\prime}, \mathbf{G}, \mathbf{B} ; P\right) \mid \mathbf{B}\}\right]
\end{aligned}
$$

Lemma 2 (Deletion of overadjustment variables). Let $\mathbf{G} \cup \mathbf{B}$ be an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with $\mathbf{G}$ and $\mathbf{B}$ disjoint and suppose

$$
\mathbf{L} \subset \mathbf{G} \quad \text { and } \quad Y \Perp_{\mathcal{G}} \mathbf{B} \mid \mathbf{G}, A
$$

Then $\mathbf{G}$ is also an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set and for any $\pi(A \mid \mathbf{L})$ and all $P \in \mathcal{M}(\mathcal{G})$

$$
\begin{aligned}
& \sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P)-\sigma_{\pi, \mathbf{G}}^{2}(P)= \\
& \sum_{a \in \mathcal{A}}\left(E_{P}\left[\pi^{2}(a \mid \mathbf{L}) f(a \mid \mathbf{G}) \operatorname{var}_{P}\left(Y \mid A=a, \mathbf{G}\right) \operatorname{var}_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A=a, \mathbf{G}\right\}\right]\right) \geq 0
\end{aligned}
$$

A straightforward consequence of Lemmas 1 and 2 is Proposition 2 below, which shows that the graphical criteria to compare certain pairs of static adjustment sets in Henckel et al. (2019) and Rotnitzky and Smucler (2019) is also valid for comparing $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets.
Proposition 2. Suppose $\mathbf{G}$ and $\mathbf{B}$ are two $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets such that

$$
A \Perp_{\mathcal{G}} \mathbf{G} \backslash \mathbf{B} \mid \mathbf{B} \quad \text { and } \quad Y \Perp_{\mathcal{G}} \mathbf{B} \backslash \mathbf{G} \mid \mathbf{G}, A
$$

Then, for any $\pi(A \mid \mathbf{L})$ and all $P \in \mathcal{M}(\mathcal{G})$

$$
\begin{aligned}
& \sigma_{\pi, \mathbf{B}}^{2}(P)-\sigma_{\pi, \mathbf{G}}^{2}(P)=\mathbf{1}^{\top} \operatorname{var}_{P}(\mathbf{S}) \mathbf{1}+ \\
& \sum_{a \in \mathcal{A}}\left(E_{P}\left[\pi^{2}(a \mid \mathbf{L}) f(a \mid \mathbf{G}) \operatorname{var}_{P}\left(Y \mid A=a, \mathbf{G}\right) \operatorname{var}_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A=a, \mathbf{G}\right\}\right]\right) \geq 0
\end{aligned}
$$

where $\mathbf{S}$ is defined as in Lemma 1.
Proof. Write $\sigma_{\pi, \mathbf{B}}^{2}-\sigma_{\pi, \mathbf{G}}^{2}=\sigma_{\pi, \mathbf{B}}^{2}-\sigma_{\pi, \mathbf{B} \cup(\mathbf{G} \backslash \mathbf{B})}^{2}+\sigma_{\pi, \mathbf{G} \cup(\mathbf{B} \backslash \mathbf{G})}^{2}-\sigma_{\pi, \mathbf{G}}^{2}$ and apply Lemmas 1 and 2.
Define

$$
\mathbf{O}(A, Y, \mathcal{G}) \equiv \operatorname{pa}_{\mathcal{G}}(\operatorname{cn}(A, Y, \mathcal{G})) \backslash \operatorname{forb}(A, Y, \mathcal{G}) \quad \text { and } \quad \mathbf{O}(A, Y, \mathbf{L}, \mathcal{G}) \equiv \mathbf{O}(A, Y, \mathcal{G}) \cup \mathbf{L}
$$

Henckel et al. (2019) and Rotnitzky and Smucler (2019) in the linear setting and the non-parametric setting respectively showed that $\mathbf{O}(A, Y, \mathcal{G})$ is the globally optimal static adjustment set in graphs with no hidden variables. We will now establish that the set $\mathbf{O}(A, Y, \mathbf{L}, \mathcal{G})$ is a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set in graphs with no hidden variables, i.e. when $\mathbf{N}=\mathbf{V}$.
Proposition 3. Suppose that $\mathbf{N}=\mathbf{V}$ where $\mathbf{V}$ is the set of all the vertices in $\mathcal{G}$. Then $\mathbf{O} \equiv \mathbf{O}(A, Y, \mathbf{L}, \mathcal{G})$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set and for any other $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ it holds that

$$
A \Perp_{\mathcal{G}} \mathbf{O} \backslash \mathbf{Z} \mid \mathbf{Z} \quad \text { and } \quad Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O} \mid A, \mathbf{O}
$$

Consequently, $\mathbf{O}(A, Y, \mathbf{L}, \mathcal{G}) \preceq_{\mathbf{L}} \mathbf{Z}$ for any $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$.
In Section 6 we provide an alternative graphical characterization of $\mathbf{O}(A, Y, \mathbf{L}, \mathcal{G})$ as the set of neighbors of $Y$ in a suitably constructed undirected graph.

# 6 Graphical characterizations 

Assuming that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$, in this section we will define an undirected graph which will be the basis for our graphical criteria for characterizing the globally optimal (when it exists), the optimal minimal and the optimal minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets. The construction of this new graph relies on a result in van der Zander et al. (2019) which, for completeness, we state next before the definition of the aforementioned undirected graph. In what follows, following van der Zander et al. (2019), we define the proper back-door graph $\mathcal{G}^{p b d}(A, Y)$ as the DAG formed by removing from $\mathcal{G}$ the first edge of every causal path from $A$ to $Y$.

Theorem 1 (Theorem 1 from van der Zander et al. (2019)). The set $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if (1) $Y \Perp_{\mathcal{G}^{p b d}(A, Y)} A \mid \mathbf{Z}$, (2) $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$, and (3) $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$.

Definition 6. Let

$$
\mathcal{H}^{0}(A, Y, \mathbf{L}, \mathcal{G}) \equiv\left\{\mathcal{G}_{\mathrm{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})}^{p b d}(A, Y)\right\}^{m}
$$

and

$$
\operatorname{ignore}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G}) \equiv\left\{\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \backslash\{A, Y\}\right\} \cap\left\{\mathbf{N}^{c} \cup \operatorname{forb}(A, Y, \mathcal{G})\right\}
$$

The non-parametric adjustment efficiency graph associated with $A, Y, \mathbf{L}, \mathbf{N}$ in $\mathcal{G}$ is defined as the undirected graph, denoted with $\mathcal{H}^{1}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$, constructed from $\mathcal{H}^{0}(A, Y, \mathbf{L}, \mathcal{G})$ by (1) removing all vertices in $\operatorname{ignore}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$, (2) adding an edge between any pair of remaining vertices if they were connected in $\mathcal{H}^{0}(A, Y, \mathbf{L}, \mathcal{G})$ by a path with vertices in $\operatorname{ignore}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ and (3) adding an edge: (i) between $A$ and each vertex in $\mathbf{L}$ and, (ii) between $Y$ and each vertex in $\mathbf{L}$.

For conciseness, unless unclear, throughout we will drop $\mathbf{L}$ and $\mathbf{N}$ from ignore $(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ and we will also write $\mathcal{H}^{0}$ and $\mathcal{H}^{1}$ instead of $\mathcal{H}^{0}(A, Y, \mathbf{L}, \mathcal{G})$ and $\mathcal{H}^{1}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$.

Textor and Liskiewicz (2011) used the undirected graph $\mathcal{H}^{0}$ as the basis for a graphical characterization of minimal static adjustment sets when $\mathbf{N}=\mathbf{V}$. We will show later that our construction of $\mathcal{H}^{1}$ entails, among other characterizations, a graphical criterion that extends the one in Textor and Liskiewicz (2011) to minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets and sets $\mathbf{N}$ that can be a strict subset of $\mathbf{V}$. In addition, it entails the graphical characterization of a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set for $(\mathbf{L}, \mathbf{N})$ admissible pairs when $\mathbf{N} \subset$ $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. The heuristics behind the construction of $\mathcal{H}^{1}$ are as follows. If $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ then any $\mathbf{L}-\mathbf{N}$ dynamic adjustment set must be a subset of $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. On the other hand, even if $\mathbf{N} \not \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$, Proposition 1 established that all minimal, and consequently all minimum, $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets are subsets of $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Now, suppose that $\mathbf{C}$ satisfies $\mathbf{L} \subset \mathbf{C} \subset \mathbf{N}, \mathbf{C} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$ and $\mathbf{C}$ is an $A-Y$ cut in the moralized graph $\mathcal{H}^{0}$ of the proper back-door graph $\mathcal{G}_{\mathrm{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})}^{p b d}(A, Y)$. By Theorem 1, the moralization property (1) and Proposition 1, the cut $\mathbf{C}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set and is a subset of $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Next note that variables in ignore $(A, Y, \mathcal{G})$ are either hidden or forbidden and hence cannot be part of any $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. Steps 1 and 2 of Definition 6 are similar in spirit to a latent projection (Verma and Pearl, 1990; Richardson et al., 2017) on $\mathbf{V}\left(\mathcal{H}^{0}\right) \backslash \operatorname{ignore}(A, Y, \mathcal{G})$. The so called latent projection operation in DAGs marginalizes DAGs over hidden variables while preserving d-separation relations between the observable variables. Lemma 3 below establishes that $\mathcal{H}^{1}$ preserves the separations in $\mathcal{H}^{0}$ between variables that lie in $\mathbf{V}\left(\mathcal{H}^{1}\right)$, the vertex set of $\mathcal{H}^{1}$, when the set of variables that are conditioned on contains $\mathbf{L}$.

Lemma 3. Let $U, V \in \mathbf{V}\left(\mathcal{H}^{1}\right)$ and $\mathbf{L} \subset \mathbf{W} \subset \mathbf{V}\left(\mathcal{H}^{1}\right)$. Then $U \perp_{\mathcal{H}^{0}} V \mid \mathbf{W}$ if and only if $U \perp_{\mathcal{H}^{1}} V \mid \mathbf{W}$.
Next we note that steps 1 and 2 of Definition 6 also ensure that $A-Y$ cuts in $\mathcal{H}^{1}$ intersect neither forb $(A, Y, \mathcal{G})$ nor $\mathbf{N}^{c}$, while step 3 ensures that all $A-Y$ cuts in $\mathcal{H}^{1}$ are supersets of $\mathbf{L}$. This, together with the preceding discussion, suggests that $A-Y$ cuts in $\mathcal{H}^{1}$ should coincide with $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets in $\mathcal{G}$. Proposition 4 below establishes that this is indeed true when $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$.

## Proposition 4.

1. If $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$ then $A$ and $Y$ are not adjacent in $\mathcal{H}^{1}$.
2. If $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$ then $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$.
3. If $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ then $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$.

4. $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimal $A-Y$ cut in $\mathcal{H}^{1}$.
5. $\mathbf{Z}$ is a minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimum $A-Y$ cut in $\mathcal{H}^{1}$.

Next, we provide several examples illustrating the construction of $\mathcal{H}^{1}$. It is easy to check that in each of our examples $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$.
![img-0.jpeg](img-0.jpeg)

Figure 1: Example of the construction of the non-parametric adjustment efficiency graph, where $\mathbf{L}=\{L\}$ and $\mathbf{N}=\{A, M, L, F, Y\}$. Here $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\mathbf{V}(\mathcal{G})$, $\operatorname{forb}(A, Y, \mathcal{G})=\{A, Y, M\}$ and ignore $(A, Y, \mathcal{G})=\{M, U\}$.
![img-1.jpeg](img-1.jpeg)

Figure 2: Example of the construction of the non-parametric adjustment efficiency graph, where $\mathbf{L}=\emptyset$ and $\mathbf{N}=\mathbf{V}(\mathcal{G})$. Here $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\mathbf{V}(\mathcal{G})$, $\operatorname{forb}(A, Y, \mathcal{G})=\{A, Y\}$ and ignore $(A, Y, \mathcal{G})=\emptyset$.
![img-2.jpeg](img-2.jpeg)

Figure 3: Example of the construction of the non-parametric adjustment efficiency graph, where $\mathbf{L}=\emptyset$ and $\mathbf{N}=\left\{A, Y, Z_{1}, Z_{2}\right\}$. Here $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\left\{A, Y, Z_{1}, U\right\}$, forb $(A, Y, \mathcal{G})=\{A, Y\}$ and ignore $(A, Y, \mathcal{G})=\{U\}$.

![img-3.jpeg](img-3.jpeg)

Figure 4: Example of the construction of the non-parametric adjustment efficiency graph, where $\mathbf{L}=\{L\}$ and $\mathbf{N}=\{A, Y, L, F\}$. Here $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\{A, Y, L, U\}$, $\operatorname{forb}(A, Y, \mathcal{G})=\{A, Y\}$ and ignore $(A, Y, \mathcal{G})=\{U\}$.

We will now define a binary relation in the class of $A-Y$ cuts in $\mathcal{H}^{1}$ that will aid us in the construction of our proposed graphical criteria for characterizing optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets. For $A-Y$ cuts $\mathbf{Z}_{1}, \mathbf{Z}_{2}$ in $\mathcal{H}^{1}$, we define $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$ if and only if $Y \perp_{\mathcal{H}^{1}} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid \mathbf{Z}_{1}$ and $A \perp_{\mathcal{H}^{1}} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}$. For example, in Figure 2 b), $\mathbf{Z}_{1}=\left\{W_{1}, W_{2}, W_{3}\right\}$ and $\mathbf{Z}_{2}=\{T\}$ are $A-Y$ cuts and $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$. Halin (1993) showed $\unlhd_{\mathcal{H}^{1}}$ is a partial order in the class of minimal (minimum) $A-Y$ cuts in $\mathcal{H}^{1}$.

Our next proposition and Proposition 2 entail that $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$ implies $\mathbf{Z}_{1} \preceq_{\mathbf{L}} \mathbf{Z}_{2}$ for $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets $\mathbf{Z}_{1}, \mathbf{Z}_{2}$ that are subsets of $\mathbf{V}\left(\mathcal{H}^{1}\right)$.

Proposition 5. If $\mathbf{Z}_{1}$ and $\mathbf{Z}_{2}$ are $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets with respect to $A, Y$ in $\mathcal{G}$ such that $\mathbf{Z}_{1}, \mathbf{Z}_{2} \subset$ $\mathbf{V}\left(\mathcal{H}^{1}\right)$ and $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$, then

$$
Y \Perp_{\mathcal{G}} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid A, \mathbf{Z}_{1}
$$

and

$$
A \Perp_{\mathcal{G}} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}
$$

Theorems 1 and 2 of Halin (1993) imply that the set of all minimal (minimum) $A-Y$ cuts in $\mathcal{H}^{1}$ are lattices with respect to $\unlhd_{\mathcal{H}^{1}}$ with the infimum between two minimal (minimum) $A-Y$ cuts in $\mathcal{H}^{1}$ given by

$$
\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2} \equiv \partial_{\mathcal{H}^{1}}\left\{\operatorname{cc}\left(\mathbf{Z}_{1} \cup \mathbf{Z}_{2}, Y, \mathcal{H}^{1}\right)\right\}
$$

which is a subset of $\mathbf{Z}_{1} \cup \mathbf{Z}_{2}$. This result, together with Propositions 2, 4 and 5, entails the following Proposition.
Proposition 6. Assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Then, the set of all minimal (minimum) $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets is a lattice with respect to $\unlhd_{\mathcal{H}^{1}}$. Specifically, if $\mathbf{Z}_{1}$ and $\mathbf{Z}_{2}$ are minimal (minimum) $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets, then $\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2}$ is a minimal (minimum) $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. Furthermore,

$$
\left(\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2}\right) \preceq_{\mathbf{L}} \mathbf{Z}_{1} \text { and }\left(\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2}\right) \preceq_{\mathbf{L}} \mathbf{Z}_{2}
$$

Rotnitzky and Smucler (2019) showed that $\preceq$ is not a total preorder in the class of minimal static adjustment sets (see their Example 2). This, implies that $\preceq_{\mathbf{L}}$ is not a total preorder. Nevertheless, Proposition 6 implies that given two minimal (minimum) $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets $\mathbf{Z}_{1}$ and $\mathbf{Z}_{2}$ there exists another one, namely $\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2}$, included in their union which satisfies (8). The set $\mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2}$ thus yields an NP-Z estimator of $\chi_{\pi}(P ; \mathcal{G})$ with variance smaller than or equal to the variance of the NP-Z estimators of $\chi_{\pi}(P ; \mathcal{G})$ that adjust for $\mathbf{Z}_{1}$ or for $\mathbf{Z}_{2}$, under any $P \in \mathcal{M}(\mathcal{G})$.

Next, we define the following sets which are our candidates for the optimal, optimal minimal and optimal minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets respectively,

$$
\mathbf{O}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G}) \equiv \operatorname{nb}_{\mathcal{H}^{1}}(Y), \mathbf{O}_{\min }(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G}) \equiv \partial_{\mathcal{H}^{1}}\left\{\operatorname{cc}\left(\operatorname{nb}_{\mathcal{H}^{1}}(Y), A, \mathcal{G}\right)\right\}
$$

and for $\mathcal{C}_{\mathcal{H}^{1}}^{*}(A, Y) \equiv\left\{\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{l}\right\}$ the class of all minimum $A-Y$ cuts in $\mathcal{H}^{1}$, we define

$$
\mathbf{O}_{m}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G}) \equiv \mathbf{Z}_{1} \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{2} \wedge_{\mathcal{H}^{1}} \cdots \wedge_{\mathcal{H}^{1}} \mathbf{Z}_{l}
$$

For brevity henceforth we will write $\mathbf{O}, \mathbf{O}_{\text {min }}$ and $\mathbf{O}_{m}$ instead of $\mathbf{O}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G}), \mathbf{O}_{\text {min }}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ and $\mathbf{O}_{m}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ respectively. The set $\mathbf{O}$ is comprised of vertices adjacent to $Y$ in $\mathcal{H}^{1}$ and $\mathbf{O}_{\text {min }}$ is the set of vertices in $\mathbf{O}$ that have at least one path to $A$ in $\mathcal{H}^{1}$ that does not intersect any other vertices of $\mathbf{O}$. It can be shown that if $\mathbf{L}=\emptyset$ and $\mathbf{N}=\mathbf{V}$ then $\mathbf{O}=\operatorname{pa}_{\mathcal{G}}(\operatorname{cn}(A, Y, \mathcal{G})) \backslash \operatorname{forb}_{\mathcal{G}}(A, Y, \mathcal{G})$ and $\mathbf{O}_{\text {min }}$ is equal to the smallest subset of $\mathbf{O}$ that satisfies $A \Perp_{\mathcal{G}} \mathbf{O} \backslash \mathbf{O}_{\text {min }} \mid \mathbf{O}_{\text {min }}$. Thus, our definitions of $\mathbf{O}$ and $\mathbf{O}_{\text {min }}$ coincide with the ones in Rotnitzky and Smucler (2019) in the special case in which $\mathbf{L}=\emptyset$ and $\mathbf{N}=\mathbf{V}$. If $\mathbf{N}=\mathbf{V}$, it can be shown that $\mathbf{O}(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ coincides with $\mathbf{O}(A, Y, \mathbf{L}, \mathcal{G})$ as defined in Section 5.

As for $\mathbf{O}_{m}$, we note that there are graphs for which the number of minimum $A-Y$ cuts is exponential in the number of vertices in the graph, yet although $\mathbf{O}_{m}$ is the infimum over all minimum $A-Y$ cuts, its computation does not require enumeration of all the cuts. In fact, in Section 7 we provide a polynomial time algorithm to compute $\mathbf{O}_{m}$. We also provide a polynomial time algorithm to compute $\mathbf{O}_{\text {min }}$. On the other hand, one can trivially compute $\mathbf{O}$ in polynomial time by checking which variables are neighbors of $Y$ in $\mathcal{H}^{1}$. The following Theorem establishes that when $(\mathbf{L}, \mathbf{N})$ is an admissible pair, $\mathbf{O}_{\min }$ and $\mathbf{O}_{m}$ are the optimal minimal and minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets respectively. In addition $\mathbf{O}$ is a globally optimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set provided $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ or $\mathbf{N}=\mathbf{V}$.
Theorem 2. Assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Then

1. $\mathbf{O}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$. In addition, if $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ or if $\mathbf{N}=\mathbf{V}$, then for any other $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ it holds that

$$
Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O} \mid A, \mathbf{O} \quad \text { and } \quad A \Perp_{\mathcal{G}} \mathbf{O} \backslash \mathbf{Z} \mid \mathbf{Z}
$$

Consequently $\mathbf{O} \preceq_{\mathbf{L}} \mathbf{Z}$.
2. $\mathbf{O}_{\text {min }}$ is a minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$. In addition, for any other minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ it holds that

$$
Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O}_{\text {min }} \mid A, \mathbf{O}_{\text {min }} \quad \text { and } \quad A \Perp_{\mathcal{G}} \mathbf{O}_{\text {min }} \backslash \mathbf{Z} \mid \mathbf{Z}
$$

Consequently $\mathbf{O}_{\text {min }} \preceq_{\mathbf{L}} \mathbf{Z}$.
3. $\mathbf{O}_{m}$ is a minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$. In addition, for any other minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ it holds that

$$
Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O}_{m} \mid A, \mathbf{O}_{m} \quad \text { and } \quad A \Perp_{\mathcal{G}} \mathbf{O}_{m} \backslash \mathbf{Z} \mid \mathbf{Z}
$$

Consequently $\mathbf{O}_{m} \preceq_{\mathbf{L}} \mathbf{Z}$.
Example 1. Consider the graphs in Figure 1. There is only one $A-Y$ cut in $\mathcal{H}^{1}$ in Figure 1 c). Thus, in this case, $\mathbf{O}=\mathbf{O}_{\text {min }}=\mathbf{O}_{m}=\{L, F\}$.
![img-4.jpeg](img-4.jpeg)

Figure 5: Example of the construction of the non-parametric adjustment efficiency graph, where $\mathbf{L}=\emptyset$ and $\mathbf{N}=\mathbf{V}$. Here, $K>2$, and the $\cdots$ between $W_{2}$ and $W_{K}$ stand for the same pattern repeating itself. Thus, in $\mathcal{G}$, all vertices $W_{i}, i=1, \ldots, K$ are parents of $T$ and of $Y$. In $\mathcal{H}^{0}=\mathcal{H}^{1}$ all vertices $W_{i}, i=1, \ldots, K$ are adjacent to $T$, to $Y$ and to all $W_{j}, j=1, \ldots, K+1, j \neq i$. In this example $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\mathbf{V}$, $\operatorname{forb}(A, Y, \mathcal{G})=\{A, Y\}$ and $\operatorname{ignore}(A, Y, \mathcal{G})=\emptyset$.

Example 2. Note that the DAG in Figure 5 a) contains as a special case, when $K=3$, the DAG in Figure 2 a). In $\mathcal{H}^{1}$ in Figure 5 b), the neighbors of $Y$ are $W_{1}, \ldots, W_{K+1}$ and thus $\mathbf{O}=\left\{W_{1}, \ldots, W_{K+1}\right\}$. Of the neighbors of $Y$ in $\mathcal{H}^{1}$, only $W_{1}, \ldots, W_{K}$ have paths to $A$ that don't intersect other neighbors of $Y$. Thus $\mathbf{O}_{\text {min }}=\left\{W_{1}, \ldots, W_{K}\right\}$. There is only one minimum $A-Y$ cut in $\mathcal{H}^{1}$ and it is given by $\{T\}$. Thus $\mathbf{O}_{m}=\{T\}$. For a large $K$, this example shows that the optimal minimum $\mathbf{L}-\mathbf{N}$ dynamic adjustment set may have a much smaller cardinality, in this case cardinality 1, than the optimal minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set, which in this case has cardinality $K$. It can be shown that in this example $\mathbf{O}_{m}$ can be much less efficient than $\mathbf{O}_{\text {min }}$, and in turn $\mathbf{O}_{\text {min }}$ can be much less efficient than $\mathbf{O}$. Informally, $\mathbf{O}_{m}$ will be much less efficient than $\mathbf{O}_{\text {min }}$ when in Figure 5 a), the associations encoded in the green and red arrows are strong and the associations encoded in the blue arrows are weak. $\mathbf{O}_{\text {min }}$ will be much less efficient than $\mathbf{O}$ when the associations encoded in the green arrows are weak, and the associations encoded in the blue, red and purple arrows are strong.

Example 3. Consider the DAG in Figure 3 a). Here $\mathbf{L}=\emptyset, \mathbf{N}=\left\{A, Y, Z_{1}, Z_{2}\right\}$. Note that $\mathbf{N} \neq \mathbf{V}(\mathcal{G})$ and $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \not \subset \mathbf{N}$ and hence the assumptions needed in part 1) of Theorem 2 for $\mathbf{O}$ to be the optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set do not hold.

All possible $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets in $\mathcal{G}$ are $\mathbf{Z}^{*}=\emptyset, \mathbf{Z}^{* *}=\left\{Z_{1}, Z_{2}\right\}$ and $\mathbf{Z}^{* * *}=\left\{Z_{1}\right\}$. Rotnitzky and Smucler (2019) showed that $\mathbf{Z}^{*} \preceq \mathbf{Z}^{* * *}$ and that no optimal static, and consequently no optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set, exists since there are two distinct $P$ and $P^{\prime}$ in $\mathcal{M}(\mathcal{G})$ such that, for $\pi(A \mid \mathbf{L})=I_{1}(A), \sigma_{\pi, \mathbf{Z}^{*}}(P)<\sigma_{\pi, \mathbf{Z}^{* *}}(P)$ and $\sigma_{\pi, \mathbf{Z}^{*}}^{2}\left(P^{\prime}\right)>\sigma_{\pi, \mathbf{Z}^{* *}}^{2}\left(P^{\prime}\right)$. However, by parts 2) and 3) of Theorem 2, $\mathbf{O}_{\text {min }}=\mathbf{O}_{m}=\emptyset$ is the optimal minimum and minimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set.

Example 4. In the DAG of Figure 4, $\mathbf{L}=\{L\}, \mathbf{N}=\{A, Y, L, F\}$. Here $\mathbf{N} \neq \mathbf{V}$ and $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \not \subset \mathbf{N}$ and hence the assumptions needed in part 1) of Theorem 2 for $\mathbf{O}=\{L\}$ to be the globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set do not hold. However, using Proposition 2, it is easy to show that $\{L, F\}$ is the globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. This examples proves that the conditions in part 1) of Theorem 2 are sufficient but not necessary for the existence of a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set.

# 7 Polynomial time algorithms to compute $\mathbf{O}_{\text {min }}$ and $\mathbf{O}_{m}$ 

In this section we provide polynomial time algorithms to compute $\mathbf{O}_{m}$ and $\mathbf{O}_{\text {min }}$. We assume the availability of the following sub-routines:

1. disjointPaths $(A, Y, \mathcal{H})$. Computes a maximal number of inner vertex disjoint paths between $A$ and $Y$. This can be done in $\mathcal{O}[\{\# \mathbf{V}(\mathcal{H})\}^{1 / 2} \# \mathbf{E}(\mathcal{H})]$ time using a maximum flow algorithm. See Corollary 7.1.5 in Jungnickel (2005). By Manger's Theorem (see Theorem 7.1.4 of Jungnickel (2005)), a routine minCut $(A, Y, \mathcal{H})$ that computes the size of the minimum $A-Y$ cut in an undirected graph $\mathcal{H}$ can also be implemented in $\mathcal{O}[\{\# \mathbf{V}(\mathcal{H})\}^{1 / 2} \# \mathbf{E}(\mathcal{H})]$ time.
2. testExistAdj $(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$. Returns true if and only if there exists an adjustment set $\mathbf{Z}$ with respect to $A, Y$ in $\mathcal{G}$ that satisfies $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$. This can be done in $\mathcal{O}\{\# \mathbf{V}(\mathcal{G})+\# \mathbf{E}(\mathcal{G})\}$ time using the FINDADJ routine developed in van der Zander et al. (2019).

## Algorithm 1: Subroutine to determine if a vertex is a member of a minimum $A-Y$ cut

input : An undirected graph $\mathcal{H}$ with vertex set $\mathbf{V}$, two non-adjacent vertices $A, Y \in \mathbf{V}$ and $V \in \mathbf{V} \backslash\{A, Y\}$.
output: Boolean. True if there exists a minimum $A-Y$ cut $\mathbf{Z}$ with $V \in \mathbf{Z}$.
procedure isInMinimum $(V, A, Y, \mathcal{H})$
$\mathbf{E}^{\prime}=\mathbf{E}(\mathcal{H}) \cup\{\{A, V\},\{V, Y\}\}$.
$\mathcal{H}^{\prime}=\left(\mathbf{V}(\mathcal{H}), \mathbf{E}^{\prime}\right)$
$m_{1}=\# \min \operatorname{Cut}\left(A, Y, \mathcal{H}^{\prime}\right)$
$m_{2}=\# \operatorname{minCut}(A, Y, \mathcal{H})$
if $m_{1}=m_{2}$ then
1 return true
else
1 return false

# Algorithm 2: Algorithm to compute $\mathbf{O}_{m}$ 

input : $\mathcal{G}$ a DAG with vertex set $\mathbf{V}$ and vertices $A, Y \in \mathbf{V}$ such that $A \in \operatorname{an}_{\mathcal{G}}(Y) .(\mathbf{L}, \mathbf{N})$ an admissible pair with respect to $A, Y$ in $\mathcal{G}$.
output: $\mathbf{O}_{m}$.
procedure findOptMinimum $(A, Y, \mathcal{G}, \mathbf{N}, \mathbf{L})$
if testExistsAdj $(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ then
construct $\mathcal{H}^{1}$
$\pi_{1}, \pi_{2}, \ldots, \pi_{m}=$ disjointPaths $\left(A, Y, \mathcal{H}^{1}\right)$
out $=\emptyset$
for $i=1,2, \ldots, m$ do
$A-V_{1}-V_{2}-\ldots-V_{k_{i}}-Y=\pi_{i}$
for $j=k_{i}, \ldots, 1$ do
if isInMinimum $\left(V_{j}, \mathcal{H}^{1}\right)$ then
out $=$ out $\cup\left\{V_{j}\right\}$
break
else
I out $=*$
return out

## Algorithm 3: Algorithm to compute $\mathbf{O}_{\text {min }}$

input : $\mathcal{G}$ a DAG with vertex set $\mathbf{V}$ and vertices $A, Y \in \mathbf{V}$ such that $A \in \operatorname{an}_{\mathcal{G}}(Y) .(\mathbf{L}, \mathbf{N})$ an admissible pair with respect to $A, Y$ in $\mathcal{G}$.
output: $\mathbf{O}_{\text {min }}$.
procedure findOptMinimal $(A, Y, \mathcal{G}, \mathbf{N}, \mathbf{L})$
if testExistsAdj $(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$ then
construct $\mathcal{H}^{1}$
$\mathrm{nb}=\mathrm{nb}_{\mathcal{H}^{1}}(Y)$
out $=\emptyset$
stack $=\emptyset$
visited $=\emptyset$
stack.push $(A)$
while stack $\neq \emptyset$ do
$V=$ stack.pop()
if $V \in \mathrm{nb}$ and $V \notin$ visited then
out $=$ out $\cup\{V\}$
visited $=$ visited $\cup\{V\}$
else if $V \notin$ visited then
visited $=$ visited $\cup\{V\}$
stack.push $\left(\mathrm{nb}_{\mathcal{H}^{1}}(V)\right)$
else
I out $=*$
return out

In the Supplementary Material we prove the following results.
Lemma 4. Algorithm 1 outputs true if and only if there exists a minimum $A-Y$ cut $\mathbf{Z}$ in $\mathcal{H}$ with $V \in \mathbf{Z}$.
Proposition 7. Assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Then, the output of Algorithm 2 is equal to $\mathbf{O}_{m}$. Furthermore, the complexity of Algorithm is $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{7 / 2}\right]$.

Proposition 8. Assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Then, the output of Algorithm 3 is equal to $\mathbf{O}_{\text {min }}$. Furthermore, the complexity of Algorithm is $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$.

Algorithm 3 is a simple modification of the depth first search algorithm (see Section 8.2 of Jungnickel (2005)). Its complexity is dominated by the complexity of constructing $\mathcal{H}^{1}$, which is $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$.

# 8 Discussion 

In this paper we have shown that for $(\mathbf{L}, \mathbf{N})$ an admissible pair, a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set exists when $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. We also noted that there are graphs that admit an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set but with no globally optimal one. However, in Example 4 we exhibited a graph such that $\mathbf{N} \neq \mathbf{V}$ and $\mathbf{N} \not \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$, but an optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set does exist. A complete characterization of the full class of graphs under which a globally optimal $\mathbf{L}-\mathbf{N}$ dynamic adjustment set exists remains an open problem.

The results in this paper are for point interventions, that is, for interventions on a single treatment vertex $A$. For multiple time dependent static interventions, Rotnitzky and Smucler (2019) introduced the notion of a time dependent adjustment set and provided graphical criteria to compare two time dependent adjustment sets. They also showed that there exist graphs without hidden variables in which no optimal time dependent adjustment set exists. The extension of these results to general dynamic treatment regimes and graphs with hidden variables is an interesting problem that warrants further research.

Another related line of research is the derivation of semiparametric efficient estimators of the policy value of a static point intervention in graphical models. Unlike the non-parametric estimators considered in this paper, semiparametric efficient estimators exploit all the information encoded in the assumed causal graphical model. Rotnitzky and Smucler (2019) propose a semiparametric efficient estimator for static point interventions and DAGs without hidden variables. Bhattacharya et al. (2020) derived the semiparametric efficient influence function of the policy value in special classes of DAGs with hidden variables. The derivation of the semiparametric efficient influence function of the policy value of a static or dynamic regime in an arbitrary DAG with hidden variables in which the policy value is identified remains an important open problem.

## 9 Supplementary Material

### 9.1 Proofs of results in Section 2

Proof of Proposition 1. 1) Assume first that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$. Let $y \in \mathbb{R}$ and $a \in \mathcal{A}$. Taking $\pi(A \mid \mathbf{L})=I_{a}(A)$, it follows from the definition of $\mathbf{L}-\mathbf{N}$ dynamic adjustment set that

$$
E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{L}, \operatorname{pa}_{\mathcal{G}}(A)\right\}\right]=E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{Z}\right\}\right]
$$

Note that

$$
E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{L}, \operatorname{pa}_{\mathcal{G}}(A)\right\}\right]=E_{P}\left[\frac{I_{(-\infty, y]}(Y) I_{a}(A)}{f\left\{A=a \mid \mathbf{L}, \operatorname{pa}_{\mathcal{G}}(A)\right\}}\right]
$$

Since by assumption $\mathbf{L} \subset \operatorname{nd}_{\mathcal{G}}(A)$, by the Local Markov Property it holds that $A \Perp \mathbf{L} \mid \operatorname{pa}_{\mathcal{G}}(A)$ under all $P \in \mathcal{M}(\mathcal{G})$. This implies

$$
f\left\{A=a \mid \mathbf{L}, \operatorname{pa}_{\mathcal{G}}(A)\right\}=f\left\{A=a \mid \operatorname{pa}_{\mathcal{G}}(A)\right\}
$$

and hence

$$
E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{L}, \operatorname{pa}_{\mathcal{G}}(A)\right\}\right]=E_{P}\left[\frac{I_{(-\infty, y]}(Y) I_{a}(A)}{f\left\{A=a \mid \operatorname{pa}_{\mathcal{G}}(A)\right\}}\right]=E_{P}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \operatorname{pa}_{\mathcal{G}}(A)\right\}\right]
$$

Now (9), (10) and the fact that by assumption $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$ imply that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.

Assume now that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$. Take $y \in \mathbb{R}$. We have to show that

$$
E_{P}\left(E_{\pi_{\mathbf{Z}}}^{*}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \mathbf{Z}\right\} \mid \mathbf{Z}\right]\right)=E_{P}\left(E_{\pi^{*}}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right]\right)
$$

For $a \in \mathcal{A}$ define

$$
\begin{aligned}
& B(a, \mathbf{Z})=E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{Z}\right\} \\
& \widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right)=E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\}
\end{aligned}
$$

Note that

$$
\begin{aligned}
E_{P}\left(E_{\pi_{\mathbf{Z}}}^{*}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \mathbf{Z}\right\} \mid \mathbf{Z}\right]\right) & =\sum_{a \in \mathcal{A}} E_{P}\left[\pi(a \mid \mathbf{L}) E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \mathbf{Z}\right\}\right] \\
& =\sum_{a \in \mathcal{A}} E_{P}[\pi(a \mid \mathbf{L}) B(a, \mathbf{Z})] \\
& =\sum_{a \in \mathcal{A}} E_{P}\left[\pi(a \mid \mathbf{L}) E_{P}\{B(a, \mathbf{Z}) \mid \mathbf{L}\}\right]
\end{aligned}
$$

and

$$
\begin{aligned}
E_{P}\left(E_{\pi^{*}}\left[E_{P}\left\{I_{(-\infty, y]}(Y) \mid A, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right]\right) & =\sum_{a \in \mathcal{A}} E_{P}\left[\pi(a \mid \mathbf{L}) E_{P}\left\{I_{(-\infty, y]}(Y) \mid A=a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\}\right] \\
& =\sum_{a \in \mathcal{A}} E_{P}\left[\pi(a \mid \mathbf{L}) \widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right)\right] \\
& =\sum_{a \in \mathcal{A}} E_{P}\left[\pi(a \mid \mathbf{L}) E_{P}\left\{\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right) \mid \mathbf{L}\right\}\right]
\end{aligned}
$$

Thus, to prove this part of the proposition, it suffices to show that

$$
E_{P}\left\{\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right) \mid \mathbf{L}\right\}=E_{P}\left\{\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right) \mid \mathbf{L}\right\}
$$

Now, since $\operatorname{pa}_{\mathcal{G}}(A) \cup \mathbf{L}$ satisfies the back-door criterion, and since by assumption $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set, Corollary 2 of Shpitser et al. (2010) implies that

$$
\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right)=E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\}
$$

and

$$
B(a, \mathbf{Z})=E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \mathbf{Z}\right\}
$$

where $Y_{a}$ is a random variable with distribution equal to the marginal law of $Y$ when the vector $\mathbf{V}$ has a distribution given by

$$
f_{a}(\mathbf{v})=\delta_{a}(\mathbf{v}) \prod_{V_{j} \in \mathbf{V} \backslash\{A\}} f\left\{v_{j} \mid \operatorname{pa}_{\mathcal{G}}\left(v_{j}\right)\right\}
$$

with $\delta_{a}(\mathbf{v})$ being the indicator function that the coordinate of $\mathbf{v}$ corresponding to $A$ is equal to $a$.
Thus

$$
E\left\{\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right) \mid \mathbf{L}\right\}=E\left[E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right\} \mid \mathbf{L}\right]=E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \mathbf{L}\right\}
$$

and, since $\mathbf{L} \subset \mathbf{Z}$,

$$
E\{B(a, \mathbf{Z}) \mid \mathbf{L}\}=E\left[E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \mathbf{Z}\right\} \mid \mathbf{L}\right]=E\left\{I_{(-\infty, y]}\left(Y_{a}\right) \mid \mathbf{L}\right\}
$$

Hence

$$
E\{B(a, \mathbf{Z}) \mid \mathbf{L}\}=E\left\{\widetilde{B}\left(a, \operatorname{pa}_{\mathcal{G}}(A), \mathbf{L}\right) \mid \mathbf{L}\right\}
$$

We conclude that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set.
2) It suffices to show that if $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ then $\mathbf{Z} \cap$ $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set too. Take $\mathbf{Z}$ an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. By part 1), $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ adjustment set. Then, by Theorem $1, Y \Perp_{\mathcal{G} \text { atd }(A, Y)} A \mid \mathbf{Z}$ and $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$. By Lemma 1 from van der Zander et al. (2019), $Y \Perp_{\mathcal{G} \text { atd }(A, Y)} A \mid \mathbf{Z} \cap \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Using Theorem 1 again, we obtain that $\mathbf{Z} \cap \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ is an $\mathbf{L}-\mathbf{N}$ adjustment set. Then part 1) of this proposition implies that $\mathbf{Z} \cap \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$.

Finally, note that parts 3) and 4) follow immediately from part 1). This finishes the proof of the proposition.

# 9.2 Proofs of results in Section 5 

To prove Lemmas 1 and 2 we will use the fact that for any $\mathbf{L}-\mathbf{N}$ dynamic adjustment set $\mathbf{Z}$ it holds that

$$
\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})=\sum_{a \in \mathcal{A}} \psi_{P, \pi, a}(\mathbf{Z} ; \mathcal{G})
$$

where

$$
\psi_{P, \pi, a}(\mathbf{Z} ; \mathcal{G})=I_{a}(A) \frac{\pi(a \mid \mathbf{L})}{f(a \mid \mathbf{Z})}\{Y-b(a, \mathbf{Z} ; P)\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{Z} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{Z} ; P)\}
$$

Define $\boldsymbol{\Psi}_{P, \pi}(\mathbf{Z} ; \mathcal{G})=\left(\psi_{P, \pi, a}(\mathbf{Z} ; \mathcal{G})\right)_{a \in \mathcal{A}}$.
Proof of Lemma 1. We show first that that $\mathbf{G} \cup \mathbf{B}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. The assumption $A \Perp_{\mathcal{G}} \mathbf{G} \mid \mathbf{B}$ implies

$$
f(A \mid \mathbf{G}, \mathbf{B})=f(A \mid \mathbf{B})
$$

Then, for all $P \in \mathcal{M}(\mathcal{G})$,

$$
E_{P}\left\{\frac{\pi(A \mid \mathbf{L}) Y}{f(A \mid \mathbf{G}, \mathbf{B})}\right\}=E_{P}\left\{\frac{\pi(A \mid \mathbf{L}) Y}{f(A \mid \mathbf{B})}\right\}=\chi_{\pi}(P, \mathcal{G})
$$

where the last equality holds because $\mathbf{B}$ is, by assumption, an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. This proves that $\mathbf{G} \cup \mathbf{B}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. Using (12) we obtain

$$
E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G}, \mathbf{B} ; P)\}=E_{P}\left\{\frac{I_{a}(a) \pi(a \mid \mathbf{L}) Y}{f(a \mid \mathbf{G}, \mathbf{B})}\right\}=E_{P}\left\{\frac{I_{a}(a) \pi(a \mid \mathbf{L}) Y}{f(a \mid \mathbf{B})}\right\}=E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{B} ; P)\}
$$

Write

$$
\begin{aligned}
\psi_{P, \pi, a}(\mathbf{B} ; \mathcal{G}) & =\frac{I_{a}(A) \pi(a \mid \mathbf{L}) Y}{f(a \mid \mathbf{B})}-\pi(a \mid \mathbf{L})\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{B})}-1\right\} b(a, \mathbf{B} ; P)-E_{P}[\pi(a \mid \mathbf{L}) b(a, \mathbf{B} ; P)] \\
& =\frac{I_{a}(A) \pi(a \mid \mathbf{L}) Y}{f(a \mid \mathbf{G}, \mathbf{B})}-\pi(a \mid \mathbf{L})\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} b(a, \mathbf{G}, \mathbf{B} ; P) \\
& +\pi(a \mid \mathbf{L})\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\}\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G}, \mathbf{B} ; P)\} \\
& =\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G})+\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}
\end{aligned}
$$

where the second equality follows from (12) and (13). Since

$$
E_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) g(A, \mathbf{G}, \mathbf{B})\right\}=0 \text { for any } g \text { such that } E_{P}\{g(A, \mathbf{G}, \mathbf{B}) \mid \mathbf{G}, \mathbf{B}\}=0
$$

and

$$
E_{P}\left[\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\} \mid \mathbf{G}, \mathbf{B}\right]=0
$$

we conclude that

$$
\operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{B} ; \mathcal{G})\right\}=\operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G})\right\}+\operatorname{var}_{P}\left[\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}\right]
$$

Next note that

$$
\begin{aligned}
& \operatorname{var}_{P}\left[\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}\right]= \\
& E_{P}\left[\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}^{2} \pi(a \mid \mathbf{L})^{2} \operatorname{var}_{P}\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1 \mid \mathbf{G}, \mathbf{B}\right\}\right]= \\
& E_{P}\left[\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}^{2} \pi(a \mid \mathbf{L})^{2}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\}\right]= \\
& E_{P}\left[\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}^{2} \pi(a \mid \mathbf{L})^{2}\left\{\frac{1}{f(a \mid \mathbf{B})}-1\right\}\right]= \\
& E_{P}\left[\operatorname{var}_{P}\{b(a, \mathbf{G}, \mathbf{B} ; P) \mid \mathbf{B}\} \pi(a \mid \mathbf{L})^{2}\left\{\frac{1}{f(a \mid \mathbf{B})}-1\right\}\right]
\end{aligned}
$$

where the last equality follows from

$$
\begin{aligned}
b(a, \mathbf{B} ; P)=E_{P}(Y \mid A=a, \mathbf{B})=E_{P}\left\{E_{P}(Y \mid A=a, \mathbf{G}, \mathbf{B}) \mid A=a, \mathbf{B}\right\} & =E_{P}\{b(a, \mathbf{G}, \mathbf{B}) \mid A=a, \mathbf{B}\} \\
& =E_{P}\{b(a, \mathbf{G}, \mathbf{B}) \mid \mathbf{B}\}
\end{aligned}
$$

since $A \Perp_{\mathcal{G}} \mathbf{G} \mid \mathbf{B}$ by assumption.
Now, by (11), $\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})=\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{Z} ; \mathcal{G})$, where $\mathbf{1}$ is a vector of length $\# \mathcal{A}$ filled with ones. Hence $\operatorname{var}_{P}\left\{\psi_{P, \pi}(\mathbf{B} ; \mathcal{G})\right\}=$ $\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{B} ; \mathcal{G})\right\}$. Recall that $\mathbf{S}=\left(S_{a}\right)_{a \in \mathcal{A}}$, where

$$
S_{a} \equiv\left\{\frac{I_{a}(A)}{f(a \mid \mathbf{G}, \mathbf{B})}-1\right\} \pi(a \mid \mathbf{L})\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}
$$

Since by (14) it holds that $E_{P}(\mathbf{S} \mid \mathbf{G}, \mathbf{B})=\mathbf{0}$, we have

$$
\begin{aligned}
\sigma_{\pi, \mathbf{B}}^{2}(P)=\operatorname{var}_{P}\left\{\psi_{P, \pi}(\mathbf{B} ; \mathcal{G})\right\}=\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{B} ; \mathcal{G})\right\} & =\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G})\right\}+\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \mathbf{S}\right\} \\
& =\sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P)+\mathbf{1}^{\top} \operatorname{var}_{P}(\mathbf{S}) \mathbf{1}
\end{aligned}
$$

We already derived the expression for $\operatorname{var}_{P}\left(S_{a}\right)$ in (15). Now, if $a \neq a^{\prime}$

$$
\begin{aligned}
& \operatorname{cov}_{P}\left(S_{a}, S_{a^{\prime}}\right)= \\
& E_{P}\left[\left\{\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{B})}-\pi(a \mid \mathbf{L})\right\}\left\{\frac{I_{a^{\prime}}(A) \pi\left(a^{\prime} \mid \mathbf{L}\right)}{f\left(a^{\prime} \mid \mathbf{B}\right)}-\pi\left(a^{\prime} \mid \mathbf{L}\right)\right\}\{b(a, \mathbf{G}, \mathbf{B} ; P)-b(a, \mathbf{B} ; P)\}\left\{b\left(a^{\prime}, \mathbf{G}, \mathbf{B} ; P\right)-b\left(a^{\prime}, \mathbf{B} ; P\right)\right\}\right] \\
& E_{P}\left[\left\{\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{B})}-\pi(a \mid \mathbf{L})\right\}\left\{\frac{I_{a^{\prime}}(A) \pi\left(a^{\prime} \mid \mathbf{L}\right)}{f\left(a^{\prime} \mid \mathbf{B}\right)}-\pi\left(a^{\prime} \mid \mathbf{L}\right)\right\} \operatorname{cov}_{P}\left[b(a, \mathbf{G}, \mathbf{B} ; P), b\left(a^{\prime}, \mathbf{G}, \mathbf{B} ; P\right) \mid \mathbf{B}, A\right]\right]= \\
& E_{P}\left[\left\{\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{B})}-\pi(a \mid \mathbf{L})\right\}\left\{\frac{I_{a^{\prime}}(A) \pi\left(a^{\prime} \mid \mathbf{L}\right)}{f\left(a^{\prime} \mid \mathbf{B}\right)}-\pi\left(a^{\prime} \mid \mathbf{L}\right)\right\} \operatorname{cov}_{P}\left[b(a, \mathbf{G}, \mathbf{B} ; P), b\left(a^{\prime}, \mathbf{G}, \mathbf{B} ; P\right) \mid \mathbf{B}\right]\right]= \\
& -E_{P}\left[\pi(a \mid \mathbf{L}) \pi\left(a^{\prime} \mid \mathbf{L}\right) \operatorname{cov}_{P}\left\{b(a, \mathbf{G}, \mathbf{B} ; P), b\left(a^{\prime}, \mathbf{G}, \mathbf{B} ; P\right) \mid \mathbf{B}\right\}\right]
\end{aligned}
$$

This finishes the proof Lemma 1.
Proof of Lemma 2. We first show that $\mathbf{G}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. The assumptions that $Y \Perp_{\mathcal{G}} \mathbf{B} \mid A, \mathbf{G}$ and $\mathbf{L} \subset \mathbf{G}$ imply that for all $P \in \mathcal{M}(\mathcal{G})$

$$
b(A, \mathbf{G}, \mathbf{B} ; P)=E_{P}(Y \mid A, \mathbf{G}, \mathbf{B})=E_{P}(Y \mid A, \mathbf{G})=b(A, \mathbf{G} ; P)
$$

Hence,

$$
E_{P}\left[E_{\pi_{\mathbf{G}}^{*}}\{b(A, \mathbf{G} ; P) \mid \mathbf{G}\}\right]=E_{P}\left[E_{\pi_{\mathbf{G}}^{*}}\{b(A, \mathbf{G}, \mathbf{B} ; P) \mid \mathbf{G}\}\right]=E_{P}\left[E_{\pi_{\mathbf{G} \cup \mathbf{B}}^{*}}\{b(A, \mathbf{G}, \mathbf{B} ; P) \mid \mathbf{G} \cup \mathbf{B}\}\right]=\chi_{\pi}(P ; \mathcal{G})
$$

where the first equality follows from (16), the second equality follows from the fact that, since $\pi_{\mathbf{G}}^{*}(A \mid \mathbf{G}) \equiv \pi(A \mid \mathbf{L})$ and $\pi_{\mathbf{G} \cup \mathbf{B}}^{*}(A \mid \mathbf{G} \cup \mathbf{B}) \equiv \pi(A \mid \mathbf{L})$ then $\pi_{\mathbf{G}}^{*}(A \mid \mathbf{G})=\pi_{\mathbf{G} \cup \mathbf{B}}^{*}(A \mid \mathbf{G} \cup \mathbf{B})$, and the third equality follows from the assumption that $\mathbf{G} \cup \mathbf{B}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. This shows that $\mathbf{G}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set.

Next, write

$$
\operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G})\right\}=\operatorname{var}_{P}\left\{E_{P}\left(\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G})\right\}+E_{P}\left\{\operatorname{var}_{P}\left(\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right)\right\}\right.
$$

Now

$$
\begin{aligned}
& E_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}= \\
& E_{P}\left[\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{G}, \mathbf{B})}\{Y-b(a, \mathbf{G} ; P)\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)\} \mid A, Y, \mathbf{G}\right]= \\
& I_{a}(A) \pi(a \mid \mathbf{L})\{Y-b(a, \mathbf{G} ; P)\} E_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A, Y, \mathbf{G}\right\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)\}= \\
& I_{a}(A) \pi(a \mid \mathbf{L})\{Y-b(a, \mathbf{G} ; P)\} E_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A, \mathbf{G}\right\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)\}= \\
& \frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{G})}\{Y-b(a, \mathbf{G} ; P)\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)\}= \\
& \psi_{P, \pi, a}(\mathbf{G} ; \mathcal{G})
\end{aligned}
$$

where the first equality follows from (16), the third equality follows from $Y \Perp_{\mathcal{G}} \mathbf{B} \mid A, \mathbf{G}$ and the fourth from Lemma 10 from Rotnitzky and Smucler (2019) which states that

$$
E_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A, \mathbf{G}\right\}=\frac{1}{f(a \mid \mathbf{G})}
$$

On the other hand,

$$
\begin{aligned}
& \operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}= \\
& \operatorname{var}_{P}\left[\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{G}, \mathbf{B})}\{Y-b(a, \mathbf{G} ; P)\}+\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)-E_{P}\{\pi(a \mid \mathbf{L}) b(a, \mathbf{G} ; P)\} \mid A, Y, \mathbf{G}\right]= \\
& I_{a}(A) \pi(a \mid \mathbf{L})^{2}\{Y-b(a, \mathbf{G} ; P)\}^{2} \operatorname{var}_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A=a, \mathbf{G}\right\}
\end{aligned}
$$

where the first equality follows from (16) and the second follows from $Y \Perp_{\mathcal{G}} \mathbf{B} \mid A, \mathbf{G}$. Thus

$$
\begin{aligned}
& E_{P}\left[\operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right]= \\
& E_{P}\left[\pi(a \mid \mathbf{L})^{2} f(a \mid \mathbf{G}) \operatorname{var}_{P}(Y \mid A=a, \mathbf{G}) \operatorname{var}_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A=a, \mathbf{G}\right\}\right]
\end{aligned}
$$

Now, by (11), $\psi_{P, \pi}(\mathbf{Z} ; \mathcal{G})=\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{Z} ; \mathcal{G})$, where $\mathbf{1}$ is a vector of length $\# \mathcal{A}$ filled with ones. Thus $\sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P)=$ $\operatorname{var}_{P}\left\{\psi_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G})\right\}=\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G})\right\}$. We then have

$$
\begin{aligned}
\sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P) & =\operatorname{var}_{P}\left[E_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right]+E_{P}\left[\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right]\right. \\
& =\operatorname{var}_{P}\left\{\mathbf{1}^{\top} \boldsymbol{\Psi}_{P, \pi}(\mathbf{G} ; \mathcal{G})\right\}+\mathbf{1}^{\top} E_{P}\left[\operatorname{var}_{P}\left\{\boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right] \mathbf{1} \\
& =\sigma_{\pi, \mathbf{G}}^{2}(P)+\mathbf{1}^{\top} E_{P}\left[\operatorname{var}_{P}\left\{\boldsymbol{\Psi}_{P, \pi}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right] \mathbf{1}
\end{aligned}
$$

We obtained an expression for $E_{P}\left[\operatorname{var}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}\right]$ in (17). Using (16), if $a \neq a^{\prime}$ we obtain

$$
\begin{aligned}
& \operatorname{cov}_{P}\left\{\psi_{P, \pi, a}(\mathbf{G}, \mathbf{B} ; \mathcal{G}), \psi_{P, \pi, a^{\prime}}(\mathbf{G}, \mathbf{B} ; \mathcal{G}) \mid A, Y, \mathbf{G}\right\}= \\
& \operatorname{cov}_{P}\left[\frac{I_{a}(A) \pi(a \mid \mathbf{L})}{f(a \mid \mathbf{G}, \mathbf{B})}\{Y-b(a, \mathbf{G} ; P)\}, \frac{I_{a^{\prime}}(A) \pi\left(a^{\prime} \mid \mathbf{L}\right)}{f\left(a^{\prime} \mid \mathbf{G}, \mathbf{B}\right)}\left\{Y-b\left(a^{\prime}, \mathbf{G} ; P\right)\right\} \mid A, Y, \mathbf{G}\right]=0
\end{aligned}
$$

since $I_{a}(A) I_{a^{\prime}}(A)=0$. This shows that

$$
\sigma_{\pi, \mathbf{G}, \mathbf{B}}^{2}(P)=\sigma_{\pi, \mathbf{G}}^{2}(P)+\sum_{a \in \mathcal{A}}\left(E_{P}\left[\pi^{2}(a \mid \mathbf{L}) f(a \mid \mathbf{G}) \operatorname{var}_{P}(Y \mid A=a, \mathbf{G}) \operatorname{var}_{P}\left\{\frac{1}{f(a \mid \mathbf{G}, \mathbf{B})} \mid A=a, \mathbf{G}\right\}\right]\right)
$$

This concludes the proof of Lemma 2 .
The proof of Proposition 3 below uses Proposition 4, the proof of which can be found in the following section.
Proof of Proposition 3. Let $\mathbf{Z}$ be an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. Note that by Proposition 1, $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set.

We begin with the proof of $A \Perp_{\mathcal{G}} \mathbf{O} \backslash \mathbf{Z} \mid \mathbf{Z}$. Consider a path $\pi$ in $\mathcal{G}$ between $A$ and a vertex $O \in \mathbf{O} \backslash \mathbf{Z}$. Note that since $\mathbf{O}$ does not contain descendants of $A$, if $\pi$ is directed then it enters $A$ through the back-door. Now, since $\mathbf{L} \subset \mathbf{O}, \mathbf{L} \subset \mathbf{Z}$ and $O \in \mathbf{O} \backslash \mathbf{Z}$, it holds that $O \in \mathbf{O} \backslash \mathbf{L}$. Hence, there exists a directed path from $O$ to $Y$, say $\delta$, such that all vertices in that path except for $O$ are members of $\operatorname{forb}(A, Y, \mathcal{G})$. The path from $A$ to $Y$ obtained by joining $\pi$ and $\delta$, say $\gamma$, is non-directed. Since $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ adjustment set, by Corollary 1 from Shpitser et al. (2010), it does not contain vertices in $\operatorname{forb}(A, Y, \mathcal{G})$ and it has to block $\gamma$. We conclude that $\pi$ must be blocked by $\mathbf{Z}$, which is what we wanted to show.

Next, we show that $Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O} \mid A, \mathbf{O}$. Consider a path $\pi$ in $\mathcal{G}$ between $Y$ and a vertex $Z \in \mathbf{Z} \backslash \mathbf{O}$. Suppose for the sake of contradiction that $\pi$ is open given $A, \mathbf{O}$. Now, if $\pi$ does not have colliders, by Lemma E. 4 from Henckel et al. (2019), it is blocked by $A, \mathbf{O} \backslash \mathbf{L}$ and hence it is blocked by $A, \mathbf{O}$, which is a contradiction. Assume then that $\pi$ has at least one collider. Let $C$ be the collider on $\pi$ that is closest to $Y$. Suppose first that in $\pi$ the edge containing $Y$ points out of $Y$. Then $C$ is a descendant of $Y$. Since $\pi$ is open given $A, \mathbf{O}$, it follows that $C$ is an ancestor of either $A$ or $\mathbf{O}$. This implies that either $A$ or a vertex in $\mathbf{O}$ is a descendant of $Y$. This contradicts

the fact that $A \in \operatorname{an}_{\mathcal{G}}(Y)$ and $\mathbf{O} \cap \operatorname{de}_{\mathcal{G}}(A)=\emptyset$. Suppose next that in $\pi$ the edge containing $Y$ points into $Y$. Let $F$ bet the only fork on $\pi$ that lies between $C$ and $Y$. Since $\pi$ is open given $A, \mathbf{O}, C$ is an ancestor of either $A$ or a vertex in $\mathbf{O}$. Since $F$ is an ancestor of $C$, it must be that $F$ is an ancestor of either $A$ or a vertex in $\mathbf{O}$. Since $\mathbf{O} \cap \operatorname{de}_{\mathcal{G}}(A)=\emptyset$, it follows that $F \notin \operatorname{de}_{\mathcal{G}}(A)$. Thus, there exists a vertex on the sub-path of $\pi$ that goes from $F$ to $Y$ that is a member of $\mathbf{O}$. This implies that $\pi$ is closed given $A, \mathbf{O}$, which is a contradiction. Hence $Y \Perp_{\mathcal{G}} \mathbf{Z} \backslash \mathbf{O} \mid A, \mathbf{O}$ holds.

Finally, we prove that $\mathbf{O}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set. Clearly, $\mathbf{L} \subset \mathbf{O} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Note that from any vertex in $\mathbf{O} \backslash \mathbf{L}$ there exists a directed path in $\mathcal{G}$ to $Y$ that only intersects vertices in $\operatorname{forb}(A, Y, \mathcal{G})$. The definition of $\mathcal{H}^{1}$ then implies that $\mathbf{O}$ is exactly the set of neighbours of $Y$ in $\mathcal{H}^{1}$. Thus, $\mathbf{O}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. It follows from part 2) of Proposition 4 that $\mathbf{O}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustent set.

# 9.3 Proofs of results in Section 6 

Proof fo Lemma 3. Assume first that $U \perp_{\mathcal{H}^{0}} V \mid \mathbf{W}$ holds. If no path between $U$ and $V$ in $\mathcal{H}^{1}$ exists, the result is trivial. Hence, assume there exists a path $\pi$ from $U$ to $V$ in $\mathcal{H}^{1}$. We will show that $\pi$ intersects $\mathbf{W}$. If all edges in $\pi$ are also present in $\mathcal{H}^{0}$ then clearly $\pi$ has to intersect a vertex in $\mathbf{W}$. Otherwise, if an edge, say $S-T$, in $\pi$ is not present in $\mathcal{H}^{0}$ then $S-T$ is of one of two types of edges: (i) the edge goes from a vertex in $\mathbf{L}$ to either $A$ or $Y$, or (ii) there exists a path from $S$ to $T$ in $\mathcal{H}^{0}$ that goes only through vertices in ignore $(A, Y, \mathcal{G})$. If there exists an edge $S-T$ in $\pi$ of type (i) then, since $\mathbf{L} \subset \mathbf{W}$, we conclude that $\pi$ is blocked by $\mathbf{W}$ in $\mathcal{H}^{1}$. Assume then that all edges in $S-T$ that are not present in $\mathcal{H}^{0}$ are of type (ii). Consider the path $\delta$ in $\mathcal{H}^{0}$ obtained from $\pi$ by replacing each edge $S-T$ in $\pi$ that is not present in $\mathcal{H}^{0}$ by the corresponding path in $\mathcal{H}^{0}$ from $S$ to $T$ that goes only through vertices in ignore $(A, Y, \mathcal{G})$. Since by assumption $U \perp_{\mathcal{H}^{0}} V \mid \mathbf{W}$, the path $\delta$ has to intersect $\mathbf{W}$. Since $\mathbf{W} \subset \mathbf{V}\left(\mathcal{H}^{1}\right)$, we conclude that $\pi$ has to intersect $\mathbf{W}$.

Assume next that $U \perp_{\mathcal{H}^{1}} V \mid \mathbf{W}$ holds. If no path between $U$ and $V$ in $\mathcal{H}^{0}$ exists, the result is trivial. Assume then that there exists a path $\pi$ from $U$ to $V$ in $\mathcal{H}^{0}$. We will show that $\pi$ intersects $\mathbf{W}$. If $\pi$ goes only through vertices that are not in ignore $(A, Y, \mathcal{G})$ then $\pi$ is also a path in $\mathcal{H}^{1}$ and hence it intersects a vertex in $\mathbf{W}$. If $\pi$ intersects at least one vertex in ignore $(A, Y, \mathcal{G})$, consider the path $\delta$ in $\mathcal{H}^{1}$ obtained from $\pi$ by removing all vertices in ignore $(A, Y, \mathcal{G})$ and adding an edge between any pair of remaining vertices if they were connected in $\pi$ by a path going only through vertices ignore $(A, Y, \mathcal{G})$. Since by assumption $U \perp_{\mathcal{H}^{1}} V \mid \mathbf{W}$, the path $\delta$ has to intersect $\mathbf{W}$. We conclude that $\pi$ has to intersect $\mathbf{W}$.

In order to prove Proposition 4, we will need the following lemmas.
Lemma 5. Let $\mathcal{G}$ be a $D A G$ with vertex set $\mathbf{V}$ and assume that $(A, Y, \mathbf{L}, \mathbf{N})$ satisfy the inclusion conditions. Assume that $(\mathbf{L}, \mathbf{N})$ is an admissible pair with respect to $A, Y$ in $\mathcal{G}$. Then $\mathbf{V}\left(\mathcal{H}^{1}\right)=\{\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}\} \backslash$ $\{\operatorname{forb}(A, Y, \mathcal{G}) \backslash\{A, Y\}\}$. If $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$ then $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{V}\left(\mathcal{H}^{1}\right)$.

Proof. This follows immediately from the definition of $\mathcal{H}^{1}$.
Lemma 6. Let $\mathcal{G}$ be a $D A G$ with vertex set $\mathbf{V}$ and assume that $(A, Y, \mathbf{L}, \mathbf{N})$ satisfy the inclusion conditions.

1. If $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$ then $\mathbf{Z}$ is a $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.
2. If $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ then $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$.
3. $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimal $A-Y$ cut in $\mathcal{H}^{1}$.
4. $\mathbf{Z}$ is a minimum $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is a minimum $A-Y$ cut in $\mathcal{H}^{1}$.

Proof of Lemma 6. Our proof will make use of the following facts. By Theorem 1 and Corollary 2 of van der Zander et al. (2019), if $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set then $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}^{p b d}}(\{A, Y\} \cup \mathbf{L})$. Note also that $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=$ $\operatorname{an}_{\mathcal{G}^{p b d}(A, Y)}(\{A, Y\} \cup \mathbf{L})$.

1) By assumption $Y \perp_{\mathcal{H}^{1}} A \mid \mathbf{Z}$. Lemma 5 implies $\mathbf{L} \subset \mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}$ and $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$. In particular, since $\mathbf{L} \subset \mathbf{Z}$, Lemma 3 implies $Y \perp_{\mathcal{H}^{0}} A \mid \mathbf{Z}$. Let $\mathbf{M}^{\prime}=\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{Z})$ and $\mathcal{H}^{0, \prime}=\left\{\mathcal{G}_{\mathbf{M}^{\prime}}^{p b d}(A, Y)\right\}^{m}$. Since $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ we have that $\mathbf{M}^{\prime} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. This implies that $\mathcal{G}_{\mathbf{M}^{\prime}}^{p b d}(A, Y)$ is a subgraph of $\mathcal{G}_{\operatorname{an} \mathcal{G}(\{A, Y\} \cup \mathbf{L})}^{p b d}(A, Y)$ and hence that $\mathcal{H}^{0, \prime}$ is a subgraph of $\mathcal{H}^{0}$. Then $Y \perp_{\mathcal{H}^{0}} A \mid \mathbf{Z}$ implies $Y \perp_{\mathcal{H}^{0, \prime}} A \mid \mathbf{Z}$. Now (1)

implies $Y \Perp_{\mathcal{G}^{p b d}(A, Y)} A \mid \mathbf{Z}$. Since moreover $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$ and $\mathbf{L} \subset \mathbf{Z} \subset \mathbf{N}$, Theorem 1 implies that $\mathbf{Z}$ is a $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$.
2) By part 1) we only need to prove that if $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$ and $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ then $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. Assume that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set and $\mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Then by Theorem $1, Y \Perp_{\mathcal{G}^{p b d}(A, Y)} A \mid \mathbf{Z}$ and $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$. Moreover, since $\mathbf{L} \subset \mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ we have that $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{Z})=\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Thus, $Y \Perp_{\mathcal{G}^{p b d}(A, Y)} A \mid \mathbf{Z}$ and (1) imply that $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{0}$. Since $\mathbf{L} \subset \mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}$ and $\mathbf{Z} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$, Lemma 3 implies that $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$, which is what we wanted to show.
3) Take $\mathbf{Z}$ a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set. We will show that $\mathbf{Z}$ is a minimal $A-Y$ cut in $\mathcal{H}^{1}$. Since $\mathbf{L} \subset \mathbf{Z} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}$, part 2) implies that $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. Assume for the sake of contradiction that $\mathbf{Z}$ is a not a minimal $A-Y$ cut in $\mathcal{H}^{1}$. Then there exists $\mathbf{Z}^{\prime} \subsetneq \mathbf{Z}$ that is an $A-Y$ cut in $\mathcal{H}^{1}$. By part 1), $\mathbf{Z}^{\prime}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$, which contradicts the fact that $\mathbf{Z}$ was a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set.

Now take $\mathbf{Z}$ a minimal $A-Y$ cut in $\mathcal{H}^{1}$. We will show that $\mathbf{Z}$ is a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$. By part 1), we know that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$. Assume for the sake of contradiction that $\mathbf{Z}$ is not a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set. Then there exists $\mathbf{Z}^{\prime} \subsetneq \mathbf{Z}$ that is a minimal $\mathbf{L}-\mathbf{N}$ static adjustment set. Arguing as before, we see that $\mathbf{Z}^{\prime}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. This contradicts the fact that $\mathbf{Z}$ was a minimal $A-Y$ cut in $\mathcal{H}^{1}$
4) This can be proven using arguments analogous to those used in the proof of part 3).

We are now ready to prove Proposition 4.
Proof of Proposition 4. We prove parts 1) and 2). Parts 3) - 5) follow immediately from Lemma 6 and Proposition 1.

1) Since $(\mathbf{L}, \mathbf{N})$ form an admissible pair with respect to $A, Y$ in $\mathcal{G}$, by Theorem 2 of van der Zander et al. (2019) $\mathbf{W}=\left\{\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L}) \cap \mathbf{N}\right\} \backslash \operatorname{forb}(A, Y, \mathcal{G})$ is an $\mathbf{L}-\mathbf{N}$ static adjustment set. Since $\mathbf{W} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$, by part 2) of Lemma $6, \mathbf{W}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. Hence $A$ and $Y$ cannot be adjacent in $\mathcal{H}^{1}$.
2) Let $\mathbf{Z}$ be an $A-Y$ cut in $\mathcal{H}^{1}$. By part 1) of Lemma $6, \mathbf{Z}$ is a $\mathbf{L}-\mathbf{N}$ static adjustment set with respect to $A, Y$ in $\mathcal{G}$. Then part 1) of Proposition 1 implies that $\mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$.

Proof of Proposition 5. We begin with the proof of (6). Since $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$, we have that that $Y \perp_{\mathcal{H}^{1}} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid \mathbf{Z}_{1}$. Lemma 3 implies $Y \perp_{\mathcal{H}^{0}} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid \mathbf{Z}_{1}$ and hence

$$
Y \perp_{\mathcal{H}^{0}} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid \mathbf{Z}_{1}, A
$$

Recall that $\mathcal{H}^{0}=\left\{\mathcal{G}_{\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})}^{p b d}(A, Y)\right\}^{m}$. Also, $\mathbf{Z}_{1}, \mathbf{Z}_{2} \subset \mathbf{V}\left(\mathcal{H}^{1}\right) \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})=\operatorname{an}_{\mathcal{G}^{p b d}(A, Y)}(\{A, Y\} \cup \mathbf{L})$ and $\mathbf{L} \subset \mathbf{Z}_{1}, \mathbf{L} \subset \mathbf{Z}_{2}$. Then $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{Z}_{1} \cup \mathbf{Z}_{2})=\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Hence equations (1) and (18) imply

$$
Y \Perp_{\mathcal{G}^{p b d}(A, Y)} \mathbf{Z}_{2} \backslash \mathbf{Z}_{1} \mid \mathbf{Z}_{1}, A
$$

Now, assume for the sake of contradiction that (6) does not hold, and hence that there exists a path $\pi$ in $\mathcal{G}$ between $Y$ and a vertex $Z \in \mathbf{Z}_{2} \backslash \mathbf{Z}_{1}$ that is open in $\mathcal{G}$ given $A, \mathbf{Z}_{1}$. Assume first that $\pi$ does not have colliders, and hence it is either directed or has a single fork. Since $\pi$ is open in $\mathcal{G}$ given $A, \mathbf{Z}_{1}, \pi$ does not intersect $A$. Since the proper back-door graph $\mathcal{G}^{p b d}(A, Y)$ is formed by removing from $\mathcal{G}$ the first edge in all causal paths between $A$ and $Y$, the path $\pi$ must exist in $\mathcal{G}^{p b d}(A, Y)$. This contradicts (19). Hence $\pi$ has to have at least one collider. Since $\pi$ is open in $\mathcal{G}$ given $A, \mathbf{Z}_{1}$, all colliders in $\pi$ must be ancestors of a vertex in $\{A\} \cup \mathbf{Z}_{1}$ an no non-collider in $\pi$ can be in $\{A\} \cup \mathbf{Z}_{1}$. Again, the definition of the proper back-door graph implies that $\pi$ must exist in $\mathcal{G}^{p b d}(A, Y)$ and that all colliders in $\pi$ are also ancestors in $\mathcal{G}^{p b d}(A, Y)$ of a vertex in $\{A\} \cup \mathbf{Z}_{1}$. This contradicts (19). It must be that (6) holds.

Turn now to the proof of (7). Since $\mathbf{Z}_{1} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}_{2}$ we have that $A \perp_{\mathcal{H}^{1}} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}$. By Lemma 3, this implies that

$$
A \perp_{\mathcal{H}^{0}} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}
$$

Let $\widetilde{\mathbf{M}}(A, Y, \mathcal{G})=\operatorname{an}_{\mathcal{G}^{p b d}(A, Y)}\left(\{A\} \cup \mathbf{Z}_{1} \cup \mathbf{Z}_{2}\right)$ and $\widetilde{\mathcal{H}}^{0}(A, Y, \mathcal{G})=\left\{\mathcal{G}_{\widetilde{\mathbf{M}}(A, Y, \mathcal{G})}^{p b d}(A, Y)\right\}^{m}$. We will show that (20) implies

$$
A \perp_{\widetilde{\mathcal{H}}^{0}(A, Y, \mathcal{G})} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}
$$

Note that, since $\mathbf{Z}_{1}, \mathbf{Z}_{2} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$, we have $\widetilde{\mathbf{M}}(A, Y, \mathcal{G}) \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. Thus $\mathcal{G}_{\widetilde{\mathbf{M}}(A, Y, \mathcal{G})}^{\text {pbdd }}(A, Y)$ is a subgraph of $\mathcal{G}_{\operatorname{an} \mathcal{G}(\{A, Y\} \cup \mathbf{L})}^{\text {pbdd }}(A, Y)$ and $\widetilde{\mathcal{H}}^{0}(A, Y, \mathcal{G})$ is a subgraph of $\mathcal{H}^{0}(A, Y, \mathcal{G})$. Hence, (21) follows from (20). Now equations (1) and (21) imply

$$
A \Perp_{\mathcal{G}^{\text {pbdd }}(A, Y)} \mathbf{Z}_{1} \backslash \mathbf{Z}_{2} \mid \mathbf{Z}_{2}
$$

Next, assume for the sake of contradiction that (7) does not hold, and hence that there exists a path $\pi$ in $\mathcal{G}$ between $A$ and a vertex $Z \in \mathbf{Z}_{1} \backslash \mathbf{Z}_{2}$ that is open in $\mathcal{G}$ given $\mathbf{Z}_{2}$. Assume first that $\pi$ does not have colliders, and hence it is either directed or has a single fork. Since $\pi$ is open in $\mathcal{G}$ given $\mathbf{Z}_{2}, \pi$ does not intersect $\mathbf{Z}_{2}$. Since $\mathbf{Z}_{1} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset, \mathbf{Z}_{1} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ and $\mathbf{L} \cap \operatorname{de}_{\mathcal{G}}(A)=\emptyset$ no edge in $\pi$ can be of the form $A \rightarrow V$ for some $V$ in $\pi$. Since the proper back-door graph $\mathcal{G}^{\text {pbd }}(A, Y)$ is formed by removing from $\mathcal{G}$ the first edge in all causal paths from $A$ to $Y$, the path $\pi$ must exist in $\mathcal{G}^{\text {pbd }}(A, Y)$. This contradicts (22). Hence $\pi$ has to have at least one collider. Since $\pi$ is open in $\mathcal{G}$ given $\mathbf{Z}_{2}$, all colliders in $\pi$ must be ancestors in $\mathcal{G}$ of a vertex in $\mathbf{Z}_{2}$ an no non-collider in $\pi$ can be in $\mathbf{Z}_{2}$. We can assume without loss of generality that $A$ only appears once on the path $\pi$. Then the only edge in $\pi$ that could possibly not be an edge in $\mathcal{G}^{\text {pbd }}$ is the edge that contains $A$, if it points out of $A$. But if the edge points out of $A$, the collider on $\pi$ that is closest to $A$ would be a descendant of $A$, and hence could not be an ancestor of a vertex in $\mathbf{Z}_{2}$, which is a contradiction. Thus $\pi$ must exist in $\mathcal{G}^{\text {pbd }}(A, Y)$. Since $\mathbf{Z}_{2} \cap \operatorname{forb}(A, Y, \mathcal{G})=\emptyset$, $\mathbf{Z}_{2} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$ and $\mathbf{L} \cap \operatorname{de}_{\mathcal{G}}(A)=\emptyset$, all colliders in $\pi$ are also ancestors in $\mathcal{G}^{\text {pbd }}(A, Y)$ of a vertex in $\mathbf{Z}_{2}$. This contradicts (22). It must be that (7) holds. This finishes the proof of the proposition.

Proof of Theorem 2. We begin with the proof of part 1). If $\mathbf{N}=\mathbf{V}$, the result follows from Proposition 3. Assume then that $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$. By part 1) of Proposition $4, A$ and $Y$ are not adjacent in $\mathcal{H}^{1}$. Thus, any path in $\mathcal{H}^{1}$ from $A$ to $Y$ has to intersect $\mathbf{O}=\operatorname{nb}_{\mathcal{H}^{1}}(Y)$. It follows that $\mathbf{O}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. Moreover, it is easy to show that $\mathbf{O} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}$ for any other $A-Y$ cut $\mathbf{Z}$. Since $\mathbf{N} \subset \operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$, by part 3) of Proposition $4, \mathbf{Z}$ is an $\mathbf{L}-\mathbf{N}$ dynamic adjustment set with respect to $A, Y$ in $\mathcal{G}$ if and only if $\mathbf{Z}$ is an $A-Y$ cut in $\mathcal{H}^{1}$. The desired result now follows from Proposition 5 .

Turn now to the proof of parts 2) and 3). Since by part 1) of Proposition $4, A$ and $Y$ are not adjacent in $\mathcal{H}^{1}$, Theorems 1 and 2 from Halin (1993) imply that $\mathbf{O}_{\text {min }}$ and $\mathbf{O}_{m}$ are $A-Y$ cuts in $\mathcal{H}^{1}$ and, moreover, $\mathbf{O}_{\text {min }} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}$ for all $\mathbf{Z}$ that is a minimal $A-Y$ cut in $\mathcal{H}^{1}$ and $\mathbf{O}_{m} \unlhd_{\mathcal{H}^{1}} \mathbf{Z}$ for all $\mathbf{Z}$ that is a minimum $A-Y$ cut in $\mathcal{H}^{1}$. By parts 4) and 5) of Proposition 4, the set of minimal (minimum) $\mathbf{L}-\mathbf{N}$ dynamic adjustment sets with respect to $A, Y$ in $\mathcal{G}$ is equal to the set of minimal (minimum) $A-Y$ cuts in $\mathcal{H}^{1}$. The desired result now follows from Proposition 5 .

# 9.4 Proofs of results in Section 7 

Proof of Lemma 4. First note that the new graph $\mathcal{H}^{\prime}$ is constructed from the graph $\mathcal{H}$ by adding at most two edges: $A-V$ and $V-Y$. Assume that the algorithm return true. Then $m_{1}=m_{2}$. We will show that $V$ is included in a minimum $A-Y$ cut for $\mathcal{H}$. Since $A-V-Y$ is a path in $\mathcal{H}^{\prime}$, any minimum $A-Y$ cut in $\mathcal{H}^{\prime}$ has to include $V$. Let $\mathbf{Z}^{\prime}$ be a minimum $A-Y$ cut in $\mathcal{H}^{\prime}$. Then $\# \mathbf{Z}^{\prime}=m_{1}$. Since $\mathcal{H}$ is a sub-graph of $\mathcal{H}^{\prime}, \mathbf{Z}^{\prime}$ is also an $A-Y$ cut in $\mathcal{H}$ and hence $m_{2} \leq \# \mathbf{Z}^{\prime}=m_{1}$. Since by assumption $m_{1}=m_{2}$, it must be that $\# \mathbf{Z}^{\prime}=m_{2}$. Hence $\mathbf{Z}^{\prime}$ is a minimum $A-Y$ cut in $\mathcal{H}$ that satisfies $V \in \mathbf{Z}^{\prime}$.

Assume next that there exists a minimum $A-Y$ cut $\mathbf{Z}$ in $\mathcal{H}$ such that $V \in \mathbf{Z}$. Then $\# \mathbf{Z}=m_{2}$. Clearly $\mathbf{Z}$ is also an $A-Y$ cut in $\mathcal{H}^{\prime}$. This implies $m_{2}=\# \mathbf{Z} \geq m_{1}$. However, since $\mathcal{H}$ is a sub-graph of $\mathcal{H}^{\prime}$, we have $m_{1} \geq m_{2}$. Hence $m_{1}=m_{2}$ and the algorithm outputs true.

Proof of Proposition 7. By assumption testExistsAdj $(A, Y, \mathcal{G}, \mathbf{N}, \mathbf{L})=$ true. Let us call the output of the algorithm $\mathbf{Z}^{*}$. By Manger's Theorem (see for example Chapter 7 of Jungnickel (2005)), the output of $\min \operatorname{Cut}(A, Y, \mathcal{H})$ coincides with the number of paths returned by disjointPaths $(A, Y, \mathcal{H})$. Let $\pi_{1}, \ldots, \pi_{m}$ be the paths returned by disjointPaths $(A, Y, \mathcal{H})$.

Now, since $\mathbf{O}_{m}$ is an $A-Y$ cut in $\mathcal{H}^{1}$ of size $m$, there is exactly one vertex $V_{j} \in \mathbf{O}_{m}$ in each path $\pi_{j}, j=1, \ldots, m$. The definition of $\mathbf{O}_{m}$ implies that such $V_{j}$ is the vertex on $\pi_{j}$ that: (i) is a member of at least one minimum $A-Y$ cut, and (ii) is closer to $Y$ on $\pi_{j}$ than any other vertex on $\pi_{j}$ that is a member of at least one minimum $A-Y$ cut. These are precisely the vertices that are included in $\mathbf{Z}^{*}$. Thus $\mathbf{Z}^{*}=\mathbf{O}_{m}$.

Next, we will bound the worst case complexity of Algorithm 2. To do so, we first need to bound the cardinalities of $\mathbf{V}\left(\mathcal{H}^{1}\right)$ and of $\mathbf{E}\left(\mathcal{H}^{1}\right)$ as a function of $\# \mathbf{V}(\mathcal{G})$. Clearly $\# \mathbf{V}\left(\mathcal{H}^{1}\right) \leq \# \mathbf{V}(\mathcal{G})$. This in turn implies $\# \mathbf{E}\left(\mathcal{H}^{1}\right) \leq\{\# \mathbf{V}(\mathcal{G})\}^{2}$. Now, the first step in Algorithm 2 is running testExistAdj $(A, Y, \mathbf{L}, \mathbf{N}, \mathcal{G})$, which has complexity $\mathcal{O}\{\# \mathbf{V}(\mathcal{G})+\# \mathbf{E}(\mathcal{G})\}=\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$. Next, the algorithm constructs $\mathcal{H}^{1}$. Since van der Zander et al. (2019) show that the proper back-door graph can be constructed in $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$ time, that $\operatorname{an}_{\mathcal{G}}(\{A, Y\} \cup \mathbf{L})$

and $\operatorname{forb}(A, Y, \mathcal{G})$ can be computed in $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$ time (see their Section 6 for these three claims) and that a graph $\mathcal{G}$ can be moralized in $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$ time (see their Lemma 2), we have that the construction of $\mathcal{H}^{1}$ has complexity $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{2}\right]$. Next, Algorithm 2 makes one call to disjointPaths $\left(A, Y, \mathcal{H}^{1}\right)$, which has complexity $\mathcal{O}\left[\left\{\# \mathbf{V}\left(\mathcal{H}^{1}\right)\right\}^{1 / 2} \# \mathbf{E}\left\{\mathcal{H}^{1}\right\}\right]=\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{5 / 2}\right]$. After that, the algorithm makes at most $\# \mathbf{V}(\mathcal{G})$ calls to isInMinimum $\left(V_{j}, \mathcal{H}_{1}\right)$. The complexity of isInMinimum $\left(V_{j}, \mathcal{H}_{1}\right)$ is bounded by the complexity of $\operatorname{minCut}\left(A, Y, \mathcal{H}_{1}\right)$, which is bounded by $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{5 / 2}\right]$. Hence, the overall complexity of the outer for loop is $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{7 / 2}\right]$. This dominates the complexities of all other steps. We conclude that the worst case complexity of Algorithm 2 is $\mathcal{O}\left[\{\# \mathbf{V}(\mathcal{G})\}^{7 / 2}\right]$.

Proof of Proposition 8. Since by assumption testExistsAdj $(A, Y, \mathcal{G}, \mathbf{N}, \mathbf{L})=$ true, it follows from part 1) of Proposition 4 that $A$ and $Y$ are not adjacent in $\mathcal{H}^{1}$. We claim that, at any iteration of the algorithm,
if $V \in$ visited, there exists a path in $\mathcal{H}^{1}$ from $V$ to $A$ that does not intersect $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$ except possibly at $V$.

We prove this by induction on the number of times the while loop was entered, say $k$. Before entering the while loop for the first time, visited $=\emptyset$ and hence (23) holds trivially. Suppose that after $k \geq 0$ iterations of the while loop (23) holds. Take $V$ a vertex that is a member of visited after $k+1$ iterations. If $V$ was already a vertex in visited after $k$ iterations, then by the inductive assumption, there is a path in $\mathcal{H}^{1}$ from $V$ to $A$ that does not intersect $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$, except possibly at $V$. If $V$ was only added to visited after $k+1$ iterations, then $V$ is a neighbor of a vertex, say $W$, that was a already a member of visited after $k$ iterations, but not a member of $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$. By the inductive hypothesis, there is a path in $\mathcal{H}^{1}$ from $W$ to $A$ that does not intersect $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$. Since $W$ and $V$ are adjacent, we conclude that there exists a path $V$ to $A$ that does not intersect $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$, except possibly at $V$. This finishes the proof that (23) holds at any iteration of the algorithm.

Now note that at any iteration, out is formed by the vertices in visited that are adjacent to $Y$. Then the fact that (23) holds implies that out $\subset \mathbf{O}_{\text {min }}$. So to prove the proposition, it suffices to show that when the algorithm finishes, $\mathbf{O}_{\text {min }} \subset$ out. Take a vertex $O \in \mathbf{O}_{\text {min }}$. Then in $\mathcal{H}^{1}$ there is a path, say $\pi$, from $O$ to $A$ that only intersects $\mathrm{nb}_{\mathcal{H}^{1}}(Y)$ at $O$. The vertex adjacent to $A$ in $\pi$ is added to the stack during the first iteration of the while loop. During the next iterations, all subsequent vertices in $\pi$ are visited and their neighbours added to the stack, until $O$ is reached. When $O$ is reached, since it is a neighbor of $Y$, it is added to out. Thus, when the algorithm finishes, $\mathbf{O}_{\text {min }} \subset$ out.

This finishes the proof of the proposition.
