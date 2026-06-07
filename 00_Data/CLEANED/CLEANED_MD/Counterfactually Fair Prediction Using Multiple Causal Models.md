# Counterfactually Fair Prediction Using Multiple Causal Models 

Fabio Massimo Zennaro ${ }^{[0000-0003-0195-8301]}$ and Magdalena<br>Ivanovska ${ }^{[0000-0002-3916-3486]}$<br>Department of Informatics, University of Oslo, PO Box 1080 Blindern, 0316 Oslo, Norway<br>fabiomz@ifi.uio.no<br>magdalei@ifi.uio.no


#### Abstract

In this paper we study the problem of making predictions using multiple structural casual models defined by different agents, under the constraint that the prediction satisfies the criterion of counterfactual fairness. Relying on the frameworks of causality, fairness and opinion pooling, we build upon and extend previous work focusing on the qualitative aggregation of causal Bayesian networks and causal models. In order to complement previous qualitative results, we devise a method based on Monte Carlo simulations. This method enables a decision-maker to aggregate the outputs of the causal models provided by different experts while guaranteeing the counterfactual fairness of the result. We demonstrate our approach on a simple, yet illustrative, toy case study.


Keywords: Causality $\cdot$ Structural Causal Networks $\cdot$ Fairness $\cdot$ Counterfactual Fairness $\cdot$ Opinion Pooling $\cdot$ Judgement Aggregation $\cdot$ Monte Carlo Sampling

## 1 Introduction

In this paper we analyze the problem of integrating together the information provided in the form of multiple, potentially-unfair, predictive structural causal models in order to generate predictions that are counterfactually fair.

This work is rooted in two main fields of research: causality and fairness. Causality deals with the definition and the study of causal relationships; structural causal models, in particular, are versatile and theoretically-grounded models that allow us to express causal relations and to study these relationships via interventions and counterfactual reasoning [9]. Fairness is a research topic interested in evaluating if and how prediction systems deployed in sensitive scenarios may be guaranteed to support fair decisions; counterfactual fairness, in particular, is a concept of fairness developed in relation to causal models [7]. The use of causal models in societally-sensitive contexts has been advocated by several researchers on the ground that the additional structure of these models and the possibility of evaluating the effect of interventions would allow for deeper understanding and control in critical situations [2].

So far, little research has addressed the problem of aggregating multiple causal models. With no reference to fairness, 3] studied a method to aggregate causal Bayesian networks, while [1] introduced a notion of compatibility to analyze under which conditions causal models may be combined. Taking fairness into account, 11] proposed to tackle the problem of integrating multiple causal models as an optimization problem under the constraint of an $\epsilon$-relaxation of fairness.

In this paper we offer a complete solution for the problem of generating counterfactually-fair predictions given a set of causal models. Differently from [3], we focus our study on structural causal models instead of causal Bayesian networks, as the latter ones can encode causal relationships but do not support counterfactual reasoning [9; similarly to [3], though, we opt for a two-stage approach, made up of a qualitative stage, in which we work out the topology of an aggregated counterfactually-fair model, and a quantitative step, in which we use this topology to generate counterfactually-fair results out of individual causal models. The qualitative stage builds upon our previous work on this same topic in [13], and relies on the framework for judgment aggregation 6] and the work on pooling of causal Bayesian networks [3]. The quantitative stage relies on Monte Carlo simulations [8] and, again, on opinion pooling 4 .

The rest of the paper is organized as follows: Section 2 reviews basic concepts in the research areas considered; Section 3 provides the formalization of our problem and our contribution; Section 4 draws conclusions on this work and indicates future avenues of research.

# 2 Background 

This section reviews basic notions used to define the problem of generating predictions out of multiple causal models under fairness: Section 2.1 recalls the primary definitions in the study of causality; Section 2.2 discusses the notion of fairness in machine learning; Section 2.3 offers a formalization of the problem of opinion pooling.

### 2.1 Causality

Following the formalism in [9], we provide the basic definitions for working with causality.

Causal Model. A (structural) causal model $\mathcal{M}$ is a triple $(\mathcal{U}, \mathcal{V}, \mathcal{F})$ where:

- $\mathcal{U}$ is a set of exogenous variables $\left\{U_{1}, U_{2}, \ldots, U_{m}\right\}$ representing background factors that are not affected by other variables in the model;
- $\mathcal{V}$ is a set of endogenous variables $\left\{V_{1}, V_{2}, \ldots, V_{n}\right\}$ representing factors that are determined by other exogenous or endogenous variables in the model;
- $\mathcal{F}$ is a set of functions $\left\{f_{1}, f_{2}, \ldots, f_{n}\right\}$, one for each variable $V_{i}$, such that the value $v_{i}$ is determined by the structural equation:

$$
v_{i}=f_{i}\left(v_{p a_{i}}, u_{p a_{i}}\right)
$$

where $v_{p a_{i}}$ are the values assumed by the variables in the set $\mathcal{V}_{p a_{i}} \subseteq \mathcal{V} \backslash\left\{V_{i}\right\}$ and $u_{p a_{i}}$ are the values assumed by the variables in the set $\mathcal{U}_{p a_{i}} \subseteq \mathcal{U}$; that is, for each endogenous variable, there is a set of (parent) endogenous and a set of (parent) exogenous variables that determine its value through the corresponding structural equations.

Causal Diagram. The causal diagram $\mathcal{G}(\mathcal{M})$ associated with the causal model $\mathcal{M}$ is the directed graph $(\mathrm{V}, \mathrm{E})$ where:

- V is the set of vertices representing the variables $\mathcal{U} \cup \mathcal{V}$ in $\mathcal{M}$;
- E is the set of edges determined by the structural equations in $\mathcal{M}$; edges are coming to each endogenous node $V_{i}$ from each of its parent nodes $\mathcal{V}_{p a_{i}} \cup \mathcal{U}_{p a_{i}}$; we denote $V_{j} \rightarrow V_{i}$ the edge going from $V_{j}$ to $V_{i}$.

Assuming the acyclicity of causality, we will take that a causal model $\mathcal{M}$ entails an acyclic causal diagram $\mathcal{G}(\mathcal{M})$ represented as a directed acyclic graph (DAG).

Context. Given a causal model $\mathcal{M}=(\mathcal{U}, \mathcal{V}, \mathcal{F})$, we define a context $\vec{u}=$ $\left(u_{1}, u_{2}, \ldots, u_{m}\right)$ as a specific instantiation of the exogenous variables, $U_{1}=$ $u_{1}, U_{2}=u_{2}, \ldots, U_{m}=u_{m}$. Given an endogenous variable $V_{i}$, we will use the shorthand notation $V_{i}(\vec{u})$ to denote the value of the variable $V_{i}$ under the context $\vec{u}$. This value is obtained by propagating the context $\vec{u}$ through the causal diagram according to the structural equations.

Intervention. Given a causal model $\mathcal{M}=(\mathcal{U}, \mathcal{V}, \mathcal{F})$, we define intervention $d o\left(V_{i}=\bar{v}\right)$ as the substitution of the structural equation $v_{i}=f_{i}\left(v_{p a_{i}}, u_{p a_{i}}\right)$ in the model $\mathcal{M}$ with the equation $v_{i}=\bar{v}$. Given two endogenous variables $X$ and $Y$, we will use the shorthand notation $Y_{X \leftarrow x}$ to denote the value of the variable $Y$ under the intervention $d o(X=x)$.
Notice that, from the point of view of the causal diagram, performing the intervention $d o(X=x)$ is equivalent to setting the value of the variable $X$ to $x$ and removing all the incoming edges $\cdot \rightarrow X$ in $X$.

Counterfactual. Given a causal model $\mathcal{M}=(\mathcal{U}, \mathcal{V}, \mathcal{F})$, the context $\vec{u}$, two endogenous variables $X$ and $Y$, and the intervention $d o(X=x)$, a counterfactual is the value of the expression $Y_{X \leftarrow x}(\vec{u})$.
Note that, under the given context $\vec{u}$, the variable $Y$ takes the value $Y(\vec{u})$. Instead, the counterfactual $Y_{X \leftarrow x}(\vec{u})$ represents the value that $Y$ would have taken in the context $\vec{u}$ had the value of $X$ been $x$.

Probabilistic Causal Model. A probabilistic causal model $\mathcal{M}$ is a tuple $(\mathcal{U}, \mathcal{V}, \mathcal{F}, P(U))$ where:

- $(\mathcal{U}, \mathcal{V}, \mathcal{F})$ is a causal model;
- $P(U)$ is a probability distribution over the exogenous variables. The probability distribution $P(U)$, combined with the dependence of each endogenous variable $V_{i}$ on the exogenous variables, as specified in the structural equation for $v_{i}$, allows us to define a probability distribution $P(V)$ over the endogenous variables as: $P(V=v)=\sum_{\{\vec{u} \mid V=v\}} P(U=\vec{u})$.

Notice that we overload the notation $\mathcal{M}$ to denote both (generic) causal models and probabilistic causal models; the context will allow the reader to distinguish between them.

# 2.2 Fairness 

Following the work of [7], we review the topic of fairness, with a particular emphasis on counterfactual fairness for predictive models.

Fairness and Learned Models. Black-box machine learning systems deployed in sensitive contexts (e.g.: police enforcement or educational grants allocation) and trained on historical real-world data have the potential of perpetuating, or even introducing [7], socially or morally unacceptable discriminatory biases (for a survey, see, for instance, 14]). The study of fairness is concerned with the definition of new metrics to assess and guarantee the social fairness of a predictive decision system.

Fairness of a Predictor. A predictive model can be represented as a (potentially probabilistic) function of the form $\hat{Y}=f(Z)$, where $\hat{Y}$ is a predictor and $Z$ is a vector of covariates. An observational approach to fairness states that the set of covariates can be partitioned in a set of protected attributes $\mathcal{A}$, representing discriminatory elements of information, and a set of features $\mathcal{X}$, carrying no sensitive information. The predictive model can then be redefined as $\hat{Y}=f(A, X)$ and the fairness problem is expressed as the problem of learning a predictor $\hat{Y}$ that does not discriminate with respect to the protected attributes $\mathcal{A}$. Given the complexities of social reality and disagreement over what constitutes a fair policy, different measures of fairness may be adopted to rule out discrimination (e.g.: counterfactual fairness or fairness through unawareness); for a more thorough review of different types of fairness and their limitations, see [5] and [7].

Fairness Over Causal Models. Given a probabilistic causal model $(\mathcal{U}, \mathcal{V}, \mathcal{F}, P(U))$ fairness may be evaluated following an observational approach. Let us take $\hat{Y}$ to be an endogenous variable whose structural equation provides the predictive function $f_{\hat{Y}}$; let us also partition the remaining variables $\mathcal{U} \cup \mathcal{V} \backslash\{\hat{Y}\}$ into a set of protected attributes $\mathcal{A}$ and a set of features $\mathcal{X}$. Then we can evaluate the fairness of the predictor $\hat{Y}$ with respect to the discriminatory attributes $\mathcal{A}$.

Counterfactual Fairness. Given a probabilistic causal model $\mathcal{M}=(\mathcal{U}, \mathcal{V}, \mathcal{F}, P(U))$, a predictor $\hat{Y}$, and a partition of the variables $\mathcal{U} \cup \mathcal{V} \backslash\{\hat{Y}\}$ into $(\mathcal{A}, \mathcal{X})$, the predictor $f_{\hat{Y}}$ is counterfactually fair if, for every context $\vec{u}$,

$$
P\left(\hat{Y}_{A \leftarrow a}(\vec{u}) \mid X=x, A=a\right)=P\left(\hat{Y}_{A \leftarrow a^{\prime}}(\vec{u}) \mid X=x, A=a\right)
$$

for all values $y$ of the predictor, for all values $a^{\prime}$ in the domain of $A$, and for all $x$ in the domain of $X[7]$.
In other words, the predictor $\hat{Y}$ is counterfactually fair if, under all the contexts,

the prediction on $\hat{Y}$ given the observation of the protected attributes $A=a$ and the features $X=x$ would not change if we were to intervene $d o\left(A=a^{\prime}\right)$ to force the value of the protected attributes $A$ to $a^{\prime}$, for all the possible values that the protected attributes can assume.
Denoting $\operatorname{Desc}_{\mathcal{M}}(\mathcal{A})$ the descendants of the nodes in $\mathcal{A}$ in the model $\mathcal{M}$, an immediate property follows from the definition of counterfactual fairness:

Lemma 1. (Lemma 1 in [7]) Given a probabilistic causal model $(\mathcal{U}, \mathcal{V}, \mathcal{F}, P(U))$, a predictor $\hat{Y}$ and a partition of the variables into $(\mathcal{A}, \mathcal{X})$, the predictor $\hat{Y}$ is counterfactually fair if $f_{\hat{Y}}$ is a function depending only on variables that are not in $\operatorname{Desc}_{\mathcal{M}}(\mathcal{A})$.

# 2.3 Opinion Pooling 

Following the study of [4], we introduce the framework for opinion pooling.
Opinion Pooling. Assume there are $N$ experts, each one expressing his/her opinion $o_{i}, 1 \leq i \leq N$. The problem of pooling (or aggregating) the opinions $o_{i}$ consists in finding a single pooled opinion $o^{*}$ representing the collective opinion that best represents the individual opinions in the given context.

Probabilistic Opinion Pooling. Given opinions in the form of probability distributions $p_{i}(x), 1 \leq i \leq N$, defined over the same domain, probabilistic opinion pooling is concerned with finding a single pooled probability distribution $p^{*}(x)=F\left(p_{1}, \ldots, p_{n}\right)(x)$, where $F$ is a functional mapping a tuple of pdfs to a single probability distribution 4 .
Now, given a set of probabilistic opinions $p_{i}(x)$, different functionals $F$ may be chosen to perform opinion pooling, either using a principled approach such as an axiomatic approach based on the definition of a set of desired properties [4], or using standard statistical operators, such as arithmetic averaging or geometric averaging.

Judgment Aggregation. Given opinions in the form of a set of Boolean functions $j_{i}(x)$, judgment aggregation is concerned with finding a single Boolean function $j^{*}(x)=F\left(j_{1}, \ldots, j_{n}\right)(x)$, where $F$ is a functional mapping a tuple of Boolean functions to a single Boolean function [6].
As in the case of probabilistic opinion pooling, given a set of judgments $j_{i}(x)$, different functions $F$ may be chosen to perform judgment aggregation, such as majority voting or intersection [3].

Aggregation of Causal Bayesian Networks. Given opinions expressed in the form of causal Bayesian networks ${ }^{1}(\mathrm{CBN}) \mathcal{B}_{i}$, aggregation of CBNs is concerned with

[^0]
[^0]:    ${ }^{1}$ A Bayesian network (BN) 10 is a structured representations of the joint probability distribution of a set of variables in the form of a directed acyclic graph with associated conditional probability distributions. A causal BN is a BN where all the edges represent causal relations between variables.

defining a single pooled CBN $\mathcal{B}^{*}$.
A seminal study in aggregating CBNs is offered by 3]. They suggest a two-stage approach to the problem of aggregating $N$ causal Bayesian networks $\mathcal{B}_{i}$. In the first qualitative stage, they determine the graph of the pooled CBN reducing the problem to a judgment aggregation over the edges in the individual CBNs; namely, for every two variables $X$ and $Y$, the presence of an edge from node $X$ to node $Y$ in the model $\mathcal{B}_{i}$ is represented as the $i$-th expert casting the judgment $j_{i}(X \rightarrow Y)=1$, and the absence of it as the judgment $j_{i}(X \rightarrow Y)=0$; the problem of defining the pooled graph is then reduced to a judgment aggregation problem over the judgments $j_{i}()$. In the second quantitative step, they derive the conditional probability distributions for the pooled graph applying probabilistic opinion pooling to the corresponding conditional probability distributions in the individual CBNs. A critical result in the study of [3] is the translation of the classical impossibility theorem from judgment aggregation [6] into an impossibility theorem for the qualitative aggregation of CBNs:

Theorem 1. (Theorem 1 in [3]) Given a set of CBNs defined over at least three variables, there is no judgment aggregation rule $f$ that satisfies all the following properties:

- Universal Domain: the domain of $f$ includes all logically possible acyclic causal relations;
- Acyclicity: the pooled graph produced by $f$ is guaranteed to be acyclic over the set of nodes;
- Unbiasedness: given two variables $X$ and $Y$, the causal dependence of $X$ on $Y$ in the pooled graph rests only on whether $X$ is causally dependent on $Y$ in the individual graphs, and the aggregation rule is not biased towards a positive or negative outcome;
- Non-dictatorship: the pooled graph produced by $f$ is not trivially equal to the graph provided by one of the experts.

As a consequence of this theorem, no unique aggregation rule satisfying the above properties can be chosen for the pooling of causal judgments in the first step of the two-stage approach. A relaxation of these properties must be decided depending on the scenario at hand.

# 3 Aggregation of Causal Models Under Fairness 

This section analyzes how probabilistic causal models can be aggregated under fairness: Section 3.1 provides a formalization of our problem; Section 3.2 discusses how to define the topology of a counterfactually-fair causal graph by pooling together the graphs of different probabilistic structural causal models; Section 3.3 explains how to evaluate a counterfactually-fair prediction out of the individual models using the pooled graph; finally, Section 3.4 offers an illustration of the use of our method on a toy case study.

# 3.1 Problem Formalization 

Let us consider the case in which $N$ experts are required to provide a probabilistic causal model $\mathcal{M}_{i}=\left(\mathcal{U}, \mathcal{V}, \mathcal{F}_{i}, P_{i}(U)\right)$ representing a potentially socially-sensitive scenario. For simplicity, we assume that the experts are provided with a fixed set of variables $(\mathcal{U}, \mathcal{V})$. The task of the experts can be summarized in two modeling phases: (i) a qualitative phase, in which they define the causal topology of the graph $\mathcal{G}\left(\mathcal{M}_{i}\right)$ (which variables are causally influencing which other variables); and, (ii) a quantitative phase, specifying the probability distribution functions $P_{i}(U)$ (how the stochastic behavior of the exogenous variables is modeled) and the structural equations $\mathcal{F}_{i}$ (how each endogenous variable is causally influenced by its parents variables).

Critically, we are not requesting the experts to provide fair models. Individual experts may not be aware of specific discrimination issues, they may have different understandings of fairness or, simply, they may not have the technical competence to formally evaluate or guarantee fairness. The task of defining which form of fairness is relevant, and enforcing it, is up to the final decision-maker only.

The (potentially unfair) models $\mathcal{M}_{i}$ defined by the experts are then provided to a decision-maker, who wants to exploit them to compute a single counterfactuallyfair predictive output $\hat{Y}^{*}$. We assume the decision-maker to be knowledgeable of fairness implications and to be responsible for partitioning the exogenous and endogenous variables $\mathcal{U} \cup \mathcal{V}$ into sensitive attributes $\mathcal{A}$ and non-sensitive attributes $\mathcal{X}$.

In summary, our problem may be expressed as follows: given $N$ (potentially counterfactually-unfair) probabilistic causal models $\mathcal{M}_{i}$ defined on the same variables $(\mathcal{U}, \mathcal{V})$, and a partition of the variables into $(\mathcal{A}, \mathcal{X})$, can we define a pooling algorithm that allows us to construct an aggregated counterfactually-fair causal model $\mathcal{M}^{*}=f\left(\mathcal{M}_{i}\right)$ and compute a counterfactually-fair predictive output $\hat{Y}^{*}$ ?

Mirroring the modeling approach of the experts, we propose to solve this problem by adopting a two-stage approach. We reduce the task of the final decision-maker to the two following phases: (i) a qualitative phase, in which we compute the topology of a counterfactually-fair pooled graph $\mathcal{G}\left(\mathcal{M}^{*}\right)$ (which nodes and causal links from the individual models can be retained under a requirement of counterfactual fairness); and, (ii) a quantitative phase, in which we provide a method to evaluate a probability distribution over the final predictor $\hat{Y}^{*}$ (how is the final counterfactually-fair predictor computed).

### 3.2 Qualitative Aggregation over the Graph

In the qualitative phase of our approach, we consider the different expert models $\mathcal{M}_{i}$ and we focus on the problem of defining the topology of an aggregated graph $\mathcal{G}\left(\mathcal{M}^{*}\right)$ that guarantees counterfactual fairness.

We tackle this challenge following the solution proposed in [3] to perform a qualitative aggregation of causal Bayesian networks (see Section 2.3): in each causal model $\mathcal{M}_{i}$, we convert each edge in a binary judgment and we then

perform judgment aggregation according to a chosen aggregation rule JARule (). However, this solution presents two shortcomings: (i) it does not guarantee that the predictor $\hat{Y}^{*}$ in the aggregated probabilistic causal model $\mathcal{M}^{*}$ will be counterfactually fair; and (ii) because of Theorem 1, we cannot apply this procedure without first choosing one of the properties in the theorem statement to sacrifice. We solve the first problem by relying and enforcing the condition specified in Lemma 1; practically, we introduce in our algorithm a removal step, in which we remove all the protected attributes and their descendants from the aggregated model $\mathcal{M}^{*}$. This procedure satisfies by construction the condition in Lemma 1, and thus guarantees counterfactual fairness. We address the second problem by arguing that the structure of the causal graph immediately suggests the possibility of dropping the property of unbiasedness, which requires that the presence of an edge in the pooled graph depends only on the presence of the same edge in each individual graph; we can relax this property, by making the presence of an edge in the final graph dependent also on an ordering of the edges. In our specific case, we can easily introduce an ordering of the edges with respect to the predictor $\hat{Y}$, as a starting point. The ordering produced in this way may not be total, and we may still have to introduce another rule to break potential ties (e.g., random selection or an alphabetical criterion). We formalize this procedure in an additional algorithmic step, pooling step, in which we order edges in relation to their distance from the predictor and then we perform judgment aggregation using the rule JARule () so that, if the edge is selected for insertion in the pooled model $\mathcal{G}\left(\mathcal{M}^{*}\right)$, then it is added as long as acyclicity is not violated 3 .

The two algorithmic steps defined above may be interchangeably combined. This gives rise to two alternative algorithms: a removal-pooling algorithm (Algorithm 1), and a pooling-removal algorithm (Algorithm 2). We provide the pseudo code for the two functions, Removal() and Pooling(), in Algorithm A.1 and A. 2 in the appendix; also, for a detailed description and analysis of these functions and their outputs we refer the reader to [13].

At the end, both algorithms return the skeleton of a pooled causal model $\mathcal{M}^{*}$ that is guaranteed to be counterfactually fair. However, the result, so far, contains only a qualitative description of the causal model: we determined the topology of the graph $\mathcal{G}\left(\mathcal{M}^{*}\right)$, but the structural equations of the pooled causal model $\mathcal{M}^{*}$ are left undefined.

```
Algorithm 1 Removal-Pooling Algorithm
    Input: \(N\) graph models \(\mathcal{G}\left(\mathcal{M}_{i}\right)\) over the variables \(\{\mathcal{U}, \mathcal{V}\}\), a predictor \(\hat{Y} \in \mathcal{V}\), a
        partitioning of the variables \(\{\mathcal{U}, \mathcal{V}\} \backslash\{\hat{Y}\}\) into protected attributes \(\mathcal{A}\) and \(\mathcal{X}\), a
        judgment aggregation rule JARule ()
    2:
    \(3:\left\{\mathcal{M}_{i}^{\prime}\right\}_{i=1}^{N}=\operatorname{Removal}\left(\left\{\mathcal{M}_{i}\right\}_{i=1}^{N}, \mathcal{A}\right)\)
    \(4: \mathcal{M}^{*}=\operatorname{Pooling}\left(\left\{\mathcal{M}_{i}^{\prime}\right\}_{i=1}^{N}\right.\), JARule ())
    5: \(\operatorname{return} \mathcal{M}^{*}\)
```

```
Algorithm 2 Pooling-Removal Algorithm
    Input: \(N\) graph models \(\mathcal{G}\left(\mathcal{M}_{i}\right)\) over the variables \(\{\mathcal{U}, \mathcal{V}\}\), a predictor \(\hat{Y} \in \mathcal{V}\), a
partitioning of the variables \(\{\mathcal{U}, \mathcal{V}\} \backslash\{\hat{Y}\}\) into protected attributes \(\mathcal{A}\) and \(\mathcal{X}\), a
judgment aggregation rule JARule()
\(\mathcal{M}^{\prime}=\) Pooling \(\left(\left\{\mathcal{M}_{i}\right\}_{i=1}^{N}\right.\), JARule ( \(\left.)\right)\)
\(\mathcal{M}^{*}=\operatorname{Removal}\left(\mathcal{M}^{\prime}, \mathcal{A}\right)\)
    return \(\mathcal{M}^{*}\)
```


# 3.3 Quantitative Aggregation over the Distribution of the Predictor 

In the quantitative phase of our approach, we study how we can use the topology of the pooled and counterfactually-fair causal graph $\mathcal{G}\left(\mathcal{M}^{*}\right)$ that we have generated in the first step to produce quantitative and counterfactually-fair outputs.

After the phase of qualitative aggregation, the individual models provided by the experts $\mathcal{M}_{i}$ have been aggregated only with respect to their nodes and edges; the pooled graph $\mathcal{M}^{*}$ encodes the topology of a counterfactually-fair causal model, but it lacks the definition of probability distributions over the exogenous nodes and structural equations over the endogenous nodes in order to be complete and usable.

Defining the probability distributions and the structural equations in the aggregated model $\mathcal{M}^{*}$ by pooling together individual functions in each expert model $\mathcal{M}_{i}$ is a particularly challenging task: different experts may provide substantially different functions, functions may be defined on different domains (since the same node may have different incoming edges in different expert graphs), and domains may have been changed in the aggregated model (since nodes may have been dropped in order to guarantee counterfactual fairness). Therefore, instead of finding an explicit form for the probability distributions and the structural equations in the aggregated model $\mathcal{M}^{*}$, we suggest to compute the distribution of the predictor $\hat{Y}_{i}$ in each expert model $\mathcal{M}_{i}$ while integrating out all the components that do not belong to the counterfactually-fair graph $\mathcal{G}\left(\mathcal{M}^{*}\right)$, and finally aggregate them to obtain the final counterfactually-fair predictor $\hat{Y}^{*}$.

More formally, let $\mathcal{Z} \subseteq \mathcal{U} \cup \mathcal{V}$ be the set of fair features corresponding to nodes that are present in $\mathcal{G}\left(\mathcal{M}^{*}\right)$, and let $\bar{Z} \subseteq \mathcal{U} \cup \mathcal{V}$ be the set of unfair features corresponding to nodes that are not present in $\mathcal{G}\left(\mathcal{M}^{*}\right)$. Now, if we are given an instance of fair features $Z=z$, we can compute the probability distribution of the predictor $\hat{Y}_{i}$ in each model $\mathcal{M}_{i}$ by integrating out the unfair features:

$$
P\left(\hat{Y}_{i} \mid Z=z\right)=\int P\left(\hat{Y}_{i} \mid Z=z, \bar{Z}\right) d \bar{Z}
$$

In other words, we use the aggregated model $\mathcal{G}\left(\mathcal{M}^{*}\right)$ to identify in each expert model a countefactually fair sub-graph and to integrate out the contributions of the rest of the graph. Practically, this operation of integration and estimation of the distribution of $P\left(\hat{Y}_{i} \mid Z=z\right)$ can be efficiently carried out using Monte Carlo sampling [8].

The final result will then consist of a set of $N$ individual pdfs $P\left(\bar{Y}_{i} \mid Z=z\right)$. In order to take a decision, these pdfs can be simply merged together using simple statistical operators (e.g.: by taking the mean of the expected values) or relying on standard opinion pooling operators [4].

# 3.4 Illustration 

Here we give a simple illustration of the problem of causal model aggregation under counterfactual fairness, which we recover from [13].

Setup. In this example, we imagine that the head of a Computer Science department asked two professors, Alice and Bob, to design a predictive system to manage PhD selections. In particular, we imagine that Bob and Alice were required to define a causal model over the endogenous variables age (Age), gender (Gnd), MSc university department (Dpt), MSc final mark (Mrk), experience in the job market (Job), quality of the cover letter (Cvr), the relative exogenous variables (U.) and a predictor $(\hat{Y})$.

The graphs of the two models provided by Alice $\mathcal{G}\left(\mathcal{M}_{A}\right)$ and Bob $\mathcal{G}\left(\mathcal{M}_{B}\right)$ are given in Figures 1 and 2, respectively.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Graph $\mathcal{G}\left(\mathcal{M}_{A}\right)$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Graph $\mathcal{G}\left(\mathcal{M}_{B}\right)$.

Moreover, Alice and Bob came up with the following probability distributions over the exogenous nodes $\mathcal{U}$ :

$$
\begin{aligned}
U_{a g e, A} \sim \operatorname{Poisson}(\lambda=3) & U_{a g e, B} \sim \operatorname{Poisson}(\lambda=4) \\
U_{j o b, A} \sim \operatorname{Bernoulli}(p=0.3) & U_{j o b, B} \sim \operatorname{Bernoulli}(p=0.2) \\
U_{g n d, A} \sim \operatorname{Bernoulli}(p=0.5) & U_{g n d, B} \sim \operatorname{Bernoulli}(p=0.5) \\
U_{d p t, A} \sim \text { Categorical}([0.7,0.2,0.1]) & U_{d p t, B} \sim \text { Categorical }([0.7,0.15,0.1,0.05]) \\
U_{m r k, A} \sim \operatorname{Beta}(\alpha=2, \beta=2) & U_{m r k, B} \sim \operatorname{Beta}(\alpha=2, \beta=2) \\
U_{c v r, A} \sim \operatorname{Beta}(\alpha=2, \beta=5) & U_{c v r, B} \sim \operatorname{Beta}(\alpha=2, \beta=5)
\end{aligned}
$$

and they defined the structural equations for the endogenous nodes $\mathcal{V}$ :

$$
\begin{aligned}
V_{a g e_{-} A} & =20+U_{a g e_{-} A} \\
V_{g n d_{-} A} & =U_{g n d_{-} A} \\
V_{j o b_{-} A} & =U_{j o b_{-} A}+\frac{V_{g n d_{-} A}}{2}+\frac{V_{a g e_{-} A}}{100} \\
V_{d p t_{-} A} & =\text { if }\left(V_{g n d_{-} A}=1\right) \text { then } 0 \text { else } \frac{U_{d p t_{-} A}}{10} \\
V_{m r k_{-} A} & =\text { if }\left(V_{d p t_{-} A}=0\right) \text { then } U_{m r k_{-} A}+0.1 \text { else } U_{m r k_{-} A}-0.1 \\
V_{c v r_{-} A} & =U_{c v r_{-} A}+0.2 \\
\hat{Y}_{A} & =V_{j o b_{-} A}+V_{d p t_{-} A}+V_{m r k_{-} A}+V_{c v r_{-} A} \\
V_{a g e_{-} B} & =19+U_{a g e_{-} B} \\
V_{g n d_{-} B} & =U_{g n d_{-} B} \\
V_{j o b_{-} B} & =U_{j o b_{-} B}+\frac{V_{a g e_{-} B}}{100}+\left[\text { if }\left(V_{g n d_{-} B}=1\right) \text { then } 0.5 \text { else } 0\right] \\
V_{d p t_{-} B} & =\frac{U_{d p t_{-} B}}{10} \\
V_{m r k_{-} B} & =\text { if }\left(V_{d p t_{-}B}=0\right) \text { then } U_{m r k_{-}B}+0.1 \text { else } U_{m r k_{-}B} \\
V_{c v r_{-} B} & =U_{c v r_{-} B}+0.1 \\
\hat{Y}_{A} & =\frac{V_{j o b_{-} A}}{100}+V_{j o b_{-} A}+V_{d p t_{-} A}+V_{m r k_{-} A}+V_{c v r_{-} A}
\end{aligned}
$$

Notice that these probability distributions and structural equations are pure examples, and do not have any deep meaningful relation with the scenario at hand; they were chosen mainly to illustrate the use of a variety of distributions and functions, and to output as a predictor $\hat{Y}$ a score that can be used for decision-making. In reality, such functions would be determined via machine learning methods or carefully defined by a modeler.

Notice that the models and the structural equations were defined by Alice and Bob with no explicit concern about any form of fairness. Now, however, the head of the department wants to aggregate these models in a way that guarantees counterfactual fairness with respect to the gender of the PhD candidate.

Qualitative Aggregation. As a first step, the head of the department assumes all the exogenous variables to be non-sensitive and partitions the endogenous ones into protected attributes $\mathcal{A}=\{\mathrm{Gnd}\}$ and features $\mathcal{X}=\{\mathrm{Age}, \mathrm{Dpt}, \mathrm{Mrk}, \mathrm{Job}, \mathrm{Cvr}\}$, and then chooses as a judgment aggregation rule JARule () the strict majority rule.

She then decides to apply the pooling-removal algorithm to the models $\mathcal{M}_{A}$ and $\mathcal{M}_{B}$. A detailed explanation of the application of this algorithm is available in [13]. The resulting pooled counterfactually-fair model $\mathcal{M}^{*}$ is illustrated in Figure 3.

Quantitative Aggregation. At this point, the head of the department can use the individual expert models $\mathcal{M}_{A}$ and $\mathcal{M}_{B}$, and the aggregated counterfactually-fair model $\mathcal{G}\left(\mathcal{M}^{*}\right)$ to compute predictive scores for the PhD applicants.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Graph of the pooled counterfactually-fair model $\mathcal{G}\left(\mathcal{M}^{*}\right)$ after applying the pooling-removal algorithm.

Suppose, for instance, that the following candidates were to submit their application:

App $_{1}=\{$ Age $=22 ;$ Gnd $=\mathrm{F} ;$ Dpt $=$ Computer Science; Mrk $=0.8 ;$ Job $=$ True; Cvr $=0.4\}$
App $_{2}=\{$ Age $=22 ;$ Gnd $=\mathrm{M} ;$ Dpt $=$ Computer Science; Mrk $=0.8 ;$ Job $=$ True; Cvr $=0.4\}$
From a formal point of view, we may imagine the second candidate as the result of the intervention $d o(\mathrm{Gnd}=M)$ on the first candidate, thus forcing the gender to male.

Now, for the sake of illustration, we implemented the models and the candidates using Edward [12], a Python library for probabilistic modeling, and we made the code available online ${ }^{2}$. Whenever using Monte Carlo sampling, we collected $10^{5}$ samples.

The models provided by Alice and Bob obviously define two different predictors $\hat{Y}_{A}$ and $\hat{Y}_{B}$ with two dissimilar probability distributions (see Figure B. 1 in the appendix for an estimation of these pdfs). If the head of the department were to feed the data about the candidates to the two models, she would receive different and unfair results:

$$
\begin{array}{ll}
\hat{Y}_{A}\left(\mathrm{App}_{1}\right)=4.720 & \hat{Y}_{B}\left(\mathrm{App}_{1}\right)=3.340 \\
\hat{Y}_{A}\left(\mathrm{App}_{2}\right)=2.720 & \hat{Y}_{B}\left(\mathrm{App}_{2}\right)=2.840
\end{array}
$$

Indeed, these results show both a legitimate disagreement between Alice and Bob on how they score individual candidates, but they also show a troubling internal disagreement in that both experts assign different scores to the two applicants when the only difference between them is their gender. Since the head of the department considers gender a protected attribute, this result is deemed unfair. More formally, if the second candidate were to be seen as an intervention we would have:

$$
P\left(\hat{Y}_{\mathrm{Gnd} \leftarrow F}(\vec{u}) \mid X=x, A=a\right) \neq P\left(\hat{Y}_{\mathrm{Gnd} \leftarrow M}(\vec{u}) \mid X=x, A=a\right)
$$

thus denying counterfactual fairness.

[^0]
[^0]:    ${ }^{2}$ https://github.com/FMZennaro/Fair-Pooling-Causal-Models

To tackle the problem, the head of the department decides to evaluate the predictive score for the candidates by computing the distribution of the predictor $\hat{Y}_{i}$ given only the fair features $\mathcal{Z}$ from the pooled counterfactually-fair model $\mathcal{M}^{*}$ :

$$
\begin{aligned}
& P\left(\hat{Y}_{A} \mid Z=z\right)=\int_{\text {Age }, \text { Gnd,Job }} P\left(\hat{Y}_{A} \mid D p t=\mathrm{CS}, \operatorname{Mrk}=0.8, \text { Cvr }=0.4\right) \\
& P\left(\hat{Y}_{B} \mid Z=z\right)=\int_{\text {Age }, \text { Gnd,Job }} P\left(\hat{Y}_{B} \mid D p t=\mathrm{CS}, \operatorname{Mrk}=0.8, \text { Cvr }=0.4\right)
\end{aligned}
$$

This step does not provide a scalar output as in the previous evaluation, but it defines two probability distributions $P\left(\hat{Y}_{A} \mid Z=z\right)$ and $P\left(\hat{Y}_{B} \mid Z=z\right)$ (see Figure B. 2 in the appendix for an estimation of these pdfs). These two pdfs can now be pooled together for final decision making. After deciding to compute the average of the expected value of the pdfs ${ }^{3}$, the head of the department obtains the following fair results:

$$
\begin{array}{ll}
E\left[P\left(\hat{Y}_{A}\left(\operatorname{App}_{1}\right) \mid Z\right)\right]=3.022 & E\left[P\left(\hat{Y}_{B}\left(\operatorname{App}_{1}\right) \mid Z\right)\right]=2.312 \\
E\left[P\left(\hat{Y}_{A}\left(\operatorname{App}_{2}\right) \mid Z\right)\right]=3.030 & E\left[P\left(\hat{Y}_{B}\left(\operatorname{App}_{2}\right) \mid Z\right)\right]=2.313
\end{array}
$$

These results are more comforting in that, while they still allow room for disagreement between Alice and Bob over the evaluation of individual candidates, they guarantee that the two applicants, who differ only on a protected attribute, receive identical predictive scores (within the numerical precision of a Monte Carlo simulation ${ }^{4}$ ). Again, formally, if we were to see the second candidate as an intervention on the first, we would have:

$$
P\left(\hat{Y}_{\mathrm{Gnd} \leftarrow F}(\vec{u}) \mid X=x, A=a\right)=P\left(\hat{Y}_{\mathrm{Gnd} \leftarrow M}(\vec{u}) \mid X=x, A=a\right)
$$

thus satisfying counterfactual fairness. Therefore, these counterfactually-fair scores can now be safely averaged into a final fair predictor $\hat{Y}^{*}$ by the head of the department and used for decision-making.

# 4 Conclusion 

This paper offers a complete approach to the problem of computing aggregated predictive outcomes from a collection of causal models while respecting a principle of counterfactual fairness. Our solution comprises two phases: (i) a qualitative step, in which we use judgment aggregation to determine a counterfactuallyfair pooled model; and, (ii) a quantitative step, in which we use Monte Carlo

[^0]
[^0]:    ${ }^{3}$ Notice that the decision of considering just the expected value of the pdfs may not be ideal in this case, given the multimodality of these pdfs, as shown in Figure B. 2 in the appendix.
    ${ }^{4}$ This precision can be increased by incrementing the number of Monte Carlo samples collected.

sampling to evaluate the predictive output of each model by integrating out unfair components, and then we perform opinion pooling to aggregate these outputs. The entire approach was illustrated on the toy-case of PhD admissions, showing that it does indeed provide counterfactually-fair results.

However, this work represents just a first attempt at solving the problem of aggregating multiple causal models in order to provide counterfactually-fair predictions. Some avenues for future development that we are investigating include:

- our method presupposes causal models defined over the same set of exogenous and endogenous variables; however, our solution is quite flexible and, with little formal work, it may be extended to produce fair outcomes from the aggregation of causal graphs defined on different sets of exogenous and endogenous variables;
- from a formal point of view, it may be interesting to investigate extreme cases (e.g.: scenarios in which qualitative aggregation provides no fair model), examine what are the conditions for a fair model to exist, and evaluate how these conditions may be relaxed to allow the most fair possible aggregation of causal models;
- more importantly, it may be worth to study how a purely observational approach to fairness may be integrated by a pro-active affirmative approach. In this last more realistic approach, the aim is not only to guarantee unbiased outcomes with respect to the available historical data (which may itself be biased), but purposefully and actively compensate existing bias through policies and interventions.


# Appendix A: Algorithms 

```
Algorithm A. 1 Removal Function
    Input: \(N\) graph models \(\mathcal{G}\left(\mathcal{M}_{j}\right)=\left(\mathrm{V}_{j}, \mathrm{E}_{j}\right)\), where the vertex set \(\mathrm{V}_{j}\) is defined
    over the exogenous and endogenous variables \(\mathcal{U} \cup \mathcal{V}\); a partitioning of the variables
    \(\mathcal{U} \cup \mathcal{V} \backslash\{\hat{Y}\}\) into protected attributes \(\mathcal{A}\) and \(\mathcal{X}\).
    Initialize \(\mathcal{W}_{\text {fair }}:=\mathcal{U} \cup \mathcal{V}\)
    for \(j=1\) to \(N\) do
        \(\mathcal{W}_{\neg}:=\{W \mid(W \in \mathcal{A}) \vee\left(W \in \operatorname{Desc}_{\mathcal{M}_{j}}(\mathcal{A})\right)\}\)
        \(\mathcal{W}_{\text {fair }}:=\mathcal{W}_{\text {fair }} \backslash \mathcal{W}_{\neg}\)
    end for
    for \(j=1\) to \(N\) do
        Remove from the edge set \(\mathrm{E}_{j}\) of \(\mathcal{G}\left(\mathcal{M}_{j}\right)\) all edges
        \(V_{x} \rightarrow V_{y} \mid\left(V_{x} \notin \mathcal{W}_{\text {fair }} \vee V_{y} \notin \mathcal{W}_{\text {fair }}\right)\)
    end for
    return \(\mathcal{M}_{j}\)
Algorithm A. 2 Pooling Function
    Input: \(N\) graphs models \(\mathcal{G}\left(\mathcal{M}_{j}\right)=\left(\mathrm{V}_{j}, \mathrm{E}_{j}\right)\), where the vertex set \(\mathrm{V}_{j}\) is defined
    over the exogenous and endogenous variables \(\mathcal{U} \cup \mathcal{V}\); a judgment aggregation rule
    JARule ().
    Initialize \(D\) to the length of the longest path in the models \(\mathcal{M}_{j}\)
    Initialize \(\mathcal{M}^{*}\) by setting up the graph \(\mathcal{G}\left(\mathcal{M}^{*}\right)\) in which \(\mathrm{V}^{*}=\mathcal{U} \cup \mathcal{V}\) and \(\mathrm{E}^{*}=\emptyset\)
    for \(j=1\) to \(N\) do
        Initialize the vertex set \(\mathrm{V}_{j, 0}:=\hat{Y}\)
        Initialize the edge set \(\mathrm{E}_{j, 0}:=\emptyset\)
    end for
    for \(j=1\) to \(N\) do
        for \(d=1\) to \(D\) do
            \(\mathrm{E}_{j, d}:=\left\{\left(V_{x} \rightarrow V_{y}\right) \mid\left(V_{x} \rightarrow V_{y}\right) \in \mathrm{E}_{j} \wedge\left(V_{x} \in \mathrm{~V}_{j, d-1} \vee V_{y} \in \mathrm{~V}_{j, d-1}\right)\right\}\)
            \(\mathrm{V}_{j, d}:=\left\{V_{x} \mid\left(V_{x} \rightarrow \cdot\right) \in \mathrm{E}_{j, d} \vee\left(\cdot \rightarrow V_{x}\right) \in \mathrm{E}_{j, d}\right\}\)
        end for
    end for
    for \(j=1\) to \(N\) do
        for \(d=1\) to \(D\) do
            \(\forall\left(V_{x} \rightarrow V_{y}\right) \in \mathrm{E}_{j, d}\), if \(\left(\operatorname{JARule}\left(V_{x} \rightarrow V_{y}\right)=1\right) \vee\left(\mathrm{E}^{*} \cup\left\{V_{x} \rightarrow V_{y}\right\}\right.\) is acyclic)
    then \(\mathrm{E}^{*}:=\mathrm{E}^{*} \cup\left\{V_{x} \rightarrow V_{y}\right\}\)
        end for
    end for
    return \(\mathcal{M}^{*}\)
```

# Appendix B: Figures 

![img-3.jpeg](img-3.jpeg)

Fig. B.1. Histogram and probability distribution function (computed via kernel density estimation) of $P(\hat{Y})$ in the model provided by Alice and Bob. The $x$-axis reports the domain of the outcome of the predictor $\hat{Y}$; the left $y$-axis reports the number of samples used to compute the histogram, while the right $y$-axis reports the normalized values used to compute the pdf.

![img-4.jpeg](img-4.jpeg)

Fig. B.2. Histogram and probability distribution function (computed via kernel density estimation) of $P(\hat{Y} \mid D p t=\mathrm{CS}, M r k=0.8, C v r=0.4)$ in the model provided by Alice and Bob. The $x$-axis reports the domain of the outcome of the predictor $\hat{Y}$; the left $y$-axis reports the number of samples used to compute the histogram, while the right $y$-axis reports the normalized values used to compute the pdf.