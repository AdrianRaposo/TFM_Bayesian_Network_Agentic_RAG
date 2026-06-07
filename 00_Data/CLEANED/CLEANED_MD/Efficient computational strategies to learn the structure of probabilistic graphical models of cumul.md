# Efficient computational strategies to learn the structure of probabilistic graphical models of cumulative phenomena 

Daniele Ramazzotti ${ }^{\mathrm{a}}$, Marco S. Nobile ${ }^{\mathrm{b}, \mathrm{c}}$, Marco Antoniotti ${ }^{\mathrm{b}, \mathrm{d}}$, Alex Graudenzi ${ }^{\mathrm{b}}$<br>${ }^{a}$ Dept. of Pathology, Stanford University, CA, USA<br>${ }^{b}$ Dept. of Informatics, Systems and Communication, University of Milano - Bicocca, Milan, Italy<br>${ }^{c}$ SYSBIO Centre of Systems Biology, Milan, Italy<br>${ }^{d}$ Milan Center for Neuroscience, University of Milano - Bicocca, Monza, Italy


#### Abstract

Structural learning of Bayesian Networks (BNs) is a $N P$-hard problem, which is further complicated by many theoretical issues, such as the $I$-equivalence among different structures. In this work, we focus on a specific subclass of BNs, named Suppes-Bayes Causal Networks (SBCNs), which include specific structural constraints based on Suppes' probabilistic causation to efficiently model cumulative phenomena. Here we compare the performance, via extensive simulations, of various state-of-the-art search strategies, such as local search techniques and Genetic Algorithms, as well as of distinct regularization methods. The assessment is performed on a large number of simulated datasets from topologies with distinct levels of complexity, various sample size and different rates of errors in the data. Among the main results, we show that the introduction of Suppes' constraints dramatically improve the inference accuracy, by reducing the solution space and providing a temporal ordering on the variables. We also report on trade-offs among different search techniques that can be efficiently employed in distinct experimental settings. This manuscript is an extended version of the paper "Structural Learning of Probabilistic Graphical Models of Cumulative Phenomena" presented at the 2018 International Conference on Computational Science. [1].


Keywords: Graphical Models, Structural Learning, Causality, Suppes-Bayes Causal Networks, Cumulative Phenomena

## 1. Introduction

Bayesian Networks (BNs) are probabilistic graphical models representing the relations of conditional dependence among random variables, encoded in directed acyclic graphs (DAGs) [2]. In

the last decades, BNs have been effectively applied in several different fields and disciplines, such as (but not limited to) diagnostics and predictive analytics [2].

One of the most challenging task with BNs is that of learning their structure from data. Two main approaches are commonly used to tackle this problem.

1. Constraint-based techniques: mainly due to the works by Judea Pearl [3] and others, these approaches aim at discovering the relations of conditional independence from the data, using them as constraints to learn the network.
2. Score-based techniques: in this case the problem of learning the structure of a BN is defined as an optimization task (specifically, maximization) where the search space of the valid solutions (i.e., all the possible DAGs) is evaluated via scores based on a likelihood function [2].

Regardless of the approach, the main difficulty in this optimization problem is the huge number of valid solutions in the search space, namely, all the possible DAGs, which makes this task a known $N P$-hard one in its most general instance, and even when constraining each node to have at most two parents $[4,5]$. Therefore, all state-of-the-art techniques solve this task by means of meta-heuristics $[2,6,7]$.

Moreover, the inference is further complicated by the well-known issue of $I$-equivalence: BNs with even very different structures can encode the same set of conditional independence properties[2]. Thus, any algorithm for structural learning can converge to a set of equivalent structures rather than to the correct one, given that the inference itself is performed by learning the statistical relations among the variables emerging from their induced distributions rather than the structure itself $[2]$.

In this paper, we investigate the application of BNs for the characterization of a specific class of dynamical phenomena, i.e., those driven by the monotonic accumulation of events. In particular, the process being modeled/observed must imply:

1. a temporal ordering among its events (i.e., the nodes in the BN), and
2. a monotonic accumulation over time, which probabilistically entails that the occurrence of an earlier event must be positively correlated to the subsequent occurrence of its successors, leading to a significant temporal pattern [8].

An example can be found in the dynamics of cascading failures, that is a failure in a system of interconnected parts where the failure of a part can trigger the failure of successive parts. These

phenomenon can happen in different contexts, such as power transmission, computer networking, finance and biological systems. In these scenarios, different configurations may lead to failure, but some of them are more likely than others and, hence, can be modeled probabilistically [9].

The two particular conditions mentioned above can be very well modelled by the notion of probabilistic causation by Patrick Suppes [10, 11], and allow us to define a set of structural constraints to the BNs to be inferred, which, accordingly, have been dubbed as Suppes-Bayes Causal Networks (SBCNs) in previous works [12, 8]. SBCNs have been already applied in a number of different fields, ranging from cancer progression inference $[13,14,15]$ to social discrimination discovery [12] and stress testing [16].

We specifically position our work within the aforementioned optimization-based framework for BN structure learning. The goal of this paper is to investigate how structure learning is influenced by different algorithmic choices, when representing cumulative dynamical phenomena. In particular, it is known that given a temporal ordering on the variables (i.e., a partially ordered set among the events, poset in the terminology of Bayesian networks) of a BN, finding the optimal solution that is consistent with the ordering can be accomplished in time $O\left(n^{k}\right)$, where $n$ is the number of variables and $k$ the bounded in-degree of a node [17, 18]. Thus, the search in the space of orderings can be performed way more efficiently than the search in the space of structures, as the search space is much smaller, the branching factor is lower and acyclicity checks are not necessary [7, 19].

The determination of the right ordering ordering.in complex dynamical phenomena is generally a difficult task, which often requires considerable domain knowledge. However, the representation of cumulative phenomena via SBCNs allows one to overcome this hurdle, as Suppes' constraints dramatically reduce the search space of valid solutions, also providing a temporal ordering on the variables. This represents a serious theoretical advancement in structure learning of BNs for the modeling of cumulative phenomena, which we investigate in this work with a series of synthetic experiments.

In particular, in this paper we quantitatively assess the performance of learning the structure of a BN when:

- the temporal ordering among variables is given / not given, i.e., when Suppes' constraints are imposed / not imposed (in the former case we deal with SBCNs);
- different heuristic search strategies are adopted, i.e., Hill Climbing (HC), Tabu Search (TS),

and Genetic Algorithms (GA);

- different regularization terms are used, i.e., Bayesian Information Criterion (BIC) and Akaike information criterion (AIC).


# 2. Background 

In this Section we provide an introduction to Bayesian networks together with a review of some state-of-the-art methods to tackle to problem of learning their structures from a set of observations $D$ over the variables described in the network.

### 2.1. Bayesian Graphical Models

A Bayesian network is a statistical graphical model that succinctly represents a joint distribution over $n$ random variables and encodes it in a directed acyclic graph $G=(V, E)$ over the $n$ nodes $V$ referring to the variables and their relations $E$ (arcs in the DAG). Given the structure of a BN, the full joint distribution of the $n$ variables can be written as the product of the conditional distributions on each variable. In fact, an edge between pair of nodes, e.g., $A$ and $B$, denotes statistical dependence, i.e., $\operatorname{Pr}(A \wedge B) \neq \operatorname{Pr}(A) \operatorname{Pr}(B)$, regardless of which any other variables we condition on, that is, for any other set of variables $\mathcal{C}$ it holds that [2]

$$
\operatorname{Pr}(A \wedge B \mid \mathcal{C}) \neq \operatorname{Pr}(A \mid \mathcal{C}) \cdot \operatorname{Pr}(B \mid \mathcal{C})
$$

In such a DAG, the set of variables connected toward any node $X$ determines its set of "parent" nodes $\pi(X)$. Moreover, the joint distribution over all the variables can be written as $\prod_{X} \operatorname{Pr}(X \mid \pi(X))$, where, if a node has no incoming edges (i.e., no parents), in the product we use its marginal probability $\operatorname{Pr}(X)$. Thus, to compute the probability of any combination of values over the variables, only the conditional probabilities of each variable given its parents must be parameterized. However, even in the simplest case of binary variables, the number of parameters in each conditional probability table is locally of exponential size: namely, $2^{|\pi(X)|}-1$. Thus, the total number of parameters needed to compute the full joint distribution is of size $\sum_{X} 2^{|\pi(X)|}-1$, which is considerably less than $2^{n}-1$ for sparse networks.

A useful property of the graphical structure is that we can define, for each variable, a set of nodes called the Markov blanket such that, conditioned on it, this variable is independent of all the

other variables in the network. It can be proven that, for any BN, the Markov blanket consists of a node's parents, its children and the parents of the children [2].

We also point out that the usage of the symmetrical notion of conditional dependence introduces important limitations in the task of learning the structure of a BN. As a matter of fact, we note that the two edges $A \rightarrow B$ and $B \rightarrow A$ denote equivalent dependence between $A$ and $B$. Hence, two graphs having a different structure can model an identical set of independence and conditional independence relations (I-equivalence). This yields to the notion of Markov equivalence class as a partially directed acyclic graph, in which the edges that can take either orientation are left undirected. It is also known that two BNs are Markov equivalent when they have the same skeleton and the same $v$-structures, the former being the set of edges, ignoring their direction (e.g., $A \rightarrow B$ and $B \rightarrow A$ constitute a unique edge in the skeleton) and the latter being all the edge structures in which a variable has at least two parents, but those do not share an edge (e.g., $A \rightarrow B \leftarrow C$ ) [20].

BNs have an interesting relation to canonical boolean logical operators $\wedge, \vee$ and $\oplus$ and formulas over variables $[21,8]$. In fact these formulas, which are "deterministic" in principle, in BNs are naturally softened into probabilistic relations to allow some degree of uncertainty or noise. This probabilistic approach to modeling logic allows representation of qualitative relationships among variables in a way that is inherently robust to small perturbations by noise. For instance, the phrase "in order to hear music when listening to an mp3, it is necessary and sufficient that the power is on and the headphones are plugged in" can be represented by a probabilistic conjunctive formulation that relates power, headphones and music, in which the probability that music is audible depends only on whether power and headphones are present. On the other hand, there is a small probability that the music will still not play (perhaps we forgot to load any songs into the device) even if both power and headphones are on, and there is small probability that we will hear music even without power or headphone (perhaps we are next to a concert and overhear that music) [21, 22].

# 2.2. Approaches to Learning the Structure of a BN 

In the the literature, there have been two initial families of methods aimed at learning the structure of a BN from data. The methods belonging to the first family aim to explicitly capture all the conditional independence relations encoded in the edges, and will be referred to as constraint based approaches (2.2.1). The second family, that of score based approaches (2.2.2), aims at the selection of a model that maximizes the likelihood of the data given the model. Since both approaches

lead to intractability ( $N P$-hardness) [4, 5], computing and verifying an exact solution is impractical. For this reason, heuristic methods like Hill Climbing [23], Tabu Search [24], Simulated Annealing [25] and Genetic Algorithms [26, 27] are generally employed. These algorithms are characterized by a polynomial complexity, although they only provide asymptotic guarantees of converging to optimal solutions.

Recently, a third class of learning algorithms that takes advantage of specialized logical relations (mentioned in the previous section) have been introduced (2.2.3). In the rest of this section we describe in detail some of these approaches, leaving to specific readings more detailed discussions $[2,21,22]$.

# 2.2.1. Constraint-based Approaches 

We briefly present an intuitive explanation of several common algorithms used for structure discovery by explicitly considering conditional independence relations between variables. For more detailed explanations and analyses of complexity, correctness and stability, we refer the reader to the related references $[28,29]$.

The basic idea behind this class of algorithms is to build a graph structure reflecting the independence relations in the observed data, thus matching as closely as possible the empirical distribution. The difficulty in this approach lies in the number of conditional pairwise independence tests that an algorithm would have to perform to test all possible relations. This number is indeed exponential, requiring to condition on a power set, when testing for the conditional independence between two variables. Because of this inherent intractability, this class of algorithms requires the introduction of some approximations.

### 2.2.2. Score-based Approaches

These approaches to structural learning aim to maximize the likelihood of a set of observed data. Since we assume that the data are independent and identically distributed, the likelihood of the data $\mathcal{L}(\cdot)$ is simply the product of the probability of each observation. That is,

$$
\mathcal{L}(D)=\prod_{d \in D} \operatorname{Pr}(d)
$$

for a set of observations $D$. Since we want to infer a model $\mathcal{G}$ that best explains the observed data, we define the likelihood of observing the data given a specific model $\mathcal{G}$ as:

$$
\mathcal{L L}(\mathcal{G}, D)=\prod_{d \in D} \operatorname{Pr}(d \mid \mathcal{G})
$$

However, the actual likelihood is never used in practice, as this quantity rapidly becomes very small and impossible to represent in a computer. Instead, the logarithm of the likelihood function is usually adopted for three reasons: (i) the $\log (\cdot)$ function is monotonic; (ii) log-likelihood mitigates the numerical issues caused by normal likelihood; (iii) it is easy to compute, because the logarithm of a product is equal to the sum of the logs (e.g., $\log (x y)=\log x+\log y)$, and the likelihood for a Bayesian network is a product of simple terms [2].

Practically, however, there is a problem in learning the network structure by maximizing loglikelihood alone. Namely, for any arbitrary set of data, the most likely graph is always the fully connected one (i.e., all edges are present), since adding an edge can only increase the likelihood of the data. To overcome this limitation, log-likelihood is almost always supplemented with a regularization term that penalizes the complexity of the model. There is a plethora of regularization terms, some based on information theory and others on Bayesian statistics (see [30] and references therein), which all serve to promote sparsity in the learned graph structure, though different regularization terms are better suited for particular applications [2, 22].

# 2.2.3. Learning Logically Constrained Networks 

In Section 2.1, we noted that an important class of BNs captures common binary logical operators, such as $\wedge, \vee$, and $\oplus$. Although the learning algorithms mentioned above can be used to infer the structure of such networks, some algorithms employ knowledge of these logical constraints in the learning process.

A widespread approach for the learning of monotonic progression networks with a directed acyclic graph (DAG) structure and conjunctive events are Conjunctive Bayesian Networks (see CBNs, [31]). This approach was originally adopted to model cancer progression in terms of accumulation of drivers genes [14, 15], in a way closely related to the model we discuss in this work.

This model is a standard BN over Bernoulli random variables with the constraint that the probability of a node $X$ taking the value 1 is zero if at least one of its parents has value 0 . This defines a conjunctive relationship, in that all the parents of $X$ must be 1 for $X$ to possibly be 1 .

Thus, this model alone cannot represent noise, which is an essential part of any real data. In response to this, hidden $C B N s$ [32] were developed by augmenting the set of variables: a correspondence to a new variable $Y$ that represents the observed state is assigned to each CBN variable $X$, which captures the "true" state. Thus, each new variable $Y$ takes the value of the corresponding variable $X$ with a high probability, and the opposite value with a low probability, in order to model noise observations. In this model, the variables $X$ are latent, i.e., they are not present in the observed data, and have to be inferred from the observed values for the new variables.

# 3. Inference of Causal Networks 

In this Section we present the foundations of our framework and, specifically, we define the main characteristics of the SBCNs and of some heuristic strategies for the likelihood fit. Without losing in generality, from now on, we consider a simplified formulation of the problem of learning the structure of BNs where all the variables depicted in the graph are Bernoulli random variables, i.e., their support is $(0,1)$. All the conclusions derived in these settings can be also directly applied to the general case where the nodes in the BN describe geneal random variables [2].

More precisely, we consider as an input for our learning task a dataset $D$ of $n$ Bernoulli variables and $m$ cross-sectional samples. We assume the value 1 to indicate that a given variable has been observed in the sample and 0 that the variable had not been observed.

### 3.1. Suppes-Bayes Causal Networks

In [10], Suppes introduced the notion of prima facie causation. A prima facie relation between a cause $u$ and its effect $v$ is verified when the following two conditions are true.

1. Temporal Priority (TP): any cause happens before its effect.
2. Probability Raising (PR): the presence of the cause raises the probability of observing its effect.

Definition 1 (Probabilistic Causation, [10]). For any two events $u$ and $v$, occurring respectively at times $t_{u}$ and $t_{v}$, under the mild assumptions that $0<\operatorname{Pr}(u), \operatorname{Pr}(v)<1$, the event $u$ is called a prima facie cause of $v$ if it occurs before and raises the probability of $u$, i.e.,

$$
\begin{cases}(\mathrm{TP}) & t_{u}<t_{v} \\ (\mathrm{PR}) & \operatorname{Pr}(v \mid u)>\operatorname{Pr}(v \mid \neg u)\end{cases}
$$

The notion of prima facie causality has known limitations in the context of the general theories of causality [11], however, this characterization seems to appropriate to model the dynamics of phenomena driven by the monotonic accumulation of events where a temporal order among them is implied and, thus, the occurrence of an early event positively correlates to the subsequent occurrence in time of a later one. Let us now refer again to systems where cascading failure may occur: some configurations of events, in a specific order, may be more likely to cause a failure than others. This condition leads to the emergence of an observable temporal pattern among the events captured by Suppes' definition of causality in terms of statistical relevance, i.e., statistical dependency.

Let us now consider a graphical representation of the aforementioned dynamics in terms of a $\mathrm{BN} G=(V, E)$. Furthermore, let us consider a given node $v_{i} \in V$ and let us name $\pi\left(v_{i}\right)$ the set of all the nodes in $V$ pointing to (and yet temporally preceding) $v_{i}$. Then, the joint probability distribution of the $n=|V|$ variables induced by the BN can be written as:

$$
\operatorname{Pr}\left(v_{I}, \ldots, v_{n}\right)=\prod_{v_{i} \in V} \operatorname{Pr}\left(v_{i} \mid \pi\left(v_{i}\right)\right)
$$

When building our model, we need to constrain the characteristics of the considered relations as depicted in the network (i.e., the arcs in the graph), in order to account for the cumulative process above mentioned, which, in turns, needs to be reflected in its induced probability distribution [8]. To this extent, we can define a class of BNs over Bernoulli random variables named Monotonic Progression Networks (MPNs) [8, 21, 33]. Intuitively, MPNs represent the progression of events monotonically ${ }^{1}$ accumulating over time, where the conditions for any event to happen is described by a probabilistic version of the canonical boolean operators, i.e., conjunction ( $\wedge$ ), inclusive disjunction $(\vee)$, and exclusive disjunction $(\oplus)$.

MPNs can model accumulative phenomena in a probabilistic fashion, i.e., they are also modeling irregularities (noise) in the data as a small probability $\varepsilon$ of not observing later events given their predecessors.

Given these premises, in [14] the authors describe an efficient algorithm (named CAPRI, see [14] for details) to learn the structure of constrained Bayesian networks which account for Suppes' criteria and which later on are dubbed Suppes-Bayes Causal Networks (SBCNs) in [12]. SBCNs are well suited to model cumulative phenomena as they may encode irregularities in a similar way

[^0]
[^0]:    ${ }^{1}$ The events accumulate over time and when later events occur, earlier events are observed as well.

to MPNs [8]. The efficient inference schema of [8] relies on the observation (see [7]) that a way for circumventing the intrinsic computational complexity of the task of learning the structure of a Bayesian Network is to postulate a pre-determined ordering among the nodes. Intuitively, CAPRI exploits Suppes' theory to first mine an ordering among the nodes, reducing the complexity of the problem, and then fits the network by means of likelihood maximization. In [8] it is also shown that a SBCN, learned using CAPRI, can also embed the notion of accumulation through time as defined in a MPN, and, specifically, conjunctive parent sets; nevertheless SBCNs can easily be generalized to represent all the canonical boolean operators (Extended Suppes-Bayes Causal Networks), notwithstanding an increase of the algorithmic complexity [8]. We refer the reader to [8] for further details and, following [12], we now formally define a SBCN.

Definition 2 (Suppes-Bayes Causal Network). Given an input cross-sectional dataset $D$ of $n$ Bernoulli variables and $m$ samples, the Suppes-Bayes Causal Network $S B C N=(V, E)$ subsumed by $D$ is a directed acyclic graph such that the following requirements hold:

1. [Suppes' constraints] for each $\operatorname{arc}(u \rightarrow v) \in E$ involving the selective advantage relation between nodes $u, v \in V$, under the mild assumptions that $0<\operatorname{Pr}(u), \operatorname{Pr}(v)<1$ :

$$
\operatorname{Pr}(u)>\operatorname{Pr}(v) \quad \text { and } \quad \operatorname{Pr}(v \mid u)>\operatorname{Pr}(v \mid \neg u)
$$

2. [Simplification] let $E^{\prime}$ be the set of arcs satisfying the Suppes' constraints as before; among all the subsets of $E^{\prime}$, the set of $\operatorname{arcs} E$ is the one whose corresponding graph maximizes the log-likelihood $\mathcal{L} \mathcal{L}$ of the data and the adopted regularization function $R(f)$ :

$$
E=\underset{E \subseteq E^{\prime}, G=(V, E)}{\arg \max } \mathcal{L} \mathcal{L}(G, D)-R(f)
$$

Before moving on, we once again notice that the efficient implementation of Suppes' constraints of CAPRI does not, in general, guarantee to converge to the monotonic progression networks as depicted before. To overcome this limitation, one could extend the Algorithm in order to learn, in addition to the network structure, also the logical relations involving any parent set, increasing the overall computational complexity. Once again, we refer the interested reader to the discussions provided in $[14,8]$ and, without losing in generality, for the purpose of this work, we consider the efficient implementation of CAPRI presented in [14].

It is important to remark that the evaluation of Suppes' constraints might be extended to longer serial dependence relations, by assessing, for instance, the statistical dependency involving more

than two events. We here decide to evaluate pairwise conditions to keep the overall computational complexity at a minimum. However, we leave the investigation of this issue to further development of the framework.

# 3.2. Optimization and Evolutionary Computation 

The problem of the inference of SBCNs can be re-stated as an optimization problem, in which the goal is the maximization of a likelihood score. Regardless of the strategy used in the inference process, the huge size of the search space of valid solutions makes this problem very hard to solve. Moreover, as stated above, the general problem of learning the structure of a BN is $N P$-hard $[5]^{2}$. Because of that, state-of-the-art techniques largely rely on heuristics [2], often based on stochastic global optimization methods like Genetic Algorithms (GAs) [6, 8]. Methods for BN learning can roughly be subdivided into two categories: single individual or population-based meta-heuristics.

Hill Climbing (HC) and Tabu Search (TS) both belong to the first category. The former is a greedy approach for the structural learning of BNs, in which new edges are attached to the current putative solution as long as they increase the likelihood score and they do not introduce any cycles in the network. TS is a stochastic variant of HC able to escape local minima, in which solutions visited in the past are not repeated by means of a tabu list.

GAs [34], a global search methodology inspired by the mechanisms of natural selection, belong to the second category. GAs were shown to be effective for BN learning, both in the case of available and not available a priori knowledge about nodes' ordering [6, 8]. In a GA, a population $\mathfrak{P}$ of candidate solutions (named individuals) iteratively evolves, converging towards the global optimum of a given fitness function $f$ that, in this context, corresponds to the score to be maximized. The population $\mathfrak{P}$ is composed of $Q$ randomly created individuals, usually represented as fixedlength strings over a finite alphabet. These strings encode putative solutions of the problem under investigation; in the case of BN learning, individuals represent linearized adjacency matrices of candidate BNs with $K$ nodes, encoded as string of binary values whose length ${ }^{3}$ is $O\left(K^{2}\right)$.

[^0]
[^0]:    ${ }^{2}$ We are aware of special formulations of the problem that are solvable in polynomial time. Their existence points to interesting questions regarding the "barrier" between $N P$ problems and polynomial ones; however, these are questions beyond the scope of the present paper.
    ${ }^{3}$ Since BNs are DAGs, the representation can be reduced by not encoding the elements on the diagonal, which are always equal to zero. In such case, the strings representing the individual have length $K \times K-K$.

The individuals in $\mathfrak{P}$ undergo an iterative process whereby three genetic operators-selection, crossover and mutation-are applied in sequence to simulate the evolutionary recombination process, which results in a new population of possibly improved solutions. During the selection process, individuals from $\mathfrak{P}$ are chosen, using a fitness-dependent sampling procedure [35], and are inserted into a new temporary population $\mathfrak{P}^{\prime}$. In this work we assume a ranking selection: individuals are ranked according to their fitness values and the probability of selecting an individual is proportional to its position in the ranking. The crossover operator is then used to recombine the structures of two promising selected parents. We assume a single point crossover, in which the two strings encoded by the two parents are "cut" in the same random position and one of the resulting substrings is exchanged. Finally, the mutation operator replaces an arbitrary symbol of an offspring, with a probability $\mathcal{P}_{m}$, using a random symbol taken from the alphabet. In the case of BNs, the mutation consists in flipping a single bit of the individual according to the specified probability. It is worth noting that in the case of ordered nodes both crossover and mutation are closed operators, because the resulting offsprings always encode valid DAGs. To the aim of ensuring a consistent population of individuals throughout the generations, in the case of unordered nodes the two operators are followed by a correction procedure, in which the candidate BN is analyzed to identify the presence of invalid cycles. For further information about our implementation of GAs for the inference of BNs, including the correction phase, we refer the interested reader to [8].

# 4. Results 

We now discuss the results of a large number of experiments we conducted on simulated data, with the aim of assessing the performance of the state-of-the-art score-based techniques for the BN structure inference, and comparing the performance of these methods with the learning scheme defined in CAPRI.

Our main objective is to investigate how the performance is affected by different algorithmic choices at the different steps of the learning process.

Data Generation.. All simulations are performed with the following generative models. We consider 6 different topological structures.

1. Trees: one predecessor at most for any node, one unique root (i.e., a node with no parents).
2. Forests: likewise, more than one possible root.

3. Conjunctive DAGs with single root: 3 predecessors at most for each node, all the confluences are ruled by logical conjunctions, one unique root.
4. Conjunctive DAGs with multiple roots: likewise, possible multiple roots.
5. Disjunctive DAGs with single root: 3 predecessors at most for each node, all the confluences are ruled by logical disjunctions, one unique root.
6. Disjunctive DAGs with multiple roots: likewise, possible multiple roots.

We constrain the induced distribution of each generative structure by implying a cumulative model for either conjunctions or disjunctions, i.e., any child node cannot occur if its parent set is not activated as described for the MPN in the Method Section 3. For each of these configurations, we generate 100 random structures. Furthermore, we simulate a model of noise in terms of random observations (i.e., false positives and false negatives) included in the generated datasets with different rates.

These data generation configurations are chosen to reflect: (a) different structural complexities of the models in terms of number of parameters, i.e., arcs, to be learned, (b) different types of induced distributions suitable to model cumulative phenomena as defined by the MPNs (see Section 3.1), i.e., conjunction $(\wedge)$ or inclusive disjunction $(\vee)^{4}$ and, $(c)$ situations of reduced sample sizes and noisy data.

We here provide an example of data generation. Let now $n$ be the number of nodes we want to include in the network and let us set $p_{\min }=0.05$ and $p_{\max }=0.95$ as the minimum and maximum probabilities of any node. A directed acyclic graph without disconnected components (i.e., an instance of types (3) and (5) topologies) with maximum depth $\log n$ and where each node has at most $w^{*}=3$ parents is generated.

Performance Assessment.. In all these configurations, the performance is assessed in terms of:

- accuracy $=\frac{(T P+T N)}{(T P+T N+F P+F N)}$;
- sensitivity $=\frac{T P}{(T P+F N)}$;
- specificity $=\frac{T N}{(F P+T N)}$;

[^0]
[^0]:    ${ }^{4}$ Here we stick with the efficient search scheme of CAPRI and, for this reason, we do not consider exclusive disjunction $(\oplus)$ parent sets

```
Algorithm 1: Data generation: single source directed acyclic graphs
    Input: \(n\), the number of nodes of the graph, \(p_{\min }=0.05\) and \(p_{\max }=0.95\) be the minimum
        and maximum probabilities of any node and \(w^{*}=3\) the maximum incoming edges
        per node.
    Result: a randomly generated single source directed acyclic graph.
    Pick an event \(r \in G\) as the root of the directed acyclic graph;
    Assign to each node \(u \neq r\) an integer in the interval \([2,\lceil\log n\rceil]\) representing its depth in the
        graph ( 1 is reserved for \(r\) ), ensuring that each level has at least one node;
    forall nodes \(u \neq r\) do
        Let \(l\) be the level assigned to the node;
        \(\operatorname{Pick}\left|\operatorname{Pr}(u)\right|\) uniformly over \(\left(0, w^{*}\right]\), and accordingly define the parents of \(u\) with events
            selected among those at which level \(l-1\) was assigned;
    end
    Assign \(\operatorname{Pr}(r)\), a random value in the interval \(\left[p_{\min }, p_{\max }\right]\);
    forall events \(u \neq r\) do
        Let \(\alpha\) be a random value in the interval \(\left[p_{\min }, p_{\max }\right]\);
        Let \(\pi(u)\) be the direct predecessor of \(u\);
        Then assign:
```

```
\(\operatorname{Pr}(u)=\alpha \operatorname{Pr}(x \in \pi(u))\);
```

12 end
13 return The generated single source directed acyclic graph.
with $T P$ and $F P$ being the true and false positives (we mark as positive any arc that is present in the network) and $T N$ and $F N$ being the true and false negatives (we mark negative any arc that is not present in the network) with respect to the generative model. All these measures are values in $[0,1]$ with results close to 1 indicators of good performance.

Implementation.. In all the following experiments, the adopted likelihood functions (i.e., the fitness evaluations) are implemented using the bnlearn package [36] written in the R language, while GA [34] the inspyred [37], networkx [38] and numpy [39] packages.

The framework for the inference of SBCNs is implemented in R and is available in the TRONCO

suite for TRanslational ONCOlogy [40, 41]. TRONCO is available under a GPL3 license at its webpage: https://sites.google.com/site/troncopackage or on Bioconductor.

Algorithm Settings.. We test the performance of classical search strategies, such as Hill Climbing (HC) and Tabu Search (TS), and of more sophisticated algorithms such Genetic Algorithms (GA) ${ }^{5}$.

For HC and TS, we generate data as described above with networks of 10 and 15 nodes (i.e., $0 / 1$ Bernoulli random variables). We generated 10 independent datasets for each combination of the 4 sample levels (i.e., $50,100,150$ and 200 samples) and the 9 noise levels (i.e., from $0 \%$ to $20 \%$ with step $2.5 \%$ ) for a total of $4,320,000$ independent datasets. The experiments were repeated either $(i)$ including or (ii) not including the Suppes' constraints described in CAPRI [14], and independently using 5 distinct optimization scores and regularizators, namely standard (i) log-likelihood [2], (ii) AIC [42], (iii) BIC [43], (iv) BDE [44] and (v) K2 [45], leading to a final number of $86,400,000$ different configurations.

Being more precise, given an input dataset of observations $D$ and a graphical model $G$, we can define a function to evaluate the goodness of this structure given the data:

$$
f(G, D)=\mathcal{L} \mathcal{L}(D \mid G)-\mathcal{R}(G)
$$

where $\mathcal{L} \mathcal{L}(\cdot)$ is the log-likelihood, while $\mathcal{R}(\cdot)$ is a regularization term with the aim of limiting the complexity of $G$. The DAG induced by $G$ in fact defines a probability distribution over its nodes, namely $\left\{x_{1}, \ldots, x_{n}\right\}$ :

$$
\begin{gathered}
\operatorname{Pr}\left(x_{1}, \ldots, x_{n}\right)=\prod_{x_{i}=1}^{n} \operatorname{Pr}\left(x_{i} \mid \pi_{i}\right) \\
\operatorname{Pr}\left(x_{i} \mid \pi_{i}\right)=\boldsymbol{\theta}_{x_{i} \mid \pi_{i}}
\end{gathered}
$$

where $\pi_{i}=\left\{x_{j} \mid x_{j} \rightarrow x_{i} \in G\right\}$ are $x_{i}$ 's parents in the DAG, and $\boldsymbol{\theta}_{x_{i} \mid \pi\left(x_{i}\right)}$ is a density function. Then, the log-likelihood of the graph can be defined as:

$$
L L(D \mid G)=\log \operatorname{Pr}(D \mid G, \boldsymbol{\theta})
$$

[^0]
[^0]:    ${ }^{5}$ Further experiments on multi-objective optimization techniques, such as Non-dominated Sorting Genetic Algorithm (NSGA- II), were performed, but are not shown here because of the worse overall performance, and of the higher computational cost, with respect to canonical GA.

Then, the regularization term $\mathcal{R}(G)$ introduces a penalty for the number of parameters in the model $G$ also considering the size of the data. The above mentioned scores that we considered differ in this penalty, with AIC and BIC being Information-theoretic score and BDE and K2, Bayesian scores [30].

While a detailed description of these regularizators is beyond the scope of this paper, we critically discuss the different performances granted by each strategy for the inference of BNs.

With respect to GA we used a restricted data generation settings, using networks of 15 nodes, datasets of 100 samples and 5 noise levels (from $0 \%$ to $20 \%$ with step $5 \%$ ) for a total of 3,000 independent datasets. We tested the GA either $(i)$ with or $(i i)$ without Suppes' constraints, using BIC regularization term, leading to the final total of 6,000 different configurations. Finally, the GA was launched with a population size of 32 individuals, a mutation rate of $p_{m}=0.01$ and 100 generations.

We summarize the performance evaluation of the distinct techniques and settings in the next Subsections and in Figures 1, 2, 3 and 4.
![img-0.jpeg](img-0.jpeg)

Figure 1: Performance in terms of accuracy for the 6 considered structures with 15 nodes, noise levels from $0 \%$ to $20 \%$ with step $2.5 \%$ and sample sizes of $50,100,150$ and 200 samples. Here we use BIC as a regularization scheme and we consider HC as a search stategy both for the classical case and when Suppes' priors are applied.

![img-1.jpeg](img-1.jpeg)

Figure 2: Performance in terms of accuracy for directed acyclic graphs with multiple sources and disjunctive parents (structure vi) of 15 nodes, noise levels from $0 \%$ to $20 \%$ with step $2.5 \%$ and sample sizes of $50,100,150$ and 200 samples. Here we consider HC as a search strategy both for the classical case and when Suppes' priors are applied and we show the results for all five regularizators introduced in the text.

# Performance Assessment 

By looking at Figure 1, one can first appreciate the variation of accuracy with respect to a specific search strategy, i.e., HC with BIC, which is taken as an example of typical behavior. In brief, the overall performance worsens with respect to: $(i)$ a larger number of nodes in the network, $(i)$ more complex generative structures, and (iii) smaller samples sizes / higher noise rates. Although such a trend is intuitively expected, given the larger number of parameters to be learned for more complex models, we here underline the role of statistical complications, such as the presence of spurious correlations [46] and the occurrence of Simpson's paradox [47].

For instance, it is interesting to observe a typical decrease of the accuracy when we compare topologies with the same properties, but different number of roots (i.e., 1 root vs. multiple roots). In the former case, we expect, in fact, a lower number of arcs (i.e., dependencies) to be learned (on average) and, hence, we may attribute the decrease of the performance to the emergence of

spurious correlations among independent nodes, such as the children of the different sources of the DAG. This is due to the fact that, when sample sizes are not infinite, it is very unlikely to observe perfect independence and, accordingly, the likelihood scores may lead to overfitting. The trends displayed in Figure 1 are shared by most of the analyzed search strategies.

Role of the Regularization Term.. By looking at Figure 2 one can first notice that the accuracy with no regularization is dramatically lower than the other cases, as a consequence of the expected overfitting (in this case we compare the performance of HC on disjunctive DAGs with multiple roots, but the trend is maintained in the other cases). Conversely, all regularization terms ensure the inference of sparser models, by penalizing the number of retrieved arcs. BDE regularization term seems to be the only exception (see Figure 2), leading to unintuitive behaviors: in fact, while for all the other methods the performance decreases when higher level of noise are applied, for BDE the accuracy seems to improve with higher noise rates. This result might be explained by observing that given a topological structure, structural spurious correlations may arise between a given node and any of its undirected predecessors (i.e., one of the predecessors of its direct parents): with higher error rates, and, accordingly, more random samples in the datasets, all the correlations are reduced, hence leading to a lower impact of the regularization term. Given these considerations, one can hypothesize that the overall trend of BDE is due to a scarce penalization to the likelihood fit, favoring dense networks rather than sparse ones.

Search Strategies.. No significant differences in the performance between the accuracy of HC, TS and GA are observed. However, one can observe a consistent improvement in sensitivity when using GA (see Figures 3 and 4). This suggests different inherent properties of the search schemes: while with HC and TB the regularization terms, rather than the search strategy, account for most of the inference performance, GAs are capable of returning denser networks with better hit rates. This is probably due to GA's random mutations, which allow jumps into areas of the search space characterized by excellent fitness, which could not be reached by means of greedy approaches like HC.

Suppes' Structural Constraints.. Finally, the most important result, which can be observed across all the different experiments, is that the overall performance of all the considered search strategies is dramatically enhanced by the introduction of Suppes' structural constraints. In particular, as

one can see, e.g., in Figure 1, there is a constant improvement in the inference, up to $10 \%$, when Suppes' priors are used. Even though the accuracy of the inference is affected by the noise in the observations, in fact, the results with Suppes' priors are consistently better than the inference with no constraints, with respect to all the considered inference settings and to all the performance measures. This is an extremely important result as it proves that the introduction of structural constraints based on Suppes' probabilistic causation indeed simplify the optimization task, by reducing the huge search space, when dealing with BNs describing cumulative phenomena.

# 5. Conclusion 

In this paper we investigated the structure learning of Bayesian Networks aimed at modeling phenomena driven by the monotonic accumulation of events over time. To this end, we made use of a subclass of constrained Bayesian networks named Suppes-Bayes Causal Networks, which include structural constraints grounded in Suppes' theory of probabilistic causation.

While the problem of learning the structure of a Bayesian Network is known to be intractable, such constraints allow to prune the search space of the possible solutions, leading to a tremendous reduction of the number of valid networks to be considered, hence taming the complexity of the problem in a remarkable way.

We here discussed the theoretical implications of the inference process at the different steps, also by comparing various state-of-the-art algorithmic approaches and regularization methods. We finally provided an in-depth study on realistically simulated data of the effect of each inference choice, thus providing some sound guidelines for the design of efficient algorithms for the inference of models of cumulative phenomena.

According to our results, none of the tested search strategies significantly outperforms the others in all the experimental settings, in terms of both sensitivity and specificity.

Yet, we could prove that Suppes' constraints consistently improve the inference accuracy, in all the considered scenarios and with all the inference schemes, hence positioning SBCNs as the new benchmark in the the efficient inference and representation of cumulative phenomena.

## Acknowledgments.

This work was supported in part by the ASTIL Program of Regione Lombardia, by the ELIXIRITA network, and by the SysBioNet project, a MIUR initiative for the Italian Roadmap of European

Strategy Forum on Research Infrastructures (ESFRI). We would like to thank for the useful discussions our colleagues Giulio Caravagna of ICR, London, UK, Giancarlo Mauri of DISCo, Università degli Studi di Milano-Bicocca, Milan, Italy, and Bud Mishra of Courant Institute of Mathematical Sciences, New York University, NY, USA.

![img-2.jpeg](img-2.jpeg)

Figure 3: Performance in terms of accuracy for directed acyclic graphs with multiple sources and disjunctive parents (structure $v i$ ) of 15 nodes, noise levels from $0 \%$ to $20 \%$ with step $2.5 \%$ and sample sizes of $50,100,150$ and 200 samples. Here we use BIC as a regularization scheme and we consider both HC and TB as search strategies for the classical case and when Suppes' priors are applied.

![img-3.jpeg](img-3.jpeg)

Figure 4: Performance of HC, TB and GA, in terms of sensitivity and specificity for forests (panels 1A, 1B), directed acyclic graphs with multiple sources and conjunctive parents (panels 2A, 2B) and directed acyclic graphs with multiple sources and disjunctive parents (panels 3A, 3B) (configurations (ii), (iv) and (vi)) of 15 nodes, noise levels from $0 \%$ to $20 \%$ with step $5 \%$ and sample sizes of 100 samples. Here we use BIC as a regularization scheme for HC and TB, and for all the algorithms we either consider (panels A) or not consider (panels B) Suppes' constraints (SC).
