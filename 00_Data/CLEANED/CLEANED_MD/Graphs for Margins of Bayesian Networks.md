# Graphs for margins of Bayesian networks 

Robin J. Evans<br>August 24, 2015


#### Abstract

Directed acyclic graph (DAG) models, also called Bayesian networks, impose conditional independence constraints on a multivariate probability distribution, and are widely used in probabilistic reasoning, machine learning and causal inference. If latent variables are included in such a model, then the set of possible marginal distributions over the remaining (observed) variables is generally complex, and not represented by any DAG. Larger classes of mixed graphical models, which use multiple edge types, have been introduced to overcome this; however, these classes do not represent all the models which can arise as margins of DAGs. In this paper we show that this is because ordinary mixed graphs are fundamentally insufficiently rich to capture the variety of marginal models.

We introduce a new class of hyper-graphs, called mDAGs, and a latent projection operation to obtain an mDAG from the margin of a DAG. We show that each distinct marginal of a DAG model is represented by at least one mDAG, and provide graphical results towards characterizing when two such marginal models are the same. Finally we show that mDAGs correctly capture the marginal structure of causally-interpreted DAGs under interventions on the observed variables.


## 1 Introduction

Directed acyclic graph (DAG) models, also known as Bayesian networks, are widely used in probabilistic reasoning, machine learning and causal inference (Bishop, 2007; Darwiche, 2009; Pearl, 2009). Their popularity stems from a relatively simple definition in terms of a Markov property, a modular structure which is computationally scalable, their nice statistical properties, and their intuitive causal interpretations.

DAG models are not closed under marginalization, in the sense that a margin of a joint distribution which obeys a DAG model will not generally be faithfully represented by any DAG. Indeed, although DAG models that include latent variables are widely used, they induce models over the observed variables that are extremely complicated, and not well understood.

Various authors have developed larger classes of graphical models to represent the result of marginalizing (and in some cases also conditioning) in Bayesian networks. In the context of causal models Pearl and Verma (Verma, 1991; Pearl and Verma, 1992; Pearl, 2009) introduced mixed graphs obtained

![img-0.jpeg](img-0.jpeg)

Figure 1: An mDAG with maximal non-trivial bidirected edges (facets) {a, c}, {c, d, e} and {d, e, f}.

by an operation called *latent projection* to represent the models induced by marginalizing. These have been developed into larger classes of graphical models such as summary graphs, MC-graphs, ancestral graphs and acyclic directed mixed graphs (ADMGs) which are closed under marginalization from the perspective of conditional independence constraints (Koster, 2002; Richardson and Spirtes, 2002; Richardson, 2003; Wermuth, 2011).

As has long been known, however, these models do not fully capture the range of marginal constraints imposed by DAG models. In this paper we show that no class of ordinary graphs is rich enough to do so, regardless of how many types of edge are used. Instead we introduce the mDAG, a hyper-graph which extends the idea of an ADMG to have hyper bidirected edges; an example is given in Figure 1. Intuitively, each red hyper-edge represents an exogenous latent variable whose children are the vertices joined by the edge.

We show that mDAGs are the natural graphical object to represent margins of DAG models. They are rich enough to represent the variety of models that can be induced observationally, and to graphically represent the effect of interventions when the DAG is interpreted causally. In addition, if the class of possible interventions is suitably defined, then there is a one-to-one correspondence between causally interpreted mDAGs and the marginal models induced by causally interpreted DAGs. The graphical framework also provides a platform for studying the models themselves, which are complex objects (see, for example, Evans, 2012; Shpitser et al., 2014). We provide some graphical results for Markov equivalence in this context, i.e. criteria for when two marginal models are equal, though a complete characterization remains an open problem.

As we shall see, marginal DAG models are relatively complex and there is, as yet, no general parameterization or fitting algorithm available to use with them; in contrast, explicit parametric incorporation of latent variables makes fitting relatively straightforward. However the latter approach has some disadvantages: most obviously it requires additional assumptions about the nature of the latent variables that may be implausible or untestable; additionally, the resulting models are typically not statistically regular (Drton, 2009). In con-

texts where the hidden variables represent arbitrary confounders whose nature is unknown - such as is common in epidemiological models - it may be preferable to use a marginal DAG model rather than an ordinary latent variable model. For these reasons marginal DAG models have attracted considerable interest, as the references in the previous paragraphs attest.

The remainder of the paper is organized as follows: in Section 2 we review directed acyclic graphs and their Markov properties; in Section 3 we consider latent variables, and discuss existing results in this area. Section 4 introduces mDAGs, and shows that they are rich enough to represent the class of models induced by margins of Bayesian networks, while Section 5 gives Markov properties for mDAGs. Section 6 considers Markov equivalence, and demonstrates that ordinary mixed graphical models cannot capture the full range of possible models. Section 7 extends the interpretation of these models to causal settings, and Section 8 contains a discussion including some open problems.

# 2 Directed Graphical Models 

We begin with a review of definitions concerning directed acyclic graphs. We omit examples of many of these ideas because these are well known but see, for example, Richardson and Spirtes (2002) or Pearl (2009) for more detail.

Definition 2.1. A directed graph $\mathcal{D}$ is a pair $(V, \mathcal{E})$, where $V$ is a finite set of vertices and $\mathcal{E}$ a collection of edges, which are ordered pairs of vertices. If $(v, w) \in \mathcal{E}$ we write $v \rightarrow w$. Self-loops are not allowed: that is $(v, v) \notin \mathcal{E}$ for any $v$. A graph is acyclic if it does not contain any sequences of edges of the form $v_{1} \rightarrow \cdots \rightarrow v_{k} \rightarrow v_{1}$ with $k>1$. We call such a graph a directed acyclic graph (DAG); all the directed graphs considered in this paper are acyclic.

A path from $v_{0}$ to $v_{k}$ is an alternating sequence of vertices and edges $\left\langle v_{0}, e_{1}, v_{1} \ldots, e_{k}, v_{k}\right\rangle$, such that each edge $e_{i}$ is between the vertices $v_{i-1}$ and $v_{i}$; no repetition of vertices (or, therefore, of edges) is permitted. A path may contain zero edges: i.e. $\left\langle v_{0}\right\rangle$ is a path from $v_{0}$ to itself. $v_{0}$ and $v_{k}$ are the endpoints of the path, and any other vertices are non-endpoints. A path is directed from $v_{0}$ to $v_{k}$ if it is of the form $v_{0} \rightarrow v_{1} \rightarrow \cdots \rightarrow v_{k}$.

If $v \rightarrow w$ then $v$ is a parent of $w$, and $w$ a child of $v$. The set of parents of $w$ is denoted by $\mathrm{pa}_{\mathcal{D}}(w)$, and the set of children of $v$ by $\operatorname{ch}_{\mathcal{D}}(v)$. If there is a directed path from $v$ to $w$ (including the case $v=w$ ), we say that $v$ is an ancestor ${ }^{1}$ of $w$. The set of ancestors of $w$ is denoted by $\operatorname{an}_{\mathcal{D}}(w)$. We apply these definitions disjunctively to sets of vertices so that

$$
\operatorname{pa}_{\mathcal{D}}(A)=\bigcup_{a \in A} \operatorname{pa}_{\mathcal{D}}(a), \quad \quad \operatorname{an}_{\mathcal{D}}(A)=\bigcup_{a \in A} \operatorname{an}_{\mathcal{D}}(a)
$$

A set is called ancestral if it contains all its own ancestors: $A=\operatorname{an}_{\mathcal{D}}(A)$.

[^0]
[^0]:    ${ }^{1}$ Note that $w$ is always an ancestor of itself, which differs from the convention used by some authors (e.g. Lauritzen, 1996).

Given DAGs $\mathcal{D}(V, \mathcal{E})$ and $\mathcal{D}^{\prime}\left(V^{\prime}, \mathcal{E}^{\prime}\right)$, we say that $\mathcal{D}^{\prime}$ is a subgraph of $\mathcal{D}$, and write $\mathcal{D}^{\prime} \subseteq \mathcal{D}$, if $V^{\prime} \subseteq V$ and $\mathcal{E}^{\prime} \subseteq \mathcal{E}$. The induced subgraph of $\mathcal{D}$ over $A \subseteq V$ is the DAG $\mathcal{D}_{A}$ with vertices $A$ and edges $\mathcal{E}_{A}=\{(v, w) \in \mathcal{E}: v, w \in A\}$; that is, those edges with both endpoints in $A$.

A graphical model arises when a graph is identified with structure on a multivariate probability distribution. With each vertex $v$ we associate a random variable $X_{v}$ taking values in some set $\mathcal{X}_{v}$; the joint distribution is over the product space $\mathcal{X}_{V}=\times_{v \in V} \mathcal{X}_{v}$. In DAGs the structure takes the form of each variable $X_{v}$ 'depending' only upon the random variables $X_{\mathrm{pa}(v)}$ corresponding to its immediate parents in the graph. Unless explicitly stated otherwise we make no assumption about the state-space of each of the random variables $X_{v}$, save that we work with Lebesgue-Rokhlin probability spaces. Hence $X_{v}$ could be discrete, one-dimensional real, vector-valued, or a countably generated process such as a Brownian motion (see Rokhlin, 1952, Section 2).

Definition 2.2 (Structural Equation Property). Let $\mathcal{D}$ be a DAG with vertices $V$, and $\mathcal{X}_{V}$ a Cartesian product space. We say that a joint distribution $P$ over $\mathcal{X}_{V}$ satisfies the structural equation property (SEP) for $\mathcal{D}$ if for some independent random variables $E_{v}$ (the error variables) taking values in $\mathscr{E}_{v}$, and measurable functions $f_{v}: \mathcal{X}_{\mathrm{pa}(v)} \times \mathscr{E}_{v} \rightarrow \mathcal{X}_{v}$, recursively setting

$$
X_{v}=f_{v}\left(X_{\mathrm{pa}(v)}, E_{v}\right), \quad v \in V
$$

gives $X_{V}$ the joint distribution $P$. Equivalently, each $X_{v}$ is $\sigma\left(X_{\mathrm{pa}(v)}, E_{v}\right)$ measurable, where $\sigma(Y)$ denotes the $\sigma$-algebra generated by the random variable $Y$. We denote the collection of such distributions (the structural equation model for $\mathcal{D}$ ) by $\mathcal{M}_{s e}(\mathcal{D})$.

Remark 2.3. The fact that we can use this recursive definition follows from the fact that the graph is acyclic.

Although in principle the error variables have arbitrary state-space, it follows from the discussion in Chentsov (1982, Section 2.11) that there is no loss of generality if they are assumed to be uniformly distributed on $(0,1)$.

Note that the structural equation model for $\mathcal{D}$ does not require that a joint density for $X_{V}$ exists, and in particular allows for degenerate relationships such as functional dependence between two variables. If a joint density with respect to a product measure does exist, then the model is equivalent to that defined by requiring the usual factorization of the joint density (Pearl, 2009).

Remark 2.4. The potential outcomes view of causal inference (Rubin, 1974) considers the random function $f_{v}\left(\cdot, E_{v}\right): \mathcal{X}_{\mathrm{pa}(v)} \rightarrow \mathcal{X}_{v}$, generally denoted by $X_{v}(\cdot)=f_{v}\left(\cdot, E_{v}\right)$, as the main unit of interest. Under our formulation this is almost surely measurable, and we can identify the pair $\left(f_{v}, E_{v}\right)$ with $X_{v}(\cdot)$.

In general, some care is needed when defining random functions: one might naïvely choose to set, for example, $X_{v}\left(x_{\mathrm{pa}(v)}\right) \sim N(0,1)$ independently for each $x_{\mathrm{pa}(v)} \in \mathcal{X}_{\mathrm{pa}(v)}$; however if the indexing set $\mathcal{X}_{\mathrm{pa}(v)}$ is continuous, then the

function $X_{v}(\cdot)$ will almost surely not be Lebesgue measurable, and therefore $X_{v}\left(X_{\mathrm{pa}(v)}\right)$ is not a random variable.

The structural equation model implies that each random variable is a measurable function of its parents in the graph; it is therefore clear that, conditional upon its parents, each variable is independent of the other variables already defined. Pearl (1985) introduced 'd-separation' as a method for interrogating Bayesian networks about their conditional independence implications. The resulting Markov property is equivalent to the structural equation property, but it is often easier to work with in practice.

Definition 2.5. Let $\pi$ be a path from $v$ to $w$, and let $a$ be a non-endpoint on $\pi$. We say $a$ is a collider on the path if the two edges in $\pi$ which contain $a$ are both oriented towards it: i.e. $\rightarrow a \leftarrow$. Otherwise (i.e. if $\rightarrow a \rightarrow ; \leftarrow a \rightarrow$; or $\leftarrow a \leftarrow$ ) we say $a$ is a non-collider.

Definition 2.6 (d-separation). Let $\pi$ be a path from $a$ to $b$ in a DAG $\mathcal{D}$; we say that $\pi$ is blocked by a (possibly empty) set $C \subseteq V \backslash\{a, b\}$ if either (i) there is a non-collider on $\pi$ which is also in $C$, or (ii) there is a collider on the path which is not contained in $\operatorname{an}_{\mathcal{D}}(C)$.

Sets $A$ and $B$ are said to be $d$-separated given $C$ if all paths from any $a \in A$ to any $b \in B$ are blocked by $C$.

Definition 2.7 (Global Markov Property). Let $\mathcal{D}$ be a DAG and $X_{V}$ random variables under a joint probability measure $P$. We say that $P$ obeys the global Markov property for $\mathcal{D}$ if

$$
X_{A} \pm X_{B} \mid X_{C}[P]
$$

whenever $A$ and $B$ are d-separated by $C$ in $\mathcal{D}$. Denote the collection of probability measures that satisfy the global Markov property by $\mathcal{M}_{g}(\mathcal{D})$.

In fact $\mathcal{M}_{g}(\mathcal{D})=\mathcal{M}_{\text {se }}(\mathcal{D})$, so the structural equation property and the global Markov property are equivalent (Lauritzen et al., 1990). We use $\mathcal{M}(\mathcal{D})$ to denote these equivalent models.

# 3 Latent Variables 

In a great many practical statistical applications it is necessary to include unmeasured random variables in a model to correctly capture the dependence structure among observed variables. Consider a DAG $\mathcal{D}$ with vertices $V \dot{\cup} U$, and suppose that $\left(X_{V}, X_{U}\right) \sim P \in \mathcal{M}(\mathcal{D})$ (here and throughout $\dot{U}$ represents a union of disjoint sets). What restrictions does this place on the marginal distribution of $X_{V}$ under $P$ ? In this context we call $V$ the observed vertices, and $X_{V}$ the observed variables; similarly $U$ (respectively $X_{U}$ ) are the unobserved or latent vertices (variables).

Definition 3.1. Let $\mathcal{D}$ be a DAG with vertices $V \cup U$, and $\mathcal{X}_{V}$ a state-space for $V$. Define the marginal $D A G$ model $\mathcal{M}(\mathcal{D}, V)$ by the collection of probability distributions $P$ over $\mathcal{X}_{V}$ such that there exist
(i) some state-space $\mathcal{X}_{U}$ for $X_{U}$; and
(ii) a probability measure $Q \in \mathcal{M}(\mathcal{D})$ over $\mathcal{X}_{V} \times \mathcal{X}_{U}$;
and $P$ is the marginal distribution of $Q$ over $X_{V}$.
In other words, we need to construct $\left(X_{U}, X_{V}\right)$ with joint distribution $Q \in$ $\mathcal{M}(\mathcal{D})$ such that $X_{V} \sim P$. Trivially, if $U=\emptyset$ then everything is observed and $\mathcal{M}(\mathcal{D}, V)=\mathcal{M}(\mathcal{D})$. The problem of interest is to characterize the set $\mathcal{M}(\mathcal{D}, V)$ in general.

Remark 3.2. Note that we allow the state-space of the latent variables to be arbitrary in principle (though see Remark 2.3) and the model is nonparametric. Typical latent variable models either assume a fixed finite number of levels for the latents, or invoke some other parametric structure such as Gaussianity. Such models are useful in many contexts, but have various disadvantages if the aim is to remain agnostic as to the precise nature of the unobserved variables. In general any latent variable model will be a sub-model of the marginal DAG model, and may impose additional constraints on the observed joint distribution (see, for example, Allman et al., 2013). This is clearly undesirable if it is simply an artefact of an arbitrary and untested parametric structure applied to unmeasured variables. In addition, latent variable models are often not regular and may have poor statistical properties, such as nonstandard asymptotics (Drton, 2009). The regularity of marginal DAG models has not been established in general, but is known in some special cases (Evans, 2015).

The following proposition shows that taking margins with respect to ancestral sets preserves the structure of the original graph, representing an important special case. The result is well known, see for example Richardson and Spirtes (2002).

Proposition 3.3. Let $\mathcal{D}$ and $\mathcal{D}^{\prime}$ be DAGs with the same vertex set $V$.
(a) If $A \subseteq V$ is an ancestral set in $\mathcal{D}$, then $\mathcal{M}(\mathcal{D}, A)=\mathcal{M}\left(\mathcal{D}_{A}\right)$.
(b) If $\mathcal{D}^{\prime} \subseteq \mathcal{D}$, then $\mathcal{M}\left(\mathcal{D}^{\prime}\right) \subseteq \mathcal{M}(\mathcal{D})$.

Proof. These both follow directly from the definition of the structural equation property, since each variable depends only upon its parents. For the first claim it is clear from the recursive form of the SEP that the restrictions on $X_{A}$ are identical for $\mathcal{D}$ and $\mathcal{D}_{A}$ if $A$ is ancestral.

For the second claim, note that since $\operatorname{pa}_{\mathcal{D}^{\prime}}(w) \subseteq \operatorname{pa}_{\mathcal{D}}(w)$, any $\sigma\left(X_{\operatorname{pa}_{\mathcal{D}^{\prime}}(w)}, E_{w}\right)$ measurable random variable must also be $\sigma\left(X_{\operatorname{pa}_{\mathcal{D}}(w)}, E_{w}\right)$-measurable.

![img-1.jpeg](img-1.jpeg)

Figure 2: A DAG $\mathcal{K}$ with hidden vertices.
![img-2.jpeg](img-2.jpeg)

Figure 3: A directed acyclic graph on five vertices.

Example 3.4. Consider the DAG $\mathcal{K}$ shown in Figure 2, which contains five vertices. We claim that the model defined by the margin of this graph over the vertices $\{1,2,3\}$ is precisely those distributions for which $X_{1} \Perp X_{2}$. To see this, first note that from the global Markov property for $\mathcal{K}$, any distribution in $\mathcal{M}(\mathcal{K},\{1,2,3\})$ must satisfy $X_{1} \Perp X_{2}$.

Conversely, suppose that $P$ is a distribution on $\left(X_{1}, X_{2}, X_{3}\right)$ such that $X_{1} \Perp$ $X_{2}$; now let $\left(X_{4}, X_{5}, X_{3}\right) \sim P$ so that $X_{4} \Perp X_{5}$; by Proposition 3.3(a) and the global Markov property the distribution of $\left(X_{3}, X_{4}, X_{5}\right)$ satisfies the Markov property for the ancestral subgraph $4 \rightarrow 3 \leftarrow 5$. Setting $X_{1}=X_{4}$ and $X_{2}=X_{5}$ is consistent with the structural equation property for $\mathcal{K}$, so it follows that the joint distribution of $\left(X_{1}, \ldots, X_{5}\right)$ is contained in $\mathcal{M}(\mathcal{K})$, and that $\left(X_{1}, X_{2}, X_{3}\right) \sim P$. Hence $P \in \mathcal{M}(\mathcal{K},\{1,2,3\})$.

Even in small problems, explicitly characterizing the margin of a DAG model can be quite tricky, as the following example shows.

Example 3.5. Consider the DAG $\mathcal{D}$ in Figure 3, and the marginal model $\mathcal{M}(\mathcal{D},\{1,2,3,4\})$. By applying the global Markov property to $\mathcal{D}$, one can see that any joint distribution satisfies $X_{1} \Perp X_{3} \mid X_{2}$, so this also holds for any marginal distribution. It was also shown by Robins (1986) that any such distribution with a positive probability density must also satisfy a non-parametric constraint that the quantity

$$
q\left(x_{3}, x_{4}\right) \equiv \int p_{2}\left(x_{2} \mid x_{1}\right) \cdot p_{4}\left(x_{4} \mid x_{1}, x_{2}, x_{3}\right) d x_{2}
$$

is independent of $x_{1}$ (here $p_{2}$ and $p_{4}$ represent the relevant conditional densities). This does not correspond to an ordinary conditional independence, and is known as a Verma constraint after Verma and Pearl (1990) who introduced it to the computer science literature.

# 3.1 Existing Results 

Margins of DAG models are of considerable interest because of their relationship to causal models under confounding, and consequently have been well studied. Restricting to implications of d-separation applied to the observed variables leads to a pure conditional independence model; this is a super-model of the marginal DAG model (so for Example 3.5 we would just find $X_{1} \Perp X_{3} \mid X_{2}$, for instance). This class, which we refer to as ordinary Markov models, was the subject of the work by Richardson (2003) and Evans and Richardson (2014) (see also Richardson and Spirtes, 2002).

Constraints of the kind given in Example 3.5 can be generalized via the algorithm of Tian and Pearl (2002), and when used to augment the ordinary Markov model yield nested Markov models (Shpitser et al., 2014); these models are defined in Section 5. For discrete variables both ordinary and nested Markov models are curved exponential families, and can be parameterized and fitted using the methods of Evans and Richardson (2010, 2014); see also Shpitser et al. (2013). Evans (2015) shows that, up to inequality constraints, nested models are the same as marginal DAG models when the observed variables are discrete ${ }^{2}$ : so, for example, the model in Example 3.5 has no equality constraints beyond the conditional independence and (1).

In addition to conditional independences and Verma constraints, margins also exhibit inequality constraints. These were first identified by Bell (1964), and the earliest example in the context of graphical models was the instrumental inequality of Pearl (1995). Evans (2012) extended Pearl's work to general DAG models and gave a graphical criterion similar to d-separation for detecting inequality constraints. Further inequalities are given in Fritz (2012). Bonet (2001) showed that a full derivation of inequalities in these models is likely to be very complicated in general. An alternative approach using information theory, also for discrete variables, is given by Chaves et al. (2014).

A related problem to the one we consider here arises when observed and latent variables are assumed to be jointly Gaussian. Again one can define an 'ordinary model' using conditional independence constraints, which is larger than the marginal model but can be smoothly parameterized using the results in Richardson and Spirtes (2002). However margins of these models also induce Verma constraints and inequalities, as well as more exotic constraints (see 8.3.1 of Richardson and Spirtes, 2002); an overview is given in Drton et al. (2012). Fox et al. (2014) characterize these models in a fairly large class of graphs, though the general case remains an open problem.

### 3.2 Reduction

It might seem that to characterize general models of the form $\mathcal{M}(\mathcal{D}, V)$ we will have to consider an infinite collection of models with arbitrarily many latent variables, making the problem extremely hard. However the three results in this subsection show that without any loss of generality we can assume latent

[^0]
[^0]:    ${ }^{2}$ In algebraic language, the marginal and nested models have the same Zariski closure.

![img-3.jpeg](img-3.jpeg)

Figure 4: (a) A DAG, $\mathcal{D}$, and (b) the exogenized version $\mathfrak{r}(\mathcal{D}, u)$. The two DAGs induce the same marginal model over the vertices $\left\{l_{1}, l_{2}, k_{1}, k_{2}, k_{3}\right\}$.
variables to be exogenous (that is, they have no parents), and that for a fixed number of observed variables, the number of latent variables can be limited to a finite value. This is in the spirit of the latent projection operation used in Pearl (2009).

Definition 3.6. Let $\mathcal{D}$ be a DAG containing a vertex $u$. Define the exogenized $D A G \mathfrak{r}(\mathcal{D}, u)$ as follows: take the vertices and edges of $\mathcal{D}$, and then (i) add an edge $l \rightarrow k$ from every $l \in \mathrm{pa}_{\mathcal{D}}(u)$ to $k \in \operatorname{ch}_{\mathcal{D}}(u)$ (if necessary), and (ii) delete any edge $l \rightarrow u$ for $l \in \mathrm{pa}_{\mathcal{D}}(u)$. All other edges are as in $\mathcal{D}$.

In other words, we join all parents of $u$ to all children of $u$ with directed edges, and then remove edges between $u$ and its parents; the process is most easily understood visually: see the example in Figure 4. Note that if $u$ has no parents in $\mathcal{D}$, then $\mathfrak{r}(\mathcal{D}, u)=\mathcal{D}$.

Lemma 3.7. Let $\mathcal{D}$ be a $D A G$ with vertices $V \dot{\cup}\{u\}$, and $\tilde{\mathcal{D}} \equiv \mathfrak{r}(\mathcal{D}, u)$. Then $\mathcal{M}(\mathcal{D}, V)=\mathcal{M}(\tilde{\mathcal{D}}, V)$; i.e. the marginal models induced by the two graphs over $V$ are the same.

Proof. If $u$ has no parents in $\mathcal{D}$ then the result is trivial, since $\mathcal{D}=\tilde{\mathcal{D}}$. Otherwise let $L=\mathrm{pa}_{\mathcal{D}}(u)$ and $K=\operatorname{ch}_{\mathcal{D}}(u)$. Suppose $P \in \mathcal{M}(\mathcal{D}, V)$, so one can construct $\left(X_{u}, X_{V}\right) \sim Q \in \mathcal{M}(\mathcal{D})$ such that $X_{V} \sim P$. Let $Q$ be generated using the SEP by independent error variables $\left(E_{v}: v \in V \cup\{u\}\right)$, so that each $X_{v}$ is $\sigma\left(X_{\mathrm{pa}_{\mathcal{D}}(v)}, E_{v}\right)$-measurable.

Now let $\tilde{X}_{u}=E_{u}$, and all other $X_{v}$ remain unchanged, so that $\tilde{X}_{u}$ is $\sigma\left(E_{u}\right)$ measurable. The only other variables whose parents sets are different in $\tilde{\mathcal{D}}$ are those in $K$, so we need only show that $X_{k}$ is $\sigma\left(\tilde{X}_{u}, X_{L}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right)$ measurable for $k \in K$. Since $X_{u}$ is $\sigma\left(X_{L}, E_{u}\right)=\sigma\left(X_{L}, \tilde{X}_{u}\right)$-measurable, it follows that

$$
\sigma\left(X_{u}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right) \subseteq \sigma\left(\tilde{X}_{u}, X_{L}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right)
$$

![img-4.jpeg](img-4.jpeg)

Figure 5: Two DAGs whose marginal models over the vertices $\left\{v_{1}, v_{2}, v_{3}\right\}$ are the same.
$X_{k}$ is $\sigma\left(X_{u}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right)$-measurable by the definition of $\mathcal{M}(\mathcal{D})$, so it is also $\sigma\left(\tilde{X}_{u}, X_{L}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right)$-measurable. The joint distribution $\tilde{Q}$ of $\left(\tilde{X}_{u}, X_{V}\right)$ is therefore contained in $\mathcal{M}(\tilde{\mathcal{D}})$, and so $P \in \mathcal{M}(\tilde{\mathcal{D}}, V)$.

Conversely, if $\left(\tilde{X}_{u}, X_{V}\right) \sim \tilde{Q} \in \mathcal{M}(\tilde{\mathcal{D}})$, let $E_{u}=\tilde{X}_{u}$, and $X_{u}=\left(X_{L}, \tilde{X}_{u}\right)$; then $E_{u}$ is independent of other error variables, and $X_{u}$ is $\sigma\left(X_{L}, E_{u}\right)$-measurable. For $k \in K$,

$$
\sigma\left(X_{u}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right) \supseteq \sigma\left(\tilde{X}_{u}, X_{L}, X_{\mathrm{pa}_{\mathcal{D}}(k)}, E_{k}\right)
$$

so $\left(X_{u}, X_{V}\right) \sim Q \in \mathcal{M}(\mathcal{D})$.
As a consequence of this lemma it is sufficient to consider models in which the unobserved vertices are exogenous. Our second result shows that only a finite number of exogenous latent variables are necessary.

Lemma 3.8. Let $\mathcal{D}$ be a $D A G$ with vertices $V \dot{\cup}\{u, w\}$ (where $u \neq w$ ), such that $\mathrm{pa}_{\mathcal{D}}(w)=\mathrm{pa}_{\mathcal{D}}(u)=\emptyset$ and $\operatorname{ch}_{\mathcal{D}}(w) \subseteq \operatorname{ch}_{\mathcal{D}}(u)$. Then $\mathcal{M}(\mathcal{D}, V)=\mathcal{M}\left(\mathcal{D}_{-w}, V\right)$, where $\mathcal{D}_{-w}$ is the induced subgraph of $\mathcal{D}$ after removing $w$.

Proof. By Proposition 3.3(b), $\mathcal{M}\left(\mathcal{D}_{-w}, V\right) \subseteq \mathcal{M}(\mathcal{D}, V)$. Take $P \in \mathcal{M}(\mathcal{D}, V)$, so that there exists $\left(X_{V}, X_{u}, X_{w}\right) \sim Q \in \mathcal{M}(\mathcal{D})$ whose $V$-margin is $P$. Letting $\tilde{X}_{u}=\left(X_{u}, X_{w}\right)$ note that $\left(X_{V}, \tilde{X}_{u}\right)$ satisfies the SEP for $\mathcal{D}_{-w}$. Hence $P \in$ $\mathcal{M}\left(\mathcal{D}_{-w}, V\right)$

This result, combined with Lemma 3.7, shows that for a fixed set of observed variables $V$, there are only finitely many distinct models of the form $\mathcal{M}(\mathcal{D}, V)$. In particular, all unobserved vertices may be assumed to be exogenous, and their child sets to correspond to maximal sets of observed vertices. An example of two DAGs shown to have equal marginal models by this result is given in Figure 5.

We can make one final simplification, again without any loss of generality.
Lemma 3.9. Let $\mathcal{D}$ be a $D A G$ with vertices $V \dot{\cup}\{u\}$, such that $u$ has no parents and at most one child. Then $\mathcal{M}(\mathcal{D}, V)=\mathcal{M}\left(\mathcal{D}_{-u}, V\right)$.

Proof. $\mathcal{M}\left(\mathcal{D}_{-u}, V\right) \subseteq \mathcal{M}(\mathcal{D}, V)$, so suppose $P \in \mathcal{M}(\mathcal{D}, V)$. For the unique $v \in \operatorname{ch}_{\mathcal{D}}(u)$ (if indeed there is any such $v$ ), let $\tilde{E}_{v}=\left(E_{v}, E_{u}\right)$, so $\tilde{E}_{v} \perp$ $\left(E_{w}: w \in V\right)$, and $X_{v}$ is $\sigma\left(X_{\mathrm{pa}(v)}, E_{v}\right)=\sigma\left(X_{\mathrm{pa}(v) \backslash u}, \tilde{E}_{v}\right)$-measurable. Then $P \in \mathcal{M}(\mathcal{D}, V)$.

The combination of these results means that we can restrict our attention to models in which the latent variables are exogenous, and have nonnested sets of children of size at least two. A similar conclusion is reached by Pearl and Verma (1992), but the authors also claim that each latent variable can be assumed to have exactly two children. In the context of models of conditional independence this is correct, but in general it is too restrictive, as we show in Section 6.1.

# 4 mDAGs 

The results of the previous section suggest a way to construct a new class of graph, rich enough to represent the distinct models that can arise as the margins of DAGs. First we define the following abstract object, which will be used to represent latent structure.

Definition 4.1. A simplicial complex (or abstract simplicial complex), $\mathcal{B}$, over a finite set $V$ is a collection of non-empty subsets of $V$ such that
(i) $\{v\} \in \mathcal{B}$ for all $v \in V$;
(ii) for non-empty sets $A \subseteq B \subseteq V$ we have $B \in \mathcal{B} \Longrightarrow A \in \mathcal{B}$.

The inclusion maximal elements of $\mathcal{B}$ are called facets. Any simplicial complex $\mathcal{B}$ can be characterized by its non-trivial facets (i.e. those of size at least 2), denoted by $\overline{\mathcal{B}}$.

Definition 4.2. An $m D A G$ (marginalized DAG) $\mathcal{G}$ is a triple $(V, \mathcal{E}, \mathcal{B})$, where $(V, \mathcal{E})$ defines a DAG, and $\mathcal{B}$ is an abstract simplicial complex on $V$. The elements of $\mathcal{B}$ are called the bidirected faces.

DAGs correspond to mDAGs whose bidirected faces are just singleton vertices: $\mathcal{B}=\{\{v\}: v \in V\}$. We can represent an mDAG as a graph with ordinary directed edges $\mathcal{E}$, and bidirected hyper-edges corresponding to the non-trivial facets $\overline{\mathcal{B}}$. We call $(V, \mathcal{E})$ the underlying $D A G$, and draw its edges in blue; the bidirected hyper-edges are in red. See the example in Figure 1. If $w$ has no parents and $\{w\}$ is a facet of $\mathcal{B}$, we say that $w$ is exogenous. Informally we may think of each facet $B$ as representing a latent variable with children $B$. The definitions of parents, children, ancestors and ancestral sets are extended to mDAGs by applying them to the underlying DAG, ignoring the bidirected faces.

Visually, there is some resemblance between the bidirected hyper-edges in mDAGs and the factor nodes in factor graphs, but this similarity is only

superficial: for example, factor graphs do not require inclusion maximality (Kschischang et al., 2001).

If we restrict the facets of $\mathcal{B}$ to have size at most 2 (so that $\mathcal{B}$ is an 'edge complex'), then the definition of an mDAG is isomorphic to that of an acyclic directed mixed graph or ADMG (Richardson, 2003). Clearly then, mDAGs are a richer class of graphs: the relationship between mDAGs and ADMGs is explained further in Section 6.1.

Definition 4.3 (Subgraph). Let $\mathcal{G}(V, \mathcal{E}, \mathcal{B})$ and $\mathcal{H}\left(V^{\prime}, \mathcal{E}^{\prime}, \mathcal{B}^{\prime}\right)$ be mDAGs. Say that $\mathcal{H}$ is a subgraph of $\mathcal{G}$, and write $\mathcal{H} \subseteq \mathcal{G}$, if $V^{\prime} \subseteq V, \mathcal{E}^{\prime} \subseteq \mathcal{E}$, and $\mathcal{B}^{\prime} \subseteq \mathcal{B}$.

The induced subgraph of $\mathcal{G}$ over $A \subseteq V$ is the mDAG defined by the induced underlying $\operatorname{DAG}\left(A, \mathcal{E}_{A}\right)$ and bidirected faces $\mathcal{B}_{A}=\{B \subseteq A: B \in \mathcal{B}\}$. In other words, taking those parts of each edge which intersect with the vertices in $A$.

# 4.1 Latent Projection 

We now relate margins of DAG to mDAGs, via an operation called latent projection. This is based on the approach taken by Pearl (2009), but allows for joint dependence of more than two variables due to a common 'cause' or ancestor.

Definition 4.4. Let $\mathcal{G}$ be an mDAG with bidirected faces $\mathcal{B}$, and let $W, U$ be disjoint sets of vertices in $\mathcal{G}$. We say that the vertices in $W$ share a hidden common cause in $\mathcal{G}$, with respect to $U$, if there exists a set $B \in \mathcal{B}$ such that
(i) $B \subseteq U \dot{\cup} W$; and
(ii) for each $w \in W$ there is a directed path $\pi_{w}$ from some $b \in B$ to $w$, with all vertices on $\pi_{b}$ being in $U \cup\{w\}$.

If $\mathcal{G}$ is a DAG, a hidden common cause is a common ancestor $a \in V$ of each $w \in W$, where $a$ and the vertices on a directed path between $a$ and $w$ are unobserved. Note that if $W \in \mathcal{B}$ then $W$ is trivially a hidden common cause with respect to any $U \subseteq V \backslash W$.

The concept of a hidden common cause is similar to a system of treks which induce latent correlation; see, for example, Foygel et al. (2012). The difference is that treks only consider pairwise dependence, not dependence between an arbitrary collection of variables.

Example 4.5. Let $\mathcal{G}$ be the DAG in Figure 6(a). The vertices $W=\{3,4,5,6\}$ share a hidden common cause $B=\{1\}$ with respect to $U=\{1,2\}$. In the mDAG in Figure 6(c) the set of vertices $W=\{3,4,5,6\}$ share a hidden common cause in the bidirected facet $\{2,3,4\}$, with respect to $\{2\}$.

The hidden common cause forms the basis for determining which vertices should share a bidirected face in an mDAG after projecting out some of the variables. We formalize this with the next definition.

![img-5.jpeg](img-5.jpeg)

Figure 6: (a) A DAG on seven vertices, and (b) its latent projection to an mDAG over $\{1,3,4,5,6,7\}$, (c) over $\{2,3,4,5,6,7\}$ and (d) over $\{3,4,5,6,7\}$.

Definition 4.6. Let $\mathcal{G}$ be an mDAG with vertices $V \dot{\cup} U$. The latent projection of $\mathcal{G}$ onto $V$, denoted by $\mathfrak{p}(\mathcal{G}, V)$, is an mDAG with vertices $V$, and edges $\mathcal{E}^{\prime}$ and bidirected faces $\mathcal{B}^{\prime}$ defined as follows:

- $(a, b) \in \mathcal{E}^{\prime}$ whenever $a \neq b$ and there is a directed path $a \rightarrow \cdots \rightarrow b$ in $\mathcal{G}$, with all non-endpoints in $U$;
- $W \in \mathcal{B}^{\prime}$ whenever the vertices $W \subseteq V$ share a hidden common cause in $\mathcal{G}$ with respect to $U$.

It is straightforward to see that $\mathcal{B}^{\prime}$ is an abstract simplicial complex, and therefore the definition above gives an mDAG.

Example 4.7. Consider the mDAG in Figure 6(a), and its latent projection after projecting out the vertex 2, shown in Figure 6(b). In the original graph the directed paths $7 \rightarrow 2 \rightarrow 5$ and $7 \rightarrow 2 \rightarrow 6$ are manifested as the directed edges $7 \rightarrow 5$ and $7 \rightarrow 6$ in the projection. Additionally, there is a hidden common cause for the vertices 5,6 (as noted in the previous example), so we end up with a bidirected facet $\{5,6\}$ in the projection. The projection of the graph in Figure 6(b) onto $\{3,4,5,6,7\}$ is shown in (d).

Definition 4.8. Let $\mathcal{G}(V, \mathcal{E}, \mathcal{B})$ be an mDAG with bidirected facets $\overline{\mathcal{B}}$. We define $\overline{\mathcal{G}}$, the canonical $D A G$ associated with $\mathcal{G}$, as the DAG with vertices $V \cup \overline{\mathcal{B}}$ and edges

$$
\mathcal{E} \cup\{B \rightarrow v: v \in B \in \overline{\mathcal{B}}\}
$$

![img-6.jpeg](img-6.jpeg)

Figure 7: The canonical DAG associated with the mDAG in Figure 1.

In other words, we replace every non-trivial facet $B \in \mathcal{B}$ with a vertex whose children are precisely the elements of $B$. The canonical DAG associated with the mDAG from Figure 1 is shown in Figure 7.

Proposition 4.9. Let $\mathcal{G}$ be an $m D A G$ with vertex set $V$.
(a) $\mathcal{H} \subseteq \mathcal{G} \Longrightarrow \mathfrak{p}(\mathcal{H}, W) \subseteq \mathfrak{p}(\mathcal{G}, W)$ for any $W \subseteq V$;
(b) $\mathfrak{p}(\overline{\mathcal{G}}, V)=\mathcal{G}$;
(c) if $A \subseteq V$ is an ancestral set in $\mathcal{G}$, then $\mathfrak{p}(\mathcal{G}, A)=\mathcal{G}_{A}$.

Proof. (a): If $\mathcal{H}$ is a subgraph of $\mathcal{G}$, then any directed path or hidden common cause in $\mathcal{H}$ must also be found in $\mathcal{G}$.
(b): Since $\overline{\mathcal{G}}$ is a DAG on vertices $V \cup \overline{\mathcal{B}}$ and no $B \in \overline{\mathcal{B}}$ has any parents in $\overline{\mathcal{G}}$, the only directed edges added in $\mathfrak{p}(\overline{\mathcal{G}}, V)$ are those already joining elements of $V$ in $\overline{\mathcal{G}}$, and therefore are precisely the directed edges in $\mathcal{G}$. The only hidden common causes with respect to $\overline{\mathcal{B}}$ are singletons $\{v\}$ and subsets of any $B \in \overline{\mathcal{B}}$, whose children are all observed. Hence the bidirected faces in $\mathfrak{p}(\overline{\mathcal{G}}, V)$ are precisely $\mathcal{B}$.
(c): Since $A$ is ancestral, any directed paths between elements of $A$ have all vertices in $A$, and there are no directed paths from $V \backslash A$ to $A$ (hence there are no hidden common causes).

A critical fact about latent projection is that it does not matter in what order we project out vertices, or indeed if we do several at once.

Theorem 4.10. Let $\mathcal{G}$ be an $m D A G$ with vertices $V \dot{\cup} U_{1} \dot{\cup} U_{2}$. Then

$$
\mathfrak{p}(\mathcal{G}, V)=\mathfrak{p}\left(\mathfrak{p}\left(\mathcal{G}, V \cup U_{1}\right), V\right)=\mathfrak{p}\left(\mathfrak{p}\left(\mathcal{G}, V \cup U_{2}\right), V\right)
$$

That is, the order of projection does not matter.
The proof of this result is found in the Appendix. The commutativity is illustrated in Figure 6: if we first project out 1 and then 2 from the DAG

(a) we obtain the mDAGs in (c) and then (d) respectively. If the order of projection is reversed we obtain the mDAGs in (b) and then (d).

A second crucial fact is that if two DAGs have the same latent projection onto a set $V$, then their marginal models over $V$ are also the same. To prove this we use the following two lemmas, which show that two different DAGs result in the same mDAG if their margins are equivalent by Lemmas 3.7, 3.8 and 3.9 .

Lemma 4.11. Let $\mathcal{D}$ be a $D A G$ with vertices $V \dot{\cup}\{u\}$, and $\mathfrak{r}(\mathcal{D}, u)$ the exogenized $D A G$ for $u$. Then

$$
\mathfrak{p}(\mathcal{D}, V)=\mathfrak{p}(\mathfrak{r}(\mathcal{D}, u), V)
$$

Proof. From the definition of $\mathfrak{r}$, any directed paths passing through $u$ as an intermediate node $l \rightarrow u \rightarrow k$ in $\mathcal{D}$ are replaced by $l \rightarrow k$ in $\mathfrak{r}(\mathcal{D}, u)$. Hence the directed edges in both projections are the same.

The only vertex being projected out is $u$ and since its child set is the same in both $\mathcal{D}$ and $\mathfrak{r}(\mathcal{D}, u)$, the groups of vertices sharing a hidden common cause with respect to $\{u\}$ will remain unchanged. Hence the bidirected faces in both projections are the same.

Lemma 4.12. Let $\mathcal{G}$ be an $m D A G$ with vertices $V \dot{U} U$, containing an exogenous vertex $w \in U$. If either $\left|\operatorname{ch}_{\mathcal{G}}(w)\right| \leq 1$, or $\operatorname{ch}_{\mathcal{G}}(w) \subseteq \operatorname{ch}_{\mathcal{G}}(u)$ for some $u \in U$, then

$$
\mathfrak{p}(\mathcal{G}, V)=\mathfrak{p}\left(\mathcal{G}_{-w}, V\right)
$$

Proof. Since $w$ has no parents, there are no directed paths containing it as an intermediate vertex; hence we need only show that if some vertices in $V$ share a hidden common cause in $\mathcal{G}$ with respect to $U$, then they also share one in $\mathcal{G}_{-w}$ with respect to $U \backslash\{w\}$.

Since $w$ is exogenous this is clearly true whenever the hidden common cause is not $\{w\}$, and so if $w$ has no children the result is trivial. If $\left|\operatorname{ch}_{\mathcal{G}}(w)\right|=\{k\}$ then $\{k\}$ will also serve as a hidden common cause.

If $\operatorname{ch}_{\mathcal{G}}(w) \subseteq \operatorname{ch}_{\mathcal{G}}(u)$ for some $u \in U$ then clearly any vertices which share $\{w\}$ as a hidden common cause in $\mathcal{G}$ will also have $\{u\}$ as a hidden common cause in $\mathcal{G}$ and $\mathcal{G}_{-w}$.

Theorem 4.13. Let $\mathcal{D}, \mathcal{D}^{\prime}$ be two DAGs whose latent projections onto some set $V$ are the same. Then $\mathcal{M}(\mathcal{D}, V)=\mathcal{M}\left(\mathcal{D}^{\prime}, V\right)$.

Proof. Let $\mathcal{G}=\mathfrak{p}(\mathcal{D}, V)$ be the latent projection. We will show that $\mathcal{M}(\mathcal{D}, V)=$ $\mathcal{M}(\overline{\mathcal{G}}, V)$, and thereby prove the result. Let the vertex set of $\mathcal{D}$ be $V \dot{U} U$.

If no vertex in $U$ has any parents in $\mathcal{D}$, each vertex in $U$ has at least two children, and their child sets are never nested, then $\mathcal{D}=\overline{\mathcal{G}}$ and there is nothing to prove. Otherwise suppose $u \in U$ has at least one parent. Then $\mathfrak{r}(\mathcal{D}, u)$ has the same latent projection onto $V$ as $\mathcal{D}$ by Lemma 4.11, and $\mathcal{M}(\mathfrak{r}(\mathcal{D}, u), V)=\mathcal{M}(\mathcal{D}, V)$ by Lemma 3.7. The problem reduces to $\mathfrak{r}(\mathcal{D}, u)$,

and by repeated application it reduces to DAGs in which no vertex in $U$ has any parents.

Similarly, if either $w \in U$ has only one child, or $\operatorname{ch}_{\mathcal{G}}(w) \subseteq \operatorname{ch}_{\mathcal{G}}(u)$ for some other $u \in U$, then by Lemmas 3.8 and 3.9 we have $\mathcal{M}\left(\mathcal{D}_{-w}, V\right)=\mathcal{M}(\mathcal{D}, V)$ and by Lemma $4.12 \mathfrak{p}\left(\mathcal{D}_{-w}, V\right)=\mathcal{G}$, so the problem reduces to $\mathcal{D}_{-w}$. It follows that we can reduce to the canonical DAG $\overline{\mathcal{G}}$, and the result is proved.

This result shows that mDAGs are rich enough to fully express the class of marginal DAG models. In Section 6 we will see that ordinary (i.e. not hyper) graphs are unable to do this, and in Section 7 that mDAGs are, from a causal perspective, the natural object to represent these models.

# 5 Markov Properties 

We are now in a position to define a Markov property for mDAGs that relates to the original problem of characterizing the margins of DAG models.

Definition 5.1. Say that $P$ obeys the marginal Markov property for an mDAG $\mathcal{G}$ with vertices $V$, if it is contained within the marginal DAG model of the canonical DAG: $P \in \mathcal{M}(\overline{\mathcal{G}}, V)$. We denote the set of such distributions (the marginal model) by $\mathcal{M}_{m}(\mathcal{G})$.

For instance, we know from Example 3.4 that the marginal model for $1 \leftrightarrow$ $3 \leftrightarrow 2$ is the collection of distributions under which $X_{1} \pm X_{2}$.

It follows from Theorem 4.13 that the marginal model of any DAG $\mathcal{M}(\mathcal{G}, V)$ is the same as the model obtained by applying the marginal Markov property to its latent projection $\mathfrak{p}(\mathcal{G}, V)$. For some $W \subseteq V$ we denote the marginal model of an mDAG with respect to $W$ as $\mathcal{M}_{m}(\mathcal{G}, W) \equiv \mathcal{M}(\overline{\mathcal{G}}, W)$. Note that Theorem 4.10 shows that this is a sensible definition.

Proposition 5.2. Let $\mathcal{G}, \mathcal{H}$ be mDAGs with vertex set $V$.
(a) If $A$ is an ancestral set in $\mathcal{G}$, then $\mathcal{M}_{m}\left(\mathcal{G}_{A}\right)=\mathcal{M}_{m}(\mathcal{G}, A)$.
(b) If $\mathcal{H} \subseteq \mathcal{G}$, then $\mathcal{M}_{m}(\mathcal{H}) \subseteq \mathcal{M}_{m}(\mathcal{G})$.

Proof. (a) By definition $\mathcal{M}_{m}(\mathcal{G}, A)=\mathcal{M}(\overline{\mathcal{G}}, A)=\mathcal{M}_{m}(\mathfrak{p}(\overline{\mathcal{G}}, A))$, and from Proposition $4.9 \mathfrak{p}(\overline{\mathcal{G}}, A)=\mathcal{G}_{A}$.
(b) If $\mathcal{H} \subseteq \mathcal{G}$ then $\overline{\mathcal{H}} \subseteq \overline{\mathcal{G}}$, so by Proposition $3.3 \mathcal{M}(\overline{\mathcal{H}}) \subseteq \mathcal{M}(\overline{\mathcal{G}})$. It follows that $\mathcal{M}(\overline{\mathcal{H}}, V) \subseteq \mathcal{M}(\overline{\mathcal{G}}, V)$, giving the required result.

The marginal Markov property also implies certain factorizations of the joint density, if one exists. To describe them, we first need to define a special subgraph.

Definition 5.3. Let $\mathcal{G}(V, \mathcal{E}, \mathcal{B})$ be an mDAG with vertices $V$. Say that $C \subseteq V$ is bidirected-connected if for every $v, w \in C$ there is a sequence of vertices $v=v_{0}, v_{1}, \ldots, v_{k}=w$ all in $C$ such that $\left\{v_{i-1}, v_{i}\right\} \in \mathcal{B}$ for $i=1, \ldots, k$. A maximal bidirected-connected set is called a district.

Let $\mathcal{G}$ be an mDAG with district $D$. The graph $\mathcal{G}[D]$ is the mDAG with vertices $D \cup \mathrm{pa}_{\mathcal{G}}(D)$, directed edges $D \cup \mathrm{pa}_{\mathcal{G}}(D)$ to $D$, and bidirected edges $\mathcal{B}_{D}=\{B \subseteq D: B \in \mathcal{B}\}$.

In other words, $\mathcal{G}[D]$ is the induced sub-graph over $D$, together with any directed edges that point into $D$ (and the associated vertices). As an example, for the mDAG in Figure 8(a) has districts $\{1\},\{3\}$ and $\{2,4\}$. The subgraph corresponding to $D=\{2,4\}$ is shown in Figure 8(b).

Proposition 5.4. Let $\mathcal{G}$ be an $m D A G$ with districts $D_{1}, \ldots, D_{k}$, and suppose that $P$ with density $p$ obeys the marginal Markov property for $\mathcal{G}$. Then

$$
p\left(x_{V}\right)=\prod_{i=1}^{k} q_{i}\left(x_{D_{i}} \mid x_{\mathrm{pa}\left(D_{i}\right) \backslash D_{i}}\right)
$$

for some conditional distributions $q_{i}$ that obey the marginal Markov property with respect to $\mathcal{G}\left[D_{i}\right], i=1, \ldots, k$.

The proof of this is omitted but see Shpitser et al. (2014), which includes various examples. $q_{i}$ is a conditional distribution, but can be renormalized as a joint density over $D_{i} \cup \mathrm{pa}_{\mathcal{G}}\left(D_{i}\right)$. The notion of conditional distributions in graphical models is dealt with in Shpitser et al. (2014) by having two types of vertex, separately representing the random and conditioned variables; we have omitted these details for the sake of brevity.

# 5.1 Weaker Markov Properties 

The marginal model precisely answers our original question: what collections of distributions can be induced as the margin of a DAG model? However, because the definition is rather indirect, it is generally difficult to characterize the set $\mathcal{M}_{m}(\mathcal{G})$, and we may be unable to tell whether or not a particular distribution lies in it or not. This complexity is one of the motivations behind the ordinary and nested Markov properties of Richardson (2003) and Shpitser et al. (2014) respectively. Both properties follow from treating the ancestrality in Proposition 5.2(b) and the factorization in Proposition 5.4 as axiomatic. In order to do so, we assume the existence of a joint density with respect to a product measure on $\mathcal{X}_{V}$.

Definition 5.5. Let $\mathcal{G}$ be an mDAG with vertices $V$, and $P$ a probability distribution over $\mathcal{X}_{V}$ with density $p$. Say that $P$ obeys the nested Markov property with respect to $P$ if either $|V|=1$, or both:

1. for every ancestral set $A \subseteq V$, the margin of $P$ over $X_{A}$ obeys the nested Markov property for $\mathcal{G}_{A}$; and
2. if $\mathcal{G}$ has districts $D_{1}, \ldots, D_{k}$ then $p\left(x_{V}\right)=\prod_{i=1}^{k} q_{i}\left(x_{D_{i}} \mid x_{\mathrm{pa}\left(D_{i}\right) \backslash D_{i}}\right)$, where each $q_{i}$ obeys the nested Markov property for $\mathcal{G}\left[D_{i}\right]$.

![img-7.jpeg](img-7.jpeg)

Figure 8: (a) An mDAG $\mathcal{G}$ representing the DAG in Figure 3, with the vertex 5 treated as unobserved. (b) The subgraph $\mathcal{G}[\{2,4\}]$.

We denote the resulting models by $\mathcal{M}_{n}(\mathcal{G})$. The nested model 'throws away' the inequality constraints of the marginal model, but for discrete variables is known to give models of the same dimension (Evans, 2015), and it has the advantage of a fairly explicit characterization. Various equivalent formulations to the one above are given in Shpitser et al. (2014).

The ordinary model can be defined in the same way as the nested model, but replacing 2 with the weaker condition:
2'. if $\mathcal{G}$ has districts $D_{1}, \ldots, D_{k}$ then $p\left(x_{V}\right)=\prod_{i=1}^{k} q_{i}\left(x_{D_{i}} \mid x_{\mathrm{pa}\left(D_{i}\right) \backslash D_{i}}\right)$ for some conditional densities $q_{i}$.

Crucially, no further structure is imposed upon the pieces $q_{i}$, so the definition does not recurse. From their definitions and Proposition 5.4 it is clear that the models obey the inclusion $\mathcal{M}_{m}(\mathcal{G}) \subseteq \mathcal{M}_{n}(\mathcal{G}) \subseteq \mathcal{M}_{o}(\mathcal{G})$ : the next example show that these inclusions are strict in general.

Example 5.6. Consider again the graph in Figure 3; its latent projection over the vertices $\{1,2,3,4\}$ is shown in Figure 8(a): call this projection $\mathcal{G}$. Applying the ancestrality property we see that, under the ordinary Markov property the margin over $\left(X_{1}, X_{2}, X_{3}\right)$ satisfies the global Markov property for the DAG $1 \rightarrow 2 \rightarrow 3$, so $X_{1} \perp X_{3} \mid X_{2}$.

If we factorize into districts we find

$$
p\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=q_{1}\left(x_{1}\right) \cdot q_{3}\left(x_{3} \mid x_{1}, x_{2}\right) \cdot q_{24}\left(x_{2}, x_{4} \mid x_{1}, x_{3}\right)
$$

which is a vacuous requirement under the ordinary Markov property, and indeed there are no further constraints. However, the nested property additionally requires that $q_{24}$ obeys the nested property for the mDAG in Figure 8(b). Under this graph we see that $X_{4} \perp X_{1} \mid X_{3}$, and this gives the constraint (1); hence $\mathcal{M}_{n}(\mathcal{G}) \subset \mathcal{M}_{o}(\mathcal{G})$.

If $X_{2}$ and $X_{4}$ are discrete, then the marginal Markov property induces an extra inequality constraint known as Bell's inequality (Bell, 1964; Gill, 2014); hence $\mathcal{M}_{m}(\mathcal{G}) \subset \mathcal{M}_{n}(\mathcal{G})$.

# 6 Markov Equivalent Graphs 

A natural question to ask when two different graphs lead to the same model under a particular Markov property. That is, what is the equivalence class determined by $\mathcal{G} \sim \mathcal{G}^{\prime}$ whenever $\mathcal{M}_{m}(\mathcal{G})=\mathcal{M}_{m}\left(\mathcal{G}^{\prime}\right)$ ? Without further assumptions such as a causal ordering, graphs that are Markov equivalent are indistinguishable; any model search procedure over the class of mDAG models should therefore report the equivalence class rather than a single graph. In addition, because the marginal Markov property is difficult to characterize explicitly, it can be helpful to reduce a problem down to a simpler graph (see Example 6.4).

For the ordinary Markov property there is a relatively simple criterion for determining whether two graphs are equivalent (Richardson, 2003); for the nested Markov model, on the other hand, equivalence is an open problem. This section provides partial results towards a characterization in the case of the marginal model. We conjecture that if two graphs are equivalent under the marginal property then they are also equivalent under the nested property. The results of Evans (2015) show that this holds for discrete variables, but the general case is still open.

Our first substantive equivalence result generalizes an idea for instrumental variables.

Proposition 6.1. Let $\mathcal{G}$ be an $m D A G$ containing a bidirected facet $B=C \dot{\cup} D$ such that:
(i) every bidirected face containing any $c \in C$ is a subset of $B$; and
(ii) $\mathrm{pa}_{\mathcal{G}}(d) \supseteq \mathrm{pa}_{\mathcal{G}}(C)$ for each $d \in D$.

Let $\mathcal{H}$ be the $m D A G$ defined from $\mathcal{G}$ by removing the facet $B$ and replacing it with $C$ and $D$, and adding edges $c \rightarrow d$ for each $c \in C$ and $d \in D$ (where such an edge is not already present).

Then $\mathcal{M}_{m}(\mathcal{G})=\mathcal{M}_{m}(\mathcal{H})$.
Proof. The result follows from Lemma A. 4 in the appendix, which shows that under these circumstances we can split the latent variable corresponding to $B$ into two independent pieces.

Example 6.2. Consider the mDAG in Figure 9(a). We can apply the Proposition with $C=\{a, b\}$ and $D=\{c, d\}$ to see that it is Markov equivalent to the graph in Figure 9(b). The advantage of such a reduction is that it moves the graph 'closer' to something which looks like a DAG, having smaller bidirected facets. This makes it clearer how the joint distribution factorizes.

Example 6.3. The canonical example to which Proposition 6.1 can be applied is the instrumental variables model, shown in Figure 10(a). As noted by Didelez and Sheehan (2007), it is not possible observationally to tell whether 1 is a direct cause of 2 , or there is a hidden common cause, or both. Applying

![img-8.jpeg](img-8.jpeg)

Figure 9: Two mDAGs shown to be Markov equivalent by application of Proposition 6.1
![img-9.jpeg](img-9.jpeg)

Figure 10: Three Markov equivalent graphs representing the instrumental variables model.

![img-10.jpeg](img-10.jpeg)

Figure 11: (a) An mDAG; (b) an mDAG which is Markov equivalent to the one in (a); and (c) a DAG which is Markov equivalent to the mDAGs.

Proposition 6.1 to the graphs in Figure 10(b) and (c) with $C=\{1\}$ and $D=\{2\}$ shows that they are indeed equivalent to Figure 10(a).

Example 6.4. The mDAG in Figure 11(a) can be reduced to the simpler one in 11(b) by applying Proposition 6.1 with $C=\{1\}$ and $D=\{2,3\}$. This can be further simplified to the DAG in (c) by applying the proposition again, this time with $C=\{2\}$ and $D=\{3\}$. By using the global Markov property for DAGs, this shows that each graph represents those distributions under which $X_{4} \Perp X_{1}, X_{2} \mid X_{3}$.

Define the skeleton of an $\operatorname{mDAG} \mathcal{G}(V, \mathcal{E}, \mathcal{B})$ as the simple undirected graph with vertices $V$, and edges $v-w$ whenever $v$ and $w$ appear together in some edge (directed or bidirected) in $\mathcal{G}$.

Proposition 6.5. Let $\mathcal{G}$ and $\mathcal{H}$ be mDAGs with different skeletons. Then if the state-space $\mathcal{X}_{V}$ is discrete $\mathcal{M}_{m}(\mathcal{G}) \neq \mathcal{M}_{m}(\mathcal{H})$.

Proof. This follows from Evans (2012), Corollary 4.4.
Note that this is not necessarily true for all state-spaces: if $X_{2}$ is continuous the three models defined by applying the marginal Markov property to the graphs in Figure 10 are all saturated (i.e. contain any joint distribution over those variables), even though they have skeleton $1-2-3$ (Bonet, 2001).

# 6.1 Bidirected Graphs and Connection to ADMGs 

The notion of latent projection was defined by Verma (1991) with respect to acyclic directed mixed graphs (though this term for such graphs was not introduced until Richardson (2003)). The importance of our more general formulation is now made clear.

Example 6.6. Consider the mDAGs in Figure 12. The graph in Figure 12(a) is the latent projection one would obtain from a single latent variable having all three observed nodes as children, while Figure 12(b) corresponds to having three independent latents, each with a pair of observed variables as children. The first graph is associated with a model which is clearly saturated, but

![img-11.jpeg](img-11.jpeg)

Figure 12: (a) An mDAG corresponding to a saturated model; (b) an mDAG corresponding to a model with constraints.
the second is not: for example, if the observed variables are binary, it is not possible to have $P\left(X_{1}=X_{2}=X_{3}=1\right)=P\left(X_{1}=X_{2}=X_{3}=0\right)=\frac{1}{2}$ (Fritz, 2012).

Under Verma's original formulation of latent projection with ADMGs, both these models are represented by the same graph: the one in Figure 12(b). However, as the previous example shows, the two marginal models formed in this way are actually distinct. The next result generalizes this idea.

Lemma 6.7. Let $\mathcal{G}$ be a purely bidirected $m D A G$ with vertices $V$, whose bidirected faces consist of all non-empty $B \subset V$ strict subsets of vertices. Then the model $\mathcal{M}(\mathcal{G})$ is not saturated (for any state-space $\mathcal{X}_{V}$ ).

Proof. For each $v \in V$, let $B_{v}=V \backslash\{v\}$, so that $\mathcal{B}$ consists of the sets $B_{v}$ and their subsets. The canonical DAG for $\mathcal{G}$ has vertices $V \cup\left\{B_{v}: v \in V\right\}$ and edges $B_{v} \rightarrow w$ whenever $v \neq w$.

Let $\left(X_{V}, Y_{\mathcal{B}}\right)$ have a joint distribution which respects the SEP with respect to $\mathcal{G}$, so that, writing $\boldsymbol{Y}_{-v} \equiv\left(Y_{B_{w}}: w \neq v\right)$, we have $X_{v}=f_{v}\left(\boldsymbol{Y}_{-v}, E_{v}\right)$.

Given some permutation $s$ of $V$ such that $s(v) \neq v$ for any $v \in V$, let $\mathcal{F}_{v}=\sigma\left(Y_{B_{v}}, E_{s(v)}\right)$. Note that each $X_{v}$ is $\sigma\left(\bigvee_{w \neq v} \mathcal{F}_{w}\right)$-measurable, and that all the $\sigma$-algebrae $\mathcal{F}_{v}$ are independent.

It follows from Lemma A. 2 in the appendix that if $\mathbb{E}\left(X_{v}-X_{w}\right)^{2} \leq \epsilon$ for each $v, w$, then each $X_{v}$ has variance at most $|V| \epsilon$. But this precludes, for example, the possibility of a joint binary distribution in which $P(\left\{X_{v}\right.$ all equal $\})=1-\epsilon$ with $P\left(X_{v}=0\right)=P\left(X_{v}=1\right)=\frac{1}{2}$ for some sufficiently small positive $\epsilon$. Since it is always possible to dichotomize a (non-trivial) random variable, this shows that the model is not saturated on any state-space.

In the case where mDAGs contain only bidirected edges, Markov equivalence turns out to be very simple.

Proposition 6.8. Let $\mathcal{G}, \mathcal{G}^{\prime}$ be mDAGs containing no directed edges. Then $\mathcal{M}_{m}(\mathcal{G})=\mathcal{M}_{m}\left(\mathcal{G}^{\prime}\right)$ if and only if $\mathcal{G}=\mathcal{G}^{\prime}$.

![img-12.jpeg](img-12.jpeg)

Figure 13: mDAGs representing the eight distinct models over three (unlabelled) variables.

Proof. Suppose that $\mathcal{G}$ and $\mathcal{G}^{\prime}$ are not equal, so (without loss of generality) there exists some $B \in \mathcal{B}(\mathcal{G}) \backslash \mathcal{B}\left(\mathcal{G}^{\prime}\right)$. Since $B$ is ancestral (there are no directed edges), it is sufficient to prove that $\mathcal{M}_{m}\left(\mathcal{G}_{B}\right) \neq \mathcal{M}_{m}\left(\mathcal{G}_{B}^{\prime}\right)$, so assume that in fact the vertices of $\mathcal{G}$ and $\mathcal{G}^{\prime}$ are $B$. The model $\mathcal{M}_{m}(\mathcal{G})$ is saturated.

Let $\tilde{\mathcal{G}}$ be the bidirected graph with vertices $B$ and such that $\mathcal{B}(\tilde{\mathcal{G}})$ consists of all strict subsets of $B$; by Lemma $6.7 \mathcal{M}_{m}(\tilde{\mathcal{G}})$ is not saturated. But $\mathcal{G}^{\prime} \subseteq \tilde{\mathcal{G}}$, so $\mathcal{M}_{m}\left(\mathcal{G}^{\prime}\right) \subseteq \mathcal{M}_{m}(\tilde{\mathcal{G}}) \subset \mathcal{M}_{m}(\mathcal{G})$, so in particular $\mathcal{M}_{m}(\mathcal{G}) \neq \mathcal{M}_{m}\left(\mathcal{G}^{\prime}\right)$

It follows from this result that ordinary graphs are fundamentally unable to fully represent marginal models, even if we add additional kinds of edge; the number of possible marginal models just grows too quickly. Consequently our extension to hyper-edges is necessary.

Corollary 6.9. No class of ordinary graphs (i.e. not hyper-graphs) is sufficient to represent marginal models of DAGs.

Proof. The number of simplicial complexes on $n$ vertices grows faster than $2^{\binom{n}{\lfloor n / 2\rfloor}}$ (see, for example, Kleitman, 1969), so by Proposition 6.8 there are at least this many marginal models. For a class of ordinary graphs with $k$ different edge types, there are only $2^{k\binom{n}{2}}$ different graphs, and $\binom{n}{\lfloor n / 2\rfloor}>k\binom{n}{2}$ for sufficiently large $n$. Hence ordinary graphs are not sufficient.

# 6.2 mDAGs on Three Variables 

There are 48 distinct mDAGs over three unlabelled vertices (i.e. up to permutation of the vertices). Using Propositions 5.2, 6.1 and 6.5 one can show that of these there are 8 equivalence classes of induced models. These are shown in Figure 13. Five of them are DAG models, the other three being the instrumental variables model from Figure 10(a), the 'unrelated confounding' model studied by Evans (2012), and the pairwise bidirected model from Example 6.6.

![img-13.jpeg](img-13.jpeg)

Figure 14: Three mDAGs whose associated models under the marginal Markov property may or may not be saturated.

For four nodes the problem becomes much more complicated. As an illustration of the limitations of the results in this section, we note that we are unable to determine whether or not the graphs in Figure 14 represent saturated models under the marginal Markov property or not.

# 7 Causal Models and Interventions 

The use of DAGs to represent causal models goes back to the work of Sewall Wright, and has found popularity more recently (see Spirtes et al., 2000; Pearl, 2009, and references therein). The use of an arrow $X \rightarrow Y$ to express the statement that ' $X$ causes $Y$ ' is natural and intuitive, and directed acyclic graphs provide a convenient recursive structure for representing causal models, with acyclicity enforcing the idea that causes should precede effects in time.

Note that the structural equation property as formulated in Definition 2.2 only posits the existence of some functions $f_{v}$ and error variables $E_{v}$ which generate the required joint distribution. In general, there will be many graphical structures and pairs $\left(f_{v}, E_{v}\right)$ which give rise to a given distribution. However, if a distribution is structurally generated in this way, then when some of the variables in the system are intervened upon (in an appropriately defined way), a suitably modified version of the original DAG will correctly represent the resulting interventional probability distribution (Pearl, 2009). Analogously we will show that mDAGs are able to represent the models induced on the margins of DAGs after intervention.

Definition 7.1. Let $\mathcal{D}$ be a DAG with vertices $V$, and suppose that data are generated according to a particular collection of pairs $\left(f_{v}, E_{v}\right), v \in V$ which satisfy the SEP for $\mathcal{D}$. An intervention on $A \subseteq V$ replaces $\left(f_{v}, E_{v}\right)$ with $\left(\tilde{f}_{v}, \tilde{E}_{v}\right)$ for each $v \in A$, where $\tilde{f}_{v}: \mathscr{E}_{v} \rightarrow \mathcal{X}_{v}$ is measurable, and all $E_{w}, \tilde{E}_{v}$ are independent.

Denote by $\mathcal{D}_{\tilde{A}}$ the $D A G \mathcal{D}$ after intervening on $A$, formed from $\mathcal{D}$ by removing edges directed towards $v \in A$.

An intervention removes the dependence of a variable on all of its parents. If $P$ is generated by $\left(f_{v}, E_{v}\right)$ according to the DAG $\mathcal{D}$, then the distribution

![img-14.jpeg](img-14.jpeg)

Figure 15: The mDAG from Figure 1 after intervening on $d$.
$P_{\bar{A}}$ after intervention on $A$ is generated according to the mutilated DAG $\mathcal{D}_{\bar{A}}$, and hence obeys the SEP for $\mathcal{M}\left(\mathcal{D}_{\bar{A}}\right)$. This definition of an intervention is based on the one in Pearl (2009).

Note that intervention is not a purely probabilistic operation, in the sense that its effect it is not identifiable from the observed probability distribution alone: it relies upon knowledge of the full structural generating system.

# 7.1 Causal mDAGs 

Let $\mathcal{D}$ be a DAG with vertex set $U \dot{\cup} V$ and let $\mathcal{G}=\mathfrak{p}(\mathcal{D}, V)$. If $\left(X_{U}, X_{V}\right)$ are generated according to the structural equation property for $\mathcal{D}$, the definitions and results of previous sections tell us that the distribution of $X_{V}$, say $P$, is contained in $\mathcal{M}_{m}(\mathcal{G})$. If an intervention is performed on some of the vertices in $V$, what then should we expect from the resulting marginal distribution?

Definition 7.2. Let $\mathcal{G}(V, \mathcal{E}, \mathcal{B})$ be an mDAG, and $A \subseteq V$. The mDAG $\mathcal{G}_{\bar{A}}$ has vertices $V$, directed edges $\mathcal{E}_{\bar{A}}=\{(w, v) \in \mathcal{E}: v \notin A\}$, and bidirected faces $\{B \backslash A: B \in \mathcal{B}\}$ (together with the singletons $\{a\}$ for $a \in A$ ).

In other words to obtain $\mathcal{G}_{\bar{A}}$ from $\mathcal{G}$, delete directed edges pointing to $A$, and remove vertices in $A$ from each bidirected edge. For example Figure 15 shows the result of intervening on $\{d\}$ in the mDAG from Figure 1. The next result shows that this definition of a mutilated mDAG is sensible, because mutilation and projection commute.

Proposition 7.3. Let $A \subseteq V$. If $\mathcal{G}=\mathfrak{p}(\mathcal{D}, V)$, then $\mathcal{G}_{\bar{A}}=\mathfrak{p}\left(\mathcal{D}_{\bar{A}}, V\right)$.
Proof. Note that the definition of latent projections and of hidden common causes refer only to directed paths with non-endpoint vertices in $U$. Since $U \cap A=\emptyset$, it follows that such a directed path in $\mathcal{D}$ is also contained in $\mathcal{D}_{\bar{A}}$ if and only if the final vertex is not in $A$. Hence, the directed edges in $\mathfrak{p}\left(\mathcal{D}_{\bar{A}}, V\right)$ are precisely those which are in $\mathcal{G}=\mathfrak{p}(\mathcal{D}, V)$ and do not point to $A$, as required.

Now, suppose $B \in \mathcal{B}\left(\mathcal{G}_{\bar{A}}\right)$ : then there is some $B^{\prime} \in \mathcal{B}(\mathcal{G})$ with $B^{\prime} \backslash A=B$. Hence $B^{\prime}$ share a hidden common cause in $\mathcal{D}$ with respect to $U$, and by the same reasoning as above, the vertices in $B^{\prime} \backslash A=B$ share a hidden common cause in $\mathcal{D}_{\bar{A}}$ with respect to $U$. Hence $B \in \mathcal{B}\left(\mathfrak{p}\left(\mathcal{D}_{\bar{A}}, V\right)\right)$

Conversely, if $B \in \mathcal{B}\left(\mathfrak{p}\left(\mathcal{D}_{\bar{A}}, V\right)\right)$, then the elements of $B$ share a hidden common cause in $\mathcal{D}_{\bar{A}}$ with respect to $U$, and hence also in the supergraph $\mathcal{D}$. So there is some $B^{\prime} \preccurlyeq B$ with $B^{\prime} \backslash A=B$ such that $B^{\prime} \in \mathcal{B}(\mathcal{G})$, and hence $B \in \mathcal{B}\left(\mathcal{G}_{\bar{A}}\right)$.

It follows from this result that mDAGs not only represent the structure of a margin of a DAG model, but they can also correctly represent the manner in which it will change under interventions on the observed variables.

Proposition 7.4. Let $\mathcal{D}, \mathcal{D}^{\prime}$ be DAGs with the same latent projection $\mathcal{G}$ over some set of variables $V$. For any subset $A \subseteq V$ of intervened nodes, $\mathcal{M}\left(\mathcal{D}_{\bar{A}}, V\right)=$ $\mathcal{M}\left(\mathcal{D}_{\bar{A}}^{\prime}, V\right)$

Proof. By Proposition 7.3, $\mathfrak{p}\left(\mathcal{D}_{\bar{A}}, V\right)=\mathfrak{p}\left(\mathcal{D}_{\bar{A}}^{\prime}, V\right)$, so that the result follows from Theorem 4.13.

Two DAGs may be observationally Markov equivalent, such as the graphs $1 \rightarrow 2$ and $1 \leftarrow 2$ (which both represent saturated models). However, for any two distinct causal DAGs, there is always some intervention under which the resulting mutilated DAGs are not Markov equivalent. For example, if we intervene on 1 in the causal model $1 \leftarrow 2$ the two variables become independent, but in $1 \rightarrow 2$ the model remains unchanged.

We might hope that something similar holds for mDAGs: given distinct mDAGs $\mathcal{G}, \mathcal{H}$, is there always some intervention such that $\mathcal{M}_{m}\left(\mathcal{G}_{\bar{A}}\right) \neq \mathcal{M}_{m}\left(\mathcal{H}_{\bar{A}}\right)$, so that one could in principle distinguish between the two causal models via a suitable experiment? In fact this turns out not to be the case: consider the mDAGs in Figures 16(a) and (b); denote then by $\mathcal{G}$ and $\mathcal{H}$ respectively. Both represent saturated models, so in particular $\mathcal{M}_{m}(\mathcal{G})=\mathcal{M}_{m}(\mathcal{H})$. In addition, after intervening on any of the vertices the resulting mutilated graphs are the same: $\mathcal{G}_{\bar{A}}=\mathcal{H}_{\bar{A}}$ for any $A \neq \emptyset$. Hence $\mathcal{M}\left(\mathcal{G}_{\bar{A}}\right)=\mathcal{M}\left(\mathcal{H}_{\bar{A}}\right)$ for any $A \subseteq\{1,2,3\}$.

The next result shows that two causal mDAGs can be distinguished by intervention if they have different underlying DAGs.

Proposition 7.5. Let $\mathcal{G}$ and $\mathcal{H}$ be mDAGs on the same vertex set $V$, and suppose that their underlying DAGs are distinct. Then for some $A \subseteq V$, $\mathcal{M}_{m}\left(\mathcal{G}_{\bar{A}}\right) \neq \mathcal{M}_{m}\left(\mathcal{H}_{\bar{A}}\right)$.

Proof. Suppose that the edge $v \rightarrow w$ appears in $\mathcal{G}$ but not $\mathcal{H}$. Then let $A=V \backslash\{w\}$ : since non-trivial bidirected faces contain at least two vertices, $\mathcal{G}_{\bar{A}}$ and $\mathcal{H}_{\bar{A}}$ are DAGs. Therefore the only edges in $\mathcal{G}_{\bar{A}}$ and $\mathcal{H}_{\bar{A}}$ are those directed into $w$. It follows that $X_{v} \Perp X_{w}$ under any distribution in $\mathcal{M}_{m}\left(\mathcal{H}_{\bar{A}}\right)$, whereas any form of dependence between $X_{v}$ and $X_{w}$ is possible in $\mathcal{M}_{m}\left(\mathcal{G}_{\bar{A}}\right)$.

Remark 7.6. The inability to distinguish between certain causal mDAGs is partly an artefact of the sort of interventions we consider. If we allow more delicate interventions which can block a specific causal mechanism between any pair of variables, this would correspond to removing individual directed edges from the graph. In this case, by blocking all the direct causal links we

![img-15.jpeg](img-15.jpeg)

Figure 16: Two mDAGs whose corresponding models are the same under any set of perfect node interventions.
would obtain a distribution which satisfies the marginal Markov property for the underlying bidirected graphs. It would then follow from Proposition 6.8 that causal models would be in one-to-one correspondence with graphs.

# 8 Discussion 

The class of mDAGs provides a natural framework to represent the margins of non-parametric Bayesian network models, and the structure of these models under interventions when interpreted causally. We have given a partial characterization of the Markov equivalence class of these models under the marginal Markov property, but a full result is still an open problem. As mentioned in Section 6, Markov equivalence for the nested Markov model is also open.

Fitting and testing models under the marginal Markov property is difficult because no explicit representation of the model is generally available, though the results in Section 6 give characterizations in special cases (see Example 6.4). The work of Bonet (2001) suggests that a general characterization may be infeasible because of the complexity of the inequality constraints. The nested model provides a useful surrogate because, at least in the discrete case, it is known to be smooth, has an explicit parameterization, and has the same dimension as the marginal model (Evans, 2015). Since $\mathcal{M}_{n}(\mathcal{G}) \supseteq \mathcal{M}_{m}(\mathcal{G})$, if the nested model is a bad fit then so is the marginal model. The converse is not true however, so we potentially lose power by ignoring inequality constraints. Evans (2012) gives a graphical method for deriving some inequality constraints, so these can in principle be tested after fitting a larger model. The approach of Richardson et al. (2011) gives a parameterization of the marginal model for the mDAG in Figure 10(a), incorporating inequality constraints; a general parameterization for such models is another open problem.

Alternatively it is possible to use a latent variable model $\mathcal{M}_{l}(\mathcal{G})$ as a second surrogate, knowing that $\mathcal{M}_{l}(\mathcal{G}) \subseteq \mathcal{M}_{m}(\mathcal{G})$. If the nested and latent variable models give similar fits (by some suitable criterion) then we effectively have a fit for the marginal model, which lies in between the two. Methods for fitting models under the marginal Markov property would enable power-

ful search procedures for distinguishing between different causal models with latent variables.

# Acknowledgements 

We thank Steffen Lauritzen for helpful discussions, and two anonymous referees for excellent suggestions, including the idea of using a simplicial complex to represent the bidirected structure.

# A Technical Proofs 

## A. 1 Proof of Theorem 4.10

Lemma A.1. Let $\mathcal{G}\left(V \dot{\cup} U_{1} \dot{U} U_{2}, \mathcal{E}_{\mathcal{G}}, \mathcal{B}_{\mathcal{G}}\right)$ be an $m D A G$, and $\mathcal{H}\left(V \dot{\cup} U_{1}, \mathcal{E}_{\mathcal{H}}, \mathcal{B}_{\mathcal{H}}\right)$ the latent projection of $\mathcal{G}$ over $V \dot{U} U_{1}$. Then
(a) for $a, b \in V$, there is a directed path from $a$ to $b$ in $\mathcal{G}$ with non-endpoint vertices in $U_{1} \dot{U} U_{2}$ if and only if there is such a path in $\mathcal{H}$ with non-endpoint vertices in $U_{1}$;
(b) there is a hidden common cause for $B \subseteq V$ in $\mathcal{G}$ with respect to $U_{1} \dot{U} U_{2}$ if and only if there is a hidden common cause for $B$ in $\mathcal{H}$ with respect to $U_{1}$.

Proof. (a): Suppose there is a directed path from $a$ to $b$ in $\mathcal{G}$ with non-endpoint vertices in $U_{1} \cup U_{2}$. If any non-endpoint vertices on the path are also in $U_{1}$, then the problem reduces to showing the existence of two shorter paths (acyclicity means we can always concatenate directed paths and still obtain a path). On the other hand if all non-endpoint vertices are in $U_{2}$ then there is an edge $a \rightarrow b$ in $\mathcal{H}$.

Conversely if there is a directed path in $\mathcal{H}$ with intermediate vertices in $U_{1}$ then each edge $c \rightarrow d$ in that path represents a directed path from $c$ to $d$ in $\mathcal{G}$ with intermediate vertices in $U_{2}$.
(b): Let $B \subseteq V$ have a hidden common cause in $\mathcal{G}$ with respect to $U_{1} \cup U_{2}$; for each $b \in B$ there is a directed path $\pi_{b}$ to $b$ with all other vertices in $U_{1} \cup U_{2}$ as described in the definition of a hidden common cause. Let $u_{b}$ be the first vertex on $\pi_{b}$ which is not in $U_{2}$ (certainly $b \notin U_{2}$, so this is well defined). Then the vertices $A=\left\{u_{b}: b \in B\right\}$ share a hidden common cause with respect to $U_{2}$, and hence $A \in \mathcal{B}_{\mathcal{H}}$.

But for each $b \in B$, there is a directed path in $\mathcal{G}$ from $u_{b}$ to $b$ with nonendpoints in $U_{1} \cup U_{2}$, and hence by (a) there is a directed path in $\mathcal{H}$ from $u_{b}$ to $b$ with non-endpoints in $U_{1}$; hence the vertices in $B$ share a hidden common cause with respect to $U_{1}$ in $\mathcal{H}$.

Conversely, suppose the elements of $B$ share a hidden common cause $A \in \mathcal{B}_{\mathcal{H}}$ with respect to $U_{1}$ in $\mathcal{H}$. By the definition of latent projection, the vertices in $A$ must share a hidden common cause $C$ with respect to $U_{2}$ in $\mathcal{G}$. It follows by concatenating the paths from $C$ to $A$, and from $A$ to $B$, that the vertices in $B$ share the hidden common cause $C$ with respect to $U_{1} \cup U_{2}$ in $\mathcal{G}$.

Proof of Theorem 4.10. It is sufficient to prove the first equality: let $\mathcal{H}=$ $\mathfrak{p}\left(\mathcal{G}, V \cup U_{1}\right)$. Let $a, b \in V$; by Lemma A.1, there is a directed path from $a$ to $b$ in $\mathcal{G}$ with all non-endpoint vertices in $U_{1} \cup U_{2}$ if and only if there is such a path in $\mathcal{H}$ with all non-endpoint vertices in $U_{1}$. Hence the directed edges in $\mathfrak{p}(\mathcal{G}, V)$ and $\mathfrak{p}(\mathcal{H}, V)$ are the same.

Also by Lemma A.1, for any set $B \subseteq V$, there is a hidden common cause in $\mathcal{G}$ for $B$ with respect to $U_{1} \cup U_{2}$, if and only if there is one in $\mathcal{H}$ for $B$ with respect to $U_{1}$. Hence the bidirected faces in $\mathfrak{p}(\mathcal{G}, V)$ and $\mathfrak{p}(\mathcal{H}, V)$ are also the same.

# A. 2 Measure Theoretic Results 

Let $X$ be a square integrable random variable, and $\mathcal{F}$ a $\sigma$-algebra. Say that $X$ is $(\epsilon, \mathcal{F})$-measurable if $\mathbb{E}(X-\mathbb{E}[X \mid \mathcal{F}])^{2} \leq \epsilon$

Let $\mathcal{F}^{-i} \equiv \mathcal{F}_{1} \vee \cdots \vee \mathcal{F}_{i-1} \vee \mathcal{F}_{i+1} \vee \cdots \vee \mathcal{F}_{k}$.
Lemma A.2. Let $X_{i}$ be $\left(\epsilon, \mathcal{F}^{-i}\right)$-measurable for $i=1, \ldots, k$, where $\mathcal{F}_{j}$ are independent $\sigma$-algebrae.

Then $\mathbb{E}\left(X_{i}-X_{j}\right)^{2} \leq \epsilon$ for all $i, j$ implies that $X_{i}$ is $\left(2 \epsilon, \mathcal{F}^{-i, j}\right)$-measurable for $i \neq j$. In addition, $\operatorname{Var} X_{i} \leq k \epsilon$.

Proof. Since $X_{i}, \mathcal{F}^{-i} \mathbb{1} \mathcal{F}_{i}$,

$$
\begin{aligned}
\mathbb{E}\left(X_{i}-\mathbb{E}\left[X_{i} \mid \mathcal{F}^{-i, j}\right]\right)^{2} & =\mathbb{E}\left(X_{i}-\mathbb{E}\left[X_{i} \mid \mathcal{F}^{-j}\right]\right)^{2} \\
& \leq \mathbb{E}\left(X_{i}-\mathbb{E}\left[X_{j} \mid \mathcal{F}^{-j}\right]\right)^{2} \\
& \leq \mathbb{E}\left(X_{i}-X_{j}\right)^{2}+\mathbb{E}\left(X_{j}-\mathbb{E}\left[X_{j} \mid \mathcal{F}^{-j}\right]\right)^{2} \\
& \leq 2 \epsilon
\end{aligned}
$$

so $X_{i}$ is $\left(2 \epsilon, \mathcal{F}^{-i, j}\right)$-measurable. Repeating this proof shows that $X_{i}$ is $(k \epsilon, \emptyset)$ measurable, which is to say that its variance is at most $k \epsilon$.

Lemma A.3. Let $X$ be a $\sigma(Y, Z)$-measurable random variable, and $(X, Y, Z)$ have joint distribution $P$. Then there exist random variables $U, W$ such that:
(i) $U \mathbb{1} W$;
(ii) $X$ is $\sigma(Y, U)$-measurable;
(iii) $Z$ is $\sigma(W, X, Y)$-measurable;
(iv) $(X, Y, Z)$ has the appropriate joint distribution $P$.

Proof. Using the fact that our probability space is Lebesgue-Rokhlin, there exists a measurable function $g$ such that if $U$ is a uniform random variable independent of $Y$ then $(X, Y) \equiv(g(Y, U), Y)$ has the correct marginal distribution (Chentsov, 1982, Theorem 2.2). Similarly, let $W$ be a uniform random variable independent of $U, Y$ (and therefore $X$ ), and let $h$ be a measurable function such that $(X, Y, Z) \equiv(X, Y, h(X, Y, W))$ has the same distribution as $(X, Y, Z)$.

By construction, (i)-(iv) are satisfied.
Lemma A.4. Let $\mathcal{G}$ be an $m D A G$ containing a bidirected facet $B=C \dot{\cup} D$ such that: for any $c \in C$, any bidirected edge containing $c$ is a subset of $B$; and $\mathrm{pa}_{\mathcal{G}}(d) \supseteq \mathrm{pa}_{\mathcal{G}}(C)$ for each $d \in D$.

Take $P \in \mathcal{M}_{m}(\mathcal{G})$. Then there exists $Q \in \mathcal{M}(\overline{\mathcal{G}})$ such that under $Q$ we have $Y_{B}=\left(Y_{C}, Y_{D}\right)$, where:
(i) $Y_{C} \mathbb{1} Y_{D}$
(ii) each $X_{c}$ is $\sigma\left(X_{\mathrm{pa}_{\mathcal{G}}(c)}, Y_{C}\right)$-measurable
(iii) each $X_{d}$ is $\sigma\left(X_{C}, X_{\mathrm{pa}_{\mathcal{G}}(C)}, X_{\mathrm{pa}_{\mathcal{G}}(d)}, Y_{\mathcal{B}(d) \backslash B}, Y_{D}\right)$-measurable;
(iv) the $V$-margin of $Q$ is $P$.

Proof. This is just an application of Lemma A. 3 with $X=X_{C}, Y=X_{\mathrm{pa}_{\mathcal{G}}(C)}$, $Z=X_{D}$, and some extra variables $X_{\mathrm{pa}_{\mathcal{G}}(d)}, Y_{\mathcal{B}(d) \backslash B}$ on which $Z$ can depend (but this extension is trivial).

In other words, the result says that we can decompose $Y_{B}$ into two independent pieces, one of which determines the value of $X_{C}$ (once its parents are known) and contains no further information, in the sense that it is irrelevant once $X_{C}$ and $X_{\mathrm{pa}(C)}$ are known.