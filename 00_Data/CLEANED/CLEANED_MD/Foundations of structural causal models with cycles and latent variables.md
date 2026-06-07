# FOUNDATIONS OF STRUCTURAL CAUSAL MODELS WITH CYCLES AND LATENT VARIABLES 

By Stephan Bongers ${ }^{1}$, Patrick Forré ${ }^{1}$, Jonas Peters ${ }^{2}$ and Joris M. Mooij ${ }^{3}$<br>${ }^{1}$ Informatics Institute, University of Amsterdam, s.r.bongers@uva.nl; p.d.forre@uva.nl<br>${ }^{2}$ Department of Mathematical Sciences, University of Copenhagen, jonas.peters@math.ku.dk<br>${ }^{3}$ Korteweg-De Vries Institute, University of Amsterdam, j.m.mooij@uva.nl

Structural causal models (SCMs), also known as (nonparametric) structural equation models (SEMs), are widely used for causal modeling purposes. In particular, acyclic SCMs, also known as recursive SEMs, form a wellstudied subclass of SCMs that generalize causal Bayesian networks to allow for latent confounders. In this paper, we investigate SCMs in a more general setting, allowing for the presence of both latent confounders and cycles. We show that in the presence of cycles, many of the convenient properties of acyclic SCMs do not hold in general: they do not always have a solution; they do not always induce unique observational, interventional and counterfactual distributions; a marginalization does not always exist, and if it exists the marginal model does not always respect the latent projection; they do not always satisfy a Markov property; and their graphs are not always consistent with their causal semantics. We prove that for SCMs in general each of these properties does hold under certain solvability conditions. Our work generalizes results for SCMs with cycles that were only known for certain special cases so far. We introduce the class of simple SCMs that extends the class of acyclic SCMs to the cyclic setting, while preserving many of the convenient properties of acyclic SCMs. With this paper we aim to provide the foundations for a general theory of statistical causal modeling with SCMs.

1. Introduction Structural causal models (SCMs), also known as (nonparametric) structural equation models (SEMs), are widely used for causal modeling purposes [5, 51, 55, 73]. They form the basis for many statistical methods that aim at inferring knowledge of the underlying causal structure from data [see, e.g., $7,37,45,48,56$ ]. In these models, the causal relationships between the variables are expressed in the form of deterministic, functional relationships, and probabilities are introduced through the assumption that certain variables are exogenous latent random variables. SCMs arose out of certain causal models that were first introduced in genetics [79], econometrics [25], electrical engineering [39, 40] and the social sciences $[12,23]$.

Acyclic SCMs, also known as recursive SEMs, form a special well-studied subclass of SCMs that generalize causal Bayesian networks [51]. They have many convenient properties [see, e.g., 15, 16, 34, 35, 50, 60, 78]: (i) they induce a unique distribution over the variables; (ii) they are closed under perfect interventions; (iii) they are closed under marginalizations; (iv) their marginalization respects the latent projection; (v) they obey (various equivalent versions of) the Markov property and (vi) their graphs express the causal relationships encoded by the SCM in an intuitive manner.

One important limitation of acyclic SCMs is that they cannot model systems that involve causal cycles. In many systems occurring in the real world, there are feedback loops between

[^0]
[^0]:    MSC2020 subject classifications: Primary 62A09, 68T30; secondary 68T37.
    Keywords and phrases: structural causal models, causal graph, cycles, interventions, counterfactuals, solvability, Markov properties, marginalization.

observed variables. For example, in economics the price of a product may be a function of the demanded or supplied quantities, and vice versa, the demanded and supplied quantities may be functions of the price. The underlying dynamic processes describing such systems have an acyclic causal structure over time. However, causal cycles may arise when one approximates such systems over time [17, 42, 43] or when one describes the equilibrium states of these systems $[3,6,27,29,33,46,57]$. In particular, in [6] it was shown that the equilibrium states of a system governed by (random) differential equations can be described by an SCM that represents their causal semantics, which gives rise to a plethora of SCMs that include cycles (we provide some examples of such feedback systems in Appendix D. 1 of the Supplementary Material). In contrast to their acyclic counterparts, SCMs with cycles have enjoyed less attention in the literature and are not as well understood. In general, none of the above properties (i)-(vi) hold in the class of SCMs. However, some progress has been made in the case of discrete [49, 52] and linear models [27, 31, 63, 70-72], and more recently, for more general cyclic models the Markov properties have been elucidated [18].

Contributions The purpose of this paper is to provide the foundations for a general theory of statistical causal modeling with SCMs. We study properties of SCMs and allow for cycles, latent variables and nonlinear functional relationships between the variables. We investigate to which extent and under which sufficient conditions each of the properties (i)-(vi) holds, in particular, in the presence of cycles. In the next paragraphs, we describe our contributions in more detail.

When there are cyclic functional relationships between variables, one encounters various technical complications, which even arise in the linear setting. The structural equations of an acyclic SCM trivially have a unique solution. This unique solvability property ensures that the SCM gives rise to a unique, well-defined probability distribution on the variables. In the case of cycles, however, this property may be violated, and consequently, the SCM may not have a solution at all, or may allow for multiple different probability distributions [26]. Even if one starts with a cyclic SCM that is uniquely solvable, performing an intervention on the SCM may lead to an intervened SCM that is not uniquely solvable. Hence, a cyclic SCM may not give rise to a unique, well-defined probability distribution corresponding to that intervention, and whether or not this happens may depend on the intervention. We provide sufficient conditions for the existence and uniqueness of these probability distributions after intervention. In general, it is not clear whether the solutions of the structural equations of an SCM are measurable if cycles are present. In addition, we provide sufficient and necessary conditions for the measurability of solution functions of cyclic SCMs.

SCMs provide a detailed modeling description of a system. Not all information may be necessary for a certain modeling task, which motivates to consider certain classes of SCMs to be equivalent. In this paper, we formally introduce several of such equivalence relations. For example, we consider two SCMs observationally equivalent if they cannot be distinguished based on observations alone. Observationally equivalent SCMs can often still be distinguished by interventions. We consider two SCMs interventionally equivalent if they cannot be distinguished based on observations and interventions. While these concepts have been around in implicit form for acyclic SCMs, we formulate them in such a way that they also apply to cyclic SCMs that have either no solution at all or have multiple different induced probability distributions on the variables. Finally, we consider two SCMs counterfactually equivalent if they cannot be distinguished based on observations and interventions and in addition encode the same counterfactual distributions, which are the distributions induced by the so-called twin SCM via the twin network method [1]. These different equivalence relations formalize the different levels of abstraction in the so-called causal hierarchy [53, 69]. In addition, we add another, strong version of equivalence, such that equivalent SCMs have

the same solutions. This notion clarifies ambiguities when a function is constant in one of its arguments, for example.

Marginalization becomes useful if not all variables are observed: given a joint probability distribution on some variables, we obtain a marginal distribution on a subset of the variables by integrating out the remaining variables. Analogously, we can marginalize an acyclic SCM by substituting the solutions of the structural equations of a subset of the endogenous variables into the structural equations of the remaining endogenous variables. For acyclic SCMs, the induced observational and interventional distributions of the marginalized SCM coincide with the marginals of the distributions induced by the original SCM [see 15, 16, 75, 78, a.o.]. In other words, for acyclic SCMs the operation of marginalization preserves the probabilistic and causal semantics (restricted to the remaining variables). We show that for cyclic SCMs a marginalization does not always exist without further assumptions. In [18] it is shown that for modular SCMs, which can be seen as an SCM together with an additional structure of a compatible system of solution functions, a marginalization can be defined that preserves the probabilistic and causal semantics. We prove that this additional structure is not necessary and use a local unique solvability condition instead. Under this condition, we show that an SCM and its marginalization are observationally, interventionally and counterfactually equivalent on the remaining endogenous variables. Analogously, we define a marginalization operation on the associated graph of an SCM, which generalizes the latent projection [15, 76, 78]. In general, the marginalization of an SCM does not respect the latent projection of its associated graph, but we show that it does so under an additional local ancestral unique solvability condition.

In graphical models, Markov properties allow one to read off conditional independencies in a distribution directly from a graph. Various equivalent formulations of Markov properties exist for acyclic SCMs [34], one prominent example being the $d$-separation criterion, also known as the directed global Markov property, which was originally derived for Bayesian networks [50]. Markov properties have been of key importance to derive various central results regarding causal reasoning and causal discovery. For cyclic SCMs, however, the usual Markov properties do not hold in general, as was already pointed out by Spirtes [71]. His solution in terms of collapsed graphs was recently generalized and reformulated for a general class of causal graphical models [18] by adapting the notion of $d$-separation into what has been termed $\sigma$-separation. This resulted in a general directed global Markov property expressed in terms of $\sigma$-separation instead of $d$-separation. Here, we formulate these general Markov properties specifically within the framework of SCMs. Again, they only hold under certain unique solvability conditions.

In addition to its interpretation in terms of conditional independencies, the graph of an acyclic SCM also has a direct causal interpretation [51]. As was already observed in [49], the causal interpretation of SCMs with cycles can be counterintuitive, as the causal semantics under interventions no longer needs to be compatible with the structure imposed by the functional relations between the variables. We resolve this issue by showing that under certain ancestral unique solvability conditions the causal interpretation of SCMs is consistent with its graph.

Cycles lead to several technical complications related to solvability issues. We introduce a special subclass of (possibly cyclic) SCMs, the class of simple SCMs, for which most of these technical complications are absent and which preserves much of the simplicity of the theory for acyclic SCMs. A simple SCM is an SCM that is uniquely solvable with respect to every subset of the variables. Because of this strong solvability assumption, simple SCMs have all the convenient properties (i)-(vi): they always have uniquely defined observational, interventional and counterfactual distributions; we can perform every perfect intervention and marginalization on them and the result is again a simple SCM; marginalization does respect

![img-0.jpeg](img-0.jpeg)

Fig 1: Overview of the objects constructed from an SCM and the mappings between them. The numbers correspond to the definition, proposition or theorem of the corresponding object, mapping or result. When an arrow is dashed, the relation only holds under nontrivial assumptions that can be found in the corresponding definition or theorem. The symbol " $\subseteq$ " stands for the subgraph of a directed mixed graph (see Definition A. 1 in the Supplementary Material) and the symbol " $\odot$ " denotes that the surrounding diagram commutes. Table 1 gives an overview of the commutativity results for each pair of mappings between the objects with the names in bold.




Table 1: Overview of the commutativity results of different pairs of mappings, defined on SCMs (left table) and on graphs (right table). All results apply under the assumptions stated in the corresponding proposition. The entries denoted by dots are omitted due to symmetry. We do not consider the commutativity of the twin operation with itself in this paper. Proposition 5.11 (in parentheses) is not a commutativity result but a weaker relation. The graphical twin operator is only defined for directed graphs.
the latent projection; they obey the general directed global Markov property, and for special cases (including the acyclic, linear and discrete case) they obey the (stronger) directed global Markov property; their graphs have a direct and intuitive causal interpretation.

The scope of this paper is limited to establishing the foundations for statistical causal modeling with cyclic SCMs (Figure 7 in Appendix A. 4 of the Supplementary Material shows an overview of how SCMs relate to other causal graphical models). For a detailed discussion of causal reasoning, causal discovery and causal prediction with cyclic SCMs we refer the reader to other literature [e.g., 14, 21, 27, 28, 58, 59, 61]. Several recent results (generalizations of the do-calculus, adjustment criteria and an identification algorithm) for modular SCMs [19, 20] directly apply to the subclass of simple SCMs, as well. Finally, many causal discovery algorithms that have been designed for the acyclic case also apply to simple SCMs with no or only minor changes [44, 47].
Overview Figure 1 gives an overview of the different objects that can be constructed from an SCM and the different mappings between them. For pairs of mappings between the objects with the names in bold, we prove commutativity results which are summarized in Table 1.
Outline This paper is structured as follows: In Section 2, we provide a formal definition of SCMs and a natural notion of equivalence between SCMs, define the (augmented) graph corresponding to an SCM, and describe perfect interventions and counterfactuals. In Section 3,

we discuss the concept of (unique) solvability, its properties and how it relates to self-cycles. In Section 4, we define and relate various equivalence relations between SCMs. In Section 5, we define a marginalization operation that is applicable to cyclic SCMs under certain conditions. We discuss several properties of this marginalization operation and discuss the relation with a marginalization operation defined on directed mixed graphs. In Section 6, we discuss Markov properties of SCMs. In Section 7, we discuss the causal interpretation of the graphs of SCMs. Section 8 introduces and discusses the class of simple SCMs.

The Supplementary Material introduces causal graphical models in Appendix A. This section also contains details on Markov properties and modular SCMs. Appendix B provides additional (unique) solvability properties, some results for linear SCMs are discussed in Appendix C, other examples in Appendix D and the proofs of all the theoretical results are in Appendix E. Appendix F contains some lemmas and measurable selection theorems that are used in several proofs.
2. Structural causal models In this section, we provide the definition and properties of structural causal models (SCMs). Our definition of SCMs slightly deviates from existing definitions [5, 51, 73], because we make the definition of the SCM independent of the random variables that solve it. This enables us to deal with the various technical complications that arise in the presence of cycles.

# 2.1. Structural causal models and their solutions 

DEFINITION 2.1 (Structural causal model). A structural causal model (SCM) is a tuple ${ }^{1}$

$$
\mathcal{M}:=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle
$$

where

1. $\mathcal{I}$ is a finite index set of endogenous variables,
2. $\mathcal{J}$ is a disjoint finite index set of exogenous variables,
3. $\mathcal{X}=\prod_{i \in \mathcal{I}} \mathcal{X}_{i}$ is the product of the domains of the endogenous variables, where each domain $\mathcal{X}_{i}$ is a standard measurable space (see Definition F.1),
4. $\mathcal{E}=\prod_{j \in \mathcal{J}} \mathcal{E}_{j}$ is the product of the domains of the exogenous variables, where each domain $\mathcal{E}_{j}$ is a standard measurable space,
5. $\boldsymbol{f}: \boldsymbol{\mathcal { X }} \times \mathcal{E} \rightarrow \mathcal{X}$ is a measurable function that specifies the causal mechanism,
6. $\mathbb{P}_{\mathcal{E}}=\prod_{j \in \mathcal{J}} \mathbb{P}_{\mathcal{E}_{j}}$ is a product measure, the exogenous distribution, where $\mathbb{P}_{\mathcal{E}_{j}}$ is a probability measure on $\mathcal{E}_{j}$ for each $j \in \mathcal{J} .^{2}$

In SCMs, the functional relationships between variables are expressed in terms of deterministic equations, where each equation expresses an endogenous variable (on the left-hand side) in terms of a causal mechanism depending on endogenous and exogenous variables (on the right-hand side). This allows us to model interventions in an unambiguous way by changing the causal mechanisms that target specific endogenous variables (see Section 2.4).

Definition 2.2 (Structural equations). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. We call the set of equations

$$
x_{i}=f_{i}(\boldsymbol{x}, \boldsymbol{e}) \quad \boldsymbol{x} \in \mathcal{X}, \boldsymbol{e} \in \mathcal{E}
$$

for $i \in \mathcal{I}$ the structural equations of the structural causal model $\mathcal{M}$.

[^0]
[^0]:    ${ }^{1}$ We often use boldface for variables that have multiple components, for example, vectors in a Cartesian product.
    ${ }^{2}$ For the case $\mathcal{J}=\emptyset$, we have that $\mathcal{E}$ is the singleton $\mathbf{1}$ and $\mathbb{P}_{\mathcal{E}}$ is the degenerate probability measure $\mathbb{P}_{\mathbf{1}}$.

Although it is common to assume the absence of cyclic functional relations (see Definition 2.9), we make no such assumption here. In particular, we allow for self-cycles, which we will discuss in more detail in Sections 2.2 and 3.3.

The solutions of an SCM in terms of random variables are defined up to almost sure equality. Random variables that are almost surely equal are generally considered to be equivalent to each other for all practical purposes.

Definition 2.3 (Solution). A pair $(\boldsymbol{X}, \boldsymbol{E})$ of random variables $\boldsymbol{X}: \Omega \rightarrow \boldsymbol{\mathcal { X }}, \boldsymbol{E}: \Omega \rightarrow$ $\mathcal{E}$, where $\Omega$ is a probability space, is a solution of the $S C M \mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ if

1. $\mathbb{P}^{\boldsymbol{E}}=\mathbb{P}_{\mathcal{E}}$, that is, the distribution of $\boldsymbol{E}$ is equal to $\mathbb{P}_{\mathcal{E}}$, ${ }^{3}$ and
2. the structural equations are satisfied, that is,

$$
\boldsymbol{X}=\boldsymbol{f}(\boldsymbol{X}, \boldsymbol{E}) \text { a.s.. }
$$

For convenience, we call a random variable $\boldsymbol{X}$ a solution of $\mathcal{M}$ if there exists a random variable $\boldsymbol{E}$ such that $(\boldsymbol{X}, \boldsymbol{E})$ forms a solution of $\mathcal{M}$.

Often, the endogenous random variables $\boldsymbol{X}$ can be observed, while the exogenous random variables $\boldsymbol{E}$ are treated as latent. Latent exogenous variables are often referred to as "disturbance terms" or "noise variables." For a solution $\boldsymbol{X}$, we call the distribution $\mathbb{P}^{\boldsymbol{X}}$ the observational distribution of $\mathcal{M}$ associated to $\boldsymbol{X}$. In general, there may be multiple different observational distributions associated to an SCM due to the existence of different solutions of the structural equations. This is a consequence of the allowance of cycles in SCMs, as the following simple example illustrates.

Example 2.4 (Cyclic SCMs). For brevity, we use throughout this paper the notation $\boldsymbol{n}:=\{1,2, \ldots, n\}$ for $n \in \mathbb{N}$. Let $\mathcal{M}=\left\langle\mathbf{2}, \mathbf{1}, \mathbb{R}^{2}, \mathbb{R}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}}\right\rangle$ be an $S C M^{4}$ with $f_{1}(\boldsymbol{x}, e)=x_{2}$ and $f_{2}(\boldsymbol{x}, e)=x_{1}$, and $\mathbb{P}_{\mathbb{R}}$ an arbitrary probability measure on $\mathbb{R}$. Then $(X, X)$ is a solution of $\mathcal{M}$ for any arbitrary random variable $X$ with values in $\mathbb{R}$. Hence, any probability distribution on $\{(x, x): x \in \mathbb{R}\}$ is an observational distribution associated to $\mathcal{M}$. Now consider instead the same SCM but with $f_{1}(\boldsymbol{x}, e)=x_{2}+1$. This SCM has no solutions at all, and hence induces no observational distribution.

Due to the fact that the structural equations only need to be satisfied almost surely, there may exist many different SCMs representing the same set of solutions (see Example D.4). It therefore seems natural not to differentiate between structural equations that have different solutions on at most a $\mathbb{P}_{\mathcal{E}}$-null set of exogenous variables. This leads to an equivalence relation between SCMs. To be able to state the equivalence relation concisely, we introduce the following notation: For subsets $\mathcal{U} \subseteq \mathcal{I}$ and $\mathcal{V} \subseteq \mathcal{J}$, we write $\mathcal{X}_{\mathcal{U}}:=\prod_{i \in \mathcal{U}} \mathcal{X}_{i}$ and $\mathcal{E}_{\mathcal{V}}:=\prod_{j \in \mathcal{V}} \mathcal{E}_{j}$. In particular, $\mathcal{X}_{\mathcal{S}}$ and $\mathcal{E}_{\mathcal{S}}$ are defined by the singleton $\mathbf{1}$. Moreover, for a subset $\mathcal{W} \subseteq \mathcal{I} \cup \mathcal{J}$, we use the convention that we write $\mathcal{X}_{\mathcal{W}}$ and $\mathcal{E}_{\mathcal{W}}$ instead of $\mathcal{X}_{\mathcal{W} \cap \mathcal{I}}$ and $\mathcal{E}_{\mathcal{W} \cap \mathcal{J}}$, respectively and we adopt a similar notation for the (random) variables in those

[^0]
[^0]:    ${ }^{3}$ This implies that the components $E_{j}$ of $\boldsymbol{E}$ are mutually independent, since $\mathbb{P}_{\mathcal{E}}=\prod_{j \in \mathcal{J}} \mathcal{E}_{j}$.
    ${ }^{4}$ We will abuse notation by using nondisjoint subsets of the natural numbers to index both endogenous and exogenous variables; these should be understood to be disjoint copies of the natural numbers: if we write $\mathcal{I}=\boldsymbol{n}$ and $\mathcal{J}=\boldsymbol{m}$, we mean instead $\mathcal{I}=\{1,2, \ldots, n\}$ and $\mathcal{J}=\left\{1^{\prime}, 2^{\prime}, \ldots, m^{\prime}\right\}$ where $k^{\prime}$ is a copy of $k$.

spaces, that is, we write $\boldsymbol{x}_{\mathcal{W}}$ and $\boldsymbol{e}_{\mathcal{W}}$ instead of $\boldsymbol{x}_{\mathcal{W} \backslash \mathcal{I}}$ and $\boldsymbol{e}_{\mathcal{W} \backslash \mathcal{J}}$, respectively. This allows us to define the following natural equivalence relation for SCMs. ${ }^{5,6}$

Definition 2.5 (Equivalence). The two SCMs $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { K }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ and $\overline{\mathcal{M}}=$ $\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \check{\boldsymbol{f}}, \mathbb{P}_{\mathcal{E}}\right\rangle$ are equivalent, denoted by $\mathcal{M} \equiv \overline{\mathcal{M}}$, if for all $i \in I$, for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$,

$$
x_{i}=f_{i}(\boldsymbol{x}, \boldsymbol{e}) \quad \Longleftrightarrow \quad x_{i}=\tilde{f}_{i}(\boldsymbol{x}, \boldsymbol{e})
$$

Thus, two equivalent SCMs can only differ in terms of their causal mechanism. Importantly, equivalent SCMs have the same solutions and, as we will see in Sections 2.4 and 2.5, they have the same causal and counterfactual semantics (see Definitions 2.12 and 2.17, respectively). This equivalence relation on the set of all SCMs gives rise to the quotient set of equivalence classes of SCMs.
2.2. The (augmented) graph We will now define two types of graphs that can be used for representing structural properties of the SCM. These graphical representations are related to Wright's path diagrams [79]. The structural properties of the functional relations between variables modeled by an SCM are specified by the causal mechanism of the SCM and can be encoded in an (augmented) graph. For the graphical notation and standard terminology on directed (mixed) graphs that is used throughout this paper, we refer the reader to Appendix A.1.

We first define the parents of an endogenous variable.
DEFINITION 2.6 (Parent). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. We call $k \in \mathcal{I} \cup \mathcal{J}$ a parent of $i \in \mathcal{I}$ if and only if there does not exist a measurable function ${ }^{7} \tilde{f}_{i}: \boldsymbol{\mathcal { X }}_{\backslash k} \times \boldsymbol{\mathcal { E }}_{\backslash k} \rightarrow \mathcal{X}_{i}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$,

$$
x_{i}=f_{i}(\boldsymbol{x}, \boldsymbol{e}) \quad \Longleftrightarrow \quad x_{i}=\tilde{f}_{i}\left(\boldsymbol{x}_{\backslash k}, \boldsymbol{e}_{\backslash k}\right)
$$

Exogenous variables have no parents by definition. These parental relations are preserved under the equivalence relation $\equiv$ on SCMs. They can be represented by a directed graph or a directed mixed graph. ${ }^{8}$

Definition 2.7 (Graph and augmented graph). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. We define:

[^0]
[^0]:    ${ }^{5}$ An attempt at coarsening this notion of equivalence by replacing the quantifier "for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ " by "for almost every $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ under the observational distribution $\mathbb{P}^{\boldsymbol{\mathcal { X }}}$ " will not lead to a well-defined equivalence relation, since in general the observational distribution $\mathbb{P}^{\boldsymbol{\mathcal { X }}}$ may be nonunique or even nonexistent. Refining it by replacing the quantifier "for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ " by "for all $\boldsymbol{e} \in \mathcal{E}$ " would make it too fine for our purposes, since we assume the exogenous distribution to be fixed and we assume as usual that random variables that are almost surely identical are indistinguishable in practice. Note that the "for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ " and "for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ " quantifiers do not commute in general (see Example D.5)
    ${ }^{6}$ We may extend this definition to allow $\overline{\mathcal{J}} \neq \mathcal{J}$ and for a larger class of SCMs such that the exogenous distribution does not factorize. Then, for any $\mathcal{M}$ that satisfies Definition 2.1, except for that it may have a nonfactorizing exogenous distribution, there exists an equivalent SCM with a factorizing exogenous distribution (and a different $\mathcal{J}$ ); the latter can be obtained by partitioning the exogenous components into independent tuples. This motivates why we can restrict ourselves in Definition 2.1 to factorizing exogenous distributions only. For some more discussion on the representation of latent confounders, see also Example D.6.
    ${ }^{7}$ For $\boldsymbol{\mathcal { X }}=\prod_{i \in \mathcal{I}} \mathcal{X}_{i}, \mathcal{I}$ some index set, $I \subseteq \mathcal{I}$ and $k \in \mathcal{I}$, we denote $\boldsymbol{\mathcal { X }}_{\backslash I}=\prod_{i \in \mathcal{I} \backslash I} \mathcal{X}_{i}$ and $\boldsymbol{\mathcal { X }}_{\backslash k}=$ $\prod_{i \in \mathcal{I} \backslash\{k\}} \mathcal{X}_{i}$, and similarly for their elements.
    ${ }^{8} \mathrm{~A}$ directed mixed graph $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ consists of a set of nodes $\mathcal{V}$, a set of directed edges $\mathcal{E}$ and a set of bidirected edges $\mathcal{B}$ (see Definition A. 1 for a more precise definition).

![img-1.jpeg](img-1.jpeg)

Fig 2: The augmented graph (left) and the graph (center) of the SCM $\mathcal{M}$ of Example 2.8 and the graph of the intervened SCM $\mathcal{M}_{\operatorname{do}(\{3\}, 1)}$ of Example 2.16 (right).

1. the augmented graph $\mathcal{G}^{a}(\mathcal{M})$ as the directed graph with nodes $\mathcal{I} \cup \mathcal{J}$ and directed edges $u \rightarrow v$ if and only if $u \in \mathcal{I} \cup \mathcal{J}$ is a parent of $v \in \mathcal{I}$;
2. the graph $\mathcal{G}(\mathcal{M})$ as the directed mixed graph with nodes $\mathcal{I}$, directed edges $u \rightarrow v$ if and only if $u \in \mathcal{I}$ is a parent of $v \in \mathcal{I}$ and bidirected edges $u \leftrightarrow v$ if and only if there exists a $j \in \mathcal{J}$ that is a parent of both $u \in \mathcal{I}$ and $v \in \mathcal{I}$.

We call the mappings $\mathcal{G}^{a}$ and $\mathcal{G}$, that map $\mathcal{M}$ to $\mathcal{G}^{a}(\mathcal{M})$ and $\mathcal{G}(\mathcal{M})$, the augmented graph mapping and the graph mapping, respectively.

In particular, the augmented graph contains no directed edges pointing toward an exogenous variable, that is, $u \in \mathcal{I} \cup \mathcal{J}$ cannot be a parent of $v \in \mathcal{J}$, because they are not functionally related through the causal mechanism. We call a directed edge $i \rightarrow i$ in $\mathcal{G}^{a}(\mathcal{M})$ and $\mathcal{G}(\mathcal{M})$ (here, $i$ is a parent of itself) a self-cycle at $i$. By definition, the mappings $\mathcal{G}^{a}$ and $\mathcal{G}$ are invariant under the equivalence relation $\equiv$ on SCMs, and hence the equivalence class of an SCM $\mathcal{M}$ is mapped to a unique augmented graph $\mathcal{G}^{a}(\mathcal{M})$ and a unique graph $\mathcal{G}(\mathcal{M})$.

Example 2.8 (Graphs of an SCM). Let $\mathcal{M}=\left\langle\mathbf{5}, \mathbf{3}, \mathbb{R}^{5}, \mathbb{R}^{3}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}^{3}}\right\rangle$ be an SCM with causal mechanism given by

$$
\begin{aligned}
& f_{1}(\boldsymbol{x}, \boldsymbol{e})=x_{1}-x_{1}^{2}+\alpha e_{1}^{2}, \quad f_{3}(\boldsymbol{x}, \boldsymbol{e})=-x_{4}+e_{2}, \quad f_{5}(\boldsymbol{x}, \boldsymbol{e})=x_{4} \cdot e_{3} \\
& f_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1}+x_{3}+x_{4}+e_{1}, \quad f_{4}(\boldsymbol{x}, \boldsymbol{e})=x_{2}+e_{2}
\end{aligned}
$$

where $\alpha \neq 0$ and $\mathbb{P}_{\mathbb{R}^{3}}$ is a product of three probability measures $\mathbb{P}_{\mathbb{R}}$ over $\mathbb{R}$ that are nondegenerate. The augmented graph $\mathcal{G}^{a}(\mathcal{M})$ and the graph $\mathcal{G}(\mathcal{M})$ of $\mathcal{M}$ are depicted ${ }^{9}$ in Figure 2 (left and center). Observe that if $\alpha$ had been equal to zero, then the endogenous variable 1 would not have any parents in $\mathcal{G}^{a}(\mathcal{M})$, that is, it would not have a self-cycle and directed edge from any exogenous variables in $\mathcal{G}^{a}(\mathcal{M})$, and it would not have a self-cycle and bidirected edge from any other variable in $\mathcal{G}(\mathcal{M})$. Moreover, if one of the probability measures $\mathbb{P}_{\mathbb{R}}$ over $\mathbb{R}$ were degenerate, then some of the directed edges from the exogenous variables to the endogenous variables in the augmented graph $\mathcal{G}^{a}(\mathcal{M})$ and bidirected edges in the graph $\mathcal{G}(\mathcal{M})$ would be missing.

As is illustrated in this example, the augmented graph provides a more detailed representation than the graph. Therefore, we use the augmented graph as the standard graphical representation for SCMs, unless stated otherwise. For an SCM $\mathcal{M}$, we denote the sets $\mathrm{pa}_{\mathcal{G}^{a}(\mathcal{M})}(\mathcal{U}), \operatorname{ch}_{\mathcal{G}^{a}(\mathcal{M})}(\mathcal{U}), \operatorname{an}_{\mathcal{G}^{a}(\mathcal{M})}(\mathcal{U})$, etc., for some subset $\mathcal{U} \subseteq \mathcal{I} \cup \mathcal{J}$, by respectively $\mathrm{pa}(\mathcal{U}), \operatorname{ch}(\mathcal{U}), \operatorname{an}(\mathcal{U})$, etc., when the notation is clear from the context.

[^0]
[^0]:    ${ }^{9}$ For visualizing an (augmented) graph, we adapt the common convention of using random variables, with the index set as a subscript, instead of using the index set itself. With a slight abuse of notation, we still use the random variables notation in the (augmented) graph in the case that the SCM has no solution at all.

Definition 2.9. We call an SCM $\mathcal{M}$ acyclic if $\mathcal{G}^{a}(\mathcal{M})$ is a directed acyclic graph (DAG). Otherwise, we call $\mathcal{M}$ cyclic.

Equivalently, an SCM $\mathcal{M}$ is acyclic if $\mathcal{G}(\mathcal{M})$ is an acyclic directed mixed graph (ADMG) [60]. Acyclic SCMs are also known as semi-Markovian SCMs [51, 76]. A commonly considered class of acyclic SCMs are the Markovian SCMs, which are acyclic SCMs for which each exogenous variable has at most one child. Several Markov properties were first shown for these models $[35,51,76]$.
2.3. Structurally minimal representations We have discussed an equivalence relation between SCMs in Section 2.1. In this subsection, we show that for each SCM there exists a representative of the equivalence class of that SCM for which each component of the causal mechanism does not depend on its nonparents [see also 55].

Definition 2.10 (Structurally minimal SCM). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { Z }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}_{i} \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an SCM. We call $\mathcal{M}$ structurally minimal if for all $i \in \mathcal{I}$ there exists a mapping $\tilde{f}_{i}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(i)} \times$ $\boldsymbol{\mathcal { E }}_{\mathrm{pa}(i)} \rightarrow \mathcal{X}_{i}$ such that $f_{i}(\boldsymbol{x}, \boldsymbol{e})=\tilde{f}_{i}\left(\boldsymbol{x}_{\mathrm{pa}(i)}, \boldsymbol{e}_{\mathrm{pa}(i)}\right)$ for all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$.

We already encountered a structurally minimal SCM $\mathcal{M}$ in Example 2.8. Taking instead $\alpha=0$ in that example gives an SCM $\mathcal{M}$ that is not structurally minimal, since the endogenous variable 1 is then not a parent of itself, while $f_{1}(\boldsymbol{x}, \boldsymbol{e})$ depends on $x_{1}$. However, the equivalent SCM where we have replaced the causal mechanism of 1 by $f_{1}(\boldsymbol{x}, \boldsymbol{e})=0$ yields a structurally minimal SCM. In general, there always exists an equivalent structurally minimal SCM.

Proposition 2.11 (Existence of a structurally minimal SCM). For an SCM $\mathcal{M}=$ $\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$, there exists an equivalent $S C M \tilde{\mathcal{M}}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ that is structurally minimal.

For a causal mechanism $\boldsymbol{f}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}$ and a subset $\mathcal{U} \subseteq \mathcal{I}$, we write $\boldsymbol{f}_{\mathcal{U}}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow$ $\boldsymbol{\mathcal { X }}_{\mathcal{U}}$ for the $\mathcal{U}$ components ${ }^{10}$ of $\boldsymbol{f}$. A structurally minimal representation is compatible with the (augmented) graph, in the sense that for every $\mathcal{U} \subseteq \mathcal{I}$ there exists a unique measurable mapping $\tilde{\boldsymbol{f}}_{\mathcal{U}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{U})} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{U})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{U}}$ such that $\boldsymbol{f}_{\mathcal{U}}(\boldsymbol{x}, \boldsymbol{e})=\tilde{\boldsymbol{f}}_{\mathcal{U}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{U})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{U})}\right)$ for all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$. Moreover, for any $\mathcal{U} \subseteq \mathcal{I}$ there exists a unique measurable mapping $\tilde{\boldsymbol{f}}_{\mathrm{an}(\mathcal{U})}$ : $\boldsymbol{\mathcal { X }}_{\mathrm{an}(\mathcal{U})} \times \boldsymbol{\mathcal { E }}_{\mathrm{an}(\mathcal{U})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathrm{an}(\mathcal{U})}$ with $\boldsymbol{f}_{\mathrm{an}(\mathcal{U})}(\boldsymbol{x}, \boldsymbol{e})=\tilde{\boldsymbol{f}}_{\mathcal{U}}\left(\boldsymbol{x}_{\mathrm{an}(\mathcal{U})}, \boldsymbol{e}_{\mathrm{an}(\mathcal{U})}\right)$ for all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$.
2.4. Interventions To define the causal semantics of SCMs, we consider here an idealized class of interventions introduced by Pearl [51] that we refer to as perfect interventions. Other types of interventions, like mechanism changes [77], fat-hand interventions [13], activity interventions [45] and stochastic versions of all these are at least as relevant, but we do not consider them here.

Definition 2.12 (Perfect intervention on an SCM). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an $S C M, I \subseteq \mathcal{I}$ a subset of endogenous variables and $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$ a value. The perfect intervention $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ maps $\mathcal{M}$ to the $S C M \mathcal{M}_{\operatorname{do}\left(I, \xi_{I}\right)}:=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$, where the intervened causal mechanism $\tilde{\boldsymbol{f}}$ is given by

$$
\tilde{f}_{i}(\boldsymbol{x}, \boldsymbol{e})= \begin{cases}\xi_{i} & i \in I \\ f_{i}(\boldsymbol{x}, \boldsymbol{e}) & i \in \mathcal{I} \backslash I\end{cases}
$$

[^0]
[^0]:    ${ }^{10}$ For $\mathcal{U}=\emptyset$, we always consider the trivial mapping $\boldsymbol{f}_{\emptyset}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}_{\emptyset}$ where $\boldsymbol{\mathcal { X }}_{\emptyset}$ is the singleton $\mathbf{1}$.

This operation $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ preserves the equivalence relation (see Definition 2.5) on the set of all SCMs, and hence this mapping induces a well-defined mapping on the set of equivalence classes of SCMs. Previous work has considered interventions only on a specific subset of endogenous variables [2, 3, 67]. Instead, we assume that we can intervene on any subset of endogenous variables in the model.

We define an analogous operation $\operatorname{do}(I)$ on directed mixed graphs.
DEFINITION 2.13 (Perfect intervention on a directed mixed graph). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $I \subseteq \mathcal{V}$ a subset. The perfect intervention $\operatorname{do}(I)$ maps $\mathcal{G}$ to the directed mixed graph $\operatorname{do}(I)(\mathcal{G}):=(\mathcal{V}, \overline{\mathcal{E}}, \overline{\mathcal{B}})$, where $\overline{\mathcal{E}}=\mathcal{E} \backslash\{v \rightarrow i: v \in \mathcal{V}, i \in I\}$ and $\overline{\mathcal{B}}=\mathcal{B} \backslash\{v \leftrightarrow i: v \in \mathcal{V}, i \in \mathcal{I}\}$.

This operation simply removes all incoming edges on the nodes in $I$. The two notions of intervention are compatible with the (augmented) graph mapping.

Proposition 2.14. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { Z }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an SCM, $I \subseteq \mathcal{I}$ a subset of endogenous variables and $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X } _ { I }}$ a value. Then $\left(\mathcal{G}^{a} \circ \operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)\right)(\mathcal{M})=\left(\operatorname{do}(I) \circ \mathcal{G}^{a}\right)(\mathcal{M})$ and $\left(\mathcal{G} \circ \operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)\right)(\mathcal{M})=(\operatorname{do}(I) \circ \mathcal{G})(\mathcal{M})$.

The two notions of perfect intervention satisfy the following elementary properties.
Proposition 2.15. For an SCM and a directed mixed graph, we have the following properties:

1. perfect interventions on disjoint subsets of variables commute;
2. acyclicity is preserved under perfect intervention.

The following example shows that an SCM with a solution may not have a solution anymore after performing a perfect intervention on the SCM, and vice versa that an SCM without a solution may yield an SCM with a solution after intervention.

EXAMPLE 2.16 (Intervened SCM and its graphs). Consider the SCM $\mathcal{M}$ of Example 2.8 which has a solution if and only if $\alpha \geq 0$. Applying the perfect intervention $\operatorname{do}(\{3\}, 1)$ to $\mathcal{M}$ gives the intervened model $\mathcal{M}_{\operatorname{do}(\{3\}, 1)}$ with the intervened causal mechanism

$$
\begin{array}{ll}
\tilde{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=x_{1}-x_{1}^{2}+\alpha e_{1}^{2}, & \tilde{f}_{3}(\boldsymbol{x}, \boldsymbol{e})=1, \quad \tilde{f}_{5}(\boldsymbol{x}, \boldsymbol{e})=x_{4} \cdot e_{3} \\
\tilde{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1}+x_{3}+x_{4}+e_{1}, & \tilde{f}_{4}(\boldsymbol{x}, \boldsymbol{e})=x_{2}+e_{2}
\end{array}
$$

for which the graph $\mathcal{G}\left(\mathcal{M}_{\operatorname{do}(\{3\}, 1)}\right)$ is depicted in Figure 2 (right). This is an example where a perfect intervention leads to an intervened SCM $\mathcal{M}_{\operatorname{do}(\{3\}, 1)}$ that does not have a solution anymore. In addition, performing a perfect intervention $\operatorname{do}(\{4\}, 1)$ on $\mathcal{M}_{\operatorname{do}(\{3\}, 1)}$ yields again an SCM with a solution for $\alpha \geq 0$.

Recall that for each solution $\boldsymbol{X}$ of an SCM $\mathcal{M}$ we call the distribution $\mathbb{P}^{\boldsymbol{X}}$ the observational distribution of $\mathcal{M}$ associated to $\boldsymbol{X}$. For cyclic SCMs, the observational distribution is in general not unique. ${ }^{11}$ For example, the SCM $\mathcal{M}$ of Example 2.8 has two different observational distributions if $\alpha>0$. Similarly, an intervened SCM may induce a distribution that is

[^0]
[^0]:    ${ }^{11}$ In order to assure the existence of a unique observational distribution it is common to consider only SCMs for which the structural equations have a unique solution (see, e.g., Definition 7.1.1 in [51]). Although these SCMs induce a unique observational distribution, they generally do not induce a unique distribution after a perfect intervention.

not unique. Whenever the intervened $\operatorname{SCM} \mathcal{M}_{\operatorname{do}\left(I, \xi_{I}\right)}$ has a solution $\boldsymbol{X}$ we therefore call the distribution $\mathbb{P}^{\boldsymbol{X}}$ the interventional distribution of $\mathcal{M}$ under the perfect intervention $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ associated to $\boldsymbol{X} .{ }^{12}$
2.5. Counterfactuals The causal semantics of an SCM are described by the interventions on the SCM. Adding another layer of complexity, one can describe the counterfactual semantics of an SCM by the interventions on the so-called twin SCM, an idea introduced in [1].

DEFINITION 2.17 (Twin SCM). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. The twin operation maps $\mathcal{M}$ to the twin structural causal model (twin SCM)

$$
\mathcal{M}^{\text {twin }}:=\left\langle\mathcal{I} \cup \mathcal{I}^{\prime}, \mathcal{J}, \mathcal{X} \times \mathcal{X}, \mathcal{E}, \check{\boldsymbol{f}}, \mathbb{P}_{\mathcal{E}}\right\rangle
$$

where $\mathcal{I}^{\prime}=\left\{i^{\prime}: i \in \mathcal{I}\right\}$ is a copy of $\mathcal{I}$ and the causal mechanism $\check{\boldsymbol{f}}: \boldsymbol{X} \times \boldsymbol{X} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{X} \times \boldsymbol{X}$ is the measurable function given by $\check{\boldsymbol{f}}\left(\boldsymbol{x}, \boldsymbol{x}^{\prime}, \boldsymbol{e}\right)=\left(\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e}), \boldsymbol{f}\left(\boldsymbol{x}^{\prime}, \boldsymbol{e}\right)\right)$.

The twin operation on SCMs preserves the equivalence relation $\equiv$ on the set of all SCMs. We define an analogous twin operation twin $(\mathcal{I})$ on directed graphs.

DEFINITION 2.18 (Twin graph). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ be a directed graph and $\mathcal{I} \subseteq \mathcal{V}$ a subset such that $\mathcal{J}:=\mathcal{V} \backslash \mathcal{I}$ is exogenous, that is, $\operatorname{pa}_{\mathcal{G}}(\mathcal{J})=\emptyset$. The twin $(\mathcal{I})$ operation maps $\mathcal{G}$ to the twin graph w.r.t. $\mathcal{I}$ defined by $\operatorname{twin}(\mathcal{I})(\mathcal{G}):=(\tilde{\mathcal{V}}, \tilde{\mathcal{E}})$, where:

1. $\tilde{\mathcal{V}}=\mathcal{V} \cup \mathcal{I}^{\prime}$, where $\mathcal{I}^{\prime}$ is a copy of $\mathcal{I}$,
2. $\tilde{\mathcal{E}}=\mathcal{E} \cup \mathcal{E}^{\prime}$, where $\mathcal{E}^{\prime}$ is given by

$$
\mathcal{E}^{\prime}=\left\{j \rightarrow i^{\prime}: j \in \mathcal{J}, i \in \mathcal{I}, j \rightarrow i \in \mathcal{E}\right\} \cup\left\{\tilde{i}^{\prime} \rightarrow i^{\prime}: \tilde{i}, i \in \mathcal{I}, \tilde{i} \rightarrow i \in \mathcal{E}\right\}
$$

with $i^{\prime}, \tilde{i}^{\prime} \in \mathcal{I}^{\prime}$ the respective copies of $i, \tilde{i} \in \mathcal{I}$.
Twin operations are compatible with the augmented graph mapping and preserve acyclicity.

Proposition 2.19. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. Then $\left(\mathcal{G}^{a} \circ\right.$ twin $)(\mathcal{M})=$ $\left(\operatorname{twin}(\mathcal{I}) \circ \mathcal{G}^{a}\right)(\mathcal{M})$.

Proposition 2.20. For SCMs and directed graphs, we have that acyclicity is preserved under the twin operation.

The perfect intervention and the twin operation for SCMs and directed graphs commute with each other in the following way.

Proposition 2.21. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM and $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ a directed graph. Then we have that perfect intervention commutes with the twin operation on both:

1. the SCM $\mathcal{M}$ : for a subset $I \subseteq \mathcal{I}$ and value $\boldsymbol{\xi}_{I} \in \boldsymbol{X}_{I},\left(\operatorname{do}\left(I \cup I^{\prime}, \boldsymbol{\xi}_{I \cup I^{\prime}}\right)\right) \circ \operatorname{twin}\right)(\mathcal{M})=$ $\left(\operatorname{twin} \circ \operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)\right)(\mathcal{M})$, and
2. the directed graph $\mathcal{G}$ : for subsets $I \subseteq \mathcal{I} \subseteq \mathcal{V}$ such that $\mathcal{J}:=\mathcal{V} \backslash \mathcal{I}$ is exogenous, $(\operatorname{do}(I \cup$ $\left.I^{\prime}\right) \circ \operatorname{twin}(\mathcal{I}))(\mathcal{G})=(\operatorname{twin}(\mathcal{I}) \circ \operatorname{do}(I))(\mathcal{G})$,
[^0]
[^0]:    ${ }^{12}$ In the literature, one often finds the notation $p(\boldsymbol{x})$ and $p\left(\boldsymbol{x} \mid \operatorname{do}\left(\boldsymbol{X}_{I}=\boldsymbol{x}_{I}\right)\right)$ for the densities of the observational and interventional distribution, respectively, in case these are uniquely defined by the SCM [e.g., 51].

where $I^{\prime}$ is the copy of $I$ in $\mathcal{I}^{\prime}$ and $\boldsymbol{\xi}_{I^{\prime}}=\boldsymbol{\xi}_{I}$.
Whenever the intervened twin $\operatorname{SCM}\left(\mathcal{M}^{\text {twin }}\right)_{\operatorname{do}\left(\tilde{I}, \boldsymbol{\xi}_{I}\right)}$, where $\tilde{I} \subseteq \mathcal{I} \cup \mathcal{I}^{\prime}$ and $\boldsymbol{\xi}_{\tilde{I}} \in \boldsymbol{\mathcal { X }}_{\tilde{I}}$, has a solution $\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)$, we call the distribution $\mathbb{P}^{\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)}$ the counterfactual distribution of $\mathcal{M}$ under the perfect intervention $\operatorname{do}\left(\tilde{I}, \boldsymbol{\xi}_{\tilde{I}}\right)$ associated to $\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)$. In Example D.3, we provide an example of how counterfactuals can be sensibly formulated for a well-known market equilibrium model described in terms of a cyclic SCM.

The interpretation of counterfactual statements has received a lot of attention in the literature $[1,8,36,51,66]$. For acyclic graphs, an alternative graphical approach to counterfactuals is the framework of Single World Intervention Graphs (SWIGs) [64]. One topic of discussion is that there exist SCMs that induce the same observational and interventional distributions, but differ in their counterfactual statements [11] (see also Example D.7). This raises the question how one can estimate such SCMs from data.
3. Solvability In this section, we introduce the notions of solvability and unique solvability with respect to a subset of the endogenous variables of an SCM. They describe the existence and uniqueness of measurable solution functions for the subsystem of structural equations that correspond with a certain subset of the endogenous variables. These notions play a central role in formulating sufficient conditions under which several properties of acyclic SCMs may be extended to the cyclic setting. For example, we show that solvability of an SCM is a sufficient and necessary condition for the existence of a solution of an SCM. Further, unique solvability of an SCM implies the uniqueness of the induced observational distribution.
3.1. Definition of solvability Intuitively, one can think of the structural equations corresponding to a subset of endogenous variables $\mathcal{O} \subseteq \mathcal{I}$ as a description of how the subsystem formed by the variables $\mathcal{O}$ interacts with the rest of the system $\mathcal{I} \backslash \mathcal{O}$ through the variables $\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}$. A solution function w.r.t. $\mathcal{O}$ assigns each input value $\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)$ of this subsystem to a specific output value $\boldsymbol{x}_{\mathcal{O}}$ of the subsystem. This is formalized as follows.

Definition 3.1 (Solvability). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. We call $\mathcal{M}$ solvable w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ if there exists a measurable mapping $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$,

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

We then call $\boldsymbol{g}_{\mathcal{O}}$ a measurable solution function w.r.t. $\mathcal{O}$ for $\mathcal{M}$. We call $\mathcal{M}$ solvable if it is solvable w.r.t. $\mathcal{I}$.

By definition, solvability w.r.t. a subset respects the equivalence relation $\equiv$ on SCMs. The measurable solution functions w.r.t. a certain subset do not always exist, and if they exist, they are not always uniquely defined. For example, for the SCM $\mathcal{M}$ in Example 2.8, the measurable solution functions w.r.t. $\{1\}$ are given by $g_{1}^{\pm}\left(e_{1}\right)= \pm \sqrt{\alpha e_{1}^{2}}$ if and only if $\alpha \geq 0$.

The following theorem states that various possible notions of "solvability" are equivalent.
THEOREM 3.2 (Sufficient and necessary conditions for solvability). For an SCM $\mathcal{M}=$ $\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\rangle$, the following are equivalent:

1. $\mathcal{M}$ has a solution (see Definition 2.3);
2. for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ the structural equations $\boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})$ have a solution $\boldsymbol{x} \in \mathcal{X}$;
3. $\mathcal{M}$ is solvable (see Definition 3.1).

![img-2.jpeg](img-2.jpeg)
![img-3.jpeg](img-3.jpeg)

Fig 3: Left: The graphs of the observationally equivalent SCMs $\mathcal{M}$ and $\tilde{\mathcal{M}}$ of Examples 3.5 and 4.2, respectively. Right: The graphs of the interventionally equivalent SCMs $\tilde{\mathcal{M}}$ and $\tilde{\mathcal{M}}$ of Example 4.4.

While in the acyclic case, the above theorem is almost trivial, in the cyclic case the measure-theoretic aspects are not that obvious. In particular, to prove the existence of a measurable solution function $\boldsymbol{g}: \mathcal{E}_{\mathrm{pa}(\mathcal{I})} \rightarrow \boldsymbol{\mathcal { X }}$ in case the structural equations have a solution for almost every $\boldsymbol{e} \in \mathcal{E}$, we make use of a strong measurable selection theorem (see Theorem F. 8 or [30]). This theorem implies that if there exists a solution $\boldsymbol{X}: \Omega \rightarrow \boldsymbol{\mathcal { X }}$, then there necessarily exists a random variable $\boldsymbol{E}: \Omega \rightarrow \mathcal{E}$ and a mapping $\boldsymbol{g}: \mathcal{E}_{\mathrm{pa}(\mathcal{I})} \rightarrow \mathcal{X}$ such that $\boldsymbol{g}\left(\boldsymbol{E}_{\mathrm{pa}(\mathcal{I})}\right)$ is a solution. However, it does not imply that there necessarily exists a random variable $\boldsymbol{E}: \Omega \rightarrow \mathcal{E}$ and a mapping $\boldsymbol{g}: \mathcal{E}_{\mathrm{pa}(\mathcal{I})} \rightarrow \mathcal{X}$ such that $\boldsymbol{X}=\boldsymbol{g}\left(\boldsymbol{E}_{\mathrm{pa}(\mathcal{I})}\right)$ holds a.s., for example, if $\boldsymbol{X}$ is a nontrivial mixture of such solutions (see Example D.8).

Solvability w.r.t. a strict subset of $\mathcal{I}$ is in general neither sufficient nor necessary for the existence of a (global) solution of the SCM. Consider, for example, the SCM $\mathcal{M}$ in Example 2.8 with $\alpha<0$. Even though this SCM is solvable w.r.t. $\{2,3,4\}$, it is not (globally) solvable, and hence does not have any solution. In Proposition B.1, we provide a sufficient condition for solvability w.r.t. a strict subset of $\mathcal{I}$ that is similar to condition (2) in Theorem 3.2 in the sense that it is formulated in terms of the solutions of (a subset of) the structural equations without requiring measurability of the solutions. For the class of linear SCMs, we provide in Proposition C. 2 a sufficient and necessary condition for solvability w.r.t. a subset of $\mathcal{I}$.
3.2. Unique solvability The notion of unique solvability w.r.t. a subset $\mathcal{O} \subseteq \mathcal{I}$ is similar to the notion of solvability, but with the additional requirement that the measurable solution function $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X } }_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \mathcal{E}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X } _ { \mathcal { O } }}$ is unique up to a $\mathbb{P}_{\mathcal{E}}$-null set.

DEFINITION 3.3 (Unique solvability). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM. We call $\mathcal{M}$ uniquely solvable w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ if there exists a measurable mapping $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X } }_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times$ $\mathcal{E}_{\mathrm{pa}(\mathcal{O})} \rightarrow \mathcal{X}_{\mathcal{O}}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$,

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

We call $\mathcal{M}$ uniquely solvable if it is uniquely solvable w.r.t. $\mathcal{I}$.
If $\mathcal{M} \equiv \tilde{\mathcal{M}}$ and $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{O}$, then $\tilde{\mathcal{M}}$ is uniquely solvable w.r.t. $\mathcal{O}$, too, and the same mapping $\boldsymbol{g}_{\mathcal{O}}$ is a measurable solution function w.r.t. $\mathcal{O}$ for both $\mathcal{M}$ and $\tilde{\mathcal{M}}$.

The following result explains why the notions of (unique) solvability do not play an important role in the theory of acyclic SCMs.

Proposition 3.4. An acyclic SCM $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ is uniquely solvable w.r.t. every subset $\mathcal{O} \subseteq \mathcal{I}$.

We now illustrate that also cyclic SCMs can be uniquely solvable w.r.t. every subset.
Example 3.5 (Cyclic SCM, uniquely solvable w.r.t. each subset). Consider the SCM $\mathcal{M}=\left\langle\mathbf{4}, \mathbf{4}, \mathbb{R}^{4}, \mathbb{R}^{4}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}^{4}}\right\rangle$ with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad f_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{2}, \quad f_{3}(\boldsymbol{x}, \boldsymbol{e})=x_{1} x_{4}+e_{3}, \quad f_{4}(\boldsymbol{x}, \boldsymbol{e})=x_{2} x_{3}+e_{4}
$$

and $\mathbb{P}_{\mathbb{R}^{4}}$ the standard-normal distribution on $\mathbb{R}^{4}$. This SCM $\mathcal{M}$ is uniquely solvable w.r.t. every subset and its (augmented) graph includes a cycle (see Figure 3).

Theorem 3.2 provides sufficient and necessary conditions for (global) solvability. The next theorem states that under the additional uniqueness requirement there exists a sufficient and necessary condition for unique solvability w.r.t. any subset (for solvability w.r.t. a subset we only have the sufficient condition provided in Proposition B.1), and moreover, that all solutions of a uniquely solvable SCM induce the same observational distribution.

THEOREM 3.6 (Sufficient and necessary conditions for unique solvability). Let $\mathcal{M}=$ $\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { Z }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$ be an SCM and $\mathcal{O} \subseteq \mathcal{I}$ a subset. The following are equivalent:

1. for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x}_{\backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\backslash \mathcal{O}}$ the structural equations

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

have a unique solution $\boldsymbol{x}_{\mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathcal{O}}$;
2. $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{O}$.

Furthermore, if $\mathcal{M}$ is uniquely solvable, then there exists a solution, and all solutions have the same observational distribution.

It is well known that under acyclicity the observational distribution is unique. Theorem 3.6 generalizes this result to settings with cycles. For linear SCMs, the unique solvability condition w.r.t. a subset is equivalent to a matrix invertibility condition (see Proposition C.3).

In general, (unique) solvability w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ does not imply (unique) solvability w.r.t. a strict superset $\mathcal{O} \subsetneq \mathcal{V} \subseteq \mathcal{I}$ nor w.r.t. a strict subset $\mathcal{W} \subsetneq \mathcal{O}$ (see Example B.2). Moreover, (unique) solvability is in general not preserved under unions and intersections (see Appendix B.3).
3.3. Self-cycles One can think of a structural equation of a single endogenous variable $i \in \mathcal{I}$ as describing a small subsystem that interacts with the rest of the system. If the output $x_{i}$ of this subsystem is uniquely determined by the input $\left(\boldsymbol{x}_{\backslash i}, \boldsymbol{e}\right)$ from the rest of the system (up to a $\mathbb{P}_{\mathcal{E}}$-null set), then $i$ is not a parent of itself (see Definition 2.6).

Proposition 3.7 (Self-cycles). The SCM $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ is uniquely solvable w.r.t. $\{i\}$ for $i \in \mathcal{I}$ if and only if $\left.\mathcal{G}^{a}(\mathcal{M}) \text { (or } \mathcal{G}(\mathcal{M})\right)$ has no self-cycle $i \rightarrow i$ at $i \in \mathcal{I}$.

A self-cycle at an endogenous variable denotes that that variable is not uniquely determined by its parents, up to a $\mathbb{P}_{\mathcal{E}}$-null set. This implies that an SCM with a self-cycle at an endogenous variable in its graph can be either solvable, or not solvable, w.r.t. that variable. For the SCM $\mathcal{M}$ of Example 2.8, we have indeed that it is solvable w.r.t. $\{1\}$ for $\alpha>0$, while for $\alpha<0$ it is not. For linear SCMs with structural equations $X_{i}=\sum_{j \in \mathcal{I}} B_{i j} X_{j}+\sum_{k \in \mathcal{J}} \Gamma_{i k} E_{k}$, the endogenous variable $i \in \mathcal{I}$ has a self-cycle if and only if $B_{i i}=1$ (see also Appendix C).
3.4. Interventions The property of (unique) solvability is in general not preserved under perfect intervention. For example, a (uniquely) solvable SCM can lead to a nonuniquely solvable SCM after intervention, which either has no solution or has solutions with multiple induced distributions (see, e.g., Examples 2.16 and D.9). A sufficient condition for the intervened SCM to be (uniquely) solvable is that the original SCM has to be (uniquely) solvable w.r.t. the subset of nonintervened endogenous variables.

Proposition 3.8. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM that is (uniquely) solvable w.r.t. $\mathcal{O} \subseteq \mathcal{I}$. Then, for any set $I$ such that $\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O} \subseteq I \subseteq \mathcal{I} \backslash \mathcal{O}$ and value $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$ the intervened $S C M \mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ is (uniquely) solvable w.r.t. $\mathcal{O} \cup I$.

![img-4.jpeg](img-4.jpeg)

Fig 4: The graphs of the SCM $\mathcal{M}$ (left) of Example 3.11 and the marginal $\operatorname{SCM} \mathcal{M}_{\operatorname{marg}(\{2,3\})}$ (right) of Example 5.10.
Proposition 3.4 shows that acyclic SCMs are uniquely solvable w.r.t. every subset and hence are uniquely solvable after every perfect intervention. This also directly follows from the fact that acyclicity is preserved under perfect intervention (see Proposition 2.15). Moreover, since acyclicity is preserved under the twin operation (see Proposition 2.20), an acyclic SCM induces unique observational, interventional and counterfactual distributions.
3.5. Ancestral (unique) solvability We saw that, in general, solvability w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ does not imply solvability w.r.t. a strict subset of $\mathcal{O}$. Here we show that it does imply solvability w.r.t. the ancestral subsets in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$, that is, in the induced subgraph of the graph $\mathcal{G}(\mathcal{M})$ on $\mathcal{O}$. A subset $\mathcal{A} \subseteq \mathcal{O}$ is called an ancestral subset in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$ if $\mathcal{A}=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})$, where $\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})$ are the ancestors of $\mathcal{A}$ according to the induced subgraph ${ }^{13} \mathcal{G}(\mathcal{M})_{\mathcal{O}}$.

Definition 3.9 (Ancestral (unique) solvability). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { K }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an SCM. We call $\mathcal{M}$ ancestrally (uniquely) solvable w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ if $\mathcal{M}$ is (uniquely) solvable w.r.t. every ancestral subset in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$. We call $\mathcal{M}$ ancestrally (uniquely) solvable if it is ancestrally (uniquely) solvable w.r.t. $\mathcal{I}$.

Proposition 3.10 (Solvability is equivalent to ancestral solvability). The SCM $\mathcal{M}=$ $\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$ is solvable w.r.t. the subset $\mathcal{O} \subseteq \mathcal{I}$ if and only if $\mathcal{M}$ is ancestrally solvable w.r.t. $\mathcal{O}$.

A similar result does not hold for unique solvability. Although ancestral unique solvability w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ implies unique solvability w.r.t. $\mathcal{O}$, the converse does not hold in general, as the following example illustrates.

Example 3.11 (Unique solvability w.r.t. $\mathcal{O}$ does not imply ancestral unique solvability w.r.t. $\mathcal{O}$ ). Consider the SCM $\mathcal{M}=\left\langle\mathbf{4}, \mathbf{1}, \mathbb{R}^{4}, \mathbb{R}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}}\right\rangle$ with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, e)=e, f_{2}(\boldsymbol{x}, e)=x_{2} \cdot\left(1-\mathbf{1}_{\{0\}}\left(x_{1}-x_{3}\right)\right)+1, f_{3}(\boldsymbol{x}, e)=x_{3}, f_{4}(\boldsymbol{x}, e)=x_{3}
$$

and $\mathbb{P}_{\mathbb{R}}$ the standard-normal measure on $\mathbb{R}$. This SCM is uniquely solvable w.r.t. the set $\{2,3\}$, and thus solvable w.r.t. this set. Although it is solvable w.r.t., the ancestral subset $\{3\}$ in $\mathcal{G}(\mathcal{M})_{\{2,3\}}$, depicted in Figure 4 (left), it is not uniquely solvable w.r.t. this subset, because the structural equation $x_{3}=x_{3}$ holds for any $x_{3} \in \mathbb{R}$. Hence, it is not ancestrally uniquely solvable w.r.t. $\{2,3\}$.

However, for the class of linear SCMs we have that unique solvability w.r.t. $\mathcal{O}$ always implies ancestral unique solvability w.r.t. $\mathcal{O}$ (see Proposition C.4).

Although in general unique solvability is not preserved under unions, in Proposition B. 4 we show that if an SCM is uniquely solvable w.r.t. two ancestral subsets and w.r.t. their intersection, then it is uniquely solvable w.r.t. their union. In general, the property of ancestral unique solvability is not preserved under perfect intervention, as can be seen in Example D.9. The notion of ancestral unique solvability will appear in various results in Sections 5 and 6.

[^0]
[^0]:    ${ }^{13}$ Here, one can also use the augmented graph $\mathcal{G}^{a}(\mathcal{M})$ on $\mathcal{O}$ since $\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})=\operatorname{an}_{\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})$ for every subset $\mathcal{A} \subseteq \mathcal{O} \subseteq \mathcal{I}$.

4. Equivalences In Section 2, we already encountered an equivalence relation on the class of SCMs (see Definition 2.5). The (augmented) graph of an SCM, its solutions and its induced observational, interventional and counterfactual distributions are preserved under this equivalence relation. In this section, we give several coarser equivalence relations on the class of SCMs: observational, interventional and counterfactual equivalence.
4.1. Observational equivalence Observational equivalence is the property that two SCMs are indistinguishable on the basis of their observational distributions.

DEFINITION 4.1 (Observational equivalence). Two SCMs $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { I }}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ and $\tilde{\mathcal{M}}=\left\langle\tilde{\mathcal{I}}, \tilde{\mathcal{J}}, \tilde{\mathcal{X}}, \tilde{\mathcal{E}}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\tilde{\mathcal{E}}}\right\rangle$ are observationally equivalent w.r.t. $\mathcal{O} \subseteq \mathcal{I} \cap \tilde{\mathcal{I}}$, denoted by $\mathcal{M} \equiv_{\text {obs }(\mathcal{O})} \tilde{\mathcal{M}}$, if $\boldsymbol{\mathcal { X }}_{\mathcal{O}}=\tilde{\boldsymbol{\mathcal { X }}}_{\mathcal{O}}$ and for all solutions $\boldsymbol{X}$ of $\mathcal{M}$ there exists a solution $\tilde{\boldsymbol{X}}$ of $\tilde{\mathcal{M}}$ such that $\mathbb{P}^{\boldsymbol{X}_{\mathcal{O}}}=\mathbb{P}^{\tilde{\boldsymbol{X}}_{\mathcal{O}}}$ and for all solutions $\tilde{\boldsymbol{X}}$ of $\tilde{\mathcal{M}}$ there exists a solution $\boldsymbol{X}$ of $\mathcal{M}$ such that $\mathbb{P}^{\boldsymbol{X}_{\mathcal{O}}}=\mathbb{P}^{\tilde{\boldsymbol{X}}_{\mathcal{O}}} . \mathcal{M}$ and $\tilde{\mathcal{M}}$ are called observationally equivalent if they are observationally equivalent w.r.t. $\mathcal{I}=\tilde{\mathcal{I}}$.

Equivalent SCMs have the same solutions, and hence they are observationally equivalent w.r.t. every subset $\mathcal{O} \subseteq \mathcal{I}$. However, observational equivalence does not imply equivalence.

EXAMPLE 4.2 (Observational equivalence does not imply equivalence). Consider the SCM $\tilde{\mathcal{M}}$ that is the same as $\mathcal{M}$ of Example 3.5 but with the causal mechanism $\tilde{\boldsymbol{f}}$ given by

$$
\tilde{f}_{1}(\boldsymbol{x}, \boldsymbol{e}):=e_{1}, \quad \tilde{f}_{2}(\boldsymbol{x}, \boldsymbol{e}):=e_{2}, \quad \tilde{f}_{3}(\boldsymbol{x}, \boldsymbol{e}):=\frac{x_{1} e_{4}+e_{3}}{1-x_{1} x_{2}}, \quad \tilde{f}_{4}(\boldsymbol{x}, \boldsymbol{e}):=\frac{x_{2} e_{3}+e_{4}}{1-x_{1} x_{2}}
$$

This SCM $\tilde{\mathcal{M}}$ is observationally equivalent to the SCM $\mathcal{M}$. Because both SCMs have a different (augmented) graph they are not equivalent to each other (see Figure 3).

This example shows that if two SCMs $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are observationally equivalent, then their associated augmented graphs $\mathcal{G}^{a}(\mathcal{M})$ and $\mathcal{G}^{a}(\tilde{\mathcal{M}})$ are not necessarily equal to each other.
4.2. Interventional equivalence We consider two SCMs to be interventionally equivalent if they induce the same interventional distributions under all perfect interventions.

DEFINITION 4.3 (Interventional equivalence). Two SCMs $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ and $\tilde{\mathcal{M}}=\left\langle\tilde{\mathcal{I}}, \tilde{\mathcal{J}}, \tilde{\mathcal{X}}, \tilde{\mathcal{E}}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\tilde{\mathcal{E}}}\right\rangle$ are interventionally equivalent w.r.t. $\mathcal{O} \subseteq \mathcal{I} \cap \tilde{\mathcal{I}}$, denoted by $\mathcal{M} \equiv_{\text {int }(\mathcal{O})} \tilde{\mathcal{M}}$, if $\boldsymbol{\mathcal { X }}_{\mathcal{O}}=\tilde{\boldsymbol{\mathcal { X }}}_{\mathcal{O}}$ and for every $I \subseteq \mathcal{O}$ and every value $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$ their intervened models $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ and $\tilde{\mathcal{M}}_{\mathrm{do}\left(I, \xi_{I}\right)}$ are observationally equivalent with respect to $\mathcal{O} . \mathcal{M}$ and $\tilde{\mathcal{M}}$ are called interventionally equivalent if they are interventionally equivalent w.r.t. $\mathcal{I}=\tilde{\mathcal{I}}$.

Equivalent SCMs have the same solutions under every perfect intervention, and hence they are interventionally equivalent w.r.t. every subset $\mathcal{O} \subseteq \mathcal{I}$. SCMs that are interventionally equivalent w.r.t. a subset $\mathcal{O} \subseteq \mathcal{I}$ are interventionally equivalent w.r.t. every strict subset $\mathcal{W} \subseteq$ $\mathcal{O}$. But in general, they are not interventionally equivalent w.r.t. a strict superset $\mathcal{O} \subsetneq \mathcal{V} \subseteq \mathcal{I}$, as can be seen in Example 4.2, where the SCMs $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are interventionally equivalent w.r.t. $\{1,2\}$ but are not interventionally equivalent. Interventional equivalence w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ implies observational equivalence w.r.t. $\mathcal{O}$, since the empty perfect intervention $(I=\emptyset)$ is a special case of a perfect intervention. However, observational equivalence w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ does not imply interventional equivalence w.r.t. $\mathcal{O}$ in general, as can be seen in Example 4.2, where the SCMs $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are observationally equivalent but not interventionally equivalent.

Although interventional equivalence is a finer notion than observational equivalence, we have that if two SCMs $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are interventionally equivalent, then their associated augmented graphs $\mathcal{G}^{a}(\mathcal{M})$ and $\mathcal{G}^{a}(\tilde{\mathcal{M}})$ are not necessarily equal to each other.

Example 4.4 (Interventionally equivalent SCMs with different graphs). Consider the SCM $\overline{\mathcal{M}}=\left\langle\mathbf{2}, \mathbf{2},\{-1,1\}^{2},\{-1,1\}^{2}, \check{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ and the SCM $\overline{\mathcal{M}}$ that is the same as $\overline{\mathcal{M}}$ except for its causal mechanism $\check{f}$, where the causal mechanisms are given by

$$
\check{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad \check{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1} e_{2}, \quad \check{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad \check{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{2}
$$

and $\mathbb{P}_{\boldsymbol{\mathcal { E }}}=\mathbb{P}^{\boldsymbol{E}}$ with $E_{1}, E_{2} \sim \mathcal{U}(\{-1,1\})$ uniformly distributed and $E_{1} \pm E_{2}$. Then $\overline{\mathcal{M}}$ and $\overline{\mathcal{M}}$ are interventionally equivalent although $\mathcal{G}(\overline{\mathcal{M}})$ is not equal to $\mathcal{G}(\overline{\mathcal{M}})$ (see Figure 3).

Example D. 6 showcases an SCM with two endogenous and three exogenous variables, for which there is no interventionally equivalent SCM (satisfying smoothness constraints) with one exogenous variable taking values in $\mathbb{R}^{2}$ whose first and second components enter in the first and second structural equation, respectively. In this sense, representing confounders with dependent exogenous variables can be nontrivial in nonlinear models.
4.3. Counterfactual equivalence We consider two SCMs to be counterfactually equivalent if their twin SCMs induce the same counterfactual distributions under every perfect intervention.

Definition 4.5 (Counterfactual equivalence). Two SCMs $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { Z }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ and $\overline{\mathcal{M}}=\left\langle\overline{\mathcal{I}}, \overline{\mathcal{J}}, \overline{\mathcal{X}}, \check{\boldsymbol{f}}, \mathbb{P}_{\overline{\mathcal{E}}}\right\rangle$ are counterfactually equivalent with respect to $\mathcal{O} \subseteq \mathcal{I} \cap \overline{\mathcal{I}}$, denoted by $\mathcal{M} \equiv_{\mathcal{O}(\mathcal{O})} \overline{\mathcal{M}}$, if $\mathcal{M}^{\text {twin }}$ and $\overline{\mathcal{M}}^{\text {twin }}$ are interventionally equivalent with respect to $\mathcal{O} \cup \mathcal{O}^{\prime}$, where $\mathcal{O}^{\prime}$ corresponds to the copy of $\mathcal{O}$ in $\mathcal{I}^{\prime} \cap \overline{\mathcal{I}}^{\prime}$. $\mathcal{M}$ and $\overline{\mathcal{M}}$ are called counterfactually equivalent if they are counterfactually equivalent with respect to $\mathcal{I}=\overline{\mathcal{I}}$.

The notion of counterfactual equivalence is coarser than equivalence and finer than interventional equivalence.

Proposition 4.6. For SCMs, we have that equivalence implies counterfactual equivalence w.r.t. $\mathcal{O}$, which in turn implies interventional equivalence w.r.t. $\mathcal{O}$, for any $\mathcal{O} \subseteq \mathcal{I}$.

Interventionally equivalent SCMs that have the same causal mechanism (that differ only in their exogenous distribution) may not be counterfactually equivalent (see, e.g., Example D.7). Although the notion of counterfactual equivalence is finer than the notion of observational and interventional equivalence, the (augmented) graphs for counterfactually equivalent SCMs are in general not equal to each other (see Example D.10).
4.4. Relations between equivalences The definitions of observational, interventional and counterfactual equivalence provide equivalence relations on the set of all SCMs. For two SCMs to be observationally, interventionally or counterfactually equivalent w.r.t. $\mathcal{O} \subseteq \mathcal{I} \cap \overline{\mathcal{I}}$, the domains of their endogenous variables $\mathcal{O}$ have to be equal, that is, $\boldsymbol{\mathcal { X }}_{\mathcal{O}}=\overline{\mathcal{X}}_{\mathcal{O}}$. Apart from that, the index sets of the endogenous and the exogenous variables, the spaces of the other endogenous and exogenous variables, the causal mechanism and the exogenous probability measure may all differ. The observational, interventional and counterfactual equivalence classes w.r.t. $\mathcal{O} \subseteq \mathcal{I} \cap \overline{\mathcal{I}}$ are related in the following way (see Proposition 4.6):

$$
\begin{aligned}
\mathcal{M} \text { and } \overline{\mathcal{M}} \text { are equivalent } & \Longrightarrow \quad \mathcal{M} \text { and } \overline{\mathcal{M}} \text { are counterfactually equivalent w.r.t. } \mathcal{O} \\
& \Longrightarrow \quad \mathcal{M} \text { and } \overline{\mathcal{M}} \text { are interventionally equivalent w.r.t. } \mathcal{O} \\
& \Longrightarrow \quad \mathcal{M} \text { and } \overline{\mathcal{M}} \text { are observationally equivalent w.r.t. } \mathcal{O}
\end{aligned}
$$

This hierarchy allows us to compare SCMs at different levels of abstraction and formally establishes the "ladder" of causation (last two implications) [51, 53, 69].

5. Marginalizations In this section, we show how, and under which condition, one can marginalize an SCM over a subset $\mathcal{L} \subseteq \mathcal{I}$ of endogenous variables (thereby "hiding" the variables $\mathcal{L}$ ), to another SCM on the margin $\mathcal{I} \backslash \mathcal{L}$ that is observationally, interventionally and even counterfactually equivalent with respect to $\mathcal{I} \backslash \mathcal{L}$. In other words, we provide a formal notion of marginalization and show that this preserves the probabilistic, causal and counterfactual semantics on the margin.

The problem of marginalization of directed graphical models has been addressed for acyclic graph structures, for example, ADMGs and mDAGs [see 15, 16, 60, 62, 78, a.o.], and more recently in [18] for certain graph structures ("HEDGes") that may include cycles. Although in the acyclic setting it has been shown that the marginalization for some of these graph structures preserves the probabilistic and causal semantics, in the cyclic setting this has only been shown for modular SCMs [18]. We show that without the additional structure of a compatible system of solution functions (see Appendix A.3) one can still define a marginalization for SCMs under certain local unique solvability conditions. Intuitively, the idea is that if the state of a subsystem of endogenous variables is uniquely determined by the parents outside of this subsystem, then one can ignore the internals of this subsystem by treating it as a "black box" that can be described by certain measurable solution functions (see Figure 4). One can marginalize over this subsystem by substituting these measurable solution functions into the rest of the model, thereby removing the functional dependencies on the variables of the subsystem from the rest of the system, while preserving the probabilistic, causal and the counterfactual semantics of the rest of the system. We show that in general this marginalization operation defined on SCMs does not respect the latent projection on its associated (augmented) graph, where the latent projection is a similar marginalization operation defined on directed mixed graphs [15, 76, 78]. We show that under certain stronger local ancestral unique solvability conditions the marginalization does respect the latent projection.
5.1. Marginalization of a structural causal model Before we show how one can marginalize an SCM w.r.t. a subset of endogenous variables, we first point out that in general it is not always possible to find an SCM on the margin that preserves the causal semantics, as the following example illustrates.

Example 5.1 (No SCM on the margin preserves the causal semantics). Consider the SCM $\mathcal{M}=\left\langle\mathbf{3}, \emptyset, \mathbb{R}^{3}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ with causal mechanism $f_{1}(\boldsymbol{x})=x_{1}+x_{2}+x_{3}, \quad f_{2}(\boldsymbol{x})=$ $x_{2}, \quad f_{3}(\boldsymbol{x})=0$. Then there exists no SCM $\tilde{\mathcal{M}}$ on the endogenous variables $\{2,3\}$ that is interventionally equivalent to $\mathcal{M}$ w.r.t. $\{2,3\}$. To see this, suppose there exists such an SCM $\tilde{\mathcal{M}}$, then for every $\left(\xi_{2}, \xi_{3}\right) \in \boldsymbol{\mathcal { X }}_{\{2,3\}}$ such that $\xi_{2}+\xi_{3} \neq 0$ the intervened model $\tilde{\mathcal{M}}_{\mathrm{do}\left(\{2,3\},\left(\xi_{2}, \xi_{3}\right)\right)}$ has a solution but $\mathcal{M}_{\mathrm{do}\left(\{2,3\},\left(\xi_{2}, \xi_{3}\right)\right)}$ does not.

More generally, for an SCM $\mathcal{M}$ that is not solvable w.r.t. a subset $\mathcal{L} \subseteq \mathcal{I}$ there is no SCM $\tilde{\mathcal{M}}$ on the endogenous variables $\mathcal{I} \backslash \mathcal{L}$ that is interventionally equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}$.

The following example illustrates that for an SCM that is uniquely solvable w.r.t. a subset there exists an SCM on the margin that preserves the causal semantics.

Example 5.2 (SCM on the margin that preserves the causal semantics). Consider the SCM $\mathcal{M}$ of Example 3.11 that is uniquely solvable w.r.t. the subset $\mathcal{L}=\{2,3\}$ (depicted by the gray box in Figure 4). Substituting the measurable solution functions $\boldsymbol{g}_{\mathcal{L}}$ into the causal mechanism components $f_{1}$ and $f_{4}$ for the remaining endogenous variables $\{1,4\}$ gives a "marginal" causal mechanism $\tilde{f}_{1}(\boldsymbol{x}, e):=e$ and $\tilde{f}_{4}(\boldsymbol{x}, e):=x_{1}$. This defines an SCM $\tilde{\mathcal{M}}$ on the margin $\mathcal{I} \backslash \mathcal{L}=\{1,4\}$ that is interventionally equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}$ to $\mathcal{M}$.

In general, for an SCM $\mathcal{M}$ and a given subset $\mathcal{L} \subseteq \mathcal{I}$ of endogenous variables and its complement $\mathcal{O}=\mathcal{I} \backslash \mathcal{L}$, we can consider the "subsystem" of structural equations $\boldsymbol{x}_{\mathcal{L}}=\boldsymbol{f}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathcal{L}}, \boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)$. If $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ with measurable solution function $\boldsymbol{g}_{\mathcal{L}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}}$, then for each input $\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{L})}\right) \in \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})}$ of the subsystem, there exists an output $\boldsymbol{x}_{\mathcal{L}} \in \boldsymbol{\mathcal { X }}_{\mathcal{L}}$, which is unique for $\mathbb{P}_{\boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})}}$-almost every $\boldsymbol{e}_{\mathrm{pa}(\mathcal{L})} \in \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})}$ and for all $\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}} \in \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}$. We can remove this subsystem of endogenous variables from the model by substitution. This leads to a marginal SCM that is observationally, interventionally and counterfactually equivalent to the original SCM w.r.t. the margin, as we prove in Theorem 5.6.

DEFINITION 5.3 (Marginalization of an SCM). Let $\mathcal{M}=\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$ be an SCM that is uniquely solvable w.r.t. a subset $\mathcal{L} \subseteq \mathcal{I}$ and let $\mathcal{O}=\mathcal{I} \backslash \mathcal{L}$. For $\boldsymbol{g}_{\mathcal{L}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}} \times$ $\boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})} \rightarrow \mathcal{L}$, any measurable solution function of $\mathcal{M}$ w.r.t. $\mathcal{L}$, we call the $\operatorname{SCM} \mathcal{M}_{\operatorname{marg}(\mathcal{L})}:=$ $\left\langle\mathcal{O}, \mathcal{J}, \boldsymbol{\mathcal { X }}_{\mathcal{O}}, \boldsymbol{\mathcal { E }}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ with the marginal causal mechanism $\tilde{\boldsymbol{f}}: \boldsymbol{\mathcal { X }}_{\mathcal{O}} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ given by

$$
\tilde{\boldsymbol{f}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)=\boldsymbol{f}_{\mathcal{O}}\left(\boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{L})}\right), \boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)
$$

a marginalization of $\mathcal{M}$ w.r.t. $\mathcal{L}$. We denote by $\operatorname{marg}(\mathcal{L})(\mathcal{M})$ the equivalence class of the marginalizations of $\mathcal{M}$ w.r.t. $\mathcal{L}$.

The marginalization of $\mathcal{M}$ w.r.t. $\mathcal{L}$ is defined up to the equivalence $\equiv$ on SCMs, since the measurable solution functions $\boldsymbol{g}_{\mathcal{L}}$ are uniquely defined up to $\mathbb{P}_{\mathcal{E}}$-null sets. With this definition at hand, we can always construct a marginal SCM over a subset of the endogenous variables of an acyclic SCM by mere substitution (see also Proposition 3.4). Moreover, this definition extends that notion to SCMs that are uniquely solvable w.r.t. a certain subset. For linear SCMs this condition translates into a matrix invertibility condition, and since substitution preserves linearity, marginalization yields a linear marginal SCM (see Proposition C.5).

In general, marginalization is not always defined for all subsets. For instance, the SCM of Example 3.11 cannot be marginalized over the variable 3 (due to the self-cycle at 3), but can be marginalized over the variables 2 and 3 together. It follows from Proposition 3.7 that we can only marginalize over a single variable if that variable has no self-cycle. Note that we may introduce new self-cycles if we marginalize over a subset of variables, as can be seen, for example, from the SCM $\mathcal{M}$ in Example 2.8. This SCM has only one self-cycle; however, marginalizing w.r.t. $\{2\}$ gives a marginal SCM with another self-cycle at variable 4.

The definition of marginalization satisfies an intuitive property: if we can marginalize over two disjoint subsets after each other, then we can also marginalize over the union of those subsets at once, and the respective results agree.

Proposition 5.4. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an SCM that is uniquely solvable w.r.t. a subset $\mathcal{L}_{1} \subseteq \mathcal{I}$ and let $\mathcal{L}_{2} \subseteq \mathcal{I}$ be a subset disjoint from $\mathcal{L}_{1}$. Then $\mathcal{M}_{\operatorname{marg}\left(\mathcal{L}_{1}\right)}$ is uniquely solvable w.r.t. $\mathcal{L}_{2}$ if and only if $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}_{1} \cup \mathcal{L}_{2}$, Moreover, $\operatorname{marg}\left(\mathcal{L}_{2}\right) \circ \operatorname{marg}\left(\mathcal{L}_{1}\right)(\mathcal{M})=\operatorname{marg}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)(\mathcal{M})$.

In this proposition, $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ have to be disjoint, since marginalizing first over $\mathcal{L}_{1}$ gives a marginal $\operatorname{SCM} \mathcal{M}_{\operatorname{marg}\left(\mathcal{L}_{1}\right)}$ with endogenous variables $\mathcal{I} \backslash \mathcal{L}_{1}$.

Next, we show that the distributions of a marginal SCM are identical to the marginal distributions induced by the original SCM. A simple proof of this result proceeds by showing that both the intervention and the twin operation commute with marginalization.

Proposition 5.5. Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. a subset $\mathcal{L} \subseteq \mathcal{I}$. Then the marginalization $\operatorname{marg}(\mathcal{L})$ commutes with both:

1. the perfect intervention $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ for a subset $I \subseteq \mathcal{I} \backslash \mathcal{L}$ and a value $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$, that is, $\left(\operatorname{mag}(\mathcal{L}) \circ \operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)\right)(\mathcal{M})=(\operatorname{do}(I, \boldsymbol{\xi}) \circ \operatorname{mag}(\mathcal{L}))(\mathcal{M})$, and
2. the twin operation twin, that is, $\left(\operatorname{mag}\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right) \circ \operatorname{twin}\right)(\mathcal{M})=(\operatorname{twin} \circ \operatorname{mag}(\mathcal{L}))(\mathcal{M})$, where $\mathcal{L}^{\prime}$ is the copy of $\mathcal{L}$ in $\mathcal{I}^{\prime}$.

With Proposition 5.5 at hand, we can prove the main result of this subsection.
THEOREM 5.6 (Marginalization of an SCM preserves the observational, causal and counterfactual semantics). Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. a subset $\mathcal{L} \subseteq \mathcal{I}$. Then $\mathcal{M}$ and $\operatorname{mag}(\mathcal{L})(\mathcal{M})$ are observationally, interventionally and counterfactually equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}$.

This shows that our definition of marginalization (Definition 5.3) preserves the probabilistic, causal and counterfactual semantics, under a certain local unique solvability condition. Moreover, this allows us to marginalize SCMs w.r.t. a certain subset that do not satisfy the additional assumptions imposed by modular SCMs, for example, the SCM $\mathcal{M}$ of Example 3.11 does not have any additional structure of a compatible system of solution functions, but $\mathcal{M}$ can be marginalized w.r.t. the subset $\{2,3\}$ (see Appendix A.3).

In general, interventional equivalence does not imply counterfactual equivalence (see, e.g., Example D.7). However, for our definition of marginalization we arrive at a marginal SCM that is not only interventionally equivalent, but also counterfactually equivalent w.r.t. the margin.

For an SCM $\mathcal{M}$, unique solvability w.r.t. a certain subset $\mathcal{L} \subseteq \mathcal{I}$ is a sufficient, but not a necessary condition for the existence of an SCM $\tilde{\mathcal{M}}$ on the margin $\mathcal{I} \backslash \mathcal{L}$ such that $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are counterfactually equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}$ (see, e.g., Example D.11). Hence, in certain cases it may be possible to relax the uniqueness condition.
5.2. Marginalization of a graph We now turn to a marginalization operation for directed mixed graphs, which we call the latent projection. This name is inspired from a similar construction on directed mixed graphs in [78]. In [78], the authors concentrate on a mapping between directed mixed graphs and show that it preserves conditional independence properties [see also 76]. In this subsection, we provide a sufficient condition for the marginalization of an SCM to respect the latent projection, that is, that the augmented graph of the marginal SCM is a subgraph of the latent projection of the augmented graph of the original SCM.

DEFINITION 5.7 (Marginalization/latent projection of a directed mixed graph). Let $\mathcal{G}=$ $(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathcal{L} \subseteq \mathcal{V}$ a subset. The marginalization of $\mathcal{G}$ w.r.t. $\mathcal{L}$ or the latent projection of $\mathcal{G}$ onto $\mathcal{V} \backslash \mathcal{L}$ maps $\mathcal{G}$ to the marginal graph $\operatorname{mag}(\mathcal{L})(\mathcal{G}):=(\tilde{\mathcal{V}}, \tilde{\mathcal{E}}, \tilde{\mathcal{B}})$, where:

1. $\tilde{\mathcal{V}}=\mathcal{V} \backslash \mathcal{L}$,
2. for $i, j \in \tilde{\mathcal{V}}: i \rightarrow j \in \tilde{\mathcal{E}}$ if and only if there exists a directed path $i \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow j$ in $\mathcal{G}$ with $n \geq 0$ and $\ell_{1}, \ldots, \ell_{n} \in \mathcal{L}$,
3. for $i \neq j \in \tilde{\mathcal{V}}: i \leftrightarrow j \in \tilde{\mathcal{B}}$ if and only if
a) there exist $n, m \geq 0, \ell_{1}, \ldots, \ell_{n} \in \mathcal{L}, \tilde{\ell}_{1}, \ldots, \tilde{\ell}_{m} \in \mathcal{L}$ such that $i \leftarrow l_{1} \leftarrow l_{2} \leftarrow \cdots \leftarrow$ $\ell_{n} \leftrightarrow \tilde{\ell}_{m} \rightarrow \tilde{\ell}_{m-1} \rightarrow \cdots \rightarrow \tilde{\ell}_{1} \rightarrow j$ in $\mathcal{G}$, or
b) there exist $n, m \geq 1, \ell_{1}, \ldots, \ell_{n} \in \mathcal{L}, \tilde{\ell}_{1}, \ldots, \tilde{\ell}_{m} \in \mathcal{L}$ such that $i \leftarrow l_{1} \leftarrow l_{2} \leftarrow \cdots \leftarrow \ell_{n}$ and $\tilde{\ell}_{m} \rightarrow \tilde{\ell}_{m-1} \rightarrow \cdots \rightarrow \tilde{\ell}_{1} \rightarrow j$ in $\mathcal{G}$ and $\ell_{n}=\tilde{\ell}_{m}$.

Note that this gives $\mathcal{G}(\mathcal{M})=\operatorname{mag}(\mathcal{J})\left(\mathcal{G}^{a}(\mathcal{M})\right)$ for any SCM $\mathcal{M}$. Further, for a subgraph $\mathcal{H} \subseteq \mathcal{G}$ we have $\operatorname{mag}(\mathcal{L})(\mathcal{H}) \subseteq \operatorname{mag}(\mathcal{L})(\mathcal{G})$ for any subset of nodes $\mathcal{L}$. It does not matter in which order we project out the nodes or if we perform several projections at once.

Proposition 5.8. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathcal{L}_{1}, \mathcal{L}_{2} \subseteq \mathcal{V}$ two disjoint subsets. Then $\left(\operatorname{merg}\left(\mathcal{L}_{1}\right) \circ \operatorname{merg}\left(\mathcal{L}_{2}\right)\right)(\mathcal{G})=\left(\operatorname{merg}\left(\mathcal{L}_{2}\right) \circ \operatorname{merg}\left(\mathcal{L}_{1}\right)\right)(\mathcal{G})=\operatorname{merg}\left(\mathcal{L}_{1} \cup\right.$ $\left.\mathcal{L}_{2}\right)(\mathcal{G})$.

Similar to the definition of marginalization for SCMs, this definition of the latent projection commutes with both the (graphical) perfect intervention and the twin operation.

Proposition 5.9. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathcal{L}, \mathcal{I}, I \subseteq \mathcal{V}$ subsets. Then the marginalization $\operatorname{merg}(\mathcal{L})$ commutes with both:

1. perfect intervention $\operatorname{do}(I)$ if $I$ is disjoint from $\mathcal{L}$, that is, $(\operatorname{merg}(\mathcal{L}) \circ \operatorname{do}(I))(\mathcal{G})=(\operatorname{do}(I) \circ$ $\operatorname{merg}(\mathcal{L}))(\mathcal{G})$, and
2. the twin operation $\operatorname{twin}(\mathcal{I})$ if $\mathcal{B}=\emptyset, \mathcal{J}:=\mathcal{V} \backslash \mathcal{I}$ is exogenous (i.e., $\operatorname{pa}_{\mathcal{G}}(\mathcal{J})=\emptyset$ ) and $\mathcal{L} \subseteq \mathcal{I}$, that is, $\left(\operatorname{merg}\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right) \circ \operatorname{twin}(\mathcal{I})\right)(\mathcal{G})=(\operatorname{twin}(\mathcal{I} \backslash \mathcal{L}) \circ \operatorname{merg}(\mathcal{L}))(\mathcal{G})$,
where $\mathcal{L}^{\prime}$ is the copy of $\mathcal{L}$ in $\mathcal{I}^{\prime}$.
An example of an SCM for which a marginalization respects the latent projection is the SCM $\mathcal{M}$ of Example 2.8. Marginalizing $\mathcal{M}$ w.r.t. $\mathcal{L}=\{2\}$ gives a marginal $\operatorname{SCM} \mathcal{M}_{\operatorname{merg}(\mathcal{L})}$ with a graph that is a subgraph of the latent projection of the graph of the SCM $\mathcal{M}$ onto $\mathcal{I} \backslash \mathcal{L}$. In general, not all marginalizations respect the latent projection, as is illustrated in the following example.

EXAMPLE 5.10 (Marginalization does not respect the latent projection). Consider the SCM $\mathcal{M}$ of Example 3.11. Although $\mathcal{M}$ and its marginalization $\mathcal{M}_{\operatorname{merg}(\mathcal{L})}$ with $\mathcal{L}=\{2,3\}$ are interventionally equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}=\{1,4\}$, the graph $\mathcal{G}\left(\mathcal{M}_{\operatorname{merg}(\mathcal{L})}\right)$ is not a subgraph of the latent projection of $\mathcal{G}(\mathcal{M})$ onto $\mathcal{I} \backslash \mathcal{L}$, as can be verified from the graphs depicted in Figure 4.

Under the local ancestral unique solvability condition, which is a stronger condition than the local unique solvability condition (i.e., ancestral unique solvability w.r.t. a subset implies unique solvability w.r.t. that subset), one can prove that the marginalization of an SCM respects the latent projection.

Proposition 5.11. Let $\mathcal{M}$ be an SCM that is ancestrally uniquely solvable w.r.t. a subset $\mathcal{L} \subseteq \mathcal{I}$. Then $\left(\mathcal{G}^{a} \circ \operatorname{merg}(\mathcal{L})\right)(\mathcal{M}) \subseteq\left(\operatorname{merg}(\mathcal{L}) \circ \mathcal{G}^{a}\right)(\mathcal{M})$ and $(\mathcal{G} \circ \operatorname{merg}(\mathcal{L}))(\mathcal{M}) \subseteq$ $(\operatorname{merg}(\mathcal{L}) \circ \mathcal{G})(\mathcal{M})$.

The (augmented) graph of a marginalized SCM can be a strict subgraph of the corresponding latent projection if, for example, certain paths cancel each other out after the substitution of the measurable solution function(s) into the causal mechanism(s) on the margin (see Example D.12). For acyclic SCMs, we recover with Proposition 5.11 the known result that this class is closed under marginalization (see Proposition 3.4) [15]. For linear SCMs, we have that unique solvability w.r.t. a subset $\mathcal{L}$ holds if and only if ancestral unique solvability w.r.t. $\mathcal{L}$ holds (see Proposition C.4), and hence, a marginalization of a linear SCM always respects the latent projection.
6. Markov properties In this section, we give a short overview of Markov properties for SCMs with cycles. We make use of the Markov properties that were recently developed by Forré and Mooij [18] for HEDGes, a graphical representation that is similar to the augmented graph of SCMs. We briefly summarize some of their main results and apply them to the class

of SCMs. In Appendix A.2, we provide a more thorough introduction and give an intuitive derivation, which can act as an entry point for the reader into the more extensive discussion of Markov properties provided in [18].

Markov properties associate a set of conditional independence relations to a graph. The directed global Markov property for directed acyclic graphs (see Definitions A. 4 and A.6), also known as the $d$-separation criterion [50], is one of the most widely used. It directly extends to a similar property for acyclic directed mixed graphs (ADMGs) [60]. It does not hold in general for cyclic SCMs, however, as was already observed earlier [71, 72].

EXAMPLE 6.1 (Directed global Markov property does not hold for cyclic SCM). One can check that for every solution $\boldsymbol{X}$ of the SCM $\mathcal{M}$ of Example 3.5, $X_{1}$ is not independent of $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$. However, the variables $X_{1}$ and $X_{2}$ are d-separated given $\left\{X_{3}, X_{4}\right\}$ in $\mathcal{G}(\mathcal{M})$ (see Figure 3). Hence the global directed Markov property does not hold here.

Although some progress has been made in the case of discrete [18, 49, 52] and linear models [18, 27, 31, 63, 70-72], only recently a general directed global Markov property has been introduced for more general cyclic models [18], that is based on $\sigma$-separation (see Definition A. 16 and A.20), an extension of $d$-separation. This notion of $\sigma$-separation was derived from the notion of $d$-separation in the acyclification of the graph [18] (see Definition A.13). The acyclification of a graph generalizes the idea of the collapsed graph developed by Spirtes [71] and can, in particular, be applied to the graphs of SCMs. The main idea of the acyclification is that under the condition that the SCM is uniquely solvable w.r.t. each strongly connected component, we can replace the causal mechanisms of these strongly connected components by their measurable solution functions, which results in an acyclic SCM. This acyclified SCM (see Definition A.11) is observationally equivalent to the original SCM (see Proposition A.12).

EXAMPLE 6.2 (Construction of an observationally equivalent acyclic SCM). The SCM $\mathcal{M}$ of Example 3.5 is uniquely solvable w.r.t. all its strongly connected components, that is, the subsets $\{1\},\{2\}$ and $\{3,4\}$. Replacing the causal mechanisms of these strongly connected components by their measurable solution functions gives the observationally equivalent SCM $\overline{\mathcal{M}}$ of Example 4.2. Because $\overline{\mathcal{M}}$ is acyclic (see Figure 3) we can apply the directed global Markov property to $\overline{\mathcal{M}}$. The fact that $X_{1}$ and $X_{2}$ are not d-separated given $\left\{X_{3}, X_{4}\right\}$ in $\mathcal{G}(\overline{\mathcal{M}})$ is in line with $X_{1}$ being dependent of $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$ for every solution $\boldsymbol{X}$ of $\overline{\mathcal{M}}$ (and hence of $\mathcal{M}$ ).

This acyclification preserves solutions, and $d$-separation in the acyclification can directly be translated into $\sigma$-separation on the original graph (see Proposition A.19). This leads to the general directed global Markov property. The following theorem summarizes the main results of [18] applied to SCMs.

THEOREM 6.3 (Global Markov properties for SCMs [18]). Let $\mathcal{M}$ be a uniquely solvable SCM. Then its observational distribution $\mathbb{P}^{\boldsymbol{X}}$ exists, is unique and the following two statements hold:

1. $\mathbb{P}^{\boldsymbol{X}}$ satisfies the directed global Markov property (" $d$-separation criterion") relative to $\mathcal{G}(\mathcal{M})$ (see Definition A.6) if $\mathcal{M}$ satisfies at least one of the following conditions:
a) $\mathcal{M}$ is acyclic;
b) all endogenous spaces $\mathcal{X}_{i}$ are discrete and $\mathcal{M}$ is ancestrally uniquely solvable;
c) $\mathcal{M}$ is linear (see Definition C.1), each of its causal mechanisms $\left\{f_{i}\right\}_{i \in \mathcal{I}}$ has a nontrivial dependence on at least one exogenous variable, and $\mathbb{P}_{\mathbb{E}}$ has a density w.r.t. the Lebesgue measure on $\mathbb{R}^{\mathcal{J}}$.

2. $\mathbb{P}^{\boldsymbol{X}}$ satisfies the general directed global Markov property (" $\sigma$-separation criterion") relative to $\mathcal{G}(\mathcal{M})$ (see Definition A.20) if $\mathcal{M}$ is uniquely solvable w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M}){ }^{14}$

The general directed global Markov property is generally weaker than the directed global Markov property, since $\sigma$-separation implies $d$-separation. The acyclic case is well known and was first shown in the context of linear-Gaussian structural equation models [32, 75]. The discrete case fixes the erroneous theorem by Pearl and Dechter [52], for which a counterexample was found by Neal [49], by adding the ancestral unique solvability condition, and extends it to allow for bidirected edges in the graph. The linear case is an extension of existing results for the linear-Gaussian setting without bidirected edges [31, 71, 72] to a linear (possibly non-Gaussian) setting with bidirected edges in the graph.

In constraint-based approaches to causal discovery, one usually assumes the converse of the (general) directed global Markov property to hold [51, 73], which is called $\sigma$-faithfulness respectively $d$-faithfulness (see Definition A. 9 and A.23). Meek [41] showed that for multinomial and linear-Gaussian DAG (i.e., acyclic and causally sufficient SCMs) models, $d$ faithfulness holds for all parameter values up to a measure zero set. Up to our knowledge no such results have been shown in more general parametric or nonparametric settings (neither for $d$-faitfhulness in acyclic or cyclic settings, nor for $\sigma$-faithfulness).
7. Causal interpretation of the graph of SCMs In Example 4.4, we already saw that sometimes no information in the observational, interventional and even the counterfactual distributions suffices to decide whether a directed path or bidirected edge is present in the graph, or not. Here, we do not attempt to provide a complete characterization of the conditions under which the presence or absence of a directed path or bidirected edge in the graph can be identified from the observational and interventional distributions. Instead, we give sufficient conditions to detect a directed path and bidirected edge in the graph.

In general, cyclic SCMs may have none, one or multiple induced observational distributions, and this may change after intervening in the system. Here, we restrict ourselves to graphs of SCMs where the induced (marginal) observational and interventional distributions are uniquely defined.
7.1. Directed paths and edges For cyclic SCMs, the causal interpretation of the SCM is not always consistent with its graph. This can be illustrated with the SCM $\mathcal{M}$ of Example 5.10. Here, one sees a difference in the marginal distribution $\mathbb{P}_{\mathcal{M}_{\mathrm{do}(\{1\}, \xi_{1})}}$ on $\mathcal{X}_{4}$ for different values of $\xi_{1}$, although variable 1 is not an ancestor of variable 4 and each marginal distribution $\mathbb{P}_{\mathcal{M}_{\mathrm{do}(\{1\}, \xi_{1})}}$ on $\mathcal{X}_{4}$ is uniquely defined. This counterintuitive behavior that an intervention on a nonancestor of a variable can change the distribution of that variable was already observed by Neal [49]. However, under a specific unique solvability condition, we obtain a direct causal interpretation for the absence of a directed edge or directed path in the graph of an SCM.

[^0]
[^0]:    ${ }^{14}$ Since [18] also provides results under the weaker condition that an SCM is solvable (not necessarily uniquely) w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$, one might believe that Theorem 6.3.(2) could be generalized to stating that in that case, any of its observational distributions satisfies the general directed global Markov property. However, that is not true: consider, for example, the SCM $\mathcal{M}=\left\langle\mathbf{2}, \emptyset, \mathbb{R}^{2}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ with $f_{1}(\boldsymbol{x})=x_{1}$ and $f_{2}(\boldsymbol{x})=x_{2}$. Then $\mathcal{M}$ is solvable w.r.t. each of its strongly connected components $\{1\}$ and $\{2\}$. The solution with $X_{1}=X_{2}$, where $X_{2}$ has a nondegenerate distribution, shows a dependence between $X_{1}$ and $X_{2}$, and thus $X_{1} \perp X_{2}$ does not hold. In general, all strongly connected components that admit multiple solutions may be dependent on any other variable(s) in the model.

Proposition 7.1 (Sufficient condition for detecting a directed edge in the latent projection of the graph of an SCM). Consider an $\operatorname{SCM} \mathcal{M}=\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { E }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$, a subset $\mathcal{O} \subseteq \mathcal{I}$ and $i, j \in \mathcal{O}$ such that $i \neq j$. Let $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$, where $I:=\mathcal{O} \backslash\{i, j\}$, such that $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ is uniquely solvable w.r.t. $\operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right) \backslash i}(j)$. If there exist values $\xi_{i} \neq \tilde{\xi}_{i} \in \mathcal{X}_{i}$ such that both $\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \xi_{i}\right)}$ and $\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \tilde{\xi}_{i}\right)}$ induce unique marginal distributions on $\mathcal{X}_{j}$, and these two induced distributions do not coincide, that is, there exists a measurable set $\mathcal{B}_{j} \subseteq \mathcal{X}_{j}$ such that

$$
\mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \xi_{i}\right)}}\left(X_{j} \in \mathcal{B}_{j}\right) \neq \mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \tilde{\xi}_{i}\right)}}\left(X_{j} \in \mathcal{B}_{j}\right)
$$

the directed edge $i \rightarrow j$ is present in the latent projection $\operatorname{marg}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\mathcal{M}))$ of $\mathcal{G}(\mathcal{M})$ on $\mathcal{O}$.

Two cases are of special interest: $\mathcal{O}=\mathcal{I}$, which corresponds with a directed edge $i \rightarrow j$ in $\mathcal{G}(\mathcal{M})$, and $\mathcal{O}=\{i, j\}$, which corresponds with a directed path $i \rightarrow \cdots \rightarrow j$ in $\mathcal{G}(\mathcal{M})$.

The condition in Proposition 7.1 is a sufficient condition for determining whether a directed edge or path is present in the graph. In general, not all directed edges and paths can be identified from the interventional distributions with this sufficient condition. For example, no interventional distribution satisfies the condition of Proposition 7.1 for the SCM $\overline{\mathcal{M}}$ in Example 4.4, although there is a directed edge $1 \rightarrow 2$ in the graph $\mathcal{G}(\overline{\mathcal{M}})$.
7.2. Bidirected edges It is well known that there exists a similar sufficient condition for detecting bidirected edges in the graph of an acyclic SCM also known as the commoncause principle [see, e.g., 51]. In the two variables case, this criterion informally states that there exists a bidirected edge between the variables $i$ and $j$ in the graph of the SCM, if the marginal interventional distribution of $X_{j}$ under the intervention $\operatorname{do}(\{i\}, x_{i})$ differs from the conditional distribution of $X_{j}$ given $X_{i}=x_{i}$ (see Example D.13). The following proposition provides a generalization of this sufficient condition for detecting bidirected edges in graphs of SCMs that may include cycles.

Proposition 7.2 (Sufficient condition for detecting a bidirected edge in the latent projection of the graph of an SCM). Consider an SCM $\mathcal{M}=\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$, a subset $\mathcal{O} \subseteq \mathcal{I}$ and $i, j \in \mathcal{O}$ such that $i \neq j$. Let $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$, where $I:=\mathcal{O} \backslash\{i, j\}$, such that $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ is uniquely solvable w.r.t. both $\operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)}(i)$ and $\operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right) \backslash i}(j)$. Assume that for every $\xi_{i} \in \mathcal{X}_{i}$ both $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ and $\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \xi_{i}\right)}$ induce a unique marginal distribution on $\mathcal{X}_{j} \times \mathcal{X}_{i}$ and $\mathcal{X}_{j}$, respectively. If $j \notin \operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)}(i)$ and there exists a measurable set $\mathcal{B}_{j} \subseteq \mathcal{X}_{j}$ such that for every version of the regular conditional probability $\mathbb{P}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}\left(X_{j} \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right)$, there exists a value $\xi_{i} \in \mathcal{X}_{i}$ such that

$$
\mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}\left(\{i\}, \xi_{i}\right)}}\left(X_{j} \in \mathcal{B}_{j}\right) \neq \mathbb{P}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}\left(X_{j} \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right)
$$

then there exists a bidirected edge $i \leftrightarrow j$ in the latent projection $\operatorname{marg}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\mathcal{M}))$ of $\mathcal{G}(\mathcal{M})$ on $\mathcal{O}$.

This proposition gives a sufficient condition for determining that a bidirected edge is present in the graph. In general, not all bidirected edges in the graph can be identified from the observational, interventional and even the counterfactual distributions, as we saw in Example D.10. In this example, there exists a bidirected edge $1 \leftrightarrow 2 \in \mathcal{G}(\mathcal{M})$ while the density $p\left(x_{2} \mid \operatorname{do}\left(X_{1}=x_{1}\right)\right)=p\left(x_{2} \mid X_{1}=x_{1}\right)$ for all $x_{1} \in \mathcal{X}_{1}$. For the acyclic setting, the above criterion is generally considered as a universal way to detect a confounder (note that then one can also deal with the case $j \in \operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)}(i)$ by swapping the roles of $i$ and $j$ ). If $i$ and $j$ are part of a cycle, the above sufficient condition cannot be applied, and in that case, to the best of our knowledge, no simple sufficient conditions for detecting the presence of a bidirected edge are known.

8. Simple SCMs In this section, we introduce the well-behaved class of simple SCMs. Simple SCMs satisfy all the local unique solvability conditions to ensure that this class is closed under both perfect intervention and marginalization. They extend the subclass of acyclic SCMs to the cyclic setting, while preserving many of their convenient properties.

Definition 8.1 (Simple SCM). Let $\mathcal{M}=\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\rangle$ be an SCM. We call $\mathcal{M}$ simple if it is uniquely solvable w.r.t. every subset $\mathcal{O} \subseteq \mathcal{I}$.

Loosely speaking, an SCM is simple if any subset of its structural equations can be solved uniquely for its associated variables in terms of the other variables that appear in these equations. An example of a simple SCM is given in Example D.1.

On simple SCMs one can perform any number of marginalizations (see Definition 5.3) in any order (see Proposition 5.4). All these marginalizations respect the latent projection (see Proposition 5.11) and each resulting marginal SCM is again simple. Moreover, we show that this class is closed under intervention and the twin operation.

Proposition 8.2. The class of simple SCMs is closed under marginalization, perfect intervention and the twin operation.

The class of simple SCMs contains the acyclic SCMs as a subclass (see Proposition 3.4). In particular, a simple SCM has no self-cycles (see Proposition 3.7), since a self-cycle denotes that that variable cannot be uniquely (up to a $\mathbb{P}_{\mathcal{E}}$-null set) determined by its parents.

From Proposition 8.2, it follows that the results summarized in Theorem 6.3 also apply to all the observational, interventional and counterfactual distributions of simple SCMs.

Corollary 8.3 (Global Markov properties for simple SCMs). Let $\mathcal{M}$ be a simple SCM. Then the:

1. observational distribution,
2. interventional distribution after perfect intervention on $I \subset \mathcal{I}$,
3. counterfactual distribution after perfect intervention on $\bar{I} \subseteq \mathcal{I} \cup \mathcal{I}^{\prime}$,
all exist, are unique and satisfy the general directed global Markov property relative to $\mathcal{G}(\mathcal{M}), \operatorname{do}(I)(\mathcal{G}(\mathcal{M}))$ and $\operatorname{do}(\bar{I})(\operatorname{twin}(\mathcal{G}(\mathcal{M})))$, respectively. Moreover, if $\mathcal{M}$ satisfies at least one of the three conditions (1a), (1b), (1c) of Theorem 6.3, then they also obey the directed global Markov property relative to $\mathcal{G}(\mathcal{M}), \operatorname{do}(I)(\mathcal{G}(\mathcal{M}))$ and $\operatorname{do}(\bar{I})(\operatorname{twin}(\mathcal{G}(\mathcal{M})))$, respectively.

Many of these properties are also shown to hold for the class of modular SCMs [18], which contains, in particular, the class of simple SCMs (see Appendix A. 3 for more details).

Moreover, simple SCMs satisfy the unique solvability conditions of Proposition 7.1 and 7.2 , which allows us to define the causal relationships for simple SCMs in terms of its graph.

Definition 8.4 (Causal relationships for simple SCMs). Let $\mathcal{M}$ be a simple SCM.

1. If there exists a directed edge $i \rightarrow j \in \mathcal{G}(\mathcal{M})$, that is, $i \in \mathrm{pa}(j)$, then we call $i$ a direct cause of $j$ according to $\mathcal{M}$;
2. If there exists a directed path $i \rightarrow \cdots \rightarrow j$ in $\mathcal{G}(\mathcal{M})$, that is, $i \in \operatorname{an}(j)$, then we call $i$ a cause of $j$ according to $\mathcal{M}$;
3. If there exists a bidirected edge $i \leftrightarrow j \in \mathcal{G}(\mathcal{M})$, then we call $i$ and $j$ (latently) confounded according to $\mathcal{M}$.

In summary, we have the following sufficient conditions for determining the different causal and confoundedness relationships according to a specific simple SCM $\mathcal{M}$.

COROLLARY 8.5 (Sufficient conditions for the presence of causal and confoundedness relationships for simple SCMs). Let $\mathcal{M}$ be a simple SCM and $i, j \in \mathcal{I}$ such that $i \neq j$ and $I:=\mathcal{I} \backslash\{i, j\}$. Then:

1. If there exist values $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X } _ { I }}$ and $\xi_{i} \neq \bar{\xi}_{i} \in \mathcal{X}_{i}$ and a measurable set $\mathcal{B}_{j} \subseteq \mathcal{X}_{j}$ such that

$$
\mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}(\{i\}, \xi_{i})}}\left(X_{j} \in \mathcal{B}_{j}\right) \neq \mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}(\{i\}, \bar{\xi}_{i})}}\left(X_{j} \in \mathcal{B}_{j}\right)
$$

then $i$ is a direct cause of $j$ according to $\mathcal{M}$, that is, $i \rightarrow j \in \mathcal{G}(\mathcal{M})$;
2. If there exist values $\xi_{i} \neq \bar{\xi}_{i} \in \mathcal{X}_{i}$ and a measurable set $\mathcal{B}_{j} \subseteq \mathcal{X}_{j}$ such that

$$
\mathbb{P}_{\mathcal{M}_{\mathrm{do}(\{i\}, \xi_{i})}}\left(X_{j} \in \mathcal{B}_{j}\right) \neq \mathbb{P}_{\mathcal{M}_{\mathrm{do}(\{i\}, \bar{\xi}_{i})}}\left(X_{j} \in \mathcal{B}_{j}\right)
$$

then $i$ is a cause of $j$ according to $\mathcal{M}$, that is, $i \rightarrow \cdots \rightarrow j$ in $\mathcal{G}(\mathcal{M})$;
3. If $j \notin \operatorname{an}_{\mathcal{G}\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)}(i)$ and there exist a value $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X } _ { I }}$ and a measurable set $\mathcal{B}_{j} \subseteq$ $\mathcal{X}_{j}$ such that for every version of the regular conditional probability $\mathbb{P}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}\left(X_{j} \in\right.$ $\left.\mathcal{B}_{j} \mid X_{i}=\xi_{i}\right)$ there exists a value $\xi_{i} \in \mathcal{X}_{i}$ such that

$$
\mathbb{P}_{\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}\right)_{\mathrm{do}(\{i\}, \xi_{i})}}\left(X_{j} \in \mathcal{B}_{j}\right) \neq \mathbb{P}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}\left(X_{j} \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right)
$$

then $i$ and $j$ are confounded according to $\mathcal{M}$, that is, $i \leftrightarrow j \in \mathcal{G}(\mathcal{M})$.
For simple SCMs, it is in general not possible to identify all the causal and confoundedness relationships in the graph from the observational, interventional or even the counterfactual distributions. Examples 4.4 and D. 10 show that this is already impossible for acyclic SCMs without further assumptions.

Finally, there is a connection between SCMs and potential outcomes [68] that generalizes to the cyclic setting. One of the consequences of Proposition 8.2 is that all counterfactuals are defined for a simple SCM (even if it is cyclic). This allows us to define potential outcomes in terms of a simple SCM in the following way.

DEFINITION 8.6 (Potential outcome). Let $\mathcal{M}=\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { X }}, \boldsymbol{\mathcal { E }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{E}}\rangle$ be a simple SCM, $I \subseteq \mathcal{I}$ a subset, $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X } _ { I }}$ a value and $\boldsymbol{E}$ a random variable such that $\mathbb{P}^{\boldsymbol{E}}=\mathbb{P}_{\boldsymbol{E}}$. The potential outcome under the perfect intervention $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ is defined as $\boldsymbol{X}_{\boldsymbol{\xi}_{I}}:=\boldsymbol{g}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}\left(\boldsymbol{E}_{\mathrm{pa}(\mathcal{I})}\right)$, where $\boldsymbol{g}_{\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}}: \boldsymbol{\mathcal { E } _ { \mathrm { pa } ( \mathcal { I } ) }} \rightarrow \boldsymbol{\mathcal { X }}$ is a measurable solution function for $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$.
9. Discussion In this paper, we studied the basic properties of SCMs in the presence of cycles and latent variables without restricting to linear functional relationships between the variables. We saw that cyclic SCMs behave differently in many aspects than acyclic SCMs. Indeed, in the presence of cycles, many of the convenient properties of acyclic SCMs do not hold in general: SCMs do not always have a solution; they do not always induce unique observational, interventional and counterfactual distributions; a marginalization does not always exist, and if it exists the marginal model does not always respect the latent projection; they do not always satisfy a Markov property and their graphs are not always consistent with their causal semantics.

We introduced various notions of (unique) solvability and showed that under appropriate (unique) solvability conditions, many of the operations and results for the acyclic setting can be extended to SCMs with cycles. For example, we introduced several equivalence relations between SCMs to compare SCMs at different levels of abstraction, we showed how to define

marginal SCMs on a subset of the variables that are (in various ways) equivalent to the original SCM, we discussed under which conditions the distributions satisfy the (general) directed global Markov property relative to their graphs and we showed under which conditions the graph of an SCM can be interpreted causally. Most of these results are shown under sufficient conditions that are not necessary (e.g., for the marginalization operation this was shown in Example D.11). It may therefore be possible to further relax some of the conditions.

These insights led us to introduce the more well-behaved class of simple SCMs, which forms an extension of the class of acyclic SCMs to the cyclic setting that preserves many of its convenient properties: simple SCMs induce unique observational, interventional and counterfactual distributions; the class of simple SCMs is closed under both perfect intervention and marginalization; the marginalization respects the latent projection; the induced distributions obey the general directed global Markov property and obey the directed global Markov property in the acyclic, discrete and linear case. This class does not contain SCMs that have self-cycles and graphs of simple SCMs have a direct and intuitive causal interpretation.

One key property of simple SCMs is that the solutions always satisfy the conditional independencies implied by $\sigma$-separation. By simply replacing $d$-separation with $\sigma$-separation it turns out that one can directly extend results and algorithms for acyclic SCMs to the more general class of simple SCMs. For example, adjustment criteria (including the back-door criterion), Pearl's do-calculus and Tian's ID algorithm for the identification of causal effects have been extended recently to the class of modular SCMs, which contains the class of simple SCMs [20]. Several causal discovery algorithms have already been proposed that work with simple SCMs, for example, the first constraint-based causal discovery algorithm that can deal with cycles and nonlinear functional relationships [19]. Also, Local Causal Discovery (LCD) [10], Y-structures [38] and the Joint Causal Inference framework (JCI) all apply to simple SCMs [47] even though they were originally developed for acyclic SCMs only. Recently, it has been shown that even the well-known Fast Causal Inference (FCI) algorithm $[74,80]$ is directly applicable to simple SCMs [44] and provides a consistent estimate of the Markov equivalence class (under the faithfulness assumption). Moreover, a method for constructing nonlinear simple SCMs using neural networks and sampling from them has been proposed [19]. This illustrates that the class of simple SCMs forms a convenient and practical extension of the class of acyclic SCMs that can be used for the purposes of causal modeling, reasoning, discovery and prediction.

We hope that this work will provide the foundations for a general theory of statistical causal modeling with SCMs. Future work might consist of reparametrizing and reducing the space of the exogenous variables of an SCM while preserving the causal and counterfactual semantics; extending and generalizing the identifiability results for (direct) causes and confounders; extending the graphs of SCMs to represent selection bias; proving completeness results for some Markov properties for a subclass of SCMs that contains cycles.

Acknowledgments S. Bongers and J.M. Mooij are supported in part by NWO, the Netherlands Organization for Scientific Research (VIDI grant 639.072.410 and VENI grant 639.031.036). P. Forré and J.M. Mooij are supported in part by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement $\mathrm{n}^{\circ} 639466$ ). J. Peters is supported by research grants from VILLUM FONDEN (18968) and the Carlsberg Foundation.

The authors are grateful to Bernhard Schölkopf and Robin Evans for stimulating discussions, and to Noud de Kroon, Tineke Blom and Alexander Ly for providing helpful comments on earlier drafts. We thank two anonymous reviewers and the associate editor for helpful comments.

# 28

# FOUNDATIONS OF STRUCTURAL CAUSAL MODELS WITH CYCLES AND LATENT VARIABLES 

Supplementary Material

This Supplementary Material contains a summary of the basic terminology and results for causal graphical models (Appendix A), additional (unique) solvability properties (Appendix B), some results for linear SCMs (Appendix C), other examples (Appendix D), the proofs of all the theoretical results (Appendix E) and the measurable selection theorems (Appendix F) that are used in several proofs.

## APPENDIX A: CAUSAL GRAPHICAL MODELS

In this appendix, we provide a summary of the basic terminology and results for causal graphical models. In Appendix A. 1 we provide the terminology for directed (mixed) graphs. In Appendix A. 2 we give an introduction and an intuitive derivation of Markov properties for SCMs with cycles. In Appendix A. 3 we provide a definition of modular SCMs and show how they relate to SCMs. In Appendix A. 4 we provide an overview of the causal graphical models related to SCMs. The proofs of the theoretical results in this appendix are given in Appendix E.
A.1. Directed (mixed) graphs In this subsection, we introduce the terminology for directed (mixed) graphs, where we do allow for cycles [18, 34, 51, 60].

DEFINITION A. 1 (Directed (mixed) graph).

1. A directed graph is a pair $\mathcal{G}=(\mathcal{V}, \mathcal{E})$, where $\mathcal{V}$ is a set of nodes and $\mathcal{E}$ is a set of directed edges, which is a subset $\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$ of ordered pairs of nodes. Each element $(i, j) \in \mathcal{E}$ can be represented by the directed edge $i \rightarrow j$ or equivalently $j \leftarrow i$. In particular, $(i, i) \in \mathcal{E}$ represents a self-cycle $i \rightarrow i$.
2. A directed mixed graph is a triple $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$, where the pair $(\mathcal{V}, \mathcal{E})$ forms a directed graph and $\mathcal{B}$ is a set of bidirected edges, which is a subset $\mathcal{B} \subseteq\{\{i, j\}: i, j \in \mathcal{V}, i \neq j\}$ of unordered (distinct) pairs of nodes. Each element $\{i, j\} \in \mathcal{B}$ can be represented by the bidirected edge $i \leftrightarrow j$ or equivalently $j \leftrightarrow i$. Note that a directed graph can be considered as a directed mixed graph without bidirected edges.
3. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph. A directed mixed graph $\tilde{\mathcal{G}}=(\tilde{\mathcal{V}}, \tilde{\mathcal{E}}, \tilde{\mathcal{B}})$ is a subgraph of $\mathcal{G}$ if $\tilde{\mathcal{V}} \subseteq \mathcal{V}, \tilde{\mathcal{E}} \subseteq \mathcal{E}$ and $\tilde{\mathcal{B}} \subseteq \mathcal{B}$, in which case we write $\tilde{\mathcal{G}} \subseteq \mathcal{G}$. For a subset $\mathcal{W} \subseteq \mathcal{V}$, we define the induced subgraph of $\mathcal{G}$ on $\mathcal{W}$ by $\mathcal{G}_{\mathcal{W}}:=(\mathcal{W}, \tilde{\mathcal{E}}, \tilde{\mathcal{B}})$, where $\tilde{\mathcal{E}}$ and $\tilde{\mathcal{B}}$ are the set of directed and bidirected edges in $\mathcal{E}$ and $\mathcal{B}$, respectively, that lie in $\mathcal{W} \times \mathcal{W}$ and $\{\{i, j\}: i, j \in \mathcal{W}, i \neq j\}$, respectively.
4. A walk between $i, j \in \mathcal{V}$ in a directed mixed graph $\mathcal{G}$ is a tuple $\left(i_{0}, \epsilon_{1}, i_{1}, \epsilon_{2}, i_{2}, \ldots, \epsilon_{n}, i_{n}\right)$ of alternating nodes and edges in $\mathcal{G}$ for some $n \geq 0$, where all $i_{0}, \ldots, i_{n} \in \mathcal{V}$, all $\epsilon_{1}, \ldots, \epsilon_{n} \in \mathcal{E} \cup \mathcal{B}$ such that $\epsilon_{k} \in\left\{i_{k-1} \rightarrow i_{k}, i_{k-1} \leftarrow i_{k}, i_{k-1} \leftrightarrow i_{k}\right\}$ for all $k=1, \ldots, n$, and it starts with node $i_{0}=i$ and ends with node $i_{n}=j$. Note that $n=0$ corresponds with a trivial walk consisting of a single node. If all nodes $i_{0}, \ldots, i_{n}$ are distinct, it is called a path. A walk (path) of the form $i \rightarrow \cdots \rightarrow j$, that is, $\epsilon_{k}$ is $i_{k-1} \rightarrow i_{k}$ for all $k=1,2, \ldots, n$, is called a directed walk (path) from $i$ to $j$.

5. A cycle through $i \in \mathcal{V}$ in a directed mixed graph $\mathcal{G}$ is a directed path from $i$ to some node $j$ extended with the edge $j \rightarrow i \in \mathcal{E}$. In particular, a self-cycle $i \rightarrow i \in \mathcal{E}$ is a cycle. Note that a path cannot contain any cycles. A directed graph and a directed mixed graph are said to be acyclic if they contain no cycles, and are then referred to as a directed acyclic graph (DAG) and an acyclic directed mixed graph (ADMG), respectively.
6. For a directed mixed graph $\mathcal{G}$ and a node $i \in \mathcal{V}$ we define the set of parents of $i$ by $\mathrm{pa}_{\mathcal{G}}(i):=\{j \in \mathcal{V}: j \rightarrow i \in \mathcal{E}\}$, the set of children of $i$ by $\operatorname{ch}_{\mathcal{G}}(i):=\{j \in \mathcal{V}: i \rightarrow j \in \mathcal{E}\}$, the set of ancestors of $i$ by

$$
\operatorname{an}_{\mathcal{G}}(i):=\{j \in \mathcal{V}: \text { there is a directed path from } j \text { to } i \text { in } \mathcal{G}\}
$$

and the set of descendants of $i$ by

$$
\operatorname{de}_{\mathcal{G}}(i):=\{j \in \mathcal{V}: \text { there is a directed path from } i \text { to } j \text { in } \mathcal{G}\}
$$

Note that we have $\{i\} \cup \operatorname{pa}_{\mathcal{G}}(i) \subseteq \operatorname{an}_{\mathcal{G}}(i)$ and $\{i\} \cup \operatorname{ch}_{\mathcal{G}}(i) \subseteq \operatorname{de}_{\mathcal{G}}(i)$. We can apply all these definitions to subsets $\mathcal{U} \subseteq \mathcal{V}$ by taking unions, for example $\operatorname{pa}_{\mathcal{G}}(\mathcal{U}):=\cup_{i \in \mathcal{U}} \mathrm{pa}_{\mathcal{G}}(i)$. A subset $\mathcal{A} \subseteq \mathcal{V}$ is called an ancestral subset in $\mathcal{G}$ if $\mathcal{A}=\operatorname{an}_{\mathcal{G}}(\mathcal{A})$, that is, $\mathcal{A}$ is closed under taking ancestors of $\mathcal{A}$ in $\mathcal{G}$.
7. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph. We call $\mathcal{G}$ strongly connected if for every pair of distinct nodes $i, j \in \mathcal{V}$, the graph contains a cycle that passes through both $i$ and $j$. The strongly connected component of $i \in \mathcal{V}$, denoted by $\operatorname{sc}_{\mathcal{G}}(i)$, is the maximal subset $\mathcal{S} \subseteq \mathcal{V}$ such that $i \in \mathcal{S}$ and the induced subgraph $\mathcal{G}_{\mathcal{S}}$ is strongly connected. Equivalently, $\operatorname{sc}_{\mathcal{G}}(i)=\operatorname{an}_{\mathcal{G}}(i) \cap \operatorname{de}_{\mathcal{G}}(i)$.
8. A loop in a directed mixed graph $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ is a subset $\mathcal{O} \subseteq \mathcal{V}$ that is strongly connected in the induced subgraph $\mathcal{G}_{\mathcal{O}}$ of $\mathcal{G}$ on $\mathcal{O}$.
9. For a directed graph $\mathcal{G}=(\mathcal{V}, \mathcal{E})$, we define the graph of strongly connected components of $\mathcal{G}$ as the directed graph $\mathcal{G}^{\mathrm{sc}}:=\left(\mathcal{V}^{\mathrm{sc}}, \mathcal{E}^{\mathrm{sc}}\right)$, where $\mathcal{V}^{\mathrm{sc}}$ are the strongly connected components of $\mathcal{G}$, that is, $\mathcal{V}^{\mathrm{sc}}$ are the equivalence classes in $\mathcal{V} / \sim$ with the equivalence relation $i \sim j$ if and only if $i \in \operatorname{sc}_{\mathcal{G}}(j)$, and $\mathcal{E}^{\mathrm{sc}}=(\mathcal{E} \backslash\{i \rightarrow i: i \in \mathcal{V}\}) / \sim$ with the equivalence relation $(i \rightarrow j) \sim\left(i^{\prime} \rightarrow j^{\prime}\right)$ if and only if $i \sim i^{\prime}$ and $j \sim j^{\prime}$.

We omit the subscript $\mathcal{G}$ whenever it is clear which directed (mixed) graph $\mathcal{G}$ we are referring to.

LEMMA A. 2 (DAG of strongly connected components). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ be a directed graph. Then $\mathcal{G}^{\text {sc }}$, the graph of strongly connected components of $\mathcal{G}$, is a DAG.
A.2. Markov properties In this subsection, we give a short overview of Markov properties for SCMs with cycles. We will make use of the Markov properties that were recently developed by Forré and Mooij [18] for HEDGes, a graphical representation that is similar to the augmented graph of SCMs. We briefly summarize some of their main results and apply them to the class of SCMs. We also provide a shorter and more intuitive derivation so that this subsection can act as an entry point for the reader into the more extensive discussion of Markov properties provided in [18].

Markov properties associate a set of conditional independence relations to a graph. The directed global Markov property for directed acyclic graphs, also known as the $d$-separation criterion [50], is one of the most widely used. It directly extends to a similar property for acyclic directed mixed graphs (ADMGs) [60]. It does not hold in general for cyclic SCMs, however, as was already observed earlier [71, 72]. Under some conditions (roughly speaking, linearity or discrete variables) the directed global Markov property can be shown to hold also in the presence of cycles [18].

Inspired by work of Spirtes [71], Forré and Mooij [18] recognized that in the general cyclic case a different extension of $d$-separation, termed $\sigma$-separation, is needed, leading to the general directed global Markov property. One key result in [18] implies that under the assumption of unique solvability w.r.t. each strongly connected component of its graph, the observational distribution of an SCM satisfies the general directed global Markov property w.r.t. its graph. The solvability assumptions are in general not preserved under interventions. Under the stronger assumption of simplicity, however, they are, and one obtains the corollary that also all interventional and counterfactual distributions of a simple SCM satisfy the general directed global Markov property w.r.t. to their corresponding graphs.

For a more extensive study of different Markov properties that can be associated to SCMs we refer the reader to [18].
A.2.1. The directed global Markov property Conditional independencies in the observational distribution of an acyclic SCM can be read off from its graph by using the graphical criterion called $d$-separation [51]. The directed global Markov property associates a conditional independence relation in the observational distribution of the SCM to each $d$-separation entailed by the graph. Here, we use a formulation of $d$-separation that generalizes $d$-separation for DAGs [50] and $m$-separation for ADMGs [60] and mDAGs [15].

Definition A. 3 (Collider). Let $\pi=\left(i_{0}, \epsilon_{1}, i_{1}, \epsilon_{2}, i_{2}, \ldots, \epsilon_{n}, i_{n}\right)$ be a walk (path) in a directed mixed graph $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$. A node $i_{k}$ on $\pi$ is called a collider on $\pi$ if it is a non-endpoint node $(1 \leq k<n)$ and the two edges $\epsilon_{k}, \epsilon_{k+1}$ meet head-to-head on $i_{k}$ (i.e., if the subwalk $\left(i_{k-1}, \epsilon_{k}, i_{k}, \epsilon_{k+1}, i_{k+1}\right)$ is of the form $i_{k-1} \rightarrow i_{k} \leftarrow i_{k+1}, i_{k-1} \leftrightarrow i_{k} \leftarrow i_{k+1}$, $i_{k-1} \rightarrow i_{k} \leftrightarrow i_{k+1}$ or $i_{k-1} \leftrightarrow i_{k} \leftrightarrow i_{k+1}$ ). The node $i_{k}$ is called a non-collider on $\pi$ otherwise, that is, if it is an endpoint node $(k=0$ or $k=n)$ or if the subwalk $\left(i_{k-1}, \epsilon_{k}, i_{k}, \epsilon_{k+1}, i_{k+1}\right)$ is of the form $i_{k-1} \rightarrow i_{k} \rightarrow i_{k+1}, i_{k-1} \leftarrow i_{k} \leftarrow i_{k+1}, i_{k-1} \leftarrow i_{k} \rightarrow i_{k+1}, i_{k-1} \leftrightarrow i_{k} \rightarrow i_{k+1}$ or $i_{k-1} \leftarrow i_{k} \leftrightarrow i_{k+1}$.

Note in particular that the end points of a walk are non-colliders on the walk.
DEFINITION A. 4 (d-separation). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and let $C \subseteq \mathcal{V}$ be a subset of nodes. A walk (path) $\pi=\left(i_{0}, \epsilon_{1}, i_{1}, \ldots, i_{n}\right)$ in $\mathcal{G}$ is said to be $C$-dblocked or $d$-blocked by $C$ if

1. it contains a collider $i_{k} \notin \operatorname{an}_{\mathcal{G}}(C)$, or
2. it contains a non-collider $i_{k} \in C$.

The walk (path) $\pi$ is said to be $C$-d-open if it is not d-blocked by $C$. For two subsets of nodes $A, B \subseteq \mathcal{V}$, we say that $A$ is $d$-separated from $B$ given $C$ in $\mathcal{G}$ if all paths between any node in $A$ and any node in $B$ are d-blocked by $C$, and write

$$
A \underset{\mathcal{G}}{\stackrel{d}{\mathcal{L}}} B \mid C
$$

The next lemma is a straightforward generalization of Lemma 3.3 in [22] to the cyclic setting. It implies that it suffices to formulate $d$-separation in terms of paths rather than walks.

LEMMA A.5. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph, $C \subseteq \mathcal{V}$ and $i, j \in \mathcal{V}$. There exists a $C$-d-open walk between $i$ and $j$ in $\mathcal{G}$ if and only if there exists a $C$-d-open path between $i$ and $j$ in $\mathcal{G}$.

![img-5.jpeg](img-5.jpeg)

Fig 5: The graphs of the observationally equivalent SCMs $\mathcal{M}$ (left) and $\overline{\mathcal{M}}$ (right) of Example A. 8 and A.10.
DEFINITION A. 6 (Directed global Markov property). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathbb{P}_{\mathcal{V}}$ a probability distribution on $\boldsymbol{X}_{\mathcal{V}}=\prod_{i \in \mathcal{V}} \mathcal{X}_{i}$, where each $\mathcal{X}_{i}$ is a standard probability space. The probability distribution $\mathbb{P}_{\mathcal{V}}$ satisfies the directed global Markov property relative to $\mathcal{G}$ if for all subsets $A, B, C \subseteq \mathcal{V}$ we have

$$
A \underset{\mathcal{G}}{\stackrel{d}{\mathcal{G}}} B \mid C \quad \Longrightarrow \quad \boldsymbol{X}_{A} \underset{\mathbb{P}_{\mathcal{V}}}{\mathbb{1}} \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}
$$

that is, $\left(X_{i}\right)_{i \in A}$ and $\left(X_{i}\right)_{i \in B}$ are conditionally independent given $\left(X_{i}\right)_{i \in C}$ under $\mathbb{P}_{\mathcal{V}}$, where we take the canonical projections $X_{i}: \boldsymbol{X}_{\mathcal{V}} \rightarrow \mathcal{X}_{i}$ as random variables.

From the results in [18] it directly follows that for the observational distribution of an SCM, the directed global Markov property w.r.t. the graph of the SCM (also known as the $d$-separation criterion), holds under one of the following assumptions.

THEOREM A. 7 (Directed global Markov property for SCMs [18]). Let $\mathcal{M}$ be a uniquely solvable SCM that satisfies at least one of the following three conditions:

1. $\mathcal{M}$ is acyclic;
2. all endogenous spaces $\mathcal{X}_{i}$ are discrete and $\mathcal{M}$ is ancestrally uniquely solvable;
3. $\mathcal{M}$ is linear (see Definition C.1), each of its causal mechanisms $\left\{f_{i}\right\}_{i \in \mathcal{I}}$ has a nontrivial dependence on at least one exogenous variable, and $\mathbb{P}_{\mathcal{E}}$ has a density w.r.t. the Lebesgue measure on $\mathbb{R}^{\mathcal{J}}$.

Then its observational distribution $\mathbb{P}^{\boldsymbol{X}}$ exists, is unique and satisfies the directed global Markov property relative to $\mathcal{G}(\mathcal{M})$ (see Definition A.6).

The acyclic case is well known and was first shown in the context of linear-Gaussian structural equation models [32, 75]. The discrete case fixes the erroneous theorem by Pearl and Dechter [52], for which a counterexample was found by Neal [49], by adding the ancestral unique solvability condition, and extends it to allow for bidirected edges in the graph. The linear case is an extension of existing results for the linear-Gaussian setting without bidirected edges $[31,71,72]$ to a linear (possibly non-Gaussian) setting with bidirected edges in the graph.

The following counterexample of an SCM for which the directed global Markov property does not hold was already given in [71, 72].

Example A. 8 (Directed global Markov property does not hold for cyclic SCM). Consider the SCM $\mathcal{M}=\left\langle\mathbf{4}, \mathbf{4}, \mathbb{R}^{4}, \mathbb{R}^{4}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}^{4}}\right\rangle$ with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad f_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{2}, \quad f_{3}(\boldsymbol{x}, \boldsymbol{e})=x_{1} x_{4}+e_{3}, \quad f_{4}(\boldsymbol{x}, \boldsymbol{e})=x_{2} x_{3}+e_{4}
$$

and $\mathbb{P}_{\mathbb{R}^{4}}$ is the standard-normal distribution on $\mathbb{R}^{4}$. The graph of $\mathcal{M}$ is depicted in Figure 5 on the left. The model is uniquely solvable (it is even simple). One can check that for every solution $\boldsymbol{X}$ of $\mathcal{M}, X_{1}$ is not independent of $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$. However, the variables $X_{1}$ and $X_{2}$ are d-separated given $\left\{X_{3}, X_{4}\right\}$ in $\mathcal{G}(\mathcal{M})$. Hence the global directed Markov property does not hold here.

In constraint-based approaches to causal discovery, one usually assumes the converse of the directed global Markov property to hold [51, 73].

Definition A. 9 (d-Faithfulness). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathbb{P}_{\mathcal{V}}$ a probability distribution on $\boldsymbol{\mathcal { X } _ { \mathcal { V } }}=\prod_{i \in \mathcal{V}} \mathcal{X}_{i}$, where each $\mathcal{X}_{i}$ is a standard probability space. The probability distribution $\mathbb{P}_{\mathcal{V}}$ is $d$-faithful to $\mathcal{G}$ if for all subsets $A, B, C \subseteq \mathcal{V}$ we have

$$
A \underset{\mathcal{G}}{\stackrel{d}{\downarrow}} B \mid C \quad \Longleftarrow \quad \boldsymbol{X}_{A} \underset{\mathbb{P}_{\mathcal{V}}}{\stackrel{\natural}{\downarrow}} \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}
$$

where we take the canonical projections $X_{i}: \boldsymbol{\mathcal { X } _ { \mathcal { V } }} \rightarrow \mathcal{X}_{i}$ as random variables.
In other words, the $d$-faithfulness assumption states that the graph explains, via $d$ separation, all the conditional independencies that are present in the observational distribution. Meek [41] showed that for multinomial and linear-Gaussian DAG (i.e., acyclic and causally sufficient SCMs) models, $d$-faithfulness holds for all parameter values up to a measure zero set (in a natural parameterization). Up to our knowledge no such results have been shown in more general parametric or nonparametric settings (neither in the acyclic case, nor in the cyclic one).
A.2.2. The general directed global Markov property In [18] the general directed global Markov property is introduced, that is based on $\sigma$-separation, an extension of $d$-separation. This notion of $\sigma$-separation was derived from the notion of $d$-separation in the acyclification of the graph. The acyclification of a graph generalizes the idea of the collapsed graph for directed graphs, developed by Spirtes [71], to HEDGes. In particular, this notion can be applied to directed mixed graphs, and thus to the graphs of SCMs. The main idea of the acyclification is that under the condition that the SCM is uniquely solvable w.r.t. each strongly connected component, we can replace the causal mechanisms of these strongly connected components by their measurable solution functions, which results in an acyclic SCM. This acyclification preserves the solutions, and $d$-separation in the acyclification can directly be translated into $\sigma$-separation in the original graph. This then leads to the general directed global Markov property. We will discuss this now in more detail.

EXAMPLE A. 10 (Construction of an observationally equivalent acyclic SCM). Consider the SCM $\mathcal{M}$ of Example A. 8 which is uniquely solvable w.r.t. all its strongly connected components, i.e., the subsets $\{1\},\{2\}$ and $\{3,4\}$. Replacing the causal mechanisms of these strongly connected components by their measurable solution functions gives the SCM $\overline{\mathcal{M}}$ that is the same as $\mathcal{M}$ except that its causal mechanism $\boldsymbol{f}$ is given by

$$
\tilde{f}_{1}(\boldsymbol{x}, \boldsymbol{e}):=e_{1}, \quad \tilde{f}_{2}(\boldsymbol{x}, \boldsymbol{e}):=e_{2}, \quad \tilde{f}_{3}(\boldsymbol{x}, \boldsymbol{e}):=\frac{x_{1} e_{4}+e_{3}}{1-x_{1} x_{2}}, \quad \tilde{f}_{4}(\boldsymbol{x}, \boldsymbol{e}):=\frac{x_{2} e_{3}+e_{4}}{1-x_{1} x_{2}}
$$

By construction, $\mathcal{M}$ and $\overline{\mathcal{M}}$ are observationally equivalent. Because $\overline{\mathcal{M}}$ is acyclic (see Figure 5 on the right) we can apply the directed global Markov property to $\overline{\mathcal{M}}$. The fact that $X_{1}$ and $X_{2}$ are not d-separated given $\left\{X_{3}, X_{4}\right\}$ in $\mathcal{G}(\overline{\mathcal{M}})$ is in line with $X_{1}$ being dependent of $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$ for every solution $\boldsymbol{X}$ of $\overline{\mathcal{M}}$ (and hence of $\mathcal{M}$ ).

One of the key insights in [18] is that this example can easily be generalized as follows.
DEfinition A. 11 (Acyclification of an SCM). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an SCM that is uniquely solvable w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$. For each $i \in \mathcal{I}$, let $g_{i}$ be the $i^{\text {th }}$ component of a measurable solution function $\boldsymbol{g}_{\mathrm{sc}(i)}: \boldsymbol{\mathcal { X } _ { \mathrm { pa } ( s ( ( ) ) \backslash \mathrm { sc } ( i ) } \times}$ $\mathcal{E}_{\mathrm{pa}(\mathrm{sc}(i))} \rightarrow \boldsymbol{\mathcal { X } _ { \mathrm { sc } ( i ) }}$ of $\mathcal{M}$ w.r.t. $\mathrm{sc}(i)$, where pa and sc denote the parents and strongly

![img-6.jpeg](img-6.jpeg)

Fig 6: The graphs of the original SCM $\mathcal{M}$ (left), of the acyclified SCM (center), and of the acyclification of the graph of $\mathcal{M}$ (right) corresponding to Example A.15.
connected components according to $\mathcal{G}^{a}(\mathcal{M})$, respectively. We call the SCM $\mathcal{M}^{\mathrm{acy}}:=$ $\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { E }}, \check{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$ with the acyclified causal mechanism $\check{\boldsymbol{f}}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}$ given by

$$
\check{f}_{i}(\boldsymbol{x}, \boldsymbol{e})=g_{i}\left(\boldsymbol{x}_{\mathrm{pa}(\mathrm{sc}(i)) \backslash \mathrm{sc}(i)}, \boldsymbol{e}_{\mathrm{pa}(\mathrm{sc}(i))}\right), \quad i \in \mathcal{I}
$$

an acyclification of $\mathcal{M}$. We denote by $\operatorname{acy}(\mathcal{M})$ the equivalence class of the acyclifications of $\mathcal{M}$.

Note that $\operatorname{acy}(\mathcal{M})$ is well-defined: all acyclifications of an SCM $\mathcal{M}$ belong to the same equivalence class of SCMs.

Proposition A.12. Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$. Then an acyclification $\mathcal{M}^{\text {acy }}$ of $\mathcal{M}$ is acyclic and observationally equivalent to $\mathcal{M}$.

We can also define a graphical acyclification for directed mixed graphs, which is a special case of the operation defined in [18] for HEDGes.

DEFINITION A. 13 (Acyclification of a directed mixed graph). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph. The acyclification of $\mathcal{G}$ maps $\mathcal{G}$ to the acyclified graph $\mathcal{G}^{\text {acy }}:=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ with directed edges $j \rightarrow i \in \mathcal{E}$ if and only if $j \in \mathrm{pa}_{\mathcal{G}}\left(\mathrm{sc}_{\mathcal{G}}(i)\right) \backslash \mathrm{sc}_{\mathcal{G}}(i)$ and bidirected edges $i \leftrightarrow j \in \mathcal{B}$ if and only if there exist $i^{\prime} \in \operatorname{sc}_{\mathcal{G}}(i)$ and $j^{\prime} \in \operatorname{sc}_{\mathcal{G}}(j)$ with $i^{\prime}=j^{\prime}$ or $i^{\prime} \leftrightarrow j^{\prime} \in \mathcal{B}$.

The following compatibility result is immediate from the definitions.
Proposition A.14. Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$. Then $\mathcal{G}^{a}(\operatorname{acy}(\mathcal{M})) \subseteq \operatorname{acy}\left(\mathcal{G}^{a}(\mathcal{M})\right)$ and $\mathcal{G}(\operatorname{acy}(\mathcal{M})) \subseteq$ $\operatorname{acy}(\mathcal{G}(\mathcal{M}))$.

The following example illustrates that the graph of the acyclification of an SCM can be a strict subgraph of the acyclification of the graph of the SCM.

Example A. 15 (Graph of the acyclification of the SCM is a strict subgraph of the acyclification of its graph). Consider the SCM $\mathcal{M}=\left\langle\mathbf{2}, \mathbf{1}, \mathbb{R}^{2}, \mathbb{R}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}}\right\rangle$ with the causal mechanism defined by

$$
f_{1}(\boldsymbol{x}, e)=x_{2}-e, \quad f_{2}(\boldsymbol{x}, e)=\frac{1}{2} x_{1}+e
$$

and $\mathbb{P}_{\mathbb{R}}$ the standard Gaussian measure on $\mathbb{R}$. The SCM $\mathcal{M}$ is uniquely solvable w.r.t. the (only) strongly connected component $\{1,2\}$. An acyclification of $\mathcal{M}$ is the acyclified SCM $\mathcal{M}^{\text {acy }}$ with the acyclified causal mechanism $\check{f}$ defined by

$$
\check{f}_{1}(\boldsymbol{x}, e)=0, \quad \check{f}_{2}(\boldsymbol{x}, e)=e
$$

The graph $\mathcal{G}(\operatorname{acy}(\mathcal{M}))$ is a strict subgraph of $\operatorname{acy}(\mathcal{G}(\mathcal{M}))$ as can be seen in Figure 6.
Translating the notion of $d$-separation from the acyclified graph back to the original graph led to the notion of $\sigma$-separation.

DEFINITION A. 16 ( $\sigma$-separation [18]). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and let $C \subseteq \mathcal{V}$ be a subset of nodes. A walk (path) $\pi=\left(i_{0}, \epsilon_{1}, i_{1}, \ldots, i_{n}\right)$ in $\mathcal{G}$ is said to be $C$ - $\sigma$ blocked or $\sigma$-blocked by $C$ if

1. its first node $i_{0} \in C$ or its last node $i_{n} \in C$, or
2. it contains a collider $i_{k} \notin \operatorname{an}_{\mathcal{G}}(C)$, or
3. it contains a non-endpoint non-collider $i_{k} \in C$ that points towards a neighboring node on $\pi$ that lies in a different strongly connected component of $\mathcal{G}$, that is, such that $i_{k-1} \leftarrow i_{k}$ in $\pi$ and $i_{k-1} \notin \operatorname{sc}_{\mathcal{G}}\left(i_{k}\right)$, or $i_{k} \rightarrow i_{k+1}$ in $\pi$ and $i_{k+1} \notin \operatorname{sc}_{\mathcal{G}}\left(i_{k}\right)$.
The walk (path) $\pi$ is said to be $C$ - $\sigma$-open if it is not $\sigma$-blocked by $C$. For two subsets of nodes $A, B \subseteq \mathcal{V}$, we say that $A$ is $\sigma$-separated from $B$ given $C$ in $\mathcal{G}$ if all paths between any node in $A$ and any node in $B$ are $\sigma$-blocked by $C$, and write

$$
A \underset{\mathcal{G}}{\sigma} B \mid C
$$

The only difference between $\sigma$-separation and $d$-separation is that $d$-separation does not have the extra condition on the non-collider that it has to point to a node in a different strongly connected component. It is therefore obvious that $\sigma$-separation reduces to $d$-separation for acyclic graphs, since $\operatorname{sc}_{\mathcal{G}}(i)=\{i\}$ for each $i \in \mathcal{V}$ in that case.

Although for proofs it is often easier to make use of walks, it suffices to formulate $\sigma$ separation in term of paths rather than walks because of the following result, which is analogous to a similar result for $d$-separation (see Lemma A.5).

LEMMA A.17. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph, $C \subseteq \mathcal{V}$ and $i, j \in \mathcal{V}$. There exists a $C$ - $\sigma$-open walk between $i$ and $j$ in $\mathcal{G}$ if and only if there exists a $C$ - $\sigma$-open path between $i$ and $j$ in $\mathcal{G}$.

It is clear from the definitions that $\sigma$-separation implies $d$-separation. The other way around does not hold in general, as can be seen in the following example.

Example A. 18 ( $d$-separation does not imply $\sigma$-separation). Consider the directed graph $\mathcal{G}$ as depicted in Figure 5 (left). Here $X_{1}$ is d-separated from $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$, but $X_{1}$ is not $\sigma$-separated from $X_{2}$ given $\left\{X_{3}, X_{4}\right\}$.

The following result in [18] relates $\sigma$-separation to $d$-separation.
Proposition A.19. Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph. Then for $A, B, C \subseteq$ $\mathcal{V}$,

$$
A \underset{\mathcal{G}}{\sigma} B \mid C \Longleftrightarrow A \underset{\operatorname{acy}(\mathcal{G})}{d} B \mid C
$$

By replacing in Definition A. 6 " $d$-separation" by " $\sigma$-separation", one obtains the formulation of what Forré and Mooij [18] termed the general directed global Markov property.

DEFINITION A. 20 (General directed global Markov property [18]). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathbb{P}_{\mathcal{V}}$ a probability distribution on $\boldsymbol{X}_{\mathcal{V}}=\prod_{i \in \mathcal{V}} \mathcal{X}_{i}$, where each $\mathcal{X}_{i}$ is a standard probability space. The probability distribution $\mathbb{P}_{\mathcal{V}}$ satisfies the general directed global Markov property relative to $\mathcal{G}$ if for all subsets $A, B, C \subseteq \mathcal{V}$ we have

$$
A \underset{\mathcal{G}}{\stackrel{\sigma}{\mathcal{G}}} B \mid C \quad \Longrightarrow \quad \boldsymbol{X}_{A} \underset{\mathbb{P}_{\mathcal{V}}}{\mathbb{1}} \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}
$$

that is, $\left(X_{i}\right)_{i \in A}$ and $\left(X_{i}\right)_{i \in B}$ are conditionally independent given $\left(X_{i}\right)_{i \in C}$ under $\mathbb{P}_{\mathcal{V}}$, where we take the canonical projections $X_{i}: \boldsymbol{\mathcal { X }}_{\mathcal{V}} \rightarrow \mathcal{X}_{i}$ as random variables.

The fact that $\sigma$-separation implies $d$-separation means that the directed global Markov property implies the general directed global Markov property. In other words, the general directed global Markov property is weaker than the directed global Markov property. It is actually strictly weaker, as we saw in Example A.18.

The following fundamental result, also known as the $\sigma$-separation criterion, follows directly from the theory in [18].

THEOREM A. 21 (General directed global Markov property for SCMs). Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$. Then its observational distribution $\mathbb{P}^{\boldsymbol{X}}$ exists, is unique and it satisfies the general directed global Markov property relative to $\mathcal{G}(\mathcal{M}) .{ }^{15}$

The proof is based on the reasoning that, for $A, B, C \subseteq \mathcal{I}$, if $A$ is $\sigma$-separated from $B$ given $C$ in $\mathcal{G}(\mathcal{M})$, then $A$ is $d$-separated from $B$ by $C$ in $\operatorname{acy}(\mathcal{G}(\mathcal{M}))$ and hence in $\mathcal{G}(\operatorname{acy}(\mathcal{M}))$, and since $\operatorname{acy}(\mathcal{M})$ is acyclic and observationally equivalent to $\mathcal{M}$, it follows from the directed global Markov property applied to $\operatorname{acy}(\mathcal{M})$ that $\boldsymbol{X}_{A} \Perp_{\mathbb{P}} \times \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}$ for every solution $\boldsymbol{X}$ of $\mathcal{M}$. Note that the ancestral unique solvability condition for the discrete case is strictly weaker than the condition of unique solvability w.r.t. each strongly connected component in Theorem A.21. For the linear case, the condition of unique solvability is equivalent to the condition of unique solvability w.r.t. each strongly connected component (see Proposition C.4).

The results in Theorems A. 7 and A. 21 are not preserved under perfect intervention, because intervening on a strongly connected component could split it into several strongly connected components with different solvability properties. As the class of simple SCMs is preserved under perfect intervention and the twin operation (Proposition 8.2), we obtain the following corollary.

COROLLARY A. 22 (Global Markov properties for simple SCMs). Let $\mathcal{M}$ be a simple SCM. Then the:

1. observational distribution,
2. interventional distribution after perfect intervention on $I \subset \mathcal{I}$,
3. counterfactual distribution after perfect intervention on $\tilde{I} \subseteq \mathcal{I} \cup \mathcal{I}^{\prime}$,
all exist, are unique and satisfy the general directed global Markov property relative to $\mathcal{G}(\mathcal{M}), \operatorname{do}(I)(\mathcal{G}(\mathcal{M}))$ and $\operatorname{do}(\tilde{I})(\operatorname{twin}(\mathcal{G}(\mathcal{M})))$, respectively. Moreover, if $\mathcal{M}$ satisfies at least one of the three conditions (1), (2), (3) of Theorem A.7, then they also satisfies the directed global Markov property relative to $\mathcal{G}(\mathcal{M}), \operatorname{do}(I)(\mathcal{G}(\mathcal{M}))$ and $\operatorname{do}(\tilde{I})(\operatorname{twin}(\mathcal{G}(\mathcal{M})))$, respectively.

Similar to $d$-faithfulness, $\sigma$-faithfulness ${ }^{16}$ is defined as follows.

[^0]
[^0]:    ${ }^{15}$ Since [18] also provides results under the weaker condition that an SCM is solvable (not necessarily uniquely) w.r.t. each strongly connected component of $\mathcal{G}(\mathcal{M})$, one might believe that Theorem A. 21 could be generalized to stating that in that case, any of its observational distributions satisfies the general directed global Markov property. However, that is not true: consider for example the SCM $\mathcal{M}=\left\langle\mathbf{2}, \emptyset, \mathbb{R}^{2}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ with $f_{1}(\boldsymbol{x})=x_{1}$ and $f_{2}(\boldsymbol{x})=x_{2}$. Then $\mathcal{M}$ is solvable w.r.t. each of its strongly connected components $\{1\}$ and $\{2\}$. The solution with $X_{1}=X_{2}$ shows a dependence between $X_{1}$ and $X_{2}$ and thus $X_{1} \Perp X_{2}$ does not hold. In general, all strongly connected components that admit multiple solutions may be dependent on any other variable(s) in the model.
    ${ }^{16}$ In [63] it is called "collapsed graph faithfulness".

DEFINITION A. 23 ( $\sigma$-Faithfulness). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{B})$ be a directed mixed graph and $\mathbb{P}_{\mathcal{V}}$ a probability distribution on $\boldsymbol{\mathcal { X } _ { \mathcal { V } }}=\prod_{i \in \mathcal{V}} \mathcal{X}_{i}$, where each $\mathcal{X}_{i}$ is a standard probability space. The probability distribution $\mathbb{P}_{\mathcal{V}}$ is $\sigma$-faithful to $\mathcal{G}$ if for all subsets $A, B, C \subseteq \mathcal{V}$ we have

$$
A \underset{\mathcal{G}}{\stackrel{\sigma}{\mathcal{G}}} B \mid C \quad \Longleftarrow \quad \boldsymbol{X}_{A} \underset{\mathbb{P}_{\mathcal{V}}}{\mathbb{1}} \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}
$$

where we take the canonical projections $X_{i}: \boldsymbol{\mathcal { X } _ { \mathcal { V } }} \rightarrow \mathcal{X}_{i}$ as random variables.
In other words, the graph explains, via $\sigma$-separation, all the conditional independencies that are present in the observational distribution. Although it has been conjectured [72] that under certain conditions $\sigma$-faithfulness should hold, formulating and proving such completeness results is an open problem to the best of our knowledge.
A.3. Modular SCMs In this subsection, we relate the class of (simple) SCMs to that of modular SCMs. Modular SCMs introduced by Forré and Mooij [18] are causal graphical models on which marginalizations and interventions are defined and they satisfy the general directed global Markov property. For a comprehensive account on modular SCMs we refer the reader to [18].
A.3.1. Definition of a modular SCM In contrast to an SCM from which a graph can be derived, a modular SCM is defined in terms of a graphical object, which Forré and Mooij [18] call a directed graph with hyperedges (HEDG). The hyperedges of a HEDG are described in terms of a simplicial complex.

DEFINITION A. 24 (Simplicial complex). Let $\mathcal{V}$ be a finite set. A simplicial complex $\mathcal{H}$ over $\mathcal{V}$ is a set of subsets of $\mathcal{V}$ such that

1. all single element sets $\{v\}$ are in $\mathcal{H}$ for $v \in \mathcal{V}$, and
2. if $\mathcal{F} \in \mathcal{H}$, then also all subsets $\overline{\mathcal{F}} \subseteq F$ are elements of $\mathcal{H}$.

DEFINITION A. 25 (Directed graph with hyperedges (HEDGes) [18]). A directed graph with hyperedges (HEDG) is a triple $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{H})$, where $(\mathcal{V}, \mathcal{E})$ is a directed graph and $\mathcal{H}$ a simplicial complex over the set of nodes $\mathcal{V}$. The elements $\mathcal{F}$ of $\mathcal{H}$ are called hyperedges of $\mathcal{G}$. The elements $\mathcal{F}$ of $\mathcal{H}$ that are inclusion-maximal elements of $\mathcal{H}$ are called maximal hyperedges and are denoted by $\overline{\mathcal{H}}$.

A HEDG $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{H})$ can be represented as a directed graph $\overline{\mathcal{G}}:=(\mathcal{V}, \mathcal{E})$ consisting of nodes $\mathcal{V}$ and directed edges $\mathcal{E}$, with additional maximal hyperedges $\mathcal{F} \in \overline{\mathcal{H}}$ with $|\mathcal{F}| \geq 2$ (i.e., not corresponding to single element sets $\{v\} \in \overline{\mathcal{H}}$ ), that point to their target nodes $v \in \mathcal{F}$. For a HEDG $\mathcal{G}$, we define $\mathrm{pa}_{\mathcal{G}}, \mathrm{ch}_{\mathcal{G}}$, etc., in terms of the underlying directed graph $\overline{\mathcal{G}}$, that is, $\mathrm{pa}_{\overline{\mathcal{G}}}, \mathrm{ch}_{\overline{\mathcal{G}}}$, etc., respectively.

A loop in a HEDG $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{H})$ is a subset $\mathcal{O} \subseteq \mathcal{V}$ that is a loop in the underlying directed graph $\overline{\mathcal{G}}=(\mathcal{V}, \mathcal{E})$. In other words, a loop of $\mathcal{G}$ is a set of nodes $\mathcal{O} \subseteq \mathcal{V}$ such that for every two nodes $v, w \in \mathcal{O}$ there are directed paths $v \rightarrow \cdots \rightarrow w$ and $w \rightarrow \cdots \rightarrow v$ in $\mathcal{G}$ for which all the intermediate nodes lie in $\mathcal{O}$ (if any exist). In particular, a loop may consist of a single element $\{v\}$ for $v \in \mathcal{V}$. The set of loops in $\mathcal{G}$ is denoted by $\mathcal{L}(\mathcal{G})$.

In order to define a modular SCM one needs the notion of a compatible system of solution functions, which assigns to each loop a separate solution function such that all these solution functions are "compatible" with each other.

Definition A. 26 (Compatible system of solution functions ${ }^{17}$ ). Let $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{H})$ be a HEDG. For every $v \in \mathcal{V}$ and maximal hyperedge $\mathcal{F}$ in $\mathcal{H}$, let $\mathcal{X}_{v}$ and $\mathcal{E}_{\mathcal{F}}$ be standard measurable spaces. For a subset $\mathcal{O} \subseteq \mathcal{V}$ we define ${ }^{18}$

$$
\boldsymbol{X}_{\mathcal{O}}:=\prod_{v \in \mathcal{O}} \mathcal{X}_{v} \quad \text { and } \quad \widetilde{\mathcal{E}}_{\mathcal{O}}:=\prod_{\substack{\mathcal{F} \in \mathcal{H} \\ \mathcal{F} \cap \mathcal{O} \neq \emptyset}} \mathcal{E}_{\mathcal{F}}
$$

Consider a family of measurable mappings $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}$ indexed by $\mathcal{L}(\mathcal{G})$ which are of the form

$$
\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{X}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}} \times \widetilde{\mathcal{E}}_{\mathcal{O}} \rightarrow \boldsymbol{X}_{\mathcal{O}}
$$

We call the family of measurable mappings $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}$ a compatible system of solution functions, if for all $\mathcal{O}, \mathcal{O} \in \mathcal{L}(\mathcal{G})$ with $\mathcal{O} \subseteq \mathcal{O}$ and for all $\widetilde{\boldsymbol{e}}_{\mathcal{O}} \in \widetilde{\mathcal{E}}_{\mathcal{O}}$ and $\boldsymbol{x}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}} \in$ $\boldsymbol{X}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}}$ we have

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}}, \widetilde{\boldsymbol{e}}_{\mathcal{O}}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}}, \widetilde{\boldsymbol{e}}_{\mathcal{O}}\right)
$$

This structure of a compatible system of solution functions is at the heart of the defnition of a modular SCM.

Definition A. 27 (Modular structural causal model (mSCM) [18]). A modular structural causal model (mSCM) is a tuple

$$
\widehat{\mathcal{M}}:=\left\langle\mathcal{G}, \boldsymbol{X}, \mathcal{E},\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}, \mathbb{P}_{\mathcal{E}}\right\rangle
$$

where

1. $\mathcal{G}=(\mathcal{V}, \mathcal{E}, \mathcal{H})$ is a $H E D G$,
2. $\mathcal{X}=\prod_{v \in \mathcal{V}} \mathcal{X}_{v}$ is the product of standard measurable spaces $\mathcal{X}_{v}$,
3. $\mathcal{E}=\prod_{\mathcal{F} \in \mathcal{H}} \mathcal{E}_{\mathcal{F}}$ is the product of standard measurable spaces $\mathcal{E}_{\mathcal{F}}$,
4. $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}$ is a compatible system of solution functions,
5. $\mathbb{P}_{\mathcal{E}}=\prod_{\mathcal{F} \in \mathcal{H}} \mathbb{P}_{\mathcal{E}_{\mathcal{F}}}$ is a product measure, where $\mathbb{P}_{\mathcal{E}_{\mathcal{F}}}$ is a probability measure on $\mathcal{E}_{\mathcal{F}}$ for each $\mathcal{F} \in \mathcal{H}$.

Let $\widehat{\mathcal{M}}=\left\langle\mathcal{G}, \boldsymbol{X}, \mathcal{E},\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be a modular SCM and $\mathcal{O}_{1}, \ldots, \mathcal{O}_{r} \in \mathcal{L}(\mathcal{G})$ the strongly connected components of $\mathcal{G}$ ordered according to a topological order of the DAG of strongly connected components of $\mathcal{G}$. Then for any random variable $\boldsymbol{E}: \Omega \rightarrow \boldsymbol{\mathcal { E }}$ such that $\mathbb{P}^{\boldsymbol{E}}=\mathbb{P}_{\mathcal{E}}$ one can inductively define the random variables $X_{v}:=\left(\boldsymbol{g}_{\mathcal{O}_{i}}\right)_{v}\left(\boldsymbol{X}_{\mathrm{pa}_{\mathcal{G}}\left(\mathcal{O}_{i}\right) \backslash \mathcal{O}_{i}}, \widetilde{\boldsymbol{E}}_{\mathcal{O}_{i}}\right)$ for all $v \in \mathcal{O}_{i}$ for all $i \geq 1$, starting at $X_{v}:=\left(\boldsymbol{g}_{\mathcal{O}_{i}}\right)_{v}\left(\widetilde{\boldsymbol{E}}_{\mathcal{O}_{i}}\right)$ for all $v \in \mathcal{O}_{1}$. Because $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}$ is a compatible system of solution functions, we have for every $\mathcal{O} \in \mathcal{L}(\mathcal{G})$

$$
\boldsymbol{X}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{X}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}}, \widetilde{\boldsymbol{E}}_{\mathcal{O}}\right)
$$

We call the random variable $\boldsymbol{X}$ a solution of the modular SCM $\widehat{\mathcal{M}}$. Note that the solution $\boldsymbol{X}$ depends on the choice of the random variable $\boldsymbol{E}: \Omega \rightarrow \mathcal{E}$.

The causal semantics of modular SCMs can be defined in terms of perfect interventions, which is defined as follows.

[^0]
[^0]:    ${ }^{17}$ We deviate from the terminology in [18] where this is called a "compatible system of structural equations".
    ${ }^{18}$ We use the "hat" notation $\widetilde{\mathcal{E}}_{\mathcal{O}}$ to distinguish it from the ordinary subscript convention that $\mathcal{E}_{\mathcal{O}}=\prod_{\mathcal{F} \in \mathcal{O}} \mathcal{E}_{\mathcal{F}}$ for some subset $\mathcal{O} \subseteq \mathcal{H}$.

DEFINITION A. 28 (Perfect intervention on an mSCM). Consider a modular SCM $\widehat{\mathcal{M}}=$ $\left\langle\mathcal{G}, \boldsymbol{\mathcal { X }}, \mathcal{E},\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}, \mathbb{P}_{\mathcal{E}}\right\rangle$, a subset $I \subseteq \mathcal{V}$ of endogenous variables and a value $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}$. The perfect intervention $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ maps $\widehat{\mathcal{M}}$ to the modular SCM

$$
\widehat{\mathcal{M}}_{\mathrm{do}\left(I, \boldsymbol{\xi}_{I}\right)}:=\left\langle\mathcal{G}^{\mathrm{do}}, \boldsymbol{\mathcal { X }}, \mathcal{E}^{\mathrm{do}},\left(\boldsymbol{g}_{\mathcal{O}}^{\mathrm{do}}\right)_{\mathcal{O} \in \mathcal{L}\left(\mathcal{G}^{\mathrm{do}}\right)}, \mathbb{P}_{\mathcal{E}^{\mathrm{do}}}\right\rangle
$$

where

1. $\mathcal{G}^{\mathrm{do}}=\left(\mathcal{V}, \mathcal{E}^{\mathrm{do}}, \mathcal{H}^{\mathrm{do}}\right)$, where

$$
\begin{gathered}
\mathcal{E}^{\mathrm{do}}=\mathcal{E} \backslash\{v \rightarrow w: v \in \mathcal{V}, w \in I\} \\
\mathcal{H}^{\mathrm{do}}=\{\mathcal{F} \backslash I: \mathcal{F} \in \mathcal{H}\} \cup\{\{v\}: v \in I\}
\end{gathered}
$$

2. $\phi:\{\mathcal{F} \in \mathcal{H}: \mathcal{F} \backslash I \neq \emptyset\} \rightarrow \mathcal{H}^{\mathrm{do}} \backslash\{\{v\}: v \in I\}$ is a mapping such that $\phi(\mathcal{F}) \supseteq \mathcal{F} \backslash I$ for all $\mathcal{F} \in \mathcal{H}$ for which $\mathcal{F} \backslash I \neq \emptyset$,
3. $\mathcal{E}^{\mathrm{do}}=\prod_{\tilde{\mathcal{F}} \in \tilde{\mathcal{H}}^{\mathrm{do}}} \mathcal{E}_{\tilde{\mathcal{F}}}^{\mathrm{do}}$, where

$$
\mathcal{E}_{\tilde{\mathcal{F}}}^{\mathrm{do}}=\left\{\begin{array}{ll}
\mathcal{X}_{v} & \text { if } \tilde{\mathcal{F}}=\{v\} \text { for } v \in I \\
\prod_{\mathcal{F}=\phi^{-1}(\tilde{\mathcal{F}})} \mathcal{E}_{\mathcal{F}} & \text { if } \tilde{\mathcal{F}} \in \tilde{\mathcal{H}}^{\mathrm{do}} \backslash\{\{v\}: v \in I\}
\end{array}\right.
$$

4. for every $\mathcal{O} \in \mathcal{L}\left(\mathcal{G}^{\mathrm{do}}\right)$

$$
\boldsymbol{g}_{\mathcal{O}}^{\mathrm{do}}=\left\{\begin{array}{ll}
\mathbb{I}_{\{v\}} & \text { if } \mathcal{O}=\{v\} \text { for } v \in I \\
\boldsymbol{g}_{\mathcal{O}} & \text { otherwise }
\end{array}\right.
$$

(note that if $\mathcal{O}$ is a loop in $\mathcal{G}^{\mathrm{do}}$, then it is a loop in $\mathcal{G}$ ),
5. $\mathbb{P}_{\mathcal{E}^{\mathrm{do}}}=\prod_{\tilde{\mathcal{F}} \in \tilde{\mathcal{H}}^{\mathrm{do}}} \mathbb{P}_{\mathcal{E}_{\tilde{\mathcal{F}}}^{\mathrm{do}}}$, where

$$
\mathbb{P}_{\mathcal{E}_{\tilde{\mathcal{F}}}^{\mathrm{do}}}=\left\{\begin{array}{ll}
\delta_{\xi_{v}} & \text { if } \tilde{\mathcal{F}}=\{v\} \text { for } v \in I \\
\prod_{\mathcal{F}=\phi^{-1}(\tilde{\mathcal{F}})} \mathbb{P}_{\mathcal{E}_{\mathcal{F}}} & \text { if } \tilde{\mathcal{F}} \in \tilde{\mathcal{H}}^{\mathrm{do}} \backslash\{\{v\}: v \in I\}
\end{array}\right.
$$

In contrast to SCMs, these perfect interventions on modular SCMs are directly defined on the underlying HEDG and depend on the choice of the mapping $\phi$.
A.3.2. Relation between SCMs and modular SCMs The solutions of a modular SCM can be described by an SCM that is loop-wisely solvable.

DEFINITION A. 29 (Underlying SCM). Let $\widehat{\mathcal{M}}=\left\langle\mathcal{G}, \boldsymbol{\mathcal { X }}, \mathcal{E},\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be a modular SCM. Then the mapping $\iota$ maps $\widehat{\mathcal{M}}$ to the underlying SCM $\hat{\mathcal{M}}:=\langle\tilde{\mathcal{I}}, \tilde{\mathcal{J}}, \hat{\mathcal{X}}, \hat{\mathcal{E}}, \hat{\boldsymbol{f}}, \mathbb{P}_{\hat{\mathcal{E}}}\rangle$, where

1. $\tilde{\mathcal{I}}=\mathcal{V}$,
2. $\tilde{\mathcal{J}}=\tilde{\mathcal{H}}$,
3. $\hat{\mathcal{X}}=\mathcal{X}$,
4. $\hat{\mathcal{E}}=\mathcal{E}$,
5. $\hat{\boldsymbol{f}}$ is given by $\hat{f}_{v}=\left(\boldsymbol{g}_{\{v\}}\right)_{v}$ for all $v \in \mathcal{V}$,
6. $\mathbb{P}_{\hat{\mathcal{E}}}=\mathbb{P}_{\mathcal{E}}$.

Every solution $\boldsymbol{X}$ of a modular SCM $\widehat{\mathcal{M}}$ is also a solution of the underlying SCM $\iota(\widehat{\mathcal{M}})$. Observe that for the modular SCM $\widehat{\mathcal{M}}$ we have that the induced subgraph $\mathcal{G}^{a}(\iota(\widehat{\mathcal{M}}))_{\tilde{\mathcal{I}}}$, of the augmented graph of the underlying $\operatorname{SCM} \mathcal{G}^{a}(\iota(\widehat{\mathcal{M}}))$ on $\tilde{\mathcal{I}}$, is a subgraph of the underlying

HEDG $\mathcal{G}$, that is, $\mathcal{G}^{a}(\iota(\widehat{\mathcal{M}}))_{\widehat{\mathcal{I}}} \subseteq \mathcal{G}$. This implies that, in general, the underlying HEDG $\mathcal{G}$ of $\widehat{\mathcal{M}}$ may have more loops than the loops in $\mathcal{G}(\iota(\widehat{\mathcal{M}}))$. For a subset $\mathcal{O} \subseteq \widehat{\mathcal{I}}$, we have for the exogenous parents of the underlying SCM $\iota(\widehat{\mathcal{M}})$

$$
\operatorname{pa}(\mathcal{O}) \cap \hat{\mathcal{J}} \subseteq\{\mathcal{F} \in \hat{\mathcal{J}}: \mathcal{F} \cap \mathcal{O} \neq \emptyset\}
$$

where $\mathrm{pa}(\mathcal{O})$ denotes the set of parents of $\mathcal{O}$ in $\mathcal{G}^{a}(\iota(\widehat{\mathcal{M}}))$. Hence, in general, not all the hyperedges $\mathcal{F} \in \mathcal{H}$ such that $|\mathcal{F}|=2$ (i.e., bidirected edges) are in the set of bidirected edges $\mathcal{B}$ of the graph of the underlying $\operatorname{SCM} \mathcal{G}(\iota(\widehat{\mathcal{M}}))=(\mathcal{V}, \mathcal{E}, \mathcal{B})$. We conclude that the graph of the underlying SCM is, in general, a sparser graph than the HEDG of the modular SCM.

Next, we show that the compatible system of solution functions of a modular SCM induces a compatible system of solution functions on the underlying SCM. For this we need the notion of loop-wise solvability for SCMs.

Definition A. 30 (Loop-wise (unique) solvability for SCMs). We call an SCM $\mathcal{M}$

1. loop-wisely solvable, if $\mathcal{M}$ is solvable w.r.t. every loop $\mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))$, and
2. loop-wisely uniquely solvable, if $\mathcal{M}$ is uniquely solvable w.r.t. every loop $\mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))$.

DEFINITION A. 31 (Compatible system of solution functions for SCMs). For a loopwisely solvable SCM $\mathcal{M}$, we call a family of measurable solution functions $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))}$, where $\boldsymbol{g}_{\mathcal{O}}$ is a measurable solution function of $\mathcal{M}$ w.r.t. $\mathcal{O}$, a compatible system of solution functions, if for all $\mathcal{O}, \mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))$ with $\mathcal{O} \subseteq \mathcal{O}$ and for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$ we have

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)
$$

The underlying SCM of a modular SCM always has a compatible system of solution functions, by construction.

Proposition A.32. Let $\widehat{\mathcal{M}}=\left\langle\mathcal{G}, \boldsymbol{X}, \mathcal{E},\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be a modular SCM. Then the underlying SCM $\hat{\mathcal{M}}:=\iota(\widehat{\mathcal{M}})$ is loop-wisely solvable. Moreover, it has a compatible system of solution functions $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\hat{\mathcal{M}}))}$, where $\boldsymbol{g}_{\mathcal{O}}$ is a measurable solution function of $\hat{\mathcal{M}}$ w.r.t. $\mathcal{O}$.

This shows that a modular SCM can be seen as an SCM together with an additional structure of a compatible system of solution functions, and is, in particular, loop-wisely solvable.

Moreover, the class of simple SCMs corresponds exactly with those SCMs that are loopwisely uniquely solvable.

LEMMA A.33. An SCM $\mathcal{M}$ is simple if and only if it is loop-wisely uniquely solvable.
In particular, for simple SCMs, or loop-wisely uniquely solvable SCMs, there always exists a compatible system of solution functions.

Proposition A.34. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be a simple SCM. Then every family of measurable solution functions $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))}$, where $\boldsymbol{g}_{\mathcal{O}}$ is a measurable solution function of $\mathcal{M}$ w.r.t. $\mathcal{O}$, is a compatible system of solution functions.

![img-7.jpeg](img-7.jpeg)

Fig 7: Overview of causal graphical models. The "gray" and "dark gray" areas contain all the causal graphical models that can be modeled by an SCM and an acyclic SCM, respectively.
A.4. Overview of causal graphical models Figure 7 gives an overview of the causal graphical models related to SCMs. The "gray" area contains all the causal graphical models that can be modeled by an SCM, by which we mean, that there exists an SCM that can describe all its observational and interventional distributions. The "dark gray" area contains all the causal graphical models which can be modeled by an acyclic SCM. Acyclic SCMs generalize causal Bayesian networks (causal BNs) [51] to allow for latent confounders and to derive counterfactuals. Simple SCMs form a subclass of SCMs that extends acyclic SCMs to the cyclic setting, while preserving many of their convenient properties. Modular SCMs [18] can be seen as SCMs that have an additional structure of compatible system of solution functions and contain, in particular, the class of simple SCMs. Forré and Mooij [18] showed that modular SCMs satisfy various convenient properties, like marginalization and the general directed global Markov property. We show that for SCMs in general various of those properties still hold under certain solvability conditions. A generalization of SCMs, known as causal constraints models (CCMs), has been proposed [3] in order to completely model the causal semantics of the equilibrium solutions of a dynamical system given the initial conditions. This class of CCMs is rich enough to model the causal semantics of SCMs, but does not come with a single graphical representation that provides both a Markov property and a causal interpretation [4].

# APPENDIX B: (UNIQUE) SOLVABILITY PROPERTIES 

In this appendix, we provide additional (unique) solvability properties for SCMs. In Appendix B. 1 we provide a sufficient condition of solvability w.r.t. (strict) subsets. In Appendix B. 2 we discuss how (unique) solvability is preserved under strict super- and subsets. In Appendix B. 3 we discuss how (unique) solvability is preserved under unions and intersections. The proofs of the theoretical results in this appendix are given in Appendix E.
B.1. Sufficient condition for solvability w.r.t. subsets For solvability w.r.t. a (strict) subset of $\mathcal{I}$ there exists a sufficient condition that is similar to the sufficient (and necessary) condition (2) in Theorem 3.2 in the sense that it is formulated in terms of the solutions of (a subset of) the structural equations, but no measurability is required.

Proposition B. 1 (Sufficient condition for solvability w.r.t. a subset). Let $\mathcal{M}=$ $\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\rangle$ be an SCM and $\mathcal{O} \subseteq \mathcal{I}$ a subset. If for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x}_{\backslash \mathcal{O}} \in \mathcal{X}_{\backslash \mathcal{O}}$ the topological space

$$
\mathcal{S}_{\left(\boldsymbol{e}, \boldsymbol{x}_{\backslash \mathcal{O}}\right)}:=\left\{\boldsymbol{x}_{\mathcal{O}} \in \mathcal{X}_{\mathcal{O}}: \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})\right\}
$$

with the subspace topology induced by $\boldsymbol{\mathcal { X }}_{\mathcal{O}}$ is nonempty and $\sigma$-compact, ${ }^{19}$ then $\mathcal{M}$ is solvable w.r.t. $\mathcal{O}$.

For many purposes, this condition of $\sigma$-compactness suffices since it contains for example all countable discrete spaces, every interval of the real line, and moreover all the Euclidean spaces. In particular, it suffices to prove a sufficient and necessary condition for unique solvability w.r.t. a subset, in terms of the solutions of a subset of the structural equations (see Theorem 3.6). For larger solution spaces, we refer the reader to [30]. For the class of linear SCMs (see Definition C.1), we provide in Proposition C. 2 a sufficient and necessary condition for solvability w.r.t. a (strict) subset of $\mathcal{I}$.
B.2. (Unique) solvability w.r.t. strict super- and subsets In general, (unique) solvability w.r.t. $\mathcal{O} \subseteq \mathcal{I}$ does not imply (unique) solvability w.r.t. a strict superset $\mathcal{O} \subsetneq \mathcal{V} \subseteq \mathcal{I}$ nor w.r.t. a strict subset $\mathcal{W} \subsetneq \mathcal{O}$, as can be seen in the following example.

EXAMPLE B. 2 (Solvability is not preserved under strict sub- or supersets). Consider the $\operatorname{SCM} \mathcal{M}=\left\langle\mathbf{3}, \emptyset, \mathbb{R}^{3}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ where the causal mechanism is given by

$$
f_{1}(\boldsymbol{x})=x_{1} \cdot\left(1-\mathbf{1}_{\{1\}}\left(x_{2}\right)\right)+1, f_{2}(\boldsymbol{x})=x_{2}, f_{3}(\boldsymbol{x})=x_{3} \cdot\left(1-\mathbf{1}_{\{-1\}}\left(x_{2}\right)\right)+1
$$

This SCM is (uniquely) solvable w.r.t. the subsets $\{1,2\},\{2,3\}$, however it is not (uniquely) solvable w.r.t. the subsets $\{1\},\{3\}$ and $\{1,2,3\}$, and not uniquely solvable w.r.t. $\{2\}$.

However, in Proposition 3.10 we show that solvability w.r.t. $\mathcal{O}$ implies solvability w.r.t. every ancestral subset in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$.
B.3. (Unique) solvability w.r.t. unions and intersections In general, (unique) solvability is not preserved under unions and intersections. The following example illustrates that (unique) solvability is in general not preserved under intersections.

Example B. 3 (Solvability is not preserved under intersections). Consider the SCM $\mathcal{M}=\left\langle\mathbf{3}, \emptyset, \mathbb{R}^{3}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ where the causal mechanism is given by

$$
f_{1}(\boldsymbol{x})=0, f_{2}(\boldsymbol{x})=x_{2} \cdot\left(1-\mathbf{1}_{\{0\}}\left(x_{1} \cdot x_{3}\right)\right)+1, f_{3}(\boldsymbol{x})=0
$$

Then $\mathcal{M}$ is (uniquely) solvable w.r.t. $\{1,2\}$ and $\{2,3\}$, however it is not (uniquely) solvable w.r.t. their intersection.

Example B. 2 gives an example where (unique) solvability is not preserved under unions. Even, if we take the union of disjoint subsets, (unique) solvability is not preserved (see Example 2.4). Although, in general, unique solvability is not preserved under unions, we show next that unique solvability is preserved under the union of ancestral subsets, under the following assumptions.

Proposition B. 4 (Combining measurable solution functions on different sets). Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathcal{X}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\right\rangle$ be an $\operatorname{SCM}, \mathcal{O} \subseteq \mathcal{I}$ a subset and $\mathcal{A}, \tilde{\mathcal{A}} \subseteq \mathcal{O}$ two ancestral subsets in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$. If $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{A}, \tilde{\mathcal{A}}$ and $\mathcal{A} \cap \tilde{\mathcal{A}}$, then $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{A} \cup \tilde{\mathcal{A}}$.

[^0]
[^0]:    ${ }^{19}$ A topological space $\mathcal{X}$ is called $\sigma$-compact if it is the union of a countable set of compact topological spaces.

A consequence of this property is that in order to check whether an SCM is ancestrally uniquely solvable w.r.t. $\mathcal{O}$, it suffices to check that it is uniquely solvable w.r.t. the ancestral subsets for each node in $\mathcal{O}$.

COROLLARY B.5. Let $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \boldsymbol{\mathcal { Z }}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be an SCM and $\mathcal{O} \subseteq \mathcal{I}$ a subset. Then $\mathcal{M}$ is ancestrally uniquely solvable w.r.t. $\mathcal{O}$ if and only if $\mathcal{M}$ is uniquely solvable w.r.t. $\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(i)$ for every $i \in \mathcal{O}$.

# APPENDIX C: LINEAR SCMS 

In this appendix, we provide some results about (unique) solvability and marginalization for linear SCMs. Linear SCMs form a special class of SCMs that has seen much attention in the literature [see, e.g., 5, 27]. The proofs of the theoretical results in this appendix are given in Appendix E.

Definition C. 1 (Linear SCM). We call an SCM $\mathcal{M}=\left\langle\mathcal{I}, \mathcal{J}, \mathbb{R}^{\mathcal{I}}, \mathbb{R}^{\mathcal{J}}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}^{\mathcal{J}}}\right\rangle$ linear if each component of the causal mechanism is a linear combination of the endogenous and exogenous variables, that is

$$
f_{i}(\boldsymbol{x}, \boldsymbol{e})=\sum_{j \in \mathcal{I}} B_{i j} x_{j}+\sum_{k \in \mathcal{J}} \Gamma_{i k} e_{k}
$$

where $i \in \mathcal{I}, B \in \mathbb{R}^{\mathcal{I} \times \mathcal{I}}$ and $\Gamma \in \mathbb{R}^{\mathcal{I} \times \mathcal{J}}$ are matrices, and $\mathbb{P}_{\mathbb{R}^{\mathcal{J}}}$ is a product probability measure $^{20}$ on $\mathbb{R}^{\mathcal{J}}$.

For a subset $\mathcal{O} \subseteq \mathcal{I}$ we also use the shorthand vector-notation

$$
\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})=B_{\mathcal{O I}} \boldsymbol{x}+\Gamma_{\mathcal{O} \mathcal{J}} \boldsymbol{e}
$$

A nonzero coefficient $B_{i j}$ for $i, j \in \mathcal{I}$ such that $i \neq j$ corresponds with a directed edge $j \rightarrow i$ in the (augmented) graph, and a coefficient $B_{i i}=1$ for $i \in \mathcal{I}$ corresponds with a self-cycle $i \rightarrow i$ in the (augmented) graph of the SCM. A nonzero coefficient $\Gamma_{i j}$ for $i \in \mathcal{I}, j \in \mathcal{J}$ with $\mathbb{P}_{\mathcal{E}_{j}}$ a nondegenerate probability distribution over $\mathbb{R}$ corresponds with a directed edge $j \rightarrow i$ in the augmented graph. A nonzero entry $\left(\Gamma \Gamma^{\mathcal{I}}\right)_{i j}$ for $i, j \in \mathcal{I}$ with $i \neq j$ such that there exists a $k \in \mathcal{J}$ for which $\Gamma_{i k}, \Gamma_{j k} \neq 0$ and $\mathbb{P}_{\mathcal{E}_{k}}$ a nondegenerate probability distribution over $\mathbb{R}$ corresponds with a bidirected edge $i \leftrightarrow j$ in the graph of the SCM.

For linear SCMs, the solvability condition w.r.t. a subset, Definition 3.1, translates into a matrix condition. In order to state this condition we need to define the pseudoinverse (or the Moore-Penrose inverse) $A^{+}$of a real matrix $A[24,54]$. The pseudoinverse of the matrix $A$ is defined by $A^{+}:=V \Sigma^{+} U^{*}$, where $A=U \Sigma V^{*}$ is the singular value decomposition of $A$ and $\Sigma^{+}$is obtained by replacing each nonzero entry on the diagonal of $\Sigma$ by its reciprocal [24]. One of its useful properties is that $A A^{+} A=A$.

Proposition C. 2 (Sufficient and necessary condition for solvability w.r.t. a subset for linear SCMs). Let $\mathcal{M}$ be a linear SCM and $\mathcal{L} \subseteq \mathcal{I}$ and $\mathcal{O}=\mathcal{I} \backslash \mathcal{L}$. Then $\mathcal{M}$ is solvable w.r.t. $\mathcal{L}$ if and only if for the matrix $A_{\mathcal{L} \mathcal{L}}=\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$, for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x}_{\mathcal{O}} \in \mathcal{X}_{\mathcal{O}}$ the identity

$$
A_{\mathcal{L} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{*}\left(B_{\mathcal{L O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}\right)=B_{\mathcal{L O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}
$$

[^0]
[^0]:    ${ }^{20}$ Note that we do not assume that the probability measure $\mathbb{P}_{\mathbb{R}^{\mathcal{J}}}$ is Gaussian.

is satisfied, where $A_{\mathcal{L} \mathcal{L}}^{+}$is the pseudoinverse of $A_{\mathcal{L} \mathcal{L}}$. Moreover, if $\mathcal{M}$ is solvable w.r.t. $\mathcal{L}$, then for every vector $\boldsymbol{v} \in \mathbb{R}^{\mathcal{L}}$ the mapping $\boldsymbol{g}_{\mathcal{L}}^{\boldsymbol{v}}: \mathbb{R}^{\mathcal{O}} \times \mathbb{R}^{\mathcal{J}} \rightarrow \mathbb{R}^{\mathcal{L}}$ given by

$$
\boldsymbol{g}_{\mathcal{L}}^{\boldsymbol{v}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)=A_{\mathcal{L} \mathcal{L}}^{+}\left(B_{\mathcal{L O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}\right)+\left[\mathbb{I}_{\mathcal{L}}-A_{\mathcal{L} \mathcal{L}}^{+} A_{\mathcal{L} \mathcal{L}}\right] \boldsymbol{v}
$$

is a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{L}$.
For linear SCMs, the unique solvability condition w.r.t. a subset translates into a matrix invertibility condition, as was already shown in [27].

Proposition C. 3 (Sufficient and necessary condition for unique solvability w.r.t. a subset for linear SCMs). Let $\mathcal{M}$ be a linear $S C M, \mathcal{L} \subseteq \mathcal{I}$ and $\mathcal{O}=\mathcal{I} \backslash \mathcal{L}$. Then $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if the matrix $A_{\mathcal{L} \mathcal{L}}=\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$ is invertible. Moreover, if $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$, then the mapping $\boldsymbol{g}_{\mathcal{L}}: \mathbb{R}^{\mathcal{O}} \times \mathbb{R}^{\mathcal{J}} \rightarrow \mathbb{R}^{\mathcal{L}}$ given by

$$
\boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)=A_{\mathcal{L} \mathcal{L}}^{-1}\left(B_{\mathcal{L O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}\right)
$$

is a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{L}$.
Note that if $A_{\mathcal{L} \mathcal{L}}$ is invertible, then $A_{\mathcal{L} \mathcal{L}}^{+}=A_{\mathcal{L} \mathcal{L}}^{-1}$ (see Lemma 1.3 in [54]), and the matrix condition of Proposition C. 2 is always satisfied and all the measurable solution functions $\boldsymbol{g}_{\mathcal{L}}^{\boldsymbol{v}}$ of Proposition C. 2 are (up to a $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-null set) equal to the solution function $\boldsymbol{g}_{\mathcal{L}}$ of Proposition C.3.

REMARK. A sufficient condition for $A_{\mathcal{L} \mathcal{L}}$ to be invertible is that the spectral radius of $B_{\mathcal{L} \mathcal{L}}$ is less than one. If that is the case, then $A_{\mathcal{L} \mathcal{L}}^{-1}=\sum_{n=0}^{\infty}\left(B_{\mathcal{L} \mathcal{L}}\right)^{n}$. Note that the nonzero nondiagonal entries of the matrix $B_{\mathcal{L} \mathcal{L}}$ represent the directed edges in the induced subgraph $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$. In particular, if the diagonal entries of the matrix $B_{\mathcal{L} \mathcal{L}}$ are zero, then for $n \in \mathbb{N}$, the coefficients of the matrix $\left(B_{\mathcal{L} \mathcal{L}}\right)^{n}$ in the sum represent the sum of the product of the edge weights $B_{i j}$ over directed paths of length $n$ in the induced subgraph $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$.

From Proposition 3.10 we know that an SCM is solvable w.r.t. $\mathcal{L}$ if and only if it is ancestrally solvable w.r.t. $\mathcal{L}$. In particular, this result also holds for linear SCMs. We saw in Example 3.11 that a similar result for unique solvability does not hold, that is, in general, it does not hold that unique solvability w.r.t. $\mathcal{L}$ implies ancestral unique solvability w.r.t. $\mathcal{L}$. For the class of linear SCMs we do have the following positive result.

Proposition C. 4 (Equivalent unique solvability conditions for linear SCMs). For a linear SCM $\mathcal{M}$ and a subset $\mathcal{L} \subseteq \mathcal{I}$ the following are equivalent:

1. $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$;
2. $\mathcal{M}$ is ancestrally uniquely solvable w.r.t. $\mathcal{L}$;
3. $\mathcal{M}$ is uniquely solvable w.r.t. each strongly connected component in $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$.

Under the condition of unique solvability w.r.t. a subset $\mathcal{L}$ we can define the marginalization w.r.t. $\mathcal{L}$ of a linear SCM by mere substitution.

Proposition C. 5 (Marginalization of a linear SCM). Let $\mathcal{M}$ be a linear SCM and $\mathcal{L} \subseteq \mathcal{I}$ a subset of endogenous variables such that $\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$ is invertible. Then there exists a marginalization $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ that is linear and with marginal causal mechanism $\tilde{\boldsymbol{f}}: \mathbb{R}^{\mathcal{O}} \times$ $\mathbb{R}^{\mathcal{J}} \rightarrow \mathbb{R}^{\mathcal{O}}$ given by

$$
\tilde{\boldsymbol{f}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)=\left[B_{\mathcal{O O}}+B_{\mathcal{O} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{-1} B_{\mathcal{L} \mathcal{O}}\right] \boldsymbol{x}_{\mathcal{O}}+\left[B_{\mathcal{O} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{-1} \Gamma_{\mathcal{L} \mathcal{J}}+\Gamma_{\mathcal{O} \mathcal{J}}\right] \boldsymbol{e}
$$

where $A_{\mathcal{L} \mathcal{L}}=\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$. Moreover, this marginalization respects the latent projection, that is, $\left(\mathcal{G}^{a} \circ \operatorname{marg}(\mathcal{L})\right)(\mathcal{M}) \subseteq\left(\operatorname{marg}(\mathcal{L}) \circ \mathcal{G}^{a}\right)(\mathcal{M})$.

![img-8.jpeg](img-8.jpeg)

Fig 8: Damped coupled harmonic oscillator (top) and the graph of the SCM $\mathcal{M}$ that describes the positions of the masses at equilibrium (bottom) of Example D. 1 for $d=5$.

From Theorem 5.6 we know that $\mathcal{M}$ and its marginalization $\mathcal{M}_{\operatorname{mag}(\mathcal{L})}$ over $\mathcal{L}$ are observationally, interventionally and counterfactually equivalent w.r.t. $\mathcal{O}$. A similar result can also be found in [27]. In contrast to nonlinear SCMs, this class of linear SCMs has the convenient property that every marginalization of a model of this class respects the latent projection. Moreover, the subclass of simple linear SCMs is even closed under marginalization.

# APPENDIX D: EXAMPLES 

In this appendix, we provide additional examples. In Appendix D. 1 we provide some examples of SCMs that describe the equilibrium states of certain feedback systems governed by (random) differential equations [6] that motivated our study of cyclic SCMs. In Appendix D. 2 we provide additional examples that support the main text.
D.1. SCMs as equilibrium models In many systems occurring in the real world feedback loops between observed variables are present. For example, in economics, the price of a product may be a function of the demanded or supplied quantities, and vice versa; or in physics, two masses that are connected by a spring may exert forces on each other. Such systems are often described by a system of (random) differential equations. In [6] it was shown that SCMs are capable of modeling the causal semantics of the equilibrium states of such systems. For illustration purposes we provide the following toy example of interacting masses that are attached to springs.

Example D. 1 (Damped coupled harmonic oscillator). Consider a one-dimensional system of $d$ point masses $m_{i} \in \mathbb{R}(i=1, \ldots, d)$ with positions $Q_{i}$, which are coupled by springs, with spring constants $k_{i}>0$ and equilibrium lengths $\ell_{i}>0(i=0, \ldots, d)$, under influence of friction with friction coefficients $b_{i} \in \mathbb{R}(i=1, \ldots, d)$ and with fixed endpoints $Q_{0}=0$ and $Q_{d+1}=L>0$ (see Figure 8 (top)). The equations of motion of this system are provided by the following differential equations

$$
\frac{d^{2} Q_{i}}{d t^{2}}=\frac{k_{i}}{m_{i}}\left(Q_{i+1}-Q_{i}-\ell_{i}\right)+\frac{k_{i-1}}{m_{i}}\left(Q_{i-1}-Q_{i}+\ell_{i-1}\right)-\frac{b_{i}}{m_{i}} \frac{d Q_{i}}{d t} \quad(i=1, \ldots, d)
$$

The dynamics of the masses, in terms of the position, velocity and acceleration, is described by a single and separate equation of motion for each mass. Under friction, that is, $b_{i}>0$ $(i=1, \ldots, d)$, there is a unique equilibrium position, where the sum of forces vanishes for each mass. If one starts out of equilibrium, for example, by moving one or several masses out of equilibrium, then the masses will start to oscillate and converge to their unique equilibrium position. At equilibrium (i.e., for $t \rightarrow \infty$ ) the velocity $\frac{d Q_{i}}{d t}$ and acceleration $\frac{d^{2} Q_{i}}{d t^{2}}$ of the masses vanish (i.e., $\frac{d Q_{i}}{d t}, \frac{d^{2} Q_{i}}{d t^{2}} \rightarrow 0$ ), and thus the following equation holds at equilibrium

$$
0=\frac{k_{i}}{m_{i}}\left(Q_{i+1}-Q_{i}-\ell_{i}\right)+\frac{k_{i-1}}{m_{i}}\left(Q_{i-1}-Q_{i}+\ell_{i-1}\right)
$$

for each mass $(i=1, \ldots, d)$. Hence, for each mass $i=1, \ldots, d$ its equilibrium position $Q_{i}$ is given by

$$
Q_{i}=\frac{k_{i}\left(Q_{i+1}-\ell_{i}\right)+k_{i-1}\left(Q_{i-1}+\ell_{i-1}\right)}{k_{i}+k_{i-1}}
$$

By considering the $\ell_{i}$ and $k_{i}$ and $L$ as fixed parameters, we arrive at a linear SCM (see [6] for more details about constructing an SCM from a dynamical system)

$$
\mathcal{M}=\left\langle\{1, \ldots, d\}, \emptyset, \mathbb{R}^{d}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle
$$

where the causal mechanism $\boldsymbol{f}$ is given by

$$
f_{i}(\boldsymbol{q})=\frac{k_{i}\left(q_{i+1}-\ell_{i}\right)+k_{i-1}\left(q_{i-1}+\ell_{i-1}\right)}{k_{i}+k_{i-1}}
$$

Alternatively, (some of) the parameters could be treated as exogenous variables instead. Its graph is depicted in Figure 8 (bottom). This SCM allows us to describe the equilibrium behavior of the system under perfect intervention. For example, when forcing the mass $j$ to a fixed position $Q_{j}=\xi_{j}$ with $0 \leq \xi_{j} \leq L$, the equilibrium positions of the masses correspond to the solutions of the intervened model $\mathcal{M}_{\mathrm{do}(\{j\}, \xi)}$ It is an easy exercise to show that $\mathcal{M}$ is a simple SCM by using Proposition C.3.

Next, we show that the well known market equilibrium model from economics, which has been thoroughly discussed in the literature [see, e.g., 65], can be described by a (non-simple) SCM. This example illustrates how self-cycles enrich the class of SCMs.

Example D. 2 (Price, supply and demand). Let $X_{D}$ denote the demand and $X_{S}$ the supply of a quantity of a product. The price of the product is denoted by $X_{P}$. The following system of differential equations describes how the demanded and supplied quantities are determined by the price, and how price adjustments occur in the market:

$$
\begin{aligned}
X_{D} & =\beta_{D} X_{P}+E_{D} \\
X_{S} & =\beta_{S} X_{P}+E_{S} \\
\frac{d X_{P}}{d t} & =X_{D}-X_{S}
\end{aligned}
$$

where $E_{D}$ and $E_{S}$ are exogenous random influences on the demand and supply, respectively, $\beta_{D}<0$ is the reciprocal of the slope of the demand curve, and $\beta_{S}>0$ is the reciprocal of the slope of the supply curve. At the situation known as a "market equilibrium", the price is determined implicitly by the condition that demanded and supplied quantities should be equal, since $\frac{d X_{P}}{d t}=0$ at equilibrium. Applying the results in [6] gives rise to a linear SCM $\mathcal{M}=\left\langle\{P, S, D\},\{S, D\}, \mathbb{R}^{3}, \mathbb{R}^{2}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{E}}\right\rangle$ at equilibrium with the causal mechanism defined by

$$
\begin{aligned}
f_{D}(\boldsymbol{x}, \boldsymbol{e}) & :=\beta_{D} x_{P}+e_{D} \\
f_{S}(\boldsymbol{x}, \boldsymbol{e}) & :=\beta_{S} x_{P}+e_{S} \\
f_{P}(\boldsymbol{x}, \boldsymbol{e}) & :=x_{P}+\left(x_{D}-x_{S}\right)
\end{aligned}
$$

Note how we use a self-cycle for $P$ in order to implement the equilibrium equation $X_{D}=X_{S}$ as the causal mechanism for the price $P .{ }^{21}$ Moreover, $\mathcal{M}$ is uniquely solvable. Its augmented graph is depicted in Figure 9 (left).

[^0]
[^0]:    ${ }^{21}$ Richardson and Robins [65] argue that this market equilibrium model cannot be modeled as an SCM. We observe that it can, as long as one allows for self-cycles.

![img-9.jpeg](img-9.jpeg)

Fig 9: The augmented graph of the SCM $\mathcal{M}$ (left), its twin SCM $\mathcal{M}^{\text {twin }}$ (center) and the intervened twin SCM $\left(\mathcal{M}^{\text {twin }}\right)_{\operatorname{do}\left(\left\{S, S^{\prime}\right\},\left(s, s^{\prime}\right)\right)}$ (right) of Examples D. 2 and D.3.

Next, we provide an example of how counterfactuals can be sensibly formulated for cyclic SCMs, namely for the price, supply and demand model at equilibrium.

Example D. 3 (Price, supply and demand at equilibrium). Consider the price, supply and demand model at equilibrium of Example D. 2 given by the SCM $\mathcal{M}$. As an example of a counterfactual query, consider

$$
\mathbb{P}\left(X_{P}^{\prime} \mid \operatorname{do}\left(X_{S}=s, X_{S^{\prime}}=s^{\prime}\right), X_{P}=p\right)
$$

which denotes the conditional distribution of $X_{P}^{\prime}$ given $X_{P}=p$ of a solution of the intervened twin model $\mathcal{M}_{\operatorname{do}\left(\left\{S, S^{\prime}\right\},\left(s, s^{\prime}\right)\right)}^{\text {twin }}$. In words: how would-ceteris paribus-price have been distributed, had we intervened to set supplied quantities equal to $s^{\prime}$, given that actually we intervened to set supplied quantities equal to $s$ and observed that this led to price $p$ ? A straightforward calculation shows that this counterfactual distribution of price is the Dirac measure on $x_{P}^{\prime}=p+\left(s^{\prime}-s\right) / \beta_{D}$. The augmented graphs of the SCM, its twin graph, and its intervened twin graph are depicted in Figure 9.
D.2. Additional examples In this subsection, we provide additional examples that support the main text.

# Section 2 

Example D. 4 (Structural equations up to almost sure equality). Consider the SCM $\mathcal{M}=\langle\mathbf{1}, \mathbf{1}, \mathcal{X}, \mathcal{E}, f, \mathbb{P}_{\mathcal{E}}\rangle$ with $\mathcal{X}=\mathcal{E}=\{-1,0,1\}, \mathbb{P}_{\mathcal{E}}(\{-1\})=\mathbb{P}_{\mathcal{E}}(\{1\})=\frac{1}{2}$ and $f(x, e)=$ $e^{2}+e-1$. Let $\overline{\mathcal{M}}$ be the SCM $\mathcal{M}$ but with a different causal mechanism $\tilde{f}(x, e)=e$. Then the sets of solutions of the structural equations agree for both SCMs for $e \in\{-1,+1\}$, while they differ only for $e=0$, which occurs with probability zero. Hence, a pair of random variables $(X, E)$ is a solution of $\mathcal{M}$ if and only if it is a solution of $\overline{\mathcal{M}}$.

Example D. 5 (The for-all and for-almost-every quantifier do not commute in general). Consider the SCM $\mathcal{M}=\langle\mathbf{2}, \mathbf{1}, \boldsymbol{\mathcal { X }}, \mathcal{E}, \boldsymbol{f}, \mathbb{P}_{\mathcal{E}}\rangle$ with $\boldsymbol{\mathcal { X }}=(0,1)^{2}, \mathcal{E}=(0,1)$, the causal mechanism $\boldsymbol{f}$ given by

$$
f_{1}(\boldsymbol{x}, e)=x_{1}, \quad f_{2}(\boldsymbol{x}, e)=\mathbf{1}_{\{0\}}\left(x_{1}-e\right) \cdot\left(x_{2}+1\right)
$$

and $\mathbb{P}_{\mathcal{E}}=\mathbb{P}^{E}$ with $E \sim \mathcal{U}(0,1)$. Define the property

$$
P(\boldsymbol{x}, e):= \begin{cases}1 & \text { if } \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, e) \text { holds } \\ 0 & \text { otherwise }\end{cases}
$$

![img-10.jpeg](img-10.jpeg)

Fig 10: Augmented graphs of the SCMs $\mathcal{M}$ (left) and $\mathcal{M}^{*}$ (right) in Example D.6. For SCM $\overline{\mathcal{M}}^{*}$, the exogenous variable $E$ consists of two real-valued components; the structural equation for $X_{1}$ depends only on the first, while the structural equation for $X_{2}$ depends only on the second component.

Then, for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ and for $\mathbb{P}_{\mathcal{E}}$-almost every $e \in \mathcal{E}$ the property $P(\boldsymbol{x}, e)$ holds, however for $\mathbb{P}_{\mathcal{E}}$-almost every $e \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ the property $P(\boldsymbol{x}, e)$ does not hold, since for $\mathbb{P}_{\mathcal{E}}$ almost every $e \in \mathcal{E}$ the equation $\boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, e)$ does not hold for $x_{1}=e$. Hence, in general, for a property $P(\boldsymbol{x}, e)$ we have that for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ and for $\mathbb{P}_{\mathcal{E}}$-almost every $e \in \mathcal{E} P(\boldsymbol{x}, e)$ does not imply for $\mathbb{P}_{\mathcal{E}}$-almost every $e \in \mathcal{E}$ for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }} P(\boldsymbol{x}, e)$ (see Lemma F. 11 for additional properties of the for-almost-every quantifier).

Example D. 6 (Representation of latent confounders). Consider the SCM $\mathcal{M}=$ $\left\langle\mathbf{2}, \mathbf{3}, \mathbb{R}^{2}, \mathbb{R}^{3}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}^{3}}\right\rangle$ with causal mechanism given by

$$
\begin{aligned}
f_{1}\left(e_{1}, e_{3}\right) & =e_{1}+e_{3} \\
f_{2}\left(x_{1}, e_{2}, e_{3}\right) & =x_{1} e_{3}+e_{2}
\end{aligned}
$$

and $\mathbb{P}_{\mathbb{R}^{3}}$ the standard-normal distribution on $\mathbb{R}^{3}$; Figure 10 (left) shows the corresponding augmented graph. Then there exists no SCM $\mathcal{M}^{*}=\left\langle\mathbf{2}, \mathbf{1}, \mathbb{R}^{2}, \mathbb{R}^{2}, \boldsymbol{f}^{*}, \mathbb{P}_{\mathbb{R}^{2}}^{*}\right\rangle$ that satisfies the following conditions:

1. $\mathcal{M}^{*}$ is interventionally equivalent to $\mathcal{M}$,
2. its structural equations have the form

$$
\begin{aligned}
& x_{1}=f_{1}^{*}\left(e_{1}^{*}\right) \\
& x_{2}=f_{2}^{*}\left(x_{1}, e_{2}^{*}\right)
\end{aligned}
$$

where $e_{1}^{*}, e_{2}^{*}$ are the two components of $e^{*}=\left(e_{1}^{*}, e_{2}^{*}\right) \in \mathbb{R}^{2}$,
3. the function $e_{2}^{*} \mapsto f_{2}^{*}\left(x_{1}, e_{2}^{*}\right)$ is strictly monotonically increasing for all $x_{1} \in \mathbb{R}$,
4. the cumulative distribution function $F_{2}^{*}$ of the second component of $\mathbb{P}_{\mathbb{R}^{2}}^{*}$ is continuous and strictly monotonically increasing.
The augmented graph of such an SCM is shown in Figure 10 (right).
The proof of this statement proceeds by contradiction. Assume that such an SCM $\mathcal{M}^{*}$ exists. For any uniquely solvable SCM $\tilde{\mathcal{M}}$ and any endogenous variable $i$ appearing in $\tilde{\mathcal{M}}$, we denote with $F_{X_{i}}^{\tilde{\mathcal{M}}}$ the marginal cumulative distribution function of the $i^{\text {th }}$ component of the observational distribution of $\tilde{\mathcal{M}}$. For all $\xi \in \mathbb{R}$, we have for all $x_{2} \in \mathbb{R}$

$$
F_{X_{2}}^{\mathcal{M}_{\mathrm{do}(1) \cdot \xi)}}\left(x_{2}\right)=\mathbb{P}\left(\xi E_{3}+E_{2} \leq x_{2}\right)=\Phi\left(x_{2} / \sqrt{1+\xi^{2}}\right)
$$

where $\Phi$ denotes the (invertible) cdf of the standard-normal distribution. Now define $\phi: \mathbb{R} \rightarrow$ $\mathbb{R}$ with $\phi\left(e_{2}\right):=\Phi^{-1}\left(F_{2}^{*}\left(e_{2}\right)\right)$ and define the SCM $\tilde{\mathcal{M}}:=\left\langle\mathbf{2}, \mathbf{1}, \mathbb{R}^{2}, \mathbb{R}^{2}, \tilde{\boldsymbol{f}}, \tilde{\mathbb{P}}_{\mathbb{R}^{2}}\right\rangle$ such that the causal mechanism $\tilde{\boldsymbol{f}}$ is given by

$$
\begin{aligned}
\tilde{f}_{1}\left(e_{1}\right) & =f_{1}^{*}\left(e_{1}\right) \\
\tilde{f}_{2}\left(x_{1}, e_{2}\right) & =f_{2}^{*}\left(x_{1}, \phi^{-1}\left(e_{2}\right)\right)
\end{aligned}
$$

and $\tilde{\mathbb{P}}_{\mathbb{R}^{2}}$ is the push-forward measure of $\mathbb{P}_{\mathbb{R}^{2}}^{*}$ using $\left(\mathbb{I}_{\mathbb{R}}, \phi\right)$. Then, $\tilde{\mathcal{M}}$ is interventionally equivalent to $\mathcal{M}^{*}$ by construction, and the second component of $\tilde{\mathbb{P}}_{\mathbb{R}^{2}}$ has a standard-normal distribution. Let $\left(\tilde{X}_{1}, \tilde{X}_{2}, \tilde{E}\right)$ be a solution of $\tilde{\mathcal{M}}$ and let us write $\tilde{E}=\left(\tilde{E}_{1}, \tilde{E}_{2}\right)$. Then, for all

$\xi \in \mathbb{R}$ and $\tilde{e}_{2} \in \mathbb{R}$,

$$
F_{X_{2}}^{\mathcal{M}_{\mathrm{do}(\{1\}, \xi)}}\left(\tilde{f}_{2}\left(\xi, \tilde{e}_{2}\right)\right)=\mathbb{P}\left(\tilde{f}_{2}\left(\xi, \tilde{E}_{2}\right) \leq \tilde{f}_{2}\left(\xi, \tilde{e}_{2}\right)\right)=\mathbb{P}\left(\tilde{E}_{2} \leq \tilde{e}_{2}\right)=\Phi\left(\tilde{e}_{2}\right)
$$

using that $\tilde{e}_{2} \mapsto \tilde{f}_{2}\left(\xi, \tilde{e}_{2}\right)$, too, is strictly monotonically increasing for all $\xi$. This implies that, for all $\xi \in \mathbb{R}$ and $\tilde{e}_{2} \in \mathbb{R}$,

$$
\tilde{f}_{2}\left(\xi, \tilde{e}_{2}\right)=\left(F_{X_{2}}^{\mathcal{M}_{\mathrm{do}(\{1\}, \xi)}}\right)^{-1}\left(\Phi\left(\tilde{e}_{2}\right)\right)=\sqrt{1+\xi^{2}} \tilde{e}_{2}
$$

where we used interventional equivalence of $\mathcal{M}$ and $\tilde{\mathcal{M}}$, and (1) for the second equality. Furthermore, $\tilde{X}_{2}=\tilde{f}_{2}\left(\tilde{X}_{1}, \tilde{E}_{2}\right)=\sqrt{1+\tilde{X}_{1}^{2}} \tilde{E}_{2}$ a.s., so $\tilde{E}_{2}=\tilde{X}_{2} / \sqrt{1+\tilde{X}_{1}^{2}}$ a.s.. Now let $\left(X_{1}, X_{2}, E_{1}, E_{2}, E_{3}\right)$ be a solution of $\mathcal{M}$. By observational equivalence, $\left(\tilde{X}_{1}, \tilde{X}_{2}\right)$ has the same distribution as $\left(X_{1}, X_{2}\right)$, and thus $\tilde{E}_{2}$ is distributed as

$$
\frac{X_{2}}{\sqrt{1+\tilde{X}_{1}^{2}}}=\frac{\left(E_{1}+E_{3}\right) E_{3}+E_{2}}{\sqrt{1+\left(E_{1}+E_{3}\right)^{2}}} \text { a.s.. }
$$

This contradicts the fact that $\tilde{E}_{2}$ has a standard-normal distribution as, for example, the mean of the right-hand side is nonzero.

EXAMPLE D. 7 (Counterfactual density unidentifiable from observational and interventional densities [11]). Let $\rho \in \mathbb{R}$ and

$$
\mathcal{M}_{\rho}=\langle\mathbf{2}, \mathbf{2},\{0,1\} \times \mathbb{R},\{0,1\} \times \mathbb{R}^{2}, \boldsymbol{f}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle
$$

be the SCM with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad f_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{21}\left(1-x_{1}\right)+e_{22} x_{1}
$$

and $\mathbb{P}_{\boldsymbol{E}}=\mathbb{P}^{\left(E_{1}, \boldsymbol{E}_{2}\right)}$ with $E_{1} \sim \operatorname{Bernoulli}(1 / 2)$,

$$
\boldsymbol{E}_{2}:=\binom{E_{21}}{E_{22}} \sim \mathcal{N}\left(\mathbf{0},\binom{1 \rho}{\rho 1}\right)
$$

normally distributed and $E_{1} \perp \boldsymbol{E}_{2}$. In an epidemiological setting, this SCM could be used to model whether a patient was treated or not $\left(X_{1}\right)$ and the corresponding outcome for that patient $\left(X_{2}\right)$.

Suppose in the actual world we did not assign treatment to a patient $\left(X_{1}=0\right)$ and the outcome was $X_{2}=c \in \mathbb{R}$. Consider the counterfactual query "What would the outcome have been, if we had assigned treatment to this patient?". We can answer this question by introducing a parallel counterfactual world that is modeled by the twin SCM $\mathcal{M}_{\rho}^{\text {twin }}$, as depicted in Figure 11. The counterfactual query then asks for $p\left(X_{2^{\prime}}=x_{2^{\prime}} \mid \operatorname{do}\left(X_{1^{\prime}}=1, X_{1}=0\right), X_{2}=\right.$ c). One can calculate that

$$
\binom{X_{2^{\prime}}}{X_{2}} \mid \operatorname{do}\left(X_{1^{\prime}}=1, X_{1}=0\right) \sim \mathcal{N}\left(\mathbf{0},\binom{1 \rho}{\rho 1}\right)
$$

and hence $X_{2^{\prime}} \mid \operatorname{do}\left(X_{1^{\prime}}=1, X_{1}=0\right), X_{2}=c \sim \mathcal{N}\left(\rho c, 1-\rho^{2}\right)$. Note that the answer to the counterfactual query depends on a quantity $\rho$ that we cannot identify from the observational density $p\left(X_{1}, X_{2}\right)$ or the interventional densities $p\left(X_{2} \mid \operatorname{do}\left(X_{1}=0\right)\right)$ and $p\left(X_{2} \mid \operatorname{do}\left(X_{1}=\right.\right.$ 1)), none of which depends on $\rho$. Therefore, even data from randomized controlled trials combined with observational data would not suffice to determine the value of this particular counterfactual query. Indeed, SCMs $\mathcal{M}_{\rho}$ and $\mathcal{M}_{\rho^{\prime}}$ with $\rho \neq \rho^{\prime}$ are interventionally equivalent, but not counterfactually equivalent.

![img-11.jpeg](img-11.jpeg)

Fig 11: The augmented graph of the $S C M \mathcal{M}_{\rho}$ (left), its twin $S C M \mathcal{M}_{\rho}^{\text {twin }}$ (center) and the intervened twin SCM $\left(\mathcal{M}_{\rho}^{\text {twin }}\right)_{\operatorname{do}\left(\{1^{\prime}, 1\},(1,0)\right)}$ (right) of Example D.7.
![img-12.jpeg](img-12.jpeg)

Fig 12: The augmented graphs of SCMs $\tilde{\mathcal{M}}, \tilde{\mathcal{M}}, \mathcal{M}$, and $\tilde{\mathcal{M}}$ that appear in Examples 4.4, D.10, and D.13.

# Section 3 

EXAMPLE D. 8 (Mixtures of solutions are solutions). Let $\mathcal{M}=\langle\mathbf{1}, \emptyset, \mathbb{R}, \mathbf{1}, f, \mathbb{P}_{\mathbf{1}}\rangle$ be an SCM with causal mechanism $f: \mathcal{X} \times \mathcal{E} \rightarrow \mathcal{X}$ defined by $f(x, e)=x-x^{2}+1$. There exist only two measurable solution functions $g_{ \pm}: \mathcal{E} \rightarrow \mathcal{X}$ for $\mathcal{M}$, defined by $g_{ \pm}(e)= \pm 1$. Let $X: \Omega \rightarrow \mathbb{R}$ be a random variable that is a nontrivial mixture of point masses on $\{-1,+1\}$. Then $X$ is a solution of $\mathcal{M}$, however neither $g_{+}(E)=X$ a.s., nor $g_{-}(E)=X$ a.s., for any random variable $E$ such that $\mathbb{P}^{E}=\mathbb{P}_{\mathcal{E}}$.

EXAMPLE D. 9 (Solvability is not preserved under perfect intervention). Consider the $S C M \mathcal{M}=\left\langle\mathbf{2}, \emptyset, \mathbb{R}^{2}, \mathbf{1}, \boldsymbol{f}, \mathbb{P}_{\mathbf{1}}\right\rangle$ with the following causal mechanism

$$
f_{1}(\boldsymbol{x})=x_{1}+x_{1}^{2}-x_{2}+1, \quad f_{2}(\boldsymbol{x})=x_{2}\left(1-\mathbf{1}_{\{0\}}\left(x_{1}\right)\right)+1
$$

This SCM has a unique solution $(0,1)$. Doing a perfect intervention $\operatorname{do}\left(\{1\}, \xi_{1}\right)$ for some $\xi_{1} \neq 0$, however, leads to an intervened model $\mathcal{M}_{\operatorname{do}\left(\{1\}, \xi_{1}\right)}$ that is not solvable. Performing instead the perfect intervention $\operatorname{do}\left(\{2\}, \xi_{2}\right)$ for some $\xi_{2}>1$ leads also to a nonuniquely solvable SCM $\mathcal{M}_{\operatorname{do}\left(\{2\}, \xi_{2}\right)}$ which has solutions with multiple induced distributions, for example, $\left(X_{1}, X_{2}\right)=\left(\phi\left(\xi_{2}\right) \sqrt{\xi_{2}-1}, \xi_{2}\right)$ with some measurable $\phi: \mathbb{R} \rightarrow\{-1,+1\}$, but also mixtures of those.

## Section 4

EXAMPLE D. 10 (Counterfactually equivalent SCMs with different graphs). Consider the SCM $\tilde{\mathcal{M}}=\langle\mathbf{2}, \mathbf{2},\{-1,1\}^{2},\{-1,1\}^{2}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\rangle$ with causal mechanism given by $\tilde{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=$ $e_{1}$ and $\tilde{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{2}$, and $\mathbb{P}_{\boldsymbol{E}}=\mathbb{P}^{\boldsymbol{E}}$ with $E_{1}, E_{2} \sim \mathcal{U}(\{-1,1\})$ uniformly distributed and $E_{1} \Perp E_{2}$. Consider also the SCM $\mathcal{M}$ that is the same as $\tilde{\mathcal{M}}$ except for its causal mechanism, which is given by $f_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}$ and $f_{2}(\boldsymbol{x}, \boldsymbol{e})=e_{1} e_{2}$. Then $\mathcal{M}$ and $\tilde{\mathcal{M}}$ are counterfactually equivalent although $\mathcal{G}(\mathcal{M})$ is not equal to $\mathcal{G}(\tilde{\mathcal{M}})$ (see Figure 12).

## Section 5

Example D. 11 (Marginalization condition of an SCM is not a necessary condition). Consider the SCM $\mathcal{M}=\left\langle\mathbf{4}, \mathbf{1}, \mathbb{R}^{4}, \mathbb{R}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}}\right\rangle$ with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, e)=e, \quad f_{2}(\boldsymbol{x}, e)=x_{1}, \quad f_{3}(\boldsymbol{x}, e)=x_{2}, \quad f_{4}(\boldsymbol{x}, e)=x_{4}
$$

and $\mathbb{P}_{\mathbb{R}}$ is the standard-normal measure on $\mathbb{R}$. This SCM is solvable w.r.t. $\mathcal{L}=\{2,4\}$, but not uniquely solvable w.r.t. $\mathcal{L}$, and hence we cannot apply Definition 5.3 to $\mathcal{L}$. However, the SCM $\overline{\mathcal{M}}$ on the endogenous variables $\{1,3\}$ with the causal mechanism $\hat{\boldsymbol{f}}$ given by $\hat{f}_{1}(\boldsymbol{x}, e)=e$ and $\hat{f}_{3}(\boldsymbol{x}, e)=x_{1}$ is counterfactually equivalent to $\mathcal{M}$ w.r.t. $\{1,3\}$, which can be checked easily.

EXAMPLE D. 12 (Graph of the marginal SCM is a strict subgraph of the latent projection). Consider the SCM $\mathcal{M}=\left\langle\mathbf{3}, \mathbf{1}, \mathbb{R}^{3}, \mathbb{R}, \boldsymbol{f}, \mathbb{P}_{\mathbb{R}}\right\rangle$ with causal mechanism given by

$$
f_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}, \quad f_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1}-x_{3}, \quad f_{3}(\boldsymbol{x}, \boldsymbol{e})=x_{1}
$$

and take for $\mathbb{P}_{\mathbb{R}}$ the standard-normal measure on $\mathbb{R}$. In contrast, to the (augmented) graph of $\mathcal{M}$, there is no directed path in the (augmented) graph of the marginal $S C M \mathcal{M}_{\operatorname{marg}(\{3\})}$.

# Section 7 

Example D. 13 (Detecting a bidirected edge in the graph of an SCM). Consider the SCM $\overline{\mathcal{M}}=\left\langle\mathbf{2}, \mathbf{2},\{-1,1\}^{2},\{-1,1\}^{2}, \hat{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ with causal mechanism given by $\hat{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}$ and $\hat{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1} e_{2}$, and $\mathbb{P}_{\boldsymbol{\mathcal { E }}}=\mathbb{P}^{\boldsymbol{E}}$ with $E_{1}, E_{2} \sim \mathcal{U}(\{-1,1\})$ uniformly distributed and $E_{1} \Perp E_{2}$. Consider also the SCM $\overline{\mathcal{M}}$ that is the same as $\overline{\mathcal{M}}$ except for its causal mechanism, which is given by $\hat{f}_{1}(\boldsymbol{x}, \boldsymbol{e})=e_{1}$ and $\hat{f}_{2}(\boldsymbol{x}, \boldsymbol{e})=x_{1} e_{1}$. See Figure 12 for their augmented graphs. For the SCM $\overline{\mathcal{M}}$ we observe that the marginal interventional distribution $\mathbb{P}_{\overline{\mathcal{M}}_{\text {do }}(\{1\}, \xi_{1})}}\left(X_{2}=-1\right)$ is not equal to the conditional distribution $\mathbb{P}_{\overline{\mathcal{M}}}\left(X_{2}=-1 \mid X_{1}=\xi_{1}\right)$ for both $\xi_{1}=-1$ and $\xi_{1}=1$. This observation suffices to identify the presence of the bidirected edge $1 \leftrightarrow 2$ in the graph $\mathcal{G}(\overline{\mathcal{M}})$. For the SCM $\overline{\mathcal{M}}$, whose graph does not contain the bidirected edge $1 \leftrightarrow 2$, the marginal interventional distribution and conditional distribution coincide.

## APPENDIX E: PROOFS

This appendix contains the proofs of all the theoretical results in the appendices A, B and C, and the main text. Some of the proofs will rely on the measure theoretic terminology and results of Appendix F.

## E.1. Proofs of the appendices

## Appendix A

Proof of Lemma A.5. It suffices to show that for every $C$-d-open walk between $i$ and $j$ in $\mathcal{G}$, there exists a $C$-d-open path between $i$ and $j$ in $\mathcal{G}$. Take a $C$-d-open walk $\pi=(i=$ $\left.i_{0}, \ldots, i_{n}=j\right)$. If a node $\ell$ occurs more than once in $\pi$, let $i_{j}$ be the first occurrence of $\ell$ in $\pi$ and $i_{k}$ the last occurrence of $\ell$ in $\pi$. We now construct a new walk $\pi^{\prime}$ from $\pi$ by removing the subwalk between $i_{j}$ and $i_{k}$ of $\pi$ from $\pi$. It is easy to check that the new walk $\pi^{\prime}$ is still $C$-d-open. If $\ell$ is an endpoint on $\pi^{\prime}$, then $i_{j}$ or $i_{k}$ must be endpoint of $\pi$, and hence $\ell \notin C$. If $\ell$ is a non-endpoint non-collider on $\pi^{\prime}$, then also $i_{j}$ or $i_{k}$ must have been a non-endpoint non-collider on $\pi$, and hence $\ell \notin C$. If $\ell$ is a collider on $\pi^{\prime}$, then either (i) $i_{j}$ or $i_{k}$ are both colliders on $\pi$, and hence $\ell$ is ancestor of $C$ in $\mathcal{G}$, or (ii) on the subwalk between $i_{j}$ and $i_{k}$ that was removed, there must be a directed path in $\mathcal{G}$ from $i_{j}$ or $i_{k}$ to a collider in $\operatorname{an}_{\mathcal{G}}(C)$, and hence, $\ell$ is in $\operatorname{an}_{\mathcal{G}}(C)$. The other nodes on $\pi^{\prime}$ cannot be responsible for $C$-d-blocking the walk, since they also occur (together with their adjacent edges) on $\pi$ and they do not $C$-d-block $\pi$.

In $\pi^{\prime}$, the number of nodes that occur multiple times is at least one less than in $\pi$. Repeat this procedure until no repeated nodes are left.

Proof of ThEOREM A.7. The first case is a well known result. An elementary proof is obtained by noting that an acyclic system of structural equations trivially satisfies the local directed Markov property, and then apply [35, Proposition 4], followed by applying the stability of $d$-separation with respect to (graphical) marginalization [18, Lemma 2.2.15]. Alternatively, the result also follows from sequential application of Theorems 3.8.2, 3.8.11, 3.7.7, 3.7.2 and 3.3.3 (using Remark 3.3.4) in [18].

The discrete case is proved by the series of results Theorem 3.8.12, Remark 3.7.2, Theorem 3.6.6 and 3.5.2 in [18].

The linear case is proved in Example 3.8.17 in [18]. To connect the assumptions made there with the ones we state here, observe that under the linear transformation rule for Lebesgue measures, the image measure of $\mathbb{P}_{\mathcal{E}}$ under the linear mapping $\mathbb{R}^{\mathcal{J}} \rightarrow \mathbb{R}^{\mathcal{I}}: \boldsymbol{e} \mapsto \Gamma_{\mathcal{I} \mathcal{J}} \boldsymbol{e}$ gives a measure on $\mathcal{X}=\mathbb{R}^{\mathcal{I}}$ with a density w.r.t. the Lebesgue measure on $\mathbb{R}^{\mathcal{I}}$, as long as the image of the linear mapping is the entire $\mathbb{R}^{\mathcal{I}}$. This is guaranteed if each causal mechanism has a nontrivial dependence on some exogenous variable(s), that is, for each $i \in \mathcal{I}$ there is some $j \in \mathcal{J}$ with $\Gamma_{i j} \neq 0$.

Proof of Proposition A.12. This follows directly from the fact that the strongly connected components of $\mathcal{G}^{a}(\mathcal{M})$ form a DAG by Lemma A. 2 and that the directed edges in $\mathcal{G}^{a}(\operatorname{acy}(\mathcal{M}))$ by construction respect every topological ordering of that DAG. Both SCMs are observationally equivalent by construction.

Proof of Proposition A.14. This follows immediately from the Definitions A. 11 and A. 13 .

Proof of Lemma A.17. It suffices to show that for every $C$ - $\sigma$-open walk between $i$ and $j$ in $\mathcal{G}$, there exists a $C$ - $\sigma$-open path between $i$ and $j$ in $\mathcal{G}$. Let $\pi=\left(i=i_{0}, \ldots, i_{n}=j\right)$ be a $C$ - $\sigma$-open walk in $\mathcal{G}$. If a node $\ell$ occurs more than once in $\pi$, let $i_{j}$ be the first node in $\pi$ and $i_{k}$ the last node in $\pi$ that are in the same strongly connected component as $\ell$. Since $i_{j}$ and $i_{k}$ are in the same strongly connected component, there are directed paths $i_{j} \rightarrow \cdots \rightarrow i_{k}$ and $i_{k} \rightarrow \cdots \rightarrow i_{j}$ in $\mathcal{G}$. We now construct a new walk $\pi^{\prime}$ from $\pi$ by replacing the subwalk between $i_{j}$ and $i_{k}$ of $\pi$ by a particular directed path between $i_{j}$ and $i_{k}$ : (i) If $k=n$, or if $k<n$ and $i_{k} \rightarrow i_{k+1}$ on $\pi$, we replace it by a shortest directed path $i_{j} \rightarrow \cdots \rightarrow i_{k}$, otherwise (ii) we replace it by a shortest directed path $i_{j} \leftarrow \cdots \leftarrow i_{k}$. We now show that the new walk $\pi^{\prime}$ is still $C$ - $\sigma$-open.
$\pi^{\prime}$ cannot become $C$ - $\sigma$-blocked through one of the initial nodes $i_{0} \ldots i_{j-1}$ or one of the final nodes $i_{k+1} \ldots i_{n}$ on $\pi^{\prime}$, since these nodes occur in the same local configuration on $\pi$ and do not $C$ - $\sigma$-block $\pi$ by assumption. Furthermore, $\pi^{\prime}$ cannot become $C$ - $\sigma$-blocked through one of the nodes strictly between $i_{j}$ and $i_{k}$ on $\pi^{\prime}$ (if there are any), since these nodes are all non-endpoint non-colliders that only point to nodes in the same strongly connected component on $\pi^{\prime}$. Because $\pi$ is $C$ - $\sigma$-open, $i_{k} \notin C$ if $k=n$ or if $i_{k} \rightarrow i_{k+1}$ on $\pi$. This holds in particular in case (i). Similarly, $i_{j} \notin C$ if $j=0$ or $i_{j-1} \leftarrow i_{j}$ on $\pi$.

In case (i), $\pi^{\prime}$ is not $C$ - $\sigma$-blocked by $i_{k}$ because $i_{k}$ is a non-collider on $\pi^{\prime}$ but $i_{k} \notin C$. Also $i_{j}$ does not $C$ - $\sigma$-block $\pi^{\prime}$. Assume $i_{j} \neq i_{k}$ (otherwise there is nothing to prove). If $j=0$, or if $j>0$ and $i_{j-1} \leftarrow i_{j}$ on $\pi^{\prime}$, then the same holds for $\pi$ and hence $i_{j} \notin C ; i_{j}$ is then a noncollider on $\pi^{\prime}$, but $i_{j} \notin C$. If $j>0$ and $i_{j-1} \leftrightarrow i_{j}$ or $i_{j-1} \rightarrow i_{j}$ on $\pi^{\prime}$ then $i_{j}$ is a non-endpoint non-collider on $\pi^{\prime}$ that does not point to a node in another strongly connected component.

Now consider case (ii). If $j=0$ or $i_{j-1} \leftarrow i_{j}$ on $\pi^{\prime}$ then this case is analogous to case (i). So assume $j>0$ and $i_{j-1} \rightarrow i_{j}$ or $i_{j-1} \leftrightarrow i_{j}$ on $\pi^{\prime}$. If $i_{j}$ is an endpoint of $\pi^{\prime}$, then $i_{j}=i_{k}$ and $k=n$ and therefore $i_{k} \notin C$, and hence $i_{j}$ and $i_{k}$ do not $C$ - $\sigma$-block $\pi^{\prime}$. Otherwise, $i_{j}$ must be a collider on $\pi^{\prime}$ (whether $i_{j}=i_{k}$ or not). Then on the subwalk of $\pi$ between $i_{j}$ and $i_{k}$

there must be a directed path from $i_{j}$ to a collider that is ancestor of $C$, which implies that $i_{j}$ is itself ancestor of $C$, and hence $i_{j}$ does not $C$ - $\sigma$-block $\pi^{\prime}$. Also $i_{k}$ cannot $C$ - $\sigma$-block $\pi^{\prime}$. Assume $i_{j} \neq i_{k}$ (otherwise there is nothing to prove). Since $i_{k} \leftarrow i_{k+1}$ or $i_{k} \leftrightarrow i_{k+1}$ on $\pi^{\prime}, i_{k}$ is a non-endpoint non-collider on $\pi^{\prime}$ that does not point to a node in another strongly connected component.

Now in $\pi^{\prime}$, the number of nodes that occurs more than once is at least one less than in $\pi$. Repeat this procedure until no nodes occur more than once.

Proof of Proposition A.19. This follows directly as a special case of Corollary 2.8.4 in [18].

Proof of Theorem A.21. An SCM $\mathcal{M}$ that is uniquely solvable w.r.t. each strongly connected component is uniquely solvable and hence, by Theorem 3.6, all its solutions have the same observational distribution. The last statement follows from the series of results Theorem 3.8.2, 3.8.11, Lemma 3.7.7 and Remark 3.7.2 in [18]. Alternatively, we give here a shorter proof: Under the stated conditions one can always construct the acyclification $\operatorname{acy}(\mathcal{M})$ which is observationally equivalent to $\mathcal{M}$ and is acyclic (see Proposition A.12) and hence we can apply Theorem A. 7 to $\operatorname{acy}(\mathcal{M})$. Together with Proposition A. 14 and A. 19 this gives

$$
A \underset{\mathcal{G}(\mathcal{M})}{\stackrel{\sigma}{\mathcal{P}}} B \mid C \Longleftrightarrow A \underset{\operatorname{acy}(\mathcal{G}(\mathcal{M}))}{\stackrel{d}{\mathcal{Q}}}(B \mid C \Longrightarrow A \underset{\mathcal{G}(\operatorname{acy}(\mathcal{M}))}{\stackrel{d}{\mathcal{Q}}}(B \mid C \Longrightarrow \boldsymbol{X}_{A} \underset{\mathbb{P}_{\mathcal{M}}^{A}}{\mathbb{1}} \boldsymbol{X}_{B} \mid \boldsymbol{X}_{C}
$$

for $A, B, C \subseteq \mathcal{I}$ and $\boldsymbol{X}$ a solution of $\mathcal{M}$.
Proof of Corollary A.22. First observe that simplicity is preserved under both perfect intervention and the twin operation (see Proposition 8.2). Now the first statement follows from Theorem A. 21 if one takes into account the identities of Proposition 2.14 and 2.19. Similarly, the last statement follows from Theorem A.7.

Proof of Proposition A.32. Let $\tilde{\mathcal{M}}=:\left\langle\mathcal{V}, \hat{\mathcal{H}}, \boldsymbol{X}, \boldsymbol{\mathcal { E }}, \tilde{\boldsymbol{f}}, \mathbb{P}_{\boldsymbol{\mathcal { E }}}\right\rangle$ be the induced SCM. Observe that every loop $\mathcal{O} \in \mathcal{L}(\mathcal{G}(\tilde{\mathcal{M}}))$ is a loop in $\mathcal{L}(\mathcal{G})$. Fix $\check{\boldsymbol{x}} \in \boldsymbol{X}$ and $\check{\boldsymbol{e}} \in \boldsymbol{\mathcal { E }}$. For every $\mathcal{O} \in \mathcal{L}(\mathcal{G}(\tilde{\mathcal{M}}))$, define

$$
I_{\mathcal{O}}:=\left(\operatorname{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}\right) \backslash(\operatorname{pa}(\mathcal{O}) \backslash \mathcal{O}) \subseteq \tilde{\mathcal{I}}
$$

and

$$
J_{\mathcal{O}}:=\{\mathcal{F} \in \tilde{\mathcal{J}}: \mathcal{F} \cap \mathcal{O} \neq \emptyset\} \backslash \operatorname{pa}(\mathcal{O}) \subseteq \tilde{\mathcal{J}}
$$

Now, define the family of measurable mappings $\left(\tilde{\boldsymbol{g}}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\tilde{\mathcal{M}}))}$, where the mapping $\tilde{\boldsymbol{g}}_{\mathcal{O}}$ : $\boldsymbol{X}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ is given by

$$
\tilde{\boldsymbol{g}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right):=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \check{\boldsymbol{x}}_{I_{\mathcal{O}}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}, \check{\boldsymbol{e}}_{J_{\mathcal{O}}}\right)
$$

where $\boldsymbol{x}_{\mathrm{pa}_{\mathcal{G}}(\mathcal{O}) \backslash \mathcal{O}}=\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \check{\boldsymbol{x}}_{I_{\mathcal{O}}}\right)$ and $\widehat{\boldsymbol{e}}_{\mathcal{O}}=\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}, \check{\boldsymbol{e}}_{J_{\mathcal{O}}}\right)$. Observe that from the definition of the parents (see Definition 2.6) it follows that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$ we have

$$
\boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{f}}_{\mathcal{O}}\left(\boldsymbol{x}_{\backslash I_{\mathcal{O}}}, \check{\boldsymbol{x}}_{I_{\mathcal{O}}}, \boldsymbol{e}_{\backslash J_{\mathcal{O}}}, \check{\boldsymbol{e}}_{J_{\mathcal{O}}}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{f}}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

This, together with the fact that the family of mappings $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G})}$ is a compatible system of solution functions, implies that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$ we have

$$
\boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{g}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{f}}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

Hence, $\iota(\widehat{\mathcal{M}})$ is loop-wisely solvable and thus $\left(\tilde{\boldsymbol{g}}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\hat{\mathcal{M}}))}$ is a family of measurable solution functions. In particular, for all $\mathcal{O}, \tilde{\mathcal{O}} \in \mathcal{L}(\mathcal{G}(\hat{\mathcal{M}}))$ with $\tilde{\mathcal{O}} \subseteq \mathcal{O}$ and for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ we have

$$
\boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{g}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\tilde{\mathcal{O}}}=\tilde{\boldsymbol{g}}_{\tilde{\mathcal{O}}}\left(\boldsymbol{x}_{\mathrm{pa}(\tilde{\mathcal{O}}) \backslash \tilde{\mathcal{O}}}, \boldsymbol{e}_{\mathrm{pa}(\tilde{\mathcal{O}})}\right)
$$

From this we conclude that $\left(\tilde{\boldsymbol{g}}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\hat{\mathcal{M}}))}$ is a compatible system of solution functions.
Proof of Lemma A.33. Suppose $\mathcal{M}$ is loop-wisely uniquely solvable and consider a subset $\mathcal{O} \subseteq \mathcal{I}$. Consider the induced subgraph $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$ of $\mathcal{G}^{a}(\mathcal{M})$ on the nodes $\mathcal{O}$. Then every strongly connected component of $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$ is an element of $\mathcal{L}(\mathcal{G}(\mathcal{M}))$. Let $\mathcal{C}$ be such a strongly connected component in $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$, and let $\boldsymbol{g}_{\mathcal{C}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{C}) \backslash \mathcal{C}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{C})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{C}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{C}$. Since $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$ partitions into strongly connected components, we can recursively (by following a topological ordering of the DAG $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}^{\text {sc }}$ from Lemma A.2) insert these mappings into each other to obtain a mapping $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ that makes $\mathcal{M}$ uniquely solvable w.r.t. $\mathcal{O}$.

Proof of Proposition A.34. Let $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \in \mathcal{L}(\mathcal{G}(\mathcal{M}))}$ be any family of measurable solution functions, where $\boldsymbol{g}_{\mathcal{O}}$ is measurable solution function of $\mathcal{M}$ w.r.t. $\mathcal{O}$. Then, for $\mathcal{O}, \tilde{\mathcal{O}} \in$ $\mathcal{L}(\mathcal{G}(\mathcal{M}))$ such that $\tilde{\mathcal{O}} \subseteq \mathcal{O}$, we have that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e}) \quad \Longrightarrow \quad \boldsymbol{x}_{\tilde{\mathcal{O}}}=\boldsymbol{f}_{\tilde{\mathcal{O}}}(\boldsymbol{x}, \boldsymbol{e})
$$

This implies that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\tilde{\mathcal{O}}}=\boldsymbol{g}_{\tilde{\mathcal{O}}}\left(\boldsymbol{x}_{\mathrm{pa}(\tilde{\mathcal{O}}) \backslash \tilde{\mathcal{O}}}, \boldsymbol{e}_{\mathrm{pa}(\tilde{\mathcal{O}})}\right)
$$

Proof of Corollary 8.5. This follows directly from Proposition 7.1 and 7.2.

# Appendix B 

Proof of Proposition B.1. Let $\tilde{\boldsymbol{f}}: \boldsymbol{\mathcal { E }} \times \boldsymbol{\mathcal { X }} \rightarrow \boldsymbol{\mathcal { X }}$ be the causal mechanism of a structurally minimal SCM that is equivalent to $\mathcal{M}$ (see Proposition 2.11). In particular, for any $\boldsymbol{\epsilon}_{\backslash \mathrm{pa}(\mathcal{O})} \in \boldsymbol{\mathcal { E }}_{\backslash \mathrm{pa}(\mathcal{O})}$ and $\boldsymbol{\xi}_{\backslash \mathrm{pa}(\mathcal{O})} \in \boldsymbol{\mathcal { X }}_{\backslash \mathrm{pa}(\mathcal{O})}$, we have that for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ and all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$, $\tilde{\boldsymbol{f}}(\boldsymbol{x}, \boldsymbol{e})=\tilde{\boldsymbol{f}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{\xi}_{\backslash \mathrm{pa}(\mathcal{O})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{e}_{\backslash \mathrm{pa}(\mathcal{O})}\right)$. This means that we may also consider $\tilde{\boldsymbol{f}}$ as a mapping $\tilde{\boldsymbol{f}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O})} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}$.

Consider the set

$$
\tilde{\boldsymbol{\mathcal { S }}}:=\left\{\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{x}_{\mathcal{O}}\right) \in \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \times \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { X }}_{\mathcal{O}}: \boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{f}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)\right\}
$$

By similar reasoning as in the proof of Theorem 3.2, $\tilde{\boldsymbol{\mathcal { S }}}$ is measurable.
By assumption, for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x}_{\backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\backslash \mathcal{O}}$ the space $\left\{\boldsymbol{x}_{\mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathcal{O}}\right.$ : $\left.\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})\right\}$ is nonempty and $\sigma$-compact. By applying Lemma F. 10 to the canonical projection $\boldsymbol{p r}_{\boldsymbol{\mathcal { E }}_{\mathrm{pa}}(\mathcal{O})}: \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})}$ and using the equivalence of $\boldsymbol{f}$ and $\tilde{\boldsymbol{f}}$, we obtain that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})}}$-almost every $\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})} \in \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})}$ and for all $\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}$ the space

$$
\tilde{\boldsymbol{\mathcal { S }}}_{\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}\right)}:=\left\{\boldsymbol{x}_{\mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathcal{O}}: \boldsymbol{x}_{\mathcal{O}}=\tilde{\boldsymbol{f}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)\right\}
$$

is nonempty and $\sigma$-compact.

The second measurable selection theorem, Theorem F.9, now implies that there exists a measurable $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})}}$-almost every $\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})} \in$ $\boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})}$ and for all $\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}$

$$
\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)=\overline{\boldsymbol{f}}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right), \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)
$$

Once more applying Lemma F.10, we obtain that for $\mathbb{P}_{\boldsymbol{E}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \Longrightarrow \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

Hence $\mathcal{M}$ is solvable w.r.t. $\mathcal{O}$.
Proof of Proposition B.4. Without loss of generality, we assume that $\mathcal{M}$ is structurally minimal (see Proposition 2.11). Define $\mathcal{C}:=\mathcal{A} \cap \overline{\mathcal{A}}$ and $\mathcal{D}:=\mathcal{A} \cup \overline{\mathcal{A}}$. Let $\boldsymbol{g}_{\mathcal{A}}, \boldsymbol{g}_{\overline{\mathcal{A}}}$ be measurable solution functions for $\mathcal{M}$ w.r.t. $\mathcal{A}$ and $\overline{\mathcal{A}}$, respectively. Note that $\mathrm{pa}(\mathcal{C}) \backslash \mathcal{C} \subseteq$ $\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A}$ and similarly $\mathrm{pa}(\mathcal{C}) \backslash \mathcal{C} \subseteq \mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}$. Indeed, for $c \in \mathrm{pa}(\mathcal{C})$ : if $c \in \mathcal{O}$ then $c \in \mathcal{C}$ because $\mathcal{A}$ and $\overline{\mathcal{A}}$ are both ancestral in $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$, while if $c \notin \mathcal{O}$ then $c \notin \mathcal{A}$ and $c \notin \overline{\mathcal{A}}$. Hence by Lemma E.1, for $\mathbb{P}_{\boldsymbol{E}}$-almost all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\left(\boldsymbol{g}_{\mathcal{A}}\right)_{\mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right)=\left(\boldsymbol{g}_{\overline{\mathcal{A}}}\right)_{\mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right)
$$

Hence for $\mathbb{P}_{\boldsymbol{E}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\begin{aligned}
& \boldsymbol{x}_{\mathcal{D}}=\boldsymbol{f}_{\mathcal{D}}(\boldsymbol{x}, \boldsymbol{e}) \\
& \Longleftrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{A} \backslash \mathcal{C}}=\boldsymbol{f}_{\mathcal{A} \backslash \mathcal{C}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\mathcal{C}}=\boldsymbol{f}_{\mathcal{C}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\mathcal{C}}=\boldsymbol{f}_{\mathcal{C}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\overline{\mathcal{A}} \backslash \mathcal{C}}=\boldsymbol{f}_{\overline{\mathcal{A}} \backslash \mathcal{C}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{A} \backslash \mathcal{C}}=\left(\boldsymbol{g}_{\mathcal{A}}\right)_{\mathcal{A} \backslash \mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{A})}\right) \\
\boldsymbol{x}_{\mathcal{C}}=\left(\boldsymbol{g}_{\mathcal{A}}\right)_{\mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right) \\
\boldsymbol{x}_{\mathcal{C}}=\left(\boldsymbol{g}_{\overline{\mathcal{A}}}\right)_{\mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right) \\
\boldsymbol{x}_{\overline{\mathcal{A}} \backslash \mathcal{C}}=\left(\boldsymbol{g}_{\overline{\mathcal{A}}}\right)_{\overline{\mathcal{A}} \backslash \mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right) \\
\Longleftrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{A}}=\boldsymbol{g}_{\mathcal{A}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{A})}\right) \\
\boldsymbol{x}_{\overline{\mathcal{A}}}=\boldsymbol{g}_{\overline{\mathcal{A}}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right)
\end{array}\right.
\end{aligned}
$$

Now $\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A} \subseteq \mathrm{pa}(\mathcal{D}) \backslash \mathcal{D}$, and similarly, $\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}} \subseteq \mathrm{pa}(\mathcal{D}) \backslash \mathcal{D}$. Hence, we conclude that the mapping $\boldsymbol{h}_{\mathcal{D}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{D}) \backslash \mathcal{D}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{D})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{D}}$ defined by

$$
\begin{aligned}
& \boldsymbol{h}_{\mathcal{D}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{D}) \backslash \mathcal{D}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{D})}\right):= \\
& \quad\left(\left(\boldsymbol{g}_{\mathcal{A}}\right)_{\overline{\mathcal{A}} \backslash \mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{A})}\right),\left(\boldsymbol{g}_{\mathcal{A}}\right)_{\mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{A}) \backslash \mathcal{A}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{A})}\right),\left(\boldsymbol{g}_{\overline{\mathcal{A}}}\right)_{\overline{\mathcal{A}} \backslash \mathcal{C}}\left(\boldsymbol{x}_{\mathrm{pa}(\overline{\mathcal{A}}) \backslash \overline{\mathcal{A}}}, \boldsymbol{e}_{\mathrm{pa}(\overline{\mathcal{A}})}\right)\right)
\end{aligned}
$$

is a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{D}$, and that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{D}$.

Proof of Corollary B.5. It suffices to show the implication to the left. We have to show that $\mathcal{M}$ is uniquely solvable w.r.t. each ancestral subset of $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$. The proof proceeds via induction with respect to the size of the ancestral subset. For ancestral subsets of size 0 , the claim is trivially true. Ancestral subsets of size 1 must be of the form $\{i\}=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(i)$ for $i \in \mathcal{O}$ and hence the claim is true by assumption. Assume that the claim holds for all

ancestral subsets of size $\leq n$. Let $\mathcal{A}$ be an ancestral subset of $\mathcal{G}(\mathcal{M})_{\mathcal{O}}$ of size $n+1$. If $\mathcal{A}=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(i)$ for some $i \in \mathcal{O}$ then the claim holds for $\mathcal{A}$ by assumption. Otherwise, $\mathcal{A}=\bigcup_{i \in \mathcal{A}} \operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(i)$ is a union of ancestral subsets of size $\leq n$. Choose distinct elements $\left\{i_{1}, \ldots, i_{k}\right\} \subseteq \mathcal{A}$ where $k$ is the smallest integer such that $\bigcup_{j=1}^{k} \operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}\left(i_{j}\right)=\mathcal{A}$. By applying Proposition B. 4 to $\bigcup_{j=1}^{k-1} \operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}\left(i_{j}\right)$ and $\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}\left(i_{k}\right)$, thereby noting that the intersection of these two sets is an ancestral subset of size $\leq n$ and making use of the induction hypothesis, we arrive at the conclusion that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{A}$.

# Appendix C 

Proof of Proposition C.2. Let $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and $\boldsymbol{x}_{\mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathcal{O}}$. For $\boldsymbol{x}_{\mathcal{L}} \in \boldsymbol{\mathcal { X }}$,

$$
\begin{aligned}
& \boldsymbol{x}_{\mathcal{L}}=\boldsymbol{f}_{\mathcal{L}}(\boldsymbol{x}, \boldsymbol{e}) \\
& \Longleftrightarrow \boldsymbol{x}_{\mathcal{L}}=B_{\mathcal{L} \mathcal{L}} \boldsymbol{x}_{\mathcal{L}}+B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e} \\
& \Longleftrightarrow \mathcal{A}_{\mathcal{L} \mathcal{L}} \boldsymbol{x}_{\mathcal{L}}=B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e} \\
& \Longleftrightarrow\left\{\begin{array}{l}
A_{\mathcal{L} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{+}\left(B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}\right)=B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e} \\
\exists_{\boldsymbol{v} \in \boldsymbol{X}_{\mathcal{L}}}: \boldsymbol{x}_{\mathcal{L}}=A_{\mathcal{L} \mathcal{L}}^{+}\left(B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}\right)+\left[\mathbb{I}_{\mathcal{L}}-A_{\mathcal{L} \mathcal{L}}^{+} A_{\mathcal{L} \mathcal{L}}\right] \boldsymbol{v}
\end{array}\right.
\end{aligned}
$$

where the last equivalence follows from [Theorem 2, 54].
Proof of Proposition C.3. $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if for $\mathbb{P}_{\mathcal{E}}$ almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x}_{\mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ the linear system of equations

$$
\begin{aligned}
\boldsymbol{x}_{\mathcal{L}} & =\boldsymbol{f}_{\mathcal{L}}(\boldsymbol{x}, \boldsymbol{e}) \\
\Longleftrightarrow \boldsymbol{x}_{\mathcal{L}} & =B_{\mathcal{L} \mathcal{L}} \boldsymbol{x}_{\mathcal{L}}+B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e} \\
\Longleftrightarrow & A_{\mathcal{L} \mathcal{L}} \boldsymbol{x}_{\mathcal{L}}=B_{\mathcal{L} \mathcal{O}} \boldsymbol{x}_{\mathcal{O}}+\Gamma_{\mathcal{L} \mathcal{J}} \boldsymbol{e}
\end{aligned}
$$

has a unique solution $\boldsymbol{x}_{\mathcal{L}} \in \mathcal{X}_{\mathcal{L}}$. Hence, $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if $A_{\mathcal{L} \mathcal{L}}$ is invertible.

Proof of Proposition C.4. It suffices to show $(1) \Longrightarrow(2)$ and $(1) \Longleftrightarrow(3)$. We start by showing that $(1) \Longrightarrow(2)$. Let $\mathcal{V} \subseteq \mathcal{L}$ and denote $\mathcal{U}:=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{L}}}(\mathcal{V})$, then we need to show that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{U}$. From Proposition C. 3 we know that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if the matrix $A_{\mathcal{L} \mathcal{L}}=\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$ is invertible. The matrix $A_{\mathcal{L} \mathcal{L}}$ is invertible if and only if the rows of $A_{\mathcal{L} \mathcal{L}}$ are all linearly independent. In particular, the rows of $A_{\mathcal{U} \mathcal{L}}$ are all linearly independent. Because $A_{\mathcal{U} \mathcal{L}}=\left[A_{\mathcal{U} \mathcal{U}} Z_{\mathcal{U} \mathcal{L}}\right]$, where $Z_{\mathcal{U} \mathcal{L}}$ is the zero matrix, we know that the rows of $A_{\mathcal{U} \mathcal{U}}=\mathbb{I}_{\mathcal{U}}-B_{\mathcal{U} \mathcal{U}}$ are also all linearly independent, and hence $A_{\mathcal{U} \mathcal{U}}$ is invertible.

Next, we show that $(1) \Longleftrightarrow(3)$. Observe that the strongly connected components of $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$ form a partition of the set $\mathcal{L}$ and that the directed mixed graph $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$ and the directed graph $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{L}}$ have the same strongly connected components. Because, by Lemma A.2, the graph of strongly connected components $\mathcal{G}^{\mathrm{sc}}$ of the directed graph $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{L}}$ is a DAG, the square matrix $B_{\mathcal{L} \mathcal{L}}$ can be permuted to an upper triangular block matrix $\tilde{B}_{\mathcal{L} \mathcal{L}}$, where for each diagonal block $\tilde{B}_{\mathcal{V} \mathcal{V}}$ of $\tilde{B}_{\mathcal{L} \mathcal{L}}$ the set of nodes $\mathcal{V}$ is a strongly connected component in $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$.

Without loss of generality we assume now that $B_{\mathcal{L} \mathcal{L}}$ is an upper triangular block matrix. From Proposition C. 3 it follows that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if the matrix $A_{\mathcal{L} \mathcal{L}}=\mathbb{I}_{\mathcal{L}}-B_{\mathcal{L} \mathcal{L}}$ is invertible. Because $B_{\mathcal{L} \mathcal{L}}$ is an upper triangular block matrix, we know that $A_{\mathcal{L} \mathcal{L}}$ is an upper triangular block matrix, where for each diagonal block $A_{\mathcal{V} \mathcal{V}}$ of $A_{\mathcal{L} \mathcal{L}}$

the set of nodes $\mathcal{V}$ is a strongly connected component in $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$. Since an upper triangular block matrix $A_{\mathcal{L} \mathcal{L}}$ is invertible if and only if every diagonal block in $A_{\mathcal{L} \mathcal{L}}$ is invertible, we have that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$ if and only if $\mathcal{M}$ is uniquely solvable w.r.t. each strongly connected component in $\mathcal{G}(\mathcal{M})_{\mathcal{L}}$.

Proof of Proposition C.5. By the definition of marginalization and Proposition C. 3 the marginal causal mechanism $\hat{\boldsymbol{f}}$ is given by

$$
\begin{aligned}
\hat{\boldsymbol{f}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right) & :=\boldsymbol{f}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right), \boldsymbol{e}\right) \\
& =B_{\mathcal{O O}} \boldsymbol{x}_{\mathcal{O}}+B_{\mathcal{O} \mathcal{L}} \boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)+\Gamma_{\mathcal{O} \mathcal{J}} \boldsymbol{e} \\
& =\left[B_{\mathcal{O O}}+B_{\mathcal{O} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{-1} B_{\mathcal{L} \mathcal{O}}\right] \boldsymbol{x}_{\mathcal{O}}+\left[B_{\mathcal{O} \mathcal{L}} A_{\mathcal{L} \mathcal{L}}^{-1} \Gamma_{\mathcal{L} \mathcal{J}}+\Gamma_{\mathcal{O} \mathcal{J}}\right] \boldsymbol{e}
\end{aligned}
$$

From Propositions C. 4 and 5.11 it follows that the marginalization respects the latent projection.

# E.2. Proofs of the main text 

## Section 2

Proof of Proposition 2.11. Let $i \in \mathcal{I}$. Note that Definition 2.6 can alternatively be formulated as follows: for $k \in \mathcal{I} \cup \mathcal{J}, k \notin \mathrm{pa}(i)$ if and only if there exists a measurable mapping $\hat{f}_{i}: \boldsymbol{X} \times \mathcal{E} \rightarrow \mathcal{X}_{i}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$,

$$
x_{i}=f_{i}(\boldsymbol{x}, \boldsymbol{e}) \Longleftrightarrow x_{i}=\hat{f}_{i}(\boldsymbol{x}, \boldsymbol{e})
$$

and either $k \in \mathcal{I}$ and there exists $\hat{x}_{k} \in \mathcal{X}_{k}$ such that $\hat{f}_{i}(\boldsymbol{x}, \boldsymbol{e})=\hat{f}_{i}\left(\boldsymbol{x}_{\backslash k}, \hat{x}_{k}, \boldsymbol{e}\right)$ for all $\boldsymbol{x} \in$ $\boldsymbol{X}, \boldsymbol{e} \in \mathcal{E}$, or $k \in \mathcal{J}$ and there exists $\hat{e}_{k} \in \mathcal{E}_{k}$ such that $\hat{f}_{i}(\boldsymbol{x}, \boldsymbol{e})=\hat{f}_{i}\left(\boldsymbol{x}, \boldsymbol{e}_{\backslash k}, \hat{e}_{k}\right)$ for all $\boldsymbol{x} \in \boldsymbol{X}, \boldsymbol{e} \in \mathcal{E}$. By repeatedly applying (this formulation of) Definition 2.6 to all $k \notin \mathrm{pa}(i)$, we obtain the existence of a measurable mapping $\tilde{f}_{i}: \boldsymbol{X} \times \mathcal{E} \rightarrow \mathcal{X}_{i}$ and $\tilde{\boldsymbol{x}}_{\backslash \mathrm{pa}(i)} \in \boldsymbol{X}_{\backslash \mathrm{pa}(i)}$, $\tilde{\boldsymbol{e}}_{\backslash \mathrm{pa}(i)} \in \boldsymbol{\mathcal { E }}_{\backslash \mathrm{pa}(i)}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$,

$$
x_{i}=f_{i}(\boldsymbol{x}, \boldsymbol{e}) \Longleftrightarrow x_{i}=\tilde{f}_{i}(\boldsymbol{x}, \boldsymbol{e})
$$

and for all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$,

$$
\tilde{f}_{i}(\boldsymbol{x}, \boldsymbol{e})=\tilde{f}_{i}\left(\boldsymbol{x}_{\mathrm{pa}(i)}, \tilde{\boldsymbol{x}}_{\backslash \mathrm{pa}(i)}, \boldsymbol{e}_{\mathrm{pa}(i)}, \tilde{\boldsymbol{e}}_{\backslash \mathrm{pa}(i)}\right)
$$

Define the SCM $\tilde{\mathcal{M}}$ as $\mathcal{M}$ except that its causal mechanism is $\tilde{\boldsymbol{f}}$ instead of $\boldsymbol{f}$. Then $\tilde{\mathcal{M}}$ is structurally minimal and equivalent to $\mathcal{M}$.

Proof of Proposition 2.14. The $\operatorname{do}\left(I, \boldsymbol{\xi}_{I}\right)$ operation on $\mathcal{M}$ completely removes the functional dependence on $\boldsymbol{x}$ and $\boldsymbol{e}$ from the $f_{i}$ components for $i \in I$ and hence the corresponding incoming directed and bidirected edges on nodes in $I$ from the (augmented) graph.

Proof of Proposition 2.15. The first statement follows from Definitions 2.12 and 2.13. For the second statement, note that a perfect intervention can only remove parental relations, and therefore will never introduce a cycle.

Proof of Proposition 2.19. This follows directly from Definitions 2.17 and 2.18.

Proof of Proposition 2.20. The additional edges introduced by the twin operation cannot lead to a directed cycle involving both copied and original nodes, because there are no edges pointing from copied nodes to original nodes (i.e., of the form $i^{\prime} \rightarrow v$ with $i^{\prime} \in I^{\prime}$ and $v \in \mathcal{V}$ ). Directed cycles involving only original nodes are absent by assumption, and directed cycles involving only copied nodes as well since they would correspond with a directed cycle in the original directed graph.

Proof of Proposition 2.21. It suffices to prove the property for directed graphs, since the property for SCMs follows directly from Definitions 2.12 and 2.17.

Applying the intervention do $(I)$ on the graph $\mathcal{G}$ removes all the incoming edges from the nodes in $I$. Now, if we perform the twin operation w.r.t. $\mathcal{I}$ on this graph $\operatorname{do}(I)(\mathcal{G})$, then we copy the same edges as if we had twinned the graph $\mathcal{G}$ w.r.t. $\mathcal{I}$, except those edges that do point to one of the nodes in $I$. Hence, if we apply the intervention $\operatorname{do}\left(I \cup I^{\prime}\right)$ on the graph $\operatorname{twin}(\mathcal{I})(\mathcal{G})$, which removes all incoming edges of both $I$ and its copy $I^{\prime}$, then we clearly obtain the same graph.

# Section 3 

Proof of Theorem 3.2. First we define the solution space $\mathcal{S}(\mathcal{M})$ of $\mathcal{M}$ by

$$
\mathcal{S}(\mathcal{M}):=\{(\boldsymbol{e}, \boldsymbol{x}) \in \mathcal{E} \times \mathcal{X}: \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})\}
$$

This is a measurable set, since $\mathcal{S}(\mathcal{M})=\boldsymbol{h}^{-1}(\Delta)$, where $\boldsymbol{h}: \mathcal{E} \times \mathcal{X} \rightarrow \mathcal{X} \times \mathcal{X}$ is the measurable mapping defined by $\boldsymbol{h}(\boldsymbol{e}, \boldsymbol{x})=(\boldsymbol{x}, \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e}))$ and $\Delta$ is the set defined by $\{(\boldsymbol{x}, \boldsymbol{x}): \boldsymbol{x} \in$ $\mathcal{X}\}$, which is measurable since $\mathcal{X}$ is Hausdorff. Note that

$$
\mathcal{A}:=\boldsymbol{p} \boldsymbol{r}_{\mathcal{E}}(\mathcal{S}(\mathcal{M}))=\{\boldsymbol{e} \in \mathcal{E}: \exists \boldsymbol{x} \in \mathcal{X} \text { s.t. } \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})\}
$$

is an analytic set because the projection $\boldsymbol{p r}_{\mathcal{E}}: \mathcal{X} \times \mathcal{E} \rightarrow \mathcal{E}$ is a measurable mapping between standard measurable spaces (Lemma F.3).

Suppose that (1) holds, that is, $\mathcal{M}$ has a solution. Then there exists a pair of random variables $(\boldsymbol{E}, \boldsymbol{X}): \Omega \rightarrow \mathcal{E} \times \mathcal{X}$ such that $\boldsymbol{X}=\boldsymbol{f}(\boldsymbol{X}, \boldsymbol{E}) \mathbb{P}$-a.s.. Note that

$$
\begin{aligned}
\{\omega \in \Omega: \boldsymbol{X}(\omega)=\boldsymbol{f}(\boldsymbol{X}(\omega), \boldsymbol{E}(\omega))\} & \subseteq\{\omega \in \Omega: \exists \boldsymbol{x} \in \mathcal{X} \text { s.t. } \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{E}(\omega))\} \\
& \subseteq \boldsymbol{E}^{-1}(\{\boldsymbol{e} \in \mathcal{E}: \exists \boldsymbol{x} \in \mathcal{X} \text { s.t. } \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})\}) \\
& =\boldsymbol{E}^{-1}(\mathcal{A})
\end{aligned}
$$

By Lemma F.6, $\mathcal{A}$ is $\mathbb{P}^{\boldsymbol{E}}$-measurable because it is analytic, and we can write $\mathcal{A}=\mathcal{B} \dot{\cup} \mathcal{N}$ with $\mathcal{B} \subseteq \mathcal{E}$ measurable and $\mathcal{N}$ a $\mathbb{P}^{\boldsymbol{E}}$-null set. Hence $\boldsymbol{E}^{-1}(\mathcal{A})=\boldsymbol{E}^{-1}(\mathcal{B}) \cup \boldsymbol{E}^{-1}(\mathcal{N})$ where $\boldsymbol{E}^{-1}(\mathcal{N})$ is a $\mathbb{P}$-null set. Therefore,

$$
\boldsymbol{E}^{-1}(\mathcal{B}) \supseteq\{\omega \in \Omega: \boldsymbol{X}(\omega)=\boldsymbol{f}(\boldsymbol{X}(\omega), \boldsymbol{E}(\omega))\} \backslash \boldsymbol{E}^{-1}(\mathcal{N})
$$

which implies that $\mathbb{P}\left(\boldsymbol{E}^{-1}(\mathcal{B})\right)=1$. Hence, $\mathcal{E} \backslash \mathcal{A}$ is a $\mathbb{P}_{\mathcal{E}}$-null set. In other words, for $\mathbb{P}_{\mathcal{E}^{-}}$ almost every $\boldsymbol{e} \in \mathcal{E}$ the structural equations $\boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})$ have a solution $\boldsymbol{x} \in \mathcal{X}$, that is, (2) holds.

Suppose that (2) holds. Then $\mathcal{E} \backslash \boldsymbol{p r}_{\mathcal{E}}(\mathcal{S}(\mathcal{M}))$ is a $\mathbb{P}_{\mathcal{E}}$-null set. By application of the measurable selection theorem F.8, there exists a measurable $\boldsymbol{g}: \mathcal{E} \rightarrow \mathcal{X}$ such that for $\mathbb{P}_{\mathcal{E}^{-}}$ almost all $\boldsymbol{e} \in \mathcal{E}, \boldsymbol{g}(\boldsymbol{e})=\boldsymbol{f}(\boldsymbol{g}(\boldsymbol{e}), \boldsymbol{e})$. Hence, there exists a measurable mapping $\boldsymbol{g}: \mathcal{E} \rightarrow \mathcal{X}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$

$$
\boldsymbol{x}=\boldsymbol{g}(\boldsymbol{e}) \quad \Longrightarrow \quad \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e})
$$

which we call property (A). Let $\check{\boldsymbol{f}}: \boldsymbol{\mathcal { E }} \times \boldsymbol{\mathcal { X }} \rightarrow \boldsymbol{\mathcal { X }}$ be the causal mechanism of a structurally minimal SCM that is equivalent to $\mathcal{M}$ (see Proposition 2.11). In particular, for any $\boldsymbol{\epsilon}_{\backslash \mathrm{pa}(\mathcal{I})} \in$ $\mathcal{E}_{\backslash \mathrm{pa}(\mathcal{I})}$, we have that $\check{\boldsymbol{f}}(\boldsymbol{x}, \boldsymbol{e})=\check{\boldsymbol{f}}\left(\boldsymbol{x}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}, \boldsymbol{\epsilon}_{\backslash \mathrm{pa}(\mathcal{I})}\right)$ for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ and all $\boldsymbol{e} \in \mathcal{E}$. This means that we may also consider $\check{\boldsymbol{f}}$ as a mapping $\check{\boldsymbol{f}}: \boldsymbol{\mathcal { X }} \times \mathcal{E}_{\mathrm{pa}(\mathcal{I})} \rightarrow \boldsymbol{\mathcal { X }}$. By applying Lemma F. 10 to the canonical projection $\boldsymbol{p r}_{\mathcal{E}_{\mathrm{pa}}(\mathcal{I})}: \mathcal{E} \rightarrow \mathcal{E}_{\mathrm{pa}(\mathcal{I})}$ and using the equivalence of $\boldsymbol{f}$ and $\check{\boldsymbol{f}}$, we obtain that for $\mathbb{P}_{\mathcal{E}_{\mathrm{pa}(\mathcal{I})}}$-almost all $\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})} \in \mathcal{E}_{\mathrm{pa}(\mathcal{I})}$ there exists $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ with $\boldsymbol{x}=\check{\boldsymbol{f}}\left(\boldsymbol{x}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)$. By applying the implication (2) $\Longrightarrow(\mathrm{A})$ to $\mathcal{E}_{\mathrm{pa}(\mathcal{I})}$ and $\check{\boldsymbol{f}}$, we conclude the existence of a measurable $\boldsymbol{g}: \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{I})} \rightarrow \boldsymbol{\mathcal { X }}$ such that for $\mathbb{P}_{\mathcal{E}_{\mathrm{pa}(\mathcal{I})}}$-almost all $\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})} \in \mathcal{E}_{\mathrm{pa}(\mathcal{I})}, \boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)=$ $\check{\boldsymbol{f}}\left(\boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right), \boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)$. Once more using Lemma F.10, we obtain that for $\mathbb{P}_{\mathcal{E}}$-almost all $\boldsymbol{e} \in \mathcal{E}$, $\boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)=\boldsymbol{f}\left(\boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right), \boldsymbol{e}\right)$. In other words, (3) holds.

Lastly, suppose that (3) holds, that is there exists a measurable solution function $\boldsymbol{g}$ : $\mathcal{E}_{\mathrm{pa}(\mathcal{I})} \rightarrow \mathcal{X}$. Then the measurable mappings $\boldsymbol{E}: \mathcal{E} \rightarrow \mathcal{E}$ and $\boldsymbol{X}: \mathcal{E} \rightarrow \mathcal{X}$, defined by $\boldsymbol{E}(\boldsymbol{e}):=\boldsymbol{e}$ and $\boldsymbol{X}(\boldsymbol{e}):=\boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)$, respectively, define a pair of random variables $(\boldsymbol{X}, \boldsymbol{E})$ such that $\boldsymbol{X}=\boldsymbol{f}(\boldsymbol{X}, \boldsymbol{E})$ holds a.s. and hence $(\boldsymbol{X}, \boldsymbol{E})$ is a solution. Hence (1) holds.

Proof of Proposition 3.4. Let $\check{\boldsymbol{f}}: \boldsymbol{\mathcal { E }} \times \boldsymbol{\mathcal { X }} \rightarrow \boldsymbol{\mathcal { X }}$ be the causal mechanism of a structurally minimal SCM $\tilde{\mathcal{M}}$ that is equivalent to $\mathcal{M}$ (see Proposition 2.11). For a subset $\mathcal{O} \subseteq \mathcal{I}$ consider the induced subgraph $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$ of the augmented graph $\mathcal{G}^{a}(\mathcal{M})$ on $\mathcal{O}$. Then the acyclicity of $\mathcal{G}^{a}(\mathcal{M})$ implies that the induced subgraph $\mathcal{G}^{a}(\mathcal{M})_{\mathcal{O}}$ is acyclic, and hence there exists a topological ordering on the nodes $\mathcal{O}$. We can substitute the components $\tilde{f}_{i}$ of the causal mechanism $\check{\boldsymbol{f}}$ for $i \in \mathcal{O}$ into each other along this topological ordering. This gives a measurable solution function $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ for $\tilde{\mathcal{M}}$, and hence for $\mathcal{M}$. It is clear from the acyclic structure that this mapping $\boldsymbol{g}_{\mathcal{O}}$ is independent of the choice of the topological ordering and is the only solution function for $\mathcal{M}$. Therefore, $\tilde{\mathcal{M}}$ is uniquely solvable w.r.t. $\mathcal{O}$, and so is $\mathcal{M}$.

Proof of Proposition 3.7. This follows immediately from Definitions 2.7 and 3.3.

Proof of Theorem 3.6. Suppose that (1) holds. By Proposition B. 1 there exists a measurable solution function $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ for $\mathcal{M}$ w.r.t. $\mathcal{O}$. Then for $\mathbb{P}_{\mathcal{E}^{-}}$ almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x}_{\backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\backslash \mathcal{O}}$ we have that $\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)$ is a solution of $\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})$. Hence, because of (1), for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x}_{\backslash \mathcal{O}} \in \boldsymbol{\mathcal { X }}_{\backslash \mathcal{O}}$ we have that $\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})$ implies $\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)$. Thus, $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{O}$, that is, (2) holds.

Suppose that (2) holds. Let $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{O}$. Then, for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

This implies (1).
For the last statement, assume that $\mathcal{M}$ is uniquely solvable. Let $\boldsymbol{g}: \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{I})} \rightarrow \boldsymbol{\mathcal { X }}$ be a measurable solution function. Then there exists a measurable set $\boldsymbol{B} \subseteq \mathcal{E}$ with $\mathbb{P}_{\mathcal{E}}(\boldsymbol{B})=1$ and for all $\boldsymbol{e} \in \boldsymbol{B}$,

$$
\forall \boldsymbol{x} \in \boldsymbol{\mathcal { X }}: \boldsymbol{x}=\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{e}) \Longrightarrow \boldsymbol{x}=\boldsymbol{g}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{I})}\right)
$$

The existence of a solution for $\mathcal{M}$ follows directly from Theorem 3.2. Each solution $(\boldsymbol{X}, \boldsymbol{E})$ : $\Omega \rightarrow \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }}$ of $\mathcal{M}$ satisfies $\boldsymbol{X}(\omega)=\boldsymbol{f}(\boldsymbol{X}(\omega), \boldsymbol{E}(\omega)) \mathbb{P}$-a.s.. In addition, it satisfies $\boldsymbol{E}(\omega) \in$ $\boldsymbol{B} \mathbb{P}$-a.s., since $\mathbb{P} \circ \boldsymbol{E}^{-1}=\mathbb{P}_{\mathcal{E}}$. Hence, it satisfies $\boldsymbol{X}(\omega)=\boldsymbol{g}\left(\boldsymbol{E}(\omega)_{\mathrm{pa}(\mathcal{I})}\right) \mathbb{P}$-a.s.. Thus for every solution $(\boldsymbol{X}, \boldsymbol{E})$ the associated observational distribution is the push-forward of $\mathbb{P}_{\mathcal{E}}$ under $\boldsymbol{g} \circ \boldsymbol{p r}_{\mathrm{pa}(\mathcal{I})}$.

Proof of Proposition 3.8. Let $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{O}$. Then the mapping $\tilde{\boldsymbol{g}}_{\mathcal{O} \cup I}: \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O} \cup I}$ defined by $\tilde{\boldsymbol{g}}_{\mathcal{O} \cup I}\left(\boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right):=\left(\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{\xi}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right), \boldsymbol{\xi}_{I}\right)$ is a measurable solution function for the SCM $\mathcal{M}_{\operatorname{do}\left(I, \xi_{I}\right)}$ w.r.t. $\mathcal{O} \cup I$. If $\mathcal{M}$ is (uniquely) solvable w.r.t. $\mathcal{O}$, then it follows that $\mathcal{M}_{\operatorname{do}\left(I, \xi_{I}\right)}$ is (uniquely) solvable w.r.t. $\mathcal{O} \cup I$.

Proof of Proposition 3.10. It suffices to show that solvability of $\mathcal{M}$ w.r.t. $\mathcal{O}$ implies ancestral solvability w.r.t. $\mathcal{O}$. Solvability of $\mathcal{M}$ w.r.t. $\mathcal{O}$ implies that there exists a measurable mapping $\boldsymbol{g}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{g}_{\mathcal{O}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
$$

Let $\tilde{\boldsymbol{f}}: \boldsymbol{\mathcal { E }} \times \boldsymbol{\mathcal { X }} \rightarrow \boldsymbol{\mathcal { X }}$ be the causal mechanism of a structurally minimal SCM $\tilde{\mathcal{M}}$ that is equivalent to $\mathcal{M}$ (see Proposition 2.11). Let $\mathcal{P}:=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})$ for some $\mathcal{A} \subseteq \mathcal{O}$. Then for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{P}}=\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \\
\boldsymbol{x}_{\mathcal{O} \backslash \mathcal{P}}=\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{O} \backslash \mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)
\end{array} \Longrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{P}}=\tilde{\boldsymbol{f}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right) \\
\boldsymbol{x}_{\mathcal{O} \backslash \mathcal{P}}=\tilde{\boldsymbol{f}}_{\mathcal{O} \backslash \mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O} \backslash \mathcal{P})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O} \backslash \mathcal{P})}\right)
\end{array}\right.\right.
$$

Since $\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P} \subseteq \mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}$, we have that in particular for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{P}}=\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{P}}=\tilde{\boldsymbol{f}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right)
$$

This implies that the mapping $\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{P}}$ cannot depend on elements different from $\mathrm{pa}(\mathcal{P})$. Moreover, it follows from the definition of $\mathcal{P}$ that $(\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}) \cap \mathrm{pa}(\mathcal{P})=\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}$ and thus we have $\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}=(\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}) \cup(\mathrm{pa}(\mathcal{O}) \backslash(\mathcal{O} \cup \mathrm{pa}(\mathcal{P})))$. Now, pick an element $\hat{\boldsymbol{x}}_{\mathrm{pa}(\mathcal{O}) \backslash(\mathcal{O} \cup \mathrm{pa}(\mathcal{P}))} \in \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash(\mathcal{O} \cup \mathrm{pa}(\mathcal{P}))}$ and define the mapping $\tilde{\boldsymbol{g}}_{\mathcal{P}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{P})} \rightarrow$ $\boldsymbol{\mathcal { X }}_{\mathcal{P}}$ by

$$
\tilde{\boldsymbol{g}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right):=\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}}, \hat{\boldsymbol{x}}_{\mathrm{pa}(\mathcal{O}) \backslash(\mathcal{O} \cup \mathrm{pa}(\mathcal{P}))}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)
$$

Then, for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{P}}=\tilde{\boldsymbol{g}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{P}}=\left(\boldsymbol{g}_{\mathcal{O}}\right)_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right)
$$

Together this gives that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{P}}=\tilde{\boldsymbol{g}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P}) \backslash \mathcal{P}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right) \quad \Longrightarrow \quad \boldsymbol{x}_{\mathcal{P}}=\tilde{\boldsymbol{f}}_{\mathcal{P}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{P})}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{P})}\right)
$$

which is equivalent to the statement that $\mathcal{M}$ is solvable w.r.t. $\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{O}}}(\mathcal{A})$.

# Section 4 

Lemma E.1. Let $\mathcal{M}$ be an SCM that is uniquely solvable w.r.t. two subsets $A, B \subseteq \mathcal{I}$ that satisfy $A \subseteq B$ and $\mathrm{pa}(A) \backslash A \subseteq \mathrm{pa}(B) \backslash B$. Let $\boldsymbol{g}_{A}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(A) \backslash A} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(A)} \rightarrow \boldsymbol{\mathcal { X }}_{A}$ and $\boldsymbol{g}_{B}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(B) \backslash B} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(B)} \rightarrow \boldsymbol{\mathcal { X }}_{B}$ be measurable solution functions for $\mathcal{M}$ w.r.t. $A$ and $B$, respectively. Then for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)=\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right)
$$

Proof. Without loss of generality, we assume that $\mathcal{M}$ is structurally minimal (see Proposition 2.11). Let $\overline{\boldsymbol{\mathcal { E }}} \subseteq \boldsymbol{\mathcal { E }}$ be a measurable set with $\mathbb{P}_{\boldsymbol{\mathcal { E }}}(\overline{\boldsymbol{\mathcal { E }}})=1$ such that for all $\boldsymbol{e} \in \overline{\boldsymbol{\mathcal { E }}}$ for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ :

$$
\boldsymbol{x}_{A}=\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right) \Longleftrightarrow \boldsymbol{x}_{A}=\boldsymbol{f}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A)}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)
$$

and

$$
\boldsymbol{x}_{B}=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longleftrightarrow \boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right)
$$

Now let $\boldsymbol{e} \in \overline{\boldsymbol{\mathcal { E }}}$ and let $\boldsymbol{x}_{A \cup \mathrm{pa}(B) \backslash B} \in \boldsymbol{\mathcal { X }}_{A \cup \mathrm{pa}(B) \backslash B}$. Then

$$
\begin{aligned}
& \boldsymbol{x}_{A}=\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \\
& \Longrightarrow\left\{\begin{array}{cc}
\boldsymbol{x}_{A}=\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \\
\exists \boldsymbol{x}_{B \backslash A} \in \boldsymbol{\mathcal { X }}_{B \backslash A}: & \boldsymbol{x}_{B \backslash A}=\left(\boldsymbol{g}_{B}\right)_{B \backslash A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \\
\Longrightarrow \exists \boldsymbol{x}_{B \backslash A} \in \boldsymbol{\mathcal { X }}_{B \backslash A}: & \boldsymbol{x}_{B}=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \\
\Longrightarrow \exists \boldsymbol{x}_{B \backslash A} \in \boldsymbol{\mathcal { X }}_{B \backslash A}: & \boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \\
\Longrightarrow \exists \boldsymbol{x}_{B \backslash A} \in \boldsymbol{\mathcal { X }}_{B \backslash A}: & \boldsymbol{x}_{A}=\boldsymbol{f}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A)}, \boldsymbol{e}_{\mathrm{pa}(A)}\right) \\
\Longrightarrow \boldsymbol{x}_{A}=\boldsymbol{f}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A)}, \boldsymbol{e}_{\mathrm{pa}(A)}\right) \\
\Longrightarrow \boldsymbol{x}_{A}=\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)
\end{array}\right.
\end{aligned}
$$

where the exists-quantifier could be omitted because the expression it binds to does not depend on $\boldsymbol{x}_{B \backslash A}$ (from the assumptions it follows that $(A \cup \mathrm{pa}(A)) \cap(B \backslash A)=\emptyset$ ). Hence, for all $\boldsymbol{e} \in \overline{\boldsymbol{\mathcal { E }}}$ and all $\boldsymbol{x}_{A \cup \mathrm{pa}(B) \backslash B} \in \boldsymbol{\mathcal { X }}_{A \cup \mathrm{pa}(B) \backslash B}$

$$
\boldsymbol{x}_{A}=\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longrightarrow \boldsymbol{x}_{A}=\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)
$$

Hence, for all $\boldsymbol{e} \in \overline{\boldsymbol{\mathcal { E }}}$ and all $\boldsymbol{x}_{A \cup \mathrm{pa}(B) \backslash B} \in \boldsymbol{\mathcal { X }}_{A \cup \mathrm{pa}(B) \backslash B}$

$$
\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right)=\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)
$$

Since this expression does not depend on $\boldsymbol{x}_{(B \backslash A) \cup \mathcal{I} \backslash(B \cup \mathrm{pa}(B))}$, from Lemma F.11.(2) we conclude that for all $\boldsymbol{e} \in \overline{\boldsymbol{\mathcal { E }}}$ and all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\left(\boldsymbol{g}_{B}\right)_{A}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right)=\boldsymbol{g}_{A}\left(\boldsymbol{x}_{\mathrm{pa}(A) \backslash A}, \boldsymbol{e}_{\mathrm{pa}(A)}\right)
$$

LEMMA E.2. An SCM $\mathcal{M}$ is observationally equivalent to $\mathcal{M}^{\text {twin }}$ w.r.t. $\mathcal{O} \subseteq \mathcal{I}$.
Proof. Let $(\boldsymbol{X}, \boldsymbol{E})$ be a solution of $\mathcal{M}$, then $((\boldsymbol{X}, \boldsymbol{X}), \boldsymbol{E})$ is a solution of $\mathcal{M}^{\text {twin }}$. Conversely, let $\left(\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right), \boldsymbol{E}\right)$ be a solution of $\mathcal{M}^{\text {twin }}$, then $(\boldsymbol{X}, \boldsymbol{E})$ is a solution of $\mathcal{M}$.

Proof of Proposition 4.6. First we show that equivalence implies counterfactual equivalence w.r.t. $\mathcal{O}$. The twin operation preserves the equivalence relation on SCMs and since equivalent SCMs are interventionally equivalent w.r.t. every subset, the two equivalent twin SCMs have to be interventionally equivalent w.r.t. $\mathcal{O} \cup \mathcal{O}^{\prime}$ for every $\mathcal{O} \subseteq \mathcal{I}$ with $\mathcal{O}^{\prime}$ the copy of $\mathcal{O}$ in $\mathcal{I}^{\prime}$.

Now, let $\mathcal{M}$ and $\tilde{\mathcal{M}}$ be counterfactually equivalent w.r.t. $\mathcal{O}$. Then $\mathcal{M}^{\text {twin }}$ and $\tilde{\mathcal{M}}^{\text {twin }}$ are interventionally equivalent w.r.t. $\mathcal{O} \cup \mathcal{O}^{\prime}$. Thus for $I \subseteq \mathcal{O}, I^{\prime} \subseteq \mathcal{O}^{\prime}$ the copy of $I$ and $\boldsymbol{\xi}_{I^{\prime}}=$ $\boldsymbol{\xi}_{I} \in \boldsymbol{\mathcal { X }}_{I}, \mathcal{M}_{\mathrm{do}\left(I \cup I^{\prime}, \boldsymbol{\xi}_{I \cup I^{\prime}}\right)}^{\text {twin }}$ and $\tilde{\mathcal{M}}_{\mathrm{do}\left(I \cup I^{\prime}, \boldsymbol{\xi}_{I \cup I^{\prime}}\right)}^{\text {twin }}$ are observationally equivalent w.r.t. $\mathcal{O} \cup \mathcal{O}^{\prime}$. In particular, they are observationally equivalent w.r.t. $\mathcal{O}$. From Proposition 2.21 we have that $\mathcal{M}_{\mathrm{do}\left(I \cup I^{\prime}, \boldsymbol{\xi}_{I \cup I^{\prime}}\right)}^{\text {twin }}=\left(\mathcal{M}_{\mathrm{do}\left(I, \boldsymbol{\xi}_{I}\right)}\right)^{\text {twin }}$ and $\tilde{\mathcal{M}}_{\mathrm{do}\left(I \cup I^{\prime}, \boldsymbol{\xi}_{I \cup I^{\prime}}\right)}^{\text {twin }}=\left(\tilde{\mathcal{M}}_{\mathrm{do}\left(I, \boldsymbol{\xi}_{I}\right)}\right)^{\text {twin }}$, and together with Lemma E. 2 this gives that $\mathcal{M}_{\mathrm{do}\left(I, \boldsymbol{\xi}_{I}\right)}$ and $\tilde{\mathcal{M}}_{\mathrm{do}\left(I, \boldsymbol{\xi}_{I}\right)}$ are observationally equivalent w.r.t. $\mathcal{O}$.

# Section 5 

Lemma E.3. Let $\mathcal{M}$ be an SCM. Let $B \subseteq \mathcal{I}$ and $A \subseteq \mathcal{I} \cup \mathcal{J}$ such that $(\operatorname{pa}(B) \backslash B) \subseteq A$ and $B \cap A=\emptyset$. Assume that $\boldsymbol{g}_{B}: \boldsymbol{\mathcal { X }}_{A} \times \boldsymbol{\mathcal { E }}_{A} \rightarrow \boldsymbol{\mathcal { X }}_{B}$ is a measurable function such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longleftrightarrow \boldsymbol{x}_{B}=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{A}, \boldsymbol{e}_{A}\right)
$$

Then $\mathcal{M}$ is uniquely solvable w.r.t. $B$.
Proof. Assume that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longleftrightarrow \boldsymbol{x}_{B}=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{A}, \boldsymbol{e}_{A}\right)
$$

Let $C:=A \backslash(\operatorname{pa}(B) \backslash B)$, then by Lemma F.11.(7) we have that there exists $\hat{\boldsymbol{e}}_{C} \in \boldsymbol{\mathcal { E }}_{C}$ and $\hat{\boldsymbol{x}}_{C} \in \boldsymbol{\mathcal { X }}_{C}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}_{\mathcal{J} \backslash C}}$-almost every $\boldsymbol{e}_{\mathcal{J} \backslash C} \in \boldsymbol{\mathcal { E }}_{\mathcal{J} \backslash C}$ and for all $\boldsymbol{x}_{\mathcal{I} \backslash C} \in \boldsymbol{\mathcal { X }}_{\mathcal{I} \backslash C}$

$$
\boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longleftrightarrow \boldsymbol{x}_{B}=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \hat{\boldsymbol{x}}_{C}, \boldsymbol{e}_{\mathrm{pa}(B)}, \hat{\boldsymbol{e}}_{C}\right)
$$

Defining the mapping $\boldsymbol{h}_{B}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(B) \backslash B} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(B)} \rightarrow \boldsymbol{\mathcal { X }}_{B}$ by

$$
\boldsymbol{h}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right):=\boldsymbol{g}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \hat{\boldsymbol{x}}_{C}, \boldsymbol{e}_{\mathrm{pa}(B)}, \hat{\boldsymbol{e}}_{C}\right)
$$

where we picked $\hat{\boldsymbol{e}}_{C} \in \boldsymbol{\mathcal { E }}_{C}$ and $\hat{\boldsymbol{x}}_{C} \in \boldsymbol{\mathcal { X }}_{C}$ such that the above equivalence holds, and applying Lemma F.11.(6) we get that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{B}=\boldsymbol{f}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B)}, \boldsymbol{e}_{\mathrm{pa}(B)}\right) \Longleftrightarrow \boldsymbol{x}_{B}=\boldsymbol{h}_{B}\left(\boldsymbol{x}_{\mathrm{pa}(B) \backslash B}, \boldsymbol{e}_{\mathrm{pa}(B)}\right)
$$

holds. Thus, $\mathcal{M}$ is uniquely solvable w.r.t. $B$.
Proof of Proposition 5.4. From unique solvability of $\mathcal{M}$ w.r.t. $\mathcal{L}_{1}$ it follows that there exists a mapping $\boldsymbol{g}_{\mathcal{L}_{1}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash\left(\mathcal{L}_{1}\right)} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}_{1}}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{L}_{1}}=\boldsymbol{f}_{\mathcal{L}_{1}}(\boldsymbol{x}, \boldsymbol{e})
$$

Let $\overline{\mathrm{pa}}$ denotes the parents in $\mathcal{G}^{a}\left(\mathcal{M}_{\operatorname{mag}\left(\mathcal{L}_{1}\right)}\right)$. Note that $\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2} \subseteq \operatorname{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup\right.$ $\mathcal{L}_{2}$ ). Let $\hat{\boldsymbol{f}}$ denote the marginal causal mechanism of a structurally minimal SCM that is equivalent to the marginalization $\mathcal{M}_{\operatorname{mag}\left(\mathcal{L}_{1}\right)}$ constructed from $\boldsymbol{g}_{\mathcal{L}_{1}}$ (see Proposition 2.11).
$\Longrightarrow$ : If $\mathcal{M}_{\operatorname{mag}\left(\mathcal{L}_{1}\right)}$ is uniquely solvable w.r.t. $\mathcal{L}_{2}$, then there exists a mapping $\hat{\boldsymbol{g}}_{\mathcal{L}_{2}}$ : $\boldsymbol{\mathcal { X }}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}} \times \boldsymbol{\mathcal { E }}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}_{2}}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}_{1}} \in \boldsymbol{\mathcal { X }}_{\mathcal{I} \backslash \mathcal{L}_{1}}$

$$
\left.\boldsymbol{x}_{\mathcal{L}_{2}}=\hat{\boldsymbol{g}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right) \Longleftrightarrow \boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}\left(\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right), \boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}_{1}}, \boldsymbol{e}\right)
$$

Define the mapping $\boldsymbol{h}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}}$ by

$$
\begin{aligned}
& \left(\boldsymbol{h}_{\mathcal{L}_{1}}, \boldsymbol{h}_{\mathcal{L}_{2}}\right)\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right):= \\
& \left(\boldsymbol{g}_{\mathcal{L}_{1}}\left(\left(\hat{\boldsymbol{g}}_{\mathcal{L}_{2}}\right)_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right), \boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right), \hat{\boldsymbol{g}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right)\right)
\end{aligned}
$$

Then for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$

$$
\begin{aligned}
& \left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{f}_{\mathcal{L}_{1}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}\left(\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right), \boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}_{1}}, \boldsymbol{e}\right) \\
\Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\tilde{\boldsymbol{g}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right)
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\left(\tilde{\boldsymbol{g}}_{\mathcal{L}_{2}}\right)_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\left(\boldsymbol{x}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right), \boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\tilde{\boldsymbol{g}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right) \backslash \mathcal{L}_{2}}, \boldsymbol{e}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right)
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{h}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{h}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right)
\end{array}\right.
\end{aligned}
$$

where in the first equivalence we used unique solvability w.r.t. $\mathcal{L}_{1}$ of $\mathcal{M}$, in the second we used substitution, in the third we used unique solvability w.r.t. $\mathcal{L}_{2}$ of $\mathcal{M}_{\operatorname{marg}\left(\mathcal{L}_{1}\right)}$, in the fourth we used again substitution and in the last equivalence we used the definition of $\boldsymbol{h}$. From this we conclude that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}_{1} \cup \mathcal{L}_{2}$. Hence, by definition it follows that $\operatorname{marg}\left(\mathcal{L}_{2}\right) \circ \operatorname{marg}\left(\mathcal{L}_{1}\right)(\mathcal{M})=\operatorname{marg}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)(\mathcal{M})$.
$\Longleftarrow$ : If $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}_{1} \cup \mathcal{L}_{2}$, then there exists a mapping $\boldsymbol{h}$ : $\boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)} \times \boldsymbol{\mathcal { E }}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}}$ such that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ for all $\boldsymbol{x} \in \mathcal{X}$

$$
\boldsymbol{x}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}}=\boldsymbol{h}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{1} \cup \mathcal{L}_{2}}(\boldsymbol{x}, \boldsymbol{e})
$$

Then, for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ for all $\boldsymbol{x} \in \mathcal{X}$

$$
\begin{aligned}
& \left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{h}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{h}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right)
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{f}_{\mathcal{L}_{1}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\boldsymbol{f}_{\mathcal{L}_{2}}\left(\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right), \boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}_{1}}, \boldsymbol{e}\right)
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
x_{\mathcal{L}_{1}}=\boldsymbol{g}_{\mathcal{L}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1}\right) \backslash \mathcal{L}_{1}}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1}\right)}\right) \\
\boldsymbol{x}_{\mathcal{L}_{2}}=\tilde{\boldsymbol{f}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}, \boldsymbol{e}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right)
\end{array}\right.
\end{aligned}
$$

This gives for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ for all $\boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}_{1}} \in \mathcal{X}_{\mathcal{I} \backslash \mathcal{L}_{1}}$

$$
\begin{aligned}
x_{\mathcal{L}_{2}} & =\boldsymbol{h}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right) \backslash\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{L}_{1} \cup \mathcal{L}_{2}\right)}\right) \\
\Longleftrightarrow \boldsymbol{x}_{\mathcal{L}_{2}} & =\tilde{\boldsymbol{f}}_{\mathcal{L}_{2}}\left(\boldsymbol{x}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}, \boldsymbol{e}_{\widetilde{\mathrm{pa}}\left(\mathcal{L}_{2}\right)}\right)
\end{aligned}
$$

Now apply Lemma E. 3 to conclude that $\mathcal{M}_{\operatorname{marg}\left(\mathcal{L}_{1}\right)}$ is uniquely solvable w.r.t. $\mathcal{L}_{2}$.

Proof of Proposition 5.5. The commutation relation with the perfect intervention follows straightforwardly from the definitions of perfect intervention and marginalization and the fact that if $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$, then $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ is also uniquely solvable w.r.t. $\mathcal{L}$, since the structural equations for the variables $\mathcal{L}$ are the same for $\mathcal{M}$ and $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$.

The commutation relation with the twin operation follows straightforwardly from the definition of the twin operation and marginalization and the fact that if $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$, then twin $(\mathcal{M})$ is uniquely solvable w.r.t. $\mathcal{L} \cup \mathcal{L}^{\prime}$, where $\mathcal{L}^{\prime}$ is the copy of $\mathcal{L}$ in $\mathcal{I}^{\prime}$.

Lemma E.4. Given an SCM $\mathcal{M}$ and a subset $\mathcal{L} \subseteq \mathcal{I}$ such that $\mathcal{M}$ is uniquely solvable w.r.t. $\mathcal{L}$. Then $\mathcal{M}$ and $\operatorname{marg}(\mathcal{L})(\mathcal{M})$ are observationally equivalent w.r.t. $\mathcal{I} \backslash \mathcal{L}$.

Proof. Let $\mathcal{O}:=\mathcal{I} \backslash \mathcal{L}$. From unique solvability w.r.t. $\mathcal{L}$ it follows that for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \boldsymbol{X}$

$$
\begin{aligned}
& \left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{L}}=\boldsymbol{f}_{\mathcal{L}}(\boldsymbol{x}, \boldsymbol{e}) \\
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}(\boldsymbol{x}, \boldsymbol{e})
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{L}}=\boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{L})}\right) \\
\boldsymbol{x}_{\mathcal{O}}=\boldsymbol{f}_{\mathcal{O}}\left(\boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{L})}\right), \boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right)
\end{array}\right. \\
& \Longleftrightarrow\left\{\begin{array}{l}
\boldsymbol{x}_{\mathcal{L}}=\boldsymbol{g}_{\mathcal{L}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{L})}\right) \\
\boldsymbol{x}_{\mathcal{O}}=\overline{\boldsymbol{f}}\left(\boldsymbol{x}_{\mathcal{O}}, \boldsymbol{e}\right),
\end{array}\right.
\end{aligned}
$$

where $\overline{\boldsymbol{f}}$ is the marginal causal mechanism of $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ constructed from a measurable solution function $\boldsymbol{g}_{\mathcal{L}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{L})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{L}}$ for $\mathcal{M}$ w.r.t. $\mathcal{L}$. Hence, a solution $(\boldsymbol{X}, \boldsymbol{E})$ of $\mathcal{M}$ satisfies $\boldsymbol{X}_{\mathcal{O}}=\overline{\boldsymbol{f}}\left(\boldsymbol{X}_{\mathcal{O}}, \boldsymbol{E}\right)$ a.s.. Conversely, if $\left(\overline{\boldsymbol{X}}_{\mathcal{O}}, \boldsymbol{E}\right)$ is a solution of the marginal $\operatorname{SCM} \mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ then with $\overline{\boldsymbol{X}}_{\mathcal{L}}:=\boldsymbol{g}_{\mathcal{L}}\left(\overline{\boldsymbol{X}}_{\mathrm{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{E}_{\mathrm{pa}(\mathcal{L})}\right)$, the random variables $(\boldsymbol{X}, \boldsymbol{E}):=$ $\left(\overline{\boldsymbol{X}}_{\mathcal{O}}, \overline{\boldsymbol{X}}_{\mathcal{L}}, \boldsymbol{E}\right)$ are a solution of $\mathcal{M}$.

Proof of Theorem 5.6. The observational equivalence follows from Lemma E.4. Using both Lemma E. 4 and Proposition 5.5 we can prove the interventional equivalence. Observe that from Proposition 5.5 we know that for a subset $I \subseteq \mathcal{I} \backslash \mathcal{L}$ and a value $\xi_{I} \in \boldsymbol{\mathcal { X }}_{I},\left(\operatorname{marg}(\mathcal{L}) \circ \operatorname{do}\left(I, \xi_{I}\right)\right)(\mathcal{M})$ exists. By Lemma E. 4 we know that $\operatorname{do}\left(I, \xi_{I}\right)(\mathcal{M})$ and $\left(\operatorname{marg}(\mathcal{L}) \circ \operatorname{do}\left(I, \xi_{I}\right)\right)(\mathcal{M})$ are observationally equivalent w.r.t. $\mathcal{O}$ and hence by applying again Proposition 5.5, $\operatorname{do}\left(I, \xi_{I}\right)(\mathcal{M})$ and $(\operatorname{do}(I, \xi) \circ \operatorname{marg}(\mathcal{L}))(\mathcal{M})$ are observationally equivalent w.r.t. $\mathcal{O}$. This implies that $\mathcal{M}$ and $\operatorname{marg}(\mathcal{L})(\mathcal{M})$ are interventionally equivalent w.r.t. $\mathcal{O}$. Lastly, we need to show that twin $(\mathcal{M})$ and $(\operatorname{twin} \circ \operatorname{marg}(\mathcal{L}))(\mathcal{M})$ are interventionally equivalent w.r.t. $\left(\mathcal{I} \cup \mathcal{I}^{\prime}\right) \backslash\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right)$, where $\mathcal{L}^{\prime}$ is the copy of $\mathcal{L}$ in $\mathcal{I}^{\prime}$. From Proposition $5.5\left(\right.$ twin $\left.\circ \operatorname{marg}(\mathcal{L})\right)(\mathcal{M})$ is equivalent to $\left(\operatorname{marg}\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right) \circ\right.$ twin $)(\mathcal{M})$ and since we proved that $\left(\operatorname{marg}\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right) \circ\right.$ twin $)(\mathcal{M})$ and twin $(\mathcal{M})$ are interventionally equivalent w.r.t. $\left(\mathcal{I} \cup \mathcal{I}^{\prime}\right) \backslash\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right)$ the result follows.

Proof of Proposition 5.8. A similar proof as for Theorem 1 in [15] works.
Proof of Proposition 5.9. First we prove the commutation relation of the perfect intervention. Observe that applying the $\operatorname{do}(I)$ operation to the latent projection $\operatorname{marg}(\mathcal{L})(\mathcal{G})$ removes all the incoming edges on the nodes $I$. Such an incoming edge at a node in $I$ in $\operatorname{marg}(\mathcal{L})(\mathcal{G})$ corresponds to a path in $\mathcal{G}$ that points to that node. But since $\operatorname{do}(I)(\mathcal{G})$ is just $\mathcal{G}$ with all the incoming edges on $I$ removed, the graph $(\operatorname{marg}(\mathcal{L}) \circ \operatorname{do}(I))(\mathcal{G})$ also has all the incoming edges on the nodes $I$ removed.

Next, we will prove the commutation relation of the twin operation. We will denote the copy in $\mathcal{I}^{\prime}$ of any node $i \in \mathcal{I}$ by $i^{\prime}$, that is, $\mathcal{I}^{\prime}=\left\{i^{\prime}: i \in \mathcal{I}\right\}$. The edges in $(\operatorname{twin}(\mathcal{I} \backslash \mathcal{L}) \circ$ $\operatorname{marg}(\mathcal{L}))(\mathcal{G})$ can be partitioned into three cases:

$$
\left\{\begin{array}{l}
v \rightarrow w \quad v \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, w \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, v \rightarrow w \in \operatorname{marg}(\mathcal{L})(\mathcal{G}) \\
v \rightarrow w^{\prime} \quad v \in \mathcal{J}, w \in \mathcal{I} \backslash \mathcal{L}, v \rightarrow w \in \operatorname{marg}(\mathcal{L})(\mathcal{G}) \\
v^{\prime} \rightarrow w^{\prime} \quad v \in \mathcal{I} \backslash \mathcal{L}, w \in \mathcal{I} \backslash \mathcal{L}, v \rightarrow w \in \operatorname{marg}(\mathcal{L})(\mathcal{G})
\end{array}\right.
$$

where $\mathcal{J}:=\mathcal{V} \backslash \mathcal{I}$.
Note that in twin $(\mathcal{I})(\mathcal{G})$, there are no directed edges of the form $v^{\prime} \rightarrow w$ by definition. Therefore, the edges in $\left(\operatorname{marg}\left(\mathcal{L} \cup \mathcal{L}^{\prime}\right) \circ \operatorname{twin}(\mathcal{I})\right)(\mathcal{G})$ can be partitioned into three cases:

$$
\left\{\begin{array}{l}
v \rightarrow w \quad v \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, w \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, v \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow w \in \operatorname{twin}(\mathcal{I})(\mathcal{G}) \\
v \rightarrow w^{\prime} \quad v \in \mathcal{J}, w \in \mathcal{I} \backslash \mathcal{L}, v \rightarrow \ell_{1}^{\prime} \rightarrow \cdots \rightarrow \ell_{n}^{\prime} \rightarrow w^{\prime} \in \operatorname{twin}(\mathcal{I})(\mathcal{G})
\end{array}\right.
$$

where all $\ell_{1}, \ldots, \ell_{n} \in \mathcal{L}$ and $\ell_{1}^{\prime}, \ldots, \ell_{n}^{\prime} \in \mathcal{L}^{\prime}$. Thus, the non-endpoint nodes on the directed paths in twin $(\mathcal{I})(\mathcal{G})$ must either all lie in $\mathcal{L}$ or in $\mathcal{L}^{\prime}$. With the definition of twin $(\mathcal{I})(\mathcal{G})$ we can rewrite this as follows:

$$
\left\{\begin{array}{l}
v \rightarrow w \quad v \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, w \in \mathcal{J} \cup \mathcal{I} \backslash \mathcal{L}, v \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow w \in \mathcal{G} \\
v \rightarrow w^{\prime} \quad v \in \mathcal{J}, w \in \mathcal{I} \backslash \mathcal{L}, v \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow w \in \mathcal{G} \\
v^{\prime} \rightarrow w^{\prime} \quad v \in \mathcal{I} \backslash \mathcal{L}, w \in \mathcal{I} \backslash \mathcal{L}, v \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow w \in \mathcal{G}
\end{array}\right.
$$

where all intermediate $\ell_{1}, \ldots, \ell_{n}$ must lie in $\mathcal{L}$. This corresponds exactly with the edges in $(\operatorname{twin}(\mathcal{I} \backslash \mathcal{L}) \circ \operatorname{marg}(\mathcal{L}))(\mathcal{G})$.

Proof of Proposition 5.11. Without loss of generality, we assume that $\mathcal{M}$ is structurally minimal (see Proposition 2.11). Let $\boldsymbol{g}_{\mathcal{L}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{L}$ and denote by $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ the marginal SCM constructed from $\boldsymbol{g}_{\mathcal{L}}$. For $j \in \mathcal{I} \backslash \mathcal{L}$, define $A_{j}:=\operatorname{an}_{\mathcal{G}(\mathcal{M})_{\mathcal{L}}}(\operatorname{pa}(j) \cap \mathcal{L}) \subseteq \mathcal{L}$ and let $\tilde{\boldsymbol{g}}_{A_{j}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $A_{j}$. Because $A_{j} \subseteq \mathcal{L}$ and $\operatorname{pa}\left(A_{j}\right) \backslash A_{j} \subseteq \operatorname{pa}(\mathcal{L}) \backslash \mathcal{L}$, by Lemma E.1, for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\left(\boldsymbol{g}_{\mathcal{L}}\right)_{A_{j}}\left(\boldsymbol{x}_{\operatorname{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\operatorname{pa}(\mathcal{L})}\right)=\tilde{\boldsymbol{g}}_{A_{j}}\left(\boldsymbol{x}_{\operatorname{pa}\left(A_{j}\right) \backslash A_{j}}, \boldsymbol{e}_{\operatorname{pa}\left(A_{j}\right)}\right)
$$

Therefore, the component $\tilde{f}_{j}$ of the marginal causal mechanism $\tilde{f}$ of $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ satisfies for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\begin{aligned}
\tilde{f}_{j}\left(\boldsymbol{x}_{\mathcal{I} \backslash \mathcal{L}}, \boldsymbol{e}\right) & :=f_{j}\left(\left(\boldsymbol{g}_{\mathcal{L}}\right)_{\operatorname{pa}(j)}\left(\boldsymbol{x}_{\operatorname{pa}(\mathcal{L}) \backslash \mathcal{L}}, \boldsymbol{e}_{\operatorname{pa}(\mathcal{L})}\right), \boldsymbol{x}_{\operatorname{pa}(j) \backslash \mathcal{L}}, \boldsymbol{e}_{\operatorname{pa}(j)}\right) \\
& =f_{j}\left(\left(\tilde{\boldsymbol{g}}_{A_{j}}\right)_{\operatorname{pa}(j) \cap \mathcal{L}}\left(\boldsymbol{x}_{\operatorname{pa}\left(A_{j}\right) \backslash A_{j}}, \boldsymbol{e}_{\operatorname{pa}\left(A_{j}\right)}\right), \boldsymbol{x}_{\operatorname{pa}(j) \backslash \mathcal{L}}, \boldsymbol{e}_{\operatorname{pa}(j)}\right)
\end{aligned}
$$

Hence, the endogenous parents of $j$ in $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ are a subset of $\left(\left(\operatorname{pa}\left(A_{j}\right) \backslash A_{j}\right) \cup(\operatorname{pa}(j) \backslash\right.$ $\mathcal{L})) \cap \mathcal{I}$ and the exogenous parents of $j$ in $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ are a subset of $\left(\operatorname{pa}\left(A_{j}\right) \cup \operatorname{pa}(j)\right) \cap \mathcal{J}$. Hence, all parents of $j$ in $\mathcal{M}_{\operatorname{marg}(\mathcal{L})}$ are a subset of those $k \in(\mathcal{I} \backslash \mathcal{L}) \cup \mathcal{J}$ such that there exists a path $k \rightarrow \ell_{1} \rightarrow \cdots \rightarrow \ell_{n} \rightarrow j \in \mathcal{G}^{a}(\mathcal{M})$ for $n \geq 0$ and $\ell_{1}, \ldots, \ell_{n} \in \mathcal{L}$. Therefore, the augmented graph $\mathcal{G}^{a}(\operatorname{marg}(\mathcal{L})(\mathcal{M}))$ is a subgraph of the latent projection $\operatorname{marg}(\mathcal{L})\left(\mathcal{G}^{a}(\mathcal{M})\right)$.

Hence,

$$
\begin{aligned}
\mathcal{G}(\operatorname{margr}(\mathcal{L})(\mathcal{M})) & =\operatorname{margr}(\mathcal{J})\left(\mathcal{G}^{a}(\operatorname{margr}(\mathcal{L})(\mathcal{M}))\right) \\
& \subseteq \operatorname{margr}(\mathcal{J})\left(\operatorname{margr}(\mathcal{L})\left(\mathcal{G}^{a}(\mathcal{M})\right)\right) \\
& =\operatorname{margr}(\mathcal{L})\left(\operatorname{margr}(\mathcal{J})\left(\mathcal{G}^{a}(\mathcal{M})\right)\right) \\
& =\operatorname{margr}(\mathcal{L})(\mathcal{G}(\mathcal{M}))
\end{aligned}
$$

and we conclude that also the graph $\mathcal{G}(\operatorname{margr}(\mathcal{L})(\mathcal{M}))$ is a subgraph of the latent projection $\operatorname{margr}(\mathcal{L})(\mathcal{G}(\mathcal{M}))$.

# Section 6 

Proof of Theorem 6.3. This follows directly from Theorems A. 7 and A.21.

## Section 7

Proof of Proposition 7.1. We define $\tilde{\mathcal{M}}:=\mathcal{M}_{\mathrm{do}\left(I, \xi_{t}\right)}, \overline{\mathrm{pa}}:=\mathrm{pa}_{\mathcal{G}^{a}(\tilde{\mathcal{M}})}$ and $\mathcal{A}:=$ $\operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}}) \backslash i}(j)$. Suppose that $i \rightarrow j \notin \operatorname{margr}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\mathcal{M}))$ and assume that the two induced distributions do not coincide. Because $i \rightarrow j \notin \operatorname{margr}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\mathcal{M}))$ it follows that $(\overline{\mathrm{pa}}(\mathcal{A}) \backslash \mathcal{A}) \cap \mathcal{I}=\emptyset$. Let now $\tilde{\boldsymbol{g}}_{\mathcal{A}}: \boldsymbol{\mathcal { E }}_{\overline{\mathrm{pa}}(\mathcal{A})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{A}}$ be a measurable solution function for $\tilde{\mathcal{M}}$ w.r.t. $\mathcal{A}$, that is, we have for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{A}}=\tilde{\boldsymbol{f}}_{\mathcal{A}}(\boldsymbol{x}, \boldsymbol{e}) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{A}}=\tilde{\boldsymbol{g}}_{\mathcal{A}}\left(\boldsymbol{e}_{\overline{\mathrm{pa}}(\mathcal{A})}\right)
$$

where $\tilde{\boldsymbol{f}}$ is the ausal mechanism of $\tilde{\mathcal{M}}$. Because $i \notin \mathcal{A}$ and $j \in \mathcal{A}$, it follows that for the intervened model $\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{t}\right)}\right)_{\mathrm{do}\left(\{i\}, \xi_{i}\right)}$ the marginal solution $X_{j}$ is also a marginal solution of $\left(\mathcal{M}_{\mathrm{do}\left(I, \xi_{t}\right)}\right)_{\mathrm{do}\left(\{i\}, \tilde{\xi}_{i}\right)}$ and vice versa, which is in contradiction with the assumption.

Proof of Proposition 7.2. Let's define $\tilde{\mathcal{M}}:=\mathcal{M}_{\mathrm{do}\left(I, \xi_{t}\right)}, \overline{\mathrm{pa}}:=\mathrm{pa}_{\mathcal{G}^{a}(\tilde{\mathcal{M}})}, \mathcal{A}_{i}:=$ $\operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}})}(i)$ and $\mathcal{A}_{j}^{\backslash i}:=\operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}}) \backslash i}(j)$. Suppose that there does not exist a bidirected edge $i \leftrightarrow j$ in the latent projection $\operatorname{margr}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\mathcal{M}))$. Because $i \leftrightarrow j \notin \operatorname{margr}(\mathcal{I} \backslash \mathcal{O})(\mathcal{G}(\tilde{\mathcal{M}}))$, where here $\tilde{\mathcal{M}}$ is the intervened model $\mathcal{M}_{\mathrm{do}\left(I, \xi_{t}\right)}$, we have that $\operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}}) \backslash i}(i) \cap \operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}}) \backslash i}(j) \cap \mathcal{J}=$ $\emptyset$. From $j \notin \operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}})}(i)$ it follows that $\operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}}) \backslash i}(i)=\operatorname{an}_{\mathcal{G}(\tilde{\mathcal{M}})}(i)$, and hence $\operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}})}(i) \cap$ $\operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}}) \backslash i}(j) \cap \mathcal{J}=\emptyset$. Observe that $\overline{\mathrm{pa}}\left(\mathcal{A}_{i}\right) \subseteq \operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}})}(i)$ and $\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \subseteq \operatorname{an}_{\mathcal{G}^{a}(\tilde{\mathcal{M}}) \backslash i}(j) \cup$ $\{i\}$, and thus $\overline{\mathrm{pa}}\left(\mathcal{A}_{i}\right) \cap \overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \cap \mathcal{J}=\emptyset$. Let $\boldsymbol{g}_{\mathcal{A}_{i}}: \boldsymbol{\mathcal { E }}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{i}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{A}_{i}}$ be a measurable solution function for $\tilde{\mathcal{M}}$ w.r.t. $\mathcal{A}_{i}$, that is, we have for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{A}_{i}}=\tilde{\boldsymbol{f}}_{\mathcal{A}_{i}}(\boldsymbol{x}, \boldsymbol{e}) \quad \Longleftrightarrow \quad \boldsymbol{x}_{\mathcal{A}_{i}}=\boldsymbol{g}_{\mathcal{A}_{i}}\left(\boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{i}\right)}\right)
$$

where $\tilde{\boldsymbol{f}}$ is the intervened causal mechanism of $\tilde{\mathcal{M}}$. Because $\overline{\mathrm{pa}}\left(\mathcal{A}_{i}\right) \cap \overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \cap \mathcal{J}=\emptyset$ and $i \in \mathcal{A}_{i}$, we have that $X_{i} \mathbb{L} \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}$ for every solution $(\boldsymbol{X}, \boldsymbol{E})$ of $\tilde{\mathcal{M}}$.

Assume for the moment that $i \in \overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \backslash \mathcal{A}_{j}^{\backslash i}$, then $\left(\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \backslash \mathcal{A}_{j}^{\backslash i}\right) \cap \mathcal{I}=\{i\}$. Let $\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}$ : $\mathcal{X}_{i} \times \boldsymbol{\mathcal { E }}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{A}_{j}^{\backslash i}}$ be a measurable solution function for $\tilde{\mathcal{M}}$ w.r.t. $\mathcal{A}_{j}^{\backslash i}$, that is, we have for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$

$$
\boldsymbol{x}_{\mathcal{A}_{j}^{\backslash i}}=\tilde{\boldsymbol{f}}_{\mathcal{A}_{j}^{\backslash i}}(\boldsymbol{x}, \boldsymbol{e}) \Longleftrightarrow \boldsymbol{x}_{\mathcal{A}_{j}^{\backslash i}}=\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}\left(x_{i}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}\right)
$$

For every measurable set $\mathcal{B}_{j} \subseteq \mathcal{X}_{j}$ there exists a version of the regular conditional probability $\mathbb{P}_{\mathcal{M}_{\text {do }\left(I, \xi_{I}\right)}}\left(X_{j} \in \mathcal{B} \mid X_{i}=\xi_{i}\right)$ such that for every value $\xi_{i} \in \mathcal{X}_{i}$ it satisfies

$$
\begin{aligned}
\mathbb{P}_{\mathcal{M}_{\text {do }\left(I, \xi_{I}\right)}}\left(X_{j} \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right) & =\mathbb{P}_{\tilde{\mathcal{M}}}\left(X_{j} \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right) \\
& =\mathbb{P}_{\tilde{\mathcal{M}}}\left(\left(\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}\right)_{j}\left(X_{i}, \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}\right) \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right) \\
& =\mathbb{P}_{\tilde{\mathcal{M}}}\left(\left(\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}\right)_{j}\left(\xi_{i}, \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}\right) \in \mathcal{B}_{j} \mid X_{i}=\xi_{i}\right) \\
& =\mathbb{P}_{\tilde{\mathcal{M}}}\left(\left(\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}\right)_{j}\left(\xi_{i}, \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}\right) \in \mathcal{B}_{j}\right) \\
& =\mathbb{P}_{\tilde{\mathcal{M}}_{\mathrm{do}\left(\{i\}, \xi_{i}\}}}\left(\left(\boldsymbol{g}_{\mathcal{A}_{j}^{\backslash i}}\right)_{j}\left(X_{i}, \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}\right) \in \mathcal{B}_{j}\right) \\
& =\mathbb{P}_{\tilde{\mathcal{M}}_{\mathrm{do}\left(\{i\}, \xi_{i}\}}}\left(X_{j} \in \mathcal{B}_{j}\right) \\
& =\mathbb{P}_{\left(\mathcal{M}_{\text {do }\left(I, \xi_{I}\right)}\right)_{\text {do }\left(\{i\}, \xi_{i}\right)}}\left(X_{j} \in \mathcal{B}_{j}\right)
\end{aligned}
$$

where we used $X_{i} \perp \boldsymbol{E}_{\overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right)}$ in the fourth equality.
If we assume $i \notin \overline{\mathrm{pa}}\left(\mathcal{A}_{j}^{\backslash i}\right) \backslash \mathcal{A}_{j}^{\backslash i}$ instead of $i \in \mathrm{pa}\left(\mathcal{A}_{j}^{\backslash i}\right) \backslash \mathcal{A}_{j}^{\backslash i}$, then we similarly arrive at the same conclusion.

# Section 8 

Proof of Proposition 8.2. We first show that the class of simple SCMs is closed under marginalization. Take two disjoint subsets $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ in $\mathcal{I}$. Then, it suffices to show that $\mathcal{M}_{\operatorname{marg}\left(\mathcal{L}_{1}\right)}$ is uniquely solvable w.r.t. $\mathcal{L}_{2}$. This follows directly from Proposition 5.4.

To show that the class of simple SCMs is closed under perfect intervention. Let $\mathcal{M}$ be a simple SCM, $\mathcal{O} \subseteq \mathcal{I}, I \subseteq \mathcal{I}$ and $\boldsymbol{\xi}_{I} \in \boldsymbol{X}_{I}$. Define $\mathcal{O}_{1}:=\mathcal{O} \cap I$ and $\mathcal{O}_{2}:=\mathcal{O} \backslash I$, then $\mathcal{O}=\mathcal{O}_{1} \cup \mathcal{O}_{2}$. Note that $\operatorname{pa}\left(\mathcal{O}_{2}\right) \backslash \mathcal{O}_{2}=\left(\operatorname{pa}\left(\mathcal{O}_{2}\right) \backslash\left(\mathcal{O}_{2} \cup I\right)\right) \cup\left(\operatorname{pa}\left(\mathcal{O}_{2}\right) \cap I\right)$ and $\operatorname{pa}\left(\mathcal{O}_{2}\right) \backslash$ $\left(\mathcal{O}_{2} \cup I\right) \subseteq \operatorname{pa}(\mathcal{O}) \backslash \mathcal{O}$. Let $\boldsymbol{g}_{\mathcal{O}_{2}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{O}_{2}\right) \backslash \mathcal{O}_{2}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}\left(\mathcal{O}_{2}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}_{2}}$ be a measurable solution function for $\mathcal{M}$ w.r.t. $\mathcal{O}_{2}$. The mapping $\tilde{\boldsymbol{g}}_{\mathcal{O}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}(\mathcal{O})} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}}$ defined by

$$
\left\{\begin{array}{l}
\left(\tilde{\boldsymbol{g}}_{\mathcal{O}}\right)_{\mathcal{O}_{1}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right):=\boldsymbol{\xi}_{\mathcal{O}_{1}} \\
\left(\tilde{\boldsymbol{g}}_{\mathcal{O}}\right)_{\mathcal{O}_{2}}\left(\boldsymbol{x}_{\mathrm{pa}(\mathcal{O}) \backslash \mathcal{O}}, \boldsymbol{e}_{\mathrm{pa}(\mathcal{O})}\right):=\boldsymbol{g}_{\mathcal{O}_{2}}\left(\boldsymbol{x}_{\mathrm{pa}\left(\mathcal{O}_{2}\right) \backslash\left(\mathcal{O}_{2} \cup I\right)}, \boldsymbol{\xi}_{\mathrm{pa}\left(\mathcal{O}_{2}\right) \cap I}, \boldsymbol{e}_{\mathrm{pa}\left(\mathcal{O}_{2}\right)}\right)
\end{array}\right.
$$

is a measurable solution function for $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ w.r.t. $\mathcal{O}$, and it is clear that $\mathcal{M}_{\mathrm{do}\left(I, \xi_{I}\right)}$ is uniquely solvable w.r.t. $\mathcal{O}$.

Next, we show that the class of simple SCMs is closed under the twin operation. Let $\tilde{\mathcal{O}} \subseteq \mathcal{I} \cup \mathcal{I}^{\prime}$. Take $\mathcal{O}_{1}=\tilde{\mathcal{O}} \cap \mathcal{I}, \mathcal{O}_{2}^{\prime}=\tilde{\mathcal{O}} \cap \mathcal{I}^{\prime}$ and $\mathcal{O}_{2}$ the original copy of $\mathcal{O}_{2}^{\prime}$ in $\mathcal{I}$. Let $\boldsymbol{g}_{\mathcal{O}_{1}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{O}_{1}\right) \backslash \mathcal{O}_{1}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}\left(\mathcal{O}_{1}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}_{1}}$ and $\boldsymbol{g}_{\mathcal{O}_{2}}: \boldsymbol{\mathcal { X }}_{\mathrm{pa}\left(\mathcal{O}_{2}\right) \backslash \mathcal{O}_{2}} \times \boldsymbol{\mathcal { E }}_{\mathrm{pa}\left(\mathcal{O}_{2}\right)} \rightarrow \boldsymbol{\mathcal { X }}_{\mathcal{O}_{2}}$ be measurable solution functions for $\mathcal{M}$ w.r.t. $\mathcal{O}_{1}$ and $\mathcal{O}_{2}$, respectively. Define now the mapping $\boldsymbol{h}_{\tilde{\mathcal{O}}}: \boldsymbol{\mathcal { X }}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}}) \backslash \tilde{\mathcal{O}}} \times \boldsymbol{\mathcal { E }}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}})} \rightarrow \boldsymbol{\mathcal { X }}_{\tilde{\mathcal{O}}}$ by

$$
\begin{aligned}
& \left(\boldsymbol{h}_{\tilde{\mathcal{O}}}\right)_{\tilde{\mathcal{O}}} \mathcal{E}_{\mathcal{I}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}}) \backslash \tilde{\mathcal{O}}}, \boldsymbol{e}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}})}\right):=\boldsymbol{g}_{\mathcal{O}_{1}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}\left(\mathcal{O}_{1}\right) \backslash \mathcal{O}_{1}}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{O}_{1}\right)}\right) \\
& \left(\boldsymbol{h}_{\tilde{\mathcal{O}}}\right)_{\tilde{\mathcal{O}}} \mathcal{E}_{\mathcal{I}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}}) \backslash \tilde{\mathcal{O}}}, \boldsymbol{e}_{\overline{\mathrm{pa}}(\tilde{\mathcal{O}})}\right):=\boldsymbol{g}_{\mathcal{O}_{2}}\left(\boldsymbol{x}_{\overline{\mathrm{pa}}\left(\mathcal{O}_{2}^{\prime}\right) \backslash \mathcal{O}_{2}^{\prime}}, \boldsymbol{e}_{\overline{\mathrm{pa}}\left(\mathcal{O}_{2}^{\prime}\right)}\right)
\end{aligned}
$$

where we define $\overline{\mathrm{pa}}:=\mathrm{pa}_{\mathcal{G}^{a}}\left(\mathcal{M}^{\text {twin }}\right)$ as the parents w.r.t. the twin graph $\mathcal{G}^{a}\left(\mathcal{M}^{\text {twin }}\right)$. Then by construction this mapping $\boldsymbol{h}_{\tilde{\mathcal{O}}}$ is a measurable solution function for $\mathcal{M}^{\text {twin }}$ w.r.t. $\tilde{\mathcal{O}}$, and it is clear that $\mathcal{M}^{\text {twin }}$ is uniquely solvable w.r.t. $\tilde{\mathcal{O}}$.

Lastly, it follows that the observational and all the intervened models of $\mathcal{M}$ and $\mathcal{M}^{\text {twin }}$ are uniquely solvable. From Theorem 3.6 we conclude that $\mathcal{M}$ induces unique observational, interventional and counterfactual distributions.

Proof of Corollary 8.3. This follows from Corollary A. 22 .

# APPENDIX F: MEASURABLE SELECTION THEOREMS 

In this appendix, we derive some lemmas and state two measurable selection theorems that are used in several proofs in Appendix E. First, we introduce the measure theoretic notation and terminology needed to understand the results (see [30] for more details).

DEFINITION F. 1 (Standard measurable space). A measurable space $(\boldsymbol{X}, \boldsymbol{\Sigma})$ is a standard measurable space if it is isomorphic to $(\boldsymbol{\mathcal { Y }}, \mathcal{B}(\boldsymbol{\mathcal { Y }}))$, where $\boldsymbol{\mathcal { Y }}$ is a Polish space, that is, a separable completely metrizable space, ${ }^{22}$ and $\mathcal{B}(\boldsymbol{\mathcal { Y }})$ are the Borel subsets of $\boldsymbol{\mathcal { Y }}$, that is, the $\sigma$ algebra generated by the open sets in $\boldsymbol{\mathcal { Y }}$. A measure space $(\boldsymbol{X}, \boldsymbol{\Sigma}, \boldsymbol{\mu})$ is a standard probability space if $(\boldsymbol{X}, \boldsymbol{\Sigma})$ is a standard measurable space and $\boldsymbol{\mu}$ is a probability measure.

Examples of standard measurable spaces are the open and closed subsets of $\mathbb{R}^{d}$, and the finite sets with the usual complete metric. If we say that $\boldsymbol{X}$ is a standard measurable space, then we implicitly assume that there exists a $\sigma$-algebra $\boldsymbol{\Sigma}$ such that $(\boldsymbol{X}, \boldsymbol{\Sigma})$ is a standard measurable space. Similarly, if we say that $\boldsymbol{X}$ is a standard probability space with probability measure $\mathbb{P}_{\boldsymbol{X}}$, then we implicitly assume that there exists a $\sigma$-algebra $\boldsymbol{\Sigma}$ such that $\left(\boldsymbol{X}, \boldsymbol{\Sigma}, \mathbb{P}_{\boldsymbol{X}}\right)$ is a standard probability space.

DEFINITION F. 2 (Analytic set). Let $\boldsymbol{X}$ be a Polish space. A set $\boldsymbol{\mathcal { A }} \subseteq \boldsymbol{X}$ is called analytic if there exist a Polish space $\boldsymbol{\mathcal { Y }}$ and a continuous mapping $\boldsymbol{f}: \boldsymbol{\mathcal { Y }} \rightarrow \boldsymbol{X}$ with $\boldsymbol{f}(\boldsymbol{\mathcal { Y }})=\boldsymbol{\mathcal { A }}$.

LEMMA F.3. Let $\boldsymbol{X}$ and $\boldsymbol{\mathcal { Y }}$ be standard measurable spaces and $\boldsymbol{f}: \boldsymbol{X} \rightarrow \boldsymbol{\mathcal { Y }}$ a measurable mapping. Then

1. every measurable set $\boldsymbol{\mathcal { A }} \subseteq \boldsymbol{X}$ is analytic;
2. if the subsets $\boldsymbol{\mathcal { A }} \subseteq \boldsymbol{X}$ and $\tilde{\boldsymbol{\mathcal { A }}} \subseteq \boldsymbol{\mathcal { Y }}$ are analytic, then the sets $\boldsymbol{f}(\boldsymbol{\mathcal { A }})$ and $\boldsymbol{f}^{-1}(\tilde{\boldsymbol{\mathcal { A }}})$ are analytic.

Proof. From Proposition 13.7 in [30] it follows that every measurable set $\boldsymbol{\mathcal { A }} \subseteq \boldsymbol{X}$ is analytic. From Proposition 14.4.(ii) in [30] it follows that the image and the preimage of an analytic set is an analytic set.

DEFINITION F. 4 ( $\boldsymbol{\mu}$-measurability). Let $(\boldsymbol{X}, \boldsymbol{\Sigma}, \boldsymbol{\mu})$ be a measure space. A set $\boldsymbol{\mathcal { E }} \subseteq \boldsymbol{X}$ is called a $\boldsymbol{\mu}$-null set if there exists a $\boldsymbol{\mathcal { A }} \in \boldsymbol{\Sigma}$ with $\boldsymbol{\mathcal { E }} \subseteq \boldsymbol{\mathcal { A }}$ and $\boldsymbol{\mu}(\boldsymbol{\mathcal { A }})=0$. We denote the class of $\boldsymbol{\mu}$-null sets by $\boldsymbol{\mathcal { N }}$, and we denote the $\sigma$-algebra generated by $\boldsymbol{\Sigma} \cup \boldsymbol{\mathcal { N }}$ by $\boldsymbol{\Sigma}$, and its members are called the $\boldsymbol{\mu}$-measurable sets. Note that each member of $\bar{\Sigma}$ is of the form $\boldsymbol{\mathcal { A }} \cup \boldsymbol{\mathcal { E }}$ with $\boldsymbol{\mathcal { A }} \in \boldsymbol{\Sigma}$ and $\boldsymbol{\mathcal { E }} \in \boldsymbol{\mathcal { N }}$. The measure $\boldsymbol{\mu}$ is extended to a measure $\bar{\mu}$ on $\bar{\Sigma}$, by $\bar{\mu}(\boldsymbol{\mathcal { A }} \cup \boldsymbol{\mathcal { E }})=\boldsymbol{\mu}(\boldsymbol{\mathcal { A }})$ for every $\boldsymbol{\mathcal { A }} \in \boldsymbol{\Sigma}$ and $\boldsymbol{\mathcal { E }} \in \boldsymbol{\mathcal { N }}$, and is called its completion. A mapping $\boldsymbol{f}: \boldsymbol{X} \rightarrow \boldsymbol{\mathcal { Y }}$ between measurable spaces is called $\boldsymbol{\mu}$-measurable if the inverse image $\boldsymbol{f}^{-1}(\boldsymbol{\mathcal { C }})$ of every measurable set $\boldsymbol{\mathcal { C }} \subseteq \boldsymbol{\mathcal { Y }}$ is $\boldsymbol{\mu}$-measurable.

[^0]
[^0]:    ${ }^{22}$ A metrizable space is a topological space $\boldsymbol{X}$ for which there exists a metric $d$ such that $(\boldsymbol{X}, d)$ is a metric space and induces the topology on $\boldsymbol{X}$. For a metric space $(\boldsymbol{X}, d)$, a Cauchy sequence is a sequence $\left(x_{n}\right)_{n \in \mathbb{N}}$ of elements of $\boldsymbol{X}$ such that for every $\epsilon>0$ there exists an $N \in \mathbb{N}$ such that for all natural numbers $p, q>N$ we have $d\left(x_{n}, x_{m}\right)<\epsilon$. We call $(\boldsymbol{X}, d)$ complete if every Cauchy sequence has a limit in $\boldsymbol{X}$. A completely metrizable space is a topological space $\boldsymbol{X}$ for which there exists a metric $d$ such that $(\boldsymbol{X}, d)$ is a complete metric space that induces the topology on $\boldsymbol{X}$. A topological space $\boldsymbol{X}$ is called separable if it contains a countable dense subset, that is, there exists a sequence $\left(x_{n}\right)_{n \in \mathbb{N}}$ of elements in $\boldsymbol{X}$ such that every nonempty open subset of $\boldsymbol{X}$ contains at least one element of the sequence. A separable completely metrizable space is called a Polish space (see [9] and [30] for more details).

DEFINITION F. 5 (Universal measurability). Let $(\boldsymbol{X}, \boldsymbol{\Sigma})$ be a standard measurable space. A set $\mathcal{A} \subseteq \boldsymbol{X}$ is called universally measurable if it is $\boldsymbol{\mu}$-measurable for every $\sigma$-finite measure ${ }^{23} \boldsymbol{\mu}$ on $\boldsymbol{X}$ (i.e., in particular every probability measure). A mapping $\boldsymbol{f}: \boldsymbol{X} \rightarrow \boldsymbol{\mathcal { Y }}$ between standard measurable spaces is universally measurable if it is $\boldsymbol{\mu}$-measurable for every $\sigma$-finite measure $\boldsymbol{\mu}$.

LEMMA F.6. Let $\mathcal{E}$ be a standard probability space with probability measure $\mathbb{P}_{\mathcal{E}}$ and $\mathcal{A} \subseteq \mathcal{E}$ an analytic set. Then $\mathcal{A}$ is $\mathbb{P}_{\mathcal{E}}$-measurable and there exist measurable sets $\mathcal{S}, \mathcal{T} \subseteq \mathcal{E}$ such that $\mathcal{S} \subseteq \mathcal{A} \subseteq \mathcal{T}$ and $\mathbb{P}_{\mathcal{E}}(\mathcal{S})=\overline{\mathbb{P}}_{\mathcal{E}}(\mathcal{A})=\mathbb{P}_{\mathcal{E}}(\mathcal{T})$, where $\overline{\mathbb{P}}_{\mathcal{E}}$ is the completion of $\mathbb{P}_{\mathcal{E}}$.

Proof. Let $\mathcal{A} \subseteq \mathcal{E}$ be an analytic set. Since every analytic set in a standard measurable space is a universally measurable set (see Theorem 21.10 in [30]), we know that $\mathcal{A}$ is a universally measurable set, and hence it is in particular a $\mathbb{P}_{\mathcal{E}}$-measurable set. Thus, there exist a measurable set $\mathcal{S} \subseteq \mathcal{E}$ and a $\mathbb{P}_{\mathcal{E}}$-null set $\mathcal{C} \subseteq \mathcal{E}$ such that $\mathcal{A}=\mathcal{S} \cup \mathcal{C}$ and $\overline{\mathbb{P}}_{\mathcal{E}}(\mathcal{A})=\mathbb{P}_{\mathcal{E}}(\mathcal{S})$, where $\overline{\mathbb{P}}_{\mathcal{E}}$ is the completion of $\mathbb{P}_{\mathcal{E}}$. Moreover, there exists a measurable set $\mathcal{C} \subseteq \mathcal{E}$ such that $\mathcal{C} \subseteq \overline{\mathcal{C}}$ and $\mathbb{P}_{\mathcal{E}}(\overline{\mathcal{C}})=0$. Let $\mathcal{T}:=\mathcal{S} \cup \overline{\mathcal{C}}$, then $\mathcal{A} \subseteq \mathcal{T}$ and $\mathbb{P}_{\mathcal{E}}(\mathcal{T})=\mathbb{P}_{\mathcal{E}}(\mathcal{S})$.

LEMMA F.7. Let $\boldsymbol{f}: \mathcal{X} \rightarrow \boldsymbol{\mathcal { Y }}$ be a $\boldsymbol{\mu}$-measurable mapping. If $\boldsymbol{\mathcal { Y }}$ is countably generated, then there exists a measurable mapping $\boldsymbol{g}: \boldsymbol{X} \rightarrow \boldsymbol{\mathcal { Y }}$ such that $\boldsymbol{f}(\boldsymbol{x})=\boldsymbol{g}(\boldsymbol{x})$ holds $\boldsymbol{\mu}$-a.e..

Proof. Let the $\sigma$-algebra of $\boldsymbol{\mathcal { Y }}$ be generated by the countable generating set $\left\{\mathcal{C}_{n}\right\}_{n \in \mathbb{N}}$. The $\boldsymbol{\mu}$-measurable set $\boldsymbol{f}^{-1}\left(\mathcal{C}_{n}\right)=\mathcal{A}_{n} \cup \mathcal{E}_{n}$ for some $\mathcal{A}_{n} \in \boldsymbol{\Sigma}$ and some $\mathcal{E}_{n} \in \mathcal{N}$ and hence there is some $\mathcal{E}_{n} \subseteq \boldsymbol{\mathcal { B } _ { n } \in \boldsymbol { \Sigma }}$ such that $\boldsymbol{\mu}\left(\boldsymbol{\mathcal { B } _ { n }}\right)=0$. Let $\overline{\boldsymbol{\mathcal { B }}}=\cup_{n \in \mathbb{N}} \boldsymbol{\mathcal { B } _ { n }}, \boldsymbol{\mathcal { A } _ { n }}=\boldsymbol{\mathcal { A } _ { n }} \backslash \overline{\boldsymbol{\mathcal { B }}}$ and $\overline{\boldsymbol{\mathcal { A }}}=\cup_{n \in \mathbb{N}} \boldsymbol{\mathcal { A } _ { n }}$, then $\boldsymbol{\mu}(\overline{\boldsymbol{\mathcal { B }}})=0, \overline{\boldsymbol{\mathcal { A }}}$ and $\overline{\boldsymbol{\mathcal { B }}}$ are disjoint and $\boldsymbol{\mathcal { X }}=\boldsymbol{\mathcal { A }} \cup \overline{\boldsymbol{\mathcal { B }}}$. Now define the mapping $\boldsymbol{g}: \boldsymbol{X} \rightarrow \boldsymbol{\mathcal { Y }}$ by

$$
\boldsymbol{g}(\boldsymbol{x}):= \begin{cases}\boldsymbol{f}(\boldsymbol{x}) & \text { if } \boldsymbol{x} \in \overline{\boldsymbol{\mathcal { A }}}, \\ \boldsymbol{y}_{0} & \text { otherwise }\end{cases}
$$

where for $\boldsymbol{y}_{0}$ we can take an arbitrary point in $\boldsymbol{\mathcal { P }}$. This mapping $\boldsymbol{g}$ is measurable since for each generator $\mathcal{C}_{n}$ we have

$$
\boldsymbol{g}^{-1}\left(\mathcal{C}_{n}\right)= \begin{cases}\overline{\boldsymbol{\mathcal { A }}}_{n} & \text { if } \boldsymbol{y}_{0} \notin \mathcal{C}_{n} \\ \overline{\boldsymbol{\mathcal { A }}}_{n} \cup \overline{\boldsymbol{\mathcal { B }}} & \text { otherwise }\end{cases}
$$

is in $\boldsymbol{\Sigma}$. Moreover, $\boldsymbol{f}(\boldsymbol{x})=\boldsymbol{g}(\boldsymbol{x}) \boldsymbol{\mu}$-almost everywhere.
With this result at hand we can now prove the first measurable selection theorem.
THEOREM F. 8 (Measurable selection theorem). Let $\mathcal{E}$ be a standard probability space with probability measure $\mathbb{P}_{\mathcal{E}}, \mathcal{X}$ a standard measurable space and $\mathcal{S} \subseteq \mathcal{E} \times \mathcal{X}$ a measurable set such that $\mathcal{E} \backslash \boldsymbol{p r}_{\mathcal{E}}(\mathcal{S})$ is a $\mathbb{P}_{\mathcal{E}}$-null set, where $\boldsymbol{p r}_{\mathcal{E}}: \mathcal{E} \times \mathcal{X} \rightarrow \mathcal{E}$ is the projection mapping on $\mathcal{E}$. Then there exists a measurable mapping $\boldsymbol{g}: \mathcal{E} \rightarrow \mathcal{X}$ such that $(\boldsymbol{e}, \boldsymbol{g}(\boldsymbol{e})) \in \mathcal{S}$ for $\mathbb{P}_{\mathcal{E}}$ almost every $\boldsymbol{e} \in \mathcal{E}$.

Proof. Take the subset $\hat{\mathcal{E}}:=\mathcal{E} \backslash \boldsymbol{B}$, for some measurable set $\boldsymbol{B} \supseteq \mathcal{E} \backslash \boldsymbol{p r}_{\mathcal{E}}(\boldsymbol{S})$ and $\mathbb{P}_{\mathcal{E}}(\boldsymbol{B})=0$, and note that $\hat{\mathcal{E}}$ is a standard measurable space (see Corollary 13.4 in [30]) and

[^0]
[^0]:    ${ }^{23}$ A measure $\boldsymbol{\mu}$ on a measurable space $(\boldsymbol{X}, \boldsymbol{\Sigma})$ is called $\sigma$-finite if $\boldsymbol{X}=\cup_{n \in \mathbb{N}} \boldsymbol{A}_{n}$, with $\boldsymbol{A}_{n} \in \boldsymbol{\Sigma}, \boldsymbol{\mu}\left(\boldsymbol{A}_{n}\right)<$ $\infty$.

$\hat{\boldsymbol{\mathcal { E }}} \subseteq \boldsymbol{p r}_{\boldsymbol{\mathcal { E }}}(\boldsymbol{\mathcal { S}})$. Let $\hat{\boldsymbol{\mathcal { S }}}=\boldsymbol{\mathcal { S }} \cap(\hat{\boldsymbol{\mathcal { E }}} \times \boldsymbol{\mathcal { X}})$. Because the set $\hat{\boldsymbol{\mathcal { S }}}$ is measurable, it is in particular analytic (see Lemma F.3). It follows by the Jankov-von Neumann Theorem (see Theorem 18.8 or 29.9 in [30]) that $\hat{\boldsymbol{\mathcal { S }}}$ has a universally measurable uniformizing function, that is, there exists a universally measurable mapping $\hat{\boldsymbol{g}}: \hat{\boldsymbol{\mathcal { E }}} \rightarrow \boldsymbol{\mathcal { X }}$ such that for all $\boldsymbol{e} \in \hat{\boldsymbol{\mathcal { E }}},(\boldsymbol{e}, \hat{\boldsymbol{g}}(\boldsymbol{e})) \in \hat{\boldsymbol{\mathcal { S }}}$. Hence, in particular, it is $\left.\mathbb{P}_{\boldsymbol{\mathcal { E }}}\right|_{\hat{\boldsymbol{E}}}$-measurable, where $\left.\mathbb{P}_{\boldsymbol{\mathcal { E }}}\right|_{\hat{\boldsymbol{E}}}$ is the restriction of $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$ to $\hat{\boldsymbol{\mathcal { E }}}$.

Now define the mapping $\boldsymbol{g}^{*}: \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}$ by

$$
\boldsymbol{g}^{*}(\boldsymbol{e}):= \begin{cases}\hat{\boldsymbol{g}}(\boldsymbol{e}) & \text { if } \boldsymbol{e} \in \hat{\boldsymbol{\mathcal { E }}} \\ \boldsymbol{x}_{0} & \text { otherwise }\end{cases}
$$

where for $\boldsymbol{x}_{0}$ we can take an arbitrary point in $\boldsymbol{\mathcal { X }}$. Then this mapping $\boldsymbol{g}^{*}$ is $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-measurable. To see this, take any measurable set $\mathcal{C} \subseteq \mathcal{X}$, then

$$
\boldsymbol{g}^{*-1}(\mathcal{C})= \begin{cases}\hat{\boldsymbol{g}}^{-1}(\mathcal{C}) & \text { if } \boldsymbol{x}_{\mathbf{0}} \notin \mathcal{C} \\ \hat{\boldsymbol{g}}^{-1}(\mathcal{C}) \cup \mathcal{B} & \text { otherwise }\end{cases}
$$

Because $\hat{\boldsymbol{g}}^{-1}(\mathcal{C})$ is $\left.\mathbb{P}_{\boldsymbol{\mathcal { E }}}\right|_{\hat{\boldsymbol{E}}}$-measurable it is also $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-measurable and thus $\boldsymbol{g}^{*-1}(\mathcal{C})$ is $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$ measurable.

By Lemma F. 7 and the fact that standard measurable spaces are countably generated (see Proposition 12.1 in [30]), we prove the existence of a measurable mapping $\boldsymbol{g}: \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { X }}$ such that $\boldsymbol{g}^{*}=\boldsymbol{g} \mathbb{P}_{\boldsymbol{\mathcal { E }}}$-a.e. and thus it satisfies $(\boldsymbol{e}, \boldsymbol{g}(\boldsymbol{e})) \in \boldsymbol{\mathcal { S }}$ for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$.

This theorem rests on the assumption that the standard measurable space $\boldsymbol{\mathcal { E }}$ has a probability measure $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$. If this space becomes the product space $\boldsymbol{\mathcal { Y }} \times \boldsymbol{\mathcal { E }}$, for some standard measurable space $\boldsymbol{\mathcal { Y }}$ where only the space $\boldsymbol{\mathcal { E }}$ has a probability measure, then in general this theorem does not hold anymore. However, if we assume in addition that the fibers of $\boldsymbol{\mathcal { S }}$ in $\boldsymbol{\mathcal { Y }}$ are $\sigma$-compact for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$, then we can prove a second measurable selection theorem. A topological space is $\sigma$-compact if it is the union of countably many compact subspaces. For example, all countable discrete spaces, every interval of the real line, and moreover all the Euclidean spaces are $\sigma$-compact spaces.

THEOREM F. 9 (Second measurable selection theorem). Let $\boldsymbol{\mathcal { E }}$ be a standard probability space with probability measure $\mathbb{P}_{\boldsymbol{\mathcal { E }}}, \boldsymbol{\mathcal { X }}$ and $\boldsymbol{\mathcal { Y }}$ standard measurable spaces and $\boldsymbol{\mathcal { S }} \subseteq \boldsymbol{\mathcal { X }} \times$ $\boldsymbol{\mathcal { E }} \times \boldsymbol{\mathcal { Y }}$ a measurable set such that $\boldsymbol{\mathcal { E }} \backslash \boldsymbol{\mathcal { K }}_{\sigma}$ is a $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-null set, where

$$
\boldsymbol{\mathcal { K }}_{\sigma}:=\left\{\boldsymbol{e} \in \boldsymbol{\mathcal { E }}: \forall \boldsymbol{x} \in \boldsymbol{\mathcal { X }}\left(\boldsymbol{\mathcal { S }}_{(\boldsymbol{x}, \boldsymbol{e})} \text { is nonempty and } \sigma \text {-compact }\right)\right\}
$$

with $\boldsymbol{\mathcal { S }}_{(\boldsymbol{x}, \boldsymbol{e})}$ denoting the fiber over $(\boldsymbol{x}, \boldsymbol{e})$, that is

$$
\boldsymbol{\mathcal { S }}_{(\boldsymbol{x}, \boldsymbol{e})}:=\{\boldsymbol{y} \in \boldsymbol{\mathcal { Y }}:(\boldsymbol{x}, \boldsymbol{e}, \boldsymbol{y}) \in \boldsymbol{\mathcal { S }}\}
$$

Then there exists a measurable mapping $\boldsymbol{g}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { Y }}$ such that for $\mathbb{P}_{\boldsymbol{\mathcal { E }}}$-almost every $\boldsymbol{e} \in \boldsymbol{\mathcal { E }}$ and for all $\boldsymbol{x} \in \boldsymbol{\mathcal { X }}$ we have $(\boldsymbol{x}, \boldsymbol{e}, \boldsymbol{g}(\boldsymbol{x}, \boldsymbol{e})) \in \boldsymbol{\mathcal { S }}$.

Proof. Take the subset $\hat{\boldsymbol{\mathcal { E }}}:=\boldsymbol{\mathcal { E }} \backslash \boldsymbol{\mathcal { B }}$, for some measurable set $\boldsymbol{\mathcal { B }} \supseteq \boldsymbol{\mathcal { E }} \backslash \boldsymbol{\mathcal { K }}_{\sigma}$ and $\mathbb{P}_{\boldsymbol{\mathcal { E }}}(\boldsymbol{\mathcal { B }})=0$. Note that $\hat{\boldsymbol{\mathcal { E }}}$ is a standard measurable space, $\hat{\boldsymbol{\mathcal { E }}} \subseteq \boldsymbol{\mathcal { K }}_{\sigma}$ and $\hat{\boldsymbol{\mathcal { S }}}=\boldsymbol{\mathcal { S }} \cap(\boldsymbol{\mathcal { X }} \times \hat{\boldsymbol{\mathcal { E }}} \times \boldsymbol{\mathcal { Y }})$ is measurable. By assumption, for each $(\boldsymbol{x}, \boldsymbol{e}) \in \boldsymbol{\mathcal { X }} \times \hat{\boldsymbol{\mathcal { E }}}$ the fiber $\hat{\boldsymbol{\mathcal { S }}}_{(\boldsymbol{x}, \boldsymbol{e})}$ is nonempty and $\sigma$-compact and hence by applying the Theorem of Arsenin-Kunugui (see Theorem 35.46 in [30]) it follows that the set $\hat{\boldsymbol{\mathcal { S }}}$ has a measurable uniformizing function, that is, there exists a measurable mapping $\hat{\boldsymbol{g}}: \boldsymbol{\mathcal { X }} \times \hat{\boldsymbol{\mathcal { E }}} \rightarrow \boldsymbol{\mathcal { Y }}$ such that for all $(\boldsymbol{x}, \boldsymbol{e}) \in \boldsymbol{\mathcal { X }} \times \hat{\boldsymbol{\mathcal { E }}},(\boldsymbol{x}, \boldsymbol{e}, \hat{\boldsymbol{g}}(\boldsymbol{x}, \boldsymbol{e})) \in \hat{\boldsymbol{\mathcal { S }}}$. Now define the mapping $\boldsymbol{g}: \boldsymbol{\mathcal { X }} \times \boldsymbol{\mathcal { E }} \rightarrow \boldsymbol{\mathcal { Y }}$ by

$$
\boldsymbol{g}(\boldsymbol{x}, \boldsymbol{e}):= \begin{cases}\hat{\boldsymbol{g}}(\boldsymbol{x}, \boldsymbol{e}) & \text { if } \boldsymbol{e} \in \hat{\boldsymbol{\mathcal { E }}} \\ \boldsymbol{y}_{0} & \text { otherwise }\end{cases}
$$

where for $\boldsymbol{y}_{0}$ we can take an arbitrary point in $\mathcal{Y}$. This mapping $\boldsymbol{g}$ inherits the measurability from $\hat{\boldsymbol{g}}$ and it satisfies for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ and for all $\boldsymbol{x} \in \mathcal{X}$ that $(\boldsymbol{x}, \boldsymbol{e}, \boldsymbol{g}(\boldsymbol{x}, \boldsymbol{e})) \in$ $\mathcal{S}$.

The next two lemmas provide some useful properties for the "for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ " quantifier.

Lemma F.10. Let $\phi: \mathcal{E} \rightarrow \overline{\mathcal{E}}$ be a measurable map between two standard measurable spaces. Let $\mathbb{P}_{\mathcal{E}}$ be a probability measure on $\mathcal{E}$ and let $\mathbb{P}_{\overline{\mathcal{E}}}=\mathbb{P}_{\mathcal{E}} \circ \phi^{-1}$ be its push-forward under $\phi$. Let $\tilde{P}: \overline{\mathcal{E}} \rightarrow\{0,1\}$ be a property, that is, a (measurable) boolean-valued function on $\overline{\mathcal{E}}$. Then the property $P=\tilde{P} \circ \phi$ on $\mathcal{E}$ holds $\mathbb{P}_{\mathcal{E}}$-a.e. if and only if the property $\tilde{P}$ holds $\mathbb{P}_{\overline{\mathcal{E}}}$-a.e..

Proof. Assume the property $P=\tilde{P} \circ \phi$ holds $\mathbb{P}_{\mathcal{E}}$-a.e., then $\mathcal{C}=\{\boldsymbol{e} \in \mathcal{E}: P(\boldsymbol{e})=1\}$ contains a measurable set $\mathcal{C}^{*}$ with $\mathbb{P}_{\mathcal{E}}$-measure 1 , that is, $\mathcal{C}^{*} \subseteq \mathcal{C}$ and $\mathbb{P}_{\mathcal{E}}\left(\mathcal{C}^{*}\right)=1$. By Lemma F.3, $\phi\left(\mathcal{C}^{*}\right)$ is analytic. By Lemma F.6, there exist measurable sets $\mathcal{A}, \mathcal{B}$ such that $\mathcal{A} \subseteq \phi\left(\mathcal{C}^{*}\right) \subseteq \mathcal{B}$ and $\mathbb{P}_{\overline{\mathcal{E}}}(\mathcal{A})=\mathbb{P}_{\overline{\mathcal{E}}}(\mathcal{B})$. Because $\phi$ is measurable, $\phi^{-1}(\mathcal{A})$ and $\phi^{-1}(\mathcal{B})$ are both measurable. Also, $\phi^{-1}(\mathcal{A}) \subseteq \phi^{-1}\left(\phi\left(\mathcal{C}^{*}\right)\right) \subseteq \phi^{-1}(\mathcal{B})$. As $\mathcal{C}^{*} \subseteq \phi^{-1}\left(\phi\left(\mathcal{C}^{*}\right)\right)$, we must have that $\mathbb{P}_{\mathcal{E}}\left(\phi^{-1}(\mathcal{B})\right) \geq \mathbb{P}_{\mathcal{E}}\left(\mathcal{C}^{*}\right)=1$. Hence $\mathbb{P}_{\overline{\mathcal{E}}}(\mathcal{A})=\mathbb{P}_{\overline{\mathcal{E}}}(\mathcal{B})=1$. Note that as $\mathcal{C}^{*} \subseteq \mathcal{C}$, $\mathcal{A} \subseteq \phi\left(\mathcal{C}^{*}\right) \subseteq \phi(\mathcal{C}) \subseteq\{\tilde{\boldsymbol{e}} \in \overline{\mathcal{E}}: \tilde{P}(\tilde{\boldsymbol{e}})=1\}$. Hence the set $\overline{\mathcal{C}}:=\{\tilde{\boldsymbol{e}} \in \overline{\mathcal{E}}: \tilde{P}(\tilde{\boldsymbol{e}})=1\}$ contains a measurable set of $\mathbb{P}_{\overline{\mathcal{E}}}$-measure 1 , in other words, $\tilde{P}$ holds $\mathbb{P}_{\overline{\mathcal{E}}}$-a.s..

The converse is easier to prove. Suppose $\overline{\mathcal{C}}=\{\tilde{\boldsymbol{e}} \in \overline{\mathcal{E}}: \tilde{P}(\tilde{\boldsymbol{e}})=1\}$ contains a measurable set $\overline{\mathcal{C}}^{*}$ with $\mathbb{P}_{\overline{\mathcal{E}}}$-measure 1 , that is, $\overline{\mathcal{C}}^{*} \subseteq \overline{\mathcal{C}}$ and $\mathbb{P}_{\overline{\mathcal{E}}}\left(\overline{\mathcal{C}}^{*}\right)=1$. Because $\phi$ is measurable, the set $\phi^{-1}\left(\overline{\mathcal{C}}^{*}\right)$ is measurable and $\mathbb{P}_{\mathcal{E}}\left(\phi^{-1}\left(\overline{\mathcal{C}}^{*}\right)\right)=1$, and furthermore, $\phi^{-1}\left(\overline{\mathcal{C}}^{*}\right) \subseteq \phi^{-1}(\overline{\mathcal{C}})=$ $\mathcal{C}$.

Lemma F. 11 (Some properties for the for-almost-every quantifier). Let $\mathcal{X}=\mathcal{X} \times \tilde{\mathcal{X}}$ and $\mathcal{E}=\mathcal{E} \times \tilde{\mathcal{E}}$ be products of nonempty standard measurable spaces and $\mathbb{P}_{\mathcal{E}}=\mathbb{P}_{\mathcal{E}} \times \mathbb{P}_{\tilde{\mathcal{E}}}$ be the product measure of probability measures $\mathbb{P}_{\mathcal{E}}$ and $\mathbb{P}_{\tilde{\mathcal{E}}}$ on $\mathcal{E}$ and $\tilde{\mathcal{E}}$, respectively. Denote by " $\forall \boldsymbol{e}$ " the quantifier "for $\mathbb{P}_{\mathcal{E}}$-almost every $\boldsymbol{e} \in \mathcal{E}$ " and by " $\forall \boldsymbol{x}$ " the quantifier "for all $\boldsymbol{x} \in \mathcal{X}$ ", and similarly for their components, for example, " $\forall e$ " for "for $\mathbb{P}_{\mathcal{E}}$-almost every $e \in \mathcal{E}$ " and " $\forall x$ " for "for all $x \in \mathcal{X}$ ". Then we have the following properties:

1. $\forall e: P(e) \Longrightarrow \exists e: P(e)$ (similarly to $\forall x: P(x) \Longrightarrow \exists x: P(x)$ );
2. $\forall e: P(e) \Longleftrightarrow \forall \boldsymbol{e}: P(e)$ (similarly to $\forall x: P(x) \Longleftrightarrow \forall \boldsymbol{x}: P(x)$ );
3. $\exists x \forall e: P(x, e) \Longrightarrow \forall e \exists x: P(x, e)$ (similarly to $\exists x \forall e: P(x, e) \Longrightarrow \forall e \exists x: P(x, e)$ );
4. $\forall e \forall x: P(x, e) \Longrightarrow \forall x \forall e: P(x, e)$ (similarly to $\forall e \forall x: P(x, e) \Longrightarrow \forall x \forall e: P(x, e)$ );
5. $\forall \boldsymbol{e}: P(\boldsymbol{e}) \Longrightarrow \exists \tilde{e} \forall e: P(\boldsymbol{e})$ (similarly to $\forall \boldsymbol{x}: P(\boldsymbol{x}) \Longrightarrow \exists \tilde{x} \forall x: P(\boldsymbol{x})$ );
6. $\forall e \forall x: P(x, e) \Longleftrightarrow \forall \boldsymbol{e} \forall \boldsymbol{x}: P(x, e)$;
7. $\forall \boldsymbol{e} \forall \boldsymbol{x}: P(\boldsymbol{x}, \boldsymbol{e}) \Longrightarrow \exists \tilde{e} \exists \tilde{x} \forall e \forall x: P(\boldsymbol{x}, \boldsymbol{e})$,
where $P$ denotes a property, that is, a measurable boolean-valued function, on the corresponding measurable spaces and we write $\boldsymbol{e}$ and $\boldsymbol{x}$ for $(e, \tilde{e})$ and $(x, \tilde{x})$, respectively.

Proof. We only prove the statements that may not be immediately obvious.
Property 2. Let $p r_{\mathcal{E}}: \mathcal{E} \rightarrow \mathcal{E}$ be the projection mapping on $\mathcal{E}$. Then by Lemma F. 10 we have

$$
\forall e: P(e) \Longleftrightarrow \forall \boldsymbol{e}: P \circ \operatorname{pr}_{\mathcal{E}}(\boldsymbol{e}) \Longleftrightarrow \forall \boldsymbol{e}: P(e)
$$

Property 4: We have

$$
\begin{aligned}
& \forall e \forall x: P(x, e) \\
& \Longrightarrow \exists \mathbb{P}_{\mathcal{E}} \text {-null set } N \forall e \in \mathcal{E} \backslash N \forall x: P(x, e) \\
& \Longrightarrow \exists \mathbb{P}_{\mathcal{E}} \text {-null set } N \forall x \forall e \in \mathcal{E} \backslash N: P(x, e) \\
& \Longrightarrow \forall x \exists \mathbb{P}_{\mathcal{E}} \text {-null set } N \forall e \in \mathcal{E} \backslash N: P(x, e) \\
& \Longrightarrow \forall x \forall e: P(x, e) .
\end{aligned}
$$

Property 5: Let $\boldsymbol{N}$ be a measurable $\mathbb{P}_{\mathcal{E}}$-null set such that $P(\boldsymbol{e})$ holds for all $\boldsymbol{e} \in \boldsymbol{\mathcal { E }} \backslash \boldsymbol{N}$. Define for $\tilde{e} \in \tilde{\mathcal{E}}$ the set $N_{\tilde{e}}:=\{e \in \mathcal{E}:(e, \tilde{e}) \in \boldsymbol{N}\}$. Note that the sets $N_{\tilde{e}}$ are measurable. From Fubini's theorem it follows that for $\mathbb{P}_{\tilde{\mathcal{E}}}$-almost every $\tilde{e} \in \tilde{\mathcal{E}}$ we have $\mathbb{P}_{\tilde{\mathcal{E}}}\left(N_{\tilde{e}}\right)=0$. That is, there exists a measurable $\mathbb{P}_{\tilde{\mathcal{E}}}$-null set $\tilde{N}$ such that $\mathbb{P}_{\mathcal{E}}\left(N_{\tilde{e}}\right)=0$ for all $\tilde{e} \in \tilde{\mathcal{E}} \backslash \tilde{N}$. Hence, there exists $\tilde{e} \in \tilde{\mathcal{E}} \backslash \tilde{N}$ such that $\mathbb{P}_{\mathcal{E}}\left(N_{\tilde{e}}\right)=0$; for all $e \in \mathcal{E} \backslash N_{\tilde{e}}, P(\boldsymbol{e})$ then holds. This means $\exists \tilde{e} \forall e: P(\boldsymbol{e})$.

Property 7: We have

$$
\begin{aligned}
& \forall \boldsymbol{e} \forall \boldsymbol{x}: P(\boldsymbol{x}, \boldsymbol{e}) \Longrightarrow \exists \tilde{e} \forall e \forall \boldsymbol{x}: P(\boldsymbol{x}, \boldsymbol{e}) \Longrightarrow \exists \tilde{e} \forall e \forall \tilde{x} \forall x: P(\boldsymbol{x}, \boldsymbol{e}) \\
& \Longrightarrow \exists \tilde{e} \forall \tilde{x} \forall e \forall x: P(\boldsymbol{x}, \boldsymbol{e}) \Longrightarrow \exists \tilde{e} \exists \tilde{x} \forall e \forall x: P(\boldsymbol{x}, \boldsymbol{e}),
\end{aligned}
$$

where in the first equivalence we used Property 5, in the third equivalence we used Property 4 and in the last equivalence we used Property 1.
