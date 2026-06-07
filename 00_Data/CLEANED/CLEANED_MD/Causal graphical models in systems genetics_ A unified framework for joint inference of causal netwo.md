# CAUSAL GRAPHICAL MODELS IN SYSTEMS GENETICS: A UNIFIED FRAMEWORK FOR JOINT INFERENCE OF CAUSAL NETWORK AND GENETIC ARCHITECTURE FOR CORRELATED PHENOTYPES ${ }^{1}$ 

By Elias Chaibub Neto, Mark P. Keller, Alan D. Attie and Brian S. Yandell<br>University of Wisconsin-Madison

Causal inference approaches in systems genetics exploit quantitative trait loci (QTL) genotypes to infer causal relationships among phenotypes. The genetic architecture of each phenotype may be complex, and poorly estimated genetic architectures may compromise the inference of causal relationships among phenotypes. Existing methods assume QTLs are known or inferred without regard to the phenotype network structure. In this paper we develop a QTL-driven phenotype network method (QTLnet) to jointly infer a causal phenotype network and associated genetic architecture for sets of correlated phenotypes. Randomization of alleles during meiosis and the unidirectional influence of genotype on phenotype allow the inference of QTLs causal to phenotypes. Causal relationships among phenotypes can be inferred using these QTL nodes, enabling us to distinguish among phenotype networks that would otherwise be distribution equivalent. We jointly model phenotypes and QTLs using homogeneous conditional Gaussian regression models, and we derive a graphical criterion for distribution equivalence. We validate the QTLnet approach in a simulation study. Finally, we illustrate with simulated data and a real example how QTLnet can be used to infer both direct and indirect effects of QTLs and phenotypes that co-map to a genomic region.

1. Introduction. In the past few years it has been recognized that genetics can be used to establish causal relationships among phenotypes organized in networks [Schadt et al. (2005), Kulp and Jagalur (2006), Li et al. (2006), Chen, EmmertStreib and Storey (2007), Liu, de la Fuente and Hoeschele (2008), Aten et al. (2008), Chaibub Neto et al. (2008)]. These approaches aim to generate a hypothesis about causal relationships among phenotypes involved in biological pathways underlying complex diseases such as diabetes. A key element in these methods is the identification of quantitative trait loci (QTLs) that are causal for each phenotype. The genetic architecture of each phenotype, which consists of the locations
[^0]
[^0]:    Received December 2008; revised July 2009.
    ${ }^{1}$ Supported by CNPq Brazil (ECN); NIDDK Grants DK66369, DK58037 and DK06639 (ADA, MPK, BSY, ECN); and by NIGMS Grants PA02110 and GM069430-01A2 (BSY).

    Key words and phrases. Causal graphical models, QTL mapping, joint inference of phenotype network and genetic architecture, systems genetics, homogeneous conditional Gaussian regression models, Markov chain Monte Carlo.

and effects of detectable QTLs, may be complex. Poorly estimated genetic architectures may compromise the inference of causal relationships among phenotypes. Existing methods that estimate QTLs from genome scans that ignore causal phenotypes bias the genetic architecture by incorrectly inferring QTLs that have indirect effects.

In this paper we propose a novel framework for the joint inference of phenotype network structure and genetic architecture (QTLnet). We model phenotypes and QTL genotypes jointly using homogeneous conditional Gaussian regression (HCGR) models [Lauritzen (1996)]. The genetic architecture for each phenotype is inferred conditional on the phenotype network. Because the phenotype network structure is itself unknown, the algorithm iterates between updating the network structure and genetic architecture using a Markov chain Monte Carlo (MCMC) approach. The posterior sample of network structures is summarized by Bayesian model averaging. To the best of our knowledge, no other proposed method explicitly uses an inferred network structure among phenotypes when performing QTL mapping. Tailoring QTL mapping to network structure avoids the false detection of QTLs with indirect effects and improves phenotype network structure inference.

We employ a causal inference framework with components of both randomized experiments and conditional probability. Randomization of alleles during meiosis and the unidirectional influence of genotype on phenotype allow the inference of causal QTLs for phenotypes. Causal relationships among phenotypes can be inferred using these QTL nodes, enabling us to distinguish between networks that would otherwise be distribution equivalent.

We are particularly interested in inferring causal networks relating sets of phenotypes mapping to coincident genomic regions. It is widely asserted that alleged "hot spots" may have a "master regulator" and that most co-mapping is due to indirect effects [Breitling et al. (2008)]. That is, such a hot spot QTL could influence a single phenotype that is upstream of many others in a causal network; ignoring the phenotype network would result in a perceived hot spot. One objective of our QTLnet method is to sort out the direct and indirect effects of QTLs and phenotypes in such situations.

In the next sections we develop in detail a framework for the joint inference of causal network and genetic architecture of correlated phenotypes. The core idea is to learn the structure of mixed Bayesian networks composed of phenotypes (continuous variables) and QTLs (discrete variables). We model the conditional distribution of phenotypes given the QTLs with homogeneous conditional Gaussian regression models described in Section 2. This allows us to justify formal inference of causal direction along the Bayesian networks in Section 3. That is, we can reduce the size of equivalence classes of Bayesian networks of phenotypes by using driving QTL. In Section 4 we show how a conditional LOD score can formally measure conditional dependence among phenotypes and QTLs and how QTL mapping can be embedded in a graphical models framework. Section 5 presents the MCMC approach for QTLnet. Simulation studies in Section 6 validate the QTLnet

approach and provide an explanation for some QTL hot spots. Section 7 uses real data to illustrate how QTLnet can be used to infer direct and indirect effects of QTLs and phenotypes that co-map to a genomic region. The Discussion puts this work in the context of open questions. Proofs of formal results are given in the Supplement [Chaibub Neto et al. (2009)].
2. HCGR genetic model. In this section we recast the genetical model for QTL studies as a homogeneous conditional Gaussian regression model that jointly models phenotypes and QTL genotypes. Conditional on the QTL genotypes and covariates, the phenotypes are distributed according to a multivariate normal distribution. The QTLs and covariates enter the HCGR model through the mean in a similar fashion to the seemingly unrelated regression model [Banerjee et al. (2008)]. However, the correlation structure among phenotypes is explicitly modeled according to the directed graph representation of the phenotype network. We derive the genetic model from a system of linear regression equations and show that it corresponds to a homogenous conditional Gaussian regression model.

In QTL studies, the observed data consist of phenotypic trait values, $\mathbf{y}$, and marker genotypes, $\mathbf{m}$, on $n$ individuals derived from an inbred line cross. Following Sen and Churchill (2001), we condition on unobserved QTL genotypes, q, to partition our model into genetic and recombination components, respectively relating phenotypes to QTLs and QTLs to observed markers across the genome,

$$
p(\mathbf{y}, \mathbf{q} \mid \mathbf{m})=p(\mathbf{y} \mid \mathbf{q}, \mathbf{m}) p(\mathbf{q} \mid \mathbf{m})=p(\mathbf{y} \mid \mathbf{q}) p(\mathbf{q} \mid \mathbf{m})
$$

where the second equality follows from conditional independence, $\mathbf{y} \Perp \mathbf{m} \mid \mathbf{q}$. That is, given the QTL genotypes, the marker genotypes provide no additional information about the phenotypes. Estimation of the recombination model, $p(\mathbf{q} \mid \mathbf{m})$, is a well-solved problem [Broman et al. (2003)] and is not addressed in this paper.

Let $i=1, \ldots, n$ and $t=1, \ldots, T$ index individuals and phenotype traits, respectively. Let $\mathbf{y}=\left(\mathbf{y}_{1}, \ldots, \mathbf{y}_{n}\right)^{\prime}$ represent all phenotypic trait values, $\mathbf{y}_{i}=$ $\left(y_{1 i}, \ldots, y_{T i}\right)^{\prime}$ represent the measurements of the $T$ phenotype traits for individual $i$, and let $\boldsymbol{\varepsilon}_{i}=\left(\varepsilon_{1 i}, \ldots, \varepsilon_{T i}\right)^{\prime}$ represent the associated independent normal error terms. We assume that individual $i$ and trait $t$ have the following phenotype model:

$$
y_{t i}=\mu_{t i}^{\star}+\sum_{v \in \operatorname{pa}\left(y_{t}\right)} \beta_{t v} y_{v i}+\varepsilon_{t i}, \quad \varepsilon_{t i} \sim N\left(0, \sigma_{t}^{2}\right)
$$

where $\mu_{t i}^{\star}=\mu_{t}+\mathbf{X}_{t i} \boldsymbol{\theta}_{t}$, where $\mu_{t}$ is the overall mean for trait $t, \boldsymbol{\theta}_{t}$ is a column vector of all genetic effects constituting the genetic architecture of trait $t$ plus any additional additive or interactive covariates, and $\mathbf{X}_{t i}$ represents the row vector of genetic effects predictors derived from the QTL genotypes along with any covariates. The notation $\mathrm{pa}\left(y_{t}\right)$ represents the set of parent phenotype nodes of $y_{t}$, that is, the set of phenotype nodes that directly affect $y_{t}$. Genetic effects may follow Cockerham's genetic model, but need not be restricted to this form [Zeng, Wang and Zou (2005)].

The Jacobian transformation from $\boldsymbol{\varepsilon}_{i} \rightarrow \mathbf{y}_{i}$ allows us to represent the joint density of the phenotype traits conditional on the respective genetic architectures as multivariate normal with the following mean vector and covariance matrix.

Result 1. The conditional joint distribution of the phenotype traits organized according to the set of structural equations defined in (2.1) is $\mathbf{y}_{i} \mid \boldsymbol{\mu}_{i}^{\star}, \boldsymbol{\beta}, \boldsymbol{\sigma}^{2} \sim$ $N_{T}\left(\boldsymbol{\Omega}^{-1} \boldsymbol{\gamma}_{i}, \boldsymbol{\Omega}^{-1}\right)$, where $\boldsymbol{\mu}_{i}^{\star}=\left(\mu_{1 i}^{\star}, \ldots, \mu_{T i}^{\star}\right)^{\prime}, \boldsymbol{\beta}=\left\{\beta_{t v}: v \in \operatorname{pa}\left(y_{t}\right), t=1\right.$, $\ldots, T\}, \boldsymbol{\sigma}^{2}=\left(\sigma_{1}^{2}, \ldots, \sigma_{T}^{2}\right)^{\prime}, \boldsymbol{\Omega}$ is the concentration matrix with entries given by

$$
\omega_{t v}= \begin{cases}\frac{1}{\sigma_{t}^{2}}+\sum_{s} \frac{\beta_{s t}^{2}}{\sigma_{s}^{2}} \mathbb{1}_{\{t \rightarrow s\}}, & \text { for } t=v \\ -\frac{\beta_{v t}}{\sigma_{v}^{2}} \mathbb{1}_{\{t \rightarrow v\}}-\frac{\beta_{t v}}{\sigma_{t}^{2}} \mathbb{1}_{\{v \rightarrow t\}}+\sum_{s} \frac{\beta_{s v} \beta_{s t}}{\sigma_{v}^{2}} \mathbb{1}_{\{v \rightarrow s, t \rightarrow s\}}, & \text { for } t \neq v\end{cases}
$$

$\boldsymbol{\gamma}_{i}$ is a vector with entries $\frac{\mu_{i i}^{\star}}{\sigma_{i}^{2}}-\sum_{s \neq t} \frac{\beta_{s t} \mu_{i t}^{\star}}{\sigma_{s}^{2}} \mathbb{1}_{\{t \rightarrow s\}}$, and $\mathbb{1}_{\{t \rightarrow s\}}$ is the indicator function that trait $t$ affects trait $s$.

REMARKs. (1) The model allows different genetic architectures for each phenotype. (2) The covariance structure depends exclusively in the relationships among phenotypes since $\boldsymbol{\Omega}$ depends only on the partial regression coefficients relating phenotypes ( $\beta$ 's) and variances of error terms ( $\sigma^{2}$ 's), and not on the genetic architectures defined by the $\boldsymbol{\theta}$ 's. (3) When the correlation between two phenotypes arises exclusively because of a pleoitropic QTL, conditioning on the QTL genotypes makes the phenotypes independent; thus, the concentration matrix of the conditional model does not depend on the genetic architecture. (4) This model can represent acyclic and cyclic networks. However, we focus on acyclic networks in this paper.

We now show that our model corresponds to a homogeneous conditional Gaussian regression model. The conditional Gaussian (CG) parametric family models the covariation of discrete and continuous random variables. Continuous random variables conditional on discrete variables are multivariate normal [Lauritzen (1996)]. The joint distribution of the vectors of discrete $\left(\mathbf{q}_{i}\right)$ and continuous $\left(\mathbf{y}_{i}\right)$ variables have a density $f$ such that

$$
\log f\left(\mathbf{q}_{i}, \mathbf{y}_{i}\right)=g\left(\mathbf{q}_{i}\right)+\mathbf{h}^{\prime}\left(\mathbf{q}_{i}\right) \mathbf{y}_{i}-\mathbf{y}_{i}^{\prime} \mathbf{K}\left(\mathbf{q}_{i}\right) \mathbf{y}_{i} / 2
$$

where $g\left(\mathbf{q}_{i}\right)$ is a scalar, $\mathbf{h}\left(\mathbf{q}_{i}\right)$ is a vector and $\mathbf{K}\left(\mathbf{q}_{i}\right)$ is a positive definite matrix. The density $f$ depends on observed markers $\mathbf{m}_{i}$ as

$$
\log f\left(\mathbf{q}_{i}, \mathbf{y}_{i}\right)=\log p\left(\mathbf{y}_{i}, \mathbf{q}_{i} \mid \mathbf{m}_{i}\right)
$$

where $g\left(\mathbf{q}_{i}\right)=\log p\left(\mathbf{q}_{i} \mid \mathbf{m}_{i}\right)-\frac{1}{2}\left(T \log 2 \pi-\log \operatorname{det}(\boldsymbol{\Omega})+\sum_{t=1}^{T} \mu_{i t}^{\star 2} / \sigma_{t}^{2}\right)$. Observe that the linear coefficients $\mathbf{h}\left(\mathbf{q}_{i}\right)=\boldsymbol{\gamma}_{i}$ depend on $\mathbf{q}_{i}$ through $\mathbf{X}_{t i}$, while the concentration matrix $\mathbf{K}\left(\mathbf{q}_{i}\right)=\boldsymbol{\Omega}$ does not. Thus, our model is a homogeneous CG model

[Lauritzen (1996), page 160]. Furthermore, since our genetic model was derived from a set of regression equations with normal errors, our model is in the homogeneous conditional Gaussian regression parametric family.
3. A causal framework for systems genetics. This section formalizes our causal inference framework for systems genetics that combines ideas from randomized experiments with a purely probabilistic approach to causal inference. We argue that while causal claims about the relationship between QTLs and phenotypes are justified by randomization of alleles during meiosis and the unidirectional influence of genotype on phenotype, causal claims about the relationships between phenotypes follow from conditional probability. In a nutshell, by adding QTL nodes to phenotype networks, we can distinguish between phenotype networks that would, otherwise, be distribution equivalent.

In order to formalize our approach, we first show that adding causal QTL nodes can break Markov-equivalence among phenotype networks by creating new conditional independence relationships among nodes. Second, we note that two models in the HCGR parametric family are distribution equivalent if and only if they are Markov equivalent. The last result together with Theorem 1 (see below) provide a simple graphical criterion to determine whether two DAGs belonging to the HCGR parametric family are distribution equivalent.

The analogy between the randomization of alleles during meiosis and a randomized experimental design was first pointed out by Li et al. (2006). Causality can be unambiguously inferred from a randomized experiment for two reasons [Dawid (2007)]: (1) the treatment to an experimental unit (genotype) precedes measured outcomes (phenotypes); and (2) random allocation of treatments to experimental units guarantees that other common causes are averaged out. The central dogma of molecular biology [Crick (1958)] suggests that QTL genotypes generally precede phenotypes. For the types of Eukaryotic data which we analyze (including clinical traits gene expression and metabolites), causality must go from QTL to phenotype. Furthermore, random allocation of QTL genotypes eliminates confounding from other genetic and environmental effects.

Causal relationships among phenotypes require the additional assumption of conditional independence. Suppose a QTL, $Q$, and two phenotypes mapping to $Q$, $Y_{1}$ and $Y_{2}$, have true causal relationship $Q \rightarrow Y_{1} \rightarrow Y_{2}$. That is, $Y_{2}$ is independent of $Q$ given $Y_{1}$. The randomization of genotypes in $Q$ leads to a randomization of $Y_{1}$, thus averaging out confounding affects. However, precedence of the 'randomized' $Y_{1}$ before the 'outcome' $Y_{2}$ cannot in general be determined a priori. Conditional independence is the key to determine causal order among phenotypes [Schadt et al. (2005), Li et al. (2006), Chen, Emmert-Streib and Storey (2007), Liu, de la Fuente and Hoeschele (2008), Chaibub Neto et al. (2008)].

In the remainder of this section we present some graphical model definitions and results needed in the formalization of our causal graphical models framework. A path is any unbroken, nonintersecting sequence of edges in a graph, which may go along or against the direction of the arrows.

Definition 1 (d-separation). A path $p$ is said to be d-separated (or blocked) by a set of nodes $Z$ if and only if

1. $p$ contains a chain $i \rightarrow m \rightarrow j$ or a fork $i \leftarrow m \rightarrow j$ such that the middle node $m$ is in $Z$, or
2. $p$ contains an inverted fork (or collider) $i \rightarrow m \leftarrow j$ such that the middle node $m$ is not in $Z$ and such that no descendant of $m$ is in $Z$.

A set $Z$ is said to d-separate $X$ from $Y$ if and only if $Z$ blocks every path from a node in $X$ to a node in $Y . X$ and $Y$ are d-connected if they are not d-separated [Pearl $(1988,2000)]$.

Two graphs are Markov equivalent (or faithful indistinguishable) if they have the same set of d-separation relations [Spirtes, Glymour and Scheines (2000)]. The skeleton of a causal graph is the undirected graph obtained by replacing its arrows by undirected edges. A v-structure is composed by two converging arrows whose tails are not connected by an arrow.

THEOREM 1 (Detecting Markov equivalence). Two directed acyclic graphs (DAGs) are Markov equivalent if and only if they have the same skeletons and the same set of $v$-structures [Verma and Pearl (1990)].

Two models are likelihood equivalent if $f\left(y \mid M_{1}\right)=f\left(y \mid M_{2}\right)$ for any data set $y$, where $f(y \mid M)$ represent the prior predictive density of the data, $y$, conditional on model $M$ [Heckerman, Geiger and Chickering (1995)]. In this paper we extend the definition of likelihood equivalence to predictive densities obtained by plugging in maximum likelihood estimates in the respective sampling models. A closely related concept, distribution equivalence, states that two models are distribution equivalent if one is a reparametrization of the other. While likelihood equivalence is defined in terms of predictive densities (prior predictive density or sampling model evaluated on the maximum likelihood estimates), distribution equivalence is defined in terms of the sampling model directly. Because of the invariance property of maximum likelihood estimates, distribution and likelihood equivalence are equivalent concepts in the frequentist setting. This is also true in the Bayesian setting with proper priors invariant to model reparameterizations.

Suppose that for each pair of connected phenotypes in a graph there exists at least one QTL affecting one but not the other phenotype. Denote this new graph with QTLs included by the "extended graph." The next result shows that, in this particular situation, we can distinguish between causal models belonging to a Markov equivalent class of phenotype networks.

Result 2. Consider a class of Markov equivalent DAGs $\mathcal{G}$. Let $Y_{1}$ and $Y_{2}$ be any two adjacent nodes in the graphs in $\mathcal{G}$. Assume that for each such pair there exists at least one variable, $Q$, directly affecting $Y_{1}$ but not $Y_{2}$. Let $\mathcal{G}_{E}$ represent the class of extended graphs. Then the graphs in $\mathcal{G}_{E}$ are not Markov equivalent.

As an illustrative example consider the following class of Markov equivalent models: $\mathcal{G}=\left\{Y_{1} \rightarrow Y_{2} \rightarrow Y_{3}, Y_{1} \leftarrow Y_{2} \leftarrow Y_{3}, Y_{1} \leftarrow Y_{2} \rightarrow Y_{3}\right\}$. These causal models are Markov equivalent because they have the same set of conditional independence relations, namely, $Y_{1} \Perp Y_{3} \mid Y_{2}$. In accordance with Theorem 1, the three models have the same skeleton, $Y_{1}-Y_{2}-Y_{3}$, and the same set of v-structures (no v -structures). Now consider one QTL, $Q$, affecting $Y_{2}$ but not $Y_{1}$ and $Y_{3}$. Then $\mathcal{G}_{E}$ is composed by


Observe that these models still have the same skeleton but different sets of v structures: $Y_{1} \rightarrow Y_{2} \leftarrow Q, Q \rightarrow Y_{2} \leftarrow Y_{3}$ and $\varnothing$, respectively. The next result guarantees that for the HCGR parametric family Markov equivalence implies distribution equivalence and vice-versa.

Result 3. For the HCGR parametric family, two DAGs are distribution equivalent if and only if they are Markov equivalent.

It follows from Results 2 and 3 that by extending the phenotype network to include QTLs we are able to reduce the size of and equivalence class of graphs (possibly to a single network). Furthermore, if we consider Theorem 1 and Result 3 together, we have the following:

Result 4. For the HCGR parametric family, two DAGs are distribution equivalent if and only if they have the same skeletons and same sets of v-structures.

Result 4 provides a simple graphical criterion to determine whether two HCGR models are distribution equivalent. This allows us to determine distribution equivalence by inspection of graph structures without the need to go through algebraic manipulations of joint probability distributions as in Chaibub Neto et al. (2008).
4. QTL mapping and phenotype network structure. In this section we show that the conditional LOD score can be used as a formal measure of conditional independence relationships between phenotypes and QTLs. Even though in this paper we restrict our attention to HCGR models, conditional LOD profiling is a general framework for the detection of conditional independencies between continuous and discrete random variables and does not depend on the particular parametric family adopted in the modeling. Contrary to partial correlations, the conditional LOD score does not require the assumption of multinormality of the data in order to formally test for independence [recall that only in the Gaussian

case, a zero (partial) correlation implies statistical (conditional) independence], and it can handle interactive covariates.

The conditional LOD score is defined as

$$
\begin{aligned}
\operatorname{LOD}(y, q \mid x) & =\operatorname{LOD}(y, q, x)-\operatorname{LOD}(y, x) \\
& =\log _{10}\left\{\frac{f(y \mid q, x)}{f(y)}\right\}-\log _{10}\left\{\frac{f(y \mid x)}{f(y)}\right\}
\end{aligned}
$$

where $f(\cdot)$ represents a predictive density (a maximized likelihood or the prior predictive density in a Bayesian setting). It follows directly from this definition that

$$
\operatorname{LOD}(y, q \mid x)=0 \quad \Leftrightarrow \quad f(y \mid q, x)=f(y \mid x) \quad \Leftrightarrow \quad Y \Perp Q \mid X
$$

Therefore, we can use conditional LOD scores as a formal measure of independence between continuous $(Y)$ and discrete $(Q)$ random variables, conditional on any set of variables $X$, that could be either continuous, discrete or both.

Furthermore, the conditional LOD score can be used to formally test for conditional independence in the presence of interacting covariates (denoted by $X \cdot Q$ ) since

$$
\operatorname{LOD}(y, q \mid x, x \cdot q)=\log _{10}\left\{\frac{f(y \mid q, x, x \cdot q)}{f(y)}\right\}-\log _{10}\left\{\frac{f(y \mid x)}{f(y)}\right\}=0
$$

if and only if $Y \Perp\{Q, X \cdot Q\} \mid X$. This is a very desirable property since, in general, testing for conditional independence in the presence of interactions is not straightforward. For example, Andrei and Kendziorski (2009) point that in the presence of interactions, there is no one-to-one correspondence between zero partial correlations and conditional independencies, even when we assume normality of the full conditional distributions.

Traditional QTL mapping focuses on single trait analysis, where the network structure among the phenotypes is not taken into consideration in the analysis. Thus, single-trait analysis may detect QTLs that directly affect the phenotype under investigation, as well as QTLs with indirect effects, affecting phenotypes upstream to the phenotype under study. Consider, for example, the causal graph in Figure 1. The outputs of single trait analysis when Figure 1 represents the true network are given in Figure 2.
![img-0.jpeg](img-0.jpeg)

FIG. 1. Example network with five phenotypes and four QTLs.

![img-1.jpeg](img-1.jpeg)

FIG. 2. Output of a single trait QTL mapping analysis for the phenotypes in Figure 1. Dashed and pointed arrows represent direct and indirect QTL/phenotype causal relationships, respectively.

Now let's consider QTL mapping according to the phenotype network structure. When the phenotype structure corresponds to the true causal model, we avoid detecting indirect QTLs by simply performing mapping analysis of the phenotypes conditional on their parents. For example, in Figure 1, if we perform a mapping analysis of $Y_{5}$ conditional on $Y_{2}, Y_{3}$ and $Y_{4}$, we do not detect $Q_{1}, Q_{2}$ and $Q_{4}$ because $Y_{5} \Perp Q_{1} \mid Y_{2}, Y_{3}, Y_{4}, Y_{5} \Perp Q_{2} \mid Y_{2}, Y_{3}, Y_{4}$ and $Y_{5} \Perp Q_{4} \mid Y_{2}, Y_{3}, Y_{4}$. We only detect $Q_{5}$ since $Y_{5} \Perp Q_{5} \mid Y_{2}, Y_{3}, Y_{4}$.

Now consider Figure 3(a). If we perform a mapping analysis of $Y_{5}$ conditional on $Y_{3}$ and $Y_{4}$, we still detect $Q_{1}$ and $Q_{2}$ as QTLs for $Y_{5}$, since failing to condition on $Y_{2}$ leaves the paths $Q_{1} \rightarrow Y_{1} \rightarrow Y_{2} \rightarrow Y_{5}$ and $Q_{2} \rightarrow Y_{2} \rightarrow Y_{5}$ in Figure 1 open. In other words, $Q_{1}$ and $Q_{2}$ are d-connected to $Y_{5}$ conditional on $\left(Y_{3}, Y_{4}\right)$ in the true causal graph. Mistakenly inferring that a QTL has a direct effect when in reality it indirectly affects the phenotype is problematic, but not a serious concern.

On the other hand, if we map an upstream phenotype conditional on downstream phenotypes, we could infer that downstream QTLs are causal. This would be a serious problem, as it would dramatically reverse the causal flow. Consider, for example, Figure 3(b). If we perform a mapping analysis of $Y_{4}$ conditional on $Y_{1}, Y_{3}$ and $Y_{5}$, we incorrectly detect $Q_{5}$ as a QTL for $Y_{4}$ because in the true network the paths $Y_{4} \rightarrow Y_{5} \leftarrow Q_{5}$ and $Y_{4} \leftarrow Y_{3} \rightarrow Y_{5} \leftarrow Q_{5}$ in Figure 1 are open when we condition on $Y_{5}$. That is, if we perform mapping analysis of a phenotype conditional on phenotypes located downstream in the true network, we induce dependencies between the upstream phenotype and QTLs affecting downstream phenotypes, and we erroneously conclude that a downstream QTL affects an upstream phenotype. However, a model with reversed causal relationships among phenotypes and incorrectly having downstream QTLs detected as direct QTLs for the upstream node will generally have a lower marginal likelihood score than the
![img-2.jpeg](img-2.jpeg)

FIG. 3. QTL mapping tailored to the network structure. (a) and (b) display the results of QTL mapping according to slightly altered network structures from Figure 1. Dashed, pointed and wiggled arrows represent, respectively, direct, indirect and incorrect QTL/phenotype causal relationships.

model with the correct causal order for the phenotypes and correct genetic architecture. Therefore, in practice, our model selection procedure protects against this type of mistake.
5. QTLnet algorithm. In this section we propose a statistical framework (QTLnet) for the joint inference of phenotype network structure and genetic architecture in systems genetics studies. Work to date in genetical network reconstruction has treated the problems of QTL inference and phenotype network reconstruction separately, generally performing genetic architecture inference first, and then using QTLs to help in the determination of the phenotype network structure [Chaibub Neto et al. (2008), Zhu et al. (2008)]. As indicated in the previous section, such strategy can incorporate QTLs with indirect effects into the genetic architecture of phenotypes.

The great challenge in the reconstruction of networks is that the graph space grows super-exponentially with the number of nodes, so that exhaustive searches are impractical even for small networks, and heuristic approaches are needed to efficiently traverse the graph space. The Metropolis-Hastings algorithm below integrates the sampling of network structures [Madigan and York (1995), Husmeier (2003)] and QTL mapping.

Let $\mathcal{M}$ represent the structure of a phenotype network composed of $T$ nodes. The posterior probability of a specified structure is given by

$$
p(\mathcal{M} \mid \mathbf{y}, \mathbf{q})=\frac{p(\mathbf{y} \mid \mathbf{q}, \mathcal{M}) p(\mathcal{M})}{\sum_{\mathcal{M}} p(\mathbf{y} \mid \mathbf{q}, \mathcal{M}) p(\mathcal{M})}
$$

where the marginal likelihood

$$
p(\mathbf{y} \mid \mathbf{q}, \mathcal{M})=\int_{\Gamma} p(\mathbf{y} \mid \mathbf{q}, \boldsymbol{\Gamma}, \mathcal{M}) p(\boldsymbol{\Gamma} \mid \mathcal{M}) d \boldsymbol{\Gamma}
$$

is obtained by integrating the product of the prior and likelihood of the HCGR model with respect to all parameters $\boldsymbol{\Gamma}$ in the model. Assuming that the phenotype network is a DAG, the likelihood function factors according to $\mathcal{M}$ as

$$
p\left(\mathbf{y}_{i} \mid \mathbf{q}_{i}, \boldsymbol{\Gamma}, \mathcal{M}\right)=\prod_{t} p\left(y_{t i} \mid \mathbf{q}_{t i}, \mathrm{pa}\left(y_{t}\right)\right)
$$

where

$$
p\left(y_{t i} \mid \mathbf{q}_{t i}, \mathrm{pa}\left(y_{t}\right)\right)=N\left(\mu_{t i}^{\star}+\sum_{y_{k} \in \mathrm{pa}\left(y_{t}\right)} \beta_{t k} y_{k i}, \sigma_{t}^{2}\right)
$$

and the problem factors out as a series of linear regression models. (Note that QTL genotypes $\mathbf{q}_{t i}$ enter the model through $\mu_{t i}^{\star}$.)

We estimate the posterior probability in (5.1) using a Metropolis-Hastings algorithm detailed in Section 1 of the Supplement. The M-H proposals, which make

single changes (add or drop an edge, or change causal direction), require remapping of any phenotypes that have altered sets of parent nodes. The accept/reject calculation involves estimation of the marginal likelihood conditional on the parent nodes and newly mapped QTL(s).

Because the graph space grows rapidly with the number of phenotype nodes, the network structure with the highest posterior probability may still have a very low probability. Therefore, instead of selecting the network structure with the highest posterior probability, we perform Bayesian model averaging [Hoeting et al. (1999)] for the causal relationships between phenotypes and infer an averaged network. Explicitly, let $\Delta_{u v}$ represent a causal relationship between phenotypes $u$ and $v$, that is, $\Delta_{u v}=\left\{Y_{u} \rightarrow Y_{v}, Y_{u} \leftarrow Y_{v}, Y_{u} \nrightarrow Y_{v}\right.$ and $\left.Y_{u} \nleftarrow Y_{v}\right\}$. Then

$$
\begin{aligned}
p\left(\Delta_{u v} \mid \mathbf{y}\right) & =\sum_{k} p\left(\Delta_{u v} \mid \mathcal{M}_{k}, \mathbf{y}, \mathbf{q}\right) p\left(\mathcal{M}_{k} \mid \mathbf{y}, \mathbf{q}\right) \\
& =\sum_{k} \mathbb{1}\left\{\Delta_{u v} \in \mathcal{M}_{k}\right\} p\left(\mathcal{M}_{k} \mid \mathbf{y}, \mathbf{q}\right)
\end{aligned}
$$

The averaged network is constructed by putting together all causal relationships with maximum posterior probability or with posterior probability above a predetermined threshold.
6. Simulations. In this section we evaluate the performance of the QTLnet approach in simulation studies of a causal network with five phenotypes and four causal QTLs. We consider situations with strong or weak causal signals, leading respectively to high or low phenotype correlations. We show that important features of the causal network can be recovered. Further, this simulation illustrates how an alleged hot spot could be explained by sorting out direct and indirect effects of the QTLs.

We generated 1000 data sets according to Figure 1. Each simulated cross object [Broman et al. (2003)] had 5 phenotypes simulated for an F2 population with 500 individuals. The genome had 5 chromosomes of length 100 cM with 10 equally spaced markers per chromosome. We simulated one QTL per phenotype, except for phenotype $Y_{3}$ with no QTLs. The QTLs $Q_{t}, t=1,2,4,5$, were unlinked and placed at the middle marker on chromosome $t$.

Each simulated cross object had different sampled parameter value combinations for each realization. In the strong signal simulation, we sampled the additive and dominance effects according to $U[0.5,1]$ and $U[0,0.5]$, respectively. The partial regression coefficients for the phenotypes were sampled according to $\beta_{u v} \sim$ $0.5 U[-1.5,-0.5]+0.5 U[0.5,1.5]$. In the weak signal simulation, we generated data sets with additive and dominance effects from $U[0,0.5]$ and $U[0,0.25]$, respectively, and partial regression coefficients sampled with $\beta_{u v} \sim U[-0.5,0.5]$. The residual phenotypic variance was fixed at 1 in both settings.

TABLE 1
Frequencies of QTL detection for both unconditional (top half) and conditional (bottom half) QTL mapping according with the true phenotype network structure in Figure 1. Results, for each simulation, based on 1000 simulated data sets described in the text. The expected architecture is the set of d-connected QTLs for the phenotype conditioning with respect to the network in Figure 1


We first show the accuracy of the mapping analysis in our simulated data sets. We used interval mapping with a LOD score threshold of 5 to detect significant QTLs. Table 1 shows the results of both unconditional and QTL mapping according to the phenotype network in Figure 1. In the strong signal setting, the unconditional mapping often detected indirect QTLs, but the mapping of phenotypes conditional on their parent nodes increased detection of the true genetic architectures. In the weak signal simulation, the unconditional mapping did not detect indirect QTLs in most cases, but we still observe improvement in detection of the correct genetic architecture when we condition on the parents.

The expected architecture contains the d-connected QTLs when conditioning (or not) on other phenotypes as indicated in the first column of Table 1. For instance, $Q_{1}$ and $Q_{2}$ are d-connected to $Y_{2}$, but only $Q_{2}$ is d-connected to $Y_{2}$ when properly conditioning on $Y_{1}$. Supplementary Tables S1, S2, S3, S4 and S5 show the simulation results for all possible conditional mapping combinations.

For each simulated data set we applied the QTLnet algorithm using simple interval mapping for QTL detection. The ratio of marginal likelihoods in the Metropolis-Hastings algorithm was computed using the BIC asymptotic approximation to the Bayes factor (equation 1.1 on the Supplement). We adopted uniform priors over network structures. We ran each Markov chain for 30,000 iterations, sampled a structure every 10 iterations, and discarded the first 300 (burnin) network structures producing posterior samples of size 2700. Posterior probabilities for each causal relationship were computed via Bayesian model averaging.

Table 2 shows the frequency, out of the 1000 simulations, the true model was the most probable, second most probable, etc. The results show that in the strong

TABLE 2
Frequencies that the posterior probability of the true model was the highest, second highest, etc. Results based on 1000 simulated data sets described in the text


signal setting the true model got the highest posterior probability in most of the simulations. In the weak signal setting the range of rankings was very widespread.

Table 3 shows the proportion of times that each possible causal direction $\left(Y_{u} \rightarrow Y_{v}, Y_{u} \leftarrow Y_{v}\right)$ or no causal relation $\left(\left\{Y_{u} \nrightarrow Y_{v}, Y_{u} \nleftarrow Y_{v}\right\}\right)$ had the highest posterior probability for all pairs of phenotypes. The results show that in the strong signal simulations, the correct causal relationships were recovered with high probability. The results are weaker but in the correct direction in the weak signal setting.

Interestingly, single trait analysis with strong signal showed that $Y_{5}$ mapped to $Q_{1}$ more frequently than to $Q_{5}$ (Table 1). This result can be understood using a path analysis [Wright (1934)] argument. In path analysis, we decompose the correlation between two variables among all paths connecting the two variables in a graph. Let $\mathcal{D}_{u v}$ represent the set of all direct and indirect directed paths connecting $u$ and $v$ (a directed path is a path with all arrows pointing in the same direction).

TABLE 3
Frequencies that each possible causal relationship had the highest posterior probability (computed via Bayesian model averaging). Results based on 1000 simulated data sets described in the text


Then the correlation between these nodes can be decomposed as

$$
\begin{aligned}
\operatorname{cor}\left(y_{u}, y_{v}\right) & =\sum_{P \in \mathcal{D}_{u v}} \phi_{p_{2} u} \phi_{p_{3} p_{2}} \cdots \phi_{v p_{m-1}} \\
& =\left\{\frac{\operatorname{var}\left(y_{u}\right)}{\operatorname{var}\left(y_{v}\right)}\right\}^{1 / 2} \sum_{P \in \mathcal{D}_{u v}} \beta_{p_{2} u} \beta_{p_{3} p_{2}} \cdots \beta_{v p_{m-1}}
\end{aligned}
$$

where $\phi_{i j}=\beta_{i j}\left\{\operatorname{var}\left(y_{j}\right) / \operatorname{var}\left(y_{i}\right)\right\}^{1 / 2}$ is a standardized path coefficient. Assuming intra-locus additivity and encoding the genotypes as 0,1 and 2 (for the sake of easy computation), we have from equation (6.1) that

$$
\begin{aligned}
& \operatorname{cor}\left(y_{5}, q_{1}\right)=\beta_{1, q_{1}}\left(\beta_{52} \beta_{21}+\beta_{53} \beta_{31}+\beta_{54} \beta_{41}+\beta_{54} \beta_{43} \beta_{31}\right)\left\{\frac{\operatorname{var}\left(q_{1}\right)}{\operatorname{var}\left(y_{5}\right)}\right\}^{1 / 2} \\
& \operatorname{cor}\left(y_{5}, q_{5}\right)=\beta_{1, q_{5}}\left\{\frac{\operatorname{var}\left(q_{5}\right)}{\operatorname{var}\left(y_{5}\right)}\right\}^{1 / 2}
\end{aligned}
$$

We therefore see that if the partial regression coefficients between phenotypes are high, and the QTL effects $\beta_{1, q_{1}}$ and $\beta_{5, q_{5}}$ and QTL variances are close (as in the strong signal simulation), then $\operatorname{cor}\left(y_{5}, q_{1}\right)$ will be higher than $\operatorname{cor}\left(y_{5}, q_{5}\right)$ and $Y_{5}$ will map to $Q_{1}$ with stronger signal than to $Q_{5}$.

This result suggests a possible scenario for the appearance of eQTL hot spots when phenotypes are highly correlated. A set of correlated phenotypes may be better modeled in a causal network with one upstream phenotype that in turn has a causal QTL. Ignoring the phenotype network can result in an apparent hot spot for the correlated phenotypes. Here, all phenotypes detect $\mathrm{QTL} Q_{1}$ with high probability when mapped unconditionally (Table 1). In the weak signal setting, the phenotypes map mostly to their respective QTLs and do not show evidence for a hot spot. No hot spot was found in additional simulations having strong QTL/phenotype relationships and weak phenotype/phenotype relations (results not shown). Thus, our QTLnet approach can effectively explain a hot spot found with unconditional mapping when phenotypes show strong causal structure.
7. Network inference for a liver hot spot. In this section we illustrate the application of QTLnet to a subset of gene expression data derived from a F2 intercross between inbred lines $C 3 H / H e J$ and $C 57 B L / 6 J$ [Ghazalpour et al. (2006), Wang et al. (2006)]. The data set is composed of genotype data on 1,065 markers and liver expression data on the 3421 available transcripts from 135 female mice. Interval mapping indicates that 14 transcripts map to the same region on chromosome 2 with a LOD score higher than 5.3 (permutation $p$-value $<0.001$ ). Only one transcript, $P s c d b p$, is located on chromosome 2 near the hot spot locus. The 14 transcripts show a strong correlation structure, and the correlation structure adjusting for the peak marker on chromosome 2, $r s 3707138$, is still strong (see Supplementary Table S6). This co-mapping suggest all transcripts are under

the regulation of a common factor. Causal relationships among phenotypes could explain the strong correlation structure that we observe, although other possibilities are environmental factors or a latent factor that is not included.

We applied the QTLnet algorithm on the 129 mice that had no missing transcript data using Haley-Knott (1992) regression (and assuming genotyping error rate of 0.01 ) for the detection of QTLs conditional on the network structure, and we used the BIC approximation to estimate the marginal likelihood ratio in the Metropolis-Hastings algorithm (equation 1.1 on the Supplement). We adopted uniform priors over network structures. We ran a Markov chain for 1,000,000 iterations and sampled a network structure every 100 iterations, discarding the first 1000 and basing inference on a posterior sample with 9000 network structures. Diagnostic plots and measures (see Section 3 on the Supplement) support the convergence of the Markov chain.

We performed Bayesian model averaging and, for each of 91 possible pairs $\left(Y_{u}, Y_{v}\right)$, we obtained the posterior probabilities of $Y_{u} \rightarrow Y_{v}, Y_{u} \leftarrow Y_{v}$ and of no direct causal connection. The results are shown in Supplementary Table S7. Figure 4 shows a model-averaged network.

This network suggests a key role of $I l 16$ in the regulation of the other transcripts in the network. $I l 16$ is upstream to all other transcripts, and is the only one directly
![img-3.jpeg](img-3.jpeg)

FIG. 4. Model-averaged posterior network. Arrow darkness is proportional to the posterior probability of the causal relation computed via Bayesian model averaging. For each pair of phenotypes, the figure displays the causal relationship (presence or absence of an arrow) with highest posterior probability. Light grey nodes represent QTLs and show their chromosome number and position in centimorgans. Riken represents the riken gene 6530401C20Rik.

mapping to the locus of chromosome 2. We would have expected the cis transcript, Pscdbp, to be the upstream phenotype in this network. However, the data suggests Pscdbp is causal to only two other transcripts and that some other genetic factor on chromosome 2 may be driving this pathway. This estimated QTLnet causal network provides new hypotheses that could be tested in future mouse experiments.
8. Discussion. We have developed a statistical framework for causal inference in systems genetics. Causal relationships between QTLs and phenotypes are justified by the randomization of alleles during meiosis together with the unidirectional influence of genotypes on phenotypes. Causal relationships between phenotypes follows from breakage of distribution equivalence due to QTL nodes augmenting the phenotype network. We have proposed a novel approach to jointly infer genetic architecture and causal phenotype network structure using HCGR models. We argue in this paper that failing to properly account for phenotype network structure for mapping analysis can yield QTLs with indirect effects in the genetic architecture, which can decrease the power to detect the correct causal relationships between phenotypes.

Current literature in systems genetics [Chaibub Neto et al. (2008), Zhu et al. (2008)] has considered the problems of genetic architecture and phenotype network structure inference separately. Chaibub Neto et al. (2008) used the PC-algorithm [Spirtes, Glymour and Scheines (2000)] to first infer the skeleton of the phenotype network and then use QTLs to determine the directions of the edges in the phenotype network. Zhu et al. (2008) reconstructed networks from a consensus of Bayesian phenotype networks with a prior distribution based on causal tests of Schadt et al. (2005). Their prior was computed with QTLs determined by single trait analysis.

Liu, de la Fuente and Hoeschele (2008) presented an approach based in structural equation models (and applicable to species where sequence information is available) that partially accounts for the phenotype network structure when selecting the QTLs to be incorporated in the network. They perform eQTL mapping using cis, cis-trans and trans-regulation [Doss et al. (2005), Kulp and Jagalur (2006)] and then use local structural models to identify regulator-target pairs for each eQTL. The identified relationships are then used to construct an encompassing directed network (EDN) with nodes composed by transcripts and eQTLs and arrows from (1) eQTls to cis-regulated target transcripts; (2) cis-regulated transcripts to cis-trans-regulated target transcripts; and (3) trans-regulator transcripts to target transcripts, and from trans-eQTL to target transcripts. The EDN defines a network search space for network inference with model selection based on penalized likelihood scores and an adaptation of Occam's window [Madigan and Raftery (1994)]. Their local structural models, which fit at most two candidate regulators per target transcript, can include indirect eQTLs in the genetic architecture of target transcripts when there are multiple paths connecting a cis-regulator to a cis-transtarget transcript. In other words, some transcripts identified as cis-regulated targets may actually be cis-trans.

Winrow et al. (2009) rely on a (nonhomogeneous) conditional Gaussian model and employ the standard Metropolis-Hastings ( $\mathrm{M}-\mathrm{H}$ ) algorithm (add, remove or delete edges) to search over the space of DAG structures. It differs from our approach in how QTL detection is coupled with the M-H proposal. QTLnet constructs M-H proposals for edges connecting phenotypes and detects QTLs conditional on the network structure. On the other hand, Winrow et al. first detect QTLs and then construct M-H proposals for both phenotypes and QTL nodes. In Section 4 of the Supplement we present a simulation study comparing our approach to Winrow's strategy. QTLnet inferred the proper genetic architecture and phenotype network structure at a higher rate than Winrow's approach with high signal-tonoise ratio. In the weak signal setting, QTLnet picks up direct causal relationship at a higher rate, but Winrow's is better when there is no direct causal link; on average, they were comparable. Although Winrow's strategy also avoids the detection of indirect QTLs, it is prone to miss direct QTLs when the causal effects among phenotypes are strong, and can perform poorly depending on the structure of the phenotype network (see Supplement for details).

Current interest in the eQTL literature centers on understanding the relationships among expression traits that co-map to a genomic region. It is often suggested that these eQTL "hot spots" result from a master regulator affecting the expression levels of many other genes [see Breitling et al. (2008)]. A path analysis argument suggests that if the correlation structure between the phenotypes is strong because of a strong causal signal, a well-defined hot spot pattern will likely appear when we perform single trait analysis. Our simulations and real data example suggest that this is the situation where the QTLnet algorithm is expected to be most fruitful.

The QTLnet approach is based on a Metropolis-Hastings algorithm that at each step proposes a slightly modified phenotype network and fits the genetic architecture conditional on this proposed network. Conditioning on the phenotype network structure should generally lead to a better inferred genetic architecture. Likewise, a better inferred genetic architecture should lead to a better inferred phenotype structure (models with better inferred genetic architectures should have higher marginal likelihood scores. A poorly inferred genetic architecture may compromise the marginal likelihood of a network with phenotype structure close to the true network).

Because the proposal mechanism of the Metropolis-Hastings algorithm is based in small modification of the last accepted network (addition, deletion or reversion of a single edge), the mixing of the Markov chain is generally slow and it is necessary to run long chains and use big thinning windows in order to achieve good mixing. This is a bottleneck to the scalability of this approach. We therefore plan to investigate more efficient versions of the Metropolis-Hastings algorithm for network structure inference. In particular, a new and more extensive edge reversal move proposed by Grzegorczyk and Husmeier (2008) and an approach based in a Markov blanket decomposition of the network [Riggelsen (2005)].

Our method is currently implemented with R code. The analysis of the real data example took over 20 hours in a 64 bit Intel(R) Core(TM) 2 Quad 2.66 GHz machine. We can handle up to 20 phenotype nodes, at this point. The run time for the code, written in R, should be substantially improved as we optimize code, converting key functions to C (under development). Nonetheless, because the number of DAGs increases super-exponentially with the number of phenotype nodes, scaling up the proposed approach to large networks will likely be a very challenging task. Current R code is available from the authors upon request.

One of the most attractive features of a Bayesian framework is its ability to formally incorporate prior information in the analysis. Given the complexity of biological processes and the many limitations associated with the partial pictures provided by any of the "omic" data sets now available, incorporation of external information is highly desirable. We are currently working in the development of priors for network structures.

The QTLnet approach can be seen as a method to infer causal Bayesian networks composed of phenotype and QTL nodes. Standard Bayesian networks provide a compact representation of the conditional dependency and independencies associated with a joint probability distribution. The main criticism of a causal interpretation of such networks is that different structures may be likelihood equivalent while representing totally different causal process. In other words, we can only infer a class of likelihood equivalent networks. We have formally shown how to break likelihood equivalence by incorporating causal QTLs.

We have focussed on experimental crosses with inbred founders, as the recombination model and genetic architecture are relatively straightforward. However, this approach might be extended to outbred populations with some additional work. The genotypic effects are random, and the problem needs to be recast in terms of variance components.

In this paper we only consider directed acyclic graphs. We point out, however, that the HCGR parametric family accommodates cyclic networks. The QTLnet approach can only infer causality among phenotypes that are consistent with the assumption of no latent variables and no measurement error. However, these complications can impact network reconstruction. We are currently investigating extensions of the proposed framework along these lines.

Acknowledgments. We would like to thank Alina Andrei, the associate editor and two anonymous referees for their helpful comments and suggestions.

# SUPPLEMENTARY MATERIAL 

Supplement to "Causal graphical models in systems genetics: A unified framework for joint inference of causal network and genetic architecture for correlated phenotypes" (DOI: 10.1214/09-AOAS288SUPP; .pdf). The Supplement article presents: (1) the Metropolis-Hastings algorithm for QTLnet; (2) sup-

plementary tables for the simulations and real data example; (3) convergence diagnostics for the real data example; (4) comparison with Winrow et al. (2009); and (5) the proofs of Results 1, 2, 3 and 4.
