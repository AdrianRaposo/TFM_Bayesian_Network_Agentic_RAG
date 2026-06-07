# Article 

## Causal Algebras on Chain Event Graphs with Informed Missingness for System Failure

Xuewen Yu ${ }^{1, *}$ (D) and Jim Q. Smith ${ }^{1,2}$

## check for updates

Citation: Yu, X.; Smith, J.Q. Causal Algebras on Chain Event Graphs with Informed Missingness for System Failure. Entropy 2021, 23, 1308. https://doi.org/10.3390/e23101308

Academic Editor: Kateřina
Hlaváčková-Schindler

Received: 10 September 2021
Accepted: 2 October 2021
Published: 6 October 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Statistics Department, University of Warwick, Coventry CV4 7AL, UK; j.q.smith@warwick.ac.uk
2 The Alan Turing Institute, London NW1 2DB, UK

* Correspondence: xuewen.yu@warwick.ac.uk

Abstract: Graph-based causal inference has recently been successfully applied to explore system reliability and to predict failures in order to improve systems. One popular causal analysis following Pearl and Spirtes et al. to study causal relationships embedded in a system is to use a Bayesian network (BN). However, certain causal constructions that are particularly pertinent to the study of reliability are difficult to express fully through a BN. Our recent work demonstrated the flexibility of using a Chain Event Graph (CEG) instead to capture causal reasoning embedded within engineers' reports. We demonstrated that an event tree rather than a BN could provide an alternative framework that could capture most of the causal concepts needed within this domain. In particular, a causal calculus for a specific type of intervention, called a remedial intervention, was devised on this tree-like graph. In this paper, we extend the use of this framework to show that not only remedial maintenance interventions but also interventions associated with routine maintenance can be well-defined using this alternative class of graphical model. We also show that the complexity in making inference about the potential relationships between causes and failures in a missing data situation in the domain of system reliability can be elegantly addressed using this new methodology. Causal modelling using a CEG is illustrated through examples drawn from the study of reliability of an energy distribution network.

Keywords: Chain Event Graphs; interventions; causal calculus

## 1. Introduction

The use of Bayesian Networks (BN) for the study of reliability has been widely advocated in the literature [1]. However, the asymmetric processes that are common in system reliability can hardly be fully captured by the framework of a BN.

Fortunately, it has been shown that any discrete BN can be embellished into a treebased graph called a Chain Event Graph (CEG) [2,3]. The CEG is a graphical model that is a function of an underlying event tree and certain context specific conditional independence statements. In particular, the CEG can model and depict the types of structural asymmetries that the BN framework struggles to embody [4]. This can then provide a framework for studying the causal mechanisms behind the failures of a given system. For example, Cowell and Smith [2] developed a dynamic programming algorithm for maximum a posterior (MAP) structural learning for causal discovery within a restricted class of CEGs called stratified CEGs.

Conventional causal algebras have been adapted from Pearl's do-calculus for BNs [5] to the singular manipulation on a CEG, and the back-door theorem has been generalised to estimate the effect of this manipulation by previous research [6,7]. In a different strand of research, Barclay, Hutton, and Smith [8] developed a class of CEGs suited for incorporating various missing data structures directly through its topology. Unlike BNs, conjugate inference is still well supported by the structure of CEGs even in the presence of missingness [2].

In Section 2, we adapt the MAP structural learning algorithm [2] to search for the best scoring structure of a CEG when some data is informedly missing. The selected model

provides the best explanation of the observed data that has been informedly censored. By assuming that each candidate CEG is causal in the sense formally defined in [6,7], the best scoring CEG is of a CEG in idle mode, and then causal deductions can be made from it.

In our recent work [9], we demonstrated how to embed the causal reasoning underlying engineering reports for CEGs designed specifically for applications in system reliability. The causal calculus we developed there only provided a framework to study and analyse the impact of remedial interventions, i.e., interventions designed to rectify the root cause after a failure had been observed.

In Section 3, we extend the use of the CEG causal framework with missingness to express and analyse a different kind of intervention called a routine intervention. This new class of intervention is necessary when we are evaluating the impact of interventions within scheduled maintenance regimes. These regimes are prepared in advance and are used to inspect machines with the objective of preventing future failures that might be about to happen. In this context, although the data may be informedly missing, we can still develop algorithms that, under certain stated hypotheses, produce formulae to give quantitative estimates of the impacts of various candidate routine interventions of this type.

In this paper, we can, therefore, show how we can use the underlying CEG model to predict the effect of various types of such interventions. In particular we report a new backdoor criterion-an analogue of Pearl's back-door criterion for BNs [5]. This gives a quick sufficient condition as to whether the effect of such an intervention is identifiable when data is censored in a way that induces informed missingness. This criterion significantly increases the scope of the original causal calculus using CEGs designed for the singular manipulation [6] and the stochastic manipulation established for BNs [5]. It, thus, enables us to transfer causal technologies so that they apply to this graphical family.

In Section 4, we demonstrate how to interpret the causal structures of a best scoring CEG by a simple example of a conservator system. Furthermore, comparative experiments are designed to show that the proposed new causal algebras can embellish the current structural learning algorithm to capture the causal effects of a routine intervention.

The contributions of this paper are threefold. First, we formally derive a method for selecting a CEG providing the framework of a probability model of maintenance regimes, which acknowledges the presence of informed missingness within the fitted data endemic in these applications. Second, we devise new causal algebras for the routine intervention and prove the identifiability of its causal effects in presence of the types of missing data that we might expect from this application. Third, we demonstrate how important this new intervention calculus can be in making valid inferences and how naive inferences that treat the system as uncontrolled and ignore the underlying causal structure within this application can severely mislead the analyst.

# 2. Causal Identifiability on Chain Event Graphs with Informed Missingness 

We begin this section by briefly reviewing and then extending the definition of a CEG [2,3,6,7,8] before providing a systematic approach to embedding information about the context-specific missingness into a CEG customised for the domain of reliability [9,10].

Suppose we have a vector of variables $\boldsymbol{X}=\left(X_{1}, X_{2} \ldots, X_{n}\right)$ taking values in a state space $\mathbb{X}=\mathbb{X}_{1} \times \cdots \times \mathbb{X}_{n}$, among which we explore various putative causal hypotheses. An event tree $\mathcal{T}(\boldsymbol{X})=\left(V_{\mathcal{T}}, E_{\mathcal{T}}\right)$ can be constructed to represent relationships embedded in $\boldsymbol{X}$, where $V_{\mathcal{T}}$ denotes the vertex set and $E_{\mathcal{T}}$ denotes the edge set of $\mathcal{T}(\boldsymbol{X})$. Each non-leaf node is also called a situation. Let $S_{\mathcal{T}}$ denote the set of non-leaf nodes. The floret of a situation $v \in S_{\mathcal{T}}$ is a subtree of $\mathcal{T}(\boldsymbol{X})$, denoted by $\mathcal{F}(v)=\left(V_{\mathcal{F}(v)}, E_{\mathcal{F}(v)}\right)$. The vertex set of $\mathcal{F}(v)$ consists of $v$ and the vertices in $S_{\mathcal{T}}$ connected from $v$ by a directed edge in $E_{\mathcal{T}}$ : $V_{\mathcal{F}(v)}=\{v\} \cup\left\{v^{\prime} \in V_{\mathcal{T}} \mid e_{v, v^{\prime}} \in E_{\mathcal{T}}\right\}$. The edge set of $\mathcal{F}(v)$ is a subset of $E_{\mathcal{T}}$ satisfying $E_{\mathcal{F}(v)}=\left\{e_{v, v^{\prime}}: v^{\prime} \in V_{\mathcal{T}}, e_{v, v^{\prime}} \in E_{\mathcal{T}}\right\}$

Let $\mathcal{F}_{\mathcal{T}}=\{\mathcal{F}(v)\}_{v \in S_{\mathcal{T}}}$ denote the collection of all florets on the tree $\mathcal{T}$. Let $\mu\left(v_{0}, v\right)$ denote a subpath from the root node $v_{0}$ to a node $v \in V_{\mathcal{T}}$ on the event tree. Every floret $\mathcal{F}(v)$ represents a random variable conditional on $\mu\left(v_{0}, v\right)$. We denote this conditional

random variable by $X(v)=X \mid \mu\left(v_{0}, v\right)$ for $X \in \boldsymbol{X}$. Each emanating edge $e_{v, v^{\prime}}$ of $v$ is labelled by a value $x \in \mathbb{X}(v)$. Thus, every conditional variable $X_{i}, i \in\{1, \ldots, n\}$, is represented on a set of florets on the event tree, denoted by $\mathcal{F}\left(v\left(X_{i}\right)\right)$. Previous research [3,4,6,7] has demonstrated the capability of a tree-like structure to encode the asymmetric information. The corresponding event tree $\mathcal{T}$ associated with this description can be asymmetric and non-stratified [2,4] so that the florets representing the same variable can have different distances from the root node $v_{0}$.

Figure 1 depicts an event tree for a conservator system. Its variables are $\boldsymbol{X}=\left(X_{\text {cause }}\right.$, $\left.X_{\text {leak }}, X_{\text {alarm }}, X_{s / b}, X_{\text {fail }}\right)$. The categorical variable $X_{\text {cause }}$ represents causes of defects and has three levels \{temperature, seal/pipe, and breathing system\}; $X_{\text {leak }}$ is the oil leak indicator; $X_{\text {alarm }}$ is the alarm indicator; $X_{s / b}$ is an indicator of whether there is a sight glass defect or a buchholz defect; and $X_{\text {fail }}$ is a failure indicator. This tree is constructed under the assumption that the fault caused by low temperature is irrelevant to the sight glass or buchholz defect, labelled as $s / b$ on the tree. The situations of the tree are annotated as $\left\{v_{0}, \cdots, v_{37}\right\}$, and the leaves are the unlabelled vertices. Since the last variable modelled on this tree is $X_{\text {fail }}$, the leaves represent the status of the conservator being failed or operational.
![img-0.jpeg](img-0.jpeg)

Figure 1. An event tree constructed for the conservator system of a transformer.
Let $\Lambda_{\mathcal{T}}$ denote the set of all root-to-leaf paths on the tree and $\lambda\left(v, v^{\prime}\right) \in \Lambda_{\mathcal{T}}$ denote the root-to-leaf paths passing through vertices $v, v^{\prime} \in V_{\mathcal{T}}$. The vector $\boldsymbol{\theta}_{v}=\mathbb{P}(X(v))=$ $\mathbb{P}\left(X \mid \mu\left(v_{0}, v\right)\right)$ is called the vector of primitive probabilities. Let $\boldsymbol{\theta}_{\mathcal{T}}=\left(\boldsymbol{\theta}_{v}\right)_{v \in V_{\mathcal{T}}}$, which satisfies $\sum_{v^{\prime} \in c h(v)} \theta_{v, v^{\prime}}=1$ and $\theta_{v, v^{\prime}} \in(0,1)$ for all $v \in V_{\mathcal{T}}$, where $c h(v)=\left\{v^{\prime} \in V_{\mathcal{T}} \mid e_{v, v^{\prime}} \in\right.$ $\left.E_{\mathcal{T}}\right\}$. Then, the pair $\left(\mathcal{T}(\boldsymbol{X}), \boldsymbol{\theta}_{\mathcal{T}}\right)$ indexes the probability tree [2,3] defined over $\boldsymbol{X}$.

The BN is capable of handling the missing data whenever this applies to all values of a pre-assigned set of variables by assigning a missingness indicator to each unobservable variable within that set. It is, therefore, possible to use the BN as a framework for identifying when causal hypotheses are identifiable in this rather restricted setting. The associated analyses use various graphically stated criteria-such as the front-door and the back-door criteria-see e.g., [11-13]. However, unfortunately, the types of missingness that routinely occur in reliability-and, in particular, those associated with the data we collect when performing routine maintenance-are rarely missing across the original random vector associated with the system in this sort of symmetric way. This is because we only learn about those parts of a system that we have chosen to inspect.

In contrast, the probability tree provides a natural and more flexible way to visualise and model the context-specific missingness, where the unobservability of the variable partially depends on which path it lies on the tree. Here, we import the informed missingness into the event tree by defining the floret-dependent missingness [14]. Thus, consider a floret $\mathcal{F}(v)$, if the value of the corresponding variable $X(v)$ is unobservable, then we classify this floret into $\mathcal{F}(v) \in \mathcal{F}^{M}$.

On the other hand, if conditioned on $\mu\left(v_{0}, v\right)$, the value of the variable $X(v)$ is always observed, and then the corresponding floret is classified into $\mathcal{F}(v) \in \mathcal{F}^{O}$. Accordingly, we have two subsets of florets, $\mathcal{F}^{M}$ and $\mathcal{F}^{O}$, representing unobservable florets and fully observed florets, respectively. Then, $\mathcal{F}^{M} \cap \mathcal{F}^{O}=\varnothing$ and $\mathcal{F}^{M} \cup \mathcal{F}^{O}=\mathcal{F}_{\mathcal{T}}$. For every unobservable floret $\mathcal{F}\left(v_{j}\right) \in \mathcal{F}^{M}$, we define a missing floret indicator as:

$$
B_{\mathcal{F}\left(v_{j}\right)}= \begin{cases}1 & \text { if } x\left(v_{j}\right) \text { is missing } \\ 0 & \text { otherwise }\end{cases}
$$

Then, $B_{\mathcal{F}\left(v_{j}\right)}$ represents the conditional missingness and

$$
\mathbb{P}\left(B_{\mathcal{F}\left(v_{j}\right)}=1\right)=\mathbb{P}\left(X\left(v_{j}\right) \text { missing } \mid \mu\left(v_{0}, v_{j}\right)\right)
$$

When $\mathbb{P}\left(B_{\mathcal{F}\left(v_{j}\right)}=1\right) \in(0,1)$, we construct a floret representing this indicator, denote this by $\mathcal{F}\left(v\left(B_{\mathcal{F}\left(v_{j}\right)}\right)\right)$, and call it a missing indicator floret. We then reconstruct an event tree by importing the missing indicator florets on to $\mathcal{T}$. We call this a missingness event tree (m-tree). Here, we assume that $B_{\mathcal{F}\left(v_{j}\right)}$ precedes $X\left(v_{j}\right)$, denoted by $B_{\mathcal{F}\left(v_{j}\right)} \prec X\left(v_{j}\right)$. In particular $\mathcal{F}\left(v_{j}\right)$ is appended to the edge emanating from $v\left(B_{\mathcal{F}\left(v_{j}\right)}\right)$ labelled by $B_{\mathcal{F}\left(v_{j}\right)}=0$. This artificially introduced ordering has already been shown to be useful for interpreting an event tree constructed with informed missingness [8]. The m-tree then has a new class of florets $\mathcal{F}^{M I}=\mathcal{F}(v(\boldsymbol{B}))$ for $\boldsymbol{B}=\left\{B_{\mathcal{F}}\right\}_{\mathcal{F} \in \mathcal{F}^{M}}$, which is the set of missing indicator florets. The variables associated to the m-tree are expanded to $(\boldsymbol{X}, \boldsymbol{B})$. We denote the topology of the m-tree by $\mathcal{T}(\boldsymbol{X}, \boldsymbol{B})$. An example of the missingness event tree is shown in Figure 2.

Having a missingness event tree, we further elicit a missingness staged tree from $\mathcal{T}(\boldsymbol{X}, \boldsymbol{B})$. For two situations $v$ and $w$, if $\mathcal{F}(v)$ and $\mathcal{F}(w)$ represent the same variable, then these two situations are in the same stage whenever $\boldsymbol{\theta}_{v}=\boldsymbol{\theta}_{w}$ [3], and the emanating edge $e_{v, v^{\prime}}$ is labelled the same value of $X$ as $e_{w, w^{\prime}}$ when $\theta_{v, v^{\prime}}=\theta_{w, w^{\prime}}$. Here, we relax the restrictions for a stratified staged tree where two situations in the same stage have the same distance from the root node [2,4]. For example, $v_{18}$ can be in the same stage as $v_{38}$ in the missingness event tree in Figure 2, similar example see [8].

Here, we assume that situations along the same root-to-leaf path cannot be in the same stage. This is the square-free condition defined by Collazo et al. [3]. Vertices in the same stage are assigned a unique colour, and the edges emanating from the same stage with the same label are assigned the same colour. Such a coloured tree that embeds contextspecific conditional independence relations is a missingness staged tree. Let $U=\left\{u_{1}, . ., u_{l}\right\}$ denote the set of stages in the m-tree. Let $u\left(X_{i}\right)$ represent the set of stages associated with variable $X_{i}$ and $U(\boldsymbol{X})=\left\{u\left(X_{1}\right), \cdots, u\left(X_{n}\right)\right\}$. Let $U(\boldsymbol{B})=U / U(\boldsymbol{X})$ denote the set of

stages associated to the missing floret indicators. An example of a missingness staged tree of the m-tree in Figure 2 is depicted in Figure 3.

Two situations $v_{j}, v_{k} \in u_{i} \in U$ in the same stage are in the same position $w$ if the rooted subtrees $\mathcal{T}_{v_{j}}(\boldsymbol{X}, \boldsymbol{B})$ and $\mathcal{T}_{v_{k}}(\boldsymbol{X}, \boldsymbol{B})$ are isomorphic. This clustering gives a finer partition of vertices than $U$, denoted by $W=\left\{w_{1}, \ldots, w_{m}\right\}$. A missingness chain event graph (MCEG) $\mathcal{C}(\boldsymbol{X}, \boldsymbol{B})=\left(V_{\mathcal{C}}, E_{\mathcal{C}}\right)$ can be constructed from a missingness staged tree as follows. A sink node $w_{\infty}$ is created by merging all the leaves of $\mathcal{T}(\boldsymbol{X}, \boldsymbol{B})$. Then, the vertex set is $V_{\mathcal{C}}=W \bigcup w_{\infty}$.

For any two $w, w^{\prime} \in V_{\mathcal{C}}$, we create an edge for every $v \in w$ and the child node $v^{\prime} \in \operatorname{ch}(v) \in V_{\mathcal{T}}$, which belongs to the position $w^{\prime}$, where the annotating edge probability is the same as that of $e_{v, v^{\prime}} \in E_{\mathcal{T}}$ and is inherited from the original tree. The colours of the vertices and edges of the MCEG are the same as the corresponding stages and edges in the missingness staged tree [15].

Note that the events on the event tree are chronologically ordered. By definition, a cause comes before its effects. We can be reasonably confident in providing $\boldsymbol{X}$ with a plausible order. For example, the trajectory of the events that lead to a machine's failure always starts with a cause, followed by symptoms, and terminates with a failure. Therefore, we can construct event trees for analysing system failures following this order. In this case, having failed or not is always modelled on the leaves of the tree. Examples are shown in Figures 1 and 2.

It follows that, for this special application of CEGs in system reliability, it is convenient to adapt the semantics and to replace the sink node $w_{\infty}$ defined above by $w_{\infty}^{f}$ and $w_{\infty}^{u}$. In this way, $w_{\infty}^{f}$ is the receiving node of the edges labelled by a failure, while $w_{\infty}^{u}$ is the receiving node of the edges labelled by an operational condition.

Thus, we can classify the root-to-sink paths into two categories: failure paths and deteriorating paths. The former terminate in $w_{\infty}^{f}$, while the latter terminate in $w_{\infty}^{u}$. Figure 4 gives an example of such a MCEG derived from Figure 3.

It is possible to perform conjugate inference on an idle MCEG even when the data is informed censored [8,16]. This enables us to greatly speed up the search for good explanatory models. The simplest prior to set up in this context assumes each stage vector $\boldsymbol{\theta}_{u}=\left(\theta_{u_{1}}, \ldots, \theta_{u_{j}}\right)$ is independently Dirichlet with parameters $\left(\alpha_{u 1}, \ldots, \alpha_{u m_{u}}\right)$ [3,8]. This is identical to the case when there are no missingness indicators:

$$
f(\boldsymbol{\theta} \mid \mathcal{C}(\boldsymbol{X}, \boldsymbol{B}))=\prod_{u \in U} \frac{\Gamma\left(\sum_{j=1}^{m_{u}} \alpha_{u j}\right)}{\prod_{j=1}^{m_{u}} \Gamma\left(\alpha_{u j}\right)} \prod_{j=1}^{m_{u}} \theta_{u j}^{\alpha_{u j}}
$$

Let $\alpha_{u}=\sum_{j=1}^{m_{u}} \alpha_{u j}$ so that, in particular, the equivalent sample size is $\alpha=\sum_{u \in U} \sum_{j=1}^{m_{u}} \alpha_{u j}$.
Then, given a set of observations $D$, the posterior can be computed in a closed form due to Dirichlet-multinomial conjugacy. Thus,

$$
\begin{aligned}
f(\boldsymbol{\theta} \mid D, \mathcal{C}(\boldsymbol{X}, \boldsymbol{B})) & =\prod_{u \in U} f\left(\boldsymbol{\theta}_{u} \mid D, \mathcal{C}(\boldsymbol{X}, \boldsymbol{B})\right) \\
& =\prod_{u \in U} \frac{\Gamma\left(\sum_{j=1}^{m_{u}} \alpha_{u j+}\right)}{\prod_{j=1}^{m_{u}} \Gamma\left(\alpha_{u j+}\right)} \prod_{j=1}^{m_{u}} \theta_{u j}^{\alpha_{u j+}}
\end{aligned}
$$

where $\alpha_{u j+}=\alpha_{u j}+n_{u j}$, and $\boldsymbol{\alpha}_{u+}=\boldsymbol{\alpha}_{u}+\boldsymbol{n}_{u}$ is the updated parameter vector.
The log-likelihood score for a $\operatorname{MCEG} \mathcal{C}(\boldsymbol{X}, \boldsymbol{B})$ can be decomposed into local scores associated with the variables $\boldsymbol{X}$ and the missingness indicators $\boldsymbol{B}$.

$$
\log Q(\mathcal{C}(\boldsymbol{X}, \boldsymbol{B}))=\log f_{\mathcal{C}(\boldsymbol{X}, \boldsymbol{B})}(D)=\sum_{i=1}^{n} \log Q_{u\left(X_{i}\right)}(\mathcal{C}(\boldsymbol{X}, \boldsymbol{B}))+\sum_{u \in U(\boldsymbol{B})} \log Q_{u}(\mathcal{C}(\boldsymbol{X}, \boldsymbol{B}))
$$

We can explicitly compute the log-likelihood in a closed form:

$$
\log Q(\mathcal{C}(\boldsymbol{X}, \boldsymbol{B}))=\sum_{u \in \Omega}\left(\log \Gamma\left(\alpha_{u}\right)-\log \Gamma\left(\alpha_{u+}\right)-\sum_{j=1}^{m_{u}}\left(\log \Gamma\left(\alpha_{u j}\right)-\log \Gamma\left(\alpha_{u j+}\right)\right)\right)
$$

To elicit a best scoring CEG from an event tree, it is necessary to search over all possible orderings over the variables modelled by the tree when the total order over the variables is unknown. The event tree is defined to be built with respect to $\boldsymbol{X}$, and the associated missingness event tree is built as a function of $\mathcal{T}(\boldsymbol{X})$ with appropriate hypotheses of missingness. Therefore, even when the dataset has missing values, we still only search over permutations over $\boldsymbol{X}$ to find an appropriate ordering that best explains the observed process.

Let $\Pi$ denote an ordering of $\boldsymbol{X}$. This could be a set of partial orderings. All variables represented on the m-tree can automatically be ordered given $\Pi$. We denote the m-tree with a specified ordering $\Pi$ by $\mathcal{T}(\boldsymbol{X}(\Pi), \boldsymbol{B})=\left(V_{T}, E_{T}\right)$.

It is non-trivial to identify causal structure from a finite observational dataset. However, the idle model first needs to be estimated before any causal relations can be explored. Many advances have been made in casting the causal discovery as a Bayesian model selection problem [2,17,18]. The MAP structural learning algorithm is a popular and well-developed tool for selecting a best topology of CEGs that best explains the data.

Under the hypothesis that there are no unobserved confounders [2], we render the best scoring structure selected by the MAP algorithm causal and assume it is the model of the idle system when there is no intervention imported. This enables us to further perform causal analysis. Given such a causal graph, we can derive causal hypotheses from the structure and estimate causal effects under different hypothesised underlying causal mechanisms.

Sometimes there is only a putative partial order rather than total order on the variables $\boldsymbol{X}$ whose causal relationship needs to be explored. However, in this setting we can still perform the search over candidate CEGs for the best fitting model, providing that the missing variables only extend to later nodes of the tree.

Cowell and Smith [2] and Collazo et al. [3] presented a recursive algorithm to find the best sink variable for every subset of $\boldsymbol{X}$ ordered by increasing size. This algorithm can be simply adapted for the tree built for the informedly missing data. Let $\boldsymbol{X}_{j} \subseteq \boldsymbol{X}$ denote the subset of variables whose ordering is needed to be learned and $\Pi_{\boldsymbol{X}_{j}}$ denote the best partial ordering over $\boldsymbol{X}_{j}$.

Then, through applying the algorithm designed by [2,3] on every $\boldsymbol{X}_{j}$, we can find the best ordering over the variables defined on the tree, where $\Pi=\left\{\Pi_{X_{j}}\right\}_{j}$. Here, we search over subspaces $\mathbb{X}_{j_{1}} \times \cdots \times \mathbb{X}_{j_{k}}$ for $X_{j_{1}}, \ldots, X_{j_{k}} \in \boldsymbol{X}_{j}$ and compute the local scores with respect to the corresponding $\boldsymbol{Y}$. In particular, for every $\boldsymbol{X}_{j}^{(l)}=\left\{X_{j_{1}}, \ldots, X_{j_{l}}\right\}$, where $l \in\{1, \ldots, k-1\}$, we find a best sink variable $X^{\prime} \in \boldsymbol{X}_{j}^{(l)}$ for every $\boldsymbol{X}_{j}^{(k-1)} \subseteq \boldsymbol{X}_{j}^{(k)}$ that has been ordered appropriately. The best sink variable $X^{\prime}$ is found by computing the local score of the best subtree spanned by $\boldsymbol{X}_{j}^{(k-1)} \cup\left\{X_{s}\right\}$ for every $X_{s} \in \boldsymbol{X}_{j}^{(k)}$ together with the corresponding missingness indicators.

The MAP score can be evaluated directly from the local scores that have been computed because the total score is the sum of local scores as shown in Equation (5). Two MCEGs $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ with respect to the same data set can be compared by the log-posterior Bayes factor. Suppose both trees have Dirichlet priors whose hyperparameters are $\boldsymbol{\alpha}_{1}$ and $\boldsymbol{\alpha}_{2}$. The Bayes factor, then, has a closed form [3]:

$$
\operatorname{lpBF}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)=\log q\left(\mathcal{C}_{1}\right)-\log q\left(\mathcal{C}_{2}\right)+\log Q\left(\mathcal{C}_{1}\right)-\log Q\left(\mathcal{C}_{2}\right)
$$

where $\log q\left(\mathcal{C}_{i}\right)$ denotes the log prior. Different priors over models can be chosen given expert judgement on different missingness mechanisms and conditional dependencies.

When using a uniform prior, $\log q\left(\mathcal{C}_{1}\right)-\log q\left(\mathcal{C}_{2}\right)=\frac{1}{N_{\mathcal{C}}}-\frac{1}{N_{\mathcal{C}}}=0$, where $N_{\mathcal{C}}$ denotes the total number of models.
![img-1.jpeg](img-1.jpeg)

Figure 2. A missingness event tree constructed from Figure 1.

![img-2.jpeg](img-2.jpeg)

Figure 3. A missingness staged tree of the m-tree in Figure 2.

![img-3.jpeg](img-3.jpeg)

Figure 4. A MCEG derived from Figure 3. For simplicity, the edges labelled "no" are coloured in red.

# 3. Causal Algebras for Routine Maintenance 

By assuming the best scoring CEG causal and treating it as the idle system, one can always design experiments to collect data under the influence of interventions, and thus we can estimate the causal effects from the partially observed system. By controlling certain events on the tree, the semantics of a causal CEG allow us to explore its effect on the events that lie downstream of the controlled events along the root-to-sink paths. For a reliability analysis, it is extremely useful to trace and discover the potential causes of abnormal conditions or failures. By designing causal algebras for different interventions, we can make predictive inferences about the effects of a variety of types of maintenance and thus improve the prediction of system failures.

Having defined the remedial intervention on the CEG for the reliability system in [9], here, we investigate a new class of intervention regime. In the reliability literature, there are two main categories of maintenance: corrective maintenance (CM) and preventive maintenance (PM) [19]. CM takes place after a failure, while PM often refers to a scheduled maintenance that helps to identify and prevent problems during inspections before a failure occurs [20]. In this section, we carefully customise causal algebras for the intervention in light of the latter case, calling this a routine intervention. A routine intervention not only has an impact on the lifetime of the maintained equipment but also affects the likelihood of different defects that may occur in the equipment.

# 3.1. Effects on Lifetime 

In the context of reliability, the interventions largely consist of replacing failed components of the system. This type of intervention-unusual in most causal analyses-requires special attention, especially as there are some very well-known effects of such interventions that need to be incorporated before it is possible to realistically model the effects of interventions. In particular, when describing the failure of equipment, the bathtub effect [20] is widely applicable. This divides the lifetime of an equipment into three periods: the early life of a new component has a decreasing failure rate; this is followed by a period with a constant failure rate; the failure rate rises during the wear-out period [21]. A Weibull distribution whose density is given by

$$
f(t)=\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}
$$

is often used by reliability engineers to model this varying hazard [20], where the scale parameter is $\eta>0$, and the shape parameter is $\beta>0$. The survival function takes the form:

$$
1-F(t)=e^{-\left(\frac{t}{\eta}\right)^{\beta}}
$$

Let $\Lambda_{\mathcal{C}}$ denote the set of all root-to-sink paths on the $\operatorname{MCEG} \mathcal{C}(\boldsymbol{X}(\Pi), \boldsymbol{B})$. Then, the lifetime of the repaired equipment can be modelled on the associated root-to-sink paths, denoted by $\tilde{\Lambda} \subseteq \Lambda_{\mathcal{C}}$. For $\lambda \in \tilde{\Lambda}$, let $T(\lambda)$ represent the total lifetime of the equipment when the failure trajectory is modelled on the path $\lambda$.

For a repairable system, the PM prolongs the life of the component [22-24]. By adopting the Arithmetic Reduction of Age (ARA) model, which assumes the life of the equipment is shortened up to proportionality [23], we now establish methods to evaluate the effect of the scheduled PM on the equipment's lifetime.

Let $Z_{s}^{\lambda}$ represent the failure time of an equipment with observed age $s$ given a failure process that is modelled on the path $\lambda$. Then, the survival function is

$$
\mathbb{P}\left(Z_{s}^{\lambda}>t\right)=\frac{1-F_{\lambda}(s+t)}{1-F_{\lambda}(s)}=e^{-\left(\frac{s+t}{\eta_{\lambda}}\right)^{\beta_{\lambda}}+\left(\frac{s}{\eta_{\lambda}}\right)^{\beta_{\lambda}}}
$$

where $F_{\lambda}(\cdot)$ denotes the reliability distribution for failure trajectory $\lambda$.
In an idle system, for $\lambda \in \tilde{\Lambda}, T(\lambda)$ has the same distribution as $Z_{0}^{\lambda}$, i.e., $T(\lambda) \stackrel{d}{=} Z_{0}^{\lambda}$. Thus,

$$
\mathbb{P}(T(\lambda)>t)=\mathbb{P}\left(Z_{0}^{\lambda}>t\right)=1-F_{\lambda}(t)
$$

Preventive maintenance can be scheduled periodically. However, for simplicity, we only demonstrate the effect of a single time routine maintenance in this paper. We suppose that an equipment is diagnosed during a routine maintenance and is repaired at age $\tau$. Kijima [24] and Guessoum and Aupiedy [23] introduced a parameter representing the degree of repair, denoted by $A \in[0,1]$. When $A=0$, the repair is perfect and restores the maintained part to as good as new (AGAN). On the other hand, $A=1$ corresponds to a minimal repair, after which the maintained part is functioning as it was just prior to the repair.

Since the repaired equipment is rejuvenated, the virtual age [23,24] after maintenance is then $A \tau$. Let $T^{*}(\lambda)$ denote the post-intervention time to failure. Then, after a routine intervention, the residual lifetime of the maintained equipment has the same distribution as $Z_{A \tau}^{\lambda}$. Therefore,

$$
\mathbb{P}\left(T^{*}(\lambda)>t\right)=\mathbb{P}\left(Z_{A \tau}^{\lambda}>t\right)=\frac{1-F_{\lambda}(t+A \tau)}{1-F_{\lambda}(A \tau)}
$$

# 3.2. Manipulations on the MCEG 

If $X_{i} \in \boldsymbol{X}$ takes value $x_{i j}$, let $e\left(x_{i j}\right) \in E_{\mathcal{C}}$ denote the edges labelled by this value that emanate from $w\left(X_{i}\right)$. The set of vertices receiving $e\left(x_{i j}\right)$ are represented by $w\left(x_{i j}\right)$. The path related probability, denoted by $\pi(\lambda)$ for $\lambda \in \Lambda_{\mathcal{C}}$, can then be factorised as:

$$
\pi(\lambda)=\prod_{e \in E_{\lambda}} \theta_{e}
$$

where $E_{\lambda}$ represents a collection of edges lying along the path $\lambda$.
When there is a routine intervention, we are only interested in the process portrayed by the deteriorating paths. We denote this set of paths by $\Lambda_{x_{f a l, 0}}=\Lambda\left(e\left(x_{f a l l, 0}\right)\right)$, where $x_{f a l l, 0}$ represents $X_{f a l l}=0$. Whatever this preventive action is, an analogue of the do-operation $d o\left(X_{f a l l}=0\right)$ is imported into the idle MCEG. Thus, we force $e\left(x_{f a l l, 0}\right)$ to have probability 1 and $e\left(x_{f a l l, 1}\right)$ to have probability 0 , or, equivalently, we manipulate $\Lambda_{x_{f a l l, 0}}$. Therefore, we always have the post-intervened path probability:

$$
\hat{\pi}^{\Lambda_{x_{f a l l, 0}}}(\lambda)= \begin{cases}\frac{\prod_{e \in E_{\lambda}} \theta_{e}}{\theta_{e\left(x_{f a l l, 0}\right)}} & \text { if } \lambda \in \Lambda_{x_{f a l l, 0}} \\
0 & \text { otherwise }\end{cases}
$$

This is a singular manipulation on the MCEG and yields a manipulated MCEG with respect to $\Lambda_{x_{f a l l, 0}}$. We denote this by $\mathcal{C}^{\Lambda_{x_{f a l l, 0}}}$.

Depending on the preventive action taken, other manipulations can also be imported into the MCEG in addition to the singular manipulation on $\Lambda_{x_{f a l l, 0}}$. We next demonstrate two scenarios of composite manipulations.

### 3.2.1. Composite Singular Manipulations under Routine Intervention

In this section, we discuss the situation where the preventive maintenance perfectly repaired a problem, and, as a consequence of this repair, an event $x_{r}$ is forced to occur. The event $x_{r}$ is labelled on a set of edges $e\left(x_{r}\right)$ whose receiving nodes are $w\left(x_{r}\right)$ and emanating nodes are $p a\left(w\left(x_{r}\right)\right)$. In this case, the unit will be forced to pass through every edge $e \in e\left(x_{r}\right)$ with probability 1 . We, therefore, have a composition of singular manipulations, and the manipulated events are $\boldsymbol{x}=\left\{x_{f a l l, 0}, x_{r}\right\}$. On an MCEG, the controlled event is represented by

$$
\Lambda_{\boldsymbol{x}}=\Lambda(e(\boldsymbol{x}))=\Lambda\left(e\left(x_{f a l l, 0}\right)\right) \cap \Lambda\left(e\left(x_{r}\right)\right)
$$

Let $\mathcal{F}(e(\boldsymbol{x}))$ denote the set of florets that the edges $e(\boldsymbol{x})$ lie in.
If we are interested in the effect of the routine maintenance on event $y$, then, on the MCEG, we represent it by $\Lambda_{y}=\Lambda(e(y))$. The set of florets that $e(y)$ lies in is denoted by $\mathcal{F}(e(y))$.

Given a CEG, let $\pi\left(\Lambda_{y} \| \Lambda_{x}\right)$ denote the probability of observing event $y$ given a manipulation that forces the events $\boldsymbol{x}$ to occur. We aim to estimate this probability from the observed data and to demonstrate that the effects of a routine intervention are identifiable. We have shown in [9] that causal effects from a singular manipulation are estimable, also called recoverable, by adapting the back-door theorem [5]. Here, we simply extend our previous results [9] so that it now also applies to the types of composite manipulations that we discuss here.

The MCEG provides flexible choices of events $z$ to be the back-door partition so that $\Lambda_{z}$ partitions $\Lambda_{\mathcal{C}}[6,7]$. We first impose a constraint on $z$ that $\mathcal{F}(e(z)) \nsubseteq \mathcal{F}^{M I}$, i.e., that cannot be a missingness indicator. This is to ensure that $\pi\left(\Lambda_{y} \| \Lambda_{x}\right)$ can be estimated from the partially observed data [9]. Note that any of $\mathcal{F}(e(\boldsymbol{x})), \mathcal{F}(e(y)), \mathcal{F}(e(z))$ might be unobservable. Let

$$
\mathcal{F}_{x \cup y \cup z}=\left\{\mathcal{F}: \mathcal{F} \in \mathcal{F}(e(\boldsymbol{x})) \cup \mathcal{F}(e(y)) \cup \mathcal{F}(e(z)) \text { and } \mathcal{F} \notin \mathcal{F}^{M I}\right\}
$$

We define the manifest paths to be the largest set of root-to-sink paths on the MCEG passing along edges labelled by $\boldsymbol{x}, y$ and $\boldsymbol{z}$. We let $\boldsymbol{b}_{\mathcal{F}(e(\boldsymbol{x})), 0}=\left\{b_{\mathcal{F}, 0}\right\}_{\mathcal{F} \in \mathcal{F}(e(\boldsymbol{x}))}$ denote the set of missingness indicators of florets $\mathcal{F}(e(\boldsymbol{x}))$ taking value 0 , i.e., values of the corresponding floret variables are observed. Then, the manifest paths are

$$
\Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{x, y, y, z, 0}}\right)\right)=\Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}(e(\boldsymbol{x})), 0}\right)\right) \cap \Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}(e(y)), 0}\right)\right) \cap \Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}(e(z)), 0}\right)\right)
$$

We can construct a sub-MCEG $\mathcal{C}^{M}$ using the manifest paths. Let the collection of the root-to-sink paths of this subgraph be $\Lambda_{\mathcal{C}^{M}}=\Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{x, y, z, 0}}\right)\right)$. We call this sub-MCEG the manifest MCEG. This construction ensures that there is no edge in the manifest MCEG associated with a controlled event, effect, or partition event being missing.

We next reconstruct $\pi\left(\Lambda_{y} \| \Lambda_{x}\right)$ from the manifest MCEG. Let $\pi^{\Lambda_{\mathcal{C}^{M}}}\left(\Lambda_{y} \| \Lambda_{z}\right)$ denote the probability of observing an event $y$ given a manipulation forcing $\boldsymbol{x}$ to happen within the manifest MCEG. Note that the manipulated MCEG is a subgraph of the manifest MCEG. For a singular manipulation on $\Lambda_{x}$, the manipulated paths on the manifest MCEG are

$$
\Lambda_{*}=\Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{x, y, z, 0}}\right)\right) \cap \Lambda_{x}
$$

The manipulated MCEG with respect to $\Lambda_{*}$ is then denoted by $\overline{\mathcal{C}}^{\Lambda_{*}}$ and satisfies $\Lambda_{\overline{\mathcal{C}}^{\Lambda_{*}}}=\Lambda_{*}$.
Theorem 1 (The m-back-door criterion for composite singular manipulations). When a dataset has missing values, the effect of a singular manipulation on $\boldsymbol{x}$ on $y$ is identifiable on the MCEG if we can find a partition $\Lambda_{x}$ of $\Lambda_{\mathcal{C}^{M}}$ such that

$$
\pi^{\Lambda_{\mathcal{C}^{M}}}\left(\Lambda_{y} \| \Lambda_{x}\right)=\sum_{z} \pi\left(\Lambda_{y} \mid \Lambda_{x}, \Lambda_{z}, \Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{x, y, z, 0}}\right)\right)\right) \pi\left(\Lambda_{z} \mid \Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{x, y, z, 0}}\right)\right)\right)
$$

For the proof of this theorem, see $[9,14]$.
Example 1. Given the causal MCEG in Figure 4 of a conservator system, we demonstrate how the formulae defined above works for a specific routine maintenance that successfully prevents an oil leak. This is equivalent to importing a combination of do $\left(X_{\text {fail }}=0\right)$ and do $\left(X_{\text {leak }}=0\right)$ operations to the idle MCEG. The controlled events are $\boldsymbol{x}=\left\{x_{\text {fail }, 0}, x_{\text {leak }, 0}\right\}$. From Figure 4, we next identify the associated root-to-sink paths. In particular,

$$
\begin{gathered}
\Lambda_{x_{\text {fail }, 0}}=\bigcup_{w \in\left\{w_{25}, \cdots, w_{30}\right\}} \Lambda\left(e_{w, w_{m}^{0}}\right) \\
\Lambda_{x_{\text {leak }, 0}}=\Lambda\left(e_{w_{2}, w_{8}}\right) \cup \Lambda\left(e_{w_{3}, w_{9}}\right) \cup \Lambda\left(e_{w_{4}, w_{10}}\right)
\end{gathered}
$$

and $\Lambda_{x_{\text {fail }, 0}, x_{\text {leak }, 0}}=\Lambda_{x_{\text {fail }, 0}} \cap \Lambda_{x_{\text {leak }, 0}}$.
To next focus on alarm, the effect event is $x_{\text {alarm }, 1}$. The associated set of paths is $\Lambda_{x_{\text {alarm }, 1}}=$ $\Lambda\left(e_{w_{9}, w_{25}}\right) \cup \Lambda\left(e_{w_{6}, w_{11}}\right) \cup \Lambda\left(e_{w_{7}, w_{13}}\right) \cup \Lambda\left(e_{w_{8}, w_{25}}\right) \cup \Lambda\left(e_{w_{9}, w_{12}}\right) \cup \Lambda\left(e_{w_{10}, w_{14}}\right)$. The causal query with respect to $\boldsymbol{x}$ is identifiable whenever $\pi\left(\Lambda_{x_{\text {alarm }, 1}} \| \Lambda_{x_{\text {fail }, 0}, x_{\text {leak }, 0}}\right)$ can be recovered from the MCEG by estimating it from the dataset with missing entries. There are a variety of possible choices for the partition events $z$. Here, we simply let $z$ be $X_{\text {cause }}$ whose corresponding positions lie upstream of the controlled events $x_{\text {leak }, 0}$ on the tree. The corresponding floret is, then, $\mathcal{F}(e(z))$ $=\mathcal{F}\left(w_{1}\right)$.

We now construct the manifest MCEG and the manipulated MCEG in order to identify the effects of the intervention. Notice that the controlled events and the effect events are always observable in our example. Thus,

$$
\begin{gathered}
\Lambda\left(w\left(b_{\mathcal{F}(e(\boldsymbol{x})), 0}\right)\right)=\left(\bigcup_{w \in\left\{w_{25}, \cdots, w_{30}\right\}} \Lambda(w)\right) \cap\left(\bigcup_{w \in\left\{w_{2}, w_{3}, w_{4}\right\}} \Lambda(w)\right)=\Lambda_{\mathcal{C}} \\
\Lambda\left(w\left(b_{\mathcal{F}(e(\boldsymbol{y})), 0}\right)\right)=\bigcup_{w \in\left\{w_{5}, \cdots, w_{10}\right\}}=\Lambda_{\mathcal{C}}
\end{gathered}
$$

However, the back-door partition events might be missing. The collection of paths along which $\boldsymbol{z}$ are observed is

$$
\Lambda\left(w\left(b_{F(e(z)), 0}\right)\right)=\Lambda\left(w_{1}\right)
$$

Following Equation (17), the manifest paths are $\Lambda\left(w\left(\boldsymbol{b}_{F_{x, y, z, 0}}\right)\right)=\Lambda_{\mathcal{C}} \cap \Lambda\left(w_{1}\right)=\Lambda\left(w_{1}\right)$. Thus, to investigate this, we construct the manifest MCEG with respect to $\Lambda\left(w_{1}\right)$. This is a subgraph of the idle MCEG in Figure 4 obtained by simply removing the edge $e_{w_{0}, w_{3}}$, which represents the causes that are missing. We further elicit the manipulated MCEG from the manifest MCEG. By the definition of the manipulated paths given in Equation (18), we select the manipulated paths from the manifest paths: $\Lambda_{*}=\Lambda\left(w_{1}\right) \cap \Lambda_{x_{f a l, 0}, x_{l e a k, 0}}$. Since the intervention forces $x_{f a i l, 0}$ and $x_{\text {leak, } 0}$ to happen, the events $x_{f a i l, 1}$ and $x_{\text {leak, } 1}$ should never be observed. Thus, the probability of a manipulated path passing along the edges $e\left(x_{f a i l, 1}\right)$ and $e\left(x_{\text {leak }, 1}\right)$ is 0 .

Equivalently, the positions $w\left(x_{f a i l, 1}\right)=w_{m}^{t}$ and $w\left(e\left(x_{l e a k, 1}\right)\right)=\left\{w_{5}, w_{6}, w_{7}\right\}$ should never be passed through by any path in the manipulated graph. Then, by removing the nodes and edges that are not traversed by the manipulated paths in the manifest MCEG, we can derive the manipulated MCEG with respect to $\Lambda_{*}$, see Figure 5. We can then estimate the causal effects on alarm using the formula given in the $m$-back-door theorem defined above. The conditional path probabilities in Equation (19) can simply be evaluated using the factorisation of the corresponding primitive probabilities in the manipulated MCEG.
![img-4.jpeg](img-4.jpeg)

Figure 5. The manipulated MCEG when controlling $x_{\text {leak }, 0}$ and $x_{f a i l, 0}$

# 3.2.2. Composite Singular and Stochastic Manipulations under Routine Intervention 

During routine inspections, the field engineers may clean the components, check the oil level and leakage, replace some units, and so on [25]. Since there are different types of repair and because the degree of this repair varies, the manipulations enacted by the routine intervention could be more complicated than forcing a specific event to happen. In

fact, repairing or replacing an equipment could affect multiple units or multiple defects of a unit.

Therefore, depending on the repaired subcomponent and the degree of repair, multiple florets can be influenced separately and simultaneously. Thus, a routine intervention could introduce more uncertainty to the probability distributions over these relevant florets. Therefore, the distributions of some of the primitive probabilities may need to be reassigned. This manipulation is then called a stochastic manipulation on the MCEG.

Unlike a remedial intervention [9], a stochastic manipulation induced by a routine intervention is not restricted to root causes. Consider a floret $\mathcal{F}$ whose distribution is manipulated by a routine intervention. The events represented by this floret could be defects or symptoms of the maintained equipment.

Let $\boldsymbol{x}_{r}$ denote the controlled events of a routine intervention. Suppose we can find the edges labelled by these events, denoted by $e\left(\boldsymbol{x}_{r}\right)$, then $\mathcal{F}\left(e\left(\boldsymbol{x}_{r}\right)\right)$ is the set of florets whose distribution are manipulated under the routine intervention. Let $\boldsymbol{w}^{*}=p a\left(w\left(\boldsymbol{x}_{r}\right)\right)$ denote the set of emanating nodes of edges $e\left(\boldsymbol{x}_{r}\right)$. We can then conclude that $\mathcal{F}\left(\boldsymbol{w}^{*}\right)=\mathcal{F}\left(e\left(\boldsymbol{x}_{r}\right)\right)$.

For $w \in \boldsymbol{w}^{*}$, we update the probability distribution after a routine intervention via the transformation:

$$
\hat{q}\left(\boldsymbol{\theta}_{w}\right)=G\left[q\left(\boldsymbol{\theta}_{w}\right)\right]
$$

where $\hat{q}(\cdot)$ represents the post-intervened distribution. The transformation $G$ preserves the properties of the transition probabilities so that $\sum_{e \in E(w)} \theta_{e}=1$ and $\theta_{e}>0$.

Motivated by the steady model [26,27], one straightforward option is to map distributions to distributions through non-linear state space models. A possible transformation to increase uncertainty in a distribution is the power steady transformation [26,28], which can be characterised by information loss after the intervention takes.

$$
\hat{q}\left(\boldsymbol{\theta}_{w}\right) \propto q\left(\boldsymbol{\theta}_{w}\right)^{\phi}
$$

where $\phi \in(0,1]$. Assume that the value of $\phi$ can be assessed and informed by the domain experts. Then, a power steady evolution assumes that such information loss is linear and proportional to $\phi$ so that:

$$
\mathbb{E}\left[\log \hat{q}\left(\boldsymbol{\theta}_{w}\right)\right]=\phi \mathbb{E}\left[\log q\left(\boldsymbol{\theta}_{w}\right)\right]+c
$$

for some constant $c$.
For a Dirichlet prior $\boldsymbol{\theta}_{w} \sim \operatorname{Dirichlet}\left(\boldsymbol{\alpha}_{w}\right)$ with concentration parameters $\boldsymbol{\alpha}_{w}=\left(\alpha_{w 1}, \cdots, \alpha_{w m_{w}}\right)$, following [29], we can transform it to $\operatorname{Dirichlet}\left(\hat{\boldsymbol{\alpha}}_{w}\right)$, where $\hat{\boldsymbol{\alpha}}_{w}=$ $\left(\hat{\alpha}_{w 1}, \cdots, \hat{\alpha}_{w m_{w}}\right)$ and $\hat{\alpha}_{w j}-1=\phi\left(\alpha_{w j}-1\right)$, for $j \in\left\{1, \cdots, m_{w}\right\}$. By this transformation, the mode remains the same. We can consider such manipulations when searching for the best scoring MCEG for causal discovery. This is explained in Section 4.

Having updated the transition probabilities, the path probabilities under the stochastic manipulation given a routine intervention can be re-evaluated. Let $\Lambda\left(\boldsymbol{w}^{*}\right)$ denote the set of root-to-sink paths on the MCEG passing through any position $w \in \boldsymbol{w}^{*}$. Let $\bar{\Lambda}\left(\boldsymbol{w}^{*}\right)=\Lambda_{\mathcal{C}} / \Lambda\left(\boldsymbol{w}^{*}\right)$. Then, the probabilities of paths in $\Lambda_{x_{f a l, 0}} \cap \Lambda\left(\boldsymbol{w}^{*}\right)$ are affected by both the singular manipulation on $x_{f a i l, 0}$ and the stochastic manipulation on $\mathcal{F}\left(\boldsymbol{w}^{*}\right)$. The probabilities of paths in $\Lambda_{x_{f a i, 0}} \cap \bar{\Lambda}\left(\boldsymbol{w}^{*}\right)$ are affected by the singluar manipulation on $x_{f a i l, 0}$. Therefore, the post-intervened path probabilities on the MCEG are:

$$
\hat{\pi}(\lambda)= \begin{cases}\frac{\prod_{e \in E_{\lambda}} \theta_{e}}{\theta_{e\left(x_{f a i l, 0}\right)} \cdot \prod_{e^{\prime} \in E\left(\boldsymbol{w}^{*}\right) \cap E_{\lambda}} \theta_{e^{\prime}}} \times \prod_{e^{\prime} \in E\left(\boldsymbol{w}^{*}\right) \cap E_{\lambda}} \hat{\theta}_{e^{\prime}} & \text { if } \lambda \in \Lambda_{x_{f a i l, 0}} \cap \Lambda\left(\boldsymbol{w}^{*}\right) \\ \frac{\prod_{e \in E_{\lambda}} \theta_{e}}{\theta_{e\left(x_{f, 0}\right)}} & \text { if } \lambda \in \Lambda_{x_{f a i l, 0}} \cap \bar{\Lambda}\left(\boldsymbol{w}^{*}\right) \\ 0 & \text { otherwise }\end{cases}
$$

Let $\boldsymbol{x}^{*}$ denote the set of all events represented on $\mathcal{F}\left(\boldsymbol{w}^{*}\right)$ and let $\boldsymbol{x}=\boldsymbol{x}_{\text {fail }, 0} \cap \boldsymbol{x}^{*}$ denote the set of events that are manipulated. Then, the set of florets associated with the manipulated events, the effect event and the partition events is

$$
\mathcal{F}_{\boldsymbol{x} \cup y \cup z}=\left\{\mathcal{F}: \mathcal{F} \in \mathcal{F}\left(e\left(x_{f a i l, 0}\right)\right) \cup \mathcal{F}\left(\boldsymbol{w}^{*}\right) \cup \mathcal{F}(e(y)) \cup \mathcal{F}(e(\boldsymbol{z})) \text { and } \mathcal{F} \notin \mathcal{F}^{M I}\right\}
$$

The manifest paths are defined analogously to Equation (17) so that no event of interest, i.e., $\boldsymbol{x}, \boldsymbol{y}$, and $\boldsymbol{z}$, is missing in this restricted class of paths.

$$
\Lambda\left(w\left(\boldsymbol{b}_{\mathcal{F}_{w, y, z, 0}}\right)\right)=\Lambda\left(w\left(b_{\mathcal{F}\left(e\left(x_{f a i l, 0}\right)\right), 0}\right)\right) \cap \Lambda\left(\boldsymbol{w}^{*}\right) \cap \Lambda\left(w\left(b_{\mathcal{F}(e(y)), 0}\right)\right) \cap \Lambda\left(w\left(b_{\mathcal{F}(e(z)), 0}\right)\right)
$$

We next show the identifiability of the effects by adapting the back-door criterion for stochastic manipulation [9]. More specifically, this is possible whenever we need to identify a $\Lambda_{z}$ that partitions the root-to-sink paths of the manifest MCEG $\mathcal{C}^{M}$ so that

$$
\begin{aligned}
& \pi^{\Lambda_{c^{M}}}\left(\Lambda_{y} \| \Lambda_{x_{f a i l, 0}}, \hat{\boldsymbol{\theta}}_{\boldsymbol{w}^{*}}\right)=\sum_{x \in \boldsymbol{x}} \sum_{z} \pi\left(\Lambda_{y} \mid \Lambda_{x}, \Lambda_{z}, \Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}, 0}\right)\right)\right) \pi\left(\Lambda_{z} \mid \Lambda_{x}, \Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}, 0}\right)\right)\right) \\
& \times \hat{\pi}\left(\Lambda_{x} \mid \Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}, 0}\right)\right)\right)
\end{aligned}
$$

where

$$
\hat{\pi}\left(\Lambda_{x} \mid \Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}, 0}\right)\right)\right)=\frac{\hat{\pi}\left(\Lambda_{x}, \Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}}\right)\right)\right)}{\hat{\pi}\left(\Lambda\left(w\left(\boldsymbol{b}_{F_{w, y, z, 0}, 0}\right)\right)\right)}
$$

The numerator and denominator are the post-intervened path probabilities. Note that these can be computed using Equation (28). Assuming that a stochastic manipulation on $\hat{\boldsymbol{\theta}}_{w^{*}}$ is equivalent to forcing each $x$ with probability $\pi\left(\Lambda_{x} \| \hat{\boldsymbol{\theta}}_{w^{*}}\right)$ for every $x \in x^{*}$ [5], we can obtain Equation (31) by expressing the causal query as

$$
\pi^{\Lambda_{c^{M}}}\left(\Lambda_{y} \| \Lambda_{x_{f a i l, 0}}, \hat{\boldsymbol{\theta}}_{\boldsymbol{w}^{*}}\right)=\sum_{x \in \boldsymbol{x}^{*}} \pi^{\Lambda_{c^{M}}}\left(\Lambda_{y} \| \Lambda_{x_{f a i l, 0}, x}\right) \pi^{\Lambda_{c^{M}}}\left(\Lambda_{x} \mid \Lambda_{x_{f a i l, 0}}, \hat{\boldsymbol{\theta}}_{\boldsymbol{w}^{*}}\right)
$$

The first component on the right hand side of the equation can be evaluated by applying the results in Equation (19), and the second component can be simplified to Equation (32). By doing this, we have the expression in Equation (31).

Example 2. Given the idle system in Figure 4, suppose routine maintenance involved in checking the oil level, cleaning the leakage, and topping up the oil, but this did not fully prevent the oil leak. The manipulations imported to the idle system under this intervention are then different from the one we discussed in Example 1. Suppose florets $\mathcal{F}\left(w_{2}\right), \mathcal{F}\left(w_{3}\right), \mathcal{F}\left(w_{4}\right)$ are directly affected in response to the maintenance. Then, these florets are stochastically manipulated, and $\boldsymbol{w}^{*}=\left\{w_{2}, w_{3}, w_{4}\right\}$. This gives the same $\Lambda\left(w\left(b_{\mathcal{F}(e(x)), 0}\right)\right)$ as in Example 1. If we are interested in how the sight glass or buchholz defect is affected by this intervention, then the effect event is $x_{s} / b_{s} 1$. Note that this event is unobservable and $\Lambda\left(w\left(b_{\mathcal{F}\left(e\left(x_{s} / b_{s}\right)\right), 0}\right)\right)=\bigcup_{w \in\left\{w_{19}, \cdots, w_{24}\right\}} \Lambda(w)$.

Here, we can choose $X_{\text {alarm }}$ as the partition events $z$, and these are always observable. Next the manifest MCEG is constructed from the idle MCEG by removing the paths that do not traverse any position in $\left\{w_{19}, \cdots, w_{24}\right\}$. The manipulated MCEG is obtained by further deleting the paths that terminate in $w_{m}^{T}$ from the manifest MCEG, see Figure 6. If the post-intervention probabilities $\hat{\boldsymbol{\theta}}_{\boldsymbol{w}^{*}}$ are known, then we can evaluate the path probabilities in the manipulated MCEG following the factorisations we specified in Equation (28). Then, conditional on the manifest paths, each probability in Equation (31) can be computed to estimate the effects of the observed maintenance on the sight glass or the buchholz.

![img-5.jpeg](img-5.jpeg)

Figure 6. The manipulated MCEG for Example 2.

# 4. Experiments 

Due to commercial sensitivity, we cannot disclose the real maintenance data from the energy distribution company and examine our methodology on it. Here, we show experimentally, using synthetic data, how the structural learning algorithm over a class of MCEGs can be used to provide useful causal inferences. We, then, perform a comparative study to demonstrate how the predictions are improved when incorporating the causal algebras we specified in previous section into the algorithm for the synthetic experimental data.

### 4.1. Causal Discovery with the Structural Learning Algorithm

Assume a ground truth missingness staged tree in Figure 3 and a corresponding MCEG in Figure 4 are valid. Assume the causal ordering here is $\Pi_{1}=X_{\text {cause }} \prec X_{\text {leak }}$ $\prec X_{\text {alarm }} \prec X_{s / b} \prec X_{\text {fail }}$. The oil leak, alarm, and sight glass or buchholz defect are faults that may appear before a failure or routine maintenance. Thus, the oil leak could be a potential cause of alarm and the defect in buchholz or sight glass. We assume that, for any floret, the parameters of primitive probability vector are independent, and the vectors of primitive probabilities associated with each stage are mutually independent.

This ensures a model search based on product of independent Dirichlet priors over the model parameters and a closed-form conjugate analysis [30]. Based on these assumptions, we now generate observation data $D_{1}$ of size 5000 from the ground truth MCEG with the corresponding hypothesized transition probabilities. This emulates the dataset in a situation when there has been no intervention to the system.

To begin to learn a best model for $D_{1}$ given the event tree in Figure 2, we specify the Dirichlet hyperparameters. We use established methods and treat each $\alpha_{a j}$ as the number of phantom units [3], which is believed to arrive at $j^{\text {th }}$ child of stage $u$. We let the total phantom units entering the root vertex $v_{0}$ be 1 and denote this by $\alpha=1$.

By performing the MAP algorithm, the best scoring MCEG is shown in Figure 7. In this MCEG, denoted by $\mathcal{C}\left(\boldsymbol{X}\left(\Pi_{1}\right), \boldsymbol{B}\right)$, the positions representing the same variable $X_{i} \in \boldsymbol{X}$ are vertically aligned in descending order with respect to $\mathbb{P}\left(X_{i}(w)=1 \mid D_{1}, \mu\left(w_{0}, w\right)\right)$. For transparency, the edges that are supposed to have a label "yes" have been coloured red for clarity.

The posterior means for each stage are summarised in Table 1. The score of this selected model is $-20,389.83$. The stages for $X_{\text {leak }}, X_{\text {alarm }}$ and the missing indicator of $s / b$ defect in this tree are accurately learned by the algorithm when these are compared with the stages in the ground truth MCEG. In terms of the stages for $X_{s / b}$, the stage assigned to $v_{23}$ is wrong. There are 15 misclassifications appearing for $X_{\text {fail }}$. One possible reason is that the dataset is not sufficiently large to provide sufficient information on the last event modelled on the tree.

The best scoring MCEG in Figure 7 has a complex topology because many stages for the last variable modelled on the tree are misspecified. However, we can still summarise some causal explanations from it when assuming it is causal. We read the causal relationships from the semantics of a causal CEG in an analogous way to a causal BN [3,6]. For example, from Figure 7, we see that all the edges representing oil leak point to the stage $u^{\prime}=$ $\left\{w_{6}, \cdots, w_{9}\right\}$, which is coloured in green, while the edges representing no leak point to the stage $u^{\prime \prime}=\left\{w_{10}, \cdots, w_{13}\right\}$, which is coloured in brown. The stage $u^{\prime}$ is located above $u^{\prime \prime}$ on the tree, meaning the mean posterior probability of alarm at this stage is higher than that at $u^{\prime \prime}$.

Therefore, the oil leak gives rise to the likelihood of alarm. Root causes also lie upstream of alarm on the tree and can affect the possibility of alarm. However, from Figure 7, whether the cause is missing and which cause is observed appear to have no influence on alarm given an oil leak. Thus, given the oil leak, the alarm is independent of the root causes we specified for this model. We could say that the oil leak is the main cause of alarm given the hypothesised causal ordering $\Pi_{1}$. One causal implication of this discovery is that we could prevent an alarm by fixing or preventing the oil leak. For positions associated with failure indicators, $w_{37}$ is aligned at the lowest position. This means that the probability $\mathbb{P}\left(X_{\text {fail }}=1 \mid \mu\left(w_{0}, w_{37}\right), D_{1}\right)$ is the lowest compared with the probability of failure conditional on the position $w_{34}$ or $w_{35}$ or $w_{36}$. There are eight edges pointing to $w_{37}$ labelled by no $s / b$ defect and only one edge pointing to it labelled by a $s / b$ defect. Thus, to increase the reliability of the machine, we can schedule the preventive maintenance for the sight glass or the buchholz.

# 4.2. A Comparison Study 

Now, we assume the routine intervention described in Example 2 has occurred, and Figure 4 portrays the real causal structure. We, then, simulate synthetic data $D_{2}$ of size 5000 from this intervened model to emulate an experimental dataset by the following setups. First, we assume the 5000 pieces of equipment here have been intervened in the same way by the same routine maintenance. Second, a complete and unique root-to-sink path on the tree can be identified for each case in $D_{2}$. Third, assume we have the estimated posteriors from the past failure data before conduction of routine maintenance, and these are now used as priors to generate the data that would be observed after the routine maintenance.

Here, the prior independence assumptions are still assumed to be valid so that conjugate sampling can be characterised. To simulate from the intervened system instead of the idle system, the florets $\mathcal{F}\left(w_{2}\right), \mathcal{F}\left(w_{3}\right), \mathcal{F}\left(w_{4}\right)$ are stochastically manipulated in response to the routine maintenance, and we adjust the corresponding Dirichlet hyperparameters as described in the previous section.

![img-6.jpeg](img-6.jpeg)

Figure 7. The best scoring MCEG selected for $D_{1}$ with hypothesised causal ordering $\Pi_{1}$.
Table 1. Mean posterior probabilities $\mathbb{P}\left(X=1 \mid\right.$ stage, $\left.D_{1}\right)$.


It is possible to embody the effects of this intervention when learning the causal structure by incorporating the stochastic manipulations we developed in the previous section into the MAP algorithm. We can check whether this improves the causal structure learning and parameter estimations. On the corresponding missingness event tree, see Figure 2, we accordingly revise the Dirichlet hyperparameters of florets $\mathcal{F}\left(v_{1}\right), \mathcal{F}\left(v_{5}\right), \mathcal{F}\left(v_{6}\right)$ and $\mathcal{F}\left(v_{7}\right)$ using the method we proposed in Section 3.2.2.

We defined $\phi$ in Equation (27) to add uncertainties to the intervened floret distributions. In this study, we aim to compare the estimates learned from the best scoring model selected by the algorithm when no distributions are manipulated, i.e., $\phi=1$, with the estimates learned from the best scoring model selected by the algorithm when inputting $\phi<1$. In particular, we consider six different cases here: $\phi=0.1, \phi=0.3, \phi=0.5, \phi=0.7, \phi=0.9$, and $\phi=1$.

Now, we run the algorithm for $\alpha=0.001, \alpha=0.01, \alpha=0.1, \alpha=1, \alpha=3, \alpha=5$, where $\alpha$ is the prior parameter representing the number of phantom units entering the root node. We assess the resulted models in terms of situational errors [31] and MAP scores. The situational error (The total situational error of a tree is evaluated as $\gamma(\mathcal{T})=$ $\sum_{v \in \mathcal{V}_{T}}\left\|\theta_{v}^{*}-\hat{\theta}_{v}\right\|_{2}$ ) for $\alpha$ situation $v$ measures the Euclidean distance between the true conditional probabilities $\theta_{v}^{*}$ and the mean posterior probabilities $\hat{\theta}_{v}$ estimated on the best scoring model.

The results are shown in Figure 8. The upper panel of each plot displays the total situational errors, while the lower panel displays the MAP scores for the best scoring models for different values of $\phi$. For any prior parameter $\alpha$ we choose, we observe that the best scoring model is selected from the algorithm by setting $\phi=0.1$, which gives the smallest

situational error and the highest MAP score. In particular, the situational error rises when $\phi$ increases towards 1. Thus, the posterior parameters are better estimated by incorporating the manipulations into the learning algorithm when modelling the experimental data for an intervened system.

When $\phi=1$ (i.e., the distributions are not manipulated), the MAP score in each plot of Figure 8 is much lower than that for $\phi=0.1$. This means the best structure selected with $\phi=0.1$ is more consistent with the dataset $D_{2}$ than the best model selected by the algorithm without importing stochastic manipulations.
![img-7.jpeg](img-7.jpeg)

Figure 8. Comparing situational errors and MAP scores for the best scoring models selected to fit $D_{2}$. The x-axis of each plot is labelled by different values of $\phi$, where $\phi=1$ refers to the case when no manipulation is imported to the prior. Each plot displays results for a specified total phantom number $\alpha$.

# 5. Discussion 

Thus far, we demonstrated how the context-specific CEG is a compelling graphical tool for analysing system failure data. This happens not only because of its ability to represent structural asymmetries but also its flexibility in being able to perform the necessary analyses in a straightforward way even in the presence of censored data that are informedly missing; causal analyses can be performed through simple MAP structural learning algorithms. We developed bespoke causal algebras for the routine intervention and extended the back-door theorems for identifying its causal effects on the MCEG. The results from our designed experiments confirm the usefulness of these bespoke causal algebras in structural learning to improve the predictions needed for system reliability.

One concern of the study is that the model classes containing the best explanation can become huge when the systems are very large. However, the established methodology allows us to scale up the search space for more complex models with up to 20 variables [32]. Furthermore, these challenges associated with scalability are generic ones and are currently being actively researched. Each new development can be simply translated into causal analyses of reliability systems using the technologies we described above.

Author Contributions: Development of the methodology behind the use of CEGs for modeling routine maintenance regimes was led by X.Y. with contributions by J.Q.S.; software and data analysis, X.Y.; presentation of the material led by X.Y. with contributions from J.Q.S. Both authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by Engineering and Physical Sciences Research Council (EPSRC) with grant number EP/L016710/1 and the statistics department of the University of Warwick. Professor Jim Q. Smith is supported by the Alan Turing Institute and EPSRC with grant number EP/K039628/1.

Data Availability Statement: The data used to support the findings of this study are available from the corresponding author upon request.

Conflicts of Interest: The authors declare no conflict of interest.
