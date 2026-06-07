# Exact distribution theory for belief net responses 

Peter M. Hooper*


#### Abstract

Bayesian belief networks provide estimates of conditional probabilities, called query responses. The precision of these estimates is assessed using posterior distributions. This paper discusses two claims and a conjecture by Kleiter (1996) concerning the exact posterior distribution of queries. The two claims provide conditions where a query has an exact beta distribution. The first claim is clarified by the following generalization. Assuming a BDe prior and complete data, a query has the same distribution under equivalent network structures. If the query can be represented as a network parameter under an equivalent structure, it must then have a beta distribution. Kleiter's second claim is contradicted by a counterexample. His conjecture, concerning finite mixtures of beta distributions, is also disproved.


Keywords: Bayesian network, BDe prior, belief network, beta distribution, Dirichlet distribution, query response.

## 1 Introduction

Bayesian networks (belief networks) are concise models of joint probability distributions. These models can be used to estimate the probability of an event of interest given partial information. As a simple example, consider three binary variables: $A$ indicates the presence $a_{1}$ or absence $a_{2}$ of a medical condition while $B$ and $C$ each indicate the presence/absence of a symptom. Suppose the two symptoms are known to occur independently of one another among those who have the medical condition and also among those who do not; i.e., $B$ and $C$ are conditionally independent given $A$. This assumption is represented by the network $\{B \leftarrow A \rightarrow C\}$, where $A$ is called the parent of $B$ and $C$. Suppose we want to estimate the probability that a subject has the medical condition given that the subject exhibits both symptoms. Such probabilities are called query responses, or simply queries. Put $\theta_{a}=P\{A=a\}, \theta_{b \mid a}=P\{B=b \mid A=a\}$, etc. Applying Bayes Theorem, we have

$$
P\left\{A=a_{1} \mid B=b_{1}, C=c_{1}\right\}=\frac{\theta_{a_{1}} \theta_{b_{1} \mid a_{1}} \theta_{c_{1} \mid a_{1}}}{\theta_{a_{1}} \theta_{b_{1} \mid a_{1}} \theta_{c_{1} \mid a_{1}}+\theta_{a_{2}} \theta_{b_{1} \mid a_{2}} \theta_{c_{1} \mid a_{2}}}
$$

The $\theta$ probabilities are the parameters in the model. These parameters are estimated using data from a sample of subjects, then expression (A.1) is applied to estimate the query.

The precision of estimates is usually evaluated via the Bayesian paradigm; i.e., prior

[^0]
[^0]:    *Department of Mathematical and Statistical Sciences, University of Alberta, Edmonton, Alberta, Canada, mailto:hooper@stat.ualberta.ca

information is combined with data to obtain a posterior distribution for the parameters. The usual prior distributions assume that vectors of $\theta$ probabilities (summing to one) are independent Dirichlet random vectors. If we have complete data (i.e., all three variables are observed for each subject in the sample) then the posterior distribution has the same form as the prior. In this case, each $\theta$ parameter has a beta distribution. The joint distribution of the parameters determines a distribution for each query. This distribution is usually not analytically tractable, but can often be approximated to an acceptable degree of accuracy by a beta distribution. Kleiter (1996) describes a stochastic simulation technique to carry out this approximation. Van Allen, Singh, Greiner, and Hooper (2008) present a more direct approach, using a delta-rule approximation of the query variance, and prove that the beta approximation is asymptotically valid.

Kleiter (1996) also presents several claims concerning the exact distribution of queries. The present paper provides a critical analysis of this work. One claim is generalized using properties of BDe priors and equivalent network structures. This generalization clarifies how the choice of a prior distribution affects whether a query has an exact beta distribution. A counter-example is constructed for a second claim. The query in expression (A.1) typically does not have a beta distribution, contrary to Kleiter's Theorem 6. A conjecture concerning finite mixtures of beta distributions is also shown to be false. The paper is organized as follows: section 2 introduces notation and assumptions, section 3 presents the generalization, and section 4 discusses Kleiter's work.

# 2 Notation and assumptions 

Let $(\mathcal{V}, \mathcal{A})$ denote a Bayesian network, where $\mathcal{V}$ is a set of random variables (nodes) and $\mathcal{A}$ is a directed acyclic graph (DAG) structure encoding dependence assertions; i.e., a node is conditionally independent of its non-descendants given its parents. Denote variables by upper-case roman letters, realized values by lower-case, and vectors by boldface. Vectors (i.e., sets of variables listed in some order) are represented by concatenation; e.g., $\boldsymbol{Y}=A B$ and $\boldsymbol{y}=a b$. Vectors are sometimes treated as sets of variables; e.g., $A \in \boldsymbol{Y}$. Domains of network variables and vectors are denoted by $\mathcal{D}$; e.g., $\mathcal{D}_{\boldsymbol{Y}}=\mathcal{D}_{A} \times \mathcal{D}_{B}$. All such domains are assumed to be finite. When a vector is expressed in terms of subvectors, say $\boldsymbol{X}=\boldsymbol{A B C}$, it is implicitly assumed that the subvectors are pairwise disjoint.

Let $\boldsymbol{X}$ be a vector consisting of all variables in $\mathcal{V}$. The joint distribution of $\boldsymbol{X}$ is determined as a product of conditional probabilities of variables $C$ given parents $\mathrm{pa}(C)=\boldsymbol{F}$. These probabilities, denoted $\theta_{c \mid \boldsymbol{f}}$, are often presented in two-way tables $\left(\right.$ CPtables $\left.\boldsymbol{\theta}_{C \mid \boldsymbol{F}}\right)$, with rows indexed by $\mathcal{D}_{\boldsymbol{F}}$ and columns indexed by $\mathcal{D}_{C}$. Denote CPtable rows by $\boldsymbol{\theta}_{C \mid \boldsymbol{f}}$ and let $\boldsymbol{\Theta}=\left\langle\boldsymbol{\theta}_{C \mid \mathrm{pa}(C)}, C \in \mathcal{V}\right\rangle$ be a vector comprising all CPtable parameters. We express uncertainty about parameters by modeling $\boldsymbol{\Theta}$ as a random vector. Uncertainty propagates to query responses; i.e., the probability of a hypothesis $\boldsymbol{H}=\boldsymbol{h}$ given evidence $\boldsymbol{E}=\boldsymbol{e}$. Queries are denoted

$$
q_{\boldsymbol{h} \mid \boldsymbol{e}}=q_{\boldsymbol{h} \mid \boldsymbol{e}}(\boldsymbol{\Theta})=P(\boldsymbol{H}=\boldsymbol{h} \mid \boldsymbol{E}=\boldsymbol{e}, \boldsymbol{\Theta})
$$

We allow $\boldsymbol{E}=$ the empty set, writing $q_{\boldsymbol{h}}=P(\boldsymbol{H}=\boldsymbol{h} \mid \boldsymbol{\Theta})$. The notation in (A.2) emphasizes the fact that a query is a function of $\boldsymbol{\Theta}$, hence a random variable.

The posterior distribution of $q_{\boldsymbol{h} \mid \boldsymbol{e}}$ depends on whether one assumes that the data supporting the posterior distribution of $\boldsymbol{\Theta}$ include the partial observation $\boldsymbol{E}=\boldsymbol{e}$. The inclusion of $\boldsymbol{E}$ is appropriate when making a prediction based on observed evidence, but not when making an inference about a probability of merely potential interest. Our focus here is on the inferential problem. The addition of a partial observation typically has little effect on the query distribution, and has no effect at all when $q_{\boldsymbol{h} \mid \boldsymbol{e}}$ can be represented as a CPtable parameter under an equivalent network structure; see Section 3. There is a well-known formula that involves both conditioning frameworks: the mean of the query distribution (with $\boldsymbol{\Theta}$ conditioned on $\boldsymbol{E}$ ) is obtained by replacing parameters by their expected values (not conditioned on $\boldsymbol{E}$ ) before evaluating the query; i.e., $\mathcal{E}\left\{q_{\boldsymbol{h} \mid \boldsymbol{e}}(\boldsymbol{\Theta}) \mid \boldsymbol{E}=\boldsymbol{e}\right\}=q_{\boldsymbol{h} \mid \boldsymbol{e}}(\mathcal{E}\{\boldsymbol{\Theta}\})$. This result is implicit in Spiegelhalter and Lauritzen (1990) and explicit in Cooper and Herskovits (1992).

Now consider three assumptions; see Table 1 for an example.
Dirichlet prior. The prior distribution is assumed to have the usual properties: different CPtables are independent (global independence), rows within a CPtable are independent (local independence), and each row has a Dirichlet distribution:

$$
\boldsymbol{\theta}_{C \mid \boldsymbol{f}} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{C \mid \boldsymbol{f}}\right) \text { for each } \boldsymbol{f} \in \mathcal{D}_{\mathrm{pa}(C)}
$$

where $\boldsymbol{\alpha}_{C \mid \boldsymbol{f}}$ is a vector of positive weights $\alpha_{c \mid \boldsymbol{f}}$. It is convenient to indicate summation by replacing an index with a dot. The sum $\alpha_{\cdot \mid \boldsymbol{f}}=\sum_{c} \alpha_{c \mid \boldsymbol{f}}$ provides a measure of precision concerning the parameters, since (A.3) implies that each parameter has a beta distribution

$$
\theta_{c \mid \boldsymbol{f}} \sim \operatorname{Beta}\left(\alpha_{c \mid \boldsymbol{f}}, \alpha_{\cdot \mid \boldsymbol{f}}-\alpha_{c \mid \boldsymbol{f}}\right)
$$

with mean $\mu=\alpha_{c \mid \boldsymbol{f}} / \alpha_{\cdot \mid \boldsymbol{f}}$ and variance $\mu(1-\mu) /\left(1+\alpha_{\cdot \mid \boldsymbol{f}}\right)$. If $C$ is binary, then (A.4) is equivalent to (A.3) since the probabilities sum to one. The stronger Dirichlet assumption (A.3) is needed for general results concerning variables with finite domain.

BDe constraints. This assumption places restrictions on the prior weights so that prior information is equivalent to a weighted likelihood from a (possibly fictitious) sample of complete observations. Assume there exists a vector $\boldsymbol{\alpha}_{\boldsymbol{X}}=\left\langle\alpha_{\boldsymbol{x}}, \boldsymbol{x} \in \mathcal{D}_{\boldsymbol{X}}\right\rangle$ of positive weights such that the prior Dirichlet weights $\alpha_{c \mid \boldsymbol{f}}$ are obtained by summing $\alpha_{\boldsymbol{x}}$ over all $\boldsymbol{x} \in \mathcal{D}_{\boldsymbol{X}}$ with $C$ and $\mathrm{pa}(C)$ fixed at $c$ and $\boldsymbol{f}$. We refer to the $\alpha_{\boldsymbol{x}}$ as BDe weights, to distinguish them from the Dirichlet weights $\alpha_{c \mid \boldsymbol{f}}$. In practice, BDe weights might be specified as $\alpha_{\boldsymbol{x}}=\sum w_{i} I\left(\overline{\boldsymbol{y}}_{i}=\boldsymbol{x}\right)$, where $w_{i}>0, I$ is the $0 / 1$ indicator function, and each $\overline{\boldsymbol{y}}_{i} \in \mathcal{D}_{\boldsymbol{X}}$ is a (fictitious) complete observation. The BDe weights need not be uniquely determined from the Dirichlet weights unless $\boldsymbol{X}=\boldsymbol{A} B$ with $\mathrm{pa}(B)=\boldsymbol{A}$. BDe constraints were originally formulated to facilitate the learning of network structure (Heckerman, Geiger and Chickering, 1995).

Complete data. The posterior distribution is obtained from a sample of $n$ complete observations, where $n=0$ is allowed. Let $n_{c \boldsymbol{f}}$ denote the number of cases with $C=c$ and $\mathrm{pa}(C)=\boldsymbol{f}$. Given a Dirichlet prior and complete data, the posterior distribution

Table 1: Example of prior and posterior weights, both BDe and corresponding Dirichlet. The DAG structure is $\mathcal{A}=\{B \leftarrow A \rightarrow C\}$ with $A$ and $C$ binary, $B$ ternary. The prior assigns non-uniform weights for $B$, indicating an expectation that $b_{1}$ is most likely and $b_{3}$ is least likely, with total weight equivalent to a sample of six observations. The posterior weights are consistent with a sample of 100 observations. Sample frequencies are given by the difference in BDe weights (posterior minus prior). If the arc $B \rightarrow C$ were to be added, then $\alpha_{c \mid a}$ would be replaced by $\alpha_{c \mid a b}=\alpha_{a b c}$.


has the same form as the prior but with weights $\alpha_{c \mid \boldsymbol{f}}$ replaced by $\alpha_{c \mid \boldsymbol{f}}+n_{c \boldsymbol{f}}$. If the prior Dirichlet weights satisfy BDe constraints, then the posterior weights do as well. Let $\boldsymbol{y}_{i} \in \mathcal{D}_{\boldsymbol{X}}$ denote the sample observations. Posterior BDe weights are obtained by replacing the prior BDe weights $\alpha_{\boldsymbol{x}}$ with $\alpha_{\boldsymbol{x}}+\sum I\left(\boldsymbol{y}_{i}=\boldsymbol{x}\right)$. From now on $\alpha_{\boldsymbol{x}}$ and $\alpha_{c \mid \boldsymbol{f}}$ denote the posterior BDe and Dirichlet weights, since only the posterior distribution is relevant to our discussion.

# 3 Query distributions under equivalent DAG structures 

The induced dependence model for a DAG structure $\mathcal{A}$ is defined as the subset of triplets $\boldsymbol{A B C} \subseteq \boldsymbol{X}$ with $\boldsymbol{A}$ and $\boldsymbol{B}$ conditionally independent given $\boldsymbol{C}$. Two DAG structures are said to be equivalent if they induce the same dependence model. In general, a query can have different distributions under equivalent structures. However, if the prior distribution under each structure satisfies BDe constraints with the same BDe weight vector $\boldsymbol{\alpha}_{\boldsymbol{X}}$ for all structures, then a query must have the same distribution under equivalent structures. A query $q_{h \mid \boldsymbol{e}}$ must then have a beta distribution if it can be expressed as a parameter $\theta_{h \mid \boldsymbol{e}}$ for an equivalent structure. This result is implicit in theory showing that a metric associated with BDe constraints assigns equal support to equivalent DAG structures (Heckerman et al., 1995) and is also closely related to work by Geiger and Heckerman (1997) discussed below. For clarity, a separate proof is provided here. Two preliminary results are needed.

The proof employs a well-known connection between gamma and Dirichlet distribu-

tions; e.g., see Johnson and Kotz (1972), page 271. This connection is also used later in Section 4. A random variable $\gamma$ has a gamma distribution with shape parameter $\alpha$ and scale parameter $\beta$ if its density is $\exp (-g / \beta) g^{\alpha-1} \beta^{-\alpha} / \Gamma(\alpha)$ for $g>0$. The mean and variance of $\gamma$ are $\alpha \beta$ and $\alpha \beta^{2}$. If $\beta=1$, then we write $\gamma \sim \operatorname{Gamma}(\alpha)$.
Lemma 1. If $\gamma_{1}, \ldots, \gamma_{n}$ are independent with $\gamma_{i} \sim \operatorname{Gam}\left(\alpha_{i}\right)$, then $\gamma_{.}:=\sum \gamma_{i} \sim$ $\operatorname{Gam}(\alpha), \boldsymbol{\eta}:=\left\langle\gamma_{1} / \gamma_{.}, \ldots, \gamma_{n} / \gamma_{.}\right\rangle \sim \operatorname{Dir}\left(\alpha_{1}, \ldots, \alpha_{n}\right)$, and $\gamma$. and $\boldsymbol{\eta}$ are independent. Conversely, if $\boldsymbol{\eta}$ and $\gamma$ are independent with $\boldsymbol{\eta}:=\left\langle\eta_{1}, \ldots, \eta_{n}\right\rangle \sim \operatorname{Dir}\left(\alpha_{1}, \ldots, \alpha_{n}\right)$ and $\gamma \sim \operatorname{Gam}(\alpha)$, then $\gamma_{i}:=\gamma \eta_{i} \sim \operatorname{Gam}\left(\alpha_{i}\right)$ with $\gamma_{1}, \ldots, \gamma_{n}$ independent.

The proof also uses the following characterization of equivalent DAG structures (Chickering (1995), Heckerman et al. (1995)).
Lemma 2. Given $\mathrm{DAG} \mathcal{A}$, put $\boldsymbol{A}=\mathrm{pa}(B)$ and suppose $B$ is a parent of $C$. The arc $B \rightarrow C$ is said to be covered in $\mathcal{A}$ if $\mathrm{pa}(C)=\boldsymbol{A} B$. If $\mathcal{B}$ is obtained from $\mathcal{A}$ by replacing the covered arc $B \rightarrow C$ with $B \leftarrow C$, then the two DAGs are equivalent. In general, $\mathcal{A}$ and $\mathcal{B}$ are equivalent if and only if there exists a sequence of DAGs $\mathcal{A}_{1}, \ldots, \mathcal{A}_{m}$ over $\mathcal{V}$ such that $\mathcal{A}=\mathcal{A}_{1}, \mathcal{B}=\mathcal{A}_{m}$, and $\mathcal{A}_{i+1}$ is obtained from $\mathcal{A}_{i}$ by reversing a single arc that is covered in $\mathcal{A}_{i}$.

Theorem 1. If we have complete data and Dirichlet priors satisfying BDe constraints with common BDe weight vector $\boldsymbol{\alpha}_{\boldsymbol{X}}$, then a query $q_{\boldsymbol{h} \mid \boldsymbol{e}}$ has the same distribution under equivalent DAG structures.

Proof. Let $\mathcal{A}$ and $\mathcal{B}$ be equivalent DAG structures. By Lemma 2, it suffices to consider the case where $\mathcal{B}$ is obtained from $\mathcal{A}$ by reversing an arc $B \rightarrow C$ that is covered by $\boldsymbol{A}$. Fixing $\boldsymbol{a} \in \mathcal{D}_{\boldsymbol{A}}$, it then suffices to show that $q_{B C \mid \boldsymbol{a}}:=\left\langle q_{b c \mid \boldsymbol{a}}, b c \in \mathcal{D}_{B C}\right\rangle$ has the same joint distribution under both $\mathcal{A}$ and $\mathcal{B}$. Write $\boldsymbol{X}=\boldsymbol{A} B C \boldsymbol{Z}$, where $\boldsymbol{Z}$ includes all other variables. Applying Lemma 1, we represent relevant parameters in terms of independent random variables $\gamma_{b c} \sim \operatorname{Gam}\left(\alpha_{\boldsymbol{a} b c}\right)$; i.e., $\theta_{b \mid \boldsymbol{a}}:=\gamma_{b} / \gamma_{. .}, \theta_{c \mid \boldsymbol{a} b}:=\gamma_{b c} / \gamma_{b}$, $\theta_{c \mid \boldsymbol{a}}:=\gamma_{c} / \gamma_{. .}$, and $\theta_{b \mid \boldsymbol{a} c}:=\gamma_{b c} / \gamma_{. c}$. This representation satisfies all required joint distributions. Under $\mathcal{A}$, we have $q_{b c \mid \boldsymbol{a}}=\theta_{b \mid \boldsymbol{a}} \theta_{c \mid \boldsymbol{a} b}$ with independent $\boldsymbol{\theta}_{B \mid \boldsymbol{a}} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{\boldsymbol{a} B \cdot}\right)$ and $\boldsymbol{\theta}_{C \mid \boldsymbol{a} b} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{\boldsymbol{a} b C}\right)$. Under $\mathcal{B}$, we have $q_{b c \mid \boldsymbol{a}}=\theta_{c \mid \boldsymbol{a}} \theta_{b \mid \boldsymbol{a} c}$ with independent $\boldsymbol{\theta}_{C \mid \boldsymbol{a}} \sim$ $\operatorname{Dir}\left(\boldsymbol{\alpha}_{\boldsymbol{a} \cdot C}\right)$ and $\boldsymbol{\theta}_{B \mid \boldsymbol{a} c} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{\boldsymbol{a} B c}\right)$. Now $q_{b c \mid \boldsymbol{a}}=\gamma_{b c} / \gamma_{. .}$and $q_{B C \mid \boldsymbol{a}} \sim \operatorname{Dir}\left(\alpha_{\boldsymbol{a} B C}\right)$ under both $\mathcal{A}$ and $\mathcal{B}$.

Example 1. Consider three equivalent DAG structures obtained via Lemma 2.

$$
A \rightarrow B \rightarrow C \quad A \leftarrow B \rightarrow C \quad A \leftarrow B \leftarrow C
$$

Each structure induces the dependence model with $A$ and $C$ conditionally independent given $B$. Given common BDe weights $\alpha_{a b c}$, there are three equivalent representations of the joint distribution: $q_{a b c}=\theta_{a} \theta_{b \mid a} \theta_{c \mid b}=\theta_{a \mid b} \theta_{b} \theta_{c \mid b}=\theta_{a \mid b} \theta_{b \mid c} \theta_{c}$. The parameters within each product are independent and each parameter has a beta distribution; e.g., $\theta_{b \mid c} \sim \operatorname{Beta}\left(\alpha_{. b c}, \alpha_{. . c}-\alpha_{. b c}\right)$. This example can be generalized in several ways: extend the length of the chain, add common parents to the three variables, and add children to any or all variables. There is no restriction on structure among the added parents or children.

Geiger and Heckerman (1997) obtain a more fundamental result that relates beta-

distributed queries directly to structural hypotheses without requiring the assumption of a Dirichlet prior; i.e., they show that global independence, local independence, and invariance to representation of equivalent structures together imply a Dirichlet prior with BDe constraints. For the simplest nontrivial case, consider three assumptions for a network with $\boldsymbol{X}=A B$.
(i) The $\left|\mathcal{D}_{A}\right|+1$ random vectors $\left\{q_{A}, q_{B \mid a}, a \in \mathcal{D}_{A}\right\}$ are mutually independent; the $\left|\mathcal{D}_{B}\right|+1$ random vectors $\left\{q_{B}, q_{A \mid b}, b \in \mathcal{D}_{B}\right\}$ are mutually independent; and (after removing redundancies from variables summing to one) each set of variables has a strictly positive probability density function.
(ii) $q_{A B}$ has a Dirichlet distribution.
(iii) The network has structure $A \rightarrow B$, global independence, local independence, and Dirichlet prior with BDe constraints.

Geiger and Heckerman prove the equivalence of (i) and (ii). The equivalence of (ii) and (iii) is well-known and easily derived; e.g., follow the proof of Theorem 1 above. These equivalences can be generalized by replacing $\{A \rightarrow B\}$ with a totally connected set $\boldsymbol{C}$ of variables covered by common parents $\boldsymbol{D}$. The assumption that $q_{\boldsymbol{C} \mid \boldsymbol{d}}$ has a Dirichlet distribution is equivalent to generalizations of (i) and (iii); see Theorem 3 in Geiger and Heckerman (1997).

# 4 Discussion of Theorems 5, 6, and 7 in Kleiter (1996) 

With BDe constraints, information about all variables is characterized in terms of complete "data" (real and/or fictitious). Kleiter (1996) introduces similar constraints to express this idea for subsets of network variables. Suppose we have a Dirichlet prior and complete data. Let $A$ be a parent of $C$. Write $\mathrm{pa}(C)=A \boldsymbol{B} \boldsymbol{D}$ and $\mathrm{pa}(A)=\boldsymbol{B} \boldsymbol{E}$, where $\boldsymbol{B}, \boldsymbol{D}$, and $\boldsymbol{E}$ are pairwise disjoint and may be empty. Vector $\boldsymbol{B}$ represents parents of both $A$ and $C$. Vector $\boldsymbol{E}$ cannot include $C$. We have $\boldsymbol{\theta}_{C \mid a b d} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{C \mid a b d}\right)$ and $\boldsymbol{\theta}_{A \mid b e} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{A \mid b e}\right)$. The variable $C$ is said to be a natural child of $A$ if

$$
\sum_{c b d} \alpha_{c \mid a b d}=\sum_{b e} \alpha_{a \mid b e} \text { for all } a \in \mathcal{D}_{A}
$$

The network satisfies natural child constraints if (A.5) holds for all pairs $A C$ with $A \in \mathrm{pa}(C)$.

Theorem 2. BDe constraints imply natural child constraints. The converse holds for networks with just two variables.

Proof. Write $\boldsymbol{X}=A \boldsymbol{B} C \boldsymbol{D} \boldsymbol{E} \boldsymbol{Z}$, where $\boldsymbol{Z}$ includes all other variables. Given BDe constraints with weight vector $\left\langle\alpha_{a b c d e x}\right\rangle$, we have $\alpha_{c \mid a b d}=\alpha_{a b c d-}$ and $\alpha_{a \mid b e}=\alpha_{a b-e}$. It follows that both sides of (A.5) equal $\alpha_{a} \ldots$. If $\boldsymbol{X}=A C$, then "natural child" implies BDe with weights $\alpha_{a c}=\alpha_{c \mid a}$.

The converse does not hold in general. E.g., suppose $\boldsymbol{X}=A B C$ and $\mathcal{A}=\{A \rightarrow$ $B \rightarrow C, A \rightarrow C\}$. The natural child constraints are $\sum_{c a} \alpha_{c \mid a b}=\sum_{a} \alpha_{b \mid a}, \sum_{c b} \alpha_{c \mid a b}=$ $\alpha_{a}$, and $\sum_{b} \alpha_{b \mid a}=\alpha_{a}$. Equivalently, setting $\alpha_{a b c}:=\alpha_{c \mid a b}$, we have $\alpha_{a}=\alpha_{a-}, \sum_{b} \alpha_{b \mid a}=$ $\alpha_{a-}$, and $\sum_{a} \alpha_{b \mid a}=\alpha_{. b}$. "Natural child" constrains only the marginal totals of table $\boldsymbol{\alpha}_{B \mid A}$. BDe constrains the entire table. A similar argument shows that the converse fails for larger networks with complete structure (i.e., where every pair of variables is connected by an arc). An application of Theorem 1 shows that, given complete data, Dirichlet prior, BDe constraints, and complete structure, we have $q_{\boldsymbol{X}} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{\boldsymbol{X}}\right)$ and so every query has a beta distribution. This conclusion can fail if BDe is replaced with natural child constraints.

The following example is related to Kleiter's Theorems 5 and 7.
Example 2. Suppose $\boldsymbol{X}=A B$ and $\mathcal{A}=\{A \rightarrow B\}$. Assuming complete data and Dirichlet prior (but not necessarily BDe constraints), we have $\boldsymbol{\theta}_{A} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{A}\right)$, $\boldsymbol{\theta}_{B \mid a} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{B \mid a}\right)$, all CPtable rows are independent, and $q_{a \mid b}=\theta_{a} \theta_{b \mid a} / \sum_{a^{\prime}} \theta_{a^{\prime}} \theta_{b \mid a^{\prime}}$. Applying Lemma 1, we represent $\theta_{a}$ as $\gamma_{a} / \gamma$., where the $\gamma_{a}$ are independent random variables with $\gamma_{a} \sim \operatorname{Gam}\left(\alpha_{a}\right)$. We also assume that $\left\langle\gamma_{a}\right\rangle$ is independent of $\boldsymbol{\theta}_{B \mid A}$. With $b$ fixed, put $\zeta_{a}=\gamma_{a} \theta_{b \mid a}$ so that $q_{a \mid b}=\zeta_{a} / \zeta$. The $\zeta_{a}$ are independent random variables and the conditional distribution of $\zeta_{a}$ given $\theta_{b \mid a}$ is gamma with shape parameter $\alpha_{a}$ and scale parameter $\theta_{b \mid a}$. The unconditional distribution of $\zeta_{a}$ is thus a continuous scale mixture of gamma distributions. Put $\Delta_{a}=\alpha_{a}-\sum_{b} \alpha_{b \mid a}$. If $\Delta_{a}=0$ (i.e., we have BDe constraints, equivalent to "natural child" here), then the second part of Lemma 1 shows that $\zeta_{a} \sim \operatorname{Gam}\left(\alpha_{b \mid a}\right)$ and consequently $q_{a \mid b} \sim \operatorname{Beta}\left(\alpha_{b \mid a}, \alpha_{b \mid}-\alpha_{b \mid a}\right)$. This is a restatement of Kleiter's Theorem 5. Theorem 1 provides an interpretation of this result: $q_{a \mid b}$ has a beta distribution because it is a parameter $\theta_{a \mid b}$ under the equivalent structure $\{A \leftarrow B\}$.

If $\Delta_{a}$ is a positive integer, then the distribution of $\zeta_{a}$ can be expressed as a finite mixture of gamma distributions with fixed scale parameter and varying shape parameter; i.e., $\sum w_{k} \operatorname{Gam}\left(\delta_{k}\right)$ where the mixing weights $w_{k}$ are Polya-Eggenberger (PE) probabilities. The shape parameter $\delta_{k}$ varies by increments of 1 from $\alpha_{b \mid a}$ to $\alpha_{b \mid a}+\Delta_{a}$. A derivation of this result is provided in the Appendix. If $\Delta_{a}$ is a nonnegative integer for each $a \in \mathcal{D}_{A}$, then it follows that the distribution of $q_{a \mid b}$ is a mixture of beta distributions where the mixing weights are products of PE probabilities.

This beta mixture result constitutes part of Kleiter's Theorem 7. His full Theorem 7 makes a more general claim that the distribution of $q_{a \mid b}$ is a finite mixture of beta distributions even if some or all $\Delta_{a}$ are negative integers. For negative $\Delta_{a}$ it is claimed that the shape parameter $\delta_{k}$ varies by increments of 1 from $\max \left\{0, \alpha_{b \mid a}+\Delta_{a}\right\}$ to $\min \left\{\alpha_{b \mid a}, \alpha_{a}\right\}$. No proofs are given in Kleiter (1996) but further details are provided by Kleiter and Kardinal (1995). Their result for $\Delta_{a}<0$ is based on an an additional assumption (an urn model sampling scheme), which is not needed for $\Delta_{a}>0$. They conjecture that the result for $\Delta_{a}<0$ remains valid without this additional assumption.

Theorem 3 below implies that the beta mixture claim for $\Delta_{a}<0$ is in fact not possible given a Dirichlet posterior distribution. This suggests that the urn model sam-

pling scheme may be incompatible with the Dirichlet assumption. Given the connection between Dirichlet and gamma distributions, a finite mixture of beta distributions would imply corresponding finite shape mixtures of gamma distributions, one for each $a \in \mathcal{D}_{A}$, but this is possible only if the $\Delta_{a}$ are nonnegative integers. The proof of Theorem 3 is given in the Appendix.

Theorem 3. Suppose $\theta$ and $\gamma$ are independent random variables with $\theta \sim \operatorname{Beta}\left(\alpha_{1}, \alpha_{2}\right)$ and $\gamma \sim \operatorname{Gam}\left(\alpha_{3}\right)$. Put $\zeta=\gamma \theta$ and $\Delta=\alpha_{3}-\alpha_{1}-\alpha_{2}$. The distribution of $\zeta$ is a finite shape mixture of gamma distributions if and only if $\Delta$ is a nonnegative integer. If $\Delta=0$, then $\zeta \sim \operatorname{Gam}\left(\alpha_{1}\right)$.

Kleiter's Theorem 6 makes the following claim. If $\boldsymbol{B}$ denotes all children of $A$, each child of $A$ is a natural child with respect to all of its parents, and all CPtable rows are independent with Dirichlet distributions, then $q_{a \mid b}$ has a beta distribution. The following example shows that the claim is not valid even with "natural child" replaced by the stronger BDe constraints.

Example 3. Let $\boldsymbol{X}=A B C$ and $\mathcal{A}=\{B \leftarrow A \rightarrow C\}$. Assuming complete data, Dirichlet prior, and BDe constraints with weights $\alpha_{a b c}$, we have independent $\boldsymbol{\theta}_{A} \sim$ $\operatorname{Dir}\left(\boldsymbol{\alpha}_{A \cdots}\right), \boldsymbol{\theta}_{B \mid a} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{a B}\right.$. $)$, and $\boldsymbol{\theta}_{C \mid a} \sim \operatorname{Dir}\left(\boldsymbol{\alpha}_{a \cdot C}\right)$. Fixing $b c \in \mathcal{D}_{B C}$ and following the steps in Example 2, we obtain

$$
q_{a \mid b c}=\theta_{a} \theta_{b \mid a} \theta_{c \mid a} / \sum_{a^{\prime}} \theta_{a^{\prime}} \theta_{b \mid a^{\prime}} \theta_{c \mid a^{\prime}}=\zeta_{a} \theta_{c \mid a} / \sum_{a^{\prime}} \zeta_{a^{\prime}} \theta_{c \mid a^{\prime}}
$$

The $\zeta_{a}$ are independent random variables, $\zeta_{a} \sim \operatorname{Gam}\left(\alpha_{a b}\right.$. $)$, and $\left\langle\zeta_{a}\right\rangle$ is independent of $\left\langle\theta_{c \mid a}\right\rangle$. Put $\Delta_{a}=\alpha_{a b}-\alpha_{a \cdots}$. By Theorem 3, we need $\Delta_{a}=0$ in order for $\zeta_{a} \theta_{c \mid a}$ to have a gamma distribution. Here we have $\Delta_{a}<0$ for all $a \in \mathcal{D}_{A}$, since all $\alpha_{a b c}$ are positive. The distribution of $q_{a \mid b c}$ is neither beta nor a finite mixture of betas. It is possible for $q_{a \mid b c}$ to have a beta distribution given certain non-BDe constraints on the weights; e.g., $\alpha_{a}=\sum_{b} \alpha_{b \mid a}$ and $\alpha_{b \mid a}=\sum_{c} \alpha_{c \mid a}$ for all $a b \in \mathcal{D}_{A B}$. Such constraints are unlikely to occur in posterior distributions.

# 5 Appendix: Proof of Theorem 3 on finite mixtures 

The conditional distribution of $\zeta$ given $\theta$ is gamma with shape parameter $\alpha_{3}$ and scale parameter $\theta$, so the marginal density of $\zeta$ is

$$
f(\zeta)=\int_{0}^{1}\left\{\frac{1}{\Gamma\left(\alpha_{3}\right) \theta^{\alpha_{3}}} \zeta^{\alpha_{3}-1} \exp (-\zeta / \theta)\right\}\left\{\frac{\Gamma\left(\alpha_{1}+\alpha_{2}\right)}{\Gamma\left(\alpha_{1}\right) \Gamma\left(\alpha_{2}\right)} \theta^{\alpha_{1}-1}(1-\theta)^{\alpha_{2}-1}\right\} d \theta
$$

Make the change of variable $\eta=(1-\theta) / \theta$, so $\theta=(\eta+1)^{-1}$ and $d \theta=-(\eta+1)^{-2} d \eta$. Some algebraic manipulation yields $f(\zeta)=g(\zeta) h\left(\zeta, \alpha_{2}, \Delta\right)$, where $\Delta=\alpha_{3}-\alpha_{1}-\alpha_{2}$,

$$
\begin{aligned}
g(\zeta) & =\frac{\Gamma\left(\alpha_{1}+\alpha_{2}\right)}{\Gamma\left(\alpha_{1}\right) \Gamma\left(\alpha_{2}\right) \Gamma\left(\alpha_{3}\right)} \zeta^{\alpha_{3}-1} \exp (-\zeta) \\
h\left(\zeta, \alpha_{2}, \Delta\right) & =\int_{0}^{\infty} \exp (-\zeta \eta) \eta^{\alpha_{2}-1}(\eta+1)^{\Delta} d \eta
\end{aligned}
$$

Now suppose $f$ can be represented as a finite mixture of $\operatorname{Gam}\left(\alpha_{k}^{*}\right)$ densities with mixing weights $w_{k}$. Define moments $M_{n}\left(\alpha_{3}\right)=E\left(\gamma^{n}\right)$. A comparison of $E\left(\zeta^{n}\right)=E\left(\theta^{n}\right) M_{n}\left(\alpha_{3}\right)$ with $w_{k} M_{n}\left(\alpha_{k}^{*}\right)$ as $n \rightarrow \infty$ shows that each $\alpha_{k}^{*}$ must be strictly less than $\alpha_{3}$. It follows that, without loss of generality, we may adopt the following parameterization:

$$
\begin{aligned}
\alpha_{k}^{*} & =\alpha_{1}+\Delta-\beta_{k} \\
w_{k} & =c_{k} \frac{\Gamma\left(\alpha_{1}+\Delta-\beta_{k}\right)}{\Gamma\left(\alpha_{1}\right)} \frac{\Gamma\left(\alpha_{2}+\beta_{k}\right)}{\Gamma\left(\alpha_{2}\right)} \frac{\Gamma\left(\alpha_{1}+\alpha_{2}\right)}{\Gamma\left(\alpha_{1}+\alpha_{2}+\Delta\right)}
\end{aligned}
$$

with $k$ ranging over a finite set $\mathcal{K},-\alpha_{2}<\beta_{k}<\alpha_{1}+\Delta, c_{k}>0$, and $\sum w_{k}=1$. Using this parameterization, the mixture assumption is equivalent to the following representation of $h$ in (A.6):

$$
\int_{0}^{\infty} \exp (-\zeta \eta) \eta^{\alpha_{2}-1}(\eta+1)^{\Delta} d \eta=\sum c_{k} \Gamma\left(\alpha_{2}+\beta_{k}\right) \zeta^{-\left(\alpha_{2}+\beta_{k}\right)}
$$

Now observe that (A.8) is valid if and only if

$$
(\eta+1)^{\Delta}=\sum c_{k} \eta^{\beta_{k}} \quad \text { for all } \eta>0
$$

Integration shows that (A.9) implies (A.8) and the converse follows from uniqueness of the Laplace transform. If $\Delta$ is a nonnegative integer, then (A.9) holds with $\mathcal{K}=$ $\left\{0, \ldots, \Delta\right\}, \beta_{k}=k$, and binomial coefficients $c_{k}=\Delta!/\{k!(\Delta-k)!\}$. The weights (A.7) are then Polya-Eggenberger probabilities (Johnson and Kotz, 1977). Otherwise (A.9) cannot hold (see below) and so $f$ cannot be a finite gamma mixture.

If $\Delta<0$, then (A.9) would imply $c_{k}=0$ for $\beta_{k} \neq 0$. To see this, first note that as $\eta \rightarrow 0$ we have $(\eta+1)^{\Delta} \rightarrow 1, \eta^{\beta} \rightarrow 0$ for $\beta>0$, and $\eta^{\beta} \rightarrow \infty$ at different rates for different $\beta<0$. Thus $c_{k}$ must be zero if $\beta_{k}<0$. Second, as $\eta \rightarrow \infty$ we have $(\eta+1)^{\Delta} \rightarrow 0, \eta^{\beta} \rightarrow 0$ for $\beta<0$, and $\eta^{\beta} \rightarrow \infty$ at different rates for different $\beta>0$. Thus $c_{k}$ must be zero if $\beta_{k}>0$.

Suppose $\Delta$ is positive and not an integer. If $\beta<0$ or if $\beta$ is not an integer then, as $\eta \rightarrow 0, \eta^{\beta}$ or one of its derivatives becomes unbounded (at different rates for different $\beta)$ while the function $(\eta+1)^{\Delta}$ and each of its derivatives remains bounded. Thus (A.9) would require that all $\beta_{k}$ be nonnegative integers. On the other hand, an examination of $(\eta+1)^{\Delta} \eta^{-\beta}$ as $\eta \rightarrow \infty$ shows that the maximum $\beta_{k}$ must equal $\Delta$. This contradiction shows that (A.9) cannot hold.

# Acknowledgments 

The author wishes to thank Russ Greiner, Byron Schmuland, and two referees for helpful comments. This work was partially supported by the Natural Sciences and Engineering Research Council of Canada.